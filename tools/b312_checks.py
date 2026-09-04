# -*- coding: utf-8 -*-
"""b312_checks.py -- THE GATE SUITE FOR A DECISION AT DEFINITIONS THAT FOUND SOMETHING.

### ### **THE THREE ARMS THAT MATTER THIS ACT:**
###   ### **`G-NOREVERDICT`** ### -- the act found a discrepancy in an instrument the corpus has
###     computed with for a month, and ### **THE ONE THING IT MUST NOT DO IS TURN THAT INTO A
###     ### VERDICT ON A MEASUREMENT.** ### Its must-fail fixtures are the sentences this act would
###     have written if it had.
###   ### **`G-NOENTAIL`** ### -- Component 3 is ordered on `SAME` only, and a weakened version of
###     it would be the same drift in softer words.
###   ### **`G-NOARCHNUM`** ### -- no archimedean number computed, checked STRUCTURALLY: the act's
###     four new tools contain no arithmetic at all.
### ### **AND `G-UNFOLD` IS NEW AND IS THE ORDER'S OWN CONDITION:** ### the decision must be made by
### unfolded definitions and NOT by a shared letter, a shared shape, or a shared position. ### Its
### arm is that the act's own tools measure their locator UNFIT for the question first.
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
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def e(n):
    return os.path.join(E16, n)


BANK = d('b312_the_remainder.txt')
REG = d('b312_registration_2026-09-03.txt')
RUN = d('b312_components_run.txt')
PIN = d('b312_source_pin.txt')
SCAN = d('b312_ferry_scan.txt')
FERRY = d('b312_ferry_2026-09-03.txt')
CENSUS = d('b312_census.txt')

OWNED = [RUN, PIN, CENSUS,
         d('b312_corr_row.txt'), d('b312_index_query.txt'), d('b312_pins_stepzero.txt'),
         d('b312_regspec_run.txt'), d('b312_satisfiable.json'),
         t('b312_regspec.py'), t('b312_correspondence.py'), t('b312_components.py'),
         t('b312_source.py'), t('b312_definitions.py')]

CARRIERS = [
    (t('b312_checks.py'), 'its own fixtures'),
    (t('b312_index_append.py'), 'its own fixtures'),
    (BANK, 'it is the act\'s own voice and is scanned as such'),
    (REG, 'it is the sealed registration'),
    (FERRY, 'IT IS THE ORDER -- not this act\'s writing'),
    (SCAN, 'it is the scan\'s own log'),
]

OWNER_NEEDLES = [
    ("the corpus's identity, in the file that assembles it",
     e('b38_act10.py'), 'resid = TrN - A - E2N'),
    ("### the corpus's remainder side, as that identity consumes it",
     e('b38_act10.py'), 'out[:, k] = lam2 / (1 - lam2)'),
    ("### and the corpus's TRACE side, in the SAME file",
     e('b38_act10.py'), 'An[i] = math.sqrt(lamd)'),
    ("### and how the remainder becomes the identity's second term",
     e('b38_act10.py'), 'return 2.0 * float(np.trapezoid(cu * eu, uu))'),
    ("the corpus CLAIMING the import, in its own header",
     e('qeps_layer.py'), 'eps(rho), their (85)'),
    ("### the corpus DECLARING the scaling convention, and its reason",
     e('qeps_layer.py'), 'the convention forced by the'),
    ("### the corpus's operator image, transcribed with the OTHER exponent",
     e('qeps_layer.py'), 'C_n(rho) = rho^(1/2)'),
    ("### the corpus's ONE cross-check against the source",
     e('qeps_layer.py'), 'CONSEQUENCE DERIVED HERE, NOT ASSUMED'),
    ("the banked atlas, where the archimedean sign comes from",
     e('carto_atlas.py'), 'sign fixed BY the E2 calibration'),
    ("### and the atlas's own disclaimer about that sign",
     e('carto_atlas.py'), 'No sign claim is made'),
    ("b286 -- the source's space", d('b286_the_cc_condition.txt'), 'THE SPACE IS `L^2(R)_ev`.'),
    ("b292 -- the instrument vectors are NOT in it",
     d('b292_the_identification.txt'), 'IS NOT IN `S(1,1)`'),
    ("b285 -- the hazard register's own sentence",
     d('b285_archimedean_opening.txt'), 'THE WORD SURVIVES; THE OBJECT DOES NOT'),
    ("b200 -- the double-name species, named", d('b200_sector_naming.txt'),
     'THE DOUBLE-NAME SPECIES'),
    ("b219 -- and the act where it was REALISED",
     d('b219_what_sigma_even_weights.txt'), 'DOUBLE-NAME'),
    ("b301 -- the normalization work-order, still live",
     d('b301_the_object_completed.txt'), 'W-ORD-ARCH-NORM-READING'),
    ("b304 -- the artefact's pin", d('b304_the_demands_shape.txt'), 'b8e0b54a'),
    ("b305 -- the arithmetic's local factor",
     d('b305_the_arithmetics_entry.txt'), 'W_p(f) = (log p) SUM_{m>=1}'),
    ("b310 -- the finite-side result, quarantined",
     d('b310_the_smear_collapses.txt'), 'SIGNED COUNT OF THE OFF-BALL POINTS'),
    ("b311 -- the decision this act stands after",
     d('b311_the_identitys_neighbourhood.txt'), 'DOES NOT TYPE AT THE ARCHIMEDEAN PLACE'),
]

SELF_NEEDLES = [
    ('bank states the verdict up front', BANK, 'NO. ### DIFFERENT.'),
    ('bank says the factor is not a scalar', BANK, 'IS NOT A SCALAR'),
    ('### bank refuses the verdict-on-a-measurement reading FIRST', BANK,
     'IT DOES NOT SAY THAT ANY BANKED NUMBER IS WRONG'),
    ('bank gives the corpus\'s imported equation', BANK, 'their (85)'),
    ('bank gives the corpus\'s declared convention', BANK, 'the convention forced'),
    ('bank gives the corpus\'s unfolded code', BANK, 'INT_{1/rho}^{1} an(u) an(rho u) du'),
    ('bank gives the corpus\'s identity', BANK, 'resid = TrN - A - E2N'),
    ('bank separates eps_even from eps', BANK, 'EVEN-INDEX SUB-SUM'),
    ('bank gives the source\'s Theorem 4.7', BANK, 'W_inf(f) + INT f(rho^-1) eps(rho) d*rho'),
    ('bank gives the source\'s defining equation', BANK,
     'sum_n [lam(n)/sqrt(1-lam(n)^2)]'),
    ('bank gives the source\'s scaling action', BANK, 'lam^{-1/2} xi(lam^{-1} v)'),
    ('bank gives the source\'s unfolded remainder', BANK, 'rho^{+1/2} INT_{rho^-1}^{1}'),
    ('bank gives the constituent table', BANK, 'THE CONSTITUENTS, MATCHED ONE BY ONE'),
    ('bank derives the squared coefficient rather than assuming it', BANK,
     'so the unfolded coefficient is its square'),
    ('### bank measures its own locator unfit BEFORE using it', BANK,
     'FLATTEN TO THE SAME STRING'),
    ('bank says a control that cannot fire reads as a pass', BANK,
     'A CONTROL THAT CANNOT FIRE READS AS A PASS'),
    ('bank quotes the differing constituent at full prominence', BANK,
     'THE SCALING ACTION\'S NORMALIZATION EXPONENT'),
    ('bank quotes the raw extraction', BANK, 'ρ1{2'),
    ('bank gives the three corroborations', BANK, 'THREE THINGS THAT MAKE THE VERDICT HARDER'),
    ('bank reports the corpus disagreeing with itself', BANK,
     'ONE IDENTITY, TWO CONVENTIONS, ONE FILE'),
    ('bank refutes the corpus\'s stated reason', BANK,
     'A SUPPORT CONDITION FIXES A DOMAIN, NOT AN AMPLITUDE'),
    ('bank derives the invisibility', BANK, 'FOR EVERY `s` WHATEVER'),
    ('bank checks the atlas rather than assuming', BANK, 'sign fixed BY the E2 calibration'),
    ('bank says the atlas is not being complained about', BANK,
     'NOT A COMPLAINT ABOUT THE ATLAS'),
    ('bank leaves the equation numbers unsettled', BANK, 'CANNOT CHECK IT AND DOES NOT'),
    ('bank files the work-order rather than running it', BANK, 'W-ORD-REMAINDER-EXPONENT'),
    ('bank names the exact check the next act owes', BANK, 'NOTHING ELSE TOUCHED'),
    ('### bank says Component 3 does not run', BANK, 'IT DOES NOT RUN'),
    ('bank refuses the cause claim by name', BANK, 'NO CLAIM IS MADE ABOUT THE IMBALANCE'),
    ('bank reports the expectation refuted', BANK, 'REFUTED'),
    ('bank names the third normalization failure', BANK, 'THIRD ACT RUNNING'),
    ('bank gives the import ledger', BANK, 'THE IMPORT LEDGER'),
    ('bank states the ledger\'s own limit', BANK, 'DID NOT VERIFY A SINGLE PROOF'),
    ('bank restates the object\'s three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged under its cap', BANK, 'UNDER b310'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'DAYS PAST BOTH, AND'),
    ('bank records the W2 ruling verbatim', BANK, 'a mean-zero variant of the corpus'),
    ('bank marks the ruling recorded and not applied', BANK, 'RECORDED, NOT APPLIED'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank carries the hook work-order', BANK, 'W-ORD-HOOK-COVERAGE'),
    ('### bank names the fold and the act that comes before it', BANK,
     'THE NEXT ACT IS A FRESH-CLONE CERTIFICATION TEST'),
    ('bank gives the reason the certification precedes the fold', BANK,
     'IS A SUMMARY, NOT A'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank reports the shadow as nothing', BANK, 'NOTHING IS WHAT IT IS'),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('bank declares its deviations', BANK, 'DEVIATIONS, DECLARED'),
    ('registration declares the read preceded the seal', REG,
     'so the read is done and section (5) records what it found'),
    ('registration refuses to dress a finding as a prediction', REG, 'IT IS NOT DONE HERE'),
    ('registration records the verdict on the expectation', REG, 'REFUTED, AND REFUTED AT THE'),
    ('registration caps banked measurements called wrong', REG, 'banked measurements called wrong'),
    ('registration caps the entailment', REG, 'entailments run on a non-SAME verdict'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the verdict', RUN, 'DIFFERENT'),
    ('the run reports the extraction side by side', RUN, 'THE EXTRACTION, SIDE BY SIDE'),
    ('the pin log reports the hash match', PIN, 'MATCHES THE ARTEFACT b304 PINNED'),
    ('the pin log reports the text layer intact', PIN,
     'pages with NO text layer at all         : 0'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### ### **`G-NOREVERDICT` -- THE SENTENCES A VERDICT ON A MEASUREMENT WOULD HAVE PRODUCED.**
    ('no banked number is called wrong', BANK, 'THE BANKED NUMBERS ARE WRONG.'),
    ('the identity is not called broken', BANK, 'THE CORPUS IDENTITY IS BROKEN.'),
    ('the residue is not re-verdicted', BANK, 'THE BANKED RESIDUE IS AN ARTEFACT OF THE FACTOR.'),
    ('no act is re-verdicted', BANK, 'b38 IS RE-VERDICTED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    # ### **`G-NOENTAIL`.**
    ('the entailment is not run', BANK, 'THE ENTAILMENT RUNS ANYWAY.'),
    ('the identity is not restated as the source theorem', BANK,
     'THE CORPUS IDENTITY IS THE SOURCE THEOREM WITH THE FINITE PLACES ATTACHED.'),
    ('the imbalance is not explained', BANK, 'THE FACTOR EXPLAINS THE IMBALANCE.'),
    # ### **`G-NOARCHNUM` AND THE READ'S OWN LIMITS.**
    ('no archimedean number is computed', BANK, 'THE ARCHIMEDEAN VALUE IS COMPUTED.'),
    ('no proof of the source is claimed verified', BANK, 'THE SOURCE PROOF IS VERIFIED.'),
    ('the Selecta edition is not checked', BANK, 'THE SELECTA EDITION IS CHECKED.'),
    # ### **`G-RULING` AND THE STANDING CAPS.**
    ('the ruling is not applied', BANK, 'THE W2 VARIANT IS BUILT.'),
    ('the branch is not decided', BANK, 'THE BRANCH IS DECIDED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the fold is not folded', BANK, 'THE FOLD IS DONE.'),
]

TOOLNUM = [
    ("the artefact's hash, its page count and every fragment location",
     'tools/b312_source.py'),
    ("the two exponents, extracted rather than asserted", 'tools/b312_definitions.py'),
    ("the flattener and the hash check the source tool imports", 'tools/b305_source.py'),
    ("the truncation detector that measured the text layer", 'tools/b303_source.py'),
    ("the components' tables and verdicts", 'tools/b312_components.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits and their attribution", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b312_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b312_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b312_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b312_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
    ("the byte checks the profile comparison imports", 'tools/b302_kernel.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b312' in x)

# ### ### **`G-NOARCHNUM`'s STRUCTURAL ARM.**
ARITH = re.compile(r'(?<![\w.])\d+\.\d+|(?<![\w.])\d+[eE][-+]?\d+|\bFraction\b|\bmath\.|'
                   r'\bfloat\s*\(')
STRINGS = re.compile(r"'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"")


def _strip_strings(line):
    return STRINGS.sub(lambda m: ' ' * len(m.group(0)), line)


def arith_sites(path):
    out = []
    for i, line in enumerate(io.open(path, encoding='utf-8', errors='replace').read().splitlines(),
                             1):
        s = line.strip()
        if s.startswith('#'):
            continue
        if ARITH.search(_strip_strings(line)):
            out.append((i, s))
    return out


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b312 -- GATE SUITE (A DECISION AT DEFINITIONS THAT FOUND SOMETHING)')
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
    print('    ### **THE FIRST FIVE ARE `G-NOREVERDICT`: the sentences a verdict on a MEASUREMENT')
    print('    ### would have produced, which is the one drift this act had to guard against. ###')
    print('    ### THE NEXT THREE ARE `G-NOENTAIL`.**')

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()

    # ### G-SOURCE.
    print('\n  G-SOURCE (the artefact pinned BEFORE it was read; every fragment located):')
    pin = io.open(PIN, encoding='utf-8').read()
    matched = 'MATCHES THE ARTEFACT b304 PINNED : True' in pin
    layer = 'pages with NO text layer at all         : 0' in pin
    located = pin.count('FRAGMENTS NOT LOCATED : 0') >= 2
    print('    hash matches the corpus pin : %s ; text layer intact : %s ; fragments located : %s'
          % (matched, layer, located))
    if not (matched and layer and located):
        fails.append('G-SOURCE')

    # ### G-UNFOLD -- ### **NEW, AND IT IS THE ORDER'S OWN CONDITION.**
    print('\n  G-UNFOLD (the decision by UNFOLDED DEFINITIONS, not by a shared letter):')
    unfit = 'FLATTEN TO THE SAME STRING' in bank
    tworuns = ('THE EXTRACTION, SIDE BY SIDE' in run
               and 'off the RAW page text' in run
               and chr(961) + '1{2' in run)
    refused = 'WHICH IS EXACTLY WHY THE SHAPE DECIDES' in bank
    table = 'THE CONSTITUENTS, MATCHED ONE BY ONE' in bank
    print('    locator measured unfit first : %s ; raw extraction in the run : %s'
          % (unfit, tworuns))
    print('    the shared shape refused by name : %s ; constituent table present : %s'
          % (refused, table))
    if not (unfit and tworuns and refused and table):
        fails.append('G-UNFOLD')

    # ### G-NOARCHNUM -- the structural arm.
    print('\n  G-NOARCHNUM (no archimedean number computed -- checked STRUCTURALLY):')
    tot = 0
    for path in (t('b312_source.py'), t('b312_definitions.py'), t('b312_components.py'),
                 t('b312_regspec.py')):
        sites = arith_sites(path)
        tot += len(sites)
        print('    %-26s arithmetic sites : %d' % (os.path.basename(path), len(sites)))
        for i, s in sites:
            print('        ### line %-5d %s' % (i, s[:84]))
    fx = (bool(ARITH.search('x = 1.5')) and bool(ARITH.search('v = Fraction(1, 2)'))
          and not bool(ARITH.search('for i in range(len(pages)):')))
    print('    fixture arms agree : %s' % fx)
    print('    ### **THE ACT\'S FOUR NEW TOOLS CONTAIN NO ARITHMETIC AT ALL.** ### Every exponent')
    print('    ### the bank reports is an EXTRACTED STRING, and every archimedean quantity it names')
    print('    ### is a LOCATED QUOTATION.')
    if tot or not fx:
        fails.append('G-NOARCHNUM')

    # ### G-NOREVERDICT -- beyond the must-fail arm, the positive one.
    print('\n  G-NOREVERDICT (the finding is about definitions, not about measurements):')
    says = ('IT DOES NOT SAY THAT ANY BANKED NUMBER IS WRONG' in bank
            and 'NO ACT IS RE-VERDICTED' in bank.upper())
    filed = ('W-ORD-REMAINDER-EXPONENT' in bank and 'THIS ACT MAY NOT RUN IT' in bank)
    mv = re.compile(r'\b(grade moves to|we promote|promoted to derives|is now derived|'
                    r'this act re-verdicts)\b', re.I)
    mhits = [ln for ln in bank.splitlines() if mv.search(ln)]
    dpos = bool(mv.search('and b310 is now derived'))
    print('    the refusal is stated : %s ; the work-order is filed not run : %s' % (says, filed))
    print('    grade-moving lines : %d ; discrimination : %s' % (len(mhits), dpos))
    if not (says and filed and dpos) or mhits:
        fails.append('G-NOREVERDICT')

    # ### G-NOENTAIL.
    print('\n  G-NOENTAIL (Component 3 ordered on SAME only, and the verdict is DIFFERENT):')
    notrun = 'IT DOES NOT RUN' in bank
    quar = 'stays quarantined at its own scope' in bank
    nocause = 'NO CLAIM IS MADE ABOUT THE IMBALANCE' in bank
    print('    Component 3 declared not run : %s ; b310 stays quarantined : %s ; no cause : %s'
          % (notrun, quar, nocause))
    if not (notrun and quar and nocause):
        fails.append('G-NOENTAIL')

    # ### G-RULING.
    print('\n  G-RULING (the author\'s W2 recorded VERBATIM and NOT applied):')
    verbatim = 'a mean-zero variant of the corpus' in bank and 'replacing nothing' in bank
    notapplied = 'RECORDED, NOT APPLIED' in bank
    print('    verbatim : %s ; NOT applied : %s' % (verbatim, notapplied))
    if not (verbatim and notapplied):
        fails.append('G-RULING')

    # ### G-NOBUILD.
    print('\n  G-NOBUILD (the profile must NOT move: nothing was ordered built):')
    prof = KRN.normalise(io.open(PROFILE, 'rb').read())
    phead = KRN.normalise(KRN.git_show('AXIOM_PRINTS.txt') or b'')
    identical = (prof == phead)
    dirty = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                           capture_output=True, text=True).stdout
    lean_rows = [x for x in dirty.splitlines() if x.strip().endswith('.lean')]
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    print('    profile identical to git HEAD (NORMALISED) : %s ; `.lean` changed : %d ; prints : %d'
          % (identical, len(lean_rows), len(lines)))
    if not identical or lean_rows:
        fails.append('G-NOBUILD')

    # ### G-NOPAPERS / G-ANCESTOR.
    print('\n  G-NOPAPERS / G-ANCESTOR:')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    print('    PLACE-papers tracked changes : %d ; table is a TRUE PREFIX : %s'
          % (len(tracked), pfx))
    if tracked:
        fails.append('G-NOPAPERS')
    if not pfx:
        fails.append('G-ANCESTOR')

    # ### G-STRUCK / G-STEM.
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(e_['patterns']) for e_ in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-30s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        hit = bool(ferry_scan.scan_text(text, struck, stem_list)[0])
        fired_disc += 1 if hit else 0
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s'
          % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s' % sorted(got))
    print('    UNEXPECTED : %d  %s' % (len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
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

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 12
    print('\n' + '=' * 100)
    print('### COUNTS, PRINTED BY THIS TOOL SO THE BANK NEVER TYPES ONE AT A SHELL:')
    print('    owner needles %d   self needles %d   must-fail fixtures %d'
          % (len(OWNER_NEEDLES), len(SELF_NEEDLES), len(MUST_FAIL)))
    print('    declared carriers %d   toolnum rows %d' % (len(CARRIERS), len(TOOLNUM)))
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
