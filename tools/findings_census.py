# -*- coding: utf-8 -*-
"""findings_census.py -- THE FINDINGS CENSUS (built b163).

### WHAT IT DOES: extracts the correspondence spine mechanically -- row number,
### terminal modules, the grade cell and the status cell -- so an object census can
### be built on what the record SAYS rather than on what the executor remembers.

### WHAT IT DOES NOT DO: assign objects, grade anything, or decide relations.
### ### THE EXTRACTION IS MECHANICAL; THE OBJECT ASSIGNMENT IS A READ, and the two
### are kept apart so the read can be checked against the extraction.

### REACH: it reads CORRESPONDENCE.md's numbered rows. ### A RESULT WITH NO
### CORRESPONDENCE ROW IS INVISIBLE TO IT -- and the corpus holds many, which is why
### the census below is completed from the banks and FINDINGS by hand and says so.

Usage:
    python findings_census.py [--terminals]
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
ROW = re.compile(r'^\| *(\d+) \|')
MOD = re.compile(r'`([A-Z][A-Za-z0-9]*(?:Shadow|Chart|Section|Glue|Silence|Arrival|Limit|Draft))`')


def rows():
    out = []
    for L in io.open(CORR, encoding='utf-8').read().split('\n'):
        m = ROW.match(L)
        if not m:
            continue
        cells = L.split('|')
        n = int(m.group(1))
        terminals = cells[3] if len(cells) > 4 else ''
        grade = cells[5] if len(cells) > 6 else ''
        status = cells[6] if len(cells) > 7 else ''
        mods = sorted(set(MOD.findall(terminals)))
        # terminal-count hint, as the row itself states it
        cnt = re.search(r'\((\d+) terminals?', terminals)
        out.append(dict(n=n, mods=mods, count=int(cnt.group(1)) if cnt else None,
                        grade=grade.strip()[:58], status=status.strip()[:34]))
    return out


def main(argv):
    rs = rows()
    print("=" * 96)
    print("THE CORRESPONDENCE SPINE, EXTRACTED MECHANICALLY (b163)")
    print("=" * 96)
    print("  numbered rows: %d" % len(rs))
    graded = {}
    for r in rs:
        key = r['grade'].split('(')[0].strip().split(' ')[0] or '(blank)'
        graded[key] = graded.get(key, 0) + 1
    print("\n  GRADE CELLS, by leading word -- as the rows themselves carry them:")
    for k in sorted(graded, key=lambda x: -graded[x]):
        print("      %-28s %d" % (k, graded[k]))
    withmod = [r for r in rs if r['mods']]
    print("\n  rows naming at least one kernel module : %d" % len(withmod))
    print("  rows naming none                        : %d" % (len(rs) - len(withmod)))
    tot = sum(r['count'] for r in rs if r['count'])
    print("  terminals claimed across rows that state a count: %d" % tot)
    if '--terminals' in argv:
        print("\n  row : modules")
        for r in rs:
            print("  %3d : %s" % (r['n'], ", ".join(r['mods']) or "### none named"))
    print("\n  ### REACH: this reads CORRESPONDENCE.md's numbered rows only.")
    print("  ### A RESULT WITH NO CORRESPONDENCE ROW IS INVISIBLE TO IT.")
    print("  ### The object census is completed from the banks and FINDINGS by a read,")
    print("  ### and the two halves are reported separately so the read can be checked.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
