# Render a style D film page (kit.js + render(t) + DUR) to PNG stills or an MP4. Input: the film's .html; it must sit next to kit.js and fonts/.
"""Render a style D film to stills or to an MP4, in real time order, many pages in parallel.

  uv run --with playwright python render.py film.html --stills 2.5,8,13 --out stills/ [--variant public]
  uv run --with playwright python render.py film.html --video film.mp4 [--variant public] [--workers 6] [--fps 30]
  uv run --with playwright --with pillow python render.py film.html --per-shot [--at end|mid|<seconds>] --out sheet-public

--per-shot empties --out, shoots one still per shot (default: 0.7 s before the shot ends, where everything has
arrived and the camera has finished moving), tiles them into <out>.png, and lists every label the stage edge cuts:
picture text that is partly or wholly outside the visible band. Check the sheet AND that list before any full render.

The page exposes render(t) (seconds) and DUR. Every frame is a pure function of t, so two renders are identical and
frames can be shot by several pages at once. ?v=<variant> is passed to the page: one file holds several cuts.
The run stops with an error if the Outfit font did not load (a fallback font renders silently otherwise).
A full render of a 2-minute film at 1920x1080, 30 fps, 6 workers took about 8-10 minutes on an M-series Mac.
"""
import argparse, asyncio, pathlib, shutil, subprocess, sys


async def open_page(browser, url):
    page = await browser.new_page(viewport={"width": 1920, "height": 1080})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    await page.goto(url)
    await page.evaluate("document.fonts.ready")
    if errors:
        sys.exit("page error: " + errors[0])
    ok = await page.evaluate("document.fonts.check('700 30px Outfit') && [...document.fonts].some(f => f.family.replace(/\"/g,'') === 'Outfit' && f.status === 'loaded')")
    if not ok:
        sys.exit("Outfit did not load: put fonts/ (from the skill's scripts/style-d/fonts) next to the film page")
    return page


# picture text (inside the stage clip) whose box is not fully inside the visible stage band and not fully transparent
CUT_JS = """(() => { const st = document.querySelector('clipPath#stg rect'); if (!st) return [];
  const svg = document.getElementById('v').getBoundingClientRect(), y0 = +st.getAttribute('y') + svg.top, y1 = y0 + +st.getAttribute('height');
  const out = [];
  for (const t of document.querySelectorAll('g[clip-path="url(#stg)"] text')) {
    let op = 1, n = t; while (n && n.getAttribute) { const o = n.getAttribute('opacity'); if (o !== null) op *= +o; n = n.parentNode; }
    if (op < 0.2 || !t.textContent.trim()) continue;
    const r = t.getBoundingClientRect();
    if (r.top < y0 - 1 || r.bottom > y1 + 1 || r.left < svg.left - 1 || r.right > svg.right + 1) out.push(t.textContent.trim());
  }
  return out; })()"""


def tile(paths, dest, cols=4, scale=0.3):
    from PIL import Image
    ims = [Image.open(p) for p in paths]
    w, h = int(ims[0].width * scale), int(ims[0].height * scale)
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * h), (40, 40, 40))
    for k, im in enumerate(ims):
        sheet.paste(im.resize((w, h)), ((k % cols) * w, (k // cols) * h))
    sheet.save(dest)


async def main():
    from playwright.async_api import async_playwright
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page")
    ap.add_argument("--stills", help="comma-separated times in seconds")
    ap.add_argument("--out", default="stills")
    ap.add_argument("--video")
    ap.add_argument("--variant", default="public")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--crf", type=int, default=16)
    ap.add_argument("--per-shot", action="store_true", help="one still per shot + contact sheet + cut-label check")
    ap.add_argument("--at", default="end", help="per-shot time: end (0.7 s before the cut), mid, or seconds into the shot")
    a = ap.parse_args()
    page_path = pathlib.Path(a.page).resolve()
    url = page_path.as_uri() + "?v=" + a.variant
    ffmpeg = shutil.which("ffmpeg") or str(pathlib.Path.home() / ".local/bin/ffmpeg")
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        if a.stills:
            out = pathlib.Path(a.out).resolve()
            out.mkdir(parents=True, exist_ok=True)
            page = await open_page(browser, url)
            for t in [float(x) for x in a.stills.split(",") if x]:
                await page.evaluate(f"render({t})")
                await page.screenshot(path=str(out / f"t{t:06.1f}.png"), type="png")
            print("stills ->", out)
        if a.per_shot:
            out = pathlib.Path(a.out).resolve()
            shutil.rmtree(out, ignore_errors=True)   # stale stills from an earlier timing would join the sheet
            out.mkdir(parents=True)
            page = await open_page(browser, url)
            spans = await page.evaluate("SH.map(s => [s.a, s.b])")
            cut = []
            for i, (s0, s1) in enumerate(spans, 1):
                d = s1 - s0
                u = d - 0.7 if a.at == "end" else d / 2 if a.at == "mid" else min(float(a.at), d - 0.05)
                await page.evaluate(f"render({s0 + u})")
                await page.screenshot(path=str(out / f"shot{i:02d}.png"), type="png")
                cut += [(i, t) for t in await page.evaluate(CUT_JS)]
            sheet = out.parent / (out.name + ".png")
            tile(sorted(out.glob("shot*.png")), sheet)
            print("sheet ->", sheet)
            if cut:
                print("LABELS CUT BY THE STAGE EDGE (fix before rendering):")
                for i, t in cut:
                    print(f"  shot {i}: {t!r}")
            else:
                print("no picture label is cut by the stage edge")
        if a.video:
            frames = page_path.parent / ("frames-" + a.variant)
            shutil.rmtree(frames, ignore_errors=True)
            frames.mkdir()
            page0 = await open_page(browser, url)
            dur = await page0.evaluate("DUR")
            n = int(round(dur * a.fps))
            pages = [page0] + [await open_page(browser, url) for _ in range(a.workers - 1)]

            async def worker(k, page):
                for i in range(k, n, a.workers):
                    await page.evaluate(f"render({i / a.fps})")
                    await page.screenshot(path=str(frames / f"{i:05d}.png"), type="png")

            await asyncio.gather(*(worker(k, pg) for k, pg in enumerate(pages)))
            video = pathlib.Path(a.video).resolve()
            subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", str(frames / "%05d.png"),
                            "-c:v", "libx264", "-crf", str(a.crf), "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                            str(video)], check=True)
            shutil.rmtree(frames, ignore_errors=True)
            print("video ->", video, n, "frames,", round(dur, 1), "s")
        await browser.close()


asyncio.run(main())
