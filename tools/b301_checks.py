# -*- coding: utf-8 -*-
"""b301 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM EMITTING FILES AND FROM THIS ACT'S OWN FILES.
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY, NEVER A SUBSTRING** (b277's species).

### ### **THE TWO GATES THIS ACT ADDS ARE `G-EXACT` AND `G-VECTORS`, AND EACH ANSWERS A FALSIFIER
### ### THE ORDER NAMED.**
###   ### **`G-EXACT` (V3):** ### the convergence re-check had to run in exact rationals, because
###     the quantity at stake is irrational and a float comparison decides a rounding. ### The gate
###     reads the runner's SOURCE for float literals ### **AND** ### asserts at RUNTIME that what
###     the runner returns is a `Fraction`. ### **THE SOURCE ARM ALONE WOULD MISS A FLOAT PRODUCED
###     BY DIVIDING TWO INTEGERS, AND THE RUNTIME ARM ALONE WOULD MISS A LITERAL THAT NEVER
###     REACHES THE RETURN. ### NEITHER ARM IS THE CHECK.**
###   ### **`G-VECTORS` (V4):** ### the order forbids transporting a result about the object's
###     archimedean unit to the vectors the instruments compute from, or back. ### The gate finds
###     every sentence carrying BOTH names and requires that sentence to carry the separation in
###     its own words. ### **ITS LIMIT IS PRINTED WITH IT: A SENTENCE CAN SAY "DIFFERENT" AND STILL
###     TRANSPORT A RESULT. ### IT CLOSES THE SILENT CO-OCCURRENCE AND NOTHING MORE.**
"""
import io
import os
import re
import subprocess
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import needle_pull   # noqa: E402
import hedge_audit   # noqa: E402
import ferry_scan    # noqa: E402
import banned_terms  # noqa: E402
import b301_the_object as OBJ  # noqa: E402  ### the runner is IMPORTED so G-EXACT can run it

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'


def d(n):
    return os.path.join(D, n)


BANK = d('b301_the_object_completed.txt')
REG = d('b301_registration_2026-09-02.txt')
GATE = d('b301_object_gate.txt')
SCAN = d('b301_ferry_scan.txt')
FERRY = d('b301_ferry_2026-09-02.txt')
PINS = d('b301_pins_step_zero.txt')
SPEC = d('b301_satisfiable.json')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b301_the_object.py')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNED = [BANK, REG, GATE, SCAN, FERRY, PINS, SPEC, RUNNER,
         os.path.join(ROOT, 'tools', 'b301_regspec.py'),
         os.path.join(ROOT, 'tools', 'b301_correspondence.py'),
         os.path.join(ROOT, 'tools', 'b301_index_append.py')]
# ### THE FIXTURE-CARRIER, SCANNED AND REPORTED SEPARATELY -- b300's stated exception, carried.
FIXTURE_CARRIERS = [os.path.join(ROOT, 'tools', 'b301_checks.py')]

OWNER_NEEDLES = [
    ("the finite local space, from its construction line (EMITTER)",
     d('b279_the_local_space.txt'), 'the L^2(Q_p)-CLOSURE OF'),
    ("d_1 > 0 at every finite place (EMITTER)",
     d('b198_nonvanishing.txt'), 'A LEVEL DIMENSION d_1(p,n) > 0'),
    ("the arrival depth's zero cell (EMITTER)",
     d('b198_nonvanishing.txt'), 'ZERO at exactly one cell, (2,1)'),
    ("the level rule with its exceptional place (EMITTER)",
     d('b226_stated_choice.txt'), 'ell(p) := 2 if p = 2, else 1'),
    ("the finite unit's owed generic step (EMITTER)",
     d('b226_stated_choice.txt'), 'THE GENERIC ODD PLACE IS *OWED*'),
    ("von Neumann 4.1.1's H_a (EMITTER)",
     d('b226_stated_choice.txt'), 'H_a be the closed'),
    ("von Neumann 4.1.2's norm-one hypothesis (EMITTER)",
     d('b226_stated_choice.txt'), 'with ||f_a|| = 1'),
    ("the C0 norm-sum demand at b197's grade (EMITTER)",
     d('b226_stated_choice.txt'), 'SUM_v | ||f_v|| - 1 | CONVERGE'),
    ("b226's exact zero, the result being re-checked (EMITTER)",
     d('b226_stated_choice.txt'), 'THE SUM IS ZERO'),
    ("the choice-dependence question, filed open (EMITTER)",
     d('b226_stated_choice.txt'), 'DOES (x)\'_v (S-bar_v, u_v) DEPEND ON THE CHOICE?'),
    ("the author's re-scope ruling, verbatim (EMITTER)",
     d('b225_serializing_close.txt'), 'purity is not required by the new plan'),
    ("the ruling asks for a SECTOR unit (EMITTER)",
     d('b225_serializing_close.txt'), 'with the archimedean unit from the Sonin sector'),
    ("b221's purity reading, on the product it is about (EMITTER)",
     d('b221_cell_level_assembly.txt'), 'NEEDS PURITY, NOT MERELY EXISTENCE'),
    ("the source's inner product (EMITTER)",
     d('b300_source_read.txt'), 'We normalize the inner product'),
    ("the archimedean space's conditional verdict (EMITTER)",
     d('b300_the_archimedean_leg.txt'), 'THE SPACE: ### (CONSTRUCTED, CONDITIONALLY)'),
    ("scalar-invariance of membership (EMITTER)",
     d('b292_the_identification.txt'), 'IF AND ONLY IF `cv` IS'),
    ("the finite two-radius family and its diagonal (EMITTER)",
     d('b293_the_finite_family.txt'), 'THE CORPUS\'S EXISTING SPACE IS THE DIAGONAL MEMBER'),
    ("b293's refusal to use the archimedean family as evidence (EMITTER)",
     d('b293_the_finite_family.txt'), 'NOWHERE THE EVIDENCE'),
    ("the archimedean orbit and the self-dual point (EMITTER)",
     d('b291_the_involution.txt'), 'THE CORPUS\'S ARCHIMEDEAN MEMBER IS SELF-DUAL'),
    ("what stood before the finite family was built (EMITTER)",
     d('b291_the_involution.txt'), 'NO TWO-PARAMETER FINITE-PLACE FAMILY'),
    ("b221's own note that the halt is not at infinity (EMITTER)",
     d('b221_cell_level_assembly.txt'), 'the halt is at the FINITE places, not at infinity'),
]

SELF_NEEDLES = [
    ('bank returns the status in one sentence', BANK, 'IS ### CONSTRUCTED CONDITIONALLY ###'),
    ('bank types the four conditions', BANK, 'A PREMISE (the level limit), A RESULT'),
    ('bank separates the two products', BANK, '`P-RTP` -- THE RESTRICTED TENSOR PRODUCT'),
    ('bank records the purity halt against P-RTP only', BANK,
     'AGAINST `P-RTP` AND AGAINST NOTHING ELSE'),
    ('bank quotes the ruling that purity is not required', BANK,
     'NOT REQUIRED BY THE NEW PLAN'),
    ('bank gives the requirement census', BANK, '4 MET, 3 OPEN, 1 NOT ASKED'),
    ('bank names what Q3 is missing', BANK, 'EVERY ODD `p` AT LEVEL 1'),
    ('bank names what Q4 is missing', BANK, '`c = +1` AT RANK 2 ABOVE BENCH'),
    ('bank re-checks rather than cites the convergence', BANK,
     'RE-CHECKED RATHER THAN CITED'),
    ('bank reports the corpus picture agreeing with the source', BANK,
     'AGREES WITH THE SOURCE ON THE NOSE'),
    ('bank carries the exact enclosure as an integer', BANK, '29289321881345247559'),
    ('bank says no compiled terminal is disturbed', BANK,
     'NO COMPILED TERMINAL IS DISTURBED'),
    ('bank declines to renormalize', BANK, 'THIS ACT DOES NOT PERFORM IT'),
    ('bank says the row does not move, with reasons', BANK,
     'IT DOES NOT MOVE, AND THE REASON IS DERIVED'),
    ('bank quotes the term-3 row it declines to edit', BANK,
     'term 3 -- restricted-tensor assembly'),
    ('bank files the uniform form as a proposal', BANK, 'UNBANKED-UNTIL-TESTED'),
    ('bank states the uniform form\'s promotion criterion', BANK,
     'A DEFINITION OF THE FAMILY ### ACROSS ### PLACES'),
    ('bank states the caution beside the resemblance', BANK,
     'A SHARED FORM IS A RESEMBLANCE UNTIL A DEFINITION IS WRITTEN'),
    ('bank reports the shadow check returning a candidate', BANK,
     'THE FIRST WHOSE CHECK RETURNED A CANDIDATE'),
    ('bank refuses to break its own registered cap', BANK,
     'A CEILING IS A PROHIBITION THE ACT'),
    ('bank keeps M-2 unchanged', BANK, '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`'),
    ('bank restates the seam debt unpaid', BANK, 'THE SEAM\'S DEBT ITEM 1: ### STILL UNPAID'),
    ('bank states what it did not check, per ruling (2)', BANK, 'NOT CHECKED THIS ACT'),
    ('bank corrects the order\'s commit count', BANK, 'THREE COMMITS WENT, NOT TWO'),
    ('bank records the hook coverage observation', BANK, 'W-ORD-HOOK-COVERAGE'),
    ('registration separates the products before any requirement', REG,
     'THE TWO PRODUCTS, SEPARATED BEFORE ANY REQUIREMENT'),
    ('registration records the seats disagreeing', REG, 'THE SEATS DO NOT AGREE'),
    ('registration caps the lean files at zero', REG, '`.lean` FILES MOVED: CAP 0'),
    ('the object gate reports the census', GATE, 'constituent cells   : 13'),
    ('the object gate certifies the enclosure by squaring', GATE,
     'certified by squaring (lo^2 < 1/2 < hi^2) : True'),
    ('the step-zero pins read 0/0 in all three repos', PINS, 'behind/ahead: 0	0'),
]

MUST_FAIL = [
    ('the object is not called unconditionally constructed', BANK,
     'THE OBJECT IS CONSTRUCTED.'),
    ('term 3 is not called constructed', BANK, 'TERM 3 IS CONSTRUCTED.'),
    ('the row is not called moved', BANK, 'THE ROW MOVES.'),
    ('no aggregation is stated', BANK, 'THE AGGREGATION IS STATED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the uniform form is not promoted', BANK, 'THE UNIFORM FORM IS DERIVED.'),
    ('no unit is renormalized', BANK, 'THE ARCHIMEDEAN UNIT IS RENORMALIZED.'),
    ('the owed generic place is not called discharged', BANK,
     'THE GENERIC ODD PLACE IS DISCHARGED.'),
    ('the struck phrase is not used in the closing', BANK, 'HANDOFF CURRENT.'),
    ('no act is re-verdicted', BANK, 'b300 IS RE-VERDICTED.'),
]

TOOLNUM = [
    ("the constituent-cell and requirement censuses", 'tools/e16/b301_the_object.py'),
    ("the exact enclosure of 1 - 1/sqrt(2)", 'tools/e16/b301_the_object.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b301_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b301_checks.py'),
    ("the correspondence row's number and its read-back", 'tools/b301_correspondence.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]

NEW_THIS_ACT = ('tools/e16/b301_the_object.py', 'tools/b301_regspec.py', 'tools/b301_checks.py',
                'tools/b301_correspondence.py', 'tools/b301_index_append.py')

# ### G-VECTORS' TWO NAME SETS AND THE SEPARATION WORDS A CO-OCCURRING SENTENCE MUST CARRY.
UNIT_NAMES = re.compile(r'u_inf|u_\{?inf\}?', re.I)
INSTR_NAMES = re.compile(r'zeta_n|psi_n|psi\^_n', re.I)
SEPARATORS = re.compile(r'DIFFERENT|APART|SEPARATEL|NOT THE|IS NOT|NEITHER|TRANSPORT', re.I)

FLOAT_LITERAL = re.compile(r'(?<![\w.])\d+\.\d+|(?<![\w.])\.\d+|\bfloat\s*\(|\bimport\s+math\b')


def git_tracked(repo, relpath):
    p = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', relpath],
                       capture_output=True, text=True)
    return p.returncode == 0


def strip_literals(line):
    """### RETURN THE LINE WITH COMMENTS AND STRING LITERALS REMOVED.

    ### **CRUDE ON PURPOSE AND ITS CRUDENESS IS ITS REACH:** ### it removes anything between
    ### matching quotes and anything after an unquoted `#`. ### A float spelled inside a string in
    ### order to be printed is invisible to it -- ### **WHICH IS THE POINT: A PRINTED NUMBER IS NOT
    ### A DECIDING NUMBER.**
    """
    out, i, quote = [], 0, None
    while i < len(line):
        ch = line[i]
        if quote:
            if ch == chr(92):
                i += 2
                continue
            if ch == quote:
                quote = None
            i += 1
            continue
        if ch in (chr(39), chr(34)):
            quote = ch
            i += 1
            continue
        if ch == '#':
            break
        out.append(ch)
        i += 1
    return ''.join(out)


def margin_free(text):
    """### THE CORPUS'S LEFT MARGIN AND INLINE EMPHASIS RUNS REMOVED, THEN FLATTENED.

    ### `###` is BOTH a line prefix and an inline emphasis marker in this record. ### Stripping it
    ### leaves the prose; ### **TREATING IT AS A SEGMENT BOUNDARY WOULD SHRED THE TEXT INTO
    ### FRAGMENTS TOO SHORT TO CARRY A CO-OCCURRENCE AT ALL** -- which is how a check meant to be
    ### strict becomes one that passes because it can no longer see anything. ### That was this
    ### gate's own second draft and it is recorded rather than quietly replaced.
    """
    out = []
    for line in text.splitlines():
        s = line.lstrip()
        while s.startswith('#'):
            s = s.lstrip('#').lstrip()
        out.append(s)
    flat = ' '.join(' '.join(out).split())
    return re.sub(r'#{2,}', ' ', flat)


def cooccurrences(text, window=300, context=200):
    """### RETURN `(pairs, unmarked)` -- ### **A WINDOWED PROXIMITY CHECK, NOT A SENTENCE SPLIT.**

    ### A pair is a UNIT name and an INSTRUMENT name within `window` characters of each other in
    ### the margin-free text; the surrounding `context` characters must carry the separation in the
    ### act's own words.
    ### ### **WHY A WINDOW AND NOT A SENTENCE: ### THE FALSIFIER TABLES AND LEDGERS IN THIS RECORD
    ### ### CARRY NO SENTENCE-ENDING PUNCTUATION AT ALL.** ### A sentence splitter either fuses a
    ### whole table into one unit, or -- taught to break on the record's own row markers -- shreds
    ### it into fragments shorter than a single claim. ### **NEITHER UNIT IS THE ONE THE CHECK IS
    ### ABOUT, AND BOTH DRAFTS WERE TRIED HERE BEFORE THIS ONE.**
    """
    flat = margin_free(text)
    us = [m.start() for m in UNIT_NAMES.finditer(flat)]
    vs = [m.start() for m in INSTR_NAMES.finditer(flat)]
    pairs, unmarked = [], []
    for a in us:
        for b in vs:
            if abs(a - b) <= window:
                lo, hi = max(0, min(a, b) - context), min(len(flat), max(a, b) + context)
                pairs.append((a, b))
                if not SEPARATORS.search(flat[lo:hi]):
                    unmarked.append(flat[lo:hi])
                break
    return pairs, unmarked



def main():
    fails = []
    print('=' * 100)
    print('b301 -- GATE SUITE')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (pulled from emitting files):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    # ### ==========================================================================================
    # ### G-EXACT -- ### **TWO ARMS, AND NEITHER ARM IS THE CHECK.**
    # ### ==========================================================================================
    print('\n  G-EXACT (V3: the deciding runner carries no float):')
    # ### DEFECT FIXED ON THIS GATE'S FIRST RUN. ### The first version scanned the whole file and
    # ### returned EIGHT hits -- ### **EVERY ONE A DOCUMENT SECTION NUMBER INSIDE A STRING**:
    # ### `Definition 4.4`, `Lemma 4.1.2`, `Definition 3.3.1`. ### **A CHECK THAT CANNOT TELL A
    # ### FLOAT FROM A CITATION IS NOT CHECKING FOR FLOATS**, and it would have been silenced by
    # ### deleting the citations rather than by fixing the scope.
    # ### ### **THE FIX IS THE SCOPE: A FLOAT THAT DECIDES ANYTHING IS IN CODE, NOT IN THE PROSE
    # ### ### THE CODE PRINTS.** ### Comments and string literals are removed before the scan.
    src = io.open(RUNNER, encoding='utf-8').read()
    body = src.split('"""', 2)[-1]          # ### skip the module docstring's prose
    lits = []
    for i, line in enumerate(body.splitlines(), 1):
        code = strip_literals(line)
        if not code.strip():
            continue
        for m in FLOAT_LITERAL.finditer(code):
            lits.append((i, m.group(0), line.strip()[:80]))
    print('    SOURCE ARM  : float literals / float() / math in the runner body : %d' % len(lits))
    for i, tok, ln in lits[:8]:
        print('        ### %-14s %s' % (tok, ln))
    lo, hi = OBJ.enclose_inv_sqrt2(20)
    dev_lo, dev_hi = Fraction(1) - hi, Fraction(1) - lo
    types_ok = all(isinstance(x, Fraction) for x in (lo, hi, dev_lo, dev_hi))
    cert = OBJ.certified(lo, hi)
    print('    RUNTIME ARM : the enclosure returns Fractions : %s ; certified by squaring : %s'
          % (types_ok, cert))
    # ### THE DISCRIMINATION ARM: the source scanner must fire on a line that HAS a float.
    # ### BOTH POLARITIES ON THE STRIPPER ITSELF, since it is now what the arm's reach rests on.
    disc = bool(FLOAT_LITERAL.search(strip_literals('x = 0.5 + 1')))
    quiet = not FLOAT_LITERAL.search(strip_literals('s = "CC Definition 4.4, eq (16)"'))
    print('    DISCRIMINATION: fires on a float in CODE : %s ; stays quiet on a citation inside a'
          ' STRING : %s' % (disc, quiet))
    print('    ### **THE SOURCE ARM ALONE MISSES A FLOAT MADE BY DIVIDING INTEGERS; THE RUNTIME')
    print('    ### ARM ALONE MISSES A LITERAL THAT NEVER REACHES A RETURN. ### BOTH, OR NEITHER.**')
    if lits or not types_ok or not cert or not disc or not quiet:
        fails.append('G-EXACT')

    # ### ==========================================================================================
    # ### G-VECTORS -- ### **V4: A SENTENCE NAMING BOTH MUST CARRY THE SEPARATION.**
    # ### ==========================================================================================
    print('\n  G-VECTORS (V4: the unit and the instrument vectors stay apart):')
    pairs, unmarked = cooccurrences(io.open(BANK, encoding='utf-8').read())
    print('    UNIT/INSTRUMENT name pairs within 300 chars : %d' % len(pairs))
    print('    of those, whose neighbourhood carries the separation : %d'
          % (len(pairs) - len(unmarked)))
    print('    UNMARKED CO-OCCURRENCES : %d  %s'
          % (len(unmarked), 'PASS' if not unmarked else '### FAIL ###'))
    for s in unmarked[:5]:
        print('        ### %s' % s[:200])
    ctrl_p, ctrl_u = cooccurrences('the unit u_inf is paired against zeta_n in the same step')
    ctrl_ok = len(ctrl_p) == 1 and len(ctrl_u) == 1
    ctrl2_p, ctrl2_u = cooccurrences('u_inf is a DIFFERENT vector from zeta_n and psi_n')
    ctrl2_ok = len(ctrl2_p) == 1 and not ctrl2_u
    print('    CONTROL: an unseparated co-occurrence IS caught : %s ; a separated one is NOT : %s'
          % (ctrl_ok, ctrl2_ok))
    print('    ### **THE LIMIT: A NEIGHBOURHOOD CAN SAY "DIFFERENT" AND STILL TRANSPORT A')
    print('    ### RESULT. ### IT CLOSES THE SILENT CO-OCCURRENCE AND NOTHING MORE.**')
    if unmarked or not ctrl_ok or not ctrl2_ok:
        fails.append('G-VECTORS')

    # ### ==========================================================================================
    # ### G-STRUCK and G-STEM.
    # ### ==========================================================================================
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK (record: %d struck entries, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(e['patterns']) for e in struck), unconf))
    total = 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                     struck, stem_list)
        total += len(ch)
        print('    %-44s struck-clause hits : %d  %s'
              % (os.path.basename(p), len(ch), 'PASS' if not ch else '### FAIL ###'))
        for h in ch:
            print('        line %d col %d  %s' % (h[1], h[2], h[0]))
    for p in FIXTURE_CARRIERS:
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), struck, stem_list)
        print('    %-44s struck-clause hits : %d  ### ITS OWN FIXTURES (stated exception)'
              % (os.path.basename(p) + ' (EXCEPTION)', len(ch)))
    probes = [('S-1', 'a title must name its objects and conditions, not claim an achieved '
                      'property'),
              ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
              ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
    fired = 0
    for eid, text in probes:
        hit = bool(ferry_scan.scan_text(text, struck, stem_list)[0])
        fired += 1 if hit else 0
        print('    DISCRIMINATION %-4s comes back hit : %s  %s'
              % (eid, hit, 'PASS' if hit else '### FAIL ###'))
    if total or fired != len(probes):
        fails.append('G-STRUCK')

    print('\n  G-STEM (banned + retired stems over every file this act wrote):')
    stem_total, swept = 0, 0
    for p in OWNED + FIXTURE_CARRIERS:
        if not os.path.exists(p):
            continue
        swept += 1
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                      [], stem_list)
        stem_total += len(sh)
        if sh:
            print('    ### %-40s stem hits : %d' % (os.path.basename(p), len(sh)))
            for h in sh:
                print('        line %d  %s  |  %s' % (h[1], h[0], h[3][:88]))
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    files swept %d   stem hits %d   control fires %s   %s'
          % (swept, stem_total, ctrl, 'PASS' if not stem_total and ctrl else '### FAIL ###'))
    if stem_total or not ctrl:
        fails.append('G-STEM')

    # ### ==========================================================================================
    # ### THE THREE PLANNED ZEROS, RE-MEASURED AGAINST WHAT LANDED.
    # ### ==========================================================================================
    print('\n  G-TOOLNUM (ruling 3: every reported number has a committed producer):')
    orphan = 0
    for what, tool in TOOLNUM:
        exists = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tracked = git_tracked(ROOT, tool)
        ok = exists and (tracked or tool in NEW_THIS_ACT)
        orphan += 0 if ok else 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, exists, tracked))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-NOPAPERS (V10: PLACE-papers read only):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    rows = [x for x in pp.splitlines() if x.strip()]
    tracked_changes = [x for x in rows if not x.startswith('??')]
    untracked = [x for x in rows if x.startswith('??')]
    print('    TRACKED files changed by anyone : %d  %s'
          % (len(tracked_changes), 'PASS' if not tracked_changes else '### FAIL ###'))
    t0 = os.path.getmtime(REG)
    newer = []
    for x in untracked:
        rel = x[3:].strip().strip('"')
        f = os.path.join(PP, rel.replace('/', os.sep))
        if os.path.isfile(f) and os.path.getmtime(f) > t0:
            newer.append(rel)
    print('    untracked rows (pre-existing, left where they sit) : %d' % len(untracked))
    print('    of those, written AFTER this registration was sealed : %d  %s'
          % (len(newer), 'PASS' if not newer else '### FAIL ###'))
    if tracked_changes or newer:
        fails.append('G-NOPAPERS')

    print('\n  G-SHADOW (V8: nothing built -- measured, not asserted):')
    sd = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    lean = [x for x in sd.splitlines() if x.strip().endswith('.lean')]
    print('    `.lean` files moved in the kernel repo : %d  %s'
          % (len(lean), 'PASS' if not lean else '### FAIL ###'))
    if lean:
        fails.append('G-SHADOW')

    print('\n  HEDGE AUDIT (every prose file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-28s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            for s in gh:
                print('        (i) %s' % s[:140])

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 7
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
