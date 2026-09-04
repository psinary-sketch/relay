# -*- coding: utf-8 -*-
"""b312_correspondence.py -- TWO ROWS: THE IDENTIFICATION THAT FAILED, AND WHY IT WAS NOT SEEN.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS, AND IT IS THE SHARPEST THIS TABLE HAS CARRIED:**
###   ### **ROW ONE RECORDS A DISCREPANCY IN AN INSTRUMENT THE CORPUS HAS COMPUTED WITH FOR A
###     ### MONTH, AND A ROW LIKE THAT READS AS A VERDICT ON EVERYTHING THAT INSTRUMENT TOUCHED.**
###     ### It is not one. ### **THE ACT COMPARED TWO WRITTEN DEFINITIONS AND COMPUTED NOTHING**,
###     and the grade cell says so before it says anything else.
###   ### **ROW TWO EXPLAINS WHY A CROSS-CHECK PASSED, AND AN EXPLANATION READS AS AN EXCUSE OR AS
###     ### AN ACCUSATION.** ### It is neither: it is a derivation about where a check was taken.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE REMAINDER IS NOT THE SOURCE'S (b312)",

     "THE REMAINDER IS NOT THE SOURCE'S (b312): the corpus's `eps` and CC's `\u03b5` were unfolded "
     "to their base objects and compared constituent by constituent, artefact pinned by sha256 "
     "`b8e0b54a\u2026` BEFORE a word of it was read. **NINE CONSTITUENTS; EIGHT AGREE EXACTLY** "
     "\u2014 the mode family, the auxiliary vector, the analytic continuation, the outer "
     "coefficient `\u03bb\u00b2/(1\u2212\u03bb\u00b2)`, the interval from `1/\u03c1` to `1`, the "
     "integrand, the value zero at the identity, and the one-sided derivative. **THE NINTH IS THE "
     "SCALING ACTION'S NORMALIZATION EXPONENT, AND IT DISAGREES.** CC's own eq. (61) defines "
     "`(\u03d1(\u03bb)\u03be)(v) := \u03bb^(\u22121/2) \u03be(\u03bb^(\u22121) v)` \u2014 unitary, "
     "obtained by conjugating a unitary representation \u2014 so at the argument the remainder uses "
     "it is `\u03c1^(+1/2)`, and CC's Lemma 5.4 proof writes exactly that. The corpus's "
     "`qeps_layer.py` declares `\u03b8(a) f(x) = a^(1/2) f(x/a)` and its code applies `r ** -0.5`. "
     "**THE TWO FUNCTIONS THEREFORE DIFFER BY A FACTOR OF `\u03c1`, WHICH IS NOT A SCALAR.** "
     "VERDICT: **DIFFERENT.**",

     "**NO TERMINAL, AND THE SHADOW WAS EXPECTED TO BE NOTHING AND IS NOTHING** \u2014 a quotation "
     "is not decidable and a comparison of two analytic definitions is not finite-decidable. **THE "
     "DECISION IS MADE BY EXTRACTION, NOT BY THIS SEAT'S EYE**: `tools/b312_definitions.py` reads "
     "the sign off the RAW page text and the exponent off the corpus's own committed files, and "
     "its fixtures prove it can report EITHER answer before it is trusted. **AND THE ACT'S OWN "
     "LOCATOR IS MEASURED UNFIT FOR THIS QUESTION FIRST**: `b305_source.py`'s flattener strips "
     "every non-alphanumeric character, so `\u03c1^(+1/2)` and `\u03c1^(\u22121/2)` flatten to the "
     "SAME STRING \u2014 that is demonstrated, not asserted, and it is why this act has two tools "
     "instead of one.",

     "**NO PRINT. NOTHING COMPILED THIS ACT** \u2014 the profile stands unchanged at 475. "
     "`tools/b312_source.py` locates **17 fragments, 0 unlocated**, across pages 5, 22, 26, 27, "
     "31, 32, 47 and 52 of the pinned artefact. **THE SOURCE IS SELF-CONSISTENT AT THREE "
     "INDEPENDENT PLACES** \u2014 its definition (61) on page 22, its own worked unfolding of an "
     "inner product of exactly this shape on page 26, and its Lemma 5.4 proof on page 31 \u2014 "
     "**SO A TRANSCRIPTION SLIP IN THE SOURCE WOULD HAVE TO HAVE HAPPENED THREE TIMES, THE SAME "
     "WAY.** **AND THE CORPUS DISAGREES WITH ITSELF**: `qeps_layer.py`'s `Qeps` carries "
     "`r ** 0.5`, which AGREES with CC's eq. (99); and inside `b38_act10.py` the identity's TRACE "
     "side applies the square root of the scaling while its REMAINDER side applies `r ** -0.5`. "
     "**ONE IDENTITY, TWO CONVENTIONS, ONE FILE.**",

     "**A DECISION AT DEFINITIONS, AND NOTHING MORE THAN THAT.** **SCOPE, AND IT IS THE WHOLE OF "
     "THE ROW'S HONESTY: THIS ACT COMPARED TWO WRITTEN DEFINITIONS AND COMPUTED NO ARCHIMEDEAN "
     "NUMBER. IT DOES NOT CALL ANY BANKED MEASUREMENT WRONG, AND EVERY BANKED RESULT STANDS "
     "EXACTLY WHERE ITS OWN ACT LEFT IT, AT ITS OWN GRADE.** It does not decide whether the corpus "
     "meant the source's function and missed, or defined its own \u2014 **a corpus may define its "
     "own object; what it may not do is call that object the source's, and the header does** "
     "\u2014 because deciding that needs a computation this act may not run. The corpus's stated "
     "reason, that the convention is *forced by the supplied support law*, **DOES NOT REACH ITS "
     "CONCLUSION: THE SUPPORT CONDITION IS IDENTICAL UNDER BOTH CONVENTIONS, AND A SUPPORT "
     "CONDITION FIXES A DOMAIN, NOT AN AMPLITUDE.** The equation numbers are NOT settled either: "
     "the corpus cites *their (85)* and *eq (100)* where the pinned arXiv-v1 has (84) and (99), "
     "its header says *arXiv-v1 / Selecta numbering*, and the offset is uniform \u2014 consistent "
     "with an edition shift; **THE SELECTA EDITION IS NOT PINNED BY THIS CORPUS, SO THIS ACT "
     "CANNOT CHECK IT AND DOES NOT.** **COMPONENT 3'S ENTAILMENT DOES NOT RUN** \u2014 the order "
     "runs it on SAME only \u2014 so no claim is made about the imbalance's cause. NO AGGREGATION "
     "IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED under b310's cap. h2 stands exactly "
     "where the deposit left it.",

     "current"),

    ("A CHECK TAKEN AT A ZERO CANNOT SEE A FACTOR (b312)",

     "A CHECK TAKEN AT A ZERO CANNOT SEE A FACTOR (b312): the corpus's one cross-check of its "
     "remainder against the source is the one-sided derivative at the identity, which its own "
     "header derives and CC's Lemma 5.4 states; **THE TWO AGREE, AND THE AGREEMENT IS EMPTY.** "
     "Write the common integral as `F(\u03c1)`, so the corpus's function is "
     "`\u03c1^(\u22121/2) F(\u03c1)` and the source's is `\u03c1^(+1/2) F(\u03c1)`. The interval "
     "of integration is empty at the identity, so `F(1) = 0`; the derivative of "
     "`\u03c1^s F(\u03c1)` there is `s F(1) + F'(1)`, which is `F'(1)` **FOR EVERY `s` "
     "WHATEVER.** **A CROSS-CHECK TAKEN AT A ZERO OF THE FUNCTION CANNOT SEE A MULTIPLICATIVE "
     "FACTOR THAT IS FINITE AND NONZERO THERE**, and that is the whole of why a corpus checking "
     "itself against its source found agreement.",

     "**NO TERMINAL.** The derivation is three lines of calculus and is the bank's, UNCOMPILED. "
     "**WHAT IS MACHINE-CHECKED IS NOT THE DERIVATION BUT THE INPUT TO IT**: that `F(1) = 0` is "
     "the corpus's own documented property of its integrand, quoted from `qeps_layer.py`'s header, "
     "and that the two exponents are what they are is `b312_definitions.py`'s extraction with its "
     "fixtures. **THE STEP FROM THOSE TO THE INVISIBILITY IS THIS SEAT'S AND IS NOT CERTIFIED.**",

     "**NO PRINT.** The other channel is checked too, as the order required \u2014 **the "
     "archimedean term's sign convention against the corpus's banked atlas rather than assumed.** "
     "`carto_atlas.py`'s own header records the explicit formula and then says of the sign "
     "*[sign fixed BY the E2 calibration]*, and two lines above: *DISCLAIMED REGISTER: a "
     "computation maps and cannot prove. No sign claim is made.* **SO THE THING TO BE CHECKED "
     "AGAINST IS ITSELF A CALIBRATION.** That is not a complaint about the atlas \u2014 the atlas "
     "disclaims exactly this and always has \u2014 **IT IS THE REASON A FACTOR IN A NEIGHBOURING "
     "TERM WOULD NOT HAVE ANNOUNCED ITSELF THROUGH THAT CHANNEL EITHER.**",

     "**A DERIVATION ABOUT WHERE A CHECK WAS TAKEN. NEITHER AN EXCUSE NOR AN ACCUSATION.** "
     "**SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: it explains why one particular check was "
     "insensitive to one particular factor. IT IS NOT A CLAIM THAT ANY OTHER CHECK THE CORPUS RAN "
     "WAS INSENSITIVE, AND IT AUDITS NONE OF THEM.** **WHAT IT OBLIGATES IS FILED, NOT RUN: "
     "`W-ORD-REMAINDER-EXPONENT`, whose exact check is named so the next act need not invent it "
     "\u2014 re-run the corpus's own identity with the remainder's exponent flipped and nothing "
     "else touched, and compare the residue against the banked one. THAT IS A COMPUTATION, AND "
     "THIS ACT MAY NOT RUN IT.** It inherits `W-ORD-ARCH-NORM-READING`, which b301 filed and which "
     "is still live. **AND THE NAVIGATOR'S REGISTERED EXPECTATION IS REFUTED** \u2014 *SAME "
     "FUNCTION up to the normalization the corpus records by a factor* \u2014 refuted in the "
     "region its own hedge pointed at, but not covered by it: *up to a factor* is a scalar's "
     "licence and the factor here is `\u03c1`. **THIS IS THE THIRD ACT RUNNING WHOSE SEALED "
     "PREDICTION FAILED AT A NORMALIZATION.** NO GRADE IS MOVED. NO ACT IS RE-VERDICTED. NO "
     "AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the "
     "deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b312 -- THE IDENTIFICATION\'S ROW, AND THE INVISIBILITY\'S.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1

    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s'
          % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0

    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s'
          % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('COMPUTED NO ARCHIMEDEAN NUMBER' in r1[4]
          and 'DOES NOT CALL ANY BANKED MEASUREMENT WRONG' in r1[4]
          and 'ENTAILMENT DOES NOT RUN' in r1[4])
    g2 = ('NEITHER AN EXCUSE NOR AN ACCUSATION' in r2[4]
          and 'IT AUDITS NONE OF THEM' in r2[4]
          and 'MAY NOT RUN IT' in r2[4])
    print('  row 1 refuses to be read as a verdict on a measurement : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses the audit reading and files rather than runs : %s  %s'
          % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1

    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(c == 6 for c in cellcounts)
          and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
