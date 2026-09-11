# -*- coding: utf-8 -*-
"""b417_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY
### ARM RUN HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.

### ### **EVERY ARM THAT READS A CORRESPONDENCE ROW READS IT BY ITS MARKER**, and every arm that
### compares a corpus file to its prior state compares it to the blob at the pin the act started from
### (`PLACE-papers 85b8daa`), not to `HEAD` -- after the push `HEAD` is this act's own commit.
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
import repair_snapshot as RS   # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
FX = os.path.join('D:', os.sep, 'SIDE-effects')
TECHNE = os.path.join(DL, 'TECHNE-Core')
MOD = os.path.join(TECHNE, 'modules', '2026-09')
SEAL = os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean')
CLASSES = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean')
PLACED = os.path.join(PP, 'heritage', 'PRIME_CORE_READER.md')
CANON = os.path.join(DL, 'PRIME_CORE_READER.md')
PIN_PP = '85b8daa'
PIN_RELAY = '20ce1c7'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b417_checks_postpush.txt' if POST else 'b417_checks.txt')
NL = chr(10)

L = []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


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
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


RULE_RE = re.compile('[-=#]{8,}')


def fold(s):
    s = RULE_RE.sub('. ', (s or ''))
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def pycode_of(src):
    """### **DROP EVERY STRING AND COMMENT TOKEN, BY PYTHON`S OWN TOKENIZER.**"""
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
    """### `A2`: ### **READ THE TOOL`S VERDICT LINE, NEVER THE WORD AS A SUBSTRING.**"""
    for ln in (text or '').splitlines():
        if key in ln:
            return ln
    return ''


def stamp_of(text, key='run at (UTC) :'):
    m = re.search(re.escape(key) + r' (\S+)', text or '')
    return m.group(1) if m else ''


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'SNAP', 'LIVE', 'SWEEP', 'PLACEREC', 'READS', 'LOCK', 'GATE',
             'BANK', 'TRAILS', 'CORR', 'FACE', 'FERRY', 'SCAN', 'MODULE', 'CLOSING')


def _raw_no_arms():
    """### RETURN the `G-NO*` arms whose test reads a raw document text."""
    src = read(os.path.abspath(__file__))
    bad = []
    try:
        tree = ast.parse(src)
    except Exception:
        return ['PARSE-FAILED']
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Assign)
                and any(getattr(t, 'id', '') == 'ARMS' for t in node.targets)):
            continue
        for el in node.value.elts:
            if not (isinstance(el, ast.Tuple) and len(el.elts) == 3):
                continue
            nm = getattr(el.elts[0], 'value', '')
            if not (isinstance(nm, str) and nm.startswith('G-NO')):
                continue
            names = {n.id for n in ast.walk(el.elts[2]) if isinstance(n, ast.Name)}
            if names & set(RAW_TEXTS):
                bad.append(nm)
    return bad


FACE = read(os.path.join(D, 'b417_registration_2026-09-11.txt'))
FERRY = read(os.path.join(D, 'b417_ferry.txt'))
SCAN = read(os.path.join(D, 'b417_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b417_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b417_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b417_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b417_extract.txt'))
EXT1 = read(os.path.join(D, 'b417_extract_run1.txt'))
COMP = read(os.path.join(D, 'b417_components.txt'))
SNAP = read(os.path.join(D, 'b417_snapshot.txt'))
LIVE = read(os.path.join(D, 'b417_live.txt'))
SWEEP = read(os.path.join(D, 'b417_sweep.txt'))
PLACEREC = read(os.path.join(D, 'b417_place.txt'))
READS = read(os.path.join(D, 'b417_reads.txt'))
LOCK = read(os.path.join(D, 'b417_lockgate_notes.txt'))
SEALV = read(os.path.join(D, 'b417_reg_seal_verify.txt'))
GATE = read(os.path.join(D, 'b417_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b417_desk_notes.txt'))
BANK = read(os.path.join(D, 'b417_the_contradiction_put.txt'))
CLOSING = read(os.path.join(D, 'b417_closing.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
MODULE = read(os.path.join(MOD, 'SAFE_BY_BEING_BROKEN.md'))
KD = read(os.path.join(D, 'b417_kernel_digests_before.txt')).split()
SEALBEF, CLSBEF = (KD[0] if KD else ''), (KD[2] if len(KD) > 2 else '')

FBANK, FCOMP, FEXT, FDESK = fold(BANK), fold(COMP), fold(EXT), fold(DESKN)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b417_components.py'))
EXTSRC = read(os.path.join(T, 'b417_extract.py'))
DESKSRC = read(os.path.join(T, 'b417_desk_bank.py'))
RSSRC = read(os.path.join(T, 'repair_snapshot.py'))
HYGSRC = read(os.path.join(T, 'b369_hygiene.py'))
ACT_SRC = SELFSRC + COMPSRC + EXTSRC + DESKSRC + RSSRC
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC + RSSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b417_')]
PB, CB = rb(PLACED), rb(CANON)
HL = PB.find(b'# PRIME CORE')
HEAD_NOW = PB[:HL].decode('utf-8', 'replace') if HL > 0 else ''
OLDPLACED = blob(PP, PIN_PP, 'heritage/PRIME_CORE_READER.md') or b''
OLDHEAD = OLDPLACED[:OLDPLACED.find(b'# PRIME CORE')].decode('utf-8', 'replace') if OLDPLACED else ''
CL_I = HEAD_NOW.find('**AND A FOURTH, per (R33)')
CLAUSE = HEAD_NOW[CL_I:HEAD_NOW.find('---', CL_I)] if CL_I > 0 else ''
B416MARK = 'THE TUPLES CONTRADICT THE UNIVERSALITY CLAIM THAT WOULD HAVE DERIVED THEM'
B417MARK = '**READING (a) WOULD LEAVE TWO DISTINCT TUPLES WHERE THE MODEL NAMES FOUR CLASSES'
ROW416 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| \*\*' + re.escape(B416MARK), CORR)]
ROW417 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B417MARK), CORR)]
HYG_NUM = git(ROOT, 'diff', '--numstat', PIN_RELAY, '--', 'tools/b369_hygiene.py')
MODIFIED_TOOLS = sorted(x.split('/')[-1] for x in git(
    ROOT, 'diff', '--name-only', '--diff-filter=M', PIN_RELAY, '--', 'tools').splitlines() if x.strip())
TECH_LR = git(TECHNE, 'rev-list', '--left-right', '--count', 'origin/main...HEAD').split()
TECH_REMOTE_HAS = git(TECHNE, 'branch', '-r', '--contains', '4aaf600')
BAKS_NOW = [f for f in os.listdir(os.path.join(FX, '.githooks')) if '.b304-backup' in f]


def two_records_restored():
    return all(rb(os.path.join(D, f)) == (blob(ROOT, PIN_RELAY, 'data/' + f) or b'x')
               for f in ('b369_hooks.txt', 'b369_hygiene.json')) and \
        not os.path.exists(os.path.join(D, 'b369_hygiene_notes2.txt'))


SLOT = re.compile(r'\bn[1-4]\b|n[₁₂₃₄]|\btuples?\b|\bOmega\b|Ω|universality sentence|\bratios?\b')
FIFTEEN = re.compile(r'\bP\b|Prime[ -]Core|\bdeserts?\b|the fifteen|\bReader\b')


def joined_sentences(text):
    """### THE AMENDMENT, MADE MECHANICAL: a sentence naming a slot AND a member-of-P subject."""
    out = []
    for s in re.split(r'(?<=[.!?])\s+|\n', text or ''):
        if SLOT.search(s) and FIFTEEN.search(s):
            out.append(s.strip()[:120])
    return out


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker, part 1 of 1',
     'paste ends (part 1 of 1)' in FERRY),
    ('G-AMENDMENT-BANKED', 'the amendment is in the ferry file and on the face as before the lock',
     'AMENDMENT to ACT b417, ratified by this paste' in FERRY
     and 'THE AMENDMENT ARRIVED BEFORE THIS FACE EXISTED' in FACE),
    ('G-SCAN-CLEAN', 'the scan VERDICT LINE reports 0 hits',
     '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins tool reports REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0',
     'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-SURVEY-RUN1-KEPT', 'the first run is kept, with its two misses',
     'ANCHOR MISSES : 2' in fold(verdict_line(EXT1, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies, and it was taken before the first component run',
     'SEAL INTACT' in SEALV and 'LOCKED BEFORE ANY WRITE' in FACE
     and bool(stamp_of(FACE, 'locked at (UTC) :')) and bool(stamp_of(SNAP))
     and stamp_of(FACE, 'locked at (UTC) :') < stamp_of(SNAP)),
    ('G-LOCKGATE-EIGHT', 'the lock gate read 8 gates, 8 passing, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict line reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT') and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-RULINGS-RATIFIED-NOT-EXTENDED', 'the face says both rulings are executed, not extended',
     'it does not improve on either and does not extend either' in fold(FACE)),

    ('G-NOLEAN', 'no .lean file is opened for write by any tool of this act',
     not re.search(r"\.lean[^)]{0,40}['\"]w", ACT_WORK)),
    ('G-NOBUILD', 'no working tool names the Lean compiler as a program to run',
     not re.search(r"run\([^)]{0,40}lean", ACT_WORK, re.I)),
    ('G-NOTERMINAL', 'the act states 0 terminals added, in its bank', '0 terminals added' in FBANK),
    ('G-SEAL-DIGEST-UNCHANGED', 'FiniteSideSeal.lean carries the sha256 recorded before the act',
     bool(SEALBEF) and hashlib.sha256(rb(SEAL)).hexdigest() == SEALBEF),
    ('G-NOTUPLE-EDIT', 'Classes.lean carries the sha256 recorded before the act',
     bool(CLSBEF) and hashlib.sha256(rb(CLASSES)).hexdigest() == CLSBEF),
    ('G-NOSENTENCE-EDIT', 'MATTER_AS_ARITHMETIC equals its blob at the starting pin',
     rb(os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md'))
     == blob(PP, PIN_PP, 'phase2/physics/MATTER_AS_ARITHMETIC.md')),

    ('G-DEFECT-REPORT-SIDE-BY-SIDE', 'both halves are printed in their own words',
     'Three of four formation components are universal' in COMP and 'classB := (3, 2, 2, 0)' in COMP),
    ('G-OWNER-CARRIES-BOTH', 'the citation control found the owner carrying both halves',
     'MATTER_AS_ARITHMETIC in the BOTH bucket : True' in FEXT),
    ('G-CITERS-TWO-SHAPES', 'both shapes ran and both yields are printed',
     'A SECOND SHAPE' in EXT and 'first shape' in COMP and 'second shape' in COMP),
    ('G-CITERS-RESIDUE-HAND-READ', 'every residue document is printed in full and scored with its words',
     all(r in READS and r in COMP for r in (
         'phase1.5/structural/AT_REST.md', 'phase2/formation/CAPACITY.md',
         'phase2/formation/UNIVERSALITY.md', 'meta/W1_REVIEW_DIGEST.md',
         'phase2/physics/YANG_MILLS_MONOGRAPH.md', 'phase2/quantum/ARITHMETIC_ORIGIN_QECC.md'))),
    ('G-NO-SEAT-RULING', 'no sentence of the bank says the sentence or the tuples are wrong',
     # ### REPAIRED AFTER RUN 1, WHEN `G-NOBORROWEDBAR` CAUGHT IT: its positive half read the RAW
     # ### components text; it reads the folded text now, as every `G-NO*` arm must.
     not re.search(r'\b(sentence|tuples?) (is|are) (the )?wrong', FBANK, re.I)
     and 'NOT SCORED BY THIS SEAT' in FCOMP),
    ('G-COSTS-PRICED', 'what each change would cost is printed', 'WHAT EACH CHANGE WOULD COST' in COMP),
    ('G-OMEGA-FOUR-AGAINST-HEADER', 'four header figures read, each agreeing with the formula',
     'header Omega figures read : 4' in EXT
     and 4 == len(re.findall(r'(?m)^  [ABCD] +\(\d, \d, \d, \d\) +\S+ +\S+ +True', EXT))),
    ('G-LOADBEARING-B-D', 'n2 = 2 is load-bearing for B and for D',
     'LOAD-BEARING FOR BOTH B AND D' in FCOMP),
    ('G-R34-MOVES-PRINTED', 'every stated figure marked, moves and unmoved both present',
     'MOVES' in COMP and 'unmoved' in COMP and 'NO FIGURE MOVES ANYWHERE' in FCOMP),
    ('G-CLASS-A-UNMOVED-BOTH', 'class A`s value is named unmoved under both readings',
     '4/81 UNDER READING (a), 4/81 UNDER READING (b). UNMOVED UNDER BOTH' in FCOMP),

    ('G-B369-REPAIRED', 'the tool names the single source b386 left',
     "'.githooks', 'pre-push')" in HYGSRC and "'git-hooks'" not in pycode_of(HYGSRC)),
    ('G-SNAPSHOT-BEFORE-LIVE', 'the snapshot ran before the live run, by the records` own clocks',
     bool(stamp_of(SNAP)) and bool(stamp_of(LIVE)) and stamp_of(SNAP) < stamp_of(LIVE)
     and 'the snapshot record precedes this run : True' in LIVE),
    ('G-SNAPSHOT-DIFF-PRINTED', 'contained and escaped writes are both printed',
     'CONTAINED WRITES' in SNAP and 'ESCAPED WRITES' in SNAP),
    ('G-ESCAPES-RESTORED', 'the snapshot left 0 files differing; what bytes cannot restore is named',
     'FILES STILL DIFFERING AFTER THE RESTORE : 0' in fold(SNAP) and 'NAMED, NOT RESTORABLE BY BYTES' in SNAP),
    ('G-B369-RUNS-AFTER', 'no FileNotFoundError in either run',
     'FileNotFoundError in the live run : False' in LIVE
     and 'FileNotFoundError in the snapshot run : False' in SNAP),
    ('G-B369-VERDICT-NOT-EDITED', 'one code line removed, and its verdict expression intact',
     HYG_NUM.split()[1:2] == ['1'] and 'ok = (identical and nfail == 0 and ok_syntax' in HYGSRC),
    ('G-PRIOR-RECORDS-RESTORED', 'both prior-act records equal their blobs; no run record left',
     two_records_restored() and 'BYTES AGAINST THE BLOB SAY 0' in fold(COMP)),
    ('G-BACKUPS-BY-RULE', 'swept only because every byte was in a store, and none remain',
     # ### REPAIRED AFTER RUN 1: the needle kept a backtick the fold strips, so it could never match.
     'EVERY BACKUPS BYTES PRESENT IN AN OBJECT STORE, AND NONE TRACKED : True' in fold(SWEEP)
     and 'content lost : 0' in SWEEP and not BAKS_NOW),
    ('G-ONLY-B369-REPAIRED', 'the existing relay tools modified are b369_hygiene.py and the index only',
     MODIFIED_TOOLS == ['b369_hygiene.py', 'banked_index.py']),
    ('G-HARNESS-FIXTURES-BOTH-POLARITIES', 'the harness`s fixtures pass now, both polarities',
     RS.self_test(verbose=False) and 'both polarities, before it is trusted : PASS' in SNAP),
    ('G-SPECIES-FILED-BESIDE', 'the module sits beside the two siblings',
     bool(MODULE) and os.path.exists(os.path.join(MOD, 'DATED_ARM.md'))
     and os.path.exists(os.path.join(MOD, 'GUARD_WITH_NOTHING_LISTENING.md'))),
    ('G-SPECIES-CARRIES-B416-WHOLE', 'the retired path, the SameFileError, the prior record rewritten',
     all(k in MODULE for k in ('The retired path', 'SameFileError', 'The prior record rewritten'))),
    ('G-SPECIES-LOCAL-NOT-PUSHED', 'TECHNE: origin-only 0, local-only 17, no remote branch carries it',
     TECH_LR == ['0', '17'] and not TECH_REMOTE_HAS),

    ('G-CAVEATS-LISTED', 'the unchanged description yields its caveats', '13 caveats in 9 files' in FEXT),
    ('G-CAVEAT-CONTROL-HOLDS', 'the b413/b414 control found (T1.4) named',
     # ### REPAIRED AFTER RUN 1: the parentheses were a regex group, not the literal `(T1.4)`.
     bool(re.search(re.escape('records of b413/b414 naming (T1.4) : ') + r'([1-9]\d*)', FEXT))),
    ('G-CAVEATS-MARKED-EACH', 'every caveat carries a mark',
     13 == len(re.findall(r'(?m)^  \[\s*\d+\] \S+ +(?:TESTED|UNTESTED) ', COMP))),
    ('G-CAVEAT-READS-PRINTED', 'every caveat`s candidate lines printed before the marks',
     13 == READS.count('writer (earliest act naming it)')),

    ('G-P-CONTROL-HOLDS', 'the Reader scored 15 of 15 by the same predicate', '15 of 15' in EXT),
    ('G-P-LIVE-USE-COUNTED', 'members still cited and dropped are both counted',
     'MEMBERS STILL CITED : 15' in FEXT and 'MEMBERS DROPPED : 0' in FEXT),
    ('G-DESERT-CONTROL-FIRST', 'the control is printed before the live count',
     0 < EXT.find('found in the placed Reader (control)') < EXT.find('LIVE DOCUMENTS ASSERTING IT')),
    ('G-CONSTANCE-OWN-WORDS-REPORTED', 'CONSTANCE read in its own words, reported in the bank',
     'the Reader`s wording present verbatim in CONSTANCE : False' in EXT
     and 'CONSTANCE, in its own words' in FBANK),
    ('G-R33-ONE-CLAUSE', 'the head carries four numbered clauses and one added under (R33)',
     4 == len(re.findall(r'(?m)^> \d\.', HEAD_NOW)) and 1 == HEAD_NOW.count('**AND A FOURTH, per (R33)')),
    ('G-R33-SEVEN-NAMED', 'the seven are named in the clause',
     all(re.search(r'\b%d\b' % v, CLAUSE) for v in (43, 59, 67, 73, 83, 89, 97))),
    ('G-R33-PREDICTIONS-CITED', 'the predictions section is cited as naming two of them',
     'predictions section' in CLAUSE and '43 and 67' in CLAUSE),
    ('G-R33-NOT-EXTENDED', 'the clause names no prime beyond the ruling`s seven',
     bool(CLAUSE) and not re.search(r'\b(113|131)\b', CLAUSE)),
    ('G-READER-BODY-BYTE-IDENTICAL', 'the placed body equals the canonical bytes',
     HL > 0 and PB[HL:] == CB),
    ('G-READER-PRIOR-CLAUSES-PRESERVED', 'the head at the starting pin is today`s head less the clause',
     bool(OLDHEAD) and HEAD_NOW.replace(HEAD_NOW[HEAD_NOW.find('>\n> **AND A FOURTH'):
                                                 HEAD_NOW.find('\n---', CL_I)] if CL_I > 0 else '', '', 1)
     == OLDHEAD.rstrip('\n').rsplit('\n---', 1)[0] + OLDHEAD[len(OLDHEAD.rstrip('\n').rsplit('\n---', 1)[0]):]),

    ('G-READING-A-RECOMPUTED', 'reading (a)`s tuples are recomputed',
     'reading (a) tuples : B (3, 2, 2, 0) -> (3, 3, 2, 0) ; D (2, 2, 2, 0) -> (2, 3, 2, 0)' in EXT),
    ('G-READING-A-COLLAPSE-COUNTED', 'distinct tuples under reading (a) are counted',
     'distinct tuples among the four named classes : 4 -> 2' in FCOMP),
    ('G-READING-B-HYPOTHESIS-QUOTED', 'the weakening is quoted from the hypothesis lines',
     'Connected reductive symmetry groups' in COMP and 'with connected reductive symmetry group G' in COMP),
    ('G-N4-DOCS-CLASSIFIED', 'each n4 document is classified by the universality it asserts',
     all(re.search(r'(?m)^  %s +U1 (True|False)' % d, EXT) for d in
         ('MATTER_AS_ARITHMETIC', 'COMPLEX_ANALYSIS', 'BSD_VIA_FORMATION_TRANSFER'))),
    ('G-NEITHER-ADOPTED', 'neither reading is adopted, in the components and the bank',
     'NEITHER READING IS ADOPTED' in FCOMP and 'Neither reading is adopted' in FBANK),
    ('G-SLOTS-FIFTEEN-SEPARATE', 'no sentence of the bank or the closing joins the slots and the fifteen',
     not joined_sentences(BANK) and not joined_sentences(CLOSING)),
    ('G-PRIOR-DEFECTS-ROUTED', 'the four prior defects are routed on the desk',
     all(k in FDESK for k in ('b416’s count of sums', 'b416’s closing row number',
                              'CONSTANCE’s own lattice sentence', 'example systems'))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md equals its blob at the starting pin',
     rb(os.path.join(PP, 'REGISTRY.md')) == blob(PP, PIN_PP, 'REGISTRY.md')),
    ('G-ROWS-BY-MARKER', 'b416`s row is 265 by its marker; this act`s row is 266 by its own',
     ROW416 == [265] and ROW417 == [266]),

    ('G-NOGRADE', 'no grade string is minted by this act`s bank',
     not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged', '0 premises discharged' in FBANK),
    ('G-NODOOR', 'the bank states 0 doors restated', '0 doors restated' in FBANK),
    ('G-NOROUTE', 'the bank states 0 routes proposed', '0 routes proposed' in FBANK),
    ('G-NOKAPPA', 'no kappa value is measured', not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NOCHANNEL', 'no channel is opened by the act`s working tools',
     not re.search(r'\bchannel_open|open_channel\b', ACT_WORK)),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md is not written', 'FACES_LEDGER' not in ACT_WORK),
    ('G-NOFOLD', 'FINDINGS.md is not written', 'FINDINGS' not in ACT_WORK),
    ('G-NORULE', 'STRUCK_CLAUSES is not written', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no deposit action and no Zenodo byte', 'zenodo' not in ACT_WORK.lower()),
    ('G-NOPLATFORM', 'no platform call of any kind', not re.search('urllib|requests|http', ACT_WORK)),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 3),
    ('G-NOORIENTATION-EDIT', 'neither orientation object is written',
     'THE_FINDINGS_AS_THEY_STAND' not in ACT_WORK and 'PATHS_TO_THE_CRITICAL_LINE' not in ACT_WORK),
    ('G-NOLOCKEDFACE', 'no locked face is edited: the seal still verifies', 'SEAL INTACT' in SEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank is opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-6])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry is opened for write',
     not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOCONSTANCE-EDIT', 'CONSTANCE equals its blob at the starting pin',
     rb(os.path.join(PP, 'phase1.5', 'deep-structure', 'CONSTANCE.md'))
     == blob(PP, PIN_PP, 'phase1.5/deep-structure/CONSTANCE.md')),

    ('G-TRAIL-APPEND-ONLY', 'the trail block is appended and the prior mark survives',
     '<!-- b417' in TRAILS and '<!-- b416' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'this act`s row is appended and b416`s survives, both by marker',
     bool(ROW416) and bool(ROW417)),
    ('G-WRITELIST-KINDS', 'the face names 10 kinds',
     10 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
    ('G-NOEXTRAKIND', 'the act wrote exactly the six relay act-tool files the face names',
     6 == len(TOOLS_THIS_ACT)),
    ('G-NOSTAGE-A', 'no working tool of this act stages by -A',
     not re.search('add[^' + chr(92) + 'n]{0,24}-A(?![A-Za-z])', ACT_WORK)),

    ('G-NOBORROWEDBAR', 'no `G-NO*` arm of this suite reads a RAW document text',
     0 == len(_raw_no_arms())),
    ('G-ARMS-DECLARED-EQ-RUN', 'declared on the face equals run here, both ways', None),
    ('G-ARMS-OWN-BANK', 'arms this act builds run over this act`s own bank', bool(BANK) and len(FBANK) > 2000),
    ('G-ARMS-STRIP-PROSE', 'this suite strips comments AND strings, by the tokenizer',
     'def pycode_of' in SELFSRC and 'tokenize' in pycode_of(SELFSRC)),
    ('G-ARMS-FOLD-MARKERS', 'this suite folds markup before matching banked prose',
     'def fold' in SELFSRC and 'fold' in pycode_of(SELFSRC)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'A2: verdicts are read from their own lines',
     'def verdict_line' in SELFSRC and 'verdict_line' in pycode_of(SELFSRC)),
    ('G-NOWRAP-MIDTOKEN', 'the report writers wrap at word boundaries, never by a fixed slice',
     'def wrap(' in COMPSRC and 'def wrap(' in EXTSRC and 'def wrap(' in DESKSRC
     and 0 == len(re.findall(r'\[k:k ?\+ ?\d+\]', pycode_of(COMPSRC + EXTSRC + DESKSRC)))),
    ('G-MUSTFAIL', 'none of the forbidden whole lines is in the bank',
     not any(s in FBANK.lower() for s in (
         'the sentence is wrong', 'the tuples are wrong', 'the species module was pushed',
         'the reader body was edited', 'a grade was moved', 'h2 has moved'))),
]

rule('=')
say('b417_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
rule('=')
say()
declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
passing = failing = 0
say('%-44s %-54s %s' % ('ARM', 'WHAT IT READS', 'VERDICT'))
rule()
for name, desc, res in ARMS:
    if res is None:
        res = (declared == run)
    ok = bool(res)
    passing += 1 if ok else 0
    failing += 0 if ok else 1
    say('  %-42s %-52s %s' % (name, desc[:52], 'PASS' if ok else '### **FAIL**'))
    if not ok:
        say('      ### **FAILING : %s**' % name)
rule()
say()
say('  declared on the face : %d' % len(declared))
say('  run here             : %d' % len(run))
say('  declared but not run : %s' % (sorted(declared - run) or 'none'))
say('  run but not declared : %s' % (sorted(run - declared) or 'none'))
say('  sentences joining the slots and the fifteen -- bank : %s ; closing : %s'
    % (joined_sentences(BANK) or 'none', joined_sentences(CLOSING) or ('none' if CLOSING else '(no closing yet)')))
say()
say('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**' % (len(ARMS), passing, failing))
rule('=')
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
print()
print('wrote %s' % os.path.basename(OUT))
sys.exit(1 if failing else 0)
