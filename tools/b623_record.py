# -*- coding: utf-8 -*-
"""b623_record.py -- THE ACT'S RECORD TOOL, UNDER (R233). ### ONE SUBCOMMAND PER BANK.

### ### b623: LANE THREE, ACT FIFTY -- THE UNPUSHED TAGS SETTLED BY CITATION; THE DE-ALIGNMENT KERNEL'S AXIOM ARTEFACT PRINTED AND ITS
### ROWS ENTERED; FOUR RESEARCH WORK-ORDERS AND ONE ARM ENTERED.
### Subcommands write only `data/b623_*` unless the docstring names another file; `dry` on the command line routes every b623 bank, the
### housekeeping lists, REGISTRY's row update and the artefact module to the seat's scratchpad (for `findings` and `trail`, `dry` prints
### and appends nothing; `record_lines dry` prints the ledger lines without appending them). Banks are written by encode, temp file,
### `os.replace`; ledger appends through b566's guarded `append_to`. The data is tools/b623_worklist.py. No platform call. The one Lean
### call is the artefact's build, run detached by the seat's watchdog; `sec_prints` reads its log. The templates are tools/b622_record.py
### (the harness, the pages) and b611's citation matcher (in the data module). The N5 scorer takes the trail record's expected line
### (OPEN_TRAILS :12799).
### ### THE TEST COUNT (R233)(3): `count_cases` is sealed in the form b622 used, which counts every line ending in PASS or FAIL; the
### standing repair is ONE edit of this tool after the seal, through the Edit tool, with its test, committed alone (OPEN_TRAILS :12799's
### pattern); the sealed form is the test's positive control.
"""
import difflib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b623_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/db8d87ba-3c6c-4b82-8201-6f0312a45734/scratchpad'
SESSION_ID = 'db8d87ba-3c6c-4b82-8201-6f0312a45734'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
SESSION_FROM = 0     # ### this session opened on this act's ferry
PUSH_FILES = ('tools/push_gated.sh', 'tools/test_push_gated.sh')
COUNT_FILES = ('tools/b623_record.py', 'tools/b623_test_count.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b623_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b623_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def jx(name):
    return jl(name) if os.path.exists(_p(name)) else {}


def rd(name):
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def lines_of(t):
    return K.lines_of(t)


def _rel(n, rev=PRE_RELAY):
    return _show(RELAY, rev, 'data/' + n) or ''


def _scan(path):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', path], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout or ''


def _clean(out):
    return re.search(r'^\s*VERDICT\s*: CLEAN\s*$', out, re.M) is not None


def _write(path, b):
    open(path + '.tmp', 'wb').write(b)
    os.replace(path + '.tmp', path)


DEFECTS = []
DEFECT_SHORT = []
CORRECTION = ''
# ### b622's form: a defect found after the seal is written by the seat into data/b623_defects.json (keys `defects`, `short`,
# ### `correction`), a bank of this act, read here -- so carrying it needs no edit of this tool after the seal.
_DJ = os.path.join(D, 'b623_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b623 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b623_defects.txt', L)


# ================================================================================ (R233)(3): THE TEST COUNT
def count_cases(text, case_re=None):
    """### THE SEALED FORM, b622's: every line ending in PASS or FAIL is a case. (R233)(3) repairs it after the seal."""
    cases = [l for l in (text or '').split(NL) if re.search(r'( PASS| FAIL)$', l)]
    return len(cases), sum(1 for c in cases if c.endswith(' PASS'))


PUSH_CASE = r'^  [A-Z] \S.* : wanted .* ; got .* ; (?:PASS|### FAIL)$'    # ### test_push_gated.sh's check lines
COUNT_CASE = r'^  \(\d+\) '                                                 # ### the numbered case lines of a Python test


def count_test(*a):
    """### tools/b623_test_count.py run (it exists only after the repair) and banked: data/b623_count_test.txt and .json, its cases counted
    ### by this tool's counter with the numbered case pattern; the test's own lines read for the sealed form's verdict."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'b623_test_count.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out, COUNT_CASE)
    sealed = re.search(r'^### THE SEALED FORM \(the positive control\): (REFUTED|NOT REFUTED|NOT FOUND)', out, re.M)
    L = ['b623 -- COMPONENT 1: THE TEST OF THE CASE COUNTER, RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt('b623_count_test.txt', L)
    put_json('b623_count_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, repaired_all_pass=bool(n) and n == p and r.returncode == 0,
                                          sealed_refuted=bool(sealed) and sealed.group(1) == 'REFUTED'))
    print(L[-1])


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('the census v0.4: every kernel cell naming a tag unpushed', PP, PRE_PP, K.CENSUS, ('GREP', r'unpushed by name'), 260),
        ('OPEN_TRAILS: W-ORD-TAG-REMOTES, W-ORD-SEC-AXIOM-ARTEFACT, the form, the precedence order, the quantifier column, the N5 line, b622`s '
         'offer, record and correction', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12228, 12266, 12330, 12332, 12334, 12597, 12799, 12863, 12865, 12885], 1500),
        ('REGISTRY: the row notes naming the tags (:608, :628) and the dated form (:1060-:1070)', PP, PRE_PP, 'REGISTRY.md',
         [608, 628] + list(range(1060, 1071)), 900),
        ('SPIRAL_MAP: the federation table`s version cells', PP, PRE_PP, 'SPIRAL_MAP.md', [86, 95, 96, 97, 98, 99, 100, 159], 200),
        ('SPIRAL_MAP v0.7: the same cells', PP, PRE_PP, 'SPIRAL_MAP_v0_7.md', [88, 97, 98, 99, 100, 101, 102, 161], 200),
        ('FINDINGS: the line naming residual-bridge v0.1 and b622`s entry', PP, PRE_PP, 'FINDINGS.md', [7304, 7466], 400),
        ('SIDE-structural-error-correction: the build file', K.SEC, K.SEC_PIN[1], 'lakefile.toml', ('ALL',), 200),
        ('SIDE-structural-error-correction: the toolchain', K.SEC, K.SEC_PIN[1], 'lean-toolchain', ('ALL',), 200),
        ('SIDE-structural-error-correction: the root module', K.SEC, K.SEC_PIN[1], 'SIDEStructuralErrorCorrection.lean', ('ALL',), 200),
        ('SIDE-explicit-formula: the house artefact form, AxiomCheckFamily.lean`s head', 'D:/SIDE-explicit-formula', 'v0.21', 'AxiomCheckFamily.lean',
         list(range(1, 15)), 200),
        ('relay tools/terminal_table.py: the artefact patterns, the print reader and the banked-profile reader', RELAY, PRE_RELAY,
         'tools/terminal_table.py', [53, 57, 59, 489, 493, 511, 540, 542, 824, 825], 200),
        ('relay tools/push_gated.sh: usage, the tag refusal, the tag read-back', RELAY, PRE_RELAY, 'tools/push_gated.sh',
         [4, 49, 57, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 127, 128], 200),
        ('relay data/b557_tiers.txt: the six de-alignment terminals` profiles', RELAY, PRE_RELAY, 'data/b557_tiers.txt',
         ('GREP', r'^### :20[2-7] |^    profile   : |^    :21[01] '), 200),
        ('relay data/b622_unclassified.txt: the proposals', RELAY, PRE_RELAY, 'data/b622_unclassified.txt', ('GREP', r'^### |THE SEAT`S PROPOSAL'), 200),
        ('relay data/b622_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b622_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b623 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        elif isinstance(sel, tuple) and sel[0] == 'ALL':
            nums = [i + 1 for i, l in enumerate(sl) if l.strip()]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            line = sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE'
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b623_reads.txt', L)


def answers(*a):
    calls, results = [], {}
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            try:
                o = json.loads(raw)
            except Exception:
                continue
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                    calls.append((i, c['id'], c['input']))
                if isinstance(c, dict) and c.get('type') == 'tool_result':
                    t = c.get('content')
                    results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    since = [c for c in calls if c[0] > SESSION_FROM]
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b623 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
        L.append('### NONE YET: no prompt has been put to the author in this act.')
    put_txt('b623_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7', 'SIDE-cosmo': 'c5cba30'}


def kern_state(ks=None):
    """### {kernel: [main, {tag: peeled commit}, branches]} -- the tags by name AND peel, so a re-pointed tag shows."""
    out = {}
    for k in (ks or (KERNS + tuple(K.TAG_KERNELS) + (K.SEC_NAME,))):
        p = 'D:/' + k
        tags = {}
        for l in g(p, 'for-each-ref', '--format=%(refname:short) %(objectname) %(*objectname)', 'refs/tags').split(NL):
            if l.strip():
                x = l.split()
                tags[x[0]] = (x[2] if len(x) > 2 else x[1])[:7]
        out[k] = [g(p, 'rev-parse', '--short=7', 'main').strip(), tags,
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip())]
    return out


def kernels(*a):
    put_json('b623_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ COMPONENT 1: THE RECORD LINES
B622_ENTRY = '## The quantifier column: five shapes read from the Lean statements at v0.20 and v0.21'
W_HEAD = '*Appended 2026-10-04 by b623 to b622’s entry (:%d), under `(R233)`(1) -- b622 AT ITS WEIGHT:*'
U_HEAD = '*Appended 2026-10-04 by b623 to W-ORD-QUANTIFIER-COLUMN (:%d), under `(R233)`(2) -- THE THREE UNCLASSIFIED NODES RULED; THE BUNDLE CLAUSE:*'
C_HEAD = '*Appended 2026-10-04 by b623 beneath the N5 scorer’s line (:%d), under `(R233)`(3) -- THE TEST COUNT, STANDING:*'
O_HEAD = '*Appended 2026-10-04 by b623, under `(R233)`(4)%s -- %s, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD:*'
QC_HEAD = '### `W-ORD-QUANTIFIER-COLUMN` -- THE QUANTIFIER SHAPE OF EACH NODE, A PAGE COLUMN, PRICED, NOT STARTED'
N5_HEAD = '*Appended 2026-10-04 by b619 beneath the build clause (:12356), under the author’s ruling `(R229)`(2) -- THE N5 SCORER, STANDING:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def b622_figures():
    """### b622's figures, each read from its bank at relay PRE_RELAY, beside the ruling's (R233)(1)."""
    S = {k: v[0] for k, v in json.loads(_rel('b622_scores.json')).items()}
    pj = {k: json.loads(_rel('b622_page_%s_c4.json' % k)) for k in ('zeta', 'chi')}
    cnt = {}
    for k in ('zeta', 'chi'):
        c = {}
        for s in pj[k]['shapes'].values():
            c[s] = c.get(s, 0) + 1
        cnt[k] = c
    SJ = json.loads(_rel('b622_sieve_shapes.json'))
    rep = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', _rel('b622_repin_sieve.txt'))
    pre, post = _count_bank(_rel('b622_checks.txt')), _count_bank(_rel('b622_checks_postpush.txt'))
    gt = _rel('b622_gen_test.txt')
    return dict(scores=S, shapes=cnt, nodes={k: len(pj[k]['shapes']) for k in pj}, rows=len(SJ['rows']),
                same=sum(1 for r in SJ['rows'] if r['same']), diff=[(r['id'], r['gen'], r['hand'].replace(' (H)', '')) for r in SJ['rows'] if not r['same']],
                repin=(rep.group(1), rep.group(2)) if rep else None, pre=pre, post=post,
                cases=len([l for l in gt.split(NL) if re.match(COUNT_CASE, l)]))


SHAPE_ORDER = ('FINITE', 'UNIVERSAL', 'LIMIT', 'DENSITY', 'FAMILY', '—', 'UNCLASSIFIED')


def _weight(entry, ot_lines):
    F = b622_figures()
    S = F['scores']
    sh = lambda k: ', '.join('%s %d' % (s, F['shapes'][k][s]) for s in SHAPE_ORDER if F['shapes'][k].get(s))   # noqa: E731
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else str([S[k] for k in ks])   # noqa: E731
    return ('\n%s relay tools/chain_page.py reads each node’s shape from its statement when a node list carries the column’s line, a '
            'list without it emitting byte for byte (relay 664e6302, with its test of %d cases); the five test nodes FINITE, UNIVERSAL, '
            'UNIVERSAL, DENSITY, FAMILY; the ζ page at %d nodes (%s), the χ page at %d (%s), each re-emitted twice and committed alone, the '
            'page arms and the frozen control 2 of 2 after each pass; the sieve at v0.6 (d0318e8), %d rows at the generator’s mark, %d '
            'agreeing with the hand read, %s; re-pin %s of %s; README (105b6eb) with the v0.17–v0.21 sentence and the live line at v5.18; the '
            '39 sentences in seven work-lists and seven addenda (relay 109da0d5). H56a-H56d %s; N1-N5 %s; S1-S5 %s. FINDINGS :7464, :7466; '
            'OPEN_TRAILS :12863, :12865, :12885. Relay 5d0816dd; PLACE-papers c9e9a9c. The suite %d of %d before the push and %d of %d after '
            'it, NOT CLEAN in letter on the seat’s defects (a) the record tool counting the test’s verdict line as a case, (c) a leading '
            'space dropped by a sealed arm, (d) a sealed arm comparing against the pages before the act, each claim tested directly and '
            'holding, neither sealed tool edited. **Ruled, `(R233)`(1):** where a sieve row names a page node the generator’s read governs, '
            'the hand read recorded beside it. **Entered under `(R233)`(2)-(4):** OPEN_TRAILS :%d (the three nodes and the bundle clause), :%d '
            '(the test count, standing), :%d-:%d (the four work-orders). Nothing deposited; no kernel touched.\n' % (
                W_HEAD % entry, F['cases'], F['nodes']['zeta'], sh('zeta'), F['nodes']['chi'], sh('chi'), F['rows'], F['same'],
                ' and '.join('%s %s against the hand’s %s' % d for d in F['diff']), F['repin'][0], F['repin'][1],
                allh(('H56a', 'H56b', 'H56c', 'H56d'), 'HOLDS').replace('HOLDS', 'HOLD'), allh(('N1', 'N2', 'N3', 'N4', 'N5'), 'HELD'),
                allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'), F['pre'][0], F['pre'][1], F['post'][0], F['post'][1],
                ot_lines[0], ot_lines[1], ot_lines[2], ot_lines[5]))


def _unclassified(qc_line):
    UJ = json.loads(_rel('b622_unclassified.json'))
    names = list(UJ['proposals'])
    return ('\n%s %s take UNIVERSAL as premise bundles whose strongest field is universal, each field read from the kernel source at its '
            'page’s pin (relay data/b622_unclassified.txt): the author’s ruling of the seat’s proposals. **The bundle clause:** from the '
            'generator’s next edit, a node whose statement is a premise bundle -- a Prop structure, or a Prop definition whose body is a '
            'conjunction of named fields -- prints the shape of its strongest field in the order FINITE, UNIVERSAL, LIMIT, DENSITY, FAMILY, '
            'each field read by the reader’s own rules; the edit is not made by b623. The sieve’s row RH-03 takes the same reading at the '
            'sieve’s next version.\n' % (U_HEAD % qc_line, ', '.join(n.split('.')[-1] for n in names)))


def _testcount(n5_line):
    return ('\n%s the record tool counts a test’s cases by the test’s own case pattern -- the numbered case lines of a Python test, the '
            'check lines of test_push_gated.sh -- and never by its summary lines, so a verdict line such as “### ALL PASS” is not a case; '
            'a test of the counter plants a summary line and expects the count unchanged, and runs the sealed form as its positive '
            'control. The instances at b597 and b622 (b622’s defect (a), the entry’s “10 of 10”, corrected at :12885) are its reason; '
            'the repair is one edit of the act’s own record tool after its seal, committed alone in relay with its test, from b623 on.\n'
            % (C_HEAD % n5_line))


def _workorder(i):
    wid, roman, items, price = K.WORK_ORDERS[i]
    return ('\n%s Items: %s. Price: %s. Trigger: the author’s word. From the bright-register reading of b621–b622. Not started.\n' % (
        O_HEAD % (roman, wid), items, price))


def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def ledger_check(*texts):
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b623_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def record_lines(*a):
    """### OPEN_TRAILS: the three nodes ruled and the bundle clause (addressed to :12266), the test count standing (addressed to :12799), the
    ### four work-orders; FINDINGS: b622's weight, addressed to its entry, citing the OPEN_TRAILS lines. The OPEN_TRAILS lines are computed
    ### first (each append opens with a blank line) and checked after each append."""
    Q = R2._Q()
    entry, qc, n5l = Q.line_of(Q.FIND, B622_ENTRY), Q.line_of(Q.OT, QC_HEAD), Q.line_of(Q.OT, N5_HEAD)
    if (entry, qc, n5l) != (7466, 12266, 12799):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (entry, qc, n5l))
    n0 = len(lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), '')))
    ot_texts = [(U_HEAD % qc, _unclassified(qc)), (C_HEAD % n5l, _testcount(n5l))] + [
        (O_HEAD % (K.WORK_ORDERS[i][1], K.WORK_ORDERS[i][0]), _workorder(i)) for i in range(4)]
    want, n = [], n0
    for _h, t in ot_texts:
        want.append(n + 2)
        n += len(t.strip(NL).split(NL)) + 1
    wt = _weight(entry, want)
    allt = wt + ''.join(t for _h, t in ot_texts)
    bad = ledger_check(allt)
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s ; OPEN_TRAILS lines expected %s' % (
        bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', want))
    if DRY:
        print(wt)
        for _h, t in ot_texts:
            print(t)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    for h, _t in ot_texts:
        Q.guard_absent(Q.OT, h)
    out = []
    for (h, t), w in zip(ot_texts, want):
        r = Q.append_to(Q.OT, t)
        got = Q.line_of(Q.OT, h)
        out.append(dict(file='OPEN_TRAILS.md', head=h, line=got, append=r))
        if got != w:
            put_json('b623_record_lines.json', dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED; FINDINGS NOT APPENDED' % (h[:60], got, w))
    r1 = Q.append_to(Q.FIND, wt)
    out.insert(0, dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r1))
    put_json('b623_record_lines.json', dict(entry=entry, qc=qc, n5=n5l, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ (R233)(4): THE OFFERING-LINE ARM'S COUNT
OFFER_FROM = 6818    # ### FINDINGS: b594's entry, the first under (R204)(3)
OFFER_TO = 622       # ### the entries filed b594 to b622, the acts before this one: this act's own entry never moves the count


def offering_rows(find_text):
    """### every FINDINGS entry from b594's on: (line, act, carries) -- carries when a sentence of its `**Read in mutual light**` paragraph
    ### names an offering it strengthens (`strengthen...` and `offering...` in one sentence), the form of (R204)(3)(iii)."""
    L = (find_text or '').replace(chr(13), '').split(NL)
    heads = [i for i, l in enumerate(L) if l.startswith('## ')]
    out = []
    for j, h in enumerate(heads):
        if h + 1 < OFFER_FROM:
            continue
        end = heads[j + 1] if j + 1 < len(heads) else len(L)
        m = re.search(r'\*Filed at b(\d+)', NL.join(L[h:h + 6]))
        if m and int(m.group(1)) > OFFER_TO:
            continue
        ml = [l for l in L[h:end] if l.startswith('**Read in mutual light**')]
        hit = [s for l in ml for s in re.split(r'(?<=[.;])\s+(?=[A-Z])', l) if re.search(r'\bstrengthen', s) and re.search(r'\boffering', s)]
        out.append(dict(line=h + 1, act=('b' + m.group(1)) if m else None, carries=bool(hit), sentence=(hit[0][:200] if hit else None)))
    return out


def offering(*a):
    t = _show(PP, 'HEAD', 'FINDINGS.md') or ''
    rows = offering_rows(t)
    w, wo = sum(1 for r in rows if r['carries']), sum(1 for r in rows if not r['carries'])
    L = ['b623 -- (R233)(4)`s ARM: THE FINDINGS ENTRIES b594-b622 CARRYING THE OFFERING LINE OF (R204)(3)(iii), AND THOSE WITHOUT (%s; '
         'FINDINGS at PLACE-papers %s)' % (utc(), g(PP, 'rev-parse', '--short=7', 'HEAD').strip()), '',
         '### the matcher: a sentence of the entry`s `**Read in mutual light**` paragraph naming an offering it strengthens', '']
    L += ['  :%-5d %-5s %s  %s' % (r['line'], r['act'], 'CARRIES' if r['carries'] else '### WITHOUT', r['sentence'] or '') for r in rows]
    L += ['', '### ### **ENTRIES SINCE b594 : %d ; CARRYING THE OFFERING LINE : %d ; WITHOUT : %d.**' % (len(rows), w, wo)]
    put_txt('b623_offering.txt', L)
    put_json('b623_offering.json', dict(at=utc(), entries=len(rows), carrying=w, without=wo, rows=rows))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE TAGS
def _ledger_texts(rev=PRE_PP):
    return {f: K.show(f, rev) for f in K.RULED_LEDGERS}, {f: K.show(f, rev) for f in K.BESIDE_LEDGERS}


def _remote(k):
    """### one `git ls-remote origin` per kernel per run (OPEN_TRAILS :12703): {ref: sha}"""
    import b616_claims as KC0
    return KC0.remote_refs('D:/' + k)


def _peel(k, tag):
    return g('D:/' + k, 'rev-parse', '--verify', '-q', tag + '^{commit}').strip()


def _remote_peel(refs, tag):
    return refs.get('refs/tags/%s^{}' % tag) or refs.get('refs/tags/%s' % tag)


def tag_rows(remote=True):
    ruled, beside = _ledger_texts()
    rows = []
    for k, t, s in K.TAGS:
        cit = K.citations(k, t, ruled)
        bes = K.citations(k, t, beside)
        refs = _remote(k) if remote else {}
        loc = _peel(k, t)
        typ = g('D:/' + k, 'cat-file', '-t', 'refs/tags/' + t).strip()
        same = sorted(n[len('refs/tags/'):] for n, h in refs.items() if n.startswith('refs/tags/') and not n.endswith('^{}')
                      and _remote_peel(refs, n[len('refs/tags/'):]) == loc and n[len('refs/tags/'):] != t)
        rows.append(dict(kernel=k, tag=t, census_sha=s, local_peel=loc, type=typ, url=g('D:/' + k, 'remote', 'get-url', 'origin').strip(),
                         remote_main=refs.get('refs/heads/main'), at_remote=_remote_peel(refs, t), remote_same_commit=same,
                         ancestor_of_remote_main=(subprocess.run(['git', '-C', 'D:/' + k, 'merge-base', '--is-ancestor', loc, refs.get('refs/heads/main', '')],
                                                                 capture_output=True).returncode == 0) if refs.get('refs/heads/main') else None,
                         cited={f: [(n, sh_) for n, sh_, _l in v] for f, v in cit.items()},
                         cited_text={f: [l[:220] for _n, _s, l in v] for f, v in cit.items()},
                         beside={f: [n for n, _s, _l in v] for f, v in bes.items()}))
    return rows


def tags(*a):
    """### data/b623_tags.txt and .json: each unpushed tag with its kernel, its peeled commit, its remote and every ledger line citing it, read
    ### at PLACE-papers PRE_PP; the remote read once per kernel; before any push."""
    rows = tag_rows()
    L = ['b623 -- COMPONENT 2: THE TWELVE UNPUSHED TAGS, EACH WITH ITS KERNEL, ITS PEELED COMMIT, ITS REMOTE AND EVERY LEDGER CITATION '
         '(%s)' % utc(), '',
         '### the ledgers read at PLACE-papers %s: %s; printed beside and not counted: %s' % (PRE_PP, ', '.join(K.RULED_LEDGERS), ', '.join(K.BESIDE_LEDGERS)),
         '### a citation (the author`s answer before the seal): b611`s prose matcher, or a version cell beside the kernel`s own cell in a table row', '']
    for r in rows:
        n = sum(len(v) for v in r['cited'].values())
        L.append('### %s %s = %s (%s) -- %s' % (r['kernel'], r['tag'], r['local_peel'][:7], r['type'], 'CITED (%d line%s): PUSH' % (n, '' if n == 1 else 's')
                                                if n else 'CITED BY NO LEDGER: RECORDED LOCAL'))
        L.append('    remote %s ; remote main %s ; the tag at the remote %s ; the remote tags the same commit as %s ; the commit an ancestor of the '
                 'remote`s main %s' % (r['url'], (r['remote_main'] or '?')[:7], (r['at_remote'] or 'ABSENT')[:7], r['remote_same_commit'] or 'none',
                                        r['ancestor_of_remote_main']))
        for f, v in sorted(r['cited'].items()):
            for (ln, shp), txt in zip(v, r['cited_text'][f]):
                L.append('    cited: %s :%d (%s) -- %s' % (f, ln, shp, txt))
        for f, v in sorted(r['beside'].items()):
            L.append('    beside, not counted: %s %s' % (f, ', '.join(':%d' % x for x in v)))
    cited = [r for r in rows if r['cited']]
    one = [r for r in cited if r['remote_same_commit']]
    L += ['', '### ### **TAGS : %d IN %d KERNELS ; CITED : %d ; CITED BY NO LEDGER : %d ; CITED AND ON A COMMIT THE REMOTE ALREADY TAGS : %d (%s).**' % (
        len(rows), len(set(r['kernel'] for r in rows)), len(cited), len(rows) - len(cited), len(one),
        ', '.join('%s %s = %s' % (r['kernel'], r['tag'], '/'.join(r['remote_same_commit'])) for r in one))]
    put_txt('b623_tags.txt', L)
    put_json('b623_tags.json', dict(at=utc(), pre_pp=PRE_PP, rows=rows))
    print(L[-1])


def tags_readback(*a):
    """### after the pushes: every tag read at its remote again (one ls-remote per kernel), its peel against the local peel; the local tags
    ### of the nine kernels against the face; data/b623_tags_readback.json."""
    T = jl('b623_tags.json')
    face = jl('b623_kernels_face.json')['kernels']
    now = kern_state(list(K.TAG_KERNELS))
    out = []
    for r in T['rows']:
        refs = _remote(r['kernel'])
        rp = _remote_peel(refs, r['tag'])
        cited = bool(r['cited'])
        out.append(dict(kernel=r['kernel'], tag=r['tag'], cited=cited, local_peel=_peel(r['kernel'], r['tag']), remote_peel=rp,
                        equal=bool(rp) and rp == _peel(r['kernel'], r['tag']), pushed=bool(rp), log=('b623_tagpush_%s_%s.txt' % (
                            r['kernel'][5:], r['tag'])) if cited else None))
    unmoved = {k: now[k][1] == face[k][1] and now[k][0] == face[k][0] for k in K.TAG_KERNELS}
    h57a = 'HOLDS' if all(x['equal'] for x in out if x['pushed']) and any(x['pushed'] for x in out) else 'REFUTED'
    h57b = 'HOLDS' if all(x['pushed'] == x['cited'] for x in out) else 'REFUTED'
    put_json('b623_tags_readback.json', dict(at=utc(), rows=out, unmoved=unmoved, H57a=h57a, H57b=h57b))
    L = ['b623 -- COMPONENT 2: THE TAGS READ BACK AT THEIR REMOTES AFTER THE PUSHES (%s)' % utc(), '']
    L += ['  %-28s %-5s %-6s local %s remote %s %s' % (x['kernel'], x['tag'], 'cited' if x['cited'] else 'local', x['local_peel'][:7],
                                                      (x['remote_peel'] or 'ABSENT')[:7], 'EQUAL' if x['equal'] else ('### UNEQUAL' if x['pushed'] else ''))
          for x in out]
    L += ['', '### the nine kernels` mains and local tags (name and peel) against the face: %s' % unmoved,
          '### ### **H57a %s -- every pushed tag`s peel read back equal: %d of %d. H57b %s -- cited %d pushed %d; uncited %d pushed %d.**' % (
              h57a, sum(x['equal'] for x in out if x['pushed']), sum(x['pushed'] for x in out), h57b, sum(x['cited'] for x in out),
              sum(x['cited'] and x['pushed'] for x in out), sum(not x['cited'] for x in out), sum((not x['cited']) and x['pushed'] for x in out))]
    put_txt('b623_tags_readback.txt', L)
    print(L[-1])


HK_HEAD = ('b623 -- THE HOUSEKEEPING LIST OF %s (opened under (R233)(5)(a); no earlier list found -- relay git ls-files and PLACE-papers '
           'OPEN_TRAILS / FINDINGS searched; the list lives in relay because no byte of the kernel is written by this act)')
HK_FORM = '### each row: the tag, its peeled commit, its state at the remote, the ledger lines citing it, what is recorded, the informing act'


def _hk_rows(k, T, RB):
    rows = []
    for r in [x for x in T['rows'] if x['kernel'] == k]:
        rb = [x for x in RB['rows'] if x['kernel'] == k and x['tag'] == r['tag']][0]
        cites = '; '.join('%s %s' % (f, ', '.join(':%d' % n for n, _s in v)) for f, v in sorted(r['cited'].items()))
        if not r['cited']:
            rows += ['%s %s = %s -- LOCAL, NOT PUSHED' % (k, r['tag'], r['local_peel'][:7]),
                     '    at the remote: absent (read back %s); the remote`s main %s, the commit an ancestor of it %s' % (
                         'absent' if not rb['remote_peel'] else rb['remote_peel'][:7], (r['remote_main'] or '?')[:7], r['ancestor_of_remote_main']),
                     '    cited by no ledger line of %s at PLACE-papers %s' % (', '.join(K.RULED_LEDGERS), PRE_PP),
                     '    recorded: the tag stays in the clone alone, unmoved; a later act that cites it pushes it by the existing-tag mode',
                     '    informing act: b623 (R233)(5)(a), W-ORD-TAG-REMOTES (OPEN_TRAILS :12597)', '']
        if r['cited'] and r['remote_same_commit']:
            rows += ['%s %s = %s -- PUSHED, ONE COMMIT WITH %s' % (k, r['tag'], r['local_peel'][:7], ' AND '.join(r['remote_same_commit'])),
                     '    at the remote: %s, read back equal %s; the remote`s %s peels to the same commit' % (
                         (rb['remote_peel'] or 'ABSENT')[:7], rb['equal'], ', '.join(r['remote_same_commit'])),
                     '    cited at: %s, the name kept in the ledgers as written' % cites,
                     '    recorded: %s and %s are one commit; a later edition may normalise the cited name, this act does not (the author`s '
                     'answer before the seal)' % (r['tag'], ' and '.join(r['remote_same_commit'])),
                     '    informing act: b623 (R233)(5)(a), W-ORD-TAG-REMOTES (OPEN_TRAILS :12597)', '']
    return rows


def housekeeping(*a):
    """### relay data/SIDE-<k>_housekeeping.txt, created, for every kernel holding a tag recorded local or a pushed tag one commit with the
    ### remote's v0.1.0 (the author's answer before the seal); written after the read-back."""
    T, RB = jl('b623_tags.json'), jl('b623_tags_readback.json')
    made = []
    for k in K.TAG_KERNELS:
        rows = _hk_rows(k, T, RB)
        if not rows:
            continue
        name = '%s_housekeeping.txt' % k
        p = os.path.join(SP if DRY else D, name)
        if not DRY and os.path.exists(p):
            sys.exit('### %s EXISTS -- NOTHING WRITTEN' % name)
        n = sum(1 for l in rows if l and not l.startswith(' '))
        text = NL.join([HK_HEAD % k, '', HK_FORM, ''] + rows + ['### %d row%s.' % (n, '' if n == 1 else 's')]) + NL
        _write(p, text.encode('utf-8'))
        made.append(dict(file='data/' + name, rows=n, sha256=sha(text.encode('utf-8'))))
        print('  written: %s%s (%d rows)' % ('DRY ' if DRY else '', name, n))
    put_json('b623_housekeeping.json', dict(at=utc(), files=made, dry=DRY))


REG_HEAD = ('## Row update — 2026-10-04 (the tags `REGISTRY.md:628` verified to exist, read against their remotes; b623, under the author’s '
            'ruling `(R233)`(5)(a), W-ORD-TAG-REMOTES (OPEN_TRAILS :12597); fold into the row note at next hand edit)')
REG_TAIL = '*Appended by b623. No row above is edited; the row note folds this at its next hand edit. Nothing deposits.*'


def registry_text(pre):
    RB = jl('b623_tags_readback.json')
    T = jl('b623_tags.json')
    get = lambda k, t: [x for x in RB['rows'] if x['kernel'] == k and x['tag'] == t][0]   # noqa: E731
    tg = lambda k, t: [x for x in T['rows'] if x['kernel'] == k and x['tag'] == t][0]   # noqa: E731
    b, s = get('SIDE-bijection', 'v0.1'), get('SIDE-substrate-cluster', 'v0.4')
    other = {k: _remote(k) for k in ('SIDE-dirichlet-mod-24', 'SIDE-class-number-anomaly')}
    od = (_remote_peel(other['SIDE-dirichlet-mod-24'], 'v0.1.0') or '')[:7]
    oc = (_remote_peel(other['SIDE-class-number-anomaly'], 'v0.2') or '')[:7]
    para = ('Appended; **no row above is edited.** `REGISTRY.md:628` reads that all cited tags were verified to exist (substrate-cluster '
            'v0.4, dirichlet v0.1.0, class-number-anomaly v0.2, bijection v0.1). Read by ls-remote on 2026-10-04 before this act’s pushes, two '
            'of the four were carried by their clones alone and absent at their remotes (relay `data/b610_census.txt`, Part C; '
            '`data/b623_tags.txt`): `SIDE-substrate-cluster` v0.4 = `%s` and `SIDE-bijection` v0.1 = `%s`, each on the commit its remote '
            'already tags v0.1.0 (`%s` and `%s`). **Corrected by this note:** both are now at their remotes, pushed by b623 one at a time '
            'through `tools/push_gated.sh`’s existing-tag mode, the peeled commit read back equal at each remote (relay '
            '`data/b623_tags_readback.txt`), neither moved nor re-pointed; dirichlet v0.1.0 = `%s` and class-number-anomaly v0.2 = `%s` '
            'read at their remotes the same day. The line’s “verified to exist” now holds at the remotes for all four. :628 is not edited.' % (
                s['local_peel'][:7], b['local_peel'][:7], '/'.join(tg('SIDE-substrate-cluster', 'v0.4')['remote_same_commit']),
                '/'.join(tg('SIDE-bijection', 'v0.1')['remote_same_commit']), od or 'NOT READ', oc or 'NOT READ'))
    if not (s['equal'] and b['equal']):
        para += ' NOT READ BACK EQUAL'
    add = NL + REG_HEAD + NL + NL + para + NL + NL + '<!-- b623 (R233)(5)(a) ROW UPDATE, 2026-10-04 -->' + NL + NL + REG_TAIL + NL
    return pre + add, para


def registry(*a):
    """### PLACE-papers REGISTRY.md: one dated row update in its own form appended at the end, after the read-back; the disk file must equal
    ### its HEAD blob first; the appended text scanned and checked against the table's grade reader."""
    head = _show(PP, 'HEAD', 'REGISTRY.md')
    disk = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8', newline='').read().replace('\r\n', '\n')
    if head is None or disk != head or head != _show(PP, PRE_PP, 'REGISTRY.md'):
        sys.exit('### REGISTRY ON DISK, AT HEAD AND AT %s DIFFER -- NOTHING WRITTEN' % PRE_PP)
    new, para = registry_text(head)
    bad = ledger_check(para)
    nd, _n = _nd(para)
    sc, clean = _scan_text(para, 'registry')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if DRY:
        print(new[len(head):])
        return
    if bad or any(nd.values()) or not clean or 'NOT READ' in para:   # ### a remote unread or a read-back unequal writes nothing
        sys.exit('### THE NOTE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM, OR A REMOTE WAS NOT READ -- NOTHING WRITTEN')
    _write(os.path.join(PP, 'REGISTRY.md'), new.encode('utf-8'))
    put_json('b623_registry.json', dict(at=utc(), line=lines_of(new).index(REG_HEAD) + 1, sha256=sha(new.encode('utf-8')), before=len(head.encode('utf-8')),
                                        added=len(new.encode('utf-8')) - len(head.encode('utf-8')), para=para, clean=clean))
    print('  REGISTRY row update at :%d' % (lines_of(new).index(REG_HEAD) + 1))


def push_diff(*a):
    """### push_gated.sh and its test, edited after the seal, printed as their diff against relay PRE_RELAY (data/b623_push_diff.txt);
    ### the stat line kept as git prints it, leading space and all (b622's defect (c))."""
    d = g(RELAY, 'diff', PRE_RELAY, '--', *PUSH_FILES)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', *PUSH_FILES)
    L = ['b623 -- COMPONENT 2: push_gated.sh`S EXISTING-TAG MODE AND ITS TEST CASES, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), '',
         '### ' + (st.rstrip(NL).split(NL)[-1] if st.strip() else 'NO DIFF'), ''] + d.rstrip(NL).split(NL)
    put_txt('b623_push_diff.txt', L)
    print(L[2])


def push_test(*a):
    """### tools/test_push_gated.sh run and counted by its case pattern (data/b623_push_test.txt and .json)."""
    r = subprocess.run(['bash', os.path.join(ROOT, 'tools', 'test_push_gated.sh')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out, PUSH_CASE)
    m = re.search(r'\*\*(\d+) of (\d+) checks as wanted -- (PASS|FAIL)\*\*', out)
    L = ['b623 -- COMPONENT 2: tools/test_push_gated.sh RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the case pattern; the test`s own line: %s' % (
        n, p, n - p, m.group(0) if m else 'NONE')]
    put_txt('b623_push_test.txt', L)
    put_json('b623_push_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, summary=m.group(0) if m else None))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE ARTEFACT
SEC_DOC = ('/-!\n# Axiom audit -- act b623, ruling (R233)(5)(b)\n\nRun `lake env lean AxiomCheck.lean` (once the library is built) to reproduce '
           'the `#print axioms` output for every declaration of\nSIDEStructuralErrorCorrection/Basic.lean and '
           'SIDEStructuralErrorCorrection/DeAlignment.lean -- the six de-alignment theorems and every other\ndeclaration the library '
           'exports, its theorems the terminals. Each is expected to reduce to the standard base (`propext`,\n`Classical.choice`, '
           '`Quot.sound`) or less, with no `sorryAx`. The compiler`s output is the verdict, not this comment.\n-/\n')


def sec_text():
    ex = K.sec_exports()
    return 'import %s\n\n%s\n%s' % (K.SEC_ROOT_MODULE, SEC_DOC, ''.join('#print axioms %s\n' % n for _m, _l, _k, n in ex)), ex


def sec_exports(*a):
    ex = K.sec_exports()
    L = ['b623 -- COMPONENT 3: SIDE-structural-error-correction`S EXPORTS AT %s = %s, READ FROM THE BLOBS (%s)' % (K.SEC_PIN + (utc(),)), '']
    L += ['  %-48s :%-4d %-9s %s%s' % (m, l, k, n, '   ### one of the six' if n in K.SEC_SIX else ('   ### named by the work-order' if n in K.SEC_NAMED else ''))
          for m, l, k, n in ex]
    L += ['', '### ### **DECLARATIONS : %d ; THEOREMS (THE TERMINALS) : %d ; DEFINITIONS : %d ; STRUCTURES : %d ; THE SIX AND THE TWO NAMED PRESENT : %s.**' % (
        len(ex), sum(1 for x in ex if x[2] == 'theorem'), sum(1 for x in ex if x[2] == 'def'), sum(1 for x in ex if x[2] == 'structure'),
        all(n in [x[3] for x in ex] for n in K.SEC_SIX + K.SEC_NAMED))]
    put_txt('b623_sec_exports.txt', L)
    put_json('b623_sec_exports.json', dict(at=utc(), pin=K.SEC_PIN, exports=[list(x) for x in ex]))
    print(L[-1])


def sec_artefact(*a):
    """### SIDE-structural-error-correction/AxiomCheck.lean written on the branch (the seat checks the branch out first); refused unless the
    ### branch is checked out at the pin with a clean tree and the file absent."""
    text, ex = sec_text()
    if DRY:
        _write(os.path.join(SP, 'AxiomCheck_dry.lean'), text.encode('utf-8'))
        print('  DRY AxiomCheck.lean: %d #print axioms lines' % len(ex))
        return
    cur = g(K.SEC, 'branch', '--show-current').strip()
    head = g(K.SEC, 'rev-parse', '--short=7', 'HEAD').strip()
    dirty = g(K.SEC, 'status', '--porcelain', '--untracked-files=all').strip()
    p = os.path.join(K.SEC, K.SEC_ARTEFACT)
    if cur != K.SEC_BRANCH or head != K.SEC_PIN[1] or dirty or os.path.exists(p):
        sys.exit('### NOT ON %s AT %s WITH A CLEAN TREE AND NO ARTEFACT (%s, %s, %r) -- NOTHING WRITTEN' % (K.SEC_BRANCH, K.SEC_PIN[1], cur, head, dirty[:80]))
    _write(p, text.encode('utf-8'))
    put_json('b623_sec_artefact.json', dict(at=utc(), file=K.SEC_ARTEFACT, sha256=sha(text.encode('utf-8')), prints=len(ex), branch=cur, on=head))
    print('  written: %s (%d #print axioms lines)' % (K.SEC_ARTEFACT, len(ex)))


BUILD_TARGETS = ('+SIDEStructuralErrorCorrection.Basic', '+SIDEStructuralErrorCorrection.DeAlignment', '+SIDEStructuralErrorCorrection',
                 'AxiomCheck.lean')


def builds(*logs):
    """### the four detached build calls' watchdog logs (scratchpad), one module per call in import order, banked whole as
    ### data/b623_sec_build.txt with data/b623_sec_build.json: each call's target, free memory at its start, exit, seconds, peak."""
    calls, L = [], ['b623 -- COMPONENT 3: THE BUILD OF SIDE-structural-error-correction AND THE PRINTS, FOUR DETACHED CALLS, EACH LOG AS THE '
                    'WATCHDOG WROTE IT (%s)' % utc(), '']
    for p in logs:
        t = io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
        st = re.search(r'^### START (\S+) free (\d+) MB pid (\d+) cmd (.*) cwd (.*)$', t, re.M)
        ex = re.search(r'^### EXIT (-?\d+) (\S+) (\d+) s peak (-?\d+) MB', t, re.M)
        tgt = [x for x in BUILD_TARGETS if st and st.group(4).rstrip().endswith(' ' + x)]
        calls.append(dict(log=os.path.basename(p), target=tgt[0] if tgt else None, start=st.group(1) if st else None,
                          start_free=int(st.group(2)) if st else None, pid=int(st.group(3)) if st else None, rc=int(ex.group(1)) if ex else None,
                          seconds=int(ex.group(3)) if ex else None, peak_mb=int(ex.group(4)) if ex else None, detached=bool(st)))
        L += ['### LOG %s' % os.path.basename(p)] + t.rstrip(NL).split(NL) + ['']
    L += ['### ### **CALLS : %d ; TARGETS %s ; EXITS %s ; FREE AT START %s MB.**' % (len(calls), [c['target'] for c in calls], [c['rc'] for c in calls],
                                                                                [c['start_free'] for c in calls])]
    put_txt('b623_sec_build.txt', L)
    put_json('b623_sec_build.json', dict(at=utc(), calls=calls))
    print(L[-1])


PRINT_LINE = re.compile(r"^'([A-Za-z_][A-Za-z0-9_.]*)'[ \t]+(does not depend on any axioms|depends on axioms: \[([^\]]*)\])$")


def sec_prints(log, *a):
    """### the prints read back from the watchdog's log of `lake env lean AxiomCheck.lean` (a log in the scratchpad): data/b623_sec_prints.txt
    ### (every line as printed) and data/b623_profile.json in the house form of the banked profiles (lines, exit, sorry, std3) that
    ### relay tools/terminal_table.py reads (W-ORD-TABLE-PROFILE-JSON)."""
    raw = io.open(log, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    m = re.search(r'^### EXIT (-?\d+)', raw, re.M)
    rc = int(m.group(1)) if m else None
    body = [l for l in raw.split(NL) if not l.startswith('### ')]
    joined, cur = [], ''
    for l in body:   # ### Lean wraps a long axiom list onto indented lines: join them to their print
        if l.startswith("'"):
            if cur:
                joined.append(cur)
            cur = l.strip()
        elif cur and l.startswith(' '):
            cur += ' ' + l.strip()
        else:
            if cur:
                joined.append(cur)
            cur = ''
    if cur:
        joined.append(cur)
    ex = K.sec_exports()
    want = [n for _m, _l, _k, n in ex]
    got = {}
    for l in joined:
        mm = PRINT_LINE.match(l)
        if mm:
            got[mm.group(1)] = (l, [x.strip() for x in (mm.group(3) or '').split(',') if x.strip()])
    std3 = {n: all(x in K.STD3 for x in got[n][1]) for n in got}
    sorry = any('sorryAx' in got[n][1] for n in got)
    kinds = {n: k for _m, _l, k, n in ex}
    L = ['b623 -- COMPONENT 3: THE PRINTS OF AxiomCheck.lean, READ BACK FROM THE WATCHDOG`S LOG (%s); exit %s' % (utc(), rc), '']
    L += ['  %-9s %-62s %s' % (kinds.get(n, '?'), n, got[n][0] if n in got else '### NOT PRINTED') for n in want]
    th = [n for n in want if kinds[n] == 'theorem']
    L += ['', '### ### **PRINTED : %d of %d ; THEOREMS AT THE STANDARD THREE OR FEWER : %d of %d ; ALL DECLARATIONS : %d of %d ; sorryAx : %s ; '
              'exit %s.**' % (sum(1 for n in want if n in got), len(want), sum(1 for n in th if std3.get(n)), len(th),
                              sum(1 for n in want if std3.get(n)), len(want), 'PRESENT' if sorry else 'NONE', rc)]
    put_txt('b623_sec_prints.txt', L)
    put_json('b623_profile.json', dict(lines=[got[n][0] for n in want if n in got], exit=rc, sorry=sorry, std3={n: std3.get(n, False) for n in want},
                                       kinds=kinds, printed_at=K.SEC_NAME + ' ' + K.SEC_BRANCH))
    print(L[-1])


def sec_tag(*a):
    """### v0.2.2 read back after push_gated: local and remote peels, the tag's type, the commit's parent and files (data/b623_sec_tag.json)."""
    refs = _remote(K.SEC_NAME)
    loc = _peel(K.SEC_NAME, K.SEC_TAG)
    rp = refs.get('refs/tags/%s^{}' % K.SEC_TAG)
    files = sorted(x for x in g(K.SEC, 'show', '--name-only', '--pretty=format:', loc).split(NL) if x.strip()) if loc else []
    parent = g(K.SEC, 'rev-parse', '--short=7', loc + '^').strip() if loc else ''
    d = dict(at=utc(), tag=K.SEC_TAG, local_peel=loc, remote_peel=rp, equal=bool(rp) and rp == loc,
             type=g(K.SEC, 'cat-file', '-t', 'refs/tags/' + K.SEC_TAG).strip(), parent=parent, files=files,
             remote_main=refs.get('refs/heads/main'), artefact_blob_sha256=sha(subprocess.run(['git', '-C', K.SEC, 'show', '%s:%s' % (loc, K.SEC_ARTEFACT)],
                                                                                              capture_output=True).stdout) if loc else None)
    put_json('b623_sec_tag.json', d)
    print('  %s : local %s remote %s equal %s ; %s ; parent %s ; files %s ; remote main %s' % (K.SEC_TAG, loc[:7], (rp or 'ABSENT')[:7], d['equal'],
                                                                                             d['type'], parent, files, (d['remote_main'] or '?')[:7]))


def table(*a):
    """### relay tools/terminal_table.py regenerated (it reads SIDE-structural-error-correction at its HEAD and relay's committed banked
    ### profiles); the diff banked as data/b623_table.txt and .json: the rows added, gone and changed."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    T = json.loads(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8').read())
    sec = [x for x in T['rows'] if x['repo'] == K.SEC_NAME]
    added = [list(x) if isinstance(x, list) else [x] for x in diff.get('added') or []]
    L = ['b623 -- COMPONENT 3: THE TERMINAL TABLE REGENERATED (%s); exit %d' % (utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d %s' % (len(added), len(diff.get('gone') or []), len(diff.get('changed') or []),
                                                                         diff.get('changed') or ''),
         '### the added rows: %s' % added, '', '### the SIDE-structural-error-correction rows now (%d):' % len(sec)]
    L += ['  %-62s %-9s %-12s %s' % (x['name'], x['grade'], x['profile_state'], x['profile']) for x in sec]
    L += ['', '### ### **ROWS ADDED : %d, OF THEM SIDE-structural-error-correction`S : %d ; GONE : %d ; CHANGED : %d ; SEC ROWS PROFILED : %d of %d.**' % (
        len(added), sum(1 for x in added if x and x[0] == K.SEC_NAME), len(diff.get('gone') or []), len(diff.get('changed') or []),
        sum(1 for x in sec if x['profile_state'] == 'PROFILED'), len(sec))]
    put_txt('b623_table.txt', L)
    put_json('b623_table.json', dict(at=utc(), rc=r.returncode, added=added, gone=diff.get('gone') or [], changed=diff.get('changed') or [],
                                     sec_rows=len(sec), sec_profiled=sum(1 for x in sec if x['profile_state'] == 'PROFILED'),
                                     sec_grades=sorted(set(x['grade'] for x in sec))))
    print(L[-1])


def tiers(*a):
    """### the b557 tier bank re-read for the SEC rows: each of its readings of a SIDE-structural-error-correction terminal, its profile
    ### against this act's print and its pin against the tag; the differences printed (data/b623_tiers_reread.txt and .json)."""
    TJ = json.loads(_rel('b557_tiers.json'))
    P = jl('b623_profile.json')
    got = {}
    for l in P['lines']:
        mm = PRINT_LINE.match(l)
        if mm:
            got[mm.group(1)] = mm.group(2)
    rows = []
    for doc, v in TJ.items():
        if not isinstance(v, dict):
            continue
        for t in v.get('terms') or []:
            if t['name'] in [x[3] for x in K.sec_exports()]:
                same_src = all(_show(K.SEC, K.SEC_PIN[1], m) == _show(K.SEC, K.SEC_TAG, m) for m in K.SEC_MODULES)
                rows.append(dict(doc=doc, row=t['row'], name=t['name'], pin=t['pin'], tier=t['tier'], b557_profile=t['profile'],
                                 b623_profile=got.get(t['name']), same=t['profile'] == got.get(t['name']), modules_same_at_tag=same_src))
    L = ['b623 -- COMPONENT 3: THE b557 TIER BANK (relay data/b557_tiers.json @ %s) RE-READ FOR THE SIDE-structural-error-correction ROWS (%s)' % (PRE_RELAY, utc()), '']
    L += ['  %-6s :%-4d %-50s %-4s b557 %-40s b623 %-40s %s' % (x['doc'][:6], x['row'], x['name'], x['tier'], x['b557_profile'], x['b623_profile'],
                                                               'SAME' if x['same'] else '### DIFFERS') for x in rows]
    L += ['', '### the two modules` blobs at %s and at %s identical: %s' % (K.SEC_PIN[1], K.SEC_TAG, all(x['modules_same_at_tag'] for x in rows) if rows else None),
          '### ### **READINGS RE-READ : %d ; PROFILES THE SAME : %d ; DIFFERING : %d ; TIERS MOVED : 0 (the tier is the bank`s; no grade is moved here).**' % (
              len(rows), sum(x['same'] for x in rows), sum(not x['same'] for x in rows))]
    put_txt('b623_tiers_reread.txt', L)
    put_json('b623_tiers_reread.json', dict(at=utc(), rows=rows))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe through b622's list; writes the page only when it changed;
    ### banks data/b623_page_<k>.json."""
    import chain_page as CP
    if k not in K.NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b623_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NODES[k]), pdir, os.path.join(D, K.PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b623_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    elif DRY:
        _write(os.path.join(SP, 'page_%s_dry.md' % k), b)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b623_page_%s.json' % k, dict(page=K.PNAME[k], nodes=K.NODES[k], probe=K.PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed,
                                           diff=dl, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; diff lines %d' % (k, rc, len(b), changed, secs, len(dl)))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b623 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s), after the kernel tag' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b623_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b623_page_arms.txt', L)
    for l in L:
        print(l[:240])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', K.CENSUS, 'day1/A_Place_to_Stand_v5_18.md',
            'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H57a', 'H57b', 'H57c', 'H57d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK


def _pp_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL)
            if l.strip()]


def _relay_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(RELAY, 'log', '--reverse', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def _alone(repo, files, commits):
    return [h for h, s in commits if _files(h, repo) == sorted(files)]


def _epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _lock():
    m = re.search(r'locked at \(UTC\) : (\S+)', rd('b623_registration_2026-10-04.txt') or '')
    return _epoch(m.group(1)) if m else None


def _after_lock(repo, h):
    lk = _lock()
    return lk is not None and int(g(repo, 'show', '-s', '--format=%ct', h).strip() or 0) > lk


HK_FILES = lambda: sorted(x['file'] for x in jx('b623_housekeeping.json').get('files') or [])   # noqa: E731


def n5(trail_line=None, ot=None, *a):
    """### N5, scored by its letter: nothing deposits; no main kernel file edited outside the tagged artefact branch; no keystone edited; no
    ### file written beyond the artefact module, the tags bank, the housekeeping lists, REGISTRY's notes, the table, the record-tool repair and
    ### its test, the re-emitted pages, the record lines and the trails. ### THE STANDING REPAIR (OPEN_TRAILS :12799): `trail_line` is the
    ### line the trail record's head takes on OPEN_TRAILS; a pending record is counted as OPEN_TRAILS' write."""
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
    face = jl('b623_kernels_face.json')['kernels']
    now = kern_state(list(face))
    others = [k for k in face if k != K.SEC_NAME]
    kern_ok = all(now[k][0] == face[k][0] and now[k][2] == face[k][2] and now[k][1] == face[k][1] for k in others)
    sec_files = _files(_peel(K.SEC_NAME, K.SEC_TAG), K.SEC) if _peel(K.SEC_NAME, K.SEC_TAG) else []
    sec_ok = sec_files == [K.SEC_ARTEFACT] and g(K.SEC, 'rev-parse', '--short=7', K.SEC_TAG + '^{commit}^').strip() == K.SEC_PIN[1]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])   # ### the pending record is OPEN_TRAILS' write when it is the act's only one there
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if jx('b623_page_%s.json' % k).get('changed')]
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md'] + pages)
    cur_ok = all((_show(PP, PRE_PP, p) or '') == (_show(PP, 'HEAD', p) or '') for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith(('b623_', 'audit_b623_', 'terminal_table'))
                              and x != 'data/b622_closing_push_out.txt'))
    allowed = set(HK_FILES()) | {'tools/b623_test_count.py'}
    beyond_allowed = [x for x in relay_beyond if x not in allowed]
    ok = kern_ok and sec_ok and cur_ok and pp_ch == want_pp and not beyond_allowed and rec_ok
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; the nine tag kernels and the seven read unmoved (main, tags by peel, branches) %s; SIDE-structural-error-correction`s '
            'tag adds %s on %s %s; the current versions and the census unedited %s; PLACE-papers %s (wanted %s); %s; relay beyond the act`s banks, '
            'the table, the housekeeping lists and the count test: %s' % (kern_ok, sec_files, K.SEC_PIN[1], sec_ok, cur_ok, pp_ch, want_pp, rec_state,
                                                                          beyond_allowed or 'NONE'))


def node_moves(k):
    """### N4's 'the pages' grades do not move': the node lines (`N. `name` ...`, where the grade cells sit) the re-emission's diff touches."""
    return [l for l in jx('b623_page_%s.json' % k).get('diff') or [] if re.match(r'^[+-]\d+\. `', l)]


def scores(*a):
    RB, TB = jx('b623_tags_readback.json'), jx('b623_tags.json')
    P, ST, TBL, TR = jx('b623_profile.json'), jx('b623_sec_tag.json'), jx('b623_table.json'), jx('b623_tiers_reread.json')
    PT, CT = jx('b623_push_test.json'), jx('b623_count_test.json')
    arms = rd('b623_page_arms.txt')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    ex = K.sec_exports()
    th = [n for _m, _l, k, n in ex if k == 'theorem']
    std3 = P.get('std3') or {}
    printed = set()
    for l in P.get('lines') or []:
        mm = PRINT_LINE.match(l)
        if mm:
            printed.add(mm.group(1))
    h57c = 'HOLDS' if th and all(n in printed and std3.get(n) for n in th) and P.get('sorry') is False and P.get('exit') == 0 else 'REFUTED'
    added = TBL.get('added') or []
    h57d = 'HOLDS' if TBL and added and all(x and x[0] == K.SEC_NAME for x in added) and len(added) == len(ex) and not TBL.get('gone') \
        and not TBL.get('changed') else 'REFUTED'
    rows = RB.get('rows') or []
    cited = [x for x in rows if x['cited']]
    rc = _relay_commits()
    pg = _alone(RELAY, list(PUSH_FILES), rc)
    cc = _alone(RELAY, list(COUNT_FILES), rc)
    face = jx('b623_kernels_face.json').get('kernels') or {}
    now = kern_state(list(K.TAG_KERNELS)) if face else {}
    unmoved = bool(face) and all(now[k][0] == face[k][0] and all(now[k][1].get(t) == p for t, p in face[k][1].items())
                                 and set(now[k][1]) == set(face[k][1]) for k in K.TAG_KERNELS)
    tiers_same = bool(TR.get('rows')) and all(x['same'] for x in TR['rows']) and len(TR['rows']) >= 6
    arms_ok = 'PAGE ARMS PASSING : 2 of 2' in arms and 'PASSING : 2 of 2.**' in arms.split('PAGE ARMS PASSING')[-1]
    S = {
        'H57a': (RB.get('H57a', 'REFUTED'), 'pushed %d, read back equal %d' % (sum(x['pushed'] for x in rows), sum(x['equal'] for x in rows if x['pushed']))),
        'H57b': (RB.get('H57b', 'REFUTED'), 'cited %d of %d, each pushed %s; uncited %d, none pushed %s' % (
            len(cited), len(rows), all(x['pushed'] for x in cited), len(rows) - len(cited), not any(x['pushed'] for x in rows if not x['cited']))),
        'H57c': (h57c, 'theorems %d, printed %d, within the standard three %d, sorryAx %s, exit %s; all %d declarations within it %d' % (
            len(th), sum(1 for n in th if n in printed), sum(1 for n in th if std3.get(n)), P.get('sorry'), P.get('exit'), len(ex),
            sum(1 for n in std3 if std3[n]))),
        'H57d': (h57d, 'rows added %d (SEC %d, the exports %d), gone %d, changed %d' % (len(added), sum(1 for x in added if x and x[0] == K.SEC_NAME),
                                                                                    len(ex), len(TBL.get('gone') or []), len(TBL.get('changed') or []))),
        'N1': (('HELD' if len(cited) >= 4 and all(x['pushed'] for x in cited) and not any(x['pushed'] for x in rows if not x['cited']) else 'REFUTED'),
               'cited and pushed %d of 12 (at least four); the rest recorded local %d, housekeeping files %s' % (
                   sum(1 for x in cited if x['pushed']), len(rows) - len(cited), HK_FILES())),
        'N2': (('HELD' if rows and all(x['equal'] for x in rows if x['pushed']) and any(x['pushed'] for x in rows) else 'REFUTED'),
               'every pushed tag`s peel read back equal: %d of %d' % (sum(x['equal'] for x in rows if x['pushed']), sum(x['pushed'] for x in rows))),
        'N3': (('HELD' if th and all(n in printed and std3.get(n) for n in th) and P.get('sorry') is False else 'REFUTED'),
               'theorems within the standard three %d of %d, sorryAx %s' % (sum(1 for n in th if std3.get(n)), len(th), P.get('sorry'))),
        'N4': (('HELD' if h57d == 'HOLDS' and arms_ok and all(jx('b623_page_%s.json' % k).get('rc') == 0 and not node_moves(k) for k in ('zeta', 'chi'))
                else 'REFUTED'), 'the table gains the SEC rows alone %s; the page arms %s; node lines of the pages moved at the re-emission %s' % (
                    h57d, arms_ok, {k: node_moves(k) for k in ('zeta', 'chi')})),
        'N5': (n5v[0], n5v[1] + ' ### relay tools/push_gated.sh with its test, edited after the seal by the author`s answer before it, is a '
               'shared tool the expectation`s list does not name' + (' (committed %s)' % pg if pg else '')),
        'S1': (('HELD' if len(pg) == 1 and _after_lock(RELAY, pg[0]) and PT.get('cases') and PT.get('cases') == PT.get('passing') else 'REFUTED'),
               'push_gated.sh and its test in one relay commit of their own %s, after the lock %s; the test`s cases %s, passing %s' % (
                   pg, bool(pg) and _after_lock(RELAY, pg[0]), PT.get('cases'), PT.get('passing'))),
        'S2': (('HELD' if len(cc) == 1 and _after_lock(RELAY, cc[0]) and CT.get('repaired_all_pass') is True and CT.get('sealed_refuted') is True else 'REFUTED'),
               'the record tool`s count repair and its test in one relay commit of their own %s, after the lock %s; the test against the repaired '
               'counter all passing %s, against the sealed one refuted %s' % (cc, bool(cc) and _after_lock(RELAY, cc[0]), CT.get('repaired_all_pass'),
                                                                               CT.get('sealed_refuted'))),
        'S3': (('HELD' if unmoved else 'REFUTED'), 'the nine kernels` mains and every local tag by name and peel against the face: %s' % unmoved),
        'S4': (('HELD' if ST.get('equal') and ST.get('files') == [K.SEC_ARTEFACT] and ST.get('parent') == K.SEC_PIN[1] and ST.get('type') == 'tag'
                else 'REFUTED'), 'v0.2.2 read back equal %s, annotated %s, parent %s, files %s' % (ST.get('equal'), ST.get('type'), ST.get('parent'),
                                                                                               ST.get('files'))),
        'S5': (('HELD' if tiers_same else 'REFUTED'), 'b557`s readings of SEC terminals re-read %d, profiles the same %d' % (
            len(TR.get('rows') or []), sum(x['same'] for x in TR.get('rows') or []))),
    }
    put_json('b623_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 5: THE RECORD
TRAIL_HEAD = ('### b623 — lane three, act fifty under (R233): the unpushed tags settled by citation; the de-alignment kernel’s axiom artefact '
              'printed and its rows entered; four research work-orders and one arm entered')


def _title_entry():
    RB, TBL, P = jx('b623_tags_readback.json'), jx('b623_table.json'), jx('b623_profile.json')
    rows = RB.get('rows') or []
    th = [n for _m, _l, k, n in K.sec_exports() if k == 'theorem']
    std = sum(1 for n in th if (P.get('std3') or {}).get(n))
    return ('## The unpushed tags: %d pushed by citation and %d recorded local across nine kernels; SIDE-structural-error-correction’s axiom '
            'artefact at v0.2.2, %d terminals at the standard three, %d rows entered; four research work-orders priced' % (
                sum(1 for x in rows if x['pushed']), sum(1 for x in rows if not x['pushed']), std, len(TBL.get('added') or [])))


def _finding_text():
    S, rl, RB, TB = (jl(n) for n in ('b623_scores.json', 'b623_record_lines.json', 'b623_tags_readback.json', 'b623_tags.json'))
    P, ST, TBL, TR, OF = (jl(n) for n in ('b623_profile.json', 'b623_sec_tag.json', 'b623_table.json', 'b623_tiers_reread.json', 'b623_offering.json'))
    RG = jl('b623_registry.json')
    t = _title_entry()
    rows = RB['rows']
    pushed = [x for x in rows if x['pushed']]
    local = [x for x in rows if not x['pushed']]
    one = [r for r in TB['rows'] if r['cited'] and r['remote_same_commit']]
    ex = K.sec_exports()
    th = [n for _m, _l, k, n in ex if k == 'theorem']
    pc = _pp_commits()
    reg_c = ([h for h, s in pc if _files(h) == ['REGISTRY.md']] or ['?'])[0]
    rc = _relay_commits()
    pg = (_alone(RELAY, list(PUSH_FILES), rc) or ['?'])[0]
    cc = (_alone(RELAY, list(COUNT_FILES), rc) or ['?'])[0]
    hk = ([h for h, s in rc if _files(h, RELAY) == ['data/terminal_table.json', 'data/terminal_table.md', 'data/terminal_table_diff.json',
                                                    'data/terminal_table_prior.json', 'data/terminal_table_run.txt']] or ['?'])[0]
    e = ['', t, '',
         '*Filed at b623 on the author’s ruling `(R233)` and the author’s two answers before the seal. Banks: relay `data/b623_tags.txt`, '
         '`data/b623_tags_readback.txt`, `data/b623_sec_exports.txt`, `data/b623_sec_prints.txt`, `data/b623_profile.json`, `data/b623_table.txt`, '
         '`data/b623_tiers_reread.txt`, `data/b623_push_test.txt`, `data/b623_offering.txt`, `data/b623_author_answers.txt`. Nothing deposits.*', '',
         '**The tags** (`(R233)`(5)(a), W-ORD-TAG-REMOTES, OPEN_TRAILS :12597): the twelve tags the census’s cells name unpushed, in nine kernels, '
         'each read with its peeled commit, its remote and every line of REGISTRY, FINDINGS, SPIRAL_MAP (and its v0.7) and the two pages citing it '
         'at PLACE-papers c9e9a9c -- by b611’s prose matcher and, by the author’s answer before the seal, a version cell beside the kernel’s '
         'own cell in SPIRAL_MAP’s federation table. %d cited, each pushed one at a time through `tools/push_gated.sh`’s existing-tag mode '
         '(added after the seal by the author’s other answer, its test %d of %d checks, relay %s), the peeled commit read back equal at its '
         'remote, H57a %s: %s. %d cited by no ledger and recorded local: %s. Of the cited, %d sit on the commit their remote already tags '
         'v0.1.0 (%s), each recorded in its kernel’s housekeeping list as one commit with the cited name kept. No tag moved or re-pointed; '
         'H57b %s. REGISTRY’s row note :628 corrected by a dated row update in its own form (PLACE-papers %s, alone, :%d).' % (
             len(pushed), jl('b623_push_test.json')['passing'], jl('b623_push_test.json')['cases'], pg, S['H57a'][0],
             ', '.join('%s %s' % (x['kernel'][5:], x['tag']) for x in pushed), len(local), ', '.join('%s %s' % (x['kernel'][5:], x['tag']) for x in local),
             len(one), ', '.join('%s %s' % (r['kernel'][5:], r['tag']) for r in one), S['H57b'][0], reg_c, RG['line']), '',
         '**The artefact** (`(R233)`(5)(b), W-ORD-SEC-AXIOM-ARTEFACT, OPEN_TRAILS :12330): SIDE-structural-error-correction’s %d declarations '
         'at v0.2.1 (%d theorems, the terminals; the six de-alignment theorems and `d_eff_formula` and `silence_yields_protection` among them) '
         'each given `#print axioms` in `AxiomCheck.lean`, the house form of SIDE-explicit-formula’s audits, on the branch %s, built one module '
         'per call by a detached process watched from the foreground at the memory hold; tagged %s by `tools/push_gated.sh`, peeled %s, read '
         'back equal %s, the tag adding that one file on v0.2.1. The prints: %d of %d theorems within the standard three, no `sorryAx`; %d '
         'of the %d declarations depend on no axiom at all. The table regenerated: %d rows added, all the kernel’s, %d profiled from the '
         'banked prints, none gone, no grade moved (relay %s, alone); H57c %s, H57d %s. b557’s tier bank re-read: %d readings, %d profiles '
         'the same, the modules unchanged at the tag.' % (
             len(ex), len(th), K.SEC_BRANCH, K.SEC_TAG, (ST['local_peel'] or '?')[:7], ST['equal'],
             sum(1 for n in th if P['std3'].get(n)), len(th), sum(1 for l in P['lines'] if 'does not depend on any axioms' in l), len(ex),
             len(TBL['added']), TBL['sec_profiled'], hk, S['H57c'][0], S['H57d'][0], len(TR['rows']), sum(x['same'] for x in TR['rows'])), '',
         '**The record lines** (`(R233)`(1)-(4)): b622’s weight at FINDINGS :%d; on OPEN_TRAILS the three nodes ruled UNIVERSAL with the bundle '
         'clause (:%d, to :12266), the test count standing (:%d, to :12799) and the four work-orders (:%d-:%d). The record tool’s count repaired '
         'after the seal with its test, alone (relay %s). The arm of `(R233)`(4) in this act’s suite: %d entries since b594, %d carrying the '
         'offering line, %d without.' % (rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                                         rl['lines'][6]['line'], cc, OF['entries'], OF['carrying'], OF['without']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it settles the tags b610’s census found carried by the clones alone (:7212) and '
         'b619’s census printed in its cells (:7404); it gives the de-alignment kernel the printed profile b598’s grades lacked and b599 priced '
         '(OPEN_TRAILS :12330), re-reading b557’s tier bank on its own prints. It strengthens the programme’s offering of a federation a reader '
         'can follow by its ledgers: every tag a ledger names now resolves at its remote, and every terminal the de-alignment kernel exports '
         'carries a printed profile in the table.', '',
         '**Next.** Per `(R233)`(6): b624, W-ORD-E0-INDUCTION and W-ORD-ACT-ROOT in one act. The author rules on the closing.', '',
         '*Nothing deposits; no kernel file edited but the artefact module added on its branch; no keystone edited; nothing here is a statement '
         'about RH, GRH or any zero.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b623_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) a citation is a ledger line of REGISTRY, FINDINGS, SPIRAL_MAP (its current file and v0.7) or the two pages naming the kernel '
              'and the tag as a whole version -- b611’s prose matcher, or a version cell beside the kernel’s own cell -- read at PLACE-papers '
              'c9e9a9c, before this act’s own REGISTRY note; OPEN_TRAILS, ERRATA, the loom and README printed beside and not counted; (2) the '
              'refinement for the tags on a commit the remote already tags v0.1.0 applied to all five that meet its description (bijection v0.1 '
              'among them), the figure “four” in the author’s answer being the seat’s own miscount relayed in the prompt; (3) the artefact '
              'prints every declaration of both modules in the house form, its theorems the terminals H57c and N3 score; “at the standard three” '
              'read as within it; (4) the prints banked in relay `data/b623_profile.json`, the form W-ORD-TABLE-PROFILE-JSON reads, so the rows '
              'come in profiled; (5) the page arm “after the kernel tag” run after v0.2.2 in Component 4, the pre-seal run at HEAD being the '
              'suite’s prerun')


def _trail_text():
    S, fj, rl, RB = (jl(n) for n in ('b623_scores.json', 'b623_findings.json', 'b623_record_lines.json', 'b623_tags_readback.json'))
    ST, TBL, RG = (jl(n) for n in ('b623_sec_tag.json', 'b623_table.json', 'b623_registry.json'))
    pc = _pp_commits()
    ec = lambda p: ' '.join([h for h, s in pc if _files(h) == [p]]) or '?'   # noqa: E731
    rc = _relay_commits()
    pg = (_alone(RELAY, list(PUSH_FILES), rc) or ['?'])[0]
    cc = (_alone(RELAY, list(COUNT_FILES), rc) or ['?'])[0]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R233) ratified.** (1) b622 at its weight. (2) The three UNCLASSIFIED nodes ruled UNIVERSAL; the bundle clause. (3) The test count, '
             'standing. (4) Four work-orders and one arm. (5) W-ORD-TAG-REMOTES and W-ORD-SEC-AXIOM-ARTEFACT; H57a-H57d. (6) The act after: b624.', '',
             '**Entered:** FINDINGS.md:%d (b622’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d (the three nodes and the '
             'bundle clause, to :12266), :%d (the test count, to :12799), :%d-:%d (the four work-orders); this record; REGISTRY.md :%d (%s); relay '
             'tools/push_gated.sh and tools/test_push_gated.sh %s; relay tools/b623_record.py and tools/b623_test_count.py %s; relay %s; '
             'SIDE-structural-error-correction %s = %s (AxiomCheck.lean on %s); relay data/b623_tags.txt, data/b623_tags_readback.txt, '
             'data/b623_sec_prints.txt, data/b623_profile.json, data/b623_table.txt, data/b623_tiers_reread.txt.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'], rl['lines'][6]['line'],
                 RG['line'], ec('REGISTRY.md'), pg, cc, ', '.join('data/' + os.path.basename(f) for f in HK_FILES()), K.SEC_TAG, (ST['local_peel'] or '?')[:7],
                 K.SEC_BRANCH), '',
             '**The author’s two answers before the seal** (relay data/b623_author_answers.txt): push_gated.sh gains an existing-tag mode after '
             'the seal through the Edit tool, with a case in its test, the edit and test committed alone, N5 refuted in its letter by that one '
             'shared-tool edit; a version cell in SPIRAL_MAP’s federation table is a citation, so nine are cited and pushed and three recorded '
             'local, and the tags on a commit the remote already tags v0.1.0 recorded in their kernels’ housekeeping lists as one commit, the '
             'cited name kept in the ledgers as written.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b623_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R233)`(6), b624, W-ORD-E0-INDUCTION and W-ORD-ACT-ROOT in one act; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel file edited but the artefact module added; row U1 unedited; `h2` where the '
             'deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e[:9000])
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b623_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b623_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-04 by b623 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    """### OPEN_TRAILS: a correction to the record, its text read from data/b623_defects.json (`correction`), addressed to the record and
    ### appended at the end; `dry` prints it. Nothing is written when the bank carries no correction."""
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b623_defects.json -- NOTHING WRITTEN')
    rec = Q.line_of(Q.OT, TRAIL_HEAD)
    t = '\n%s %s\n' % (CORR_HEAD % rec, CORRECTION)
    bad = ledger_check(t)
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'correction')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(t)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CORR_HEAD % rec)
    r = Q.append_to(Q.OT, t)
    put_json('b623_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec), head=CORR_HEAD % rec, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec))


def desk(*a):
    S = jl('b623_scores.json')
    L = ['=' * 104, 'b623 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H57a-H57d, (R233)(5).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H57 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b623_defects.txt').rstrip(NL).split(NL)
    put_txt('b623_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = (jl(n) for n in ('b623_scores.json', 'b623_findings.json', 'b623_trail.json', 'b623_record_lines.json'))
    RB, ST, TBL, RG = (jl(n) for n in ('b623_tags_readback.json', 'b623_sec_tag.json', 'b623_table.json', 'b623_registry.json'))
    L = ['b623 -- THE COMPONENTS, BANKED UNDER (R233).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b622`s closing push-out relay %s ; push-b622* branches deleted by name '
         '(data/b623_branches.txt) ; the kept branches untouched ; the suite, its sources repaired and the offering-line arm added, run at HEAD before '
         'the face (data/b623_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b622`s weight FINDINGS :%d ; OPEN_TRAILS :%d (the nodes and the bundle clause), :%d (the test count), :%d-:%d (the work-orders) ; '
         'the count repair data/b623_count_test.txt' % (rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                                                         rl['lines'][6]['line']),
         '### COMPONENT 2 : the tags data/b623_tags.txt ; push_gated`s mode data/b623_push_diff.txt, its test data/b623_push_test.txt ; the read-back '
         'data/b623_tags_readback.txt ; housekeeping %s ; REGISTRY :%d ; H57a %s, H57b %s' % (HK_FILES(), RG['line'], S['H57a'][0], S['H57b'][0]),
         '### COMPONENT 3 : the exports data/b623_sec_exports.txt ; the prints data/b623_sec_prints.txt, data/b623_profile.json ; %s = %s ; the table '
         'data/b623_table.txt (added %d) ; the tiers data/b623_tiers_reread.txt ; H57c %s, H57d %s' % (K.SEC_TAG, (ST['local_peel'] or '?')[:7],
                                                                                                   len(TBL['added']), S['H57c'][0], S['H57d'][0]),
         '### COMPONENT 4 : the pages changed %s and %s ; page arms data/b623_page_arms.txt' % (jx('b623_page_zeta.json').get('changed'),
                                                                                            jx('b623_page_chi.json').get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b624 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b623_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b623_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
