# -*- coding: utf-8 -*-
"""b446_census.py -- COMPONENT 2: EVERY BANKED COMPARISON AGAINST THE 1.49e-08 FLOOR. ### **AFTER THE LOCK.**

### ### **THE MATCHERS, CONTROLS AND CLASS ARE THE FACE'S, CARRIED, NOT IMPROVED:**
### M0 -- lines carrying RESOLVED, DRIFTING or AT_FLOOR as words (addition (a)'s count, reproduced).
### M1 -- gate verdict instances: a verdict word outside backticks, the stripped line not beginning with `###`,
###       and a numeric literal on the line (a decimal or an exponent literal); an aggregate "N gate verdicts"
###       counts N; distinct by (file stem, whitespace-collapsed line).
### M2 -- floor-arm decisions: M1 instances whose verdict is AT_FLOOR, plus the gate's detail string `<= floor`.
### M3 -- quoted-threshold comparisons: a line naming 1.49e-08, 1.490e-08 or 1.4901e-08 with above, below,
###       under, exceed or floor; distinct by (file stem, line).
### THE KIND: IN if the line or the three lines before it name an eigenvalue, a mode, lam, a spectrum or a
###       singular value; OUT otherwise. ### THE RADIUS READING: VACUOUS -- the floor was measured at no radius.
### ### NOTHING IS RE-VERDICTED. An OUT comparison is the bar quoted outside its scope, and only that.
"""
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b446_floor_census.txt')
OJ = os.path.join(D, 'b446_floor_census.json')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

VERD = ('RESOLVED', 'DRIFTING', 'AT_FLOOR')
NUM = re.compile(r'[-+]?\d+\.\d+|\d+(?:\.\d+)?[eE][-+]?\d+')
AGG = re.compile(r'\b(\d+) gate verdicts\b')
FLOORNUM = re.compile(r'1\.49e-08|1\.490e-08|1\.4901e-08')
CMPWORD = re.compile(r'\b(above|below|under|exceed\w*|floor)\b', re.I)
KIND = re.compile(r'eigen|\bmodes?\b|\blam(?:_n|bda)?\b|spectr|singular value', re.I)
RADIUS = re.compile(r'\ba\s*=\s*([0-9]+(?:\.[0-9]+)?)')


def stem_of(rel):
    m = re.match(r'(?:audit_)?(b\d+)', rel)
    return m.group(1) if m else rel


def outside_backticks(line, word):
    """### True if `word` occurs as a word in the parts of the line that are not inside backticks."""
    parts = line.split('`')
    return any(re.search(r'\b%s\b' % word, p) for i, p in enumerate(parts) if i % 2 == 0)


def files():
    out = []
    for dp, _dn, fn in os.walk(D):
        for f in fn:
            if (f.endswith('.txt') or f.endswith('.json')) and not f.startswith('b446_') and not f.startswith('audit_b446_'):
                out.append(os.path.join(dp, f))
    return sorted(out)


def main():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    m0 = Counter()
    m0_stems = set()
    m1 = {}
    m2 = {}
    m3 = {}
    for p in files():
        rel = os.path.relpath(p, D).replace(os.sep, '/')
        st = stem_of(rel)
        ls = io.open(p, encoding='utf-8', errors='replace').read().splitlines()
        for i, l in enumerate(ls):
            toks = [v for v in VERD if re.search(r'\b%s\b' % v, l)]
            if toks and p.endswith('.txt'):
                for v in toks:
                    m0[v] += 1
                m0_stems.add(st)
            ctx = ' '.join(ls[max(0, i - 3):i + 1])
            kind = 'IN' if KIND.search(ctx) else 'OUT'
            rad = RADIUS.search(l)
            key = (st, re.sub(r'\s+', ' ', l.strip()))
            live = [v for v in toks if outside_backticks(l, v)]
            if live and not l.strip().startswith('###') and (NUM.search(l) or AGG.search(l)):
                ag = AGG.search(l)
                n = int(ag.group(1)) if ag else 1
                if key not in m1:
                    m1[key] = dict(file=rel, line=i + 1, stem=st, verdicts=live, n=n, kind=kind,
                                   radius=rad.group(1) if rad else None, text=l.strip()[:160])
                if 'AT_FLOOR' in live and key not in m2:
                    m2[key] = dict(file=rel, line=i + 1, why='AT_FLOOR verdict')
            if '<= floor' in l and key not in m2:
                m2[key] = dict(file=rel, line=i + 1, why='detail string <= floor', text=l.strip()[:160])
            if FLOORNUM.search(l) and CMPWORD.search(l):
                if key not in m3:
                    m3[key] = dict(file=rel, line=i + 1, stem=st, kind=kind, radius=rad.group(1) if rad else None,
                                   concluded=sorted(set(w.lower() for w in CMPWORD.findall(l))), text=l.strip()[:160])

    rec('=' * 100)
    rec('b446 -- COMPONENT 2: THE CENSUS OF COMPARISONS AGAINST 1.49e-08. ### AFTER THE LOCK.')
    rec('=' * 100)
    rec('  population : %d files under relay/data (.txt and .json), b446`s own excluded' % len(files()))
    rec('')
    rec('  ### THE MATCHERS` YIELDS, EACH PRINTED:')
    rec('    M0 word-lines : RESOLVED %d ; DRIFTING %d ; AT_FLOOR %d ; over %d stems (%d act stems)'
        % (m0['RESOLVED'], m0['DRIFTING'], m0['AT_FLOOR'], len(m0_stems), sum(1 for s in m0_stems if re.fullmatch(r'b\d+', s))))
    inst = Counter()
    for v in m1.values():
        for t in v['verdicts']:
            inst[t] += v['n']
    rec('    M1 gate verdict instances : %d distinct lines carrying %d verdicts -- RESOLVED %d ; DRIFTING %d ; AT_FLOOR %d'
        % (len(m1), sum(inst.values()), inst['RESOLVED'], inst['DRIFTING'], inst['AT_FLOOR']))
    rec('    M2 floor-arm decisions : %d' % len(m2))
    rec('    M3 quoted-threshold comparisons : %d distinct lines' % len(m3))

    rec('')
    rec('  ### THE CONTROLS:')
    pos1 = sum(1 for v in m1.values() if v['file'] == 'b437_closing.txt' and v['radius'] in ('5.196152', '5.385165', '5.567764')) == 3
    pos2 = any(v['file'] == 'b444_closing.txt' and 'above the 1.49e-08 floor at 14 of 22 cells' in v['text'] for v in m3.values())
    neg = not any(v['stem'] == 'b272' and 'AT_FLOOR' in v['verdicts'] for v in m1.values())
    rec('    positive -- b437`s three RESOLVED lines at the crossing in M1 : %s' % pos1)
    rec('    positive -- b444`s "above the 1.49e-08 floor at 14 of 22 cells" in M3 : %s' % pos2)
    rec('    negative -- b272`s AT_FLOOR definition lines NOT in M1 : %s' % neg)
    controls = pos1 and pos2 and neg
    rec('    ### CONTROLS : %s' % ('PASS -- THE COUNTS ARE BANKED' if controls else '### FAIL -- NOT BANKED AS A COUNT; A MATCHER DEFECT'))

    rec('')
    rec('  ### THE DOMAIN OF KIND:')
    k1 = Counter(v['kind'] for v in m1.values())
    k1n = Counter()
    for v in m1.values():
        k1n[v['kind']] += v['n'] * len(v['verdicts'])
    k3 = Counter(v['kind'] for v in m3.values())
    allc = len(m1) + len(m3)
    out_c = k1['OUT'] + k3['OUT']
    rec('    M1 lines : IN %d ; OUT %d   (verdicts : IN %d ; OUT %d)' % (k1['IN'], k1['OUT'], k1n['IN'], k1n['OUT']))
    rec('    M3 lines : IN %d ; OUT %d' % (k3['IN'], k3['OUT']))
    rec('    ALL COMPARISONS (M1 lines + M3 lines) : %d ; IN %d ; OUT %d ; OUT share %.3f'
        % (allc, allc - out_c, out_c, (out_c / allc) if allc else 0))
    rec('    ### THE RADIUS READING : every one of the %d lies outside a radius domain, because the floor was measured at no' % allc)
    rec('    ### radius -- VACUOUS, printed beside and not scored as a finding.')
    rec('')
    rec('  ### ### **WHAT THE FLOOR ARM DECIDED : %d. ### WHAT THE DRIFT ARM REFUSED : %d. ### WHAT PASSED BOTH : %d.**'
        % (len(m2), inst['DRIFTING'], inst['RESOLVED']))
    rec('  ### NOTHING IS RE-VERDICTED; an OUT comparison is the bar quoted outside its scope, and only that.')

    rec('')
    rec('  ### THE LIST, PER ACT (act ; comparisons ; IN ; OUT ; radii carried ; what the comparisons concluded):')
    per = defaultdict(lambda: dict(n=0, IN=0, OUT=0, radii=set(), concl=Counter()))
    for v in m1.values():
        r = per[v['stem']]
        r['n'] += 1
        r[v['kind']] += 1
        if v['radius']:
            r['radii'].add(v['radius'])
        for t in v['verdicts']:
            r['concl'][t] += v['n']
    for v in m3.values():
        r = per[v['stem']]
        r['n'] += 1
        r[v['kind']] += 1
        if v['radius']:
            r['radii'].add(v['radius'])
        r['concl']['quoted: ' + '/'.join(v['concluded'])] += 1
    for st in sorted(per, key=lambda s: (int(s[1:]) if re.fullmatch(r'b\d+', s) else 10 ** 6, s)):
        r = per[st]
        rads = sorted(r['radii'], key=float)
        rec('    %-26s %4d  IN %-4d OUT %-4d radii %-28s %s' % (st[:26], r['n'], r['IN'], r['OUT'],
            (','.join(rads[:4]) + ('..(%d)' % len(rads) if len(rads) > 4 else '')) or '-',
            '; '.join('%s %d' % kv for kv in sorted(r['concl'].items()))))

    rec('')
    rec('  ### EVERY COMPARISON, ONE LINE EACH (file:line ; kind ; radius ; text):')
    for v in sorted(list(m1.values()) + list(m3.values()), key=lambda x: (x['file'], x['line'])):
        rec('    %s:%d ; %s ; %s ; %s' % (v['file'], v['line'], v['kind'], v['radius'] or '-', v['text'][:120]))
    rec('')
    rec('  ### THE FLOOR ARM`S DECISIONS, EVERY ONE:')
    for v in m2.values():
        rec('    %s:%d ; %s' % (v['file'], v['line'], v['why']))
    if not m2:
        rec('    NONE FOUND.')
    rec('')
    rec('  ### ### **RESIDUE -- READ BEYOND THE FACE`S MATCHERS, PRINTED AND NOT GOVERNING (BAR 3, BAR 10).**')
    jv = Counter()
    jfiles = Counter()
    jwhy = Counter()
    for p in files():
        if not p.endswith('.json'):
            continue
        ls = io.open(p, encoding='utf-8', errors='replace').read().splitlines()
        for i, l in enumerate(ls):
            mm = re.search(r'"verdict": "(RESOLVED|DRIFTING|AT_FLOOR)"', l)
            if mm:
                jv[mm.group(1)] += 1
                jfiles[os.path.relpath(p, D).replace(os.sep, '/')] += 1
                if mm.group(1) == 'AT_FLOOR':
                    nxt = ' '.join(ls[i:i + 2])
                    w = re.search(r'"why": "([^"]*)"', nxt)
                    jwhy[w.group(1) if w else '?'] += 1
    rec('    (r1) STRUCTURED GATE RECORDS IN JSON, `"verdict": "X"` -- M1 cannot see them (no numeric literal on the')
    rec('         verdict line), and M2`s line dedup folds identical ones: RESOLVED %d ; DRIFTING %d ; AT_FLOOR %d, in %d files'
        % (jv['RESOLVED'], jv['DRIFTING'], jv['AT_FLOOR'], len(jfiles)))
    for w, n in jwhy.items():
        rec('         every AT_FLOOR record`s reason : %d x "%s"' % (n, w))
    zero_only = bool(jwhy) and all('abs(value) = 0.000000e+00' in w for w in jwhy)
    rec('         ### ALL AT_FLOOR RECORDS ARE ON A VALUE OF EXACTLY ZERO : %s -- ANY POSITIVE FLOOR REFUSES THEM, SO THE' % zero_only)
    rec('         ### FLOOR`S SIZE DECIDED NONE OF THEM.' if zero_only else '         ### SOME AT_FLOOR RECORDS ARE ON A NONZERO VALUE.')
    prose = [v for v in m1.values() if not re.search(r'->|drift|abs\(value\)|verdict|\[RESOLVED|\[DRIFTING|RESOLVED\s*$|DRIFTING\s*$|RESOLVED  |DRIFTING  ', v['text'])]
    rec('    (r2) M1 LINES WITHOUT A GATE-ROW MARK (arrow, drift, abs(value), verdict, bracket, or the word ending the row),')
    rec('         for a hand read -- the English word, not a verdict, may be what M1 caught : %d' % len(prose))
    for v in prose[:40]:
        rec('         %s:%d | %s' % (v['file'], v['line'], v['text'][:110]))
    spec = [v for v in m1.values() if v['stem'] == 'b264' and v['kind'] == 'OUT']
    rec('    (r3) THE KIND RULE`S THREE-LINE WINDOW LOSES A TABLE`S HEADING: b264`s own mode-table rows classed OUT : %d' % len(spec))
    rec('         (they are eigenvalue rows -- the floor`s own domain). With them read IN, OUT would be %d of %d, share %.3f.'
        % (out_c - len(spec), allc, ((out_c - len(spec)) / allc) if allc else 0))
    dup = [v for v in m1.values() if v['n'] > 1]
    rec('    (r4) AGGREGATE LINES COUNTED N EACH : %s -- the same run`s aggregate banked in more than one file counts again.'
        % ['%s:%d x%d' % (v['file'], v['line'], v['n']) for v in dup])
    J_res = dict(json_verdicts=dict(jv), json_files=len(jfiles), at_floor_reasons=dict(jwhy), at_floor_zero_only=zero_only,
                 m1_unmarked=len(prose), b264_rows_out=len(spec), aggregates=[[v['file'], v['line'], v['n']] for v in dup])
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    J = dict(m0=dict(m0), m0_stems=len(m0_stems), m0_act_stems=sum(1 for s in m0_stems if re.fullmatch(r'b\d+', s)),
             m1_lines=len(m1), m1_verdicts=dict(inst), m2=len(m2), m3_lines=len(m3),
             controls=dict(pos_b437=pos1, pos_b444=pos2, neg_b272=neg, ok=controls),
             kind=dict(m1_lines=dict(k1), m1_verdicts=dict(k1n), m3_lines=dict(k3), all=allc, out=out_c),
             per_act={k: dict(n=v['n'], IN=v['IN'], OUT=v['OUT']) for k, v in per.items()},
             floor_arm=list(m2.values()), residue=J_res)
    io.open(OJ + '.tmp', 'w', encoding='utf-8').write(json.dumps(J, indent=1))
    os.replace(OJ + '.tmp', OJ)
    return 0 if controls else 2


if __name__ == '__main__':
    sys.exit(main())
