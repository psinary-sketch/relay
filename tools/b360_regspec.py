# -*- coding: utf-8 -*-
"""b360_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any file of the act's
### content is written.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b360_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b360_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')

THIS_ACT = 360


def span_start():
    """### ### **THE SPAN'S FIRST ACT, READ OFF THE FINDINGS DOCUMENT AND NOT TYPED.**

    ### The last section whose heading ends `-- THE FOLD` carries a filing line naming the act that wrote
    ### it. ### The span begins at the act AFTER that one. ### **A SPAN TAKEN FROM A DRAFT IS A SPAN
    ### NOBODY MEASURED**, and this is the whole reason the number is computed here.
    """
    import re
    txt = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    heads = [m.start() for m in re.finditer(r'^## .*THE FOLD\s*$', txt, re.M)]
    if not heads:
        raise LookupError('no fold section in the findings document')
    tail = txt[heads[-1]:]
    m = re.search(r'Filed by b(\d+)', tail)
    if not m:
        raise LookupError('the last fold section names no filing act')
    return int(m.group(1)) + 1


def count():
    """### ### **THE SPAN, AS A LIST OF `(act, bank path)`, COUNTED OFF THE BANKS ON DISK.**

    ### An act's bank is the one `data/bNNN_*.txt` whose SECOND line opens with the act's own name and
    ### carries `### THE BANK.` ### **AN ACT WITH NO SUCH FILE, OR WITH MORE THAN ONE, RAISES** -- because
    ### a fold that guessed which file was an act's bank would be quoting a file nobody chose.
    """
    import glob
    out = []
    for n in range(span_start(), THIS_ACT):
        hits = []
        for p in sorted(glob.glob(os.path.join(D, 'b%d_*.txt' % n))):
            lines = io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))
            if len(lines) > 1 and lines[1].startswith('b%d -- ' % n) and '### THE BANK.' in lines[1]:
                hits.append(p)
        if len(hits) != 1:
            raise LookupError('b%d: %d candidate banks -- %s' % (n, len(hits), [os.path.basename(h) for h in hits]))
        out.append(('b%d' % n, hits[0]))
    return out


CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A): NOTHING IS DEPOSITED AND NOTHING IS WRITTEN AT ZENODO, in every branch."),
    ("network calls to any platform", 0, 0, "calls", "### section (A): this act makes none. ### RE-MEASURED by G-NODEPOSIT on STRIPPED code."),
    ("deposited artifacts touched", 0, 0, "files", "### section (A): the records are immutable at their versions."),
    ("quantities computed", 0, 0, "quantities", "### section (H): no frame, seed, transform, quadrature, fit, score, coefficient or series."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 4, 4, "bars", "### section (H): F-QUOTE, F-NOGRADE, F-ADDITIVE and the roster arm, each an equality or a presence."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("verdict branches", 3, 3, "branches", "### section (J): the arc folds / it does not fold into one statement / unaffordable."),
    ("branches left unclaimed", 0, 0, "branches", "### section (J): a branch that cannot be taken is shown unreachable (b350's rule)."),
    ("quotations reaching FINDINGS.md without being located at the act that ORIGINATED them", 0, 0,
     "quotations", "### section (C): BAR ONE. ### The emitter REFUSES to write."),
    ("grade strings written that do not appear verbatim in their own act's bank", 0, 0, "grades",
     "### section (C): BAR TWO, the no-grade-moved claim made mechanical."),
    ("lines of FINDINGS.md edited above the appended section", 0, 0, "lines", "### section (C): PURELY ADDITIVE."),
    ("times the section may appear in FINDINGS.md", 1, 1, "sections", "### section (C): idempotent; a second run writes nothing."),
    ("span acts counted from the record rather than taken from the draft", 11, None, "acts",
     "### section (B): the emitter counts the span itself off the banks on disk. ### The demand is what it counts."),
    ("bridges typed between the rhyming obstructions", 0, 0, "bridges", "### section (D): NONE, in either direction."),
    ("equivalences compiled", 0, 0, "compilations", "### section (D): the deposit's own refusal is quoted at the deposited file."),
    ("obstructions the fold presents as one obstruction", 0, 0, "obstructions",
     "### section (D): three that rhyme are three, and b358's localization is a fourth entry of the same kind."),
    ("arc clauses written above the grade their acts support", 0, 0, "clauses",
     "### section (E): where the order's phrasing runs ahead of the acts, the narrower sentence is written and the difference declared."),
    ("desk items carrying neither a standing nor what would move it", 0, 0, "items", "### section (F)."),
    ("work opened by the span's own finding", 0, 0, "orders", "### section (F): it is filed as a sentence and opens nothing."),
    ("mirror roster rows appended", 1, 1, "rows", "### section (G): FACES_LEDGER.md, at the END of the list."),
    ("mirror roster rows moved, removed or re-ordered", 0, 0, "rows", "### section (G): order is significant and no existing slot changes."),
    ("prior archives rebuilt", 0, 0, "archives", "### section (G): the ruling's own words -- not retroactive."),
    ("mirror rebuilds", 1, 1, "rebuilds", "### section (G)/(H): AFTER the commit, verified on all three clauses."),
    ("PLACE-papers files written", 1, 1, "files", "### FINDINGS.md and no other. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("faces ledger rows appended or rewritten", 0, 0, "rows", "### the closing: the faces writer runs only if a row moves, and none does."),
    ("ERRATA entries opened", 0, 0, "entries", "### section (L): none by this act."),
    ("routed items opened", 0, 0, "items", "### section (L): H1, H-NGEK, E-2026-09-07-1's passages and the row-204 correction all stay put."),
    ("ledger passages repaired in place", 0, 0, "passages", "### section (L)."),
    ("relay tools created", 7, 7, "files", "the extract, the regspec, the fold, the roster writer, the correspondence, the index append and the suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("keystones created or edited", 0, 0, "documents", "### section (C)."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing; the alias set checked against the banked keys first."),
    ("aliases colliding with a banked key", 0, 0, "aliases", "### section (I): `the arc as one statement` reaches b348's key and is NOT claimed."),
    ("frames recomputed", 0, 0, "frames", "### section (L): the instrument lane stays PARKED under ruling R4."),
    ("ledger rows moved", 0, 0, "rows", "### section (L)."),
    ("bars moved", 0, 0, "bars", "### section (L)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (L)."),
    ("acts re-verdicted", 0, 0, "acts", "### section (L)."),
    ("proofs attempted", 0, 0, "proofs", "### section (L)."),
    ("new mathematics", 0, 0, "statements", "### section (L)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (L)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (L)."),
    ("claims about h2, totality, the roster's correctness", 0, 0, "claims", "### section (L)."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("posture-lock changes", 0, 0, "changes", "### section (L): the posture lock is separate and is not touched by a fold."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b360_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    # ### THE SPAN IS COUNTED HERE OFF THE BANKS ON DISK, NEVER TAKEN FROM THE DRAFT.
    span = count()
    print('  ### THE SPAN, COUNTED OFF THE BANKS ON DISK : %d act(s) -- %s' % (len(span), ' '.join(a for a, _p in span)))
    clauses = []
    for (c, cap, dem, u, frm) in CLAUSES:
        if c.startswith('span acts counted'):
            d2 = len(span)
            cap2 = len(span)
        elif c.startswith('artifact counts predicted'):
            d2, cap2 = n, cap
        else:
            d2, cap2 = dem, cap
        clauses.append({"clause": c, "cap": cap2, "demand": d2, "units": u, "from": frm})
    spec = {"registration": "data/b360_registration_2026-09-07.txt -- b360, THE FOLD, b349 THROUGH b359",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses) and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s' % (len(unsat), unsat if unsat else ''))
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('      %s' % c)
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
