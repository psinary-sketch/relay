# -*- coding: utf-8 -*-
"""b444_components.py -- THE COMPONENTS. ### **RUN AFTER THE LOCK.**
### ### COMPONENT 2 FIRST: the transform exactly as the face fixed it -- T1, T2, T3 -- on banked columns only.
### ### COMPONENT 1: the fold's rows, each verdict string verified by exact match in its own bank; the span
### counted three ways; the one statement; the work-order. `b444_fold.py` writes them.
"""
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
OUT = os.path.join(D, 'b444_components.txt')
NL = chr(10)
FLOOR = 1.49e-08

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy) if sxx > 0 and syy > 0 else float('nan')


def component_2():
    rec('=' * 100)
    rec('  ### ### **COMPONENT 2 -- THE CHANNELS DECORRELATED, BY THE TRANSFORM THE FACE FIXED**')
    rec('=' * 100)
    rows = [r for r in json.loads(read(os.path.join(D, 'b437_rungs.json')))['rows'] if r.get('zero') is not None]
    rec('    table : %d full cells from b437_rungs.json ; ### THE ZERO CHANNEL IS INHERITED from the atlas`s zero list.' % len(rows))
    chart = json.loads(read(os.path.join(D, 'b334_chart.json')))['block']
    rec('    aim map : %d cells at a in %s, no zero channel, radius overlap with the table %s ### KEPT APART.'
        % (len(chart), sorted(set(c['a'] for c in chart)), sorted(set(c['a'] for c in chart) & set(r['a'] for r in rows))))
    if len(rows) < 3:
        rec('    ### NOT APPLICABLE -- fewer than three full cells.')
        return dict(verdict='NOT APPLICABLE')
    a = [r['a'] for r in rows]
    Z = [r['zero'] for r in rows]
    P = [r['pole'] for r in rows]
    PR = [r['pr'] for r in rows]
    A = [r['arch'] for r in rows]
    RB = [r['resid'] for r in rows]
    B = [r['bound'] for r in rows]

    rec('')
    rec('  ### T1 -- THE CORRELATION STRUCTURE, AS MEASURED (Pearson r over %d cells)' % len(rows))
    names = [('a', a), ('Z', Z), ('PR', PR), ('A', A)]
    rec('         ' + ''.join('%10s' % n for n, _ in names))
    t1 = {}
    for n1, v1 in names:
        line = '    %4s ' % n1
        for n2, v2 in names:
            r_ = pearson(v1, v2)
            t1['%s,%s' % (n1, n2)] = r_
            line += '%10.4f' % r_
        rec(line)
    pmax = max(abs(p) for p in P)
    rec('    P (pole) : max |P| = %.3e -- %s the bar at every cell, so it is not correlated (face, T1).'
        % (pmax, 'BELOW' if pmax <= FLOOR else 'NOT below'))

    rec('')
    rec('  ### T2 -- THE SHARED VARIATION REMOVED: e = Z - (P - PR + A), RECOMPUTED AND CHECKED AGAINST THE BANK')
    e = [z - (p - pr + ar) for z, p, pr, ar in zip(Z, P, PR, A)]
    dev = max(abs(x - y) for x, y in zip(e, RB))
    rec('    max |e - banked resid| = %.3e against 1e-15 : %s' % (dev, 'MATCHES' if dev <= 1e-15 else 'DISAGREES'))
    if dev > 1e-15:
        rec('    ### NOT APPLICABLE -- THE BANK AND ITS CHANNELS DISAGREE.')
        return dict(verdict='NOT APPLICABLE', dev=dev)

    rec('')
    rec('  ### T3 -- WHAT THE RESIDUAL CARRIES')
    rec('    %-10s %-14s %-14s %-12s %-12s %s' % ('a', 'e', '|e| / floor', 'bound', 'Z', 'above floor'))
    above = []
    for r, ei in zip(rows, e):
        ab = abs(ei) > FLOOR
        if ab:
            above.append((r['a'], ei))
        rec('    %-10.6f %-+14.3e %-14.2f %-12.2e %-12.6f %s' % (r['a'], ei, abs(ei) / FLOOR, r['bound'], r['zero'], ab))
    t3 = dict(r_a=pearson(e, a), r_Z=pearson(e, Z), r_PR=pearson(e, PR), r_A=pearson(e, A))
    rec('    r(e, a) %.4f ; r(e, Z) %.4f ; r(e, PR) %.4f ; r(e, A) %.4f' % (t3['r_a'], t3['r_Z'], t3['r_PR'], t3['r_A']))
    signs = ''.join('+' if x > 0 else '-' for x in e)
    changes = sum(1 for i in range(1, len(signs)) if signs[i] != signs[i - 1])
    rec('    sign sequence along a : %s ; sign changes %d' % (signs, changes))
    rec('    the zero-side truncation bound, for scale : max %.2e (never the bar)' % max(B))
    rec('    b437`s refinement deltas on the RATIO, printed beside and not used : 6.34e-07, 6.40e-07, 2.30e-07')
    rec('')
    if not above:
        verdict = 'NOTHING ABOVE THE FLOOR'
        rec('  ### ### **VERDICT : NOTHING ABOVE THE FLOOR.** Every |e| is at or below 1.49e-08; the transform ran and is empty.')
    else:
        verdict = 'STRUCTURE'
        mx = max(abs(x) for _, x in above)
        rec('  ### ### **VERDICT : STRUCTURE -- ABOVE THE FLOOR AT %d OF %d CELLS**, the largest %.3e, %.1f times the floor.'
            % (len(above), len(rows), mx, mx / FLOOR))
        rec('    ### WHAT IT IS, AS MEASURED: the part of the zero channel the identity does not carry, at the size above,')
        rec('    ### with the correlations and sign pattern printed. ### **WHETHER IT IS THE OBJECT`S IS NOT DECIDED.**')
        rec('    ### WHAT WOULD DECIDE: re-run the same chain at these cells on a refined autocorrelation grid and a wider')
        rec('    ### frequency window -- b437`s refinement, applied to e rather than the ratio -- and see whether e moves.')
        rec('    ### A residual that moves with the grid is the instrument`s quadrature; one that stays is a candidate for')
        rec('    ### the object. ### **PRICED: a measurement, blocked by the parked instrument lane. NOT RUN.**')
    rec('    ### NO CLAIM ABOUT ZEROS IS MADE IN THIS BRANCH OR ANY OTHER; the zero side is inherited.')
    out = dict(verdict=verdict, cells=len(rows), dev=dev, t1=t1, t3=t3, signs=signs, sign_changes=changes,
               above=[dict(a=x, e=y, ratio=abs(y) / FLOOR) for x, y in above], e=list(zip(a, e)),
               pole_max=pmax, bound_max=max(B), floor=FLOOR)
    json.dump(out, io.open(os.path.join(D, 'b444_decorrelation.json'), 'w', encoding='utf-8'), indent=1)
    return out


ROWS = [
    ('b433', 'b433_closing.txt', 'the five rulings executed', 'every repair append-or-narrow, original preserved : True    HELD', 'RECORD', ''),
    ('b434', 'b434_closing.txt', 'the fold of b423-b432 -- THE PRIOR FOLD`S FILING ACT', 'the span counts TEN', 'RECORD',
     'filed the previous fold; its lore was folded there and is not folded again'),
    ('b435', 'b435_closing.txt', 'the cure shared, and the skips that print like passes', 'BOTH EXPECTATIONS HELD', 'RECORD', ''),
    ('b436', 'b436_closing.txt', 'the witness arc at site (iv), the window', '7 candidates, 0 held', 'RECORD',
     'BORDERLINE -- it tested an elementary bound on the model`s prime sum; counted RECORD, as a site of the witness arc'),
    ('b437', 'b437_closing.txt', 'the window opened by rungs', 'it peaks at 0.875425 (a = 4.0) and falls', 'MODEL', ''),
    ('b438', 'b438_closing.txt', 'what alternates the sign, and where the room closes', '(N2)(a) the zero belongs to the interaction', 'MODEL', ''),
    ('b439', 'b439_closing.txt', 'the fixed profile, the fixed point, and one arithmetic claim', '(N1)(a) the profile is FIXED in s', 'MODEL', ''),
    ('b440', 'b440_closing.txt', 'the fixed point named, the break attributed, and two facts built', 'HOLDS AS MATHEMATICS, AND', 'MODEL', ''),
    ('b441', 'b441_closing.txt', 'the identification filed, the overstatement corrected, and two filings',
     'VERDICT: THE RECORD NEVER DENIED THE IDENTIFICATION.', 'MODEL',
     'BORDERLINE -- it also corrected the record`s reading of a line and a defect`s reach; counted MODEL, for its measured counting half'),
    ('b442', 'b442_closing.txt', 'the minimum named, and site (v)', 'u0 IS THE MINIMUM OF THE RIEMANN-SIEGEL theta ON 0 <= t <= 50. HOLDS, WITH ITS QUANTIFIER.', 'MODEL',
     'BORDERLINE -- it also ran site (v); counted MODEL, for the name'),
    ('b443', 'b443r_closing.txt', 'site (vi), and the arc`s product named -- re-issued on a fresh face',
     '10 candidates, 0 held: ABSENT 4; CLASS BOUNDARY 4; FORM 1; IMPORT UNDER THE BAR 1.', 'RECORD', ''),
]


def component_1():
    rec('')
    rec('=' * 100)
    rec('  ### ### **COMPONENT 1 -- THE FOLD, b433 THROUGH b443**')
    rec('=' * 100)
    r = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=ROOT)
    io.open(os.path.join(D, 'b444_span.txt'), 'w', encoding='utf-8', newline=NL).write(r.stdout or '')
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', r.stdout or '')
    tool_count = int(m.group(1)) if m else None
    fnd = read(os.path.join(PP, 'FINDINGS.md'))
    heads = [ln for ln in fnd.splitlines() if ln.startswith('## ') and ('THE FOLD' in ln or 'folded at' in ln)]
    matched = [h for h in heads if re.search(r'— THE FOLD\s*$', h)]
    rule_start, act = 435, 444
    rule_count = act - rule_start
    rec('    span by the tool                 : %s (from b423 -- it reads %d of %d fold headings; it misses b434`s)'
        % (tool_count, len(matched), len(heads)))
    rec('    span by the tool`s own rule      : %d (b435-b443: start = b434 + 1)' % rule_count)
    rec('    span by the order                : 11 (b433-b443: adds b433, in no fold, and b434, the prior filer)')
    rec('    ### b443`s closing called 11 the record`s convention: WRONG, CORRECTED HERE, b443`s bank unedited.')
    rows, verified = [], 0
    rec('')
    for act_, bank, subj, needle, col, note in ROWS:
        txt = read(os.path.join(D, bank))
        ok = needle in txt
        verified += ok
        rec('    %-5s %-7s %-6s %s' % (act_, 'VERIFIED' if ok else 'NOT VERIFIED', col, needle[:80]))
        rows.append(dict(act=act_, bank=bank, subject=subj, verdict=needle if ok else None, column=col, note=note))
    cols = {}
    for rw in rows:
        cols[rw['column']] = cols.get(rw['column'], 0) + 1
    rec('    strings verified : %d of %d ; columns OBJECT %d, MODEL %d, RECORD %d'
        % (verified, len(rows), cols.get('OBJECT', 0), cols.get('MODEL', 0), cols.get('RECORD', 0)))
    sites = json.loads(read(os.path.join(D, 'b443r_site_vi.json')))
    t = sites['tallies']
    in_span = sum(sum(t[k].values()) for k in ('b436', 'b442', 'b443'))
    rec('    witness candidates in the span (sites iv-vi) : %d ; across six sites : %d ; union of kinds %d'
        % (in_span, sites['total'], sites['union6']))
    one = ('**In this arc the witness enumeration closed and the archimedean channel got a name.** Sites (iv)–(vi) '
           'exhausted %d candidates with no witness held; with sites (i)–(iii), folded at b434 and cited here, the '
           'enumeration completed at six sites, %d candidates, and a closed taxonomy of %d failure kinds. The channel '
           'was identified as twice the Riemann–Siegel theta’s derivative — a verified source’s statement, carried at '
           'K5 — its sign change named as theta’s minimum on `0 ≤ t ≤ 50`, and the counting half measured with the '
           'pole as its constant. The navigator’s premises were withdrawn where the seat refuted them, and the '
           'seat’s own sentences were corrected where they were wrong.' % (in_span, sites['total'], sites['union6']))
    cited = ('*Folded at b434 and cited, not folded again: two external proofs graded and the discipline calibrated '
             'symmetric (b429, b430); the corpus’s own terminal found NOT THE CLAIM against its own prose (b430); a '
             'keystone lemma named for a theorem it does not invoke (b431).*')
    rec('    one statement composed ; prior-fold clauses cited : True')
    wo = ('**W-ORD-SPAN-HEADING.** `tools/b363_span.py` finds fold sections by `^## .*— THE FOLD\\s*$` and so misses '
          'b434’s heading, *"The external-grading arc — b423 through b432, folded at b434"*, reading a span of 21 where '
          'its own rule gives 9. **The repair:** read every fold heading the record carries, in both forms, and print '
          'any heading it cannot parse rather than skip it. **Trigger:** the next act that opens the instrument lane, or '
          'the next fold, whichever comes first. This fold’s own heading is written in the form the tool reads.')
    out = dict(rows=rows, verified=verified, columns=cols, span=dict(tool=tool_count, rule=rule_count, order=11),
               one=one, cited=cited, work_order=wo, in_span=in_span, total=sites['total'], union=sites['union6'],
               headings_matched=len(matched), headings=len(heads))
    json.dump(out, io.open(os.path.join(D, 'b444_fold.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    return out


def main():
    rec('b444 -- THE FOLD, AND THE CHANNELS DECORRELATED. ### THE COMPONENTS, RUN AFTER THE LOCK.')
    c2 = component_2()
    c1 = component_1()
    rec('')
    rec('=' * 100)
    rec('  ### ### **C2 VERDICT : %s ; C1 strings %d of %d verified ; span tool %s / rule %s / order 11**'
        % (c2['verdict'], c1['verified'], len(c1['rows']), c1['span']['tool'], c1['span']['rule']))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)


if __name__ == '__main__':
    main()
