# Style D: a long silent film (1–3 minutes, one SVG page, words on screen)

Use style D when the ask is a **film**, not a slide loop: a promo or explainer of 1–3 minutes, silent, captioned,
delivered as an MP4 (for a team channel, a README, a talk). Styles A–C make short looping clips that live inside a deck;
style D makes one continuous story of 10–20 shots.

Most of this comes from one build: a promo for two Claude skills that work as one loop, made in three versions over
two days, plus an internal cut using a real client project's lines. The public cut ships as `examples/loop-promo/`.
Read that film's source before writing your own: it is the positive example for every rule below. A second build, a
film of about a minute and a half about a client's data for an internal audience, added step 0, the review lenses in
step 9 and the section "A film about someone's data, shown in public"; it is summarised at the end. Throughout,
**the owner** is the person the film is made for, who approves it.

## The method, step by step (each step ends with the check that proves it)

0. **Pick the world before building the film: three directions, the same two shots.** Skip this when the owner has
   already named the look. Otherwise write a short spec (the story and the hero, as in step 1), then build the same
   two shots (8–10 s each) in three worlds that differ in what the hero travels through and in look, not only in
   colour (for a data film: streams into a reservoir; a whiteboard map; an auditor's desk with string). Each
   direction gets a per-shot sheet (step 6), three stills per shot and a short MP4. The owner picks one in a single
   look, and the full film is built once.
   - Why: the owner of the second build asked for three styles before anything was built and chose in one reply;
     nothing built for the chosen world was thrown away later, because only two shots existed when the choice was made.
   → Check: three folders, each with a sheet and an MP4 of the same two shots, and the person's choice in writing.

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
     stage width, and every label inside the stage should be **26 px or more as rendered**: its font size × the stage
     scale (1.1) × the smallest camera scale the shot reaches, in the 1920-wide frame (the caption is 50; the header,
     the kit's per-shot tag line and the corner map are outside the stage and keep their own sizes). The second build
     started at 20 px and its cold reviewer called the text too small for a room; the smallest, dimmest lines (grey
     "e.g." examples under a label) were the hardest, so give secondary text a light grey, never a mid grey, on a dark
     stage.
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

   The six rows below have no kit function: draw them in the film, as the second build did.

   | Idea | Shape (drawn in the film) | Why it works |
   |---|---|---|
   | many systems feeding one store | hills with a stream each, running into one lake; arrows on the stream show the direction, a small sign on a stream credits who moves it | "wide" without a list of names; two-way arrows show a sync, not a one-way dump |
   | how far back each source goes | the lake cut open: deeper = older, one bar per source from its start date, a shaded band for the period being asked about | bars that stop short of the band show at a glance which sources cannot answer for that period; no chart axis to read |
   | rules for duplicate records | one sorting net per rule: two droplets in; merged, both passed, or stacked into one out | each rule becomes a visible verb, and the three can sit side by side |
   | a tool replaced by another | one stream narrowing into the other's bend, a stitched seam and a date post at the handover | reads as a handover, not a break; never draw a gap or a dry bed |
   | verdicts on a list | a printed list feeding three buckets that fill to the real counts | counts become levels; the flying slips are decoration, so say so in the notes |
   | the question the film is about | a paper boat with the question as its label, in every shot | the hero for a data film; the label can fade when the answer arrives |

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
   - A film with no quotes still makes a claim in every label and every number. In the second build a subtitle
     "things we could measure about a customer" sat over a list where about a quarter of the rows were not about
     customers at all ("things we could track" replaced it), and the example under a "use one copy" rule was a case
     where the audit used parts of both.
     Give the checker every on-screen string, the source files, and the rule that decorative pieces (flying slips,
     tick colours) are declared as such.

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
   → Check: gate is green or yellow, and every yellow item is explained in the notes. A red on fast motion alone is the
   exception below.
   - A film that holds still for reading can go red on fast motion and still be the right film. The gate counts a frame
     pair as fast only when the whole frame's mean grey changes by 9 or more (12 fps, 320 wide), so on a dark frame
     with small elements a slow push or glide scores nothing. Worked example: lengthening shots for reading took it
     from yellow (0.037) to red (0.005, then 0.011 with 12% pushes). `setupFilm({accents})` adds one quick push per
     shot, aimed at what just arrived, and 30% pushes got it to yellow (0.038), but at each peak edge labels were
     cropped for about 0.2 s and the gate read 9 of them as cuts. The owner watched both side by side and chose calm.
     So: render a short side-by-side of calm and accented, let the person choose, and if calm, deliver with the red
     written into the notes (`deliver.py` refuses red, so copy the film yourself).

9. **Reviewers, chosen by who appears in the film**, after the MP4 is rendered and before it goes to anyone (between
   render and deliver in step 8). Always a cold viewer: a cheap agent that sees only frames, no source, no brief, and
   reads at about 3 words a second. Add a fact checker with the source files (step 5). When the film shows a
   colleague's work, add a stand-in for that colleague, reading only for whether their work is blamed, misdescribed
   or uncredited. When it names a client, add stand-ins for the client's people, reading for blame, mockery and
   misattribution. A **stand-in** is an agent given a person's own words (their messages, call notes, emails) and
   told to read the film as that person would; if you have a skill that builds them, use it. Run the lenses in
   parallel and give each the same **review pack**, one file holding: every on-screen string **as built** (ask the
   building agent for the list; never use your plan), the source files, and frames pulled from the final MP4,
   because the stills folder can predate the last render. Frames at 0.6 s into each shot, its middle and 0.3 s
   before its end, from the cut's `DURS`:
   ```sh
   python3 - <<'EOF'
   import subprocess; d=[9.5,12.5,17,8]   # paste the cut's DURS
   s=0
   for i,x in enumerate(d,1):
       for tag,t in (("a",s+0.6),("b",s+x/2),("c",s+x-0.3)):   # -> s01a.png, s01b.png, s01c.png, ...
           subprocess.run(["ffmpeg","-loglevel","error","-y","-ss",f"{t:.2f}","-i","film.mp4","-frames:v","1",
                           "-vf","scale=1600:-1",f"s{i:02d}{tag}.png"],check=True)
       s+=x
   EOF
   ```
   - Why: in the second build the cold viewer and the fact checker found no must-fix; the two stand-ins found five.
     A note filed under "the client's questions" was a question the client never asked (it set the client up as
     naive); the example on a duplicate rule used a source with an unresolved issue; a bucket called "Not usable"
     read as "N of the client's sources are broken" when most were only off-topic for the question; a caption made
     the client the actor of a "challenge"; and the ending could be read as a verdict on the client rather than on
     the data. The owner accepted four and kept the ending: a stand-in's verdict is advice, the owner rules.
   → Check: a review file exists per lens, with fixed and not-fixed lists, and every not-fixed item has a reason.

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

## A film about someone's data, shown in public

A film that shows a client's data, and the colleagues who move it, to a company audience (and possibly the client)
has rules a promo does not. All of them came from the second build's reviews.

- **A challenge has no actor.** "Changing: <a channel> moved to a new tool", never "<client> moved <a channel>…". A limit
  sits on the source's history, mess sits on systems recording things differently, and nothing reads as the
  pipelines being broken, leaky or late: no drips, cracks, gaps, red crosses or "lost".
- **Copies that exist by design say so** ("the same record, copied on purpose → use one"). Without it, a copy reads as
  someone's mistake.
- **Name a verdict by what it means for the question**, not as a quality grade: "Not for this question N", not
  "Not usable N".
- **No open question on screen, not even as an example.** If a source has an unresolved issue, pick another example or
  a generic one ("records one system copies so it can act on them").
- **Put the client's hope in the client's own words.** The hope is what the client wants the data to show; in the
  second build it was the hero's label and a caption. "One lever", our own word, confused the owner; searching the
  call transcripts found a short phrase the client had used themselves, which became the label and one of the notes
  in the opening shot. Offer the owner 3–4 wordings with their character counts (captions ≤ 58, step 7), and say
  which one is the client's.
- **A question shown as the client's must be one they asked.** The opening shot showed the client's questions as
  notes under a small heading; one was our paraphrase of a question they never asked. Prefer their words, and mark
  any paraphrase as yours in the delivery notes.
- **Names on screen only when the owner chooses them.** Then send each named person the cut before it plays, and ask
  whether they would rather not be named. Keep a thank-you in one voice: "…and my Claude, who helped us understand"
  mixes two; "…who helped me understand" or "our Claude … us" does not.
- **Credit the people who move the data** on the end card and on the streams they run, and keep the thank-you away
  from any word about data quality ("messy", "limited"), where it reads as sarcasm.

## Mechanics and traps

| Trap | What happens | Fix |
|---|---|---|
| Font not bundled | the film renders in a fallback font with no error | `new_film.py` copies `fonts/`; `render.py` exits if Outfit did not load (it asks for both weights first, so a film whose first frame has no text no longer fails the check) |
| Caption wipes in | a still, a review frame or a paused screen shows half a sentence | `setupFilm({capMode:'fade'})` fades each caption in whole |
| A morph's in-between state | a blank sheet between "notes" and "boat" reads as a glitch on a still | keep any featureless in-between under 0.5 s |
| A count-up mid-shot | a reviewer reads the counts on a frame caught mid-climb as the result (they did not even add up to the list's total) | hold the final counts at least 2 s before the cut; say in the notes that the climb is animation |
| The hero's label changes | a longer label overflows the hull in some shots only | make the shape grow to fit its label, and re-check the end still of every shot after any label change |
| The gate counts cuts that are not there | a calm 7-shot film read as 11 hard cuts | note the true count in the delivery notes; it does not change the verdict |
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
| Still red after the camera moves | the gate's fast measure ignores small motion on a dark frame | show calm vs `accents` side by side and let the person choose (step 8); never add motion silently |

## Timings and sizes (worked example, M-series Mac)

- 16 shots, 126 s (public) and 148 s (internal), 1920×1080, 30 fps, x264 CRF 16.
- Full render with 6 parallel pages: roughly 8–10 minutes per cut. A still: about a second each after page load.
- The film page is ~30 KB of hand-written SVG and JS; the kit is ~15 KB.

## Second build: a data film for an internal audience

7 shots and an end card, about 85 s, one cut (public), calm. The hero was a paper boat carrying the client's question;
the world a reservoir (systems as hills with streams, the data store as a lake, history as depth). Built in five
rounds by one building agent resumed each time: directions (step 0), the full film, a first review (text size, a
stray mark, gaps that read as lost data), the review in four lenses (cold viewer, fact checker, a colleague's
stand-in, the client's stand-ins; step 9), then two details from the source material and the end card. A two-agent
pass over the source material proposed ten details and kept two: the rest were wrong, showed one of our own working
tables as if it were the client's, or put an unresolved question on screen. The calm cut went red on the film gate's
fast-motion measure only (0.001; see step 8) and was delivered by hand with the red in the notes.

## Tested cold

A fresh agent given only this skill and a new topic (a test kitchen developing a recipe: three tasters score each
round, a checker re-measures independently) built a 13-shot, 96.5 s film to the contact-sheet stage in about ten
minutes, with ALL OK on pacing and no script errors. It used the kit's shapes for its own meanings (dials for taster
scores, sticky notes for their notes, tape for the chef's fix list, a balance for the two measurements) and drew
its own for the rest (a pot, plates, a barrier). Everything it found unclear is fixed above: the per-shot sheet, the
visible area, the advisories, number collapsing, the AND/OR lamps, the tape and dial options, and the scale rule.
