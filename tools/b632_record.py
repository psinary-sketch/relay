# -*- coding: utf-8 -*-
"""b632_record.py -- THE ACT'S RECORD TOOL, UNDER (R242). ### ONE SUBCOMMAND PER BANK.

### ### b632: LANE THREE, ACT FIFTY-NINE -- THE E0 RULE'S GRADES APPLIED TO THE UNGRADED TERMINAL ROWS WITH PROVENANCE, A SECOND
### READER ON SIXTY BEFORE THE PUSH; THE PUBLIC PAGE'S APOSTROPHES, THE RECORD TOOL'S WRITER AND THE b596 CASE (9) REPAIRED.
### Subcommands write only `data/b632_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`. The data is tools/b632_worklist.py. No platform is called and no registry is read. The case counter is
### (R233)(3)'s. b628's full intake bank (relay data/b628_intake_crank_v0_5.txt) is never read here, never staged or committed.
### Carried from b631's sealed tool (relay 50fc6208, by substitution), its findings writer restored at step zero (relay 66dfb8ca);
### the act's own parts written here.
"""
import collections
import copy
import difflib
import hashlib
import io
import json
import os
import random
import re
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b632_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/89dd14e7-e119-4cf8-b592-ceaac809eff2/scratchpad'
SESSION_ID = '89dd14e7-e119-4cf8-b592-ceaac809eff2'
PROJECTS = 'C:/Users/echo chamber/.claude/projects'
SESSION = '%s/D--/%s.jsonl' % (PROJECTS, SESSION_ID)
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b632_registration_2026-10-06.txt'

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
    os.makedirs(os.path.dirname(p), exist_ok=True)
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
_DJ = os.path.join(D, 'b632_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b632 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b632_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


def input_digest():
    """### b630's rule-readings bank by its blob at the commit that wrote it: (sha256 of the blob, the blob id)."""
    b = subprocess.run(['git', '-C', RELAY, 'show', '%s:%s' % (K.INPUT_REV, K.INPUT_BANK)], capture_output=True).stdout
    return hashlib.sha256(b).hexdigest(), g(RELAY, 'rev-parse', '%s:%s' % (K.INPUT_REV, K.INPUT_BANK)).strip(), b


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the edition form, the second-reader form and its two amendments, the precedence and authority orders, the build '
         'clause, the N5 line, b626`s seam entry, W-ORD-TABLE-RULE-GRADES, b631`s lines, its build route, record and correction',
         PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12212, 12228, 12354, 12356, 12799, 12839, 12863, 12994, 13133, 13159, 13161, 13163, 13165,
                                        13167, 13169, 13191], 1500),
        ('FINDINGS: b631`s weight of b630 and b631`s entry', PP, PRE_PP, 'FINDINGS.md', [7677, 7679], 600),
        ('relay data/b630_table_rule_readings.txt, the input bank: its head', RELAY, K.INPUT_REV, K.INPUT_BANK, [1, 2, 3, 4, 5, 6, 7, 8], 600),
        ('relay tools/terminal_table.py: the provenance column, its rule reading and its writer', RELAY, PRE_RELAY, 'tools/terminal_table.py',
         ('GREP', r'^(RULE_BASELINE|_DECL_KW|def (rule_reading|baseline_keys|provenance|emit|main)\b)|differ = provenance\(|\| provenance \|'), 300),
        ('relay tools/e0_rule.py: the shared rule after 576891c5, its clauses and its grade', RELAY, PRE_RELAY, 'tools/e0_rule.py',
         ('GREP', r'^(RULE_TEXT|DOMAIN|SPLITS|BINDER|SEAMS|DATA_TYPE|def (grade|domain_case|data_binder|seam_antecedents|statement_only))\b'), 300),
        ('relay data/b620_reader_prompt.txt: the packet form', RELAY, PRE_RELAY, 'data/b620_reader_prompt.txt', ('ALL',), 400),
        ('relay data/b620_key.txt: the key form', RELAY, PRE_RELAY, 'data/b620_key.txt', [1, 2, 3, 4, 5], 300),
        ('relay tools/b630_record.py: the findings writer, b630`s', RELAY, PRE_RELAY, 'tools/b630_record.py', ('GREP', r'^def (findings|trail|_finding_text)\b'), 200),
        ('relay tools/b631_record.py at its sealed commit: the writer absent', RELAY, PRE_RELAY, 'tools/b631_record.py', ('GREP', r'^def (findings|trail|_finding_text)\b'), 200),
        ('relay tools/test_chain_page_b596.py: case (9)', RELAY, PRE_RELAY, 'tools/test_chain_page_b596.py', list(range(174, 190)), 300),
        ('relay data/b631_nodes_chi.txt: the χ list`s backmatter record (the probe text)', RELAY, PRE_RELAY, 'data/b631_nodes_chi.txt', ('GREP', r'^# backmatter: '), 500),
        ('relay data/b631_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b631_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    L = ['b632 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    dg, bid, b = input_digest()
    L += ['', '### THE INPUT BANK BY DIGEST: relay %s at %s -- blob %s, %d bytes, sha256 %s' % (K.INPUT_BANK, K.INPUT_REV, bid, len(b), dg),
          '### THE E0 RULE SINCE 576891c5, its commits to tools/e0_rule.py:']
    L += ['    ' + l for l in g(RELAY, 'log', '--format=%h %s', '576891c5^..' + PRE_RELAY, '--', 'tools/e0_rule.py').split(NL) if l.strip()]
    d30 = set(re.findall(r'^def (\w+)', _show(RELAY, PRE_RELAY, 'tools/b630_record.py') or '', re.M))
    d31 = set(re.findall(r'^def (\w+)', _show(RELAY, PRE_RELAY, 'tools/b631_record.py') or '', re.M))
    shared = sorted(n for n in d30 - d31 if n in ('findings', 'trail', 'correction', 'desk', 'components', 'scores', 'n5', 'root', 'root_arm', 'table'))
    L += ['### THE DROPPED WRITER, BY DIFF OF THE TWO SEALED TOOLS AT %s: shared subcommands in b630`s tool and absent from b631`s: %s' % (PRE_RELAY, shared or 'NONE')]
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                         g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b632_reads.txt', L)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R242) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
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
    L = ['### b632 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b632_author_answers.txt', L)


def answer_of(k):
    """### the author's answer to the act's k-th prompt (0-based, across calls), whole: cut from the result after its own question's
    ### `"<question>"="` and before the next question's `", "<question>"="`, the questions read from the bank's prompt headers."""
    t = rd('b632_author_answers.txt')
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
KERN_PIN = {'SIDE-explicit-formula': '8c51431', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-spinor': '520abe7',
            'SIDE-effects': 'ef4cff7', 'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab', 'SIDE-global-section': '17ce9ff'}
WRITTEN_KERNS = ()   # ### this act writes no kernel


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
    put_json('b632_kernels_face.json', dict(at=utc(), kernels=kern_state()))


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
    p = os.path.join(SP if DRY else D, 'b632_scanfile_%s.md' % name)
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
W_HEAD = '*Appended 2026-10-06 by b632 to b631’s entry (:%d), under `(R242)`(1) -- b631 AT ITS WEIGHT:*'
TP_HEAD = '*Appended 2026-10-06 by b632 beneath the N5 scorer’s line (:%d), under `(R242)`(2) -- A TEST READS EVERY INPUT AT ITS OWN PIN, STANDING:*'


def _weight():
    return ('\n%s SIDE-explicit-formula v0.25 = 8c51431 on the kept branch dedekind-b631: DedekindConfig q, ζ’s configuration with its pole '
            'term summed with the family’s; dedekind_instance with no premise, the positivity equivalence derived; dedekind_rhs on '
            'TrivialSummandPremise and EulerFactorPremise q, both used; dedekind_three by rfl; Family.lean’s premises extended and the file '
            'unchanged; five declarations at the standard three, no sorryAx; the peel equal locally and at the remote. The build: two lake '
            'calls crossed the hold and were stopped by PID before finishing; the direct compile exited 0 at 32 s after a dip to 2,238 MB, and '
            'the AxiomCheck read 2,404 MB at one sample, both exiting on their own -- the watch reading the log’s last line alone, the '
            'seat’s; the route standing at OPEN_TRAILS :13167. The χ page at v0.25 with the five nodes and the backmatter sentence, no grade '
            'or tier moved; the ζ page unchanged; five table rows from the rule (2 definitions, 2 without hypothesis, 1 on its two named '
            'premises), no existing row moved. H65a to H65d hold; N2 refuted in letter by the split, the navigator’s; N1 and N3 to N5 held. '
            'The record lines at FINDINGS :7677 and OPEN_TRAILS :13159, :13161, :13163 and :13165, the multiplicity form registry-read and '
            'not asserted, no registry read in that act. Relay af38a0c3; PLACE-papers 3c2062c; the root 56b10119…, b624 to b631 agreeing, '
            'the one-byte control computed offline. The suite 80 of 82 by the seat’s pre-seal arms -- the build arm not admitting the direct '
            'route, the record arm expecting one prompt where two were answered -- each claim holding. Defects (a) to (k) the seat’s, among '
            'them the backtick apostrophes carried onto the public page and the record tool assembled without its findings writer, worked '
            'around from scratch scripts using the sealed tool’s own text and guards; both repaired at b632’s step zero (PLACE-papers '
            '62ab6f4; relay 66dfb8ca). The local intake bank untracked. Nothing deposited; no sorry on any main.\n' % (W_HEAD % K.B631_ENTRY))


def _testpin():
    return ('\n%s a test that regenerates anything reads every input at its own pin -- its lists, its probes, the table, the generator, '
            'the rule and the kernel’s checkout -- the live tree being for the act’s arms and not for the tests. From b631’s carried case '
            '(9) of tools/test_chain_page_b596.py, where b630’s rule-graded rows joined an older list’s Correspondence against relay HEAD’s '
            'table; the case is frozen to the test’s own pin by one edit after b632’s seal, committed alone with its run. At b632’s step zero '
            'tools/test_chain_page_b630.py was found failing in the same way, its list pinned at v0.24 read against the kernel’s checkout at '
            'v0.25 (the generator stops at the checkout, exit 3, before the hold is read); carried to the author, not repaired.\n' % (TP_HEAD % K.N5_LINE))


def record_lines(*a):
    """### FINDINGS: b631's weight (to its entry :7679). OPEN_TRAILS: the test-pin line, standing (beneath :12799, appended at the end)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The Dedekind zeta of ℚ(ζ_q) as a configuration of the schema at v0.25')
    if entry != K.B631_ENTRY:
        sys.exit('### b631`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B631_ENTRY, _weight()), ('OPEN_TRAILS.md', TP_HEAD % K.N5_LINE, _testpin())]
    cells, nd, clean = _guarded(items, 'OPEN_TRAILS.md', 'lines')
    fcells = predict_cells(items[0][2], 'FINDINGS.md')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    print('  backtick parity odd in: %s ; FINDINGS cells: %s' % (ticks or 'NONE', fcells or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or fcells or any(nd.values()) or not clean or ticks:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR ODD BACKTICKS -- NOTHING WRITTEN')
    _land(Q, items, 'b632_record_lines.json', K.B631_ENTRY)


def _run_test(rel, bank, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b632 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel,
                                  failing=[re.match(r'^  (\(\d+\))', l).group(1) for l in out.split(NL)
                                           if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]))
    print(L[-1])


def case9_run(*a):
    """### (R242)(2): test_chain_page_b596.py after its one edit, run and counted (data/b632_case9_test.txt)."""
    _run_test('tools/test_chain_page_b596.py', 'b632_case9_test')


# ================================================================================ COMPONENT 2: THE RULE GRADES
def rule_full(statement, name):
    """### the table's rule reading (terminal_table.rule_reading) with the shared rule's reason and its premises: RETURN
    ### (kind, grade, why, premises, header) -- premises the (binder, type) pairs the rule reads as premises."""
    import terminal_table as TT
    import e0_rule as E
    m = TT._DECL_KW.match(statement or '')
    if not m:
        return None, None, '', [], ''
    if m.group(1) not in ('theorem', 'lemma'):
        return 'def', 'DEF', '', [], ''
    head = ' '.join(re.sub(r'^\S+', '', statement[m.end():], count=1).split())
    gr, why, _b = E.grade(head, 'theorem')
    prem = []
    if gr == 'INTERFACES':
        h2 = E.statement_only(head)
        spans = E.exist_spans(h2)
        bs = [mm.groups() for mm in E.BINDER.finditer(h2) if not any(x <= mm.start() < y for x, y in spans)]
        bs = [(b, t) for b, t in bs if not E.data_binder(t)] + [('→', s) for s in E.seam_antecedents(E.conclusion(h2))]
        cs = E.conclusion_start(h2)
        facts = [((mm.group(1) or '[inst]'), mm.group(2).strip()) for mm in E.INSTANCE.finditer(h2) if cs is None or mm.start() < cs]
        prem = [(b, t) for b, t in bs if not E.domain_case(t, h2)] + facts
        if ', '.join('%s : %s' % bt for bt in prem) != why:
            prem = [('?', why)]          # ### the reconstruction disagrees with the rule's own reason: the reason is kept whole
    return 'theorem', gr, why, prem, head


REL = re.compile(r'^\s*(?:⊆|⊂|∣|=|≠|<|≤|>|≥|∈|∉|↔|→|∧|∨)')


def premise_name(t, head):
    """### the NAMED PREMISE of a premise type, by the face's reading: a leading ¬ and any ∀/∃ prefix to its comma stripped, the head
    ### token's last dotted component (p.Prime and Nat.Prime both read Prime); RETURN (name, None), or (None, why) when the head is a
    ### variable the statement binds or the type is a bare relation."""
    s = ' '.join((t or '').split())
    bound = set()
    for _ in range(6):
        s = re.sub(r'^¬\s*', '', s)
        m = re.match(r'^(∀|∃!?)\s+([^,]*),\s*', s)
        if not m:
            break
        bound |= set(re.findall(r"[^\W\d][\w'₀-₉]*", m.group(2).split(':')[0].split('∈')[0]))
        s = s[m.end():]
    s = s.lstrip('( ')
    m = re.match(r"([^\W\d][\w'₀-₉]*(?:\.[^\W\d][\w'₀-₉]*)*)", s)
    if not m:
        return None, 'a bare relation'
    tok, rest = m.group(1), s[m.end():]
    if REL.match(rest) or rest.lstrip().startswith(':'):
        return None, 'a bare relation'
    hb = set()
    for grp in re.findall(r'[({⦃\[]\s*([^:(){}\[\]⦃⦄]+?)\s*:', head or ''):
        hb |= set(grp.split())
    if '.' not in tok and (tok in hb or tok in bound):
        return None, 'a variable the statement binds'
    return tok.split('.')[-1], None


def _head_table():
    return json.loads(subprocess.run(['git', '-C', RELAY, 'show', 'HEAD:data/terminal_table.json'], capture_output=True).stdout.decode('utf-8'))


_FILECACHE = {}


def _file_at(repo, rev, path):
    k = (repo, rev, path)
    if k not in _FILECACHE:
        r = subprocess.run(['git', '-C', 'D:/' + repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
        _FILECACHE[k] = r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
    return _FILECACHE[k]


def at_pin(r):
    """### the row's statement read at its pin -- the commit the table read it at (its repository head, the row's `head`) -- by git:
    ### True when the statement's first line stands in the file there."""
    t = _file_at(r['repo'], r['head'], r.get('statement_file') or '')
    first = (r.get('statement') or '').split(NL)[0].strip()
    return bool(t) and bool(first) and first in t


def _bank_rows(b):
    out = []
    for l in b.decode('utf-8').replace(chr(13), '').split(NL):
        if l.startswith('  ') and l.count(' | ') == 3:
            repo, name, kind, rdg = [x.strip() for x in l.split(' | ')]
            out.append((repo, name, kind, rdg))
    return out


def rule_grades(*a):
    """### (R242)(3) PART ONE: b630's banked readings re-read against the table at relay HEAD; every row still UNGRADED with a readable
    ### statement printed with its statement, its pin and the rule's grade; the grades applied to a working copy of the table with
    ### provenance "rule" (data/b632_table_working.json), not committed; the moves banked (data/b632_rule_moves.txt and .json); the
    ### counts and the premise census printed."""
    dg, bid, b = input_digest()
    bank = _bank_rows(b)
    T = _head_table()
    rows = T['rows']
    by = {(r['repo'], r['name']): r for r in rows}
    W = copy.deepcopy(T)
    wby = {(r['repo'], r['name']): r for r in W['rows']}
    status, moved, changed_reading = collections.Counter(), [], []
    for repo, name, kind, rdg in bank:
        r = by.get((repo, name))
        if r is None:
            status['gone from the table'] += 1
            continue
        if r['grade'] != 'UNGRADED':
            status['graded since the bank, provenance %s' % r.get('provenance')] += 1
            continue
        k2, gr, why, prem, head = rule_full(r.get('statement'), r['name'])
        if gr is None:
            status['no statement the rule reads'] += 1
            continue
        if gr != rdg:
            changed_reading.append((repo, name, rdg, gr))
        moved.append(dict(repo=repo, name=name, kind=k2, grade=gr, why=why, premises=prem, pin=r.get('pin'), head=r['head'],
                          file=r.get('statement_file'), at_pin=at_pin(r), statement=r.get('statement'), header=head))
        w = wby[(repo, name)]
        w['grade'], w['provenance'] = gr, 'rule'
        status['UNGRADED and readable: moved'] += 1
    ung_head = [r for r in rows if r['grade'] == 'UNGRADED']
    W['counts'] = dict(W['counts'], ungraded=sum(1 for r in W['rows'] if r['grade'] == 'UNGRADED'))
    cell_moved = [(r['repo'], r['name']) for r in rows if r.get('provenance') == 'cell' and wby[(r['repo'], r['name'])]['grade'] != r['grade']]
    other_moved = [(r['repo'], r['name']) for r in rows if r.get('provenance') != 'cell' and r['grade'] != 'UNGRADED'
                   and wby[(r['repo'], r['name'])]['grade'] != r['grade']]
    grades = collections.Counter(x['grade'] for x in moved)
    by_repo = collections.Counter(x['repo'] for x in moved)
    unnamed, census_rows, nbind = [], collections.defaultdict(set), 0
    for x in moved:
        if x['grade'] != 'INTERFACES':
            continue
        for bnd, t in x['premises']:
            nm, why = premise_name(t, x['header'])
            if nm:
                nbind += 1
                census_rows[nm].add(x['repo'] + '/' + x['name'])      # ### counted by premise: the rows resting on it, each row once
            else:
                unnamed.append((x['repo'], x['name'], bnd, t, why))
    named = collections.Counter({nm: len(v) for nm, v in census_rows.items()})
    left = collections.Counter(r['grade'] for r in W['rows'] if r['grade'] in ('UNGRADED', 'UNCLASSIFIED'))
    L = ['b632 -- COMPONENT 2, (R242)(3) PART ONE: THE E0 RULE`S GRADES ON THE TABLE`S UNGRADED ROWS, APPLIED TO A WORKING COPY WITH '
         'PROVENANCE "rule", NOT COMMITTED (%s)' % utc(), '',
         '### the input: relay %s at %s, blob %s, sha256 %s ; its rows %d' % (K.INPUT_BANK, K.INPUT_REV, bid[:12], dg, len(bank)),
         '### the table at relay HEAD %s: %d rows ; UNGRADED %d ; provenance %s' % (
             g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), len(rows), len(ung_head), dict(collections.Counter(r.get('provenance') for r in rows))),
         '### the bank`s rows re-read against it: %s' % dict(status),
         '### readings that moved since the bank: %d %s' % (len(changed_reading), changed_reading[:10] or ''),
         '### UNGRADED rows the bank does not carry: %d' % sum(1 for r in ung_head if (r['repo'], r['name']) not in set((x[0], x[1]) for x in bank)),
         '### statements read at their pins by git (the first line standing in the file at the row`s commit): %d of %d' % (
             sum(1 for x in moved if x['at_pin']), len(moved)), '',
         '### ### **ROWS MOVED %d ; DERIVES %d ; INTERFACES %d ; DEF %d ; ENCODES-CONCLUSION %d ; UNCLASSIFIED LEFT %d ; UNGRADED LEFT %d.**' % (
             len(moved), grades['DERIVES'], grades['INTERFACES'], grades['DEF'], grades['ENCODES-CONCLUSION'], left['UNCLASSIFIED'], left['UNGRADED']),
         '### moved by repository: %s' % dict(by_repo.most_common()),
         '### cell-graded rows whose grade moves in the working copy: %d %s ; other graded rows moved: %d %s' % (
             len(cell_moved), cell_moved[:5] or '', len(other_moved), other_moved[:5] or ''), '',
         '### THE PREMISE CENSUS of the INTERFACES rows (the face`s reading: the head of each premise`s type, its last dotted component):',
         '### ### **DISTINCT NAMED PREMISES %d ; INTERFACES ROWS %d ; PREMISE BINDERS NAMED %d ; UNNAMED %d (a variable the statement binds, or a '
         'bare relation).**' % (len(named), grades['INTERFACES'], nbind, len(unnamed)),
         '### each named premise with the count of rows resting on it, and the rows:']
    L += ['    %-28s %3d  %s' % (n, c, ', '.join(sorted(census_rows[n]))) for n, c in sorted(named.items(), key=lambda x: (-x[1], x[0]))]
    L += ['  unnamed: %s | %s | %s : %s -- %s' % u for u in unnamed]
    L += ['', '### ROW BY ROW: repository | name | kind | the rule`s grade | pin | file | premises | the statement at its pin (whitespace joined):']
    for x in sorted(moved, key=lambda x: (x['repo'], x['name'])):
        pin = ('cited %s, read at %s' % (x['pin'], x['head'])) if x['pin'] else 'read at %s' % x['head']
        L.append('  %s | %s | %s | %s | %s | %s | %s | %s' % (x['repo'], x['name'], x['kind'], x['grade'], pin, x['file'],
                                                           ('; '.join('%s : %s' % bt for bt in x['premises']) or '-'), ' '.join((x['statement'] or '').split())))
    put_txt(K.MOVES, L)
    put_json(K.MOVES.replace('.txt', '.json'), dict(
        at=utc(), input=dict(path=K.INPUT_BANK, rev=K.INPUT_REV, blob=bid, sha256=dg, rows=len(bank)), head=g(RELAY, 'rev-parse', 'HEAD').strip(),
        status=dict(status), changed_reading=changed_reading, moved=len(moved), grades=dict(grades), by_repo=dict(by_repo),
        at_pin=sum(1 for x in moved if x['at_pin']), cell_moved=cell_moved, other_moved=other_moved, left=dict(left),
        named=dict(named), unnamed=[list(u) for u in unnamed], rows=[{k: v for k, v in x.items() if k not in ('statement', 'header')} for x in moved]))
    put_txt(K.WORKING, [json.dumps(W, indent=1, ensure_ascii=False)])
    for l in L[2:20]:
        print(l[:300])


# ================================================================================ COMPONENT 3: THE PACKET AND THE HOLD
GRADE_WORDS = re.compile(r'\b(DERIVES|INTERFACES|ENCODES-CONCLUSION|ENCODES|DEF|UNGRADED|UNCLASSIFIED|SHELL)\b')
ACT_NO = re.compile(r'\bb\d{3,4}\b')
KERNEL_B = re.compile(r'\bB\d{3}\b')


def _sample():
    M = jl(K.MOVES.replace('.txt', '.json'))
    T = _head_table()
    st = {(r['repo'], r['name']): r for r in T['rows']}
    top = [k for k, _c in sorted(M['by_repo'].items(), key=lambda x: (-x[1], x[0]))[:2]]
    rng = random.Random(K.SEED)
    items = []
    for k in top:
        pool = sorted((x for x in M['rows'] if x['repo'] == k), key=lambda x: x['name'])
        items += rng.sample(pool, K.PER_KERNEL)
    rng.shuffle(items)
    out = []
    for i, x in enumerate(items, 1):
        r = st[(x['repo'], x['name'])]
        out.append(dict(item='G%03d' % i, repo=x['repo'], name=x['name'], grade=x['grade'], why=x['why'], file=x['file'], head=x['head'],
                        pin=x['pin'], statement=r['statement'], at_pin=at_pin(r)))
    return top, out


def _prompt_text():
    import e0_rule as E
    rule = [re.sub(r'\(R\d+\)', '(R—)', ACT_NO.sub('b—', re.sub(r'^###\s?', '', l))) for l in E.RULE_TEXT]
    return NL.join([
        'You are being asked to act as an independent second reader for a research programme`s machine-checked declarations. You have no '
        'context of the work that produced them, and that is the point: read only the files named below, judge each item on its own words, '
        'and write your answers to one file. Do not open, search or read any other file in any repository on this machine, do not run git, '
        'and do not change any file except the one answer file named at the end.', '',
        'The packet is the directory D:/relay/data/%s. Read its two files: 00_README.txt and 01_statements.txt.' % K.PACKET_DIR, '',
        'THE RULE. Each item is one Lean declaration`s statement as its repository holds it at the commit named. Grade each by the rule below, '
        'read from the statement`s own binders and conclusion alone -- not from its name, its proof or what you know of the mathematics. The '
        'rule`s text follows as its source carries it, the citations of the acts and rulings that wrote each clause masked:', ''] + rule + [
        '',
        'THE GRADES. Answer exactly one of:',
        '  DEF -- the declaration is a definition, structure or other object (its keyword is def, abbrev, instance, structure, class or '
        'inductive), not a theorem;',
        '  DERIVES -- a theorem whose explicit hypothesis binders are all domain conditions under the rule, or which has none;',
        '  INTERFACES -- a theorem with at least one explicit hypothesis binder that is a premise under the rule; name that binder in your reason;',
        '  ENCODES-CONCLUSION -- a theorem one of whose explicit hypothesis binders has the conclusion itself as its type, its bound variables renamed.',
        'Give one line of reason.', '',
        'TASK -- 60 statements (01_statements.txt), items G001 to G060.', '',
        'THE ANSWER FILE. Write all your answers to D:/relay/data/%s, one item per line, in the packet`s own order, in exactly this form:' % K.ANSWERS,
        '  G001 | DERIVES | your one line of reason',
        'Every item G001 to G060 must have exactly one line. Use no other grade words than the four above, and do not put a vertical bar '
        'inside a reason. When the file is complete, read it back once to check every item is present, then stop. Do not commit, push or '
        'edit anything else.']).replace('`', "'")      # ### every backtick here is a possessive (the rule's ten among them): written plain


LEAD = ('Reader task follows. The packet is at D:\\relay\\data\\%s\\ and your answers go to D:\\relay\\data\\%s. Read only the packet '
        'files. Do not open FINDINGS.md, OPEN_TRAILS.md, any file under D:\\relay\\data\\ other than the packet, anything named b632_key or '
        'b632_rule_moves, or any repository history. Write the answers file, report that it is written, and stop.' % (K.PACKET_DIR, K.ANSWERS))
ONE_LINER = ('Get-Content D:\\reader_b632\\full_prompt.txt -Raw | claude -p --output-format json --allowedTools Read Glob Write '
             '--disallowedTools Bash PowerShell WebFetch WebSearch --permission-mode acceptEdits --permission-prompts none --add-dir '
             'D:\\relay\\data --setting-sources user --strict-mcp-config > D:\\reader_b632\\reader_run.log 2> D:\\reader_b632\\reader_run.err')
HOLD_PROMPT = ('The reader packet is at data/b632_reader_packet/ and the prompt at data/b632_reader_prompt.txt. Open a fresh Claude Code '
               'session on D:, clear it, paste the prompt led with prose, let the reader write data/b632_reader_answers.txt and close; then '
               'answer here that the bank is there.')


def packet(*a):
    """### the seeded sample of sixty (thirty from each of the two kernels with the most moves), each its statement at its pin with the
    ### grade withheld: data/b632_reader_packet/ (00_README.txt, 01_statements.txt), the key data/b632_key.txt, the prompt
    ### data/b632_reader_prompt.txt in b620's form; the reader's directory D:/reader_b632 (lead.txt, full_prompt.txt); the scan of the
    ### packet for a grade word and an act number and the no-disclosure arm over it (data/b632_packet_scan.txt)."""
    top, items = _sample()
    readme = ["The reader's packet. Two files: this one; and 01_statements.txt, 60 statements of Lean declarations, each with the repository, "
              'the file and the commit it is read at. The task is in the prompt that came with it.']
    st = ['Statements. Each is one declaration as its repository holds it at the commit named, copied verbatim; the task is in the prompt.', '']
    for x in items:
        st.append('%s -- repository %s, file %s, at commit %s' % (x['item'], x['repo'], x['file'], x['head']))
        st += ['    ' + l for l in (x['statement'] or '').split(NL)]
        st.append('')
    key = ['b632 -- THE KEY, (R242)(3): the seeded sample (seed %d, Python random.Random: %d from each of %s, sampled from each kernel`s moved '
           'rows sorted by name, then shuffled) keyed to its row and the rule`s grade; banked beside the packet; the reader does not read it.'
           % (K.SEED, K.PER_KERNEL, ' and '.join(top)), '']
    key += ['%s %-34s %-74s rule %-18s %s' % (x['item'], x['repo'], x['name'], x['grade'], x['why'][:200]) for x in items]
    prompt = _prompt_text()
    pdir = _w(K.PACKET_DIR)
    os.makedirs(pdir, exist_ok=True)
    put_txt(K.PACKET_DIR + '/00_README.txt', readme)
    put_txt(K.PACKET_DIR + '/01_statements.txt', st)
    put_txt(K.KEY, key)
    put_txt(K.PROMPT, [prompt])
    pk = NL.join(readme + st)
    gw = [m.group(0) for m in GRADE_WORDS.finditer(pk)]
    an = [m.group(0) for m in ACT_NO.finditer(pk)]
    kb = sorted(set(m.group(0) for m in KERNEL_B.finditer(pk)))
    nd, nn = _nd(pk + NL + prompt)
    S = ['b632 -- COMPONENT 3: THE PACKET`S SCANS (%s)' % utc(), '',
         '### the packet: %d items ; %d from each of %s ; statements read at their pins %d of %d' % (len(items), K.PER_KERNEL, top,
                                                                                                  sum(1 for x in items if x['at_pin']), len(items)),
         '### the rule`s grades among the sixty (in the key, not the packet): %s' % dict(collections.Counter(x['grade'] for x in items)),
         '### grade words in the packet (%s): %d %s' % (GRADE_WORDS.pattern, len(gw), gw[:10] or ''),
         '### act numbers in the packet (%s): %d %s' % (ACT_NO.pattern, len(an), an[:10] or ''),
         '### the kernel`s own namespace names of the B-form in the packet (printed as they stand, not act numbers): %s' % (kb or 'NONE'),
         '### act numbers in the prompt: %d ; ruling ids in the prompt: %d' % (len(ACT_NO.findall(prompt)), len(re.findall(r'\(R\d+\)', prompt))),
         '### the no-disclosure arm over the packet and the prompt: hits %s over sets of %s' % (nd, nn), '',
         '### ### **GRADE WORDS %d ; ACT NUMBERS %d ; NO-DISCLOSURE HITS %d.**' % (len(gw), len(an), sum(nd.values()))]
    put_txt('b632_packet_scan.txt', S)
    put_json('b632_packet_scan.json', dict(at=utc(), items=len(items), top=top, grade_words=gw, act_numbers=an, kernel_b=kb, nd=nd,
                                           at_pin=sum(1 for x in items if x['at_pin']), grades=dict(collections.Counter(x['grade'] for x in items)),
                                           prompt_acts=len(ACT_NO.findall(prompt))))
    if not DRY:
        if os.path.exists(K.READER_DIR) and os.listdir(K.READER_DIR):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- THE READER`S DIRECTORY NOT WRITTEN' % K.READER_DIR)
        os.makedirs(K.READER_DIR, exist_ok=True)
        _write(os.path.join(K.READER_DIR, 'lead.txt'), (LEAD + NL).encode('utf-8'))
        _write(os.path.join(K.READER_DIR, 'full_prompt.txt'), (LEAD + NL + NL + prompt + NL).encode('utf-8'))
        print('  written: %s/lead.txt and full_prompt.txt' % K.READER_DIR)
    for l in S[2:]:
        print(l[:240])


def hold(*a):
    """### the hold's text: the one prompt, verbatim, and b620's one-liner with the paths changed beneath it (printed, not banked)."""
    print(HOLD_PROMPT)
    print()
    print('cd D:\\reader_b632')
    print(ONE_LINER)


# ================================================================================ COMPONENT 4: THE KEYING
ANS_RE = re.compile(r'^(G\d{3}) \| (DERIVES|INTERFACES|ENCODES-CONCLUSION|DEF) \| (.*)$')


def key_back(*a):
    """### the reader's bank keyed back against the key: the agreement rate over sixty, the disagreements by grade pair with the reader's
    ### lines; the branch (R242)(3) takes (data/b632_agreement.txt and .json)."""
    key = {}
    for l in rd(K.KEY).split(NL):
        m = re.match(r'^(G\d{3}) (\S+)\s+(\S+)\s+rule (\S+)\s*(.*)$', l)
        if m:
            key[m.group(1)] = dict(repo=m.group(2), name=m.group(3), grade=m.group(4), why=m.group(5))
    ans, bad = {}, []
    raw = rd(K.ANSWERS)
    for l in raw.split(NL):
        if not l.strip():
            continue
        m = ANS_RE.match(l.strip())
        if m and m.group(1) not in ans:
            ans[m.group(1)] = (m.group(2), m.group(3), l.strip())
        else:
            bad.append(l[:200])
    agree = sorted(i for i in key if i in ans and ans[i][0] == key[i]['grade'])
    dis = sorted(i for i in key if i not in agree)
    rate = len(agree) / float(len(key)) if key else 0.0
    pairs = collections.Counter((key[i]['grade'], ans[i][0] if i in ans else 'NO ANSWER') for i in dis)
    branch = 'commit' if rate >= K.AGREE_BAR else 'hold'
    L = ['b632 -- COMPONENT 4, (R242)(3) PART TWO: THE READER`S BANK KEYED BACK (%s)' % utc(), '',
         '### the reader`s bank relay data/%s: %d bytes, sha256 %s ; lines in the answer form %d ; lines not in it %d %s' % (
             K.ANSWERS, len(raw.encode('utf-8')), hashlib.sha256(raw.encode('utf-8')).hexdigest(), len(ans), len(bad), bad[:3] or ''),
         '### items keyed %d ; answered %d ; agreeing %d ; disagreeing %d' % (len(key), sum(1 for i in key if i in ans), len(agree), len(dis)),
         '### by kernel: %s' % dict((k, '%d of %d' % (sum(1 for i in agree if key[i]['repo'] == k), sum(1 for i in key if key[i]['repo'] == k)))
                                    for k in sorted(set(v['repo'] for v in key.values()))),
         '### ### **AGREEMENT %d OF %d = %.4f AGAINST THE BAR %.2f : %s.**' % (len(agree), len(key), rate, K.AGREE_BAR,
                                                                             'AT OR ABOVE -- THE COMMIT BRANCH' if branch == 'commit' else 'BELOW -- THE HOLD BRANCH'), '',
         '### THE DISAGREEMENTS BY GRADE PAIR (the rule`s grade -> the reader`s): %s' % {'%s -> %s' % k: v for k, v in pairs.items()}]
    for (rg, ag), _n in sorted(pairs.items()):
        L.append('### %s -> %s:' % (rg, ag))
        for i in dis:
            if key[i]['grade'] == rg and (ans[i][0] if i in ans else 'NO ANSWER') == ag:
                L.append('    %s %s %s -- the rule: %s' % (i, key[i]['repo'], key[i]['name'], key[i]['why'][:160] or '-'))
                L.append('        the reader: %s' % (ans[i][2] if i in ans else 'NO ANSWER'))
    put_txt(K.AGREEMENT, L)
    put_json(K.AGREEMENT.replace('.txt', '.json'), dict(at=utc(), items=len(key), answered=sum(1 for i in key if i in ans), agree=len(agree),
                                                         rate=rate, bar=K.AGREE_BAR, branch=branch, pairs={'%s -> %s' % k: v for k, v in pairs.items()},
                                                         disagreements=dis, bad_lines=bad, answers_sha256=hashlib.sha256(raw.encode('utf-8')).hexdigest()))
    for l in L[2:8]:
        print(l[:240])


def reader_audit(*a):
    """### the reader's own session transcript, every tool call with its path, read after its bank landed (data/b632_reader_run.txt): the
    ### sessions under the projects folder written after the packet's commit that name the packet, this session excluded."""
    pk = g(RELAY, 'log', '-1', '--format=%ct', '--', 'data/' + K.PACKET_DIR).strip()
    since = int(pk) if pk.isdigit() else 0
    found = []
    for d in sorted(os.listdir(PROJECTS)):
        if not d.startswith('D--'):
            continue
        for f in os.listdir(os.path.join(PROJECTS, d)):
            p = os.path.join(PROJECTS, d, f)
            if f.endswith('.jsonl') and SESSION_ID not in f and os.path.getmtime(p) >= since:
                t = io.open(p, encoding='utf-8', errors='replace').read()
                if K.PACKET_DIR in t:
                    found.append((p, t))
    L = ['b632 -- THE READER`S RUN, ITS TRANSCRIPT AUDITED (%s)' % utc(), '', '### sessions found naming the packet, written after its commit: %d' % len(found)]
    outside = []
    for p, t in found:
        calls = []
        for raw in t.split(NL):
            try:
                o = json.loads(raw)
            except Exception:
                continue
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if isinstance(c, dict) and c.get('type') == 'tool_use':
                    inp = c.get('input') or {}
                    path = inp.get('file_path') or inp.get('path') or inp.get('pattern') or inp.get('command') or ''
                    calls.append((c.get('name'), str(path)[:200]))
        L.append('### %s -- tool calls %d' % (p, len(calls)))
        L += ['    %-6s %s' % c for c in calls]
        outside += [c for c in calls if not (K.PACKET_DIR in c[1].replace('\\', '/') or K.ANSWERS in c[1] or c[1].replace('\\', '/').endswith('/' + K.PACKET_DIR))]
    L += ['', '### ### **SESSIONS %d ; CALLS OUTSIDE THE PACKET AND THE ANSWER FILE : %d %s.**' % (len(found), len(outside), outside[:6] or '')]
    put_txt('b632_reader_run.txt', L)
    print(L[-1])


def branch():
    return (jx(K.AGREEMENT.replace('.txt', '.json')).get('branch')) or 'pending'


# ================================================================================ COMPONENT 5: THE TABLE, THE PAGES, THE ROOT
def table_test(*a):
    """### the commit branch: test_terminal_table_b630.py after the generator's edit, run and counted (data/b632_table_test.txt)."""
    _run_test('tools/test_terminal_table_b630.py', 'b632_table_test')


def cpage_test(*a):
    """### the commit branch: the page generator's provenance cell, its test run and counted (data/b632_cpage_test.txt)."""
    _run_test('tools/test_chain_page_b632.py', 'b632_cpage_test')


def table_compare(*a):
    """### the commit branch: the table regenerated by the edited generator (data/terminal_table.json on disk) against the working copy,
    ### row by row in grade and provenance, every difference printed (data/b632_table_compare.txt and .json)."""
    W = jl(K.WORKING)
    N = json.load(io.open(_r('terminal_table.json'), encoding='utf-8'))
    w = {(r['repo'], r['name']): r for r in W['rows']}
    n = {(r['repo'], r['name']): r for r in N['rows']}
    only_w, only_n = sorted(set(w) - set(n)), sorted(set(n) - set(w))
    diff = [(k, (w[k]['grade'], w[k].get('provenance')), (n[k]['grade'], n[k].get('provenance'))) for k in sorted(set(w) & set(n))
            if (w[k]['grade'], w[k].get('provenance')) != (n[k]['grade'], n[k].get('provenance'))]
    L = ['b632 -- COMPONENT 5: THE REGENERATED TABLE AGAINST THE WORKING COPY, ROW BY ROW (%s)' % utc(), '',
         '### rows: working %d, regenerated %d ; only in the working copy %d %s ; only in the regenerated %d %s' % (
             len(w), len(n), len(only_w), only_w[:5] or '', len(only_n), only_n[:5] or ''),
         '### the regenerated table`s provenance: %s ; its grades by provenance rule: %s' % (
             dict(collections.Counter(r.get('provenance') for r in N['rows'])),
             dict(collections.Counter(r['grade'] for r in N['rows'] if r.get('provenance') == 'rule')))]
    L += ['  %s / %s : working %s|%s -> regenerated %s|%s' % (k[0], k[1], a_[0], a_[1], b_[0], b_[1]) for k, a_, b_ in diff]
    L += ['', '### ### **ROWS DIFFERING IN GRADE OR PROVENANCE : %d ; ROWS IN ONE AND NOT THE OTHER : %d.**' % (len(diff), len(only_w) + len(only_n))]
    put_txt('b632_table_compare.txt', L)
    put_json('b632_table_compare.json', dict(at=utc(), differ=[[list(k), list(a_), list(b_)] for k, a_, b_ in diff], only_working=[list(k) for k in only_w],
                                             only_regenerated=[list(k) for k in only_n]))
    print(L[-1])


def nodes_zeta(*a):
    """### the commit branch: b630's ζ list carried as b632's at pin v0.25, its record lines unchanged (data/b632_nodes_zeta.txt)."""
    src = rd(K.NODES['zeta']).rstrip(NL).split(NL)
    if '# pin: v0.24' not in src:
        sys.exit('### b630`S LIST CARRIES NO `# pin: v0.24` LINE -- NOTHING WRITTEN')
    head = ['# b632 -- (R242)(3) and the author`s answer before b632`s seal (relay data/b632_author_answers.txt, prompt 2): b630`s list',
            '# (relay data/b630_nodes_zeta.txt) carried at pin v0.25, every record line unchanged, for the ζ page`s fresh probe on the',
            '# commit branch; the kernel`s main is at v0.25 and v0.25 adds no ζ node.', '#']
    put_txt(K.NEW_NODES_ZETA, head + [('# pin: v0.25' if l == '# pin: v0.24' else l) for l in src])


def probe_page(k, *a):
    """### the commit branch, ONE call in the foreground per page: the page's fresh probe at v0.25 from its list in force (the generator
    ### refuses beneath the hold and prints its reading), free memory sampled every 2 s and the probe's children's working sets beside
    ### it; the probe's output banked as data/b632_probe_out.txt or data/b632_chi_probe_out.txt; the page written where it changed;
    ### a joining row the probe does not resolve listed by name and not fabricated (data/b632_probe_<k>.txt and .json)."""
    import threading
    import chain_page as CP
    samples, stop = [], threading.Event()

    def sampler():
        while not stop.is_set():
            out = subprocess.run(['tasklist', '/FO', 'CSV', '/NH'], capture_output=True, text=True).stdout
            row = {}
            for l in out.split(NL):
                f = [x.strip('"') for x in l.strip().split('","')]
                if len(f) >= 5 and f[0].lower() in ('lean.exe', 'lake.exe'):
                    row[f[0] + ':' + f[1]] = int(re.sub(r'\D', '', f[4]) or 0) // 1024
            samples.append((time.time(), R2.free_mb(), row))
            stop.wait(2)

    nl = K.NEW_NODES_ZETA if k == 'zeta' else K.NEW_NODES_CHI
    po_name = K.NEW_PROBE_ZETA if k == 'zeta' else K.NEW_PROBE_CHI
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d) ; list %s' % (fm, CP.HOLD_MB, nl))
    if 0 <= fm < CP.HOLD_MB:
        put_json('b632_probe_%s.json' % k, dict(at=utc(), rc=None, refused=True, free_before=fm))
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    pd = os.path.join(SP, '_b632_probe_%s' % k)
    th = threading.Thread(target=sampler, daemon=True)
    t0 = time.time()
    th.start()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), pd, None)
    stop.set()
    th.join()
    secs = int(time.time() - t0)
    po = os.path.join(pd, 'chain_page_probe_out.txt')
    if os.path.exists(po) and not DRY and rc in (0, 6):
        _write(os.path.join(D, po_name), open(po, 'rb').read().replace(b'\r\n', b'\n'))
    peak_child = max([sum(s[2].values()) for s in samples] or [0])
    low = min([s[1] for s in samples] or [fm])
    unres = []
    for l in log or []:
        if l.startswith('unresolved: '):
            unres = re.findall(r"'([^']+)'", l)
    L = ['b632 -- COMPONENT 5: THE %s PAGE`S FRESH PROBE AT v0.25 (%s); exit %s ; %d s' % ('ζ' if k == 'zeta' else 'χ', utc(), rc, secs), '',
         '### free memory before the call %d MB (the hold %d) ; the lowest sample during it %d MB ; samples %d, every 2 s' % (fm, CP.HOLD_MB, low, len(samples)),
         '### the probe`s children (lean, lake): peak working set summed %d MB' % peak_child,
         '### joining rows the probe did not resolve, listed by name and not fabricated: %d %s' % (len(unres), unres or ''), '',
         '### the samples (seconds from start | free MB | child working sets MB):']
    L += ['    %5.0f | %5d | %s' % (t - t0, f, ' '.join('%s=%d' % kv for kv in sorted(r.items()))) for t, f, r in samples]
    L += ['', '### the generator`s log: %s' % (' / '.join(log)[:900] if log else 'empty'),
          '### ### **EXIT %s ; THE LOWEST FREE READING %d MB AGAINST THE HOLD %d%s ; PEAK OF THE CHILDREN %d MB.**' % (
              rc, low, CP.HOLD_MB, ' -- A DIP BENEATH IT MID-CALL, RECORDED' if low < CP.HOLD_MB else '', peak_child)]
    put_txt('b632_probe_%s.txt' % k, L)
    put_json('b632_probe_%s.json' % k, dict(at=utc(), rc=rc, seconds=secs, free_before=fm, low=low, peak_child=peak_child, unresolved=unres,
                                            dip=low < CP.HOLD_MB, log=log))
    print(L[-1])
    if rc:
        sys.exit('### THE %s PROBE OR PAGE EXITED %s' % (k, rc))
    _page_write(k, pg, fm, secs, rc)


def chilist():
    """### the χ list and probe in force: on the commit branch b632's list with its fresh probe; after step zero b632's list (the
    ### apostrophes) with b631's probe; before it b631's."""
    if os.path.exists(_r(K.NEW_NODES_CHI)) and os.path.exists(_r(K.NEW_PROBE_CHI)):
        return K.NEW_NODES_CHI, K.NEW_PROBE_CHI
    if os.path.exists(_r(K.NEW_NODES_CHI)):
        return K.NEW_NODES_CHI, K.PROBE['chi']
    return K.NODES['chi'], K.PROBE['chi']


def zlist():
    """### the ζ list and probe in force: on the commit branch b632's list at v0.25 with its fresh probe; otherwise b630's."""
    if os.path.exists(_r(K.NEW_NODES_ZETA)) and os.path.exists(_r(K.NEW_PROBE_ZETA)):
        return K.NEW_NODES_ZETA, K.NEW_PROBE_ZETA
    return K.NODES['zeta'], K.PROBE['zeta']


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


def _page_write(k, pg, fm, secs, rc, stage=''):
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
    added = sorted(n for n in gb if n not in ga and n.startswith('corr:'))
    nl, pr = zlist() if k == 'zeta' else chilist()
    put_json('b632_page_%s%s.json' % (k, ('_' + stage) if stage else ''), dict(
        page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb), grade_cells_moved=gmoved,
        tier_cells_moved=tmoved, corr_added=added, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs, nodes=nl, probe=pr, stage=stage or 'final'))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s ; tier cells moved %s ; Correspondence rows added %d' % (
        k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE', tmoved or 'NONE', len(added)))
    for x in dl[:12]:
        print('    ' + x[:240])


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked list and probe; `page chi stepzero` banks under the stage's
    ### name (data/b632_page_chi_stepzero.json), so the commit branch's re-emission does not overwrite it."""
    import chain_page as CP
    stage = [x for x in a if x != 'dry'][:1]
    stage = stage[0] if stage else ''
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = zlist() if k == 'zeta' else chilist()
    print('  list %s ; probe %s' % (nl, pr))
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b632_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b632_page_%s%s.json' % (k, ('_' + stage) if stage else ''), dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    _page_write(k, pg, fm, secs, rc, stage)


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b632 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        nl, pr = zlist() if k == 'zeta' else chilist()
        r = GCP.arm(os.path.join(D, nl), os.path.join(SP, '_b632_gcp'), os.path.join(D, pr))
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
    put_txt('b632_page_arms.txt', L)
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
    L = ['b632 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(ch)),
         '### the rows changed, by the grade each now reads: %s' % dict(collections.Counter(tg.get(n) for n in ch)),
         '### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
         '### ### **THE GRADE COLUMN`S DIFF, THE TABLE BEFORE THIS RUN AGAINST AFTER IT : %d ROWS MOVED %s.**' % (
             len(gmoved), dict(collections.Counter('%s -> %s' % (before.get(n), tg.get(n)) for n in gmoved)) or 'EMPTY')]
    L += ['  %-62s %s -> %s' % (n, before.get(n), tg.get(n)) for n in gmoved]
    name = 'b632_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 changed=ch, grade_moved=gmoved, files_moved=moved))
    print(L[6])


ROOT_EXCLUDE = re.compile(r'^b632_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    out = sorted('data/' + f for f in os.listdir(D) if f.startswith('b632_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))
    pk = os.path.join(D, K.PACKET_DIR)
    if os.path.isdir(pk):
        out += sorted('data/%s/%s' % (K.PACKET_DIR, f) for f in os.listdir(pk))
    return out


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b632'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline: the root recomputed over the banked items and over a copy of one bank with its first byte
    ### changed. The chain's verify is read inside the suite alone ((R242)'s procedural line), never here."""
    import shutil
    import act_root as AR
    J = jl('b632_act_root.json')
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
    L = ['b632 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s) ; '
         'the copy`s root differs %s' % (bank, r2, same, J['root'], r2 != J['root']),
         '', '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b632_root_arm.txt', L)
    put_json('b632_root_arm.json', dict(at=utc(), bank=bank, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H66a', 'H66b', 'H66c', 'H66d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b631_closing_push_out.txt', 'data/act_roots.txt', 'tools/test_record_findings_b632.py', 'tools/test_chain_page_b596.py'}
N5_GEN = ('tools/terminal_table.py', 'tools/test_terminal_table_b630.py', 'tools/chain_page.py', 'tools/test_chain_page_b632.py')


def _relay_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(RELAY, 'log', '--reverse', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def sorry_tokens(rev='main'):
    n = 0
    for f in g(K.KER, 'ls-tree', '-r', '--name-only', rev).split(NL):
        if f.endswith('.lean'):
            t = _show(K.KER, rev, f) or ''
            t = re.sub(r'/-.*?-/', '', t, flags=re.S)
            t = re.sub(r'--[^\n]*', '', t)
            n += len(re.findall(r'\bsorry\b', t))
    return n


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
    face = jl('b632_kernels_face.json')['kernels']
    now = kern_state(list(face))
    kern_ok = all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    pp_beyond = [x for x in pp_ch if x not in ('FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE)]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    gen = [x for x in relay_ch if x in N5_GEN]
    beyond = [x for x in relay_ch if not os.path.basename(x).startswith(('b632_', 'audit_b632_', 'terminal_table')) and x not in N5_ALLOWED
              and x not in N5_GEN]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ok = kern_ok and not pp_beyond and not beyond and not gen and rec_ok and not tracked_local and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel unmoved against the face %s; PLACE-papers %s (beyond the ledgers and the pages: %s); %s; relay '
            'beyond the list: %s; the generators` edits the author ordered on the commit branch, outside the list`s letter: %s; b628`s local '
            'intake bank in any relay commit %s, untracked now %s; no outbound request was made, so no identifier in one' % (
                kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE', gen or 'NONE', tracked_local, untracked_local))


def scores(*a):
    M, P, A = jx(K.MOVES.replace('.txt', '.json')), jx('b632_packet_scan.json'), jx(K.AGREEMENT.replace('.txt', '.json'))
    TF, RA, TC, C9 = jx('b632_table_rule.json'), jx('b632_root_arm.json'), jx('b632_table_compare.json'), jx('b632_case9_test.json')
    PZ, PX = jx('b632_page_zeta.json'), jx('b632_page_chi.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    moved, named = M.get('moved') or 0, len(M.get('named') or {})
    rate = A.get('rate')
    br = A.get('branch')
    cell_ok = M.get('cell_moved') == [] and (br != 'commit' or (TF and not [n for n in (TF.get('grade_moved') or []) if n in _cell_names()]))
    pairs = A.get('pairs') or {}
    S = {
        'H66a': (('HOLDS' if moved >= 1700 else 'REFUTED'), 'rows taking a rule grade %d against 1,700' % moved),
        'H66b': (('HOLDS' if M and named <= 40 else 'REFUTED'), 'distinct named premises under the INTERFACES rows %d against forty, each printed '
                 'with its count in data/b632_rule_moves.txt; %d premise binders unnamed beside them' % (named, len(M.get('unnamed') or []))),
        'H66c': (('HOLDS' if rate is not None and rate >= K.AGREE_BAR else 'REFUTED'), 'the second reader agrees on %s of %s = %s against %.2f' % (
            A.get('agree'), A.get('items'), ('%.4f' % rate) if rate is not None else None, K.AGREE_BAR)),
        'H66d': (('HOLDS' if M and cell_ok else 'REFUTED'), 'cell-graded rows moved in the working copy %s; in the committed table %s' % (
            M.get('cell_moved'), 'not committed' if br != 'commit' else [n for n in (TF.get('grade_moved') or []) if n in _cell_names()])),
        'N1': (('HELD' if moved >= 1700 and cell_ok else 'REFUTED'), 'as H66a and H66d'),
        'N2': (('HELD' if M and named <= 40 else 'REFUTED'), 'as H66b'),
        'N3': (('HELD' if P and not P.get('grade_words') and not P.get('act_numbers') else 'REFUTED'),
               'the packet`s scan: grade words %s, act numbers %s' % (P.get('grade_words'), P.get('act_numbers'))),
        'N4': (('HELD' if rate is not None and rate >= K.AGREE_BAR else 'REFUTED'), 'as H66c'),
        'N5': n5v,
        'S1': (('HELD' if M and not M.get('changed_reading') else 'REFUTED'), 'readings moved since b630`s bank %s' % M.get('changed_reading')),
        'S2': (('HELD' if P and P.get('at_pin') == P.get('items') == 60 else 'REFUTED'), 'the packet`s statements read at their pins %s of %s' % (
            P.get('at_pin'), P.get('items'))),
        'S3': (('HELD' if A and not [p for p in pairs if 'DEF' in p.split(' -> ')] else 'REFUTED'), 'the disagreements by pair %s' % pairs),
        'S4': ((('HELD' if TC and not TC.get('differ') and not TC.get('only_working') and not TC.get('only_regenerated') else 'REFUTED')
                if br == 'commit' else 'NOT SCORABLE'), 'the regenerated table against the working copy: %s' % (
            ('%d rows differing' % len(TC.get('differ') or [])) if br == 'commit' else 'the hold branch, no regeneration by an edited generator')),
        'S5': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the one-byte control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                                     RA.get('root_copy') != RA.get('root') if RA else None)),
    }
    put_json('b632_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


def _cell_names():
    T = _head_table()
    return set(r['name'] for r in T['rows'] if r.get('provenance') == 'cell')


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b632 — lane three, act fifty-nine under (R242): the E0 rule’s grades on the ungraded terminal rows with provenance, a '
              'second reader on sixty before the push; the public page’s apostrophes, the record tool’s writer and the b596 case (9) repaired')


def _title_entry():
    M, A = jx(K.MOVES.replace('.txt', '.json')), jx(K.AGREEMENT.replace('.txt', '.json'))
    gr = M.get('grades') or {}
    return ('## The E0 rule’s grades on %d terminal rows with provenance: %d DERIVES, %d INTERFACES on %d named premises, %d DEF; the second '
            'reader at %s on sixty; the table %s' % (M.get('moved') or 0, gr.get('DERIVES', 0), gr.get('INTERFACES', 0), len(M.get('named') or {}),
                                                     gr.get('DEF', 0), ('%.2f' % A['rate']) if A.get('rate') is not None else 'unread',
                                                     'committed' if A.get('branch') == 'commit' else 'held'))


def _finding_text():
    S, rl, M, A = (jl(n) for n in ('b632_scores.json', 'b632_record_lines.json', K.MOVES.replace('.txt', '.json'), K.AGREEMENT.replace('.txt', '.json')))
    J, P = jl('b632_act_root.json'), jx('b632_packet_scan.json')
    PZ, PX, TC = jx('b632_page_zeta.json'), jx('b632_page_chi.json'), jx('b632_table_compare.json')
    gr = M.get('grades') or {}
    t = _title_entry()
    commit = A.get('branch') == 'commit'
    tab = (('The working table was committed by its generator: tools/terminal_table.py edited on the commit branch by the author’s answer '
            'before the seal, the rule now reading every row no ledger cell grades, the regenerated table compared with the working copy row '
            'by row (%d rows differing) and committed alone; tools/chain_page.py writes a rule-graded Correspondence row’s provenance in its '
            'tier cell; both pages re-emitted from fresh probes at v0.25 (the ζ page changed %s, Correspondence rows added %d; the χ page changed '
            '%s, rows added %d).' % (len(TC.get('differ') or []), PZ.get('changed'), len(PZ.get('corr_added') or []), PX.get('changed'),
                                     len(PX.get('corr_added') or [])))
           if commit else
           ('The table was not committed: the agreement stood below the bar, the working copy is banked (relay data/%s) and the '
            'disagreements go to the author’s ruling; both pages untouched.' % K.WORKING))
    e = ['', t, '',
         '*Filed at b632 on the author’s ruling `(R242)` and the author’s two answers before the seal. Banks: relay `data/b632_rule_moves.txt`, '
         '`data/b632_key.txt`, `data/b632_packet_scan.txt`, `data/b632_agreement.txt`, `data/b632_act_root.txt`, `data/b632_author_answers.txt`. '
         'Nothing deposits.*', '',
         '**The rule’s grades** (`(R242)`(3) part one, W-ORD-TABLE-RULE-GRADES, OPEN_TRAILS :13133): b630’s readings of the 1,799 ungraded '
         'rows (relay data/b630_table_rule_readings.txt, sha256 %s) re-read against the table at relay HEAD; %d rows still without a grade '
         'and with a statement the rule reads took it, provenance rule -- %d DERIVES, %d INTERFACES, %d DEF, %d ENCODES-CONCLUSION -- every '
         'statement read at its pin by git; no reading moved since the bank; no cell-graded row moved. The INTERFACES rows rest on %d named '
         'premises, each printed with its count, and %d premise binders that name no premise (a variable the statement binds, or a bare '
         'relation). H66a %s, H66b %s, H66d %s.' % ((M.get('input') or {}).get('sha256'), M.get('moved'), gr.get('DERIVES', 0), gr.get('INTERFACES', 0),
                                                    gr.get('DEF', 0), gr.get('ENCODES-CONCLUSION', 0), len(M.get('named') or {}),
                                                    len(M.get('unnamed') or []), S['H66a'][0], S['H66b'][0], S['H66d'][0]), '',
         '**The second reader** (`(R242)`(3), the form of OPEN_TRAILS :12212 as amended at :12839 and :12863): sixty moved rows, thirty from '
         'each of %s, seed %d, each statement at its pin with the grade withheld (grade words in the packet %d, act numbers %d, no-disclosure '
         'hits %d); a fresh session read the packet and wrote its bank; keyed back, it agrees on %d of %d, %.4f against 0.85 (relay '
         'data/b632_agreement.txt). H66c %s.' % (' and '.join(P.get('top') or []), K.SEED, len(P.get('grade_words') or []),
                                                  len(P.get('act_numbers') or []), sum((P.get('nd') or {}).values()), A.get('agree'), A.get('items'),
                                                  A.get('rate') or 0.0, S['H66c'][0]), '',
         '**The table and the pages.** ' + tab, '',
         '**The repairs** (`(R242)`(2)): the χ page’s backmatter with plain apostrophes (PLACE-papers 62ab6f4); the record tool’s findings '
         'writer restored with a scratch-copy test (relay 66dfb8ca); test_chain_page_b596.py case (9) frozen to its pin; the test-pin line '
         'standing (OPEN_TRAILS :%d); b631 at its weight (FINDINGS :%d).' % (rl['lines'][1]['line'], rl['lines'][0]['line']), '',
         '**The root.** b632 over %d repositories, %d tags and %d banks; its chain verified inside the suite.' % (
             len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b630’s banked readings (FINDINGS :7657) at the table they were made '
         'for, and b620’s second-reader form (FINDINGS :7422), whose row agreement of 0.567 it meets with statements and not cited lines; '
         'it is re-read by every page whose Correspondence the rule now fills. It strengthens the programme’s offering of a table whose every '
         'grade names its source -- a ledger cell or the shared rule -- with a reader outside the acts checking the rule on a sample.', '',
         '**Next.** Per `(R242)`(4): b633, the author’s word pending -- the deposit preparations of the (R110) route, the census at its next '
         'version with the kernel column and the new faces, or W-ORD-GATE-FROM-ELABORATOR. The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds or locates any zero; a rule grade reads a statement’s binders and '
         'confers nothing on a ledger.*', '']
    return t, NL.join(e)


FOR_AUTHOR = ('(1) the record tool’s writer restored in this act’s record tool, carried from b631’s and committed alone with its test; '
              '(2) plain apostrophes read as the page’s own ASCII form (eight possessives on the χ page, no curly one); (3) “its statement at '
              'its pin” read as the table’s statement at the commit the table read it (its repository head), the cited pin printed beside it '
              'where a row carries one; (4) the named premise read as the head of a premise’s type, its last dotted component, a variable '
              'the statement binds or a bare relation counted apart; (5) the packet’s grade vocabulary placed in the prompt and not the '
              'packet, the rule’s text quoted with its act and ruling citations masked; the kernel’s own B-form namespaces printed as they '
              'stand; (6) the b630 test’s case (7), which encodes the retired baseline condition, on the commit branch as the author’s answer '
              'leaves it; (7) test_chain_page_b630.py failing at step zero (its list at v0.24 against the kernel at v0.25), carried')


def _next_lines():
    return ['b633 names no kernel terminal; the author’s word chooses among the deposit preparations of the (R110) route, the census’s next '
            'version and W-ORD-GATE-FROM-ELABORATOR']


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b632_scores.json', 'b632_findings.json', 'b632_record_lines.json', 'b632_act_root.json'))
    A = jx(K.AGREEMENT.replace('.txt', '.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b632_author_answers.txt'), re.M))
    rows_ = ['', TRAIL_HEAD, '',
             '**(R242) ratified.** (1) b631 at its weight. (2) The housekeeping: the χ page’s apostrophes, the record tool’s writer, the b596 '
             'case (9) frozen, the test-pin line. (3) W-ORD-TABLE-RULE-GRADES with the second reader. (4) The act after: b633.', '',
             '**Entered:** FINDINGS.md:%d (b631’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the test-pin line, standing); this record.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line']), '',
             '**The branch:** the second reader at %s on sixty -- %s.' % (('%.4f' % A['rate']) if A.get('rate') is not None else 'unread',
                                                                         'the table committed and both pages re-emitted' if A.get('branch') == 'commit'
                                                                         else 'the table held, the disagreements to the author’s ruling'), '',
             '**Act root:** b632 `%s` (previous `%s`, b631’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**Prompts to the author:** %d (relay data/b632_author_answers.txt)%s.' % (
                 n_ans, (': ' + ' / '.join(_elide(answer_of(i))[:400] for i in range(n_ans))) if n_ans else ''), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b632_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R242)`(4), b633 on the author’s word: the deposit preparations of the (R110) route, the census at its next version, '
             'or W-ORD-GATE-FROM-ELABORATOR; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b632_scores.json')
    L = ['=' * 104, 'b632 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H66a-H66d, (R242)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H66 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d ; NOT SCORABLE %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS),
                                               sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
                                               sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK),
                                               sum(S[k][0] == 'NOT SCORABLE' for k in SK)), '']
    L += rd('b632_defects.txt').rstrip(NL).split(NL)
    put_txt('b632_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b632_scores.json', 'b632_findings.json', 'b632_trail.json', 'b632_record_lines.json', 'b632_act_root.json'))
    A = jx(K.AGREEMENT.replace('.txt', '.json'))
    L = ['b632 -- THE COMPONENTS, BANKED UNDER (R242).', '',
         '### COMPONENT 0 : the process listing ; b631`s closing push-out relay %s ; push-b631* branches deleted by name (data/b632_branches.txt) ; '
         'the record tool`s writer relay 66dfb8ca ; the χ page`s apostrophes PLACE-papers 62ab6f4 ; every test file under tools/ run '
         '(data/b632_tests_stepzero.txt) ; the suite run at HEAD before the face (data/b632_arms_prerun.txt) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b631`s weight FINDINGS :%d ; the test-pin line OPEN_TRAILS :%d ; case (9) frozen (data/b632_case9_test.txt)' % (
             rl['lines'][0]['line'], rl['lines'][1]['line']),
         '### COMPONENT 2 : data/b632_rule_moves.txt ; data/b632_table_working.json ; H66a %s, H66b %s, H66d %s' % (S['H66a'][0], S['H66b'][0], S['H66d'][0]),
         '### COMPONENT 3 : data/b632_reader_packet/ ; data/b632_key.txt ; data/b632_reader_prompt.txt ; data/b632_packet_scan.txt ; the hold',
         '### COMPONENT 4 : data/b632_reader_answers.txt ; data/b632_agreement.txt ; H66c %s ; the branch %s' % (S['H66c'][0], A.get('branch')),
         '### COMPONENT 5 : %s ; the root %s' % ('the generator`s edit, the table, the page generator`s edit, the probes and both pages' if A.get('branch') == 'commit'
                                               else 'the working copy banked, the pages untouched', J['root'][:16]),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b633 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b632_components.txt', L)


def findings(*a):
    """### (R242)(2): THE FINDINGS WRITER, RESTORED. b630's body (relay tools/b630_record.py :1051-:1066 at e99c6de4), which b631's
    ### assembly dropped (b631's defect (j)); the entry is guarded for table cells, TECHNE text and stems, refused if its title stands,
    ### appended through b566's guarded append_to and its line banked. Tested on a scratch copy by tools/test_record_findings_b632.py."""
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
    put_json('b632_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
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
    put_json('b632_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b632_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-06 by b632 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b632_defects.json -- NOTHING WRITTEN')
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
    put_json('b632_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b632_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
