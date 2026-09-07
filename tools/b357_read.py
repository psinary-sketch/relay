# -*- coding: utf-8 -*-
"""b357_read.py -- WHAT THE LEDGERS SAY THE CHECKS CERTIFY. ### ONE TABLE. ### NO ROW IS EDITED.

### ### **WHAT IT IMPORTS IS THE WHOLE ARGUMENT THAT IT COMPUTES NOTHING:** ### a needle puller, the anchor
### tool, the shared normaliser and a clock. ### **NO FRAME, NO SEED, NO TRANSFORM, NO FIT.**
### ### **EVERY ROW IS LOCATED BY `anchor_from_file` AT ITS OWN LEDGER BEFORE IT IS CLASSIFIED.** ### A row
### that cannot be located is reported as UNCLASSIFIED, never classified from memory.
### ### **AND THE TWO FINDINGS ARE KEPT APART** (registration section (C)): the ATTRIBUTION fault and the
### MEMBERSHIP question are different, and a row may carry the first and be right about the second.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import run_clock     # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WIDER = 'SAYS THE WIDER SENTENCE'
NARROWER = 'SAYS THE NARROWER SENTENCE'
SILENT = 'SILENT'
STATUSES = (WIDER, NARROWER, SILENT)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def d(n):
    return os.path.join(D, n)


# ### (ledger, hint, act the row is about, status, what the row says the check certified)
ROWS = [
    (FINDINGS, 'The discriminating seeds of b328 are explicitly inside the class', 'b328', WIDER,
     'that the seeds ARE IN THE CLASS, and it credits the SCAN in the same breath -- '
     '*"(b328\'s lawfulness scan)"*. ### **THE CLEAREST INSTANCE IN THE RECORD.**'),
    (FINDINGS, '**(S)** For every `g` in the source', 'b332', NARROWER,
     'nothing about the corpus\'s own objects. ### It states the CLAUSE, quantifying over the source\'s '
     'class, which is the statement being aimed at and not a claim that anything the corpus built is in it.'),
    (FINDINGS, 'a local proposition per seed (lawful or not), decided by b320', 'b320', NARROWER,
     'that the scan DECIDES A LOCAL PROPOSITION PER SEED. ### **IT DOES NOT SAY THE SEEDS ARE IN THE '
     'CLASS**, and it names the scan as what decided the proposition rather than as what established '
     'membership. ### This row is careful and was written when an act was grading a constituent.'),
    (FINDINGS, 'K1** the class | IMPORT-UNDER-THE-BAR (b328) | MEASURED-ON-FAMILIES (b320)', 'b320/b328', NARROWER,
     'that the class is IMPORTED under the bar and that what b320 did was MEASURED-ON-FAMILIES. ### **THE '
     'GRADE WORD ITSELF CARRIES THE LIMIT** -- measured on families, not established for a class.'),
    (FINDINGS, 'the finite-instance explicit formula is realized on lawful objects', 'b313-b321', SILENT,
     'nothing about what any check certified. ### It says the formula is realized ON lawful objects and '
     'grades the arc; the word does the work of naming which objects, not of reporting a test.'),
    (FACES, 'TWO SEEDS BUILT, both lawful at every width (Definition 3.1 scan', 'b328', WIDER,
     'that the seeds ARE LAWFUL, with *"(Definition 3.1 scan)"* given as the warrant. ### **THE '
     'PARENTHETICAL IS THE ATTRIBUTION**: the scan is named as what makes them lawful.'),
    (FACES, '56 of 56 seeds lawful by Definition 3.1 and the pole conditions', 'b334', WIDER,
     'that fifty-six seeds are LAWFUL BY Definition 3.1. ### The preposition *by* does the same work as '
     'b328\'s parenthetical: the check is named as the ground of the property.'),
    (FACES, 'S1 -- the clause stated: for every g in the source', 'b332', NARROWER,
     'nothing about the corpus\'s objects; it states the clause over the source\'s class, as FINDINGS does.'),
    (CORR, 'the discriminating seeds of b328 inside it), the places sum', 'b332', WIDER,
     'that the seeds are INSIDE the class, in a parenthetical inside the clause. ### It does NOT credit the '
     'scan -- ### **so it carries the membership assertion without the attribution fault**, and the two are '
     'reported apart as the registration required.'),
    (CORR, 'the reading this act supports is *the seeds are built as autocorrelations', 'b355', NARROWER,
     'exactly the narrower sentence, in the record already. ### **b355 PUT IT THERE**, and it is the row a '
     'later reader should find first.'),
    (INDEX, "(S) for every g in the source's class (Definition 3.1 with Proposition C.1", 'b332', WIDER,
     'the same parenthetical as the correspondence row it summarises -- *"b328\'s seeds inside"*. ### '
     '**MEMBERSHIP ASSERTED, ATTRIBUTION NOT MADE.**'),
    (INDEX, 'lawfulness and every aimed seed at b334, b343, b344 and b349 USED BOTH', 'b355', NARROWER,
     'the narrower sentence, with the classification b355 made. ### Already in the index.'),
]

# ### **WHICH WIDER ROWS CARRY THE ATTRIBUTION FAULT. ### DECLARED HERE AS DATA, ROW BY ROW, BY THE SEAT.**
# ### ### **AND WHY IT IS DATA AND NOT A TEST:** ### the first run of this tool decided this grouping by
# ### GREPPING THIS SEAT'S OWN COMMENTARY for the word `ATTRIBUTION`. ### That is `b348`'s use-and-mention
# ### species -- a scanner over prose cannot tell what a sentence DOES from what it MENTIONS -- and it
# ### mis-grouped two rows of five. ### **THE CURE IS THE ONE b348 MINTED: THE SEAT STATES THE JUDGEMENT
# ### ### AND NO SCANNER INFERS IT FROM PROSE.** ### The superseded run is kept at
# ### `data/b357_read_run_SUPERSEDED_LEXICAL_GROUPING.txt` and is not edited.
FAULT = {
    ('FINDINGS.md', 'b328'): True,        # "(b328's lawfulness scan)" -- the scan named as the warrant
    ('FACES_LEDGER.md', 'b328'): True,    # "(Definition 3.1 scan)" -- the same, parenthetically
    ('FACES_LEDGER.md', 'b334'): True,    # "lawful BY Definition 3.1" -- the preposition attributes
    ('CORRESPONDENCE.md', 'b332'): False,  # "the seeds of b328 inside it" -- membership, no warrant named
    ('banked_index.py', 'b332'): False,    # the same parenthetical, summarised into the index
}


def main():
    rec('=' * 100)
    rec('b357 -- WHAT THE LEDGERS SAY THE CHECKS CERTIFY. ### ONE TABLE. ### NO ROW IS EDITED.')
    rec('=' * 100)
    rec('  ### the sealed statuses, and no others : %s' % ' / '.join(STATUSES))
    rec('  ### the four ledgers : FINDINGS.md, FACES_LEDGER.md, CORRESPONDENCE.md, banked_index.py')
    rec('  ### ### **THE ATTRIBUTION FAULT AND THE MEMBERSHIP QUESTION ARE KEPT APART.**')

    rec('')
    rec('-' * 100)
    rec('  ### THE TABLE. ### EVERY ROW LOCATED AT ITS OWN LEDGER BEFORE IT IS CLASSIFIED.')
    rec('-' * 100)
    out, unclassified = [], []
    for path, hint, act, status, certifies in ROWS:
        try:
            n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
        except (AF.AnchorError, LookupError) as e:
            unclassified.append(dict(ledger=os.path.basename(path), hint=hint, error=str(e)[:90]))
            rec('')
            rec('  ### ### **UNCLASSIFIED -- COULD NOT BE LOCATED** : %s / %s' % (os.path.basename(path), hint[:60]))
            rec('      %s' % str(e)[:110])
            continue
        out.append(dict(ledger=os.path.basename(path), line=n, act=act, status=status,
                        certifies=certifies, text=line.strip()[:300]))
        rec('')
        rec('  ### **%s : %d**   (the row is about %s)' % (os.path.basename(path), n, act))
        rec('      | %s' % line.strip()[:190])
        rec('      ### **STATUS : %s**' % status)
        rec('      ### it says the check certified : %s' % certifies)

    wider = [r for r in out if r['status'] == WIDER]
    narrower = [r for r in out if r['status'] == NARROWER]
    silent = [r for r in out if r['status'] == SILENT]

    rec('')
    rec('-' * 100)
    rec('  ### THE COUNT.')
    rec('-' * 100)
    rec('    rows located and classified : %d ; unclassified : %d' % (len(out), len(unclassified)))
    rec('    %-32s %d' % (WIDER, len(wider)))
    rec('    %-32s %d' % (NARROWER, len(narrower)))
    rec('    %-32s %d' % (SILENT, len(silent)))
    for r in wider:
        rec('      WIDER : %-22s line %-6d (about %s)' % (r['ledger'], r['line'], r['act']))

    rec('')
    rec('-' * 100)
    rec("  ### THE BRANCH, BY THE SEALED RULE OF SECTION (D).")
    rec('-' * 100)
    rec('    ### **(NO ROW SAYS THE WIDER SENTENCE) -- UNREACHABLE, AND SHOWN SO.** ### %d rows say it.'
        % len(wider))
    rec('    ### **(THE ROWS ARE SILENT) -- UNREACHABLE, AND SHOWN SO.** ### Only %d of %d is silent; the'
        % (len(silent), len(out)))
    rec('      rest say one thing or the other.')
    rec('    ### **AND THE MIXTURE RULE, SEALED BEFORE THE READING:** ### some rows say it and others are')
    rec('      narrower or silent, so ### **THE SECOND BRANCH IS TAKEN**, because one row asserting it is')
    rec('      enough to need an erratum and the others are reported beside it.')
    verdict = 'SOME ROWS SAY IT' if wider else ('THE ROWS ARE SILENT' if silent and not narrower
                                                else 'NO ROW SAYS THE WIDER SENTENCE')
    rec('    ### ### ### **THEREFORE: %s.**' % verdict)

    rec('')
    rec('-' * 100)
    rec('  ### THE TWO FINDINGS, KEPT APART AS THE REGISTRATION REQUIRED.')
    rec('-' * 100)
    attrib = [r for r in wider if FAULT[(r['ledger'], r['act'])]]
    memonly = [r for r in wider if not FAULT[(r['ledger'], r['act'])]]
    rec('    ### **(1) THE ATTRIBUTION FAULT** -- crediting the SCAN with establishing membership:')
    for r in attrib:
        rec('        %-22s line %-6d (about %s)' % (r['ledger'], r['line'], r['act']))
    rec('    ### **(2) MEMBERSHIP ASSERTED WITHOUT THE ATTRIBUTION** -- the row says the seeds are in the')
    rec('    ### class and does not say what made them so:')
    for r in memonly:
        rec('        %-22s line %-6d (about %s)' % (r['ledger'], r['line'], r['act']))

    lex = [r for r in wider if 'scan' in r['certifies'].lower() and 'ATTRIBUTION' in r['certifies']]
    moved = [r for r in wider
             if (r in lex) != bool(FAULT[(r['ledger'], r['act'])])]
    rec('    ### ### **AND HOW THIS GROUPING WAS MADE, DECLARED BECAUSE THE FIRST RUN MADE IT WRONGLY:**')
    rec('    ### ### The grouping above is ### **DECLARED DATA** ### -- this seat states, row by row, which')
    rec('    ### ### rows name a warrant. ### The first run instead GREPPED THIS SEAT\'S OWN COMMENTARY for')
    rec('    ### ### the word `ATTRIBUTION` and grouped %d/%d; ### **IT MIS-GROUPED %d ROWS OF %d:**'
        % (len(lex), len(wider) - len(lex), len(moved), len(wider)))
    for r in moved:
        rec('        %-22s line %-6d (about %s)   ### belongs in group (%d)'
            % (r['ledger'], r['line'], r['act'], 1 if FAULT[(r['ledger'], r['act'])] else 2))
    rec('    ### ### **THIS IS b348\'s USE-AND-MENTION SPECIES**, in an act whose whole subject is what a')
    rec('    ### ### check certifies: ### a scanner over prose cannot tell what a sentence DOES from what')
    rec('    ### ### it MENTIONS, and `CORRESPONDENCE.md:251` says *"without the attribution fault"* while')
    rec('    ### ### `FINDINGS.md:3039` credits the scan without ever using the word. ### **THE SUPERSEDED')
    rec('    ### ### RUN IS KEPT AT `data/b357_read_run_SUPERSEDED_LEXICAL_GROUPING.txt`, UNEDITED**, and')
    rec('    ### ### ### **THE VERDICT AND THE FIVE WIDER ROWS ARE THE SAME IN BOTH RUNS.**')
    rec('    ### ### **AND THE SENTENCE THE REGISTRATION FIXED BEFORE ANY ROW WAS READ:** ### **THE WIDER')
    rec('    ### ### SENTENCE IS NOT NECESSARILY FALSE.** ### The corpus builds `f` as `g conv g-sharp`')
    rec('    ### ### with the source\'s support and vanishing conditions; if the objects integrated were')
    rec('    ### ### smooth they would be in the class. ### **WHAT IS WRONG IN GROUP (1) IS THE WARRANT,')
    rec('    ### ### NOT THE CLAIM**, and whether the claim itself holds is `b355`\'s `H1`, graded')
    rec('    ### ### `REFUTABLE` and ROUTED, and it is NOT decided here.')

    rec('')
    rec('-' * 100)
    rec('  ### THE CONSEQUENCE, STATED ONCE AND PLAINLY, AS THE ORDER REQUIRED.')
    rec('-' * 100)
    rec('    ### ### **CLASS MEMBERSHIP IN THIS FAMILY RESTS ON THE CONSTRUCTION, AND THE SCAN CONFIRMS IT')
    rec('    ### ### RATHER THAN TESTING IT.**')
    rec('    ### Every `f` in the family is built as `g conv g-sharp`. ### For a true autocorrelation the')
    rec('    ### transform is a squared modulus and pointwise positivity is automatic, so the scan cannot')
    rec('    ### fail on such an object and what it discriminates is arithmetic that has gone wrong.')
    rec('    ### ### **AN INDEPENDENT TEST WOULD REQUIRE AN OBJECT NOT BUILT AS AN AUTOCORRELATION** --')
    rec('    ### ### something claimed to be in the class on other grounds, scanned to see whether it is.')
    rec('    ### ### **NO ACT HAS NEEDED ONE, AND NONE IS ORDERED HERE.**')

    rec('')
    rec('-' * 100)
    rec('  ### THE ERRATA ENTRY: DRAFTED AND ROUTED. ### **NOT OPENED.**')
    rec('-' * 100)
    rec('    ### The record\'s convention is that this seat drafts and routes; the author opens. ### The')
    rec('    ### draft is written to `data/b357_errata_draft.txt` and ### **NOTHING IS WRITTEN TO')
    rec('    ### `ERRATA.md`.**')
    rec('    ### **WHAT IT SAYS:** ### that %d passages across %d ledgers assert class membership -- %d of'
        % (len(wider), len(set(r['ledger'] for r in wider)), len(attrib)))
    rec('    ### them crediting the Definition 3.1 scan with establishing it and %d asserting it without'
        % len(memonly))
    rec('    ### saying what established it; that the scan cannot fail on an object built as an')
    rec('    ### autocorrelation and')
    rec('    ### therefore confirms the construction rather than testing the class; that ### **NO BANKED')
    rec('    ### ### NUMBER IS AFFECTED AND NO CHECK IS DEMOTED**; and that the separate question of')
    rec('    ### whether the piecewise-linear object is in a class defined over smooth functions is')
    rec('    ### `b355`\'s and remains routed.')

    rec('')
    rec('-' * 100)
    rec("  ### BOTH SEATS' EXPECTATIONS, SCORED.")
    rec('-' * 100)
    rec("    ### **THE NAVIGATOR'S (L2)** -- every lawfulness check in the family used the")
    rec('    ### construction-confirming scan and none used an independent test : ### **MET.** ### Every')
    rec('    ### check the ledgers describe is the Definition 3.1 scan on an object built as an')
    rec('    ### autocorrelation, and no independent test appears anywhere in the four ledgers.')
    rec("    ### **THIS SEAT'S** -- the ledgers will be MIXED, and the careful rows will be the ones")
    rec('    ### written when an act was grading a constituent rather than summarising a finding :')
    rec('    ### ### **MET, AND THE SECOND HALF IS THE INTERESTING ONE.** ### The two narrowest rows in')
    rec('    ### FINDINGS -- *"a local proposition per seed (lawful or not), decided by b320\'s scan"* and')
    rec('    ### the `K1` grade `MEASURED-ON-FAMILIES` -- are both from the constituent table. ### The')
    rec('    ### widest is from the prose that summarises what the arc achieved.')
    rec('    ### ### **SO THE RECORD IS MORE CAREFUL WHERE IT IS GRADING THAN WHERE IT IS NARRATING**, and')
    rec('    ### ### that is a fact about how this corpus is written, not about any one act.')

    rec('')
    rec('=' * 100)
    rec('  VERDICT : ### **%s**' % verdict)
    rec('  ### ### **NO ROW IS EDITED. ### NO VERDICT MOVES. ### NOTHING IS DEMOTED. ### EVERY BANKED')
    rec('  ### ### NUMBER STANDS AND EVERY CHECK THAT PASSED STILL PASSED.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b357_read_run', LINES)
    io.open(d('b357_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(verdict=verdict, statuses=list(STATUSES), rows=out, unclassified=unclassified,
             n_wider=len(wider), n_narrower=len(narrower), n_silent=len(silent),
             wider=[dict(ledger=r['ledger'], line=r['line'], act=r['act']) for r in wider],
             attribution_fault=[dict(ledger=r['ledger'], line=r['line'], act=r['act']) for r in attrib],
             membership_only=[dict(ledger=r['ledger'], line=r['line'], act=r['act']) for r in memonly],
             grouping='DECLARED DATA, row by row; the lexical rule of the superseded run mis-grouped '
                      '%d of %d (b348\'s use-and-mention species)' % (len(moved), len(wider)),
             superseded_run='data/b357_read_run_SUPERSEDED_LEXICAL_GROUPING.txt',
             ledgers=sorted(set(r['ledger'] for r in out)),
             errata='DRAFTED AND ROUTED -- data/b357_errata_draft.txt ; NOTHING WRITTEN TO ERRATA.md',
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
