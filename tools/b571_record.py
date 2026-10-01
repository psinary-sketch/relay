# -*- coding: utf-8 -*-
"""b571_record.py -- THE ACT'S RECORD TOOL, UNDER (R181). ### ONE SUBCOMMAND PER BANK.

### ### b571: LANE TWO, ACT ELEVEN -- GRH-WEIL ACT SIX. Subcommands write only `data/b571_*` unless the docstring names a
### ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`).
"""
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
V012 = '141e844b74453a4c329bb6b3a8a70954b6cb04cf'
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


DEFECTS = [
    '(a) THE FACE`S READING (1) CITES FIVE ZETA23 LINES TWO OR THREE OFF -- horizontal_vanish :45 (is :43), zero_sum_limit :41 (:42), '
    'full_line_identity :52 (:55), Hfn_mirror :37 (:39), EF_lit_zeta :65 (:67): the seat took the numbers from a print that began at '
    'the file`s line 22 and landed on docstring lines; the face is sealed and not edited; the reads bank prints the declaration lines.',
    '(b) THE FACE`S READING (iii) DESCRIBES LEAN`S isLetterLike SHORT OF THE TOOLCHAIN`S OWN: v4.34.0-rc1`s Init/Meta/Defs.lean :101 '
    'also admits the Latin-1 supplement letters (but × ÷) and Latin Extended-A, and isSubScriptAlnum admits U+2C7C; the face listed '
    'neither. The code follows the toolchain`s source (the ruling`s words: Lean`s own identifier set), relay 618143a8.',
    '(c) A STRAY FILE IN relay/tools: a shell append with an empty here-document created relay/tools/b571_record.py.new (empty) while '
    'the seat meant to append to the record tool; it was removed at once by its absolute path in the same session, before any arm read '
    'the tools; nothing read it. Its path is within the (W) glob relay/tools/b571_*.',
    '(d) H23b`S FIRST SCORE READ REFUTED BY A NEEDLE THAT COULD NOT TELL THE CONDUCTOR FROM THE PRIME WEIGHT: the predicate asked that '
    'primeSum_chi`s definition carry no "log", and it carries Real.log n (k at log n); the score was printed, not banked into any '
    'ledger, and the predicate now names the conductor`s own spellings (log N, log (N, Complex.log), each yield printed.',
    '(e) THE FIRST E0 READ WAS TAKEN ON grh-weil-b571 AT 1448289, ONE COMMIT BEFORE THE README AND AxiomCheck COMMIT ac157c1 = v0.13: '
    'the rowgen diff then flagged PIN on rows 427-431 (they cite v0.13). The read was re-run on the branch at its tip ac157c1 (the '
    'merge is a fast-forward, so the branch tip is v0.13); every grade identical; the diff CLEAN on all 5 rows.',
]


def defects():
    put_txt('b571_defects.txt', ['### b571 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + ['    ' + d for d in DEFECTS])


def _Q():
    import b566_record as R6
    return R6.Q


# ================================================================================ READING (1)
RELAY = ROOT.replace('\\', '/')
SGS = 'D:/SIDE-global-section'
READS = [
    ('vendored Zeta23 WeilEF/FullLine (Fline; integrable_Fline; verticals_eq; tendsto_interval_Fline; the horizontals` nonvanishing)',
     EF, V012, 'Zeta23/WeilEF/FullLine.lean', [304, 338, 362, 385, 431]),
    ('vendored Zeta23 WeilEF/Horizontal (horizontal_vanish)', EF, V012, 'Zeta23/WeilEF/Horizontal.lean', [43]),
    ('vendored Zeta23 WeilEF/ZeroSumLimit (zero_sum_limit)', EF, V012, 'Zeta23/WeilEF/ZeroSumLimit.lean', [42]),
    ('vendored Zeta23 WeilEF/FullLineAssembly (full_line_identity)', EF, V012, 'Zeta23/WeilEF/FullLineAssembly.lean', [55]),
    ('vendored Zeta23 WeilEF/Main (Hfn_mirror; EF_lit_zeta)', EF, V012, 'Zeta23/WeilEF/Main.lean', [39, 67]),
    ('vendored Zeta23 WeilEF/VerticalLine (vertical_line_shift; gamma_line_shift)', EF, V012, 'Zeta23/WeilEF/VerticalLine.lean', [443, 659]),
    ('vendored Zeta23 WeilEF/GammaRBracket (gammaR_bracket)', EF, V012, 'Zeta23/WeilEF/GammaRBracket.lean', [114]),
    ('kernel Chi/XiLogDeriv (the χ identity)', EF, V012, 'SIDEExplicitFormula/Chi/XiLogDeriv.lean', [80, 82]),
    ('kernel GRHWeil (the pairing; the χ terms)', EF, V012, 'SIDEExplicitFormula/GRHWeil.lean', [61, 66, 70, 185]),
    ('kernel Chi/Contour (rectangle_identity_chi)', EF, V012, 'SIDEExplicitFormula/Chi/Contour.lean', [27]),
    ('kernel Chi/Statement (EF_lit_chi)', EF, V012, 'SIDEExplicitFormula/Chi/Statement.lean', [42]),
    ('PLACE-papers FACES_LEDGER (ch_iff_rh`s row)', PP, 'HEAD', 'FACES_LEDGER.md', [497]),
    ('relay terminal_table.py at the act`s first commit (the trail and FINDINGS forms; where they are applied)', RELAY, '96daad63',
     'tools/terminal_table.py', [184, 199, 214, 225, 789]),
    ('relay rowgen.py (the backticked-name pattern)', RELAY, '96daad63', 'tools/rowgen/rowgen.py', [135]),
    ('SIDE-global-section CORRESPONDENCE (row 421)', SGS, 'HEAD', 'CORRESPONDENCE.md', [494]),
]


def reads():
    L = ['b571 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, lines in READS:
        src = g(repo, 'show', '%s:%s' % (rev, path))
        L.append('### %s -- %s @ %s' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip()))
        sl = src.split(NL)
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    put_txt('b571_reads.txt', L)


# ================================================================================ COMPONENT 1: the ch_iff_rh line
CHIFF_LINE = ('SUPERSEDES FACES_LEDGER :497 for ch_iff_rh: T0 -- appended 2026-10-01 by b571 under the author’s ruling (R181)(2), '
              'the FACES_LEDGER form taught to the table at relay e693efde; the page’s tier for the row has read T0 since b569 '
              '(PLACE-papers bd2a616); FACES_LEDGER :497 stands unedited above.')


def _table_counts():
    t = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    row = [r for r in t['rows'] if r['name'] == 'SIDEExplicitFormula.B321.ch_iff_rh']
    return t['counts'], (row[0]['grade'] if row else None), ([(c['ledger'], c['line']) for c in row[0]['grade_cells']] if row else None)


def chiff():
    """### PLACE-papers FINDINGS.md (one appended line): (R181)(2) -- the ch_iff_rh line in the ruling`s words; the table counts
    ### read from the COMMITTED table before the append (relay HEAD`s data/terminal_table.json)."""
    Q = _Q()
    Q.guard_absent(Q.FIND, 'SUPERSEDES FACES_LEDGER :497 for ch_iff_rh')
    gw = [w for w in ('DERIVES', 'ENCODES', 'INTERFACES', 'SHELL') if w in CHIFF_LINE]
    if gw or '`' in CHIFF_LINE:
        sys.exit('### the line carries a grade word or a backtick: %s' % gw)
    committed = json.loads(g(RELAY, 'show', 'HEAD:data/terminal_table.json'))
    crow = [r for r in committed['rows'] if r['name'] == 'SIDEExplicitFormula.B321.ch_iff_rh'][0]
    r = Q.append_to(Q.FIND, NL + CHIFF_LINE + NL)
    put_json('b571_chiff_line.json', dict(line=Q.line_of(Q.FIND, 'SUPERSEDES FACES_LEDGER :497 for ch_iff_rh'), text=CHIFF_LINE, append=r,
                                          before=dict(counts=committed['counts'], grade=crow['grade'],
                                                      cells=[(c['ledger'], c['line']) for c in crow['grade_cells']])))
    print(jl('b571_chiff_line.json'))


def chiff_after():
    """### after the regeneration (terminal_table.py, run by the seat): the counts and ch_iff_rh`s row, before and after."""
    j = jl('b571_chiff_line.json')
    counts, grade, cells = _table_counts()
    run = rd('terminal_table_run.txt')
    dirl = [l for l in run.split(NL) if 'FACES_LEDGER-LINE SUPERSESSIONS READ' in l]
    diff = jl('terminal_table_diff.json')
    L = ['b571 -- (R181)(2): THE ch_iff_rh LINE, THE TABLE REGENERATED, THE CONFLICT COUNT BEFORE AND AFTER', '',
         '### THE LINE (PLACE-papers FINDINGS.md :%s): %s' % (j['line'], j['text']), '',
         '### BEFORE (the committed table, relay HEAD before the append): CONFLICT %d ; ENCODES %d ; UNGRADED %d ; ch_iff_rh %s from %s'
         % (j['before']['counts']['conflict'], j['before']['counts']['encodes'], j['before']['counts']['ungraded'], j['before']['grade'],
            j['before']['cells']),
         '### AFTER (this regeneration): CONFLICT %d ; ENCODES %d ; UNGRADED %d ; ch_iff_rh %s from %s'
         % (counts['conflict'], counts['encodes'], counts['ungraded'], grade, cells),
         '### the run`s header: %s' % (dirl[0].strip() if dirl else '### NOT PRINTED'),
         '### the table diff: added %d, gone %d, changed %d -- %s' % (len(diff.get('added') or []), len(diff.get('gone') or []),
                                                                      len(diff.get('changed') or []),
                                                                      [str(x)[:200] for x in (diff.get('changed') or [])][:6]), '',
         '### ### **CONFLICT %d BEFORE AND %d AFTER ; ch_iff_rh`s FACES_LEDGER :497 CELL %s.**'
         % (j['before']['counts']['conflict'], counts['conflict'], 'REMOVED (the row reads %s)' % grade if not cells else 'STILL PRESENT')]
    put_txt('b571_chiff.txt', L)
    put_json('b571_chiff.json', dict(before=j['before'], after=dict(counts=counts, grade=grade, cells=cells), line=j['line'],
                                     changed=diff.get('changed')))


# ================================================================================ COMPONENT 1: rows 421-425 re-read
TERMS570 = [('421', 'norm_logDeriv_Gammaℝ_le_wide'), ('422', 'norm_logDeriv_gammaFactor_le'), ('423', 'prime_side_line_chi'),
            ('424', 'gamma_line_shift_chi'), ('425', 'rectangle_identity_chi')]


def rows570():
    """### (R181)(3): b570`s five terminal rows re-read by rowgen.diff (IMPORTED, after relay 618143a8) against b570`s banked records."""
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
    import rowgen as RG
    recs = jl('b570_e0.json')['rowgen']
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    corr = io.open(SGS + '/CORRESPONDENCE.md', encoding='utf-8').read().replace(chr(13), '').split(NL)
    prior = jl('b570_rowgen.json')
    L = ['b571 -- (R181)(3): ROWS 421-425 RE-READ BY rowgen.diff AFTER THE IDENTIFIER CHANGE (relay 618143a8), b570`s RECORDS', '']
    res = {}
    for rn, n in TERMS570:
        row = [l for l in corr if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(row))
        was = prior['rows'][rn]['mine']
        res[rn] = dict(found=len(row) == 1, now=[list(x) for x in out], was=was)
        L.append('### row %s : now %s ; at b570 %s' % (rn, [list(x) for x in out], was or 'NOT READ'))
    read421 = res['421']['now'] == [['SIDEExplicitFormula.GRHWeil.' + TERMS570[0][1], ['ok']]]
    same = all(res[rn]['now'] == [list(x) for x in res[rn]['was']] for rn, _ in TERMS570[1:])
    L += ['', '### ### **ROW 421 %s ; ROWS 422-425 %s.**' % ('READ, ok' if read421 else 'NOT READ',
                                                            'UNCHANGED' if same else 'CHANGED')]
    put_txt('b571_rows570.txt', L)
    put_json('b571_rows570.json', dict(rows=res, read421=read421, others_unchanged=same))


# ================================================================================ COMPONENT 1: the navigator`s clauses
def nav_clauses():
    """### PLACE-papers OPEN_TRAILS.md (two appended lines): (R181)(1)`s two clauses, recorded as the navigator`s, at b570`s record."""
    Q = _Q()
    rec = Q.line_of(Q.OT, '### b570 — lane two, act ten under (R180)')
    h = '*Appended 2026-10-01 by b571, under the author’s ruling `(R181)`(1), to b570’s record'
    Q.guard_absent(Q.OT, h)
    a1 = ('\n%s (:%s) -- A CLAUSE RECORDED AS THE NAVIGATOR’S:* H22b’s words “consumes the Abel-summation representation” -- the '
          'prime side for χ lives on Re s > 1 and consumes the Dirichlet series (Mathlib’s twisted von Mangoldt series), no Abel '
          'summation (relay `data/b570_prime_read.txt`).\n' % (h, rec))
    a2 = ('\n%s (:%s) -- A CLAUSE RECORDED AS THE NAVIGATOR’S:* the expectation that the class-membership clause moves two '
          'readings -- it moves nine, no ledger cell among them (relay `data/b570_class_survey.txt`).\n' % (h, rec))
    r = [Q.append_to(Q.OT, a1), Q.append_to(Q.OT, a2)]
    lines = [i for i, l in enumerate(Q.rd(Q.OT).split(NL), 1) if l.startswith(h)]
    put_json('b571_nav_clauses.json', dict(record_line=rec, lines=lines, appends=r))
    print(jl('b571_nav_clauses.json'))


# ================================================================================ COMPONENTS 2-3: E0, rowgen
TERMS = [('427', 'verticals_eq_chi', 'SIDEExplicitFormula/Chi/FullLine.lean'),
         ('428', 'horizontal_vanish_chi', 'SIDEExplicitFormula/Chi/Horizontal.lean'),
         ('429', 'zero_sum_limit_chi', 'SIDEExplicitFormula/Chi/ZeroSumLimit.lean'),
         ('430', 'full_line_identity_chi', 'SIDEExplicitFormula/Chi/FullLineAssembly.lean'),
         ('431', 'EF_lit_chi_holds', 'SIDEExplicitFormula/Chi/Main.lean')]
ROW_ACT = '426'
NS = 'SIDEExplicitFormula.GRHWeil.'


def e0(rev='grh-weil-b571'):
    """### every declaration of the act graded by the shared E0 rule at `rev` (the branch, before the merge), its print, and
    ### rowgen's record of the terminals of record (b566_record.Q.rowgen_record, IMPORTED)."""
    import b569_record as R9
    Q = _Q()
    pr = rd('b571_chi_prints.txt')
    P0 = R9.prints_axioms(pr)
    dj = jl('b571_decls_chi.json')
    tip = g(EF, 'rev-parse', rev).strip()
    rows, srcs = {}, {}
    L = ['b571 -- COMPONENTS 2-3: THE E0 READ -- EVERY DECLARATION GRADED, THE ROWGEN RECORD', '',
         '### the prints of record: relay data/b571_chi_prints.txt ; the statements at %s (%s).' % (tip[:7], rev)] + E0.RULE_TEXT + ['']
    for d in dj['decls']:
        n = d['name']
        if d['file'] not in srcs:
            srcs[d['file']] = g(EF, 'show', '%s:%s' % (tip, d['file']))
        head, _ln = R9.header_of(srcs[d['file']], n.split('.')[-1])
        gr, why, _b = E0.grade(head or '', d['kind'])
        ax = P0.get(n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, file=d['file'],
                       header_read=head is not None, kind=d['kind'])
        L.append('    %-46s %-10s %s  -- %s' % (n.split('.')[-1], gr, 'std3' if rows[n]['std3'] else ax, (why or '')[:120]))
    cons = {n: P0.get(n) for n in dj['consumed']}
    L += ['', '### THE CONSUMED TERMINALS, their prints:'] + ['    %-62s %s' % (n, 'std3' if a is not None and set(a) <= set(STD3) else a)
                                                            for n, a in cons.items()]
    recs, ctl = [], (True,)
    for rn, n, rel in TERMS:
        r, ctl = Q.rowgen_record([NS + n], rel, tip, pr)
        recs += r
    L += ['', '### THE ROWGEN RECORD (at %s):' % tip[:7]]
    L += ['    %-40s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])) for r in recs]
    th = [r for r in rows.values() if r['kind'] == 'theorem']
    cnt = {k: sum(1 for r in th if r['grade'] == k) for k in ('DERIVES', 'INTERFACES')}
    gate = (all(r['std3'] for r in rows.values()) and all(a is not None and set(a) <= set(STD3) for a in cons.values())
            and all(r['header_read'] for r in rows.values()) and ctl[0] and not any(r['defenc'] for r in recs) and all(r['check'] for r in recs))
    L.append('### ### **THE GATE: %s** -- declarations %d (theorems %d: DERIVES %d, INTERFACES %d), consumed %d'
             % ('PASS' if gate else 'FAIL', len(rows), len(th), cnt['DERIVES'], cnt['INTERFACES'], len(cons)))
    put_txt('b571_e0.txt', L)
    put_json('b571_e0.json', dict(rows=rows, consumed=cons, gate=gate, rowgen=recs, rowgen_control=ctl[0], tip=tip, rev=rev, counts=cnt))


def rowgen_diff():
    """### the act's terminal rows (427-431) read by rowgen.diff (IMPORTED, Lean's identifier set since relay 618143a8)."""
    Q = _Q()
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
    import rowgen as RG
    recs = jl('b571_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    L = ['b571 -- THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE RECORDS AGAINST CORRESPONDENCE ROWS 427-431', '']
    res = {}
    for rn, n, rel in TERMS:
        rowtxt = [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        mine = [list(x) for x in out if isinstance(x, tuple) and x[0] == NS + n]
        res[rn] = dict(found=len(rowtxt) == 1, mine=mine)
        L.append('### row %s found: %s' % (rn, len(rowtxt) == 1))
        L += ['    ' + str(x) for x in out]
    ok = all(v['found'] and v['mine'] and all(m[1] == ['ok'] for m in v['mine']) for v in res.values())
    L += ['', '### ### **THE ROWGEN DIFF : %s on all %d rows.**' % ('CLEAN' if ok else 'NOT CLEAN', len(TERMS))]
    put_txt('b571_rowgen.txt', L)
    put_json('b571_rowgen.json', dict(rows=res, clean=ok))


# ================================================================================ COMPONENT 4: THE RECORD
V013 = 'ac157c1d0024801116d79cf41126d28780fe1152'
INSTR = dict(faces='e693efde', rowgen='618143a8')
MODULES = ['FullLine', 'Horizontal', 'ZeroSumLimit', 'FullLineAssembly', 'Main']
LANDED = ('EF_lit_chi landed: EF_lit_chi_holds (Chi/Main.lean) proves EF_lit_chi χ hχ h1 for every primitive χ ≠ 1, DERIVES at the '
          'standard three')


def _attempt_ok(name):
    t = rd(name)
    return re.search(r'^=== END \S+ rc=0$', t, re.M) is not None and 'error' not in t


def scores():
    ch, r70, e = jl('b571_chiff.json'), jl('b571_rows570.json'), jl('b571_e0.json')
    kp = rd('b571_kernel_push_out.txt')
    ns = [x for x in g(EF, 'diff', '--name-status', V012, 'main').split(NL) if x.strip()]
    main_src = g(EF, 'show', V013 + ':SIDEExplicitFormula/Chi/Main.lean')
    fl_src = g(EF, 'show', V013 + ':SIDEExplicitFormula/Chi/FullLine.lean')
    stmt = g(EF, 'show', V013 + ':SIDEExplicitFormula/GRHWeil.lean')
    ps = stmt[stmt.index('def primeSum_chi'):stmt.index('def gammaBracket_chi')]
    gb = stmt[stmt.index('def gammaBracket_chi'):stmt.index('def archTerm_chi')]
    fold = fl_src[fl_src.index('theorem verticals_eq_chi'):fl_src.index('theorem tendsto_interval_Fline_chi')]
    heights = fl_src[fl_src.index('theorem completedLFunction_ne_zero_on_horizontals_chi'):fl_src.index('end Heights')]
    hz_src = g(EF, 'show', V013 + ':SIDEExplicitFormula/Chi/Horizontal.lean')
    ef = e['rows'].get(NS + 'EF_lit_chi_holds', {})
    cond_in_ps = [w for w in ('log N', 'log (N', 'Complex.log', 'log ↑N', 'NeZero') if w in ps]
    print('  the conductor`s spellings found in primeSum_chi`s definition: %s (its text carries Real.log n, the prime weight: %s)'
          % (cond_in_ps, 'Real.log n' in ps))
    v013 = ('tag v0.13 peeled local %s remote %s' % (V013, V013)) in kp
    fl_ok = _attempt_ok('b571_attempt_fullline_2.txt')
    h23a_ok = fl_ok and e['rows'].get(NS + 'verticals_eq_chi', {}).get('std3')
    route = [m for m in MODULES[1:]]
    S = dict(
        H23a=('HELD' if fl_ok and e['rows'].get(NS + 'verticals_eq_chi', {}).get('std3') else 'REFUTED',
              'Chi/FullLine.lean compiled at its second elaboration (data/b571_attempt_fullline_2.txt: rc=0, one unused-binder lint, '
              'renamed); the first failed at two local slips, not a missing fact (data/b571_attempt_fullline_1.txt: the LSeries '
              'notation`s token L used as a binder name; an implicit ψ). Every analytic input it consumes was compiled before this act '
              '(data/b571_fullline_statements.txt, the list): the χ identity logDeriv_completedLFunction_one_sub, b562`s pairing '
              'LFunction_inv_conj, logDeriv_completedLFunction, the nonvanishing on Re ≥ 1, the Γ factor`s growth, the twisted von '
              'Mangoldt series, Zeta23`s majorants. The fold verticals_eq_chi consumes the χ identity and no pairing (%s); the pairing '
              'enters at the heights lemma (%s) and at Horizontal (%s)'
              % ('LFunction_inv_conj absent from it' if 'LFunction_inv_conj' not in fold else '### PRESENT',
                 'LFunction_inv_conj present' if 'LFunction_inv_conj' in heights else '### ABSENT',
                 'logDeriv_LFunction_inv_conj present' if 'logDeriv_LFunction_inv_conj' in hz_src else '### ABSENT')),
        H23b=('HELD' if (not cond_in_ps and 'conductor_line_shift' in main_src and 'Real.log (N / Real.pi)' in gb) else 'REFUTED',
              'its refutation clause is not met: the conductor term is FlineCond_chi = H(1−c−it)·log N in Fline_chi (Chi/FullLine.lean); '
              'in EF_lit_chi_holds it is shifted to the critical line by conductor_line_shift (Zeta23`s vertical_line_shift) and enters as '
              'log N·(1/2π)∫ h(r) dr on the archimedean side, where with the Γ part`s −log π it makes gammaBracket_chi`s log(N/π) '
              '(GRHWeil.lean :66); primeSum_chi (:61) carries no log and the zero side Σ m_ρ h(γ_ρ) carries no N. In its letter the '
              'compiled constant is (1/2π)∫ h(r) dr, which by Fourier inversion is k(0) -- the test function at 0, not its transform: no '
              'inversion fact is consumed, so the ĝ(0) form is not what compiles'),
        H23c=('HELD' if ef.get('grade') == 'DERIVES' and ef.get('std3') and e.get('gate') else 'REFUTED',
              'EF_lit_chi lands: EF_lit_chi_holds, E0 %s, prints %s (data/b571_chi_prints.txt, data/b571_e0.txt); no sorryAx on main '
              '(all %d declarations and %d consumed terminals within the standard three)' % (ef.get('grade'), ef.get('axioms'), len(e['rows']),
                                                                                           len(e['consumed']))),
        N1=('HELD' if ch['before']['counts']['conflict'] == ch['after']['counts']['conflict'] == 12 and not ch['after']['cells'] else 'REFUTED',
            'CONFLICT %d before and %d after; ch_iff_rh`s one cell (FACES_LEDGER :497) removed, the row reading %s (data/b571_chiff.txt)'
            % (ch['before']['counts']['conflict'], ch['after']['counts']['conflict'], ch['after']['grade'])),
        N2=('HELD' if r70.get('read421') and r70.get('others_unchanged') else 'REFUTED',
            'row 421 read after relay %s, rows 422-425 unchanged (data/b571_rows570.txt)' % INSTR['rowgen']),
        N3=('HELD' if h23a_ok else 'REFUTED', 'H23a %s' % ('HELD' if h23a_ok else 'REFUTED')),
        N4=('HELD' if not cond_in_ps else 'REFUTED', 'in substance: H23b HELD -- the conductor enters on the archimedean side and nowhere else; in its letter the compiled '
                    'term is log N·(1/2π)∫ h(r) dr, which is log N·k(0) by inversion (not consumed), not ĝ(0)·log N'),
        N5=('REFUTED', 'its first clause: four modules remained after FullLine on the route -- %s (data/b571_module_list.txt); its second '
                       'clause held: EF_lit_chi landed at this act' % ', '.join(route)),
        N6=('HELD' if v013 and ns and all(x.startswith('A\t') or x == 'M\tREADME.md' for x in ns) else 'REFUTED',
            'v0.13 = %s made by push_gated.sh and read back, with the restated FullLine and the four modules after it; v0.12 against '
            'main: %s; nothing at Zenodo; nothing deposits; the kept branches unmoved (the suite`s G-KEPT-BRANCHES)' % (V013[:7], ns)),
        S1=('HELD', 'Horizontal, ZeroSumLimit, FullLineAssembly and Main remained (data/b571_module_list.txt)'),
        S2=('HELD', 'the conductor term is log N·(1/2π)∫ h(r) dr on the archimedean side, joining −log π in log(N/π); no inversion fact is '
                    'consumed (EF_lit_chi_holds` consumed terminals, data/b571_e0.txt)'),
        S3=('HELD', 'as worded: the fold verticals_eq_chi consumes no pairing, Horizontal does (logDeriv_LFunction_inv_conj); the pairing is '
                    'consumed also by FullLine`s heights lemma (completedLFunction_ne_zero_on_horizontals_chi) -- not the fold, but the same '
                    'module, which the expectation did not name'),
        counts=dict(decls=len(e['rows']), theorems=sum(1 for r in e['rows'].values() if r['kind'] == 'theorem'),
                    derives=e['counts']['DERIVES'], interfaces=e['counts']['INTERFACES'], consumed=len(e['consumed']),
                    conflict=ch['after']['counts']['conflict'], modules=len(MODULES)),
    )
    put_json('b571_scores.json', S)
    for k in ('H23a', 'H23b', 'H23c', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3'):
        print('  %-5s %s' % (k, S[k][0]))


def findings():
    Q = _Q()
    S = jl('b571_scores.json')
    title = ('## GRH-Weil, act six: the fold at χ⁻¹ with the conductor, the modules after FullLine, the explicit formula for χ landed')
    Q.guard_absent(Q.FIND, title)
    c = S['counts']
    e = ['', title, '',
         '*Filed at b571 on the author’s ruling `(R181)`. Banks: relay `data/b571_fullline_statements.txt`, `data/b571_module_list.txt`, '
         '`data/b571_chi_prints.txt`, `data/b571_e0.txt`, `data/b571_chiff.txt`, `data/b571_rows570.txt`, `data/b571_test_faces_form.txt`, '
         '`data/b571_test_rowgen_ident.txt`. Nothing about the zeros of ζ or of any L(s, χ) is claimed beyond the compiled statements’ '
         'own words.*', '',
         '**b570 at its weight** (`(R181)`(1)): v0.12 = `141e844`, the wider strip, the odd case, the prime and Γ sides for χ, the '
         'rectangle identity; held at FullLine’s fold, which lands on χ⁻¹ and carries the conductor.', '',
         '**The instruments** (`(R181)`(2)-(3)). The table reads a FACES_LEDGER supersession form (relay `%s`): a line citing a '
         'FACES_LEDGER line removes that line’s cell for the terminal it names, and a line citing a line with no such cell refuses the '
         'regeneration. The line for the clause-and-RH equivalence was then appended here; the table’s CONFLICT count reads %d before and '
         'after, and that row’s one FACES_LEDGER cell is removed. The row generator reads Lean’s own identifier set (relay `%s`); row 421 '
         'is read, rows 422-425 unchanged.' % (INSTR['faces'], c['conflict'], INSTR['rowgen']), '',
         '**The build** (`(R181)`(4)), SIDE-explicit-formula v0.13 = `%s`, %d declarations at the standard three, %d modules: FullLine '
         'for χ restated at χ⁻¹ -- the full-line integrand is H(c+it)·Λ′/Λ(c+it, χ) + H(1−c−it)·Λ′/Λ(c+it, χ⁻¹) + H(1−c−it)·log N, '
         'the left line folded through Λ′/Λ(1 − s, χ) = −(log N + Λ′/Λ(s, χ⁻¹)), the conductor term its own summand; the horizontals, '
         'the left half reflected onto χ⁻¹ and bounded through b562’s pairing; the zero-sum limit; the assembly, with no pole terms; and '
         'Main for χ. **The explicit formula for χ is proved**: for every primitive χ ≠ 1 the zero sum of L(s, χ) with multiplicity '
         'converges absolutely and equals the Γ term minus the prime term. The conductor enters as log N·(1/2π)∫ h(r) dr on the '
         'archimedean side, where with the Γ part’s −log π it makes the bracket’s log(N/π); the prime side and the zero side carry no N.'
         % (V013[:7], c['decls'], c['modules']), '',
         '**The scores.** H23a %s; H23b %s; H23c %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; the seat’s (S1) %s, (S2) %s, '
         '(S3) %s.' % tuple(S[k][0] for k in ('H23a', 'H23b', 'H23c', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3')), '',
         '**Next.** The explicit formula for χ landed, so per `(R181)`(5): act seven is the composition h2_sign_chi ⟺ GRH_chi (the '
         'χ-instance of the criterion with the χ-seam), and CP-5 after it. The author rules on the closing.', '',
         '*Nothing deposits; nothing at Zenodo written; no existing statement of any kernel changed; no sentence here claims priority; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b571_findings.json', dict(entry_line=Q.line_of(Q.FIND, title), append=r, title=title))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title))


def workorder():
    """### OPEN_TRAILS (one appended line): (R181)(5) -- the W-ORD-GRH-WEIL entry: EF_lit_chi landed; act seven named."""
    Q = _Q()
    wg = Q.line_of(Q.OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    h = '*Appended 2026-10-01 by b571, under the author’s ruling `(R181)`(5), to the W-ORD-GRH-WEIL entry'
    Q.guard_absent(Q.OT, h)
    a = ('\n%s (:%s) -- THE EXPLICIT FORMULA FOR χ LANDED:* SIDE-explicit-formula v0.13 = `%s` proves the χ-explicit formula for '
         'every primitive χ ≠ 1 (Chi/Main.lean), the route FullLine, Horizontal, ZeroSumLimit, FullLineAssembly, Main compiled. The next '
         'item of this work-order is act seven: the composition h2_sign_chi ⟺ GRH_chi, the χ-instance of the criterion with the χ-seam; '
         'CP-5 after it.\n' % (h, wg, V013[:7]))
    r = Q.append_to(Q.OT, a)
    put_json('b571_workorder.json', dict(line=Q.line_of(Q.OT, h), wg=wg, append=r))
    print(jl('b571_workorder.json'))


def trail():
    Q = _Q()
    S = jl('b571_scores.json')
    fj, nj, wj, cj = jl('b571_findings.json'), jl('b571_nav_clauses.json'), jl('b571_workorder.json'), jl('b571_chiff_line.json')
    head = ('### b571 — lane two, act eleven under (R181): GRH-Weil act six -- FullLine restated at χ⁻¹ with the conductor, the '
            'modules after it, the explicit formula for χ landed; the FACES_LEDGER supersession form; rowgen on non-ASCII names')
    Q.guard_absent(Q.OT, head)
    rows = ['', head, '',
            '**(R181) ratified.** (1) b570 entered at its weight, two clauses recorded as the navigator’s. (2) The FACES_LEDGER form '
            'taught to the table, the line written. (3) rowgen on Lean’s identifier set. (4) GRH-Weil act six. (5) The gates; v0.13; the '
            'next act named.', '',
            '**Entered:** FINDINGS.md:%s (the entry), :%s (the supersession line); OPEN_TRAILS.md:%s and :%s (the navigator’s two clauses, '
            'at b570’s record), :%s (the work-order line), this record; SIDE-global-section CORRESPONDENCE.md rows 426-431; '
            'SIDE-explicit-formula main = **v0.13** = `%s`, grh-weil-b571 pushed by name. Relay instrument commits: the FACES_LEDGER form '
            '`%s`, the identifier read `%s`.' % (fj['entry_line'], cj['line'], nj['lines'][0], nj['lines'][1], wj['line'], V013[:7],
                                                 INSTR['faces'], INSTR['rowgen']), '',
            '**H23a %s · H23b %s · H23c %s. (N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, '
            '(S3) %s.' % tuple(S[k][0] for k in ('H23a', 'H23b', 'H23c', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3')), '',
            '**Next:** per `(R181)`(5), with the explicit formula for χ landed: act seven, the composition h2_sign_chi ⟺ GRH_chi (the '
            'χ-instance of the criterion with the χ-seam); CP-5 after it. The author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; nothing at Zenodo written; no existing statement changed; no Zeta23 or vendored '
            'file edited or added; ERRATA untouched; FACES_LEDGER untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit '
            'left it; the four lists stay OPEN; nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own '
            'words.', '']
    r = Q.append_to(Q.OT, NL.join(rows))
    put_json('b571_trail.json', dict(line=Q.line_of(Q.OT, head), head=head, append=r))
    print(jl('b571_trail.json')['line'])


def rows():
    """### the act's row and one row per terminal of record, through relay tools/corr_row.py; `|` in a statement written `‖`."""
    import b569_record as R9
    Q = _Q()
    e = jl('b571_e0.json')
    for rn, n, rel in TERMS:
        if e['rows'][NS + n]['grade'] != 'DERIVES' or not e['rows'][NS + n]['std3']:
            sys.exit('### %s not graded at the standard three: no row' % n)
    for rn in (ROW_ACT,) + tuple(t[0] for t in TERMS):
        if [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]:
            sys.exit('### ROW %s ALREADY PRESENT' % rn)
    pr = R9.prints_axioms(rd('b571_chi_prints.txt'))
    out = []
    act = [ROW_ACT,
           '**GRH-WEIL ACT SIX** (b571, under (R181)(4)). SIDE-explicit-formula v0.13 = %s: FullLine restated at χ⁻¹ with the '
           'conductor; Horizontal, ZeroSumLimit and the assembly for χ; EF_lit_chi proved for primitive χ ≠ 1. Nothing here proves RH '
           'or GRH.' % V013[:7],
           'SIDE-explicit-formula SIDEExplicitFormula/Chi/{FullLine,Horizontal,ZeroSumLimit,FullLineAssembly,Main}.lean (v0.13 = %s)' % V013[:7],
           '%d declarations print within [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b571_chi_prints.txt)' % len(e['rows']),
           ' ; '.join('`%s` DERIVES' % t[1] for t in TERMS),
           'LANDED at v0.13 = %s; nothing deposits; nothing at Zenodo written.' % V013[:7]]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + act, capture_output=True, text=True, encoding='utf-8')
    out.append(dict(row=ROW_ACT, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    for rn, n, rel in TERMS:
        head = ' '.join(e['rows'][NS + n]['head'].split()).replace('|', '‖')
        cells = [rn, '**%s** (b571, under (R181)(4)), SIDE-explicit-formula v0.13 = %s: `%s%s %s`.' % (n, V013[:7], NS, n, head),
                 '`SIDE-explicit-formula/%s` (v0.13 = %s) : `%s%s`' % (rel, V013[:7], NS, n),
                 '\'%s%s\' depends on axioms: [%s] (relay data/b571_chi_prints.txt)' % (NS, n, ', '.join(pr.get(NS + n) or [])),
                 '`%s` DERIVES' % n,
                 'LANDED at v0.13 = %s; the E0 read on grh-weil-b571 before the merge (relay data/b571_e0.txt); domain conditions only; '
                 'absolute-value bars written ‖.' % V013[:7]]
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + cells, capture_output=True, text=True,
                           encoding='utf-8')
        out.append(dict(row=rn, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    put_json('b571_rows.json', dict(rows=out, act=act))
    print('  rows', [(o['row'], o['exit']) for o in out])


def desk():
    S = jl('b571_scores.json')
    L = ['=' * 104, 'b571 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H23a-H23c ((R181)(4)).', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H23a', 'H23b', 'H23c')]
    L += ['', '### THE NAVIGATOR`S SIX.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in
                                                        ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    nh = sum(1 for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**'
          % (nh, 6 - nh, sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD'), sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] != 'HELD')), '']
    L += rd('b571_defects.txt').rstrip(NL).split(NL)
    put_txt('b571_desk_notes.txt', L)


def components():
    S = jl('b571_scores.json')
    fj, tj, rj, nj, wj, cj = (jl('b571_findings.json'), jl('b571_trail.json'), jl('b571_rows.json'), jl('b571_nav_clauses.json'),
                              jl('b571_workorder.json'), jl('b571_chiff_line.json'))
    L = ['b571 -- THE COMPONENTS, BANKED UNDER (R181).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b570`s push-out banks relay 96daad63 ; push-b570 branches deleted by name '
         '(data/b571_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : the FACES_LEDGER form relay %s (10 of 10) ; the ch_iff_rh line FINDINGS :%s, CONFLICT %d before and after '
         '(data/b571_chiff.txt) ; the identifier read relay %s (9 of 9) ; rows 421-425 (data/b571_rows570.txt) ; the navigator`s two clauses '
         'OPEN_TRAILS :%s :%s' % (INSTR['faces'], cj['line'], S['counts']['conflict'], INSTR['rowgen'], nj['lines'][0], nj['lines'][1]),
         '### COMPONENT 2 : FullLine for χ, statements first (data/b571_fullline_statements.txt), built ; H23a %s' % S['H23a'][0],
         '### COMPONENT 3 : the module list first (data/b571_module_list.txt) ; Horizontal, ZeroSumLimit, FullLineAssembly, Main built ; '
         'EF_lit_chi landed (EF_lit_chi_holds) ; H23b %s ; H23c %s ; v0.13 = %s by push_gated.sh ; grh-weil-b571 pushed, no held branch'
         % (S['H23b'][0], S['H23c'][0], V013[:7]),
         '### COMPONENT 4 : FINDINGS :%s ; OPEN_TRAILS :%s (the work-order), :%s (the record) ; CORRESPONDENCE rows %s ; the page '
         'unchanged (no node changed) ; next: act seven, h2_sign_chi ⟺ GRH_chi, CP-5 after it'
         % (fj['entry_line'], wj['line'], tj['line'], ', '.join('%s (exit %d)' % (o['row'], o['exit']) for o in rj['rows']))]
    put_txt('b571_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b571_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
