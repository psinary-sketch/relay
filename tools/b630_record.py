# -*- coding: utf-8 -*-
"""b630_record.py -- THE ACT'S RECORD TOOL, UNDER (R240). ### ONE SUBCOMMAND PER BANK.

### ### b630: LANE THREE, ACT FIFTY-SEVEN -- THE NYMAN–BEURLING DISTANCES d_N² IN ARB BALLS BESIDE 2λ₁ FROM THE KERNEL; NEW ROWS
### GRADED FROM THE RULE WITH PROVENANCE; HELPER ROWS AS OBJECTS; THE PROBE HOLD; THE OUTBOUND-IDENTIFIER LINE.
### Subcommands write only `data/b630_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`. The data is tools/b630_worklist.py. The registry records of the bench are read by the seat once each, by
### curl with no header, into the scratchpad; this tool reads the captures and never calls a platform. The case counter is (R233)(3)'s.
### b628's full intake bank (relay data/b628_intake_crank_v0_5.txt) is never read here past its header, never staged or committed.
"""
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
import b604_record as R4  # noqa: E402
import b630_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
SESSION_ID = 'f5c41941-fa74-40e9-b806-a98e7280e315'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b630_registration_2026-10-05.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')


def _w(name):
    return os.path.join(SP if DRY else D, name)


def _r(name):
    return os.path.join(D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _w(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_r(name), encoding='utf-8'))


def jx(name):
    return jl(name) if os.path.exists(_r(name)) else {}


def rd(name):
    p = _r(name)
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


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b630_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b630 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b630_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the edition form, the precedence and authority orders, the build clause, the N5 line, the face`s work-order (the '
         'bench half), the Dedekind work-order, b629`s three corrections', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12228, 12354, 12356, 12799, 12893, 12895, 13119, 13121, 13123], 1500),
        ('FINDINGS: b629`s entry', PP, PRE_PP, 'FINDINGS.md', [7635], 600),
        ('SIDE-explicit-formula v0.24: the dilation, d_N and its monotonicity (NymanBeurling.lean)', K.KER, 'v0.24', K.FACE_FILE,
         [32, 41, 44, 67, 70, 94, 95, 96, 97, 101], 300),
        ('SIDE-explicit-formula v0.20: Keiper`s λ₁ (Keiper.lean)', K.KER, 'v0.20', K.LICOEFF['file'], [238, 239, 240], 300),
        ('SIDE-explicit-formula v0.20: the sign of λ₁ (KeiperSign.lean)', K.KER, 'v0.20', 'SIDEExplicitFormula/KeiperSign.lean', [6, 7, 30, 31, 82], 300),
        ('relay tools/terminal_table.py: the grade column', RELAY, PRE_RELAY, 'tools/terminal_table.py',
         ('GREP', r'^GRADES =|^def (build|emit|statement|grade_cells)\(|UNGRADED'), 300),
        ('relay tools/chain_page.py: the probe entry point and the node-list reader', RELAY, PRE_RELAY, 'tools/chain_page.py',
         ('GREP', r'^def (read_nodes|probe_imports|probe_text|build|source_header)\(|HOLD_MB|free_mb'), 300),
        ('relay tools/b627_margin.py: the Arb pattern and the ball printing form', RELAY, PRE_RELAY, 'tools/b627_margin.py',
         ('GREP', r'^from flint|ctx\.prec|acb\.integral|def _s\(|def _r\(|\.str\('), 300),
        ('relay data/b629_defects.txt', RELAY, PRE_RELAY, 'data/b629_defects.txt', ('GREP', r'^    \('), 400),
        ('relay data/b629_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b629_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b630 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        if rev is None:      # ### a file read on disk (the local bank), never by git: it is in no commit
            at = 'disk (untracked)'
            p = os.path.join(ROOT, *path.split('/'))
            t = io.open(p, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(p) else None
        else:
            at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
            t = _show(repo, rev, path)
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
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                         g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b630_reads.txt', L)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R240) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def _calls():
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
    return [c for c in calls if c[0] > act_from()], results


def answers(*a):
    since, results = _calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b630 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b630_author_answers.txt', L)


def answer_of(k):
    """### the author's answer to the act's k-th prompt (0-based, across calls), whole: cut from the result after its own question's
    ### `"<question>"="` and before the next question's `", "<question>"="`, the questions read from the bank's prompt headers."""
    t = rd('b630_author_answers.txt')
    qs = []
    for blk in re.split(r'^### CALL ', t, flags=re.M)[1:]:
        res = re.search(r'^RESULT \(transcript line \d+\): (.*)', blk, re.M | re.S)     # ### the result runs to the call's end
        for q in re.findall(r'^### PROMPT \d+ \([^)]*\): (.*)$', blk, re.M):
            qs.append((q, ' '.join(res.group(1).split()) if res else ''))
    if len(qs) <= k:
        return 'no answer banked'
    q, r = qs[k]
    a = r.find('"%s"="' % q)
    if a < 0:
        return 'no answer banked'
    a += len(q) + 4
    ends = [r.find('", "%s"="' % q2, a) for q2, r2 in qs if r2 == r and q2 != q] + [r.find('". You can now continue', a), r.find('". Read the answers', a)]
    ends = [e for e in ends if e >= 0]
    return r[a:min(ends)].strip() if ends else r[a:].strip()


def _elide(text):
    """### the author's answer as banked, a sentence carrying one of the scanner's own stems elided and marked so, never reworded."""
    import banned_terms as BT
    rx = re.compile(r'(%s)' % '|'.join(re.escape(s) for s in BT.STEMS), re.I)
    return ' '.join('[a sentence elided here under the scanner’s stem rule, verbatim in the bank]' if rx.search(s) else s
                    for s in re.split(r'(?<=[.;])\s+', text))


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-fano-darkness', 'SIDE-li-map')
KERN_PIN = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7',
            'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab', 'SIDE-global-section': '17ce9ff'}
WRITTEN_KERNS = ()   # ### b630 writes no kernel


def kern_state(ks=None):
    out = {}
    for k in (ks or KERNS):
        p = 'D:/' + k
        tags = {}
        for l in g(p, 'for-each-ref', '--format=%(refname:short) %(objectname) %(*objectname)', 'refs/tags').split(NL):
            if l.strip():
                x = l.split()
                tags[x[0]] = (x[2] if len(x) > 2 else x[1])[:7]
        out[k] = [g(p, 'rev-parse', '--short=7', 'main').strip(), tags,
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()),
                  g(p, 'status', '--porcelain', '--untracked-files=no').strip()]
    return out


def kernels(*a):
    put_json('b630_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ THE LEDGER HELPERS
def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def predict_cells(text, ledger):
    import terminal_table as TT
    out = []
    for i, ln in enumerate(text.split(NL)):
        if not TT.GRADE_RE.search(ln):
            continue
        own = TT.FIND_SUP_RE.search(ln) if ledger == 'FINDINGS.md' else None
        for off, seg in TT._segments(ln):
            gs_ = [(m.start(), m.end(), m.group(1)) for m in TT.GRADE_RE.finditer(seg)]
            names = TT._names_on(seg)
            for g0, g1, gr in gs_:
                best, bd = None, None
                for a0, b0, nm in names:
                    d = abs((g0 - b0) if g0 >= b0 else (a0 - g1))
                    if d <= TT.WINDOW and (bd is None or d < bd):
                        best, bd = nm, d
                if best is not None and not (own and (best == own.group(2) or best.endswith('.' + own.group(2)))):
                    out.append((i, best, gr))
    return out


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b630_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _land(Q, items, bank, entry=None):
    want = {}
    n = {'FINDINGS.md': len(lines_of(io.open(Q.FIND, encoding='utf-8').read().replace(chr(13), ''))),
         'OPEN_TRAILS.md': len(lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), '')))}
    for f, h, t in items:
        want[h] = n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        Q.guard_absent(Q.FIND if f == 'FINDINGS.md' else Q.OT, h)
    out = []
    for f, h, t in items:
        path = Q.FIND if f == 'FINDINGS.md' else Q.OT
        r = Q.append_to(path, t)
        got = Q.line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


def _guarded(items, ledger, name):
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(allt, ledger)
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, name)
    print('  table cells these lines would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    return cells, nd, clean


# ================================================================================ COMPONENT 1: THE RECORD LINES
B629_ENTRY = 7635
W_HEAD = '*Appended 2026-10-05 by b630 to b629’s entry (:%d), under `(R240)`(1) -- b629 AT ITS WEIGHT:*'
OI_HEAD = '*Appended 2026-10-05 by b630 beneath the form of an edition (:11864), under `(R240)`(2)(i) -- NO OUTBOUND IDENTIFIER, STANDING:*'
PV_HEAD = ('*Appended 2026-10-05 by b630, under `(R240)`(3) and the author’s answer before b630’s seal (relay data/b630_author_answers.txt, '
           'prompt 1) -- THE TABLE’S PROVENANCE COLUMN, A CLAUSE:*')
HL_HEAD = ('*Appended 2026-10-05 by b630, under `(R240)`(4) and the author’s answer before b630’s seal (relay data/b630_author_answers.txt, '
           'prompt 2) -- HELPER DECLARATIONS AS ROWS AND NODES, A CLAUSE:*')
NY_HEAD = '*Appended 2026-10-05 by b630 to W-ORD-NYMAN-BEURLING-FACE (:12893), under `(R240)`(1) -- AN ITEM, NYMAN’S THESIS AT A REGISTRY:*'
TR_HEAD = ('*Appended 2026-10-05 by b630, under the author’s answer before b630’s seal (relay data/b630_author_answers.txt, prompt 1) -- '
           'W-ORD-TABLE-RULE-GRADES, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD:*')


def _weight(entry):
    return ('\n%s SIDE-explicit-formula v0.24 = aa17442 on the kept branch nb-b629: NymanBeurling.lean and its audit module; '
            'measurability and square-integrability of the dilation family proved from Mathlib, no obligation named; NB and BD stated; '
            'rh_iff_nb read at the named premise NymanBeurlingPremise alone and distN_antitone read without hypothesis by the shared rule; '
            '13 declarations at the standard three, no sorryAx; the tag’s peel equal locally and at the remote; the lake build that exited '
            '0 standing and the audit run by lake env lean. The citation: Beurling’s record matching the recollection; Báez-Duarte’s record '
            'an arXiv posting of 2002-02-15 with no journal reference, the year 2003 the navigator’s, unconfirmed and not written; Nyman’s '
            'thesis on recollection alone, the docstring saying so. The b592 test 8 of 8 (relay b76ce426); the keystone guard extended to '
            'upper-case short names (relay 830d2974, 8 of 8), the ζ page emitted twice, the two false rows gone, 218 grade cells unmoved. '
            'H63a to H63c held; H63d refuted on its scorer’s letter alone, 0 existing grades moved (OPEN_TRAILS :13119); N1 to N4 held, N5 '
            'refuted in letter by the ordered repair. The root 219ae8b5…, b624 to b629 agreeing; relay 89fa8fd0, PLACE-papers 655e2d2. The '
            'suite 78 of 82, the four arms named and each claim tested directly; defects (a) to (k) the seat’s (relay data/b629_defects.txt). '
            'The local intake bank untracked. Nothing deposited.\n' % (W_HEAD % entry))


def _outbound():
    return ('\n%s no identifier of the author (address, name, token) is placed in any outbound header, URL or payload by either seat '
            'unless the author asks in the act’s own words; a registry’s polite pool is declined. From b629’s defect (a): the author’s '
            'address sent in two Crossref User-Agent headers, unasked.\n' % OI_HEAD)


def _provenance():
    return ('\n%s a table row without a ledger cell takes the shared E0 rule’s reading at the pin as its grade, with the provenance '
            'mark rule beside it, until a ledger cell is written; then the cell governs and the mark is cell. A row graded by cells reads '
            'cell; a row with neither reads none. The rule applies to rows new to the table from b630 on (a row absent from the table at '
            'relay 75227e9c): the thirteen rows of v0.24 take their grades so in this act; the 1799 rows ungraded before it keep their '
            'state, their rule readings counted and banked, not applied (relay data/b630_table_rule_readings.txt), by the author’s answer. '
            'A row whose rule reading and cell disagree is printed, as b625’s 33 were.\n' % PV_HEAD)


def _helpers():
    return ('\n%s helper declarations that are defs or instances (unitMeasure, rho and constOne at v0.24, and their like) are table '
            'rows at DEF with the object shape — and enter the node list as objects; a helper that is a theorem is a theorem, graded by '
            'the rule and its shape read by the column as every theorem’s is (rhoFun_bound at v0.24). The ruling’s listing of rhoFun_bound '
            'among the defs is corrected so, by the author’s answer.\n' % HL_HEAD)


def _nyman():
    return ('\n%s a registry record for Bertil Nyman’s thesis (Uppsala, 1950) is sought, read once and printed beside the '
            'recollection; until one is read the module’s docstring names the thesis on the recollection alone, as it does at v0.24. '
            'Price: one read in an act that reads registries. Not started.\n' % NY_HEAD)


def _rule_grades_wo():
    R = jx('b630_table_rule_readings.json')
    return ('\n%s Items: the shared E0 rule’s grades applied to the table rows that have no ledger cell, row by row with the move '
            'printed; a seeded sample of the moves put to the second reader by the batch form before the table is pushed; both pages '
            're-emitted; the count of rows read at a named premise that result printed beside the count of named premises they rest on. '
            'The fact the item starts from: nine-tenths of the terminal table has no grade from any ledger -- %s of %s rows ungraded, %s of '
            'them carrying a statement the rule can read (relay data/b630_table_rule_readings.txt, this work-order’s input). Price: one act. '
            'Trigger: the author’s word. Not started.\n' % (TR_HEAD, R.get('ungraded', '?'), R.get('rows', '?'), R.get('readable', '?')))


def record_lines(*a):
    """### FINDINGS: b629's weight (to its entry :7635). OPEN_TRAILS: the outbound-identifier line beneath :11864, the provenance
    ### clause, the helper clause, the Nyman item (to :12893), W-ORD-TABLE-RULE-GRADES. No line makes a table cell (predicted)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The Nyman–Beurling face at v0.24')
    if entry != B629_ENTRY:
        sys.exit('### b629`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    if not jx('b630_table_rule_readings.json'):
        sys.exit('### THE RULE READINGS ARE NOT BANKED -- NOTHING WRITTEN')
    items = [('FINDINGS.md', W_HEAD % entry, _weight(entry)), ('OPEN_TRAILS.md', OI_HEAD, _outbound()),
             ('OPEN_TRAILS.md', PV_HEAD, _provenance()), ('OPEN_TRAILS.md', HL_HEAD, _helpers()), ('OPEN_TRAILS.md', NY_HEAD, _nyman()),
             ('OPEN_TRAILS.md', TR_HEAD, _rule_grades_wo())]
    cells, nd, clean = _guarded(items, 'OPEN_TRAILS.md', 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    print('  backtick parity odd in: %s' % (ticks or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean or ticks:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR ODD BACKTICKS -- NOTHING WRITTEN')
    _land(Q, items, 'b630_record_lines.json', entry)


# ================================================================================ COMPONENT 2: THE TABLE AND THE LIST
def rule_readings(*a):
    """### every table row ungraded by the ledgers, its rule reading at its statement as the table prints it (terminal_table's own
    ### rule_reading): counted by kind, by reading and by repository, and banked row by row; NOT applied (the author's answer, prompt 1).
    ### Reads relay HEAD's committed table (data/b630_table_rule_readings.txt and .json)."""
    import terminal_table as TT
    T = json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))
    rows = T['rows']
    ung = [r for r in rows if r['grade'] == 'UNGRADED']
    out, kinds, reads_, repos = [], {}, {}, {}
    for r in ung:
        kind, gr = TT.rule_reading(r.get('statement'), r['name'])
        out.append(dict(repo=r['repo'], name=r['name'], kind=kind, reading=gr))
        kinds[kind] = kinds.get(kind, 0) + 1
        reads_[gr] = reads_.get(gr, 0) + 1
        if gr is not None:
            repos[r['repo']] = repos.get(r['repo'], 0) + 1
    readable = sum(1 for x in out if x['reading'] is not None)
    L = ['b630 -- COMPONENT 2, (R240)(3): THE RULE READINGS OF THE TABLE`S UNGRADED ROWS, COUNTED AND BANKED, NOT APPLIED (%s)' % utc(), '',
         '### the table at relay HEAD %s: %d rows ; ungraded by any ledger %d (%.1f%%) ; readable by the rule %d' % (
             g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), len(rows), len(ung), 100.0 * len(ung) / len(rows), readable),
         '### by declaration kind: %s' % kinds, '### by the rule`s reading: %s' % {str(k): v for k, v in reads_.items()},
         '### readable rows by repository: %s' % dict(sorted(repos.items(), key=lambda x: -x[1])), '',
         '### row by row (repository | name | kind | the rule`s reading), the input of W-ORD-TABLE-RULE-GRADES:']
    L += ['  %s | %s | %s | %s' % (x['repo'], x['name'], x['kind'], x['reading']) for x in out]
    put_txt('b630_table_rule_readings.txt', L)
    put_json('b630_table_rule_readings.json', dict(at=utc(), rows=len(rows), ungraded=len(ung), readable=readable, kinds=kinds,
                                                   readings={str(k): v for k, v in reads_.items()}, repos=repos))
    print(L[2])


def table_test(*a):
    """### the provenance test, run and counted by its case pattern (data/b630_table_test.txt)."""
    _run_test('tools/test_terminal_table_b630.py', 'b630_table_test')


def probe_test(*a):
    """### the probe-hold test, run and counted by its case pattern (data/b630_probe_test.txt)."""
    _run_test(K.PROBE_TEST, 'b630_probe_test')


def _run_test(rel, bank):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b630 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel))
    print(L[-1])


def nodes_new(*a):
    """### the ζ node list at v0.24 with the helpers: b629's list (every record and backmatter line unchanged), the four helper
    ### declarations of NymanBeurling.lean appended after the face's nodes, each with its reason (data/b630_nodes_zeta.txt)."""
    src = rd(K.NODES['zeta']).rstrip(NL).split(NL)
    if '# pin: v0.24' not in src:
        sys.exit('### b629`S LIST CARRIES NO `# pin: v0.24` LINE -- NOTHING WRITTEN')
    head = ['# b630 -- THE ζ NODE LIST AT v0.24 WITH THE HELPERS, (R240)(4) and the author`s answer before b630`s seal: b629`s list',
            '# (relay data/b629_nodes_zeta.txt, every record and backmatter line unchanged); the four helper declarations of',
            '# NymanBeurling.lean appended after the face`s nodes -- three defs, objects, and one theorem. Every cell is elaborated by',
            '# the generator`s probe at the pin, never typed here.', '#']
    recs = [l for l in src if l and not l.startswith('#')]
    last = max(i for i, l in enumerate(src) if l and not l.startswith('#'))
    adds = ['%s | kernel | added: (R240)(4), helper, %s: %s' % (n, k, w) for n, k, w in K.HELPERS]
    put_txt(K.NEW_NODES_ZETA, head + src[:last + 1] + adds + src[last + 1:])
    print('  records carried %d ; appended %d' % (len(recs), len(adds)))


# ================================================================================ COMPONENT 3: THE PROBE HOLD
def probe_profile(*a):
    """### ONE profiled probe run of the ζ list with the helpers, in the foreground: the generator's own reading of free memory and
    ### its refusal beneath the hold; the probe's child processes sampled every 2 s for their working set; Python's own allocations
    ### by tracemalloc, the largest ten printed; the probe's output banked as data/b630_probe_out.txt for the page (data/b630_probe_profile.txt)."""
    import threading
    import tracemalloc
    import chain_page as CP
    samples, stop = [], threading.Event()

    def sampler():
        while not stop.is_set():
            out = subprocess.run(['tasklist', '/FO', 'CSV', '/NH'], capture_output=True, text=True).stdout
            row = {}
            for l in out.split(NL):
                f = [x.strip('"') for x in l.strip().split('","')]
                if len(f) >= 5 and f[0].lower() in ('lean.exe', 'lake.exe'):
                    row[f[0] + ':' + f[1]] = int(f[4].replace(' K', '').replace(',', '').replace('.', '').strip() or 0) // 1024
            samples.append((time.time(), R2.free_mb(), row))
            stop.wait(2)

    fm = R2.free_mb()
    pd = os.path.join(SP, '_b630_probe')
    th = threading.Thread(target=sampler, daemon=True)
    tracemalloc.start()
    t0 = time.time()
    th.start()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NEW_NODES_ZETA), pd, None)
    stop.set()
    th.join()
    secs = int(time.time() - t0)
    cur, peak_py = tracemalloc.get_traced_memory()
    top = tracemalloc.take_snapshot().statistics('lineno')[:10]
    tracemalloc.stop()
    po = os.path.join(pd, 'chain_page_probe_out.txt')
    if os.path.exists(po) and not DRY and rc == 0:
        _write(os.path.join(D, K.NEW_PROBE_ZETA), open(po, 'rb').read().replace(b'\r\n', b'\n'))
    peak_child = max([sum(s[2].values()) for s in samples] or [0])
    peak_one = max([max(s[2].values()) for s in samples if s[2]] or [0])
    low = min([s[1] for s in samples] or [fm])
    L = ['b630 -- COMPONENT 3, (R240)(5): ONE PROFILED PROBE RUN OF THE ζ LIST WITH THE HELPERS (%s); exit %d ; %d s' % (utc(), rc, secs), '',
         '### free memory before the call %d MB (the hold %d) ; the lowest sample during it %d MB ; samples %d, every 2 s' % (fm, K.HOLD_MB, low, len(samples)),
         '### the probe`s child processes (lean, lake): peak working set summed %d MB ; the largest single process %d MB' % (peak_child, peak_one),
         '### Python`s own allocations (tracemalloc): peak %.1f MB, current at the end %.1f MB ; the ten largest by line:' % (peak_py / 2 ** 20, cur / 2 ** 20)]
    L += ['    %8.1f KB  %s' % (s.size / 1024, str(s.traceback)[:160]) for s in top]
    L += ['', '### the samples (seconds from start | free MB | child working sets MB):']
    L += ['    %5.0f | %5d | %s' % (t - t0, f, ' '.join('%s=%d' % kv for kv in sorted(r.items()))) for t, f, r in samples]
    L += ['', '### the generator`s log: %s' % (' / '.join(log)[:600] if log else 'empty'),
          '### ### **PEAK OF THE PROBE`S CHILDREN %d MB ; PYTHON`S OWN PEAK %.1f MB ; THE LOWEST FREE READING %d MB AGAINST THE HOLD %d.**' % (
              peak_child, peak_py / 2 ** 20, low, K.HOLD_MB)]
    put_txt('b630_probe_profile.txt', L)
    put_json('b630_probe_profile.json', dict(at=utc(), rc=rc, seconds=secs, free_before=fm, low=low, peak_child=peak_child, peak_one=peak_one,
                                             peak_py_mb=peak_py / 2 ** 20, log=log))
    print(L[-1])
    if rc:
        sys.exit('### THE PROBE EXITED %d' % rc)


# ================================================================================ COMPONENT 4: THE BENCH INPUTS
def _arxiv_entries(t):
    out = []
    for e in re.findall(r'<entry>(.*?)</entry>', t or '', re.S):
        def f(tag):
            m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), e, re.S)
            return ' '.join(m.group(1).split()) if m else None
        out.append(dict(id=f('id'), title=f('title'), published=f('published'), journal_ref=f('arxiv:journal_ref'),
                        authors=[' '.join(x.split()) for x in re.findall(r'<name>(.*?)</name>', e, re.S)],
                        summary=(f('summary') or '')[:600]))
    return out


def nb_inputs(*a):
    """### before any computation: the two registry records read by the seat once each (scratchpad b630_cite_<key>.txt, the exact
    ### command lines in b630_cite_commands.txt), printed beside the ferry's recollection; liCoeff_one_keiper's statement read at v0.20
    ### and 2λ₁ computed in balls with the identity check; the precision, the method and the N_max rule (data/b630_nb_inputs.txt)."""
    from flint import arb, ctx
    ctx.prec = K.PREC
    L = ['b630 -- COMPONENT 4, (R240)(6): THE BENCH INPUTS, BANKED BEFORE ANY COMPUTATION (%s)' % utc(), '']
    cmds = io.open(os.path.join(SP, 'b630_cite_commands.txt'), encoding='utf-8').read() if os.path.exists(os.path.join(SP, 'b630_cite_commands.txt')) else ''
    L += ['### the registry reads, each once, by these command lines (no header, no identifier):'] + ['    ' + c for c in cmds.strip().split(NL) if c.strip()]
    reads_ = {}
    for key, url in K.REGISTRY_READS:
        p = os.path.join(SP, 'b630_cite_%s.txt' % key)
        t = io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
        ents = _arxiv_entries(t)
        reads_[key] = dict(url=url, bytes=len(t.encode('utf-8')), entries=ents)
        L += ['', '### %s -- read once: %s (%d bytes, %d entries)' % (key, url, reads_[key]['bytes'], len(ents)),
              '    the recollection (the ferry`s, printed beside, not copied): %s' % K.RECOLLECTION[key]]
        L += ['    the record: %s | %s | published %s | journal_ref %s | %s' % (x['id'], x['title'], x['published'], x['journal_ref'],
                                                                             ', '.join(x['authors'])) for x in ents] or ['    the record: NONE RETURNED']
    src = _show(K.KER, K.LICOEFF['tag'], K.LICOEFF['file']) or ''
    m = re.search(r'theorem %s :\s*\n?\s*(.*?) := by' % K.LICOEFF['name'], src, re.S)
    stmt = ' '.join(m.group(1).split()) if m else None
    line = next((i + 1 for i, l in enumerate(src.split(NL)) if l.startswith('theorem %s' % K.LICOEFF['name'])), None)
    gam, lg = arb.const_euler(), (4 * arb.pi()).log()
    lam1 = 1 + gam / 2 - lg / 2
    two, chk = 2 * lam1, 2 + gam - lg
    L += ['', '### the kernel`s λ₁: %s at %s (%s), %s :%s -- %s' % (K.LICOEFF['name'], K.LICOEFF['tag'],
                                                                  g(K.KER, 'rev-parse', '--short=7', K.LICOEFF['tag'] + '^{commit}').strip(),
                                                                  K.LICOEFF['file'], line, stmt),
          '### the statement equals the expected form %s' % (stmt == K.LICOEFF['want']),
          '### 2λ₁ = 2(1 + γ/2 − ½ log 4π) = %s ; 2 + γ − log 4π = %s ; the difference %s, containing 0 %s' % (
              two.str(30), chk.str(30), (two - chk).str(5), (two - chk).contains(0)),
          '', '### the precision: %d bits, every quantity a ball at it' % K.PREC,
          '### the integration: closed form per piece (tools/b630_nb_bench.py), each piece`s trigamma part checked against acb.integral in '
          'the tool`s fixtures; the minimisation: arb_mat.solve on the Gram matrix of rho(1/n), n = 2 … N (rho(1/1) is zero)',
          '### the N_max rule: the largest N <= %d whose ball for d_N² has radius at most 10^-%d of its midpoint' % (K.N_CAP, K.REL_DIGITS),
          '### the object: the kernel`s d_N, the distance in L²(0, 1) from 1 to the span of rho(1/n), n <= N -- the constrained form, its '
          'span the sums Σ a_k {1/(kx)} with Σ a_k/k = 0; the literature`s d_N of the recollection is the distance in L²(0, ∞), no '
          'constraint, so the kernel`s d_N² is at least it at each N (a reading of the two definitions, printed, not a result of this act)',
          '### H64c read over 2 <= N <= N_max: at N = 1 log N = 0 and the product is 0; N = 1 is printed']
    put_txt('b630_nb_inputs.txt', L)
    put_json('b630_nb_inputs.json', dict(at=utc(), reads=reads_, commands=cmds, licoeff_statement=stmt, licoeff_line=line,
                                         statement_ok=stmt == K.LICOEFF['want'], two_lambda1=two.str(30), check=chk.str(30),
                                         identity=(two - chk).contains(0), prec=K.PREC, n_cap=K.N_CAP))
    print(L[-6][:200])


# ================================================================================ COMPONENT 5: THE BENCH
def nb_bench(*a):
    """### the bench run twice, each one call of tools/b630_nb_bench.py in the foreground: the first written to data/b630_nb_bench.txt,
    ### the second to the scratchpad; compared byte for byte; the result parsed (data/b630_nb_bench.json)."""
    if not os.path.exists(_r('b630_nb_inputs.txt')):
        sys.exit('### THE INPUTS ARE NOT BANKED -- NOT STARTED')
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    tool = os.path.join(ROOT, 'tools', 'b630_nb_bench.py')
    o1, o2 = _w('b630_nb_bench.txt'), os.path.join(SP, 'b630_nb_bench_run2.txt')
    runs = []
    for o in (o1, o2):
        t0 = time.time()
        r = subprocess.run([sys.executable, tool, 'run', o], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
        runs.append(dict(rc=r.returncode, secs=int(time.time() - t0), err=(r.stderr or '')[-300:]))
    b1, b2 = open(o1, 'rb').read(), open(o2, 'rb').read()
    t = b1.decode('utf-8')
    rows = []
    for l in t.split(NL):
        f = [x.strip() for x in l.split(' | ')]
        if len(f) == 8 and f[0].isdigit():
            rows.append(dict(N=int(f[0]), d2=f[1], rad=f[2], prod=f[3], prod_rad=f[4], above=f[5] == 'yes', cond=float(f[6]), six=f[7] == 'yes'))
    nmax = int(re.search(r'^# N_max .*: (\d+)$', t, re.M).group(1))
    mono = re.search(r'^# the steps N -> N\+1 .*: (.*)$', t, re.M).group(1)
    above = re.search(r'^# N >= 2 with N <= N_max .*: (.*)$', t, re.M).group(1)
    two = re.search(r'^# 2λ₁ = .*? = (\S+)', t, re.M).group(1)
    put_json('b630_nb_bench.json', dict(at=utc(), runs=runs, same=b1 == b2, sha256=sha(b1), bytes=len(b1), n_max=nmax, n_cap=K.N_CAP,
                                        mono_fail=mono, above_fail=above, two_lambda1=two, rows=rows))
    print('  runs %s ; byte for byte %s ; N_max %d ; uncertified steps %s ; not above 2λ₁ %s' % (
        [(x['rc'], x['secs']) for x in runs], b1 == b2, nmax, mono, above))


def _grade_cells(text):
    out = {}
    for l in (text or '').split(NL):
        m = re.match(r'^\| `([^`]+)` \| [^|]+ \| ([A-Z][A-Z-]*) \|', l)
        if m:
            out['corr:' + m.group(1)] = m.group(2)
        m2 = re.match(r'^\d+\. `([^`]+)` — .* — E0: ([A-Z][A-Z-]*) — tier: (.*?) — axioms: ', l)
        if m2:
            out['node:' + m2.group(1)] = m2.group(2)
            out['tier:' + m2.group(1)] = m2.group(3)
    return out


def _page_write(k, pg, fm, secs, rc):
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = _grade_cells(prev.decode('utf-8')), _grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n) and n in ga and n in gb and not n.startswith('tier:'))
    tmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n) and n in ga and n in gb and n.startswith('tier:'))
    put_json('b630_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, tier_cells_moved=tmoved, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s ; tier cells moved %s' % (
        k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE', tmoved or 'NONE'))
    for x in dl[:24]:
        print('    ' + x[:240])


def page_new(*a):
    """### ONE call in the foreground: the ζ page at v0.24 from the new list by a fresh probe (the checkout at v0.24, free memory
    ### above the hold); the probe's output banked as data/b630_probe_out.txt; the page written where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    pd = os.path.join(SP, '_b630_probe')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NEW_NODES_ZETA), pd, None)
    secs = int(time.time() - t0)
    po = os.path.join(pd, 'chain_page_probe_out.txt')
    if os.path.exists(po) and not DRY:
        _write(os.path.join(D, K.NEW_PROBE_ZETA), open(po, 'rb').read().replace(b'\r\n', b'\n'))
    if rc:
        put_json('b630_page_zeta.json', dict(rc=rc, log=log, at=utc(), seconds=secs))
        sys.exit('### ζ RE-EMIT AT v0.24 FAILED, exit %d: %s' % (rc, log))
    _page_write('zeta', pg, fm, secs, rc)


def zlist():
    if os.path.exists(_r(K.NEW_NODES_ZETA)) and os.path.exists(_r(K.NEW_PROBE_ZETA)):
        return K.NEW_NODES_ZETA, K.NEW_PROBE_ZETA
    return K.NODES['zeta'], K.PROBE['zeta']


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked list and probe."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = zlist() if k == 'zeta' else (K.NODES[k], K.PROBE[k])
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b630_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b630_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    _page_write(k, pg, fm, secs, rc)


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b630 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        nl, pr = zlist() if k == 'zeta' else (K.NODES[k], K.PROBE[k])
        r = GCP.arm(os.path.join(D, nl), os.path.join(SP, '_b630_gcp'), os.path.join(D, pr))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', nl, r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
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
    put_txt('b630_page_arms.txt', L)
    for l in L:
        print(l[:240])


def _table_grades():
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    tg = {}
    for r in T['rows']:
        tg.setdefault(r['name'], r['grade'])
    return tg


def table(*a):
    before = _table_grades()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    tg = _table_grades()
    ch = [(x[1] if isinstance(x, list) else x) for x in diff.get('changed') or []]
    gmoved = sorted(n for n in set(before) | set(tg) if before.get(n) != tg.get(n))
    tag = a[0] if a and a[0] != 'dry' else 'table'
    L = ['b630 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(ch)),
         '### the rows changed, with the grade each now reads:']
    L += ['  %-62s %s' % (n, tg.get(n)) for n in ch] or ['  NONE']
    L += ['### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
          '### ### **THE GRADE COLUMN`S DIFF, THE TABLE BEFORE THIS RUN AGAINST AFTER IT : %s.**' % ('; '.join('%s %s -> %s' % (
              n.split('.')[-1], before.get(n), tg.get(n)) for n in gmoved) or 'EMPTY')]
    name = 'b630_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 changed=ch, grade_moved=gmoved, files_moved=moved))
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b630_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b630_') and os.path.isfile(os.path.join(D, f))
                  and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b630'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import act_root as AR
    res = AR.verify()
    J = jl('b630_act_root.json')
    bank = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank))
    shutil.copy(os.path.join(ROOT, *bank.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank, AR.sha256_file(cp)) if it.split()[0] == bank else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    L = ['b630 -- COMPONENT 6: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s) ; '
              'the copy`s root differs %s' % (bank, r2, same, J['root'], r2 != J['root']),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b630_root_arm.txt', L)
    put_json('b630_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H64a', 'H64b', 'H64c', 'H64d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK


def _relay_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(RELAY, 'log', '--reverse', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def _alone(repo, files, commits):
    return [h for h, s in commits if _files(h, repo) == sorted(files)]


def sorry_tokens(rev='main'):
    n = 0
    for f in g(K.KER, 'ls-tree', '-r', '--name-only', rev).split(NL):
        if f.endswith('.lean'):
            t = _show(K.KER, rev, f) or ''
            t = re.sub(r'/-.*?-/', '', t, flags=re.S)
            t = re.sub(r'--[^\n]*', '', t)
            n += len(re.findall(r'\bsorry\b', t))
    return n


ALLOWED_TOOLS = {'tools/terminal_table.py', 'tools/chain_page.py', 'tools/test_terminal_table_b630.py', K.PROBE_TEST}


def n5(trail_line=None, ot=None, *a):
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
    face = jl('b630_kernels_face.json')['kernels']
    now = kern_state(list(face))
    kern_ok = all(now[k] == list(v) for k, v in face.items())
    st = sorry_tokens('main')
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    want_pp = sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + [K.PNAME[k] for k in ('zeta', 'chi') if g(PP, 'diff', '--name-only', PRE_PP, 'HEAD', '--', K.PNAME[k]).strip()]))
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not os.path.basename(x).startswith(('b630_', 'audit_b630_', 'terminal_table'))
              and x not in ALLOWED_TOOLS | {'data/b629_closing_push_out.txt', 'data/act_roots.txt'}]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    cmds = (jx('b630_nb_inputs.json').get('commands') or '')
    ident = bool(re.search(r'@|mailto|User-Agent|-A |-H ', cmds)) or not cmds.strip()
    ok = kern_ok and st == 0 and pp_ch == want_pp and not beyond and rec_ok and not tracked_local and untracked_local and not ident
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel unmoved against the face`s snapshot %s; sorry tokens on the explicit-formula main %d (comments '
            'stripped); PLACE-papers %s; %s; relay beyond the list: %s; b628`s local intake bank in any relay commit %s, untracked now %s; the '
            'registry command lines carry an address, a header or nothing %s' % (kern_ok, st, pp_ch, rec_state, beyond or 'NONE', tracked_local,
                                                                                 untracked_local, ident))


def _rows_by(T, names):
    return {r['name']: r for r in T['rows'] if r['name'] in names}


def scores(*a):
    B, I_, PZ, PX = jx('b630_nb_bench.json'), jx('b630_nb_inputs.json'), jx('b630_page_zeta.json'), jx('b630_page_chi.json')
    TF, TT_, PT, RA = jx('b630_table_final.json'), jx('b630_table_test.json'), jx('b630_probe_test.json'), jx('b630_root_arm.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    T = json.load(io.open(_r('terminal_table.json'), encoding='utf-8'))
    rr = _rows_by(T, set(K.RULE_ROWS))
    rule_ok = len(rr) == 13 and all(r.get('provenance') == 'rule' and r['grade'] not in ('UNGRADED', None) for r in rr.values())
    helpers = {n: (rr.get(n) or {}).get('grade') for n, _k, _w in K.HELPERS}
    moved_other = [n for n in (TF.get('grade_moved') or []) if n not in K.RULE_ROWS]
    nmax = B.get('n_max', 0)
    S = {
        'H64a': (('HOLDS' if B and B.get('mono_fail') == 'NONE' else 'REFUTED'), 'steps N -> N+1 whose decrease is not certified, N < N_max %d: %s' % (nmax, B.get('mono_fail'))),
        'H64b': (('HOLDS' if nmax >= 20 else 'REFUTED'), 'N_max %d (the cap %s)' % (nmax, B.get('n_cap'))),
        'H64c': (('HOLDS' if B and B.get('above_fail') == 'NONE' else 'REFUTED'), 'N in 2 … N_max whose d_N² · log N is not certified above 2λ₁ = %s: %s' % (
            B.get('two_lambda1'), B.get('above_fail'))),
        'H64d': (('HOLDS' if B.get('same') is True and all(x['rc'] == 0 for x in B.get('runs') or [{'rc': 1}]) else 'REFUTED'),
                 'two runs %s, byte for byte %s, sha256 %s' % ([(x['rc'], x['secs']) for x in B.get('runs') or []], B.get('same'), (B.get('sha256') or '')[:16])),
        'N1': (('HELD' if B and B.get('mono_fail') == 'NONE' else 'REFUTED'), 'as H64a'),
        'N2': (('HELD' if nmax >= 20 else 'REFUTED'), 'N_max %d' % nmax),
        'N3': (('HELD' if B and B.get('above_fail') == 'NONE' else 'REFUTED'), 'as H64c, read over 2 <= N <= N_max (at N = 1 the product is 0)'),
        'N4': (('HELD' if rule_ok and not moved_other and all(v == 'DEF' for v in helpers.values()) else 'REFUTED'),
               'the thirteen rows from the rule %s; other rows whose grade moved %s; the helpers read %s (rhoFun_bound a theorem, DERIVES by the '
               'author`s answer, so the letter four DEF is refuted where it reads so)' % (rule_ok, moved_other or 'NONE', helpers)),
        'N5': n5v,
        'S1': (('HELD' if TT_.get('cases') and TT_.get('cases') == TT_.get('passing') and rule_ok and not moved_other else 'REFUTED'),
               'the provenance test %s of %s; the thirteen from the rule %s; other grades moved %s' % (TT_.get('passing'), TT_.get('cases'), rule_ok, moved_other or 'NONE')),
        'S2': (('HELD' if PT.get('cases') and PT.get('cases') == PT.get('passing') else 'REFUTED'), 'the probe-hold test %s of %s' % (PT.get('passing'), PT.get('cases'))),
        'S3': (('HELD' if I_.get('reads') and all(v.get('bytes', 0) > 0 and v.get('entries') for v in I_['reads'].values()) else 'REFUTED'),
               'each registry record read once, entries: %s' % {k: len(v.get('entries') or []) for k, v in (I_.get('reads') or {}).items()}),
        'S4': (('HELD' if not (PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or []) else 'REFUTED'),
               'grade cells moved on the pages %s ; tier cells moved %s' % ((PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or []) or 'NONE',
                                                                         (PZ.get('tier_cells_moved') or []) + (PX.get('tier_cells_moved') or []) or 'NONE')),
        'S5': (('HELD' if RA.get('verify') and all(v[1] == 'AGREE' for v in RA['verify']) and [v[0] for v in RA['verify']] == ['b624', 'b625', 'b626', 'b627', 'b628', 'b629', 'b630'] else 'REFUTED'),
               'the chain %s' % [(v[0], v[1]) for v in RA.get('verify') or []]),
    }
    put_json('b630_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 7: THE RECORD
TRAIL_HEAD = ('### b630 — lane three, act fifty-seven under (R240): the Nyman–Beurling distances d_N² in Arb balls beside 2λ₁; new rows '
              'graded from the rule with provenance; helper rows as objects; the probe hold')


def _title_entry():
    B = jx('b630_nb_bench.json')
    return ('## The Nyman–Beurling distances d_N² for N ≤ %s in Arb balls, d_N² · log N beside 2λ₁ = %s; 13 rows graded from the rule with '
            'provenance, 3 helper defs as objects and 1 helper theorem; the probe hold' % (B.get('n_max', '?'), (B.get('two_lambda1') or '?')[:12]))


def _finding_text():
    S, rl, B, I_ = (jl(n) for n in ('b630_scores.json', 'b630_record_lines.json', 'b630_nb_bench.json', 'b630_nb_inputs.json'))
    J, RA, PR, RR = jl('b630_act_root.json'), jl('b630_root_arm.json'), jx('b630_probe_profile.json'), jx('b630_table_rule_readings.json')
    rows = {r['N']: r for r in B['rows']}
    nmax = B['n_max']
    show = [n for n in (2, 5, 10, 20, 50, nmax) if n in rows and n <= nmax]
    tbl = '; '.join('N = %d: d_N² = %s (± %s), d_N² · log N = %s' % (n, rows[n]['d2'][:12], rows[n]['rad'], rows[n]['prod'][:10]) for n in sorted(set(show)))
    t = _title_entry()
    e = ['', t, '',
         '*Filed at b630 on the author’s ruling `(R240)` and the author’s two answers before the seal. Banks: relay `data/b630_nb_inputs.txt`, '
         '`data/b630_nb_bench.txt`, `data/b630_table_rule_readings.txt`, `data/b630_table_final.txt`, `data/b630_table_test.txt`, '
         '`data/b630_probe_test.txt`, `data/b630_probe_profile.txt`, `data/b630_act_root.txt`, `data/b630_author_answers.txt`. Nothing deposits.*', '',
         '**The bench** (`(R240)`(6), a T3/T4 bench with no claim): the kernel’s d_N (SIDE-explicit-formula v0.24, NymanBeurling.lean :94), '
         'the distance in L²(0, 1) from 1 to the span of rho(1/n), n ≤ N, computed for N = 1 … %d at %d bits: each inner product in closed '
         'form per piece, the trigamma parts checked against Arb’s own integrator, the minimisation a linear solve in balls. N_max, the '
         'largest N whose ball keeps six certified digits, is %d. %s. Beside them 2λ₁ = %s from the kernel’s liCoeff_one_keiper at v0.20 '
         '(the identity 2λ₁ = 2 + γ − log 4π checked in balls, %s). The recollection, read from the registry and printed beside, not copied: '
         'the rate d_N² ~ C/log N with C = 2 + γ − log 4π is a conjecture of Báez-Duarte, Balazard, Landreau and Saias, and Burnol’s lower '
         'bound is a lim inf; the kernel’s d_N is the constrained (0, 1) form, at least the literature’s (0, ∞) form at each N. The bench '
         'is the finite distances of a fourth face, computed, set beside a constant the kernel holds at another face; nothing is inferred '
         'about N beyond N_max. H64a %s, H64b %s, H64c %s, H64d %s.' % (
             B['n_cap'], K.PREC, nmax, tbl, B['two_lambda1'][:20], I_.get('identity'), S['H64a'][0], S['H64b'][0], S['H64c'][0], S['H64d'][0]), '',
         '**The table** (`(R240)`(3)–(4), by the author’s answers): the thirteen rows of v0.24 graded from the shared E0 rule with the '
         'provenance mark rule, every row graded by cells marked cell, no existing grade moved; the three helper defs at DEF with the object '
         'shape —, the helper theorem rhoFun_bound graded by the rule. Nine-tenths of the terminal table has no grade from any ledger: %s of '
         '%s rows, %s of them readable by the rule, banked and not applied, the input of W-ORD-TABLE-RULE-GRADES (OPEN_TRAILS :%d).' % (
             RR.get('ungraded'), RR.get('rows'), RR.get('readable'), rl['lines'][5]['line']), '',
         '**The probe hold** (`(R240)`(5)): the generator’s probe reads free memory before it starts and refuses beneath %d MB, printing the '
         'reading; one profiled run: its children’s peak %s MB, Python’s own peak %.1f MB, the lowest free reading %s MB.' % (
             K.HOLD_MB, PR.get('peak_child'), PR.get('peak_py_mb') or 0, PR.get('low')), '',
         '**The record lines and the root.** b629’s weight at FINDINGS :%d; the outbound-identifier line beneath :11864 (OPEN_TRAILS :%d); '
         'the provenance clause (:%d); the helper clause (:%d); the Nyman item (:%d). The root of b630 over %d repositories, %d tags and %d '
         'banks; the chain verified, %s.' % (rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                                            rl['lines'][4]['line'], len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks']),
                                            ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b629’s face, whose d_N it computes, and b601–b602’s Keiper face, '
         'whose λ₁ it sets beside them; and b625’s 33 rows where a rule reading met a cell, whose form the provenance column now carries. '
         'It strengthens the programme’s offering of one located clause read through many faces, each number set beside the others with '
         'its own ball and its own grade.', '',
         '**Next.** Per `(R240)`(7): b631, W-ORD-DEDEKIND-INSTANCE (OPEN_TRAILS :12895). The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH holds, that NB does, or that the conjectured rate holds at any N.*', '']
    return t, NL.join(e)


FOR_AUTHOR = ('(1) the table’s rule applied to rows absent from the table at relay 75227e9c, so the thirteen rows of v0.24 and every later new '
              'row; (2) H64c and N3 read over 2 ≤ N ≤ N_max, the product 0 at N = 1 printed; (3) six certified digits read as a radius at most '
              '10^-6 of the midpoint; (4) the kernel’s d_N computed as defined at v0.24, the constrained (0, 1) form, its relation to the '
              'literature’s form printed as a reading of the two definitions; (5) the bench’s cap N ≤ 100 named before the run; (6) the profiled '
              'probe run’s output used for the ζ page, so one probe serves both')


def _next_lines():
    t = _show(PP, 'HEAD', 'OPEN_TRAILS.md') or ''
    l = lines_of(t)
    src = l[K.DEDEKIND_LINE - 1] if len(l) >= K.DEDEKIND_LINE else ''
    m = re.search(r'the two named premises of \(R213\)\(3\)\(d\) \((.*?)\)', src)
    return ['no kernel terminal yet for the Dedekind instance; the two premises of (R213)(3)(d), from OPEN_TRAILS :%d: %s' % (
        K.DEDEKIND_LINE, m.group(1) if m else '### NOT READ')]


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b630_scores.json', 'b630_findings.json', 'b630_record_lines.json', 'b630_act_root.json'))
    rc = _relay_commits()
    n_ans = len(re.findall(r'^### PROMPT ', rd('b630_author_answers.txt'), re.M))
    tbl = (_alone(RELAY, ['tools/terminal_table.py', 'tools/test_terminal_table_b630.py'], rc) or ['?'])[0]
    prb = (_alone(RELAY, ['tools/chain_page.py', K.PROBE_TEST], rc) or ['?'])[0]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R240) ratified.** (1) b629 at its weight. (2) The seat’s two mistakes, a standing line on outbound identifiers. (3) Table rows '
             'graded from the rule with provenance. (4) Helper declarations as rows and objects. (5) The probe hold. (6) The Nyman–Beurling '
             'bench. (7) The act after: b631.', '',
             '**Entered:** FINDINGS.md:%d (b629’s weight), :%d (the entry); OPEN_TRAILS.md:%d (no outbound identifier, beneath :11864), :%d '
             '(the provenance clause), :%d (the helper clause), :%d (the Nyman item, to :12893), :%d (W-ORD-TABLE-RULE-GRADES); this record; '
             'relay tools/terminal_table.py with its test %s; tools/chain_page.py with its test %s.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                 rl['lines'][4]['line'], rl['lines'][5]['line'], tbl, prb), '',
             '**Act root:** b630 `%s` (previous `%s`, b629’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**Prompts to the author:** %d (relay data/b630_author_answers.txt)%s.' % (
                 n_ans, (': ' + ' / '.join(_elide(answer_of(i))[:400] for i in range(n_ans))) if n_ans else ''), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b630_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R240)`(7), b631, W-ORD-DEDEKIND-INSTANCE (OPEN_TRAILS :12895); the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


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
    put_json('b630_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
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
    put_json('b630_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b630_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b630 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b630_defects.json -- NOTHING WRITTEN')
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
    put_json('b630_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


def desk(*a):
    S = jl('b630_scores.json')
    L = ['=' * 104, 'b630 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H64a-H64d, (R240)(6).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H64 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b630_defects.txt').rstrip(NL).split(NL)
    put_txt('b630_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b630_scores.json', 'b630_findings.json', 'b630_trail.json', 'b630_record_lines.json', 'b630_act_root.json'))
    B = jx('b630_nb_bench.json')
    L = ['b630 -- THE COMPONENTS, BANKED UNDER (R240).', '',
         '### COMPONENT 0 : the process listing ; b629`s closing push-out relay %s ; push-b629* branches deleted by name (data/b630_branches.txt) ; '
         'every test file under tools/ run (data/b630_tests_stepzero.txt) ; the suite, its four arms repaired, run at HEAD before the face '
         '(data/b630_arms_prerun.txt) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b629`s weight FINDINGS :%d ; no outbound identifier OPEN_TRAILS :%d ; provenance :%d ; helpers :%d ; the Nyman item '
         ':%d ; W-ORD-TABLE-RULE-GRADES :%d' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : data/b630_table_rule_readings.txt ; data/b630_table_test.txt ; data/b630_table_final.txt ; data/b630_nodes_zeta.txt',
         '### COMPONENT 3 : data/b630_probe_test.txt ; data/b630_probe_profile.txt',
         '### COMPONENT 4 : data/b630_nb_inputs.txt',
         '### COMPONENT 5 : data/b630_nb_bench.txt ; N_max %s ; H64a %s, H64b %s, H64c %s, H64d %s' % (B.get('n_max'), S['H64a'][0], S['H64b'][0],
                                                                                                S['H64c'][0], S['H64d'][0]),
         '### COMPONENT 6 : the pages (data/b630_page_zeta.json, data/b630_page_chi.json) ; page arms data/b630_page_arms.txt ; the root %s ; '
         'the arm data/b630_root_arm.txt' % J['root'][:16],
         '### COMPONENT 7 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b631 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b630_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b630_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
