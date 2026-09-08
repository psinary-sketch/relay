# -*- coding: utf-8 -*-
"""b362_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE HINT THE ORDER CARRIES IS A HINT.** ### It arrives from recall and not from a file, and the
### locked registration fixes that ### **A HINT IS SOMETHING TO SEARCH ON AND NEVER SOMETHING TO CITE.**
### ### This step is where that rule becomes checkable: every statement the act reports is located at a
### PINNED source and read from it, and the hint's own words are located at the banked ferry so a reader
### can see what was searched on.
### ### **BAR 1: A SENTENCE THIS ACT CANNOT LOCATE IS NOT QUOTED.**
### ### **BAR 3: A STATEMENT IS QUOTED WITH ITS HYPOTHESES UNFOLDED**, which is why the setup lines --
### the space, the function, the family, the parameter range -- are located one by one and not summarised.
"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b361_ferry_2026-09-07.txt')
S1 = d('b362_source_baezduarte0202141.txt')
S2 = d('b362_source_baezduarte_abs0202141.txt')
S3 = d('b362_source_burnol0103058.txt')
S5 = d('b362_source_baezduarte0205003.txt')
B321 = d('b321_the_window_opened.txt')
REG358 = d('b358_registration_2026-09-07.txt')

READS = [
    # ---- THE ORDER, AND THE HINT IN ITS OWN WORDS ---------------------------------------------------
    ('the order -- leg 2', 'ORDER', FERRY, 'LEG 2 (b362) \u2014 THE APPROXIMATION REGISTER, READ UNDER A CAP.'),
    ('the order -- the CAP', 'ORDER', FERRY, 'CAP, quoted in the registration: ONE act; reads and a pricing'),
    ('the order -- (i), and the hint\u2019s provenance', 'ORDER', FERRY,
     '(i) THE STATEMENT, located and pinned: the navigator asserts,'),
    ('the order -- the hint is recall and NOT a file', 'ORDER', FERRY,
     'from recall and NOT from any file, that the hypothesis has a'),
    ('the order -- the hint, in its own words', 'ORDER', FERRY,
     'Nyman\u2013Beurling criterion, that a fixed function lies in the'),
    ('the order -- and the variant it names', 'ORDER', FERRY,
     'sequence of distances tends to zero \u2014 with a variant due to'),
    ('the order -- (ii), the structural question', 'ORDER', FERRY,
     '(ii) THE STRUCTURAL QUESTION, decided from the quoted'),
    ('the order -- the shortfall comparison it demands', 'ORDER', FERRY,
     'the shortfall the window act found in the positivity register,'),
    ('the order -- (iii), the obstruction', 'ORDER', FERRY,
     '(iii) THE OBSTRUCTION, named in this register\u2019s own terms: what'),
    ('the order -- (iv), the pricing', 'ORDER', FERRY,
     '(iv) THE PRICING, in acts and in what would have to be built,'),
    ('the order -- the floor-versus-edge question', 'ORDER', FERRY,
     'two fresh incidents of exactly this \u2014 how a floor would be told'),
    ('the order -- (v), the verdict set', 'ORDER', FERRY,
     '(v) THE VERDICT: (A REGISTER WORTH OPENING \u2014 with what the'),

    # ---- (i) THE STATEMENT, AT ITS PINNED SOURCE, WITH ITS HYPOTHESES UNFOLDED ----------------------
    ('S3 -- the classical criterion, stated as a theorem', 'STATEMENT', S3,
     'Theorem 1.1 (Nyman [14], Beurling [3]) The Riemann Hypothesis holds if and only if'),
    ('S3 -- the setting it is stated in', 'STATEMENT', S3,
     'The context in which our construction takes place is that of t he Nyman-Beurling formulation'),
    ('S3 -- the family, and its parameter range', 'STATEMENT', S3,
     'of K consisting of the \ufb01nite linear combinations of the function s t'),
    ('S1 -- the same criterion at the other source, with its own caveat', 'STATEMENT', S1,
     'Nyman-Beurling criterion ([13], [6]) states, in a slig htly'),
    ('S1 -- AND THE CAVEAT ITSELF: the ORIGINAL formulation is a different space', 'STATEMENT', S1,
     'modi\ufb01ed form [4] (the original formulation is related to L2(0, 1)), that the'),
    ('S1 -- the fractional part and the characteristic function', 'STATEMENT', S1,
     'We denote the fractional part of x by \u03c1(x) = x \u2212 [x], and let \u03c7 stand'),
    ('S1 -- the space', 'STATEMENT', S1,
     'where the main object of interest is the subspace of Beurling functions ,'),
    ('S1 -- the family, as a linear hull over a REAL parameter', 'STATEMENT', S1,
     'de\ufb01ned as the linear hull of the family {\u03c1a|1 \u2264 a \u2208 R} with'),
    ('S1 -- the strengthening: the family restricted to the naturals', 'STATEMENT', S1,
     'The much smaller subspace Bnat of natural Beurling functions is generated'),
    ('S1 -- and the theorem that is the variant the hint names', 'STATEMENT', S1,
     'Theorem 1.1. The Riemann hypothesis is equivalent to the statement that'),
    ('S2 -- the same statement on a second, independent surface', 'STATEMENT', S2,
     'By the Nyman-Beurling criterion the Riemann hypothesis is equivalent to the statement'),

    # ---- (ii) THE STRUCTURAL QUESTION: WHAT A FINITE INSTANCE IS -------------------------------------
    ('S3 -- the distance itself, defined as an infimum over the family', 'STRUCTURE', S3,
     'the Hilbert-space distance inff \u2208B \u03bb \u2016\u03c7 \u2212f \u2016. We have'),

    # ---- (iii) THE RATE: THE UNCONDITIONAL SIDE ------------------------------------------------------
    ('S3 -- the lower bound, attributed to its four authors', 'RATE', S3,
     'Theorem 1.2 (B\u00b4 aez-Duarte, Balazard, Landreau and Saias [2]) Let us write D(\u03bb) for'),
    ('S3 -- and what happens to it if the hypothesis FAILS', 'RATE', S3,
     'If the Riemann Hypothesis fails this result is true but trivi al as the left-hand side then take'),
    ('S3 -- so the proof assumes it, and the sum is over ALL non-trivial zeros', 'RATE', S3,
     'value +\u221e. So we will assume that the Riemann Hypothesis holds. The sum on the right-hand'),
    ('S3 -- the improvement, counting multiplicities', 'RATE', S3, 'Theorem 1.3 We have:'),

    # ---- (iii) THE RATE: THE CONDITIONAL SIDE, MARKED AS SUCH ---------------------------------------
    ('S5 -- the upper bound, and the hypothesis it is under', 'RATE', S5,
     'second version di\ufb00ers from the \ufb01rst in showing that under the Riemann'),
    ('S5 -- the approximant it is achieved by', 'RATE', S5,
     'hypothesis the distance between \u03c7 and \u2212'),
    ('S5 -- and its order', 'RATE', S5, 'order (log log n)\u2212'),

    # ---- (iv) THE PRICING: WHAT A CONTROL WOULD HAVE TO REPRODUCE ------------------------------------
    ('S3 -- the numerical explorations, NAMED at a reference this act did not fetch', 'PRICE', S3,
     '5.5 to give the exact order of decrease of the quantity D(\u03bb) and the numerical explorations'),
    ('S3 -- and who reported them', 'PRICE', S3,
     'reported by B\u00b4 aez-Duarte, Balazard, Landreau and Saias in [ 2] seem to support this.'),

    # ---- THE SHORTFALL THE WINDOW ACT FOUND, AT ITS OWN ACT ------------------------------------------
    ('b321 -- the shortfall, in the window act\u2019s own words', 'WINDOW', B321,
     '\u0023\u0023\u0023 \u0023\u0023\u0023 OWN DISTANCE FROM THE ANSWER**, and reporting this control as having settled the exponent'),

    # ---- THE CIRCULARITY CHECK, CARRIED FROM b358'S OWN LOCKED FACE ---------------------------------
    ('b358 -- circularity question (i)', 'CIRCULAR', REG358,
     "**(i)** Does the statement's own hypothesis list contain the hypothesis under study, by name?"),
    ('b358 -- circularity question (iii), the one that matters', 'CIRCULAR', REG358,
     '**(iii)** Does the ERROR TERM -- as opposed to the main term -- depend on it, even where the main'),

    # ---- THE DEPOSIT'S REFUSAL, AT THE DEPOSITED FILE ------------------------------------------------
    ("the deposit's refusal, read at the deposited monograph itself", 'REFUSAL', DEP,
     'while deliberately **not** compiling the cross-register equivalences, since to compile'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b362 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b362_extract_notes', LINES)
        return 2
    rec('')
    rec('  ### ### **THE PINS ON THE RENDERINGS THIS ACT ACTUALLY READS.** ### The fetch pinned the bytes')
    rec('  ### that came back; these are the extracted texts the quotations come from, and')
    rec('  ### **A HASH ON A PDF DOES NOT CERTIFY THAT ITS EXTRACTED TEXT IS A FAITHFUL RENDERING OF IT**')
    rec("  ### -- b353's seam, restated rather than assumed away.")
    pins = {}
    for lbl, p in (('S1', S1), ('S2', S2), ('S3', S3), ('S5', S5)):
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        pins[lbl] = dict(file=os.path.basename(p), sha256=h, bytes=os.path.getsize(p))
        rec('      %-4s %-42s sha256 %s  %d bytes' % (lbl, os.path.basename(p), h[:32] + '...',
                                                      os.path.getsize(p)))
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % str(e).replace(chr(10), ' | ')[:180])
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n, differs=bool(differs)))
        rec('')
        rec('  [%-9s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('=' * 100)
    p = run_clock.write(D, 'b362_extract_notes', LINES)
    io.open(d('b362_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built, pins=pins,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
