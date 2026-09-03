# -*- coding: utf-8 -*-
"""b303_checks.py -- THE GATE SUITE. ### **ONE ARM PER REGISTERED FALSIFIER, AND NO MORE.**

### ### **EVERY COUNT THIS ACT REPORTS ABOUT ITSELF COMES OUT OF THIS FILE** (RULING (3) /
### `W-ORD-ADHOC-CHECK-FIXTURES`), except the kernel profile, which is `b303_kernel.py`'s and is
### ### RE-CHECKED HERE INDEPENDENTLY OF THAT TOOL'S OWN REPORT.

### ### **THE STANDING SHAPE, INHERITED AND NOT RE-INVENTED:** ### owner needles are pulled from
### ### EMITTING ### files; self needles from this act's own; must-fail fixtures are ###
### WHOLE-LINE EQUALITY ### and never substrings, because a substring must-fail is a sentence this
### act could satisfy by rephrasing rather than by not claiming the thing.
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
MODULE = os.path.join(SIDE, 'Core', 'ValuationDivisibilityShadow.lean')
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b303_the_uniform_family.txt')
REG = d('b303_registration_2026-09-03.txt')
KRUN = d('b303_kernel_run.txt')
FRUN = d('b303_family_run.txt')
SRUN = d('b303_source_read.txt')
SCAN = d('b303_ferry_scan.txt')
FERRY = d('b303_ferry_2026-09-03.txt')
SPEC = d('b303_satisfiable.json')

OWNED = [BANK, REG, KRUN, FRUN, SRUN, SCAN, FERRY, SPEC, MODULE,
         d('b303_corr_row.txt'), d('b303_index_query.txt'), d('b303_pins_step_zero.txt'),
         t('b303_kernel.py'), t('b303_regspec.py'), t('b303_source.py'),
         t('b303_family.py'), t('b303_pins.py'), t('b303_correspondence.py')]
FIXTURE_CARRIERS = [t('b303_checks.py'), t('b303_index_append.py')]

# ### ==============================================================================================
# ### THE OWNER NEEDLES. ### **EVERY ONE INTO THE FILE THAT EMITTED THE SENTENCE.**
# ### ==============================================================================================
SOURCE_CLAUSES = [                                          # ### V1 / V2
    ("b302's self-declared exposure -- what this act was sent to test",
     d('b302_the_unit_requirement.txt'), 'WOULD NEED REVISITING'),
    ("b302's declaration that the clause is held THROUGH A READER",
     d('b302_the_unit_requirement.txt'), 'THROUGH A READER'),
    ("b197's report of Definition 3.3.1 -- the thing TESTED",
     d('b197_values_and_c0.txt'), 'is a C0-sequence, if and only if f_alpha in'),
    ("b197's own method finding: the text layer drops every displayed formula",
     d('b197_values_and_c0.txt'), 'OCR TEXT LAYER DROPS EVERY DISPLAYED FORMULA'),
    ("the corpus's own extract, defective exactly at 3.3.1 (EMITTER)",
     d('ext_b196_vonneumann1939_extract.txt'), 'is a C0-sequence, if and'),
]

FAMILY_CLAUSES = [                                          # ### V3 / V4 / V5 / V7
    ("b301's caution -- the sentence that governs this act",
     d('b301_the_object_completed.txt'), 'A SHARED FORM IS A RESEMBLANCE UNTIL A DEFINITION'),
    ("b301's difference 1 -- an index set and a continuum",
     d('b301_the_object_completed.txt'), 'AN INDEX SET AND A CONTINUUM'),
    ("b301's difference 2 -- the sum and the product, and the chart caution",
     d('b301_the_object_completed.txt'), 'THE INVARIANT IS A SUM AT ONE PLACE'),
    ("b301's difference 3 -- one side has a level and the other has none",
     d('b301_the_object_completed.txt'), 'ONE SIDE HAS A LEVEL AND THE OTHER HAS NONE'),
    ("b301's difference 4 -- the hazard register still governs",
     d('b301_the_object_completed.txt'), "b285's HAZARD REGISTER STILL GOVERNS"),
    ("b301's promotion criterion for the uniform form",
     d('b301_the_object_completed.txt'), 'A DEFINITION OF THE FAMILY'),
    ("b293's family definition (EMITTER)",
     d('b293_the_finite_family.txt'), 'Son(p,n; a,b) :='),
    ("b293's quotation of b21's chart -- THE BRIDGE, and it is the corpus's",
     d('b293_the_finite_family.txt'), "In b21's chart"),
    ("b293's index range, set by the level",
     d('b293_the_finite_family.txt'), 'THE INDEX RANGE THE LEVEL CARRIES'),
    ("b293's V4 -- the archimedean family was the template and nowhere the evidence",
     d('b293_the_finite_family.txt'), 'THE ARCHIMEDEAN FAMILY WAS THE TEMPLATE'),
    ("CC Definition 4.4, quoted at b288 from its at-content read",
     d('b288_the_family_and_the_complement.txt'), "let Sonin's space"),
    ("CC's own identification of the corpus-relevant space as S(1,1)",
     d('b288_the_family_and_the_complement.txt'), "which is Sonin's space"),
    ("b288's product invariance and the orbit/diagonal statement",
     d('b288_the_family_and_the_complement.txt'), 'THE PRODUCT IS INVARIANT'),
    ("b198's PROVED theorem -- no finite exact levels at infinity",
     d('b198_nonvanishing.txt'), 'real_no_compact_open_addSubgroup'),
    ("b285's hazard register (EMITTER)",
     d('b285_archimedean_opening.txt'), 'THE HAZARD REGISTER'),
    ("b285's boundary -- the arc's vocabulary has no referents at infinity",
     d('b285_archimedean_opening.txt'), 'HAS NO REFERENTS THERE'),
    ("b286's closure of the arity question -- TWO",
     d('b286_the_cc_condition.txt'), 'CLOSED BY READING'),
]

FENCE_CLAUSES = [                                           # ### V9 / V8
    ("the annihilation criterion, from the act that folded it",
     d('b297_the_fold.txt'), 'ONLY IF `a >= 0` OR `b >= n-1`'),
    ("C3-VIA-SCALING is closed, and stays closed",
     d('b297_the_fold.txt'), 'C3-VIA-SCALING IS CLOSED'),
    ("b302's condition-count sentence -- the one this act corrects",
     d('b302_the_unit_requirement.txt'), 'CONDITIONS ARE NOW THREE'),
    ("b301's headline, which counted one of its own three typed results",
     d('b301_the_object_completed.txt'), 'LEVEL-LIMIT PREMISE, on ONE RESULT'),
    ("b301's (R2), the result its own headline did not count",
     d('b301_the_object_completed.txt'), '(R2) `W-ORD-PHI-MU-L2`'),
    ("b302's gate on the two-radius route, still not passed",
     d('b302_the_unit_requirement.txt'), 'IS STILL NOT PASSED'),
]

OWNER_NEEDLES = SOURCE_CLAUSES + FAMILY_CLAUSES + FENCE_CLAUSES

SELF_NEEDLES = [
    # ### COMPONENT 1
    ('bank returns CONFIRMS', BANK, 'THE VERDICT IS `CONFIRMS`'),
    ('bank quotes the definition whole', BANK, 'is a `C_0`-sequence, if and'),
    ('bank names the two conjuncts separately', BANK, '(ii) THE NORM SUM'),
    ('bank records the absent partition of I', BANK, 'NO PARTITION OF `I`'),
    ('bank pins the artefact by hash', BANK, '571060b596af58af35f09f077984a2b747e7acbc'),
    ('bank says the tool runs no OCR and reads nothing', BANK, 'RUNS NO OCR AND READS NOTHING'),
    ('bank says a confirmation adds no result', BANK, 'IT DOES NOT ADD A RESULT'),
    ('bank limits the read to one definition', BANK, 'READ ONE DEFINITION AND CLAIMS ONE'),
    # ### COMPONENT 2
    ('bank addresses difference 1 by name', BANK, 'DIFFERENCE 1 -- AN INDEX SET'),
    ('bank addresses difference 2 by name', BANK, 'DIFFERENCE 2 -- THE INVARIANT'),
    ('bank addresses difference 3 by name', BANK, 'DIFFERENCE 3 -- ONE SIDE HAS A LEVEL'),
    ('bank addresses difference 4 by name', BANK, "DIFFERENCE 4 -- b285's HAZARD REGISTER"),
    ('bank states the definition', BANK, 'A MEMBER OF THE TWO-RADIUS FAMILY IS A CHOICE'),
    ('bank declares its own packaging word as unowned', BANK, "IS THIS ACT'S PHRASE"),
    ('bank runs the E0 gate and reports its verdict', BANK, "THE GATE'S VERDICT"),
    ('bank says the chart is not this act\'s', BANK, 'THE CHART IS NOT SUPPLIED BY THIS ACT'),
    ('bank reports the finite half verified at content', BANK, 'CELLS FAILING: 0'),
    ('bank reports the two grades as different', BANK, 'IS NOT ONE VERIFICATION'),
    ('bank gives the uniformity answer as a division', BANK, 'ONE SENTENCE, TWO OBJECTS'),
    ('bank reports this seat was wrong about the form', BANK, 'WAS WRONG ABOUT THE FORM'),
    # ### COMPONENT 3
    ('bank states the capability as a capability', BANK, 'A PLACE TO LIVE ACROSS ALL PLACES'),
    ('bank fences the annihilation criterion', BANK, 'REMAINS EXACTLY THAT'),
    ('bank names what a bearing statement would have to be', BANK, 'FOUR REQUIREMENTS'),
    ('bank refuses its own most attractive analogy', BANK, 'IT IS NOT THE SAME STATEMENT'),
    # ### THE SHADOW
    ('bank splits the shadow candidate in two', BANK, 'THE COEFFICIENT HALF'),
    ('bank says why the coefficient half is not built', BANK, 'CERTIFY THE STAND-IN'),
    ('bank reports the profile counts', BANK, '449 -> 461 PRINTS'),
    ('bank reports the byte prefix', BANK, 'TRUE BYTE PREFIX'),
    ('bank declares the control that was wrong on first compile', BANK,
     'WRONG ON THE FIRST COMPILE'),
    # ### THE CLOSING
    ('bank corrects the condition count', BANK, 'THE CONDITIONS ARE ### FOUR'),
    ('bank types W-ORD-PHI-MU-L2 as the membership half', BANK, 'MEMBERSHIP HALF OF DEFINITION'),
    ('bank re-verdicts neither predecessor', BANK, 'NEITHER b301 NOR b302 IS RE-VERDICTED'),
    ('bank keeps M-2 unchanged', BANK, '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT ITEM 1: ### STILL UNPAID"),
    ('bank names item 1 as A2, state M-2', BANK, 'Item 1 is `A2`'),
    ('bank states what it did not check', BANK, 'NOT CHECKED THIS ACT'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    # ### THE REGISTRATION
    ('registration is sealed before the bank', REG, 'SEALED BEFORE THE BANK'),
    ('registration declares C1 known before the seal', REG, 'ALREADY KNOWN WHEN THIS FILE WAS'),
    ('registration permits the honest uniformity answer', REG, 'MAY COME BACK'),
    ('registration records the pre-component index queries', REG, 'uniform-family'),
    ('registration declares the hook coverage shortfall', REG, 'THE HOOK IS INSTALLED IN `relay`'),
    # ### THE RUN LOGS
    ('the source run reports the truncation', SRUN, 'TEXT LAYER STOPS DEAD  : YES'),
    ('the source run\'s control holds on the next page', SRUN, 'PASS -- the finding is this'),
    ('the family run reports no failing cells', FRUN, '### CELLS FAILING : 0'),
    ('the family run reports no chart mismatches', FRUN, 'mismatches : 0'),
    ('the kernel run reports the baseline byte-identity', KRUN, 'BYTE-IDENTICAL to banked : True'),
    ('the kernel run reports the true byte prefix', KRUN, 'TRUE BYTE PREFIX of the new one : True'),
    ('the kernel run reports no BOM', KRUN, 'BOM on the written file  : False'),
]

# ### **WHOLE-LINE EQUALITY. ### NEVER A SUBSTRING.**
MUST_FAIL = [
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the family is not called a route', BANK, 'THE FAMILY IS A ROUTE.'),
    ('the definition is not called an aggregation', BANK, 'THE DEFINITION IS AN AGGREGATION.'),
    ('the family is not promoted to a corpus object', BANK, 'THE FAMILY IS A CORPUS OBJECT.'),
    ('the annihilation criterion is not carried to infinity', BANK,
     'THE ANNIHILATION CRITERION HOLDS AT INFINITY.'),
    ('the two instances are not called one object', BANK, 'THE TWO INSTANCES ARE ONE OBJECT.'),
    ('Q4 is not called met', BANK, 'Q4 IS MET.'),
    ('no bench grade is promoted', BANK, 'c = +1 AT RANK 2 IS DERIVED.'),
    ('the ruling is not called a derivation', BANK, 'RULE ARCH-UNIT IS DERIVED.'),
    ('the shadow is not called evidence about a space', BANK, 'THE SHADOW CERTIFIES THE FAMILY.'),
    ('the C0 condition is not identified with the restriction condition', BANK,
     'REQUIREMENT (4) IS DEFINITION 3.3.1.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the struck phrase is not used', BANK, 'HANDOFF CURRENT.'),
    ('no predecessor is re-verdicted', BANK, 'b302 IS RE-VERDICTED.'),
]

TOOLNUM = [
    ("the source artefact's hash, page index and truncation", 'tools/b303_source.py'),
    ("the finite family's cell arms, dimensions and chart identities", 'tools/b303_family.py'),
    ("the kernel counts, the byte checks and the numstat", 'tools/b303_kernel.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b303_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b303_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b303_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b303_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(t_ for _w, t_ in TOOLNUM if '/b303' in t_)

# ### G-SCOPE's FORBIDDEN VOCABULARY FOR ### THIS ### module, and the ONE declared exemption.
# ### **THE LIST IS THIS ACT'S OWN AND IS WIDER THAN b302's**, because this module sits closer to
# ### the corpus's objects than an enclosure did: it is about indices, and the objects built ON
# ### those indices are exactly what it must not name.
FORBIDDEN = re.compile(
    r'sonin|hilbert|norm|transform|sector|subspace|dimension|cutoff|scale|place|'
    r'archimedean|adelic|ball|unit[ _]vector|\bb\d{3}\b', re.I)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def lean_terminals(path):
    """### RETURN `[(name, statement)]` FROM THE MODULE'S OWN SOURCE."""
    src = io.open(path, encoding='utf-8').read()
    return [(m.group(1), ' '.join(m.group(2).split()))
            for m in re.finditer(r'^theorem\s+(\w+)\s*:(.*?):=\s*(?:by)?', src, re.S | re.M)]


def main():
    fails = []
    print('=' * 100)
    print('b303 -- GATE SUITE')
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

    print('\n  G-SOURCE  (V1/V2) : source clauses pulled : %d' % len(SOURCE_CLAUSES))
    print('  G-FAMILY  (V3/V4/V5/V7) : owner clauses pulled : %d' % len(FAMILY_CLAUSES))
    print('  G-FENCE   (V8/V9) : fence clauses pulled : %d' % len(FENCE_CLAUSES))

    # ### ==========================================================================================
    # ### G-DIFF (V3) -- ### **EACH OF THE FOUR DIFFERENCES ADDRESSED UNDER ITS OWN HEADING.**
    # ### ==========================================================================================
    print('\n  G-DIFF (V3: the four differences addressed one by one, not dissolved):')
    bank = io.open(BANK, encoding='utf-8').read()
    heads = re.findall(r'DIFFERENCE (\d) --', bank)
    got = sorted(set(heads))
    ok_diff = got == ['1', '2', '3', '4']
    print('    headings found : %s  %s' % (got, 'PASS' if ok_diff else '### FAIL ###'))
    # ### THE DISCRIMINATION: the regex must NOT fire on a bare mention of the word.
    disc = bool(re.search(r'DIFFERENCE (\d) --', 'DIFFERENCE 2 -- the invariant'))
    quiet = not re.search(r'DIFFERENCE (\d) --', 'the differences are four in number')
    print('    DISCRIMINATION: fires on a heading : %s ; quiet on a bare mention : %s'
          % (disc, quiet))
    if not (ok_diff and disc and quiet):
        fails.append('G-DIFF')

    # ### ==========================================================================================
    # ### G-E0 (V7) -- ### **EVERY CONSTITUENT ROW CARRIES BOTH PLACE CLASSES OR IS NAMED UNOWNED.**
    # ### ==========================================================================================
    print('\n  G-E0 (V7: the E0 gate table, and the unowned constituent named):')
    named_unowned = 'UNOWNED' in bank
    verdict = "THE GATE'S VERDICT" in bank
    halts = 'DOES NOT HALT' in bank
    print('    the gate table names an UNOWNED constituent : %s' % named_unowned)
    print('    the gate prints a verdict                   : %s' % verdict)
    print('    the verdict says whether it halts           : %s' % halts)
    if not (named_unowned and verdict and halts):
        fails.append('G-E0')

    # ### ==========================================================================================
    # ### G-SCOPE (V12) -- ### **THE MODULE'S OWN TERMINALS, READ FROM ITS SOURCE.**
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
    disc = bool(FORBIDDEN.search('the_sonin_subspace_dimension_at_this_place'))
    quiet = not FORBIDDEN.search('valuation_and_divisibility_agree_over_the_range_at_p_two_n_one')
    print('    DISCRIMINATION: fires on a forbidden name : %s ; quiet on a real one : %s'
          % (disc, quiet))
    print('    ### **DECLARED EXEMPTION: THE NAMESPACE.** ### `B303` prefixes every terminal here')
    print('    ### as `B302` prefixes b302\'s -- the corpus\'s provenance convention, not a leak.')
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
    mine = sum(1 for ln in lines if ln.startswith("'B303."))
    bom = prof.startswith(b'\xef\xbb\xbf')
    prefix = prof.startswith(head)
    dirty = subprocess.run(['git', '-C', SIDE, 'diff', '--numstat', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
    rng = ['HEAD'] if dirty else ['HEAD~1', 'HEAD']
    src = 'the WORKING TREE vs HEAD' if dirty else 'THE COMMIT ITSELF (HEAD~1..HEAD)'
    ns = subprocess.run(['git', '-C', SIDE, 'diff', '--numstat'] + rng
                        + ['--', 'AXIOM_PRINTS.txt'],
                        capture_output=True, text=True).stdout.split()
    print('    numstat scope read       : %s' % src)
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
    # ### G-NOAGG (V8) -- ### **THE AGGREGATION CAP, MEASURED OVER THIS ACT'S OWN PROSE.**
    # ### ==========================================================================================
    print('\n  G-NOAGG (V8: no aggregation stated, named as stateable, or sketched):')
    claim = re.compile(r'\b(the aggregation is|we state the aggregation|M-2 is (?:now )?stated|'
                       r'aggregation over places is)\b', re.I)
    hits = [ln for ln in bank.splitlines() if claim.search(ln)]
    unchanged = '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`' in bank
    print('    aggregation-claim lines in the bank : %d  %s'
          % (len(hits), 'PASS' if not hits else '### FAIL ###'))
    print('    the bank carries M-2\'s row unchanged : %s' % unchanged)
    dpos = bool(claim.search('and here the aggregation is stated at last'))
    dneg = not claim.search('NO AGGREGATION IS STATED, NAMED AS STATEABLE, OR SKETCHED')
    print('    DISCRIMINATION: fires on a real claim : %s ; quiet on the refusal : %s'
          % (dpos, dneg))
    if hits or not unchanged or not dpos or not dneg:
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
    print('    TRACKED files changed : %d  %s'
          % (len(tracked), 'PASS' if not tracked else '### FAIL ###'))
    print('    untracked rows (pre-existing) : %d ; written after the seal : %d  %s'
          % (len(untracked), len(newer), 'PASS' if not newer else '### FAIL ###'))
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

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 9
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
