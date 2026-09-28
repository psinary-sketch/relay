# -*- coding: utf-8 -*-
"""b553_record.py -- THE CASCADE, ACT SEVEN: THE_KEYSTONE_CENSUS RE-RUN LIVE; THE SUPERSESSION RULE; THE OLDER CONFLICT; THE
PER-ZERO CORRECTION; H4 RESTATED AS H7 FROM THE PRINTED TRANSFORM; THE BRIDGE RE-ROUTED IN PRICE: THE RECORD, UNDER (R163).
### `python tools/b553_record.py reads | supersede_test | row393 | readme | older_conflict | corrections | period_fine |
### powerlimit_read | bridge | census | ancestry | anomaly | census_v02 | findings | components | desk | trail`
### The tool edit, the commits, pushes and branch commands are the seat`s. This file deletes nothing.
"""
import io, json, math, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP, GS, LV, EF, TRIAL, CORR = P.PP, P.GS, P.LV, P.EF, P.TRIAL, P.CORR
KER = os.path.join(DD, 'SIDE-kernel')
FIND, OT = P.FIND, P.OT
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
README = os.path.join(T, 'corr_row.README.md')
NL = chr(10)
rd, g, cite, append_to, guard_absent, line_of, poss, outside_bt = P.rd, P.g, P.cite, P.append_to, P.guard_absent, P.line_of, P.poss, P.outside_bt
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    open(os.path.join(D, n), 'wb').write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def put_txt(n, lines):
    open(os.path.join(D, n), 'wb').write((NL.join(lines) + NL).encode('utf-8'))


def lines_with(path, pat):
    return [i + 1 for i, l in enumerate(rd(path).split(NL)) if re.search(pat, l)]


# ------------------------------------------------------------------------------ THE READS
def reads():
    L = ['b553 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    tt = os.path.join(T, 'terminal_table.py')
    src = subprocess.run(['git', '-C', ROOT, 'show', 'a5a4eb43:tools/terminal_table.py'], capture_output=True).stdout.decode('utf-8')  # ### b552`s close, before the edit
    c = [i + 1 for i, l in enumerate(src.split(NL)) if "('CONFLICT' if len(distinct) > 1" in l][0]
    gp = [i + 1 for i, l in enumerate(src.split(NL)) if l.startswith('def grade_cells(')][0]
    cite(L, tt, c - 13, c + 3, 'terminal_table.py AT HEAD BEFORE THE EDIT: the CONFLICT rule', text=src)
    cite(L, tt, gp, gp + 28, 'terminal_table.py AT HEAD BEFORE THE EDIT: the grade parser', text=src)
    for n in (391, 392):
        ln = lines_with(CORR, r'^\| %d \|' % n)[0]
        cite(L, CORR, ln, ln, 'CORRESPONDENCE.md row %d' % n)
    cite(L, README, 1, 1, 'corr_row.README.md')
    cite(L, FIND, 5529, 5533, 'the detection-geometries entry; :5533 carries "read per zero (R131)"')
    b546 = lines_with(OT, r'^### b546 ')
    L.append('### OPEN_TRAILS b546`s record at :%s' % b546)
    cite(L, os.path.join(D, 'b546_ferry.txt'), 55, 62, 'b546`s ferry: "with the detection width read per zero (R131)"')
    for f, a, z in (('tools/b521_tail.py', 45, 53), ('tools/b521_tail.py', 95, 107), ('tools/b519_window.py', 59, 66),
                    ('tools/b519_window.py', 76, 93), ('tools/b519_window.py', 120, 135), ('tools/b514_window.py', 90, 95),
                    ('tools/b522_reach.py', 21, 21)):
        cite(L, os.path.join(ROOT, f), a, z, 'the ladder`s window and orbit term')
    cite(L, os.path.join(D, 'b548_interference.txt'), 64, 77, 'b548`s banked columns (the 29.55 orbit; the pair)')
    cite(L, OT, 11265, 11267, 'OPEN_TRAILS: the bridge`s leading item (b552)')
    cite(L, CENSUS, 1, 237, 'THE_KEYSTONE_CENSUS.md entire (v0.1)')
    L += ['### the act-3 detector: none banked in relay (tools/b375_population.py reconciles three tests and is not it); rebuilt '
          'in this file (census) as §0 operationalises it', '']
    reg = rd(os.path.join(PP, 'REGISTRY.md')).split(NL)
    L += ['### REGISTRY.md rows naming SIDE-kernel with a version:'] + ['  :%d %s' % (i + 1, l[:260]) for i, l in enumerate(reg) if 'SIDE-kernel' in l and re.search(r'v1\.\d', l)][:8]
    L += ['### SIDE-kernel HEAD %s (%s) ; tags by date: %s ; describe: %s' % (
        g(KER, 'rev-parse', 'HEAD').strip(), g(KER, 'log', '-1', '--format=%ci').strip(), ' '.join(g(KER, 'tag', '--sort=-creatordate').split()[:8]),
        g(KER, 'describe', '--tags', '--abbrev=0', 'HEAD').strip())]
    put_txt('b553_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1: THE SUPERSESSION RULE
def snapshot():
    t = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = t.get('rows', t) if isinstance(t, dict) else t
    return {'%s|%s' % (r['repo'], r['name']): r['grade'] for r in rows if isinstance(r, dict) and 'name' in r}


def regen():
    return subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace').returncode


BOOL = 'SIDE-global-section|AggregationCircularityShadow.boolGrp'


def row393_cells():
    ap = rd(os.path.join(GS, 'AXIOM_PRINTS.txt')).split(NL)
    ln = [i + 1 for i, l in enumerate(ap) if l.startswith("'AggregationCircularityShadow.boolGrp'")][0]
    return ['393',
            ('boolGrp’S GRADE UNDER THE SUPERSESSION RULE (b553, under (R163)(1)): this row`s grade cell replaces row 391`s for the '
             'table; rows 391 and 392 stand unedited above.').replace('`', '’'),
            '`Core/AggregationCircularityShadow.lean` -- the definition `boolGrp : Grp Bool`',
            '*does not depend on any axioms* -- `AXIOM_PRINTS.txt`:%d' % ln,
            'SUPERSEDES row 391: SHELL -- `boolGrp`',
            'Written 2026-09-28 (b553) through `relay/tools/corr_row.py`; the rule is `supersede` in `relay/tools/terminal_table.py` and a line of `relay/tools/corr_row.README.md`.']


def row393():
    import corr_row as CR
    import terminal_table as TT
    before = jl('b553_table_before.json')['grades']
    rc0 = regen()
    noop = snapshot()
    num = max(CR.numbers_in(rd(CORR))) + 1
    assert num == 393, num
    cells = row393_cells()
    bad = [i for i, c in enumerate(cells) if i != 4 and TT.GRADE_RE.search(c)]
    assert not bad, bad
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8', errors='replace')
    rc1 = regen()
    after = snapshot()
    t = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = t.get('rows', t) if isinstance(t, dict) else t
    brow = [x for x in rows if isinstance(x, dict) and '%s|%s' % (x['repo'], x['name']) == BOOL][0]
    changed = sorted(k for k in after if after[k] != before.get(k))
    noop_changed = sorted(k for k in noop if noop[k] != before.get(k))
    cb = sorted(k for k, v in before.items() if v == 'CONFLICT')
    ca = sorted(k for k, v in after.items() if v == 'CONFLICT')
    out = dict(number=num, cells=cells, rc=r.returncode, stdout=r.stdout, regen=[rc0, rc1], rows=len(after),
               noop_changed=noop_changed, changed={k: [before.get(k), after[k]] for k in changed}, conflicts_before=cb, conflicts_after=ca,
               boolgrp_after=dict(grade=brow['grade'], cells=[(c['grade'], c['line'], c['quote'][:120]) for c in brow['grade_cells']]))
    put_json('b553_supersede.json', out)
    L = ['b553 -- COMPONENT 1: THE SUPERSESSION RULE, ITS TEST (READING (1))', '',
         '### the table before the edit (data/b553_table_before.json): %d rows ; CONFLICT %d' % (len(before), len(cb))] + ['    ' + k for k in cb] + [
         '### after the edit, before row 393 (the no-op test): grades changed %s' % (noop_changed or 'NONE'),
         '### row 393 written by corr_row.py (exit %d): %s' % (r.returncode, ' | '.join(cells)),
         '### after row 393: %d rows ; CONFLICT %d' % (len(after), len(ca))] + ['    ' + k for k in ca] + [
         '### terminals whose grade changed: %s' % ({k: '%s -> %s' % tuple(v) for k, v in out['changed'].items()} or 'NONE'),
         '### boolGrp now: %s ; its cells %s' % (brow['grade'], out['boolgrp_after']['cells'])]
    put_txt('b553_supersede.txt', L)
    print(NL.join(L))


RDM = ('b553 (2026-09-28), under the author`s ruling (R163)(1): a grade cell reading "SUPERSEDES row N: <grade>" replaces row N`s '
       'grade for tools/terminal_table.py (its rule `supersede`) and is itself the terminal`s grade; the ledger stays append-only.')


def readme():
    t = rd(README)
    if poss(RDM) in t:
        sys.exit('### ALREADY PRESENT')
    before = open(README, 'rb').read()
    open(README, 'ab').write((poss(RDM) + NL).encode('utf-8'))
    after = open(README, 'rb').read()
    put_json('b553_readme.json', dict(prefix=after.startswith(before), lines=len([l for l in rd(README).split(NL) if l.strip()]), text=poss(RDM)))
    print(rd(README))


# ------------------------------------------------------------------------------ COMPONENT 2: THE OLDER CONFLICT
def older_conflict():
    t = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = t.get('rows', t) if isinstance(t, dict) else t
    pick = lambda n: [x for x in rows if isinstance(x, dict) and x['name'] == n]
    r5 = pick('R5_output_HilbertPolya_to_RH')[0]
    r5h = pick('SIDEExplicitFormula.RegisterDepth.register5_output_holds')
    later = max(r5['grade_cells'], key=lambda c: (c['ledger'], c['line']))
    acts = [c['act'] for c in r5['grade_cells']]
    stmt_files = [r5.get('statement_file')]
    b538_later = any(c['act'] == 'b538' for c in r5['grade_cells'])
    branch1 = b538_later
    L = ['b553 -- COMPONENT 2: THE OLDER CONFLICT (READING (2))', '',
         '### R5_output_HilbertPolya_to_RH (%s, %s): grade %s ; its statement %s' % (r5['repo'], r5.get('statement_file'), r5['grade'], (r5.get('statement') or '')[:200])]
    L += ['    %-20s %-26s :%-6s act %-6s %s' % (c['grade'], c['ledger'], c['line'], c['act'], c['quote'][:220]) for c in r5['grade_cells']]
    L += ['### the acts on its cells: %s -- b538 among them: %s' % (acts, b538_later),
          '### all cells name the same terminal (one repository, one statement file): %s' % (len(set(stmt_files)) == 1),
          '### (R163)(2)`s first branch (the later cell b538`s register census against an earlier ENCODES or INTERFACES cell): %s' % ('APPLIES' if branch1 else 'DOES NOT APPLY'),
          '### its second branch (the cells grade different statements under one name): DOES NOT APPLY -- every cell reads the Hilbert-Pólya edge `R5_output_HilbertPolya_to_RH`',
          '### THE CASE: the cells are ENCODES-CONCLUSION (FINDINGS, the correspondence rubric) and ENCODES (FACES_LEDGER, the tier-table word b547 carried) -- one '
          'verdict in two vocabularies; neither branch fits; NO ROW IS WRITTEN; carried to the author.', '',
          '### beside it, the terminal the ruling`s wording names (register5_output_holds):']
    for x in r5h:
        L += ['### %s (%s): grade %s' % (x['name'], x['repo'], x['grade'])] + ['    %-20s %-26s :%-6s act %-6s %s' % (c['grade'], c['ledger'], c['line'], c['act'], c['quote'][:200]) for c in x['grade_cells']]
    out = dict(cells=r5['grade_cells'], acts=acts, branch1=branch1, branch2=False, row_written=False, neighbour=[dict(name=x['name'], grade=x['grade'], cells=x['grade_cells']) for x in r5h])
    put_json('b553_older.json', out)
    put_txt('b553_older.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 3: THE CORRECTION
CF = '*Appended at b553 (2026-09-28) to the detection-geometries entry (`FINDINGS.md`:5529), under `(R163)`(3) -- A CORRECTION, THE NAVIGATOR’S:*'
CO = '*Appended at b553 (2026-09-28) to b546`s record, under `(R163)`(3) -- A CORRECTION, THE NAVIGATOR’S:*'


def corrections():
    guard_absent(FIND, CF)
    guard_absent(OT, CO)
    b546 = lines_with(OT, r'^### b546 ')[0]
    s1 = (CF + ' its sentence at :5533, "The detection width is read per zero (R131)", came from `(R156)`(4)`s wording, the navigator`s, '
          'from recall. (R131)`s run (b522) banks one detection width for the functional as a whole -- a = 34 -- and none per zero (b552, '
          'relay `data/b552_detection_scatter.txt`). H6 is carried unscored until a per-zero detection width has a definition fixed by ruling.')
    s2 = (CO + ' (the record at :%d) `(R156)`(4)`s "the detection width read per zero (R131)" was the navigator`s, from recall; b522 banks one '
          'width for the functional, none per zero. H6 is carried unscored.' % b546)
    o1 = append_to(FIND, NL.join(['', s1, '']))
    o2 = append_to(OT, NL.join(['', s2, '']))
    out = dict(findings=o1, findings_line=line_of(FIND, CF), trails=o2, trails_line=line_of(OT, CO), b546_line=b546)
    put_json('b553_corrections.json', out)
    print(poss(s1)); print(poss(s2)); print(out['findings_line'], out['trails_line'])


# ------------------------------------------------------------------------------ COMPONENT 4: READING SEVEN
G0 = 16.290216
ORB = {'pair': (0.9532604747946607, 16.290215720390393), 'crest': (0.7979971571786801, 29.551761098629115)}


def orbit_term(a, b, gg):
    import b521_tail as B21
    import b514_window as B14
    W = B21.PWindow(a, 'q', 7)
    return float(sum(W.khat(B14.gamma_of(r)).real for r in B14.images(b, gg)))


def period_fine():
    import numpy as np
    lo, hi = math.log(30.0), math.log(60.0)
    n = int(round((hi - lo) / 0.005))
    grid = [lo + 0.005 * i for i in range(n + 1)]
    if grid[-1] < hi - 1e-12:
        grid.append(hi)
    res = {}
    banked = [json.loads(l) for l in rd(os.path.join(D, 'b548_interference.jsonl')).split(NL) if l.strip()]
    for key, (b, gg) in ORB.items():
        v = [orbit_term(math.exp(x), b, gg) for x in grid]
        ch = [grid[i] + (grid[i + 1] - grid[i]) * v[i] / (v[i] - v[i + 1]) for i in range(len(grid) - 1) if v[i] * v[i + 1] < 0]
        sp = [ch[i + 1] - ch[i] for i in range(len(ch) - 1)]
        per = [ch[i + 2] - ch[i] for i in range(len(ch) - 2)]
        x = gg - G0
        delta = b - 0.5
        pred_mean = 4 * math.pi / (7 * abs(x)) if abs(x) > 1e-6 else None
        pred_per = 2 * pred_mean if pred_mean else None
        preds = []
        for i in range(len(sp)):
            mid = 0.5 * (ch[i] + ch[i + 1])
            Wm = 7.0 * mid / 8.0
            th = math.acos(1.0 / math.cosh(2 * delta * Wm))
            rate = 7.0 * abs(x) / 4.0
            preds.append((2 * th / rate, (2 * math.pi - 2 * th) / rate) if pred_mean else None)
        ctrl = []
        for r in banked:
            if r['a'] > 45:
                continue
            bk = [t[2] for t in r['terms'] if t[0] == 'off' and abs(t[1] - gg) < 1e-5]
            fresh = orbit_term(r['a'], b, gg)
            ctrl.append((r['a'], fresh, bk[0] if bk else r['pair'], fresh - (bk[0] if bk else r['pair'])))
        n3045 = sum(1 for c in ch if math.log(30) <= c <= math.log(45))
        mono = all(v[i + 1] < v[i] for i in range(len(v) - 1)) or all(v[i + 1] > v[i] for i in range(len(v) - 1))
        res[key] = dict(b=b, gamma=gg, x=x, delta=delta, changes_ln=ch, changes_a=[math.exp(c) for c in ch], spacings=sp, periods=per,
                        pred_mean=pred_mean, pred_period=pred_per, preds=preds, per_ratios=[p / pred_per for p in per] if pred_per else [],
                        mean=(sum(sp) / len(sp)) if sp else None, n_30_45=n3045, monotone=mono, vmin=min(v), vmax=max(v),
                        sign=('NEG' if max(v) < 0 else ('POS' if min(v) > 0 else 'MIXED')), control=ctrl,
                        values_sample=[(round(math.exp(grid[i]), 3), v[i]) for i in range(0, len(grid), 20)])
    c = res['crest']
    pr = res['pair']
    h71_crest = bool(c['per_ratios']) and all(abs(r - 1) <= 0.03 for r in c['per_ratios'])
    h71_pair = None
    h72 = pr['n_30_45'] >= 2
    ref1 = not h71_crest
    ref2 = pr['monotone']
    s1_alt = len(c['spacings']) >= 3 and all((c['spacings'][i] - c['spacings'][i + 1]) * (c['spacings'][i + 1] - c['spacings'][i + 2]) < 0 for i in range(len(c['spacings']) - 2))
    s1 = s1_alt and c['mean'] is not None and abs(c['mean'] / c['pred_mean'] - 1) <= 0.03
    s2 = len(pr['changes_ln']) == 0
    ctrl_max = max(abs(d) for k in res for (_, _, _, d) in res[k]['control'])
    L = ['b553 -- COMPONENT 4: READING SEVEN -- THE PERIOD AT THE OBJECT`S RESOLUTION (H7 of (R163)(4)); the ladder`s own code, no zero sum, no tail', '',
         '### the grid: ln a from ln 30 to ln 60, step 0.005 (%d points); the orbit term: 4 images, khat of b521`s PWindow at p = 7' % len(grid),
         '### the control (integer widths 30-45, fresh against b548`s banked column): largest |difference| %.3e' % ctrl_max]
    for k in ('crest', 'pair'):
        o = res[k]
        L += ['', '### the %s orbit: σ %.6f, γ %.6f, x = γ − g0 = %.6f, δ = %.6f ; the term`s sign over 30-60: %s (min %.4g, max %.4g) ; monotone %s' % (
            k, o['b'], o['gamma'], o['x'], o['delta'], o['sign'], o['vmin'], o['vmax'], o['monotone']),
              '    sign changes: %d at a = %s' % (len(o['changes_ln']), ', '.join('%.3f' % x for x in o['changes_a'])),
              '    in 30-45: %d' % o['n_30_45']]
        if o['pred_mean']:
            L += ['    derived: mean spacing 4π/(7x) = %.5f ; full period 8π/(7x) = %.5f ; π/γ = %.5f' % (o['pred_mean'], o['pred_period'], math.pi / o['gamma'])]
            L += ['    spacing %.5f  predicted (short %.5f / long %.5f)' % (s, p[0], p[1]) for s, p in zip(o['spacings'], o['preds'])]
            L += ['    full periods: %s ; ratios to 8π/(7x): %s' % (', '.join('%.5f' % p for p in o['periods']), ', '.join('%.4f' % r for r in o['per_ratios'])),
                  '    mean spacing %.5f ; ratio to 4π/(7x) %.4f ; ratio to π/γ %.4f' % (o['mean'], o['mean'] / o['pred_mean'], o['mean'] / (math.pi / o['gamma']))]
        L += ['    control at integer widths: ' + ', '.join('%g: %+.4f (bank %+.4f)' % (a, f, bk) for a, f, bk, _ in o['control'])]
    L += ['', '### H7, clause by clause:',
          '  H7.1 (29.551761)  every full period within 3 %% of 8π/(7x)                        : %s' % ('HOLDS' if h71_crest else 'FAILS'),
          '  H7.1 (16.290216)  the derived spacing does not exist (prediction (b)); sign changes %d        : NOT SCORABLE on spacing' % len(pr['changes_ln']),
          '  H7.2  the 16.290216 term has at least two sign changes in 30-45                  : %s (%d)' % ('HOLDS' if h72 else 'FAILS', pr['n_30_45']),
          '  REFUTER 1  a spacing off the derivation by more than 3 %%                           : %s' % ('fires' if ref1 else 'does not fire'),
          '  REFUTER 2  the 16.29 term monotone on the fine grid                                 : %s (monotone %s)' % ('fires' if ref2 else 'does not fire', pr['monotone']),
          '### H7 IS %s' % ('REFUTED' if (ref1 or ref2 or not h72) else 'NOT REFUTED'),
          '### the banked "monotone fall" of the pair (b552): the fine grid finds the term %s -- a property of the term, not of the bank`s column.' % (
              'without a sign change' if s2 else 'changing sign')]
    out = dict(res=res, h71_crest=h71_crest, h72=h72, ref1=ref1, ref2=ref2, refuted=(ref1 or ref2 or not h72), s1=s1, s1_alt=s1_alt, s2=s2,
               control_max=ctrl_max, grid_n=len(grid))
    put_json('b553_period_fine.json', out)
    put_txt('b553_period_fine.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 5: THE BRIDGE
BRH = ('### `W-ORD-LI-WEIL-BRIDGE` (its leading item at :11265) -- THE BRIDGE RE-ROUTED IN PRICE, appended 2026-09-28, b553, under the '
       'author`s ruling (R163)(5)')


def powerlimit_read():
    t = rd(os.path.join(D, 'b553_powerlimit_check.txt'))
    ex = re.search(r'(?m)^exit (\d+)', t)
    body = t.split(NL, 1)[1] if NL in t else ''
    st = {}
    for n in ('rest_term_small', 'dominant_summable', 'rest_tendsto_zero'):
        m = re.search(r'(?ms)^@?SIDEExplicitFormula\.B321\.%s :.*?(?=^@?SIDEExplicitFormula\.B321\.|^real|\Z)' % n, body)
        st[n] = ' '.join(m.group(0).split()) if m else None
    out = dict(exit=int(ex.group(1)) if ex else None, header=t.split(NL)[0], statements=st)
    put_json('b553_powerlimit.json', out)
    print(json.dumps(out, indent=1, ensure_ascii=False)[:4000])


TRUNC = [
    ('T1', 'the Li test function g_n in the kernel`s variable, as a definition, with its transform identified: paperFT g_n = h_n, '
           'h_n(ρ) = 1 − (1 − 1/ρ)^n (BALPOS :422); its form -- one-sided in log x or not -- fixed from the source first', 'new'),
    ('T2', 'a smoothing of g_n where it is not C² (needed iff T1 finds a jump), with its transform`s convergence', 'new, conditional'),
    ('T3', 'the cutoff family χ_R: C², compactly supported, → 1 pointwise, bounded', 'new; Mathlib bump functions'),
    ('T4', 'g_{n,R} := g_n · χ_R is C² with compact support -- the hypotheses of EF_lit', 'new'),
    ('T5', 'EF_lit at each g_{n,R}: the zero sum equals literatureRHS g_{n,R}', 'Zeta23 EF_lit (hypothesis field), direct'),
    ('T6', 'the zero side`s dominant: the sum grouped by ρ and 1 − ρ̄, since h_n alone decays only like n/ρ; a summable dominant for '
           'the grouped terms uniformly in R', 'new; dominant_summable`s pattern'),
    ('T7', 'the zero side`s limit R → ∞ by Tannery through the grouped dominant', 'rest_tendsto_zero`s pattern'),
    ('T8', 'the prime side`s limit (the Λ(n) sum at g_{n,R} → at g_n) and the archimedean integral`s limit', 'new'),
    ('T9', 'λ_n identified as the limit: the Bombieri-Lagarias arithmetic formula in the kernel`s objects', 'new; BL 1999 (not re-read at source)'),
]
FORWARD = [
    ('F1', 'the repair of GammaBounds.lean:177 at Mathlib 51e6992 (b551: a rewrite pattern not found)', 'measured'),
    ('F2', 'the eleven modules downstream of GammaBounds, unattempted at b551, each re-built and repaired as needed', 'unmeasured'),
    ('F3', 'the lakefile`s require moved to 51e6992 and the branch merged -- a main-moving act on lv', 'ruling'),
    ('F4', 'then T1-T9 in lv: the Li test function is outside every compiled explicit-formula class there too', 'as T1-T9'),
]


def bridge():
    guard_absent(OT, BRH)
    pl = jl('b553_powerlimit.json')
    L = ['', BRH, '',
         '**The three PowerLimit lemmas, fresh (`#check`, relay `data/b553_powerlimit_check.txt`, exit %s):** `rest_term_small`, '
         '`dominant_summable`, `rest_tendsto_zero` -- statements banked in relay `data/b553_powerlimit.json`. They bound and pass to '
         'the limit the zero sum of the power-window route; the truncation route reuses their pattern, not their statements.' % pl.get('exit'), '',
         '**The truncation route, inside SIDE-explicit-formula, in lemmas:**', '']
    L += ['- **%s** %s -- *%s*' % t for t in TRUNC]
    L += ['', '**The toolchain forward, in the same terms:**', '']
    L += ['- **%s** %s -- *%s*' % t for t in FORWARD]
    L += ['', '**The comparison, by inclusion:** the forward carries T1-T9 as F4 and adds F1-F3, so the truncation route prices below it '
          'whatever F2 costs. So, per `(R163)`(5): the residue theorem`s Li-channel premise is to be restated in SIDE-explicit-formula and '
          'cited by lv by tag; `toolchain-trial-b551` stands as data, not as the route. **Its own hazard, stated with it:** T6 -- h_n decays '
          'like n/ρ, so the zero sum converges only with ρ and 1 − ρ̄ grouped; EF_lit`s sum is over the carrier with multiplicities, and '
          'the grouping must be carried through T5-T7. **Priced, not attempted.**', '']
    o = append_to(OT, NL.join(L))
    o['line'] = line_of(OT, BRH)
    o.update(trunc=len(TRUNC), forward=len(FORWARD), n4=True)
    put_json('b553_bridge.json', o)
    print('  OPEN_TRAILS :%s' % o['line'])


# ------------------------------------------------------------------------------ COMPONENT 6: THE CENSUS
LOGS = {'OPEN_TRAILS.md', 'FINDINGS.md', 'VERIFICATION_LOOM.md', 'internal/CONVERGENCE.md'}
RETIRED = ('archive/', 'heritage/', 'outputs/')
V01 = ['PATHS_TO_THE_CRITICAL_LINE', 'THE_UNCONDITIONAL_SURROUND', 'SIMPLICITY_OF_RIEMANN_ZEROS', 'GRH_CASCADE', 'R_CURVE_CRITERION',
       'INDEX_ARITY_AT_THE_CRITICAL_LINE', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'INVARIANCE_BARRIERS',
       'SILENCE_STAGES_DEALIGNMENT', 'TECHNE_TOOLKIT', 'E_DIFFICULTY_THEOREM', 'REPARAMETERIZATION_BARRIERS_v0_1', 'ENUMERA',
       'EXHAUSTIVENESS_LICENSE', 'THE_RESIDUE_OF_RH']
TIERED = {'THE_UNCONDITIONAL_SURROUND': 'b539', 'PATHS_TO_THE_CRITICAL_LINE': 'b540', 'THE_RESIDUE_OF_RH': 'b549'}
TIERED_OTHER = ['day1/A_Place_to_Stand (CONCORDANCE-CARRIED)', 'BALANCE_AND_POSITIVITY', 'FACES_OF_H2_AT_FINITE_INSTANCE', 'FACES_LEDGER', 'THE_IDENTITY_CHAIN']


def is_log(f):
    return f in LOGS or bool(re.search(r'(?i)(^|/)(FINDINGS|VERIFICATION_LOOM|OPEN_TRAILS)-archive', f))


def detect(rev):
    """### §0 as operationalised: (i) an Abstract heading or ORCID anywhere; (ii) a heading matching correspondence; 6 KiB; day1/ is
    ### CONCORDANCE-CARRIED; logs are SUPPORT; retired trees are SUPPORT; (iii) the stem in REGISTRY, SPIRAL_MAP, README or clusters/."""
    files = [f for f in subprocess.run(['git', '-C', PP, 'ls-tree', '-r', '--name-only', rev], capture_output=True).stdout.decode('utf-8').split(NL) if f.endswith('.md')]
    show = lambda f: subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (rev, f)], capture_output=True).stdout
    trunk = ''.join(show(f).decode('utf-8', 'replace') for f in files if f in ('REGISTRY.md', 'SPIRAL_MAP.md', 'README.md') or f.startswith('clusters/'))
    rows = []
    for f in files:
        b = show(f)
        t = b.decode('utf-8', 'replace')
        h = [l for l in t.split(NL) if l.lstrip().startswith('#')]
        i = any(re.search(r'(?i)abstract', x) for x in h) or bool(re.search(r'(?i)orcid', t))
        ii = any(re.search(r'(?i)correspondence', x) for x in h)
        stem = os.path.basename(f)[:-3]
        iii = stem in trunk
        if f.startswith('day1/'):
            cls = 'CONCORDANCE-CARRIED'
        elif len(b) < 6144:
            cls = 'BELOW FLOOR'
        elif is_log(f) or f.startswith(RETIRED):
            cls = 'SUPPORT'
        elif i and ii and iii:
            cls = 'KEYSTONE'
        elif i and iii:
            cls = 'KEYSTONE-CANDIDATE'
        else:
            cls = 'SUPPORT'
        raw = (not f.startswith('day1/')) and len(b) >= 6144 and i and ii
        rows.append(dict(file=f, stem=stem, size=len(b), i=i, ii=ii, iii=iii, cls=cls, raw=raw))
    return rows


def counts(rows):
    return {k: sum(1 for r in rows if r['cls'] == k) for k in ('KEYSTONE', 'CONCORDANCE-CARRIED', 'KEYSTONE-CANDIDATE', 'SUPPORT')}


def census():
    old, new = detect('0d4a6fe~1'), detect('HEAD')
    raw_old = sorted(r['file'] for r in old if r['raw'])
    cand_old = sum(1 for r in old if not r['file'].startswith('day1/') and r['size'] >= 6144 and r['i'] and not r['ii'])
    sup_old = sum(1 for r in old if not r['file'].startswith('day1/') and r['size'] >= 6144 and not (r['i'] and r['ii'])) - cand_old
    ko = sorted(r['stem'] for r in old if r['cls'] == 'KEYSTONE')
    kn = [r for r in new if r['cls'] == 'KEYSTONE']
    entrants = sorted(r['stem'] for r in kn if r['stem'] not in V01)
    leavers = sorted(set(V01) - set(r['stem'] for r in kn))
    iii_old_fail = sorted(set(V01) - set(ko))
    raw_new = sorted(r['file'] for r in new if r['raw'])
    nav = ['BALANCE_AND_POSITIVITY', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY', 'THE_GLOBAL_SECTION', 'THE_METHOD_CANON']
    L = ['b553 -- COMPONENT 6 (a): THE CENSUS`S §0 TEST, REBUILT AND RE-RUN (READING (7))', '',
         '### THE CONTROL at 0d4a6fe~1 (the tree v0.1 counted): raw KEYSTONE %d (v0.1: 20) ; CONCORDANCE-CARRIED %d (v0.1: 9) ; '
         'KEYSTONE-CANDIDATE by (i) without (ii) %d (v0.1: 62) ; SUPPORT >= 6 KiB %d (v0.1: 101)' % (
             len(raw_old), counts(old)['CONCORDANCE-CARRIED'], cand_old, sup_old),
         '### the raw twenty at 0d4a6fe~1: %s' % ', '.join(os.path.basename(f)[:-3] for f in raw_old),
         '### after §0`s removals and (iii) at 0d4a6fe~1: KEYSTONE %d -- equal to v0.1`s sixteen: %s ; of the sixteen, failing (iii) as read here at that tree: %s' % (len(ko), ko == sorted(V01), iii_old_fail or 'NONE'),
         '### entrants and leavers are therefore counted against v0.1`s PUBLISHED sixteen (§2), not against the rebuilt detector`s output at that tree.',
         '### CONCORDANCE-CARRIED at HEAD: %s' % [r['file'] for r in new if r['cls'] == 'CONCORDANCE-CARRIED'], '',
         '### AT HEAD (%s): %s ; v0.1: 16 / 9 / 62 / 101' % (g(PP, 'rev-parse', '--short', 'HEAD').strip(), counts(new)),
         '### the raw detector at HEAD: %d -- %s' % (len(raw_new), ', '.join(raw_new)), '',
         '  keystone                                         (i)   (ii)  (iii)  Correspondence heading  cascade']
    order = {s: i for i, s in enumerate(V01)}
    for r in sorted(kn, key=lambda r: order.get(r['stem'], 99)):
        L.append('  %-48s %-5s %-5s %-6s %-23s %s' % (r['stem'], r['i'], r['ii'], r['iii'], 'present' if r['ii'] else 'ABSENT',
                                                     ('TIERED (%s)' % TIERED[r['stem']]) if r['stem'] in TIERED else 'untiered'))
    L += ['', '### entrants since 2026-08-12: %s ; leavers: %s' % (entrants or 'NONE', leavers or 'NONE'),
          '### the navigator`s four, as the test reads them:']
    for n in nav:
        rr = [r for r in new if r['stem'] == n]
        L.append('    %-52s %s' % (n, ('%s ((i) %s, (ii) %s, (iii) %s)' % (rr[0]['cls'], rr[0]['i'], rr[0]['ii'], rr[0]['iii'])) if rr else 'NO SUCH FILE'))
    L += ['### the new raw passes at HEAD and their class: %s' % ', '.join('%s -> %s' % (r['file'], r['cls']) for r in new if r['raw'] and r['stem'] not in V01)]
    put_json('b553_census.json', dict(old_counts=dict(raw=len(raw_old), cc=counts(old)['CONCORDANCE-CARRIED'], cand=cand_old, sup=sup_old),
                                      old_keystones=ko, iii_old_fail=iii_old_fail, new_counts=counts(new), keystones=[r['stem'] for r in kn], files={r['stem']: r['file'] for r in kn},
                                      entrants=entrants, leavers=leavers, raw_new=raw_new, nav={n: ([r['cls'] for r in new if r['stem'] == n] or ['NO SUCH FILE'])[0] for n in nav},
                                      tiered=TIERED))
    put_txt('b553_census.txt', L)
    print(NL.join(L))


NAMED5 = ['2152047', 'c66f3c5', '27a3ae7', '3b2e8d6', 'bd2ae1a']


def all_repos():
    import glob
    reps = sorted(x for x in glob.glob(os.path.join(DD, 'SIDE-*')) if os.path.isdir(os.path.join(x, '.git')))
    return reps + [os.path.join(DD, 'MY-DOwnloads', 'TECHNE-Core'), ROOT, PP]


def resolve(sha, reps):
    found = []
    for r in reps:
        full = subprocess.run(['git', '-C', r, 'rev-parse', '--verify', '-q', sha + '^{commit}'], capture_output=True, text=True).stdout.strip()
        if full:
            anc = subprocess.run(['git', '-C', r, 'merge-base', '--is-ancestor', full, 'HEAD'], capture_output=True).returncode == 0
            reach = '' if anc else subprocess.run(['git', '-C', r, 'branch', '-a', '--contains', full], capture_output=True, text=True).stdout.split() + \
                subprocess.run(['git', '-C', r, 'tag', '--contains', full], capture_output=True, text=True).stdout.split()
            found.append(dict(repo=os.path.basename(r), full=full, ancestor=anc, reached_by=reach))
    return found


def ancestry():
    cz = jl('b553_census.json')
    reps = all_repos()
    cited = {}
    for stem in cz['keystones']:
        t = rd(os.path.join(PP, cz['files'][stem]))
        for l in t.split(NL):
            for m in re.finditer(r'`([0-9a-f]{7,40})`', l):
                pre = re.findall(r'(SIDE-[A-Za-z0-9-]+|relay|PLACE-papers)', l[:m.start()])
                cited.setdefault(m.group(1), dict(docs=set(), attrib=set()))
                cited[m.group(1)]['docs'].add(stem)
                cited[m.group(1)]['attrib'].add(pre[-1] if pre else '?')
    res = {}
    for sha in sorted(set(cited) | set(NAMED5)):
        f = resolve(sha, reps)
        st = 'ABSENT' if not f else ('ANCESTOR' if any(x['ancestor'] for x in f) else 'NOT-ANCESTOR')
        res[sha] = dict(status=st, found=f, docs=sorted(cited.get(sha, {}).get('docs', [])), attrib=sorted(cited.get(sha, {}).get('attrib', [])), cited=sha in cited)
    per_doc = {s: sum(1 for v in res.values() if s in v['docs']) for s in cz['keystones']}
    fails = {k: v for k, v in res.items() if v['cited'] and v['status'] != 'ANCESTOR'}
    L = ['b553 -- COMPONENT 6 (b): PIN ANCESTRY OVER EVERY PIN THE LIVE KEYSTONES CITE (READING (8))', '',
         '### repositories tested: %d ; distinct cited pins: %d ; ANCESTOR %d ; NOT-ANCESTOR %d ; ABSENT %d' % (
             len(reps), sum(1 for v in res.values() if v['cited']), sum(1 for v in res.values() if v['cited'] and v['status'] == 'ANCESTOR'),
             sum(1 for v in res.values() if v['cited'] and v['status'] == 'NOT-ANCESTOR'), sum(1 for v in res.values() if v['cited'] and v['status'] == 'ABSENT')),
         '### THE FAILURES (cited, not an ancestor of any HEAD that holds them):']
    L += ['    %-12s %-13s found in %s ; cited by %s ; line attribution %s' % (k, v['status'], [(x['repo'], x['reached_by'][:4]) for x in v['found']] or 'NOWHERE',
                                                                           v['docs'], v['attrib']) for k, v in fails.items()] or ['    NONE']
    L += ['', '### THE FIVE v0.1 NAMED, RE-TESTED (cited now or not):']
    L += ['    %-8s %-13s cited now %-5s found in %s' % (k, res[k]['status'], res[k]['cited'], [x['repo'] for x in res[k]['found']] or 'NOWHERE') for k in NAMED5]
    L += ['', '### pins cited per keystone (the census`s order key): %s' % per_doc]
    put_json('b553_ancestry.json', dict(results={k: dict(v, found=v['found']) for k, v in res.items()}, per_doc=per_doc, fails=sorted(fails),
                                        named5={k: res[k]['status'] for k in NAMED5}))
    put_txt('b553_ancestry.txt', L)
    print(NL.join(L))


HAND = {
    'bd2ae1a': ('RESOLVED IN PLACE-papers: commit bd2ae1a60a74 (2026-07-25, "E-CHARACTERIZATION sitting (read+derive, HELD)"), an ancestor of its '
                'HEAD. PATHS_TO_THE_CRITICAL_LINE.md:420 attributes it to SIDE-lv-conservation, where it resolves nowhere; '
                'THE_H2_PROGRAMME_CHARTER.md:116 names "the `bd2ae1a` `E`-CHARACTERIZATION sitting" -- the PLACE-papers commit. v0.1 tested '
                '"all 43 local repositories" at the root of D:; PLACE-papers lives under MY-DOwnloads and was not among them. The referent is read, '
                'not ruled.'),
    '21433177': 'NOT A PIN: the digits of a Zenodo concept record (10.5281/zenodo.21433177, PATHS :83); an all-digit token the hex pattern admits.',
    '5e932f97': 'A MATHLIB PIN: 5e932f97dd25 resolves in every Mathlib clone at that rev (e.g. SIDE-lv-conservation/.lake/packages/mathlib, '
                '2026-04-17, "chore: bump toolchain to v4.29.1"); the rule tested SIDE-*, relay and PLACE-papers only.',
    '6e8638a': 'ABSENT everywhere tested, three Mathlib clones included (SIDE-kernel`s, D:/mathlib4, SIDE-explicit-formula`s); cited by TECHNE_TOOLKIT beside SIDE-kernel and TECHNE.Core (whose two local '
               'clones diverge, :416). Stated, not assessed.',
    '27a3ae7': 'NOT-ANCESTOR as at v0.1: reachable from SIDE-kernel`s branch derivative-engine only (act 3b`s derivative-engine adjudication).',
}


def ancestry_read():
    an = jl('b553_ancestry.json')
    L = ['b553 -- COMPONENT 6 (b), THE RESIDUE HAND-READ: each failure and each named pin, read beside the mechanical status', '']
    for k in sorted(set(an['fails']) | {'bd2ae1a'}):
        L.append('  %-10s mechanical %-13s ; %s' % (k, an['results'][k]['status'], HAND.get(k, 'no hand-read')))
    put_txt('b553_ancestry_read.txt', L)
    put_json('b553_ancestry_read.json', dict(notes=HAND, genuine=[k for k in an['fails'] if k in ('6e8638a', '27a3ae7')],
                                             artefacts=[k for k in an['fails'] if k in ('21433177', '5e932f97')], bd2ae1a='RESOLVED IN PLACE-papers'))
    print(NL.join(L))


def anomaly():
    reg = rd(os.path.join(PP, 'REGISTRY.md')).split(NL)
    regrows = [(i + 1, l[:240]) for i, l in enumerate(reg) if 'SIDE-kernel' in l and re.search(r'v1\.\d', l)]
    tags = g(KER, 'tag', '--sort=-creatordate').split()
    out = dict(head=g(KER, 'rev-parse', 'HEAD').strip(), head_date=g(KER, 'log', '-1', '--format=%ci').strip(), latest_tag=tags[0] if tags else None,
               latest_tag_commit=g(KER, 'rev-parse', '--short', tags[0] + '^{commit}').strip() if tags else None,
               head_is_latest_tag=bool(tags) and g(KER, 'rev-parse', tags[0] + '^{commit}').strip() == g(KER, 'rev-parse', 'HEAD').strip(),
               v15=g(KER, 'rev-parse', '--short', 'v1.5^{commit}').strip(), registry_rows=regrows,
               remote_main=(g(KER, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0])
    L = ['b553 -- COMPONENT 6 (c): ANOMALY 1 RE-READ (READING (9))', '',
         '### SIDE-kernel HEAD %s (%s) ; latest tag %s = %s ; HEAD is the latest tag: %s ; v1.5 = %s ; remote main %s' % (
             out['head'][:12], out['head_date'], out['latest_tag'], out['latest_tag_commit'], out['head_is_latest_tag'], out['v15'], out['remote_main'][:12]),
         '### REGISTRY.md rows naming SIDE-kernel at a version:'] + ['    :%d %s' % x for x in regrows] + [
         '### PRESENT STATUS: HEAD %s the latest tag; the corpus`s deposit pin stays v1.5 (SPIRAL_MAP.md:49) while the working head has moved '
         'past it -- the manifest-law question v0.1 named is still not decided by any row read here.' % ('IS' if out['head_is_latest_tag'] else 'is NOT')]
    put_json('b553_anomaly.json', out)
    put_txt('b553_anomaly.txt', L)
    print(NL.join(L))


S9H = '### §9 ANNOTATED -- THE REQUIRED LINE SUPERSEDED (appended 2026-09-28, b553, under the author`s ruling `(R163)`(6))'
V02H = '# THE KEYSTONE CENSUS v0.2 -- RE-RUN LIVE, 2026-09-28 (b553, under the author`s ruling `(R163)`(6); the v0.1 body above is unchanged)'


def census_v02():
    guard_absent(CENSUS, V02H)
    cz, an, am = jl('b553_census.json'), jl('b553_ancestry.json'), jl('b553_anomaly.json')
    per = an['per_doc']
    order = sorted(cz['keystones'], key=lambda s: (-per.get(s, 0), V01.index(s) if s in V01 else 99))
    remaining = [s for s in order if s not in TIERED]
    s9 = ['', S9H, '',
          '§9`s required line ("`THE_RESIDUE_OF_RH`\'s compiled terminals live on the HELD, UNMERGED branch `word-pairing-interface`") is '
          'superseded: SIDE-lv-conservation`s `main` was fast-forwarded to `2f71068` over that branch`s line (b454), and `main` is tagged '
          '`v0.11.0` at `2f71068` (b550, read back from the remote). The terminals are on `main`; the line above is kept as written.', '']
    v = ['', V02H, '',
         '*Tier C, as v0.1. Produced by relay `tools/b553_record.py` (`census`, `ancestry`, `anomaly`); banks relay `data/b553_census.txt`, '
         '`data/b553_ancestry.txt`, `data/b553_anomaly.txt`. §0`s test rebuilt as operationalised, with (iii) read as the document`s stem '
         'appearing in REGISTRY, SPIRAL_MAP, README or a clusters/ file, and retired trees (archive/, heritage/, outputs/) counted SUPPORT.*', '',
         '**The control.** At the tree v0.1 counted, the rebuilt detector returns v0.1`s raw 20 and its 9 CONCORDANCE-CARRIED exactly; after '
         '§0`s removals and (iii) as read here it keeps %d of v0.1`s sixteen (%s fails (iii) at that tree and passes at HEAD); it returns %d '
         'KEYSTONE-CANDIDATE and %d SUPPORT against v0.1`s 62 and 101 -- differences this re-run prints and does not close. Entrants are '
         'counted against v0.1`s published sixteen.' % (16 - len(cz['iii_old_fail']), ', '.join(cz['iii_old_fail']) or 'none', cz['old_counts']['cand'], cz['old_counts']['sup']), '',
         '**The classes at HEAD** (v0.1 beside): KEYSTONE %d (16) · CONCORDANCE-CARRIED %d (9) · KEYSTONE-CANDIDATE %d (62) · SUPPORT %d (101).' % (
             cz['new_counts']['KEYSTONE'], cz['new_counts']['CONCORDANCE-CARRIED'], cz['new_counts']['KEYSTONE-CANDIDATE'], cz['new_counts']['SUPPORT']), '',
         '**Entrants since 2026-08-12:** %s. The navigator`s four read: %s.' % (', '.join(cz['entrants']) or 'none',
                                                                               '; '.join('%s %s' % (k, v_) for k, v_ in cz['nav'].items())), '',
         '| keystone | cited pins | Correspondence heading | cascade |', '|:--|--:|:--|:--|']
    for s in order:
        v.append('| `%s` | %d | present | %s |' % (s, per.get(s, 0), ('TIERED (%s)' % TIERED[s]) if s in TIERED else 'untiered'))
    v += ['', '*The cascade has also tiered, outside the KEYSTONE class: %s.*' % ', '.join(TIERED_OTHER), '',
          '**Pin ancestry.** Mechanical failures: %s. Hand-read (relay `data/b553_ancestry_read.txt`): `21433177` is a Zenodo record`s digits, not a pin; '
          '`5e932f97` is a Mathlib pin that resolves in every Mathlib clone at that rev; `6e8638a` resolves nowhere tested; `27a3ae7` is reachable '
          'from SIDE-kernel`s `derivative-engine` only. **`bd2ae1a` resolves: a PLACE-papers commit of 2026-07-25 (the E-CHARACTERIZATION '
          'sitting), which THE_H2_PROGRAMME_CHARTER.md:116 names; v0.1 did not test PLACE-papers.**' % ('; '.join('`%s` %s' % (k, an['results'][k]['status']) for k in an['fails']) or 'none'),
          'The five v0.1 named, re-tested: %s.' % '; '.join('`%s` %s' % kv for kv in an['named5'].items()), '',
          '**Anomaly 1.** SIDE-kernel HEAD `%s`, latest tag `%s` (`%s`); HEAD %s the latest tag; the corpus`s deposit pin stays `v1.5` = `%s`.' % (
              am['head'][:7], am['latest_tag'], am['latest_tag_commit'], 'is' if am['head_is_latest_tag'] else 'is not', am['v15']), '',
          '**The cascade`s remaining roster, in the census`s order:** %s. **Next:** `%s`.' % (', '.join('`%s`' % s for s in remaining), remaining[0]), '',
          '*No byte above this section changes. Nothing deposits.*', '']
    o1 = append_to(CENSUS, NL.join(s9))
    o2 = append_to(CENSUS, NL.join(v))
    out = dict(s9=o1, s9_line=line_of(CENSUS, S9H), v02=o2, v02_line=line_of(CENSUS, V02H), order=order, remaining=remaining, next=remaining[0])
    put_json('b553_census_v02.json', out)
    print('  CENSUS §9 :%s ; v0.2 :%s ; next %s' % (out['s9_line'], out['v02_line'], out['next']))
    print('  roster: %s' % remaining)


# ------------------------------------------------------------------------------ THE ENTRY, SCORES, DESK, COMPONENTS, TRAIL
FH = ('## The cascade, act seven: THE_KEYSTONE_CENSUS re-run live, the roster set from the census, the pins re-tested; the '
      'supersession rule; the period read at the object`s resolution; the bridge re-routed in price')
HEADING = ('### b553 — the cascade, act seven under (R163): THE_KEYSTONE_CENSUS re-run live; the supersession rule; the older conflict; '
           'the per-zero correction; H7 from the printed transform; the bridge re-routed in price')


def findings():
    guard_absent(FIND, FH)
    su, ol, pf, br, cz, an, am, cv = (jl('b553_supersede.json'), jl('b553_older.json'), jl('b553_period_fine.json'), jl('b553_bridge.json'),
                                      jl('b553_census.json'), jl('b553_ancestry.json'), jl('b553_anomaly.json'), jl('b553_census_v02.json'))
    c, pr = pf['res']['crest'], pf['res']['pair']
    L = ['', FH, '',
         '*Filed at b553 on the author`s ruling `(R163)`. The cascade`s act seven. Banks: relay `data/b553_supersede.txt`, `data/b553_older.txt`, '
         '`data/b553_period_fine.txt`, `data/b553_census.txt`, `data/b553_ancestry.txt`, `data/b553_anomaly.txt`.*', '',
         '**The census, re-run live.** §0 rebuilt as operationalised; at the tree v0.1 counted it returns v0.1`s raw 20 and Day-1`s 9 exactly, and '
         '15 of the sixteen under (iii) as read here (EXHAUSTIVENESS_LICENSE was not yet cited by the trunk). At HEAD: '
         'KEYSTONE %d · CONCORDANCE-CARRIED %d · KEYSTONE-CANDIDATE %d · SUPPORT %d (v0.1: 16 · 9 · 62 · 101). Entrants since 2026-08-12: %s. '
         'The navigator`s four read %s. THE_KEYSTONE_CENSUS stays Tier C; its v0.2 section is at :%s, the §9 annotation at :%s.' % (
             cz['new_counts']['KEYSTONE'], cz['new_counts']['CONCORDANCE-CARRIED'], cz['new_counts']['KEYSTONE-CANDIDATE'], cz['new_counts']['SUPPORT'],
             ', '.join(cz['entrants']) or 'none', '; '.join('%s %s' % kv for kv in cz['nav'].items()), cv['v02_line'], cv['s9_line']), '',
         '**The pins, re-tested.** Mechanical failures among the pins the live keystones cite: %s -- hand-read: two artefacts (a Zenodo record`s '
         'digits; a Mathlib pin), `6e8638a` absent everywhere tested, `27a3ae7` off HEAD. **`bd2ae1a`, v0.1`s unreproducible pin, resolves: a PLACE-papers '
         'commit of 2026-07-25 that THE_H2_PROGRAMME_CHARTER.md:116 names; v0.1 never tested PLACE-papers.** The five v0.1 named: %s. Anomaly 1: SIDE-kernel HEAD `%s`, '
         'latest tag `%s`; HEAD %s the latest tag; the deposit pin stays v1.5.' % (
             ', '.join('`%s` %s' % (k, an['results'][k]['status']) for k in an['fails']) or 'none',
             '; '.join('`%s` %s' % kv for kv in an['named5'].items()), am['head'][:7], am['latest_tag'], 'is' if am['head_is_latest_tag'] else 'is not'), '',
         '**The roster set from the census.** Remaining, in the census`s order: %s. **Next keystone:** `%s`.' % (', '.join('`%s`' % s for s in cv['remaining']), cv['next']), '',
         '**The supersession rule.** `tools/terminal_table.py` gains `supersede`; with row 393 (`SUPERSEDES row 391: SHELL`) boolGrp reads %s; '
         'terminals whose grade changed: %s; CONFLICT %d before, %d after.' % (
             su['boolgrp_after']['grade'], ', '.join('%s %s' % (k.split('|')[1], ' -> '.join(v)) for k, v in su['changed'].items()) or 'none',
             len(su['conflicts_before']), len(su['conflicts_after'])), '',
         '**The older conflict.** R5_output_HilbertPolya_to_RH`s cells are ENCODES-CONCLUSION and ENCODES -- one verdict in two vocabularies, no '
         'b538 cell among them; neither branch of `(R163)`(2) applies and no row is written (carried to the author).', '',
         '**The period at the object`s resolution (H7).** From the ladder`s transform, printed before evaluation: an off-line orbit with γ ≠ g0 '
         'carries a non-oscillating part and oscillates at 7x/4 in ln a (x = γ − g0), crossing zero twice per period at alternating short '
         'and long spacings, mean 4π/(7x) -- not π/γ; the pair orbit (γ = g0) has no oscillating dominant part and is predicted not to change '
         'sign. On the fine grid (step 0.005, 30-60; the control against b548 to %.1e): the 29.55 orbit`s full periods against 8π/(7x) %s, its '
         'mean spacing %.4f against 4π/(7x) = %.4f; the 16.29 term changes sign %d times in 30-60 (%d in 30-45), monotone %s. **H7 %s.**' % (
             pf['control_max'], ', '.join('%.3f' % r for r in c['per_ratios']), c['mean'], c['pred_mean'], len(pr['changes_ln']), pr['n_30_45'],
             pr['monotone'], 'REFUTED' if pf['refuted'] else 'NOT REFUTED'), '',
         '**The bridge re-routed in price.** The truncation route inside SIDE-explicit-formula (%d items) against the toolchain forward (%d items, '
         'one of them the whole truncation route): the truncation route prices below by inclusion (OPEN_TRAILS.md:%s). Not attempted.' % (
             br['trunc'], br['forward'], br['line']), '',
         '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited; nothing here is a statement about RH or about ζ’s zeros.*', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_of(FIND, FH)
    put_json('b553_findings.json', o)
    print('  FINDINGS :%s' % o['line'])


PRIOR_PP = 'c0af276'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', 'phase2/method/THE_KEYSTONE_CENSUS.md'}
MEMDIR = P.MEMDIR
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '64faaa7'}


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def scores():
    su, ol, pf, br, cz, an, cv = (jl('b553_supersede.json'), jl('b553_older.json'), jl('b553_period_fine.json'), jl('b553_bridge.json'),
                                  jl('b553_census.json'), jl('b553_ancestry.json'), jl('b553_census_v02.json'))
    committed = g(PP, 'log', '-1', '--pretty=%s').startswith('b553 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in g(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in g(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b553_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b553_')) if tk else None
    m = mains()
    lean = [(k, f) for k, v in m.items() for f in v if f.endswith('.lean')]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(TRIAL, 'rev-parse', 'HEAD').strip(), status=g(TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    c, pr = (pf.get('res') or {}).get('crest', {}), (pf.get('res') or {}).get('pair', {})
    n3 = False  # ### its first clause (the derived spacing IS π/γ) fails by the derivation printed on the face; see the desk
    return dict(
        n1=bool(su) and su['boolgrp_after']['grade'] == 'SHELL' and list(su['changed']) == ['SIDE-global-section|AggregationCircularityShadow.boolGrp'],
        n2=bool(ol) and ol['branch1'] and ol['row_written'],
        n3=n3 and bool(pf.get('h71_crest')) and bool(pf.get('h72')),
        n4=bool(br.get('n4')),
        n5=bool(cz) and cz['new_counts']['KEYSTONE'] > 16 and len(cz['entrants']) >= 4,
        n6=bool(an) and an['named5'].get('bd2ae1a') == 'ABSENT',
        n7=not lean and not zen and tok == 0 and dep and all(pref.values()) and set(written) <= WRITE_OK
        and trial['head'].startswith('f22ff35') and trial['status'] == '' and all(not m[k] for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula'))
        and set(m['SIDE-global-section']) <= {'CORRESPONDENCE.md'},
        mains=m, prefixes=pref, written=written, zen=zen, token=tok, deposit_clean=dep, trial=trial,
        n3_clauses=dict(spacing_is_pi_over_gamma=False, no_non_oscillating=False, fine_confirms_both=bool(pf.get('h71_crest')) and False,
                        pair_two_changes=bool(pf.get('h72'))),
        s1=bool(pf.get('s1')), s2=bool(pf.get('s2')), s3=bool(cv) and cv.get('next') == 'SIMPLICITY_OF_RIEMANN_ZEROS')


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'), ('s1', 's2', 's3')
    su, ol, pf, br, cz, an, cv = (jl('b553_supersede.json'), jl('b553_older.json'), jl('b553_period_fine.json'), jl('b553_bridge.json'),
                                  jl('b553_census.json'), jl('b553_ancestry.json'), jl('b553_census_v02.json'))
    c, pr = pf['res']['crest'], pf['res']['pair']
    L = ['=' * 104, 'b553 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SEVEN.', '-' * 104,
         '  **(N1)** ### **%s.** -- boolGrp after: %s ; terminals whose grade changed: %s ; CONFLICT %d -> %d.' % (
             w(sc['n1']), su['boolgrp_after']['grade'], list(su['changed']), len(su['conflicts_before']), len(su['conflicts_after'])),
         '  **(N2)** ### **%s.** -- the cells` acts %s ; b538 among them %s ; one statement under one name ; no superseding row written.' % (w(sc['n2']), ol['acts'], ol['branch1']),
         '  **(N3)** ### **%s.** -- clauses: the derived spacing is π/γ: FAILS (derived 4π/(7x) = %.4f for 29.55, π/γ = %.4f) ; no non-oscillating part: '
         'FAILS (the ½ of sin²) ; the fine grid confirms both to 3 %%: FAILS (29.55`s periods %s ; 16.29 has no derived spacing) ; the 16.29 term with '
         'two sign changes in 30-45: %s (%d).' % (w(sc['n3']), c['pred_mean'], math.pi / c['gamma'], ['%.3f' % r for r in c['per_ratios']],
                                                  'HOLDS' if pf['h72'] else 'FAILS', pr['n_30_45']),
         '  **(N4)** ### **%s.** -- by inclusion: the forward (%d items) contains the truncation route (%d items).' % (w(sc['n4']), br['forward'], br['trunc']),
         '  **(N5)** ### **%s.** -- live KEYSTONE %d ; entrants %s.' % (w(sc['n5']), cz['new_counts']['KEYSTONE'], cz['entrants'] or 'NONE'),
         '  **(N6)** ### **%s.** -- the five: %s.' % (w(sc['n6']), an['named5']),
         '  **(N7)** ### **%s.** -- mains changed %s ; `.lean` none ; token %s ; deposit clean %s ; prefixes %s ; trial %s.' % (
             w(sc['n7']), {k: v for k, v in sc['mains'].items() if v} or 'NONE', sc['token'], sc['deposit_clean'], sc['prefixes'], sc['trial']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- 29.55`s spacings alternate %s ; mean %.5f against 4π/(7x) %.5f (ratio %.4f).' % (w(sc['s1']), pf['s1_alt'], c['mean'], c['pred_mean'], c['mean'] / c['pred_mean']),
         '  **(S2)** ### **%s.** -- 16.29`s sign changes on the fine grid over 30-60: %d ; its sign %s.' % (w(sc['s2']), len(pr['changes_ln']), pr['sign']),
         '  **(S3)** ### **%s.** -- the next untiered keystone: %s.' % (w(sc['s3']), cv['next']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b553_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b553_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b553_desk_notes.txt', L)
    put_json('b553_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b553 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b553_supersede.txt', 'b553_older.txt', 'b553_period_fine.txt', 'b553_powerlimit_check.txt', 'b553_census.txt', 'b553_ancestry.txt', 'b553_anomaly.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b553_readme.json', 'b553_corrections.json', 'b553_bridge.json', 'b553_census_v02.json', 'b553_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)[:3000]))
    L += ['### THE BRANCHES : see data/b553_branches.txt', '=' * 132]
    put_txt('b553_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc, su, pf, cv, fj, co, br = (scores(), jl('b553_supersede.json'), jl('b553_period_fine.json'), jl('b553_census_v02.json'), jl('b553_findings.json'),
                                  jl('b553_corrections.json'), jl('b553_bridge.json'))
    body = ['', HEADING, '',
            '**(R163) ratified.** (1) The supersession rule in `tools/terminal_table.py`, row 393 in its form. (2) The older conflict read. (3) '
            '`(R156)`(4)`s "per zero" corrected as the navigator`s. (4) H4 restated as H7 from the printed transform. (5) The bridge re-routed in '
            'price. (6) THE_KEYSTONE_CENSUS re-run live as act seven. (7) The next keystone named from the census.', '',
            '**Entered:** FINDINGS.md:%s (the correction) and :%s (the entry); OPEN_TRAILS.md:%s (the correction) and :%s (the bridge price); '
            'THE_KEYSTONE_CENSUS.md:%s (§9 annotated) and :%s (v0.2); SIDE-global-section CORRESPONDENCE.md row 393; relay '
            '`tools/terminal_table.py` (`supersede`) and `tools/corr_row.README.md`.' % (
                co['findings_line'], fj['line'], co['trails_line'], br['line'], cv['s9_line'], cv['v02_line']), '',
            '**H7 %s.** boolGrp reads %s. **Next keystone:** `%s`.' % ('REFUTED' if pf['refuted'] else 'NOT REFUTED', su['boolgrp_after']['grade'], cv['next']), '',
            '**CP-1:** open; the cascade continues with `%s`.' % cv['next'], '',
            '**Next:** `%s`.' % cv['next'], '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
            '**No kernel lane opened at this act; the numerical lane carried the closed-form evaluations alone.** Nothing deposits; nothing at '
            'Zenodo written; no `.lean` file edited; no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` '
            'where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or about ζ’s zeros.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b553_trail_notes.json', out)


if __name__ == '__main__':
    fn = {k: globals()[k] for k in ('reads', 'row393', 'readme', 'older_conflict', 'corrections', 'period_fine', 'powerlimit_read', 'bridge',
                                    'census', 'ancestry', 'ancestry_read', 'anomaly', 'census_v02', 'findings', 'components', 'desk', 'trail')}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
