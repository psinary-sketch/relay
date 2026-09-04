# -*- coding: utf-8 -*-
"""b325_checks.py -- THE GATE SUITE FOR A NEGATIVE CONTROL THAT CAME BACK SILENT.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-NOTSEES`** ### -- ### **THE ONE THIS ACT WOULD MOST EASILY HAVE BREACHED.**
###     The sign crosses at `a = 22` and a seat that wanted a result would call that `SEES IT`.
###     ### The order's verdict needs the zero side as corroboration; the on-line library is not
###     owned; so the bank, the run, the table and the index must ALL refuse the word.
###   ### ### **`G-NOTCANNOT`** ### -- the opposite breach. ### `DOES NOT SEE IT` at thirteen cells
###     is a scope statement, and the bank must refuse the capability reading BY NAME and carry the
###     structural reason and the priced reach beside the verdict.
###   ### ### **`G-CONTROL`** ### -- the positive control FIRED, the cause is measured, the repaired
###     control PASSES at every width, and ### **b321 IS NOT RE-VERDICTED** ### in the same breath.
###   ### ### **`G-DEVIATION`** ### -- the seat ran ahead of its own EXECUTION block; the sealed
###     registration carries that on its FACE as section (0); the regspec prints the checker's
###     refusal; the bank carries all three of the act's own failings at full prominence.
###   ### **`G-DEPOSIT`** ### -- no file under `outputs/DEPOSITED-v1.1.2/` is written, measured by
###     `git status` AND by the deposited twin's md5.
###   ### **`G-APPEND`** ### -- the internal keystone append-only, against the file AND the blob.
###   ### **`G-NOEDIT`** ### -- no owner instrument edited, INCLUDING the atlas whose cache defect
###     was found: guarded in the caller, reported, left alone.
###   ### **`G-ONCE`** ### -- tools that write run files write once per path.
"""
import hashlib
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
import b317_checks as K7  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
CONFINE_DEP = os.path.join(DEPOSIT, 'Which_Structure_Confines.md')
CONFINE_INT = os.path.join(PP, 'day1', 'Which_Structure_Confines.md')
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
CENSUS_TOOL = os.path.join(ROOT, 'tools', 'e16', 'epstein_census.py')
ATLAS = os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py')
WINDOW = os.path.join(ROOT, 'tools', 'b321_window.py')

OWNERS = ['tools/e16/epstein_census.py', 'tools/e16/epstein_li_v3.py', 'tools/e16/carto_atlas.py',
          'tools/e16/epstein_census_bank.jsonl', 'tools/b316_instrument.py', 'tools/b317_smear.py',
          'tools/b318_square.py', 'tools/b319_stable.py', 'tools/b320_weil.py',
          'tools/b321_window.py', 'tools/b322_ladder.py', 'tools/b323_fold.py',
          'tools/b324_reread.py', 'tools/noise_floor.py']

TWIN_MD5 = '6b18d69bcf9e619d3b2fb22376ccc432'


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b325_the_negative_control.txt')
REG = d('b325_registration_2026-09-04.txt')
RUN = d('b325_run.txt')
FIL = d('b325_filings_run.txt')
EXTRACT = d('b325_extract_notes.txt')
SCAN = d('b325_ferry_scan.txt')
FERRY = d('b325_ferry_2026-09-04.txt')
CENSUS = d('b325_census.txt')
REGSPEC = d('b325_regspec_run.txt')
SATIS = d('b325_satisfiable_run.txt')

OWNED = [RUN, FIL, CENSUS, EXTRACT, REGSPEC, SATIS, d('b325_filings_rerun.txt'),
         d('b325_index_run.txt'), d('b325_pins_stepzero.txt'), d('b325_reg_termscan.txt'),
         d('b325_satisfiable.json'), d('b325_rows.json'), d('b325_stdout.txt'),
         t('b325_regspec.py'), t('b325_correspondence.py'), t('b325_epstein.py'),
         t('b325_run.py'), t('b325_filings.py'), t('b325_extract.py')]

CARRIERS = [
    (t('b325_checks.py'), 'its own fixtures'),
    (t('b325_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("the confinement keystone's finding, AT THE VERIFIED DEPOSIT COPY", CONFINE_DEP,
     'it does not confine zeros to it'),
    ("### and its ablation sentence, at the deposit", CONFINE_DEP,
     'One ingredient removed. Outcome changed.'),
    ("### the same finding at the INTERNAL copy this act appended to", CONFINE_INT,
     'it does not confine zeros to it'),
    ("the residue keystone's sharpest test", RESIDUE, 'positive ledger but RH false'),
    ("the archimedean factor, at the corpus's own census header", CENSUS_TOOL,
     'Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s)'),
    ("### and the census's own 2-D reason", CENSUS_TOOL,
     'critical-line scan would IMPOSE the real part'),
    ("the prime loop the constant was copied from, at the atlas", ATLAS,
     'for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):'),
    ("the inherited constant, at b321's own file", WINDOW,
     'PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)'),
    ("### and b321's own header on why it was left at eleven", WINDOW,
     'so the list is far longer than it needs to be'),
    ("b321 -- the forced sign this act tested from the outside", d('b321_the_window_opened.txt'),
     'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION'),
    ("b324 -- the hand-on this act discharged", d('b324_the_keystones_reread.txt'),
     'THE EPSTEIN DISCRIMINATION TEST'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### bank gives the verdict at its scope', BANK, "AT THE ARC'S CELLS: ### DOES NOT SEE IT"),
    ('### and reports the expectation refuted', BANK, 'REFUTED AT THE CURRENT REACH'),
    ('### and the sign at every cell', BANK, 'NEGATIVE AT ALL THIRTEEN CELLS'),
    ('### and the structural reason', BANK, 'r_Q(2) = r_Q(3) = 0'),
    ('### and the finite channel identically zero', BANK, 'IDENTICALLY ZERO UNTIL `a = 2`'),
    ('### bank prices the reach', BANK, 'CROSSES TO POSITIVE AT'),
    ('### and refuses to verdict it', BANK,
     'WITHOUT ITS CORROBORATION IS A MEASUREMENT, NOT A VERDICT'),
    ('### bank reports the control firing', BANK,
     'THE POSITIVE CONTROL FIRED, AND CAUGHT A REAL DEFECT'),
    ('### and the cause', BANK, "b321's OWN HEADER EXPLAINS WHY IT WAS LEFT AT ELEVEN"),
    ('### and that b321 is not re-verdicted', BANK, 'b321 IS NOT RE-VERDICTED'),
    ('### and the scope-bound constant', BANK, 'THE CONSTANT IS SCOPE-BOUND'),
    ('bank says the distribution does not transfer, in the corpus voice', BANK,
     'DOES NOT TRANSFER, AND THE CORPUS SAYS SO ITSELF'),
    ('### and the finite side is not r_Q', BANK, 'THE FINITE SIDE IS NOT THE REPRESENTATION NUMBERS'),
    ('### and the lawful class transfers, measured', BANK,
     'THE LAWFUL CLASS TRANSFERS, AND THAT IS A MEASURED FACT'),
    ('### and the zero library is half owned', BANK, 'BANKS TWO OFF-LINE ZEROS AND NO ON-LINE ONES'),
    ('bank declares deviation (A)', BANK, 'THE SEAT RAN AHEAD OF ITS OWN EXECUTION BLOCK'),
    ('### and (B)', BANK, 'THE SATISFIABILITY CHECKER REFUSED TO SEAL, AND IT WAS RIGHT'),
    ('### and (C)', BANK, 'THE NOISE-FLOOR GATE WAS FED PAIRS THAT WERE NOT A REFINEMENT'),
    ('### and (C) repaired', BANK, 'ALL THREE RESOLVED, CONVERGED TO NINE DECIMALS'),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### and refuses SEES IT', BANK, 'IT DOES NOT CLAIM `SEES IT`'),
    ('### and refuses the capability reading', BANK,
     'IT DOES NOT CLAIM THE INSTRUMENT CANNOT SEE A FAILURE'),
    ('bank gives step zero', BANK, 'STEP ZERO.'),
    ('### on the canonical drive only', BANK, 'THE CANONICAL DRIVE ONLY'),
    ('bank gives the read', BANK, 'COMPONENT 1 -- THE READ.'),
    ('### with the ledger register decided', BANK,
     'POSITIVITY IS OF THE COEFFICIENT SEQUENCE, NOT OF THE ZEROS'),
    ('### and the off-line zeros', BANK, 'TWO ZEROS, BOTH OFF THE LINE'),
    ('bank gives the pricing, typed', BANK, 'COMPONENT 2 -- THE PRICING, TYPED.'),
    ('### with its verdict', BANK, 'THE FALSIFIER FITS INSIDE THIS ACT'),
    ("### and the run's shape written before it ran", BANK,
     "THE RUN'S SHAPE, AS WRITTEN DOWN BEFORE IT RAN"),
    ('bank gives the run', BANK, 'COMPONENT 3 -- THE RUN.'),
    ('### with the verdict at the cells', BANK, "VERDICT AT THE ARC'S CELLS : ### DOES NOT SEE IT"),
    ('### and the entailment', BANK, 'THE ENTAILMENT, STATED AS THE ORDER REQUIRES'),
    ('### and what the zeta window was', BANK,
     "AND SO THE ZETA WINDOW'S EMPTINESS STANDS AS INTRINSIC AT THIS REACH"),
    ('### without downgrading b321', BANK, 'THIS ACT DOES NOT DOWNGRADE IT'),
    ('### and the priced widths', BANK, "BEYOND THE ARC'S CELLS -- PRICED, NEVER VERDICTED"),
    ('### with the crossing', BANK, 'THE EPSTEIN SIGN CROSSES AT `a = 22`'),
    ('### called a price', BANK, 'THIS IS A PRICE AND NOT A VERDICT'),
    ('bank gives the filings', BANK, 'COMPONENT 4 -- THE FILINGS.'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and that nothing is kept', BANK, 'NOTHING IS KEPT'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 REMAINS OWED UNDER'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('### opening the on-line library', BANK, 'THE ON-LINE EPSTEIN ZERO LIBRARY'),
    ('### and the scope of the constant', BANK, 'THE SCOPE OF `b321_window.PRIMES`'),
    ('### and the atlas cache, guarded not fixed', BANK, 'GUARDED IN THE CALLER'),
    ('### and its own three declared against itself', BANK, 'DECLARED AGAINST THIS ACT ITSELF'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### the bridge read named next', BANK, 'THE BRIDGE READ IS NAMED NEXT BY THE ORDER'),
    ('### and refuses to recommend', BANK, 'NO RECOMMENDATION AND NO RANKING'),
    ('registration names the act', REG, 'THE NEGATIVE CONTROL. ### THE REGISTRATION.'),
    ('### and carries the deviation on its face', REG, "(0) A DEVIATION, ON THIS FILE'S FACE"),
    ('### saying the seat ran ahead', REG, 'RAN AHEAD OF ITS OWN EXECUTION BLOCK'),
    ('### with every bar marked', REG, '[SEAT, POST-HOC]'),
    ('the run reports the fixtures', RUN, 'THE EPSTEIN INSTRUMENT FIXTURES'),
    ('### and the control at a = 32 both ways', RUN,
     'every prime -0.000389214 (permitted) ; eleven primes 0.003489041 (FORBIDDEN'),
    ('the run gives the verdict', RUN, "VERDICT AT THE ARC'S CELLS : DOES NOT SEE IT"),
    ('### the positive control at every cell', RUN,
     'THE POSITIVE CONTROL: ### ZETA IS NON-POSITIVE AT EVERY CELL : True'),
    ('### no forbidden sign', RUN, 'CELLS WHERE EPSTEIN TAKES THE FORBIDDEN SIGN : NONE'),
    ('### the crossing, priced', RUN, 'THE EPSTEIN SIGN CROSSES AT `a = 22.0`'),
    ('### the control at every priced width', RUN,
     'the positive control holds at every priced width too : True'),
    ('### the noise gate', RUN, 'PASS -- all 3 value(s) are above the floor and stable'),
    ('### zero checks failing', RUN, 'CHECKS FAILING : 0'),
    ('the regspec prints the refusal', REGSPEC,
     'THE CHECKER REFUSED: *NOT SATISFIABLE. DO NOT SEAL.*'),
    ('### and that the deviation is not hidden by the move', REGSPEC,
     'THE DEVIATION IS NOT HIDDEN BY THE MOVE'),
    ('the satisfiability run passes on the corrected spec', SATIS, 'JOINTLY SATISFIABLE'),
    ('the filing reports append-only', FIL, 'APPEND-ONLY : True'),
    ('### and the deposit byte-unchanged', FIL, 'THE DEPOSIT IS BYTE-UNCHANGED : True'),
    ('### and zero filing failures', FIL, 'FILING CHECKS FAILING : 0'),
    ('the extract found every quotation', EXTRACT, 'QUOTATIONS NOT FOUND : 0'),
    ('the census found nothing missing', CENSUS, 'TOTAL MISSING : 0'),
    ('the ferry scan was clean', SCAN, 'STRUCK-CLAUSE HITS : 0'),
    ('### on stems too', SCAN, 'BANNED/RETIRED-STEM HITS : 0'),
]

MUST_FAIL = [
    ('the instrument is not said to see it', BANK, 'THE INSTRUMENT SEES IT.'),
    ('### nor to be unable to', BANK, 'THE INSTRUMENT CANNOT SEE A FAILURE.'),
    ('the crossing is not a verdict', BANK, 'THE CROSSING IS THE VERDICT.'),
    ('b321 is not re-verdicted', BANK, 'b321 IS RE-VERDICTED.'),
    ('the zeta window is not downgraded', BANK, 'THE ZETA WINDOW IS DOWNGRADED.'),
    ('the on-line zeros are not claimed', BANK, 'THE ON-LINE ZEROS ARE OWNED.'),
    ('the explicit formula is not closed', BANK, 'THE EXPLICIT FORMULA CLOSES FOR Z_Q.'),
    ('the registration is not said to precede the run', BANK,
     'THE REGISTRATION WAS SEALED BEFORE THE COMPONENTS.'),
    ('the atlas is not fixed', BANK, 'THE ATLAS IS FIXED.'),
    ('no deposited text is edited', BANK, 'THE DEPOSIT IS EDITED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('the wave is not started', BANK, 'THE WAVE IS STARTED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('RH is not addressed', BANK, 'RH HOLDS.'),
    ('### either way', BANK, 'RH FAILS.'),
]

TOOLNUM = [
    ("the Epstein instrument: r_Q, Lambda_Q, kernel, channels, ten fixtures", 'tools/b325_epstein.py'),
    ("the thirteen cells, the priced widths, the positive control, the noise gate",
     'tools/b325_run.py'),
    ("the quotations, the deposit md5 and the drives", 'tools/b325_extract.py'),
    ("the artifact-count prediction demand (ruling 1) and the printed refusal",
     'tools/b325_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the noise-floor gate", 'tools/noise_floor.py'),
    ("the off-line zero library this act read", 'tools/e16/epstein_census.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b325_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b325_correspondence.py'),
    ("the index keys' read-back arms", 'tools/b325_index_append.py'),
    ("the append-only filing and its prefix checks", 'tools/b325_filings.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b325' in x)

SEAL = '8e5b014f1b89fef03bf8d737c9c03d472fe92781131c962c1039ef69a25366c1'


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def main():
    fails = []
    print('=' * 100)
    print('b325 -- GATE SUITE (A NEGATIVE CONTROL THAT CAME BACK SILENT AT THE CELLS REACHED)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (each at the file that EMITTED it; the deposit at its VERIFIED copy):')
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
    reg = io.open(REG, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()
    regspec = io.open(REGSPEC, encoding='utf-8').read()
    rows = [ln for ln in tbl.split('\n') if ln.startswith('| 162 |') or ln.startswith('| 163 |')]
    rowtxt = '\n'.join(rows)

    print('\n  G-NOTSEES (the crossing at a = 22 is a PRICE; nobody writes SEES IT):')
    ns = ('IT DOES NOT CLAIM `SEES IT`' in bank
          and 'PRICED, NEVER VERDICTED' in run
          and 'THIS IS NOT A `SEES IT`' in rowtxt
          and 'NOT A SEES-IT VERDICT' in idx
          and len(rows) == 2)
    verd = [ln for ln in run.split('\n') if 'VERDICT' in ln and 'SEES IT' in ln]
    clean = all('DOES NOT SEE IT' in ln for ln in verd)
    print('    bank, run, table rows and index row all refuse the word : %s' % ns)
    print('    ### every VERDICT line in the run reads DOES NOT SEE IT (%d line(s)) : %s'
          % (len(verd), clean))
    print('    ### **A POSITIVE SIGN WITHOUT ITS CORROBORATION IS A MEASUREMENT.**')
    if not (ns and clean):
        fails.append('G-NOTSEES')

    print('\n  G-NOTCANNOT (a scope statement is not a capability statement):')
    nc = ('IT DOES NOT CLAIM THE INSTRUMENT CANNOT SEE A FAILURE' in bank
          and 'r_Q(2) = r_Q(3) = 0' in run
          and 'r_Q(2) = r_Q(3) = 0' in rowtxt
          and 'r_Q(2) = r_Q(3) = 0' in idx
          and 'A SCOPE STATEMENT IS NOT A CAPABILITY STATEMENT' in idx
          and 'a ~ 22' in idx and 'a ~ 22' in rowtxt)
    print('    the refusal BY NAME, the structural reason and the priced reach ride with the verdict'
          ' in bank, run, table and index : %s' % nc)
    if not nc:
        fails.append('G-NOTCANNOT')

    print('\n  G-CONTROL (the positive control fired, was traced, passes repaired; b321 unmoved):')
    m32 = re.search(r'^\s+32\s+1024\s+\S+\s+(-?\d+\.\d+)\s', run, re.M)
    z32 = float(m32.group(1)) if m32 else float('nan')
    gc = ('eleven primes 0.003489041 (FORBIDDEN' in run
          and 'every prime -0.000389214 (permitted)' in run
          and z32 <= 0.0
          and 'ZETA IS NON-POSITIVE AT EVERY CELL : True' in run
          and 'the positive control holds at every priced width too : True' in run
          and 'b321 IS NOT RE-VERDICTED' in bank
          and 'b321 IS NOT RE-VERDICTED' in rowtxt
          and 'b321 IS NOT RE-VERDICTED' in idx)
    print('    zeta at a = 32 in the banked table : %s (must be <= 0)' % z32)
    print('    fired, traced, repaired, and b321 unmoved in bank, table and index : %s' % gc)
    print('    ### **A CONTROL THAT FIRES IS WORTH MORE THAN ONE THAT PASSES.**')
    if not gc:
        fails.append('G-CONTROL')

    print('\n  G-DEVIATION (three of the act\'s own, at full prominence, and on the sealed face):')
    gd = ("(0) A DEVIATION, ON THIS FILE'S FACE" in reg
          and reg.index("(0) A DEVIATION") < reg.index('(A) WHAT THIS ACT IS')
          and '[SEAT, POST-HOC]' in reg and '[ORDER]' in reg
          and 'THE CHECKER REFUSED: *NOT SATISFIABLE. DO NOT SEAL.*' in regspec
          and 'THREE DEVIATIONS AND DEFECTS OF THIS ACT' in bank
          and bank.index('THREE DEVIATIONS AND DEFECTS') < bank.index('WHAT THIS ACT DOES NOT SAY.')
          and 'THREE FAILINGS OF ITS OWN' in rowtxt
          and 'THREE FAILINGS OF ITS OWN' in idx)
    print('    section (0) precedes every bar; bars marked; refusal printed; bank carries all three'
          ' before its scope section; table and index carry them : %s' % gd)
    if not gd:
        fails.append('G-DEVIATION')

    print('\n  G-DEPOSIT (no file under outputs/DEPOSITED-v1.1.2/ is written):')
    st = subprocess.run(['git', '-C', PP, 'status', '--porcelain',
                         'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    twin = hashlib.md5(open(CONFINE_DEP, 'rb').read()).hexdigest()
    print('    git status over the deposit path : %r' % st)
    print('    deposited twin md5 : %s  (verified %s)' % (twin, TWIN_MD5))
    print('    ### ### **BYTE-UNCHANGED : %s**' % (not st and twin == TWIN_MD5))
    if st or twin != TWIN_MD5:
        fails.append('G-DEPOSIT')

    print('\n  G-APPEND (the internal keystone append-only, against the file AND the blob):')
    rel = 'day1/Which_Structure_Confines.md'
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(CONFINE_INT, encoding='utf-8', errors='replace').read()
    pfx = now.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))
    once = now.count('<!-- b325 cross-reference -->')
    print('    %-40s blob is a TRUE PREFIX : %s ; block appears %d time(s)' % (rel, pfx, once))
    if not (pfx and once == 1):
        fails.append('G-APPEND')

    print('\n  G-NOWIDEN (the seal is the one on the file whose face declares the deviation):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    same = SEAL in reg
    print('    seal verifies : %s ; hash matches the literal in this gate : %s' % (intact, same))
    print('    ### **THIS SEAL DOES NOT CERTIFY BARS-BEFORE-VALUES, AND THE FILE SAYS SO.**')
    if not (intact and same):
        fails.append('G-NOWIDEN')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    eps = io.open(t('b325_epstein.py'), encoding='utf-8').read()
    runsrc = io.open(t('b325_run.py'), encoding='utf-8').read()
    arms = [('the falsifier, able to return a forbidden sign (it did, at a = 22)',
             '0.017211484' in run),
            ('the positive control, able to FAIL (it did, with eleven primes)',
             'FORBIDDEN' in run),
            ('the Epstein fixtures, all ten printed', run.count('True') >= 10),
            ('the full-prime control guards the atlas cache in the caller',
             '_KERN' in eps),
            ('the noise gate fed a refinement pair, not adjacent cells',
             'RESOLVED' in run and 'DRIFTING' not in run.split('(3c)')[-1]),
            ('the filing tool, able to REFUSE a deposited target',
             'REFUSED -- deposited path targeted' in io.open(t('b325_filings.py'),
                                                             encoding='utf-8').read()),
            ('the filing, idempotent on a second run', 'ALREADY FILED' in
             io.open(d('b325_filings_rerun.txt'), encoding='utf-8').read()
             if os.path.exists(d('b325_filings_rerun.txt')) else False),
            ('the run file names its verdict from the data, not a literal',
             'DOES NOT SEE IT' in runsrc and 'SEES IT' in runsrc)]
    for lbl, ok_ in arms:
        print('    %-66s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOEDIT (no owner instrument edited -- the atlas cache defect included):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    print('    ### the atlas cache is GUARDED IN THE CALLER, REPORTED, LEFT ALONE : %s'
          % ('GUARDED IN THE CALLER' in bank))
    if dirty or 'GUARDED IN THE CALLER' not in bank:
        fails.append('G-NOEDIT')

    print('\n  G-ONCE (tools that write run files write once per path):')
    two_names = all(('_rerun.txt' in io.open(t(x), encoding='utf-8').read())
                    for x in ('b325_filings.py',))
    run_sha = sha(RUN)
    print('    the idempotent writer names its two paths differently : %s' % two_names)
    print('    the run file sha256 (deterministic recomputation) : %s' % run_sha[:16])
    print('    ### b325_run.py is a pure recomputation; b325_index_append.py writes through a')
    print('    ### shell redirect the caller names; the correspondence tool writes the TABLE only.')
    if not two_names:
        fails.append('G-ONCE')

    print('\n  G-PAPERS (only the internal keystone changed in PLACE-papers):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = sorted(x[3:].strip() for x in pp.splitlines()
                     if x.strip() and not x.startswith('??'))
    only = tracked in ([], [rel])
    print('    tracked changes : %s' % tracked)
    print('    ### exactly the internal keystone, or already committed : %s' % only)
    if not only:
        fails.append('G-PAPERS')

    print('\n  G-ANCESTOR (the correspondence table is a true prefix of its blob):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    pfx2 = tbl.startswith(head.rstrip('\n'))
    print('    table is a TRUE PREFIX : %s' % pfx2)
    if not pfx2:
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

    print('\n  G-STEM-APPENDED (the appended block, swept):')
    blk = now[now.index('<!-- b325 cross-reference -->'):] \
        if '<!-- b325 cross-reference -->' in now else ''
    ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
    _c, sh = ferry_scan.scan_text(blk, [], stem_list)
    print('    %-40s struck : %d   stem : %d' % (rel, len(ch), len(sh)))
    for h in sh:
        print('        %s' % h[3][:92])
    if ch or sh:
        fails.append('G-STEM-APPENDED')

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
        print('    %-66s %-34s exists=%s tracked=%s' % (what[:66], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN),
                      ('the filing', FIL), ('the extract', EXTRACT), ('the regspec', REGSPEC)]:
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
