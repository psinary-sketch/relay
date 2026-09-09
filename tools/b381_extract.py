# -*- coding: utf-8 -*-
"""b381_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**"""
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


FERRY = d('b381_ferry_2026-09-09.txt')
B380BANK = d('b380_the_role_axis_scored_structurally.txt')
B380CLOSE = d('b380_closing.txt')
B379BANK = d('b379_the_apparatus_axis_rescored.txt')
B375FERRY = d('b375_ferry_2026-09-08.txt')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    # ---- THE RULING --------------------------------------------------------------------------------
    ('(R14) -- the ruling, ratified by this paste and strikeable', 'RULING', FERRY,
     "RULING (R14), the author's, ratified by this paste and"),
    ('(R14) -- by content and role, not by location', 'RULING', FERRY,
     'strikeable: THE CLASS RULING GOVERNS DOCUMENTS BY CONTENT AND'),
    ('(R14) -- where the canonical copy lives is a separate fact', 'RULING', FERRY,
     'document; where its canonical copy lives is a separate fact'),
    ('(R14) -- the book is inside the class ruling and outside the mirroring one', 'RULING', FERRY,
     "is therefore within the class ruling's reach and outside the"),
    ('(R14) -- both hold, neither is edited into the other', 'RULING', FERRY,
     "mirroring ruling's - both hold, neither is edited into the"),
    ('(R14) -- the registry-drift filing stays open and is the author`s', 'RULING', FERRY,
     "other. The filing on that document's registry drift stays open"),

    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b381 - THE CONTROL REBUILT, AND CO-LOCATION TESTED. The'),
    ('the order -- concentration REPLACED by co-location', 'ORDER', FERRY,
     'executor\'s draft is ADOPTED in its aim; its "concentration" is'),
    ('the order -- the non-adoption clause stands', 'ORDER', FERRY,
     'non-adoption clause stands.'),
    ('the order -- component 1, the control`s own weakness measured first', 'ORDER', FERRY,
     "COMPONENT 1 - THE CONTROL'S OWN WEAKNESS, MEASURED FIRST: b380"),
    ('the order -- component 1, a threshold any value would have passed', 'ORDER', FERRY,
     'agreed with seven declaring synthesis at a threshold any value'),
    ('the order -- component 1, both facts as ONE finding', 'ORDER', FERRY,
     'Report both facts as one finding - a control that cannot fail'),
    ('the order -- component 1, from the record`s own purpose statements', 'ORDER', FERRY,
     "add gathering exemplars taken from the RECORD'S OWN PURPOSE"),
    ('the order -- component 1, heads that say they record, collect or certify nothing',
     'ORDER', FERRY,
     'whose own heads say they record, collect, or certify nothing,'),
    ('the order -- component 1, until it can fail in both directions', 'ORDER', FERRY,
     'each quoted - until the exemplar set can fail in both'),
    ('the order -- component 1, no exemplar chosen by this seat`s judgement', 'ORDER', FERRY,
     "this seat's judgement of what a document is; each is quoted."),
    ('the order -- component 2, co-location not reach', 'ORDER', FERRY,
     'COMPONENT 2 - CO-LOCATION, NOT REACH: build the predicate from'),
    ('the order -- component 2, synthesis COMBINES a cluster with other content', 'ORDER', FERRY,
     "the author's rubric quoted - synthesis COMBINES a cluster with"),
    ('the order -- component 2, different clusters in the SAME unit', 'ORDER', FERRY,
     'sources from DIFFERENT clusters occupy the SAME unit (section,'),
    ('the order -- component 2, the unit defined in the registration before any score',
     'ORDER', FERRY,
     'entry, or paragraph, the unit defined in the registration'),
    ('the order -- component 2, a collection partitions and a synthesis co-locates',
     'ORDER', FERRY,
     'before any score). A collection partitions its sources one per'),
    ('the order -- component 2, reach kept unchanged beside', 'ORDER', FERRY,
     'entry; a synthesis co-locates them. Measure per document: reach'),
    ('the order -- component 2, state what it is deaf to', 'ORDER', FERRY,
     'polarities. State what the predicate is deaf to - at minimum,'),
    ('the order -- component 2, many sources in one place without relating them', 'ORDER', FERRY,
     'that a document quoting many sources in one place without'),
    ('the order -- component 3, the control run before any scoring', 'ORDER', FERRY,
     'COMPONENT 3 - THE CONTROL RUN BEFORE ANY SCORING: co-location'),
    ('the order -- component 3, NOT ADOPTED and the corpus NOT re-scored', 'ORDER', FERRY,
     'exemplars, the predicate is NOT ADOPTED, the corpus is NOT'),
    ('the order -- component 3, a failure is a result and is reported as one', 'ORDER', FERRY,
     "re-scored, and the act's finding is that co-location does not"),
    ('the order -- component 3, only if it separates does the corpus get scored', 'ORDER', FERRY,
     "Only if it separates does the corpus get scored, with b380's"),
    ('the order -- component 4, what the columns now mean', 'ORDER', FERRY,
     'COMPONENT 4 - WHAT THE COLUMNS NOW MEAN, stated plainly'),
    ('the order -- component 4, upper bound and unvalidated', 'ORDER', FERRY,
     'upper bound on synthesis and its negative column is'),
    ('the order -- the closing, (R14) recorded with the book`s status', 'ORDER', FERRY,
     "CLOSING: the ruling's evidence file updated; (R14) recorded"),
    ('the order -- (F1), co-location separates the rebuilt exemplar set', 'ORDER', FERRY,
     'co-location separates the rebuilt exemplar set, because the'),
    ('the order -- (F2), the positive role column shrinks materially', 'ORDER', FERRY,
     "(F2) the corpus's positive role column shrinks materially from"),

    # ---- THE RUBRIC, IN THE AUTHOR'S OWN WORDS -----------------------------------------------------
    ("the rubric -- the SUPPORT half, in the author's words", 'RUBRIC', B375FERRY,
     "as the census's own test: SUPPORT documents gather a subject's"),
    ("the rubric -- the KEYSTONE half, in the author's words", 'RUBRIC', B375FERRY,
     'questions and working notes. KEYSTONES synthesize a cluster'),
    ('the rubric -- against other available content', 'RUBRIC', B375FERRY,
     'AGAINST other available content - kernels, other keystones,'),

    # ---- WHAT b380 LEFT ----------------------------------------------------------------------------
    ('b380 -- the predicate failed its own control', 'PRIOR', B380BANK,
     '### ### ### IT FAILED ITS OWN CONTROL ON EXACTLY THE DISTINCTION THE RUBRIC IS ABOUT.**'),
    ('b380 -- reach is not argument', 'PRIOR', B380BANK,
     '### has reached, and ### **REACH IS NOT ARGUMENT.** ### The six documents reaching furthest '
     'are:'),
    ('b380 -- the upper bound and the unvalidated column', 'PRIOR', B380BANK,
     '### ### ### **SO THE `A+` COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE `A-` COLUMN IS'),
    ('b380 -- a control drawn from one side cannot test the distinction', 'PRIOR', B380BANK,
     '### ### ### **NEW -- `A CONTROL DRAWN FROM ONE SIDE OF A DISTINCTION CANNOT TEST THE`'),
    ('b380 -- the ledgers would have agreed with any threshold', 'PRIOR', B380BANK,
     '### **THEY WOULD HAVE AGREED WITH ANY THRESHOLD**, so their agreement carries no information '
     'about'),
    ('b379 -- the correction moved nothing where the ruling needs movement', 'PRIOR', B379BANK,
     '### ### ### **THE SUSPECT COLUMN WAS UNDERCOUNTING, AND CORRECTING IT MOVED NOTHING WHERE '
     'THE'),

    # ---- THE DRAFT THE ORDER ADOPTED AND AMENDED ---------------------------------------------------
    ('the draft -- component 1, the control rebuilt to fail in both directions', 'DRAFT', B380CLOSE,
     '### ### **COMPONENT 1 -- THE CONTROL, REBUILT SO THAT IT CAN FAIL IN BOTH DIRECTIONS.** ### '
     'The'),
    ('the draft -- component 2, the second feature not adopted if it fails', 'DRAFT', B380CLOSE,
     '### ### **COMPONENT 2 -- ONE SECOND FEATURE, TESTED AGAINST THAT CONTROL AND NOT ADOPTED.** '
     '###'),
    ('the draft -- CONCENTRATION, which the order REPLACED', 'DRAFT', B380CLOSE,
     '### ### **CONCENTRATION** ### -- whether a document`s references cluster on a few subjects '
     'it'),
    ('the draft -- a second failed feature is a better result', 'DRAFT', B380CLOSE,
     '### it. ### **A SECOND FAILED FEATURE IS A BETTER RESULT THAN A THIRD UNVALIDATED COLUMN.**'),

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
    rec('b381_extract.py -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
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

    # ### **b380'S CONTROL SET, CARRIED FROM ITS BANKED JSON AND NEVER TYPED HERE.** ### This act
    # ### rebuilds the set; it does not re-derive the old one by hand.
    E80 = json.load(io.open(d('b380_reads.json'), encoding='utf-8'))
    RS80 = json.load(io.open(d('b380_rescore.json'), encoding='utf-8'))
    rows80 = {r['file']: r for r in RS80['rows']}
    syn, gat = E80['declare_synthesis'], E80['declare_gathering']
    rec('')
    rec('-' * 100)
    rec('  ### `b380`S CONTROL SET, AND WHY THE ORDER CALLS IT WEAK.')
    rec('-' * 100)
    rec('    ### **DECLARING SYNTHESIS : %d ### / ### DECLARING GATHERING : %d**' % (len(syn), len(gat)))
    for f in syn:
        r = rows80[f]
        rec('      SYNTHESIS   %-62s reach %d   b380 scored %s'
            % (f, r['evidence']['reach'], r['structural_a']))
    for f in gat:
        r = rows80[f]
        rec('      GATHERING   %-62s reach %d   b380 scored %s'
            % (f, r['evidence']['reach'], r['structural_a']))
    rec('    ### ### **THE ORDER`S TWO FACTS, BOTH READ OFF THIS TABLE:** ### the threshold was `2`')
    rec('    ### and every synthesis declarer cleared it, so ### **NO VALUE OF THE THRESHOLD WOULD')
    rec('    ### ### HAVE FAILED THEM**; and both gathering declarers cleared it too, so ### **THE')
    rec('    ### ### ONE SIDE THAT COULD HAVE INFORMED THE PREDICATE DISAGREED WITH IT.**')
    rec('    ### ### ### **THAT IS ONE FINDING, NOT TWO**, and Component 1 measures it before it')
    rec('    ### rebuilds anything.')

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
    pth = run_clock.write(D, 'b381_extract_notes', LINES)
    io.open(d('b381_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, prior_synthesis=syn, prior_gathering=gat,
                        built=out, run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
