# -*- coding: utf-8 -*-
"""b530_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE CARRIED FROM b529's SPEC WAS RE-READ AGAINST THIS FACE** (b456's error): the kernel
### ### clauses count the three NEW kernel files; the grades clause counts rest_bound alone; HMax takes none.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b530_registration_2026-09-25.txt')
SPEC = os.path.join(ROOT, 'data', 'b530_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### (Z).'),
    ('.lean files written or edited in any repository', 3, 3, 'files', '### (W): DecayBound.lean, RestBound.lean and AxiomCheckRest.lean in the kernel, all NEW.'),
    ('kernel builds', 0, 0, 'builds', '### (Z): no `lake build`; `lake env lean` on one module.'),
    ('chains run, or channel values computed', 1, 1, 'runs', '### READING (7): b530_values.py evaluates k-hat at every banked zero below 150 for the measured rest; no chain run.'),
    ('lanes opened', 1, 1, 'lanes', '### (R140)(3): the kernel lane for this act alone.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): (R51) stands.'),
    ('network remotes contacted', 0, 0, 'remotes', '### (Z): the pins` ls-remote reads and the ritual`s pushes excepted.'),
    ('scratch trees left', 0, 0, 'trees', '### (Z).'),
    ('branches merged or fetched', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('detached checkouts made', 0, 0, 'checkouts', '### section (Z).'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### (Z).'),
    ('grades conferred on rest_bound, by statement-read', 1, 1, 'grades', '### READING (8): DERIVES under H-STRIP and H-COUNT; the corollaries and HMax take none.'),
    ('grades moved on any other row of the corpus, or grade names minted', 0, 0, 'grades', '### section (Z) and READING (8): no grade name minted.'),
    ('kernel tags made', 0, 0, 'tags', '### section (Z).'),
    ('vendored modules edited', 0, 0, 'modules', '### READING (2).'),
    ('props stated and proved', 0, 0, 'props', '### READING (5): HMax is stated, not proved; f4_needs is proved FALSE below 1/2, not stated as proved.'),
    ('work-orders filed', 0, 0, 'work-orders', '### section (Z): (A) and (B) are priced, nothing filed.'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('routes proposed', 0, 0, 'routes', '### section (Z).'),
    ('claims about RH, h2 or any zero beyond quoting a verified source', 0, 0, 'claims', '### section (A): a compiled bound on a sum over zeros is not a claim about RH or any real part.'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### (W).'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### (W).'),
    ('state terms changed on any line', 0, 0, 'terms', '### section (Z).'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### section (Z).'),
    ('registry rows written or edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('mirror zips removed or rewritten', 0, 0, 'zips', '### (W).'),
    ('mirror zips written outside a repository', 1, 1, 'zips', '### (W): mirror-refresh-*-b530.zip, under (R69).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core writes', 0, 0, 'writes', '### (W): nothing.'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### section (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('measurements taken before the lock and not declared', 0, 0, 'measurements', '### section (C).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R140).'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b530_addendum.txt, under the stem glob.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (R50).'),
    ('PLACE-papers documents written other than by appending', 0, 0, 'documents', '### section (Z).'),
    ('PLACE-papers documents written at all', 1, 1, 'documents', '### (W): OPEN_TRAILS.md, ONE appended record.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` act-tool files named on this face', 7, 7, 'files', '### (W): the stem glob (R91) permits.'),
    ('existing `relay` tools edited in place', 0, 0, 'tools', '### (W): NONE.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b530_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        ext = io.open(os.path.join(ROOT, 'data', 'b530_extract.txt'),
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
    spec = {"registration": ("data/b530_registration_2026-09-25.txt -- b530, "
                             "f3, THE OTHER ZEROS BOUNDED ABOVE, WITH ITS LIMIT PRINTED"),
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
