# -*- coding: utf-8 -*-
"""b366_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **ADDITION ONE PUTS A QUOTATION FIRST**, and the locked registration reproduces it. ### This file
### RE-PULLS it from `b365`'s closing by the anchor tool, so the quotation inside a locked file can be
### checked against the file it came from rather than taken on the seat's word.
### ### **AND THE `(R3)` QUOTATIONS ARE PULLED FROM THE PINNED RENDERING ITSELF**, not copied out of
### `b365`'s prose. ### **A QUOTATION COPIED FROM A QUOTATION IS A RECOLLECTION WITH A CITATION ON IT.**
### ### **NO SOURCE IS FETCHED.** ### The pinned text on disk is the only source text read.
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
T = os.path.join(ROOT, 'tools')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(T, n)


FERRY = d('b366_ferry_2026-09-07.txt')
DRAFT = d('b365_closing.txt')
SRC = d('b358_source_lagarias0404394.txt')
B357S = t('b357_checks.py')
B363 = d('b363_the_anchored_gate_arms.txt')
B364 = d('b364_the_copy_that_did_not_reproduce.txt')
B365 = d('b365_the_owed_read_paid.txt')

READS = [
    # ---- THE ORDER AND ITS RULINGS -----------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY, 'ACT b366 - THE DATED-ARM SWEEP. The executor'),
    ('(R1) -- the fold threshold', 'RULING', FERRY, '(R1) THE FOLD THRESHOLD is NINE acts. Until a span'),
    ('(R1) -- and the spans stay beside it', 'RULING', FERRY,
     '"the fold is due" is not said. The nine observed spans stay on'),
    ('(R2) -- what a gate suite is for', 'RULING', FERRY,
     '(R2) WHAT A GATE SUITE IS FOR, split by predicate. An arm'),
    ('(R2) -- the standing half', 'RULING', FERRY,
     'the act wrote - is a STANDING CHECK and must reproduce at any'),
    ('(R2) -- the dated half, and the content/address test', 'RULING', FERRY,
     'by CONTENT rather than by ADDRESS: a predicate asking whether a'),
    ('(R2) -- prospective, and nothing rewritten', 'RULING', FERRY,
     'row sits at a line number is dated. Prospective. No past suite'),
    ("(R2) -- and b363's control relabelled here, not by editing b363", 'RULING', FERRY,
     'correctness on its standing ones - relabelled in this act'),
    ('(R3) -- the grade word', 'RULING', FERRY,
     "(R3) THE GRADE WORD: where a source applies its own theorem to"),
    ('(R3) -- where it sits between the two it is not', 'RULING', FERRY,
     'SUPPORTED-BY-THE-SOURCE'),
    ('the order -- addition one', 'ORDER', FERRY,
     'ADDITION ONE - THE RULING THE DRAFT NAMES IS QUOTED FIRST:'),
    ('the order -- addition two', 'ORDER', FERRY,
     'ADDITION TWO - THE SWEEP AS A REWRITE RULE, NOT A REPAIR:'),
    ('the order -- the helper-or-work-order test', 'ORDER', FERRY,
     'by tool; write the rewrite rule (address predicates become'),
    ('the order -- the two figures asked for apart', 'ORDER', FERRY,
     'exist and how many are one substitution from standing.'),
    ('the order -- addition three', 'ORDER', FERRY,
     'ADDITION THREE - THE TWO SPECIES KEPT APART, as b364 kept them:'),
    ('the order -- the closing draft scope', 'ORDER', FERRY,
     'NAVIGATOR EDITS, and it should propose THE SCAFFOLD REPAIR: the'),

    # ---- ADDITION ONE: THE DRAFT'S OWN RULING ------------------------------------------------------
    ('the draft -- the ruling it says would make the sweep unnecessary', 'DRAFT', DRAFT,
     'AND THE ONE THING THAT WOULD MAKE THE SWEEP UNNECESSARY, NAMED:'),
    ('the draft -- and what it says would follow', 'DRAFT', DRAFT,
     'that a banked suite is a certificate of its own moment and is not re-run.'),

    # ---- THE ONE CONFIRMED INSTANCE, AT ITS OWN SUITE ----------------------------------------------
    ("the confirmed dated arm -- its own label", 'DATED', B357S,
     'G-LOCATED (every classified row located by the anchor tool at its own ledger, NOW)'),
    ('the confirmed dated arm -- the address comparison', 'DATED', B357S, "if n != r['line']:"),
    ('the confirmed dated arm -- the frozen literal it needs', 'DATED', B357S,
     "ok_dec = ('%d' % was) in bank and ('%d' % now) in bank and 'STRADDLE THIS ACT' in bf"),
    ('b364 -- the half that holds and the half that cannot', 'DATED', B364,
     'WHAT THE ARM WAS CERTIFYING -- TWO THINGS, AND ONLY ONE OF THEM HAS FAILED'),
    ('b364 -- the species named', 'DATED', B364, 'AND THE SPECIES IS NAMED: A DATED ARM'),
    ('b364 -- it does not become wrong, it becomes old', 'DATED', B364,
     'IT DOES NOT BECOME WRONG. ### IT BECOMES OLD'),
    ('b364 -- and the choice it named and did not make', 'DATED', B364,
     'DOES NOT DECIDE IT EITHER -- IT NAMES THE CHOICE'),

    # ---- THE RELABELLING'S SUBJECT, AT b363's OWN BANK ---------------------------------------------
    ("b363 -- the control's figure", 'RELABEL', B363,
     "COPIES REPRODUCING THEIR OWN ACT'S VERDICT : 5 of 6"),
    ('b363 -- and its own reading of the one that did not', 'RELABEL', B363,
     'NOT REPRODUCE IS A MEASUREMENT OF A SUITE READING A MOVED REPOSITORY.** ### It is reported at full'),

    # ---- (R3): THE QUOTATIONS, AT THE PINNED RENDERING ITSELF --------------------------------------
    ("the source -- Theorem 5.1's own quantifier", 'R3', SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    ('the source -- the convention it states for the exception', 'R3', SRC, 'GL(1) we have e(0,π'),
    ('the source -- and why it is forced', 'R3', SRC,
     'if we wish to have entire functions in all cases, for we must re move the poles at s = 0 and'),
    ('the source -- it applies a cuspidal-hypothesis lemma to the exception', 'R3', SRC,
     'Remark. For the case πtriv on GL(1) Lemma 4.3 yields'),
    ("the source -- and it evaluates the theorem's constant for the exception", 'R3', SRC,
     'C1(πtriv ) = 1'),
    ('the source -- with the conductor it uses to do so', 'R3', SRC, 'using Q(πtriv) = 1.'),
    ('b365 -- the sentence the grade word is for', 'R3', B365,
     'SO THE SUPPORT IS BY THE PAPER'),

    # ---- THE OTHER SPECIES, KEPT APART -------------------------------------------------------------
    ('b365 -- the wrong arm has no mechanizable half', 'SPECIES', B365,
     'ITS ONLY CURE IS A SECOND READER.**'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b366 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b366_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('  ### ### **AND NO SOURCE IS FETCHED. ### THE PINNED TEXT ON DISK IS THE ONLY SOURCE TEXT.**')
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
        rec('  [%-7s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    nrule = sum(1 for b in built if b['tag'] == 'RULING')
    nr3 = sum(1 for b in built if b['tag'] == 'R3')
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec("  ### ### **RULING LINES LOCATED AT THE ORDER ITSELF : %d** ### -- the rulings this act executes"
        % nrule)
    rec('  ### are quoted from the paste that carries them, and none is retyped.')
    rec("  ### ### **(R3) LINES LOCATED AT THE PINNED RENDERING : %d** ### -- the grade word's evidence is"
        % nr3)
    rec("  ### pulled from the source, not copied out of `b365`'s prose.")
    rec('  ### **AND THE SEAM STANDS: A HASH ON A PDF DOES NOT CERTIFY THAT ITS EXTRACTED TEXT IS A')
    rec('  ### FAITHFUL RENDERING OF IT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b366_extract_notes', LINES)
    io.open(d('b366_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff,
             ruling_lines=nrule, r3_lines=nr3, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
