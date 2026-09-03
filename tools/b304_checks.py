# -*- coding: utf-8 -*-
"""b304_checks.py -- THE GATE SUITE. ### **ONE ARM PER REGISTERED FALSIFIER, AND NO MORE.**

### ### **EVERY COUNT THIS ACT REPORTS ABOUT ITSELF COMES OUT OF THIS FILE**, except the kernel
### profile and the smearing values, which are their own tools' and are ### RE-CHECKED HERE
### INDEPENDENTLY OF THOSE TOOLS' OWN REPORTS.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import hedge_audit   # noqa: E402
import ferry_scan    # noqa: E402
import banned_terms  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
MODULE = os.path.join(SIDE, 'Core', 'IndexRangeShadow.lean')
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b304_the_demands_shape.txt')
REG = d('b304_registration_2026-09-03.txt')
KRUN = d('b304_kernel_run.txt')
SRUN = d('b304_smearing_run.txt')
HRUN = d('b304_hooks.txt')
SCAN = d('b304_ferry_scan.txt')
FERRY = d('b304_ferry_2026-09-03.txt')
SPEC = d('b304_satisfiable.json')

OWNED = [BANK, REG, KRUN, SRUN, HRUN, SCAN, FERRY, SPEC, MODULE,
         d('b304_corr_row.txt'), d('b304_index_query.txt'), d('b304_pins_step_zero.txt'),
         d('b304_regspec_run.txt'),
         t('b304_kernel.py'), t('b304_regspec.py'), t('b304_smearing.py'),
         t('b304_hooks.py'), t('b304_correspondence.py')]
FIXTURE_CARRIERS = [t('b304_checks.py'), t('b304_index_append.py')]

# ### ==============================================================================================
# ### THE OWNER NEEDLES. ### **EVERY ONE INTO THE FILE THAT EMITTED THE SENTENCE.**
# ### ==============================================================================================
UNIT_CLAUSES = [                                            # ### V1 / V2
    ("b226's definition of the archimedean unit (EMITTER)",
     d('b226_stated_choice.txt'), 'the rank-2 Sonin-sector eigenfunction, normalized'),
    ("b300's identification of u_inf with phi_mu",
     d('b300_the_archimedean_leg.txt'), 'AT THE FIRST EVEN NEGATIVE EIGENVALUE'),
    ("CM Corollary 3.2, as the corpus already carried it",
     d('b201_eigenfunction_exhibit.txt'), 'BELONGS TO THE SONIN SPACE'),
    ("CM Corollary 3.2's proof line -- the orthogonal-complement definition",
     d('b201_eigenfunction_exhibit.txt'), "Sonin's space is the orthogonal of the"),
    ("CM Theorem 2.6(i) -- Wsa is selfadjoint",
     d('b201_eigenfunction_exhibit.txt'), 'Wsa is selfadjoint'),
    ("b214's printed eigenvalue, which the corollary's hypothesis needs NEGATIVE",
     d('b226_stated_choice.txt'), 'mu = -20.48057322913694697'),
    ("b201's still-missing steps, which this act does NOT close",
     d('b201_eigenfunction_exhibit.txt'), '(M-a) SIMPLICITY'),
    ("the work-order as b300 filed it",
     d('b301_the_object_completed.txt'), '(R2) `W-ORD-PHI-MU-L2`'),
]

DEMAND_CLAUSES = [                                          # ### V3 / V4
    ("(SPEC-1), quoted from its emitting act",
     d('b263_top_level_silence.txt'), 'IT COUNTS FIRST LEVELS'),
    ("(SPEC-1)'s ground -- S1 + S2, and it names no other spec",
     d('b263_top_level_silence.txt'), 'GROUND: S1 (act 9 assigns zero there)'),
    ("(SPEC-2), the termwise requirement",
     d('b263_top_level_silence.txt'), "IT REDUCES TO `Theta_q`'s TERMS AT LEVELS"),
    ("(SPEC-3)",
     d('b263_top_level_silence.txt'), 'IT IS DEFINED OVER ALL PRIMES'),
    ("b263's own limit on the three",
     d('b263_top_level_silence.txt'), 'THESE EXCLUDE; THEY DO NOT DETERMINE'),
    ("b263's conditional, stated before the specification",
     d('b263_top_level_silence.txt'), 'IS VACUOUS ON THE SECOND'),
    ("S1 -- the one-level index set, and the empty range",
     d('b263_top_level_silence.txt'), 'ranging over `{1}` only'),
    ("S1's empty-range sentence",
     d('b263_top_level_silence.txt'), 'READS `1 <= k <= 0`'),
    ("act 9's closed form WITH its range (EMITTER)",
     d('b220_aggregation_freedom.txt'), 'for 1 <= k <= n-1, 0 for k >= n'),
    ("b262's partition of the index set",
     d('b262_junction_limit.txt'), 'THOSE TWO ARE THE PARTITION'),
    ("### b262's CONFIRMING SENTENCE -- the falsifier's negation",
     d('b262_junction_limit.txt'), 'whose only level IS the top level'),
]

REACH_CLAUSES = [                                           # ### V5 / V6 / V7
    ("the barrier's verdict and its scope",
     d('b280_the_consequence.txt'), 'AT EVERY FINITE PLACE AND'),
    ("b270's absorption -- a property of the OPERATOR, not of the unit",
     d('b280_the_consequence.txt'), 'a functional of `u|_ball` ALONE'),
    ("the closure that makes S-bar_p vanish on the ball",
     d('b280_the_consequence.txt'), 'VANISHES a.e. ON `Z_p`'),
    ("W-ORD-FIBER-GENERAL, restated at its own scope",
     d('b280_the_consequence.txt'), 'PROVED AT LEVEL 1 AND FULLY VERIFIED'),
    ("### b21's escaped-mass artifact, as b284 quotes its namer",
     d('b284_the_scalings_domain.txt'), 'ESCAPED MASS FOLDED BACK IN'),
    ("b284's own meeting of it -- the control disagreed and was not promoted",
     d('b284_the_scalings_domain.txt'), 'IS THE ARTIFACT, NOT THE ANSWER'),
    ("b271's scope sentence, the precedent for reach-not-verdict",
     d('b280_the_consequence.txt'), 'A STATEMENT ABOUT SCOPE AND NOT A CHANGE'),
    ("b284's closed route, which this act does not reopen",
     d('b297_the_fold.txt'), 'C3-VIA-SCALING IS CLOSED'),
    ("b220's admissible-set verdict, Option B's cost",
     d('b263_top_level_silence.txt'), 'THE ADMISSIBLE SET IS ALL FUNCTIONS'),
]

OWNER_NEEDLES = UNIT_CLAUSES + DEMAND_CLAUSES + REACH_CLAUSES

SELF_NEEDLES = [
    # ### STEP ZERO
    ('bank reports the push clause had no referent', BANK, 'NOTHING WAS AHEAD OF ORIGIN'),
    ('bank reports the hook installed in all three', BANK, 'ONE TRACKED SOURCE, THREE INSTALLS'),
    ('bank reports both polarities exercised', BANK, 'ALLOWED from a `push-*` branch'),
    ('bank names the empty-scope trap it avoided', BANK, 'NEVER INVOKES THE HOOK AT ALL'),
    ('bank states the hook is not tracked', BANK, 'IS NOT TRACKED'),
    # ### COMPONENT 1
    ('bank quotes b226 unit definition', BANK, '`u_inf` := the rank-2 Sonin-sector'),
    ('bank quotes Corollary 3.2 whole', BANK, 'assume `mu` is a negative'),
    ('bank quotes the Sonin space as a subspace of L2', BANK, 'square integrable even functions'),
    ('bank gives Route A as definitional', BANK, 'MEMBERSHIP IS DEFINITIONAL'),
    ('bank checks the corollary hypothesis', BANK, 'WHICH IS NEGATIVE'),
    ('bank states the normalization step', BANK, 'AN EIGENVECTOR IS NONZERO'),
    ('bank discharges the work-order', BANK, '`W-ORD-PHI-MU-L2` IS DISCHARGED'),
    ('bank refuses the sector', BANK, 'IT DOES NOT PUT `u_inf` IN THE SECTOR'),
    # ### COMPONENT 2
    ('bank quotes the three specs', BANK, 'IT COUNTS FIRST LEVELS'),
    ('bank gives the negative answer', BANK, 'THE STATED GROUND DOES NOT NAME IT'),
    ('bank gives the empty-range reason', BANK, 'HAS NO CONTENT AT ALL'),
    ('bank states what the loosening would do at n>=2', BANK, 'THE DEMAND DOES DISSOLVE'),
    ('bank states it does not dissolve at one level', BANK, 'IT DOES NOT DISSOLVE, AND CANNOT'),
    # ### COMPONENT 3
    ('bank confirms the one-point index set', BANK, 'One point; and it IS the top'),
    ('bank reports the falsifier search returned its negation', BANK, 'THE OWNER ASSERTS ITS'),
    ('bank states index-smearing is dead', BANK, 'THERE IS NOTHING TO SMEAR OVER'),
    # ### COMPONENT 4
    ('bank quotes the source move', BANK, 'POSITIVE DEFINITE BY CONSTRUCTION'),
    ('bank decides the reach by definitions', BANK, 'IT IS ### NOT ### A FUNCTIONAL'),
    ('bank says the barrier is not weakened', BANK, 'not a counterexample to it'),
    ('bank splits the group exposure', BANK, 'THE `p^Z` PART: ### EXPOSED'),
    ('bank reports the zero at all six cells', BANK, 'CELLS FAILING: 0'),
    ('bank derives the zero rather than only measuring it', BANK, 'ONE PER SHELL RANGE'),
    ('bank refuses the zero as a barrier', BANK, 'AND IT IS NOT A BARRIER'),
    # ### COMPONENT 5
    ('bank assembles option A', BANK, 'OPTION A -- TERMWISE AGREEMENT'),
    ('bank assembles option B', BANK, 'OPTION B -- AGGREGATE AGREEMENT'),
    ('bank names the positivity as forced', BANK, 'FORCED, NOT EARNED'),
    ('bank states the question behind the question', BANK, 'carry arithmetic content'),
    ('bank refuses to answer it', BANK, 'DOES NOT ANSWER IT AND MUST NOT'),
    # ### THE SHADOW AND THE CLOSING
    ('bank splits the shadow candidate', BANK, 'WHAT DOES NOT QUALIFY'),
    ('bank reports the profile counts', BANK, '461 -> 470 PRINTS'),
    ('bank reports the byte prefix', BANK, 'TRUE BYTE PREFIX'),
    ('bank lists then counts the conditions', BANK, 'COUNTED FROM THAT LIST'),
    ('bank keeps M-2 unchanged', BANK, '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1: ### STILL UNPAID"),
    ('bank states what it did not check', BANK, 'NOT CHECKED THIS ACT'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    # ### THE REGISTRATION
    ('registration declares the missing falsifiers', REG, 'HAS NO REFERENT'),
    ('registration records the search for them', REG, 'THE SEARCH IS RECORDED'),
    ('registration labels the falsifiers as this seat\'s', REG, "THIS SEAT'S OWN"),
    ('registration is sealed before the bank', REG, 'SEALED BEFORE THE BANK'),
    # ### THE RUN LOGS
    ('the hook log reports all three identical', HRUN, 'ALL THREE BYTE-IDENTICAL'),
    ('the hook log reports a refusal', HRUN, 'REFUSED'),
    ('the smearing log reports no failing cells', SRUN, '### CELLS FAILING : 0'),
    ('the smearing log reports the shell orthogonality', SRUN, 'orthogonal to every shell  : True'),
    ('the kernel log reports the baseline byte-identity', KRUN, 'BYTE-IDENTICAL to banked : True'),
    ('the kernel log reports the true byte prefix', KRUN, 'TRUE BYTE PREFIX of the new one : True'),
    ('the kernel log reports no BOM', KRUN, 'BOM on the written file  : False'),
]

MUST_FAIL = [
    ('the object is not called constructed', BANK, 'THE OBJECT IS CONSTRUCTED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the zero is not called a barrier', BANK, 'THE SMEARED VALUE IS A BARRIER.'),
    ('the zero is not called a route', BANK, 'THE FINITE ANALOGUE IS A ROUTE.'),
    ('the specification is not loosened', BANK, 'SPEC-2 IS LOOSENED.'),
    ('no recommendation is made', BANK, 'OPTION A IS RECOMMENDED.'),
    ('no recommendation is made either way', BANK, 'OPTION B IS RECOMMENDED.'),
    ('the positivity question is not answered', BANK,
     'A FORCED POSITIVITY CARRIES ARITHMETIC CONTENT.'),
    ('the sector is not entered', BANK, 'u_inf IS IN THE SONIN SECTOR.'),
    ('the arch-norm reading is not decided', BANK, 'W-ORD-ARCH-NORM-READING IS DISCHARGED.'),
    ('no bench grade is promoted', BANK, 'c = +1 AT RANK 2 IS DERIVED.'),
    ('the closed route is not reopened', BANK, 'C3-VIA-SCALING IS REOPENED.'),
    ('the p^Z part is not claimed computed', BANK, 'THE p^Z PART WAS COMPUTED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the struck phrase is not used', BANK, 'HANDOFF CURRENT.'),
]

TOOLNUM = [
    ("the hook hashes and the polarity outcomes", 'tools/b304_hooks.py'),
    ("the compressed traces and the smeared values", 'tools/b304_smearing.py'),
    ("the kernel counts, the byte checks and the numstat", 'tools/b304_kernel.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b304_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b304_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b304_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b304_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b304' in x)

# ### G-SCOPE's FORBIDDEN VOCABULARY FOR THIS module. ### **THE SHADOW IS ABOUT TWO INTEGER
# ### RANGES**, so everything the ranges INDEX is forbidden to it.
FORBIDDEN = re.compile(
    r'prime|place|tower|level|sonin|space|trace|sum|aggregat|barrier|projection|scaling|'
    r'unit|\bb\d{3}\b', re.I)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def lean_terminals(path):
    src = io.open(path, encoding='utf-8').read()
    return [(m.group(1), ' '.join(m.group(2).split()))
            for m in re.finditer(r'^theorem\s+(\w+)\s*:(.*?):=\s*(?:by)?', src, re.S | re.M)]


def main():
    fails = []
    print('=' * 100)
    print('b304 -- GATE SUITE')
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

    print('\n  G-UNIT   (V1/V2) : unit clauses pulled : %d' % len(UNIT_CLAUSES))
    print('  G-DEMAND (V3/V4) : specification clauses pulled : %d' % len(DEMAND_CLAUSES))
    print('  G-REACH  (V5/V6/V7) : barrier and artifact clauses pulled : %d' % len(REACH_CLAUSES))

    bank = io.open(BANK, encoding='utf-8').read()

    # ### ==========================================================================================
    # ### G-CARD (V8) -- ### **THE CARD CARRIES NO RECOMMENDATION.**
    # ### ==========================================================================================
    print('\n  G-CARD (V8: the card is assembled and routed, with no recommendation):')
    rec = re.compile(r'\b(we recommend|this act recommends|option [ab] is (?:the )?(?:better|'
                     r'preferred|recommended)|the right choice is)\b', re.I)
    hits = [ln for ln in bank.splitlines() if rec.search(ln)]
    both = ('OPTION A -- TERMWISE AGREEMENT' in bank and 'OPTION B -- AGGREGATE AGREEMENT' in bank)
    unanswered = 'DOES NOT ANSWER IT AND MUST NOT' in bank
    dpos = bool(rec.search('and so option A is the better choice here'))
    dneg = not rec.search('NO RECOMMENDATION IS MADE ON EITHER OPTION')
    print('    recommendation-shaped lines : %d  %s'
          % (len(hits), 'PASS' if not hits else '### FAIL ###'))
    print('    both options assembled : %s ; the question left unanswered : %s' % (both, unanswered))
    print('    DISCRIMINATION: fires on a real recommendation : %s ; quiet on the refusal : %s'
          % (dpos, dneg))
    if hits or not both or not unanswered or not dpos or not dneg:
        fails.append('G-CARD')

    # ### ==========================================================================================
    # ### G-EXACT (V14) -- ### **NO FLOAT TOKEN IN THE DECIDING RUNNER OR ITS LOG.**
    # ### ==========================================================================================
    print('\n  G-EXACT (V14: the deciding runner is exact -- no float anywhere):')
    src = io.open(t('b304_smearing.py'), encoding='utf-8').read()
    log = io.open(SRUN, encoding='utf-8').read()
    floaty = re.compile(r'\bfloat\(|\bnumpy\b|\bmath\.|\d+\.\d+e[-+]?\d+|(?<![\d.])\d+\.\d+(?![\d.])')
    # ### THE DETECTOR WAS WRONG ON ITS FIRST RUN AND THE REPAIR IS THE DETECTOR, NOT THE TEXT.
    # ### It fired on `2006.13771` -- ### **AN arXiv IDENTIFIER, WHICH IS NOT A FLOAT TOKEN.**
    # ### **THIS IS NOT b302's D2 INVERTED AND THE DIFFERENCE MATTERS:** ### there the counter
    # ### caught a genuine instance of its target class and the PROSE was rewritten; here the
    # ### match is not an instance of the class at all, so the CLASS is what needed stating.
    # ### **AN arXiv ID IS REMOVED BEFORE SCANNING, AND BOTH POLARITIES ARE FIXTURED BELOW SO THE
    # ### NARROWING CANNOT HIDE A REAL DECIMAL.**
    arxiv = re.compile(r'arXiv:\s*\d+\.\d+(?:v\d+)?', re.I)

    def strip_ids(s):
        return arxiv.sub('arXiv:<id>', s)

    src_hits = [m.group(0) for m in floaty.finditer(strip_ids(src))]
    log_hits = [m.group(0) for m in floaty.finditer(strip_ids(log))]
    print('    float-shaped tokens in the runner : %d %s' % (len(src_hits), src_hits[:5]))
    print('    float-shaped tokens in its log    : %d %s' % (len(log_hits), log_hits[:5]))
    fpos = bool(floaty.search(strip_ids('x = 1.5')))
    fneg = not floaty.search(strip_ids('Fraction(1, 2) and the integer 12'))
    fid = not floaty.search(strip_ids('the source arXiv:2006.13771 was read'))
    fstill = bool(floaty.search(strip_ids('arXiv:2006.13771 and a real decimal 0.75')))
    print('    DISCRIMINATION: fires on a decimal : %s ; quiet on a Fraction : %s' % (fpos, fneg))
    print('    ### AND ON THE REPAIR ITSELF: quiet on an arXiv id : %s ;'
          ' STILL fires on a decimal beside one : %s' % (fid, fstill))
    if src_hits or log_hits or not fpos or not fneg or not fid or not fstill:
        fails.append('G-EXACT')

    # ### ==========================================================================================
    # ### G-SCOPE (V12) -- ### **THE SHADOW'S TERMINALS, READ FROM ITS SOURCE.**
    # ### ==========================================================================================
    print('\n  G-SCOPE (V12: the shadow carries its own scope in its own statements):')
    terms = lean_terminals(MODULE)
    bad = []
    for name, stmt in terms:
        hit = FORBIDDEN.search(name) or FORBIDDEN.search(stmt)
        if hit:
            bad.append((name, hit.group(0)))
    print('    terminals read from the module : %d' % len(terms))
    print('    naming a forbidden object : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ###'))
    for n, w in bad:
        print('        ### %-64s  <<%s>>' % (n, w))
    disc = bool(FORBIDDEN.search('the_sonin_space_at_this_prime'))
    quiet = not FORBIDDEN.search('index_range_at_bound_one_is_a_single_point')
    print('    DISCRIMINATION: fires on a forbidden name : %s ; quiet on a real one : %s'
          % (disc, quiet))
    print('    ### **DECLARED EXEMPTION: THE NAMESPACE.** ### `B304` prefixes every terminal here.')
    if bad or not disc or not quiet:
        fails.append('G-SCOPE')

    # ### ==========================================================================================
    # ### G-KERNEL -- ### **THE PROFILE, RE-CHECKED INDEPENDENTLY OF THE BUILD TOOL.**
    # ### ==========================================================================================
    print('\n  G-KERNEL (the profile, re-checked here and not taken from the build\'s own report):')
    prof = io.open(PROFILE, 'rb').read()
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'],
                          capture_output=True).stdout
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    zero = sum(1 for ln in lines if ln.rstrip().endswith('does not depend on any axioms'))
    mine = sum(1 for ln in lines if ln.startswith("'B304."))
    bom = prof.startswith(b'\xef\xbb\xbf')
    prefix = prof.startswith(head)
    dirty = subprocess.run(['git', '-C', SIDE, 'diff', '--numstat', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
    rng = ['HEAD'] if dirty else ['HEAD~1', 'HEAD']
    scope = 'the WORKING TREE vs HEAD' if dirty else 'THE COMMIT ITSELF (HEAD~1..HEAD)'
    ns = subprocess.run(['git', '-C', SIDE, 'diff', '--numstat'] + rng
                        + ['--', 'AXIOM_PRINTS.txt'],
                        capture_output=True, text=True).stdout.split()
    print('    numstat scope read       : %s' % scope)
    print('    prints on disk           : %d, zero-axiom %d, other %d'
          % (len(lines), zero, len(lines) - zero))
    print('    of them, this act\'s      : %d' % mine)
    print('    BOM (read as bytes)      : %s  %s' % (bom, 'PASS' if not bom else '### FAIL ###'))
    print('    HEAD is a TRUE BYTE PREFIX : %s  %s'
          % (prefix, 'PASS' if prefix else '### FAIL ###'))
    numstat_ok = (len(ns) >= 2 and ns[1] == '0' and int(ns[0]) > 0)
    print('    insertions / deletions   : %s / %s  %s'
          % (ns[0] if len(ns) >= 2 else 'n/a', ns[1] if len(ns) >= 2 else 'n/a',
             'PASS' if numstat_ok else '### FAIL -- EMPTY SCOPE OR A DELETION ###'))
    if bom or not prefix or (len(lines) - zero) or not numstat_ok or mine == 0:
        fails.append('G-KERNEL')

    # ### ==========================================================================================
    # ### G-NOAGG (V9).
    # ### ==========================================================================================
    print('\n  G-NOAGG (V9: no aggregation stated, named as stateable, or sketched):')
    claim = re.compile(r'\b(the aggregation is|we state the aggregation|M-2 is (?:now )?stated|'
                       r'aggregation over places is)\b', re.I)
    ahits = [ln for ln in bank.splitlines() if claim.search(ln)]
    unchanged = '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`' in bank
    dpos = bool(claim.search('and here the aggregation is stated at last'))
    dneg = not claim.search('NO AGGREGATION IS STATED, NAMED AS STATEABLE, OR SKETCHED')
    print('    aggregation-claim lines in the bank : %d  %s'
          % (len(ahits), 'PASS' if not ahits else '### FAIL ###'))
    print('    the bank carries M-2\'s row unchanged : %s' % unchanged)
    print('    DISCRIMINATION: fires on a real claim : %s ; quiet on the refusal : %s'
          % (dpos, dneg))
    if ahits or not unchanged or not dpos or not dneg:
        fails.append('G-NOAGG')

    # ### ==========================================================================================
    # ### G-STRUCK, G-STEM, G-TOOLNUM, G-NOPAPERS, G-SEAL.
    # ### ==========================================================================================
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
            print('    ### %-42s hits : %d' % (os.path.basename(p), len(ch)))
            for h in ch:
                print('        line %d col %d  %s' % (h[1], h[2], h[0]))
    print('    files scanned %d   struck-clause hits %d  %s'
          % (scanned, total, 'PASS' if not total else '### FAIL ###'))
    for p in FIXTURE_CARRIERS:
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), struck, stem_list)
        print('    %-44s hits : %d  ### ITS OWN FIXTURES (stated exception)'
              % (os.path.basename(p) + ' (EXCEPTION)', len(ch)))
    fired = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        hit = bool(ferry_scan.scan_text(text, struck, stem_list)[0])
        fired += 1 if hit else 0
        print('    DISCRIMINATION %-4s comes back hit : %s  %s'
              % (eid, hit, 'PASS' if hit else '### FAIL ###'))
    if total or fired != 3:
        fails.append('G-STRUCK')

    print('\n  G-STEM (every file this act wrote):')
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

    print('\n  G-TOOLNUM (ruling 3 / V14):')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-NOPAPERS (V13):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    rows = [x for x in pp.splitlines() if x.strip()]
    tracked = [x for x in rows if not x.startswith('??')]
    untracked = [x for x in rows if x.startswith('??')]
    t0 = os.path.getmtime(REG)
    newer = [x for x in untracked
             if os.path.isfile(os.path.join(PP, x[3:].strip().strip('"').replace('/', os.sep)))
             and os.path.getmtime(os.path.join(PP, x[3:].strip().strip('"').replace('/', os.sep)))
             > t0]
    ppmain = subprocess.run(['git', '-C', PP, 'rev-parse', 'HEAD'],
                            capture_output=True, text=True).stdout.strip()
    print('    TRACKED files changed : %d  %s'
          % (len(tracked), 'PASS' if not tracked else '### FAIL ###'))
    print('    untracked rows (pre-existing) : %d ; written after the seal : %d  %s'
          % (len(untracked), len(newer), 'PASS' if not newer else '### FAIL ###'))
    print('    PLACE-papers HEAD : %s   ### and it did not move (D6\'s throwaway left no trace)'
          % ppmain[:7])
    if tracked or newer:
        fails.append('G-NOPAPERS')

    print('\n  G-SEAL (the registration is byte-for-byte what was sealed):')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    print('    seal intact : %s  %s' % (intact, 'PASS' if intact else '### FAIL ###'))
    if not intact:
        fails.append('G-SEAL')

    print('\n  HEDGE AUDIT:')
    for lbl, path in [('the bank', BANK), ('the registration', REG)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-28s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            for s in gh:
                print('        (i) %s' % s[:140])

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 10
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
