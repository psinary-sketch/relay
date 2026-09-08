# -*- coding: utf-8 -*-
"""b363_correspondence.py -- ONE ROW: THE ANCHORED GATE ARMS, COUNTED AND NOT ASSERTED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a sharper gate were a
### result; as if `7 of 11` were a rate; as if the four survivors were four defects; as if a banked arm had
### actually been rewritten; or as if filing a trail entry were paying it.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE = (
    "**SCOPE: A SHARPER INSTRUMENT IS NOT A RESULT.** The helper makes needles equal to their files and says NOTHING about whether any gate asks the right question and NOTHING WHATEVER ABOUT THE OBJECT OF "
    "STUDY. NOTHING WAS COMPUTED ABOUT THE OBJECT: no frame, no seed, no transform, no quadrature, no fit, no score, no series. NO ARM WAS ACTUALLY RETIRED -- the census says what the helper WOULD HAVE "
    "reached had it existed, and the banked suites are byte-identical to what their acts left. 7 OF 11 IS NOT A RATE AND NOT A FORECAST: it is a count over eleven named arms in three named acts and it "
    "predicts nothing about the twelfth. THE FOUR SURVIVORS ARE NOT FOUR DEFECTS -- two are wrong arms and two are arms that were RIGHT, and a helper that quietened either of the latter would be a defect. "
    "THE TRAIL ENTRY IS FILED AND NOT PAID, AND NAMING A READ IS NOT PERFORMING ONE. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE "
    "IS CLOSED and THE PARTITION STAYS UNDECIDED. NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item "
    "1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where "
    "the deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b363_reads.json'), encoding='utf-8'))
    N = json.load(io.open(os.path.join(D, 'b363_census.json'), encoding='utf-8'))
    T = json.load(io.open(os.path.join(D, 'b363_trail.json'), encoding='utf-8'))
    m = ("THE ANCHORED-ARM HELPER IS BUILT AND IS **NARROWER THAN THE RULE IT WAS PROPOSED UNDER**: it would have reached **%d OF THE %d ARMS THE BANKS DECLARE**, and the draft that proposed it was wrong "
         "about its own population as well as its own estimate (b363)" % (N['retired'], N['enumerated']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code. **THE POPULATION IS COUNTED AND NOT TAKEN FROM THE DRAFT**, and it is counted twice before anything is "
            "emitted: the three acts' own headline figures, each located by the anchor tool at its own bank (FOUR, TWO and FIVE), summing to **%d**; and **%d ARMS ENUMERATED ONE BY ONE**, each pinned to the "
            "line of the bank that describes it. **THE TOOL REFUSES TO EMIT IF THE TWO DISAGREE.** They agree. The draft claimed **%d** and its own arithmetic over its own banks was wrong -- **WHICH IS WHY "
            "THE ORDER ASKED FOR A COUNT AND NOT A CONFIRMATION** -- and its cure estimate of *%s* is refuted at **%d**. **THE CLASSIFICATION IS DECLARED DATA AND NOT INFERRED FROM PROSE** (b357's cure for "
            "b357's incident: a scanner that reads a judgement out of prose is a check that can confirm rather than test), with each arm's anchor printed beside it. **THE FOUR NOT RETIRED SPLIT INTO TWO "
            "KINDS AND NOT ONE: %d ARE WRONG ARMS (A3, A10)** -- predicates testing something other than what their labels name, one of them called a wrong arm in its own act's bank -- **AND %d ARE MISSING "
            "SENTENCES (A6, A9)**, arms that were RIGHT because the bank genuinely did not carry what they asked for. **A HELPER THAT QUIETENED EITHER OF THOSE WOULD BE A DEFECT AND NOT A CURE.** **THE "
            "FOURTH SPECIES IS NAMED AND IS UNTOUCHED BY ANY NEEDLE TOOL:** the first three species are failures of how a sentence is written down and a needle built from the file cures all of them; the "
            "wrong arm is a failure of which question is asked, and **A NEEDLE BUILT FROM A FILE IS STILL A NEEDLE FOR THE WRONG QUESTION**. **THE CONTROL IS THE BANKED SUITES, UNEDITED:** six copied into "
            "tools/ under declaring names, run, deleted in a finally, **%d OF %d REPRODUCING THEIR OWN ACT'S VERDICT**, and the one that does not (b357, G-LOCATED) is **REPORTED AT FULL PROMINENCE AND NOT "
            "ADJUSTED** -- it is a suite reading a moved repository, which b357's own bank predicted. **THE HELPER EXERCISED OVER EVERY NEEDLE THOSE SIX SUITES DECLARE: %d DECLARED, %d BUILT, %d REFUSED.** "
            "%d reads, %d without an anchor, %d of %d anchors differing from the hint that found them."
            % (N['headline_sum'], N['enumerated'], N['draft_population'], N['draft_retirement'], N['retired'],
               len(N['wrong_arms']) if isinstance(N.get('wrong_arms'), list) else N['wrong_arms'],
               len(N['missing_sentences']) if isinstance(N.get('missing_sentences'), list) else N['missing_sentences'],
               N['copies_reproducing'], N['copies'], N['needles_declared'], N['needles_built'],
               N['needles_refused'], E['reads'], E['without_anchor'], E['anchors_differing'], E['reads']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A GATE HELPER IS NOT EVEN AN INSTRUMENT, LET ALONE A RESULT.** This act built a shared utility, counted eleven arms in three banks, classified them, ran six banked "
         "suites as copies and filed one trail entry. It computed nothing about the object and retired nothing in fact.",
         "**PRINT: PLACE-papers, ONE FILE.** OPEN_TRAILS.md gains **ONE APPEND-ONLY BLOCK** under its own mark, `%s` -- %d bytes, %d quotations every one built by the anchor tool from its own file, the "
         "working file a true prefix of what it was **AND OF ITS COMMITTED BLOB** (the reading BEFORE THE PUSH, which by b352's straddling rule is the one that carries). **NO ROW ABOVE TOUCHED.** "
         "**FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED** -- the order's *only if a row moves* is honoured by not writing. **NO BANKED SUITE WAS EDITED.** New shared "
         "tool tools/gate_needle.py in the relay repo, seven fixtures, both polarities. **THE HOOK AND THE MIRROR ARE OWED AND PAID.** Nothing in TECHNE-Core; no findings section edited; no roster row "
         "changed."
         % (T['entry'], T['grew'], len(T['quotes'])),
         "**NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED.** The trail entry OPENS a question and decides none: b358's grade stands as b358 left it, b361's decision stands as b361 left it, and "
         "b361 had already banked that its decision would move if H-CUSP moved. **NO ACT IS RE-VERDICTED:** b355, b356, b357, b360, b361 and b362 stand exactly as banked, and the one copy that does not "
         "reproduce changes none of them. **AND BOTH SEATS' EXPECTATIONS WERE SCORED:** the navigator's is **MET, with its stated reason met twice over** (two wrong arms, not one) and understated in two "
         "ways it did not foresee -- the population was never nine nor thirteen, and two of the four survivors are not defects at all; this seat's registered expectation (*the helper will build, its fixtures "
         "will hold, and it will be narrower than the species count suggests*) is **MET IN ALL THREE CLAUSES AND IS WORTH VERY LITTLE**, since the registration itself named the reason the third clause "
         "would hold -- **ARITHMETIC OVER ONE'S OWN BANKS IS NOT A MEASUREMENT** -- so a seat predicting its own draft was optimistic has predicted its own habit and not the world; **AND THE ONE THING IT "
         "DID NOT PREDICT IS THE ONE THING WORTH HAVING**, that the population itself was wrong. **THE VERDICT BRANCH TAKEN IS (BUILT AND FOUND NARROWER THAN ITS RULE), AND THE OTHER TWO ARE SHOWN "
         "UNREACHABLE RATHER THAN LEFT UNCLAIMED.**",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b363 -- ONE ROW: THE ANCHORED GATE ARMS, COUNTED AND NOT ASSERTED.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s' % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = (all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS)
          and 'NARROWER THAN THE RULE IT WAS PROPOSED UNDER' in ROWS[0][0]
          and 'COUNTED AND NOT TAKEN FROM THE DRAFT' in ROWS[0][1]
          and 'REFUSES TO EMIT IF THE TWO DISAGREE' in ROWS[0][1]
          and 'DECLARED DATA AND NOT INFERRED FROM PROSE' in ROWS[0][1]
          and 'ARE MISSING SENTENCES' in ROWS[0][1]
          and 'STILL A NEEDLE FOR THE WRONG QUESTION' in ROWS[0][1]
          and 'REPORTED AT FULL PROMINENCE AND NOT ADJUSTED' in ROWS[0][1]
          and 'APPEND-ONLY BLOCK' in ROWS[0][3]
          and 'NO ROW ABOVE TOUCHED' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'NO BANKED SUITE WAS EDITED' in ROWS[0][3]
          and 'NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED' in ROWS[0][4]
          and 'A SHARPER INSTRUMENT IS NOT A RESULT' in ROWS[0][5]
          and 'NO ARM WAS ACTUALLY RETIRED' in ROWS[0][5]
          and 'IS NOT A RATE AND NOT A FORECAST' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the count not taken from the draft, the refusal to emit, the declared classification, the two kinds, the wrong-arm limit, the control reported not adjusted, the append-only block, the ledger NOT written, no promotion : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT (%d) -- NOTHING WRITTEN.' % len(present))
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d ; row to append : %d' % (max(nums), start))
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[5] or 'M-2' not in r[5]]
    if over:
        print('  ### FAIL -- a row lacks its scope refusal or M-2')
        return 1
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
             for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
    new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    cells = [G.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
          and back.startswith(txt.rstrip(chr(10))))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s' % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
