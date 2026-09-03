# -*- coding: utf-8 -*-
"""b306_checks.py -- THE GATE SUITE. ### **ONE ARM PER REGISTERED FALSIFIER AND GATE, AND NO MORE.**

### ### **AND ONE ARM THIS ACT ADDS TO THE STANDING SHAPE:** ### `G-SHARED` runs the extended
### sweep over `CORRESPONDENCE.md` and `banked_index.py` and ### **EXPECTS EXACTLY THE TWO
### ANCESTORS' HITS AND NO OTHERS.** ### A suite that merely reported the number would let this
### act's own new row slip in beside them; ### **THE ARM PINS WHICH ROWS ARE ALLOWED TO HIT.**
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
import b306_stem_scope   # noqa: E402  ### the extended sweep, READ not copied

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b306_the_difference.txt')
REG = d('b306_registration_2026-09-03.txt')
DRUN = d('b306_difference_run.txt')
SRUN = d('b306_stem_scope.txt')
SCAN = d('b306_ferry_scan.txt')
FERRY = d('b306_ferry_2026-09-03.txt')
SPEC = d('b306_satisfiable.json')

OWNED = [BANK, REG, DRUN, SCAN, FERRY, SPEC,
         d('b306_corr_row.txt'), d('b306_index_query.txt'), d('b306_pins_step_zero.txt'),
         d('b306_regspec_run.txt'),
         t('b306_stem_scope.py'), t('b306_difference.py'), t('b306_regspec.py'),
         t('b306_correspondence.py')]
# ### THE DECLARED EXCEPTIONS (b300's stated shape). ### **A SWEEP LOG THAT REPORTS A HIT MUST
# ### QUOTE THE LINE IT HIT**, so `b306_stem_scope.txt` necessarily carries the very stem it found
# ### in an ancestor's row. ### **THAT IS THE `ferry_scan.py` LAW ONE LEVEL OUT: A HIT IS A STRING,
# ### NOT A FAULT, AND A REPORT OF A HIT IS NOT A NEW HIT.** ### Swept and reported separately.
FIXTURE_CARRIERS = [t('b306_checks.py'), t('b306_index_append.py'), SRUN]

# ### THE TWO ANCESTORS' ROWS THE EXTENDED SWEEP IS ALLOWED TO HIT, AND NO OTHERS.
ALLOWED_SHARED_HITS = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}

OWNER_NEEDLES = [
    ("CC Theorem 1, as the corpus already carried its shape", d('b305_the_arithmetics_entry.txt'),
     'W_inf(g*g*) >= Tr('),
    ("the source's primes-not-involved sentence", d('b305_the_arithmetics_entry.txt'),
     'RATIONAL PRIMES'),
    ("eq. (149), the local factor", d('b305_the_arithmetics_entry.txt'),
     '(log p) SUM_{m=1}^{inf}'),
    ("b305's identification of the summand, carried not re-derived",
     d('b305_the_arithmetics_entry.txt'), 'THESE ARE THE SAME EXPRESSION'),
    ("### b291's deciding sentence -- the families lie outside the space",
     d('b291_the_involution.txt'), "SO NEITHER PAIRED FAMILY LIES IN THE OBJECT'S"),
    ("b254's realization (A) table (EMITTER)", d('b254_fourth_face_off.txt'),
     'REALIZATION (A)'),
    ("b254's uniform sign", d('b254_fourth_face_off.txt'), 'UNIFORMLY NEGATIVE AT EVERY CELL'),
    ("b248's split table (EMITTER)", d('b248_second_object.txt'), 'ARCHIMEDEAN      JUNCTION'),
    ("b260's PR summand with its adoption", d('b260_junction_sign.txt'), 'adopted b229'),
    ("b260's J1, the junction's derived sign", d('b260_junction_sign.txt'),
     'ON THE OWNERS'),
    ("b260's test function and its cutoff guard", d('b260_junction_sign.txt'),
     'np.convolve(w, w, mode='),
    ("b261's E2even form", d('b261_e2even_monotone.txt'), 'E2even(a) = 2 * INT_0^2 psi(s)'),
    ("### b261's bench grade for the kernel's sign", d('b261_e2even_monotone.txt'),
     'HOLDS AT BENCH. ### THE DERIVATION IS NOT CLAIMED'),
    ("act 9's closed form with its range (EMITTER)", d('b220_aggregation_freedom.txt'),
     'for 1 <= k <= n-1, 0 for k >= n'),
    ("b304's per-index demand at one-level primes", d('b304_the_demands_shape.txt'),
     'IT DOES NOT DISSOLVE, AND CANNOT'),
    ("### b305's naming of the sweep-scope hole, which this act closes",
     d('b305_the_arithmetics_entry.txt'), 'hole in the sweep'),
    ("b284's closed route, not reopened", d('b297_the_fold.txt'), 'C3-VIA-SCALING IS CLOSED'),
    ("b292's infinite-dimensional refusal, the shadow's precedent", d('b302_the_unit_requirement.txt'),
     'QUANTIFIES OVER AN'),
]

SELF_NEEDLES = [
    # ### THE VERDICT
    ('bank gives the verdict', BANK, 'THE VERDICT: ### DIFFERENT'),
    ('bank names the first differing constituent', BANK, 'THE FIRST DIFFERING CONSTITUENT IS THE'),
    ('bank quotes b291 as the decider', BANK, 'NEITHER PAIRED FAMILY LIES IN THE'),
    ('bank refuses partly-same', BANK, 'ONLY IF BOTH ARE'),
    ('bank answers the FOOT question', BANK, 'THE CORPUS'),
    # ### STEP ZERO
    ('bank reports nothing ahead', BANK, 'NOTHING WAS AHEAD OF ORIGIN IN ANY REPO'),
    ('bank reports the sweep hole closed', BANK, 'THE HOLE b305 NAMED IS CLOSED'),
    ('bank attributes the index hit to itself', BANK, "THIS SEAT'S, FROM b305"),
    ('bank leaves the ancestor row alone', BANK, 'NOT REWRITTEN'),
    ('bank says a ban is not retroactive', BANK, 'A BAN IS NOT RETROACTIVE'),
    ('bank owns the generator-not-artefact lesson', BANK, 'FIXED A GENERATOR AND'),
    # ### COMPONENT 1
    ('bank quotes Theorem 1 whole', BANK, 'have support in the interval'),
    ('bank quotes Theorem 6.11 relaxation', BANK, '13 < c < 17'),
    ('bank says Theorem 1 sums over no places', BANK, 'SUMS OVER NO PLACES AT ALL'),
    ('bank distinguishes zeroed from excluded', BANK, 'THEY ARE ZEROED IN IT'),
    ('bank quotes the primes-not-involved sentence', BANK, 'RATIONAL PRIMES ARE NOT INVOLVED'),
    # ### COMPONENT 2
    ('bank refuses the order algebra on the order word', BANK, 'ON THE ORDER'),
    ('bank reports the two-table confirmation', BANK, 'TWO ACTS, TWO TOOLS, ONE COLUMN'),
    ('bank reports the junction disagreement', BANK, 'W-ORD-JUNCTION-LAST-PLACE'),
    ('bank carries the junction grade', BANK, 'SIGNED BY THEOREM'),
    ('bank carries E2even at bench', BANK, 'AT BENCH'),
    # ### COMPONENT 3
    ('bank names and refuses the resemblance', BANK, 'IS A SHARED SHAPE AND IT IS NOT'),
    ('bank gives the constituent table', BANK, 'NO COUNTERPART'),
    ('bank decides the window as complementary', BANK, 'COMPLEMENTARY CHOICES OF THE SAME KNOB'),
    ('bank decides the test-function class', BANK, 'FAILS BY CONSTRUCTION'),
    ('bank reports F3 on the announcement', BANK, 'ANNOUNCES THE SEMI-LOCAL VERSION'),
    # ### COMPONENT 4
    ('bank names the open question', BANK, 'W-ORD-SOURCE-METHOD-APPLICABILITY'),
    ('bank refuses to invalidate measurements', BANK, 'ARE NOT INVALIDATED'),
    ('bank says no grade moves', BANK, 'NO GRADE MOVES'),
    ('bank states the small thing gained', BANK, 'PRIME SIDE TRAVELS'),
    # ### THE CLOSING
    ('bank checks the shadow', BANK, 'NOTHING BUILDABLE'),
    ('bank reports the profile unchanged', BANK, '470 PRINTS, UNCHANGED'),
    ('bank restates three conditions from the list', BANK, 'COUNTED FROM THAT LIST'),
    ('bank names the fold as next with its arc', BANK, 'THE ARC IS b297-b306'),
    ('bank restates the patent receipts', BANK, 'NO RECEIPT LOCATED'),
    ('bank says the patent lane is unverified by this seat', BANK, 'VERIFIED BY THIS SEAT'),
    ('bank keeps M-2 unchanged', BANK, '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1: ### STILL UNPAID"),
    ('bank states what it did not check', BANK, 'NOT CHECKED THIS ACT'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    # ### THE REGISTRATION
    ('registration pulls the three falsifiers verbatim', REG, "the corpus's archimedean trace is"),
    ('registration carries their provenance', REG, 'THE AUTHOR, BY THE b306 FERRY'),
    ('registration fixes the not-partly-same rule in advance', REG, 'only if both are'),
    ('registration is sealed before the bank', REG, 'SEALED BEFORE THE BANK'),
    # ### THE RUN LOGS
    ('the difference run reports no failing checks', DRUN, '### CHECKS FAILING : 0'),
    ('the difference run reports the uniform sign', DRUN, 'UNIFORMLY NEGATIVE'),
    ('the difference run prints the junction disagreement', DRUN, 'DIFFERS AT THE LAST PRINTED'),
    ('the sweep log reports its attribution', SRUN, 'THE ROW NUMBER IS THE ATTRIBUTION'),
]

MUST_FAIL = [
    ('the two differences are not called the same', BANK, 'THE TWO DIFFERENCES ARE THE SAME.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('no measurement is invalidated', BANK, 'E2even IS WRONG.'),
    ('the source is not doubted', BANK, 'THEOREM 1 IS WRONG.'),
    ('no grade is moved', BANK, 'E2even IS DERIVED.'),
    ('the junction grade is not moved', BANK, 'THE JUNCTION IS AT BENCH.'),
    ('the closed route is not reopened', BANK, 'C3-VIA-SCALING IS REOPENED.'),
    ('no ancestor row is claimed rewritten', BANK, 'ROW 101 IS REWRITTEN.'),
    ('the corpus cell is not called an instance', BANK,
     'THE CORPUS CELL IS AN INSTANCE OF THEOREM 1.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the patent lane is not confirmed', BANK, 'THE RECEIPTS ARE CONFIRMED.'),
    ('the struck phrase is not used', BANK, 'HANDOFF CURRENT.'),
]

TOOLNUM = [
    ("the shared-target sweep's hits and their attribution", 'tools/b306_stem_scope.py'),
    ("the difference identity, its tolerance and the per-cell residuals", 'tools/b306_difference.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b306_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b306_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b306_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b306_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b306' in x)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b306 -- GATE SUITE')
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

    # ### G-QUOTE (G1).
    print('\n  G-QUOTE (G1: Component 1 quotations carry equation or page locations):')
    eqs = len(re.findall(r'eq\. \(\d+\)', bank))
    pgs = len(re.findall(r'page index \d+', bank))
    okq = eqs >= 5 and pgs >= 4
    print('    equation citations : %d ; page-index citations : %d ; %s'
          % (eqs, pgs, 'PASS' if okq else '### FAIL ###'))
    if not okq:
        fails.append('G-QUOTE')

    # ### G-RESEMBLANCE (G2).
    print('\n  G-RESEMBLANCE (G2: the resemblance is named AND refused as evidence):')
    named = 'THE RESEMBLANCE, NAMED AND REFUSED' in bank
    refused = 'IT IS NOT EVIDENCE' in bank or 'IS NOT EVIDENCE' in bank
    scoped = 'SHARE A SHAPE AND NOTHING ELSE' in bank
    print('    named : %s ; refused : %s ; the scope sentence carried : %s'
          % (named, refused, scoped))
    if not (named and refused and scoped):
        fails.append('G-RESEMBLANCE')

    # ### G-DECIDE (G4).
    print('\n  G-DECIDE (G4: a DIFFERENT verdict quotes the first differing constituent):')
    verdict = 'THE VERDICT: ### DIFFERENT' in bank
    first = 'THE FIRST DIFFERING CONSTITUENT IS THE' in bank
    quoted = 'NEITHER PAIRED FAMILY LIES IN THE' in bank
    notundec = 'NOT `UNDECIDED`' in bank
    print('    verdict stated : %s ; first constituent named : %s ; quotation given : %s ;'
          ' UNDECIDED explicitly excluded : %s' % (verdict, first, quoted, notundec))
    if not (verdict and first and quoted and notundec):
        fails.append('G-DECIDE')

    # ### G-NOMOVE (G13).
    print('\n  G-NOMOVE (G13: no grade moves and no measurement is disturbed):')
    mv = re.compile(r'\b(grade moves to|we promote|promoted to derives|is now derived|'
                    r're-verdict(?:ed|s)?)\b', re.I)
    mhits = [ln for ln in bank.splitlines() if mv.search(ln)]
    says = 'NO GRADE MOVES' in bank and 'NO MEASUREMENT IS DISTURBED' in bank
    dpos = bool(mv.search('and E2even is now derived'))
    dneg = not mv.search('NO GRADE MOVES AND NO MEASUREMENT IS DISTURBED')
    print('    grade-moving lines : %d  %s' % (len(mhits), 'PASS' if not mhits else '### FAIL ###'))
    print('    the bank says both refusals : %s' % says)
    print('    DISCRIMINATION: fires on a real promotion : %s ; quiet on the refusal : %s'
          % (dpos, dneg))
    if mhits or not says or not dpos or not dneg:
        fails.append('G-NOMOVE')

    # ### G-SHARED (G14) -- ### **THE EXTENDED SWEEP, WITH THE ALLOWED HITS PINNED.**
    print('\n  G-SHARED (G14: the extended sweep, and ONLY the two ancestors\' rows may hit):')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if not os.path.exists(path):
            continue
        for label, _stem, _text in b306_stem_scope.sweep(path):
            got.add((name, label))
    extra = got - ALLOWED_SHARED_HITS
    missing = ALLOWED_SHARED_HITS - got
    print('    hits found   : %s' % sorted(got))
    print('    allowed      : %s' % sorted(ALLOWED_SHARED_HITS))
    print('    UNEXPECTED   : %d %s  %s'
          % (len(extra), sorted(extra), 'PASS' if not extra else '### FAIL ###'))
    print('    expected-but-absent : %d %s   ### an ancestor row silently changed would show here'
          % (len(missing), sorted(missing)))
    if extra or missing:
        fails.append('G-SHARED')

    # ### G-ANCESTOR -- ### **THE TABLE'S PRE-EXISTING ROWS ARE BYTE-UNCHANGED.**
    print('\n  G-ANCESTOR (G14: no ancestor\'s correspondence row was rewritten):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    prefix = now.startswith(head.rstrip('\n'))
    print('    the committed table is a TRUE PREFIX of the current one : %s  %s'
          % (prefix, 'PASS' if prefix else '### FAIL ###'))
    print('    ### **A PREFIX CHECK OVER TEXT IS WHAT PROVES NOTHING EARLIER WAS TOUCHED** --')
    print('    ### appending is the only permitted change and this is what says so.')
    if not prefix:
        fails.append('G-ANCESTOR')

    # ### G-NOBUILD (G8).
    print('\n  G-NOBUILD (G8: nothing built; the profile does not move):')
    prof = io.open(PROFILE, 'rb').read()
    phead = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'],
                           capture_output=True).stdout
    identical = (prof == phead)
    dirty = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                           capture_output=True, text=True).stdout.strip()
    lean_rows = [x for x in dirty.splitlines() if x.strip().endswith('.lean')]
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    print('    profile BYTE-IDENTICAL to git HEAD : %s  %s'
          % (identical, 'PASS' if identical else '### FAIL ###'))
    print('    `.lean` files changed : %d  %s'
          % (len(lean_rows), 'PASS' if not lean_rows else '### FAIL ###'))
    print('    prints on disk : %d   ### unchanged by this act' % len(lines))
    if not identical or lean_rows:
        fails.append('G-NOBUILD')

    # ### G-NOAGG (G5).
    print('\n  G-NOAGG (G5):')
    claim = re.compile(r'\b(the aggregation is|we state the aggregation|M-2 is (?:now )?stated)\b',
                       re.I)
    ahits = [ln for ln in bank.splitlines() if claim.search(ln)]
    unchanged = '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`' in bank
    print('    aggregation-claim lines : %d  %s'
          % (len(ahits), 'PASS' if not ahits else '### FAIL ###'))
    print('    M-2\'s row present and unchanged : %s' % unchanged)
    if ahits or not unchanged:
        fails.append('G-NOAGG')

    # ### G-STRUCK, G-STEM, G-TOOLNUM, G-NOPAPERS, G-SEAL.
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

    print('\n  G-STEM (every file this act wrote, EXCEPT the declared carriers):')
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
    # ### THE CARRIERS, REPORTED SEPARATELY AS b300's STATED EXCEPTION.
    for p in FIXTURE_CARRIERS:
        if not os.path.exists(p):
            continue
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                      [], stem_list)
        print('    %-44s stem hits : %d  ### DECLARED CARRIER'
              % (os.path.basename(p) + ' (EXCEPTION)', len(sh)))
    print('    ### **`b306_stem_scope.txt` IS A CARRIER BY NECESSITY: ### A SWEEP LOG THAT REPORTS')
    print('    ### A HIT MUST QUOTE THE LINE IT HIT.** ### The ancestor row it names is b284\'s,')
    print('    ### and a report of a hit is not a new hit.')
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
    print('    untracked (pre-existing) : %d ; written after the seal : %d  %s'
          % (len(untracked), len(newer), 'PASS' if not newer else '### FAIL ###'))
    if tracked or newer:
        fails.append('G-NOPAPERS')

    print('\n  G-SEAL:')
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

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 11
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
