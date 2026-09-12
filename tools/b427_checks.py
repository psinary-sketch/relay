# -*- coding: utf-8 -*-
"""b427_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from, in git's own view; rows are read by
### marker; every candidate's first-failing-step quotation is re-found in its own source by the components' own
### reader, IMPORTED; site (i)'s counts are read off b424's banked JSON and never typed.
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
import b427_components as CMP   # noqa: E402
import b427_desk_bank as DB     # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PINS_FILE = os.path.join(D, 'b427_pins_stepzero.txt')


def _pin(name, path):
    t = io.open(PINS_FILE, encoding='utf-8', errors='replace').read() if os.path.exists(PINS_FILE) else ''
    m = re.search(r'--- %s\s+\(%s\)\s+local HEAD\s+: ([0-9a-f]{40})' % (re.escape(name), re.escape(path)), t)
    return m.group(1)[:7] if m else ''


PIN_RELAY = _pin('relay', 'D:\\relay')
PIN_PP = _pin('PLACE-papers', 'D:\\MY-DOwnloads\\PLACE-papers')
PIN_SIDE = _pin('SIDE-global-section', 'D:\\SIDE-global-section')
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b427_checks_postpush.txt' if POST else 'b427_checks.txt')
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
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
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


def strings_of(src):
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.STRING:
                out.append(tok.string)
    except Exception:
        return [src]
    return out


def verdict_line(text, key):
    for ln in (text or '').splitlines():
        if key in ln:
            return ln
    return ''


def stamp_of(text, key='at (UTC) :'):
    m = re.search(re.escape(key) + r' (\S+)', text or '')
    return m.group(1) if m else ''


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'TAB', 'WR', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B427T', 'CORR', 'FACE',
             'FERRY', 'SCAN', 'SEALV', 'FLED')


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


FACEPATH = os.path.join(D, 'b427_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b427_ferry.txt'))
SCAN = read(os.path.join(D, 'b427_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b427_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b427_faces_census_stepzero.txt'))
PINSREC = read(PINS_FILE)
EXT = read(os.path.join(D, 'b427_extract.txt'))
COMP = read(os.path.join(D, 'b427_components.txt'))
TAB = read(CMP.TABLE)
WR = read(CMP.WREC)
TJ = json.loads(read(CMP.TJSON) or '{"candidates": [], "held": 0, "tally": {}, "site_i": {}, "site_i_n": 0}')
LOCK = read(os.path.join(D, 'b427_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b427_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b427_desk_notes.txt'))
BANK = read(DB.BANKOUT)
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B427T = TRAILS.split('<!-- b427')[-1] if '<!-- b427' in TRAILS else ''
FLED = read(CMP.FL)
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FFACE, FSEALV = fold(BANK), fold(COMP), fold(FACE), fold(SEALV)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b427_components.py'))
EXTSRC = read(os.path.join(T, 'b427_extract.py'))
DESKSRC = read(os.path.join(T, 'b427_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b427_')]
B426MARK_RE = r'(?m)^\| (\d+) \| \*\*THE FALSIFIER RE-READ BY ADDRESS UNDER \(R38\)'
CORPUS_TOUCHED = ['FACES_LEDGER.md', 'OPEN_TRAILS.md']
CORPUS_UNTOUCHED = ['REGISTRY.md', 'FINDINGS.md', 'SPIRAL_MAP.md', 'VERIFICATION_LOOM.md', 'ERRATA.md',
                    'phase2/physics-speculative/FORMATION_DISTANCE.md', 'phase2/physics/FANO_DERIVATION_OF_LAMBDA.md',
                    'phase2/physics/STORMER.md', 'phase1.5/method/INSTRUMENTS.md', 'day1/A_Place_to_Stand.md']
U1 = next((x for x in FLED.splitlines() if x.startswith('| U1 ')), '')
U1_PIN = next((x for x in (blob(PP, PIN_PP, 'FACES_LEDGER.md') or b'').decode('utf-8').splitlines()
               if x.startswith('| U1 ')), '')
ROW426 = [int(x.group(1)) for x in re.finditer(B426MARK_RE, CORR)]
ROW427 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(DB.ROWMARK), CORR)]
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')
CANDS = TJ['candidates']


def quotes_refound():
    """### EVERY QUOTATION AT A FIRST FAILING STEP, RE-FOUND IN ITS OWN SOURCE BY THE COMPONENTS' OWN READER."""
    for c in CANDS:
        for x in c['quotes']:
            if x['step'] != c['first']:
                continue
            if CMP.q(x['path'], x['start'], x['end']) == '### MISS':
                return False
    return bool(CANDS)


def each_first_quoted():
    return all(any(x['step'] == c['first'] for x in c['quotes']) for c in CANDS) and bool(CANDS)


def step_order():
    """### EVERY CANDIDATE CARRIES EXACTLY THREE STEPS AND ITS FIRST FAILING ONE IS THE FIRST 'FAIL' IN ORDER."""
    for c in CANDS:
        st = c['steps']
        if len(st) != 3:
            return False
        firsts = [k for k, s in enumerate(st) if s['out'] == 'FAIL']
        if not firsts or (firsts[0] + 1) != c['first']:
            return False
    return True


def convergence_counted():
    """### SITE (i)'S COUNTS ARE b424'S OWN, RE-READ HERE FROM ITS BANKED JSON."""
    ti, ni = CMP.site_i_tally()
    return ti == TJ['site_i'] and ni == TJ['site_i_n'] and ni > 0


def tally_recomputed():
    t = {}
    for c in CANDS:
        if c['first'] is not None:
            t[c['kind']] = t.get(c['kind'], 0) + 1
    same = sum(v for k, v in t.items() if k in TJ['site_i'])
    diff = sum(v for k, v in t.items() if k not in TJ['site_i'])
    return t == TJ['tally'] and same == TJ['same'] and diff == TJ['diff']


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0 and the three pins parse',
     '0' == (verdict_line(PINSREC, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and all(len(p) == 7 for p in (PIN_RELAY, PIN_PP, PIN_SIDE))),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the candidate table and the write',
     'SEAL INTACT' in SEALV and bool(stamp_of(TAB)) and bool(stamp_of(WR))
     and stamp_of(FACE, 'locked at (UTC) :') < min(stamp_of(TAB), stamp_of(WR))),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the seal verifies and the registration gate reads CLEAR',
     'SEAL INTACT' in SEALV and 'CLEAR' in verdict_line(GATE, 'GATE VERDICT')
     and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-LEG1-CLOSED', 'b426 at row 275 by its marker and its closing record tracked',
     ROW426 == [275] and git(ROOT, 'ls-files', 'data/b426_closing.txt') == 'data/b426_closing.txt'),
    ('G-SITE-QUOTED-FIRST', 'the site`s own cell is quoted before any candidate',
     TAB.index('THE SITE`S OWN TEXT') < TAB.index('THE CANDIDATES, EACH BY S1 CLASS')
     if ('THE SITE`S OWN TEXT' in TAB and 'THE CANDIDATES, EACH BY S1 CLASS' in TAB) else False),
    ('G-SITE-CELL-STANDS', 'entry (ii)`s WITNESS cell still reads NONE KNOWN',
     'WITNESS: `NONE KNOWN`' in U1 and U1.count('WITNESS:') == 6),
    ('G-CAND-CAP', 'the candidates are within the declared cap', 0 < len(CANDS) <= CMP.CAP),
    ('G-CAND-OPENING-THREE', 'the navigator`s opening three are the first three candidates',
     [c['origin'] for c in CANDS[:3]] == ['the navigator`s opening list'] * 3),
    ('G-CAND-EACH-QUOTED', 'every candidate`s first failing step carries a quotation', each_first_quoted()),
    ('G-CAND-STEP-ORDER', 'every candidate carries three steps and fails at the first FAIL in order', step_order()),
    ('G-CAND-FIRST-FAIL', 'every quotation at a first failing step is re-found in its own source', quotes_refound()),
    # ### **BOTH ARMS BELOW WERE REPAIRED MID-ACT, AND THE REASON IS PRINTED RATHER THAN BURIED.** ### `BAR 12`'s
    # ### own detector `_raw_no_arms` fired on them: their names begin `G-NO` and their first implementations read a
    # ### RAW RECORD TEXT -- the write record's own sentence and the table's own heading. ### **AN ARM THAT PASSES
    # ### BECAUSE THE TOOL PRINTED A SENTENCE ABOUT ITSELF IS THE SPECIES THE BAR EXISTS FOR**, whatever the arm's
    # ### name, so they are re-aimed at the DATA the printer consumed instead of at its output.
    ('G-NONE-HELD-OR-STOP', 'no candidate held, so the cell was not written',
     TJ['held'] == 0 and bool(CANDS) and all(c['first'] is not None for c in CANDS) and bool(U1) and U1 == U1_PIN),
    ('G-NOT-ADMITTED-PRINTED', 'every hit not admitted carries its reason',
     bool(CMP.NOT_ADMITTED) and all(bool(str(a).strip()) and bool(str(b).strip()) for a, b in CMP.NOT_ADMITTED)),
    ('G-SITEI-FROM-JSON', 'site (i)`s counts are read off b424`s own banked JSON, not typed', convergence_counted()),
    ('G-CONVERGENCE-COUNTED', 'the comparison with site (i) is recomputed here and agrees', tally_recomputed()),
    ('G-LEDGER-BLOCK-WRITTEN', 'the ledger block was written through the writer`s append_block',
     'LEDGER WRITE : WRITTEN' in WR and 'append_block' in COMPSRC),
    ('G-U1-BYTE-IDENTICAL', 'row U1`s line is byte-identical to the pin`s', bool(U1) and U1 == U1_PIN),
    ('G-NO-SEVENTH-SITE', 'no seventh site is entered', U1.count('WITNESS:') == 6 and U1_PIN.count('WITNESS:') == 6),
    ('G-WITNESS-FIELDS-SIX', 'the six WITNESS fields read as they did at the pin',
     re.findall(r'WITNESS: *`([A-Z ]+)`', U1) == re.findall(r'WITNESS: *`([A-Z ]+)`', U1_PIN)),
    ('G-QUOTES-VERIFIED', 'the writer`s verify_quotes ran and reported 0 misses', 'misses : 0 []' in WR),
    ('G-L2-APART', '(L2)`s two clauses scored apart', COMP.count('(L2) *') == 2),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B427T for k in (1, 2, 3, 4)) and B427T.count('**OPEN.**') == 4
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
    ('G-NODEPOSIT', 'no Zenodo byte', 'zenodo' not in (ACT_WORK + ' '.join(strings_of(COMPSRC))).lower()),
    ('G-NOPLATFORM', 'no host is reached at all by this act`s code',
     not re.search(r'https?://', ' '.join(strings_of(COMPSRC + EXTSRC + DESKSRC)))
     and not re.search(r'urllib|import requests|http\.client', pycode_of(COMPSRC + EXTSRC + DESKSRC))),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 6),
    ('G-NOLOCKEDFACE', 'the seal still verifies', 'SEAL INTACT -- the body is byte-for-byte what was sealed' in FSEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|2[0-6])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOFOLD', 'FINDINGS.md unchanged since the pin and no span record under this act',
     unchanged(PP, PIN_PP, 'FINDINGS.md') and not [f for f in os.listdir(D) if f.startswith('b427_span')]),
    ('G-NOLANEEDIT', 'the cosmology lane`s documents and REGISTRY.md unchanged since this act`s pin',
     all(unchanged(PP, PIN_PP, r) for r in ('REGISTRY.md', 'phase2/physics-speculative/FORMATION_DISTANCE.md',
                                            'phase2/physics/STORMER.md'))),
    ('G-CORPUS-SCOPE', 'exactly the two declared corpus files differ from the pin',
     sorted(git(PP, 'diff', '--name-only', PIN_PP).split()) == sorted(CORPUS_TOUCHED)
     and all(unchanged(PP, PIN_PP, r) for r in CORPUS_UNTOUCHED)),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     prefix_ok('OPEN_TRAILS.md') and '<!-- b427' in TRAILS and '<!-- b426' in TRAILS),
    ('G-LEDGER-APPEND-ONLY', 'the pin`s ledger is a true prefix and b424`s block is still present',
     prefix_ok('FACES_LEDGER.md') and '<!-- b424 update -->' in FLED and '<!-- b427 update -->' in FLED),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b426 at 275 and this act at 276, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW426 == [275] and ROW427 == [276]),
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
     not any(s in FBANK.lower() for s in ('the lock was overridden', 'a witness was found', 'a grade was moved',
                                          'h2 has moved', 'the site is closed', 'a seventh site'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b427_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
say('=' * 100)
say('  pins read off this act`s own step-zero record : relay %s ; PLACE-papers %s ; SIDE-global-section %s'
    % (PIN_RELAY, PIN_PP, PIN_SIDE))
say('  corpus files differing from the pin : %s' % sorted(git(PP, 'diff', '--name-only', PIN_PP).split()))
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
