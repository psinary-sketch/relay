# -*- coding: utf-8 -*-
"""b405_desk_bank.py -- THE DESK, ROW `U1` RESTATED, THE TRAIL BLOCK, THE ROW, THE KEY, THE BANK.

### ### **`(R24)` IS EXECUTED INSIDE THE COLUMN LAW AND NOT BY AMENDING IT.** ### The ledger fixes
### seven columns for every table line in the file; a row cannot gain a column alone, so the two new
### coordinates go in as LABELLED FIELDS inside cell `5`, exactly as `b401` and `b404` entered their
### sites. ### **THE COLUMN COUNT OF EVERY LINE IS RE-MEASURED AFTER THE WRITE AND MUST NOT MOVE.**
###
### ### **TWO CELLS ARE APPENDED TO AND THE OTHER FIVE MUST COME BACK BYTE-IDENTICAL**, checked cell
### by cell against the PRE-ACT blob -- `HEAD` before the push, `HEAD~1` after it, ### **THE
### ### REFERENCE NAMED AND NOT ONLY THE SIDE** (`b401`'s species, sharpened at `b403`).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                  # noqa: E402
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b405 the row law restated: kind and witness, and the countermodel read whole -->'
PRIOR = '<!-- b404 the fifth site, the sixth candidate, and the row law strained -->'
BANKOUT = os.path.join(D, 'b405_the_rows_law_restated.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


SEALTXT = io.open(os.path.join(D, 'b405_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b405_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b405_components.txt'), encoding='utf-8').read()
EXTR = io.open(os.path.join(D, 'b405_extract.txt'), encoding='utf-8').read()
READS = EXTR.count('  ### ') - EXTR.count('  ### ANCHOR MISS') - EXTR.count('  ### BLOCK MISS')
MISSES = EXTR.count('### ANCHOR MISS') + EXTR.count('### BLOCK MISS')

DEPOSIT_REFUSAL = (
    'the deposit, section 27.3: *"compiling the *structure* of the one-premise-in-five-registers '
    'claim while deliberately **not** compiling the cross-register equivalences, since to compile '
    '\'discharge one and you discharge all five\' would be to compile RH-equivalence itself."*')

# ### ==================================================================================================
# ### ### **THE APPEND TO CELL 5 -- THE TWO COORDINATES, AS LABELLED FIELDS.**
# ### ==================================================================================================
CELL4_ADD = (
    ' ### **THE ROW GAINS TWO COORDINATES, added 2026-09-10 (b405) under RULING `(R24)`, the '
    'author’s: `KIND`, as b404 minted it, and `WITNESS`, the shared witness that would close the '
    'site or `NONE KNOWN`.** '
    '*They are entered as LABELLED FIELDS inside this cell and NOT as new columns: the ledger’s own '
    'COLUMN LAW fixes seven columns and says rows are written only by `b327_faces_row.py`, so a row '
    'cannot gain a column alone and this act will not give 159 table lines an eighth cell to give '
    'one row one. If the author wants true columns that is a ledger-wide act.* '
    '### **`WITNESS` IS SOURCED FROM THE COMPILED THEOREM AND FROM NOWHERE ELSE.** A shared witness '
    'is what `SIDELvConservation.T3.T3prime_shared_witness` says it is, at `SIDE-lv-conservation` '
    '`v0.10.0 = 93c27ec` — TWO CLAUSES ON ONE OBJECT IN THE FAMILY’S OWN PARAMETER SPACE: '
    '`h1 : ∀ C ∈ 𝒞, C Phi` (**SHAREDNESS** — one object satisfies every member) and '
    '`h2 : mellin Phi (s / 2) ≠ 0` (**NON-DEGENERACY** — the quantity that must not vanish does not '
    'vanish at it). Its companion `T3.T3doubleprime_general_commutation_fails` is why both are '
    'needed: two integrands agreeing on `Ioi 0` and differing at `t = -1` give every member its own '
    'witness and no single `Φ` for all. **PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.** '
    'Both profiles printed at the pin: `[propext, Classical.choice, Quot.sound]`; the one `sorry` '
    'sits at the intermediate `T3_perClass_to_combinations` and at neither terminal. '
    '**A CELL BELOW NAMES WHAT A WITNESS WOULD HAVE TO BE. NAMING THAT IS NOT CLAIMING ONE EXISTS, '
    'AND IS NOT A BRIDGE TO ANY OTHER SITE.** '
    '### **`(i)` — KIND: NOT EMPTY. WITNESS: `UNSTATED`.** The quantifiers are *"UNOWNED, and they '
    'are the clause"* — a live open part. And the witness form does not transpose here at all: the '
    'entry’s quantifiers run over the class and, through the explicit formula, over the zeros — a '
    '`∀` with no `∃` inside it, and the shared-witness form is a repair for `∀∃ ⟹ ∃∀`. '
    '**THE CELL IS NOT `NONE KNOWN`, BECAUSE THAT WOULD IMPLY A WITNESS IS THE RIGHT KIND OF THING '
    'TO LOOK FOR HERE.** '
    '### **`(ii)` — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.** The coordinate is *"BOUNDED BY A '
    'MEASUREMENT and not by an argument"*, which is live and not empty. The witness would be ONE '
    'argument serving every height, against a method that produces zeros one at a time — and b351 '
    'says the record has none in the sentence that sets this coordinate against the one that '
    'closed: *"one convergent series did what sixty boxes of argument principle could not do for '
    'the height"*. '
    '### **`(iii)` — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.** The witness would be ONE `g` serving '
    'every width, and **THIS IS THE ONE SITE OF THE SIX WHOSE OWN BANKED TEXT SUPPLIES THE INNER '
    'EXISTENTIAL IN THE THEOREM’S SHAPE**: Boas–Kac, as b353 quotes it, reads *"There exists g in '
    'Cc^infty(R) with support in [-A/2, A/2] such that f = g * g^*"*, and that `∃g` is indexed by '
    '`A`. Its two clauses read: `h1`, one `g` works at every `A`; `h2`, the `f` it builds is not '
    'the degenerate one. No such `g` is named. '
    '### **`(iv)` — KIND: NOT EMPTY. WITNESS: `UNSTATED`.** What the record holds here is TEN '
    'VALUES indexed by the width, not ten existential witnesses, and what it needs is one statement '
    'uniform in `a`; a uniform bound is not an object in the family’s parameter space. **AND THIS '
    'IS WHERE THE SHARED INDEX STOPS MEANING A SHARED SHAPE**: `(iii)` and `(iv)` share the support '
    'width, which b401 put on the face of its own entry — and `(iii)` carries the existential while '
    '`(iv)` does not. '
    '### **`(v)` — KIND: `(b)`. WITNESS: `NONE KNOWN`.** The KIND cell is a transcription, not a '
    'reading: the entry declares *"(v) IS KIND (b)"* itself, and is the only one of the six that '
    'declares a kind at all. The witness would be ONE CONSTANT SERVING EVERY REPRESENTATION — this '
    'site IS a `∀∃ ⟹ ∃∀`, the implied constant being the inner existential — and the entry names '
    'the shape by contrast without supplying the witness, since Theorem 5.1’s absolute constant is '
    'a witness for the ARCHIMEDEAN side and not for this one. '
    '### **`(vi)` — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.** A residue filed as the whole of the '
    'remaining weight is the opposite of empty. And **THIS IS THE ONLY SITE OF THE SIX WHOSE OWN '
    'TEXT NAMES BOTH CLAUSES OF THE WITNESS FORM**: `h1` is *"consistent at every finite modulus"*; '
    '`h2` is the *"(positive global density)"* the passage must reach. It names no object '
    'satisfying them — which is why b404 reported the shape and refused the bridge. '
    '### **THE TALLY, PRINTED SO NO READER HAS TO COUNT: KIND — 5 NOT EMPTY, 1 `(b)`, 0 `(a)`, 0 '
    'UNSTATED. WITNESS — 4 `NONE KNOWN`, 2 `UNSTATED`, AND `0` SITES WITH A WITNESS FOUND.** '
    '### **AND THE NAVIGATOR NAMED TWO WITNESSES AS ALREADY FOUND; NEITHER SURVIVES THE SITES’ OWN '
    'TEXT.** The abscissa’s convergent sum is a witness for no site of this row **because the '
    'abscissa is not a site of this row** — it is the coordinate that CLOSED (b351: *"THE ABSCISSA '
    'WAS ALREADY CLOSED, AND HAS BEEN SINCE b326"*) and was therefore never entered. The finite '
    'side’s zero is not a shared witness across places either: in `B329.finite_side_silence` the '
    'clause carrying the zero is written `((p, n) ∈ cells → ballQ p n * sumAN p n = sumAQ p n)` — '
    'a membership test against a SEVEN-CELL DECIDED LIST discharged by `decide` — while the two '
    'clauses that ARE general in `p` carry no zero. **THE THEOREM IS GENERAL WHERE IT IS EMPTY OF '
    'THE ZERO AND DECIDED WHERE IT IS NOT.** Adding an eighth place adds a new obligation, so there '
    'is no cross-place claim in that clause at all: the same answer arrived at separately seven '
    'times is not one witness shared. '
    '### **THE SIX READ AS SIX, BY THREE TESTS FIXED BEFORE THE READ:** writes its missing '
    'statement — `4` of 6 (`iii`, `iv`, `v`, `vi`); files a residue — `1` of 6 (`vi`); declares its '
    'kind — `1` of 6 (`v`). **ENTRIES DOING BOTH OF THE FIRST TWO: ONE**, which is exactly what '
    'this row’s own refusal cell already said — *"and which **one of the six already has**"* — so '
    'the reading that `(iv)` also did was refutable by a sentence in the very cell it was about, '
    'and is refuted here. `(iv)`’s *"A FOURTH INSTANCE OF THE OBSTRUCTION AND NOT A CRACK IN IT"* '
    'says the obstruction is REAL and never says what fraction of the problem the missing statement '
    'carries, **AND SAYING AN OBSTRUCTION IS REAL IS NOT FILING A RESIDUE.** Where an entry names '
    'no statement, its residue test is **VACUOUS** and is recorded as vacuous rather than as a '
    'plain NO. '
    '### **NO NEW MEASUREMENT WAS TAKEN TO FILL ANY CELL, NO CELL WAS FILLED FROM THE NAVIGATOR’S '
    'PARAGRAPH OR FROM ANOTHER SITE, AND NO BRIDGE IS TYPED BETWEEN ANY TWO OF THE SIX.**')

# ### ==================================================================================================
# ### ### **THE APPEND TO CELL 7 -- THE REFUSAL, VERBATIM, AND WHAT IT CANNOT SAY.**
# ### ==================================================================================================
CELL6_ADD = (
    ' ### **RESTATED 2026-09-10 (b405) UNDER `(R24)`, AND THE CLAUSE IS NOT TOUCHED.** The refusal '
    'stands word for word and governs six: *NOTHING IS CLAIMED ABOUT THE EQUIVALENCE OF* them; *a '
    'row naming things that look alike is exactly where an equivalence gets compiled by accident*; '
    'this row *names a resemblance of SHAPE and types no bridge between* them, *in either '
    'direction*; *three separate obstructions that rhyme are three obstructions* — and so are six. '
    '**b405 types no bridge between any two of the six, and types none between the compiled '
    'countermodel and any instance of the shape it is about.** '
    '### **AND THE ONE THING THIS ACT ADDS IS A FINDING ABOUT THE CLAUSE ITSELF, NOT A CHANGE TO '
    'IT.** The clause was put ONE question — *can it distinguish a site empty in KIND (a) from one '
    'empty in KIND (b)?* — under a predicate fixed before it was asked: a clause can express a '
    'distinction between two states of ONE site only if some predicate in it has ONE site for its '
    'subject. **ITS FOUR SENTENCES HAVE, FOR THEIR SUBJECTS: the three; a row naming three things; '
    'a row and the pair at each end of a bridge; three obstructions. `0` OF `4` HAVE ONE SITE FOR A '
    'SUBJECT.** ### **SO THE ANSWER IS `NO`, AND THE REASON IS STRUCTURAL RATHER THAN CARELESS: '
    'EVERY CLAUSE OF THE REFUSAL IS BINARY OR HIGHER — ABOUT PAIRS, ABOUT THE SET, ABOUT THE ROW — '
    'WHILE `(a)` VERSUS `(b)` IS A UNARY PROPERTY OF ONE SITE. A BINARY LAW CANNOT EXPRESS A UNARY '
    'DISTINCTION, AND NO AMOUNT OF RESTATING IT WILL MAKE IT.** **THIS IS NOT A DEFECT IN THE '
    'SITES; IT IS A MISSING COORDINATE IN THE ROW**, which is what `(R24)` supplies and why the '
    'clause is restated rather than retired. '
    '### **THE STRAIN b404 REPORTED IS NOT RELIEVED AND IS NOT RESTATED AWAY.** Of the relief b404 '
    'routed — every entry naming its missing statement exactly and filing its residue as the whole '
    'of the remaining weight — the measurement is now on the face of the row: `4` of 6 name the '
    'statement and `1` of 6 files the residue. **THE ROUTED RELIEF IS STILL ROUTED AND STILL NOT '
    'APPLIED: b405 REWRITES NO ENTRY.** '
    '### **AND THE ROUTE FROM THE COMPILED SHAPE TO ANY INSTANCE IS PRICED HERE AND NOT TAKEN.** To '
    'carry `T3′` to a site one would need an identification of that site’s family with the '
    'theorem’s `Set Coupling` and of its parameter space with `ℝ → ℂ`, and then both clauses at '
    'that identification; **not one of the six sites is stated in those terms, and none of the six '
    'supplies a candidate shared witness — six sites, zero candidates.** And a build buys nothing: '
    'both terminals are already compiled and both profiles already printed, so **THE ROUTE IS '
    'PRICEABLE WITHOUT A BUILD**, which refutes the expectation that it was not. What the route’s '
    'own text puts at its second clause is quoted and not endorsed — the corpus’s own archived '
    'trails line reads *"`T3prime_shared_witness` with `h1 : ∀ C ∈ 𝒞, C Phi` … **and** `h2 : mellin '
    'Phi (s/2) ≠ 0` (open, RH-strength)"* and calls that `h2` *"the same h2 of §27.3’s five '
    'registers"*. **THIS ROW MAKES NO CLAIM ABOUT `h2` IN EITHER DIRECTION. QUOTING A HYPOTHESIS IS '
    'NOT ASSERTING IT, AND h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.** '
    'THE DEPOSIT’S REFUSAL GOVERNS THIS ENTRY AS IT GOVERNS THE LEDGER: ' + DEPOSIT_REFUSAL + ' '
    'NOTHING IS PAID HERE, NO GRADE IS CONFERRED, AND NO EQUIVALENCE IS COMPILED.')

DESK = [
    ('the four open lists (refs unnameable; grades on an absent declaration; undated figures; '
     'uncited bibliography entries)', 'STANDING',
     'None fires on this act. ### The triggers are unchanged and printed in the closing.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane. ### **A BLOCK ON THE WORK IS NOT AN ABSENCE OF A '
     'TRIGGER.**'),
    ('W-ORD-E0-RANK-PROPAGATION', 'STANDING', 'No grade moves in this act.'),
    ('b321’s face -- the two-route prime-power convention disagreeing at closed endpoints',
     'STANDING', 'ROUTED at b400 and still routed. ### It moves no value.'),
    ('SIDE-window’s missing pre-push guard', 'STANDING',
     'ROUTED at b403. ### That repository is not on the four-repo roster.'),
    ('the KINDS write-list shortfall at b400', 'STANDING',
     'ROUTED. ### This act’s own write list is built as KINDS and its arms re-measure it.'),
    ('the keystone’s widened no-Mathlib claim at `c66f3c5`', 'STANDING',
     'ROUTED at b404 and not repaired here. ### An import line is not a measurement.'),
    ('SIDE-effects’ absent printed axiom profile', 'STANDING',
     'ROUTED at b404. ### The lane is PARKED and nothing is built.'),
    ('the row’s own restatement into residue form', 'STANDING',
     'ROUTED at b404. ### b405 MEASURES how far the row is from that form -- 4 of 6 name the '
     'statement, 1 of 6 files the residue -- and rewrites no entry.'),
    ('(R24): row U1 restated, not retired -- the two coordinates', 'CLOSE',
     'EXECUTED. ### KIND and WITNESS entered as labelled fields inside cell 5, the refusal verbatim, '
     'six KIND cells and six WITNESS cells filled from the sites’ own text, UNSTATED where the text '
     'does not support a fill, and the column law obeyed rather than amended.'),
    ('the row’s law: restated or retired', 'CLOSE',
     'DECIDED BY THE AUTHOR, NOT BY THIS SEAT. ### (R24) rules RESTATED, and the act executes it '
     'and prices nothing it was not asked to price.'),
    ('the (a)/(b) distinction’s home in the row', 'CLOSE',
     'FOUND. ### The refusal clause cannot carry it -- 0 of 4 predicates are unary -- so it is a '
     'MISSING COORDINATE and is now a coordinate.'),
    ('the shape-to-instance route', 'STANDING',
     'PRICED AND NOT TAKEN. ### Six sites, zero candidate witnesses; the identification is the whole '
     'price; a build buys nothing. ### **THE ROUTE STAYS OPEN AND UNTAKEN.**'),
    ('the navigator’s two named witnesses', 'CLOSE',
     'SCORED AND BOTH DECLINED. ### The abscissa is not a site of this row; the finite side’s zero '
     'is per-cell over a seven-cell decided list. ### Neither is filed against a nearby site to keep '
     'a count up.'),
    ('M-2', 'STANDING', 'OWED and stays owed. ### No aggregation is stated.'),
    ('h2', 'STANDING',
     '**WHERE THE DEPOSIT LEFT IT.** ### The act quotes the record’s identification of the '
     'theorem’s second clause with it and claims nothing in either direction.'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES FOUR ITEMS AND LEAVES THE REST STANDING.**')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 1500), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0)


def column_shape(text):
    """### **EVERY TABLE LINE'S COLUMN COUNT, SO A RESTATED CELL CANNOT MOVE ONE.**"""
    return [ln.rstrip().count('|') for ln in text.split(chr(10)) if ln.startswith('|')]


def do_faces():
    before = io.open(FACES, encoding='utf-8', newline='').read()
    shape_before = column_shape(before)
    lines = before.split(chr(10))
    idx = [i for i, ln in enumerate(lines) if ln.startswith('| U1 |')]
    if len(idx) != 1:
        rec('  ### HARD FAILURE -- expected exactly one `U1` row, found %d.' % len(idx))
        return False, 0
    i = idx[0]
    if '(b405)' in lines[i]:
        rec('  ### ALREADY FILED -- the b405 segments are present. ### NOTHING APPENDED.')
        return True, 2
    oldc = GD.split_cells(lines[i])
    rec('  ### the row splits into %d cells on its UNESCAPED pipes' % len(oldc))
    if len(oldc) != 7:
        rec('  ### HARD FAILURE -- expected 7 cells.')
        return False, 0
    for add in (CELL4_ADD, CELL6_ADD):
        if GD.raw_pipes(add):
            rec('  ### HARD FAILURE -- an appended cell carries an UNESCAPED pipe.')
            return False, 0
    newc = list(oldc)
    newc[4] = oldc[4].rstrip() + CELL4_ADD + ' '
    newc[6] = oldc[6].rstrip() + CELL6_ADD + ' '
    lines[i] = '|' + '|'.join(newc) + '|'
    after = chr(10).join(lines)
    open(FACES + '.tmp', 'wb').write(after.encode('utf-8'))
    os.replace(FACES + '.tmp', FACES)
    back = io.open(FACES, encoding='utf-8', newline='').read()
    bl, al = before.split(chr(10)), back.split(chr(10))
    ok = (len(bl) == len(al))
    untouched = sum(1 for a, b in zip(bl, al) if a == b)
    rec('  ### lines %d -> %d ; UNCHANGED %d of %d' % (len(bl), len(al), untouched, len(bl)))
    ok = ok and untouched == len(bl) - 1
    shape_after = column_shape(back)
    same_shape = (shape_before == shape_after)
    rec('  ### ### **TABLE LINES %d ; COLUMN COUNTS UNCHANGED ON EVERY ONE : %s**'
        % (len(shape_after), same_shape))
    rec('  ### **(R24) GAVE THE ROW TWO COORDINATES AND THE LEDGER NO NEW COLUMN.**')
    ok = ok and same_shape
    backc = GD.split_cells(al[i])
    ok = ok and len(backc) == 7
    for k in range(7):
        if k in (4, 6):
            good = backc[k].startswith(oldc[k].rstrip()) and len(backc[k]) > len(oldc[k])
            rec('      cell %d  APPENDED TO : prior text a TRUE PREFIX : %-5s   %d -> %d bytes'
                % (k, good, len(oldc[k].encode('utf-8')), len(backc[k].encode('utf-8'))))
        else:
            good = backc[k] == oldc[k]
            rec('      cell %d  UNTOUCHED   : BYTE-IDENTICAL : %s' % (k, good))
        ok = ok and good
    for lbl, cond in (
            ('the row still reads `U1`', al[i].startswith('| U1 |')),
            ('the two coordinates are named', 'THE ROW GAINS TWO COORDINATES' in al[i]),
            ('the column law is obeyed not amended', 'cannot gain a column alone' in al[i]),
            ('the witness form is sourced from the theorem',
             'h2 : mellin Phi (s / 2) ≠ 0' in al[i]),
            ('six KIND cells are present',
             all(('**`(%s)` — KIND' % s) in al[i]
                 for s in ('i', 'ii', 'iii', 'iv', 'v', 'vi'))),
            ('the tally is printed', 'KIND — 5 NOT EMPTY, 1 `(b)`, 0 `(a)`' in al[i]),
            ('zero witnesses found', '`0` SITES WITH A WITNESS FOUND' in al[i]),
            ('the abscissa is declined', 'the abscissa is not a site of this row' in al[i]),
            ('the finite side is declined', 'SEVEN-CELL DECIDED LIST' in al[i]),
            ('the refusal is restated', 'types no bridge between' in al[i]),
            ('the unary/binary finding is on the face', 'A BINARY LAW CANNOT EXPRESS A UNARY'
             in al[i]),
            ('the missing coordinate is named', 'MISSING COORDINATE IN THE ROW' in al[i]),
            ('the route is priced not taken', 'THE ROUTE IS PRICEABLE WITHOUT A BUILD' in al[i]),
            ('h2 is left where it is', 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT' in al[i]),
            ('the deposit refusal is quoted',
             'deliberately **not** compiling the cross-register' in al[i])):
        ok = ok and cond
        rec('      %-46s : %s' % (lbl, cond))
    rec('  ### ### **%s**' % ('PASS' if ok else '### FAIL ###'))
    return ok, 2


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b405 — the row’s law restated under (R24), and the compiled countermodel read whole '
        '— filed 2026-09-10',
        '',
        '**Row `U1` gains two coordinates and loses no text.** `(R24)`, the author’s, rules the row '
        '**RESTATED, NOT RETIRED**: it gains `KIND`, as b404 minted it, and `WITNESS` — the shared '
        'witness that would close the site, or `NONE KNOWN` — with the refusal clause verbatim and '
        'no new measurement taken to fill a cell. **THE COORDINATES ARE ENTERED AS LABELLED FIELDS '
        'INSIDE THE ROW’S OWN CELL AND NOT AS NEW COLUMNS**, because the ledger’s COLUMN LAW fixes '
        'seven columns across 159 table lines and a row cannot gain a column alone; every line’s '
        'column count was re-measured after the write and none moved.',
        '',
        '**The `WITNESS` column is sourced from a compiled theorem and from nowhere else.** A '
        'shared witness is what `SIDELvConservation.T3.T3prime_shared_witness` says it is, read at '
        'the ref the corpus itself cites (`SIDE-lv-conservation v0.10.0 = 93c27ec`): **two clauses '
        'on one object in the family’s own parameter space** — `h1 : ∀ C ∈ 𝒞, C Phi`, that one '
        'object satisfies every member, and `h2 : mellin Phi (s / 2) ≠ 0`, that the quantity which '
        'must not degenerate does not degenerate at it. Its companion '
        '`T3.T3doubleprime_general_commutation_fails` is why both are needed: two integrands '
        'agreeing on `Ioi 0` and differing at `t = -1` give each member its own witness and no '
        'single `Φ` for both. **PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.** Both profiles '
        'are printed at the pin in the repository’s own tracked transcript — `[propext, '
        'Classical.choice, Quot.sound]`, the standard three — and the single `sorry` sits at the '
        'intermediate `T3_perClass_to_combinations`, at neither terminal. Nothing was built.',
        '',
        '**And the form does not transpose to every site, which is the reading this act adds.** '
        'Two of the six carry no inner existential at all — `(i)`, whose quantifiers run over the '
        'class and over the zeros with no `∃` inside, and `(iv)`, where the record holds ten values '
        'indexed by the width rather than ten witnesses — so their `WITNESS` cells read `UNSTATED` '
        'rather than `NONE KNOWN`, because `NONE KNOWN` would imply a witness is the right kind of '
        'thing to look for. **A SHARED INDEX IS NOT A SHARED SHAPE**: `(iii)` and `(iv)` share the '
        'support width, which b401 put on the face of its own entry, and only `(iii)` carries the '
        'existential — Boas–Kac’s own *"There exists g … with support in [-A/2, A/2]"*, indexed by '
        '`A`. `(vi)` is the only site whose own text names **both** clauses: `h1` is *"consistent '
        'at every finite modulus"*, `h2` is the *"(positive global density)"* the passage must '
        'reach. **FOUR CELLS READ `NONE KNOWN`, TWO READ `UNSTATED`, AND NO SITE OF THE SIX HAS A '
        'WITNESS FOUND.**',
        '',
        '**The navigator named two witnesses as already found and neither survives the sites’ own '
        'text.** The abscissa’s convergent sum is a witness for no site of this row **because the '
        'abscissa is not a site of this row**: it is the coordinate that CLOSED — b351 banks it as '
        '*"THE ABSCISSA WAS ALREADY CLOSED, AND HAS BEEN SINCE b326"* and sets it against the '
        'height in the next breath — and a coordinate that closed was never entered as an '
        'obstruction. The finite side’s zero is not a shared witness across places either: in '
        '`B329.finite_side_silence` the clause carrying the zero is written `((p, n) ∈ cells → '
        'ballQ p n * sumAN p n = sumAQ p n)`, a membership test against a **seven-cell decided '
        'list** discharged by `decide`, while the two clauses that ARE general in `p` carry no '
        'zero. **THE THEOREM IS GENERAL WHERE IT IS EMPTY OF THE ZERO AND DECIDED WHERE IT IS NOT.** '
        'Adding an eighth place adds a new obligation, so **there is no cross-place claim in that '
        'clause at all** — the same answer arrived at separately seven times is not one witness '
        'shared, and the navigator’s framing over-reached here too.',
        '',
        '**The refusal clause was quoted verbatim and put one question, and the answer is a fact '
        'about the clause and not about the sites.** Can it distinguish a site empty in KIND `(a)` '
        'from one empty in KIND `(b)`? Under the predicate fixed before it was asked — a clause can '
        'express a distinction between two states of ONE site only if some predicate in it has ONE '
        'site for its subject — its four sentences take for their subjects: the three; a row naming '
        'three things; a row and the pair at each end of a bridge; three obstructions. **`0` OF `4` '
        'ARE UNARY.** Every clause of the refusal is binary or higher while `(a)` versus `(b)` is a '
        'unary property of one site, so **A BINARY LAW CANNOT EXPRESS A UNARY DISTINCTION**, and no '
        'amount of restating it will make it. **THIS IS NOT A DEFECT IN THE SITES; IT IS A MISSING '
        'COORDINATE IN THE ROW** — which is exactly what `(R24)` supplies, and why the clause is '
        'restated rather than retired.',
        '',
        '**The six read as six, by three tests fixed before the read.** Writes its missing '
        'statement: `4` of 6 (`iii`, `iv`, `v`, `vi`). Files a residue: `1` of 6 (`vi`). Declares '
        'its kind: `1` of 6 (`v`). **ENTRIES DOING BOTH OF THE FIRST TWO: ONE** — which the row’s '
        'own refusal cell had already said, *"and which one of the six already has"*, so the '
        'reading that `(iv)` also did was refutable by a sentence in the very cell it was about. '
        '`(iv)`’s *"A FOURTH INSTANCE OF THE OBSTRUCTION AND NOT A CRACK IN IT"* says the '
        'obstruction is real and never weighs it, and **SAYING AN OBSTRUCTION IS REAL IS NOT FILING '
        'A RESIDUE**; where an entry names no statement at all its residue test is **VACUOUS**, and '
        'is recorded as vacuous rather than as a plain NO. The relief b404 routed is still routed '
        'and still not applied: **b405 REWRITES NO ENTRY.**',
        '',
        '**The route from the compiled shape to any instance is priced and not taken.** It would '
        'need an identification of a site’s family with the theorem’s `Set Coupling` and of its '
        'parameter space with `ℝ → ℂ`, and then both clauses at that identification; **not one of '
        'the six is stated in those terms, and six sites supply zero candidate witnesses.** A build '
        'buys nothing — both terminals are already compiled and both profiles already printed — so '
        '**the route is PRICEABLE WITHOUT A BUILD**, refuting the expectation that it was not. '
        'Where the record itself puts the route’s second clause is quoted and not endorsed: the '
        'corpus’s archived trails line reads *"`T3prime_shared_witness` with `h1 : ∀ C ∈ 𝒞, C Phi` '
        '… **and** `h2 : mellin Phi (s/2) ≠ 0` (open, RH-strength)"* and calls that `h2` *"the same '
        'h2 of §27.3’s five registers"*. **THIS ACT MAKES NO CLAIM ABOUT h2 IN EITHER DIRECTION. '
        'QUOTING A HYPOTHESIS IS NOT ASSERTING IT.**',
        '',
        '**Nothing deposits.** `0` grades moved, `0` bridges typed, `0` entries rewritten, `0` '
        'keystones edited, `0` kernels built, `0` `.lean` files touched, `0` new columns, `0` '
        'content lost. The instrument and instrument-audit lanes stay parked and the wave stays '
        'parked. Registration `data/b405_registration_2026-09-10.txt`, LOCKED before any write at '
        'sha256 `%s`, chained on `tools/b378_lockgate.py` run as b405 — %d gates read, %d checked '
        'by digest. Bank: `relay/data/b405_the_rows_law_restated.txt`. **h2 where the deposit left '
        'it.**' % (SEALHASH, LG['gates_read'], LG['face_subject_gates']),
    ]


SCOPE = ("### THIS ROW RECORDS A ROW RESTATED AND A THEOREM READ. ### IT CERTIFIES NO EQUIVALENCE, "
         "OPENS NO TERMINAL, MOVES NO GRADE AND TYPES NO BRIDGE -- LEAST OF ALL BETWEEN A COMPILED "
         "SHAPE AND ANY INSTANCE OF IT")


def corr_rows(Q):
    m = ("**THE ROW'S REFUSAL CLAUSE IS BINARY AND THE DISTINCTION IT WAS ASKED TO CARRY IS UNARY, "
         "SO THE (a)/(b) KIND IS A MISSING COORDINATE AND NOT A DEFECT IN THE SITES; AND OF SIX "
         "SITES, ZERO HAVE A SHARED WITNESS AND TWO HAVE NO PLACE FOR ONE** (b405, the row's law "
         "restated)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b405 -- %d gates read, %d checked by digest; %d reads, %d ANCHOR MISSES. **(R24), THE "
            "AUTHOR'S, IS EXECUTED INSIDE THE COLUMN LAW AND NOT BY AMENDING IT**: KIND and WITNESS "
            "enter as labelled fields inside cell 5, every table line's column count re-measured "
            "and unmoved, the refusal verbatim, 5 of 7 cells BYTE-IDENTICAL and 2 carrying their "
            "prior text as a TRUE PREFIX. **THE WITNESS COLUMN IS SOURCED FROM "
            "T3.T3prime_shared_witness AT v0.10.0 = 93c27ec** -- two clauses on one object, h1 "
            "SHAREDNESS and h2 NON-DEGENERACY -- with its countermodel companion showing why both "
            "are needed, both profiles PRINTED at the pin as the standard three axioms. **THE FORM "
            "DOES NOT TRANSPOSE TO EVERY SITE**: (i) and (iv) carry no inner existential, so their "
            "cells read UNSTATED and not NONE KNOWN. **4 NONE KNOWN, 2 UNSTATED, 0 WITNESSES "
            "FOUND.** **BOTH NAVIGATOR CANDIDATES DECLINED**: the abscissa is not a site of this "
            "row, and the finite side's zero is per-cell over a seven-cell decided list while the "
            "clauses general in p carry no zero. **THE SIX BY THREE TESTS: 4 write the missing "
            "statement, 1 files a residue, 1 declares a kind** -- and the row's own cell had "
            "already said one of the six does both. %d GRADES MOVED, %d BRIDGES TYPED, %d ENTRIES "
            "REWRITTEN, %d NEW COLUMNS, %d KERNELS BUILT, %d CONTENT LOST"
            % (LG['gates_read'], LG['face_subject_gates'], READS, MISSES, 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### TWO KERNEL TERMINALS "
            "WERE READ WHOLE AT THE REF THE CORPUS CITES AND NEITHER WAS BUILT: "
            "SIDELvConservation.T3.T3prime_shared_witness AND "
            "SIDELvConservation.T3.T3doubleprime_general_commutation_fails, AT "
            "SIDE-lv-conservation v0.10.0 = 93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f -- A "
            "REPOSITORY THIS ACT READS AT A TAG AND DOES NOT TOUCH, AND WHICH IS NOT ON THE "
            "FOUR-REPO ROSTER. ### READING A THEOREM ABOUT A SHAPE IS NOT CLAIMING IT AT AN "
            "INSTANCE")
    prof = ("### THE AXIOM PROFILES THIS ACT READS ARE PRINTED, NOT RUN: BOTH T3 TERMINALS AT "
            "[propext, Classical.choice, Quot.sound] FROM THE REPOSITORY'S OWN TRACKED "
            "VERIFICATION_TRANSCRIPT.md AT THE PIN, AND B329.finite_side_silence AND "
            "B329.compact_smear_vanishes_at_cells FROM AXIOM_PRINTS.txt LINES 590 AND 587. ### NO "
            "PROFILE IS INFERRED. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, "
            "NO RULE STRUCK OR AMENDED, NO COLUMN LAW AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, "
            "NO REGISTRY ROW EDITED, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO LIST CLOSED. ### "
            "THE CORPUS WRITES ARE TWO CELLS OF ONE LEDGER ROW, APPENDED TO AND CHECKED CELL BY "
            "CELL AGAINST THE PRE-ACT BLOB, AND ONE APPEND-ONLY TRAIL BLOCK -- 0 CONTENT LOST")
    grade = ("### THE PREDICATE THAT DECIDED COMPONENT 2 WAS FIXED ON THE LOCKED FACE BEFORE THE "
             "CLAUSE WAS READ, SO THE ANSWER COULD NOT BE CHOSEN AFTER THE FACT. ### THE BRANCH "
             "RULE FOR THE FINITE SIDE WAS LIKEWISE FIXED IN ADVANCE, WITH BOTH BRANCHES AND THEIR "
             "EVIDENCE NAMED. ### WHERE AN ENTRY NAMES NO MISSING STATEMENT, ITS RESIDUE TEST IS "
             "RECORDED AS VACUOUS IN THE SAME SENTENCE AS ITS VERDICT. ### A CELL IS FILLED FROM "
             "ITS OWN SITE'S BANKED TEXT AND FROM NOWHERE ELSE, AND WHERE THE FORM DOES NOT "
             "TRANSPOSE THE CELL SAYS SO RATHER THAN READING NONE KNOWN. ### A NAVIGATOR CANDIDATE "
             "THAT BELONGS TO NO SITE IS DECLINED IN THOSE WORDS RATHER THAN FILED AGAINST THE "
             "NEAREST ONE. ### AND A RULING IS EXECUTED INSIDE THE LAW IT MEETS RATHER THAN BY "
             "QUIETLY AMENDING IT")
    status = ("data/b405_the_rows_law_restated.txt; data/b405_components.txt; "
              "data/b405_extract.txt; data/b405_registration_2026-09-10.txt (LOCKED before any "
              "write at sha256 %s, chained on tools/b378_lockgate.py run as b405); "
              "tools/b405_extract.py; tools/b405_regspec.py; tools/b405_reg_gate.py; "
              "tools/b405_components.py; tools/b405_desk_bank.py; tools/b405_checks.py; "
              "PLACE-papers FACES_LEDGER.md (row U1, two cells appended to) and OPEN_TRAILS.md "
              "(one append-only block); CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what is a shared witness in this corpus',
           'can the uniformity row tell two kinds of empty apart',
           'does any uniformity site have a shared witness',
           'is the finite side zero the same at every place',
           'was row u1 retired',
           'what would it cost to carry the countermodel to an instance')
MUST_NOT_HIT = ('a bridge was typed', 'the row was retired', 'a new column was added',
                'a shared witness was found', 'a kernel was built')

KEY = 'the-rows-law-restated'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b405 EXECUTED (R24) AND RESTATED ROW U1 RATHER THAN RETIRING IT. **THE ROW GAINS TWO "
        "COORDINATES, KIND AND WITNESS, ENTERED AS LABELLED FIELDS INSIDE ITS OWN CELL AND NOT AS "
        "NEW COLUMNS** -- the ledger's COLUMN LAW fixes seven columns across 159 table lines, so a "
        "row cannot gain a column alone; every line's column count was re-measured after the write "
        "and none moved. **THE WITNESS COLUMN IS SOURCED FROM A COMPILED THEOREM AND FROM NOWHERE "
        "ELSE**: a shared witness is what SIDELvConservation.T3.T3prime_shared_witness says it is, "
        "read at SIDE-lv-conservation v0.10.0 = 93c27ec -- TWO CLAUSES ON ONE OBJECT IN THE "
        "FAMILY'S OWN PARAMETER SPACE, h1 SHAREDNESS and h2 NON-DEGENERACY -- with "
        "T3.T3doubleprime_general_commutation_fails showing why both are needed, since two "
        "integrands agreeing on Ioi 0 and differing at t = -1 give each member its own witness and "
        "no single Phi for both. **PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.** Both "
        "profiles PRINTED at the pin as [propext, Classical.choice, Quot.sound], the one sorry at "
        "the intermediate T3_perClass_to_combinations and at neither terminal. **AND THE FORM DOES "
        "NOT TRANSPOSE TO EVERY SITE**: (i) and (iv) carry no inner existential to share, so their "
        "cells read UNSTATED rather than NONE KNOWN; (iii) is the one site whose own banked text "
        "supplies the existential, Boas-Kac's ex-g indexed by A; (vi) is the only site naming BOTH "
        "clauses, consistency at every finite modulus and a positive global density. **FOUR CELLS "
        "NONE KNOWN, TWO UNSTATED, ZERO WITNESSES FOUND.** **BOTH OF THE NAVIGATOR'S NAMED "
        "WITNESSES ARE DECLINED ON THE SITES' OWN TEXT**: the abscissa is not a site of this row at "
        "all -- it is the coordinate that CLOSED at b326 and was never entered -- and the finite "
        "side's zero is guarded by membership in a SEVEN-CELL DECIDED LIST while the two clauses "
        "general in p carry no zero, so THE THEOREM IS GENERAL WHERE IT IS EMPTY OF THE ZERO AND "
        "DECIDED WHERE IT IS NOT and there is no cross-place claim in the clause that carries it. "
        "**THE REFUSAL CLAUSE WAS QUOTED VERBATIM AND CANNOT CARRY THE DISTINCTION IT WAS ASKED "
        "TO**: 0 of its 4 sentences have ONE site for a subject, so A BINARY LAW CANNOT EXPRESS A "
        "UNARY DISTINCTION -- NOT A DEFECT IN THE SITES BUT A MISSING COORDINATE IN THE ROW, which "
        "is what (R24) supplies. **THE SIX BY THREE TESTS: 4 of 6 write the missing statement, 1 of "
        "6 files a residue, 1 of 6 declares a kind**, and the row's own refusal cell had already "
        "said one of the six does both. **THE SHAPE-TO-INSTANCE ROUTE IS PRICED AND NOT TAKEN**: "
        "six sites, zero candidate witnesses, the identification is the whole price, and a build "
        "buys nothing because both terminals are already compiled and both profiles already "
        "printed -- SO THE ROUTE IS PRICEABLE WITHOUT A BUILD. **NO CLAIM IS MADE ABOUT h2 IN "
        "EITHER DIRECTION.**")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED AND NO REPOSITORY "
        "CLONED. ### THE FOUR AXIOM PROFILES READ ARE PRINTED PROFILES IN TRACKED FILES, READ AND "
        "NOT RUN; NONE IS INFERRED. ### NO GRADE MOVED OR CONFERRED, NO BRIDGE TYPED BETWEEN ANY "
        "TWO OF THE SIX SITES, NO BRIDGE TYPED BETWEEN THE COMPILED SHAPE AND ANY INSTANCE, NO "
        "ENTRY REWRITTEN, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO COLUMN LAW AMENDED, NO FACE "
        "PROMOTED, NO ROW PAID, NO RULE STRUCK, NO CLASS RULED, NO LIST CLOSED. ### THE CORPUS "
        "WRITES ARE TWO CELLS OF ROW U1, APPENDED TO AND CHECKED CELL BY CELL AGAINST THE PRE-ACT "
        "BLOB WITH THE OTHER FIVE BYTE-IDENTICAL, AND ONE APPEND-ONLY TRAIL BLOCK. ### NOTHING "
        "DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b405_the_rows_law_restated.txt; data/b405_components.txt; data/b405_extract.txt; "
        "data/b405_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b405 -- %d gates read, %d checked by digest); "
        "tools/b405_extract.py; tools/b405_components.py; tools/b405_desk_bank.py; "
        "tools/b405_checks.py; PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md "
        "row %d" % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b405 (row U1 restated under (R24) with two coordinates inside the column law, the "
           "shared witness sourced from the compiled theorem, and both named witnesses declined)")
    row_new = ('    # ### THE ROW-S LAW RESTATED (b405).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-48s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + chr(10)
    ROW_ANCHOR = ('INDEX = [' + chr(10)
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + chr(10))
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ('"%s"' % KEY) not in txt and ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s' % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-56s reaches the b405 key : %s' % (qq, g2))
    for lbl, cond in (
            ('(R24) is named', '(R24)' in out),
            ('the two coordinates are named', 'KIND AND WITNESS' in out),
            ('no new column', 'NOT AS NEW COLUMNS' in out),
            ('the witness has two clauses', 'TWO CLAUSES ON ONE OBJECT' in out),
            ('the pin is named', '93c27ec' in out),
            ('the form does not transpose', 'DOES NOT TRANSPOSE TO EVERY SITE' in out),
            ('zero witnesses found', 'ZERO WITNESSES FOUND' in out),
            ('both candidates declined', 'ARE DECLINED ON THE SITES' in out),
            ('the binary/unary finding', 'A BINARY LAW CANNOT EXPRESS A' in out),
            ('the missing coordinate', 'MISSING COORDINATE IN THE ROW' in out),
            ('the route is priceable', 'PRICEABLE WITHOUT A BUILD' in out),
            ('no claim about h2', 'NO CLAIM IS MADE ABOUT h2' in out)):
        ok = ok and cond
        rec('    %-56s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-48s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok, cells):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A("b405 -- THE ROW'S LAW, RESTATED; THE COUNTERMODEL, READ WHOLE. ### THE BANK.")
    A('### 2026-09-10. ### CONCURRENCY: SOLO (research seat). ### FERRY_STANDING v2 BY REFERENCE.')
    A('### Registration `data/b405_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes,' % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### chained on `tools/b378_lockgate.py` run as b405 -- ### **%d GATES READ, %d PASSING,'
      % (LG['gates_read'], LG['gates_passing']))
    A('### %d CHECKED BY DIGEST.**' % LG['face_subject_gates'])
    A(BAR)
    A('')
    A(SUB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUB)
    A('### ### ### **THE ROW IS RESTATED AND THE CLAUSE THAT WAS ASKED TO CARRY THE NEW')
    A('### ### ### DISTINCTION CANNOT CARRY IT -- NOT BECAUSE IT IS BADLY WRITTEN, BUT BECAUSE')
    A('### ### ### IT IS THE WRONG ARITY.** ### Every sentence of the refusal takes a PAIR, a SET')
    A('### or the ROW for its subject: *the three*; *a row naming three things that look alike*;')
    A('### *types no bridge between the three, in either direction*; *three separate obstructions')
    A('### that rhyme are three obstructions*. ### ### **`0` OF `4` HAVE ONE SITE FOR A SUBJECT,')
    A('### ### AND `(a)` VERSUS `(b)` IS A UNARY PROPERTY OF ONE SITE.** ### **A BINARY LAW CANNOT')
    A('### ### EXPRESS A UNARY DISTINCTION**, and restating it more carefully cannot help. ###')
    A('### **SO IT IS NOT A DEFECT IN THE SITES. ### IT IS A MISSING COORDINATE IN THE ROW** --')
    A('### which is exactly what `(R24)` supplies, and why the author ruled RESTATED and not')
    A('### RETIRED.')
    A('### ### **AND THE SECOND COORDINATE COST MORE THAN IT LOOKED.** ### `WITNESS` is sourced')
    A('### from a compiled theorem and from nowhere else -- `T3.T3prime_shared_witness` at the ref')
    A('### the corpus itself cites -- and read at content the theorem says a shared witness is')
    A('### ### **TWO CLAUSES ON ONE OBJECT**: `h1`, one object satisfies every member; `h2`, the')
    A('### quantity that must not degenerate does not degenerate at it. ### **AND THAT FORM DOES')
    A('### ### NOT TRANSPOSE TO EVERY SITE OF THE ROW.** ### Two of the six carry no inner')
    A('### existential at all, so their cells read `UNSTATED` and not `NONE KNOWN`: saying no')
    A('### witness is known would imply a witness is the right kind of thing to look for. ###')
    A('### ### **FOUR CELLS `NONE KNOWN`, TWO `UNSTATED`, AND `0` OF SIX SITES WITH A WITNESS')
    A('### ### FOUND.** ### The navigator named two as already found; ### **NEITHER SURVIVES THE')
    A('### ### SITES’ OWN TEXT**, and both are declined in those words rather than filed')
    A('### against the nearest site to keep a count up.')
    A('')
    A(SUB)
    A('### (2) COMPONENT 1 -- THE SIX READ AS SIX.')
    A(SUB)
    A('### **T1 WRITES THE MISSING STATEMENT : `4` of 6** -- `(iii)`, `(iv)`, `(v)`, `(vi)`.')
    A('### **T2 FILES A RESIDUE          : `1` of 6** -- `(vi)`, and in the keystone’s own')
    A('###   words, filed at all three problems alike.')
    A('### **T3 DECLARES ITS KIND        : `1` of 6** -- `(v)`, which says *"(v) IS KIND (b)"*.')
    A('### ### **ENTRIES DOING BOTH T1 AND T2 : ONE.** ### And the row had already said so about')
    A('### itself, in the refusal cell: *"and which **one of the six already has**"*. ### **THE')
    A('### ### DRAFT’S EXPECTATION THAT `(iv)` ALSO DID WAS REFUTABLE BY A SENTENCE IN THE')
    A('### ### VERY CELL IT WAS ABOUT**, and it is refuted here: `(iv)`’s *"A FOURTH INSTANCE')
    A('### OF THE OBSTRUCTION AND NOT A CRACK IN IT"* says the obstruction is REAL and never says')
    A('### what fraction of the problem the missing statement carries. ### **SAYING AN OBSTRUCTION')
    A('### ### IS REAL IS NOT FILING A RESIDUE.**')
    A('### ### **AND WHERE AN ENTRY NAMES NO STATEMENT, ITS RESIDUE TEST IS VACUOUS AND IS')
    A('### ### RECORDED AS VACUOUS IN THE SAME SENTENCE AS ITS VERDICT** -- `(i)` and `(ii)`. ###')
    A('### A `NO` that could not have been a `YES` is not evidence about the entry.')
    A('')
    A(SUB)
    A('### (3) ADDITION ONE -- THE COUNTERMODEL AT ITS TERMINAL.')
    A(SUB)
    A('### **THE PIN:** ### `SIDE-lv-conservation v0.10.0 = 93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f`,')
    A('### the ref `INDEX_ARITY_AT_THE_CRITICAL_LINE.md` cites. ### **THE FILE WAS READ AT THE PIN')
    A('### ### BY `git show`, NOT FROM THE WORKING TREE**, which is ahead of it. ### That')
    A('### repository is READ AT A TAG AND NOT TOUCHED, and it is not on the four-repo roster.')
    A('### **THE STATEMENTS, WHOLE:**')
    A('###   `T3prime_shared_witness (\U0001d49e) (s) (h1 : ∀ C ∈ \U0001d49e, C Phi)')
    A('###     (h2 : mellin Phi (s / 2) ≠ 0) : ∃ Φ, (∀ C ∈ \U0001d49e, C Φ)'
      ' ∧ mellin Φ (s / 2) ≠ 0`')
    A('###     -- proved by `⟨Phi, h1, h2⟩`. ### **THE PROOF IS THE TRIPLE; THE CONTENT IS')
    A('###     ### THE HYPOTHESES.**')
    A('###   `T3doubleprime_general_commutation_fails : ¬ ∀ \U0001d49e s, (∀ C ∈'
      ' \U0001d49e, ∃ Φ, C Φ ∧ ...) → ∃ Φ, ...`')
    A('###     -- countermodel at `s = 3`, `f1` and `f2` agreeing on `Ioi 0` and differing at')
    A('###     `t = -1`.')
    A('### **THE PROFILE, PRINTED AND NOT RUN:** ### `[propext, Classical.choice, Quot.sound]` for')
    A('### both, from the repository’s own TRACKED `VERIFICATION_TRANSCRIPT.md` at the pin. ###')
    A('### The single `sorry` sits at the intermediate `T3_perClass_to_combinations` and at')
    A('### **NEITHER TERMINAL**. ### ### **NOTHING WAS BUILT; THE LANE IS PARKED.**')
    A('### ### **WHAT A SHARED WITNESS IS, IN THE THEOREM’S OWN TERMS:** ### `h1` is')
    A('### ### **SHAREDNESS** ### -- ONE object satisfies EVERY member of the family. ### `h2` is')
    A('### ### **NON-DEGENERACY** ### -- the quantity that must not vanish does not vanish AT it.')
    A('### ### **AND THE COUNTERMODEL IS WHY BOTH ARE NEEDED: PER-MEMBER WITNESSES DO NOT ADD UP')
    A('### ### TO A SHARED ONE.**')
    A('')
    A(SUB)
    A('### (4) THE SIX WITNESS CELLS, AND THE TWO THAT HAVE NO PLACE FOR ONE.')
    A(SUB)
    A('### `(i)`   ### **UNSTATED** ### -- a `∀` over the class and, through the explicit')
    A('###         formula, over the zeros, with no `∃` inside it. ### **NOTHING TO SHARE.**')
    A('### `(ii)`  ### **NONE KNOWN** ### -- one argument serving every height; b351 says the')
    A('###         record has none, in the sentence that sets this coordinate against the one that')
    A('###         closed.')
    A('### `(iii)` ### **NONE KNOWN** ### -- one `g` serving every width. ### **THE ONE SITE WHOSE')
    A('###         ### OWN BANKED TEXT SUPPLIES THE INNER EXISTENTIAL**, in Boas-Kac’s own')
    A('###         *"There exists g ... with support in [-A/2, A/2]"*, indexed by `A`.')
    A('### `(iv)`  ### **UNSTATED** ### -- ten VALUES indexed by the width, not ten witnesses. ###')
    A('###         **A SHARED INDEX IS NOT A SHARED SHAPE:** ### `(iii)` and `(iv)` share the')
    A('###         support width and only `(iii)` carries the existential.')
    A('### `(v)`   ### **NONE KNOWN** ### -- one constant serving every representation. ### The')
    A('###         site IS a `∀∃ ⇒ ∃∀` with the constant as the inner')
    A('###         existential, and the entry names the shape by contrast without supplying the')
    A('###         witness.')
    A('### `(vi)`  ### **NONE KNOWN** ### -- one object consistent at every finite modulus and')
    A('###         non-degenerate. ### **THE ONLY SITE WHOSE OWN TEXT NAMES BOTH CLAUSES.**')
    A('')
    A(SUB)
    A('### (5) ADDITION TWO -- THE FINITE SIDE’S WITNESS, AND THE BRANCH TAKEN.')
    A(SUB)
    A('### **THE BRANCH RULE WAS FIXED ON THE LOCKED FACE BEFORE THE READ**, both branches named')
    A('### with the evidence that would decide each. ### ### **THE BRANCH TAKEN IS `(beta)`.**')
    A('### `finite_side_silence`’s clause carrying the zero is written')
    A('### `((p, n) ∈ cells → ballQ p n * sumAN p n = sumAQ p n)` -- ### **A MEMBERSHIP')
    A('### ### TEST AGAINST A SEVEN-CELL DECIDED LIST**, `[(2,1), (2,2), (3,1), (3,2), (5,1),')
    A('### (7,1), (2,3)]`, discharged by `decide`. ### The value is the same at every cell it is')
    A('### proved at, and it is proved at seven cells and no others; an eighth place is a new')
    A('### obligation. ### ### **THERE IS NO CROSS-PLACE CLAIM IN THAT CLAUSE AT ALL, SO ZERO IS')
    A('### ### NOT A SHARED WITNESS ACROSS PLACES -- IT IS THE SAME ANSWER ARRIVED AT SEPARATELY')
    A('### ### SEVEN TIMES.** ### **AND THE NAVIGATOR’S FRAMING OVER-REACHED HERE TOO.**')
    A('### ### **AND THE SHARPER THING, WHICH NEITHER BRANCH OF THE QUESTION SAYS:** ### `(a)` and')
    A('### `(b)` ARE general in `p` and neither carries the zero; `(c)` carries the zero and has no')
    A('### generality. ### ### **THE THEOREM IS GENERAL WHERE IT IS EMPTY OF THE ZERO AND DECIDED')
    A('### ### WHERE IT IS NOT** -- a fact about the terminal, not a complaint about it.')
    A('')
    A(SUB)
    A('### (6) THE ROUTE, PRICED AND NOT TAKEN.')
    A(SUB)
    A('### **THE STATEMENT THAT WOULD HAVE TO HOLD:** ### an identification of a site’s family')
    A('### with the theorem’s `Set Coupling` and of its parameter space with `ℝ →')
    A('### ℂ`, then both clauses at that identification. ### **THE IDENTIFICATION IS THE WHOLE')
    A('### ### PRICE, AND NOT ONE OF THE SIX SITES IS STATED IN THOSE TERMS.**')
    A('### **A CANDIDATE SHARED WITNESS AT ANY SITE:** ### ### **NONE. ### SIX SITES, ZERO')
    A('### ### CANDIDATES.**')
    A('### **`UNPRICEABLE` WITHOUT A BUILD:** ### ### **NO, AND THAT REFUTES THE EXPECTATION.** ###')
    A('### A build buys nothing: both terminals are ALREADY compiled and their profiles ALREADY')
    A('### printed, so no parked lane is withholding a measurement. ### **THE ROUTE IS PRICEABLE')
    A('### ### AND THE PRICE IS NOT A BUILD.**')
    A('### **AND WHERE THE RECORD PUTS THE ROUTE’S SECOND CLAUSE, QUOTED AND NOT ENDORSED:**')
    A('### the corpus’s own archived trails line reads *"`T3prime_shared_witness` with `h1 :')
    A('### ∀ C ∈ \U0001d49e, C Phi` ... **and** `h2 : mellin Phi (s/2) ≠ 0` (open,')
    A('### RH-strength)"* and calls that `h2` *"the same h2 of §27.3’s five registers"*.')
    A('### ### **THIS ACT MAKES NO CLAIM ABOUT `h2` IN EITHER DIRECTION.** ### **QUOTING A')
    A('### ### HYPOTHESIS IS NOT ASSERTING IT.**')
    A('')
    A(SUB)
    A('### (7) THE WRITES, AND WHAT THEY COST THE RECORD.')
    A(SUB)
    A('### **`FACES_LEDGER.md` ROW `U1`** ### -- two cells appended to, checked cell by cell')
    A('### against the PRE-ACT blob: the other five ### **BYTE-IDENTICAL**, the two touched')
    A('### carrying their prior text as a ### **TRUE PREFIX**. ### ### **AND EVERY TABLE')
    A('### ### LINE’S COLUMN COUNT RE-MEASURED AFTER THE WRITE AND UNMOVED:** ### `(R24)`')
    A('### gave the row two coordinates and the ledger no new column.')
    A('### **`OPEN_TRAILS.md`** ### -- one append-only block, the b404 block untouched.')
    A('### **`CORRESPONDENCE.md`** ### -- row `%d`, appended, six cells non-empty.' % rownum)
    A('### **THE INDEX** ### -- one key, `%s`, %s.' % (KEY, 'PASS' if kok else '### FAIL ###'))
    A('### **AND NOTHING ELSE.** ### `0` `.lean` files touched, `0` kernels built, `0` keystones')
    A('### edited, `0` locked faces edited, `0` entries rewritten, `0` new columns, `0` grades')
    A('### moved, `0` bridges typed, `0` content lost. ### ### **NOTHING DEPOSITS.**')
    A('')
    A(SUB)
    A('### (8) THIS ACT’S OWN DEFECTS, PRINTED RATHER THAN SMOOTHED.')
    A(SUB)
    A('### ### **(1) A PATCH SCRIPT DESTROYED ONE OF THIS ACT’S OWN TOOLS MID-WRITE.** ###')
    A('### `io.open(path, \'w\')` truncates BEFORE it encodes, so an encode error left a')
    A('### ### **ZERO-BYTE HUSK** ### where `b405_extract.py` had been -- the species `b328` banked')
    A('### for `json.dump`, recurring on a plain text write. ### The cure is the same one and is')
    A('### now used for every write in this act’s tools: ### **ENCODE FIRST, WRITE BYTES.**')
    A('### ### **(2) THE LOCKED FACE NAMES THREE STEP-ZERO RECORDS AT PATHS THEY NO LONGER HAVE.**')
    A('### ### Section (A) calls them `b405_census_zero.txt`, `b405_faces_census_zero.txt` and')
    A('### `b405_pins_zero.txt`; they were renamed to the `_stepzero` names `b378_lockgate.py`')
    A('### reads, before the lock, and section (W) names them correctly. ### **BOTH NAMES ARE')
    A('### ### PRINTED AND THE LOCKED FACE IS NOT EDITED.** ### The bytes are the same bytes.')
    A('### ### **(3) A QUOTED HEREDOC COLLAPSED A BACKSLASH AND TURNED AN ASTRAL CHARACTER INTO A')
    A('### ### LONE SURROGATE PAIR**, which no encoder will emit -- the `b328` heredoc species,')
    A('### banked and met again. ### Built from `chr(92)` instead, as the bank says to.')
    A('### ### **(4) AN ARM TESTED FOR A TOOL’S VERDICT WORD AS A SUBSTRING AND FIRED ON THIS')
    A('### ### ACT’S OWN PROSE.** ### `G-KEY` read `"NO KEY" not in stdout` and failed on a')
    A('### successful lookup, because the act’s own banked grade line reads *"NO KEYSTONE EDITED"*')
    A('### -- which contains `NO KEY`. ### ### **THAT IS THE SAME SPECIES AS `b400`’s `G-ONEQ`,')
    A('### ### `b403`’s `G-FERRYWORDS` AND `b404`’s `G-NOAXIOMCLAIM`, IN ITS FOURTH DRESS: A')
    A('### ### SUBSTRING TEST FOR A VERDICT FIRES ON PROSE THAT MERELY CONTAINS THE VERDICT’S')
    A('### ### WORDS.** ### The cure is the tool’s own predicate: ### **READ THE VERDICT LINE, NOT')
    A('### ### THE WHOLE OUTPUT.** ### The raw substring count is printed beside the verdict so a')
    A('### reader sees the trap and not only its repair.')
    A('### ### **(5) AND THE WRITE LIST NAMES SOME OF THIS ACT’S OWN FILES ONLY BY THEIR KIND.**')
    A('### ### Covered by a named KIND but not by a named path: the materialised-at-pin copies')
    A('### under `data/_b405/`, which the face names as a DIRECTORY -- the correct way to name a')
    A('### class -- and the lock-gate and desk-writer run records, which it does not name at all:')
    A('### `b405_lockgate.json`, `b405_lockgate_notes.txt`, and the `b405_desk_notes*.txt` series.')
    A('### ### **THE COUNT IS LEFT TO THE SUITE AND NOT FROZEN HERE, BECAUSE RE-RUNNING THE DESK')
    A('### ### WRITER ADDS ANOTHER RUN RECORD AND MOVES IT** -- a figure the act’s own re-runs')
    A('### change does not belong in the act’s own prose.')
    A('### **AND ONE PATH ON THE FACE NAMES A FILE NO TOOL EMITS:**')
    A('### section (W) KIND 6 says `data/b405_desk.txt` and the desk writer emits')
    A('### `b405_desk_notes.txt`. ### **BAR 9 IS A KIND-MEMBERSHIP BAR AND IT IS MET AT `0` FILES')
    A('### ### OF NO NAMED KIND; THE PATH-LEVEL SHORTFALL IS `10` AND IS PRINTED HERE RATHER THAN')
    A('### ### BEHIND A KINDER NUMBER.** ### The locked face is not edited.')
    A('')
    A(SUB)
    A('### (9) WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It types ### **NO BRIDGE** ### between any two of the six, and none between the compiled')
    A('### countermodel and any instance of the shape it is about.')
    A('### It does not say a witness EXISTS at any site. ### **NAMING WHAT A WITNESS WOULD HAVE TO')
    A('### ### BE IS NOT CLAIMING ONE EXISTS.**')
    A('### It does not say the finite-side terminal is wrong, small, or badly done. ### **IT SAYS')
    A('### ### WHERE ITS GENERALITY IS AND WHERE ITS ZERO IS, AND THEY ARE IN DIFFERENT CLAUSES.**')
    A('### It rewrites no entry, retires no clause, amends no column law, and closes no list.')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### `h2` STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'wb').write((chr(10).join(B) + chr(10)).encode('utf-8'))
    rec('  bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))
    return len(B)


def main():
    bar('=')
    rec('b405 -- THE DESK, ROW `U1` RESTATED, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.')
    bar('=')
    bar()
    rec('  ### THE DESK UNDER (R7).')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### ROW `U1`, TWO CELLS APPENDED TO, CHECKED CELL BY CELL, COLUMN SHAPE RE-MEASURED.')
    bar()
    fok, cells = do_faces()
    if not fok:
        run_clock.write(D, 'b405_desk_notes', LINES)
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'FACES_LEDGER.md'], capture_output=True)

    rec()
    bar()
    rec('  ### THE TRAIL BLOCK, APPEND-ONLY.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b404 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            run_clock.write(D, 'b405_desk_notes', LINES)
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_r24': '(r24)' in low,
        'says_restated_not_retired': 'restated, not retired' in low,
        'says_two_coordinates': 'two coordinates' in low,
        'says_no_new_column': 'not as new columns' in low,
        'says_two_clauses': 'two clauses on one object' in low,
        'says_pin': '93c27ec' in low,
        'says_profile': 'classical.choice' in low,
        'says_not_transpose': 'the form does not transpose' in low,
        'says_zero_found': 'no site of the six has a witness found' in low,
        'says_abscissa_declined': 'the abscissa is not a site of this row' in low,
        'says_seven_cells': 'seven-cell decided list' in low,
        'says_binary_unary': 'a binary law cannot express a unary distinction' in low,
        'says_missing_coordinate': 'missing coordinate in the row' in low,
        'says_route_priceable': 'priceable without a build' in low,
        'says_no_h2_claim': 'no claim about h2 in either direction' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-32s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b405_desk_notes', LINES)
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)

    rec()
    bar()
    rec('  ### THE CORRESPONDENCE ROW.')
    bar()
    ROWS = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b405_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b405_desk_notes', LINES)
        return 1
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    present = [mm for mm, _s, _t, _p, _g, _sc, _st in ROWS if mm in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = max(nums)
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
        new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
        open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(TABLE + '.tmp', TABLE)
        back = io.open(TABLE, encoding='utf-8').read()
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(chr(10))))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(chr(10))),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            run_clock.write(D, 'b405_desk_notes', LINES)
            return 1
        rownum = start

    rec()
    bar()
    rec('  ### THE INDEX KEY.')
    bar()
    kok = do_key(rownum)

    rec()
    bar()
    rec('  ### THE BANK.')
    bar()
    nb = bank(Q, rownum, kok, cells)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### CELLS %d. ### ROW %d. ### KEY %s. ### BANK %d '
        'LINES.**' % (Q['items'], Q['closed'], cells, rownum, 'PASS' if kok else 'FAIL', nb))
    bar('=')
    run_clock.write(D, 'b405_desk_notes', LINES)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
