# -*- coding: utf-8 -*-
"""b128 -- THE REPAIR ACT. One attempt under the stop-loss ruling.

THE ROUTE, exact algebra with u = L*sigma:
    I(L) = INT_0^2 Phi_K(sigma) Psi(L sigma) dsigma
         = (1/L) INT_0^{2L} Phi_K(u/L) Psi(u) du
INCUMBENT evaluates the LEFT side: Psi interpolated at dilated points L*sigma.
REPAIR   evaluates the RIGHT side: Psi read AT ITS NATIVE u NODES, the dilation
carried by Phi_K -- which is NQ-INDEPENDENT (corr = convolve(w,w) depends on the
window alone). The repair MOVES the interpolation onto an NQ-independent object;
it does not delete interpolation.

Gate criteria are those banked in data/b128_registration_2026-08-23.txt and are
NOT adjustable here.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import b121_instrument as B121
import qeps_layer as Q

UMAX = 2.0 * math.log(math.sqrt(48.001))
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
BANKED_I = B121.BANKED_I
B119_MARGIN = {2: 0.064826976, 3: 0.095154244, 4: 0.111534989, 8: 0.133564668,
               9: 0.135216620, 12: 0.137327894, 16: 0.137215854,
               24: 0.134217931, 48: 0.123962521}
MIN_MARGIN = min(B119_MARGIN.values())

# ---- pre-committed gate criteria (from the registration; do not edit) ----
G_ID_TOL = 5.0e-3
G_U_TOL = 5.0e-3
G_NQ_ORDER = 10.0
G_NQ_USABLE = 0.064826976

_sg, _K, _Phi = B121.build_kernel()
_pcache = {}


def psi_of(NQ, npts):
    """Psi on a native u grid of npts points. UNCHANGED from the incumbent --
    the repair does not touch how Psi is computed (instance 1 is untouched)."""
    key = (NQ, npts)
    if key not in _pcache:
        ug = np.linspace(0.0, UMAX, npts)
        _pcache[key] = (ug,) + B121.psi_at(NQ, ug)
    return _pcache[key]


def I_incumbent(L, ug, psi):
    """The LEFT side: Psi interpolated at the dilated points L*sigma."""
    q = np.interp(L * _sg, ug, psi, right=psi[-1])
    return float(np.trapezoid(_Phi * q, _sg))


def I_repaired(L, ug, psi):
    """The RIGHT side: Psi at NATIVE nodes; the dilation carried by Phi_K.
    The u nodes used are exactly those of ug that lie in [0, 2L], plus the
    endpoint 2L itself so the interval is covered without extrapolating Psi
    beyond its own grid."""
    hi = 2.0 * L
    m = ug <= hi + 1e-15
    un = ug[m]
    if un[-1] < hi - 1e-15:
        # close the interval at 2L; Psi there by its own native-grid interp,
        # which is an interpolation of Psi at ONE point, not at 2001.
        un = np.append(un, hi)
        pn = np.append(psi[m], float(np.interp(hi, ug, psi)))
    else:
        pn = psi[m]
    ph = np.interp(un / L, _sg, _Phi)       # Phi_K at u/L -- NQ-INDEPENDENT
    return float(np.trapezoid(ph * pn, un) / L)


def table(npts, NQ):
    ug, psi, sig = psi_of(NQ, npts)
    return ({a2: I_incumbent(math.log(math.sqrt(a2)), ug, psi) for a2 in CELLS},
            {a2: I_repaired(math.log(math.sqrt(a2)), ug, psi) for a2 in CELLS},
            psi)


def main():
    print("=" * 78)
    print("b128 -- THE REPAIR ACT   (one attempt; stop-loss governs)")
    print("=" * 78)

    # ================= COMPONENT 1 : G-ID =================
    print("\n" + "-" * 78)
    print("COMPONENT 1 -- THE ROUTE BUILT AND G-ID SAT")
    print("-" * 78)
    inc, rep, psi = table(400, 700)
    print("\n(ID-a) the nine banked pairings through the change-of-variables form")
    print("       recorded configuration NQ = 700, u grid 400 points")
    print("%6s %16s %16s %16s %14s" % ("a^2", "banked", "repaired", "incumbent",
                                       "|rep-banked|"))
    worst_id = 0.0
    worst_inc = 0.0
    for a2 in CELLS:
        d = abs(rep[a2] - BANKED_I[a2])
        worst_id = max(worst_id, d)
        worst_inc = max(worst_inc, abs(inc[a2] - BANKED_I[a2]))
        print("%6d %16.9f %16.9f %16.9f %14.3e" %
              (a2, BANKED_I[a2], rep[a2], inc[a2], d))
    print("\n  worst |repaired - banked|  = %.6e   (criterion < %.1e)" % (worst_id, G_ID_TOL))
    print("  worst |incumbent - banked| = %.6e   (the incumbent's own, for scale)" % worst_inc)
    id_a = worst_id < G_ID_TOL
    print("  ### (ID-a) %s" % ("PASS" if id_a else "FAIL"))

    print("\n(ID-b) the known answer -- INHERITED FROM THE INCUMBENT, NOT EARNED")
    print("       (the repair does not touch how Psi is computed)")
    print("       Psi(0) = %+.9f   known -1.165002987   dev %.2e"
          % (psi[0], abs(psi[0] - (-1.165002987))))
    id_b = abs(psi[0] - (-1.165002987)) < 1e-9
    print("  ### (ID-b) %s" % ("PASS" if id_b else "FAIL"))
    print("\n### G-ID : %s" % ("PASS" if (id_a and id_b) else "FAIL -- HALT"))
    if not (id_a and id_b):
        print("\n*** STOP-LOSS: the attempt ends here. Route to component 4. ***")
        return

    # ================= COMPONENT 2 : G-U then G-NQ =================
    print("\n" + "-" * 78)
    print("COMPONENT 2 -- G-U AND G-NQ")
    print("-" * 78)
    print("\n(G-U) u-grid refinement 200 -> 400 -> 800, at NQ = 700")
    tabs = {}
    for npts in (200, 400, 800):
        i_, r_, _ = table(npts, 700)
        tabs[npts] = (i_, r_)
    print("%6s %14s %14s %14s %14s %14s" %
          ("a^2", "rep@200", "rep@400", "rep@800", "|400-200|", "|800-400|"))
    d1 = d2 = 0.0
    d1i = d2i = 0.0
    for a2 in CELLS:
        a, b, c = tabs[200][1][a2], tabs[400][1][a2], tabs[800][1][a2]
        ai, bi, ci = tabs[200][0][a2], tabs[400][0][a2], tabs[800][0][a2]
        d1 = max(d1, abs(b - a)); d2 = max(d2, abs(c - b))
        d1i = max(d1i, abs(bi - ai)); d2i = max(d2i, abs(ci - bi))
        print("%6d %14.9f %14.9f %14.9f %14.3e %14.3e" % (a2, a, b, c, abs(b - a), abs(c - b)))
    print("\n  REPAIRED  : max|400-200| = %.6e ; max|800-400| = %.6e" % (d1, d2))
    print("  INCUMBENT : max|400-200| = %.6e ; max|800-400| = %.6e  (the referee)" % (d1i, d2i))
    u_a, u_b = d2 < d1, d2 < G_U_TOL
    print("  ### (U-a) differences shrink : %s" % ("PASS" if u_a else "FAIL"))
    print("  ### (U-b) max|800-400| < %.1e : %s" % (G_U_TOL, "PASS" if u_b else "FAIL"))
    print("### G-U : %s" % ("PASS" if (u_a and u_b) else "FAIL -- HALT"))
    gu = u_a and u_b

    print("\n(G-NQ) the b121 test re-run ON THE PAIRINGS, u grid 400")
    NQS = (600, 800, 900)
    print("%6s %14s %14s %14s %14s" %
          ("a^2", "rep@700", "rep excursion", "inc@700", "inc excursion"))
    exc_r = exc_i = 0.0
    for a2 in CELLS:
        er = max(abs(table(400, NQ)[1][a2] - rep[a2]) for NQ in NQS)
        ei = max(abs(table(400, NQ)[0][a2] - inc[a2]) for NQ in NQS)
        exc_r = max(exc_r, er); exc_i = max(exc_i, ei)
        print("%6d %14.9f %14.3e %14.9f %14.3e" % (a2, rep[a2], er, inc[a2], ei))
    print("\n  ### INCUMBENT pairing excursion over NQ : %.6e" % exc_i)
    print("  ### REPAIRED  pairing excursion over NQ : %.6e" % exc_r)
    print("  ratio (incumbent / repaired) = %.3f   (criterion >= %.0f)"
          % (exc_i / exc_r if exc_r else float('inf'), G_NQ_ORDER))
    print("  [Psi's own spread, a DIFFERENT quantity, was 4.361e-01 -- quoted with its name]")
    nq_a = exc_r <= exc_i / G_NQ_ORDER
    nq_b = exc_r < G_NQ_USABLE
    print("  ### (NQ-a) collapse >= 1 order   : %s" % ("PASS" if nq_a else "FAIL"))
    print("  ### (NQ-b) < %.9f (min b119 margin) : %s" % (G_NQ_USABLE, "PASS" if nq_b else "FAIL"))
    print("### G-NQ : %s" % ("PASS" if (nq_a and nq_b) else "FAIL -- HALT"))
    gnq = nq_a and nq_b

    print("\n### THE DECOMPOSITION, reported whether or not the gate passed, so the")
    print("### answer is decomposed and not merely scored:")
    print("  instance-2 contribution (deleted by the repair) = %.6e"
          % abs(exc_i - exc_r))
    print("  instance-1 contribution (untouched, the located cause) = %.6e" % exc_r)
    if exc_i:
        print("  the located cause carries %.1f%% of the incumbent's pairing excursion"
              % (100.0 * exc_r / exc_i))

    print("\n" + "=" * 78)
    print("GATE SUMMARY : G-ID %s | G-U %s | G-NQ %s"
          % ("PASS", "PASS" if gu else "FAIL", "PASS" if gnq else "FAIL"))
    if not (gu and gnq):
        print("*** STOP-LOSS: THE ONE ATTEMPT ENDS. No second try, no tuning.")
        print("*** THE ONE ASKING IS PRESERVED, NOT SPENT. Route to component 4.")
    print("=" * 78)


main()
