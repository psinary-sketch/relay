# -*- coding: utf-8 -*-
"""b629_record.py -- THE ACT'S RECORD TOOL, UNDER (R239). ### ONE SUBCOMMAND PER BANK.

### ### b629: LANE THREE, ACT FIFTY-SIX -- THE NYMAN–BEURLING CRITERION AS A COMPILED FACE AT v0.24; THE INTAKE FORM ENTERED; THE
### b592 TEST REPAIRED.
### Subcommands write only `data/b629_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`. The data is tools/b629_worklist.py. The registry records of the citation are read by the seat once each, by
### curl, into the scratchpad; this tool reads the captures and never calls a platform. The case counter is (R233)(3)'s standing form.
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
import b629_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
SESSION_ID = 'f5c41941-fa74-40e9-b806-a98e7280e315'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b629_registration_2026-10-05.txt'

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
_DJ = os.path.join(D, 'b629_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b629 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b629_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the face`s work-order, the serial build and its standing line, b628`s correction, the synthesis form and its '
         'clauses, the edition form, the precedence and authority orders, the build clause, the N5 line', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12228, 12354, 12356, 12566, 12601, 12699, 12799, 12893, 13065, 13067, 13069, 13091], 1500),
        ('FINDINGS: b628`s entry', PP, PRE_PP, 'FINDINGS.md', [7611, 7613], 600),
        ('SIDE-explicit-formula v0.23: the house form of a named premise with a citation (PlattRung.lean)', K.KER, 'v0.23',
         'SIDEExplicitFormula/PlattRung.lean', [1, 2, 3, 10, 22, 23, 49, 50, 51, 52, 54, 55, 56], 300),
        ('SIDE-explicit-formula v0.23: the audit module of the last face (AxiomCheckPlattRung.lean)', K.KER, 'v0.23', 'AxiomCheckPlattRung.lean', ('ALL',), 300),
        ('SIDE-explicit-formula v0.23: the library root`s imports', K.KER, 'v0.23', 'SIDEExplicitFormula.lean', ('GREP', r'PlattRung|Simplicity'), 300),
        ('SIDE-explicit-formula v0.23: the toolchain', K.KER, 'v0.23', 'lean-toolchain', ('ALL',), 200),
        ('relay tools/chain_page.py: the shape reader', RELAY, PRE_RELAY, 'tools/chain_page.py', ('GREP', r'^SHAPES =|^def (shape_of|_measure_bounded|_domain)\('), 300),
        ('relay tools/test_chain_page_b592.py: its pins and its regeneration', RELAY, PRE_RELAY, K.TEST_FILE,
         ('GREP', r'^PRE_RELAY|^import chain_page|def regen|def _gen|C\.build\(|\(1\) the|\(2\) every|\(3\) the'), 300),
        ('relay data/b628_intake_crank_v0_5.txt: its header lines alone (the local bank, untracked)', RELAY, None, K.LOCAL_BANK, [1, 2, 3], 200),
        ('relay data/b628_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b628_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b629 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    put_txt('b629_reads.txt', L)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R239) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
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
    L = ['### b629 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b629_author_answers.txt', L)


def answer_of(k):
    """### the author's answer to the act's k-th prompt (0-based, across calls), whole: cut from the result after its own question's
    ### `"<question>"="` and before the next question's `", "<question>"="`, the questions read from the bank's prompt headers."""
    t = rd('b629_author_answers.txt')
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
WRITTEN_KERNS = ('SIDE-explicit-formula',)   # ### the one this act writes: the face, on its branch and tag


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
    put_json('b629_kernels_face.json', dict(at=utc(), kernels=kern_state()))


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
    p = os.path.join(SP if DRY else D, 'b629_scanfile_%s.md' % name)
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
B628_ENTRY = 7613
W_HEAD = '*Appended 2026-10-05 by b629 to b628’s entry (:%d), under `(R239)`(1) -- b628 AT ITS WEIGHT:*'
IF_HEAD = '*Appended 2026-10-05 by b629 beneath the synthesis form`s clauses (:12699), under `(R239)`(2) -- THE INTAKE FORM, A CLAUSE:*'
CP_HEAD = '*Appended 2026-10-05 by b629 to W-ORD-ZETA23-SERIAL-BUILD (:13065), under `(R239)`(1) -- THE CLONE AND THE CACHE, KEPT:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry):
    pre, post = _count_bank(_rel('b628_checks.txt')), _count_bank(_rel('b628_checks_postpush.txt'))
    DJ = json.loads(_rel('b628_defects.json'))
    roots = [l.split() for l in _rel('act_roots.txt').split(NL) if l.startswith('b628 ')]
    return ('\n%s route (b): thmB₀_mult’s profile from Zeta23’s AUDIT.md :80 at 3635e748 in its recorded run (toolchain v4.33.0-rc2, '
            'Mathlib 51e6992e), ThmB_statement from the clone’s own build of Zeta23.Statement (986 s), both at the standard three, banked '
            'with source marks and the bank’s sha256; the parallel closure build stopped by PID at 717 MB free against the 2560 hold with '
            'no module finished, the serial build priced as W-ORD-ZETA23-SERIAL-BUILD (OPEN_TRAILS :13065), the standing line at :13067; '
            'SIDE-explicit-formula v0.23 = 98b7668, the docstring on two_thirds naming AUDIT.md :80, the pin, the toolchain and the digest, '
            'no code line changed, the audit module’s 19 prints equal line for line with v0.22, the grade where it was. The intake pilot on '
            'the ANNEX paper (A_WOUND_UP_ENOUGH_CRANK_v0_5.md, the census’s latest version on D: being v0.4): 28 claims, 3 kernel-verified '
            'at their pins, 7 routes all dark, 15 statement-grade, the full bank local and untracked, the summary with its digest '
            'committed. The b596 test’s case (1) at its pin and case (3) with it, 11 of 11. H62a-H62f held, H62a on the artefact’s line; '
            'N1-N3 and N5 held; N4 refuted, fifteen of 28 statement-grade against the navigator’s third, written before the paper was '
            'read -- the form working, the navigator’s figure the error; S2 refuted in letter, the correction at :13091. Relay 75227e9c; '
            'PLACE-papers f610d1f. The root %s, b624-b628 verifying. The suite %d of %d before the push and %d of %d after it by the '
            'seat’s predicates, each claim tested directly and holding; defects (a)-(g) the seat’s (relay data/b628_defects.txt, %d '
            'entries). Nothing deposited; no statement line changed.\n'
            % (W_HEAD % entry, (roots[0][1][:8] + '…' + roots[0][1][-4:]) if roots else '?', pre[0], pre[1], post[0], post[1], len(DJ['defects'])))


def _intake_form():
    return ('\n%s one document in; its claims extracted from its own text with line citations into a claim bank; each claim graded in '
            'the taxonomy’s vocabulary (:12566), the terminal and pin named where kernel-verified; each routed through the sieve’s five '
            'tests with test and verdict; each assigned a cluster by the census’s rows; every claim below kernel-verified yielding a '
            'priced work-order line or the reason none is possible; the no-disclosure arm over the bank. A document REGISTRY files as '
            'not for publication keeps its full bank local and untracked, relay carrying the summary and the digest alone; a published '
            'document’s full bank may be committed. The pilot’s figures stand as the form’s example (b628, relay '
            'data/b628_intake_summary.txt: 28 claims, 3 kernel-verified, 7 routes, 15 statement-grade).\n' % IF_HEAD)


def _clone_paths():
    return ('\n%s the clone of Zeta23 at 3635e748 (D:/zeta23-b628, its .lake holding Zeta23.Statement built) and the Mathlib cache '
            'for 51e6992e (D:/mathlib-cache-b628) are kept on D:, outside every repository, for this work-order; the serial build starts '
            'from them.\n' % CP_HEAD)


def record_lines(*a):
    """### FINDINGS: b628's weight (to its entry :7613). OPEN_TRAILS: the intake form's clause (beneath :12699), the clone and cache
    ### paths (to :13065). No line makes a table cell (predicted)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## thmB₀_mult’s axiom profile in Zeta23’s build at 3635e748')
    if entry != B628_ENTRY:
        sys.exit('### b628`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % entry, _weight(entry)), ('OPEN_TRAILS.md', IF_HEAD, _intake_form()),
             ('OPEN_TRAILS.md', CP_HEAD, _clone_paths())]
    cells, nd, clean = _guarded(items, 'OPEN_TRAILS.md', 'lines')
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    _land(Q, items, 'b629_record_lines.json', entry)


# ================================================================================ COMPONENT 1: THE TEST REPAIR
CONTROL_FMT = '### THE POSITIVE CONTROL: the same test with %s as it stood at relay %s (exit %d): cases %d, passing %d, failing %s'
CONTROL_RE = r'^### THE POSITIVE CONTROL: the same test with tools/test_chain_page_b592\.py as it stood at relay (\w+) \(exit (\d+)\): cases (\d+), passing (\d+), failing (.*)$'


def test_repair(*a):
    """### (R239)(3): the b592 test as repaired run and counted by its case pattern, the repaired cases named; its diff against
    ### PRE_RELAY; the control: the test as it stood (its blob at PRE_RELAY) failing the repaired cases (data/b629_test_repair.txt, .json)."""
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    test = os.path.join(ROOT, *K.TEST_FILE.split('/'))
    r = subprocess.run([sys.executable, test], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    old = os.path.join(SP, '_b629_test_old.py')                       # ### the blob at PRE_RELAY, in the scratchpad, run as if in tools/
    _write(old, _show(RELAY, PRE_RELAY, K.TEST_FILE).encode('utf-8'))
    runner = ('import sys; src = open(%r, encoding="utf-8").read(); g = {"__name__": "__main__", "__file__": %r}; '
              'exec(compile(src, "test@%s", "exec"), g)' % (old, test, PRE_RELAY))
    r2 = subprocess.run([sys.executable, '-c', runner], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    out2 = (r2.stdout or '') + (r2.stderr or '')
    n2, p2 = count_cases(out2)
    failed2 = [re.match(r'^  (\(\d+\))', l).group(1) for l in out2.split(NL) if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]
    cases = [l.strip() for l in out.split(NL) if any(l.startswith('  ' + c + ' ') for c in K.TEST_CASES)]
    d = g(RELAY, 'diff', PRE_RELAY, '--', K.TEST_FILE)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', K.TEST_FILE).rstrip(NL).split(NL)[-1].strip()
    L = ['b629 -- COMPONENT 1, (R239)(3): %s REPAIRED, RUN AND COUNTED (%s); exit %d' % (K.TEST_FILE, utc(), r.returncode), '',
         '### ' + (st or 'NO DIFF'), ''] + d.rstrip(NL).split(NL) + ['', '### THE RUN:'] + out.rstrip(NL).split(NL)
    L += ['', '### THE REPAIRED CASES:'] + ['    ' + c for c in cases] + [
          '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p), '',
          CONTROL_FMT % (K.TEST_FILE, PRE_RELAY, r2.returncode, n2, p2, failed2)]
    put_txt('b629_test_repair.txt', L)
    put_json('b629_test_repair.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, repaired=cases, stat=st,
                                           control=dict(rc=r2.returncode, cases=n2, passing=p2, failing=failed2)))
    print(L[-3])
    print(L[-1])


# ================================================================================ CARRIED FROM b628, NOT CALLED BY b629 (Zeta23, citation, intake)
def zeta23_artefact(*a):
    """### the repository at the pin read for an axiom artefact or a build cache for FinalMult: every tracked file whose name says
    ### audit, axiom or print, the audit record's lines on the multiplicity statements, the comparator's delegation, and whether a
    ### build tree for FinalMult exists beside the clone; one ls-remote of the upstream (data/b629_zeta23_artefact.txt and .json)."""
    files = [x for x in g(K.FM, 'ls-tree', '-r', '--name-only', K.ZETA23_PIN).split(NL) if re.search(r'(?i)audit|axiom|print', x)]
    audit = lines_of(_show(K.FM, K.ZETA23_PIN, 'AUDIT.md') or '')
    deleg = lines_of(_show(K.FM, K.ZETA23_PIN, 'comparator/Solution/Multiplicity.lean') or '')
    named = [i + 1 for i, l in enumerate(audit) if 'thmB₀_mult' in l or 'ThmB_statement' in l]
    multi = [(i + 1, l) for i, l in enumerate(audit) if 'two_thirds_simple_on_critical_line' in l]
    olean = [p for p in (os.path.join(K.FM, '.lake', 'build', 'lib', 'lean', 'Zeta23', 'FinalMult.olean'),
                         os.path.join(K.ZETA23_CLONE, '.lake', 'build', 'lib', 'lean', 'Zeta23', 'FinalMult.olean')) if os.path.exists(p)]
    rem = g(K.FM, 'ls-remote', 'origin', 'refs/tags/v1.0^{}', 'refs/tags/v1.0')
    peel = [l.split('\t')[0] for l in rem.split(NL) if l.endswith('^{}')]
    L = ['b629 -- COMPONENT 2, (R239)(4): THE UPSTREAM READ AT ITS PIN FOR AN AXIOM ARTEFACT OR A BUILD CACHE FOR FinalMult (%s)' % utc(), '',
         '### the upstream: %s (clone %s) ; one ls-remote: tag v1.0 peels at the remote to %s ; the pin %s ; equal %s' % (
             g(K.FM, 'remote', 'get-url', 'origin').strip(), K.FM, peel[0] if peel else 'NOT READ', K.ZETA23_PIN_FULL,
             bool(peel) and peel[0] == K.ZETA23_PIN_FULL),
         '### tracked files at the pin whose name says audit, axiom or print: %s' % files,
         '### AUDIT.md at the pin: a record of the upstream`s own runs (its toolchain line :%s); its #print axioms lines name the comparator '
         'statements; lines naming thmB₀_mult or ThmB_statement: %s' % (
             next((i + 1 for i, l in enumerate(audit) if l.startswith('Toolchain')), '?'), named or 'NONE')]
    L += ['    AUDIT.md :%d %s' % (i, l[:160]) for i, l in multi]
    L += ['### the comparator`s delegation (comparator/Solution/Multiplicity.lean): ' + ' / '.join(
        ':%d %s' % (i + 1, l.strip()) for i, l in enumerate(deleg) if 'thmB₀_mult' in l)[:600]]
    L += ['### a build tree holding Zeta23/FinalMult.olean beside the clone or at the clone`s pin directory: %s' % (olean or 'NONE'), '',
          '### ### **THE FINDING: an artefact exists at the pin -- AUDIT.md, the upstream`s record, printing the comparator statement that '
          'delegates to thmB₀_mult at the standard three -- and it prints no line on thmB₀_mult or ThmB_statement by name; no build cache '
          'for FinalMult exists. The ruling`s print by name is not carried by the artefact: the module is built in a clone at the pin.**']
    put_txt('b629_zeta23_artefact.txt', L)
    put_json('b629_zeta23_artefact.json', dict(at=utc(), files=files, named=named, multi=[x[0] for x in multi], olean=olean,
                                               peel=peel[0] if peel else None, pin=K.ZETA23_PIN_FULL))
    print(L[-1])


def _logs(prefix):
    return sorted((f for f in os.listdir(SP) if re.match(r'%s_\d+\.log$' % prefix, f)), key=lambda f: int(re.findall(r'_(\d+)\.log$', f)[0]))


def build_bank(prefix, name, *a):
    """### the detached build calls' watchdog logs (scratchpad <prefix>_<n>.log), banked: data/<name>.txt and .json."""
    calls = []
    L = ['b629 -- THE DETACHED BUILD CALLS AT THE HOLD, %s (%s), one target per call, watched from the foreground' % (prefix, utc()), '']
    for f in _logs(prefix):
        t = io.open(os.path.join(SP, f), encoding='utf-8', errors='replace').read()
        st = re.search(r'^### START (\S+) free (\d+) MB pid (\d+) cmd (.*?) cwd', t, re.M)
        ex = re.search(r'^### EXIT (-?\d+) (\S+) (\d+) s peak (-?\d+)', t, re.M)
        errs = [l for l in t.split(NL) if re.search(r'\berror\b', l, re.I) and not l.startswith('###')]
        built = len(re.findall(r'^.?\s*(?:✔|Built|\[\d+/\d+\] Built)', t, re.M))
        calls.append(dict(log=f, start=st.group(1) if st else None, free=int(st.group(2)) if st else None, cmd=st.group(4) if st else None,
                          rc=int(ex.group(1)) if ex else None, secs=int(ex.group(3)) if ex else None, peak=int(ex.group(4)) if ex else None,
                          errors=errs[:5], built=built))
        L.append('### %s : %s ; started %s, free %s MB ; exit %s after %s s, peak %s MB ; built lines %d ; errors %d' % (
            f, calls[-1]['cmd'], calls[-1]['start'], calls[-1]['free'], calls[-1]['rc'], calls[-1]['secs'], calls[-1]['peak'], built, len(errs)))
        L += ['    ' + e[:200] for e in errs[:5]]
    L += ['', '### ### **CALLS %d ; ELAPSED %d s IN ALL.**' % (len(calls), sum(c['secs'] or 0 for c in calls))]
    put_txt(name + '.txt', L)
    put_json(name + '.json', dict(at=utc(), calls=calls))
    print(L[-1])


STD = {'propext', 'Classical.choice', 'Quot.sound'}


def _parse_prints(t):
    return [dict(name=m.group(1), axioms=[x.strip() for x in (m.group(2) or '').split(',') if x.strip()])
            for m in re.finditer(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", t)]


def zeta23_axioms(log, *a):
    """### the #print axioms of thmB₀_mult and ThmB_statement from the print call's log in the clone at the pin, banked with the peeled
    ### SHA, the toolchain and Mathlib; the bank's own sha256 in data/b629_zeta23_axioms.json (a file cannot carry its own digest)."""
    t = io.open(log, encoding='utf-8', errors='replace').read()
    pr = _parse_prints(t)
    head = g(K.ZETA23_CLONE, 'rev-parse', 'HEAD').strip()
    tc = (io.open(os.path.join(K.ZETA23_CLONE, 'lean-toolchain'), encoding='utf-8').read().strip() if os.path.exists(os.path.join(K.ZETA23_CLONE, 'lean-toolchain')) else '?')
    AJ = jx('b629_zeta23_artefact.json')
    L = ['b629 -- COMPONENT 2, (R239)(4): #print axioms ON thmB₀_mult AND ThmB_statement IN ZETA23`S OWN BUILD', '',
         '### the clone %s at HEAD %s ; the pin %s (tag v1.0 peeled at the remote %s) ; equal %s' % (
             K.ZETA23_CLONE, head, K.ZETA23_PIN_FULL, AJ.get('peel'), head == K.ZETA23_PIN_FULL == AJ.get('peel')),
         '### the toolchain %s ; Mathlib %s (lakefile.toml at the pin)' % (tc, K.ZETA23_MATHLIB),
         '### the print file: import Zeta23.FinalMult and Zeta23.Statement, then #print axioms on each name; run by lake env lean in the clone', '']
    L += ['  %s' % l.strip() for l in t.split(NL) if "depends on axioms" in l or "does not depend" in l]
    want = ['Zeta23.thmB₀_mult', 'Zeta23.ThmB_statement']
    got = {x['name']: x['axioms'] for x in pr}
    beyond = [n for n in want if n in got and set(got[n]) - STD]
    L += ['', '### ### **PRINTS %d ; NAMED %s ; BEYOND THE STANDARD THREE %s ; sorryAx %s.**' % (
        len(pr), [n for n in want if n in got], beyond or 'NONE', 'PRESENT' if 'sorryAx' in t else 'ABSENT')]
    b = put_txt('b629_zeta23_axioms.txt', L)
    put_json('b629_zeta23_axioms.json', dict(at=utc(), head=head, pin=K.ZETA23_PIN_FULL, toolchain=tc, mathlib=K.ZETA23_MATHLIB, prints=pr,
                                             beyond=beyond, sorry='sorryAx' in t, missing=[n for n in want if n not in got],
                                             bank_sha256=hashlib.sha256(b).hexdigest()))
    print(L[-1])
    print('  the bank`s sha256: %s' % hashlib.sha256(b).hexdigest())


# ================================================================================ COMPONENT 3: THE CITATION
def cite_diff(*a):
    """### the docstring on the citation branch against v0.22: the diff, every changed line, and the statement lines -- every line of
    ### the file outside a comment or docstring -- equal before and after (data/b629_cite_diff.txt and .json)."""
    def code(t):
        t = re.sub(r'/-.*?-/', '', t, flags=re.S)
        return [l.rstrip() for l in re.sub(r'--[^\n]*', '', t).split(NL) if l.strip()]
    old = _show(K.KER, 'v0.22', K.CITE_FILE) or ''
    new = _show(K.KER, K.CITE_BRANCH, K.CITE_FILE) or ''
    d = g(K.KER, 'diff', 'v0.22', K.CITE_BRANCH, '--', K.CITE_FILE)
    files = sorted(x for x in g(K.KER, 'diff', '--name-only', 'v0.22', K.CITE_BRANCH).split(NL) if x.strip())
    same = code(old) == code(new)
    L = ['b629 -- COMPONENT 3: THE DOCSTRING AT two_thirds, %s AGAINST v0.22 (%s)' % (K.CITE_BRANCH, utc()), '',
         '### files changed: %s ; the statement lines (comments and docstrings stripped) equal before and after: %s ; the words "%s" '
         'present: %s' % (files, same, K.CITE_WORDS, K.CITE_WORDS in new), ''] + d.rstrip(NL).split(NL)
    put_txt('b629_cite_diff.txt', L)
    put_json('b629_cite_diff.json', dict(at=utc(), files=files, statements_equal=same, words=K.CITE_WORDS in new,
                                         axioms_sha=jx('b629_zeta23_axioms.json').get('bank_sha256'),
                                         sha_in_docstring=(jx('b629_zeta23_axioms.json').get('bank_sha256') or '#') in new))
    print(L[2])


def prints(log_old, log_new, *a):
    """### the audit module's prints at v0.22 and at the citation branch, compared line by line (data/b629_prints.txt and .json)."""
    def pl(p):
        t = io.open(p, encoding='utf-8', errors='replace').read()
        return [l.strip() for l in t.split(NL) if 'depends on axioms' in l or 'does not depend' in l], 'sorryAx' in t
    a_, sa = pl(log_old)
    b_, sb = pl(log_new)
    L = ['b629 -- COMPONENT 3: THE AUDIT MODULE`S PRINTS, v0.22 AGAINST v0.23, LINE BY LINE (%s)' % utc(), '']
    for i in range(max(len(a_), len(b_))):
        x, y = (a_[i] if i < len(a_) else '### NONE'), (b_[i] if i < len(b_) else '### NONE')
        L.append('  %s %s' % ('SAME' if x == y else '### DIFFERS', x if x == y else '%s  ||  %s' % (x, y)))
    L += ['', '### ### **LINES v0.22 %d ; v0.23 %d ; EQUAL LINE FOR LINE %s ; sorryAx %s / %s.**' % (len(a_), len(b_), a_ == b_ and bool(a_), sa, sb)]
    put_txt('b629_prints.txt', L)
    put_json('b629_prints.json', dict(at=utc(), old=a_, new=b_, equal=a_ == b_ and bool(a_), sorry=[sa, sb]))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE INTAKE
CLAIM_RE = r'^CLAIM (C\d\d) ¦ :(\d+) ¦ grade=([^¦]+?) ¦ terminal=([^¦]+?) ¦ pin=([^¦]+?) ¦ route=(yes|no) ¦ test=([^¦]+?) ¦ verdict=([^¦]+?) ¦ cluster=([^¦]+?) ¦ wo=([^¦]*?) ¦ reason=(.*)$'


def _claims(t):
    return [dict(id=m.group(1), line=int(m.group(2)), grade=m.group(3).strip(), terminal=m.group(4).strip(), pin=m.group(5).strip(),
                 route=m.group(6), test=m.group(7).strip(), verdict=m.group(8).strip(), cluster=m.group(9).strip(), wo=m.group(10).strip(),
                 reason=m.group(11).strip()) for m in re.finditer(CLAIM_RE, t, re.M)]


def _sixgrams(text):
    w = re.findall(r"[A-Za-z0-9’']+", text.lower())
    return set(' '.join(w[i:i + 6]) for i in range(len(w) - 5))


def intake(*a):
    """### the full bank (data/b629_intake_crank_v0_5.txt, the seat's, untracked) read and checked: each claim one grade of the form's
    ### vocabulary, one cluster of the census's rows, a kernel-verified grade only with a terminal and a pin that resolve, a route read
    ### through the five tests, every claim below kernel-verified carrying a work-order line or a reason; the no-disclosure arm over
    ### the whole bank; the summary written with no six-word run of the paper in it (data/b629_intake_summary.txt and .json)."""
    p = _r(K.INTAKE_LOCAL)
    raw = open(p, 'rb').read()
    t = raw.decode('utf-8').replace(chr(13), '')
    doc = io.open(K.INTAKE_DOC, encoding='utf-8').read().replace(chr(13), '')
    dl = lines_of(doc)
    C = _claims(t)
    nclaim = len(re.findall(r'^CLAIM ', t, re.M))
    bad = []
    for c in C:
        why = []
        if c['grade'] not in K.GRADES:
            why.append('grade')
        if c['cluster'] not in K.CLUSTERS:
            why.append('cluster')
        if not (0 < c['line'] <= len(dl)) or not dl[c['line'] - 1].strip():
            why.append('line')
        if c['grade'] == 'kernel-verified':
            parts = c['pin'].split('@')
            ok = len(parts) == 2 and c['terminal'] != '-'
            if ok:
                repo, rev = parts
                f = c['terminal'].split('#')[-1] if '#' in c['terminal'] else ''
                src = _show('D:/' + repo, rev, f) if f else None
                ok = bool(src) and re.search(r'^(theorem|def|structure|lemma) %s\b' % re.escape(c['terminal'].split('#')[0].split('.')[-1]), src, re.M) is not None
            if not ok:
                why.append('terminal/pin')
        if c['route'] == 'yes' and c['verdict'] not in K.VERDICTS[:2]:
            why.append('route verdict')
        if c['route'] == 'no' and c['verdict'] != 'NOT A ROUTE':
            why.append('non-route verdict')
        if c['grade'] != 'kernel-verified' and not (c['wo'] or c['reason'] not in ('', '-')):
            why.append('work-order or reason')
        if why:
            bad.append((c['id'], why))
    nd, nn = _nd(t)
    grades = {gname: sum(c['grade'] == gname for c in C) for gname in K.GRADES}
    clusters = {}
    for c in C:
        clusters[c['cluster']] = clusters.get(c['cluster'], 0) + 1
    wos = [(c['id'], c['wo']) for c in C if c['wo']]
    S = ['b629 -- COMPONENT 4, (R239)(5): THE INTAKE PILOT`S SUMMARY BANK (%s). ### NO SENTENCE OF THE PAPER IS IN THIS BANK.' % utc(), '',
         '### the document: the ANNEX`s paper the census at its latest version on D: names (THE_KEYSTONE_CENSUS_v0_4.md row R22; REGISTRY '
         ':366), %s, %d lines, sha256 %s; REGISTRY files it non-keystone and not for publication, so its claims stay in the full bank, '
         'which is local, untracked and never pushed (the author`s answer before the seal)' % (
             os.path.basename(K.INTAKE_DOC), len(dl), hashlib.sha256(doc.encode('utf-8')).hexdigest()),
         '### the full bank: data/%s, %d bytes, sha256 %s' % (K.INTAKE_LOCAL, len(raw), hashlib.sha256(raw).hexdigest()),
         '### the form: the synthesis form`s grades (OPEN_TRAILS :12566), the sieve`s five tests (THE_FINDINGS_AS_THEY_STAND_v0_6.md), the '
         'census`s rows as clusters, kernel-verified only where a terminal at a pin carries the claim', '',
         '### CLAIMS %d (lines read as claims %d) ; malformed %s' % (len(C), nclaim, bad or 'NONE'),
         '### GRADES: ' + ' ; '.join('%s %d' % (k, v) for k, v in grades.items()),
         '### CLUSTERS: ' + ' ; '.join('%s %d' % (k, v) for k, v in sorted(clusters.items())),
         '### ROUTES: %d read through the five tests -- ' % sum(c['route'] == 'yes' for c in C) + ' ; '.join(
             '%s %s%s' % (c['id'], c['verdict'], (' at test %s' % c['test']) if c['verdict'] == 'DARK' else '') for c in C if c['route'] == 'yes'),
         '### KERNEL-VERIFIED: ' + (' ; '.join('%s on %s at %s' % (c['id'], c['terminal'].split('#')[0], c['pin']) for c in C if c['grade'] == 'kernel-verified') or 'NONE'),
         '### THE NO-DISCLOSURE ARM OVER THE FULL BANK: %s (needle sets %s)' % (nd, nn), '', '### THE CLAIM ROWS, WITHOUT THE PAPER`S TEXT:']
    S += ['  %s :%d | %s | %s | %s | test %s %s | %s' % (c['id'], c['line'], c['grade'], c['terminal'].split('#')[0] if c['terminal'] != '-' else '-',
                                                        c['pin'], c['test'], c['verdict'], c['cluster']) for c in C]
    S += ['', '### THE WORK-ORDER LINES, THE SEAT`S WORDS:'] + ['  %s: %s' % x for x in wos]
    S += ['', '### THE REASONS NONE IS POSSIBLE:'] + ['  %s: %s' % (c['id'], c['reason']) for c in C if c['reason'] not in ('', '-')]
    leak = _sixgrams(NL.join(S)) & _sixgrams(doc)
    S += ['', '### ### **THE SUMMARY CARRIES NO SIX-WORD RUN OF THE PAPER: %s.**' % ('TRUE' if not leak else 'FALSE %s' % sorted(leak)[:3])]
    if leak:
        sys.exit('### THE SUMMARY WOULD CARRY THE PAPER`S WORDS -- NOTHING WRITTEN: %s' % sorted(leak)[:5])
    put_txt(K.INTAKE_SUMMARY, S)
    put_json(K.INTAKE_SUMMARY.replace('.txt', '.json'), dict(at=utc(), claims=len(C), claim_lines=nclaim, malformed=bad, grades=grades, clusters=clusters,
                                                             kv=[c['id'] for c in C if c['grade'] == 'kernel-verified'],
                                                             statement=[c['id'] for c in C if c['grade'] == 'statement-grade'],
                                                             workorders=len(wos), nd=nd, local_sha256=hashlib.sha256(raw).hexdigest(),
                                                             local_bytes=len(raw), rows=C and [dict((k, v) for k, v in c.items()) for c in C]))
    print(S[6])
    print(S[7])
    print(S[-1])


# ================================================================================ COMPONENT 2: THE API READ
def nb_api(*a):
    """### Mathlib at the kernel's pin: every declaration the face reads, printed with file and line by git at the pin; the obligations
    ### the definitions will need listed before any module is written (data/b629_nb_api.txt and .json)."""
    pin = g(K.MATHLIB, 'rev-parse', 'HEAD').strip()
    kpin = g(K.KER, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b629 -- COMPONENT 2, (R239)(4): THE API READ, MATHLIB AT THE KERNEL`S PIN (%s)' % utc(), '',
         '### the kernel SIDE-explicit-formula at %s (toolchain %s) ; its Mathlib checkout %s at %s, read by git grep' % (
             kpin, (_show(K.KER, 'HEAD', 'lean-toolchain') or '').strip(), K.MATHLIB, pin), '']
    found = []
    for path, rx in K.API:
        t = _show(K.MATHLIB, 'HEAD', path)
        hits = [(i + 1, l) for i, l in enumerate(lines_of(t or '')) if re.search(rx, l)]
        found.append(dict(path=path, rx=rx, hits=[h[0] for h in hits]))
        L.append('### %s (%s)' % (path, 'NOT AT THE PIN' if t is None else '%d line(s)' % len(hits)))
        L += ['    :%-5d %s' % (n, l.strip()[:170]) for n, l in hits]
    obl = [('rhoFun_measurable', 'Measurable (rhoFun θ): fract is measurable (Floor.lean, measurable_fract), division by x and the '
            'product by θ measurable -- expected discharged'),
           ('rhoFun_memLp', 'MemLp (rhoFun θ) 2 μ on the unit interval: |rhoFun θ x| ≤ 1 + |θ| from fract_nonneg and fract_lt_one, the '
            'measure finite on (0, 1) (volume_Ioo, isFiniteMeasure_restrict), MemLp.of_bound -- expected discharged')]
    L += ['', '### THE OBLIGATIONS THE DEFINITIONS NEED, LISTED BEFORE ANY MODULE IS WRITTEN:'] + ['    %s: %s' % o for o in obl]
    missing = [f['path'] for f in found if not f['hits']]
    L += ['', '### ### **DECLARATIONS READ %d ; FILES WITHOUT A HIT %s ; OBLIGATIONS LISTED %d.**' % (
        sum(len(f['hits']) for f in found), missing or 'NONE', len(obl))]
    put_txt('b629_nb_api.txt', L)
    put_json('b629_nb_api.json', dict(at=utc(), mathlib=pin, kernel=kpin, found=found, obligations=[o[0] for o in obl], missing=missing))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE FACE
def citation(*a):
    """### the registry records of the three works, read once each by the seat into the scratchpad (b629_cite_<key>.txt), printed
    ### beside the ferry's recollection: each record's title, venue, year and identifier as the record gives them, or its absence
    ### (data/b629_citation.txt and .json)."""
    out = {}
    L = ['b629 -- COMPONENT 3: THE CITATION`S REGISTRY RECORDS, EACH READ ONCE, BESIDE THE FERRY`S RECOLLECTION (%s)' % utc(), '']
    for key, url in K.REGISTRY_READS:
        p = os.path.join(SP, 'b629_cite_%s.txt' % key)
        t = io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
        rec = {}
        if 'crossref' in url:
            try:
                j = json.loads(t)
                m = j.get('message') or {}
                items = m.get('items') if 'items' in m else [m]
                rec = [dict(title=(x.get('title') or [''])[0], venue=(x.get('container-title') or [''])[0],
                            year=((x.get('issued') or {}).get('date-parts') or [[None]])[0][0], doi=x.get('DOI'),
                            volume=x.get('volume'), page=x.get('page'), author=', '.join(a_.get('family', '') for a_ in x.get('author') or []))
                       for x in (items or [])][:3]
            except Exception as e:
                rec = [dict(error='%s' % type(e).__name__)]
        else:
            ti = re.findall(r'<title>(.*?)</title>', t, re.S)
            pub = re.findall(r'<published>(.*?)</published>', t)
            jr = re.findall(r'<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>', t, re.S)
            au = re.findall(r'<name>(.*?)</name>', t)
            rec = [dict(title=' '.join(ti[1].split()) if len(ti) > 1 else None, published=pub[0] if pub else None,
                        journal_ref=' '.join(jr[0].split()) if jr else None, author=', '.join(au))]
        out[key] = dict(url=url, bytes=len(t.encode('utf-8')), records=rec, recollection=K.RECOLLECTION[key])
        L.append('### %s -- read once: %s (%d bytes)' % (key, url, out[key]['bytes']))
        L.append('    the recollection: %s' % K.RECOLLECTION[key])
        L += ['    the record: %s' % json.dumps(r_, ensure_ascii=False) for r_ in rec] or ['    the record: NONE']
    put_txt('b629_citation.txt', L)
    put_json('b629_citation.json', dict(at=utc(), reads=out))
    for l in L[2:]:
        print(l[:220])


def face_prints(log, *a):
    """### the AxiomCheck module's output at the branch, parsed: every #print axioms line; beyond the standard three, sorryAx; the face's
    ### nodes each printed (data/b629_prints.txt and .json)."""
    t = io.open(log, encoding='utf-8', errors='replace').read()
    pr = _parse_prints(t)
    bad = [x['name'] for x in pr if set(x['axioms']) - STD]
    names = [x['name'] for x in pr]
    missing = [n for n in K.FACE_NODES if n not in names]
    L = ['b629 -- COMPONENT 3: THE AXIOM PRINTS OF %s AT %s (%s)' % (K.AXCHECK_FILE, K.FACE_BRANCH, utc()), '']
    L += ['  %-62s %s' % (x['name'], x['axioms'] or 'no axioms') for x in pr]
    L += ['', '### ### **PRINTS %d ; BEYOND THE STANDARD THREE %s ; FACE NODES NOT PRINTED %s ; sorryAx %s.**' % (
        len(pr), bad or 'NONE', missing or 'NONE', 'PRESENT' if 'sorryAx' in t else 'ABSENT')]
    put_txt('b629_prints.txt', L)
    put_json('b629_prints.json', dict(at=utc(), prints=pr, beyond=bad, missing=missing, sorry='sorryAx' in t))
    print(L[-1])


def _face_src(rev):
    return _show(K.KER, rev, K.FACE_FILE) or ''


def face_grades(*a):
    """### the face's terminals graded by the shared E0 rule from their source headers at the tag; the obligations read: each a
    ### theorem (discharged) or a structure field (named); the face's files against v0.23 (data/b629_face.txt and .json)."""
    import e0_rule as E
    src = _face_src(K.FACE_TAG) or _face_src(K.FACE_BRANCH)
    out = {}
    for n in K.FACE_NODES:
        short = n.split('.')[-1]
        m = re.search(r'^(theorem|def|structure|abbrev) %s\b(.*?)(:=|where)' % re.escape(short), src, re.M | re.S)
        kind = m.group(1) if m else None
        head = ' '.join(m.group(2).split()) if m else ''
        gr = E.grade(head, 'theorem') if kind == 'theorem' else (None, '', [])
        out[short] = dict(kind=kind, grade=gr[0], why=gr[1], binders=[b for b, _t in gr[2]] if gr and gr[2] else [])
    obl = {o: ('discharged' if out.get(o, {}).get('kind') == 'theorem' else
               'named' if re.search(r'^\s+%s\s*:' % o, src, re.M) else 'ABSENT') for o in K.OBLIGATIONS}
    files = sorted(x for x in g(K.KER, 'diff', '--name-only', K.PRE_KER, K.FACE_TAG if _face_src(K.FACE_TAG) else K.FACE_BRANCH).split(NL) if x.strip())
    sorry = len(re.findall(r'\bsorry\b', re.sub(r'--[^\n]*', '', re.sub(r'/-.*?-/', '', src, flags=re.S))))
    L = ['b629 -- COMPONENT 3: THE FACE`S NODES GRADED BY THE SHARED E0 RULE, ITS OBLIGATIONS READ (%s)' % utc(), '']
    L += ['  %-28s %-9s %-16s %s' % (k, v['kind'], v['grade'], v['why'][:120]) for k, v in out.items()]
    L += ['', '### the obligations: %s' % obl, '### the kernel`s files changed against v0.23: %s ; sorry tokens in the module %d' % (files, sorry),
          '', '### ### **rh_iff_nb %s ON %s ; distN_antitone %s ; OBLIGATIONS NAMED %d.**' % (
              out.get('rh_iff_nb', {}).get('grade'), out.get('rh_iff_nb', {}).get('why', '')[:80], out.get('distN_antitone', {}).get('grade'),
              sum(v == 'named' for v in obl.values()))]
    put_txt('b629_face.txt', L)
    put_json('b629_face.json', dict(at=utc(), nodes=out, obligations=obl, files=files, sorry=sorry))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES, THE TABLE, THE ROOT
def nodes_new(*a):
    """### the ζ node list at v0.24: b628's list (every record and backmatter line unchanged), the pin moved to v0.24, the face's
    ### nodes appended, each with its reason (data/b629_nodes_zeta.txt)."""
    src = rd(K.NODES['zeta']).rstrip(NL).split(NL)
    if '# pin: v0.23' not in src:
        sys.exit('### b628`S LIST CARRIES NO `# pin: v0.23` LINE -- NOTHING WRITTEN')
    head = ['# b629 -- THE ζ NODE LIST AT v0.24, (R239)(4): b628`s list (relay data/b628_nodes_zeta.txt, every record and backmatter',
            '# line unchanged), the pin moved to v0.24; the Nyman–Beurling face`s nodes appended. Every cell is elaborated by the',
            '# generator`s probe at the pin, never typed here.', '#']
    body = [('# pin: v0.24' if l == '# pin: v0.23' else l) for l in src]
    why = ('the dilation family ρ_θ', 'its measurability obligation', 'its square-integrability obligation', 'the Nyman–Beurling statement',
           'the Báez-Duarte form', 'the named premise (T1-lit), the equivalence NB ↔ RH', 'the face at INTERFACES on the premise',
           'the finite distances d_N', 'd_N monotone non-increasing')
    recs = [l for l in body if l and not l.startswith('#')]
    last = max(i for i, l in enumerate(body) if l and not l.startswith('#'))
    adds = ['%s | kernel | added: (R239)(4), %s' % (n, w) for n, w in zip(K.FACE_NODES, why)]
    put_txt(K.NEW_NODES_ZETA, head + body[:last + 1] + adds + body[last + 1:])
    print('  records carried %d ; appended %d' % (len(recs), len(adds)))


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
    put_json('b629_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, tier_cells_moved=tmoved, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s ; tier cells moved %s' % (
        k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE', tmoved or 'NONE'))
    for x in dl[:24]:
        print('    ' + x[:240])


def page_new(*a):
    """### ONE call in the foreground: the ζ page at v0.23 from the new list by a fresh probe (the checkout at v0.23, free memory
    ### above the hold); the probe's output banked as data/b629_probe_out.txt; the page written where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    pd = os.path.join(SP, '_b629_probe')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NEW_NODES_ZETA), pd, None)
    secs = int(time.time() - t0)
    po = os.path.join(pd, 'chain_page_probe_out.txt')
    if os.path.exists(po) and not DRY:
        _write(os.path.join(D, K.NEW_PROBE_ZETA), open(po, 'rb').read().replace(b'\r\n', b'\n'))
    if rc:
        put_json('b629_page_zeta.json', dict(rc=rc, log=log, at=utc(), seconds=secs))
        sys.exit('### ζ RE-EMIT AT v0.23 FAILED, exit %d: %s' % (rc, log))
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
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b629_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b629_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    _page_write(k, pg, fm, secs, rc)


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b629 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        nl, pr = zlist() if k == 'zeta' else (K.NODES[k], K.PROBE[k])
        r = GCP.arm(os.path.join(D, nl), os.path.join(SP, '_b629_gcp'), os.path.join(D, pr))
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
    put_txt('b629_page_arms.txt', L)
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
    L = ['b629 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(ch)),
         '### the rows changed, with the grade each now reads:']
    L += ['  %-62s %s' % (n, tg.get(n)) for n in ch] or ['  NONE']
    L += ['### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
          '### ### **THE GRADE COLUMN`S DIFF, THE TABLE BEFORE THIS RUN AGAINST AFTER IT : %s.**' % ('; '.join('%s %s -> %s' % (
              n.split('.')[-1], before.get(n), tg.get(n)) for n in gmoved) or 'EMPTY')]
    name = 'b629_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 changed=ch, grade_moved=gmoved, files_moved=moved))
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b629_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b629_') and os.path.isfile(os.path.join(D, f))
                  and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b629'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import act_root as AR
    res = AR.verify()
    J = jl('b629_act_root.json')
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
    L = ['b629 -- COMPONENT 5: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s) ; '
              'the copy`s root differs %s' % (bank, r2, same, J['root'], r2 != J['root']),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b629_root_arm.txt', L)
    put_json('b629_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H63a', 'H63b', 'H63c', 'H63d')
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


def _statement_lines_changed():
    """### every .lean file that existed at v0.23 and changed in the explicit-formula kernel since, its code lines (comments and
    ### docstrings stripped) before and after: the files whose code differs. A file the act creates is not a changed statement."""
    out = []
    for f in [x for x in g(K.KER, 'diff', '--name-only', '--diff-filter=M', K.PRE_KER, 'main').split(NL) if x.strip().endswith('.lean')]:
        def code(t):
            t = re.sub(r'/-.*?-/', '', t or '', flags=re.S)
            return [l.rstrip() for l in re.sub(r'--[^\n]*', '', t).split(NL) if l.strip()]
        if code(_show(K.KER, K.PRE_KER, f)) != code(_show(K.KER, 'main', f)):
            out.append(f)
    return out


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
    face = jl('b629_kernels_face.json')['kernels']
    now = kern_state(list(face))
    others_ok = all(now[k] == list(v) for k, v in face.items() if k not in WRITTEN_KERNS)
    st = sorry_tokens('main')
    stl = _statement_lines_changed()
    ker_files = sorted(set(x for x in g(K.KER, 'diff', '--name-only', K.PRE_KER, 'main').split(NL) if x.strip()))
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    want_pp = sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + [K.PNAME[k] for k in ('zeta', 'chi') if g(PP, 'diff', '--name-only', PRE_PP, 'HEAD', '--', K.PNAME[k]).strip()]))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith(('b629_', 'audit_b629_', 'terminal_table'))
                              and x != 'data/b628_closing_push_out.txt'))
    beyond = [x for x in relay_beyond if x not in {K.TEST_FILE, 'data/act_roots.txt'}]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ker_ok = sorted(ker_files) == sorted([K.FACE_FILE, K.AXCHECK_FILE])
    ok = others_ok and st == 0 and not stl and ker_ok and pp_ch == want_pp and not beyond and rec_ok and not tracked_local and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; the kernels this act does not write unmoved %s; sorry tokens on the explicit-formula main %d (comments stripped); '
            'existing files whose code lines changed since v0.23 %s; the explicit-formula kernel`s files changed %s; PLACE-papers %s; %s; '
            'relay beyond the list: %s; b628`s local intake bank in any relay commit %s, untracked now %s' % (
                others_ok, st, stl or 'NONE', ker_files or 'NONE', pp_ch, rec_state, beyond or 'NONE', tracked_local, untracked_local))


def scores(*a):
    PR, FG, TR, CI = jx('b629_prints.json'), jx('b629_face.json'), jx('b629_test_repair.json'), jx('b629_citation.json')
    PZ, PX, RA, TF = jx('b629_page_zeta.json'), jx('b629_page_chi.json'), jx('b629_root_arm.json'), jx('b629_table_final.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    nodes, obl = FG.get('nodes') or {}, FG.get('obligations') or {}
    named = [o for o, v in obl.items() if v == 'named']
    rh = nodes.get('rh_iff_nb') or {}
    mono = nodes.get('distN_antitone') or {}
    rh_ok = rh.get('grade', '').startswith('INTERFACES') and K.PREMISE in rh.get('why', '') and len(rh.get('binders') or []) == 1
    mono_ok = (mono.get('grade') or '').startswith('DERIVES')
    std_ok = bool(PR) and not PR.get('beyond') and not PR.get('sorry') and not PR.get('missing')
    moved = (PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or [])
    tmoved = (PZ.get('tier_cells_moved') or []) + (PX.get('tier_cells_moved') or [])
    others = [x for x in moved if not any(x.endswith(n) for n in K.FACE_NODES)]
    ver = RA.get('verify') or []
    tag = g(K.KER, 'rev-parse', '--short=7', K.FACE_TAG + '^{commit}').strip()
    S = {
        'H63a': (('HOLDS' if obl and all(v in ('discharged', 'named') for v in obl.values()) else 'REFUTED'),
                 'the family`s obligations: %s' % (obl or 'NOT READ')),
        'H63b': (('HOLDS' if rh_ok else 'REFUTED'), 'rh_iff_nb reads %s on %s' % (rh.get('grade'), rh.get('why'))),
        'H63c': (('HOLDS' if mono_ok and std_ok else 'REFUTED'), 'distN_antitone reads %s; the prints beyond the standard three %s, sorryAx %s' % (
            mono.get('grade'), PR.get('beyond'), PR.get('sorry'))),
        'H63d': (('HOLDS' if not others and TF.get('grade_moved') == [] else 'REFUTED'), 'grade cells moved on the pages beyond the face`s own %s; '
                 'the table`s grade column %s' % (others or 'NONE', TF.get('grade_moved'))),
        'N1': (('HELD' if std_ok and not [o for o, v in obl.items() if v == 'ABSENT'] else 'REFUTED'),
               'prints beyond the standard three %s ; sorryAx %s ; obligations %s' % (PR.get('beyond'), PR.get('sorry'), obl)),
        'N2': (('HELD' if len(named) <= 2 else 'REFUTED'), 'obligations named rather than discharged: %s' % (named or 'NONE')),
        'N3': (('HELD' if rh_ok and mono_ok else 'REFUTED'), 'rh_iff_nb %s ; distN_antitone %s' % (rh.get('grade'), mono.get('grade'))),
        'N4': (('HELD' if not others else 'REFUTED'), 'other grade cells moved %s' % (others or 'NONE')),
        'N5': n5v,
        'S1': (('HELD' if TR.get('cases') and TR.get('cases') == TR.get('passing') and (TR.get('control') or {}).get('failing') == K.TEST_CASES
                and len(_alone(RELAY, [K.TEST_FILE], _relay_commits())) == 1 else 'REFUTED'),
               'the b592 test %s of %s; the test as it stood fails %s; committed alone %s' % (TR.get('passing'), TR.get('cases'),
                                                                                            (TR.get('control') or {}).get('failing'), _alone(RELAY, [K.TEST_FILE], _relay_commits()))),
        'S2': (('HELD' if not named else 'REFUTED'), 'both obligations discharged from Mathlib: %s' % obl),
        'S3': (('HELD' if CI.get('reads') and all(v.get('bytes', 0) > 0 for v in CI['reads'].values()) else 'REFUTED'),
               'each registry record read once: %s' % {k: v.get('bytes') for k, v in (CI.get('reads') or {}).items()}),
        'S4': (('HELD' if not tmoved or all(any(x.endswith(n) for n in K.FACE_NODES) for x in tmoved) else 'REFUTED'),
               'tier cells moved %s' % (tmoved or 'NONE')),
        'S5': (('HELD' if ver and all(v[1] == 'AGREE' for v in ver) and [v[0] for v in ver] == ['b624', 'b625', 'b626', 'b627', 'b628', 'b629'] else 'REFUTED'),
               'the chain %s ; v0.24 at %s' % ([(v[0], v[1]) for v in ver], tag or 'NONE')),
    }
    put_json('b629_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b629 — lane three, act fifty-six under (R239): the Nyman–Beurling criterion as a compiled face at v0.24; the intake '
              'form entered; the b592 test repaired')


def _title_entry():
    FG = jx('b629_face.json')
    named = sum(v == 'named' for v in (FG.get('obligations') or {}).values())
    return ('## The Nyman–Beurling face at v0.24: the dilation family in L² with %d obligation%s named, NB and BD stated, rh_iff_nb INTERFACES '
            'on one premise, d_N defined and monotone; the intake form entered from its pilot; the b592 test repaired' % (named, '' if named == 1 else 's'))


def _finding_text_carried_b628():
    S, rl, ZA, PR, CD, TR = (jl(n) for n in ('b629_scores.json', 'b629_record_lines.json', 'b629_zeta23_axioms.json', 'b629_prints.json',
                                             'b629_cite_diff.json', 'b629_test_repair.json'))
    IS, J, RA, ZB = jl('b629_intake_summary.json'), jl('b629_act_root.json'), jl('b629_root_arm.json'), jx('b629_zeta23_build.json')
    thm = [p for p in ZA['prints'] if p['name'] == 'Zeta23.thmB₀_mult']
    tag = g(K.KER, 'rev-parse', '--short=7', K.CITE_TAG + '^{commit}').strip()
    t = _title_entry()
    e = ['', t, '',
         '*Filed at b629 on the author’s ruling `(R239)` and the author’s two answers before the seal. Banks: relay `data/b629_zeta23_artefact.txt`, '
         '`data/b629_zeta23_build.txt`, `data/b629_zeta23_axioms.txt`, `data/b629_cite_diff.txt`, `data/b629_prints.txt`, `data/b629_intake_summary.txt`, '
         '`data/b629_test_repair.txt`, `data/b629_tests_stepzero.txt`, `data/b629_table_final.txt`, `data/b629_act_root.txt`, '
         '`data/b629_author_answers.txt`. Nothing deposits.*', '',
         '**Route (b)** (`(R239)`(4), OPEN_TRAILS :12970): the upstream at its pin carries an audit record, AUDIT.md, printing the '
         'comparator statement that delegates to thmB₀_mult at the standard three, and no print of thmB₀_mult or ThmB_statement by '
         'name, and no build cache for FinalMult; so the module was built in a clone at the pin (%s, %d calls detached at the hold, %d s '
         'in all) under %s with Mathlib 51e6992e, and the two names printed there: thmB₀_mult %s, sorryAx %s (relay '
         'data/b629_zeta23_axioms.txt, sha256 %s). SIDE-explicit-formula v0.23 = %s adds a docstring to SimpleProportion’s two_thirds '
         'field naming the theorem, the repository, the pin, the toolchain and that sha256 -- “%s” -- and changes no statement: the code '
         'lines equal before and after, the audit module’s %d prints equal line for line. exceptional_mass_le_third stays INTERFACES on '
         'two_thirds: a theorem in another kernel’s build is a citation here until it compiles here. H62a %s, H62b %s, H62c %s.' % (
             K.ZETA23_CLONE, len(ZB.get('calls') or []), sum(c.get('secs') or 0 for c in ZB.get('calls') or []), ZA['toolchain'],
             thm[0]['axioms'] if thm else 'not printed', 'present' if ZA['sorry'] else 'absent', ZA['bank_sha256'], tag, K.CITE_WORDS,
             len(PR['new']), S['H62a'][0], S['H62b'][0], S['H62c'][0]), '',
         '**The intake pilot** (`(R239)`(5), W-ORD-INTAKE): one document in, by the synthesis form’s rules without an edition -- the '
         'ANNEX’s paper the census names (row R22; REGISTRY :366), filed there non-keystone and not for publication, so the full bank '
         'stays local and untracked and the relay carries its summary and digest (data/b629_intake_summary.txt; the full bank’s sha256 '
         '%s), by the author’s answer before the seal. %d claims, each with one grade of the form’s vocabulary and one cluster of the '
         'census’s rows: %s; kernel-verified %s; %d routes read through the sieve’s five tests; %d work-order lines; the no-disclosure '
         'arm over the full bank %s. H62d %s, H62e %s, H62f %s. The pilot is the form’s test on one document and certifies nothing the '
         'document does not.' % (
             IS['local_sha256'], IS['claims'], '; '.join('%s %d' % (k, v) for k, v in IS['grades'].items() if v),
             ', '.join(IS['kv']) or 'none', sum(1 for r in IS['rows'] if r['route'] == 'yes'), IS['workorders'], IS['nd'],
             S['H62d'][0], S['H62e'][0], S['H62f'][0]), '',
         '**The carried test defect** (`(R239)`(2)): case (1) of tools/test_chain_page_b596.py loads the E0 rule at the test’s own pin; '
         'the test %d of %d by its case pattern, the test as it stood failing %s; committed alone. Every test file under tools/ ran at '
         'step zero (data/b629_tests_stepzero.txt): the standing line entered beneath :12799 (OPEN_TRAILS :%d).' % (
             TR['passing'], TR['cases'], TR['control']['failing'], rl['lines'][1]['line']), '',
         '**The record lines and the root.** b628’s weight at FINDINGS :%d; the word at :12970 (OPEN_TRAILS :%d) and :12893 (:%d). '
         'The root of b629 over %d repositories, %d tags and %d banks; the chain verified, %s.' % (
             rl['lines'][0]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'], len(J['reads']['heads']), len(J['reads']['tags']),
             len(J['reads']['banks']), ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b596’s named premise and b625’s re-pricing, and gives '
         'SimpleProportion’s field the source kernel’s own print beside it, the grade where b596 set it; it re-reads the census’s '
         'ANNEX row (b619) and b611’s striking of the ANNEX act, and runs the synthesis form on the one document the sequence could not '
         'reach, without writing a synthesis. It strengthens the programme’s offering of a ladder whose rungs are carried at their '
         'honest grade, a source kernel’s theorem cited where it holds and never claimed where it does not compile.', '',
         '**Next.** Per `(R239)`(6): b629, W-ORD-NYMAN-BEURLING-FACE (OPEN_TRAILS :12893), the opening act of its two; no kernel terminal is '
         'named for it yet. The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds, or that the 2/3 theorem compiles in this kernel.*', '']
    return t, NL.join(e)


def _finding_text():
    S, rl, PR, FG, TR, CI = (jl(n) for n in ('b629_scores.json', 'b629_record_lines.json', 'b629_prints.json', 'b629_face.json',
                                             'b629_test_repair.json', 'b629_citation.json'))
    J, RA, KB, PZ = jl('b629_act_root.json'), jl('b629_root_arm.json'), jx('b629_build.json'), jx('b629_page_zeta.json')
    tag = g(K.KER, 'rev-parse', '--short=7', K.FACE_TAG + '^{commit}').strip()
    obl = FG['obligations']
    t = _title_entry()
    reads = '; '.join('%s: %s' % (k, '; '.join(json.dumps(r_, ensure_ascii=False)[:160] for r_ in v.get('records') or []) or 'no record')
                      for k, v in CI['reads'].items())
    e = ['', t, '',
         '*Filed at b629 on the author’s ruling `(R239)`. Banks: relay `data/b629_nb_api.txt`, `data/b629_citation.txt`, `data/b629_build.txt`, '
         '`data/b629_prints.txt`, `data/b629_face.txt`, `data/b629_test_repair.txt`, `data/b629_tests_stepzero.txt`, `data/b629_table_final.txt`, '
         '`data/b629_act_root.txt`, `data/b629_root_arm.txt`. Nothing deposits.*', '',
         '**The face** (`(R239)`(4), W-ORD-NYMAN-BEURLING-FACE, OPEN_TRAILS :12893): SIDE-explicit-formula v0.24 = %s adds '
         'SIDEExplicitFormula/NymanBeurling.lean on the branch %s. The dilation family ρ_θ(x) = {θ/x} − θ{1/x} as functions on the unit '
         'interval, each in Mathlib’s Lp 2 for the Lebesgue measure on (0, 1); its two obligations %s. NB: the constant function 1 lies in '
         'the closure of the span of the ρ_θ, 0 < θ ≤ 1; BD: the same over θ = 1/(n + 1). The equivalence NB ↔ RiemannHypothesis enters '
         'as the named premise NymanBeurlingPremise (T1-lit), its citation read from the registry records once each and printed beside the '
         'ferry’s recollection -- %s; rh_iff_nb reads %s on that premise alone. The finite distances d_N, the distance from 1 to the span '
         'of the first N Báez-Duarte dilations, defined as reals, and distN_antitone -- d_N monotone non-increasing -- reads %s. %d '
         'prints, beyond the standard three %s, sorryAx %s. The face is a fourth compiled face of the clause at INTERFACES on the classical '
         'equivalence; it proves no part of that equivalence. H63a %s, H63b %s, H63c %s.' % (
             tag, K.FACE_BRANCH, ', '.join('%s %s' % (o, v) for o, v in obl.items()), reads,
             FG['nodes'].get('rh_iff_nb', {}).get('grade'), FG['nodes'].get('distN_antitone', {}).get('grade'),
             len(PR['prints']), PR['beyond'] or 'none', 'present' if PR['sorry'] else 'absent', S['H63a'][0], S['H63b'][0], S['H63c'][0]), '',
         '**The intake form** (`(R239)`(2)): the clause entered beneath the synthesis form`s clauses (OPEN_TRAILS :%d), from b628`s pilot, the '
         'pilot`s figures its example; a document filed not for publication keeps its full bank local.' % rl['lines'][1]['line'], '',
         '**The b592 test** (`(R239)`(3)): tools/test_chain_page_b592.py runs the generator against its own pinned lists and probes and '
         'nothing live; the test %d of %d by its case pattern, the test as it stood failing %s; committed alone. Every test file under tools/ '
         'ran at step zero (data/b629_tests_stepzero.txt).' % (TR['passing'], TR['cases'], TR['control']['failing']), '',
         '**The pages, the table and the root.** The ζ page re-emitted at v0.24 from a fresh probe with the face’s nodes (data/b629_page_zeta.json); '
         'the table`s grade column %s. The root of b629 over %d repositories, %d tags and %d banks; the chain verified, %s. b628’s weight at '
         'FINDINGS :%d; the clone and cache paths beside :13065 (OPEN_TRAILS :%d).' % (
             'unmoved but for the face`s own rows' if S['H63d'][0] == 'HOLDS' else 'moved, see the scores', len(J['reads']['heads']),
             len(J['reads']['tags']), len(J['reads']['banks']), ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify']),
             rl['lines'][0]['line'], rl['lines'][2]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b623’s bright-register reading that priced the face (OPEN_TRAILS '
         ':12893) and b626’s rung, whose named-premise form it follows; the clause’s faces -- Weil positivity, Li’s criterion, the '
         'forall-upto pair -- gain an L² face, the one that turns the clause into a distance. It strengthens the programme’s offering of '
         'one located clause read through many faces, each carried at its honest grade.', '',
         '**Next.** Per `(R239)`(5): b630, the Nyman–Beurling bench, d_N computed up to a named bound beside Báez-Duarte’s rate, a T3/T4 '
         'bench with no claim. The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH holds or that NB does.*', '']
    return t, NL.join(e)


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
    put_json('b629_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) the measure the unit interval`s Lebesgue measure restricted to (0, 1) on ℝ, Lp 2 of it the space; (2) BD`s θ = 1/n '
              'for n ≥ 1 written θ = 1/(n + 1) for n : ℕ, and d_N over the first N of them; (3) d_N defined as the distance itself, its '
              'square the ruling`s d_N², the monotonicity stated on d_N; (4) the dilation family defined for every real θ, its obligations '
              'proved for every θ, NB restricting θ to (0, 1]; (5) the registry reads: Crossref for Beurling`s DOI, arXiv for Báez-Duarte, '
              'a Crossref search for Nyman`s thesis, each once; (6) test_asof.py`s case (9), failing once at step zero on the remote read '
              'of b567`s tag and passing alone, recorded as transient')


def _decl(src, name):
    m = re.search(r'^(?:theorem|def|noncomputable def|abbrev) %s\b[^\n]*(?:\n(?![ \t]*\n)[^\n]*)*?:=' % re.escape(name), src, re.M)
    return ' '.join(m.group(0).split()) if m else '### NOT READ AT THE PIN'


def _next_lines():
    src = _face_src(K.FACE_TAG)
    return ['%s (SIDE-explicit-formula %s, %s): %s' % (n, K.FACE_TAG, K.FACE_FILE, _decl(src, n.split('.')[-1])) for n in (K.FACE_NS + '.distN', K.MONO)]


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b629_scores.json', 'b629_findings.json', 'b629_record_lines.json', 'b629_act_root.json'))
    rc = _relay_commits()
    tst = (_alone(RELAY, [K.TEST_FILE], rc) or ['?'])[0]
    tag = g(K.KER, 'rev-parse', '--short=7', K.FACE_TAG + '^{commit}').strip()
    n_ans = len(re.findall(r'^### PROMPT ', rd('b629_author_answers.txt'), re.M))
    rows_ = ['', TRAIL_HEAD, '',
             '**(R239) ratified.** (1) b628 at its weight. (2) The intake form, a clause. (3) The b592 test repaired. (4) '
             'W-ORD-NYMAN-BEURLING-FACE, its opening act. (5) The act after: b630.', '',
             '**Entered:** FINDINGS.md:%d (b628’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the intake form, beneath :12699), :%d (the '
             'clone and cache, to :13065); this record; relay tools/test_chain_page_b592.py %s; SIDE-explicit-formula v0.24 = %s.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'], tst, tag), '',
             '**Act root:** b629 `%s` (previous `%s`, b628’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**Prompts to the author:** %d (relay data/b629_author_answers.txt)%s.' % (
                 n_ans, (': ' + ' / '.join(_elide(answer_of(i)) for i in range(n_ans))) if n_ans else ''), '',
             '**The next act’s terminals, each statement at its pin** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b629_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R239)`(5), b630, the Nyman–Beurling bench (the second act); the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


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
    put_json('b629_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b629_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b629 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b629_defects.json -- NOTHING WRITTEN')
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
    put_json('b629_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


def desk(*a):
    S = jl('b629_scores.json')
    L = ['=' * 104, 'b629 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H63a-H63d, (R239)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H63 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b629_defects.txt').rstrip(NL).split(NL)
    put_txt('b629_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b629_scores.json', 'b629_findings.json', 'b629_trail.json', 'b629_record_lines.json', 'b629_act_root.json'))
    L = ['b629 -- THE COMPONENTS, BANKED UNDER (R239).', '',
         '### COMPONENT 0 : the process listing ; b628`s closing push-out relay %s ; push-b628* branches deleted by name (data/b629_branches.txt) ; '
         'every test file under tools/ run (data/b629_tests_stepzero.txt) ; the suite, b628`s predicates repaired, run at HEAD before the '
         'face (data/b629_arms_prerun.txt) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b628`s weight FINDINGS :%d ; the intake form OPEN_TRAILS :%d ; the clone and cache :%d ; the b592 test repair '
         'data/b629_test_repair.txt' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : data/b629_nb_api.txt',
         '### COMPONENT 3 : data/b629_citation.txt ; data/b629_build.txt ; data/b629_prints.txt ; data/b629_face.txt ; v0.24 ; H63a %s, H63b %s, '
         'H63c %s' % (S['H63a'][0], S['H63b'][0], S['H63c'][0]),
         '### COMPONENT 4 : the ζ page at v0.24 (data/b629_page_zeta.json, data/b629_nodes_zeta.txt, data/b629_probe_out.txt) ; the table ; page arms '
         'data/b629_page_arms.txt ; the root %s ; the arm data/b629_root_arm.txt ; H63d %s' % (J['root'][:16], S['H63d'][0]),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b630 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b629_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b629_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
