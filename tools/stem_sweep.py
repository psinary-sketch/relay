# -*- coding: utf-8 -*-
"""stem_sweep.py -- THE STEM SWEEP (built b280, at the author's instruction).

### WHAT IT IS: ### a term scan for a RETIRED phrase across a named range of banked files.
### ### **IT REPORTS. ### IT DOES NOT EDIT.** ### The append-only law governs: a retired stem
### found in a banked act is FILED with its file and line, never corrected in place.

### THE RETIRING, RECORDED HERE SO THE TOOL CARRIES ITS OWN REASON:
###   RETIRED STEM : `outcome-blind`
###   REPLACEMENT  : the protocol is named ### **GROUNDS-FIRST**; its descriptive form is
###                  ### **CONSEQUENCE-WITHHELD**.
### ### The stem is matched CASE-INSENSITIVELY and across the hyphen/space boundary, because a
### retired phrase does not stay hyphenated when prose moves it.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RETIRED = r'outcome[-\s]?blind'
REPLACEMENT_NAME = 'GROUNDS-FIRST'
REPLACEMENT_DESC = 'CONSEQUENCE-WITHHELD'

# ### CONTROLS: one stem that MUST be found (the sweep can fire) and one that MUST NOT be
# ### (the sweep can stay quiet). ### **A SWEEP REPORTING ZERO PROVES NOTHING WITHOUT BOTH.**
CONTROL_PRESENT = r'Sonin'
CONTROL_ABSENT = r'zzq[-]not[-]a[-]stem[-]zzq'


def sweep(paths, pattern):
    rx = re.compile(pattern, re.IGNORECASE)
    hits = []
    for p in paths:
        try:
            lines = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
        except IOError:
            continue
        for i, ln in enumerate(lines, 1):
            if rx.search(ln):
                hits.append((p, i, ln.strip()))
    return hits


def act_range_files(lo, hi):
    """### EVERY BANKED FILE OF ACTS `lo`..`hi`, BY NAME PREFIX."""
    d = os.path.join(ROOT, 'data')
    out = []
    for fn in sorted(os.listdir(d)):
        m = re.match(r'^b(\d+)[_.]', fn)
        if m and lo <= int(m.group(1)) <= hi:
            out.append(os.path.join(d, fn))
    return out


def main(argv):
    lo, hi = 268, 279
    files = act_range_files(lo, hi)
    print('=' * 100)
    print('stem_sweep.py -- THE RETIRED STEM ACROSS ACTS b%d-b%d' % (lo, hi))
    print('=' * 100)
    print('  RETIRED STEM : %s' % RETIRED)
    print('  REPLACEMENT  : protocol name %s ; descriptive form %s'
          % (REPLACEMENT_NAME, REPLACEMENT_DESC))
    print('  FILES SWEPT  : %d' % len(files))
    print()
    print('  ### CONTROLS, BOTH POLARITIES:')
    cp = sweep(files, CONTROL_PRESENT)
    ca = sweep(files, CONTROL_ABSENT)
    print('    present-control  /%s/  : %d hits  %s'
          % (CONTROL_PRESENT, len(cp), 'PASS (the sweep can fire)' if cp else '### FAIL ###'))
    print('    absent-control   /%s/  : %d hits  %s'
          % (CONTROL_ABSENT, len(ca), 'PASS (the sweep can stay quiet)' if not ca else '### FAIL ###'))
    print()
    hits = sweep(files, RETIRED)
    print('  ### OCCURRENCES OF THE RETIRED STEM : %d' % len(hits))
    for p, i, ln in hits:
        print('    %s:%d' % (os.path.basename(p), i))
        print('        %s' % ln[:104])
    print()
    print('  ### **NO TEXT WAS CHANGED. THE APPEND-ONLY LAW HOLDS.**')
    print('=' * 100)
    return 0 if (cp and not ca) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
