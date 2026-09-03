# -*- coding: utf-8 -*-
"""b308_checks.py -- THE GATE SUITE FOR AN INSTRUMENT BUILD.

### ### **TWO ARMS ARE THIS ACT'S OWN AND NEITHER EXISTED BEFORE IT:**
###   ### **`G-EXACT`** ### -- the order says *exact arithmetic in every verdict*, so the two files
###     this act wrote are scanned for float literals and float-producing operators. ### **A
###     REGISTRATION CLAUSE WITH NO MEASUREMENT BEHIND IT IS A PROMISE, NOT A CAP.**
###   ### **`G-NONEW`** ### -- the order forbids a first-level value at a cell or member the record
###     does not already carry. ### The arm requires every such number printed to sit on a line that
###     names its owning tool, and it fires on a number that does not. ### **THE CAP IS ZERO AND
###     THIS IS WHAT MEASURES IT.**
### ### **AND `G-PAPERS` IS INVERTED BACK:** ### b307 touched `PLACE-papers` and checked WHICH file
### moved. ### **THIS ACT TOUCHES IT NOT AT ALL**, so the gate checks that nothing moved.
### ### **A GATE COPIED FORWARD UNINVERTED WOULD HAVE PASSED THIS ACT FOR DOING NOTHING**, which is
### the same defect as b307's in the other direction, and it is named here because the temptation to
### copy a green gate forward is exactly how a suite stops checking.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b308_the_local_field_instrument.txt')
REG = d('b308_registration_2026-09-03.txt')
RUN = d('b308_instrument_run.txt')
SCAN = d('b308_ferry_scan.txt')
FERRY = d('b308_ferry_2026-09-03.txt')
CENSUS = d('b308_census.txt')

INSTRUMENT = t('b308_local_field.py')
RUNNER = t('b308_reproduction.py')

OWNED = [RUN, CENSUS,
         d('b308_corr_row.txt'), d('b308_index_query.txt'), d('b308_pins_stepzero.txt'),
         d('b308_regspec_run.txt'), d('b308_satisfiable.json'),
         t('b308_regspec.py'), t('b308_correspondence.py')]

# ### DECLARED CARRIERS. ### **EACH IS A PLACE A CHECK HAS AGREED NOT TO COUNT, AND THE REASON IS
# ### PRINTED WITH IT** -- b306's lore rule. ### **THIS ACT HAS MORE OF THEM THAN ITS ANCESTORS AND
# ### THAT IS ITS SUBJECT'S DOING: A TOOL THAT HUNTS FOR A CODE SHAPE MUST SPELL THAT SHAPE.**
CARRIERS = [
    (t('b308_checks.py'), 'its own fixtures'),
    (t('b308_index_append.py'), 'its own fixtures'),
    (INSTRUMENT, 'it spells the fold\'s code shape IN ORDER TO SCAN FOR IT, and it exhibits the '
                 'model\'s collapse in order to count it'),
    (RUNNER, 'it quotes the owners\' lines in order to rule on them'),
    (FERRY, 'IT IS THE ORDER -- not this act\'s writing'),
    (SCAN, 'it is the scan\'s own log'),
]

OWNER_NEEDLES = [
    ("b21's chart and Haar normalization, which tie the two radii", d('b21_2026-08-18.txt'),
     'via x = p^(-n) m; Haar measure'),
    ("b21's model space, one `n` for both radii", d('b21_2026-08-18.txt'),
     'V_n IS canonically the model space'),
    ("b21's genuine transform", d('b21_2026-08-18.txt'),
     'THE GENUINE TRANSFORM: (F f)(y) = int f(x) psi(x y) dx'),
    ("b21's entry-exact model transform", d('b21_2026-08-18.txt'),
     'the model transform IS the'),
    ("b21's location of the artifact", d('b21_2026-08-18.txt'),
     "MODEL'S mod-N WRAPAROUND IS THE ARTIFACT"),
    ("b280's ball in the chart", d('b280_the_consequence.txt'),
     'ball_n = { x = p^{-n} p^n k }'),
    ("b280's Haar bridge", d('b280_the_consequence.txt'),
     'a chart point `m` at level `n`'),
    ("b280's absorption at k = n", d('b280_the_consequence.txt'), '`P(n) = 0`'),
    ("b284's escape", d('b284_the_scalings_domain.txt'), 'strictly bigger than'),
    ("### b284's sentence this act turns into a computation",
     d('b284_the_scalings_domain.txt'), 'WHERE THERE IS NOTHING TO FOLD'),
    ("### b284's own declaration of its exposure", d('b284_the_scalings_domain.txt'),
     'THE DISAGREEMENT IS THE ARTIFACT, NOT THE ANSWER'),
    ("b293's ball of exponent e", d('b293_the_finite_family.txt'),
     'B_e := { m : v_p(m) >= n - e }'),
    ("b293's dimension law", d('b293_the_finite_family.txt'), 'dim Son(p,n; a,b) = p^{2n}'),
    ("b293's dilation invariant", d('b293_the_finite_family.txt'),
     'THE SUM `a+b` IS INVARIANT'),
    ("b295's annihilation criterion", d('b295_the_second_mechanism.txt'),
     '`a >= 0`  ###  OR  ###  `b >= n - 1`'),
    ("b295's own scope sentence", d('b295_the_second_mechanism.txt'),
     'AND PAIRINGS OF THIS SHAPE'),
    ("### b295's own exposure declaration (Z5)", d('b295_the_second_mechanism.txt'),
     'NO LEVEL-SHIFTING MAP'),
    ("b305's price, whose reproduction list this act adopted as a bar",
     d('b305_the_arithmetics_entry.txt'), 'THREE ACTS FOR THE CORE'),
]

SELF_NEEDLES = [
    ('bank names the tie and the file that ties it', BANK, 'THE FILE THAT TIES THEM'),
    ('bank states the model is a point and the instrument a plane', BANK,
     'THE INSTRUMENT IS THE PLANE'),
    ('bank gives the frame law for the scaling part', BANK, 'BOTH RADII MOVE'),
    ('bank says what the fold is', BANK, 'THAT RE-READING IS THE FOLD'),
    ('bank refuses new mathematics', BANK, 'NO NEW MATHEMATICS'),
    # ### RE-POINTED AT WHAT THE FILE EMITS, NOT RE-WORDED -- the bank's own hard wrap.
    ('bank refuses a new first-level value', BANK,
     'NO FIRST-LEVEL VALUE IS COMPUTED AT ANY CELL OR'),
    ('bank reports the two re-pointed needles', BANK, 'RE-POINTED AT WHAT THE'),
    ('bank reports the transform inversion scalar', BANK, 'SCALAR COMING OUT EXACTLY'),
    ('bank reports the collapse checked in both directions', BANK, '15 ROWS'),
    ('bank reports the unitary normalization as an identity', BANK, 'THE SCALAR IS'),
    ('bank reports the Haar projector equals the model projector', BANK, 'ENTRY-WISE'),
    ('bank puts the not-dead witness before the zeros', BANK,
     'A ZERO FROM A DEAD INSTRUMENT IS NOT A ZERO'),
    ('bank reports the family recovered with zero disagreements', BANK, 'DISAGREEING, 0'),
    ('bank carries the dimension law\'s own scope', BANK, 'THE ACT DOES NOT CLAIM THE LAW THERE'),
    ('bank reports the criterion counts', BANK, 'MEMBERS REACHED : 80'),
    ('bank reports the two banked values', BANK, 'banked `4/7`, recomputed `4/7`'),
    ('bank reports the model fold counts', BANK, 'AGREEING WITH THE CLOSED FORM AT ALL TEN'),
    ('bank reports the instrument folds nothing', BANK, "THE INSTRUMENT'S ARE `0` AT ALL TEN"),
    ('bank reports the escaped mass exactly', BANK, 'EXACT NONZERO RATIONAL AT EVERY CELL'),
    ('bank reports zero undeclared sites in the operational path', BANK,
     'UNDECLARED SITES IN THE INSTRUMENT'),
    ('bank owns the narrative defect the arm caught', BANK, 'THE DEFECT WAS THE'),
    ('bank names b284 as the exposed result', BANK, 'DECLARED ITSELF'),
    ('bank bounds the retirement', BANK, 'AND IT RETIRES NOTHING ELSE'),
    ('bank says the truncation is untouched', BANK, 'IT DOES NOT REMOVE THE'),
    ('bank gives capabilities and limits as a list', BANK, 'WHAT IT CANNOT DO'),
    ('bank names the next computation without doing it', BANK, 'NAMED, AND NOT COMPUTED'),
    ('bank refuses to treat naming as evidence', BANK, 'A NAMED COMPUTATION IS NOT EVIDENCE'),
    ('bank restates the object\'s three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged', BANK, "`M-2`'s ROW: ### UNCHANGED"),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'DAYS PAST BOTH, AND NOTHING ON THIS'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank reports the census count and its scope limit', BANK,
     'DOES NOT INCLUDE THIS ACT'),
    ('bank reports the shadow as nothing', BANK, 'EXPECTED NOTHING, AND NOTHING IS WHAT IT IS'),
    ('bank reads three holding falsifiers honestly', BANK, 'THEY WERE EXPECTED TO'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('registration is sealed before the instrument existed', REG,
     'BEFORE THE INSTRUMENT IS WRITTEN'),
    ('registration adopts b305\'s reproduction list as the bar', REG,
     'THE REPRODUCTION IS THE GATE ON THE BUILD'),
    ('registration forbids repairing the instrument to agree', REG,
     'THE INSTRUMENT IS NOT REPAIRED TO MAKE IT'),
    ('registration says a reproduction does not raise a grade', REG,
     'DOES NOT RAISE ITS GRADE'),
    ('the run reports F1 did not fire', RUN,
     '(F1) the reproduction matches at every reachable cell ......... ### **DID NOT FIRE**'),
    ('the run reports F2 did not fire', RUN, '(F2) the scaling part acts without wraparound'),
    ('the run reports F3 did not fire', RUN, '(F3) the untied radii recover the two-radius'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run reports zero unpullable owner sentences', RUN, '### UNPULLABLE : 0'),
    ('the run reports the exposure table by call path', RUN, 'BY CALL PATH'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('no act is re-verdicted', BANK, 'b304 IS RE-VERDICTED.'),
    ('the instrument is not called a result', BANK, 'THE INSTRUMENT IS A RESULT.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the artifact is not retired generally', BANK, 'THE ARTIFACT IS RETIRED.'),
    ('the truncation is not claimed removed', BANK, 'THE TRUNCATION IS REMOVED.'),
    ('the reproduction is not called a confirmation', BANK, 'THE BANKED RESULTS ARE CONFIRMED.'),
    ('no new first-level value is claimed', BANK, 'A NEW FIRST-LEVEL VALUE IS COMPUTED.'),
    ('nothing is claimed compiled', BANK, 'A TERMINAL IS BUILT.'),
    ('the next computation is not claimed done', BANK, 'THE SCALING TRACE IS COMPUTED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the archimedean place is not reached', BANK, 'THE ARCHIMEDEAN PLACE IS REACHED.'),
]

TOOLNUM = [
    ("the instrument's frames, transform, conditions, dilation and fold counts",
     'tools/b308_local_field.py'),
    ("the components' every reported number and every verdict", 'tools/b308_reproduction.py'),
    ("the family's conditions, dimension and chart", 'tools/b303_family.py'),
    ("the projection, the trace and the smear", 'tools/b304_smearing.py'),
    ("the operator A at k = n", 'tools/e16/b281_compression.py'),
    ("the criterion and its registered witnesses", 'tools/e16/b295_second_mechanism.py'),
    ("the cyclotomic re-valuation of a witness", 'tools/e16/b294_family_value.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits and their attribution", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b308_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b308_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b308_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b308_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b308' in x)

# ### ### **`G-EXACT`'s PATTERNS.** ### A float literal, and the two operators that manufacture one
# ### out of integers. ### **THE `/` ARM IS THE ONE THAT MATTERS**: in Python 3 `1 / 2` is a float
# ### even between integers, and a single one of those inside a verdict would make the whole column
# ### an approximation while every printed value still looked exact.
# ### ### **THE EXPONENT TAIL IS OPTIONAL AND ITS ABSENCE WAS A HOLE THIS GATE'S OWN FIXTURE FOUND
# ### ### ON THE FIRST RUN.** ### The first pattern was `\d+\.\d+` OR `\d+[eE][-+]?\d+` as
# ### alternatives, and `1.5e-6` -- the exact literal b307's own arithmetic used -- matched NEITHER:
# ### the first arm's trailing lookahead met the `e`, and the second arm's lookbehind met the `.`.
# ### ### **A FLOAT-CATCHER THAT MISSES A FLOAT IN SCIENTIFIC NOTATION IS THE UNDER-REPORT
# ### ### DIRECTION `ferry_scan.py`'s header NAMES AS THE DANGEROUS ONE**, because its output reads
# ### clean. ### The fixture is the only reason it was seen, and it is kept beside the pattern.
FLOAT_LIT = re.compile(r'(?<![\w.])\d+\.\d+(?:[eE][-+]?\d+)?(?![\w.])'
                       r'|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])')
FLOAT_CALL = re.compile(r'\bfloat\s*\(|\bmath\.|\bnumpy\b|\bnp\.')


# ### **BACKSLASH-ESCAPED QUOTES ARE PART OF THE LITERAL, AND THE FIRST VERSION OF THIS PATTERN DID
# ### NOT KNOW THAT.** ### One prose line -- a `rec(...)` whose text contains `b21\'s` -- closed its
# ### literal early and leaked its `p^{-1/2}` through as an arithmetic division. ### **A LEAK OF ONE
# ### IS STILL A WRONG COUNT, AND THE FIX IS IN THE PATTERN RATHER THAN IN A SENTENCE EXCUSING IT.**
STRINGS = re.compile(r"'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"")
DIVSHAPE = re.compile(r'[^/\s]\s*/\s*[^/\s]')


def _strip_strings(line):
    """### **STRING LITERALS BLANKED, SO A `/` INSIDE PRINTED PROSE IS NOT COUNTED AS ARITHMETIC.**

    ### ### **THE FIRST DRAFT OF THIS GATE COUNTED THEM ALL AND THIS SEAT WROTE A SENTENCE SAYING
    ### ### `every one divides Fractions`. ### THAT SENTENCE WAS FALSE OF MOST OF THEM** -- they are
    ### `%d/%d` format specifiers and the prose `p^{-r}Z_p / p^s Z_p`, which are not divisions at
    ### all. ### The fix is to make the split mechanical rather than to soften the sentence, which is
    ### the same repair (4c) needed and for the same reason.
    """
    return STRINGS.sub(lambda m: ' ' * len(m.group(0)), line)


def exact_scan(path):
    """### RETURNS `(float_literal_sites, float_call_sites, arithmetic_div_sites)`.

    ### ### **`Fraction / Fraction` IS EXACT AND `int / int` IS NOT**, and no scanner reading text
    ### can tell them apart. ### So the `/` arm is reported as SITES TO READ rather than as a
    ### verdict, and the reading is printed beside them. ### **A SCANNER THAT PRONOUNCED ON THIS
    ### WOULD BE PRONOUNCING ON TYPES IT CANNOT SEE.**
    """
    lits, calls, divs = [], [], []
    for i, line in enumerate(io.open(path, encoding='utf-8', errors='replace').read().splitlines(),
                             1):
        s = line.strip()
        if s.startswith('#'):
            continue
        if FLOAT_LIT.search(_strip_strings(line)):
            lits.append((i, s))
        if FLOAT_CALL.search(_strip_strings(line)):
            calls.append((i, s))
        if DIVSHAPE.search(_strip_strings(line)):
            divs.append((i, s))
    return lits, calls, divs


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b308 -- GATE SUITE (AN INSTRUMENT BUILD)')
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
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

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

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()

    # ### G-FALSIFIER -- the three registered ones, read off the runner's own verdict block.
    print('\n  G-FALSIFIER (the three registered falsifiers, read off the runner):')
    fired = [ln for ln in run.splitlines() if 'FIRED** ###' in ln and 'DID NOT FIRE' not in ln]
    zero = '### CHECKS FAILING : 0' in run
    print('    falsifiers that FIRED : %d ; runner reports zero checks failing : %s'
          % (len(fired), zero))
    for ln in fired:
        print('        ### %s' % ln.strip())
    print('    ### **AND THE HONEST READING: THREE FALSIFIERS THAT ALL HELD HAVE CAUGHT NOTHING.**')
    print('    ### The suite does not treat that as evidence, and the bank says so in its own text.')
    if fired or not zero:
        fails.append('G-FALSIFIER')

    # ### G-REPRO -- the reproduction's own counts, read off the runner rather than the bank.
    print('\n  G-REPRO (the reproduction, read off the RUN and not off the prose):')
    checks = [('family set-equality disagreements', 'DISAGREEING : 0'),
              ('dimension law disagreements', 'THE LAW IN ITS OWN TESTED RANGE : 0'),
              ('criterion members reached and disagreements', 'MEMBERS REACHED : 80'),
              ('criterion disagreements', '### DISAGREEING : 0   ### FORCED ZEROS CONFIRMED : 50'),
              ('owner sentences unpullable at the run', '### UNPULLABLE : 0'),
              ('the fold: two routes and a zero instrument column',
               'THE INSTRUMENT FOLDS ANYTHING : 0'),
              ('nothing escaped nowhere -- the positive arm', 'CELLS WHERE NOTHING ESCAPED : 0'),
              ('undeclared sites in the operational path',
               "UNDECLARED SITES IN THE INSTRUMENT'S OPERATIONAL PATH : 0")]
    for lbl, anchor in checks:
        ok = anchor in run
        print('    %-52s %s' % (lbl, 'PASS' if ok else '### FAIL ### anchor=%r' % anchor))
        if not ok:
            fails.append('G-REPRO: %s' % lbl)

    # ### G-EXACT -- ### **THIS ACT'S OWN, AND IT MEASURES A CAP THAT WOULD OTHERWISE BE A PROMISE.**
    print('\n  G-EXACT (zero float tokens in any deciding path):')
    tot_lit, tot_call = 0, 0
    for path in (INSTRUMENT, RUNNER):
        lits, calls, divs = exact_scan(path)
        tot_lit += len(lits)
        tot_call += len(calls)
        print('    %-30s float literals : %d   float-producing calls : %d   '
              'arithmetic `/` sites : %d'
              % (os.path.basename(path), len(lits), len(calls), len(divs)))
        for i, s in lits + calls:
            print('        ### line %-5d %s' % (i, s[:88]))
        for i, s in divs:
            print('        `/` line %-5d %s' % (i, s[:88]))
    print('    ### **THE `/` SITES ARE REPORTED AND NOT JUDGED**: `Fraction / Fraction` is exact and')
    print('    ### `int / int` is not, and no scanner reading text can tell them apart, so each is')
    print('    ### PRINTED IN FULL for a reader. ### **STRING LITERALS ARE BLANKED FIRST**, because')
    print('    ### the first draft counted `%d/%d` format specifiers and printed prose as divisions')
    print('    ### and this seat wrote a sentence that was false of most of them. ### **THE READING')
    print('    ### OF WHAT REMAINS IS THIS SEAT\'S, NOT THE SCANNER\'S.**')
    # ### THE FIXTURE, BOTH POLARITIES. ### A scanner that never fires is not a scanner.
    fx_lit = bool(FLOAT_LIT.search('    tol = 1.5e-6'))
    fx_lit2 = bool(FLOAT_LIT.search('    x = 0.5'))
    fx_quiet = not bool(FLOAT_LIT.search('    v = Fraction(1, p ** 2)'))
    fx_call = bool(FLOAT_CALL.search('    y = float(z)'))
    fx_call_q = not bool(FLOAT_CALL.search('    y = Fraction(z)'))
    print('    fixture: catches `1.5e-6` %s, catches `0.5` %s, quiet on `Fraction(1, p ** 2)` %s'
          % (fx_lit, fx_lit2, fx_quiet))
    print('    fixture: catches `float(z)` %s, quiet on `Fraction(z)` %s' % (fx_call, fx_call_q))
    ok_exact = (tot_lit == 0 and tot_call == 0
                and fx_lit and fx_lit2 and fx_quiet and fx_call and fx_call_q)
    print('    float literals %d   float-producing calls %d   %s'
          % (tot_lit, tot_call, 'PASS' if ok_exact else '### FAIL ###'))
    if not ok_exact:
        fails.append('G-EXACT')

    # ### G-NONEW -- ### **THIS ACT'S OWN, AND IT MEASURES THE ORDER'S SHARPEST RESTRICTION.**
    print('\n  G-NONEW (no first-level value at a cell or member the record does not carry):')
    print('    ### The runner prints a first-level NUMBER in exactly one place -- (3f) -- and every')
    print('    ### such line must name the owning tool that also produces it.')
    val_lines = [ln for ln in run.splitlines() if '<A f, f>' in ln]
    named = [ln for ln in val_lines if 'producer:' in ln]
    banked_only = all(('banked' in ln) for ln in val_lines)
    print('    lines printing a first-level value : %d ; naming their producer : %d ; all banked : %s'
          % (len(val_lines), len(named), banked_only))
    for ln in val_lines:
        print('        %s' % ln.strip()[:96])
    ok_nonew = (len(val_lines) > 0 and len(named) == len(val_lines) and banked_only)
    print('    %s' % ('PASS' if ok_nonew else '### FAIL ###'))
    print('    ### **AND THE ARM THAT MAKES IT MEAN SOMETHING: THE COUNT IS NOT ZERO.** ### A run')
    print('    ### that printed no value at all would pass a cap on new values while also having')
    print('    ### failed to reproduce the two the record carries.')
    if not ok_nonew:
        fails.append('G-NONEW')

    # ### G-PAPERS -- ### **INVERTED BACK: NOTHING MOVES THERE THIS ACT.**
    print('\n  G-PAPERS (INVERTED BACK: the papers repo is NOT touched this act):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    print('    tracked files changed in PLACE-papers : %d %s  %s'
          % (len(tracked), [x[3:].strip() for x in tracked],
             'PASS' if not tracked else '### FAIL ###'))
    print('    ### **A GATE COPIED FORWARD FROM b307 UNINVERTED WOULD HAVE FAILED THIS ACT FOR NOT')
    print('    ### TOUCHING A REPOSITORY IT WAS NEVER ASKED TO TOUCH**, and the inversion is')
    print('    ### recorded because copying a green gate forward is how a suite stops checking.')
    if tracked:
        fails.append('G-PAPERS')

    # ### G-NOBUILD.
    print('\n  G-NOBUILD (nothing built; the profile does not move):')
    prof = io.open(PROFILE, 'rb').read()
    phead = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'],
                           capture_output=True).stdout
    identical = (prof == phead)
    dirty = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                           capture_output=True, text=True).stdout.strip()
    lean_rows = [x for x in dirty.splitlines() if x.strip().endswith('.lean')]
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    print('    profile BYTE-IDENTICAL to git HEAD : %s ; `.lean` changed : %d ; prints : %d'
          % (identical, len(lean_rows), len(lines)))
    if not identical or lean_rows:
        fails.append('G-NOBUILD')

    # ### G-ANCESTOR.
    print('\n  G-ANCESTOR (no ancestor correspondence row rewritten):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    prefix = now.startswith(head.rstrip('\n'))
    print('    committed table is a TRUE PREFIX of the current one : %s  %s'
          % (prefix, 'PASS' if prefix else '### FAIL ###'))
    if not prefix:
        fails.append('G-ANCESTOR')

    # ### G-NOMOVE.
    print('\n  G-NOMOVE (an instrument build moves no grade and re-verdicts nothing):')
    mv = re.compile(r'\b(grade moves to|we promote|promoted to derives|is now derived|'
                    r'this act re-verdicts)\b', re.I)
    mhits = [ln for ln in bank.splitlines() if mv.search(ln)]
    says = 'NO GRADE MOVED' in bank and 'NO ACT' in bank
    dpos = bool(mv.search('and b304 is now derived'))
    print('    grade-moving lines : %d ; both refusals present : %s ; discrimination : %s'
          % (len(mhits), says, dpos))
    if mhits or not says or not dpos:
        fails.append('G-NOMOVE')

    # ### G-STRUCK.
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(e['patterns']) for e in struck), unconf))
    total, scanned = 0, 0
    for p in OWNED + [BANK, REG]:
        if not os.path.exists(p):
            continue
        scanned += 1
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                     struck, stem_list)
        total += len(ch)
        if ch:
            print('    ### %-40s hits : %d' % (os.path.basename(p), len(ch)))
            for h in ch:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d  %s'
          % (scanned, total, 'PASS' if not total else '### FAIL ###'))
    for p, why in CARRIERS:
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), struck, stem_list)
        print('    %-30s hits : %d  ### DECLARED CARRIER -- %s'
              % (os.path.basename(p), len(ch), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        hit = bool(ferry_scan.scan_text(text, struck, stem_list)[0])
        fired_disc += 1 if hit else 0
        print('    DISCRIMINATION %-4s comes back hit : %s  %s'
              % (eid, hit, 'PASS' if hit else '### FAIL ###'))
    if total or fired_disc != 3:
        fails.append('G-STRUCK')

    # ### G-STEM at the extended scope.
    print('\n  G-STEM (this act\'s files, EXCEPT the declared carriers):')
    stem_total, swept = 0, 0
    for p in OWNED + [BANK, REG]:
        if not os.path.exists(p):
            continue
        swept += 1
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                      [], stem_list)
        stem_total += len(sh)
        if sh:
            print('    ### %-40s stem hits : %d' % (os.path.basename(p), len(sh)))
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    for p, why in CARRIERS:
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), [], stem_list)
        print('    %-30s stem hits : %d  ### CARRIER -- %s' % (os.path.basename(p), len(sh), why))
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    files swept %d   stem hits %d   control fires %s   %s'
          % (swept, stem_total, ctrl, 'PASS' if not stem_total and ctrl else '### FAIL ###'))
    if stem_total or not ctrl:
        fails.append('G-STEM')

    print('\n  G-SHARED (the extended sweep over the shared append-targets):')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s' % sorted(got))
    print('    ### **THE EXCEPTION LIST, WITH ITS REASONS, PRINTED BECAUSE IT IS PRINTED:**')
    print('    ### `row 2` predates the ban (b142), so it is not a defect at all -- a ban is not')
    print('    ### retroactive. ### `row 101` is b284\'s, a defect when written that the old sweep')
    print('    ### could not see, FILED AND NOT REWRITTEN under the append-only law.')
    print('    UNEXPECTED : %d %s  %s'
          % (len(extra), sorted(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-56s %-38s exists=%s tracked=%s' % (what[:56], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-SEAL:')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    print('    seal intact : %s  %s' % (intact, 'PASS' if intact else '### FAIL ###'))
    if not intact:
        fails.append('G-SEAL')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            print('        ### %d flagged sentence(s) -- DESCRIBED, NOT QUOTED, so this log does'
                  % len(gh))
            print('        ### not itself acquire the shape it is reporting.')

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 12 + len(checks)
    print('\n' + '=' * 100)
    print('### COUNTS, PRINTED BY THIS TOOL SO THE BANK NEVER TYPES ONE AT A SHELL:')
    print('    owner needles %d   self needles %d   must-fail fixtures %d   G-REPRO anchors %d'
          % (len(OWNER_NEEDLES), len(SELF_NEEDLES), len(MUST_FAIL), len(checks)))
    print('    declared carriers %d   toolnum rows %d   correspondence-table rows scanned by'
          ' G-ANCESTOR: the whole file' % (len(CARRIERS), len(TOOLNUM)))
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
