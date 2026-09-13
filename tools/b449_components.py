# -*- coding: utf-8 -*-
"""b449_components.py -- THE (R61) RECORD RATIFIED UNDER A FACE, AND THE OUTLIER'S INTEGRAND AT ITS AIM. ### **AFTER THE LOCK.**

### Usage: `count` -- Component 1(a), the banks counted beside the record, both controls, into `data/b449_count.json`;
### `loom` -- Component 1(b), one loom block by `b244_loom_append.py`;
### `integrand` -- Component 2 under (R62): the seed and the autocorrelation formed at four levels by b447's code path,
###   the prime channel re-summed as the control, its terms, the one-sided derivatives at v* = ln 17, the node placement,
###   into `data/b449_integrand.json`. No `channels` call; no zero side, pole or archimedean channel;
### `report` -- everything into `data/b449_components.txt`.
"""
import io
import json
import math
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
OUT = os.path.join(D, 'b449_components.txt')
CNT = os.path.join(D, 'b449_count.json')
INT = os.path.join(D, 'b449_integrand.json')
BLOCK = os.path.join(D, 'b449_loom_block.md')
LOOMRUN = os.path.join(D, 'b449_loom_append_run.txt')
CELL = '4.123106'
LEVELS = (8193, 16385, 32769, 65537)
SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def load(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def dump(path, obj):
    io.open(path + '.tmp', 'w', encoding='utf-8').write(json.dumps(obj, indent=1, ensure_ascii=False))
    os.replace(path + '.tmp', path)


# ------------------------------------------------------------------------------------------ COMPONENT 1
def counter(kind=None):
    """### ONE COUNTER, USED FOR THE COUNT AND FOR BOTH CONTROLS."""
    out = dict(candidates=0, held=0, kinds=set(), per={}, total=0)
    for s, p in SITES:
        d = load(p)
        cs = d['candidates']
        h = d.get('held')
        out['held'] += (len(h) if isinstance(h, list) else int(h or 0))
        out['candidates'] += len(cs)
        out['kinds'] |= set(c['kind'] for c in cs)
        k = sum(1 for c in cs if c['kind'] == kind) if kind else 0
        out['per'][s] = (k, len(cs))
        out['total'] += k
    out['kinds'] = sorted(out['kinds'])
    return out


def record_lines():
    ls = io.open(TRAILS, encoding='utf-8').read().splitlines()
    s = [i for i, l in enumerate(ls) if l == '<!-- (R61) the failure-mode partition gets a trigger, not a shelf -->'][0]
    e = s
    while not ls[e].startswith('*The partition row in `FINDINGS.md` is not edited'):
        e += 1
    return s + 1, e + 1, NL.join(ls[s:e + 1])


def per_site(text):
    return dict((m.group(1), (int(m.group(2)), int(m.group(3))))
                for m in re.finditer(r'\((i|ii|iii|iv|v|vi)\) (\d+) of (\d+)', text))


def count():
    lo, hi, rt = record_lines()
    g = lambda pat: (lambda m: int(m.group(1)) if m else None)(re.search(pat, rt))
    rec_fig = dict(
        candidates=g(r'\*\*(\d+)\*\* candidates over six sites'),
        held=g(r'\*\*(\d+)\*\* held'),
        kinds=g(r'\*\*(\d+)\*\* failure kinds'),
        cb_total=g(r'\*\*(\d+) of \d+\*\*, a majority overall'),
        majority_sites=g(r'at \*\*(\d+) of 6\*\* sites'),
        imports=g(r'A further \*\*(\d+)\*\* failed as imports under the bar'),
        per=per_site(rt),
        not_majority=re.findall(r'\((i|ii|iii|iv|v|vi)\)', (re.search(r'it is not the majority at ([^.]*)\.', rt) or [None, ''])[1]))
    cb = counter('CLASS BOUNDARY')
    im = counter('IMPORT UNDER THE BAR')
    neg = counter('NOT A KIND')
    maj = [s for s, (k, n) in cb['per'].items() if 2 * k > n]
    bank = dict(candidates=cb['candidates'], held=cb['held'], kinds=len(cb['kinds']), cb_total=cb['total'],
                majority_sites=len(maj), imports=im['total'], per=cb['per'],
                not_majority=[s for s, _ in SITES if s not in maj])
    rows = []
    for key in ('candidates', 'held', 'kinds', 'cb_total', 'majority_sites', 'imports', 'per', 'not_majority'):
        b, r = bank[key], rec_fig[key]
        if key == 'per':
            b = dict((k, list(v)) for k, v in b.items())
            r = dict((k, list(v)) for k, v in r.items())
        rows.append(dict(figure=key, bank=b, record=r, agree=(b == r)))
    b443 = [l for l in io.open(os.path.join(D, 'b443r_the_arc_product.txt'), encoding='utf-8').read().splitlines()
            if l.startswith('**The class boundary, per site, corrected:**')][0]
    rep443 = per_site(b443)
    pos = dict((s, list(cb['per'][s])) for s, _ in SITES) == dict((s, list(rep443.get(s, (None, None)))) for s, _ in SITES)
    negok = all(k == 0 for k, _n in neg['per'].values()) and neg['total'] == 0
    disc = [r['figure'] for r in rows if not r['agree']]
    ratified = (not disc) and pos
    res = dict(record_lines=[lo, hi], rows=rows, positive=dict(b443=dict((k, list(v)) for k, v in rep443.items()), fires=pos),
               negative=dict(per=dict((k, list(v)) for k, v in neg['per'].items()), fires=negok),
               kinds=cb['kinds'], discrepancies=disc, ratified=ratified)
    dump(CNT, res)
    print('count: discrepancies %s ; positive %s ; negative %s ; ratified %s' % (disc, pos, negok, ratified))
    return 0


def loom():
    b448 = [l for l in io.open(os.path.join(D, 'b448_closing.txt'), encoding='utf-8').read().splitlines() if 'mirror           :' in l][0].strip()
    r61 = [l for l in io.open(os.path.join(D, 'b448_r61_mirror.txt'), encoding='utf-8').read().splitlines() if 'manifest declares source HEAD' in l][0].strip()
    block = NL.join([
        '',
        '<!-- b449 loom entry -->',
        '',
        '### **A MIRROR CHECK WHOSE ARTEFACT IS GONE — noted once, 2026-09-13 (b449)**',
        '',
        'b448’s closing record reads *“%s”* (relay `data/b448_closing.txt`). That check was made on '
        '`D:\\MY-DOwnloads\\mirror-refresh-2026-09-13.zip` as built at PLACE-papers `b1656b1`. Later the same day the '
        '`(R61)` execution rebuilt the mirror at `dc5e18e` (relay `data/b448_r61_mirror.txt`: *“%s”*). `tools/mirror_build.ps1` '
        'names its zip by date alone and removes an existing zip of that name before writing (lines 122–123), so the '
        'rebuild replaced the zip b448 verified. **b448’s check therefore names an artefact no longer on disk.** Its verdict '
        'is not re-read or changed, and b448’s bank is not edited. The builder already takes a `DateTag` parameter (line 4) '
        'that holds two builds from one day apart; the work-order `W-ORD-MIRROR-ZIP-NAME` is filed with b449’s trail record.'
        % (b448, r61),
        ''])
    io.open(BLOCK, 'w', encoding='utf-8', newline=NL).write(block)
    p = subprocess.run([sys.executable, os.path.join(T, 'b244_loom_append.py'), BLOCK], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    io.open(LOOMRUN, 'w', encoding='utf-8', newline=NL).write(p.stdout + p.stderr)
    print(p.stdout + p.stderr)
    return p.returncode


# ------------------------------------------------------------------------------------------ COMPONENT 2
def integrand():
    import numpy as np
    import b317_smear as SM
    import b318_square as SQ
    import b321_window as WI
    a45 = load('b445_arms.json')
    banked = [a45['base'][CELL], a45['a'][CELL], load('b446_doubling.json')[CELL], load('b447_doubling.json')[CELL]]
    a = banked[0]['a']
    vstar = math.log(17.0)
    t0 = time.time()
    g = SM.mean_zero_variant(a)
    lv = []
    for j, nv in enumerate(LEVELS):
        t = time.time()
        f = SQ.autocorrelation(g, nv=nv)
        v, w = np.asarray(f.v), np.asarray(f.w)
        PR, _terms = WI.prime_sum(v, w, 'corpus')
        L = float(v[-1])
        terms = {}
        for p in WI.primes_to(math.exp(L) + WI.PRIME_TOL):
            k = 1
            while p ** k <= math.exp(L) + WI.PRIME_TOL:
                n = p ** k
                ln = math.log(n)
                if ln <= L:
                    terms[n] = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, v, w))
                k += 1
        h = float(v[1] - v[0])
        F = lambda x: float(np.interp(x, v, w, left=0.0, right=0.0))
        Fs = F(vstar)
        Dm = (Fs - F(vstar - h)) / h
        Dp = (F(vstar + h) - Fs) / h
        maxslope = float(np.max(np.abs(np.diff(w)))) / h
        k = int(np.searchsorted(v, vstar))
        left, right = float(v[k - 1]), float(v[min(k, v.size - 1)])
        near = min(abs(vstar - left), abs(right - vstar))
        edge = [float(x) for x in w[-6:]]
        lv.append(dict(nv=nv, size=int(v.size), L=L, vstar=vstar, L_minus_vstar=L - vstar, h=h,
                       prime=PR, prime_banked=banked[j]['prime'], control=abs(PR - banked[j]['prime']),
                       terms=dict((str(n), x) for n, x in sorted(terms.items())), terms_sum=sum(terms.values()),
                       F_vstar=Fs, Dminus=Dm, Dplus=Dp, jump=Dp - Dm, maxslope=maxslope, maxabs=float(np.max(np.abs(w))),
                       node_left=left, node_right=right, index_right=k, near=near,
                       placement='SITS ON' if near <= 1e-12 else 'STRADDLE', edge_values=edge,
                       seconds=round(time.time() - t, 1)))
        print('nv %d : PR %.17e banked %.17e |diff| %.1e ; F(v*) %+.3e D- %+.3e D+ %+.3e ; near %.3e ; %.1fs'
              % (nv, PR, banked[j]['prime'], abs(PR - banked[j]['prime']), Fs, Dm, Dp, near, time.time() - t))
    dump(INT, dict(a=a, sqrt17=math.sqrt(17.0), vstar=vstar, levels=lv, seconds=round(time.time() - t0, 1)))
    return 0


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    C = load('b449_count.json')
    I = load('b449_integrand.json')
    rec('=' * 100)
    rec('b449 -- THE (R61) RECORD RATIFIED UNDER A FACE, AND THE OUTLIER`S INTEGRAND AT ITS AIM. ### THE COMPONENTS, AFTER THE LOCK.')
    rec('=' * 100)

    rec('')
    rec('  ### ### **COMPONENT 1 -- THE (R61) RECORD, VERIFIED UNDER THIS FACE.**')
    rec('    the record read at OPEN_TRAILS.md:%d-%d (not edited)' % tuple(C['record_lines']))
    rec('    %-16s %-44s %-44s %s' % ('figure', 'the banks, counted', 'the record, parsed', 'agree'))
    for r in C['rows']:
        fmt = lambda x: (', '.join('(%s) %d/%d' % (k, v[0], v[1]) for k, v in x.items()) if isinstance(x, dict)
                         else (', '.join('(%s)' % s for s in x) if isinstance(x, list) else str(x)))
        rec('    %-16s %-44s %-44s %s' % (r['figure'], fmt(r['bank'])[:44], fmt(r['record'])[:44], r['agree']))
    rec('    kinds counted : %s' % '; '.join(C['kinds']))
    rec('    POSITIVE CONTROL -- CLASS BOUNDARY per site against b443r_the_arc_product.txt:24 %s : %s'
        % (', '.join('(%s) %d/%d' % (k, v[0], v[1]) for k, v in C['positive']['b443'].items()), 'FIRES' if C['positive']['fires'] else '### DOES NOT FIRE'))
    rec('    NEGATIVE CONTROL -- `NOT A KIND` per site %s : %s'
        % ([v[0] for v in C['negative']['per'].values()], 'ZERO AT ALL SIX' if C['negative']['fires'] else '### NOT ZERO'))
    if C['discrepancies']:
        rec('  ### DISCREPANCIES : %s -- ROUTED, NOT REPAIRED.' % C['discrepancies'])
    else:
        rec('    discrepancies : 0')
    rec('  ### ### **THE (R61) RECORD : %s.**' % ('RATIFIED AT b449' if C['ratified'] else 'NOT RATIFIED'))
    lr = io.open(LOOMRUN, encoding='utf-8').read() if os.path.exists(LOOMRUN) else ''
    rec('    loom note : marker count %d ; appender %s'
        % (io.open(os.path.join(PP, 'VERIFICATION_LOOM.md'), encoding='utf-8').read().count('<!-- b449 loom entry -->'),
           'PREFIX UNCHANGED YES' if 'PREFIX UNCHANGED (pure insertion) : YES' in lr else '### PREFIX NOT PROVED'))
    rec('    W-ORD-MIRROR-ZIP-NAME : filed with the trail record; trigger the next mirror build or the next opening of the')
    rec('    instrument-audit lane; ### THIS ACT`S CLOSING BUILD FIRES IT, and passes -DateTag 2026-09-13-b449; repair NOT made.')

    rec('')
    rec('  ### ### **COMPONENT 2 -- THE OUTLIER`S INTEGRAND, CANDIDATE (c1), UNDER (R62).**')
    lv = I['levels']
    rec('    a (banked, governs) %.6f ; sqrt(17) %.12f ; v* = ln 17 = %.15f ; wall %.1f s' % (I['a'], I['sqrt17'], I['vstar'], I['seconds']))
    ctrl = all(x['control'] <= 1e-15 for x in lv)
    rec('    THE CONTROL -- the prime channel re-summed against its bank:')
    for x in lv:
        rec('      nv %-6d PR %.17e  banked %.17e  |diff| %.1e  terms sum |diff| %.1e'
            % (x['nv'], x['prime'], x['prime_banked'], x['control'], abs(x['terms_sum'] - x['prime'])))
    rec('    ### CONTROL : %s' % ('PASSES AT ALL FOUR LEVELS' if ctrl else '### FAILS -- COMPONENT 2 NOT DECIDED'))
    rec('')
    rec('    THE AIM AND THE ONE-SIDED DERIVATIVES (F = interp with zero beyond the support; h = the level`s node spacing):')
    rec('    %-6s %-12s %-11s %-11s %-11s %-11s %-11s %-10s %-9s' % ('nv', 'L - v*', 'h', 'F(v*)', 'D-', 'D+', 'D+ - D-', 'max|f`|', 'max|f|'))
    for x in lv:
        rec('    %-6d %+.4e  %.4e  %+.3e  %+.3e  %+.3e  %+.3e  %.3e  %.3e'
            % (x['nv'], x['L_minus_vstar'], x['h'], x['F_vstar'], x['Dminus'], x['Dplus'], x['jump'], x['maxslope'], x['maxabs']))
    fin = lv[-1]
    bar = 1e-6 * fin['maxslope']
    kink = abs(fin['jump']) > bar
    rec('    f`s last six node values at nv 65537 : %s' % ['%.2e' % e for e in fin['edge_values']])
    rec('    rule at the finest level: |D+ - D-| %.3e against 1e-6 * max|f`| = %.3e' % (abs(fin['jump']), bar))
    rec('  ### ### **A KINK AT v* : %s.**' % ('YES' if kink else 'NO'))
    rec('')
    rec('    THE NODE PLACEMENT, FROM THE NODE POSITIONS:')
    for x in lv:
        rec('      nv %-6d nodes %d ; about v*: %.15f | %.15f ; nearest %.4e ; %s'
            % (x['nv'], x['size'], x['node_left'], x['node_right'], x['near'], x['placement']))
    place = [x['placement'] for x in lv]
    place_rule = place == ['STRADDLE', 'STRADDLE', 'SITS ON', 'SITS ON']
    rec('    placement (8193, 16385, 32769, 65537) : %s ; the pattern the account requires : %s' % (place, place_rule))
    rec('')
    rec('    THE PRIME CHANNEL`S CHANGE, BY TERM (term = 2 log p / sqrt(n) * interp(ln n, v, w)):')
    ns = list(lv[0]['terms'].keys())
    rec('      %-5s %-14s %-14s %-14s' % ('n', 'step 1', 'step 2', 'step 3'))
    steps = []
    for j in (1, 2, 3):
        d = dict((n, lv[j]['terms'][n] - lv[j - 1]['terms'][n]) for n in ns)
        dpr = lv[j]['prime'] - lv[j - 1]['prime']
        gross = sum(abs(x) for x in d.values())
        top = max(d, key=lambda n: abs(d[n]))
        steps.append(dict(d=d, dpr=dpr, gross=gross, top=top, share17=abs(d['17']) / gross if gross else 0.0,
                          net17=abs(d['17']) / abs(dpr) if dpr else 0.0, topshare=abs(d[top]) / gross if gross else 0.0))
    for n in ns:
        rec('      %-5s %+.4e    %+.4e    %+.4e' % (n, steps[0]['d'][n], steps[1]['d'][n], steps[2]['d'][n]))
    rec('      %-5s %+.4e    %+.4e    %+.4e' % ('dPR', steps[0]['dpr'], steps[1]['dpr'], steps[2]['dpr']))
    for j, s in enumerate(steps):
        rec('      step %d : n=17 share of gross %.4f (of net %.4f) ; largest term n=%s, share of gross %.4f'
            % (j + 1, s['share17'], s['net17'], s['top'], s['topshare']))
    grows17 = abs(steps[1]['d']['17']) > abs(steps[0]['d']['17'])
    c3 = steps[0]['share17'] >= 0.9 and steps[1]['share17'] >= 0.9 and grows17
    rec('    (iii) n=17 carries >= 0.9 of the change at steps 1 and 2 and its own change grows : %s' % c3)
    account = bool(ctrl and kink and place_rule and c3)
    rec('    THE ACCOUNT: (i) kink %s ; (ii) placement %s ; (iii) the n = 17 term %s' % (kink, place_rule, c3))
    if not ctrl:
        mstate = 'NOT DECIDED'
    elif account:
        mstate = 'CLOSES'
    else:
        mstate = 'STAYS OPEN'
    rec('  ### ### **THE KINK AND THE NODE PLACEMENT ACCOUNT FOR THE GROWTH : %s.**' % ('YES' if account else 'NO'))
    rec('  ### ### **THE MEASUREMENT %s.**' % mstate)
    tops = [s['top'] for s in steps]
    g1, g2 = steps[0]['d'][tops[0]], steps[1]['d'][tops[0]]
    rec('    ### READ BESIDE THE RULE, NOT A VERDICT: the largest term at steps 1, 2, 3 is n = %s, %s, %s; the n = %s term`s change'
        % (tops[0], tops[1], tops[2], tops[0]))
    rec('    ### goes %+.3e -> %+.3e between steps 1 and 2.' % (g1, g2))
    for j, st in enumerate(steps):
        pos = max((n for n in ns if st['d'][n] > 0), key=lambda n: st['d'][n], default=None)
        neg = min((n for n in ns if st['d'][n] < 0), key=lambda n: st['d'][n], default=None)
        rec('    ### step %d : gross/net %.3f ; largest positive term n = %s (%+.3e), largest negative n = %s (%+.3e)'
            % (j + 1, st['gross'] / abs(st['dpr']), pos, st['d'][pos], neg, st['d'][neg]))
    rec('    ### so dPR grows from step 1 to step 2 while the n = 2 term`s change halves: at step 1 the n = 3 term`s change')
    rec('    ### offsets most of n = 2`s, and by step 2 it has fallen %.1f-fold. A read of the banked terms, not a verdict on (c2).'
        % (abs(steps[0]['d']['3']) / abs(steps[1]['d']['3'])))
    if mstate == 'STAYS OPEN':
        rec('    ### (c2), the grid`s alignment with a feature, stays PRICED AND NOT RUN: a grid offset the chain does not take,')
        rec('    ### an instrument edit, about four minutes (b447).')
    rec('    ### NO CLAIM ABOUT ZEROS. ### THE INSTRUMENT LANE OPENED BY (R62) CLOSES AT THIS ACT`S END.')

    rec('')
    rec('  ### ### **THE EXPECTATIONS.**')
    n1 = 'HELD' if (C['ratified'] and C['positive']['fires']) else 'REFUTED'
    n2a = 'HELD' if kink else 'REFUTED'
    n2b = 'HELD' if (place[:2] == ['STRADDLE', 'STRADDLE'] and 'STRADDLE' not in place[2:] and mstate == 'CLOSES') else 'REFUTED'
    rec('    (N1)    the banks reproduce the record and the control fires   ### %s' % n1)
    rec('    (N2)(a) the integrand carries a kink at sqrt(17)                ### %s' % n2a)
    rec('    (N2)(b) the first two straddle, the last two do not, it closes  ### %s -- placement %s ; measurement %s' % (n2b, place, mstate))
    seat = dict(n1='HELD', n2a='REFUTED', n2b='REFUTED')
    sc = lambda k, got: 'HELD' if seat[k] == got else 'REFUTED'
    rec('    ### the seat`s own from the face, from reading code: (N1) %s -- %s; (N2)(a) %s -- %s; (N2)(b) %s -- %s.'
        % (seat['n1'], sc('n1', n1), seat['n2a'], sc('n2a', n2a), seat['n2b'], sc('n2b', n2b)))
    rec('')
    rec('    ### NO CHAIN FILE EDITED. ### NO CHANNEL BUT THE PRIME CHANNEL. ### THE (R61) RECORD NOT EDITED. ### NO CLOSING EDITED.')
    rec('    ### NO CLAIM ABOUT RH, h2 OR ANY ZERO. ### THE FOUR LISTS ARE OPEN.')
    rec('=' * 100)
    res = dict(ratified=C['ratified'], discrepancies=C['discrepancies'], control=ctrl, kink=kink, bar=bar,
               jump=fin['jump'], placement=place, place_rule=place_rule, c3=c3, account=account, measurement=mstate,
               steps=[dict(share17=s['share17'], net17=s['net17'], top=s['top'], topshare=s['topshare'], dpr=s['dpr']) for s in steps],
               expect=dict(n1=n1, n2a=n2a, n2b=n2b), seat=seat)
    I['verdict'] = res
    dump(INT, I)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'report'
    sys.exit(dict(count=count, loom=loom, integrand=integrand, report=report)[mode]())
