#!/usr/bin/env bash
# check.sh - every cheap, offline, deterministic check for wiggle-that-diagram, one line each.
#
#   bash scripts/check.sh
#
# Output: PASS / FAIL + name per check, then "N checks passed" (and "K failed" when any). Exit 1 if anything FAILed.
# Needs python3 and node. The browser contract tests (style-*/test_contract.py) need Chrome and are run by hand.

set -u
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT" || exit 2
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
PY=${PYTHON:-python3}
export PYTHONDONTWRITEBYTECODE=1

PASSED=0; FAILED=0
indent() { sed 's/^/        /' | head -"${1:-12}"; }
pass() { printf 'PASS  %s\n' "$1"; PASSED=$((PASSED + 1)); }
fail() { printf 'FAIL  %s\n' "$1"; FAILED=$((FAILED + 1)); [ -n "${2:-}" ] && printf '%s\n' "$2" | indent; return 0; }

# check NAME cmd...  -> PASS when the command exits 0
check() { local name=$1; shift; local out; out=$("$@" 2>&1); local rc=$?
  if [ $rc -eq 0 ]; then pass "$name"; else fail "$name" "exit $rc: $(printf '%s\n' "$out" | tail -8)"; fi; }

# Syntax check a set of JS files. Files using import/export are copied to .mjs so node parses them as modules.
js_syntax() { local name=$1; shift; local bad="" n=0 f
  for f in "$@"; do n=$((n + 1)); local t=$f
    if grep -qE '^(import|export) ' "$f"; then t="$TMP/esm$n.mjs"; cp "$f" "$t"; fi
    node --check "$t" >/dev/null 2>"$TMP/err" || bad="$bad$f: $(head -1 "$TMP/err")"$'\n'
  done
  if [ -z "$bad" ]; then pass "$name ($n files)"; else fail "$name" "$bad"; fi; }

WIG=plugins/wiggle-that-diagram/skills/wiggle-that-diagram

PYFILES=$(find $WIG/scripts -name '*.py'; echo $WIG/scripts/common/ffprobe-shim/ffprobe)
js_syntax "node --check scripts + example JS (style C head/tail are fragments, left out)" \
  $(find $WIG/scripts $WIG/examples -name '*.js' ! -name head.js ! -name tail.js)
# shellcheck disable=SC2086
check "every Python script compiles" "$PY" -c 'import sys; [compile(open(f).read(), f, "exec") for f in sys.argv[1:]]' $PYFILES
check "bash -n style-a/make.sh" bash -n $WIG/scripts/style-a/make.sh
check "pace_check.py on beats.example.json" "$PY" $WIG/scripts/common/pace_check.py $WIG/scripts/common/beats.example.json
check "pace_check.py on the pizza demo beats" "$PY" $WIG/scripts/common/pace_check.py $WIG/examples/pizza/beats.json
check "pace_check.py on the expenses demo beats" "$PY" $WIG/scripts/common/pace_check.py $WIG/examples/expenses/beats.json
style_c_rebuild() {
  local E=$WIG/examples/pizza out
  out=$("$PY" $WIG/scripts/style-c/build.py $E/beats.json --src $E/style-c --out "$TMP/c" --css $E/style-c/theme.css 2>&1) || { fail "style C rebuild of pizza" "$(printf '%s\n' "$out" | tail -6)"; return; }
  if cmp -s "$TMP/c/pizza.html" demos/final/pizza.html; then pass "style C build.py rebuilds demos/final/pizza.html byte for byte"
  else fail "style C rebuild differs from demos/final/pizza.html (rebuild the demo or fix the builder)"; fi
}
style_c_rebuild

# The version lives in three places; they must agree.
versions() { "$PY" - <<'PY'
import json, re, sys
m = json.load(open('.claude-plugin/marketplace.json'))['plugins'][0]['version']
p = json.load(open('plugins/wiggle-that-diagram/.claude-plugin/plugin.json'))['version']
s = re.search(r'^\s*version:\s*"?([^"\s]+)', open('plugins/wiggle-that-diagram/skills/wiggle-that-diagram/SKILL.md').read(), re.M).group(1)
sys.exit(0 if m == p == s else f'marketplace {m}, plugin.json {p}, SKILL.md {s}')
PY
}
check "versions agree: marketplace.json, plugin.json, SKILL.md" versions

echo
if [ $FAILED -gt 0 ]; then echo "$PASSED checks passed, $FAILED FAILED"; exit 1; fi
echo "$PASSED checks passed"
