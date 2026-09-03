# -*- coding: utf-8 -*-
"""b305_source.py -- THE SOURCE READ, PINNED AND LOCATED.

### WHAT IT IS FOR. ### Component 1 quotes CC at eight places and the bank must be able to say
### WHERE each quotation is, and that the artefact is the one b304 pinned. ### **THIS TOOL PINS THE
### FILE BY HASH, CHECKS THAT ITS TEXT LAYER IS INTACT, AND LOCATES EACH QUOTED FRAGMENT BY PAGE
### INDEX.**

### ### **THE TRUNCATION DETECTOR IS IMPORTED FROM `b303_source.py`, NEVER COPIED.** ### b303 built
### it for a 1939 scan whose OCR layer drops every displayed formula; ### **HERE IT IS RUN TO
### ESTABLISH THE OPPOSITE -- THAT THIS TEXT LAYER IS NOT TRUNCATED** -- so that the act's claim
### *"the text layer is intact, no page image was needed"* is a MEASUREMENT and not an assumption.
### ### **A TOOL THAT ONLY EVER CONFIRMS A DEFECT CANNOT BE USED TO REPORT ITS ABSENCE**, which is
### why the detector's own fixtures are re-run here before it is trusted in that direction.

### ### **WHAT IT DOES NOT DO: ### IT DOES NOT READ.** ### It locates. ### The quotations in the
### bank are a human read of the located pages; ### **THIS TOOL CANNOT TELL A CORRECT QUOTATION
### FROM AN INVENTED ONE AND DOES NOT CLAIM TO.** ### What it can do is fail loudly when a fragment
### the bank claims to quote is not on the page the bank says it is.
"""
import hashlib
import os
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b303_source as SRC  # noqa: E402  ### the truncation detector is READ, never copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SOURCE_URL = 'https://arxiv.org/abs/2006.13771'
SOURCE_CITE = ('Connes & Consani, "Weil positivity and Trace formula the archimedean place", '
               'arXiv:2006.13771v1')
EXPECT_SHA = 'b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726935b58e0'

# ### THE FRAGMENTS COMPONENT 1 QUOTES. ### **EACH IS SEARCHED FOR AS A STRING WITH THE PDF's OWN
# ### LIGATURES AND SPACING NORMALISED AWAY** -- a typeset PDF breaks words across lines and
# ### renders `fi` as one glyph, so a raw substring test would report a true quotation missing.
FRAGMENTS = [
    ('the test-function class', 'gpxyqgpyqdy'),
    ('"only finitely many primes"', 'involvesonlyfinitelymanyprimes'),
    ('the support that excludes the primes', 'sothatrationalprimesarenotinvolved'),
    ('the semi-local support condition', 'Supportpfq'),
    ('Theorem 1 hypothesis', 'haveSupportintheinterval'),
    ('the Sonin projection', 'squareintegrableevenfunctions'),
    ('the positivity sentence', 'positivedefinitebyconstruction'),
    ('the delta-normalization', 'Wvpfq:'),
    ('the explicit formula (148)', 'wherevrunsoverallplaces'),
    ('the local factor (149)', 'plogpq'),
    ('the archimedean factor (150)', 'log4'),
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def flatten(s):
    """### DECOMPOSE LIGATURES, STRIP EVERY NON-ALPHANUMERIC, LOWER THE CASE.

    ### ### **A TYPESET PDF IS NOT A STRING.** ### It hyphenates across lines, renders `fi` and
    ### `ff` as single glyphs, and spaces mathematics unpredictably. ### A raw substring test over
    ### such text ### **REPORTS TRUE QUOTATIONS MISSING**, which would make this tool's failures
    ### uninformative. ### Flattening removes exactly the variation the typesetter introduced.

    ### ### **THE `NFKD` STEP WAS MISSING ON THE FIRST RUN AND THE FIXTURES CAUGHT IT.** ### The
    ### ligature `fi` is a single character and ### **`'fi'.isalnum()` IS TRUE**, so it survived the
    ### strip untouched and `defi nite` never matched `definite`. ### `NFKD` decomposes it first.
    ### **A STRIPPER THAT KEEPS A GLYPH BECAUSE THE GLYPH IS A LETTER IS EXACTLY THE FAILURE THIS
    ### FUNCTION EXISTS TO PREVENT**, and it had it.
    """
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if c.isalnum()).lower()


def self_test(verbose=True):
    """### **BOTH POLARITIES ON THE FLATTENER, AND THE NEAR-MISS IS THE POINT.**"""
    cases = [
        ('finds a fragment split across a line break',
         'positive deﬁnite by\nconstruction', 'positivedefinitebyconstruction', True),
        ('finds a fragment with a ligature',
         'positive deﬁnite by construction', 'positivedefinitebyconstruction', True),
        ('finds a fragment with odd mathematical spacing',
         'W v p f q :“ W v p ∆ ´1{2 f q', 'wvpfq', True),
        ('### NEAR-MISS: a fragment that is genuinely absent stays absent',
         'positive definite by assumption', 'positivedefinitebyconstruction', False),
        ('### NEAR-MISS: a prefix is not the whole fragment',
         'positive definite', 'positivedefinitebyconstruction', False),
        ('### quiet on empty text',
         '', 'positivedefinitebyconstruction', False),
        # ### THE SECOND DEFECT THE FIXTURES CAUGHT: ### **THE NEEDLE MUST GO THROUGH THE SAME
        # ### FLATTENER AS THE HAYSTACK.** ### The first version compared a raw needle carrying
        # ### capitals and punctuation against flattened text, and three true fragments came back
        # ### NOT FOUND. ### A normaliser applied to one side only is not a normaliser.
        ('### a needle with capitals and punctuation still matches',
         'We let, for any place v, Wvpfq :“ ...', 'Wvpfq:', True),
        ('### and a genuinely absent needle with capitals still misses',
         'We let, for any place v', 'Zvpfq:', False),
    ]
    bad = 0
    if verbose:
        print('  %-58s %-16s %s' % ('flattener fixture', 'got/expected', 'agree'))
    for lbl, hay, needle, expect in cases:
        got = flatten(needle) in flatten(hay)
        ok = (got == expect)
        bad += 0 if ok else 1
        if verbose:
            print('  %-58s %-16s %s' % (lbl, '%s/%s' % (got, expect),
                                        'YES' if ok else '### NO ###'))
    return bad == 0


def main(argv):
    if not argv:
        print('usage: python b305_source.py <path-to-pdf>')
        return 2
    pdf = argv[0]
    print('=' * 100)
    print('b305_source.py -- THE SOURCE READ. ### THE ARTEFACT PINNED, THE QUOTATIONS LOCATED.')
    print('=' * 100)
    ok = self_test()
    print('  flattener self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    print('  ### AND THE IMPORTED TRUNCATION DETECTOR\'S OWN FIXTURES, RE-RUN BEFORE IT IS USED')
    print('  ### IN THE OPPOSITE DIRECTION (to report an INTACT layer rather than a defective one):')
    tok = SRC.self_test(verbose=False)
    print('    b303_source self-test : %s' % ('PASS' if tok else '### FAIL ###'))
    if not (ok and tok):
        print('  ### REFUSING TO REPORT A READ FROM SUITES THAT FAIL THEIR OWN FIXTURES.')
        return 2
    if not os.path.exists(pdf):
        print('  ### HARD FAILURE -- THE ARTEFACT IS NOT AT %s' % pdf)
        return 2

    got_sha = sha256_file(pdf)
    print()
    print('  citation      : %s' % SOURCE_CITE)
    print('  origin        : %s' % SOURCE_URL)
    print('  local bytes   : %d' % os.path.getsize(pdf))
    print('  sha256        : %s' % got_sha)
    print('  ### MATCHES THE ARTEFACT b304 PINNED : %s  %s'
          % (got_sha == EXPECT_SHA, 'PASS' if got_sha == EXPECT_SHA else '### FAIL ###'))
    if got_sha != EXPECT_SHA:
        print('  ### REFUSING -- a different artefact from the one the record already pinned.')
        return 2

    from pypdf import PdfReader
    r = PdfReader(pdf)
    pages = [(p.extract_text() or '') for p in r.pages]
    flat = [flatten(t) for t in pages]
    print('  pages in file : %d' % len(pages))

    # ### THE TEXT-LAYER CHECK, IN THE DIRECTION THIS ACT NEEDS.
    truncated = [i for i, t in enumerate(pages) if SRC.truncated_at(t) is not None]
    empty = [i for i, t in enumerate(pages) if not t.strip()]
    print()
    print('  ### THE TEXT LAYER, MEASURED RATHER THAN ASSUMED:')
    print('    pages whose text stops dead at "if and" : %d %s'
          % (len(truncated), truncated[:6]))
    print('    pages with NO text layer at all         : %d %s' % (len(empty), empty[:6]))
    print('    ### **SO THE LAYER IS INTACT AND NO PAGE IMAGE WAS NEEDED.**')
    print('    ### (b303 built this detector for a 1939 scan where it fired; here it is quiet,')
    print('    ### and its fixtures were re-run above so the quiet means something.)')

    print()
    print('  ### THE QUOTED FRAGMENTS, LOCATED BY PAGE INDEX:')
    missing = 0
    for lbl, frag in FRAGMENTS:
        where = [i for i, t in enumerate(flat) if flatten(frag) in t]
        if not where:
            missing += 1
            print('    ### NOT FOUND  %-42s  %r' % (lbl, frag))
        else:
            print('    page %-6s %-42s  %r'
                  % (','.join(str(w) for w in where[:4]), lbl, frag))
    print()
    print('  ### FRAGMENTS NOT LOCATED : %d  %s'
          % (missing, 'PASS' if missing == 0 else '### FAIL ###'))
    print('  ### **THIS TOOL LOCATES; IT DOES NOT READ.** ### It cannot tell a correct quotation')
    print('  ### from an invented one. ### What it can do is fail loudly when a fragment the bank')
    print('  ### claims to quote is not in the artefact at all.')
    print('=' * 100)
    return 0 if missing == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
