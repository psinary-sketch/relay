# -*- coding: utf-8 -*-
"""b168 -- THE REPAIRED EPSILON GRID. A DOMAIN FIX, NOT A RESOLUTION CHANGE.

### THE DEFECT (b167): the incumbent grid's first node is exp(1e-4) = 1.0001000050,
not 1, and np.interp CLAMPS below its first node -- so an evaluation at rho = 1
returned e_n(1.0001) where e_n(1) = 0 was wanted. The deficit was identical at
n_rho 400/800/1600/3200: ### REFINEMENT CANNOT CURE A DOMAIN DEFECT.

### THE ROUTINE WAS NEVER AT FAULT. b38_act10.per_mode_eps_grids takes its own
empty-range branch at rho = 1 --

    lo, hi = 1.0 / r, 1.0
    if hi - lo <= 0:
        continue

-- and leaves the entry at zero, which IS b115 (2g)'s derived e_n(0) = 0. The
routine has been honest at rho = 1 all along and nobody ever asked it.

### THE REPAIR: PREPEND rho = 1.0 TO THE INCUMBENT GRID, VALUE TAKEN FROM THE
### ROUTINE, EVERY INCUMBENT NODE LEFT IN PLACE.
Rebuilding as linspace(0, ln(RHO_MAX), n) would also reach rho = 1 but would
REDISTRIBUTE EVERY NODE and shift every interpolated value in the record.
Prepending one node means np.interp at any rho >= exp(1e-4) uses THE SAME
NEIGHBOURING NODES AND RETURNS THE SAME NUMBER, so ### THE INCUMBENT-PRESERVATION
### LAW IS SATISFIED BY CONSTRUCTION AND NOT BY LUCK. Only rho in [1, exp(1e-4))
changes, and there it changes from a clamped constant to the honest rise from zero.

### e_n(0) IS NOT SET TO ZERO BY HAND -- b167 named that as the thing a repair must
### not do. The value is whatever the routine returns at the new node.

### b134_wroute.py IS NOT MODIFIED. Its psi_W takes E as a parameter, so the
repaired grid is INJECTED rather than patched over, and a prior act's instrument
stays reproducible exactly as that act ran it.
"""
import math
import numpy as np
import b38_act10 as B38

RHO_MAX = 48.001
NMODE = 10


def incumbent_grid(n_rho=800, rho_max=RHO_MAX):
    """the grid as b113/b115/b134 built it -- first node exp(1e-4)."""
    return np.exp(np.linspace(1e-4, math.log(rho_max), n_rho))


def repaired_grid(n_rho=800, rho_max=RHO_MAX):
    """### the incumbent grid with rho = 1 PREPENDED. Domain fix; nodes preserved."""
    return np.concatenate(([1.0], incumbent_grid(n_rho, rho_max)))


def eps_on(rr):
    """the mode parts on a given grid, from b38's own routine."""
    return B38.per_mode_eps_grids(rr)


def E_modes(ug, n_rho=800, repaired=True, nmode=NMODE):
    """e_n at the requested u, read off the chosen grid by np.interp."""
    rr = repaired_grid(n_rho) if repaired else incumbent_grid(n_rho)
    ee = eps_on(rr)
    E = np.zeros((nmode, len(ug)))
    for n in range(min(nmode, ee.shape[0])):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    return E
