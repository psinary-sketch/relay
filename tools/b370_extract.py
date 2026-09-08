# -*- coding: utf-8 -*-
"""b370_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **A FOLD QUOTES NINE ACTS, SO EVERY QUOTATION IS LOCATED IN THE BANK OF THE ACT THAT
### ### ORIGINATED IT** -- `b360`'s rule, and the reason its rhyming obstructions were quoted at their
### own acts and not at the ledger row that collected them.
### ### **NO FINDING IS READ FROM A LATER ACT'S SUMMARY OF AN EARLIER ONE.**
### ### **AND THE SPAN COUNTER IS READ BEFORE IT IS FIXED**, so the act meets the tool it is ordered to
### repair as it stands.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b370_ferry_2026-09-08.txt')
SPAN = t('b363_span.py')
B = {n: d(f) for n, f in (
    (361, 'b361_the_held_item.txt'), (362, 'b362_the_approximation_register.txt'),
    (363, 'b363_the_anchored_gate_arms.txt'), (364, 'b364_the_copy_that_did_not_reproduce.txt'),
    (365, 'b365_the_owed_read_paid.txt'), (366, 'b366_the_dated_arm_sweep.txt'),
    (367, 'b367_the_scaffold_repair.txt'), (368, 'b368_the_front_document_reconciled.txt'),
    (369, 'b369_the_list_repaired.txt'))}

READS = [
    ('the order -- the act and its span', 'ORDER', FERRY,
     'ACT b370 - THE FOLD, b361 through b369, nine acts against the'),
    ('the order -- step zero, the tool that writes', 'ORDER', FERRY,
     "STEP ZERO - THE TOOL THAT WRITES INTO OTHER ACTS: the span"),
    ('the order -- and the fixture it demands', 'ORDER', FERRY,
     'fixture proving it leaves a foreign pointer byte-identical.'),
    ('the order -- a lesson filed and not built', 'ORDER', FERRY,
     'filed in a bank and not built into a tool is a lesson that will'),
    ('the order -- component 1, the nine', 'ORDER', FERRY,
     'COMPONENT 1 - THE FOLD, nine acts, each with its grade, owning'),
    ('the order -- component 1, the two extra tables', 'ORDER', FERRY,
     "the corrections the acts made to their own readings and"),
    ('the order -- component 2, the arc as one statement', 'ORDER', FERRY,
     'COMPONENT 2 - THE ARC AS ONE STATEMENT, at the grade the acts'),
    ('the order -- component 2, no new mathematics', 'ORDER', FERRY,
     'produced no new mathematics about the clause; it produced two'),
    ('the order -- component 2, its main product', 'ORDER', FERRY,
     'was making the record checkable by a reader who trusts none of'),
    ('the order -- component 3, the three mints', 'ORDER', FERRY,
     'COMPONENT 3 - THE LORE, with three mints: one incident does not'),
    ('the order -- component 3, the durability split', 'ORDER', FERRY,
     'by any arm); and the DURABILITY SPLIT - a repair to a tracked'),
    ('the order -- component 4, the desk', 'ORDER', FERRY,
     'COMPONENT 4 - THE DESK, swept under the freshness rule, marks'),
    ('the order -- component 5, the next arc', 'ORDER', FERRY,
     'COMPONENT 5 - THE NEXT ARC NAMED AND NOT OPENED: the federation'),
    ('the order -- component 5, its first target', 'ORDER', FERRY,
     'the ranking cannot look; and its first target is the one'),
    ('the order -- the closing', 'ORDER', FERRY,
     'CLOSING: the fold purely additive with the no-grade-moved check'),

    # ---- THE NINE ACTS, EACH AT ITS OWN BANK -------------------------------------------------------
    ('b361 -- the grade', 'ACT', B[361],
     'DECIDED. ### `K(pi_triv) = 0`, SO THE INDEX CONDITION IS VACUOUS FOR THE CORPUS'),
    ('b361 -- the obstacle: the value is identified, not quoted', 'ACT', B[361],
     'AND THE VALUE IS NOT QUOTED FROM THE SOURCE. ### IT IS AN IDENTIFICATION OF TWO OF THE'),
    ('b362 -- the grade', 'ACT', B[362],
     'LOCATED BUT NOT WORTH OPENING** -- at the reach the record can afford, and the reason is'),
    ('b362 -- the correction: the space', 'ACT', B[362],
     'THE CORRECTION IS THE SPACE**, and the source itself flags it:'),
    ('b363 -- the grade', 'ACT', B[363],
     'THE HELPER IS BUILT AND IT IS NARROWER THAN THE RULE IT WAS PROPOSED UNDER.'),
    ('b363 -- refuted in input as well as output', 'ACT', B[363],
     'AND THE DRAFT IS REFUTED IN ITS INPUT AS WELL AS IN ITS OUTPUT.'),
    ('b364 -- the grade', 'ACT', B[364], 'THE BRANCH IS `REAL`, AND THE COPY WAS INNOCENT.'),
    ('b364 -- refuted by a run and not by an argument', 'ACT', B[364],
     'SO THE NAVIGATOR'),
    ('b365 -- the grade', 'ACT', B[365],
     'THE CONVENTION IS LOCATED, AND THE SOURCE WORKS THE EXCEPTIONAL CASE ITSELF.'),
    ('b366 -- the grade', 'ACT', B[366],
     'THREE DATED ARMS IN THE WHOLE RECORD, OUT OF 1255 ARMS ACROSS 146 SUITES.'),
    ('b366 -- and the third is missing its content', 'ACT', B[366],
     'AND THE THIRD IS NOT HARDER TO WRITE. ### IT IS MISSING ITS CONTENT'),
    ('b367 -- the grade', 'ACT', B[367],
     'NOT LOCATED. ### THE TERMINALS DO NOT EXIST, AND THE KERNEL SAYS SO ITSELF.'),
    ('b367 -- the record already found it', 'ACT', B[367],
     'AND THE RECORD ALREADY FOUND THIS, THIRTEEN DAYS AGO, AND SAID SO IN THESE WORDS'),
    ('b368 -- the grade', 'ACT', B[368],
     'THE FRONT DOCUMENT IS RECONCILED, AND IT WAS RECONCILED WITHOUT EDITING A SENTENCE.'),
    ('b368 -- the ledger names only half of them', 'ACT', B[368],
     'LEDGER NAMES ONLY HALF OF THEM.'),
    ('b369 -- the grade', 'ACT', B[369],
     'THE LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED IN THE SAME FILE.'),
    ('b369 -- the predicate that knows one shape', 'ACT', B[369],
     'BOTH FAILURES ARE THE SAME SENTENCE: A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE'),
    ('b369 -- the durability split, in its own words', 'ACT', B[369],
     'THE TWO REPAIRS ARE NOT'),

    # ---- THE RECORD THIS FOLD APPENDS TO -----------------------------------------------------------
    ('the record -- the last fold heading', 'RECORD', FINDINGS,
     '## THE UNIFORMITY ARC, b349–b359 — THE FOLD'),
    ('the record -- the last fold filing line', 'RECORD', FINDINGS,
     '*A fold is a summary of its acts at their own grades. It proves nothing, discharges nothing, and '
     'moves no grade. No coordinate is closed, the partition stays UNDECIDED, and `h2` stands exactly '
     'where the deposit left it. Filed by b360'),

    # ---- THE TOOL THIS ACT IS SENT TO FIX ----------------------------------------------------------
    ('the span counter -- its own hardcoded act', 'STEPZERO', SPAN, 'THIS_ACT = 363'),
    ('the span counter -- the run-file write', 'STEPZERO', SPAN,
     "    p = run_clock.write(D, 'b363_span_notes', LINES)"),
    ('the span counter -- the json write', 'STEPZERO', SPAN,
     "    io.open(os.path.join(D, 'b363_span.json'), 'w', encoding='utf-8', newline=chr(10)).write("),
    ('the span counter -- its own claim to decide nothing', 'STEPZERO', SPAN,
     '### ### **THIS TOOL DECIDES NOTHING.**'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b370 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b370_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE REF, PRINTED BEFORE ANY QUOTATION FROM THE PAPERS REPOSITORY.')
    rec('-' * 100)
    b = subprocess.run(['git', '-C', PP, 'rev-parse', '--abbrev-ref', 'HEAD'],
                       capture_output=True, text=True).stdout.strip()
    h = subprocess.run(['git', '-C', PP, 'rev-parse', 'HEAD'],
                       capture_output=True, text=True).stdout.strip()
    rec('    PLACE-papers  ref `%s` = `%s`' % (b, h))
    rec('    ### **AND THE NINE BANKS ARE THIS REPOSITORY`S OWN, AT `relay` HEAD.**')
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
        rec('  [%-8s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:220])
    ndiff = sum(1 for x in built if x['differs'])
    counts = {}
    for x in built:
        counts[x['tag']] = counts.get(x['tag'], 0) + 1
    acts = sorted({x['file'].split('_')[0] for x in built if x['tag'] == 'ACT'})
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **BY TAG : %s**' % counts)
    rec('  ### ### **BANKS QUOTED, EACH THE ACT THAT ORIGINATED ITS OWN FINDING : %d ### -- %s**'
        % (len(acts), ', '.join(acts)))
    rec('  ### **NO FINDING IS READ FROM A LATER ACT`S SUMMARY OF AN EARLIER ONE** (`b360`s rule).')
    rec('=' * 100)
    p = run_clock.write(D, 'b370_extract_notes', LINES)
    io.open(d('b370_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             banks_quoted=acts, papers_ref=b, papers_head=h, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
