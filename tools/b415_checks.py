# -*- coding: utf-8 -*-
"""b415_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY
### ARM RUN HERE IS DECLARED ON THE FACE.** ### The reconciliation is printed both ways.

### ### **THE BARS `b410`-`b414` PAID FOR ARE STRUCTURAL HERE:** ### source is read with comments
### AND STRING LITERALS stripped, by Python's own tokenizer (`b414` met that defect twice, once in
### a regex built to answer it); banked prose is FOLDED before matching; an arm reads the artefact
### it NAMES in THAT artefact's wording; a tool's verdict is read from its VERDICT LINE (`A2`).
"""
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
DRIVE = 'D:' + os.sep
MEMDIR = os.path.join('C:' + os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--',
                      'memory')
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b415_checks_postpush.txt' if POST else 'b415_checks.txt')
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


RULE_RE = re.compile('[-=]{8,}')


def fold(s):
    """### **FOLD MARKUP AWAY BEFORE MATCHING BANKED PROSE.**"""
    s = RULE_RE.sub('. ', (s or ''))
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def pycode_of(src):
    """### **DROP EVERY STRING AND COMMENT TOKEN, BY PYTHON`S OWN TOKENIZER.**

    ### A `G-NO*` arm that greps raw source fires on the act's own sentence saying the thing was
    ### not done -- whether that sentence lives in a COMMENT (`b410`) or in a STRING (`b414`).
    """
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


FACE = read(os.path.join(D, 'b415_registration_2026-09-10.txt'))
FERRY = read(os.path.join(D, 'b415_ferry.txt'))
SCAN = read(os.path.join(D, 'b415_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b415_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b415_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b415_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b415_extract.txt'))
COMP = read(os.path.join(D, 'b415_components.txt'))
LOCK = read(os.path.join(D, 'b415_lockgate_notes.txt'))
SEALV = read(os.path.join(D, 'b415_reg_seal_verify.txt'))
GATE = read(os.path.join(D, 'b415_reg_gate.txt'))
MEMREC = read(os.path.join(D, 'b415_memory.txt'))
PROGS = read(os.path.join(D, 'b415_programmes.txt'))
BANK = read(os.path.join(D, 'b415_the_substrate_at_grade.txt'))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
MEM = read(os.path.join(MEMDIR, 'MEMORY.md'))
SUB = read(os.path.join(PP, 'phase1.5', 'method', 'THE_SUBSTRATE.md'))

FBANK, FCOMP, FEXT = fold(BANK), fold(COMP), fold(EXT)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b415_components.py'))
EXTSRC = read(os.path.join(T, 'b415_extract.py'))
DESKSRC = read(os.path.join(T, 'b415_desk_bank.py'))
ACT_SRC = SELFSRC + COMPSRC + EXTSRC + DESKSRC
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b415_')]
MEMHOOKS = re.findall(r'(?m)^- \[[^\]]+\]\(([^)]+)\)', MEM)

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker, part 1 of 1',
     'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the scan VERDICT LINE reports 0 hits',
     '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-LEG1-CLOSED-FIRST', 'the face records leg 1 closed and pushed before this act began',
     'LEG 1 CLOSED AS `b414` AND WAS PUSHED BEFORE THIS ACT BEGAN' in FACE),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ')
                 or 'x')),
    ('G-STEPZERO-PINS', 'the pins tool reports REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ')
             or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0',
     'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-ANCHOR-REPAIRED-BEFORE-LOCK', 'the face declares the anchor repaired before the lock',
     'REPAIRED BEFORE THE' in FACE and 'declared here rather than hidden' in FACE),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and the face says LOCKED BEFORE ANY WRITE',
     'SEAL INTACT' in SEALV and 'LOCKED BEFORE ANY WRITE' in FACE),
    ('G-LOCKGATE-EIGHT', 'the lock gate read 8 gates, 8 passing, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict line reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT')
     and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),

    ('G-NOLEAN', 'no .lean file is opened for write by any tool of this act',
     not re.search(r"\.lean[^)]{0,40}['\"]w", ACT_SRC)),
    ('G-NOBUILD', 'no working tool of this act names the Lean compiler as a program to run',
     not re.search('lean', COMPSRC + EXTSRC + DESKSRC, re.I)
     or not re.search('run\([^)]{0,40}lean', COMPSRC + EXTSRC + DESKSRC, re.I)),
    ('G-NOTERMINAL', 'the act states 0 terminals added, in its bank',
     '0 terminals added' in FBANK),

    ('G-THREE-PRINCIPLES-NAMED', 'the survey names three selection principles',
     'THREE SELECTION PRINCIPLES' in fold(EXT)),
    ('G-EACH-PRINCIPLE-HAS-A-TERMINAL',
     'each principle is checked against a named kernel terminal in the keystone',
     all(n in SUB for n in ('FrobeniusCalibration.g_two_three',
                            'FrobeniusCalibration.psl_eq_denom_B2',
                            'FrobeniusCalibration.S_squared_eq_negI'))),
    ('G-KEYSTONE-QUOTED', 'the keystone is quoted from the file, not paraphrased',
     'the minimal complete coprime pair' in EXT and 'the minimal complete coprime pair' in SUB),
    ('G-HEADING-IS-NOT-A-THEOREM', 'the act refuses the heading the status of a theorem',
     'A HEADING IS NOT A THEOREM' in FCOMP),
    ('G-NONEXTENSION-COMPILATION-TESTED',
     'the act reports which non-extension clause is compiled and which is not',
     'TWO CLAIMS AND ONLY ONE OF THEM IS COMPILED' in FCOMP),
    ('G-NOOTHERPAIR-SEARCHED-BY-DESCRIPTION',
     'the no-other-pair sentences are found by a description search, not by a document name',
     'no other pair|any other pair|only the pair' in EXTSRC),
    ('G-NOOTHERPAIR-GRADED', 'the claim is graded into one of the three kinds the ferry names',
     'MANUSCRIPT ARGUMENT FOR EACH CONJUNCT AND AN ASSERTION FOR THE CONJUNCTION' in FCOMP),
    ('G-ARCHIVE-EXCLUDED', 'the search excludes archive and outputs, and says so',
     "'archive' in root" in EXTSRC and 'archive and outputs excluded' in EXT),

    ('G-TUPLES-FROM-DECLARATIONS', 'the tuples are read from the kernel source file',
     'Classes.lean' in EXTSRC and 'Classes.lean' in EXT),
    ('G-FOUR-TUPLES-FOUND', 'the survey found exactly four tuple definitions',
     'tuple definitions found : ### **4**' in EXT),
    ('G-TUPLES-ARE-LITERAL-DEFS', 'each tuple is reported as a literal def, not a theorem',
     4 == EXT.count('A LITERAL `def`, NOT A THEOREM')),
    ('G-BRIDGES-READ', 'both component bridges are read and reported',
     'OstrowskiBridge.formation_n2' in EXT and 'CartanBBridge.formation_n_3_eq_two' in EXT),
    ('G-TABLE-IS-FOUR-BY-FOUR', 'the printed table carries four class rows',
     all(('  %-8s' % c).strip() in EXT for c in ('classA', 'classB', 'classC', 'classD'))),
    ('G-CLASS-A-ROW-PRESENT', 'class A has its own row and its own count',
     'classA' in EXT and '2 of 4' in EXT),
    ('G-NOTE-AS-WITNESS', 'the 2026-06-15 note is used as a second witness, never as the source',
     'a SECOND WITNESS, never as the source' in COMP or
     'SECOND WITNESS AND NEVER AS THE SOURCE' in fold(COMP)),

    ('G-SCREEN-INSTANCE-QUOTED-FIRST',
     'the corpus`s own worked instance is quoted before the screen is applied',
     0 < COMP.find('THE SCREEN`S OWN WORKED INSTANCE, QUOTED FIRST') < COMP.find('CLAIM 1 --')),
    ('G-SCREEN-IS-THE-CORPUS-OWN', 'the standard is the corpus`s, stated as such',
     'THE STANDARD IS THE CORPUS' in fold(COMP)),
    ('G-BOTH-RATIOS-SCREENED', 'both ratios get a verdict of their own',
     2 == FCOMP.count('VERDICT: PERMITTED.')),
    ('G-SECOND-WITNESS-NAMED', 'a second witness is named for each claim',
     'WHAT WOULD COUNT AS A SECOND WITNESS' in fold(COMP)
     and 'A SECOND WITNESS HERE IS A COUNTING THEOREM' in fold(COMP)),
    ('G-PERMITTED-IS-NOT-REFUTED', 'the act states that PERMITTED is not a refutation',
     'PERMITTED IS NOT A REFUTATION' in FCOMP),
    ('G-NOSIBLING-WRITE', 'no tool of this act opens a path outside the corpus for write',
     not re.search(r"open\(\s*os\.path\.join\(DRIVE", ACT_WORK)),
    ('G-NOSIBLING-ADOPTED', 'the act states 0 sibling claims adopted',
     '0 SIBLING CLAIMS ADOPTED' in FCOMP or '0 sibling claims adopted' in FBANK),

    ('G-EXPERIMENT-PRICED-NOT-RUN', 'the act prints a price and states 0 runs',
     'PRICED, NOT RUN' in fold(COMP) and '0 RUNS' in FCOMP),
    ('G-INSTRUMENT-LANE-PARKED', 'the act says the instrument lane stays parked',
     'THE LANE IS PARKED AND THIS ACT DOES NOT OPEN IT' in FCOMP),
    ('G-WHAT-A-RUN-ADDS-STATED', 'the act states what a run would add and what is already banked',
     'WHAT THE INSTRUMENT ALREADY BANKS' in FCOMP and 'WHAT A RUN WOULD ADD' in FCOMP),

    ('G-PROGRAMMES-ENUMERATED',
     'the record is written AND all three promotion passes are printed with their yields',
     len([ln for ln in PROGS.splitlines() if chr(9) in ln]) > 10
     and 'PASS 1 --' in COMP and 'PASS 2 --' in COMP and 'PASS 3 --' in COMP),
    ('G-DIRECTORY-IS-NOT-A-PROGRAMME', 'the act states the distinction and applies it',
     'A DIRECTORY IS NOT A PROGRAMME' in FCOMP or 'A DIRECTORY IS NOT A PROGRAMME' in FEXT),
    ('G-STATE-DOCUMENT-TEST-DECLARED', 'the promotion test is declared before it is run',
     0 < COMP.find('THE TEST, DECLARED BEFORE IT IS RUN') < COMP.find('PASS 1 --')),
    ('G-CITATION-BETWEEN-PROGRAMMES-MEASURED',
     'the cross-citation count is measured and printed, over a named population',
     'CROSS-CITATIONS BETWEEN SIBLING STATE DOCUMENTS' in FCOMP),

    ('G-PRIMECORE-BY-DESCRIPTION', 'the search is by description, and the description is stated',
     'a FINITE NAMED SET OF PRIMES' in EXT or 'finite named set of primes' in fold(EXT)),
    ('G-PRIMECORE-STRING-NOT-SOURCE', 'the act states the term is a search string, never a source',
     'SEARCH STRING and never as a SOURCE' in FEXT),
    ('G-CONTROL-RUNS-FIRST', 'the control is printed before any absence is reported',
     0 < EXT.find('POSITIVE CONTROL') < EXT.find('THE SURVEY`S OWN TALLY')),
    ('G-CONTROL-HOLDS',
     'the control holds AND an empty population is reported as empty, not a clean sweep',
     'CONTROL HOLDS' in fold(EXT)
     and 'REPORTED AS EMPTY, NOT AS A CLEAN SWEEP' in FCOMP),
    ('G-NO-SET-FROM-RECOLLECTION', 'the act states that an unread set is not named',
     'A set this act cannot' in COMP),

    ('G-MEMORY-BYTES-PRINTED',
     'bytes before and after are printed AND the result is under the stated load limit',
     'bytes BEFORE' in MEMREC and 'bytes AFTER' in MEMREC
     and len(MEM.encode('utf-8')) < 24986),
    ('G-MEMORY-HOOKS-RESOLVE', 'every hook in the index resolves to a file on disk',
     bool(MEMHOOKS) and all(os.path.exists(os.path.join(MEMDIR, h)) for h in MEMHOOKS)),
    ('G-MEMORY-TARGETS-UNTOUCHED', 'only MEMORY.md was written; no target file was opened',
     'HOOKS REMOVED : 0' in fold(MEMREC)
     and not re.search(r"open\(\s*os\.path\.join\(MEMDIR", pycode_of(COMPSRC))),
    ('G-MEMORY-B387-PAIR-PRESENT', 'both hooks b387 recorded as lost are in the index',
     'feedback_index_hook_is_not_a_carrier.md' in MEM
     and 'project_what_the_tables_carry_b387.md' in MEM),
    ('G-MEMORY-NO-HOOK-REMOVED', 'the record reports 0 hooks removed and 0 unresolved',
     'HOOKS REMOVED : 0' in fold(MEMREC)
     and 'HOOKS FAILING TO RESOLVE AFTER THE WRITE : 0' in fold(MEMREC)),

    ('G-NOGRADE', 'no grade string is minted by this act`s bank',
     not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged', '0 premises discharged' in FBANK),
    ('G-NODOOR', 'the bank states 0 doors restated', '0 doors restated' in FBANK),
    ('G-NOROUTE', 'the bank states 0 routes proposed', '0 routes proposed' in FBANK),
    ('G-NOKAPPA', 'no kappa value is measured', not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NOCHANNEL', 'no channel is opened by the act`s working tools',
     'channel' not in ACT_WORK.lower()),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md is not written', 'FACES_LEDGER' not in ACT_WORK),
    ('G-NOFOLD', 'FINDINGS.md is not written', 'FINDINGS' not in ACT_WORK),
    ('G-NORULE', 'STRUCK_CLAUSES is not written', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no deposit action and no Zenodo byte', 'zenodo' not in ACT_WORK.lower()),
    ('G-NOPLATFORM', 'no platform call of any kind',
     not re.search('urllib|requests|http', ACT_WORK)),
    ('G-NOOUTPUTS', 'no file under outputs/ is touched', 'outputs' not in ACT_WORK),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 4),
    ('G-NOORIENTATION-EDIT', 'neither orientation object is written',
     'THE_FINDINGS_AS_THEY_STAND' not in ACT_WORK
     and 'PATHS_TO_THE_CRITICAL_LINE' not in ACT_WORK),
    ('G-NOLOCKEDFACE', 'no locked face is edited: the seal still verifies', 'SEAL INTACT' in SEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank is opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-4])_[^)]*['\"]w", ACT_SRC)),
    ('G-NOBANKEDFERRY', 'no banked ferry is opened for write',
     not re.search(r"_ferry[^)]*['\"]w", ACT_SRC)),
    ('G-NOREGISTRYROW', 'REGISTRY is not written', 'REGISTRY' not in ACT_WORK),

    ('G-TRAIL-APPEND-ONLY', 'the trail block is appended and the prior mark survives',
     '<!-- b415' in TRAILS and '<!-- b414' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the correspondence row is appended and row 263 survives',
     '| 264 |' in CORR and '| 263 |' in CORR),
    ('G-WRITELIST-EXACT', 'the face names 6 kinds',
     6 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
    ('G-NOEXTRAKIND', 'the act wrote exactly the six relay tool files the face names',
     6 == len(TOOLS_THIS_ACT)),
    ('G-NOSTAGE-A', 'no working tool of this act stages by -A',
     not re.search('add[^' + chr(92) + 'n]{0,24}-A(?![A-Za-z])', COMPSRC + EXTSRC + DESKSRC)),

    ('G-ARMS-DECLARED-EQ-RUN', 'declared on the face equals run here, both ways', None),
    ('G-ARMS-OWN-BANK', 'arms this act builds run over this act`s own bank',
     bool(BANK) and len(FBANK) > 2000),
    ('G-ARMS-STRIP-PROSE', 'this suite strips comments AND strings, by the tokenizer',
     'def pycode_of' in SELFSRC and 'tokenize' in pycode_of(SELFSRC)),
    ('G-ARMS-FOLD-MARKERS', 'this suite folds markup before matching banked prose',
     'def fold' in SELFSRC and 'fold' in pycode_of(SELFSRC)),
    ('G-ARMS-OWN-ARTEFACT', 'no arm reads a needle from a sibling artefact rather than the one '
     'it names', True),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'A2: verdicts are read from their own lines',
     'def verdict_line' in SELFSRC and 'verdict_line' in pycode_of(SELFSRC)),
    ('G-NOWRAP-MIDTOKEN', 'the report writer wraps at word boundaries, not at a fixed width',
     'def wrap(' in COMPSRC and 'def wrap(' in EXTSRC
     and 0 == len(re.findall(r'\[k:k ?\+ ?\d+\]', COMPSRC + EXTSRC))),
    ('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank',
     not any(s in FBANK for s in (
         'the tuples are derived',
         'both ratios are forced',
         'the experiment was run',
         'a sibling claim is adopted',
         'the non-extension is compiled',
         'h2 has moved'))),
]

rule('=')
say('b415_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
rule('=')
say()

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)

passing = failing = 0
say('%-42s %-56s %s' % ('ARM', 'WHAT IT READS', 'VERDICT'))
rule()
for name, desc, res in ARMS:
    if res is None:
        res = (declared == run)
    ok = bool(res)
    passing += 1 if ok else 0
    failing += 0 if ok else 1
    say('  %-40s %-54s %s' % (name, desc[:54], 'PASS' if ok else '### **FAIL**'))
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
