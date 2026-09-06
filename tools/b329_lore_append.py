# -*- coding: utf-8 -*-
"""b329_lore_append.py -- "GENERAL AND PER-CELL ARE STATED IN THE MODULE HEADER, NEVER AVERAGED" INTO THE LORE.
### APPEND ONLY, IDEMPOTENT, READ BACK BY RUNNING THE LORE'S OWN SELF-TEST.

### ### **THE RULE:** ### *a kernel module that mixes decided cells with general theorems carries both
### scope words as separate statements in its own header, and its rows and ledger updates say which
### is which.* ### **THE INCIDENT:** ### b329 -- the finite-side seal: the decomposition and the scaling
### part general, the compact part per cell, in one module; b309's header had called its general law
### uncompiled, and b329 compiled it without letting the per-cell arm borrow the word. ### **THE
### GATE:** ### `b329_header_gate.check`, both polarities. ### **WHY LIST ONE:** ### it has a callable
### gate that fires.
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

MARK = "rule='General and per-cell are stated in the module header, never averaged"

ENTRY_ANCHOR = "         discharged='b328'),\n]\n"
ENTRY_NEW = (
    "         discharged='b328'),\n"
    "    dict(rule='General and per-cell are stated in the module header, never averaged: a kernel module '\n"
    "              'that mixes decided cells with general theorems carries both scope words as separate '\n"
    "              'statements in its own header, and its rows and ledger updates say which is which.',\n"
    "         incident='b329 -- the finite-side seal: the decomposition and the scaling part GENERAL, the '\n"
    "                  'compact part PER CELL, in one module (FiniteSideSeal.lean); b309\\'s own header had '\n"
    "                  'called its general law uncompiled, and b329 compiled it without letting the per-cell '\n"
    "                  'arm borrow the word -- and found that the audit bar (zero axioms) forbids the '\n"
    "                  'library\\'s divisibility lemmas, so the general theorems are equations with witnesses.',\n"
    "         tool='b329_header_gate.check -- fires on a header carrying one scope word only or an averaging '\n"
    "              'phrase; quiet on FiniteSideSeal.lean\\'s header; both polarities in its fixtures().',\n"
    "         discharged='b329'),\n"
    "]\n")

FIX_ANCHOR = "def self_test(verbose=True):\n"
FIX_NEW = (
    "def _fixture_header_scope():\n"
    "    \"\"\"### BOTH POLARITIES: a header with one scope word and an averaging phrase makes the gate FIRE;\n"
    "    ### FiniteSideSeal.lean's own header leaves it QUIET.\"\"\"\n"
    "    sys.path.insert(0, os.path.join(ROOT, 'tools'))\n"
    "    import b329_header_gate\n"
    "    return b329_header_gate.fixtures()\n"
    "\n"
    "\n"
    "def self_test(verbose=True):\n")

LIST_ANCHOR = "                     ('phase condition (b326/b328)', _fixture_phase_condition)]:\n"
LIST_NEW = ("                     ('phase condition (b326/b328)', _fixture_phase_condition),\n"
            "                     ('header scope, general vs per-cell (b329)', _fixture_header_scope)]:\n")

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    rec('=' * 100)
    rec('b329 -- THE LORE GAINS THE HEADER-SCOPE RULE, WITH ITS INCIDENT AND ITS GATE.')
    rec('=' * 100)
    present = MARK in txt
    rec('  rule already present : %s' % present)
    if not present:
        for anc in (ENTRY_ANCHOR, FIX_ANCHOR, LIST_ANCHOR):
            if anc not in txt:
                rec('  ### HARD FAILURE -- an anchor is not in the lore file: %r' % anc[:60])
                return 2
        new = txt.replace(ENTRY_ANCHOR, ENTRY_NEW, 1).replace(FIX_ANCHOR, FIX_NEW, 1).replace(LIST_ANCHOR, LIST_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
        rec('  written : the entry, its fixture, and the fixture\'s line in the self-test list')
    back = io.open(PATH, encoding='utf-8').read()
    rec('  read back : entry once %s ; fixture present %s' % (back.count(MARK) == 1, '_fixture_header_scope' in back))
    r = subprocess.run([sys.executable, PATH], capture_output=True, text=True, encoding='utf-8', errors='replace')
    rec('  the lore\'s own self-test, run after the write : exit %d' % r.returncode)
    line = [ln for ln in (r.stdout or '').splitlines() if 'header scope' in ln]
    for ln in line:
        rec('    %s' % ln.strip())
    both = any('fires: True' in ln and 'stays quiet: True' in ln for ln in line)
    rec('  ### BOTH POLARITIES ON THE NEW RULE : %s' % both)
    rec('=' * 100)
    return 0 if (r.returncode == 0 and both) else 1


if __name__ == '__main__':
    code = main()
    base = 'b329_lore_run' if any('written :' in x for x in LINES) else 'b329_lore_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
