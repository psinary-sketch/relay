# -*- coding: utf-8 -*-
"""b142 COMPONENT 1 -- THE CAP READ. The profile act's opening gate and a HALT.

### THE QUESTION, EXACTLY: does the epsilon-cap at rho = 48.001 bind ANYWHERE in
### the licensed functionals' evaluation? Nothing else is asked here, and if the
### answer is yes the act stops at this file.

THE TWO LICENSED FUNCTIONALS, at b140's own wording:
    the RISE          M(0.80 L) - M(0.50 L),   M = running maximum of psi_coarse
    the DEFICIT NORM  ||r||_{L1[0, 2L]},       r = psi_coarse - M  (r <= 0)

THE OPERATIVE DEFINITION, quoted from b138_coarse.py lines 33-37 and NOT
re-derived here:
    psi_coarse(u) = INT_{-2}^{+2} Kn(s) Psi(clip(u+s, ug[0], ug[-1])) ds
### THE CLIP IS THE CAP MADE OPERATIONAL. Everything below reads rho-support off
### that one line.

THE CIRCULARITY GATE: nothing here cites a ratio table, a sweep, or any measured
C/F/I. The rho-support of a functional is a fact about ITS DOMAIN OF EVALUATION,
not about the density's values.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121

RHO_CAP = 48.001
UMAX = 2.0 * math.log(math.sqrt(RHO_CAP))
L_LO, L_HI = math.log(math.sqrt(2.0)), math.log(math.sqrt(48.0))
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
HALF = 2.0                      # K's support half-width in s, from b138 line 33

print("=" * 78)
print("b142 COMPONENT 1 -- THE CAP READ (the opening gate; a HALT if it binds)")
print("=" * 78)

# ---- (ii) ug's range READ, NOT ASSUMED -- registered where-I-could-be-wrong ----
ug = np.load(r"D:\relay\tools\e16\b134_ug.npy")
print("\n--- ug's ACTUAL RANGE, read from the array (registered as read-not-assumed) ---")
print("  ug[0] = %.9f   ug[-1] = %.9f   points = %d" % (ug[0], ug[-1], len(ug)))
print("  UMAX  = 2*log(sqrt(48.001)) = %.9f" % UMAX)
print("  ug[-1] == UMAX to %.3e ; so the clip's ceiling IS the epsilon-cap: %s"
      % (abs(ug[-1] - UMAX), abs(ug[-1] - UMAX) < 1e-9))
print("  rho at ug[-1] = exp(u) = %.4f" % math.exp(ug[-1]))

# ---- (i) the clamped mass fraction MEASURED, not asserted ----
sg, K, Phi = B121.build_kernel()
ss = np.linspace(-HALF, HALF, 1601)
Kn = np.interp(np.abs(ss), sg, K)
Kn = Kn / float(np.trapezoid(Kn, ss))
print("\n--- CHECK (i): IS THE CLIP A BITE OR A FORMALITY? the clamped mass, MEASURED ---")
print("  registered: 'if Kn's mass near |s|=2 is negligible the halt is wrong'")
print("%10s %14s %16s" % ("u", "clamp s>", "Kn mass clamped"))
for u in (0.0, 1.0, 1.871222, 2.5, 3.0, 3.4, 3.871201):
    scut = UMAX - u
    m = float(np.trapezoid(np.where(ss > scut, Kn, 0.0), ss))
    print("%10.6f %14s %16.9f" % (u, ("%.4f" % scut) if scut <= HALF else "  (none)", m))
print("  ### Kn is EVEN in s, so the mass above s=0 is exactly 0.5 by construction:")
print("      measured %.12f" % float(np.trapezoid(np.where(ss > 0, Kn, 0.0), ss)))

# ---- the rho-support of each functional, per cell ----
print("\n--- THE LICENSED FUNCTIONALS' rho-SUPPORT (the registered deliverable) ---")
print("  psi_coarse(u) reads Psi on [u-2, u+2]; a functional needing psi_coarse")
print("  up to u_top reads Psi to u_top+2, i.e. rho to exp(u_top+2).")
print("%6s %10s %12s %12s %12s %10s %12s %12s %10s"
      % ("a^2", "L", "rise u_top", "rise rho", "cap?", "|", "dfct u_top", "dfct rho", "cap?"))
rise_bind = defc_bind = 0
for a2 in CELLS:
    L = math.log(math.sqrt(a2))
    ur, ud = 0.80 * L, 2.0 * L
    rr, rd = math.exp(ur + HALF), math.exp(ud + HALF)
    br, bd = rr > RHO_CAP, rd > RHO_CAP
    rise_bind += br
    defc_bind += bd
    print("%6d %10.6f %12.6f %12.4f %12s %10s %12.6f %12.4f %10s"
          % (a2, L, ur, rr, "BINDS" if br else "clear", "|", ud, rd,
             "BINDS" if bd else "clear"))

print("\n  the exact thresholds, solved rather than scanned:")
u_ok = UMAX - HALF
print("    psi_coarse is cap-free only for u <= UMAX - 2 = %.6f" % u_ok)
print("    RISE   binds when 0.80 L > %.6f, i.e. a^2 > %.4f  (licensed top %d)"
      % (u_ok, math.exp(2.0 * u_ok / 0.80), 48))
print("    DEFICIT binds when 2.00 L > %.6f, i.e. a^2 > %.4f" % (u_ok, math.exp(u_ok)))

print("\n--- (iii) THE LOWER CLIP, NAMED AND **NOT** COUNTED AS THE CAP ---")
print("  psi_coarse(u) also reads Psi below ug[0]=%.6f for u < 2, clamped to" % ug[0])
print("  Psi(0). That is b119's registered downward endpoint extension, a")
print("  SEPARATE convention. ### COUNTING IT WOULD INFLATE THE READ. Not counted.")

print("\n" + "=" * 78)
print("### THE CAP READ, THE VERDICT")
print("=" * 78)
print("  RISE    : binds at %d of %d licensed cells" % (rise_bind, len(CELLS)))
print("  DEFICIT : binds at %d of %d licensed cells" % (defc_bind, len(CELLS)))
bind = (rise_bind + defc_bind) > 0
print("\n  ### THE CAP %s." % ("BINDS" if bind else "DOES NOT BIND"))
if bind:
    need = math.exp(2.0 * L_HI + HALF)
    print("  ### THE HALT FIRES. Components 2 and 3 consume component 1 and DO NOT RUN.")
    print("\n  THE REQUIREMENT, QUANTIFIED FOR THE ENGINEERING QUEUE:")
    print("    a VALIDATED epsilon evaluation to u = 2*L_HI + 2 = %.6f," % (2 * L_HI + HALF))
    print("    ### i.e. rho = %.4f, against the present validated cap %.3f" % (need, RHO_CAP))
    print("    ### a factor of exp(2) = %.6f in rho, and %.6f in u." % (need / RHO_CAP,
          (2 * L_HI + HALF) / UMAX))
    print("    the shortfall in u is exactly HALF = %.1f, the kernel's support" % HALF)
    print("    half-width -- ### THE MISSING INTERVAL IS THE SMOOTHING WIDTH ITSELF.")

    # ---- HOW HARD IT BITES: the requirement quantified, not merely named ----
    print("\n" + "-" * 78)
    print("### HOW HARD IT BITES -- the deficit norm's integrand, clamped fraction")
    print("-" * 78)
    print("  For each cell, the domain [0,2L] of ||r||_{L1} is swept and the Kn")
    print("  mass that psi_coarse reads from CLAMPED (unvalidated) Psi is averaged")
    print("  over that domain. ### THIS IS WHAT THE NEXT ACT WOULD BE INTEGRATING.")
    print("%6s %14s %16s %16s" % ("a^2", "2L", "mean clamped", "max clamped"))
    for a2 in CELLS:
        L = math.log(math.sqrt(a2))
        us = np.linspace(0.0, 2.0 * L, 801)
        fr = np.array([float(np.trapezoid(np.where(ss > UMAX - u, Kn, 0.0), ss)) for u in us])
        print("%6d %14.6f %16.9f %16.9f" % (a2, 2.0 * L, float(fr.mean()), float(fr.max())))
    print("\n  ### AT THE LARGEST CELL psi_coarse's TOP SAMPLE IS BUILT FROM ~HALF")
    print("  ### CLAMPED KERNEL MASS. An outward-rounded enclosure over that")
    print("  ### integrand would be RIGOROUS ABOUT THE WRONG INTEGRAND, which is")
    print("  ### exactly the reason the staged registration wrote a halt and not")
    print("  ### a caveat.")
    print("\n  ### AND THE STRUCTURAL FACT, WHICH THE REGISTRATION DID NOT ANTICIPATE:")
    print("      2*L_HI = log 48 = %.6f and UMAX = log 48.001 = %.6f." % (2 * L_HI, UMAX))
    print("      ### THE LICENSED RANGE'S TOP AND THE VALIDATED DOMAIN'S TOP ARE THE")
    print("      ### SAME POINT. So the deficit norm's domain exactly exhausts the")
    print("      ### validated density -- and then psi_coarse asks for 2 MORE.")
    print("      ### THE b119 SPLIT AND THE LICENSED RANGE WERE NEVER COMPATIBLE AT")
    print("      ### THE TOP END, AND THIS READ IS WHERE THAT BECOMES VISIBLE.")
