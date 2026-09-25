# -*- coding: utf-8 -*-
"""b540_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE CARRIED FROM b539's SPEC WAS RE-READ AGAINST THIS FACE** (b456's error): no kernel file;
### ### one ERRATA entry filed with one bullet inserted; six PLACE-papers documents written.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b540_registration_2026-09-25.txt')
SPEC = os.path.join(ROOT, 'data', 'b540_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### (Z): nothing at Zenodo is written or read.'),
    ('platform calls of any kind', 0, 0, 'calls', '### (Z): no call to the deposit platform.'),
    ('.lean files written or edited in any repository', 0, 0, 'files', '### (Z): no kernel file.'),
    ('kernel builds', 0, 0, 'builds', '### (Z).'),
    ('chains run, or channel values computed', 0, 0, 'runs', '### (Z): no number computed.'),
    ('lanes opened', 0, 0, 'lanes', '### (Z): no kernel lane opens.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): (R51) stands.'),
    ('network remotes contacted', 0, 0, 'remotes', '### READING (4): no fetch; the pins, the ritual`s pushes and the ls-remote read-backs excepted.'),
    ('scratch trees left', 0, 0, 'trees', '### (Z).'),
    ('branches merged or fetched', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('detached checkouts made', 0, 0, 'checkouts', '### section (Z).'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### READING (4).'),
    ('grades conferred by statement-read on this act`s compiled model theorems', 0, 0, 'grades', '### (Z).'),
    ('grades moved on any other row of the corpus, or grade names minted', 0, 0, 'grades', '### section (Z) and READING (8): no grade name minted.'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('vendored modules edited', 0, 0, 'modules', '### READING (2).'),
    ('props stated and proved', 0, 0, 'props', '### (Z).'),
    ('work-orders filed', 0, 0, 'work-orders', '### (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('routes proposed', 0, 0, 'routes', '### section (Z).'),
    ('claims about RH, h2 or any zero beyond quoting a verified source', 0, 0, 'claims', '### section (A): a relation between two premises is not a claim about RH.'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### (W).'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### (W).'),
    ('state terms changed on any line', 0, 0, 'terms', '### section (Z).'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 1, 1, 'entries', '### READING (2): E-2026-09-25-3 filed as drafted.'),
    ('registry rows written or edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('mirror zips removed or rewritten', 0, 0, 'zips', '### (Z).'),
    ('mirror zips written outside a repository', 0, 0, 'zips', '### (Z): no mirror zip is built.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R150).'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b540_addendum.txt, under the stem glob.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (R50).'),
    ('PLACE-papers documents written other than by appending', 1, 1, 'documents', '### READING (2): ERRATA, one bullet inserted in the DEPOSIT-FACING list.'),
    ('PLACE-papers documents written at all', 6, 6, 'documents', '### (W): ERRATA, the map, SURR, PATHS, FINDINGS, OPEN_TRAILS.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` act-tool files named on this face', 5, 5, 'files', '### (W): the stem glob (R91) permits.'),
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
    print('b540_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        ext = io.open(os.path.join(ROOT, 'data', 'b540_extract.txt'),
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
    spec = {"registration": ("data/b540_registration_2026-09-25.txt -- b540, "
                             "THE CASCADE, ACT TWO, UNDER (R150)"),
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
