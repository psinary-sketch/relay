# -*- coding: utf-8 -*-
"""b419_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay a8de7d9, PLACE-papers
### bd8b1ba, SIDE-global-section 61a8abd), never to HEAD; correspondence rows are read by marker; a tracked
### file's sameness is read in GIT'S OWN VIEW (hash-object against the index), never by raw bytes, since a
### CRLF checkout of an LF blob differs on bytes and not on content (this act's own run-1 lesson).
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
import walker_guard as WG   # noqa: E402,F401  ### imported so the suite runs against the guard it cites

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CLASSES = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean')
PIN_RELAY, PIN_PP, PIN_SIDE = 'a8de7d9', 'bd8b1ba', '61a8abd'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b419_checks_postpush.txt' if POST else 'b419_checks.txt')
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


def git_unchanged_since_pin(repo, pin, rel):
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
    """### LEAN BLOCK COMMENTS (docstrings included) AND LINE COMMENTS REMOVED BEFORE ANY SEARCH FOR A TERM."""
    src = re.sub(r'/-.*?-/', ' ', src, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', src)


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'PROBE', 'VERIFY', 'RECL', 'LOCKP', 'TOUT', 'LOCK', 'GATE', 'BANK', 'TRAILS',
             'CORR', 'FACE', 'FERRY', 'SCAN', 'CLOSING', 'SEALV')


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


FACEPATH = os.path.join(D, 'b419_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b419_ferry.txt'))
SCAN = read(os.path.join(D, 'b419_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b419_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b419_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b419_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b419_extract.txt'))
EXT1 = read(os.path.join(D, 'b419_extract_run1.txt'))
COMP = read(os.path.join(D, 'b419_components.txt'))
PROBE = read(os.path.join(D, 'b419_n_probe.txt'))
VERIFY = read(os.path.join(D, 'b419_n_verify.txt'))
RECL = read(os.path.join(D, 'b419_twentyeight.txt'))
LOCKP = read(os.path.join(D, 'b419_lock_priced.txt'))
TOUT = read(os.path.join(D, 'b419_timeouts.txt'))
LOCK = read(os.path.join(D, 'b419_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b419_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b419_desk_notes.txt'))
BANK = read(os.path.join(D, 'b419_the_clause_printed.txt'))
CLOSING = read(os.path.join(D, 'b419_closing.txt'))
POPPATH = os.path.join(D, 'b419_timeout_population.json')
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
SEALF = os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean')
MODF = os.path.join(SIDE, 'Core', 'SmearGeneral.lean')
PROFB = rb(os.path.join(SIDE, 'AXIOM_PRINTS.txt'))
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FEXT, FDESK, FTOUT, FLOCKP = fold(BANK), fold(COMP), fold(EXT), fold(DESKN), fold(TOUT), fold(LOCKP)
FFACE = fold(FACE)
FSEALV = fold(SEALV)

SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b419_components.py'))
EXTSRC = read(os.path.join(T, 'b419_extract.py'))
DESKSRC = read(os.path.join(T, 'b419_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b419_')]
B418MARK = "**THE GENERAL CLAUSE IS OVER-BUDGET WITH ONE HELPER UNSUPPLIED, AND THE WALKER'S MISS WAS A SILENT"
B419MARK = "**THE GENERAL CLAUSE IS PROVED, ZERO AXIOMS, ON THE FIRST PROBE**"
ROW418 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B418MARK), CORR)]
ROW419 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B419MARK), CORR)]
NDIR = r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\fbe6b4b2-25ed-44b7-91cb-756e5456e21d\scratchpad\n419'
PROBES = sorted(f for f in os.listdir(NDIR) if re.match(r'p\d\d\.lean$', f)) if os.path.isdir(NDIR) else []
FIRSTPROBE = read(os.path.join(NDIR, 'p01.start')).strip()
LASTEND = read(os.path.join(NDIR, PROBES[-1][:-5] + '.end')).strip() if PROBES else ''
ANN = []
_a = read(os.path.join(D, 'b416_components.txt'))
_i = _a.find('(T1.4-a, b414)')
for _ln in _a[_a.rfind(NL, 0, _i) + 1:].splitlines():
    if not _ln.strip().startswith('|'):
        break
    ANN.append(_ln.strip()[1:].strip())


def minutes(a, b):
    from datetime import datetime
    f = '%Y-%m-%dT%H:%M:%SZ'
    try:
        return (datetime.strptime(b, f) - datetime.strptime(a, f)).total_seconds() / 60.0
    except Exception:
        return 1e9


def kernel_changed_paths():
    tracked = set(git(SIDE, 'diff', '--name-only', PIN_SIDE).split())
    untracked = set(git(SIDE, 'ls-files', '--others', '--exclude-standard', '--', 'Core', 'AllPrints.lean',
                        'AXIOM_PRINTS.txt').split())
    return (tracked | untracked) - {'CORRESPONDENCE.md'}


def seal_words_survive():
    old = (blob(SIDE, PIN_SIDE, 'Core/FiniteSideSeal.lean') or b'').decode('utf-8').split()
    new = read(SEALF).split()
    ta = ' '.join(ANN).split()
    return any(new[:i] == old[:i] and new[i:i + len(ta)] == ta and new[i + len(ta):] == old[i:]
               for i in range(len(old) + 1))


def allprints_procedure():
    old = blob(SIDE, PIN_SIDE, 'AllPrints.lean') or b''
    new = rb(os.path.join(SIDE, 'AllPrints.lean'))
    last = b'import SinglePrimeFactor\n'
    ins = old.replace(last, last + b'import SmearGeneral\n', 1)
    return (new.startswith(ins) and new[len(ins):] ==
            b'#print axioms SmearGeneral.smear_general\n#print axioms SmearGeneral.cells_are_instances\n')


def pop():
    import json
    try:
        return json.load(io.open(POPPATH, encoding='utf-8'))
    except Exception:
        return []


SCORED = [c for c in pop() if c.get('scope') != 'ELSEWHERE']
N_SAID = len([c for c in SCORED if c['timed_out']])
N_SILENT_BATCHED = len([c for c in SCORED if not c['timed_out'] and c['siblings'] > 0])
OLDPROF = blob(SIDE, PIN_SIDE, 'AXIOM_PRINTS.txt') or b''

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-SURVEY-RUN1-KEPT', 'survey run 1 kept, and run 2 maps with agreement',
     bool(EXT1) and 'AGREE' in EXT and 'DIFFER' not in EXT.split('two mappings are compared')[-1].split('written')[0]),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the first probe',
     'SEAL INTACT' in SEALV and bool(FIRSTPROBE) and stamp_of(FACE, 'locked at (UTC) :') < FIRSTPROBE),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT') and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-N-REPAIR-AS-NAMED', 'the probe carries b418`s named term',
     '.symm.trans (Nat.pow_succ r (j - 1))' in read(os.path.join(NDIR, 'p01.lean'))
     and '.trans (Nat.pow_succ r (j - 1))' in read(os.path.join(D, 'b418_components.txt'))),
    ('G-N-FIRST-PROBE-ONLY-REPAIR', 'the first probe differs from b418`s probe 16 by that one line',
     'lines differing : 1' in PROBE and 'and it is the named repair : True' in PROBE),
    ('G-N-PROBES-OUTSIDE-REPOS', 'every probe is a scratch file outside the repositories',
     bool(PROBES) and 'scratchpad' in NDIR and not NDIR.upper().startswith('D:')),
    ('G-N-BUDGET-HONOURED', 'no more than sixteen probes and 150 minutes',
     0 < len(PROBES) <= 16 and minutes(FIRSTPROBE, LASTEND) <= 150),
    ('G-N-ONE-VERDICT', 'exactly one verdict line',
     1 == len(re.findall(r'VERDICT : (PROVED|STILL FAILING|OVER-BUDGET)', FCOMP))),
    ('G-N-PROFILE-READ', 'the verdict is read from the profile`s lines, the exit line read by nothing',
     'VERDICT, READ FROM THE PROFILE : PROVED' in fold(PROBE) and 'read by nothing' in PROBE
     # ### REPAIRED AFTER RUN 1: the first version searched the RAW source and fired on `verdict_of`s own
     # ### docstring, which says the verdict is NEVER read from the exit code. ### It now reads the CODE only.
     and 'EXIT' not in pycode_of(COMPSRC[COMPSRC.find('def verdict_of'):COMPSRC.find('def run_n_probe')]).upper()),
    ('G-N-PROFILES-BANKED', 'every probe`s source and printed profile is banked',
     PROBE.count('THE PRINTED PROFILE, IN FULL') == len(PROBES) and '### THE PROBE`S SOURCE, IN FULL' in PROBE),
    ('G-N-NO-SORRY', 'no probe and no Core file carries sorry as a term',
     all(not re.search(r'\bsorry\b', lean_code(read(os.path.join(NDIR, f)))) for f in PROBES)
     and all(not re.search(r'\bsorry\b', lean_code(read(os.path.join(SIDE, 'Core', f))))
             for f in os.listdir(os.path.join(SIDE, 'Core')) if f.endswith('.lean'))),
    ('G-N-KERNEL-BY-VERDICT', 'PROVED, and the kernel changed in exactly the four named files',
     'VERDICT : PROVED' in FCOMP and kernel_changed_paths() ==
     {'AXIOM_PRINTS.txt', 'AllPrints.lean', 'Core/FiniteSideSeal.lean', 'Core/SmearGeneral.lean'}),
    ('G-N-PREFIX-TRUE', 'the pin`s profile is a true byte prefix of the kernel`s',
     bool(OLDPROF) and PROFB.startswith(OLDPROF) and len(PROFB) > len(OLDPROF)),
    ('G-N-ALLPRINTS-APPEND-ONLY', '(C)(ii)`s measure: one import inserted, the prints appended', allprints_procedure()),
    ('G-N-CELLS-INSTANCES', 'the terminal deriving the seven cells prints clean',
     b"'SmearGeneral.cells_are_instances' does not depend on any axioms" in PROFB
     and b"'SmearGeneral.smear_general' does not depend on any axioms" in PROFB),
    ('G-N-RECLASSIFIED', 'eight qualified and twenty unreached, over b414`s hand-read',
     RECL.count('QUALIFIED BY THE PROOF   b414:') == 8 and RECL.count('UNREACHED BY THE PROOF   b414:') == 20),
    ('G-N-T14-VERBATIM', 'every line of b416`s drafted annotation is in the seal',
     len(ANN) == 4 and all(a in read(SEALF) for a in ANN)),
    ('G-N-SEAL-WORDS-SURVIVE', 'every word of the seal at the pin survives in order', seal_words_survive()),
    ('G-N-CLASSES-UNCHANGED', 'Classes.lean carries its before-digest',
     hashlib.sha256(rb(CLASSES)).hexdigest().startswith('d4f931db1d50c01f')),
    ('G-N1-APART', '(N1)`s three clauses printed on three lines',
     all(k in COMP for k in ('the verdict PROVED', 'the profile empty', 'on the first attempt'))),
    ('G-LOCK-RULES-QUOTED', 'both rules quoted from their sources',
     "'### VERDICT: ### **0 HIT(S) REPORTED.'" in LOCKP and 'A HIT IS A STRING, NOT A FAULT' in LOCKP),
    ('G-LOCK-ROUTES-PRICED', 'three routes, each with a cost, a who and a lane',
     all(('ROUTE (%d)' % k) in LOCKP for k in (1, 2, 3)) and LOCKP.count('cost :') == 3 and LOCKP.count('lane :') == 3),
    ('G-LOCK-LANE-NAMED', 'the route needing the instrument lane is named', 'ONLY ROUTE (2) NEEDS THE INSTRUMENT LANE' in FLOCKP),
    ('G-LOCK-FREQUENCY', 'every scan read by its verdict line, the refusals counted',
     'scan records read :' in LOCKP and 'with a verdict line reading a non-zero count :' in LOCKP),
    ('G-LOCK-ROUTED', 'routed to the author, none chosen', 'ROUTED TO THE AUTHOR. THIS ACT CHOOSES NONE' in FLOCKP),
    ('G-NOLOCKGATE-EDIT', 'the lock gate unchanged since the pin, in git`s view',
     git_unchanged_since_pin(ROOT, PIN_RELAY, 'tools/b378_lockgate.py')),
    ('G-NOSCAN-EDIT', 'the scan unchanged since the pin, in git`s view',
     git_unchanged_since_pin(ROOT, PIN_RELAY, 'tools/ferry_scan.py')),
    ('G-T-POPULATION-LISTED', 'the population record exists and every scored call is listed',
     len(SCORED) > 0 and len(re.findall(r'A BANKED VERDICT RESTS ON IT : (YES|NO)', TOUT)) == len(SCORED)),
    ('G-T-ACT-MAPPED', 'every scored call carries an act or NO ACT',
     len(re.findall(r'batch \d+  act (b\d+|NO ACT) \(lag', TOUT)) == len(SCORED)),
    ('G-T-BATCH-SAID', 'every silent batched call is said to be beyond the guard',
     TOUT.count('THE RECORD DOES NOT ALLOW THE GUARD') == N_SILENT_BATCHED),
    ('G-T-GUARD-APPLIED', 'every call whose result says timeout reads INCOMPLETE',
     TOUT.count('INCOMPLETE -- the tool`s own result says it timed out') == N_SAID),
    ('G-T-RESTING-READ', 'every decision printed with the line read, none unread',
     'UNREAD' not in TOUT and TOUT.count('line read :') == len(SCORED)),
    ('G-T-CONTROL-FIRST', 'the control passes and precedes every re-run',
     'CONTROL : PASS' in FTOUT and 0 < TOUT.find('POSITIVE CONTROL') < TOUT.find('### RE-RUN')),
    ('G-T-CONFIRMED-OR-MOVED', 'each resting verdict reads CONFIRMED or MOVED',
     'BANKED VERDICTS RESTING ON A TIMED-OUT CALL : 2' in FTOUT
     and len(re.findall(r'### \*\*(CONFIRMED|MOVED)\*\*', COMP)) == 2),
    ('G-T-NO-REVERDICT', 'neither resting act`s bank changed since the pin',
     git_unchanged_since_pin(ROOT, PIN_RELAY, 'data/b231_the_two.txt')
     and git_unchanged_since_pin(ROOT, PIN_RELAY, 'data/b300_the_archimedean_leg.txt')),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in TRAILS.split('<!-- b419')[-1] for k in (1, 2, 3, 4))
     and TRAILS.split('<!-- b419')[-1].count('**OPEN.**') == 4 and 'Trigger: the ruling on which test governs' in BANK),
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
    # ### REPAIRED AFTER RUN 1 (kept as b419_checks_run1.txt): the arm read the raw verify text, which this suite`s
    # ### own G-NOBORROWEDBAR forbids a G-NO arm to do; it reads the folded copy, as every other G-NO arm does.
    ('G-NOLOCKEDFACE', 'the seal still verifies', 'SEAL INTACT -- the body is byte-for-byte what was sealed' in FSEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-8])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     read(os.path.join(PP, 'OPEN_TRAILS.md')).startswith((blob(PP, PIN_PP, 'OPEN_TRAILS.md') or b'x').decode('utf-8').rstrip(NL))
     and '<!-- b419' in TRAILS and '<!-- b418' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'b418`s row at 267 and this act`s at 268, both by marker', ROW418 == [267] and ROW419 == [268]),
    ('G-WRITELIST-KINDS', 'the face names 10 kinds', 10 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
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
                                          'h2 has moved', 'the identification with the source is compiled'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b419_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
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
say('  ### the face`s BAR 3 clause, as written -- AllPrints` prior bytes a prefix of its new : %s ### (a defect of the'
    % (rb(os.path.join(SIDE, 'AllPrints.lean')).startswith(blob(SIDE, PIN_SIDE, 'AllPrints.lean') or b'x')))
say('  ### face: Lean takes an import only at a file`s head; (C)(ii)`s measure is the arm G-N-ALLPRINTS-APPEND-ONLY)')
say('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**' % (len(ARMS), passing, failing))
say('=' * 100)
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if failing else 0)
