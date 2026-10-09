# -*- coding: utf-8 -*-
"""b643_record.py -- THE ACT'S RECORD TOOL, UNDER (R253). ### ONE SUBCOMMAND PER BANK.

### ### b643: LANE THREE, ACT SEVENTY -- THE TWO READERS REPAIRED AND RERUN; THE PAGES RE-EMITTED AT v0.26; THE KEYSTONE CENSUS AT v0.7; THE
### PI-0-1 FORM READ AT SOURCE; THE SECOND READER. Subcommands write only `data/b643_*` unless the docstring names another file; `dry` routes
### WRITES to the scratchpad. The generic helpers are b602's, b633's, b641's and b642's record tools', imported; ledger appends through b566's
### guarded `append_to`. Lean runs are the seat's, detached under the watchdog; this tool generates their files and reads their logs.
"""
import collections
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b641_record as R41  # noqa: E402
import b643_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = 'e594f88a-2fab-4757-943d-7ab1bc3de815'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b643_registration_2026-10-08.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
_write, _scan, _clean = R3._write, R3._scan, R3._clean
lines_of, _nd, predict_cells, _land = R3.lines_of, R3._nd, R3.predict_cells, R3._land
kern_state, sorry_tokens = R3.kern_state, R3.sorry_tokens
KERNS_READ = R41.KERNS_READ
_poss = R41._poss
OUTSIDE_NEEDLES = R41.OAI_NEEDLES     # ### (R253)(5)(f): no line naming an outside collection; b641's needles carried
STD3 = '[propext, Classical.choice, Quot.sound]'


def put_txt(name, L):
    _write(os.path.join(SP if DRY else D, name), (NL.join(L) + NL).encode('utf-8'))


def put_json(name, j):
    _write(os.path.join(SP if DRY else D, name), (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    try:
        return io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '')
    except OSError:
        return ''


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b643_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b643 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b643_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b643_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


# ================================================================================ READING (1): THE READS
MATHLIB = K.EF + '/.lake/packages/mathlib'


def READS():
    return [
        ('relay data/b642_grades.txt: the WithTop note', RELAY, PRE_RELAY, 'data/b642_grades.txt', ('GREP', r'WithTop|contDiff_riemannZeta₀'), 300),
        ('relay data/b642_table.txt: the three primed names', RELAY, PRE_RELAY, 'data/b642_table.txt', ('GREP', r"(dedekind_rhs|TrivialSummandPremise|trivialSummandPremise'_witness)' |grades differing"), 300),
        ('relay data/b642_nonvacuity.txt: the counts and the class lines', RELAY, PRE_RELAY, 'data/b642_nonvacuity.txt',
         ('GREP', r'^WITNESSED \d+ ;|^  (WITNESSED|UNWITNESSED) / '), 200),
        ('relay data/b641_premise_status.txt: the heads by status, the figure line', RELAY, PRE_RELAY, 'data/b641_premise_status.txt',
         ('GREP', r'^### ### \*\*(HEADS|DISCHARGED|OPEN|CITED|WITNESSED|DOMAIN) |REFUTED-BY-COMPUTATION'), 260),
        ('relay data/b642_defects.txt: defects (a), (h), (i), (k)', RELAY, PRE_RELAY, 'data/b642_defects.txt', ('GREP', r'^    \((a|h|i|k)\) '), 600),
        ('relay tools/e0_rule.py before the repair: the binder classes, the lexicon and the typing`s fall-through', RELAY, PRE_RELAY, 'tools/e0_rule.py',
         ('GREP', r'^CLASSES = |^OUTCOME_OF|^LEXICON = |^def _lex|^def typing|UNLEXED|^SORT_ATOMS|^def binders_of|^def grade'), 220),
        ('relay tools/terminal_table.py: the textual reader', RELAY, PRE_RELAY, 'tools/terminal_table.py',
         ('GREP', r'^ID_FIRST|^ID_REST|^NAME_RE|^def statement|B378\.decl_re|B378\.declares|import b378_terminals'), 220),
        ('relay tools/b378_terminals.py before the repair: the declaration pattern', RELAY, PRE_RELAY, 'tools/b378_terminals.py',
         ('GREP', r'^KEYWORD = |^LEAD = |^def decl_re|re\.escape\(last\) \+'), 220),
        ('relay tools/chain_page.py: corr_select and the table it reads', RELAY, PRE_RELAY, 'tools/chain_page.py',
         ('GREP', r'^def corr_select|pick = lambda|return sorted\(set\(n for n, r in rec|^def record_rows|HEAD:data/terminal_table\.json|^CHI_PREFIX|^SCHEMA_PREFIX'), 220),
        ('relay data/b638_nodes_zeta.txt: its pin line', RELAY, PRE_RELAY, 'data/b638_nodes_zeta.txt', ('GREP', r'^# pin'), 220),
        ('relay data/b638_nodes_chi.txt: its pin line', RELAY, PRE_RELAY, 'data/b638_nodes_chi.txt', ('GREP', r'^# pin'), 220),
        ('relay tools/act_root.py: the census path (a reader of the census`s kernel column, not a generator)', RELAY, PRE_RELAY, 'tools/act_root.py',
         ('GREP', r'^CENSUS = |^def census_kernels|census_kernels\(rev\)'), 220),
        ('relay tools/b638_record.py: the edition generator that wrote v0.6', RELAY, PRE_RELAY, 'tools/b638_record.py',
         ('GREP', r'^def edition|^def census\(|^def _edition|glossary_block\('), 200),
        ('relay tools/b634_elab.py: the elaborated reader -- it prints types, no dependency', RELAY, PRE_RELAY, 'tools/b634_elab.py',
         ('GREP', r'^def gen|^def parse|b634Dump|getUsedConstants|BINDER |CONCL '), 200),
        ('the census at v0.6: its headings', PP, PRE_PP, K.CEN6, ('GREP', r'^#{1,3} '), 200),
        ('relay data/glossary.txt', RELAY, PRE_RELAY, 'data/glossary.txt', ('GREP', r'.'), 260),
        ('OPEN_TRAILS: the work-orders of b641, the squeeze, the Epstein price, b642`s record and correction', PP, PRE_PP, 'OPEN_TRAILS.md',
         list(K.OT_WORKORDERS) + [K.OT_SQUEEZE, K.OT_EPSTEIN, K.B642_RECORD, K.B642_CORRECTION], 700),
        ('FINDINGS: b642`s entry and its weight line beneath b641`s', PP, PRE_PP, 'FINDINGS.md', [K.B642_WEIGHT_LINE, K.B642_ENTRY], 400),
        ('relay data/b642_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b642_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    L = ['b643 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)] if isinstance(sel, tuple) else \
            [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### SIDE-explicit-formula main %s ; %s peeled %s' % (g(K.EF, 'rev-parse', 'main').strip()[:12], K.EF_TAG,
                                                               g(K.EF, 'rev-parse', K.EF_TAG + '^{commit}').strip()[:12]),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b643_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()), len(L)))


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R253) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b643 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % (n, DATE), '']
    for i, cid, inp in since:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    if not since:
        L.append('### NONE: no prompt has been put to the author in this act.')
    put_txt('b643_author_answers.txt', L)
    print('  prompts banked: %d' % n)


def answer_of(k):
    R3.rd = lambda name: rd('b643_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b643_kernels_face.json', dict(at=utc(), kernels=kern_state(list(KERNS_READ))))


# ================================================================================ COMPONENT 0: THE TWO REPAIRS, BANKED
def repairs(*a):
    """data/b643_repairs.txt: each repair`s commit by its files alone, its planted test`s cases before the edit (the scratchpad`s runs) and
    after (the step-zero bank), and contDiff_riemannZeta₀ and the three primed rows read by the repaired rule and reader."""
    import e0_rule as E
    import terminal_table as TT
    j = jl('b643_tests_stepzero.json')
    pre = json.load(io.open(os.path.join(SP, 'b643_tests_prerepair.json'), encoding='utf-8'))
    L = ['b643 -- COMPONENT 0, (R253)(3): THE TWO READER REPAIRS, EACH WITH ITS PLANTED TEST, EACH COMMITTED ALONE (%s)' % utc(), '']
    for c, tool, test in ((K.E0_COMMIT, K.E0_TOOL, K.E0_TEST), (K.B378_COMMIT, K.B378_TOOL, K.B378_TEST)):
        files = sorted(x for x in g(RELAY, 'show', '--name-only', '--format=', c).split(NL) if x.strip())
        tn = os.path.basename(test)
        bp =os.path.join(SP, tn.replace('.py', '_before.txt'))
        before = io.open(bp, encoding='utf-8').read() if os.path.exists(bp) else ''
        L += ['### relay %s : %s ; alone with its test %s' % (c, ', '.join(files), files == sorted([tool, test])),
              '    before the edit : %s' % ([l for l in before.split(NL) if 'cases as wanted' in l] or ['### NOT READ'])[0],
              '    after the edit  : %s' % ((j.get(tn) or {}).get('last') or '### NOT RUN')]
        L += ['    ' + l for l in (j.get(tn) or {}).get('output', '').rstrip(NL).split(NL)]
        L.append('    the test files the repaired module`s own tests ran after it: %s' % ', '.join(
            '%s %s/%s' % (n, (j.get(n) or {}).get('passing'), (j.get(n) or {}).get('cases')) for n in (
                ('test_e0_rule.py', 'test_e0_existential.py', 'test_premise_status.py') if c == K.E0_COMMIT else
                ('test_terminal_table_b630.py', 'test_terminal_table_b635.py', 'test_terminal_table_b636.py', 'test_terminal_table_b637.py',
                 'test_name_patterns_b636.py', 'test_row_sort.py', 'test_rowgen_ident.py'))))
        L.append('')
    hd = '{n : WithTop ℕ∞} : ContDiff ℂ n riemannZeta₀'
    L += ['### contDiff_riemannZeta₀ by the repaired rule: the binder n : WithTop ℕ∞ types %s (%s) ; the grade %s (b642 read INTERFACES)' % (
        E.typing('WithTop ℕ∞')[0], E.typing('WithTop ℕ∞')[1], E.grade(hd, 'theorem')[0])]
    for n in ("SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'", "SIDEExplicitFormula.Schema.Dedekind.TrivialSummandPremise'",
              "SIDEExplicitFormula.SaltCheckNonvacuity.trivialSummandPremise'_witness'"):
        st = TT.statement(K.EF, 'main', n)
        L.append('### %s by the repaired reader: %s' % (n, ('RESOLVED in %s : %s' % (st['file'], ' '.join(st['text'].split())[:160])) if st else 'UNRESOLVED'))
    L += ['', '### the step-zero tests before the repairs (the scratchpad`s copy of the runner bank): not clean %s' % sorted(
        n for n, x in pre.items() if x['rc'] != 0 or x['failing'])]
    put_txt('b643_repairs.txt', L)
    print(NL.join(L[-6:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R253)(1) AND (2)
W_HEAD = '*Appended 2026-10-08 by b643 to b642’s entry (:%d), under `(R253)`(1) -- b642 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
WS_HEAD = ('*Appended 2026-10-08 by b643, under `(R253)`(2) -- W-ORD-WATCHDOG-STOP, ENTERED AND PRICED, NOT ACTED, TRIGGER A SECOND ACT WITH LOWS '
           'BENEATH THE HOLD:*')
J_HEAD = ('*Appended 2026-10-08 by b643 beneath b642’s squeeze correction (:%d), under `(R253)`(1) -- THE NAVIGATOR’S DEFECT (j), AS THE SEAT '
          'RECORDED IT:*')


def _weight():
    S, A, NV = jl('b642_scores.json'), jl('b642_act_root.json'), rd('b642_nonvacuity.txt')
    pre = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)', rd('b642_checks.txt'))
    post = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)', rd('b642_checks_postpush.txt'))
    nv = re.search(r'^WITNESSED (\d+) ; UNWITNESSED (\d+) ; total (\d+)', NV, re.M)
    dg = re.search(r'^  WITNESSED / DEGENERATE: (\d+)', NV, re.M)
    dm = re.search(r'TOTAL: (\d+) prints over the four modules; beyond the standard three or sorryAx: (\d+)', rd('b642_declarations.txt'))
    tb = re.search(r'added (\d+) ; gone (\d+) ; moved (\d+) ; grade moved (\d+)', rd('b642_table.txt'))
    nd = len(json.load(io.open(os.path.join(D, 'b642_defects.json'), encoding='utf-8')).get('defects') or [])
    kp = re.search(r'push_gated: tag v0\.26 peeled local (\w+) remote (\w+)', rd('b642_kernel_push_out.txt'))
    sc = lambda k: (S.get(k) or ['?'])[0]   # noqa: E731
    return ('\n%s SIDE-explicit-formula v0.26 = %s, main, the branch and the tag equal and read back at the remote. N1 %s: the five '
            'declarations DERIVES at the standard three, %s prints over four modules, beyond the three or sorryAx %s. N2 %s -- every clause held '
            'but the gate`s reading of dedekind_rhs\' (PREDICATE-UNLISTED, (R243)(2)); the two refutations compiled by other witnesses than '
            'b641 computed (the box of half-width 1/2; the point mass at log 2), each a refutation of the premise as stated (defect (h)). N3 %s: '
            '%s heads, %s WITNESSED (%s of them DEGENERATE) and %s UNWITNESSED with a reason. N4 %s: the table added %s rows, gone %s, moved %s, '
            'grade moved %s. N5 %s. The suite %s of %s pre-push and %s of %s post-push, G-CHAIN-PAGE and G-CHAIN-PAGE-CHI failing in their letter '
            '(defect (k): Component 5 read b641`s table at relay HEAD; with the v0.26 table a cell moves on both pages); nothing relabelled. '
            'Defects (a)-(l), %d, as the seat listed them. The root %s… over %d repositories, %d tags and %d banks. Nothing deposited.\n' % (
                W_HEAD % K.B642_ENTRY, (kp.group(2) if kp and kp.group(1) == kp.group(2) else '?')[:7], sc('N1'), dm.group(1) if dm else '?',
                dm.group(2) if dm else '?', sc('N2'), sc('N3'), nv.group(3) if nv else '?', nv.group(1) if nv else '?', dg.group(1) if dg else '?',
                nv.group(2) if nv else '?', sc('N4'), tb.group(1) if tb else '?', tb.group(2) if tb else '?', tb.group(3) if tb else '?',
                tb.group(4) if tb else '?', sc('N5'), pre.group(2) if pre else '?', pre.group(1) if pre else '?', post.group(2) if post else '?',
                post.group(1) if post else '?', nd, (A.get('root') or '?')[:16], len((A.get('reads') or {}).get('heads') or []),
                len((A.get('reads') or {}).get('tags') or []), len((A.get('reads') or {}).get('banks') or [])))


def _watchdog_text():
    return ('\n%s a detached run whose watchdog samples free memory beneath the 2,560 MB hold is stopped, its stop logged with the reading, '
            'and retried once the host is freed above the hold; the hold now gates the start alone (b642 read lows down to 1919 MB inside runs '
            'started above it, none stopped, relay data/b642_defects.txt (a)). Priced by the seat: one act -- the watchdog (build1.py, carried '
            'into each act`s scratchpad) gains the stop and the retry, with a test planting a low sample (expected: the run stopped and retried) '
            'and a high one (expected: untouched). Until it is acted, every act prints the watchdog`s lows per run for every detached run, the '
            'reader`s runs among them. Trigger: a second act with lows beneath the hold.\n' % WS_HEAD)


def _j_text():
    return ('\n%s (R252)(5) wrote `:2485 at 3635e748` for ZetaZeroFree; :2485 is the line in SIDE-explicit-formula`s vendored copy at 8c51431, '
            'and at 3635e748 the lemma is at :2457 -- read at b642 by git show at both commits, the statement byte-identical at the two lines, and '
            'recorded beneath (R251)(7)’s block with the source line (relay data/b642_reads.txt; data/b642_defects.txt (j)). The defect is the '
            'navigator`s and stands as recorded; no line is edited.\n' % (J_HEAD % K.OT_SQUEEZE))


def record_lines(*a):
    """### Component 1, (R253)(1)-(2): FINDINGS, b642 at its weight (to :7965); OPEN_TRAILS, W-ORD-WATCHDOG-STOP and the defect (j) line."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## SIDE-explicit-formula v0.26: Keiper')
    if entry != K.B642_ENTRY:
        sys.exit('### b642`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B642_ENTRY, _poss(_weight())), ('OPEN_TRAILS.md', WS_HEAD, _poss(_watchdog_text())),
             ('OPEN_TRAILS.md', J_HEAD % K.OT_SQUEEZE, _poss(_j_text()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT', 'None') if x in allt]
    outside = [n for n in OUTSIDE_NEEDLES if n in allt]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks: %s ; unread figures: %s ; outside names: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or unread or outside:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS, AN UNREAD FIGURE OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    _land(Q, items, 'b643_record_lines.json', K.B642_ENTRY)


# ================================================================================ COMPONENT 2: THE RERUN, (R253)(3)
# ### b634's reader, imported and not copied, given two kernel entries of this act's: SIDE-explicit-formula at v0.26 (the table's rows of that
# ### kernel now include v0.26's) and SIDE-structural-error-correction at b636's pin; their run and types banks are b643's, so no prior bank is
# ### written. The driver (elab_drive) is launched by the seat as a detached process; it runs one module per lean call, the hold read before each.
ELAB = {'ef': ('b643-ef', dict(KERNEL='SIDE-explicit-formula', KER=K.EF, KER_PIN=K.EF_PIN, KER_TAG=K.EF_TAG,
                                ROOTS=('SIDEExplicitFormula/', 'Zeta23/', 'Vendored/Bulka/'), RUNS='b643_elab_ef_runs.json', TYPES='b643_elab_ef.txt',
                                WORK=os.path.join(SP, 'b643_elab_ef'), ACT='b643')),
        'sec': ('b643-sec', dict(KERNEL='SIDE-structural-error-correction', KER=K.SEC, KER_PIN=K.SEC_PIN, KER_TAG='v0.2.2',
                                 ROOTS=('SIDEStructuralErrorCorrection/',), RUNS='b643_elab_sec_runs.json', TYPES='b643_elab_sec.txt',
                                 WORK=os.path.join(SP, 'b643_elab_sec'), ACT='b643'))}


def _elab_use(which):
    import b634_elab as EL
    key, entry = ELAB[which]
    EL.KERNELS[key] = entry
    EL.use(key)
    return EL


def elab_plan(which='ef', *a):
    EL = _elab_use(which)
    calls, missing, via, n = EL.plan()
    print('  %s: rows %d ; calls %d ; named by no module %s ; by grep %d' % (which, n, len(calls), missing, len(via)))


def elab_drive(which='ef', *a):
    """the detached driver: b634_elab.run then join under this act`s kernel entry; its last line `### EXIT <rc>`."""
    EL = _elab_use(which)
    rc = EL.run()
    if rc == 0:
        EL.join()
    print('### EXIT %d %s' % (rc, utc()), flush=True)


def elab_resolve(which='ef', *a):
    """the detached second pass: b634_elab.resolve_missing then join, under this act`s kernel entry; its last line `### EXIT <rc>`."""
    EL = _elab_use(which)
    rc = EL.resolve_missing()
    if rc == 0:
        EL.join()
    print('### EXIT %d %s' % (rc, utc()), flush=True)


def _rows_state(rows):
    out = {}
    for r in rows:
        out.setdefault((r['repo'], r['name']), (r['grade'], r.get('provenance'), r.get('mark') or '', r.get('kind') or ''))
    return out


def _grade_of(E, e):
    import b634_record as R34
    try:
        return E.grade(R34._elab_header(e), 'theorem' if e['kind'] == 'theorem' else 'def')[0]
    except Exception as x:
        return 'UNCLASSED (%s)' % type(x).__name__


def _binder_classes(E, e):
    import b634_record as R34
    try:
        bs = E.binders_of(E.statement_only(R34._elab_header(e)))
        return '; '.join('%s : %s -> %s %s/%s' % (b['name'], b['type'][:40], b['typing'], b['cls'], b['outcome']) for b in bs
                         if b['kind'] != 'existential')
    except Exception as x:
        return 'UNREAD (%s)' % type(x).__name__


def rerun(*a):
    """data/b643_rerun.txt: (1) every name of the two kernels` elaborated banks at this act graded by the rule before the repairs (relay
    PRE_RELAY`s e0_rule.py) and after (the live rule), every move printed with its binders` classes, the reader named; (2) the three primed rows
    by the textual reader; (3) the terminal table regenerated (tools/terminal_table.py) and diffed by row against b642`s committed table, every
    row added, gone or moved printed. Writes data/terminal_table.* (the table`s own files) and this bank."""
    import b634_elab as EL
    import b626_record as R26
    import e0_rule as E
    import terminal_table as TT
    E_old = R26.e0_module(K.PRE_RELAY)
    L = ['b643 -- COMPONENT 2, (R253)(3): THE RERUN UNDER THE REPAIRED READERS (%s)' % utc(), '',
         '### the rule before the repairs: relay %s tools/e0_rule.py ; after: relay HEAD %s (%s alone with its test)' % (
             K.PRE_RELAY, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), K.E0_COMMIT), '']
    moves_all = []
    for which in ('ef', 'sec'):
        key, entry = ELAB[which]
        p = os.path.join(D, entry['TYPES'])
        B = EL.parse(io.open(p, encoding='utf-8').read()) if os.path.exists(p) else {}
        runs = json.load(io.open(os.path.join(D, entry['RUNS']), encoding='utf-8')) if os.path.exists(os.path.join(D, entry['RUNS'])) else {}
        calls = [c for c in runs.get('calls') or [] if not c.get('superseded')]
        lows = [c.get('low') for c in calls if c.get('low') is not None]
        typed = {n: e for n, e in B.items() if not e.get('missing')}
        moves = []
        for n, e in sorted(typed.items()):
            a_, b_ = _grade_of(E_old, e), _grade_of(E, e)
            if a_ != b_:
                moves.append((n, a_, b_, _binder_classes(E, e)))
        moves_all += [(entry['KERNEL'],) + m for m in moves]
        L += ['### THE ELABORATED READER, %s at %s = %s (data/%s, its calls in data/%s)' % (entry['KERNEL'], entry['KER_TAG'], entry['KER_PIN'],
                                                                                         entry['TYPES'], entry['RUNS']),
              '    names typed %d ; missing %d ; calls %d, exit 0 %d ; the watchdog`s lows per call: lowest %s MB, beneath the hold in %d of %d '
              'calls' % (len(typed), len(B) - len(typed), len(calls), sum(1 for c in calls if c.get('rc') == 0), min(lows) if lows else '-',
                         sum(1 for x in lows if x < 2560), len(lows)),
              '    every call`s low: %s' % ', '.join('%s %s' % (c['module'].split('/')[-1], c.get('low')) for c in calls),
              '    ### GRADE MOVES UNDER THE REPAIRED RULE (reader: elaborated): %d' % len(moves)]
        L += ['      %s : %s -> %s ; binders: %s' % m for m in moves]
        L.append('')
    L.append('### THE TEXTUAL READER (tools/terminal_table.py through b378_terminals.decl_re, %s) OVER THE THREE PRIMED ROWS:' % K.B378_COMMIT)
    for n in ("SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'", "SIDEExplicitFormula.Schema.Dedekind.TrivialSummandPremise'",
              "SIDEExplicitFormula.SaltCheckNonvacuity.trivialSummandPremise'_witness'"):
        st = TT.statement(K.EF, 'main', n)
        L.append('    %s : %s' % (n, ('RESOLVED in %s' % st['file']) if st else 'UNRESOLVED'))
    before = _rows_state(json.loads(_show(RELAY, K.PRE_RELAY, 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    rows1 = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']
    after = _rows_state(rows1)
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    gm = [k for k in moved if before[k][0] != after[k][0]]
    L += ['', '### THE TERMINAL TABLE REGENERATED (exit %d) AGAINST b642`S COMMITTED TABLE (relay %s), BY ROW: rows %d -> %d ; added %d ; gone %d ; '
          'moved %d ; grade moved %d' % (r.returncode, K.PRE_RELAY, len(before), len(rows1), len(added), len(gone), len(moved), len(gm))]
    L += ['  + %s %s %s' % (k[0], k[1], after[k]) for k in added] + ['  - %s %s %s' % (k[0], k[1], before[k]) for k in gone]
    L += ['  ~ %s %s %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved]
    L += ['', '### ### **ELABORATED GRADE MOVES %d ; TABLE ROWS MOVED %d (GRADE MOVED %d) ; ADDED %d ; GONE %d.**' % (
        len(moves_all), len(moved), len(gm), len(added), len(gone))]
    put_txt('b643_rerun.txt', L)
    put_json('b643_rerun.json', dict(at=utc(), moves=[list(m) for m in moves_all], table=dict(moved=[list(k) for k in moved], grade_moved=[list(k) for k in gm],
                                                                                              added=[list(k) for k in added], gone=[list(k) for k in gone])))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE PAGES AT v0.26, (R253)(4)
def _corr_rows(text):
    i = text.find('\n## Correspondence')
    return re.findall(r'^\| `([^`]+)`', text[i:], re.M) if i >= 0 else []


def _kind(l):
    if l.startswith('| `'):
        return 'a Correspondence or Placement row'
    if l.startswith('- **'):
        return 'a glossary line'
    if re.match(r'^\d+\. |^- `|^`', l):
        return 'a node line'
    if l.startswith('#'):
        return 'a heading'
    return 'other'


def page(k, *a):
    """the page `k` (zeta | chi) at v0.26: the fresh probe`s output (the seat`s detached run, the scratchpad`s b643_probe_<k>/) banked as
    data/b643_probe_out_<k>.txt; the page re-emitted from that bank (no lean call) and checked equal to the run`s own page; diffed by kind
    against PLACE-papers HEAD, the Correspondence rows counted before and after; written to PLACE-papers when its bytes differ (never under
    `dry`); data/b643_page_<k>.json."""
    import difflib
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    src = os.path.join(SP, 'b643_probe_%s' % k, 'chain_page_probe_out.txt')
    gen = os.path.join(SP, 'b643_page_%s_gen.md' % k)
    if not os.path.exists(src) or not os.path.exists(gen):
        sys.exit('### THE PROBE OUTPUT OR THE RUN`S PAGE IS ABSENT -- NOTHING WRITTEN')
    pb = open(src, 'rb').read()
    _write(os.path.join(SP if DRY else D, K.PROBE[k]), pb)
    rc, pg, _meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b643_%s' % k), src)
    if rc:
        sys.exit('### %s RE-EMIT FROM THE BANKED PROBE FAILED, exit %d %s' % (k, rc, log[-2:]))
    b = pg.encode('utf-8')
    same_run = b == open(gen, 'rb').read()
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    pt = prev.decode('utf-8')
    changed = prev != b
    dl = [x for x in difflib.unified_diff(pt.split(NL), pg.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    kinds = collections.Counter('%s %s' % ('added' if x[0] == '+' else 'removed', _kind(x[1:])) for x in dl)
    # ### the Correspondence counted before the act (PLACE-papers PRE_PP), not before this call: a re-emission after Component 6 reads HEAD
    # ### as already v0.26, and the before-and-after the author ordered printed is the act`s; the HEAD count is kept beside it.
    pre = R2.cr0(subprocess.run(['git', '-C', PP, 'show', K.PRE_PP + ':' + K.PNAME[k]], capture_output=True).stdout).decode('utf-8')
    c0, c1, ch0 = _corr_rows(pre), _corr_rows(pg), _corr_rows(pt)
    gl0 = [l for l in pt.split(NL) if l.startswith('- **')]
    gl1 = [l for l in pg.split(NL) if l.startswith('- **')]
    if changed and not DRY and same_run:
        _write(os.path.join(PP, K.PNAME[k]), b)
    put_json('b643_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), probe_sha256=sha(pb), same_as_run=same_run,
                                           changed=changed, written=bool(changed and not DRY and same_run), kinds=dict(kinds),
                                           corr_before=len(c0), corr_after=len(c1), corr_added=sorted(set(c1) - set(c0)),
                                           corr_removed=sorted(set(c0) - set(c1)), corr_at=K.PRE_PP, corr_head_before=len(ch0),
                                           glossary_before=len(gl0), glossary_after=len(gl1),
                                           diff=dl, free_mb_before=fm, at=utc()))
    print('  %s : exit %d ; equal to the run`s page %s ; changed against HEAD %s ; Correspondence %d -> %d (+%d, -%d) ; glossary lines %d -> %d' % (
        k, rc, same_run, changed, len(c0), len(c1), len(set(c1) - set(c0)), len(set(c0) - set(c1)), len(gl0), len(gl1)))
    for kk, n in sorted(kinds.items()):
        print('      %-50s %d' % (kk, n))


def page_arms(*a):
    """the page arms (G-CHAIN-PAGE, G-CHAIN-PAGE-CHI) on this act`s lists and probes against PLACE-papers HEAD, and the frozen control
    (test_chain_page_b596) at its relay pin; data/b643_page_arms.txt."""
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b643 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b643_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; first differing line %s' % (arm, 'PASS' if r['ok'] else 'FAIL', K.NODES[k], r['rc'],
                                                                                         r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    save = CP.E0
    CP.E0 = R26.e0_module(TC.RELAY_PIN)
    try:
        c = TC.control()
    finally:
        CP.E0 = save
    for x in c:
        L.append('    %s (E0 at %s) %s : %s -- exit %d' % (TC.ARM, TC.RELAY_PIN, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b643_page_arms.txt', L)
    print(NL.join(l[:200] for l in L))


# ================================================================================ COMPONENT 4: THE DEPENDENCY PRINT, (R253)(5)(b)
# ### The elaborated reader prints types and no dependency (relay tools/b634_elab.py, data/b643_reads.txt); the print it would need is this one.
# ### Per kernel, one lean call per TOP module (a built module no other module of the kernel imports), each importing that module alone: the
# ### environment then holds every kernel module beneath it, and the call prints, for every constant of every kernel module loaded, the kernel
# ### constants and the head names its type (T) and its value (V) use. Nothing is read from text; the module list and the import graph are read
# ### from the kernel's tree at HEAD to choose the tops, the constants from the environment.
DEP_KERNELS = ['SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-carrier-spec',
               'SIDE-structural-error-correction', 'SIDE-rcurve', 'SIDE-grh-transfer']
DOMAIN_HEADS = ('AnalyticOnNhd', 'Continuous', 'EqOn', 'HasCompactSupport', 'HasDerivAt', 'Integrable', 'IsOpen', 'IsRoot', 'Monotone', 'Prime',
                'StrictMono', 'Tendsto')
DEPS_WORK = os.path.join(SP, 'b643_deps')
DEPS_RUNS = os.path.join(D, 'b643_deps_runs.json')


def _kernel_modules(k):
    """(mode, {module: path}, {module: [kernel imports]}) for kernel k at HEAD, the built modules only."""
    d = 'D:/' + k
    lake = os.path.isdir(os.path.join(d, '.lake', 'build', 'lib', 'lean'))
    bdir = os.path.join(d, '.lake', 'build', 'lib', 'lean') if lake else os.path.join(d, 'build')
    built = set()
    for r, _ds, fs in os.walk(bdir):
        for f in fs:
            if f.endswith('.olean'):
                built.add(os.path.relpath(os.path.join(r, f), bdir)[:-6].replace(os.sep, '.'))
    mods = {}
    for f in g(d, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL):
        f = f.strip()
        if not f.endswith('.lean'):
            continue
        p = f[len('Vendored/Bulka/'):] if f.startswith('Vendored/Bulka/') else f
        m = p[:-5].replace('/', '.')
        if m not in built and not lake:
            m = os.path.basename(p)[:-5]       # ### SIDE-global-section: build/<Module>.olean, flat names, sources under Core/ etc.
        if m in built:
            mods[m] = f
    imp = {}
    for m, f in mods.items():
        t = _show(d, 'HEAD', f) or ''
        imp[m] = [x for x in re.findall(r'^import (\S+)', t, re.M) if x in mods]
    return ('lake' if lake else 'leanpath'), mods, imp


def _tops(imp):
    imported = set(x for v in imp.values() for x in v)
    return sorted(m for m in imp if m not in imported)


DEPS_PRELUDE = r'''import Lean
open Lean Meta

def b643Kind : ConstantInfo → String
  | .thmInfo _ => "theorem"
  | .defnInfo _ => "def"
  | .axiomInfo _ => "axiom"
  | .opaqueInfo _ => "opaque"
  | .inductInfo _ => "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"
  | .quotInfo _ => "quot"

def b643Keep (env : Environment) (kmods : Array Name) (hs : Array String) (c : Name) : Bool :=
  (match env.getModuleIdxFor? c with
   | some i => kmods.contains (env.header.moduleNames[i.toNat]!)
   | none => false) ||
  (match c with
   | .str _ s => hs.contains s
   | _ => false)

def b643Val : ConstantInfo → Option Expr
  | .thmInfo v => some v.value
  | .defnInfo v => some v.value
  | .opaqueInfo v => some v.value
  | _ => none

def b643Join (xs : Array Name) : String := " ".intercalate (xs.toList.map toString)
'''


def _deps_file(top, kmods, path):
    lines = ['import %s' % top] + DEPS_PRELUDE.split(NL)
    lines.append('def b643Mods : Array Name := #[%s]' % ', '.join('`' + '.'.join('«%s»' % p for p in m.split('.')) for m in kmods))
    lines.append('def b643Heads : Array String := #[%s]' % ', '.join('"%s"' % h for h in DOMAIN_HEADS))
    lines += ['#eval show MetaM Unit from do',
              '  let env ← getEnv',
              '  for m in b643Mods do',
              '    match env.getModuleIdx? m with',
              '    | none => pure ()',
              '    | some i =>',
              '      for n in (env.header.moduleData[i.toNat]!).constNames do',
              '        match env.find? n with',
              '        | none => pure ()',
              '        | some ci =>',
              '          let t := ci.type.getUsedConstants.filter (b643Keep env b643Mods b643Heads)',
              '          let v := match b643Val ci with',
              '            | some e => e.getUsedConstants.filter (b643Keep env b643Mods b643Heads)',
              '            | none => #[]',
              '          IO.println s!"DEP\\t{n}\\t{b643Kind ci}\\t{m}\\tT\\t{b643Join t}\\tV\\t{b643Join v}"',
              '']
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline=NL).write(NL.join(lines))
    return path


def deps_plan(*a):
    for k in DEP_KERNELS:
        mode, mods, imp = _kernel_modules(k)
        tops = _tops(imp)
        print('  %-34s %-8s modules %3d ; tops %3d : %s' % (k, mode, len(mods), len(tops), ', '.join(tops[:8]) + (' ...' if len(tops) > 8 else '')))


def _deps_runs():
    return json.load(io.open(DEPS_RUNS, encoding='utf-8')) if os.path.exists(DEPS_RUNS) else dict(calls=[])


def deps_drive(*a):
    """the detached driver: every kernel`s tops, one lean call each, the hold read before each (waiting beneath it, stopping after ten minutes
    beneath it), the free memory sampled during each and the lowest kept; data/b643_deps_runs.json written as each call lands."""
    import time
    import b634_elab as EL
    J = _deps_runs()
    done = set((c['kernel'], c['top']) for c in J['calls'] if c.get('rc') == 0)
    only = [x for x in a if x in DEP_KERNELS]
    for k in (only or DEP_KERNELS):
        mode, mods, imp = _kernel_modules(k)
        kmods = sorted(mods)
        for i, top in enumerate(_tops(imp), 1):
            if (k, top) in done:
                continue
            fm, waited = EL.free_mb(), 0
            while 0 <= fm < 2560 and waited < 600:
                print('  %s %s: free %d MB beneath the hold -- waiting' % (k, top, fm), flush=True)
                time.sleep(30)
                waited += 30
                fm = EL.free_mb()
            if 0 <= fm < 2560:
                J['stopped'] = 'beneath the hold for ten minutes before %s %s' % (k, top)
                _put_deps_runs(J)
                print('### STOPPED: %s' % J['stopped'], flush=True)
                print('### EXIT 3', flush=True)
                return
            tag = '%s__%03d_%s' % (k, i, re.sub(r'[^A-Za-z0-9]+', '_', top))
            src = _deps_file(top, kmods, os.path.join(DEPS_WORK, tag + '.lean'))
            out = os.path.join(DEPS_WORK, tag + '.out')
            cmd = ['lake', 'env', 'lean', src.replace('/', os.sep)] if mode == 'lake' else ['lean', src.replace('/', os.sep)]
            env = dict(os.environ, LEAN_PATH='build') if mode == 'leanpath' else dict(os.environ)
            t0, low = time.time(), fm
            with open(out, 'wb') as fo:
                p = subprocess.Popen(cmd, cwd='D:/' + k, stdout=fo, stderr=subprocess.STDOUT, env=env)
                while p.poll() is None:
                    time.sleep(2)
                    f = EL.free_mb()
                    if f >= 0:
                        low = min(low, f)
            text = open(out, 'rb').read().decode('utf-8', 'replace')
            n = sum(1 for l in text.split(NL) if l.startswith('DEP\t'))
            c = dict(kernel=k, top=top, tag=tag, rc=p.returncode, seconds=int(time.time() - t0), free_before=fm, low=low, deps=n,
                     out=out.replace('\\', '/'), errors=[l[:200] for l in text.split(NL) if ': error' in l][:5])
            J['calls'].append(c)
            _put_deps_runs(J)
            print('  %s [%d] %s exit %s ; %d s ; free %d MB before, low %s MB ; DEP lines %d' % (k, i, top, p.returncode, c['seconds'], fm, low, n),
                  flush=True)
    J['stopped'] = None
    _put_deps_runs(J)
    print('### EXIT 0 %s' % utc(), flush=True)


def _put_deps_runs(J):
    b = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(DEPS_RUNS + '.tmp', 'wb').write(b)
    os.replace(DEPS_RUNS + '.tmp', DEPS_RUNS)


INTERNAL = re.compile(r'\._|\.proof_\d+(_\d+)*$|\.match_\d+(_\d+)*$|\.eq_\d+(_\d+)*$|\.eq_def$|\.sunfold$|\._unfold$|\.induct$|\.mutual_induct$')


def _owner(n):
    """an auxiliary constant folded into its parent declaration (`foo._proof_1`, `foo.match_2`, `foo.eq_1` -> `foo`)."""
    m = INTERNAL.search(n)
    return n[:m.start()] if m else n


def _deps_load():
    """{kernel: {owner: dict(kind, module, T=set, V=set)}} from every call`s output, the auxiliaries folded into their owners."""
    J = _deps_runs()
    out = {}
    for c in J.get('calls') or []:
        if c.get('rc') != 0:
            continue
        K_ = out.setdefault(c['kernel'], {})
        for l in io.open(c['out'], encoding='utf-8', errors='replace'):
            if not l.startswith('DEP\t'):
                continue
            p = l.rstrip('\n').split('\t')
            if len(p) < 8:
                continue
            n, kind, mod, t, v = p[1], p[2], p[3], p[5], p[7]
            o = _owner(n)
            e = K_.setdefault(o, dict(kind=None, module=mod, T=set(), V=set()))
            if o == n:
                e['kind'], e['module'] = kind, mod
                e['T'] |= set(t.split())
                e['V'] |= set(v.split())
            else:
                e['V'] |= set(t.split()) | set(v.split())     # ### an auxiliary`s type and value are the owner`s proof
    for K_ in out.values():
        for e in K_.values():
            e['T'] = set(_owner(x) for x in e['T'])
            e['V'] = set(_owner(x) for x in e['V'])
    return out


def _head_names(k, h, decl, K_):
    """the constants of kernel k that ARE head h: its declaration (by module and last component) and its projections and constructors; for a
    library predicate, every used name whose last component is h and which is not the kernel`s own."""
    if decl and decl.get('repo') == k:
        f = decl['file']
        mod = os.path.basename(f)[:-5] if k == 'SIDE-global-section' else (f[len('Vendored/Bulka/'):] if f.startswith('Vendored/Bulka/') else f)[:-5].replace('/', '.')
        base = [n for n, e in K_.items() if e['module'] == mod and n.split('.')[-1] == h]
        return set(base) | set(n for n in K_ for b in base if n.startswith(b + '.'))
    used = set(x for e in K_.values() for x in (e['T'] | e['V']))
    return set(x for x in used if x.split('.')[-1] == h and x not in K_)


def _components(nodes, K_):
    adj = collections.defaultdict(set)
    for n in nodes:
        for d in (K_[n]['T'] | K_[n]['V']):
            if d in nodes and d != n:
                adj[n].add(d)
                adj[d].add(n)
    seen, comps = set(), []
    for n in sorted(nodes):
        if n in seen:
            continue
        stack, comp = [n], set()
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            comp.add(x)
            stack += [y for y in adj[x] if y not in seen]
        users = set(y for x in comp for y in comp if x != y and x in (K_[y]['T'] | K_[y]['V']))
        terms = sorted(x for x in comp if x not in users)
        comps.append((comp, terms or ['(a cycle) ' + sorted(comp)[0]]))
    return comps


def consumers(*a):
    """data/b643_consumers.txt and .json: per head of the census`s 50, per kernel its rows sit in, the theorems whose statement or proof uses the
    head (CONSUMERS, statement and proof apart), the CHAINS (weakly connected components of the kernel`s use-graph restricted to the declarations
    consuming the head directly or transitively, the head and its projections removed, each named by its terminal declarations), and HINGE where the
    consumers lie in more than one kernel or more than one chain within a kernel -- both readings printed."""
    P = jl('b642_premise_status.json')
    DEP = _deps_load()
    J = _deps_runs()
    L = ['b643 -- COMPONENT 4, (R253)(5)(b): THE CONSUMERS, THE CHAINS AND THE HINGES, FROM THE DEPENDENCY PRINT (%s)' % utc(), '',
         '### the print: data/b643_deps_runs.json, %d calls over %d kernels, every call exit 0 %s ; declarations read per kernel: %s' % (
             len(J.get('calls') or []), len(DEP), all(c.get('rc') == 0 for c in J.get('calls') or []),
             ', '.join('%s %d' % (k, len(v)) for k, v in sorted(DEP.items()))),
         '### the watchdog`s lows per call: %s' % ', '.join('%s %s' % (c['tag'].split('__')[-1][:28], c.get('low')) for c in J.get('calls') or []),
         '### a CONSUMER is a theorem (not an auxiliary, which is folded into its owner) whose type (statement) or value (proof) uses the head or one of '
         'its projections or constructors; read from the print alone.', '']
    rows = []
    for v in P.get('heads') or []:
        h, decl = v['head'], v.get('decl')
        per, hinge_k, hinge_c = [], [], []
        for k in v['kernels']:
            K_ = DEP.get(k)
            if K_ is None:
                per.append(dict(kernel=k, read=False, why='no call of that kernel'))
                continue
            rows_k = [x.split(' ', 1)[1] for x in v.get('rule_rows') or [] if x.split(' ', 1)[0] == k]
            seen = [x for x in rows_k if x in K_ or any(n.endswith('.' + x) for n in K_)]
            if rows_k and not seen:
                per.append(dict(kernel=k, read=False, why='the declarations its rows sit in (%s) are in modules with no olean at HEAD; '
                                                          'the print reads built environments only' % ', '.join(rows_k[:3])))
                continue
            H = _head_names(k, h, decl, K_)
            direct = [n for n, e in K_.items() if n not in H and ((e['T'] | e['V']) & H)]
            thm = sorted(n for n in direct if K_[n]['kind'] == 'theorem')
            st = sorted(n for n in thm if K_[n]['T'] & H)
            R_ = set(direct)
            grow = True
            while grow:
                new = set(n for n, e in K_.items() if n not in R_ and n not in H and ((e['T'] | e['V']) & R_))
                grow = bool(new)
                R_ |= new
            comps = _components(R_, K_)
            cons_comps = [c for c in comps if set(thm) & c[0]]
            per.append(dict(kernel=k, read=True, head_names=sorted(H)[:6], n_head=len(H), consumers=len(thm), statement=len(st),
                            proof_only=len(thm) - len(st), reach=len(R_), chains=[t[:3] for _c, t in cons_comps], n_chains=len(cons_comps),
                            sample=thm[:5]))
            if len(cons_comps) > 1:
                hinge_c.append(k)
        kk = [p['kernel'] for p in per if p.get('read') and p['consumers'] > 0]
        if len(kk) > 1:
            hinge_k = kk
        anyread = any(p.get('read') for p in per)
        rows.append(dict(head=h, per=per, consumers=sum(p.get('consumers', 0) for p in per) if anyread else None, hinge=bool(hinge_k or hinge_c),
                         hinge_kernels=hinge_k, hinge_chains=hinge_c, unread=[p['kernel'] for p in per if not p.get('read')]))
        L.append('%s  CONSUMERS %s%s%s' % (h, rows[-1]['consumers'] if anyread else 'NOT READ',
                                           (' (unread: %s)' % ', '.join(rows[-1]['unread'])) if rows[-1]['unread'] and anyread else '',
                                           ('  ### HINGE -- across kernels: %s ; across chains within: %s' % (hinge_k or 'no', hinge_c or 'no'))
                                           if rows[-1]['hinge'] else ''))
        for p in per:
            if not p.get('read'):
                L.append('    %s : ### NOT READ -- %s' % (p['kernel'], p.get('why')))
                continue
            L.append('    %s : head constants %d %s ; consumers %d (statement %d, proof only %d) ; reach %d ; chains %d%s' % (
                p['kernel'], p['n_head'], p['head_names'][:3], p['consumers'], p['statement'], p['proof_only'], p['reach'], p['n_chains'],
                (' : ' + ' | '.join(', '.join(t) for t in p['chains'][:8])) if p['n_chains'] else ''))
    nh = sum(1 for r in rows if r['hinge'])
    L += ['', '### ### **HEADS %d ; WITH A CONSUMER %d ; WITHOUT %d ; NOT READ %d ; A KERNEL UNREAD BESIDE A READ ONE %d ; HINGES %d (across kernels %d, '
              'across chains within a kernel %d).**' % (
                  len(rows), sum(1 for r in rows if r['consumers']), sum(1 for r in rows if r['consumers'] == 0),
                  sum(1 for r in rows if r['consumers'] is None), sum(1 for r in rows if r['unread'] and r['consumers'] is not None), nh,
                  sum(1 for r in rows if r['hinge_kernels']), sum(1 for r in rows if r['hinge_chains']))]
    put_txt('b643_consumers.txt', L)
    put_json('b643_consumers.json', dict(at=utc(), rows=rows))
    print(L[-1])


SIX = ('OPEN', 'CITED', 'DISCHARGED', 'WITNESSED', 'DOMAIN', 'REFUTED-BY-COMPUTATION')


def _nv_rows():
    """the non-vacuity bank`s rows: {head: (outcome, class)}."""
    out, sec = {}, None
    for l in lines_of(rd('b642_nonvacuity.txt')):
        m = re.match(r'^== (WITNESSED|UNWITNESSED) \(\d+\)', l)
        if m:
            sec = m.group(1)
            continue
        if l.startswith('== '):
            sec = None
        m = re.match(r'^(\S+)  \[([A-Z-]+); b641 status ', l)
        if m and sec:
            out[m.group(1)] = (sec, m.group(2))
    return out


def premise_table(*a):
    """data/b643_premise_table.txt and .json: the 50 heads joined by head -- STATUS over six values (b642`s recomputed status bank, the head b641
    put at REFUTED-BY-COMPUTATION taking that value), NON-VACUITY over three (WITNESSED, DEGENERATE, UNWITNESSED with its reason class, from b642`s
    non-vacuity bank, a DEGENERATE witness never counted WITNESSED), CONSUMERS by kernel and HINGE (data/b643_consumers.json); counts by row."""
    P, C, Q = jl('b642_premise_status.json'), jl('b643_consumers.json'), jl('b641_premise_status.json')
    refuted = set(d['head'] for d in Q.get('dedekind') or [] if d.get('status') == 'REFUTED-BY-COMPUTATION')
    NV = _nv_rows()
    cons = dict((r['head'], r) for r in C.get('rows') or [])
    rows, errs = [], []
    for v in P.get('heads') or []:
        h = v['head']
        st = 'REFUTED-BY-COMPUTATION' if h in refuted else v['status']
        o, c = NV.get(h, (None, None))
        nv = None if o is None else ('DEGENERATE' if c == 'DEGENERATE' else 'WITNESSED' if o == 'WITNESSED' else 'UNWITNESSED (%s)' % c)
        cr = cons.get(h)
        if st not in SIX or nv is None or cr is None:
            errs.append('%s: status %s ; non-vacuity %s ; consumers %s' % (h, st, nv, cr is not None))
            continue
        bykern = ', '.join('%s %d' % (p['kernel'], p['consumers']) for p in cr['per'] if p.get('read'))
        def _chains(p):
            names = ['`%s`' % t[0].split('.')[-1] if not t[0].startswith('(a cycle)') else t[0] for t in p['chains']]
            return '%d chains, %s%s' % (p['n_chains'], ', '.join(names[:6]), (' and %d more' % (len(names) - 6)) if len(names) > 6 else '')
        hinge = ('HINGE: %s' % '; '.join(
            (['kernels ' + ', '.join(cr['hinge_kernels'])] if cr['hinge_kernels'] else []) +
            ['in %s %s' % (p['kernel'], _chains(p)) for p in cr['per'] if p.get('read') and p['kernel'] in cr['hinge_chains']])
                 ) if cr['hinge'] else '—'
        unread = cr.get('unread') or []
        cell = ('not read (%s: its rows` modules have no olean at HEAD)' % ', '.join(unread)) if cr['consumers'] is None else \
            ('%d (%s%s)' % (cr['consumers'], bykern, ('; not read: %s' % ', '.join(unread)) if unread else ''))
        rows.append(dict(head=h, status=st, nonvacuity=nv, consumers=cr['consumers'], by_kernel=bykern, hinge=hinge, is_hinge=cr['hinge'],
                         cons_cell=cell, unread=unread))
    cs, cn = collections.Counter(r['status'] for r in rows), collections.Counter(r['nonvacuity'].split(' (')[0] for r in rows)
    L = ['b643 -- COMPONENT 4, (R253)(5)(b)-(c): THE PREMISE TABLE AT v0.7, JOINED BY HEAD FROM THE BANKS (%s)' % utc(), '',
         '| head | status | non-vacuity | consumers (by kernel) | hinge |', '|:--|:--|:--|:--|:--|']
    L += ['| %s | %s | %s | %s | %s |' % (r['head'], r['status'], r['nonvacuity'], r['cons_cell'], r['hinge']) for r in rows]
    L += ['', '### COUNTS BY ROW: heads %d ; status %s ; non-vacuity %s ; heads with a consumer %d ; with none %d ; consumers not read %d ; hinges %d' % (
        len(rows), ', '.join('%s %d' % (s, cs[s]) for s in SIX), ', '.join('%s %d' % kv for kv in sorted(cn.items())),
        sum(1 for r in rows if r['consumers']), sum(1 for r in rows if r['consumers'] == 0), sum(1 for r in rows if r['consumers'] is None),
        sum(1 for r in rows if r['is_hinge']))]
    L.append('### every head one status and one non-vacuity value: %s ; a consumers count read: %d of %d (not read: %s) ; DEGENERATE counted as '
             'WITNESSED: %d' % (not errs and len(rows) == 50, sum(1 for r in rows if r['consumers'] is not None), len(rows),
                                [r['head'] for r in rows if r['consumers'] is None] or 'none',
                                sum(1 for r in rows if r['nonvacuity'] == 'WITNESSED' and NV.get(r['head'], ('', ''))[1] == 'DEGENERATE')))
    if errs:
        print(NL.join('  ### ' + e for e in errs))
        sys.exit('### PREMISE TABLE: %d HEADS UNJOINED -- NOTHING WRITTEN' % len(errs))
    put_txt('b643_premise_table.txt', L)
    put_json('b643_premise_table.json', dict(at=utc(), rows=rows, status=dict(cs), nonvacuity=dict(cn)))
    print(NL.join(L[-2:]))


# ================================================================================ COMPONENT 6: THE EDITION, (R253)(5)
# ### v0.6 carried line for line, three changes: (1) the glossary block regenerated from data/glossary.txt by the generator's own builder
# ### (tools/chain_page.py glossary_block), so it is the pages' block byte for byte; (2) the v0.7 version line above v0.6's; (3) a v0.7 back matter
# ### at the end: the readings, the premise table joined from the banks, the counts by row, the Pi-0-1 paragraph's state, the version history.
# ### No cell is typed: every row and count is read from data/b643_premise_table.json and the banks it was joined from.
V7_TAG = '## Back matter of the v0.7 edition — written 2026-10-08 by b643 under the author’s ruling `(R253)`(5), by the form of `(R187)`(5)'


def _old_glossary_block():
    import tempfile
    import chain_page as CP
    old = subprocess.run(['git', '-C', RELAY, 'show', '%s:data/glossary.txt' % K.PRE_RELAY], capture_output=True).stdout
    p = os.path.join(tempfile.mkdtemp(), 'glossary_pre.txt')
    open(p, 'wb').write(old)
    return CP.glossary_block(p)


def _v7_backmatter(T, C):
    rows = T['rows']
    cs, cn = collections.Counter(r['status'] for r in rows), collections.Counter(r['nonvacuity'].split(' (')[0] for r in rows)
    P = dict((v['head'], v) for v in (jl('b642_premise_status.json').get('heads') or []))
    nrule, nelab = sum(P[r['head']]['rule'] for r in rows), sum(P[r['head']]['elab'] for r in rows)
    hinges = [r for r in rows if r['is_hinge']]
    pi = rd('b643_pi01_attempts.txt')
    pi_read = re.search(r'REACHED AND READ (\d+)', pi)
    L = ['', V7_TAG, '',
         '### The readings v0.7 adds, each the seat’s and strikeable', '',
         '- **The heads.** The census’s heads are those of relay `data/b641_premise_status.json`, the census v0.6 premise table’s heads.',
         '- **STATUS.** The status of relay `data/b642_premise_status.json` (the reader of b640, run again at b642), the head b641 computed false '
         'taking REFUTED-BY-COMPUTATION, its refutation compiled at b642.',
         '- **NON-VACUITY.** The outcome of relay `data/b642_nonvacuity.txt`: WITNESSED, DEGENERATE, or UNWITNESSED with its reason class; a '
         'DEGENERATE witness is its own value and is not counted with the WITNESSED.',
         '- **CONSUMERS.** The theorems of each kernel whose statement or proof uses the head, read from the dependency print of each kernel’s '
         'elaborated environment (relay `data/b643_consumers.txt`), an auxiliary declaration folded into its owner.',
         '- **HINGE.** A head whose consumers lie in more than one kernel, or in more than one chain within a kernel; the chain as the glossary '
         'defines it, named by its terminal declarations.',
         '- **The numerals.** In this back matter every numeral is a count of the table’s own rows or cells.', '',
         '### The premise table at v0.7: status, non-vacuity, consumers, hinge', '',
         '| head | status | non-vacuity | consumers (by kernel) | hinge |', '|:--|:--|:--|:--|:--|']
    L += ['| %s | %s | %s | %s | %s |' % (r['head'], r['status'], r['nonvacuity'], r['cons_cell'], r['hinge']) for r in rows]
    L += ['', '*%d heads. Status: %s. Non-vacuity: %s. Heads with a consumer: %d; with none: %d; consumers not read: %d. Hinges: %d. The '
          'rule-graded rows resting on the heads: %d; the rule-elab rows beside: %d.*' % (
              len(rows), ', '.join('%s %d' % (s, cs[s]) for s in SIX), ', '.join('%s %d' % kv for kv in sorted(cn.items())),
              sum(1 for r in rows if r['consumers']), sum(1 for r in rows if r['consumers'] == 0), sum(1 for r in rows if r['consumers'] is None),
              len(hinges), nrule, nelab), '',
          '### The Π⁰₁ form of the open clause', '',
          ('The paragraph is written where Kreisel’s statement and Davis, Matijasevič and Robinson’s are read at source; %s, so it is not '
           'written and the work-order stays open (relay `data/b643_pi01_attempts.txt`).' % (
               'neither was reached' if pi_read and pi_read.group(1) == '0' else 'the attempt bank names what was reached')), '',
          '### Version history', '',
          '- **v0.7, 2026-10-08 (b643, `(R253)`(5))**: the premise table under the status of six values, the non-vacuity column with DEGENERATE '
          'apart, the consumers read from the dependency print and the hinges marked with their chains; the glossary block extended by the '
          'status, the witness, the degenerate witness, the consumer, the chain and the hinge.',
          '- **v0.6, 2026-10-07 (b638)** and the editions before it: carried above.']
    return L


def edition(*a):
    """PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_7.md beside v0.6 (unedited), and data/b643_edition.json. `dry`: the scratchpad."""
    import chain_page as CP
    T, C = jl('b643_premise_table.json'), jl('b643_consumers.json')
    if not T or not C:
        sys.exit('### NO PREMISE TABLE OR CONSUMERS BANK -- NOTHING WRITTEN')
    v6 = lines_of(K.show(K.CEN6))
    ob, nb = _old_glossary_block(), CP.glossary_block()
    at = [i for i in range(len(v6)) if v6[i:i + len(ob)] == ob]
    vl = [i for i, l in enumerate(v6) if l.startswith('*v0.6, 2026-10-07')]
    if len(at) != 1 or len(vl) != 1:
        sys.exit('### THE GLOSSARY BLOCK (%s) OR THE VERSION LINE (%s) NOT FOUND ONCE -- NOTHING WRITTEN' % (at, vl))
    i, j = at[0], vl[0]
    ver = ('*v0.7, 2026-10-08 -- the premise table under six statuses, with a non-vacuity column (DEGENERATE apart), a consumers column read '
           'from the dependency print and the hinges marked with their chains; the glossary extended; v0.6 stands beside it, unedited.*')
    out = v6[:i] + nb + v6[i + len(ob):j] + [ver, ''] + v6[j:] + _v7_backmatter(T, C)
    b = (NL.join(out) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b643_census_dry.md') if DRY else os.path.join(PP, *K.CEN7.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### v0.7 EXISTS -- NOTHING WRITTEN')
    _write(dest, b)
    put_json('b643_edition.json', dict(at=utc(), path=K.CEN7, sha256=sha(b), bytes=len(b), lines=len(out), glossary_at=i + 1,
                                       glossary_lines=len(nb), glossary_sha256=sha((NL.join(nb) + NL).encode('utf-8')), version_line=j + len(nb) - len(ob) + 1,
                                       backmatter=out.index(V7_TAG) + 1, v6_lines=len(v6), dry=DRY))
    print('  %s : %d lines, %d bytes, sha256 %s ; the glossary block %d lines at :%d ; the back matter at :%d' % (
        ('DRY ' + dest) if DRY else K.CEN7, len(out), len(b), sha(b)[:16], len(nb), i + 1, out.index(V7_TAG) + 1))


def termscan(*a):
    """data/b643_census_termscan.txt: the scanner (b633`s _scan, the banned-term and stem scan) over the census at v0.7, its verdict printed."""
    t = _scan(os.path.join(PP, *K.CEN7.split('/')))
    put_txt('b643_census_termscan.txt', t.rstrip(NL).split(NL))
    print('  ' + ' ; '.join(l.strip() for l in t.split(NL) if re.search(r'live uses|VERDICT', l)) + ' ; clean %s' % _clean(t))


def edition_diff(*a):
    """data/b643_edition_diff.txt: v0.7 against v0.6 by section, every changed line printed with its kind."""
    import difflib
    v6 = lines_of(K.show(K.CEN6))
    v7 = lines_of(io.open(os.path.join(PP, *K.CEN7.split('/')), encoding='utf-8').read())
    ob = _old_glossary_block()
    gi = [i for i in range(len(v6)) if v6[i:i + len(ob)] == ob]
    gset = set(range(gi[0], gi[0] + len(ob))) if gi else set()
    L = ['b643 -- COMPONENT 6: v0.7 AGAINST v0.6, BY SECTION (%s)' % utc(), '']
    kinds, outside = collections.Counter(), 0
    for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, v6, v7, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        outside += sum(1 for k in range(a1, a2) if k not in gset)
        head = next((v7[k] for k in range(b1, -1, -1) if k < len(v7) and v7[k].startswith('#')), '(the head)')
        kinds[tag] += 1
        L.append('### %s at v0.6 :%d-:%d -> v0.7 :%d-:%d ; section: %s ; removed %d, added %d' % (tag.upper(), a1 + 1, a2, b1 + 1, b2, head[:90], a2 - a1, b2 - b1))
        L += ['    - %s' % l[:200] for l in v6[a1:a2]][:6] + ['    + %s' % l[:200] for l in v7[b1:b2]][:6]
    L += ['', '### ### **HUNKS %d (%s) ; v0.6 LINES REMOVED OUTSIDE THE GLOSSARY BLOCK : %d.**' % (
        sum(kinds.values()), dict(kinds), outside)]
    put_txt('b643_edition_diff.txt', L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 6: THE SECOND READER, (R253)(6)
READER_DIR = 'C:/reader_b643'
QUESTIONS = ('What is the clause?',
             'What is a hinge, and which premises are hinges?',
             'Which premise is refuted, and what does that do to the theorem that rests on it?')
READER_LEAD = ('Reader task follows. The packet is at C:\\reader_b643\\packet\\ and your answers go to C:\\reader_b643\\answers.txt. Read only the two '
               'packet files. Do not open any other file on this machine, do not run any command, and do not search the web. Write the answers '
               'file, report that it is written, and stop.')
READER_CMD = ('Get-Content C:\\reader_b643\\full_prompt.txt -Raw | claude -p --output-format json --allowedTools Read Glob Write --disallowedTools '
              'Bash PowerShell WebFetch WebSearch --permission-mode acceptEdits --setting-sources user --strict-mcp-config > '
              'C:\\reader_b643\\reader_run.log 2> C:\\reader_b643\\reader_run.err')


def _reader_task():
    return (READER_LEAD + NL + NL +
            'You are an independent reader. You know nothing of the research programme the packet describes, and that is the point. The packet has '
            'two files: census.txt, a census of the programme`s papers, and questions.txt, three questions. Read the census and answer each question '
            'in your own words, from the census alone, in a few sentences each: say what the text says, not what you know of the mathematics, and '
            'say plainly where the text is unclear to you. Write the file C:\\reader_b643\\answers.txt with exactly three sections, headed ANSWER 1:, '
            'ANSWER 2: and ANSWER 3:, each followed by your answer to that question; then a fourth section headed UNCLEAR: listing any sentence of '
            'the census you could not follow, or the word none. Then stop.')


def reader_packet(*a):
    """the reader`s packet staged off D:\\ (C:/reader_b643: packet/census.txt -- the census at v0.7 as committed, packet/questions.txt,
    lead.txt, full_prompt.txt) and its copy banked (data/b643_reader_packet/, data/b643_reader_prompt.txt); the no-disclosure arm and the
    outside-name needles over it; data/b643_reader_packet.txt with the command the reader is run by."""
    import b616_record as R6
    census = io.open(os.path.join(PP, *K.CEN7.split('/')), encoding='utf-8').read().replace(chr(13), '')
    qs = NL.join('%d. %s' % (i + 1, q) for i, q in enumerate(QUESTIONS))
    task = _reader_task()
    nd = R6.nd_hits(census + NL + qs + NL + task, R6.nd_sets())[0]
    outside = [n for n in OUTSIDE_NEEDLES if n in census]
    if any(nd.values()) or outside:
        sys.exit('### THE PACKET WOULD CARRY TECHNE TEXT OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    pdir = os.path.join(SP if DRY else D, 'b643_reader_packet')
    os.makedirs(pdir, exist_ok=True)
    for n_, t_ in (('census.txt', census), ('questions.txt', qs)):
        _write(os.path.join(pdir, n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    _write(os.path.join(SP if DRY else D, 'b643_reader_prompt.txt'), (task + NL).encode('utf-8'))
    if not DRY:
        if os.path.exists(READER_DIR) and os.listdir(READER_DIR):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- THE READER`S DIRECTORY NOT WRITTEN' % READER_DIR)
        os.makedirs(READER_DIR + '/packet', exist_ok=True)
        for n_, t_ in (('packet/census.txt', census), ('packet/questions.txt', qs), ('lead.txt', READER_LEAD), ('full_prompt.txt', task)):
            _write(os.path.join(READER_DIR, n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    L = ['b643 -- COMPONENT 6, (R253)(6): THE SECOND READER`S PACKET, STAGED OFF D:\\ (%s)' % utc(), '',
         '### staged: %s (packet/census.txt %d bytes, sha256 %s ; packet/questions.txt ; lead.txt ; full_prompt.txt) ; banked: relay '
         'data/b643_reader_packet/, data/b643_reader_prompt.txt' % (READER_DIR, len(census.encode('utf-8')), sha(census.encode('utf-8'))),
         '### the questions: %s' % ' / '.join(QUESTIONS), '### the no-disclosure arm over the packet and the prompt: %s ; outside names: %s' % (
             dict(nd), outside or 'NONE'), '', '### the command, run from %s, a directory with no project memory:' % READER_DIR, '    ' + READER_CMD]
    put_txt('b643_reader_packet.txt', L)
    print(NL.join(L[-5:]))


ANS_RE = re.compile(r'^ANSWER ([123]):\s*(.*?)(?=^ANSWER [123]:|^UNCLEAR:|\Z)', re.M | re.S)


def _hinge_names():
    return [r['head'] for r in (jl('b643_premise_table.json').get('rows') or []) if r.get('is_hinge')]


def _needles():
    import b640_record as R40
    hn = _hinge_names()
    return {1: (r'h2_sign|located clause|quadratic form|positiv|non-?negative', 'the clause: the located open statement (h2_sign, a positivity of the '
                'explicit-formula quadratic form)', R40.q1_asserts),
            2: (r'more than one (kernel|chain)|across (kernels|chains|more than one)|several (kernels|chains)', 'what a hinge is: consumers in more '
                'than one kernel or chain', r'\b(%s)\b' % '|'.join(re.escape(h) for h in hn) if hn else r'(?!)', 'names a hinge the table marks'),
            3: (r'TrivialSummandPremise', 'the refuted premise named', r'dedekind_rhs|no instance|vacuous|cannot be (used|applied)|never appl|restat|'
                r're-?proved', 'what the refutation does to the theorem on it')}


def reader_score(*a):
    """data/b643_reader_compare.txt and .json: the reader`s answers copied from off D:\\, each scored by its needles (question 1 by the repaired
    needle of b641, an assertion of RH proved refusing it), and beside them the seat`s hand reading (data/b643_reader_handread.txt), both figures."""
    src = os.path.join(READER_DIR, 'answers.txt')
    if not os.path.exists(src):
        sys.exit('### %s IS ABSENT -- NOTHING READ' % src)
    t = io.open(src, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    _write(os.path.join(SP if DRY else D, 'b643_reader_answers.txt'), t.encode('utf-8'))
    ans = dict((int(m.group(1)), ' '.join(m.group(2).split())) for m in ANS_RE.finditer(t))
    N = _needles()
    lg = os.path.join(READER_DIR, 'reader_run.log')
    mem = ('memory named in the run log: %s' % bool(re.search(r'MEMORY\.md|[\\/]memory[\\/]', io.open(lg, encoding='utf-8', errors='replace').read()))
           if os.path.exists(lg) else 'the run log absent')
    hand = dict((int(m.group(1)), m.group(2).strip()) for m in re.finditer(r'^HAND ([123]): (AGREE|DIFFER)', rd('b643_reader_handread.txt'), re.M))
    L = ['b643 -- COMPONENT 6, (R253)(6): THE SECOND READER`S ANSWERS, SCORED BY THE NEEDLES AND BY HAND (%s)' % utc(), '',
         '### the answers: relay data/b643_reader_answers.txt, copied from %s ; the reader`s session: %s ; the hinges the table marks: %s' % (
             src, mem, ', '.join(_hinge_names()) or 'none'), '']
    res, k = {}, 0
    for q in (1, 2, 3):
        a_ = ans.get(q, '')
        n = N[q]
        if q == 1:
            hits = n[2](a_)
            ok, why = bool(re.search(n[0], a_, re.I)) and not hits, ['%s %s' % (n[1], bool(re.search(n[0], a_, re.I))),
                                                                       'RH proved asserted %s' % (hits or 'no')]
        else:
            m1, m2 = bool(re.search(n[0], a_, re.I)), bool(re.search(n[2], a_, re.I if q == 3 else 0))
            ok, why = m1 and m2, ['%s %s' % (n[1], m1), '%s %s' % (n[3], m2)]
        k += ok
        res[q] = dict(question=QUESTIONS[q - 1], answer=a_, needle=ok, why=why, hand=hand.get(q))
        L += ['### QUESTION %d: %s' % (q, QUESTIONS[q - 1]), '    the reader: %s' % (a_ or '### NO ANSWER'),
              '    the needles: %s ; ### %s' % ('; '.join(why), 'AGREE' if ok else 'DIFFER'),
              '    by hand: %s' % (hand.get(q) or '### NOT READ'), '']
    kh = sum(1 for v in hand.values() if v == 'AGREE')
    unclear = re.search(r'^UNCLEAR:\s*(.*)\Z', t, re.M | re.S)
    L += ['### UNCLEAR, the reader`s: %s' % (' '.join(unclear.group(1).split())[:1500] if unclear else '### NONE GIVEN'), '',
          '### ### **BY THE NEEDLES %d OF 3 ; BY HAND %s OF 3.**' % (k, kh if hand else '### NOT READ')]
    put_txt('b643_reader_compare.txt', L)
    put_json('b643_reader_compare.json', dict(at=utc(), answers=res, needles=k, hand=kh if hand else None,
                                               unclear=(unclear.group(1).strip() if unclear else None)))
    print(L[-1])


# ================================================================================ COMPONENT 5: THE PI-0-1 READ, (R253)(5)(d)
# ### every attempt at the two named sources, by the route tried and what came back; plain requests, no header naming the author. A source
# ### counts as read only when its own text was reached; an index, an abstract or a secondary account is recorded and not counted.
PI01_ATTEMPTS = [
    ('Davis, Matijasevič, Robinson, "Hilbert`s tenth problem. Diophantine equations: positive aspects of a negative solution", Proc. Sympos. '
     'Pure Math. 28 (1976) 323-378', [
         ('web search for an open copy of the paper', 'bibliographic records only (Scholarpedia, Springer, celebratio.org, arXiv papers citing it); '
          'no copy of the paper`s text'),
         ('https://www.ams.org/books/pspum/028.2/', 'HTTP 403 Forbidden'),
         ('https://doi.org/10.1090/pspum/028.2/0432534', 'a redirect to https://www.ams.org/pspum/028.2'),
         ('https://www.ams.org/pspum/028.2', 'HTTP 403 Forbidden'),
         ('https://celebratio.org/Robinson_JB/article/972/', 'a narrative naming the paper as a non-technical introduction; no quotation of its '
          'Riemann-hypothesis section'),
         ('web search at the PDMI pages for the paper', 'no copy found; the Riemann-hypothesis equation located instead in Matiyasevich`s 1993 '
          'book (section 6.4) by a secondary account, which is not the named source')]),
    ('Kreisel, "Mathematical significance of consistency proofs", J. Symbolic Logic 23 (1958) 155-182', [
         ('web search for the statement', 'secondary accounts (a 2019 survey of the Riemann hypothesis in computer science) saying Kreisel '
          'constructed a Pi-0-1 formula equivalent to RH; not the paper`s text'),
         ('https://philpapers.org/rec/KREMSO', 'HTTP 403 Forbidden'),
         ('https://www.jstor.org/stable/2964396', 'a page that failed to load its content'),
         ('https://doi.org/10.2307/2964396', 'a redirect to Cambridge Core'),
         ('https://www.cambridge.org/core/product/identifier/S0022481200058503/type/journal_article', 'the landing page with the paper`s opening '
          'extract only; the full text behind a login; the visible text does not mention the Riemann hypothesis')]),
]


def pi01(*a):
    """data/b643_pi01_attempts.txt: each named source, each route tried and what it returned; the verdict per (R253)(5)(d)."""
    L = ['b643 -- COMPONENT 5, (R253)(5)(d): THE PI-0-1 FORM OF RH READ AT SOURCE -- THE ATTEMPTS (%s)' % utc(),
         '### plain requests by the seat`s fetch tool, no header or parameter naming the author; a source counts as read only when its own text was '
         'reached.', '']
    reached = 0
    for src, tries in PI01_ATTEMPTS:
        L.append('### %s' % src)
        L += ['    %d. %s -- %s' % (i, r, w) for i, (r, w) in enumerate(tries, 1)]
        L.append('    ### REACHED AND READ : NO')
        L.append('')
    L += ['### ### **SOURCES NAMED 2 ; REACHED AND READ %d.** Per (R253)(5)(d) the paragraph is NOT written in the census`s opening; W-ORD-H2-PI1 '
          'stays open (OPEN_TRAILS :13531), this bank its attempt.' % reached]
    put_txt('b643_pi01_attempts.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 7: THE SEAL'S HASHES
def seal_hashes():
    rec_ = jl('b643_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b643 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b643_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


# ================================================================================ THE ROOT
ROOT_EXCLUDE = re.compile(r'^b643_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b643_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    """### (R251)(3): the act root, the last step of the act -- after the last declared seal re-run; no bank it names is written after it."""
    banks = root_banks()
    print('  banks named: %d ; the seal bank among them %s' % (len(banks), 'data/b643_seal_hashes.json' in banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b643'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the root recomputed from its banked items offline and a one-byte change on a copy of one bank moving it; the local part of verify.
    ### Writes data/b643_root_arm.*, which the root does not name."""
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b643_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b643 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; banks named %d ; changed or written after the root: %s' % (J.get('at'), len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b643_root_arm.txt', L)
    put_json('b643_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def table_final(*a):
    """the table at the end against the table committed at Component 2 (relay HEAD`s data/terminal_table.json before this run), by row."""
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b643 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved)),
         '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b643_table_final.txt', L)
    put_json('b643_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ================================================================================ THE SCORES AND THE RECORD
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = NK + SK
FIVE_BANKS = ('b643_consumers', 'b643_premise_table', 'b643_rerun', 'b643_pi01_attempts', 'b643_edition_diff')
N5_ALLOWED = {'data/b642_closing_push_out.txt', 'data/act_roots.txt', 'data/glossary.txt', K.E0_TOOL, K.E0_TEST, K.B378_TOOL, K.B378_TEST}
N5_PP = tuple(sorted(['FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE, K.CEN7]))
PRIMED_N = ("SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'", "SIDEExplicitFormula.Schema.Dedekind.TrivialSummandPremise'",
            "SIDEExplicitFormula.SaltCheckNonvacuity.trivialSummandPremise'_witness'")


def TRAIL_HEAD():
    return ('### b643 — lane three, act seventy under (R253): the two readers repaired and rerun; the pages at v0.26; the keystone census at v0.7 '
            'with six statuses, a non-vacuity column, a consumers column and the hinges; the Π⁰₁ form sought at source; the second reader')


def _glossary_same():
    import chain_page as CP
    import b638_record as R8
    b = CP.glossary_block()
    pages = [R8.glossary_lines(R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout).decode('utf-8'))
             for k in ('zeta', 'chi')]
    cen = R8.glossary_lines(io.open(os.path.join(PP, *K.CEN7.split('/')), encoding='utf-8').read()) if os.path.exists(os.path.join(PP, *K.CEN7.split('/'))) else []
    return all(p == b for p in pages) and cen == b, len(b)


def n5(trail_line=None):
    ot_text = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ot_lines = lines_of(ot_text)
    if trail_line is None:
        rec_ok, rec_state = False, 'no expected line given'
    elif len(ot_lines) >= trail_line and ot_lines[trail_line - 1] == TRAIL_HEAD():
        rec_ok, rec_state = True, 'the trail record written at :%d' % trail_line
    elif TRAIL_HEAD() not in ot_text and len(ot_lines) < trail_line:
        rec_ok, rec_state = True, 'the trail record pending at :%d' % trail_line
    else:
        rec_ok, rec_state = False, 'the trail record neither at :%s nor pending' % trail_line
    face = jl('b643_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b643_|audit_b643_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    five = [b for b in FIVE_BANKS if not os.path.exists(os.path.join(D, b + '.txt'))]
    add = ''
    for f in ('FINDINGS.md', 'OPEN_TRAILS.md'):
        pre = R2.cr0(subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRE_PP, f)], capture_output=True).stdout) or b''
        cur = R2.cr0(open(os.path.join(PP, f), 'rb').read())
        add += cur[len(pre):].decode('utf-8', 'replace') if cur.startswith(pre) else cur.decode('utf-8', 'replace')
    cen = io.open(os.path.join(PP, *K.CEN7.split('/')), encoding='utf-8').read() if os.path.exists(os.path.join(PP, *K.CEN7.split('/'))) else ''
    outside = [n for n in OUTSIDE_NEEDLES if n in add or n in cen]
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not differ and not five and not outside and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposited (no platform called); every kernel unmoved %s; PLACE-papers %s (beyond the ledgers, the two pages and the census at '
            'v0.7: %s); %s; relay beyond the act`s own banks and tools, the two repairs and their tests, the glossary, the table and the roots file: '
            '%s; the census banks absent: %s; sealed tools not agreeing %s; an outside collection named in the census or the ledgers` appends: %s; '
            'b628`s bank untracked %s; no identifier of the author in any outbound request' % (
                kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE', five or 'NONE', differ or 'NONE', outside or 'NONE', untracked_local))


def _tests_of(name):
    x = jl('b643_tests_stepzero.json').get(name) or {}
    return x.get('rc'), x.get('cases'), x.get('passing')


def scores(*a):
    import e0_rule as E
    TF, RA, ST, RR, PG, CJ, PT, RJ = (jl(n_) for n_ in ('b643_table_final.json', 'b643_root_arm.json', 'b643_tests_stepzero.json', 'b643_rerun.json',
                                                         'b643_page_arms.txt', 'b643_consumers.json', 'b643_premise_table.json', 'b643_reader_compare.json'))
    tl = [x for x in a if x.startswith('trail_line=')]
    _r, _n, sh = seal_hashes()
    T_ = dict((r['name'], r) for r in json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'] if r['repo'] == 'SIDE-explicit-formula')
    td = E.typing('WithTop ℕ∞')[0]
    mv = [m for m in RR.get('moves') or [] if m[1] == 'SIDEExplicitFormula.Keiper.contDiff_riemannZeta₀']
    pr = [(n.split('.')[-1], (T_.get(n) or {}).get('grade')) for n in PRIMED_N]
    n1 = td == 'data' and len(mv) == 1 and mv[0][2:4] == ['INTERFACES', 'DERIVES'] and all(gr not in (None, '—', 'UNGRADED') for _n_, gr in pr)
    pga = rd('b643_page_arms.txt')
    n2 = '**PAGE ARMS PASSING : 2 of 2.**' in pga and pga.count('PASSING : 2 of 2.') == 2
    rows = PT.get('rows') or []
    deg = sum(1 for r in rows if r['nonvacuity'] == 'DEGENERATE')
    n3 = len(rows) == 50 and all(r['status'] in SIX for r in rows) and 'DEGENERATE counted as WITNESSED: 0' in rd('b643_premise_table.txt') \
        and all(r.get('hinge_kernels') or r.get('hinge_chains') for r in CJ.get('rows') or [] if r.get('hinge'))
    unread3 = [r['head'] for r in rows if r.get('consumers') is None]
    gsame, glen = _glossary_same()
    clean = [n for n, x in ST.items() if x.get('rc') == 0 and not x.get('failing')]
    e0b = re.search(r'tools/e0_rule\.py.*\n.*before the edit : ### ### \*\*(\d+) of (\d+)', rd('b643_repairs.txt'))
    S = {
        'N1': (('HELD' if n1 else 'REFUTED'), 'the repaired gate types n : WithTop ℕ∞ as %s; contDiff_riemannZeta₀ %s; the three primed rows graded %s' % (
            td, (' -> '.join(mv[0][2:4])) if mv else '### NOT MOVED', pr)),
        'N2': (('HELD' if n2 else 'REFUTED'), 'the page arms and the frozen control at v0.26: %s' % ' ; '.join(l.strip() for l in pga.split(NL) if 'PASSING' in l)),
        'N3': (('HELD' if n3 and not unread3 else 'REFUTED IN ONE CLAUSE' if n3 else 'REFUTED'),
               'heads %d, each one status of six and one non-vacuity value (DEGENERATE %d, none counted WITNESSED); a consumers count read for %d, '
               'not read for %s (their rows` modules have no olean at HEAD); hinges %d, each with its kernels or chains' % (
                   len(rows), deg, len(rows) - len(unread3), unread3 or 'none', sum(1 for r in CJ.get('rows') or [] if r.get('hinge')))),
        'N4': (('HELD' if gsame else 'REFUTED'), 'the glossary block (%d lines) byte for byte on both pages at PLACE-papers HEAD and in the census at v0.7: %s' % (glen, gsame)),
        'N5': n5(int(tl[0].split('=')[1]) if tl else None),
        'S1': (('HELD' if all(_tests_of(t)[1:] == (n_, n_) for t, n_ in (('test_e0_databinder_b643.py', 10), ('test_primed_names_b643.py', 8))) else 'REFUTED'),
               'the two planted tests: test_e0_databinder_b643.py %s of %s, test_primed_names_b643.py %s of %s after the repairs, each failing before '
               'its edit (data/b643_repairs.txt)' % (_tests_of('test_e0_databinder_b643.py')[2], _tests_of('test_e0_databinder_b643.py')[1],
                                                     _tests_of('test_primed_names_b643.py')[2], _tests_of('test_primed_names_b643.py')[1])),
        'S2': (('HELD' if ST and len(clean) == len(ST) else 'REFUTED'), 'every test file clean: %d of %d; not clean %s' % (
            len(clean), len(ST), sorted(n for n in ST if n not in clean) or 'none')),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against the table committed at Component 2: moved %s, gone %s, added %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []))),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED') if RA else 'PENDING',
               'the root recomputed equal and the one-byte control moving it'),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED'), 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    put_json('b643_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:260]))


def _title():
    RR, PT, CJ, RJ = jl('b643_rerun.json'), jl('b643_premise_table.json'), jl('b643_consumers.json'), jl('b643_reader_compare.json')
    gm = len((RR.get('table') or {}).get('grade_moved') or [])
    deg = sum(1 for r in PT.get('rows') or [] if r['nonvacuity'] == 'DEGENERATE')
    h = sum(1 for r in CJ.get('rows') or [] if r.get('hinge'))
    reached = re.search(r'REACHED AND READ (\d+)', rd('b643_pi01_attempts.txt'))
    return ('## The two readers repaired and rerun, %d grades moved; the pages at v0.26; the keystone census at v0.7: %d heads, six statuses, '
            'non-vacuity with %d degenerate, consumers with %d hinges; the Π⁰₁ form %s; the second reader %s of 3 by the needles and %s by hand' % (
                gm, len(PT.get('rows') or []), deg, h, 'not reached at source' if reached and reached.group(1) == '0' else 'read at source',
                RJ.get('needles', '?'), RJ.get('hand', '?')))


TITLE = _title()


def _finding_text():
    S, rl, J, RR, PT, CJ, RJ, P = (jl(n_) for n_ in ('b643_scores.json', 'b643_record_lines.json', 'b643_act_root.json', 'b643_rerun.json',
                                                     'b643_premise_table.json', 'b643_consumers.json', 'b643_reader_compare.json', 'b643_page_zeta.json'))
    PC = jl('b643_page_chi.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b643_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    t = RR.get('table') or {}
    rows = PT.get('rows') or []
    cs = collections.Counter(r['status'] for r in rows)
    cn = collections.Counter(r['nonvacuity'].split(' (')[0] for r in rows)
    hinges = [r['head'] for r in CJ.get('rows') or [] if r.get('hinge')]
    sc = lambda k: (S.get(k) or ['?'])[0]   # noqa: E731
    e = ['', TITLE, '',
         '*Filed at b643 on the author’s ruling `(R253)` and the author’s answers (%d). Banks: relay `data/b643_repairs.txt`, `data/b643_rerun.txt`, '
         '`data/b643_page_zeta.json`, `data/b643_page_chi.json`, `data/b643_consumers.txt`, `data/b643_premise_table.txt`, '
         '`data/b643_pi01_attempts.txt`, `data/b643_reader_compare.txt`, `data/b643_act_root.txt`.*' % n_ans, '',
         '**The repairs** (Component 0, `(R253)`(3)): the gate’s lexicon takes WithBot and WithTop as Type formers, so a binder whose type applies '
         'one is data (relay %s, alone with its planted test, 10 of 10, 6 of 10 before the edit); the textual reader’s declaration pattern ends a '
         'name where Lean’s identifier ends, so a primed name resolves and an unprimed one no longer resolves at its primed neighbour (relay %s, '
         'alone with its planted test, 8 of 8, 3 of 8 before). N1 %s.' % (K.E0_COMMIT, K.B378_COMMIT, sc('N1')), '',
         '**The rerun** (Component 2): the elaborated reader over SIDE-explicit-formula at v0.26 and SIDE-structural-error-correction at v0.2.2, '
         'one module per lean call; under the repaired rule %d grade moves, contDiff_riemannZeta₀ from INTERFACES to DERIVES; the terminal table '
         'regenerated, %d rows moved, %d of them in grade (the three primed rows graded among them), none added or gone.' % (
             len(RR.get('moves') or []), len(t.get('moved') or []), len(t.get('grade_moved') or [])), '',
         '**The pages** (Component 3, `(R253)`(4)): the lists pinned at v0.26 by their pin lines alone and probed afresh; the zeta page’s '
         'Correspondence %s to %s rows and the chi page’s %s to %s under the selection rule unchanged, on the author’s answer; both pages carry the '
         'extended glossary; the page arms pass and the frozen control passes. N2 %s.' % (
             P.get('corr_before'), P.get('corr_after'), PC.get('corr_before'), PC.get('corr_after'), sc('N2')), '',
         '**The census at v0.7** (Components 4 and 6, `(R253)`(5)): phase2/method/THE_KEYSTONE_CENSUS_v0_7.md beside v0.6, every cell of its '
         'premise table joined from the banks. Status: %s. Non-vacuity: %s, a degenerate witness its own value and never counted a witness. '
         'Consumers read from the dependency print of each kernel’s elaborated environment, %d heads with a consumer; hinges %d -- %s. The glossary '
         'extended by six entries, the chain in the author’s words, the block the same on both pages and in the census. N3 %s; N4 %s.' % (
             ', '.join('%s %d' % (s, cs[s]) for s in SIX), ', '.join('%s %d' % kv for kv in sorted(cn.items())),
             sum(1 for r in rows if r['consumers']), len(hinges), ', '.join('`%s`' % h for h in hinges), sc('N3'), sc('N4')), '',
         '**The Π⁰₁ form** (Component 5, `(R253)`(5)(d)): Kreisel’s statement and Davis, Matijasevič and Robinson’s were sought at source and not '
         'reached; the paragraph is not written and W-ORD-H2-PI1 stays open, the attempts banked.', '',
         '**The second reader** (Component 6, `(R253)`(6)): run from a directory with no project memory, three questions on the census; %s of 3 by '
         'the needles, question one by the repaired needle, and %s of 3 by hand, both figures as banked.' % (RJ.get('needles', '?'), RJ.get('hand', '?')), '',
         '**The record lines** (`(R253)`(1)-(2)): b642 at its weight (FINDINGS :%s); W-ORD-WATCHDOG-STOP entered and priced (OPEN_TRAILS :%s); '
         'the navigator’s defect (j) as recorded (:%s).' % (ls[0].get('line'), ls[1].get('line'), ls[2].get('line')), '',
         '**The root.** b643 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, sc(k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it reads b642’s non-vacuity bank (FINDINGS :%d) beside the dependency print, so that a '
         'premise’s witness and the theorems that rest on it stand in one row, and it repairs the two misreadings b642 banked as printed. It '
         'strengthens the programme’s offering of an assumption list a reader can check: for every premise the census counts, whether it has a '
         'witness, which theorems consume it, and whether it is a hinge between lines of argument.' % K.B642_ENTRY, '',
         '**Next.** Per `(R253)`(7): b644, the author’s word pending -- the description re-cut as synthesis under the b640 plan, the census at v0.7 '
         'joining the file set, and W-ORD-H2-LATTICE; the deposit draft held.', '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; the census counts premises, witnesses and consumers and confers '
         'nothing.*', '']
    return TITLE, NL.join(e)


FOR_AUTHOR = ('(1) the repair of the textual reader landed in tools/b378_terminals.py`s declaration pattern, which tools/terminal_table.py imports '
              'and does not copy; (2) the node lists carried as this act`s editions, b638`s untouched, their pin lines alone edited; (3) the glossary '
              'extended before the pages were re-emitted, so the block they print is the census`s; (4) the census generated by the record tool from '
              'the banks, act_root.py`s census path being a reader of the kernel column and left on v0.6; (5) the consumers counted as theorems, an '
              'auxiliary declaration folded into its owner, a library predicate`s consumers counted in each kernel its rows sit in; (6) the dependency '
              'print run one top module per lean call, each environment holding every kernel module beneath it')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b643_scores.json', 'b643_findings.json', 'b643_record_lines.json', 'b643_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b643_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R253) ratified.** (1) b642 at its weight. (2) W-ORD-WATCHDOG-STOP. (3) The two reader repairs and the rerun. (4) The pages at '
             'v0.26. (5) The census at v0.7 with its glossary, its four columns, its counts and its Π⁰₁ paragraph sought. (6) The second reader. '
             '(7) The deposit held; the act after: b644. (8) The seal after the components.', '',
             '**Entered:** FINDINGS.md:%s (b642’s weight), :%s (the entry); OPEN_TRAILS.md:%s (W-ORD-WATCHDOG-STOP), :%s (defect (j)); this record; '
             'PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_7.md and the two pages.' % (
                 ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ls[2].get('line')), '',
             '**Act root:** b643 `%s` (previous `%s`, b642’s; relay data/act_roots.txt), computed after the last bank it names.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b643_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): b644 names no kernel terminal; the description re-cut and the census joining the file set.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b643_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R253)`(7), b644, the author’s word pending; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b643_scores.json')
    L = ['=' * 104, 'b643 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rd('b643_defects.txt').rstrip(NL).split(NL)
    put_txt('b643_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b643_scores.json', 'b643_findings.json', 'b643_trail.json', 'b643_record_lines.json', 'b643_act_root.json'))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    L = ['b643 -- THE COMPONENTS, BANKED UNDER (R253).', '',
         '### COMPONENT 0 : step zero and the two repairs (data/b643_tests_stepzero.txt, data/b643_repairs.txt) ; relay %s, %s ; N1 %s' % (
             K.E0_COMMIT, K.B378_COMMIT, S['N1'][0]),
         '### COMPONENT 1 : b642`s weight FINDINGS :%s ; W-ORD-WATCHDOG-STOP OPEN_TRAILS :%s ; defect (j) :%s' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line')),
         '### COMPONENT 2 : the rerun (data/b643_rerun.txt, data/b643_elab_ef.txt, data/b643_elab_sec.txt)',
         '### COMPONENT 3 : the pages at v0.26 (data/b643_page_zeta.json, data/b643_page_chi.json, data/b643_page_arms.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 4 : the census banks (data/b643_consumers.txt, data/b643_premise_table.txt, data/glossary.txt) ; N3 %s ; N4 %s' % (S['N3'][0], S['N4'][0]),
         '### COMPONENT 5 : the Pi-0-1 read (data/b643_pi01_attempts.txt)',
         '### COMPONENT 6 : the edition (data/b643_edition.json, data/b643_edition_diff.txt) and the second reader (data/b643_reader_compare.txt)',
         '### COMPONENT 7 : the seal (data/b643_seal_hashes.json)',
         '### COMPONENT 8 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'))]
    put_txt('b643_components.txt', L)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    e = _poss(e)
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE ENTRY -- NOTHING WRITTEN')
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    unread = [x for x in ('### NOT', 'None', '?;', ' ? ', '`?`', ' ? of 3') if x in e]
    outside = [n for n in OUTSIDE_NEEDLES if n in e]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s ; outside names %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN',
                                                                                         unread or 'NONE', outside or 'NONE'))
    if 'dry' in a:
        print(e)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread or outside:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b643_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    Q = R2._Q()
    e = _poss(_trail_text())
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE RECORD -- NOTHING WRITTEN')
    cells = predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    unread = [x for x in ('### NOT', 'None', '`?`') if x in e]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', unread or 'NONE'))
    if 'dry' in a:
        print(e[:7000])
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD())
    r = Q.append_to(Q.OT, e)
    put_json('b643_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD()), head=TRAIL_HEAD(), append=r))
    print('  OPEN_TRAILS record :%s' % jl('b643_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-08 by b643 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD())
    t = '\n%s %s\n' % (CORR_HEAD % rec_, CORRECTION)
    if 'dry' in a:
        print(t)
        return
    Q.guard_absent(Q.OT, CORR_HEAD % rec_)
    r = Q.append_to(Q.OT, t)
    put_json('b643_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


# ================================================================================ THE DISPATCHER
if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'answer_of', 'put_txt', 'put_json', 'act_from', 'READS', 'seal_hashes', 'n5',
                                                          'TRAIL_HEAD', 'root_banks', 'rows_of_table'):
        print('usage: b643_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
