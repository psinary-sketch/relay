# -*- coding: utf-8 -*-
"""b406_desk_bank.py -- THE DESK, THE ONE REPAIR, THE TRAIL BLOCK, THE ROW, THE KEY, THE STANDING
### CLAUSE AND THE BANK.

### ### **THE REPAIR IS THE ONLY IN-PLACE EDIT THIS ACT MAKES, AND IT IS GUARDED THREE WAYS:** ###
### the target string is UNIQUE in the file; the replacement is the record's own house form copied
### from where the record already writes it; and the ORIGINAL is preserved verbatim in the appended
### block and in the bank. ### **IT ADDS A QUALIFIER AND CHANGES NOTHING ELSE** -- the arms
### re-measure that against the pre-act blob.
###
### ### **AND EVERY WRITE ENCODES BEFORE IT OPENS** (`b405`'s zero-byte husk).
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
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
STANDING = os.path.join(ROOT, 'tools', 'FERRY_STANDING.md')
MARK = '<!-- b406 the sites without an existential, and the finite side qualifier swept -->'
PRIOR = '<!-- b405 the row law restated: kind and witness, and the countermodel read whole -->'
BANKOUT = os.path.join(D, 'b406_the_sites_without_an_existential.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def write_bytes(path, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.**"""
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


SEALTXT = io.open(os.path.join(D, 'b406_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b406_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b406_components.txt'), encoding='utf-8').read()
EXTR = io.open(os.path.join(D, 'b406_extract.txt'), encoding='utf-8').read()

# ### ==================================================================================================
# ### ### **THE ONE REPAIR.** ### The target is unique in the file; the replacement copies the
# ### ### record's own house form from `FINDINGS.md:3049`.
# ### ==================================================================================================
OLD = '**kernel terminals `B329.*` (24, zero-axiom) and `B310.*`**'
NEW = ('**kernel terminals `B329.*` (24, zero-axiom; the decomposition and the scaling part '
       'GENERAL, the compact part PER CELL) and `B310.*`**')
ORIGINAL_SENTENCE = ('Half one of the reading is the clause statement’s own **K3**: *the '
                     'source’s construction on the object returns the test function at the '
                     'identity times a dimension and no arithmetic* (b310), at '
                     '**kernel terminals `B329.*` (24, zero-axiom) and `B310.*`**.')

DESK = [
    ('the four open lists', 'STANDING',
     'None fires on this act; the triggers are unchanged and printed in the closing.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane. ### A block on the work is not an absence of a '
     'trigger.'),
    ('W-ORD-E0-RANK-PROPAGATION', 'STANDING', 'No grade moves in this act.'),
    ('b321’s face; SIDE-window’s missing guard; the KINDS write-list shortfall',
     'STANDING', 'ROUTED and still routed; none is repaired here.'),
    ('the keystone’s widened no-Mathlib claim; SIDE-effects’ absent printed profile',
     'STANDING', 'ROUTED at b404. ### The lane is PARKED and nothing is built.'),
    ('the row’s own restatement into residue form', 'STANDING',
     'ROUTED at b404, MEASURED at b405 (4 of 6 name the statement, 1 of 6 files the residue), and '
     'still not applied. ### b406 rewrites no entry.'),
    ('the shape-to-instance route', 'STANDING',
     'PRICED at b405 and untaken. ### b406 adds nothing to it.'),
    ('what the repair of the OTHER form is called', 'CLOSE',
     'FOUND, IN THE RECORD’S OWN WORDS: the barrier is the SIEVE CEILING LEMMA and the gap is '
     'classified by ESCAPE-KIND (scale-horizon / raw-infinitude); the repair is A BRIGHT CHANNEL, '
     'an interface with kappa > 0. ### No name is minted by the seat.'),
    ('the two sites without an existential', 'CLOSE',
     'READ AT DEPTH. ### (i)’s existential is one level down and belongs to (iii); (iv)’s '
     'is TRIVIALLY SATISFIABLE. ### b405’s cells stand and its reason gains one clause.'),
    ('a third coordinate for the row', 'STANDING',
     'PRICED AND NOT ADDED: 5 of 6 fillable from banked text, 1 UNSTATED, and it would sit inside '
     'the column law. ### (R24) gave the row two coordinates and no more.'),
    ('the finite side’s qualifier across the reader-facing surfaces', 'CLOSE',
     'SWEPT AND CLASSIFIED. ### Living record 11 of 12 QUALIFIED, one repaired in place with its '
     'original preserved. ### The navigator’s ferries are 1 of 4 and are DECLARED, not '
     'repaired.'),
    ('the verdict-word substring species', 'CLOSE',
     'PROMOTED into FERRY_STANDING as A2 by that file’s own amendment mechanism, six '
     'incidents listed by act, the version line NOT bumped and the reason printed.'),
    ('the second new standing sentence -- every write encodes before it opens', 'STANDING',
     'ROUTED TO THE AUTHOR. ### The order named one sentence for promotion and this act promotes '
     'one.'),
    ('the arity of the standing laws', 'CLOSE',
     'AUDITED AND PRINTED: 4 of 5 BINARY, n-ARY or AGGREGATE; (R14) alone UNARY, and it names its '
     'own limit. ### Nothing struck, amended or re-ruled.'),
    ('M-2', 'STANDING', 'OWED and stays owed. ### No aggregation is stated.'),
    ('h2', 'STANDING',
     'WHERE THE DEPOSIT LEFT IT. ### No claim in either direction.'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES FIVE ITEMS AND LEAVES THE REST STANDING.**')
    rec('')
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1200), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def do_repair(side='HEAD'):
    """### **ONE SENTENCE, IN PLACE -- AND THE PRESERVED ORIGINAL IS NOT A REPAIR TARGET.**

    ### ### **THIS FUNCTION'S FIRST VERSION REPAIRED THIS ACT'S OWN PRESERVED ORIGINAL.** ### It
    ### searched the WHOLE file; on the second run the only remaining occurrence of the target was
    ### the original quoted verbatim inside this act's own appended block, and the edit landed
    ### there. ### **A BLOCK THAT PRESERVES A SENTENCE BY QUOTATION IS NOT A PLACE TO REPAIR IT**
    ### (b391's species, and b403's re-banking from an already-edited file). ### The cure is to
    ### scope the search to the region BEFORE this act's own mark, and to refuse on any count but
    ### one -- both printed.
    """
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    live, kept = (before.split(MARK, 1) + [''])[:2] if MARK in before else (before, '')
    n_live, n_kept = live.count(OLD), kept.count(OLD)
    rec('  ### the target occurs %d time(s) in the LIVE region and %d time(s) inside this act`s'
        % (n_live, n_kept))
    rec('  ### own preserved block. ### **THE PRESERVED ONE IS NOT A TARGET AND IS NOT COUNTED.**')
    if n_live == 0 and NEW in live:
        rec('  ### ALREADY REPAIRED -- the qualifier is present in the live region.')
        return True, 1
    if n_live != 1:
        rec('  ### HARD FAILURE -- a repair target that is not unique is not a repair target.')
        return False, 0
    blob = subprocess.run(['git', '-C', PP, 'show', '%s:OPEN_TRAILS.md' % side],
                          capture_output=True).stdout.decode('utf-8')
    rec('  ### the pre-act blob at %s carries the ORIGINAL : %s' % (side, OLD in blob))
    after = live.replace(OLD, NEW, 1) + ((MARK + kept) if MARK in before else '')
    write_bytes(TRAILS, after)
    back = io.open(TRAILS, encoding='utf-8', newline='').read()
    bl, al = before.split(chr(10)), back.split(chr(10))
    same = sum(1 for a, b in zip(bl, al) if a == b)
    ok = (len(bl) == len(al)) and same == len(bl) - 1 and back.count(NEW) == 1
    rec('  ### lines %d -> %d ; UNCHANGED %d of %d ; the repaired line is the only one that moved'
        % (len(bl), len(al), same, len(bl)))
    delta = len(back.encode('utf-8')) - len(before.encode('utf-8'))
    rec('  ### bytes +%d, and the ONLY text added is the qualifier itself : %s'
        % (delta, delta == len(NEW.encode('utf-8')) - len(OLD.encode('utf-8'))))
    ok = ok and delta == len(NEW.encode('utf-8')) - len(OLD.encode('utf-8'))
    liveback = back.split(MARK, 1)[0] if MARK in back else back
    for lbl, cond in (
            ('the qualifier is now present in the live region',
             'the compact part PER CELL) and `B310.*`' in liveback),
            ('the claim is otherwise word for word',
             liveback.replace(NEW, OLD) == live),
            ('and this act`s own preserved original is untouched',
             kept == (back.split(MARK, 1)[1] if MARK in back else '')),
            ('no grade word was added or removed',
             len(re.findall(r'PROVED-|DERIVES-|MEASURED-|IMPORT-', back))
             == len(re.findall(r'PROVED-|DERIVES-|MEASURED-|IMPORT-', before)))):
        ok = ok and cond
        rec('      %-46s : %s' % (lbl, cond))
    rec('  ### ### **%s**' % ('PASS' if ok else '### FAIL ###'))
    return ok, 1


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b406 — the two sites without an existential, the record’s own name for the '
        'other form, and the finite side’s qualifier swept — filed 2026-09-10',
        '',
        '**b405 left two cells reading `UNSTATED` because the shared-witness form does not '
        'transpose at `(i)` and `(iv)`. Read at depth, both cells stand and the reason gains one '
        'clause.** `(i)`’s obstruction is two universals with no `∃` between them — '
        'but unfold the CLASS the first quantifier ranges over and the source’s own '
        'characterisation of membership IS existential: Boas–Kac’s `∃ g`, indexed '
        'by the support width, **which is site `(iii)`’s and not `(i)`’s**. `(iv)`’s '
        'record holds TEN VALUES, and a measured value is not an existential claim; the '
        'existential one can always manufacture — `∀a ∃C_a . |V(a)| ≤ C_a`, '
        'take `C_a = |V(a)|` — is **TRIVIALLY SATISFIABLE**, and the shared witness it would '
        'demand is a bound good for every `a`, which IS the missing statement rather than a repair '
        'for its absence. **AN EXISTENTIAL THE RECORD HOLDS IS NOT THE SAME OBJECT AS ONE YOU CAN '
        'ALWAYS MANUFACTURE**, and that is exactly what separates `(iv)` from `(v)`, whose source '
        'STATES an implied constant per representation. So the precise statement is: **no inner '
        'existential the shared-witness form can repair.** The cells are not edited.',
        '',
        '**The record already has a name for the other form, and it is not *uniform witness*.** '
        'The barrier is named twice: `phase1.5/method/INVARIANCE_BARRIERS.md` Theorem 3.1, **the '
        'Sieve Ceiling Lemma** — a proof factoring through a `κ = 0` interface *"does '
        'not establish the universal statement"* and can reach *"P holds for x in a density-one '
        'subset of each I-class, but cannot certify individual elements"*; and '
        '`phase1.5/method/THE_DIFFICULTY_KINDS.md` names the gap itself, **the escape-kind**, '
        'which *"classifies why finite certificates don’t reach the global claim"* with two '
        'values, **`scale-horizon`** and **`raw-infinitude`**. **The repair also has a name, and '
        'it is Corollary 3.6’s: A BRIGHT CHANNEL** — *"any proof of universality must '
        'contain at least one inference step operating through a κ > 0 interface"*. **The two '
        'do not weigh the same, and this act says so rather than reporting one as the other:** the '
        'barrier has a theorem, a corollary, a classification and two kinds; the repair has one '
        'corollary and a name, stated only as the negation of the barrier’s hypothesis. **The '
        'record says what must be true of a closing proof and not what would make one.** No name '
        'is minted here.',
        '',
        '**A third coordinate is PRICED and NOT ADDED.** `ESCAPE-KIND`, with the record’s own '
        'two values, would fill **5 of 6** cells from banked text alone under a strict test — '
        '`(ii)`, `(iii)`, `(iv)` by a scale the site names (a height, a width, a width), `(i)` and '
        '`(v)` by a set the site names (the zeros and the class; the cuspidal representations on '
        '`GL(N)`) — and would leave **`(vi)` `UNSTATED`**, because that site’s own '
        'language is *local-to-global* and deciding it would be this seat’s inference rather '
        'than the site’s text. It would sit inside the column law as `KIND` and `WITNESS` do. '
        '**`(R24)` gave the row two coordinates and no more, and a seat that prices a third and '
        'then writes it has not priced anything. b406 writes nothing to the row.**',
        '',
        '**`(iii)`’s two clauses, in the source’s own symbols, and then a full stop.** '
        '`h1` (SHAREDNESS): one `g ∈ Cc^∞(ℝ)` such that for EVERY `A > 0`, '
        '`supp g ⊆ [-A/2, A/2]` and `f_A = g ∗ g^*` is the Boas–Kac representative '
        'at width `A` — one `g` where the source gives one `g` per `A`. `h2` '
        '(NON-DEGENERACY): that same `g` in the criterion’s own class, '
        '`g ∈ Cc^∞(ℝ_+^*)` with `g̃(z) = 0` for all `z ∈ F`, and '
        '`g ≢ 0`. **WHETHER SUCH A `g` CAN EXIST IS NOT ATTEMPTED**: that is a mathematical '
        'claim about the source’s class, it needs the parked lane, and naming the two clauses '
        'of a witness is not deriving whether one exists.',
        '',
        '**The standing laws, audited for arity — a reading, not a ruling.** The '
        'deposit’s §27.3 refusal is n-ARY (its subject is the cross-register '
        'equivalences) and **cannot answer anything about one register’s own status**. '
        '`(R20)` is MIXED — two unary limbs, a BINARY kernel limb (*a kernel deposits when a '
        'published claim cites its terminals*) and a BINARY obligation — and **cannot answer '
        'anything about a record with no claim on either side of it, which is precisely the '
        '`SIDE-kernel` question b392 entered as standing in the same breath as the ruling**. '
        '`(R1)` is an AGGREGATE on a count and **cannot see a reason**: not whether one act '
        'belongs in a fold, nor whether a span that ended at eight should fold early. Row '
        '`U1`’s refusal is n-ARY, `0` of `4` predicates unary, as b405 measured. **`(R14)` '
        'alone is UNARY — its subject is a document — and it is the one law that states '
        'its own limit in its own text**, naming the separate mirroring ruling beside it. **Four '
        'of five cannot answer a unary question; the fifth knew it and said so. Nothing is struck, '
        'amended or re-ruled.**',
        '',
        '**The finite side’s qualifier, swept wherever a reader meets it — and the '
        'sweep’s first matcher was too small.** A narrow closure-verb set returned **`0` '
        'unqualified** and would have let this act bank *nothing to repair*; it missed the '
        'corpus’s own house form for the claim, which is not a verb at all: *at kernel '
        'terminals `B329.*` (24, zero-axiom)*. Widened by that phrase the sweep returns **`1`**. '
        '**A SWEEP’S YIELD IS A PROPERTY OF ITS MATCHER UNTIL A SECOND SHAPE HAS BEEN TRIED**, '
        'and both yields are printed. Scoped to citations of the seal’s own terminals the '
        'living record is **11 of 12 QUALIFIED**. The wider shape — the words *finite side / '
        'finite places / trace silence* — reaches the h2 programme’s `TraceSilence`, '
        '`general_p_no_fixed_cell` and `Grading.*`, **a DIFFERENT OBJECT in other repositories**; '
        'its yield is printed and **nothing in it is hand-read or repaired**, because a sentence '
        'about another object is not an unqualified sentence about this one.',
        '',
        '**The one unqualified sentence is repaired in place, and its original is preserved here '
        'verbatim.** It is in this ledger, in b398’s verdict block, and it read: *"'
        + ORIGINAL_SENTENCE + '"* The repair adds the parenthetical **the record already writes at '
        '`FINDINGS.md:3049`** — *(24, zero-axiom; the decomposition and the scaling part '
        'GENERAL, the compact part PER CELL)* — and nothing else: **no grade moves, no claim '
        'changes, and the sentence is otherwise word for word.** **AND THE ELISION IS THICKER IN '
        'THE NAVIGATOR’S OWN FERRIES THAN IN THE LIVING RECORD**: of four ferry candidates, '
        '**three carry it** (b329, b331, b405), and b331’s ferry carries both dresses twelve '
        'lines apart — *24 zero-axiom terminals; general and per-cell* at line 36 and *the '
        'finite side is compiled* bald at line 46. **And the act that ferry ordered wrote the '
        'qualifier back in**: b331’s own fold stands at `FINDINGS.md:2896` as *the finite '
        'side compiled: the decomposition and the scaling part general, the compact part per '
        'cell*. **The seat repaired the elision on the way in.** No ferry is edited and no prior '
        'bank is edited; both are declared.',
        '',
        '**The verdict-word species is promoted into `FERRY_STANDING` by that file’s own '
        'amendment mechanism.** `A2`, under `AUTHOR-RULED CLAUSES (NOT MEASURED)`, in the shape '
        '`A1` already has. **The version line is NOT bumped, and that is a decision:** the file is '
        'cited as `FERRY_STANDING v2` and the scan reports any other version as a **stale '
        'citation**, so bumping it would fire on the next correct ferry — which is why `A1` '
        'went in under `v2` too. **The count is measured, not adopted:** the record carries **six** '
        'incidents — b316 (latent), b317, b400, b403, b404, b405 — **four of them in '
        'this session**. The order calls it the fifth in one session; this act prints what it can '
        'evidence and leaves the count to the reader. **And one sentence is deliberately not '
        'promoted**: this ferry’s standing block also carries *every write encodes before it '
        'opens*, bought by b405’s zero-byte husk — **ROUTED to the author, not promoted, '
        'because promoting what was not asked is scope-widening dressed as diligence.**',
        '',
        '**Nothing deposits.** `0` grades moved, `0` bridges typed, `0` entries rewritten, `0` '
        'coordinates added, `0` names minted, `0` keystones edited, `0` ferries edited, `0` prior '
        'banks edited, `0` kernels built, `0` `.lean` files touched, `0` content lost. Both lanes '
        'stay parked and the wave stays parked. Registration '
        '`data/b406_registration_2026-09-10.txt`, LOCKED before any write at sha256 `%s`, chained '
        'on `tools/b378_lockgate.py` run as b406 — %d gates read, %d checked by digest. Bank: '
        '`relay/data/b406_the_sites_without_an_existential.txt`. **h2 where the deposit left it.**'
        % (SEALHASH, LG['gates_read'], LG['face_subject_gates']),
    ]


A2 = (
    "- **A2** An arm that reads a tool's verdict reads the tool's VERDICT LINE, never the verdict "
    "word as a substring of the tool's whole output.  --- **AUTHOR-RULED 2026-09-10**, in the "
    "standing block of the b406 ferry (`relay/data/b406_ferry.txt`): *\"every arm reading a tool's "
    "verdict reads the verdict LINE\"*, with the promotion ordered in the same paste: *\"Promote "
    "that sentence into FERRY_STANDING by its own amendment mechanism, with the five incidents "
    "listed by act, so the next ferry inherits it by reference rather than by restatement.\"* "
    "**THE OCCASION, AND THE INCIDENTS THE RECORD CARRIES, BY ACT:** b316 `G-NOTRACE` (LATENT -- "
    "searched raw source and passed only because no docstring there named the call); b317 "
    "`G-NOUNIT` (fired on the runner's own docstring line asserting the absence); b400 `G-ONEQ` "
    "(fired on the bank's own negated sentence); b403 `G-FERRYWORDS` (found the ferry's phrase in "
    "a file that act had just written); b404 `G-NOAXIOMCLAIM` (fired on the act's own negated "
    "sentence); b405 `G-KEY` (matched `NO KEY` inside `NO KEYSTONE EDITED` and failed a SUCCESSFUL "
    "lookup). **SIX INCIDENTS IN THE RECORD, FOUR OF THEM IN ONE SESSION.** The cure in every "
    "dress is the same: read the assertion, or read the verdict line -- never the substring. "
    "**NOT MEASURED; carried by no count.**")

A2_NOTE = (
    "**AND THE VERSION LINE IS NOT BUMPED FOR THIS AMENDMENT, FOR THE REASON `A1` WAS NOT.** This "
    "file is cited as `FERRY_STANDING v2` and `relay/tools/ferry_scan.py` reports any other "
    "version as a STALE citation; bumping it here would make every live ferry's citation stale and "
    "the scan would fire on the next correct ferry. The head's own rule covers it: an amendment is "
    "recorded here, and the version moves *when next revised*. **AND ONE SENTENCE THE SAME FERRY "
    "CARRIES IS DELIBERATELY NOT PROMOTED:** *every write encodes before it opens* (b405's "
    "zero-byte husk, `io.open(p,'w')` truncating before it encodes). The order named one sentence; "
    "the second is **ROUTED TO THE AUTHOR** and is not added here, because promoting what was not "
    "asked is scope-widening dressed as diligence.")


def do_standing():
    before = io.open(STANDING, encoding='utf-8', newline='').read()
    if '**A2**' in before:
        rec('  ### ALREADY FILED -- A2 is present. ### NOTHING APPENDED.')
        return True
    # ### **THE FILE'S OWN LINE ENDING, DETECTED AND NOT ASSUMED.** ### `core.autocrlf` makes this
    # ### working file CRLF while its blob stays LF, so an anchor typed with `chr(10)` MISSES a
    # ### file that plainly contains the sentence -- the banked `powershell-bom-trap` species, met
    # ### here and printed rather than worked around in silence.
    eol = chr(13) + chr(10) if (chr(13) + chr(10)) in before else chr(10)
    rec('  ### the working file`s line ending, detected : %s'
        % ('CRLF' if len(eol) == 2 else 'LF'))
    anchor = '**NOT MEASURED; carried by no count.**' + eol
    if anchor not in before:
        rec('  ### HARD FAILURE -- the A1 anchor is not in the file.')
        return False
    ver_before = re.search(r'^VERSION: (\d+)\s*$', before, re.M).group(1)
    addition = eol + A2 + eol + eol + A2_NOTE + eol
    after = before.replace(anchor, anchor + addition, 1)
    write_bytes(STANDING, after)
    back = io.open(STANDING, encoding='utf-8', newline='').read()
    ver_after = re.search(r'^VERSION: (\d+)\s*$', back, re.M).group(1)
    ok = True
    for lbl, cond in (
            ('A2 is present', '**A2**' in back),
            ('it sits under AUTHOR-RULED (NOT MEASURED)',
             back.index('AUTHOR-RULED CLAUSES (NOT MEASURED)') < back.index('**A2**')),
            ('it declares itself NOT MEASURED', back.count('NOT MEASURED; carried by no count') == 2),
            ('the six incidents are listed by act',
             all(a in back for a in ('b316', 'b317', 'b400', 'b403', 'b404', 'b405'))),
            ('the VERSION line did not move', ver_before == ver_after == '2'),
            ('the reason for not bumping is on the file', 'STALE citation; bumping it here' in back),
            ('the unpromoted sentence is ROUTED and named',
             'ROUTED TO THE AUTHOR' in back and 'every write encodes before it opens' in back),
            ('no measured clause was added by hand',
             back.count('  --- **AUTHOR-RULED') == 2),
            ('the file is otherwise byte-identical',
             back.replace(addition, '') == before)):
        ok = ok and cond
        rec('      %-48s : %s' % (lbl, cond))
    rec('  ### bytes %d -> %d ; VERSION %s -> %s'
        % (len(before.encode('utf-8')), len(back.encode('utf-8')), ver_before, ver_after))
    rec('  ### ### **%s**' % ('PASS' if ok else '### FAIL ###'))
    return ok


SCOPE = ("### THIS ROW RECORDS TWO SITES READ AT DEPTH, A NAME FOUND IN THE RECORD, A COORDINATE "
         "PRICED AND NOT ADDED, AND ONE SENTENCE REPAIRED BY ADDING A QUALIFIER. ### IT CERTIFIES "
         "NO EQUIVALENCE, OPENS NO TERMINAL, MOVES NO GRADE, MINTS NO NAME AND TYPES NO BRIDGE")


def corr_rows(Q):
    m = ("**THE SHARED-WITNESS FORM FAILS AT TWO SITES FOR TWO DIFFERENT REASONS -- ONE "
         "EXISTENTIAL BELONGS TO ANOTHER SITE AND THE OTHER IS TRIVIALLY SATISFIABLE -- AND THE "
         "RECORD ALREADY NAMES BOTH THE BARRIER AND ITS REPAIR, MORE FULLY THE FIRST THAN THE "
         "SECOND** (b406, the sites without an existential)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b406 -- %d gates read, %d checked by digest; the survey left 0 anchor misses. "
            "**COMPONENT 1**: (i)'s obstruction is two universals with no existential between "
            "them, and the existential one depth down is Boas-Kac's ex-g, which is (iii)'s; "
            "(iv)'s record holds TEN VALUES and the existential one can always manufacture is "
            "TRIVIALLY SATISFIABLE, so the shared witness it would demand IS the missing "
            "statement. **b405's cells stand and its reason gains one clause: no inner existential "
            "THE SHARED-WITNESS FORM CAN REPAIR.** **COMPONENT 2, SCORED IN TWO PARTS**: the "
            "barrier is the SIEVE CEILING LEMMA (Theorem 3.1) and the ESCAPE-KIND classification "
            "(scale-horizon / raw-infinitude); the repair is A BRIGHT CHANNEL, kappa > 0 "
            "(Corollary 3.6). **THE RECORD NAMES THE BARRIER MORE FULLY THAN THE REPAIR AND THIS "
            "ACT SAYS SO RATHER THAN REPORTING ONE AS THE OTHER.** No name is minted. **COMPONENT "
            "3**: a third coordinate ESCAPE-KIND would fill 5 of 6 from banked text and leave (vi) "
            "UNSTATED -- PRICED AND NOT ADDED. **ADDITION ONE**: (iii)'s two clauses stated in the "
            "source's symbols; whether such a g can exist is NOT ATTEMPTED. **ADDITION TWO**: 4 of "
            "5 standing laws are BINARY, n-ARY or AGGREGATE where they are applied unarily; (R14) "
            "alone is UNARY and names its own limit. **ADDITION THREE**: the narrow closure "
            "matcher returned 0 UNQUALIFIED and the widened one returned 1 -- the living record is "
            "11 of 12 QUALIFIED, the navigator's ferries 1 of 4, and ONE sentence is repaired in "
            "place with its original preserved. **ADDITION FOUR**: A2 promoted into FERRY_STANDING "
            "by that file's own mechanism, six incidents by act, VERSION NOT BUMPED. %d GRADES "
            "MOVED, %d BRIDGES TYPED, %d NAMES MINTED, %d COORDINATES ADDED, %d KERNELS BUILT, %d "
            "CONTENT LOST"
            % (LG['gates_read'], LG['face_subject_gates'], 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT AND "
            "NO `.lean` FILE TOUCHED; THE SEAL `Core/FiniteSideSeal.lean` WAS READ AT ITS HEADER "
            "AND ITS CELL LIST ONLY, TO ESTABLISH WHAT QUALIFIER A READER-FACING SENTENCE OWES. "
            "### READING A THEOREM'S SCOPE IS NOT CLAIMING ITS CONTENT")
    prof = ("### NO AXIOM PROFILE IS READ OR INFERRED BY THIS ACT: IT MEASURES SENTENCES ABOUT "
            "TERMINALS, NOT TERMINALS. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW "
            "PAID, NO RULE STRUCK OR AMENDED, NO LAW RE-RULED BY THE ARITY AUDIT, NO CLASS RULED, "
            "NO REGISTRY ROW EDITED, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO BANKED FERRY "
            "EDITED, NO PRIOR ACT'S BANK EDITED, NO ROW OF FACES_LEDGER WRITTEN, NO LIST CLOSED. "
            "### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE SENTENCE REPAIRED IN "
            "PLACE BY ADDING A QUALIFIER THE RECORD ALREADY WRITES ELSEWHERE -- 0 CONTENT LOST, "
            "THE ORIGINAL PRESERVED VERBATIM IN THE APPENDED BLOCK")
    grade = ("### THE SWEEP'S SUBJECT WAS THE SEAL'S OWN TERMINALS AND NOT THE ENGLISH WORDS, "
             "BECAUSE THE h2 PROGRAMME SAYS *TRACE SILENCE AT THE FINITE PLACES* ABOUT A DIFFERENT "
             "OBJECT; THE WIDER YIELD IS PRINTED AND NOTHING IN IT IS REPAIRED. ### BOTH CLOSURE "
             "MATCHERS ARE PRINTED WITH THEIR YIELDS, BECAUSE THE FIRST RETURNED 0 AND WOULD HAVE "
             "BANKED *NOTHING TO REPAIR*. ### AN EXISTENTIAL THAT ANY FAMILY OF VALUES SUPPLIES "
             "FOR FREE IS CALLED TRIVIALLY SATISFIABLE IN THE SAME SENTENCE AS THE VERDICT IT "
             "DECIDES. ### A COORDINATE IS PRICED AND NOT WRITTEN, BECAUSE A SEAT THAT PRICES A "
             "THIRD AND THEN ADDS IT HAS NOT PRICED ANYTHING. ### AND A COUNT THE ORDER STATED WAS "
             "MEASURED AGAINST THE RECORD RATHER THAN CARRIED FORWARD")
    status = ("data/b406_the_sites_without_an_existential.txt; data/b406_components.txt; "
              "data/b406_extract.txt; data/b406_registration_2026-09-10.txt (LOCKED before any "
              "write at sha256 %s, chained on tools/b378_lockgate.py run as b406); "
              "tools/b406_extract.py; tools/b406_regspec.py; tools/b406_reg_gate.py; "
              "tools/b406_components.py; tools/b406_desk_bank.py; tools/b406_checks.py; "
              "PLACE-papers OPEN_TRAILS.md (one append-only block and one sentence repaired in "
              "place); relay tools/FERRY_STANDING.md (one A2 clause); CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what does the corpus call the barrier between instances and the class',
           'what would close a per-instance to universal gap',
           'why do the two sites have no shared witness',
           'is the finite side compiled in general',
           'what is an escape kind',
           'was a third coordinate added to the uniformity row')
MUST_NOT_HIT = ('a third coordinate was added', 'a name was minted', 'a witness was found',
                'a ferry was edited', 'a kernel was built')
KEY = 'the-sites-without-an-existential'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b406 READ THE TWO SITES b405 LEFT UNSTATED AND FOUND THEY FAIL THE SHARED-WITNESS FORM "
        "FOR TWO DIFFERENT REASONS. **(i)'s obstruction is two universals with no existential "
        "between them** -- and the existential one depth down, in the class's own Boas-Kac "
        "characterisation, is ex-g indexed by the support width, **which is site (iii)'s and not "
        "(i)'s**. **(iv)'s record holds TEN VALUES, and a measured value is not an existential "
        "claim**; the existential anyone can manufacture -- for all a there exists C_a with |V(a)| "
        "<= C_a, take C_a = |V(a)| -- is **TRIVIALLY SATISFIABLE**, and the shared witness it "
        "would demand is a bound good for every a, which IS the missing statement rather than a "
        "repair for its absence. **AN EXISTENTIAL THE RECORD HOLDS IS NOT THE SAME OBJECT AS ONE "
        "YOU CAN ALWAYS MANUFACTURE**, and that separates (iv) from (v), whose source STATES an "
        "implied constant per representation. b405's cells stand; the precise reason is **NO INNER "
        "EXISTENTIAL THE SHARED-WITNESS FORM CAN REPAIR**. **THE RECORD ALREADY NAMES BOTH THE "
        "BARRIER AND ITS REPAIR, AND NOT EQUALLY.** The barrier: INVARIANCE_BARRIERS.md Theorem "
        "3.1, **the SIEVE CEILING LEMMA** -- a proof factoring through a kappa = 0 interface *does "
        "not establish the universal statement* and reaches only *P holds for x in a density-one "
        "subset of each I-class, but cannot certify individual elements* -- and "
        "THE_DIFFICULTY_KINDS.md's **ESCAPE-KIND**, which *classifies why finite certificates "
        "don't reach the global claim*, with two values **scale-horizon** and **raw-infinitude**. "
        "The repair: Corollary 3.6's **BRIGHT CHANNEL**, an interface with **kappa > 0**. **THE "
        "BARRIER HAS A THEOREM, A CLASSIFICATION AND TWO KINDS; THE REPAIR HAS ONE COROLLARY AND A "
        "NAME, STATED ONLY AS THE NEGATION OF THE BARRIER'S HYPOTHESIS.** No name is minted by the "
        "seat. **A THIRD COORDINATE, ESCAPE-KIND, WOULD FILL 5 OF 6 FROM BANKED TEXT AND LEAVE "
        "(vi) UNSTATED -- PRICED AND NOT ADDED.** **(iii)'S TWO CLAUSES ARE STATED IN THE SOURCE'S "
        "OWN SYMBOLS AND WHETHER SUCH A g CAN EXIST IS NOT ATTEMPTED.** **THE ARITY AUDIT: 4 OF 5 "
        "STANDING LAWS ARE BINARY, n-ARY OR AGGREGATE WHERE THEY ARE APPLIED UNARILY** -- the "
        "deposit's 27.3 refusal cannot answer anything about one register's status, (R20) cannot "
        "answer anything about a record with no claim on either side (the SIDE-kernel question), "
        "(R1) is a threshold on a count and cannot see a reason -- **and (R14) alone is UNARY and "
        "names its own limit in its own text**. **AND THE FINITE SIDE'S QUALIFIER WAS SWEPT: the "
        "narrow closure matcher returned 0 UNQUALIFIED and would have banked NOTHING TO REPAIR; "
        "widened by the corpus's own house form -- at kernel terminals B329.* (24, zero-axiom) -- "
        "it returned 1.** The living record is 11 of 12 QUALIFIED; **the navigator's own ferries "
        "are 1 of 4**, and b331's ferry carries both dresses twelve lines apart while the act it "
        "ordered wrote the qualifier back in. One sentence repaired in place, its original "
        "preserved.")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY "
        "CLONED AND NO AXIOM PROFILE READ OR INFERRED. ### NO GRADE MOVED OR CONFERRED, NO NAME "
        "MINTED, NO COORDINATE ADDED, NO BRIDGE TYPED, NO WITNESS CLAIMED TO EXIST, NO ENTRY "
        "REWRITTEN, NO LAW STRUCK OR RE-RULED, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO "
        "BANKED FERRY EDITED, NO PRIOR BANK EDITED, NO ROW OF FACES_LEDGER WRITTEN, NO LIST "
        "CLOSED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE SENTENCE REPAIRED "
        "IN PLACE BY ADDING A QUALIFIER THE RECORD ALREADY WRITES AT FINDINGS.md:3049, WITH THE "
        "ORIGINAL PRESERVED VERBATIM. ### FERRY_STANDING GAINS ONE AUTHOR-RULED CLAUSE AND ITS "
        "VERSION LINE DOES NOT MOVE. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    where = (
        "data/b406_the_sites_without_an_existential.txt; data/b406_components.txt; "
        "data/b406_extract.txt; data/b406_registration_2026-09-10.txt (LOCKED before any write, "
        "chained on tools/b378_lockgate.py run as b406 -- %d gates read, %d checked by digest); "
        "tools/b406_extract.py; tools/b406_components.py; tools/b406_desk_bank.py; "
        "tools/b406_checks.py; PLACE-papers OPEN_TRAILS.md; relay tools/FERRY_STANDING.md; "
        "CORRESPONDENCE.md row %d" % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b406 (the two sites read at depth, the record's own name for the barrier and its "
           "repair found and scored apart, a third coordinate priced and not added, and the "
           "finite side's qualifier swept with one sentence repaired)")
    row_new = ('    # ### THE SITES WITHOUT AN EXISTENTIAL (b406).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-42s NO KEY before : %s' % (qq, pre[qq]))
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
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, not a substring]'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-62s reaches the b406 key : %s' % (qq[:62], g2))
    for lbl, cond in (
            ('the two reasons are distinguished', 'TRIVIALLY SATISFIABLE' in out),
            ("(i)'s existential is filed to (iii)", "which is site (iii)'s and not" in out),
            ('the barrier is named', 'SIEVE CEILING LEMMA' in out),
            ('the escape-kind is named', 'ESCAPE-KIND' in out),
            ('the repair is named', 'BRIGHT CHANNEL' in out),
            ('the two are scored apart', 'NOT EQUALLY' in out),
            ('the coordinate is priced not added', 'PRICED AND NOT ADDED' in out),
            ('addition one stops', 'NOT ATTEMPTED' in out),
            ('the arity audit is carried', '4 OF 5 ' in out),
            ('the matcher lesson is carried', 'NOTHING TO REPAIR' in out),
            ('the ferries are counted', 'ARE 1 OF 4' in out or '1 of 4' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-42s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok, repaired, sok):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A('b406 -- THE SITES WITHOUT AN EXISTENTIAL, AND WHAT THEIR REPAIR WOULD BE CALLED.')
    A('### THE BANK. ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b406_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py`' % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### run as b406 -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A(BAR)
    A('')
    A(SUB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUB)
    A('### ### ### **THE TWO SITES FAIL THE SHARED-WITNESS FORM FOR TWO DIFFERENT REASONS, AND')
    A('### ### ### NEITHER REASON IS *THERE IS NO EXISTENTIAL*.**')
    A('### `(i)`’s obstruction is two universals with no `∃` between them -- but unfold')
    A('### the CLASS the first quantifier ranges over and the source’s own characterisation of')
    A('### membership IS existential: Boas-Kac’s `∃ g`, indexed by the support width.')
    A('### ### **THAT EXISTENTIAL IS REAL AND IT BELONGS TO SITE `(iii)`.** ### Filing it at `(i)`')
    A('### would have counted one existential twice.')
    A('### `(iv)`’s record holds ### **TEN VALUES**, and a measured value is not an')
    A('### existential claim. ### The existential anyone can manufacture -- `∀a ∃C_a .')
    A('### |V(a)| ≤ C_a`, take `C_a = |V(a)|` -- is ### **TRIVIALLY SATISFIABLE**, and the')
    A('### shared witness it would demand is a bound good for every `a`, ### **WHICH IS THE')
    A('### ### MISSING STATEMENT RATHER THAN A REPAIR FOR ITS ABSENCE.**')
    A('### ### **AN EXISTENTIAL THE RECORD HOLDS IS NOT THE SAME OBJECT AS ONE YOU CAN ALWAYS')
    A('### ### MANUFACTURE**, and that is exactly what separates `(iv)` from `(v)`, whose source')
    A('### STATES an implied constant per representation.')
    A('### ### ### **SO `b405`’S CELLS STAND AND ITS REASON GAINS ONE CLAUSE: NO INNER')
    A('### ### ### EXISTENTIAL *THE SHARED-WITNESS FORM CAN REPAIR*.** ### The predecessor is')
    A('### corrected without being rewritten, and no cell is edited.')
    A('')
    A(SUB)
    A('### (2) COMPONENT 2 -- THE NAME, SCORED IN TWO PARTS BECAUSE THEY DO NOT WEIGH THE SAME.')
    A(SUB)
    A('### **THE BARRIER: ### PRESENT, AND NAMED TWICE.**')
    A('###   `INVARIANCE_BARRIERS.md` Theorem 3.1, ### **THE SIEVE CEILING LEMMA** ### -- a proof')
    A('###   factoring through a `κ = 0` interface *"does not establish the universal')
    A('###   statement"* and reaches only *"P holds for x in a density-one subset of each')
    A('###   I-class, but cannot certify individual elements"*.')
    A('###   `THE_DIFFICULTY_KINDS.md`, ### **THE ESCAPE-KIND** ### -- it *"classifies why finite')
    A('###   certificates don’t reach the global claim"*, with two values,')
    A('###   ### **`scale-horizon`** ### and ### **`raw-infinitude`**, and the document says the')
    A('###   dichotomy IS the finding.')
    A('### **THE REPAIR: ### PRESENT, AND IT IS NOT *UNIFORM WITNESS*.**')
    A('###   Corollary 3.6 -- *"any proof of universality must contain at least one inference step')
    A('###   operating through a `κ > 0` interface"* -- ### **A BRIGHT CHANNEL.**')
    A('### ### ### **AND THE TWO DO NOT WEIGH THE SAME.** ### The barrier has a theorem, a')
    A('### corollary, a classification and two kinds. ### The repair has ### **ONE COROLLARY AND A')
    A('### ### NAME**, and the corollary states it only as the negation of the barrier’s')
    A('### hypothesis. ### **THE RECORD SAYS WHAT MUST BE TRUE OF A CLOSING PROOF AND NOT WHAT')
    A('### ### WOULD MAKE ONE**, and reporting one as the other would have been this act’s own')
    A('### elision. ### **NO NAME IS MINTED. ### MINTING IS THE AUTHOR’S.**')
    A('')
    A(SUB)
    A('### (3) THE THIRD COORDINATE, PRICED AND NOT ADDED.')
    A(SUB)
    A('### `ESCAPE-KIND` would fill ### **`5` OF 6** ### cells from banked text alone under the')
    A('### strict test -- `(ii)`, `(iii)`, `(iv)` by a SCALE the site names (a height, a width, a')
    A('### width); `(i)` and `(v)` by a SET the site names (the class and the zeros; the cuspidal')
    A('### representations on `GL(N)`) -- and would leave ### **`(vi)` `UNSTATED`**, because that')
    A('### site’s own language is *local-to-global* and deciding it would be this seat’s')
    A('### inference rather than the site’s text. ### It would sit inside the column law')
    A('### exactly as `KIND` and `WITNESS` do.')
    A('### ### ### **AND IT IS NOT ADDED.** ### `(R24)` gave the row two coordinates and no more.')
    A('### ### **A SEAT THAT PRICES A THIRD AND THEN WRITES IT HAS NOT PRICED ANYTHING**, and this')
    A('### act writes nothing to the row at all.')
    A('')
    A(SUB)
    A('### (4) ADDITION ONE -- TWO CLAUSES, AND A FULL STOP.')
    A(SUB)
    A('### **`h1` (SHAREDNESS):** ### one `g ∈ Cc^∞(ℝ)` such that for EVERY `A > 0`,')
    A('### `supp g ⊆ [-A/2, A/2]` and `f_A = g ∗ g^*` is the Boas-Kac representative at')
    A('### width `A` -- ### **ONE `g` WHERE THE SOURCE GIVES ONE `g` PER `A`.**')
    A('### **`h2` (NON-DEGENERACY):** ### that same `g` in the criterion’s own class,')
    A('### `g ∈ Cc^∞(ℝ_+^*)` with `g̃(z) = 0` for all `z ∈ F`, and')
    A('### `g ≢ 0`.')
    A('### ### ### **WHETHER SUCH A `g` CAN EXIST IS `NOT ATTEMPTED`.** ### That is a mathematical')
    A('### claim about the source’s class; it needs the parked lane; and this act neither')
    A('### derives it nor gestures at it. ### **NAMING THE TWO CLAUSES OF A WITNESS IS NOT DERIVING')
    A('### ### WHETHER ONE EXISTS.**')
    A('')
    A(SUB)
    A('### (5) ADDITION TWO -- THE ARITY AUDIT. ### **A READING, NOT A RULING.**')
    A(SUB)
    A('### **THE DEPOSIT’S §27.3 REFUSAL** ### -- n-ARY. ### **CANNOT ANSWER ANYTHING')
    A('###   ### ABOUT ONE REGISTER’S OWN STATUS.**')
    A('### **`(R14)`** ### -- ### **UNARY**, its subject a document. ### Cannot answer a relation')
    A('###   between two documents -- ### **AND IT KNOWS THIS AND SAYS SO**, naming the separate')
    A('###   mirroring ruling beside it: *both hold, neither is edited into the other*.')
    A('### **`(R20)`** ### -- MIXED: two unary limbs, a BINARY kernel limb, a BINARY obligation.')
    A('###   ### **CANNOT ANSWER ANYTHING ABOUT A RECORD WITH NO CLAIM ON EITHER SIDE OF IT** --')
    A('###   which is precisely the `SIDE-kernel` question `b392` entered as standing in the same')
    A('###   breath as the ruling.')
    A('### **`(R1)`** ### -- AGGREGATE, a threshold on a count. ### **CANNOT SEE A REASON:** ### not')
    A('###   whether one act belongs in a fold, nor whether a span that ENDED at eight should fold.')
    A('### **ROW `U1`’S REFUSAL** ### -- n-ARY, `0` of `4` unary (`b405`).')
    A('### ### ### **FOUR OF FIVE CANNOT ANSWER A UNARY QUESTION; THE FIFTH KNEW IT AND SAID SO.**')
    A('### ### **NOTHING IS STRUCK, AMENDED OR RE-RULED. ### A LAW THAT CANNOT ANSWER A QUESTION')
    A('### ### IS NOT A BAD LAW; IT IS A LAW WITH A SCOPE.**')
    A('')
    A(SUB)
    A('### (6) ADDITION THREE -- THE QUALIFIER SWEPT, AND THE MATCHER THAT WAS TOO SMALL.')
    A(SUB)
    A('### ### **THE FIRST MATCHER RETURNED `0` UNQUALIFIED AND WOULD HAVE LET THIS ACT BANK')
    A('### ### *NOTHING TO REPAIR*.** ### A narrow closure-verb set -- compiled / sealed / closed /')
    A('### proved / certified / silent / established -- missed the corpus’s own house form for')
    A('### the claim, which is not a verb at all: ### *at kernel terminals `B329.*` (24,')
    A('### zero-axiom)*. ### Widened by that phrase the sweep returns ### **`1`**.')
    A('### ### **A SWEEP’S YIELD IS A PROPERTY OF ITS MATCHER UNTIL A SECOND SHAPE HAS BEEN')
    A('### ### TRIED**, and both yields are printed rather than the kinder one.')
    A('### **THE LIVING RECORD, SCOPED TO CITATIONS OF THE SEAL’S OWN TERMINALS: `11` OF `12`')
    A('###   ### QUALIFIED.**')
    A('### **THE NAVIGATOR’S OWN FERRIES: `1` OF `4`** -- `b329` line 91, `b331` line 46 and')
    A('###   `b405` line 41 carry the elision; `b331` line 36 carries the qualifier, ### **TWELVE')
    A('###   ### LINES FROM ITS OWN BALD SENTENCE.**')
    A('### ### **AND THE ACT THAT FERRY ORDERED WROTE THE QUALIFIER BACK IN**: ### `b331`’s')
    A('### fold stands at `FINDINGS.md:2896` as *the finite side compiled: the decomposition and')
    A('### the scaling part general, the compact part per cell*. ### **THE SEAT REPAIRED THE')
    A('### ### ELISION ON THE WAY IN**, which is why the living record reads `11` of `12` and the')
    A('### ferries read `1` of `4`.')
    A('### **THE ONE REPAIR, AND THE ORIGINAL PRESERVED VERBATIM:**')
    A('###   `OPEN_TRAILS.md`, `b398`’s verdict block, ### **BEFORE:**')
    for k in range(0, len(ORIGINAL_SENTENCE), 130):
        A('###     | %s' % ORIGINAL_SENTENCE[k:k + 130])
    A('###   ### **AFTER:** ### the same sentence with the parenthetical the record already writes')
    A('###   at `FINDINGS.md:3049` -- *(24, zero-axiom; the decomposition and the scaling part')
    A('###   GENERAL, the compact part PER CELL)*. ### **NO GRADE MOVES, NO CLAIM CHANGES, AND THE')
    A('###   ### SENTENCE IS OTHERWISE WORD FOR WORD.**')
    A('### **AND THE WIDE SHAPE WAS THROWN OUT WITH ITS YIELD PRINTED.** ### The words *finite')
    A('### side / finite places / trace silence* reach the h2 programme’s `TraceSilence`,')
    A('### `general_p_no_fixed_cell` and `Grading.*` -- ### **A DIFFERENT OBJECT IN OTHER')
    A('### ### REPOSITORIES.** ### Nothing in that yield is hand-read or repaired: ### **A')
    A('### ### SENTENCE ABOUT ANOTHER OBJECT IS NOT AN UNQUALIFIED SENTENCE ABOUT THIS ONE.**')
    A('### **NO FERRY IS EDITED AND NO PRIOR BANK IS EDITED**; both are DECLARED.')
    A('### **AND NOTHING IN THE KERNEL IS TOUCHED.**')
    A('')
    A(SUB)
    A('### (7) ADDITION FOUR -- THE STANDING CLAUSE, PROMOTED, AND THE COUNT MEASURED.')
    A(SUB)
    A('### `A2` is appended to `tools/FERRY_STANDING.md` under `AUTHOR-RULED CLAUSES (NOT')
    A('### MEASURED)`, in the shape `A1` has: the clause, the ruling quoted from this ferry, the')
    A('### occasion, and ### **NOT MEASURED; CARRIED BY NO COUNT.**')
    A('### ### **THE VERSION LINE IS NOT BUMPED, AND THAT IS A DECISION AND NOT AN OMISSION.** ###')
    A('### The file is cited as `FERRY_STANDING v2` and `ferry_scan.py` reports any other version')
    A('### as a ### **STALE CITATION**; bumping it would fire the scan on the next correct ferry.')
    A('### `A1` went in under `v2` for the same reason.')
    A('### ### **THE COUNT IS MEASURED, NOT ADOPTED:** ### the record carries ### **SIX**')
    A('### incidents -- `b316` (latent), `b317`, `b400`, `b403`, `b404`, `b405` -- ### **FOUR OF')
    A('### ### THEM IN THIS SESSION.** ### The order calls it the fifth in one session; this act')
    A('### prints what it can evidence and leaves the count to the reader.')
    A('### ### **AND ONE SENTENCE IS DELIBERATELY NOT PROMOTED.** ### This ferry also carries')
    A('### *every write encodes before it opens*, bought by `b405`’s zero-byte husk. ### The')
    A('### order named ONE sentence. ### **THE SECOND IS ROUTED TO THE AUTHOR AND NOT PROMOTED,')
    A('### ### BECAUSE PROMOTING WHAT WAS NOT ASKED IS SCOPE-WIDENING DRESSED AS DILIGENCE.**')
    A('')
    A(SUB)
    A('### (8) THE WRITES, AND WHAT THEY COST THE RECORD.')
    A(SUB)
    A('### **`OPEN_TRAILS.md`** ### -- one append-only block ### **AND ONE SENTENCE REPAIRED IN')
    A('### PLACE**, the only line in the file that moved, `+%d` bytes -- and the added text is'
      % (len(NEW.encode('utf-8')) - len(OLD.encode('utf-8'))))
    A('### the qualifier itself and nothing else.')
    A('### **`tools/FERRY_STANDING.md`** ### -- one `A2` clause, `VERSION` unmoved at `2`, %s.'
      % ('PASS' if sok else '### FAIL ###'))
    A('### **`CORRESPONDENCE.md`** ### -- row `%d`, appended, six cells non-empty.' % rownum)
    A('### **THE INDEX** ### -- one key, `%s`, %s.' % (KEY, 'PASS' if kok else '### FAIL ###'))
    A('### **AND NOTHING ELSE.** ### `0` rows of `FACES_LEDGER.md` written, `0` coordinates added,')
    A('### `0` entries rewritten, `0` names minted, `0` grades moved, `0` bridges typed, `0`')
    A('### `.lean` files touched, `0` kernels built, `0` ferries edited, `0` prior banks edited,')
    A('### `0` keystones edited, `0` locked faces edited, `0` content lost.')
    A('### ### **NOTHING DEPOSITS.**')
    A('')
    A(SUB)
    A('### (9) THIS ACT’S OWN DEFECTS, PRINTED RATHER THAN SMOOTHED.')
    A(SUB)
    A('### ### **(1) THE REPAIR RE-FIRED ON THIS ACT’S OWN PRESERVED ORIGINAL.** ### The')
    A('### first version searched the WHOLE file for the target string. ### On the second run the')
    A('### only remaining occurrence was the original ### **QUOTED VERBATIM INSIDE THIS ACT’S')
    A('### ### OWN APPENDED BLOCK**, and the edit landed there -- caught by the arm that requires')
    A('### the claim to be otherwise word for word. ### ### **A BLOCK THAT PRESERVES A SENTENCE BY')
    A('### ### QUOTATION IS NOT A PLACE TO REPAIR IT** ### (b391’s preserved-block species,')
    A('### and b403’s re-banking from an already-edited file). ### The search is now scoped to')
    A('### the region BEFORE this act’s own mark, and both counts are printed.')
    A('### ### **(2) AN ANCHOR TYPED WITH `chr(10)` MISSED A FILE THAT PLAINLY CONTAINED IT.** ###')
    A('### `core.autocrlf` makes `FERRY_STANDING.md` ### **CRLF IN THE WORKING TREE WHILE ITS BLOB')
    A('### ### STAYS LF**, so the `A1` anchor -- a real sentence, present, readable -- did not')
    A('### match. ### The banked `powershell-bom-trap` species. ### The line ending is now DETECTED')
    A('### from the file and PRINTED, never assumed.')
    A('### ### **(3) A QUOTED HEREDOC COLLAPSED BACKSLASHES AND BROKE TWO PATCH SCRIPTS**, the')
    A('### banked `bash-heredoc-backslash` species, met twice more in this act. ### Both were')
    A('### redone through the editor instead.')
    A('### ### **(4) AND THE SEAT READ A STALE RUN RECORD THREE TIMES.** ### `run_clock` VERSIONS')
    A('### the desk notes, and the newest-by-mtime file was not the newest run; the seat read')
    A('### `HARD FAILURE` from an old record while the live run was passing. ### ### **AN')
    A('### ### ACT’S OWN RUN RECORD MUST BE READ FROM THE RUN, NOT FROM A DIRECTORY')
    A('### ### LISTING** -- and a versioning writer makes every `ls -t` a guess.')
    A('')
    A(SUB)
    A('### (10) WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It does not say a witness exists at any site, or that one can. ### **`(iii)`’S TWO')
    A('### ### CLAUSES ARE NAMED AND THEIR SATISFIABILITY IS `NOT ATTEMPTED`.**')
    A('### It does not say the record’s barrier-name and its repair-name are the same')
    A('### achievement. ### **ONE HAS A THEOREM AND A CLASSIFICATION; THE OTHER HAS A COROLLARY')
    A('### ### AND A NAME.**')
    A('### It does not mint a name, add a coordinate, rewrite an entry, strike a law, or bump a')
    A('### standing version.')
    A('### It does not repair a sentence about another object, a banked ferry, or a prior')
    A('### act’s bank.')
    A('### It types ### **NO BRIDGE** ### between any two of the six sites.')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### `h2` STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'wb').write((chr(10).join(B) + chr(10)).encode('utf-8'))
    rec('  bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))
    return len(B)


def main():
    bar('=')
    rec('b406 -- THE DESK, THE ONE REPAIR, THE TRAIL BLOCK, THE ROW, THE KEY, THE STANDING CLAUSE.')
    bar('=')
    bar()
    rec('  ### THE DESK UNDER (R7).')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### THE ONE REPAIR, IN PLACE, AGAINST THE PRE-ACT BLOB AT `HEAD`.')
    bar()
    rok, repaired = do_repair()
    if not rok:
        run_clock.write(D, 'b406_desk_notes', LINES)
        return 1

    rec()
    bar()
    rec('  ### THE TRAIL BLOCK, APPEND-ONLY, CARRYING THE ORIGINAL VERBATIM.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b405 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            run_clock.write(D, 'b406_desk_notes', LINES)
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_two_reasons': 'trivially satisfiable' in low,
        'says_i_belongs_to_iii': "which is site `(iii)`’s and not `(i)`’s" in low,
        'says_barrier': 'sieve ceiling lemma' in low,
        'says_escape_kind': 'escape-kind' in low,
        'says_repair': 'bright channel' in low,
        'says_not_equal': 'do not weigh the same' in low,
        'says_priced_not_added': 'priced and not added' in low,
        'says_not_attempted': 'not attempted' in low,
        'says_arity': 'four of five cannot answer a unary question' in low,
        'says_matcher': 'nothing to repair' in low,
        'says_ferries': '1 of 4' in low or 'three carry it' in low,
        'says_original_kept': 'kernel terminals `b329.*` (24, zero-axiom) and `b310.*`**.' in low,
        'says_no_version_bump': 'version line is not bumped' in low,
        'says_routed_second': 'routed to the author' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
        'says_h2': 'h2 where the deposit left it' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b406_desk_notes', LINES)
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)

    rec()
    bar()
    rec('  ### THE STANDING CLAUSE, APPENDED BY THE FILE’S OWN MECHANISM.')
    bar()
    sok = do_standing()
    if not sok:
        run_clock.write(D, 'b406_desk_notes', LINES)
        return 1

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
        run_clock.write(D, 'b406_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b406_desk_notes', LINES)
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
        write_bytes(TABLE, new)
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
            run_clock.write(D, 'b406_desk_notes', LINES)
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
    nb = bank(Q, rownum, kok, repaired, sok)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### REPAIRS %d. ### STANDING %s. ### ROW %d. '
        '### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], repaired, 'PASS' if sok else 'FAIL', rownum,
           'PASS' if kok else 'FAIL', nb))
    bar('=')
    run_clock.write(D, 'b406_desk_notes', LINES)
    return 0 if (kok and sok) else 1


if __name__ == '__main__':
    sys.exit(main())
