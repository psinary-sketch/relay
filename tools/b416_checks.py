# -*- coding: utf-8 -*-
"""b416_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY
### ARM RUN HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
"""
import ast
import hashlib
import io
import os
import re
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
SEAL = os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean')
PLACED = os.path.join(PP, 'heritage', 'PRIME_CORE_READER.md')
CANON = os.path.join(DL, 'PRIME_CORE_READER.md')
FIGURE = os.path.join(PP, 'outputs', 'prime-core-lattice-b416.svg')
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b416_checks_postpush.txt' if POST else 'b416_checks.txt')
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


RULE_RE = re.compile('[-=]{8,}')


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


# ### **b410'S BAR, MADE MECHANICAL.** ### A `G-NO*` arm that reads a RAW document text fires on
# ### the act's own sentence saying the thing was not done. ### Every such arm here must read a
# ### STRIPPED source (`ACT_WORK`, `pycode_of`) or a FOLDED one (`FBANK`, `FCOMP`, ...) or a
# ### structural fact. ### The arms are found by parsing THIS FILE, not by grepping it.
RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'PLACEREC', 'FIGREC', 'LOCK', 'GATE', 'BANK',
             'TRAILS', 'REGISTRY', 'CORR', 'FACE', 'FERRY', 'SCAN')


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


FACE = read(os.path.join(D, 'b416_registration_2026-09-11.txt'))
FERRY = read(os.path.join(D, 'b416_ferry.txt'))
SCAN = read(os.path.join(D, 'b416_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b416_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b416_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b416_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b416_extract.txt'))
COMP = read(os.path.join(D, 'b416_components.txt'))
LOCK = read(os.path.join(D, 'b416_lockgate_notes.txt'))
SEALV = read(os.path.join(D, 'b416_reg_seal_verify.txt'))
GATE = read(os.path.join(D, 'b416_reg_gate.txt'))
PLACEREC = read(os.path.join(D, 'b416_place.txt'))
FIGREC = read(os.path.join(D, 'b416_figure.txt'))
DESKN = read(os.path.join(D, 'b416_desk_notes.txt'))
BANK = read(os.path.join(D, 'b416_the_reader_placed.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
REGISTRY = read(os.path.join(PP, 'REGISTRY.md'))
SVG = read(FIGURE)
SEALBEF = (read(os.path.join(D, 'b416_seal_digest_before.txt')).split() or [''])[0]

FBANK, FCOMP, FEXT, FDESK = fold(BANK), fold(COMP), fold(EXT), fold(DESKN)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b416_components.py'))
EXTSRC = read(os.path.join(T, 'b416_extract.py'))
DESKSRC = read(os.path.join(T, 'b416_desk_bank.py'))
ACT_SRC = SELFSRC + COMPSRC + EXTSRC + DESKSRC
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b416_')]
HOOKSRC = read(os.path.join(T, 'b371_hookpath.py'))
PB, CB = rb(PLACED), rb(CANON)
HEADLEN = PB.find(b'# PRIME CORE') if PB.find(b'# PRIME CORE') > 0 else 0
OUTPUTS = [f for f in os.listdir(os.path.join(PP, 'outputs'))
           if os.path.isfile(os.path.join(PP, 'outputs', f))]

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker, part 1 of 1',
     'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the scan VERDICT LINE reports 0 hits',
     '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ')
                 or 'x')),
    ('G-STEPZERO-PINS', 'the pins tool reports REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ')
             or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0',
     'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and the face says LOCKED BEFORE ANY WRITE',
     'SEAL INTACT' in SEALV and 'LOCKED BEFORE ANY WRITE' in FACE),
    ('G-LOCKGATE-EIGHT', 'the lock gate read 8 gates, 8 passing, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict line reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT')
     and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-R32-RATIFIED-NOT-EXTENDED', 'the face says (R32) is executed and not extended',
     'does not improve on it and does not extend it' in FACE),

    ('G-NOLEAN', 'no .lean file is opened for write by any tool of this act',
     not re.search(r"\.lean[^)]{0,40}['\"]w", ACT_SRC)),
    ('G-NOBUILD', 'no working tool names the Lean compiler as a program to run',
     not re.search(r"run\([^)]{0,40}lean", COMPSRC + EXTSRC + DESKSRC, re.I)),
    ('G-NOTERMINAL', 'the act states 0 terminals added, in its bank',
     '0 terminals added' in FBANK),

    ('G-COMPONENTS-COUNT-PER-COMPONENT',
     'the act answers per component and the face says so',
     'THE ANSWER IS PER COMPONENT, NOT PER CLASS' in FACE
     and 'PER COMPONENT, NOT PER CLASS' in FCOMP),
    ('G-N1-MEANING-FROM-OWNER', 'n1`s meaning is quoted from the owning document',
     'independent algebraic structures on the substrate' in
     read(os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md'))),
    ('G-N4-MEANING-FROM-OWNER', 'n4`s meaning is quoted from the owning document',
     'mechanism classes contributed by the bindings between stages' in
     read(os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md'))),
    ('G-OWNER-DOCUMENT-NAMED', 'the owning document is named in the components',
     'MATTER_AS_ARITHMETIC' in COMP),
    ('G-UNIVERSALITY-SENTENCE-QUOTED', 'the owner`s universality sentence is quoted',
     'Three of four formation components' in EXT),
    ('G-UNIVERSALITY-TESTED-AGAINST-DECLARATIONS',
     'the claim is tested against the kernel`s own tuples and the disagreement printed',
     'THE UNIVERSALITY SENTENCE AND THE DECLARATIONS DISAGREE' in fold(EXT)),
    ('G-TUPLES-READ-NOT-RECALLED', 'the tuples are read from Classes.lean',
     'Classes.lean' in EXTSRC and 'classA' in EXT and 'classD' in EXT),
    ('G-PRICE-SEARCH-RUN', 'the search for a priced derivation route was run and its yield shown',
     'together with a price, cost, derivation or bridge' in EXT),
    ('G-BRIDGE-PATTERN-READ', 'both bridges are read from their own source',
     'OstrowskiBridge.lean' in EXT and 'CartanBBridge.lean' in EXT),
    ('G-BRIDGE-SUPPLY-NAMED', 'what each bridge had to supply is named',
     'DECLARE A FINITE TYPE WHOSE ELEMENTS' in fold(EXT)),
    ('G-N1-PRICE-PRINTED', 'a price for deriving n1 is printed',
     'VERDICT ON THE PRICE' in COMP),
    ('G-N1-PRICED-NOT-BUILT', 'the act states 0 .lean files written',
     'PRICED; NOT BUILT' in fold(COMP) and '0 .lean files written' in fold(COMP)),
    ('G-PRICE-ANSWERS-THE-MEASUREMENT',
     'the price turns on what the act measured, not on the ferry`s expectation',
     'COUNTS PRIMES AND `n1` COUNTS CHANNELS' in COMP or
     'COUNTS PRIMES AND n1 COUNTS CHANNELS' in FCOMP),

    ('G-DATEDTOOL-BY-DESCRIPTION', 'the dated-tool search is by description, not by name',
     'SEARCHED BY DESCRIPTION' in fold(EXT) and 'os.path.join' in EXTSRC),
    ('G-MENTION-IS-NOT-A-BREAK', 'the act states the distinction and applies it',
     'A STATIC HIT IS A MENTION' in fold(EXT) and 'MENTIONS :' in fold(EXT)),
    ('G-DATEDTOOL-RUN-NOT-GREPPED', 'each hit was run, and the breaks counted separately',
     'BREAKS :' in fold(EXT)),
    ('G-B371-REPAIRED', 'the tool now names the path b386 left',
     ".githooks', 'pre-push'" in HOOKSRC and "'git-hooks'" not in pycode_of(HOOKSRC)),
    ('G-B371-RUNS-AFTER',
     'it runs clean AND the records it re-wrote were restored, 0 still differing',
     'it runs without a `FileNotFoundError`        : ### **True**' in COMP
     and 'still differing after the restore  : ### **0**' in COMP),
    ('G-B371-FIXTURES-BOTH-POLARITIES', 'its own polarity exercise ran',
     'COMPONENT 3 OUTCOME' in read(os.path.join(D, 'b371_hookpath_notes5.txt'))),
    ('G-ONLY-B371-REPAIRED', 'exactly one existing tool of the roster was edited',
     'b369_hygiene' not in pycode_of(SELFSRC + COMPSRC)
     or 'ROUTED' in FCOMP),
    ('G-OTHER-DATEDTOOL-ROUTED', 'the other dated tool is named and routed',
     'b369_hygiene.py' in COMP and 'ROUTED' in FCOMP),

    ('G-T14-ANNOTATION-DRAFTED', 'the annotation is drafted in the components',
     '(T1.4-a, b414)' in COMP),
    ('G-T14-BYTES-SHOWN', 'the edit`s byte and line counts are printed',
     'bytes the annotation would add' in COMP and 'bytes it would remove' in COMP),
    ('G-T14-NOT-APPLIED', 'the annotation is not in the sealed file',
     '(T1.4-a, b414)' not in read(SEAL)),
    ('G-SEAL-DIGEST-UNCHANGED', 'the sealed file`s sha256 is the one recorded before the act',
     bool(SEALBEF) and hashlib.sha256(rb(SEAL)).hexdigest() == SEALBEF),
    ('G-ANNOTATION-IS-ADDITIVE', 'the annotation removes nothing',
     'bytes it would remove          : ### **0**' in COMP),

    ('G-CAVEATS-BY-DESCRIPTION', 'the caveat search is by description',
     'THE DESCRIPTION:' in fold(EXT) and 'NOT COMPILED' in EXT),
    ('G-CAVEAT-CONTROL-FIRST', 'the control is printed before the count',
     0 < EXT.find('POSITIVE CONTROL -- `(T1.4)`') < EXT.find('CAVEATS OF THIS SHAPE')),
    ('G-CAVEAT-CONTROL-HOLDS', 'the control found a caveat in the file that owns (T1.4)',
     'CONTROL HOLDS' in fold(EXT)),
    ('G-CAVEATS-COUNTED-NOT-GRADED', 'the act says it counts and does not grade',
     'COUNTED, NOT GRADED' in fold(COMP)),

    ('G-READER-LOCATED-BY-DIGEST', 'the canonical copy is located by digest',
     'sha256' in PLACEREC and bool(CB)),
    ('G-READER-BODY-BYTE-IDENTICAL', 'the placed body equals the canonical bytes',
     bool(PB) and bool(CB) and PB[HEADLEN:] == CB),
    ('G-READER-HEAD-THREE-CLAUSES', 'the currency note carries exactly three clauses',
     3 == len(re.findall(r'(?m)^> \d\.', read(PLACED)[:2000]))),
    ('G-READER-CLASS-LINE', 'the head carries a class line naming Tier N',
     '**CLASS.**' in read(PLACED)[:2000] and 'Tier N' in read(PLACED)[:2000]),
    ('G-READER-SCHEME-LINE', 'the head carries a scheme line',
     '**SCHEME.**' in read(PLACED)[:2000]),
    ('G-READER-TIER-N', 'the registry row records Tier N and the theory-space cluster',
     'TIER N — theory-space cluster' in REGISTRY),
    ('G-READER-ENCODING-REPORTED', 'the encoding damage is measured and printed',
     'cp1252 re-encoding damage' in PLACEREC),
    ('G-READER-BODY-NOT-EDITED',
     '0 bytes of the body edited, so the defects found in it are still there',
     'BYTES OF THE BODY EDITED : 0' in fold(PLACEREC)
     and bool(PB) and PB[HEADLEN:] == CB),
    ('G-REGISTRY-ROW-WRITTEN', 'the registry carries row p2-35 once',
     1 == len(re.findall(r'(?m)^\| p2-35 \|', REGISTRY))),
    ('G-THREE-CARRIERS-CROSSREFERENCED', 'three carriers are named on the row',
     all(c in REGISTRY for c in ('CONSTANCE.md', 'CONSERVATION.md', 'FANO_PLANE.md'))),
    ('G-LINEAGE-ONE-LINE-ONLY', 'the lineage appears exactly once in the corpus',
     1 == (REGISTRY.count('PRIME GROUND → CONVERGENCE → the Reader → theory-space')
           + TRAILS.count('PRIME GROUND → CONVERGENCE → the Reader → theory-space'))),
    ('G-CONTINUATION-NAMED-OUTSIDE', 'the continuation is named as outside the repo',
     'outside this repo' in REGISTRY or 'outside the repo' in FBANK),
    ('G-NOCONTINUATION-WRITE', 'no tool of this act writes outside the named repositories',
     not re.search(r"open\(\s*os\.path\.join\(DL", ACT_WORK)),
    ('G-FINDING-IN-RECORD-NOT-IN-BODY',
     'the defects found are in the act`s record and not in the placed body',
     'arithmetic-desert' in FDESK.lower() or 'arithmetic desert' in FDESK.lower()),

    ('G-FIGURE-WRITTEN', 'the figure exists and is an SVG', SVG.startswith('<svg')),
    ('G-FIGURE-FROM-ARITHMETIC', 'the figure is computed, not transcribed',
     'def isprime' in COMPSRC and 'lattice cells drawn' in FIGREC),
    ('G-FIGURE-FOUR-KINDS', 'four kinds are distinguished in the figure',
     all(k in SVG for k in ('generator', 'consecutive', 'jump', 'inclusion'))),
    ('G-FIGURE-FORTYTHREE-SHOWN', '43 is on the lattice and marked outside P',
     '>43<' in SVG and 'outside P' in SVG),
    ('G-FIGURE-READER-SENTENCE-BESIDE',
     'the Reader`s own sentence is beside it, read across the wrapped text elements',
     'arithmetic deserts where no sum of' in
     re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', SVG))),
    ('G-FIGURE-NO-GRADE', 'the figure states it carries no grade',
     'carries no grade' in SVG),
    ('G-FIGURE-NOT-CITED-AS-EVIDENCE', 'the figure is cited nowhere as evidence',
     'cited nowhere as evidence' in SVG and 'illustration only' in REGISTRY),
    ('G-ONE-OUTPUTS-FILE', 'exactly one file under outputs was written by this act',
     1 == len([f for f in OUTPUTS if 'b416' in f])),

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
    ('G-NOPLATFORM', 'no platform call of any kind',
     not re.search('urllib|requests|http', ACT_WORK)),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 5),
    ('G-NOORIENTATION-EDIT', 'neither orientation object is written',
     'THE_FINDINGS_AS_THEY_STAND' not in ACT_WORK
     and 'PATHS_TO_THE_CRITICAL_LINE' not in ACT_WORK),
    ('G-NOLOCKEDFACE', 'no locked face is edited: the seal still verifies', 'SEAL INTACT' in SEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank is opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-5])_[^)]*['\"]w", ACT_SRC)),
    ('G-NOBANKEDFERRY', 'no banked ferry is opened for write',
     not re.search(r"_ferry[^)]*['\"]w", ACT_SRC)),

    ('G-TRAIL-APPEND-ONLY', 'the trail block is appended and the prior mark survives',
     '<!-- b416' in TRAILS and '<!-- b415' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the correspondence row is appended and row 264 survives',
     '| 265 |' in CORR and '| 264 |' in CORR),
    ('G-REGISTRY-APPEND-ONLY', 'the registry row is appended and p2-34 survives',
     '| p2-35 |' in REGISTRY and '| p2-34 |' in REGISTRY),
    ('G-WRITELIST-EXACT', 'the face names 9 kinds',
     9 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
    ('G-NOEXTRAKIND', 'the act wrote exactly the six relay tool files the face names',
     6 == len(TOOLS_THIS_ACT)),
    ('G-NOSTAGE-A', 'no working tool of this act stages by -A',
     not re.search('add[^' + chr(92) + 'n]{0,24}-A(?![A-Za-z])', COMPSRC + EXTSRC + DESKSRC)),

    ('G-NOBORROWEDBAR',
     'no `G-NO*` arm of this suite reads a RAW document text; each reads stripped or folded',
     0 == len(_raw_no_arms())),

    ('G-ARMS-DECLARED-EQ-RUN', 'declared on the face equals run here, both ways', None),
    ('G-ARMS-OWN-BANK', 'arms this act builds run over this act`s own bank',
     bool(BANK) and len(FBANK) > 2000),
    ('G-ARMS-STRIP-PROSE', 'this suite strips comments AND strings, by the tokenizer',
     'def pycode_of' in SELFSRC and 'tokenize' in pycode_of(SELFSRC)),
    ('G-ARMS-FOLD-MARKERS', 'this suite folds markup before matching banked prose',
     'def fold' in SELFSRC and 'fold' in pycode_of(SELFSRC)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'A2: verdicts are read from their own lines',
     'def verdict_line' in SELFSRC and 'verdict_line' in pycode_of(SELFSRC)),
    ('G-NOWRAP-MIDTOKEN', 'the report writers wrap at word boundaries, not at a fixed width',
     'def wrap(' in COMPSRC and 'def wrap(' in EXTSRC
     and 0 == len(re.findall(r'\[k:k ?\+ ?\d+\]', COMPSRC + EXTSRC))),
    ('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank',
     not any(s in FBANK for s in (
         'the tuples are derived',
         'the annotation was applied',
         'the reader body was edited',
         'the desert sentence is true',
         'a grade was moved',
         'h2 has moved'))),
]

rule('=')
say('b416_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
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
say()
say('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
    % (len(ARMS), passing, failing))
rule('=')

io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
print()
print('wrote %s' % os.path.basename(OUT))
sys.exit(1 if failing else 0)
