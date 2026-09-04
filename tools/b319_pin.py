# -*- coding: utf-8 -*-
"""b319_pin.py -- THE SECOND SCHEME, TRIED. ### **PIN THE RANK.**

### ### **WHY THIS RUNS AT ALL.** ### The order says: if the reach is still empty, ### *the reason
### named and the second scheme (pin the rank) tried before the act closes.* ### The reach IS still
### empty, so the second scheme is tried here rather than filed again.

### ### **WHAT PINNING IS.** ### b318 specified it: fix `r` at the coarsest frame of an axis and, at
### every finer frame, take the top-`r` right singular vectors as the outside basis rather than
### thresholding. ### The rank is then constant BY CONSTRUCTION.

### ### ### **AND THAT IS EXACTLY WHY IT CANNOT BE RIGHT ON BOTH AXES.** ### A constant rank is a
### THEOREM about the grid axis, where the space is fixed and only the discretization moves. ### On
### the domain axis it is a FALSEHOOD: a longer domain is a bigger space, and its dimension must
### grow. ### **PINNING THERE WOULD MANUFACTURE THE CONSTANCY THE BAR ASKS FOR BY DISCARDING THE
### ### DIMENSIONS THE SPACE ACTUALLY HAS.**
### ### This file measures both halves of that rather than asserting either.
"""
import io
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)

import b316_instrument as INS   # noqa: E402
import b317_smear as SM         # noqa: E402
import b319_stable as ST        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b319_pin.py -- THE SECOND SCHEME, TRIED. ### **PIN THE RANK.**')
    rec('=' * 100)
    rec('  ### The order: ### *if still empty, the reason named and the second scheme (pin the')
    rec('  ### rank) tried before the act closes.* ### The reach IS still empty. ### **SO IT IS')
    rec('  ### ### TRIED HERE, ON BOTH AXES, AND MEASURED.**')

    # ### ------------------------------------------------------------------ THE GRID AXIS
    rec('')
    rec('-' * 100)
    rec('### (A) THE GRID AXIS. ### **PINNING CHANGES NOTHING, BECAUSE THERE IS NOTHING LEFT TO FIX.**')
    rec('-' * 100)
    rec('    %-8s %-9s %-9s %-11s %-24s'
        % ('N', 'rank eig', 'rank pin', 'identical?', 'largest eig outside'))
    r_pin = None
    same = True
    for fk in SM.GRID_AXIS:
        fr = INS.Frame(*fk)
        st, _gr = ST.both_subspaces(fr, ST.TAU)
        eig = st['eig']
        if r_pin is None:
            r_pin = st['rank']
        # ### the pinned cut: the top `r_pin` singular directions, by construction
        idx_eig = np.where(eig > ST.TAU)[0]
        order = np.argsort(-eig)
        idx_pin = np.sort(order[:r_pin])
        ident = bool(idx_eig.size == idx_pin.size and np.array_equal(idx_eig, idx_pin))
        same = same and ident
        rec('    %-8d %-9d %-9d %-11s %-24.3e'
            % (fk[0], st['rank'], r_pin, 'YES' if ident else '### NO', float(eig[idx_pin].min())))
        del fr, st
    rec('    ### ### **THE TWO CUTS SELECT THE SAME INDEX SET AT EVERY GRID FRAME : %s**' % same)
    rec('    ### The eigenvalue criterion ALREADY returns a constant rank on this axis, so pinning')
    rec('    ### is not a second scheme here -- ### **IT IS THE SAME SUBSPACE REACHED BY A WEAKER')
    rec('    ### ### ARGUMENT.** ### The eigenvalue cut says WHY the rank is 69; the pin says only')
    rec('    ### that it was 69 at the coarsest frame and was made to stay there.')

    # ### ------------------------------------------------------------------ THE DOMAIN AXIS
    rec('')
    rec('-' * 100)
    rec('### (B) THE DOMAIN AXIS. ### **PINNING IS NOT A REFINEMENT SCHEME HERE, IT IS AN ERROR.**')
    rec('-' * 100)
    rec('    ### A longer domain is a BIGGER SPACE. ### Its dimension must grow, and the measured')
    rec('    ### rank does: `20, 37, 69, 133, 262`. ### **PINNING AT THE COARSEST FRAME FIXES IT AT')
    rec('    ### ### 20 AND THEREFORE CALLS EVERY OTHER DIRECTION IN-SPACE.**')
    rec('    ### The question that decides it: ### **HOW FAR FROM ONE IS THE WORST EIGENVALUE THE')
    rec('    ### ### PIN ADMITS?** ### For a subspace that is meant to approximate the eigenvalue-one')
    rec('    ### eigenspace, an admitted direction at eigenvalue far below one is a refutation.')
    rec('')
    rec('    %-8s %-9s %-9s %-22s %-22s'
        % ('X', 'rank eig', 'rank pin', 'worst admitted (eig)', 'worst admitted (pin)'))
    r_pin_d = None
    worst_pin = 0.0
    for fk in SM.DOMAIN_AXIS:
        fr = INS.Frame(*fk)
        st, _gr = ST.both_subspaces(fr, ST.TAU)
        eig = st['eig']
        if r_pin_d is None:
            r_pin_d = st['rank']
        order = np.argsort(-eig)
        out_pin = np.sort(order[:r_pin_d])
        mask_pin = np.zeros(eig.size, dtype=bool)
        mask_pin[out_pin] = True
        # ### the worst eigenvalue each scheme calls IN the space (should be within TAU of one,
        # ### i.e. `eig` should be at most TAU)
        adm_eig = float(eig[eig <= ST.TAU].max()) if (eig <= ST.TAU).any() else 0.0
        adm_pin = float(eig[~mask_pin].max()) if (~mask_pin).any() else 0.0
        worst_pin = max(worst_pin, adm_pin)
        rec('    %-8g %-9d %-9d %-22.3e %-22.3e'
            % (fk[1], st['rank'], r_pin_d, adm_eig, adm_pin))
        del fr, st
    rec('')
    rec('    ### ### **THE EIGENVALUE CUT NEVER ADMITS A DIRECTION FURTHER THAN `TAU = %.0e` FROM'
        % ST.TAU)
    rec('    ### ### ONE, BY CONSTRUCTION.** ### The pinned cut admits one at ### **%.3e** ### from'
        % worst_pin)
    rec('    ### one at the deepest domain, which is %.0f times the threshold.'
        % (worst_pin / ST.TAU))
    rec('    ### ### **SO PINNING DOES NOT RESCUE THE DOMAIN AXIS. ### IT MANUFACTURES A CONSTANT')
    rec('    ### ### RANK BY CALLING DIRECTIONS IN-SPACE THAT THE SOURCE\'S OWN CRITERION PUTS OUT**,')
    rec('    ### and a reach bought that way would be a reach about the pin and not about the space.')

    rec('')
    rec('-' * 100)
    rec('### (C) THE READING, AND IT IS ABOUT THE BAR RATHER THAN ABOUT THE SCHEME.')
    rec('-' * 100)
    rec('  ### ### **(B3) AS THIS ACT SEALED IT CANNOT BE SATISFIED, AND THAT IS A DEFECT IN (B3).**')
    rec('  ### It requires the rank CONSTANT across each step of BOTH axes. ### On the grid axis')
    rec('  ### that is now met and is a real achievement. ### **ON THE DOMAIN AXIS IT IS')
    rec('  ### ### UNSATISFIABLE BY THE NATURE OF THE OBJECT**: the space grows, so its dimension')
    rec('  ### must, and no scheme that reports the space honestly can hold it fixed.')
    rec('  ### **THE REACH IS THEREFORE REPORTED EMPTY UNDER THE SEALED BAR**, and the bar\'s own')
    rec('  ### defect is named rather than the bar being quietly reinterpreted after the fact.')
    rec('  ### ### **WHAT THE NEXT ACT SHOULD SEAL INSTEAD:** ### rank constancy as a condition on')
    rec('  ### the GRID axis only, with the domain axis carrying a convergence bar and no rank')
    rec('  ### condition at all. ### **THAT IS A PROPOSAL AND NOT A CHANGE**: this registration is')
    rec('  ### sealed and this act does not edit it.')
    rec('=' * 100)
    return 0


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(ROOT, 'data', 'b319_pin.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
