# -*- coding: utf-8 -*-
"""b435_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b435_registration_2026-09-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b435_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### section (Z): the ls-remote reads are the pins`, the pushes the ritual`s.'),
    ('kernel .lean files touched', 0, 0, 'files', '### section (Z).'),
    ('kernel builds', 0, 0, 'builds', '### section (Z).'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('channels opened', 0, 0, 'channels', '### section (Z).'),
    ('rows of `FACES_LEDGER.md` written or rewritten', 0, 0, 'rows', '### section (Z).'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### section (Z).'),
    ('sites of the witness arc attempted', 0, 0, 'sites', '### section (Z): checkpointed after (iii).'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),
    ('fits, samples or likelihoods computed', 0, 0, 'computations', '### section (Z).'),
    ('candidate zeros, seeds or arrangements constructed', 0, 0, 'candidates', '### section (Z).'),
    ('claims about RH, h2 or zeta', 0, 0, 'claims', '### section (Z).'),
    ('claims that a counterexample exists or is findable', 0, 0, 'claims', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('author rulings ratified by this paste', 1, 1, 'rulings', '### reading (1): (R46), quoted from the banked paste.'),
    ('rulings extended beyond their own words', 0, 0, 'rulings', '### reading (1); ### (K) BAR 8.'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z).'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### section (Z).'),
    ('register rows or ledger rows edited', 0, 0, 'rows', '### section (Z).'),
    ('lane verdicts changed by the seat', 0, 0, 'verdicts', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### section (Z).'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 12.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where their clauses differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('counts the seat predicts on this face', 0, 0, 'predictions', '### section (J): C10.'),

    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('pre-push guard runs at step zero', 0, 0, 'runs', '### section (A): DEFERRED TO THE CLOSE, AND THE REASON IS THIS ACT`S SUBJECT.'),
    ('readings of the order declared in advance on this face', 8, 8, 'readings', '### section (A): (0) to (7).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): the extract reports 0.'),
    ('survey run records read without proof of their own run', 0, 0, 'records', '### (K) BAR 11.'),
    ('orientation citations read by address rather than by marker', 0, 0, 'citations', '### section (A).'),
    ('searches or fetches before the lock', 0, 0, 'reads', '### section (A): the corpus only.'),

    ('lanes opened', 1, 1, 'lanes', '### section (A) and (K) BAR 9: THE INSTRUMENT LANE, FOR THE GUARD LAYER ONLY.'),
    ('lanes left open at this act`s end', 0, 0, 'lanes', '### (K) BAR 9: IT CLOSES AT THIS ACT`S END.'),
    ('research instruments touched', 0, 0, 'files', '### section (Z): NOT ONE FILE OF THE LI, FAMILY, WITNESS OR FALSIFIER MACHINERY.'),
    ('instruments touched outside the guard layer', 0, 0, 'files', '### (K) BAR 9.'),

    ('handlers quoted at their own file and line', 1, 1, 'handlers', '### reading (2): b314`s.'),
    ('shared guard tools written', 1, 1, 'tools', '### reading (2): the extraction (R46) orders.'),
    ('fixture polarities the shared tool is exercised in', 2, 2, 'polarities', '### reading (2) and (K) BAR 1.'),
    ('genuine failures the shared tool is allowed to swallow', 0, 0, 'failures', '### (K) BAR 1: IT MUST STILL FAIL LOUDLY.'),
    ('call sites named', 10, 10, 'sites', '### reading (3): the ten the survey printed.'),
    ('call sites repointed', 10, 0, 'sites', '### reading (3): AT MOST TEN, AND THE NUMBER IS MEASURED, NOT TYPED.'),
    ('call sites left without a printed reason', 0, 0, 'sites', '### reading (3) and (K) BAR 3.'),
    ('site calls made by a mechanical rule dressed as a measurement', 0, 0, 'calls', '### reading (3): THE CALL IS THE SEAT`S AND IS SAID TO BE.'),
    ('guards folded into a total rather than named on their own rows', 0, 0, 'guards', '### reading (4) and (K) BAR 4.'),
    ('tools whose behaviour changes other than the silent skip', 0, 0, 'tools', '### (K) BAR 2.'),

    ('states the guard report distinguishes', 3, 3, 'states', '### reading (5): PASS, FAIL, SKIPPED.'),
    ('skips counted into a failure total', 0, 0, 'skips', '### (K) BAR 5.'),
    ('skips reported without their reason', 0, 0, 'skips', '### reading (5).'),
    ('sweep repairs longer than the same one line', 0, 0, 'repairs', '### (K) BAR 6.'),
    ('sweep findings counted but left, unstated', 0, 0, 'findings', '### (K) BAR 6: THE ACT PRINTS HOW MANY IT LEFT.'),

    ('census positive controls', 1, 1, 'controls', '### (K) BAR 7: it must find b314`s.'),
    ('counts stated from a census whose control did not find b314`s', 0, 0, 'counts', '### (K) BAR 7.'),
    ('repairs made on the strength of the census', 0, 0, 'repairs', '### (K) BAR 8.'),
    ('censuses run more than once', 0, 0, 'censuses', '### reading (6): ONCE.'),

    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 10.'),
    ('arms scanning source without stripping comments', 0, 0, 'arms', '### (K) BAR 10.'),
    ('arms stripping the string literals their own evidence lives in', 0, 0, 'arms', '### (K) BAR 10: STRINGS ARE KEPT AND THE TOOL SAYS SO.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 10.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 10: A2.'),
    ('act numbers matched unbounded inside a git SHA', 0, 0, 'arms', '### (K) BAR 10.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 10.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### (K) BAR 12.'),

    ('new `relay` act-tool files', 6, 6, 'files', '### (W): extract, regspec, reg_gate, components, checks, desk_bank.'),
    ('further `relay` act tools declared while running', 2, 0, 'files', '### (W): PERMITTED, PROVIDED THE SUITE PRINTS ITS NAME AND THE REASON.'),
    ('existing `relay` tools edited in place', 4, 1, 'tools', '### (W): banked_index.py certain; b304_hooks.py and the repointed sites measured.'),
    ('corpus documents written other than by append', 0, 0, 'documents', '### (W): OPEN_TRAILS and CORRESPONDENCE, APPENDED ONLY.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('TECHNE commits', 0, 0, 'commits', '### section (W).'),
    ('ad-hoc shell-typed numbers in the bank', 0, 0, 'count', 'RULING (3).'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b435_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    text = io.open(REG, encoding='utf-8').read()
    n, hits = CNT.count_predictions(text)
    print()
    print('  registration : %s' % os.path.basename(REG))
    print('  bytes/lines  : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print('  ### ARTIFACT-COUNT PREDICTIONS FOUND : %d' % n)
    for ln, txt in hits:
        print('      line %-4d  %s' % (ln, txt))
    measured = dict(ARMS=count_arms(text))
    print()
    print('  ### ### **THE OPEN CLAUSE, MEASURED RATHER THAN TYPED:** ### ARMS %d' % measured['ARMS'])
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b435_registration_2026-09-12.txt -- b435, "
                             "THE CURE SHARED, AND THE SKIPS THAT PRINT LIKE PASSES"),
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    print()
    print('  clauses emitted : %d' % len(clauses))
    nz = [c for c in clauses if c['demand']]
    print('  ### ### **CLAUSES WITH A NON-ZERO DEMAND : %d**' % len(nz))
    for c in nz:
        print('      %-62s demand %-4s cap %s' % (c['clause'][:62], c['demand'], c['cap']))
    print('  written : %s' % os.path.basename(SPEC))
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
