# -*- coding: utf-8 -*-
"""b400_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK.

### ### **WHAT IT WRITES:** ### the desk sweep under `(R7)`; the three OWED pair rows of the faces
### ledger, APPENDED TO and not rewritten; the append-only trail block; the correspondence row; the
### banked-index key; and the bank.

### ### **AND IT IS THE SIXTH NEW TOOL FILE OF THIS ACT, WHICH THE LOCKED FACE ALREADY NAMES.**
### `b399` sealed `5` and wrote `6`, this file being the one its list omitted; `b400`'s face was
### built by walking the ritual forward from the lock and names all six. ### **A DEFECT NAMED BY
### ### THE ACT THAT COMMITTED IT IS REPAIRED BY THE NEXT ACT'S LIST, NOT BY EDITING ITS FACE.**
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
MARK = '<!-- b400 the bridge restated: two objects on their families, one question at the window -->'
PRIOR = '<!-- b399 (M) tested by sign then refuted by value; the grade move routed -->'
BANKOUT = os.path.join(D, 'b400_the_bridge_restated.txt')

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


SEALTXT = io.open(os.path.join(D, 'b400_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = J('b400_lockgate')
X = J('b400_extract')
F = X['fig']
CF = J('b400_components')
READS = len(X['reads'])
ANCH = sum(1 for r in X['reads'] if r['verdict'].startswith('ANCHORED'))
SRCN = len(X['srcreads'])
SRCOK = sum(1 for s in X['srcreads'] if s['pages'])
TOOLS = [n for n in sorted(os.listdir(os.path.join(ROOT, 'tools')))
         if n.startswith('b400_') and n.endswith('.py')]

# ### **THE b400 SEGMENT APPENDED TO EACH OWED PAIR ROW. ### APPENDED, NEVER REWRITTEN.**
DEPOSIT_REFUSAL = (
    'the deposit, section 27.3: *"compiling the *structure* of the one-premise-in-five-registers '
    'claim while deliberately **not** compiling the cross-register equivalences, since to compile '
    '\'discharge one and you discharge all five\' would be to compile RH-equivalence itself."*')

PAIR_SEG = {
    'F2–F3': (
        ' ### **RESTATED 2026-09-10 (b400), AND STILL OWED — AND WHAT IT WAITS FOR HAS CHANGED '
        'KIND.** With `(M)` refuted, b400 assembled the constraint set and reached the fourth '
        'verdict its order admitted: **(TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE '
        'WINDOW)**. On the source’s lawful class `Σ_p W_p(f) = 0` **identically** — not small, but '
        'zero by the definition of the class, since eq. (149) samples `f` at `p^{±m}` and '
        '`supp(f) ⊂ (1/2, 2)` contains no prime power (the source’s own design sentence, *"so that '
        'rational primes are not involved"*, verified at page index 2 this act). The Li margin’s '
        'archimedean half `λ_A(n) = S_∞(n) + 1` is already owned in closed form, so the only part '
        'a bridge could supply is `λ_Z(n) = −S_f(n)`, which is **not** the zero function. **A '
        'relation carrying an object whose finite channel is identically zero to one whose finite '
        'channel is not would have to supply that channel from outside itself: it is not a '
        'transport of a quantity but a new statement about the primes.** So **on the lawful '
        'families the relation this row asks for cannot carry anything** — and the word *lawful* '
        'is part of the claim, not a hedge on it: b400 does **not** show that no formula relating '
        'the two indexed families can be written, only that on these families it would carry '
        'nothing, and that a correspondence chosen to make an identity come out is **compiled, not '
        'derived**. **THE DEPOSIT’S REFUSAL STANDS AND IS QUOTED HERE BECAUSE IT IS WHAT FORBIDS '
        'THAT MOVE:** ' + DEPOSIT_REFUSAL + ' **What this row now waits for is `(Q400)`, at the '
        'window: at a support with `a² ≥ 2`, where `Σ_p W_p(f)` is not identically zero, is there '
        'a relation between that prime constituent and `λ_Z(n)`? Typed, priced as a RESULT and '
        '**NOT OPENED**. NOTHING IS PAID HERE, NO GRADE IS CONFERRED, AND NO EQUIVALENCE IS '
        'COMPILED.**'),
    'F2–L1': (
        ' ### **RESTATED 2026-09-10 (b400), AND STILL OWED.** This row says the Sonin margin’s '
        'second term *"no statement in the record carries to a finite-place sum"*. b400 states why '
        'that is not an accident of the record: **on the lawful class there is no finite-place sum '
        'to carry it to** — `Σ_p W_p(f) = 0` identically, by the support condition and eq. (149), '
        'the source having chosen its window so that no prime is involved. **THE PAIR IS THEREFORE '
        'DECLARED TWO OBJECTS ON THEIR FAMILIES**, as rows L1 and L2 already define them, with one '
        'reason of principle added: they differ not only in domain and in second term but in '
        '**arithmetic content, one of them having none by design**. What the row waits for is '
        '`(Q400)` at the window, typed and **not opened**. NO EQUIVALENCE IS COMPILED, and the '
        'deposit’s refusal governs: ' + DEPOSIT_REFUSAL),
    'F3–L1': (
        ' ### **RESTATED 2026-09-10 (b400), AND STILL OWED.** Seen from the Li side the same thing '
        'reads sharper: this row’s *"finite channel is what the Sonin margin does not contain"* is '
        '`λ_Z(n) = −S_f(n)`, and the bench prints it **negative on `n ∈ [156, 186] ∪ [247, 287]`** '
        'while `λ_n` itself stays positive throughout `1 ≤ n ≤ 300` — so the Li side’s finite '
        'channel is live, and the Sonin side’s is identically zero on the lawful class. **TWO '
        'OBJECTS ON THEIR FAMILIES.** The one question left is `(Q400)`, at a support where the '
        'primes enter — where Theorem 1’s bound is gone (its support hypothesis, verified at page '
        'index 3) but **Proposition C.1’s criterion is not** (it carries no support hypothesis at '
        'all, verified at page index 51). Typed, priced, **NOT OPENED**; nothing paid, no grade '
        'conferred, no equivalence compiled.'),
}

DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the uniformity row U1', 'STAND',
     "the row's own refusal stands. ### **AND b400 ADDS A FOURTH SITE OF THE SAME SHAPE AND "
     "TYPES NO BRIDGE TO THE OTHER THREE:** ### `(Q400)` needs one statement uniform in the "
     "support, and the record holds instances indexed by it. ### **THREE OBSTRUCTIONS THAT RHYME "
     "ARE THREE OBSTRUCTIONS, AND SO ARE FOUR**"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', 'PARKED'),
    ('the instrument-audit lane, PARKED under ruling R22', 'STAND', 'PARKED at b397'),
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
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
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
     'ROUTED at b399 as `W-ORD-E0-RANK-PROPAGATION`, trigger THE AUTHOR`S WORD. ### **OPEN**'),

    # ---- WHAT THIS ACT CLOSES --------------------------------------------------------------------
    ('what the owed bridge needs instead of `(M)`, opened at b399', 'CLOSE',
     '### **CLOSED AS A QUESTION AND NOT AS A PAYMENT.** ### `b399` left the row waiting on a '
     'relation nobody had named and said naming one was not in its order. ### **b400`S ORDER WAS '
     'EXACTLY THAT, AND THE ANSWER IS THAT ON THE LAWFUL FAMILIES THERE IS NOTHING TO NAME:** ### '
     'the Sonin margin`s finite channel is identically zero there by the source`s own design, so '
     'a relation to a live finite channel would have to supply the arithmetic from outside '
     'itself. ### **WHAT REPLACES THE OPEN ITEM IS NOT A STATEMENT BUT A QUESTION AT A WIDER '
     'SUPPORT, `(Q400)`, TYPED AND PRICED AND NOT OPENED**'),
    ('the ferry`s phrase that Proposition C.1 does not apply at the window', 'CLOSE',
     '### **CLOSED BY READING THE SOURCE, AND THE ORDER IS HALF WRONG.** ### Theorem 1 carries a '
     'support hypothesis (page index `3`); ### **PROPOSITION C.1 CARRIES NONE** ### (page index '
     '`51`): its only conditions are smoothness, compact support and a finite vanishing set. ### '
     '**SO AT THE WINDOW THE BOUND IS GONE AND THE CRITERION IS STILL IN FORCE**, which is why '
     '`(Q400)` is worth typing rather than filing as unreachable'),

    # ---- WHAT THIS ACT ADDS ----------------------------------------------------------------------
    ('`(Q400)` -- the prime constituent at a support where the primes enter', 'STAND',
     '### **NEW at `b400`, AND IT IS THE ACT`S RESIDUE RATHER THAN ITS PRODUCT.** ### The one '
     'absent element is any statement evaluating or bounding `SUM_p W_p(f)` at `a^2 >= 2` against '
     'an archimedean quantity; the record holds ten cells of VALUES there and no statement. ### '
     '**PRICED AS A RESULT AND NOT AS AN INSTRUMENT RUN. ### NOT OPENED.** ### **OPEN**'),
    ('the window`s emptiness is about the TOTAL and not its constituents', 'STAND',
     '### **NEW at `b400`, AND IT IS THE DISTINCTION THAT KEEPS `b321`S FINDING FROM CLOSING '
     '`(Q400)`.** ### `b321` found the window`s balance *FORCED BY THE SHAPE OF THE COMPUTATION '
     'AND NOT EVIDENCE OF ANYTHING* -- but that was the TOTAL `SUM_v W_v`, forced by a vanishing '
     'pole term and an on-line zero library. ### **THE CONSTITUENT `SUM_p W_p` IS PRINTED IN THAT '
     'SAME ACT AS A LIVE, SIGN-CHANGING COLUMN.** ### **OPEN, AND REFUSABLE**'),
    ('`b321`s prime-power rule and its printed list are two conventions', 'STAND',
     '### **NEW at `b400`, AND IT IS A DEFECT ON A PRIOR ACT`S FACE, PRINTED AND NOT REPAIRED.** '
     '### The rule says `p^m <= a^2`; the list omits `4` at `a = 2` and `9` at `a = 3`, which is '
     'the STRICT reading. ### **IT MOVES NO VALUE** -- a self-convolution vanishes at the '
     'endpoints of its support -- and the prior face is NOT EDITED. ### **ROUTED**'),
    ('a tool whose header says READ ONLY may still write its own run record', 'STAND',
     '### **NEW at `b400` AS AN INCIDENT ON ITS OWN FACE.** ### `tools/b373_pins.py` was run at '
     'step zero while identifying the pins instrument and overwrote `b373`s banked '
     '`data/b373_pins.json` with today`s heads; it was restored BYTE-IDENTICAL to its committed '
     'blob. ### **SAME SPECIES AS `b304_hooks.py`, AT A SECOND TOOL.** ### **FILED**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES TWO ITEMS AND OPENS FOUR.**')
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
    rec('    ### ### **AND NOTHING IS PAID:** ### `0` grades conferred, `0` rows paid, and the')
    rec('    ### ### three owed pair rows still read ### **OWED** ### after the act.')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


# ==================================================================================================
def do_faces():
    """### **THE THREE OWED PAIR ROWS, APPENDED TO. ### EVERY PRIOR BYTE PRESERVED.**"""
    before = io.open(FACES, encoding='utf-8', newline='').read()
    if 'RESTATED 2026-09-10 (b400)' in before:
        # ### **AN ALREADY-FILED BRANCH THAT REPORTS `0` WOULD MAKE THE BANK PRINT A FALSE COUNT.**
        # ### It counts the rows that carry the segment and re-runs the arms on them.
        rows = [ln for ln in before.split(chr(10))
                if ln.startswith('| ') and 'RESTATED 2026-09-10 (b400)' in ln]
        rec('  ### ALREADY FILED -- the b400 segment is present in %d row(s). ### NOTHING APPENDED.'
            % len(rows))
        ok = len(rows) == 3
        for pair in PAIR_SEG:
            line = [x for x in before.split(chr(10)) if x.startswith('| %s | OWED |' % pair)]
            good = bool(line) and 'RESTATED 2026-09-10 (b400)' in line[0] and \
                'not opened' in line[0].lower()
            ok = ok and good
            rec('  ### %-8s still reads OWED and carries the b400 segment : %s' % (pair, good))
        rec('  ### ### **%s**' % ('PASS' if ok else '### FAIL ###'))
        return ok, len(rows)
    lines = before.split(chr(10))
    n_edit = 0
    for i, ln in enumerate(lines):
        for pair, seg in PAIR_SEG.items():
            if ln.startswith('| %s | OWED |' % pair):
                body = ln.rstrip()
                if not body.endswith('|'):
                    rec('  ### HARD FAILURE -- row %s does not end in a pipe.' % pair)
                    return False, n_edit
                stem = body[:-1].rstrip()
                lines[i] = stem + seg + ' |'
                n_edit += 1
                rec('  ### row %-8s line %-5d : %d -> %d bytes ; the prior cell is a true prefix '
                    ': %s' % (pair, i + 1, len(body.encode('utf-8')),
                              len(lines[i].encode('utf-8')), lines[i].startswith(stem)))
    if n_edit != 3:
        rec('  ### HARD FAILURE -- expected 3 owed pair rows, edited %d.' % n_edit)
        return False, n_edit
    after = chr(10).join(lines)
    open(FACES + '.tmp', 'wb').write(after.encode('utf-8'))
    os.replace(FACES + '.tmp', FACES)
    back = io.open(FACES, encoding='utf-8', newline='').read()
    bl, al = before.split(chr(10)), back.split(chr(10))
    same = sum(1 for a, b in zip(bl, al) if a == b)
    grew = sum(1 for a, b in zip(bl, al) if a != b and b.startswith(a.rstrip()[:-1].rstrip()))
    rec('  ### lines %d -> %d ; UNCHANGED %d ; APPENDED-TO %d ; LOST %d'
        % (len(bl), len(al), same, grew, len(bl) - len(al)))
    ok = (len(bl) == len(al) and same == len(bl) - 3 and grew == 3)
    # ### **AND THE PRESERVED BLOCK IS CHECKED BY NAME, BECAUSE THE RECORD HAS BANKED THE SPECIES.**
    pres = [i for i, ln in enumerate(al, 1) if ln.startswith('> | F2–F3 | OWED |')]
    pres_ok = all(al[i - 1] == bl[i - 1] for i in pres)
    rec('  ### preserved `>` quotation blocks naming an owed pair row : %d ; UNTOUCHED : %s'
        % (len(pres), pres_ok))
    ok = ok and pres_ok
    for pair in PAIR_SEG:
        line = [x for x in al if x.startswith('| %s | OWED |' % pair)]
        good = bool(line) and 'RESTATED 2026-09-10 (b400)' in line[0] \
            and 'not opened' in line[0].lower()
        ok = ok and good
        rec('  ### %-8s still reads OWED and carries the b400 segment : %s' % (pair, good))
    rec('  ### ### **%s**' % ('PASS' if ok else '### FAIL ###'))
    return ok, n_edit


# ==================================================================================================
def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b400 — the bridge restated: two objects on their families, one question at the '
        'window — filed 2026-09-10',
        '',
        '**b399 refuted `(M)` and refused to name a replacement, because naming one was not in its '
        'order. This act’s order was exactly that, and the answer is the fourth verdict its ferry '
        'admitted: (TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW).** The constraint '
        'set is eight constraints, each at a file and a line, **0 from the navigator**, and the '
        'record holds **2 of the 8 at DERIVES** (`C-V`, `C-VI`) — the rest at import, at content, '
        'or at measurement, and the verdict is only as strong as the softest constraint it uses.',
        '',
        '**The obstruction, derived.** On the source’s lawful class `Σ_p W_p(f) = 0` **identically** '
        '— not small, not below a bar, but **zero by the definition of the class**: eq. (149) '
        'samples `f` at `p^{±m}`, `supp(f) ⊂ (1/2, 2)` holds no prime power, and the source says so '
        'of its own design (*"so that rational primes are not involved"*, page index 2 of an '
        'artefact verified by digest this act). So the Sonin margin is a function of the '
        'archimedean place alone there. On the Li family `λ_A(n) = S_∞(n) + 1` is already owned in '
        'closed form, so the only part of `λ_n` a bridge could supply is `λ_Z(n) = −S_f(n)` — and '
        'that is **not** the zero function (the bench: negative on `n ∈ [156, 186] ∪ [247, 287]`). '
        '**A relation carrying an object whose finite channel is identically zero to one whose '
        'finite channel is not would have to supply that channel from outside itself: it is not a '
        'transport of a quantity but a new statement about the primes.** The one candidate the '
        'record held for such a statement was `(M)`, refuted at b399 by a printed value. And the '
        'two families have **no common point at which both margins are defined**.',
        '',
        '**And what this does NOT show, in the same breath, because an impossibility claimed wider '
        'than its argument is a false claim.** It does **not** show that no formula relating the '
        'two indexed families can be written: `S_f(n)` is a function of `n`, and a correspondence '
        '`a → n` fixed by hand can be made to satisfy almost any equation. **What is shown is that '
        'on the lawful families such a formula would carry nothing**, one side having no arithmetic '
        'content to carry — and that a correspondence chosen to make an identity true is '
        '**compiled, not derived**, which is exactly what the deposit’s refusal forbids. *The word '
        '“lawful” is part of the claim, not a hedge on it.*',
        '',
        '**So the pair is declared two objects, and one reason of principle is added to the ones '
        'the ledger held.** Rows L1 and L2 already say *one distribution on two families, not one '
        'functional* and *two evaluations of one distribution … separated by the pole constant*. '
        '**b400 adds that they differ in arithmetic content, and that one of them has none by '
        'design** — which is not a fact about how far the record has got, but about how the source '
        'built its class.',
        '',
        '**The bridge is restated as one question, `(Q400)`, typed and priced and NOT opened.** At '
        'a support with `a² ≥ 2`, where `Σ_p W_p(f)` is not identically zero: is there a relation '
        'between that prime constituent on the widened family and `λ_Z(n) = −S_f(n)` on the Li '
        'family? Dependencies: the places split (b232 step 4, one named assumption); `Σ_p W_p` **is** '
        'CC’s (149) factor for factor (b305/b306); `λ_Z(n) = −S_f(n)` (b327, under a sealed bar); '
        '**Proposition C.1 available at the window** and **Theorem 1 not**. **The one absent '
        'element, and it is the only one: any statement evaluating or bounding `Σ_p W_p(f)` at `a² '
        '≥ 2` against an archimedean quantity.** The record holds ten cells of values there and no '
        'statement — **priced as a RESULT, not as an instrument run**, since a further computation '
        'buys more instances and not a statement. This is `U1`’s shape at a fourth site, and this '
        'act **names the resemblance and types no bridge to the other three**.',
        '',
        '**The order’s own phrase about the window is quoted and corrected rather than quietly '
        'improved.** The ferry says the window is *"outside the source’s class and where neither '
        'Theorem 1 nor Proposition C.1 applies."* **Theorem 1 carries a support hypothesis** — '
        '*"have support in the interval [2^{−1/2}, 2^{1/2}]"*, page index 3 — **and Proposition C.1 '
        'carries none**: *"a finite set disjoint from Z and containing {0,1}, then RH ⟺ Σ_v W_v(g ⋆ '
        'ḡ♯) ≤ 0 for all g ∈ C_c^∞(R*₊) with g̃(z) = 0 for all z ∈ F"*, page index 51. **So the '
        'order is right about Theorem 1 and wrong about Proposition C.1, and the correction makes '
        'the window better rather than worse: there the bound is gone and the criterion is still in '
        'force.**',
        '',
        '**And the window’s caution is carried with the distinction that keeps it from being a '
        'closure.** b321 opened exactly this object and found its balance *FORCED BY THE SHAPE OF '
        'THE COMPUTATION AND NOT EVIDENCE OF ANYTHING*, carrying *no information the zero side did '
        'not already carry*. **What b321 found empty was the TOTAL `Σ_v W_v`. `(Q400)` asks about '
        'the constituent `Σ_p W_p`, which that same act printed as a live, sign-changing column** — '
        '`+0.000062755` at `a = 1.5`, `−0.064050234` at `a = 2.1`, `+0.190860829` at `a = 3`. **A '
        'total forced by structure does not make its constituents empty**, and the distinction is '
        'stated so a reader can refuse it.',
        '',
        '**Component 3: no banked lawful seed admits a prime power — 0 of 3 — and the census could '
        'not have come out any other way.** The least prime power is `2`; Theorem 1’s support '
        'condition is exactly `supp(f) ⊂ (1/2, 2)`; so a prime power in the support requires `a² ≥ '
        '2`, which is exactly the failure of that condition. **Lawful implies prime-free by the '
        'definition of lawful, not by the accident of which cells were run.** What a family that '
        'did admit one would cost is stated exactly: it leaves Theorem 1’s class, so the trace '
        'bound is gone; it stays inside Proposition C.1’s, so the criterion is not; and at a '
        'different object the archimedean side does not transfer either (`Γ(s)` against `Γ(s/2)`, '
        'b325). **The price is a theorem, not a run.**',
        '',
        '**Two defects are printed rather than repaired.** (i) `b321`’s Component 3 states its rule '
        'as *a prime power `p^m` enters exactly when `p^m ≤ a²`* and its printed list omits `4` at '
        '`a = 2` and `9` at `a = 3`, the strict reading — **the rule and the list are two '
        'conventions and disagree at 2 of 13 cells**; it moves no value, because a self-convolution '
        'vanishes at the endpoints of its support, and **the prior face is not edited**. (ii) At '
        'step zero this seat ran `tools/b373_pins.py` while identifying the pins instrument; **it '
        'writes when run** and overwrote b373’s banked `data/b373_pins.json`, which was restored '
        '**byte-identical to its committed blob**. Same species as `b304_hooks.py`, at a second '
        'tool.',
        '',
        '**The claim the ferry forbids unless the record makes it is not made.** *No claim that the '
        'bridge and the clause are one question unless the record’s own words say it.* The search '
        'ran over the three ledgers, returned **5 hits, all hand-read**, and **none is about the '
        'bridge and the clause**. The claim is not made, in either direction.',
        '',
        '**The trails’ triggers, restated with the one that fired.** `W-ORD-LI-WEIL-BRIDGE` — '
        '**THE AUTHOR’S WORD**, and it **fired again** with the b400 ferry; answered **TWO OBJECTS '
        'ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW**, and the row stays open on `(Q400)`. '
        '`W-ORD-DISCRIMINATING-FAMILY` and `W-ORD-LI-FAMILY-CONTROL` — unchanged, and neither can '
        'fire while the instrument lane is PARKED under (R4); **a block on the work is not an '
        'absence of a trigger.** `W-ORD-E0-RANK-PROPAGATION` — unchanged, trigger **THE AUTHOR’S '
        'WORD**; this act moves no grade.',
        '',
        '**The four lists stay OPEN by name**, each with its trigger: LIST 1 (rows citing at a ref '
        'nobody can name) — when a row of it is cited; LIST 2 (rows grading a declaration the '
        'record has classified absent) — when a grade must be defended; LIST 3 (the undated '
        'figures) — when a figure is quoted forward; LIST 4 (the bibliography entries nothing '
        'cites) — at the next bibliography pass. **This act closes none of them.**',
        '',
        '*The clause has not moved. No coordinate is closed. No grade moved or was conferred. No '
        'equivalence is compiled. Nothing deposits and the platform was not called at all. h2 '
        'stands exactly where the deposit left it and this act makes no claim about it in either '
        'direction.*',
        '',
    ]


SCOPE = (
    "**SCOPE: THE BRIDGE RESTATED, AND THE PAIR DECLARED TWO OBJECTS.** b399 refuted (M) and "
    "refused to name a replacement; this act's order was exactly that, and the verdict is the "
    "ferry's fourth: **(TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW).** THE "
    "CONSTRAINT SET IS 8 CONSTRAINTS, EACH AT A FILE AND A LINE, 0 FROM THE NAVIGATOR, and the "
    "record holds 2 of the 8 at DERIVES. **THE OBSTRUCTION, DERIVED:** on the source's lawful "
    "class SUM_p W_p(f) = 0 IDENTICALLY -- zero by the definition of the class, since (149) samples "
    "f at p^{+-m} and supp(f) is inside (1/2, 2), which the source chose so that rational primes "
    "are not involved (its own sentence, page index 2 of an artefact verified by digest this act) "
    "-- so the Sonin margin is a function of the archimedean place alone there; on the Li family "
    "lambda_A(n) = S_inf(n) + 1 is already owned in closed form, so the only part a bridge could "
    "supply is lambda_Z(n) = -S_f(n), which is NOT the zero function (negative on n in [156,186] "
    "and [247,287]). **A RELATION CARRYING AN OBJECT WHOSE FINITE CHANNEL IS IDENTICALLY ZERO TO "
    "ONE WHOSE FINITE CHANNEL IS NOT WOULD HAVE TO SUPPLY THAT CHANNEL FROM OUTSIDE ITSELF: IT IS "
    "NOT A TRANSPORT OF A QUANTITY BUT A NEW STATEMENT ABOUT THE PRIMES**, and the one candidate "
    "the record held for one was (M), refuted at b399. **AND WHAT THIS DOES NOT SHOW IS STATED IN "
    "THE SAME BREATH:** it does NOT show that no formula relating the two indexed families can be "
    "written -- only that on the lawful families such a formula would carry nothing, and that a "
    "correspondence chosen to make an identity come out is COMPILED, NOT DERIVED, which the "
    "deposit's refusal forbids. **SO THE PAIR IS DECLARED TWO OBJECTS**, as rows L1 and L2 define "
    "them, with one reason of principle added: they differ in ARITHMETIC CONTENT and one of them "
    "has none by design. **AND THE BRIDGE IS RESTATED AS ONE QUESTION AT THE WINDOW, (Q400), TYPED "
    "AND PRICED AND NOT OPENED:** at a support with a^2 >= 2, is there a relation between SUM_p "
    "W_p(f) and lambda_Z(n)? The one absent element, and the only one, is any statement evaluating "
    "or bounding SUM_p W_p(f) at a^2 >= 2 against an archimedean quantity; the record holds ten "
    "cells of VALUES there and no statement, so it is priced as a RESULT and not as an instrument "
    "run. **THE ORDER'S OWN PHRASE IS QUOTED AND CORRECTED RATHER THAN IMPROVED:** Theorem 1 "
    "carries a support hypothesis (page index 3) and PROPOSITION C.1 CARRIES NONE (page index 51), "
    "so at the window the bound is gone and THE CRITERION IS STILL IN FORCE. **AND THE WINDOW'S "
    "CAUTION IS CARRIED WITH THE DISTINCTION THAT KEEPS IT FROM BEING A CLOSURE:** what b321 found "
    "FORCED BY THE SHAPE OF THE COMPUTATION was the TOTAL SUM_v W_v; (Q400) asks about the "
    "CONSTITUENT SUM_p W_p, which that same act printed as a live sign-changing column. "
    "**COMPONENT 3: 0 OF 3 LAWFUL SEEDS ADMIT A PRIME POWER, AND THE CENSUS COULD NOT HAVE COME "
    "OUT ANY OTHER WAY** -- the least prime power is 2 and the support condition is exactly "
    "supp(f) inside (1/2, 2), so a prime power requires a^2 >= 2, which is that condition's "
    "failure. **TWO DEFECTS ARE PRINTED RATHER THAN REPAIRED:** b321's prime-power rule and its "
    "printed list are two conventions disagreeing at 2 of 13 cells (it moves no value; the prior "
    "face is not edited), and this seat ran b373_pins.py at step zero and overwrote b373's banked "
    "run record, restored BYTE-IDENTICAL to its committed blob. **THE CLAIM THE FERRY FORBIDS IS "
    "NOT MADE:** 5 needle hits across the three ledgers, all hand-read, none about the bridge and "
    "the clause. NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR "
    "AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, "
    "NEITHER MAP TOUCHED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO PRIOR ACT'S FACE BANK OR "
    "INSTRUMENT EDITED, NO EQUIVALENCE COMPILED. NOTHING DEPOSITS; **THE PLATFORM WAS NOT CALLED "
    "AT ALL**; 0 BRANCHES TOUCHED, 0 CLONES, 0 BUILDS, 0 INSTRUMENT RUNS, NO .lean FILE TOUCHED, "
    "NO .git/hooks/pre-push DELETED. THE INSTRUMENT LANE AND THE INSTRUMENT-AUDIT LANE STAY "
    "PARKED. THE WAVE STAYS PARKED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. THE FOUR "
    "OPEN LISTS ARE RESTATED OPEN BY NAME WITH THEIR TRIGGERS. The seam's debt item 1 restated, "
    "still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's "
    "record. **THE CLAUSE HAS NOT MOVED AND NO COORDINATE IS CLOSED.** h2 stands exactly where the "
    "deposit left it and this act makes no claim about it in either direction.")


def corr_rows(Q):
    m = ("**THE BRIDGE IS RESTATED AND THE PAIR DECLARED TWO OBJECTS: ON THE LAWFUL FAMILIES THE "
         "RELATION THE WORK ORDER ASKS FOR CAN CARRY NOTHING, AND WHAT SURVIVES IS ONE QUESTION AT "
         "THE WINDOW** (b400, the bridge restated)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b400, %d gates read and %d checked "
            "by digest. THE CONSTRAINT SET IS %d CONSTRAINTS, EACH AT A FILE AND A LINE, 0 FROM "
            "THE NAVIGATOR, %d OF THEM HELD AT DERIVES. %d reads, %d ANCHORED; %d source "
            "fragments, %d located in artefacts VERIFIED against the corpus's banked digests "
            "BEFORE a word was read. **THE OBSTRUCTION:** on the lawful class SUM_p W_p(f) = 0 "
            "IDENTICALLY, so the Sonin margin is archimedean alone there; lambda_A(n) = S_inf(n) + "
            "1 is already owned, so the only part a bridge could supply is the live finite channel "
            "lambda_Z(n) = -S_f(n) -- **A NEW STATEMENT ABOUT THE PRIMES AND NOT A TRANSPORT OF A "
            "QUANTITY** -- and the one candidate, (M), is refuted. **AND THE LIMIT IS STATED WITH "
            "IT:** it does NOT show no formula can be written, only that on these families one "
            "would carry nothing and a chosen correspondence is COMPILED NOT DERIVED. **(Q400) IS "
            "TYPED, PRICED AS A RESULT AND NOT OPENED**, its one absent element named. THE ORDER'S "
            "OWN PHRASE IS CORRECTED AT SOURCE: Theorem 1 carries a support hypothesis and "
            "PROPOSITION C.1 CARRIES NONE, so at the window the bound is gone and the criterion is "
            "in force. COMPONENT 3: %d OF %d LAWFUL SEEDS ADMIT A PRIME POWER, and the census "
            "could not have come out otherwise. TWO DEFECTS PRINTED NOT REPAIRED: b321's rule "
            "against its own list, and this seat's own step-zero overwrite of b373's banked record, "
            "restored byte-identical. %d GRADES MOVED, %d ROWS PAID, %d EQUIVALENCES COMPILED, %d "
            "CONTENT LOST"
            % (LG['gates_read'], LG['face_subject_gates'], CF['constraints'],
               CF['constraints_at_derives'], READS, ANCH, SRCN, SRCOK,
               CF['lawful_with_prime'], CF['lawful'], 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN, AND NONE IS OPENED. ### NO "
            "INSTRUMENT WAS RUN, NO KERNEL BUILT, NO OBJECT RECOMPUTED, NO BRANCH TOUCHED AND NO "
            ".lean FILE TOUCHED. ### THE ONLY ARITHMETIC IS PRIME POWERS IN AN INTERVAL, ON THE "
            "RECORD'S OWN GRID, PRINTED AGAINST THE BANKED LIST CELL BY CELL. ### DECLARING TWO "
            "OBJECTS IS NOT BRIDGING THEM, AND TYPING A QUESTION IS NOT ANSWERING IT")
    prof = ("### NO AXIOM PROFILE IS ASSERTED OR RECOMPUTED. ### NO GRADE MOVED OR CONFERRED, NO "
            "FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS "
            "RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST "
            "CLOSED, NO FACE ROW OF THE LEDGER EDITED, NO EQUIVALENCE COMPILED. ### THE CORPUS "
            "WRITES ARE THREE OWED PAIR ROWS APPENDED TO AND ONE APPEND-ONLY TRAIL BLOCK, 0 "
            "CONTENT LOST. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### THE VERDICT IS DERIVED FROM A CONSTRAINT SET WHOSE EVERY MEMBER CARRIES A FILE, A "
             "LINE AND A GRADE, AND THE ACT NAMES WHICH FOUR IT USES. ### THE IMPOSSIBILITY IS "
             "STATED AT THE SCOPE IT IS DERIVED AT, WITH THE SENTENCE NAMING WHAT IT DOES NOT SHOW "
             "IN THE SAME COMPONENT. ### THE ORDER'S OWN PHRASE WAS TESTED AGAINST A VERIFIED "
             "SOURCE AND CORRECTED IN PRINT RATHER THAN IMPROVED IN SILENCE. ### THE CLAIM THE "
             "FERRY PERMITS ONLY ON THE RECORD'S WORD WAS SEARCHED FOR, THE FIVE HITS HAND-READ, "
             "AND THE CLAIM NOT MADE. ### THE PRIME CENSUS IS SET AGAINST THE BANKED LIST CELL BY "
             "CELL RATHER THAN BY A COUNT OF MATCHES, AND THE ONE DISAGREEMENT IS NAMED AS A "
             "CONVENTION AND ROUTED. ### AND THE ACT'S OWN STEP-ZERO INCIDENT IS ON ITS LOCKED "
             "FACE, DECLARED BEFORE THE COMPONENTS RAN")
    status = ("data/b400_the_bridge_restated.txt; data/b400_components_run.txt; "
              "data/b400_extract_notes3.txt; data/b400_registration_2026-09-10.txt (LOCKED before "
              "any write at sha256 %s, chained on tools/b378_lockgate.py run as b400); "
              "tools/b400_extract.py; tools/b400_regspec.py; tools/b400_reg_gate.py; "
              "tools/b400_components.py; tools/b400_desk_bank.py; tools/b400_checks.py; "
              "PLACE-papers FACES_LEDGER.md (three OWED pair rows, appended to) and "
              "OPEN_TRAILS.md (one append-only block); CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what replaces the refuted bridge identity',
           'why can the sonin margin not reach the li margin',
           'is the sonin margin prime free',
           'does proposition c1 apply at the widened window',
           'where would a bridge have to live',
           'are the two margins one object or two')
MUST_NOT_HIT = ('the bridge was paid', 'a grade was moved', 'the window was opened',
                'the platform was called', 'an equivalence was compiled')

KEY = 'the-bridge-restated'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b400 RESTATED THE OWED BRIDGE AND REACHED THE FOURTH VERDICT ITS ORDER ADMITTED: **TWO "
        "OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW**. THE CONSTRAINT SET IS 8 "
        "CONSTRAINTS, EACH AT A FILE AND A LINE, 0 FROM THE NAVIGATOR, 2 HELD AT DERIVES. **THE "
        "OBSTRUCTION, DERIVED:** on the source's lawful class SUM_p W_p(f) = 0 IDENTICALLY -- zero "
        "by the definition of the class, because (149) samples f at p^{+-m} and supp(f) is inside "
        "(1/2, 2), the source having chosen its window *so that rational primes are not involved* "
        "-- so the Sonin margin is a function of the archimedean place ALONE there. On the Li "
        "family lambda_A(n) = S_inf(n) + 1 is already owned in closed form, so the only part of "
        "lambda_n a bridge could supply is lambda_Z(n) = -S_f(n), which is NOT the zero function. "
        "**A RELATION CARRYING AN OBJECT WHOSE FINITE CHANNEL IS IDENTICALLY ZERO TO ONE WHOSE "
        "FINITE CHANNEL IS NOT WOULD HAVE TO SUPPLY THAT CHANNEL FROM OUTSIDE ITSELF: IT IS NOT A "
        "TRANSPORT OF A QUANTITY BUT A NEW STATEMENT ABOUT THE PRIMES.** The one candidate the "
        "record held was (M), refuted at b399. **AND WHAT THIS DOES NOT SHOW IS STATED IN THE SAME "
        "BREATH: IT DOES NOT SHOW THAT NO FORMULA CAN BE WRITTEN**, only that on the lawful "
        "families one would carry nothing, and that a correspondence chosen to make an identity "
        "come out is COMPILED, NOT DERIVED. **THE BRIDGE IS RESTATED AS (Q400), TYPED AND PRICED "
        "AND NOT OPENED:** at a support with a^2 >= 2, where SUM_p W_p(f) is not identically zero, "
        "is there a relation between that prime constituent and lambda_Z(n)? THE ONE ABSENT "
        "ELEMENT, AND THE ONLY ONE, IS ANY STATEMENT EVALUATING OR BOUNDING SUM_p W_p(f) AT a^2 >= "
        "2 AGAINST AN ARCHIMEDEAN QUANTITY. **THE ORDER'S OWN PHRASE WAS CORRECTED AT SOURCE: "
        "THEOREM 1 CARRIES A SUPPORT HYPOTHESIS AND PROPOSITION C.1 CARRIES NONE**, so at the "
        "window the bound is gone and the criterion is still in force. **AND THE WINDOW'S CAUTION "
        "IS CARRIED WITH THE DISTINCTION THAT KEEPS IT FROM BEING A CLOSURE:** what b321 found "
        "forced by the shape of the computation was the TOTAL SUM_v W_v, not the CONSTITUENT SUM_p "
        "W_p, which that act printed as a live sign-changing column. **COMPONENT 3: 0 OF 3 LAWFUL "
        "SEEDS ADMIT A PRIME POWER, AND THE CENSUS COULD NOT HAVE COME OUT ANY OTHER WAY** -- the "
        "least prime power is 2 and the support condition is exactly supp(f) inside (1/2, 2). NO "
        "ROW IS PAID, NO GRADE MOVED, NO EQUIVALENCE COMPILED.")
    grade = (
        "### NO INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED -- the only arithmetic "
        "is prime powers in an interval on the record's own grid, printed against the banked list "
        "cell by cell. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE "
        "STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS "
        "NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO EQUIVALENCE COMPILED. ### THE CORPUS "
        "WRITES ARE THREE OWED PAIR ROWS APPENDED TO AND ONE APPEND-ONLY TRAIL BLOCK -- ALL "
        "ADDITIVE, 0 CONTENT LOST. ### THE IMPOSSIBILITY IS STATED AT ITS DERIVED SCOPE WITH THE "
        "SENTENCE NAMING WHAT IT DOES NOT SHOW BESIDE IT. ### TWO DEFECTS ARE PRINTED RATHER THAN "
        "REPAIRED: b321's prime-power rule against its own printed list, and this seat's own "
        "step-zero overwrite of b373's banked run record, restored byte-identical to its committed "
        "blob. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT "
        "MOVED AND NO COORDINATE IS CLOSED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### "
        "M-2 UNCHANGED")
    where = (
        "data/b400_the_bridge_restated.txt; data/b400_components_run.txt; "
        "data/b400_extract_notes3.txt; data/b400_registration_2026-09-10.txt (LOCKED before any "
        "write, chained on tools/b378_lockgate.py run as b400 -- %d gates read, %d checked by "
        "digest); tools/b400_extract.py; tools/b400_regspec.py; tools/b400_reg_gate.py; "
        "tools/b400_components.py; tools/b400_desk_bank.py; tools/b400_checks.py; PLACE-papers "
        "FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b400 (the bridge restated: on the lawful families the relation can carry nothing, and '
           'what survives is one question at the window)')
    row_new = ('    # ### THE BRIDGE RESTATED (b400).%s'
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
        rec('    %-52s reaches the b400 key : %s' % (qq, g2))
    for lbl, cond in (
            ('the verdict is the fourth one', 'TWO OBJECTS ON THEIR FAMILIES' in out),
            ('the prime-free constraint is stated as identical zero',
             'SUM_p W_p(f) = 0 IDENTICALLY' in out),
            ('the live channel is named', 'lambda_Z(n) = -S_f(n)' in out),
            ('the obstruction is stated as a new statement about the primes',
             'NEW STATEMENT ABOUT THE PRIMES' in out),
            ('the limit of the obstruction is stated',
             'IT DOES NOT SHOW THAT NO FORMULA CAN BE WRITTEN' in out),
            ('a chosen correspondence is compiled not derived', 'COMPILED, NOT DERIVED' in out),
            ('the question is typed and not opened', 'NOT OPENED' in out),
            ('the one absent element is named', 'THE ONLY ONE, IS ANY STATEMENT' in out),
            ('the order`s phrase is corrected at source',
             'PROPOSITION C.1 CARRIES NONE' in out),
            ('the window caution keeps its distinction', 'not the CONSTITUENT' in out
             or 'CONSTITUENT SUM_p' in out),
            ('the lawful seeds carry no prime power',
             '0 OF 3 LAWFUL SEEDS ADMIT A PRIME POWER' in out),
            ('no equivalence is compiled', 'NO EQUIVALENCE COMPILED' in out),
            ('the prior face defect is printed not repaired',
             "b321's prime-power rule against its own printed list" in out),
            ('the act`s own step-zero incident is on the record',
             'restored byte-identical to its committed blob' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


# ==================================================================================================
def bank(Q, rownum, kok, faces_edited):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A('b400 -- THE BRIDGE RESTATED, OR THE PAIR DECLARED TWO OBJECTS. ### THE BANK.')
    A('### Ferry part 1 of 1, receipt confirmed IN FULL (Rule 1). ### 2026-09-10.')
    A('### CONCURRENCY: SOLO (research seat).')
    A('### The face was LOCKED before any write at sha256 `%s`.' % SEALHASH)
    A(BAR)
    A('')
    A(SUB)
    A('### THE VERDICT.')
    A(SUB)
    A('### ### ### **(TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW.)**')
    A('')
    A(SCOPE)
    A('')
    A(SUB)
    A('### THE CONSTRAINT SET, AS COMPONENT 1 PRINTED IT.')
    A(SUB)
    for ln in io.open(os.path.join(D, 'b400_components_run2.txt'),
                      encoding='utf-8').read().split(chr(10)):
        if ln.startswith('  ### ### **C-') or ln.startswith('      ### GRADE') \
                or ln.startswith('      ### AT '):
            A(ln)
    A('')
    A('### ### **CONSTRAINTS : `%d`. ### AT A FILE AND A LINE : `%d`. ### FROM THE NAVIGATOR : `0`.'
      % (CF['constraints'], CF['constraints']))
    A('### ### HELD AT `DERIVES` : `%d`.**' % CF['constraints_at_derives'])
    A('')
    A(SUB)
    A('### WHAT THE ACT WROTE, AND WHAT IT DID NOT.')
    A(SUB)
    A('### **THE LEDGER WRITES** ### -- `%d` OWED pair rows of `FACES_LEDGER.md`, APPENDED TO and'
      % faces_edited)
    A('### not rewritten, with the deposit`s refusal quoted beside them; one append-only block in')
    A('### `OPEN_TRAILS.md`. ### **`0` CONTENT LOST. ### `0` GRADES MOVED. ### `0` ROWS PAID. ###')
    A('### ### `0` EQUIVALENCES COMPILED.**')
    A('### **THE DESK** ### -- `%d` items swept, `%d` closed, `%d` standing, `%d` lists closed.'
      % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    A('### **THE SURVEY** ### -- `%d` reads, `%d` ANCHORED; `%d` source fragments, `%d` located in'
      % (READS, ANCH, SRCN, SRCOK))
    A('### artefacts VERIFIED against the corpus`s banked digests BEFORE a word was read.')
    A('### **THE GATE CHAIN** ### -- `%d` gates read, `%d` passing, `%d` checked by digest.'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A('### **THE ROW AND THE KEY** ### -- correspondence row `%d`; index key `%s` : %s.'
      % (rownum, KEY, 'PASS' if kok else 'FAIL'))
    A('')
    A(SUB)
    A('### THE TWO DEFECTS, PRINTED RATHER THAN REPAIRED.')
    A(SUB)
    A('### ### **(1) A PRIOR ACT`S FACE CARRIES TWO CONVENTIONS.** ### `b321`s Component 3 states')
    A('### its rule as *a prime power `p^m` enters exactly when `p^m <= a^2`* and its printed list')
    A('### omits `4` at `a = 2` and `9` at `a = 3`, which is the STRICT reading -- ### **THEY')
    A('### ### DISAGREE AT `2` OF `13` CELLS.** ### It moves no value: a self-convolution vanishes')
    A('### at the endpoints of its support. ### **THE PRIOR FACE IS NOT EDITED AND BOTH')
    A('### ### CONVENTIONS ARE PRINTED.**')
    A('### ### **(2) THIS SEAT OVERWROTE A PRIOR ACT`S BANKED RECORD AT STEP ZERO.**')
    A('### `tools/b373_pins.py` is the `(R9)` pins AUDIT, not the `ls-remote` pins, and ### **IT')
    A('### ### WRITES WHEN RUN.** ### Run while identifying the right instrument, it overwrote')
    A('### `data/b373_pins.json` with today`s heads. ### Restored from its committed blob and')
    A('### re-hashed ### **BYTE-IDENTICAL**, and the incident was declared on the face BEFORE the')
    A('### components ran. ### **SAME SPECIES AS `b304_hooks.py`, AT A SECOND TOOL:** ### a tool')
    A('### whose header says READ ONLY may still write its own run record.')
    A('')
    A(SUB)
    A('### WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It does not say that no formula relating the two indexed families can be written.')
    A('### It does not name a replacement for `(M)`; ### **IT NAMES A QUESTION AND DOES NOT OPEN')
    A('### ### IT.**')
    A('### It does not say that the bridge and the clause are one question -- ### **THE RECORD`S')
    A('### ### OWN WORDS DO NOT SAY IT, AND `5` HITS WERE HAND-READ TO CHECK.**')
    A('### It does not lift the family obstruction, move a grade, close a coordinate, close a list')
    A('### or move the clause. ### It compiles no equivalence.')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### h2 STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    rec('  ### bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))


# ==================================================================================================
def main():
    bar('=')
    rec('b400 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
    bar('=')
    bar()
    rec('  ### THE DESK UNDER (R7).')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### THE THREE OWED PAIR ROWS OF THE FACES LEDGER, APPENDED TO.')
    bar()
    fok, fn = do_faces()
    if not fok:
        run_clock.write(D, 'b400_desk_notes', LINES)
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
        rec('  ### the b399 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            run_clock.write(D, 'b400_desk_notes', LINES)
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_verdict': 'two objects on their families, one question at the window' in low,
        'says_identically_zero': 'identically' in low and 'zero by the definition of the class'
                                 in low,
        'says_live_channel': '−s_f(n)' in low or '-s_f(n)' in low,
        'says_new_statement': 'new statement about the primes' in low,
        'says_limit': 'does **not** show that no formula relating' in low,
        'says_compiled': 'compiled, not derived' in low,
        'says_question_typed': '(q400)' in low,
        'says_not_opened': 'not opened' in low,
        'says_absent_element': 'the only one' in low,
        'says_order_corrected': 'proposition c.1 carries none' in low,
        'says_window_caution': 'what b321 found empty was the total' in low,
        'says_component3': '0 of 3' in low,
        'says_defects': 'two conventions' in low and 'byte-identical' in low,
        'says_one_question_refused': 'none is about the bridge and the clause' in low,
        'says_lists_open': 'the four lists stay open by name' in low,
        'says_block_not_absence': 'a block on the work is not an absence of a trigger' in low,
        'says_nothing_paid': 'no grade moved or was conferred' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-32s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b400_desk_notes', LINES)
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
        run_clock.write(D, 'b400_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b400_desk_notes', LINES)
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
            run_clock.write(D, 'b400_desk_notes', LINES)
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
    bank(Q, rownum, kok, fn)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### PAIR ROWS %d. ### ROW %d. ### KEY %s. ###'
        % (Q['items'], Q['closed'], fn, rownum, 'PASS' if kok else 'FAIL'))
    rec('  ### ### BANK WRITTEN.**')
    bar('=')
    run_clock.write(D, 'b400_desk_notes', LINES)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
