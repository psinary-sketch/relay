# -*- coding: utf-8 -*-
"""b409_desk_bank.py -- THE DECLARATIONS, THE RELATIVIZED LEMMA, THE FREEZE, THE ROW, THE KEY.

### ### **THIS ACT WRITES ONE LINE INTO EACH OF THE DOCUMENTS WHOSE SCHEME IT COULD READ**, and
### ### **NOT ONE INTO A DOCUMENT IT COULD NOT.** ### `(R25)` disposition (B): declare, never
### renumber, and ROUTE what cannot be read rather than guessing it.
###
### ### **THREE THINGS THIS FILE IS CAREFUL ABOUT, EACH BECAUSE AN ACT WAS BURNED BY IT.**
### ### (1) ### **EVERY WRITE ENCODES BEFORE IT OPENS** (b405's zero-byte husk).
### ### (2) ### **THE BYTE-ORDER MARK IS PRESERVED** -- two of the declarable documents carry one,
### ###     and this act's own first head test read them as headless.
### ### (3) ### **THE HEAD NOTE NAMES NO CLASS SYMBOL.** ### A note listing the classes would pin
### ###     the document's scheme by its own text, and the matcher would then be reading this
### ###     act's sentence back to itself. ### **A DECLARATION MUST NOT BE ITS OWN EVIDENCE.**
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
import class_scheme               # noqa: E402
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b409 the obstacles dissolved where the record allows -->'
PRIOR = '<!-- b408 the other two channels, the reduction as a classified proof priced -->'
BANKOUT = os.path.join(D, 'b409_the_obstacles_dissolved.txt')
BOM = '﻿'
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def write_bytes(path, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.** ### b405's husk is why this exists."""
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


SEALTXT = io.open(os.path.join(D, 'b409_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b409_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b409_components.txt'), encoding='utf-8').read()
GR, GD_ = LG['gates_read'], LG['face_subject_gates']


def table_rows():
    """### The declaration list, READ FROM THE FILE THE COMPONENTS EMITTED, never recomputed."""
    out = []
    for ln in io.open(os.path.join(D, 'b409_scheme_table.txt'), encoding='utf-8'):
        if not ln.strip():
            continue
        rel, sch, head, uses = ln.rstrip(NL).split('\t')
        out.append(dict(rel=rel, sch=sch, head=(head == 'True'), uses=int(uses)))
    return out


# ### =================================================================================================
# ### KIND 10 -- THE DECLARATIONS.
# ### =================================================================================================
NOTE = ('*CLASS-NUMBERING SCHEME: %s.* Declared b409 under `(R25)`, read from this document’s '
        'own text (%d of its class symbols pin %s, %d pin the other); the corpus keeps **two** '
        'numberings and this note says which one this document uses. **No symbol in this document '
        'was renumbered, and nothing above this line was altered.**')


def note_for(src, sch):
    st, ex, _ev = class_scheme.pin(src)
    a, b = (st, ex) if sch == 'STAGE' else (ex, st)
    return NOTE % (sch, a, sch, b)


def do_declarations():
    rows = [r for r in table_rows() if r['sch'] in ('STAGE', 'EXCLUSION-ORDER') and r['head']]
    routed = [r for r in table_rows() if not (r['sch'] in ('STAGE', 'EXCLUSION-ORDER')
                                              and r['head'])]
    rec('  ### ### **DECLARABLE : %d. ### ROUTED, NOT GUESSED : %d.**' % (len(rows), len(routed)))
    rec('  ### **AND THE NOTE NAMES NO CLASS SYMBOL**, so it cannot pin the document it declares.')
    rec('')
    ok = True
    written = already = 0
    for r in rows:
        p = os.path.join(PP, r['rel'].replace('/', os.sep))
        before = io.open(p, encoding='utf-8', newline='').read()
        if class_scheme.DECL.search(before):
            already += 1
            rec('      %-52s ALREADY DECLARED -- nothing written.' % r['rel'][:52])
            continue
        body = before[len(BOM):] if before.startswith(BOM) else before
        lines = body.split(NL)
        h = [i for i, ln in enumerate(lines) if re.match(r'^#\s+\S', ln)]
        if not h:
            ok = False
            rec('      %-52s ### HARD FAILURE -- no `# ` head after the mark.' % r['rel'][:52])
            continue
        i = h[0]
        note = note_for(before, r['sch'])
        # ### **AFTER THE HEAD AND ITS BLANK LINE**, so the original head keeps its own paragraph.
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        lines[j:j] = [note, '']
        after = (BOM if before.startswith(BOM) else '') + NL.join(lines)
        write_bytes(p, after)
        back = io.open(p, encoding='utf-8', newline='').read()
        bl, al = before.split(NL), back.split(NL)
        # ### **THE FIVE THINGS THAT MUST BE TRUE OF EVERY ONE OF THESE WRITES**, checked here
        # ### and not assumed: everything ABOVE the note is byte-identical, everything BELOW it
        # ### is byte-identical, exactly two lines appear, the mark survives, and the matcher
        # ### reads back the scheme the note claims.
        head_kept = al[:j] == bl[:j]
        two_lines = len(al) == len(bl) + 2
        bom_kept = back.startswith(BOM) == before.startswith(BOM)
        reads = class_scheme.declared_scheme(back) == r['sch']
        tail_kept = al[j + 2:] == bl[j:]
        good = head_kept and two_lines and bom_kept and reads and tail_kept
        ok = ok and good
        written += 1
        rec('      %-52s %-16s +2 lines %-5s above kept %-5s mark kept %-5s below kept %-5s '
            'reads back %-5s %s'
            % (r['rel'][:52], r['sch'], two_lines, head_kept, bom_kept, tail_kept, reads,
               'PASS' if good else '### FAIL ###'))
    rec('')
    rec('  ### ### **DOCUMENTS DECLARED : %d ### ; ALREADY CARRYING A DECLARATION : %d ###'
        % (written, already))
    rec('  ### ### ; SYMBOLS RENUMBERED : `0`.**')
    rec('  ### **THE ROUTED, NAMED AND NOT GUESSED (%d):**' % len(routed))
    for r in routed[:8]:
        rec('      %-58s %s' % (r['rel'][:58], r['sch']))
    if len(routed) > 8:
        rec('      ... and %d more, every one listed in `data/b409_scheme_table.txt`.'
            % (len(routed) - 8))
    if written + already:
        subprocess.run(['git', '-C', PP, 'add', '--'] + [r['rel'] for r in rows],
                       capture_output=True)
    return ok, written, already, len(routed)


# ### =================================================================================================
# ### KIND 11 -- THE RELATIVIZED LEMMA.
# ### =================================================================================================
IBMARK = '<!-- b409 the lemma relativized for a conditional conclusion -->'
IBSEC = [
    '',
    IBMARK,
    '',
    '## 10. The lemma relativized: a proof of a conditional',
    '',
    '**Why this section exists.** Theorem 3.1 is stated about a proof of the universal statement '
    '`∀x ∈ M: P(x)`. A reduction that imports premises it has not derived does not prove that '
    'statement; it proves `H ⟹ ∀x ∈ M: P(x)` for a finite set of hypotheses `H`. **A proof of a '
    'conditional is not a proof of its consequent, so Theorem 3.1 as written does not quantify '
    'over it** — which is why the question is asked here rather than assumed away.',
    '',
    '**Theorem 3.1-H (relativized form).** *Let `M` be a determined structure with specification '
    '`S`, let `I` be an interface with `κ(P, I) = 0` for target parameter `P`, and let `H` be a '
    'finite set of `ℒ`-sentences **every member of which factors through `I` for `P`** in the '
    'sense of Definition 2.5. Let `π` be a formal first-order proof in `ZFC ∪ S` of `H ⟹ (∀x ∈ M: '
    'P(x))`. If `π` factors through `I` for `P`, then `π` does not establish that statement; the '
    'strongest statement `π` can establish has the form `H ⟹` (`P` holds on a density-one subset '
    'of each `I`-class), and the individual element remains unreached.*',
    '',
    '**The proof is the original’s, movement by movement, and only the first movement '
    'changes.** Lemma 3.2 and Corollary 3.3 run by induction over `π`’s inference steps: a '
    'step whose conclusion is `I`-factored cannot discriminate within a `~_{I,P}`-class. Adding '
    '`H` adds **premises**, and a step invoking a premise that references an individual-element '
    'specification across `I` **does not factor** — so the theorem’s own hypothesis fails at '
    'that step. **Hence the extra condition on `H`, and it is stated in the theorem rather than '
    'discovered in the proof.** Lemma 3.4 survives unchanged: a conclusion `H ⟹ ∀x P(x)` still has '
    'a truth value at each `x` that depends on `x`, so Corollary 3.3 applies to it verbatim and '
    'the bound becomes the relativized one; nothing in that argument mentions the shape of the '
    'conclusion. Proposition 3.5 survives unchanged and for a reason worth stating: it is a '
    '**general non-entailment**, exhibiting one determined system where density-one holds and '
    'universality fails, and so needs no witness satisfying `H` at all.',
    '',
    '**What this costs, said plainly.** The relativized form needs **one hypothesis the original '
    'did not**: that every sentence of `H` itself factors through `I` for `P`. Without it the '
    'theorem is false as stated, since a single non-factoring premise breaks the induction. **A '
    'restatement that quietly costs more than the original is not the original relativized**, so '
    'the cost is on the face of the statement.',
    '',
    '**And what it does not settle.** Applying 3.1-H to the corpus’s reduction — with `H` = '
    '{ the source’s Definition 3.1, Proposition C.1, the local term (149), Theorem 4.7 } — '
    'requires classifying **those four sentences** under Definition 2.5, and **nobody has run that '
    'classification**. So the relativization succeeds and hands the corpus a new unasked question '
    'in place of the old one. **A theorem that applies *provided a condition* is not a theorem '
    'that applies.**',
    '',
    '**Grade.** `UNCOMPILED`. The original’s semantic core is compiled and axiom-free at '
    '`SieveCeilingSemantic.sieve_ceiling_semantic`; **that terminal covers the original and not '
    'this restatement**, nothing was compiled for this section, and **no new grade is minted for '
    'it.** Filed b409.',
]


def do_keystone():
    before = io.open(IB, encoding='utf-8', newline='').read()
    if IBMARK in before:
        rec('  ### ALREADY FILED -- the b409 section is present. ### NOTHING APPENDED.')
        return True, len(IBSEC)
    io.open(IB, 'a', encoding='utf-8', newline=NL).write(NL.join(IBSEC) + NL)
    after = io.open(IB, encoding='utf-8', newline='').read()
    ao = after.startswith(before)
    seg = after.split(IBMARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'the conditional is the subject': 'a proof of a conditional is not a proof of its '
                                          'consequent' in low,
        'the extra hypothesis is stated': 'every member of which factors through `i` for `p`' in low,
        'the cost is on the face': 'one hypothesis the original did not' in low,
        'movement 3 needs no witness': 'needs no witness satisfying `h` at all' in low,
        'the four imports are named': 'proposition c.1, the local term (149), theorem 4.7' in low,
        'the classification is unrun': 'nobody has run that classification' in low,
        'the grade is not borrowed': 'covers the original and not this restatement' in low,
        'no new grade': 'no new grade is minted for it' in low,
    }
    rec('  ### bytes %d -> %d ; append-only %s'
        % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
    for k, v in says.items():
        rec('      %-34s %s' % (k, v))
    ok = ao and all(says.values())
    if ok:
        subprocess.run(['git', '-C', PP, 'add', '--',
                        'phase1.5/method/INVARIANCE_BARRIERS.md'], capture_output=True)
    return ok, len(IBSEC)


# ### =================================================================================================
# ### KIND 12 -- THE FREEZE MARK, INSIDE AN EXISTING CELL, WITH NO ENTRY ADDED.
# ### =================================================================================================
CELL6_ADD = (
    " ### ### **THE REGISTER IS FROZEN AT SIX, b409.** ### No entry is taken from this act and "
    "### **NO SEVENTH SITE IS ENTERED.** ### The reason is the row's own count and not a judgement "
    "about its worth: across six entries it has recorded `6` sites, `2` coordinates, `1` price "
    "corrected, `0` bridges typed, `0` grades conferred and ### **`0` STATEMENTS ABOUT THE "
    "OBJECT**. ### ### **A FREEZE IS NOT A CLOSURE, NOT A RETIREMENT AND NOT A GRADE.** ### The "
    "row stays OPEN, its refusal above stands verbatim and unedited, every cell keeps its text, "
    "and the register may be reopened by the act that meets the condition. ### **THE CONDITION IS "
    "PRINTED HERE SO A LATER ACT CAN SEE WHEN IT IS SATISFIED: A SITE WHOSE ENTRY PRODUCES A "
    "STATEMENT ABOUT THE OBJECT** -- about `ξ`, about the Epstein object, or about any zero -- "
    "**RATHER THAN A STATEMENT ABOUT THE RECORD.** ### None of the six has. ### And the freeze is "
    "recorded INSIDE this cell rather than as a new column, because ### **THE ROW CANNOT GAIN A "
    "COLUMN ALONE** -- the same law b405 obeyed when it added the two coordinates.")


def column_shape(text):
    return [ln.rstrip().count('|') for ln in text.split(NL) if ln.startswith('|')]


def do_faces():
    before = io.open(FACES, encoding='utf-8', newline='').read()
    shape_before = column_shape(before)
    lines = before.split(NL)
    idx = [i for i, ln in enumerate(lines) if ln.startswith('| U1 |')]
    if len(idx) != 1:
        rec('  ### HARD FAILURE -- expected exactly one `U1` row, found %d.' % len(idx))
        return False
    i = idx[0]
    if '(b409' in lines[i] or 'FROZEN AT SIX, b409' in lines[i]:
        rec('  ### ALREADY FILED -- the b409 freeze mark is present. ### NOTHING APPENDED.')
        return True
    oldc = GD.split_cells(lines[i])
    if len(oldc) != 7 or GD.raw_pipes(CELL6_ADD):
        rec('  ### HARD FAILURE -- %d cells, or an unescaped pipe in the mark.' % len(oldc))
        return False
    newc = list(oldc)
    newc[6] = oldc[6].rstrip() + CELL6_ADD + ' '
    lines[i] = '|' + '|'.join(newc) + '|'
    write_bytes(FACES, NL.join(lines))
    back = io.open(FACES, encoding='utf-8', newline='').read()
    bl, al = before.split(NL), back.split(NL)
    untouched = sum(1 for a, b in zip(bl, al) if a == b)
    ok = (len(bl) == len(al)) and untouched == len(bl) - 1
    rec('  ### lines %d -> %d ; UNCHANGED %d of %d' % (len(bl), len(al), untouched, len(bl)))
    same_shape = (shape_before == column_shape(back))
    rec('  ### ### **TABLE LINES %d ; COLUMN COUNTS UNCHANGED ON EVERY ONE : %s**'
        % (len(column_shape(back)), same_shape))
    ok = ok and same_shape
    backc = GD.split_cells(al[i])
    ok = ok and len(backc) == 7
    for k in range(7):
        if k == 6:
            good = backc[k].startswith(oldc[k].rstrip()) and len(backc[k]) > len(oldc[k])
            rec('      cell %d  APPENDED TO : prior text a TRUE PREFIX : %-5s   %d -> %d bytes'
                % (k, good, len(oldc[k].encode('utf-8')), len(backc[k].encode('utf-8'))))
        else:
            good = backc[k] == oldc[k]
            rec('      cell %d  UNTOUCHED   : BYTE-IDENTICAL : %s' % (k, good))
        ok = ok and good
    for lbl, cond in (
            ('the row still reads `U1`', al[i].startswith('| U1 |')),
            ('the freeze is at six', 'THE REGISTER IS FROZEN AT SIX' in al[i]),
            ('no seventh site', 'NO SEVENTH SITE IS ENTERED' in al[i]),
            ('a freeze is not a closure', 'A FREEZE IS NOT A CLOSURE' in al[i]),
            ('the row stays open', 'The row stays OPEN' in al[i]),
            ('the condition is printed', 'A SITE WHOSE ENTRY PRODUCES A STATEMENT ABOUT THE '
                                         'OBJECT' in al[i]),
            ('zero statements about the object', '`0` STATEMENTS ABOUT THE OBJECT' in al[i]),
            ('the column law is obeyed', 'THE ROW CANNOT GAIN A COLUMN ALONE' in al[i]),
            ('the b405 coordinates are still there',
             'THE ROW GAINS TWO COORDINATES' in al[i]),
            ('the refusal is still there', 'types no bridge between' in al[i])):
        ok = ok and cond
        rec('      %-42s : %s' % (lbl, cond))
    if ok:
        subprocess.run(['git', '-C', PP, 'add', '--', 'FACES_LEDGER.md'], capture_output=True)
    return ok


# ### =================================================================================================
# ### THE DESK.
# ### =================================================================================================
DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('W-ORD-E0-RANK-PROPAGATION', 'STANDING', 'No grade moves in this act.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('the keystone’s widened no-Mathlib claim; SIDE-effects’ absent printed profile',
     'STANDING', 'ROUTED at b404. ### Nothing is built here.'),
    ('the row’s restatement into residue form', 'STANDING',
     'ROUTED at b404, MEASURED at b405, and still not applied.'),
    ('the two class numberings', 'CLOSE',
     'RULED BY (R25) AND EXECUTED. ### Both kept, 29 documents declared, **0 SYMBOLS '
     'RENUMBERED**, 66 ROUTED. ### And a correction b408 could not have made: **the '
     'correspondence table misnames the second scheme as the monograph’s**, and two independent '
     'witnesses say the monograph uses the other one.'),
    ('whether the global class has been examined', 'CLOSE',
     'ABSENT UNDER BOTH SCHEMES, with a positive control that PASSED and found a whole section '
     'the corpus had never cited. ### And the reading: **DARK ON THE PLACEMENT REGISTER**, by the '
     'monograph’s own antisymmetry sentence.'),
    ('the lemma for a conditional conclusion', 'CLOSE',
     'RELATIVIZES, and written. ### Theorem 3.1-H is appended beside the original, **UNCOMPILED**, '
     'costing one hypothesis the original did not need.'),
    ('the mathematics-facing gate arms', 'CLOSE',
     'THREE PROPOSED, **0 WRITTEN** -- and not one can be written without a ruling the author has '
     'not made. ### That is the finding, not the excuse.'),
    ('row U1', 'CLOSE',
     'FROZEN AT SIX, with the reopening condition printed inside the cell. ### **0 ENTRIES ADDED, '
     '0 COORDINATES, 0 GRADES.** ### A freeze is not a closure.'),
    ('the routed prices', 'STANDING',
     'b408 listed 2 ROUTED and 1 NAMED. ### b409 discharges none and adds two: the naming of '
     'b408’s one statement, and now the Definition-2.5 classification of the four imports.'),
    ('the fold', 'STANDING', 'NOT DUE. ### The span is 7 against (R1)’s threshold of 9.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT. ### No claim in either direction.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1200), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


# ### =================================================================================================
# ### THE TRAIL BLOCK.
# ### =================================================================================================
def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b409 — the obstacles dissolved where the record allows — filed 2026-09-10',
        '',
        '**`(R25)` is executed: both numberings are kept, twenty-nine documents now declare which '
        'one they use, and no symbol anywhere was renumbered.** The sweep found `95` live '
        'documents carrying `1506` class-symbol uses, with `8` deposited documents and their `516` '
        'uses left untouched. **Only `29` of the `95` can be assigned a scheme from their own '
        'text; `66` are marked SCHEME UNDECLARED and ROUTED, not guessed** — so the expectation '
        'that a majority would be readable is **refuted**, and its stated reason is refuted too: '
        'the documents do not cite the monograph’s table, exactly one document carries that '
        'table, and the monograph contradicts it. **Disposition (A) was priced before (B) was '
        'executed: it would have rewritten `1506` symbol uses across `95` documents, of which the '
        '`382` in exclusion-order documents change meaning, and `outputs/` cannot be edited at '
        'all — so the deposited copies would have been left disagreeing with the live ones, a '
        'worse hazard than the one being cured.** Disposition (B) cost `29` lines and moved `0` '
        'symbols.',
        '',
        '**And b408’s finding is confirmed while b408’s label is corrected — without '
        'editing b408.** There are two numberings and they do disagree on six of seven symbols. '
        'But the second is **not the monograph’s**: the monograph’s own class table '
        'gives *C₄ (Modular/PSL₂)*, and `ENUMERA.md` independently reconciles *the '
        'monograph’s canonical index is C₁ Schwarz · C₂ Euler · C₃ functional-equation · C₄ '
        'modular/PSL₂ · C₅ spectral · C₆ Cauchy–Riemann · C₇ Hadamard*. **The correspondence '
        'table describes a live scheme correctly and misnames whose it is** — and the scheme is '
        'live, in `9` documents. **One document uses both in its own text**: '
        '`PATHS_TO_THE_CRITICAL_LINE.md` pins one scheme on the balance of its symbols and its '
        'fifth-path line uses the other, which is precisely the line b408 met. **This act’s '
        'own two instruments also disagreed, and both numbers are printed rather than one:** the '
        'survey called `28` documents readable and the matcher calls `29` decidable, a difference '
        'of one that conceals a symmetric difference of five, because the survey’s predicate '
        'was *matches the canonical index* rather than *decides between the two* — it scores a '
        'document that uses the other scheme consistently at zero, and scores a document whose '
        'only pinned symbol is the one both schemes share at one. **The survey’s line is not '
        'edited and its number is not withdrawn; the matcher governs and the defective predicate '
        'is named.** **And two of the declarable documents begin with a byte-order mark, which '
        'this act’s first head test read as headless and would have routed unread** — a '
        'document is not headless because an invisible character stands in front of its head.',
        '',
        '**The modular relation has never been examined as a channel, under either numbering — '
        'and the search that says so carries a positive control that passed and found something a '
        'symbol search could not have found.** Four hits by description and two by symbol across '
        '`4746` files, every one hand-read, and not one is an examination. **The control located '
        '`INVARIANCE_BARRIERS.md` §9, *The calibration family: the archimedean instance and the '
        'per-place table*, a section this record had never cited**, whose archimedean row reads '
        '*the archimedean interface carries κ > 0 for the density register and κ = 0 for the '
        'placement register*. **The corpus grades κ by register and has a calibrated row for one '
        'interface** — and b408 could not have reached it, because that section names its '
        'interfaces by description and never by symbol. **The family’s rows are places. The '
        'modular symmetry is not a place, so it has no row, and the family’s own stated next '
        'moves are further per-place instance rows, which would not reach it.**',
        '',
        '**The reading, on the monograph’s own definition: DARK ON THE PLACEMENT REGISTER, '
        'for the functional equation’s own reason.** The monograph states of *each* mechanism '
        'class that *the constraint function of each mechanism class is antisymmetric about the '
        'reflection axis (the functional equation forces this). An antisymmetric continuous '
        'function has exactly one zero on the axis.* An antisymmetric constraint locates the '
        '**axis**, not a point on it; so the modular relation, like the functional equation, '
        'preserves the critical line and distinguishes no individual zero on it. **And what this '
        'verdict is not, said in the same breath as the verdict: it is a reading of the '
        'record’s own two sentences, not a measured κ under Definition 2.4’s supremum. '
        'The calibration family has no row for the modular relation, so no certificate exists, and '
        'this act writes none.** A consequence is **named and not drawn**: if every class’s '
        'constraint is antisymmetric and the channels are the mechanism classes with no fourth, '
        'then Corollary 3.6’s bright channel is not among the three as the record reads them '
        '— **that follows from two sentences read together and it is not established here.** `0` '
        'routes proposed, priced or opened.',
        '',
        '**Theorem 3.1 relativizes to a proof of a conditional, and the relativized form is '
        'written into the barrier keystone as §10 — UNCOMPILED.** Lemma 3.4 and Proposition 3.5 '
        'survive unchanged; Proposition 3.5 needs no witness satisfying `H` at all, because it is '
        'a general non-entailment. **Only the induction changes, and it costs one hypothesis the '
        'original did not need: every sentence of `H` must itself factor through `I` for `P`.** '
        'Without it a step invoking a premise that references an individual-element specification '
        'across `I` does not factor, and the theorem’s own hypothesis fails at that step. '
        '**A restatement that quietly costs more than the original is not the original '
        'relativized, so the cost is on the face of the statement.** **And the restatement takes '
        'no new grade.** The original’s semantic core is compiled and axiom-free at '
        '`SieveCeilingSemantic.sieve_ceiling_semantic`; that terminal covers the original and not '
        'this section, nothing was compiled here, and borrowing a compiled grade for prose is the '
        'one thing this apparatus exists to prevent. **The relativization succeeds and hands the '
        'corpus a new unasked question in place of the old one:** applying it to the corpus’s '
        'reduction turns on whether the source’s Definition 3.1, Proposition C.1, the local '
        'term (149) and Theorem 4.7 each factor through the product-formula interface — **a '
        'Definition 2.5 classification of four sentences that nobody has run.** A theorem that '
        'applies *provided a condition* is not a theorem that applies.',
        '',
        '**Three mathematics-facing gate arms are proposed and `0` are written, and the reason is '
        'the finding.** `G-VACUOUS-POPULATION` would have caught b399’s vacuous pass; '
        '`G-PREMISE-BEFORE-CONCLUSION` would have caught b404’s false premise; '
        '`G-KIND-BEFORE-APPLICATION` would have caught b405, b406 and b407. **Not one can be '
        'written without a decision the author has not made** — what counts as the population, '
        'what a refuted premise with a surviving conclusion scores, and what the one statement is '
        'called, which b408 routed and is still routed. **An arm cannot enforce a law the record '
        'has not named.** That is why there are eight standing apparatus arms and none of these.',
        '',
        '**Row `U1` is frozen as a register complete at six, and the freeze is written inside an '
        'existing cell with no entry added and no column gained.** Across six entries it has '
        'recorded `6` sites, `2` coordinates, `1` price corrected, `0` bridges typed, `0` grades '
        'conferred and **`0` statements about the object**. **A freeze is not a closure, not a '
        'retirement and not a grade**: the row stays OPEN, its refusal stands verbatim and '
        'unedited, and the reopening condition is printed inside the cell so a later act can see '
        'when it is met — **a site whose entry produces a statement about the object rather than '
        'about the record.**',
        '',
        '**Nothing deposits.** `0` symbols renumbered, `0` schemes guessed, `0` entries added to '
        '`U1`, `0` coordinates, `0` grades moved or minted, `0` routes opened, `0` bridges typed, '
        '`0` rules struck or amended, `0` folds run, `0` in-place repairs, `0` locked faces '
        'edited, `0` prior banks edited, `0` kernels built, `0` `.lean` files touched, `0` content '
        'lost. Both lanes stay parked and the wave stays parked. Registration '
        '`data/b409_registration_2026-09-10.txt`, LOCKED before any write at sha256 `%s`, chained '
        'on `tools/b378_lockgate.py` run as b409 — %d gates read, %d checked by digest. Bank: '
        '`relay/data/b409_the_obstacles_dissolved.txt`. **h2 where the deposit left it.**'
        % (SEALHASH, GR, GD_),
    ]


SCOPE = ("### THIS ROW RECORDS A RULING EXECUTED, A SEARCH THAT RETURNED ABSENT WITH A PASSING "
         "CONTROL, A READING, A RESTATED THEOREM AND A FREEZE. ### IT RENUMBERS NO SYMBOL, GUESSES "
         "NO SCHEME, CERTIFIES NO KAPPA, OPENS NO CHANNEL, MOVES NO GRADE, MINTS NO GRADE, TYPES "
         "NO BRIDGE AND ADDS NO ENTRY TO ANY ROW")


def corr_rows(Q):
    m = ("**THE CORPUS'S ONE CALIBRATED KAPPA TABLE HAS NO ROW FOR THE MODULAR RELATION, AND ITS "
         "OWN NEXT MOVES WOULD NOT REACH IT -- FOUND BY A POSITIVE CONTROL THAT A SYMBOL SEARCH "
         "COULD NOT HAVE FOUND** (b409, the obstacles dissolved)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b409 -- %d gates read, %d checked by digest. **COMPONENT 1: (R25) EXECUTED IN "
            "DISPOSITION (B) -- 29 documents declared their scheme, 0 SYMBOLS RENUMBERED, 66 "
            "ROUTED AS SCHEME UNDECLARED.** Only 29 of 95 live documents can be assigned a scheme "
            "from their own text, so the expectation of a readable majority is REFUTED and its "
            "stated reason with it. **b408'S CONCLUSION STANDS AND ITS LABEL WAS WRONG: the second "
            "scheme is NOT the monograph's**, on two independent witnesses -- the monograph's own "
            "class table and ENUMERA's reconciliation -- **AND IT IS NEVERTHELESS LIVE, IN 9 "
            "DOCUMENTS.** Disposition (A) was priced first at 1506 symbol uses and left untaken. "
            "**AND THIS ACT'S TWO INSTRUMENTS DISAGREED: 28 against 29, a difference of one "
            "concealing a symmetric difference of five; BOTH ARE PRINTED, THE MATCHER GOVERNS, AND "
            "THE DEFECTIVE PREDICATE IS NAMED.** **COMPONENT 2: THE GLOBAL CLASS IS ABSENT UNDER "
            "BOTH SCHEMES** -- 4 hits by description, 2 by symbol, 4746 files, every hit hand-read "
            "-- **AND THE POSITIVE CONTROL PASSED AND FOUND INVARIANCE_BARRIERS SECTION 9, A "
            "CALIBRATION FAMILY THIS RECORD HAD NEVER CITED, WHICH GRADES KAPPA BY REGISTER AND "
            "HAS A ROW FOR THE ARCHIMEDEAN INTERFACE AND NONE FOR THE MODULAR RELATION.** The "
            "reading is **DARK ON THE PLACEMENT REGISTER**, by the monograph's own antisymmetry "
            "sentence, and is marked A READING AND NOT A MEASURED KAPPA. A consequence for "
            "Corollary 3.6 is NAMED AND NOT DRAWN. **COMPONENT 3: THE LEMMA RELATIVIZES** and "
            "Theorem 3.1-H is written into the keystone as section 10, **UNCOMPILED, COSTING ONE "
            "HYPOTHESIS THE ORIGINAL DID NOT NEED**, and applying it turns on a Definition 2.5 "
            "classification of four imported sentences THAT NOBODY HAS RUN. **COMPONENT 4: 3 "
            "MATHEMATICS-FACING ARMS PROPOSED, 0 WRITTEN -- none can be written without a ruling "
            "the author has not made.** **COMPONENT 5: ROW U1 FROZEN AS A REGISTER COMPLETE AT "
            "SIX**, the mark inside an existing cell, the reopening condition printed, %d ENTRIES "
            "ADDED, %d COORDINATES, %d SYMBOLS RENUMBERED, %d SCHEMES GUESSED, %d ROUTES OPENED, "
            "%d GRADES MINTED, %d CONTENT LOST"
            % (GR, GD_, 0, 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT, NO "
            "`.lean` FILE TOUCHED AND NO AXIOM PROFILE READ OR INFERRED. ### THE COMPILED TERMINAL "
            "NAMED IN SECTION 10 IS NAMED AS COVERING THE ORIGINAL THEOREM AND EXPLICITLY NOT THE "
            "RESTATEMENT. ### WRITING A RESTATED THEOREM IN PROSE CONFERS NO GRADE ON IT")
    prof = ("### NO GRADE MOVED, CONFERRED OR MINTED, NO CLASS SYMBOL RENUMBERED IN ANY DOCUMENT, "
            "NO SCHEME ASSIGNED BY GUESS OR BY PROVENANCE, NO ENTRY ADDED TO ROW U1, NO COORDINATE "
            "ADDED, NO ROW RETIRED OR CLOSED, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO "
            "FERRY_STANDING CLAUSE ADDED, NO IN-PLACE REPAIR MADE, NO LOCKED FACE EDITED, NO PRIOR "
            "ACT'S BANK EDITED, NO BANKED FERRY EDITED, NO REGISTRY ROW EDITED, NO FILE UNDER "
            "outputs/ TOUCHED, NO BRIDGE TYPED, NO ROUTE PROPOSED PRICED OR OPENED. ### THE CORPUS "
            "WRITES ARE 29 ONE-LINE HEAD NOTES, ONE APPENDED KEYSTONE SECTION, ONE APPEND-ONLY "
            "TRAIL BLOCK, ONE FREEZE MARK INSIDE AN EXISTING CELL AND ONE APPENDED CORRESPONDENCE "
            "ROW -- 0 CONTENT LOST")
    grade = ("### A SEARCH THAT RETURNED ABSENT CARRIED A POSITIVE CONTROL, AND THE CONTROL FOUND A "
             "SECTION THE PREDECESSOR'S SYMBOL SEARCH COULD NOT HAVE REACHED. ### A VERDICT WAS "
             "PRINTED WITH WHAT IT IS NOT IN THE SAME BREATH: A READING OF TWO SENTENCES, NOT A "
             "MEASURED KAPPA. ### A CONSEQUENCE THAT FOLLOWS FROM TWO SENTENCES READ TOGETHER WAS "
             "NAMED AND NOT DRAWN. ### A RESTATED THEOREM PRINTED THE HYPOTHESIS IT COSTS ON THE "
             "FACE OF ITS STATEMENT AND REFUSED THE ORIGINAL'S COMPILED GRADE. ### TWO OF THIS "
             "ACT'S OWN INSTRUMENTS DISAGREED AND BOTH YIELDS WERE PRINTED WITH THE DEFECTIVE "
             "PREDICATE NAMED. ### A PREDECESSOR WAS CORRECTED WITHOUT BEING EDITED. ### AND A "
             "HEAD-NOTE FORMAT WAS CHOSEN THAT NAMES NO CLASS SYMBOL, SO THAT A DECLARATION CANNOT "
             "BECOME ITS OWN EVIDENCE")
    status = ("data/b409_the_obstacles_dissolved.txt; data/b409_components.txt; "
              "data/b409_extract.txt; data/b409_scheme_table.txt; "
              "data/b409_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b409); tools/class_scheme.py; "
              "tools/b409_extract.py; tools/b409_regspec.py; tools/b409_reg_gate.py; "
              "tools/b409_components.py; tools/b409_desk_bank.py; tools/b409_checks.py; "
              "PLACE-papers 29 head notes, phase1.5/method/INVARIANCE_BARRIERS.md (section 10), "
              "FACES_LEDGER.md (row U1, one cell appended to, NO ENTRY ADDED) and OPEN_TRAILS.md; "
              "CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


# ### =================================================================================================
# ### THE INDEX KEY.
# ### =================================================================================================
def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('which class numbering does a document use',
           'has the modular relation been examined as a channel',
           'does the corpus grade kappa by register',
           'does the sieve ceiling lemma cover a conditional',
           'why is row U1 frozen',
           'what would a mathematics-facing gate arm require')
MUST_NOT_HIT = ('a symbol was renumbered', 'a scheme was guessed', 'a kappa was certified',
                'a channel was opened', 'a grade was minted')
KEY = 'the-obstacles-dissolved'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    statement = (
        "b409 EXECUTED (R25) AND DISSOLVED THE OBSTACLES THE RECORD ALLOWS. **BOTH NUMBERINGS ARE "
        "KEPT AND 29 DOCUMENTS NOW DECLARE WHICH THEY USE; 0 SYMBOLS WERE RENUMBERED AND 66 "
        "DOCUMENTS ARE MARKED SCHEME UNDECLARED AND ROUTED, NOT GUESSED.** Only 29 of 95 live "
        "documents can be assigned a scheme from their own text. **b408'S CONCLUSION STANDS AND "
        "ITS LABEL WAS WRONG: the second scheme is NOT the monograph's** -- the monograph's own "
        "class table and ENUMERA's reconciliation agree against it -- **BUT IT IS LIVE, IN 9 "
        "DOCUMENTS**, and one document uses both in its own text. Disposition (A) was priced at "
        "1506 symbol uses before (B) was executed at 29 lines. **AND THIS ACT'S OWN TWO "
        "INSTRUMENTS DISAGREED, 28 AGAINST 29 -- A DIFFERENCE OF ONE CONCEALING A SYMMETRIC "
        "DIFFERENCE OF FIVE; BOTH PRINTED, THE MATCHER GOVERNS, THE DEFECTIVE PREDICATE NAMED.** "
        "**THE MODULAR RELATION HAS NEVER BEEN EXAMINED AS A CHANNEL UNDER EITHER NUMBERING: "
        "ABSENT UNDER BOTH SCHEMES**, 4 hits by description and 2 by symbol across 4746 files, "
        "every one hand-read. **AND THE POSITIVE CONTROL PASSED AND FOUND WHAT A SYMBOL SEARCH "
        "COULD NOT: INVARIANCE_BARRIERS SECTION 9, THE CALIBRATION FAMILY, WHICH GRADES KAPPA BY "
        "REGISTER -- the archimedean interface carries kappa > 0 for the density register and "
        "kappa = 0 for the placement register -- AND WHOSE ROWS ARE PLACES, SO THE MODULAR "
        "SYMMETRY HAS NO ROW AND THE FAMILY'S OWN NEXT MOVES WOULD NOT REACH IT.** The reading is "
        "**DARK ON THE PLACEMENT REGISTER**, because the monograph says *the constraint function "
        "of each mechanism class is antisymmetric about the reflection axis (the functional "
        "equation forces this)* -- an antisymmetric constraint locates the AXIS, not a point on "
        "it. **THIS IS A READING OF THE RECORD'S OWN TWO SENTENCES AND NOT A MEASURED KAPPA UNDER "
        "DEFINITION 2.4; NO CERTIFICATE EXISTS AND NONE IS WRITTEN.** A consequence for Corollary "
        "3.6's bright channel is **NAMED AND NOT DRAWN**. **THE SIEVE CEILING LEMMA RELATIVIZES TO "
        "A PROOF OF A CONDITIONAL** and Theorem 3.1-H is written into the keystone as section 10: "
        "Lemma 3.4 and Proposition 3.5 survive unchanged, only the induction changes, and **IT "
        "COSTS ONE HYPOTHESIS THE ORIGINAL DID NOT NEED -- THAT EVERY SENTENCE OF H ITSELF FACTORS "
        "THROUGH I.** **THE RESTATEMENT IS UNCOMPILED AND TAKES NO NEW GRADE**, and applying it "
        "turns on a Definition 2.5 classification of four imported sentences **THAT NOBODY HAS "
        "RUN**. **3 MATHEMATICS-FACING GATE ARMS PROPOSED, 0 WRITTEN** -- none can be written "
        "without a ruling the author has not made, which is the finding and not the excuse. **ROW "
        "U1 IS FROZEN AS A REGISTER COMPLETE AT SIX**, the mark inside an existing cell, 0 entries "
        "added, 0 coordinates, and the reopening condition printed: a site whose entry produces a "
        "statement about the OBJECT. **A FREEZE IS NOT A CLOSURE, NOT A RETIREMENT AND NOT A "
        "GRADE.**")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY "
        "CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO CLASS SYMBOL RENUMBERED, NO SCHEME "
        "GUESSED, NO KAPPA CERTIFIED OR MEASURED, NO CHANNEL OPENED, NO ROUTE PROPOSED PRICED OR "
        "OPENED, NO GRADE MOVED CONFERRED OR MINTED, NO ENTRY ADDED TO ROW U1, NO COORDINATE "
        "ADDED, NO ROW RETIRED OR CLOSED, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO IN-PLACE "
        "REPAIR MADE, NO LOCKED FACE OR PRIOR BANK EDITED. ### THE CORPUS WRITES ARE 29 ONE-LINE "
        "HEAD NOTES, ONE APPENDED KEYSTONE SECTION, ONE APPEND-ONLY TRAIL BLOCK, ONE FREEZE MARK "
        "INSIDE AN EXISTING CELL AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE "
        "PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b409_the_obstacles_dissolved.txt; data/b409_components.txt; data/b409_extract.txt; "
        "data/b409_scheme_table.txt; data/b409_registration_2026-09-10.txt (LOCKED before any "
        "write, chained on tools/b378_lockgate.py run as b409 -- %d gates read, %d checked by "
        "digest); tools/class_scheme.py; tools/b409_components.py; tools/b409_desk_bank.py; "
        "tools/b409_checks.py; PLACE-papers 29 head notes, INVARIANCE_BARRIERS.md section 10, "
        "FACES_LEDGER.md row U1 and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (GR, GD_, rownum))
    act = ("b409 (both numberings kept and 29 documents declared, the modular relation found "
           "absent under both with a control that found the calibration family, the lemma "
           "relativized for a conditional, three arms proposed and none built, row U1 frozen)")
    row_new = ('    # ### THE OBSTACLES DISSOLVED (b409).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-42s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b409 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('both numberings kept', 'BOTH NUMBERINGS ARE KEPT' in out),
            ('zero renumbered', '0 SYMBOLS WERE RENUMBERED' in out),
            ('the routed are not guessed', 'ROUTED, NOT GUESSED' in out),
            ('b408 corrected', "b408'S CONCLUSION STANDS AND ITS LABEL WAS WRONG" in out),
            ('the two instruments disagreed', 'SYMMETRIC DIFFERENCE OF FIVE' in out),
            ('absent under both schemes', 'ABSENT UNDER BOTH SCHEMES' in out),
            ('the control found the family', 'THE POSITIVE CONTROL PASSED AND FOUND' in out),
            ('kappa by register', 'GRADES KAPPA BY REGISTER' in out),
            ('no row for the modular symmetry', 'HAS NO ROW' in out),
            ('dark on the placement register', 'DARK ON THE PLACEMENT REGISTER' in out),
            ('a reading and not a kappa', 'NOT A MEASURED KAPPA' in out),
            ('the consequence is not drawn', 'NAMED AND NOT DRAWN' in out),
            ('the lemma relativizes', 'RELATIVIZES TO A PROOF OF A CONDITIONAL' in out),
            ('the cost is printed', 'ONE HYPOTHESIS THE ORIGINAL DID NOT NEED' in out),
            ('the restatement is uncompiled', 'UNCOMPILED AND TAKES NO NEW GRADE' in out),
            ('the classification is unrun', 'THAT NOBODY HAS RUN' in out),
            ('three arms, none built', '3 MATHEMATICS-FACING GATE ARMS PROPOSED, 0 WRITTEN' in out),
            ('the row is frozen', 'FROZEN AS A REGISTER COMPLETE AT SIX' in out),
            ('a freeze is not a closure', 'A FREEZE IS NOT A CLOSURE' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-42s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


# ### =================================================================================================
# ### THE BANK.
# ### =================================================================================================
def bank(Q, rownum, kok, decl, ibn):
    B = []
    BARR, SUBB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BARR)
    A('b409 -- THE OBSTACLES DISSOLVED WHERE THE RECORD ALLOWS.')
    A('### THE BANK. ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b409_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py` run as b409'
      % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (GR, LG['gates_passing'], GD_))
    A(BARR)
    A('')
    A(SUBB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUBB)
    A('### ### ### **THE CORPUS DOES GRADE `κ` BY REGISTER, AND IT HAS A CALIBRATED ROW FOR')
    A('### ### ### THE ARCHIMEDEAN INTERFACE AND NONE FOR THE MODULAR RELATION.**')
    A('### `INVARIANCE_BARRIERS.md` §9, *The calibration family: the archimedean instance and')
    A('### the per-place table*, is a section this record ### **HAD NEVER CITED**, and its')
    A('### archimedean row reads *"the archimedean interface carries κ > 0 for the density')
    A('### register and κ = 0 for the placement register."*')
    A('### ### **`b408` COULD NOT HAVE FOUND IT.** ### That section names its interfaces by')
    A('### DESCRIPTION and never by symbol, and `b408` searched for the class SYMBOL beside a')
    A('### channel word. ### **THE FERRY`S INSTRUCTION TO SEARCH BY DESCRIPTION, WITH A POSITIVE')
    A('### ### CONTROL, IS WHAT FOUND IT** -- and the control is why the ABSENT verdict can be')
    A('### trusted at all.')
    A('### ### **AND THE FAMILY`S ROWS ARE PLACES.** ### The modular symmetry is not a place, so')
    A('### it has no row; and the family`s own stated next moves are ### **FURTHER PER-PLACE')
    A('### ### INSTANCE ROWS**, which would not reach it.')
    A('')
    A(SUBB)
    A('### (2) (R25), EXECUTED.')
    A(SUBB)
    A('### ### **BOTH NUMBERINGS KEPT. ### `%d` DOCUMENTS DECLARED. ### `0` SYMBOLS RENUMBERED.**'
      % decl)
    A('### `95` live documents carry `1506` class-symbol uses; `8` deposited documents and their')
    A('### `516` uses were ### **NOT TOUCHED.**')
    A('### ### ### **AND ONLY `29` OF THE `95` CAN BE ASSIGNED A SCHEME FROM THEIR OWN TEXT.** ###')
    A('### `66` are marked ### **SCHEME UNDECLARED** ### and ROUTED. ### **THE NAVIGATOR`S (N1)')
    A('### ### IS REFUTED, AND ITS STATED REASON WITH IT:** ### the documents do not cite the')
    A('### monograph`s table; ### **EXACTLY ONE DOCUMENT CARRIES IT, AND THE MONOGRAPH')
    A('### ### CONTRADICTS IT.**')
    A('')
    A('### ### **`b408`’S CONCLUSION STANDS AND ITS LABEL WAS WRONG -- CORRECTED, NOT')
    A('### ### EDITED.** ### There ARE two numberings and they disagree on six of seven symbols.')
    A('### But the second is ### **NOT THE MONOGRAPH`S**: the monograph`s own class table gives')
    A('### *"| C₄ (Modular/PSL₂) | Transformation | Modular symmetry (PSL₂(ℤ)')
    A('### action) |"*, and `ENUMERA.md` independently reconciles *"the monograph’s canonical')
    A('### index is C₁ Schwarz · C₂ Euler · C₃ functional-equation ·')
    A('### C₄ modular/PSL₂ ..."*. ### **THE TABLE DESCRIBES A LIVE SCHEME CORRECTLY AND')
    A('### ### MISNAMES WHOSE IT IS** -- and it IS live, in `9` documents.')
    A('')
    A('### ### **AND THIS ACT`S OWN TWO INSTRUMENTS DISAGREED.** ### The survey called `28`')
    A('### readable; the matcher calls `29` decidable. ### **A DIFFERENCE OF ONE CONCEALING A')
    A('### ### SYMMETRIC DIFFERENCE OF FIVE**, because the survey`s predicate was *matches the')
    A('### canonical index* and not *decides between the two*: it scores a document that uses the')
    A('### other scheme consistently at zero, and a document whose only pinned symbol is the one')
    A('### both schemes share at one. ### **BOTH NUMBERS ARE PRINTED, THE SURVEY`S LINE IS NOT')
    A('### ### EDITED, THE MATCHER GOVERNS, AND THE DEFECTIVE PREDICATE IS NAMED.**')
    A('### ### **AND TWO OF THE DECLARABLE DOCUMENTS BEGIN WITH A BYTE-ORDER MARK**, which this')
    A('### act`s FIRST head test read as headless and would have ROUTED unread. ### **A DOCUMENT')
    A('### ### IS NOT HEADLESS BECAUSE AN INVISIBLE CHARACTER STANDS IN FRONT OF ITS HEAD.**')
    A('')
    A('### **AND THE HEAD NOTE NAMES NO CLASS SYMBOL, BY DESIGN.** ### A note listing the classes')
    A('### would pin its own document`s scheme, and the matcher would be reading this act`s')
    A('### sentence back to itself. ### **A DECLARATION MUST NOT BE ITS OWN EVIDENCE.**')
    A('')
    A(SUBB)
    A('### (3) THE GLOBAL CLASS: ABSENT, AND THEN READ.')
    A(SUBB)
    A('### **ABSENT UNDER BOTH SCHEMES.** ### `4` hits by description and `2` by symbol across')
    A('### `4746` files, ### **EVERY ONE HAND-READ**, and not one examines the modular relation')
    A('### as a channel. ### The two artefact hits `b408` met are settled by the path`s own')
    A('### MACHINERY line rather than by a numbering table: *"the level curves, the logarithmic')
    A('### derivative ... the Hadamard product"* are the LOCAL and ORDER classes, and ###')
    A('### **NEITHER IS THE MODULAR RELATION.**')
    A('')
    A('### ### ### **AND THE READING: DARK ON THE PLACEMENT REGISTER.**')
    A('### The monograph states of ### **EVERY** ### class that *"the constraint function of each')
    A('### mechanism class is antisymmetric about the reflection axis (the functional equation')
    A('### forces this). An antisymmetric continuous function has exactly one zero on the axis."*')
    A('### ### **AN ANTISYMMETRIC CONSTRAINT LOCATES THE AXIS, NOT A POINT ON IT.** ### So the')
    A('### modular relation, like the functional equation, preserves the critical line and')
    A('### distinguishes no individual zero on it -- ### **WHICH IS THE RECORD`S OWN PLACEMENT')
    A('### ### REGISTER, THE ONE THE ARCHIMEDEAN ROW GRADES AT `κ = 0`.**')
    A('')
    A('### ### **AND WHAT THIS VERDICT IS NOT, IN THE SAME BREATH AS THE VERDICT.** ### It is a')
    A('### ### **READING OF THE RECORD`S OWN TWO SENTENCES, NOT A MEASURED `κ` UNDER')
    A('### ### DEFINITION 2.4`S SUPREMUM.** ### The calibration family has ### **NO ROW** ### for')
    A('### the modular relation, so ### **NO CERTIFICATE EXISTS**, and this act writes none.')
    A('### ### **AND A CONSEQUENCE IS NAMED AND NOT DRAWN:** ### if every class`s constraint is')
    A('### antisymmetric and the channels are the mechanism classes with no fourth, then Corollary')
    A('### 3.6`s bright channel is not among the three as the record reads them. ### **THAT')
    A('### ### FOLLOWS FROM TWO SENTENCES READ TOGETHER AND IT IS NOT ESTABLISHED HERE.** ### `0`')
    A('### routes proposed, priced or opened.')
    A('')
    A(SUBB)
    A('### (4) THE LEMMA, RELATIVIZED AND WRITTEN.')
    A(SUBB)
    A('### ### **IT RELATIVIZES**, and Theorem 3.1-H is written into the barrier keystone as')
    A('### §10, `%d` lines. ### Lemma 3.4 and Proposition 3.5 ### **SURVIVE UNCHANGED** --' % ibn)
    A('### 3.5 needs no witness satisfying `H` at all, because it is a ### **GENERAL')
    A('### ### NON-ENTAILMENT.** ### Only the induction changes.')
    A('### ### ### **AND IT COSTS ONE HYPOTHESIS THE ORIGINAL DID NOT NEED: THAT EVERY SENTENCE')
    A('### ### ### OF `H` ITSELF FACTORS THROUGH `I` FOR `P`.** ### Without it a step invoking a')
    A('### premise that references an individual-element specification across `I` does not factor,')
    A('### and the theorem`s own hypothesis fails at that step. ### **A RESTATEMENT THAT QUIETLY')
    A('### ### COSTS MORE THAN THE ORIGINAL IS NOT THE ORIGINAL RELATIVIZED**, so the cost is on')
    A('### the face of the statement.')
    A('### ### **AND IT TAKES NO NEW GRADE.** ### The original`s semantic core is compiled and')
    A('### axiom-free at `SieveCeilingSemantic.sieve_ceiling_semantic`; ### **THAT TERMINAL COVERS')
    A('### ### THE ORIGINAL AND NOT THIS SECTION**, nothing was compiled here, and the section is')
    A('### marked ### **UNCOMPILED.** ### **BORROWING A COMPILED GRADE FOR PROSE WOULD BE THE ONE')
    A('### ### THING THIS WHOLE APPARATUS EXISTS TO PREVENT.**')
    A('### ### ### **AND THE RELATIVIZATION HANDS THE CORPUS A NEW UNASKED QUESTION IN PLACE OF')
    A('### ### ### THE OLD ONE.** ### Applying 3.1-H to the reduction turns on whether the')
    A('### source`s Definition 3.1, Proposition C.1, the local term (149) and Theorem 4.7 each')
    A('### factor through the product-formula interface -- ### **A DEFINITION 2.5 CLASSIFICATION')
    A('### ### OF FOUR SENTENCES THAT NOBODY HAS RUN.** ### **A THEOREM THAT APPLIES *PROVIDED A')
    A('### ### CONDITION* IS NOT A THEOREM THAT APPLIES**, and this act does not run the check.')
    A('')
    A(SUBB)
    A('### (5) THE SPINE: THREE PROPOSED, NONE BUILT.')
    A(SUBB)
    A('### `G-VACUOUS-POPULATION` would have caught `b399`; `G-PREMISE-BEFORE-CONCLUSION` would')
    A('### have caught `b404`; `G-KIND-BEFORE-APPLICATION` would have caught `b405`, `b406` and')
    A('### `b407`. ### ### **`0` WRITTEN.**')
    A('### ### ### **AND NOT ONE CAN BE WRITTEN WITHOUT A DECISION THE AUTHOR HAS NOT MADE** --')
    A('### what counts as *the population*, what a refuted premise with a surviving conclusion')
    A('### scores, and what `b408`’s one statement is CALLED, which is routed and still')
    A('### routed. ### **AN ARM CANNOT ENFORCE A LAW THE RECORD HAS NOT NAMED.** ### That is the')
    A('### finding and not the excuse: there are eight standing apparatus arms and none of these,')
    A('### because an apparatus arm needs no ruling and a mathematics arm does.')
    A('')
    A(SUBB)
    A('### (6) THE ROW, FROZEN.')
    A(SUBB)
    A('### Row `U1` is marked ### **A REGISTER COMPLETE AT SIX**, inside an existing cell, with')
    A('### ### **`0` ENTRIES ADDED, `0` COORDINATES, `0` GRADES AND NO NEW COLUMN.**')
    A('### The reason is the row`s own count: `6` sites, `2` coordinates, `1` price corrected,')
    A('### `0` bridges typed, `0` grades conferred, ### **`0` STATEMENTS ABOUT THE OBJECT.**')
    A('### ### **A FREEZE IS NOT A CLOSURE, NOT A RETIREMENT AND NOT A GRADE.** ### The row stays')
    A('### OPEN, its refusal stands verbatim and unedited, and ### **THE REOPENING CONDITION IS')
    A('### ### PRINTED INSIDE THE CELL** ### so a later act can see when it is met: ### **A SITE')
    A('### ### WHOSE ENTRY PRODUCES A STATEMENT ABOUT THE OBJECT** ### rather than about the')
    A('### record. ### None of the six has.')
    A('')
    A(SUBB)
    A('### (7) THE EXPECTATIONS.')
    A(SUBB)
    A('### **(N1) REFUTED** -- `66` of `95` documents cannot be assigned a scheme from their own')
    A('###   text, and the stated reason is false as well.')
    A('### **(N2) MET** -- and decided by the path`s own MACHINERY line, not by a numbering table.')
    A('### **(N3) MET IN BOTH HALVES**, the second exactly as stated: ABSENT under both schemes,')
    A('###   and DARK for the functional equation`s own reason -- the antisymmetry the monograph')
    A('###   says the functional equation forces.')
    A('### **(N4) MET, WITH ITS COST PRINTED.**')
    A('### ### **`1` REFUTED, `3` MET.** ### And the one refutation is the navigator`s own')
    A('### expectation about the corpus`s citing habits, refuted by a count and not by an opinion.')
    A('')
    A(SUBB)
    A('### (8) WHAT THIS ACT DID NOT DO.')
    A(SUBB)
    A('### `0` class symbols renumbered in any document. ### `0` schemes assigned by guess or by')
    A('### provenance. ### `0` files under `outputs/` touched. ### `0` κ values measured or')
    A('### certified. ### `0` channels opened. ### `0` routes proposed, priced or opened. ### `0`')
    A('### grades moved, conferred or minted. ### `0` entries added to row `U1`. ### `0`')
    A('### coordinates added. ### `0` rows retired or closed. ### `0` folds run. ### `0` rules')
    A('### struck, amended or widened. ### `0` `FERRY_STANDING` clauses added. ### `0` in-place')
    A('### repairs. ### `0` locked faces edited. ### `0` prior acts` banks edited. ### `0` banked')
    A('### ferries edited. ### `0` registry rows edited. ### `0` kernels built. ### `0` `.lean`')
    A('### files touched. ### `0` axiom profiles read or inferred. ### `0` repositories cloned.')
    A('### `0` platform calls. ### `0` content lost.')
    A('### ### **BOTH LANES STAY PARKED. ### THE WAVE STAYS PARKED. ### NOTHING DEPOSITS.**')
    A('### ### **AND `h2` IS WHERE THE DEPOSIT LEFT IT** -- no claim in either direction.')
    A('')
    A(BARR)
    A('### THE WRITES, BY KIND.')
    A(BARR)
    A('### **KIND 10** -- `%d` one-line head notes, original heads preserved, byte-order marks'
      % decl)
    A('###   preserved, `0` symbols moved.')
    A('### **KIND 11** -- `INVARIANCE_BARRIERS.md` §10, appended, `%d` lines, UNCOMPILED.' % ibn)
    A('### **KIND 12** -- `OPEN_TRAILS.md` one appended block; `FACES_LEDGER.md` row `U1` one')
    A('###   cell appended to with ### **NO ENTRY ADDED**; `CORRESPONDENCE.md` row `%d`;' % rownum)
    A('###   `banked_index.py` key `%s` -- read back %s.' % (KEY, 'PASS' if kok else 'FAIL'))
    A('### **AND NOTHING ELSE, OF ANY KIND.**')
    A(BARR)
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  ### BANK WRITTEN : %s  (%d lines, %d bytes)' % (os.path.basename(BANKOUT), len(B), n))
    return len(B)


# ### =================================================================================================
def main():
    rec('=' * 100)
    rec('b409_desk_bank.py -- THE DECLARATIONS, THE LEMMA, THE FREEZE, THE ROW, THE KEY, THE BANK.')
    rec('=' * 100)
    rec('  face LOCKED : %s' % SEALHASH)
    rec('')
    bar()
    rec('  ### THE DESK.')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### KIND 10 -- THE DECLARATIONS, ONE LINE EACH.')
    bar()
    dok, written, already, routed = do_declarations()
    if not dok:
        rec('  ### HARD FAILURE in the declarations.')
        rec('  ### run record : %s' % run_clock.write(D, 'b409_desk_notes', LINES))
        return 1

    rec()
    bar()
    rec('  ### KIND 11 -- THE RELATIVIZED LEMMA, APPENDED TO THE KEYSTONE.')
    bar()
    kok2, ibn = do_keystone()
    if not kok2:
        rec('  ### HARD FAILURE in the keystone append.')
        rec('  ### run record : %s' % run_clock.write(D, 'b409_desk_notes', LINES))
        return 1

    rec()
    bar()
    rec('  ### KIND 12 -- ROW `U1`, THE FREEZE MARK INSIDE AN EXISTING CELL.')
    bar()
    if not do_faces():
        rec('  ### HARD FAILURE in the row.')
        rec('  ### run record : %s' % run_clock.write(D, 'b409_desk_notes', LINES))
        return 1

    rec()
    bar()
    rec('  ### KIND 12 -- THE TRAIL BLOCK.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the b409 block is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b408 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=NL).write(
            NL.join(trail_block(Q)) + NL)
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            rec('  ### run record : %s' % run_clock.write(D, 'b409_desk_notes', LINES))
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_both_kept': 'both numberings are kept' in low,
        'says_none_renumbered': 'no symbol anywhere was renumbered' in low,
        'says_routed': 'routed, not guessed' in low,
        'says_n1_refuted': 'is **refuted**' in low,
        'says_a_priced': 'disposition (a) was priced before (b) was executed' in low,
        'says_label_wrong': 'misnames whose it is' in low,
        'says_instruments': 'symmetric difference of five' in low,
        'says_predicate_named': 'the defective predicate is named' in low,
        'says_bom': 'byte-order mark' in low,
        'says_absent': 'never been examined as a channel' in low,
        'says_control': 'positive control that passed' in low,
        'says_section9': 'the calibration family' in low,
        'says_no_row': 'so it has no row' in low,
        'says_dark': 'dark on the placement register' in low,
        'says_not_kappa': 'not a measured κ' in low,
        'says_not_drawn': 'it is not established here' in low,
        'says_relativizes': 'relativizes to a proof of a conditional' in low,
        'says_cost': 'one hypothesis the original did not need' in low,
        'says_uncompiled': 'takes no new grade' in low,
        'says_unrun': 'nobody has run' in low,
        'says_three_arms': '`0` are written' in low,
        'says_frozen': 'frozen as a register complete at six' in low,
        'says_not_closure': 'a freeze is not a closure' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
        'says_h2': 'h2 where the deposit left it' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        rec('  ### run record : %s' % run_clock.write(D, 'b409_desk_notes', LINES))
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
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### run record : %s' % run_clock.write(D, 'b409_desk_notes', LINES))
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
        new = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new)
        back = io.open(TABLE, encoding='utf-8').read()
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            rec('  ### run record : %s' % run_clock.write(D, 'b409_desk_notes', LINES))
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
    nb = bank(Q, rownum, kok, written + already, len(IBSEC))

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### DOCUMENTS DECLARED %d. ### SYMBOLS RENUMBERED '
        '0. ### KEYSTONE SECTION %d LINES. ### ROW U1 FROZEN, 0 ENTRIES. ### CORR ROW %d. ### KEY '
        '%s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], written + already, ibn, rownum,
           'PASS' if kok else 'FAIL', nb))
    bar('=')
    p = run_clock.write(D, 'b409_desk_notes', LINES)
    print(NL + '  ### THIS RUN WROTE : %s   (stamp %s)'
          % (os.path.basename(p), run_clock.read_stamp(p)))
    lp, ls, note = run_clock.latest(D, 'b409_desk_notes')
    print('  ### AND THE GUARD AGREES : %s   (%s ; %s)'
          % (os.path.basename(lp or '-'), ls, note))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
