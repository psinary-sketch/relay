# -*- coding: utf-8 -*-
"""b447_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS (P1)-(P7). ### **UNDER (R60).**
### ### Every read is a line quoted with its number, re-taken here from its source before the face is typed.
### It runs no chain and appends nothing."""
import io
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
OUT = os.path.join(D, 'b447_extract.txt')
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


def main():
    rec('=' * 100)
    rec('b447 -- THE SURVEY. ### THE PRE-FACE READS, RE-TAKEN FROM THEIR SOURCES.')
    rec('=' * 100)

    rec('')
    rec('(P1) THE OUTLIER AS b445 AND b446 LEFT IT -- AND HOW MANY LEVELS b446`S ORDER USED.')
    a45 = json.load(io.open(os.path.join(D, 'b445_arms.json'), encoding='utf-8'))
    a46 = json.load(io.open(os.path.join(D, 'b446_doubling.json'), encoding='utf-8'))
    k = '4.123106'
    e0, e1, e2 = a45['base'][k]['e'], a45['a'][k]['e'], a46[k]['e']
    rec('      a = %s : e(8193) %+.6e ; e(16385) %+.6e ; e(32769) %+.6e ; seconds at 32769 %s'
        % (k, e0, e1, e2, a46[k]['seconds']))
    rec('      b446`s order p = log2(|e0 - e1| / |e1 - e2|) = %.4f -- THREE LEVELS, TWO DIFFERENCES' % math.log2(abs(e0 - e1) / abs(e1 - e2)))
    quote(os.path.join(D, 'b446_registration_2026-09-12.txt'), 'the measured order', 'P1 face rule')
    rec('      the other four orders : %s' % ['%.4f' % a46['report']['orders'][x] for x in ('3.158312', '3.461088', '3.605551', '4.061553')])

    rec('')
    rec('(P2) THE LOOM, ITS APPENDER, AND ITS LAST ENTRY.')
    LOOM = os.path.join(PP, 'VERIFICATION_LOOM.md')
    quote(os.path.join(T, 'b244_loom_append.py'), 'APPEND ONE HUNK TO THE LOOM', 'P2 appender')
    quote(LOOM, '<!-- b327 loom entry -->', 'P2 last entry marker')
    marks = [l for l in io.open(LOOM, encoding='utf-8-sig').read().splitlines() if re.match(r'<!-- b\d+ loom entry -->', l)]
    rec('      loom entry markers in the file : %d, the last %s' % (len(marks), marks[-1] if marks else None))

    rec('')
    rec('(P3) THE TOOL`S OWN HEADER SENTENCE, AND THE CENSUS IT SITS BESIDE.')
    NF = os.path.join(T, 'noise_floor.py')
    quote(NF, 'A MAGNITUDE TEST ALONE WOULD HAVE PASSED ALL FOUR OF b264', 'P3 header 1')
    quote(NF, 'IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.', 'P3 header 2')
    cj = json.load(io.open(os.path.join(D, 'b446_floor_census.json'), encoding='utf-8'))
    rec('      b446 census : comparisons %d ; OUT of kind %d ; JSON AT_FLOOR %d ; all on an exact zero %s'
        % (cj['kind']['all'], cj['kind']['out'], cj['residue']['json_verdicts']['AT_FLOOR'], cj['residue']['at_floor_zero_only']))
    BFR = os.path.join(TE, 'modules', '2026-09', 'BAR_FLOOR_RULE.md')
    quote(BFR, 'A numerical bar is stated **with the floor of the object it tests**', 'P3 bar-floor rule')
    quote(BFR, '**b345 — a bar finer than its object', 'P3 bar-floor incident 1')

    rec('')
    rec('(P4) WHAT THE RECORD HOLDS CLOSED -- ONE ANCHOR EACH.')
    FND = os.path.join(PP, 'FINDINGS.md')
    quote(FND, 'the enumeration completed at six sites', 'P4 witness arc')
    quote(os.path.join(D, 'b441_closing.txt'), 'IDENTIF', 'P4 identification', 150)
    quote(os.path.join(D, 'b442_closing.txt'), 'MINIMUM', 'P4 minimum', 150)
    quote(os.path.join(D, 'b445_closing.txt'), 'VERDICT, BY THE RULE FIXED ON THE FACE: INTEGRATION', 'P4 residual')
    quote(os.path.join(D, 'b446_closing.txt'), 'NO DOMAIN OF RADIUS EXISTS', 'P4 floor by kind')

    rec('')
    rec('(P5) WHAT STANDS OPEN -- THE DESK`S STAND ITEMS b440-b446, AND THE RECORD`S NAMED ITEMS WITH TRIGGERS.')
    n = 0
    for b in ['440', '441', '442', '443r', '444', '445', '446']:
        ls = io.open(os.path.join(D, 'b%s_desk_notes.txt' % b), encoding='utf-8').read().splitlines()
        for l in ls:
            m = re.match(r'^    (.{60,}?)\s+STAND$', l)
            if m:
                n += 1
                rec('      b%-5s STAND | %s' % (b, m.group(1).strip()))
    rec('      desk STAND lines : %d' % n)
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    quote(FND, '**W-ORD-SPAN-HEADING.**', 'P5 span work-order')
    quote(FND, '**Its trigger:** the next act that removes a directory', 'P5 removal work-order')
    quote(OT, "**Trigger unchanged: the instrument lane opening.**", 'P5 disproof lane')
    quote(OT, 'fast-radio-burst dispersion measures as an independent baryon-fraction probe.** Trigger:', 'P5 FRB trail')
    quote(OT, 'Trigger: the ruling on which test governs, or any disposition on the four open lists.', 'P5 four lists')
    quote(FND, '| **The failure-mode partition** |', 'P5 partition', 120)
    quote(FND, '| **The uniformity row `U1`** | NAMED-ONLY', 'P5 U1', 120)
    quote(FND, '| **`M-2`** | OWED', 'P5 M-2', 120)

    rec('')
    rec('(P6) THE QUANTIFIER, IN THE RECORD`S OWN WORDS.')
    quote(FND, '| **K8** the quantifiers | UNOWNED', 'P6 K8', 200)
    quote(FND, 'aimed at the QUANTIFIER rather than at its constituents', 'P6 partition aim', 60)
    quote(FND, 'the exhaustion move reaches the quantifier in no branch of that act', 'P6 b351', 60)
    quote(FND, 'No move aimed at the quantifier remains on this board that the span has not tried and priced.', 'P6 b360 sentence', 60)
    rec('      FINDINGS.md lines carrying "quantifier" after the b360 fold`s sentence :')
    ls = io.open(FND, encoding='utf-8-sig').read().splitlines()
    i360 = [i for i, l in enumerate(ls) if 'No move aimed at the quantifier remains on this board' in l][0]
    for i in range(i360 + 1, len(ls)):
        if re.search(r'quantifier', ls[i], re.I):
            rec('        FINDINGS.md:%d | %s' % (i + 1, ls[i].strip()[:150]))

    rec('')
    rec('(P7) THE SPAN, BY THE TOOL, READ-ONLY.')
    import subprocess
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '447'], capture_output=True,
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
