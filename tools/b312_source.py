# -*- coding: utf-8 -*-
"""b312_source.py -- THE SOURCE'S REMAINDER, PINNED AND LOCATED.

### ### **THE FLATTENER AND THE HASH CHECK ARE IMPORTED FROM `b305_source.py`, NEVER COPIED** --
### the standing design point, carried since b305 and re-used at b311.

### ### ### **AND THIS ACT ADDS A DECLARATION THE EARLIER ONES DID NOT NEED: ### THE FLATTENER IS
### ### ### UNABLE TO SEE THE ONE CHARACTER THIS ACT TURNS ON.** ### It strips every
### non-alphanumeric character,
### so the source's `rho^{+1/2}` and a hypothetical `rho^{-1/2}` flatten to the SAME STRING.
### ### **A LOCATOR THAT CANNOT SEE A MINUS SIGN CANNOT DECIDE A QUESTION ABOUT A MINUS SIGN**, and
### this tool therefore LOCATES ONLY. ### The sign is read by `b312_definitions.py` off the RAW,
### UNFLATTENED page text, and that separation is the whole reason there are two tools.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b305_source as S5  # noqa: E402  ### the flattener and the hash check are READ, never copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXPECT_SHA = S5.EXPECT_SHA
EXPECT_BYTES = 1213504

# ### THE FRAGMENTS THIS ACT'S COMPONENTS QUOTE. ### **EACH IS THE LOAD-BEARING PHRASE OF A CLAIM
# ### THE BANK MAKES**, and each is searched flattened, which is why none of them is asked to carry
# ### the sign.
FRAGMENTS = [
    # --- Component 1: the source's identity and the function it defines ---
    ('S1 Theorem 4.7 -- the trace side equals the distribution plus the function',
     'TrpϑpfqSq“ W8pfq'),
    ('S2 the defining equation of the source\'s remainder',
     '1´λpnq2xξn|ϑpρ´1qζny'),
    ('S3 the symmetry the source imposes on it', 'ϵpρ´1q“ ϵpρq'),
    ('S4 the OTHER equation, the one about delta -- NOT the remainder\'s',
     'fpρ´1qδpρqd˚ρ“ Tr'),
    # --- Component 1: the source's scaling action, its definition and its unitarity ---
    ('S5 the scaling action, DEFINED', 'pϑpλqξqpvq :“ λ´1{2ξpλ´1vq'),
    ('S6 and declared UNITARY, by conjugation of a unitary representation',
     'be the unitary representation ϑm conjugated by the isomorphism'),
    ('S7 the source UNFOLDING an inner product of exactly the remainder\'s shape',
     'xψn|ϑpρ´1qξny“ ρ1{2'),
    # --- Component 1: the auxiliary vector, and the unfolded remainder ---
    ('S8 the auxiliary vector in terms of the analytic continuation',
     'ζnpxq“ 1a 1´λpnq2ηnpxq“ λpnqa 1´λpnq2ξan n pxq'),
    ('S9 the remainder UNFOLDED by the source itself',
     'ρ1{2 ż 1 ρ´1 ξan n pxqξan n pρxqdx'),
    ('S10 the analytic continuation agrees at the endpoint', 'ξan\nn p1q“ ξnp1q'),
    ('S11 the normalization of the inner product, named by the source',
     'recalling the normalization (16)'),
    # --- Component 1/2: the jump, and the operator-image equation ---
    ('S12 the derivative jump at the identity', 'Lemma 5.4 The derivative of ϵpρq at ρ“ 1'),
    ('S13 the jump, stated of the function', 'has a jump in its derivative at ρ“ 1'),
    ('S14 the operator image, its leading factor', 'Cn“ρ1{2'),
    ('S15 the operator image before the derivative substitution',
     'pDuξnqpxqpDuζnqpρxqdx'),
    # --- Component 2: the numbers the source publishes, QUOTED and not computed ---
    ('S16 the source\'s own tabulated terms', 'tp0q“ 11.9719'),
    ('S17 the linear form the remainder is integrated against',
     'fpxqϵpexpp|x|qqdx'),
]


def locate(pdf):
    """### **EVERY FRAGMENT'S PAGE INDICES, BY THE IMPORTED FLATTENER.**"""
    from pypdf import PdfReader
    r = PdfReader(pdf)
    pages = [S5.flatten(p.extract_text() or '') for p in r.pages]
    out = []
    for label, frag in FRAGMENTS:
        f = S5.flatten(frag)
        hits = [i for i, p in enumerate(pages) if f in p]
        out.append((label, frag, hits))
    return out, len(r.pages)


def insensitivity_fixture():
    """### **THE FLATTENER'S INSENSITIVITY, DEMONSTRATED RATHER THAN ASSERTED.**"""
    plus = S5.flatten('ρ1{2')
    minus = S5.flatten('ρ´1{2')
    return plus, minus, (plus == minus)


def main(argv):
    if not argv:
        print('usage: python b312_source.py <path-to-pdf>')
        return 2
    pdf = argv[0]
    print('=' * 100)
    print('b312_source.py -- THE SOURCE\'S REMAINDER. ### PINNED, THEN LOCATED.')
    print('=' * 100)
    print('  ### THE FLATTENER\'S OWN FIXTURES, IMPORTED FROM b305 AND RE-RUN BEFORE IT IS USED:')
    if not S5.self_test():
        print('  ### REFUSING TO LOCATE ANYTHING WITH A FLATTENER THAT FAILS ITS OWN FIXTURES.')
        return 2

    if not os.path.exists(pdf):
        print('  ### HARD FAILURE -- THE ARTEFACT IS NOT AT %s' % pdf)
        return 2
    got_sha = S5.sha256_file(pdf)
    size = os.path.getsize(pdf)
    print()
    print('  artefact      : %s' % os.path.basename(pdf))
    print('  local bytes   : %d   (the corpus\'s pin expects %d)' % (size, EXPECT_BYTES))
    print('  sha256        : %s' % got_sha)
    print('  ### MATCHES THE ARTEFACT b304 PINNED AND b305 RE-COMPUTED : %s  %s'
          % (got_sha == EXPECT_SHA, 'PASS' if got_sha == EXPECT_SHA else '### FAIL ###'))
    if got_sha != EXPECT_SHA:
        print('  ### REFUSING TO READ. ### A document that does not match the pin is a DIFFERENT')
        print('  ### document, whatever its name, and this act stops here.')
        return 2

    plus, minus, insensitive = insensitivity_fixture()
    print()
    print('  ### ### **THE FLATTENER\'S INSENSITIVITY, MEASURED BEFORE IT IS TRUSTED:**')
    print('      the source\'s exponent flattens to    : %r' % plus)
    print('      a sign-flipped one flattens to        : %r' % minus)
    print('      ### **THE TWO ARE INDISTINGUISHABLE : %s**' % insensitive)
    print('  ### **SO THIS TOOL LOCATES AND DOES NOT DECIDE.** ### The sign is read off the RAW page')
    print('  ### text by `b312_definitions.py`, and that is why this act has two tools and not one.')
    if not insensitive:
        print('  ### THE INSENSITIVITY FIXTURE DID NOT BEHAVE AS DECLARED -- REFUSING.')
        return 2

    rows, npages = locate(pdf)
    print()
    print('  pages in file : %d' % npages)
    print()
    print('  ### THE QUOTED FRAGMENTS, LOCATED BY PAGE INDEX:')
    missing = []
    for label, frag, hits in rows:
        if not hits:
            missing.append(label)
        print('    %-12s %-70s %s'
              % (','.join(str(h) for h in hits) if hits else '### NONE',
                 label, S5.flatten(frag)[:34]))
    print()
    print('  ### FRAGMENTS NOT LOCATED : %d  %s'
          % (len(missing), 'PASS' if not missing else '### FAIL ###'))
    for m in missing:
        print('      ### %s' % m)
    print('  ### **THIS TOOL LOCATES; IT DOES NOT READ.** ### It cannot tell a correct quotation')
    print('  ### from an invented one, and it cannot see a sign at all.')
    print('=' * 100)
    return 0 if not missing else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
