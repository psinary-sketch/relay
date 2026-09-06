# -*- coding: utf-8 -*-
"""b329_checks.py -- THE GATE SUITE FOR THE FINITE-SIDE SEAL.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-PROFILE`** ### -- every terminal zero-axiom; the banked profile a TRUE BYTE PREFIX of the
###     new one; the module's prints in the profile in the module's own order; the count in the profile
###     equal to the count the kernel tool printed.
###   ### ### **`G-GENERAL` / `G-CELLS`** ### -- the theorems whose docstrings say GENERAL bind `p` and name
###     no cell; the ones that say PER CELL name the list.
###   ### ### **`G-HEADER`** ### -- the module header carries GENERAL and PER CELL as separate scope
###     statements, the UNAVAILABLE arm, and what it does not certify; the gate fires on an averaging
###     header and stays quiet on this one.
###   ### ### **`G-DEVIATIONS`** ### -- the three registered bars not met in their registered form are
###     declared in the bank, in the header, and in the index.
###   ### **`G-NUMBERS`** ### -- every number the bank quotes is read back from the file that produced it.
###   ### **`G-ORDER`** ### -- the registration sealed before the module existed and before any build.
###   ### **`G-VANILLA`, `G-COVERAGE`, `G-ROWS`, `G-LEDGER`, `G-INDEX`, `G-LORE`, `G-APPENDONLY`, the stem
###     sweep, the hedge audit, `G-TOOLNUM`** -- standing.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import b329_kernel as KT  # noqa: E402
import b329_correspondence as R  # noqa: E402
import b329_header_gate as HG  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
LORE = os.path.join(ROOT, 'tools', 'lore_rules.py')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MODULE = os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean')
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
ALLP = os.path.join(SIDE, 'AllPrints.lean')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b329_the_finite_side_seal.txt')
REG = d('b329_registration_2026-09-05.txt')
EXTRACT = d('b329_extract_notes.txt')
KBASE = d('b329_kernel_baseline.txt')
KRUN = d('b329_kernel_run.txt')
KRUN2 = d('b329_kernel_run2.txt')
PROBE = d('b329_axiom_probe.txt')
COV = d('b329_coverage_gate.txt')
CORR1 = d('b329_corr_run.txt')
CORR2 = d('b329_corr_run2.txt')
CORRR = d('b329_corr_rerun.txt')
FIL = d('b329_filings_run.txt')
FILR = d('b329_filings_rerun.txt')
IDX = d('b329_index_run.txt')
IDXR = d('b329_index_rerun.txt')
LRUN = d('b329_lore_run.txt')
LRER = d('b329_lore_rerun.txt')
SCAN = d('b329_ferry_scan.txt')
CENSUS = d('b329_census.txt')
FCEN = d('b329_faces_census.txt')
REGSPEC = d('b329_regspec_run.txt')
SATIS = d('audit_b329_reg_satisfiable.txt')
TERMSCAN = d('b329_reg_termscan.txt')
GATE = d('b329_reg_gate.txt')
PINS = d('b329_pins_stepzero.txt')
INDEXQ = d('audit_b329_index_query.txt')
SEAL = '380f2a84e9db57bc922437dff575f3cc9cfb01435e8539360365cb64d6a1cbe7'

OWNED = [BANK, REG, KBASE, KRUN, KRUN2, PROBE, COV, CORR1, CORR2, CORRR, FIL, FILR, IDX, IDXR, LRUN, LRER, CENSUS, FCEN,
         REGSPEC, SATIS, PINS, INDEXQ, GATE, d('b329_satisfiable.json'), d('b329_axiom_probe.lean'), MODULE,
         t('b329_extract.py'), t('b329_kernel.py'), t('b329_regspec.py'), t('b329_axiom_probe.py'), t('b329_header_gate.py'),
         t('b329_lore_append.py'), t('b329_correspondence.py'), t('b329_filings.py'), t('b329_index_append.py')]

CARRIERS = [
    (t('b329_checks.py'), 'its own fixtures'),
    (d('b329_ferry_2026-09-05.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("b309 -- the mechanism in one sentence", d('b309_the_scaling_trace.txt'), 'THE SCALING MAP HAS NO FIXED POINT OFF THE BALL,'),
    ("### because p^j - 1 is invertible", d('b309_the_scaling_trace.txt'), 'BECAUSE `p^j - 1` IS INVERTIBLE'),
    ("b310 -- the fixed-point sentence, first line", d('b310_the_smear_collapses.txt'), 'IS A SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN THE TWO'),
    ("### its second line", d('b310_the_smear_collapses.txt'), "CONGRUENCES THE OBJECT'S TWO CONDITIONS IMPOSE, WEIGHTED BY THE EMBEDDING'S HAAR FACTOR."),
    ("### the identity value", d('b310_the_smear_collapses.txt'), 'at `t = 1` every off-ball point is fixed and the count is `(p^n - 1)^2`;'),
    ("b304 -- the zero at all six", d('b304_the_demands_shape.txt'), 'THE SMEARED VALUE EXACTLY 0 AT ALL SIX'),
    ("### the traces are not all zero", d('b304_the_demands_shape.txt'), 'AND THOSE TRACES ARE NOT ALL ZERO'),
    ("### the valuation shells", d('b304_the_demands_shape.txt'), 'VALUATION SHELLS'),
    ("B309 module -- the general law uncompiled", os.path.join(SIDE, 'Core', 'ScalingTraceShadow.lean'), "general law is the bank's derivation and is uncompiled"),
    ("B310 module -- offBallFixed", os.path.join(SIDE, 'Core', 'SmearCollapseShadow.lean'), 'def offBallFixed (p n t m : Nat) : Nat :='),
    ("B270 module -- the polarity idiom", os.path.join(SIDE, 'Core', 'BallAbsorptionShadow.lean'), 'def hasLiveStep (p n k : Nat) : Bool :='),
    ("CORRESPONDENCE row 133", TABLE, '| 133 | THE FIXED-POINT SENTENCE, AND ITS BEARING (b310)'),
    ("the faces ledger's F5 row", LEDGER, '| F5 | F5 -- the fixed-point silence'),
    ("b310 registration -- certifies arithmetic and not", d('b310_registration_2026-09-03.txt'), 'IT CERTIFIES ARITHMETIC AND NOT'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### never averaged', BANK, 'FOR THE COMPACT PART, NEVER AVERAGED.**'),
    ('### the axiom finding', BANK, 'THE AXIOM FINDING, WHICH THIS SEAT DID NOT EXPECT'),
    ('### equations with witnesses', BANK, 'STATED AS EQUATIONS WITH THEIR WITNESSES AND PROVED FROM THE AXIOM-FREE PART OF CORE PLUS SIX'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('### sealed before any build', BANK, 'THE REGISTRATION WAS SEALED BEFORE ANY BUILD OF THIS ACT RAN.'),
    ('bank gives component 1', BANK, 'COMPONENT 1 -- THE DECOMPOSITION, GENERAL.'),
    ('### D1', BANK, '(D1) THE REGISTERED (T1.4) IS NOT MET IN ITS REGISTERED FORM:'),
    ('### primality nowhere', BANK, 'CONSEQUENTLY PRIMALITY IS USED NOWHERE IN THE MODULE'),
    ('bank gives component 2', BANK, "COMPONENT 2 -- THE SCALING PART'S SILENCE, GENERAL, WITH ITS POLARITY CONTROLS."),
    ("### b309's law compiled", BANK, "THIS IS THE LAW B309's OWN HEADER CALLED UNCOMPILED"),
    ('### the ball-forcing is the scaling map\'s', BANK, "SO THE BALL-FORCING IS THE SCALING MAP'S PROPERTY AND NOT EVERY MAP'S."),
    ('### D2', BANK, '(D2) THE REGISTERED (T2.1) IS NOT MET IN ITS `Nat.Coprime` FORM'),
    ('### D3', BANK, '(D3) THE REGISTERED (T1.6) IS THE FACTORIZATION BEFORE'),
    ('bank gives component 3', BANK, "COMPONENT 3 -- THE COMPACT PART'S SILENCE, PER CELL."),
    ('### the unavailable arm', BANK, 'THE UNAVAILABLE ARM, STATED IN THE HEADER AND NOT MANUFACTURED:'),
    ('### a check added', BANK, 'NOT A CLAIM ADDED'),
    ('### the seam', BANK, 'THE SEAM, NAMED:'),
    ('bank gives component 4', BANK, 'COMPONENT 4 -- EXHAUSTIVENESS, ONE THEOREM, HYPOTHESES NAMING THE GENERALITY.'),
    ('bank gives component 5', BANK, 'COMPONENT 5 -- THE PROFILE AND THE ROWS.'),
    ('### the prefix', BANK, 'BANKED PROFILE A TRUE BYTE PREFIX OF THE NEW ONE : True**'),
    ('### the first draft', BANK, 'THE FIRST DRAFT OF THE MODULE COMPILED, AND ITS GENERAL THEOREMS PRINTED `[propext,'),
    ('### no profile from it', BANK, 'NO PROFILE WAS WRITTEN FROM'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### not general for the compact part', BANK, "IT DOES NOT SAY THE COMPACT PART'S SILENCE IS PROVED IN GENERAL."),
    ("### not the source's trace", BANK, "IT DOES NOT SAY THE SOURCE'S TRACE IS COMPILED."),
    ('### nothing archimedean', BANK, 'IT DOES NOT SAY ANYTHING ABOUT THE ARCHIMEDEAN PLACE.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### nothing deposits', BANK, 'NOTHING DEPOSITS.'),
    ('### this act is the shadow', BANK, 'THE SHADOW: THIS ACT IS THE SHADOW.'),
    ('### next', BANK, 'NEXT, BY THE ORDER: THE TECHNE EXTRACTION, THEN THE FOLD FROM b323 ONWARD.'),
    ('module header -- general', MODULE, 'GENERAL (over every base `p`, level, power and index; by induction, from the'),
    ('module header -- per cell', MODULE, 'PER CELL (decided by finite evaluation over the explicit list `cells`, and'),
    ('module header -- unavailable', MODULE, 'THE UNAVAILABLE ARM, STATED AND NOT MANUFACTURED.'),
    ('module header -- what it does not certify', MODULE, 'WHAT IT DOES NOT CERTIFY.'),
    ('module header -- the axiom finding', MODULE, 'THE AXIOM FINDING, AND WHAT IT CHANGED.'),
    ('module header -- three bars not met', MODULE, 'THREE REGISTERED BARS ARE NOT MET IN'),
    ('registration -- the risk clause', REG, 'A GENERAL BAR THAT RESISTS IS DECLARED NOT MET, THE PER-CELL ARM IS NOT'),
    ('registration -- this act is the shadow', REG, 'THIS ACT IS THE SHADOW.'),
]

MUST_FAIL = [
    ('the bank never claims the compact part general', BANK, "### ### **THE COMPACT PART'S SILENCE IS PROVED IN GENERAL.**"),
    ('the bank never claims the trace compiled', BANK, "### ### **THE SOURCE'S TRACE IS COMPILED.**"),
    ('the module never sorries', MODULE, 'sorry'),
    ('the profile carries no axiom line', PROFILE, "'B329.finite_side_silence' depends on axioms: [propext, Quot.sound]"),
]

TOOLNUM = [
    ('566 -> 590 prints, 24 terminals, the prefix', 'tools/b329_kernel.py'),
    ('85 / 49 / 36 probed prints, 5 tactics, 31 lemmas', 'tools/b329_axiom_probe.py'),
    ('rows 170-174', 'tools/b329_correspondence.py'),
    ('the coverage zeros', 'tools/b315_coverage_gate.py'),
    ('24 clauses', 'tools/b329_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('26542 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b329_extract.py'),
    ('the ledger block', 'tools/b329_filings.py'),
    ('the index rows', 'tools/b329_index_append.py'),
    ('the lore entry', 'tools/b329_lore_append.py'),
    ('the header gate', 'tools/b329_header_gate.py'),
]
NEW_THIS_ACT = {'tools/b329_kernel.py', 'tools/b329_axiom_probe.py', 'tools/b329_correspondence.py', 'tools/b329_regspec.py',
                'tools/b329_extract.py', 'tools/b329_filings.py', 'tools/b329_index_append.py', 'tools/b329_lore_append.py',
                'tools/b329_header_gate.py'}


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace('\r\n', '\n')


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def docstrings(src):
    out = {}
    for m in re.finditer(r'/--((?:(?!-/).)*?)-/\s*(?:set_option[^\n]*\n\s*)?theorem\s+([A-Za-z_][A-Za-z0-9_\']*)', src, re.S):
        out[m.group(2)] = m.group(1)
    return out


def statements(src):
    out = {}
    for m in re.finditer(r'^theorem\s+([A-Za-z_][A-Za-z0-9_\']*)(.*?):=', src, re.S | re.M):
        out[m.group(1)] = m.group(2)
    return out


def main():
    fails = []
    print('=' * 100)
    print('b329 -- GATE SUITE (THE FINITE-SIDE SEAL: GENERAL WHERE IT SAYS GENERAL, PER CELL WHERE IT SAYS PER CELL)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print('\n  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
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
    src = io.open(MODULE, encoding='utf-8').read()
    prof = io.open(PROFILE, 'rb').read()
    prof_n = norm(prof.decode('utf-8', 'replace'))
    krun = io.open(KRUN, encoding='utf-8').read()
    krun2 = io.open(KRUN2, encoding='utf-8').read()
    kbase = io.open(KBASE, encoding='utf-8').read()
    probe = io.open(PROBE, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    lore = io.open(LORE, encoding='utf-8').read()
    thms = R.read_module()
    scope = dict(thms)
    names = KT.theorems_in(src)
    prints_in_module = [ln.split()[-1] for ln in src.splitlines() if ln.startswith('#print axioms ')]
    b329_lines = [ln for ln in prof_n.splitlines() if ln.startswith("'B329.")]

    print('\n  G-PROFILE (every terminal zero-axiom; the prefix; the module\'s prints in the profile in its own order):')
    m = re.search(r'prints before -> after\s*:\s*(\d+) -> (\d+)\s+zero-axiom: (\d+) -> (\d+)\s+other: (\d+) -> (\d+)', krun)
    before, after, o1 = int(m.group(1)), int(m.group(2)), int(m.group(6))
    nlines = len([ln for ln in prof_n.splitlines() if ln.strip()])
    # ### the names carry apostrophes (`mul_assoc'`), so the profile line is parsed by its verb, not split on quotes
    order_ok = [re.match(r"^'(.*)' (?:does not depend|depends)", ln).group(1) for ln in b329_lines] == prints_in_module == ['B329.' + n for n in names]
    allzero = all(ln.rstrip().endswith('does not depend on any axioms') for ln in prof_n.splitlines() if ln.strip())
    prefix = 'TRUE BYTE PREFIX OF THE NEW ONE : True' in krun
    base_ok = 'BYTE-IDENTICAL to banked : True' in kbase and 'BYTE-IDENTICAL to banked : True' in krun
    bom = prof.startswith(b'\xef\xbb\xbf')
    gp = (nlines == after and after - before == len(names) and o1 == 0 and order_ok and allzero and prefix and base_ok and not bom)
    print('    profile lines %d == kernel-tool after %d ; added %d == theorems %d ; other 0 %s ; order %s ; all zero-axiom %s ; prefix %s ; baseline %s ; BOM %s : %s'
          % (nlines, after, after - before, len(names), o1 == 0, order_ok, allzero, prefix, base_ok, bom, gp))
    if not gp:
        fails.append('G-PROFILE')

    print('\n  G-KERNEL-IDEM (the kernel tool re-run on the already-imported path added nothing and rewrote nothing):')
    # ### the tool's precondition is disk == HEAD, so before the commit the re-run REFUSES (b329_kernel_run2.txt keeps that
    # ### refusal); the idempotent re-run is the post-commit one, the latest numbered run file.
    runs = sorted([p for p in os.listdir(D) if re.match(r'b329_kernel_run\d*\.txt$', p)], key=lambda s: int(re.search(r'(\d*)\.txt$', s).group(1) or 1))
    latest = io.open(d(runs[-1]), encoding='utf-8').read()
    head_prof = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'], capture_output=True).stdout
    committed = norm(head_prof.decode('utf-8', 'replace')) == prof_n
    if committed:
        gi = ('prints added             : 0' in latest and 'READ BACK BYTE-WISE : True' in latest and 'SKIPPED, AND SAID' in latest)
        print('    HEAD carries the profile ; latest run %s is the idempotent one : %s' % (runs[-1], gi))
    else:
        gi = 'HARD FAILURE -- the working tree profile already differs from HEAD' in krun2
        print('    HEAD does not yet carry the profile ; the pre-commit re-run REFUSED on its precondition, as recorded : %s  (the idempotent re-run is owed after the commit)' % gi)
    if not gi:
        fails.append('G-KERNEL-IDEM')

    print('\n  G-VANILLA (refused forms in the module code with comments stripped; theorem never lemma; no imports):')
    ref = KT.refused_in_source(src)
    gv = all(v == 0 for v in ref.values()) and len(names) == len(prints_in_module)
    print('    %s ; theorems %d == prints %d : %s' % (ref, len(names), len(prints_in_module), gv))
    if not gv:
        fails.append('G-VANILLA')

    print('\n  G-GENERAL / G-CELLS (statements read from the source against their docstrings\' scope words):')
    st = statements(src)
    bad_g, bad_c = [], []
    for n, s in thms:
        body = st.get(n, '')
        if s == 'GENERAL':
            # ### general: no cell literal, no `cells`, and at least one universally bound Nat variable
            if re.search(r'\(\s*\d+\s*,\s*\d+\s*\)|\bcells\b', body) or not re.search(r"[{(]\s*[A-Za-z' ]+:\s*Nat", body):
                bad_g.append(n)
        elif s == 'PER CELL':
            if not (re.search(r'\bcells\b', body) or re.search(r'\[\(\s*\d+\s*,', body) or re.search(r'unitFixesOffBall\s+\d', body)):
                bad_c.append(n)
        elif s == 'EXHAUSTIVENESS':
            if not (re.search(r'\bcells\b', body) and re.search(r'\{\s*p\b', body)):
                bad_g.append(n)
    ng = sum(1 for _n, s in thms if s == 'GENERAL')
    nc = sum(1 for _n, s in thms if s == 'PER CELL')
    print('    GENERAL %d (no cell literal, p bound) violations %s ; PER CELL %d (list named) violations %s ; exhaustiveness names cells and binds p'
          % (ng, bad_g, nc, bad_c))
    if bad_g or bad_c or ng == 0 or nc == 0:
        fails.append('G-GENERAL/G-CELLS')

    print('\n  G-HEADER (both scope words as separate statements, the UNAVAILABLE arm, what it does not certify; the gate in both polarities):')
    hok, hreasons = HG.check(src)
    hf, hq = HG.fixtures()
    print('    header %s %s ; fires on the averaging fixture %s ; quiet here %s' % (hok, hreasons, hf, hq))
    if not (hok and hf and hq):
        fails.append('G-HEADER')

    print('\n  G-POLARITY (both arms present and printed zero-axiom):')
    pol = ['identity_fixes_every_index', 'unit_fixes_offball_at_cells', 'some_unit_fixes_offball_above_level_one',
           'no_unit_fixes_offball_at_level_one', 'identity_trace_is_the_dimension', 'traces_not_all_zero_off_identity']
    gpol = all(("'B329.%s' does not depend on any axioms" % n) in prof_n for n in pol)
    print('    %s' % gpol)
    if not gpol:
        fails.append('G-POLARITY')

    print('\n  G-DOCSTRING (every non-helper theorem cites b304, b309 or b310; the exhaustiveness docstring carries b310\'s sentence verbatim):')
    docs = docstrings(src)
    nocite = [n for n, s in thms if s != 'helper' and not re.search(r'\bb3(04|09|10)\b', docs.get(n, ''))]
    fs = re.sub(r'\s+', ' ', docs.get('finite_side_silence', ''))
    frag1 = 'IS A SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN THE TWO'
    frag2 = "CONGRUENCES THE OBJECT'S TWO CONDITIONS IMPOSE, WEIGHTED BY THE EMBEDDING'S HAAR FACTOR."
    verb = (frag1 + ' ' + frag2) in fs and frag1 in extract and frag2 in extract
    print('    theorems without a citing act : %s ; the sentence verbatim (both extract fragments, joined) : %s' % (nocite, verb))
    if nocite or not verb:
        fails.append('G-DOCSTRING')

    print('\n  G-COVERAGE (b315\'s gate, run now):')
    cv = subprocess.run([sys.executable, t('b315_coverage_gate.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    gc = cv.returncode == 0 and 'MODULES WITH A PRINT TARGET AND NOT IMPORTED : 0' in (cv.stdout or '') and 'PRINT TARGETS NOT IN THE PROFILE            : 0' in (cv.stdout or '')
    print('    exit %d ; both zeros : %s' % (cv.returncode, gc))
    if not gc:
        fails.append('G-COVERAGE')

    print('\n  G-ALLPRINTS-APPEND (the certification file: one import after the last import, the prints at the END, nothing else moved):')
    ab = blob_of(SIDE, 'AllPrints.lean')
    aw = io.open(ALLP, encoding='utf-8').read()
    wl = norm(aw).rstrip('\n').split('\n')
    bl = norm(ab).rstrip('\n').split('\n') if ab is not None else []
    if ab is not None and 'import FiniteSideSeal' in ab:
        ga = wl == bl
        how = 'blob already carries the module: equal'
    else:
        tail = wl[-len(prints_in_module):]
        stripped = [ln for ln in wl[:-len(prints_in_module)] if ln != 'import FiniteSideSeal']
        ga = stripped == bl and tail == ['#print axioms ' + n for n in prints_in_module] and wl.count('import FiniteSideSeal') == 1
        how = 'blob plus one import plus the prints at the end'
    print('    %s : %s' % (how, ga))
    if not ga:
        fails.append('G-ALLPRINTS-APPEND')

    print('\n  G-ROWS (rows 170-174: one per component, each with its scope word, its scope refusal and M-2; every theorem named):')
    rows = [ln for ln in tbl.split('\n') if re.match(r'^\| 17[0-4] \|', ln)]
    rowtxt = '\n'.join(rows)
    named = [n for n, s in thms if s != 'helper' and ('`B329.%s`' % n) not in rowtxt]
    gr = (len(rows) == 5 and all(('GENERAL' in r or 'PER CELL' in r) and 'SCOPE' in r and 'M-2' in r for r in rows) and not named
          and all(('(%s)' % w) in rowtxt for w in ('GENERAL', 'PER CELL')) and 'NOT COMPILED AND SAID' in rowtxt)
    print('    rows %d ; theorems not named in a row %s ; scope words and refusals : %s' % (len(rows), named, gr))
    if not gr:
        fails.append('G-ROWS')

    print('\n  G-ANCESTOR (the correspondence table is a true prefix of its blob; rows 130-133, 168, 169 byte-equal):')
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    pfx2 = norm(tbl).startswith(norm(head).rstrip('\n'))
    anc = [ln for ln in norm(head).split('\n') if re.match(r'^\| (13[0-3]|16[89]) \|', ln)]
    anc_ok = all(ln in norm(tbl).split('\n') for ln in anc) and len(anc) == 6
    print('    table is a TRUE PREFIX : %s ; ancestor rows unchanged : %s' % (pfx2, anc_ok))
    if not (pfx2 and anc_ok):
        fails.append('G-ANCESTOR')

    print('\n  G-LEDGER (the b329 block once, through the writer, with both statuses and the UNAVAILABLE arm; F5 row untouched; blob a true prefix; deposit unchanged):')
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    blk = led[led.index('<!-- b329 update -->'):] if '<!-- b329 update -->' in led else ''
    f5w = [ln for ln in norm(led).split('\n') if ln.startswith('| F5 | F5 -- the fixed-point silence')]
    f5b = [ln for ln in norm(lb).split('\n') if ln.startswith('| F5 | F5 -- the fixed-point silence')]
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gl = (led.count('<!-- b329 update -->') == 1 and 'PROVED-GENERAL' in blk and 'PROVED-AT-CELLS' in blk and 'UNAVAILABLE' in blk
          and f5w == f5b and len(f5w) == 1 and norm(led).startswith(norm(lb).rstrip('\n')) and not dep and 'WRITTEN' in io.open(FIL, encoding='utf-8').read())
    print('    %s (deposit status %r)' % (gl, dep))
    if not gl:
        fails.append('G-LEDGER')

    print('\n  G-PAPERS / G-SIDE (only the files this act names changed):')
    pp = git(PP, 'status', '--porcelain')
    changed_pp = sorted(x[3:].strip() for x in pp.splitlines() if x.strip() and not x.startswith('??'))
    sd = git(SIDE, 'status', '--porcelain')
    changed_sd = sorted(x[3:].strip() for x in sd.splitlines() if x.strip() and not x.startswith('??'))
    untracked_sd = sorted(x[3:].strip() for x in sd.splitlines() if x.startswith('??'))
    gs = set(changed_pp) <= {'FACES_LEDGER.md'} and set(changed_sd) <= {'AXIOM_PRINTS.txt', 'AllPrints.lean', 'CORRESPONDENCE.md'} and set(untracked_sd) <= {'Core/FiniteSideSeal.lean'}
    print('    PLACE-papers %s ; SIDE %s (untracked %s) : %s' % (changed_pp, changed_sd, untracked_sd, gs))
    if not gs:
        fails.append('G-PAPERS/G-SIDE')

    print('\n  G-NOEDIT (owner files, sealed files, the deposit, HANDOFF, the mirror roster: no tracked change):')
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py',
              'tools/b315_coverage_gate.py', 'tools/ferry_scan.py', 'tools/reg_seal.py', 'tools/b300_regspec.py', 'tools/mirror_roster.json',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b304_the_demands_shape.txt', 'data/b309_the_scaling_trace.txt',
              'data/b310_the_smear_collapses.txt', 'data/b310_registration_2026-09-03.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = git(SIDE, 'status', '--porcelain', '--', 'Core/ScalingTraceShadow.lean', 'Core/SmearCollapseShadow.lean', 'Core/BallAbsorptionShadow.lean').strip()
    gn = not st_r and not st_s
    print('    relay %r ; SIDE %r : %s' % (st_r, st_s, gn))
    if not gn:
        fails.append('G-NOEDIT')

    print('\n  G-APPENDONLY (banked_index.py and lore_rules.py: every line of the blob still present, in order):')
    ok_ap = True
    # ### the lore's fixture list closes with `)]:`; appending a fixture turns the previous last line's `)]:` into `),`
    # ### -- the same one-line change b328 made to b326's line. That single transformation is the only edit allowed.
    LIST_OLD = "                     ('phase condition (b326/b328)', _fixture_phase_condition)]:"
    LIST_NEWL = "                     ('phase condition (b326/b328)', _fixture_phase_condition),"
    for rel, path in (('tools/banked_index.py', INDEX), ('tools/lore_rules.py', LORE)):
        b = blob_of(ROOT, rel)
        w = io.open(path, encoding='utf-8').read()
        bl2 = norm(b).split('\n') if b is not None else []
        wl2 = norm(w).split('\n')
        if rel.endswith('lore_rules.py') and LIST_OLD in bl2 and LIST_NEWL in wl2:
            bl2 = [LIST_NEWL if ln == LIST_OLD else ln for ln in bl2]
            note = ' (the list-closing line allowed to change `)]:` -> `),`)'
        else:
            note = ''
        s = subsequence(bl2, wl2) if b is not None else False
        print('    %-22s blob is an in-order subsequence of the working file : %s%s' % (rel, s, note))
        ok_ap = ok_ap and s
    if not ok_ap:
        fails.append('G-APPENDONLY')

    print('\n  G-ORDER (the registration sealed before the module existed and before any build; the baseline before the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    i = raw.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(raw[:i]).hexdigest() if i > 0 else ''
    seal_m = os.path.getmtime(REG)
    after_seal = all(seal_m < os.path.getmtime(p) for p in [MODULE, KRUN, KRUN2, PROBE, CORR2, FIL, IDX, LRUN, BANK])
    before_seal = os.path.getmtime(KBASE) < seal_m
    go = intact and rawhash == SEAL and after_seal and before_seal
    print('    seal verifies %s ; raw hash equals the literal %s ; the module and every build/record after the seal %s ; the baseline before it %s : %s'
          % (intact, rawhash == SEAL, after_seal, before_seal, go))
    if not go:
        fails.append('G-ORDER')

    print('\n  G-DEVIATIONS (the three bars not met in their registered form: in the bank, in the header, in the index):')
    gd = (all(('(D%d)' % k) in bank for k in (1, 2, 3)) and all(x in src for x in ('(T1.4)', '(T1.6)', '(T2.1)', 'NOT MET'))
          and 'THREE REGISTERED BARS NOT MET IN THEIR REGISTERED FORM' in idx and 'NOT MET' in io.open(REG, encoding='utf-8').read())
    print('    %s' % gd)
    if not gd:
        fails.append('G-DEVIATIONS')

    print('\n  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    checks.append(('profile %d -> %d' % (before, after), ('%d -> %d' % (before, after)) in bank))
    pm = re.search(r'prints\s*:\s*(\d+)\s*\(axiom-free (\d+) ; carrying axioms (\d+)\)', probe)
    tm = re.search(r'TACTICS CARRYING AXIOMS : (\d+)', probe)
    cm = re.search(r'CORE LEMMAS CARRYING AXIOMS : (\d+)', probe)
    checks.append(('probe %s/%s/%s, tactics %s, lemmas %s' % (pm.group(1), pm.group(2), pm.group(3), tm.group(1), cm.group(1)),
                   ('%s of %s probed prints carry axioms, %s tactics and %s core lemmas' % (pm.group(3), pm.group(1), tm.group(1), cm.group(1))) in bank
                   and ('%s prints, %s axiom-free, %s carrying' % (pm.group(1), pm.group(2), pm.group(3))) in bank))
    rm = re.search(r'last 5 row number\(s\) are \[(\d+), \d+, \d+, \d+, (\d+)\]', io.open(CORR2, encoding='utf-8').read())
    checks.append(('rows %s-%s' % (rm.group(1), rm.group(2)), ('rows %s-%s' % (rm.group(1), rm.group(2))) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace'))
    checks.append(('%s bytes sealed' % sm.group(1), ('%s bytes' % sm.group(1)) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read())
    checks.append(('%s clauses' % cl.group(1), ('%s CLAUSES' % cl.group(1)) in bank))
    checks.append(('%d terminals' % len(names), ('%d terminals' % len(names)) in bank or ('%d zero-axiom' % len(names)) in bank))
    bm = re.search(r'banked profile on disk\s*:\s*(\d+) prints, (\d+) zero-axiom, (\d+) otherwise, (\d+) bytes', kbase)
    checks.append(('baseline %s prints, %s bytes' % (bm.group(1), bm.group(4)), ('%s prints' % bm.group(1)) in bank and ('%s bytes' % bm.group(4)) in bank))
    km = re.search(r'bytes  before -> after\s*:\s*(\d+) -> (\d+)', krun)
    checks.append(('bytes %s -> %s' % (km.group(1), km.group(2)), ('%s -> %s BYTES' % (km.group(1), km.group(2))) in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print('\n  G-LORE (the header-scope rule in the lore once, both polarities, the lore self-test exit 0):')
    lr = subprocess.run([sys.executable, LORE], capture_output=True, text=True, encoding='utf-8', errors='replace')
    fired = any('header scope' in ln and 'fires: True' in ln and 'stays quiet: True' in ln for ln in (lr.stdout or '').splitlines())
    glo = fired and lr.returncode == 0 and lore.count("rule='General and per-cell are stated in the module header, never averaged") == 1
    print('    fires/quiet %s ; exit %d ; entry once : %s' % (fired, lr.returncode, glo))
    if not glo:
        fails.append('G-LORE')

    print('\n  G-INDEX (the key returns two rows; the two must-not-hit queries stay NO KEY):')
    def q(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = q('finite-side-seal')
    gi2 = o.count('act      :') == 2 and 'GENERAL FOR THE SCALING PART, PER CELL FOR THE COMPACT PART' in o
    for s in ('a general compact-part silence', 'the archimedean silence'):
        gi2 = gi2 and any(ln.strip().startswith('### NO KEY') for ln in q(s).splitlines())
    print('    %s' % gi2)
    if not gi2:
        fails.append('G-INDEX')

    print('\n  G-ONCE (run files written once per path; the refused first row run kept; the re-runs recorded):')
    once_ok = all(os.path.exists(p) for p in [CORR1, CORR2, CORRR, FIL, FILR, IDX, IDXR, LRUN, LRER, KBASE, KRUN, KRUN2])
    print('    %s' % once_ok)
    if not once_ok:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
            for h in (ch + sh)[:6]:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-36s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                        ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                     if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-STEM-APPENDED (the ledger block, the rows, the index rows, the lore entry, swept):')
    ib = idx[idx.index('# ### THE FINITE-SIDE SEAL -- THE MODULE AND ITS TWO SCOPES (b329).'):idx.index('# ### THE DISCRIMINATING FAMILY -- THE CONDITION AND THE SEEDS (b328).')] if '# ### THE FINITE-SIDE SEAL -- THE MODULE AND ITS TWO SCOPES (b329).' in idx else ''
    lb2 = lore[lore.index("rule='General and per-cell"):lore.index("discharged='b329')")] if "rule='General and per-cell" in lore else ''
    for lbl, blk2 in (('FACES block', blk), ('rows 170-174', rowtxt), ('index rows', ib), ('lore entry', lb2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-16s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
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
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote, the appended blocks, rows and entries included):')
    tmpdir = tempfile.mkdtemp(prefix='b329_hedge_')
    targets = [('the bank', BANK), ('the registration', REG), ('the kernel run', KRUN), ('the probe', PROBE), ('the module', MODULE),
               ('the filing', FIL), ('the extract tool', t('b329_extract.py')), ('the kernel tool', t('b329_kernel.py')),
               ('the row tool', t('b329_correspondence.py')), ('the header gate', t('b329_header_gate.py'))]
    for lbl, text in (('the FACES block', blk), ('rows 170-174', rowtxt), ('the index rows', ib), ('the lore entry', lb2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline='\n').write(text + '\n')
        targets.append((lbl, p))
    for lbl, path in targets:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-22s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n, len(gh), len(ua)))
        for s in gh:
            print('      ### GRADED HEDGE: %s' % s[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
