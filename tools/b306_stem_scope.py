# -*- coding: utf-8 -*-
"""b306_stem_scope.py -- THE STEM SWEEP, EXTENDED TO THE SHARED APPEND-TARGETS.

### ### **THE HOLE THIS CLOSES, NAMED BY b305 AND QUOTED FROM ITS OWN BANK:** ### *"THE SWEEP RUNS
### OVER THIS ACT'S FILES AND NOT OVER `CORRESPONDENCE.md`, SO THE ROW WAS CAUGHT BY THE BANK'S HIT
### AND NOT BY ITS OWN -- and that is a real hole in the sweep's scope, named here rather than
### left."**
### At b305 a banned stem reached a correspondence row and was caught ### ONLY ### because the same
### word also appeared in that act's bank. ### **HAD THE WORD APPEARED IN THE ROW ALONE, `G-STEM`
### WOULD HAVE REPORTED CLEAN.**

### ### **WHY THE SHARED TARGETS ARE A DIFFERENT SPECIES FROM AN ACT'S OWN FILES.** ### An act's
### files are written once and swept once. ### **`CORRESPONDENCE.md` AND `banked_index.py` ARE
### APPENDED TO BY EVERY ACT AND SWEPT BY NONE**, so a hit in them can be OLDER than the act
### running, and a tool that hard-failed on any hit would make every later act pay for an earlier
### act's word. ### ### **SO THIS TOOL REPORTS PER ROW AND ATTRIBUTES BY ROW NUMBER. ### IT DOES
### NOT REFUSE.** ### The act reads the attribution and decides.

### ### **AND THE LIMIT, IN THE HEADER SO IT IS NOT TRUSTED BEYOND IT:** ### the stems are READ
### from `ferry_scan.stems()`, which reads them from `banned_terms.py` and `stem_sweep.py` -- ###
### **NEVER COPIED**, so a stem retired or added moves this tool with it. ### **A HIT IS A STRING,
### NOT A FAULT**: a row that quotes a struck clause in order to record its striking would hit.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import ferry_scan  # noqa: E402  ### the stems are READ from the tools that own them

SIDE = r'D:\SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE SHARED APPEND-TARGETS. ### **EVERY FILE MORE THAN ONE ACT WRITES INTO.**
TARGETS = [
    ('CORRESPONDENCE.md', os.path.join(SIDE, 'CORRESPONDENCE.md'), 'row'),
    ('banked_index.py', os.path.join(ROOT, 'tools', 'banked_index.py'), 'line'),
]

ROW_RE = re.compile(r'^\|\s*(\d+)\s*\|')


def rows_of(path):
    """### RETURN `[(label, text)]`. ### **A TABLE IS SPLIT BY ROW SO A HIT NAMES ITS ROW**, which
    is what makes attribution possible; anything else is split by line."""
    text = io.open(path, encoding='utf-8', errors='replace').read()
    out = []
    for i, ln in enumerate(text.splitlines(), 1):
        m = ROW_RE.match(ln)
        out.append(('row %s' % m.group(1) if m else 'line %d' % i, ln))
    return out


def self_test(verbose=True):
    """### **BOTH POLARITIES, AND THE ROW-ATTRIBUTION ARM IS THE ONE THAT MATTERS.**

    ### A sweep that found a hit but could not say WHICH ROW carries it would leave the act unable
    ### to tell its own row from an ancestor's, ### **WHICH IS THE WHOLE POINT OF EXTENDING THE
    ### SCOPE.**
    """
    stem_list = ferry_scan.stems()
    import banned_terms
    s0 = banned_terms.STEMS[0]
    cases = [
        ('fires: a banned stem in a table row',
         '| 42 | a sentence carrying %s in it | b | c | d | e |' % s0, True),
        ('quiet: a clean table row',
         '| 43 | the pair certifies sharpness at that cell | b | c | d | e |', False),
        ('fires: a banned stem outside a row',
         'a heading carrying %s' % s0, True),
        ('quiet: an ordinary heading', '## The correspondence', False),
    ]
    bad = 0
    if verbose:
        print('  %-52s %-14s %s' % ('sweep fixture', 'got/exp', 'agree'))
    for lbl, text, expect in cases:
        _c, sh = ferry_scan.scan_text(text, [], stem_list)
        got = bool(sh)
        ok = (got == expect)
        bad += 0 if ok else 1
        if verbose:
            print('  %-52s %-14s %s' % (lbl, '%s/%s' % (got, expect),
                                        'YES' if ok else '### NO ###'))
    # ### THE ATTRIBUTION ARM.
    lab = ROW_RE.match('| 118 | statement | t | p | g | current |')
    lab2 = ROW_RE.match('some prose line')
    a1 = (lab is not None and lab.group(1) == '118')
    a2 = (lab2 is None)
    bad += 0 if (a1 and a2) else 1
    if verbose:
        print('  %-52s %-14s %s' % ('### row number recovered from a real row',
                                    '%s/%s' % (a1, True), 'YES' if a1 else '### NO ###'))
        print('  %-52s %-14s %s' % ('### and NOT invented for a prose line',
                                    '%s/%s' % (a2, True), 'YES' if a2 else '### NO ###'))
    return bad == 0


def sweep(path):
    """### RETURN `[(label, stem-label, line-text)]` FOR ONE FILE."""
    stem_list = ferry_scan.stems()
    hits = []
    for label, text in rows_of(path):
        _c, sh = ferry_scan.scan_text(text, [], stem_list)
        for h in sh:
            hits.append((label, h[0], text.strip()))
    return hits


def main(argv):
    print('=' * 100)
    print('b306_stem_scope.py -- THE STEM SWEEP, EXTENDED TO THE SHARED APPEND-TARGETS.')
    print('=' * 100)
    ok = self_test()
    print('  self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT A SWEEP FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2
    stem_list = ferry_scan.stems()
    print('  stem patterns read from the owning tools : %d   ### NEVER COPIED' % len(stem_list))
    print()

    total = 0
    for name, path, unit in TARGETS:
        if not os.path.exists(path):
            print('  ### %-24s NOT PRESENT AT %s' % (name, path))
            continue
        units = rows_of(path)
        hits = sweep(path)
        total += len(hits)
        print('  %-24s %s units swept : %-6d   stem hits : %d'
              % (name, unit, len(units), len(hits)))
        for label, stem, text in hits:
            print('      ### %-10s %s' % (label, stem))
            print('          %s' % text[:110])

    print()
    print('  ### TOTAL STEM HITS ACROSS THE SHARED TARGETS : %d' % total)
    print('  ### **A HIT IS A STRING, NOT A FAULT, AND A HIT HERE MAY BE OLDER THAN THE ACT')
    print('  ### RUNNING** -- these files are appended to by every act and were swept by none')
    print('  ### until now. ### **THE ROW NUMBER IS THE ATTRIBUTION; THE ACT READS IT AND DECIDES.**')
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
