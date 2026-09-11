# -*- coding: utf-8 -*-
"""b418_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Corpus files are compared to their blobs at the pin the act started from (PLACE-papers 09a1e80,
### relay 1dc9f72), never to HEAD; correspondence rows are read by marker.
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
import walker_guard as WG   # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_PP, PIN_RELAY = '09a1e80', '1dc9f72'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b418_checks_postpush.txt' if POST else 'b418_checks.txt')
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


def stamp_of(text, key='run at (UTC) :'):
    m = re.search(re.escape(key) + r' (\S+)', text or '')
    return m.group(1) if m else ''


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'WALK', 'R35', 'REP', 'NATT', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'CORR',
             'FACE', 'FERRY', 'FERRY2', 'SCAN', 'CLOSING', 'RETIRED')


def _raw_no_arms():
    src = read(os.path.abspath(__file__))
    bad = []
    tree = ast.parse(src)
    for node in ast.walk(tree):
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


FACE = read(os.path.join(D, 'b418_registration_2026-09-11.txt'))
FERRY = read(os.path.join(D, 'b418_ferry.txt'))
FERRY2 = read(os.path.join(D, 'b418_ferry2.txt'))
SCAN = read(os.path.join(D, 'b418_ferry_scan.txt'))
SCAN1 = read(os.path.join(D, 'b418_ferry_scan_run1.txt'))
CEN = read(os.path.join(D, 'b418_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b418_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b418_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b418_extract.txt'))
EXT1 = read(os.path.join(D, 'b418_extract_run1.txt'))
EXT2 = read(os.path.join(D, 'b418_extract_run2.txt'))
COMP = read(os.path.join(D, 'b418_components.txt'))
WALK = read(os.path.join(D, 'b418_walker.txt'))
R35 = read(os.path.join(D, 'b418_r35.txt'))
REP = read(os.path.join(D, 'b418_repairs.txt'))
NATT = read(os.path.join(D, 'b418_n_attempt.txt'))
LOCK = read(os.path.join(D, 'b418_lockgate_notes2.txt'))
LOCK1 = read(os.path.join(D, 'b418_lockgate_notes.txt'))
SEALV = read(os.path.join(D, 'b418_reg_seal_verify.txt'))
GATE = read(os.path.join(D, 'b418_reg_gate.txt'))
HALT = read(os.path.join(D, 'b418_halt.txt'))
DESKN = read(os.path.join(D, 'b418_desk_notes.txt'))
BANK = read(os.path.join(D, 'b418_the_ruling_carried.txt'))
CLOSING = read(os.path.join(D, 'b418_closing.txt'))
P235 = read(os.path.join(D, 'b418_p235_before.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
MATTER = read(os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md'))
ATREST_B = rb(os.path.join(PP, 'phase1.5', 'structural', 'AT_REST.md'))
CONST = read(os.path.join(PP, 'phase1.5', 'deep-structure', 'CONSTANCE.md'))
REGISTRY = read(os.path.join(PP, 'REGISTRY.md'))
RETIRED = read(os.path.join(T, 'retired', 'RETIRED.md'))
GUARDSRC = read(os.path.join(T, 'walker_guard.py'))
KD = read(os.path.join(D, 'b418_kernel_digests_before.txt')).split()
KDIG = dict(zip(KD[1::2], KD[0::2]))

FBANK, FCOMP, FEXT, FDESK, FWALK = fold(BANK), fold(COMP), fold(EXT), fold(DESKN), fold(WALK)
FFACE = fold(FACE)


def lean_code(src):
    """### A LEAN SOURCE WITH ITS BLOCK COMMENTS (`/- ... -/`, docstrings included) AND LINE COMMENTS
    ### REMOVED, so a search finds terms and never the prose that talks about them."""
    src = re.sub(r'/-.*?-/', ' ', src, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', src)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b418_components.py'))
EXTSRC = read(os.path.join(T, 'b418_extract.py'))
DESKSRC = read(os.path.join(T, 'b418_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC + GUARDSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b418_')]
B417MARK = '**READING (a) WOULD LEAVE TWO DISTINCT TUPLES WHERE THE MODEL NAMES FOUR CLASSES'
B418MARK = "**THE GENERAL CLAUSE IS OVER-BUDGET WITH ONE HELPER UNSUPPLIED, AND THE WALKER'S MISS WAS A SILENT"
ROW417 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B417MARK), CORR)]
ROW418 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B418MARK), CORR)]
OLDMATTER = (blob(PP, PIN_PP, 'phase2/physics/MATTER_AS_ARITHMETIC.md') or b'').decode('utf-8')
OLDAT = blob(PP, PIN_PP, 'phase1.5/structural/AT_REST.md') or b''
OLDCONST = (blob(PP, PIN_PP, 'phase1.5/deep-structure/CONSTANCE.md') or b'').decode('utf-8')
OLDREG = (blob(PP, PIN_PP, 'REGISTRY.md') or b'').decode('utf-8')
CLINE = '> *Correction, b418: 43 = 2⁴ + 3³ is a sum of a power of two and a power of three'
NDIR = r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\fbe6b4b2-25ed-44b7-91cb-756e5456e21d\scratchpad\n418'
PROBES = sorted(f for f in os.listdir(NDIR) if re.match(r'p\d\d\.lean$', f)) if os.path.isdir(NDIR) else []
FIRSTPROBE = (read(os.path.join(NDIR, 'p01.out')).split('start ')[-1].split()[:1] or [''])[0] if PROBES else ''


def kernel_same(path_key, path):
    return bool(KDIG.get(path_key)) and hashlib.sha256(rb(path)).hexdigest() == KDIG.get(path_key)


def sentences_joined(text):
    SLOT = re.compile(r'\bn[1-4]\b|n[₁₂₃₄]|\btuples?\b|\bOmega\b|Ω|universality sentence|\bratios?\b')
    FIF = re.compile(r'\bP\b|Prime[ -]Core|\bdeserts?\b|the fifteen|\bReader\b')
    return [s.strip()[:120] for s in re.split(r'(?<=[.!?])\s+|\n', text or '') if SLOT.search(s) and FIF.search(s)]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the first ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-RESUME-BANKED', 'the resume order is banked verbatim', 'RESUME b418. Connection dropped' in FERRY2),
    ('G-DROP-DECLARED', 'the face declares the drop', 'THE DROP, DECLARED ON THE FACE' in FACE),
    ('G-HALT-DECLARED', 'the halt record exists and the face declares the refusal',
     'HALTED AT THE LOCK' in HALT and 'THE LOCK REFUSED ONCE' in FACE and 'LOCK REFUSED' in LOCK1),
    ('G-REPASTE-BANKED', 'the re-paste is banked verbatim in the gated ferry',
     'RE-PASTE b418. The survey stands' in FERRY2 and 'cannot reach part of a directory' in FERRY2),
    ('G-FIRST-FERRY-KEPT', 'the first ferry file is kept unedited', 'STEP ZERO ON RESUME, AS REPORTED' in FERRY
     and 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the gated ferry`s scan reports 0 hits',
     '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:') and 'b418_ferry2.txt' in SCAN),
    ('G-SCAN-RUN1-KEPT', 'the first scan is kept with its one hit', '1 HIT(S) REPORTED' in verdict_line(SCAN1, 'VERDICT:')),
    ('G-LIMIT-GUARD-ONE-LINE', 'the guard`s verdict turns on one line returning INCOMPLETE',
     1 == len([ln for ln in GUARDSRC.splitlines() if 'return INCOMPLETE' in ln and '>= limit - margin' in ln])),
    ('G-LIMIT-GUARD-FIXTURES', 'the guard`s fixtures pass, both polarities', WG.self_test(verbose=False)),
    ('G-NO-WRAPPER-FOUND-SAID', 'the face and the guard both say no wrapper existed',
     'FOUND NONE' in FFACE and 'Relay had none' in GUARDSRC),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-SURVEY-RUN1-KEPT', 'survey runs 1 and 2 are kept', bool(EXT1) and bool(EXT2)),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the first component run',
     'SEAL INTACT' in SEALV and bool(stamp_of(FACE, 'locked at (UTC) :'))
     and stamp_of(FACE, 'locked at (UTC) :') < stamp_of(WALK)),
    ('G-LOCKGATE-EIGHT', 'the permitting lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT') and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-RULING-RATIFIED-NOT-EXTENDED', 'the face executes (R35) without extending it',
     'it does not improve on it and does not extend it' in fold(FACE)),
    ('G-IGNORE-TESTED-FIRST', 'the ignore test is printed before the miss',
     0 < EXT.find('THE IGNORE HYPOTHESIS') < EXT.find('(b) THE MISS')),
    ('G-IGNORE-REFUTED-PRINTED', 'every missed file is printed NOT IGNORED', EXT.count('NOT IGNORED (exit 1)') == 27),
    ('G-MISS-FROM-METADATA', 'the miss is read from the transcript`s metadata',
     'DURATION 20.04 s ; numFiles 13' in FEXT),
    ('G-REPLAY-REACHES', 'the replay reaches 52 files', 'numFiles 52' in EXT),
    ('G-POPULATION-LISTED', 'the arc`s population is listed and the limit calls counted',
     os.path.exists(os.path.join(D, 'b418_walker_population.json'))
     and 'CALLS OVER THE DIRECTORY THAT REACHED THE LIMIT : 1' in FWALK),
    ('G-RERUN-EACH-CALL', 'the truncated call re-run bounded, complete, and matching Python',
     'bounded calls : 6 ; every one COMPLETE under the guard : True' in WALK
     and 'agree file for file : True' in WALK),
    ('G-BANKED-ABSENCES-HAND-READ', 'the records read and the count of absences resting on it printed',
     'ABSENT VERDICTS RESTING ON A TRUNCATED CALL : 0' in FWALK and "lines of b417`s records naming the walker" in WALK),
    ('G-BEYOND-ARC-REPORTED', 'the census beyond the arc is printed and bounded',
     'REACHED THE LIMIT AND SAID NOTHING' in FWALK and 'UPPER BOUND' in FCOMP),
    ('G-R35-NARROWED-BOTH', 'both occurrences carry the narrowing',
     2 == MATTER.count('with a connected reductive symmetry group *(narrowed in place b418 under (R35)')),
    ('G-R35-ORIGINAL-PRESERVED', 'the original words are quoted beside each',
     2 == MATTER.count('it read "universal across IDS-amenable systems"')),
    ('G-R35-ONE-STIPULATED-LINE', 'one STIPULATED line', 1 == MATTER.count('remains STIPULATED')),
    ('G-R35-MEASURED-AGAINST-BLOB', 'the diff against the pin is printed: 2 removed, 3 added',
     'lines removed 2, lines added 3' in R35),
    ('G-R35-NO-TUPLE-MOVED', 'the class table and Classes.lean are unchanged',
     all(x in MATTER for x in OLDMATTER.splitlines() if x.startswith('| ') and '— ' in x)
     and kernel_same('*/d/SIDE-formation-arithmetic/SIDEFormationArithmetic/Classes.lean',
                     os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean'))),
    ('G-ATREST-APPEND-ONLY', 'AT_REST`s pin bytes are a true prefix', bool(OLDAT) and ATREST_B.startswith(OLDAT)),
    ('G-CONSTANCE-ONE-LINE', 'CONSTANCE is its pin text plus exactly one line',
     CONST.replace(CONST[CONST.find(CLINE):CONST.find('\n', CONST.find(CLINE)) + 1], '', 1) == OLDCONST
     and CONST.count(CLINE) == 1),
    ('G-CONSTANCE-ORIGINAL-PRESERVED', 'the sentence stays byte-for-byte',
     'No combination of powers yields 43, 47, or 53 directly.' in CONST),
    ('G-P235-PRESERVED-FIRST', 'the row was preserved verbatim before the edit',
     'PRESERVED VERBATIM BEFORE ANY EDIT' in P235 and 'a three-clause currency note' in P235),
    ('G-P235-FIGURES-REMOVED', 'both stale figures are gone from the row, and no count restated',
     all(a not in [x for x in REGISTRY.splitlines() if x.startswith('| p2-35 |')][0]
         for a in ('three-clause', 'carries six'))),
    ('G-P235-ONLY-ROW-CHANGED', 'exactly one registry line differs from the pin',
     1 == sum(1 for x, y in zip(OLDREG.split('\n'), REGISTRY.split('\n')) if x != y)
     and len(OLDREG.split('\n')) == len(REGISTRY.split('\n'))),
    ('G-HYGIENE-RETIRED', 'the tool is in tools/retired/ and gone from tools/',
     os.path.exists(os.path.join(T, 'retired', 'b369_hygiene.py')) and not os.path.exists(os.path.join(T, 'b369_hygiene.py'))),
    ('G-RETIRED-REASON-FILED', 'RETIRED.md carries the reason, the verdict, the writes and the guard',
     all(k in RETIRED for k in ('The reason', 'FAILED', 'Its writes', 'repair_snapshot.py'))),
    ('G-RETIREMENT-DATES-NAMED', 'RETIRED.md names the tools its move dates',
     'Dated by this move' in RETIRED and RETIRED.count('- `tools/') >= 10),
    ('G-N-STRATEGY-BEFORE-LINE', 'the lock precedes the first probe',
     bool(FIRSTPROBE) and stamp_of(FACE, 'locked at (UTC) :') < FIRSTPROBE and 'THE STEPS, IN THE ORDER' in FACE),
    ('G-N-PROBES-OUTSIDE-REPOS', 'every probe is a scratch file outside the repositories',
     bool(PROBES) and 'scratchpad' in NDIR and not NDIR.upper().startswith('D:')),
    ('G-N-CAP-HONOURED', 'no more than sixteen probes', 0 < len(PROBES) <= 16),
    ('G-N-ONE-VERDICT', 'exactly one verdict line', 1 == len(re.findall(r'VERDICT : (PROVED|BLOCKED|OVER-BUDGET)', FCOMP))),
    ('G-N-PROFILES-BANKED', 'every probe`s source and printed profile is banked',
     NATT.count('### PRINTED:') == len(PROBES) and len(PROBES) > 0),
    # ### REPAIRED AFTER RUN 1: the first version searched Core/ for the raw word and fired on
    # ### SinglePrimeFactor.lean's own docstring saying the kernel carries none -- prose reporting an
    # ### absence. ### It now strips block and line comments and looks for the TERM.
    ('G-N-NO-SORRY', 'no probe carries a sorry, and Core carries none as a term',
     'occurrences of `sorry` across every probe : 0' in NATT
     and all(not re.search(r'\bsorry\b', lean_code(read(os.path.join(SIDE, 'Core', f))))
             for f in os.listdir(os.path.join(SIDE, 'Core')) if f.endswith('.lean'))),
    ('G-N-KERNEL-BY-VERDICT', 'the verdict is not PROVED, so the kernel files are unchanged',
     'VERDICT : PROVED' not in FCOMP
     and kernel_same('*/d/SIDE-global-section/Core/FiniteSideSeal.lean', os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean'))
     and kernel_same('*/d/SIDE-global-section/Core/SinglePrimeFactor.lean', os.path.join(SIDE, 'Core', 'SinglePrimeFactor.lean'))
     and kernel_same('*/d/SIDE-global-section/AXIOM_PRINTS.txt', os.path.join(SIDE, 'AXIOM_PRINTS.txt'))),
    ('G-EXAMPLES-PARSED', 'the three systems are parsed with each table`s key',
     all(k in COMP for k in ('genetic code', 'Shannon', 'Navier-Stokes')) and 'PARSE BY DIFFERENT KEYS' in FCOMP),
    ('G-GATE1B-QUOTED', 'Gate 1b`s note is quoted', 'decomposition-dependent' in COMP),
    ('G-EXAMPLES-NOT-REPAIRED', 'COMPLEX_ANALYSIS equals its pin blob',
     rb(os.path.join(PP, 'phase2', 'formation', 'COMPLEX_ANALYSIS.md')) == blob(PP, PIN_PP, 'phase2/formation/COMPLEX_ANALYSIS.md')),
    ('G-SLOTS-FIFTEEN-SEPARATE', 'no sentence of the bank or the closing joins the slots and the fifteen',
     not sentences_joined(BANK) and not sentences_joined(CLOSING)),
    ('G-NOSEAL-EDIT', 'FiniteSideSeal.lean carries its before-digest',
     kernel_same('*/d/SIDE-global-section/Core/FiniteSideSeal.lean', os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean'))),
    ('G-NOTUPLE-EDIT', 'Classes.lean carries its before-digest',
     kernel_same('*/d/SIDE-formation-arithmetic/SIDEFormationArithmetic/Classes.lean',
                 os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean'))),
    ('G-NOGRADE', 'no grade string minted', not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged', '0 premises discharged' in FBANK),
    ('G-NODOOR', 'the bank states 0 doors restated', '0 doors restated' in FBANK),
    ('G-NOROUTE', 'the bank states 0 routes proposed', '0 routes proposed' in FBANK),
    ('G-NOKAPPA', 'no kappa value measured', not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md is not written', 'FACES_LEDGER' not in ACT_WORK),
    ('G-NOFOLD', 'FINDINGS.md is not written', 'FINDINGS' not in ACT_WORK),
    ('G-NORULE', 'STRUCK_CLAUSES is not written', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no Zenodo byte', 'zenodo' not in ACT_WORK.lower()),
    ('G-NOPLATFORM', 'no platform call', not re.search('urllib|requests|http', ACT_WORK)),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 3),
    ('G-NOLOCKEDFACE', 'the seal still verifies', 'SEAL INTACT' in SEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-7])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-TRAIL-APPEND-ONLY', 'the trail block appended, the prior mark kept', '<!-- b418' in TRAILS and '<!-- b417' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'b417`s row at 266 and this act`s at 267, both by marker', ROW417 == [266] and ROW418 == [267]),
    ('G-WRITELIST-KINDS', 'the face names 11 kinds', 11 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
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
     not any(s in FBANK.lower() for s in ('the smear identity is proved', 'the theorem is proved',
                                          'the lock was overridden', 'a grade was moved', 'h2 has moved'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b418_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
say('=' * 100)
passing = failing = 0
for name, desc, res in ARMS:
    if res is None:
        res = (declared == run)
    ok = bool(res)
    passing += 1 if ok else 0
    failing += 0 if ok else 1
    say('  %-42s %-52s %s' % (name, desc[:52], 'PASS' if ok else '### **FAIL**'))
say('-' * 100)
say('  declared on the face : %d' % len(declared))
say('  run here             : %d' % len(run))
say('  declared but not run : %s' % (sorted(declared - run) or 'none'))
say('  run but not declared : %s' % (sorted(run - declared) or 'none'))
say('  sentences joining the slots and the fifteen -- bank : %s ; closing : %s'
    % (sentences_joined(BANK) or 'none', sentences_joined(CLOSING) or ('none' if CLOSING else '(no closing yet)')))
say('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**' % (len(ARMS), passing, failing))
say('=' * 100)
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if failing else 0)
