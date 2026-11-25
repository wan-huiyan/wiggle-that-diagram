# Style D: a long silent film (1–3 minutes, one SVG page, words on screen)

Use style D when the ask is a **film**, not a slide loop: a promo or explainer of 1–3 minutes, silent, captioned,
delivered as an MP4 (for a team channel, a README, a talk). Styles A–C make short looping clips that live inside a deck;
style D makes one continuous story of 10–20 shots.

Everything here comes from one build: a promo for two Claude skills that work as one loop, made in three versions over
two days, plus an internal cut using a real client project's lines. The public cut ships as `examples/loop-promo/`.
Read that film's source before writing your own: it is the positive example for every rule below.

## The method, step by step (each step ends with the check that proves it)

1. **Write the story as one hero object travelling through one world.** Pick the object the viewer follows (a draft,
   an order, a ticket). It appears in most shots and changes as the story goes: it slides in, gets stamped, gains its
   figures, rides the loop. The steps of the process are **places** in that world (stations on a track, a ground to
   dig in, a wall to pass through), never slides. Cut hard between shots; move the camera inside them.
   - Why: version 1 was built this way and the owner said it "tells the story more clearly". Version 2 kept the same
     content but used a fixed step rail along the bottom and one titled panel per step; the owner's verdict was that it
     "feels more like an animated slide deck". Version 3 went back to version 1's story with version 2's nicer shapes.
   - Orientation without a rail: a small map of the process in a corner (`mini()`), lit at the current station.
   → Check: say each shot as "the <hero> <verb>s <where>". If a shot is "a panel explaining step N", rewrite it.

2. **Give each idea one shape, and use the same shape every time the idea recurs.** List the 6–9 ideas the film
   shows, then pick a shape per idea from the table below (or invent one with the same logic). Do not reuse one shape
   for different ideas, and do not invent a new metaphor per shot either: variety comes from ideas having different
   shapes, not from shots having different styles.
   - Why: the first version 3 build drew calls, the checklist, people, results, the re-scorer and the stop rule as
     rounded rectangles with text. The owner asked for it to be "less card based" with "more variety in elements".
     Re-drawing each idea as its own object (below) fixed it without changing a word or a timing.
   - **Draw the objects big.** A cold test on a new topic got the shapes right and still looked thin: three small
     people and three tiny plates on a wide dark stage. The main object of a shot should span at least a third of the
     stage width, and picture text should be 20 px or more in the 1920-wide frame (the caption is 50).
   → Check: a contact sheet of one still per shot. If most frames are boxes with text in them, redo step 2; if most
   frames are mostly empty, scale the objects up.

   | Idea | Shape (kit function) | Why it works |
   |---|---|---|
   | a conversation, a call, a recording | voice waveform, bars coloured by who speaks (`wave`) | shows hours of talk without a transcript; colour says whose words |
   | someone's own words | quote pill (`quote`), speech bubble with attribution (`bubble`) | the quote mark says "verbatim"; the line under it says who and when |
   | a profile built from those words | a person assembling from dots that fly out of the waveform (`dotFigure`, `dotTarget`) | the picture *is* the claim: made from their words, nothing else |
   | a list of requirements, a fix list | printed tape with tick boxes, torn edge, coming out of a slot (`tape`) | lists grow, get ticked and get printed by someone; a box does none of that |
   | a score | half dial with a needle and a pass mark (`gauge`) | the needle moving past the mark reads at a glance; bars look like a chart |
   | feedback from a person | sticky note (`sticky`) | feedback gets handed over; a note can fly, stick, pile up |
   | an idea | light bulb on a wire that lights up (`bulb`) | universally read, and "lights up" is the verb |
   | analysis, digging into data | a drill through ground layers, finding a seam, the find rising out (drawn in the example's dig shot; no kit function, because it only fits "dig") | "dig" becomes literal; the find has to come up and be carried to the draft |
   | traceability | thin threads from each figure on the draft to its source file | shows "every figure traced" without a sentence |
   | separation of duties | a wall with a slot; only the finished page goes through (example's verify shot) | shows *why* the checker cannot mark its own work |
   | inspection | magnifying glass sweeping the page (`lens`) | |
   | two independent results agreeing | a balance that levels (`balance`) | "match" becomes a physical event |
   | a condition that must hold | signal lamp, red until it turns green (`lamp`) | two lamps = two conditions; a gate opens when both are green |
   | a repeating process | ring track with stations, the hero riding laps (`track`, `onTrack`) | one lap = one round, without saying it |
   | an automated worker | small robot that takes notes in and prints a list out (`robot`) | |

3. **Write every on-screen word in one place, per cut.** All strings live in `STR.<cut>` (one file, several cuts,
   chosen with `?v=`); captions are 3–8 words, picture labels 1–6. When the film needs a real cut and a public cut,
   follow "Real lines" below.
   Fixed labels that never change between cuts ("fix list", "next round") may stay in the shot code; anything a cut
   would change (a quote, a name, a figure, a date) goes in `STR`.
   → Check: switch `?v=` and look at two stills of the same shot: every line that should differ does.

4. **Build each shot from the kit, with the camera inside the shot.** What the viewer sees at camera scale 1 is
   about x 87–1833 and y 97–825 in the film's own coordinates (the stage band 130–930 on screen, scaled 1.1 around
   (960, 470)); a push to scale s shrinks that window around the focus point. A ring track of radius 300 at the
   centre already puts its top station's label outside it. `cam(scale, focusX, focusY)` around the whole
   picture; a slow push (1.00 → 1.05) or glide while words are read, a pull back before the cut. The picture is
   clipped to the stage band, so a push never covers the header or the caption. `cap()` and `mini()` draw on the
   overlay, which the camera does not move.
   - Why: version 2's first render failed the huashu film gate (no in-shot motion, 78% of frames fully still). Adding a
     camera inside each shot, and nothing else, turned it yellow.
   → Check: stills at the start, middle and end of a shot differ in framing, not only in what has appeared.

5. **Fact-check every real line BEFORE the first full render.** Give a separate agent the complete source files (not
   excerpts) and two questions: is each quoted fragment verbatim at the cited file and line, and does each shot show
   something that actually happened?
   - Why: in the worked example all 118 quoted fragments were real, and six shots still showed things that did not
     happen: a profile "built from two calls" that came from fourteen, a reviewer credited with a catch we made
     ourselves, a slide title that was on no slide, a step that one run never had. True quotes do not make a true
     picture. The check arrived after rendering had started, and two full renders were thrown away.
   → Check: the agent's list is empty, or every item is fixed or recorded as a deliberate choice.

6. **Look at every shot of every cut before rendering.**
   `render.py film.html --per-shot --variant <cut> --out sheet-<cut>` empties the folder (old stills from an earlier
   timing would otherwise join the sheet), shoots one still 0.7 s before each cut, tiles `sheet-<cut>.png`, and lists
   every picture label the stage edge cuts. The cut with the real (longer) strings is the one that overflows.
   - Why the list: a label cut by the frame is easy to miss on a sheet. The worked example's own loop shot hid the
     name of its first station for two versions; the first run of this check also found three more.
   → Check: the cut-label list is empty (a decorative piece drifting off screen is fine; a label is not), and on the
   sheet: no text over text; no text on the paper tape in a colour that vanishes on it; nothing
   cropped by the camera at the end of a shot (a pan that frames the right side cuts the left labels); the caption
   is fully on screen.

7. **Set durations from the words actually drawn.** `node film_beats.js film.html` renders every shot at 14 times in
   node and collects the visible text (a number that animates, like a dial going 1/5, 2/5 … 4/5, counts once), then
   `fit_durs.py beats.<cut>.json` prints the `DURS` array that passes the reading rule, and `pace_check.py` confirms.
   It also prints two advisories per shot: a caption over ~58 characters (it runs off the frame; captions do not
   wrap), and new words arriving less than 2.5 s apart (fine for the rows of one list landing together, not for
   three separate things that each need a read). `fit_durs.py` only lengthens: if the total is far from what was
   asked, cut words or shots, and agree the length with the person before rendering. Never keep a hand list of on-screen words: it drifted four times in the worked example and
   each drift was a pacing failure found late. Expect the real cut to run longer (worked example: 121 s public,
   146 s internal) because real quotes are longer.
   → Check: `pace_check.py` prints ALL OK for every cut.

8. **Render, then gate, then deliver.** `render.py film.html --video film.mp4 --variant <cut>` per cut, one after the
   other in the background. Then huashu's `deliver.py` (it runs the film gate, refuses red, copies the film and
   writes `交付说明.md`), then append your own notes section after it (it rewrites the file), then `deliver.py --verify`.
   → Check: gate is green or yellow, and every yellow item is explained in the notes.

9. **One cold reviewer.** A cheap agent that sees only frames sampled every ~3 s, no source, no brief. Fix what it
   misreads; record what you leave and why.
   → Check: a review file exists, with fixed and not-fixed lists.

## Real lines: a cut with a real client's words, and a public cut

- One file, two string sets: `STR.public` (generic lines; any invented figure labelled "example") and
  `STR.internal = Object.assign(clone(STR.public), {...real lines...})`, so a missing real line falls back to the
  generic one instead of crashing.
- A real line is verbatim, carries who said it and when ("<name>, <date> call"), and has a file and line you can cite.
  Keep a table outside the film: shot → line → source path:line → kind (client's own words / an AI stand-in / ours).
- An AI agent's words (a reviewer, a stand-in for a client person) are labelled as that agent's, never as the
  client's. Your own framing stays outside the quote marks ("It asked: …"). A summary in your log is not a quote:
  write "both asked why X", not a bubble saying "Why X?" in quote marks, unless the log quotes it.
- If the film shows the method as now written and a real run did it differently (a step the run did not have, a
  question settled another way), say so on the shot in a small tag, not only in a notes file nobody watching reads.
- If lines come from several runs or deliverables, tag every shot with which one (`setupFilm({tags:[...]})`): one hero
  object riding through every shot otherwise implies one deliverable.
- Never put a person's profile on screen (how they read, what they distrust, how to win them): only what they asked,
  said or scored. The internal cut never goes in a repo, especially one that is mirrored to the client.

## Mechanics and traps

| Trap | What happens | Fix |
|---|---|---|
| Font not bundled | the film renders in a fallback font with no error | `new_film.py` copies `fonts/`; `render.py` exits if Outfit did not load |
| Overlay drawn inside the camera | caption and map zoom and drift with the picture | draw them with `cap()` / `mini()`, which write to the overlay, never into the shot's returned SVG |
| Zoom covers header or caption | a camera push draws over them | the kit clips the picture to the stage band (`setupFilm({stage})`) |
| SVG ids repeat | two `tape()` calls fight over one clipPath | the kit numbers clip ids and resets them every frame; do the same for your own `clipPath`s |
| Text the same colour as the paper | muted grey labels vanish on the cream tape | labels over paper use the dark ink; check on the contact sheet |
| Camera pan crops labels | the last frame of a shot cuts the left-hand labels | pan less, or move the content; check the END still of each shot |
| Outdated renders keep running | CPU spent on a version you already changed | `pkill -f "render.py"` before re-rendering |
| zsh glob with no match | `rm -rf frames-* && ...` aborts the whole `&&` chain ("no matches found") | name the folder, or use `;`, or `setopt nonomatch` |
| An either-or condition drawn with the AND shape | two lamps read as "both" | write "or" between them and let either one open the gate (the kit's lamp note) |
| Stills folder reused across timings | the sheet tiles yesterday's stills next to today's | `--per-shot` empties the folder first; with `--stills`, empty it yourself |
| `film_beats.js` writes next to the page | run on the shipped example, it writes into the skill folder | `--out <somewhere else>` |
| `deliver.py` rewrites the notes | your notes section disappears | append it after `deliver.py`, then `deliver.py --verify` |
| A peer agent's reply never arrives | you wait on a fact-check that was sent to a busy session | read the other session's transcript instead of waiting |
| Gate red: fast-motion | long reading holds | camera inside the shot (step 4); a yellow on "few cuts per 10 s" is expected and is explained, not fixed |

## Timings and sizes (worked example, M-series Mac)

- 16 shots, 126 s (public) and 148 s (internal), 1920×1080, 30 fps, x264 CRF 16.
- Full render with 6 parallel pages: roughly 8–10 minutes per cut. A still: about a second each after page load.
- The film page is ~30 KB of hand-written SVG and JS; the kit is ~15 KB.

## Tested cold

A fresh agent given only this skill and a new topic (a test kitchen developing a recipe: three tasters score each
round, a checker re-measures independently) built a 13-shot, 96.5 s film to the contact-sheet stage in about ten
minutes, with ALL OK on pacing and no script errors. It used the kit's shapes for its own meanings (dials for taster
scores, sticky notes for their notes, tape for the chef's fix list, a balance for the two measurements) and drew
its own for the rest (a pot, plates, a barrier). Everything it found unclear is fixed above: the per-shot sheet, the
visible area, the advisories, number collapsing, the AND/OR lamps, the tape and dial options, and the scale rule.
