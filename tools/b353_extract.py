# -*- coding: utf-8 -*-
"""b353_extract.py -- EXTRACT-TO-DISK, AND THE SEARCH RECORDED.

### ### **TWO JOBS.** ### (1) Every quotation this act uses, pulled at its emitting file and line through the
### sortie's shared normaliser. ### (2) ### **THE SEARCH ITSELF, RECORDED** -- what was queried, what was
### fetched, what was found and ### **WHAT WAS LOOKED FOR AND NOT FOUND** -- because the order's second branch
### demands the search be recorded, and honesty demands it be recorded in whichever branch is taken.
### ### **THE IMPORTED SOURCE IS PINNED BY HASH**, and the hash is of the file this seat actually read.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import quote_norm    # noqa: E402
import run_clock     # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


# ### THE IMPORTED SOURCE, PINNED. ### The file lives in this session's scratchpad and NOT in any repo,
# ### which is the record's own convention for hash-pinned sources; the hash is what survives.
SOURCE = dict(
    arxiv='2006.13771v1',
    title='Weil positivity and Trace formula, the archimedean place',
    authors='Alain Connes and Caterina Consani',
    submitted='24 June 2020',
    pdf_url='https://arxiv.org/pdf/2006.13771v1',
    html_read='https://ar5iv.labs.arxiv.org/html/2006.13771',
    sha256='b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726935b58e0',
    bytes=1213504,
    grade='TRUSTED-AT-CITE',
)

# ### WHAT WAS READ IN THE SOURCE, QUOTED. ### These are transcriptions from the rendered text of the pinned
# ### paper; the mathematical notation is flattened by the renderer and that is declared, not hidden.
SOURCE_QUOTES = [
    ('THEOREM 1 -- the source\'s main positivity statement, with EVERY hypothesis',
     'Let g in Cc^infty(R+*) have support in [2^-1/2, 2^1/2] and Fourier transform vanishing at i/2 and 0. '
     'Then W_infty(g * g^*) >= Tr(theta(g) S theta(g)^*).'),
    ('DEFINITION (section 3; the corpus calls it Definition 3.1)',
     'Let G be a locally compact abelian group and f in L^1(G, dg). We say f is positive definite when its '
     'Fourier transform is pointwise positive, i.e. f^(t) >= 0, for all t in G^.'),
    ('PROPOSITION 2 -- BOAS-KAC. ### THE STATEMENT OF THE SHAPE THE ORDER ASKS FOR',
     'Let f in Cc^infty(R) have support in the interval [-A, A] (A > 0). The following conditions are '
     'equivalent: 1. The Fourier transform f^ is pointwise positive. 2. There exists g in Cc^infty(R) with '
     'support in [-A/2, A/2] such that f = g * g^*.'),
    ('THE RH CRITERION, AND THE CLASS IT QUANTIFIES OVER',
     'RH <=> sum_v W_v(g * gbar^#) <= 0, for all g in Cc^infty(R+*) with g~(z) = 0 for all z in F.'),
    ('WHY THE SUPPORT IS RESTRICTED, IN THE SOURCE\'S OWN WORDS',
     'In this paper we consider the simplest instance of this strategy, namely when the support of the test '
     'function is contained in the interval (1/2, 2) subset R+*.'),
    ('THE VANISHING CONDITIONS AS AN IDEAL',
     'The vanishing conditions int f(rho) rho^(+-1/2) d*rho = 0 define an ideal J in the convolution algebra '
     'Cc^infty(R+*).'),
]

# ### WHAT WAS LOOKED FOR AND NOT FOUND. ### An absence of reading, reported as one.
SEARCH_MISSES = [
    ('the words "dense", "density", "approximation", "exhaust", "uniform in", applied to the test-function '
     'class, anywhere in the pinned source',
     'NOT FOUND in the rendered text of 2006.13771v1'),
    ('a statement carrying positivity from one support to a larger one, or to the union over all supports',
     'NOT LOCATED in the pinned source'),
    ('a statement bounding the Weil functional uniformly in the support parameter',
     'NOT LOCATED in the pinned source'),
]

SEARCHES = [
    ('web', 'Weil positivity functional dense subfamily test functions implies positivity whole class '
            'continuity argument'),
    ('web', 'Bombieri "Remarks on Weil\'s quadratic functional" positivity test function class support '
            'restriction density'),
    ('fetch', 'https://arxiv.org/abs/2006.13771  -- title, authors, abstract, version'),
    ('fetch', 'https://alainconnes.org/wp-content/uploads/Selecta.pdf  -- REFUSED, HTTP 403'),
    ('fetch', 'https://arxiv.org/pdf/2006.13771v1 -- downloaded and hashed; NO TEXT LAYER the reader could use'),
    ('fetch', 'https://ar5iv.labs.arxiv.org/html/2006.13771 -- read at content, twice, with targeted questions'),
    ('index', "banked_index: 'the Weil functional', 'positivity', 'the test function class', 'density', "
              "'the admissible class' -- NO KEY, all five; 'the import ledger', 'the seed's width', "
              "'the aim plane' -- HIT"),
]

READS = [
    # ---- THE ORDER --------------------------------------------------------------------------------
    ('the order -- a read under the import bar and a pricing', 'ORDER', d('b353_ferry_2026-09-07.txt'),
     'under the import bar and a PRICING; NO argument constructed, NO'),
    ('the order -- the width is the reach of the test-function class', 'ORDER', d('b353_ferry_2026-09-07.txt'),
     'unbounded with no method at all, and the width is the reach of'),
    ('the order -- what to read for', 'ORDER', d('b353_ferry_2026-09-07.txt'),
     'argument: does the literature carry a density or approximation'),
    ('the order -- located in a real source, pinned by hash', 'ORDER', d('b353_ferry_2026-09-07.txt'),
     'located in a real source, pinned by hash, quoted with its'),
    ('the order -- the coverage class filed beside it', 'ORDER', d('b353_ferry_2026-09-07.txt'),
     'File the phase coordinate\'s vanishing-transform class'),

    # ---- THE IMPORT BAR ---------------------------------------------------------------------------
    ('the import bar, the author\'s ruling verbatim', 'BAR', d('b233_registration_2026-08-28.txt'),
     '### "Imports are verified ourselves where we have the tools, not only trusted. The import ledger'),
    ('the import bar -- the three grades', 'BAR', d('b233_registration_2026-08-28.txt'),
     '### gains a verification column -- VERIFIED-INTERNALLY / VERIFIED-AT-BENCH / TRUSTED-AT-CITE --'),

    # ---- WHAT b351 LEFT ---------------------------------------------------------------------------
    ('b351 -- the width is NOT BOUNDED and has no method', 'b351', d('b351_the_partition_question.txt'),
     '### ### **AND THIS COORDINATE IS WORSE OFF THAN THE HEIGHT, WHICH IS WORTH SAYING PLAINLY BECAUSE THE'),
    ('b351 -- the partition stays UNDECIDED', 'b351', d('b351_the_partition_question.txt'),
     '### ### ### **UNDECIDED.**'),
    ('b351 -- the phase class the algebra cannot see', 'b351', d('b351_the_partition_question.txt'),
     "### ### **AND EXACTLY ONE CLASS SURVIVES THE ALGEBRA: `|G| = 0`.**"),

    # ---- THE COVERAGE CLASS, IN b349's OWN WORDS ---------------------------------------------------
    ('b349 -- three lawful seeds mean these three did not', 'b349', d('b349_the_room_relative.txt'),
     '### ### NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT.**'),
    ('b349 -- all three lawful, in the window, none degenerate', 'b349', d('b349_the_room_relative.txt'),
     '### ### DEGENERATE.** ### The window is'),

    # ---- THE CORPUS'S OWN CLASS, AND WHAT IT MEASURED ----------------------------------------------
    ("the corpus's Definition 3.1 test, and ITS OWN STATED REACH", 'CLASS', t('b318_square.py'),
     '### The scan runs in units of the cell\'s own width `L = log a`, so a narrow cell is scanned as'),
    ('the corpus -- a scan cannot prove positivity beyond its interval', 'CLASS', t('b318_square.py'),
     '### show a function is NOT positive definite by exhibiting a negative value, and it cannot prove'),
    ('the corpus -- the square is in the source\'s class at every cell', 'CLASS', d('b320_the_lawful_function.txt'),
     '### formed with the source\'s own involution, tested by the source\'s own Definition 3.1 -- *positive'),
    ("the corpus -- Theorem 1's three conditions, per cell", 'CLASS', d('b320_the_lawful_function.txt'),
     "### ### **(1c) THEOREM 1's THREE CONDITIONS, PER CELL.**"),
    ('the corpus -- the covered cells named from the check', 'CLASS', d('b320_the_lawful_function.txt'),
     '### ### **(2) THE COVERED CELLS ARE NAMED FROM THE CHECK AND NOT FROM THE WISH: ### 1.3, 1.35,'),
    ('the corpus -- the test functions ARE PIECEWISE LINEAR', 'CLASS', t('b326_closure.py'),
     '### `f = autocorrelation(seed)` is piecewise linear on b318\'s uniform grid, and its transform has'),
    ('the corpus -- each bump is piecewise linear on its own nodes', 'CLASS', t('b317_smear.py'),
     '### ### **THE UNION GRID IS NOT A CONVENIENCE EITHER.** ### Each bump is piecewise linear on its'),
    ('the corpus -- the reaching widths, far outside the source\'s support', 'CLASS', t('b334_aimmap.py'),
     'REACHING = (40.0, 81.0)'),

    # ---- THE STANDING RULES ------------------------------------------------------------------------
    ('b322 -- a price is not a prediction', 'RULE', d('b322_the_membership.txt'),
     '### it does. ### **A PRICE IS NOT A PREDICTION.**'),
    ('b350 -- pricing is not measuring', 'RULE', d('b350_the_two_held_axes.txt'),
     '### **PRICING IS NOT MEASURING, AND NOTHING PRICED HERE'),
    ('b352 -- a fit is a description and not a fact', 'RULE', d('b352_the_fourth_candidate.txt'),
     '### ### **A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING.**'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b353 -- EXTRACT-TO-DISK, THE SEARCH RECORDED, AND THE SOURCE PINNED.')
    rec('=' * 100)

    rec('')
    rec('  ### ### **THE IMPORTED SOURCE, PINNED BY HASH.**')
    for k in ('arxiv', 'title', 'authors', 'submitted', 'pdf_url', 'html_read', 'bytes', 'sha256', 'grade'):
        rec('    %-11s : %s' % (k, SOURCE[k]))
    rec('    ### ### **THE HASH IS OF THE FILE THIS SEAT DOWNLOADED AND HELD**, in this session\'s')
    rec('    ### ### scratchpad and in no repository -- which is the record\'s own convention for a')
    rec('    ### ### hash-pinned source. ### **THE HASH IS WHAT SURVIVES THE SESSION; THE FILE DOES NOT.**')
    rec('    ### ### **AND THE READING WAS DONE ON THE RENDERED HTML, NOT THE PDF**, because the PDF this')
    rec('    ### ### seat downloaded carries no text layer the reader could use. ### The rendered text')
    rec('    ### ### FLATTENS THE MATHEMATICAL NOTATION, and every quotation below is transcribed from it')
    rec('    ### ### with the notation written in plain characters. ### **THAT IS A TRANSCRIPTION AND NOT A')
    rec('    ### ### FACSIMILE, AND IT IS DECLARED RATHER THAN HIDDEN.**')

    rec('')
    rec('  ### ### **THE SEARCH, RECORDED. ### EVERY QUERY AND EVERY FETCH, INCLUDING THE ONE REFUSED.**')
    for kind, what in SEARCHES:
        rec('    [%-5s] %s' % (kind, what))

    rec('')
    rec('  ### ### **WHAT WAS LOOKED FOR AND NOT FOUND.** ### **THIS IS AN ABSENCE OF READING, NOT AN')
    rec('  ### ### ABSENCE OF LITERATURE**, and the record has four incidents to say why that distinction')
    rec('  ### ### is not a formality.')
    for what, res in SEARCH_MISSES:
        rec('    - %s' % what)
        rec('      -> %s' % res)

    rec('')
    rec('  ### ### **THE SOURCE, QUOTED.**')
    for lbl, q in SOURCE_QUOTES:
        rec('')
        rec('    [%s]' % lbl)
        for i in range(0, len(q), 96):
            rec('      | %s' % q[i:i + 96])

    rec('')
    rec('-' * 100)
    rec('  ### THE READS, EACH AT ITS EMITTING FILE AND LINE.')
    rec('-' * 100)
    bad = 0
    for label, tag, path, anchor in READS:
        try:
            needle_pull.pull(path, anchor)
        except LookupError:
            bad += 1
            rec('  ### ### **UNPULLABLE** : %s' % label)
            rec('      file   : %s' % os.path.relpath(path, ROOT))
            rec('      anchor : %r' % anchor)
            continue
        txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
        num = None
        for i, ln in enumerate(txt, 1):
            if quote_norm.contains(ln, anchor):
                num = i
                break
        rec('')
        rec('  [%-5s] %s' % (tag, label))
        rec('      %s : line %s' % (os.path.relpath(path, ROOT).replace(os.sep, '/'), num))
        rec('      | %s' % txt[num - 1].rstrip())
        if num < len(txt) and txt[num].strip():
            rec('      | %s' % txt[num].rstrip())
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### UNPULLABLE : %d' % (len(READS), bad))
    rec('  ### ### **AN EXTRACT IS A QUOTATION AT A LINE. ### IT IS NOT A READING OF THE ARGUMENT AROUND IT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b353_extract_notes', LINES)
    io.open(d('b353_source.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(source=SOURCE, quotes=SOURCE_QUOTES, misses=SEARCH_MISSES, searches=SEARCHES,
             reads=len(READS), unpullable=bad,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
