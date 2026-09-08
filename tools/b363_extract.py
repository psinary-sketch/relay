# -*- coding: utf-8 -*-
"""b363_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE POPULATION OF THIS ACT'S CENSUS IS A SET OF SENTENCES IN THREE BANKS**, and the order fixes
### that they be ### **ENUMERATED FROM THEIR BANKS BY THE ANCHOR TOOL.** ### This step is that enumeration's
### evidence: every arm the census counts is located here, at the bank whose own seat declared it, before
### the census classifies anything.
### ### **BAR 1: AN ARM THIS ACT CANNOT LOCATE IS REPORTED AS NOT LOCATED AND IS NOT COUNTED FROM MEMORY.**
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

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b363_ferry_2026-09-07.txt')
DRAFT = d('b362_closing.txt')
B360 = d('b360_the_fold.txt')
B361 = d('b361_the_held_item.txt')
B362 = d('b362_the_approximation_register.txt')
B358 = d('b358_the_li_asymptotics.txt')
SRC = d('b358_source_lagarias0404394.txt')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY, 'ACT b363 — THE ANCHORED GATE ARMS. The executor'),
    ('the order -- addition one, the count', 'ORDER', FERRY, "ADDITION ONE — THE EVIDENCE IS THE ACT"),
    ('the order -- addition two, the control', 'ORDER', FERRY,
     'ADDITION TWO — THE CONTROL IS THE BANKED SUITES, UNEDITED: the'),
    ('the order -- addition three, the owed read', 'ORDER', FERRY,
     'ADDITION THREE — THE OWED READ IS FILED, NOT RUN: a trail entry'),
    ('the order -- the fourth species, untouched by any needle tool', 'ORDER', FERRY,
     'tool, and the act says plainly that the helper does not reach'),
    ("the order -- the navigator's expectation", 'ORDER', FERRY,
     'fewer arms than the draft estimates, because at least one of'),
    ('the order -- the next draft, counted and not typed', 'ORDER', FERRY,
     "onward when the span reaches the fold"),

    # ---- THE DRAFT'S OWN ESTIMATE, WHICH IS WHAT THE COUNT SCORES ------------------------------------
    ("the draft -- its own population figure", 'DRAFT', DRAFT, 'NINE ARMS THAT FIRED ON THEIR OWN ACTS'),
    ("the draft -- its own retirement estimate", 'DRAFT', DRAFT,
     'census of thirteen incidents should convert to a cure covering nine or ten'),
    ('the draft -- the act it proposed', 'DRAFT', DRAFT, 'THE ANCHORED-ARM HELPER, BUILT.'),

    # ---- THE POPULATION: b360's FOUR ---------------------------------------------------------------
    ("b360 -- the headline figure for its own incident section", 'POP', B360, '(E7) FOUR ARMS OF THIS ACT'),
    ('b360 arm 1 -- a self-needle typed with a marker prefix the file does not carry', 'POP', B360,
     'RATHER THAN SOFTENED.** ### One self-needle was typed with a marker prefix the bank does not carry'),
    ('b360 arm 2 -- a plain substring against markup that carries emphasis inside the phrase', 'POP', B360,
     "RETIRE IT** -- and was re-typed against the file. ### One arm looked for the deposit"),
    ('b360 arm 3 -- G-ORDER demanded a component order the act never promised', 'POP', B360,
     'FIRST VERSION DEMANDED A COMPONENT ORDER THIS ACT NEVER PROMISED'),
    ("b360 arm 4 -- G-ROSTER searched raw text where the bank wraps through the phrase", 'POP', B360,
     'component order as measured rather than demanding one. ### And ### **`G-ROSTER`'),

    # ---- THE POPULATION: b361's TWO ----------------------------------------------------------------
    ("b361 -- the headline figure for its own incident section", 'POP', B361, '(E4) TWO ARMS OF THIS ACT'),
    ('b361 arm 5 -- G-SCOPE typed a noun the file does not use', 'POP', B361, 'FILE.** ### `G-SCOPE`'),
    ('b361 arm 6 -- G-NUMBERS asked for a number the bank had not printed', 'POP', B361,
     "and `G-NUMBERS` asked for the correspondence row"),

    # ---- THE POPULATION: b362's FIVE ---------------------------------------------------------------
    ("b362 -- the headline figure for its own incident section", 'POP', B362, '(E5) FIVE ARMS OF THIS ACT'),
    ('b362 arms 7 and 8 -- two inherited needles carrying the previous leg’s wording', 'POP', B362,
     'CORRECTED TO THE FILE RATHER THAN SOFTENED.** ### Two were inherited needles still carrying the'),
    ('b362 arm 9 -- a row number the bank had not printed', 'POP', B362, "previous leg"),
    ('b362 arm 10 -- THE WRONG ARM: a true-prefix test on a spliced row', 'POP', B362,
     'THE WRONG ARM ENTIRELY** -- a true-prefix test on a ledger whose new row is SPLICED INTO THE'),
    ('b362 arm 11 -- the needle-wrapping species, through an indented continuation', 'POP', B362,
     "THE NEEDLE-WRAPPING SPECIES, TWICE OVER**: the deposit"),

    # ---- THE TRAIL ENTRY'S TWO ACTS, EACH AT ITS OWN BANK -------------------------------------------
    ('the trail -- b358 grades the cuspidality hypothesis', 'TRAIL', B358,
     '`H-CUSP` (`π` cuspidal on `GL(N)`): the corpus'),
    ('the trail -- b361 inherits that grade and does not decide it', 'TRAIL', B361,
     '(i) IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT.'),
    ('the trail -- and says the decision would move with it', 'TRAIL', B361,
     'GRADE AND CONFERS NONE, AND IF `H-CUSP` EVER MOVED THIS DECISION WOULD MOVE WITH IT.'),
    ("the trail -- the theorem's own hypothesis, at the pinned source", 'TRAIL', SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    ("the trail -- and the source's own marking of the exception", 'TRAIL', SRC,
     '2 )ζ(s). This function has simple poles at s = 0 and s = 1.'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b363 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b363_extract_notes', LINES)
        return 2
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
        rec('  [%-5s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    npop = sum(1 for b in built if b['tag'] == 'POP')
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **POPULATION LINES LOCATED : %d** ### -- the headline figures and the arm descriptions'
        % npop)
    rec('  ### beneath them. ### **THE CENSUS COUNTS ARMS AND NOT LINES**, and the arithmetic from these')
    rec("  ### lines to that count is the census tool's and is printed there.")
    rec('=' * 100)
    p = run_clock.write(D, 'b363_extract_notes', LINES)
    io.open(d('b363_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, population_lines=npop,
             built=built, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
