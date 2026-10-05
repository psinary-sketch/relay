# -*- coding: utf-8 -*-
"""b624_record.py -- THE ACT'S RECORD TOOL, UNDER (R234). ### ONE SUBCOMMAND PER BANK.

### ### b624: LANE THREE, ACT FIFTY-ONE -- THE E0 GATE'S READING OF INDUCTION STEPS, WITH ITS TEST AND THE χ PAGE RE-EMITTED; THE
### ACT ROOT CHAINED FROM THIS ACT AND VERIFIED BY A SUITE ARM.
### Subcommands write only `data/b624_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads (b623's defect (b), repaired: every bank is read from relay data). Banks are written by
### encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`. The data is tools/b624_worklist.py. No
### platform call; no Lean call: the pages are re-emitted from their banked probes and the headers graded as the generator reads
### them. The E0 rule as it stood before the act is read from its blob at relay PRE_RELAY, never from memory. The case counter is
### (R233)(3)'s standing form (OPEN_TRAILS :12889). The N5 scorer takes the trail record's expected line (OPEN_TRAILS :12799).
### b623's defects' sources repaired here: a housekeeping commit is found by its subject and holds the table files that moved
### (d), (f); a predicate reads the text its positive control mutates (e); dry routes writes only (b).
"""
import difflib
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b624_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/db8d87ba-3c6c-4b82-8201-6f0312a45734/scratchpad'
SESSION_ID = 'db8d87ba-3c6c-4b82-8201-6f0312a45734'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
SESSION_FROM = 0
PLANTED = SP + '/b624_planted'
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')


def _w(name):
    """### where a bank is WRITTEN: the scratchpad under `dry`, relay data otherwise."""
    return os.path.join(SP if DRY else D, name)


def _r(name):
    """### where a bank is READ: relay data, always (b623's defect (b))."""
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
_DJ = os.path.join(D, 'b624_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b624 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b624_defects.txt', L)


# ================================================================================ THE CASE COUNTER, (R233)(3)'s standing form
def count_cases(text, case_re=None):
    """### a test's cases are the lines its own case pattern matches, never its summary lines (OPEN_TRAILS :12889)."""
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


COUNT_CASE = r'^  \(\d+\) '


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the form, the precedence order, the act root, the quantifier column, the E0 induction work-order, the authority '
         'order and the build clause, the N5 line, b623`s record lines, record and correction', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12210, 12228, 12266, 12354, 12356, 12436, 12438, 12799] + list(range(12887, 12918)), 1500),
        ('relay tools/e0_rule.py: the domain pattern, the binder pattern, conclusion and the grade function', RELAY, PRE_RELAY,
         'tools/e0_rule.py', [41, 51, 64, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172], 300),
        ('relay tools/test_e0_rule.py, whole', RELAY, PRE_RELAY, 'tools/test_e0_rule.py', ('ALL',), 260),
        ('relay tools/chain_page.py: the header reader and the E0 call', RELAY, PRE_RELAY, 'tools/chain_page.py', [326, 327, 331, 806, 811], 300),
        ('SIDE-explicit-formula v0.21: finsetSum_insert, finsetSum_productLemma and its proof head, family_theorem', K.KER, 'v0.21',
         'SIDEExplicitFormula/Schema/Family.lean', [130, 131, 132, 136, 137, 138, 142, 143, 213], 300),
        ('SIDE-explicit-formula v0.21: power_contDiff, proved by match arms', K.KER, 'v0.21', 'SIDEExplicitFormula/PowerWindow.lean',
         [139, 140, 141, 142, 143, 146], 300),
        ('the χ page`s finsetSum_insert row', PP, PRE_PP, K.DIR_PAGE, ('GREP', r'finsetSum_insert'), 300),
        ('the census v0.4`s kernel column head', PP, PRE_PP, 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md', [41, 43], 400),
        ('relay data/b623_tags.txt`s count line', RELAY, PRE_RELAY, 'data/b623_tags.txt', ('GREP', r'^### ### \*\*TAGS'), 400),
        ('relay data/b622_unclassified.txt: the proposals', RELAY, PRE_RELAY, 'data/b622_unclassified.txt', ('GREP', r'THE SEAT`S PROPOSAL'), 200),
        ('relay tools/mirror_build.ps1: MANIFEST`s form', RELAY, PRE_RELAY, 'tools/mirror_build.ps1', [3, 71, 73, 116, 117, 118, 119, 120], 200),
        ('relay data/b623_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b623_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b624 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b624_reads.txt', L)


def act_from():
    """### the transcript line at which this act's ferry was pasted (the first user message carrying `RULING (R234) BEGIN`): the
    ### session carried b623 before it, so the act's prompts are those after this line."""
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R234) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


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
    since = [c for c in calls if c[0] > act_from()]
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b624 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b624_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
         'SIDE-structural-error-correction')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7', 'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab'}


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
    put_json('b624_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ COMPONENT 1: THE RECORD LINES
B623_ENTRY = '## The unpushed tags: 9 pushed by citation and 3 recorded local across nine kernels'
W_HEAD = '*Appended 2026-10-05 by b624 to b623’s entry (:%d), under `(R234)`(1) -- b623 AT ITS WEIGHT:*'
R_HEAD = '*Appended 2026-10-05 by b624 to %s (:%d), under `(R234)`(1) -- b623’S READING %s, CONFIRMED AS PRINTED, BESIDE THE CLAUSE IT RESOLVES:*'
M_HEAD = '*Appended 2026-10-05 by b624 to W-ORD-ACT-ROOT (:%d), under the author’s answer before b624’s seal -- THE ACT ROOT IN MANIFEST, STANDING:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry, ot_lines):
    S = {k: v[0] for k, v in json.loads(_rel('b623_scores.json')).items()}
    pre, post = _count_bank(_rel('b623_checks.txt')), _count_bank(_rel('b623_checks_postpush.txt'))
    DJ = json.loads(_rel('b623_defects.json'))
    allv = lambda ks, w: w if all(S[k] == w for k in ks) else str([S[k] for k in ks])   # noqa: E731
    return ('\n%s the twelve unpushed tags listed with kernel, SHA, remote and citations (relay data/b623_tags.txt); nine cited by a ledger '
            'and pushed one at a time by push_gated.sh in its existing-tag mode, the peeled SHA read back equal at each remote; three cited '
            'by no ledger and recorded local in their kernels’ housekeeping lists; no tag moved or re-pointed; REGISTRY’s row note :628 '
            'corrected by a dated row update in its own form (:1072). SIDE-structural-error-correction’s AxiomCheck module built at the '
            'hold, detached and watched, tagged v0.2.2 = 6bf19ab: 62 declarations printed, 34 theorems within the standard three, no '
            'sorryAx; the terminal table regenerated with the 62 rows, no grade moved elsewhere; b557’s tier bank re-read against them. '
            'The record tool’s count repair with its planted-summary test (relay 72a0c117), committed alone after the seal. The four '
            'work-orders at OPEN_TRAILS :12891-:12897; the offering-line arm 29 of 29. H57a-H57d %s; N1-N4 %s; N5 REFUTED in its letter. '
            '**N5, ruled, `(R234)`(1):** push_gated.sh gained its existing-tag mode after b623’s seal by the author’s answer before it, an '
            'instrument edit outside N5’s file list, the ferry having assumed the mode existed -- the navigator’s; the edit ratified as '
            'the act’s one necessary instrument edit (relay 40f13d5f); the ruling’s “before the seal” the navigator’s, the edit having '
            'landed after the lock as the answer ordered. The suite %d of %d before the push and %d of %d after it, by the '
            'seat’s defects (d) and (e), each claim tested directly and holding; defects (a)-(f) the seat’s, as relay data/b623_defects.txt '
            'records them (%d entries). FINDINGS :7490, :7492; OPEN_TRAILS :12887-:12917; relay 884d0848, PLACE-papers 271de07 (relay '
            'data/b623_closing_push_out.txt). **Confirmed, `(R234)`(1):** the five readings b623 resolved, each as printed, re-printed '
            'beside the clause it resolves at OPEN_TRAILS :%d-:%d. Nothing deposited; no kernel file edited outside the tagged artefact '
            'branch.\n' % (W_HEAD % entry, allv(('H57a', 'H57b', 'H57c', 'H57d'), 'HOLDS').replace('HOLDS', 'HOLD'), allv(('N1', 'N2', 'N3', 'N4'), 'HELD'),
                            pre[0], pre[1], post[0], post[1], len(DJ['defects']), ot_lines[0], ot_lines[4]))


def _reading(i, rd_):
    line, what, key = K.READINGS[i]
    return '\n%s %s %s, as b623’s record printed it (OPEN_TRAILS :12899); confirmed by the author, `(R234)`(1), and struck or kept on its own.\n' % (
        R_HEAD % (what, line, key), key, rd_[key])


def _manifest(ar_line):
    return ('\n%s every mirror build from b624 on adds one line to MANIFEST in its stage, in MANIFEST’s own form -- “Act root: <act> <root>”, '
            'read from relay data/act_roots.txt’s last line -- before the zip closes, by b614’s stage pattern, the builder (relay '
            'tools/mirror_build.ps1) unedited. No MANIFEST is written by b624, which builds no mirror; the root lives in relay '
            'data/act_roots.txt and the trail record. The ferry’s “MANIFEST’s refresh line added in its own form” assumed a standing '
            'file -- the navigator’s. Editing a built zip’s MANIFEST is struck: a banked digest is not re-banked to accommodate an edit.\n'
            % (M_HEAD % ar_line))


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
    p = os.path.join(SP if DRY else D, 'b624_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def record_lines(*a):
    """### OPEN_TRAILS: the five readings, each beside the clause it resolves; the MANIFEST standing line (to :12210). FINDINGS: b623's
    ### weight with N5's ruling, citing them. The OPEN_TRAILS lines computed first (each append opens with a blank line)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B623_ENTRY)
    if entry != 7492:
        sys.exit('### b623`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    rd_ = K.b623_readings()
    if sorted(rd_) != ['(1)', '(2)', '(3)', '(4)', '(5)']:
        sys.exit('### THE FIVE READINGS DO NOT READ (%s) -- NOTHING WRITTEN' % sorted(rd_))
    n0 = len(lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), '')))
    ot = [(R_HEAD % (K.READINGS[i][1], K.READINGS[i][0], K.READINGS[i][2]), _reading(i, rd_)) for i in range(5)]
    ot.append((M_HEAD % K.ACT_ROOT_OT, _manifest(K.ACT_ROOT_OT)))
    want, n = [], n0
    for _h, t in ot:
        want.append(n + 2)
        n += len(t.strip(NL).split(NL)) + 1
    wt = _weight(entry, want)
    allt = wt + ''.join(t for _h, t in ot)
    bad = ledger_check(allt)
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s ; OPEN_TRAILS lines expected %s' % (
        bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', want))
    if DRY:
        print(wt)
        for _h, t in ot:
            print(t)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    for h, _t in ot:
        Q.guard_absent(Q.OT, h)
    out = []
    for (h, t), w in zip(ot, want):
        r = Q.append_to(Q.OT, t)
        got = Q.line_of(Q.OT, h)
        out.append(dict(file='OPEN_TRAILS.md', head=h, line=got, append=r))
        if got != w:
            put_json('b624_record_lines.json', dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED; FINDINGS NOT APPENDED' % (h[:60], got, w))
    r1 = Q.append_to(Q.FIND, wt)
    out.insert(0, dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r1))
    put_json('b624_record_lines.json', dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ COMPONENT 2: THE CLAUSE AND THE TEST
def e0_module(rev=None):
    """### tools/e0_rule.py at relay `rev` (None: the working file), loaded as a module of its own."""
    if rev is None:
        import e0_rule as E
        return E
    src = _show(RELAY, rev, 'tools/e0_rule.py')
    m = types.ModuleType('e0_rule_%s' % rev)
    exec(compile(src, 'e0_rule@%s' % rev, 'exec'), m.__dict__)
    return m


def e0_before(*a):
    """### the grade function and the patterns it reads, printed from tools/e0_rule.py at relay PRE_RELAY, before the edit."""
    src = _show(RELAY, PRE_RELAY, 'tools/e0_rule.py')
    sl = lines_of(src)
    keep = [i + 1 for i, l in enumerate(sl) if re.match(r'^(DOMAIN|BINDER|CLASS_PREDS) =|^def grade\(', l)]
    gi = [i + 1 for i, l in enumerate(sl) if l.startswith('def grade(')][0]
    nums = sorted(set(keep) | set(range(gi, gi + 13)))
    L = ['b624 -- COMPONENT 2: THE E0 RULE`S GRADE FUNCTION BEFORE THE EDIT, tools/e0_rule.py @ relay %s (%s; blob %s)' % (
        PRE_RELAY, utc(), g(RELAY, 'rev-parse', '%s:tools/e0_rule.py' % PRE_RELAY).strip()[:12]), '']
    L += ['    :%-4d %s' % (n, sl[n - 1]) for n in nums]
    put_txt('b624_e0_before.txt', L)


def e0_diff(*a):
    d = g(RELAY, 'diff', PRE_RELAY, '--', *K.E0_FILES)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', *K.E0_FILES)
    L = ['b624 -- COMPONENT 2: THE E0 RULE`S CLAUSE AND ITS TEST, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), '',
         '### ' + (st.rstrip(NL).split(NL)[-1].strip() if st.strip() else 'NO DIFF'), ''] + d.rstrip(NL).split(NL)
    put_txt('b624_e0_diff.txt', L)
    print(L[2])


def e0_test(*a):
    """### tools/test_e0_rule.py run with the planted directory, counted by its case pattern; run again with the rule as it stood at
    ### PRE_RELAY (its blob loaded in place of the working file) as the positive control: data/b624_e0_test.txt and .json."""
    def run(rule_dir):
        env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONPATH=(rule_dir + os.pathsep if rule_dir else '') + os.path.join(ROOT, 'tools'))
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_e0_rule.py'), PLANTED], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', env=env)
        return r.returncode, (r.stdout or '') + (r.stderr or '')
    rc, out = run(None)
    n, p = count_cases(out, COUNT_CASE)
    old = tempfile.mkdtemp()
    open(os.path.join(old, 'e0_rule.py'), 'wb').write(_show(RELAY, PRE_RELAY, 'tools/e0_rule.py').encode('utf-8'))
    shutil.copy(os.path.join(ROOT, 'tools', 'test_e0_rule.py'), os.path.join(old, 'test_e0_rule.py'))
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONPATH=os.path.join(ROOT, 'tools'))
    r2 = subprocess.run([sys.executable, os.path.join(old, 'test_e0_rule.py'), PLANTED], capture_output=True, text=True, encoding='utf-8',
                        errors='replace', env=env)
    out2 = (r2.stdout or '') + (r2.stderr or '')
    n2, p2 = count_cases(out2, COUNT_CASE)
    failed2 = [l.strip()[:4] for l in out2.split(NL) if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]
    planted = [l.strip() for l in out.split(NL) if l.strip().startswith('planted: ')]
    L = ['b624 -- COMPONENT 2: tools/test_e0_rule.py RUN AND COUNTED (%s); exit %d' % (utc(), rc), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p), '',
          '### THE POSITIVE CONTROL: the same test with tools/e0_rule.py as it stood at relay %s (exit %d): cases %d, passing %d, failing %s' % (
              PRE_RELAY, r2.returncode, n2, p2, failed2)]
    put_txt('b624_e0_test.txt', L)
    put_json('b624_e0_test.json', dict(at=utc(), rc=rc, cases=n, passing=p, planted=planted, control=dict(rc=r2.returncode, cases=n2, passing=p2,
                                                                                                           failing=failed2)))
    print(L[-3])
    print(L[-1])


def _headers(rule):
    """### both pages re-emitted from their banked probes through the generator with `rule` as its E0 module: ({(page, node): (header,
    ### kind)}, {page: emitted text})."""
    import chain_page as CP
    seen, pages = {}, {}
    save = CP.E0
    CP.E0 = rule
    try:
        for k in ('zeta', 'chi'):
            rc, pg, meta, _log = CP.build(os.path.join(D, K.NODES[k]), tempfile.mkdtemp(), os.path.join(D, K.PROBE[k]))
            pages[k] = pg if rc == 0 else None
            for n, c in (meta or {}).get('cells', {}).items():
                if c.get('source_header') is not None:
                    seen[(k, n)] = (c['source_header'], c['kind'])
    finally:
        CP.E0 = save
    return seen, pages


def e0_nodes(*a):
    """### every header both pages grade, read through the generator at its pins, graded by the rule before (relay PRE_RELAY) and
    ### after (the working file): the grades and the premise lists that move; beside them every page node whose table grade (the
    ### ledger's, relay data/terminal_table.json) differs from the rule's read, printed for the author's ruling (data/b624_e0_nodes.txt
    ### and .json)."""
    old, new = e0_module(PRE_RELAY), e0_module(None)
    seen, _p = _headers(new)
    heads = {}
    for (k, n), (h, kind) in seen.items():
        heads.setdefault(n, (h, kind, k))
    rows = []
    for n, (h, kind, k) in sorted(heads.items()):
        kk = 'theorem' if kind == 'theorem' else 'def'
        a, b = old.grade(h, kk), new.grade(h, kk)
        rows.append(dict(name=n, page=k, kind=kind, before=a[0], after=b[0], why_before=a[1], why_after=b[1],
                         binders_before=[x for x, _t in a[2]], binders_after=[x for x, _t in b[2]]))
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    tg = {}
    for r in T['rows']:
        tg.setdefault(r['name'], r['grade'])
    dis = [dict(name=r['name'], page=r['page'], table=tg[r['name']], rule=r['after']) for r in rows
           if r['kind'] == 'theorem' and tg.get(r['name']) not in (None, 'UNGRADED') and tg[r['name']].split('-')[0] != r['after'].split('-')[0]]
    moved = [r for r in rows if r['before'] != r['after']]
    premv = [r for r in rows if r['before'] == r['after'] and r['why_before'] != r['why_after']]
    named = {n: [r for r in rows if r['name'] == n] for n, _f, _l in K.CLAUSE_NODES}
    L = ['b624 -- COMPONENT 2: EVERY NODE THE PAGES GRADE, READ AT ITS PIN BY THE GENERATOR, GRADED BY THE E0 RULE BEFORE (relay %s) AND '
         'AFTER THE CLAUSE (%s)' % (PRE_RELAY, utc()), '',
         '### distinct nodes graded %d ; grades moved %d ; premise lists moved with the grade unmoved %d' % (len(rows), len(moved), len(premv)), '']
    L += ['### THE NAMED NODES:'] + ['  %-62s %s -> %s ; binders %s -> %s' % (n, (v[0]['before'] if v else 'NOT ON A PAGE'), (v[0]['after'] if v else ''),
                                                                         (v[0]['binders_before'] if v else ''), (v[0]['binders_after'] if v else ''))
                                       for n, v in named.items()]
    L += ['', '### GRADES MOVED:'] + ['  %-62s %s -> %s (%s)' % (r['name'], r['before'], r['after'], r['why_after'][:100]) for r in moved]
    L += ['', '### PREMISE LISTS MOVED, THE GRADE UNMOVED:'] + ['  %-62s %s: %s -> %s' % (r['name'], r['after'], r['why_before'][:90], r['why_after'][:90])
                                                          for r in premv]
    L += ['', '### FOR THE AUTHOR`S RULING -- PAGE NODES WHOSE TABLE GRADE (FROM LEDGER CELLS) DIFFERS FROM THE RULE`S READ AFTER THE CLAUSE:']
    L += ['  %-62s %-5s table %s ; rule %s' % (x['name'], x['page'], x['table'], x['rule']) for x in dis] or ['  NONE']
    L += ['', '### ### **NODES %d ; GRADES MOVED %d (%s) ; ENCODES-CONCLUSION READ %d ; DISAGREEMENTS PRINTED %d.**' % (
        len(rows), len(moved), ', '.join(r['name'].split('.')[-1] for r in moved) or 'none', sum(1 for r in rows if r['after'] == 'ENCODES-CONCLUSION'),
        len(dis))]
    put_txt('b624_e0_nodes.txt', L)
    put_json('b624_e0_nodes.json', dict(at=utc(), rows=rows, moved=[r['name'] for r in moved], premise_moved=[r['name'] for r in premv],
                                        disagreements=dis))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE TABLE AND THE PAGE
def table(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    L = ['b624 -- COMPONENT 3: THE TERMINAL TABLE REGENERATED AFTER THE CLAUSE (%s); exit %d' % (utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d %s' % (len(diff.get('added') or []), len(diff.get('gone') or []),
                                                                         len(diff.get('changed') or []), diff.get('changed') or ''),
         '### the table files that moved against relay HEAD: %s' % (moved or 'NONE'),
         '', '### ### **THE GRADE COLUMN`S DIFF : %s.**' % ('EMPTY' if not (diff.get('changed') or diff.get('added') or diff.get('gone')) else 'NOT EMPTY')]
    put_txt('b624_table.txt', L)
    put_json('b624_table.json', dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                     changed=diff.get('changed') or [], files_moved=moved))
    print(L[-1])


def _grade_cells(text):
    """### a page's grade column: {name: grade} from its node lines' and its correspondence rows' grade cells."""
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


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; its grade cells compared to the prior emission (the
    ### page at HEAD); written only when it changed (data/b624_page_<k>.json)."""
    import chain_page as CP
    if k not in K.NODES:
        sys.exit('usage: page zeta|chi')
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b624_%s' % k), os.path.join(D, K.PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b624_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = _grade_cells(prev.decode('utf-8')), _grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))
    put_json('b624_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s' % (k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE'))
    for x in dl:
        print('    ' + x[:240])


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b624 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s), after the clause' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b624_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b624_page_arms.txt', L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 4: THE ACT ROOT
ROOT_EXCLUDE = re.compile(r'^b624_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|root_test.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    """### the data/ banks the act wrote and names in its root: every relay data/b624_* bank on disk now, but those a later step
    ### rewrites (the defects, scores, desk, record, suite runs, closing and the root's own banks)."""
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b624_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root_test(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_act_root.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out, COUNT_CASE)
    L = ['b624 -- COMPONENT 4: tools/test_act_root.py RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt('b624_root_test.txt', L)
    put_json('b624_root_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p))
    print(L[-1])


def root(*a):
    """### tools/act_root.py compute b624 over the act's banks, written: data/act_roots.txt (+1 line), data/b624_act_root.json and .txt."""
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b624'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the act-root arm run by the record tool after the root: tools/act_root.py's verify over data/act_roots.txt (one ls-remote per
    ### repository), and the one-byte control -- a copy of one named bank with one byte changed, the root recomputed over the copy,
    ### the result different (data/b624_root_arm.txt and .json)."""
    import act_root as AR
    res = AR.verify()
    J = jl('b624_act_root.json')
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
    L = ['b624 -- COMPONENT 4: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s (%s) with its first byte changed; the root recomputed over the copy %s ; over the bank %s '
              '(the banked root %s) ; the copy`s root differs %s' % (bank, cp.replace('\\', '/'), r2, same, J['root'], r2 != J['root']),
          '### ls-remote calls by the arm, per repository: %d repositories, at most %d each' % (len(AR.LSR), max(AR.LSR.values()) if AR.LSR else 0),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b624_root_arm.txt', L)
    put_json('b624_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, copy=cp, root_copy=r2, root_recomputed=same,
                                        root=J['root'], lsr=dict(AR.LSR)))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md', K.PAGE)
HKEYS = ('H58a', 'H58b', 'H58c', 'H58d')
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


def _by_subject(commits, prefix):
    """### b623's defects (d) and (f), repaired: a commit found by its subject, its files read from it."""
    return [h for h, s in commits if s.startswith(prefix)]


def _epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _lock():
    m = re.search(r'locked at \(UTC\) : (\S+)', rd('b624_registration_2026-10-05.txt') or '')
    return _epoch(m.group(1)) if m else None


def _after_lock(repo, h):
    lk = _lock()
    return lk is not None and int(g(repo, 'show', '-s', '--format=%ct', h).strip() or 0) > lk


def n5(trail_line=None, ot=None, *a):
    """### N5, scored by its letter: nothing deposits; no kernel touched; no instrument edited before the seal beyond the suite-source
    ### repairs; no file written beyond the reader edit and its tests, the two planted scratch modules, the regenerated table, the
    ### re-emitted page, act_root.py and its test, data/act_roots.txt, MANIFEST's one line (none written, by the author's answer), the
    ### record lines and the trails. The trail record's expected line a parameter (OPEN_TRAILS :12799); a pending record is OT's write."""
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
    face = jl('b624_kernels_face.json')['kernels']
    now = kern_state(list(face))
    kern_ok = now == {k: list(v) for k, v in face.items()}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if jx('b624_page_%s.json' % k).get('changed')]
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages)
    rc = _relay_commits()
    lk = _lock()
    before_lock = [h for h, s in rc if lk is not None and int(g(RELAY, 'show', '-s', '--format=%ct', h).strip() or 0) <= lk]
    inst_before = [f for h in before_lock for f in _files(h, RELAY) if f.startswith('tools/') and not os.path.basename(f).startswith('b624_')]
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith(('b624_', 'audit_b624_', 'terminal_table'))
                              and x != 'data/b623_closing_push_out.txt'))
    allowed = set(K.E0_FILES) | set(K.ROOT_FILES) | {'data/act_roots.txt'}
    beyond = [x for x in relay_beyond if x not in allowed]
    ok = kern_ok and pp_ch == want_pp and not beyond and not inst_before and rec_ok
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel read unmoved (main, tags by peel, branches, status) %s; PLACE-papers %s (wanted %s); %s; instruments '
            'committed before the lock %s; relay beyond the act`s banks and the table: %s (allowed: the reader and its test, act_root.py and its '
            'test, data/act_roots.txt); the planted modules in the scratchpad; MANIFEST unwritten by the author`s answer' % (
                kern_ok, pp_ch, want_pp, rec_state, inst_before or 'NONE', beyond or 'NONE'))


def scores(*a):
    E, N, TB = jx('b624_e0_test.json'), jx('b624_e0_nodes.json'), jx('b624_table.json')
    PZ, PX, RA, RT = jx('b624_page_zeta.json'), jx('b624_page_chi.json'), jx('b624_root_arm.json'), jx('b624_root_test.json')
    arms = rd('b624_page_arms.txt')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    rows = {r['name']: r for r in N.get('rows') or []}
    pl, ins = rows.get(K.CLAUSE_NODES[0][0], {}), rows.get(K.CLAUSE_NODES[1][0], {})
    et = rd('b624_e0_test.txt')
    case = lambda n: bool(re.search(r'^  \(%d\) .* PASS$' % n, et, re.M))   # noqa: E731
    h58a = 'HOLDS' if pl.get('after') == ins.get('after') == 'DERIVES' and pl.get('before') == pl.get('after') and ins.get('before') == ins.get('after') else 'REFUTED'
    h58b = 'HOLDS' if case(10) and case(11) and case(12) else 'REFUTED'
    h58c = 'HOLDS' if TB and not (TB.get('changed') or TB.get('added') or TB.get('gone')) else 'REFUTED'
    agree = [v for v in RA.get('verify') or []]
    h58d = 'HOLDS' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and agree and all(v[1] == 'AGREE' for v in agree) else 'REFUTED'
    rc = _relay_commits()
    e0c = _alone(RELAY, list(K.E0_FILES), rc)
    arc = _alone(RELAY, list(K.ROOT_FILES), rc)
    arms_ok = 'PAGE ARMS PASSING : 2 of 2' in arms and 'PASSING : 2 of 2.**' in arms.split('PAGE ARMS PASSING')[-1]
    cells_moved = (PX.get('grade_cells_moved') or []) + (PZ.get('grade_cells_moved') or [])
    S = {
        'H58a': (h58a, 'finsetSum_productLemma %s -> %s; finsetSum_insert %s -> %s' % (pl.get('before'), pl.get('after'), ins.get('before'), ins.get('after'))),
        'H58b': (h58b, 'the planted interface case (10) %s, the planted shell (11) %s, the similar Prop (12) %s' % (case(10), case(11), case(12))),
        'H58c': (h58c, 'the table`s regeneration: added %d, gone %d, changed %d' % (len(TB.get('added') or []), len(TB.get('gone') or []), len(TB.get('changed') or []))),
        'H58d': (h58d, 'the arm`s verify %s; the recomputed root equals the tool`s %s; the one-byte control changes it %s' % (
            [(v[0], v[1]) for v in agree], RA.get('root_recomputed') == RA.get('root'), RA.get('root_copy') != RA.get('root'))),
        'N1': (('HELD' if pl.get('after') == ins.get('after') == 'DERIVES' and not N.get('moved') else 'REFUTED'),
               'the two lemmas read %s and %s; kernel nodes whose grade moved under the clause %s' % (pl.get('after'), ins.get('after'), N.get('moved'))),
        'N2': (('HELD' if case(10) and case(11) else 'REFUTED'), 'the planted interface on exactly one premise %s; the planted shell ENCODES-CONCLUSION %s' % (case(10), case(11))),
        'N3': (('HELD' if h58c == 'HOLDS' and not cells_moved and PX.get('rc') == 0 else 'REFUTED'),
               'the table`s grade column diff empty %s; the χ page`s grade cells moved %s' % (h58c == 'HOLDS', cells_moved or 'NONE')),
        'N4': (('HELD' if h58d == 'HOLDS' else 'REFUTED'), 'the recomputed root equals the tool`s %s; the one-byte control changes it %s' % (
            RA.get('root_recomputed') == RA.get('root'), RA.get('root_copy') != RA.get('root'))),
        'N5': n5v,
        'S1': (('HELD' if len(e0c) == 1 and _after_lock(RELAY, e0c[0]) and E.get('cases') and E.get('cases') == E.get('passing')
                and sorted(E.get('control', {}).get('failing') or []) == ['(11)', '(8) ', '(9) '] else 'REFUTED'),
               'the rule and its test in one relay commit of their own %s after the lock; the test %s of %s; the rule as it stood fails %s' % (
                   e0c, E.get('passing'), E.get('cases'), (E.get('control') or {}).get('failing'))),
        'S2': (('HELD' if N.get('moved') == [K.CLAUSE_NODES[1][0]] else 'REFUTED'), 'grades moved over every page node: %s' % N.get('moved')),
        'S3': (('HELD' if h58c == 'HOLDS' and not cells_moved else 'REFUTED'), 'the table unmoved %s; the pages` grade cells moved %s' % (h58c, cells_moved or 'NONE')),
        'S4': (('HELD' if len(arc) == 1 and RT.get('cases') and RT.get('cases') == RT.get('passing') and h58d == 'HOLDS' else 'REFUTED'),
               'act_root.py and its test in one relay commit of their own %s; the test %s of %s; the arm %s' % (arc, RT.get('passing'), RT.get('cases'), h58d)),
        'S5': (('HELD' if len(jx('b624_record_lines.json').get('lines') or []) == 7 else 'REFUTED'),
               'the record lines: %s' % [(x['file'], x['line']) for x in jx('b624_record_lines.json').get('lines') or []]),
    }
    put_json('b624_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 5: THE RECORD
TRAIL_HEAD = ('### b624 — lane three, act fifty-one under (R234): the E0 gate at induction steps -- the statement’s binders alone, the '
              'non-membership a domain condition, the conclusion as a binder read ENCODES-CONCLUSION; the act root chained from b624')


def _title_entry():
    N, J = jx('b624_e0_nodes.json'), jx('b624_act_root.json')
    reads = J.get('reads') or {}
    return ('## The E0 gate at induction steps: hypotheses the proof introduces do not enter the grade, %d nodes re-read at v0.20 and '
            'v0.21 with %d grade moved; the act root chained from b624 over %d repositories, %d tags and %d banks, verified by one arm' % (
                len(N.get('rows') or []), len(N.get('moved') or []), len(reads.get('heads') or {}), len(reads.get('tags') or {}), len(reads.get('banks') or {})))


def _finding_text():
    S, rl, E, N, TB = (jl(n) for n in ('b624_scores.json', 'b624_record_lines.json', 'b624_e0_test.json', 'b624_e0_nodes.json', 'b624_table.json'))
    PX, J, RA = jx('b624_page_chi.json'), jl('b624_act_root.json'), jl('b624_root_arm.json')
    rc = _relay_commits()
    e0c = (_alone(RELAY, list(K.E0_FILES), rc) or ['?'])[0]
    arc = (_alone(RELAY, list(K.ROOT_FILES), rc) or ['?'])[0]
    pc = _pp_commits()
    pgc = ' '.join(h for h, s in pc if _files(h) == [K.DIR_PAGE]) or 'none'
    t = _title_entry()
    e = ['', t, '',
         '*Filed at b624 on the author’s ruling `(R234)` and the author’s three answers before the seal. Banks: relay `data/b624_e0_before.txt`, '
         '`data/b624_e0_diff.txt`, `data/b624_e0_test.txt`, `data/b624_e0_nodes.txt`, `data/b624_table.txt`, `data/b624_page_chi.json`, '
         '`data/b624_act_root.txt`, `data/b624_root_arm.txt`, `data/act_roots.txt`, `data/b624_author_answers.txt`. Nothing deposits.*', '',
         '**The clause** (`(R234)`(2), W-ORD-E0-INDUCTION, OPEN_TRAILS :12436): relay `tools/e0_rule.py` reads the grade from the statement’s '
         'binders alone -- a header handed in with a proof inside it (a proof by match arms, no `:=`) is cut where its first arm begins, so '
         'neither the arms nor the next declaration a reader ran on into is read; a non-membership is a domain condition as a membership is; '
         'a theorem one of whose explicit hypothesis binders has the conclusion itself as its type, its bound variables abstracted, reads '
         'ENCODES-CONCLUSION. Edited after the seal through the Edit tool, with its test, alone (relay %s): the test %d of %d by its case '
         'pattern, the rule as it stood failing exactly the clause’s three cases (8), (9) and (11). Read at the pins through the page '
         'generator, %d nodes: one grade moved, the step lemma’s, INTERFACES to DERIVES on its non-membership binder; the product lemma '
         'DERIVES before and after, its induction hypothesis in the proof and never read; one premise list shortened with its grade unmoved '
         '(power_contDiff, whose header ran on past its arms); no node reads ENCODES-CONCLUSION. The planted modules: the interface reads '
         'INTERFACES on its one premise, an induction in its proof; the shell reads ENCODES-CONCLUSION on an alpha-variant binder; a merely '
         'similar Prop does not. H58a %s, H58b %s.' % (e0c, E['passing'], E['cases'], len(N['rows']), S['H58a'][0], S['H58b'][0]), '',
         '**The table and the page.** The table regenerated: %s (H58c %s). The χ page re-emitted from its banked v0.21 probe: its grade '
         'cells unmoved (%s); the step lemma’s correspondence row loses its premises annotation, its grade cell keeping the ledger’s '
         'INTERFACES beside the rule’s DERIVES (PLACE-papers %s). Printed for the author’s ruling: %d page node(s) whose table grade, '
         'read from ledger cells, differs from the rule’s read -- %s.' % (
             'no row added, gone or changed' if S['H58c'][0] == 'HOLDS' else 'rows moved', S['H58c'][0], 'none' if not PX.get('grade_cells_moved') else PX['grade_cells_moved'],
             pgc, len(N['disagreements']), '; '.join('%s table %s, rule %s' % (x['name'].split('.')[-1], x['table'], x['rule']) for x in N['disagreements']) or 'none'), '',
         '**The act root** (`(R234)`(3), W-ORD-ACT-ROOT, OPEN_TRAILS :12210): relay `tools/act_root.py`, with its test (relay %s), hashes one '
         'sorted line per repository head (%d: relay, PLACE-papers and the census’s %d kernels, each confirmed by one ls-remote), per tag '
         'REGISTRY cites (%d) and per bank this act wrote (%d), then the previous root -- for b624 the empty string’s sha256. The root of b624 '
         'is `%s`, the first line of relay `data/act_roots.txt`. The arm recomputes the chain from the banks and the remotes: %s; a one-byte '
         'change to a copy of one bank changes the root. H58d %s. MANIFEST carries the root from the next mirror build on, by a standing '
         'line (OPEN_TRAILS :%d).' % (arc, len(J['reads']['heads']), len(J['reads']['heads']) - 2, len(J['reads']['tags']), len(J['reads']['banks']), J['root'],
                                      ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify']), S['H58d'][0], rl['lines'][6]['line']), '',
         '**The record lines** (`(R234)`(1)): b623’s weight at FINDINGS :%d with N5’s ruling; the five readings each beside the clause it '
         'resolves at OPEN_TRAILS :%d-:%d.' % (rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][5]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b603’s family form (:7028), whose step lemma b603’s housekeeping graded '
         'INTERFACES and b604 recorded (:7058, OPEN_TRAILS :12438); it answers b591’s existential clause (OPEN_TRAILS :12188) with its '
         'counterpart for the statement’s end; and it gives b593’s priced root (OPEN_TRAILS :12210) its first link. It strengthens the '
         'programme’s offering of a grade a reader can recompute from a statement alone, and of a record whose every act can be checked '
         'against the remotes by one hash.', '',
         '**Next.** Per `(R234)`(5): b625, W-ORD-VENDOR-FINALMULT. The author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; nothing here is a statement about RH, GRH or any zero.*', '']
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
    put_json('b624_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) the clause’s “hypotheses the proof introduces” read in the rule as the header cut where a proof begins inside it (a '
              'match arm), since a proof after `:=` never reached the rule; (2) “a premise bundle by its strongest field” read for the grade '
              'as one named premise, INTERFACES on the bundle whatever its fields’ shapes, no grade moved by it; (3) the act root’s '
              'repositories the census’s kernel column (32 kernels, SIDE-explicit-formula not among them) with relay and PLACE-papers; its tags '
              'every version REGISTRY names beside a census kernel that the clone carries, by b611’s matcher and the cell rule; its banks every '
              'b624 bank written before the root and not rewritten after; (4) relay and PLACE-papers pushed once before the root, so each head '
              'the root names is at its remote; (5) the act-root arm a source of the suite, printed per act and counted by the record tool, '
              'not on this face, by the ferry')


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b624_scores.json', 'b624_findings.json', 'b624_record_lines.json', 'b624_act_root.json'))
    N = jl('b624_e0_nodes.json')
    rc = _relay_commits()
    e0c = (_alone(RELAY, list(K.E0_FILES), rc) or ['?'])[0]
    arc = (_alone(RELAY, list(K.ROOT_FILES), rc) or ['?'])[0]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R234) ratified.** (1) b623 at its weight; its five readings confirmed; N5’s letter the navigator’s, the push_gated edit ratified. '
             '(2) W-ORD-E0-INDUCTION. (3) W-ORD-ACT-ROOT. (4) H58a-H58d. (5) The act after: b625.', '',
             '**Entered:** FINDINGS.md:%d (b623’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d-:%d (b623’s five readings, '
             'each beside its clause), :%d (the act root in MANIFEST, standing, to :12210); this record; relay tools/e0_rule.py and '
             'tools/test_e0_rule.py %s; relay tools/act_root.py and tools/test_act_root.py %s; relay data/act_roots.txt; relay data/b624_e0_nodes.txt, '
             'data/b624_act_root.txt, data/b624_root_arm.txt.' % (rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][5]['line'],
                                                                   rl['lines'][6]['line'], e0c, arc), '',
             '**Act root:** b624 `%s` (previous `%s`, the empty string’s sha256; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**The author’s three answers before the seal** (relay data/b624_author_answers.txt): the non-membership read as a domain condition '
             'beside the ruled clause, the step lemma reading DERIVES, the table keeping its ledger cells’ INTERFACES and the disagreement printed; '
             'the rule gaining ENCODES-CONCLUSION where a binder is the conclusion up to its bound variables; MANIFEST’s root line at every mirror '
             'build from now on, none written by b624. The navigator’s, recorded: the ferry’s DERIVES test beside its no-move expectation, the '
             'taxonomy’s grade named as the rule’s output, and a MANIFEST file assumed standing.', '',
             '**For the author’s ruling:** %s.' % ('; '.join('%s -- the table %s from its ledger cells, the rule %s' % (x['name'], x['table'], x['rule'])
                                                           for x in N['disagreements']) or 'no disagreement'), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b624_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R234)`(5), b625, W-ORD-VENDOR-FINALMULT (OPEN_TRAILS :12290); the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
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
    put_json('b624_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b624_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b624 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b624_defects.json -- NOTHING WRITTEN')
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
    put_json('b624_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec), head=CORR_HEAD % rec, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec))


def desk(*a):
    S = jl('b624_scores.json')
    L = ['=' * 104, 'b624 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H58a-H58d, (R234)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H58 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b624_defects.txt').rstrip(NL).split(NL)
    put_txt('b624_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b624_scores.json', 'b624_findings.json', 'b624_trail.json', 'b624_record_lines.json', 'b624_act_root.json'))
    L = ['b624 -- THE COMPONENTS, BANKED UNDER (R234).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b623`s closing push-out relay %s ; push-b623* branches deleted by name '
         '(data/b624_branches.txt) ; the kept branches untouched ; the suite, b623`s defects` sources repaired and the act-root arm a source, run at '
         'HEAD before the face (data/b624_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b623`s weight FINDINGS :%d ; the five readings OPEN_TRAILS :%d-:%d ; the MANIFEST line :%d' % (
             rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][5]['line'], rl['lines'][6]['line']),
         '### COMPONENT 2 : data/b624_e0_before.txt ; the clause data/b624_e0_diff.txt ; its test data/b624_e0_test.txt ; the nodes data/b624_e0_nodes.txt ; '
         'H58a %s, H58b %s' % (S['H58a'][0], S['H58b'][0]),
         '### COMPONENT 3 : the table data/b624_table.txt ; the χ page data/b624_page_chi.json ; page arms data/b624_page_arms.txt ; H58c %s' % S['H58c'][0],
         '### COMPONENT 4 : data/b624_root_test.txt ; the root %s (data/act_roots.txt, data/b624_act_root.txt) ; the arm data/b624_root_arm.txt ; H58d %s' % (
             J['root'][:16], S['H58d'][0]),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b625 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b624_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b624_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
