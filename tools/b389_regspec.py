# -*- coding: utf-8 -*-
"""b389_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any write of this act.
### ### **AND ONE CLAUSE OF THIS ACT IS A WITHDRAWAL OF `b388`'S OWN FINDING**, committed here in
### advance so the correction cannot be quietly folded into a different answer later.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b389_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b389_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (J): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (J)."),
    ("`.lean` files touched", 0, 0, "files", "### section (F)/(J)."),
    ("builds run", 0, 0, "builds", "### section (F)/(J)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (F)/(J)."),
    ("terminals written", 0, 0, "terminals", "### section (J)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    # ---- THE STANDING CLAUSE THIS ACT CARRIES ABOVE ALL OTHERS -----------------------------------
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes",
     "### section (F)/(J)/(H) BAR 8. ### **THE ORDER'S OWN CLAUSE, AND THE ONE THIS ACT IS MOST "
     "EXPOSED TO BECAUSE IT IS THE ACT THAT CALLS THE PLATFORM.**"),
    ("write paths to the platform in this act`s code", 0, 0, "paths",
     "### section (H) BAR 8: no POST, PUT, PATCH, DELETE, no `-X`, no `--data`, no token. "
     "### MECHANICAL, NOT ASSERTED."),
    ("credentials presented to any platform", 0, 0, "credentials", "### section (C)/(D)."),

    # ---- STEP ZERO AND THE DECLARED READINGS -----------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378`s gate run as b389, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(H)."),
    ("readings of the order declared in advance on this face", 6, 6, "readings",
     "### section (A): eight syntheses on disk against six in the registry and three in the map; "
     "zero of six Zenodo routes answering with the control at 200; no written deposit rule "
     "located by either half of the search; `SIDE-interface-split` absent with b388`s reading "
     "of it refuted; both maps preserving their superseded heads; and two corpus documents "
     "written into and no others."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims",
     "### section (A)/(C)/(H) BAR 3. ### `b378`'s price, and this act pays it twice."),
    ("extract reads left without an anchor", 0, 0, "reads",
     "### section (A): 30 reads, 0 without an anchor, 9 anchors differing from the typed hint."),

    # ---- COMPONENT 1: THE CLUSTER SYNTHESES ENUMERATED -------------------------------------------
    ("populations of cluster syntheses reported separately", 3, 3, "populations",
     "### section (B)/(H) BAR 2: disk, registry, map."),
    ("the three populations added into one figure", 0, 0, "figures",
     "### section (B)/(H) BAR 2. ### **A DIFFERENCE OF COUNTS IS NOT A DIFFERENCE OF MEMBERS**, "
     "and averaging three populations would destroy the only finding this component has."),
    ("syntheses whose date and self-described cluster are read from the file", "SYN", "SYN",
     "syntheses", "### section (B): every one on disk, by its own words and not by its name. "
     "### COUNTED OFF THE DISK BY THIS FILE, NOT TYPED."),
    ("clusters added to either map by this component", 0, 0, "clusters",
     "### section (B)/(E)/(J): the eight-versus-six finding is ROUTED, NOT ACTED ON."),

    # ---- COMPONENT 2: THE DEPOSITED LAYER --------------------------------------------------------
    ("Zenodo routes probed and recorded with code and byte count", 6, 6, "routes",
     "### section (C)/(H) BAR 3."),
    ("Zenodo routes that answered", 0, 0, "routes",
     "### section (A)/(C): ### **A `200` CARRYING AN EMPTY RESULT IS AN EMPTY RESULT**, and the "
     "`q=recid:` route that returned 200 with `total: 0` is counted as NOT ANSWERING."),
    ("positive controls run against a host known to answer", 1, 1, "controls",
     "### section (C)/(H) BAR 3: 200, so ### **THE NETWORK IS NOT THE CAUSE.**"),
    ("DOIs swept", 17, 17, "DOIs", "### section (C): every one the corpus names outside archive/."),
    ("records enumerated from the platform", 0, 0, "records",
     "### section (C): the sweep returned none, and the component says so."),
    ("figures in the live half sourced from the corpus instead of the platform", 0, 0, "figures",
     "### section (C)/(H) BAR 4. ### **A RECOLLECTION DRESSED AS A LIVE READ WOULD BE THE WORST "
     "OUTCOME AVAILABLE HERE**, because the order said READ LIVE."),
    ("verdicts returned on (F2)", 1, 1, "verdicts",
     "### section (C)/(I): ### **UNTESTED.** ### Neither met nor refuted, and not guessed."),
    ("halves of the deposit-rule search printed", 2, 2, "searches",
     "### section (C)/(H) BAR 5: by the name a reader gave it, AND by the content such a rule "
     "would have -- `b385`'s species."),
    ("written deposit rules located", 0, 0, "rules",
     "### section (A)/(C): ### **(F3) MET.**"),
    ("standing laws quoted and named as NOT a deposit rule", 2, 2, "laws",
     "### section (C): the internal-until-fruit law and the sequencing law."),
    ("observed practice stated as a rule", 0, 0, "statements",
     "### section (C): stated ### **AS OBSERVATION** ### and routed to the author."),
    ("deposit rules written by this seat", 0, 0, "rules",
     "### section (G): ### **A SEAT THAT SUPPLIES THE WORDS HAS WRITTEN A NEW RULE UNDER AN OLD "
     "NAME** (`b385`)."),

    # ---- COMPONENT 3: THE UNREACHED REPOSITORY ---------------------------------------------------
    ("credential-free routes tried on the repository name", 4, 4, "routes",
     "### section (D): ls-remote, the public account listing, the corpus`s other citations, and "
     "the archive`s own audit."),
    ("public repositories listed on the account", 42, 42, "repositories",
     "### section (A)/(D): 40 of them `SIDE-*`."),
    ("corpus citations of the name, classified by their own hedging", 10, 10, "citations",
     "### section (A)/(D): 8 of them marking it future, candidate, proposed, reserved or `or "
     "similar`."),
    ("verdicts returned on the repository", 1, 1, "verdicts",
     "### section (D): one of ABSENT / PRIVATE / UNDECIDABLE-WITHOUT-CREDENTIALS, with what each "
     "would mean for the citing document`s Proposition."),
    ("b388 findings withdrawn by this act", 1, 1, "findings",
     "### section (A)/(D)/(H) BAR 6. ### **`b388` REPORTED A FALSE DEFECT** ### because its "
     "extractor harvested every `SIDE-*` backtick out of a member document and read a "
     "future-tense mention as a citation."),
    ("withdrawals reported as a component result rather than a footnote", 1, 1, "withdrawals",
     "### section (D)/(H) BAR 6. ### **A SEAT THAT CORRECTS A PRIOR ACT`S ERROR BY QUIETLY "
     "REPORTING A DIFFERENT ANSWER HAS HIDDEN THE ERROR INSIDE THE CORRECTION** (`b385`)."),
    ("documents edited by this component", 0, 0, "documents",
     "### section (D)/(F): the citing document is ### **CORRECT AS WRITTEN** ### and needs "
     "nothing."),
    ("LIST 1 closures", 0, 0, "closures",
     "### section (J): ### **A LIST LOSING A MEMBER BY WITHDRAWAL IS NOT A CLOSURE.**"),

    # ---- COMPONENT 4: (R18) APPLIED --------------------------------------------------------------
    ("head notes written", 2, 2, "notes",
     "### section (E)/(H) BAR 7: exactly one per map, and (R18) adds nothing else."),
    ("corpus documents written into by this act", 2, 2, "documents",
     "### section (F): SPIRAL_MAP.md and THE_LOAD_BEARING_MAP.md, plus the ledger appends "
     "OPEN_TRAILS.md and CORRESPONDENCE.md which are not document edits."),
    ("prior head declarations removed", 0, 0, "declarations",
     "### section (A)/(E)/(H) BAR 7: the precedent is that prior heads are PRESERVED -- "
     "SPIRAL_MAP carries b190 and b186; THE_LOAD_BEARING_MAP carries b190 and b189."),
    ("prior head declarations re-read out of the files after the write", "HEADS", "HEADS",
     "declarations", "### section (E)/(H) BAR 7: every one, from the file and not from memory. "
     "### COUNTED OFF THE TWO MAPS BY THIS FILE, NOT TYPED."),
    ("lines changed outside either map`s head block", 0, 0, "lines",
     "### section (E)/(H) BAR 7/(I) `(E3)`: if either diff touches one, ### **THE COMPONENT HAS "
     "EXCEEDED `(R18)` AND THE ARM MUST CATCH IT.**"),
    ("maps merged into the other", 0, 0, "maps", "### section (E): `(R18)`'s own words."),
    ("rows, clusters or terminals moved by a head note", 0, 0, "items", "### section (E)."),

    # ---- THE BARS AND THE APPARATUS --------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (H)."),
    ("bars with a stated floor", 8, 8, "bars",
     "### section (H): `b347`'s rule -- ### **A BAR WITHOUT A FLOOR IS NOT A BAR.**"),
    ("numerical bars on a computed quantity", 0, 0, "bars",
     "### section (H): ### **THIS ACT COMPUTES NOTHING ABOUT THE OBJECT**, and says UNPRICED "
     "rather than leaving it blank."),
    ("must-fail fixtures", 4, 4, "fixtures", "### section (H): BARS 2, 4, 6 and 7."),
    ("gate arms declared", "ARMS", "ARMS", "arms",
     "### section (H): named, and each written by content. ### COUNTED OFF THIS FACE`S OWN TEXT "
     "BY THIS FILE -- and ### **THE WILDCARD MENTION `G-NO*` IS NOT AN ARM** (`b348`'s "
     "use-and-mention species, which would otherwise have made it 35)."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms",
     "### section (H): stripped code or tool output only (`b348`, `b373`) -- ### **BUT A POSITIVE "
     "ARM READS THE CODE ITSELF** (`b386`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "### section (H): `b352`/`b388` -- `G-HEADSKEPT` diffs against the PRE-ACT blob, and "
     "`G-ORDER` is SIDE-INVARIANT."),
    ("new `relay` tool files", 6, 6, "files",
     "### section (F): the cap counts FILES (`b382`), and this act is at it exactly."),
    ("files staged by `-A`", 0, 0, "commands",
     "`b381`: ### **STAGE BY AN EXPLICIT FILE LIST.**"),
    ("untracked run records of earlier acts committed", 0, 0, "files", "### section (F)."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "### section (F): RULING (R16)."),

    # ---- THE STANDING NOTHINGS OF THE PROGRAMME --------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (J)."),
    ("documents reclassified", 0, 0, "documents", "### section (J)."),
    ("registry rows edited", 0, 0, "rows", "### section (F)/(J)."),
    ("standards edited", 0, 0, "files", "### section (J)."),
    ("amendments applied", 0, 0, "amendments", "### section (J): b383`s three stay routed."),
    ("correspondence rows edited", 0, 0, "rows", "### section (F)/(J): rows are APPENDED."),
    ("lists closed", 0, 0, "lists", "### section (J): the four stay OPEN."),
    ("clusters added, split, merged or renamed in either map", 0, 0, "clusters",
     "### section (F)/(J)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (J)."),
    ("faces promoted", 0, 0, "faces", "### section (J)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (J)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (J)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (J): ### **NO CLAIM IN EITHER DIRECTION.**"),
    ("posture-lock changes", 0, 0, "changes", "### section (J): the posture lock is separate."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (J): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A)/(C): every quoted line read at its own line number; every probe run live."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration`s own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


PP = r'D:\MY-DOwnloads\PLACE-papers'
MAPS = [os.path.join(PP, 'SPIRAL_MAP.md'),
        os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')]


def count_syntheses():
    """### **EVERY CLUSTER SYNTHESIS ON DISK OUTSIDE `archive/`.** ### Counted, not remembered."""
    n = 0
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.startswith(('.git', 'archive')):
            continue
        n += len([f for f in fn if 'CLUSTER_SYNTHESIS' in f and f.endswith('.md')])
    return n


def count_heads():
    """### **THE CLASS DECLARATIONS STANDING IN BOTH MAPS` HEAD BLOCKS BEFORE THIS ACT WRITES.**"""
    n = 0
    for f in MAPS:
        lines = io.open(f, encoding='utf-8').read().splitlines()[:40]
        n += len([L for L in lines if L.startswith('**DOCUMENT CLASS')])
    return n


def count_arms(text):
    """### **THE NAMED ARMS ON THE FACE.** ### `G-NO*` IS A WILDCARD MENTION AND IS NOT AN ARM."""
    import re
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b389_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    print('  ITS SELF-TEST, RUN HERE BEFORE IT IS TRUSTED:')
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
    measured = dict(SYN=count_syntheses(), HEADS=count_heads(), ARMS=count_arms(text))
    print()
    print('  ### ### **THE THREE OPEN CLAUSES, MEASURED RATHER THAN TYPED:**')
    for k in ('SYN', 'HEADS', 'ARMS'):
        print('      %-8s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b389_registration_2026-09-09.txt -- b389, THE LOOK-SEE, THE "
                             "DEPOSITED LAYER, AND THE UNREACHED REPOSITORY"),
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
