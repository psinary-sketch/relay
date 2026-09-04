# -*- coding: utf-8 -*-
"""b319_checks.py -- THE GATE SUITE FOR AN INSTRUMENT BUILD AND A KERNEL REPAIR.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-ONELEAN`** ### -- ### **THE CAP THAT WAS ZERO FOR SIXTEEN ACTS AND IS ONE HERE.**
###     Exactly one `.lean` file changed, and it is the certification file. ### **NO `Core/` MODULE
###     ### WAS TOUCHED**, which is what keeps the repair bookkeeping rather than mathematics.
###   ### **`G-PREFIX`** ### -- the old profile must be a LITERAL BYTE PREFIX of the new one. ### Not
###     a subset of its lines: a prefix. ### Read off the repair's own log.
###   ### **`G-ASPRINTED`** ### -- the axiom-bearing count is read off the PRINTED file, and if any
###     newly-certified terminal bore an axiom it would be at full prominence.
###   ### **`G-BARDEFECT`** ### -- ### **THE ONE THIS ACT COULD MOST EASILY HAVE BREACHED.** ### The
###     order asked for a nonempty reach; the sealed bar returns zero. ### The bank must report the
###     empty reach AND name its own bar's defect, and must NOT reinterpret the bar after the fact.
###   ### **`G-PINTRIED`** ### -- the second scheme was tried, on both axes, and refuted on one.
###   ### **`G-NOVERDICT`** ### -- the unit's residual is a MEASUREMENT. ### No membership verdict.
###   ### **`G-NOUNITDEF`** ### -- b317 and b318 refused any `sonin_unit` CALL. ### This act's order
###     requires one, so the cap becomes: ### **NO UNIT IS DEFINED HERE.** ### b316's construction is
###     imported; `def sonin_unit` appears in no tool of this act.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402  ### the stripper and git helper, IMPORTED not copied

D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS = ['tools/e16/carto_atlas.py', 'tools/e16/qeps_layer.py', 'tools/e16/b205_prolate.py',
          'tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
          'tools/b315_coverage_gate.py', 'tools/noise_floor.py', 'tools/b305_source.py',
          'tools/b317_extract.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b319_the_stable_rank.txt')
REG = d('b319_registration_2026-09-04.txt')
RUN = d('b319_components_run.txt')
REP = d('b319_coverage_repair.txt')
PIN = d('b319_pin.txt')
SCAN = d('b319_ferry_scan.txt')
FERRY = d('b319_ferry_2026-09-04.txt')
CENSUS = d('b319_census.txt')
EXTRACT = d('b319_extract_notes.txt')

OWNED = [RUN, REP, PIN, CENSUS, EXTRACT, d('b319_corr_row.txt'), d('b319_index_query.txt'),
         d('b319_index_run.txt'), d('b319_pins_stepzero.txt'), d('b319_regspec_run.txt'),
         d('b319_reg_termscan.txt'), d('b319_satisfiable.json'), d('b319_satisfiable_run.txt'),
         d('b319_rows.json'),
         t('b319_regspec.py'), t('b319_correspondence.py'), t('b319_run.py'),
         t('b319_stable.py'), t('b319_extract.py'), t('b319_coverage_repair.py'), t('b319_pin.py')]

CARRIERS = [
    (t('b319_checks.py'), 'its own fixtures'),
    (t('b319_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("the two projections, from the extract", EXTRACT, 'becomes the multiplication by the charac'),
    ("the spectral decomposition (81), from the extract", EXTRACT,
     'The spectral decomposition of the positive operator'),
    ("### and that its remainder IS the projection on the space", EXTRACT,
     'is the orthogonal projection on Sonin'),
    ("the eigenvalue-one characterization, from the extract", EXTRACT, 'is the eigenspace of'),
    ("the bandwidth parameter, from the extract", EXTRACT, 'with bandwidth parameter'),
    ("b318 -- the act that filed the order", d('b318_the_forced_sign.txt'),
     'THE REACH IS EMPTY AND THE RANK IS WHY'),
    ("b316 -- the limit this act may not cross", d('b316_the_archimedean_instrument.txt'),
     'NOT YET CERTIFIED FOR MEMBERSHIP QUESTIONS'),
    ("the grid scheme this act replaces", t('b316_instrument.py'), 'def subspace'),
    ("### and the unit this act imports rather than defines", t('b316_instrument.py'),
     'def sonin_unit'),
    ("the smear column, imported", t('b317_smear.py'), 'def compressed_trace'),
    ("the square, imported", t('b318_square.py'), 'def square_trace'),
    ("the coverage gate's own parsers, imported", t('b315_coverage_gate.py'), 'def targets_of'),
    ("the floor/drift gate", t('noise_floor.py'), 'def gate'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('bank gives the rank verdict', BANK, 'THE RANK HOLDS STILL'),
    ('### bank counts the rank changes both ways', BANK,
     'RANK CHANGES ALONG THAT LADDER: ### b316 ONE, THIS'),
    ('bank reports the grid half attained', BANK, 'THE GRID HALF OF THE'),
    ('### bank names its own bar defective', BANK, 'THE BAR THIS ACT SEALED IS DEFECTIVE'),
    ('### and says why it cannot be met', BANK, 'UNSATISFIABLE BY THE NATURE OF THE OBJECT'),
    ('bank reports the spectral separation', BANK, 'THE CUT SITS INSIDE A REAL SPECTRAL SEPARATION'),
    ('### bank says the stable cut contains the grid cut', BANK, 'STRICTLY CONTAINS'),
    ('### bank refuses to call changed values a reproduction', BANK,
     'THE STRUCTURAL FINDINGS SURVIVE AND THE'),
    ('### bank refutes the second scheme rather than deferring it', BANK,
     'IT IS REFUTED, NOT DEFERRED'),
    ('### bank reports the unit residual with no verdict', BANK, 'A MEASUREMENT AND NOT A VERDICT'),
    ('bank reports the profile prefix', BANK, 'LITERAL BYTE PREFIX'),
    ('bank reports the axiom-bearing count', BANK,
     'AXIOM-BEARING TERMINALS AMONG THE NEWLY CERTIFIED'),
    ('### bank refuses to call the repair a result', BANK, 'BOOKKEEPING THE RECORD OWED ITSELF'),
    ('### bank names the byte trap it avoided', BANK,
     "THAT IS b309's DEFECT, AND IT WAS AVOIDED"),
    ('bank files the reach-bar order', BANK, 'W-ORD-REACH-BAR'),
    ('bank discharges the rank order', BANK, 'W-ORD-RANK-STABLE-SUBSPACE'),
    ('bank carries the membership order forward', BANK, 'W-ORD-ARCH-MEMBERSHIP'),
    ('bank discharges the coverage order', BANK, 'W-ORD-KERNEL-COVERAGE'),
    ('bank declares its deviations', BANK, 'DEVIATIONS, DECLARED.'),
    ('bank lists what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK.'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank marks the archimedean leg', BANK, 'DERIVED-NOT-CONFIRMED'),
    ('bank keeps M-2 unchanged under its cap', BANK, "UNDER b310's CAP"),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('### bank declares the re-seal', BANK, 'RE-SEALED'),
    ('bank names the next act', BANK, 'THE LAWFUL FUNCTION AND THE SOURCE'),
    ('bank says which statement is finite-decidable', BANK,
     'ONE THING IS FINITE-DECIDABLE AND IT IS SAID WHICH'),
    ('registration names the act', REG, 'THE STABLE RANK'),
    ('registration seals before any spectrum', REG, 'SEALED BEFORE ANY SPECTRUM OF THIS ACT'),
    ('registration carries the threshold and the bars', REG, 'THE THRESHOLD AND THE BARS'),
    ('### registration forbids a membership verdict', REG, 'IT MAY NOT DECIDE MEMBERSHIP'),
    ('### registration declares the reading it was forced into', REG, 'A READING THE ORDER FORCES'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run counts the rank changes', RUN,
     'RANK CHANGES ALONG THE GRID AXIS -- b316 SCHEME : 1 ; THIS ACT : 0'),
    ('the run reports the square never negative', RUN,
     'CELLS AT WHICH THE SQUARE IS NEGATIVE ANYWHERE : 0'),
    ('### the run reports the reach empty', RUN, 'CELLS INSIDE THE REACH : 0 OF 6'),
    ('### the run reports the noise gate refusing', RUN, 'REFUSED -- 6 of 12'),
    ('the run marks the unit residual as no verdict', RUN, 'A MEASUREMENT, NOT A VERDICT'),
    ('the run checks the sandwich spectrum', RUN, 'inside [0,1] : True'),
    ('the repair reproduces the baseline', REP, 'BYTE FOR BYTE : True'),
    ('### the repair proves the prefix', REP, 'EVERY PRE-EXISTING PRINT BYTE-IDENTICAL : True'),
    ('### the repair reports the axiom count', REP,
     'AXIOM-BEARING TERMINALS AMONG THE NEWLY CERTIFIED : 0'),
    ('the repair shows the gate passing', REP, 'GATE PASSES'),
    ('the repair reports zero build errors', REP, 'build errors : 0'),
    ('the pin agrees on the grid axis', PIN, 'THE SAME INDEX SET AT EVERY GRID FRAME : True'),
    ('### the pin is refuted on the domain axis', PIN,
     'PINNING IS NOT A REFINEMENT SCHEME HERE, IT IS AN ERROR'),
    ('### the pin names the bar defect', PIN, 'CANNOT BE SATISFIED, AND THAT IS A DEFECT IN (B3)'),
    ('the extract reports nothing missing', EXTRACT, 'SOURCE FRAGMENTS NOT FOUND : 0'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### **`G-BARDEFECT` -- the sentences an act that wanted its reach would have written.**
    ('the reach is not called non-empty', BANK, 'THE REACH IS NON-EMPTY.'),
    ('the bar is not reinterpreted', BANK, 'THE BAR IS AMENDED.'),
    ('the number is not called converged', BANK, 'THE NUMBER HAS CONVERGED.'),
    # ### **`G-NOVERDICT`.**
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    ('the unit is not placed in the space', BANK, 'THE UNIT IS IN THE SPACE.'),
    ('the residual is not called small', BANK, 'THE RESIDUAL IS SMALL.'),
    # ### **THE REPAIR IS NOT A RESULT.**
    ('the repair is not called a proof', BANK, 'THE TERMINALS ARE PROVED.'),
    ('no axiom is hidden', BANK, 'THE PROFILE IS CLEAN.'),
    # ### **`G-NOREVERDICT`.**
    ('b316 is not re-verdicted', BANK, 'b316 IS RE-VERDICTED.'),
    ('b318 is not re-verdicted', BANK, 'b318 IS RE-VERDICTED.'),
    ('b318 numbers are not called wrong', BANK, "b318's NUMBERS ARE WRONG."),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    # ### **THE SPACE.**
    ("the source's eigenspace is not claimed", BANK, "THE SOURCE'S EIGENSPACE IS COMPUTED."),
    ('the inequality is not evaluated', BANK, 'THE INEQUALITY IS EVALUATED.'),
    # ### **THE STANDING CAPS.**
    ('no Core module is edited', BANK, 'A CORE MODULE IS EDITED.'),
    ('no instrument is edited', BANK, 'THE OWNER INSTRUMENT IS EDITED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('nothing about the identity', BANK, 'THE IDENTITY IS AFFECTED.'),
    ('no p-adic reach is claimed', BANK, 'THE p-ADIC ZERO CARRIES OVER.'),
]

TOOLNUM = [
    ("the subspace by the eigenvalue-one criterion", 'tools/b319_stable.py'),
    ("the components, the axes, the reach and the unit residual", 'tools/b319_run.py'),
    ("the kernel-coverage repair and its byte comparison", 'tools/b319_coverage_repair.py'),
    ("the second scheme, tried on both axes", 'tools/b319_pin.py'),
    ("the source fragments, located", 'tools/b319_extract.py'),
    ("### the finder those fragments were located with", 'tools/b317_extract.py'),
    ("the grid scheme, the projector and the unit", 'tools/b316_instrument.py'),
    ("the variant, the kernel and the smear", 'tools/b317_smear.py'),
    ("the square and the autocorrelation", 'tools/b318_square.py'),
    ("the coverage gate's two counts", 'tools/b315_coverage_gate.py'),
    ("the prolate eigenvalues the threshold is argued from", 'tools/e16/qeps_layer.py'),
    ("the floor/drift verdicts", 'tools/noise_floor.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b319_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b319_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b319_correspondence.py'),
    ("the index key's read-back arms", 'tools/b319_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b319' in x)

# ### **THE DECLARED LITERALS, AND WHERE EACH COMES FROM.**
# ### `0.0`, `1.0` are the points the act's own comparisons are stated against.
# ### `100.0` is a percent for display; `1e-9`, `1e-300` are tolerances and a divide guard.
# ### ### **AND `0.5, 0.7, 1.1, 1.5, 2.0, 3.0, 4.0, 1e-12` ARE b316's OWN, NOT THIS ACT'S.** ### They
# ### are the Gaussian centres and the three dilations of b316's worked-inner-product check, which
# ### (2d) reproduces VERBATIM so that the check is the same check. ### b316's own `FLOAT_OK`
# ### declared exactly these. ### **A REPRODUCED CHECK THAT CHANGED ITS CONSTANTS WOULD NOT BE A
# ### ### REPRODUCTION**, and none of them decides anything about this act's subspace.
FLOAT_OK = {'0.0', '1.0', '100.0', '1e-9', '1e-300',
            '0.5', '0.7', '1.1', '1.5', '2.0', '3.0', '4.0', '1e-12'}


def main():
    fails = []
    print('=' * 100)
    print('b319 -- GATE SUITE (AN INSTRUMENT BUILD AND A KERNEL REPAIR)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (the source ones pulled from the EXTRACT FILE, not the PDF):')
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
    rep = io.open(REP, encoding='utf-8').read()
    pin = io.open(PIN, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8').read()
    src = io.open(t('b319_run.py'), encoding='utf-8').read()
    stb = io.open(t('b319_stable.py'), encoding='utf-8').read()
    code = K7.strip_text(src) + K7.strip_text(stb)

    print('\n  G-ONELEAN (exactly one `.lean` changed, and no `Core/` module):')
    st = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    leans = [x[3:].strip() for x in st.splitlines() if x.strip().endswith('.lean')]
    cores = [x for x in leans if x.startswith('Core/')]
    print('    `.lean` paths changed in the kernel repo : %s' % leans)
    print('    ### of those under `Core/` : %d  %s' % (len(cores), cores or ''))
    l_relay = subprocess.run(['git', '-C', ROOT, 'status', '--short', '--', '*.lean'],
                             capture_output=True, text=True).stdout.strip()
    print('    `.lean` changed in relay : %r' % l_relay)
    if len(leans) > 1 or cores or l_relay:
        fails.append('G-ONELEAN')

    print('\n  G-PREFIX (the old profile is a LITERAL BYTE PREFIX of the new one):')
    pref = 'EVERY PRE-EXISTING PRINT BYTE-IDENTICAL : True' in rep
    base = 'BYTE FOR BYTE : True' in rep
    print('    baseline reproduced before the edit : %s ; prefix after it : %s' % (base, pref))
    if not (base and pref):
        fails.append('G-PREFIX')

    print('\n  G-ASPRINTED (the axiom count is read off the printed file):')
    asp = 'AXIOM-BEARING TERMINALS AMONG THE NEWLY CERTIFIED : 0' in rep
    said = 'READ OFF THE PRINTED FILE' in bank
    print('    the repair reports it : %s ; the bank says where it came from : %s' % (asp, said))
    if not (asp and said):
        fails.append('G-ASPRINTED')

    print('\n  G-GATEPASSES (the gate that filed the order now passes):')
    gp = 'GATE PASSES' in rep
    print('    the coverage gate passes : %s' % gp)
    if not gp:
        fails.append('G-GATEPASSES')

    print('\n  G-BARDEFECT (the reach is reported under the bar AS WRITTEN, and the bar is named):')
    empty = 'CELLS INSIDE THE REACH : 0 OF 6' in run
    named = ('THE BAR THIS ACT SEALED IS DEFECTIVE' in bank
             and 'UNSATISFIABLE BY THE NATURE OF THE OBJECT' in bank)
    proposal = 'PROPOSAL' in bank
    print('    the reach is empty and said so : %s ; the bar is named defective : %s' % (empty, named))
    print('    and the fix is a PROPOSAL, not a change to a sealed file : %s' % proposal)
    if not (empty and named and proposal):
        fails.append('G-BARDEFECT')

    print('\n  G-PINTRIED (the second scheme tried on both axes, and refuted on one):')
    pt = ('THE SAME INDEX SET AT EVERY GRID FRAME : True' in pin
          and 'PINNING IS NOT A REFINEMENT SCHEME HERE, IT IS AN ERROR' in pin
          and 'IT IS REFUTED, NOT DEFERRED' in bank)
    print('    tried on the grid axis, refuted on the domain axis, and said so : %s' % pt)
    if not pt:
        fails.append('G-PINTRIED')

    print('\n  G-NOVERDICT (the unit residual is a measurement):')
    nv = ('A MEASUREMENT, NOT A VERDICT' in run and 'A MEASUREMENT AND NOT A VERDICT' in bank
          and 'IT MAY NOT DECIDE MEMBERSHIP' in reg)
    print('    the run, the bank and the seal all say so : %s' % nv)
    if not nv:
        fails.append('G-NOVERDICT')

    print('\n  G-NOUNITDEF (no unit is DEFINED here -- b316\'s is imported):')
    defined = re.search(r'def\s+sonin_unit', code)
    called = 'INS.sonin_unit' in src
    print('    `def sonin_unit` in this act\'s tools : %s ; b316\'s is called : %s'
          % (bool(defined), called))
    print('    ### **b317 AND b318 CAPPED ANY CALL. ### THIS ACT\'S ORDER REQUIRES ONE**, so the cap')
    print('    ### becomes DEFINITION rather than use, and the verdict cap at G-NOVERDICT carries')
    print('    ### what the old one was really protecting.')
    if defined or not called:
        fails.append('G-NOUNITDEF')

    print('\n  G-NOWEIL (neither side of the source\'s inequality is computed):')
    nw = not re.search(r'def .*weil|W_infinity\s*=|def .*w_inf', code)
    print('    no distribution is computed in either tool : %s' % nw)
    if not nw:
        fails.append('G-NOWEIL')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the sandwich spectrum, inside [0,1]', 'inside [0,1] : True' in run),
            ('the threshold selection, able to change its mind', 'monotone : True' in run),
            ('the identity control at every frame', 'identity trace' in run),
            ('the coverage gate, still able to fail', 'fixtures' in rep),
            ('the pin, refuted on the domain axis', '1.000e+00' in pin),
            ('the noise-floor gate -- REPORTED REFUSING', 'REFUSED -- 6 of 12' in run)]
    for lbl, ok_ in arms:
        print('    %-56s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOFLOAT (no undeclared float literal in the deciding runner):')
    sq_, sl_ = K7.strip_fixture()
    print('    STRIPPER FIXTURE (imported from b317): quiet=%s loud=%s' % (sq_, sl_))
    if not (sq_ and sl_):
        fails.append('G-NOFLOAT (fixture)')
    rcode = K7.strip_text(src)
    lits = set()
    for m in re.finditer(r'(?<![\w.])(\d+\.\d*(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w.])', rcode):
        lits.add(m.group(1))
    extra = sorted(x for x in lits if x not in FLOAT_OK)
    print('    float literals in b319_run.py : %d ; UNDECLARED : %d %s'
          % (len(lits), len(extra), extra if extra else ''))
    if extra:
        fails.append('G-NOFLOAT')

    print('\n  G-NOEDIT (the owner instruments byte-identical to git HEAD, checked AFTER the run):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    if dirty:
        fails.append('G-NOEDIT')

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

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
        if ferry_scan.scan_text(text, struck, stem_list)[0]:
            fired_disc += 1
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
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
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
    print('    ### **AND THE SEAL BLOCK CARRIES A SUPERSEDED HASH**, because this registration was')
    print('    ### sealed with a banned stem in it and RE-SEALED after the repair. ### Declared.')
    if not intact:
        fails.append('G-SEAL')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN),
                      ('the repair', REP)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        for s in gh:
            print('      ### GRADED HEDGE: %s' % s[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d' % unpullable)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
