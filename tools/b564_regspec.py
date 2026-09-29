# -*- coding: utf-8 -*-
"""b564_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE CARRIED FROM b563's SPEC WAS RE-READ AGAINST THIS FACE** (b456's error): kernel work on one
### ### branch, new files only; main by fast-forward; one tag at most; appends only; NO relay tool edited; web reads declared.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b564_registration_2026-09-29.txt')
SPEC = os.path.join(ROOT, 'data', 'b564_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### (Z): nothing at Zenodo is written or read.'),
    ('platform calls of any kind', 0, 0, 'calls', '### (Z): nothing at Zenodo is read or written.'),
    ('.lean files reaching a main other than by fast-forward onto a clean branch', 0, 0, 'files', '### (Z) and (W).'),
    ('new .lean files written on the branch', 12, 3, 'files', '### READING (6): Chi/ZeroConfig, Chi/Generic, one per attempted frontier module, AxiomCheckChi; new files only.'),
    ('existing .lean files touched on main', 0, 0, 'files', '### (Z): no existing .lean file is edited.'),
    ('code lines changed in any existing .lean file', 0, 0, 'lines', '### (Z): no existing .lean file is edited.'),
    ('Zeta23 files edited or added', 0, 0, 'files', '### (A) and (Z).'),
    ('tags pushed before main reads back', 0, 0, 'tags', '### (R171)(2) and (Z).'),
    ('kernel builds by lake build', 0, 0, 'builds', '### (Z): elaboration by `lake env lean` only.'),
    ('elaboration attempts per part', 4, 1, 'attempts', '### READING (6): at most four per part.'),
    ('numerical computations over any zeros', 0, 0, 'computations', '### (Z): no numerical lane.'),
    ('web searches run for prior art', 40, 1, 'searches', '### READING (3): GitHub, arXiv, the Zulip archive, each printed with its query.'),
    ('lanes opened', 1, 1, 'lanes', '### (A): a kernel lane on branches.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): (R51) stands.'),
    ('git network remotes fetched from', 0, 0, 'remotes', '### (Z): no fetch; the pins, the ritual`s pushes, the branch and tag pushes and the ls-remote read-backs excepted.'),
    ('scratch trees left', 0, 0, 'trees', '### (Z): no worktree made.'),
    ('fast-forward merges onto the kernel`s main', 1, 0, 'merges', '### READING (6): only on the gate and the standard three.'),
    ('kernel branches pushed by name', 1, 1, 'branches', '### READING (7): grh-weil-b564.'),
    ('detached checkouts made', 0, 0, 'checkouts', '### (Z): branches are checked out by name and main restored.'),
    ('public pages fetched', 40, 0, 'reads', '### READING (3): a URL read only when its title or snippet names a formalization.'),
    ('grades conferred by statement-read on this act`s compiled declarations', 400, 1, 'grades', '### READING (7): the three-grade vocabulary.'),
    ('grade sources removed by the trail-line supersession form', 1, 1, 'sources', '### READING (2): OPEN_TRAILS :11577 for li_identity_of_exchange.'),
    ('grade names minted', 0, 0, 'grades', '### (Z).'),
    ('kernel tags made', 1, 0, 'tags', '### READING (7): v0.8 only on the gate, pushed only after main reads back.'),
    ('vendored modules edited', 0, 0, 'modules', '### (Z).'),
    ('sorry-bodied declarations reaching a main', 0, 0, 'declarations', '### (Z): no sorry reaches any main.'),
    ('work-orders filed', 0, 0, 'work-orders', '### (Z): lines appended to filed entries only.'),
    ('stubbed declarations written', 0, 0, 'declarations', '### READING (6)(c): nothing is stubbed.'),
    ('converse attempts', 0, 0, 'attempts', '### READING (4) and (Z): nothing is attempted.'),
    ('claims about RH, h2 or any zero beyond quoting a verified source or a compiled statement', 0, 0, 'claims', '### section (A).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z): no prior bank is rewritten.'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### (Z): no keystone byte.'),
    ('state terms changed on any line', 0, 0, 'terms', '### section (Z).'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z): no erratum.'),
    ('registry rows written or edited', 0, 0, 'rows', '### section (Z).'),
    ('correspondence rows written', 1, 1, 'rows', '### READING (9): the act`s row.'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('mirror zips removed or rewritten', 0, 0, 'zips', '### (Z).'),
    ('mirror zips written outside a repository', 0, 0, 'zips', '### (Z): no mirror zip is built.'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core writes', 0, 0, 'writes', '### (W): nothing.'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### (W): SPIRAL_MAP is not written.'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('measurements taken before the lock and not declared', 0, 0, 'measurements', '### section (C).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R174).'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b564_addendum.txt, under the stem glob relay/data/b564_*.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (R50).'),
    ('PLACE-papers documents written other than by appending', 0, 0, 'documents', '### (W): every write is an append.'),
    ('PLACE-papers documents written at all', 4, 4, 'documents', '### (W): FINDINGS, OPEN_TRAILS, README and REGISTRY, by appending.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` act-tool files named on this face', 7, 7, 'files', '### (W): the stem glob (R91) permits.'),
    ('existing `relay` tools edited in place', 0, 0, 'tools', '### (Z): no existing relay tool is edited.'),
    ('new standing `relay` tools', 0, 0, 'tools', '### (Z).'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b564_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        ext = io.open(os.path.join(ROOT, 'data', 'b564_extract.txt'),
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
    spec = {"registration": ("data/b564_registration_2026-09-29.txt -- b564, LANE TWO ACT SIX, GRH-WEIL ACT TWO, UNDER (R174)"),
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
