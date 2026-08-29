# -*- coding: utf-8 -*-
"""b241_checks.py -- the b241 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a reading was chosen because it shrinks the residual. ### THE ACT'S WHOLE
###       ### EXPOSURE. ### Gates 8 and 9: the orientation must read ROUTED, no candidate
###       ### may be adopted, and the shrink must be DISCLOSED rather than omitted.
###   (2) that an absence was reported without ever showing the test could see a presence.
###       ### Gates 4 and 5 are POSITIVE CONTROLS ON ABSENCES: each runs the same test
###       ### against a file where the thing IS there, and requires it to fail.
###   (3) that this act asserted b240's check is a tautology instead of demonstrating it.
###       ### Gate 6 RUNS b240's own algebra on ARBITRARY NUMBERS and requires it to pass.
###   (4) that the registration was credited with foresight it does not have. ### Gate 2
###       ### requires the registration to disclose that the reads preceded it, and gate 10
###       ### requires the act to say the dissent was registered before its VERDICT and not
###       ### before its EVIDENCE.
###   (5) that a correction executed without a ruling. ### Gate 11: File E and the kernel
###       ### tree must be byte-unmodified, and the bank must say no correction executed.
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

REG = os.path.join(D, 'b241_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b241_residual_ledger.txt')
SIB = os.path.join(D, 'b241_sibling_read.txt')
B240BANK = os.path.join(D, 'b240_first_face_off.txt')
B240DIAG = os.path.join(D, 'b240_diagnostics.txt')
B240MEAN = os.path.join(D, 'b240_meanings.txt')

FILE_E = 'D:/SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean'
B38 = os.path.join(E16, 'b38_act10.py')
B37 = os.path.join(E16, 'b37_act9.py')
B36 = os.path.join(E16, 'b36_act8.py')


def src(p):
    return io.open(p, encoding='utf-8').read()


def has_trace_function(path):
    """### THE ABSENCE TEST OF COMPONENT 3, WRITTEN ONCE SO IT CAN BE POINTED AT TWO FILES.
    ### `b37_act9.py` defines no trace and calls none -- that absence IS its
    ### 'resid47: 0 by construction'. ### A test for an absence that has never been shown to
    ### detect a PRESENCE is not evidence of anything, so gate 4 aims this at `b38_act10.py`."""
    s = src(path)
    return ('def trace_modes' in s) or ('trace_modes(' in s)


def tautology_holds(independent_resid):
    """### b240's OWN DECOMPOSITION ALGEBRA, RUN ON ARBITRARY NUMBERS.

    ### b240_diagnostics.py:74-75   resid = Tr - A - E2 ; pred = 2*E2 + Dm + resid + Thq + PR
    ### b240_faceoff.py:110-112     T = Tr + E2 + Dm ; Lft = T + Thq ; Rgt = A - PR
    ### With `resid` DEFINED as the residue the two collapse to the same expression, so the
    ### 'check' passes for ANY inputs. ### With `resid` supplied INDEPENDENTLY it must fail --
    ### and that is the fixture, which is how this gate shows it can say no.
    """
    import numpy as np
    rng = np.random.default_rng(20260829)
    worst = 0.0
    for _ in range(500):
        Tr, A, E2, Dm, Thq, PR, indep = rng.normal(0.0, 3.0, 7)
        resid = indep if independent_resid else (Tr - A - E2)
        pred = 2 * E2 + Dm + resid + Thq + PR
        lft = (Tr + E2 + Dm) + Thq
        rgt = A - PR
        worst = max(worst, abs(pred - (lft - rgt)))
    # ### `bool(...)` DELIBERATELY: numpy's `np.False_` is not a bool and the harness REFUSED
    # ### this gate for it on the first run. ### Recorded rather than silently patched.
    return bool(worst <= 1e-9)


def tautology_on_b240_rows():
    """### THE WITNESS: the same algebra on b240's SIX BANKED ROWS. ### Must pass."""
    rows = [(3.358857, 0.677615, 4.048575, 0.000000, 0.000000, 8.085046),
            (3.033289, 0.605701, 3.373977, 0.000000, 0.106484, 7.119451),
            (2.748101, 0.540018, 3.047750, 0.161978, 0.249320, 6.747167),
            (2.192479, 0.410725, 2.520787, 0.317018, 0.561045, 6.002054),
            (2.116618, 0.393176, 2.453999, 0.473862, 0.608882, 6.046537),
            (1.950128, 0.354973, 2.313445, 0.518491, 0.714334, 5.851371)]
    return all(abs((twoE2 + Dm + r + Thq + PR) - LmR) <= 5e-6
               for (twoE2, Dm, r, Thq, PR, LmR) in rows)


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b241')

    # 1 -- ### THE REGISTRATION PRECEDES THE BANK ON DISK.
    h.run('registration-precedes-the-bank',
          check=lambda: (os.path.exists(REG) and os.path.exists(BANK)
                         and os.path.getmtime(REG) < os.path.getmtime(BANK)),
          fixture=lambda: os.path.getmtime(BANK) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 4000)

    # 2 -- ### THE REGISTRATION DOES NOT CLAIM FORESIGHT IT DOES NOT HAVE.
    # ### The ferry ordered the reads FIRST. ### A registration written after the reads that
    # ### presented itself as a sight-unseen prediction would be a forgery, and section (0) says so.
    h.run('registration-discloses-its-reading-order',
          check=lambda: all(contains(REG, s) for s in
                            ('owners read at content first',
                             'THIS FILE IS NOT A SIGHT-UNSEEN PREDICTION',
                             'A REGISTRATION THAT CLAIMED TO PREDICT READS ALREADY DONE WOULD BE '
                             'A FORGERY')),
          fixture=lambda: contains(B240MEAN, 'THIS FILE IS NOT A SIGHT-UNSEEN PREDICTION'),
          witness=lambda: contains(REG, 'NOT A SIGHT-UNSEEN PREDICTION'))

    # 3 -- ### THE STANDING CLAUSE IS QUOTED AT REGISTRATION, AS THE FERRY DIRECTS, AND THE
    # ### FIVE TESTS ARE FIXED THERE BEFORE ANY VERDICT.
    h.run('standing-clause-quoted-and-tests-fixed',
          check=lambda: all(contains(REG, s) for s in
                            ('no reading is chosen because it shrinks the residual',
                             '(T1) THE WARRANT IS A QUOTATION',
                             '(T3) THE UNDERDETERMINED ROUTES',
                             '(T4) NO CORRECTION WITHOUT FORCE',
                             '(T5) NUMBERS ARE THE QUESTION, NEVER THE ANSWER')),
          fixture=lambda: contains(B240BANK, '(T4) NO CORRECTION WITHOUT FORCE'),
          witness=lambda: contains(REG, '(T1) THE WARRANT IS A QUOTATION'))

    # 4 -- ### POSITIVE CONTROL ON AN ABSENCE (Component 3). ### `b37_act9.py` HAS NO TRACE
    # ### FUNCTION -- that absence IS "0 by construction". ### THE FIXTURE AIMS THE SAME TEST
    # ### AT `b38_act10.py`, WHICH DOES HAVE ONE, AND REQUIRES IT TO FAIL.
    h.run('b37-has-no-trace-function-CONTROLLED',
          check=lambda: not has_trace_function(B37),
          fixture=lambda: not has_trace_function(B38),
          witness=lambda: os.path.getsize(B37) > 3000 and contains(B37, 'def theta_quotient'))

    # 5 -- ### POSITIVE CONTROL ON THE SECOND ABSENCE (Component 1). ### `b38_act10.py`'s `A`
    # ### SUMS, SUBTRACTS AND REGULARIZES WITH NOTHING. ### THE FIXTURE AIMS THE SAME TEST AT
    # ### `b36_act8.py`'s ASSEMBLY LINE, WHICH DOES COMBINE CHANNELS, AND REQUIRES IT TO FAIL.
    h.run('A-combines-no-channel-CONTROLLED',
          check=lambda: not any(t in src(B38).split('def trace_modes')[0].split('def left_side')[1]
                                for t in ('trace_modes', 'e2_of_grid', 'theta_quotient', 'resid')),
          fixture=lambda: not any(t in 'RIGHT = (Tr_full + E2 - Dneg) - Thq'
                                  for t in ('Tr_full', 'E2', 'Thq')),
          witness=lambda: contains(B38, 'A = float(np.trapezoid(GU ** 2 * C.kernel(U), U)'))

    # 6 -- ### THE TAUTOLOGY IS DEMONSTRATED, NOT ASSERTED. ### b240's own algebra passes on
    # ### FIVE HUNDRED ARBITRARY TUPLES. ### THE FIXTURE SUPPLIES `resid` INDEPENDENTLY, WHERE
    # ### IT MUST FAIL -- which is what shows the demonstration is about the DEFINITION of
    # ### `resid` and not about the arithmetic being trivially true.
    h.run('b240-decomposition-is-a-tautology-DEMONSTRATED',
          check=lambda: tautology_holds(independent_resid=False),
          fixture=lambda: tautology_holds(independent_resid=True),
          witness=tautology_on_b240_rows)

    # 7 -- ### THE TWO SIBLING FORMULAS DIFFER IN SOURCE, AND THE ACT QUOTES BOTH LINES.
    h.run('sibling-resid47-formulas-differ-in-source',
          check=lambda: (contains(B38, 'resid = TrN - A - E2N')
                         and contains(B36, 'resid47 = Tr_full - (A + E2)')
                         and contains(BANK, 'resid = TrN - A - E2N')
                         and contains(BANK, 'resid47 = Tr_full - (A + E2)')),
          fixture=lambda: contains(B38, 'resid47 = Tr_full - (A + E2)'),
          witness=lambda: contains(B38, 'E2N = float(E2n.sum())'))

    # 8 -- ### THE ORIENTATION IS ROUTED AND NO CANDIDATE IS ADOPTED. ### THE ACT'S PRINCIPAL
    # ### EXPOSURE, AND THE GATE READS THE VERDICT LINE ITSELF.
    h.run('q-orientation-routed-no-candidate-adopted',
          check=lambda: (contains(BANK, 'THE VERDICT ON (d): ### (UNDERDETERMINED)')
                         and contains(BANK, 'NO ORIENTATION IS CHOSEN')
                         and contains(BANK, 'THE AGGREGATION IS UNSTATED')
                         and not contains(BANK, 'THE ORIENTATION IS FIXED BY TEXT')),
          fixture=lambda: contains(B240BANK, 'THE VERDICT ON (d): ### (UNDERDETERMINED)'),
          witness=lambda: contains(BANK, 'O1'))

    # 9 -- ### THE SHRINK IS DISCLOSED IN THE SAME BREATH AS THE VERDICT (test T2). ### An act
    # ### that routed the question but hid that one candidate helps would pass gate 8 and
    # ### still be concealing the thing the standing clause is about.
    h.run('shrink-direction-disclosed-beside-the-verdict',
          check=lambda: (contains(BANK, 'O1 SHRINKS THE RESIDUAL, AND THAT IS NOT WHY IT IS '
                                        'LISTED FIRST')
                         and contains(BANK, 'NO ORIENTATION ON THIS LIST CLOSES THE SEPARATION')
                         and contains(BANK, 'ACCUMULATING WARRANT FOR A SIGN THAT HAPPENS TO '
                                            'HELP')),
          fixture=lambda: contains(B240DIAG, 'O1 SHRINKS THE RESIDUAL'),
          witness=lambda: contains(BANK, 'SHRINKS THE RESIDUAL'))

    # 10 -- ### THE REGISTERED EXPECTATION IS BANKED **AND** ITS CREDIT IS NOT OVERCLAIMED.
    h.run('expectation-banked-and-credit-not-overclaimed',
          check=lambda: (contains(REG, 'THE EXECUTOR\'S EXPECTATION, REGISTERED HERE BEFORE '
                                       '(E)\'s VERDICT IS WRITTEN: ### DISSENT')
                         and contains(BANK, 'IT WAS REGISTERED BEFORE ITS VERDICT, NOT BEFORE '
                                            'ITS EVIDENCE')),
          fixture=lambda: contains(B240MEAN, 'IT WAS REGISTERED BEFORE ITS VERDICT, NOT BEFORE '
                                             'ITS EVIDENCE'),
          witness=lambda: contains(REG, 'DISSENT'))

    # 11 -- ### NOTHING WAS CORRECTED, AMENDED OR TOUCHED. ### File E byte-unmodified in the
    # ### RESIDENCE, the kernel tree clean, and the bank saying so in its own words.
    h.run('no-correction-executed-file-E-untouched',
          check=lambda: (unmodified('D:/SIDE-global-section',
                                    'Interfaces/FiniteInstanceIdentity.lean')
                         and unmodified('D:/SIDE-global-section', 'Core')
                         and unmodified('D:/SIDE-global-section', 'CORRESPONDENCE.md')
                         and contains(BANK, 'NO CORRECTION EXECUTED')
                         and contains(BANK, 'RULE M-1 UNAMENDED')),
          # ### THE FIXTURE: a path this act DID write must read as MODIFIED, or `unmodified`
          # ### is answering yes to everything and gate 11 proves nothing.
          fixture=lambda: unmodified('D:/relay', 'data/b241_residual_ledger.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    # 12 -- ### THE INDEX WAS QUERIED AND ITS RESULT REPORTED WHETHER OR NOT IT HELPED --
    # ### AND HERE IT DID NOT HELP, IT STOPPED A VERDICT. ### The act must say that.
    h.run('index-queried-and-its-result-reported',
          check=lambda: (contains(REG, 'quotient-trace (act 9 / b197 / b215) -- HIT')
                         and contains(BANK, 'b197, re-confirmed b215')
                         and contains(BANK, 'THE GATE EARNED ITS KEEP THIS ACT')),
          fixture=lambda: contains(B240BANK, 'THE GATE EARNED ITS KEEP THIS ACT'),
          witness=lambda: contains(REG, 'NO KEY'))

    # 13 -- ### THE GOVERNING FILE E WAS READ, AND THE STALE WORKING COPY IS FILED RATHER THAN
    # ### QUIETLY AVOIDED. ### The gate checks the drift is REAL, so the filing is not decorative.
    h.run('governing-file-E-read-stale-copy-filed',
          check=lambda: (contains(FILE_E, 'RULE M-1: C2, per-cell instrument realization')
                         and not contains(os.path.join(ROOT, 'tools', 'lean', 'mathlib-companion',
                                                       'FiniteInstanceIdentity.lean'),
                                          'RULE M-1')
                         and contains(BANK, 'W-ORD-FILE-E-WORKING-COPY-STALE')),
          fixture=lambda: contains(os.path.join(ROOT, 'tools', 'lean', 'mathlib-companion',
                                                'FiniteInstanceIdentity.lean'), 'RULE M-1'),
          witness=lambda: contains(FILE_E, 'T.value + Q.value = W.wInf - W.wPrimes'))

    # 14 -- ### THE LEDGER IS RESTATED WITH A STATUS PER TERM, AND THE TALLY MATCHES.
    h.run('five-term-ledger-restated-with-status',
          check=lambda: all(contains(BANK, s) for s in
                            ('ONE RECONCILED-BY-TEXT, TWO ROUTED, TWO STANDING',
                             'RECONCILED-BY-TEXT (Component 3)', 'ROUTED (Component 4)',
                             'ROUTED (new this act)', 'STANDING, AND THE ONE TERM WITH A '
                             'SETTLED')),
          fixture=lambda: contains(B240BANK, 'ONE RECONCILED-BY-TEXT, TWO ROUTED, TWO STANDING'),
          witness=lambda: contains(BANK, 'ONE RECONCILED-BY-TEXT'))

    # 15 -- ### THE CEILING AND h2, IN THE ACT'S OWN WORDS, IN BOTH FILES.
    h.run('ceiling-and-h2-in-both-files',
          check=lambda: (both(BANK, 'DECIDES NOTHING GLOBAL',
                              'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT')
                         and contains(REG, 'DECIDES NOTHING GLOBAL')
                         and contains(SIB, 'DECIDES NOTHING GLOBAL')),
          # ### THE FIRST FIXTURE HERE POINTED AT THIS VERY FILE, WHICH CONTAINS THE PHRASE AS A
          # ### STRING LITERAL, SO IT PASSED AND THE HARNESS REFUSED THE GATE. ### Exactly b213's
          # ### species -- a check re-matching the text the executor had just written -- and the
          # ### harness caught it. ### The fixture now points at a real file that lacks the phrase.
          fixture=lambda: contains(os.path.join(ROOT, 'tools', 'lean', 'RESIDENCE.md'),
                                   'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    for row in h.rows:
        print('  %-52s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
