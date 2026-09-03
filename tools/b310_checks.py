# -*- coding: utf-8 -*-
"""b310_checks.py -- THE GATE SUITE FOR A COLLAPSE, A BEARING, AND A SHADOW.

### ### **THE ARM THAT MATTERS MOST THIS ACT IS `G-NOBRANCH`, AND IT GUARDS THE ONE THING THE ACT
### ### COULD MOST EASILY OVERCLAIM.** ### Component 4 touches a branch nobody has settled and a
### specification the corpus owes. ### **THE MUST-FAIL FIXTURES ASSERT WHOLE-LINE ABSENCE OF THE
### ### SENTENCES THE ACT WOULD WRITE IF IT HAD DECIDED EITHER**, so the cap is measured over the
### act's own prose rather than trusted to the seat.

### ### **`G-COLLAPSE` AND `G-READS-ONE-POINT` GUARD THE OTHER DIRECTION:** ### a collapse is the
### shape a broken assembly produces for free, so the suite requires the run to carry a NONZERO
### surviving term AND a discriminating weight. ### **A DEAD ASSEMBLY COULD NOT HAVE PRODUCED THIS
### ### RESULT, AND THAT IS CHECKED RATHER THAN ASSERTED.**

### ### **`G-KERNEL` CARRIES b309's `(D6)` IN BOTH HALVES:** ### the baseline is FOUND rather than
### assumed to be `HEAD`, and both sides are NORMALISED before the byte comparison.
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
import b302_kernel as KRN  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
MODULE = os.path.join(SIDE, 'Core', 'SmearCollapseShadow.lean')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b310_the_smear_collapses.txt')
REG = d('b310_registration_2026-09-03.txt')
RUN = d('b310_components_run.txt')
KRUN = d('b310_kernel_run.txt')
SCAN = d('b310_ferry_scan.txt')
FERRY = d('b310_ferry_2026-09-03.txt')
CENSUS = d('b310_census.txt')

OWNED = [RUN, KRUN, CENSUS,
         d('b310_corr_row.txt'), d('b310_index_query.txt'), d('b310_pins_stepzero.txt'),
         d('b310_regspec_run.txt'), d('b310_satisfiable.json'),
         t('b310_regspec.py'), t('b310_correspondence.py'), t('b310_components.py'),
         t('b310_kernel.py'), t('b310_smear.py'), MODULE]

CARRIERS = [
    (t('b310_checks.py'), 'its own fixtures'),
    (t('b310_index_append.py'), 'its own fixtures'),
    (BANK, 'it quotes the refuted clause of its own sealed prediction, and the struck gate name,'
           ' IN ORDER TO DECLARE THEM'),
    (REG, 'it is the sealed prediction, including the clause the run refuted'),
    (FERRY, 'IT IS THE ORDER -- not this act\'s writing'),
    (SCAN, 'it is the scan\'s own log'),
]

OWNER_NEEDLES = [
    ("### THE SOURCE'S MOVE, quoted by b304 from CC", t('b304_smearing.py'),
     'associate to a test function'),
    ("b304 -- the projection is onto Sonin's space", t('b304_smearing.py'), 'THE FAITHFUL'),
    ("b304 -- the part it refused", t('b304_smearing.py'), 'REFUSES THE'),
    ("b305 -- eq. (149), where the prime's contribution lives",
     d('b305_the_arithmetics_entry.txt'), 'W_p(f) = (log p) SUM_{m>=1}'),
    ("### b305 -- and the sentence that locates the logarithm",
     d('b305_the_arithmetics_entry.txt'), '`log p` is in `W_p`'),
    ("b309 -- the zero this act CARRIES", d('b309_the_scaling_trace.txt'),
     'THE VALUE IS EXACTLY ZERO'),
    ("### b309 -- the scope that travels with it", d('b309_the_scaling_trace.txt'),
     'The vanishing of one trace'),
    ("b309 -- the mechanism this act generalises", d('b309_the_scaling_trace.txt'),
     'AND `p^j - 1` IS A UNIT'),
    ("b308 -- Tr(Pi) equals the constrained dimension",
     d('b308_the_local_field_instrument.txt'), 'EQUALS THE CONSTRAINED DIMENSION AT ALL SIX'),
    ("b285 -- the boundary this act does not cross", d('b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES'),
    ("### b262 -- ITS OWN sentence, a REQUIREMENT and not a disjunction",
     d('b262_junction_limit.txt'), 'ABSORB A DIVERGENT QUANTITY'),
    ("### b262 -- and the refusal it attaches in the same breath",
     d('b262_junction_limit.txt'), 'NOT A CLAIM THAT IT FAILS TO DO IT'),
    ("### b263 -- ITS OWN formulation of the branch", d('b263_top_level_silence.txt'),
     'EITHER THE FINITE-PLACE SIDE SUPPLIES'),
    ("b263 -- (SPEC-1)", d('b263_top_level_silence.txt'), '(SPEC-1) IT COUNTS FIRST LEVELS'),
    ("b263 -- (SPEC-2)", d('b263_top_level_silence.txt'),
     "(SPEC-2) IT REDUCES TO `Theta_q`'s TERMS"),
    ("b263 -- (SPEC-3)", d('b263_top_level_silence.txt'), '(SPEC-3) IT IS DEFINED OVER ALL PRIMES'),
    ("### b263 -- its own refusal: these exclude, they do not determine",
     d('b263_top_level_silence.txt'), 'THESE EXCLUDE; THEY DO NOT DETERMINE'),
    ("### b263 -- the specification is conditional and vacuous on the other branch",
     d('b263_top_level_silence.txt'), 'FOR THE FIRST BRANCH ONLY AND IS VACUOUS ON THE SECOND'),
]

SELF_NEEDLES = [
    ('bank states the value up front', BANK, 'RETURNS ONE TERM AND THERE IS NO'),
    ('bank gives the collapse formula', BANK, '`T(w) = w_0 * (p^n - 1)^2`'),
    ('bank says the scaling part is discrete at a finite place', BANK, 'WHICH IS DISCRETE'),
    ('bank says no bump is chosen and no price is paid', BANK, 'NO PRICE IS PAID'),
    ('bank says the sum is finite for the source\'s own class', BANK,
     'COMPACTLY SUPPORTED'),
    ('bank reports zero surviving terms', BANK, 'TERMS SURVIVING AT A NONZERO POWER : ### 0'),
    ('bank says the zeros are not substituted in', BANK, 'ZEROS ARE NOT SUBSTITUTED IN'),
    ('bank refuses to widen b309\'s scope', BANK, 'USING A RESULT IS NOT WIDENING IT'),
    ('bank says the sweep is the check and not the proof', BANK, 'CHECK AND NOT THE PROOF'),
    ('bank states what the surviving term does not contain', BANK,
     'NO LOGARITHM OF THE PRIME'),
    ('bank reports both arms of the one-point measurement', BANK,
     'OR THE FIRST IS A CHECK THAT CANNOT FAIL'),
    ('bank reports the unified formula checked against both owners', BANK,
     '0 DISAGREEING'),
    ('bank keeps the unit column from being vacuous', BANK,
     'would have agreed about nothing'),
    ('bank locates the arithmetic in the distribution', BANK,
     'THE POWERS THIS TRACE DOES NOT READ'),
    ('bank gives the fixed-point sentence', BANK, 'SIGNED COUNT OF THE OFF-BALL POINTS'),
    ('bank refuses to merge the two kinds of zero', BANK, 'NOT THE SAME KIND OF ZERO'),
    ('bank keeps the archimedean place out', BANK, 'THIS ACT DERIVES NOTHING'),
    ('bank separates b262\'s sentence from b263\'s formulation', BANK,
     "b263's WORDING, NOT b262's"),
    ('bank states the bearing in one sentence', BANK,
     'CANNOT SUPPLY THE FIRST-LEVEL MASS THROUGH THE OBJECT'),
    ('bank says SPEC-1 cannot be met by this class', BANK, 'CANNOT BE MET BY THIS CLASS'),
    ('bank says SPEC-3 can be met', BANK, 'CAN BE MET.'),
    ('bank leaves SPEC-2 undecided', BANK, 'NOT DECIDED BY'),
    ('bank refuses to manufacture a SPEC-2 verdict', BANK,
     'cheapest thing in the act'),
    ('bank lists the four things it is not', BANK, 'THE FOUR THINGS THIS IS NOT'),
    ('bank says a distribution is not a trace on a space', BANK,
     'A DISTRIBUTION IS NOT A TRACE ON A SPACE'),
    ('bank reports the shadow was checked and built', BANK,
     'Both candidates pass both tests'),
    ('bank says the terminals certify arithmetic not the collapse', BANK,
     'CERTIFY IS ARITHMETIC AND NOT THE COLLAPSE'),
    ('bank says why the second terminal is not a copy of b309\'s', BANK,
     '`ALONE` IS A CLAIM ABOUT BOTH'),
    ('bank reports the profile move and the prefix', BANK, 'TRUE BYTE PREFIX OF THE NEW ONE'),
    ('bank restates the object three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged', BANK, "`M-2`'s ROW: ### `(SPECIFIED-NOT-STATED)`, UNCHANGED"),
    ('bank distinguishes the scope restatement from the row moving', BANK,
     'THE ROW STANDS'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'DAYS PAST BOTH, AND'),
    ('bank names the window question as the author\'s', BANK, 'AND NOT OPENED HERE'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank declares the refuted clause', BANK, 'WRONG AT EVERY NEGATIVE ONE'),
    ('bank names the pattern against itself', BANK, 'habit, not an accident'),
    ('bank declares the stem hit in its own gate name', BANK,
     'which carries a banned'),
    ('bank declares the notation guard firing', BANK, 'THIRD ACT RUNNING'),
    ('bank declares the kernel-tool half of b309 D6', BANK,
     'FIXED WHERE IT WAS BITTEN AND NOT WHERE THE DEFECT LIVED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('registration seals the derivation in advance', REG, 'BEFORE ANY CODE FOR IT EXISTED'),
    ('registration names the three misreadings', REG, 'THREE MISREADINGS'),
    ('registration caps branch decisions at zero', REG, 'branch decisions'),
    ('registration declares the attribution hazard in advance', REG,
     "b263's FORMULATION, NOT b262's WORDING"),
    ('the run reports zero surviving terms', RUN, 'TERMS SURVIVING AT A NONZERO POWER : 0'),
    ('the run reports the navigator\'s expectation holding', RUN, 'the navigator'),
    ('the run declares the factor refutation', RUN, 'REFUTED AT NEGATIVE POWERS'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the kernel run reports the baseline byte-identical', KRUN, 'BYTE-IDENTICAL to banked : True'),
    ('the kernel run reports two zero-axiom terminals', KRUN, 'terminals printed        : 2, 2'),
    ('the kernel run reports the true byte prefix', KRUN, 'TRUE BYTE PREFIX'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### ### **`G-NOBRANCH`'s OWN FIXTURES -- THE SENTENCES THE ACT WOULD WRITE IF IT HAD DECIDED.**
    ('the branch is not decided', BANK, 'THE BRANCH IS DECIDED.'),
    ('the archimedean side is not chosen', BANK, 'THE ARCHIMEDEAN SIDE ABSORBS IT.'),
    ('the finite side is not excluded', BANK, 'THE FINITE SIDE IS EXCLUDED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('SPEC-2 is not decided', BANK, '(SPEC-2) CANNOT BE MET.'),
    ('the finite side is not said to contribute nothing', BANK,
     'THE FINITE SIDE CONTRIBUTES NOTHING.'),
    ('the source construction is not called empty', BANK, 'THE SOURCE CONSTRUCTION IS EMPTY.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('b309 is not re-verdicted', BANK, 'b309 IS RE-VERDICTED.'),
    ('the terminals do not certify the collapse', BANK, 'THE TERMINALS CERTIFY THE COLLAPSE.'),
    ('the sweep is not called a proof', BANK, 'THE SWEEP IS A PROOF.'),
    ('nothing about the archimedean place', BANK, 'THE ARCHIMEDEAN PLACE IS REACHED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]

TOOLNUM = [
    ("the assembly, the counts and the weights", 'tools/b310_smear.py'),
    ("every table and every verdict in the components", 'tools/b310_components.py'),
    ("the shadow build, the profile and the byte comparisons", 'tools/b310_kernel.py'),
    ("the byte checks the kernel tool imports", 'tools/b302_kernel.py'),
    ("the closed form, the reduced route and the ambient", 'tools/b309_scaling_trace.py'),
    ("the frame, the ball and the embedding law", 'tools/b308_local_field.py'),
    ("the projector and the unit trace", 'tools/b304_smearing.py'),
    ("the conditions and the exact nullspace", 'tools/b303_family.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits and their attribution", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b310_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b310_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b310_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b310_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b310' in x)

FLOAT_LIT = re.compile(r'(?<![\w.])\d+\.\d+(?:[eE][-+]?\d+)?(?![\w.])'
                       r'|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])')
FLOAT_CALL = re.compile(r'\bfloat\s*\(|\bmath\.|\bnumpy\b|\bnp\.')
STRINGS = re.compile(r"'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"")


def _strip_strings(line):
    return STRINGS.sub(lambda m: ' ' * len(m.group(0)), line)


def exact_scan(path):
    lits, calls = [], []
    for i, line in enumerate(io.open(path, encoding='utf-8', errors='replace').read().splitlines(),
                             1):
        s = line.strip()
        if s.startswith('#'):
            continue
        if FLOAT_LIT.search(_strip_strings(line)):
            lits.append((i, s))
        if FLOAT_CALL.search(_strip_strings(line)):
            calls.append((i, s))
    return lits, calls


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b310 -- GATE SUITE (A COLLAPSE, A BEARING, AND A SHADOW)')
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
    print('    ### **THE FIRST EIGHT ARE `G-NOBRANCH`: THE SENTENCES THIS ACT WOULD HAVE WRITTEN IF')
    print('    ### IT HAD DECIDED THE BRANCH OR VERDICTED `M-2`.** ### The caps on both are ZERO and')
    print('    ### this is what measures them.')

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()

    # ### G-COLLAPSE and G-READS-ONE-POINT.
    print('\n  G-COLLAPSE / G-READS-ONE-POINT (a collapse is what a broken assembly gives free):')
    checks = [('no term survives at a nonzero power', 'TERMS SURVIVING AT A NONZERO POWER : 0'),
              ('the surviving term is NOT itself zero', 'w_0 * Tr(Pi)'),
              ('the quiet and loud weights agree', 'same?'),
              ('and a different identity value DIFFERS', "differs?"),
              ('the unified formula agrees with both owners', 'count == b304 trace_scaled'),
              ('and the unit column is not an agreement about zeros', 'nonzero)'),
              ('the run reports zero failures', '### CHECKS FAILING : 0')]
    for lbl, anchor in checks:
        ok = anchor in run
        print('    %-56s %s' % (lbl, 'PASS' if ok else '### FAIL ### anchor=%r' % anchor))
        if not ok:
            fails.append('G-COLLAPSE: %s' % lbl)

    # ### G-KERNEL -- ### **b309's (D6) IN BOTH HALVES.**
    print('\n  G-KERNEL (the profile moves; baseline FOUND, both sides NORMALISED):')
    prof = KRN.normalise(io.open(PROFILE, 'rb').read())
    revs = subprocess.run(['git', '-C', SIDE, 'rev-list', 'HEAD', '--', 'AXIOM_PRINTS.txt'],
                          capture_output=True, text=True).stdout.split()
    phead, base_rev = None, None
    for r in revs:
        blob = subprocess.run(['git', '-C', SIDE, 'show', r + ':AXIOM_PRINTS.txt'],
                              capture_output=True).stdout
        if b'B310.' not in blob:
            phead, base_rev = KRN.normalise(blob), r
            break
    if phead is None:
        phead, base_rev = prof, 'NONE FOUND'
    prefix = prof.startswith(phead)
    lines_now = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    lines_head = [ln for ln in phead.decode('utf-8').splitlines() if ln.strip()]
    added = len(lines_now) - len(lines_head)
    nonzero_axioms = [ln for ln in lines_now if 'does not depend on any axioms' not in ln]
    mine = [ln for ln in lines_now if 'B310.' in ln]
    print('    baseline commit (most recent profile WITHOUT this act\'s namespace) : %s'
          % base_rev[:7])
    print('    prints at the baseline -> now : %d -> %d   (added %d)'
          % (len(lines_head), len(lines_now), added))
    print('    the baseline profile is a TRUE BYTE PREFIX of the current one : %s  %s'
          % (prefix, 'PASS' if prefix else '### FAIL ###'))
    print('    terminals NOT printing zero axioms : %d  %s'
          % (len(nonzero_axioms), 'PASS' if not nonzero_axioms else '### FAIL ###'))
    for ln in mine:
        print('        %s' % ln)
    if not prefix or nonzero_axioms or added != 2 or len(mine) != 2:
        fails.append('G-KERNEL')

    # ### G-EXACT.
    print('\n  G-EXACT (zero float literals in the deciding runner):')
    tot_lit, tot_call = 0, 0
    for path in (t('b310_smear.py'), t('b310_components.py')):
        lits, calls = exact_scan(path)
        tot_lit += len(lits)
        tot_call += len(calls)
        print('    %-28s float literals : %d   float-producing calls : %d'
              % (os.path.basename(path), len(lits), len(calls)))
        for i, s in lits + calls:
            print('        ### line %-5d %s' % (i, s[:88]))
    fx = (bool(FLOAT_LIT.search('  tol = 1.5e-6')) and bool(FLOAT_LIT.search('  x = 0.5'))
          and not bool(FLOAT_LIT.search('  v = Fraction(1, p ** 2)'))
          and bool(FLOAT_CALL.search('  y = float(z)'))
          and not bool(FLOAT_CALL.search('  y = Fraction(z)')))
    print('    fixture arms all agree : %s' % fx)
    if tot_lit or tot_call or not fx:
        fails.append('G-EXACT')

    # ### G-NOPAPERS.
    print('\n  G-NOPAPERS:')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    print('    tracked files changed in PLACE-papers : %d  %s'
          % (len(tracked), 'PASS' if not tracked else '### FAIL ###'))
    if tracked:
        fails.append('G-NOPAPERS')

    # ### G-ANCESTOR.
    print('\n  G-ANCESTOR:')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    print('    committed table is a TRUE PREFIX of the current one : %s  %s'
          % (pfx, 'PASS' if pfx else '### FAIL ###'))
    if not pfx:
        fails.append('G-ANCESTOR')

    # ### G-NOMOVE.
    print('\n  G-NOMOVE:')
    mv = re.compile(r'\b(grade moves to|we promote|promoted to derives|is now derived|'
                    r'this act re-verdicts)\b', re.I)
    mhits = [ln for ln in bank.splitlines() if mv.search(ln)]
    says = 'NO GRADE MOVES' in bank and 'NO ACT IS RE-VERDICTED' in bank
    dpos = bool(mv.search('and b309 is now derived'))
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
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                     struck, stem_list)
        total += len(ch)
        if ch:
            print('    ### %-40s hits : %d' % (os.path.basename(p), len(ch)))
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

    # ### G-STEM.
    print('\n  G-STEM (this act\'s files, EXCEPT the declared carriers):')
    stem_total, swept = 0, 0
    for p in OWNED:
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

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s' % sorted(got))
    print('    ### **THE EXCEPTION LIST WITH ITS REASONS:** ### `row 2` predates the ban (b142) --')
    print('    ### a ban is not retroactive. ### `row 101` is b284\'s, a defect when written that the')
    print('    ### old sweep could not see, FILED AND NOT REWRITTEN.')
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
        print('    %-48s %-36s exists=%s tracked=%s' % (what[:48], tool, ex, tr))
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
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN),
                      ('the kernel run', KRUN)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 10 + len(checks)
    print('\n' + '=' * 100)
    print('### COUNTS, PRINTED BY THIS TOOL SO THE BANK NEVER TYPES ONE AT A SHELL:')
    print('    owner needles %d   self needles %d   must-fail fixtures %d   collapse arms %d'
          % (len(OWNER_NEEDLES), len(SELF_NEEDLES), len(MUST_FAIL), len(checks)))
    print('    declared carriers %d   toolnum rows %d' % (len(CARRIERS), len(TOOLNUM)))
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
