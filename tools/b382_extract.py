# -*- coding: utf-8 -*-
"""b382_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**

### ### **COMPONENT 1 ASKS FOR THE SEQUENCE'S OWN ACCOUNT, QUOTED AND NOT SUMMARISED**, so this
### table is longer than usual on purpose: ### **EVERY CLAIM THE ACCOUNT MAKES ABOUT A PRIOR ACT IS
### ### ANCHORED IN THAT ACT'S OWN BANK**, and the account is assembled from these lines rather than
### from this seat's memory of them.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b382_ferry_2026-09-09.txt')
B375 = d('b375_the_keystone_and_cluster_census.txt')
B376 = d('b376_the_two_axis_read.txt')
B377 = d('b377_the_unblocked_obligation.txt')
B378 = d('b378_the_refs_widened.txt')
B379 = d('b379_the_apparatus_axis_rescored.txt')
B380 = d('b380_the_role_axis_scored_structurally.txt')
B381 = d('b381_the_control_rebuilt.txt')
B381C = d('b381_closing.txt')
EVID = d('b380_ruling_evidence.txt')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b382 - THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED. The'),
    ('the order -- the author takes the second path', 'ORDER', FERRY,
     "executor's draft offered two paths; the author takes the second."),
    ('the order -- the relating-word feature is NOT built', 'ORDER', FERRY,
     'The relating-word feature is NOT built. Reason recorded: reach'),
    ('the order -- a reader and not a predicate', 'ORDER', FERRY,
     'understood rather than a structure measured, which is a reader'),
    ('the order -- this act closes the sequence and does not rule', 'ORDER', FERRY,
     'and not a predicate. This act closes the evidence sequence and'),
    ('the order -- component 1, quoted not summarised', 'ORDER', FERRY,
     "COMPONENT 1 - THE SEQUENCE'S OWN ACCOUNT, assembled from its"),
    ('the order -- component 1, what each act asked, found and left', 'ORDER', FERRY,
     'banks and quoted, not summarised: what each act from the census'),
    ('the order -- component 1, the three tests and their crossing', 'ORDER', FERRY,
     'the three tests and their crossing; the corpus\'s own prior'),
    ('the order -- component 1, four widenings and none of the role column', 'ORDER', FERRY,
     'definition and its drift between statement and operation; four'),
    ('the order -- component 1, the control that could fail', 'ORDER', FERRY,
     'and the standing count of documents that do not state what they'),
    ('the order -- component 1, one page, every claim anchored', 'ORDER', FERRY,
     'are. One page, every claim anchored.'),
    ('the order -- component 2, a conclusion about METHOD', 'ORDER', FERRY,
     'COMPONENT 2 - THE CONCLUSION THE EVIDENCE SUPPORTS, stated as a'),
    # ### **THESE THREE WERE TYPED FROM THE PASTE'S VISUAL WRAPPING AND FOUND NO ANCHOR** -- the
    # ### `b313`/`b317` species, and the tool caught it. ### **VERIFY EVERY CANDIDATE ANCHOR AGAINST
    # ### ### ITS FILE BEFORE WRITING IT**, which is what the second attempt did.
    ('the order -- component 2, not recoverable from structure', 'ORDER', FERRY,
     'conclusion about METHOD and not as a class ruling: role is not'),
    ('the order -- component 2, nor from their prose', 'ORDER', FERRY,
     "recoverable from a document's structure, and it is stated by"),
    ('the order -- component 2, must rest on DECLARATION', 'ORDER', FERRY,
     'prose either. Therefore the class ruling, whatever it rules,'),
    ('the order -- component 2, declaration rather than classification', 'ORDER', FERRY,
     'must rest on DECLARATION rather than on classification. State'),
    ('the order -- component 2, priced and NOT ordered here', 'ORDER', FERRY,
     'document, and a phased application - priced by the record\'s own'),
    ('the order -- component 3, the exemplar caution', 'ORDER', FERRY,
     'COMPONENT 3 - THE EXEMPLAR CAUTION, carried forward: the'),
    ('the order -- component 3, re-derived and not inherited', 'ORDER', FERRY,
     'that if that set is ever reused, it is re-derived and not'),
    ('the order -- component 4, the open items restated', 'ORDER', FERRY,
     'COMPONENT 4 - THE OPEN ITEMS, restated for the ruling: the four'),
    ('the order -- component 4, nothing closed but the sequence', 'ORDER', FERRY,
     'restated as a floor against the wider question. Nothing closed'),
    ('the order -- the closing, the evidence file named complete', 'ORDER', FERRY,
     "CLOSING: the ruling's evidence file finalised as this act's"),
    ('the order -- the closing, the untracked records named', 'ORDER', FERRY,
     'untracked run records b381 swept and returned named as still'),
    ('the order -- the closing, proposing nothing that waits on the ruling', 'ORDER', FERRY,
     'ferry as DRAFT - NAVIGATOR EDITS, proposing nothing that waits'),

    # ---- b375, THE CENSUS --------------------------------------------------------------------------
    ('b375 -- the same instrument on two definitions gives opposite answers', 'SEQ', B375,
     '### ### ### DEFINITIONS ONE ACT APART, GIVES OPPOSITE ANSWERS.**'),
    ('b375 -- the instrument did not change, the definition did', 'SEQ', B375,
     '### ### **THE INSTRUMENT DID NOT CHANGE. ### THE DEFINITION OF `KEYSTONE` DID.** ### The two '
     'sets'),
    ('b375 -- six clusters have documents and no keystone', 'SEQ', B375,
     '### ### RULING.** ### `6` clusters have documents and no keystone; the order asked for the '
     'fact'),

    # ---- b376, THE TWO-AXIS READ -------------------------------------------------------------------
    ('b376 -- every one of the three tests crosses the quadrants', 'SEQ', B376,
     '### ### ### **EVERY ONE OF THE THREE TESTS CROSSES THE QUADRANTS, AND SO DOES THE CORPUS`S '
     'OWN'),
    ('b376 -- the census drops clause (iii) and adds a size floor', 'SEQ', B376,
     '### ### THROUGH PROXIES, DROPS CLAUSE `(iii)` ENTIRELY AND ADDS A SIZE FLOOR THE DEFINITION '
     'NEVER'),
    ('b376 -- 340 of 349 documents', 'SEQ', B376,
     '### ### ### **THE FIRST THING BOTH READINGS AGREE ON IS THE SIZE OF `A?`: ### 340 OF 349 '
     'DOCUMENTS'),

    # ---- b377, THE OBLIGATION ----------------------------------------------------------------------
    ('b377 -- the pin was the missing element, not the terminal', 'SEQ', B377,
     '### ### ### **THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL.**'),
    ('b377 -- the banked figure is a floor and not an answer', 'SEQ', B377,
     '### ### ### **SO THE BANKED FIGURE IS A FLOOR AND NOT AN ANSWER**, and the reason it can only '
     'be a'),

    # ---- b378, THE REFS WIDENED --------------------------------------------------------------------
    ('b378 -- an upper bound taken at one ref is not a count', 'SEQ', B378,
     '### ### ### **AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT** -- and ### **A SEARCH THAT '
     'CANNOT'),
    ('b378 -- b377`s number was never wrong', 'SEQ', B378,
     '### ### **`b377`S NUMBER WAS NEVER WRONG. ### IT WAS AN UPPER BOUND TAKEN AT ONE REF AND WAS '
     'NOT'),

    # ---- b379, THE APPARATUS AXIS ------------------------------------------------------------------
    ('b379 -- correcting the suspect column moved nothing where the ruling needs movement', 'SEQ',
     B379,
     '### ### ### **THE SUSPECT COLUMN WAS UNDERCOUNTING, AND CORRECTING IT MOVED NOTHING WHERE '
     'THE'),
    ('b379 -- the correction leaves the role column exactly where it was', 'SEQ', B379,
     '### ### **THE CORRECTION ENLARGES THE APPARATUS COLUMN AND LEAVES THE ROLE COLUMN EXACTLY '
     'WHERE IT'),

    # ---- b380, THE FIRST STRUCTURAL FEATURE --------------------------------------------------------
    ('b380 -- the role column moved and the predicate failed its own control', 'SEQ', B380,
     '### ### ### **THE ROLE COLUMN MOVED FOR THE FIRST TIME IN FIVE ACTS, AND THE PREDICATE THAT '
     'MOVED'),
    ('b380 -- the premise survives its own widening', 'SEQ', B380,
     '### ### ### **THE PREMISE SURVIVES ITS OWN WIDENING.** ### Being generous about what counts '
     'as a'),
    ('b380 -- the A- column is measuring narrow reach', 'SEQ', B380,
     '### ### ### **SO THE `A-` COLUMN IS NOT MEASURING GATHERING. ### IT IS MEASURING NARROW '
     'REACH**,'),
    ('b380 -- agreement over all nine that declare anything', 'SEQ', B380,
     '### ### **AGREEMENT OVER ALL `9` THAT DECLARE ANYTHING  : `7` OF `9`.**'),

    # ---- b381, THE SECOND STRUCTURAL FEATURE AND THE CONTROL ---------------------------------------
    ('b381 -- the control was rebuilt so it could fail and the feature failed', 'SEQ', B381,
     '### ### ### **THE CONTROL WAS REBUILT SO THAT IT COULD FAIL IN BOTH DIRECTIONS, AND THE NEW'),
    ('b381 -- the two sets overlap completely', 'SEQ', B381,
     '### the highest gathering ratio is ### **`1.000`**, so the two sets ### **OVERLAP COMPLETELY '
     'AND NO'),
    ('b381 -- the branch, not adopted, the corpus not scored', 'SEQ', B381,
     '### ### ### **THE BRANCH IS PARTLY. ### THE PREDICATE IS NOT ADOPTED. ### THE CORPUS WAS NOT '
     'SCORED.**'),
    ('b381 -- heads stating a gathering purpose', 'SEQ', B381,
     '###   ### **HEADS STATING A GATHERING PURPOSE   : `63` OF `404`**'),
    ('b381 -- the balance of the rebuilt control', 'SEQ', B381,
     '### ### **THE BALANCE: `5` SYNTHESIS EXEMPLARS AND `61` GATHERING EXEMPLARS**, against a '
     'floor of'),
    ('b381 -- two independent structural features now fail the same distinction', 'SEQ', B381,
     '### ### ### INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME DISTINCTION.**'),
    ('b381 -- a control that cannot fail on one side is one defect', 'SEQ', B381,
     '### ### ### **A CONTROL THAT CANNOT FAIL ON ONE SIDE AND CANNOT INFORM ON THE OTHER IS NOT '
     'TWO'),

    # ---- THE EXEMPLAR CAUTION, FROM b381'S OWN CLOSING ---------------------------------------------
    ('b381 -- the matcher was repaired twice after its output was seen', 'CAUTION', B381C,
     '### ### ### **AND THE MATCHER THAT BUILT IT WAS REPAIRED TWICE AFTER ITS OUTPUT WAS SEEN.**'),
    ('b381 -- the part a reader should be most sceptical of', 'CAUTION', B381C,
     '### ### THAT IS EXACTLY THE CLAIM A READER CANNOT CHECK WITHOUT THE INTERMEDIATE NUMBERS**, '
     'so all'),
    ('b381 -- the staging incident, self-reported and reverted', 'CAUTION', B381C,
     '### ### ### **AND ONE INCIDENT, SELF-REPORTED AND REVERTED:** ### the closing commit used'),

    # ---- THE EVIDENCE FILE THIS ACT FINALISES ------------------------------------------------------
    ('the evidence file -- (R14) banked verbatim and whole', 'EVID', EVID,
     '### **(R14), THE AUTHOR`S, RATIFIED AT b381 AND STRIKEABLE. ### BANKED VERBATIM,'),
    ('the evidence file -- the role axis unchanged since b380', 'EVID', EVID,
     '### ### **SO THE RULING`S EVIDENCE ON THE ROLE AXIS IS UNCHANGED SINCE b380:** ### the'),

    # ---- THE LORE ----------------------------------------------------------------------------------
    ('the lore -- a predicate that knows one shape', 'LORE', PRED,
     '**A predicate written against the shape you have seen will report exactly that shape and '
     'will report'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def main():
    rec('=' * 100)
    rec('b382_extract.py -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, PRINTED BEFORE ANY QUOTATION.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        br = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
        hd = git(repo, 'rev-parse', 'HEAD')[:12]
        dirty = bool(git(repo, 'status', '--porcelain'))
        refs[name] = dict(branch=br, head=hd, dirty=dirty)
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s' % (name, br, hd, dirty))

    # ### **THE UNTRACKED RUN RECORDS `b381` SWEPT AND RETURNED**, named here so a later act does
    # ### not rediscover them as a defect. ### **THEY ARE NOT THIS ACT'S TO COMMIT EITHER.**
    rec('')
    rec('-' * 100)
    rec('  ### THE UNTRACKED RUN RECORDS, NAMED SO A LATER ACT DOES NOT REDISCOVER THEM.')
    rec('-' * 100)
    untracked = sorted(x[3:].strip() for x in git(ROOT, 'status', '--porcelain').split(chr(10))
                       if x.startswith('??') and 'b382' not in x)
    for u in untracked:
        rec('    %s' % u)
    rec('  ### ### **%d UNTRACKED RECORDS, LEFT BY EARLIER ACTS AND STILL UNTRACKED.** ### `b381`'
        % len(untracked))
    rec('  ### swept them in with `git add -A` and reverted them to exactly this state. ### **THEY')
    rec('  ### ### ARE NOT THIS ACT`S TO COMMIT EITHER**, and naming them is the whole of what this')
    rec('  ### act does about them.')

    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-7s] %s' % (tag, lbl))
        try:
            n, line = AF.find(path, hint)
        except Exception as e:
            noanchor += 1
            rec('      ### ### **NO ANCHOR** -- %s' % str(e)[:150])
            out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), line=None,
                            text=None, error=str(e)[:200]))
            continue
        diff = (line.rstrip(chr(10)) != hint)
        differing += 1 if diff else 0
        bytag[tag] = bytag.get(tag, 0) + 1
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, diff))
        rec('      | %s' % line.strip()[:200])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), line=n,
                        text=line.rstrip(chr(10))))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (differing, len(READS)))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL AND NO PRIOR SCORE WAS OVERWRITTEN.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b382_extract_notes', LINES)
    io.open(d('b382_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, untracked=untracked, built=out,
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
