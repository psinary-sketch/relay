# -*- coding: utf-8 -*-
"""b420_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay 897ca3c, PLACE-papers 9d45b45,
### SIDE-global-section 9ea4d92), in git's own view, never to HEAD; rows are read by marker.
"""
import ast
import hashlib
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
import b420_components as CMP   # noqa: E402  ### the annotation texts, IMPORTED so the arm and the writer agree

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CLASSES = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean')
PIN_RELAY, PIN_PP, PIN_SIDE = '897ca3c', '9d45b45', '9ea4d92'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b420_checks_postpush.txt' if POST else 'b420_checks.txt')
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
    """### GIT'S OWN VIEW: no content difference between the pin and the working file."""
    return subprocess.run(['git', '-C', repo, 'diff', '--quiet', pin, '--', rel]).returncode == 0


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


def lean_code(src):
    src = re.sub(r'/-.*?-/', ' ', src, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', src)


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'C1K', 'C1V', 'C1R', 'C2', 'C3', 'C4', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B420T',
             'CORR', 'FACE', 'FERRY', 'SCAN', 'CLOSING', 'SEALV', 'BUILD')


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


FACEPATH = os.path.join(D, 'b420_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b420_ferry.txt'))
SCAN = read(os.path.join(D, 'b420_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b420_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b420_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b420_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b420_extract.txt'))
COMP = read(os.path.join(D, 'b420_components.txt'))
C1K = read(os.path.join(D, 'b420_c1_kernel.txt'))
C1V = read(os.path.join(D, 'b420_c1_verify.txt'))
C1R = read(os.path.join(D, 'b420_c1_record.txt'))
C2 = read(os.path.join(D, 'b420_c2_priced.txt'))
C3 = read(os.path.join(D, 'b420_c3_clauses.txt'))
C4 = read(os.path.join(D, 'b420_c4_barrier.txt'))
BUILD = read(os.path.join(D, 'b420_kernel_build.txt'))
LOCK = read(os.path.join(D, 'b420_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b420_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b420_desk_notes.txt'))
BANK = read(os.path.join(D, 'b420_the_lemma_aimed.txt'))
CLOSING = read(os.path.join(D, 'b420_closing.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B420T = TRAILS.split('<!-- b420')[-1] if '<!-- b420' in TRAILS else ''
SPFP = os.path.join(SIDE, 'Core', 'SinglePrimeFactor.lean')
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FEXT, FC4, FC2, FB420T = fold(BANK), fold(COMP), fold(EXT), fold(C4), fold(C2), fold(B420T)
FFACE, FSEALV = fold(FACE), fold(SEALV)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b420_components.py'))
EXTSRC = read(os.path.join(T, 'b420_extract.py'))
DESKSRC = read(os.path.join(T, 'b420_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b420_')]
B414MARK = "**THE KERNEL'S OWN HEADER NAMED THE MISSING IDENTIFICATION IN ADVANCE"
B419MARK = "**THE GENERAL CLAUSE IS PROVED, ZERO AXIOMS, ON THE FIRST PROBE**"
B420MARK = "**THE BARRIER LEMMA DOES NOT REACH THE ARC'S POSITIVITY ARGUMENT: NOT AN INSTANCE, ON FORM**"


def rows_of(mark, text):
    return [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mark), text)]


def row_line(mark, text):
    i = text.find('| ' + mark)
    j = text.rfind(NL, 0, i) + 1
    return text[j:text.find(NL, i)] if i >= 0 else None


ROW419, ROW420 = rows_of(B419MARK, CORR), rows_of(B420MARK, CORR)
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')
SPF_NOW = read(SPFP)
SPF_PIN = (blob(SIDE, PIN_SIDE, 'Core/SinglePrimeFactor.lean') or b'').decode('utf-8')
N420 = r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\fbe6b4b2-25ed-44b7-91cb-756e5456e21d\scratchpad\n420'

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
     'SEAL INTACT' in SEALV and bool(stamp_of(C1K)) and stamp_of(FACE, 'locked at (UTC) :') < stamp_of(C1K)),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT') and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-R36-RATIFIED', 'the ferry carries (R36) and the face ratifies it without extending it',
     'RULING (R36)' in FERRY and 'ROUTE (1) -- IS RATIFIED BY THE PASTE' in FFACE and 'does not extend it' in FFACE),
    ('G-R36-ITEM-TRIGGERED', 'the trail records the instrument item with a trigger that can fire',
     'INSTRUMENT ITEM (R36), NOT OPENED' in FB420T and 'Trigger: the author opens an instrument lane' in FB420T),
    ('G-NOLOCKGATE-EDIT', 'the lock gate unchanged since the pin, in git`s view', unchanged(ROOT, PIN_RELAY, 'tools/b378_lockgate.py')),
    ('G-NOSCAN-EDIT', 'the scan unchanged since the pin, in git`s view', unchanged(ROOT, PIN_RELAY, 'tools/ferry_scan.py')),
    ('G-C1-SPF-ANNOTATED', 'both annotations are in SinglePrimeFactor.lean', CMP.ANN1 in SPF_NOW and CMP.ANN2 in SPF_NOW),
    ('G-C1-SPF-WORDS-SURVIVE', 'removing the annotations returns the pin`s bytes',
     bool(SPF_PIN) and SPF_NOW.replace(CMP.ANN1, '', 1).replace(CMP.ANN2, '', 1) == SPF_PIN),
    ('G-C1-ROW263-UNEDITED', 'row 263`s line is byte-identical to its line at the pin',
     row_line(B414MARK, CORR) is not None and row_line(B414MARK, CORR) == row_line(B414MARK, OLDCORR)
     and rows_of(B414MARK, CORR) == [263]),
    ('G-C1-ROW263-NAMED', 'this act`s row names row 263 and its marker',
     bool(ROW420) and 'ROW 263' in (row_line(B420MARK, CORR) or '') and "THE KERNEL'S OWN HEADER NAMED THE MISSING" in (row_line(B420MARK, CORR) or '')),
    ('G-C1-EIGHT-LISTED', 'the eight sentences listed beside their terminal',
     'QUALIFIED sentences listed beside their terminal : 8' in C1R and C1R.count('now compiled  | QUALIFIED BY') == 8),
    ('G-C1-PROFILE-IDENTICAL', 'the profile equals its blob at the pin, byte for byte',
     rb(os.path.join(SIDE, 'AXIOM_PRINTS.txt')) == blob(SIDE, PIN_SIDE, 'AXIOM_PRINTS.txt')),
    ('G-C1-NO-TERMINAL-MOVED', 'AllPrints, the seal, the module and Classes unchanged',
     all(unchanged(SIDE, PIN_SIDE, f) for f in ('AllPrints.lean', 'Core/FiniteSideSeal.lean', 'Core/SmearGeneral.lean'))
     and hashlib.sha256(rb(CLASSES)).hexdigest().startswith('d4f931db1d50c01f')),
    ('G-C2-PARTS-SPLIT', 'the step is priced in its two parts', 'PART (i) -- ON THE FINITE AMBIENT' in C2 and 'PART (ii) -- THE SOURCE' in C2),
    ('G-C2-EACH-PRICED', 'each part carries exactly one price', C2.count('**PRICE :') == 2),
    ('G-C2-NOBUILD', 'no probe directory and no build beyond Component 1`s rebuild',
     not os.path.isdir(N420) and set(re.findall(r'=== (\w+) start', BUILD)) == {'SinglePrimeFactor', 'SmearGeneral', 'AllPrints'}),
    ('G-N1-APART', '(N1)`s clauses scored on separate lines', 'MET' in FC2 and 'REFUTED AT PART (ii)' in FC2),
    ('G-C3-CLAUSES-READ', 'the eight clauses re-read', 'clauses re-read : 8' in C3 and C3.count('b419 face line') == 8),
    ('G-C3-EACH-GRADED', 'each clause graded MEETABLE or NOT MEETABLE',
     len(re.findall(r'### \*\*(NOT )?MEETABLE AS WRITTEN', C3)) == 8),
    ('G-C3-OWN-FACE-CORRECT', 'this face asks the profile, not the driver, for sameness',
     'AllPrints.lean is NOT a kind of this act' in FFACE and 'BYTE-IDENTICAL TO ITS BLOB AT THE PIN' in FFACE),
    ('G-C4-INSTANCE-QUOTED', 'the instance quoted from the keystone and row S1',
     all(k in C4 for k in ('**Definition 2.1 (Determined system).**', '**Definition 2.3 (Target parameter).**',
                           'S1 -- the clause stated:')) and '### MISS' not in C4),
    ('G-C4-FIVE-HYPOTHESES', 'the five hypotheses read one by one',
     all(('HYPOTHESIS %d --' % k) in C4 for k in range(1, 6))),
    ('G-C4-FERRY-VS-SOURCE', 'the ferry`s descriptions printed beside their sources',
     'the ferry`s description of b419`s clause' in C4 and 'b419`s clause in its own words' in C4
     and '(the ferry`s paraphrase of it)' in C4),
    ('G-C4-ONE-VERDICT', 'exactly one verdict line',
     1 == len(re.findall(r'\*\*(INSTANCE|NOT AN INSTANCE|UNDECIDABLE) -- THE', C4))
     and 1 == len(re.findall(r'VERDICT : (INSTANCE|NOT AN INSTANCE|UNDECIDABLE)', FCOMP))),
    ('G-C4-LEDGER-BY-VERDICT', 'not INSTANCE, so FACES_LEDGER.md is unchanged since the pin',
     'VERDICT : NOT AN INSTANCE' in FCOMP and unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-C4-SIDE-BY-SIDE', 'the two sentences printed side by side, and the question answered',
     'THE LEMMA`S PREDICTED REACH' in C4 and 'WHAT THE AIM MAP MEASURED' in C4 and 'DO THEY DESCRIBE ONE FACT?' in C4),
    ('G-N2-APART', '(N2)`s premise clauses and conclusion on separate lines', C4.count('(N2) premise') == 2 and '(N2) conclusion' in C4),
    ('G-N3-SCORED', '(N3) scored', bool(re.search(r'\(N3\).*(MET|REFUTED)', C4))),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B420T for k in (1, 2, 3, 4)) and B420T.count('**OPEN.**') == 4
     and 'Trigger: the ruling on which test governs' in BANK),
    ('G-NOGRADE', 'no grade string minted', not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged', '0 premises discharged' in FBANK),
    ('G-NODOOR', 'the bank states 0 doors restated', '0 doors restated' in FBANK),
    ('G-NOROUTE', 'the bank states 0 routes proposed', '0 routes proposed' in FBANK),
    ('G-NOKAPPA', 'no kappa value measured', not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NOFOLD', 'FINDINGS.md is not written', 'FINDINGS' not in ACT_WORK),
    ('G-NORULE', 'STRUCK_CLAUSES is not written', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no Zenodo byte', 'zenodo' not in ACT_WORK.lower()),
    ('G-NOPLATFORM', 'no platform call', not re.search('urllib|requests|http', ACT_WORK)),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 3),
    ('G-NOLOCKEDFACE', 'the seal still verifies', 'SEAL INTACT -- the body is byte-for-byte what was sealed' in FSEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     TRAILS.startswith((blob(PP, PIN_PP, 'OPEN_TRAILS.md') or b'x').decode('utf-8').rstrip(NL))
     and '<!-- b420' in TRAILS and '<!-- b419' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b419 at 268 and this act at 269, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW419 == [268] and ROW420 == [269]),
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
     not any(s in FBANK.lower() for s in ('the lock was overridden', 'the lock gate was changed', 'a grade was moved',
                                          'h2 has moved', 'the lemma applies to the arc'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b420_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
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
