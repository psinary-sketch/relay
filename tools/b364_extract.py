# -*- coding: utf-8 -*-
"""b364_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **WHAT THIS ACT READS IS A PREDICATE AND TWO RUNS**, and the predicate is the one thing a
### diagnosis must not paraphrase. ### `BAR 1` of the locked registration: ### **A PARAPHRASED PREDICATE
### IS THIS SEAT'S READING OF AN ARM AND NOT THE ARM.**
### ### **BAR: AN ANCHOR THIS ACT CANNOT LOCATE IS REPORTED AS NOT LOCATED AND IS NOT SUPPLIED FROM
### ### MEMORY.**
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


FERRY = d('b364_ferry_2026-09-07.txt')
SUITE = t('b357_checks.py')
B357 = d('b357_what_the_ledgers_say.txt')
B363 = d('b363_the_anchored_gate_arms.txt')
CEN363 = d('b363_census_run3.txt')
B314 = d('b314_the_fold_and_the_cold_clone.txt')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the leg', 'ORDER', FERRY, 'LEG 1 (b364) - THE COPY THAT DID NOT REPRODUCE. Diagnose, do'),
    ('the order -- do not repair-to-pass', 'ORDER', FERRY,
     'not repair-to-pass. Report what the failing locating arm'),
    ('the order -- what must be reported', 'ORDER', FERRY,
     'checked, what it found in the copy, and what it finds in the'),
    ('the order -- the environmental branch', 'ORDER', FERRY,
     'here before the diagnosis: (ENVIRONMENTAL - the copy fails for'),
    ('the order -- and what it requires be SHOWN', 'ORDER', FERRY,
     'suite at its own location still passes, shown by running it'),
    ('the order -- the real branch', 'ORDER', FERRY,
     "/ (REAL - the arm fails at the banked suite's own location too;"),
    ('the order -- the undecided branch', 'ORDER', FERRY,
     '/ (UNDECIDED - the resisting step named). In every'),
    ('the order -- nothing edited, no verdict moved', 'ORDER', FERRY,
     'branch the banked suite is not edited and no verdict is moved'),
    ("the order -- the navigator's expectation", 'ORDER', FERRY,
     "navigator's expectations: (L1) ENVIRONMENTAL"),

    # ---- (i) THE PREDICATE, AT ITS OWN SUITE -------------------------------------------------------
    ("the arm's own label, from its own suite", 'PRED', SUITE,
     "G-LOCATED (every classified row located by the anchor tool at its own ledger, NOW)"),
    ('the arm -- what it does with a row', 'PRED', SUITE, "n, line = AF.find(path, r['text'][:110])"),
    ('the arm -- what it calls a failure', 'PRED', SUITE, "print('    ### FAIL (NO ANCHOR NOW)"),
    ('the arm -- what it allows, and on what condition', 'PRED', SUITE,
     "ok_dec = ('%d' % was) in bank and ('%d' % now) in bank and 'STRADDLE THIS ACT' in bf"),
    ('the arm -- the four ledgers it reads', 'PRED', SUITE, "LEDGERS = {'FINDINGS.md': FINDINGS,"),

    # ---- (ii) WHAT THE COPY FOUND, AT b363's BANKED CONTROL ----------------------------------------
    ("b363's control row for b357", 'COPY', CEN363, 'b357  banked GATES FAILING 0'),
    ("b363's own reading of that failure", 'COPY', B363,
     "`G-LOCATED` reads an index whose lines have since moved"),

    # ---- b357's OWN PREDICTION, AT ITS OWN BANK ----------------------------------------------------
    ('b357 -- two line numbers straddle that act, declared', 'B357', B357,
     'AND TWO LINE NUMBERS STRADDLE THIS ACT, DECLARED BY'),
    ('b357 -- the relied-on line, and where its own append moved it', 'B357', B357,
     "`b357`'S OWN INDEX KEY MOVED THAT ROW TO `1054`.**"),
    ('b357 -- the second line, moved by the same append', 'B357', B357,
     '(the narrower row `b355` put there) ### **MOVED TO `645`**'),

    # ---- THE COLD-CLONE ACT'S WORK-ORDER -----------------------------------------------------------
    ('b314 -- the absolute-paths work-order, by its own ID', 'B314', B314,
     'W-ORD-ABSOLUTE-PATHS`.** ### Instrument files carry hard-coded'),
    ('b314 -- and what it says an instrument carrying one cannot do', 'B314', B314,
     'absolute paths into the corpus. ### **AN INSTRUMENT CARRYING ONE CANNOT BE RUN FROM A CLONE'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b364 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b364_extract_notes', LINES)
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
    npred = sum(1 for b in built if b['tag'] == 'PRED')
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **PREDICATE LINES LOCATED AT THE SUITE ITSELF : %d** ### -- the arm is QUOTED and not'
        % npred)
    rec('  ### paraphrased, which is BAR 1 of the locked registration.')
    rec('=' * 100)
    p = run_clock.write(D, 'b364_extract_notes', LINES)
    io.open(d('b364_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, predicate_lines=npred,
             built=built, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
