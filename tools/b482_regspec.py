# -*- coding: utf-8 -*-
"""b482_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **BAR 6: EVERY CLAUSE CARRIED FROM b457's SPEC IS RE-READ AGAINST THIS FACE** -- b456's error,
### ### where a clause capping annotations at none was carried forward and contradicted the face it
### ### was meant to bound. ### The kernel-lane clauses of b457 are DROPPED here rather than kept at
### ### their old caps, because this act opens no lane and a clause about a run that cannot happen is
### ### not a bound, it is noise.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b482_registration_2026-09-22.txt')
SPEC = os.path.join(ROOT, 'data', 'b482_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### (K) BAR 1: THIS SEAT fetches nothing; the two manifests are the AUTHOR`S fetch under (R94) and were already on disk. The pins` ls-remote reads and the ritual`s pushes excepted.'),
    ('.lean files written or edited in any repository', 0, 0, 'files', '### section (Z).'),
    ('kernel builds', 0, 0, 'builds', '### (K) BAR 2: none; b475`s run is not this act`s and its log is not opened.'),
    ('chains run, or channel values computed', 0, 0, 'runs', '### (K) BAR 4: every number is a function of the banked entries; no chain is run.'),
    ('lean runs', 0, 0, 'runs', '### (K) BAR 2: none; b475`s detached run is another act`s and is not polled.'),
    ('repositories cloned', 0, 0, 'repositories', '### (K) BAR 1: the zeta23 clone is ALREADY on disk and is READ; nothing is fetched or cloned.'),
    ('lanes opened', 1, 1, 'lanes', '### section (B)(3): the KERNEL lane opens to READ STATEMENTS AT A PIN and CLOSES at the act`s end.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): (R51) stands.'),
    ('network remotes contacted', 0, 0, 'remotes', '### section (Z): the pins` ls-remote reads and the ritual`s pushes excepted.'),
    ('scratch trees left', 0, 0, 'trees', '### section (Z): none made.'),
    ('branches merged or fetched', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('detached checkouts made', 0, 0, 'checkouts', '### section (Z).'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### section (Z).'),
    ('grades moved on any row, or grade names minted', 0, 0, 'grades', '### section (Z).'),
    ('relations graded and recorded in this act`s record and the trail', 24, 24, 'relations', '### section (B)(3): six declarations against four named corpus statements, one verdict each.'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('candidate zeros, seeds, families or arrangements constructed', 0, 0, 'candidates', '### section (Z).'),
    ('claims about RH, h2 or any zero beyond quoting a verified source', 0, 0, 'claims', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z) and (K) BAR 3: b449`s trail record least of all.'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### (W): ERRATA.md and REGISTRY.md are LEDGERS, not keystones; no keystone is touched.'),
    ('state terms changed on any line', 0, 0, 'terms', '### (K) BAR 5: every corpus write is an APPEND or an ANNOTATION with the prior text preserved verbatim; no state word is overwritten.'),
    ('dispositions taken beyond those ruled', 0, 0, 'dispositions', '### (R65)-(R69).'),
    ('dispositions recommended', 0, 0, 'dispositions', '### section (Z).'),
    ('exit codes used as a verdict', 0, 0, 'verdicts', '### (K) BAR 7.'),
    ('waves opened', 0, 0, 'waves', '### (R66), section (Z).'),
    ('sentences graded by the gate', 0, 0, 'sentences', '### section (Z): the gate stays priced and unbuilt.'),
    ('ERRATA entries written', 0, 0, 'entries', '### section (Z).'),
    ('live surfaces narrowed', 0, 0, 'surfaces', '### section (Z).'),
    ('live notes inserted', 0, 0, 'notes', '### section (Z): README is not written.'),
    ('registry rows written or edited', 0, 0, 'rows', '### section (Z).'),
    ('ledger rows of FACES_LEDGER written or edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z) and (K) BAR 6.'),
    ('seventh sites entered', 0, 0, 'sites', '### (K) BAR 6: the freeze at six stands.'),
    ('bridges typed between any two of the six sites', 0, 0, 'bridges', '### (K) BAR 6.'),
    ('mirror zips removed or rewritten', 0, 0, 'zips', '### (W): this act`s zip carries its own act suffix and collides with none.'),
    ('mirror zips written outside a repository', 1, 1, 'zips', '### (W): mirror-refresh-*-b482.zip, under (R69).'),
    ('sites of the witness arc reopened or attempted', 0, 0, 'sites', '### section (Z).'),
    ('lane verdicts changed by the seat', 0, 0, 'verdicts', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### section (Z).'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 7.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where their clauses differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('counts or values the seat predicts on this face', 0, 0, 'predictions', '### section (J): C10.'),
    ('statements imported', 0, 0, 'statements', '### (K) BAR 1: the six are READ and PLACED; not one is imported, copied or vendored.'),
    ('TECHNE-Core writes', 0, 0, 'writes', '### (W): nothing.'),
    ('work-orders filed', 0, 0, 'work-orders', '### section (Z).'),
    ('work-orders repaired', 0, 0, 'work-orders', '### section (Z).'),
    ('instrument files edited', 0, 0, 'files', '### section (Z): not b321_window.py.'),
    ('new instruments built', 0, 0, 'instruments', '### section (Z).'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### section (Z).'),
    ('ferry parts received', 2, 2, 'parts', '### section (A): b482`s own banked ferry, and the amendment, part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('act numbers claimed by an unclosed ferry other than its own', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A): 0 of 4.'),
    ('repositories ahead of origin at step zero', 0, 0, 'repositories', '### section (A): nothing pushed because nothing was ahead.'),
    ('readings of the order declared in advance on this face', 7, 7, 'readings', '### section (A): (0) to (6).'),
    ('pre-face reads declared', 5, 5, 'reads', '### section (A): (P0) to (P4).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): 0.'),
    ('measurements taken before the lock and not declared', 0, 0, 'measurements', '### section (A): (P5) declares the one prior read of a ferry file.'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R95), banked and addressed to the act AFTER the fold; this act does not execute it.'),
    ('author rulings recorded as entries by this act', 0, 0, 'rulings', '### section (Z): b458 did that work.'),
    ('indices assigned that a site`s entry does not name', 0, 0, 'indices', '### (K) BAR 2.'),
    ('ranges typed rather than read off a source', 0, 0, 'ranges', '### (K) BAR 3.'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b482_addendum.txt, under the stem glob (R91) permits.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (R50).'),
    ('expectations registered', 3, 3, 'expectations', '### section (J): (N1), (N2), (N3) as b482`s own banked ferry registered them; the amendment says they stand.'),
    ('expectations scored on a population other than the one named', 0, 0, 'expectations', '### section (J): each of the six carries b476`s own population.'),
    ('prose passages of the corpus rewritten', 0, 0, 'passages', '### (K) BAR 5: appends and annotations only; no passage is rewritten.'),
    ('species summed', 0, 0, 'sums', '### section (Z).'),
    ('loom blocks appended', 0, 0, 'blocks', '### section (Z).'),
    ('PLACE-papers documents written other than by appending', 0, 0, 'documents', '### (W): OPEN_TRAILS.md only, appended.'),
    ('PLACE-papers documents written at all', 1, 1, 'documents', '### (W): OPEN_TRAILS.md, appended only.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('items proposed', 0, 0, 'proposals', '### section (Z).'),
    ('open items closed, restated or shelved beyond what the rulings dispose', 0, 0, 'items', '### section (Z).'),
    ('chain files edited', 0, 0, 'files', '### section (Z).'),
    ('new cells or radii', 0, 0, 'cells', '### section (B)(1): both families are read from their own banks.'),
    ('verdicts forced into a named outcome', 0, 0, 'verdicts', '### (K) BAR 5.'),
    ('banked figures re-verdicted', 0, 0, 'figures', '### section (Z).'),
    ('yields withheld because they do not help an expectation', 0, 0, 'yields', '### (K) BAR 5.'),
    ('lines removed from any document', 0, 0, 'lines', '### (K) BAR 5: no line of any written file before the write is absent from it after, and the raw counts are printed beside that claim.'),
    ('prefix proofs omitted', 0, 0, 'proofs', '### (K) BAR 4: before and after, byte for byte.'),
    ('bars declared', 8, 8, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 7: A2.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### (K) BAR 8.'),
    ('new `relay` act-tool files named on this face', 7, 7, 'files', '### (W): the stem glob (R91) permits, so the bound is on the STEM and not on a list of names.'),
    ('further `relay` act tools under the (R47) generator', 2, 0, 'files', '### (W): THE BOUND IS 2.'),
    ('write-list entries naming a class rather than a path or a generator', 0, 0, 'entries', '### (W) and (R47).'),
    ('existing `relay` tools edited in place', 0, 0, 'tools', '### (W): every tool this act runs is either carried unchanged or written under this act`s own stem.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('ad-hoc shell-typed numbers in the bank', 0, 0, 'count', 'RULING (3).'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b482_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b482_registration_2026-09-22.txt -- b482, "
                             "THE XiPrime TOPIC READ AGAINST THE CORPUS STATEMENTS"),
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
