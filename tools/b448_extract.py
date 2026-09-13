# -*- coding: utf-8 -*-
"""b448_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS (P1)-(P6).
### ### Every read is a line quoted with its number, re-taken here from its source before the face is typed.
### Banked values are read, not recomputed by any chain; it runs no chain and appends nothing."""
import io
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
OUT = os.path.join(D, 'b448_extract.txt')
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def quote(path, needle, label, show=170):
    try:
        ls = io.open(path, encoding='utf-8-sig', errors='replace').read().splitlines()
    except Exception:
        ls = []
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    rel = path.replace(os.sep, '/')
    if not hit:
        MISSES.append((label, rel, needle))
        rec('      ### MISS : %s -- %r not in %s' % (label, needle, rel))
        return None
    i, l = hit[0]
    rec('      %s:%d | %s' % (rel.split('/')[-1] if 'relay' not in rel else os.path.relpath(path, ROOT).replace(os.sep, '/'), i, l[:show]))
    return i


def load(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]


def main():
    rec('=' * 100)
    rec('b448 -- THE SURVEY. ### THE PRE-FACE READS, RE-TAKEN FROM THEIR SOURCES.')
    rec('=' * 100)

    FND = os.path.join(PP, 'FINDINGS.md')
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    R351 = os.path.join(D, 'b351_registration_2026-09-07.txt')
    RUN351 = os.path.join(D, 'b351_read_run.txt')

    rec('')
    rec('(P1) THE PARTITION AT ITS OWN ANCHORS -- WHAT IT CLASSIFIES, OVER WHAT, AND ITS BRANCH RULE.')
    quote(FND, '| **The failure-mode partition** | **NAMED HERE AS A RESEARCH PROPOSAL AND NOT OPENED**', 'P1 b348 row', 120)
    quote(FND, 'a finite classification of the ways the margin could fail, over the aim plane', 'P1 b348 object', 60)
    quote(R351, 'width -- admit a finite classification of the ways the margin could fail?', 'P1 b351 question')
    quote(R351, 'the margin is the', 'P1 margin defined')
    quote(R351, "room the corpus charts, `places = prime - arch`, and it FAILS at an aim when that room is not", 'P1 margin fails at an aim')
    quote(R351, 'An absence of a bound is NOT an obstruction, and this branch may not be reached by failing to find', 'P1 branch rule')
    quote(R351, '`BOUNDED BY A MEASUREMENT` -- the record has looked as far as it has looked and says so;', 'P1 state measurement')
    quote(R351, 'A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE.', 'P1 distinction one')
    quote(R351, 'A METHOD THAT PRODUCES INSTANCES DOES', 'P1 distinction two')
    quote(RUN351, '(M-gamma) "there exist T0 and finitely many classes C1..Ck such that every aim with gamma > T0 lies in one of them', 'P1 M-gamma', 200)
    quote(RUN351, 'VERDICT : ### **UNDECIDED**', 'P1 b351 verdict')
    quote(FND, 'the exhaustion move reaches the quantifier in no branch of that act', 'P1 fold scope', 60)

    rec('')
    rec('(P2) THE ARC`S TAXONOMY AT ITS OWN ANCHORS -- WHAT IT CLASSIFIES AND HOW A KIND IS ASSIGNED.')
    quote(OT, 'enumerate every candidate shared witness for the site from the record and the literature by description', 'P2 enumeration defined', 60)
    quote(OT, 'fail each at a quoted step or hold it', 'P2 fail at a quoted step', 60)
    quote(FND, 'a closed taxonomy of 11 failure kinds', 'P2 fold statement', 60)
    DR = os.path.join(D, 'b443r_u1_draft.md')
    quote(DR, '| kind | (i) | (ii) | (iii) | (iv) | (v) | (vi) | total |', 'P2 taxonomy header')
    kinds = []
    for l in io.open(DR, encoding='utf-8').read().splitlines():
        m = re.match(r'^\| ([A-Z][A-Z -]+[A-Z]) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$', l)
        if m:
            kinds.append((m.group(1), [int(x) for x in m.group(2, 3, 4, 5, 6, 7)], int(m.group(8))))
    for k, per, tot in kinds:
        rec('        %-28s %s total %d' % (k, per, tot))
    rec('      kinds in the draft`s table : %d ; candidates summed : %d' % (len(kinds), sum(t for _k, _p, t in kinds)))
    rec('      the site rows` missing statements (the draft`s own words):')
    for l in io.open(DR, encoding='utf-8').read().splitlines():
        m = re.match(r'^\| \*\*\((i|ii|iii|iv|v|vi)\)\*\* ([^|]+)\| [^|]+\| ([^|]+)\|', l)
        if m:
            rec('        (%s) %s -- %s' % (m.group(1), m.group(2).strip(), m.group(3).strip()[:110]))
    vi = load('b443r_site_vi.json')
    rec('      b443r_site_vi.json : total %s ; union after five %s ; after six %s' % (vi['total'], vi['union5'], vi['union6']))

    rec('')
    rec('(P3) THE LINKS BETWEEN THEM, COUNTED OFF THE CANDIDATE BANKS -- A READ, NOT A CLASSIFICATION.')
    n, cite = 0, []
    for site, p in SITES:
        for c in load(p)['candidates']:
            n += 1
            if 'b351' in json.dumps(c, ensure_ascii=False):
                cite.append((site, c['id'], c['kind'], c['name']))
    rec('      candidates read : %d ; carrying the string `b351` anywhere in their banked record : %d' % (n, len(cite)))
    for s, i, k, nm in cite:
        rec('        (%s) %-4s %-26s %s' % (s, i, k, nm[:80]))

    rec('')
    rec('(P4) THE CHANNELS AT a = 4.123106, FOUR LEVELS, FROM THEIR OWN BANKS.')
    k = '4.123106'
    a45 = load('b445_arms.json')
    rows = [a45['base'][k], a45['a'][k], load('b446_doubling.json')[k], load('b447_doubling.json')[k]]
    rec('      %-7s %-22s %-22s %-22s %-12s %-14s' % ('nv', 'zero Z', 'arch A', 'prime PR', 'pole P', 'e'))
    for r in rows:
        rec('      %-7d %.15e  %.15e  %.15e  %+.2e  %+.6e' % (r['nv'], r['zero'], r['arch'], r['prime'], r['pole'], r['e']))
    WI = os.path.join(T, 'b321_window.py')
    quote(WI, 'residual=Z - (P - PR + A), prime_terms=terms)', 'P4 residual formula')
    quote(WI, 'val = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, v, w))', 'P4 prime channel by interpolation')
    quote(WI, 'A = float(np.trapezoid(hhat_blocked(v, w, U) * AT.kernel(U), U) / (2.0 * math.pi))', 'P4 arch channel by trapezoid')
    quote(WI, 'Z = 2.0 * float(np.sum(hhat_blocked(v, w, AT.GAM)))', 'P4 zero channel')
    rec('      ### THE CHANGES PER LEVEL ARE NOT TAKEN HERE; the face fixes the rule that reads them first.')

    rec('')
    rec('(P5) b447`S RULE, THE METHOD`S ASYMPTOTIC ORDER IN THE RECORD`S WORDS, AND THE BAR-FLOOR RULE`S LAST LINE.')
    quote(os.path.join(D, 'b447_registration_2026-09-12.txt'), '`[0.9465, 1.9465]` -- the median `1.4465` of b446', 'P5 b447 rule')
    quote(os.path.join(D, 'b447_components.txt'), "rule: p2 in [0.9465, 1.9465] : False ; |d3| < |d2| : True", 'P5 b447 rule applied')
    quote(os.path.join(D, 'b447_components.txt'), 'p2 = log2(|d2| / |d3|) = 2.4322', 'P5 b447 p2')
    quote(os.path.join(D, 'b446_components.txt'), 'THE ORDERS ARE NOT THE TRAPEZOID RULE`S ASYMPTOTIC 2', 'P5 asymptotic 2')
    BFR = os.path.join(TE, 'modules', '2026-09', 'BAR_FLOOR_RULE.md')
    quote(BFR, '- **The other face (b447):**', 'P5 bar-floor last line', 80)
    lines = io.open(BFR, encoding='utf-8').read().splitlines()
    rec('      BAR_FLOOR_RULE.md lines : %d ; the last non-empty begins %r' % (len(lines), [x for x in lines if x.strip()][-1][:40]))

    rec('')
    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '448'], capture_output=True,
                         text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'STARTS AT|runs through|THE CURRENT SPAN|NOTHING WAS WRITTEN', l):
            rec('      ' + l.strip())

    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
