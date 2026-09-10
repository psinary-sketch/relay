# -*- coding: utf-8 -*-
"""b401_desk_bank.py -- THE DESK, THE LEDGER WRITE, AND THE BANK.

### ### **THE LEDGER WRITE HERE IS HARDER THAN `b400`'S AND IS DONE CELL BY CELL.** ### `b400`
### appended to the END of three rows, so `startswith` proved preservation in one line. ### This act
### must append to ### **TWO CELLS OF ONE ROW** -- the instance list and the OWED cell -- and an
### insertion in the middle of a line is NOT a prefix of anything. ### So the row is split on its
### unescaped pipes by the shared splitter, each cell is checked separately, and ### **EVERY CELL
### ### THIS ACT DOES NOT TOUCH MUST COME BACK BYTE-IDENTICAL** while the two it touches must have
### their prior text as a TRUE PREFIX.
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
MARK = '<!-- b401 the absent element searched; the fourth site entered -->'
PRIOR = '<!-- b400 the bridge restated: two objects on their families, one question at the window -->'
BANKOUT = os.path.join(D, 'b401_the_absent_element_searched.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


SEALTXT = io.open(os.path.join(D, 'b401_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = J('b401_lockgate')
X = J('b401_extract')
CF = J('b401_components')
READS = len(X['reads'])
ANCH = sum(1 for r in X['reads'] if r['verdict'].startswith('ANCHORED'))
SRCN = len(X['srcreads'])
SRCOK = sum(1 for s in X['srcreads'] if s['pages'])
TOOLS = [n for n in sorted(os.listdir(os.path.join(ROOT, 'tools')))
         if n.startswith('b401_') and n.endswith('.py')]

# ### **THE TWO CELL APPENDS. ### APPENDED, NEVER REWRITTEN.**
CELL4_ADD = (
    ' ### **(iv) THE PRIME CONSTITUENT AT A WIDENED SUPPORT**, added 2026-09-10 (b401): the record '
    'holds b321’s **ten values** of `Σ_p W_p(f)` at cells above the boundary, indexed by '
    'the width `a`, and `(Q400)` needs **one statement uniform in `a`** — any statement '
    'evaluating or bounding `Σ_p W_p(f)` at `a² ≥ 2` against an archimedean quantity. '
    'b401 searched both pinned sources and 4536 corpus files by five matcher shapes and confirmed '
    'that statement **ABSENT**; what it located instead is Lagarias Theorem 6.1, '
    '`S_f(n,π) = λ_n(n,π) + O(n log n)` **unconditionally** — on the *other* '
    'family, against the *zeros*, and already owned by b358. Its correction term is **uniform in '
    'the prime and vacuously so, carrying no prime index at all**, and by its own words the implied '
    'constant **depends on π**. ### **SO THIS IS A FOURTH INSTANCE OF THE OBSTRUCTION AND NOT '
    'A CRACK IN IT.** ### **AND WHAT IT SHARES WITH (iii) IS SAID HERE RATHER THAN LEFT TO BE '
    'NOTICED: (iii) AND (iv) SHARE AN INDEX — THE SUPPORT WIDTH — AND DIFFER IN OBJECT**, '
    '(iii) being about the admissible *class* at a support and (iv) about a *constituent’s '
    'value* at one. **Two questions about different things, indexed the same way; a fourth row '
    'sharing an index with a third is exactly where one obstruction gets counted twice, so the '
    'sharing is on the face of the entry.**')

CELL6_ADD = (
    ' ### **RESTATED 2026-09-10 (b401) FOR A FOURTH INSTANCE, AND THE REFUSAL IS RESTATED WITH IT '
    'RATHER THAN SUMMARISED.** The row’s law now governs **four**: *NOTHING IS CLAIMED ABOUT '
    'THE EQUIVALENCE OF* them, *a row naming things that look alike is exactly where an equivalence '
    'gets compiled by accident*, and this row *names a resemblance of SHAPE and types no bridge '
    'between* them, *in either direction*. **b401 types no bridge between any two of the four — '
    'least of all between (iii) and (iv), which share an index.** Three obstructions that rhyme are '
    'three obstructions; **so are four, and two of them rhyming more closely does not make them '
    'one.** NOTHING IS PAID HERE, NO GRADE IS CONFERRED, AND NO EQUIVALENCE IS COMPILED.')

DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', 'PARKED'),
    ('the instrument-audit lane, PARKED under ruling R22', 'STAND',
     'PARKED, and it is what forbids repairing the stale README count this act found'),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', 'each still carries its owner'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', 'no act sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', 'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', 'ROUTED to the author'),
    ("the census's definition-versus-operation drift", 'STAND', 'FILED at b377, NOT REPAIRED'),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     'OPEN. ### **TRIGGER: when a row of it is cited by an act.**'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade. ### **TRIGGER: when a grade must be defended.**'),
    ('LIST 3 -- the undated figures across the roster', 'STAND',
     'OPEN. ### This act dates none. ### **TRIGGER: when a figure is quoted forward.**'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     'OPEN. ### **TRIGGER: at the next bibliography pass.**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', 'OPEN AND THE AUTHOR`S'),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the deposited layer, unread since b389', 'STAND', 'STILL BLOCKED; the platform was not asked'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('the five deafnesses of b396`s sweep', 'STAND', 'FILED at b396'),
    ('the keystones` stale `HELD` prose', 'STAND', 'ROUTED at b397, OPEN'),
    ('the two deposited records` remediation', 'STAND', 'DRAFTED at b395, TRIGGERED at b397'),
    ('the `82` at-risk figures', 'STAND', 'TRIGGERED at b397, and PARKED by `(R22)`'),
    ('`(N)`, the smallest next statement toward the clause', 'STAND',
     'NAMED at b398, NOT ATTEMPTED there and NOT ATTEMPTED here. ### **OPEN**'),
    ('the grade move inside b332`s E0 ranking table', 'STAND',
     'ROUTED at b399, trigger THE AUTHOR`S WORD. ### **OPEN**'),
    ('`b321`s prime-power rule against its own printed list', 'STAND',
     'ROUTED at b400 and ### **STILL ROUTED**. ### The `<=` in the rule against the `<` in the '
     'list, disagreeing at `2` of `13` cells and moving no value. ### **NOT REPAIRED HERE**'),
    ('the write-list arms `b400` left failing', 'STAND',
     '### `b400`s `G-WRITELIST` and `G-WRITELIST-KIND` failed and were not weakened. ### **b401 '
     'BUILT ITS LIST AS KINDS, WHICH IS THE REPAIR OF THE SPECIES AND NOT OF `b400`S FACE.** ### '
     'The locked face of `b400` is not edited. ### **FILED**'),
    ('`(Q400)`, the prime constituent at a support where the primes enter', 'STAND',
     '### **OPEN, AND NOW WITH ITS ABSENCE CONFIRMED BY SEARCH RATHER THAN BY A CONSTRAINT SET.** '
     '### `b401` looked, in both pinned sources and `4536` corpus files by `5` matcher shapes, and '
     'the statement it needs is ### **NOT THERE.** ### **NOT OPENED**'),

    # ---- WHAT THIS ACT CLOSES --------------------------------------------------------------------
    ('whether `b400`s absent element is absent by search or only by argument', 'CLOSE',
     '### **CLOSED BY A PRINTED SEARCH, AND THE ANSWER IS THAT IT IS ABSENT.** ### Five matcher '
     'shapes over `4536` files and both verified sources at content; every yield printed and every '
     'residue hand-read. ### **AND THE SEARCH`S REAL YIELD IS THE OTHER HALF:** ### the KIND of '
     'statement is not absent -- Lagarias Theorem `6.1` bounds a finite-place contribution '
     'UNCONDITIONALLY, on the other family, against the zeros, and ### **THE RECORD ALREADY OWNED '
     'IT AT `b358`.**'),
    ('whether the corpus`s one-prime window is the same object as `(Q400)`', 'CLOSE',
     '### **CLOSED BY UNFOLDING AND NOT BY THE SHARED WORD `WINDOW`: ### IT IS NOT.** ### '
     '`SIDE-window` bounds a COUNT of prime powers below an integer bound, at no support at all -- '
     'its own README says the windows are half-vacuous, that `W` has nothing to do with the '
     'corpus`s `W_2` / `W_inf`, and that ### *nothing here bears on the sign of `W_inf - W_2`.* '
     '### **ONE IS A WEIGHTED SUM AGAINST A TEST FUNCTION; THE OTHER IS A CARDINALITY**'),

    # ---- WHAT THIS ACT ADDS ----------------------------------------------------------------------
    ('a uniformity that holds because its index is absent', 'STAND',
     '### **NEW at `b401`, AND IT IS THE ACT`S SHARPEST SENTENCE.** ### Theorem `6.1`s correction '
     'term is uniform in the prime ### **BECAUSE IT CARRIES NO PRIME INDEX AT ALL** -- and a '
     'uniformity that holds because the index is absent is not a uniform bound in that index, it '
     'is a bound about a different object. ### `b399`s vacuity species at a second site. ### '
     '**OPEN, AND REFUSABLE**'),
    ('the source is uniform on the archimedean channel and not on the finite one', 'STAND',
     '### **NEW at `b401`.** ### Theorem `5.1`s implied constant is ### **ABSOLUTE** ### (`b358`); '
     'Theorem `6.1`s ### **DEPENDS ON THE REPRESENTATION**, by its own words. ### **THE ASYMMETRY '
     'IS BETWEEN THE TWO CHANNELS AND IT RUNS THE WRONG WAY FOR THE BRIDGE.** ### **OPEN**'),
    ('`SIDE-window`s README terminal count, stale against its own head', 'STAND',
     '### **NEW at `b401`, AND FOUND ONLY BY READING IT WHOLE.** ### The headline says `43` '
     'terminals; the repository`s five `AxiomCheck` files carry `69` `#print axioms` invocations '
     'and the terminal tables do not mention the local model `HEAD`s own commit message names as '
     '`v0.5`. ### **EXACT WHEN WRITTEN, STALE AGAINST ITS OWN HEAD** -- `b371`s species at a '
     'second repository. ### **ROUTED, NOT REPAIRED:** ### another repository`s file, and the '
     'instrument-audit lane is PARKED. ### **OPEN**'),
    ('the axiom claim of `SIDE-window`, neither confirmed nor denied', 'STAND',
     '### **NEW at `b401` AS A DECLARED WEAKNESS AND NOT AS A FINDING.** ### The profile was read '
     'from what the repository PRINTS and not from a run, because the instrument lane is PARKED. '
     '### **A QUOTED HEADLINE IS NOT A MEASUREMENT**, and the stale count above is exactly what '
     'that weakness costs. ### **OPEN**'),
]


def do_desk():
    rec('    ### ### **THIS LEG CLOSES TWO ITEMS AND OPENS FOUR.**')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 1400), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    rec('    ### ### **AND NOTHING IS PAID:** ### `0` grades conferred, `0` rows paid.')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0)


# ==================================================================================================
def do_faces():
    """### **ROW `U1`, TWO CELLS APPENDED TO, CHECKED CELL BY CELL.**"""
    before = io.open(FACES, encoding='utf-8', newline='').read()
    lines = before.split(chr(10))
    idx = [i for i, ln in enumerate(lines) if ln.startswith('| U1 |')]
    if len(idx) != 1:
        rec('  ### HARD FAILURE -- expected exactly one `U1` row, found %d.' % len(idx))
        return False, 0
    i = idx[0]
    old = lines[i]
    oldc = GD.split_cells(old)
    rec('  ### the row splits into %d cells on its UNESCAPED pipes' % len(oldc))
    if len(oldc) != 7:
        rec('  ### HARD FAILURE -- expected 7 cells.')
        return False, 0
    if 'b401' in old:
        rec('  ### ALREADY FILED -- the b401 segment is present. ### NOTHING APPENDED.')
        return True, 2
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
    rec('  ### lines %d -> %d ; LOST %d' % (len(bl), len(al), len(bl) - len(al)))
    untouched = sum(1 for k, (a, b) in enumerate(zip(bl, al)) if a == b)
    rec('  ### lines UNCHANGED : %d of %d ### (every line but the row)' % (untouched, len(bl)))
    ok = ok and untouched == len(bl) - 1
    backc = GD.split_cells(al[i])
    rec('  ### the row re-splits into %d cells' % len(backc))
    ok = ok and len(backc) == 7
    for k in range(7):
        if k in (4, 6):
            good = backc[k].startswith(oldc[k].rstrip()) and len(backc[k]) > len(oldc[k])
            rec('      cell %d  APPENDED TO   : prior text a TRUE PREFIX : %-5s   %d -> %d bytes'
                % (k, good, len(oldc[k].encode('utf-8')), len(backc[k].encode('utf-8'))))
        else:
            good = backc[k] == oldc[k]
            rec('      cell %d  UNTOUCHED     : BYTE-IDENTICAL : %s' % (k, good))
        ok = ok and good
    for lbl, cond in (('the row still reads `U1`', al[i].startswith('| U1 |')),
                      ('the fourth instance is present', '**(iv) THE PRIME CONSTITUENT' in al[i]),
                      ('the shared index is named', 'SHARE AN INDEX' in al[i]),
                      ('the refusal is restated', 'types no bridge' in al[i]),
                      ('no equivalence is claimed', 'NO EQUIVALENCE IS COMPILED' in al[i])):
        ok = ok and cond
        rec('      %-38s : %s' % (lbl, cond))
    rec('  ### ### **%s**' % ('PASS' if ok else '### FAIL ###'))
    return ok, 2


# ==================================================================================================
def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b401 — the absent element searched, and the fourth site entered — filed 2026-09-10',
        '',
        '**b400 named `(Q400)`’s one absent element from a constraint set and not from a search. '
        'This leg searched, and the element is ABSENT — but the search’s real yield is the other '
        'half.** Five matcher shapes over **4536** corpus files and both pinned sources at content, '
        'every yield printed and every residue hand-read. What is absent: any statement evaluating '
        'or bounding `Σ_p W_p(f)` at `a² ≥ 2` against an archimedean quantity. What is **present**: '
        '**Lagarias Theorem 6.1** — *for any irreducible cuspidal unitary automorphic '
        'representation on GL(N) there holds* `S_f(n,π) = λ_n(n,π) + O(n log n)`, **unconditionally** '
        '— so a bound on a finite-place contribution exists, in a source this corpus has pinned, '
        '**and b358 already owned it**. **THE ELEMENT IS ABSENT; THE KIND OF ELEMENT IS NOT.**',
        '',
        '**Why it is not the missing element — three reasons, each named.** (i) **Wrong family**: it '
        'is on the Li family `G_n`, whose members have no compact support and lie outside Theorem '
        '1’s class — it is not the Sonin family at any support, because it is not indexed by a '
        'support at all. (ii) **Wrong comparison quantity**: it bounds against the *incomplete Li '
        'coefficient* `λ_n(T,π)`, a sum over **zeros** to a height, not an archimedean quantity. '
        '(iii) **Its hypothesis is not of a kind the Sonin side can carry**: it quantifies over the '
        '**representation**, not the test function, and for the corpus’s own object it holds under '
        'the source’s stated convention — `H-CUSP`, graded by b358 and **inherited, not decided**, '
        'by b361, and **not decided here either**. And the other source’s near-misses are all at '
        'the wrong support in the wrong direction: Theorem 1 and Theorem 6.11 are both at the '
        'narrow interval, and the source’s own preliminary positivity is proved *for small enough '
        'intervals* — **its machinery runs toward narrow, not wide** — while the widening it names '
        'it **does not take**.',
        '',
        '**ADDITION ONE — the uniformity question, asked before the fourth site: UNIFORM, AND '
        'VACUOUSLY.** The correction term is `O(n log n)` in the Li index, and **it carries no prime '
        'index at all** — `S_f(n,π)` is one quantity summed over every finite place at once. So it '
        'is uniform in the prime **because there is no prime in it to be uniform in**. **A '
        'uniformity that holds because the index is absent is not a uniform bound in that index; it '
        'is a bound about a different object** — b399’s vacuity species at a second site. So the '
        'order’s UNIFORM branch is entered and **its consequence is not drawn**: this is not the '
        'class-level statement the uniformity row has been missing, and **no prime-by-prime opening '
        'is priced**. And the one index the term does carry is not uniform either — the implied '
        'constant **depends on π** by the theorem’s own words, against Theorem 5.1’s, which b358 '
        'banked as **ABSOLUTE**. **The source is uniform where the archimedean channel is concerned '
        'and not where the finite one is, and that asymmetry runs the wrong way for the bridge.**',
        '',
        '**ADDITION TWO — the corpus’s own one-prime window, read whole: a DIFFERENT OBJECT, and '
        'the kernel says so itself.** `SIDE-window` (pin `aacb415`) bounds **a count** — `W n`, the '
        'number of prime powers below `n` — **at no support at all**: its README states that the '
        'windows are half-vacuous, *the lower endpoint never binds*, that *`W` is tabulated, not '
        'characterized*, that *`W` HAS NOTHING TO DO WITH THE CORPUS’S `W_2` / `W_∞`*, and that '
        '*nothing here bears on the sign of `W_∞ − W_2`*. **One is a weighted sum against a test '
        'function; the other is a cardinality.** Decided by unfolding, not by the shared word '
        '“window”. b16’s staircase agrees with the compiled rungs by **two independent routes '
        'sharing no code** — Python arithmetic over a grid against a Lean `decide` over naturals — '
        '**and that buys confidence in the count and nothing about the sum.**',
        '',
        '**And reading it whole found what reading it by name would not: a stale count on its own '
        'README.** The headline says **43 terminals**, all axiom-free; the repository’s five '
        '`AxiomCheck` files carry **69** `#print axioms` invocations, and the terminal tables do '
        'not mention the local model that `HEAD`’s own commit message names as `v0.5`. **Exact when '
        'written, stale against its own head** — b371’s species at a second repository. **Routed, '
        'not repaired**: another repository’s file, and the instrument-audit lane is PARKED under '
        '(R22). And **the axiom claim itself is neither confirmed nor denied here** — it was read '
        'from a printed profile and not from a run, because the instrument lane is PARKED. **A '
        'quoted headline is not a measurement, and the stale count is exactly what that weakness '
        'costs.**',
        '',
        '**COMPONENT 2 — the fourth site: ENTERED, with its shared index named on the face of the '
        'entry.** `(Q400)` fits row `U1`’s shape exactly — the record holds b321’s ten values of '
        '`Σ_p W_p(f)` indexed by `a`, and needs one statement uniform in `a`. Addition One decides '
        'which it is: the one bound located is uniform **only where no index exists** and is '
        'explicitly not uniform in the one index it carries, so **`(Q400)` is a fourth instance of '
        'the obstruction and not the first crack in it**. **And (iii) and (iv) share an index — the '
        'support width — and differ in object**: (iii) is about the admissible *class* at a '
        'support, (iv) about a *constituent’s value* at one. Two questions about different things, '
        'indexed the same way. **A fourth row sharing an index with a third is exactly where one '
        'obstruction gets counted twice, so the sharing is stated in the entry itself**, the row’s '
        'refusal is restated **verbatim**, and **no bridge is typed between any two of the four — '
        'least of all between the two that share an index.** Three obstructions that rhyme are '
        'three obstructions; so are four.',
        '',
        '**The `≤` against `<` discrepancy b400 routed on b321’s face stays ROUTED and is not '
        'repaired here.** **The four lists stay OPEN by name**, each with its trigger: LIST 1 — '
        'when a row of it is cited; LIST 2 — when a grade must be defended; LIST 3 — when a figure '
        'is quoted forward; LIST 4 — at the next bibliography pass. **This leg closes none of '
        'them.**',
        '',
        '*No grade moved or was conferred. No equivalence is compiled. No kernel was built and no '
        'instrument was run. Nothing deposits and the platform was not called at all. h2 stands '
        'exactly where the deposit left it and this leg makes no claim about it in either '
        'direction.*',
        '',
    ]


SCOPE = (
    "**SCOPE: THE ABSENT ELEMENT SEARCHED, AND THE FOURTH SITE ENTERED.** b400 named (Q400)'s one "
    "absent element from a CONSTRAINT SET and not from a search; this leg searched, by 5 matcher "
    "shapes over 4536 corpus files and both pinned sources at content, every yield printed and "
    "every residue hand-read. **COMPONENT 1: PRESENT BUT NOT APPLICABLE.** What is absent: any "
    "statement evaluating or bounding SUM_p W_p(f) at a^2 >= 2 against an archimedean quantity. "
    "What is PRESENT: Lagarias Theorem 6.1, `S_f(n,pi) = lambda_n(n,pi) + O(n log n)` "
    "UNCONDITIONALLY -- so a bound on a finite-place contribution exists in a pinned source, and "
    "**b358 ALREADY OWNED IT**. **THE ELEMENT IS ABSENT; THE KIND OF ELEMENT IS NOT.** It is not "
    "the missing element for THREE named reasons: (i) WRONG FAMILY -- the Li family has no compact "
    "support and is not indexed by a support at all; (ii) WRONG COMPARISON QUANTITY -- it bounds "
    "against the incomplete Li coefficient, a sum over ZEROS, not an archimedean quantity; (iii) "
    "ITS HYPOTHESIS QUANTIFIES OVER THE REPRESENTATION and for the corpus's object holds under the "
    "source's own convention -- H-CUSP, graded by b358, INHERITED by b361 and NOT DECIDED HERE. "
    "And CC's near-misses are all at the NARROW support: Theorem 1 and Theorem 6.11 both, with the "
    "source's preliminary positivity proved *for small enough intervals* -- **ITS MACHINERY RUNS "
    "TOWARD NARROW, NOT WIDE** -- and the widening it names it DOES NOT TAKE. **ADDITION ONE: "
    "UNIFORM -- AND VACUOUSLY.** The correction term O(n log n) CARRIES NO PRIME INDEX AT ALL, so "
    "it is uniform in the prime because there is no prime in it to be uniform in; **A UNIFORMITY "
    "THAT HOLDS BECAUSE THE INDEX IS ABSENT IS NOT A UNIFORM BOUND IN THAT INDEX, IT IS A BOUND "
    "ABOUT A DIFFERENT OBJECT**, b399's vacuity species at a second site. The UNIFORM branch is "
    "entered and ITS CONSEQUENCE IS NOT DRAWN: no prime-by-prime opening is priced. And the one "
    "index it does carry is not uniform either -- the implied constant DEPENDS ON pi, against "
    "Theorem 5.1's ABSOLUTE constant. **ADDITION TWO: A DIFFERENT OBJECT, DECIDED BY UNFOLDING.** "
    "SIDE-window (pin aacb415) bounds a COUNT of prime powers below an integer bound, at NO "
    "SUPPORT AT ALL -- half-vacuous windows, the lower endpoint never binding -- and its own README "
    "says W HAS NOTHING TO DO WITH THE CORPUS'S W_2 / W_inf and that nothing there bears on the "
    "sign of W_inf - W_2. (N3) MET. And reading it WHOLE found a STALE COUNT on its own README: 43 "
    "terminals claimed against 69 `#print axioms` invocations, the tables omitting the v0.5 local "
    "model HEAD's own commit message names -- b371's species at a second repository, ROUTED not "
    "repaired. The axiom claim is NEITHER CONFIRMED NOR DENIED: read from a printed profile and "
    "not from a run, the lane being PARKED. **COMPONENT 2: ENTERED, WITH ITS SHARED INDEX NAMED.** "
    "(Q400) fits U1's shape, and Addition One makes it a FOURTH INSTANCE OF THE OBSTRUCTION AND "
    "NOT THE FIRST CRACK IN IT. **(iii) AND (iv) SHARE AN INDEX -- THE SUPPORT WIDTH -- AND DIFFER "
    "IN OBJECT**, and the sharing is stated in the entry because a fourth row sharing an index "
    "with a third is where one obstruction gets counted twice; the row's refusal is restated "
    "VERBATIM and NO BRIDGE IS TYPED between any two of the four. NO GRADE MOVED OR CONFERRED, NO "
    "FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO "
    "REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NEITHER MAP TOUCHED, NO CLUSTER RESHAPED, NO LIST "
    "CLOSED, NO PRIOR ACT'S FACE BANK OR INSTRUMENT EDITED, NO EQUIVALENCE COMPILED. NOTHING "
    "DEPOSITS; **THE PLATFORM WAS NOT CALLED AT ALL**; 0 BRANCHES TOUCHED, 0 CLONES, 0 BUILDS, 0 "
    "INSTRUMENT RUNS, NO .lean FILE TOUCHED, NO .git/hooks/pre-push DELETED. THE INSTRUMENT LANE "
    "AND THE INSTRUMENT-AUDIT LANE STAY PARKED. THE WAVE STAYS PARKED. M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME WITH "
    "THEIR TRIGGERS. The <= against < discrepancy b400 routed stays ROUTED. **THE CLAUSE HAS NOT "
    "MOVED, (Q400) IS NOT OPENED, AND NO COORDINATE IS CLOSED.** h2 stands exactly where the "
    "deposit left it and this leg makes no claim about it in either direction.")


def corr_rows(Q):
    m = ("**THE ABSENT ELEMENT IS CONFIRMED ABSENT BY SEARCH, THE KIND OF ELEMENT IS NOT ABSENT AT "
         "ALL, AND THE UNIFORMITY THAT WOULD HAVE CRACKED IT IS VACUOUS** (b401, the absent element "
         "searched)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b401, %d gates read and %d checked "
            "by digest. %d reads, %d ANCHORED; %d source fragments, %d located in artefacts "
            "VERIFIED against the corpus's banked digests BEFORE a word was read. **COMPONENT 1 -- "
            "PRESENT BUT NOT APPLICABLE:** %d matcher shapes over 4536 corpus files, every yield "
            "printed and every residue hand-read; the statement (Q400) needs is ABSENT, and what "
            "is present is Lagarias Theorem 6.1 bounding a finite-place contribution "
            "UNCONDITIONALLY -- on the other family, against the zeros, and ALREADY OWNED AT b358 "
            "-- not it for %d named reasons. **ADDITION ONE -- UNIFORM, AND VACUOUSLY:** the "
            "correction term carries NO PRIME INDEX AT ALL, and a uniformity holding because the "
            "index is absent is a bound about a different object; the implied constant DEPENDS ON "
            "pi against Theorem 5.1's ABSOLUTE one. **ADDITION TWO:** SIDE-window bounds a COUNT "
            "at NO SUPPORT and its own README says so; and reading it whole found its terminal "
            "count STALE against its own head, %d claimed against %d `#print axioms` invocations, "
            "ROUTED not repaired. **COMPONENT 2:** the fourth site ENTERED with its shared index "
            "named -- (iii) and (iv) share the support width and differ in object. %d GRADES "
            "MOVED, %d ROWS PAID, %d EQUIVALENCES COMPILED, %d CONTENT LOST, %d KERNELS BUILT"
            % (LG['gates_read'], LG['face_subject_gates'], READS, ANCH, SRCN, SRCOK,
               CF['matcher_shapes'], CF['reasons'], CF['readme_claim'],
               CF['axiom_prints_total'], 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS LEG AS ITS OWN, AND NONE IS OPENED. ### NO "
            "INSTRUMENT WAS RUN, NO KERNEL BUILT, NO OBJECT RECOMPUTED, NO BRANCH TOUCHED AND NO "
            ".lean FILE TOUCHED. ### THE `SIDE-window` TERMINALS ARE READ FROM A PRINTED PROFILE "
            "AND NOT FROM A RUN, AND THE ACT SAYS SO RATHER THAN LETTING A QUOTED HEADLINE PASS "
            "FOR A MEASUREMENT. ### CONFIRMING AN ABSENCE IS NOT SUPPLYING WHAT IS ABSENT")
    prof = ("### NO AXIOM PROFILE IS ASSERTED OR RECOMPUTED, AND THE ONE QUOTED IS DECLARED AS "
            "QUOTED. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE "
            "STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE "
            "CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO EQUIVALENCE COMPILED. ### "
            "THE CORPUS WRITES ARE TWO CELLS OF ONE LEDGER ROW, APPENDED TO AND CHECKED CELL BY "
            "CELL, AND ONE APPEND-ONLY TRAIL BLOCK -- 0 CONTENT LOST")
    grade = ("### THE ABSENCE IS ESTABLISHED BY A SEARCH WHOSE EVERY MATCHER PRINTS ITS WHOLE YIELD "
             "AND WHOSE RESIDUE IS HAND-READ, AT FIVE SHAPES RATHER THAN ONE. ### THE UNIFORMITY "
             "VERDICT CARRIES THE WORD THAT SCOPES IT IN THE SAME SENTENCE. ### WHERE THE RECORD "
             "ALREADY OWNED A SOURCE STATEMENT THE ACT CITES THE OWNING ACT RATHER THAN IMPORTING "
             "IT AGAIN, AND LEAVES AN INHERITED HYPOTHESIS INHERITED. ### THE ONE-PRIME WINDOW IS "
             "DECIDED BY UNFOLDING AND NOT BY A SHARED WORD. ### THE FOURTH INSTANCE NAMES THE "
             "INDEX IT SHARES WITH THE THIRD, BECAUSE THAT IS WHERE ONE OBSTRUCTION GETS COUNTED "
             "TWICE. ### AND THE ONE FINDING ABOUT ANOTHER REPOSITORY IS PRINTED AND ROUTED RATHER "
             "THAN REPAIRED")
    status = ("data/b401_the_absent_element_searched.txt; data/b401_components_run.txt; "
              "data/b401_extract_notes.txt; data/b401_registration_2026-09-10.txt (LOCKED before "
              "any write at sha256 %s, chained on tools/b378_lockgate.py run as b401); "
              "tools/b401_extract.py; tools/b401_regspec.py; tools/b401_reg_gate.py; "
              "tools/b401_components.py; tools/b401_desk_bank.py; tools/b401_checks.py; "
              "PLACE-papers FACES_LEDGER.md (row U1, two cells appended to) and OPEN_TRAILS.md "
              "(one append-only block); CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('is there a bound on the prime sum at a wider support',
           'does the record hold an unconditional finite place bound',
           'is the li coefficient bound uniform in the prime',
           'does the one prime window bound the weil sum',
           'is q400 a fourth instance of the uniformity obstruction',
           'what does side-window actually prove')
MUST_NOT_HIT = ('the bound was found', 'the window was opened', 'a kernel was built',
                'the obstruction was cracked', 'an equivalence was compiled')

KEY = 'the-absent-element-searched'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b401 SEARCHED FOR (Q400)'S ONE ABSENT ELEMENT RATHER THAN ASSUMING IT ABSENT, AND THE "
        "VERDICT IS **PRESENT BUT NOT APPLICABLE**. Five matcher shapes over 4536 corpus files and "
        "both pinned sources at content, every yield printed and every residue hand-read. **WHAT IS "
        "ABSENT**: any statement evaluating or bounding SUM_p W_p(f) at a^2 >= 2 against an "
        "archimedean quantity. **WHAT IS PRESENT**: Lagarias Theorem 6.1 -- *for any irreducible "
        "cuspidal unitary automorphic representation on GL(N) there holds* S_f(n,pi) = "
        "lambda_n(n,pi) + O(n log n) -- **UNCONDITIONALLY**, and **b358 ALREADY OWNED IT**. **THE "
        "ELEMENT IS ABSENT; THE KIND OF ELEMENT IS NOT.** It is not the missing element for three "
        "named reasons: WRONG FAMILY (the Li family has no compact support and is not indexed by a "
        "support at all); WRONG COMPARISON QUANTITY (it bounds against the incomplete Li "
        "coefficient, a sum over ZEROS, not an archimedean quantity); and ITS HYPOTHESIS "
        "QUANTIFIES OVER THE REPRESENTATION, holding for the corpus's object only under the "
        "source's own convention -- H-CUSP, graded by b358, INHERITED by b361, NOT DECIDED HERE. "
        "CC's near-misses are all at the NARROW support and its machinery runs TOWARD NARROW, NOT "
        "WIDE; the widening it names it does not take. **ADDITION ONE: UNIFORM -- AND VACUOUSLY.** "
        "The correction term O(n log n) CARRIES NO PRIME INDEX AT ALL, so it is uniform in the "
        "prime because there is no prime in it to be uniform in -- **A UNIFORMITY THAT HOLDS "
        "BECAUSE THE INDEX IS ABSENT IS NOT A UNIFORM BOUND IN THAT INDEX; IT IS A BOUND ABOUT A "
        "DIFFERENT OBJECT.** The UNIFORM branch is entered and ITS CONSEQUENCE IS NOT DRAWN: no "
        "prime-by-prime opening is priced. The implied constant DEPENDS ON pi, against Theorem "
        "5.1's ABSOLUTE one. **ADDITION TWO: A DIFFERENT OBJECT.** SIDE-window bounds a COUNT of "
        "prime powers below an integer bound, at NO SUPPORT AT ALL, and its README says W HAS "
        "NOTHING TO DO WITH THE CORPUS'S W_2 / W_inf. Reading it whole found its terminal count "
        "STALE AGAINST ITS OWN HEAD -- 43 claimed against 69 `#print axioms` invocations -- ROUTED "
        "not repaired. **COMPONENT 2: THE FOURTH SITE ENTERED, WITH ITS SHARED INDEX NAMED** -- "
        "(iii) and (iv) share the support width and differ in object, and no bridge is typed "
        "between any two of the four.")
    grade = (
        "### NO INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED. ### THE SIDE-window "
        "AXIOM PROFILE IS READ FROM A PRINTED PROFILE AND NOT FROM A RUN, AND THE ACT DECLARES THAT "
        "AS WEAKER. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK "
        "OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT "
        "EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO EQUIVALENCE COMPILED. ### THE CORPUS "
        "WRITES ARE TWO CELLS OF ROW U1, APPENDED TO AND CHECKED CELL BY CELL WITH THE OTHER FIVE "
        "BYTE-IDENTICAL, AND ONE APPEND-ONLY TRAIL BLOCK -- 0 CONTENT LOST. ### AN INHERITED "
        "HYPOTHESIS IS LEFT INHERITED. ### A STALE COUNT FOUND ON ANOTHER REPOSITORY'S README IS "
        "PRINTED AND ROUTED, NOT REPAIRED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT "
        "ALL. ### THE CLAUSE HAS NOT MOVED, (Q400) IS NOT OPENED, AND NO COORDINATE IS CLOSED. ### "
        "THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED")
    where = (
        "data/b401_the_absent_element_searched.txt; data/b401_components_run.txt; "
        "data/b401_extract_notes.txt; data/b401_registration_2026-09-10.txt (LOCKED before any "
        "write, chained on tools/b378_lockgate.py run as b401 -- %d gates read, %d checked by "
        "digest); tools/b401_extract.py; tools/b401_regspec.py; tools/b401_reg_gate.py; "
        "tools/b401_components.py; tools/b401_desk_bank.py; tools/b401_checks.py; PLACE-papers "
        "FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b401 (the absent element is absent by search; the kind of element is not; and the '
           'uniformity that would have cracked it is vacuous)')
    row_new = ('    # ### THE ABSENT ELEMENT SEARCHED (b401).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-44s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-56s reaches the b401 key : %s' % (qq, g2))
    for lbl, cond in (
            ('the verdict is present-but-not-applicable', 'PRESENT BUT NOT APPLICABLE' in out),
            ('the absence is by search', '4536 corpus files' in out),
            ('the located theorem is named', 'Theorem 6.1' in out),
            ('the element/kind distinction is made',
             'THE ELEMENT IS ABSENT; THE KIND OF ELEMENT IS NOT' in out),
            ('the three reasons are there', 'WRONG FAMILY' in out and 'WRONG COMPARISON' in out),
            ('the owning act is credited', 'b358 ALREADY OWNED IT' in out),
            ('the inherited hypothesis stays inherited', 'NOT DECIDED HERE' in out),
            ('the uniformity carries its scoping word', 'UNIFORM -- AND VACUOUSLY' in out),
            ('the consequence is not drawn', 'ITS CONSEQUENCE IS NOT DRAWN' in out),
            ('the one-prime window is a different object', 'at NO SUPPORT AT ALL' in out),
            ('the stale count is on the record', 'STALE AGAINST ITS OWN HEAD' in out),
            ('the shared index is named', 'share the support width' in out),
            ('no bridge is typed', 'no bridge is typed' in out)):
        ok = ok and cond
        rec('    %-56s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


# ==================================================================================================
def bank(Q, rownum, kok, cells):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A('b401 -- THE ABSENT ELEMENT SEARCHED, AND THE FOURTH SITE. ### THE BANK.')
    A('### Ferry part 1 of 1, receipt confirmed IN FULL (Rule 1). ### 2026-09-10.')
    A('### LEG 1 OF A TWO-LEG SORTIE. ### CONCURRENCY: SOLO (research seat).')
    A('### The face was LOCKED before any write at sha256 `%s`.' % SEALHASH)
    A(BAR)
    A('')
    A(SUB)
    A('### THE VERDICTS.')
    A(SUB)
    A('### ### ### **COMPONENT 1 : ### PRESENT BUT NOT APPLICABLE.**')
    A('### ### ### **ADDITION ONE : ### UNIFORM -- AND VACUOUSLY.**')
    A('### ### ### **ADDITION TWO : ### A DIFFERENT OBJECT -- A COUNT, AT NO SUPPORT AT ALL.**')
    A('### ### ### **COMPONENT 2 : ### ENTERED, WITH ITS SHARED INDEX NAMED.**')
    A('')
    A(SCOPE)
    A('')
    A(SUB)
    A('### WHAT THE LEG WROTE, AND WHAT IT DID NOT.')
    A(SUB)
    A('### **THE LEDGER WRITE** ### -- `%d` cells of row `U1` in `FACES_LEDGER.md`, APPENDED TO'
      % cells)
    A('### and checked CELL BY CELL, the other five coming back ### **BYTE-IDENTICAL**; one')
    A('### append-only block in `OPEN_TRAILS.md`. ### **`0` CONTENT LOST. ### `0` GRADES MOVED.')
    A('### ### `0` ROWS PAID. ### `0` EQUIVALENCES COMPILED.**')
    A('### **THE DESK** ### -- `%d` items swept, `%d` closed, `%d` standing, `%d` lists closed.'
      % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    A('### **THE SURVEY** ### -- `%d` reads, `%d` ANCHORED; `%d` source fragments, `%d` located in'
      % (READS, ANCH, SRCN, SRCOK))
    A('### artefacts VERIFIED against the corpus`s banked digests BEFORE a word was read.')
    A('### **THE SEARCH** ### -- `%d` matcher shapes over `4536` files, every yield printed.'
      % CF['matcher_shapes'])
    A('### **THE GATE CHAIN** ### -- `%d` gates read, `%d` passing, `%d` checked by digest.'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A('### **THE ROW AND THE KEY** ### -- correspondence row `%d`; index key `%s` : %s.'
      % (rownum, KEY, 'PASS' if kok else 'FAIL'))
    A('')
    A(SUB)
    A('### THE ONE FINDING ABOUT ANOTHER REPOSITORY, PRINTED AND ROUTED.')
    A(SUB)
    A('### `SIDE-window`s README headline claims ### **`%d` TERMINALS**, all axiom-free; the'
      % CF['readme_claim'])
    A('### repository`s five `AxiomCheck` files carry ### **`%d` `#print axioms` INVOCATIONS**, and'
      % CF['axiom_prints_total'])
    A('### the README`s terminal tables do not mention the local model `HEAD`s own commit message')
    A('### names as `v0.5`. ### **EXACT WHEN WRITTEN, STALE AGAINST ITS OWN HEAD** -- `b371`s')
    A('### species at a second repository. ### **ROUTED, NOT REPAIRED:** ### it is another')
    A('### repository`s file and the instrument-audit lane is PARKED under `(R22)`.')
    A('### ### **AND THE AXIOM CLAIM IS NEITHER CONFIRMED NOR DENIED HERE.** ### It was read from')
    A('### a PRINTED PROFILE and not from a run, the instrument lane being PARKED. ### **A QUOTED')
    A('### ### HEADLINE IS NOT A MEASUREMENT, AND THE STALE COUNT IS EXACTLY WHAT THAT COSTS.**')
    A('')
    A(SUB)
    A('### WHAT THIS LEG DOES NOT SAY.')
    A(SUB)
    A('### It does not say that no such bound could exist -- ### **ONLY THAT NONE IS IN THE RECORD')
    A('### ### OR IN EITHER PINNED SOURCE, BY FIVE MATCHER SHAPES AND A HAND-READ RESIDUE.**')
    A('### It does not decide `H-CUSP`; that grade stays `b358`s and `b361`s.')
    A('### It does not confirm or deny `SIDE-window`s axiom claim, and it builds nothing.')
    A('### It does not open `(Q400)`, and it types no bridge between any two instances of `U1`.')
    A('### It does not repair `b321`s convention split, `b400`s write list, or another')
    A('### repository`s README. ### **PRINTED, ROUTED, AND LEFT.**')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### h2 STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS LEG MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    rec('  ### bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))


# ==================================================================================================
def main():
    bar('=')
    rec('b401 -- THE DESK, THE LEDGER WRITE, AND THE BANK.')
    bar('=')
    bar()
    rec('  ### THE DESK UNDER (R7).')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### ROW `U1`, TWO CELLS APPENDED TO, CHECKED CELL BY CELL.')
    bar()
    fok, cells = do_faces()
    if not fok:
        run_clock.write(D, 'b401_desk_notes', LINES)
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
        rec('  ### the b400 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            run_clock.write(D, 'b401_desk_notes', LINES)
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_absent_by_search': 'the element is absent; the kind of element is not' in low,
        'says_matcher_scope': '4536' in low,
        'says_located': 'theorem 6.1' in low,
        'says_owned': 'b358 already owned it' in low,
        'says_three_reasons': 'wrong family' in low and 'wrong comparison quantity' in low,
        'says_inherited': 'inherited, not decided' in low,
        'says_uniform_vacuous': 'uniform, and vacuously' in low,
        'says_no_pricing': 'no prime-by-prime opening' in low,
        'says_pi_dependent': 'depends on π' in low,
        'says_count_not_sum': 'the other is a cardinality' in low,
        'says_stale': 'stale against its own head' in low,
        'says_not_measurement': 'a quoted headline is not a measurement' in low,
        'says_fourth_instance': 'fourth instance of the obstruction' in low,
        'says_shared_index': 'share an index' in low,
        'says_no_bridge': 'no bridge is typed between any two of the four' in low,
        'says_routed_kept': 'stays routed' in low,
        'says_lists_open': 'the four lists stay open by name' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-28s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b401_desk_notes', LINES)
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
        run_clock.write(D, 'b401_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b401_desk_notes', LINES)
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
            run_clock.write(D, 'b401_desk_notes', LINES)
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
    bank(Q, rownum, kok, cells)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### CELLS %d. ### ROW %d. ### KEY %s. ### BANK '
        'WRITTEN.**' % (Q['items'], Q['closed'], cells, rownum, 'PASS' if kok else 'FAIL'))
    bar('=')
    run_clock.write(D, 'b401_desk_notes', LINES)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
