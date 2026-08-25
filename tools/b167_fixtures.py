# -*- coding: utf-8 -*-
"""b167 -- FIXTURES for the empty-scope gate, BOTH POLARITIES, before service.
### The nursery convention: a check's first run is part of its construction."""
import functools, os, subprocess, sys, tempfile
print = functools.partial(print, flush=True)
TOOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banned_terms.py')
ok = True


def run(args):
    r = subprocess.run([sys.executable, TOOL] + args, capture_output=True, text=True)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def chk(name, got, want):
    global ok
    good = (got == want)
    ok &= good
    print("  %-52s exit %-2s (want %s)  %s" % (name, got, want, "PASS" if good else "### FAIL"))


d = tempfile.mkdtemp()
clean = os.path.join(d, 'clean.txt')
dirty = os.path.join(d, 'dirty.txt')
open(clean, 'w').write("this file names what is missing rather than filling it.\n")
open(dirty, 'w').write("there is a %s in the argument here.\n" % "g" "ap")

print("### THE EMPTY-SCOPE GATE, BOTH POLARITIES")
# NEGATIVE polarity: no scope at all must now FAIL HARD
chk("no arguments at all -> hard failure", run([])[0], 2)
chk("bare filenames (ignored; b166's case) -> hard failure", run([clean])[0], 2)
chk("--new with no files following -> hard failure", run(['--new'])[0], 2)

# POSITIVE polarity: a real scope must still be judged on its content
chk("--new on a clean file -> clean", run(['--new', clean])[0], 0)
chk("--new on a file with a live use -> not clean", run(['--new', dirty])[0], 1)

print("\n### AND THE GATE MUST NOT SWALLOW A REAL VERDICT")
code, out = run(['--new', clean])
chk("clean run still prints a verdict", int('VERDICT' in out), 1)
chk("clean run does NOT print NO SCOPE", int('NO SCOPE' in out), 0)
code, out = run([clean])
chk("empty run prints NO SCOPE", int('NO SCOPE' in out), 1)
chk("empty run does NOT print the word CLEAN as its verdict",
    int('VERDICT          : CLEAN' in out), 0)

print("\n### FIXTURES: %s" % ("ALL PASS" if ok else "### FAILED"))
sys.exit(0 if ok else 1)
