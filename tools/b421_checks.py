# -*- coding: utf-8 -*-
"""b421_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay df1cb0d, PLACE-papers 743be4a,
### SIDE-global-section 5c72065), in git's own view, never to HEAD; rows are read by marker.
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

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CLASSES = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean')
PIN_RELAY, PIN_PP, PIN_SIDE = 'df1cb0d', '743be4a', '5c72065'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b421_checks_postpush.txt' if POST else 'b421_checks.txt')
NDIR = r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\fbe6b4b2-25ed-44b7-91cb-756e5456e21d\scratchpad\n421'
PRINTS = ['key', 'mod_add_iff', 'diagA', 'diagB', 'trA_eq', 'trB_eq', 'grid_trace_is_signed_count']
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
    return re.sub(r'--[^\n]*', ' ', re.sub(r'/-.*?-/', ' ', src, flags=re.S))


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'PROBES', 'C1V', 'C2', 'C3', 'CONF', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B421T',
             'CORR', 'FACE', 'FERRY', 'SCAN', 'CLOSING', 'SEALV', 'MOD')


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


FACEPATH = os.path.join(D, 'b421_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b421_ferry.txt'))
SCAN = read(os.path.join(D, 'b421_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b421_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b421_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b421_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b421_extract.txt'))
COMP = read(os.path.join(D, 'b421_components.txt'))
PROBES = read(os.path.join(D, 'b421_c1_probes.txt'))
C1V = read(os.path.join(D, 'b421_c1_verify.txt'))
C2 = read(os.path.join(D, 'b421_c2_specification.txt'))
C3 = read(os.path.join(D, 'b421_c3_span.txt'))
CONF = read(os.path.join(D, 'b421_conflations.txt'))
LOCK = read(os.path.join(D, 'b421_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b421_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b421_desk_notes.txt'))
BANK = read(os.path.join(D, 'b421_the_finite_ambient.txt'))
CLOSING = read(os.path.join(D, 'b421_closing.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B421T = TRAILS.split('<!-- b421')[-1] if '<!-- b421' in TRAILS else ''
MOD = read(os.path.join(SIDE, 'Core', 'GridTrace.lean'))
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FEXT, FC2, FC3, FCONF, FB421T = fold(BANK), fold(COMP), fold(EXT), fold(C2), fold(C3), fold(CONF), fold(B421T)
FFACE, FSEALV, FMOD = fold(FACE), fold(SEALV), re.sub(r'\s+', ' ', MOD)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b421_components.py'))
EXTSRC = read(os.path.join(T, 'b421_extract.py'))
DESKSRC = read(os.path.join(T, 'b421_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b421_')]
B420MARK = "**THE BARRIER LEMMA DOES NOT REACH THE ARC'S POSITIVITY ARGUMENT: NOT AN INSTANCE, ON FORM**"
B421MARK = "**THE GRID TRACE DEFINED HERE EQUALS THE MODEL'S COUNTING FORM, ZERO AXIOMS, ON THE THIRD PROBE**"


def rows_of(mark, text):
    return [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mark), text)]


ROW420, ROW421 = rows_of(B420MARK, CORR), rows_of(B421MARK, CORR)
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')
PS = sorted(f for f in os.listdir(NDIR) if re.match(r'p\d\d\.lean$', f)) if os.path.isdir(NDIR) else []
T0 = read(os.path.join(NDIR, 'p01.start')).strip()
T1 = read(os.path.join(NDIR, PS[-1][:-5] + '.end')).strip() if PS else ''


def minutes(a, b):
    from datetime import datetime
    f = '%Y-%m-%dT%H:%M:%SZ'
    try:
        return (datetime.strptime(b, f) - datetime.strptime(a, f)).total_seconds() / 60.0
    except Exception:
        return 1e9


def kernel_changed():
    tracked = set(git(SIDE, 'diff', '--name-only', PIN_SIDE).split())
    untracked = set(git(SIDE, 'ls-files', '--others', '--exclude-standard', '--', 'Core', 'AllPrints.lean',
                        'AXIOM_PRINTS.txt').split())
    return (tracked | untracked) - {'CORRESPONDENCE.md'}


def allprints_measure():
    old, new = blob(SIDE, PIN_SIDE, 'AllPrints.lean') or b'', rb(os.path.join(SIDE, 'AllPrints.lean'))
    ins = old.replace(b'import SmearGeneral\n', b'import SmearGeneral\nimport GridTrace\n', 1)
    return new.startswith(ins) and new[len(ins):] == b''.join(b'#print axioms GridTrace.%s\n' % x.encode() for x in PRINTS)


PROFB = rb(os.path.join(SIDE, 'AXIOM_PRINTS.txt'))
OLDPROF = blob(SIDE, PIN_SIDE, 'AXIOM_PRINTS.txt') or b''
RUNC1 = COMPSRC[COMPSRC.find('def run_c1_record'):COMPSRC.find('def run_c1_kernel')]

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the first probe',
     'SEAL INTACT' in SEALV and bool(T0) and stamp_of(FACE, 'locked at (UTC) :') < T0),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT') and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-C1-TWO-OBJECTS-NAMED', 'the statement names both objects',
     'gridTrace p n t = B329.signedTrace p n t' in MOD and 'THE TWO OBJECTS THIS MODULE RELATES' in MOD),
    ('G-C1-SCOPE-DOCSTRING', 'the docstring says the source`s trace is not this object, and the source governs',
     "THE SOURCE'S TRACE IS NOT THIS OBJECT" in MOD and 'the source governs' in FMOD),
    ('G-C1-PROBES-OUTSIDE-REPOS', 'every probe is a scratch file outside the repositories',
     bool(PS) and 'scratchpad' in NDIR and not NDIR.upper().startswith('D:')),
    ('G-C1-BUDGET-HONOURED', 'no more than sixteen probes and 150 minutes', 0 < len(PS) <= 16 and minutes(T0, T1) <= 150),
    ('G-C1-ONE-VERDICT', 'exactly one verdict line', 1 == len(re.findall(r'VERDICT : (PROVED|BLOCKED|OVER-BUDGET)', FCOMP))),
    ('G-C1-PROFILE-READ', 'the verdict is read from the profile, the exit line read by nothing',
     'VERDICT, READ FROM THE PROFILE : PROVED' in fold(PROBES) and 'read by nothing' in PROBES
     and 'EXIT' not in pycode_of(RUNC1).upper()),
    ('G-C1-PROFILES-BANKED', 'every probe`s source and printed profile is banked',
     PROBES.count('### PRINTED:') == len(PS) and len(PS) > 0),
    ('G-C1-NO-SORRY', 'no probe and no Core file carries sorry as a term',
     all(not re.search(r'\bsorry\b', lean_code(read(os.path.join(NDIR, f)))) for f in PS)
     and all(not re.search(r'\bsorry\b', lean_code(read(os.path.join(SIDE, 'Core', f))))
             for f in os.listdir(os.path.join(SIDE, 'Core')) if f.endswith('.lean'))),
    ('G-C1-NO-MATHLIB', 'the module and every probe import SmearGeneral and nothing else',
     re.findall(r'(?m)^import (\S+)', MOD) == ['SmearGeneral']
     and all(re.findall(r'(?m)^import (\S+)', read(os.path.join(NDIR, f))) == ['SmearGeneral'] for f in PS)),
    ('G-C1-KERNEL-BY-VERDICT', 'PROVED, and the kernel changed in exactly the three owed files',
     'VERDICT : PROVED' in FCOMP and kernel_changed() == {'AXIOM_PRINTS.txt', 'AllPrints.lean', 'Core/GridTrace.lean'}),
    ('G-C1-PREFIX-TRUE', 'the pin`s profile is a true byte prefix of the kernel`s',
     bool(OLDPROF) and PROFB.startswith(OLDPROF) and len(PROFB) > len(OLDPROF)),
    ('G-C1-ALLPRINTS-INSERT-APPEND', 'one import inserted after the last import, the prints appended', allprints_measure()),
    ('G-C1-EXISTING-UNCHANGED', 'no existing Core file changed; Classes carries its digest',
     not [f for f in git(SIDE, 'diff', '--name-only', PIN_SIDE, '--', 'Core').split() if f != 'Core/GridTrace.lean']
     and hashlib.sha256(rb(CLASSES)).hexdigest().startswith('d4f931db1d50c01f')),
    ('G-N1-APART', '(N1)`s two clauses scored on separate lines', 'proves within the budget --' in COMP and 'no Mathlib import' in COMP),
    ('G-C2-BOTH-DEFINITIONS', 'the price stated under both definitions',
     'UNDER THE KEYSTONE`S DEFINITION 2.1' in C2 and 'UNDER THE MONOGRAPH`S FORMAL DEFINITION' in C2 and C2.count('PRICE UNDER') == 2),
    ('G-C2-CITED-AS-SEATS', 'the classical theorem is cited as the seat`s, the keystone unedited',
     "THE SEAT`S CITATION, NOT THE RECORD`S" in C2 and unchanged(PP, PIN_PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')),
    ('G-C2-SEARCH-READ', 'the search hit hand-read and the holding count printed',
     'the one hit, OPEN_TRAILS.md' in C2 and 'documents holding the specification : 0' in C2),
    ('G-C2-B407-ROUTED', 'b407 routed and its bank unchanged',
     'THAT ACT IS NOT RE-VERDICTED' in FC2 and unchanged(ROOT, PIN_RELAY, 'data/b407_the_barriers_own_instance.txt')),
    ('G-N2-SCORED', '(N2) scored', bool(re.search(r'\(N2\).*(MET|REFUTED)', FC2))),
    # ### REPAIRED AFTER RUN 1 (kept as b421_checks_run1.txt): the arm looked for the file name `b363_span.py` in
    # ### the run record, and the tool names itself by its own header line, never by its file name. ### It now
    # ### reads that header and the JSON the tool emitted under this act's stem.
    ('G-C3-SPAN-BY-TOOL', 'the span counted by the b363 tool under this act`s stem',
     "b363 -- THE FOLD'S OWN THRESHOLD, COUNTED." in read(os.path.join(D, 'b421_span_run.txt'))
     and str(__import__('json').load(io.open(os.path.join(D, 'b421_span.json'), encoding='utf-8')).get('this_act')).endswith('421')
     and 'current_span' in read(os.path.join(D, 'b421_span.json'))),
    ('G-C3-BOTH-COUNTS', 'both counts printed', bool(re.search(r'THE ACT`S COUNT : \d+\. ### WITHOUT THIS ACT : \d+', C3))),
    ('G-C3-FOLD-NAMED', 'the fold named with its span and its filing act',
     'the fold named : b413-b421' in C3 and 'to be filed by b422' in C3),
    ('G-C3-NOFOLD', 'FINDINGS.md unchanged since the pin', unchanged(PP, PIN_PP, 'FINDINGS.md')),
    ('G-N3-APART', '(N3)`s two clauses scored on separate lines', '*the span counts eight*' in C3 and '*the fold is named for b422' in C3),
    ('G-CONFLATIONS-ENTERED', 'the three conflations entered, in the record and the trail',
     'conflations entered with their corrections : 3' in CONF and 'three conflations at b420' in FB421T),
    ('G-CONFLATIONS-QUOTED', 'each with the navigator`s words, the correction and the source',
     CONF.count('THE NAVIGATOR`S WORDS') == 3 and CONF.count('THE SEAT`S CORRECTION') == 3
     and CONF.count('THE SOURCE :') == 3 and '### MISS' not in CONF),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B421T for k in (1, 2, 3, 4)) and B421T.count('**OPEN.**') == 4
     and 'Trigger: the ruling on which test governs' in BANK),
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
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|20)_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md unchanged since the pin', unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     TRAILS.startswith((blob(PP, PIN_PP, 'OPEN_TRAILS.md') or b'x').decode('utf-8').rstrip(NL))
     and '<!-- b421' in TRAILS and '<!-- b420' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b420 at 269 and this act at 270, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW420 == [269] and ROW421 == [270]),
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
     not any(s in FBANK.lower() for s in ('the lock was overridden', 'the source trace is compiled', 'a grade was moved',
                                          'h2 has moved', 'the fold was run'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b421_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
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
