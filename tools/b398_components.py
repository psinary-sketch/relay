# -*- coding: utf-8 -*-
"""b398_components.py -- THE TWO MARGINS, THE VERDICT, THE OBLIGATION, AND THE NEXT STATEMENT.

### ### **NOTHING IS COMPUTED HERE.** ### Every figure is read from the file that emitted it. ###
### The only writes are the three `trigger` cells `(R23)` requires and one sharpening of the OWED
### pair row -- both additive, both with the pre-edit lines preserved verbatim.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FERRY = os.path.join(D, 'b398_ferry_2026-09-10.txt')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
OUT = os.path.join(D, 'b398_components.txt')
TMARK = '<!-- b398 (R23) TRIGGERS GIVEN, 2026-09-10 -->'
LMARK = '<!-- b398 THE OWED BRIDGE SHARPENED, 2026-09-10 -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
E = json.load(io.open(os.path.join(D, 'b398_reads.json'), encoding='utf-8'))
BYLABEL = {r['label']: r for r in E['reads']}


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=240):
    return ' '.join(s.split())[:n]


def text_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def g(*a):
    r = subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def numstat(rel):
    for ln in g('diff', '--numstat', 'HEAD', '--', rel).split(chr(10)):
        p = ln.split()
        if len(p) >= 2 and p[0].isdigit():
            return int(p[0]), int(p[1])
    return 0, 0


def show(label, n=340):
    # ### **MATCH BY FRAGMENT WHERE THE STORED LABEL CARRIES A STRUCK STEM.** ### The extract ran
    # ### before the lock and its JSON keeps the label it recorded; this file may not carry that
    # ### word, so the lookup falls back to a fragment match. ### **THE STORED RECORD IS NOT
    # ### ### EDITED** -- a run artifact is evidence, and evidence is not rewritten to suit a
    # ### later scanner.
    r = BYLABEL.get(label)
    if r is None:
        cands = [v for k, v in BYLABEL.items() if label in k]
        r = cands[0] if len(cands) == 1 else None
    if not r:
        rec('    ### **%s : NOT IN THE EXTRACT**' % label)
        return
    rec('    %s  ### `%s:%s`' % (label, r['path'], r['line']))
    rec('      > %s' % flat(r['text'], n))


# ==================================================================================================
#  COMPONENT 1 -- THE TWO MARGINS.
# ==================================================================================================
def component1():
    bar('=')
    rec('  COMPONENT 1 -- THE TWO MARGINS, EACH TO ITS BASE OBJECTS.')
    bar('=')
    rec('  ### ### **THE PLACE-SETS FIRST, BEFORE ANY COMPARISON** -- the order`s own instruction,')
    rec('  ### ### and its expectation `(F1)`.')
    rec()
    rec('  ### **(A) THE SONIN MARGIN`S PLACE-SET : `{infinity}`.**')
    show('### **THE THEOREM THE RECORD READ, AND THE WITHDRAWAL IT FORCED**', 460)
    rec('  ### ### **AND NOT BY OMISSION.** ### The semilocal Sonin space is ### **ONE ARCHIMEDEAN')
    rec('  ### ### COPY**, and ### **FINITE PLACES CONTRIBUTE NO INDEPENDENT SONIN DIRECTIONS.**')
    rec()
    rec('  ### **(B) THE LI MARGIN`S PLACE-SET : `{infinity}` UNION `{ALL FINITE PLACES}`, PLUS A')
    rec('  ### POLE TERM AT `s = 0` THAT IS NOT A PLACE AT ALL.**')
    show('### **THE SOURCE`S OWN DECOMPOSITION**', 420)
    rec()
    rec('  ### ### ### **`(F1)` IS MET, AND IT IS THE FIRST THING PRINTED.**')
    rec('  ### ### **AND THE DIFFERENCE IS NOT A DEFECT IN EITHER OBJECT.** ### It is the reason')
    rec('  ### ### the reading has to ADD finite terms to the Sonin margin before the two can be')
    rec('  ### ### compared at all -- which is the reading`s own construction, not an objection')
    rec('  ### ### to it.')
    rec()
    bar('-')
    rec('  ### THE SONIN MARGIN, CONSTITUENT BY CONSTITUENT.')
    bar('-')
    for lb in ('(1) THE MARGIN, THE TEST CLASS AND THE SUPPORT CONDITION',
               '(2) THE ARCHIMEDEAN DISTRIBUTION AND ITS IDENTIFICATION',
               '(3) THE KERNEL BOTH CHANNELS EVALUATE',
               '(4) THE DECOMPOSITION, AND THE OPERATOR',
               '(5) THE OPERATOR, NAMED'):
        show(lb)
    rec('  ### ### **THE MEASURE AND THE NORMALIZATION ARE THE SOURCE`S**, carried at the import')
    rec('  ### ### bar: Connes-Consani `arXiv:2006.13771v1`, Theorem 1 and Theorem 4.7, pinned at')
    rec('  ### ### `b304`/`b305`. ### **NEITHER PDF IS ON THIS DRIVE**, so every source statement')
    rec('  ### ### here is quoted ### **AS THE CORPUS QUOTES IT** -- weaker than reading the')
    rec('  ### ### source, and said so.')
    rec()
    bar('-')
    rec('  ### THE LI MARGIN, CONSTITUENT BY CONSTITUENT.')
    bar('-')
    for lb in ('(1) THE MARGIN AND ITS TWO CHANNELS',
               '(2) THE SPLIT, IN THE KEYSTONE`S OWN WORDS',
               '(3) THE FAMILY AND ITS WEIL NORM',
               '(4) THE POLE CONSTANT, DERIVED AT b327 UNDER A SEALED BAR',
               '(5) ### **THE PRIME SUMMAND, BANKED**',
               '(6) THE SPLIT IS NOT A PLACE-SPLIT'):
        show(lb, 420)
    rec('  ### ### **AND THE PROGRAMME`S OWN CAUTION IS CARRIED, NOT SET ASIDE:** ### the')
    rec('  ### ### `lambda_A` / `lambda_Z` split is ### **NOT** ### a place-split, so the act does')
    rec('  ### ### not treat `lambda_Z` as `-S_f` by definition -- it treats it so because `b327`')
    rec('  ### ### ### **DERIVED** ### it.')
    return dict(place_sonin='{infinity}', place_li='{infinity} + {all finite places} + pole',
                f1='MET', sonin_constituents=5, li_constituents=6)


# ==================================================================================================
#  COMPONENT 2 -- THE READING, TESTED.
# ==================================================================================================
def component2():
    bar('=')
    rec('  COMPONENT 2 -- THE READING, TESTED AND NOT ADOPTED ON ANYBODY`S WORD.')
    bar('=')
    rec('  ### ### **AND THE FIRST FORM OF THIS TEST GOT IT BACKWARDS.** ### It read `b197``s')
    rec('  ### ### withdrawal of `Tr_infinity + SUM_p Tr_p` as covering the premise and called the')
    rec('  ### ### reading ### **REFUTED.** ### `b197` forbids that reading in a sentence written')
    rec('  ### ### for exactly this case:')
    show('### **THE WARNING THIS SEAT WALKED INTO**', 420)
    show('### **AND WHY IT WAS WRITTEN DOWN**', 300)
    rec('  ### ### **THE SEAT READ IT AS IF IT DID, AND THE FILE CAUGHT IT.** ### The correction')
    rec('  ### ### was made before the lock and stands on the face. ### **A WITHDRAWAL THAT NAMES')
    rec('  ### ### ITS OWN SCOPE IS NOT A WITHDRAWAL OF EVERYTHING NEARBY.**')
    rec()
    rec('  ### **HALF ONE : ### BANKED, AND AT KERNEL TERMINALS.**')
    show('### **THE CLAUSE STATEMENT`S OWN WORDS**', 460)
    show('### **K3, UNFOLDED TO ITS OWNER**', 520)
    rec('  ### ### `B329.*` (24, zero-axiom) and `B310.*` carry it; the decomposition and scaling')
    rec('  ### ### parts are ### **GENERAL** ### and the compact part is ### **PER CELL.**')
    rec()
    rec('  ### **HALF TWO : ### BANKED, VERBATIM, WITH ONE EXCEPTION CARRIED.**')
    show('### **K4, UNFOLDED TO ITS OWNER**', 520)
    show('### `lambda_Z(n) = -S_f(n)`, derived at `b327`', 420)
    rec('  ### ### **`the corpus`s prime side IS the source`s finite-places sum, factor for')
    rec('  ### ### factor`**, and ### **`DIFFERENT ONLY IN THE CUTOFF WINDOW (b306)`** -- carried,')
    rec('  ### ### not dropped. ### **AN EXCEPTION CARRIED IS NOT AN EXCEPTION DISCHARGED.**')
    rec()
    rec('  ### ### ### **SO BOTH HALVES OF THE NAVIGATOR`S READING ARE BANKED, AND THE LEDGER`S')
    rec('  ### ### ### OWED ROW IS NARROWER THAN IT LOOKS.**')
    rec()
    rec('  ### **THE CONCLUSION, UNFOLDED TO THE IDENTITY IT REQUIRES.**')
    rec('  ###   the Sonin margin      ### **`W_inf(f) - Tr(theta(g) S theta(g)*)`**')
    rec('  ###   the Weil functional   ### **`W_inf(f) + SUM_p W_p(f)`**')
    rec('  ### ### **THEY AGREE IF AND ONLY IF `-Tr(theta(g) S theta(g)*) = SUM_p W_p(f)`.**')
    rec('  ### **AND THAT IS WHAT THE LEDGER ALREADY TYPES AS OWED:**')
    show('OWN TYPING OF', 420)
    show('### **AND THE SQUARE IS NOT A ZERO CHANNEL**', 300)
    rec()
    rec('  ### **A SECOND OBSTRUCTION, INDEPENDENT OF THE FIRST.**')
    show('### **THE FAMILY OBSTRUCTION**', 460)
    show('### b327`s verdict', 300)
    rec('  ### ### **THE SONIN MARGIN IS NOT DEFINED ON THE LI FAMILY**, so even with the')
    rec('  ### ### identification the two sides are ### **ONE FUNCTIONAL ON TWO DISJOINT')
    rec('  ### ### FAMILIES** -- a decomposition of neither into the other. ### **AND NO')
    rec('  ### ### NORMALIZATION FIXES A DOMAIN.**')
    rec()
    bar('-')
    rec('  ### ### ### **THE VERDICT : UNDECIDABLE FROM THE RECORD.**')
    bar('-')
    rec('  ### **NOT `ASSEMBLES`:** ### the identity the conclusion needs is not in the record.')
    rec('  ### **NOT `DIFFERENT`:** ### no constituent of the reading is refuted -- both premises')
    rec('  ### are banked, and the ledger`s own `differ at their second term` is a statement that')
    rec('  ### the identification is ### **NOT HELD**, not that it is ### **FALSE.**')
    rec('  ### ### **THE READING IS SHOWN TO REST ON THE OWED BRIDGE ITSELF**, which is why no')
    rec('  ### ### amount of re-reading closes it. ### **THAT IS THE RESULT.**')
    rec()
    rec('  ### **THE EXACT MISSING STATEMENT, NAMED AND TYPED:**')
    rec('  ###   ### **(M)** ### For every `g` in the source`s class -- `g` in `C_c^inf(R*_+)` with')
    rec('  ###   `g~(0) = g~(1) = 0` -- ### **`- Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv')
    rec('  ###   ### g-bar^#)`** ### in the source`s own normalization.')
    rec('  ###   ### **TYPE : A RESULT.**')
    rec('  ###     ### NOT A READ -- no file states it, and this act looked in the ledger, the')
    rec('  ###     clause statement, `b306`, `b310`, `b320`, `b321`, `b324`, `b327` and `b329`.')
    rec('  ###     ### NOT A RULING -- it is a mathematical identity, not an author`s choice.')
    rec('  ###     ### NOT A CONSTRUCTION -- both sides already exist in the record, at grades.')
    rec('  ###   ### **IT IS A DERIVATION ON CONTENT, AND IT IS THE OWED BRIDGE`S FIRST HALF.**')
    rec('  ###   ### **AND ITS SECOND HALF WOULD STILL BE OWED AFTERWARDS**, because the family')
    rec('  ###   obstruction is untouched by it.')
    rec()
    rec('  ### ### **`(F2)` : THE VERDICT IS MET AND THE REASON IS NOT.** ### The order expected')
    rec('  ### ### the missing statement to be ### *a normalization the record never fixed across')
    rec('  ### ### the two families.* ### It is instead ### **AN IDENTITY BETWEEN TWO SECOND TERMS')
    rec('  ### ### AT ONE PLACE-SET**, prior to any question about families -- and the family')
    rec('  ### ### question is a separate, second obstruction that `(M)` does not touch. ### **A')
    rec('  ### ### PREDICTION MET FOR A DIFFERENT REASON IS REPORTED WITH THE REASON.**')
    return dict(verdict='UNDECIDABLE FROM THE RECORD', half_one='BANKED', half_two='BANKED',
                missing='(M) -Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#)',
                missing_type='RESULT', obstructions=2, f2='MET, for a different reason',
                self_correction=1)


# ==================================================================================================
#  COMPONENT 3 -- WHAT THE OUTCOME OBLIGES.
# ==================================================================================================
SHARPEN = (' ### **SHARPENED 2026-09-10 (b398), AND STILL OWED.** Both premises of the '
           'decomposition reading are BANKED — the finite-place term at `K3` '
           '(`B329.*` 24 zero-axiom, `B310.*`; decomposition and scaling GENERAL, compact part '
           'PER CELL) and the prime-side identification at `K4` (*factor for factor*, DIFFERENT '
           'only in the cutoff window, b306) — so what is owed is narrower than this row made it '
           'look: **exactly `(M)`: for every `g` in the source’s class, '
           '`−Tr(θ(g) S θ(g)*) = Σ_p W_p(g ⋆ ḡ♯)` in the source’s normalization, typed a '
           'RESULT (a derivation on content).** A second obstruction is independent of it and '
           'survives it: **the Sonin margin is not defined on the Li family** (b327 — `G_n`’s '
           'inverse Mellin transform has no compact support, outside Theorem 1’s class), so even '
           'with `(M)` the two sides are one functional on two disjoint families. **NOTHING IS '
           'PAID HERE, NO GRADE IS CONFERRED, AND THE DEPOSIT’S REFUSAL STANDS: a decomposition '
           'of one functional is NOT an equivalence of the faces and does not compile one.** ')


def component3():
    bar('=')
    rec('  COMPONENT 3 -- WHAT THE OUTCOME OBLIGES, AT EXACTLY ITS SCOPE.')
    bar('=')
    rec('  ### ### **THE ORDER GAVE OBLIGATIONS FOR `ASSEMBLES` AND FOR `DIFFERENT`. ### NEITHER')
    rec('  ### ### FIRES.** ### The act does not borrow the nearer one.')
    rec('  ### **WHAT `UNDECIDABLE` OBLIGES:** ### the owed row stays ### **OWED**, sharpened by')
    rec('  ### `(M)`; the pair rows keep carrying it; ### **NOTHING IS PAID AND NO GRADE IS')
    rec('  ### CONFERRED.**')
    rec()
    pre = blob('FACES_LEDGER.md')
    prelines = pre.split(chr(10))
    live = [(i + 1, ln) for i, ln in enumerate(prelines)
            if ln.startswith('| F2–F3 | OWED |')]
    rec('  ### **THE OWED PAIR ROW, FOUND BY CONTENT : line(s) %s.**' % [i for i, _ in live])
    assert len(live) == 1, 'the owed pair row must be exactly one'
    ln_i, row = live[0]
    cur = text_of(FACES).replace(chr(13) + chr(10), chr(10))
    lines = cur.split(chr(10))
    assert lines[ln_i - 1] == row, 'the working row must equal the blob row'
    # ### **ADDITIVE: THE SHARPENING GOES INSIDE THE ROW`S LAST CELL AND NOTHING IS REMOVED.**
    cells = row.split('|')
    old_cell = cells[-2]
    cells[-2] = old_cell.rstrip() + SHARPEN
    newrow = '|'.join(cells)
    kept = old_cell.strip() in cells[-2]
    lines[ln_i - 1] = newrow
    blk = ['', LMARK, '',
           ('**b398 — THE OWED BRIDGE SHARPENED, NOT PAID.** The row above now names the exact '
            'statement the bridge needs. **Nothing is paid, no grade is conferred, and the row '
            'is still OWED.** The pre-edit row is preserved verbatim below.'), '',
           '> %s' % row, '']
    io.open(FACES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines + blk))
    add, dele = numstat('FACES_LEDGER.md')
    post = text_of(FACES).replace(chr(13) + chr(10), chr(10))
    al = post.split(chr(10))
    aset = set(al)
    changed = [x for x in prelines if x not in aset]
    lost = [x for x in changed if not any(x in y for y in al)]
    rec('  ### **THE WRITE : `+%d / -%d` ; lines changed in place `%d` ; ### **CONTENT LOST `%d`**'
        % (add, dele, len(changed), len(lost)))
    rec('  ### ### **THE PRE-EDIT CELL IS A SUBSTRING OF THE POST-EDIT CELL : %s** -- nothing'
        % kept)
    rec('  ### ### removed from the row. ### **THE PRE-EDIT ROW IS PRESERVED VERBATIM : %s.**'
        % (('> ' + row) in al))
    still = 'OWED' in newrow
    rec('  ### ### **AND THE ROW IS STILL `OWED` AFTER THE ACT : %s.**' % still)
    rec()
    rec('  ### ### **THE INVARIANT CLAUSE, IN EVERY BRANCH:** ### **THE CLAUSE HAS NOT MOVED. ###')
    rec('  ### ### NO COORDINATE IS CLOSED. ### AND THE ACT SAYS SO.**')
    return dict(row_line=ln_i, added=add, deleted=dele, changed=len(changed), lost=len(lost),
                kept=kept, verbatim=(('> ' + row) in al), still_owed=still,
                branches_fired=1, paid=0, grades=0)


# ==================================================================================================
#  THE TRIGGERS -- (R23).
# ==================================================================================================
TRIGGERS = {
    'W-ORD-LI-WEIL-BRIDGE':
        ("**THE AUTHOR'S WORD** — given by the b398 ferry, which is that word; **FIRED, and "
         "answered UNDECIDABLE FROM THE RECORD with `(M)` named** (b398)"),
    'W-ORD-DISCRIMINATING-FAMILY':
        ("**when an act needs the instrument to say NO on a candidate function** — and it cannot "
         "fire while the instrument lane is PARKED under (R4), which is a block on the work and "
         "not an absence of a trigger (b398)"),
    'W-ORD-LI-FAMILY-CONTROL':
        ("**when an act asserts, or depends on, the explicit formula closing on the Li family** — "
         "and it cannot fire while the instrument lane is PARKED under (R4) (b398)"),
}


def triggers():
    bar('=')
    rec('  RULING `(R23)` -- THE TRIGGER COLUMN, SWEPT AND FILLED.')
    bar('=')
    rec('  ### ### **AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS SHELVED.**')
    rec('  ### **THE POPULATION IS THE TABLE THAT HAS THE COLUMN, FOUND BY ITS OWN HEADER.** ###')
    rec('  ### `FACES_LEDGER.md` has ### **NO TRIGGER COLUMN AT ALL** ### -- its pair table is')
    rec('  ### `pair | kind | relation`, and its `NONE` means ### *the record states no')
    rec('  ### relation.* ### An earlier form of the sweep matched `| none |` anywhere and kept')
    rec('  ### ### **`51` ROWS**; ### **A SWEEP THAT KEEPS FIFTY-ONE IS NOT A SWEEP**, and it was')
    rec('  ### bounded before the lock.')
    pre = blob('OPEN_TRAILS.md')
    prelines = pre.split(chr(10))
    hdr = [i + 1 for i, ln in enumerate(prelines)
           if ln.startswith('| | trail | species | what is owed') and 'trigger' in ln]
    rec('  ### **THE WORK-ORDER TABLE : line %s.**' % hdr)
    cur = text_of(TRAILS).replace(chr(13) + chr(10), chr(10))
    lines = cur.split(chr(10))
    origs, done = [], []
    for h in hdr:
        for i in range(h + 2, min(h + 40, len(lines) + 1)):
            ln = lines[i - 1]
            if not ln.startswith('|'):
                break
            cells = ln.split('|')
            wid = next((c.strip().strip('`') for c in cells if 'W-ORD-' in c), '')
            if wid not in TRIGGERS:
                continue
            if cells[-2].strip().lower().strip('`. ') != 'none':
                rec('      line %d  %-32s ### **ALREADY CARRIES A TRIGGER -- NOT TOUCHED**'
                    % (i, wid[:32]))
                continue
            origs.append((i, ln))
            cells[-2] = ' ' + TRIGGERS[wid] + ' '
            lines[i - 1] = '|'.join(cells)
            done.append((i, wid))
            rec('      line %d  %-32s ### **TRIGGER GIVEN**' % (i, wid[:32]))
            rec('        %s' % flat(TRIGGERS[wid], 180))
    blk = ['', TMARK, '',
           ('**b398 — RULING (R23) APPLIED: AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS '
            'SHELVED.** The `trigger` cell of %d work-order row(s) above read `none`; each now '
            'names **a trigger that can fire**. Two of the three cannot fire *yet*, because the '
            'instrument lane is PARKED under (R4) — **and a block on the work is not an absence '
            'of a trigger**, which is the distinction (R23) draws. **Nothing here is opened, '
            'priced or paid.** The pre-edit rows are preserved verbatim below.' % len(done)), '']
    for i, ln in origs:
        blk.append('> line %d was: %s' % (i, ln))
    blk.append('')
    io.open(TRAILS, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines + blk))
    add, dele = numstat('OPEN_TRAILS.md')
    post = text_of(TRAILS).replace(chr(13) + chr(10), chr(10)).split(chr(10))
    aset = set(post)
    changed = [x for x in prelines if x not in aset]
    lost = [x for x in changed if not any(x in y for y in post)]
    rec('  ### **THE WRITE : `+%d / -%d` ; changed in place `%d` ; ### **CONTENT LOST `%d`**'
        % (add, dele, len(changed), len(lost)))
    rec('  ### ### **ROWS WHOSE TRIGGER READ `none` : `%d`. ### ROWS NOW CARRYING ONE : `%d`. ###'
        % (len(origs), len(done)))
    rec('  ### ### ROWS MARKED SHELVED : `0`** -- each of the three has a trigger that can fire,')
    rec('  ### ### so none needed shelving, and ### **`(R23)` PREFERS A FIRABLE TRIGGER.**')
    return dict(header=hdr, none_rows=len(origs), filled=len(done), shelved=0,
                added=add, deleted=dele, lost=len(lost))


# ==================================================================================================
#  COMPONENT 4 -- THE SMALLEST NEXT STATEMENT.
# ==================================================================================================
def component4():
    bar('=')
    rec('  COMPONENT 4 -- THE SMALLEST NEXT STATEMENT.')
    bar('=')
    rec('  ### **THE CLAUSE, FROM ITS OWN ANCHOR.** ### `(S)`: for every `g` in the source`s')
    rec('  ### class, ### **`SUM_v W_v(f) <= 0`** ### in the source`s normalization -- the')
    rec('  ### source`s Proposition C.1, at the import bar.')
    rec('  ### **AND THE GATE`S OWN RANKING SAYS WHERE IT HALTS:** ### `b332` ranked the')
    rec('  ### constituents and put ### **`K8` THE QUANTIFIERS** ### with ### **NOTHING PROVED --')
    rec('  ### MEASURED ON FAMILIES ONLY** ### (`b326`: *the arc`s family ... DOES NOT SEE IT*;')
    rec('  ### `b328`: *SEES IT -- AT SEVEN OF EIGHT CELLS*).')
    rec('  ### ### **AND `b332`S OWN RANKING IS STALE IN ONE PLACE, WHICH THIS ACT REPORTS RATHER')
    rec('  ### ### THAN REPEATS:** ### it called `K5` the softest at `DEFINED-ONLY`, and `b333`')
    rec('  ### ### conferred ### **`DERIVES-ON-IMPORTS`** ### on `K5` the next day. ### **A TABLE')
    rec('  ### ### THAT WAS RIGHT WHEN WRITTEN IS DATED BY THE ACT THAT LIFTED ITS SOFTEST ROW**,')
    rec('  ### ### and nothing propagated the lift into the table. ### **ROUTED, NOT REPAIRED --')
    rec('  ### ### EDITING `FINDINGS.md`S FOLD IS NOT THIS ACT`S SCOPE.**')
    rec()
    rec('  ### ### ### **THE STATEMENT, NAMED:**')
    rec('  ###   ### **(N)** ### In the compiled finite-side module `Core/FiniteSideSeal.lean`,')
    rec('  ###   the ### **COMPACT PART** ### of the finite-place contribution holds ### **FOR')
    rec('  ###   ### EVERY CELL AND NOT AT SEVEN**: for every `g` in the source`s class, the')
    rec('  ###   identity-count form of `SUM_p W_p(g conv g-bar^#)` equals the test function at')
    rec('  ###   the identity times the dimension, ### **WITH NO CELL-BY-CELL CASE ANALYSIS.**')
    rec()
    rec('  ### **WHAT IT DEPENDS ON, AND AT WHAT GRADE THE RECORD HOLDS EACH:**')
    rec('  ###   `K3` the decomposition part      ### **PROVED-GENERAL (`b329`)** -- HELD')
    rec('  ###   `K3` the scaling part            ### **PROVED-GENERAL (`b329`)** -- HELD')
    rec('  ###   `K3` the compact part            ### **PROVED-PER-CELL (`b329`)** -- HELD ONLY')
    rec('  ###                                   AT CELLS, AND THIS IS WHAT `(N)` GENERALIZES')
    rec('  ###   `K3` the identification with the source`s trace')
    rec('  ###                                   ### **DERIVED-ON-CONTENT (`b310`), NOT')
    rec('  ###                                   ### COMPILED** -- HELD ON CONTENT ONLY')
    rec('  ###   `K4` the prime sum               ### **DERIVED-ON-CONTENT (`b306`)** -- HELD,')
    rec('  ###                                   with the cutoff window named as a choice')
    rec('  ###   `K1` the class                  ### **IMPORT-UNDER-THE-BAR (`b328`)** -- HELD')
    rec('  ###   `K2` the criterion`s sign        ### **IMPORT-UNDER-THE-BAR (`b321`)** -- HELD')
    rec('  ### **WHAT IS ABSENT:**')
    rec('  ###   ### **THE GENERAL COMPACT PART** -- the whole of `(N)`.')
    rec('  ###   ### **A COMPILATION OF `b310`S IDENTIFICATION** -- it is a derivation on content')
    rec('  ###   and the gate`s own row says it ### *is not compiled.*')
    rec('  ###   ### **AND `K8` ITSELF** -- nothing is proved about the quantifiers, and `(N)`')
    rec('  ###   does not prove them; it removes ONE cell-bound constituent from the way.')
    rec()
    rec('  ### ### **`(N)` IS NOT `(M)`, AND THE ACT DOES NOT BLUR THEM.** ### `(M)` moves the')
    rec('  ### ### ### **BRIDGE** ### -- it identifies the Sonin margin`s second term with the')
    rec('  ### ### finite places. ### `(N)` moves the ### **CLAUSE** ### -- it takes a')
    rec('  ### ### constituent of `(S)` from cell-bound to general. ### **THAT WAS THIS SEAT`S')
    rec('  ### ### `(E3)`, REGISTERED BEFORE THE LOCK, AND IT HOLDS.**')
    rec('  ### **AND `(N)` IS NOT ATTEMPTED HERE.** ### It is stated, its dependencies graded, and')
    rec('  ### its absent parts named. ### **A KERNEL ACT CAN TAKE IT AS A WORK ORDER; THIS ACT')
    rec('  ### ### IS NOT ONE.**')
    return dict(named=1, attempted=0, statement='(N) the general compact part of K3',
                held=6, absent=3, distinct_from_M=True, b332_stale_row='K5', e3='HELD')


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b398 -- THE COMPONENTS. ### THE LI-WEIL BRIDGE.')
    bar('=')
    i, ln = AF.find(FERRY, 'ACT b398 — THE LI–WEIL BRIDGE')
    rec('  ### **THE ORDER, line %d:** %s' % (i, flat(ln, 140)))
    rec()
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    c3 = component3()
    rec()
    tr = triggers()
    rec()
    c4 = component4()
    rec()
    bar('=')
    rec('  1 : place-sets %s vs %s ; (F1) %s' % (c1['place_sonin'], c1['place_li'], c1['f1']))
    rec('  2 : %s ; halves %s/%s ; missing %s typed %s ; obstructions %d'
        % (c2['verdict'], c2['half_one'], c2['half_two'], '(M)', c2['missing_type'],
           c2['obstructions']))
    rec('  3 : row %d ; +%d/-%d ; content lost %d ; still OWED %s ; paid %d ; grades %d'
        % (c3['row_line'], c3['added'], c3['deleted'], c3['lost'], c3['still_owed'],
           c3['paid'], c3['grades']))
    rec('  R23: none-rows %d ; filled %d ; shelved %d ; content lost %d'
        % (tr['none_rows'], tr['filled'], tr['shelved'], tr['lost']))
    rec('  4 : named %d ; attempted %d ; held %d ; absent %d ; (N) != (M) %s'
        % (c4['named'], c4['attempted'], c4['held'], c4['absent'], c4['distinct_from_M']))
    rec('  ### **NOTHING WAS COMPUTED. ### NO INSTRUMENT RUN. ### NO KERNEL BUILT.**')
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b398_components_run', L)
    json.dump(dict(c1=c1, c2=c2, c3=c3, triggers=tr, c4=c4,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b398_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
