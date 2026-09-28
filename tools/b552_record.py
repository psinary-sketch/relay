# -*- coding: utf-8 -*-
"""b552_record.py -- b551 SETTLED; FOUR READINGS FROM THE BANKS: THE RECORD, UNDER (R162).
### `python tools/b552_record.py reads | housekeeping_read | row392 | readme | stormer | consolidation | period | regimes | li_class |
### scatter | n6_line | findings | components | desk | trail`
### Arithmetic on banked numbers only; no new computation. The commits, pushes and branch commands are the seat`s. This file deletes
### nothing.
"""
import io, json, math, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402  (its append guard, its line finder, its possessive rule; nothing of it runs at import)
DD = 'D:' + os.sep
PP = P.PP
GS, LV, EF = P.GS, P.LV, P.EF
KER = os.path.join(DD, 'SIDE-kernel')
FIND, OT, CORR = P.FIND, P.OT, P.CORR
BALPOS = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
EFL = os.path.join(EF, 'Zeta23', 'ExplicitFormula.lean')
H2S = os.path.join(EF, 'SIDEExplicitFormula', 'H2Sign.lean')
README = os.path.join(T, 'corr_row.README.md')
TRIAL = P.TRIAL
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
    L = ['b552 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    df = rd(os.path.join(D, 'b551_defects.txt')).split(NL)
    a = [i + 1 for i, l in enumerate(df) if l.strip().startswith('(d)')][0]
    j = [i + 1 for i, l in enumerate(df) if l.strip().startswith('(j)')][0]
    cite(L, os.path.join(D, 'b551_defects.txt'), a, a + 3, 'b551`s defect (d), the Stormer clash')
    cite(L, os.path.join(D, 'b551_defects.txt'), j, j + 7, 'b551`s defect (j), row 391`s grade cell')
    r391 = lines_with(CORR, r'^\| 391 \|')[0]
    cite(L, CORR, r391, r391, 'SIDE-global-section CORRESPONDENCE.md row 391')
    cr = os.path.join(T, 'corr_row.py')
    cite(L, cr, lines_with(cr, r'^NCELLS')[0], lines_with(cr, r'^HEADS')[0], 'corr_row.py: the six cells, the heads (the grade is the fifth cell)')
    tt = os.path.join(T, 'terminal_table.py')
    cite(L, tt, lines_with(tt, r'^GRADE_RE')[0], lines_with(tt, r'^GRADE_RE')[0], 'terminal_table.py: the grade words')
    cite(L, tt, lines_with(tt, r'^def grade_cells')[0], lines_with(tt, r'^def grade_cells')[0] + 28, 'terminal_table.py: the grade parser (tight)')
    c = lines_with(tt, r"\('CONFLICT' if len\(distinct\) > 1")[0]
    cite(L, tt, c - 13, c + 3, 'terminal_table.py: the CONFLICT rule -- distinct grades over every cell naming the terminal')
    cite(L, os.path.join(D, 'b548_interference.txt'), 1, 21, 'b548`s order-7 table at widths 30-45 (per-zero terms in b548_interference.jsonl)')
    cite(L, os.path.join(D, 'b548_interference.txt'), 64, 77, 'b548`s six movers across 34-41, the pair, the rest')
    cite(L, os.path.join(D, 'b522_report.txt'), 1, 52, 'b522 under (R131): the reach per width, 15-60, and the functional per width from 28')
    fz = jl('b506_c2_results.json')['found']
    L += ['### relay data/b506_c2_results.json `found` -- the off-line zeros of Q0 in the rectangle, t < 150 (%d):' % len(fz)]
    L += ['  σ %.10f  γ %.10f' % tuple(z['rho']) for z in fz] + ['']
    gm = jl('b546_geometry.json')
    L += ['### relay data/b546_geometry.json : narrowest %s ; neg %s ; keys %s (no per-zero width)' % (gm['narrowest'], gm['neg'][:6], sorted(gm)), '']
    cite(L, os.path.join(D, 'b240_first_face_off.txt'), 27, 34, 'b240`s six diagonal cells')
    cite(L, EFL, 90, 100, 'EF_lit (SIDE-explicit-formula %s)' % g(EF, 'rev-parse', '--short', 'HEAD').strip())
    cite(L, EFL, 204, 207, 'paperFT_weilTest`s hypotheses')
    cite(L, H2S, 22, 30, 'classK and h2_sign')
    cite(L, BALPOS, 70, 70, 'BALPOS: Li`s criterion named')
    cite(L, BALPOS, 422, 422, 'BALPOS: the Bombieri-Lagarias citation and the coefficient formula')
    cite(L, BALPOS, 498, 514, 'BALPOS C.7.3: the detection threshold (Voros)')
    for f in ('Kernel/Stormer.lean', 'Kernel/StormerTest.lean'):
        t = rd(os.path.join(KER, f)).split(NL)
        L += ['### SIDE-kernel %s (HEAD %s): namespace and divideOut' % (f, g(KER, 'rev-parse', '--short', 'HEAD').strip())]
        L += ['  :%d %s' % (i + 1, l) for i, l in enumerate(t) if l.startswith('namespace') or re.match(r'^def divideOut\b', l)] + ['']
    cite(L, OT, 11230, 11245, 'OPEN_TRAILS: the toolchain item priced by trial (b551)')
    cite(L, OT, 3544, 3550, 'OPEN_TRAILS: the owed-bridges table, W-ORD-LI-WEIL-BRIDGE at :3548')
    put_txt('b552_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1
def housekeeping_read():
    t = rd(os.path.join(D, 'b552_housekeeping.txt'))
    m = re.search(r'committed (\d+) ; now (\d+) ; added (\d+) ; gone (\d+) ; grade-or-profile changed (\d+) ; head moved (\d+)', t)
    after = re.search(r'### tracked status after: \[(.*?)\]', t)
    commit = re.search(r'### the housekeeping commit: (\w+) (.*)', t)
    out = dict(committed=int(m.group(1)), now=int(m.group(2)), added=int(m.group(3)), gone=int(m.group(4)), changed=int(m.group(5)),
               heads=int(m.group(6)), after_clean=after.group(1) == '', commit=commit.group(1), subject=commit.group(2),
               changes=re.findall(r'(?m)^   changed (.*)$', t), live_subject=g(ROOT, 'log', '-1', '--format=%s', commit.group(1)).strip())
    put_json('b552_housekeeping.json', out)
    print(json.dumps(out, indent=1, ensure_ascii=False))


def table_row(name):
    t = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = t.get('rows', t) if isinstance(t, dict) else t
    r = [x for x in rows if isinstance(x, dict) and x.get('name') == name]
    return dict(grade=r[0]['grade'], cells=[(c['grade'], c['ledger'], c['line']) for c in r[0]['grade_cells']], head=r[0]['head']) if r else None


BOOL = 'AggregationCircularityShadow.boolGrp'


def row392_cells(num):
    ap = rd(os.path.join(GS, 'AXIOM_PRINTS.txt')).split(NL)
    ln = [i + 1 for i, l in enumerate(ap) if l.startswith("'%s'" % BOOL)][0]
    return [str(num),
            ('boolGrp`S GRADE RESTATED WHERE THE TABLE READS ONE (b552, under (R162)(1)(b)): row 391 quoted the tier-table words of b550 '
             'beside this name while conferring none, and `relay/tools/terminal_table.py` read the quotation as two grades. This row '
             'restates the tier word b550 gave the definition, alone in the grade cell.').replace('`S', '’S'),
            '`Core/AggregationCircularityShadow.lean` -- the definition `boolGrp : Grp Bool` (Bool under XOR)',
            '*does not depend on any axioms* -- `AXIOM_PRINTS.txt`:%d, re-run at b550 equal to the bank' % ln,
            'SHELL -- `boolGrp`',
            'Written 2026-09-28 (b552) through `relay/tools/corr_row.py`. Row 391 stands unedited above.']


def row392():
    import corr_row as CR
    before = table_row(BOOL)
    num = max(CR.numbers_in(rd(CORR))) + 1
    cells = row392_cells(num)
    assert num == 392, num
    import terminal_table as TT
    bad = [i for i, c in enumerate(cells) if i != 4 and TT.GRADE_RE.search(c)]
    assert not bad, bad
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8', errors='replace')
    t = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    after = table_row(BOOL)
    out = dict(number=num, cells=cells, rc=r.returncode, stdout=r.stdout, table_rc=t.returncode, before=before, after=after,
               diff=jl('terminal_table_diff.json'))
    put_json('b552_row392.json', out)
    L = ['b552 -- COMPONENT 1 (b): ROW 392 AND THE TABLE', '', '### the row, written by corr_row.py (exit %d):' % r.returncode, '  ' + ' | '.join(cells), '',
         '### the table regenerated by terminal_table.py (exit %d); diff: %s' % (t.returncode, {k: (len(v) if isinstance(v, list) else v) for k, v in out['diff'].items()}),
         '### %s BEFORE : grade %s ; cells %s' % (BOOL, before['grade'], before['cells']),
         '### %s AFTER  : grade %s ; cells %s' % (BOOL, after['grade'], after['cells']),
         '### the rule (terminal_table.py, the CONFLICT line): distinct grades over every cell naming the terminal; row 391`s two cells remain.']
    put_txt('b552_row392.txt', L)
    print(NL.join(L))


RDM = ('b552 (2026-09-28), under the author`s ruling (R162)(1)(b): a grade cell carries a grade or the word NONE and no quotation. Row 391 '
       'of SIDE-global-section`s CORRESPONDENCE.md quoted another table`s grade words beside a name, and tools/terminal_table.py read the '
       'quotation as two grades.')


def readme():
    if os.path.exists(README):
        sys.exit('### %s EXISTS -- not overwritten' % README)
    open(README, 'wb').write((poss(RDM) + NL).encode('utf-8'))
    out = dict(path='tools/corr_row.README.md', text=poss(RDM), existed_before=False,
               readmes_in_tools=sorted(f for f in os.listdir(T) if 'readme' in f.lower()))
    put_json('b552_readme.json', out)
    print(json.dumps(out, indent=1, ensure_ascii=False))


STH = '### `W-ORD-STORMER-CLASH` — filed 2026-09-28, b552, under the author`s ruling (R162)(1)(c)'


def stormer():
    guard_absent(OT, STH)
    locs = []
    for f in ('Kernel/Stormer.lean', 'Kernel/StormerTest.lean'):
        t = rd(os.path.join(KER, f)).split(NL)
        locs.append((f, [i + 1 for i, l in enumerate(t) if re.match(r'^def divideOut\b', l)][0], [i + 1 for i, l in enumerate(t) if l.startswith('namespace Stormer')][0]))
    L = ['', STH, '', '| # | ID | kind | the item | price | trigger |', '|:--|:--|:--|:--|:--|:--|',
         '| **1** | `W-ORD-STORMER-CLASH` | **KERNEL** | SIDE-kernel declares `Stormer.divideOut` twice: `%s`:%d and `%s`:%d, each '
         '`def divideOut` inside `namespace Stormer` (:%d, :%d). The two modules cannot be imported together; b551`s census probe of the '
         'Kernel library failed on that clash with no object file missing (relay `data/b551_defects.txt` (d)). SIDE-kernel`s cache build '
         'stays YES as the census read it. | rename the test module`s declaration (one `.lean` file, its uses in that file); a fresh '
         'profile of the renamed terminal | **the next SIDE-kernel tag** |' % (locs[0][0], locs[0][1], locs[1][0], locs[1][1], locs[0][2], locs[1][2]),
         '', '*Filed, not started. No kernel byte changes at b552.*', '']
    o = append_to(OT, NL.join(L))
    o['line'] = line_of(OT, STH)
    o['locs'] = locs
    put_json('b552_stormer.json', o)
    print('  OPEN_TRAILS :%s %s' % (o['line'], locs))


CONH = ('### The toolchain item (b551, :11230) -- THE SHARED-CHECKOUT CONSOLIDATION PRICED, appended 2026-09-28, b552, under the '
        'author`s ruling (R162)(1)(e)')


def pkgset(repo):
    m = json.loads(rd(os.path.join(DD, repo, 'lake-manifest.json')) if repo != 'TECHNE-Core' else rd(os.path.join(DD, 'MY-DOwnloads', 'TECHNE-Core', 'lake-manifest.json')))
    return tuple(sorted((p['name'], p.get('rev')) for p in m.get('packages', [])))


def consolidation():
    guard_absent(OT, CONH)
    t = rd(os.path.join(D, 'b552_size.txt'))
    rows = [re.match(r'^(\d+) ([0-9a-f]{40}) (\S+)$', l) for l in t.split(NL)]
    rows = [(int(m.group(1)), m.group(2), m.group(3)) for m in rows if m]
    total = sum(r[0] for r in rows)
    by = {}
    for kb, rev, path in rows:
        by.setdefault(rev[:10], []).append((kb, path))
    st = jl('b551_census_static.json')
    reps = {r['rev'][:10]: [] for r in st['rows'] if r['rev']}
    for r in st['rows']:
        if r['rev']:
            reps[r['rev'][:10]].append(r['repo'])
    same = {rev: len(set(pkgset(x) for x in rs)) == 1 for rev, rs in reps.items() if len(rs) > 1}
    keep = sum(max(k for k, _ in v) for v in by.values())
    gb = lambda k: k / 1024.0 / 1024.0
    par = ('**The consolidation, priced (not done).** The census`s Mathlib checkouts sized as the sum of their file lengths (relay `data/b552_size.txt`; '
           'a `du -sk` run, stopped after its first checkout for speed, is `data/b552_du.txt`): '
           '%d checkouts, **%.1f GB** in all, at %d revs; one checkout per rev would keep about %.1f GB and free about %.1f GB. The largest '
           'group, `5e932f9`, holds %d clones (%.1f GB); within each multi-repository rev the package sets are %s. **How Lake could be '
           'pointed at one checkout:** (i) the manifest`s `packagesDir` field (every manifest here says `.lake/packages`) -- changing it '
           'is a manifest edit per repository, and Lake then shares the package directory and its build outputs; or (ii) a directory '
           'junction for `.lake/packages` (NTFS `mklink /J`, no administrator right), leaving every tracked file untouched. Either way the '
           'repositories of one rev share one Mathlib build, so they must agree on every package rev and on the toolchain -- which the '
           'comparison above prints -- and a build in one writes where the others read. Nothing is moved, linked or deleted at b552.'
           % (len(rows), gb(total), len(by), gb(keep), gb(total - keep), len(by.get('5e932f97dd', [])), gb(sum(k for k, _ in by.get('5e932f97dd', []))),
              '; '.join('`%s` %s' % (k, 'identical' if v else 'NOT identical') for k, v in same.items())))
    o = append_to(OT, NL.join(['', CONH, '', par, '']))
    o['line'] = line_of(OT, CONH)
    o.update(total_kb=total, gb=gb(total), by={k: v for k, v in by.items()}, same=same, keep_gb=gb(keep))
    put_json('b552_consolidation.json', o)
    print(poss(par))
    print('  OPEN_TRAILS :%s' % o['line'])


# ------------------------------------------------------------------------------ COMPONENT 2: READING THREE
PAIR, CREST = 16.290216, 29.551761


def period():
    rows = [json.loads(l) for l in rd(os.path.join(D, 'b548_interference.jsonl')).split(NL) if l.strip()]
    A = [r['a'] for r in rows]
    lnA = [math.log(a) for a in A]
    step = max(lnA[i + 1] - lnA[i] for i in range(len(A) - 1))
    offs = sorted(set(round(t[1], 6) for r in rows for t in r['terms'] if t[0] == 'off'))
    out = []
    for gm in offs:
        v = [next(t[2] for t in r['terms'] if t[0] == 'off' and round(t[1], 6) == gm) for r in rows]
        ch = [lnA[i] + (lnA[i + 1] - lnA[i]) * v[i] / (v[i] - v[i + 1]) for i in range(len(A) - 1) if v[i] * v[i + 1] < 0]
        sp = [ch[i + 1] - ch[i] for i in range(len(ch) - 1)]
        pg = math.pi / gm
        ratios = [s / pg for s in sp]
        floor = pg <= step
        out.append(dict(gamma=gm, values=v, changes_a=[math.exp(c) for c in ch], changes_ln=ch, spacings=sp, pi_over_g=pg, ratios=ratios,
                        mean_ratio=(sum(sp) / len(sp) / pg) if sp else None, below_floor=floor, in_pop=len(ch) >= 2 and not floor,
                        agrees=bool(sp) and all(abs(r - 1) <= 0.15 for r in ratios)))
    pop = [o for o in out if o['in_pop']]
    disagree = [o for o in pop if not o['agrees']]
    crest = [o for o in out if abs(o['gamma'] - CREST) < 1e-5][0]
    cmax_i = max(range(len(A)), key=lambda i: crest['values'][i])
    pair = [r['pair'] for r in rows]
    pmin_local = [A[i] for i in range(1, len(A) - 1) if pair[i] < pair[i - 1] and pair[i] < pair[i + 1]]
    c1 = len(disagree) * 2 <= len(pop) if pop else None
    c2 = 35 <= A[cmax_i] <= 39
    c3 = any(36 <= a <= 38 for a in pmin_local)
    L = ['b552 -- COMPONENT 2: READING THREE -- THE PERIOD IN ln a AT Q0, ORDER 7 (H4 of (R162)(2)); every row READING', '',
         '### the population: b548`s per-width terms (data/b548_interference.jsonl), widths %s-%s (%d widths), one term per off-line orbit; '
         'widths 46-60 are not banked per zero and are not computed' % (A[0], A[-1], len(A)),
         '### the grid floor: the largest step in ln a is ln(31/30) = %.4f; an orbit whose π/γ is not above it is BELOW FLOOR' % step, '',
         '  γ             π/γ      changes  at a                                              spacings in ln a (ratio to π/γ)                          mean-ratio agrees  status']
    for o in out:
        L.append('  %-12.6f  %.4f   %-7d  %-48s  %-56s  %-10s %-6s  %s' % (
            o['gamma'], o['pi_over_g'], len(o['changes_a']), ', '.join('%.2f' % x for x in o['changes_a'])[:48],
            ', '.join('%.4f (%.2f)' % (s, r) for s, r in zip(o['spacings'], o['ratios']))[:56], ('%.2f' % o['mean_ratio']) if o['mean_ratio'] else '-',
            'yes' if o['agrees'] else 'no', 'BELOW FLOOR' if o['below_floor'] else ('IN' if o['in_pop'] else 'fewer than two changes')))
    L += ['', '### the 29.551761 orbit across the widths: %s' % ', '.join('%g:%+.2f' % (a, x) for a, x in zip(A, crest['values'])),
          '### its largest value at a = %g (%+.3f)' % (A[cmax_i], crest['values'][cmax_i]),
          '### the 16.290216 pair across the widths: %s' % ', '.join('%g:%+.1f' % (a, x) for a, x in zip(A, pair)),
          '### the pair`s local minima inside the range: %s (it falls at every step: %s)' % (pmin_local or 'NONE', all(pair[i + 1] < pair[i] for i in range(len(pair) - 1))), '',
          '### H4, clause by clause:',
          '  H4.1  in the population (%d orbits), every consecutive spacing within 15 %% of π/γ for a majority : %s (%d of %d disagree: %s)' % (
              len(pop), 'HOLDS' if c1 else 'FAILS', len(disagree), len(pop), ', '.join('%.2f' % o['gamma'] for o in disagree)),
          '  H4.2  the 29.551761 term at a maximum within 35-39                                  : %s (a = %g)' % ('HOLDS' if c2 else 'FAILS', A[cmax_i]),
          '        beside it, the ruling`s own word ("at a crest"): the term`s local maxima inside the range at a = %s ; one within 35-39: %s (scores nothing; the sealed face reads "largest value")' % (
              [A[i] for i in range(1, len(A) - 1) if crest['values'][i] > crest['values'][i - 1] and crest['values'][i] > crest['values'][i + 1]],
              any(35 <= A[i] <= 39 for i in range(1, len(A) - 1) if crest['values'][i] > crest['values'][i - 1] and crest['values'][i] > crest['values'][i + 1])),
          '  H4.3  the 16.290216 pair in a trough at 36-38                                         : %s' % ('HOLDS' if c3 else 'FAILS -- the pair has no local minimum in the banked range; it falls monotonically'),
          '  REFUTER 1  spacings off by more than 15 %% for a majority                              : %s' % ('fires' if not c1 else 'does not fire'),
          '  REFUTER 2  the 29.55 term not at a maximum within 35-39                               : %s' % ('fires' if not c2 else 'does not fire'),
          '### H4 IS %s' % ('REFUTED' if (not c1 or not c2) else ('NOT REFUTED, BUT FAILS IN PART' if not c3 else 'NOT REFUTED')),
          '### the 29.551761 orbit alone (N2): spacings %s against π/γ %.4f -- every one within 15 %%: %s ; the mean %.4f (ratio %.2f)' % (
              ', '.join('%.4f' % s for s in crest['spacings']), crest['pi_over_g'], crest['agrees'], sum(crest['spacings']) / len(crest['spacings']), crest['mean_ratio']),
          '### a caveat printed with it: the spacings of many orbits alternate short-long (e.g. γ = 43.86); consecutive pairs of spacings are '
          'not each π/γ. This reading does not say why; no model is fitted.']
    crest_local = [A[i] for i in range(1, len(A) - 1) if crest['values'][i] > crest['values'][i - 1] and crest['values'][i] > crest['values'][i + 1]]
    res = dict(crest_local_maxima=crest_local, crest_local_in_35_39=any(35 <= x <= 39 for x in crest_local), rows=out, population=[o['gamma'] for o in pop], disagree=[o['gamma'] for o in disagree], step=step, crest_max_a=A[cmax_i],
               pair=pair, pair_local_minima=pmin_local, c1=c1, c2=c2, c3=c3, refuted=(not c1 or not c2),
               n2=crest['agrees'], crest_spacings=crest['spacings'], crest_pi_over_g=crest['pi_over_g'])
    put_json('b552_period.json', res)
    put_txt('b552_period.txt', L)
    print(NL.join(L[-14:]))


# ------------------------------------------------------------------------------ COMPONENT 3: READING FOUR
def regimes():
    t = rd(os.path.join(D, 'b240_first_face_off.txt')).split(NL)[27:34]
    a2 = [int(l.split()[0]) for l in t if l.strip() and l.split()[0].isdigit()]
    gm = jl('b546_geometry.json')
    sw = jl('b548_sweep.json')['H2']['smallest_negative']
    st = {}
    for l in rd(os.path.join(D, 'b548_sweep_q.jsonl')).split(NL):
        if l.strip():
            r = json.loads(l)
            if str(r['p']) in sw and r['a'] == sw[str(r['p'])]:
                st[str(r['p'])] = r.get('status')
    big = math.sqrt(max(a2))
    det = gm['narrowest']
    small = min(sw.values())
    line = ('b240`s cells a² = %s, a = %s ; b522`s first negative width at order 7 within its reach: %g ; b548`s smallest negative width per '
            'order: %s ; ratios to √12 = %.4f: b522 %.2f, b548 smallest %.2f (order %s, %s)' % (
                a2, ['%.4f' % math.sqrt(x) for x in a2], det, ', '.join('p=%s: %g (%s)' % (k, v, st.get(k)) for k, v in sw.items()),
                big, det / big, small / big, min(sw, key=lambda k: sw[k]), st.get(min(sw, key=lambda k: sw[k]))))
    L = ['b552 -- COMPONENT 3: READING FOUR -- THE WIDTH REGIMES (READING, no hypothesis)', '', line, '',
         '### its limit: b240`s dissonance concerns the identity`s LEFT side (the traces) and is not touched by this line; the two sets of '
         'widths are compared as numbers, not as the same quantity.']
    res = dict(a2=a2, a=[math.sqrt(x) for x in a2], detect=det, smallest=sw, status=st, ratio_detect=det / big, ratio_smallest=small / big,
               n3=9 <= det / big <= 11, line=line)
    put_json('b552_regimes.json', res)
    put_txt('b552_regimes.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 4: READING FIVE
LIH = ('### `W-ORD-LI-WEIL-BRIDGE` (the row at :3548, the items at :11203) -- ITS LEADING ITEM, appended 2026-09-28, b552, under the '
       'author`s ruling (R162)(2), READING FIVE')


def li_class():
    ef = rd(EFL).split(NL)
    h2 = rd(H2S).split(NL)
    bp = rd(BALPOS).split(NL)
    efs = NL.join(ef[96:100])
    wt = NL.join(ef[204:207])
    ck = NL.join(h2[21:30])
    compact_req = 'HasCompactSupport k' in efs and 'ContDiff ℝ 2 k' in efs
    ck_even = 'k (-x) = k x' in ck and 'HasCompactSupport k' in ck
    li = bp[421]
    quotes_tf = bool(re.search(r'(?i)test function', NL.join(bp[417:426] + bp[497:515])))
    # the Li side read from the formula: h(ρ) = 1 − (1 − 1/ρ)^n ; ρ = 1/2 + i z
    reading = [
        'h_n(ρ) = 1 − (1 − 1/ρ)^n = 1 − ((ρ − 1)/ρ)^n is rational in ρ with its only pole at ρ = 0 (order n).',
        'Written in the ordinate, ρ = 1/2 + i z, the pole sits at z = i/2: h_n is not entire in z. The transform of a compactly supported '
        'function is entire (Paley-Wiener, classical), so the Li test function is NOT compactly supported.',
        'Under z -> −z, (ρ − 1)/ρ becomes its reciprocal on the line; h_n(−z) ≠ h_n(z) for n ≥ 1, so the test function is NOT even.',
        'As |ρ| -> ∞, h_n(ρ) = n/ρ + O(1/ρ²): the zero sum of h_n does not converge absolutely (Σ 1/|γ| diverges); the literature sums ρ '
        'and 1 − ρ together.',
        'Smoothness is not read from the banks: no bank states the test function itself.']
    cls = [('EF_lit (Zeta23/ExplicitFormula.lean:97-100)', 'compact (HasCompactSupport k)', 'none required', 'C² (ContDiff ℝ 2 k)',
            'the zero sum is part of the conclusion (Summable)'),
           ('classK (H2Sign.lean:24-26)', 'compact (HasCompactSupport k)', 'even (k (-x) = k x)', 'C², and k = h ⋆ h~ with h C², compact',
            'inherits EF_lit`s'),
           ('the Li test function (BALPOS :422`s formula, read)', 'NOT compact (a pole of h_n at ρ = 0)', 'NOT even', 'NOT ESTABLISHED FROM THE BANKS',
            'NOT absolute (h_n ~ n/ρ)')]
    in_k = False
    admitted = False
    h5 = not in_k
    L = ['b552 -- COMPONENT 4: READING FIVE -- THE LI TEST CLASS AGAINST classK (H5 of (R162)(2)); READING', '',
         '### EF_lit, verbatim (SIDE-explicit-formula %s, Zeta23/ExplicitFormula.lean:97-100):' % g(EF, 'rev-parse', '--short', 'HEAD').strip(), efs, '',
         '### paperFT_weilTest`s hypotheses, verbatim (:205-207):', wt, '',
         '### classK and h2_sign, verbatim (SIDEExplicitFormula/H2Sign.lean:22-30):', ck, '',
         '### BALPOS`s Li formula, verbatim (BALANCE_AND_POSITIVITY.md:422):', li, '',
         '### BALPOS quotes a Bombieri-Lagarias test function: %s -- it quotes the coefficient formula λ_n = Σ_ρ [1 − (1 − 1/ρ)ⁿ] and '
         'the citation (J. Number Theory 77 (1999) 274-287), and C.7.3 (:498-514) quotes Voros`s threshold; no test function is printed there.'
         % ('YES' if quotes_tf else 'NO'), '',
         '### the Li side, read from the formula alone (no source fetched; no computation):'] + ['  - ' + x for x in reading] + [
         '', '  %-52s %-38s %-22s %-44s %s' % ('class', 'support', 'parity', 'smoothness', 'summability')] + [
         '  %-52s %-38s %-22s %-44s %s' % c for c in cls] + [
         '', '### H5: the Li test function lies outside classK: %s ; EF_lit admits it: %s (EF_lit requires compact support, which it lacks)' % (not in_k, admitted),
         '### H5 %s -- refuted only if the Li test function were in classK. The bridge therefore needs the explicit formula on a class wider '
         'than EF_lit`s; entered as its leading item.' % ('HOLDS' if h5 else 'REFUTED'),
         '### "one-sided in log x" (N4`s first clause): NOT ESTABLISHED -- no bank states the test function`s form, and no source is fetched at b552.']
    res = dict(ef_lit=efs, weiltest=wt, classK=ck, li=li, quotes_test_function=quotes_tf, reading=reading, classes=cls,
               compact_required=compact_req, classK_even_compact=ck_even, in_classK=in_k, admitted=admitted, h5=h5,
               n4=compact_req and not in_k, one_sided='NOT ESTABLISHED')
    put_json('b552_li_class.json', res)
    put_txt('b552_li_class.txt', L)
    print(NL.join(L[-12:]))
    if not admitted:
        guard_absent(OT, LIH)
        body = ['', LIH, '',
                '**The leading item, before every lemma already priced:** the explicit formula on a class wider than EF_lit`s. EF_lit '
                '(`Zeta23/ExplicitFormula.lean`:97-100) quantifies over `k` with `ContDiff ℝ 2 k` and `HasCompactSupport k`; `classK` '
                '(`H2Sign.lean`:24-26) adds evenness and the `h ⋆ h~` form. The Li test function, read from the coefficient formula BALPOS '
                'quotes (:422), has a transform with a pole at ρ = 0, so it is not compactly supported (Paley-Wiener), not even, and its zero '
                'sum converges only with ρ and 1 − ρ taken together (relay `data/b552_li_class.txt`). So λ_n is not a value of EF_lit as '
                'compiled: the bridge first needs the explicit formula for a non-compact, one-sided-or-not, conditionally summed test '
                'function -- then the lemmas priced at b546. **Priced, not begun.**', '']
        o = append_to(OT, NL.join(body))
        o['line'] = line_of(OT, LIH)
        res['trail'] = o
        put_json('b552_li_class.json', res)
        print('  OPEN_TRAILS :%s' % o['line'])


# ------------------------------------------------------------------------------ COMPONENT 5: READING SIX
def scatter():
    fz = jl('b506_c2_results.json')['found']
    gm = jl('b546_geometry.json')
    rp = jl('b522_reach.json')
    per_zero = [k for k in list(gm) + list(rp) if re.search(r'(?i)per.?zero|detect.*zero|zero.*detect', k)]
    rows = sorted(({'sigma': z['rho'][0], 'gamma': z['rho'][1], 'inv': 1.0 / (z['rho'][0] - 0.5)} for z in fz), key=lambda r: r['inv'])
    L = ['b552 -- COMPONENT 5: READING SIX -- DETECTION WIDTH AGAINST (σ, γ) (H6 of (R162)(2)); READING', '',
         '### the zeros: relay data/b506_c2_results.json `found`, the off-line zeros of Q0 with t < 150 in the rectangle (%d)' % len(fz),
         '### the widths: (R131)`s run is b522 (data/b522_report.txt, data/b522_reach.json): it banks the functional`s sign per width -- one '
         'Q0 detection width for the functional as a whole (b546_geometry.json `narrowest` = %s) -- and no width per zero. Keys searched for '
         'a per-zero width in b522_reach.json and b546_geometry.json: %s' % (gm['narrowest'], per_zero or 'NONE'), '',
         '  σ              γ               1/(σ − 1/2)    a_detect     ln a_detect']
    L += ['  %.10f   %-14.10f  %-13.4f  NOT BANKED   NOT BANKED' % (r['sigma'], r['gamma'], r['inv']) for r in rows]
    L += ['', '### the population (zeros carrying a banked per-zero detection width): EMPTY -- H6 NOT SCORABLE: (R162)(2) asks for a '
          'per-zero width and (R131)`s bank carries a width for the whole functional; a per-zero width would be new computation, which the '
          'ruling forbids at this act.', '### the zeros not scored: all %d, named above.' % len(rows)]
    res = dict(rows=rows, per_zero_keys=per_zero, population=[], h6=None, n5=None, narrowest=gm['narrowest'])
    put_json('b552_detection_scatter.json', res)
    put_txt('b552_detection_scatter.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 1 (a) AND COMPONENT 6
N6L = '*Appended at b552 (2026-09-28) to b551`s entry (`FINDINGS.md`:5715), under `(R162)`(1)(a):*'
FH = ('## Four readings from the banks: the period in ln a at Q0, the width regimes of the identity`s cells and the bench, the Li test '
      'class against classK, detection width against distance from the line')
HEADING = ('### b552 — b551 settled; four readings from the banks under (R162): the period in ln a, the width regimes, the Li test class '
           'against classK, detection width against (σ, γ)')


def n6_line():
    guard_absent(FIND, N6L)
    s = (N6L + ' (N6)`s clause "main of every repository unchanged" was the navigator`s wording; the seat`s declared reading -- no `.lean` '
         'byte on any main or on the trial branch -- is its meaning, and its score stands HELD. SIDE-global-section`s main moved by row 391 '
         'alone, as (R161)(4) ordered.')
    o = append_to(FIND, NL.join(['', s, '']))
    o['line'] = line_of(FIND, N6L)
    put_json('b552_n6_line.json', o)
    print('  FINDINGS :%s' % o['line'])


def findings():
    guard_absent(FIND, FH)
    pe, rg, li, sc, r2, cs = jl('b552_period.json'), jl('b552_regimes.json'), jl('b552_li_class.json'), jl('b552_detection_scatter.json'), jl('b552_row392.json'), jl('b552_consolidation.json')
    L = ['', FH, '',
         '*Filed at b552 on the author`s ruling `(R162)`(2). Graded READING throughout: arithmetic on banked numbers, no new computation. '
         'Banks: relay `data/b552_period.txt`, `data/b552_regimes.txt`, `data/b552_li_class.txt`, `data/b552_detection_scatter.txt`.*', '',
         '**Reading Three -- the period in ln a (H4).** On b548`s per-zero terms at Q0, order 7, widths 30-45 (not 30-60: no wider width is '
         'banked per zero), %d off-line orbits change sign at least twice with π/γ above the grid`s floor; %d of them have a consecutive '
         'spacing more than 15 %% from π/γ. H4.1 %s; H4.2 (the 29.55 term at a maximum within 35-39) %s as the face read it, its largest banked value at a = %g -- though it has a crest (a local maximum) at a = %s; H4.3 '
         '(the 16.29 pair in a trough at 36-38) %s -- the pair falls at every banked width. **H4 %s.** The 29.55 orbit`s spacings are %s '
         'against π/γ = %.4f.' % (
             len(pe['population']), len(pe['disagree']), 'HOLDS' if pe['c1'] else 'FAILS', 'HOLDS' if pe['c2'] else 'FAILS', pe['crest_max_a'], ', '.join('%g' % x for x in pe['crest_local_maxima']),
             'HOLDS' if pe['c3'] else 'FAILS', 'REFUTED' if pe['refuted'] else 'NOT REFUTED',
             ', '.join('%.4f' % s for s in pe['crest_spacings']), pe['crest_pi_over_g']), '',
         '**Reading Four -- the width regimes.** %s. **Its limit:** b240`s dissonance concerns the identity`s left side and is untouched; '
         'the two sets are compared as numbers.' % poss(rg['line']).replace('`', '’'), '',
         '**Reading Five -- the Li test class against classK (H5).** EF_lit requires `ContDiff ℝ 2 k` and `HasCompactSupport k`; classK adds '
         'evenness and the `h ⋆ h~` form. BALPOS quotes the coefficient formula and no test function. Read from that formula, the Li '
         'side`s transform has a pole at ρ = 0, so its test function is not compactly supported, not even, and not absolutely summable '
         'over the zeros: outside classK, and outside EF_lit as compiled. **H5 %s.** "One-sided in log x" is not established from the '
         'banks. The explicit formula on a wider class is entered as the bridge`s leading item (OPEN_TRAILS.md:%s).' % (
             'HOLDS' if li['h5'] else 'REFUTED', (li.get('trail') or {}).get('line')), '',
         '**Reading Six -- detection width against (σ, γ) (H6).** **NOT SCORABLE**: the %d off-line zeros of Q0 below 150 are banked with σ '
         'and γ (b506), but (R131)`s run banks one detection width for the functional (a = %g), none per zero. The table prints each zero`s '
         'σ, γ and 1/(σ − 1/2) with its width NOT BANKED.' % (len(sc['rows']), sc['narrowest']), '',
         '**b551 settled.** Row 392 restates `boolGrp``s tier word alone in its grade cell; after regeneration the table reads it %s (before: '
         '%s) -- the table`s rule counts distinct grades over every cell, and row 391`s two cells remain. The consolidation priced: %.1f GB '
         'across %d checkouts.' % (r2['after']['grade'], r2['before']['grade'], cs.get('gb', 0), len(cs.get('by', {})) and sum(len(v) for v in cs['by'].values())), '',
         '**Next keystone:** THE_KEYSTONE_CENSUS.', '',
         '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited; nothing here is a statement about RH or about ζ’s zeros.*', '']
    text = NL.join(L).replace('`boolGrp``s', '`boolGrp`’s')
    o = append_to(FIND, text)
    o['line'] = line_of(FIND, FH)
    put_json('b552_findings.json', o)
    print('  FINDINGS :%s' % o['line'])


PRIOR_PP = 'a6565c8'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md'}
MEMDIR = P.MEMDIR
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': 'b4c9ebe'}


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    out = {}
    for k, h in PRE_HEADS.items():
        p = os.path.join(DD, k)
        out[k] = sorted(x for x in g(p, 'diff', '--name-only', h, 'main').split(NL) if x.strip())
    return out


def scores():
    r2, pe, rg, li, sc, du, hk = (jl('b552_row392.json'), jl('b552_period.json'), jl('b552_regimes.json'), jl('b552_li_class.json'),
                                  jl('b552_detection_scatter.json'), jl('b552_consolidation.json'), jl('b552_housekeeping.json'))
    committed = g(PP, 'log', '-1', '--pretty=%s').startswith('b552 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in g(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in g(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b552_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b552_')) if tk else None
    m = mains()
    lean = [(k, f) for k, v in m.items() for f in v if f.endswith('.lean')]
    gs_ok = set(m['SIDE-global-section']) <= {'CORRESPONDENCE.md'}
    others = all(not m[k] for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula'))
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(TRIAL, 'rev-parse', 'HEAD').strip(), status=g(TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    return dict(
        n1=bool(r2.get('after')) and r2['after']['grade'] == 'SHELL',
        n2=bool(pe.get('n2')),
        n3=bool(rg.get('n3')),
        n4=bool(li.get('n4')),
        n5=sc.get('n5'),
        n6=not lean and others and gs_ok and not zen and tok == 0 and dep and all(pref.values()) and set(written) <= WRITE_OK
        and trial['head'].startswith('f22ff35') and trial['status'] == '',
        mains=m, prefixes=pref, written=written, zen=zen, token=tok, deposit_clean=dep, trial=trial,
        s1=bool(r2.get('after')) and r2['after']['grade'] == 'CONFLICT',
        s2=bool(hk.get('after_clean')),
        s3=du.get('gb', 0) > 80)


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    r2, pe, rg, li, du = jl('b552_row392.json'), jl('b552_period.json'), jl('b552_regimes.json'), jl('b552_li_class.json'), jl('b552_consolidation.json')
    L = ['=' * 104, 'b552 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- boolGrp before %s, after %s ; after-cells %s ; the rule: distinct grades over every cell (row 391`s two remain).' % (
             w(sc['n1']), r2['before']['grade'], r2['after']['grade'], r2['after']['cells']),
         '  **(N2)** ### **%s.** -- the 29.551761 orbit`s spacings %s against π/γ %.4f (every one within 15 %%: %s).' % (
             w(sc['n2']), ['%.4f' % s for s in pe['crest_spacings']], pe['crest_pi_over_g'], pe['n2']),
         '  **(N3)** ### **%s.** -- 34 / √12 = %.2f (read within [9, 11]); beside it the smallest banked negative width %s over √12 = %.2f.' % (
             w(sc['n3']), rg['ratio_detect'], min(rg['smallest'].values()), rg['ratio_smallest']),
         '  **(N4)** ### **%s.** -- on its clauses: not compactly supported (a pole of h_n at ρ = 0), outside classK, EF_lit requires HasCompactSupport (printed: %s) ; "one-sided in log x": NOT ESTABLISHED.' % (
             w(sc['n4']), li['compact_required']),
         '  **(N5)** ### **%s.** -- no bank carries a per-zero detection width; the population is empty.' % w(sc['n5']),
         '  **(N6)** ### **%s.** -- mains changed %s ; `.lean` none ; nothing at Zenodo %s ; token %s ; deposit clean %s ; prefixes %s ; trial worktree %s.' % (
             w(sc['n6']), {k: v for k, v in sc['mains'].items() if v} or 'NONE', not sc['zen'], sc['token'], sc['deposit_clean'], sc['prefixes'], sc['trial']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- boolGrp after regeneration: %s.' % (w(sc['s1']), r2['after']['grade']),
         '  **(S2)** ### **%s.** -- relay`s tracked status after the housekeeping commit: clean %s.' % (w(sc['s2']), jl('b552_housekeeping.json').get('after_clean')),
         '  **(S3)** ### **%s.** -- the census`s Mathlib checkouts: %.1f GB.' % (w(sc['s3']), du.get('gb', 0)),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b552_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b552_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b552_desk_notes.txt', L)
    put_json('b552_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b552 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b552_housekeeping.txt', 'b552_row392.txt', 'b552_du.txt', 'b552_size.txt', 'b552_period.txt', 'b552_regimes.txt', 'b552_li_class.txt', 'b552_detection_scatter.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b552_housekeeping.json', 'b552_readme.json', 'b552_stormer.json', 'b552_consolidation.json', 'b552_n6_line.json', 'b552_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)[:3000]))
    L += ['### THE BRANCHES : see data/b552_branches.txt', '=' * 132]
    put_txt('b552_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc, pe, rg, li, r2, fj, st, cs, n6 = (scores(), jl('b552_period.json'), jl('b552_regimes.json'), jl('b552_li_class.json'), jl('b552_row392.json'),
                                          jl('b552_findings.json'), jl('b552_stormer.json'), jl('b552_consolidation.json'), jl('b552_n6_line.json'))
    body = ['', HEADING, '',
            '**(R162) ratified.** (1) b551 settled: (a) the (N6) reading accepted; (b) row 392 written, the README line entered; (c) '
            'W-ORD-STORMER-CLASH filed; (d) the pending terminal table committed as housekeeping, and so at every close from now; (e) the '
            'shared-checkout consolidation priced, not done. (2) Four readings from the banks, graded READING, H4-H6 fixed by the ruling. '
            '(3) THE_KEYSTONE_CENSUS next.', '',
            '**Entered:** FINDINGS.md:%s (the (N6) line) and :%s (the entry); OPEN_TRAILS.md:%s (W-ORD-STORMER-CLASH), :%s (the '
            'consolidation price), :%s (the bridge`s leading item); SIDE-global-section CORRESPONDENCE.md row 392; relay '
            '`tools/corr_row.README.md`.' % (n6['line'], fj['line'], st['line'], cs['line'], (li.get('trail') or {}).get('line')), '',
            '**The readings:** H4 %s (H4.1 %s, H4.2 %s, H4.3 %s); Reading Four printed with its limit; H5 %s; H6 NOT SCORABLE (no per-zero '
            'width banked). **Row 392:** boolGrp reads %s after regeneration.' % (
                'REFUTED' if pe['refuted'] else 'NOT REFUTED', 'HOLDS' if pe['c1'] else 'FAILS', 'HOLDS' if pe['c2'] else 'FAILS',
                'HOLDS' if pe['c3'] else 'FAILS', 'HOLDS' if li['h5'] else 'REFUTED', r2['after']['grade']), '',
            '**CP-1:** open; the cascade resumes with THE_KEYSTONE_CENSUS.', '',
            '**Next:** THE_KEYSTONE_CENSUS.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane and no numerical lane opened at this act.** Nothing deposits; nothing at Zenodo written; no `.lean` file edited; '
            'no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; the four '
            'lists stay OPEN; nothing here is a statement about RH or about ζ’s zeros.', '']
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
    put_json('b552_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'housekeeping_read': housekeeping_read, 'row392': row392, 'readme': readme, 'stormer': stormer,
          'consolidation': consolidation, 'period': period, 'regimes': regimes, 'li_class': li_class, 'scatter': scatter,
          'n6_line': n6_line, 'findings': findings, 'components': components, 'desk': desk, 'trail': trail}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
