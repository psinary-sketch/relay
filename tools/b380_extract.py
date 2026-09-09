# -*- coding: utf-8 -*-
"""b380_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**"""
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


FERRY = d('b380_ferry_2026-09-08.txt')
B379CLOSE = d('b379_closing.txt')
B379BANK = d('b379_the_apparatus_axis_rescored.txt')
B376BANK = d('b376_the_two_axis_read.txt')
B375FERRY = d('b375_ferry_2026-09-08.txt')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b380 - THE ROLE AXIS, SCORED STRUCTURALLY. The executor'),
    ('the order -- adopted in aim, replaced in method', 'ORDER', FERRY,
     'draft is ADOPTED in its aim and REPLACED in its method, for the'),
    ('the order -- the reason four acts have printed', 'ORDER', FERRY,
     'reason four acts have printed: the role column has not moved'),
    ('the order -- component 1, the premise tested not assumed', 'ORDER', FERRY,
     'COMPONENT 1 - THE PREMISE, REGISTERED AND TESTED, NOT ASSUMED:'),
    ('the order -- component 1, on the record before the method runs', 'ORDER', FERRY,
     'count scored NOT DETERMINABLE, so the premise is on the record'),
    ('the order -- component 2, role from structure', 'ORDER', FERRY,
     "COMPONENT 2 - ROLE FROM STRUCTURE, built from the author's"),
    ('the order -- component 2, what a document DRAWS ON', 'ORDER', FERRY,
     'itself: the clusters it names, the kernels it names, the other'),
    ('the order -- component 2, the two fixtures from the declarers', 'ORDER', FERRY,
     'known to gather and a document known to synthesize, each named'),
    ('the order -- component 2, state what it is deaf to', 'ORDER', FERRY,
     'seven that declare. State plainly what the predicate'),
    ('the order -- component 3, the prior score never overwritten', 'ORDER', FERRY,
     'predicate, the prior statement-based score kept beside it and'),
    ('the order -- component 3, the predicate`s own control', 'ORDER', FERRY,
     'declare - which is the predicate'),
    ('the order -- component 3, a disagreement is a defect in the predicate', 'ORDER', FERRY,
     'disagreement there is reported at full prominence as a defect'),
    ('the order -- component 4, the verdict on the method', 'ORDER', FERRY,
     'COMPONENT 4 - THE VERDICT ON THE METHOD, not on the class:'),
    ('the order -- component 4, role must be declared', 'ORDER', FERRY,
     'finding is that role must be DECLARED, which makes the ruling a'),
    ('the order -- component 4, no class ruled in any branch', 'ORDER', FERRY,
     'No class is ruled in any branch.'),
    ("the order -- the closing, the ruling's evidence file", 'ORDER', FERRY,
     "CLOSING: the ruling's evidence file updated with this act's"),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'the next ferry as DRAFT - NAVIGATOR EDITS. The navigator'),
    ('the order -- (F3), the both-axes quadrant non-empty', 'ORDER', FERRY,
     'declare; (F3) the both-axes quadrant is non-empty for the first'),
    # ---- THE RUBRIC THE PREDICATE IS BUILT FROM ----------------------------------------------------
    ("the rubric -- the SUPPORT half, in the author's words", 'RUBRIC', B375FERRY,
     "as the census's own test: SUPPORT documents gather a subject's"),
    ("the rubric -- the KEYSTONE half, in the author's words", 'RUBRIC', B375FERRY,
     'questions and working notes. KEYSTONES synthesize a cluster'),
    ('the rubric -- against other available content', 'RUBRIC', B375FERRY,
     'other clusters - and may not carry those. Both are in ongoing'),
    # ---- WHAT FOUR ACTS PRINTED --------------------------------------------------------------------
    ('b376 -- the corpus is largely silent about its own role', 'PRIOR', B376BANK,
     '### ### ### **THE FIRST THING BOTH READINGS AGREE ON IS THE SIZE OF `A?`: ### 340 OF 349'),
    ('b376 -- axis A is deaf to a document that never says so', 'PRIOR', B376BANK,
     '###   ### **AXIS A IS DEAF TO** ### a document that synthesises against other content and never'),
    ('b379 -- the correction moved nothing where the ruling needs movement', 'PRIOR', B379BANK,
     '### ### ### **THE SUSPECT COLUMN WAS UNDERCOUNTING, AND CORRECTING IT MOVED NOTHING WHERE THE'),
    ('b379 -- the axes come apart further', 'PRIOR', B379BANK,
     '### ### WAS**, so the two axes come apart further rather than closer -- which is the opposite of'),
    ('the draft -- the role column has not moved once', 'DRAFT', B379CLOSE,
     '### ### ### **THE STANDING OBSERVATION THIS DRAFT IS BUILT ON:** ### four acts have now widened,'),
    ('the draft -- the ruling is not waiting on more apparatus evidence', 'DRAFT', B379CLOSE,
     '### ### APPARATUS EVIDENCE.**'),
    ('the draft -- the interesting number is the same shape', 'DRAFT', B379CLOSE,
     "### ### **AND THE INTERESTING NUMBER IS THE SAME SHAPE AS THIS ACT'S:** ### not the new `A+` total, but"),
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
    rec('b380 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec('  ### anchor_from_file fixtures : %s' % (AF.self_test() if hasattr(AF, 'self_test') else True))
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

    # ### **THE DECLARING DOCUMENTS, NAMED FROM `b376`'S BANKED JSON AND NEVER TYPED HERE.**
    AX = json.load(io.open(d('b376_axes.json'), encoding='utf-8'))
    syn = [x['file'] for x in AX['scored'] if x['axis_a'] == 'A+']
    gat = [x['file'] for x in AX['scored'] if x['axis_a'] == 'A-']
    rec('')
    rec('-' * 100)
    rec('  ### THE DOCUMENTS THAT DECLARE, WHICH ARE THE PREDICATE`S CONTROL SET.')
    rec('-' * 100)
    rec('    ### **SCORED `A+` FROM A STATEMENT THEY MAKE -- THE SEVEN THE ORDER NAMES : %d**'
        % len(syn))
    for f in syn:
        rec('      %s' % f)
    rec('    ### **AND SCORED `A-` FROM A STATEMENT THEY MAKE : %d**' % len(gat))
    for f in gat:
        rec('      %s' % f)
    rec('    ### ### **SO NINE DOCUMENTS CARRY A STATEMENT-BASED MARK, NOT SEVEN.** ### The order`s')
    rec('    ### phrase names the seven that declare SYNTHESIS; ### **THE GATHERING FIXTURE COMPONENT 2')
    rec('    ### ### ASKS FOR CANNOT COME FROM THAT SET, BECAUSE NONE OF THE SEVEN GATHERS.** ### The')
    rec('    ### reading this act takes, declared on its locked face: ### **THE CONTROL IS RUN OVER ALL')
    rec('    ### ### NINE, AND THE AGREEMENT IS REPORTED OVER THE SEVEN AND OVER THE NINE SEPARATELY**,')
    rec('    ### so `(F2)` can be read exactly as it was written.')

    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-6s] %s' % (tag, lbl))
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
    pth = run_clock.write(D, 'b380_extract_notes', LINES)
    io.open(d('b380_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, declare_synthesis=syn, declare_gathering=gat,
                        built=out, run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
