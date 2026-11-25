// Write beats.<variant>.json for a style D film by counting the words it ACTUALLY draws in each shot, for pace_check.py. Input: the film's .html.
// Usage: node film_beats.js film.html [--variants public,internal] [--samples 14] [--out dir]
// Also prints, per shot, two advisories: a caption too long for one line, and new words arriving < 2.5 s apart.
// Then:  python3 <skill>/scripts/common/pace_check.py beats.public.json
// Why: a hand-kept list of on-screen words drifts every time a label changes, and each drift is a pacing failure found
// late. This loads kit.js and the film's own script in node, calls renderFrame at evenly spaced times inside every shot,
// and takes the union of all visible <text> in that shot (opacity 0 skipped). The caption comes from cap().
// pace_check then counts only words not already shown in an earlier shot.
const fs = require('fs'), path = require('path');
const args = process.argv.slice(2);
if (!args[0]) { console.error('usage: node film_beats.js film.html [--variants public,internal] [--samples 14]'); process.exit(2); }
const page = path.resolve(args[0]), dir = path.dirname(page), html = fs.readFileSync(page, 'utf8');
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const samples = +opt('--samples', 14), outDir = path.resolve(opt('--out', dir));
// every <script> in page order: src= files are read from disk, inline ones as they are
const code = [...html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)].map(m => {
  const src = (m[1].match(/src="([^"]+)"/) || [])[1];
  return src ? fs.readFileSync(path.join(dir, src), 'utf8') : m[2];
}).join('\n;\n');
let variants = opt('--variants', null);
const unesc = s => s.replace(/&lt;/g, '<').replace(/&amp;/g, '&');
const texts = svg => [...svg.matchAll(/<text\b([^>]*)>([^<]*)<\/text>/g)].filter(m => !/opacity="0(\.0+)?"/.test(m[1])).map(m => unesc(m[2]));
function run(v) {
  const warn = [];
  const f = new Function('location', 'document', 'window', code + '\n;return {SH, renderFrame, FILM};');
  const { SH, renderFrame, FILM } = f({ search: '?v=' + v }, { getElementById: () => null }, {});
  const beats = SH.map((s, i) => {
    const d = s.b - s.a, words = new Set(), first = new Map(); let caption = '';
    // a number that animates (a dial going 0/5, 1/5 ... 4/5; a counter) is read once: key texts by their digit-free shape
    const shape = t => t.replace(/\d+([.,]\d+)?/g, '#');
    const add = (t, u) => { const k = shape(t); if (!first.has(k)) { first.set(k, u); words.add(t); } };
    for (let k = 0; k < samples; k++) {
      const u = (d - 0.02) * k / (samples - 1), r = renderFrame(s.a + u);
      if (r.cap) caption = r.cap;
      texts(r.pic + r.over).forEach(t => { if (t !== r.cap) add(t, u); });
    }
    for (let u = 0; u < d - 0.02; u += 0.25) {   // finer pass, only for arrival times
      const r = renderFrame(s.a + u); texts(r.pic).forEach(t => { const k = shape(t); if (t !== r.cap && first.get(k) > u) first.set(k, u); });
    }
    if (caption.length > 58) warn.push(`shot ${i + 1}: caption is ${caption.length} characters; over ~58 it runs off a 1920 frame at the default size`);
    const groups = [...new Set([...first.entries()].filter(([t]) => t.split(' ').length >= 2 || t.length > 6).map(([, u]) => +u.toFixed(2)))].sort((a, b) => a - b);
    const close = groups.filter((u, j) => j && u - groups[j - 1] < 2.5 && u > 0.5);
    if (close.length) warn.push(`shot ${i + 1}: new words arrive at ${groups.map(u => u.toFixed(1)).join(', ')} s (less than 2.5 s apart ${close.length}x)`);
    if (FILM.header) words.add(FILM.header);
    return { title: 'shot ' + (i + 1), caption, dur: +d.toFixed(2), still: +(d - 0.6).toFixed(2), picture: [...words].join(' ') };
  });
  const out = path.join(outDir, 'beats.' + v + '.json');
  fs.writeFileSync(out, JSON.stringify({ [path.basename(page, '.html') + '-' + v]: { title: v, beats } }, null, 1));
  console.log('wrote', out, beats.length, 'shots,', beats.reduce((a, b) => a + b.dur, 0).toFixed(1), 's');
  if (warn.length) { console.log('  advisories (' + v + '): fine when the words read as one group, e.g. the rows of one list arriving together; not when each needs its own read'); warn.forEach(w => console.log('  - ' + w)); }
}
if (!variants) { // find the cuts the film defines: STR keys if present, else 'public'
  try { variants = Object.keys(new Function('location', 'document', 'window', code + '\n;return typeof STR!=="undefined"?STR:{public:1}')({ search: '' }, { getElementById: () => null }, {})).join(','); }
  catch (e) { variants = 'public'; }
}
variants.split(',').forEach(run);
