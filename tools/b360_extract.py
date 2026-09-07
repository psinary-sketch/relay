# -*- coding: utf-8 -*-
"""b360_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THIS ACT IS A FOLD, AND A FOLD IS NOTHING BUT QUOTATION.** ### Its whole content is eleven acts'
### own sentences carried into one section, so ### **THE EXTRACT IS THE ACT'S EVIDENCE AND NOT A RITUAL**:
### a sentence this step cannot locate never reaches `FINDINGS.md`, and `F-QUOTE` re-checks every one of
### them at the act that ORIGINATED it before the emitter writes a byte.
### ### **BAR 2: A SENTENCE THIS ACT CANNOT LOCATE IS NOT QUOTED.**
### ### **AND THE EMITTER DISCIPLINE (b283) IS ENFORCED BY THE PATHS BELOW:** ### every span quotation is
### read at the act's own bank, never at an act that quoted it -- which is why the three rhyming
### obstructions are read at `b332`, `b351` and `b353` and not at the faces ledger row that collects them.
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
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b360_ferry_2026-09-07.txt')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- b360, the fold of b349 through b359', 'ORDER', FERRY,
     'ACT b360 \u2014 THE FOLD, b349 through b359. The executor'),
    ('the order -- the ruling: FACES_LEDGER.md added to the mirror roster', 'ORDER', FERRY,
     'FACES_LEDGER.md is ADDED to the mirror roster. It is a'),
    ('the order -- addition one, the three that rhyme', 'ORDER', FERRY,
     'ADDITION ONE \u2014 THE THREE THAT RHYME, as the draft names its'),
    ('the order -- addition two, the arc as one statement', 'ORDER', FERRY,
     'ADDITION TWO \u2014 THE ARC AS ONE STATEMENT, at the grade the acts'),
    ('the order -- addition three, the desk', 'ORDER', FERRY,
     'ADDITION THREE \u2014 THE DESK, one list, written so a reader who'),
    ("the order -- the span's own finding, filed as a sentence and opening nothing", 'ORDER', FERRY,
     'own finding: no move aimed at the quantifier remains on the'),
    ('the order -- the closing', 'ORDER', FERRY,
     'CLOSING: correspondence rows; keys; both censuses; the faces'),

    # ---- THE SPAN: ELEVEN ACTS, EACH AT ITS OWN BANK -------------------------------------------------
    ('b349 -- the verdict', 'SPAN', d('b349_the_room_relative.txt'),
     'THE MINIMUM SURVIVES THE RELATIVE MEASURE, AT BOTH REACHING WIDTHS.'),
    ('b349 -- its own scope', 'SPAN', d('b349_the_room_relative.txt'),
     'it is one measure agreeing with another, which is'),
    ('b350 -- the verdict', 'SPAN', d('b350_the_two_held_axes.txt'),
     'The one origin that was moved does not account for it, and for the two held origins'),
    ('b350 -- the trail restated, not discharged', 'SPAN', d('b350_the_two_held_axes.txt'),
     'SO THE TRAIL IS RESTATED, NOT DISCHARGED'),
    ('b351 -- the verdict', 'SPAN', d('b351_the_partition_question.txt'),
     'THE FOUR COORDINATES DO NOT FAIL IN THE SAME WAY, AND THAT IS THE ACT'),
    ('b351 -- what UNDECIDED is', 'SPAN', d('b351_the_partition_question.txt'),
     'AND WHAT `UNDECIDED` IS: A STATEMENT ABOUT THE RECORD, NOT ABOUT THE OBJECT.'),
    ('b351 -- the abscissa already closed since b326', 'SPAN', d('b351_the_partition_question.txt'),
     'THE ABSCISSA WAS ALREADY CLOSED, AND HAS BEEN SINCE b326.'),
    ('b352 -- the verdict', 'SPAN', d('b352_the_fourth_candidate.txt'),
     'THE FLOOR IS UNDER-RESOLVED AS A FIT.'),
    ('b352 -- the instrument resolves and the cells do not agree', 'SPAN', d('b352_the_fourth_candidate.txt'),
     'THE INSTRUMENT HAS RESOLVING POWER. ### THE CELLS DO NOT AGREE.'),
    ('b352 -- the sixth frame affordable under a sealed ceiling', 'SPAN', d('b352_the_fourth_candidate.txt'),
     'THE SIXTH FRAME IS AFFORDABLE, AND IT IS AFFORDABLE UNDER A CEILING ALREADY SEALED.'),
    ('b353 -- the verdict', 'SPAN', d('b353_the_missing_statement.txt'),
     'A STATEMENT EXISTS -- AND IT DOES NOT CLOSE THE WIDTH COORDINATE, AND CANNOT.'),
    ('b354 -- the verdict', 'SPAN', d('b354_the_sixth_frame.txt'),
     'THE SIXTH RUNG LANDED, AND ITS RESIDUAL IS NEGATIVE AT EVERY COVERED CELL.'),
    ('b354 -- the act cannot separate the two', 'SPAN', d('b354_the_sixth_frame.txt'),
     'NOTHING IN THIS'),
    ('b354 -- the grade by the letter of the sealed condition', 'SPAN', d('b354_the_sixth_frame.txt'),
     'THEREFORE, BY THE LETTER OF THE SEALED CONDITION: FLOOR UNDER-RESOLVED STILL'),
    ('b355 -- the verdict', 'SPAN', d('b355_what_the_arrays_are.txt'),
     'THE RECORD STATES IT, AND `b353` DID NOT LOOK AT THE LINE.'),
    ('b355 -- the shape to carry', 'SPAN', d('b355_what_the_arrays_are.txt'),
     'A TEST APPLIED TO AN OBJECT BUILT TO PASS IT MEASURES THE'),
    ('b356 -- the verdict', 'SPAN', d('b356_the_boundary.txt'),
     "SO b354's SIXTH RUNG WAS THE INSTRUMENT'S EDGE, AND THE FIVE-FRAME PICTURE STANDS WITH ITS"),
    ('b356 -- six dimensions decided the sign', 'SPAN', d('b356_the_boundary.txt'),
     'SIX DIMENSIONS DECIDED THE SIGN.'),
    ('b356 -- the floor question is exactly where b352 left it', 'SPAN', d('b356_the_boundary.txt'),
     'THE FLOOR QUESTION IS EXACTLY WHERE b352 LEFT IT'),
    ('b357 -- the verdict', 'SPAN', d('b357_what_the_ledgers_say.txt'),
     '### ### ### **SOME ROWS SAY IT.**'),
    ('b357 -- the consequence, stated once', 'SPAN', d('b357_what_the_ledgers_say.txt'),
     'CLASS MEMBERSHIP IN THIS FAMILY RESTS ON THE CONSTRUCTION, AND THE SCAN CONFIRMS IT RATHER'),
    ('b358 -- the verdict', 'SPAN', d('b358_the_li_asymptotics.txt'),
     '### ### ### **EXISTS BUT CIRCULAR.**'),
    ('b359 -- the verdict', 'SPAN', d('b359_the_currency_pass.txt'),
     '### ### ### **NO DRIFT IS FOUND.**'),
    ('b359 -- why nothing was appended', 'SPAN', d('b359_the_currency_pass.txt'),
     'A currency pass that finds no drift and writes a note anyway would be'),

    # ---- ADDITION ONE: THE THREE THAT RHYME, EACH AT ITS OWN ACT -------------------------------------
    ('(i) the quantifier -- b332, first half', 'RHYME', d('b332_the_clause_stated.txt'),
     'a named owner; the quantifiers -- over the class, infinite, and through the explicit formula over'),
    ('(i) the quantifier -- b332, second half', 'RHYME', d('b332_the_clause_stated.txt'),
     'the zeros -- are UNOWNED, and they are the clause.'),
    ('(ii) the height -- b351, instances against a class', 'RHYME', d('b351_the_partition_question.txt'),
     'HIGHER BUYS MORE INSTANCES, AND A CLASS IS NOT MADE OF INSTANCES.'),
    ('(ii) the height -- b351, the sealed sentence', 'RHYME', d('b351_the_partition_question.txt'),
     'this before the coordinate was read: ### *A METHOD THAT PRODUCES INSTANCES DOES NOT PRODUCE A'),
    ('(iii) the width -- b353, the union', 'RHYME', d('b353_the_missing_statement.txt'),
     'ONE.** ### And the criterion it serves quantifies over the union of all supports'),
    ('(iii) the width -- b353, exhaustion at every width', 'RHYME', d('b353_the_missing_statement.txt'),
     'SO: AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.'),
    ('(iv) the countable face -- b358, the archimedean half unconditional', 'RHYME',
     d('b358_the_li_asymptotics.txt'),
     'THE ARCHIMEDEAN HALF IS UNCONDITIONAL, AND BOTH SOURCES SAY SO INDEPENDENTLY:'),
    ('(iv) the countable face -- b358, the zero half with no unconditional bound', 'RHYME',
     d('b358_the_li_asymptotics.txt'),
     'THE ZERO HALF HAS NO UNCONDITIONAL BOUND AT ALL, AND BOTH SOURCES SAY THAT TOO:'),
    ("THE DEPOSIT'S REFUSAL -- read at the deposited monograph itself", 'RHYME', DEP,
     'while deliberately **not** compiling the cross-register equivalences, since to compile'),
    ("U1's own shape sentence", 'RHYME', FACES,
     'THE SHAPE, NAMED AND NOT PROVED: in each, what the record holds is a family indexed by'),
    ("U1's own refusal, in the row's last words", 'RHYME', FACES,
     'Three separate obstructions that rhyme are three obstructions.'),

    # ---- ADDITION THREE: THE DESK -------------------------------------------------------------------
    ('the desk -- the instrument lane PARKED (b358, ruling R4)', 'DESK', d('b358_the_li_asymptotics.txt'),
     'THE INSTRUMENT LANE IS PARKED.'),
    ('the desk -- the anchored-arm helper, available and unscheduled', 'DESK', d('b358_the_li_asymptotics.txt'),
     'CHECKS that rather than asserting it. ### The anchored-arm helper stands as'),
    ("the desk -- the wave's candidate list, typed and not ranked (b324)", 'DESK', d('b324_the_keystones_reread.txt'),
     'THE WAVE\u2019S CANDIDATE LIST, TYPED. ### NO RECOMMENDATION, NO RANKING.'),
    ('the desk -- the wave is the author\u2019s and no seat starts one', 'DESK', d('b324_the_keystones_reread.txt'),
     'THE WAVE IS THE AUTHOR'),
    ('the desk -- the patent receipts, as the last fold left them', 'DESK', d('b348_fold_emitted.md'),
     'the one item on this desk with a date'),
    ('the desk -- what a fold is, as the last fold said it', 'DESK', d('b348_fold_emitted.md'),
     'A fold is a summary of its acts at their own grades.'),
    ('the roster finding this act acts on (b359)', 'DESK', d('b359_the_currency_pass.txt'),
     'FACES_LEDGER.md` IS NOT IN THE MIRROR ROSTER'),

    # ---- THE METHOD LAYER: WHAT THE SPAN MINTED OR MECHANIZED, EACH AT ITS OWN ACT ------------------
    ('method -- b349 builds the shared normaliser', 'METHOD', d('b349_the_room_relative.txt'),
     'BUILT: `tools/quote_norm.py`'),
    ('method -- b354 builds the anchor cure, and its fixtures find two defects in it first', 'METHOD',
     d('b354_the_sixth_frame.txt'),
     'AND ITS OWN FIXTURES FOUND TWO DEFECTS IN IT BEFORE IT WAS USED ONCE:'),
    ('method -- b354, the anchor tool refusing on its first use, and every refusal right', 'METHOD',
     d('b354_the_sixth_frame.txt'),
     "AND THEN IT REFUSED FIVE OF THIS ACT'S OWN TWENTY-SIX HINTS ON ITS FIRST USE"),
    ('method -- b352 mints the straddling-gate rule', 'METHOD', d('b352_the_fourth_candidate.txt'),
     "FILING TWO -- THE LORE'S THIRD SIGHTING, MINTED:"),
    ('method -- b352 runs the census the mechanized half licenses', 'METHOD', d('b352_the_fourth_candidate.txt'),
     'AND THE CENSUS OVER EVERY SEALED REGISTRATION IN THE RECORD:'),
    ('method -- b354, the seal taken against an explicit refusal', 'METHOD', d('b354_the_sixth_frame.txt'),
     '(E1) A FIRST VERSION OF THIS REGISTRATION WAS SEALED AGAINST AN EXPLICIT REFUSAL.'),
    ('method -- b354, the rule that came out of it', 'METHOD', d('b354_the_sixth_frame.txt'),
     'AN INSTRUMENT REFUSING IS ONLY A REFUSAL IF SOMETHING'),
    ('method -- b355, the species refined: a dropped possessive is a changed word', 'METHOD',
     d('b355_what_the_arrays_are.txt'), 'A DROPPED POSSESSIVE IS A CHANGED WORD'),
    ('method -- b357 applies b348’s minted cure to its own tool', 'METHOD', d('b357_what_the_ledgers_say.txt'),
     'THE CURE IS THE ONE b348 MINTED AND IS NOW APPLIED:'),
    ('method -- b358, the LOCK vocabulary, prospective only', 'METHOD', d('b358_the_li_asymptotics.txt'),
     '(R3) THE VOCABULARY, PROSPECTIVE ONLY.'),
    ('method -- b358 mechanizes the numbered-repeat cure', 'METHOD', d('b358_the_li_asymptotics.txt'),
     'AND THE NUMBERED-REPEAT SPECIES HIT THIS ACT FOUR TIMES, SO IT IS NOW MECHANIZED.'),

    # ---- THE ACTS' OWN CORRECTIONS, DEFECTIVE BARS AND DECLARED DEFECTS -----------------------------
    ('correction -- b349, the order’s own citation checked rather than accepted', 'DECLARED',
     d('b349_the_room_relative.txt'),
     "(E2) THE ORDER'S CITATION OF THE SPECIES DID NOT MATCH THE RECORD, AND THE ACT SAYS SO RATHER"),
    ('defective bar -- b352, a sealed clause of its own registration', 'DECLARED',
     d('b352_the_fourth_candidate.txt'),
     "(E5) A SEALED CLAUSE OF THIS ACT'S OWN REGISTRATION IS DEFECTIVE, AND IT IS TABLED AND NOT"),
    ('defective bar -- b352, the multi-arm detector narrower than its own rule', 'DECLARED',
     d('b352_the_fourth_candidate.txt'),
     "(E6) THE BAR-FLOOR ARM'S MULTI-ARM DETECTOR DID NOT SEE THIS ACT'S TWO-ARM BAR."),
    ('defective bar -- b354, the sealed criterion tabled and not edited', 'DECLARED', d('b354_the_sixth_frame.txt'),
     'THE CRITERION IS TABLED, NOT EDITED, AND THE TEMPTATION IS WORTH NAMING.'),
    ('defective bar -- b354, the sealed branch rule with no slot for the outcome', 'DECLARED',
     d('b354_the_sixth_frame.txt'),
     'SO THE SEALED BRANCH RULE HAS NO SLOT FOR THIS OUTCOME, AND THAT IS A FINDING OF THIS ACT.'),
    ('correction -- b354, a wall quoted from a run the act does not rely on', 'DECLARED',
     d('b354_the_sixth_frame.txt'), 'THIS BANK FIRST QUOTED A WALL FROM A SUPERSEDED RUN'),
    ('seat defect -- b356, wrong twice in the same direction', 'DECLARED', d('b356_the_boundary.txt'),
     'SO THE SEAT WAS WRONG TWICE IN THE SAME DIRECTION'),
    ('seat defect -- b357, the act’s own subject turned on itself', 'DECLARED',
     d('b357_what_the_ledgers_say.txt'), 'BUILT A CHECK THAT CONFIRMED RATHER THAN TESTED'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b360 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b360_extract_notes', LINES)
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
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n,
                          differs=bool(differs)))
        rec('')
        rec('  [%-6s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### **AND THAT PROPORTION IS THE TOOL EARNING ITS KEEP, NOT A GRADE ON THE SEAT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b360_extract_notes', LINES)
    io.open(d('b360_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
