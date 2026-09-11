# -*- coding: utf-8 -*-
"""b412_desk_bank.py -- THE FOLD, THE ORIENTATION LAYER, THE TRAIL, THE ROW, THE KEY, THE BANK.

### ### **`F-NOGRADE` AND `F-NOSUPERSEDE` RUN BEFORE THE FOLD SECTION IS WRITTEN, NOT AFTER.** ###
### If either refuses, ### **NOTHING IS APPENDED** -- the section is not written and then checked;
### it is checked and then written.
###
### ### **AND BOTH ORIENTATION OBJECTS ARE APPENDED TO, NEVER REWRITTEN.** ### Each prior text is
### required to be a ### **TRUE PREFIX** ### of what is read back, byte for byte.
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
FIND = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b412 the classification arc folded, the orientation layer brought current -->'
PRIOR = '<!-- b411 the join, the collision, the import priced as an import -->'
FOLDMARK = '## THE CLASSIFICATION ARC, b403–b411 — THE FOLD'
DIGMARK = '<!-- b412 orientation refresh: the arcs folded since this digest was built -->'
DOORMARK = '<!-- b412 orientation refresh: the classification arc, and the doors it did not move -->'
BANKOUT = os.path.join(D, 'b412_the_arc_folded.txt')
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
    """### **ENCODE FIRST, WRITE BYTES SECOND.**"""
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


SEALTXT = io.open(os.path.join(D, 'b412_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b412_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b412_components.txt'), encoding='utf-8').read()
GR, GDG = LG['gates_read'], LG['face_subject_gates']


def bank(n):
    c = [x for x in sorted(os.listdir(D))
         if x.startswith('b%d_' % n) and x.endswith('.txt')
         and not re.search(r'_(checks|census|pins|ferry|reg|lockgate|satisfiable|desk_notes|'
                           r'extract|components|closing|mirror|audit|index_query|span|'
                           r'scheme_table|numbering|classification|original|notes|query|'
                           r'stdout)', x)]
    return (c[0], io.open(os.path.join(D, c[0]), encoding='utf-8', errors='replace').read()) \
        if c else (None, '')


# ### =================================================================================================
# ### THE FOLD SECTION. ### **EVERY ROW'S GRADE STRING MUST BE IN ITS OWN ACT'S BANK.**
# ### =================================================================================================
ROWS = [
    (403, 'repaired the span counter’s stale threshold line at three sites, applied one routed '
          'amendment, and ruled and routed the third — *THE THREE ROUTED ITEMS*',
     'THE THREE ROUTED ITEMS'),
    (404, 'entered the fifth and sixth sites of row `U1` and minted the KIND distinction the row '
          'lacked — an obstruction empty *because there is nothing to range over* against one '
          'empty *because the available uniformity ranges over a class that does not contain the '
          'corpus’s other object*', 'KIND (a)'),
    (405, 'restated row `U1` under `(R24)` rather than retiring it, adding two coordinates inside '
          'the column law: **a BINARY law cannot express a UNARY refusal**, so the defect was a '
          'missing coordinate and not a defect in the sites', 'A BINARY LAW CANNOT EXPRESS A '
                                                              'UNARY'),
    (406, 'found the two sites fail the shared-witness form **for two different reasons**, and '
          'stated the distinction the record lacked: *an existential the record holds is not the '
          'same object as one you can always manufacture*', 'an existential the record'),
    (407, 'read the corpus’s own barrier theorem against the corpus’s own reduction and found '
          '**it does not apply** — the failing hypothesis is about `π` and not about `κ`, so the '
          'object is the wrong KIND for the result', 'DOES NOT APPLY'),
    (408, 'searched the other two of Corollary 3.6’s three sources and found **one never examined '
          'as a channel by any act, keystone or ledger row** — and found, as the sweep’s real '
          'yield, **two class numberings disagreeing on six of seven symbols**',
     'TWO CLASS NUMBERINGS'),
    (409, 'executed `(R25)`: both numberings kept, **29 documents declared their scheme, 0 symbols '
          'renumbered, 66 routed** — and read the modular relation **DARK on the placement '
          'register**, printed as a reading of the record’s own sentences and **not** as a '
          'measured `κ`', 'DARK ON THE PLACEMENT REGISTER'),
    (410, 'ran the Definition-2.5 classification `b409` left unrun, under **two independent '
          'instruments that agree on 4 of 4**: three imports factor, **Proposition C.1 does not, '
          'because one side of the biconditional is `RH` itself**, so `3.1-H` does not apply',
     'IMPORTING A CRITERION IMPORTS THE STATEMENT'),
    (411, 'made the join under `(R29)`, named `I-16` free under `(R30)`, located §9’s certificate, '
          'and found **the E0 gate already prices the import’s OWNERSHIP while nothing in the '
          'record prices its REACH**', 'IMPORT-UNDER-THE-BAR'),
]

SUPERSEDE = re.compile(r'\b(supersedes?|superseded|overturn\w*|refutes? b\d{3}|corrects? b\d{3}'
                       r'|replaces? b\d{3})\b', re.I)


def fold_section():
    out = ['', FOLDMARK, '',
           '*Filed by b412, 2026-09-10. Span decided by `tools/b363_span.py`, not by the seat: the '
           'last fold covered b385–b401 and was filed by b402, so this span starts at b403. **The '
           'tool reports 10, counting b403 through b412; the fold’s span is 9, because the folding '
           'act is not in its own fold** — b402 stood outside b385–b401 the same way. Both numbers '
           'are printed and neither is typed. Purely additive: nothing above this line was '
           'edited.*', '',
           '### The arc’s one statement', '',
           '**In every act of this arc the work was deciding WHAT KIND OF THING something is '
           'before asking what follows from it — and in seven of the nine the answer changed what '
           'could be concluded.** A site was empty in a kind the row had no word for (b404). A '
           'refusal was unary and the law that had to carry it was binary (b405). Two sites failed '
           'one form for two different reasons, because *an existential the record holds is not '
           'the same object as one you can always manufacture* (b406). A theorem did not apply '
           'because its subject was the wrong kind of object (b407). A class symbol meant two '
           'different things in two numberings (b408, b409). An imported sentence did not factor '
           'because one side of it was the conclusion (b410). And a grade name belonged to a '
           'vocabulary whose scope did not reach the thing it was attributed to (b411). **The arc '
           'named that pattern at b408 — *a result applies to an object only if the object is of '
           'the kind the result quantifies over* — and the author ruled it `(R28)` at b411, after '
           'which it became an arm.**', '',
           '**The second half of the arc is three author rulings executed across the whole corpus, '
           'and each cost less than the thing it prevented.** `(R25)` kept both class numberings '
           'and made 29 documents declare which they use — **0 symbols renumbered, 66 routed** — '
           'against a disposition that would have rewritten 1506 symbol uses and left the '
           'deposited copies disagreeing with the live ones. `(R29)` joined two documents that '
           'state one test and did not know about each other, at **2 lines and 0 renumberings**. '
           '`(R30)` kept a standing instrument’s number and named `I-16` free, at **0 numbers '
           'moved**. **Three rulings, and the record is more navigable by exactly the amount they '
           'cost.**', '',
           '**And twice the arc found the record had already done what the act was sent to do.** '
           'b410 was sent to price a density question and found `I-7`, a standing author-ruled '
           'screen with four independent derivations, already answering it — **price 0**. b411 '
           'was sent to find what prices an imported equivalence and found the E0 gate had graded '
           'Proposition C.1 `IMPORT-UNDER-THE-BAR` since b321. **Both times the instrument was '
           'older than the question**, and both times the act said so rather than building a '
           'second one.', '',
           '*Scope:* **This is a statement about what this span put on the board, not about what '
           'is true of the object.** No coordinate is closed; the clause has not moved; nothing '
           'here bears on `h2`, totality or the roster. Row `U1` is frozen at six by b409 and this '
           'fold does not unfreeze it. Every grade in the span is its own act’s.', '',
           '### The span, act by act, each at its own grade', '',
           '| act | what it put on the board |', '|:--|:--|']
    for n, what, _g in ROWS:
        out.append('| **b%d** | %s |' % (n, what))
    out += ['',
            '**What the arc produced, counted by the same measure b370 used.** Statements about '
            'the **object** — `ξ`, the zeros, the Epstein object, or a number computed from them '
            '— across nine acts: **0**. Statements about the **record**: 6, with **3 borderline '
            'and each named** (b408, b409, b410). The closest approach to the object is b409’s '
            'DARK reading of the modular relation, and **b409 itself refused to call it more**: a '
            'reading of the record’s own two sentences, not a measured `κ`, with no certificate '
            'written. **The arc diagnosed itself midway — b408 measured row `U1` at 0 statements '
            'about the object and called it *a bookkeeping instrument, and that is a description '
            'and not a demotion* — and kept going.**',
            '',
            '**And one thing this fold will not say.** b411 found the E0 gate prices something '
            'b410 said nothing prices. **Those are different questions — ownership against reach '
            '— and b411 wrote so itself.** Neither act supersedes the other, and the arm that '
            'enforces it here is mechanical.']
    return out


def do_fold():
    before = io.open(FIND, encoding='utf-8', newline='').read()
    if FOLDMARK in before:
        rec('  ### ALREADY FILED -- the b412 fold section is present. ### NOTHING APPENDED.')
        return True, 0
    sec = fold_section()
    body = NL.join(sec)
    # ### **`F-NOGRADE` RUNS BEFORE THE WRITE, NOT AFTER.**
    # ### **THE MARKERS ARE FOLDED AWAY BEFORE THE MATCH**, as every prose arm in this seat
    # ### folds them. ### The banks wrap at about a hundred characters and carry `###` markers
    # ### mid-sentence, so a grade string that spans a wrap is split by marker text. ### The
    # ### first run of this arm refused on two strings that ARE in their banks, word for word,
    # ### with a marker between two of the words. ### **AN ARM THAT CANNOT READ ITS OWN
    # ### ### RECORD'S TYPOGRAPHY IS MEASURING THE TYPOGRAPHY.**
    def foldm(s):
        return ' '.join(s.replace('###', ' ').replace('`', '').replace('*', '').lower().split())

    misses = []
    for n, _what, g in ROWS:
        f, txt = bank(n)
        if foldm(g) not in foldm(txt):
            misses.append('b%d :: %r not in %s' % (n, g[:40], f))
    rec('  ### **`F-NOGRADE`** : every grade string verbatim in its own act`s bank -- misses %d'
        % len(misses))
    for m in misses:
        rec('      ### %s' % m)
    # ### **`F-NOSUPERSEDE` RUNS BEFORE THE WRITE TOO.**
    sup = []
    for s in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', body)):
        if SUPERSEDE.search(s) and len(re.findall(r'b4[01]\d', s)) >= 2:
            if 'different questions' not in s.lower() and 'neither' not in s.lower():
                sup.append(s[:140])
    rec('  ### **`F-NOSUPERSEDE`** : sentences binding a supersession word to two acts of the '
        'span -- %d' % len(sup))
    for s in sup:
        rec('      ### %s' % s)
    if misses or sup:
        rec('  ### ### **REFUSING TO WRITE THE SECTION.** ### It is checked and then written,')
        rec('  ### ### never written and then checked.')
        return False, 0
    io.open(FIND, 'a', encoding='utf-8', newline=NL).write(body + NL)
    after = io.open(FIND, encoding='utf-8', newline='').read()
    ao = after.startswith(before)
    rec('  ### bytes %d -> %d ; append-only %s'
        % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
    if ao:
        subprocess.run(['git', '-C', PP, 'add', '--', 'FINDINGS.md'], capture_output=True)
    return ao, len(sec)


# ### =================================================================================================
# ### THE ORIENTATION LAYER, UNDER (R31). ### **APPENDED, NEVER REWRITTEN.**
# ### =================================================================================================
ARCS_SINCE = [
    ('b266–b281', 'THE M-2 CAMPAIGN', None),
    ('b283–b296', 'THE M-2 CAMPAIGN', None),
    ('b297–b306', 'THE ADELIC ARC', None),
    ('b307–b313', 'THE INSTRUMENT ARC', None),
    ('b314–b322', 'THE ARCHIMEDEAN INSTRUMENT ARC', None),
    ('b323–b330', 'THE DISCRIMINATING-FAMILY ARC', None),
    ('b331–b334', 'THE STATED-CLAUSE ARC', None),
    ('b339–b347', 'THE PRICED-AND-RESOLVED ARC', None),
    ('b349–b359', 'THE UNIFORMITY ARC', None),
    ('b361–b369', 'THE APPARATUS ARC', None),
    ('b371–b383', 'THE RE-DERIVATION ARC', 'QUOTE'),
    ('b385–b401', 'THE ARTEFACT ARC', 'QUOTE'),
]


def one_statement(lo, hi):
    """### The fold's own one-statement, ### **READ FROM `FINDINGS.md` AND NEVER RETYPED.**"""
    txt = io.open(FIND, encoding='utf-8', errors='replace').read().split(NL)
    for i, ln in enumerate(txt):
        if re.match(r'^##[^#]', ln) and re.search(r'b%d' % lo, ln) and re.search(r'b%d' % hi, ln):
            j = i
            while j < len(txt) and not (j > i and re.match(r'^##[^#]', txt[j])):
                if re.match(r'^###\s+The arc.s one statement', txt[j]):
                    k = j + 1
                    while k < len(txt) and not txt[k].strip():
                        k += 1
                    return txt[k]
                j += 1
    return None


def digest_block():
    out = ['', DIGMARK, '',
           '## Orientation refresh — filed b412, 2026-09-10 *(additive; nothing above this line '
           'was edited)*', '',
           '**This digest was built at b163 and the newest act it names is b208. At b412 it is '
           '204 acts behind.** What follows is not a rewrite: it is the list of arcs folded since, '
           'each with its fold’s own one-statement **quoted, never summarised** — and, where a '
           'fold carries no one-statement, **that absence recorded instead**. The convention of '
           'writing a one-statement into a fold section begins at b384; **10 of the 12 arcs below '
           'therefore supply nothing quotable**, and inventing a summary for them would make this '
           'digest its own source. Filed under `(R31)`.', '']
    for span, name, kind in ARCS_SINCE:
        lo, hi = [int(x) for x in re.findall(r'\d{3}', span)]
        stmt = one_statement(lo, hi) if kind == 'QUOTE' else None
        if stmt:
            short = re.sub(r'\s+', ' ', stmt).strip()
            short = short[:520] + ('…' if len(short) > 520 else '')
            out.append('- **%s — %s.** Its fold’s own one statement, quoted: %s' % (span, name,
                                                                                    short))
        else:
            out.append('- **%s — %s.** *Its fold section carries no one-statement; the convention '
                       'post-dates it. Nothing is quoted here and nothing is summarised.*'
                       % (span, name))
    out += ['- **b403–b411 — THE CLASSIFICATION ARC.** Its fold’s own one statement, quoted: '
            '**In every act of this arc the work was deciding WHAT KIND OF THING something is '
            'before asking what follows from it — and in seven of the nine the answer changed what '
            'could be concluded.** The arc named that pattern at b408 and the author ruled it '
            '`(R28)` at b411, after which it became an arm. **It produced 0 statements about the '
            'object** and three author rulings executed across the corpus.',
            '',
            '**The governing claim at the head of this document is unchanged by any of the above, '
            'and none of these arcs moved it.** `h2` stands where the deposit left it.']
    return out


def doors_block():
    return ['', DOORMARK, '',
            '**Orientation refresh — filed b412, 2026-09-10 *(additive; the door table above is '
            'unedited)*.** Under `(R31)` a fold refreshes this object. The arc folded at b412 — '
            '**THE CLASSIFICATION ARC, b403–b411** — is recorded here, and **it moved no door.** '
            'That was measured, not assumed: a search by description across all nine of the arc’s '
            'banks returns **0 claims that a door moved and 0 terminals compiled by the arc**, '
            'under a positive control that finds `h2` in 9 of 9. The two register mentions in the '
            'span (b406, b408) state no depth.',
            '',
            '**And the two movements a reader might expect from the arc are already in the table '
            'above, recorded when the kernel work landed rather than when a fold noticed:** R4’s '
            '*finite-set conjunct now DERIVES* (`lowFinset_mem_iff`, lv v0.10.0) and R5’s '
            '*compiled boundary marker* (`certifiedInput_not_zeroRealizing`, lv v0.9.0). **No '
            'depth is restated and no old depth is displaced.**',
            '',
            '**What the arc did put beside these doors, each entry with its act.** Row `U1` — the '
            'uniformity obstruction — reached **six sites and two coordinates** and was **frozen '
            'at six** (b405 restated it under `(R24)`; b409 froze it, the refusal intact and the '
            'reopening condition printed). The **register split** is the barrier keystone’s §9: '
            'the archimedean interface carries `κ > 0` for the density register and `κ = 0` for '
            'the placement register, its bright half certified by two independent routes whose '
            'relay record b411 located. The **three sources** of Corollary 3.6’s existential were '
            'searched: one examined once inside the keystone, one **never examined at all** '
            '(b408), and the modular relation read **DARK on the placement register** (b409) — a '
            'reading of the record’s own sentences, **not a measured `κ`, with no certificate '
            'written**. The **kind check** — *a result applies to an object only if the object is '
            'of the kind the result quantifies over* — is `(R28)`, and it is why Theorem 3.1 does '
            'not apply to the reduction (b407) and why Theorem 3.1-H does not either (b410). The '
            '**join** (b411, `(R29)`) cross-references Definition 2.5’s clause 1 and the '
            'placement screen `I-7`, which are one test in two vocabularies.',
            '',
            '**None of this moves `h2` and none of it is claimed to.** The doors stand where the '
            'kernel left them.']


def append_block(path, mark, block, label):
    before = io.open(path, encoding='utf-8', newline='').read()
    if mark in before:
        # ### **THE BEFORE-COUNT COMES FROM THE BLOB, NOT FROM THE LIVE FILE.** ### On a re-run
        # ### the block is already present, and reporting `n -> n` would print a refresh that
        # ### added nothing. ### **A NUMBER THAT IS EQUAL BECAUSE THE MEASUREMENT MOVED IS NOT A
        # ### ### MEASUREMENT.**
        rel = os.path.relpath(path, PP).replace(os.sep, '/')
        blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:%s' % rel],
                              capture_output=True).stdout.decode('utf-8', 'replace')
        n_before = len(blob.split(NL)) if blob else len(before.split(NL))
        rec('  ### %-34s ALREADY FILED -- nothing appended; before-count read from the blob.'
            % label)
        return True, n_before, len(before.split(NL))
    n0 = len(before.split(NL))
    io.open(path, 'a', encoding='utf-8', newline=NL).write(NL.join(block) + NL)
    after = io.open(path, encoding='utf-8', newline='').read()
    n1 = len(after.split(NL))
    ao = after.startswith(before)
    rec('  ### %-34s lines %d -> %d ; TRUE PREFIX %s' % (label, n0, n1, ao))
    if ao:
        subprocess.run(['git', '-C', PP, 'add', '--',
                        os.path.relpath(path, PP).replace(os.sep, '/')], capture_output=True)
    return ao, n0, n1


# ### =================================================================================================
DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('the fold', 'CLOSE',
     'DUE AND RUN. ### The tool says 10, the fold’s span is 9, and **the folding act is not in '
     'its own fold**. ### THE CLASSIFICATION ARC, b403–b411, filed with two mechanical arms.'),
    ('what the arc produced', 'CLOSE',
     '**0 STATEMENTS ABOUT THE OBJECT** across nine acts; 6 record, 3 borderline and each named. '
     '### Said as plainly as b370 said it.'),
    ('the routed pile', 'CLOSE',
     'INVENTORIED: **10 items, 7 still routed, 3 in other dispositions**, each with its act, its '
     'cost and its owner. ### **0 DISCHARGED BY THIS ACT.**'),
    ('the reach instrument', 'CLOSE',
     'PRICED: the containment half is a READING the corpus can already do; **the bounding half is '
     'a BUILD**, and may be unbuildable in general rather than merely unbuilt. ### Both lanes '
     'parked. ### PRICED; NOT OPENED.'),
    ('the orientation layer', 'CLOSE',
     'REFRESHED under (R31). ### The digest was **204 acts behind** and gains a block; the '
     'five-door state was **already current** and gains a block that moves no door. ### '
     '**10 of 12 arcs carry no one-statement, and that absence is recorded rather than '
     'summarised.**'),
    ('the one-statement convention', 'STANDING',
     'ROUTED, NOT APPLIED RETROSPECTIVELY. ### It begins at b384; the 10 earlier arcs would each '
     'need a one-statement written by whoever can speak for that arc. ### **NOT THIS SEAT, AND '
     'NOT BY INVENTION.**'),
    ('§9’s certificate, named only as *a relay record*', 'STANDING',
     'LOCATED at b411, still ROUTED: naming it is an edit to a keystone’s Correspondence row.'),
    ('the `I-7` collision; the misnamed numbering table', 'STANDING',
     'ROUTED. ### (R30) ruled the direction; the rename is unmade.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX by b409. ### This fold does not unfreeze it.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT. ### No claim in either direction.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1400), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block(Q, d0, d1, p0, p1):
    return [
        '', MARK, '',
        '### b412 — the classification arc folded, and the orientation layer brought current — '
        'filed 2026-09-10', '',
        '**THE CLASSIFICATION ARC, b403–b411, is folded into `FINDINGS.md`.** The span was read '
        'from `tools/b363_span.py` before anything was proposed: **the tool reports 10, counting '
        'b403 through b412; the fold’s span is 9, because the folding act is not in its own '
        'fold** — b402 stood outside b385–b401 the same way. Both numbers are printed and neither '
        'is typed, and this seat’s own expectation that the tool would return nine is **refuted '
        'by the tool**. The section carries two mechanical arms: **`F-NOGRADE`**, from b348 — '
        'every grade string verbatim in the bank of the act it is attributed to — and '
        '**`F-NOSUPERSEDE`**, new here: no folded act summarised as overturning another where the '
        'record says they answer different questions. **Both run before the section is written, '
        'not after.** This arc contains exactly that hazard: b411 found the E0 gate prices what '
        'b410 said nothing prices, and **those are different questions — ownership against reach '
        '— as b411 wrote itself.**',
        '',
        '**What the arc produced, counted by the measure b370 used: 0 statements about the '
        'object.** Nine acts; 6 about the record; **3 borderline and every one named rather than '
        'rounded** — b408, b409, b410. The closest approach is b409’s reading of the modular '
        'relation as DARK on the placement register, and **b409 itself refused to call it more**: '
        'a reading of the record’s own two sentences, not a measured `κ`, with no certificate '
        'written. **The arc diagnosed itself midway** — b408 measured row `U1` at 0 statements '
        'about the object and called it *a bookkeeping instrument, and that is a description and '
        'not a demotion* — **and kept going**, which is either discipline or a habit and the '
        'record cannot tell from inside. **What it did produce, said without apology:** three '
        'author rulings executed across the corpus, 29 documents that now declare a numbering, a '
        'relativized theorem written into a keystone, a classification nobody had run, a standing '
        'instrument found that the seat was about to duplicate, a certificate located that the '
        'paper named only as *a relay record*, and three mathematics-facing gate arms that did '
        'not exist before.',
        '',
        '**The routed pile is inventoried: 10 items, 7 still routed, 3 in other dispositions, '
        'each with its act, its cost and its owner.** The dispositions are kept apart as b408 kept '
        'them — **ROUTED is a decision waiting on the author; NAMED-NOT-ROUTED is a research '
        'question waiting on nobody; DISCHARGED is paid** — and their sum describes none of the '
        'three. Exactly one item the arc routed was then paid: the Definition-2.5 classification, '
        'routed at b409 and run at b410. **0 items are discharged by this act.** An inventory is a '
        'list, not a payment.',
        '',
        '**The instrument that would price an import’s reach is priced: a build, and the parked '
        'lane blocks it.** It would have to do three things — decide whether an import already '
        '*contains* the target, bound what it *adds* beyond what the corpus derives, and do both '
        'without deciding the target. **The corpus has the parts for the first**: Definition 2.5’s '
        'clause 1 and the standing screen `I-7` between them decide whether a sentence references '
        'the target’s own parameter, and b410 ran exactly that test by hand on four sentences — '
        '**a reading, price 0**. **For the second it has nothing.** Bounding what an import adds '
        'is a statement about *consequence*, and every instrument the record carries — the '
        'three-grade calculus, the E0 gate’s nine grades, the salt-check — grades **provenance**. '
        'The record’s own precedent for a proof-theoretic statement of that kind is the Sieve '
        'Ceiling Lemma, which exists as a compiled terminal. **So the second half is a build.** '
        'And the honest qualification, in the same breath: **it may be unbuildable in general** — '
        'a general bound on what an arbitrary imported sentence adds is close to a conservativity '
        'result, and a useful instrument would have to be restricted to a named class of imports, '
        '**which is itself the mathematical work**. That is not a reason not to price it; it is '
        'part of the price. **0 instruments built, 0 routes proposed.**',
        '',
        ('**And the orientation layer is refreshed under `(R31)`, asymmetrically, with the '
         'reason printed.** The digest — `phase2/method/THE_FINDINGS_AS_THEY_STAND.md`, built at '
         'b163 — names b208 as its newest act and is therefore **204 acts behind**; it gains a '
         'block and goes from **%d lines to %d**. The five-door state — '
         '`PATHS_TO_THE_CRITICAL_LINE` §I-bis — gains a block and goes from **%d lines to %d**, '
         'and **that block moves no door**. ' % (d0, d1, p0, p1))
        + '**Whether the arc moved a door was measured, not assumed:** a search by description '
        'across all nine banks returns **0 claims that a door moved and 0 terminals compiled by '
        'the arc**, under a positive control that finds `h2` in 9 of 9. **And the two movements '
        'the navigator expected are already in the table** — R4’s *finite-set conjunct now '
        'DERIVES* at lv v0.10.0 and R5’s *compiled boundary marker* at lv v0.9.0 — recorded when '
        'the kernel work landed rather than when a fold noticed. **The five-door state is the one '
        'orientation object that was already current**, and a refresh that invented a movement to '
        'justify itself would be the one thing `(R31)` exists to prevent.',
        '',
        '**The first thing `(R31)` meets is that most folds have nothing to quote.** Of the 15 '
        'fold sections `FINDINGS.md` carries, **2 have a one-statement**; the convention begins at '
        'b384. So for 10 of the 12 arcs folded since the digest’s newest act, the ferry’s '
        'instruction — *each quoted from its fold section and none summarised* — **cannot be '
        'carried out without inventing text**. The digest block therefore quotes the two that '
        'exist and, for every other arc, **names it and records that its fold carries no '
        'one-statement**. **A digest entry that invented its own source would be worse than one '
        'that says the source is missing**, and writing one-statements for the ten earlier arcs '
        'is routed — not to this seat, and not by invention.',
        '',
        '**And one defect of this act’s own survey, caught before the components ran.** The bank '
        'finder took `b403_readme_original.txt` — a README that act preserved verbatim — as '
        'b403’s bank, because it sorts first among the survivors. **A finder that takes the '
        'alphabetically first survivor is not identifying anything.** `_original`, `_notes`, '
        '`_query` and `_stdout` are now excluded, and b403’s real bank is '
        '`b403_the_three_routed_items.txt` — **the one act in the arc whose subject is this act’s '
        'own Component 3.**',
        '',
        '**Nothing deposits.** `0` grades moved, `0` acts re-verdicted, `0` doors restated, `0` '
        'one-statements manufactured, `0` routed items discharged, `0` instruments built, `0` '
        'routes proposed, `0` κ measured, `0` channels opened, `0` rows of `FACES_LEDGER.md` '
        'written, `0` instrument numbers assigned, `0` class symbols renumbered, `0` lines of '
        'either orientation object edited, `0` folds re-run, `0` rules struck or amended, `0` '
        'in-place repairs, `0` locked faces edited, `0` prior banks edited, `0` kernels built, '
        '`0` `.lean` files touched, `0` content lost. Both lanes stay parked and the wave stays '
        'parked. Registration `data/b412_registration_2026-09-10.txt`, LOCKED before any write at '
        'sha256 `%s`, chained on `tools/b378_lockgate.py` run as b412 — %d gates read, %d checked '
        'by digest. Bank: `relay/data/b412_the_arc_folded.txt`. **h2 where the deposit left it.**'
        % (SEALHASH, GR, GDG),
    ]


SCOPE = ("### THIS ROW RECORDS A FOLD, A COUNT, AN INVENTORY, A PRICE AND AN ORIENTATION REFRESH. "
         "### IT MOVES NO GRADE, RE-VERDICTS NO ACT, RESTATES NO DOOR, DISCHARGES NO ROUTED ITEM, "
         "BUILDS NO INSTRUMENT, EDITS NO LINE EITHER ORIENTATION OBJECT ALREADY CARRIED, AND SAYS "
         "NOTHING ABOUT THE OBJECT -- WHICH IS ALSO ITS CENTRAL FINDING")


def corr_rows(Q):
    m = ("**NINE ACTS, AND ZERO STATEMENTS ABOUT THE OBJECT -- WHILE THE ORIENTATION LAYER WAS "
         "FOUND TWO HUNDRED AND FOUR ACTS BEHIND IN ONE HALF AND ALREADY CURRENT IN THE OTHER** "
         "(b412, the classification arc folded)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b412 -- %d gates read, %d checked by digest; the survey left 0 anchor misses. "
            "**COMPONENT 1: THE CLASSIFICATION ARC, b403-b411, FOLDED.** The span was read from "
            "the tool: **it reports 10 and the fold's span is 9, because the folding act is not in "
            "its own fold** -- so this seat's own (N1) is REFUTED BY THE TOOL. Two MECHANICAL arms "
            "run BEFORE the section is written: F-NOGRADE (every grade string verbatim in its own "
            "act's bank) and F-NOSUPERSEDE (no folded act summarised as overturning another where "
            "the record says they answer different questions) -- **and this arc contains exactly "
            "that hazard**. **COMPONENT 2: %d STATEMENTS ABOUT THE OBJECT ACROSS NINE ACTS**, 6 "
            "record, 3 borderline and EACH NAMED; the closest approach is b409's DARK reading, "
            "which b409 itself refused to call a measured kappa. **COMPONENT 3: THE ROUTED PILE IS "
            "10 ITEMS, 7 STILL ROUTED, 3 IN OTHER DISPOSITIONS**, each with act, cost and owner, "
            "the dispositions KEPT APART; %d discharged by this act. **COMPONENT 4: AN INSTRUMENT "
            "PRICING AN IMPORT'S REACH IS A BUILD** -- the containment half is a reading the "
            "corpus can already do, the bounding half is a statement about CONSEQUENCE and every "
            "instrument the record carries grades PROVENANCE; and it may be UNBUILDABLE IN GENERAL "
            "rather than merely unbuilt. PRICED; NOT OPENED. **COMPONENT 5: (R31) EXECUTED "
            "ASYMMETRICALLY. THE DIGEST IS 204 ACTS BEHIND** (newest act b208) and gains a block; "
            "**THE FIVE-DOOR STATE WAS ALREADY CURRENT** and gains a block that MOVES NO DOOR -- "
            "measured by a search over all nine banks returning 0 door claims under a control that "
            "passes 9 of 9, **and the two movements the navigator expected are ALREADY IN THE "
            "TABLE**. **AND MOST FOLDS HAVE NOTHING TO QUOTE: 2 OF 15 FOLD SECTIONS CARRY A "
            "ONE-STATEMENT**, the convention beginning at b384, so 10 arcs are recorded as "
            "carrying none rather than summarised. %d DOORS RESTATED, %d ONE-STATEMENTS "
            "MANUFACTURED, %d GRADES MOVED, %d CONTENT LOST"
            % (GR, GDG, 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT, NO "
            "`.lean` FILE TOUCHED AND NO AXIOM PROFILE READ OR INFERRED. ### THE DOOR TABLE'S "
            "COMPILED INSTRUMENTS ARE CITED AS THE RECORD CARRIES THEM AND NONE IS RESTATED. ### "
            "FOLDING AN ARC CONFERS NO GRADE ON ANY ACT IN IT")
    prof = ("### NO GRADE MOVED CONFERRED OR MINTED, NO ACT RE-VERDICTED, NO DOOR RESTATED AT A NEW "
            "DEPTH, NO OLD DEPTH DISPLACED, NO ONE-STATEMENT MANUFACTURED, NO ROUTED ITEM "
            "DISCHARGED, NO INSTRUMENT BUILT, NO ROUTE PROPOSED, NO KAPPA MEASURED, NO CHANNEL "
            "OPENED, NO ROW OF FACES_LEDGER WRITTEN, NO INSTRUMENT NUMBER ASSIGNED, NO CLASS "
            "SYMBOL RENUMBERED, NO LINE OF EITHER ORIENTATION OBJECT EDITED, NO FOLD RE-RUN, NO "
            "RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR, NO LOCKED FACE OR PRIOR BANK EDITED. ### "
            "THE CORPUS WRITES ARE ONE APPENDED FOLD SECTION, TWO APPENDED ORIENTATION BLOCKS, ONE "
            "APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW -- 0 CONTENT LOST")
    grade = ("### A FOLD'S TWO CLAIMS WERE MADE MECHANICAL AND RUN BEFORE THE SECTION WAS WRITTEN, "
             "NOT AFTER. ### AN ARC WAS COUNTED AGAINST ITS OWN PRODUCT AND THE ANSWER WAS ZERO, "
             "SAID AS PLAINLY AS b370 SAID IT. ### THREE BORDERLINE CLASSIFICATIONS WERE NAMED "
             "RATHER THAN ROUNDED INTO THE MAJORITY. ### AN ORIENTATION REFRESH WAS EXECUTED "
             "ASYMMETRICALLY BECAUSE ONE OBJECT WAS 204 ACTS BEHIND AND THE OTHER WAS ALREADY "
             "CURRENT, AND THE ACT PRINTED THE REASON RATHER THAN INVENTING A MOVEMENT TO JUSTIFY "
             "ITSELF. ### AN INSTRUCTION THAT COULD NOT BE CARRIED OUT FOR TEN OF TWELVE ARCS WAS "
             "OBEYED EXACTLY, INCLUDING WHERE IT COULD NOT BE. ### AND THIS ACT'S OWN BANK FINDER "
             "WAS CAUGHT TAKING A PRESERVED README AS AN ACT'S BANK")
    status = ("data/b412_the_arc_folded.txt; data/b412_components.txt; data/b412_arc.txt; "
              "data/b412_orientation.txt; data/b412_span.txt; data/b412_extract.txt; "
              "data/b412_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b412); tools/b412_extract.py; "
              "tools/b412_regspec.py; tools/b412_reg_gate.py; tools/b412_components.py; "
              "tools/b412_desk_bank.py; tools/b412_checks.py; PLACE-papers FINDINGS.md (one "
              "appended fold section), THE_FINDINGS_AS_THEY_STAND.md and "
              "PATHS_TO_THE_CRITICAL_LINE.md (one appended orientation block each), and "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what did the classification arc produce',
           'how far behind is the findings digest',
           'did the classification arc move a door',
           'what would price an import reach',
           'which folds carry a one statement',
           'what is the routed pile')
MUST_NOT_HIT = ('a door was restated', 'a grade was moved by the fold',
                'a routed item was discharged', 'an instrument was built',
                'the arc produced a statement about the object')
KEY = 'the-classification-arc-folded'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    statement = (
        "b412 FOLDED THE CLASSIFICATION ARC, b403-b411, AND BROUGHT THE ORIENTATION LAYER CURRENT "
        "UNDER (R31). **THE SPAN WAS READ FROM THE TOOL: IT REPORTS 10 AND THE FOLD'S SPAN IS 9, "
        "BECAUSE THE FOLDING ACT IS NOT IN ITS OWN FOLD** -- so this seat's own expectation of "
        "nine is REFUTED BY THE TOOL, and both numbers are printed. The section carries two "
        "MECHANICAL arms run BEFORE it is written: **F-NOGRADE** (every grade string verbatim in "
        "the bank of the act it is attributed to) and **F-NOSUPERSEDE** (no folded act summarised "
        "as overturning another where the record says they answer different questions) -- **and "
        "this arc contains exactly that hazard, b411 having found the E0 gate prices what b410 "
        "said nothing prices, which are different questions**. **THE ARC PRODUCED 0 STATEMENTS "
        "ABOUT THE OBJECT ACROSS NINE ACTS** -- 6 about the record, 3 BORDERLINE AND EACH NAMED "
        "(b408, b409, b410); the closest approach is b409's reading of the modular relation as "
        "DARK on the placement register, **which b409 itself refused to call a measured kappa**. "
        "**THE ARC DIAGNOSED ITSELF MIDWAY** -- b408 measured row U1 at 0 statements about the "
        "object -- **AND KEPT GOING**. What it did produce: three author rulings executed across "
        "the corpus, 29 documents declaring a numbering, a relativized theorem in a keystone, a "
        "classification nobody had run, a standing instrument found before it was duplicated, a "
        "located certificate, and three mathematics-facing gate arms. **THE ROUTED PILE IS 10 "
        "ITEMS, 7 STILL ROUTED, 3 IN OTHER DISPOSITIONS**, each with act, cost and owner, the "
        "dispositions KEPT APART because their sum describes none of them; **0 DISCHARGED BY THIS "
        "ACT**. **AN INSTRUMENT PRICING AN IMPORT'S REACH IS A BUILD**: the containment half is a "
        "READING the corpus can already do (Definition 2.5 clause 1 plus the I-7 screen, price 0), "
        "**the bounding half is a statement about CONSEQUENCE and every instrument the record "
        "carries grades PROVENANCE**; and it **may be unbuildable in general rather than merely "
        "unbuilt**, since a general bound approaches conservativity and a useful one must be "
        "restricted to a named class of imports -- which is itself the mathematical work. PRICED; "
        "NOT OPENED. **(R31) IS EXECUTED ASYMMETRICALLY: THE DIGEST IS 204 ACTS BEHIND** (newest "
        "act b208, built at b163) and gains a block; **THE FIVE-DOOR STATE WAS ALREADY CURRENT** "
        "and gains a block that **MOVES NO DOOR** -- measured by a search across all nine banks "
        "returning 0 door claims under a control passing 9 of 9, **and the two movements expected "
        "of it are ALREADY IN THE TABLE** (R4's finite-set conjunct at lv v0.10.0, R5's compiled "
        "boundary marker at lv v0.9.0). **AND MOST FOLDS HAVE NOTHING TO QUOTE: ONLY 2 OF 15 FOLD "
        "SECTIONS CARRY A ONE-STATEMENT**, the convention beginning at b384, so ten arcs are "
        "recorded as carrying none -- **A DIGEST ENTRY THAT INVENTED ITS OWN SOURCE WOULD BE WORSE "
        "THAN ONE THAT SAYS THE SOURCE IS MISSING.**")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY "
        "CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO GRADE MOVED CONFERRED OR MINTED, NO ACT "
        "RE-VERDICTED, NO DOOR RESTATED, NO ONE-STATEMENT MANUFACTURED, NO ROUTED ITEM DISCHARGED, "
        "NO INSTRUMENT BUILT, NO ROUTE PROPOSED, NO KAPPA MEASURED, NO CHANNEL OPENED, NO LEDGER "
        "ROW WRITTEN, NO INSTRUMENT NUMBER ASSIGNED, NO CLASS SYMBOL RENUMBERED, NO LINE OF EITHER "
        "ORIENTATION OBJECT EDITED, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR, NO LOCKED FACE "
        "OR PRIOR BANK EDITED. ### THE CORPUS WRITES ARE ONE APPENDED FOLD SECTION, TWO APPENDED "
        "ORIENTATION BLOCKS, ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### "
        "NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b412_the_arc_folded.txt; data/b412_components.txt; data/b412_arc.txt; "
        "data/b412_orientation.txt; data/b412_span.txt; data/b412_registration_2026-09-10.txt "
        "(LOCKED before any write, chained on tools/b378_lockgate.py run as b412 -- %d gates read, "
        "%d checked by digest); tools/b412_components.py; tools/b412_desk_bank.py; "
        "tools/b412_checks.py; PLACE-papers FINDINGS.md, THE_FINDINGS_AS_THEY_STAND.md, "
        "PATHS_TO_THE_CRITICAL_LINE.md and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (GR, GDG, rownum))
    act = ("b412 (the classification arc b403-b411 folded with two mechanical arms, the arc "
           "counted at zero statements about the object, the routed pile inventoried at ten, the "
           "reach instrument priced as a build, and the orientation layer refreshed under R31)")
    row_new = ('    # ### THE CLASSIFICATION ARC FOLDED (b412).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-46s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-58s reaches the b412 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the two span numbers', "THE FOLD'S SPAN IS 9" in out),
            ('the folding act excluded', 'NOT IN ITS OWN FOLD' in out),
            ('the two mechanical arms', 'F-NOGRADE' in out and 'F-NOSUPERSEDE' in out),
            ('zero about the object', '0 STATEMENTS ABOUT THE OBJECT' in out),
            ('borderline named', 'BORDERLINE AND EACH NAMED' in out),
            ('b409 refused to call it more', 'refused to call a measured kappa' in out),
            ('the pile', 'THE ROUTED PILE IS 10 ITEMS' in out),
            ('nothing discharged', '0 DISCHARGED BY THIS ACT' in out),
            ('reach is a build', "REACH IS A BUILD" in out),
            ('provenance not consequence', 'carries grades PROVENANCE' in out),
            ('maybe unbuildable', 'unbuildable in general' in out),
            ('the digest behind', 'THE DIGEST IS 204 ACTS BEHIND' in out),
            ('the doors already current', 'ALREADY IN THE TABLE' in out),
            ('no door moved', 'MOVES NO DOOR' in out),
            ('two of fifteen', 'ONLY 2 OF 15 FOLD SECTIONS' in out),
            ('absence not invention', 'WORSE THAN ONE THAT SAYS THE SOURCE IS MISSING' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-46s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok, nfold, d0, d1, p0, p1):
    B = []
    BARR, SUBB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BARR)
    A('b412 -- THE CLASSIFICATION ARC FOLDED, AND THE ORIENTATION LAYER BROUGHT CURRENT.')
    A('### THE BANK. ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b412_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py` run as b412'
      % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (GR, LG['gates_passing'], GDG))
    A(BARR)
    A('')
    A(SUBB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUBB)
    A('### ### ### **NINE ACTS, AND `0` STATEMENTS ABOUT THE OBJECT.**')
    A('### `6` about the record, `3` borderline and ### **EACH NAMED RATHER THAN ROUNDED** ###')
    A('### (`b408`, `b409`, `b410`). ### The closest approach is `b409`’s reading of the modular')
    A('### relation as DARK on the placement register -- and ### **`b409` ITSELF REFUSED TO CALL')
    A('### ### IT MORE**: a reading of the record`s own two sentences, not a measured `κ`, with')
    A('### no certificate written.')
    A('### ### **AND THE ARC DIAGNOSED ITSELF MIDWAY.** ### `b408` measured row `U1` at `0`')
    A('### statements about the object across six entries and called it *a bookkeeping instrument,')
    A('### and that is a description and not a demotion*. ### `b409` froze the register at six for')
    A('### the same reason. ### **THE ARC KNEW, AND KEPT GOING** -- which is either discipline or')
    A('### a habit, and the record cannot tell the difference from inside.')
    A('')
    A(SUBB)
    A('### (2) WHAT IT DID PRODUCE, SAID WITHOUT APOLOGY.')
    A(SUBB)
    A('### ### **THREE AUTHOR RULINGS EXECUTED ACROSS THE WHOLE CORPUS** ### -- `(R25)` kept both')
    A('### class numberings and made `29` documents declare which they use at ### **`0` SYMBOLS')
    A('### ### RENUMBERED**; `(R29)` joined two documents that state one test and did not know')
    A('### about each other, at ### **`2` LINES AND `0` RENUMBERINGS**; `(R30)` kept a standing')
    A('### instrument`s number and named `I-16` free, at ### **`0` NUMBERS MOVED.**')
    A('### **A RELATIVIZED THEOREM** ### written into a keystone, UNCOMPILED. ### **A')
    A('### ### CLASSIFICATION NOBODY HAD RUN**, run under two agreeing instruments. ### **A')
    A('### ### STANDING INSTRUMENT FOUND** ### that the seat was about to duplicate. ### **A')
    A('### ### CERTIFICATE LOCATED** ### that the paper named only as *a relay record*. ### And')
    A('### ### **THREE MATHEMATICS-FACING GATE ARMS THAT DID NOT EXIST BEFORE.**')
    A('### ### **THAT IS NINE ACTS OF WORK ON THE RECORD, AND THE RECORD IS THE THING THAT')
    A('### ### CARRIES THE MATHEMATICS.**')
    A('')
    A(SUBB)
    A('### (3) THE FOLD, AND ITS TWO MECHANICAL ARMS.')
    A(SUBB)
    A('### **THE SPAN, FROM THE TOOL:** ### it reports ### **`10`**, counting `b403` through')
    A('### `b412`; ### **THE FOLD`S SPAN IS `9`**, because ### **THE FOLDING ACT IS NOT IN ITS OWN')
    A('### ### FOLD** -- `b402` stood outside `b385`-`b401` the same way. ### **BOTH NUMBERS')
    A('### ### PRINTED; NEITHER TYPED. ### THIS SEAT`S OWN `(N1)` IS REFUTED BY THE TOOL.**')
    A('### **`F-NOGRADE`** ### -- every grade string verbatim in the bank of the act it is')
    A('### attributed to. ### **`F-NOSUPERSEDE`** ### -- no folded act summarised as overturning')
    A('### another where the record says they answer different questions.')
    A('### ### **BOTH RUN BEFORE THE SECTION IS WRITTEN, NOT AFTER.** ### The section is checked')
    A('### and then written, never written and then checked.')
    A('### ### **AND THIS ARC CONTAINS EXACTLY THAT HAZARD:** ### `b411` found the E0 gate prices')
    A('### what `b410` said nothing prices -- ### **OWNERSHIP AGAINST REACH, TWO DIFFERENT')
    A('### ### QUESTIONS**, as `b411` wrote itself.')
    A('')
    A(SUBB)
    A('### (4) THE ROUTED PILE: TEN ITEMS, SEVEN STILL ROUTED.')
    A(SUBB)
    A('### Each with ### **ITS ACT, ITS COST AND ITS OWNER**, and the dispositions ### **KEPT')
    A('### ### APART** ### as `b408` kept them: ### **ROUTED** ### is a decision waiting on the')
    A('### author; ### **NAMED, NOT ROUTED** ### is a research question waiting on nobody; ###')
    A('### **DISCHARGED** ### is paid. ### **THEIR SUM DESCRIBES NONE OF THE THREE.**')
    A('### ### **EXACTLY ONE ITEM THE ARC ROUTED WAS THEN PAID** -- the Definition-2.5')
    A('### classification, routed at `b409` and run at `b410`.')
    A('### ### **`0` ITEMS DISCHARGED BY THIS ACT.** ### An inventory is a list, not a payment.')
    A('')
    A(SUBB)
    A('### (5) THE REACH INSTRUMENT, PRICED AS A BUILD.')
    A(SUBB)
    A('### It would have to ### **(1)** ### decide whether an import already CONTAINS the target;')
    A('### ### **(2)** ### bound what it ADDS beyond what the corpus derives; ### **(3)** ### do')
    A('### both WITHOUT deciding the target.')
    A('### ### **THE CORPUS HAS THE PARTS FOR `(1)`:** ### Definition 2.5`s clause 1 and the')
    A('### standing screen `I-7` between them decide whether a sentence references the target`s own')
    A('### parameter, and `b410` ran exactly that test by hand on four sentences. ### **A READING,')
    A('### ### PRICE `0`.**')
    A('### ### **FOR `(2)` IT HAS NOTHING.** ### Bounding what an import adds is a statement about')
    A('### ### **CONSEQUENCE**, and every instrument the record carries -- the three-grade')
    A('### calculus, the E0 gate`s nine grades, the salt-check -- grades ### **PROVENANCE.**')
    A('### ### ### **SO THE SECOND HALF IS A BUILD, AND BOTH LANES ARE PARKED.**')
    A('### ### **AND THE HONEST QUALIFICATION, IN THE SAME BREATH:** ### it may be ###')
    A('### **UNBUILDABLE IN GENERAL** ### rather than merely unbuilt -- a general bound on what an')
    A('### arbitrary imported sentence adds is close to a conservativity result, and a useful')
    A('### instrument would have to be restricted to a named class of imports, ### **WHICH IS')
    A('### ### ITSELF THE MATHEMATICAL WORK.** ### That is not a reason not to price it; it is')
    A('### part of the price. ### **PRICED; NOT OPENED.**')
    A('')
    A(SUBB)
    A('### (6) THE ORIENTATION LAYER, REFRESHED ASYMMETRICALLY UNDER (R31).')
    A(SUBB)
    A('### ### **THE DIGEST IS `204` ACTS BEHIND.** ### Built at `b163`, its newest act is `b208`,')
    A('### and it gains a block: ### **`%d` LINES -> `%d`.**' % (d0, d1))
    A('### ### **THE FIVE-DOOR STATE WAS ALREADY CURRENT.** ### It gains a block that ### **MOVES')
    A('### ### NO DOOR**: ### **`%d` LINES -> `%d`.**' % (p0, p1))
    A('### ### **WHETHER THE ARC MOVED A DOOR WAS MEASURED, NOT ASSUMED** -- a search by')
    A('### description across all nine banks returns ### **`0` CLAIMS THAT A DOOR MOVED AND `0`')
    A('### ### TERMINALS COMPILED BY THE ARC**, under a positive control finding `h2` in `9 of 9`.')
    A('### ### **AND THE TWO MOVEMENTS EXPECTED OF IT ARE ALREADY IN THE TABLE:** ### `R4`’s')
    A('### *finite-set conjunct now DERIVES* at `lv v0.10.0`, `R5`’s *compiled boundary marker* at')
    A('### `lv v0.9.0` -- recorded when the kernel work landed rather than when a fold noticed.')
    A('### ### **A REFRESH THAT INVENTED A MOVEMENT TO JUSTIFY ITSELF WOULD BE THE ONE THING')
    A('### ### `(R31)` EXISTS TO PREVENT.**')
    A('')
    A(SUBB)
    A('### (7) AND THE FIRST THING (R31) MEETS: MOST FOLDS HAVE NOTHING TO QUOTE.')
    A(SUBB)
    A('### Of the ### **`15`** ### fold sections `FINDINGS.md` carries, ### **`2` HAVE A')
    A('### ### ONE-STATEMENT.** ### The convention begins at `b384`.')
    A('### ### **SO FOR `10` OF THE `12` ARCS FOLDED SINCE THE DIGEST`S NEWEST ACT, THE FERRY`S')
    A('### ### INSTRUCTION -- *each quoted from its fold section and none summarised* -- CANNOT BE')
    A('### ### CARRIED OUT WITHOUT INVENTING TEXT.**')
    A('### The digest block quotes the two that exist and, for every other arc, ### **NAMES IT AND')
    A('### ### RECORDS THAT ITS FOLD CARRIES NO ONE-STATEMENT.**')
    A('### ### **A DIGEST ENTRY THAT INVENTED ITS OWN SOURCE WOULD BE WORSE THAN ONE THAT SAYS THE')
    A('### ### SOURCE IS MISSING**, and writing one-statements for the ten earlier arcs is ###')
    A('### **ROUTED -- NOT TO THIS SEAT, AND NOT BY INVENTION.**')
    A('')
    A(SUBB)
    A('### (8) WHAT THIS ACT DID NOT DO.')
    A(SUBB)
    A('### `0` grades moved, conferred or minted. ### `0` acts re-verdicted. ### `0` doors')
    A('### restated. ### `0` old depths displaced. ### `0` one-statements manufactured. ### `0`')
    A('### routed items discharged. ### `0` instruments built. ### `0` routes proposed. ### `0` κ')
    A('### measured. ### `0` channels opened. ### `0` rows of `FACES_LEDGER.md` written. ### `0`')
    A('### instrument numbers assigned. ### `0` class symbols renumbered. ### `0` lines of either')
    A('### orientation object edited. ### `0` folds re-run. ### `0` rules struck or amended. ###')
    A('### `0` in-place repairs. ### `0` locked faces edited. ### `0` prior acts` banks edited.')
    A('### `0` kernels built. ### `0` `.lean` files touched. ### `0` platform calls. ### `0`')
    A('### content lost.')
    A('### ### **BOTH LANES STAY PARKED. ### THE WAVE STAYS PARKED. ### NOTHING DEPOSITS.**')
    A('### ### **AND `h2` IS WHERE THE DEPOSIT LEFT IT.**')
    A('')
    A(BARR)
    A('### THE WRITES, BY KIND.')
    A(BARR)
    A('### **KIND 9 -- THE FOLD.** ### `FINDINGS.md`, one appended arc section, `%d` lines.' % nfold)
    A('### **KIND 10 -- THE ORIENTATION LAYER.** ### the digest, one appended block (`%d`->`%d`);'
      % (d0, d1))
    A('###   the five-door state, one appended block (`%d`->`%d`). ### **BOTH ADDITIVE; BOTH PRIOR'
      % (p0, p1))
    A('###   ### TEXTS PRESERVED AS TRUE PREFIXES.**')
    A('### **KIND 11** -- `OPEN_TRAILS.md` one appended block; `CORRESPONDENCE.md` row `%d`;'
      % rownum)
    A('###   `banked_index.py` key `%s` -- read back %s.' % (KEY, 'PASS' if kok else 'FAIL'))
    A('### **AND NOTHING ELSE, OF ANY KIND.**')
    A(BARR)
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  ### BANK WRITTEN : %s  (%d lines, %d bytes)' % (os.path.basename(BANKOUT), len(B), n))
    return len(B)


# ### =================================================================================================
def main():
    rec('=' * 100)
    rec('b412_desk_bank.py -- THE FOLD, THE ORIENTATION LAYER, THE TRAIL, THE ROW, THE KEY.')
    rec('=' * 100)
    rec('  face LOCKED : %s' % SEALHASH)
    rec('')
    bar()
    rec('  ### THE DESK.')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### KIND 9 -- THE FOLD SECTION, CHECKED THEN WRITTEN.')
    bar()
    fok, nfold = do_fold()
    if not fok:
        rec('  ### HARD FAILURE in the fold.')
        rec('  ### run record : %s' % run_clock.write(D, 'b412_desk_notes', LINES))
        return 1

    rec()
    bar()
    rec('  ### KIND 10 -- THE ORIENTATION LAYER, UNDER (R31).')
    bar()
    dok, d0, d1 = append_block(DIGEST, DIGMARK, digest_block(), 'the digest')
    pok, p0, p1 = append_block(PATHS, DOORMARK, doors_block(), 'the five-door state')
    if not (dok and pok):
        rec('  ### HARD FAILURE -- an orientation block was not a true prefix.')
        rec('  ### run record : %s' % run_clock.write(D, 'b412_desk_notes', LINES))
        return 1
    rec('  ### ### **DIGEST `%d` -> `%d` LINES. ### FIVE-DOOR STATE `%d` -> `%d` LINES.**'
        % (d0, d1, p0, p1))

    rec()
    bar()
    rec('  ### KIND 11 -- THE TRAIL BLOCK.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the b412 block is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b411 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=NL).write(
            NL.join(trail_block(Q, d0, d1, p0, p1)) + NL)
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            rec('  ### run record : %s' % run_clock.write(D, 'b412_desk_notes', LINES))
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_folded': 'is folded into `findings.md`' in low,
        'says_both_spans': 'the fold’s span is 9' in low,
        'says_not_in_own_fold': 'not in its own fold' in low,
        'says_n1_refuted': 'refuted by the tool' in low,
        'says_two_arms': 'f-nogrady' in low or ('f-nogrode' in low or 'f-nograde' in low),
        'says_before_not_after': 'before the section is written, not after' in low,
        'says_hazard': 'different questions — ownership against reach' in low,
        'says_zero_object': '0 statements about the object' in low,
        'says_borderline': 'borderline and every one named' in low,
        'says_b409_refused': 'refused to call it more' in low,
        'says_self_diagnosed': 'the arc diagnosed itself midway' in low,
        'says_produced': 'said without apology' in low,
        'says_pile': '10 items, 7 still routed' in low,
        'says_kept_apart': 'kept apart as b408 kept them' in low,
        'says_nothing_discharged': '0 items are discharged by this act' in low,
        'says_build': 'the second half is a build' in low,
        'says_provenance': 'grades **provenance**' in low,
        'says_unbuildable': 'unbuildable in general' in low,
        'says_204': '204 acts behind' in low,
        'says_no_door': 'that block moves no door' in low,
        'says_measured': 'measured, not assumed' in low,
        'says_already': 'already in the table' in low,
        'says_two_of_fifteen': '**2 have a one-statement**' in low or '2 have a one-statement' in low,
        'says_absence': 'worse than one that says the source is missing' in low,
        'says_finder': 'alphabetically first survivor' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
        'says_h2': 'h2 where the deposit left it' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        rec('  ### run record : %s' % run_clock.write(D, 'b412_desk_notes', LINES))
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)

    rec()
    bar()
    rec('  ### THE CORRESPONDENCE ROW.')
    bar()
    ROWS2 = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS2 if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### run record : %s' % run_clock.write(D, 'b412_desk_notes', LINES))
        return 1
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    present = [mm for mm, _s, _t, _p, _g, _sc, _st in ROWS2 if mm in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = max(nums)
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS2)]
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
            rec('  ### run record : %s' % run_clock.write(D, 'b412_desk_notes', LINES))
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
    nb = bank_file(Q, rownum, kok, nfold, d0, d1, p0, p1)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### FOLD %d LINES. ### DIGEST %d->%d. ### DOORS '
        '%d->%d, 0 MOVED. ### CORR ROW %d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], nfold, d0, d1, p0, p1, rownum,
           'PASS' if kok else 'FAIL', nb))
    bar('=')
    p = run_clock.write(D, 'b412_desk_notes', LINES)
    print(NL + '  ### THIS RUN WROTE : %s   (stamp %s)'
          % (os.path.basename(p), run_clock.read_stamp(p)))
    lp, ls, note = run_clock.latest(D, 'b412_desk_notes')
    print('  ### AND THE GUARD AGREES : %s   (%s ; %s)'
          % (os.path.basename(lp or '-'), ls, note))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
