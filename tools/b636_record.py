# -*- coding: utf-8 -*-
"""b636_record.py -- THE ACT'S RECORD TOOL, UNDER (R246). ### ONE SUBCOMMAND PER BANK.

### ### b636: LANE THREE, ACT SIXTY-THREE -- THE ELABORATED READER OVER SIDE-structural-error-correction AT v0.2.2, ITS ROWS GRADED WITH
### PROVENANCE, THE PHASE 2 ROWS RE-READ; THE NAME PATTERNS AND THE TAG MATCHER REPAIRED; THE SEAL'S HASH ARM.
### Subcommands write only `data/b636_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic
### helpers are b633's record tool's, imported; ledger appends through b566's guarded `append_to`. The data is tools/b636_worklist.py;
### the elaborated reader is tools/b634_elab.py, generalised at Component 3 to take the kernel. No platform is called; no registry is read;
### nothing deposits. b628's full intake bank is never read here, never staged or committed. A stand-in bank directory named by the
### environment variable B636_STANDIN is read before data/ by the record texts' dry runs alone (findings, trail, record_lines with `dry`).
"""
import collections
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b636_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/e1567886-3bd6-4471-9e29-3d65058acee0/scratchpad'
SESSION_ID = 'e1567886-3bd6-4471-9e29-3d65058acee0'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b636_registration_2026-10-07.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
put_txt, put_json, jx, _write, _scan, _clean = R3.put_txt, R3.put_json, R3.jx, R3._write, R3._scan, R3._clean
lines_of, count_cases, COUNT_CASE, _nd, predict_cells, _land = R3.lines_of, R3.count_cases, R3.COUNT_CASE, R3._nd, R3.predict_cells, R3._land
KERNS, KERN_PIN, kern_state, sorry_tokens = R3.KERNS, R3.KERN_PIN, R3.kern_state, R3.sorry_tokens
STANDIN = os.environ.get('B636_STANDIN') if ('dry' in sys.argv[2:]) else None


def _bank_path(name):
    if STANDIN and os.path.exists(os.path.join(STANDIN, name)):
        return os.path.join(STANDIN, name)
    return os.path.join(D, name)


def jl(name):
    try:
        return json.load(io.open(_bank_path(name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    try:
        return io.open(_bank_path(name), encoding='utf-8').read().replace(chr(13), '')
    except OSError:
        return ''


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b636_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b636 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b636_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b636_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table():
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


def _run_test(rel, bank, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b636 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel,
                                  failing=[re.match(r'^  (\(\d+\))', l).group(1) for l in out.split(NL)
                                           if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]))
    print(L[-1])


def _diff(path, rev, bank, title):
    old = (_show(RELAY, rev, path) or '').split(NL)
    new = io.open(os.path.join(ROOT, *path.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    dl = list(difflib.unified_diff(old, new, '%s@%s' % (os.path.basename(path), rev), os.path.basename(path), lineterm='', n=0))
    put_txt(bank, ['b636 -- %s, THE DIFF AGAINST relay %s (%s)' % (title, rev, utc()), ''] + dl)


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the lines the ferry names, the standing lines the act addresses, b635`s weight line, record and correction', PP, PRE_PP,
         'OPEN_TRAILS.md', [11864, 12228, 12354, K.BUILD_CLAUSE, 12799, K.MANIFEST_LINE, K.GATE_WO, K.BINDER_GRAMMAR, K.BUILD_ROUTE, K.HEADLINE,
                            13279, K.B635_RECORD, K.B635_CORRECTION], 1500),
        ('FINDINGS: b635`s weight line on b634 and b635`s entry', PP, PRE_PP, 'FINDINGS.md', [7769, K.B635_ENTRY], 600),
        ('relay tools/b634_elab.py: its constants, its worklist import and its functions', RELAY, PRE_RELAY, 'tools/b634_elab.py',
         ('GREP', r'^(import b634_worklist|SP = |WORK = |RUNS = |TYPES = |VENDOR = |def \w+)'), 200),
        ('relay tools/test_elab_reader_b634.py: its cases and its call', RELAY, PRE_RELAY, 'tools/test_elab_reader_b634.py',
         ('GREP', r'^(###   \(\d\)|PR = |NAMES = |EXTRA = |    c = EL\.call)'), 200),
        ('relay data/b634_elab_types.txt: its form (the header lines and one block)', RELAY, PRE_RELAY, 'data/b634_elab_types.txt',
         ('BLOCK', K.CHI_TAIL), 300),
        ('SIDE-structural-error-correction at the pin: lakefile.toml', K.KER, K.KER_PIN, 'lakefile.toml', ('GREP', r'.'), 200),
        ('SIDE-structural-error-correction at the pin: lake-manifest.json', K.KER, K.KER_PIN, 'lake-manifest.json', ('GREP', r'.'), 200),
        ('SIDE-structural-error-correction at the pin: lean-toolchain', K.KER, K.KER_PIN, 'lean-toolchain', ('GREP', r'.'), 200),
        ('SIDE-structural-error-correction at the pin: the root module (its module list)', K.KER, K.KER_PIN, 'SIDEStructuralErrorCorrection.lean',
         ('GREP', r'.'), 200),
        ('SIDE-structural-error-correction at the pin: AxiomCheck.lean`s prints', K.KER, K.KER_PIN, 'AxiomCheck.lean', ('GREP', r'^#print axioms'), 200),
        ('SIDE-structural-error-correction at the pin: Basic.lean`s theorem statements', K.KER, K.KER_PIN, 'SIDEStructuralErrorCorrection/Basic.lean',
         ('GREP', r'^\s*(theorem|lemma)\b'), 260),
        ('SIDE-structural-error-correction at the pin: DeAlignment.lean`s theorem statements', K.KER, K.KER_PIN,
         'SIDEStructuralErrorCorrection/DeAlignment.lean', ('GREP', r'^\s*(theorem|lemma)\b'), 260),
        ('relay data/terminal_table.json at 1bc734d5: the kernel`s rows with grade and provenance', RELAY, '1bc734d5', 'data/terminal_table.json',
         ('TABLE', K.KERNEL), 260),
        ('PLACE-papers the census at v0.5: the SEC row of §1A and §1C, the Phase 2 rows with their printed reasons', PP, PRE_PP, K.CEN5,
         [K.CEN5_SEC_ROW] + list(range(K.CEN5_1C, K.CEN5_1C + 11)), 1400),
        ('relay tools/chain_page.py: NAME_RE and PRINT_SRC (the ferry`s file)', RELAY, PRE_RELAY, 'tools/chain_page.py', ('GREP', r'NAME_RE|PRINT_SRC'), 200),
        ('relay tools/terminal_table.py: NAME_RE and PRINT_SRC (where they are)', RELAY, PRE_RELAY, 'tools/terminal_table.py',
         ('GREP', r'^(NAME_RE = |PRINT_SRC = )'), 200),
        ('relay data/b635_phantom_names.txt: the thirteen names', RELAY, PRE_RELAY, 'data/b635_phantom_names.txt', ('GREP', r'^  \S'), 200),
        ('relay tools/b635_record.py: the deposit bank`s tag matcher', RELAY, PRE_RELAY, 'tools/b635_record.py',
         ('GREP', r'^def registry_tags|tags = set\(re\.findall|for k, tg in registry_tags'), 200),
        ('PLACE-papers REGISTRY.md :705', PP, PRE_PP, 'REGISTRY.md', [705], 1200),
        ('relay tools/b635_checks.py: the suite`s seal step', RELAY, PRE_RELAY, 'tools/b635_checks.py',
         ('GREP', r"reg_seal\.py'\), '--verify'|'G-SEAL-VERIFIES'|'G-REG-LOCKED-FIRST'"), 220),
        ('relay tools/b635_closing.py: the carried closing sentence', RELAY, PRE_RELAY, 'tools/b635_closing.py', ('GREP', r'outbound request'), 300),
        ('relay data/b635_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b635_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    L = ['b636 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'TABLE':
            rows = [r for r in json.loads(t).get('rows', []) if r['repo'] == sel[1]]
            c = collections.Counter((r['grade'], r.get('provenance')) for r in rows)
            L.append('### %s -- %s @ %s (%d rows of %s ; by grade and provenance %s)' % (label, path, at, len(rows), sel[1], dict(c)))
            for r in rows:
                L.append('    %-62s %-12s %-6s %s' % (r['name'], r['grade'], r.get('provenance'), r.get('statement_state')))
            continue
        if isinstance(sel, tuple) and sel[0] == 'BLOCK':
            a0 = next((i for i, l in enumerate(sl) if l.startswith('DECL %s ' % sel[1])), None)
            b0 = next((i for i in range(a0 or 0, len(sl)) if sl[i] == 'END'), None) if a0 is not None else None
            nums = list(range(1, 5)) + (list(range(a0 + 1, b0 + 2)) if a0 is not None and b0 is not None else [])
        elif isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s ; the kernel HEAD: %s' % (
              g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), g(K.KER, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b636_reads.txt', L)


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R246) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b636 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b636_author_answers.txt', L)


def answer_of(k):
    R3.rd = lambda name: rd('b636_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b636_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ (R246)(3): THE SEAL'S HASHES
def seal_hashes():
    """### RETURN (recorded {tool: sha256}, now {tool: sha256}, [(tool, 'agree'|'differ'|'absent')]) -- data/b636_seal_hashes.json, written
    ### by the suite's `--seal` at the seal, against the tools on disk."""
    rec_ = jl('b636_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b636 -- (R246)(3): THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b636_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES
W_HEAD = '*Appended 2026-10-07 by b636 to b635’s entry (:%d), under `(R246)`(1) -- b635 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
SEAL_HEAD = '*Appended 2026-10-07 by b636 beneath the build clause (:%d), under `(R246)`(3) -- THE SEAL, RESTATED, STANDING:*'


def _weight():
    AG, PH, TE = jl('b635_agree.json'), jl('b635_phantom_names.json'), jl('b635_table_elab.json')
    MJ, AR, DJ = jl('b635_mirror.json'), jl('b635_act_root.json'), jl('b635_deposit_items.json')
    RB = jl('b635_rebuild.json')
    c = collections.Counter(x['kind'] for x in PH.get('names') or [])
    tags = [x for x in DJ.get('tags') or []]
    return ('\n%s the elaborated reading applied to the explicit-formula kernel’s table rows, %d grades moving and the eleven agreeing at the '
            'rerun, %d of %d; the textual rule repaired on three patterns (type_of%% deferred, two levels of nesting, qualified class names); '
            'the thirteen names %d re-pointed and %d upstream; the 35 statement-less rows typed and graded, the upstream mark where a declaration '
            'lives outside the kernel; the table’s generator reading the elaborated bank with a retire list and a re-point map; the page printer '
            'printing any provenance as itself; both pages re-emitted from fresh probes, the ζ page corrected before any push. The cascade '
            'rebuilt, %d calls, 0 differences. The deposit bank: %d of %d items resolving, %d of %d tag pairs resolving, the one unresolved a '
            'prose version target the matcher read as a tag. The mirror %s, md5 %s, sha256 %s…, %d files and MANIFEST, its MANIFEST md5 %s carrying the line '
            '%s, clean on three clauses. Root b635 %s…%s; relay 1bc734d5, PLACE-papers 29eb4b3 and 07f4c43, closing 4b84f96d; the suite 75 of '
            '80, the five failing each in letter on a recorded cause; defects (a)-(n) the seat’s. Nothing deposited; no kernel source touched.\n'
            % (W_HEAD % K.B635_ENTRY, len(TE.get('grade_moved') or []), sum(1 for x in AG.get('rows') or [] if x['ok']), len(AG.get('rows') or []),
               c.get('TRUNCATED -> RE-POINTED', 0), c.get('UPSTREAM, OUTSIDE THE READER`S IMPORTS', 0), len(RB.get('calls') or []),
               sum(1 for x in DJ.get('items') or [] if x['ok']), len(DJ.get('items') or []), sum(1 for x in tags if x['ok']), len(tags),
               os.path.basename(MJ.get('zip', '?')), MJ.get('zip_md5', '?'), (MJ.get('zip_sha256') or '?')[:16], MJ.get('entries', 1) - 1,
               MJ.get('manifest_md5', '?'), '"%s…"' % (MJ.get('root_line') or '?')[:30], (AR.get('root') or '?')[:8], (AR.get('root') or '????')[-4:]))


def _seal_rule():
    return ('\n%s sealed means unedited by any means until the act closes; a text edit is an edit. At the seal the suite records the sha256 of '
            'every sealed tool; at the close an arm recomputes each and prints agree or differ per tool, a differ failing the arm whatever the '
            'edit touched; a sealed tool edited after the seal by any means is the arm’s catch and not the seat’s report. From b635’s defect '
            '(d), its sealed record tool’s text edited after the seal by string replacement (OPEN_TRAILS :%d).\n' % (SEAL_HEAD % K.BUILD_CLAUSE,
                                                                                                                  K.B635_CORRECTION))


def record_lines(*a):
    """### FINDINGS: b635's weight (to :7771). OPEN_TRAILS: the seal rule restated beneath the build clause (:12356)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The elaborated reading applied to ')
    if entry != K.B635_ENTRY:
        sys.exit('### b635`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B635_ENTRY, _weight()), ('OPEN_TRAILS.md', SEAL_HEAD % K.BUILD_CLAUSE, _seal_rule())]
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(allt, 'OPEN_TRAILS.md') + predict_cells(items[0][2], 'FINDINGS.md')
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; backtick parity odd in: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN',
                                                                                                  ticks or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean or ticks:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR ODD BACKTICKS -- NOTHING WRITTEN')
    _land(Q, items, 'b636_record_lines.json', K.B635_ENTRY)


# ================================================================================ THE ELABORATED READING (shared by the components)
def _elab_header(e):
    parts = []
    for b in e['binders']:
        if b['kind'] == 'explicit':
            parts.append('(%s : %s)' % (b['name'], b['type']))
        elif b['kind'] == 'implicit':
            parts.append('{%s : %s}' % (b['name'], b['type']))
        elif b['kind'] == 'strict-implicit':
            parts.append('⦃%s : %s⦄' % (b['name'], b['type']))
        else:
            parts.append('[%s]' % b['type'])
    return (' '.join(parts) + ' : ' + e['concl']).strip()


def elab_grade(e):
    import e0_rule as E
    return E.grade(_elab_header(e), 'theorem' if e['kind'] == 'theorem' else 'def')[:2]


def binder_class(b, hdr):
    """### one binder of an elaborated header, read under the criterion ((R235)(2)) as the shared rule reads it: RETURN (class, why)."""
    import e0_rule as E
    t = b['type']
    if b['kind'] == 'instance':
        return (('premise', 'a Fact instance (the rule`s INSTANCE)') if re.match(r'^\s*Fact\b', t) else
                ('domain condition (i)', 'an instance binder whose class is not Fact'))
    if b['kind'] != 'explicit':
        return 'object', 'an implicit binder: an object of the statement, not a hypothesis the rule reads'
    if E.data_binder(t):
        return 'object', 'a data binder (its type is no Prop)'
    if not re.match(r'^h\w*$', b['name'].rstrip('✝')):
        return 'not read', 'the rule`s binder pattern reads hypothesis binders named h…; this one is named %s' % b['name']
    if E.domain_case(t, hdr):
        return 'domain condition', 'the rule`s domain case holds (DOMAIN, a split, a class predicate, a restriction on a bound variable)'
    if E.unlisted_case(t, hdr):
        return 'predicate unlisted', 'a named predicate on the statement`s quantified variables, neither listed nor met'
    return 'premise', 'a Prop the criterion names in none of its domain conditions (membership, non-membership, non-emptiness, finiteness; ' \
                      'support, parity, smoothness, continuity, integrability; a real`s positivity; a natural`s bound)'


def chitail(*a):
    """### (R246)(2)(i): chi_Tail_TailHyp_traceNorm_smul_Ez_le's elaborated type (data/b634_elab_types.txt), every binder printed with its
    ### class under the criterion, the binder the old reader dropped named; the move DERIVES -> INTERFACES stands if that binder is a premise
    ### and reverts to DERIVES if it is a domain condition the criterion names; the table row's grade and provenance printed."""
    import b634_elab as EL
    import e0_rule as E
    B = EL.parse(io.open(os.path.join(D, 'b634_elab_types.txt'), encoding='utf-8').read())
    e = B[K.CHI_TAIL]
    hdr = _elab_header(e)
    T = {r['name']: r for r in _table() if r['repo'] == K.EF_KERNEL}
    row = T.get(K.CHI_TAIL, {})
    L = ['b636 -- COMPONENT 1, (R246)(2)(i): %s, ITS BINDERS UNDER THE CRITERION (%s)' % (K.CHI_TAIL, utc()), '',
         '### its elaborated type, relay data/b634_elab_types.txt (b634`s reader at SIDE-explicit-formula v0.25 = 8c51431):', '']
    cls = []
    for b in e['binders']:
        c, why = binder_class(b, hdr)
        cls.append(dict(kind=b['kind'], name=b['name'], type=b['type'], cls=c, why=why))
        L.append('  %-15s %-6s : %-60s -> %s -- %s' % (b['kind'], b['name'], b['type'][:60], c.upper(), why))
    L += ['  CONCL %s' % e['concl'], '']
    old = re.compile(r'\((h\w*) : ([^()]*(?:\([^()]*\)[^()]*)*)\)')        # ### the binder pattern before b635's repair (one nesting level)
    old_names = set(m.group(1) for m in old.finditer(hdr))
    new_names = set(m.group(1) for m in E.BINDER.finditer(hdr))
    dropped = sorted(new_names - old_names)
    hm = next((x for x in cls if x['name'] == K.CHI_TAIL_BINDER), None)
    ruled = 'INTERFACES' if hm and hm['cls'] == 'premise' else 'DERIVES'
    gnow = elab_grade(e)
    L += ['### the binders the old pattern read %s ; the repaired pattern reads %s ; dropped by the old and read now: %s' % (
        sorted(old_names), sorted(new_names), dropped),
          '### %s : %s -- its class under the criterion: %s; the conclusion uses it (traceNorm %s), the operator`s own argument' % (
              K.CHI_TAIL_BINDER, hm['type'] if hm else '?', (hm or {}).get('cls', '?').upper(), K.CHI_TAIL_BINDER),
          '### the repaired rule on the elaborated header: %s -- %s' % gnow,
          '### the table at relay HEAD: %s at provenance %s%s' % (row.get('grade'), row.get('provenance'), (' ; mark ' + row['mark']) if row.get('mark') else ''),
          '', '### ### **RULED UNDER (R246)(2)(i): %s -- %s ; THE TABLE %s.**' % (
              ruled, 'the move stands, the binder a premise' if ruled == 'INTERFACES' else 'the move reverts, the binder a domain condition the criterion names',
              'AGREES, NOTHING REGENERATED' if row.get('grade') == ruled else 'TO BE REGENERATED')]
    put_txt('b636_chitail.txt', L)
    put_json('b636_chitail.json', dict(at=utc(), name=K.CHI_TAIL, binders=cls, dropped=dropped, binder=K.CHI_TAIL_BINDER,
                                       binder_class=(hm or {}).get('cls'), ruled=ruled, rule_now=list(gnow), table=row.get('grade'),
                                       provenance=row.get('provenance'), stands=(ruled == 'INTERFACES')))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE KERNEL'S STATE
def modules():
    fs = [f for f in g(K.KER, 'ls-tree', '-r', '--name-only', K.KER_PIN).split(NL) if f.endswith('.lean')]
    return sorted(f[:-5] for f in fs if f.split('/')[0].split('.')[0] in K.KER_ROOTS)


def _olean(m):
    return os.path.join(K.KER, '.lake', 'build', 'lib', 'lean', *(m + '.olean').split('/'))


def kstate(*a):
    """### (R246)(4) and Component 2: the checkout at the pin and clean; every module's olean present or absent, printed; `lake build
    ### --no-build` read, which compiles nothing; more than ten absent a HOLD with the list banked (data/b636_kernel_state.txt and its json)."""
    head = g(K.KER, 'rev-parse', 'HEAD').strip()
    st = g(K.KER, 'status', '--porcelain', '--untracked-files=no').strip()
    ms = modules()
    pres = {m: os.path.exists(_olean(m)) for m in ms}
    fm = R2.free_mb()
    t0 = time.time()
    try:
        r = subprocess.run(['lake', 'build', '--no-build'], cwd=K.KER, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=540)
        nb_rc, nb_out = r.returncode, (r.stdout or '') + (r.stderr or '')
    except subprocess.TimeoutExpired:
        nb_rc, nb_out = 'TIMEOUT', ''
    secs = int(time.time() - t0)
    absent = [m for m in ms if not pres[m]]
    verdict = 'HOLD' if len(absent) > K.HOLD_ABOVE else ('NOTHING TO BUILD' if not absent else 'BUILD %d BY THE STANDING ROUTE' % len(absent))
    L = ['b636 -- COMPONENT 2: THE KERNEL`S STATE, %s AT %s = %s (%s)' % (K.KERNEL, K.KER_TAG, K.KER_PIN, utc()), '',
         '### checkout HEAD %s ; at the pin %s ; tracked changes %s' % (head[:12], head == K.KER_PIN_FULL, st or 'NONE'),
         '### modules at the pin: %d ; oleans present %d ; absent %d %s ; free memory %d MB' % (len(ms), len(ms) - len(absent), len(absent), absent or '', fm),
         '### `lake build --no-build` (compiles nothing): exit %s in %d s ; its last lines:' % (nb_rc, secs)]
    L += ['    ' + l for l in nb_out.rstrip(NL).split(NL)[-12:]]
    L += ['', '### PER MODULE:'] + ['    %-8s %s' % ('present' if pres[m] else 'ABSENT', m) for m in ms]
    L += ['', '### ### **%s.**' % verdict]
    put_txt('b636_kernel_state.txt', L)
    put_json('b636_kernel_state.json', dict(at=utc(), head=head, at_pin=(head == K.KER_PIN_FULL), clean=not st, modules=ms, absent=absent,
                                            nobuild_rc=nb_rc, nobuild_secs=secs, nobuild_tail=nb_out.rstrip(NL).split(NL)[-12:], verdict=verdict))
    print(NL.join(L[2:5])); print(L[-1])


def build(m, *a):
    """### ONE module by the standing route's first step (OPEN_TRAILS :13167): `lake build <module>` in the kernel, the free memory read
    ### before it against the hold and sampled every 2 s; run as a detached process by the seat; banked as it lands (data/b636_build.json)."""
    fm = R2.free_mb()
    J = jl('b636_build.json') or dict(calls=[])
    if 0 <= fm < K.HOLD_MB:
        J['calls'].append(dict(module=m, free_before=fm, started=False, at=utc()))
        put_json('b636_build.json', J)
        sys.exit('### BENEATH THE HOLD (%d MB) -- NOT STARTED' % fm)
    log = os.path.join(SP, 'b636_build_%s.log' % re.sub(r'\W+', '_', m))
    t0, low = time.time(), fm
    with open(log, 'wb') as fo:
        p = subprocess.Popen(['lake', 'build', m.replace('/', '.')], cwd=K.KER, stdout=fo, stderr=subprocess.STDOUT)
        while p.poll() is None:
            time.sleep(2)
            f = R2.free_mb()
            if f >= 0:
                low = min(low, f)
    J['calls'].append(dict(module=m, free_before=fm, started=True, rc=p.returncode, seconds=int(time.time() - t0), low=low, at=utc(),
                           olean=os.path.exists(_olean(m)), tail=open(log, 'rb').read().decode('utf-8', 'replace').rstrip(NL).split(NL)[-6:]))
    put_json('b636_build.json', J)
    print('### EXIT %s ; %d s ; lowest %d MB' % (p.returncode, int(time.time() - t0), low))


# ================================================================================ COMPONENT 3: THE READER
def reader_test(*a):
    """### the reader's generalisation: tools/b634_elab.py against relay 4b84f96d, and tools/test_elab_reader_b634.py run and counted --
    ### its six cases and the SEC declaration of known type."""
    _diff('tools/b634_elab.py', PRE_RELAY, 'b636_reader_diff.txt', 'THE READER GENERALISED TO TAKE THE KERNEL, tools/b634_elab.py')
    _diff('tools/test_elab_reader_b634.py', PRE_RELAY, 'b636_reader_test_diff.txt', 'THE READER`S TEST EXTENDED, tools/test_elab_reader_b634.py')
    _run_test('tools/test_elab_reader_b634.py', 'b636_reader_test')


def _sec_types():
    import b634_elab as EL
    return EL.parse(rd(K.ELAB_BANK))


def types_count(*a):
    """### H70a: the kernel's declarations typed in data/b636_elab_sec.txt against the table's rows of the kernel and the ruling's 62."""
    B = _sec_types()
    T = [r for r in _table() if r['repo'] == K.KERNEL]
    typed = sorted(n for n, e in B.items() if not e['missing'])
    miss = sorted(n for n, e in B.items() if e['missing'])
    notread = sorted(r['name'] for r in T if r['name'] not in B)
    L = ['b636 -- COMPONENT 3, H70a: THE KERNEL`S DECLARATIONS TYPED (%s)' % utc(), '',
         '### the table`s rows of %s : %d (the ruling`s %d) ; typed %d ; MISSING %d %s ; rows the bank does not name %d %s' % (
             K.KERNEL, len(T), K.N_DECLS, len(typed), len(miss), miss or '', len(notread), notread or ''),
         '### by kind: %s' % dict(collections.Counter(B[n]['kind'] for n in typed)),
         '', '### ### **A TYPE FOR %d OF THE %d DECLARATIONS.**' % (sum(1 for r in T if r['name'] in typed), len(T))]
    put_txt('b636_types_count.txt', L)
    put_json('b636_types_count.json', dict(at=utc(), rows=len(T), typed=len(typed), missing=miss, notread=notread,
                                           all_typed=(len(T) == K.N_DECLS and not miss and not notread)))
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 4: THE TWO READINGS
def _module_vars(module):
    t = _show(K.KER, K.KER_PIN, module + '.lean') or ''
    out = set()
    for m in re.finditer(r'^variable\b(.*?)(?=^\S)', t + NL + 'x', re.M | re.S):
        out |= set(re.findall(r'[({\[⦃]\s*([^:(){}\[\]⦃⦄]+?)\s*:', m.group(1)))
    names = set()
    for grp in out:
        names |= set(grp.split())
    return names


def _text_binders(head):
    import e0_rule as E
    h2 = E.statement_only(head or '')
    return [mm.groups() for mm in E.BINDER.finditer(h2)], h2 != (head or '')


def classify(row, e, tgrade, egrade):
    """### b634's classifier (relay tools/b634_record.py :396), carried with this kernel's sources: section variable, auto-bound implicit,
    ### header cut, notation or coercion, other ((R244)(4), in its order; the first that holds)."""
    from b632_record import rule_full
    _k, _g, _w, _p, head = rule_full(row.get('statement'), row['name'])
    tb, cut = _text_binders(head)
    tnames = set(b for b, _t in tb)
    ehyp = [b for b in e['binders'] if b['kind'] == 'explicit' and re.match(r'h\w*$', b['name'])]
    extra = [b['name'] for b in ehyp if b['name'] not in tnames]
    mod = (row.get('statement_file') or '').split(':')[0][:-5]
    sv = _module_vars(mod) if mod else set()
    if extra and any(x in sv for x in extra):
        return 'section variable', 'the elaborated type carries %s, which the module`s variable command binds and the textual header does not' % (
            [x for x in extra if x in sv])
    tbound = set(re.findall(r"[^\W\d][\w'₀-₉]*", ' '.join(re.findall(r'[({⦃]\s*([^:(){}⦃⦄]+?)\s*:', (head or '').split(' : ')[0]))))
    auto = [b['name'] for b in e['binders'] if b['kind'] == 'implicit' and b['name'] not in tbound and not b['name'].endswith('✝')
            and re.search(r'(?<![\w.])%s(?![\w])' % re.escape(b['name']), head or '')]
    if auto:
        return 'auto-bound implicit', 'implicit binders %s are bound in the elaborated type and free in the textual header' % auto
    if cut or e.get('opened') or len(ehyp) != len(tb):
        return 'header cut', 'the textual header %s; the elaborated header carries %d hypothesis binders against the text`s %d' % (
            'is cut where a proof begins' if cut else 'is read whole', len(ehyp), len(tb))
    if [b for b, _t in tb] == [b['name'] for b in ehyp]:
        return 'notation or coercion', 'the same hypothesis binders, their types printed differently: %s' % '; '.join(
            '%s : %s || %s' % (b, ' '.join(t.split())[:80], x['type'][:80]) for (b, t), x in zip(tb, ehyp) if ' '.join(t.split()) != x['type'])[:600]
    return 'other', 'binders text %s against elaborated %s; textual %s, elaborated %s' % ([b for b, _t in tb], [b['name'] for b in ehyp], tgrade, egrade)


def readings(*a):
    """### Component 4: every declaration of the kernel with its textual grade, its elaborated grade and their agreement
    ### (data/b636_two_readings_sec.txt); the disagreements classed (data/b636_gate_disagreements_sec.txt and their json)."""
    from b632_record import rule_full
    T = [r for r in _table() if r['repo'] == K.KERNEL]
    ET = _sec_types()
    rows, dis = [], []
    for r in T:
        e = ET.get(r['name'])
        _k, tg, _why, _p, _h = rule_full(r.get('statement'), r['name']) if r.get('statement') else (None, None, '', [], '')
        tg = tg or 'UNREAD'
        eg, ew = ('NO TYPE', '') if (e is None or e.get('missing')) else elab_grade(e)
        agree = tg == eg
        rows.append(dict(name=r['name'], provenance=r.get('provenance'), table=r['grade'], textual=tg, elaborated=eg, agree=agree,
                         kind=(e or {}).get('kind')))
        if not agree and tg != 'UNREAD' and eg != 'NO TYPE':
            cl, why = classify(r, e, tg, eg)
            dis.append(dict(name=r['name'], provenance=r.get('provenance'), table=r['grade'], textual=tg, elaborated=eg, cls=cl, why=why,
                            header=_elab_header(e), statement=' '.join((r.get('statement') or '').split())[:600]))
    both = [x for x in rows if x['textual'] != 'UNREAD' and x['elaborated'] != 'NO TYPE']
    ag = sum(1 for x in both if x['agree'])
    L = ['b636 -- COMPONENT 4: THE TWO READINGS OF %s AT %s, EVERY DECLARATION (%s)' % (K.KERNEL, K.KER_TAG, utc()), '',
         '### declarations %d ; read by both %d ; agreeing %d = %.4f ; textual unread (no statement) %d %s ; elaborated no type %d' % (
             len(rows), len(both), ag, (ag / len(both)) if both else 0, sum(1 for x in rows if x['textual'] == 'UNREAD'),
             [x['name'] for x in rows if x['textual'] == 'UNREAD'], sum(1 for x in rows if x['elaborated'] == 'NO TYPE')), '']
    L += ['  %-5s %-62s table %-12s textual %-12s elaborated %-12s %s' % (x['provenance'], x['name'][:62], x['table'], x['textual'], x['elaborated'],
                                                                        'AGREE' if x['agree'] else ('UNREAD' if x['textual'] == 'UNREAD' else 'DIFFER'))
          for x in rows]
    put_txt('b636_two_readings_sec.txt', L)
    put_json('b636_two_readings_sec.json', dict(at=utc(), rows=rows, both=len(both), agree=ag, ratio=(ag / len(both)) if both else 0))
    cc = collections.Counter(x['cls'] for x in dis)
    D_ = ['b636 -- COMPONENT 4: THE DISAGREEMENTS OF %s, CLASSED (%s)' % (K.KERNEL, utc()), '',
          '### ### **DISAGREEMENTS : %d ; BY CLASS : %s ; OUTSIDE THE FIVE : %d.**' % (len(dis), dict((c, cc.get(c, 0)) for c in K.CLASSES),
                                                                                       sum(1 for x in dis if x['cls'] not in K.CLASSES)), '']
    for c in K.CLASSES:
        D_ += ['### CLASS: %s (%d)' % (c, cc.get(c, 0))]
        for x in [y for y in dis if y['cls'] == c]:
            D_ += ['  %s (%s) :: table %s ; textual %s ; elaborated %s' % (x['name'], x['provenance'], x['table'], x['textual'], x['elaborated']),
                   '      why: %s' % x['why'], '      elaborated: %s' % x['header'][:600], '      textual:    %s' % x['statement']]
        D_.append('')
    put_txt(K.DISAGREE_BANK, D_)
    put_json(K.DISAGREE_BANK.replace('.txt', '.json'), dict(at=utc(), disagreements=dis, by_class=dict(cc)))
    print(L[2]); print(D_[2])


def gen_test(*a):
    """### the generator's edit for this kernel: tools/terminal_table.py against relay 7b5bea0b (the step-zero repair's blob), and
    ### tools/test_terminal_table_b636.py run and counted."""
    _diff('tools/terminal_table.py', K.REPAIRS[0], 'b636_gen_diff.txt', 'THE GENERATOR`S ELABORATED READING EXTENDED TO %s' % K.KERNEL)
    _run_test('tools/test_terminal_table_b636.py', 'b636_gen_test')


def _table_state():
    out = {}
    for r in _table():
        out.setdefault((r['repo'], r['name']), (r['grade'], r.get('provenance'), r.get('mark') or ''))
    return out


def table(*a):
    """### the terminal table regenerated; the kernel's rows printed before and after; every row whose grade, provenance or mark moved
    ### printed, each with its cause -- the kernel's elaborated reading, the step-zero name patterns (data/b636_namepat_table.txt), other."""
    before = _table_state()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _table_state()
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    np_ = rd('b636_namepat_table.txt')

    def cause(k):
        if k[0] == K.KERNEL:
            return 'the kernel`s elaborated reading'
        return 'the name patterns' if ('  %s|%s ' % k) in np_ else 'other'
    tag = a[0] if a and a[0] != 'dry' else 'sec'
    files = [f for f in K.TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    sec_b = sorted((k[1], before[k]) for k in before if k[0] == K.KERNEL)
    sec_a = sorted((k[1], after[k]) for k in after if k[0] == K.KERNEL)
    L = ['b636 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade, provenance or mark moved %d ; the table files that moved against relay HEAD: %s' % (
             len(added), len(gone), len(moved), files or 'NONE'),
         '### by cause: %s' % dict(collections.Counter(cause(k) for k in moved + added + gone)),
         '### the kernel`s rows by provenance, before %s ; after %s' % (dict(collections.Counter(v[1] for _n, v in sec_b)),
                                                                       dict(collections.Counter(v[1] for _n, v in sec_a))), '']
    L += ['### THE KERNEL`S ROWS, BEFORE AND AFTER:'] + ['  %-62s %-40s -> %s' % (n, before[(K.KERNEL, n)], after.get((K.KERNEL, n))) for n, _v in sec_b]
    L += ['', '### EVERY MOVE:']
    L += ['  MOVED %s / %-62s %s -> %s  [%s]' % (k[0], k[1], before[k], after[k], cause(k)) for k in moved]
    L += ['  ADDED %s / %-62s %s  [%s]' % (k[0], k[1], after[k], cause(k)) for k in added]
    L += ['  GONE  %s / %-62s %s  [%s]' % (k[0], k[1], before[k], cause(k)) for k in gone]
    L += ['', '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; THE KERNEL`S ROWS AT rule-elab %d.**' % (
        len(moved), len(added), len(gone), sum(1 for _n, v in sec_a if v[1] == 'rule-elab'))]
    if r.returncode:
        L += ['### THE GENERATOR EXITED %d:' % r.returncode] + (r.stdout + r.stderr).rstrip(NL).split(NL)[-15:]
    name = 'b636_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, moved=[[k[0], k[1], list(before[k]), list(after[k])] for k in moved],
                                                 added=[list(k) for k in added], gone=[list(k) for k in gone], files_moved=files,
                                                 grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]],
                                                 causes={'%s|%s' % k: cause(k) for k in moved + added + gone},
                                                 sec_rule_elab=sum(1 for _n, v in sec_a if v[1] == 'rule-elab'),
                                                 sec_after={n: list(v) for n, v in sec_a}))
    print(L[2]); print(L[3]); print(L[4]); print(L[-1])


# ================================================================================ COMPONENT 5: THE PHASE 2 ROWS
def _census_reasons():
    t = K.show(K.CEN5) or ''
    out = {}
    for l in t.split(NL):
        m = re.match(r'^\| (R\d\d) \| (\S+) `([^`]+)` \| ([^|]+) \| (.*) \|$', l)
        if m and m.group(1) in K.PHASE2_ROWS:
            out[m.group(1)] = dict(key=m.group(2), path=m.group(3), named=m.group(4).strip(), why=m.group(5).strip())
    sec_row = (lines_of(t)[K.CEN5_SEC_ROW - 1] if len(lines_of(t)) >= K.CEN5_SEC_ROW else '')
    return out, sec_row


def phase2(*a):
    """### Component 5, (R246)(4): the census's SEC row and its Phase 2 rows (§1C) re-read under the elaborated grades -- the census's two
    ### matchers (relay tools/b633_census.py sec_against_phase2: each theorem's short name as an identifier and read as words) run again at
    ### PLACE-papers 07f4c43 against the kernel's theorems as the table now holds them, every hit printed with the seat's reading and the
    ### terminal's elaborated grade; a row naming one of the terminals by statement under the elaborated reading printed as the bookend's
    ### trigger. Banked as data/b636_phase2_read.txt and its json; no census edition."""
    import b633_census as C33
    C33.K.show = lambda path, rev=PRE_PP, repo=PP: K.show(path, rev, repo)
    rows = _table()
    res = C33.sec_against_phase2(rows)
    ET = _sec_types()
    sec = {r['name'].split('.')[-1]: r for r in rows if r['repo'] == K.KERNEL}
    reasons, sec_row = _census_reasons()
    pv = collections.Counter(r.get('provenance') for r in rows if r['repo'] == K.KERNEL)
    L = ['b636 -- COMPONENT 5: THE CENSUS`S SEC ROW AND ITS PHASE 2 ROWS RE-READ UNDER THE ELABORATED GRADES (%s)' % utc(), '',
         '### §1A, the census at v0.5 :%d, as printed: %s' % (K.CEN5_SEC_ROW, sec_row),
         '### the kernel`s table rows now, by provenance: %s ; the census printed cell / rule / none as its last cell' % dict(pv),
         '### the kernel`s theorems the matchers read: %d (the census`s 34) ; their heads %s' % (res['theorems'], res['heads']), '']
    out, trig = [], []
    for x in res['rows']:
        cen = reasons.get(x['row'], {})
        hits = []
        for h in x['hits']:
            r = sec.get(h['name'], {})
            e = ET.get(r.get('name', ''))
            eg = elab_grade(e)[0] if e and not e['missing'] else 'NO TYPE'
            names_it = h['reading'] == 'UNREAD'
            hits.append(dict(h, elaborated=eg, table=r.get('grade'), provenance=r.get('provenance'), names_terminal=names_it))
            if names_it:
                trig.append((x['row'], h['name'], eg))
        named_now = [h['name'] for h in hits if h['names_terminal']]
        unchanged = (cen.get('named') == 'none' and not named_now)
        out.append(dict(row=x['row'], key=x['key'], path=x['path'], sec_mentions=x['sec_mentions'], hits=hits, census_named=cen.get('named'),
                        census_why=cen.get('why'), named_now=named_now, unchanged=unchanged))
        L += ['### %s %s `%s`' % (x['row'], x['key'], x['path']),
              '    the census at v0.5 printed: named %s -- %s' % (cen.get('named'), cen.get('why')),
              '    the matchers now: SEC repository or module mentions %d ; hits %d' % (x['sec_mentions'], len(hits))]
        L += ['      %s : identifier at %s ; as words at %s ; elaborated %s ; table %s (%s) ; the reading: %s' % (
            h['name'], h['ident'] or '-', h['phrase'] or '-', h['elaborated'], h['table'], h['provenance'], h['reading']) for h in hits]
        L += ['    ### re-read: %s' % ('UNCHANGED -- no SEC terminal named by statement' if unchanged else
                                       'CHANGED -- the terminal(s) named: %s' % named_now), '']
    L += ['### ### **ROWS RE-READ %d ; UNCHANGED %d ; TRIGGERS %d %s.**' % (len(out), sum(1 for x in out if x['unchanged']), len(trig), trig or '')]
    put_txt(K.PHASE2_BANK, L)
    put_json(K.PHASE2_BANK.replace('.txt', '.json'), dict(at=utc(), sec_row=sec_row, provenance_now=dict(pv), theorems=res['theorems'], rows=out,
                                                          triggers=[list(t_) for t_ in trig]))
    print(L[-1])


# ================================================================================ COMPONENT 5: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from b632's list and b635's probe in force (no Lean), written only where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = K.NODES[k], K.PROBE[k]
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b636_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b636_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = R3._grade_cells(prev.decode('utf-8')), R3._grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))
    kinds = collections.Counter(('correspondence row' if x[1:].startswith('|') else ('heading' if x[1:].startswith('#') else 'prose')) + x[0]
                                for x in dl)
    put_json('b636_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved,
                                           kinds=dict(kinds), free_mb_before=fm, seconds=secs, nodes=nl, probe=pr, at=utc(), dry=DRY))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d by kind %s ; cells moved %s' % (k, rc, changed, secs, len(dl), dict(kinds),
                                                                                                         gmoved or 'NONE'))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b636 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b636_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', K.NODES[k], r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
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
    put_txt('b636_page_arms.txt', L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 6: THE ROOT
ROOT_EXCLUDE = re.compile(r'^b636_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b636_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b636'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print(NL.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline; the chain's verify is read inside the suite alone."""
    import shutil
    import act_root as AR
    J = jl('b636_act_root.json')
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
    L = ['b636 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s)' % (
             bank_, r2, same, J['root']), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b636_root_arm.txt', L)
    put_json('b636_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', 'README.md', K.CEN4, K.CEN5, 'day1/A_Place_to_Stand_v5_18.md', K.SIEVE6)
HKEYS = ('H70a', 'H70b', 'H70c', 'H70d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b635_closing_push_out.txt', 'data/act_roots.txt', 'tools/terminal_table.py', 'tools/test_name_patterns_b636.py',
              'tools/b635_record.py', 'tools/test_registry_tags_b636.py', 'tools/b634_elab.py', 'tools/test_elab_reader_b634.py',
              'tools/test_terminal_table_b636.py'}


def n5(trail_line=None, ot=None, *a):
    """### (R246)'s N5, the file-set by PATH; no sealed tool's hash differs; the kernels untouched; nothing deposits."""
    if isinstance(trail_line, str):
        trail_line = int(trail_line.split('=')[-1])
    ot_text = ot if ot is not None else io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ot_lines = lines_of(ot_text)
    if trail_line is None:
        rec_ok, rec_state = False, 'no expected line given'
    elif len(ot_lines) >= trail_line and ot_lines[trail_line - 1] == TRAIL_HEAD:
        rec_ok, rec_state = True, 'the trail record written at :%d' % trail_line
    elif TRAIL_HEAD not in ot_text and len(ot_lines) < trail_line:
        rec_ok, rec_state = True, 'the trail record pending at :%d (the trails end at :%d)' % (trail_line, len(ot_lines))
    else:
        rec_ok, rec_state = False, 'the trail record neither at :%s nor pending' % trail_line
    face = jl('b636_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in ('FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE)]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b636_|audit_b636_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not tracked_local and untracked_local and not differ
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel`s tracked tree unmoved against the face %s; PLACE-papers %s (beyond the ledgers and the pages: %s); %s; '
            'relay beyond the list, matched by path: %s; the sealed tools` hashes not agreeing %s; b628`s local intake bank in any relay commit %s, '
            'untracked now %s; no identifier of the author in any outbound request' % (kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE',
                                                                                      differ or 'NONE', tracked_local, untracked_local))


def _pass_line(bank, n):
    return ('### ### **%d of %d cases as wanted -- PASS**' % (n, n)) in rd(bank)


def scores(*a):
    TC, TR, DG, P2 = jl('b636_types_count.json'), jl('b636_two_readings_sec.json'), jl(K.DISAGREE_BANK.replace('.txt', '.json')), jl(K.PHASE2_BANK.replace('.txt', '.json'))
    RT, KS, TF, RA = jl('b636_reader_test.json'), jl('b636_kernel_state.json'), jl('b636_table_final.json'), jl('b636_root_arm.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    a_ok = bool(TC) and TC.get('all_typed') is True
    ratio = TR.get('ratio', 0) if TR else 0
    b_ok = bool(TR) and ratio >= 0.95
    dis = DG.get('disagreements') or []
    c_ok = bool(DG) and all(x['cls'] in K.CLASSES for x in dis)
    rows = P2.get('rows') or []
    d_ok = bool(rows) and all(x['unchanged'] or x['named_now'] for x in rows)
    n4 = _pass_line('b636_namepat_test.txt', 7) and _pass_line('b636_tagmatch_test.txt', 5)
    _r, _n, sh = seal_hashes()
    S = {
        'H70a': (('HOLDS' if a_ok else 'REFUTED'), 'a type for %s of the table`s %s rows of the kernel (the ruling`s 62); MISSING %s (data/b636_types_count.txt)' % (
            TC.get('typed'), TC.get('rows'), TC.get('missing'))),
        'H70b': (('HOLDS' if b_ok else 'REFUTED'), 'agreement %s of %s read by both = %.4f (data/b636_two_readings_sec.txt)' % (TR.get('agree'), TR.get('both'), ratio)),
        'H70c': (('HOLDS' if c_ok else 'REFUTED'), '%d disagreements, by class %s, outside the five %d (data/%s)' % (
            len(dis), DG.get('by_class'), sum(1 for x in dis if x['cls'] not in K.CLASSES), K.DISAGREE_BANK)),
        'H70d': (('HOLDS' if d_ok else 'REFUTED'), 'the Phase 2 rows re-read: %d unchanged of %d, triggers %s (data/%s)' % (
            sum(1 for x in rows if x['unchanged']), len(rows), P2.get('triggers'), K.PHASE2_BANK)),
        'N1': (('HELD' if a_ok else 'REFUTED'), 'as H70a'),
        'N2': (('HELD' if b_ok else 'REFUTED'), 'as H70b'),
        'N3': (('HELD' if c_ok else 'REFUTED'), 'as H70c'),
        'N4': (('HELD' if n4 else 'REFUTED'), 'the thirteen names whole under the repaired patterns, 7 of 7 (data/b636_namepat_test.txt); :705`s sentence '
                                              'read as no tag, 5 of 5 (data/b636_tagmatch_test.txt): %s' % n4),
        'N5': n5v,
        'S1': (('HELD' if RT and RT.get('rc') == 0 and RT.get('passing') == RT.get('cases') and RT.get('cases', 0) >= 7 else 'REFUTED'),
               'the reader`s test %s of %s, its six cases and the kernel`s' % (RT.get('passing'), RT.get('cases'))),
        'S2': (('HELD' if KS and KS.get('absent') == [] and KS.get('at_pin') and KS.get('clean') else 'REFUTED'),
               'no olean absent at the pin: absent %s, at the pin %s, clean %s' % (KS.get('absent'), KS.get('at_pin'), KS.get('clean'))),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED'),
               'the table regenerated at the end moves %s rows' % len(TF.get('moved') or [])),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                            RA.get('root_copy') != RA.get('root') if RA else None)),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes at the record: %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    put_json('b636_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b636 — lane three, act sixty-three under (R246): the elaborated reader over SIDE-structural-error-correction at v0.2.2, its '
              'rows graded with provenance, the Phase 2 rows re-read; the name patterns and the tag matcher repaired; the seal’s hash arm')


def _figures():
    TC, TR, DG, P2, TS = (jl(n_) for n_ in ('b636_types_count.json', 'b636_two_readings_sec.json', K.DISAGREE_BANK.replace('.txt', '.json'),
                                            K.PHASE2_BANK.replace('.txt', '.json'), 'b636_table_sec.json'))
    dis = DG.get('disagreements') or []
    return dict(n=TC.get('rows', 0), r=TR.get('ratio', 0), d=len(dis), c=len(set(x['cls'] for x in dis)), m=TS.get('sec_rule_elab', 0),
                t=len(P2.get('triggers') or []), TC=TC, TR=TR, DG=DG, P2=P2, TS=TS)


def _title_entry():
    f = _figures()
    return ('## The elaborated reader over SIDE-structural-error-correction at v0.2.2: %d declarations, agreement %.4f, %d disagreements in %d '
            'classes, %d rows at rule-elab; the Phase 2 rows re-read, %d triggers; the name patterns and the tag matcher repaired; the seal’s '
            'hash arm' % (f['n'], f['r'], f['d'], f['c'], f['m'], f['t']))


def _finding_text():
    S, rl, J = jl('b636_scores.json'), jl('b636_record_lines.json'), jl('b636_act_root.json')
    f = _figures()
    KS, CT, NP = jl('b636_kernel_state.json'), jl('b636_chitail.json'), jl('b636_table_sec.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b636_author_answers.txt'), re.M))
    t = _title_entry()
    causes = collections.Counter((NP.get('causes') or {}).values())
    e = ['', t, '',
         '*Filed at b636 on the author’s ruling `(R246)`%s. Banks: relay `data/b636_elab_sec.txt`, `data/b636_two_readings_sec.txt`, '
         '`data/b636_gate_disagreements_sec.txt`, `data/b636_table_sec.txt`, `data/b636_phase2_read.txt`, `data/b636_chitail.txt`, '
         '`data/b636_act_root.txt`. Nothing deposits.*' % ((' and the author’s %d answers' % n_ans) if n_ans else ''), '',
         '**The kernel’s state** (Component 2): the checkout at %s = %s, clean; %d modules, oleans absent %s; lake reading every target up to date '
         'without building (exit %s).' % (K.KER_TAG, K.KER_PIN, len(KS.get('modules') or []), KS.get('absent'), KS.get('nobuild_rc')), '',
         '**The reader** (Component 3): relay tools/b634_elab.py takes the kernel as an argument, its test extended by one declaration of this '
         'kernel; one module per call, detached, the free memory read before each; a type for %s of the table’s %s rows. H70a %s.' % (
             f['TC'].get('typed'), f['TC'].get('rows'), S.get('H70a', ['?'])[0]), '',
         '**The two readings** (Component 4): the textual and the elaborated grades agree on %s of %s read by both, %.4f; %d disagreements, by '
         'class %s. H70b %s, H70c %s.' % (f['TR'].get('agree'), f['TR'].get('both'), f['r'], f['d'], f['DG'].get('by_class'),
                                          S.get('H70b', ['?'])[0], S.get('H70c', ['?'])[0]), '',
         '**The table**: the generator’s elaborated reading extended to this kernel with a test; %d of its rows at provenance rule-elab, the rest '
         'as the textual reading agrees; every move printed with its cause, %s.' % (f['m'], dict(causes)), '',
         '**The Phase 2 rows** (Component 5): the census’s SEC row and R12, R14, R16 and R17 re-read under the elaborated grades by the census’s '
         'own two matchers; %d triggers; the census’s reading %s. H70d %s.' % (
             f['t'], 'unchanged' if f['t'] == 0 else 'changed, the terminal named', S.get('H70d', ['?'])[0]), '',
         '**The four items** (`(R246)`(2)): chi_Tail_TailHyp_traceNorm_smul_Ez_le’s binder %s, dropped by the old reader, read as %s under the '
         'criterion, the move %s; the generator’s two name patterns read Lean identifiers as Lean does, the thirteen names whole; the deposit '
         'bank’s tag matcher reads the REGISTRY’s tag form alone, :705’s sentence no tag; the closing sentence in the rule’s words.' % (
             CT.get('binder'), CT.get('binder_class'), 'standing' if CT.get('stands') else 'reverting'), '',
         '**The seal’s hash arm** (`(R246)`(3)): the sealed tools’ sha256 recorded at the seal and recomputed at the close, agree or differ '
         'printed per tool; the seal rule restated beneath the build clause.', '',
         '**The record lines** (`(R246)`(1), (3)): b635 at its weight (FINDINGS :%s); the seal rule (OPEN_TRAILS :%s).' % tuple(
             x.get('line') for x in (rl.get('lines') or [{}, {}])[:2]), '',
         '**The root.** b636 over %d repositories, %d tags and %d banks; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b634’s reader (FINDINGS :7747) on a second kernel and b633’s census '
         '(FINDINGS :7725) at its SEC row and Phase 2 rows; b635’s entry (FINDINGS :7771) is re-read in its thirteen names, now whole. It '
         'strengthens the programme’s offering of a table whose grades name what Lean elaborated, across two kernels.', '',
         '**Next.** Per `(R246)`(5): b637 on the author’s word -- the deposit, the author’s own act; or W-ORD-BINDER-GRAMMAR with the 20 unnamed '
         'rows as its test set.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds or locates any zero; a rule grade reads a statement’s binders.*', '']
    return t, NL.join(e)


def _next_lines():
    return ['b637 names no kernel terminal; the deposit is the author’s own act, and W-ORD-BINDER-GRAMMAR’s test set is the 20 unnamed rows']


FOR_AUTHOR = ('(1) the ferry’s NAME_RE and PRINT_SRC read in tools/terminal_table.py, where they are, tools/chain_page.py carrying neither; '
              '(2) Lean’s identifier classes, ’ kept in the print pattern as carried; (3) the REGISTRY’s tag form read as a version bound to '
              'a commit, after the word tag, or alone in a table cell; (4) the closing sentence’s plain requests to github.com read as its '
              'reads and pushes; (5) the sealed tools named in the worklist, the reader and the generator outside them as ordered edits')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b636_scores.json', 'b636_findings.json', 'b636_record_lines.json', 'b636_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b636_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    rows_ = ['', TRAIL_HEAD, '',
             '**(R246) ratified.** (1) b635 at its weight. (2) The four items ruled. (3) The seal’s hash arm. (4) The elaborated reader over '
             'SIDE-structural-error-correction. (5) The act after: b637.', '',
             '**Entered:** FINDINGS.md:%s (b635’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the seal rule, standing); this record.' % (
                 (rl.get('lines') or [{}])[0].get('line'), fj.get('entry_line'), (rl.get('lines') or [{}, {}])[1].get('line')), '',
             '**Act root:** b636 `%s` (previous `%s`, b635’s; relay data/act_roots.txt).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b636_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b636_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R246)`(5), b637 on the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b636_scores.json')
    L = ['=' * 104, 'b636 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H70a-H70d, (R246)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper(), S[k2][0], S[k2][1]) for k2 in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SK]
    L += ['', '### ### **H : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k2][0] == 'HOLDS' for k2 in HKEYS), sum(S[k2][0] == 'REFUTED' for k2 in HKEYS), sum(S[k2][0] == 'HELD' for k2 in NK),
                             sum(S[k2][0] == 'REFUTED' for k2 in NK), sum(S[k2][0] == 'HELD' for k2 in SK), sum(S[k2][0] == 'REFUTED' for k2 in SK)), '']
    L += rd('b636_defects.txt').rstrip(NL).split(NL)
    put_txt('b636_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b636_scores.json', 'b636_findings.json', 'b636_trail.json', 'b636_record_lines.json', 'b636_act_root.json'))
    L = ['b636 -- THE COMPONENTS, BANKED UNDER (R246).', '',
         '### COMPONENT 0 : the process listing ; b635`s closing push-out relay %s ; push-b635* deleted by name (data/b636_branches.txt) ; the name '
         'patterns relay %s (data/b636_namepat_test.txt, data/b636_namepat_table.txt) ; the tag matcher relay %s (data/b636_tagmatch_test.txt) ; '
         'every test file run (data/b636_tests_stepzero.txt) ; the suite at HEAD before the face (data/b636_arms_prerun.txt) ; the sealed tools` '
         'hashes at the seal (data/b636_seal_hashes.json) ; b628`s local intake bank untracked' % (STEPZERO, K.REPAIRS[0], K.REPAIRS[1]),
         '### COMPONENT 1 : b635`s weight FINDINGS :%s ; the seal rule :%s ; chi_Tail (data/b636_chitail.txt)' % tuple(
             x.get('line') for x in (rl.get('lines') or [{}, {}])[:2]),
         '### COMPONENT 2 : the kernel`s state (data/b636_kernel_state.txt)',
         '### COMPONENT 3 : the reader (data/b636_reader_diff.txt, data/b636_reader_test.txt) ; data/%s ; H70a %s' % (K.ELAB_BANK, S['H70a'][0]),
         '### COMPONENT 4 : the two readings (data/b636_two_readings_sec.txt) ; data/%s ; the generator (data/b636_gen_diff.txt, '
         'data/b636_gen_test.txt) ; the table (data/b636_table_sec.txt) ; H70b %s ; H70c %s' % (K.DISAGREE_BANK, S['H70b'][0], S['H70c'][0]),
         '### COMPONENT 5 : data/%s ; the pages (data/b636_page_zeta.json, data/b636_page_chi.json) ; page arms data/b636_page_arms.txt ; H70d %s' % (
             K.PHASE2_BANK, S['H70d'][0]),
         '### COMPONENT 6 : FINDINGS :%s (the entry) ; OPEN_TRAILS :%s (the record) ; the root %s ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj.get('entry_line'), tj.get('line'), (J.get('root') or '')[:16], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b636_components.txt', L)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  table cells the entry would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b636_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    cells = predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  table cells the record would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e[:9000])
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b636_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b636_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-07 by b636 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b636_defects.json -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD)
    t = '\n%s %s\n' % (CORR_HEAD % rec_, CORRECTION)
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'correction')
    if 'dry' in a:
        print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CORR_HEAD % rec_)
    r = Q.append_to(Q.OT, t)
    put_json('b636_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'n5_', 'binder_class', 'modules', 'elab_grade', 'classify', 'seal_hashes'):
        print('usage: b636_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
