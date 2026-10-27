# -*- coding: utf-8 -*-
"""b718_registrations.py -- (R328)(4)(iv): THE NEXT DISCRIMINANTS, registered and not computed. The rule is printed before any discriminant
is named: the least |D| with h(D) = 2 and the least with h(D) = 5 among negative fundamental discriminants with two units (D < -4) not yet
used. "Used": the three the record computed at (-23, -15, -39), and any candidate the ledgers name as a discriminant -- each candidate read
in PLACE-papers FINDINGS.md, OPEN_TRAILS.md and REGISTRY.md for the number beside a discriminant word on one line, every hit printed for
the hand-read. Nothing at a candidate is computed beyond its class number and its reduced forms.
Routes: `dry` prints the rule, the candidates and the scan, and writes nothing; `write` writes data/b718_registrations.txt (the rule, the
two discriminants with their forms, the law carried with its falsifier, the conflict of (iv) named, b719's price) through the membrane.
"""
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b718_classgroup as CG   # noqa: E402
import b718_worklist as K      # noqa: E402

USED = [-23, -15, -39]
RULE = ('THE RULE ((R328)(4)(iv), the navigator`s): among negative fundamental discriminants D with two units (D < -4), ordered by |D|, '
        'take the least with h(D) = 2 and the least with h(D) = 5, each not yet used -- used meaning computed by the record (-23, -15, '
        '-39) or named as a discriminant in PLACE-papers FINDINGS.md, OPEN_TRAILS.md or REGISTRY.md (the scan below, every hit hand-read).')
WORDS = re.compile(r'(?i)discriminant|\bD\s*=|sqrt\s*\(?\s*-|Q\(\s*sqrt|class number|\bh\s*=')


def squarefree(m):
    m = abs(m)
    d = 2
    while d * d <= m:
        if m % (d * d) == 0:
            return False
        d += 1
    return True


def fundamental(D):
    if D % 4 == 1 or D % 4 == -3:
        return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return (m % 4 in (2, 3)) and squarefree(m)
    return False


def candidates(h, k=4):
    out, D = [], -5
    while len(out) < k:
        if fundamental(D) and len(CG.reduced_forms(D)) == h:
            out.append(D)
        D -= 1
    return out


def scan(D):
    pat = re.compile(r'(?<![\d.\w])%d(?![\d.])' % D)
    hits = []
    for name in ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md'):
        p = os.path.join(K.PP, name)
        if not os.path.exists(p):
            hits.append((name, 0, 'ABSENT'))
            continue
        for i, l in enumerate(io.open(p, encoding='utf-8').read().split(NL), 1):
            if pat.search(l) and WORDS.search(l):
                m = pat.search(l)
                hits.append((name, i, l[max(0, m.start() - 90):m.end() + 60].replace(NL, ' ')))
    return hits


def main(route):
    L = ['b718 -- (R328)(4)(iv): THE NEXT DISCRIMINANTS, REGISTERED AND NOT COMPUTED (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### ' + RULE, '']
    pick = {}
    for h in (2, 5):
        cs = candidates(h)
        L += ['## h = %d: the least candidates by |D|: %s' % (h, cs)]
        for D in cs:
            used = D in USED
            hs = scan(D)
            L += ['  %d: fundamental True ; h %d ; used by the record %s ; ledger hits %d' % (D, h, used, len(hs))]
            for name, i, s in hs[:12]:
                L += ['      %s :%d  ...%s...' % (name, i, s)]
            if h not in pick and not used and not hs:
                pick[h] = D
        L += ['']
    L += ['### THE RULE`S OUTPUT: h = 2 -> %s ; h = 5 -> %s' % (pick.get(2), pick.get(5))]
    for h, D in sorted(pick.items()):
        F = CG.reduced_forms(D)
        L += ['  D = %d: h = %d ; the reduced forms %s ; the principal %s' % (D, len(F), F, CG.principal(D))]
    print(NL.join(L))
    return L, pick


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else 'dry'
    if r != 'dry':
        sys.exit('usage: b718_registrations.py dry (the bank written by the Write tool from this print)')
    main(r)
