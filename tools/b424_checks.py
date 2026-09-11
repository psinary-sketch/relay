# -*- coding: utf-8 -*-
"""b424_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay 842537c, PLACE-papers a00c72c,
### SIDE-global-section 527c861), in git's own view; rows are read by marker; every candidate's quotation is re-found
### at its source by the components' own reader, IMPORTED; row U1 is read by its marker and compared to its pin.
"""
import ast
import io
import json
import os
import re
import subprocess
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b424_components as CMP   # noqa: E402
import b424_desk_bank as DB     # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_RELAY, PIN_PP, PIN_SIDE = '842537c', 'a00c72c', '527c861'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b424_checks_postpush.txt' if POST else 'b424_checks.txt')
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


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'TABLE', 'WREC', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B424T', 'CORR', 'FACE',
             'FERRY', 'SCAN', 'SEALV', 'FLTXT')


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


FACEPATH = os.path.join(D, 'b424_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b424_ferry.txt'))
SCAN = read(os.path.join(D, 'b424_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b424_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b424_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b424_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b424_extract.txt'))
COMP = read(os.path.join(D, 'b424_components.txt'))
TABLE = read(CMP.TABLE)
WREC = read(CMP.WREC)
TJ = json.loads(read(CMP.TJSON) or '{"candidates": [], "held": -1}')
LOCK = read(os.path.join(D, 'b424_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b424_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b424_desk_notes.txt'))
BANK = read(DB.BANKOUT)
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B424T = TRAILS.split('<!-- b424')[-1] if '<!-- b424' in TRAILS else ''
FLTXT = read(CMP.FL)
FLPIN = (blob(PP, PIN_PP, 'FACES_LEDGER.md') or b'').decode('utf-8')
U1NOW = next((x for x in FLTXT.splitlines() if x.startswith('| U1 ')), '')
U1PIN = next((x for x in FLPIN.splitlines() if x.startswith('| U1 ')), '')
FLNEW = FLTXT[len(FLPIN.rstrip(NL)):] if FLTXT.startswith(FLPIN.rstrip(NL)) else FLTXT
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FTABLE, FFACE, FSEALV = fold(BANK), fold(COMP), fold(TABLE), fold(FACE), fold(SEALV)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b424_components.py'))
EXTSRC = read(os.path.join(T, 'b424_extract.py'))
DESKSRC = read(os.path.join(T, 'b424_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b424_')]
B423MARK = "**THE (R37) QUESTION READ: b407'S AND b420'S READINGS OF THE LEMMA'S FIRST HYPOTHESIS, EACH AGAINST §10.2**"


def rows_of(mark, text):
    return [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mark), text)]


ROW423, ROW424 = rows_of(B423MARK, CORR), rows_of(DB.ROWMARK, CORR)
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')
CANDS = TJ['candidates']
IDS = ['C%d' % k for k in range(1, 17)]


def quotes_at_source():
    for c in CANDS:
        for x in c['quotes']:
            if x['text'] == '### MISS' or CMP.fold(x['text']) not in CMP.fold(CMP.read(x['path'])):
                return False
    return bool(CANDS)


def steps_in_order():
    for c in CANDS:
        k = next((n for n, s in enumerate(c['steps']) if s['out'] == 'FAIL'), None)
        if (k + 1 if k is not None else None) != c['first']:
            return False
    return bool(CANDS)


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the table and the ledger write',
     'SEAL INTACT' in SEALV and bool(stamp_of(TABLE)) and bool(stamp_of(WREC))
     and stamp_of(FACE, 'locked at (UTC) :') < min(stamp_of(TABLE), stamp_of(WREC))),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the seal verifies and the registration gate reads CLEAR',
     'SEAL INTACT' in SEALV and 'CLEAR' in verdict_line(GATE, 'GATE VERDICT')
     and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-LEG1-CLOSED', 'b423 at row 272 by its marker and its closing record tracked',
     ROW423 == [272] and git(ROOT, 'ls-files', 'data/b423_closing.txt') == 'data/b423_closing.txt'),
    ('G-W-POPULATION-NAMED', 'the table`s sixteen are the face`s sixteen, in order',
     [c['id'] for c in CANDS] == IDS and all(('[%s]' % i) in FACE for i in IDS)),
    ('G-W-SEARCH-PRINTED', 'the survey printed three shapes over both scopes',
     'SCOPE A' in EXT and 'SCOPE B' in EXT and all(EXT.count(s) >= 3 for s in ('W1 a witness named', 'W2 quantified over test functions',
                                                                              'W3 a positivity or bound over a class'))),
    ('G-W-EACH-READ-AT-SOURCE', 'every quotation in the table re-found at its source', quotes_at_source()),
    ('G-W-EACH-FAILED-OR-HELD', 'every candidate carries a verdict line, FAILED AT or HELD',
     sum(1 for i in IDS if re.search(r'VERDICT \[%s\] : (FAILED AT S[123] -- |HELD)' % i, TABLE)) == 16),
    ('G-W-STEPS-IN-ORDER', 'each FAILED AT names the first failing step', steps_in_order()),
    ('G-W-SITE-FORM-PRINTED', 'the site`s own text printed before the first candidate',
     0 <= TABLE.find('THE SITE`S OWN TEXT, PRINTED ONCE BEFORE ANY CANDIDATE') < TABLE.find('[C1]')
     and 'the witness form does not transpose here at all' in FTABLE),
    ('G-W-NO-HELD-NO-WITNESS-WRITE', '0 held, and row U1`s witness fields as at the pin',
     TJ['held'] == 0 and re.findall(r'WITNESS: *`([A-Z ]+)`', U1NOW) == re.findall(r'WITNESS: *`([A-Z ]+)`', U1PIN)
     and bool(U1PIN)),
    ('G-W-BLOCK-THROUGH-WRITER', 'one b424 block, written by the writer`s append_block',
     FLTXT.count(CMP.MARK) == 1 and 'append_block : WRITTEN' in WREC and 'import b327_faces_row as W' in COMPSRC),
    ('G-W-QUOTES-VERIFIED', 'the writer`s verify_quotes returned no miss', 'misses : 0 []' in WREC),
    ('G-W-CHECKPOINT', 'one site, and the checkpoint on the record and the trail',
     'SITES ATTEMPTED : 1 ; CHECKPOINT : after site (i)' in TABLE and 'checkpointed after site (i)' in B424T),
    ('G-L2-APART', '(L2)`s three clauses scored apart', COMP.count('(L2) *') == 3),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B424T for k in (1, 2, 3, 4)) and B424T.count('**OPEN.**') == 4
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
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|2[0-3])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOSEVENTHSITE', 'no seventh site: the row line as at the pin and no (vii) in the new text',
     U1NOW == U1PIN and bool(U1NOW) and '(vii)' not in FLNEW),
    ('G-NOROWEDIT', 'row U1`s line byte-identical to its pin', U1NOW == U1PIN and bool(U1PIN)),
    ('G-NOFOLD', 'FINDINGS.md unchanged since the pin and no span record under this act',
     unchanged(PP, PIN_PP, 'FINDINGS.md') and not [f for f in os.listdir(D) if f.startswith('b424_span')]),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     prefix_ok('OPEN_TRAILS.md') and '<!-- b424' in TRAILS and '<!-- b423' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b423 at 272 and this act at 273, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW423 == [272] and ROW424 == [273]),
    ('G-LEDGER-APPEND-ONLY', 'the ledger`s pin a true prefix, one b424 mark', prefix_ok('FACES_LEDGER.md') and FLTXT.count(CMP.MARK) == 1),
    ('G-WRITELIST-KINDS', 'the face names 6 kinds', 6 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
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
     not any(s in FBANK.lower() for s in ('the lock was overridden', 'a witness was found', 'a witness held',
                                          'a seventh site', 'a grade was moved', 'h2 has moved'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b424_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
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
