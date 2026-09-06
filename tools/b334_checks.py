# -*- coding: utf-8 -*-
"""b334_checks.py -- THE GATE SUITE FOR THE AIM-MAP.

### ### **THE ARMS THAT CARRY THIS ACT (registration (H), F1-F12):**
###   `G-GRID` -- the aims and widths in the grid record equal the sealed section (D).
###   `G-SEED` -- every seed lawful and reported; every aim's phase, verdict and S_4 in the record; the condition number.
###   `G-LIKE` -- the like-for-like fixture raises; every leg record's rows carry the function's name.
###   `G-ROUTES` -- every quantity's two routes with their disagreement in the records; bars held or reported.
###   `G-GATE` -- every sign through the gate; no `?` unreported.
###   `G-REACH` -- the square's and the remainder's reach from measurements; NOT REACHED where the measurement says.
###   `G-IDENTITY` -- the residual printed at every covered aim.
###   `G-CHART` -- the block, the narrowest points, the crossing region, the softness correlation with its sign.
###   `G-EXPECT` -- the three expectations of each seat scored in words against printed values, in the bank.
###   `G-LEDGER` -- one block through the writer naming S1 (K5, K6), F7 and b328's block; rows byte-identical.
###   `G-ROW`, `G-KEY`, `G-CEILING`, `G-NOPROOF`, `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`,
###     the hedge audit, the stem sweep at extended scope, the must-fail fixtures -- standing.
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
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b334_the_aim_map.txt')
REG = d('b334_registration_2026-09-06.txt')
EXTRACT = d('b334_extract_notes.txt')
GRUN, GJ = d('b334_grid_run.txt'), d('b334_grid.json')
L40, L40J = d('b334_leg_reaching_40_run.txt'), d('b334_leg_reaching_40.json')
L81, L81J = d('b334_leg_reaching_81_run.txt'), d('b334_leg_reaching_81.json')
LCV, LCVJ = d('b334_leg_covered_run.txt'), d('b334_leg_covered.json')
CRUN, CJ = d('b334_chart_run.txt'), d('b334_chart.json')
FIL, FILR = d('b334_filings_run.txt'), d('b334_filings_rerun.txt')
CORR, CORRR = d('b334_corr_run.txt'), d('b334_corr_rerun.txt')
IDX, IDXR = d('b334_index_run.txt'), d('b334_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b334_ferry_scan.txt'), d('b334_reg_termscan.txt'), d('b334_reg_gate.txt')
CENSUS, FCEN = d('b334_census.txt'), d('b334_faces_census.txt')
REGSPEC, SATIS = d('b334_regspec_run.txt'), d('audit_b334_reg_satisfiable.txt')
PINS, INDEXQ = d('b334_pins_stepzero.txt'), d('audit_b334_index_query.txt')
HOOKS, MIRROR = d('b334_hooks.txt'), d('b334_mirror.txt')
SEAL = 'bc4418a48da6ebe9b83585e94eeb53f4efdffbf97093ed3dd88601d187222aed'
MARK_L = '<!-- b334 update -->'

OWNED = [BANK, REG, GRUN, GJ, L40, L40J, L81, L81J, LCV, LCVJ, CRUN, CJ, FIL, FILR, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         d('b334_satisfiable.json'), t('b334_extract.py'), t('b334_regspec.py'), t('b334_aimmap.py'), t('b334_filings.py'), t('b334_correspondence.py'),
         t('b334_index_append.py')]

CARRIERS = [
    (t('b334_checks.py'), 'its own fixtures'),
    (d('b334_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("b333 -- the corpus's A is the source's W_inf", d('b333_the_archimedean_term_derived.txt'), "**THE CORPUS'S `A(f)` IS THE SOURCE'S `W_inf(f) = -W_R(f)`**,"),
    ('### the aim-map named as next', d('b333_the_archimedean_term_derived.txt'), 'THE AIM-MAP IS NAMED AS NEXT, ITS TARGET THE NEW SOFTEST PAIR; NEITHER IT NOR THIS ACT IS THE DISCHARGE.'),
    ("### the atlas's sign line", t('e16/carto_atlas.py'), 'sum_gamma hhat(gamma)  =  hhat(i/2) + hhat(-i/2)  -  PRIME  +  ARCH'),
    ('### the places convention', t('b326_windows.py'), 'places_z=PRz1 - Az1, places_q=PRq - Aq1, places_q_b325=PRq - Aq325,'),
    ("b328 -- the even seed's construction", t('b328_family.py'), 'phi0 = _bump_on(V, a) * np.sin(GAMMA1 * np.abs(V))'),
    ('### the threshold', t('b328_family.py'), 'THRESHOLD_DEG = 45.0'),
    ('b328 bank -- negative past forty-five degrees', d('b328_the_discriminating_family.txt'), 'NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE**;'),
    ('### the phases at the registered widths', d('b328_the_discriminating_family.txt'), "the sine-aimed seed's phase at the zero is `88.10, 88.67, 89.21, 89.39` degrees at `a = 20, 40, 81,"),
    ('b326 -- the derived Epstein kernel', t('b326_windows.py'), '`2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)`'),
    ('### the certification', t('b326_windows.py'), 'certified = (verdict == NF.RESOLVED) and abs(value) > SIGN_MARGIN * drift'),
    ('b326 bank -- no crossing at this reach', d('b326_the_reach.txt'), 'CELLS.** ### **NO CROSSING AT THIS REACH.** ### The finite side rises to `0.453` at `a = 32`'),
    ('b321 -- the margin is minus the remainder', d('b321_the_window_opened.txt'), "that makes b320's margin exactly minus the remainder integral."),
    ('### the prime sum inside the margin, at the ladder', d('b321_the_window_opened.txt'), 'THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL OF THIS LADDER.**'),
    ('### one implementation of (84)', t('b321_window.py'), 'There is exactly one implementation of (84) in this corpus.'),
    ('### the eps evaluator', t('e16/b313f_qeps_layer.py'), 'def eps(rho, NQ=700, NG=400):'),
    ("b318 -- Theorem 1's support condition", t('b318_square.py'), 'SUPPORT_G_HI = math.sqrt(2.0)            # ### Theorem 1 / (3): supp g inside [2^-1/2, 2^1/2]'),
    ('b320 bank -- the sign certified, the size not', d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    ('b332 -- K5', t('b332_statement.py'), "('K5', 'the archimedean distribution',"),
    ('### K6', t('b332_statement.py'), "('K6', 'the decomposition: the compressed square plus the remainder',"),
    ('### the re-rank: the pair', d('b333_rerank_run.txt'), 'THE AIM-MAP IS NAMED AS NEXT; ITS TARGET IS THE NEW SOFTEST: K5 and K6.'),
    ('ledger -- row S1', LEDGER, '| S1 | S1 -- the clause stated:'),
    ('### row F7', LEDGER, "| F7 | F7 -- the Epstein negative control at b326's result"),
    ("### b328's update block", LEDGER, '<!-- b328 update -->'),
    ('the ferry -- (F1)', d('b334_ferry_2026-09-06.txt'), 'here: (F1) for \u03b6 the prime sum stays inside the margin at'),
    ('### (F3)', d('b334_ferry_2026-09-06.txt'), "contains its banked off-line zeros' aims; (F3) K5 and K6"),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) a passed test at this reach', BANK, 'FOR ZETA THE PRIME SUM STAYS INSIDE THE MARGIN AT EVERY AIM AT THIS REACH -- A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE.'),
    ('### F1 scored', BANK, "THE NAVIGATOR'S (F1): MET. THIS SEAT'S (F1): MET."),
    ('### (2) the narrowest points', BANK, 'THE NARROWEST POINTS OF THE ROOM ARE AT THE LOWEST HEIGHT, `gamma = 4`, AT BOTH REACHING WIDTHS:'),
    ('### (3) the crossing region', BANK, 'THE EPSTEIN CROSSING REGION -- THE NEGATIVE CONTROL CHARTED -- IS THREE AIMS:'),
    ('### F2 scored', BANK, "THE NAVIGATOR'S (F2): NOT MET. THIS SEAT'S (F2): NOT MET."),
    ('### (4) soften apart', BANK, 'K5 AND K6 DO NOT SOFTEN TOGETHER OVER AIMS: `Spearman(s5, s6) = -0.6158` OVER THE COVERED LEG.'),
    ('### F3 scored', BANK, "THE NAVIGATOR'S (F3): NOT MET. THIS SEAT'S (F3): NOT MET."),
    ('### (5) the square far from the identity', BANK, 'THE SQUARE ON THE STABLE CUT IS FAR FROM THE IDENTITY\'S VALUE AT THE AIMED SEEDS.'),
    ('### (6) the threshold rule', BANK, 'THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION, AND THE MAP SAYS SO.'),
    ('### a chart is not a proof', BANK, 'A CHART IS NOT A PROOF. ### THE QUANTIFIER K8 STAYS UNOWNED. ### NO GRADE: THE SOFTEST PAIR'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives component 1', BANK, 'COMPONENT 1 -- THE GRID.'),
    ('### the route bar exceeded as measured', BANK, 'THE TRANSFORM-ROUTE BAR OF `1e-10` RELATIVE IS EXCEEDED, AS'),
    ('bank gives component 2', BANK, 'COMPONENT 2 -- THE FOUR QUANTITIES, PER AIM, LIKE FOR LIKE BY NAME.'),
    ('### all bars held', BANK, 'ALL BARS HELD.'),
    ('### the A_z sign expectation', BANK, 'NEGATIVE AT EVERY REACHING AIM: NOT MET'),
    ('### not reached by measurement', BANK, 'THE SQUARE AND THE REMAINDER, ON THE REACHING LEG: NOT REACHED, BY MEASUREMENT.'),
    ('bank gives component 3', BANK, 'COMPONENT 3 -- THE CHART.'),
    ('### the ceiling', BANK, 'THE CEILING, PRINTED:'),
    ('bank gives component 4', BANK, 'COMPONENT 4 -- WHAT THE MAP SAYS AND DOES NOT.'),
    ('### not a proof', BANK, 'IT DOES NOT SAY A CHART IS A PROOF.'),
    ('bank gives the filings', BANK, 'THE FILINGS.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### E1', BANK, 'E1 -- THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION.'),
    ('### E3', BANK, 'E3 -- THE FIRST LAUNCH RAN THE FOUR MODES IN PARALLEL AND THE MACHINE KILLED THEM FOR MEMORY.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE ORDER: THE COST CENSUS -- A TYPED COST COLUMN ON THE FACES LEDGER, SORTED -- THEN THE WAVE DECISION WITH THE HOUSEKEEPING CLEARED.'),
    ('registration -- the grid', REG, 'NO AIM, NO WIDTH IS ADDED OR MOVED AFTER A NUMBER IS SEEN.'),
    ('registration -- the like-for-like rule', REG, 'comparison function raises on a name mismatch, and a fixture proves it raises.'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('chart run -- the finding', CRUN, 'aims REACHED by the sealed rule 270 ; of these with a NEGATIVE quadruple term (discriminating) 170 ; REACHED with a POSITIVE term (the phase past 135 deg) 100'),
    ('grid run -- the bar exceeded', GRUN, 'worst transform-route disagreement 1.14e-04 (bar 1e-10) ### EXCEEDED, AS MEASURED ###'),
]

MUST_FAIL = [
    ('the bank never says the chart is a proof', BANK, '### ### **THE CHART IS A PROOF.**'),
    ('the bank never says the quantifier is owned', BANK, '### ### **K8 IS OWNED.**'),
    ('the bank never says the clause moved', BANK, '### ### **THE CLAUSE HAS MOVED.**'),
    ('the bank never confers a grade', BANK, '### ### **A GRADE IS CONFERRED ON K5 AND K6.**'),
    ('the bank never says a size is certified', BANK, '### ### **THE SIZE OF THE MARGIN IS CERTIFIED.**'),
    ('the bank never says h2 moved', BANK, '### ### **h2 HAS MOVED.**'),
]

TOOLNUM = [
    ('56 seeds, 270/170/100 aims, the phases, 1.14e-04, the condition numbers', 'tools/b334_aimmap.py'),
    ('the four quantities, the bars, the gate, the residuals, the reach', 'tools/b334_aimmap.py'),
    ('the narrowest points, the crossing region, -0.6158, 0.8857, 3.604e-03', 'tools/b334_aimmap.py'),
    ('the ledger block', 'tools/b334_filings.py'),
    ('rows 180 and 181', 'tools/b334_correspondence.py'),
    ('the key', 'tools/b334_index_append.py'),
    ('24 clauses', 'tools/b334_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('21334 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b334_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the ledger writer', 'tools/b327_faces_row.py'),
    ("the seed's construction, lawfulness, the transform at the aim", 'tools/b328_family.py'),
    ('the channels, the gate', 'tools/b326_windows.py'),
    ('the square trace', 'tools/b318_square.py'),
    ('the remainder integral', 'tools/b321_window.py'),
    ('the (150) witness', 'tools/b333_diagnose.py'),
    ('the eps evaluator', 'tools/e16/b313f_qeps_layer.py'),
    ('0.11 at rank 69 (b321)', 'tools/b321_run.py'),
]
NEW_THIS_ACT = {'tools/b334_aimmap.py', 'tools/b334_filings.py', 'tools/b334_correspondence.py', 'tools/b334_index_append.py', 'tools/b334_regspec.py',
                'tools/b334_extract.py'}

GRID_BETAS = (0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 0.9532604747946607)
GRID_GAMMAS = (4.0, 8.0, 12.0, 14.134725, 16.290215720390393, 20.0, 25.0, 29.551761098629115, 33.650101, 40.0, 43.858664, 46.960994, 55.0, 61.687904)


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def main():
    fails = []
    print('=' * 100)
    print('b334 -- GATE SUITE (THE AIM-MAP: A COMPUTATION ON THE CERTIFIED INSTRUMENTS; A CHART, NOT A PROOF)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
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
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    G = json.load(io.open(GJ, encoding='utf-8'))
    legs = {40.0: json.load(io.open(L40J, encoding='utf-8')), 81.0: json.load(io.open(L81J, encoding='utf-8'))}
    C = json.load(io.open(LCVJ, encoding='utf-8'))
    CH = json.load(io.open(CJ, encoding='utf-8'))
    crun = io.open(CRUN, encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    fil = io.open(FIL, encoding='utf-8').read()

    print(chr(10) + '  G-GRID (F1: the aims and widths in the record equal the sealed section (D)):')
    gg = (tuple(G['betas']) == GRID_BETAS and tuple(G['gammas']) == GRID_GAMMAS and tuple(G['reaching']) == (40.0, 81.0) and tuple(G['covered']) == (1.3, 1.41)
          and len(G['seeds']) == 56 and all(r['gamma'] in GRID_GAMMAS and r['a'] in (40.0, 81.0, 1.3, 1.41) for r in G['seeds']))
    print('    %s' % gg)
    if not gg:
        fails.append('G-GRID')

    print(chr(10) + '  G-SEED (F2: lawfulness, phase, verdict, S_4 and the condition number at every seed and aim):')
    gs = all(r['lawful'] and r['cond'] > 0 and len(r['aims']) == 7 and all('phase_deg' in q and 'S4' in q and 'reached' in q for q in r['aims']) for r in G['seeds'])
    n_reached = sum(1 for r in G['seeds'] for q in r['aims'] if q['reached'])
    n_disc = sum(1 for r in G['seeds'] for q in r['aims'] if q['reached'] and q['S4'] < 0)
    gs = gs and n_reached == CH['aims_reached'] == 270 and n_disc == CH['aims_discriminating'] == 170 and CH['aims_reached_positive_term'] == 100
    print('    lawful and complete %s ; reached %d discriminating %d : %s' % (all(r['lawful'] for r in G['seeds']), n_reached, n_disc, gs))
    if not gs:
        fails.append('G-SEED')

    print(chr(10) + '  G-LIKE (F3: the like-for-like fixture raises; every row carries its function name; the fixture run in every mode):')
    import b334_aimmap as AM
    gl = AM.fixture_like() and G['fixtures']['like'] and all(r['name'].startswith('f = E conv E^# (gamma=') for L in legs.values() for r in L['rows']) \
        and all(r['name'].startswith('f = E conv E^# (gamma=') for r in C['rows'])
    print('    %s' % gl)
    if not gl:
        fails.append('G-LIKE')

    print(chr(10) + '  G-ROUTES (F4: two routes per quantity, the disagreement in the record; the bars held or reported):')
    worst = dict(tz=0.0, tq=0.0, wz=0.0, pz=0.0, lam=0.0, sq=0.0, rem=0.0)
    for L in list(legs.values()) + [C]:
        for r in L['rows']:
            worst['tz'] = max(worst['tz'], r['d_transform_z'])
            worst['tq'] = max(worst['tq'], r['d_transform_q'])
            worst['wz'] = max(worst['wz'], r['d_witness_z'])
            worst['pz'] = max(worst['pz'], r['d_prime'])
            worst['lam'] = max(worst['lam'], r['lamq_diff'])
            if 'd_square' in r:
                worst['sq'] = max(worst['sq'], r['d_square'])
                worst['rem'] = max(worst['rem'], r['d_remainder'])
    held = worst['tz'] <= AM.BAR_TRANSFORM and worst['tq'] <= AM.BAR_TRANSFORM and worst['wz'] <= AM.BAR_WITNESS and worst['pz'] <= AM.BAR_PRIME and worst['lam'] <= AM.BAR_LAMQ and worst['rem'] <= AM.BAR_REMAINDER
    gr = held and 'ALL BARS HELD.' in bank and G['worst_route'] > AM.BAR_ROUTE_G and 'EXCEEDED, AS MEASURED' in bank
    print('    worsts %s ; the leg bars held %s ; the grid route bar exceeded (%.2e > %.0e) and reported %s : %s' % ({k: '%.2e' % v for k, v in worst.items()}, held, G['worst_route'], AM.BAR_ROUTE_G, 'EXCEEDED, AS MEASURED' in bank, gr))
    if not gr:
        fails.append('G-ROUTES')

    print(chr(10) + '  G-GATE (F5: every sign through the gate, refine 1 against 4; none unresolved):')
    gates = [r['gate'][k] for L in list(legs.values()) + [C] for r in L['rows'] for k in ('places_z', 'places_q', 'arch_z', 'arch_q')]
    gq = all(g['verdict'] == 'RESOLVED' and g['certified'] for g in gates) and all(r['gate']['places_z']['sign'] == '-' for L in list(legs.values()) + [C] for r in L['rows'])
    print('    %d gate verdicts, all RESOLVED and certified %s ; every places_z negative %s : %s' % (len(gates), all(g['verdict'] == 'RESOLVED' for g in gates), all(r['gate']['places_z']['sign'] == '-' for L in list(legs.values()) + [C] for r in L['rows']), gq))
    if not gq:
        fails.append('G-GATE')

    print(chr(10) + "  G-REACH (F6: the square's and the remainder's reach from measurements):")
    er = legs[40.0]['eps_reach']
    gre = (sorted(er['outside_at']) == [1600.0, 6561.0] and er['values'][2] > 0 and er['values'][3] < 0 and all(r['square'] == 'NOT REACHED' and r['remainder'] == 'NOT REACHED' for L in legs.values() for r in L['rows'])
           and all(isinstance(r['square'], float) for r in C['rows']) and legs[40.0]['square_reach']['support'] > legs[40.0]['square_reach']['X'])
    print('    eps outside at %s ; the reaching leg NOT REACHED on both %s ; the covered leg reached : %s' % (er['outside_at'], all(r['square'] == 'NOT REACHED' for L in legs.values() for r in L['rows']), gre))
    if not gre:
        fails.append('G-REACH')

    print(chr(10) + '  G-IDENTITY (F7: the residual printed at every covered aim):')
    gi = all('residual' in r for r in C['rows']) and len(C['rows']) == 28 and crun.count('IDENTITY RESIDUAL') == 0 and io.open(LCV, encoding='utf-8').read().count('IDENTITY RESIDUAL') == 28
    print('    %s' % gi)
    if not gi:
        fails.append('G-IDENTITY')

    print(chr(10) + '  G-CHART (F8: the block, the narrowest points, the crossing region, the softness correlation with its sign):')
    gc = (len(CH['block']) == 56 and set(CH['narrowest'].keys()) >= {'reaching_40', 'reaching_81', 'covered_1.3', 'covered_1.41'} and len(CH['crossing']) == 3
          and abs(CH['spearman_s5_s6'] - (-0.6158)) < 5e-5 and '(F-a)' in crun and '(F-b)' in crun and '(F-c)' in crun and '(F-d)' in crun)
    print('    block %d ; crossing %d ; Spearman %+.4f : %s' % (len(CH['block']), len(CH['crossing']), CH['spearman_s5_s6'], gc))
    if not gc:
        fails.append('G-CHART')

    print(chr(10) + '  G-EXPECT (F9: the three expectations of each seat scored in words in the bank against the record):')
    nav, seat = CH['navigator'], CH['seat']
    ge = (nav == dict(F1='MET', F2='NOT MET', F3='NOT MET') and seat == nav
          and "THE NAVIGATOR'S (F1): MET. THIS SEAT'S (F1): MET." in bank and "THE NAVIGATOR'S (F2): NOT MET. THIS SEAT'S (F2): NOT MET." in bank
          and "THE NAVIGATOR'S (F3): NOT MET. THIS SEAT'S (F3): NOT MET." in bank)
    print('    record %s ; bank sentences present : %s' % (nav, ge))
    if not ge:
        fails.append('G-EXPECT')

    print(chr(10) + '  G-LEDGER (F10: one block through the writer naming S1 (K5, K6), F7 and b328; every existing row byte-identical; the writer append-only):')
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    blk = led[led.index(MARK_L):] if MARK_L in led else ''
    rows_w = [ln for ln in norm(led).split(chr(10)) if re.match(r'^\| [A-Z]\d+ \| ', ln)]
    rows_b = [ln for ln in norm(lb).split(chr(10)) if re.match(r'^\| [A-Z]\d+ \| ', ln)]
    gld = (led.count(MARK_L) == 1 and rows_w == rows_b and '**S1**, constituents **K5**' in blk and '**F7**' in blk and "b328\'s update" in blk.replace("'", "\\'") or False)
    gld = led.count(MARK_L) == 1 and rows_w == rows_b and '**S1**, constituents **K5**' in blk and '**F7**' in blk and 'b328' in blk and 'append-only working=True blob=True' in fil and 'A chart is not a proof' in blk
    print('    mark once %s ; rows identical %s (%d) ; names S1/F7/b328 %s ; writer append-only %s : %s' % (led.count(MARK_L) == 1, rows_w == rows_b, len(rows_w), '**S1**, constituents **K5**' in blk and '**F7**' in blk, 'append-only working=True blob=True' in fil, gld))
    if not gld:
        fails.append('G-LEDGER')

    print(chr(10) + '  G-ROW / G-ANCESTOR (rows 180 and 181: NO TERMINAL with the reason, M-2; the table a true prefix of its blob):')
    r180 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 180 |')]
    r181 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 181 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = (len(r180) == 1 and len(r181) == 1 and all('NO TERMINAL, AND THE REASON' in x[0] and 'M-2' in x[0] for x in (r180, r181))
           and 'A PASSED TEST OVER A GRID AT THIS REACH' in r180[0] and 'NEGATIVE CONTROL CHARTED' in r181[0] and norm(tbl).startswith(norm(head).rstrip(chr(10))))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOPROOF (one row; the must-not-hit queries NO KEY; the answer says a chart is not a proof):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('aim-map')
    gk = (o.count('act      :') == 1 and 'A CHART IS NOT A PROOF' in o and 'THE QUANTIFIER K8 STAYS UNOWNED' in o and 'A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE' in o)
    for s in ('the chart is a proof', 'the quantifier owned', 'the cost census'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOPROOF')

    print(chr(10) + '  G-CEILING (the ceiling printed in the chart run and the bank):')
    gce = 'THE CEILING, PRINTED.' in crun and ('`%.3e`' % CH['tail_bound']) in bank and '9877.782657' in bank and '61.687904' in bank
    print('    %s' % gce)
    if not gce:
        fails.append('G-CEILING')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (owner files, sealed files, the deposit, TECHNE, every .lean: no tracked change beyond the act\'s files):')
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/b327_faces_rows.py',
              'tools/ferry_scan.py', 'tools/reg_seal.py', 'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/b332_statement.py',
              'tools/b328_family.py', 'tools/b326_windows.py', 'tools/b326_closure.py', 'tools/b321_window.py', 'tools/b321_run.py', 'tools/b318_square.py', 'tools/b319_stable.py',
              'tools/b317_smear.py', 'tools/b316_instrument.py', 'tools/b320_weil.py', 'tools/b320_corroborate.py', 'tools/b333_diagnose.py', 'tools/e16/carto_atlas.py',
              'tools/e16/b313f_qeps_layer.py', 'tools/noise_floor.py', 'data/carto_atlas.jsonl', 'data/b326_epstein_zeros.json', 'data/b326_offline.json',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b333_the_archimedean_term_derived.txt', 'data/b328_the_discriminating_family.txt',
              'data/b326_the_reach.txt', 'data/b321_the_window_opened.txt', 'data/b320_the_lawful_function.txt', 'data/b332_registration_2026-09-06.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FACES_LEDGER.md')]
    st_t = git(TC, 'status', '--porcelain').strip().replace('?? modules/2026-08/', '').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    fnd_same = git(PP, 'status', '--porcelain', 'FINDINGS.md').strip() == ''
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep and fnd_same
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the ledger) %s ; TECHNE %r ; deposit %r ; FINDINGS untouched %s : %s' % (st_r, st_s, st_p, st_t, dep, fnd_same, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the tool, the runs, the filings and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b334_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b334_aimmap.py'), GRUN, L40, L81, LCV, CRUN, FIL, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b334_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b334_checks_run.txt')) else ''
        after = 'the tool, the runs, the filings and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the tool, the runs, the filings and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    committed_l = MARK_L in lb
    if committed_l:
        print('    the ledger committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    the ledger not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    r40 = {r['gamma']: r for r in legs[40.0]['rows']}
    r81 = {r['gamma']: r for r in legs[81.0]['rows']}
    checks.append(('room at 40, gamma 4', ('`A_z - PR_z = %+.9f`' % r40[4.0]['room_z']) in bank))
    checks.append(('room at 81, gamma 4', ('`%+.9f` at `a = 81`' % r81[4.0]['room_z']) in bank))
    checks.append(('A_z, PR_z at 40, gamma 4', ('`A_z = %+.9f`' % r40[4.0]['arch_z']) in bank and ('`PR_z = %+.9f`' % r40[4.0]['prime_z']) in bank))
    for (lg, a, gm, p) in CH['crossing']:
        checks.append(('crossing a=%g gamma=%.6f' % (a, gm), ('`%+.6f`' % p) in bank or ('places_q = %+.6f`' % p) in bank))
    checks.append(('Epstein room at 29.55, both widths', ('`%+.9f` at `a = 40`' % r40[29.551761098629115]['room_q']) in bank and ('`%+.9f` at `a = 81`' % r81[29.551761098629115]['room_q']) in bank))
    checks.append(('Spearman', ('`Spearman(s5, s6) = %+.4f`' % CH['spearman_s5_s6']) in bank))
    oa = CH['order_agree']
    checks.append(('order agreement range', ('`%.4f` to `%.4f`' % (min(oa.values()), max(oa.values()))) in bank))
    res = [r['residual'] for r in C['rows']]
    checks.append(('residual range', ('`%.3f` to' % min(res)) in bank and ('`%.3f`' % max(res)) in bank))
    s5c = [r['s5'] for r in C['rows']]
    checks.append(('s5 range', ('`%.1e`' % min(s5c)) in bank and ('`%.1e`' % max(s5c)) in bank))
    for a, key in ((1.3, '1.568e+04'), (1.41, '9.144e+03'), (40.0, '8.039e+01'), (81.0, '5.700e+01')):
        cond = [r['cond'] for r in G['seeds'] if r['a'] == a][0]
        checks.append(('cond at %g' % a, ('%.3e' % cond) == key and ('`%s`' % key) in bank))
    checks.append(('worst route', ('`%.2e`' % G['worst_route']) in bank))
    checks.append(('transform worsts', all(('`%.3e`' % max(r['d_transform_z'] for r in L['rows'])) in bank for L in (legs[40.0], legs[81.0], C))))
    checks.append(('witness worsts', all(('`%.3e`' % max(r['d_witness_z'] for r in L['rows'])) in bank for L in (legs[40.0], legs[81.0], C))))
    checks.append(('square drift worst', ('`%.3e`' % max(r['d_square'] for r in C['rows'])) in bank))
    checks.append(('remainder worst', ('`%.3e`' % max(r['d_remainder'] for r in C['rows'])) in bank))
    checks.append(('Lambda_Q', ('`%.1e`' % legs[40.0]['lamq_diff']) in bank and ('`%.1e`' % legs[81.0]['lamq_diff']) in bank))
    ev = legs[40.0]['eps_reach']['values']
    checks.append(('eps values', all(('%+.6e' % v) in bank for v in ev[2:])))
    checks.append(('tail bound', ('`%.3e`' % CH['tail_bound']) in bank))
    checks.append(('aims 270/170/100', CH['aims_reached'] == 270 and CH['aims_discriminating'] == 170 and CH['aims_reached_positive_term'] == 100 and '270 of 392' in bank))
    nseeds = len(G['seeds'])
    checks.append(('%d seeds' % nseeds, nseeds == 56 and '56 seeds' in bank))
    rn = re.search(r'rows to append : (\d+) and (\d+)', io.open(CORR, encoding='utf-8').read())
    checks.append(('rows %s and %s' % rn.groups(), ('rows %s and %s' % rn.groups()) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    cov_min = min(r['room_margin'] for r in C['rows'])
    checks.append(('covered room minimum', ('`%+.2f`' % cov_min) in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded; no numbered repeat of a leg):')
    once_ok = all(os.path.exists(p) for p in [GRUN, GJ, L40, L40J, L81, L81J, LCV, LCVJ, CRUN, CJ, FIL, FILR, CORR, CORRR, IDX, IDXR]) \
        and not any(os.path.exists(d(n)) for n in ('b334_grid_run2.txt', 'b334_leg_reaching_40_run2.txt', 'b334_leg_reaching_81_run2.txt', 'b334_leg_covered_run2.txt', 'b334_chart_run2.txt'))
    print('    %s' % once_ok)
    if not once_ok:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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

    print(chr(10) + '  G-STEM-APPENDED (extended scope: the ledger block, rows 180 and 181, the index row, swept):')
    ib = idx[idx.index('# ### THE AIM-MAP (b334).'):idx.index('# ### THE ARCHIMEDEAN TERM DERIVED (b333).')] if '# ### THE AIM-MAP (b334).' in idx else ''
    for lbl, blk2 in (('the ledger block', blk), ('row 180', r180[0] if r180 else ''), ('row 181', r181[0] if r181 else ''), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-64s %-34s exists=%s tracked=%s' % (what[:64], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the ledger block, the rows and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b334_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('the ledger block', blk), ('row 180', r180[0] if r180 else ''), ('row 181', r181[0] if r181 else ''), ('the index row', ib)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, gh, ua = hedge_audit.audit(path)
        print('    %-36s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(gh), len(ua)))
        for s2 in gh:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
