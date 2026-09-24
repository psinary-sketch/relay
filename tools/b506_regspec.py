# -*- coding: utf-8 -*-
"""b506_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b506_registration_2026-09-23.txt')
SPEC = os.path.join(ROOT, 'data', 'b506_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### (Z): this seat calls no platform; the cache host is not a platform of record, and is counted under network remotes.'),
    ('.lean files written or edited in any repository', 0, 0, 'files', '### (W): the probe `b506_printaxioms.lean` is written by the launched process into relay`s data directory, which is not a repository of Lean, and is not committed; no `.lean` file of any kernel is written.'),
    ('kernel builds', 0, 0, 'builds', '### (Z): none; the build read is b498`s and is over.'),
    ('chains run, or channel values computed', 2, 2, 'runs', '### (B)(2)-(3): the argument-principle count, and the derived kernel on the completed bank (refusing unless the bank closes); Component 1 is carried, not re-run.'),
    ('lean runs', 0, 0, 'runs', '### (Z): none.'),
    ('repositories cloned', 0, 0, 'repositories', '### (Z): the kernel`s packages are already on disk under `.lake/packages`.'),
    ('lanes opened', 1, 1, 'lanes', '### (R116)(3): the numerical lane reopens for this act alone and shuts at its close.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): (R51) stands.'),
    ('network remotes contacted', 0, 0, 'remotes', '### (Z): none; the pins` ls-remote reads and the ritual`s pushes excepted.'),
    ('scratch trees left', 0, 0, 'trees', '### section (Z): none made.'),
    ('branches merged or fetched', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('detached checkouts made', 0, 0, 'checkouts', '### section (Z).'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### (Z): none.'),
    ('grades moved on any row, or grade names minted', 0, 0, 'grades', '### section (Z).'),
    ('relations graded and recorded in this act`s record and the trail', 0, 0, 'relations', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('candidate zeros, seeds, families or arrangements constructed', 0, 0, 'candidates', '### (Z): no new cells; the 93 are b503`s. The zeros of Z_Q0 located in (B)(2) are located, not constructed.'),
    ('claims about RH, h2 or any zero beyond quoting a verified source', 0, 0, 'claims', '### section (Z): the located zeros are zeros of Z_Q0, each confirmed by route A; no zero of zeta is touched.'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 4, 4, 'files', '### (W) and (R115)(1)-(2): one APPENDED note each to b477_components.txt, b502_components.txt, b504_components.txt and b502_ferry.txt, prefix proved; nothing else.'),
    ('banked ferries edited', 1, 1, 'files', '### (R115)(2): b502_ferry.txt, ONE appended note, its prefix proved; the banked text is untouched.'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### (W): ERRATA.md and REGISTRY.md are LEDGERS, not keystones; no keystone is touched.'),
    ('state terms changed on any line', 0, 0, 'terms', '### section (Z): every corpus write is an APPEND or an ANNOTATION with the prior text preserved verbatim; no state word is overwritten.'),
    ('dispositions taken beyond those ruled', 0, 0, 'dispositions', '### (R65)-(R69).'),
    ('dispositions recommended', 0, 0, 'dispositions', '### section (Z).'),
    ('exit codes used as a verdict', 0, 0, 'verdicts', '### section (Z).'),
    ('waves opened', 0, 0, 'waves', '### (R66), section (Z).'),
    ('sentences graded by the gate', 0, 0, 'sentences', '### (Z).'),
    ('ERRATA entries written', 0, 0, 'entries', '### (W) and (Z): ERRATA.md is not written by this act at all -- (R109)(1) says nothing is filed before the fetch-back.'),
    ('live surfaces narrowed', 0, 0, 'surfaces', '### section (Z).'),
    ('live notes inserted', 0, 0, 'notes', '### section (Z): README is not written.'),
    ('registry rows written or edited', 0, 0, 'rows', '### section (Z).'),
    ('ledger rows of FACES_LEDGER written or edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('seventh sites entered', 0, 0, 'sites', '### section (Z): the freeze at six stands.'),
    ('bridges typed between any two of the six sites', 0, 0, 'bridges', '### section (Z).'),
    ('mirror zips removed or rewritten', 0, 0, 'zips', '### (W): this act`s zip carries its own act suffix and collides with none.'),
    ('mirror zips written outside a repository', 1, 1, 'zips', '### (W): mirror-refresh-*-b506.zip, under (R69).'),
    ('sites of the witness arc reopened or attempted', 0, 0, 'sites', '### section (Z).'),
    ('lane verdicts changed by the seat', 0, 0, 'verdicts', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### section (Z).'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### section (Z).'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where their clauses differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('counts or values the seat predicts on this face', 0, 0, 'predictions', '### section (E): the seat`s expectations name comparisons, not artifact counts.'),
    ('statements imported', 0, 0, 'statements', '### (Z): tools are imported; no statement is.'),
    ('TECHNE-Core writes', 0, 0, 'writes', '### (W): nothing.'),
    ('work-orders filed', 0, 0, 'work-orders', '### section (Z).'),
    ('work-orders repaired', 0, 0, 'work-orders', '### section (Z).'),
    ('instrument files edited', 0, 0, 'files', '### (Z).'),
    ('new instruments built', 0, 0, 'instruments', '### (B)(2): b505`s count, copied under this stem with the fixture restated under (R116)(2); nothing new.'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### section (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL, banked under (R96).'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('act numbers claimed by an unclosed ferry other than its own', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A): 0 at step zero, on the first run, with no retry needed.'),
    ('repositories ahead of origin at step zero', 0, 0, 'repositories', '### section (A): nothing pushed because nothing was ahead.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A). ### ### **MEASURED OFF THE FACE, NOT TYPED** -- b488 routed that this spec`s clauses are typed and so cannot be falsified by the face they are emitted from.'),
    ('pre-face reads declared', 'PREFACE', 'PREFACE', 'reads', '### the survey`s (P1)..(Pn), MEASURED off `b506_extract.txt`.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): 0.'),
    ('measurements taken before the lock and not declared', 0, 0, 'measurements', '### section (C): every read made before the seal is declared there; NO CHAIN WAS RUN BEFORE THE SEAL.'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R116) -- b505 closed as registered; the fixture bar in the object`s units; the lane for b506.'),
    ('author rulings recorded as entries by this act', 0, 0, 'rulings', '### (Z): (R116) is ratified in the ferry and entered by the trail record.'),
    ('indices assigned that a site`s entry does not name', 0, 0, 'indices', '### section (Z).'),
    ('ranges typed rather than read off a source', 0, 0, 'ranges', '### section (Z).'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b506_addendum.txt, under the stem glob (R91) permits.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (R50).'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (N) and (S), MEASURED off the face: the navigator`s three and the seat`s three.'),
    ('expectations scored on a population other than the one named', 0, 0, 'expectations', '### sections (N) and (S): each names the printed result that scores it.'),
    ('prose passages of the corpus rewritten', 0, 0, 'passages', '### section (Z): appends and annotations only; no passage is rewritten.'),
    ('species summed', 0, 0, 'sums', '### section (Z).'),
    ('loom blocks appended', 0, 0, 'blocks', '### section (Z).'),
    ('PLACE-papers documents written other than by appending', 0, 0, 'documents', '### section (Z): every write in every file is an APPEND.'),
    ('PLACE-papers documents written at all', 1, 1, 'documents', '### (W): OPEN_TRAILS.md, ONE appended record.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('items proposed', 0, 0, 'proposals', '### section (Z).'),
    ('open items closed, restated or shelved beyond what the rulings dispose', 0, 0, 'items', '### section (Z).'),
    ('chain files edited', 0, 0, 'files', '### section (Z).'),
    ('new cells or radii', 0, 0, 'cells', '### section (Z).'),
    ('verdicts forced into a named outcome', 0, 0, 'verdicts', '### section (Z).'),
    ('banked figures re-verdicted', 0, 0, 'figures', '### section (Z).'),
    ('yields withheld because they do not help an expectation', 0, 0, 'yields', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z): no line of any written file before the write is absent from it after, and the raw counts are printed beside that claim.'),
    ('prefix proofs omitted', 0, 0, 'proofs', '### section (Z): before and after, byte for byte.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### ### **MEASURED: this face declares no numbered (K) bars and its constraints are in (Z).** ### Its constraints are in section (Z) THE NOTHINGS, which is not a (K) block. ### THE CLAUSE WAS CARRIED FROM b487 READING 8/8 AND CONTRADICTED THIS ACT`S OWN SEALED FACE, WHICH HAS NO (K) SECTION AT ALL. ### Repaired; both runs banked.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### section (Z): A2.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### section (Z).'),
    ('new `relay` act-tool files named on this face', 8, 8, 'files', '### (W): the stem glob (R91) permits, so the bound is on the STEM.'),
    ('further `relay` act tools under the (R47) generator', 2, 0, 'files', '### (W): THE BOUND IS 2.'),
    ('write-list entries naming a class rather than a path or a generator', 0, 0, 'entries', '### (W) and (R47).'),
    ('existing `relay` tools edited in place', 0, 0, 'tools', '### (W): NONE. `terminal_table.py` and `corr_row.py` are CARRIED and UNEDITED.'),
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
    print('b506_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    # ### ### **THE FACE-DERIVED CLAUSES ARE MEASURED, NOT TYPED (b488's routed finding).**
    # ### b488 found two carried clauses contradicting its own SEALED face -- one capping tool
    # ### edits at zero while the face named one, one declaring eight bars where the face had no
    # ### (K) section at all -- and nothing caught them, because the demands are TYPED. ###
    # ### **A CLAUSE THAT CANNOT BE FALSIFIED BY ITS OWN FACE IS NOT A BOUND.** ### Every clause
    # ### whose subject IS the face is now read off the face.
    ext = ''
    try:
        ext = io.open(os.path.join(ROOT, 'data', 'b506_extract.txt'),
                      encoding='utf-8', errors='replace').read()
    except Exception:
        pass
    measured = dict(
        ARMS=count_arms(text),
        # ### DISTINCT readings DECLARED, not every mention: a reading referred to from a
        # ### later paragraph is the same reading, and counting mentions inflated it to 10.
        READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
        EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)),
        BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
        PREFACE=len(re.findall(r'^\(P(\d+)\)', ext, re.M)),
    )
    print()
    print('  ### ### **MEASURED OFF THE FACE, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'PREFACE'):
        print('      %-9s %d' % (k, measured[k]))

    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b506_registration_2026-09-23.txt -- b506, "
                             "b505 RE-ISSUED FROM ITS COMPONENT 2"),
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
