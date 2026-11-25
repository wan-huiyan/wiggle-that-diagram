#!/usr/bin/env python3
# Start a style D film in a new folder: copies kit.js, fonts/ and the plumbing-only film_skeleton.html (as film.html). Input: the folder.
"""Start a style D film.

  python3 new_film.py <folder>          # refuses to overwrite an existing film.html

Then, from <folder>:
  uv run --with playwright python <skill>/scripts/style-d/render.py film.html --stills 1,6 --out stills
  node <skill>/scripts/style-d/film_beats.js film.html && python3 <skill>/scripts/common/pace_check.py beats.public.json
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).resolve().parent
if len(sys.argv) < 2:
    sys.exit(__doc__)
dst = pathlib.Path(sys.argv[1]).resolve()
dst.mkdir(parents=True, exist_ok=True)
if (dst / "film.html").exists():
    sys.exit(f"{dst / 'film.html'} exists; not overwriting")
shutil.copy(HERE / "kit.js", dst / "kit.js")
shutil.copytree(HERE / "fonts", dst / "fonts", dirs_exist_ok=True)
shutil.copy(HERE / "film_skeleton.html", dst / "film.html")
print("new film ->", dst / "film.html")
