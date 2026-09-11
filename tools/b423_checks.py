# -*- coding: utf-8 -*-
"""b423_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay de33805, PLACE-papers 53e9cd3,
### SIDE-global-section c803412), in git's own view; rows are read by marker; every deciding sentence is re-found
### at its source by the components' own function, IMPORTED.
"""
import ast
import io
import os
import re
import subprocess
import sys
import tokenize

ROOT =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b423_components as CMP   # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_RELAY, PIN_PP, PIN_SIDE = 'de33805', '53e9cd3', 'c803412'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b423_checks_postpush.txt' if POST else 'b423_checks.txt')
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


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'QREC', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B423T', 'CORR', 'FACE', 'FERRY',
             'SCAN', 'CLOSING', 'SEALV')


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


FACEPATH = os.path.join(D, 'b423_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b423_ferry.txt'))
SCAN = read(os.path.join(D, 'b423_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b423_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b423_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b423_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b423_extract.txt'))
COMP = read(os.path.join(D, 'b423_components.txt'))
QREC = read(CMP.QREC)
LOCK = read(os.path.join(D, 'b423_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b423_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b423_desk_notes.txt'))
BANK = read(os.path.join(D, 'b423_the_r37_question_read.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B423T = TRAILS.split('<!-- b423')[-1] if '<!-- b423' in TRAILS else ''
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FQREC, FFACE, FSEALV = fold(BANK), fold(COMP), fold(QREC), fold(FACE), fold(SEALV)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b423_components.py'))
EXTSRC = read(os.path.join(T, 'b423_extract.py'))
DESKSRC = read(os.path.join(T, 'b423_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b423_')]
B422MARK = "**THE KERNEL ARC FOLDED: TWO COMPILED GENERAL THEOREMS ABOUT THE MODEL, AND THE KEYSTONE'S DEFINITION 2.1"
B423MARK = "**THE (R37) QUESTION READ: b407'S AND b420'S READINGS OF THE LEMMA'S FIRST HYPOTHESIS, EACH AGAINST §10.2**"


def rows_of(mark, text):
    return [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mark), text)]


ROW422, ROW423 = rows_of(B422MARK, CORR), rows_of(B423MARK, CORR)
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')
DEC = CMP.deciding()


def verdict_of(who):
    return verdict_line(QREC, 'VERDICT ON %s`S READING :' % who).rsplit(':', 1)[-1].strip()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the component`s write',
     'SEAL INTACT' in SEALV and bool(stamp_of(QREC)) and stamp_of(FACE, 'locked at (UTC) :') < stamp_of(QREC)),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the seal verifies and the registration gate reads CLEAR',
     'SEAL INTACT' in SEALV and 'CLEAR' in verdict_line(GATE, 'GATE VERDICT')
     and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-SORTIE-OPENED', 'the ferry opens the arc and orders the sortie; the face names this leg 1',
     "THE AUTHOR'S WORD OPENS W-ORD-WITNESS-ENUMERATION." in FERRY and 'LEG 1 (b423)' in FERRY
     and 'THIS IS LEG 1, b423' in FFACE),
    ('G-Q-B407-READ', 'b407`s reading quoted and scored CONFIRMED or MOVED',
     "`xi` is determined" in QREC and verdict_of('b407') in ('CONFIRMED', 'MOVED')),
    ('G-Q-B420-READ', 'b420`s reading quoted and scored CONFIRMED or MOVED',
     'NOT SUPPLIED BY THE RECORD' in CMP.unwrapped(QREC) and verdict_of('b420') in ('CONFIRMED', 'MOVED')),
    ('G-Q-DECIDING-QUOTED', 'every deciding sentence re-found at its source and in the record',
     len(DEC) == 5 and all(s != '### MISS' and CMP.norm(s) in CMP.norm(read(p)) and CMP.norm(s) in CMP.unwrapped(QREC)
                           for _w, p, s in DEC)),
    ('G-Q-VERDICTS-REST-NAMED', 'both verdicts named as resting on hypothesis 5', QREC.count('REST ON : HYPOTHESIS 5') == 2),
    ('G-Q-NO-REVERDICT', '0 re-verdicts; b407`s, b420`s and b421`s records unchanged since the pin',
     're-verdicts : 0.' in QREC and all(unchanged(ROOT, PIN_RELAY, 'data/%s' % f) for f in (
         'b407_the_barriers_own_instance.txt', 'b420_the_lemma_aimed.txt', 'b420_c4_barrier.txt', 'b421_c2_specification.txt'))),
    ('G-Q-CONSEQUENCE-ROUTED', 'the seat`s reading of §10.2 printed as such and routed',
     'THE SEAT`S READING OF §10.2, ROUTED TO THE AUTHOR AND NOT RULED' in QREC and 'Routed to the author, not ruled' in B423T),
    ('G-NOKEYSTONE-EDIT', 'the keystone and the monograph unchanged since the pin',
     unchanged(PP, PIN_PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')
     and unchanged(PP, PIN_PP, 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
    ('G-L1-APART', '(L1)`s two clauses scored apart', COMP.count('(L1) *') == 2),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B423T for k in (1, 2, 3, 4)) and B423T.count('**OPEN.**') == 4
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
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|2[0-2])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md unchanged since the pin', unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-NOFOLD', 'FINDINGS.md unchanged since the pin and no span record under this act',
     unchanged(PP, PIN_PP, 'FINDINGS.md') and not [f for f in os.listdir(D) if f.startswith('b423_span')]),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     prefix_ok('OPEN_TRAILS.md') and '<!-- b423' in TRAILS and '<!-- b422' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b422 at 271 and this act at 272, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW422 == [271] and ROW423 == [272]),
    ('G-WRITELIST-KINDS', 'the face names 5 kinds', 5 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
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
                                          'h2 has moved', 'b407 is re-verdicted', 'b420 is re-verdicted'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b423_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
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
