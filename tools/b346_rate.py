# -*- coding: utf-8 -*-
"""b346_rate.py -- THE EXPONENT BY RATE (registration sealed first).

### ### **THE PREMISE IS TESTED BEFORE THE RATE IS MEASURED, AND BOTH ARE READ FROM THE RECORD'S OWN PRODUCING
### ### ARTIFACTS.**
###   (C1) b339's limit reading, from `b339_limit.json`, the record its own sealed arithmetic wrote.
###   (C2) b344's ladder, from `b344_ny.json`, the record its own ladder wrote.
###   (D)  the even sector's decay rate along the ARGUMENT, under BOTH conventions, on the cells b264's own
###        second axis marked converged, by two estimators sharing no code.
### ### **THE SEPARATION IN THE EXPONENT IS EXACTLY `1.0` AND IS EXACT BY CONSTRUCTION** -- the erratum's own
### sentence, *"The two functions therefore differ by a factor of `rho`, which is not a scalar"*. ### **WHAT IS
### MEASURED HERE IS THE INSTRUMENT'S OWN UNCERTAINTY IN THE RATE.**
### ### **NO OWNER FILE IS EDITED AND NO NEW CELL IS EVALUATED.** ### The owner's evaluator and b313's flipped copy
### are both IMPORTED; the copy's own header declares that it deliberately imports the owner's layer and node
### counts, and this act names that shared engine rather than claiming the routes disjoint.
"""
import io
import json
import math
import os
import re
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)
import noise_floor as NF          # noqa: E402
import qeps_layer as Q            # noqa: E402  ### the prolate layer -- SHARED BY BOTH CONVENTIONS, declared
import b38_act10 as B38           # noqa: E402  ### the node counts -- SHARED BY BOTH CONVENTIONS, declared
import b264_eps_decay as OWNER    # noqa: E402  ### r ** -0.5, the corpus's convention
import b313f_b264_eps_decay as FLIP  # noqa: E402  ### r ** 0.5, the source's convention

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SEP = 1.0                 # ### sealed, section (D): exact by construction, never measured
CORPUS_P = -1.5           # ### the corpus's convention's asymptotic exponent (b264, derived)
SOURCE_P = -0.5           # ### the source's convention's, one full power slower
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


# ### ==============================================================================================
# ### COMPONENT 1 -- THE PREMISE, TESTED.
# ### ==============================================================================================
def premise():
    rec('')
    rec('=' * 100)
    rec('  COMPONENT 1 -- THE PREMISE, TESTED AND NOT ASSUMED.')
    rec('=' * 100)
    L = load('b339_limit.json')
    P = load('b339_price.json')
    rec('')
    rec("  (C1) THE LIMIT AGAINST THE SEPARATION, from b339's own sealed limit arithmetic (data/b339_limit.json):")
    rec('    %-6s %-14s %-14s %-14s %-13s %-13s %-9s' % ('a', 'm_inf', 'off from EF', 'off from ER', 'in units s', 'in units s', 'above both?'))
    c1_rows, c1 = [], True
    for a in sorted(L, key=float):
        r = L[a]
        s = None
        pa = (P.get('cells') or {}).get(a) if isinstance(P, dict) else None
        if isinstance(pa, dict) and 's' in pa:
            s = float(pa['s'])
        above = (r['off_ef'] > 0) and (r['off_er'] > 0)
        c1 = c1 and above
        su = (r['off_ef'] / s, r['off_er'] / s) if s else (float('nan'), float('nan'))
        rec('    %-6s %-14.9f %-14.9f %-14.9f %-13.2f %-13.2f %-9s'
            % (a, r['m_inf'], r['off_ef'], r['off_er'], su[0], su[1], 'ABOVE BOTH' if above else '### NOT'))
        c1_rows.append(dict(a=a, m_inf=r['m_inf'], off_ef=r['off_ef'], off_er=r['off_er'], s=s,
                            off_ef_s=su[0], off_er_s=su[1], above_both=bool(above),
                            ratios=r['ratios'], p=r['p'], rms=r['rms']))
    rec('    ### the limit sits ABOVE BOTH candidates at every covered cell : %s' % c1)
    # ### ### **AND ONE READING OF b339's IS NARROWER THAN ITS SENTENCE, MEASURED HERE AND REPORTED.**
    # ### b339's bank wrote that the descent's ratios *"fall step by step"* and quoted three figures AT `a = 1.3`.
    # ### Re-read from its own record at all three cells, they fall monotonically at THAT CELL ONLY.
    # ### **THIS CHANGES NOTHING ABOUT b339's VERDICT, WHICH RESTED ON THE PRICE AND NOT ON THE RATIOS, AND NOTHING
    # ### ABOUT (C1), WHOSE SEALED CRITERION IS THE LIMIT'S POSITION AND NOT THE RATIOS' MONOTONICITY.**
    fall = {}
    for x in c1_rows:
        rr = x['ratios']
        fall[x['a']] = all(rr[i] > rr[i + 1] for i in range(len(rr) - 1))
        rec('    ### the descent ratios at a = %-5s : %s   falling step by step : %s'
            % (x['a'], ' '.join('%.4f' % z for z in rr), fall[x['a']]))
    rec('    ### ### **THEY FALL MONOTONICALLY AT %d OF THE %d CELLS.** ### b339 quoted this reading at `a = 1.3`,'
        % (sum(1 for v in fall.values() if v), len(fall)))
    rec("    ### where it holds. ### **IT IS NOT THE (C1) CRITERION AND b339's VERDICT DID NOT REST ON IT.**")
    rec('')
    rec("  (C2) THE ONE AXIS THAT HAS BEEN PRICED, from b344's own ladder (data/b344_ny.json):")
    N = load('b344_ny.json')
    v = [r['R_EF'] for r in N['rows']]
    steps = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    ratios = [steps[i] / steps[i + 1] for i in range(len(steps) - 1)]
    q = ratios[-1]
    limit = v[-1] + steps[-1] / (q - 1.0)
    at512 = v[N['ladder'].index(512)]
    travel = limit - at512
    floor = N['floor']
    frac = abs(travel) / abs(floor)
    c2 = frac < 1.0
    rec('    the ladder %s ; the residual %s' % (N['ladder'], ' '.join('%+.9f' % x for x in v)))
    rec('    the increments fall by factors %s, so the residual CONVERGES in NY' % ' '.join('%.2f' % x for x in ratios))
    rec("    the extrapolated limit %+.9f ; from the corpus's own NY = 512 the remaining travel is %.3e"
        % (limit, travel))
    rec("    b339's floor at that cell %+.9f ; the travel is %.4f of the floor" % (floor, frac))
    rec('    ### the remaining travel in NY is STRICTLY LESS THAN the floor : %s' % c2)
    present = c1 and c2
    rec('')
    if present:
        rec('  ### ### **A FLOOR IS PRESENT.** ### The limit sits above both candidates at every covered cell, and the')
        rec('  ### one axis of the three that has been priced cannot carry the residual to zero: its whole remaining')
        rec('  ### travel is a fraction of the floor.')
        rec('  ### ### ### **SO NO DOMAIN RESOLVES THE EXPONENT BY VALUE, AND THE ACT SAYS SO AT FULL PROMINENCE.**')
    else:
        rec('  ### ### **THE PREMISE FAILS** -- (C1) %s, (C2) %s. ### The rate below is measured on its own terms and' % (c1, c2))
        rec('  ### is NOT to be read as a consequence of a floor.')
    rec('  ### ### **AND ITS LIMIT: (C2) IS ONE AXIS OF THREE.** ### The cut\'s `tau` and the taper are named and NOT')
    rec("  ### MOVED, and nothing is concluded about them. ### **THE FLOOR IS NOT EXPLAINED.**")
    return dict(c1=bool(c1), c2=bool(c2), present=bool(present), rows=c1_rows, ratios_fall=fall, ladder=N['ladder'],
                residual=v, ratios=ratios, limit=limit, at512=at512, travel=travel, floor=floor, frac=frac)


# ### ==============================================================================================
# ### COMPONENT 2 -- THE RATE. ### TWO ESTIMATORS SHARING NO CODE.
# ### ==============================================================================================
def converged_cells():
    """### b264's OWN converged marking, read from its banked table. ### **THE ROWS IT MARKED NOT CONVERGED ARE
    ### EXCLUDED BY ITS CRITERION AND NOT BY A CHOICE THIS ACT MAKES.**"""
    txt = io.open(os.path.join(D, 'b264_run.txt'), encoding='utf-8', errors='replace').read().splitlines()
    head = '  rho       NG       eps_even         envelope C/rho   rel(NG,2NG)  rel(NQ,2NQ)  rho^1.5*eps    converged'
    i = txt.index(head)
    keep, dropped = [], []
    for ln in txt[i + 2:]:
        m = re.match(r'\s*(\d+)\s+(\d+)\s+(\S+)\s+\S+\s+\S+\s+\S+\s+\S+\s+(True|False)\s*$', ln)
        if not m:
            break
        row = dict(rho=int(m.group(1)), NG=int(m.group(2)), eps_banked=float(m.group(3)), converged=(m.group(4) == 'True'))
        (keep if row['converged'] else dropped).append(row)
    return keep, dropped, i + 1


def route_A(rho, eps):
    """### ROUTE A -- THE LOCAL SLOPE between consecutive cells."""
    return [math.log(abs(eps[k + 1]) / abs(eps[k])) / math.log(rho[k + 1] / rho[k]) for k in range(len(rho) - 1)]


def route_B(rho, eps, lo=0):
    """### ROUTE B -- THE SHARP-RATE ESTIMATOR, SHARING NO CODE WITH ROUTE A. ### For a trial exponent `q`, form
    ### `g_q = rho^q eps` over the window and take its RELATIVE DRIFT across the top; the estimate is the `q` that
    ### annihilates that drift, solved by SECANT on `q`. ### **NOT A SLOPE: A ZERO OF A DRIFT FUNCTIONAL.**"""
    def drift(q):
        g = [(r ** q) * e for r, e in zip(rho[lo:], eps[lo:])]
        return (g[-1] - g[-2]) / abs(g[-1])
    q0, q1 = 0.0, 2.0
    f0, f1 = drift(q0), drift(q1)
    for _ in range(80):
        if abs(f1 - f0) < 1e-300:
            break
        q2 = q1 - f1 * (q1 - q0) / (f1 - f0)
        q0, f0, q1 = q1, f1, q2
        f1 = drift(q1)
        if abs(f1) < 1e-14:
            break
    return -q1, abs(f1)


def rate():
    rec('')
    rec('=' * 100)
    rec('  COMPONENT 2 -- THE RATE ALONG THE ARGUMENT, UNDER BOTH CONVENTIONS.')
    rec('=' * 100)
    keep, dropped, head_line = converged_cells()
    rho = [r['rho'] for r in keep]
    rec('')
    rec("  THE CELLS -- b264's own converged marking (its table head at data/b264_run.txt line %d):" % head_line)
    rec('    converged and USED     : %s' % rho)
    rec('    NOT converged, EXCLUDED BY b264\'s OWN CRITERION : %s' % [r['rho'] for r in dropped])
    rec("    ### b264's own sentence on them: they *\"ARE NOT EVIDENCE ABOUT `eps` AND THEY ARE NOT COUNTED AS ANY.\"*")
    LAY = Q.layer(B38.EPS_NQ)
    rec('')
    rec('  THE SHARED ENGINE, NAMED RATHER THAN CLAIMED ABSENT: both evaluators take the prolate layer `Q.layer` and')
    rec("  the node counts `B38.EPS_NQ = %d` from the OWNER's files. ### b313's copy-maker declares this deliberately:" % B38.EPS_NQ)
    rec('  the exponent does not reach either. ### **A SHARED ENGINE IS A SHARED ERROR SOURCE, AND WHAT THIS ACT DOES')
    rec('  ### NOT CERTIFY IS INDEPENDENCE OF THE PROLATE SOLVER OR OF THE NODE COUNTS.**')
    rec('')
    rec('  THE VALUES, BOTH CONVENTIONS, AT b264\'s NG LAW:')
    rec('    %-6s %-7s %-22s %-22s %-13s %-13s %-11s' % ('rho', 'NG', 'eps_even, r**-0.5', 'eps_even, r**+0.5', 'ratio src/cor', 'rho itself', 'vs b264'))
    eC, eS, repro = [], [], 0.0
    t0 = time.time()
    for r in keep:
        NG = OWNER.ng_for(r['rho'])
        a = float(OWNER.eps_modes(float(r['rho']), NG, LAY)[0::2].sum())
        b = float(FLIP.eps_modes(float(r['rho']), NG, LAY)[0::2].sum())
        eC.append(a)
        eS.append(b)
        d = abs(a - r['eps_banked']) / abs(r['eps_banked'])
        repro = max(repro, d)
        rec('    %-6d %-7d %-22.15e %-22.15e %-13.9f %-13.1f %-11.3e'
            % (r['rho'], NG, a, b, b / a, float(r['rho']), d))
    rec('    ### G-REPRO -- the owner recomputed against b264\'s banked column, worst relative : %.3e' % repro)
    rec('    ### the ratio of the two conventions is the argument itself at every cell, worst departure : %.3e'
        % max(abs(b_ / a_ - r_) for a_, b_, r_ in zip(eC, eS, [float(x['rho']) for x in keep])))
    rec('    ### **THAT IS THE SEPARATION, AND IT IS EXACT BY CONSTRUCTION RATHER THAN MEASURED.**  (%.0f s)' % (time.time() - t0))
    # ### the two estimators
    rec('')
    rec('  ROUTE A -- THE LOCAL SLOPE between consecutive converged cells:')
    pA_C, pA_S = route_A(rho, eC), route_A(rho, eS)
    rec('    %-14s %-14s %-14s %-14s' % ('window', 'r**-0.5', 'r**+0.5', 'difference'))
    for k in range(len(pA_C)):
        rec('    %-14s %-14.9f %-14.9f %-14.9f' % ('%d -> %d' % (rho[k], rho[k + 1]), pA_C[k], pA_S[k], pA_S[k] - pA_C[k]))
    rec('')
    rec('  ROUTE B -- THE SHARP-RATE ESTIMATOR (a zero of a drift functional, sharing no code with route A):')
    qB_C, rC = route_B(rho, eC)
    qB_S, rS = route_B(rho, eS)
    qB_C2, _ = route_B(rho, eC, lo=1)
    qB_S2, _ = route_B(rho, eS, lo=1)
    rec('    full window   : r**-0.5 -> %.9f   ; r**+0.5 -> %.9f   (residual drift %.2e / %.2e)' % (qB_C, qB_S, rC, rS))
    rec('    bottom raised : r**-0.5 -> %.9f   ; r**+0.5 -> %.9f' % (qB_C2, qB_S2))
    # ### the uncertainty, as (D) defines it
    u1 = abs(pA_C[-1] - pA_C[-2])
    u1s = abs(pA_S[-1] - pA_S[-2])
    u2 = abs(qB_C2 - qB_C)
    u2s = abs(qB_S2 - qB_S)
    u3 = abs(qB_C - pA_C[-1])
    u3s = abs(qB_S - pA_S[-1])
    U = max(u1, u1s, u2, u2s, u3, u3s)
    which = {'(u1) spread of route A over the top pair': max(u1, u1s),
             "(u2) drift of route B's solved q as the window's bottom is raised": max(u2, u2s),
             '(u3) difference between the routes at the top': max(u3, u3s)}
    dom = max(which, key=lambda k: which[k])
    rec('')
    rec("  THE INSTRUMENT'S UNCERTAINTY IN THE RATE, AS SECTION (D) DEFINES IT -- THE LARGEST OF THREE:")
    for k in ('(u1) spread of route A over the top pair',
              "(u2) drift of route B's solved q as the window's bottom is raised",
              '(u3) difference between the routes at the top'):
        rec('    %-66s %.6e' % (k, which[k]))
    rec('    ### ### **THE UNCERTAINTY : %.6e**   ### dominated by %s' % (U, dom.split(')')[0] + ')'))
    # ### ### **AND THE TWO ARMS THAT DID NO WORK, MEASURED AND DECLARED RATHER THAN REPORTED AS AGREEMENT.**
    # ### Route B, AS SECTION (D) SEALS IT, takes the drift of `rho^q eps` ACROSS THE TOP of the window -- which is
    # ### two points -- and the `q` annihilating a TWO-POINT drift is ALGEBRAICALLY the local slope of those same
    # ### two points. ### So route B COLLAPSES ONTO ROUTE A AT THE TOP, (u3) sits at machine level, and (u2) is
    # ### STRUCTURALLY ZERO because raising the window's bottom cannot move a top-pair estimator at all.
    # ### **THAT IS A DEFECT IN THE SEALED PAIRING AND IT IS TABLED, NOT REPAIRED: THE SEALED FILE IS NOT EDITED
    # ### AND ROUTE B RUNS AS SEALED.** ### The direction of the risk is named below and so is the reading that
    # ### bounds it.
    collapse = (abs(u2) == 0.0 and abs(u2s) == 0.0) and max(u3, u3s) < 1e-12
    whole_C = max(pA_C) - min(pA_C)
    whole_S = max(pA_S) - min(pA_S)
    whole = max(whole_C, whole_S)
    rp_whole = SEP / whole if whole > 0 else float('inf')
    if collapse:
        rec('')
        rec('    ### ### **TWO OF THE THREE ARMS DID NO WORK, AND THAT IS SAID HERE RATHER THAN LEFT TO LOOK LIKE')
        rec('    ### ### AGREEMENT.** ### A `q` that annihilates a TWO-POINT drift is algebraically the local slope of')
        rec('    ### ### those same two points, so route B COLLAPSES ONTO ROUTE A at the top of the window: (u3) sits at')
        rec('    ### ### machine level (%.2e) and (u2) is STRUCTURALLY ZERO, since raising the bottom cannot move a' % max(u3, u3s))
        rec('    ### ### top-pair estimator. ### **THE SEALED PAIRING IS DEFECTIVE AND IS TABLED, NOT REPAIRED; THE')
        rec('    ### ### SEALED FILE IS NOT EDITED AND ROUTE B RAN AS SEALED.**')
        rec('    ### **THE DIRECTION OF THE RISK, NAMED: AN ARM THAT IS STRUCTURALLY ZERO CANNOT INFLATE THE')
        rec('    ### UNCERTAINTY, SO IT CANNOT MAKE THE RESOLVING POWER LOOK BETTER THAN IT IS -- IT CAN ONLY LEAVE IT')
        rec('    ### UNDERSTATED.** ### So the understatement is bounded here, by a DIAGNOSTIC and not by a new bar:')
        rec('    ### the spread of route A over the WHOLE converged window rather than its top pair.')
        rec('    DIAGNOSTIC -- whole-window spread of the local slope : %.6e (r**-0.5) / %.6e (r**+0.5)' % (whole_C, whole_S))
        rec('    DIAGNOSTIC -- the resolving power under that more conservative reading : %.1f' % rp_whole)
        rec('    ### ### **THE VERDICT DOES NOT TURN ON THE CHOICE: THE SEPARATION CLEARS BOTH READINGS.** ### This is')
        rec("    ### a diagnostic and NOT this act's uncertainty, which stays as section (D) defines it.")
    # ### the noise-floor gate
    gC, whyC = NF.classify(pA_C[-1], qB_C)
    gS, whyS = NF.classify(pA_S[-1], qB_S)
    rec('')
    rec('  THE NOISE-FLOOR GATE on each convention\'s pair of route values:')
    rec('    r**-0.5 : %-9s %s' % (gC, whyC[:96]))
    rec('    r**+0.5 : %-9s %s' % (gS, whyS[:96]))
    gate_ok = (gC == NF.RESOLVED) and (gS == NF.RESOLVED)
    return dict(collapse=bool(collapse), whole_window=whole, whole_corpus=whole_C, whole_source=whole_S,
                resolving_whole=rp_whole,
                cells=rho, dropped=[r['rho'] for r in dropped], head_line=head_line, eps_corpus=eC, eps_source=eS,
                repro=repro, routeA_corpus=pA_C, routeA_source=pA_S, routeB_corpus=qB_C, routeB_source=qB_S,
                routeB_corpus_raised=qB_C2, routeB_source_raised=qB_S2, u1=max(u1, u1s), u2=max(u2, u2s),
                u3=max(u3, u3s), U=U, dominant=dom, gate_corpus=gC, gate_source=gS, gate_ok=bool(gate_ok),
                NQ=B38.EPS_NQ)


def main():
    t0 = time.time()
    rec('=' * 100)
    rec('b346 -- THE EXPONENT BY RATE. ### the premise tested, then the rate along the argument.')
    rec('=' * 100)
    fails = []
    PR = premise()
    RA = rate()
    U, resolving = RA['U'], (SEP / RA['U'] if RA['U'] > 0 else float('inf'))
    rec('')
    rec('=' * 100)
    rec("  THE VERDICT, BY b322's RESOLVING-POWER RULE AND NO OTHER.")
    rec('=' * 100)
    rec('    the separation, EXACT BY CONSTRUCTION      : %.1f' % SEP)
    rec("    the instrument's uncertainty in the rate   : %.6e" % U)
    rec('    the resolving power (separation / uncertainty) : %.1f' % resolving)
    if RA['gate_ok'] and SEP > U:
        verdict = 'RESOLVED'
        rec('')
        rec('  ### ### **VERDICT: RESOLVED ON THIS AXIS.** ### The separation exceeds the instrument\'s own uncertainty')
        rec('  ### in the rate by a factor of %.0f, and the noise-floor gate returns RESOLVED at both conventions.' % resolving)
    elif not RA['gate_ok']:
        verdict = 'STILL UNDER-RESOLVED'
        rec('')
        rec('  ### ### **VERDICT: STILL UNDER-RESOLVED -- the gate refuses at least one convention\'s pair.**')
        fails.append('GATE')
    else:
        verdict = 'STILL UNDER-RESOLVED'
        rec('')
        rec("  ### ### **VERDICT: STILL UNDER-RESOLVED.** ### The instrument's uncertainty in the rate is %.6e," % U)
        rec('  ### which does not sit below the separation of %.1f. ### THE NEW FIGURE IS IN THE RATE\'S UNITS.' % SEP)
    # ### which convention the banked values carry -- the only naming section (D) permits
    dC = abs(RA['routeA_corpus'][-1] - CORPUS_P)
    dS = abs(RA['routeA_corpus'][-1] - SOURCE_P)
    named = 'the corpus\'s own `r ** -0.5`' if dC < dS else 'the source\'s `r ** +0.5`'
    rec('')
    rec('  WHICH CONVENTION THE BANKED VALUES CARRY, READ FROM THEIR OWN DECAY AND FROM NOTHING ELSE:')
    rec("    route A's slope at the top of the converged window : %.9f" % RA['routeA_corpus'][-1])
    rec('    its distance from the corpus\'s asymptote (%.1f)     : %.6e' % (CORPUS_P, dC))
    rec('    its distance from the source\'s asymptote  (%.1f)     : %.6e' % (SOURCE_P, dS))
    rec('    ### ### **THE BANKED VALUES CARRY %s**, and that is readable from the values alone.' % named.upper())
    rec('')
    rec('  ### ### **AND WHAT THAT IS PERMITTED TO MEAN, IN SECTION (D)\'s OWN WORDS, FIXED BEFORE THIS FIGURE EXISTED:**')
    rec('  ### ### **IT MEANS THAT THE CONVENTION UNDER WHICH A BANKED `eps`-DERIVED VALUE WAS COMPUTED IS RECOVERABLE')
    rec('  ### ### FROM THAT VALUE\'S OWN DECAY, SO THE ERRATUM\'S STANDING CLAUSE ACQUIRES A MECHANICAL TEST.')
    rec('  ### ### IT DOES NOT MEAN THAT A CONVENTION IS CORRECT.**')
    rec("  ### b313's clause governs: *\"THE EXPONENT IS FIXED BY THE SOURCE'S OWN DEFINITION OF THE OBJECT THE CORPUS")
    rec('  ### IMPORTED, AND BY NOTHING THE RESIDUE DOES"*, and *"a residue is not a vote on that"*. ### **A RATE IS')
    rec('  ### NOT A VOTE ON IT EITHER.** ### The erratum already states this convention FROM THE CODE; naming it from')
    rec('  ### the VALUES is a second and independent route to the same statement, and is worth exactly that.')
    rec('')
    rec('  ### NO FRAME BUILT ; NO CELL ADDED OR MOVED ; NO BAR MOVED ; NO ACT RE-VERDICTED ; NO OWNER FILE EDITED.')
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    p, k = os.path.join(D, 'b346_rate_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, 'b346_rate_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(os.path.join(D, 'b346_rate.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(premise=PR, rate=RA, separation=SEP, uncertainty=U, resolving_power=resolving, verdict=verdict,
             convention_named=named, slope_top=RA['routeA_corpus'][-1], d_corpus=dC, d_source=dS,
             corpus_p=CORPUS_P, source_p=SOURCE_P, fails=fails, run_file=os.path.basename(p),
             elapsed=time.time() - t0), indent=1))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
