# -*- coding: utf-8 -*-
"""b232_checks.py -- the b232 gates, routed through the b217 harness.

### THIS ACT'S RISK IS ONE RISK, AND IT IS THE LARGEST THIS PROGRAMME HAS PUT IN FRONT OF
### THIS SEAT: ### THE NUMBERS ALREADY POINTED AT THE ANSWER BEFORE THE SOURCE WAS OPENED.
### act 12's residual collapses by an order of magnitude under the reading this act derived.
### ### A SIGN CHOSEN BECAUSE A COMPARISON COMES OUT IS b229's NAMED CRIME -- so the gates
### check the ROUTE, not the answer: that CC's display is quoted, that the refused evidence
### is quoted AS refused, and that no left-side value was touched.
### AND PER THE EXECUTION LINE, ### EVERY ABSENCE CARRIES A POSITIVE CONTROL -- b231 nearly
### filed a four-tree absence on a crashed `grep -iF`, and that crash RECURRED in this act.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
METHOD = os.path.join(PLACE, 'phase2', 'method')
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b232_sign_of_A.txt')
REG = os.path.join(D, 'b232_registration_2026-08-28.txt')
B230 = os.path.join(D, 'b230_engine_statement_and_price.txt')
B231 = os.path.join(D, 'b231_the_two.txt')
B179 = os.path.join(D, 'b179_enforcement_and_equivalence.txt')

CHAIN = os.path.join(METHOD, 'THE_IDENTITY_CHAIN.md')
POLICY = os.path.join(METHOD, 'CORE_TWO_BAR_POLICY.md')
SIGNARR = os.path.join(METHOD, 'SIGN_ARRANGEMENT_RECONCILIATION.md')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')
PRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')

# ### CC's EQUATION (1) AS DISPLAYED, AND THE SENTENCE THAT PUTS THE PRIMES ON THE RIGHT.
CC_EQ1 = 'f~(0) \u2212 \u03a3_{\u03c1\u2208Z} f~(\u03c1) + f~(1) = \u03a3_v \U0001d4b2_v(f)'
CC_PRIMES = 'involves only finitely many primes'


def contains(path, needle):
    """### REPAIRED AT b232, AND THE HARNESS'S WITNESS GUARD IS WHY.

    ### THE INHERITED HELPER READ THE FILE AS **BYTES** AND LOWERCASED IT WITH
    ### `bytes.lower()` (ASCII-ONLY), WHILE LOWERCASING THE NEEDLE AS A **STRING**
    ### (UNICODE-AWARE). ### For any needle carrying a non-ASCII capital -- and this act's
    ### needles carry `Σ`, `Ζ`, `\U0001d4b2` -- the needle became `σ` while the
    ### haystack kept `Σ`, and the comparison could NEVER match. ### THE CHECK WOULD HAVE
    ### SILENTLY SAID NO ABOUT A QUOTATION THAT WAS PRESENT.
    ### b229-b231 were unaffected only because their needles were ASCII. ### THE BUG WAS
    ### LATENT ACROSS THREE ACTS AND THIS IS THE FIRST ONE WHOSE QUOTATIONS EXPOSED IT.
    ### BOTH SIDES ARE NOW DECODED AND LOWERCASED AS TEXT."""
    if not os.path.isfile(path):
        return False
    with open(path, encoding='utf-8', errors='replace') as fh:
        return needle.lower() in fh.read().lower()


def both(path, a, b):
    return contains(path, a) and contains(path, b)


def count_lines(path):
    if not os.path.isfile(path):
        return -1
    with open(path, encoding='utf-8', errors='replace') as fh:
        return sum(1 for _ in fh)


def count_sub(path, needle):
    if not os.path.isfile(path):
        return -1
    with open(path, encoding='utf-8', errors='replace') as fh:
        return len(re.findall(re.escape(needle), fh.read(), re.I))


def pdf_sweep():
    """### THE LOCAL-COPY SWEEP, IN-PROCESS. Returns (total_pdfs, cc_hits).
    ### total_pdfs IS THE POSITIVE CONTROL: if it is zero the sweep is broken and its
    ### zero for cc_hits means NOTHING (b231's crashed-grep species)."""
    total = cc = 0
    for dirpath, dirs, files in os.walk('D:/'):
        if dirpath.count(os.sep) > 5 or '$RECYCLE' in dirpath or '.git' in dirpath:
            dirs[:] = []
            continue
        for fn in files:
            if fn.lower().endswith('.pdf'):
                total += 1
                low = fn.lower()
                if '2006.13771' in low or ('weil' in low and 'positiv' in low):
                    cc += 1
    return total, cc


def file_unmodified(repo, relpath):
    """### THE FILE IS NOT EDITED BY THIS ACT: git reports no change against HEAD."""
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    if r.returncode != 0:
        return False
    return r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b232')

    # 1 -- ### CC's EQUATION (1) IS QUOTED AS DISPLAYED, WITH THE SENTENCE THAT ORIENTS IT.
    h.run('cc-equation-1-quoted-with-orientation',
          check=lambda: both(BANK, CC_EQ1, CC_PRIMES),
          fixture=lambda: both(B230, CC_EQ1, CC_PRIMES),
          witness=lambda: both(CHAIN, CC_EQ1, CC_PRIMES))

    # 2 -- ### THE IDENTIFIER IS CORRECTED: 2112.05500 is Connes-MOSCOVICI, not CC.
    h.run('ferry-identifier-corrected-at-content',
          check=lambda: both(BANK, 'Connes-Moscovici', '2006.13771'),
          fixture=lambda: both(FILE_E, 'Connes-Moscovici', '2006.13771'),
          witness=lambda: both(REG, 'Connes-Moscovici', '2006.13771'))

    # 3 -- ### THE REFUSED EVIDENCE IS QUOTED **AS REFUSED**. ### THIS IS THE ACT'S CENTRAL
    # ### GATE: the residual numbers must appear AND be marked as not used.
    h.run('residual-quoted-as-refused-not-used',
          check=lambda: both(BANK, '+4.049', 'DID NOT USE THEM'),
          fixture=lambda: both(B231, '+4.049', 'DID NOT USE THEM'),
          # ### THE FIRST WITNESS HERE WAS `the named crime` AND THE HARNESS REFUSED THE
          # ### CHECK: the bank carries the phrase LINE-WRAPPED (`the named` / `crime`), so
          # ### the exact substring is absent. ### b227's SPECIES -- a wrap silently breaks a
          # ### quotation -- CAUGHT BY b217's SECOND GUARD.
          witness=lambda: both(BANK, '+4.049', 'BEING RIGHT BY THE WRONG ROUTE'))

    # 4 -- ### THE STANDING-CLAUSE CHECK NAMES WHERE THE SIGN CAME FROM AND WHERE IT DID NOT.
    h.run('standing-clause-check-shown-both-halves',
          check=lambda: both(BANK, 'WHERE THE SIGN CAME FROM', 'WHERE IT DID NOT COME FROM'),
          fixture=lambda: both(B230, 'WHERE THE SIGN CAME FROM', 'WHERE IT DID NOT COME FROM'),
          witness=lambda: contains(BANK, 'THE ROUTE IS WHAT WAS AUDITED HERE, NOT THE ANSWER'))

    # 5 -- ### THE LOCAL-COPY ABSENCE, WITH ITS POSITIVE CONTROL IN THE SAME GATE.
    # ### THE FIXTURE IS THE CONTROL INVERTED: if the sweep found NO pdfs at all it is broken,
    # ### and a broken sweep's zero must REFUSE the check rather than pass it.
    h.run('no-local-cc-copy-with-positive-control',
          check=lambda: (lambda t, c: t > 0 and c == 0)(*pdf_sweep()),
          fixture=lambda: pdf_sweep()[0] == 0,
          witness=lambda: pdf_sweep()[0] > 0)

    # 6 -- ### THE SUB-ASSUMPTION IS DISCLOSED, NOT PAPERED OVER.
    h.run('finite-place-subassumption-disclosed',
          check=lambda: both(BANK, 'NOT in the retrieved text', 'sub-assumption'),
          fixture=lambda: both(B231, 'NOT in the retrieved text', 'sub-assumption'),
          witness=lambda: both(CHAIN, 'not in the retrieved text', 'sub-assumption'))

    # 7 -- ### wInf ADOPTED WITH ITS PROVENANCE, AND THE STATEMENT DECLARED COMPLETE.
    h.run('winf-adopted-and-statement-complete',
          check=lambda: both(BANK, 'COMPLETE AT CELL LEVEL', 'b38_act10.py'),
          fixture=lambda: both(B230, 'COMPLETE AT CELL LEVEL', 'b38_act10.py'),
          witness=lambda: contains(CHAIN, 'COMPLETE AT CELL LEVEL'))

    # 8 -- ### THE IMPORT LEDGER IS OPEN, WITH ITS HEAD SENTENCE AND BOTH ENTRIES.
    h.run('import-ledger-opened-with-head-sentence',
          check=lambda: (contains(CHAIN, 'IMPORTS ARE ENUMERATED LIKE AXIOMS')
                         and contains(CHAIN, 'IMP-1') and contains(CHAIN, 'IMP-2')),
          fixture=lambda: (contains(SIGNARR, 'IMPORTS ARE ENUMERATED LIKE AXIOMS')
                           and contains(SIGNARR, 'IMP-1') and contains(SIGNARR, 'IMP-2')),
          witness=lambda: (contains(BANK, 'IMPORTS ARE ENUMERATED LIKE AXIOMS')
                           and contains(BANK, 'IMP-1') and contains(BANK, 'IMP-2')))

    # 9 -- ### THE TWO-BAR POLICY IS FILED AND THE EXISTING PROFILE IS UNTOUCHED.
    h.run('two-bar-policy-filed-profile-untouched',
          check=lambda: (contains(POLICY, 'Two bars, explicit')
                         and count_lines(PRINTS) == 404
                         and count_sub(PRINTS, 'depends on axioms') == 0),
          fixture=lambda: (contains(SIGNARR, 'Two bars, explicit')
                           and count_lines(PRINTS) == 404),
          witness=lambda: contains(POLICY, 'Two bars, explicit'))

    # 10 -- ### THE SECOND ARRANGEMENT QUESTION IS NAMED AND EXPLICITLY NOT DECIDED.
    h.run('second-arrangement-question-not-decided',
          check=lambda: both(BANK, 'second convention question', 'does not decide it'),
          fixture=lambda: both(B231, 'second convention question', 'does not decide it'),
          witness=lambda: both(CHAIN, 'second convention question', 'does not decide it'))

    # 11 -- ### NOTHING THIS ACT TOUCHED WAS A STATED OBJECT OR A DEPOSITED ARTIFACT.
    # ### File E is QUOTED, not edited; SIGN_ARRANGEMENT's proposed repair is NOT applied.
    h.run('file-E-and-sign-arrangement-unedited',
          check=lambda: (file_unmodified(SGS, 'Interfaces/FiniteInstanceIdentity.lean')
                         and file_unmodified(PLACE,
                                             'phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md')),
          fixture=lambda: file_unmodified(PLACE, 'phase2/method/THE_IDENTITY_CHAIN.md'),
          witness=lambda: file_unmodified(SGS, 'Interfaces/FiniteInstanceIdentity.lean'))

    # 12 -- ### b179's INDEPENDENT READ OF THE SAME WORK IS CARRIED, so the source is not
    # ### resting on a single fetch of a single renderer.
    h.run('source-corroborated-by-prior-read',
          check=lambda: both(B179, '2006.13771', 'Connes-Consani'),
          fixture=lambda: both(B230, '2006.13771', 'Connes-Consani'),
          witness=lambda: contains(BANK, 'Theorem 1'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
