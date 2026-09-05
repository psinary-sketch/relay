# -*- coding: utf-8 -*-
"""b326_lore_append.py -- ONE MECHANIZED RULE INTO THE LORE, WITH ITS INCIDENT AND ITS GATE.
### APPEND ONLY, IDEMPOTENT, READ BACK BY RUNNING THE LORE'S OWN SELF-TEST.

### ### **THE RULE:** ### *a constant is scope-bound and its scope is written down.*
### ### **THE INCIDENT:** ### b325 -- `b321_window.PRIMES`, eleven primes copied from the atlas's
### loop, sufficient at the arc's cells (support below 9) and wrong at `a = 32` (support 1024):
### zeta's places sum came out `+0.003489041`, a value b321's own theorem forbids.
### ### **THE GATE:** ### b326 replaced the tuple by a generator to the reach and wrote the scope
### into the header; the lore's self-test carries a fixture in both polarities (the generated set
### reaches a prime the tuple does not; the tuple is shown insufficient at reach 100).
### ### **WHY IT GOES IN LIST ONE AND NOT LIST TWO:** ### it has a callable gate that can fire.
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'lore_rules.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = "rule='A constant is scope-bound and its scope is written down."

ENTRY_ANCHOR = ("         discharged='b289 (two modules); 25 remain -- `W-ORD-PRINT-COVERAGE`, filed b290'),\n"
                "]\n")
ENTRY_NEW = (
    "         discharged='b289 (two modules); 25 remain -- `W-ORD-PRINT-COVERAGE`, filed b290'),\n"
    "    dict(rule='A constant is scope-bound and its scope is written down. A tuple that was '\n"
    "              'ample where it was born is a tuple, not a law.',\n"
    "         incident='b325 -- `b321_window.PRIMES = (2, ..., 31)`, copied from the atlas\\'s own '\n"
    "                  'prime loop and ample at the arc\\'s cells (support below 9), was carried to '\n"
    "                  'a = 32 (support 1024) where it misses almost every prime in range: zeta\\'s '\n"
    "                  'places sum came out +0.003489041, a value b321\\'s own theorem forbids. The '\n"
    "                  'positive control fired; with every prime the value is -0.000389214.',\n"
    "         tool='b321_window.primes_to(reach) -- the set is GENERATED to the reach of the test '\n"
    "              'function\\'s support and the scope is in the header (edited b326 by order); the '\n"
    "              'lore self-test carries both polarities below.',\n"
    "         discharged='b326'),\n"
    "]\n")

FIX_ANCHOR = "def self_test(verbose=True):\n"
FIX_NEW = (
    "def _fixture_scope_bound():\n"
    "    \"\"\"### BOTH POLARITIES: the frozen tuple is insufficient at reach 100 (the gate FIRES on it);\n"
    "    ### the generated set reaches the prime the tuple does not (the gate stays QUIET on it).\"\"\"\n"
    "    sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))\n"
    "    import b321_window\n"
    "    gen = b321_window.primes_to(100)\n"
    "    fires = (37 not in b321_window.PRIMES_ATLAS) and (max(b321_window.PRIMES_ATLAS) < 100)\n"
    "    quiet = (37 in gen) and (gen[-1] == 97) and (len(gen) == 25)\n"
    "    return fires, quiet\n"
    "\n"
    "\n"
    "def self_test(verbose=True):\n")

LIST_ANCHOR = "                     ('hedge audit, both shapes (b279)', _fixture_hedge)]:\n"
LIST_NEW = ("                     ('hedge audit, both shapes (b279)', _fixture_hedge),\n"
            "                     ('scope-bound constant (b325/b326)', _fixture_scope_bound)]:\n")

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    txt = io.open(PATH, encoding='utf-8', newline='').read().replace(chr(13) + chr(10), chr(10))
    rec('=' * 100)
    rec('b326 -- THE LORE GAINS A MECHANIZED RULE, WITH ITS INCIDENT AND ITS GATE.')
    rec('=' * 100)
    present = MARK in txt
    rec('  rule already present : %s' % present)
    written = False
    if not present:
        for a in (ENTRY_ANCHOR, FIX_ANCHOR, LIST_ANCHOR):
            if txt.count(a) != 1:
                rec('  ### HARD FAILURE -- an anchor is not unique in the lore file: %r' % a[:60])
                return 2
        new = txt.replace(ENTRY_ANCHOR, ENTRY_NEW, 1)
        new = new.replace(FIX_ANCHOR, FIX_NEW, 1)
        new = new.replace(LIST_ANCHOR, LIST_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
        written = True
        rec('  written : the entry, its fixture, and the fixture\'s line in the self-test list')
    else:
        rec('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK STILL RUNS.**')
    back = io.open(PATH, encoding='utf-8', newline='').read().replace(chr(13) + chr(10), chr(10))
    ok = (back.count(MARK) == 1 and '_fixture_scope_bound' in back
          and 'scope-bound constant (b325/b326)' in back)
    rec('  read back : entry once %s ; fixture present %s' % (back.count(MARK) == 1,
                                                              '_fixture_scope_bound' in back))
    r = subprocess.run([sys.executable, PATH], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    out = r.stdout or ''
    line = [ln for ln in out.splitlines() if 'scope-bound constant' in ln]
    rec('  the lore\'s own self-test, run after the write : exit %d' % r.returncode)
    for ln in line:
        rec('    %s' % ln.strip())
    fired = any('fires: True' in ln and 'stays quiet: True' in ln for ln in line)
    ok = ok and r.returncode == 0 and fired
    rec('  ### BOTH POLARITIES ON THE NEW RULE : %s' % fired)
    rec('  ### MECHANIZED rules now : %s' % [ln for ln in out.splitlines() if 'LIST ONE' in ln][:1])
    rec('=' * 100)
    name = 'b326_lore_rerun.txt' if not written else 'b326_lore_run.txt'
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
