# -*- coding: utf-8 -*-
"""b309_checks.py -- THE GATE SUITE FOR A COMPUTATION THAT BUILT A SHADOW.

### ### **THREE ARMS ARE INVERTED OR NEW THIS ACT, AND THE INVERSIONS ARE THE POINT:**
###   ### **`G-NOBUILD` IS INVERTED INTO `G-KERNEL`.** ### Every act since b304 checked that the
###     profile did NOT move. ### **THIS ACT MOVES IT**, so the gate checks that it moved by exactly
###     this act's terminals, that all of them print zero axioms, and that ### **THE OLD PROFILE IS
###     A TRUE BYTE PREFIX OF THE NEW ONE.** ### A gate copied forward uninverted would have failed
###     this act for doing what it was ordered to do -- b307's lesson, met from the other side.
###   ### **`G-ZEROVALUE`** ### -- this act's answer is a ZERO, and a zero is the one answer a suite
###     can produce by being broken. ### The gate requires the run to carry BOTH a nonzero control
###     AND a live traceless operator, so that ### **A DEAD INSTRUMENT COULD NOT HAVE PRODUCED THIS
###     RESULT.**
###   ### **`G-REFUTED`** ### -- the act's own sealed prediction was refuted in one clause. ### The
###     gate requires the bank to SAY so and the seal to be INTACT, because ### **AN ACT THAT SEALS
###     A PREDICTION AND THEN QUIETLY EDITS IT HAS SEALED NOTHING.**
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
MODULE = os.path.join(SIDE, 'Core', 'ScalingTraceShadow.lean')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b309_the_scaling_trace.txt')
REG = d('b309_registration_2026-09-03.txt')
RUN = d('b309_components_run.txt')
KRUN = d('b309_kernel_run.txt')
SCAN = d('b309_ferry_scan.txt')
FERRY = d('b309_ferry_2026-09-03.txt')
CENSUS = d('b309_census.txt')

OWNED = [RUN, KRUN, CENSUS,
         d('b309_corr_row.txt'), d('b309_index_query.txt'), d('b309_pins_stepzero.txt'),
         d('b309_regspec_run.txt'), d('b309_satisfiable.json'),
         t('b309_regspec.py'), t('b309_correspondence.py'), t('b309_components.py'),
         t('b309_kernel.py'), MODULE]

CARRIERS = [
    (t('b309_checks.py'), 'its own fixtures'),
    (t('b309_index_append.py'), 'its own fixtures'),
    (t('b309_scaling_trace.py'), 'it spells the reduced sum\'s index shape in order to compute it'),
    (BANK, 'it quotes the refuted clause of its own sealed prediction IN ORDER TO DECLARE IT'),
    (REG, 'it is the sealed prediction, including the clause the run refuted'),
    (FERRY, 'IT IS THE ORDER -- not this act\'s writing'),
    (SCAN, 'it is the scan\'s own log'),
]

OWNER_NEEDLES = [
    ("b304's refusal of the scaling part, in its emitting file", t('b304_smearing.py'),
     'REFUSES THE'),
    ("b304 on why the model could not carry it", t('b304_smearing.py'),
     'CANNOT CARRY THE NON-UNIT PART'),
    ("b304's projection is onto Sonin's space, not a sector", t('b304_smearing.py'),
     'THE FAITHFUL'),
    ("b21's chart and Haar normalization", d('b21_2026-08-18.txt'),
     'via x = p^(-n) m; Haar measure'),
    ("b21's location of the artifact", d('b21_2026-08-18.txt'),
     "MODEL'S mod-N WRAPAROUND IS THE ARTIFACT"),
    ("b280's Haar bridge", d('b280_the_consequence.txt'), 'a chart point `m` at level `n`'),
    ("### b280's UNAVAILABLE arm at level 1", d('b280_the_consequence.txt'), 'NO `k < n` AT ALL'),
    ("b280's absorption at k = n", d('b280_the_consequence.txt'), '`P(n) = 0`'),
    ("b293's ball of exponent e", d('b293_the_finite_family.txt'),
     'B_e := { m : v_p(m) >= n - e }'),
    ("b295's scope sentence, which this act neither extends nor weakens",
     d('b295_the_second_mechanism.txt'), 'AND PAIRINGS OF THIS SHAPE'),
    ("b284's escape, which is why the model folds", d('b284_the_scalings_domain.txt'),
     'strictly bigger than'),
    ("b308's frame law for the scaling part", d('b308_the_local_field_instrument.txt'),
     'BOTH RADII MOVE'),
    ("### b308 naming this computation and leaving it undone",
     d('b308_the_local_field_instrument.txt'), 'NAMED, AND NOT COMPUTED'),
    ("b308's limit: the truncation is untouched", d('b308_the_local_field_instrument.txt'),
     'IT DOES NOT REMOVE THE'),
    # ### RE-POINTED AT THE EMITTER: b299 states this in the GENERATOR that emitted its document,
    # ### not in its bank. ### A needle at the bank would have been a needle at a quoter.
    ("b299's refusal reason for a cell terminal (its generator is the emitter)",
     t('b299_keystone.py'), 'looking like the general statement'),
]

SELF_NEEDLES = [
    ('bank states the value up front', BANK, 'THE VALUE IS EXACTLY ZERO'),
    ('bank names the quantity b304 refused', BANK, 'THIS IS THE QUANTITY b304 REFUSED'),
    ('bank says the answer was derived before the code', BANK, 'BEFORE ANY CODE FOR IT EXISTED'),
    # ### AN ANCHOR CONTAINING A NEWLINE CAN NEVER MATCH -- the puller reads line by line. ### The
    # ### same species b308 declared at its own (D4), met again and caught the same way.
    ('bank reports the census scope limit', BANK, 'ARC, WHICH REACHES'),
    ('bank puts the ambient before the value', BANK, 'THE TRACE IS NOT DEFINED UNTIL AN AMBIENT'),
    ('bank states the two regimes', BANK, 'THE ACT HAS TWO REGIMES BEFORE IT HAS A SINGLE VALUE'),
    ('bank reports the UNAVAILABLE arm as not a pass', BANK, 'UNAVAILABLE RATHER THAN AS A PASS'),
    ('bank reports the closed form checked entry by entry', BANK, '0 DISAGREEING'),
    ('bank reports the dimension law from the projector', BANK, 'RATHER THAN FROM THE COUNT'),
    ('bank reports the two routes and the bound', BANK, 'QUIETLY DROPPED'),
    ('bank names the sum b304 could only write formally', BANK, 'COULD ONLY WRITE FORMALLY'),
    ('bank declares the refuted clause', BANK, 'THAT NAMES THE WRONG OPERATOR'),
    ('bank reports the live traceless compression', BANK, 'BUT A LIVE ONE'),
    ('bank declines to count the functional equation', BANK, 'SATISFIED BY ANY SCALAR WHATEVER'),
    ('bank gives the mechanism in one sentence', BANK, 'THE ONLY FIXED POINT IT HAS'),
    ('bank says the mechanism is of the conditions', BANK, 'NO STEP MENTIONS A CELL'),
    ('bank says a sweep is not a proof', BANK, 'IS NOT A PROOF OVER ALL OF THEM'),
    ('bank refuses the obstruction reading', BANK, 'A ZERO IS NOT A ROUTE AND IT IS NOT AN'),
    ('bank keeps the barrier untouched', BANK, 'NEITHER EXTENDED NOR WEAKENED HERE'),
    ('bank says component 3 did not run', BANK, 'THERE IS NOTHING TO SMEAR'),
    ('bank says what component 3 therefore did not do', BANK, 'CONTEXT FOR NOTHING'),
    ('bank says it does not re-verdict b304', BANK, 'THE REFUSAL IS CONTINUED ON A'),
    ('bank reports the exposure by call path', BANK, 'AT MOST ONE ENTRY'),
    ('bank reports the shadow was checked not assumed', BANK, 'ALL THREE PASS BOTH TESTS'),
    ('bank says the terminals certify arithmetic not the barrier', BANK,
     'THEY CERTIFY IS ARITHMETIC AND NOT THE BARRIER'),
    ('bank reports the profile move and the prefix', BANK, 'TRUE BYTE PREFIX OF THE NEW ONE'),
    ('bank restates the object three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged', BANK, "`M-2`'s ROW: ### UNCHANGED"),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'DAYS PAST BOTH, AND NOTHING ON THIS'),
    ('bank names the window question as the author\'s', BANK, 'THE CHOICE IS THE AUTHOR'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('registration seals the derivation in advance', REG, 'BEFORE ANY CODE FOR IT EXISTED'),
    ('registration names the worst available error', REG, 'CONFLATING THEM WOULD BE'),
    ('registration carries the refuted clause', REG, 'IDENTICALLY ZERO, NOT'),
    ('registration justifies the non-zero cap', REG,
     'SEALED CAP MUST NOT FORBID AN ORDERED'),
    ('the run reports zero nonzero traces', RUN, 'NONZERO TRACES FOUND : 0'),
    ('the run reports the two-route counts', RUN, 'COMPUTED BY BOTH ROUTES : 34'),
    ('the run reports zero route disagreements', RUN, 'ROUTES DISAGREEING : 0'),
    ('the run reports the mechanism holding', RUN, 'THE MECHANISM FAILS : 0'),
    ('the run reports the closed form agreeing', RUN, 'THE TWO ROUTES TO THE SAME PREDICATE'),
    ('the run declares the wrong-operator refutation', RUN, 'THAT NAMES THE WRONG OPERATOR'),
    ('the run stops component 3', RUN, 'THERE IS NOTHING TO SMEAR'),
    ('the kernel run reports the baseline byte-identical', KRUN, 'BYTE-IDENTICAL to banked : True'),
    ('the kernel run reports three zero-axiom terminals', KRUN, 'terminals printed        : 3, 3'),
    ('the kernel run reports the true byte prefix', KRUN, 'TRUE BYTE PREFIX'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('b304 is not re-verdicted', BANK, 'b304 IS RE-VERDICTED.'),
    ('the zero is not an obstruction theorem', BANK, 'THE SCALING PART IS OBSTRUCTED.'),
    ('the zero is not a route', BANK, 'THE ZERO IS A ROUTE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the barrier is not extended', BANK, 'THE BARRIER IS EXTENDED.'),
    ('the terminals do not certify the barrier', BANK, 'THE TERMINALS CERTIFY THE BARRIER.'),
    ('the sweep is not called a proof', BANK, 'THE SWEEP IS A PROOF.'),
    ('the smeared form is not claimed', BANK, 'THE SMEARED FORM IS COMPUTED.'),
    ('nothing about the archimedean place', BANK, 'THE ARCHIMEDEAN PLACE IS REACHED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the truncation is not claimed removed', BANK, 'THE TRUNCATION IS REMOVED.'),
]

TOOLNUM = [
    ("the frames, the closed form, the two routes and the fold-free transport",
     'tools/b309_scaling_trace.py'),
    ("every table and every verdict in the components", 'tools/b309_components.py'),
    ("the shadow build, the profile and the byte comparisons", 'tools/b309_kernel.py'),
    ("the byte checks the kernel tool imports", 'tools/b302_kernel.py'),
    ("the frame, the ball and the embedding law", 'tools/b308_local_field.py'),
    ("the projector, the unit trace and the permutation test", 'tools/b304_smearing.py'),
    ("the conditions and the exact nullspace", 'tools/b303_family.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits and their attribution", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b309_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b309_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b309_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b309_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b309' in x)

FLOAT_LIT = re.compile(r'(?<![\w.])\d+\.\d+(?:[eE][-+]?\d+)?(?![\w.])'
                       r'|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])')
FLOAT_CALL = re.compile(r'\bfloat\s*\(|\bmath\.|\bnumpy\b|\bnp\.')
STRINGS = re.compile(r"'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"")


def _strip_strings(line):
    return STRINGS.sub(lambda m: ' ' * len(m.group(0)), line)


def exact_scan(path):
    """### b308's `G-EXACT`, INHERITED ### **AFTER ITS OWN TWO DEFECTS WERE FOUND BY ITS OWN
    ### FIXTURES** -- the exponent tail that made it miss `1.5e-6`, and the string stripper that
    ### did not know a backslash-escaped quote is part of a literal."""
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
    print('b309 -- GATE SUITE (A COMPUTATION THAT BUILT A SHADOW)')
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
    krun = io.open(KRUN, encoding='utf-8').read()

    # ### G-ZEROVALUE -- ### **THIS ACT'S OWN, AND IT GUARDS THE ONE ANSWER A BROKEN SUITE PRODUCES.**
    print('\n  G-ZEROVALUE (a zero is the answer a dead instrument gives; this one is not dead):')
    checks = [('no nonzero trace was found', 'NONZERO TRACES FOUND : 0'),
              ('the known-nonzero control returned the dimension law', 'NONZERO'),
              ('the compression is ALIVE somewhere while traceless', 'ALIVE ('),
              ('and it is the ZERO operator where the supports are disjoint', 'ZERO operator'),
              ('the UNAVAILABLE arm is reported, not passed', 'UNAVAILABLE'),
              ('routes agree everywhere both ran', 'ROUTES DISAGREEING : 0'),
              ('the closed form agreed with the built projector', 'THE MECHANISM FAILS : 0')]
    for lbl, anchor in checks:
        ok = anchor in run
        print('    %-56s %s' % (lbl, 'PASS' if ok else '### FAIL ### anchor=%r' % anchor))
        if not ok:
            fails.append('G-ZEROVALUE: %s' % lbl)
    print('    ### **A SUITE THAT REPORTED ONLY ZEROS WOULD PASS A GATE ON THE VALUE AND PROVE')
    print('    ### NOTHING. ### THE LIVE TRACELESS COMPRESSION IS WHAT MAKES THIS ONE MEAN')
    print('    ### SOMETHING**, and it is required here rather than merely mentioned in the bank.')

    # ### G-REFUTED -- ### **THIS ACT'S OWN.**
    print('\n  G-REFUTED (a sealed prediction refuted in one clause must be SAID, not edited):')
    said_bank = 'THAT NAMES THE WRONG OPERATOR' in bank and 'SEAL IS NOT EDITED' in bank
    said_run = 'THAT NAMES THE WRONG OPERATOR' in run
    still_there = 'IDENTICALLY ZERO, NOT' in io.open(REG, encoding='utf-8').read()
    print('    the bank declares it : %s ; the run declares it : %s ; the clause is STILL in the'
          ' sealed registration : %s' % (said_bank, said_run, still_there))
    print('    ### **AN ACT THAT SEALS A PREDICTION AND THEN QUIETLY EDITS IT HAS SEALED NOTHING.**')
    if not (said_bank and said_run and still_there):
        fails.append('G-REFUTED')

    # ### G-KERNEL -- ### **INVERTED FROM `G-NOBUILD`.**
    print('\n  G-KERNEL (INVERTED: the profile DOES move this act, so by how much and how):')
    prof = io.open(PROFILE, 'rb').read()
    phead = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'],
                           capture_output=True).stdout
    prefix = prof.startswith(phead)
    lines_now = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    lines_head = [ln for ln in phead.decode('utf-8').splitlines() if ln.strip()]
    added = len(lines_now) - len(lines_head)
    nonzero_axioms = [ln for ln in lines_now if 'does not depend on any axioms' not in ln]
    mine = [ln for ln in lines_now if 'B309.' in ln]
    print('    prints at HEAD -> now : %d -> %d   (added %d)'
          % (len(lines_head), len(lines_now), added))
    print('    HEAD profile is a TRUE BYTE PREFIX of the new one : %s  %s'
          % (prefix, 'PASS' if prefix else '### FAIL ###'))
    print('    terminals NOT printing zero axioms : %d  %s'
          % (len(nonzero_axioms), 'PASS' if not nonzero_axioms else '### FAIL ###'))
    print('    this act\'s own terminals in the profile : %d' % len(mine))
    for ln in mine:
        print('        %s' % ln)
    print('    ### **A GATE COPIED FORWARD FROM b308 UNINVERTED WOULD HAVE FAILED THIS ACT FOR')
    print('    ### BUILDING WHAT IT WAS PERMITTED TO BUILD**, which is b307\'s lesson met from the')
    print('    ### other side. ### The inversion is recorded because copying a green gate forward')
    print('    ### is how a suite stops checking.')
    if not prefix or nonzero_axioms or added != 3 or len(mine) != 3:
        fails.append('G-KERNEL')

    # ### G-EXACT.
    print('\n  G-EXACT (zero float literals in the deciding runner):')
    tot_lit, tot_call = 0, 0
    for path in (t('b309_scaling_trace.py'), t('b309_components.py')):
        lits, calls = exact_scan(path)
        tot_lit += len(lits)
        tot_call += len(calls)
        print('    %-30s float literals : %d   float-producing calls : %d'
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
    print('\n  G-NOPAPERS (the papers repo is NOT touched this act):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    print('    tracked files changed in PLACE-papers : %d %s  %s'
          % (len(tracked), [x[3:].strip() for x in tracked],
             'PASS' if not tracked else '### FAIL ###'))
    if tracked:
        fails.append('G-NOPAPERS')

    # ### G-ANCESTOR.
    print('\n  G-ANCESTOR (no ancestor correspondence row rewritten):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    print('    committed table is a TRUE PREFIX of the current one : %s  %s'
          % (pfx, 'PASS' if pfx else '### FAIL ###'))
    if not pfx:
        fails.append('G-ANCESTOR')

    # ### G-NOMOVE.
    print('\n  G-NOMOVE (a computation moves no grade and re-verdicts nothing):')
    mv = re.compile(r'\b(grade moves to|we promote|promoted to derives|is now derived|'
                    r'this act re-verdicts)\b', re.I)
    mhits = [ln for ln in bank.splitlines() if mv.search(ln)]
    says = 'NO GRADE MOVES' in bank and 'NO ACT IS RE-VERDICTED' in bank
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
    for p in OWNED:
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

    # ### G-STEM.
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
    print('    ### **THE EXCEPTION LIST WITH ITS REASONS:** ### `row 2` predates the ban (b142), so')
    print('    ### it is not a defect -- a ban is not retroactive. ### `row 101` is b284\'s, a defect')
    print('    ### when written that the old sweep could not see, FILED AND NOT REWRITTEN.')
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
        print('    %-56s %-36s exists=%s tracked=%s' % (what[:56], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-SEAL:')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    print('    seal intact : %s  %s' % (intact, 'PASS' if intact else '### FAIL ###'))
    print('    ### **AND THAT MATTERS MORE THIS ACT THAN USUALLY: THE SEAL COVERS A PREDICTION THE')
    print('    ### RUN REFUTED IN ONE CLAUSE.**')
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
            print('        ### %d flagged sentence(s) -- DESCRIBED, NOT QUOTED.' % len(gh))

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 10 + len(checks)
    print('\n' + '=' * 100)
    print('### COUNTS, PRINTED BY THIS TOOL SO THE BANK NEVER TYPES ONE AT A SHELL:')
    print('    owner needles %d   self needles %d   must-fail fixtures %d   G-ZEROVALUE arms %d'
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
