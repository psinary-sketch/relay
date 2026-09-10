# -*- coding: utf-8 -*-
"""b404_desk_bank.py -- THE DESK, ROW `U1`, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.

### ### **TWO CELLS OF ONE ROW ARE APPENDED TO AND THE OTHER FIVE MUST COME BACK BYTE-IDENTICAL**,
### checked cell by cell against the PRE-ACT blob -- `HEAD` before the push and `HEAD~1` after it,
### ### **THE REFERENCE NAMED AND NOT ONLY THE SIDE** (`b401`'s species, sharpened at `b403`).
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
MARK = '<!-- b404 the fifth site, the sixth candidate, and the row law strained -->'
PRIOR = '<!-- b403 the three routed items: one repaired, one applied, one ruled and routed -->'
BANKOUT = os.path.join(D, 'b404_the_fifth_and_sixth_sites.txt')

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


SEALTXT = io.open(os.path.join(D, 'b404_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = J('b404_lockgate')
X = J('b404_extract')
CF = J('b404_components')
F = X['fig']
READS = len(X['reads'])
ANCH = sum(1 for r in X['reads'] if r['verdict'] == 'ANCHORED')

DEPOSIT_REFUSAL = (
    'the deposit, section 27.3: *"compiling the *structure* of the one-premise-in-five-registers '
    'claim while deliberately **not** compiling the cross-register equivalences, since to compile '
    '\'discharge one and you discharge all five\' would be to compile RH-equivalence itself."*')

CELL4_ADD = (
    ' ### **(v) THE REPRESENTATION-DEPENDENT CONSTANT**, added 2026-09-10 (b404): Lagarias '
    'Theorem 6.1’s finite-place bound `S_f(n,π) = λ_n(n,π) + O(n log n)` holds *"in which the '
    'implied constant in the O-notation **depends on π**"*, while Theorem 5.1’s archimedean bound '
    'carries an **ABSOLUTE** constant — so the record holds an error term indexed by the '
    'representation and needs one that is not. **AND IT IS EMPTY AS AN OBSTRUCTION IN A WAY THE '
    'ROW HAS NOT HAD TO NAME BEFORE, SO b404 NAMES TWO KINDS: (a) empty because there is nothing '
    'to range over — vacuous forever; (b) empty because the available uniformity ranges over a '
    'class that does not contain the corpus’s other object — the obstruction real, the instrument '
    'aimed elsewhere. (v) IS KIND (b).** The corpus is **not** a one-L-function corpus: row F7 is '
    'a second object already aimed at, and b325 measured the transfer failure across the two '
    '(*THE ARCHIMEDEAN DISTRIBUTION DOES NOT TRANSFER*, `Γ(s)` against `Γ(s/2)`). But Theorem 6.1 '
    'quantifies over *irreducible cuspidal unitary automorphic representations on GL(N)*, and the '
    'corpus’s second object is **not established to be one** — the record’s own `H-CUSP` grade '
    'shows even ζ sits there only under the source’s stated convention (b358, inherited b361). '
    '**A uniformity over a class that does not contain your other object is not a uniformity you '
    'can spend.** *A correction the navigator recorded and this entry carries: the b403 ferry '
    'called the window a fifth site; the window is the row’s **fourth**, entered by b401, and '
    'b403 entered nothing. This is the distinct fifth.*'
    ' ### **(vi) THE TYPE-D RESIDUE AT EVERY FINITE MODULUS**, added 2026-09-10 (b404): the '
    'additive–multiplicative conspiracy keystone states its own boundary as a quantifier '
    'interchange — *"The step from ‘consistent at every finite modulus’ to ‘holds globally’ '
    '(positive global density) interchanges a per-modulus quantifier with a global one — a '
    'local-to-global passage, not a mechanical corollary."* The compiled half closes at **every** '
    'finite modulus; what is missing is the statement **across** them, and the paper files the '
    'residue in the same words at all three problems: *the density / representation / sieve '
    'density lower bound is **the whole of the remaining weight***. **The shape fits, and more '
    'sharply than the entries above it, because the keystone names the interchange rather than '
    'leaving it to be inferred from a measurement.** **AND THE SAME PARAGRAPH CARRIES SOMETHING '
    'THIS ROW HAS NEVER CITED:** the programme has this shape **compiled** in the RH setting — '
    'the unrestricted commutation of the two quantifiers is **FALSE AS A THEOREM** with an '
    'explicit countermodel, and it **closes only under a shared witness**. **THAT IS REPORTED, NOT '
    'TYPED AS A BRIDGE: a theorem about a SHAPE is not a theorem about any instance of it, and '
    'this row’s law forbids the crossing.**')

CELL6_ADD = (
    ' ### **EXTENDED 2026-09-10 (b404) TO SIX, AND THE ROW’S LAW IS `STRAINED` — WHICH IS SAID '
    'HERE RATHER THAN LEFT TO A READER.** The refusal is restated and now governs six: *NOTHING IS '
    'CLAIMED ABOUT THE EQUIVALENCE* of them; *a row naming things that look alike is exactly where '
    'an equivalence gets compiled by accident*; this row *names a resemblance of SHAPE and types '
    'no bridge between* them, *in either direction*. **b404 types no bridge between any two of the '
    'six.** **AND THREE STRAINS ARE NAMED RATHER THAN SUMMED:** (1) **(iii) and (iv) share an '
    'index** — the support width — so they are not two independent witnesses, which b401 put on '
    'the face of its own entry; (2) **(v) is empty in kind (b)**, so a reader counting the row’s '
    'instances as live obstructions would over-count by one; (3) **(vi) is from a different '
    'discipline** — additive number theory with a compiled local half, against five analytic '
    'sites — and *a row that spans two disciplines is either a deep observation or a loose one, '
    'and nothing in the row decides which*. **It is still naming a resemblance, and only because '
    'its refusal is restated at every entry; but the margin is thinner at six than it was at '
    'three.** **WHAT WOULD RELIEVE IT IS ROUTED AND NOT APPLIED:** every entry naming its missing '
    'statement exactly and filing its residue as the whole of the remaining weight — the form the '
    'conspiracy keystone uses and which **one of the six already has**. THE DEPOSIT’S REFUSAL '
    'GOVERNS THIS ENTRY AS IT GOVERNS THE LEDGER: ' + DEPOSIT_REFUSAL + ' NOTHING IS PAID HERE, NO '
    'GRADE IS CONFERRED, AND NO EQUIVALENCE IS COMPILED.')

DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', 'PARKED'),
    ('the instrument-audit lane, PARKED under ruling R22', 'STAND',
     'PARKED, and it is why no kernel was built to read the one profile that is unreadable'),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     'OPEN. ### **TRIGGER: when a row of it is cited by an act.**'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade. ### **TRIGGER: when a grade must be defended.**'),
    ('LIST 3 -- the undated figures across the roster', 'STAND',
     'OPEN. ### **TRIGGER: when a figure is quoted forward.**'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     'OPEN. ### **TRIGGER: at the next bibliography pass.**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', 'OPEN AND THE AUTHOR`S'),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the deposited layer, unread since b389', 'STAND', 'STILL BLOCKED'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('the keystones` stale `HELD` prose', 'STAND', 'ROUTED at b397, OPEN'),
    ('the `82` at-risk figures', 'STAND', 'TRIGGERED at b397, and PARKED by `(R22)`'),
    ('`(N)`, the smallest next statement toward the clause', 'STAND', 'NAMED at b398. ### **OPEN**'),
    ('the grade move inside b332`s E0 ranking table', 'STAND', 'ROUTED at b399. ### **OPEN**'),
    ('`(Q400)`, the prime constituent at a support where the primes enter', 'STAND',
     '### **OPEN**, and now also the row`s instance `(iv)`. ### **NOT OPENED**'),
    ('`b321`s prime-power rule against its own printed list', 'STAND',
     'ROUTED at b400, restated b401, RULED and still ROUTED at b403. ### **OPEN**'),
    ('`SIDE-window` has no pre-push guard', 'STAND', 'NAMED at b403, ROUTED. ### **OPEN**'),
    ('the KINDS write list, short by one at b403', 'STAND',
     'FILED at b403; `0` species minted; the order forbids minting until a fourth act shows the '
     'same shortfall twice. ### **OPEN**'),

    # ---- WHAT THIS ACT CLOSES --------------------------------------------------------------------
    ('the fifth site, restated as awaiting entry at b403', 'CLOSE',
     '### **CLOSED BY ENTRY.** ### Row `U1` now carries `(v)`, the representation-dependent '
     'constant, ### **WITH ITS EMPTINESS NAMED BY KIND** ### -- and the two kinds are minted here '
     'because the row had no way to say which sort of empty a site was. ### **(a) NOTHING TO '
     'RANGE OVER, VACUOUS FOREVER; (b) THE AVAILABLE UNIFORMITY AIMED AT A CLASS THAT DOES NOT '
     'CONTAIN YOUR OTHER OBJECT.** ### `(v)` is `(b)`'),
    ('whether the Type-D residue belongs in the uniformity row', 'CLOSE',
     '### **CLOSED BY THE KEYSTONE`S OWN BOUNDARY PARAGRAPH: ### ENTERED AS `(vi)`.** ### The '
     'paper names the interchange itself -- *a per-modulus quantifier with a global one* -- and '
     'files the residue as ### **THE WHOLE OF THE REMAINING WEIGHT** ### at all three problems. '
     '### **AND IT FITS MORE SHARPLY THAN THE ENTRIES ABOVE IT**, because it names its own '
     'missing statement rather than leaving it to be inferred'),

    # ---- WHAT THIS ACT ADDS ----------------------------------------------------------------------
    ('the compiled countermodel the row has never cited', 'STAND',
     '### **NEW at `b404`, AND IT IS THE ACT`S SHARPEST FIND.** ### The conspiracy keystone`s '
     'boundary paragraph reports that the programme has the row`s own shape ### **COMPILED IN THE '
     'RH SETTING**: ### the unrestricted commutation of the two quantifiers is ### **FALSE AS A '
     'THEOREM** ### with an explicit countermodel, closing ### **ONLY UNDER A SHARED WITNESS.** '
     '### **A COMPILED NEGATIVE RESULT ABOUT THE SHAPE `U1` NAMES, SITTING IN THE RECORD, UNCITED '
     'BY `U1`.** ### **REPORTED, NOT TYPED AS A BRIDGE.** ### **OPEN**'),
    ('the row could be restated so every entry files its own residue', 'STAND',
     '### **NEW at `b404` AS A FILING ONLY.** ### The keystone names its missing statement '
     'exactly and files the residue as the whole remaining weight; of the row`s six entries ### '
     '**ONE ALREADY DOES BOTH** ### and the rest name the missing thing without filing a residue. '
     '### **AN ENTRY IN THAT FORM CANNOT BE READ AS A WITNESS FOR ANOTHER**, which is what would '
     'relieve the strain. ### **ROUTED TO THE AUTHOR. ### THIS ACT RESTATES NOTHING.** ### '
     '**OPEN**'),
    ('the conspiracy keystone widens a claim the repository scopes narrowly', 'STAND',
     '### **NEW at `b404`, AND IT IS AT THE REF THE KEYSTONE ITSELF CITES.** ### The paper writes '
     'of `SIDE-effects` at `c66f3c5` ### *vanilla Lean 4, no Mathlib* ### and that the ### *`0 '
     'sorry, 0 axioms` claim holds of the structural theorems*, naming `Module1`s. ### **AT THAT '
     'REF `Module1.lean` IMPORTS MATHLIB**, and the repository`s own README scopes ### *Axiom-'
     'free; core Lean only, no Mathlib* ### to a DIFFERENT module, saying of `Module1` only ### '
     '**`Genuine content, 0 sorry`.** ### **THE README IS EXACT; THE PAPER WIDENED IT.** ### And '
     'this act does ### NOT ### say the terminals carry axioms: nothing was built, no profile '
     'exists to read, and ### **AN IMPORT LINE IS NOT A MEASUREMENT.** ### **ROUTED. ### OPEN**'),
    ('`SIDE-effects` ships no printed axiom profile at all', 'STAND',
     '### **NEW at `b404` AS A LIMIT ON WHAT ANY PARKED-LANE ACT CAN CHECK THERE.** ### `0` '
     'profile files and `0` `.lean` files carrying a `#print axioms` line. ### **SO NO ACT CAN '
     'READ THAT PROFILE WITHOUT BUILDING**, and the lane is PARKED. ### **OPEN**'),
    ('the row`s law at six, and the three strains', 'STAND',
     '### **NEW at `b404`.** ### `STRAINED`: two sites share an index; one is empty in kind (b); '
     'one is from another discipline. ### **STILL A RESEMBLANCE, AND ONLY BECAUSE THE REFUSAL IS '
     'RESTATED AT EVERY ENTRY.** ### **OPEN**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES TWO ITEMS AND OPENS FIVE.**')
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


def do_faces():
    """### **ROW `U1`, TWO CELLS APPENDED TO, CHECKED CELL BY CELL AGAINST THE PRE-ACT BLOB.**"""
    before = io.open(FACES, encoding='utf-8', newline='').read()
    lines = before.split(chr(10))
    idx = [i for i, ln in enumerate(lines) if ln.startswith('| U1 |')]
    if len(idx) != 1:
        rec('  ### HARD FAILURE -- expected exactly one `U1` row, found %d.' % len(idx))
        return False, 0
    i = idx[0]
    if '(b404)' in lines[i]:
        rec('  ### ALREADY FILED -- the b404 segments are present. ### NOTHING APPENDED.')
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
    for lbl, cond in (('the row still reads `U1`', al[i].startswith('| U1 |')),
                      ('(v) is present', '**(v) THE REPRESENTATION-DEPENDENT CONSTANT**' in al[i]),
                      ('(vi) is present', '**(vi) THE TYPE-D RESIDUE' in al[i]),
                      ('the two kinds of emptiness are named', 'IS KIND (b)' in al[i]),
                      ('the countermodel is reported not typed',
                       'NOT TYPED AS A BRIDGE' in al[i]),
                      ('the strain is named', 'THE ROW’S LAW IS `STRAINED`' in al[i]),
                      ('the refusal is restated', 'types no bridge between' in al[i]),
                      ('the deposit refusal is quoted',
                       'deliberately **not** compiling the cross-register' in al[i]),
                      ('the navigator correction is carried',
                       'the window is the row’s **fourth**' in al[i])):
        ok = ok and cond
        rec('      %-42s : %s' % (lbl, cond))
    rec('  ### ### **%s**' % ('PASS' if ok else '### FAIL ###'))
    return ok, 2


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b404 — the fifth site entered, the sixth candidate entered, and the row’s law strained '
        '— filed 2026-09-10',
        '',
        '**Row `U1` gains two instances and its law is reported STRAINED.** `(v)` **the '
        'representation-dependent constant**: Lagarias Theorem 6.1’s finite-place bound holds *"in '
        'which the implied constant in the O-notation depends on π"* while Theorem 5.1’s '
        'archimedean constant is **ABSOLUTE** — an error term indexed by the representation where '
        'the record needs one that is not. `(vi)` **the Type-D residue**: the '
        'additive–multiplicative conspiracy keystone states its own boundary as *"the step from '
        '‘consistent at every finite modulus’ to ‘holds globally’ … interchanges a per-modulus '
        'quantifier with a global one"* and files the residue, in the same words at all three '
        'problems, as **the whole of the remaining weight**.',
        '',
        '**And `(v)` is empty as an obstruction, so this act mints the distinction the row had no '
        'way to make.** **KIND (a): empty because there is nothing to range over — vacuous '
        'forever. KIND (b): empty because the available uniformity ranges over a class that does '
        'not contain the corpus’s other object — the obstruction real, the instrument aimed '
        'elsewhere.** `(v)` is **kind (b)**, and the premise the draft reasoned from is false: '
        '**the corpus is not a one-L-function corpus.** Row F7 is a second object already aimed '
        'at, and b325 measured the failure across the two — *THE ARCHIMEDEAN DISTRIBUTION DOES NOT '
        'TRANSFER*, `Γ(s)` against `Γ(s/2)`. What defeats π-uniformity is not that there is '
        'nothing to be uniform across, but that **Theorem 6.1 ranges over irreducible cuspidal '
        'unitary automorphic representations on GL(N) and the corpus’s second object is not '
        'established to be one** — the record’s own `H-CUSP` grade shows even ζ sits there only '
        'under the source’s convention.',
        '',
        '**And the keystone’s boundary paragraph carries something this row has never cited.** The '
        'same sentence reports the programme has the row’s own shape **compiled** in the RH '
        'setting: the unrestricted commutation of the two quantifiers is **FALSE AS A THEOREM**, '
        'with an explicit countermodel, and it **closes only under a shared witness**. **That is '
        'reported and not typed as a bridge** — a theorem about a *shape* is not a theorem about '
        'any instance of it, and the row’s law forbids the crossing.',
        '',
        '**ADDITION TWO — two theorems, and the expectation’s parting point is refuted by a printed '
        'line.** `crt_exhaustiveness` (SIDE-effects) says every periodic structural coupling is a '
        'congruence condition at its own period — and the modular coupling it produces has a '
        '**singleton** moduli set, `moduli := {L}`. `finite_side_silence` (SIDE-global-section) is '
        'stated at one place `p` and one level `n`, general in both, per-cell in its third '
        'conjunct, and forms no product over places. **They are two, and they do NOT part at the '
        'passage from finitely many moduli to a restricted product, because neither of them ever '
        'reaches a restricted product** — the first does not even reach finitely-many-plural. They '
        'part far earlier: one is about the periodicity of a predicate on the naturals, the other '
        'about the p-adic decomposition of an index in a grid. **So the corpus has not proved its '
        'own boundary twice; it has proved two different small things on either side of a boundary '
        'neither one crosses.**',
        '',
        '**And half of Addition Two’s instruction could not be carried out, which is a limit and '
        'not an omission.** It asks for both terminals read *with axiom profiles printed*. '
        '`SIDE-global-section` ships `AXIOM_PRINTS.txt` and `finite_side_silence` is on it, **read '
        'and not run**. **`SIDE-effects` ships no printed profile at all and not one `#print '
        'axioms` line in any `.lean` file**, and the instrument lane is PARKED — so the profile of '
        '`no_type_d_conspiracies` is **reported unread, not inferred**.',
        '',
        '**And the keystone widens a claim the repository scopes narrowly, at the ref the keystone '
        'itself cites.** The paper writes of `SIDE-effects` at `c66f3c5`: *vanilla Lean 4, no '
        'Mathlib*, and that *the `0 sorry, 0 axioms` claim holds of the structural theorems*, '
        'naming `Module1.no_type_d_conspiracies` and `crt_exhaustiveness`. **At that very ref '
        '`Module1.lean` imports Mathlib**, and the repository’s own README scopes *Axiom-free; core '
        'Lean only, no Mathlib* to a **different module**, saying of `Module1` only **“Genuine '
        'content, 0 sorry”**. **The README is exact; the paper widened it.** And this act does '
        '**not** say the terminals carry axioms — nothing was built, no profile exists to read, '
        'and **an import line is not a measurement**. **Reported and ROUTED; the keystone is not '
        'edited.**',
        '',
        '**COMPONENT 3 — the row’s law at six: STRAINED, with three strains named rather than '
        'summed.** (1) **(iii) and (iv) share an index** — the support width — so they are not two '
        'independent witnesses. (2) **(v) is empty in kind (b)**, so counting the row’s instances '
        'as live obstructions over-counts by one. (3) **(vi) is from a different discipline** — '
        'additive number theory with a compiled local half, against five analytic sites — and *a '
        'row that spans two disciplines is either a deep observation or a loose one, and nothing '
        'in the row decides which*. **It is still naming a resemblance, and only because its '
        'refusal is restated at every entry; but the margin is thinner at six than at three.** '
        '**What would relieve it is ROUTED and not applied:** every entry naming its missing '
        'statement exactly and filing its residue as the whole of the remaining weight — the '
        'keystone’s own form, which **one of the six already has**.',
        '',
        '*The navigator’s correction is recorded where the entry is made: the b403 ferry called the '
        'window a fifth site; the window is the row’s fourth, entered by b401, and b403 entered '
        'nothing. No grade moved or was conferred. No bridge is typed between any two of the six. '
        'No keystone was edited and no kernel was built. Nothing deposits and the platform was not '
        'called at all. h2 stands exactly where the deposit left it.*',
        '',
    ]


SCOPE = (
    "**SCOPE: THE FIFTH SITE ENTERED, THE SIXTH ENTERED, AND THE ROW'S LAW STRAINED.** Row U1 gains "
    "(v) THE REPRESENTATION-DEPENDENT CONSTANT -- Theorem 6.1's finite-place constant DEPENDS ON pi "
    "while Theorem 5.1's archimedean one is ABSOLUTE -- and (vi) THE TYPE-D RESIDUE, the "
    "conspiracy keystone's own boundary stated as a per-modulus-to-global quantifier interchange "
    "with the residue filed as THE WHOLE OF THE REMAINING WEIGHT. **(v) IS EMPTY AS AN OBSTRUCTION "
    "AND THIS ACT MINTS THE DISTINCTION THE ROW LACKED: KIND (a) empty because there is nothing to "
    "range over, vacuous forever; KIND (b) empty because the available uniformity ranges over a "
    "class that does not contain the corpus's other object. (v) IS KIND (b).** The draft's premise "
    "is FALSE -- the corpus is NOT a one-L-function corpus, row F7 being a second object already "
    "aimed at and b325 having measured the transfer failure across the two -- and what defeats "
    "pi-uniformity is that Theorem 6.1 ranges over cuspidal automorphic representations on GL(N) "
    "and the corpus's second object is not established to be one, the record's own H-CUSP grade "
    "showing even zeta sits there only under the source's convention. **AND THE KEYSTONE'S "
    "BOUNDARY PARAGRAPH CARRIES A COMPILED NEGATIVE RESULT ABOUT THE ROW'S OWN SHAPE THAT THE ROW "
    "HAS NEVER CITED:** the unrestricted commutation of the two quantifiers is FALSE AS A THEOREM "
    "with an explicit countermodel and closes only under a shared witness -- **REPORTED AND NOT "
    "TYPED AS A BRIDGE**, a theorem about a shape not being a theorem about an instance. **ADDITION "
    "TWO: TWO THEOREMS, AND (N5)'S PARTING POINT REFUTED BY A PRINTED LINE** -- crt_exhaustiveness "
    "produces a SINGLETON moduli set and finite_side_silence is at one place forming no product, so "
    "NEITHER EVER REACHES A RESTRICTED PRODUCT and they part far earlier, one about the periodicity "
    "of a predicate on the naturals and the other about the p-adic decomposition of an index. **THE "
    "CORPUS HAS NOT PROVED ITS OWN BOUNDARY TWICE.** **AND HALF THE INSTRUCTION COULD NOT BE "
    "CARRIED OUT:** SIDE-global-section ships a printed profile and finite_side_silence is on it, "
    "READ AND NOT RUN; SIDE-effects ships NO printed profile and NOT ONE `#print axioms` line, and "
    "the lane is PARKED, so that profile is REPORTED UNREAD AND NOT INFERRED. **AND THE KEYSTONE "
    "WIDENS A CLAIM THE REPOSITORY SCOPES NARROWLY, AT THE REF IT ITSELF CITES**: Module1.lean "
    "imports Mathlib at c66f3c5, and the README scopes its no-Mathlib/axiom-free claim to a "
    "different module, saying of Module1 only `Genuine content, 0 sorry`. THE README IS EXACT; THE "
    "PAPER WIDENED IT -- and this act does NOT say the terminals carry axioms, because AN IMPORT "
    "LINE IS NOT A MEASUREMENT. **COMPONENT 3: THE ROW'S LAW IS STRAINED**, three strains named -- "
    "(iii) and (iv) share an index, (v) is empty in kind (b), and (vi) is from another discipline "
    "-- still a resemblance and only because the refusal is restated at every entry. NO GRADE MOVED "
    "OR CONFERRED, NO BRIDGE TYPED BETWEEN ANY TWO OF THE SIX, NO KEYSTONE EDITED, NO KERNEL BUILT, "
    "NO .lean FILE TOUCHED, NO LOCKED FACE EDITED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR "
    "AMENDED, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NEITHER MAP TOUCHED, "
    "NO CLUSTER RESHAPED, NO LIST CLOSED. NOTHING DEPOSITS; **THE PLATFORM WAS NOT CALLED AT ALL**. "
    "THE INSTRUMENT LANE AND THE INSTRUMENT-AUDIT LANE STAY PARKED. THE WAVE STAYS PARKED. M-2 "
    "REMAINS (SPECIFIED-NOT-STATED). THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. **THE CLAUSE "
    "HAS NOT MOVED AND (Q400) IS NOT OPENED: NAMING A SITE IS NOT CLOSING ONE.** h2 stands exactly "
    "where the deposit left it.")


def corr_rows(Q):
    m = ("**THE ROW GAINS TWO SITES AND ITS LAW IS STRAINED; ONE SITE IS EMPTY IN A KIND THE ROW "
         "COULD NOT PREVIOUSLY NAME; AND THE RECORD HOLDS A COMPILED COUNTERMODEL FOR THE ROW'S OWN "
         "SHAPE THAT THE ROW HAS NEVER CITED** (b404, the fifth and sixth sites)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b404 -- %d gates read, %d checked by digest; %d reads, %d ANCHORED; %d source "
            "fragments located in artefacts VERIFIED by digest. **(v)** the representation-"
            "dependent constant (Theorem 6.1 DEPENDS ON pi; Theorem 5.1 ABSOLUTE) and **(vi)** the "
            "Type-D residue (the keystone's own per-modulus-to-global interchange, residue filed as "
            "THE WHOLE OF THE REMAINING WEIGHT) are ENTERED. **TWO KINDS OF EMPTINESS ARE MINTED "
            "AND (v) IS KIND (b)**: not empty for want of anything to range over -- row F7 is a "
            "second L-function and b325 measured the transfer failure -- but because Theorem 6.1 "
            "ranges over cuspidal automorphic representations on GL(N) and the corpus's second "
            "object is not established to be one. **THE COMPILED COUNTERMODEL IS REPORTED AND NOT "
            "TYPED AS A BRIDGE.** **ADDITION TWO: TWO THEOREMS AND (N5)'S PARTING POINT REFUTED** -- "
            "crt_exhaustiveness produces a SINGLETON moduli set, finite_side_silence forms no "
            "product over places, and NEITHER REACHES A RESTRICTED PRODUCT. **ONE PROFILE READ FROM "
            "A PRINTED FILE, ONE REPORTED UNREAD** because SIDE-effects ships none and the lane is "
            "PARKED. **AND THE KEYSTONE WIDENS A CLAIM THE README SCOPES NARROWLY, AT THE REF IT "
            "CITES**; ROUTED, not repaired, and NO CLAIM IS MADE THAT THE TERMINALS CARRY AXIOMS. "
            "COMPONENT 3: the row's law is **STRAINED**, three strains named. %d GRADES MOVED, %d "
            "BRIDGES TYPED, %d KEYSTONES EDITED, %d KERNELS BUILT, %d CONTENT LOST"
            % (LG['gates_read'], LG['face_subject_gates'], READS, ANCH, F['srclocated'],
               0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT AND "
            "NO `.lean` FILE TOUCHED: BOTH EXHAUSTIVENESS TERMINALS WERE READ AT CONTENT, ONE OF "
            "THEIR PROFILES WAS READ FROM A PRINTED FILE AND THE OTHER IS REPORTED UNREAD. ### "
            "ENTERING A SITE IN A RESEMBLANCE ROW IS NOT TYPING A BRIDGE, AND NAMING A SITE IS NOT "
            "CLOSING ONE")
    prof = ("### THE ONE AXIOM PROFILE THIS ACT READS IS `B329.finite_side_silence` FROM "
            "`AXIOM_PRINTS.txt`, READ AND NOT RUN. ### THE OTHER IS NOT READ AND NOT INFERRED. ### "
            "NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, "
            "NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO "
            "CLUSTER RESHAPED, NO LIST CLOSED, NO KEYSTONE EDITED, NO LOCKED FACE EDITED. ### THE "
            "CORPUS WRITES ARE TWO CELLS OF ONE LEDGER ROW, APPENDED TO AND CHECKED CELL BY CELL "
            "AGAINST THE PRE-ACT BLOB, AND ONE APPEND-ONLY TRAIL BLOCK -- 0 CONTENT LOST")
    grade = ("### EVERY CLAIM QUOTED FROM ANOTHER DOCUMENT IS QUOTED WITH THE SENTENCE THAT SCOPES "
             "IT, WHICH IS THE DEFECT THIS ACT REPORTS AND WOULD HAVE FORFEITED BY COMMITTING. ### "
             "THE EMPTINESS OF A SITE IS NAMED BY KIND RATHER THAN ASSERTED, BECAUSE A SITE EMPTY "
             "FOR WANT OF ANYTHING TO RANGE OVER AND A SITE EMPTY BECAUSE THE INSTRUMENT IS AIMED "
             "ELSEWHERE ARE DIFFERENT FACTS. ### A COMPILED RESULT ABOUT THE ROW'S SHAPE IS "
             "REPORTED WITHOUT BEING TYPED AS A BRIDGE TO ANY INSTANCE. ### AN EXPECTATION'S "
             "PREMISE WAS CHECKED BEFORE ITS CONCLUSION WAS DRAWN, AND THE PREMISE WAS FALSE WHILE "
             "THE CONCLUSION SURVIVED ON OTHER GROUNDS. ### AND WHERE AN INSTRUCTION COULD NOT BE "
             "CARRIED OUT THE ACT SAYS SO RATHER THAN SUBSTITUTING WHAT IT COULD DO")
    status = ("data/b404_the_fifth_and_sixth_sites.txt; data/b404_components_run.txt; "
              "data/b404_extract_notes3.txt; data/b404_registration_2026-09-10.txt (LOCKED before "
              "any write at sha256 %s, chained on tools/b378_lockgate.py run as b404); "
              "tools/b404_extract.py; tools/b404_regspec.py; tools/b404_reg_gate.py; "
              "tools/b404_components.py; tools/b404_desk_bank.py; tools/b404_checks.py; "
              "PLACE-papers FACES_LEDGER.md (row U1, two cells appended to) and OPEN_TRAILS.md "
              "(one append-only block); CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what is the fifth uniformity site',
           'is the type-d residue a uniformity obstruction',
           'what kinds of empty can a uniformity site be',
           'does the corpus study more than one l-function',
           'are the two exhaustiveness theorems one theorem',
           'can the side-effects axiom profile be read')
MUST_NOT_HIT = ('a bridge was typed', 'the terminals carry axioms', 'a keystone was edited',
                'the row was restated', 'a kernel was built')

KEY = 'the-fifth-and-sixth-sites'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b404 ENTERED TWO SITES IN THE UNIFORMITY ROW AND REPORTED ITS LAW **STRAINED**. **(v) THE "
        "REPRESENTATION-DEPENDENT CONSTANT**: Lagarias Theorem 6.1's finite-place bound holds *in "
        "which the implied constant in the O-notation DEPENDS ON pi*, while Theorem 5.1's "
        "archimedean constant is ABSOLUTE. **(vi) THE TYPE-D RESIDUE**: the additive-multiplicative "
        "conspiracy keystone states its own boundary as *the step from consistent at every finite "
        "modulus to holds globally interchanges a per-modulus quantifier with a global one*, and "
        "files the residue as THE WHOLE OF THE REMAINING WEIGHT at all three problems. **AND (v) IS "
        "EMPTY AS AN OBSTRUCTION, SO THE ACT MINTS THE DISTINCTION THE ROW LACKED: KIND (a) EMPTY "
        "BECAUSE THERE IS NOTHING TO RANGE OVER, VACUOUS FOREVER; KIND (b) EMPTY BECAUSE THE "
        "AVAILABLE UNIFORMITY RANGES OVER A CLASS THAT DOES NOT CONTAIN THE CORPUS'S OTHER OBJECT. "
        "(v) IS KIND (b).** The corpus is NOT a one-L-function corpus -- row F7 is a second object "
        "and b325 measured the transfer failure across the two -- but Theorem 6.1 ranges over "
        "cuspidal automorphic representations on GL(N) and the corpus's second object is not "
        "established to be one. **THE KEYSTONE'S BOUNDARY PARAGRAPH CARRIES A COMPILED NEGATIVE "
        "RESULT ABOUT THE ROW'S OWN SHAPE THAT THE ROW HAS NEVER CITED**: the unrestricted "
        "commutation of the two quantifiers is FALSE AS A THEOREM with an explicit countermodel and "
        "closes only under a shared witness -- REPORTED AND NOT TYPED AS A BRIDGE. **ADDITION TWO: "
        "TWO THEOREMS, AND THE EXPECTED PARTING POINT IS REFUTED** -- crt_exhaustiveness produces a "
        "modular coupling with a SINGLETON moduli set and finite_side_silence is at one place "
        "forming no product, so NEITHER EVER REACHES A RESTRICTED PRODUCT; they part far earlier, "
        "one about the periodicity of a predicate on the naturals and the other about the p-adic "
        "decomposition of an index in a grid. **THE CORPUS HAS NOT PROVED ITS OWN BOUNDARY TWICE.** "
        "**ONE AXIOM PROFILE READ FROM A PRINTED FILE, ONE REPORTED UNREAD**: SIDE-effects ships no "
        "printed profile and not one `#print axioms` line, and the lane is PARKED. **AND THE "
        "KEYSTONE WIDENS A CLAIM THE REPOSITORY SCOPES NARROWLY, AT THE REF IT ITSELF CITES** -- "
        "Module1.lean imports Mathlib at c66f3c5 while the README scopes its no-Mathlib/axiom-free "
        "claim to a different module and says of Module1 only `Genuine content, 0 sorry`. THE "
        "README IS EXACT; THE PAPER WIDENED IT. **AND THE ACT DOES NOT SAY THE TERMINALS CARRY "
        "AXIOMS: AN IMPORT LINE IS NOT A MEASUREMENT.**")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED AND NO OBJECT RECOMPUTED. ### THE ONE "
        "PROFILE READ IS `B329.finite_side_silence` FROM AXIOM_PRINTS.txt, READ AND NOT RUN; THE "
        "OTHER IS REPORTED UNREAD AND NOT INFERRED. ### NO GRADE MOVED OR CONFERRED, NO BRIDGE "
        "TYPED BETWEEN ANY TWO OF THE SIX SITES, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO FACE "
        "PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLASS RULED, NO LIST CLOSED. ### THE "
        "CORPUS WRITES ARE TWO CELLS OF ROW U1, APPENDED TO AND CHECKED CELL BY CELL AGAINST THE "
        "PRE-ACT BLOB WITH THE OTHER FIVE BYTE-IDENTICAL, AND ONE APPEND-ONLY TRAIL BLOCK. ### "
        "EVERY CLAIM QUOTED FROM ANOTHER DOCUMENT IS QUOTED WITH THE SENTENCE THAT SCOPES IT. ### "
        "NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND "
        "(Q400) IS NOT OPENED")
    where = (
        "data/b404_the_fifth_and_sixth_sites.txt; data/b404_components_run.txt; "
        "data/b404_extract_notes3.txt; data/b404_registration_2026-09-10.txt (LOCKED before any "
        "write, chained on tools/b378_lockgate.py run as b404 -- %d gates read, %d checked by "
        "digest); tools/b404_extract.py; tools/b404_components.py; tools/b404_desk_bank.py; "
        "tools/b404_checks.py; PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md "
        "row %d" % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b404 (two sites entered, one of them empty in a kind the row could not previously name, '
           'and a compiled countermodel for the row\'s own shape found uncited in the record)')
    row_new = ('    # ### THE FIFTH AND SIXTH SITES (b404).%s'
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
        rec('    %-52s reaches the b404 key : %s' % (qq, g2))
    for lbl, cond in (
            ('(v) is named', 'THE REPRESENTATION-DEPENDENT CONSTANT' in out),
            ('(vi) is named', 'THE TYPE-D RESIDUE' in out),
            ('the two kinds are minted', 'KIND (a)' in out and 'KIND (b)' in out),
            ('(v) is kind (b)', '(v) IS KIND (b)' in out),
            ('the second L-function is named', 'row F7 is a second object' in out),
            ('the countermodel is reported not typed', 'NOT TYPED AS A BRIDGE' in out),
            ('two theorems', 'TWO THEOREMS' in out),
            ('the parting point is refuted', 'NEITHER EVER REACHES A RESTRICTED PRODUCT' in out),
            ('one profile unread', 'ONE REPORTED UNREAD' in out),
            ('the keystone widened a scoped claim', 'THE PAPER WIDENED IT' in out),
            ('no axiom claim is made', 'AN IMPORT LINE IS NOT A MEASUREMENT' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok, cells):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A('b404 -- THE FIFTH SITE, THE SIXTH CANDIDATE, AND THE ROW`S LAW. ### THE BANK.')
    A('### Ferry part 1 of 1, receipt confirmed IN FULL (Rule 1). ### 2026-09-10.')
    A('### CONCURRENCY: SOLO (research seat).')
    A('### The face was LOCKED before any write at sha256 `%s`.' % SEALHASH)
    A(BAR)
    A('')
    A(SUB)
    A('### THE FIVE VERDICTS.')
    A(SUB)
    A('### ### ### **COMPONENT 1 : ### ENTERED AS `(v)`.**')
    A('### ### ### **COMPONENT 2 : ### NOT EMPTY IN KIND (a); ### EMPTY IN KIND (b).**')
    A('### ### ### **ADDITION ONE : ### ENTERED AS `(vi)`.**')
    A('### ### ### **ADDITION TWO : ### TWO THEOREMS, AND `(N5)`S PARTING POINT REFUTED.**')
    A('### ### ### **COMPONENT 3 : ### STRAINED.**')
    A('')
    A(SCOPE)
    A('')
    A(SUB)
    A('### THE TWO KINDS OF EMPTINESS, MINTED HERE BECAUSE THE ROW HAD NO WAY TO SAY WHICH.')
    A(SUB)
    A('### **KIND (a) -- EMPTY BECAUSE THERE IS NOTHING TO RANGE OVER.** ### The index has one')
    A('### value. ### **VACUOUS FOREVER; NOTHING COULD EVER MAKE THE SITE BITE**, and a site empty')
    A('### in kind (a) should never have been entered.')
    A('### **KIND (b) -- EMPTY BECAUSE THE AVAILABLE UNIFORMITY RANGES OVER A CLASS THAT DOES NOT')
    A('### ### CONTAIN YOUR OTHER OBJECT.** ### The obstruction is REAL and the instrument is')
    A('### AIMED ELSEWHERE. ### **A DIFFERENT STATEMENT COULD BITE**, and the site is entered.')
    A('### ### ### **`(v)` IS KIND (b), AND THE PREMISE THE DRAFT REASONED FROM IS FALSE:** ### the')
    A('### corpus is ### **NOT** ### a one-L-function corpus. ### Row `F7` is a second object')
    A('### already aimed at, and `b325` measured the failure across the two.')
    A('')
    A(SUB)
    A('### WHAT THE ACT WROTE, AND WHAT IT DID NOT.')
    A(SUB)
    A('### **THE LEDGER WRITE** ### -- `%d` cells of row `U1`, APPENDED TO and checked CELL BY CELL'
      % cells)
    A('### against the PRE-ACT blob, the other five ### **BYTE-IDENTICAL**. ### **`0` CONTENT LOST.')
    A('### ### `0` GRADES MOVED. ### `0` BRIDGES TYPED. ### `0` KEYSTONES EDITED.**')
    A('### **THE DESK** ### -- `%d` items swept, `%d` closed, `%d` standing, `%d` lists closed.'
      % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    A('### **THE SURVEY** ### -- `%d` reads, `%d` ANCHORED; `%d` source fragments located in'
      % (READS, ANCH, F['srclocated']))
    A('### artefacts VERIFIED against the corpus`s banked digests BEFORE a word was read.')
    A('### **THE GATE CHAIN** ### -- `%d` gates read, `%d` passing, `%d` checked by digest.'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A('### **THE ROW AND THE KEY** ### -- correspondence row `%d`; index key `%s` : %s.'
      % (rownum, KEY, 'PASS' if kok else 'FAIL'))
    A('')
    A(SUB)
    A('### THE TWO FINDINGS ABOUT OTHER PEOPLE`S DOCUMENTS, BOTH ROUTED.')
    A(SUB)
    A('### ### **(1) THE KEYSTONE WIDENS A CLAIM THE REPOSITORY SCOPES NARROWLY, AT THE REF IT')
    A('### ### ITSELF CITES.** ### `Module1.lean` imports Mathlib at `c66f3c5`; the README scopes')
    A('### its *Axiom-free; core Lean only, no Mathlib* to a DIFFERENT module and says of `Module1`')
    A('### only ### **`Genuine content, 0 sorry`.** ### **THE README IS EXACT; THE PAPER WIDENED')
    A('### ### IT.** ### **ROUTED. ### THE KEYSTONE IS NOT EDITED.**')
    A('### ### **(2) `SIDE-effects` SHIPS NO PRINTED AXIOM PROFILE AT ALL** -- `%d` profile files'
      % len(F.get('se_profile_files') or []))
    A('### and `%d` `.lean` files carrying a `#print axioms` line. ### **SO NO PARKED-LANE ACT CAN'
      % F.get('se_axiomcheck_files', 0))
    A('### ### READ THAT PROFILE**, and this one does not build. ### **ROUTED.**')
    A('### ### **AND WHAT THIS ACT DOES NOT SAY, IN THE SAME BREATH:** ### it does ### NOT ### say')
    A('### the terminals carry axioms. ### **AN IMPORT LINE IS NOT A MEASUREMENT**, and a claim')
    A('### shown to rest on a false premise is not thereby shown false.')
    A('')
    A(SUB)
    A('### WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It types no bridge between any two of the six sites, least of all between the compiled')
    A('### countermodel and any instance. ### **A THEOREM ABOUT A SHAPE IS NOT A THEOREM ABOUT AN')
    A('### ### INSTANCE OF IT.**')
    A('### It does not restate the row, and it does not apply what would relieve its strain.')
    A('### It does not decide `H-CUSP`, edit a keystone, build a kernel, or move a grade.')
    A('### It does not close a site by naming one. ### **NAMING A SITE IS NOT CLOSING ONE.**')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### h2 STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    rec('  ### bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))


def main():
    bar('=')
    rec('b404 -- THE DESK, ROW `U1`, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.')
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
        run_clock.write(D, 'b404_desk_notes', LINES)
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
        rec('  ### the b403 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            run_clock.write(D, 'b404_desk_notes', LINES)
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_v': 'the representation-dependent constant' in low,
        'says_vi': 'the type-d residue' in low,
        'says_kinds': 'kind (a)' in low and 'kind (b)' in low,
        'says_v_is_b': '(v)** is **kind (b)' in low or 'is **kind (b)**' in low,
        'says_not_one_lfunction': 'not a one-l-function corpus' in low,
        'says_countermodel': 'false as a theorem' in low,
        'says_not_a_bridge': 'not typed as a bridge' in low,
        'says_two_theorems': 'they are two' in low or 'two theorems' in low,
        'says_no_restricted_product': 'never reaches a restricted product' in low
                                      or 'ever reaches a restricted product' in low,
        'says_profile_unread': 'reported unread, not inferred' in low,
        'says_widened': 'the paper widened it' in low,
        'says_not_axioms': 'an import line is not a measurement' in low,
        'says_strained': 'strained' in low,
        'says_three_strains': 'share an index' in low,
        'says_routed_relief': 'routed and not applied' in low,
        'says_correction': 'the window is the row’s fourth' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-30s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b404_desk_notes', LINES)
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
        run_clock.write(D, 'b404_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b404_desk_notes', LINES)
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
            run_clock.write(D, 'b404_desk_notes', LINES)
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
    run_clock.write(D, 'b404_desk_notes', LINES)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
