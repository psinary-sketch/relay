# -*- coding: utf-8 -*-
"""b633_record.py -- THE ACT'S RECORD TOOL, UNDER (R243). ### ONE SUBCOMMAND PER BANK.

### ### b633: LANE THREE, ACT SIXTY -- THE KEYSTONE CENSUS AT v0.5: THE KERNEL COLUMN AT THE ROOT'S LIST, THE FOUR NEW FACES, PROVENANCE
### PER CLUSTER, PHASE 2 READ AGAINST SEC, THE 42 NAMED PREMISES IN BACK MATTER; TWO PREDICATES ENTERED IN THE RULE; THE READER AND
### DELIVERY FORMS AMENDED; THE b630 TEST FROZEN.
### Subcommands write only `data/b633_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`. The data is tools/b633_worklist.py, the census reads tools/b633_census.py. No platform is called and no
### registry is read. The case counter is (R233)(3)'s. b628's full intake bank is never read here, never staged or committed.
### Carried from b632's record tool (its helpers, its root, its N5 scorer matching files by path as (R243)'s Component 0 orders); the
### act's own parts written here.
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
import b604_record as R4  # noqa: E402
import b633_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/89dd14e7-e119-4cf8-b592-ceaac809eff2/scratchpad'
SESSION_ID = '89dd14e7-e119-4cf8-b592-ceaac809eff2'
PROJECTS = 'C:/Users/echo chamber/.claude/projects'
SESSION = '%s/D--/%s.jsonl' % (PROJECTS, SESSION_ID)
TABLE_FILES = tuple(K.TABLE_FILES)
FACE = 'b633_registration_2026-10-06.txt'

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
_DJ = os.path.join(D, 'b633_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b633 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b633_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the edition form, the second-reader form and its amendment, the precedence and authority orders, the build clause, '
         'the N5 line, the criterion, W-ORD-GATE-FROM-ELABORATOR, W-ORD-BINDER-GRAMMAR, the closing form, b632`s lines and record',
         PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12228, 12354, 12356, 12799, 12839, 12863, 12955, 13000, 13002, 13028, 13193, 13195], 1500),
        ('FINDINGS: b632`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B632_ENTRY], 600),
        ('the census at v0.4, its head, its §1 head and its back matter`s heads', PP, PRE_PP, K.CEN4,
         ('GREP', r'^(#|\*v0\.|\| row \|)'), 260),
        ('relay data/b619_census.txt, b619`s bank: its parts', RELAY, PRE_RELAY, 'data/b619_census.txt', ('GREP', r'^(### PART|b619 --)'), 200),
        ('relay data/act_roots.txt: b632`s line', RELAY, PRE_RELAY, 'data/act_roots.txt', ('GREP', r'^b632 '), 200),
        ('relay tools/act_root.py: its repository list', RELAY, PRE_RELAY, 'tools/act_root.py', ('GREP', r'^def (census_kernels|registry_kernels|page_kernels|repositories)\b'), 200),
        ('relay data/b632_rule_moves.txt: the census section`s head', RELAY, PRE_RELAY, 'data/b632_rule_moves.txt', ('GREP', r'^### ### \*\*DISTINCT NAMED PREMISES'), 300),
        ('SIDE-structural-error-correction v0.2.2: its AxiomCheck, the first prints', K.SEC, K.SEC_TAG, 'AxiomCheck.lean', list(range(1, 12)), 200),
        ('relay data/b628_intake_summary.txt: its head', RELAY, PRE_RELAY, K.INTAKE[0], [1, 3, 4, 5, 7, 8, 9, 10, 11], 300),
        ('relay tools/e0_rule.py: the named restrictions and the domain criterion', RELAY, PRE_RELAY, 'tools/e0_rule.py',
         ('GREP', r'^(RESTRICTIONS = |    dict\(head=|def (restriction_case|domain_case|quantified|grade)\b)'), 200),
        ('SIDE-global-section: Alt2`s definition', K.GS, '17ce9ff', 'Core/LadderOrientationShadow.lean', [95], 200),
        ('SIDE-global-section: Alternates` definitions', K.GS, '17ce9ff', 'Core/AlternationShadow.lean', [33], 200),
        ('SIDE-global-section: Alternates` second definition', K.GS, '17ce9ff', 'Core/SignTransferShadow.lean', [47], 200),
        ('relay tools/test_chain_page_b630.py: the list and the build', RELAY, PRE_RELAY, 'tools/test_chain_page_b630.py', ('GREP', r'NODES|C\.build'), 200),
        ('relay data/b632_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b632_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ] + [('the %s synthesis: its Correspondence heading' % key, PP, PRE_PP, path, ('GREP', r'^## Correspondence'), 200) for _r_, key, path in K.PHASE2]


def reads(*a):
    L = ['b633 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    T = json.loads(_show(RELAY, PRE_RELAY, 'data/terminal_table.json'))
    pv = collections.Counter(r.get('provenance') for r in T['rows'])
    gr = collections.Counter(r['grade'] for r in T['rows'])
    L += ['', '### THE TERMINAL TABLE AT relay %s: %d rows ; provenance %s ; grades %s' % (PRE_RELAY, len(T['rows']), dict(pv), dict(gr)),
          '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b633_reads.txt', L)


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R243) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
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
    L = ['### b633 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b633_author_answers.txt', L)


def answer_of(k):
    t = rd('b633_author_answers.txt')
    qs = []
    for blk in re.split(r'^### CALL ', t, flags=re.M)[1:]:
        res = re.search(r'^RESULT \(transcript line \d+\): (.*)', blk, re.M | re.S)
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
    import banned_terms as BT
    rx = re.compile(r'(%s)' % '|'.join(re.escape(s) for s in BT.STEMS), re.I)
    return ' '.join('[a sentence elided here under the scanner’s stem rule, verbatim in the bank]' if rx.search(s) else s
                    for s in re.split(r'(?<=[.;])\s+', text))


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-fano-darkness', 'SIDE-li-map')
KERN_PIN = {'SIDE-explicit-formula': '8c51431', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-spinor': '520abe7',
            'SIDE-effects': 'ef4cff7', 'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab', 'SIDE-global-section': '17ce9ff'}


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
    put_json('b633_kernels_face.json', dict(at=utc(), kernels=kern_state()))


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
    p = os.path.join(SP if DRY else D, 'b633_scanfile_%s.md' % name)
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


# ================================================================================ COMPONENT 1: THE RECORD LINES
W_HEAD = '*Appended 2026-10-06 by b633 to b632’s entry (:%d), under `(R243)`(1) -- b632 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
CR_HEAD = '*Appended 2026-10-06 by b633 to b632’s record (:%d), under `(R243)`(1) -- A CORRECTION, THE SEAT’S: A GRADE CELL DID MOVE ON THE ζ PAGE:*'
PU_HEAD = '*Appended 2026-10-06 by b633 beneath the domain-condition criterion (:%d), under `(R243)`(2) and the author’s two answers before b633’s seal -- PREDICATE-UNLISTED, STANDING:*'
RF_HEAD = '*Appended 2026-10-06 by b633 to the second-reader form’s clause (:%d), under `(R243)`(3) -- THE READER’S SESSION ISOLATED FROM THIS PROJECT’S MEMORY:*'
DF_HEAD = '*Appended 2026-10-06 by b633 to the closing form, a clause at the record’s form (:%d), under `(R243)`(5) -- THE DELIVERY FORM:*'


def _weight():
    return ('\n%s the rule’s grades applied to the table’s ungraded rows: 1,732 rows moved on the working copy (1,463 derived, 66 on named '
            'premises, 203 definitions, none encoding its conclusion), 54 left ungraded with no statement the rule reads, no cell-graded row '
            'moved, every move checked at its pin; the premise census 42 named heads and 9 unnamed, counted by row. The packet of sixty '
            'committed with its prompt and not its key (relay 28f9e27e). The reader ran in a fresh session the author opened on D: -- not '
            'headless from D:\\reader_b632, which holds the lead and the paste alone -- its transcript under the D-- project, four tool calls '
            'on the packet and its answer file alone, the project’s memory index loaded at its start and read as surfacing hook lines without '
            'grading any row. Agreement 58 of 60 = 0.9667, H66c holding, the commit branch taken; the two disagreements Alt2 c (G008) and '
            'Alternates s (G054), each a restriction on a universally quantified variable the rule read as a premise -- a sample of six rows '
            'the two predicates carry. The generator’s edit (relay 553c3e8e), the regenerated table equal to the working copy row by row, '
            '1,750 rule / 208 cell / 54 none (relay 81e01857); the page generator’s provenance cell with its test (relay 2299971f). The ζ '
            'page from its fresh probe: 1933 s and free memory at 1527 MB at its lowest (relay data/b632_probe_zeta.txt) -- the ruling’s '
            '470 s and 2,430 MB are a cold-module figure from the record’s memory and one early poll reading, corrected here by the fact clause '
            '-- lean at 11 s of CPU over seven minutes and 15,489 page faults in 20 s against a disk at 127 %% busy, recorded and not stopped; '
            '347 marked Correspondence rows; EF_lit_zetaZeroConfig and KeiperObligations reading UNIVERSAL from the fuller probe (PLACE-papers '
            'd288454). The χ page: 314 rows, 129 s, 1807 MB at its lowest, WindowObligations UNIVERSAL (79df101). One grade cell moved, on the '
            'ζ page: LiLimitExchange from ungraded to the rule’s DEF (relay data/b633_lilimit.txt); no tier cell moved and no cell graded by a '
            'ledger. H66a, H66c and H66d holding; H66b and N2 refuted, 42 named premises against forty; N5 refuted in letter by the two '
            'generator edits as ordered. The suite 82 of 83, G-PACKET-DRAWN’s positive control mutating what its predicate does not read, the '
            'predicate tested directly and holding. FINDINGS :7699, :7701; OPEN_TRAILS :13193, :13195. Relay 8e6b63cc; PLACE-papers e67c43b; '
            'the root d8bbeaaf…189f, b624 to b632 agreeing. Nothing deposited; no kernel touched.\n' % (W_HEAD % K.B632_ENTRY))


def _correction():
    return ('\n%s the record’s defect (g) (relay data/b632_defects.txt and its short form above) and the seat’s closing words say no grade '
            'cell moved on either page. One did: on the ζ page LiLimitExchange, a list mark’s Correspondence row, moved from ungraded to the '
            'rule’s DEF with its provenance printed (PLACE-papers d288454 :410; before it 62ab6f4 :194), as the ζ commit’s message names. No '
            'cell graded by a ledger moved and no tier cell moved. The record stands as written; this entry is the correction.\n' % (CR_HEAD % K.B632_RECORD))


def _unlisted():
    return ('\n%s when a named predicate on a variable the statement quantifies is met for the first time, the shared rule prints it as '
            'PREDICATE-UNLISTED and does not read it as a premise, so the named-restriction list grows by a ruling and not by a wrong grade '
            'standing until a reader catches it. “For the first time” is read against MET: the 51 names any row of the terminal table carried '
            'in the rule’s reading at relay 8e6b63cc, 45 from rows the rule grades and 6 from rows ledger cells grade, so the clause guards '
            'forward and moves no row read before it. The clause does not separate a premise structure about a fixed kernel object from a '
            'predicate restricting a quantified variable; that separation is W-ORD-BINDER-GRAMMAR’s (:%d), and MET is the forward-only guard '
            'until it lands. With it the rule enters Alt2 and Alternates as named restrictions, each with the variable it restricts and its '
            'definition’s file and line, by the second reader of b632.\n' % (PU_HEAD % K.CRITERION, K.BINDER_GRAMMAR))


def _readerform():
    return ('\n%s the reader’s fresh session runs from a directory whose project memory is not this project’s -- a path off D:\\ or a '
            'directory with its own empty .claude -- so no memory index loads at its start; the seat prints the reader’s loaded-memory listing '
            'as part of the session audit, expected empty. The b632 reader’s audit stands as the seat read it; the amendment is for the next '
            'batch.\n' % (RF_HEAD % K.READER_FORM))


def _delivery():
    return ('\n%s a ferry may reach the seat as a file at D:\\ferry\\<act>.txt that the seat reads whole and confirms by byte count and '
            'sha256 printed, the author’s line “Read D:\\ferry\\<act>.txt and confirm receipt-in-full” standing as the ratifying act in place '
            'of the paste; a closing reaches the navigator as the closing bank’s file or its remote path at the closing’s commit, the '
            'author’s line naming the act and the head. The paste form stays available; the ferry’s header reads “paste or file read”.\n'
            % (DF_HEAD % K.CLOSING_FORM))


def record_lines(*a):
    """### FINDINGS: b632's weight (to :7701). OPEN_TRAILS: the correction (to b632's record :13195); PREDICATE-UNLISTED (to the criterion
    ### :12955); the reader form (to :12839); the delivery form (to the closing form :13028) -- each appended at the end, addressed."""
    import b602_record as RR
    Q = RR._Q()
    entry = Q.line_of(Q.FIND, '## The E0 rule’s grades on 1732 terminal rows')
    if entry != K.B632_ENTRY:
        sys.exit('### b632`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B632_ENTRY, _weight()), ('OPEN_TRAILS.md', CR_HEAD % K.B632_RECORD, _correction()),
             ('OPEN_TRAILS.md', PU_HEAD % K.CRITERION, _unlisted()), ('OPEN_TRAILS.md', RF_HEAD % K.READER_FORM, _readerform()),
             ('OPEN_TRAILS.md', DF_HEAD % K.CLOSING_FORM, _delivery())]
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
    _land(Q, items, 'b633_record_lines.json', K.B632_ENTRY)


def _run_test(rel, bank, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b633 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel,
                                  failing=[re.match(r'^  (\(\d+\))', l).group(1) for l in out.split(NL)
                                           if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]))
    print(L[-1])


def b630_run(*a):
    """### (R243)(4): test_chain_page_b630.py after its freeze, run and counted (data/b633_b630_test.txt)."""
    _run_test('tools/test_chain_page_b630.py', 'b633_b630_test')


# ================================================================================ COMPONENT 2: THE RULE
def rule_test(*a):
    """### (R243)(2): the rule's edit printed against its blob at the act's pre-relay pin; the rule's self-test and test_e0_rule.py run and
    ### counted (data/b633_rule_test.txt, data/b633_rule_diff.txt)."""
    old = (_show(RELAY, PRE_RELAY, 'tools/e0_rule.py') or '').split(NL)
    new = io.open(os.path.join(ROOT, 'tools', 'e0_rule.py'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    dl = list(difflib.unified_diff(old, new, 'e0_rule.py@%s' % PRE_RELAY, 'e0_rule.py', lineterm='', n=0))
    put_txt('b633_rule_diff.txt', ['b633 -- (R243)(2): THE RULE`S EDIT, ITS DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), ''] + dl)
    _run_test('tools/test_e0_rule.py', 'b633_rule_test', SP + '/b633_planted_rule')


def _table_grades():
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    tg = {}
    for r in T['rows']:
        tg.setdefault((r['repo'], r['name']), r['grade'])
    return tg


def table(*a):
    before = _table_grades()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    tg = _table_grades()
    gmoved = sorted(n for n in set(before) | set(tg) if before.get(n) != tg.get(n))
    tag = a[0] if a and a[0] != 'dry' else 'table'
    L = ['b633 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(diff.get('changed') or [])),
         '### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
         '### ### **THE GRADE COLUMN`S DIFF, THE TABLE BEFORE THIS RUN AGAINST AFTER IT : %d ROWS MOVED %s.**' % (
             len(gmoved), dict(collections.Counter('%s -> %s' % (before.get(n), tg.get(n)) for n in gmoved)) or 'EMPTY')]
    L += ['  %s / %-60s %s -> %s' % (n[0], n[1], before.get(n), tg.get(n)) for n in gmoved]
    name = 'b633_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 grade_moved=[list(n) for n in gmoved], files_moved=moved))
    print(L[4])


# ================================================================================ THE PAGES
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


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from b632's list and probe in force (no Lean), written only where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = K.NODES[k], K.PROBE[k]
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b633_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b633_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = _grade_cells(prev.decode('utf-8')), _grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))
    put_json('b633_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved,
                                           free_mb_before=fm, seconds=secs, nodes=nl, probe=pr, at=utc(), dry=DRY))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; cells moved %s' % (k, rc, changed, secs, len(dl), gmoved or 'NONE'))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b633 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b633_gcp'), os.path.join(D, K.PROBE[k]))
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
    put_txt('b633_page_arms.txt', L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 3: THE CENSUS READS
DISCHARGE_READ = {   # ### the seat's reading of each ledger line the discharge matcher returns (name, ledger :line) -> verdict
    ('zeroSideNeg', 'OPEN_TRAILS :10882'): 'discharged: zeroSideNeg_holds discharges it',
    ('ConservationHypothesis', 'OPEN_TRAILS :61'): 'an open item to discharge (O.18), no discharge',
    ('ConservationHypothesis', 'OPEN_TRAILS :5523'): 'the route terminal resting on it, no discharge',
    ('HasDerivAt', 'FINDINGS :6244'): 'another declaration on the line, no discharge',
    ('NymanBeurlingPremise', 'FINDINGS :7639'): 'the obligations discharged on the line, not this premise',
    ('TrivialSummandPremise', 'FINDINGS :7026'): 'named undischarged', ('TrivialSummandPremise', 'FINDINGS :7056'): 'named undischarged',
    ('TrivialSummandPremise', 'OPEN_TRAILS :12420'): 'named undischarged',
    ('EulerFactorPremise', 'FINDINGS :7026'): 'named undischarged', ('EulerFactorPremise', 'FINDINGS :7056'): 'named undischarged',
    ('EulerFactorPremise', 'OPEN_TRAILS :12420'): 'named undischarged',
}
INCIDENTAL = ('identity',)   # ### a head that is an English word: its every hit is prose, read so line by line in the bank


def _discharge(name, hits):
    if not hits:
        return 'none named', []
    reads = [(h, DISCHARGE_READ.get((name, h)) or ('the word in prose, no discharge' if name in INCIDENTAL else 'UNREAD')) for h in hits]
    if any(v.startswith('discharged') for _h, v in reads):
        return 'discharged (%s)' % ', '.join(h for h, v in reads if v.startswith('discharged')), reads
    if any(v == 'named undischarged' for _h, v in reads):
        return 'named undischarged (%s)' % ', '.join(h for h, v in reads if v == 'named undischarged'), reads
    if any(v.startswith('an open item') for _h, v in reads):
        return 'an open item to discharge (%s)' % ', '.join(h for h, v in reads if v.startswith('an open item')), reads
    if any(v == 'UNREAD' for _h, v in reads):
        return 'UNREAD', reads
    return 'none named', reads


def met_table(rows):
    """### the 51 MET names (the rule's own list), each rule-met or cell-met, with the rows resting on it now, its kernels, the commits the
    ### table read them at, and the ledger lines naming its discharge, read."""
    import e0_rule as E
    import b633_census as CS
    by = collections.defaultdict(list)
    for r in rows:
        k, gr, why, prem, head = CS.rule_full(r.get('statement'), r['name'])
        if gr != 'INTERFACES':
            continue
        for _b, t in prem:
            nm, _w = CS.premise_name(t, head)
            if nm:
                by[nm].append(r)
    ledgers = {f: (K.show(f) or '').split(NL) for f in ('FINDINGS.md', 'OPEN_TRAILS.md')}
    M = json.loads(_show(RELAY, PRE_RELAY, 'data/b632_rule_moves.json'))
    out = []
    for nm in getattr(E, 'MET', ()):
        rs = by.get(nm, [])
        hits = ['%s :%d' % (f.replace('.md', ''), i) for f, ls in ledgers.items() for i, l in enumerate(ls, 1)
                if re.search(r'(?<![\w.])' + re.escape(nm) + r'(?![\w])', l) and re.search(r'discharg', l, re.I)]
        verdict, reads_ = _discharge(nm, hits)
        out.append(dict(name=nm, met='rule-met' if nm in M['named'] or nm in ('NymanBeurlingPremise', 'TrivialSummandPremise', 'EulerFactorPremise') else 'cell-met',
                        in42=nm in M['named'], b632_rows=M['named'].get(nm), rows_rule=sum(1 for r in rs if r.get('provenance') == 'rule'),
                        rows_cell=sum(1 for r in rs if r.get('provenance') == 'cell'), kernels=sorted(set(r['repo'] for r in rs)),
                        commits=sorted(set(r['head'][:7] for r in rs)), discharge=verdict, reads=reads_))
    return out


def census(*a):
    """### (R243)(6) Component 3: every read of the census at once (tools/b633_census.py), banked before any writing:
    ### data/b633_census.txt (Parts A-I) and data/b633_census.json."""
    import b633_census as CS
    X = CS.build()
    rows = CS.table_rows('HEAD')
    met = met_table(rows)
    J, old = X['J'], X['old']
    changed = []
    for row in J:
        o = old.get(row['n'], {})
        for c in CS.C9.COLS:
            new = ' ; '.join(row[c]) if isinstance(row[c], list) else row[c]
            if new != o.get(c):
                changed.append(dict(row=row['n'], col=c, was=o.get(c), now=new))
    head = g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()
    L = ['b633 -- COMPONENT 3, (R243)(6): THE CENSUS READS, BANKED BEFORE ANY WRITING (%s); PLACE-papers %s ; relay %s ; the table at relay %s' % (
        utc(), PRE_PP, head, head), '',
         '### PART A -- THE ROOT`S REPOSITORY LIST (tools/act_root.py repositories() at PLACE-papers %s): %d ; kernels among it %d ; the corpus`s own: '
         'relay, PLACE-papers ; ls-remote reads this run %d, at most %d per repository' % (
             PRE_PP, len(X['roots']), len([r for r in X['roots'] if r not in ('relay', 'PLACE-papers')]), sum(X['lsr'].values()), max(X['lsr'].values())),
         '    ' + ', '.join(X['roots']), '',
         '### PART B -- EVERY CELL OF §1 OLD -> NEW, WITH ITS SOURCE (b619`s resolvers at this act`s pins): %d cells in %d rows' % (
             len(changed), len(set(c['row'] for c in changed)))]
    SRC = dict(documents='REGISTRY @ %s, R-1 and R-2' % PRE_PP, keystones='the class lines; R-10', editions='the editions and the trails; R-9 since v0.4',
               sieve='the sieve v0.6`s headings', kernels='ls-remote, once per repository; R-6', deposit='the mirror roster at relay %s' % STEPZERO)
    for c in changed:
        L += ['  %s %s (%s)' % (c['row'], c['col'], SRC[c['col']]), '      was: %s' % c['was'], '      now: %s' % c['now']]
    L += ['', '### PART C -- THE KERNEL COLUMN AT THE ROOT`S LIST (repository | local main | remote main | current tag = peel at the remote | '
          'local peel | tags the clone carries unpushed | census rows naming it | table rows cell/rule/none):']
    for x in X['column']:
        L.append('  %-34s %s | %s | %s | %s | %s | %s | %s' % (
            x['repo'], (x['local_main'] or '')[:7], (x['remote_main'] or '')[:7], ('%s = %s' % (x['current'], (x['peel'] or '')[:7])) if x['current'] else
            ('the corpus`s own' if x['corpus'] else 'no tag'), (x['local_peel'] or '')[:7], x['local_only'] or '-', ', '.join(x['rows']) or '-',
            '%d/%d/%d' % (x['table'].get('cell', 0), x['table'].get('rule', 0), x['table'].get('none', 0))))
    un = [(x['repo'], x['local_only']) for x in X['column'] if x['local_only']]
    L += ['  ### kernels carrying tags their remotes do not: %d, tags %d -- %s' % (len(un), sum(len(t) for _r_, t in un), un),
          '  ### every current tag reads back at its clone: %s' % all(x['peel'] == x['local_peel'] for x in X['column'] if x['current']), '',
          '### PART D -- THE FACES (the explicit-formula kernel at v0.22-v0.25, from the table at relay %s):' % head]
    for f in X['faces']:
        L.append('  %s %s at %s = %s (wanted %s) -- %s' % (f['id'], f['label'], f['tag'], f['commit'], f['want'], f['path']))
        L += ['      %-60s %-11s %-5s %s' % (i['name'], i['grade'], i['provenance'], '; '.join(i['premises']) or '-') for i in f['items']]
    L += ['', '### PART E -- PROVENANCE PER CLUSTER (the table`s rows of the kernels each row names: cell / rule / none):']
    L += ['  %s %d / %d / %d   %s' % (n, v['cell'], v['rule'], v['none'], ', '.join(v['kernels'])) for n, v in sorted(X['prov'].items())]
    S = X['sec']
    L += ['', '### PART F -- PHASE 2 AGAINST SEC v0.2.2 = %s: %d theorems in the table (read at %s); two matchers, the short name as an identifier '
          'and the name read as words' % (K.SEC_COMMIT, S['theorems'], S['heads'])]
    for r in S['rows']:
        L.append('  %s %s %s ; SEC repository or module named %d times ; hits %d' % (r['row'], r['key'], r['path'], r['sec_mentions'], len(r['hits'])))
        L += ['      %s -- identifier at %s, words at %s -- %s ; its statement: %s' % (h['name'], h['ident'], h['phrase'], h['reading'], h['statement'])
              for h in r['hits']]
        L.append('      ### %s' % r['why'])
    I_ = X['intake']
    L += ['', '### PART G -- THE ANNEX: the intake pilot`s summary banks (the paper`s text absent): %s ; claims %s ; grades %s ; kernel-verified %s' % (
        ['%s sha256 %s (%d bytes)' % (b['path'], b['sha256'], b['bytes']) for b in I_['banks']], I_['claims'], I_['grades'], I_['kv'])]
    P = X['premises']
    L += ['', '### PART H -- THE 42 NAMED PREMISES (b632`s census heads) NOW, AND MET (the rule`s 51): rows on each counted by row',
          '  ### the sum of the 42 heads` INTERFACES rows %d ; the table`s rule-graded INTERFACES rows %d ; the table`s INTERFACES rows %d' % (
              P['sum_rows'], P['rule_interfaces'], P['table_interfaces'])]
    for x in P['heads']:
        L.append('  %-26s b632 %d -> now %d ; kernels %s ; commits %s' % (x['head'], x['b632_rows'], x['rows'], x['kernels'], x['commits']))
    L.append('  ### MET, each name read (rule-met or cell-met ; among the 42 ; rule rows / cell rows resting on it ; kernels ; discharge):')
    for m in met:
        L.append('  %-26s %-8s %-5s %d/%d %s %s -- %s' % (m['name'], m['met'], m['in42'], m['rows_rule'], m['rows_cell'], m['kernels'], m['commits'], m['discharge']))
        L += ['      %s : %s' % hv for hv in m['reads']]
    L += ['', '### PART I -- A FACT IN v0.4`S OWN BACK MATTER: its Correspondence names each row`s line as :399-:421 (`this edition`s line`), '
          'which are v0.3`s carried Correspondence rows; the rows stand at v0.4 :43-:65. b619`s position map took each row`s last match of its '
          'id, which falls in v0.3`s back matter; v0.4 stands unedited and v0.5`s back matter records the fact.']
    put_txt('b633_census.txt', L)
    put_json('b633_census.json', dict(at=utc(), pre_pp=PRE_PP, relay=head, roots=X['roots'], lsr=X['lsr'], changed=changed,
                                      J=[{k2: v for k2, v in row.items() if k2 != 'rows'} | dict(reg_lines=[x['line'] for x in row['rows']]) for row in J],
                                      column=X['column'], faces=X['faces'], prov=X['prov'], sec=X['sec'], intake=X['intake'], premises=X['premises'], met=met))
    print('  cells changed %d ; root list %d ; reads %d ; faces %d ; MET %d ; sum %d vs rule INTERFACES %d vs table INTERFACES %d' % (
        len(changed), len(X['roots']), sum(X['lsr'].values()), len(X['faces']), len(met), P['sum_rows'], P['rule_interfaces'], P['table_interfaces']))


# ================================================================================ COMPONENT 4: THE EDITION
BM3_TAG = '<!-- b610 (R220) THE v0.3 EDITION`S BACK MATTER, 2026-10-03 -->'
BM5_TAG = '<!-- b633 (R243) THE v0.5 EDITION’S BACK MATTER, 2026-10-06 -->'
VERSION5 = ('*v0.5, 2026-10-06 -- the census read again at its rows and widened: the kernel column at the act root’s repository list, the '
            'explicit-formula kernel’s four faces at v0.22-v0.25, the provenance of each row’s kernels’ table rows, the Phase 2 rows read '
            'against SIDE-structural-error-correction at v0.2.2, the ANNEX row’s intake figures and the 42 named premises in back matter; v0.4 '
            'stands beside it, unedited.*')
H37 = ('*(read 2026-10-04, b619; relay `data/b619_census.txt`)*', '*(read 2026-10-06, b633; relay `data/b633_census.txt`)*')
INTRO = [('the sieve rows the cluster holds at v0.5 through', 'the sieve rows the cluster holds at v0.6 through'),
         ('Each cell is read at PLACE-papers 9dbac4b or at the remote', 'Each cell is read at PLACE-papers e67c43b or at the remote')]
HEAD41 = ('sieve rows at v0.5', 'sieve rows at v0.6')
TAGS79 = ('9 kernels carry 12 tags their remotes do not (relay `data/b619_census.txt`, Part C and (F1)) -- W-ORD-TAG-REMOTES’ nine '
          '(OPEN_TRAILS :12597), each such tag named unpushed in its kernel’s cell in §1;')
INTAKE_CELL = ('the intake pilot of b628 (`(R238)`(5)): 28 claims read -- 3 kernel-verified, 1 theorem-supported, 7 argument-supported, 2 '
               'synthesis-suggested, 15 statement-grade -- its summary relay `data/b628_intake_summary.txt` (sha256 %s), the paper’s text '
               'absent from this census')


def _prov_line(head):
    return ('The last column, ruled at v0.5 (`(R243)`(6)(iii)), counts the terminal table’s rows of the kernels the row names by '
            'provenance -- cell (a ledger cell grades it), rule (the shared E0 rule reads its statement) and none (ungraded) -- in the table at '
            'relay %s; a kernel named in several rows is counted in each, so the column reads how much of each cluster’s compiled surface is '
            'ledger-graded, rule-graded or ungraded.' % head)


def _tags_line(CJ):
    un = [(x['repo'], x['local_only']) for x in CJ['column'] if x['local_only']]
    return ('%d kernels carry %d tags their remotes do not (relay `data/b633_census.txt`, Part C) -- of W-ORD-TAG-REMOTES’ nine '
            '(OPEN_TRAILS :12597), the tags b623 pushed now read at their remotes, and each tag still local is named unpushed in its kernel’s '
            'cell in §1;' % (len(un), sum(len(t) for _r_, t in un)))


def _cellx(s):
    return s.replace('|', '¦')


def _row_line(CJ, row, prov):
    line = row['table_line']
    if row['n'] == 'R22':
        c = line.split(' | ')
        c[3] = c[3] + ' ; ' + _cellx(INTAKE_CELL % CJ['intake']['banks'][0]['sha256'][:16] + '…')
        line = ' | '.join(c)
    p = prov[row['n']]
    return line + ' %d / %d / %d |' % (p['cell'], p['rule'], p['none'])


def _s1a(CJ):
    L = ['## §1A — THE KERNEL COLUMN AT THE ROOT’S LIST *(read 2026-10-06, b633, under `(R243)`(6)(i); relay `data/b633_census.txt`, Part C)*', '',
         'Every repository the act root names (relay `tools/act_root.py`, its repository list at PLACE-papers e67c43b, the list b632’s root was '
         'taken over), each read by one `git ls-remote`: its main at the clone and at the remote, its current tag at the remote with the '
         'commit it peels to, the tags its clone carries and the remote does not, the rows of §1 naming it, and its rows in the terminal table '
         'by provenance. relay and PLACE-papers are the corpus’s own repositories and carry no tag.', '',
         '| repository | main, clone / remote | current tag at the remote | unpushed by name | §1 rows naming it | table rows: cell / rule / none |',
         '|:--|:--|:--|:--|:--|:--|']
    for x in CJ['column']:
        cur = 'the corpus’s own' if x['corpus'] else (('%s = %s' % (x['current'], (x['peel'] or '')[:7])) if x['current'] else 'no tag')
        un = ', '.join('%s = %s' % tuple(t) for t in x['local_only']) or '—'
        L.append('| %s | %s / %s | %s | %s | %s | %d / %d / %d |' % (x['repo'], (x['local_main'] or '')[:7], (x['remote_main'] or '')[:7], cur, un,
                                                                   ', '.join(x['rows']) or '—', x['table'].get('cell', 0), x['table'].get('rule', 0),
                                                                   x['table'].get('none', 0)))
    return L


def _s1b(CJ, table):
    by = {(r['repo'], r['name']): r for r in table}
    em = by.get(('SIDE-explicit-formula', 'SIDEExplicitFormula.Simplicity.exceptional_mass_le_third')) or {}
    L = ['## §1B — THE EXPLICIT-FORMULA KERNEL’S FACES AT v0.22-v0.25 *(under `(R243)`(6)(ii); relay `data/b633_census.txt`, Part D)*', '',
         'Each face at its tag, its declarations at the grade the terminal table gives them with their provenance, and the named premises of '
         'every declaration the rule reads as resting on one; the table read at relay %s.' % CJ['relay'], '',
         '| face | tag = commit | file | declarations at their grades | named premises |', '|:--|:--|:--|:--|:--|']
    for f in CJ['faces']:
        decl = '; '.join('`%s` %s (%s)' % (i['name'].split('SIDEExplicitFormula.', 1)[-1], i['grade'], i['provenance']) for i in f['items'])
        prem = '; '.join('`%s` on %s' % (i['name'].split('.')[-1], ', '.join(i['premises'])) for i in f['items'] if i['premises']) or '—'
        if f['id'] == 'F2':
            decl += ('; its field `two_thirds` cites `Zeta23.thmB₀_mult` at anthropics/formal-math 3635e748, its axioms read from that '
                     'repository’s AUDIT.md :80, discharged at its source kernel and not in this one')
            prem = '`exceptional_mass_le_third` on hP : SimpleProportion (%s, %s)' % (em.get('grade'), em.get('provenance'))
        L.append('| %s %s | %s = %s | `%s` | %s | %s |' % (f['id'], f['label'], f['tag'], f['commit'], f['path'], _cellx(decl), _cellx(prem)))
    return L


def _s1c(CJ):
    S = CJ['sec']
    L = ['## §1C — THE PHASE 2 ROWS READ AGAINST SIDE-structural-error-correction AT v0.2.2 *(under `(R243)`(6)(iv); relay `data/b633_census.txt`, Part F)*', '',
         'SEC’s %d theorems at v0.2.2 = %s, as the terminal table holds their statements, read against the syntheses that carry the claims of '
         '2B, 2D, 2F and 2G by two matchers -- each theorem’s name as an identifier, and its name read as words -- every hit read; the '
         'load-bearing clause applied (OPEN_TRAILS :12699): a row that gained a kernel-verified terminal load-bearing for its head’s thesis '
         'would be printed as the trigger of the bookend, and nothing more.' % (S['theorems'], K.SEC_COMMIT), '',
         '| row | synthesis | an SEC terminal named by statement | why |', '|:--|:--|:--|:--|']
    for r in S['rows']:
        L.append('| %s | %s `%s` | %s | %s |' % (r['row'], r['key'], r['path'], 'none' if r['names'] is False else 'UNREAD', _cellx(r['why'])))
    L += ['', 'No row names an SEC terminal; SEC’s theorems state its own defined sizes and counts (`interface_size = 0`, `num_compartments = '
          'S`, `d_eff = 2 * num_compartments - 1`), arithmetic over the kernel’s own constants, which the load-bearing clause does not count. '
          'No row gains a load-bearing kernel-verified terminal, no bookend is triggered, and the census’s tier stands at C.']
    return L


def _premises_bm(CJ):
    met = {m['name']: m for m in CJ['met']}
    P = CJ['premises']
    L = ['### The named premises the INTERFACES rows rest on (`(R243)`(6)(vi)), and MET', '',
         'b632’s census read 42 named heads under the rule-graded INTERFACES rows (relay `data/b632_rule_moves.txt`). Each is printed with the '
         'kernels its rows sit in, the commits the table read those rows at, the rows resting on it at b632 and now, and whether a ledger '
         'names its discharge, each matched line read by the seat (relay `data/b633_census.txt`, Part H). Alt2 and Alternates enter the rule '
         'as domain conditions at this act (`(R243)`(2)), and the rows resting on them alone read DERIVES.', '',
         '| named premise | kernels | commits read at | INTERFACES rows resting on it, b632 → now | a ledger naming its discharge |',
         '|:--|:--|:--|:--|:--|']
    for x in P['heads']:
        note = ' (entered as a domain condition, `(R243)`(2))' if x['head'] in ('Alt2', 'Alternates') else ''
        L.append('| %s | %s | %s | %d → %d%s | %s |' % (x['head'], ', '.join(x['kernels']) or '—', ', '.join(x['commits']) or '—', x['b632_rows'],
                                                      x['rows'], note, (met.get(x['head']) or {}).get('discharge', 'none named')))
    L += ['', '*The 42 heads’ rows sum to %d now, a row counted once for each named premise it rests on; the table’s rule-graded INTERFACES '
          'rows number %d and all its INTERFACES rows %d.*' % (P['sum_rows'], P['rule_interfaces'], P['table_interfaces']), '',
          'MET, the rule’s forward guard (`(R243)`(2) and the author’s two answers before b633’s seal), holds these 42 and nine more: '
          'NymanBeurlingPremise, TrivialSummandPremise and EulerFactorPremise, rule-met, carried by rows the rule graded before b632’s census; '
          'and six cell-met, carried in the rule’s reading by rows a ledger cell grades, each named with its rows in relay '
          '`data/b633_census.txt`, Part H.']
    return L


def _edition(CJ, cur, table):
    """### v0.5 from v0.4's lines by transforms; RETURN (lines, where, kinds, ins) -- every v0.4 line's place and kind; the inserted ranges."""
    i37 = next(i for i, l in enumerate(cur, 1) if l.startswith('## §1 — THE PHASES AND CLUSTERS'))
    i39 = next(i for i, l in enumerate(cur, 1) if l.startswith('One row per phase and cluster as REGISTRY lists them'))
    i41 = next(i for i, l in enumerate(cur, 1) if l.startswith('| row | phase and cluster |'))
    rows_at = [i for i, l in enumerate(cur, 1) if re.match(r'^\| R\d\d \| ', l) and i < i41 + 30]
    i79 = next(i for i, l in enumerate(cur, 1) if l.startswith('- **Local tags the remotes do not carry.**'))
    i10 = next(i for i, l in enumerate(cur, 1) if l.startswith('*v0.4, 2026-10-04'))
    J = {r['n']: r for r in CJ['J']}
    out, where, kinds, ins, pos = [], {}, {}, {}, {}

    def add(l, key=None):
        out.append(l)
        if key:
            pos[key] = len(out)
        return len(out)

    for i, l in enumerate(cur, 1):
        if i == i10:
            a = add(VERSION5, 'ver')
            add('')
            ins['the version line'] = (a, a)
        if i == i37:
            where[i], kinds[i] = add(l.replace(H37[0], H37[1]), 'h37'), 'rewritten (fact)'
            continue
        if i == i39:
            nl = l
            for o, n in INTRO:
                nl = nl.replace(o, n)
            where[i], kinds[i] = add(nl, 'intro'), 'rewritten (fact)'
            add('')
            a = add(_prov_line(CJ['relay']), 'provline')
            ins['the provenance column`s line'] = (a, a)
            continue
        if i == i41:
            where[i], kinds[i] = add(l.replace(HEAD41[0], HEAD41[1]) + ' kernels’ table rows: cell / rule / none |', 'h41'), 'rewritten (ruled)'
            continue
        if i == i41 + 1:
            where[i], kinds[i] = add(l + ':--|'), 'rewritten (ruled)'
            continue
        if i in rows_at:
            n = re.match(r'^\| (R\d\d) \| ', l).group(1)
            where[i], kinds[i] = add(_row_line(CJ, J[n], CJ['prov']), n), 'row rewritten'
            if i == rows_at[-1]:
                for key, block in (('s1a', _s1a(CJ)), ('s1b', _s1b(CJ, table)), ('s1c', _s1c(CJ))):
                    add('')
                    a = len(out) + 1
                    for k2, bl in enumerate(block):
                        add(bl, key if k2 == 0 else None)
                    ins[key] = (a, len(out))
            continue
        if i == i79:
            where[i], kinds[i] = add(l.replace(TAGS79, _tags_line(CJ)), 'tags'), 'rewritten (fact)'
            continue
        where[i], kinds[i] = add(l), 'carried'
    return out, where, kinds, ins, pos


def _bm5(CJ, cur, where, kinds, ins, pos):
    J = {r['n']: r for r in CJ['J']}
    ch = collections.defaultdict(list)
    for c in CJ['changed']:
        ch[c['row']].append(c['col'])
    SRC = dict(documents='REGISTRY @ 76dc1210 (PLACE-papers e67c43b), R-1 and R-2', keystones='the class lines; R-10',
               editions='the editions and the trails; R-9 since v0.4', sieve='the sieve v0.6’s headings', kernels='ls-remote, once per repository; R-6',
               deposit='the mirror roster at relay aabdee5e')
    L = ['', BM5_TAG, '',
         '## Back matter of the v0.5 edition — written 2026-10-06 by b633 under the author’s ruling `(R243)`(6), by the form of `(R187)`(5), its '
         'clauses and the precedence order', '',
         '### The readings v0.5 adds, each the seat’s and strikeable', '',
         '- **R-9, since v0.4.** A dated append is read since v0.4’s commit (PLACE-papers 6a3069e); the append v0.4 named in R23 (m5-1 a5d1944) '
         'is older and leaves the cell.',
         '- **R-13, the kernel column.** The act root’s repository list at PLACE-papers e67c43b -- relay, PLACE-papers and every kernel the '
         'census, REGISTRY or a page pins -- each read by one `git ls-remote`, its current tag the remote’s highest by the peel, in §1A; §1’s '
         'kernel cells stay by R-6, so a kernel the root adds that no row’s documents name stands in §1A alone.',
         '- **R-14, the faces.** SIDE-explicit-formula’s faces at v0.22-v0.25 are read from the terminal table at their grade and provenance, '
         'with the named premises the rule reads; the two_thirds citation is a structure’s field and is read with the theorem resting on it.',
         '- **R-15, the provenance cell.** A row’s kernels’ table rows are counted by provenance, a kernel named in several rows counted in each.',
         '- **R-16, Phase 2 against SEC.** SEC’s theorems are matched against each synthesis by their names as identifiers and as words; a hit '
         'is read by the seat and printed with its reading; the load-bearing clause decides whether a match could move a tier.',
         '- **R-17, the ANNEX.** The intake pilot’s figures enter R22’s keystones cell from its summary bank, by digest; no sentence of the '
         'paper is in this census.',
         '- **R-18, the named premises.** The 42 heads are b632’s census heads, read now at the table after the rule’s two entries; MET is '
         'the rule’s own list (`tools/e0_rule.py`).', '',
         '### The cells changed, by row and column (both wordings in relay `data/b633_census.txt`, Part B)', '',
         '| row | this edition’s line | v0.4 line | columns changed | source |', '|:--|:--|:--|:--|:--|']
    v4row = {re.match(r'^\| (R\d\d) \| ', cur[i - 1]).group(1): i for i, k in kinds.items() if k == 'row rewritten'}
    for n in sorted(J):
        cols = ch.get(n, [])
        L.append('| %s | {E:%s} | :%d | %s | %s |' % (n, n, v4row[n], ', '.join(cols + ['provenance (new)']),
                                                     '; '.join([SRC[c] for c in cols] + ['the terminal table at relay %s' % CJ['relay']])))
    L += ['', '*%d cells changed in %d rows; every row gains the provenance cell.*' % (len(CJ['changed']), len(ch)), '',
          '### Rewrites under the clauses', '',
          '| line | v0.4 line | was | now | clause | the object named |', '|:--|:--|:--|:--|:--|:--|']
    rw = [('h37', 'h37', H37[0], H37[1], 'fact', 'the read and its bank')] + \
         [('intro', 'intro', o, n, 'fact', 'the sieve’s version and the pin read') for o, n in INTRO] + \
         [('h41', 'h41', HEAD41[0], HEAD41[1] + ' … kernels’ table rows: cell / rule / none', 'fact; ruled', 'the sieve’s version; the provenance column, `(R243)`(6)(iii)'),
          ('tags', 'tags', TAGS79, _tags_line(CJ), 'fact', 'the tags read by ls-remote')]
    inv = {}
    for i, w in where.items():
        inv[w] = i
    for key, _k2, was, now, clause, obj in rw:
        L.append('| {E:%s} | :%d | “%s” | “%s” | %s | %s |' % (key, inv[pos[key]], _cellx(was), _cellx(now), clause, obj))
    L += ['', '### Insertions ordered by the ruling', '', '| lines | what | Status |', '|:--|:--|:--|',
          '| {E:ver} | the version line, above v0.4’s | inserted |',
          '| {E:provline} | §1’s line on the provenance column | inserted |',
          '| {E:s1a} | §1A, the kernel column at the root’s list | inserted |',
          '| {E:s1b} | §1B, the faces at v0.22-v0.25 | inserted |',
          '| {E:s1c} | §1C, the Phase 2 rows read against SEC | inserted |', '']
    L += _premises_bm(CJ)
    L += ['', '### A fact read in v0.4’s back matter', '',
          'v0.4’s Correspondence names each row’s line as :399-:421 (“this edition’s line”), which are v0.3’s carried Correspondence rows; '
          'the rows stand at v0.4 :43-:65. b619’s position map took each row’s last match of its id, which falls in v0.3’s back matter. v0.4 '
          'stands unedited; this edition’s Correspondence names the rows’ own lines.', '',
          '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.5 | `%s` | written at b633 |' % K.CEN5, '| v0.4 | `%s` | unedited |' % K.CEN4,
          '| v0.3 | `phase2/method/THE_KEYSTONE_CENSUS_v0_3.md` | unedited |',
          '| the current version (v0.1 with its v0.2 section) | `phase2/method/THE_KEYSTONE_CENSUS.md` | unedited |',
          '| the census bank | relay `data/b633_census.txt` | banked before this edition |',
          '| the registry read | `REGISTRY.md` @ 76dc1210 (read at PLACE-papers e67c43b) | read, unedited |',
          '| the sieve read | `%s` | read, unedited |' % K.SIEVE6,
          '| the terminal table | relay `data/terminal_table.json` @ %s | read |' % CJ['relay'],
          '| SEC’s statements | SIDE-structural-error-correction v0.2.2 = 6bf19ab, through the table | read |',
          '| the intake summary | relay `data/b628_intake_summary.txt`, `data/b628_intake_summary.json` | read by digest |']
    L += ['| a synthesis read against SEC | `%s` | read, unedited |' % p for _r_, _k, p in K.PHASE2]
    L += ['', '### Correspondence', '', '| row | this edition’s line | phase and cluster | REGISTRY rows (lines) | keystone | Status |',
          '|:--|:--|:--|:--|:--|:--|']
    for n in sorted(J):
        r = J[n]
        L.append('| %s | {E:%s} | %s | %s | %s | %s |' % (n, n, _cellx(r['label']), ', '.join(':%d' % x for x in r['reg_lines']),
                                                         'yes' if r['has_keystone'] else 'none', 'read again' if ch.get(n) else 'read again, its six columns unchanged'))
    for f in CJ['faces']:
        L.append('| %s | {E:s1b} | %s, SIDE-explicit-formula %s = %s | — | — | read |' % (f['id'], f['label'], f['tag'], f['commit']))
    L += ['', '### Version history', '',
          '- **v0.5, 2026-10-06 (b633, `(R243)`(6))**: the census read again at its rows and widened -- %d cells changed in %d rows; the '
          'kernel column at the root’s %d repositories; the four faces at v0.22-v0.25; the provenance cell on every row; the Phase 2 rows read '
          'against SEC; the ANNEX’s intake figures; the 42 named premises. v0.4 stands beside it, unedited.' % (
              len(CJ['changed']), len(ch), len(CJ['roots'])),
          '- **v0.4, 2026-10-04 (b619)**, **v0.3, 2026-10-03 (b610)**, **v0.2, 2026-09-28 (b553)** and **v0.1, 2026-08-12**: carried above.']
    return L


def edition(*a):
    """### PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_5.md beside v0.4 (unedited), and data/b633_edition.json. `dry`: the scratchpad.
    ### The re-pin step is last: the {E:n} tokens resolved against the final file."""
    CJ = jl('b633_census.json')
    cur = lines_of(_show(PP, PRE_PP, K.CEN4))
    table = json.load(io.open(_r('terminal_table.json'), encoding='utf-8'))['rows']
    out, where, kinds, ins, pos = _edition(CJ, cur, table)
    bm = _bm5(CJ, cur, where, kinds, ins, pos)
    lines = out + bm
    for k2, (a_, b_) in ins.items():
        pos.setdefault(k2, a_)
    lines = [re.sub(r'\{E:(\w+)\}', lambda m: ':%d' % pos[m.group(1)], l) for l in lines]
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b633_census_dry.md') if DRY else os.path.join(PP, *K.CEN5.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### v0.5 EXISTS -- NOTHING WRITTEN')
    _write(dest, b)
    v3bm = lines.index(BM3_TAG) + 1
    bm5 = lines.index(BM5_TAG) + 1
    seg_d = [dict(line=i, at=where[i], d=len(R4._segs(lines[where[i] - 1])) - len(R4._segs(cur[i - 1])), kind=k)
             for i, k in kinds.items() if k != 'carried']
    ins_lines = [l for k2, (a_, b_) in ins.items() if k2 != 'the version line' for l in lines[a_ - 1:b_]]
    J2 = dict(at=utc(), path=K.CEN5, sha256=sha(b), bytes=len(b), lines=len(lines), body_end=v3bm - 1, v3bm=v3bm, bm=bm5, pos=pos,
              where={str(k2): v for k2, v in where.items()}, kinds={str(k2): v for k2, v in kinds.items()}, ins=ins,
              version=_count([VERSION5]), ruled=_count(ins_lines), removals=0, seg_d=seg_d,
              n_body=_count(lines[:v3bm - 1]), n_cur_body=_count(cur[:cur.index(BM3_TAG)]), n_bm5=_count(lines[bm5 - 1:]), dry=DRY)
    print('  %s : %d lines, %d bytes, sha256 %s ; body %d sentences (v0.4 %d) ; ruled %d ; version %d ; rewrites` segment change %s' % (
        ('DRY ' + dest) if DRY else K.CEN5, len(lines), len(b), J2['sha256'][:16], J2['n_body'], J2['n_cur_body'], J2['ruled'], J2['version'],
        [x['d'] for x in seg_d if x['d']]))
    put_json('b633_edition.json', J2)


def _count(ls):
    return sum(len(R4._segs(l)) for l in ls)


def _edpath():
    return os.path.join(SP, 'b633_census_dry.md') if DRY else os.path.join(PP, *K.CEN5.split('/'))


def _ed():
    return lines_of(open(_edpath(), encoding='utf-8').read().replace(chr(13), ''))


def termscan(*a):
    t = _scan(_edpath())
    put_txt('b633_census_termscan.txt', t.rstrip(NL).split(NL))
    print('  ' + ' ; '.join(l.strip() for l in t.split(NL) if re.search(r'live uses|VERDICT', l)))


def keystone_hits(text):
    """### the generator's own keystone pattern applied to a text: which page nodes it names, per page (chain_page.keystones' rule)"""
    import chain_page as CP
    out = {}
    for k in ('zeta', 'chi'):
        names = [x['name'] for x in CP.read_nodes(os.path.join(D, K.NODES[k]))[0] if x['source'] == 'kernel']
        short = sorted(set(n.split('.')[-1] for n in names))
        plain = sorted(s for s in short if re.fullmatch(r'[a-z]+|[A-Z]+', s))
        rest = sorted(s for s in short if s not in plain)
        alts = [r'\b(' + '|'.join(re.escape(s) for s in rest) + r')\b'] if rest else []
        alts += [r'(`' + re.escape(s) + r'`|[A-Za-z0-9_]\.' + re.escape(s) + r'\b)' for s in plain]
        out[k] = sorted(set(m.group(0).strip('`').split('.')[-1] for m in re.finditer('|'.join(alts), text)))
    return out


def bank(*a):
    """### data/b633_edition_CENSUS.txt (the diff bank) and data/b633_h28.json: H28a-H28c scored."""
    E = jl('b633_edition.json')
    ed = _ed()
    cur = lines_of(_show(PP, PRE_PP, K.CEN4))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### v0.5 ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b633_census_termscan.txt')
    clean = _clean(scan)
    live = re.search(r'live uses\s*: (\d+)', scan)
    body = ed[:E['body_end']]
    beyond = [(i + 1, m.group(0)) for i, l in enumerate(body) for m in R4.CEILING.finditer(l)]
    beyond0 = [(i + 1, m.group(0)) for i, l in enumerate(cur[:cur.index(BM3_TAG)]) for m in R4.CEILING.finditer(l)]
    ok, bad = 0, []
    for i, l in enumerate(cur, 1):
        if not l.strip():
            continue
        k = E['kinds'].get(str(i))
        w = E['where'].get(str(i))
        good = bool(w) and (ed[w - 1] == l if k == 'carried' else (ed[w - 1] != l and ed[w - 1].split(' | ')[0] == l.split(' | ')[0]
                                                                     if k == 'row rewritten' else ed[w - 1] != l))
        ok += good
        if not good:
            bad.append(i)
    segc = sum(abs(x['d']) for x in E['seg_d'])
    allowed = E['removals'] + E['ruled'] + E['version'] + segc
    dn = E['n_body'] - E['n_cur_body']
    h28a = 'HOLDS'
    h28b = 'HOLDS' if abs(dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and len(beyond) <= len(beyond0) else 'REFUTED'
    kh = keystone_hits(NL.join(ed))
    L = ['b633 -- COMPONENT 4: THE DIFF BANK OF THE_KEYSTONE_CENSUS v0.5 against v0.4 at %s; the final file sha256 %s (%d lines, %d bytes)' % (
        PRE_PP, E['sha256'], E['lines'], E['bytes']), '',
         '### THE COUNTS, SEPARATELY: the body v0.4 %d sentences, v0.5 %d (%+d); removals 0; the ruled insertions %d; the version line %d; the '
         'rewrites` segment change %d; v0.5`s own back matter %d' % (E['n_cur_body'], E['n_body'], dn, E['ruled'], E['version'], segc, E['n_bm5']), '',
         '### EVERY v0.4 LINE THAT MOVED IN MEANING, BOTH WORDINGS (every other line carried verbatim at its mapped line):']
    for i, l in enumerate(cur, 1):
        k = E['kinds'].get(str(i), 'carried')
        if k == 'carried':
            continue
        w = E['where'].get(str(i))
        L += ['  v0.4 :%d -> :%s %s' % (i, w, k), '      was: %s' % l[:2400], '      now: %s' % ed[w - 1][:2600]]
    L += ['### THE INSERTIONS: %s' % E['ins'],
          '### CARRIED: %d of %d non-blank v0.4 lines found at their mapped line, verbatim or as their recorded rewrite (failing %s)' % (
              ok, sum(1 for l in cur if l.strip()), bad or 'none'),
          '### THE SCANNER: %s, live %s ; the ceiling pattern in the body: %d hits (v0.4`s body %d)' % ('CLEAN' if clean else 'NOT CLEAN',
                                                                                               live.group(1) if live else '?', len(beyond), len(beyond0)),
          '### THE PAGE NODES THE EDITION NAMES (the generator`s keystone pattern): %s' % kh, '',
          '### ### **H28a %s** -- VACUOUS on its letter: the census has no work-list, so no MOVED-IN-MEANING sentence; beside it, every changed '
          'cell names its source (the census bank`s Part B) and every rewrite its clause (the back matter)' % h28a,
          '### ### **H28b %s** -- the body %+d against at most %d (removals 0 + ruled %d + version %d + the rewrites` segment change %d)' % (
              h28b, dn, allowed, E['ruled'], E['version'], segc),
          '### ### **H28c %s** -- the scanner %s, %s live stems by its count; the ceiling pattern in the body %d against v0.4`s %d' % (
              h28c, 'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(beyond), len(beyond0)),
          '### ### **THE CENSUS LANDS: NO SENTENCE HELD.**' if not bad else '### ### **HELD AT %s.**' % bad]
    put_txt('b633_edition_CENSUS.txt', L)
    put_json('b633_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, body_dn=dn, allowed=allowed, clean=clean, live=int(live.group(1)) if live else None,
                                   beyond=len(beyond), beyond0=len(beyond0), carried_ok=ok, carried_bad=bad, vacuous_a=True, keystone_hits=kh))
    for l in L[-5:]:
        print(l[:260])


def repin(*a):
    E = jl('b633_edition.json')
    ed = _ed()
    L = ['b633 -- THE RE-PIN STEP (R190)(3), THE FORM`S LAST: THE_KEYSTONE_CENSUS v0.5`s own cited lines read against its final file (sha256 %s)' % E['sha256'][:16]]
    ok = n = 0
    for k2, v in sorted(E['pos'].items(), key=lambda kv: kv[1]):
        n += 1
        l = ed[v - 1] if 0 < v <= len(ed) else ''
        if re.fullmatch(r'R\d\d', k2):
            good = l.startswith('| %s | ' % k2) and v < E['body_end']
        elif k2 == 'ver':
            good = l == VERSION5
        elif k2 == 'provline':
            good = l.startswith('The last column, ruled at v0.5')
        elif k2 in ('s1a', 's1b', 's1c'):
            good = l.startswith('## §1%s — ' % k2[-1].upper())
        elif k2 == 'h37':
            good = H37[1] in l
        elif k2 == 'intro':
            good = INTRO[1][1] in l
        elif k2 == 'h41':
            good = 'kernels’ table rows: cell / rule / none |' in l
        elif k2 == 'tags':
            good = l.startswith('- **Local tags the remotes do not carry.**') and 'b633_census' in l
        else:
            good = bool(l.strip())
        ok += good
        L.append('  {E:%s} -> :%d %s %s' % (k2, v, 'HOLDS' if good else '### FAILS', l[:120]))
    unres = re.findall(r'\{E:\w+\}', NL.join(ed))
    L += ['### unresolved tokens: %s' % (unres or 'none'), '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (ok, n)]
    put_txt('b633_repin.txt', L)
    put_json('b633_repin.json', dict(at=utc(), held=ok, of=n, unresolved=unres))
    print(L[-1])


# ================================================================================ COMPONENT 5: THE ROOT
ROOT_EXCLUDE = re.compile(r'^b633_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b633_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b633'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline; the chain's verify is read inside the suite alone."""
    import shutil
    import act_root as AR
    J = jl('b633_act_root.json')
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
    L = ['b633 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s)' % (
             bank_, r2, same, J['root']), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b633_root_arm.txt', L)
    put_json('b633_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', K.CEN4,
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H67a', 'H67b', 'H67c', 'H67d', 'H28a', 'H28b', 'H28c')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b632_closing_push_out.txt', 'data/act_roots.txt', 'tools/e0_rule.py', 'tools/test_e0_rule.py', 'tools/test_chain_page_b630.py'}
SIX = {('SIDE-global-section', 'AlternationShadow.alternates_both'), ('SIDE-global-section', 'AlternationShadow.alternates_neg'),
       ('SIDE-global-section', 'AlternationShadow.both_values_survive_global_sign'), ('SIDE-global-section', 'LadderOrientationShadow.ladder_up_to_orientation'),
       ('SIDE-global-section', 'LadderOrientationShadow.stepsI_of_alt2'), ('SIDE-global-section', 'LadderOrientationShadow.stepsMI_of_alt2')}


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
    """### (R243)'s N5, the file-set by PATH (Component 0's repair of b632's basename match)."""
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
    face = jl('b633_kernels_face.json')['kernels']
    now = kern_state(list(face))
    kern_ok = all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    pp_beyond = [x for x in pp_ch if x not in ('FINDINGS.md', 'OPEN_TRAILS.md', K.CEN5, K.PAGE, K.DIR_PAGE)]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b633_|audit_b633_)', x) or re.match(r'^data/terminal_table', x)
                                           or x in N5_ALLOWED)]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not tracked_local and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel unmoved against the face %s; PLACE-papers %s (beyond the census, the ledgers and the pages: %s); %s; '
            'relay beyond the list, matched by path: %s; b628`s local intake bank in any relay commit %s, untracked now %s; no outbound request '
            'was made, so no identifier in one' % (kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE', tracked_local, untracked_local))


def _cen5():
    p = os.path.join(PP, *K.CEN5.split('/'))
    return io.open(p, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(p) else ''


def scores(*a):
    CJ, H, RP, TR = jx('b633_census.json'), jx('b633_h28.json'), jx('b633_repin.json'), jx('b633_table_rule.json')
    RA, PZ, PX = jx('b633_root_arm.json'), jx('b633_page_zeta.json'), jx('b633_page_chi.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    c5 = _cen5()
    roots = set(CJ.get('roots') or [])
    s1a = set(re.findall(r'^\| (SIDE-[\w-]+|relay|PLACE-papers) \| \w{7} / ', c5, re.M))
    body = c5.split(BM3_TAG)[0] if c5 else ''
    named = set(re.findall(r'\b(SIDE-[a-z0-9][a-z0-9-]*[a-z0-9])\b', NL.join(l for l in body.split(NL) if re.match(r'^\| R\d\d \| ', l))))
    import b633_census as CS
    named = set(k for k in named if k not in CS.C.NOT_REPO)
    a_ok = bool(roots) and s1a == roots and named <= roots
    sec = (CJ.get('sec') or {}).get('rows') or []
    b_ok = len(sec) == 4 and all(r.get('why') for r in sec) and not any(h['reading'] == 'UNREAD' for r in sec for h in r['hits'])
    P = CJ.get('premises') or {}
    c_ok = bool(P) and P.get('sum_rows') == P.get('table_interfaces')
    d_ok = bool(c5) and 'DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): ### TIER C**' in c5 and all(r['names'] is False for r in sec)
    moved = set(tuple(x) for x in (TR.get('grade_moved') or []))
    faces_ok = True
    table = json.load(io.open(_r('terminal_table.json'), encoding='utf-8'))['rows']
    tg = {(r['repo'], r['name']): r['grade'] for r in table}
    for f in CJ.get('faces') or []:
        for i in f['items']:
            faces_ok = faces_ok and tg.get(('SIDE-explicit-formula', i['name'])) == i['grade'] and ('`%s` %s' % (i['name'].split('SIDEExplicitFormula.', 1)[-1], i['grade'])) in c5
    S = {
        'H67a': (('HOLDS' if a_ok else 'REFUTED'), 'the kernel column §1A names %d repositories against the root`s list of %d, equal %s; §1`s kernel cells name %d, '
                 'beyond the list %s' % (len(s1a), len(roots), s1a == roots, len(named), sorted(named - roots) or 'NONE')),
        'H67b': (('HOLDS' if b_ok else 'REFUTED'), 'Phase 2 rows read %d; naming an SEC terminal by statement %d; each printing why %s' % (
            len(sec), sum(1 for r in sec if r['names'] is not False), all(r.get('why') for r in sec))),
        'H67c': (('HOLDS' if c_ok else 'REFUTED'), 'the 42 heads` rows sum to %s, a row counted once per named premise; the table`s INTERFACES rows %s, '
                 'its rule-graded INTERFACES rows %s' % (P.get('sum_rows'), P.get('table_interfaces'), P.get('rule_interfaces'))),
        'H67d': (('HOLDS' if d_ok else 'REFUTED'), 'the tier line reads C in v0.5 %s; no Phase 2 row gains a load-bearing kernel-verified terminal %s' % (
            'TIER C**' in c5, all(r['names'] is False for r in sec))),
        'H28a': (H.get('H28a', 'REFUTED'), 'VACUOUS on its letter: no work-list'),
        'H28b': (H.get('H28b', 'REFUTED'), 'the body %s against at most %s' % (H.get('body_dn'), H.get('allowed'))),
        'H28c': (H.get('H28c', 'REFUTED'), 'the scanner clean %s, live %s; the ceiling in the body %s against v0.4`s %s' % (
            H.get('clean'), H.get('live'), H.get('beyond'), H.get('beyond0'))),
        'N1': (('HELD' if a_ok else 'REFUTED'), 'as H67a'),
        'N2': (('HELD' if b_ok else 'REFUTED'), 'as H67b'),
        'N3': (('HELD' if c_ok else 'REFUTED'), 'as H67c, after the two moves'),
        'N4': (('HELD' if d_ok else 'REFUTED'), 'as H67d'),
        'N5': n5v,
        'S1': (('HELD' if moved == SIX and not (PZ.get('cells_moved') or []) and not (PX.get('cells_moved') or []) else 'REFUTED'),
               'the rule`s regeneration moved %d rows, the six %s; page cells moved %s / %s' % (len(moved), moved == SIX, PZ.get('cells_moved'), PX.get('cells_moved'))),
        'S2': (('HELD' if CJ and set(CJ['lsr']) == roots and all(v == 1 for v in CJ['lsr'].values()) else 'REFUTED'),
               'the census read %d repositories, at most %s each' % (len(CJ.get('lsr') or {}), max((CJ.get('lsr') or {0: 0}).values()))),
        'S3': (('HELD' if faces_ok and CJ.get('faces') else 'REFUTED'), 'every face declaration`s grade in v0.5 equals the table`s at HEAD %s' % faces_ok),
        'S4': (('HELD' if RP and RP.get('held') == RP.get('of') and not RP.get('unresolved') else 'REFUTED'), 'the re-pin %s of %s' % (RP.get('held'), RP.get('of'))),
        'S5': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                            RA.get('root_copy') != RA.get('root') if RA else None)),
    }
    put_json('b633_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b633 — lane three, act sixty under (R243): the keystone census at v0.5 -- the kernel column at the root’s list, the four '
              'new faces, provenance per cluster, Phase 2 read against SEC, the 42 named premises in back matter; two predicates entered in the '
              'rule; the reader and delivery forms amended; the b630 test frozen')


def _figures():
    CJ = jl('b633_census.json')
    kern = set()
    for row in CJ['J']:
        kern |= set(row['kernel_src'])
    table = json.load(io.open(_r('terminal_table.json'), encoding='utf-8'))['rows']
    c = collections.Counter(r.get('provenance') or 'none' for r in table if r['repo'] in kern)
    k = sum(1 for row in CJ['J'] if row['kernel_src'])
    p = sum(1 for r in CJ['sec']['rows'] if r['names'] is not False)
    return CJ, len(CJ['roots']), c.get('cell', 0), c.get('rule', 0), c.get('none', 0), k, p


def _title_entry():
    CJ, r, c, u, n, k, p = _figures()
    return ('## The keystone census at v0.5: %d repositories in the kernel column, four faces at v0.22–v0.25, provenance %d/%d/%d across %d '
            'clusters, %d Phase 2 rows naming an SEC terminal, 42 named premises in back matter; Alt2 and Alternates entered as domain '
            'conditions' % (r, c, u, n, k, p))


def _finding_text():
    S, rl, J = jl('b633_scores.json'), jl('b633_record_lines.json'), jl('b633_act_root.json')
    CJ, r, c, u, n, k, p = _figures()
    E, TR = jl('b633_edition.json'), jx('b633_table_rule.json')
    t = _title_entry()
    P = CJ['premises']
    e = ['', t, '',
         '*Filed at b633 on the author’s ruling `(R243)` and the author’s three answers before the seal. Banks: relay `data/b633_census.txt`, '
         '`data/b633_edition_CENSUS.txt`, `data/b633_table_rule.txt`, `data/b633_rule_diff.txt`, `data/b633_act_root.txt`, '
         '`data/b633_author_answers.txt`. Nothing deposits.*', '',
         '**The census** (`(R243)`(6)): %s beside v0.4, unedited, %d lines, sha256 %s; its rows read again by b619’s resolvers at PLACE-papers '
         'e67c43b, %d cells changed in %d rows; the kernel column at the act root’s %d repositories (§1A), each read once by ls-remote; the '
         'explicit-formula kernel’s faces at v0.22-v0.25 (§1B) -- the Platt rung, the two_thirds citation, the Nyman–Beurling face and the '
         'Dedekind instance -- at the table’s grades with their named premises; a provenance cell on every row, %d/%d/%d cell/rule/none across '
         'the kernels the rows name; the Phase 2 rows read against SEC at v0.2.2 (§1C), %d naming an SEC terminal, each printing why none does '
         'and no bookend triggered; the ANNEX row with the intake pilot’s figures by digest; the 42 named premises in back matter, their rows '
         'summing to %d against %d INTERFACES rows in the table, the sum counting a row once per premise. H67a %s, H67b %s, H67c %s, H67d %s; '
         'H28a %s, H28b %s, H28c %s.' % (K.CEN5, E['lines'], E['sha256'][:16], len(CJ['changed']), len(set(x['row'] for x in CJ['changed'])), r,
                                         c, u, n, p, P['sum_rows'], P['table_interfaces'], S['H67a'][0], S['H67b'][0], S['H67c'][0], S['H67d'][0],
                                         S['H28a'][0], S['H28b'][0], S['H28c'][0]), '',
         '**The rule** (`(R243)`(2)): Alt2 and Alternates entered as named restrictions, each with its variable and its definition’s line; '
         'PREDICATE-UNLISTED added for a named predicate on a quantified variable the rule neither lists nor has met, MET the 51 names any '
         'table row carried in the rule’s reading at relay 8e6b63cc; the table regenerated, %d rows moving, the six the two predicates carry '
         'and no other.' % len(TR.get('grade_moved') or []), '',
         '**The record lines** (`(R243)`(1)-(5)): b632 at its weight, its figures read from its banks (FINDINGS :%d); a correction to b632’s '
         'record (OPEN_TRAILS :%d); PREDICATE-UNLISTED standing (:%d); the reader form amended (:%d); the delivery form (:%d); the b630 test '
         'frozen to its pin.' % tuple(x['line'] for x in rl['lines']), '',
         '**The root.** b633 over %d repositories, %d tags and %d banks; its chain verified inside the suite.' % (
             len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, S[k2][0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b619’s census v0.4 (FINDINGS :7404) at its rows and finds its back '
         'matter’s line cells pointing at v0.3’s; b632’s premise census (FINDINGS :7701), whose 42 heads it carries; and b623’s SEC artefact, '
         'whose statements it reads against Phase 2. It strengthens the programme’s offering of a census whose every kernel is read at its '
         'remote, whose every cluster says how much of its surface a ledger, the rule or nothing grades, and whose premises are named with '
         'their discharge where a ledger records one.', '',
         '**Next.** Per `(R243)`(7): b634, W-ORD-GATE-FROM-ELABORATOR if the author’s word falls there, else the (R110) deposit preparations '
         'with the census and the root. The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds or locates any zero; a rule grade reads a statement’s binders.*', '']
    return t, NL.join(e)


FOR_AUTHOR = ('(1) the kernel column read as a section, §1A, beside §1’s cells, which stay by R-6; (2) the faces read from the table, the two_thirds '
              'face as its structure with the theorem resting on it; (3) the provenance cell counting a kernel in each row naming it; (4) the '
              'Phase 2 hits read by the seat -- 2B’s “interface dark” the cognitive variable, 2F’s formation_total_seven the BSD kernel’s own; '
              '(5) the 51 MET names banked in relay, the census naming the three rule-met extras and pointing to the bank for the six cell-met, '
              'one of which carries a stem the scanner refuses in back matter; (6) H67c scored by its letter against the table’s INTERFACES '
              'count, the rule-graded count printed beside; (7) test_e0_rule.py case (19), whose planted premise is the clause’s own subject, '
              're-pointed in the same edit')


def _next_lines():
    return ['b634 names no kernel terminal; the gate act’s statements are its own to write, and the deposit’s items are the census v0.5, the '
            'root d-line and the (R110) route’s files as the author names them']


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b633_scores.json', 'b633_findings.json', 'b633_record_lines.json', 'b633_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b633_author_answers.txt'), re.M))
    rows_ = ['', TRAIL_HEAD, '',
             '**(R243) ratified.** (1) b632 at its weight. (2) The two disagreements upheld, the rule extended, PREDICATE-UNLISTED. (3) The '
             'reader form. (4) The b630 test frozen. (5) The delivery form. (6) The keystone census at v0.5. (7) The act after: b634.', '',
             '**Entered:** FINDINGS.md:%d (b632’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the correction to b632’s record), :%d '
             '(PREDICATE-UNLISTED, standing), :%d (the reader form), :%d (the delivery form); this record; %s.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                 rl['lines'][4]['line'], K.CEN5), '',
             '**Act root:** b633 `%s` (previous `%s`, b632’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**Prompts to the author:** %d (relay data/b633_author_answers.txt)%s.' % (
                 n_ans, (': ' + ' / '.join(_elide(answer_of(i))[:400] for i in range(n_ans))) if n_ans else ''), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b633_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, S[k2][0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R243)`(7), b634, W-ORD-GATE-FROM-ELABORATOR or the (R110) deposit preparations; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b633_scores.json')
    L = ['=' * 104, 'b633 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H67a-H67d and H28a-H28c, (R243)(6).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper(), S[k2][0], S[k2][1]) for k2 in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SK]
    L += ['', '### ### **H : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k2][0] == 'HOLDS' for k2 in HKEYS), sum(S[k2][0] == 'REFUTED' for k2 in HKEYS), sum(S[k2][0] == 'HELD' for k2 in NK),
                             sum(S[k2][0] == 'REFUTED' for k2 in NK), sum(S[k2][0] == 'HELD' for k2 in SK), sum(S[k2][0] == 'REFUTED' for k2 in SK)), '']
    L += rd('b633_defects.txt').rstrip(NL).split(NL)
    put_txt('b633_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b633_scores.json', 'b633_findings.json', 'b633_trail.json', 'b633_record_lines.json', 'b633_act_root.json'))
    L = ['b633 -- THE COMPONENTS, BANKED UNDER (R243).', '',
         '### COMPONENT 0 : the process listing ; b632`s closing push-out relay %s ; push-b632* branches deleted by name (data/b633_branches.txt) ; '
         'the LiLimitExchange cell (data/b633_lilimit.txt) ; every test file under tools/ run with b632`s lists (data/b633_tests_stepzero.txt) ; '
         'the suite run at HEAD before the face (data/b633_arms_prerun.txt) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b632`s weight FINDINGS :%d ; the correction :%d ; PREDICATE-UNLISTED :%d ; the reader form :%d ; the delivery form :%d ; '
         'the b630 test frozen (data/b633_b630_test.txt)' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the rule (data/b633_rule_diff.txt, data/b633_rule_test.txt) ; the table (data/b633_table_rule.txt)',
         '### COMPONENT 3 : data/b633_census.txt',
         '### COMPONENT 4 : %s ; data/b633_edition_CENSUS.txt ; H28a %s, H28b %s, H28c %s ; H67a %s, H67b %s, H67c %s, H67d %s' % (
             K.CEN5, S['H28a'][0], S['H28b'][0], S['H28c'][0], S['H67a'][0], S['H67b'][0], S['H67c'][0], S['H67d'][0]),
         '### COMPONENT 5 : the pages (data/b633_page_zeta.json, data/b633_page_chi.json) ; page arms data/b633_page_arms.txt ; the root %s' % J['root'][:16],
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b634 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b633_components.txt', L)


def findings(*a):
    """### THE FINDINGS WRITER (b630's body, restored at b632): the entry guarded for table cells, TECHNE text and stems, refused if its
    ### title stands, appended through b566's guarded append_to and its line banked."""
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
    put_json('b633_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
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
    put_json('b633_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b633_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-06 by b633 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b633_defects.json -- NOTHING WRITTEN')
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
    put_json('b633_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b633_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
