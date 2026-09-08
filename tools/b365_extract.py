# -*- coding: utf-8 -*-
"""b365_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **BAR 1 OF THE LOCKED REGISTRATION:** ### every statement attributed to the source is pulled from
### the pinned rendering by the anchor tool WITH ITS LINE, and appears here before it appears in an
### argument. ### **ITS FLOOR: IT FIXES WHAT THE RENDERING SAYS. ### IT DOES NOT CERTIFY THAT THE
### ### RENDERING IS FAITHFUL TO THE PDF**, which is the seam `b327` named and `b358` restated.
### ### **NO SOURCE IS FETCHED HERE.** ### The pinned text on disk is the only text read, and the cap says
### so.
"""
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
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b365_ferry_2026-09-07.txt')
SRC = d('b358_source_lagarias0404394.txt')
B358 = d('b358_the_li_asymptotics.txt')
B361 = d('b361_the_held_item.txt')
B363 = d('b363_the_anchored_gate_arms.txt')
B364 = d('b364_the_copy_that_did_not_reproduce.txt')
B360 = d('b360_the_fold.txt')
B362 = d('b362_the_approximation_register.txt')
B363C = d('b363_closing.txt')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the leg', 'ORDER', FERRY, 'LEG 2 (b365) - THE OWED READ, PAID. The executor'),
    ('the order -- addition one, the question', 'ORDER', FERRY,
     'ADDITION ONE - THE QUESTION, stated before the search: the'),
    ('the order -- read the source at content for the exceptional case', 'ORDER', FERRY,
     'not meet - the last at full prominence, since two acts stand on'),
    ('the order -- the circularity finding untouched', 'ORDER', FERRY,
     'it. The circularity finding is untouched in every branch.'),
    ('the order -- addition two, the mint', 'ORDER', FERRY,
     'ADDITION TWO - THE MINT AND THE THRESHOLD. The wrong-arm'),
    ('the order -- no mechanizable half, and why', 'ORDER', FERRY,
     'construction, because the needle checks the sentence and the'),
    ('the order -- the module, local-only, with A3 and A10', 'ORDER', FERRY,
     'locally, not pushed, with A3 and A10 as its incidents. And the'),
    ('the order -- the threshold, ruled and not by this seat', 'ORDER', FERRY,
     'and record that until it is ruled, "the fold is due" is a'),
    ("the order -- the navigator's expectation", 'ORDER', FERRY,
     'meet, and the honest grade is IMPORTED-ON-A-HYPOTHESIS-NOT-MET'),

    # ---- (i) THE CONVENTION, AT THE PINNED SOURCE ---------------------------------------------------
    ("the source -- zeta is the paper's own marked exception", 'CONV', SRC,
     'representation, all other'),
    ('the source -- the convention itself, named as a convention', 'CONV', SRC,
     'GL(1) we have e(0,π'),
    ('the source -- and why the convention is forced', 'CONV', SRC,
     'if we wish to have entire functions in all cases, for we must re move the poles at s = 0 and'),
    ('the source -- and the consequence it draws, IN ALL CASES', 'CONV', SRC,
     'whose singularities are simple poles at s = 0, 1. It follows that'),

    # ---- THE SOURCE CARRYING pi_triv THROUGH ITS OWN CUSPIDAL-HYPOTHESIS RESULTS --------------------
    ('the source -- the final term is 1 for the trivial representation', 'CARRY', SRC,
     'The ﬁnal term δ(π) = δ(π∨) = 1 for the trivial representation'),
    ("the source -- Lemma 4.2's hypothesis says cuspidal", 'CARRY', SRC,
     'Lemma 4.2. Letπ be an irreducible cuspidal automorphic representation on'),
    ("the source -- and Lemma 4.2's own conclusion carries the exception", 'CARRY', SRC,
     'and δ(π) = 1 if π =πtriv and δ(π) = 0 otherwise.'),
    ("the source -- Lemma 4.3's hypothesis says cuspidal", 'CARRY', SRC,
     'Lemma 4.3. For an irreducible cuspidal automorphic representation'),
    ('the source -- and its Remark applies it to the trivial representation', 'CARRY', SRC,
     'Remark. For the case πtriv on GL(1) Lemma 4.3 yields'),

    # ---- (ii) THE CONSTANT AND THE ERROR TERM ------------------------------------------------------
    ("the source -- Theorem 5.1's own hypothesis", 'CONST', SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    # ### **THE HINT `(γ − 1 − log(2π)) + 1` MATCHED TWICE** -- the constant is printed identically at
    # ### (1.13) and at (5.2), and the anchor tool REFUSED rather than choosing. ### The equation label
    # ### is what makes it unique, so the hint carries it.
    ('the source -- the constant of (5.1), at its own equation number', 'CONST', SRC,
     '2 logQ(π), (5.2)'),
    ('the source -- the index condition and the absolute implied constant', 'CONST', SRC,
     'and the implied constant in the O-notation is absolute.'),
    ('the source -- and it EVALUATES that constant FOR the exception, by name', 'CONST', SRC,
     'C1(πtriv ) = 1'),
    ('the source -- with the conductor it uses to do so', 'CONST', SRC, 'using Q(πtriv) = 1.'),
    ('the source -- the introduction, for all n at least 1, with a pi-dependent O(1)', 'CONST', SRC,
     '2n logn +C1(π) n +O (1), (1.12)'),
    ("the source -- what the theorem's proof reduces the archimedean sum to", 'CONST', SRC,
     'using (4.24). We proceed to estimate an individual sum'),

    # ---- THE TWO ACTS THAT STAND ON IT --------------------------------------------------------------
    ('b358 -- the grade it gave the cuspidality hypothesis', 'ACTS', B358,
     '`H-CUSP` (`π` cuspidal on `GL(N)`): the corpus'),
    ('b361 -- it inherits that grade and does not decide it', 'ACTS', B361,
     '(i) IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT.'),
    ('b361 -- and its decision would move with it', 'ACTS', B361,
     'GRADE AND CONFERS NONE, AND IF `H-CUSP` EVER MOVED THIS DECISION WOULD MOVE WITH IT.'),
    ('the trail entry b363 filed and priced', 'ACTS', TRAILS,
     'W-ORD-LI-CUSP` — OPENED 2026-09-07 (b363)'),

    # ---- ADDITION TWO: THE MINT'S TWO NAMED INCIDENTS, AT THEIR OWN BANKS ---------------------------
    ('A3 -- G-ORDER demanded an order the act never promised', 'MINT', B360,
     'FIRST VERSION DEMANDED A COMPONENT ORDER THIS ACT NEVER PROMISED'),
    ('A10 -- a true-prefix test on a spliced ledger row', 'MINT', B362,
     'THE WRONG ARM ENTIRELY** -- a true-prefix test on a ledger whose new row is SPLICED INTO THE'),
    # ### **THIS SEAT BELIEVED THE SENTENCE WAS BANKED AT `b362`. ### IT IS BANKED AT `b360`**, and the
    # ### anchor tool refused at the wrong file rather than finding something close at the right one.
    ('the sentence the rule is built on, at the bank that actually holds it', 'MINT', B360,
     'AN ARM THAT CANNOT PASS ON A CORRECT EDIT IS NOT A STRICTER ARM; IT IS THE WRONG ARM.** ### It was'),
    ('b363 -- no needle tool reaches it', 'MINT', B363,
     'THE WRONG QUESTION**, and this act says that plainly'),
    ("b364 -- two more, live, in this sortie's own suite", 'MINT', B364,
     'TWO OF THEM WERE THE WRONG ARM -- IN THE ACT THAT NAMED THE OTHER SPECIES'),

    # ---- ADDITION TWO: THE THRESHOLD ---------------------------------------------------------------
    ('b363 -- no threshold is declared anywhere in the record', 'THRESH', B363C,
     'THERE IS NO DECLARED THRESHOLD ANYWHERE IN THE RECORD, AND THE TOOL SAYS SO RATHER THAN'),
    ('b363 -- the observed spans, shortest longest and middle', 'THRESH', B363C,
     'span read from its own heading in `FINDINGS.md`:'),
    ('b363 -- the record has a habit and not a law', 'THRESH', B363C,
     'THE RECORD HAS A HABIT AND NOT A LAW'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b365 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b365_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('  ### ### **AND NO SOURCE IS FETCHED. ### THE PINNED TEXT ON DISK IS THE ONLY TEXT READ.**')
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
        rec('  [%-6s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    nsrc = sum(1 for b in built if b['tag'] in ('CONV', 'CARRY', 'CONST'))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **SOURCE LINES LOCATED AT THE PINNED RENDERING : %d** ### -- every statement this act'
        % nsrc)
    rec('  ### attributes to the source is one of these, and none is retyped.')
    rec('  ### **AND THE SEAM STANDS: A HASH ON A PDF DOES NOT CERTIFY THAT ITS EXTRACTED TEXT IS A')
    rec('  ### FAITHFUL RENDERING OF IT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b365_extract_notes', LINES)
    io.open(d('b365_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, source_lines=nsrc,
             built=built, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
