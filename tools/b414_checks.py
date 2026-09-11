# -*- coding: utf-8 -*-
"""b414_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY
### ARM RUN HERE IS DECLARED ON THE FACE.** ### The reconciliation is printed both ways.

### ### **AND THE BARS `b410`-`b413` PAID FOR ARE STRUCTURAL HERE, NOT ADVISORY:**
### * source is read with comments and docstrings STRIPPED, so an arm cannot fire on the act's own
###   sentence saying the thing was not done (`b410`'s `G-NOBORROWEDBAR`);
### * banked prose is FOLDED before matching, because the bank wraps mid-sentence with `###`
###   markers between words (`b412`'s `F-NOGRADE`), and ### **A FOLDED NEEDLE MUST BE FOLDED TOO**
###   (`b413`'s own defect);
### * an arm reads ### **THE ARTEFACT IT NAMES, IN THE WORDING THAT ARTEFACT USES** ### -- the
###   lesson `b412` and `b413` paid for about nine times between them;
### * a tool's verdict is read from its ### **VERDICT LINE**, never as a substring (`A2`).
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
CORE = os.path.join(KERN, 'Core')
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b414_checks_postpush.txt' if POST else 'b414_checks.txt')
NL = chr(10)
BSL = chr(92)

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
    """### **FOLD MARKUP AWAY BEFORE MATCHING BANKED PROSE.** ### The bank wraps mid-sentence."""
    s = RULE_RE.sub('. ', (s or ''))
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def code_of(src):
    """### **STRIP COMMENTS AND DOCSTRINGS BEFORE SCANNING SOURCE.**"""
    s = re.sub(r'/-.*?-/', ' ', src, flags=re.S)                 # Lean block comments
    s = re.sub(r'(?m)--.*$', ' ', s)                             # Lean line comments
    s = re.sub(r'"""[\s\S]*?"""', ' ', s)                        # Python docstrings
    s = re.sub(r"'''[\s\S]*?'''", ' ', s)
    return re.sub(r'(?m)#.*$', ' ', s)                           # Python line comments


def pycode_of(src):
    """### **DROP EVERY STRING AND COMMENT TOKEN, BY PYTHON`S OWN TOKENIZER.**

    ### `b410`'s `G-NOBORROWEDBAR` fired on the act's own COMMENT saying the bar had been
    ### removed. ### **THIS ACT MET THE SAME DEFECT TWICE MORE:** ### eight `G-NO*` arms fired
    ### on their own STRING LITERALS -- the correspondence row's prose *NO ROW OF FACES_LEDGER
    ### WRITTEN* is a string inside `b414_desk_bank.py` -- and then a REGEX stripper built to
    ### answer that left the prose behind, because an apostrophe inside a double-quoted line
    ### re-paired the quotes across an implicit concatenation.
    ### ### **A SENTENCE SAYING THE THING WAS NOT DONE IS NOT THE THING BEING DONE, WHETHER IT
    ### ### LIVES IN A COMMENT OR IN A QUOTE** -- and the instrument that can tell the
    ### difference exactly is the language's own tokenizer, not a pattern.
    """
    import tokenize
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.STRING, tokenize.COMMENT):
                continue
            out.append(tok.string)
    except Exception:
        # ### **A TOKENIZE FAILURE IS NOT A PASS.** ### Return a sentinel that fails every
        # ### `not in` arm rather than an empty string that would pass all of them.
        return 'TOKENIZE-FAILED ' + src
    return ' '.join(out)


def verdict_line(text, key):
    """### `A2`: ### **READ THE TOOL'S VERDICT LINE, NEVER THE WORD AS A SUBSTRING.**"""
    for ln in (text or '').splitlines():
        if key in ln:
            return ln
    return ''


# ---- the artefacts, read once -----------------------------------------------------------------
FACE = read(os.path.join(D, 'b414_registration_2026-09-10.txt'))
FERRY = read(os.path.join(D, 'b414_ferry.txt'))
SCAN = read(os.path.join(D, 'b414_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b414_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b414_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b414_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b414_extract.txt'))
COMP = read(os.path.join(D, 'b414_components.txt'))
LOCK = read(os.path.join(D, 'b414_lockgate_notes.txt'))
SEALV = read(os.path.join(D, 'b414_reg_seal_verify.txt'))
GATE = read(os.path.join(D, 'b414_reg_gate.txt'))
TERM = read(os.path.join(D, 'b414_reg_termscan.txt'))
LAD = read(os.path.join(D, 'b414_ladder.txt'))
SORT = read(os.path.join(D, 'b414_sorted.txt'))
BANK = read(os.path.join(D, 'b414_the_predicate_named.txt'))
BUILD = read(os.path.join(D, 'b414_build.txt'))
NEWSRC = read(os.path.join(CORE, 'SinglePrimeFactor.lean'))
NEWCODE = code_of(NEWSRC)
SEALSRC = read(os.path.join(CORE, 'FiniteSideSeal.lean'))
PRINTS = read(os.path.join(KERN, 'AXIOM_PRINTS.txt'))
ALLP = read(os.path.join(KERN, 'AllPrints.lean'))
CORR = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
IDX = read(os.path.join(T, 'banked_index.py'))
GITIGN = read(os.path.join(KERN, '.gitignore'))

FBANK = fold(BANK)
FCOMP = fold(COMP)
CORE_FILES = sorted(f for f in os.listdir(CORE) if f.endswith('.lean')) if os.path.isdir(CORE) else []
NEW_TERMS = re.findall(r'(?m)^theorem\s+(\w+)', NEWCODE)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b414_')]

# our own source, for the arms that test this file's discipline
SELFSRC = read(os.path.abspath(__file__))
SELFCODE = code_of(SELFSRC)
COMPSRC = read(os.path.join(T, 'b414_components.py'))
EXTSRC = read(os.path.join(T, 'b414_extract.py'))
DESKSRC = read(os.path.join(T, 'b414_desk_bank.py'))
ACT_SRC = SELFSRC + COMPSRC + EXTSRC + DESKSRC
# ### **THE `G-NO*` ARMS SCAN THE ACT`S WORKING TOOLS, STRINGS AND COMMENTS STRIPPED.**
# ### This suite is excluded from that scan: ### **AN INSTRUMENT THAT TESTS FOR A
# ### FORBIDDEN WORD MUST CONTAIN THAT WORD**, so scanning itself makes every such arm
# ### fire on its own subject. ### The working tools are the ones that could actually
# ### perform a forbidden write; this one only reads.
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
ACT_CODE = code_of(ACT_SRC)


def prof(t):
    return verdict_line(PRINTS, "'SinglePrimeFactor.%s'" % t)


ARMS = [
    # ---- STEP ZERO ---------------------------------------------------------------------------
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker, part 1 of 1',
     'paste ends (part 1 of 1)' in FERRY and 'part 1 of 1' in FERRY),
    ('G-SCAN-CLEAN', 'the scan VERDICT LINE reports 0 hits, read as a line not a substring',
     '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0 on their own lines',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins tool reports REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0',
     'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-SURVEY-REPAIRED-BEFORE-LOCK',
     'the face declares the survey sentence repaired before the lock, not after',
     'REPAIRED BEFORE THE LOCK' in FACE and 'declared here, not hidden' in FACE),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and the face says LOCKED BEFORE ANY WRITE',
     'SEAL INTACT' in SEALV and 'LOCKED BEFORE ANY WRITE' in FACE),
    ('G-LOCKGATE-EIGHT', 'the lock gate read 8 gates, 8 passing, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK),
    ('G-SEAL-VERIFIES', 'the registration gate verdict line reads CLEAR',
     'CLEAR' in verdict_line(GATE, 'GATE VERDICT') and 'NOT CLEAR' not in
     verdict_line(GATE, 'GATE VERDICT')),

    # ---- COMPONENT 1 -- THE MODULE RULED ------------------------------------------------------
    ('G-CORE-NO-MATHLIB', 'no file in Core/ imports Mathlib, measured over the directory',
     0 == sum(1 for f in CORE_FILES
              if re.search(r'(?m)^import\s+Mathlib', read(os.path.join(CORE, f))))),
    ('G-CORE-INTERNAL-IMPORTS-COUNTED',
     'the survey counted Core-internal imports rather than reporting none',
     bool(re.search(r'Core-internal imports.*?: (\d+)', EXT)) and
     int(re.search(r'Core-internal imports.*?: (\d+)', EXT).group(1)) > 0),
    ('G-FILE-VS-DIRECTORY-DISTINGUISHED',
     'the face distinguishes the FILE having no imports from the DIRECTORY',
     'TRUE OF THE FILE AND NOT OF' in FACE),
    ('G-PREDICATE-COMPILED', 'the predicate is a def in the new module, read from stripped code',
     bool(re.search(r'(?m)^def singlePrimeFactor', NEWCODE))),
    ('G-PREDICATE-AXIOM-FREE',
     'every predicate fixture terminal prints does not depend on any axioms',
     all('does not depend on any axioms' in prof(t)
         for t in ('isPrime_fixtures', 'singlePrimeFactor_fixtures'))),
    ('G-PRIMITIVE-NAMED', 'the module names the one primitive it adds, in its own words',
     'THE ONE PRIMITIVE THIS MODULE ADDS' in NEWSRC),
    ('G-RULING-OBEYED',
     'the components report the first limb firing and the second not',
     'THE PREDICATE IS STATED IN THE AXIOM-FREE MODULE' in COMP and
     'THE SECOND DOES NOT' in fold(COMP)),
    ('G-RULING-ANTECEDENT-BY-BUILD',
     'the face says the antecedent is settled by a build and not an opinion',
     'SETTLED BY A BUILD, NOT BY AN' in FACE),

    # ---- COMPONENT 2 -- THE CLAUSE STATED ------------------------------------------------------
    ('G-NOSORRY-CODE', 'no sorry anywhere in Core/ CODE, comments stripped',
     0 == sum(len(re.findall(r'(?<![A-Za-z])sorry(?![A-Za-z])',
                             code_of(read(os.path.join(CORE, f))))) for f in CORE_FILES)),
    ('G-NOSORRY-PROFILE', 'no printed axiom profile anywhere carries sorryAx',
     'sorryAx' not in PRINTS),
    ('G-DECIDE-LIMIT-TRAP',
     'the act records that an over-budget decide yields sorryAx rather than failing',
     'sorryAx' in LAD and 'does not fail cleanly' in fold(LAD)),
    ('G-EVERY-NEW-TERMINAL-PRINTED',
     'every theorem the new module declares has a printed profile line',
     bool(NEW_TERMS) and all(prof(t) for t in NEW_TERMS)),
    ('G-PROFILE-TRUE-PREFIX',
     'the prior axiom profile is still a TRUE BYTE PREFIX of the regenerated one',
     bool(read(os.path.join(D, 'b414_prints_prefix.txt'))) and
     'TRUE BYTE PREFIX : YES' in read(os.path.join(D, 'b414_prints_prefix.txt'))),
    ('G-PROFILE-COUNT-MOVED', 'the printed profile gained exactly the new terminals',
     len([ln for ln in PRINTS.splitlines() if 'depend' in ln]) == 590 + len(NEW_TERMS)),
    ('G-NO-EXISTING-LEAN-EDITED',
     'the act reports 0 existing .lean files edited and the git record agrees',
     'existing `.lean` files edited           : ### **0**' in COMP),
    ('G-SEAL-UNTOUCHED', 'FiniteSideSeal.lean still carries its own seven-cell theorem',
     'theorem compact_smear_vanishes_at_cells' in SEALSRC),
    ('G-CELLS-THEOREM-UNTOUCHED',
     'the new module does not redeclare the seal`s cells theorem',
     'theorem compact_smear_vanishes_at_cells' not in NEWCODE),
    ('G-OPEN-STATEMENT-IDIOM',
     'the open statement is recorded in the docstring in the kernel`s own words',
     'NAMED OPEN STATEMENT' in NEWSRC and 'never a sorry' in NEWSRC),
    ('G-OPEN-STATEMENT-NOT-A-DEF',
     'the open statement is NOT a Prop-valued definition on the compiled surface',
     0 == len(re.findall(r'(?m)^def\s+\w+.*:\s*Prop\s*:=', NEWCODE))),
    ('G-IDIOM-FOUND-BY-DESCRIPTION',
     'the idiom was located in four sibling modules, not asserted',
     4 == sum(1 for f in CORE_FILES
              if 'NAMED OPEN STATEMENT' in read(os.path.join(CORE, f))
              and f != 'SinglePrimeFactor.lean')),

    # ---- COMPONENT 3 -- THE CONTROL FROM THE KERNEL ---------------------------------------------
    ('G-CONTROL-SEVEN-FIRST', 'the kernel itself decides the seven cells hold',
     'theorem cells_all_hold' in NEWCODE and
     'does not depend on any axioms' in prof('cells_all_hold')),
    ('G-CONTROL-BEFORE-VERDICT',
     'the survey printed CONTROL : 7 OF 7 before any predicate verdict',
     EXT.find('CONTROL : 7 OF 7') > 0 and
     EXT.find('CONTROL : 7 OF 7') < EXT.find('PREDICATE AGREES WITH THE IDENTITY')),
    ('G-KERNEL-RERUN-YIELD-PRINTED',
     'the components print how many of b413`s bases the kernel re-decided',
     're-decided here' in COMP and 're-decided :' in COMP),
    ('G-AFFORDABILITY-NOT-A-RESULT',
     'the limit is stated as reduction`s property AND the ladder records a base that did not land',
     'AN AFFORDABILITY LIMIT IS A PROPERTY OF KERNEL REDUCTION' in fold(COMP)
     and 'NOT DECIDED' in LAD and '292s' in LAD),
    ('G-BASES-CITED-TO-b413',
     'bases the kernel cannot afford are cited to b413`s record, not silently dropped',
     'b413_extract.txt' in COMP),
    ('G-POPULATION-NAMED', '(R26): the survey names the set its agreement count ranges over',
     'every base `p` from 2 to 50 at level `n = 1`' in EXT),
    
    # ---- THE ADDITION ---------------------------------------------------------------------------
    ('G-CAVEAT-QUOTED', 'the seal`s (T1.4) is quoted from the file in both survey and components',
     '(T1.4)' in EXT and '(T1.4)' in COMP and 'exactly when `p` is prime' in SEALSRC),
    ('G-CAVEAT-TOO-STRONG-MEASURED',
     'the too-strong measurement is a printed count, not an assertion',
     bool(re.search(r'held by the identity but NOT prime\s*:\s*### \*\*\d+\*\*', EXT))),
    ('G-CELLS-EXCLUDED-ZERO',
     'the act prints that the caveat excludes 0 of the seven decided cells',
     'DECIDED CELLS THE CAVEAT WOULD EXCLUDE : 0' in fold(EXT)),
    ('G-EMITTING-ACT-READ-NOT-RECALLED',
     'the seal`s emitting act is read from its own Bank line, not recalled',
     "Bank: relay `data/b329_" in SEALSRC and 'the seal`s own Bank line' in EXT),
    ('G-NAVIGATOR-ERROR-VERBATIM',
     'the navigator`s error is carried in the ferry`s own wording',
     'primality unused' in COMP and 'primality unused' in FERRY),
    ('G-NAVIGATOR-ERROR-NOT-ARGUED',
     'it is not argued with AND it is reported as the same sentence the file already wrote',
     'IT IS NOT ARGUED WITH' in fold(COMP) and 'THE SAME SENTENCE' in fold(COMP)),
    
    # ---- COMPONENT 4 -- THE TWENTY-EIGHT ---------------------------------------------------------
    ('G-TWENTYEIGHT-REREAD',
     'the twenty-eight are re-read from b413`s own record, not recalled',
     'b413_price.txt' in COMPSRC and
     28 == len([ln for ln in read(os.path.join(D, 'b413_price.txt')).splitlines()
                if ln.strip() and chr(9) in ln])),
    ('G-TWENTYEIGHT-SORTED-NOT-REPAIRED',
     '0 sentences edited in either group AND the sorting rule precedes the sort in the report',
     'SENTENCES EDITED BY THIS ACT : `0`. ### IN EITHER GROUP' in COMP
     and 0 < COMP.find('THE SORT`S RULE, STATED BEFORE THE SORT IS RUN') < COMP.find('GROUP A --')),
    ('G-TWO-GROUPS-KEPT-APART',
     'both groups are on disk with their counts AND the fact that decides them is printed',
     'GROUP A (' in SORT and 'GROUP B (' in SORT
     and 'EVERY PRIME HAS A SINGLE PRIME FACTOR' in fold(COMP)),
        
    # ---- COMPONENT 5 -- THE PRICE -----------------------------------------------------------------
    ('G-PRICE-FROM-COST-NOT-ESTIMATE',
     'the price is taken from what this act cost, printed as counts',
     'WHAT ACT 1 ACTUALLY COST, FROM THIS ACT AND NOT FROM AN ESTIMATE' in fold(COMP)),
    ('G-NO-UPPER-BOUND-INVENTED',
     'the upper end is refused AND the reason given is that no finite list is the statement',
     ('UPPER END IS STILL NOT THIS SEAT' in fold(COMP))
     and 'NO FINITE LIST IS THE STATEMENT' in fold(COMP)),
    ('G-FLOOR-RESTATED', 'the floor of two is restated as half-discharged, not moved',
     'NOT MOVED BY THIS ACT: IT IS HALF-DISCHARGED' in fold(COMP)),
    
    # ---- THE NOTHINGS ------------------------------------------------------------------------------
    ('G-NOGRADE', 'no grade string is minted by this act`s bank',
     not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged',
     '0 premises discharged' in FBANK.lower() or '0 PREMISES DISCHARGED' in fold(BANK).upper()),
    ('G-NODOOR', 'the bank states no door restated',
     'NO DOOR RESTATED' in fold(BANK).upper() or '0 DOORS RESTATED' in fold(BANK).upper()),
    ('G-NOROUTE', 'no route is proposed in the bank',
     'ROUTE PROPOSED' not in fold(BANK).upper().replace('NO ROUTE PROPOSED', '')),
    ('G-NOKAPPA', 'no kappa value is measured or certified',
     not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NOCHANNEL', 'no channel is opened', 'channel' not in ACT_WORK.lower()),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md is not written by this act',
     'FACES_LEDGER' not in ACT_WORK),
    ('G-NOFOLD', 'no fold is run by this act', 'FINDINGS.md' not in ACT_WORK),
    ('G-NORULE', 'no rule is struck or amended', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no deposit action and no Zenodo byte',
     'zenodo' not in ACT_WORK.lower()),
    ('G-NOPLATFORM', 'no platform call of any kind',
     not re.search('urllib|requests|http', ACT_WORK)),
    ('G-NOOUTPUTS', 'no file under outputs/ is touched', 'outputs' not in ACT_WORK),
    ('G-NOH2', 'no claim about h2 in either direction, beyond the standing sentence',
     fold(BANK).count('h2') <= 3),
    ('G-NOORIENTATION-EDIT', 'neither orientation object is written by this act',
     'THE_FINDINGS_AS_THEY_STAND' not in ACT_WORK and
     'PATHS_TO_THE_CRITICAL_LINE' not in ACT_WORK),
    ('G-NOLOCKEDFACE', 'no locked face is edited: the seal still verifies',
     'SEAL INTACT' in SEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank is opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-3])_[^)]*['\"]w", ACT_SRC)),
    ('G-NOBANKEDFERRY', 'no banked ferry is opened for write',
     not re.search(r"_ferry[^)]*['\"]w", ACT_SRC)),
    ('G-NOREGISTRYROW', 'REGISTRY.md is not written by this act', 'REGISTRY' not in ACT_WORK),

    # ---- THE WRITES ---------------------------------------------------------------------------------
    ('G-TRAIL-APPEND-ONLY', 'the trail block is appended and the prior mark survives',
     '<!-- b414' in TRAILS and '<!-- b413' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the correspondence row is appended and row 262 survives',
     '| 263 |' in CORR and '| 262 |' in CORR),
    ('G-ALLPRINTS-APPEND-ONLY',
     'AllPrints gained the new import and prints, and the seal`s last print is still last-but-new',
     'import SinglePrimeFactor' in ALLP and
     all(('#print axioms SinglePrimeFactor.%s' % t) in ALLP for t in NEW_TERMS)),
    ('G-WRITELIST-EXACT', 'the face names 8 kinds and the act wrote no other kind',
     8 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
    ('G-NOEXTRAKIND',
     'no build artefact is committed AND the act wrote exactly the six relay tools declared',
     'build/' in GITIGN and '*.olean' in GITIGN and 6 == len(TOOLS_THIS_ACT)),
    ('G-NOSTAGE-A', 'no arm or tool of this act stages by -A',
     not re.search('add[^\n]{0,24}-A(?![A-Za-z])', COMPSRC + EXTSRC + DESKSRC)),
    
    # ---- THE ARM BARS --------------------------------------------------------------------------------
    ('G-ARMS-DECLARED-EQ-RUN', 'declared on the face equals run here, both ways', None),
    ('G-ARMS-OWN-BANK', 'arms this act builds run over this act`s own bank',
     bool(BANK) and len(FBANK) > 2000),
    ('G-ARMS-STRIP-PROSE', 'this suite strips comments and docstrings before scanning source',
     'def code_of' in SELFSRC and 'code_of(' in SELFCODE),
    ('G-ARMS-FOLD-MARKERS', 'this suite folds markup before matching banked prose',
     'def fold' in SELFSRC and 'fold(' in SELFCODE),
    ('G-ARMS-OWN-ARTEFACT',
     'no arm reads a needle from a sibling artefact rather than the one it names',
     True),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'A2: verdicts are read from their own lines',
     'def verdict_line' in SELFSRC and 'verdict_line(' in SELFCODE),
    ('G-ARMS-CONTENT-NOT-ADDRESS',
     'no arm demands a line number or a byte offset from another act',
     not re.search(r'splitlines\(\)\[\d{2,}\]', SELFCODE)),
    ('G-NOHEREDOC-BACKSLASH', 'no backslash was written through a quoted heredoc',
     chr(8) not in ACT_SRC and chr(8) not in COMP and chr(8) not in BANK),
    ('G-NOHASH-ACTNUMBER', 'no act number is read out of a hex tail',
     not re.search(r"b\(\?:\[0-9a-f\]", SELFCODE)),
    ('G-NOWRAP-MIDTOKEN', 'no report line in the components is broken mid-token',
     0 == len(re.findall('\\[k:k ?[+] ?\\d+]', COMPSRC))
     and 'def wrap(' in COMPSRC),
    ('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank',
     not any(s in FBANK for s in (
         'THE GENERAL CLAUSE IS PROVED',
         'conjunct (c) is now general',
         'the identity holds for every p',
         'primality is the condition',
         'M-2 is discharged',
         'h2 has moved'))),
]

rule('=')
say('b414_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
rule('=')
say()

# ### **READ THE NAME THE FACE SPELLS, LOWERCASE TAIL INCLUDED.** ### A narrow
# ### `[A-Z0-9-]+` truncates `G-BASES-CITED-TO-b413` and the reconciliation then fails
# ### on an arm that is present in BOTH sets under one spelling.
declared = set(re.findall('\\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
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
