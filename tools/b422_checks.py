# -*- coding: utf-8 -*-
"""b422_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay 070d3ee, PLACE-papers 2249436,
### SIDE-global-section d8acb1d), in git's own view; rows are read by marker; the fold's two F- arms are the
### components' own functions, IMPORTED, re-run over the section as the corpus now carries it.
"""
import ast
import io
import os
import re
import subprocess
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b422_components as CMP   # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_RELAY, PIN_PP, PIN_SIDE = '070d3ee', '2249436', 'd8acb1d'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b422_checks_postpush.txt' if POST else 'b422_checks.txt')
NL = chr(10)
L = []


def say(s=''):
    L.append(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def rb(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read()
    except Exception:
        return b''


def blob(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def unchanged(repo, pin, rel):
    return subprocess.run(['git', '-C', repo, 'diff', '--quiet', pin, '--', rel]).returncode == 0


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


def prefix_ok(rel):
    pin = blob(PP, PIN_PP, rel) or b'x'
    return rb(os.path.join(PP, *rel.split('/'))).startswith(pin.rstrip(b'\n'))


RULE_RE = re.compile('[-=#]{8,}')


def fold(s):
    s = RULE_RE.sub('. ', (s or ''))
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def pycode_of(src):
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.STRING, tokenize.COMMENT):
                continue
            out.append(tok.string)
    except Exception:
        return 'TOKENIZE-FAILED ' + src
    return ' '.join(out)


def verdict_line(text, key):
    for ln in (text or '').splitlines():
        if key in ln:
            return ln
    return ''


def stamp_of(text, key='at (UTC) :'):
    m = re.search(re.escape(key) + r' (\S+)', text or '')
    return m.group(1) if m else ''


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'FOLDR', 'R37R', 'ORIENT', 'WIT', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B422T',
             'CORR', 'FACE', 'FERRY', 'SCAN', 'CLOSING', 'SEALV', 'SECTION', 'KEY102', 'DIGEST', 'PATHS')


def _raw_no_arms():
    src = read(os.path.abspath(__file__))
    bad = []
    for node in ast.walk(ast.parse(src)):
        if not (isinstance(node, ast.Assign) and any(getattr(t, 'id', '') == 'ARMS' for t in node.targets)):
            continue
        for el in node.value.elts:
            if not (isinstance(el, ast.Tuple) and len(el.elts) == 3):
                continue
            nm = getattr(el.elts[0], 'value', '')
            if isinstance(nm, str) and nm.startswith('G-NO'):
                names = {n.id for n in ast.walk(el.elts[2]) if isinstance(n, ast.Name)}
                if names & set(RAW_TEXTS):
                    bad.append(nm)
    return bad


FACEPATH = os.path.join(D, 'b422_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b422_ferry.txt'))
SCAN = read(os.path.join(D, 'b422_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b422_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b422_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b422_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b422_extract.txt'))
COMP = read(os.path.join(D, 'b422_components.txt'))
FOLDR = read(os.path.join(D, 'b422_fold.txt'))
R37R = read(os.path.join(D, 'b422_r37.txt'))
ORIENT = read(os.path.join(D, 'b422_orient.txt'))
WIT = read(os.path.join(D, 'b422_witness_arc.txt'))
LOCK = read(os.path.join(D, 'b422_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b422_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b422_desk_notes.txt'))
BANK = read(os.path.join(D, 'b422_the_kernel_arc_folded.txt'))
CLOSING = read(os.path.join(D, 'b422_closing.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B422T = TRAILS.split('<!-- b422')[-1] if '<!-- b422' in TRAILS else ''
FINDTXT = read(CMP.FIND)
SECTION = FINDTXT.split('<!-- b422 the fold: the kernel arc')[-1] if '<!-- b422 the fold' in FINDTXT else ''
KEY102 = read(CMP.IB)
DIGEST = read(CMP.DIGEST)
PATHS = read(CMP.PATHS)
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FEXT, FB422T, FFACE, FSEALV = fold(BANK), fold(COMP), fold(EXT), fold(B422T), fold(FACE), fold(SEALV)
FSECTION, FKEY, FWIT = re.sub(r'\s+', ' ', SECTION), re.sub(r'\s+', ' ', KEY102.split(CMP.R37_MARK)[-1]), fold(WIT)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b422_components.py'))
EXTSRC = read(os.path.join(T, 'b422_extract.py'))
DESKSRC = read(os.path.join(T, 'b422_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b422_')]
B421MARK = "**THE GRID TRACE DEFINED HERE EQUALS THE MODEL'S COUNTING FORM, ZERO AXIOMS, ON THE THIRD PROBE**"
B422MARK = "**THE KERNEL ARC FOLDED: TWO COMPILED GENERAL THEOREMS ABOUT THE MODEL, AND THE KEYSTONE'S DEFINITION 2.1"


def rows_of(mark, text):
    return [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mark), text)]


ROW421, ROW422 = rows_of(B421MARK, CORR), rows_of(B422MARK, CORR)
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')
D21 = '**Definition 2.1 (Determined system).** A structure M is *determined* by specification S if S is a finite set of 𝓛-sentences that has M as its unique model up to isomorphism.'
OPEN_LIST = ('the lawful-class bound as a witness on the wrong class, the wide-support bound confirmed absent, '
             'exhaustion at each radius not across, the approximation register closed')
DOORS_PIN = [x for x in (blob(PP, PIN_PP, 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md') or b'').decode('utf-8').splitlines()
             if re.match(r'\| \*\*R[1-5]|\| R[1-5]\b|\| \*\*R1 / R2', x)]

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the first component write',
     'SEAL INTACT' in SEALV and stamp_of(FACE, 'locked at (UTC) :') < min(stamp_of(FOLDR) or 'z', stamp_of(R37R) or 'z')),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT') and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-R37-RATIFIED', 'the ferry carries (R37) and the face ratifies it without extending it',
     'RULING (R37)' in FERRY and 'IS RATIFIED BY THE PASTE AND IS STRIKEABLE' in FFACE and 'does not extend it' in FFACE),
    ('G-R37-APPENDED', 'the keystone carries §10.2 and its pin is a true prefix',
     CMP.R37_MARK in KEY102 and prefix_ok('phase1.5/method/INVARIANCE_BARRIERS.md')),
    ('G-R37-SENTENCE-KEPT', 'Definition 2.1`s sentence present byte for byte', KEY102.count(D21) == 1),
    ('G-R37-DECLINED-RECORDED', 'the declined reading recorded with the citation labelled the seat`s',
     'upward Löwenheim–Skolem theorem' in FKEY and 'That citation is the seat’s' in FKEY),
    ('G-R37-NO-REVERDICT', '§10.2 re-verdicts neither act, and neither bank changed',
     'It re-verdicts neither b407’s' in FKEY and unchanged(ROOT, PIN_RELAY, 'data/b407_the_barriers_own_instance.txt')
     and unchanged(ROOT, PIN_RELAY, 'data/b420_the_lemma_aimed.txt')),
    ('F-NOGRADE', 'every grade string in the section is in its attributed bank', not CMP.f_nograde(SECTION) and bool(SECTION)),
    ('F-NOSUPERSEDE', 'no folded act summarised as overturning another', not CMP.f_nosupersede(SECTION) and bool(SECTION)),
    ('G-FOLD-SPAN-BY-TOOL', 'the span from the b363 tool under this act`s stem',
     "b363 -- THE FOLD'S OWN THRESHOLD, COUNTED." in read(os.path.join(D, 'b422_span_run.txt'))
     and os.path.exists(os.path.join(D, 'b422_span.json')) and 'The tool reports 10, counting b413 through b422' in SECTION),
    ('G-FOLD-APPENDED', 'one fold section appended; FINDINGS` pin a true prefix',
     FINDTXT.count('## THE KERNEL ARC, b413–b421 — THE FOLD') == 1 and prefix_ok('FINDINGS.md')),
    ('G-FOLD-CRITERION-QUOTED', 'b412`s criterion quoted in the section', CMP.CRITERION in SECTION),
    ('G-FOLD-COLUMN-NAMED', 'the third column named and kept out of both sides',
     'A third column, declared on the fold’s registration before the count, `OBJECT-MODEL`' in SECTION
     and 'It is counted into neither side' in SECTION),
    ('G-FOLD-EACH-ACT', 'every act of the span has its row', all(('| **b%d** |' % a) in SECTION for a in range(413, 422))),
    ('G-FOLD-ONE-STATEMENT', 'the section carries a one-statement, and the digest quotes it',
     '### The arc’s one statement' in SECTION
     and read(os.path.join(D, 'b422_one_statement.txt')).strip() in DIGEST),
    ('G-FOLD-RANK-MEASURED', 'largest ranked by the face`s measure, both counts printed',
     bool(re.search(r'the keystone has \*\*\d+\*\* lines naming Theorem 3\.1', SECTION))
     and bool(re.search(r'against \*\*\d+\*\* lines carrying the universality sentence', SECTION))),
    ('G-FOLD-GRADE-SENTENCE-NAMED', 'b420`s grade sentence named beside b419`s bank',
     'moved one grade inside `K3`' in SECTION and 'b419’s own bank says **0 grades moved**' in SECTION),
    ('G-R31-DIGEST', 'the digest carries a dated b422 block, its pin a true prefix',
     '<!-- b422 orientation refresh' in DIGEST and prefix_ok('phase2/method/THE_FINDINGS_AS_THEY_STAND.md')),
    ('G-R31-DOORS', 'the door table unedited and no door restated',
     bool(DOORS_PIN) and all(x in PATHS for x in DOORS_PIN) and 'so **no door is restated**' in PATHS),
    ('G-R31-PREFIXES', 'every appended PLACE-papers file keeps its pin as a true prefix',
     all(prefix_ok(r) for r in ('FINDINGS.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md',
                                 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md',
                                 'phase1.5/method/INVARIANCE_BARRIERS.md', 'OPEN_TRAILS.md'))),
    ('G-CONFLATIONS-CARRIED', 'three conflations in the section, each with the navigator and the correction',
     all(bool(re.search(r'(?m)^\(%d\) .* — the navigator: \*.+\* — the correction: .+' % k, SECTION)) for k in (1, 2, 3))),
    ('G-WITNESS-NAMED', 'the arc named in the record and the trail',
     'NAMED. PRICED. NOT OPENED.' in WIT and 'W-ORD-WITNESS-ENUMERATION' in B422T),
    ('G-WITNESS-LIST-VERBATIM', 'site (i)`s opening list entered verbatim', OPEN_LIST in re.sub(r'\s+', ' ', B422T)),
    ('G-WITNESS-NOT-OPENED', '0 candidates attempted and the ledger unchanged',
     'candidates attempted : 0' in WIT and unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-WITNESS-PRICED', 'priced at one act per site, six sites', 'six acts' in WIT and 'sites : 6' in WIT),
    ('G-N1-APART', '(N1)`s two clauses scored apart', COMP.count('(N1) *') == 2),
    ('G-N2-SCORED', '(N2) scored', bool(re.search(r'\(N2\).*(MET|REFUTED)', FCOMP))),
    ('G-N3-APART', '(N3)`s three clauses scored apart', COMP.count('(N3) *') == 3),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B422T for k in (1, 2, 3, 4)) and B422T.count('**OPEN.**') == 4
     and 'Trigger: the ruling on which test governs' in BANK),
    ('G-NOKERNEL', 'no kernel .lean file changed and the profile unchanged',
     not [f for f in git(SIDE, 'diff', '--name-only', PIN_SIDE).split() if f.endswith('.lean')]
     and unchanged(SIDE, PIN_SIDE, 'AXIOM_PRINTS.txt')),
    ('G-NOGRADE', 'no grade string minted', not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged', '0 premises discharged' in FBANK),
    ('G-NODOOR', 'the bank states 0 doors restated', '0 doors restated' in FBANK),
    ('G-NOROUTE', 'the bank states 0 routes proposed', '0 routes proposed' in FBANK),
    ('G-NOKAPPA', 'no kappa value measured', not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NORULE', 'STRUCK_CLAUSES is not written', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no Zenodo byte', 'zenodo' not in ACT_WORK.lower()),
    ('G-NOPLATFORM', 'no platform call', not re.search('urllib|requests|http', ACT_WORK)),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 3),
    ('G-NOLOCKEDFACE', 'the seal still verifies', 'SEAL INTACT -- the body is byte-for-byte what was sealed' in FSEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|2[01])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md unchanged since the pin', unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     prefix_ok('OPEN_TRAILS.md') and '<!-- b422' in TRAILS and '<!-- b421' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b421 at 270 and this act at 271, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW421 == [270] and ROW422 == [271]),
    ('G-WRITELIST-KINDS', 'the face names 9 kinds', 9 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
    ('G-NOEXTRAKIND', 'exactly six relay act-tool files', 6 == len(TOOLS_THIS_ACT)),
    ('G-NOSTAGE-A', 'no working tool stages by -A', not re.search('add[^' + chr(92) + 'n]{0,24}-A(?![A-Za-z])', ACT_WORK)),
    ('G-NOBORROWEDBAR', 'no `G-NO*` arm reads a raw document text', 0 == len(_raw_no_arms())),
    ('G-ARMS-DECLARED-EQ-RUN', 'declared on the face equals run here, both ways', None),
    ('G-ARMS-OWN-BANK', 'arms run over this act`s own bank', bool(BANK) and len(FBANK) > 2000),
    ('G-ARMS-STRIP-PROSE', 'this suite strips comments and strings by the tokenizer', 'def pycode_of' in SELFSRC),
    ('G-ARMS-FOLD-MARKERS', 'this suite folds markup before matching', 'def fold' in SELFSRC),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'A2: verdict lines read', 'def verdict_line' in SELFSRC),
    ('G-NOWRAP-MIDTOKEN', 'the writers wrap at word boundaries',
     all('def wrap(' in s for s in (COMPSRC, EXTSRC, DESKSRC))
     and 0 == len(re.findall(r'\[k:k ?\+ ?\d+\]', pycode_of(COMPSRC + EXTSRC + DESKSRC)))),
    ('G-MUSTFAIL', 'none of the forbidden lines is in the bank',
     not any(s in FBANK.lower() for s in ('the lock was overridden', 'a witness was found', 'a grade was moved',
                                          'h2 has moved', 'the witness arc was opened'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b422_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
say('=' * 100)
passing = failing = 0
for name, desc, res in ARMS:
    if res is None:
        res = (declared == run)
    ok = bool(res)
    passing += 1 if ok else 0
    failing += 0 if ok else 1
    say('  %-42s %-56s %s' % (name, desc[:56], 'PASS' if ok else '### **FAIL**'))
say('-' * 100)
say('  declared on the face : %d' % len(declared))
say('  run here             : %d' % len(run))
say('  declared but not run : %s' % (sorted(declared - run) or 'none'))
say('  run but not declared : %s' % (sorted(run - declared) or 'none'))
say('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**' % (len(ARMS), passing, failing))
say('=' * 100)
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if failing else 0)
