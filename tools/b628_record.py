# -*- coding: utf-8 -*-
"""b628_record.py -- THE ACT'S RECORD TOOL, UNDER (R238). ### ONE SUBCOMMAND PER BANK.

### ### b628: LANE THREE, ACT FIFTY-FIVE -- THE 2/3 THEOREM'S AXIOM PROFILE READ IN ITS OWN KERNEL AND CITED AT two_thirds, v0.23;
### THE INTAKE FORM'S PILOT ON THE ANNEX PAPER; THE CARRIED TEST DEFECT REPAIRED.
### Subcommands write only `data/b628_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`. The data is tools/b628_worklist.py. No platform call. The case counter is (R233)(3)'s standing form.
### THE INTAKE: the full bank is written by the seat under data/ and is never staged, committed or pushed (the author's answer before
### the seal); this tool reads it, checks its form, runs the no-disclosure arm over it, and writes the SUMMARY bank, which carries
### no sentence of the paper -- refused if any six-word run of the paper appears in it.
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
import b628_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
SESSION_ID = 'f5c41941-fa74-40e9-b806-a98e7280e315'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b628_registration_2026-10-05.txt'

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
_DJ = os.path.join(D, 'b628_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b628 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b628_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: route (b), the next act`s face, the ANNEX act struck, the synthesis form and its clauses, the edition form, the '
         'precedence and authority orders, the build clause, the N5 line, b627`s corrections and record', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12228, 12354, 12356, 12566, 12595, 12601, 12699, 12799, 12893, 12970, 13028, 13030, 13032, 13035, 13057], 1500),
        ('FINDINGS: b627`s entry', PP, PRE_PP, 'FINDINGS.md', [7585, 7587], 600),
        ('REGISTRY: the ANNEX', PP, PRE_PP, 'REGISTRY.md', [360, 362, 366], 400),
        ('the census at its latest version on D:, v0.4: the ANNEX row', PP, PRE_PP, 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md', [10, 64, 71], 500),
        ('the sieve at v0.6: the verdict column and the five tests', PP, PRE_PP, 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md',
         [23, 25, 27, 29, 31, 32, 33, 34, 35, 37], 600),
        ('Zeta23 at 3635e748: the toolchain', K.FM, K.ZETA23_PIN, 'lean-toolchain', ('ALL',), 200),
        ('Zeta23 at 3635e748: the lakefile', K.FM, K.ZETA23_PIN, 'lakefile.toml', ('ALL',), 200),
        ('Zeta23 at 3635e748: the theorem', K.FM, K.ZETA23_PIN, 'Zeta23/FinalMult.lean', [12, 350, 351, 365], 300),
        ('Zeta23 at 3635e748: ThmB_statement', K.FM, K.ZETA23_PIN, 'Zeta23/Statement.lean', [183, 184, 185], 300),
        ('Zeta23 at 3635e748: the audit record (an artefact; its prints name the comparator statements)', K.FM, K.ZETA23_PIN, 'AUDIT.md',
         ('GREP', r'^Toolchain|lake build Solution\.Multiplicity|^\* Axiom audit|two_thirds_simple_on_critical_line'), 400),
        ('Zeta23 at 3635e748: the comparator`s delegation to thmB₀_mult', K.FM, K.ZETA23_PIN, 'comparator/Solution/Multiplicity.lean', [8, 20, 21, 22, 23, 24], 300),
        ('SIDE-explicit-formula v0.22: the proportion, its field, the terminal', K.KER, 'v0.22', K.CITE_FILE, [37, 38, 39, 40, 41, 45, 46, 47], 300),
        ('SIDE-explicit-formula v0.22: the audit module', K.KER, 'v0.22', K.AXCHECK_FILE, ('GREP', r'^#print axioms|^import'), 300),
        ('relay tools/chain_page.py: the backmatter channel', RELAY, PRE_RELAY, 'tools/chain_page.py', ('GREP', r'backmatter'), 300),
        ('relay tools/test_chain_page_b596.py: case (1)', RELAY, PRE_RELAY, K.TEST_FILE, ('GREP', r"\(1\) b592|def regen|^RELAY_PIN|^PRE_PP"), 300),
        ('relay data/b627_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b627_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
        ('relay data/b627_closing.txt: the next act`s terminals as b627`s closing printed them', RELAY, PRE_RELAY, 'data/b627_closing.txt',
         ('GREP', r'thmB₀_mult|SimpleProportion|exceptional_mass_le_third|NYMAN'), 300),
    ]


def reads(*a):
    L = ['b628 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
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
    doc = io.open(K.INTAKE_DOC, encoding='utf-8').read().replace(chr(13), '')
    L += ['', '### THE INTAKE`S DOCUMENT, READ AT ITS PATH (outside the repository tree; its text is not printed here): %s ; %d lines ; '
              'sha256 %s ; later versions present and not read for claims: %s' % (
                  K.INTAKE_DOC, len(lines_of(doc)), hashlib.sha256(doc.encode('utf-8')).hexdigest(), ', '.join(os.path.basename(x) for x in K.INTAKE_LATER)),
          '### the synthesis form`s pin-resolution rule: no line of the ledgers carries those words (git grep, PLACE-papers HEAD); read in '
          '(R238)(5)`s own words -- kernel-verified where and nowhere but where a terminal at a pin carries it, the terminal and pin named',
          '', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                         g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b628_reads.txt', L)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R238) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
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
    L = ['### b628 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b628_author_answers.txt', L)


def answer_of(k):
    """### the author's answer to the act's k-th prompt (0-based, across calls), whole: cut from the result after its own question's
    ### `"<question>"="` and before the next question's `", "<question>"="`, the questions read from the bank's prompt headers."""
    t = rd('b628_author_answers.txt')
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
WRITTEN_KERNS = ('SIDE-explicit-formula',)   # ### the one this act writes: the citation, on its branch and tag


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
    put_json('b628_kernels_face.json', dict(at=utc(), kernels=kern_state()))


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
    p = os.path.join(SP if DRY else D, 'b628_scanfile_%s.md' % name)
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
B627_ENTRY = 7587
W_HEAD = '*Appended 2026-10-05 by b628 to b627’s entry (:%d), under `(R238)`(1) -- b627 AT ITS WEIGHT:*'
TR_HEAD = '*Appended 2026-10-05 by b628 beneath the standing N5 line (:12799), under `(R238)`(2) -- STANDING: EVERY TEST FILE RUN AT STEP ZERO:*'
RB_HEAD = '*Appended 2026-10-05 by b628 to W-ORD-VENDOR-FINALMULT re-priced (:12970), under `(R238)`(3) -- THE WORD: BOTH; ROUTE (b) TAKEN AT b628:*'
NB_HEAD = '*Appended 2026-10-05 by b628 to W-ORD-NYMAN-BEURLING-FACE (:12893), under `(R238)`(3) and (6) -- MOVED TO b629:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry):
    pre, post = _count_bank(_rel('b627_checks.txt')), _count_bank(_rel('b627_checks_postpush.txt'))
    DJ = json.loads(_rel('b627_defects.json'))
    roots = [l.split() for l in _rel('act_roots.txt').split(NL) if l.startswith('b627 ')]
    return ('\n%s Q(t) from the prime side at the lowest 100 ordinates of Odlyzko’s zeros2 (read once, 105979 bytes, sha256 0439d90a…), '
            'python-flint Arb balls at 200 bits, the window and the prime sum exact, the archimedean term by acb.integral with the tail '
            'bound in the radius: 100 of 100 balls wholly above zero, 31 certified digits at the worst, the minimum 32.0011725882… at '
            't = 14.1347…; the second run byte for byte (27560 bytes); the mpmath midpoint at a relative 4.4e-18; the zero side summed '
            'over the table agreeing with Q in 25 printed digits at ordinate 1, the normalisation confirmed there and there alone (the '
            'entry’s every-ordinate sentence corrected at OPEN_TRAILS :13057, the seat’s (f)); the nearest-neighbour spacing beside '
            'each value and the log-log slope once, a centre line. H61a, H61c, H61d held; H61b and N2 not scorable, the fit withdrawn '
            '(W-BENCH-1, RH-59) and named from recall in `(R237)`(5), the navigator’s; N1, N3-N5 held; S1 and S3 refuted in letter on '
            'the seat’s (a) and (d), S2, S4, S5 held. The seam equivalence by the seam principle, OPEN_TRAILS :13032 and CORRESPONDENCE '
            'row 451. BOUNDED moving rh_upto, PlattTrudgianHeight and rh_upto_platt, the height pair as it was, no other node moved. '
            'The closing printing the next act’s terminal statements and saying the Nyman–Beurling face names none yet. The root %s, '
            'b624-b627 verifying. The suite %d of %d before the push and %d of %d after it by (a) and (g), each claim tested directly '
            'and holding; defects (b)-(g) the seat’s (relay data/b627_defects.txt, %d entries), (c) a recursive grep stopped with its '
            'children by PID, (g) carried by the defect bank and the closing alone. Nothing deposited; no kernel touched.\n'
            % (W_HEAD % entry, (roots[0][1][:8] + '…' + roots[0][1][-4:]) if roots else '?', pre[0], pre[1], post[0], post[1], len(DJ['defects'])))


def _test_line():
    T = jx('b628_tests_stepzero.json')
    bad = ['%s %s' % (n, x['failing'] or 'exit %d' % x['rc']) for n, x in sorted(T.items()) if x['rc'] != 0 or x['failing']]
    return ('\n%s every act runs every test file under relay tools/ at its step zero and prints the counts, each test`s cases counted '
            'by its own case pattern and its own last line printed beside them, so a failing case is found by the act after the edit '
            'that broke it and not four acts on; the bank is data/<act>_tests_stepzero.txt. Applied first at b628: %d test files run, '
            'not clean %s -- case (1) of test_chain_page_b596.py, b627’s carried defect (a), repaired by `(R238)`(2); and cases (1)-(3) '
            'of test_chain_page_b592.py, found here, carried, its generator exiting on an unresolved name in b592’s χ list, for the '
            'author’s word.\n' % (TR_HEAD.replace('`', '`'), len(T), '; '.join(bad) or 'none'))


def _both():
    return ('\n%s the author’s word between the routes fell on both acts at once: route (b), the cross-kernel discharge, taken at b628 '
            'beside W-ORD-INTAKE -- thmB₀_mult’s axiom profile read in Zeta23’s own build at 3635e748 and cited at two_thirds in '
            'v0.23, the grade unchanged; route (a), the port, stays priced and not started.\n' % RB_HEAD)


def _nb():
    return ('\n%s the face moves from the act after route (b) to b629, the opening act of its two; no kernel terminal is named for '
            'it yet, and the closing says so.\n' % NB_HEAD)


def record_lines(*a):
    """### FINDINGS: b627's weight (to its entry :7587). OPEN_TRAILS: the test-run standing line (beneath :12799), the word at :12970
    ### and at :12893. No line makes a table cell (predicted)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The positivity margin at height: the v0.20 window')
    if entry != B627_ENTRY:
        sys.exit('### b627`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % entry, _weight(entry)), ('OPEN_TRAILS.md', TR_HEAD, _test_line()),
             ('OPEN_TRAILS.md', RB_HEAD, _both()), ('OPEN_TRAILS.md', NB_HEAD, _nb())]
    cells, nd, clean = _guarded(items, 'OPEN_TRAILS.md', 'lines')
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    _land(Q, items, 'b628_record_lines.json', entry)


# ================================================================================ COMPONENT 1: THE TEST REPAIR
CONTROL_FMT = '### THE POSITIVE CONTROL: the same test with %s as it stood at relay %s (exit %d): cases %d, passing %d, failing %s'
CONTROL_RE = r'^### THE POSITIVE CONTROL: the same test with tools/test_chain_page_b596\.py as it stood at relay (\w+) \(exit (\d+)\): cases (\d+), passing (\d+), failing (.*)$'


def test_repair(*a):
    """### (R238)(2): the test as repaired run and counted by its case pattern, the repaired case named; its diff against PRE_RELAY;
    ### the control: the test as it stood (its blob at PRE_RELAY) failing the repaired case (data/b628_test_repair.txt and .json)."""
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    test = os.path.join(ROOT, *K.TEST_FILE.split('/'))
    r = subprocess.run([sys.executable, test], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    old = os.path.join(SP, '_b628_test_old.py')                       # ### the blob at PRE_RELAY, in the scratchpad, run as if in tools/
    _write(old, _show(RELAY, PRE_RELAY, K.TEST_FILE).encode('utf-8'))
    runner = ('import sys; src = open(%r, encoding="utf-8").read(); g = {"__name__": "__main__", "__file__": %r}; '
              'exec(compile(src, "test@%s", "exec"), g)' % (old, test, PRE_RELAY))
    r2 = subprocess.run([sys.executable, '-c', runner], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    out2 = (r2.stdout or '') + (r2.stderr or '')
    n2, p2 = count_cases(out2)
    failed2 = [re.match(r'^  (\(\d+\))', l).group(1) for l in out2.split(NL) if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]
    case = [l for l in out.split(NL) if l.startswith('  ' + K.TEST_CASE + ' ')]
    d = g(RELAY, 'diff', PRE_RELAY, '--', K.TEST_FILE)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', K.TEST_FILE).rstrip(NL).split(NL)[-1].strip()
    L = ['b628 -- COMPONENT 1, (R238)(2): %s REPAIRED, RUN AND COUNTED (%s); exit %d' % (K.TEST_FILE, utc(), r.returncode), '',
         '### ' + (st or 'NO DIFF'), ''] + d.rstrip(NL).split(NL) + ['', '### THE RUN:'] + out.rstrip(NL).split(NL)
    L += ['', '### THE REPAIRED CASE: %s' % (case[0].strip() if case else '### NOT PRINTED'),
          '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p), '',
          CONTROL_FMT % (K.TEST_FILE, PRE_RELAY, r2.returncode, n2, p2, failed2)]
    put_txt('b628_test_repair.txt', L)
    put_json('b628_test_repair.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, case=case[0].strip() if case else None, stat=st,
                                           control=dict(rc=r2.returncode, cases=n2, passing=p2, failing=failed2)))
    print(L[-3])
    print(L[-1])


# ================================================================================ COMPONENT 2: ZETA23'S PRINT
def zeta23_artefact(*a):
    """### the repository at the pin read for an axiom artefact or a build cache for FinalMult: every tracked file whose name says
    ### audit, axiom or print, the audit record's lines on the multiplicity statements, the comparator's delegation, and whether a
    ### build tree for FinalMult exists beside the clone; one ls-remote of the upstream (data/b628_zeta23_artefact.txt and .json)."""
    files = [x for x in g(K.FM, 'ls-tree', '-r', '--name-only', K.ZETA23_PIN).split(NL) if re.search(r'(?i)audit|axiom|print', x)]
    audit = lines_of(_show(K.FM, K.ZETA23_PIN, 'AUDIT.md') or '')
    deleg = lines_of(_show(K.FM, K.ZETA23_PIN, 'comparator/Solution/Multiplicity.lean') or '')
    named = [i + 1 for i, l in enumerate(audit) if 'thmB₀_mult' in l or 'ThmB_statement' in l]
    multi = [(i + 1, l) for i, l in enumerate(audit) if 'two_thirds_simple_on_critical_line' in l]
    olean = [p for p in (os.path.join(K.FM, '.lake', 'build', 'lib', 'lean', 'Zeta23', 'FinalMult.olean'),
                         os.path.join(K.ZETA23_CLONE, '.lake', 'build', 'lib', 'lean', 'Zeta23', 'FinalMult.olean')) if os.path.exists(p)]
    rem = g(K.FM, 'ls-remote', 'origin', 'refs/tags/v1.0^{}', 'refs/tags/v1.0')
    peel = [l.split('\t')[0] for l in rem.split(NL) if l.endswith('^{}')]
    L = ['b628 -- COMPONENT 2, (R238)(4): THE UPSTREAM READ AT ITS PIN FOR AN AXIOM ARTEFACT OR A BUILD CACHE FOR FinalMult (%s)' % utc(), '',
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
    put_txt('b628_zeta23_artefact.txt', L)
    put_json('b628_zeta23_artefact.json', dict(at=utc(), files=files, named=named, multi=[x[0] for x in multi], olean=olean,
                                               peel=peel[0] if peel else None, pin=K.ZETA23_PIN_FULL))
    print(L[-1])


def _logs(prefix):
    return sorted((f for f in os.listdir(SP) if re.match(r'%s_\d+\.log$' % prefix, f)), key=lambda f: int(re.findall(r'_(\d+)\.log$', f)[0]))


def build_bank(prefix, name, *a):
    """### the detached build calls' watchdog logs (scratchpad <prefix>_<n>.log), banked: data/<name>.txt and .json."""
    calls = []
    L = ['b628 -- THE DETACHED BUILD CALLS AT THE HOLD, %s (%s), one target per call, watched from the foreground' % (prefix, utc()), '']
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
    ### SHA, the toolchain and Mathlib; the bank's own sha256 in data/b628_zeta23_axioms.json (a file cannot carry its own digest)."""
    t = io.open(log, encoding='utf-8', errors='replace').read()
    pr = _parse_prints(t)
    head = g(K.ZETA23_CLONE, 'rev-parse', 'HEAD').strip()
    tc = (io.open(os.path.join(K.ZETA23_CLONE, 'lean-toolchain'), encoding='utf-8').read().strip() if os.path.exists(os.path.join(K.ZETA23_CLONE, 'lean-toolchain')) else '?')
    AJ = jx('b628_zeta23_artefact.json')
    L = ['b628 -- COMPONENT 2, (R238)(4): #print axioms ON thmB₀_mult AND ThmB_statement IN ZETA23`S OWN BUILD', '',
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
    b = put_txt('b628_zeta23_axioms.txt', L)
    put_json('b628_zeta23_axioms.json', dict(at=utc(), head=head, pin=K.ZETA23_PIN_FULL, toolchain=tc, mathlib=K.ZETA23_MATHLIB, prints=pr,
                                             beyond=beyond, sorry='sorryAx' in t, missing=[n for n in want if n not in got],
                                             bank_sha256=hashlib.sha256(b).hexdigest()))
    print(L[-1])
    print('  the bank`s sha256: %s' % hashlib.sha256(b).hexdigest())


# ================================================================================ COMPONENT 3: THE CITATION
def cite_diff(*a):
    """### the docstring on the citation branch against v0.22: the diff, every changed line, and the statement lines -- every line of
    ### the file outside a comment or docstring -- equal before and after (data/b628_cite_diff.txt and .json)."""
    def code(t):
        t = re.sub(r'/-.*?-/', '', t, flags=re.S)
        return [l.rstrip() for l in re.sub(r'--[^\n]*', '', t).split(NL) if l.strip()]
    old = _show(K.KER, 'v0.22', K.CITE_FILE) or ''
    new = _show(K.KER, K.CITE_BRANCH, K.CITE_FILE) or ''
    d = g(K.KER, 'diff', 'v0.22', K.CITE_BRANCH, '--', K.CITE_FILE)
    files = sorted(x for x in g(K.KER, 'diff', '--name-only', 'v0.22', K.CITE_BRANCH).split(NL) if x.strip())
    same = code(old) == code(new)
    L = ['b628 -- COMPONENT 3: THE DOCSTRING AT two_thirds, %s AGAINST v0.22 (%s)' % (K.CITE_BRANCH, utc()), '',
         '### files changed: %s ; the statement lines (comments and docstrings stripped) equal before and after: %s ; the words "%s" '
         'present: %s' % (files, same, K.CITE_WORDS, K.CITE_WORDS in new), ''] + d.rstrip(NL).split(NL)
    put_txt('b628_cite_diff.txt', L)
    put_json('b628_cite_diff.json', dict(at=utc(), files=files, statements_equal=same, words=K.CITE_WORDS in new,
                                         axioms_sha=jx('b628_zeta23_axioms.json').get('bank_sha256'),
                                         sha_in_docstring=(jx('b628_zeta23_axioms.json').get('bank_sha256') or '#') in new))
    print(L[2])


def prints(log_old, log_new, *a):
    """### the audit module's prints at v0.22 and at the citation branch, compared line by line (data/b628_prints.txt and .json)."""
    def pl(p):
        t = io.open(p, encoding='utf-8', errors='replace').read()
        return [l.strip() for l in t.split(NL) if 'depends on axioms' in l or 'does not depend' in l], 'sorryAx' in t
    a_, sa = pl(log_old)
    b_, sb = pl(log_new)
    L = ['b628 -- COMPONENT 3: THE AUDIT MODULE`S PRINTS, v0.22 AGAINST v0.23, LINE BY LINE (%s)' % utc(), '']
    for i in range(max(len(a_), len(b_))):
        x, y = (a_[i] if i < len(a_) else '### NONE'), (b_[i] if i < len(b_) else '### NONE')
        L.append('  %s %s' % ('SAME' if x == y else '### DIFFERS', x if x == y else '%s  ||  %s' % (x, y)))
    L += ['', '### ### **LINES v0.22 %d ; v0.23 %d ; EQUAL LINE FOR LINE %s ; sorryAx %s / %s.**' % (len(a_), len(b_), a_ == b_ and bool(a_), sa, sb)]
    put_txt('b628_prints.txt', L)
    put_json('b628_prints.json', dict(at=utc(), old=a_, new=b_, equal=a_ == b_ and bool(a_), sorry=[sa, sb]))
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
    """### the full bank (data/b628_intake_crank_v0_5.txt, the seat's, untracked) read and checked: each claim one grade of the form's
    ### vocabulary, one cluster of the census's rows, a kernel-verified grade only with a terminal and a pin that resolve, a route read
    ### through the five tests, every claim below kernel-verified carrying a work-order line or a reason; the no-disclosure arm over
    ### the whole bank; the summary written with no six-word run of the paper in it (data/b628_intake_summary.txt and .json)."""
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
    S = ['b628 -- COMPONENT 4, (R238)(5): THE INTAKE PILOT`S SUMMARY BANK (%s). ### NO SENTENCE OF THE PAPER IS IN THIS BANK.' % utc(), '',
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


# ================================================================================ COMPONENT 5: THE PAGES, THE TABLE, THE ROOT
def nodes_new(*a):
    """### the ζ node list at v0.23: b626's list (every record line unchanged), the pin moved to v0.23, one backmatter record naming
    ### exceptional_mass_le_third's citation (data/b628_nodes_zeta.txt)."""
    src = rd(K.NODES['zeta']).rstrip(NL).split(NL)
    if '# pin: v0.22' not in src:
        sys.exit('### b626`S LIST CARRIES NO `# pin: v0.22` LINE -- NOTHING WRITTEN')
    AJ = jl('b628_zeta23_axioms.json')
    head = ['# b628 -- THE ζ NODE LIST AT v0.23, (R238)(4): b626`s list (relay data/b626_nodes_zeta.txt, every record line unchanged), the',
            '# pin moved to v0.23; one backmatter record for exceptional_mass_le_third`s citation. Every cell is elaborated by the',
            '# generator`s probe at the pin, never typed here.', '#']
    body = [('# pin: v0.23' if l == '# pin: v0.22' else l) for l in src]
    bm = ('# backmatter: exceptional_mass_le_third (SIDE-explicit-formula v0.23, Simplicity.lean) stays INTERFACES on two_thirds: its '
          'premise is Zeta23.thmB₀_mult at formal-math %s, printed at %s in that kernel`s own build under %s (relay '
          'data/b628_zeta23_axioms.txt, sha256 %s) -- %s; a theorem in another kernel`s build is a citation here until it compiles here.' % (
              K.ZETA23_PIN, ', '.join(sorted(set(x for p in AJ['prints'] if p['name'] == 'Zeta23.thmB₀_mult' for x in p['axioms']))) or 'no axioms',
              AJ['toolchain'], AJ['bank_sha256'], K.CITE_WORDS))
    put_txt(K.NEW_NODES_ZETA, head + body + [bm])


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
    put_json('b628_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, tier_cells_moved=tmoved, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s ; tier cells moved %s' % (
        k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE', tmoved or 'NONE'))
    for x in dl[:24]:
        print('    ' + x[:240])


def page_new(*a):
    """### ONE call in the foreground: the ζ page at v0.23 from the new list by a fresh probe (the checkout at v0.23, free memory
    ### above the hold); the probe's output banked as data/b628_probe_out.txt; the page written where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    pd = os.path.join(SP, '_b628_probe')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NEW_NODES_ZETA), pd, None)
    secs = int(time.time() - t0)
    po = os.path.join(pd, 'chain_page_probe_out.txt')
    if os.path.exists(po) and not DRY:
        _write(os.path.join(D, K.NEW_PROBE_ZETA), open(po, 'rb').read().replace(b'\r\n', b'\n'))
    if rc:
        put_json('b628_page_zeta.json', dict(rc=rc, log=log, at=utc(), seconds=secs))
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
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b628_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b628_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    _page_write(k, pg, fm, secs, rc)


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b628 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        nl, pr = zlist() if k == 'zeta' else (K.NODES[k], K.PROBE[k])
        r = GCP.arm(os.path.join(D, nl), os.path.join(SP, '_b628_gcp'), os.path.join(D, pr))
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
    put_txt('b628_page_arms.txt', L)
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
    L = ['b628 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(ch)),
         '### the rows changed, with the grade each now reads:']
    L += ['  %-62s %s' % (n, tg.get(n)) for n in ch] or ['  NONE']
    L += ['### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
          '### ### **THE GRADE COLUMN`S DIFF, THE TABLE BEFORE THIS RUN AGAINST AFTER IT : %s.**' % ('; '.join('%s %s -> %s' % (
              n.split('.')[-1], before.get(n), tg.get(n)) for n in gmoved) or 'EMPTY')]
    name = 'b628_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 changed=ch, grade_moved=gmoved, files_moved=moved))
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b628_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b628_') and os.path.isfile(os.path.join(D, f))
                  and not ROOT_EXCLUDE.match(f) and f != K.INTAKE_LOCAL)


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b628'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import act_root as AR
    res = AR.verify()
    J = jl('b628_act_root.json')
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
    L = ['b628 -- COMPONENT 5: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s) ; '
              'the copy`s root differs %s' % (bank, r2, same, J['root'], r2 != J['root']),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b628_root_arm.txt', L)
    put_json('b628_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H62a', 'H62b', 'H62c', 'H62d', 'H62e', 'H62f')
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
    """### every .lean file changed in the explicit-formula kernel since v0.22, its code lines (comments and docstrings stripped) before
    ### and after: the files whose code differs."""
    out = []
    for f in [x for x in g(K.KER, 'diff', '--name-only', K.PRE_KER, 'main').split(NL) if x.strip().endswith('.lean')]:
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
    face = jl('b628_kernels_face.json')['kernels']
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
                              if x.strip() and not os.path.basename(x).startswith(('b628_', 'audit_b628_', 'terminal_table'))
                              and x != 'data/b627_closing_push_out.txt'))
    beyond = [x for x in relay_beyond if x not in {K.TEST_FILE, 'data/act_roots.txt'}]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', 'data/' + K.INTAKE_LOCAL).strip())
    ok = others_ok and st == 0 and not stl and ker_files in ([], [K.CITE_FILE]) and pp_ch == want_pp and not beyond and rec_ok and not tracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; the kernels this act does not write unmoved %s; sorry tokens on the explicit-formula main %d (comments stripped); '
            'files whose code lines changed since v0.22 %s; the explicit-formula kernel`s files changed %s; PLACE-papers %s; %s; relay beyond '
            'the list: %s; the full intake bank in any relay commit %s; nothing written to the ANNEX, the census or a synthesis' % (
                others_ok, st, stl or 'NONE', ker_files or 'NONE', pp_ch, rec_state, beyond or 'NONE', tracked_local))


def scores(*a):
    ZA, PR, CD, TR, IS = jx('b628_zeta23_axioms.json'), jx('b628_prints.json'), jx('b628_cite_diff.json'), jx('b628_test_repair.json'), jx('b628_intake_summary.json')
    PZ, PX, RA, TF = jx('b628_page_zeta.json'), jx('b628_page_chi.json'), jx('b628_root_arm.json'), jx('b628_table_final.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    thm = [p for p in ZA.get('prints') or [] if p['name'] == 'Zeta23.thmB₀_mult']
    h62a = bool(thm) and not (set(thm[0]['axioms']) - STD) and not ZA.get('sorry')
    moved = (PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or [])
    tmoved = (PZ.get('tier_cells_moved') or []) + (PX.get('tier_cells_moved') or [])
    nclaims = IS.get('claims') or 0
    stmt = len(IS.get('statement') or [])
    ver = RA.get('verify') or []
    tag = g(K.KER, 'rev-parse', '--short=7', K.CITE_TAG + '^{commit}').strip()
    S = {
        'H62a': (('HOLDS' if h62a else 'REFUTED'), 'thmB₀_mult reads %s in Zeta23`s own build at %s under %s; sorryAx %s' % (
            thm[0]['axioms'] if thm else 'NOT PRINTED', (ZA.get('head') or '?')[:8], ZA.get('toolchain'), ZA.get('sorry'))),
        'H62b': (('HOLDS' if CD.get('statements_equal') and PR.get('equal') else 'REFUTED'), 'the code lines equal before and after %s; the audit '
                 'module`s prints equal line for line %s (%d lines)' % (CD.get('statements_equal'), PR.get('equal'), len(PR.get('new') or []))),
        'H62c': (('HOLDS' if not moved and TF.get('grade_moved') == [] else 'REFUTED'), 'page grade cells moved %s; tier cells moved %s; the table`s '
                 'grade column %s' % (moved or 'NONE', tmoved or 'NONE', TF.get('grade_moved'))),
        'H62d': (('HOLDS' if IS.get('kv') else 'REFUTED'), 'kernel-verified claims %s' % (IS.get('kv') or 'NONE')),
        'H62e': (('HOLDS' if nclaims and IS.get('claim_lines') == nclaims and not IS.get('malformed') else 'REFUTED'),
                 'claims %d, claim lines %s, malformed %s' % (nclaims, IS.get('claim_lines'), IS.get('malformed') or 'NONE')),
        'H62f': (('HOLDS' if IS.get('nd') is not None and not any((IS.get('nd') or {}).values()) else 'REFUTED'), 'the arm over the full bank %s' % IS.get('nd')),
        'N1': (('HELD' if h62a else 'REFUTED'), 'thmB₀_mult %s, no HOLD fired' % (thm[0]['axioms'] if thm else 'NOT PRINTED')),
        'N2': (('HELD' if PR.get('equal') else 'REFUTED'), 'v0.23`s audit lines equal v0.22`s line for line %s' % PR.get('equal')),
        'N3': (('HELD' if not moved else 'REFUTED'), 'grade cells moved on either page %s' % (moved or 'NONE')),
        'N4': (('HELD' if IS.get('kv') and nclaims and stmt * 3 <= nclaims else 'REFUTED'), 'kernel-verified %d; statement-grade %d of %d' % (
            len(IS.get('kv') or []), stmt, nclaims)),
        'N5': n5v,
        'S1': (('HELD' if TR.get('cases') and TR.get('cases') == TR.get('passing') and (TR.get('control') or {}).get('failing') == [K.TEST_CASE]
                and len(_alone(RELAY, [K.TEST_FILE], _relay_commits())) == 1 else 'REFUTED'),
               'the test %s of %s; the test as it stood fails %s; committed alone %s' % (TR.get('passing'), TR.get('cases'),
                                                                                       (TR.get('control') or {}).get('failing'), _alone(RELAY, [K.TEST_FILE], _relay_commits()))),
        'S2': (('HELD' if ZA.get('head') == K.ZETA23_PIN_FULL and not ZA.get('missing') else 'REFUTED'), 'the clone at %s; names not printed %s' % (
            (ZA.get('head') or '?')[:12], ZA.get('missing'))),
        'S3': (('HELD' if CD.get('files') == [K.CITE_FILE] and CD.get('words') and CD.get('sha_in_docstring') and tag else 'REFUTED'),
               'files changed %s; the words present %s; the bank`s sha256 in the docstring %s; v0.23 at %s' % (
                   CD.get('files'), CD.get('words'), CD.get('sha_in_docstring'), tag or 'NONE')),
        'S4': (('HELD' if not tmoved and not moved else 'REFUTED'), 'tier cells moved %s' % (tmoved or 'NONE')),
        'S5': (('HELD' if ver and all(v[1] == 'AGREE' for v in ver) and [v[0] for v in ver] == ['b624', 'b625', 'b626', 'b627', 'b628'] else 'REFUTED'),
               'the chain %s' % [(v[0], v[1]) for v in ver]),
    }
    put_json('b628_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b628 — lane three, act fifty-five under (R238): the 2/3 theorem’s axiom profile read in its own kernel and cited '
              'at two_thirds, v0.23; the intake form’s pilot on the ANNEX paper; the carried test defect repaired')


def _title_entry():
    IS = jx('b628_intake_summary.json')
    return ('## thmB₀_mult’s axiom profile in Zeta23’s build at 3635e748, cited at two_thirds in v0.23, the grade INTERFACES unchanged; '
            'the intake pilot on the ANNEX paper: %d claims, %d kernel-verified, %d work-orders; the carried test defect repaired' % (
                IS.get('claims') or 0, len(IS.get('kv') or []), IS.get('workorders') or 0))


def _finding_text():
    S, rl, ZA, PR, CD, TR = (jl(n) for n in ('b628_scores.json', 'b628_record_lines.json', 'b628_zeta23_axioms.json', 'b628_prints.json',
                                             'b628_cite_diff.json', 'b628_test_repair.json'))
    IS, J, RA, ZB = jl('b628_intake_summary.json'), jl('b628_act_root.json'), jl('b628_root_arm.json'), jx('b628_zeta23_build.json')
    thm = [p for p in ZA['prints'] if p['name'] == 'Zeta23.thmB₀_mult']
    tag = g(K.KER, 'rev-parse', '--short=7', K.CITE_TAG + '^{commit}').strip()
    t = _title_entry()
    e = ['', t, '',
         '*Filed at b628 on the author’s ruling `(R238)` and the author’s two answers before the seal. Banks: relay `data/b628_zeta23_artefact.txt`, '
         '`data/b628_zeta23_build.txt`, `data/b628_zeta23_axioms.txt`, `data/b628_cite_diff.txt`, `data/b628_prints.txt`, `data/b628_intake_summary.txt`, '
         '`data/b628_test_repair.txt`, `data/b628_tests_stepzero.txt`, `data/b628_table_final.txt`, `data/b628_act_root.txt`, '
         '`data/b628_author_answers.txt`. Nothing deposits.*', '',
         '**Route (b)** (`(R238)`(4), OPEN_TRAILS :12970): the upstream at its pin carries an audit record, AUDIT.md, printing the '
         'comparator statement that delegates to thmB₀_mult at the standard three, and no print of thmB₀_mult or ThmB_statement by '
         'name, and no build cache for FinalMult; so the module was built in a clone at the pin (%s, %d calls detached at the hold, %d s '
         'in all) under %s with Mathlib 51e6992e, and the two names printed there: thmB₀_mult %s, sorryAx %s (relay '
         'data/b628_zeta23_axioms.txt, sha256 %s). SIDE-explicit-formula v0.23 = %s adds a docstring to SimpleProportion’s two_thirds '
         'field naming the theorem, the repository, the pin, the toolchain and that sha256 -- “%s” -- and changes no statement: the code '
         'lines equal before and after, the audit module’s %d prints equal line for line. exceptional_mass_le_third stays INTERFACES on '
         'two_thirds: a theorem in another kernel’s build is a citation here until it compiles here. H62a %s, H62b %s, H62c %s.' % (
             K.ZETA23_CLONE, len(ZB.get('calls') or []), sum(c.get('secs') or 0 for c in ZB.get('calls') or []), ZA['toolchain'],
             thm[0]['axioms'] if thm else 'not printed', 'present' if ZA['sorry'] else 'absent', ZA['bank_sha256'], tag, K.CITE_WORDS,
             len(PR['new']), S['H62a'][0], S['H62b'][0], S['H62c'][0]), '',
         '**The intake pilot** (`(R238)`(5), W-ORD-INTAKE): one document in, by the synthesis form’s rules without an edition -- the '
         'ANNEX’s paper the census names (row R22; REGISTRY :366), filed there non-keystone and not for publication, so the full bank '
         'stays local and untracked and the relay carries its summary and digest (data/b628_intake_summary.txt; the full bank’s sha256 '
         '%s), by the author’s answer before the seal. %d claims, each with one grade of the form’s vocabulary and one cluster of the '
         'census’s rows: %s; kernel-verified %s; %d routes read through the sieve’s five tests; %d work-order lines; the no-disclosure '
         'arm over the full bank %s. H62d %s, H62e %s, H62f %s. The pilot is the form’s test on one document and certifies nothing the '
         'document does not.' % (
             IS['local_sha256'], IS['claims'], '; '.join('%s %d' % (k, v) for k, v in IS['grades'].items() if v),
             ', '.join(IS['kv']) or 'none', sum(1 for r in IS['rows'] if r['route'] == 'yes'), IS['workorders'], IS['nd'],
             S['H62d'][0], S['H62e'][0], S['H62f'][0]), '',
         '**The carried test defect** (`(R238)`(2)): case (1) of tools/test_chain_page_b596.py loads the E0 rule at the test’s own pin; '
         'the test %d of %d by its case pattern, the test as it stood failing %s; committed alone. Every test file under tools/ ran at '
         'step zero (data/b628_tests_stepzero.txt): the standing line entered beneath :12799 (OPEN_TRAILS :%d).' % (
             TR['passing'], TR['cases'], TR['control']['failing'], rl['lines'][1]['line']), '',
         '**The record lines and the root.** b627’s weight at FINDINGS :%d; the word at :12970 (OPEN_TRAILS :%d) and :12893 (:%d). '
         'The root of b628 over %d repositories, %d tags and %d banks; the chain verified, %s.' % (
             rl['lines'][0]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'], len(J['reads']['heads']), len(J['reads']['tags']),
             len(J['reads']['banks']), ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b596’s named premise and b625’s re-pricing, and gives '
         'SimpleProportion’s field the source kernel’s own print beside it, the grade where b596 set it; it re-reads the census’s '
         'ANNEX row (b619) and b611’s striking of the ANNEX act, and runs the synthesis form on the one document the sequence could not '
         'reach, without writing a synthesis. It strengthens the programme’s offering of a ladder whose rungs are carried at their '
         'honest grade, a source kernel’s theorem cited where it holds and never claimed where it does not compile.', '',
         '**Next.** Per `(R238)`(6): b629, W-ORD-NYMAN-BEURLING-FACE (OPEN_TRAILS :12893), the opening act of its two; no kernel terminal is '
         'named for it yet. The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds, or that the 2/3 theorem compiles in this kernel.*', '']
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
    put_json('b628_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) the upstream`s AUDIT.md read as an artefact that does not carry the ruling`s print by name, so the module built; (2) '
              'the ζ page`s backmatter line as the node`s citation, the generator`s channel being the list`s; (3) the census at its '
              'latest version on D: naming v0_5, the later versions not read for claims; (4) the intake`s claims read one per assertion '
              'the paper makes in its own voice, a citation it reports read as the cited work`s and not counted; (5) the summary refused '
              'on any six-word run of the paper; (6) test_chain_page_b592.py`s cases (1)-(3), found failing at step zero, carried')


def _next_lines():
    return ['W-ORD-NYMAN-BEURLING-FACE (OPEN_TRAILS :12893) names no kernel terminal yet; its statements are b629`s to write, priced at the work-order']


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b628_scores.json', 'b628_findings.json', 'b628_record_lines.json', 'b628_act_root.json'))
    rc = _relay_commits()
    tst = (_alone(RELAY, [K.TEST_FILE], rc) or ['?'])[0]
    tag = g(K.KER, 'rev-parse', '--short=7', K.CITE_TAG + '^{commit}').strip()
    rows_ = ['', TRAIL_HEAD, '',
             '**(R238) ratified.** (1) b627 at its weight. (2) The carried test defect repaired and the step-zero test line. (3) The word: '
             'both. (4) Route (b). (5) W-ORD-INTAKE, the pilot. (6) The act after: b629.', '',
             '**Entered:** FINDINGS.md:%d (b627’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the standing test line, beneath :12799), :%d '
             '(the word, to :12970), :%d (to :12893); this record; relay tools/test_chain_page_b596.py %s; SIDE-explicit-formula v0.23 = %s; '
             'relay data/%s.' % (rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                                 tst, tag, K.INTAKE_SUMMARY), '',
             '**Act root:** b628 `%s` (previous `%s`, b627’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**The author’s answers before the seal** (relay data/b628_author_answers.txt): the intake bank -- %s; the version -- %s.' % (
                 _elide(answer_of(0)), _elide(answer_of(1))), '',
             '**The next act’s terminals, each statement at its pin** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b628_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R238)`(6), b629, W-ORD-NYMAN-BEURLING-FACE (:12893), the opening act of its two; the author rules on the closing.', '',
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
    put_json('b628_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b628_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b628 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b628_defects.json -- NOTHING WRITTEN')
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
    put_json('b628_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


def desk(*a):
    S = jl('b628_scores.json')
    L = ['=' * 104, 'b628 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H62a-H62f, (R238)(4)-(5).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H62 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b628_defects.txt').rstrip(NL).split(NL)
    put_txt('b628_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b628_scores.json', 'b628_findings.json', 'b628_trail.json', 'b628_record_lines.json', 'b628_act_root.json'))
    IS = jl('b628_intake_summary.json')
    L = ['b628 -- THE COMPONENTS, BANKED UNDER (R238).', '',
         '### COMPONENT 0 : the process listing ; b627`s closing push-out relay %s ; push-b627* branches deleted by name (data/b628_branches.txt) ; '
         'every test file under tools/ run (data/b628_tests_stepzero.txt) ; the suite, b627`s defects` sources repaired, run at HEAD before the '
         'face (data/b628_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b627`s weight FINDINGS :%d ; the test line OPEN_TRAILS :%d ; the word :%d, :%d ; the test repair data/b628_test_repair.txt' % (
             tuple(x['line'] for x in rl['lines'])),
         '### COMPONENT 2 : data/b628_zeta23_artefact.txt ; data/b628_zeta23_build.txt ; data/b628_zeta23_axioms.txt ; H62a %s' % S['H62a'][0],
         '### COMPONENT 3 : data/b628_cite_diff.txt ; data/b628_build.txt ; data/b628_prints.txt ; v0.23 ; H62b %s' % S['H62b'][0],
         '### COMPONENT 4 : data/%s (claims %d, kernel-verified %d, work-orders %d) ; the full bank local, untracked ; H62d %s, H62e %s, H62f %s' % (
             K.INTAKE_SUMMARY, IS['claims'], len(IS['kv']), IS['workorders'], S['H62d'][0], S['H62e'][0], S['H62f'][0]),
         '### COMPONENT 5 : the ζ page at v0.23 (data/b628_page_zeta.json, data/b628_nodes_zeta.txt, data/b628_probe_out.txt) ; the table ; page arms '
         'data/b628_page_arms.txt ; the root %s ; the arm data/b628_root_arm.txt ; H62c %s' % (J['root'][:16], S['H62c'][0]),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b629 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b628_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b628_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
