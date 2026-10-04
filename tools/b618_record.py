# -*- coding: utf-8 -*-
"""b618_record.py -- THE ACT'S RECORD TOOL, UNDER (R228). ### ONE SUBCOMMAND PER BANK.

### ### b618: LANE THREE, ACT FORTY-FIVE -- THE LIVING DOCUMENTS' CURRENCY: EIGHT DOCUMENTS READ FOR THEIR FUNCTIONS AND FED IN THEIR
### OWN FORMS WITH WHAT THE RECORD CARRIED PAST THEM.
### Subcommands write only `data/b618_*` unless the docstring names another file; `dry` on the command line routes every b618 bank to the
### seat's scratchpad (for `findings`, `trail` and `record_lines`, `dry` prints and appends nothing). Banks are written by encode, temp
### file, `os.replace`; ledger appends through b566's guarded `append_to`. ### THE EIGHT APPENDS ARE NOT WRITTEN BY THIS TOOL, save
### FACES_LEDGER's: `draft` banks each append's exact text, the seat writes it through the Edit tool, and `land` reads the file back against
### the committed blob plus the banked draft; FACES_LEDGER's goes through its own writer, b327_faces_row.append_block, from `land`. No
### platform call. No Lean call: both pages are re-emitted from their banked probes. The templates are tools/b617_record.py.
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

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
SPINOR = 'D:/SIDE-spinor'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
RELAY = ROOT.replace('\\', '/')
PRE_PP = '138ea0c'
PRE_RELAY = '6d813af6'
STEPZERO = 'c38ec385'
BASE_PP = '192077f'
DATE = '2026-10-04'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/74014083-db4d-4c92-b7fa-834bcf48e96a/scratchpad'
SESSION_ID = '74014083-db4d-4c92-b7fa-834bcf48e96a'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
LIVING = [
    ('VERIFICATION_LOOM', 'VERIFICATION_LOOM.md', '**PURPOSE:**'),
    ('INSTRUMENTS', 'phase1.5/method/INSTRUMENTS.md', '**PURPOSE:**'),
    ('THE_METHOD_CANON', 'phase1.5/method/THE_METHOD_CANON.md', '**PURPOSE:**'),
    ('THE_METHOD_AS_IT_STANDS', 'phase1.5/method/THE_METHOD_AS_IT_STANDS.md', '> ### **WHAT THIS DOCUMENT IS.**'),
    ('FACES_LEDGER', 'FACES_LEDGER.md', '**PURPOSE:**'),
    ('THE_LOAD_BEARING_MAP', 'phase1.5/method/THE_LOAD_BEARING_MAP.md', '**PURPOSE:**'),
    ('GAUGE_AND_INVARIANT', 'phase1.5/method/GAUGE_AND_INVARIANT.md', '**PURPOSE:**'),
    ('REGISTRY', 'REGISTRY.md', '**PURPOSE:**'),
]
DOC = {n: p for n, p, _nd in LIVING}
ORDER = [n for n, _p, _nd in LIVING]
TT_LEDGERS = ('VERIFICATION_LOOM', 'FACES_LEDGER', 'REGISTRY')   # ### terminal_table.ledger_files() reads these three for grade cells

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines', 'correction')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b618_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b618_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def rd(name):
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def lines_of(t):
    t = (t or '').replace(chr(13), '')
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def _poss(s):
    """### a backtick possessive (word`s) becomes ’s for a PLACE-papers file; a code span keeps its backticks."""
    return re.sub(r'(?<=\w)`(?=s\b)', '’', s)


def head_text(path, rev='HEAD'):
    return _show(PP, rev, path)


DEFECTS = [
    '(a) THE SEAT`S, AT COMPONENT 2, AFTER THE SEAL AND BEFORE ANY DOCUMENT WRITE: the plan`s FACES_LEDGER recommendation, written '
    'with the first draft, said the grade column would carry the E0 read and the tier and give the table six cells; the draft the face '
    'declares carries the tier alone and gives two (reading (vi)). The text corrected through the Edit tool and the plan banked again, '
    'before the first append; the bank`s first version is not kept.',
    '(b) THE SEAT`S, AT COMPONENT 3 (ii), BEFORE THE COMMIT: the Edit tool`s new text for INSTRUMENTS ended in a newline, so the file kept '
    'one blank line beyond the banked draft; `land` read the file back against the committed blob plus the draft and refused it (one line '
    'more on disk). The blank line was removed through the Edit tool, `land` read the file back equal, and the append was committed.',
    '(c) THE SEAT`S, AT COMPONENT 5, BEFORE THE RECORD: the scorer`s N5 wanted OPEN_TRAILS among the changed files, though its one write '
    'is the trail record, made after the scores, and read N5 REFUTED (b598`s, b601`s and b603`s species, repeated). The scorer corrected '
    'through the Edit tool to accept the pending trail append, named in N5`s line, and the scores banked again before the record.',
    '(d) THE SEAT`S, FOUND AT THE PRE-PUSH SUITE, AFTER THE PLACE-papers PUSH: the face declared two TABLE CELL lines (reading (vi)), '
    'predicting that FACES_LEDGER`s two T2-INTERFACES rows would give their names an INTERFACES cell; the prediction came from the bare '
    'grade-word pattern (terminal_table.GRADE_RE beside a backticked name), not from the table`s own cell reader, which reads no cell from '
    'those rows. The push gate and the suite regenerated the table unchanged (rows added 0, grade cells moved 0), so the face`s two lines '
    'and the spec`s clause of two cells are refuted in letter and G-TABLE-GRADES-DECLARED fails in its letter, 77 of 78, pre-push; the '
    'suite takes no edit after the seal. No grade moved. The pushed trail record`s item (3) and the FACES_LEDGER commit message say the '
    'cells were taken: a dated correction line is appended to OPEN_TRAILS addressed to the record, committed alone.',
    '(e) THE SEAT`S, AT THE HOUSEKEEPING COMMIT: relay 015659fc`s message says the loose and v3 matchers` counts moved; its diff moves '
    'the loose v1 count alone (1560 to 1562 cells, 1056 to 1058 names), v3 unchanged. The commit is not amended; this line is its '
    'correction.',
]
DEFECT_SHORT = ['(a) the seat’s: the plan’s FACES_LEDGER recommendation first described an earlier draft (the E0 read beside the tier, six '
                'table cells); corrected through the Edit tool to the draft the face declares (the tier alone, two cells) and the plan banked '
                'again before the first append',
                '(b) the seat’s: the Edit tool’s text for INSTRUMENTS ended in a newline, one blank line beyond the draft; the read-back refused '
                'it, the line was removed through the Edit tool and the read-back passed before the commit',
                '(c) the seat’s: the scorer’s N5 wanted OPEN_TRAILS changed before the trail record, its one write, and read REFUTED; '
                'corrected through the Edit tool to accept the pending append, the scores banked again before the record',
                '(d) the seat’s: the face’s two TABLE CELL lines came from the bare grade-word pattern, not the table’s reader, which reads no '
                'cell from FACES_LEDGER’s rows; the table moved none, G-TABLE-GRADES-DECLARED fails in its letter, 77 of 78 pre-push; a '
                'dated correction line addressed to this record',
                '(e) the seat’s: the housekeeping commit’s message names the v3 count as moved; only the loose v1 count moved']


def defects(*a):
    L = ['b618 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b618_defects.txt', L)


# ================================================================================ READING (1): THE READS
OT_LINES = [11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12044, 12082, 12190, 12192, 12194, 12228, 12280, 12300,
            12304, 12446, 12456, 12496, 12566, 12599, 12601, 12623, 12631, 12645, 12653, 12699, 12703, 12753, 12755, 12757]
READS = [
    ('relay data/b617_currency.txt whole', RELAY, PRE_RELAY, 'data/b617_currency.txt', 'ALL', 1600),
    ('relay data/b617_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b617_closing_push_out.txt', 'ALL', 260),
] + [('%s: its head to its function line, and its last thirty lines (its own form for appends)' % n, PP, PRE_PP, p, ('HEADTAIL', nd), 400)
     for n, p, nd in LIVING] + [
    ('OPEN_TRAILS: the form of an edition :11864, every clause and standing line beneath it named by the currency, and b617`s lines',
     PP, PRE_PP, 'OPEN_TRAILS.md', OT_LINES, 2400),
    ('OPEN_TRAILS: every appended head from :11864 to :12757', PP, PRE_PP, 'OPEN_TRAILS.md', ('GREPRANGE', r'^\*Appended 2026-', 11864, 12757), 300),
    ('FINDINGS: b596`s entry (the generator`s channels), the located-clause method, the pin-resolution rule, b617`s entry', PP, PRE_PP,
     'FINDINGS.md', [6760, 6856, 6886, 7278, 7366, 7368], 900),
    ('relay data/b604_author_answers.txt: the five tests (prompt 3)', RELAY, PRE_RELAY, 'data/b604_author_answers.txt', list(range(12, 16)), 900),
    ('the sieve v0.5: the five tests stated', PP, PRE_PP, 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md', list(range(26, 37)), 700),
    ('REGISTRY: the table heads, the row-update and row-addition forms, the rows for every edited document, the disagreements',
     PP, PRE_PP, 'REGISTRY.md', [62, 64, 65, 66, 67, 68, 69, 70, 81, 83, 140, 146, 157, 185, 189, 205, 214, 222, 226, 227, 246, 255, 257, 260, 263,
                                  267, 283, 291, 299, 333, 335, 336, 337, 338, 339, 340, 341, 342, 477, 479, 497, 499, 503, 505, 527, 529, 535, 537,
                                  687, 725, 731, 732, 733, 778, 787, 789, 887, 889, 897, 901, 905, 909], 500),
    ('SIDE-spinor at v0.1.0: the :731 item`s statements', SPINOR, 'v0.1.0', 'SIDESpinor/Spinor.lean', [60, 70, 71, 75, 76], 300),
    ('SIDE-spinor at HEAD: the same statements', SPINOR, 'HEAD', 'SIDESpinor/Spinor.lean', [60, 70, 71, 75, 76], 300),
    ('SPIRAL_MAP :104 and its v0.7 :106', PP, PRE_PP, 'SPIRAL_MAP.md', [104], 600),
    ('SPIRAL_MAP v0.7 :106', PP, PRE_PP, 'SPIRAL_MAP_v0_7.md', [106], 600),
    ('the spine document`s head', PP, PRE_PP, 'phase1.5/proofs/THE_RIEMANN_PATHS_CLUSTER_SPINE.md', list(range(1, 6)), 400),
]


def reads(*a):
    L = ['b618 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = lines_of(t)
        if sel == 'ALL':
            nums = [i + 1 for i, l in enumerate(sl) if l.strip()]
        elif isinstance(sel, tuple) and sel[0] == 'HEADTAIL':
            fl = next((i + 1 for i, l in enumerate(sl) if l.startswith(sel[1])), 12)
            nums = [i + 1 for i in range(0, fl) if sl[i].strip()] + [i + 1 for i in range(max(fl, len(sl) - 30), len(sl)) if sl[i].strip()]
        elif isinstance(sel, tuple) and sel[0] == 'GREPRANGE':
            nums = [i + 1 for i, l in enumerate(sl) if sel[2] <= i + 1 <= sel[3] and re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            line = sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE'
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['', '### THE EIGHT DOCUMENTS` LAST COMMITS (git log -1 at PLACE-papers %s):' % PRE_PP]
    for n, p, _nd in LIVING:
        L.append('    %-24s %s' % (n, g(PP, 'log', '-1', '--format=%h %ad %s', '--date=short', PRE_PP, '--', p).strip()[:200]))
    L += ['', '### THE VERSION LINES OF EVERY EDITION FILE SINCE %s AND OF THE SIX SYNTHESES (the finder`s line printed whole):' % BASE_PP]
    for f in added_since():
        vl = vline(f)
        L.append('    %-82s :%s %s' % (f, vl[0], (vl[2] or '### NO VERSION LINE')[:220]))
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b618_reads.txt', L)


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
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b618 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (%s), banked verbatim with the options and the '
         'recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % (n, DATE), '']
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act.')
    put_txt('b618_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-spinor': '520abe7'}


def kern_state():
    out = {}
    for k in KERNS:
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    """### data/b618_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b618_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ THE VERSION LINES
def added_since():
    """### every phase/day1/root .md file added in PLACE-papers since 192077f, as of PRE_PP"""
    return [x for x in g(PP, 'diff', '--name-only', '--diff-filter=A', BASE_PP, PRE_PP).split(NL)
            if x.endswith('.md') and (x.startswith('phase') or x.startswith('day1/') or '/' not in x)]


VTOK = re.compile(r'(?<![\w.])(?:v|Version\** )(\d+(?:\.\d+)+)(?![\w.]*\d)')


def vline(path, rev=PRE_PP):
    """### the file's version line: among its first 60 lines, those that are not a class line, a quote or a table row and carry a version
    ### token (`vX.Y`, or `Version X.Y` as ENUMERA writes it) beside a 2026 date; the first whose token is the version its file name
    ### carries, or, for a file whose name carries none, the first. Returns (line, version, text) or (0, None, None)."""
    t = _show(PP, rev, path)
    if t is None:
        return 0, None, None
    want = fname_ver(path)
    for i, l in enumerate(lines_of(t)[:60]):
        if 'DOCUMENT CLASS' in l or 'CLASS-NUMBERING' in l or l.startswith(('>', '|')):
            continue
        m = VTOK.search(l)
        if m and '2026-' in l and (want is None or 'v' + m.group(1) == want):
            return i + 1, 'v' + m.group(1), l
    return 0, None, None


def fname_ver(path):
    m = re.search(r'_v(\d+(?:_\d+)+)\.md$', path)
    return ('v' + m.group(1).replace('_', '.')) if m else None


# ================================================================================ THE LOOM'S TABLE
def _count(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _findings_entries():
    """### every `## ` heading of FINDINGS from :4000, by the act whose commit wrote it (git blame at PRE_PP)"""
    out = {}
    t = g(PP, 'blame', '--line-porcelain', '-L', '4000,', PRE_PP, '--', 'FINDINGS.md')
    summ, cur = {}, None
    for l in t.split(NL):
        m = re.match(r'^([0-9a-f]{40}) \d+ (\d+)', l)
        if m:
            cur = (m.group(1), int(m.group(2)))
        elif l.startswith('summary '):
            summ[cur[0]] = l[8:]
        elif l.startswith('\t') and l[1:].startswith('## '):
            a = re.match(r'^(b\d{3})', summ.get(cur[0], ''))
            if a:
                out.setdefault(a.group(1), []).append(cur[1])
    return out


def loom_rows():
    files = [x for x in g(RELAY, 'ls-tree', '-r', '--name-only', PRE_RELAY, 'data/').split(NL) if re.match(r'^data/b(\d{3})_checks', x)]
    fe = _findings_entries()
    rows = []
    for n in range(537, 618):
        a = 'b%d' % n
        pre = _count(_show(RELAY, PRE_RELAY, 'data/%s_checks.txt' % a))
        post = _count(_show(RELAY, PRE_RELAY, 'data/%s_checks_postpush.txt' % a))
        kept = []
        for f in sorted(x for x in files if x.startswith('data/%s_checks' % a) and x not in ('data/%s_checks.txt' % a, 'data/%s_checks_postpush.txt' % a)):
            c = _count(_show(RELAY, PRE_RELAY, f))
            kept.append((os.path.basename(f), c))
        rows.append(dict(act=a, pre=pre, post=post, kept=kept, findings=fe.get(a, [])))
    return rows


def _cnt(c):
    return '%d of %d' % c if c else '—'


# ================================================================================ INSTRUMENTS I-16 TO I-39
INSTR = [
    # (title, where, line, needle, act, ruling, reads, decides)
    ('THE FORM OF AN EDITION', 'OPEN_TRAILS', 11864, 'THE FORM OF AN EDITION, STANDING FOR CP-7', 'b577', '(R187)(5)–(6)',
     'a keystone’s current version, its tier block and its CP-1b work-list, and the page its objects sit on, as its spine',
     'the keystone’s next version, written beside the current one, which stays unedited: each marked sentence carried (STANDS), rewritten to what '
     'the compiled fact says with its declaration named at the pin the page prints (MOVED-IN-MEANING), or removed with the removal recorded in '
     'back matter; CREDIT lines placed; Placement and Correspondence in back matter; scored by H28a, H28b and H28c'),
    ('H28b, RESTATED FOR EVERY EDITION ACT', 'OPEN_TRAILS', 11902, 'H28b, RESTATED FOR EVERY EDITION ACT', 'b579', '(R189)(2)',
     'the body sentence counts of the edition and of the current version, the back matter excluded and counted beside',
     'whether the body grew by more than the CREDIT count, the removals and the citations a ruling orders'),
    ('THE STEM CLAUSE', 'OPEN_TRAILS', 11904, 'THE STEM CLAUSE, STANDING', 'b579', '(R189)(3)',
     'the sentences the work-list does not mark that carry a banned stem',
     'each stem replaced by the object its sentence names, the sentence otherwise unchanged, listed in back matter with line and both wordings'),
    ('THE CEILING CLAUSE', 'OPEN_TRAILS', 11906, 'THE CEILING CLAUSE', 'b579', 'the author’s answer before b579’s seal',
     'the sentences the work-list does not mark, against the README ceiling (README :106–:121)',
     'the words beyond the ceiling replaced by the object the sentence names, listed in back matter as a ceiling correction'),
    ('THE HISTORY CLAUSE', 'OPEN_TRAILS', 11908, 'THE HISTORY CLAUSE', 'b579', 'the author’s answer before b579’s seal',
     'a marked sentence inside a dated history entry',
     'the entry carried unchanged as the dated record, and a history line beneath it stating what the compiled fact says, counted under H28b as '
     'a ruled citation'),
    ('H28b, FINAL FORM', 'OPEN_TRAILS', 11930, 'H28b, FINAL FORM FOR EVERY EDITION ACT', 'b580', '(R190)(2)',
     'the body sentence counts, the back matter excluded and counted beside',
     'the bound: the CREDIT count, the removals, the ruled citations and one version line'),
    ('THE RE-PIN STEP', 'OPEN_TRAILS', 11932, 'THE RE-PIN STEP, THE FORM’S LAST', 'b580', '(R190)(3)',
     'the edition’s own Correspondence column and the act’s diff bank, against the final file',
     'every citation re-pointed to the final file’s lines, the offset from the current version stated once at the bank’s head'),
    ('THE NAME-AND-TITLE EXCEPTION', 'OPEN_TRAILS', 11934, 'THE NAME-AND-TITLE EXCEPTION', 'b580', 'the author’s answer before b580’s seal',
     'an object’s own name and a bibliography title that carry a banned word',
     'that such a use is not a live use: it carries unchanged, listed in back matter with its line, printed as excepted when H28c is scored'),
    ('THE FACT CLAUSE', 'OPEN_TRAILS', 11954, 'THE FACT CLAUSE, STANDING', 'b581', '(R191)(2)',
     'an unmarked sentence stating a pin, a toolchain, a count or an import, against the seat’s printed read',
     'the sentence corrected in place to the printed fact, the fact’s source printed in the diff bank, the correction listed in back matter'),
    ('THE PLACEMENT CLAUSE', 'OPEN_TRAILS', 11956, 'THE PLACEMENT CLAUSE', 'b581', 'the author’s answer before b581’s seal',
     'a b450 “does not carry” item that the work-list does not place',
     'the item inserted beside the sentence whose claim it corrects, that sentence named in back matter'),
    ('INSIDE A DATED ENTRY THE HISTORY CLAUSE GOVERNS', 'OPEN_TRAILS', 12044, 'INSIDE A DATED ENTRY THE HISTORY CLAUSE GOVERNS', 'b585',
     'the author’s answer before b585’s seal',
     'a banned stem inside a dated history entry',
     'the stem carried as the dated record with a history line beneath naming the corrected object, printed as carried-by-history when H28c '
     'is scored'),
    ('AN ITEM NAME OF A CITED PROGRAMME DOCUMENT', 'OPEN_TRAILS', 12082, 'AN ITEM NAME OF A CITED PROGRAMME DOCUMENT', 'b587', '(R197)(2)',
     'an item name that belongs to a programme document the edition cites',
     'the name carried unchanged under the name-and-title exception, with one back-matter line saying it is renamed at its own document’s '
     'edition'),
    ('THE PAGE CLAUSE', 'OPEN_TRAILS', 12190, 'THE PAGE CLAUSE', 'b592', 'the author’s answer before b592’s seal',
     'the two pages’ Placement against the node names an edition carries',
     'every page whose Placement the act changes regenerated as its last housekeeping commit before the suite'),
    ('THE RESTATEMENT CLAUSE', 'OPEN_TRAILS', 12192, 'THE RESTATEMENT CLAUSE', 'b592', 'the author’s answer before b592’s seal',
     'the unmarked sentences of the same edition that restate a marked row’s claim',
     'each rewritten with minimal substitution, listed in back matter with both wordings and counted under H28b'),
    ('AN ERA ANNOTATION IS A DATED ENTRY', 'OPEN_TRAILS', 12194, 'AN ERA ANNOTATION IS A DATED ENTRY', 'b592',
     'the author’s answer before b592’s seal',
     'an era annotation in an edition’s scope',
     'that it is a dated history entry, its banned stem carried as the record with a history line beneath'),
    ('H28b FOR A REORGANISING EDITION', 'OPEN_TRAILS', 12456, 'H28b FOR A REORGANISING EDITION', 'b605', '(R215)(3)',
     'the sentences an edition moves whole to its back matter',
     'each counted as a recorded removal in H28b’s bound, listed in the diff bank with its destination, the bound checked on what remains'),
    ('A CLAUSE OF THE FORM FOR MULTI-ACT EDITIONS', 'OPEN_TRAILS', 12496, 'A CLAUSE OF THE FORM FOR MULTI-ACT EDITIONS', 'b607', '(R217)(2)',
     'the sentences an act’s work-list names, inside a plan on the trails that spans several acts',
     'H28c and any hypothesis bound on the whole body scored on the act’s own scope, the whole-document figure printed beside and handed on'),
    ('THE PRECEDENCE ORDER', 'OPEN_TRAILS', 12228, 'THE PRECEDENCE ORDER', 'b594', '(R204)(2)',
     'a sentence where two clauses of the form meet',
     'the history clause first, then the name-and-title exception, the stem, ceiling, fact and restatement clauses, each on what the earlier '
     'leave, resolved without a prompt and listed in back matter; a prompt kept for a sentence no clause reaches, a write outside the corpus '
     'and anything irreversible'),
    ('THE FROZEN CONTROL', 'OPEN_TRAILS', 12304, 'the frozen control reads every relay source at 12c15c80', 'b597', '(R207)(2), ratified at :12300',
     'b592’s node lists, probes and terminal table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, through relay '
     'tools/test_chain_page_b596.py',
     'whether the generator still re-emits b592’s two pages byte for byte at those pins, the arm named for the two pins (FINDINGS :6886)'),
    ('THE FIVE TESTS', 'OPEN_TRAILS', 12446, 'the five tests are the author’s three answers before the seal', 'b604',
     'the author’s answer before b604’s seal, relay data/b604_author_answers.txt, prompt 3',
     'a route row of the sieve, through its tests in order: placement register, prime side, conductor uniformity, quantifier, compiled face, '
     'each at its instrument’s pin as THE_FINDINGS_AS_THEY_STAND v0.5 :30–:34 states them',
     'DARK at the first test the row fails, with that test’s number, its instrument’s pin and the reason; BRIGHT when it fails none, which '
     'says the row’s register reaches placement at a compiled face and not that the row’s open side holds'),
    ('THE PIN-RESOLUTION RULE', 'OPEN_TRAILS', 12631, 'a pin resolves when its commit is in the clone and at the remote', 'b612',
     'the seat’s reading, confirmed by the author at (R223)(1) (OPEN_TRAILS :12653; FINDINGS :7278)',
     'a pin a document cites',
     'that the pin resolves when its commit is in the clone and at the remote'),
    ('THE LOAD-BEARING CLAUSE', 'OPEN_TRAILS', 12699, 'THE FORM’S FOURTH CLAUSE, THE KC TIER’S LOAD-BEARING CLAUSE', 'b615', '(R225)(2)',
     'a synthesis’s kernel-verified rows, against the cluster’s thesis as the document’s head states it',
     'the tier line KC when at least one kernel-verified row is load-bearing for that thesis, and C when such rows certify definitions, '
     'arithmetic over the papers’ own tuples or placeholders'),
    ('THE ONE-READ RULE', 'OPEN_TRAILS', 12703, 'THE SUITE’S REMOTE READS, STANDING', 'b615', '(R225)(4)',
     'a suite’s remote pins',
     'each remote read once per run and the read reused across arms; a failed read retried once alone before an arm reads it as failed'),
    ('THE GENERATOR’S CHANNELS', 'OPEN_TRAILS', 12280, 'a `# backmatter:` record emitted after the Correspondence table', 'b596',
     '(R206)(4)(c), the author’s answers before b596’s seal (relay data/b596_author_answers.txt); relay commit cfd9aeac, FINDINGS :6856',
     'a node list’s `# backmatter: <line>` records, and the declaration keyword of each node the generator relay tools/chain_page.py prints',
     'the records emitted in list order as one paragraph after the page’s Correspondence table, a list without one regenerating byte for byte; '
     'a structure given its entry tag by the generator’s own entry-tag pattern, its source header and E0 read unchanged'),
]
FIRST_I = 16


def instr_resolve(rev='HEAD'):
    out = []
    ot = lines_of(_show(PP, rev, 'OPEN_TRAILS.md'))
    for k, x in enumerate(INSTR):
        ln = x[2]
        txt = ot[ln - 1] if 0 < ln <= len(ot) else ''
        out.append(dict(id='I-%d' % (FIRST_I + k), title=x[0], where=x[1], line=ln, ok=x[3] in txt, act=x[4]))
    return out


# ================================================================================ THE PAGES' NODES (the faces, the map)
NODE_RE = re.compile(r'^(\d+)\. `([^`]+)` — (\S+?:\d+) — (.+?) — `')
GRADE_CELL = re.compile(r'— E0: (\S+) — tier: (.*?) \(table: (.*?)\) — axioms: (\[.*?\])')


def page_nodes(rev=PRE_PP):
    out = {}
    for k, p in (('ζ', PAGE), ('χ', DIR_PAGE)):
        for l in lines_of(_show(PP, rev, p)):
            m = NODE_RE.match(l)
            if not m:
                continue
            gc = GRADE_CELL.search(l)
            q = m.group(2)
            out.setdefault(q.split('.')[-1], []).append(dict(q=q, page=k, file=m.group(3), pin=m.group(4), e0=gc.group(1) if gc else '?',
                                                             tier=gc.group(2).strip() if gc else '?'))
    return out


FACES = [('simplicity', 'simplicity_iff', 'v0.17'), ('product', 'productLemma_holds', 'v0.18'), ('doubling', 'doubling_holds', 'v0.19'),
         ('Keiper', 'keiperTaylorIdentity_of', 'v0.19'), ('the window', 'plateauRampWindow_of', 'v0.20'), ('family', 'family_theorem', 'v0.21')]
FACE_STATES = {   # ### where the record entered each face: the act and its FINDINGS entry (git blame at PRE_PP, printed in the reads)
    'simplicity_iff': 'b596, FINDINGS :6856', 'productLemma_holds': 'b600, FINDINGS :6950', 'doubling_holds': 'b601, FINDINGS :6972',
    'keiperTaylorIdentity_of': 'b601, FINDINGS :6972', 'plateauRampWindow_of': 'b602, FINDINGS :6998', 'family_theorem': 'b603, FINDINGS :7028',
}


# ================================================================================ REGISTRY
UPDATES = [   # (registry line, base file, the edition file)
    (83, 'day1/A_Place_to_Stand.md', 'day1/A_Place_to_Stand_v5_17.md'),
    (146, 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md', 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md'),
    (157, 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'),
    (185, 'phase1.5/spectral/GRH_CASCADE.md', 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md'),
    (205, 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'),
    (214, 'phase1.5/rcurve/R_CURVE_CRITERION.md', 'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md'),
    (222, 'phase1.5/method/ENUMERA.md', 'phase1.5/method/ENUMERA_v1_6.md'),
    (226, 'phase1.5/method/INVARIANCE_BARRIERS.md', 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md'),
    (227, 'phase1.5/method/TECHNE_TOOLKIT.md', 'phase1.5/method/TECHNE_TOOLKIT_v8_3.md'),
    (260, 'phase2/method/E_DIFFICULTY_THEOREM.md', 'phase2/method/E_DIFFICULTY_THEOREM_v1_0_4.md'),
    (263, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md'),
    (283, 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md', 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT_v1_3.md'),
    (479, 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md'),
    (499, 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'),
    (505, 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md'),
    (901, 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH_v1_2.md'),
    (909, 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md', 'phase1.5/method/EXHAUSTIVENESS_LICENSE_v0_2.md'),
]
MONO_BETWEEN = ['day1/A_Place_to_Stand_v5_14.md', 'day1/A_Place_to_Stand_v5_15.md', 'day1/A_Place_to_Stand_v5_16.md']
SIEVE_BETWEEN = ['phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md',
                 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md']
SPIRAL = ('SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md')
ADDS = [   # (table, id, base file, the current version file, the act and ruling, kind)
    ('1.5A', '1.5a-9', 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md', None, 'b611', '(R221)', 'synthesis', 'Phase 1.2'),
    ('1.5A', '1.5a-10', 'phase1.5/proofs/THE_RIEMANN_PATHS_CLUSTER_SPINE.md', None, '—', '(R223)(1)', 'spine', 'Phase 1.2'),
    ('1.5E', '1.5e-7', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md', None, 'b612', '(R222)', 'synthesis', '1.5E'),
    ('2B', 'p2-36', 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', None, 'b613', '(R223)', 'synthesis', '2B'),
    ('2D', 'p2-37', 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS.md',
     'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md', 'b614', '(R224)', 'synthesis', '2D'),
    ('2F', 'p2-38', 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md', None, 'b615', '(R225)', 'synthesis', '2F'),
    ('2G', 'p2-d10', 'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md', None, 'b616', '(R226)', 'synthesis', '2G'),
    ('2C', 'p2-39', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md', 'b594', '(R204)',
     'edited', '2C'),
    ('2C', 'p2-40', 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md', 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_2.md', 'b599', '(R209)',
     'edited', '2C'),
    ('2C', 'p2-41', 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md', 'b617', '(R227)', 'edited', '2C'),
    ('2C', 'p2-42', 'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md', 'b610', '(R220)', 'edited', '2C'),
]
TABLE_HEAD = {'1.5A': ('Phase 1.5A', 'Phase 1.5 table'), '1.5E': ('Phase 1.5E', 'Phase 1.5 table'), '2B': ('Phase 2B', 'Phase 2 table'),
              '2C': ('Phase 2C', 'Phase 2 table'), '2D': ('Phase 2D', 'Phase 2 table'), '2F': ('Phase 2F', 'Phase 2 table'),
              '2G': ('Phase 2G', 'Phase 2 table')}
STATUS_WORDS = ('READY', 'DRAFT', 'SHORT', 'BLOCKED', 'UNREVIEWED', 'SUPERSEDED')


def _title(path, rev=PRE_PP):
    for l in lines_of(_show(PP, rev, path)):
        l = l.lstrip('﻿')
        if l.startswith('# '):
            return l[2:].strip()
    return '### NO TITLE'


def _words(path, rev=PRE_PP):
    return len((_show(PP, rev, path) or '').split())


def _tier(path, rev=PRE_PP):
    for i, l in enumerate(lines_of(_show(PP, rev, path))[:40]):
        m = re.search(r'STANDING TAXONOMY \(K/C/N/E, author-ruled 2026-07-28\):(?: ###)? \*?\*?TIER (KC|K|C|N|E)\b', l)
        if m:
            return m.group(1), i + 1
    return None, 0


def _status(path, rev=PRE_PP):
    """### a STATUS KEY word in the document's own head (to its first numbered or Abstract heading), table rows excluded -- a synthesis's
    ### head tabulates its source papers' statuses, which are theirs, not its own. Returns [(word, line)]."""
    out = []
    for i, l in enumerate(lines_of(_show(PP, rev, path))[:60]):
        if re.match(r'^## (\d|Abstract|I\.|1\.)', l):
            break
        if l.startswith('|'):
            continue
        for w in STATUS_WORDS:
            if re.search(r'\b%s\b' % w, l):
                out.append((w, i + 1))
    return out


def reg_row(line, rev=PRE_PP):
    l = lines_of(_show(PP, rev, 'REGISTRY.md'))[line - 1]
    c = [x.strip() for x in l.strip().strip('|').split(' | ')]
    return dict(line=line, text=l, id=c[0], title=c[1], file=c[2].strip('`'), version=c[3])


def internal_counts(rev=PRE_PP):
    ls = [x for x in g(PP, 'ls-tree', '-r', '--name-only', rev, '--', 'internal').split(NL) if x.strip()]
    ms = [x for x in g(PP, 'ls-tree', '-r', '--name-only', rev, '--', 'meta').split(NL) if x.strip()]
    return len([x for x in ls if not x.endswith('.gitkeep')]), len([x for x in ms if not x.endswith('.gitkeep')])


def spinor_reads():
    out = {}
    for rev in ('v0.1.0', 'HEAD'):
        t = lines_of(_show(SPINOR, rev, 'SIDESpinor/Spinor.lean'))
        out[rev] = dict(sha=g(SPINOR, 'rev-parse', '--short=7', rev + '^{commit}').strip(), l70=t[69].strip(), l75=t[74].strip())
    return out


# ================================================================================ COMPONENT 2: THE PLAN
def _cur():
    return json.loads(_show(RELAY, PRE_RELAY, 'data/b617_currency.json'))['docs']


def plan_data():
    CU = _cur()
    P = {}
    for n, p, nd in LIVING:
        tx = lines_of(_show(PP, PRE_PP, p))
        fl = next(((i + 1, l) for i, l in enumerate(tx) if l.startswith(nd)), (0, '### NO FUNCTION LINE'))
        lc = g(PP, 'log', '-1', '--format=%h %ad', '--date=short', PRE_PP, '--', p).strip()
        P[n] = dict(path=p, function_line=fl[0], function=fl[1], last=lc, price=CU[n]['price'], items=CU[n]['items'], lines=len(tx))
    return P


RULING = {
    'VERIFICATION_LOOM': '(i) fed: one dated table in the loom`s own form, one row per act b537-b617 (act, suite count pre- and post-push, kept '
                         'failed runs by bank name, the FINDINGS entry line), with a head line stating that the verdict record since b537 lives '
                         'in the relay`s suite banks and each act`s FINDINGS entry and the loom carries the table of them',
    'INSTRUMENTS': '(ii) fed: I-8 onward, one entry per instrument in the document`s form (name, what it reads, what it decides, the trail line '
                   'that entered it, the act), the generator`s channels among them',
    'THE_METHOD_CANON': '(iii) fed: the edition form and the synthesis form by name with their trail lines, as a dated section, the located-clause '
                        'method named by title and sha256 alone since its body is private',
    'THE_METHOD_AS_IT_STANDS': '(iv) fed the same way',
    'FACES_LEDGER': '(v) fed: the faces at v0.17-v0.21 in the ledger`s supersession form (simplicity, product, doubling, family, Keiper, the '
                    'window), each with its declaration, pin and grade',
    'THE_LOAD_BEARING_MAP': '(vi) fed by pointer: a dated section stating that the map`s function is carried by the two pages at their pins, '
                            'with the 76 nodes listed by qualified name and grade in one table and the page each sits on',
    'GAUGE_AND_INVARIANT': '(vii) a dated line stating nothing was missed, by the count',
    'REGISTRY': '(viii) fed in its own dated row-update and row-addition form: the version column for every edition since 192077f, the six '
                'syntheses as new rows with cluster and tier, the spine document`s row, the two disagreements, nothing else',
}
SEAT = {
    'VERIFICATION_LOOM': ('AGREES', 'the table appended after the b449 entry under the loom`s own `<!-- bNNN loom entry -->` marker and `### ** -- '
                          'filed DATE (bNNN)**` heading; 81 rows, b537 to b617 (the currency`s 80 acts, b537-b616, and b617, whose banks landed '
                          'after the price); the FINDINGS column lists every `## ` heading the act wrote (git blame), the last its entry; a kept '
                          'run is any suite bank beside the pre- and post-push ones, its own count printed. No grade word beside a backticked '
                          'name (terminal_table.py reads the loom as a ledger).'),
    'INSTRUMENTS': ('AGREES', 'in disposition; ### A FACT CORRECTION, THE NAVIGATOR`S: the document already carries I-8 to I-15 (I-8 THE RESOLVABILITY '
                    'TEST, :247), so the entries take I-16 to I-39, the next free ids, in the document`s heading form `## I-n — TITLE (...; '
                    'provenance: ...)`. Every one of the 24 resolves to a trail line: the five tests at :12446 (b604`s record), the '
                    'pin-resolution rule at :12631, the generator`s channels at :12280 (b596`s record, the author`s answers), the frozen '
                    'control at :12304. No page-node name in the entries.'),
    'THE_METHOD_CANON': ('AGREES', 'a dated section `## XXI.` after b588`s `## XX.`, under the canon`s own `<!-- bNNN (R...) TITLE, DATE -->` marker; '
                         'the edition form (OPEN_TRAILS :11864 and its clauses, now INSTRUMENTS I-16 to I-32) and the synthesis form (:12566, '
                         ':12601, :12699); the located-clause method by its file name in TECHNE-Core and sha256 19066344..., no body sentence.'),
    'THE_METHOD_AS_IT_STANDS': ('AGREES', 'the document carries no append form of its own; a dated section after its closing disclosure line, under '
                                'a marked comment and a `---` rule as its sections are divided, stating the two forms are pointers and not a ninth '
                                'law of its reduced set.'),
    'FACES_LEDGER': ('AGREES', 'one `## UPDATE — filed DATE (bNNN)` block through the ledger`s own writer (b327_faces_row.append_block), a table of '
                     'the six faces: declaration at pin and grade, the tier as the pages print it, the ledger`s own vocabulary. terminal_table.py '
                     'reads FACES_LEDGER as a ledger: the two T2-INTERFACES rows give their names an INTERFACES cell, moving them from UNGRADED, '
                     'declared on the face before the write; the four T0 rows carry no grade word the table reads.'),
    'THE_LOAD_BEARING_MAP': ('AGREES', 'a dated `### ...` section in the map`s own appended form; one table, 76 rows: qualified name, E0 grade and '
                             'tier, pin, the page (ζ / χ); the map is not a ledger terminal_table.py reads, so its grade words move no cell.'),
    'GAUGE_AND_INVARIANT': ('AGREES', 'one dated italic line under a marked comment at the end.'),
    'REGISTRY': ('DIFFERS', 'five of the 22 edited bases have no REGISTRY row with a Version column (SPIRAL_MAP, FACES_OF_H2_AT_FINITE_INSTANCE, '
                 'REPARAMETERIZATION_BARRIERS, THE_FINDINGS_AS_THEY_STAND, THE_KEYSTONE_CENSUS), so no version cell can be written for them; '
                 'the seat recommended a pointer line, inside "nothing else". ### THE AUTHOR`S ANSWER BEFORE THE SEAL (relay '
                 'data/b618_author_answers.txt): rows in the row-addition form for the four phase documents, the pointer line for SPIRAL_MAP, '
                 'the "nothing else" clause recorded as the navigator`s. The row updates in REGISTRY`s own append form (`## Row update -- DATE '
                 '(...; fold into ... table at next hand edit)`, the majority form; b454`s in-place edit not used); the 17 cells each naming '
                 'its edition file; row additions in b454`s columns, ids the next free in each table.'),
}


def plan(*a):
    P = plan_data()
    L = ['b618 -- COMPONENT 2: THE PLAN, BANKED BEFORE ANY WRITE, at PLACE-papers %s and relay %s (%s)' % (PRE_PP, PRE_RELAY, utc()),
         '### For each document: its function line, the missed items from relay data/b617_currency.txt, the ruling`s disposition and the '
         'seat`s recommendation side by side; a prompt where they differ (put before the seal), otherwise the ruling`s disposition taken.', '']
    nd = 0
    for n in ORDER:
        x = P[n]
        it = x['items']
        L += ['### %s -- `%s` (%d lines; last %s)' % (n, x['path'], x['lines'], x['last']),
              '    function line :%d %s' % (x['function_line'], x['function'][:400])]
        if n == 'VERIFICATION_LOOM':
            L.append('    missed: %d acts with suite banks since b537 (%s to %s), %d bank files, %d kept failed runs; the loom names %d of them' % (
                it['acts'], it['first'], it['last'], it['banks'], it['kept_failed'], it['loom_mentions']))
        elif n == 'INSTRUMENTS':
            L += ['    missed: %-52s %s :%s' % (y['item'], y['where'], y['line']) for y in it['located']]
            L.append('    missed, not located by b617: %s' % it['unlocated'])
        elif n in ('THE_METHOD_CANON', 'THE_METHOD_AS_IT_STANDS'):
            L += ['    missed: %-52s %s :%s' % (y['item'][:52], y['where'], y['line']) for y in it['forms']]
        elif n == 'FACES_LEDGER':
            L += ['    missed: %-12s `%s` (%s)' % (y['face'], y['decl'], y['pin']) for y in it['faces'] if not y['in_ledger']]
        elif n == 'THE_LOAD_BEARING_MAP':
            L.append('    missed: %d of %d page nodes absent from the map -- %s' % (it['absent'], it['nodes'], ', '.join(it['absent_names'])))
        elif n == 'GAUGE_AND_INVARIANT':
            L.append('    missed: none (the ruling names no item; trail heads naming its function since its last commit: %s)' % (it['trail_heads'] or 'NONE'))
        elif n == 'REGISTRY':
            L += ['    missed: %-60s %s :%s' % (y['item'][:60], y['where'], y['line']) for y in it['ruled']]
            L.append('    missed: %d files added since its last commit that it does not name -- %s' % (len(it['unnamed']), ', '.join(it['unnamed'])))
        s = SEAT[n]
        nd += s[0] == 'DIFFERS'
        L += ['    ### THE RULING`S DISPOSITION : %s' % RULING[n],
              '    ### THE SEAT`S RECOMMENDATION : %s -- %s' % s, '    ### THE PRICE : %d' % x['price'], '']
    L += ['### ### **THE SEAT`S RECOMMENDATION DIFFERS FROM THE RULING`S DISPOSITION ON %d OF 8 DOCUMENTS** (REGISTRY; the prompt put before '
          'the seal, the author`s answer taken). INSTRUMENTS` id range is a fact correction, not a disposition.**' % nd]
    put_txt('b618_plan.txt', L)
    put_json('b618_plan.json', dict(at=utc(), differs=[n for n in ORDER if SEAT[n][0] == 'DIFFERS'], docs=P))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE DRAFTS
MARK = {
    'VERIFICATION_LOOM': '<!-- b618 loom entry -->',
    'INSTRUMENTS': '<!-- b618 (R228)(2)(ii) INSTRUMENTS I-16 TO I-39, 2026-10-04 -->',
    'THE_METHOD_CANON': '<!-- b618 (R228)(2)(iii) THE EDITION FORM AND THE SYNTHESIS FORM, 2026-10-04 -->',
    'THE_METHOD_AS_IT_STANDS': '<!-- b618 (R228)(2)(iv) THE EDITION FORM AND THE SYNTHESIS FORM, 2026-10-04 -->',
    'FACES_LEDGER': '<!-- b618 (R228)(2)(v) faces update -->',
    'THE_LOAD_BEARING_MAP': '<!-- b618 (R228)(2)(vi) THE MAP BY POINTER, 2026-10-04 -->',
    'GAUGE_AND_INVARIANT': '<!-- b618 (R228)(2)(vii) currency line, 2026-10-04 -->',
    'REGISTRY': '<!-- b618 (R228)(2)(viii) ROW UPDATE, 2026-10-04 -->',
}
LOCATED = ('THE_LOCATED_CLAUSE_METHOD.md', 'modules/2026-08/', '19066344b41299a341b017ada33b4c5174a1b221976f8740c26fba1a2c7211ec')


def d_loom():
    rows = loom_rows()
    B = ['', MARK['VERIFICATION_LOOM'], '',
         '### **THE SUITE VERDICTS OF b537–b617, ONE ROW PER ACT — filed 2026-10-04 (b618)**', '',
         'Filed under the author’s ruling `(R228)`(2)(i). **The verdict record since b537 lives in the relay’s suite banks and in each act’s '
         'FINDINGS entry, and this loom carries the table of them.** Each act banks its suite’s reading before its push (relay '
         '`data/bNNN_checks.txt`) and after it (`data/bNNN_checks_postpush.txt`); a failed run it kept beside those two is named in the fourth '
         'column with its own count. The counts are each bank’s own count line, *live passing of arms run*, read at relay `%s`; the FINDINGS column '
         'lists every `## ` heading the act wrote, by `git blame` at PLACE-papers `%s`, the last of them the act’s entry. Nothing above this '
         'entry is edited.' % (PRE_RELAY, PRE_PP), '',
         '| act | suite, pre-push | suite, post-push | kept failed runs, by bank name | FINDINGS entry |', '|:--|:--|:--|:--|:--|']
    failed = lambda c: c is None or c[0] < c[1]   # noqa: E731
    for r in rows:
        kept = ' · '.join('`%s` (%s)' % (f, _cnt(c)) for f, c in r['kept'] if failed(c)) or '—'
        fe = ', '.join(':%d' % x for x in r['findings']) or 'none (the act’s record is on OPEN_TRAILS alone)'
        B.append('| %s | %s | %s | %s | %s |' % (r['act'], _cnt(r['pre']), _cnt(r['post']), kept, fe))
    nk = sum(1 for r in rows for _f, c in r['kept'] if failed(c))
    passed = ['`%s` (%s)' % (f, _cnt(c)) for r in rows for f, c in r['kept'] if not failed(c)]
    B += ['', '*%d acts, %d kept failed runs, each the record of a run that did not read clean, its cause in that act’s record; kept beside '
          'them and passing, not listed above: %s. Nothing deposits.*' % (len(rows), nk, ', '.join(passed) or 'none')]
    return B, dict(rows=rows)


def d_instruments():
    B = ['', MARK['INSTRUMENTS'], '',
         '*Fed 2026-10-04 by b618 under the author’s ruling `(R228)`(2)(ii): the instruments the ledgers entered after this document’s last '
         'commit (847e433, 2026-09-10), one entry each, I-16 to I-39, the ids following I-15. Each entry names what the instrument reads, what it '
         'decides, the OPEN_TRAILS line that entered it and the act; that line is the instrument’s text of record, and the entry points to it '
         'without superseding it. Nothing above this line is edited.*']
    out = []
    for k, x in enumerate(INSTR):
        i = 'I-%d' % (FIRST_I + k)
        B += ['', '## %s — %s (entered %s by %s, under %s; provenance: %s :%d)' % (i, x[0], _date_of(x[2]), x[4], x[5], x[1], x[2]), '',
              '**Reads.** %s. **Decides.** %s. **Entered.** %s :%d, by %s.' % (_cap(x[6]), _cap(x[7]), x[1], x[2], x[4])]
        out.append(dict(id=i, title=x[0], line=x[2], act=x[4]))
    B += ['', '*Twenty-four entries, I-16 to I-39, each resolving to its line on OPEN_TRAILS at PLACE-papers %s. Nothing deposits.*' % PRE_PP]
    return B, dict(entries=out)


def _cap(s):
    return s if re.match(r'^b\d', s) else s[0].upper() + s[1:]


def _date_of(ln):
    """### the date the line entered OPEN_TRAILS: its own `*Appended DATE` head, else the author date, in the author's own zone, of the
    ### commit that wrote it (git blame)"""
    l = lines_of(_show(PP, PRE_PP, 'OPEN_TRAILS.md'))[ln - 1]
    m = re.match(r'^\*Appended (2026-\d\d-\d\d)', l)
    if m:
        return m.group(1)
    t = g(PP, 'blame', '--line-porcelain', '-L', '%d,%d' % (ln, ln), PRE_PP, '--', 'OPEN_TRAILS.md')
    m, z = re.search(r'^author-time (\d+)', t, re.M), re.search(r'^author-tz ([+-])(\d\d)(\d\d)', t, re.M)
    if not m:
        return '?'
    off = (1 if not z or z.group(1) == '+' else -1) * ((int(z.group(2)) * 3600 + int(z.group(3)) * 60) if z else 0)
    return time.strftime('%Y-%m-%d', time.gmtime(int(m.group(1)) + off))


def _forms_body(where):
    return [
        '**The edition form.** A keystone’s next version written beside the current one, the current unedited, from its tier block and its '
        'CP-1b work-list with the page its objects sit on as its spine (OPEN_TRAILS :11864, b577, `(R187)`(5)–(6)); its clauses, each on its '
        'own trail line -- H28b restated and final (:11902, :11930), the stem, ceiling and history clauses (:11904, :11906, :11908), the re-pin '
        'step (:11932), the name-and-title exception (:11934) and its item-name clause (:12082), the fact and placement clauses (:11954, :11956), '
        'the dated-entry and era-annotation lines (:12044, :12194), the page and restatement clauses (:12190, :12192), H28b for a reorganising '
        'edition (:12456), the multi-act clause (:12496) -- and the precedence order among them (:12228). INSTRUMENTS I-16 to I-33 carries one '
        'entry for each.',
        '',
        '**The synthesis form.** The keystone a cluster lacks, written from the cluster’s own papers read at address, one new document per '
        'cluster in the cluster’s folder, every claim graded by its paper’s own text, a Correspondence table carrying every load-bearing claim, '
        'the sieve’s five tests on any claim that is a route (OPEN_TRAILS :12566, b610, `(R220)`(5)); its three clauses -- the table’s place '
        'following the tier the rows earn, the title naming the cluster’s objects, the head’s one line that the document synthesises its papers '
        'and certifies nothing they do not (:12601, b611, `(R221)`(3)) -- and its fourth, the KC tier’s load-bearing clause (:12699, b615, '
        '`(R225)`(2)). Six documents were written by it, b611 to b616.',
        '',
        '**The located-clause method.** Its document is `%s` in TECHNE-Core, `%s`, sha256 `%s`, local and private (FINDINGS :6760); it is named '
        'here by file and digest alone, and no sentence of its body is carried.' % LOCATED,
        '',
        where]


def d_canon():
    B = ['', '', MARK['THE_METHOD_CANON'], '',
         '## XXI. The edition form and the synthesis form (added 2026-10-04, b618, under the author’s ruling `(R228)`(2)(iii); two forms of the '
         'clarified layer, named with their trail lines; the located-clause method by its file and digest)', '']
    B += _forms_body('*Appended by b618 on the author’s ruling, the section strikeable; it names the forms and points to their lines, and the '
                     'lines are their text of record. No byte above it changes.*')
    return B, {}


def d_asis():
    B = ['', MARK['THE_METHOD_AS_IT_STANDS'], '', '---', '',
         '## Addendum, 2026-10-04 (b618, under the author’s ruling `(R228)`(2)(iv)) — the edition form and the synthesis form', '',
         '*Appended after this document’s own close. The two forms below are named with their trail lines as pointers; they are not added to the '
         'eight laws this self-description is built from, and nothing above this line is edited.*', '']
    B += _forms_body('*Appended by b618; the addendum is strikeable. Nothing deposits.*')
    return B, {}


def d_faces():
    N = page_nodes()
    rows = []
    for face, decl, ver in FACES:
        x = [y for y in N.get(decl, [])]
        x = x[0] if x else None
        rows.append(dict(face=face, decl=decl, q=x['q'] if x else '?', pin=x['pin'] if x else '?', e0=x['e0'] if x else '?',
                         tier=x['tier'] if x else '?', page=x['page'] if x else '?', ver=ver))
    B = [MARK['FACES_LEDGER'], '',
         '## UPDATE — filed 2026-10-04 (b618): the faces compiled at SIDE-explicit-formula v0.17 to v0.21 entered -- simplicity, product, '
         'doubling, Keiper, the window, family', '',
         '*Rows above are never rewritten; this update names no earlier row and edits none. Written through the writer’s `append_block`, under '
         'the author’s ruling (R228)(2)(v). Each face is entered with its declaration at the pin the pages print and its grade in this ledger’s '
         'own vocabulary, the tier, as the pages print it; the statement is the page’s, and the last column names the act and the FINDINGS '
         'entry that entered the face. Bank: relay `data/b618_land_FACES_LEDGER.json`.*',
         '', '| face | declaration, at pin | grade (tier) | entered by |', '|:--|:--|:--|:--|']
    for r in rows:
        B.append('| %s | `%s` (SIDE-explicit-formula %s; the %s page) | %s | %s |' % (
            r['face'], r['q'], r['pin'], r['page'], r['tier'], FACE_STATES[r['decl']]))
    B += ['', '*Nothing about h2 moves; the rows above are unedited. Filed by b618 (relay `data/b618_land_FACES_LEDGER.json`).*']
    return B, dict(faces=rows)


def d_map():
    N = page_nodes()
    CU = _cur()
    names = CU['THE_LOAD_BEARING_MAP']['items']['absent_names']
    rows = []
    for s in names:
        for x in N.get(s, []):
            rows.append(dict(short=s, **x))
    seen, uniq = set(), []
    for r in rows:
        if (r['q'], r['page']) in seen:
            continue
        seen.add((r['q'], r['page']))
        uniq.append(r)
    B = ['', MARK['THE_LOAD_BEARING_MAP'], '',
         '### The map’s function carried by the two pages, by pointer -- the %d page nodes the map does not name, appended 2026-10-04 by '
         'b618 under the author’s ruling (R228)(2)(vi) (no byte above changes)' % len(names), '',
         '*Since this map’s last commit (5a911f4, 2026-09-29) its function -- which terminal '
         'backs which claim -- has been carried for the compiled chain by the two generated pages at their pins: `%s` (the ζ page, from relay '
         '`data/%s`, at SIDE-explicit-formula v0.20 = `914c413`) and `%s` (the χ page, from relay `data/%s`, at v0.21 = `1d5d4dd`), each '
         'declaration with its file and line, pin, statement, premises, E0 read, tier and axioms. The table lists the %d page nodes this map '
         'does not name (relay `data/b617_currency.txt`), by qualified name, with the grade and pin the page prints and the page it sits on; '
         'the pages are the record of each, and this section points to them.*' % (PAGE, NODES['zeta'], DIR_PAGE, NODES['chi'], len(names)), '',
         '| node (qualified name) | E0 read | tier | pin | page |', '|:--|:--|:--|:--|:--|']
    for r in sorted(uniq, key=lambda r: (r['short'].lower(), r['page'])):
        B.append('| `%s` | %s | %s | %s | %s |' % (r['q'], r['e0'], r['tier'] or '—', r['pin'], r['page']))
    found = sorted(set(r['short'] for r in uniq))
    B += ['', '*%d nodes in %d rows (a node on both pages has a row for each). No terminal above is re-ranked and no tier above moves. '
          'Nothing deposits.*' % (len(found), len(uniq))]
    return B, dict(names=names, found=found, rows=uniq, missing=sorted(set(names) - set(found)))


def d_gauge():
    B = ['', MARK['GAUGE_AND_INVARIANT'], '',
         '*Currency read 2026-10-04 by b618 under the author’s ruling `(R228)`(2)(vii): since this document’s last commit (33b6baa, 2026-09-08) '
         'no line of the trails names its function -- the condition under which representation-dependence is gauge -- and the ruling names no '
         'item for it; by the count of relay `data/b617_currency.txt` nothing was missed. Nothing above this line is edited.*']
    return B, {}


def _ver_cell(edfile, between=()):
    v = vline(edfile)
    tail = ''
    if between:
        tail = '; %s beside it' % ', '.join('%s (`%s`)' % (vline(b)[1], b) for b in between)
    return '%s (`%s`%s)' % (v[1], edfile, tail), v


def d_registry():
    out = dict(updates=[], adds=[], pointer=None, internal=None, spinor=None)
    B = ['', MARK['REGISTRY'], '',
         '## Row update — 2026-10-04 (the Version cells of seventeen rows read to their editions since 192077f; b618, under the author’s ruling '
         '`(R228)`(2)(viii); fold into their tables at next hand edit)', '',
         'Appended; **no row above is edited.** Each new cell is the version line of the edition file it names, read from that file’s head at '
         'PLACE-papers `%s`; the edition stands beside the version the row’s File cell names, which is unedited, and the act that wrote it is '
         'in its version line. Banks: relay `data/b618_land_REGISTRY.json`, `data/b618_regcheck.json`.' % PRE_PP, '',
         '| ID | row | Version cell as it stands | Version cell, read from the edition | the edition’s version line |', '|:--|:--|:--|:--|:--|']
    for ln, base, ed in UPDATES:
        r = reg_row(ln)
        cell, v = _ver_cell(ed, MONO_BETWEEN if ed.endswith('v5_17.md') else ())
        B.append('| %s | `REGISTRY.md:%d` | %s | %s | `%s:%d` |' % (r['id'], ln, r['version'], cell, ed, v[0]))
        out['updates'].append(dict(id=r['id'], line=ln, base=base, file_cell=r['file'], old=r['version'], ed=ed, new=v[1], vline=v[0],
                                   fname=fname_ver(ed), cell=cell))
    sv = vline(SPIRAL[1])
    B += ['', '**`SPIRAL_MAP.md`, a pointer, no cell:** `%s` stands at %s (its :%d) beside `SPIRAL_MAP.md`; no REGISTRY row registers the '
          'front-door map, so no Version cell is written for it (the author’s answer before b618’s seal, relay '
          '`data/b618_author_answers.txt`).' % (SPIRAL[1], sv[1], sv[0])]
    out['pointer'] = dict(file=SPIRAL[1], ver=sv[1], line=sv[0])
    # ### the row additions, one section per table
    for tab in ('1.5A', '1.5E', '2B', '2C', '2D', '2F', '2G'):
        rows = [x for x in ADDS if x[0] == tab]
        hp, ht = TABLE_HEAD[tab]
        why = ('the six syntheses and the spine' if tab == '1.5A' else 'the synthesis' if tab != '2C' else
               'four phase2/method documents the programme edits by the form, the author’s answer before b618’s seal')
        B += ['', '<!-- b618 (R228)(2)(viii) ROW ADDITION, 2026-10-04 -->', '',
              '## Row addition — 2026-10-04 (%s; b618, under the author’s ruling `(R228)`(2)(viii): %s; fold into %s at next hand edit)' % (
                  hp, why, ht), '',
              '| ID | Title | File | Version | Conf | Status | Words | Provenance |', '|:---|:------|:-----|:--------|:-----|:-------|:------|:-----------|']
        for t, i, base, cur, act, rule, kind, clu in rows:
            f = cur or base
            v = vline(f)
            tier, tl = _tier(f)
            st = _status(f)
            words = _words(f)
            title = _title(f)
            cell = (_ver_cell(f, SIEVE_BETWEEN)[0] if i == 'p2-41' else '%s (`%s`)' % (v[1], f)) if cur else v[1]
            stp = ('Status from its head (:%d)' % st[0][1]) if st else 'the head carries no status word of the STATUS KEY outside its tables'
            if kind == 'synthesis':
                prov = ('Entered 2026-10-04 (b618) under `(R228)`(2)(viii), from the document’s own head: the synthesis for cluster %s, written '
                        'at %s under `%s`%s; tier %s by its class line (`%s:%d`); Version from its version line (:%d); %s.' % (
                            clu, act, rule, '' if not cur else ' and its v0.2 at b615 under `(R225)`(2)', tier, f, tl, v[0], stp))
            elif kind == 'spine':
                prov = ('Entered 2026-10-04 (b618) on the author’s word at `(R223)`(1) (OPEN_TRAILS :12645), from the document’s own head: the '
                        'Riemann-paths cluster’s spine (its :3), the cluster of Phase 1.2 filed under 1.5A (REGISTRY :780); Version from its '
                        ':%d; the head carries no tier line, so no tier is read into the row; %s.' % (v[0], stp))
            else:
                extra = {'p2-40': ' The Status is the v0.1 line’s (:7), which the v0.2 line (:6) does not restate, as `REGISTRY.md:687` reads it; '
                                  'that row, in a table with no Version column, is noted here and not edited.',
                         'p2-41': ' The unnumbered current version is read as v0.1; v0.2, v0.3 and v0.4 stand beside it (b604, b605, b609).',
                         'p2-39': ' The draft of 2026-08-18 carries no version number and is read as v0.1.',
                         'p2-42': ''}[i]
                prov = ('Entered 2026-10-04 (b618) on the author’s answer before b618’s seal, from the document’s own head: Version from the '
                        'edition’s version line (`%s:%d`), written at %s under `%s`; %s; %s.%s' % (
                            f, v[0], act, rule, ('tier %s by its class line (:%d)' % (tier, tl)) if tier else 'no class line in its head', stp,
                            extra))
            status = 'UNGRADED' if not st else st[0][0]
            B.append('| %s | %s | `%s` | %s | — | %s | %s | %s |' % (i, title, base, cell, status, '{:,}'.format(words), prov))
            out['adds'].append(dict(table=t, id=i, base=base, cur=cur, file=f, ver=v[1], vline=v[0], tier=tier, status=st, words=words,
                                    title=title, cell=cell, fname=fname_ver(f)))
    # ### the two disagreements
    ni, nm = internal_counts()
    sp = spinor_reads()
    out['internal'] = dict(internal=ni, meta=nm)
    out['spinor'] = sp
    lsr = g(SPINOR, 'ls-remote', 'origin', 'refs/tags/v0.1.0^{}').split()
    out['spinor_remote'] = lsr[0][:7] if lsr else None
    if out['spinor_remote'] != sp['v0.1.0']['sha']:
        sys.exit('### SIDE-spinor v0.1.0 AT THE REMOTE (%s) IS NOT THE CLONE`S PEELED SHA (%s) -- NOTHING DRAFTED' % (out['spinor_remote'], sp['v0.1.0']['sha']))
    B += ['', MARK['REGISTRY'], '',
          '## Row update — 2026-10-04 (the INTERNAL section against the REGISTRY-SILENT line; b618, under the author’s ruling `(R228)`(2)(viii), '
          'the item of OPEN_TRAILS :12599(a); fold into the ratification block at next hand edit)', '',
          '`REGISTRY.md:787` reads that `internal/` and `meta/` have no REGISTRY section of any kind, while `REGISTRY.md:333` heads the section '
          '*INTERNAL: Reference Works (not for publication)*, a table of six `internal/` files (:337–:342). **Corrected by this note:** REGISTRY '
          'carries a section for six `internal/` files as reference works not for publication, and none for `meta/`; at PLACE-papers `%s` '
          '`internal/` tracks %d files and `meta/` %d. The ruling the :787 line opens, CENSUS-ONLY and out of release scope, stands as written. '
          'Neither line is edited.' % (PRE_PP, ni, nm),
          '', MARK['REGISTRY'], '',
          '## Row update — 2026-10-04 (`SIDE-spinor` at `REGISTRY.md:731` against SPIRAL_MAP :104; the kernel’s statements read at the pin '
          'before this row was written; b618, under the author’s ruling `(R228)`(2)(viii), the item of OPEN_TRAILS :12599(b))', '',
          'Read at `SIDE-spinor` `v0.1.0` = `%s` (the peeled SHA read at the remote by ls-remote, %s; the pin PATHS and SPIRAL_MAP cite) and '
          'again at HEAD `%s`, identical, `SIDESpinor/Spinor.lean`: :70 `%s`; :75 `%s`. **`REGISTRY.md:731` stands as read:** the first '
          'statement concludes `w = 0` for a complex `w` fixed by multiplication by `Complex.I`, and reaches σ = ½ only through the stipulation '
          'that `w` is the centred coordinate σ − ½, which no kernel statement carries; the second is the centring identity alone. SPIRAL_MAP :104 (v0.7 '
          ':106) says each Phase 1.2 checkpoint kernel forces σ = 1/2; for `SIDE-spinor` that sentence goes beyond the kernel’s statement, and '
          'its correction is SPIRAL_MAP’s, at that document’s next edition. Neither line is edited here.' % (
              sp['v0.1.0']['sha'], DATE, sp['HEAD']['sha'], sp['v0.1.0']['l70'].rstrip(' :='), sp['v0.1.0']['l75'].rstrip(' :=by').rstrip()),
          '', '*Appended by b618. No row above is edited; the tables fold these at their next hand edit. Nothing deposits.*']
    return B, out


DRAFTS = {'VERIFICATION_LOOM': d_loom, 'INSTRUMENTS': d_instruments, 'THE_METHOD_CANON': d_canon, 'THE_METHOD_AS_IT_STANDS': d_asis,
          'FACES_LEDGER': d_faces, 'THE_LOAD_BEARING_MAP': d_map, 'GAUGE_AND_INVARIANT': d_gauge, 'REGISTRY': d_registry}


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b618_scanfile_%s.md' % name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', p], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout, re.search(r'^\s*VERDICT\s*: CLEAN\s*$', r.stdout, re.M) is not None


def ledger_check(*texts):
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def keystone_hits(text):
    """### the generator's own keystone pattern (chain_page.keystones) applied to a text: which page nodes it names, per page"""
    import chain_page as CP
    out = {}
    for k in ('zeta', 'chi'):
        names = [x['name'] for x in CP.read_nodes(os.path.join(D, NODES[k]))[0] if x['source'] == 'kernel']
        short = sorted(set(n.split('.')[-1] for n in names))
        plain = sorted(s for s in short if re.fullmatch(r'[a-z]+', s))
        rest = sorted(s for s in short if s not in plain)
        alts = [r'\b(' + '|'.join(re.escape(s) for s in rest) + r')\b'] if rest else []
        alts += [r'(`' + re.escape(s) + r'`|[A-Za-z0-9_]\.' + re.escape(s) + r'\b)' for s in plain]
        out[k] = sorted(set(m.group(0).strip('`').split('.')[-1] for m in re.finditer('|'.join(alts), text)))
    return out


def draft(name, *a):
    """### data/b618_append_<NAME>.md (the append's exact text, its first line the blank that follows the file's last line) and its
    ### scan, its ceiling read, its ledger-cell check and the page nodes it names, in data/b618_draft_<NAME>.json; printed whole."""
    if name not in DRAFTS:
        sys.exit('usage: draft ' + '|'.join(ORDER))
    B, meta = DRAFTS[name]()
    B = [_poss(l) if name != 'FACES_LEDGER' else l for l in B]
    if name != 'FACES_LEDGER' and (_show(PP, 'HEAD', DOC[name]) or '').endswith(NL + NL) and B and B[0] == '':
        B = B[1:]     # ### the blob already ends in a blank line (INSTRUMENTS, GAUGE_AND_INVARIANT): the draft opens on its marker
    text = NL.join(B) + NL
    sc, clean = _scan_text(text, name)
    ceil = [l[:160] for l in B if CEILING.search(l)]
    cells = ledger_check(text) if name in TT_LEDGERS else []
    kh = keystone_hits(text)
    p = _p('b618_append_%s.md' % name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    put_json('b618_draft_%s.json' % name, dict(at=utc(), doc=DOC[name], lines=len(B), bytes=len(text.encode('utf-8')), sha256=sha(text.encode('utf-8')),
                                               scanner_clean=clean, scan_tail=[l for l in sc.split(NL) if 'VERDICT' in l or 'live' in l][:6],
                                               ceiling=ceil, ledger_cells=cells, keystone_hits=kh, meta=meta))
    if 'quiet' not in a:
        print(text)
    print('  ### %s : %d lines, %d bytes ; scanner %s ; ceiling hits %d %s ; ledger cells %s ; page nodes named %s' % (
        name, len(B), len(text.encode('utf-8')), 'CLEAN' if clean else 'NOT CLEAN', len(ceil), ceil[:3], cells or 'NONE',
        {k: len(v) for k, v in kh.items()}))


def land(name, *a):
    """### after the write: the document on disk (CR removed) must equal its committed blob plus the banked draft, byte for byte. ### For
    ### FACES_LEDGER the write is made here, through its own writer's append_block. ### Banks data/b618_land_<NAME>.json."""
    p = DOC[name]
    text = rd('b618_append_%s.md' % name)
    if not text:
        sys.exit('### NO DRAFT BANKED FOR %s' % name)
    blob = (_show(PP, 'HEAD', p) or '')
    if name == 'FACES_LEDGER':
        import b327_faces_row as FR
        if not blob.endswith(NL):
            sys.exit('### THE LEDGER BLOB DOES NOT END IN A NEWLINE')
        body = text.split(NL)
        body = body[:-1] if body and body[-1] == '' else body
        st, det = FR.append_block(MARK['FACES_LEDGER'], body)
        print('  FACES_LEDGER : %s -- %s' % (st, det))
        if st != 'WRITTEN':
            sys.exit('### THE WRITER DID NOT WRITE')
        want = blob.rstrip(NL) + NL + NL.join(body) + NL
    else:
        want = blob + text     # ### the draft's first line is the blank after the file's last line: blob + draft, byte for byte
    disk = io.open(os.path.join(PP, p), encoding='utf-8', errors='replace', newline='').read().replace(chr(13), '')
    disk = disk[1:] if disk.startswith('\ufeff') else disk
    blob0 = blob[1:] if blob.startswith('\ufeff') else blob
    want = (want[1:] if want and want.startswith('\ufeff') else want)
    ok = disk == want
    prefix = disk.startswith(blob0)
    sc, clean = _scan_text(disk[len(blob0):], name + '_landed')
    o = dict(at=utc(), doc=p, ok=ok, prefix=prefix, added_bytes=len(disk.encode('utf-8')) - len(blob0.encode('utf-8')),
             draft_sha=sha(text.encode('utf-8')), scanner_clean=clean, head_lines=len(lines_of(blob0)), disk_lines=len(lines_of(disk)))
    if not ok:
        dl = list(difflib.unified_diff((want or '').split(NL), disk.split(NL), 'want', 'disk', lineterm='', n=0))[:30]
        o['diff'] = dl
        for x in dl:
            print('    ' + x[:200])
    put_json('b618_land_%s.json' % name, o)
    print('  ### %s landed : disk == committed blob + draft : %s ; blob a true prefix : %s ; +%d bytes ; scanner on the landed bytes %s' % (
        name, ok, prefix, o['added_bytes'], 'CLEAN' if clean else 'NOT CLEAN'))


def regcheck(*a):
    """### H52b: every REGISTRY version cell written, read back from REGISTRY on disk, against the version line of the file it names"""
    t = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8-sig').read().replace(chr(13), '')
    i = t.find(MARK['REGISTRY'])
    tail = t[i:] if i >= 0 else ''
    out = []
    for m in re.finditer(r'(?<![\w.])(v\d+(?:\.\d+)+) \(`([^`]+\.md)`', tail):
        v, f = m.group(1), m.group(2)
        vl = vline(f, 'HEAD')
        out.append(dict(cell=v, file=f, vline=vl[0], file_ver=vl[1], name_ver=fname_ver(f), ok=(v == vl[1]) and (fname_ver(f) in (None, v))))
    for m in re.finditer(r'^\| (1\.5a-\d+|1\.5e-\d+|p2-\d+|p2-d\d+) \| [^|]+ \| `([^`]+)` \| (v\d+(?:\.\d+)+) \|', tail, re.M):
        vl = vline(m.group(2), 'HEAD')
        out.append(dict(cell=m.group(3), file=m.group(2), vline=vl[0], file_ver=vl[1], name_ver=fname_ver(m.group(2)), ok=m.group(3) == vl[1]))
    put_json('b618_regcheck.json', dict(at=utc(), cells=out, n=len(out), ok=sum(x['ok'] for x in out)))
    for x in out:
        print('  %-7s %-8s %-90s :%-3s %s' % ('OK' if x['ok'] else '### BAD', x['cell'], x['file'], x['vline'], x['file_ver']))
    print('  ### ### **H52b READ-BACK : %d of %d cells equal their file`s version line.**' % (sum(x['ok'] for x in out), len(out)))


# ================================================================================ COMPONENT 1: b617 AT ITS WEIGHT
B617_ENTRY = '## The sieve at v0.5: ten conclusions from the six syntheses as rows, 9 DARK and 1 NOT A ROUTE'
W_HEAD = '*Appended 2026-10-04 by b618 to b617’s entry (:%d), under `(R228)`(1) -- b617 AT ITS WEIGHT:*'


def _b617():
    j = lambda p: json.loads(_show(RELAY, PRE_RELAY, 'data/' + p))   # noqa: E731
    S, H, RL, FJ, TJ = j('b617_scores.json'), j('b617_h51.json'), j('b617_record_lines.json'), j('b617_findings.json'), j('b617_trail.json')
    chk = {n: _count(_show(RELAY, PRE_RELAY, 'data/' + n)) for n in ('b617_checks.txt', 'b617_checks_postpush.txt')}
    return dict(S={k: v[0] for k, v in S.items()}, H=H, RL=RL, FJ=FJ, TJ=TJ, chk=chk)


def _weight(entry):
    W = _b617()
    S, H, chk = W['S'], W['H'], W['chk']
    rl = dict(zip(('fact', 'currency', 'weight'), [x['line'] for x in W['RL']['lines']]))
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else [S[k] for k in ks]   # noqa: E731
    c5 = H['c5']
    return ('\n%s THE_FINDINGS_AS_THEY_STAND v0.5 (PLACE-papers 4d182cf; ERRATA 3b19f3e; the pages 45dae72 and b92025c; the record 138ea0c): '
            'RH-61 to RH-70 entered after RH-60 and one register, the symmetry and its level curves; the head at %d rows -- %d BRIGHT, %d DARK, '
            '%d NOT A ROUTE, %d FACE; the body %+d at the strict count; the carried back matter re-pinned 385 of 385; the scanner clean. Seven of '
            'the nine routes DARK by test 2 at RH-60’s instrument, one by test 4, one by test 1. ERRATA E-2026-10-04-5 (:901), -6 (:916) and -7 '
            '(:931). FINDINGS :%d, :%d; OPEN_TRAILS :%d (the 2G fact items, relay data/b617_arith.txt), :%d (b618 priced), :%d. Relay 9d80f449, '
            '237f7762, 6d813af6. The verdicts, as relay data/b617_scores.json prints them: H51a-H51c %s; N1-N5 %s; S1-S5 %s; H28a-H28c %s; the '
            'suite %d of %d before the push and %d of %d after it. Defect (a), the seat’s: an errata entry named a later entry by its id, '
            'ERRATA cut back to its committed version on a verified prefix and the three entries appended again. Confirmed by the author: the '
            'ten rows’ clusters, registers, shapes and face cells; RH-68, THEORY_SPACE’s inventory of known mechanisms, distinct from RH-60. Two '
            'of the navigator’s, corrected: the T7_CMB item -- 3 once and −1 six times is the spectrum of neither K₇ (6 once, −1 six times) nor '
            'the incidence matrix (3 once, six of modulus √2), entered as computed; THE_METHOD_CANON’s last commit is b588’s append of '
            '2026-10-01, not 2026-09-08. The generator’s channels -- relay tools/chain_page.py’s back-matter channel and its entry-tag reading '
            'of a structure, b596 (FINDINGS :6856, relay cfd9aeac) -- were recorded at that act and not on the trails as an instrument; b618 '
            'reads them on the trails at :12280, in b596’s record of the author’s answers, and enters them as an instrument at INSTRUMENTS. '
            'Nothing deposited; no kernel touched.\n' % (
                W_HEAD % entry, sum(c5.values()), c5['BRIGHT'], c5['DARK'], c5['NOT A ROUTE'], c5['FACE'], H['body_dn'], rl['weight'],
                W['FJ']['entry_line'], rl['fact'], rl['currency'], W['TJ']['line'], allh(('H51a', 'H51b', 'H51c'), 'HOLDS'),
                allh(('N1', 'N2', 'N3', 'N4', 'N5'), 'HELD'), allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'),
                'HOLD' if (H['H28a'], H['H28b'], H['H28c']) == ('HOLDS', 'HOLDS', 'HOLDS') else [H['H28a'], H['H28b'], H['H28c']],
                chk['b617_checks.txt'][0], chk['b617_checks.txt'][1], chk['b617_checks_postpush.txt'][0], chk['b617_checks_postpush.txt'][1]))


def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def record_lines(*a):
    """### FINDINGS: b617's weight, addressed to b617's entry, appended at the end."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B617_ENTRY)
    if entry != 7368:
        sys.exit('### THE ADDRESSED LINE MOVED (%s) -- NOTHING WRITTEN' % entry)
    wt = _weight(entry)
    bad = ledger_check(wt)
    nd, _n = _nd(wt)
    sc, clean = _scan_text(wt, 'weight')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(wt)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    r = Q.append_to(Q.FIND, wt)
    out = [dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r)]
    put_json('b618_record_lines.json', dict(entry=entry, lines=out))
    print('  FINDINGS.md :%s' % out[0]['line'])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b618_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b618_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b618_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b618 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b618_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b618_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H52a', 'H52b', 'H52c', 'H52d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
COMMIT_PREFIX = {n: 'b618 (R228)(2)(%s): %s' % (r, DOC[n]) for n, r in zip(ORDER, ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii'))}
TABLE_CELLS = [('SIDE-explicit-formula', 'SIDEExplicitFormula.Keiper.keiperTaylorIdentity_of'),
               ('SIDE-explicit-formula', 'SIDEExplicitFormula.Schema.PlateauRamp.plateauRampWindow_of')]
S4_EXPECT = {'zeta': [], 'chi': ['phase1.5/method/THE_LOAD_BEARING_MAP.md']}   # ### the Placement rows each page gains, from the drafts


def _pp_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL)
            if l.strip()]


def _files(h):
    return sorted(x for x in g(PP, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def _appended(n, rev='HEAD'):
    """### the bytes a document gained since PRE_PP at rev (CR removed, BOM removed), or None when PRE_PP's blob is not its prefix"""
    a = (_show(PP, PRE_PP, DOC[n]) or '').lstrip('﻿')
    b = (_show(PP, rev, DOC[n]) or '').lstrip('﻿')
    return b[len(a):] if b.startswith(a) else None


def h52(rev='HEAD'):
    """### H52a's item count: every item of the currency bank found in the bytes its document gained, or pointed to its home"""
    CU = _cur()
    A = {n: _appended(n, rev) or '' for n in ORDER}
    it = []
    for a_ in range(537, 617):
        it.append(('VERIFICATION_LOOM', 'b%d' % a_, ('| b%d | ' % a_) in A['VERIFICATION_LOOM']))
    for k, x in enumerate(INSTR):
        it.append(('INSTRUMENTS', x[0], ('## I-%d — %s (' % (FIRST_I + k, x[0])) in A['INSTRUMENTS']))
    for n in ('THE_METHOD_CANON', 'THE_METHOD_AS_IT_STANDS'):
        it.append((n, 'the edition form', '**The edition form.**' in A[n] and ':11864' in A[n]))
        it.append((n, 'the located-clause method`s form', LOCATED[2] in A[n] and 'FINDINGS :6760' in A[n]))
    for y in CU['FACES_LEDGER']['items']['faces']:
        it.append(('FACES_LEDGER', y['decl'], ('.%s`' % y['decl']) in A['FACES_LEDGER']))
    for s in CU['THE_LOAD_BEARING_MAP']['items']['absent_names']:
        it.append(('THE_LOAD_BEARING_MAP', s, re.search(r'\| `[A-Za-z0-9_.]*\b%s` \|' % re.escape(s), A['THE_LOAD_BEARING_MAP']) is not None))
    it.append(('GAUGE_AND_INVARIANT', 'the dated line (no item)', 'nothing was missed' in A['GAUGE_AND_INVARIANT']))
    R = A['REGISTRY']
    it.append(('REGISTRY', 'the spine`s row', '| 1.5a-10 | ' in R and 'THE_RIEMANN_PATHS_CLUSTER_SPINE.md' in R))
    it.append(('REGISTRY', 'the disagreement :787 / :333', '`REGISTRY.md:787`' in R and '`REGISTRY.md:333`' in R))
    it.append(('REGISTRY', 'the disagreement :731 / SPIRAL_MAP :104', '`REGISTRY.md:731`' in R and 'SPIRAL_MAP :104' in R and 'theorem spinor_forces_half' in R))
    for f in CU['REGISTRY']['items']['unnamed']:
        it.append(('REGISTRY', f, ('`%s`' % f) in R))
    return it


def scores(*a):
    P = jl('b618_plan.json')
    lands = {n: (jl('b618_land_%s.json' % n) if os.path.exists(_p('b618_land_%s.json' % n)) else {}) for n in ORDER}
    drafts = {n: (jl('b618_draft_%s.json' % n) if os.path.exists(_p('b618_draft_%s.json' % n)) else {}) for n in ORDER}
    RC = jl('b618_regcheck.json') if os.path.exists(_p('b618_regcheck.json')) else {}
    Z, X = (jl('b618_page_%s.json' % k) if os.path.exists(_p('b618_page_%s.json' % k)) else {} for k in ('zeta', 'chi'))
    it = h52()
    miss = [(d, i) for d, i, ok in it if not ok]
    ins = instr_resolve()
    face = jl('b618_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state().items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    commits = _pp_commits()
    files = {h: _files(h) for h, _s in commits}
    order = []
    alone = {}
    for n in ORDER:
        c = [h for h, f in files.items() if DOC[n] in f]
        alone[n] = len(c) == 1 and files[c[0]] == [DOC[n]] and dict(commits)[c[0]].startswith(COMMIT_PREFIX[n])
        order.append([h for h, _s in commits].index(c[0]) if c else -1)
    in_order = order == sorted(order) and -1 not in order
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    trail_pending = not os.path.exists(_p('b618_trail.json'))   # ### OPEN_TRAILS' one write is the trail record, made after the scores
    want_pp = sorted([DOC[n] for n in ORDER] + ['FINDINGS.md'] + ([] if trail_pending else ['OPEN_TRAILS.md'])
                     + [p['page'] for p in (Z, X) if p.get('changed')])
    created = [x for x in g(PP, 'diff', '--name-only', '--diff-filter=ADR', PRE_PP, 'HEAD').split(NL) if x.strip()]
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b618_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b617_closing_push_out.txt'))
    clean_d = {n: bool(drafts[n].get('scanner_clean')) for n in ORDER}
    clean_l = {n: bool(lands[n].get('scanner_clean')) for n in ORDER}
    ok_l = {n: bool(lands[n].get('ok')) and bool(lands[n].get('prefix')) for n in ORDER}
    first_commit_t = min([int(g(PP, 'log', '-1', '--format=%ct', h).strip()) for h, _s in commits if any(DOC[n] in files[h] for n in ORDER)] or [0])
    plan_t = R2_epoch(P.get('at'))
    arms2 = rd('b618_page_arms_c2.txt')
    gained = {k: [m.group(1) for m in (re.match(r'^\+\| keystone naming a node \| `([^`]+)` \|$', x) for x in (p.get('diff') or [])) if m]
              for k, p in (('zeta', Z), ('chi', X))}
    lost = {k: [x for x in (p.get('diff') or []) if x[:1] == '-' and not x.startswith('---')] for k, p in (('zeta', Z), ('chi', X))}
    S = {
        'H52a': ('HOLDS' if not miss else 'REFUTED', '%d of %d currency items landed or pointed to their homes ; by document %s ; missing %s' % (
            len(it) - len(miss), len(it), {n: '%d/%d' % (sum(1 for d, _i, ok in it if d == n and ok), sum(1 for d, _i, _o in it if d == n)) for n in ORDER},
            miss[:10] or 'none')),
        'H52b': ('HOLDS' if RC.get('n') and RC.get('ok') == RC.get('n') else 'REFUTED', 'REGISTRY`s version cells read back from the file on disk: '
                 '%s of %s equal the version line of the file each names' % (RC.get('ok'), RC.get('n'))),
        'H52c': ('HOLDS' if len(ins) == 24 and all(x['ok'] for x in ins) else 'REFUTED', 'INSTRUMENTS I-16 to I-39: %d of %d resolve to their '
                 'OPEN_TRAILS line at HEAD, its needle on it' % (sum(x['ok'] for x in ins), len(ins))),
        'H52d': ('HOLDS' if all(clean_d.values()) and all(clean_l.values()) else 'REFUTED', 'the scanner on each draft %s and on each landed '
                 'append %s' % (sum(clean_d.values()), sum(clean_l.values())) + ' of 8'),
        'N1': ('HELD' if len(P.get('differs', [])) <= 2 else 'REFUTED', 'the seat`s recommendation differs from the ruling`s disposition on %d '
               'document(s): %s' % (len(P.get('differs', [])), P.get('differs'))),
        'N2': ('HELD' if RC.get('n') and RC.get('ok') == RC.get('n') else 'REFUTED', 'every REGISTRY version cell reads back equal to its file`s '
               'version line: %s of %s' % (RC.get('ok'), RC.get('n'))),
        'N3': ('HELD' if len(ins) >= 20 and all(x['ok'] for x in ins) else 'REFUTED', 'INSTRUMENTS gains %d entries, %d resolving to a trail '
               'line' % (len(ins), sum(x['ok'] for x in ins))),
        'N4': ('HELD' if all(clean_l.values()) and all(clean_d.values()) else 'REFUTED', 'the scanner CLEAN on %d of 8 landed appends (drafts %d '
               'of 8)' % (sum(clean_l.values()), sum(clean_d.values()))),
        'N5': ('HELD' if kern_same and not created and all(ok_l.values()) and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved since the face %s; documents created, deleted or renamed %s; every append the committed '
               'blob plus its draft %s; PLACE-papers %s (wanted %s%s); relay beyond the act`s banks, tools and the table %s' % (
                   kern_same, created or 'none', ok_l, pp_ch, want_pp, ', OPEN_TRAILS pending the trail record' if trail_pending else '',
                   relay_beyond)),
        'S1': ('HELD' if plan_t and first_commit_t and plan_t < first_commit_t else 'REFUTED', 'the plan banked at %s, before the first '
               'append`s commit at %s' % (P.get('at'), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(first_commit_t)) if first_commit_t else None)),
        'S2': ('HELD' if all(ok_l.values()) else 'REFUTED', 'each document on disk equal to its committed pre-act blob plus its banked draft, '
               'byte for byte: %s' % ok_l),
        'S3': ('HELD' if all(alone.values()) and in_order else 'REFUTED', 'each append committed alone %s, in the order of (R228)(2): %s' % (
            alone, in_order)),
        'S4': ('HELD' if gained == S4_EXPECT and all(len(lost[k]) == 0 for k in lost) else 'REFUTED', 'the Placement rows each page gained %s '
               '(expected %s), rows lost %s' % (gained, S4_EXPECT, {k: len(v) for k, v in lost.items()})),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b618_scores.json', S)
    put_json('b618_h52.json', dict(at=utc(), items=[dict(doc=d, item=i, ok=ok) for d, i, ok in it], instruments=ins))
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


def R2_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _title_entry():
    LJ = jl('b618_draft_VERIFICATION_LOOM.json')
    RJ = jl('b618_draft_REGISTRY.json')['meta']
    return ('## The living documents’ currency: eight documents fed in their own forms — the loom’s %d-row table, INSTRUMENTS I-16 to I-39, '
            'the faces at v0.17–v0.21, the load-bearing map’s 76 nodes by pointer, REGISTRY’s %d row updates and %d row additions' % (
                len(LJ['meta']['rows']), len(RJ['updates']), len(RJ['adds'])))


TRAIL_HEAD = ('### b618 — lane three, act forty-five under (R228): the living documents’ currency -- eight documents read for their functions '
              'and fed in their own forms with what the record carried past them')


def _finding_text():
    S, rl = jl('b618_scores.json'), jl('b618_record_lines.json')
    RJ = jl('b618_draft_REGISTRY.json')['meta']
    t = _title_entry()
    cm = {n: next((h for h, s in _pp_commits() if s.startswith(COMMIT_PREFIX[n])), '?') for n in ORDER}
    e = ['', t, '',
         '*Filed at b618 on the author’s ruling `(R228)`. Banks: relay `data/b618_reads.txt`, `data/b618_plan.txt`, `data/b618_append_*.md`, '
         '`data/b618_land_*.json`, `data/b618_regcheck.json`, `data/b618_h52.json`, `data/b618_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The appends** (`(R228)`(2)), each in its document’s own form, dated, written through the Edit tool or, for FACES_LEDGER, its own '
         'writer, read back as the committed blob plus the banked draft byte for byte, and committed alone: VERIFICATION_LOOM (%s) one table, '
         'a row per act b537–b617, its head line saying the verdict record lives in the relay’s suite banks and the FINDINGS entries; '
         'INSTRUMENTS (%s) I-16 to I-39, the edition form, its sixteen clauses, the precedence order, the frozen control, the five tests, the '
         'pin-resolution, load-bearing and one-read rules and the generator’s channels, each with what it reads, what it decides and its '
         'trail line; THE_METHOD_CANON (%s) section XXI and THE_METHOD_AS_IT_STANDS (%s) an addendum, the edition and synthesis forms by '
         'their trail lines and the located-clause method by file and sha256; FACES_LEDGER (%s) one update, the six faces of v0.17–v0.21 at '
         'their pins with their tiers; THE_LOAD_BEARING_MAP (%s) a section by pointer, the 76 page nodes by qualified name and grade with '
         'their pages; GAUGE_AND_INVARIANT (%s) one dated line, nothing missed; REGISTRY (%s) %d Version cells in its row-update form, %d '
         'rows in its row-addition form (the six syntheses, the spine, and four phase2/method documents on the author’s answer), the pointer '
         'line for SPIRAL_MAP, and the two disagreements -- `REGISTRY.md:787` corrected against :333, and :731 standing against SPIRAL_MAP '
         ':104 with `SIDE-spinor`’s statements read at v0.1.0. No document created or retired.' % (
             cm['VERIFICATION_LOOM'], cm['INSTRUMENTS'], cm['THE_METHOD_CANON'], cm['THE_METHOD_AS_IT_STANDS'], cm['FACES_LEDGER'],
             cm['THE_LOAD_BEARING_MAP'], cm['GAUGE_AND_INVARIANT'], cm['REGISTRY'], len(RJ['updates']), len(RJ['adds'])), '',
         '**The record line.** b617’s weight at FINDINGS :%d, the author’s confirmations and the navigator’s two corrections; the generator’s '
         'channels read on the trails at :12280.' % rl['lines'][0]['line'], '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the currency b617 priced (OPEN_TRAILS :12755) lands where each document’s function '
         'line puts it -- the loom takes the suite banks the acts since b537 (:4788 to :7368) left outside it; INSTRUMENTS takes the form b577 '
         'entered (:11864) and the rules confirmed at b604, b612 and b615 (:7060, :7278, :7322); FACES_LEDGER takes the faces b596 to b603 '
         'compiled (:6856, :6950, :6972, :6998, :7028), beside b547’s update (:5587); the load-bearing map points to the pages b568 began '
         '(:6246); REGISTRY takes the editions of CP-7 and CP-8 (:6478 to :7158) and the syntheses (:7240 to :7346). It strengthens the '
         'programme’s offering of a record a reader can enter at any of its living documents: each now says, in its own form, what the '
         'record carried past it and where it lives.', '',
         '**Next.** Per `(R228)`(3): b619, THE_KEYSTONE_CENSUS’s v0.4; then W-ORD-SECOND-READER’s batch. The author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; no current version edited beyond its dated append; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.*', '']
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
    put_json('b618_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = (
    '(1) INSTRUMENTS’ ids: the ruling’s “I-8 onward” meets the document’s own I-8 to I-15, so the entries take I-16 to I-39, a fact '
    'correction, the navigator’s; (2) the generator’s channels stand on the trails at :12280, in b596’s record of the author’s answers, '
    'which the ruling’s “not on the trails as an instrument” leaves open -- entered at I-39 from that line; (3) FACES_LEDGER’s grade column '
    'carries the tier as the pages print it, and terminal_table.py reads FACES_LEDGER as a ledger, so the two T2-INTERFACES faces '
    '(keiperTaylorIdentity_of, plateauRampWindow_of) take that grade in the table, declared on the face; (4) REGISTRY’s row updates in its '
    'majority append form (“fold into the table at next hand edit”), b454’s in-place cell edit not used; the new ids the next free in each '
    'table; REPARAMETERIZATION’s Status read from its v0.1 line; (5) THE_METHOD_AS_IT_STANDS carries no append form of its own, so its '
    'addendum follows its closing line under a marked comment')


def _trail_text():
    S, fj, rl = jl('b618_scores.json'), jl('b618_findings.json'), jl('b618_record_lines.json')
    RJ = jl('b618_draft_REGISTRY.json')['meta']
    rows_ = ['', TRAIL_HEAD, '',
             '**(R228) ratified.** (1) b617 at its weight; the seat’s readings confirmed and two of the navigator’s corrected. (2) The living '
             'documents’ currency, each document fed in its own form; H52a-H52d. (3) The act after: b619, THE_KEYSTONE_CENSUS’s v0.4.', '',
             '**Entered:** FINDINGS.md:%d (b617’s weight), :%d (the entry, with its mutual-light line); this record; the eight appends, each '
             'committed alone in PLACE-papers; relay data/b618_plan.txt, data/b618_append_*.md, data/b618_land_*.json, data/b618_regcheck.json.' % (
                 rl['lines'][0]['line'], fj['entry_line']), '',
             '**Answered before the seal, by the author** (relay data/b618_author_answers.txt): REGISTRY’s five bases with no Version-column row '
             '-- rows in the row-addition form for FACES_OF_H2_AT_FINITE_INSTANCE, REPARAMETERIZATION_BARRIERS, THE_FINDINGS_AS_THEY_STAND and '
             'THE_KEYSTONE_CENSUS, the pointer line for SPIRAL_MAP; “nothing else” recorded as the navigator’s, written before the seat read '
             'which bases have a Version column.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**b619 priced** (`(R228)`(3)): THE_KEYSTONE_CENSUS v0.3’s keystone-less rows, six of them now carrying a synthesis entered in '
             'REGISTRY at this act (1.5a-9, 1.5e-7, p2-36, p2-37, p2-38, p2-d10), each row read again for its keystone; then '
             'W-ORD-SECOND-READER’s batch.', '',
             '**Defects** (relay data/b618_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R228)`(3), b619, THE_KEYSTONE_CENSUS’s v0.4; then W-ORD-SECOND-READER’s batch; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; row U1 unedited; `h2` where the deposit left it; the four lists '
             'stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b618_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b618_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-04 by b618 to its own record (:%d) -- DEFECT (d), THE TABLE CELLS CORRECTED:*'


def correction(*a):
    """### OPEN_TRAILS: the dated correction line addressed to this act's record, appended at the end (b603's (i) form)."""
    import terminal_table as TT
    Q = R2._Q()
    tl = jl('b618_trail.json')['line']
    cells = [c for c in TT.grade_cells() if c['name'].split('.')[-1] in ('keiperTaylorIdentity_of', 'plateauRampWindow_of')]
    diff = json.loads(rd('terminal_table_diff.json') or '{}')
    t = ('\n%s the record’s item (3), and the FACES_LEDGER commit (bff682d), say the two T2-INTERFACES faces, keiperTaylorIdentity_of and '
         'plateauRampWindow_of, take an INTERFACES cell in the terminal table; the table regenerated by the pre-push suite and by the push '
         'gate moved none (rows added %d, gone %d, grade cells moved %d), the table’s own cell reader reading %d cells for the two names from '
         'FACES_LEDGER’s rows, where the seat’s pre-write check used the bare grade-word pattern. The face’s two TABLE CELL lines (its reading '
         '(vi)) are refuted in letter, and its arm G-TABLE-GRADES-DECLARED fails the pre-push suite in its letter, 77 of 78 (relay '
         'data/b618_checks.txt); no grade moved in the table, and FACES_LEDGER’s rows stand as written. Defect (d), the seat’s.\n' % (
             CORR_HEAD % tl, len(diff.get('added') or []), len(diff.get('gone') or []), len(diff.get('changed') or []), len(cells)))
    bad = ledger_check(t)
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'correction')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(t)
        return
    if bad or any(nd.values()) or not clean or cells or diff.get('changed'):
        sys.exit('### THE LINE WOULD GRADE A NAME, CARRY TECHNE TEXT OR A STEM, OR THE TABLE MOVED -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CORR_HEAD % tl)
    r = Q.append_to(Q.OT, t)
    put_json('b618_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % tl), head=CORR_HEAD % tl, append=r, cells=len(cells)))
    print('  OPEN_TRAILS correction :%s' % jl('b618_correction.json')['line'])


def desk(*a):
    S = jl('b618_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b618 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H52a-H52d, (R228)(2).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H52 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b618_defects.txt').rstrip(NL).split(NL)
    put_txt('b618_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = jl('b618_scores.json'), jl('b618_findings.json'), jl('b618_trail.json'), jl('b618_record_lines.json')
    Z, X = jl('b618_page_zeta.json'), jl('b618_page_chi.json')
    cm = {n: next((h for h, s in _pp_commits() if s.startswith(COMMIT_PREFIX[n])), '?') for n in ORDER}
    L = ['b618 -- THE COMPONENTS, BANKED UNDER (R228).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b617`s closing push-out relay %s ; push-b617* branches deleted by name '
         '(data/b618_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b618_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b617`s weight FINDINGS :%d' % rl['lines'][0]['line'],
         '### COMPONENT 2 : the plan data/b618_plan.txt ; the seat differs on %s' % jl('b618_plan.json').get('differs'),
         '### COMPONENT 3 : the appends, each committed alone -- %s ; H52a %s, H52b %s, H52c %s, H52d %s' % (
             ', '.join('%s %s' % (n, cm[n]) for n in ORDER), S['H52a'][0], S['H52b'][0], S['H52c'][0], S['H52d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b618_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b619 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b618_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b618_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
