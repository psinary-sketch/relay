# -*- coding: utf-8 -*-
"""b305_checks.py -- THE GATE SUITE. ### **ONE ARM PER REGISTERED FALSIFIER AND GATE, AND NO MORE.**

### ### **EVERY COUNT THIS ACT REPORTS ABOUT ITSELF COMES OUT OF THIS FILE**, except the source
### locations, which are `b305_source.py`'s.
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
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b305_the_arithmetics_entry.txt')
REG = d('b305_registration_2026-09-03.txt')
SRUN = d('b305_source_read.txt')
SCAN = d('b305_ferry_scan.txt')
FERRY = d('b305_ferry_2026-09-03.txt')
SPEC = d('b305_satisfiable.json')

OWNED = [BANK, REG, SRUN, SCAN, FERRY, SPEC,
         d('b305_corr_row.txt'), d('b305_index_query.txt'), d('b305_pins_step_zero.txt'),
         d('b305_regspec_run.txt'),
         t('b305_source.py'), t('b305_regspec.py'), t('b305_correspondence.py')]
FIXTURE_CARRIERS = [t('b305_checks.py'), t('b305_index_append.py')]

# ### ==============================================================================================
# ### THE OWNER NEEDLES. ### **EVERY ONE INTO THE FILE THAT EMITTED THE SENTENCE.**
# ### ==============================================================================================
CORPUS_CLAUSES = [
    ("the adopted prime summand, with its adoption named (EMITTER)",
     d('b260_junction_sign.txt'), 'adopted b229'),
    ("its algebraic form",
     d('b260_junction_sign.txt'), '2 log p'),
    ("the w - tau relation, which makes tau a weighted prime term",
     d('b260_junction_sign.txt'), 'w_{p,k} * ( 1 - (p^n - p^k)/(p^n - 1) )'),
    ("act 9's closed form WITH its range (EMITTER)",
     d('b220_aggregation_freedom.txt'), 'for 1 <= k <= n-1, 0 for k >= n'),
    ("b280's chart sentence -- the (F3) check",
     d('b280_the_consequence.txt'), "b21's chart `x = p^{-n} m`"),
    ("b280's Haar sentence -- a chart point is a coset of positive measure",
     d('b280_the_consequence.txt'), 'COSET OF MEASURE'),
    ("b280's level-coherence conclusion",
     d('b280_the_consequence.txt'), 'A CONDITION ON `Q_p` AT ALL'),
    ("b280's barrier verdict and its scope",
     d('b280_the_consequence.txt'), 'AT EVERY FINITE PLACE AND'),
    ("W-ORD-FIBER-GENERAL, restated at its own scope",
     d('b280_the_consequence.txt'), 'PROVED AT LEVEL 1 AND FULLY VERIFIED'),
    ("b21's escaped-mass artifact, as b284 quotes its namer",
     d('b284_the_scalings_domain.txt'), 'ESCAPED MASS FOLDED BACK IN'),
    ("### b284's 'nothing to fold on Q_p' -- the retirement's warrant",
     d('b284_the_scalings_domain.txt'), 'WHERE THERE IS NOTHING TO FOLD'),
    ("b293's family definition",
     d('b293_the_finite_family.txt'), 'Son(p,n; a,b) :='),
    ("b293's collapsed rational condition",
     d('b293_the_finite_family.txt'), 'THE COLLAPSED RATIONAL CONDITION'),
    ("b297's annihilation criterion",
     d('b297_the_fold.txt'), 'ONLY IF `a >= 0` OR `b >= n-1`'),
    ("b303's two-radius family definition",
     d('b303_the_uniform_family.txt'), 'A MEMBER OF THE TWO-RADIUS FAMILY IS A CHOICE'),
    ("b304's compact-part zero",
     d('b304_the_demands_shape.txt'), 'EXACTLY ZERO AT ALL SIX'),
    ("b304's forced-positivity work-order, which this act discharges",
     d('b304_the_demands_shape.txt'), 'W-ORD-FORCED-POSITIVITY'),
    ("b297 as the last fold, and the arc it covered",
     d('b297_the_fold.txt'), 'THE M-2 CAMPAIGN, b283-b296'),
]

OWNER_NEEDLES = CORPUS_CLAUSES

SELF_NEEDLES = [
    # ### STEP ZERO
    ('bank says nothing was ahead', BANK, 'NOTHING WAS AHEAD OF ORIGIN IN ANY REPO'),
    # ### COMPONENT 1
    ('bank pins the artefact', BANK, 'b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726'),
    ('bank says the text layer is intact', BANK, 'THE TEXT LAYER IS INTACT'),
    ('bank quotes the finitely-many-primes sentence', BANK, 'INVOLVES ONLY FINITELY MANY PRIMES'),
    ('bank quotes the support that excludes primes', BANK, 'RATIONAL PRIMES'),
    ('bank quotes eq. 149', BANK, '(log p) SUM_{m=1}^{inf}'),
    ('bank quotes eq. 148 with the places', BANK, 'runs over all places'),
    ('bank quotes the positivity sentence', BANK, 'POSITIVE DEFINITE BY'),
    ('bank names the operator whose square gives positivity', BANK, '`A = S ϑ(g)*`'),
    ('bank gives the verdict as the pairing', BANK, 'IT IS THE PAIRING, AND NOT EITHER'),
    ('bank refutes F1', BANK, '(F1) IS REFUTED'),
    ('bank says why the difference matters', BANK, 'AN INSTRUMENT NEEDS THE DISTRIBUTION'),
    # ### COMPONENT 2
    ('bank quotes the adopted summand', BANK, 'ADOPTED b229'),
    ('bank gives the factor-by-factor match', BANK, 'THESE ARE THE SAME EXPRESSION'),
    ('bank names the evenness convention', BANK, 'RESTS ON A CONVENTION'),
    ('bank rules the quotient channel a different species', BANK, 'NOT THE SAME SPECIES'),
    ('bank says the feared verdict does not arise', BANK, 'THE FEARED VERDICT DOES NOT ARISE'),
    ('bank refuses the match as a capability', BANK, 'IS NOT DOING WITH IT WHAT THE SOURCE DOES'),
    # ### COMPONENT 3
    ('bank confirms F3 on b280 sentences', BANK, '(F3) HOLDS'),
    ('bank names the one structural change', BANK, 'UNTIE THE TWO'),
    ('bank lists what it must reproduce', BANK, 'WHAT IT MUST REPRODUCE'),
    ('bank says the instrument must reproduce the mechanism', BANK, 'NOT ONLY ITS VALUE'),
    ('bank gives the price in acts', BANK, 'THREE ACTS MINIMUM, FIVE FOR THE COMPARISON'),
    ('bank labels the price an estimate', BANK, 'NOT A RECOMMENDATION TO'),
    ('bank names the estimate own risk', BANK, 'to cost more than priced'),
    ('bank names the retired artifact', BANK, 'THE ESCAPED-MASS ARTIFACT'),
    ('bank says what it does not retire', BANK, 'NOT RETIRE THE RANGE LAW'),
    # ### THE SHADOW AND THE CLOSING
    ('bank checks the shadow rather than assuming', BANK, 'NOTHING IS BUILDABLE'),
    ('bank reports the profile unchanged', BANK, '470 PRINTS, UNCHANGED'),
    ('bank restates the three conditions from the list', BANK, 'COUNTED FROM THAT LIST'),
    ('bank discharges the forced-positivity order', BANK, 'DISCHARGED AS POSED'),
    ('bank files the successor', BANK, 'W-ORD-DIFFERENCE-CONTENT'),
    ('bank names the fold as due', BANK, 'THE FOLD IS DUE AFTER THIS ACT'),
    ('bank counts the unfolded acts', BANK, 'NINE ACTS INCLUDING THE FOLD ACT ITSELF'),
    ('bank keeps M-2 unchanged', BANK, '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`'),
    ('bank refuses the M-2 appearance explicitly', BANK, 'AT RISK OF LOOKING LIKE IT MOVED IT'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1: ### STILL UNPAID"),
    ('bank says a calculator is not a route', BANK, 'A CALCULATOR IS NOT A ROUTE'),
    ('bank states what it did not check', BANK, 'NOT CHECKED THIS ACT'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    # ### THE REGISTRATION
    ('registration notes the falsifiers have a referent', REG, 'HAVE A REFERENT'),
    ('registration pulls the three verbatim', REG, 'the arithmetic enters through the test'),
    ('registration carries their provenance', REG, 'THE AUTHOR, BY THE b305 FERRY'),
    ('registration registers this seat against F1', REG, 'MOST EXPECTS TO REFUTE'),
    ('registration is sealed before the bank', REG, 'SEALED BEFORE THE BANK'),
    # ### THE RUN LOG
    ('the source run matches the pinned artefact', SRUN, 'MATCHES THE ARTEFACT b304 PINNED : True'),
    ('the source run measures the layer intact', SRUN, 'stops dead at "if and" : 0'),
    ('the source run locates every fragment', SRUN, 'FRAGMENTS NOT LOCATED : 0'),
]

MUST_FAIL = [
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the match is not called a route', BANK, 'THE CORPUS HAS A ROUTE.'),
    ('the instrument is not recommended', BANK, 'THE INSTRUMENT SHOULD BE BUILT.'),
    ('nothing is claimed built', BANK, 'THE INSTRUMENT IS BUILT.'),
    ('the closed route is not reopened', BANK, 'C3-VIA-SCALING IS REOPENED.'),
    ('the positivity is not credited with arithmetic', BANK,
     'THE POSITIVITY CARRIES ARITHMETIC CONTENT.'),
    ('the object is not called constructed', BANK, 'THE OBJECT IS CONSTRUCTED.'),
    ('no condition is claimed discharged this act', BANK, 'A CONDITION IS DISCHARGED.'),
    ('the fold is not claimed performed', BANK, 'THE FOLD IS PERFORMED.'),
    ('the quotient channel is not demoted', BANK, 'THE QUOTIENT CHANNEL IS WRONG.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the struck phrase is not used', BANK, 'HANDOFF CURRENT.'),
]

TOOLNUM = [
    ("the artefact hash, the layer measurement and the fragment locations", 'tools/b305_source.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b305_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b305_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b305_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b305_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b305' in x)

# ### G-NOANALOGY's FORBIDDEN VOCABULARY. ### **CORPUS ### OBJECT ### NAMES, NOT THE WORD
# ### "CORPUS"** -- Component 1 says outright that it draws no analogy, and a gate that fired on
# ### that sentence would be forbidding the declaration rather than the act.
CORPUS_OBJECTS = re.compile(
    r'\bPR\b|Theta_q|tau_|Son\(|S-bar|w_\{p,k\}|ball_n|act 9|quotient channel', re.I)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def section(text, start, end):
    """### THE TEXT BETWEEN TWO HEADINGS. ### **USED TO SCOPE A GATE TO ONE COMPONENT**, which is
    the only way `G-NOANALOGY` can mean anything: the ban is on Component 1, not on the bank."""
    i = text.find(start)
    j = text.find(end, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        return None
    return text[i:j]


def main():
    fails = []
    print('=' * 100)
    print('b305 -- GATE SUITE')
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

    # ### ==========================================================================================
    # ### G-QUOTE (G1) -- ### **EVERY COMPONENT 1 QUOTATION CARRIES A LOCATION.**
    # ### ==========================================================================================
    print('\n  G-QUOTE (G1: every Component 1 quotation carries an equation or page location):')
    c1 = section(bank, 'COMPONENT 1 -- THE ENTRY.', 'COMPONENT 2 -- THE COMPARISON')
    if c1 is None:
        fails.append('G-QUOTE (section not found)')
        print('    ### FAIL -- Component 1 could not be delimited.')
    else:
        eqs = len(re.findall(r'eq\. \(\d+\)', c1))
        pgs = len(re.findall(r'PDF page index \d+', c1))
        print('    equation citations in Component 1 : %d' % eqs)
        print('    page-index citations             : %d' % pgs)
        ok_q = eqs >= 5 and pgs >= 5
        print('    both present in quantity : %s  %s' % (ok_q, 'PASS' if ok_q else '### FAIL ###'))
        if not ok_q:
            fails.append('G-QUOTE')

    # ### ==========================================================================================
    # ### G-NOANALOGY (G2) -- ### **SCOPED TO COMPONENT 1's OWN TEXT.**
    # ### ==========================================================================================
    print('\n  G-NOANALOGY (G2: Component 1 draws no analogy to the corpus\'s objects):')
    if c1 is None:
        fails.append('G-NOANALOGY (section not found)')
    else:
        hits = [m.group(0) for m in CORPUS_OBJECTS.finditer(c1)]
        print('    corpus object-names inside Component 1 : %d %s' % (len(hits), hits[:6]))
        dpos = bool(CORPUS_OBJECTS.search('and this is just like Theta_q at the top level'))
        dneg = not CORPUS_OBJECTS.search('the local Weil distribution carries the primes')
        print('    DISCRIMINATION: fires on a real analogy : %s ; quiet on a pure read : %s'
              % (dpos, dneg))
        print('    ### **THE GATE BANS OBJECT NAMES, NOT THE WORD "CORPUS"** -- Component 1 says')
        print('    ### outright that it draws no analogy, and a gate firing on that sentence would')
        print('    ### be forbidding the declaration rather than the act.')
        if hits or not dpos or not dneg:
            fails.append('G-NOANALOGY')

    # ### ==========================================================================================
    # ### G-PRICE -- ### **THE INSTRUMENT IS PRICED, NOT RECOMMENDED.**
    # ### ==========================================================================================
    print('\n  G-PRICE (the instrument is priced and not recommended):')
    rec = re.compile(r'\b(we recommend|this act recommends|should be built|the instrument ought)\b',
                     re.I)
    rhits = [ln for ln in bank.splitlines() if rec.search(ln)]
    priced = 'THREE ACTS MINIMUM, FIVE FOR THE COMPARISON' in bank
    disclaimed = 'NOT A RECOMMENDATION TO' in bank
    dpos = bool(rec.search('and we recommend building it next'))
    dneg = not rec.search('IT IS NOT A COMMITMENT, NOT A MEASUREMENT')
    print('    recommendation-shaped lines : %d  %s'
          % (len(rhits), 'PASS' if not rhits else '### FAIL ###'))
    print('    a price is given : %s ; and disclaimed as not a recommendation : %s'
          % (priced, disclaimed))
    print('    DISCRIMINATION: fires on a real recommendation : %s ; quiet on the disclaimer : %s'
          % (dpos, dneg))
    if rhits or not priced or not disclaimed or not dpos or not dneg:
        fails.append('G-PRICE')

    # ### ==========================================================================================
    # ### G-NOBUILD (G8) -- ### **NOTHING BUILT, AND THE PROFILE COMPARED BYTE-WISE.**
    # ### ==========================================================================================
    print('\n  G-NOBUILD (G8: nothing built; the profile does not move):')
    prof = io.open(PROFILE, 'rb').read()
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'],
                          capture_output=True).stdout
    identical = (prof == head)
    dirty = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                           capture_output=True, text=True).stdout.strip()
    lean_rows = [x for x in dirty.splitlines() if x.strip().endswith('.lean')]
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    print('    profile BYTE-IDENTICAL to git HEAD : %s  %s'
          % (identical, 'PASS' if identical else '### FAIL ###'))
    print('    `.lean` files changed in the kernel repo : %d  %s'
          % (len(lean_rows), 'PASS' if not lean_rows else '### FAIL ###'))
    print('    prints on disk : %d   ### unchanged by this act' % len(lines))
    if not identical or lean_rows:
        fails.append('G-NOBUILD')

    # ### ==========================================================================================
    # ### G-NOAGG (G5).
    # ### ==========================================================================================
    print('\n  G-NOAGG (G5: no aggregation stated, named as stateable, or sketched):')
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

    print('\n  G-TOOLNUM (ruling 3 / G12):')
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

    print('\n  G-NOPAPERS (G9):')
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
