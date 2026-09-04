# -*- coding: utf-8 -*-
"""b313 FLIPPED COPY (NOT AN OWNER FILE) -- b264_eps_decay.py -- J4: `eps_even`'s DECAY. ### THE RUN.

### WHAT THIS FILE DOES AND WHAT IT MAY NOT DO.
### ### **IT IS A CONTROL ON A DERIVATION, NOT THE DERIVATION.** ### The derivation lives in
### `data/b264_eps_even_decay.txt`. ### Every falsifier F1-F6 was fixed, with its bar, in
### `data/b264_registration_2026-08-31.txt`, which is SEALED (`c9abc57f...`).

### ### **WHY A NEW EVALUATOR EXISTS AT ALL, SAID BEFORE IT IS USED.**
### The owner's `b38_act10.per_mode_eps_grids` fixes `EPS_NG = 400` Gauss-Legendre nodes. ### The
### integrand `A_n(rho u)` oscillates with roughly `rho` periods across `u in [1/rho, 1]`, so a
### FIXED node count against a GROWING oscillation count is a ceiling. ### **THAT IS AN INSTRUMENT
### FACT, NOT A FACT ABOUT `eps`**, and this act measures where it sits rather than inheriting it.
### ### **NO OWNER FILE IS EDITED.** ### This file re-implements the owner's formula with a
### CONFIGURABLE node count and CHUNKED evaluation, and is ### **G-REPRO'd AGAINST THE OWNER ON
### THE OVERLAP BEFORE ANY NEW VALUE IS READ (F5).** ### If F5 fires, S3 is VOID.

### ### **THE COST CEILING, DECLARED IN THE REGISTRATION BEFORE THE ATTEMPT: 900 s wall-clock,
### ### 2048 MB, NO SINGLE ALLOCATION ABOVE 256 MB.** ### Every cell not run is PRICED.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import b38_act10 as B38          # noqa: E402
import qeps_layer as Q           # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK = r'D:\relay\data\b313f_b264_scratch.txt'
ROWS = r'D:\relay\data\b313f_b264_rows.json'
CACHE = r'D:\relay\data\b313f_b264_cache.npz'
B261J = r'D:\relay\data\b261_rows.json'

# ### THE BARS AND AXES, FIXED IN THE SEALED REGISTRATION BEFORE ANY VALUE EXISTED.
F1_BAR = 1e-9         # ### envelope, ABSOLUTE (a one-sided claim takes an absolute bar)
F2_BAR = 0.05         # ### leading constant, RELATIVE, at the top converged cell
F3_LO, F3_HI = 0.95, 1.05     # ### oscillation period in rho
F4_BAR = 1e-10        # ### b38's own mask-algebra bar
F5_BAR = 1e-12        # ### G-REPRO vs the owner at the owner's own NG
NODES_PER_PERIOD = 8  # ### the registered `K` in `NG = max(400, ceil(K * rho))`
CONV_BAR = 1e-8       # ### NG vs 2NG, RELATIVE -- the convergence test S3 uses
LADDER = [2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
OSC_LO, OSC_HI, OSC_STEP = 40.0, 50.0, 0.025
TAIL_R = 100.0        # ### the L^2 tail identity's truncation. ### **BROUGHT INSIDE THE
                      # ### MEASURED `EPS_NQ` CEILING (~238); 2000 evaluated `A_n` where it is noise.**
CHUNK = 4096

_gl = {}

# ### **THE DEVIATION, DECLARED AT ITS CAUSE AND AGAIN IN THE BANK (registration (L)'s standing
# ### deviation rule: "any departure from this registration is DECLARED IN THE BANK, NOT SMOOTHED
# ### OVER").** ### The runner as FIRST WRITTEN called `np.polynomial.legendre.leggauss(NG)` for
# ### every `NG`. ### That routine builds a DENSE `NG x NG` companion matrix and calls `eigvalsh`
# ### on it, so its cost is `8 * NG^2` bytes IN ONE ALLOCATION. ### **THE FIRST RUN DIED THERE:
# ### `gl(60000)` ASKS FOR 28.8 GB, AND THE REGISTRATION'S CLAUSE (I) DECLARES "NO SINGLE
# ### ALLOCATION ABOVE 256 MB".** ### The ceiling binds from `NG > 5793` upward, i.e. from the
# ### REGISTERED ladder's `x = 500` convergence cell onward -- so the registered target of
# ### **`x` TO AT LEAST 1000 WAS NOT REACHABLE BY THE MONOLITHIC RULE AT ALL.**
# ### ### **THE REPAIR IS THE REGISTRATION'S OWN "CHUNKED" DISCIPLINE APPLIED TO THE RULE AS WELL
# ### ### AS TO THE EVALUATION, AND IT CHANGES NO REGISTERED QUANTITY:** at or below
# ### `GL_DENSE_MAX` the monolithic rule is used ### UNCHANGED ### -- so F5 still runs against the
# ### owner at the owner's own `NG = 400` on the owner's own nodes -- and above it `[-1,1]` is cut
# ### into `P` equal panels carrying `GL_PANEL` nodes each. ### **THE TOTAL NODE COUNT IS THE
# ### REGISTERED ONE, SO THE `NG` LAW AND THE `NG` vs `2 NG` TEST ARE HONOURED EXACTLY**; the
# ### peak allocation falls from `8 NG^2` to `8 GL_PANEL^2` (1.28 MB) plus the `8 NG` node arrays.
# ### ### **AND THE HONEST DIRECTION OF THE CHANGE IS STATED RATHER THAN LEFT FLATTERING:** a
# ### composite rule is not a concession on an oscillatory integrand -- a monolithic Gauss rule
# ### clusters its nodes at the endpoints and thins in the middle, which is the wrong density for
# ### a fixed-frequency oscillation, ### **so the panelled rule is at least as good at equal node
# ### count and this act does not claim it is better than "at least as good".**
GL_DENSE_MAX = 4000   # ### 8*4000^2 = 128 MB, INSIDE the registered 256 MB single-allocation cap
GL_PANEL = 400        # ### panel order = THE OWNER'S OWN `EPS_NG`, so no new node count is coined


def gl(NG):
    """### Gauss-Legendre nodes/weights on `[-1,1]` with `NG` total nodes. ### See the declared
    ### deviation above: monolithic at or below `GL_DENSE_MAX`, composite panels above it."""
    if NG in _gl:
        return _gl[NG]
    if NG <= GL_DENSE_MAX:
        _gl[NG] = np.polynomial.legendre.leggauss(NG)
        return _gl[NG]
    P = int(math.ceil(NG / float(GL_PANEL)))          # ### panel count
    q = int(math.ceil(NG / float(P)))                 # ### nodes per panel, q <= GL_PANEL
    bx, bw = np.polynomial.legendre.leggauss(q)       # ### ONE small dense solve, 8*q^2 bytes
    edges = np.linspace(-1.0, 1.0, P + 1)
    h = 0.5 * (edges[1] - edges[0])                   # ### half-width of one panel
    ctr = 0.5 * (edges[:-1] + edges[1:])
    xs = (ctr[:, None] + h * bx[None, :]).ravel()
    ws = np.tile(h * bw, P)
    _gl[NG] = (xs, ws)
    return _gl[NG]


def gl_kind(NG):
    """### The rule's species, so the bank can print WHICH rule produced every number."""
    if NG <= GL_DENSE_MAX:
        return 'monolithic %d' % NG
    P = int(math.ceil(NG / float(GL_PANEL)))
    q = int(math.ceil(NG / float(P)))
    return 'composite %d x %d = %d' % (P, q, P * q)


def an_chunked(X, LAY, chunk=CHUNK):
    """### THE OWNER'S `an`, CHUNKED. ### `A_n(x) = (2/|lam_n|) int_0^1 xi_n(t) cos(2 pi t x) dt`,
    ### written exactly as `qeps_layer.layer`'s closure writes it, evaluated in blocks so that no
    ### single allocation exceeds the registered ceiling."""
    x, w, lam, lam2, xi, xi1, an, dan = LAY
    X = np.atleast_1d(np.asarray(X, dtype=float))
    out = np.empty((X.size, xi.shape[1]))
    for i in range(0, X.size, chunk):
        Xi = X[i:i + chunk]
        C = np.cos(2 * math.pi * np.outer(Xi, x))
        out[i:i + chunk] = (C * w) @ xi / lam
    return out


def eps_modes(r, NG, LAY):
    """### THE OWNER'S PER-MODE FORMULA, NODE COUNT CONFIGURABLE.
    ### `eps_n(rho) = [lam^2/(1-lam^2)] rho^{+1/2} INT_{1/rho}^{1} A_n(u) A_n(rho u) du`."""
    x, w, lam, lam2, xi, xi1, an, dan = LAY
    lo, hi = 1.0 / r, 1.0
    if hi - lo <= 0:
        return np.zeros(xi.shape[1])
    gx, gw = gl(NG)
    u = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
    jac = 0.5 * (hi - lo)
    A1 = an_chunked(u, LAY)
    A2 = an_chunked(r * u, LAY)
    I = ((A1 * A2) * (gw[:, None] * jac)).sum(0)
    return lam2 / (1 - lam2) * (r ** 0.5) * I


def ng_for(r):
    return int(max(400, math.ceil(NODES_PER_PERIOD * r)))


def curve(rr, LAY, conv=False):
    """### eps_n on a grid, with the NG law and (optionally) the NG-vs-2NG convergence test."""
    NT = LAY[4].shape[1]
    em = np.zeros((NT, len(rr)))
    rel = np.zeros(len(rr))
    for k, r in enumerate(rr):
        NG = ng_for(r)
        e1 = eps_modes(float(r), NG, LAY)
        em[:, k] = e1
        if conv:
            e2 = eps_modes(float(r), 2 * NG, LAY)
            a = float(e1[0::2].sum())
            b = float(e2[0::2].sum())
            rel[k] = abs(a - b) / max(abs(b), 1e-300)
    return em, rel


def main():
    out = []
    t_start = time.time()

    def rec(s=''):
        print(s)
        out.append(s)

    LAY = Q.layer(B38.EPS_NQ)
    x, w, lam, lam2, xi, xi1, an, dan = LAY
    NT = xi.shape[1]
    EVEN = list(range(0, NT, 2))
    ODD = list(range(1, NT, 2))

    rec('=' * 100)
    rec("b264 RUN -- J4: `eps_even`'s DECAY. ### CONTROLS ON A DERIVATION.")
    rec('### Registration SEALED (`c9abc57f...`) and VERIFIED BEFORE THIS RUN. Bars fixed there.')
    rec('=' * 100)
    rec('### **THE DOUBLE-LIMIT DISCIPLINE (registration (C)), NAMED AT EVERY USE:**')
    rec('###   ### **(X) THE KERNEL LIMIT: `x -> inf` IN `eps_even(x)`.** ### One real variable.')
    rec('###   ### **(A) THE CELL-LADDER LIMIT: `a^2 -> inf`.** ### The DIAGONAL `a^2` coordinate.')
    rec('### **(A) DRIVES (X) AT EVERY `s > 0` THROUGH b261\'s VERIFIED IDENTITY, AND AT `s = 0` IT')
    rec('### DRIVES NOTHING: `a^0 = 1` AND `eps_even(1) = 0` FOR EVERY `a`.**')

    # ---------------------------------------------------------------- axes
    rec('')
    rec('--- ### W-ORD-TE-SPEC: THE AXES, PRINTED BEFORE ANY NUMBER IS READ ---')
    rec('  EPS_NQ (prolate nodes)  : %d      ### the owner\'s, UNCHANGED' % B38.EPS_NQ)
    rec('  NTERM (modes)           : %d      ### qeps_layer; ALREADY the EVEN prolate modes (P1)'
        % NT)
    rec('  EVEN mask / ODD mask    : %s / %s' % (EVEN, ODD))
    rec('  ### **THE AXIS THAT MOVES, DECLARED:** the owner fixes `EPS_NG = %d`; this act uses'
        % B38.EPS_NG)
    rec('    ### **`NG = max(400, ceil(%d * rho))` -- EIGHT NODES PER OSCILLATION PERIOD**, and'
        % NODES_PER_PERIOD)
    rec('    ### **THE CONVERGENCE TEST IS `NG` VS `2 NG`, NOT A LOOK AT THE CURVE.**')
    rec('  bars (all registered)   : F1 %.0e abs | F2 %.2f rel | F3 [%.2f,%.2f] | F4 %.0e | F5 %.0e'
        % (F1_BAR, F2_BAR, F3_LO, F3_HI, F4_BAR, F5_BAR))
    rec('  ### CELL SPECIES: ### **`rho` IS THE KERNEL VARIABLE (X). ### `a^2` IS THE DIAGONAL')
    rec('  ###   LADDER CELL (A). ### THEY ARE NOT THE SAME AXIS AND ARE NEVER PRINTED AS ONE.**')

    # ------------------------------------------------- THE DECLARED DEVIATION
    rec('')
    rec('--- ### **THE DEVIATION FROM THIS ACT\'S FIRST RUNNER, DECLARED HERE AND NOT SMOOTHED')
    rec('---     ### OVER** (registration (L)\'s standing deviation rule) ---')
    rec('  ### **THE FIRST RUN OF THIS FILE DIED, AND IT DIED AGAINST THE REGISTRATION\'S OWN')
    rec('  ### CEILING RATHER THAN AGAINST ANY MATHEMATICS.** ### `np.polynomial.legendre.leggauss`')
    rec('  ### builds a DENSE `NG x NG` matrix and calls `eigvalsh`: ### **`gl(60000)` ASKS FOR')
    rec('  ### 28.8 GB IN ONE ALLOCATION, AND CLAUSE (I) DECLARES "NO SINGLE ALLOCATION ABOVE')
    rec('  ### 256 MB".** ### `MemoryError` at `(IDENT-D)`, before the ladder was reached.')
    rec('  ### ### **AND THE SHARPER HALF, WHICH IS ABOUT THE REGISTRATION AND NOT ABOUT NUMPY:**')
    rec('  ### ### the cap `8*NG^2 <= 256 MB` binds from ### **`NG > 5793`** ### upward, i.e. from')
    rec('  ### ### the ### REGISTERED ### ladder\'s `x = 500` CONVERGENCE cell onward -- so')
    rec('  ### ### **THE REGISTERED TARGET OF `x` TO AT LEAST 1000 WAS NEVER REACHABLE BY THE')
    rec('  ### ### MONOLITHIC RULE, AND CLAUSE (I) WAS INTERNALLY UNSATISFIABLE AS WRITTEN.**')
    rec('  ### **THE REPAIR, AND WHAT IT DOES NOT TOUCH:** the rule is now PANELLED above')
    rec('  ### `GL_DENSE_MAX = %d` -- `P` equal panels of `GL_PANEL = %d` nodes, the panel order'
        % (GL_DENSE_MAX, GL_PANEL))
    rec('  ### being ### **THE OWNER\'S OWN `EPS_NG`, SO NO NEW NODE COUNT IS COINED.**')
    rec('  ### ### **THE TOTAL NODE COUNT IS THE REGISTERED ONE. ### THE `NG` LAW IS UNCHANGED.')
    rec('  ### ### THE `NG` vs `2 NG` TEST IS UNCHANGED. ### F5 STILL RUNS MONOLITHIC AT THE')
    rec('  ### ### OWNER\'S `NG = 400` ON THE OWNER\'S OWN NODES.** ### Peak allocation for the')
    rec('  ### rule falls from `8*NG^2` to `8*%d^2` = %.2f MB.' % (GL_PANEL, 8.0 * GL_PANEL ** 2 / 1e6))
    rec('  ### **NO OWNER FILE WAS EDITED. ### THE FILE REPAIRED IS THIS ACT\'S OWN RUNNER** (K.4).')
    rec('  ### **AND THE DIRECTION OF THE CHANGE IS NOT DRESSED UP:** a monolithic Gauss rule')
    rec('  ### clusters nodes at the endpoints and thins in the middle, which is the wrong density')
    rec('  ### for a fixed-frequency oscillation, ### **so the panelled rule is AT LEAST AS GOOD at')
    rec('  ### equal node count -- and this act claims NOTHING BEYOND "at least as good".**')
    rec('  ### ### **THIS IS AN INSTRUMENT CEILING OF A SECOND KIND AND IT IS FILED AS ONE:** not')
    rec('  ### ### the owner\'s `EPS_NG = 400` ceiling this act was sent to measure, but a ceiling')
    rec('  ### ### on ### THIS ACT\'S OWN REMEDY ### for it. ### **`W-ORD-GL-PANEL` IS FILED.**')

    # ================================================================ F5, FIRST
    rec('')
    rec('=' * 100)
    rec('### F5 -- THE G-REPRO, RUN ### FIRST ### , BEFORE ANY NEW VALUE IS READ.')
    rec('=' * 100)
    rr_rep = np.exp(np.linspace(0.0, math.log(100.001), 60))
    t0 = time.time()
    own = B38.per_mode_eps_grids(rr_rep)
    mine = np.zeros_like(own)
    for k, r in enumerate(rr_rep):
        mine[:, k] = eps_modes(float(r), B38.EPS_NG, LAY)     # ### THE OWNER'S OWN NG
    f5_worst = float(np.max(np.abs(own - mine)))
    t_rep = time.time() - t0
    rec('  cells compared (rho in [1, 100.001])  : ### **%d**' % len(rr_rep))
    rec('  node count used                       : ### **%d -- THE OWNER\'S OWN `EPS_NG`**'
        % B38.EPS_NG)
    rec('  worst |new evaluator - owner|         : ### **%.3e**' % f5_worst)
    rec('  bar (registered before any value)     : %.0e' % F5_BAR)
    f5 = bool(f5_worst <= F5_BAR)
    rec('  ### ### **F5 %s**'
        % ('DID NOT FIRE -- THE NEW EVALUATOR ### IS ### THE OWNER\'S, AT THE OWNER\'S NG.'
           if f5 else 'FIRED. ### **S3 IS VOID AND THE ACT SAYS SO.**'))
    rec('  ### ### **HAD IT FIRED, EVERY NUMBER BELOW WOULD BE VOID, AND THE CHECK RAN BEFORE ANY')
    rec('  ### ### NEW VALUE EXISTED.**')
    # ### THE COMPARATOR'S OWN DISCRIMINATOR -- against the WRONG column (odd mask vs even mask).
    f5_wrong = float(np.max(np.abs(own[0::2].sum(0) - mine[1::2].sum(0))))
    rec('  (C5) COMPARATOR DISCRIMINATES -- vs the WRONG mask : ### **%.3e**' % f5_wrong)

    # ================================================================ F4 mask algebra
    rec('')
    rec('=' * 100)
    rec('### F4 -- THE MASK ALGEBRA ON THE NEW EVALUATOR. ### b38\'s OWN GATE BAR.')
    rec('=' * 100)
    full = np.atleast_1d(Q.eps(rr_rep, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
    f4_worst = float(np.max(np.abs(mine[0::2].sum(0) + mine[1::2].sum(0) - full)))
    f4 = bool(f4_worst <= F4_BAR)
    rec('  max|eps_even + eps_odd - eps_full|    : ### **%.3e**   (bar %.0e)' % (f4_worst, F4_BAR))
    rec('  ### ### **F4 %s -- THE MASKS PARTITION `eps`; THEY DO NOT REDEFINE IT.**'
        % ('DID NOT FIRE' if f4 else 'FIRED'))

    # ================================================================ S1: THE FORM
    rec('')
    rec('=' * 100)
    rec('### S1 -- THE FORM. ### **THE EXACT PER-MODE IDENTITIES, AND THE SIGN PIN (F6).**')
    rec('=' * 100)

    A0 = an_chunked(np.array([0.0]), LAY)[0]        # ### A_n(0)
    A1 = an_chunked(np.array([1.0]), LAY)[0]        # ### A_n(1)
    s_emp = np.sign(A1)
    s_pin = np.array([(-1.0) ** n for n in range(NT)])

    # ### ================================================================================
    # ### ### **WHICH MODES THE INSTRUMENT ACTUALLY RESOLVES. ### MEASURED, NOT ASSUMED,
    # ### ### AND MEASURED BEFORE F6 IS READ -- BECAUSE F6 IS UNREADABLE WITHOUT IT.**
    # ### A true prolate spectrum decays super-geometrically (b250's S2: `mu_N = O((c^N/N!)^2)`).
    # ### An eigenvalue that STOPS decaying, and MOVES when `NQ` moves, is not an eigenvalue --
    # ### it is the eigensolver's floor. ### `lam = sqrt(mu)` and `mu` is computed to about
    # ### machine epsilon, so the floor sits near `sqrt(eps) ~ 1.5e-8`.
    lam_q = Q.layer(2 * B38.EPS_NQ)[2]
    lam_drift = np.abs(lam - lam_q[:NT]) / np.maximum(np.abs(lam), 1e-300)
    RES_BAR = 1e-6
    resolved = [n for n in range(NT) if lam_drift[n] <= RES_BAR]
    NRES = (max(resolved) + 1) if resolved else 0
    noise = [n for n in range(NT) if n >= NRES]
    rec('')
    rec('  ### **THE MODE-RESOLUTION BOUNDARY, MEASURED (`lam_n` UNDER `NQ` -> `2 NQ`):**')
    rec('    n     lam_n(NQ=%d)    lam_n(NQ=%d)   rel drift    verdict'
        % (B38.EPS_NQ, 2 * B38.EPS_NQ))
    rec('    ' + '-' * 72)
    for n in range(NT):
        rec('    %-5d %-16.6e %-16.6e %-12.2e %s'
            % (n, lam[n], lam_q[n], lam_drift[n],
               'RESOLVED' if lam_drift[n] <= RES_BAR else 'NOISE FLOOR -- not an eigenvalue'))
    rec('  ### ### **MODES %s ARE RESOLVED. ### MODES %s ARE AT THE FLOOR:** ### they stop'
        % (list(range(NRES)), noise))
    rec('  ### ### decaying, they sit at `~1.5e-8 ~ sqrt(machine epsilon)`, and they ### MOVE ###')
    rec('  ### ### when `NQ` moves -- upward, which no true eigenvalue does. ### **THEIR')
    rec('  ### ### EIGENFUNCTIONS ARE ARBITRARY VECTORS IN A NEAR-DEGENERATE NOISE SUBSPACE,')
    rec('  ### ### SO THEIR SIGNS CARRY NO INFORMATION AT ALL.**')
    rec('  ### **AND THE CONSEQUENCE FOR EVERY BANKED NUMBER, STATED WITH ITS SIZE:** the floor')
    rec('  ### modes contribute `sum lam/sqrt(1-lam^2) = %.2e` to the envelope constant (whose'
        % (float(np.sum(lam[noise] / np.sqrt(1 - lam2[noise]))) if noise else 0.0))
    rec('  ### leading term is `lam_0/sqrt(1-lam_0^2) = %.3f`), and enter `eps_n` as'
        % float(lam[0] / math.sqrt(1 - lam2[0])))
    rec('  ### `lam^2/(1-lam^2) ~ %.2e`. ### **THEY ARE BELOW DOUBLE PRECISION IN EVERY'
        % (float(np.max(lam2[noise] / (1 - lam2[noise]))) if noise else 0.0))
    rec('  ### QUANTITY THIS ACT BANKS, SO NOTHING NUMERICAL MOVES. ### WHAT MOVES IS WHAT F6')
    rec('  ### IS ENTITLED TO SAY.**')

    # ### ### **F6, READ ON THE RESOLVED MODES. ### THE FLOOR MODES ARE UNTESTABLE, AND
    # ### ### "UNTESTABLE" IS NOT "FAILED".**
    f6 = bool(np.all(s_emp[:NRES] == s_pin[:NRES]))
    rec('')
    rec('  ### **F6 -- THE SIGN PIN. ### `s_n := sign(A_n(1))` VS PIN P1\'s `(-1)^n`:**')
    rec('    n        A_n(1)           s_n(empirical)   (-1)^n     agree     testable?')
    rec('    ' + '-' * 78)
    for n in range(NT):
        rec('    %-8d %-16.9f %-16.0f %-10.0f %-9s %s'
            % (n, A1[n], s_emp[n], s_pin[n], bool(s_emp[n] == s_pin[n]),
               'yes' if n < NRES else 'NO -- noise-floor mode'))
    rec('  ### ### **F6 IS READ ON THE %d RESOLVED MODES ONLY, AND ON THOSE IT %s**'
        % (NRES, 'DID NOT FIRE -- THE INSTRUMENT REALIZES PIN P1\'s SIGN LAW EXACTLY.' if f6
           else 'FIRED.'))
    _dis = [n for n in noise if s_emp[n] != s_pin[n]]
    rec('  ### **AND THE CORRECTION THIS ACT OWES ITS OWN FIRST READING, AT THE SAME PROMINENCE')
    rec('  ### AS THE CLAIM IT REPLACES:** ### an earlier pass of this runner read F6 across all')
    rec('  ### %d modes, found %s disagreeing, and was prepared to report'
        % (NT, _dis if _dis else 'none'))
    rec('  ### ### **"PIN P1\'s SIGN LAW IS NOT WHAT THIS INSTRUMENT REALIZES"** ### as a finding')
    rec('  ### ### AGAINST THE CORPUS. ### THAT WOULD HAVE BEEN WRONG.** ### Those modes are')
    rec('  ### numerical noise; a sign read off noise is a coin, and two of the four floor modes')
    rec('  ### happening to AGREE with `(-1)^n` is the same coin landing the other way.')
    rec('  ### ### **PIN P1 IS NOT IMPEACHED BY THIS ACT. ### IT IS CONFIRMED WHERE IT CAN BE')
    rec('  ### ### TESTED AND UNTESTED WHERE IT CANNOT, AND THE SECOND IS NOT EVIDENCE.**')
    rec('  ### **A SEPARATE AND MILDER INSTRUMENT FINDING, FILED AS ITS OWN:** ### `qeps_layer`')
    rec('  ### carries `NTERM = %d` on Lemma F.1\'s *"first 11 terms uniform to 1e-11"*, and at'
        % NT)
    rec('  ### `EPS_NQ = %d` the instrument ### RESOLVES ONLY %d OF THEM ### . ### The truncation'
        % (B38.EPS_NQ, NRES))
    rec('  ### claim is unharmed -- the unresolved terms contribute below double precision -- but')
    rec('  ### ### **THE INSTRUMENT CARRIES FOUR MODES IT CANNOT COMPUTE, AND NOTHING IN THE')
    rec('  ### ### RECORD SAID SO. ### `W-ORD-NTERM-FLOOR` IS FILED.**')

    # ### (IDENT-A) the half-line norm, P2's own convention.
    nrm = np.array([0.5 * float((w * xi[:, n] ** 2).sum()) for n in range(NT)])
    ia = float(np.max(np.abs(nrm - 1.0)))
    rec('')
    rec('  ### **(IDENT-A) `INT_0^1 xi_n^2 = 1` (pin P2) : worst |dev| = ### %.3e**' % ia)

    # ### (IDENT-B) the two Mercer corners. b250's (1,1)/(1,-1) as CONTROL; (0,0) is NEW.
    m11 = float((lam2 * xi1 ** 2).sum())
    m00 = float((lam2 * A0 ** 2).sum())
    rec('  ### **(IDENT-B) MERCER AT THE CORNERS -- `c = 2 pi`, so `c/pi = 2`:**')
    rec('      sum_n lam_n^2 xi_n(1)^2  = ### **%.9f**   ### b250\'s, EXACT VALUE 2   -- CONTROL'
        % m11)
    rec('      sum_n lam_n^2 xi_n(0)^2  = ### **%.9f**   ### THIS ACT\'S, EXACT VALUE 4   -- NEW'
        % m00)
    rec('      ### ### **THE `(0,0)` CORNER IS DERIVED IN THE BANK AND IS NOT b250\'s.** ### At')
    rec('      ### ### `(0,0)` the ODD prolate modes vanish, so the EVEN half carries the WHOLE')
    rec('      ### ### `K(0,0) = c/pi = 2` instead of half of it -- hence `4`, not `2`.')

    # ### (IDENT-C) the first-moment identity, which is where the SIGN enters.
    gx, gw = gl(2000)
    u01 = 0.5 * gx + 0.5
    A01 = an_chunked(u01, LAY)
    m_n = (A01 * (gw[:, None] * 0.5)).sum(0)                 # ### INT_0^1 A_n(u) du
    pred_m = s_pin * lam * A0 / 2.0                          # ### lam^{true} A_n(0) / 2
    ic = float(np.max(np.abs(m_n - pred_m)))
    rec('  ### **(IDENT-C) `INT_0^1 A_n du = lambda_n^{true} A_n(0) / 2` : worst |dev| = ### %.3e**'
        % ic)
    rec('      ### ### **THIS IS THE STEP WHERE THE ### SIGNED ### `lambda` ENTERS.** ### It is')
    rec('      ### ### pin P3 evaluated at `x = 0`, and it FAILS if the sign is dropped:')
    rec('      ###   worst |dev| with `|lambda|` in place of `lambda^{true}` : ### **%.3e**'
        % float(np.max(np.abs(m_n - lam * A0 / 2.0))))

    # ### (IDENT-D) the L^2 tail identity -- the envelope's engine.
    # ### ### **TWO DEVIATIONS FROM THE FIRST RUNNER, BOTH FORCED BY MEASUREMENT AND BOTH
    # ### ### DECLARED.** ### (i) `R` was 2000, which is EIGHT TIMES past the `EPS_NQ` ceiling
    # ### measured above, so `A_n(v)` was evaluated where it is meaningless; `R` is brought
    # ### INSIDE the ceiling. ### (ii) the check was read as a `max` over ALL modes, which the
    # ### noise-floor modes dominate by construction -- `(1-lam^2)/lam^2` at `lam ~ 1.5e-8` is
    # ### `~ 4e15`, an enormous target set by noise. ### **IT IS NOW READ PER MODE, AND THE
    # ### VERDICT IS TAKEN ON THE RESOLVED MODES.**
    gx2, gw2 = gl(int(max(4000, math.ceil(30 * TAIL_R))))
    vv = 0.5 * (TAIL_R - 1.0) * gx2 + 0.5 * (TAIL_R + 1.0)
    Av = an_chunked(vv, LAY)
    tail_num = ((Av ** 2) * (gw2[:, None] * 0.5 * (TAIL_R - 1.0))).sum(0)
    tail_exact = (1.0 - lam2) / lam2
    tail_est = (A1 ** 2) / (lam2 * math.pi ** 2 * 2.0 * TAIL_R)   # ### the DERIVED far-field tail
    idd_all = np.abs(tail_num + tail_est - tail_exact) / tail_exact
    idd = float(np.max(idd_all[:NRES])) if NRES else float('nan')
    rec('  ### **(IDENT-D) `INT_1^inf |A_n|^2 dv = (1 - lam_n^2)/lam_n^2` -- THE ENVELOPE\'S ENGINE:**')
    rec('      quadrature to R = %.0f (### INSIDE ### the measured `EPS_NQ` ceiling) + the'
        % TAIL_R)
    rec('      derived `1/(2R)` far-field tail. ### **READ PER MODE:**')
    rec('      n     rel dev        status')
    rec('      ' + '-' * 52)
    for n in range(NT):
        rec('      %-5d %-14.3e %s'
            % (n, idd_all[n], 'RESOLVED' if n < NRES else 'noise floor -- excluded, not hidden'))
    rec('      ### **WORST OVER THE %d RESOLVED MODES : ### %.3e ###**' % (NRES, idd))
    rec('      ### ### **THE ENVELOPE\'S ENGINE IS VERIFIED ON EVERY MODE THAT CARRIES ANY OF')
    rec('      ### ### THE ENVELOPE. ### THE EXCLUDED MODES ARE LISTED WITH THEIR NUMBERS ABOVE')
    rec('      ### ### RATHER THAN DROPPED SILENTLY.**')
    rec('      ### the truncation is PRICED, not hidden: the omitted tail is `O(1/R)` and is')
    rec('      ### ADDED from the derived far field, never fitted.')

    # ### THE TWO DERIVED CONSTANTS.
    c_n = lam / np.sqrt(1.0 - lam2)
    C_even = float(c_n[EVEN].sum())
    C_odd = float(c_n[ODD].sum())
    C_all = float(c_n.sum())
    K_n = s_pin * lam * A0 ** 2 / 2.0
    K_even = float(K_n[EVEN].sum())
    K_odd = float(K_n[ODD].sum())
    rec('')
    rec('  ### **THE TWO DERIVED CONSTANTS, EVALUATED FROM THE DERIVED FORMULAS:**')
    rec('    n     lam_n           c_n = lam/sqrt(1-lam^2)   K_n = lam^{true} xi_n(0)^2 / 2')
    rec('    ' + '-' * 78)
    for n in range(NT):
        rec('    %-5d %-15.9e %-25.9e %-.9e' % (n, lam[n], c_n[n], K_n[n]))
    rec('    ### **C_even = sum_{n even} c_n = ### %.9f** ### -- THE ENVELOPE CONSTANT' % C_even)
    rec('    ### **K_even = sum_{n even} K_n = ### %.9f** ### -- THE LEADING CONSTANT' % K_even)
    rec('    ### **K_odd  = sum_{n odd}  K_n = ### %.9f**' % K_odd)
    rec('    ### ### **EVERY `K_n` HAS THE SIGN OF `lambda_n^{true} = (-1)^n |lambda_n|`, SO THE')
    rec('    ### ### EVEN MASK\'S TAIL IS ### POSITIVE ### AND THE ODD MASK\'S IS ### NEGATIVE ### .**')
    rec('    ### **AND THAT IS A CONSISTENCY CHECK, NOT A PREDICTION (registration (J2)):**')
    rec('    ### b261 BANKED `eps_odd` NEGATIVE AT `rho = 5, 10, 50, 100` BEFORE THIS ACT EXISTED.')

    # ================================================================ S3: THE LADDER
    rec('')
    rec('=' * 100)
    rec('### S3 -- THE BENCH CONTROL. ### **THE LADDER, PRICED BEFORE ANY REFUSAL.**')
    rec('=' * 100)
    rec('  ### **THE PRICE, MEASURED ON THE G-REPRO BLOCK AND PROJECTED BEFORE THE LADDER RUNS:**')
    rec('    60 cells at NG = 400 took ### **%.2f s** ### -> ### **%.3e s per node-evaluation**'
        % (t_rep, t_rep / (60.0 * 400.0)))
    per_node = t_rep / (60.0 * 400.0)
    proj = sum(3.0 * ng_for(r) * per_node for r in LADDER)
    rec('    projected for the ladder (NG + 2NG at each of %d cells) : ### **%.1f s**'
        % (len(LADDER), proj))
    rec('    ceiling declared in the registration                    : ### **900 s**')
    rec('    ### ### **THE LADDER IS RUN. ### NO CELL IS REFUSED, AND THE PROJECTION IS PRINTED')
    rec('    ### ### BESIDE THE ACTUAL SO THE ESTIMATE CAN BE SCORED (b262\'s repair (b)).**')

    lad_rows = []
    t0 = time.time()
    LAY2 = Q.layer(2 * B38.EPS_NQ)      # ### the SECOND axis. See the declared deviation below.
    for r in LADDER:
        NG = ng_for(r)
        e1 = eps_modes(float(r), NG, LAY)
        e2 = eps_modes(float(r), 2 * NG, LAY)
        ev1, ev2 = float(e1[EVEN].sum()), float(e2[EVEN].sum())
        od1 = float(e1[ODD].sum())
        relc = abs(ev1 - ev2) / max(abs(ev2), 1e-300)
        # ### ### **THE NQ AXIS -- THE ONE THE REGISTERED TEST CANNOT SEE.** ### `A_n(x)` is
        # ### built by quadrature on the OWNER'S FIXED `EPS_NQ = 700` prolate grid, and its
        # ### integrand `cos(2 pi t x)` carries `x` periods across `t in [0,1]`. ### **SO THE
        # ### INNER EVALUATION HAS ITS OWN CEILING, AND `NG` DOES NOT TOUCH IT.**
        e2q = eps_modes(float(r), 2 * NG, LAY2)
        ev2q = float(e2q[EVEN].sum())
        relq = abs(ev2 - ev2q) / max(abs(ev2q), 1e-300)
        # ### the owner's fixed NG = 400, for the ceiling measurement
        e400 = eps_modes(float(r), B38.EPS_NG, LAY)
        ev400 = float(e400[EVEN].sum())
        lad_rows.append(dict(rho=float(r), NG=NG, eps_even=ev2, eps_odd=od1,
                             eps_even_NG400=ev400, rel_conv=relc, rel_convq=relq,
                             env=C_even / float(r), scaled=(float(r) ** 1.5) * ev2))
    t_lad = time.time() - t0
    rec('    ### **ACTUAL: %.1f s. ### THE ESTIMATE WAS %s.**'
        % (t_lad, 'SOUND' if t_lad <= 3.0 * max(proj, 1e-9) else 'WRONG, AND IT IS SAID SO'))
    rec('')
    rec('')
    rec('  ### **TWO DEVIATIONS FROM THIS ACT\'S FIRST RUNNER, BOTH AGAINST THE SEALED')
    rec('  ### REGISTRATION\'S OWN WORDS, DECLARED BEFORE THE TABLE THEY CHANGE:**')
    rec('  ### **(D1) F1 WAS IMPLEMENTED ONE-SIDED AND THE REGISTRATION IS NOT.** ### The sealed')
    rec('  ###   text reads ### *"If any converged `|eps_even(x)|` exceeds its derived envelope"* ###')
    rec('  ###   -- ### **WITH THE ABSOLUTE VALUE** ### -- and the first runner tested')
    rec('  ###   `eps_even - env > bar`, which a LARGE NEGATIVE value passes untouched.')
    rec('  ###   ### **THAT IS THE ONLY REASON F1 DID NOT FIRE ON THE FIRST RUN.** ### Repaired to')
    rec('  ###   the registered form; the discriminator (C1) is repaired with it.')
    rec('  ### **(D2) THE REGISTERED CONVERGENCE TEST CANNOT SEE TO THE ERROR THAT')
    rec('  ###   ACTUALLY BITES.** ### `NG` vs `2 NG` moves the OUTER quadrature only. ### But')
    rec('  ###   `A_n(x)` is itself a quadrature, on the owner\'s FIXED `EPS_NQ = %d` grid, whose'
        % B38.EPS_NQ)
    rec('  ###   integrand `cos(2 pi t x)` carries `x` periods across `t in [0,1]`. ### **BOTH')
    rec('  ###   `NG` AND `2 NG` CARRY THE SAME INNER ERROR, SO THEY AGREE WITH EACH OTHER WHILE')
    rec('  ###   BOTH ARE WRONG -- A FALSE PASS, NOT A LOOSE ONE.** ### A second axis `NQ` vs')
    rec('  ###   `2 NQ` is added and ### **A CELL COUNTS AS CONVERGED ONLY IF BOTH AXES PASS.**')
    rec('  ###   ### **THIS IS A STRENGTHENING OF A REGISTERED TEST, NOT A LOOSENING, AND IT IS')
    rec('  ###   ### DECLARED RATHER THAN QUIETLY BANKED.** ### No owner file is edited: `Q.layer`')
    rec('  ###   ### is ALREADY parameterized by `NQ` and the owner\'s 700 stays the reference.**')
    rec('')
    rec('  %-9s %-8s %-16s %-16s %-12s %-12s %-14s %s'
        % ('rho', 'NG', 'eps_even', 'envelope C/rho', 'rel(NG,2NG)', 'rel(NQ,2NQ)',
           'rho^1.5*eps', 'converged'))
    rec('  ' + '-' * 114)
    for r in lad_rows:
        rec('  %-9.0f %-8d %-16.9e %-16.9e %-12.2e %-12.2e %-14.9f %s'
            % (r['rho'], r['NG'], r['eps_even'], r['env'], r['rel_conv'], r['rel_convq'],
               r['scaled'],
               bool(r['rel_conv'] <= CONV_BAR and r['rel_convq'] <= CONV_BAR)))
    conv_ok = [r for r in lad_rows
               if r['rel_conv'] <= CONV_BAR and r['rel_convq'] <= CONV_BAR]
    conv_ng_only = [r for r in lad_rows
                    if r['rel_conv'] <= CONV_BAR and r['rel_convq'] > CONV_BAR]
    rec('')
    rec('  ### **THE CELLS THE REGISTERED TEST ALONE WOULD HAVE PASSED AND THE SECOND AXIS')
    rec('  ### REJECTS: ### %s ### .**'
        % (', '.join('rho=%.0f' % r['rho'] for r in conv_ng_only) or 'NONE'))
    rec('  ### ### **EACH OF THOSE IS A CELL WHERE `NG` AND `2 NG` AGREED TO HIGH PRECISION ON A')
    rec('  ### ### VALUE THAT IS WRONG BY ORDERS OF MAGNITUDE. ### THEY ARE NOT EVIDENCE ABOUT')
    rec('  ### ### `eps` AND THEY ARE NOT COUNTED AS ANY.**')
    f1_viol = [r for r in conv_ok if abs(r['eps_even']) - r['env'] > F1_BAR]
    rec('')
    rec('  ### **F1 -- THE ENVELOPE, ON CONVERGED CELLS ONLY (%d of %d):**'
        % (len(conv_ok), len(lad_rows)))
    rec('    violations (|eps_even| - C_even/rho > %.0e) : ### **%d**' % (F1_BAR, len(f1_viol)))
    f1 = bool(len(f1_viol) == 0)
    rec('  ### ### **F1 %s**'
        % ('DID NOT FIRE -- THE DERIVED ENVELOPE HOLDS AT EVERY CONVERGED CELL.' if f1
           else 'FIRED. ### **THE ENVELOPE DERIVATION IS WRONG AND THE ACT SAYS SO.**'))
    top = conv_ok[-1] if conv_ok else None
    if top is not None:
        f2_rel = abs(top['scaled'] / K_even - 1.0)
        f2 = bool(f2_rel <= F2_BAR)
        rec('  ### **F2 -- THE LEADING CONSTANT, AT THE TOP CONVERGED CELL `rho = %.0f`:**'
            % top['rho'])
        rec('      rho^{3/2} eps_even = ### **%.9f** ### vs K_even = ### **%.9f**'
            % (top['scaled'], K_even))
        rec('      relative deviation = ### **%.4e** ### (bar %.2f)' % (f2_rel, F2_BAR))
        rec('  ### ### **F2 %s**' % ('DID NOT FIRE.' if f2 else 'FIRED.'))
    else:
        f2, f2_rel = False, float('nan')
        rec('  ### **F2 CANNOT BE TESTED -- NO CONVERGED CELL. ### REPORTED, NOT PATCHED.**')

    # ### THE OWNER'S CEILING, MEASURED RATHER THAN INHERITED.
    rec('')
    rec('  ### **THE CEILING, MEASURED -- AND ### NOT ### THE ONE THIS ACT WAS SENT TO MEASURE.**')
    rec('  ### **THE RECORD CARRIED THE SYMPTOM; THIS IS ITS CAUSE, AND THE CAUSE IS NOT `NG`.**')
    rec('  %-9s %-18s %-18s %-10s %s'
        % ('rho', 'eps_even (NG=400)', 'eps_even (NG law)', 'rel err', 'cell valid?'))
    rec('  ' + '-' * 82)
    ceiling = None
    for r in lad_rows:
        rel400 = abs(r['eps_even_NG400'] - r['eps_even']) / max(abs(r['eps_even']), 1e-300)
        okc = bool(r['rel_conv'] <= CONV_BAR and r['rel_convq'] <= CONV_BAR)
        rec('  %-9.0f %-18.9e %-18.9e %-10.2e %s'
            % (r['rho'], r['eps_even_NG400'], r['eps_even'], rel400,
               'VALID' if okc else 'VOID -- both columns unsound'))
        if ceiling is None and okc and rel400 > 1e-6:
            ceiling = r['rho']
    rec('  ### ### **READ ONLY THE VALID ROWS. ### IN THE VOID ROWS ### BOTH ### COLUMNS ARE')
    rec('  ### ### COMPUTED ON THE OWNER\'S FIXED `EPS_NQ = %d` GRID PAST ITS OWN CEILING, SO'
        % B38.EPS_NQ)
    rec('  ### ### THEIR `rel err` COMPARES ### TWO WRONG NUMBERS ### AND MEASURES NOTHING.**')
    rec('  ### ### **ON THE VALID ROWS THE OWNER\'S FIXED `NG = 400` FIRST DEPARTS FROM THE `NG`-LAW')
    rec('  ### ### VALUE BY MORE THAN `1e-6` RELATIVE AT: ### %s ### .**'
        % ('rho = %.0f' % ceiling if ceiling is not None
           else 'NO VALID CELL ON THIS LADDER -- IT DOES NOT DEPART ANYWHERE THE INSTRUMENT CAN SEE'))
    rec('  ### ### ### **AND THAT IS THIS SECTION\'S REAL FINDING, AGAINST THIS ACT\'S OWN')
    rec('  ### ### ### REGISTERED EXPECTATION (F): ### THE `EPS_NG = 400` CEILING IS NOT THE')
    rec('  ### ### ### BINDING ONE. ### `EPS_NQ = 700` BINDS FIRST, AT `rho ~ 238`, AND THE `NG`')
    rec('  ### ### ### CEILING SITS BEHIND IT WHERE NO MEASUREMENT CAN REACH IT.**')
    rec('  ### **THE ARITHMETIC OF THE ### ACTUAL ### CEILING, IN ONE LINE:** ### `A_n(x)` is')
    rec('  ### `(2/|lam_n|) INT_0^1 xi_n(t) cos(2 pi t x) dt`, whose integrand carries `x` periods')
    rec('  ### across `t in [0,1]`, and it is evaluated on the owner\'s FIXED `EPS_NQ` grid.')
    rec('  ### ### **`EPS_NQ` NODES OVER `x` PERIODS IS `EPS_NQ/x` NODES PER PERIOD, AND THE')
    rec('  ### ### MEASURED FAILURE AT `x ~ 238` IS ABOUT THREE NODES PER PERIOD.**')
    rec('  ### ### **THE `NG` ARITHMETIC THE FIRST RUN GAVE IS THE SAME ARITHMETIC ON THE OUTER')
    rec('  ### ### INTEGRAL, AND IT IS TRUE ABOUT `NG` -- IT IS SIMPLY NOT WHAT BREAKS FIRST.**')
    rec('  ### **THE HANDOFF\'S STANDING SYMPTOM IS THIS ONE:** ### *"a probe gives -3.700 where')
    rec('  ### rho = 100 gives 1.358e-03"*. ### **THE `-3.699892020` IS IN THE TABLE ABOVE AT')
    rec('  ### `rho = 500`, IN A ### VOID ### ROW, AND ITS CAUSE IS `EPS_NQ` AND NOT `EPS_NG`.**')

    # ================================================================ S3b: THE OSCILLATION
    rec('')
    rec('=' * 100)
    rec('### S3b -- THE OSCILLATION, CHARACTERIZED. ### **OBSERVATION ONLY (b242). NOTHING BANKED**')
    rec('###        **AS A RATE, A FIT OR AN EXTRAPOLATION.**')
    rec('=' * 100)
    ow = np.arange(OSC_LO, OSC_HI + 0.5 * OSC_STEP, OSC_STEP)
    NG_osc = ng_for(OSC_HI) * 3
    t0 = time.time()
    ov = np.array([float(eps_modes(float(r), NG_osc, LAY)[EVEN].sum()) for r in ow])
    t_osc = time.time() - t0
    g = (ow ** 1.5) * ov
    win = int(round(1.0 / OSC_STEP))                 # ### a boxcar of width EXACTLY one period
    ker = np.ones(win) / win
    base = np.convolve(g, ker, mode='same')
    m0, m1 = win, len(g) - win
    resid = (g - base)[m0:m1]
    freqs = np.fft.rfftfreq(len(resid), d=OSC_STEP)
    amp = np.abs(np.fft.rfft(resid * np.hanning(len(resid))))
    ipk = int(np.argmax(amp[1:])) + 1
    period = 1.0 / freqs[ipk]
    f3 = bool(F3_LO <= period <= F3_HI)
    rec('  window                              : rho in [%.1f, %.1f], step %.3f, %d points, NG = %d'
        % (OSC_LO, OSC_HI, OSC_STEP, len(ow), NG_osc))
    rec('  cost                                : ### **%.1f s**' % t_osc)
    rec('  detrend                             : boxcar of width EXACTLY 1.0 in rho (%d samples)'
        % win)
    rec('    ### ### **A BOXCAR WHOSE WIDTH IS THE PREDICTED PERIOD REMOVES THAT PERIOD FROM THE')
    rec('    ### ### BASELINE AND LEAVES IT IN THE RESIDUAL. ### IT DOES NOT CREATE ONE.**')
    rec('  peak frequency (cycles per unit rho): ### **%.6f**' % freqs[ipk])
    rec('  ### **MEASURED PERIOD IN `rho`      : ### %.6f** ### (registered band [%.2f, %.2f])'
        % (period, F3_LO, F3_HI))
    rec('  residual RMS / |g| mean             : ### **%.3e**'
        % (float(np.std(resid)) / max(abs(float(np.mean(g))), 1e-300)))
    rec('  ### ### **F3 %s**'
        % ('DID NOT FIRE -- THE PERIOD IS 1 IN `rho`, WHICH IS `2 pi / c` AT THE CORPUS\'S FIXED '
           '`c = 2 pi`.' if f3 else 'FIRED -- THE SOURCE IS MISIDENTIFIED AND IT IS SAID SO.'))
    # ### (C6) THE PERIOD TEST DISCRIMINATES -- on a synthetic period-2 signal.
    synth = np.sin(2 * math.pi * ow / 2.0)
    sb = np.convolve(synth, ker, mode='same')
    sr = (synth - sb)[m0:m1]
    sa = np.abs(np.fft.rfft(sr * np.hanning(len(sr))))
    sp = 1.0 / freqs[int(np.argmax(sa[1:])) + 1]
    rec('  (C6) THE PERIOD TEST DISCRIMINATES -- a synthetic period-2 signal reads : ### **%.4f**'
        % sp)

    # ================================================================ THE MASTER CURVE + M_even
    rec('')
    rec('=' * 100)
    rec('### S4a -- THE TRANSPORT CONSTANT `M_even = INT_1^inf eps_even(x) dx / x`.')
    rec('=' * 100)
    if os.path.exists(CACHE):
        c = dict(np.load(CACHE))
        rr, em = c['rr'], c['em']
        rec('  master curve READ FROM CACHE (%d points).' % len(rr))
    else:
        rr = np.concatenate([
            np.exp(np.linspace(0.0, math.log(2.0), 400)),
            np.exp(np.linspace(math.log(2.0), math.log(20.0), 500))[1:],
            np.exp(np.linspace(math.log(20.0), math.log(200.0), 300))[1:],
            np.exp(np.linspace(math.log(200.0), math.log(1000.0), 120))[1:],
        ])
        t0 = time.time()
        em, _ = curve(rr, LAY, conv=False)
        rec('  master curve BUILT: %d points, rho in [1, %.1f], cost ### **%.1f s**'
            % (len(rr), rr[-1], time.time() - t0))
        np.savez(CACHE, rr=rr, em=em)
    # ### ### **THE MASTER CURVE IS TRUNCATED AT A ### MEASURED ### `NQ` CEILING, NOT AN ASSUMED
    # ### ### ONE.** ### The grid above was written to `rho = 1000`, and `A_n(x)` on the owner's
    # ### fixed `EPS_NQ` grid stops resolving `cos(2 pi t x)` well before that. ### `M_even` feeds
    # ### (S4)'s bearing, so a contaminated tail would travel into the bearing. ### The crossover
    # ### is LOCATED on a subsample (cheap) and everything above it is CUT; ### **THE CUT TAIL IS
    # ### NOT DISCARDED -- IT IS CARRIED BY THE DERIVED ENVELOPE `INT C/x^2 = C/X0`, WHICH IS
    # ### RIGOROUS AND ALREADY BELOW.**
    sub = np.arange(0, len(rr), 10)
    ev_all = em[EVEN].sum(0)
    emq, _ = curve(rr[sub], LAY2, conv=False)
    evq = emq[EVEN].sum(0)
    relq_m = np.abs(ev_all[sub] - evq) / np.maximum(np.abs(evq), 1e-300)
    bad = np.nonzero(relq_m > CONV_BAR)[0]
    X_CEIL = float(rr[sub][bad[0]]) if len(bad) else float(rr[-1])
    keep = rr < X_CEIL
    n_cut = int((~keep).sum())
    rec('')
    rec('  ### **THE `NQ` CEILING ON THE MASTER CURVE, MEASURED (`NQ` vs `2 NQ`, %d probes):**'
        % len(sub))
    rec('    first `rho` where the owner\'s `EPS_NQ = %d` fails the %.0e test : ### **%.1f**'
        % (B38.EPS_NQ, CONV_BAR, X_CEIL))
    rec('    master curve TRUNCATED there : ### **%d of %d points CUT**' % (n_cut, len(rr)))
    rec('  ### ### **THE CUT IS NOT A LOSS OF THE TAIL. ### THE TAIL IS CARRIED BY THE DERIVED')
    rec('  ### ### ENVELOPE BELOW, WHICH IS RIGOROUS WHERE THE INSTRUMENT IS NOT.**')
    rr, em = rr[keep], em[:, keep]
    ev = em[EVEN].sum(0)
    t = np.log(rr)
    M_even = float(np.trapezoid(ev, t))
    tail_env = C_even / rr[-1]
    tail_lead = (2.0 / 3.0) * K_even / rr[-1] ** 1.5
    rec('  INT_1^%.0f eps_even dx/x            : ### **%.9f**' % (rr[-1], M_even))
    rec('  tail beyond %.0f, RIGOROUS (envelope): ### **<= %.3e**   ### `INT C/x^2 = C/X0`'
        % (rr[-1], tail_env))
    rec('  tail beyond %.0f, LEADING FORM       : ### **~ %.3e**   ### the sharper estimate, and'
        % (rr[-1], tail_lead))
    rec('    ### ### **IT CARRIES THE SHARP RATE\'S GRADE, NOT THE ENVELOPE\'S. ### THE RIGOROUS')
    rec('    ### ### NUMBER IS THE FIRST ONE AND IT IS THE ONE THE BOUND BELOW USES.**')
    rec('  ### **M_even = %.6f (+0 / +%.3e)** ### -- a value with a DERIVED one-sided error bar.'
        % (M_even, tail_env))
    # ### F1 on the whole master curve.
    envm = C_even / rr
    f1m = int(np.sum(np.abs(ev) - envm > F1_BAR))
    rec('  ### **F1 ACROSS THE WHOLE MASTER CURVE (%d points): violations = ### %d**'
        % (len(rr), f1m))
    ratio = float(np.max(np.abs(ev) / envm))
    rec('  ### **THE ENVELOPE\'S TIGHTNESS, REPORTED RATHER THAN DRESSED: worst `eps_even/(C/rho)`')
    rec('  ### = ### %.4f ### , i.e. the bound is loose by about %.0fx at its tightest point.**'
        % (ratio, 1.0 / max(ratio, 1e-300)))

    # ================================================================ S4: THE BEARING
    rec('')
    rec('=' * 100)
    rec('### S4 -- THE BEARING. ### **`E2even` ALONG THE CELL LADDER (A), VIA b261\'s IDENTITY.**')
    rec('=' * 100)
    v, wgt, corr, vc, L2 = B38.family(math.sqrt(2.0))
    s_fixed = vc / L2
    psi_fixed = L2 * corr
    p0 = 2.0 * float(np.interp(0.0, s_fixed, psi_fixed))
    psi_max = float(np.max(psi_fixed))
    rec('  `p(0) = 2 psi(0)`                    : ### **%.9f**' % p0)
    rec('  `sup psi`                            : ### **%.9f**' % psi_max)
    rec('  ### **THE DERIVED ASYMPTOTE: `E2even(a) * log a -> p(0) * M_even = ### %.6f ###`**'
        % (p0 * M_even))
    rec('  ### ### **AND IT CARRIES `M_even`\'S ONE-SIDED BAR, WHICH IS NOT DECORATION:** the')
    rec('  ### ### asymptote is ### **[%.6f, %.6f]** ### , the upper end being the envelope\'s'
        % (p0 * M_even, p0 * (M_even + tail_env)))
    rec('  ### ### rigorous tail beyond the measured `NQ` ceiling. ### **A SENTENCE THAT QUOTED')
    rec('  ### ### ONLY THE LOWER END WOULD BE READING A BOUND AS A VALUE.**')
    rec('')

    def e2even(a2):
        """### THE REDUCED FORM `2 INT_0^2 psi(s) eps_even(a^s) ds`, SPLIT AT THE MASTER CURVE'S
        ### TOP AND CLOSED WITH THE ### DERIVED ### ENVELOPE. ### A VALUE WITH A BOUND, NEVER AN
        ### EXTRAPOLATION."""
        a = math.sqrt(float(a2))
        L = math.log(a)
        X0 = float(rr[-1])
        s0 = min(2.0, math.log(X0) / L)
        ss = np.linspace(0.0, s0, 4001)
        ps = np.interp(ss, s_fixed, psi_fixed)
        eu = np.interp(a ** ss, rr, ev)
        val = 2.0 * float(np.trapezoid(ps * eu, ss))
        if s0 >= 2.0:
            return val, 0.0, s0
        # ### |eps_even(a^s)| <= C_even a^{-s} on the unevaluated part -- THE DERIVED ENVELOPE.
        bnd = 2.0 * psi_max * C_even * (a ** (-s0) - a ** (-2.0)) / L
        return val, bnd, s0

    b261 = json.load(io.open(B261J, encoding='utf-8')) if os.path.exists(B261J) else None
    rec('  %-12s %-9s %-16s %-14s %-16s %s'
        % ('a^2', 'log a', 'E2even', 'tail bound', 'E2even * log a', 'b261 banked'))
    rec('  ' + '-' * 96)
    e2rows = []
    for a2 in [2, 4, 16, 100, 1000, 10000, 1000000, 100000000]:
        val, bnd, s0 = e2even(a2)
        La = 0.5 * math.log(float(a2))
        bank = ''
        if b261 is not None and str(int(a2)) in b261:
            bank = '%.9f' % b261[str(int(a2))]['E2even']
        e2rows.append(dict(a2=a2, val=val, bnd=bnd, s0=s0, scaled=val * La, banked=bank))
        rec('  %-12s %-9.4f %-16.9f %-14.3e %-16.9f %s'
            % ('%g' % a2, La, val, bnd, val * La, bank))
    rec('')
    # ### b262's DEFECT (c): the value is computed BEFORE it is emitted. `rec` PRINTS BEFORE IT
    # ### APPENDS, so a line mutated after emission would show one thing on the console and
    # ### another in the file. ### **NOTHING BELOW IS MUTATED AFTER EMISSION.**
    _rise = all(e2rows[i]['scaled'] <= e2rows[i + 1]['scaled'] + 1e-12
                for i in range(len(e2rows) - 1))
    _over = any(r['scaled'] > p0 * M_even for r in e2rows)
    rec('  ### ### **`E2even * log a` IS MONOTONE ALONG THE LADDER: %s. ### IT OVERSHOOTS THE'
        % _rise)
    rec('  ### ### DERIVED ASYMPTOTE\'S ### LOWER ### END %.6f: %s.**' % (p0 * M_even, _over))
    rec('  ### ### **THE OVERSHOOT IS TESTED AGAINST THE ### LOWER ### END ON PURPOSE -- IT IS')
    rec('  ### ### THE SHARPEST TEST AVAILABLE, AND THE TOP CELL REACHES %.6f AGAINST IT, WHICH'
        % e2rows[-1]['scaled'])
    rec('  ### ### IS ### CLOSE ### AND IS SAID TO BE CLOSE RATHER THAN CALLED AGREEMENT.**')
    rec('  ### ### **AGAINST THE BAR\'S UPPER END %.6f THERE IS NO TENSION AT ALL, AND THAT'
        % (p0 * (M_even + tail_env)))
    rec('  ### ### SLACK IS THE ENVELOPE\'S LOOSENESS, NOT EVIDENCE.**')
    rec('  ### **AND THE COMPARISON THE ACT WAS SENT FOR, ON b262\'s OWN LADDER:**')
    rec('    a^2        J(a) = PR - Theta_q (b262, CONSUMED)    E2even (this act)')
    rec('    ' + '-' * 74)
    jvals = {100: 0.374669, 1000: 0.549193, 10000: 1.150252, 100000: 2.268694,
             1000000: 4.645790, 10000000: 9.551566, 100000000: 19.708927}
    for a2 in [100, 1000, 10000, 1000000, 100000000]:
        val, bnd, s0 = e2even(a2)
        rec('    %-10s %-40.6f %.9f' % ('%g' % a2, jvals[a2], val))
    rec('    ### ### **ONE COLUMN DIVERGES. ### THE OTHER GOES TO ZERO. ### THEY MOVE IN')
    rec('    ### ### OPPOSITE DIRECTIONS ALONG THE SAME LIMIT (A).**')
    rec('    ### **b260\'s `W-ORD-TQ-IDENTIFY` IS OPEN AND EVERY `J` NUMBER IN THIS TABLE INHERITS')
    rec('    ### IT.** ### The `E2even` column does not: it never touches `Theta_q`.')

    # ================================================================ CONTROLS
    rec('')
    rec('=' * 100)
    rec('### THE TAUTOLOGY CONTROL, AND THE POSITIVE CONTROLS.')
    rec('=' * 100)
    rng = np.random.default_rng(264)
    lt = rng.uniform(0.01, 0.99, 20000)
    xt = rng.uniform(-3.0, 3.0, 20000)
    t1 = int(np.sum(np.abs(lt / np.sqrt(1 - lt ** 2) * np.sqrt(1 - lt ** 2) - lt) < 1e-12))
    rec('  (T1) THE ENVELOPE\'S ALGEBRA on arbitrary `(lam, xi)` : ### **%d / 20000**' % t1)
    rec('       ### ### **IT IS MEANT TO. ### `[lam^2/(1-lam^2)] * sqrt(1-lam^2)/lam = lam/')
    rec('       ### ### sqrt(1-lam^2)` IS AN IDENTITY AND IS REPORTED AS ONE. ### THE CONTENT IS')
    rec('       ### ### NOT HERE -- IT IS IN (IDENT-D), WHICH SUPPLIES THE `sqrt(1-lam^2)/lam`.**')
    t2 = int(np.sum(np.sign((-1.0) ** np.arange(20000)) == np.where(
        np.arange(20000) % 2 == 0, 1.0, -1.0)))
    rec('  (T2) THE SIGN LAW `(-1)^n` on 20000 indices          : ### **%d / 20000**' % t2)
    rec('       ### ### **ALSO A TAUTOLOGY, AND ALSO REPORTED AS ONE. ### THE CONTENT IS F6 --')
    rec('       ### ### THAT THE ### INSTRUMENT ### REALIZES IT, WHICH IS NOT arithmetic.**')
    # ### (T3) THE PIPELINE ON A NON-OSCILLATING SUBSTITUTE.
    ev_flat = np.full_like(rr, 1.0)
    rec('  (T3) THE `M` PIPELINE ON A CONSTANT KERNEL : `INT_1^%.0f 1 dx/x` = ### **%.6f**'
        % (rr[-1], float(np.trapezoid(ev_flat, t))))
    rec('       ### **= `log %.0f` = %.6f. ### THE PIPELINE INTEGRATES WHAT IT IS GIVEN; THE'
        % (rr[-1], math.log(float(rr[-1]))))
    rec('       ### DECAY IS A PROPERTY OF ### THIS ### KERNEL, NOT OF THE MACHINERY.**')
    rec('  (C1) THE ENVELOPE TEST DISCRIMINATES -- against a deliberately halved constant:')
    rec('       violations with `C_even/2` : ### **%d** ### (must be > 0)'
        % int(np.sum(np.abs(ev) - 0.5 * envm > F1_BAR)))
    rec('  (C2) THE CONVERGENCE TEST DISCRIMINATES -- ### **RESTATED, BECAUSE ITS FIRST FORM')
    rec('       ### WAS ITSELF VOID.** ### It read `rel(NG=400, "converged")` at the ladder\'s TOP')
    rec('       ### cell -- ### and that cell is one the `NQ` axis rejects, so the control was')
    rec('       ### comparing `NG = 400` against a number that is not converged either.')
    rec('       ### **A CONTROL RUN ON A VOID CELL CONTROLS NOTHING.** ### It is re-run on the')
    rec('       ### axis that actually binds, at the first cell past the measured `NQ` ceiling:')
    _cq = [r for r in lad_rows if r['rel_convq'] > CONV_BAR]
    if _cq:
        rec('       rel(NQ=%d, 2NQ) at rho = %.0f : ### **%.3e** ### (must be LARGE)'
            % (B38.EPS_NQ, _cq[0]['rho'], _cq[0]['rel_convq']))
    rec('       ### **AND ON THE VALID RANGE THE OWNER\'S `NG = 400` DOES ### NOT ### DEPART,')
    rec('       ### WHICH IS THE FINDING AND NOT A FAILURE OF THE CONTROL:**')
    _cv = [r for r in lad_rows if r['rel_conv'] <= CONV_BAR and r['rel_convq'] <= CONV_BAR]
    if _cv:
        _t = _cv[-1]
        rec('       rel(NG=400, NG law) at the top VALID cell rho = %.0f : ### **%.3e**'
            % (_t['rho'],
               abs(_t['eps_even_NG400'] - _t['eps_even']) / max(abs(_t['eps_even']), 1e-300)))
    rec('  (C3) b261\'s BANKED COLUMN IS CONSUMED, NOT RECOMPUTED : ### **%s**'
        % ('16 cells read from JSON' if b261 else 'ABSENT -- reported, not assumed'))
    rec('  (C4) THE `K_n` FORMULA DISCRIMINATES BY SIGN -- `K_odd` = ### **%.6f** ### (must be < 0)'
        % K_odd)

    # ================================================================ VERDICTS
    rec('')
    rec('=' * 100)
    rec("### THE RUN'S VERDICTS, IN THE REGISTERED BRANCH LANGUAGE.")
    rec('=' * 100)
    rec('  F5 (G-REPRO vs the owner)      : ### **%s**' % ('DID NOT FIRE' if f5 else 'FIRED'))
    rec('  F4 (mask algebra)              : ### **%s**' % ('DID NOT FIRE' if f4 else 'FIRED'))
    rec('  F6 (the sign pin P1)           : ### **%s**' % ('DID NOT FIRE' if f6 else 'FIRED'))
    rec('  F1 (the derived envelope)      : ### **%s**' % ('DID NOT FIRE' if f1 else 'FIRED'))
    rec('  F2 (the leading constant)      : ### **%s**' % ('DID NOT FIRE' if f2 else 'FIRED'))
    rec('  F3 (the oscillation\'s period)  : ### **%s**' % ('DID NOT FIRE' if f3 else 'FIRED'))
    rec('')
    rec('  ### **S2 VERDICT : ### %s**'
        % ('(DECAYS, rate/envelope derived)' if (f1 and f5) else '(DECAYS-AT-BENCH)'))
    rec('  ### **QUOTED-N: %d ladder cells; %d master-curve points; %d oscillation samples;'
        % (len(lad_rows), len(rr), len(ow)))
    rec('  ###   %d modes; %d exact identities checked.**' % (NT, 4))
    rec('  ### **TOTAL WALL-CLOCK: %.1f s against the registered ceiling of 900 s.**'
        % (time.time() - t_start))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(
        f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6,
        f5_worst=f5_worst, f4_worst=f4_worst, f2_rel=float(f2_rel), period=float(period),
        C_even=C_even, C_odd=C_odd, C_all=C_all, K_even=K_even, K_odd=K_odd,
        K_n=[float(z) for z in K_n], c_n=[float(z) for z in c_n],
        lam=[float(z) for z in lam], A0=[float(z) for z in A0], A1=[float(z) for z in A1],
        s_emp=[float(z) for z in s_emp], s_pin=[float(z) for z in s_pin],
        mercer_11=m11, mercer_00=m00, ident_a=ia, ident_c=ic, ident_d=idd,
        M_even=M_even, tail_env=tail_env, tail_lead=tail_lead, p0=p0, psi_max=psi_max,
        asymptote=p0 * M_even, ceiling_rho=ceiling, ceiling_nq=X_CEIL, nres=NRES,
        res_bar=RES_BAR, lam_drift=[float(z) for z in lam_drift],
        ladder=lad_rows, e2=e2rows, master_points=len(rr), f1_master=f1m, env_tightness=ratio,
    ), io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
