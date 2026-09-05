# -*- coding: utf-8 -*-
"""b328_checks.py -- THE GATE SUITE FOR A FAMILY THAT SAW THE COUNTEREXAMPLE WHILE ZETA HELD.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-ZETA`** ### -- ### **THE ONE THE ORDER PUTS FIRST.** ### Every cell's zeta places side
###     certified NEGATIVE through the gate and closing with zeta's own library; the bank says NO FLIP and
###     the must-fail line `ZETA FLIPS.` is absent.
###   ### ### **`G-NOTGENERAL`** ### -- SEES IT is a verdict on this family at this reach; bank, rows,
###     index and the ledger update must scope it BY NAME and keep b326's verdict on the arc's family.
###   ### ### **`G-VERDICT`** ### -- the sealed branches re-applied to the cell files: seven SEES IT with
###     the quadruple accounting and both closures; the one exception `E20` certified negative and named.
###   ### **`G-DERIVE` / `G-BUILD` / `G-ROUTES`** ### -- the derive, build and route records agree with the
###     bank: (F1) derives, (F2) met, the three defective sealed bars declared with their measurements.
###   ### **`G-ORDER`** ### -- the registration sealed before any instrument ran; the seal intact on raw
###     bytes after the restart.
###   ### **`G-LORE`** ### -- the phase condition in the lore, both polarities, one entry.
"""
import hashlib
import io
import json
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

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
LORE = os.path.join(ROOT, 'tools', 'lore_rules.py')

OWNERS_RELAY = ['tools/b317_smear.py', 'tools/b318_square.py', 'tools/b321_window.py', 'tools/b325_epstein.py',
                'tools/b326_windows.py', 'tools/b326_closure.py', 'tools/e16/carto_atlas.py', 'tools/e16/epstein_census.py',
                'tools/noise_floor.py', 'tools/b305_source.py', 'tools/ferry_scan.py', 'tools/mirror_roster.json',
                'tools/reg_seal.py', 'tools/b300_regspec.py', 'HANDOFF.md', 'data/STRUCK_CLAUSES.md',
                'data/b326_epstein_zeros.json', 'data/b326_offline.json', 'data/b326_closure.json', 'data/b326_windows.json']
OWNERS_PP = ['outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md', 'FINDINGS.md', 'VERIFICATION_LOOM.md', 'EMERGING_RESEARCH_PROGRAMMES.md']
PP_WRITTEN = ['FACES_LEDGER.md', 'OPEN_TRAILS.md']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b328_the_discriminating_family.txt')
REG = d('b328_registration_2026-09-05.txt')
EXTRACT = d('b328_extract_notes.txt')
SRC = d('b328_source.txt')
DER = d('b328_derive_run.txt')
BLD = d('b328_build_run.txt')
RTS = d('b328_routes_run.txt')
FAM = d('b328_family_run.txt')
FIL = d('b328_filings_run.txt')
CORR = d('b328_corr_run2.txt')
IDX = d('b328_index_run.txt')
LRUN = d('b328_lore_run.txt')
SCAN = d('b328_ferry_scan.txt')
SCAN2 = d('b328_ferry_resume_scan.txt')
CENSUS = d('b328_census.txt')
FCEN = d('b328_faces_census.txt')
REGSPEC = d('b328_regspec_run.txt')
SATIS = d('b328_satisfiable_run.txt')
CELLS = [(k, a) for k in ('E', 'O') for a in (20.0, 40.0, 81.0, 160.0)]
CELL_RUNS = [d('b328_cell_%s_%g_run.txt' % (k, a)) for k, a in CELLS]

OWNED = [BANK, REG, DER, BLD, RTS, FAM, FIL, CORR, IDX, LRUN, CENSUS, FCEN, REGSPEC, SATIS,
         d('b328_corr_run.txt'), d('b328_lore_rerun.txt'), d('b328_routes_run_first_diagnosis.txt'),
         d('b328_derive.json'), d('b328_build.json'), d('b328_routes.json'), d('b328_routes_first_diagnosis.json'),
         d('b328_family.json'), d('b328_satisfiable.json'), d('b328_pins_stepzero.txt'), d('b328_reg_termscan.txt'),
         d('b328_reg_gate.txt'), d('audit_b328_index_query.txt'),
         t('b328_source.py'), t('b328_extract.py'), t('b328_regspec.py'), t('b328_family.py'), t('b328_routes.py'),
         t('b328_lore_append.py'), t('b328_filings.py'), t('b328_correspondence.py'), t('b328_index_append.py')] + CELL_RUNS + \
        [d('b328_cell_%s_%g.json' % (k, a)) for k, a in CELLS]

CARRIERS = [
    (t('b328_checks.py'), 'its own fixtures'),
    (d('b328_ferry_2026-09-05.txt'), "IT IS THE ORDER -- not this act's writing"),
    (d('b328_ferry_resume_2026-09-05.txt'), 'IT IS THE RESUME ORDER'),
    (SCAN, "the scan's own log"), (SCAN2, "the resume scan's own log"),
    (SRC, 'it names the pinned artefact and its fragments'),
    (d('b328_source_text.txt'), "THE PINNED SOURCE'S OWN TEXT LAYER -- not this act's writing"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("b326 -- the seed priced, not built", d('b326_the_reach.txt'), 'A seed that changes sign there is'),
    ("### and the family that could see it", d('b326_the_reach.txt'), 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN'),
    ("b321 -- the balance is minus the zero side", d('b321_the_window_opened.txt'), 'SUM_v W_v(f) = - Z'),
    ("### and the pole term vanishes for a lawful f", d('b321_the_window_opened.txt'), 'THE POLE TERM VANISHES IDENTICALLY FOR A LAWFUL'),
    ("b320 -- Definition 3.1 applied", d('b320_the_lawful_function.txt'), '`f-hat >= 0` pointwise'),
    ("b317 -- the two moments", t('b317_smear.py'), 'INT f d*rho = 0'),
    ("b326_closure -- the four terms of a quadruple", t('b326_closure.py'), 'for rho in (complex(beta, gam), complex(beta, -gam), complex(1 - beta, gam), complex(1 - beta, -gam)):'),
    ("b326_windows -- the places sides", t('b326_windows.py'), 'places_z=PRz1 - Az1, places_q=PRq - Aq1'),
    ("the first off-line zero, at the library", d('b326_epstein_zeros.json'), '0.9532604747946607'),
    ("### its on-line neighbour below", d('b326_epstein_zeros.json'), '14.630459532385498'),
    ("the faces ledger's Epstein row", LEDGER, '| F7 | F7 -- the Epstein negative control'),
    ("the trail on OPEN_TRAILS", TRAILS, '| **2** | `W-ORD-DISCRIMINATING-FAMILY` | **CONSTRUCTION** |'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### zeta held at every cell', BANK, 'THE ZETA CONTROL HELD AT EVERY CELL: THE PERMITTED SIGN, CERTIFIED, AND THE FORMULA'),
    ('### no flip', BANK, 'NO FLIP. ### THERE IS NOTHING TO WALK.'),
    ('### sees it at seven of eight', BANK, 'SEES IT -- AT SEVEN OF EIGHT CELLS.'),
    ('### the quadruple accounts', BANK, 'THE FIRST OFF-LINE QUADRUPLE ACCOUNTS FOR THE SIGN'),
    ('### F3 met', BANK, "THE NAVIGATOR'S (F3) IS MET."),
    ('### the condition derives', BANK, 'THE CONDITION DERIVES AS ASSERTED, WITH THE QUADRUPLE'),
    ('### negative past forty-five', BANK, 'NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE'),
    ('### why b326 was positive', BANK, "WHY b326's SUMS WERE POSITIVE."),
    ('### F2 met', BANK, '(F2) IS MET.'),
    ('### E20 the exception', BANK, 'THE ONE CELL THAT DOES NOT SEE IT IS THE NARROWEST EVEN ONE'),
    ('### three sealed bars', BANK, 'THREE SEALED BARS FOUND DEFECTIVE BY RUNNING THEM, NONE EDITED, EACH MEASURED:'),
    ('### the signs do not rest on them', BANK, 'THE SIGNS DO NOT REST ON ANY OF THE THREE'),
    ("### the seat's own defects", BANK, "AND THE SEAT'S OWN DEFECTS, DECLARED:"),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### not counterexamples in general', BANK, 'IT DOES NOT SAY THE INSTRUMENT SEES COUNTEREXAMPLES.'),
    ('### nothing about zeta beyond scope', BANK, "IT SAYS NOTHING ABOUT ZETA BEYOND THE CONTROL'S SCOPE."),
    ('### b326 not re-verdicted', BANK, 'IT DOES NOT RE-VERDICT b326.'),
    ('### nothing about totality', BANK, 'NOTHING ABOUT TOTALITY.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('### sealed before any run', BANK, 'THE REGISTRATION WAS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RAN.'),
    ('### the resume', BANK, 'THE RESUME.'),
    ('### seal recomputed on raw bytes', BANK, 'the seal recomputed on raw bytes equal to the banked line'),
    ('bank gives step zero', BANK, 'STEP ZERO.'),
    ('### two ledgers censused', BANK, 'THE LEDGER CENSUS, WITH ITS SCOPE, NOW OVER TWO LEDGERS:'),
    ('bank gives component 1', BANK, 'COMPONENT 1 -- THE CONDITION, DERIVED AND CHECKED.'),
    ('### the criterion as the source states it', BANK, 'THE CRITERION AS THE SOURCE STATES IT, WITH ITS POLE TERMS.'),
    ('### the pole terms by vanishing at 0 and 1', BANK, 'THE POLE'),
    ('### the four-term sum', BANK, '**`S_4 = 4 Re[ G(c) G(-c) ]`.**'),
    ('### the even reduction', BANK, '**`S_4 = 4 |G(c)|^2 cos(2 phi)`, NEGATIVE EXACTLY WHEN `45 deg < |phi| < 135 deg`.**'),
    ('### where the phase comes from', BANK, 'WHERE THE PHASE COMES FROM.'),
    ('### the arc phases table', BANK, 'phase  -5.26   -4.92   -4.48   -3.74   -1.95   -0.06   +0.78   +0.87   +0.97   +1.81   +4.92  +12.83  +24.10'),
    ('bank gives component 2', BANK, 'COMPONENT 2 -- THE CONSTRUCTION.'),
    ('### lawful at every width', BANK, 'LAWFUL AT EVERY WIDTH, MEASURED:'),
    ('### the even seed reaches the threshold', BANK, 'THE EVEN SEED REACHES THE THRESHOLD AT EVERY WIDTH; (F2) IS MET.'),
    ('### B4 fails as sealed', BANK, '(B4) ON THESE SEEDS, AS SEALED: FAILS'),
    ('### a route meets the bar', BANK, 'A ROUTE INTEGRATING THE SAME FUNCTION MEETS THE SEALED'),
    ('bank gives component 3', BANK, 'COMPONENT 3 -- THE CONTROL RUN.'),
    ('### all sixteen resolved', BANK, 'SIXTEEN VALUES RESOLVED, DRIFTS `2e-16` TO `6e-15`, EVERY SIGN CERTIFIED AT MORE THAN TEN TIMES ITS'),
    ('### eight of eight closures', BANK, 'ZETA CLOSES AT EIGHT OF EIGHT; THE EPSTEIN FUNCTION CLOSES AT EIGHT OF EIGHT WITH EVERY LOCATED'),
    ('### the fourth link walked again', BANK, 'the fourth link b326 walked,'),
    ('### B6 arm exceeded', BANK, 'THE ARCHIMEDEAN-ROUTE ARM AT `1e-9` RELATIVE IS EXCEEDED ON THE FOUR'),
    ('### the verdict', BANK, '**VERDICT: SEES IT** ### at `E40, E81, E160, O20, O40, O81, O160`'),
    ('### zeta holds at every cell', BANK, 'ZETA HOLDS AT EVERY'),
    ('bank gives component 4', BANK, 'COMPONENT 4 -- THE ENTAILMENT, AT EXACTLY ITS SCOPE.'),
    ('### the passed test for this family', BANK, 'The zeta window is a PASSED TEST for this family'),
    ('### the first enumerated way', BANK, "THE FAMILY'S CONSTRUCTION IS FILED AS THE FIRST ENUMERATED WAY THE CLAUSE COULD"),
    ('### partly paid', BANK, '**PARTLY PAID**'),
    ('bank gives the closing', BANK, 'THE CLOSING.'),
    ('### the refusal kept', BANK, 'the refusal kept (`b328_corr_run.txt`) beside the write (`_run2.txt`).'),
    ('### the lore gains the rule', BANK, 'THE LORE GAINS THE PHASE CONDITION'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### nothing kept', BANK, 'NOTHING IS KEPT'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 REMAINS OWED UNDER'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('### the width floor opened', BANK, 'THE WIDTH FLOOR OF THE EVEN FAMILY'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### the sealing module next', BANK, 'THE FINITE-SIDE SEALING MODULE IS NAMED NEXT BY THE ORDER'),
    ('### the fold accumulating', BANK, 'THE FOLD FROM b323 ONWARD IS ACCUMULATING'),
    ('### no recommendation', BANK, 'NO RECOMMENDATION AND NO RANKING'),
    ('registration names the act', REG, 'THE DISCRIMINATING FAMILY. ### THE REGISTRATION.'),
    ('### sealed before any run', REG, 'THIS REGISTRATION IS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RUNS.'),
    ('### the four-term sum as a bar', REG, '`S_4 := f~(rho) + f~(conj rho) + f~(1 - rho) + f~(1 - conj rho) = 4 Re[ G(c) G(-c) ]`'),
    ('### the branches fixed', REG, 'THE VERDICTS, AS THE ORDER FIXES THEM:'),
    ('### the widths fixed', REG, '`a in {20, 40, 81, 160}`'),
    ('the derive run: F1', DER, '(F1) the even-seed reduction : DERIVES AS ASSERTED'),
    ('### B1 fails as sealed', DER, 'bar 1e-09   ### FAILS AS SEALED ###'),
    ('### B3 holds', DER, 'every even-reduction sign the banked sign : HOLDS'),
    ('the build run: F2', BLD, '(F2) an even seed reaches the threshold without an odd component : YES'),
    ('### lawful', BLD, 'lawful at every width : E True  O True'),
    ('the routes run: Gauss meets the bar', RTS, 'MEETS THE SEALED BAR'),
    ('### the first diagnosis refuted', RTS, "first diagnosis (second order) was refuted by the 2x ratio"),
    ('the family run: verdict', FAM, 'VERDICT : SEES IT'),
    ('### F3 met', FAM, '(F3) SEES IT with zeta holding : MET'),
    ('the filing: ledger written', FIL, 'FACES_LEDGER.md   WRITTEN'),
    ('### deposit unchanged', FIL, 'THE DEPOSIT IS BYTE-UNCHANGED : True'),
    ('the rows read back', CORR, 'last 2 row number(s) are [168, 169]'),
    ('the first rows run refused', d('b328_corr_run.txt'), 'cells carrying an UNESCAPED pipe (checked BEFORE writing) : 1'),
    ('the index key read back', IDX, 'discriminating-family returns 2 row(s), 2 required  PASS'),
    ('### the arm', IDX, 'the answer scopes the verdict to the family BY NAME        : True'),
    ('the lore run', LRUN, 'phase condition (b326/b328)          fires: True   stays quiet: True   PASS'),
    ('the satisfiability run', SATIS, 'JOINTLY SATISFIABLE'),
    ('the regspec found no predictions', REGSPEC, 'ARTIFACT-COUNT PREDICTIONS FOUND : 0'),
    ('the ferry scan was clean', SCAN, 'STRUCK-CLAUSE HITS : 0'),
    ('the resume scan was clean', SCAN2, 'STRUCK-CLAUSE HITS : 0'),
    ('the handoff census', CENSUS, 'TOTAL MISSING : 0'),
    ('the faces census', FCEN, 'TOTAL MISSING : 0'),
    ('the extract file reports itself', EXTRACT, 'PATHS MISSING : 0 ; QUOTATIONS NOT FOUND : 0'),
    ('the source pin reports itself', SRC, 'FRAGMENTS NOT LOCATED : 0'),
]

MUST_FAIL = [
    ('the instrument is not said to see counterexamples', BANK, 'THE INSTRUMENT SEES COUNTEREXAMPLES.'),
    ('zeta did not flip', BANK, 'ZETA FLIPS.'),
    ('b326 is not re-verdicted', BANK, 'b326 IS RE-VERDICTED.'),
    ("the arc's family is not said to see it", BANK, "THE ARC'S FAMILY SEES IT."),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('totality is not reached', BANK, 'TOTALITY IS REACHED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('RH is not addressed', BANK, 'RH HOLDS.'),
    ('### either way', BANK, 'RH FAILS.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('no deposited text is edited', BANK, 'THE DEPOSIT IS EDITED.'),
    ('no sealed bar was edited', BANK, 'THE BAR WAS EDITED.'),
]

TOOLNUM = [
    ("the source pin: bytes, hash, pages, fragments located", 'tools/b328_source.py'),
    ("the extract step's counts", 'tools/b328_extract.py'),
    ("the artifact-count prediction demand", 'tools/b328_regspec.py'),
    ("the satisfiability verdict", 'tools/reg_satisfiable.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
    ("the condition's checks, the seeds, the cells, the verdicts", 'tools/b328_family.py'),
    ("the route diagnostic and the Gauss route", 'tools/b328_routes.py'),
    ("the places sides and the gate (imported)", 'tools/b326_windows.py'),
    ("the closure and the exact transforms (imported)", 'tools/b326_closure.py'),
    ("the noise-floor gate", 'tools/noise_floor.py'),
    ("the seeds' builders and the class test (imported)", 'tools/b318_square.py'),
    ("the corpus's bump (imported)", 'tools/e16/carto_atlas.py'),
    ("the finite sides' second routes (imported)", 'tools/b325_epstein.py'),
    ("the ledger and trail updates", 'tools/b328_filings.py'),
    ("the writer's append mode", 'tools/b327_faces_row.py'),
    ("the lore entry and its fixture", 'tools/b328_lore_append.py'),
    ("the correspondence rows' numbers", 'tools/b328_correspondence.py'),
    ("the index key's read-back arms", 'tools/b328_index_append.py'),
    ("what is missing from HANDOFF, counted", 'tools/b307_handoff_census.py'),
    ("what is missing from the faces ledger, counted", 'tools/b327_faces_census.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the pins by ls-remote", 'tools/b303_pins.py'),
    ("the gate, needle and hedge counts", 'tools/b328_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b328' in x)
SEAL = 'ba4b7b9671563441c04ae21ba43350f405fa6a383c756c0f3b85e8cc351b64a3'


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace('\r\n', '\n')


def main():
    fails = []
    print('=' * 100)
    print('b328 -- GATE SUITE (THE DISCRIMINATING FAMILY: SEES IT ON THIS FAMILY, ZETA HOLDING, NOTHING GENERAL)')
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
    reg = io.open(REG, encoding='utf-8').read()
    fam = json.load(io.open(d('b328_family.json'), encoding='utf-8'))
    der = json.load(io.open(d('b328_derive.json'), encoding='utf-8'))
    bld = json.load(io.open(d('b328_build.json'), encoding='utf-8'))
    rts = json.load(io.open(d('b328_routes.json'), encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    trl = io.open(TRAILS, encoding='utf-8', errors='replace').read()
    rows = [ln for ln in tbl.split('\n') if ln.startswith('| 168 |') or ln.startswith('| 169 |')]
    rowtxt = '\n'.join(rows)
    cells = {(c['kind'], c['a']): c for c in fam['cells']}

    print('\n  G-ZETA (every cell: zeta certified NEGATIVE through the gate and closing; no flip anywhere):')
    gz = all(c['gate_z']['certified'] and c['gate_z']['sign'] == '-' and c['closure']['status_z'] == 'CLOSES' for c in fam['cells'])
    gz = gz and len(fam['cells']) == 8 and not fam['flips'] and 'NO FLIP. ### THERE IS NOTHING TO WALK.' in bank
    print('    8 cells, zeta certified negative and closing at each, flips %s : %s' % (fam['flips'], gz))
    if not gz:
        fails.append('G-ZETA')

    print('\n  G-VERDICT (the sealed branches re-applied to the cell files):')
    sees = set((k, a) for k, a in fam['sees'])
    expect = set(CELLS) - {('E', 20.0)}
    ok_sees = all(cells[k]['gate_q']['certified'] and cells[k]['gate_q']['sign'] == '+' and cells[k]['closure']['status_q_all'] == 'CLOSES'
                  and cells[k]['closure']['accounts'] for k in sees)
    e20 = cells[('E', 20.0)]
    ok_e20 = e20['gate_q']['certified'] and e20['gate_q']['sign'] == '-' and not e20['closure']['accounts']
    gv = (fam['verdict'] == 'SEES IT' and sees == expect and ok_sees and ok_e20 and 'DOES NOT SEE IT at\n### `E20`' in bank.replace('### **DOES NOT SEE IT at', 'DOES NOT SEE IT at'))
    gv = (fam['verdict'] == 'SEES IT' and sees == expect and ok_sees and ok_e20 and '`E20`**, the narrowest even cell' in bank)
    print('    verdict %s ; sees == every cell but E20 : %s ; each sees cell certified +, closes, quadruple accounts : %s ; E20 certified -, not accounting : %s : %s'
          % (fam['verdict'], sees == expect, ok_sees, ok_e20, gv))
    if not gv:
        fails.append('G-VERDICT')

    print('\n  G-NOTGENERAL (a verdict on this family, this instrument, this reach; b326 unmoved):')
    ng = ('IT DOES NOT SAY THE INSTRUMENT SEES COUNTEREXAMPLES.' in bank
          and 'NOT ON THE METHOD AND NOT ON ZETA' in idx and "b326's DOES NOT SEE IT on the arc's family STANDS" in idx
          and "b326's DOES NOT SEE IT ON THE ARC'S FAMILY STANDS" in rowtxt and 'NOTHING ABOUT TOTALITY' in rowtxt and len(rows) == 2
          and "b326's DOES NOT SEE IT on the arc's family stands" in led and 'PARTLY PAID' in led and 'PARTLY PAID' in trl
          and ('VERDICT: %s' % fam['verdict']) in led and ('**%s**' % fam['verdict']) in trl)
    print('    bank, index, rows, ledger update and trail scope the verdict and keep b326 : %s' % ng)
    if not ng:
        fails.append('G-NOTGENERAL')

    print('\n  G-DERIVE (F1 derives; B2, B3, B4 hold on the arc seeds; B1 fails as sealed and is declared with its grid ratio):')
    gd = (der['F1'] and der['B2']['holds'] and der['B3']['holds'] and der['B4']['holds'] and not der['B1']['holds']
          and all(der['fixtures']) and abs(der['B1']['worst_vs_coarse'] / der['B1']['worst'] - 16.0) < 0.05
          and max(abs(p) for p in der['B3']['phases']) < 45.0
          and '(B1) at\n### `1e-9` relative fails at `1.06e-7`' in bank.replace('### (B1) at\n### `1e-9`', '(B1) at\n### `1e-9`'))
    gd = (der['F1'] and der['B2']['holds'] and der['B3']['holds'] and der['B4']['holds'] and not der['B1']['holds']
          and all(der['fixtures']) and abs(der['B1']['worst_vs_coarse'] / der['B1']['worst'] - 16.0) < 0.05
          and max(abs(p) for p in der['B3']['phases']) < 45.0 and 'a ratio of `16.00`' in bank)
    print('    F1 %s B1 %s (ratio %.2f) B2 %s B3 %s (max |phase| %.2f) B4 %s : %s'
          % (der['F1'], der['B1']['holds'], der['B1']['worst_vs_coarse'] / der['B1']['worst'], der['B2']['holds'], der['B3']['holds'],
             max(abs(p) for p in der['B3']['phases']), der['B4']['holds'], gd))
    if not gd:
        fails.append('G-DERIVE')

    print('\n  G-BUILD (both seeds lawful at every width; the even seed past 45 deg everywhere, the odd below; F2 met):')
    gb = (all(x['law']['def31'] and x['law']['poles_ok'] and x['law']['P_ok'] for x in bld)
          and all(abs(x['transform']['phase_deg']) > 45 for x in bld if x['kind'] == 'E')
          and all(abs(x['transform']['phase_deg']) < 45 for x in bld if x['kind'] == 'O')
          and all(x['transform']['even_symmetry'] <= 1e-12 for x in bld if x['kind'] == 'E')
          and len(bld) == 8 and '(F2) IS MET.' in bank)
    print('    %s' % gb)
    if not gb:
        fails.append('G-BUILD')

    print('\n  G-ROUTES (B4 as sealed fails on the seeds; the Gauss route meets the bar; the first diagnosis kept and refuted):')
    gr = (all(x['transform']['route_diff'] > 1e-10 for x in bld) and all(r['gauss_meets_bar'] for r in rts)
          and all(r['simpson_2x'] < 1e-11 for r in rts) and os.path.exists(d('b328_routes_run_first_diagnosis.txt'))
          and '(B4) ON THESE SEEDS, AS SEALED: FAILS' in bank)
    print('    %s' % gr)
    if not gr:
        fails.append('G-ROUTES')

    print('\n  G-B6 (the archimedean-route arm exceeded on the four even cells and met on the four odd, as declared):')
    ev = [cells[('E', a)]['route_arch'] for a in (20.0, 40.0, 81.0, 160.0)]
    od = [cells[('O', a)]['route_arch'] for a in (20.0, 40.0, 81.0, 160.0)]
    g6 = (all(x > 1e-9 for x in ev) and all(x <= 1e-9 for x in od) and all(c['lamq_diff'] <= 1e-9 for c in fam['cells'])
          and all(c['route_prime'] <= 1e-12 for c in fam['cells']) and 'IS EXCEEDED ON THE FOUR' in bank)
    print('    even %s ; odd %s : %s' % (['%.2e' % x for x in ev], ['%.2e' % x for x in od], g6))
    if not g6:
        fails.append('G-B6')

    print('\n  G-ORDER (the registration sealed before any instrument ran; the seal intact on raw bytes):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    i = raw.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(raw[:i]).hexdigest() if i > 0 else ''
    seal_m = os.path.getmtime(REG)
    firsts = [os.path.getmtime(p) for p in [DER, BLD, RTS, FAM, FIL, CORR, IDX, LRUN] + CELL_RUNS if os.path.exists(p)]
    precedes = all(seal_m < m for m in firsts)
    print('    seal verifies : %s ; raw-bytes hash equals the literal : %s ; the sealed file predates every instrument record : %s'
          % (intact, rawhash == SEAL, precedes))
    if not (intact and rawhash == SEAL and precedes):
        fails.append('G-ORDER')

    print('\n  G-LORE (the phase condition in the lore once, both polarities, the lore self-test exit 0):')
    lr = subprocess.run([sys.executable, LORE], capture_output=True, text=True, encoding='utf-8', errors='replace')
    fired = any('phase condition' in ln and 'fires: True' in ln and 'stays quiet: True' in ln for ln in (lr.stdout or '').splitlines())
    lore = io.open(LORE, encoding='utf-8').read()
    gl = fired and lr.returncode == 0 and lore.count('four-term sum at an off-line quadruple') == 1
    print('    fires/quiet %s ; exit %d ; entry once %s : %s' % (fired, lr.returncode, lore.count('four-term sum at an off-line quadruple') == 1, gl))
    if not gl:
        fails.append('G-LORE')

    print('\n  G-APPEND (the two PLACE-papers files: blob a TRUE PREFIX; each b328 block once):')
    for rel, mark in (('FACES_LEDGER.md', '<!-- b328 update -->'), ('OPEN_TRAILS.md', '<!-- b328 trail update -->')):
        now = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        hb = blob_of(PP, rel)
        ok = norm(now).startswith(norm(hb).rstrip('\n')) if hb is not None else True
        print('    %-20s TRUE PREFIX : %s ; block once : %s' % (rel, ok, now.count(mark) == 1))
        if not (ok and now.count(mark) == 1):
            fails.append('G-APPEND ' + rel)

    print('\n  G-DEPOSIT (no file under outputs/DEPOSITED-v1.1.2/ is written):')
    st = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    print('    git status over the deposit path : %r' % st)
    if st:
        fails.append('G-DEPOSIT')

    print('\n  G-NOEDIT (owner instruments untouched; the lore and the writer edited by append only):')
    dr = git(ROOT, 'status', '--porcelain', '--', *OWNERS_RELAY).strip()
    dp = git(PP, 'status', '--porcelain', '--', *OWNERS_PP).strip()
    print('    relay owners : %r ; papers owners : %r' % (dr, dp))
    if dr or dp:
        fails.append('G-NOEDIT')

    print('\n  G-PAPERS (only FACES_LEDGER.md and OPEN_TRAILS.md changed in PLACE-papers, or already committed):')
    pp = git(PP, 'status', '--porcelain')
    changed = sorted(x[3:].strip() for x in pp.splitlines() if x.strip() and not x.startswith('??'))
    only = set(changed) <= set(PP_WRITTEN)
    print('    tracked changes : %s : %s' % (changed, only))
    if not only:
        fails.append('G-PAPERS')

    print('\n  G-ANCESTOR (the correspondence table is a true prefix of its blob):')
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    pfx2 = norm(tbl).startswith(norm(head).rstrip('\n'))
    print('    table is a TRUE PREFIX : %s' % pfx2)
    if not pfx2:
        fails.append('G-ANCESTOR')

    print('\n  G-COMPUTE (the tools of this act importing a numeric library, over STRIPPED code; the controls run against the cap of 8):')
    q, loud = K7.strip_fixture()
    comp = []
    for name in sorted(os.listdir(os.path.join(ROOT, 'tools'))):
        if name.startswith('b328') and name.endswith('.py'):
            src = K7.strip_text(io.open(t(name), encoding='utf-8').read())
            if re.search(r'\bimport\s+(mpmath|numpy|scipy)\b', src):
                comp.append(name)
    ncells = sum(1 for p in CELL_RUNS if os.path.exists(p))
    gc = q and loud and comp == ['b328_family.py', 'b328_routes.py'] and ncells <= 8
    print('    stripper fixture %s/%s ; numeric tools %s ; cell records %d (cap 8) : %s' % (q, loud, comp, ncells, gc))
    if not gc:
        fails.append('G-COMPUTE')

    print('\n  G-ONCE (run files written once per path; the refused first passes kept):')
    once_ok = (os.path.exists(d('b328_corr_run.txt')) and os.path.exists(CORR) and os.path.exists(d('b328_routes_run_first_diagnosis.txt'))
               and os.path.exists(LRUN) and os.path.exists(d('b328_lore_rerun.txt')) and all(os.path.exists(p) for p in CELL_RUNS)
               and 'b328_filings_rerun' in io.open(t('b328_filings.py'), encoding='utf-8').read())
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

    print('\n  G-STEM-APPENDED (the two appended blocks, swept):')
    for rel, mark in (('FACES_LEDGER.md', '<!-- b328 update -->'), ('OPEN_TRAILS.md', '<!-- b328 trail update -->')):
        txt = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        blk = txt[txt.index(mark):] if mark in txt else ''
        ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk, [], stem_list)
        print('    %-20s struck : %d   stem : %d' % (rel, len(ch), len(sh)))
        if ch or sh:
            fails.append('G-STEM-APPENDED ' + rel)

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
        print('    %-58s %-34s exists=%s tracked=%s' % (what[:58], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote, the appended blocks and rows included):')
    tmpdir = tempfile.mkdtemp(prefix='b328_hedge_')
    targets = [('the bank', BANK), ('the registration', REG), ('the derive run', DER), ('the build run', BLD), ('the routes run', RTS),
               ('the family run', FAM), ('the filing', FIL)] + [('cell %s%g' % (k, a), p) for (k, a), p in zip(CELLS, CELL_RUNS)]
    for rel, mark in (('FACES_LEDGER.md', '<!-- b328 update -->'), ('OPEN_TRAILS.md', '<!-- b328 trail update -->')):
        txt = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        p = os.path.join(tmpdir, rel + '.block.txt')
        io.open(p, 'w', encoding='utf-8', newline='\n').write(txt[txt.index(mark):] if mark in txt else '')
        targets.append(('the block in ' + rel, p))
    p = os.path.join(tmpdir, 'rows.txt')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(rowtxt + '\n')
    targets.append(('rows 168-169', p))
    ib = idx[idx.index('# ### THE DISCRIMINATING FAMILY -- THE CONDITION AND THE SEEDS (b328).'):idx.index('# ### THE FACES LEDGER (b327).')] if '# ### THE DISCRIMINATING FAMILY -- THE CONDITION AND THE SEEDS (b328).' in idx else ''
    p = os.path.join(tmpdir, 'index.txt')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(ib)
    targets.append(('the index rows', p))
    for lbl, path in targets:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-28s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n, len(gh), len(ua)))
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
