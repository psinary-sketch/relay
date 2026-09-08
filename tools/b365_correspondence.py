# -*- coding: utf-8 -*-
"""b365_correspondence.py -- ONE ROW: THE OWED READ, PAID.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a grade had moved; as if a
### proof had been verified; as if the theorem's HYPOTHESIS had been shown to cover the case (it has not --
### the paper APPLIES the theorem to the case, which is weaker and is what the quotations support); as if
### the threshold had been ruled; or as if the mint had shipped an arm.
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
    "**SCOPE: NO GRADE MOVES IN EITHER DIRECTION.** H-CUSP stands where b358 left it and b361's decision stands where b361 left it; A READ THAT SUPPORTS A GRADE DOES NOT RAISE IT, and the cap made that "
    "absolute before the read began. THE SUPPORT IS BY APPLICATION AND NOT BY QUANTIFIER: this act does NOT claim Theorem 5.1's hypothesis line covers the corpus's object -- it claims the paper APPLIES the "
    "theorem to that object and computes its constant for it, which is weaker and is what the quotations support. NO PROOF IS VERIFIED: this act read what the paper states, checked no derivation, and could "
    "not; A LOCATED STATEMENT IS NOT A PROVED ONE. b358's CIRCULARITY FINDING IS UNTOUCHED, and nothing here bears on the zero channel. NO SOURCE WAS FETCHED and the rendering seam stands: a hash on a PDF "
    "does not certify that its extracted text is a faithful rendering of it, so this act's finding is a finding about the rendering on disk. THE THRESHOLD IS PROPOSED AND NOT RULED, and until it is ruled THE "
    "FOLD IS DUE remains a judgement. THE MINT SHIPS NO ARM and claims no audit of the record for wrong arms. NOTHING WAS COMPUTED ABOUT THE OBJECT. NO ACT IS RE-VERDICTED. NO SUITE, BANK OR RUN FILE OF ANY "
    "OTHER ACT IS EDITED. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO FACE IS "
    "PROMOTED AND NO GRADE IS CONFERRED BY A SEAT. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the "
    "patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's "
    "ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b365_reads.json'), encoding='utf-8'))
    R = json.load(io.open(os.path.join(D, 'b365_read.json'), encoding='utf-8'))
    M = json.load(io.open(os.path.join(D, 'b365_mint.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b365_filing.json'), encoding='utf-8'))
    m = ("THE CONVENTION IS **%s** AND THE SOURCE WORKS THE EXCEPTIONAL CASE ITSELF, so the archimedean channel's unconditional status is **%s** -- and the support is **BY THE PAPER'S OWN APPLICATION AND NOT "
         "BY ITS OWN QUANTIFIER** (b365)" % (R['convention'], R['localization']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE THE READ**, on the audit's own exit code, with the three branches carried verbatim from the adopted draft and **THE PRE-LOCK SEARCH DECLARED ON THE "
            "LOCKED FACE** rather than concealed. **(i) THE CONVENTION IS LOCATED AND THE PAPER NAMES IT AS ONE:** *This convention is forced if we wish to have entire functions in all cases, for we must re "
            "move the poles at s = 0 and s = 1 for the case πtriv*, and it draws the consequence itself -- *It follows that ξ(s,π) is an entire function in all cases*. **(i-b) AND IT CARRIES THE EXCEPTION "
            "THROUGH ITS OWN CUSPIDAL-HYPOTHESIS RESULTS**, which a hypothesis line alone would have hidden: Lemma 4.3 is stated for a cuspidal representation and applied to the exception by a Remark printed "
            "beneath it, and Lemma 4.2's hypothesis says cuspidal while its own conclusion defines a term that is 1 exactly when the representation is the trivial one. **(ii) THE CONSTANT AND THE ERROR TERM "
            "ARE DERIVED INDEPENDENTLY OF CUSPIDALITY**: C1 depends on N and the conductor alone, the implied constant is ABSOLUTE in the paper's own word, and **THE PAPER PRINTS C1 FOR THE EXCEPTION AS A "
            "NUMBER** in the paragraph after Theorem 5.1. **A PAPER THAT COMPUTES A THEOREM'S OWN CONSTANT FOR A CASE IS APPLYING THE THEOREM TO THAT CASE.** **(iii) AND WHAT IN THIS RECORD RESTS ON IT IS A "
            "NEGATIVE ANSWER, WHICH IS WHY IT HAD TO BE LOOKED FOR:** a bounded pass found %d of the ledger's %d blocks citing b358 or b361, every one an update to row %s, and **NO BANKED NUMBER OF THIS "
            "RECORD IS COMPUTED FROM THEOREM 5.1's CONSTANT** -- what rests on the theorem is a statement about conditionality, not an arithmetic value. **AND THE HONEST QUALIFICATION, WHICH IS NOT A HEDGE:** "
            "the theorem's hypothesis line still says irreducible cuspidal and the paper never re-states it to admit the exception; what it does instead is APPLY it. %d reads, %d without an anchor, %d of %d "
            "anchors differing from the hint that found them, %d source lines located at the pinned rendering."
            % (len(R['faces_blocks']), R['faces_headings'], ', '.join(R['faces_rows']) or 'none',
               E['reads'], E['without_anchor'], E['anchors_differing'], E['reads'], E['source_lines']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A READ IS NOT A RESULT.** This act located a convention, quoted it, decided one question about a theorem's scope, passed over three ledger blocks and paid a trail "
         "entry. It computed nothing, verified no proof and moved no grade.",
         "**PRINT: PLACE-papers, ONE FILE.** OPEN_TRAILS.md gains **ONE APPEND-ONLY BLOCK** naming `%s` as **%s** -- %d bytes, every quotation built by the anchor tool from the pinned rendering with the "
         "scaffolding equality checked under the shared normaliser, the working file a true prefix of what it was **AND OF ITS COMMITTED BLOB** (the reading BEFORE THE PUSH, b352's rule). **THE BLOCK b363 "
         "WROTE IS NOT EDITED.** **FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** **TECHNE-Core: ONE MODULE, `%s`, COMMITTED LOCALLY AT `%s` AND NOT PUSHED**, as every "
         "module since b330 -- a JUDGEMENT RULE WITH NO MECHANIZABLE HALF, and the absence of one is its content. **THE HOOK AND THE MIRROR ARE OWED AND PAID.** No findings section edited; no roster row "
         "changed." % (F['entry'], F['status'], F['grew'], M['module'], M['techne_head']),
         "**NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED.** **AND THE NAVIGATOR'S EXPECTATION IS REFUTED IN ITS FIRST CLAUSE:** it read *the source does not state the exceptional case*, and the "
         "source states it, applies its lemmas to it by name, and computes the theorem's constant for it -- so the proposed grade IMPORTED-ON-A-HYPOTHESIS-NOT-MET never arises and no further source needs "
         "locating. **THAT EXPECTATION WAS THE READING A CAREFUL PERSON WOULD MAKE FROM THE HYPOTHESIS LINE ALONE**, which is what makes the refutation useful rather than merely a score: **A THEOREM'S SCOPE "
         "IS WHAT ITS PAPER DOES WITH IT, NOT ONLY WHAT ITS QUANTIFIER SAYS.** **THIS SEAT'S IS HALF MET AND HALF REFUTED, AND THE REFUTED HALF IS THE HALF THAT MATTERED** -- and the met half was bought by a "
         "pre-lock search declared on the locked face, so it is worth nothing. **AND THE THRESHOLD IS PROPOSED AT 9 ACTS AND NOT RULED**, with the spread 4 to 16 printed beside it as the argument against "
         "taking it too seriously: a habit that varies by a factor of four is not a rule that was being followed.",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b365 -- ONE ROW: THE OWED READ, PAID.')
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
          and 'BY THE PAPER' in ROWS[0][0] and 'NOT \nBY ITS OWN QUANTIFIER'.replace(chr(10), '') in ROWS[0][0].replace(chr(10), '')
          and 'LOCKED BEFORE THE READ' in ROWS[0][1]
          and 'THE CONVENTION IS LOCATED' in ROWS[0][1]
          and 'CARRIES THE EXCEPTION' in ROWS[0][1]
          and 'DERIVED INDEPENDENTLY OF CUSPIDALITY' in ROWS[0][1]
          and 'NEGATIVE ANSWER' in ROWS[0][1]
          and 'NOT A HEDGE' in ROWS[0][1]
          and 'APPEND-ONLY BLOCK' in ROWS[0][3]
          and 'IS NOT EDITED' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'NOT PUSHED' in ROWS[0][3]
          and 'REFUTED IN ITS FIRST CLAUSE' in ROWS[0][4]
          and 'NOT ONLY WHAT ITS QUANTIFIER SAYS' in ROWS[0][4]
          and 'NO GRADE MOVES IN EITHER DIRECTION' in ROWS[0][5]
          and 'BY APPLICATION AND NOT BY QUANTIFIER' in ROWS[0][5]
          and 'NO PROOF IS VERIFIED' in ROWS[0][5]
          and 'PROPOSED AND NOT RULED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the convention located, the exception carried, the constant independent, the negative answer, the qualification, the append-only block, the prior block not edited, the module not pushed, the expectation refuted, no grade moved : %s' % g1)
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
