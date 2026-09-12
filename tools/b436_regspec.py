# -*- coding: utf-8 -*-
"""b436_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b436_registration_2026-09-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b436_satisfiable.json')

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
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### section (Z).'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('channels opened', 0, 0, 'channels', '### section (Z).'),
    ('candidate zeros, seeds or arrangements constructed', 0, 0, 'candidates', '### section (Z).'),
    ('fits, samples or likelihoods computed', 0, 0, 'computations', '### section (Z).'),
    ('claims about RH, h2 or zeta', 0, 0, 'claims', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z).'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('b435 arms re-verdicted', 0, 0, 'arms', '### reading (1): (R47) says they were right; this act neither re-scores nor appeals them.'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### section (Z).'),
    ('register rows edited', 0, 0, 'rows', '### section (Z).'),
    ('lane verdicts changed by the seat', 0, 0, 'verdicts', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### section (Z).'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 11.'),
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
    ('pre-push guard runs at step zero', 0, 0, 'runs', '### section (A): DEFERRED TO THE CLOSE, AND SINCE b435 ITS REPORT NAMES THE STATE.'),
    ('readings of the order declared in advance on this face', 8, 8, 'readings', '### section (A): (0) to (7).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): the extract reports 0 over 22 reads.'),
    ('orientation citations read by address rather than by marker', 0, 0, 'citations', '### section (A).'),
    ('searches or fetches before the lock', 0, 0, 'reads', '### section (A): the corpus only.'),

    ('author rulings ratified by this paste', 1, 1, 'rulings', '### reading (1): (R47), quoted from the banked paste.'),
    ('rulings extended beyond their own words', 0, 0, 'rulings', '### reading (1).'),
    ('lanes opened', 0, 0, 'lanes', '### section (Z): BOTH PARKED; b435`s guard-layer exception closed at b435`s end.'),
    ('instruments written or edited', 0, 0, 'files', '### section (Z): this act writes no instrument and reads only.'),

    ('site cells quoted verbatim before any candidate', 1, 1, 'cells', '### reading (2).'),
    ('grounds quoted at their own lines for the located candidate', 3, 3, 'grounds', '### reading (2): b401`s three.'),
    ('prior searches repeated rather than built on', 0, 0, 'searches', '### reading (2).'),
    ('the object the enumeration tests, declared before the first candidate', 1, 1, 'declarations', '### section (A): A UNIFORM BOUND, not a shared witness.'),
    ('candidates tested as shared witnesses at this site', 0, 0, 'candidates', '### (K) BAR 1: the form does not transpose here.'),

    ('opening-population members', 7, 7, 'candidates', '### reading (3): the order`s seven.'),
    ('candidates dismissed without a quoted step', 0, 0, 'candidates', '### (K) BAR 2.'),
    ('candidates read at a source other than their own', 0, 0, 'candidates', '### (K) BAR 2.'),
    ('extension caps left unstated', 0, 0, 'caps', '### reading (3).'),
    ('further hits admitted without a printed reason', 0, 0, 'hits', '### reading (3).'),
    ('candidates adopted on the navigator`s word', 0, 0, 'candidates', '### (K) BAR 3.'),
    ('paraphrases deciding over their source', 0, 0, 'paraphrases', '### (K) BAR 3.'),
    ('witnesses held at this site', 1, 0, 'witnesses', '### section (J), (N1): AT MOST ONE, AND THE NUMBER IS MEASURED.'),

    ('comparisons run in a normalization other than the emitting act`s', 0, 0, 'comparisons', '### (K) BAR 4.'),
    ('normalizations quoted from their emitting acts', 3, 3, 'quotations', '### (K) BAR 4: the half-line form, the identity, the bump`s constant.'),
    ('figures computed here and presented as banked', 0, 0, 'figures', '### (K) BAR 5.'),
    ('radii spoken about beyond the ten the record printed', 0, 0, 'radii', '### (K) BAR 5 and BAR 8.'),
    ('extrapolations past the record`s window', 0, 0, 'extrapolations', '### (K) BAR 8: A TREND IS NOT A CROSSING.'),
    ('wrong-way findings softened into near misses', 0, 0, 'findings', '### (K) BAR 6.'),

    ('sites of the witness arc attempted', 1, 1, 'sites', '### reading (3): site (iv), and only it.'),
    ('sites of the witness arc attempted beyond this one', 0, 0, 'sites', '### section (Z): (v) and (vi) are not attempted.'),
    ('earlier sites read for the boundary count', 3, 3, 'sites', '### reading (6): b424, b427, b428.'),
    ('kinds or tallies typed by the seat rather than read from JSON', 0, 0, 'figures', '### (K) BAR 9.'),

    ('cells written to FACES_LEDGER.md', 1, 0, 'cells', '### (K) BAR 10: ONLY IF A CANDIDATE HOLDS, AND THE NUMBER IS MEASURED.'),
    ('cells written by anything but b327_faces_row.py', 0, 0, 'cells', '### (K) BAR 10.'),
    ('seventh sites entered', 0, 0, 'sites', '### (K) BAR 10: the register is FROZEN AT SIX.'),
    ('bridges typed between any two of the six sites', 0, 0, 'bridges', '### section (Z).'),
    ('row-law sentences edited rather than quoted', 0, 0, 'sentences', '### (K) BAR 10.'),

    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms scanning source without stripping comments', 0, 0, 'arms', '### (K) BAR 11.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms matching a banked table without normalising line endings', 0, 0, 'arms', '### (K) BAR 11: the survey lost a ten-row table to a CRLF bank on its first run.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('act numbers matched unbounded inside a git SHA', 0, 0, 'arms', '### (K) BAR 11.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 11.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### (K) BAR 12.'),

    ('new `relay` act-tool files named on this face', 6, 6, 'files', '### (W): extract, regspec, reg_gate, components, checks, desk_bank.'),
    ('further `relay` act tools under the (R47) generator', 2, 0, 'files', '### (W): the generator is this act`s component step, THE BOUND IS 2, and the closing prints the actual list against it.'),
    ('write-list entries naming a class rather than a path or a generator', 0, 0, 'entries', '### (W) and (R47).'),
    ('existing `relay` tools edited in place', 1, 1, 'tools', '### (W): banked_index.py, which the key step writes.'),
    ('corpus documents written other than by append', 0, 0, 'documents', '### (W): OPEN_TRAILS and CORRESPONDENCE, APPENDED ONLY.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('TECHNE commits', 0, 0, 'commits', '### section (W).'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),
    ('ad-hoc shell-typed numbers in the bank', 0, 0, 'count', 'RULING (3).'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b436_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b436_registration_2026-09-12.txt -- b436, "
                             "THE WITNESS ARC AT SITE (iv), THE WINDOW"),
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
