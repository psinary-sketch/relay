# -*- coding: utf-8 -*-
"""b327_source.py -- THE BRIDGE'S SOURCE, PINNED AND LOCATED. ### **A READ, NOT A VERDICT.**

### ### **THE FLATTENER AND THE HASH CHECK ARE IMPORTED FROM `b305_source.py`, NEVER COPIED.**

### ### **WHICH SOURCE, AND WHY THIS ONE.** ### The order asks for *the classical identification of
### the Li coefficients as the Weil functional on a stated test-function family, located in a real
### source under the import bar and quoted.* ### The corpus's own pentagon module names the
### citation as ### *Bombieri-Lagarias 1999, via the Guinand-Weil explicit formula* ### (`read_pentagon.txt`).
### ### **THAT PAPER WAS NOT OBTAINABLE BY THIS SEAT**: the publisher's copy and the open-archive
### mirror both refused the fetch (HTTP 403), and this act does not quote a paper it cannot hash.
### ### **THE SOURCE READ INSTEAD IS THE SAME AUTHOR'S RESTATEMENT OF THE SAME RESULT**,
### J. C. Lagarias, *Li coefficients for automorphic L-functions*, arXiv:math/0404394v4 (2005),
### which states the identification in its own voice (its §3, Theorem 3.1; its §4, Lemma 4.2 and
### (4.11)), restates Bombieri-Lagarias's Theorem 2 as its (1.11)/(4.6) at `pi = pi_triv`, and
### carries the explicit formula's trace form in its appendix. ### **THE IMPORT IS THEREFORE
### GRADED AT THIS SOURCE**, and the 1999 paper is named as the citation it restates.

### ### **THE ARTEFACT WAS RE-ACQUIRED BY FETCH IN THIS SESSION AND IS PINNED BY HASH HERE.** ### No
### prior act pinned it, so the pin below is THIS ACT'S and a later act must match it or stop.
### The corpus records no path for pinned artefacts (`W-ORD-ARTEFACT-PATHS`); the fetch cache's
### path is printed so the next reader knows where this session found it, and knows it is
### ephemeral.

### ### **WHAT IT DOES NOT DO: IT DOES NOT READ.** ### It locates fragments the bank quotes and fails
### loudly when one is absent. ### **IT CANNOT TELL A CORRECT QUOTATION FROM AN INVENTED ONE.**
"""
import glob
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b305_source as S5  # noqa: E402  ### the flattener and the hash check are READ, never copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OUT = os.path.join(ROOT, 'data', 'b327_source.txt')
TEXT = os.path.join(ROOT, 'data', 'b327_source_text.txt')

ARXIV = 'arXiv:math/0404394v4'
EXPECT_SHA = '86f3d3c49f5a889f121bb1f04f67694cb9066dc8360f6988165788679594a4a7'
EXPECT_BYTES = 423379
CACHE_GLOB = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', '*',
                          'tool-results', 'webfetch-*.pdf')

# ### THE FRAGMENTS THE BANK QUOTES. ### **EACH IS THE LOAD-BEARING PHRASE OF A CLAIM**, searched
# ### flattened on BOTH sides (b305's fixture: a needle that never went through the normaliser).
FRAGMENTS = [
    ('A1 the abstract: the coefficients related to Weil\'s quadratic functional on test functions',
     'We relate these co', 'to values of Weil'),
    ('A2 ### the same sentence, its object',
     'quadratic functional associated to the representation', 'on a suitable set of test functions'),
    ('B1 the arithmetic formula restated from [4, Theorem 2]',
     'the explicit formula of prime number theory may be used to obtain an arithmetic expression',
     None),
    ('B2 ### its three terms named: archimedean, finite, and the pole',
     'correspond to the contributions of the archimedean place and the finite places',
     'the last term is a contribution from the pole at s = 0'),
    ('B3 ### Weil positivity encoded by each Li positivity',
     'encodes', 'of Weil\'s quadratic functional for a particular test function'),
    ('C1 the Li test functions, (3.2)', 'The special test functions Gn(s)', 'corresponding to the Li coefficients'),
    ('C2 Theorem 3.1, the Weil scalar product on the Li basis', 'For the Li test functions Gn(s)', 'there holds'),
    ('C3 ### its (3.4): the norm is twice the real part of lambda_n', '2', 'Weil scalar product with respect to this basis'),
    ('D1 Definition 4.1, the archimedean coefficients tau', 'The coefficents', 'are defined by'),
    ('D2 ### with (4.4), the gamma factor\'s log-derivative', 'in which we have using (2.3) that', None),
    ('D3 Lemma 4.2, (4.6): lambda_n = S_inf - S_f + delta', 'Then for all n', 'in which'),
    ('D4 ### delta = 1 for the trivial representation', 'if', 'and', ),
    ('D5 ### the archimedean and finite attributions, and the two singularities',
     'corresponds to the contribution of the archimedean primes', 'corresponds to the finite primes'),
    ('D6 ### the pole at s = 0 remains and contributes the constant',
     'contribution cancels against the singularity at s = 1', 'the s = 0 singularity remains and contributes the constant'),
    ('D7 (4.11), the closed form of S_inf at the trivial representation', 'form parts of the arithmetic', None),
    ('D8 ### its zeta-star at 1', 'where', 'is Euler'),
    ('E1 Theorem 5.1, the unconditional asymptotic of S_inf', 'the quantities S', 'are real-valued'),
    ('E2 ### (5.4) the constant for the Li coefficients', 'For the Li coefficients we have', None),
    ('F1 the appendix: the Weil distribution functional (9.3)', 'We define the Weil distribution functional', None),
    ('F2 ### the trace functional (9.4) and the spectral side', 'We then define the trace functional', 'spectral side'),
    ('F3 ### the trace form (9.5), a contribution per place',
     'is a contribution associated to each', 'place'),
]


def locate_pdf():
    hits = []
    for p in glob.glob(CACHE_GLOB):
        try:
            if os.path.getsize(p) == EXPECT_BYTES and S5.sha256_file(p) == EXPECT_SHA:
                hits.append(p)
        except OSError:
            pass
    return hits


def main():
    lines = []

    def rec(s=''):
        lines.append(s)
        print(s)

    rec('=' * 100)
    rec('b327_source.py -- THE BRIDGE\'S SOURCE, PINNED AND LOCATED. ### THE FLATTENER IS b305\'s, IMPORTED.')
    rec('=' * 100)
    ok = bool(S5.self_test(verbose=False))
    rec('  b305 flattener self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        rec('  ### REFUSING TO LOCATE WITH A FLATTENER THAT FAILS ITS OWN FIXTURES.')
        return 2
    rec('  source        : J. C. Lagarias, Li coefficients for automorphic L-functions, %s' % ARXIV)
    rec('  restates      : E. Bombieri and J. C. Lagarias, Complements to Li\'s criterion for the Riemann')
    rec('                  hypothesis, J. Number Theory 77 (1999) 274-287 -- its [4]; NOT obtainable by this seat (HTTP 403 twice)')
    rec('  expected      : %d bytes, sha256 %s' % (EXPECT_BYTES, EXPECT_SHA))
    found = locate_pdf()
    rec('  copies matching the pin in this machine\'s fetch caches : %d' % len(found))
    for p in found:
        rec('      %s' % p)
    if not found:
        rec('  ### HARD FAILURE -- NO COPY MATCHES THE PIN. ### RE-FETCH %s AND COMPARE; A MISMATCH IS A' % ARXIV)
        rec('  ### DIFFERENT DOCUMENT AND THE ACT STOPS.')
        io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 2
    pdf = found[0]
    rec('  ### THE PIN IS THIS ACT\'S. ### A RE-ACQUISITION THAT MATCHES IT IS THE PINNED ARTEFACT.')

    import pypdf
    reader = pypdf.PdfReader(pdf)
    pages = [(pg.extract_text() or '') for pg in reader.pages]
    full = '\n'.join('=== PAGE %d ===\n%s' % (i + 1, t) for i, t in enumerate(pages))
    io.open(TEXT, 'w', encoding='utf-8', newline='\n').write(full)
    rec('  pages         : %d ; text layer written to data/%s (%d chars)' % (len(pages), os.path.basename(TEXT), len(full)))
    flat_pages = [S5.flatten(t) for t in pages]

    rec('')
    rec('  ### THE FRAGMENTS, EACH SEARCHED FLATTENED ON BOTH SIDES; A MISS IS LOUD.')
    missing = 0
    for lbl, a, b in FRAGMENTS:
        fa, fb = S5.flatten(a), (S5.flatten(b) if b else None)
        where = [i + 1 for i, fp in enumerate(flat_pages) if fa in fp and (fb is None or fb in fp)]
        if not where:
            missing += 1
        rec('    %-88s pages %s %s' % (lbl[:88], where if where else '-', '' if where else '### NOT LOCATED ###'))
    rec('')
    rec('  ### FRAGMENTS NOT LOCATED : %d' % missing)
    rec('  ### **THIS TOOL LOCATES. ### IT DOES NOT READ, AND IT CANNOT TELL A CORRECT QUOTATION FROM')
    rec('  ### AN INVENTED ONE.** ### The quotations in the bank are this seat\'s read of the located pages.')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0 if not missing else 5


if __name__ == '__main__':
    sys.exit(main())
