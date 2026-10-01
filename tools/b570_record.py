# -*- coding: utf-8 -*-
"""b570_record.py -- THE ACT'S RECORD TOOL, UNDER (R180). ### ONE SUBCOMMAND PER BANK.

### ### b570: LANE TWO, ACT TEN -- GRH-WEIL ACT FIVE. Subcommands write only `data/b570_*` unless the docstring names a
### ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`).
"""
import contextlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E0   # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
EF = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
V011 = '19b7d1e48a40ca22618722306194404423dca224'
STD3 = ['propext', 'Classical.choice', 'Quot.sound']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


# ================================================================================ READING (1)
RELAY = ROOT.replace('\\', '/')
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
READS = [
    ('vendored Zeta23 WeilEF/VerticalLine (digamma_growth_strip; norm_logDeriv_Gammaℝ_le; the prime side; gamma_line_shift)', EF, V011,
     'Zeta23/WeilEF/VerticalLine.lean', [100, 115, 177, 238, 261, 626, 659]),
    ('the held attempt (b569)', EF, 'grh-weil-b569-held', 'SIDEExplicitFormula/Chi/VerticalLine.lean', [36, 47]),
    ('kernel Chi/Statement (EF_lit_chi)', EF, V011, 'SIDEExplicitFormula/Chi/Statement.lean', [42]),
    ('Mathlib LSeries/Dirichlet (the twisted von Mangoldt series)', MATHLIB, 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11',
     'Mathlib/NumberTheory/LSeries/Dirichlet.lean', [402, 409]),
    ('relay terminal_table.py (the three supersession forms; the act:line choice)', RELAY, 'HEAD', 'tools/terminal_table.py',
     [140, 154, 166, 192, 772, 885]),
    ('PLACE-papers FACES_LEDGER (ch_iff_rh`s row)', PP, 'HEAD', 'FACES_LEDGER.md', [497]),
    ('relay the addendum form', RELAY, 'HEAD', 'data/b568_b567_h18b_addendum.txt', [1, 2, 5]),
    ('relay b569 closing push-out bank', RELAY, 'HEAD', 'data/b569_closing_push_out.txt', [1, 2, 4, 5, 6, 7]),
    ('relay b569 Bulka bank (the counts; the paragraph)', RELAY, 'HEAD', 'data/b569_bulka_generic.txt', [132, 133, 134, 136]),
]


def reads():
    L = ['b570 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, lines in READS:
        src = g(repo, 'show', '%s:%s' % (rev, path))
        L.append('### %s -- %s @ %s' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip()))
        sl = src.split(NL)
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    mb = [m for m in ('Complex.digamma_def', 'Complex.differentiableAt_Gamma', 'Complex.Gamma_ne_zero')]
    L += ['', '### the Mathlib Gamma facts the ζ argument names (VerticalLine :261-:428): ' + ', '.join(mb)]
    put_txt('b570_reads.txt', L)


# ================================================================================ COMPONENT 1 (f): the survey
DECL = re.compile(r'^theorem\s+([^\s(:{\[]+)(.*?):=', re.M | re.S)


def survey():
    """### every theorem header of SIDEExplicitFormula/** at v0.11 graded by the rule without and with the CLASS clause."""
    files = [x for x in g(EF, 'ls-tree', '-r', '--name-only', V011, 'SIDEExplicitFormula').split(NL) if x.endswith('.lean')]
    real = E0.class_case
    moved, n = [], 0
    for f in files:
        src = g(EF, 'show', '%s:%s' % (V011, f))
        for m in DECL.finditer(src):
            head = ' '.join(m.group(2).split())
            n += 1
            E0.class_case = lambda t, h: False
            old = E0.grade(head, 'theorem')[0]
            E0.class_case = real
            new, why, _b = E0.grade(head, 'theorem')
            if old != new:
                moved.append(dict(name=m.group(1), file=f, line=src.count(NL, 0, m.start()) + 1, old=old, new=new, why=why))
    E0.class_case = real
    two = {'LFunction_zeros_finite_of_isCompact', 'EF_zero_sum_summable_chi'}
    ok = sorted(x['name'] for x in moved) == sorted(two)
    L = ['b570 -- (R180)(2)(f): THE CLASS-MEMBERSHIP CLAUSE, SURVEYED: every theorem header of SIDE-explicit-formula/SIDEExplicitFormula at '
         'v0.11 = %s graded without and with the clause' % V011[:7], '',
         '### files %d ; theorem headers %d ; moved %d' % (len(files), n, len(moved))]
    for x in moved:
        L.append('    %s :%d  %-40s %s -> %s  (%s)' % (x['file'], x['line'], x['name'], x['old'], x['new'], x['why'][:120]))
    L += ['', '### ### **THE CLAUSE MOVES %s: %s** -- b569`s two χ theorems re-graded under it, the E0 rule unedited otherwise.'
          % ('EXACTLY THE TWO χ GRADES' if ok else 'A DIFFERENT SET', sorted(x['name'] for x in moved))]
    put_txt('b570_class_survey.txt', L)
    put_json('b570_class_survey.json', dict(headers=n, files=len(files), moved=moved, exactly_two=ok))


# ================================================================================ COMPONENT 1 (g): the supersession, HELD
def supersession():
    import terminal_table as TT
    t = jl('terminal_table.json')
    row = [r for r in t['rows'] if r['repo'] == 'SIDE-explicit-formula' and r['name'].endswith('.ch_iff_rh')][0]
    cells = row['grade_cells']
    corr = io.open(os.path.join('D:/SIDE-global-section', 'CORRESPONDENCE.md'), encoding='utf-8').read()
    mentions = sorted(set(int(m.group(1)) for l in corr.split(NL) for m in [re.match(r'^\|\s*(\d+)\s*\|', l)] if m and 'ch_iff_rh' in l))
    corr_cells = [c for c in cells if c['ledger'] == TT.CORR_LABEL]
    trail_cells = [c for c in cells if c['ledger'] == TT.TRAIL_LABEL]
    find_cells = [c for c in cells if c['ledger'] == TT.FIND_LABEL]
    faces_cells = [c for c in cells if c['ledger'].endswith('FACES_LEDGER.md')]
    # ### the positive control: the CORRESPONDENCE form on a synthetic pair of CORRESPONDENCE cells
    lines = TT.corr_row_lines()
    rn = max(lines)
    ctl_in = [dict(ledger=TT.CORR_LABEL, line=lines[rn], grade='ENCODES', quote='`x` ENCODES'),
              dict(ledger=TT.CORR_LABEL, line=10 ** 6, grade='DERIVES', quote='SUPERSEDES row %d: DERIVES' % rn)]
    ctl_out = TT.supersede(ctl_in)
    ctl = [c['grade'] for c in ctl_out] == ['DERIVES']
    # ### the dry computation: what the ruled line would add, a new CORRESPONDENCE cell for ch_iff_rh carrying
    # ### `SUPERSEDES row N: T0` and the ruling's reason (whose grade word is DERIVES), N any row that mentions ch_iff_rh
    n0 = mentions[0] if mentions else rn
    dry_new = dict(ledger=TT.CORR_LABEL, line=10 ** 6, grade='DERIVES',
                   quote='`ch_iff_rh` SUPERSEDES row %d: T0 -- an equivalence of two Mathlib-anchored statements, DERIVES, standard '
                         'three, no premise' % n0)
    dry = TT.supersede([dict(c) for c in cells] + [dry_new])
    distinct = sorted(set(c['grade'] for c in dry))
    mapped = sorted(set(TT.synonym(c['grade']) for c in dry))
    dry_grade = distinct[0] if len(distinct) == 1 else ('CONFLICT' if len(mapped) > 1 else mapped[0])
    # ### the CONFLICT count: the committed table, and a fresh in-memory regeneration (nothing written)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        R = TT.build()
    fresh_conf = sum(1 for r in R['rows'] if r['grade'] == 'CONFLICT')
    fresh_row = [r for r in R['rows'] if r['repo'] == 'SIDE-explicit-formula' and r['name'].endswith('.ch_iff_rh')][0]
    L = ['b570 -- (R180)(2)(g): THE ch_iff_rh SUPERSESSION -- HELD AT ITS FORM, THE HALT PROVED ROUTE BY ROUTE', '',
         '### THE CELL: the committed table (relay data/terminal_table.json) grades SIDEExplicitFormula.B321.ch_iff_rh %s from %d cell(s):'
         % (row['grade'], len(cells))]
    L += ['    %s :%s  %s  %s' % (c['ledger'], c['line'], c['grade'], (c.get('quote') or '')[:140]) for c in cells]
    L += ['### the table carries no tier column (its header, terminal_table.py :880); there is no T2 cell -- the T2 was the tier law',
          '### applied to this grade on b568`s page; under (R179)(4)`s key the page already prints T0 (b569, PLACE-papers bd2a616).', '',
          '### ROUTE 1 -- `SUPERSEDES row N:` (terminal_table.py :140-:164) removes cells read from CORRESPONDENCE rows. ch_iff_rh`s cells '
          'from CORRESPONDENCE: %d. Rows that mention ch_iff_rh at all: %s -- none carries a grade cell for it in the table.'
          % (len(corr_cells), mentions or 'none'),
          '### ROUTE 2 -- `SUPERSEDES OPEN_TRAILS :N for <t>:` removes cells read from OPEN_TRAILS lines: ch_iff_rh`s OPEN_TRAILS cells: %d.'
          % len(trail_cells),
          '### ROUTE 3 -- `SUPERSEDES FINDINGS :N for <t>:` removes cells read from FINDINGS lines: ch_iff_rh`s FINDINGS cells: %d.'
          % len(find_cells),
          '### ROUTE 4 -- FACES_LEDGER: the table`s reader has no supersession form for it; ch_iff_rh`s FACES_LEDGER cells: %d.'
          % len(faces_cells),
          '### POSITIVE CONTROL -- the CORRESPONDENCE form on a synthetic pair (row %d`s line, and a superseding cell): kept %s -> works: %s'
          % (rn, [c['grade'] for c in ctl_out], ctl), '',
          '### THE DRY COMPUTATION (terminal_table`s own supersede and synonym; nothing written): the ruled line as a new CORRESPONDENCE',
          '###   cell for ch_iff_rh -- "%s"' % dry_new['quote'],
          '###   leaves %s ; the row would read %s (it reads %s).' % ([(c['ledger'].split('/')[-1], c['line'], c['grade']) for c in dry], dry_grade,
                                                                       row['grade']),
          '', '### THE CONFLICT COUNT: the committed table %d ; this act`s fresh regeneration (in memory) %d ; ch_iff_rh in it: %s.'
          % (t['counts']['conflict'], fresh_conf, fresh_row['grade']),
          '### the ruled line would move the count to %d.' % (fresh_conf + (1 if dry_grade == 'CONFLICT' and fresh_row['grade'] != 'CONFLICT' else 0)), '',
          '### ### **HELD. THE LINE IS NOT WRITTEN.** The ruled form reaches CORRESPONDENCE cells; ch_iff_rh`s one cell is FACES_LEDGER :497,',
          '### which no supersession form of the table reaches; written, the line would add a second cell and make the row CONFLICT, the',
          '### opposite of "the page and the table then agree". What would carry the ruling: a FACES_LEDGER supersession form taught to the',
          '### table, or a FACES_LEDGER row appended in the ledger`s own form -- neither is ordered at this act. ROUTED TO THE AUTHOR.']
    put_txt('b570_supersession.txt', L)
    put_json('b570_supersession.json', dict(grade=row['grade'], cells=cells, corr_cells=len(corr_cells), trail_cells=len(trail_cells),
                                            find_cells=len(find_cells), faces_cells=len(faces_cells), mentions=mentions, control=ctl,
                                            dry_grade=dry_grade, conflict_committed=t['counts']['conflict'], conflict_fresh=fresh_conf,
                                            written=False))


def addendum():
    """### (R180)(3): the pipe slip after b569's closing record, in (R177)(3)'s declared-reading addendum form."""
    cap = rd('b569_closing_push_out.txt')
    need = [('the capture opened', r'^push_gated: capture on -> /d/relay/data/b569_closing_push_out\.txt \(2026-10-01T07:21:14Z\)$'),
            ('the push line', r'^push_gated: repo /d/relay ; branch push-b569-closing ; tip e2bf000374f707331fd99b2e696a0d28f6eb7c76 ;'),
            ('git`s own push output', r'^   51ab367b\.\.e2bf0003  push-b569-closing -> main$'),
            ('the read-back', r'^push_gated: main read back at the remote: e2bf000374f707331fd99b2e696a0d28f6eb7c76$'),
            ('the DONE line', r'^push_gated: DONE -- main and 0 tag\(s\) pushed and read back$')]
    found = [(w, re.search(p, cap, re.M) is not None) for w, p in need]
    seal = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b569_registration_2026-10-01.txt')], capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout
    L = ['### b569 -- THE DECLARED-READING ADDENDUM FOR THE PIPE SLIP, written AFTER b569`s close by b570 under (R180)(3), in the addendum '
         'form of (R177)(3).',
         '### The sealed face data/b569_registration_2026-10-01.txt is NOT edited (reg_seal --verify: %s); b569`s closing record is not '
         'edited.' % ('SEAL INTACT' if 'SEAL INTACT' in seal else '### NOT INTACT'),
         'DECLARED READING ADDENDUM: the closing push, "no push`s status passes through a pipe" (relay tools/push_gated.sh :9, its rule (1)), carried by (R180)(3)',
         '### THE SLIP: after b569`s closing record was committed (relay e2bf0003), the seat ran `push_gated.sh` for push-b569-closing with '
         'its output piped through `grep -v awk` and took the exit status from PIPESTATUS[0] (0). push_gated.sh`s own header (:9, its rule '
         '(1)) forbids it; b569`s face carried no clause on pipes. The push succeeded and was read back equal.',
         '### THE CAPTURE FILE`S COMPLETENESS (relay data/b569_closing_push_out.txt, written by push_gated.sh`s own PUSH_GATED_LOG tee, '
         'upstream of the pipe), line by line:']
    L += ['###   %-26s %s' % (w, 'PRESENT' if ok else '### ABSENT') for w, ok in found]
    L += ['### ### **THE CAPTURE IS COMPLETE: %s.** The no-pipe rule is unchanged; every later push of b570 runs unpiped.'
          % all(ok for _, ok in found)]
    put_txt('b570_b569_pipe_addendum.txt', L)


def _Q():
    import b566_record as R6
    return R6.Q


def bulka_lines():
    """### OPEN_TRAILS (appends): (R180)(4) -- W-ORD-BULKA-GENERIC closed as a reading; the χ-Li converse priced at W-ORD-GRH-WEIL."""
    Q = _Q()
    wb = Q.line_of(Q.OT, '| **3** | `W-ORD-BULKA-GENERIC`')
    wg = Q.line_of(Q.OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    h1 = '*Appended 2026-10-01 by b570, under the author’s ruling `(R180)`(4), to W-ORD-BULKA-GENERIC'
    h2 = '*Appended 2026-10-01 by b570, under the author’s ruling `(R180)`(4), to the W-ORD-GRH-WEIL entry'
    Q.guard_absent(Q.OT, h1)
    a1 = ('\n%s (:%s) -- CLOSED AS A READING:* the converse as vendored names a ζ object in 8 of its 33 modules (relay '
          '`data/b569_bulka_generic.txt` :132) and is not an argument over a zero configuration as written (the same bank :136-:151: '
          'it is stated for Bulka’s own ξ and zero type). No build follows from this work-order.\n' % (h1, wb))
    a2 = ('\n%s (:%s) -- A PRICED ITEM, NOT STARTED, THE χ-LI CONVERSE:* when wanted, it is (V1)-(V4) at χ, with the pairing across '
          '(χ, χ⁻¹) in (V1) -- the reflection ρ ↦ 1 − ρ̄ in place of ρ ↦ 1 − ρ -- and the power-sum step the generic part (relay '
          '`data/b569_bulka_generic.txt` :136-:151). Price: one kernel act after `EF_lit_chi`.\n' % (h2, wg))
    r = [Q.append_to(Q.OT, a1), Q.append_to(Q.OT, a2)]
    put_json('b570_bulka_lines.json', dict(bulka_line=Q.line_of(Q.OT, h1), grh_line=Q.line_of(Q.OT, h2), wb=wb, wg=wg, appends=r))
    print(jl('b570_bulka_lines.json'))


# ================================================================================ COMPONENTS 3-4: E0, rowgen
TERMS = [('421', 'norm_logDeriv_Gammaℝ_le_wide', 'SIDEExplicitFormula/Chi/GammaWide.lean'),
         ('422', 'norm_logDeriv_gammaFactor_le', 'SIDEExplicitFormula/Chi/VerticalLine.lean'),
         ('423', 'prime_side_line_chi', 'SIDEExplicitFormula/Chi/VerticalLine.lean'),
         ('424', 'gamma_line_shift_chi', 'SIDEExplicitFormula/Chi/VerticalLine.lean'),
         ('425', 'rectangle_identity_chi', 'SIDEExplicitFormula/Chi/Contour.lean')]
ROW_ACT = '420'
NS = 'SIDEExplicitFormula.GRHWeil.'


def e0(rev='main'):
    """### every declaration of the act graded by the shared E0 rule (with (R180)(2)(f)'s clause) at `rev`, its print, and
    ### rowgen's record of the terminals of record (b566_record.Q.rowgen_record, IMPORTED)."""
    import b569_record as R9
    Q = _Q()
    pr = rd('b570_chi_prints.txt')
    P0 = R9.prints_axioms(pr)
    dj = jl('b570_decls_chi.json')
    tip = g(EF, 'rev-parse', rev).strip()
    rows, srcs = {}, {}
    L = ['b570 -- COMPONENTS 3-4: THE E0 READ -- EVERY DECLARATION GRADED, THE ROWGEN RECORD', '',
         '### the prints of record: relay data/b570_chi_prints.txt ; the statements at %s (%s).' % (tip[:7], rev)] + E0.RULE_TEXT + ['']
    for d in dj['decls']:
        n = d['name']
        if d['file'] not in srcs:
            srcs[d['file']] = g(EF, 'show', '%s:%s' % (tip, d['file']))
        head, _ln = R9.header_of(srcs[d['file']], n.split('.')[-1])
        gr, why, _b = E0.grade(head or '', d['kind'])
        ax = P0.get(n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, file=d['file'],
                       header_read=head is not None)
        L.append('    %-40s %-10s %s  -- %s' % (n.split('.')[-1], gr, 'std3' if rows[n]['std3'] else ax, (why or '')[:120]))
    cons = {n: P0.get(n) for n in dj['consumed']}
    L += ['', '### THE CONSUMED TERMINALS, their prints:'] + ['    %-62s %s' % (n, 'std3' if a is not None and set(a) <= set(STD3) else a)
                                                            for n, a in cons.items()]
    recs, ctl = [], (True,)
    for rn, n, rel in TERMS:
        r, ctl = Q.rowgen_record([NS + n], rel, tip, pr)
        recs += r
    L += ['', '### THE ROWGEN RECORD (at %s):' % tip[:7]]
    L += ['    %-40s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])) for r in recs]
    cnt = {k: sum(1 for r in rows.values() if r['grade'] == k) for k in ('DERIVES', 'INTERFACES')}
    gate = (all(r['std3'] for r in rows.values()) and all(a is not None and set(a) <= set(STD3) for a in cons.values())
            and all(r['header_read'] for r in rows.values()) and ctl[0] and not any(r['defenc'] for r in recs) and all(r['check'] for r in recs))
    L.append('### ### **THE GATE: %s** -- theorems %d (DERIVES %d, INTERFACES %d), consumed %d' % ('PASS' if gate else 'FAIL', len(rows),
                                                                                                cnt['DERIVES'], cnt['INTERFACES'], len(cons)))
    put_txt('b570_e0.txt', L)
    put_json('b570_e0.json', dict(rows=rows, consumed=cons, gate=gate, rowgen=recs, rowgen_control=ctl[0], tip=tip, counts=cnt))


def rowgen_diff():
    Q = _Q()
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
    import rowgen as RG
    recs = jl('b570_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    L = ['b570 -- THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE RECORDS AGAINST CORRESPONDENCE ROWS 421-425', '']
    res = {}
    for rn, n, rel in TERMS:
        rowtxt = [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        mine = [list(x) for x in out if isinstance(x, tuple) and x[0] == NS + n]
        res[rn] = dict(found=len(rowtxt) == 1, mine=mine)
        L.append('### row %s found: %s' % (rn, len(rowtxt) == 1))
        L += ['    ' + str(x) for x in out]
    ascii_ok = lambda name: re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.]*', NS + name) is not None
    unread = [rn for rn, n, rel in TERMS if not ascii_ok(n)]
    ok = all(v['found'] and v['mine'] and all(m[1] == ['ok'] for m in v['mine']) for rn, v in res.items() if rn not in unread)
    L += ['', '### rows whose terminal name is not ASCII -- rowgen.py :135 cites `[A-Za-z_][A-Za-z0-9_.]*` only, so it cannot read them '
          '(defect (e)): %s' % unread,
          '### ### **THE ROWGEN DIFF : %s on the %d readable rows ; NOT READ BY ROWGEN %s.**' % ('CLEAN' if ok else 'NOT CLEAN',
                                                                                          len(TERMS) - len(unread), unread)]
    put_txt('b570_rowgen.txt', L)
    put_json('b570_rowgen.json', dict(rows=res, clean=ok, unreadable=unread))


# ================================================================================ COMPONENT 5: THE RECORD
V012 = '141e844b74453a4c329bb6b3a8a70954b6cb04cf'
HOLD_FACT = ('FullLine`s fold of the left vertical onto the right line -- for ζ Λ′/Λ(1 − s) = −Λ′/Λ(s); for χ, −(log N + Λ′/Λ(s, χ⁻¹)) '
             '(Chi/XiLogDeriv.lean), so FullLine`s χ statement carries χ⁻¹ and the conductor and is not yet stated')
INSTR = dict(readme='5fb20050', e0='b8b6487a', rowsort='97c80040')


def scores():
    sv, sp, rt = jl('b570_class_survey.json'), jl('b570_supersession.json'), rd('b570_prime_probe_out.txt')
    e = jl('b570_e0.json')
    kp = rd('b570_kernel_push_out.txt')
    zb_names = [l for l in rt.split(NL) if '@@MOD Zeta23.FromPNTPlus.ZetaBounds' in l]
    zf = [l for l in rt.split(NL) if re.search(r'ZeroFree|zero_free|ZetaZeroFree', l)]
    edge = [l.split()[1] for l in rt.split(NL) if l.startswith('@@EDGEC')]
    ns = [x for x in g(EF, 'diff', '--name-status', V011, 'main').split(NL) if x.strip()]
    gw = rd('b570_attempt_gw_env.txt')
    gw_ok = 'rc=0' in gw and 'error' not in gw
    v012 = ('tag v0.12 peeled local %s remote %s' % (V012, V012)) in kp
    S = dict(
        H22a=('HELD' if gw_ok and e['rows'].get(NS + 'norm_logDeriv_Gammaℝ_le_wide', {}).get('std3') else 'REFUTED',
              'GammaWide.lean compiled at its first elaboration from the Mathlib and Zeta23 facts Zeta23`s proof names, the interval '
              'changed (data/b570_attempt_gw_env.txt: rc=0, no message; data/b570_wide_statements.txt); no missing fact'),
        H22b=('HELD', 'its refutation clause not met: the prime side`s consumed constants name no zero-free lemma (zero-free names: %d; '
              'ZetaBounds constants: %d; data/b570_prime_read.txt). In its letter its first clause is not what the read shows: the prime '
              'side lives on Re s = c > 1 and consumes the Dirichlet series (Mathlib`s LSeries_vonMangoldt / for χ the twisted series), '
              'not the Abel-summation representation' % (len(zf), len(zb_names))),
        H22c=('REFUTED', 'EF_lit_chi is HELD, but not inside VerticalLine`s prime side: the prime side and the Γ side for χ compiled '
              '(Chi/VerticalLine.lean) and the rectangle identity too (Chi/Contour.lean); the HOLD is at %s; no sorryAx on main' % HOLD_FACT),
        N1=('REFUTED', 'the clause moves %d readings, not two: %s (data/b570_class_survey.txt); every one is a ContDiff / HasCompactSupport '
            '/ IsCompact binder on a variable its conclusion mentions' % (len(sv['moved']), sorted(x['name'] for x in sv['moved']))),
        N2=('REFUTED', 'the supersession is HELD at its form (data/b570_supersession.txt): ch_iff_rh`s one cell is FACES_LEDGER :497, which '
            'no supersession form reaches; the table reads %s, CONFLICT %d before and %d after (unchanged); written, the ruled line '
            'would make the row %s' % (sp['grade'], sp['conflict_committed'], sp['conflict_fresh'], sp['dry_grade'])),
        N3=('HELD' if gw_ok else 'REFUTED', 'H22a HELD: GammaWide is Zeta23`s argument with the interval changed (data/b570_gen_gammawide.py.txt)'),
        N4=('HELD', 'H22b HELD on its refutation clause'),
        N5=('REFUTED', 'EF_lit_chi is HELD later than VerticalLine`s prime side, at FullLine`s fold'),
        N6=('HELD' if (v012 and all(x.startswith('A') or x == 'M\tREADME.md' for x in ns)) else 'REFUTED',
            'v0.12 = %s made by push_gated.sh and read back, with the wider-strip bound; v0.11..main additions only and README appended '
            '(%d paths); nothing at Zenodo; nothing deposits' % (V012[:7], len(ns))),
        S1=('HELD', 'N2 REFUTED; the supersession HELD; the dry computation gives %s' % sp['dry_grade']),
        S2=('HELD', 'the prime side for χ compiled (prime_side_line_chi); the HOLD is later'),
        S3=('HELD', 'EF_lit_chi HELD again, at FullLine'),
        counts=dict(decls=len(e['rows']), moved=len(sv['moved']), conflict=sp['conflict_fresh'], edge=len(edge)),
    )
    put_json('b570_scores.json', S)
    pr = ['b570 -- COMPONENT 4: THE PRIME-SIDE READ, (R180)(5)(c), BEFORE THE PRIME-SIDE BUILD',
          '### the probe: relay data/b570_prime_probe.lean.txt, one lean call from the kernel checkout at grh-weil-b570 (= v0.11 + GammaWide); '
          'its output banked whole as relay data/b570_prime_probe_out.txt (written 07:50Z; the first prime-side elaboration 07:51:09Z)',
          '### from Zeta23.WeilEF.prime_side_line: Zeta23 constants reached %d ; boundary constants %d' % (len([l for l in rt.split(NL) if l.startswith('@@REACH')]), len(edge)),
          '### BY CLASS: Zeta23 generic (VerticalLine`s Hfn/tilt/inversion, PaperFT, ExplicitFormula, Bridge): all the Zeta23 constants reached ;',
          '###   ZetaBounds (continuation, strip bounds, zero-free region): %d ; zero-free names anywhere: %d ;' % (len(zb_names), len(zf)),
          '###   ζ-specific boundary names: %s' % [x for x in edge if 'vonMangoldt' in x or 'riemannZeta' in x or x.startswith('LSeries')],
          '### for χ these become Mathlib`s DirichletCharacter.LSeries_twist_vonMangoldt_eq and LSeriesSummable_twist_vonMangoldt '
          '(Dirichlet.lean :409, :402) with LFunction_eq_LSeries; no Abel-summation representation is consumed (Re s = c > 1).',
          '### ### **H22b : %s.**' % S['H22b'][0]]
    put_txt('b570_prime_read.txt', pr)
    for k in ('H22a', 'H22b', 'H22c', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3'):
        print('  %-5s %-8s %s' % (k, S[k][0], S[k][1][:130]))


DEFECTS = [
    '(a) THE PIPE-SLIP ADDENDUM`S FIRST WRITE QUOTED A CLAUSE b569`S FACE DOES NOT CARRY ("No push passes through a pipe", as b569`s '
    'section (Z)); the no-pipe rule is push_gated.sh`s own :9. Corrected before any arm read the bank.',
    '(b) THE SHELL AND HEREDOC TRAPS, TWICE: a backtick inside a double-quoted python -c string broke the SUITE_README command after its '
    'heredoc had appended the section (the section once; the test bank then written from a scratch script); the act`s AxiomCheck '
    'generator, patched through a heredoc, lost an escaped quote (a SyntaxError before any file was written); fixed with the Edit tool.',
    '(c) THE E0 READ RAN AT main BEFORE THE MERGE: the record tool`s dispatcher dropped the rev argument, so two runs read main = v0.11, '
    'where the modules do not yet exist; the read`s own gate printed FAIL both times. The dispatcher now passes its arguments; the read '
    'was taken at the branch tip and again at main after the fast-forward.',
    '(d) THE HOLD IS BY THE ACT`S EXTENT, NOT BY A FAILING STATEMENT: VerticalLine`s χ-analogue (prime side and Γ side) and Contour`s '
    'rectangle identity compiled; Zeta23`s FullLine was read and not attempted, because its fold (Λ′/Λ(1 − s) = −Λ′/Λ(s)) has for χ the '
    'form −(log N + Λ′/Λ(s, χ⁻¹)), so its χ statement must be restated with χ⁻¹ and the conductor rather than ported by substitution. No '
    'held branch is made (nothing failed). Routed to the author.',
    '(e) ROWGEN CANNOT READ ONE TERMINAL ROW: rowgen.py :135 cites backticked names of ASCII characters only, so row 421`s terminal '
    'norm_logDeriv_Gammaℝ_le_wide (its ℝ) yields no record line; the four other rows read [ok]. rowgen is not edited (no edit ordered); '
    'the row`s print and E0 grade stand on their own banks. Routed to the author.',
    '(f) THE SUITE, PRE-PUSH RUN ONE: G-WORK-ORDERS-UPDATED`S POSITIVE CONTROL PASSED -- its mutation removed one of the two occurrences '
    'of its needle in the trail record, so the arm still read true; G-ARMS-NO-LIVE-LIMB failed with it, as designed. The mutation now '
    'removes every occurrence; the table files restored to their committed state and the suite re-run.',
]


def defects():
    put_txt('b570_defects.txt', ['### b570 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + ['    ' + d for d in DEFECTS])


def findings():
    Q = _Q()
    S = jl('b570_scores.json')
    title = ('## GRH-Weil, act five: the Γℝ log-derivative bound on the wider strip, the prime side for χ, the explicit formula for χ '
             'held at FullLine’s fold')
    Q.guard_absent(Q.FIND, title)
    c = S['counts']
    e = ['', title, '',
         '*Filed at b570 on the author’s ruling `(R180)`. Banks: relay `data/b570_wide_statements.txt`, `data/b570_prime_read.txt`, '
         '`data/b570_chi_prints.txt`, `data/b570_e0.txt`, `data/b570_class_survey.txt`, `data/b570_supersession.txt`, '
         '`data/b570_b569_pipe_addendum.txt`, `data/b570_test_e0_rule.txt`, `data/b570_test_row_sort.txt`. Nothing about the zeros of ζ or '
         'of any L(s, χ) is claimed beyond the compiled statements’ own words.*', '',
         '**b569 at its weight** (`(R180)`(1)): v0.11 = `19b7d1e`, the two converses joined into iffs, seven χ-modules along the route, the '
         'summability half of the formula for χ; held at the odd Γ factor.', '',
         '**The four items** (`(R180)`(2)-(3)). (d) The third as-of form kept; the suite README names the three forms (relay `%s`). (f) The '
         'class-membership clause written in the shared rule with its test (relay `%s`); surveyed over every theorem header of the kernel '
         'at v0.11, it moves %d readings -- the two χ theorems of b569 and seven kernel lemmas whose binders restrict a test function '
         'the statement is about; no ledger cell moves. (g) HELD at its form: the cell the ruling names is read from FACES_LEDGER :497, '
         'which the table’s supersession forms do not reach, and the ruled line, written, would make the row a conflict; the CONFLICT '
         'count stays %d; routed to the author. (i) The row-sort (relay `%s`): a name’s CORRESPONDENCE cells read in row-number order; no '
         'row renumbered. The pipe slip recorded by addendum, the capture file complete.' % (INSTR['readme'], INSTR['e0'], c['moved'],
                                                                                           c['conflict'], INSTR['rowsort']), '',
         '**W-ORD-BULKA-GENERIC** closed as a reading; the χ-Li converse entered at W-ORD-GRH-WEIL as a priced item, not started.', '',
         '**The build** (`(R180)`(5)), SIDE-explicit-formula v0.12 = `%s`, %d declarations at the standard three: GammaWide (the Γℝ '
         'log-derivative bound on 3/2 ≤ σ ≤ 5/2, Zeta23’s argument with the interval changed); VerticalLine for χ (the odd case; the prime '
         'side on Re s = c > 1 from Mathlib’s twisted von Mangoldt series; the Γ side); Contour for χ (the rectangle identity, no pole '
         'terms). **HELD** at %s; FullLine was read and not attempted, so the hold is the act’s extent and not a failing statement.'
         % (V012[:7], c['decls'], HOLD_FACT), '',
         '**The scores.** H22a %s; H22b %s; H22c %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; the seat’s (S1) %s, (S2) %s, '
         '(S3) %s.' % tuple(S[k][0] for k in ('H22a', 'H22b', 'H22c', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3')), '',
         '**Next.** `EF_lit_chi` is HELD again, so per `(R180)`(6): act six at the frontier -- FullLine for χ restated with χ⁻¹ and the '
         'conductor, then Horizontal, ZeroSumLimit, the assembly and Main; the h2_sign_chi ⟺ GRH_chi composition after it. The author '
         'rules on the closing.', '',
         '*Nothing deposits; nothing at Zenodo written; no existing statement of any kernel changed; no sentence here claims priority; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b570_findings.json', dict(entry_line=Q.line_of(Q.FIND, title), append=r, title=title))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title))


def trail():
    Q = _Q()
    S = jl('b570_scores.json')
    fj, bj = jl('b570_findings.json'), jl('b570_bulka_lines.json')
    head = ('### b570 — lane two, act ten under (R180): GRH-Weil act five -- the wider strip, the odd case, the prime and Γ sides for '
            'χ, the rectangle identity; held at FullLine’s fold; b569’s four items; W-ORD-BULKA-GENERIC closed')
    Q.guard_absent(Q.OT, head)
    rows = ['', head, '',
            '**(R180) ratified.** (1) b569 entered at its weight. (2) The four items: (d) kept, (f) the clause, (g) the supersession, (i) '
            'the row-sort. (3) The pipe slip by addendum. (4) W-ORD-BULKA-GENERIC closed. (5) GRH-Weil act five. (6) The gates; v0.12; '
            'the next act named at the closing.', '',
            '**Entered:** FINDINGS.md:%s (the entry); OPEN_TRAILS.md:%s (W-ORD-BULKA-GENERIC closed), :%s (the χ-Li converse priced), this '
            'record; SIDE-global-section CORRESPONDENCE.md rows 420-425; SIDE-explicit-formula main = **v0.12** = `%s`, grh-weil-b570 '
            'pushed by name. Relay instrument commits: the README `%s`, the class clause `%s`, the row-sort `%s`. The (g) supersession '
            'HELD and not written (relay `data/b570_supersession.txt`).' % (fj['entry_line'], bj['bulka_line'], bj['grh_line'], V012[:7],
                                                                          INSTR['readme'], INSTR['e0'], INSTR['rowsort']), '',
            '**H22a %s · H22b %s · H22c %s. (N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, '
            '(S3) %s.' % tuple(S[k][0] for k in ('H22a', 'H22b', 'H22c', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3')), '',
            '**Next:** per `(R180)`(6), with `EF_lit_chi` HELD again: act six at the frontier -- FullLine for χ, its fold restated with '
            'χ⁻¹ and the conductor -- and the h2_sign_chi ⟺ GRH_chi composition after it. The author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; nothing at Zenodo written; no existing statement changed; no Zeta23 or vendored '
            'file edited or added; ERRATA untouched; FACES_LEDGER untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit '
            'left it; the four lists stay OPEN; nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own '
            'words.', '']
    r = Q.append_to(Q.OT, NL.join(rows))
    put_json('b570_trail.json', dict(line=Q.line_of(Q.OT, head), head=head, append=r))
    print(jl('b570_trail.json')['line'])


def rows():
    """### the act's row and one row per terminal of record, through relay tools/corr_row.py; `|` in a statement written `‖`."""
    import b569_record as R9
    Q = _Q()
    e = jl('b570_e0.json')
    for rn, n, rel in TERMS:
        if e['rows'][NS + n]['grade'] != 'DERIVES' or not e['rows'][NS + n]['std3']:
            sys.exit('### %s not graded at the standard three: no row' % n)
    for rn in (ROW_ACT,) + tuple(t[0] for t in TERMS):
        if [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]:
            sys.exit('### ROW %s ALREADY PRESENT' % rn)
    pr = R9.prints_axioms(rd('b570_chi_prints.txt'))
    out = []
    act = [ROW_ACT,
           '**GRH-WEIL ACT FIVE** (b570, under (R180)(5)). SIDE-explicit-formula v0.12 = %s: the Γℝ log-derivative bound on the wider '
           'strip; the odd-χ step; the prime side and the Γ side for χ; the rectangle identity for χ. EF_lit_chi HELD at FullLine`s fold. '
           'Nothing here proves RH or GRH.' % V012[:7],
           'SIDE-explicit-formula SIDEExplicitFormula/Chi/{GammaWide,VerticalLine,Contour}.lean (v0.12 = %s)' % V012[:7],
           '%d declarations print within [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b570_chi_prints.txt)' % len(e['rows']),
           ' ; '.join('`%s` DERIVES' % t[1] for t in TERMS),
           'LANDED at v0.12 = %s; EF_lit_chi HELD; nothing deposits; nothing at Zenodo written.' % V012[:7]]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + act, capture_output=True, text=True, encoding='utf-8')
    out.append(dict(row=ROW_ACT, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    for rn, n, rel in TERMS:
        head = e['rows'][NS + n]['head'].replace('|', '‖')
        cells = [rn, '**%s** (b570, under (R180)(5)), SIDE-explicit-formula v0.12 = %s: `%s%s %s`.' % (n, V012[:7], NS, n, head),
                 '`SIDE-explicit-formula/%s` (v0.12 = %s) : `%s%s`' % (rel, V012[:7], NS, n),
                 '\'%s%s\' depends on axioms: [%s] (relay data/b570_chi_prints.txt)' % (NS, n, ', '.join(pr.get(NS + n) or [])),
                 '`%s` DERIVES' % n,
                 'LANDED at v0.12 = %s; the E0 read at main (relay data/b570_e0.txt); no premise; absolute-value bars written ‖.' % V012[:7]]
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + cells, capture_output=True, text=True,
                           encoding='utf-8')
        out.append(dict(row=rn, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    put_json('b570_rows.json', dict(rows=out, act=act))
    print('  rows', [(o['row'], o['exit']) for o in out])


def desk():
    S = jl('b570_scores.json')
    L = ['=' * 104, 'b570 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H22a-H22c ((R180)(5)).', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H22a', 'H22b', 'H22c')]
    L += ['', '### THE NAVIGATOR`S SIX.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in
                                                        ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    nh = sum(1 for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**'
          % (nh, 6 - nh, sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD'), sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] != 'HELD')), '']
    L += rd('b570_defects.txt').rstrip(NL).split(NL)
    put_txt('b570_desk_notes.txt', L)


def components():
    S = jl('b570_scores.json')
    fj, tj, rj, bj = jl('b570_findings.json'), jl('b570_trail.json'), jl('b570_rows.json'), jl('b570_bulka_lines.json')
    L = ['b570 -- THE COMPONENTS, BANKED UNDER (R180).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; push-b569 branches deleted by name (data/b570_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : the README section relay %s ; the class clause relay %s (7 of 7), the survey %d moved ; the supersession HELD '
         '(data/b570_supersession.txt, CONFLICT %d unchanged) ; the row-sort relay %s (5 of 5) ; the pipe addendum data/b570_b569_pipe_addendum.txt'
         % (INSTR['readme'], INSTR['e0'], S['counts']['moved'], S['counts']['conflict'], INSTR['rowsort']),
         '### COMPONENT 2 : OPEN_TRAILS :%s (W-ORD-BULKA-GENERIC closed), :%s (the χ-Li converse priced)' % (bj['bulka_line'], bj['grh_line']),
         '### COMPONENT 3 : GammaWide.lean, statements first (data/b570_wide_statements.txt), built ; H22a %s ; the odd step compiled' % S['H22a'][0],
         '### COMPONENT 4 : the prime read (data/b570_prime_read.txt) ; H22b %s ; VerticalLine and Contour for χ built ; v0.12 = %s by '
         'push_gated.sh ; HELD at FullLine`s fold ; H22c %s' % (S['H22b'][0], V012[:7], S['H22c'][0]),
         '### COMPONENT 5 : FINDINGS :%s ; OPEN_TRAILS :%s ; CORRESPONDENCE rows %s ; next: act six at the frontier'
         % (fj['entry_line'], tj['line'], ', '.join('%s (exit %d)' % (o['row'], o['exit']) for o in rj['rows']))]
    put_txt('b570_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b570_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
