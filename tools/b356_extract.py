# -*- coding: utf-8 -*-
"""b356_extract.py -- EXTRACT-TO-DISK, AND THE RAISED AXIS SIZED, BEFORE THE SEAL.

### ### **EVERY ANCHOR IS BUILT BY READING ITS LINE** (`tools/anchor_from_file.py`, the sortie's step zero).
### ### **AND IT READS THE ONE THING THAT MAKES THIS ACT'S CONTROL BAR DEFENSIBLE:** ### `b344` moved the
### QUADRATURE AXIS itself, at a fixed frame, and printed the trace at every rung of it. ### That is the only
### measurement of this axis the record holds, and the control bar's floor comes from it rather than from a
### number this seat picks.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- leg 1, with three additions', 'ORDER', d('b356_ferry_2026-09-07.txt'),
     'LEG 1 (b356) - THE OBJECT OR THE BOUNDARY, as drafted, with'),
    ('the order -- it cannot price its own frame from the record', 'ORDER', d('b356_ferry_2026-09-07.txt'),
     'that this act cannot price its own frame from the record,'),
    ('the order -- raising the quadrature axis is re-tuning', 'ORDER', d('b356_ferry_2026-09-07.txt'),
     'licenses comparison only against b354'),
    ('the order -- the fifth rung recomputed as a control', 'ORDER', d('b356_ferry_2026-09-07.txt'),
     'the fifth rung is recomputed under the raised axis as a'),
    ('the order -- the verdict set, fixed', 'ORDER', d('b356_ferry_2026-09-07.txt'),
     '(iii) The verdict set is fixed here:'),
    ('the order -- the seal chained on the audit exit code', 'ORDER', d('b356_ferry_2026-09-07.txt'),
     "chained on the AUDIT's exit code (b354's incident, now"),

    # ---- WHAT b354 LEFT ----------------------------------------------------------------------------
    ('b354 -- the residual negative at every covered cell', 'b354', d('b354_the_sixth_frame.txt'),
     'THE SIXTH RUNG LANDED, AND ITS RESIDUAL IS NEGATIVE AT EVERY COVERED CELL'),
    ('b354 -- the rank saturated at the quadrature bound', 'b354', d('b354_the_sixth_frame.txt'),
     'THE OBSERVED RANK IS `512`. ### THAT IS `NY` EXACTLY'),
    ('b354 -- the two arrive together and are not separated', 'b354', d('b354_the_sixth_frame.txt'),
     'SO THE TWO THINGS HAPPEN AT THE SAME RUNG, AND THIS ACT CANNOT SEPARATE THEM'),
    ('b354 -- what the next act would have to settle first', 'b354', d('b354_the_sixth_frame.txt'),
     'WHAT THE NEXT ACT WOULD HAVE TO SETTLE FIRST, NAMED AND NOT PRICED'),
    ('b354 -- the measured wall, the first this ladder has', 'b354', d('b354_the_sixth_frame.txt'),
     'IS THE FIRST MEASURED WALL THIS LADDER HAS'),
    ('b354 -- the criterion undefined, tabled not edited', 'b354', d('b354_the_sixth_frame.txt'),
     'THE CRITERION IS TABLED, NOT EDITED, AND THE TEMPTATION IS WORTH NAMING'),
    ('b354 -- the seal taken against a refusal', 'b354', d('b354_the_sixth_frame.txt'),
     'A FIRST VERSION OF THIS REGISTRATION WAS SEALED AGAINST AN EXPLICIT REFUSAL'),

    # ---- THE ONE MEASUREMENT OF THIS AXIS THE RECORD HOLDS ------------------------------------------
    ('b344 -- the axis it moved, and why that one', 'AXIS', d('b344_registration_2026-09-06.txt'),
     "WHY `NY` AND NOT THE CUT'S `tau`"),
    ('b344 -- the rank does not move at all along that axis', 'AXIS', d('b344_the_floor_priced.txt'),
     'AND THE RANK DOES NOT MOVE AT ALL'),
    ('b344 -- the effective rank is intrinsic across four doublings', 'AXIS', d('b344_the_floor_priced.txt'),
     "The constraint's effective rank is intrinsic across four doublings of the rows that sample it"),
    ('b344 -- the residual converges along it', 'AXIS', d('b344_the_floor_priced.txt'),
     'THE REMAINING TRAVEL IS'),
    ('b316 -- why the quadrature grid is independent of the domain', 'AXIS', t('b316_instrument.py'),
     'THE TRANSFORM GETS ITS OWN GRID, AND THAT IS NOT A CONVENIENCE'),
    ('b316 -- what tying them together did', 'AXIS', t('b316_instrument.py'),
     'AS THE DOMAIN LENGTHENS, AND AT `X = 64` IT WAS WEAK ENOUGH TO ADMIT A VECTOR b292'),
    ('b316 -- the transform matrix is NY by N', 'AXIS', t('b316_instrument.py'),
     'return 2.0 * np.cos(2.0 * math.pi * np.outer(self.y, self.x)) * self.w'),
    ('the stable cut, from one decomposition', 'AXIS', t('b319_stable.py'),
     'BOTH CUTS FROM ONE SVD'),
    ("b320 -- the frames table with each frame's rank", 'AXIS', d('b320_components_run.txt'),
     "(2a) THE FRAMES, ON b319's STABLE CUT, WITH THE RANK PRINTED."),

    # ---- THE STANDING RULES -------------------------------------------------------------------------
    ('b322 -- a price is not a prediction', 'RULE', d('b322_the_membership.txt'),
     'A PRICE IS NOT A PREDICTION.'),
    ('b355 -- unaffordable is about a question', 'RULE', d('b355_sortie_closing.txt'),
     'UNAFFORDABLE_IS_ABOUT_A_QUESTION.md`'),
    ('b345 -- a stopped run is banked as it stood', 'RULE', d('b345_the_li_control_rerun.txt'),
     'STOPPED'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b356 -- EXTRACT-TO-DISK, AND THE RAISED AXIS SIZED BEFORE THE SEAL.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b356_extract_notes', LINES)
        return 2

    # ============================================== THE AXIS, MEASURED FROM b344's OWN LADDER.
    rec('')
    rec('  ### ### **THE ONE MEASUREMENT OF THE QUADRATURE AXIS THE RECORD HOLDS**, read from')
    rec('  ### ### `data/b344_ny.json` and not from prose:')
    B = json.load(io.open(d('b344_ny.json'), encoding='utf-8'))
    rec('    b344 moved the axis at a FIXED frame N=%s X=%s, cell a=%s' % (B['N'], B['X'], B['cell']))
    rec('    %-8s %-8s %-22s %s' % ('NY', 'rank', 'Tr', 'relative move from the previous rung'))
    prev = None
    ny_rows = []
    for r in B['rows']:
        rel = None if prev is None else abs(r['Tr'] - prev) / abs(prev)
        ny_rows.append(dict(NY=r['NY'], rank=r['rank'], Tr=r['Tr'], rel=rel))
        rec('    %-8d %-8d %-22.15f %s' % (r['NY'], r['rank'], r['Tr'], ('--' if rel is None else '%.3e' % rel)))
        prev = r['Tr']
    by = {r['NY']: r for r in B['rows']}
    step = abs(by[1024]['Tr'] - by[512]['Tr']) / abs(by[512]['Tr'])
    ranks_const = len(set(r['rank'] for r in B['rows'])) == 1
    rec('    ### ### **THE STEP THAT MATTERS: `NY = 512` TO `NY = 1024` MOVES THE TRACE BY `%.3e` RELATIVE.**'
        % step)
    rec('    ### ### **AND THE RANK IS CONSTANT AT `%d` ACROSS THE WHOLE AXIS** : %s'
        % (B['rows'][0]['rank'], ranks_const))
    rec('    ### ### **SO AT A RUNG WHERE THE BOUND IS NOT BINDING, RAISING THE AXIS LEAVES THE RANK ALONE')
    rec('    ### ### AND MOVES THE TRACE BY ABOUT ONE PART IN TEN THOUSAND.** ### That is the floor this')
    rec('    ### ### act\'s control bar is stated against, and it is a MEASURED figure of THIS axis, from')
    rec('    ### ### the only act that moved it.')
    rec('    ### **AND WHAT IT IS NOT:** ### b344 measured it at `N = 4096, X = 32` with rank `69` against a')
    rec('    ### bound of `512` -- ### **FAR FROM THE BOUND.** ### The fifth rung sits at rank `262` against')
    rec('    ### the same `512`, which is closer, and ### **NOTHING HERE SAYS THE RANK IS CONVERGED THERE.**')
    rec('    ### **THAT IS EXACTLY WHAT THIS ACT\'S CONTROL TESTS.**')

    # ============================================== THE RAISED AXIS, AND THE SHAPE OF ITS COST.
    rec('')
    rec('  ### ### **THE RAISED AXIS, CHOSEN, AND THE SHAPE OF WHAT IT COSTS.**')
    import b316_instrument as INS
    import b317_smear as SM
    RAISED = 1024
    sizes = []
    for N, X, ny in ((32768, 256.0, SM.NY_FIXED), (32768, 256.0, RAISED)):
        fr = INS.Frame(N, X, ny)
        lo_x, lo_y = fr.masks()
        free = int((~lo_x).sum())
        rowsn = int(lo_y.sum())
        sizes.append(dict(N=N, X=X, NY=ny, rows=rowsn, free=free, C_bytes=rowsn * free * 8))
        rec('    N=%-6d X=%-6.1f NY=%-5d  C is %d x %d = %.1f MB' % (N, X, ny, rowsn, free, rowsn * free * 8 / 1e6))
    rec('    ### **THE RAISED VALUE IS `%d`, AND IT IS NOT AN INVENTED NUMBER:** ### it is a rung of b344\'s'
        % RAISED)
    rec('    ### own ladder, already run by that act at a different frame.')
    rec('    ### **THE HEADROOM:** ### b354 measured the sixth rung\'s rank at `512` against a bound of')
    rec('    ### `512`, with the banked ranks extrapolating to about `516`. ### At `%d` the bound is about'
        % RAISED)
    rec('    ### twice that estimate. ### **AN ESTIMATE IS NOT A GUARANTEE, AND THE THIRD VERDICT EXISTS')
    rec('    ### ### FOR THE CASE WHERE THE RAISE DOES NOT CLEAR IT.**')
    rec('    ### **THE COST\'S SHAPE:** ### the decomposition is `O(NY^2 * free)`, so doubling the axis is')
    rec('    ### about FOUR TIMES the decomposition -- b354 measured `8.1` s for it. ### **WHAT THE CELLS')
    rec('    ### ### COST IS NOT A SHAPE THIS SEAT CAN READ:** b354 measured about `52` s per cell at rank')
    rec('    ### `512`, and how that scales with a larger rank is ### **NOT IN THE RECORD.**')
    rec('    ### ### **SO THIS ACT CANNOT PRICE ITS OWN FRAME FROM THE RECORD, AND ITS CEILING IS CHOSEN.**')

    # ============================================== THE READS.
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % e)
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.relpath(path, ROOT).replace(os.sep, '/'),
                          line=n, differs=bool(differs)))
        rec('')
        rec('  [%-5s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.relpath(path, ROOT).replace(os.sep, '/'), n, differs))
        rec('      | %s' % line.rstrip())
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('=' * 100)
    p = run_clock.write(D, 'b356_extract_notes', LINES)
    io.open(d('b356_axis.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(ny_ladder=ny_rows, step_512_to_1024=step, ranks_constant=bool(ranks_const),
             b344_frame=dict(N=B['N'], X=B['X'], cell=B['cell'], rank=B['rows'][0]['rank']),
             raised=RAISED, sizes=sizes, reads=len(READS), without_anchor=bad, anchors_differing=ndiff,
             built=built, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
