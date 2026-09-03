# -*- coding: utf-8 -*-
"""b311_source.py -- THE SOURCE'S PROOF, PINNED AND LOCATED.

### ### **THE FLATTENER AND THE HASH CHECK ARE IMPORTED FROM `b305_source.py`, NEVER COPIED** --
### the standing design point. ### b305 built the flattener for this same artefact and its own
### fixtures caught two defects in it (a surviving ligature, and a needle that never went through
### the normaliser). ### **A THIRD COPY WOULD BE A THIRD PLACE FOR THOSE TO COME BACK.**

### ### ### **WHAT IS NEW HERE, AND IT IS A DECLARATION BEFORE IT IS A TOOL: ### THE LOCAL COPY OF
### ### ### THE ARTEFACT WAS NOT FOUND ON THIS MACHINE.** ### b304 pinned it and b305 re-computed
### the pin; neither bank records a path, and a search of the drives did not turn it up.
### ### **THE ARTEFACT WAS THEREFORE RE-ACQUIRED FROM `arXiv` AND CHECKED AGAINST THE CORPUS'S OWN
### ### PIN BEFORE A WORD OF IT WAS READ: ### 1213504 BYTES, sha256 `b8e0b54a...`, BYTE-IDENTICAL.**
### ### **A RE-ACQUISITION THAT MATCHES THE PIN IS THE PINNED ARTEFACT. ### ONE THAT DID NOT MATCH
### ### WOULD HAVE BEEN A DIFFERENT DOCUMENT AND THIS ACT WOULD HAVE STOPPED**, which is the whole
### reason the corpus pins by hash rather than by name.

### ### **WHAT IT DOES NOT DO: ### IT DOES NOT READ.** ### It locates. ### The quotations in the
### bank are this seat's read of the located pages; ### **THIS TOOL CANNOT TELL A CORRECT QUOTATION
### FROM AN INVENTED ONE.** ### What it can do is fail loudly when a fragment the bank claims to
### quote is not in the artefact at all.
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

# ### THE FRAGMENTS THIS ACT'S COMPONENTS 1 AND 2 QUOTE. ### **EACH IS THE LOAD-BEARING PHRASE OF A
# ### CLAIM THE BANK MAKES, AND EACH IS SEARCHED FLATTENED.**
FRAGMENTS = [
    # --- Component 1: the construction, and what the trace side is ---
    ('C1a the construction, and that theta does NOT restrict',
     'Eventhoughthescalingactionϑdoesnotrestricttothissubspace'),
    ('C1b Sonin space is INFINITE DIMENSIONAL -- CC\'s own words',
     'infinitedimensionalSoninsspace'),
    ('C1c the positivity is by construction, via a positive operator',
     'positivedefinitebyconstruction'),
    ('C1d the trace side differs from the distribution by a COMPACT operator',
     'byaninfinitesimalinthesenseofquantizedcalculus'),
    ('C1e Theorem 1 -- the inequality itself',
     'W8pg˚g˚qěTrpϑpgqSϑpgq˚q'),
    ('C1f the support condition on the test function',
     'haveSupportintheinterval'),
    ('C1g the support chosen so no prime is involved',
     'sothatrationalprimesarenotinvolved'),
    ('C1h the Schwartz kernel of a SINGLE scaling is a delta',
     'kpx,yq“δpλx´yq'),
    # --- Component 1/2: trace-class status, stated by CC ---
    ('C2a the single-scaling trace is given FORMALLY',
     'isformallygivenby'),
    ('C2b trace class holds only after smearing against a test function',
     'isoftraceclassanditstraceisgivenby'),
    ('C2c tau is NOT a function, because of the divergency at rho = 1',
     'isnotafunctionbecauseofthedivergency'),
    ('C2d the trace-remainder delta IS a function',
     'Thetraceremainderisthefunctionof'),
    ('C2e delta has a jump in its FIRST DERIVATIVE at rho = 1',
     'hasajumpinitsfirstderivative'),
    # --- Component 2: the local weight at a non-identity scaling ---
    ('C2f the Weil local term -- the fixed-point weight at rho != 1',
     '1`ρ`1'),
    ('C2g the distribution is defined as a principal value',
     'isthendefinedasaprincipalvalue'),
    ('C2h and it tends to infinity as the variable tends to 1',
     'tendsto`8asthevariabletendsto1'),
    # --- Component 1: where the content sits, and Component 3's characterization ---
    ('C1i Theorem 4.7 -- the trace side EQUALS the distribution plus a function',
     'TrpϑpfqSq“W8pfq`'),
    ('C1j Theorem 3.6 -- the form is minus two times the identity plus a compact',
     '2Id`KIqξy'),
    ('C3a Sonin space is the EIGENVALUE-ONE eigenspace of the projection sandwich',
     'istheeigenspaceofPpPPfortheeigenvalue1'),
    ('C3b the main result names the constant',
     'c“4γ'),
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


def main(argv):
    if not argv:
        print('usage: python b311_source.py <path-to-pdf>')
        return 2
    pdf = argv[0]
    print('=' * 100)
    print('b311_source.py -- THE SOURCE\'S PROOF. ### PINNED, THEN LOCATED.')
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
    print('  ### ### **THIS COPY WAS RE-ACQUIRED: the local one was not found on this machine.**')
    print('  ### **THE PIN IS WHAT MAKES THAT SAFE**, and it is checked above rather than assumed.')

    rows, npages = locate(pdf)
    print()
    print('  pages in file : %d' % npages)
    print()
    print('  ### THE QUOTED FRAGMENTS, LOCATED BY PAGE INDEX:')
    missing = []
    for label, frag, hits in rows:
        if not hits:
            missing.append(label)
        print('    %-12s %-62s %s'
              % (','.join(str(h) for h in hits) if hits else '### NONE',
                 label, frag[:44]))
    print()
    print('  ### FRAGMENTS NOT LOCATED : %d  %s'
          % (len(missing), 'PASS' if not missing else '### FAIL ###'))
    for m in missing:
        print('      ### %s' % m)
    print('  ### **THIS TOOL LOCATES; IT DOES NOT READ.** ### It cannot tell a correct quotation')
    print('  ### from an invented one. ### What it can do is fail loudly when a fragment the bank')
    print('  ### claims to quote is not in the artefact at all.')
    print('=' * 100)
    return 0 if not missing else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
