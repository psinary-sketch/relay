# -*- coding: utf-8 -*-
"""b440_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b440_registration_2026-09-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b440_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### section (Z): the ls-remote reads are the pins`, the pushes the ritual`s.'),
    ('existing SIDE-window .lean files edited', 0, 0, 'files', '### (K) BAR 8: the five named are not edited.'),
    ('new .lean files created in SIDE-window', 2, 0, 'files', '### (W): the enumerated conditional set; NEITHER OR BOTH, never one.'),
    ('kernel builds run inside SIDE-window', 2, 0, 'builds', '### (W): only if Component 2 builds.'),
    ('Lean probes run in the session scratchpad, outside every repository', 4, 1, 'probes', '### reading (2)(beta): AT LEAST ONE, and its output is quoted.'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### section (Z).'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened', 0, 0, 'routes', '### section (Z): Component 4 is PRICED and NOT OPENED.'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('candidate zeros, seeds, families or arrangements constructed', 0, 0, 'candidates', '### section (Z) and (K) BAR 9.'),
    ('claims about RH, h2, zeta or any zero', 0, 0, 'claims', '### section (Z).'),
    ('objects compiled for the window kernel', 2, 0, 'objects', '### reading (2): NEITHER OR BOTH, never one; this face expects 0.'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z): b438`s least of all.'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### section (Z).'),
    ('register rows or ledger rows edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of FACES_LEDGER.md written', 0, 0, 'cells', '### section (Z): frozen at six.'),
    ('seventh sites entered', 0, 0, 'sites', '### section (Z).'),
    ('bridges typed between any two of the six sites', 0, 0, 'bridges', '### section (Z).'),
    ('sites of the witness arc attempted', 0, 0, 'sites', '### section (Z): checkpointed after (iv).'),
    ('lane verdicts changed by the seat', 0, 0, 'verdicts', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### section (Z).'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 11.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where their clauses differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('counts or values the seat predicts on this face', 0, 0, 'predictions', '### section (J): C10; the shape in reading (1) is a derivation and is scored like any prediction.'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),

    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 5, 5, 'readings', '### section (A): (0) to (4).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): 0 over 18 reads, one needle re-aimed before the face and said so.'),
    ('measurements taken before the lock and not declared on this face', 0, 0, 'measurements', '### section (A): the h+ evaluation is declared and re-run after the lock.'),

    ('author rulings ratified by this paste and entered on this face', 2, 2, 'rulings', '### section (A): (R51) and (R52).'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b440_addendum.txt, present whether used or not.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (K) BAR 10.'),
    ('instrument lanes opened', 0, 0, 'lanes', '### section (Z): both remain PARKED.'),
    ('components the KERNEL lane is open to build for', 1, 1, 'components', '### section (A): Component 2 only.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): its trigger fired at (R48) and its disposition waits on the author.'),
    ('new instruments built', 0, 0, 'instruments', '### section (Z).'),
    ('instrument files edited', 0, 0, 'files', '### section (Z).'),
    ('new families defined', 0, 0, 'families', '### section (Z).'),

    ('clauses of Component 1 verdicted apart', 4, 4, 'clauses', '### reading (1), (R27): (a) root, (b) density, (c) asymptote, (d) digits.'),
    ('clauses averaged into one word for the set', 0, 0, 'clauses', '### (R27).'),
    ('corpus name-searches printed for the density', 4, 3, 'searches', '### reading (1): AT LEAST THREE, and the number run is measured.'),
    ('search hits hand-read at their own line', 12, 1, 'hits', '### (K) BAR 2: AT LEAST ONE, and the number read is measured.'),
    ('sites called an IDENTIFICATION on the strength of carrying the form', 0, 0, 'sites', '### (K) BAR 2.'),
    ('u0 digit strings printed where the two disagree', 2, 0, 'values', '### (K) BAR 4: BOTH or neither.'),
    ('working precisions left unstated beside a twenty-digit value', 0, 0, 'values', '### (K) BAR 4.'),
    ('mechanism sentences stated on a failed premise', 0, 0, 'sentences', '### (K) BAR 1.'),
    ('families the mechanism sentence is tested against', 2, 2, 'families', '### reading (1): the aimed seed and the second family.'),
    ('statuses of u0 kept apart', 3, 3, 'statuses', '### (K) BAR 3: DEFINING EQUATION / CLASSICAL ASYMPTOTE / CLOSED FORM.'),
    ('precise numbers offered as an identification', 0, 0, 'claims', '### (K) BAR 3.'),

    ('cross-multiplied integer forms written out for the maximizer comparison', 1, 1, 'derivations', '### reading (2)(alpha).'),
    ('steps at which an irrational survives, exhibited', 1, 1, 'steps', '### (K) BAR 5.'),
    ('impossibilities asserted without a demonstration', 0, 0, 'claims', '### (K) BAR 5.'),
    ('probe outputs quoted including their failure text', 1, 1, 'quotations', '### reading (2)(beta).'),
    ('infrastructure failures converted into mathematical verdicts', 0, 0, 'verdicts', '### (K) BAR 6.'),
    ('Ladder.lean precedents quoted before the surrogate is adjudicated', 1, 1, 'quotations', '### reading (2)(gamma).'),
    ('facts built alone where the order says build neither', 0, 0, 'facts', '### (K) BAR 7.'),
    ('choices taken here that the act says it routes back', 0, 0, 'choices', '### (K) BAR 7.'),
    ('SIDE-window files written where nothing is built there', 0, 0, 'files', '### (K) BAR 8.'),
    ('write-list entries naming the SIDE-window set as a class', 0, 0, 'entries', '### (W), (R47): the set is enumerated.'),

    ('dictionary rows quoted from the source for Component 3', 2, 2, 'rows', '### reading (3): the P row and the A row.'),
    ('offered findings stated on a failed premise', 0, 0, 'findings', '### (K) BAR 1.'),
    ('b439 spread values re-opened', 0, 0, 'values', '### (K) BAR 9: the banked number stands; only its attribution is at stake.'),
    ('measurements and their attributions conflated', 0, 0, 'pairs', '### (K) BAR 9.'),

    ('expectations of this seat own declared on this face', 2, 2, 'expectations', '### section (J): reading (2) and reading (3).'),
    ('expectations of this seat exempt from scoring', 0, 0, 'expectations', '### (K) BAR 12.'),

    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms scanning source without stripping comments', 0, 0, 'arms', '### (K) BAR 11.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms matching a banked table without normalising line endings', 0, 0, 'arms', '### (K) BAR 11.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('format strings printed without their arguments', 0, 0, 'lines', '### (K) BAR 11.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 11.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### (K) BAR 12.'),

    ('new `relay` act-tool files named on this face', 6, 6, 'files', '### (W).'),
    ('further `relay` act tools under the (R47) generator', 2, 0, 'files', '### (W): THE BOUND IS 2.'),
    ('write-list entries naming a class rather than a path or a generator', 0, 0, 'entries', '### (W) and (R47).'),
    ('existing `relay` tools edited in place', 1, 1, 'tools', '### (W): banked_index.py.'),
    ('corpus documents written other than by append', 0, 0, 'documents', '### (W).'),
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
    print('b440_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b440_registration_2026-09-12.txt -- b440, "
                             "THE FIXED POINT NAMED, THE BREAK ATTRIBUTED, AND TWO FACTS BUILT"),
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
