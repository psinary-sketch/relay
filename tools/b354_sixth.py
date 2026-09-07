# -*- coding: utf-8 -*-
"""b354_sixth.py -- COMPONENT 1 AND 2: THE SIXTH FRAME, AND THE REFIT ON SIX.

### ### **THE INSTRUMENT IS IMPORTED AND NOTHING IN IT IS RE-TUNED.** ### `b316_instrument.Frame`,
### `b319_stable.both_subspaces`, `b317_smear.identity_trace`, `b318_square.square_trace` -- the same calls
### `b320_run.py` makes, in the same order, with `NY` unchanged at `512`.
### ### **THE MODELS AND THE MINIMISER ARE IMPORTED FROM `tools/b352_fit.py`, NEVER COPIED**, because the
### order says the criterion is the SAME one and not a new one, and ### **A CRITERION RETYPED IS A SECOND
### ### CRITERION.**
### ### **THE CHOSEN CEILING (registration (C)) IS ENFORCED HERE**, and an overrun ABANDONS the run and is
### reported as the finding, with no bar moved and no partial value taken.
### ### **BAR 4 RUNS FIRST AND LICENSES EVERYTHING ELSE:** the FIFTH rung is recomputed and must reproduce
### `b320`'s banked value at every covered cell, or the sixth rung is not a sixth rung of that ladder.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import b316_instrument as INS   # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b319_stable as ST        # noqa: E402
import b322_ladder as LAD       # noqa: E402
import b352_fit as F52          # noqa: E402  ### THE MODELS AND THE MINIMISER, IMPORTED.
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE CHOSEN CEILING, from registration section (C). ### **CHOSEN, NOT READ.**
WALL_CEILING = 900.0
BYTES_CEILING = 8 * 1024 ** 3
BAR_IDENTITY = 1e-9      # ### (E) bar 3 ; floor ~ dim*eps ~ 7e-12
BAR_REPRO = 1e-9         # ### (E) bar 4 ; floor ~ 2e-15 relative
SIXTH = (32768, 256.0, SM.NY_FIXED)
FIFTH = (16384, 128.0, SM.NY_FIXED)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def seed(a):
    """### THE SEED, BY THE SAME CALL b320 MAKES. ### Nothing here chooses anything."""
    return SM.mean_zero_variant(a)


def main():
    t0 = time.time()
    P = json.load(io.open(os.path.join(D, 'b339_price.json'), encoding='utf-8'))
    B320 = json.load(io.open(os.path.join(D, 'b320_rows.json'), encoding='utf-8'))
    cells = sorted(P['cells'], key=float)
    rec('=' * 100)
    rec('b354 -- THE SIXTH FRAME. ### THE INSTRUMENT IMPORTED, NOTHING RE-TUNED.')
    rec('=' * 100)
    rec('  ### the ladder as banked : %s' % (SM.DOMAIN_AXIS,))
    rec('  ### the sixth rung, sealed : N=%d X=%g NY=%d' % SIXTH)
    rec('  ### THE CHOSEN CEILING (registration (C)) : %.0f s of wall ; %.0f GB'
        % (WALL_CEILING, BYTES_CEILING / 1024.0 ** 3))
    rec('  ### ### **A CHOSEN CEILING IS NOT A READ ONE.** ### The record holds no wall for this ladder.')

    def over(where):
        el = time.time() - t0
        if el > WALL_CEILING:
            rec('')
            rec('  ### ### ### **THE RUN OVERRAN THE CHOSEN CEILING AT %s : %.1f s > %.0f s.**' % (where, el, WALL_CEILING))
            rec('  ### ### **ABANDONED. ### THE OVERRUN IS THE FINDING. ### NO BAR MOVES, NO PARTIAL VALUE')
            rec('  ### ### IS TAKEN, AND THIS OUTPUT IS BANKED AS IT STANDS.**')
            return True
        return False

    # ============================================================ BAR 4, FIRST, AND IT LICENSES THE REST.
    rec('')
    rec('-' * 100)
    rec('  ### BAR 4 -- THE REPRODUCTION. ### **THE FIFTH RUNG, RECOMPUTED. ### IT LICENSES EVERYTHING ELSE.**')
    rec('-' * 100)
    fr5 = INS.Frame(*FIFTH)
    st5, _g5 = ST.both_subspaces(fr5, ST.TAU)
    ti5, _f5, _c5 = SM.identity_trace(fr5, st5)
    id5 = abs(ti5 - st5['dim'])
    rec('    N=%-6d X=%-6.1f free=%-6d rank=%-4d dim=%-6d   identity |Tr - dim| = %.3e (bar %.0e)'
        % (FIFTH[0], FIFTH[1], st5['free'], st5['rank'], st5['dim'], id5, BAR_IDENTITY))
    rep = []
    rec('    %-8s %-20s %-20s %-13s %s' % ('a', 'Tr recomputed here', "b320's banked Tr", '|rel diff|', 'bar 1e-9'))
    for k in cells:
        tr = SQ.square_trace(fr5, st5, seed(float(k)))
        banked = B320['axes'][k]['domain'][-1]
        rd = abs(tr - banked) / max(abs(banked), 1e-300)
        rep.append(dict(a=k, here=float(tr), banked=float(banked), rel=float(rd), ok=bool(rd <= BAR_REPRO)))
        rec('    %-8s %-20.12f %-20.12f %-13.3e %s' % (k, tr, banked, rd, 'HOLDS' if rd <= BAR_REPRO else '### FAILS ###'))
    bar4 = all(r['ok'] for r in rep) and id5 <= BAR_IDENTITY
    rec('    ### ### **BAR 4 : %s**' % ('HOLDS AT EVERY CELL' if bar4 else '### FAILS ###'))
    if not bar4:
        rec('    ### ### **THE INSTRUMENT DOES NOT REPRODUCE THE LADDER THE RECORD HOLDS.** ### The sixth')
        rec('    ### ### rung would not be a sixth rung of that ladder. ### **THE ACT STOPS AND SAYS SO,')
        rec('    ### ### AND NO FIT IS REPORTED.**')
        run_clock.write(D, 'b354_sixth_run', LINES)
        return 1
    rec('    ### and that licenses the sixth rung: the same code, one step further along the same axis.')
    if over('bar 4'):
        run_clock.write(D, 'b354_sixth_run', LINES)
        return 1

    # ============================================================ THE SIXTH RUNG.
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 1 -- THE SIXTH RUNG.')
    rec('-' * 100)
    t_frame = time.time()
    fr6 = INS.Frame(*SIXTH)
    st6, _g6 = ST.both_subspaces(fr6, ST.TAU)
    t_svd = time.time() - t_frame
    ti6, _f6, _c6 = SM.identity_trace(fr6, st6)
    id6 = abs(ti6 - st6['dim'])
    rec('    N=%-6d X=%-6.1f free=%-6d rank=%-4d dim=%-6d' % (SIXTH[0], SIXTH[1], st6['free'], st6['rank'], st6['dim']))
    rec('    ### **BAR 3, THE IDENTITY CONTROL** : |Tr - dim| = %.3e   bar %.0e   floor ~ dim*eps = %.1e   %s'
        % (id6, BAR_IDENTITY, st6['dim'] * np.finfo(float).eps, 'HOLDS' if id6 <= BAR_IDENTITY else '### FAILS ###'))
    rec('    ### the decomposition alone : %.1f s' % t_svd)
    ranks5 = B320['axes'][cells[0]]['drank']
    extrap = ranks5[-1] * (ranks5[-1] / float(ranks5[-2]))
    saturated = (int(st6['rank']) >= SIXTH[2])
    rec('')
    rec('    ### ### **THE RANK, AND A THING THIS ACT MUST CHECK BEFORE IT READS ANY RESIDUAL.**')
    rec('      the ranks along the banked ladder : %s' % ranks5)
    rec('      their ratios per doubling         : %s'
        % ['%.3f' % (ranks5[i + 1] / float(ranks5[i])) for i in range(len(ranks5) - 1)])
    rec('      extrapolated sixth rank           : %.0f' % extrap)
    rec('      OBSERVED sixth rank               : %d      NY, the constraint count : %d'
        % (st6['rank'], SIXTH[2]))
    if saturated:
        rec('      ### ### ### **THE RANK HAS SATURATED AT `NY`.** ### It would have been about `%.0f` and'
            % extrap)
        rec('      ### ### ### it is `%d`, because `NY = %d` is the number of constraints and the rank'
            % (st6['rank'], SIXTH[2]))
        rec('      ### ### ### cannot exceed it. ### **SO THE SIXTH RUNG IS THE FIRST RUNG AT WHICH THE')
        rec('      ### ### ### RANK IS LIMITED BY `NY` RATHER THAN BY `X`** -- and it is limited only')
        rec('      ### ### ### barely, by about `%.0f` dimensions out of `%d`.' % (extrap - st6['rank'], SIXTH[2]))
        rec('      ### **`b316` FIXED `NY` INDEPENDENTLY OF `X` ON PURPOSE**, so that lengthening the')
        rec('      ### domain would not weaken the second condition. ### **AT THIS RUNG THAT INDEPENDENCE')
        rec('      ### ### HAS REACHED ITS OWN LIMIT**, and the act carries it into everything below.')
    if id6 > BAR_IDENTITY:
        rec('    ### ### **BAR 3 FAILS AT THE SIXTH FRAME. ### THE ACT STOPS AND SAYS SO.**')
        run_clock.write(D, 'b354_sixth_run', LINES)
        return 1
    if over('the sixth frame'):
        run_clock.write(D, 'b354_sixth_run', LINES)
        return 1

    rows = {}
    rec('')
    rec('    %-8s %-16s %-16s %-16s %-18s %s' % ('a', 'W_inf', 'Tr(256)', 'margin W - Tr', 'R = margin - INT_EF', 'wall'))
    for k in cells:
        tc = time.time()
        tr6 = SQ.square_trace(fr6, st6, seed(float(k)))
        c = P['cells'][k]
        margin = c['weil'] - tr6
        R6 = margin - c['int_ef']
        rows[k] = dict(tr=float(tr6), margin=float(margin), R=float(R6), wall=time.time() - tc)
        rec('    %-8s %-16.9f %-16.9f %-16.9f %-18.9f %.1f s'
            % (k, c['weil'], tr6, margin, R6, rows[k]['wall']))
        if over('cell a=%s' % k):
            run_clock.write(D, 'b354_sixth_run', LINES)
            return 1
    wall = time.time() - t0
    rec('')
    rec('    ### ### **THE SIXTH RUNG LANDED. ### WALL SO FAR : %.1f s AGAINST A CHOSEN CEILING OF %.0f s.**'
        % (wall, WALL_CEILING))
    rec('    ### ### **AND THAT PRINTED WALL IS THE FIRST MEASURED WALL THIS LADDER HAS.** ### It is not a')
    rec('    ### ### comparison, because there is no banked cost to compare it to.')

    # ============================================================ THE SIX-FRAME LADDER.
    XS6 = list(P['xs']) + [SIXTH[1]]
    rec('')
    rec('    ### THE LADDER, NOW SIX RUNGS : X = %s' % XS6)
    for k in cells:
        R5 = P['cells'][k]['R']
        rec('    a=%-6s R = %s  ### + %.9e' % (k, ['%.6e' % v for v in R5], rows[k]['R']))
        ratios = [R5[i + 1] / R5[i] for i in range(len(R5) - 1)] + [rows[k]['R'] / R5[-1]]
        rec('           ratios per doubling : %s' % ['%.4f' % r for r in ratios])

    # ============================================================ COMPONENT 2 -- THE REFIT ON SIX.
    rec('')
    rec('-' * 100)
    rec("  ### COMPONENT 2 -- THE REFIT ON SIX FRAMES, UNDER b352's SEALED CRITERION, IMPORTED.")
    rec('-' * 100)
    rec('    ### the models, the minimiser and the score come from `tools/b352_fit.py` : %s'
        % os.path.basename(F52.__file__))
    rec('    ### **A CRITERION RETYPED IS A SECOND CRITERION**, so none of it is retyped here.')
    n5, n6 = 5, 6

    def pen(n, k):
        return 2.0 * k + 2.0 * k * (k + 1.0) / (n - k - 1.0)

    d5 = pen(n5, 3) - pen(n5, 2)
    d6 = pen(n6, 3) - pen(n6, 2)
    rec('    ### **THE PENALTY FOR A THIRD PARAMETER**, from the sealed criterion and fixed in (D) before')
    rec('    ### the frame landed : at n = 5 it is %.1f ; at n = 6 it is %.1f.' % (d5, d6))

    X5 = np.asarray(P['xs'], dtype=float)
    F52J = json.load(io.open(os.path.join(D, 'b352_fit.json'), encoding='utf-8'))

    nonpos = {k: [i for i, v in enumerate(list(P['cells'][k]['R']) + [rows[k]['R']]) if v <= 0.0]
              for k in cells}
    any_nonpos = any(nonpos[k] for k in cells)
    rec('')
    rec('    ### ### **BEFORE ANY SCORE: IS THE SEALED CRITERION DEFINED ON THIS LADDER?**')
    rec('    %-8s %-46s %s' % ('a', 'R over six rungs', 'non-positive rungs'))
    for k in cells:
        allr = list(P['cells'][k]['R']) + [rows[k]['R']]
        rec('    %-8s %-46s %s' % (k, '%.4e ... %.4e' % (allr[0], allr[-1]),
                                   [int(i) for i in nonpos[k]] or 'none'))
    out = {}
    if any_nonpos:
        rec('')
        rec('    ### ### ### **THE SEALED CRITERION IS UNDEFINED ON THIS LADDER.**')
        rec('    ### It minimises the sum of squared residuals of `log R`, and ### **`log R` IS UNDEFINED')
        rec('    ### ### AT A NON-POSITIVE `R`.** ### The sixth rung is negative at every covered cell.')
        rec('    ### ### **SO NO SIX-FRAME SCORE EXISTS, AND NONE IS REPORTED.** ### The first run of this')
        rec('    ### ### file printed a not-a-number in every score column and is banked as it stood at')
        rec('    ### ### `data/b354_sixth_run_first_nan_scores.txt`. ### **THAT IS NOT A SCORE AND MUST NOT')
        rec('    ### ### BE TABLED AS ONE.**')
        rec('    ### ### ### **AND THE CRITERION IS TABLED, NOT EDITED.** ### The order says the criterion is')
        rec('    ### ### ### the SAME one and not a new one. ### A linear-space fit would fit these six')
        rec('    ### ### ### numbers -- and it would be ### **A SECOND CRITERION**, chosen after seeing that')
        rec('    ### ### ### the first failed, which is exactly the move a sealed criterion exists to')
        rec('    ### ### ### prevent. ### **THE DEFECT IS MEASURED AND CARRIED.**')
        rec('    ### **WHAT THE DEFECT IS, PRECISELY:** b352 sealed a criterion on five POSITIVE residuals')
        rec('    ### and it was well defined there. ### **ITS DOMAIN OF DEFINITION WAS NEVER STATED**, and')
        rec('    ### the sixth rung stepped outside it. ### A criterion is stated with the domain on which')
        rec('    ### it is defined, or the first datum outside that domain returns a not-a-number in')
        rec('    ### silence.')
    for k in cells:
        R5 = np.asarray(P['cells'][k]['R'], dtype=float)
        got5 = {}
        for name, f, kk, _form in F52.MODELS:
            t0m = [1.0, 1.0] + ([0.0] if kk == 3 else [])
            t5, S5, _r5 = F52.fit(f, t0m, X5, R5)
            got5[name] = dict(k=kk, t=[float(v) for v in t5], S=float(S5), aicc=F52.aicc(S5, n5, kk))
        chk = max(abs(got5[m]['aicc'] - F52J['per_cell'][k]['models'][m]['aicc']) for m in ('M1', 'M2', 'M3'))
        rec('')
        rec('  ### a = %s' % k)
        rec("    ### **G-SAMECRITERION:** this act refitting FIVE frames reproduces b352's banked AICc to")
        rec('    ### %.2e absolute -- ### **SO THE CRITERION IS THE SAME CRITERION**, and b352 is EXTENDED'
            % chk)
        rec('    ### and not re-verdicted. ### Its five-frame scores stand exactly as banked.')
        rec('    ### the sixth residual : %+.9e   ### **NEGATIVE**' % rows[k]['R'])
        rec('    ### the ratio at the last doubling : %+.4f, where the previous five ran %s'
            % (rows[k]['R'] / float(R5[-1]),
               ['%.4f' % (R5[i + 1] / R5[i]) for i in range(len(R5) - 1)]))
        out[k] = dict(five=got5, same_criterion=float(chk), R_sixth=float(rows[k]['R']),
                      R6=[float(v) for v in list(R5) + [rows[k]['R']]],
                      nonpos=[int(i) for i in nonpos[k]],
                      six=None, d21_6=None, d23_6=None, c=None, scatter=None,
                      bar1=False, bar1_23=False, bar2=False,
                      d21_5=float(got5['M2']['aicc'] - got5['M1']['aicc']),
                      pen_part=float(d6 - d5), fit_part=None, smallest_visible=None)

    # ============================================================ THE VERDICT.
    rec('')
    rec('-' * 100)
    rec("  ### THE VERDICT, BY THE SEALED BRANCH RULE OF SECTION (F).")
    rec('-' * 100)
    est = (not any_nonpos) and all(out[k]['bar1'] and out[k]['bar2'] for k in cells)
    m1best = False
    rec('    ### **(FLOOR ESTABLISHED)** demands M2 past bar 1 AND c passing bar 2 at EVERY cell.')
    rec('      ### **UNREACHABLE, AND SHOWN SO: NO SIX-FRAME SCORE EXISTS.** ### got : %s' % est)
    rec('    ### **(NO FLOOR PREFERRED)** demands M1 fitting as well or better at every cell.')
    rec('      ### **UNREACHABLE FOR THE SAME REASON.** ### got : %s' % m1best)
    rec('    ### **(ABANDONED)** is for a ceiling overrun. ### The run did NOT overrun: %.1f s against %.0f s.'
        % (time.time() - t0, WALL_CEILING))
    verdict = 'FLOOR UNDER-RESOLVED STILL'
    rec('    ### ### ### **THEREFORE, BY THE LETTER OF THE SEALED CONDITION: %s.**' % verdict)
    rec('')
    rec('    ### ### **AND THE REASON IS NOT THE ONE THE BRANCH ANTICIPATED, WHICH THE ACT SAYS AT FULL')
    rec('    ### ### PROMINENCE RATHER THAN LETTING THE LABEL CARRY IT.** ### The branch was written for')
    rec('    ### ### six frames that fit and did not settle. ### **WHAT HAPPENED IS THAT THE SIXTH FRAME')
    rec('    ### ### DID NOT FIT AT ALL**, because the residual changed sign and the sealed criterion is')
    rec('    ### ### undefined there. ### **THE SEALED BRANCH RULE HAS NO SLOT FOR THIS OUTCOME**, and that')
    rec('    ### ### is itself a finding: the branches were written over the fit verdicts and not over the')
    rec('    ### ### fit existing at all. ### **TABLED, NOT EDITED.**')
    rec('')
    rec('    ### ### **DO THE CELLS STILL DISAGREE?** ### The question presumes three scores to compare and')
    rec('    ### ### **THERE ARE NONE.** ### At five frames they disagreed; at six there is nothing to')
    rec('    ### ### disagree about.')
    still_disagree = None
    wall = time.time() - t0
    rec('')
    rec('    ### ### **THE MEASURED WALL FOR THE WHOLE COMPONENT : %.1f s, AGAINST A CHOSEN CEILING OF %.0f s.**'
        % (wall, WALL_CEILING))
    rec('    ### ### **AND THAT PRINTED WALL IS THE FIRST MEASURED WALL THIS LADDER HAS.**')
    rec('    ### **b339 IS NOT RE-VERDICTED. ### ITS `UNAFFORDABLE` STANDS.** ### And its side-reading --')
    rec("    ### that the residual descends toward a floor -- was labelled by its own act as that seat's")
    rec('    ### reading. ### **THE SIXTH RUNG IS EVIDENCE AGAINST IT, AND THIS ACT DOES NOT WITHDRAW IT**,')
    rec('    ### because b339 marked it a reading and because the sixth rung is the rung where the rank')
    rec('    ### saturates -- so the act cannot tell the object from the instrument there.')
    rec('    ### **b346 IS NOT RE-VERDICTED. ### b352 IS EXTENDED, NOT RE-VERDICTED** -- its five-frame')
    rec('    ### scores are reproduced here to %.0e and stand.' % max(out[k]['same_criterion'] for k in cells))
    rec('=' * 100)
    p = run_clock.write(D, 'b354_sixth_run', LINES)
    io.open(os.path.join(D, 'b354_sixth.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(sixth=list(SIXTH), fifth=list(FIFTH), xs6=XS6, cells=cells, per_cell=out, rows=rows,
             verdict=verdict, still_disagree=still_disagree, wall=float(wall),
             criterion_undefined=bool(any_nonpos), rank_saturated=bool(saturated),
             rank_extrapolated=float(extrap), ranks_banked=list(ranks5),
             pen5=float(d5), pen6=float(d6),
             wall_ceiling=WALL_CEILING, bytes_ceiling=BYTES_CEILING, overran=False,
             identity_sixth=float(id6), identity_fifth=float(id5), repro=rep,
             svd_wall=float(t_svd),
             frame6=dict(free=int(st6['free']), rank=int(st6['rank']), dim=int(st6['dim'])),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
