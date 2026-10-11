# -*- coding: utf-8 -*-
"""test_clusters_served_b651.py -- THE PLANTED TEST OF tools/licensed_table.py's CLUSTERS-SERVED, under (R261)(5).

###   (1) a kernel cited in the Correspondence tables of two documents of two clusters reads both clusters;
###   (2) a kernel named only outside any Correspondence section reads served: none;
###   (3) the census itself cites every kernel and is read and not counted;
###   (4) a Correspondence section ends at the next heading of its own level: a citation in the following section is not read;
###   (5) a deeper heading inside a Correspondence section stays inside it ("### Correspondence" holding a "#### tiered" sub-table);
###   (6) a longer repository name sharing the kernel's name as a prefix ("SIDE-kernel-x") is not the kernel.
### Planted text only. Usage: python tools/test_clusters_served_b651.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import licensed_table as LT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

A = '# A\n\nBody names SIDE-alpha in prose.\n\n## Correspondence\n\n| claim | SIDE-beta | x |\n\n## Version history\n\nSIDE-gamma here.\n'
B = '# B\n\n### Correspondence\n\n| claim | SIDE-beta |\n\n#### tiered\n\n| SIDE-delta | t |\n\n### Next\n\nnothing\n'
C = '# C\n\n## Correspondence\n\n| SIDE-gamma-x | not gamma |\n'
CEN = '# CENSUS\n\n## Correspondence\n\n| SIDE-alpha | SIDE-beta | SIDE-gamma | SIDE-delta |\n'
DOCS = [('A', 'method', A), ('B', 'side', B), ('C', 'surround', C), ('CENSUS', 'method', CEN)]


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-100s %s' % (label, 'PASS' if cond else '### FAIL'))

    s, _c = LT.clusters_served('SIDE-beta', DOCS, exclude=('CENSUS',))
    want('(1) a kernel cited from two clusters reads both', s == ['method', 'side'])
    s, cites = LT.clusters_served('SIDE-alpha', DOCS, exclude=('CENSUS',))
    want('(2) named only in prose: served none (the census`s citation read, not counted)', s == [] and [c[0] for c in cites] == ['CENSUS'])
    want('(3) the census is read and not counted', ('CENSUS', 'method', 1) in cites)
    s, _c = LT.clusters_served('SIDE-gamma', DOCS, exclude=('CENSUS',))
    want('(4) a section after the Correspondence section is not read; (6) SIDE-gamma-x is not SIDE-gamma', s == [])
    s, _c = LT.clusters_served('SIDE-delta', DOCS, exclude=('CENSUS',))
    want('(5) a deeper heading stays inside the Correspondence section', s == ['side'])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
