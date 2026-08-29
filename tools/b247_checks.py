# -*- coding: utf-8 -*-
"""b247_checks.py -- the b247 gates, routed through the amended b217 harness.

### EVERY FIXTURE IS ANNOTATED WITH **WHY IT FAILS**, and none is `not check`.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a derivation was performed under a statement-read's cover. ### Gate 8: no route
###       ### step may be marked DERIVES, and the bank must say none was performed.
###   (2) that an asset got a verdict outside the three permitted. ### Gate 4 is a POSITIVE
###       ### CONTROL ON AN ABSENCE -- the forbidden words are shown findable elsewhere.
###   (3) that the A-2 discriminator was invented after its number. ### Gate 5: it is in the
###       ### REGISTRATION, which precedes the reads file on disk.
###   (4) that an import was graded without a primary. ### Gate 6, and the refusal's qualifier.
###   (5) that the halt was placed where it was expected rather than where it is. ### Gate 7
###       ### requires the act to report that its own expectation named the WRONG clause.
"""
import io
import math
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

REG = os.path.join(D, 'b247_registration_2026-08-29.txt')
READS = os.path.join(D, 'b247_statement_reads.txt')
BANK = os.path.join(D, 'b247_m4_statement_and_route.txt')
B130 = os.path.join(D, 'b130_crown_opening.txt')
B246 = os.path.join(D, 'b246_two_tails.txt')
B212 = os.path.join(D, 'b212_odd_family.txt')
LAYER = os.path.join(E16, 'prolate_layer.py')
QEPS = os.path.join(E16, 'qeps_layer.py')

FORBIDDEN_VERDICTS = ('essentially the same', 'closely related', 'compatible objects')


def xi1_is_not_constant():
    """### THE A-2 DISCRIMINATOR, RE-DERIVED FROM THE LAYER RATHER THAN READ FROM THE PROSE.
    ### b212 measured `|alpha|` CONSTANT in the index; if `xi_n(1)` were the same object it would
    ### be constant too. ### THIS RECOMPUTES IT."""
    import numpy as np
    sys.path.insert(0, E16)
    import prolate_layer as PL
    x, w, mu, psi, psi1 = PL.prolate(700)
    xi1 = math.sqrt(2) * np.abs(psi1[0::2])[:11]
    return bool(float(xi1.max() / xi1.min()) > 100.0)


def xi1sq_grows_on_certified_range():
    """### THE FINDING THE ACT DID NOT GO LOOKING FOR: clause (ii)'s FIRST disjunct is FALSE.
    ### `xi_n(1)^2` GROWS across n = 0..6 by more than three orders."""
    import numpy as np
    sys.path.insert(0, E16)
    import prolate_layer as PL
    x, w, mu, psi, psi1 = PL.prolate(700)
    xi1 = math.sqrt(2) * np.abs(psi1[0::2])[:7]
    sq = xi1 ** 2
    monotone = all(sq[i] < sq[i + 1] for i in range(len(sq) - 1))
    return bool(monotone and float(sq[-1] / sq[0]) > 1e3)


def no_forbidden_verdict(path):
    s = io.open(path, encoding='utf-8').read().lower()
    return not any(f in s for f in FORBIDDEN_VERDICTS)


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b247')

    h.run('registration-precedes-reads-and-bank',
          check=lambda: (os.path.getmtime(REG) < os.path.getmtime(READS)
                         and os.path.getmtime(READS) < os.path.getmtime(BANK)),
          # ### FIXTURE: the same ordering demanded of two files written in the OPPOSITE order --
          # ### the bank before the registration. ### FAILS ON A REAL TIME ORDER, not on a negation.
          fixture=lambda: os.path.getmtime(BANK) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 6000)

    # 2 -- ### EVERY CONSTITUENT UNFOLDED TO ITS OWNER (the E0 gate), QUOTED FROM SOURCE.
    h.run('E0-constituents-unfolded-and-quoted',
          check=lambda: all(contains(BANK, s) for s in
                            ('time-and-band limiting operator on [-1,1]',
                             'c = 2 pi',
                             'lambda(n) = (-1)^n sqrt(mu_{2n})',
                             'xi_n = sqrt(2) * psi_{2n}',
                             'NOT extrapolated from the grid'))
                        and contains(LAYER, 'time-and-band limiting operator'),
          fixture=lambda: contains(B246, 'lambda(n) = (-1)^n sqrt(mu_{2n})'),
          witness=lambda: contains(LAYER, 'Slepian-Pollak 1961'))

    # 3 -- ### THE HALT IS DECLARED AND THE MISSING SENTENCE IS NAMED.
    h.run('statement-halts-with-missing-sentence-named',
          check=lambda: (contains(BANK, 'THE STATEMENT HALTS HERE')
                         and contains(BANK, 'THE MISSING SENTENCE, STATED AS THE THING THAT MUST '
                                            'BE SUPPLIED')
                         and contains(BANK, 'NO OWNER SUPPLIES IT')),
          fixture=lambda: contains(B246, 'THE MISSING SENTENCE, STATED AS THE THING THAT MUST BE '
                                         'SUPPLIED'),
          witness=lambda: contains(BANK, 'HALTS'))

    # 4 -- ### POSITIVE CONTROL ON AN ABSENCE: no verdict outside the three permitted.
    h.run('no-forbidden-verdict-word-CONTROLLED',
          check=lambda: no_forbidden_verdict(BANK),
          # ### THE CONTROL: the SAME predicate on the REGISTRATION, which names the forbidden
          # ### words in order to forbid them. ### So the matcher is shown able to FIND them, and
          # ### their absence from the bank means something.
          fixture=lambda: no_forbidden_verdict(REG),
          witness=lambda: contains(REG, 'are not verdicts and may not be written'))

    # 5 -- ### THE A-2 DISCRIMINATOR WAS REGISTERED BEFORE ITS NUMBER, AND IT IS RE-DERIVED HERE.
    h.run('A2-discriminator-registered-first-and-re-derived',
          check=lambda: (contains(REG, 'IS CONSTANT IN THE EIGENVALUE INDEX')
                         and contains(REG, 'REGISTERED AS THE TEST BEFORE THE NUMBER IS SEEN')
                         and xi1_is_not_constant()
                         and contains(BANK, '(DOUBLE-NAME)')),
          # ### FIXTURE: b212's own file, where `|alpha|` IS constant -- so the phrase is there but
          # ### the registration's sentence is not. ### FAILS ON AN ABSENT REGISTRATION SENTENCE.
          fixture=lambda: contains(B212, 'REGISTERED AS THE TEST BEFORE THE NUMBER IS SEEN'),
          witness=lambda: contains(B212, 'pi*Lambda'))

    # 6 -- ### THE IMPORT IS REFUSED, WITH ITS HYPOTHESIS CHECK **AND** ITS QUALIFIER.
    h.run('IMP3-refused-with-check-and-qualifier',
          check=lambda: (contains(BANK, 'THE IMPORT IS REFUSED')
                         and contains(BANK, 'NO PRIMARY WAS READ AT CONTENT IN THIS ACT')
                         and contains(BANK, 'REFUSING THE SECOND DOES NOT')
                         and contains(BANK, 'NOT REACHED')
                         and contains(B130, 'A CITATION IS NOT A LICENCE')),
          fixture=lambda: contains(B246, 'THE IMPORT IS REFUSED'),
          witness=lambda: contains(B130, 'Landau-Widom inapplicable'))

    # 7 -- ### THE ACT REPORTS THAT ITS OWN REGISTERED EXPECTATION NAMED THE WRONG CLAUSE.
    h.run('own-expectation-corrected-in-the-open',
          # ### THE THIRD CONJUNCT WAS A LEFTOVER -- `contains(BANK, 'AT\\n### ###   (i)') is False`,
          # ### a malformed pattern tested for falsity, which the whitespace-normalized matcher
          # ### resolved to True and so failed the gate on its first run. ### **THE GATE WAS RIGHT
          # ### TO FAIL: A CONJUNCT THAT ASSERTS NOTHING IS A CONJUNCT THAT CAN ASSERT ANYTHING.**
          # ### It is replaced by the assertion it was meant to make: that the halt is located at
          # ### clause (i)'s RATE, which is where the reading put it and NOT where I expected it.
          check=lambda: (contains(REG, 'I expect it to be writable whole EXCEPT for (iii)')
                         and contains(BANK, 'I named the wrong clause and the reading corrected me')
                         and contains(BANK, "CLAUSE (i)'s RATE IS NOT STATED BY ANY OWNER")
                         and contains(BANK, "THE STATEMENT HALTS HERE")),
          fixture=lambda: contains(B246, 'I named the wrong clause and the reading corrected me'),
          witness=lambda: contains(REG, '(iii)'))

    # 8 -- ### NO DERIVATION WAS PERFORMED, AND NO STEP IS MARKED DERIVES.
    h.run('no-derivation-performed-no-step-DERIVES',
          check=lambda: (contains(BANK, 'NO DERIVATION WAS PERFORMED')
                         and contains(BANK, 'IT IS NOT A DERIVATION AND IT IS NOT A STEP')
                         and not contains(BANK, 'SPECIES: ### **DERIVES')),
          # ### FIXTURE: the same absence test for a species string that IS present -- 'RESULT
          # ### owed' -- so the matcher is shown able to find a species line at all.
          fixture=lambda: not contains(BANK, 'RESULT owed'),
          witness=lambda: contains(BANK, 'SPECIES:'))

    # 9 -- ### CLAUSE (ii)'s FIRST DISJUNCT IS FALSE, RE-DERIVED FROM THE LAYER.
    h.run('clause-ii-first-disjunct-false-re-derived',
          check=lambda: (xi1sq_grows_on_certified_range()
                         and contains(BANK, "CLAUSE (ii)'s FIRST DISJUNCT IS FALSE")),
          # ### FIXTURE: the same growth test demanded of `lambda(n)^2`, which DECAYS. ### FAILS
          # ### on a real monotone-decreasing sequence -- a different object, not a negation.
          fixture=lambda: (lambda m: all(m[i] < m[i + 1] for i in range(6)))(
              __import__('prolate_layer').prolate(700)[2][0::2][:7]),
          witness=lambda: contains(BANK, 'A FACTOR OF ABOUT 36,000'))

    # 10 -- ### THE ROUTE'S BINDING STEP IS NAMED AND MADE A WORK-ORDER.
    h.run('binding-step-named-and-filed',
          check=lambda: (contains(BANK, "THIS IS THE ROUTE'S BINDING STEP")
                         and contains(BANK, 'W-ORD-FIXED-C-DECAY')
                         and contains(BANK, 'FILED, NOT RUN')),
          fixture=lambda: contains(B246, 'W-ORD-FIXED-C-DECAY'),
          witness=lambda: contains(BANK, 'S2'))

    # 11 -- ### THE DERIVATION ACT IS SPECIFIED AND AWAITS THE AUTHOR, WITH HALT CONDITIONS.
    h.run('derivation-act-specified-not-run',
          check=lambda: (contains(BANK, 'SPECIFIED AND NOT RUN')
                         and contains(BANK, "FILED FOR THE AUTHOR'S CONFIRMATION")
                         and contains(BANK, 'HALT CONDITIONS, FIXED IN ADVANCE')
                         and contains(BANK, 'NOT SCHEDULED BY THIS ACT')),
          fixture=lambda: contains(B246, 'HALT CONDITIONS, FIXED IN ADVANCE'),
          witness=lambda: contains(BANK, 'DERIVES-ON-IMPORTS AT CONTENT'))

    # 12 -- ### M-4 IS NOT CLAIMED PAID OR NEARLY SO.
    h.run('M4-not-claimed-paid',
          check=lambda: (contains(BANK, 'M-4 IS NOT PAID, NOT PAYABLE TODAY, AND NOT NEARLY SO')
                         and contains(BANK, 'M-2..M-5 STAND OPEN')),
          fixture=lambda: contains(B246, 'M-4 IS NOT PAID, NOT PAYABLE TODAY, AND NOT NEARLY SO'),
          witness=lambda: contains(BANK, 'M-4'))

    h.run('kernel-place-loom-untouched',
          check=lambda: (unmodified('D:/SIDE-global-section', 'Interfaces')
                         and unmodified('D:/MY-DOwnloads/PLACE-papers', 'VERIFICATION_LOOM.md')
                         and contains(BANK, 'THE LOOM AND THE MIRROR WERE NOT')),
          fixture=lambda: unmodified(ROOT, 'data/b247_m4_statement_and_route.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    h.run('ceiling-and-h2-in-every-artefact',
          check=lambda: all(contains(p, 'DECIDES NOTHING GLOBAL') for p in (REG, READS, BANK)),
          fixture=lambda: contains(os.path.join(ROOT, 'tools', 'lean', 'RESIDENCE.md'),
                                   'DECIDES NOTHING GLOBAL'),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    for row in h.rows:
        print('  %-52s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
