# -*- coding: utf-8 -*-
"""noise_floor.py -- THE NOISE-FLOOR GATE (built b272, at the author's instruction).

### WHY THIS EXISTS, AND IT IS A DEFECT REPORT BEFORE IT IS A TOOL.
### At b264 the run printed eleven modes. ### **FOUR OF THEM WERE NOT EIGENVALUES.** ### They sat
### at `~1.5e-8 ~ sqrt(machine epsilon)`, they stopped decaying, and they MOVED when `NQ` moved
### -- upward, ### **WHICH NO TRUE EIGENVALUE DOES.** ### b264's own bank says their
### *"EIGENFUNCTIONS ARE ARBITRARY VECTORS IN A NEAR-DEGENERATE NOISE SUBSPACE, SO THEIR SIGNS
### CARRY NO INFORMATION AT ALL"* ### -- and a sign WAS read off two of them before that was
### caught. ### **THE REGISTRATION TEMPLATE HAS OWED THIS CHECK FOR SIX ACTS RUNNING** (b266,
### b267, b268, b269, b270, b271, each naming it unbuilt). ### This is that check.

### ### **THE ONE THING BUILDING IT AGAINST REAL NUMBERS TAUGHT, AND IT IS NOT WHAT THIS SEAT
### ### EXPECTED: ### A MAGNITUDE TEST ALONE WOULD HAVE PASSED ALL FOUR OF b264's FLOOR MODES.**
### Mode 7 sits at `2.178e-8`, ABOVE `sqrt(eps) = 1.490e-8`; so does every other floor mode.
### ### **IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.** ### A gate built from the
### plausible rule -- "refuse anything below sqrt(eps)" -- would have shipped, passed its own
### review, and caught NOTHING. ### That is recorded here because the tool is only trustworthy
### to the extent its reach is stated.

### THE CONTRACT. ### **ANY ACT READING A COMPUTED SPECTRAL OR MODAL QUANTITY MUST CALL THIS
### BEFORE RESTING A VERDICT ON IT.** ### It returns one of four verdicts and the caller must
### not take a verdict that rests on a REFUSED value.

### THE ARMS ARE EXHAUSTIVE AND MUTUALLY EXCLUSIVE (`W-ORD-PREDICATE-ARM`, b270's species):
###   `EXACT`     -- the channel is exact arithmetic; ### **NO FLOOR APPLIES AND NONE IS
###                  INVENTED.** ### An exact act still CALLS the gate and receives this.
###   `AT_FLOOR`  -- `|value| <= floor`. ### REFUSED.
###   `DRIFTING`  -- above the floor, but the relative change under refinement is at or above
###                  the drift bar. ### REFUSED. ### **THIS IS b264's ACTUAL SPECIES.**
###   `RESOLVED`  -- above the floor and stable under refinement. ### PASS.

### WHAT IT CANNOT DO, STATED SO IT IS NOT TRUSTED BEYOND IT:
###   ### **IT CANNOT SEE A QUANTITY THE ACT NEVER HANDS IT.** ### It is a gate, not a scanner;
###   the act must enumerate what it rests verdicts on, and THAT enumeration is the step this
###   tool cannot perform -- the same reach `reg_satisfiable.py` states for itself.
###   ### **IT CANNOT CERTIFY A VALUE AS PHYSICALLY MEANINGFUL.** ### `RESOLVED` means "not
###   obviously instrument noise", and nothing more.
###   ### **IT NEEDS TWO RESOLUTIONS.** ### Handed one, it can only apply the floor arm -- and
###   the header above says what the floor arm alone is worth.
"""
import math
import sys

# ### THE MEASURED FLOOR. ### `sqrt(machine epsilon)` for float64, which is where b264's four
# ### false modes came to rest. ### NOT a guess: b264's bank names `~1.5e-8 ~ sqrt(machine
# ### epsilon)` from its own printed table.
MACHINE_EPS = 2.220446049250313e-16
DEFAULT_FLOOR = math.sqrt(MACHINE_EPS)          # ### 1.4901161193847656e-08

# ### THE DRIFT BAR, AND ITS MARGIN STATED RATHER THAN ASSERTED.
# ### In b264's own table the LARGEST relative drift among RESOLVED modes is `2.44e-07`
# ### (mode 6) and the SMALLEST among FLOOR modes is `2.34e-02` (mode 10).
# ### ### **THE SEPARATION IS FIVE ORDERS OF MAGNITUDE.** ### The bar is placed at `1e-3`: roughly
# ### four orders above the worst resolved mode and one order below the best floor mode.
# ### **A BAR INSIDE A FIVE-ORDER SEPARATION IS NOT A TUNED PARAMETER, AND IT IS PRINTED BY THE
# ### SELF-TEST SO THE CLAIM IS CHECKABLE RATHER THAN TAKEN.**
DEFAULT_DRIFT_BAR = 1e-3

EXACT = 'EXACT'
AT_FLOOR = 'AT_FLOOR'
DRIFTING = 'DRIFTING'
RESOLVED = 'RESOLVED'

REFUSING = (AT_FLOOR, DRIFTING)


def classify(value, refined=None, floor=DEFAULT_FLOOR, drift_bar=DEFAULT_DRIFT_BAR,
             exact=False):
    """### ONE VALUE, ONE VERDICT. ### Four arms, exhaustive and mutually exclusive.

    ### `value`   -- the quantity at the act's working resolution.
    ### `refined` -- the SAME quantity recomputed at a finer resolution; `None` if the act has
    ###              only one, in which case ### **ONLY THE FLOOR ARM CAN FIRE** ### and the
    ###              detail says so, because a silent half-check is worse than no check.
    ### `exact`   -- the channel is exact arithmetic. ### Returns `EXACT` and applies no floor.
    """
    if exact:
        return EXACT, 'exact channel -- no floor applies and none is invented'
    v = abs(value)
    if v <= floor:
        return AT_FLOOR, 'abs(value) = %.6e <= floor %.6e' % (v, floor)
    if refined is None:
        return RESOLVED, ('above floor %.6e; ### ONLY THE FLOOR ARM WAS APPLICABLE -- no '
                          'refined value was supplied, and the floor arm alone would have '
                          'passed every one of b264\'s four false modes' % floor)
    drift = abs(refined - value) / v
    if drift >= drift_bar:
        return DRIFTING, ('abs(value) = %.6e above floor, but relative drift %.3e >= bar %.3e '
                          '-- b264\'s species' % (v, drift, drift_bar))
    return RESOLVED, 'abs(value) = %.6e above floor; drift %.3e < bar %.3e' % (v, drift, drift_bar)


def gate(items, floor=DEFAULT_FLOOR, drift_bar=DEFAULT_DRIFT_BAR, exact=False, label=''):
    """### THE COMMAND-PATH ENTRY POINT. ### `items` is a list of `(name, value, refined)`.

    ### Returns `(ok, rows, detail)`. ### **`ok` IS FALSE IF ANY VALUE IS REFUSED, AND THE
    ### CALLER MAY NOT TAKE A VERDICT THAT RESTS ON A REFUSED VALUE.**"""
    rows = []
    refused = []
    for name, value, refined in items:
        verdict, why = classify(value, refined, floor, drift_bar, exact)
        rows.append((name, value, refined, verdict, why))
        if verdict in REFUSING:
            refused.append(name)
    if refused:
        return False, rows, ('### REFUSED -- %d of %d value(s) rest on the instrument floor: %s'
                             % (len(refused), len(rows), ', '.join(str(r) for r in refused)))
    if exact:
        return True, rows, ('### EXACT CHANNEL -- the gate was CALLED and applies no floor; '
                            'this is a verdict, not a bypass')
    return True, rows, '### PASS -- all %d value(s) are above the floor and stable' % len(rows)


# ### ----------------------------------------------------------------------------------------
# ### THE FIXTURES, BOTH POLARITIES, FROM b264's OWN PRINTED TABLE (`data/b264_run.txt`).
# ### **NOT INVENTED NUMBERS. ### EVERY ROW IS A LINE THAT WAS ACTUALLY PRINTED BY b264.**
# ### ----------------------------------------------------------------------------------------
# ### b264 PRINTED TWO COLUMNS: the value at `NQ` and a RELATIVE DRIFT. ### The fixtures carry
# ### BOTH, and the refined value is reconstructed as `value * (1 + drift)`.
# ### ### **A FIRST DRAFT CARRIED THE TWO PRINTED VALUE COLUMNS INSTEAD, AND THE RESOLVED
# ### ### MODES' DRIFTS VANISHED** -- b264 printed those to seven significant figures, at which
# ### ### width a drift of `4.40e-14` is INVISIBLE and both columns read identically. ### The
# ### ### self-test divided by that zero and died, which is how it was found. ### **A FIXTURE
# ### ### BUILT FROM A ROUNDED PRINTOUT IS NOT THE MEASUREMENT.**
B264_MODES = [
    # ### (mode, value at NQ, b264's printed relative drift, b264's own printed verdict)
    (0, 9.999714e-01, 4.40e-14, RESOLVED),
    (1, 9.794847e-01, 2.80e-14, RESOLVED),
    (2, 5.240859e-01, 2.14e-13, RESOLVED),
    (3, 5.897659e-02, 5.65e-13, RESOLVED),
    (4, 2.732329e-03, 6.03e-13, RESOLVED),
    (5, 7.629136e-05, 3.65e-10, RESOLVED),
    (6, 1.439470e-06, 2.44e-07, RESOLVED),
    (7, 2.178442e-08, 2.74e-02, DRIFTING),
    (8, 1.811457e-08, 6.37e-02, DRIFTING),
    (9, 1.650848e-08, 9.11e-02, DRIFTING),
    (10, 1.515987e-08, 2.34e-02, DRIFTING),
]


def refined_of(value, drift):
    """### RECONSTRUCT THE FINER-RESOLUTION VALUE FROM b264's PRINTED RELATIVE DRIFT."""
    return value * (1.0 + drift)


def self_test(verbose=True):
    """### BOTH POLARITIES, AGAINST b264's REAL NUMBERS. ### Returns `(ok, lines)`."""
    out = []

    def rec(s=''):
        out.append(s)
        if verbose:
            print(s)

    rec('=' * 100)
    rec('noise_floor.py -- SELF-TEST. ### BOTH POLARITIES, FROM b264\'s OWN PRINTED TABLE.')
    rec('=' * 100)
    rec('  floor     = %.6e   ### sqrt(machine epsilon), where b264\'s false modes came to rest'
        % DEFAULT_FLOOR)
    rec('  drift bar = %.3e   ### placed inside the measured separation, not tuned' % DEFAULT_DRIFT_BAR)
    rec()
    rec('  %-5s %-15s %-15s %-11s %-11s %s'
        % ('mode', 'value @NQ', 'value @2NQ', 'b264 said', 'gate says', 'agree'))
    rec('  ' + '-' * 92)
    bad = 0
    floor_arm_alone = 0
    for mode, v, d, expected in B264_MODES:
        r = refined_of(v, d)
        verdict, _ = classify(v, r)
        agree = (verdict == expected)
        if not agree:
            bad += 1
        # ### AND THE POINT THE HEADER MAKES, COUNTED RATHER THAN ASSERTED:
        # ### how many of b264's FALSE modes would the FLOOR ARM ALONE have passed?
        if expected == DRIFTING and abs(v) > DEFAULT_FLOOR:
            floor_arm_alone += 1
        rec('  %-5d %-15.6e %-15.6e %-11s %-11s %s'
            % (mode, v, r, expected, verdict, 'YES' if agree else '### NO ###'))
    rec()
    rec('  ### AGREEMENT WITH b264\'s OWN VERDICTS : %d of %d'
        % (len(B264_MODES) - bad, len(B264_MODES)))

    # ### THE DRIFT SEPARATION, PRINTED SO THE BAR'S PLACEMENT IS CHECKABLE.
    res_drift = [d for _, v, d, e in B264_MODES if e == RESOLVED]
    flo_drift = [d for _, v, d, e in B264_MODES if e == DRIFTING]
    rec('  ### LARGEST DRIFT AMONG RESOLVED MODES  : %.3e' % max(res_drift))
    rec('  ### SMALLEST DRIFT AMONG FLOOR MODES    : %.3e' % min(flo_drift))
    rec('  ### THE BAR SITS AT %.3e, INSIDE A SEPARATION OF %.1f ORDERS OF MAGNITUDE.'
        % (DEFAULT_DRIFT_BAR, math.log10(min(flo_drift) / max(res_drift))))
    rec()
    rec('  ### ### **FLOOR MODES THE MAGNITUDE ARM ALONE WOULD HAVE PASSED : %d of %d.**'
        % (floor_arm_alone, len(flo_drift)))
    rec('  ### ### **SO THE OBVIOUS GATE -- "REFUSE ANYTHING BELOW sqrt(eps)" -- WOULD HAVE')
    rec('  ### ### SHIPPED AND CAUGHT NOTHING. ### THE DRIFT ARM IS THE WHOLE TOOL.**')
    rec()

    # ### THE THREE REMAINING ARMS, EACH EXERCISED ONCE.
    a_ok, _, a_det = gate([('positive-control', 5.240859e-01, 5.240859e-01)])
    b_ok, _, b_det = gate([('below-floor', 1.0e-12, 1.0e-12)])
    c_ok, _, c_det = gate([('b264-mode-7', 2.178442e-08, 2.118681e-08)])
    d_ok, _, d_det = gate([('exact-channel', 0, None)], exact=True)
    rec('  ARM EXERCISE, ALL FOUR:')
    rec('    RESOLVED  (positive control) -> ok=%s  %s' % (a_ok, a_det))
    rec('    AT_FLOOR                     -> ok=%s  %s' % (b_ok, b_det))
    rec('    DRIFTING  (b264 mode 7)      -> ok=%s  %s' % (c_ok, c_det))
    rec('    EXACT                        -> ok=%s  %s' % (d_ok, d_det))
    rec()

    ok = (bad == 0 and a_ok and (not b_ok) and (not c_ok) and d_ok
          and floor_arm_alone == len(flo_drift))
    rec('  ### VERDICT : %s' % ('SELF-TEST PASSED -- the gate reproduces b264\'s own eleven '
                                'verdicts and all four arms fire' if ok
                                else '### SELF-TEST FAILED ###'))
    rec('  ### REACH: ### **IT CANNOT SEE A QUANTITY THE ACT NEVER HANDS IT.** ### The act must')
    rec('  ### enumerate what it rests verdicts on; that step is not this tool\'s.')
    return ok, out


if __name__ == '__main__':
    good, _ = self_test()
    sys.exit(0 if good else 1)
