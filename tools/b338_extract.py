# -*- coding: utf-8 -*-
"""b338_extract.py -- THE EXTRACT STEP FOR THE FOLD, b331-b334. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### Each of the four acts' own sentences at its own bank -- the result
### quotation, the obstacle, the grade words; the fold's own law at b323 and its rules at b331; the wave's candidate
### list at b324 (restated as the desk's first item); the housekeeping's four items at b337 and the cost census at
### b336 (the desk's state beside it); the correspondence rows 176-184 at the table; the FINDINGS section headings the
### fold appends after; the sortie ferry's leg-3 sentence. ### b283's law: every quotation located at its emitting file
### and its line before it is written anywhere else.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b338_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


B331, B332, B333, B334 = d('b331_the_fold.txt'), d('b332_the_clause_stated.txt'), d('b333_the_archimedean_term_derived.txt'), d('b334_the_aim_map.txt')
B323, B324, B336, B337 = d('b323_the_fold.txt'), d('b324_the_keystones_reread.txt'), d('b336_the_cost_census.txt'), d('b337_the_housekeeping.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
FERRY = d('b338_ferry_2026-09-06.txt')

WANTED = [
    # ### ---- the four acts, each at its own bank
    ('b331 -- the result', B331, 'AND IT IS PURELY ADDITIVE, MEASURED AND NOT PROMISED.'),
    ('### the obstacle', B331, 'IT DOES NOT SAY EITHER NEXT ACT IS THE DISCHARGE.'),
    ('### the desk carries the two next acts', B331, 'THE DESK CARRIES THE TWO NEXT RESEARCH ACTS THE ORDER NAMES -- THE DISCHARGE-STATEMENT'),
    ('### the one anchor narrowed', B331, "one anchor"),
    ('b332 -- the result', B332, "THE CLAUSE IS STATED, WHOLE, IN THE ARC'S VOCABULARY, AND IT IS NOT DISCHARGED."),
    ('### the E0 gate', B332, 'THE E0 GATE HALTS AT K8, THE QUANTIFIERS, AND AT NOTHING ELSE.'),
    ('### the ranking', B332, 'THE RANKING, UNDER THE SEALED RULE, PUTS THE ARCHIMEDEAN DISTRIBUTION SOFTEST -- NOT'),
    ('### the obstacle', B332, 'IT DOES NOT SAY THE RANKING IS A VERDICT ON THE CLAUSE.'),
    ('### the first emission', B332, 'THE FIRST EMISSION CARRIED A SENTENCE THE COMPUTED RANKING CONTRADICTED.'),
    ('### the expectation wrong about its own rule', B332, "THIS SEAT'S SEALED EXPECTATION WAS WRONG ABOUT ITS OWN SEALED RULE."),
    ('b333 -- the result', B333, "THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED."),
    ('### the chain', B333, 'THE CHAIN DERIVES ON IMPORT.'),
    ('### the re-rank', B333, 'THE RE-RANK UNDER THE SEALED RULE, NOTHING ADJUSTED: K5 AND K6 TIE AT THE SOFTEST RANK.'),
    ('### the obstacle', B333, 'IT DOES NOT SAY THE SEALED BAR WAS MET.'),
    ('### the sealed bar defective', B333, 'E1 -- THE SEALED BAR PAIRED THE BUMP WITH A TABLE MADE FOR ANOTHER FUNCTION.'),
    ('### families not conferred', B333, '`MEASURED-ON-FAMILIES` IS NOT CONFERRED on K5 by this act.'),
    ('b334 -- the result', B334, 'FOR ZETA THE PRIME SUM STAYS INSIDE THE MARGIN AT EVERY AIM AT THIS REACH -- A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE.'),
    ('### the crossing region', B334, 'THE EPSTEIN CROSSING REGION -- THE NEGATIVE CONTROL CHARTED -- IS THREE AIMS:'),
    ('### soften apart', B334, 'K5 AND K6 DO NOT SOFTEN TOGETHER OVER AIMS: `Spearman(s5, s6) = -0.6158` OVER THE COVERED LEG.'),
    ('### the threshold rule', B334, 'THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION, AND THE MAP SAYS SO.'),
    ('### the obstacle', B334, 'IT DOES NOT SAY A CHART IS A PROOF.'),
    ('### the route bar exceeded', B334, 'E4 -- THE TRANSFORM-ROUTE BAR OF `1e-10` WAS EXCEEDED AT `1.14e-04`'),
    ('### the parallel launch', B334, 'E3 -- THE FIRST LAUNCH RAN THE FOUR MODES IN PARALLEL AND THE MACHINE KILLED THEM FOR MEMORY.'),
    # ### ---- the fold's law and rules
    ("b323 -- the fold's law", B323, 'A FOLD IS PURELY ADDITIVE OR IT IS NOT A FOLD'),
    ("b331 -- the fold's rules held", d('b331_registration_2026-09-06.txt'), "(D) THE FOLD'S OWN RULES, INHERITED FROM b323 AND HELD HERE."),
    ('### F-QUOTE against the originator', d('b331_registration_2026-09-06.txt'), '`F-QUOTE` CHECKS EVERY QUOTATION AGAINST THE ACT THAT ORIGINATED IT'),
    ('### F-COUNT the arc exactly', d('b331_registration_2026-09-06.txt'), '`F-COUNT` REQUIRES THE ARC EXACTLY'),
    # ### ---- the wave's candidate list, at b324
    ("b324 -- the candidate list, typed", B324, "THE WAVE'S CANDIDATE LIST, TYPED. ### NO RECOMMENDATION, NO RANKING."),
    ('### [NEW] the instrument', B324, 'the archimedean instrument, certified against three of the source'),
    ('### [NEW] the identity', B324, 'the identity `W_infinity(f) - Tr(theta(f) S) = -INT f(rho^-1) eps(rho)'),
    ('### [NEW] non-positive by construction', B324, "the finding that the window's balance is non-positive"),
    ('### [NEW] the resolving-power rule', B324, 'the resolving-power rule and its two prices: the exponent question and the'),
    ('### [REFINEMENT-OF-DEPOSITED]', B324, "**[REFINEMENT-OF-DEPOSITED]** ### the arc's instrument sits inside the monograph's"),
    ('### [REFINEMENT-OF-INTERNAL]', B324, "**[REFINEMENT-OF-INTERNAL]** ### the wall's grading of Connes-Consani as stalling at the"),
    ("### the wave is the author's", B324, "THE WAVE IS THE AUTHOR'S. ### THIS LIST IS TYPED AND NOT RANKED, AND NO SEAT STARTS ONE."),
    ("b331 -- the negative control typed as a candidate", B331, "arc's negative control typed as a candidate; the seam's debt item 1;"),
    # ### ---- the housekeeping's state, at b337; the cost census, at b336
    ('b337 -- (1) the fetch', B337, 'THE FETCH AGREES WITH REGISTRY ON EVERY FIELD; TWO LEDGERS CURRENT, ONE DRIFT, REPAIRED BY'),
    ('### (2) the partition', B337, 'THE PARTITION, EXECUTED AS RULED: ONE APPENDED BLOCK, ENTRIES UNMOVED.'),
    ('### (3) TECHNE', B337, 'THE NINE AUGUST TECHNE FILES COMMITTED LOCALLY AT `4c0a6af`, NOT PUSHED.'),
    ('### (4) the receipts', B337, 'THE PATENT RECEIPTS: ABSENT ON THE MOUNTED VOLUMES, AND F: IS NOT MOUNTED.'),
    ('### nothing concluded', B337, 'NOTHING IS CONCLUDED ABOUT WHETHER A REPLY'),
    ('b336 -- the census', B336, 'FIFTEEN ROWS TYPED, THROUGH THE WRITER, AND NO GRADE MOVED.'),
    ('### the cheapest owed step', B336, 'NO ROW HOLDS A READ OR AN IMPORT AS ITS NEXT'),
    ('b335 -- the standing file', d('b335_the_standing_clauses.txt'), '`relay/tools/FERRY_STANDING.md`, VERSION 1, EXISTS AND IS MEASURED.'),
    # ### ---- the rows and the findings
    ('the table -- row 176', TABLE, '| 176 | THE FOLD, b323 THROUGH b330,'),
    ('### row 178', TABLE, '| 178 | THE CLAUSE STATED: THE OPEN'),
    ('### row 179', TABLE, '| 179 | THE ARCHIMEDEAN TERM DERIVED'),
    ('### row 180', TABLE, '| 180 | THE AIM-MAP, FOR ZETA: THE R'),
    ('### row 181', TABLE, '| 181 | THE AIM-MAP, FOR THE EPSTEIN'),
    ('findings -- the prior fold', FINDINGS, '## THE DISCRIMINATING-FAMILY ARC, b323\u2013b330 \u2014 THE FOLD'),
    ('### the clause stated', FINDINGS, '## THE CLAUSE STATED \u2014 b332'),
    ('### the b333 addendum', FINDINGS, '<!-- b333 addendum: the archimedean term derived -->'),
    # ### ---- the sortie ferry, leg 3
    ('the sortie -- leg 3', FERRY, 'LEG 3 (b338) \u2014 THE FOLD, b331 through b334, four acts, under'),
    ("### the desk's first item", FERRY, "the fold rules, with the wave's candidate list restated as the"),
    ("### the housekeeping's state beside it", FERRY, "desk's first item and the housekeeping's state beside it."),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b338_extract.py -- THE FOLD, b331-b334. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
