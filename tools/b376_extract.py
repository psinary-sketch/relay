# -*- coding: utf-8 -*-
"""b376_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE TWO AXES ARE QUOTED, NOT INVENTED**, so both of their sources are pulled here verbatim
### before any predicate is written: ### the author's rubric as `b375`'s order recorded it (AXIS A) and
### ### **THE TAXONOMY'S OWN `Tier K` OBLIGATION** ### -- *every such claim states its grade, terminal
### and pin* -- for AXIS B.
### ### ### **AND THE CORPUS'S OWN PRIOR ATTEMPT IS PULLED IN TWO PIECES, BECAUSE THEY DISAGREE:** ###
### the census's STATED three-clause definition, and its OPERATIONALISED line, which covers two of the
### three and adds a size floor the definition never mentions.
### ### **NO DOCUMENT IS REPAIRED, NO CLASS IS RULED AND NO ROW IS EDITED BY THIS FILE.**
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
GS = os.path.join('D:', os.sep, 'SIDE-global-section')
SE = os.path.join('D:', os.sep, 'SIDE-effects')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

REPOS = [('relay', ROOT), ('SIDE-global-section', GS), ('PLACE-papers', PP), ('SIDE-effects', SE)]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def p(*a):
    return os.path.join(PP, *a)


FERRY = d('b376_ferry_2026-09-08.txt')
PRIOR = d('b375_ferry_2026-09-08.txt')
B375BANK = d('b375_the_keystone_and_cluster_census.txt')
CENSUS = p('phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
TAX = p('phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
REGY = p('REGISTRY.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    # ---- THE ORDER ----------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY, 'ACT b376 - THE TWO-AXIS READ. Number not claimed by any'),
    ('the order -- the scope', 'ORDER', FERRY,
     'unclosed ferry. SCOPE: READS and CLASSIFICATION only. NO class'),
    ('the order -- it makes no ruling', 'ORDER', FERRY,
     "evidence the author's class ruling needs and makes no ruling."),
    ('the order -- step zero, the lock reads every gate', 'ORDER', FERRY,
     'STEP ZERO - THE LOCK READS EVERY GATE. b375'),
    ('the order -- step zero, fixture both polarities', 'ORDER', FERRY,
     'scan read NOT CLEAN and nobody looked. Chain the lock on every'),
    ('the order -- component 1, heard first', 'ORDER', FERRY,
     'COMPONENT 1 - THE CORPUS'),
    ('the order -- component 1, operation not prose', 'ORDER', FERRY,
     'location; state what test it actually applies, read from its'),
    ('the order -- component 2, quoted not invented', 'ORDER', FERRY,
     'COMPONENT 2 - THE TWO AXES, QUOTED NOT INVENTED: AXIS A -'),
    ('the order -- axis B, in the order`s words', 'ORDER', FERRY,
     'AXIS B - certifies at pins, meaning a'),
    ('the order -- what each predicate is deaf to', 'ORDER', FERRY,
     'with fixtures in both polarities, and state what each predicate'),
    ('the order -- component 3, both axes independently', 'ORDER', FERRY,
     'COMPONENT 3 - EVERY DOCUMENT SCORED ON BOTH AXES,'),
    ('the order -- component 4, do the tests track the axes', 'ORDER', FERRY,
     'COMPONENT 4 - DO THE TESTS TRACK THE AXES: for each of the'),
    ('the order -- component 4, a test that crosses mixes the axes', 'ORDER', FERRY,
     'crosses quadrants. A test that crosses is a test that'),
    ('the order -- component 5, the floor question', 'ORDER', FERRY,
     'COMPONENT 5 - THE FLOOR QUESTION, the author'),
    ('the order -- component 5, a floor and not a population', 'ORDER', FERRY,
     'plainly that the rubric-test set is a FLOOR and not a'),
    ('the order -- component 6, without recommending', 'ORDER', FERRY,
     'COMPONENT 6 - WHAT THIS READ CANNOT DECIDE: the ruling. State'),
    ('the order -- component 6, two marks rather than one class', 'ORDER', FERRY,
     'including, if the quadrants support it,'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'proposing only what this act found. The navigator'),

    # ---- AXIS A: THE AUTHOR'S RUBRIC, AS ITS OWN FERRY RECORDED IT ------------------------------------
    ('axis A -- the rubric, SUPPORT half', 'AXIS-A', PRIOR,
     'as the census'),
    ('axis A -- the rubric, KEYSTONE half', 'AXIS-A', PRIOR,
     'questions and working notes. KEYSTONES synthesize a cluster'),
    ('axis A -- the rubric, and may not carry those', 'AXIS-A', PRIOR,
     'other clusters - and may not carry those. Both are in ongoing'),

    # ---- AXIS B: THE TAXONOMY'S OWN WORDS -------------------------------------------------------------
    ('axis B -- Tier K, certified at a pin, with its obligation', 'AXIS-B', TAX,
     '**Tier K — Keystone-certified.**'),
    ('axis B -- Tier C, which certifies nothing', 'AXIS-B', TAX,
     '**Tier C — Cluster-synthesis.**'),
    ('axis B -- the registry`s own tier legend', 'AXIS-B', REGY,
     '**Document-tier legend (2026-07-28; Tier E added 2026-08-08'),

    # ---- COMPONENT 1: THE CORPUS'S OWN PRIOR ATTEMPT, IN TWO PIECES THAT DISAGREE ---------------------
    ('the prior attempt -- the STATED definition, three clauses', 'PRIOR', CENSUS,
     '| ### **KEYSTONE** | (i) states results for external readers'),
    ('the prior attempt -- the OPERATIONALISED line', 'PRIOR', CENSUS,
     '**OPERATIONALISED:** (i) = an `Abstract` heading or an ORCID block'),
    ('the prior attempt -- its own class test for SUPPORT', 'PRIOR', CENSUS,
     '| **SUPPORT** | working papers, notes, consults, **logs** |'),
    ('the prior attempt -- the correction it recorded', 'PRIOR', CENSUS,
     'The corrected figure is 16, and the correction is recorded rather than the raw number'),
    ('the prior attempt -- what it says about spines', 'PRIOR', CENSUS,
     'CONSTELLATION-MAP CONSEQUENCE: no existing synthesis can serve as a constellation spine'),

    # ---- WHAT b375 BANKED, WHICH THIS ACT READS AND DOES NOT RE-DERIVE --------------------------------
    ('b375 -- three tests, one word', 'RECORD', B375BANK,
     'THE WORD `KEYSTONE` NAMES THREE DIFFERENT TESTS IN THIS RECORD, AND THEY DO NOT'),
    ('b375 -- which governs is a ruling', 'RECORD', B375BANK,
     'WHICH GOVERNS IS A RULING AND NOT A READ.'),
    ('b375 -- the incident this act`s step zero cures', 'RECORD', B375BANK,
     'THE FIRST REGISTRATION WAS LOCKED OVER A FACE CARRYING A LIVE STRUCK-STEM USE.'),

    # ---- WHAT THE RECORD ALREADY RULED ---------------------------------------------------------------
    ('the lore -- a predicate that knows one shape', 'LORE', PRED,
     '**A predicate written against the shape you have seen will report exactly that shape and will '
     'report'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec('b376 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b376_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, PRINTED BEFORE ANY QUOTATION.')
    rec('-' * 100)
    refs = {}
    for name, path in REPOS:
        b = subprocess.run(['git', '-C', path, 'rev-parse', '--abbrev-ref', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        h = subprocess.run(['git', '-C', path, 'rev-parse', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        st = subprocess.run(['git', '-C', path, 'status', '--porcelain'],
                            capture_output=True, text=True).stdout.strip()
        refs[name] = dict(branch=b, head=h, dirty=bool(st))
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s' % (name, b, h[:12], bool(st)))
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        if not os.path.exists(path):
            rec('  ### ### **NO SUCH FILE** : %s -- %s' % (label, path))
            bad += 1
            continue
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % str(e).replace(chr(10), ' | ')[:200])
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n,
                          differs=bool(differs), text=line.rstrip()))
        rec('')
        rec('  [%-7s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:230])
    ndiff = sum(1 for x in built if x['differs'])
    counts = {}
    for x in built:
        counts[x['tag']] = counts.get(x['tag'], 0) + 1
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **BY TAG : %s**' % counts)
    rec('  ### ### **AND THE TWO AXES ARE NOW BOTH IN ONE FILE IN THEIR SOURCES` OWN WORDS, BEFORE ANY')
    rec('  ### ### PREDICATE IS WRITTEN.**')
    rec('  ### **NO DOCUMENT WAS REPAIRED, NO CLASS WAS RULED AND NO ROW WAS EDITED.**')
    rec('=' * 100)
    q = run_clock.write(D, 'b376_extract_notes', LINES)
    io.open(d('b376_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             refs=refs, built=built,
             run_file=os.path.basename(q), run_clock=run_clock.read_stamp(q)), indent=1))
    print('  written: %s' % os.path.basename(q))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
