# -*- coding: utf-8 -*-
"""b627_record.py -- THE ACT'S RECORD TOOL, UNDER (R237). ### ONE SUBCOMMAND PER BANK.

### ### b627: LANE THREE, ACT FIFTY-FOUR -- THE POSITIVITY MARGIN AT HEIGHT FROM THE PRIME SIDE; THE SEAM EQUIVALENCE RULED; THE
### BOUNDED SHAPE ENTERED; THE CLOSING FORM AMENDED.
### Subcommands write only `data/b627_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`; CORRESPONDENCE rows through relay tools/corr_row.py's `write_row`. The data is tools/b627_worklist.py.
### No platform call. The generator as it stood before the act is read from its blob at relay PRE_RELAY. The case counter is
### (R233)(3)'s standing form (OPEN_TRAILS :12889); the N5 scorer takes the trail record's expected line (OPEN_TRAILS :12799).
### The bench's numbers are tools/b627_margin.py's, run by the seat; this tool reads its banks and never computes a value.
"""
import difflib
import io
import json
import os
import re
import runpy
import subprocess
import sys
import tempfile
import time
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b627_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
SESSION_ID = 'f5c41941-fa74-40e9-b806-a98e7280e315'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b627_registration_2026-10-05.txt'

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
_DJ = os.path.join(D, 'b627_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b627 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b627_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the bench`s work-order, the rung`s and its mismatch line, the correction, the next act`s two work-orders, the '
         'precedence and authority orders, the build clause, the N5 line, the seam equivalence`s cell, b622`s record of the sieve',
         PP, PRE_PP, 'OPEN_TRAILS.md', [10884, 11864, 12228, 12354, 12356, 12799, 12865, 12891, 12893, 12897, 12970, 12998, 13026], 1500),
        ('FINDINGS: b626`s entry and the sieve at v0.6', PP, PRE_PP, 'FINDINGS.md', [7474, 7563], 600),
        ('SIDE-explicit-formula v0.20: the window family and its two obligations', K.KER, 'v0.20', 'SIDEExplicitFormula/Schema/PlateauRamp.lean',
         [45, 48, 51, 55, 56, 57, 151, 152, 153, 156, 157, 158, 173, 174, 175, 178], 300),
        ('SIDE-explicit-formula v0.20: the identity`s terms', K.KER, 'v0.20', 'SIDEExplicitFormula/B321Identity.lean', [24, 25, 26, 29, 30, 33, 34, 37, 38, 44, 45, 46], 300),
        ('SIDE-explicit-formula v0.20: the Weil test, the bracket, the transform, classK', K.KER, 'v0.20', 'Zeta23/ExplicitFormula.lean', [64, 68, 80], 300),
        ('SIDE-explicit-formula v0.20: paperFT', K.KER, 'v0.20', 'Zeta23/Defs.lean', [60], 300),
        ('SIDE-explicit-formula v0.20: classK', K.KER, 'v0.20', 'SIDEExplicitFormula/H2Sign.lean', [24, 25, 26], 300),
        ('SIDE-explicit-formula v0.22: the seam equivalence', K.KER, 'v0.22', 'SIDEExplicitFormula/PowerLimit.lean', [1240], 300),
        ('SIDE-explicit-formula v0.22: the rung', K.KER, 'v0.22', 'SIDEExplicitFormula/PlattRung.lean', [31, 32, 36, 47, 51, 52, 56], 300),
        ('SIDE-explicit-formula v0.22: the next act`s route-(b) terminals', K.KER, 'v0.22', 'SIDEExplicitFormula/Simplicity.lean', [40, 41, 45, 46, 47], 300),
        ('formal-math 3635e748 (Zeta23 v1.0): the route-(b) source terminal', K.FM, '3635e748', 'Zeta23/FinalMult.lean', [350, 351], 300),
        ('SIDE-global-section: the seam equivalence`s cell and the last row', K.GS, K.PRE_GS, 'CORRESPONDENCE.md', [456, 523], 500),
        ('relay tools/chain_page.py: the shape reader', RELAY, PRE_RELAY, 'tools/chain_page.py',
         ('GREP', r'^SHAPES =|^SHAPE_KEY|^def (shape_of|_shape|_read|_domain|_bounded|_binders)\(|return .FINITE. if ty\.strip'), 300),
        ('relay tools/test_chain_page_b596.py: its cases', RELAY, PRE_RELAY, 'tools/test_chain_page_b596.py', ('GREP', r"res\.append\(\('\(\d+\)"), 200),
        ('relay tools/b626_closing.py: the closing form', RELAY, PRE_RELAY, 'tools/b626_closing.py', ('GREP', r'^CARRIED|THE NEXT ACT'), 300),
        ('PLACE-papers: the withdrawn super-repulsion bench (FINDING W-BENCH-1); the record names no script, input or bank path', PP, PRE_PP,
         'archive/2026-08-24-ledger-split/VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md', [1810, 1816], 700),
        ('PLACE-papers: the sieve`s shape column', PP, PRE_PP, 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md', [23], 400),
        ('relay data/b626_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b626_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b627 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### the super-repulsion bench`s script, inputs and bank: the finding (:1816 above) names none; relay`s tracked files carrying '
              'the phrase are record tools and banks quoting the sieve, none a bench (git grep, relay HEAD %s)' % g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()]
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b627_reads.txt', L)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R237) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
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
    L = ['### b627 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b627_author_answers.txt', L)


def answer_of(k):
    """### the author's answer to the act's k-th prompt (0-based, across calls), whole: cut from the result after its own question's
    ### `"<question>"="` and before the next question's `", "<question>"="`, the questions read from the bank's prompt headers."""
    t = rd('b627_author_answers.txt')
    qs, i = [], 0
    for blk in re.split(r'^### CALL ', t, flags=re.M)[1:]:
        res = re.search(r'^RESULT \(transcript line \d+\): (.*)$', blk, re.M)
        for q in re.findall(r'^### PROMPT \d+ \([^)]*\): (.*)$', blk, re.M):
            qs.append((q, res.group(1) if res else ''))
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


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-fano-darkness', 'SIDE-li-map')
KERN_PIN = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7',
            'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab', 'SIDE-explicit-formula': 'e939c92'}
WRITTEN_KERNS = ('SIDE-global-section',)   # ### the one this act writes: the seam equivalence's CORRESPONDENCE row


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
    put_json('b627_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ THE LEDGER HELPERS
def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def predict_cells(text, ledger):
    """### the grade cells the terminal table's tight reader takes from `text` appended to `ledger`, the FINDINGS-form directive's
    ### own line excepted for its terminal: [(line offset, name, grade)]."""
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
    p = os.path.join(SP if DRY else D, 'b627_scanfile_%s.md' % name)
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
B626_ENTRY = 7563
SIEVE_REC = 12865
W_HEAD = '*Appended 2026-10-05 by b627 to b626’s entry (:%d), under `(R237)`(1) -- b626 AT ITS WEIGHT:*'
CF_HEAD = '*Appended 2026-10-05 by b627, under `(R237)`(4) -- THE CLOSING FORM, A CLAUSE AT THE RECORD’S FORM:*'
SV_HEAD = '*Appended 2026-10-05 by b627 to b622’s record of the sieve at v0.6 (:%d), under `(R237)`(3) -- THE SIEVE’S SHAPE COLUMN, AN ITEM FOR ITS NEXT VERSION:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry):
    pre, post = _count_bank(_rel('b626_checks.txt')), _count_bank(_rel('b626_checks_postpush.txt'))
    DJ = json.loads(_rel('b626_defects.json'))
    roots = [l.split() for l in _rel('act_roots.txt').split(NL) if l.startswith('b626 ')]
    return ('\n%s SIDE-explicit-formula v0.22 = e939c92 on the kept branch platt-b626: rh_upto T; the height pair forall_rh_upto_iff_rh '
            'at no premise through the vendored Bulka bridge, definitional, carrying no analytic content; PlattTrudgianHeight T a Prop '
            'carrying rh_upto T as the T1-lit premise; plattTrudgianT := 3 * 10 ^ 12; the rung rh_upto_platt on that premise alone; the '
            'build detached at the hold (985 s), six prints at the standard three, no sorryAx, the tag read back equal. The citation by '
            'Crossref’s record of the publisher’s deposit after the publisher’s 403, the arXiv abstract agreeing on the height, the '
            'module’s docstring naming the source; the entry’s “publisher’s page read once” corrected at OPEN_TRAILS :13026. The '
            'forall-upto mismatch recorded beside :12891 as the navigator’s, the support pair untouched. The rule reading seam '
            'antecedents alone (rh_strip_imp_rh entered with its principle) and data binders as objects, its test 20 of 20, cases '
            '(16)-(19) failing on the old rule; four grades moved; CORRESPONDENCE row 446 for the seam node, the ζ page’s conflict row '
            'closed; the two section terminals corrected by rows 447-450, the χ page unchanged. H60a-H60c held; H60d refuted on '
            'measurement, its letter the navigator’s, written before the column’s vocabulary was checked against the statement '
            '(`(R237)`(3)); N1-N5 and S1-S5 held. Relay 746ab804; PLACE-papers a43e1ba; SIDE-global-section dbacb9f. The root %s, '
            'b624-b626 verifying. The suite %d of %d before the push and %d of %d after it by the seat’s defect (a), the claim tested '
            'directly and holding; defects (a)-(c) the seat’s (relay data/b626_defects.txt, %d entries). Nothing deposited; no sorry on '
            'any main.\n' % (W_HEAD % entry, (roots[0][1][:8] + '…' + roots[0][1][-4:]) if roots else '?', pre[0], pre[1], post[0], post[1],
                             len(DJ['defects'])))


def _closing_form():
    return ('\n%s a closing that names the next act’s terminals prints, beneath each name, that terminal’s statement read at its pin, '
            'so the navigator prices the next act against statements and not names -- the forall-upto mismatch (:12998), the arrow '
            'clause’s over-breadth (:12994) and the ENCODES outcome were each a ferry written from a name. Where the next act names a '
            'work-order with no kernel terminal yet, the closing says so. Applied by the seat from b627’s closing: relay '
            'tools/b627_closing.py’s carried section, edited after b627’s seal and committed alone, prints the terminals of both '
            'routes `(R237)`(6) names, each statement read by git at its pin.\n' % CF_HEAD)


def _sieve_item():
    return ('\n%s the sieve’s shape column (phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md :23, “FINITE, UNIVERSAL, LIMIT, DENSITY or '
            'FAMILY, read by the generator”) takes the word BOUNDED at its next version: a universal quantifier whose body carries an '
            'explicit numeric bound on the quantified variable’s height, norm or index, FINITE kept for Finset and finite-range forms '
            '(`(R237)`(3)); each row naming a page node re-read from the generator as edited at b627. Not started; the version is the '
            'author’s word.\n' % (SV_HEAD % SIEVE_REC))


def record_lines(*a):
    """### FINDINGS: b626's weight (to its entry :7563). OPEN_TRAILS: the closing-form clause; the sieve's item (to b622's record
    ### :12865). No line makes a table cell (predicted)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The Platt–Trudgian height as a named premise at v0.22')
    if entry != B626_ENTRY:
        sys.exit('### b626`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % entry, _weight(entry)), ('OPEN_TRAILS.md', CF_HEAD, _closing_form()),
             ('OPEN_TRAILS.md', SV_HEAD % SIEVE_REC, _sieve_item())]
    cells, nd, clean = _guarded(items, 'OPEN_TRAILS.md', 'lines')
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    _land(Q, items, 'b627_record_lines.json', entry)


# ================================================================================ COMPONENT 1: THE SEAM EQUIVALENCE'S CORRECTIONS
CORR = os.path.join(K.GS, 'CORRESPONDENCE.md')
CT_HEAD = '*Appended 2026-10-05 by b627 to :%d, under `(R237)`(2) -- A CORRECTION ENTRY, THE SEAM PRINCIPLE:*'


def _chiff_trail_text():
    return ('\n%s\nSUPERSEDES OPEN_TRAILS :%d for `ch_iff_h2_sign_of_seam`: INTERFACES -- the node SIDEExplicitFormula.B321.ch_iff_h2_sign_of_seam '
            '(SIDE-explicit-formula v0.22 = e939c92, PowerLimit.lean :1240, the statement rh_strip_imp_rh → (conservationHypothesis ↔ h2_sign)) '
            'is graded on its seam premise rh_strip_imp_rh by the seam principle the author ruled at `(R237)`(2): an equivalence presented '
            'under an open seam premise is graded as its consequent is. The shared E0 rule reads it so since relay 629ef408 (b626); the '
            'grade the line :%d carried for it is replaced for this terminal alone, and :%d stands unedited above.\n' % (
                CT_HEAD % K.CHIFF_TRAIL, K.CHIFF_TRAIL, K.CHIFF_TRAIL, K.CHIFF_TRAIL))


def chiff_trail(*a):
    """### (R237)(2): ch_iff_h2_sign_of_seam's OPEN_TRAILS cell (:10884) superseded in OPEN_TRAILS's own directive form -- the one
    ### cell the line makes is the terminal's, INTERFACES (predicted, refused otherwise). Written alone; committed alone by the seat."""
    Q = R2._Q()
    t = _chiff_trail_text()
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'chiff_trail')
    want = [(2, 'ch_iff_h2_sign_of_seam', 'INTERFACES')]
    print('  table cells the line would make: %s (wanted %s) ; no-disclosure hits: %s ; scanner %s' % (cells, want, nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(t)
        return
    if [(i, n.split('.')[-1], gr) for i, n, gr in cells] != want or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD MAKE ANOTHER CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CT_HEAD % K.CHIFF_TRAIL)
    r = Q.append_to(Q.OT, t)
    put_json('b627_chiff_trail.json', dict(line=Q.line_of(Q.OT, CT_HEAD % K.CHIFF_TRAIL), head=CT_HEAD % K.CHIFF_TRAIL, cells=cells, append=r, at=utc()))
    print('  OPEN_TRAILS correction :%s' % jl('b627_chiff_trail.json')['line'])


def _rownums():
    return [int(m.group(1)) for m in re.finditer(r'^\|\s*(\d+)\s*\|', io.open(CORR, encoding='utf-8').read(), re.M)]


def _corr_cells(num, sup, name):
    short = name.split('.')[-1]
    return [str(num),
            '**%s’S GRADE UNDER THE SUPERSESSION RULE** (b627, under the author’s ruling (R237)(2)): this row’s grade cell replaces row '
            '%d’s for this terminal alone; row %d stands unedited above. The seam principle: an equivalence presented under an open seam '
            'premise is graded as its consequent is; its premise rh_strip_imp_rh, the seam the E0 rule names (relay 629ef408).' % (short, sup, sup),
            '`SIDE-explicit-formula` (v0.22 = e939c92) : `%s`' % name,
            'the axiom print of row %d, unchanged' % sup,
            'SUPERSEDES row %d: INTERFACES -- `%s`' % (sup, name),
            'Written 2026-10-05 (b627) through relay tools/corr_row.py; the rule is `supersede` in relay tools/terminal_table.py.']


def chiff_row(*a):
    """### (R237)(2): ch_iff_h2_sign_of_seam's CORRESPONDENCE cell (row 383, line 456) superseded by one row in CORRESPONDENCE's own
    ### form, through the row writer. Committed alone in SIDE-global-section by the seat."""
    import corr_row as CR
    import terminal_table as TT
    nxt = max(_rownums()) + 1
    rows = [_corr_cells(nxt + i, sup, n) for i, (sup, n) in enumerate(K.CHIFF_CORR)]
    text = NL.join('| ' + ' | '.join(c) + ' |' for c in rows)
    pred = []
    for ln in text.split(NL):
        for off, seg in TT._segments(ln):
            for m in TT.GRADE_RE.finditer(seg):
                pred.append((ln.split('|')[1].strip(), m.group(1), [x[2] for x in TT._names_on(seg)]))
    nd, _n = _nd(text)
    sc, clean = _scan_text(text, 'chiff_row')
    print('  rows %s ; grade words by row %s ; no-disclosure hits %s ; scanner %s' % ([r[0] for r in rows], pred, nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(text)
        return
    if any(nd.values()) or not clean or any(len(p[2]) != 1 for p in pred) or len(pred) != len(rows):
        sys.exit('### A ROW WOULD MAKE MORE THAN ITS ONE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    out = []
    for cells in rows:
        code, msg = CR.write_row(CORR, cells)
        out.append(dict(row=int(cells[0]), supersedes=int(cells[4].split('row ')[1].split(':')[0]), name=cells[2].split('`')[-2], code=code))
        if code != 0:
            put_json('b627_chiff_row.json', dict(rows=out, at=utc(), stopped=True))
            sys.exit('### corr_row refused row %s (code %d): %s' % (cells[0], code, msg))
    put_json('b627_chiff_row.json', dict(rows=out, at=utc()))
    print('  CORRESPONDENCE rows written: %s' % [(x['row'], x['supersedes']) for x in out])


# ================================================================================ COMPONENT 1: THE CLOSING FORM'S EDIT
def _first_commit_of(path):
    l = [x for x in g(RELAY, 'log', '--reverse', '--format=%h', PRE_RELAY + '..HEAD', '--', path).split(NL) if x.strip()]
    return l[0] if l else None


def closing_edit(*a):
    """### the closing tool's carried section edited after the seal (the Edit tool): the diff against the tool as sealed (its first
    ### relay commit, the sealed tools' commit), and the next act's terminals as the edited tool prints them (data/b627_closing_edit.txt)."""
    import importlib
    sealed = _first_commit_of('tools/b627_closing.py')
    d = g(RELAY, 'diff', sealed, '--', 'tools/b627_closing.py') if sealed else '### NO SEALED COMMIT'
    st = g(RELAY, 'diff', '--stat', sealed, '--', 'tools/b627_closing.py').rstrip(NL).split(NL)[-1].strip() if sealed else ''
    sys.modules.pop('b627_closing', None)
    C = importlib.import_module('b627_closing')
    nt = C.next_terminals() if hasattr(C, 'next_terminals') else ['### the tool prints no next-act terminal']
    L = ['b627 -- COMPONENT 1, (R237)(4): THE CLOSING TOOL`S CARRIED SECTION, EDITED AFTER THE SEAL, AGAINST THE TOOL AS SEALED (relay %s) (%s)' % (
        sealed, utc()), '', '### ' + (st or 'NO DIFF'), ''] + d.rstrip(NL).split(NL) + ['', '### THE NEXT ACT`S TERMINALS, AS THE EDITED TOOL PRINTS THEM:'] + nt
    put_txt('b627_closing_edit.txt', L)
    put_json('b627_closing_edit.json', dict(at=utc(), sealed=sealed, stat=st, terminals=nt))
    for l in nt:
        print(l[:220])


# ================================================================================ COMPONENT 2: THE BOUNDED SHAPE
def cp_module(rev=None):
    """### tools/chain_page.py at relay `rev` (None: as it stands), loaded as a module of its own."""
    if rev is None:
        import chain_page as CP
        return CP
    src = _show(RELAY, rev, 'tools/chain_page.py')
    m = types.ModuleType('chain_page_%s' % rev)
    m.__file__ = os.path.join(ROOT, 'tools', 'chain_page.py')
    exec(compile(src, 'chain_page@%s' % rev, 'exec'), m.__dict__)
    return m


def gen_diff(*a):
    d = g(RELAY, 'diff', PRE_RELAY, '--', *K.GEN_FILES)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', *K.GEN_FILES)
    L = ['b627 -- COMPONENT 2, (R237)(3): THE SHAPE READER`S BOUNDED WORD AND ITS TEST, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), '',
         '### ' + (st.rstrip(NL).split(NL)[-1].strip() if st.strip() else 'NO DIFF'), ''] + d.rstrip(NL).split(NL)
    put_txt('b627_gen_diff.txt', L)
    print(L[2])


CONTROL_FMT = '### THE POSITIVE CONTROL: the same test with tools/chain_page.py as it stood at relay %s (exit %d): cases %d, passing %d, failing %s'
CONTROL_RE = r'^### THE POSITIVE CONTROL: the same test with tools/chain_page\.py as it stood at relay (\w+) \(exit (\d+)\): cases (\d+), passing (\d+), failing (.*)$'


def gen_test(*a):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    test = os.path.join(ROOT, 'tools', 'test_chain_page_b596.py')
    r = subprocess.run([sys.executable, test], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out, COUNT_CASE)
    old = os.path.join(tempfile.mkdtemp(), 'chain_page_old.py')
    _write(old, _show(RELAY, PRE_RELAY, 'tools/chain_page.py').encode('utf-8'))
    runner = ('import sys, types, runpy; sys.path.insert(0, %r); m = types.ModuleType("chain_page"); m.__file__ = %r; '
              'exec(compile(open(%r, encoding="utf-8").read(), "chain_page@old", "exec"), m.__dict__); sys.modules["chain_page"] = m; '
              'runpy.run_path(%r, run_name="__main__")' % (os.path.join(ROOT, 'tools'), os.path.join(ROOT, 'tools', 'chain_page.py'), old, test))
    r2 = subprocess.run([sys.executable, '-c', runner], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    out2 = (r2.stdout or '') + (r2.stderr or '')
    n2, p2 = count_cases(out2, COUNT_CASE)
    failed2 = [re.match(r'^  (\(\d+\))', l).group(1) for l in out2.split(NL) if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]
    L = ['b627 -- COMPONENT 2: tools/test_chain_page_b596.py RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p), '',
          CONTROL_FMT % (PRE_RELAY, r2.returncode, n2, p2, failed2)]
    put_txt('b627_gen_test.txt', L)
    put_json('b627_gen_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, control=dict(rc=r2.returncode, cases=n2, passing=p2, failing=failed2)))
    print(L[-3])
    print(L[-1])


def _node_shapes(CP):
    out = {}
    for k in ('zeta', 'chi'):
        cs = CP.parse(io.open(os.path.join(D, K.PROBE[k]), encoding='utf-8').read().replace(chr(13), ''))[0]
        names = [l.split(' | ')[0] for l in rd(K.NODES[k]).split(NL) if l and not l.startswith('#')]
        for n in names:
            if n in cs:
                out[(k, n)] = CP.shape_of(n, cs)
    return out


def shapes(*a):
    """### every page node's shape by the reader before (relay PRE_RELAY) and after the edit, both pages (data/b627_shapes.txt, .json)."""
    old, new = _node_shapes(cp_module(PRE_RELAY)), _node_shapes(cp_module(None))
    moved = sorted((k, n, old[(k, n)], new.get((k, n))) for (k, n) in old if old[(k, n)] != new.get((k, n)))
    L = ['b627 -- COMPONENT 2: EVERY PAGE NODE`S SHAPE, BY THE READER AT relay %s AND AS EDITED (%s)' % (PRE_RELAY, utc()), '',
         '### nodes read %d (ζ %d, χ %d) ; shapes moved %d' % (len(old), sum(k == 'zeta' for k, _n in old), sum(k == 'chi' for k, _n in old), len(moved)), '']
    L += ['  %-5s %-62s %s -> %s%s' % (k, n, a_, b_, '' if n in K.BOUNDED_WANT else ' ### NOT A NODE THE CLAUSE NAMES') for k, n, a_, b_ in moved] or ['  NONE']
    L += ['', '### THE RUNG`S FIVE, AS EDITED:'] + ['  %-62s %s' % (n, new.get(('zeta', n))) for n in K.RUNG_NODES]
    L += ['', '### ### **NODES %d ; SHAPES MOVED %d ; OUTSIDE THE CLAUSE`S NODES %d.**' % (len(old), len(moved), sum(n not in K.BOUNDED_WANT for _k, n, _a, _b in moved))]
    put_txt('b627_shapes.txt', L)
    put_json('b627_shapes.json', dict(at=utc(), moved=[list(x) for x in moved], rung={n: new.get(('zeta', n)) for n in K.RUNG_NODES}, nodes=len(old)))
    print(L[-1])


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


def _shapes(text):
    out = {}
    for l in (text or '').split(NL):
        m = re.match(r'^\d+\. `([^`]+)` — .* — shape: ([A-Z—-]+|—) — ', l)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked list and probe; written where it changed; every shape and
    ### grade cell that moved printed (data/b627_page_<k>.json)."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b627_%s' % k), os.path.join(D, K.PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b627_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = _grade_cells(prev.decode('utf-8')), _grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n) and n in ga and n in gb)
    sa, sb = _shapes(prev.decode('utf-8')), _shapes(pg)
    smoved = sorted([n, sa.get(n), sb.get(n)] for n in set(sa) | set(sb) if sa.get(n) != sb.get(n))
    put_json('b627_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, shapes_moved=smoved, key_changed=CP.SHAPE_KEY not in prev.decode('utf-8'),
                                           rung={n: sb.get(n) for n in K.RUNG_NODES}, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s' % (k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE'))
    print('  shapes moved: %s' % (smoved or 'NONE'))
    for x in dl[:30]:
        print('    ' + x[:240])


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b627 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b627_gcp'), os.path.join(D, K.PROBE[k]))
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
    put_txt('b627_page_arms.txt', L)
    for l in L:
        print(l[:240])


def _table_grades():
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    tg = {}
    for r in T['rows']:
        tg.setdefault(r['name'], r['grade'])
    return tg


def table(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    tg = _table_grades()
    ch = [(x[1] if isinstance(x, list) else x) for x in diff.get('changed') or []]
    tag = a[0] if a and a[0] != 'dry' else 'table'
    L = ['b627 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(ch)),
         '### the rows changed, with the grade each now reads (read from the table, not the diff):']
    L += ['  %-62s %s' % (n, tg.get(n)) for n in ch] or ['  NONE']
    L += ['### the rows added: %s' % [(x[1] if isinstance(x, list) else x) for x in diff.get('added') or []],
          '### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
          '### ### **THE GRADE COLUMN`S DIFF : %s.**' % ('; '.join('%s %s' % (n.split('.')[-1], tg.get(n)) for n in ch) or 'EMPTY')]
    name = 'b627_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 changed=ch, grades={n: tg.get(n) for n in ch}, files_moved=moved))
    print(L[-1])


# ================================================================================ COMPONENTS 3-4: THE BENCH'S BANKS, READ
def _margin(text=None):
    t = text if text is not None else rd('b627_margin.txt')
    rows = [l for l in t.split(NL) if l.startswith('ROW ')]
    out = dict(rows=len(rows), yes=sum(' positive=YES' in l for l in rows), straddles=sum(' positive=STRADDLES' in l for l in rows),
               no=sum(' positive=NO' in l for l in rows))
    m = re.search(r'THE MINIMUM OVER N : (\S+) AT ORDINATE (\d+), t = (\S+)\.', t)
    out['min'] = (m.group(1), int(m.group(2)), m.group(3)) if m else None
    m = re.search(r'CERTIFIED DIGITS AT THE WORST VALUE (\d+)', t)
    out['digits'] = int(m.group(1)) if m else None
    m = re.search(r'LOG-LOG SLOPE AGAINST HEIGHT, ONCE: (\S+)', t)
    out['slope'] = m.group(1) if m else None
    out['checks'] = re.findall(r'^CHECK (\d+) t=(\S+) Q_mpmath=(\S+)$', t, re.M)
    out['convention'] = re.findall(r'^CONVENTION (\d+) t=(\S+) zero_side_over_the_table=(\S+)$', t, re.M)
    out['q'] = {int(l.split()[1]): re.search(r' Q=(\S+)', l).group(1) for l in rows}
    return out


def bench_rerun(path, *a):
    """### the second run's assembled bank (the scratchpad), compared byte for byte with data/b627_margin.txt (data/b627_margin_rerun.json)."""
    a_, b_ = open(_r('b627_margin.txt'), 'rb').read(), open(path, 'rb').read()
    put_json('b627_margin_rerun.json', dict(at=utc(), second=path, bytes=[len(a_), len(b_)], sha256=[sha(a_), sha(b_)], equal=a_ == b_))
    print('  the two runs: %d and %d bytes ; equal byte for byte %s' % (len(a_), len(b_), a_ == b_))


# ================================================================================ COMPONENT 5: THE ROOT
ROOT_EXCLUDE = re.compile(r'^b627_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    keep = re.compile(r'^b627_closing_edit\.(txt|json)$')
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b627_') and os.path.isfile(os.path.join(D, f))
                  and (keep.match(f) or not ROOT_EXCLUDE.match(f)))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b627'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import act_root as AR
    res = AR.verify()
    J = jl('b627_act_root.json')
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
    L = ['b627 -- COMPONENT 5: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s) ; '
              'the copy`s root differs %s' % (bank, r2, same, J['root'], r2 != J['root']),
          '### ls-remote calls by the arm, per repository: %d repositories, at most %d each' % (len(AR.LSR), max(AR.LSR.values()) if AR.LSR else 0),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b627_root_arm.txt', L)
    put_json('b627_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, root_copy=r2, root_recomputed=same, root=J['root'],
                                        lsr=dict(AR.LSR)))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H61a', 'H61b', 'H61c', 'H61d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
BENCH_FILES = (K.BENCH_SCRIPT, 'data/b627_margin_inputs.txt', 'data/b627_margin.txt')


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
    m = re.search(r'locked at \(UTC\) : (\S+)', rd(FACE) or '')
    return _epoch(m.group(1)) if m else None


def _after_lock(repo, h):
    lk = _lock()
    return lk is not None and int(g(repo, 'show', '-s', '--format=%ct', h).strip() or 0) > lk


def sorry_tokens(rev='main'):
    """### `sorry` tokens at the explicit-formula kernel's `rev`, comments and docstrings stripped."""
    n = 0
    for f in g(K.KER, 'ls-tree', '-r', '--name-only', rev).split(NL):
        if f.endswith('.lean'):
            t = _show(K.KER, rev, f) or ''
            t = re.sub(r'/-.*?-/', '', t, flags=re.S)
            t = re.sub(r'--[^\n]*', '', t)
            n += len(re.findall(r'\bsorry\b', t))
    return n


def _page_lines_ok(k):
    """### every changed line of a page is a shape cell, the column's key line, or the seam equivalence's cell: nothing the bench moved."""
    import chain_page as CP
    P_ = jx('b627_page_%s.json' % k)
    bad = []
    for x in P_.get('diff') or []:
        body = x[1:]
        if not (' — shape: ' in body or body in (CP.SHAPE_KEY,) or 'ch_iff_h2_sign_of_seam' in body or body.startswith('The shape cell')):
            bad.append(x[:120])
    return bad


def n5(trail_line=None, ot=None, *a):
    """### N5 by its letter: nothing deposits; no kernel touched; no file written beyond the bench script and its two banks, the generator
    ### edit and its test, the record-tool edit, the suite repair, the correction entries, the re-emitted pages, the roots line, the
    ### record lines and the trails -- the act's own banks (data/b627_*), tools (tools/b627_*) and the table read as the record's."""
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
    face = jl('b627_kernels_face.json')['kernels']
    now = kern_state(list(face))
    others_ok = all(now[k] == list(v) for k, v in face.items() if k not in WRITTEN_KERNS)
    st = sorry_tokens('main')
    ker_files = sorted(set(x for x in g(K.KER, 'diff', '--name-only', K.PRE_KER, 'main').split(NL) if x.strip()))
    gs_files = sorted(set(x for x in g(K.GS, 'diff', '--name-only', K.PRE_GS, 'main').split(NL) if x.strip()))
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    want_pp = sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + [K.PNAME[k] for k in ('zeta', 'chi') if g(PP, 'diff', '--name-only', PRE_PP, 'HEAD', '--', K.PNAME[k]).strip()]))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith(('b627_', 'audit_b627_', 'terminal_table'))
                              and x != 'data/b626_closing_push_out.txt'))
    beyond = [x for x in relay_beyond if x not in set(K.GEN_FILES) | {'data/act_roots.txt'}]
    ok = others_ok and st == 0 and ker_files == [] and gs_files in ([], ['CORRESPONDENCE.md']) and pp_ch == want_pp and not beyond and rec_ok
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; the kernels this act does not write unmoved %s; sorry tokens on the explicit-formula main %d (comments '
            'stripped); the explicit-formula kernel`s files changed since v0.22 %s; SIDE-global-section %s; PLACE-papers %s; %s; relay '
            'beyond the list: %s' % (others_ok, st, ker_files or 'NONE', gs_files or 'NONE', pp_ch, rec_state, beyond or 'NONE'))


def scores(*a):
    M, RR, SH, GT = _margin(), jx('b627_margin_rerun.json'), jx('b627_shapes.json'), jx('b627_gen_test.json')
    PZ, PX, RA, TF = jx('b627_page_zeta.json'), jx('b627_page_chi.json'), jx('b627_root_arm.json'), jx('b627_table_final.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    face = jx('b627_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items() if k not in WRITTEN_KERNS) and \
        not g(K.KER, 'diff', '--name-only', K.PRE_KER, 'main').strip()
    bad_lines = _page_lines_ok('zeta') + _page_lines_ok('chi')
    all_pos = M['rows'] == K.N_ORD and M['yes'] == K.N_ORD
    moved = SH.get('moved') or []
    rung = SH.get('rung') or {}
    n3_ok = all(rung.get(n) == 'BOUNDED' for n in K.BOUNDED_WANT) and sorted(x[1] for x in moved) == sorted(K.BOUNDED_WANT)
    rc = _relay_commits()
    genc = _alone(RELAY, list(K.GEN_FILES), rc)
    tg = _table_grades()
    chk = M['checks']
    qd = M['q']
    rel = [abs(float(qm) - float(qd[int(j)])) / abs(float(qd[int(j)])) for j, _t, qm in chk if int(j) in qd]
    conv = [abs(float(z) - float(qd[int(j)])) / abs(float(qd[int(j)])) for j, _t, z in M['convention'] if int(j) in qd]
    ver = RA.get('verify') or []
    S = {
        'H61a': (('HOLDS' if all_pos else 'REFUTED'), 'values %d ; positive (the whole ball above zero) %d ; straddling %d ; negative %d ; the '
                 'minimum %s' % (M['rows'], M['yes'], M['straddles'], M['no'], M['min'])),
        'H61b': ('NOT SCORABLE', 'by the author`s answer before the seal: the super-repulsion fit was withdrawn at W-BENCH-1 and gives no curve; '
                 'the companion columns printed beside the values, nothing scored against them (the slope %s, a centre line, not a bound)' % M['slope']),
        'H61c': (('HOLDS' if kern_ok and not bad_lines else 'REFUTED'), 'no kernel touched %s; the pages moved by the clauses of (R237)(2)-(3) '
                 'alone, every changed line a shape cell, the key line or the seam equivalence`s cell, the bench moving none: lines beyond '
                 'those %s' % (kern_ok, bad_lines or 'NONE')),
        'H61d': (('HOLDS' if RR.get('equal') is True else 'REFUTED'), 'the second run`s bank %s against the first, sha256 %s' % (
            'byte-identical' if RR.get('equal') else 'DIFFERENT', (RR.get('sha256') or ['?'])[0][:16])),
        'N1': (('HELD' if all_pos else 'REFUTED'), 'positive %d of %d at the certified precision' % (M['yes'], M['rows'])),
        'N2': ('NOT SCORABLE', 'by the author`s answer before the seal, the fit withdrawn (W-BENCH-1)'),
        'N3': (('HELD' if n3_ok else 'REFUTED'), 'the rung`s five read %s; shapes moved over both pages %s' % (rung, [x[1].split('.')[-1] for x in moved])),
        'N4': (('HELD' if RR.get('equal') is True else 'REFUTED'), 'the two runs equal byte for byte %s' % RR.get('equal')),
        'N5': n5v,
        'S1': (('HELD' if len(genc) == 1 and _after_lock(RELAY, genc[0]) and GT.get('cases') and GT.get('cases') == GT.get('passing')
                and sorted((GT.get('control') or {}).get('failing') or []) == sorted(K.GEN_CONTROL_FAILING) else 'REFUTED'),
               'the reader and its test in one relay commit %s after the lock; the test %s of %s; the reader as it stood fails %s' % (
                   genc, GT.get('passing'), GT.get('cases'), (GT.get('control') or {}).get('failing'))),
        'S2': (('HELD' if sorted(x[1] for x in moved) == sorted(K.BOUNDED_WANT) and all(x[2] == 'UNIVERSAL' and x[3] == 'BOUNDED' for x in moved)
                else 'REFUTED'), 'shapes moved: %s' % moved),
        'S3': (('HELD' if tg.get(K.CHIFF) == 'INTERFACES' and (TF.get('changed') or []) == [K.CHIFF] else 'REFUTED'),
               'the table reads ch_iff_h2_sign_of_seam %s; rows changed %s' % (tg.get(K.CHIFF), TF.get('changed'))),
        'S4': (('HELD' if all_pos and (M['digits'] or 0) >= 25 and rel and max(rel) < 1e-15 and conv and max(conv) < 1e-8 else 'REFUTED'),
               'certified digits at the worst value %s; the mpmath midpoints` largest relative difference %s; the conventions` check %s' % (
                   M['digits'], '%.2e' % max(rel) if rel else 'none', '%.2e' % max(conv) if conv else 'none')),
        'S5': (('HELD' if ver and all(v[1] == 'AGREE' for v in ver) and [v[0] for v in ver] == ['b624', 'b625', 'b626', 'b627'] else 'REFUTED'),
               'the chain %s' % [(v[0], v[1]) for v in ver]),
    }
    put_json('b627_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 5: THE RECORD
TRAIL_HEAD = ('### b627 — lane three, act fifty-four under (R237): the positivity margin at height from the prime side at the lowest '
              'zeros; the seam equivalence ruled; the BOUNDED shape entered; the closing form amended')


def _title_entry():
    M = _margin()
    m = M['min'] or ('?', 0, '?')
    return ('## The positivity margin at height: the v0.20 window from the prime side at the lowest %d zeros to %s digits, minimum %s at '
            'ordinate %s, the withdrawn fit replaced by its companion columns; ch_iff_h2_sign_of_seam at INTERFACES; the BOUNDED shape, %d nodes' % (
                M['rows'], M['digits'], m[0][:12], m[2][:12], len(jx('b627_shapes.json').get('moved') or [])))


def _next_lines():
    return (jx('b627_closing_edit.json').get('terminals') or ['### the closing edit not banked'])


def _finding_text():
    S, rl, M = jl('b627_scores.json'), jl('b627_record_lines.json'), _margin()
    CT, CR_, SH, GT, J, RA = jl('b627_chiff_trail.json'), jl('b627_chiff_row.json'), jl('b627_shapes.json'), jl('b627_gen_test.json'), jl('b627_act_root.json'), jl('b627_root_arm.json')
    RR = jl('b627_margin_rerun.json')
    rc = _relay_commits()
    genc = (_alone(RELAY, list(K.GEN_FILES), rc) or ['?'])[0]
    clc = (_alone(RELAY, ['tools/b627_closing.py'], rc) or ['?'])[-1]
    inp = rd('b627_margin_inputs.txt')
    mt = re.search(r'ordinates in the read (\d+) ; taken (\d+)', inp)
    t = _title_entry()
    m = M['min'] or ('?', 0, '?')
    e = ['', t, '',
         '*Filed at b627 on the author’s ruling `(R237)` and the author’s three answers before the seal. Banks: relay `data/b627_margin_inputs.txt`, '
         '`data/b627_margin.txt`, `data/b627_margin_rerun.json`, `data/b627_gen_diff.txt`, `data/b627_gen_test.txt`, `data/b627_shapes.txt`, '
         '`data/b627_closing_edit.txt`, `data/b627_table_final.txt`, `data/b627_act_root.txt`, `data/b627_root_arm.txt`, '
         '`data/b627_author_answers.txt`; the script `tools/b627_margin.py`. Nothing deposits.*', '',
         '**The bench** (`(R237)`(5), W-ORD-MARGIN-BENCH, OPEN_TRAILS :12897, as the author answered before the seal): Q(t) = poleTerm − '
         'primeSum + archTerm at k_t = weilTest φ_t φ_t, φ_t(u) = cos(t u)·window 4 (1/3) 6 (u), the v0.20 window of PlateauRamp.lean :55-:57 '
         'at the classK floor p = 6 (:156-:158), L = 5, the prime sum over every n ≤ 22026 (exact, k_t vanishing beyond |u| = 10), at each '
         'of the lowest %s ordinates of Odlyzko’s table read once (%s; %s ordinates in the read). python-flint Arb balls at 200 bits '
         'throughout: the window and the prime sum exact in balls, the archimedean term by acb.integral with the closed-form tail beyond '
         't + 1200 added to the radius; mpmath for the midpoint cross-check alone. Values %d; the whole ball above zero %d, straddling %d, '
         'below %d; %s certified digits at the worst value; the minimum over N %s at ordinate %s (t = %s). The second run reproduces the '
         'bank byte for byte: %s. Beside each value the nearest-neighbour spacing at its ordinate, and once the margin’s least-squares '
         'log-log slope against height, %s -- a centre line, not a bound; nothing is scored against either. The super-repulsion fit the '
         'ruling named was withdrawn at W-BENCH-1 (VERIFICATION_LOOM archive :1816) and gives no curve: H61b and N2 NOT SCORABLE, by the '
         'author’s answer, the navigator’s. The mpmath midpoints at ordinates %s agree; the zero side summed over the table at the lowest '
         'ordinate agrees with Q there, the bench’s normalisation the identity’s.' % (
             M['rows'], K.ZERO_URL, mt.group(1) if mt else '?', M['rows'], M['yes'], M['straddles'], M['no'], M['digits'], m[0][:20], m[1],
             m[2][:20], 'yes' if RR.get('equal') else 'NO', M['slope'], ', '.join(j for j, _t, _q in M['checks']) or 'none'), '',
         '**What the bench is.** Q(t) computed from the prime side is the explicit formula’s left side evaluated at a window centred on a '
         'known zero, so a positive value is the prime side agreeing with the zero side where the zero side is known, and the bench '
         'measures that agreement’s margin -- a bench of the identity’s two sides, not a test of positivity beyond the table. It makes '
         'no statement about any zero not in the table and moves no grade.', '',
         '**The seam equivalence** (`(R237)`(2)): ch_iff_h2_sign_of_seam graded on its seam premise rh_strip_imp_rh by the seam principle '
         '-- an equivalence presented under an open seam premise is graded as its consequent is; its two old cells take dated correction '
         'entries in their documents’ forms, OPEN_TRAILS :%s (to :%d) and CORRESPONDENCE row %s (superseding row 383), each committed alone; '
         'the table reads it %s.' % (CT['line'], K.CHIFF_TRAIL, ', '.join(str(x['row']) for x in CR_['rows']), _table_grades().get(K.CHIFF)), '',
         '**The BOUNDED shape** (`(R237)`(3)): the quantifier column gains BOUNDED -- a universal quantifier whose body carries an explicit '
         'numeric bound on the quantified variable’s height, norm or index; FINITE stays for Finset and finite-range forms. relay '
         'tools/chain_page.py and its test edited after the seal (%s), the test %d of %d by its case pattern, the reader as it stood failing '
         '%s. Over both pages’ nodes %d shapes moved: %s; the height pair stays UNIVERSAL, the height an object. Both pages re-emitted. '
         'The sieve’s shape column takes the word at its next version (OPEN_TRAILS :%d).' % (
             genc, GT['passing'], GT['cases'], GT['control']['failing'], len(SH['moved']),
             ', '.join('%s %s' % (x[1].split('.')[-1], x[3]) for x in SH['moved']), rl['lines'][2]['line']), '',
         '**The closing form** (`(R237)`(4)): a closing naming the next act’s terminals prints each terminal’s statement at its pin '
         'beneath the name (OPEN_TRAILS :%d); applied from this closing, relay tools/b627_closing.py edited after the seal and committed '
         'alone (%s).' % (rl['lines'][1]['line'], clc), '',
         '**The record lines and the root.** b626’s weight at FINDINGS :%d. The root of b627 over %d repositories, %d tags and %d banks; '
         'the chain verified, %s.' % (rl['lines'][0]['line'], len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks']),
                                       ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b519’s window bench at the kernel’s own window and the kernel’s '
         'own identity, and finds the prime side reproducing the zero side at every known ordinate it was asked about; it re-reads b626’s '
         'rung and gives its bounded quantifier a word of its own; and it closes the seam node b626 printed for ruling. It strengthens the '
         'programme’s offering of a ladder whose rungs are carried at their honest grade, its numbers a bench beside the kernel and never '
         'a claim of it.', '',
         '**Next.** Per `(R237)`(6): b628, the cross-kernel discharge route (b) of W-ORD-VENDOR-FINALMULT (OPEN_TRAILS :12970) if the '
         'author’s word falls there, else W-ORD-NYMAN-BEURLING-FACE (:12893). The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds, or about any zero not in the table.*', '']
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
    put_json('b627_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) H61c’s “no page moves” read on the bench’s scope: the pages move by the clauses of `(R237)`(2)-(3) alone, every changed '
              'line printed; (2) N3’s “the rung’s nodes” read as the three whose statements carry rh_upto’s bounded quantifier, the pair '
              'and the height printed beside them; (3) BOUNDED read as a premise of the body bounding |x.im|, ‖x‖, |x| or Complex.abs x, or '
              'for ℕ and ℤ the index itself, above by a term free of x; (4) the conventions’ check at the lowest ordinate printed beside '
              'the mpmath midpoints, unscored; (5) Odlyzko’s zeros2 (the lowest 100 ordinates to over 1000 places) as the named table; (6) '
              'N5’s list read with the act’s own banks and tools as the record’s')


def _elide(text):
    """### the author's answer as banked, a sentence carrying one of the scanner's own stems (banned_terms.STEMS) elided and marked so,
    ### never reworded: the answer stands verbatim in relay data/b627_author_answers.txt."""
    import banned_terms as BT
    rx = re.compile(r'(%s)' % '|'.join(re.escape(s) for s in BT.STEMS), re.I)
    out = []
    for s in re.split(r'(?<=[.;])\s+', text):
        out.append('[a sentence elided here under the scanner’s stem rule, verbatim in the bank]' if rx.search(s) else s)
    return ' '.join(out)


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b627_scores.json', 'b627_findings.json', 'b627_record_lines.json', 'b627_act_root.json'))
    CT, CR_ = jl('b627_chiff_trail.json'), jl('b627_chiff_row.json')
    rc = _relay_commits()
    genc = (_alone(RELAY, list(K.GEN_FILES), rc) or ['?'])[0]
    clc = (_alone(RELAY, ['tools/b627_closing.py'], rc) or ['?'])[-1]
    nt = [l.strip() for l in _next_lines()]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R237) ratified.** (1) b626 at its weight. (2) ch_iff_h2_sign_of_seam on its seam, by the seam principle. (3) The BOUNDED '
             'shape. (4) The closing form. (5) W-ORD-MARGIN-BENCH, as the author answered before the seal. (6) The act after: b628.', '',
             '**Entered:** FINDINGS.md:%d (b626’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the closing form), :%d (the sieve’s item, to '
             ':%d), :%d (the seam equivalence’s correction, to :%d); this record; SIDE-global-section CORRESPONDENCE row %s; relay '
             'tools/chain_page.py and tools/test_chain_page_b596.py %s; tools/b627_closing.py’s edit %s; tools/b627_margin.py with its banks.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'], SIEVE_REC, CT['line'], K.CHIFF_TRAIL,
                 ', '.join(str(x['row']) for x in CR_['rows']), genc, clc), '',
             '**Act root:** b627 `%s` (previous `%s`, b626’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**The author’s three answers before the seal** (relay data/b627_author_answers.txt): the fit -- %s; the window -- %s; the '
             'certification -- %s.' % (_elide(answer_of(0)), _elide(answer_of(1)), _elide(answer_of(2))), '',
             '**The next act’s terminals, each statement at its pin** (`(R237)`(4)): %s.' % ' / '.join(nt), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b627_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R237)`(6), b628 -- the cross-kernel discharge route (b) of W-ORD-VENDOR-FINALMULT (:12970) if the author’s word '
             'falls there, else W-ORD-NYMAN-BEURLING-FACE (:12893); the author rules on the closing.', '',
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
    put_json('b627_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b627_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b627 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b627_defects.json -- NOTHING WRITTEN')
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
    put_json('b627_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


def desk(*a):
    S = jl('b627_scores.json')
    L = ['=' * 104, 'b627 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H61a-H61d, (R237)(5).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H61 : HOLDS %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** '
          '### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
              sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'NOT SCORABLE' for k in HKEYS),
              sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK),
              sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b627_defects.txt').rstrip(NL).split(NL)
    put_txt('b627_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b627_scores.json', 'b627_findings.json', 'b627_trail.json', 'b627_record_lines.json', 'b627_act_root.json'))
    CT, CR_, SH, M = jl('b627_chiff_trail.json'), jl('b627_chiff_row.json'), jl('b627_shapes.json'), _margin()
    L = ['b627 -- THE COMPONENTS, BANKED UNDER (R237).', '',
         '### COMPONENT 0 : the process listing ; b626`s closing push-out relay %s ; push-b626* branches deleted by name (data/b627_branches.txt) ; '
         'the suite, the answers arm counting prompts from the bank, run at HEAD before the face (data/b627_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b626`s weight FINDINGS :%d ; the closing form OPEN_TRAILS :%d ; the sieve`s item :%d ; the seam equivalence`s '
         'corrections OPEN_TRAILS :%s and CORRESPONDENCE row %s ; the closing tool`s edit data/b627_closing_edit.txt' % (
             rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], CT['line'], ', '.join(str(x['row']) for x in CR_['rows'])),
         '### COMPONENT 2 : data/b627_gen_diff.txt ; data/b627_gen_test.txt ; data/b627_shapes.txt (shapes moved %d) ; the pages '
         'data/b627_page_zeta.json, data/b627_page_chi.json ; page arms data/b627_page_arms.txt' % len(SH['moved']),
         '### COMPONENT 3 : data/b627_margin_inputs.txt (Odlyzko`s zeros2, read once)',
         '### COMPONENT 4 : data/b627_margin.txt (values %d, positive %d, minimum %s) ; data/b627_margin_rerun.json ; H61a %s, H61b %s, H61c %s, '
         'H61d %s' % (M['rows'], M['yes'], (M['min'] or ['?'])[0][:16], S['H61a'][0], S['H61b'][0], S['H61c'][0], S['H61d'][0]),
         '### COMPONENT 5 : the table ; the root %s ; the arm data/b627_root_arm.txt ; FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; '
         'next: b628 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (J['root'][:16], fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0],
                                                             S['N4'][0], S['N5'][0])]
    put_txt('b627_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b627_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
