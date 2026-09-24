# -*- coding: utf-8 -*-
"""b507_fold.py -- THE FOLD AT SPAN TWENTY, b487 THROUGH b506. ### `python tools/b507_fold.py check | write`

### ### **A FOLD RESTATES AND MINTS NOTHING.** ### Every verdict string in the span table is QUOTED from
### its own act's closing bank `data/bNNN_closing.txt`, and `check` matches each one there, both sides
### normalised for markup (`#`, `*`, backticks, apostrophes) and whitespace, before `write` will run.
### ### **`write` REFUSES UNLESS `check` PASSES**, and it only APPENDS: one section to `FINDINGS.md`,
### one block to the (R31) digest, each prior byte string proved a true prefix of what it became.
### ### The span is READ from `b507_span.json` (`b363_span.py`, run at step zero, ONCE -- `span_start`
### is not idempotent across its own act's write), never typed.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND = os.path.join(PP, 'FINDINGS.md')
DIG = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
OUT = os.path.join(D, 'b507_fold.json')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SPAN = json.load(io.open(os.path.join(D, 'b507_span.json'), encoding='utf-8'))
LO, HI = SPAN['span_starts_at'], SPAN['this_act'] - 1
TITLE = 'THE MARGIN AND ITS CONTROL ARC'
HEADING = '## %s, b%d–b%d — THE FOLD' % (TITLE, LO, HI)
DMARK = '<!-- b507 orientation refresh: the margin and its control arc -->'

# ### (act, subject, [verdict strings QUOTED from its closing bank], column, borderline note)
ROWS = [
    (487, 'the ERRATA id collision renumbered append-only under (R97); three Zenodo descriptions read from disk',
     ['E-2026-09-22-1 occurrences before this act : 2', 'b485`s becomes E-2026-09-22-2 by an APPENDED dated line naming (R97).'],
     'RECORD', ''),
    (488, 'b486’s fold written home into FINDINGS under (R98); `corr_row.py` given its row-number guard',
     ['A TRANSCRIPTION, NOT A FOLD.', 'NO VERDICT IS RE-READ AND NO ACT IS RE-SCORED.'], 'RECORD', ''),
    (489, 'the margin `m(a) = A - PR` over the 35 ladder widths, and a conjecture registered',
     ['EVERY MARGIN IS POSITIVE', 'AND THE SHAPE HAS TWO TURNING POINTS, NOT ONE:'], 'MODEL', ''),
    (490, 'the ladder’s increments, the sensitivity ratio, and pid 27508 read dead',
     ['27508 ABSENT AT BOTH', 'THE TURN FRACTIONS THE ORDER ASKS FOR: NOT DECIDABLE FROM THE BANKS.'], 'MODEL', ''),
    (491, 'the b475 log read under (R101), and (R82) decided on it',
     ['191 `=== EXIT` LINES AND EVERY ONE IS `EXIT 0`', 'THE VERDICT ON (R82). HOLDS.'], 'MODEL', ''),
    (492, 'the per-n prime terms at every rung, and the increments attributed',
     ['35 OF 35 CELLS REPRODUCE EXACTLY, BIT FOR BIT.', 'IT CLOSES TO 8.5e-17 AT WORST'], 'MODEL', ''),
    (493, 'the eight Zenodo records read whole against the claim ceiling',
     ['NO DESCRIPTION IS TRUNCATED.', 'THE 8 EXCEEDING ROWS CARRY NO REPLACEMENT.'], 'RECORD', ''),
    (494, 'the (R104) sequence reconciled with the record, and the frame checked',
     ['TWO TABLES IN ONE APPENDED `FINDINGS.md` SECTION', 'OF THE 5 DIRECT ITEMS, 1 IS TAKEN UP'], 'RECORD', ''),
    (495, '`SIDE-explicit-formula` created by vendoring, pushed, and its build launched unread',
     ['BYTE-IDENTICAL : True', 'PIN CHOSEN : `v1.0`'], 'RECORD', ''),
    (496, 'K0 of (R107): the terminal table generated',
     ['949 OF 1021 ROWS CARRY NO GRADE AT ALL.', 'REGISTRY NAMES A PIN FOR 6 OF 44 KERNELS.'], 'RECORD', ''),
    (497, 'the b495 build log read',
     ['THE BUILD WAS KILLED, NOT BROKEN', 'AND NOT ONE `Zeta23` MODULE WAS REACHED.'], 'MODEL',
     'BORDERLINE -- a build killed on this machine is a fact about the machine, and it is what denied the profiles'),
    (498, 'the build re-launched in its own console, with the cache',
     ['THE SENDER : NOT ESTABLISHED.', 'FETCHED 8681'], 'RECORD', ''),
    (499, 'ten metadata edits at Zenodo under (R110), fetched back',
     ['TEN EDITS AT ZENODO, THREE MATCHES; THE GUARD SCANS FOR THE TOKEN.'], 'RECORD', ''),
    (500, 'the b498 build log read',
     ['EXIT 0; ALL THREE THE STANDARD THREE; (R82) HOLDS.'], 'MODEL', ''),
    (501, 'the places-side quadrature bound, built and tested',
     ['THE BOUND IS WHAT THE TWO SIDES DISAGREE BY.', 'floors exceeded 35 of 35'], 'MODEL', ''),
    (502, 'the ladder past sqrt(32) to sqrt(200)',
     ['m(a) POSITIVE AT ALL 119 CELLS; A THIRD EXTREMUM AT 13.152946; THE LANE SHUT.'], 'MODEL', ''),
    (503, 'the zero side made alias-free by the exact transform',
     ['THE RESIDUAL OF 7 GONE; 64 VERIFIED AS ORDERED, 86 CONSISTENT.'], 'MODEL', ''),
    (504, 'the chain on one transform, and the Epstein control on it',
     ['ONE TRANSFORM: 109 OF 119 VERIFIED; THE EPSTEIN CONTROL VERIFIES NOWHERE.'], 'MODEL', ''),
    (505, 'the Epstein control for Q0: the decomposition, and the completeness count',
     ['CLOSED AS REGISTERED UNDER (R116)(1): C1 HELD; C2 REFUSED AT ITS FIXTURE.'], 'MODEL', ''),
    (506, 'the Q0 bank counted below 150, and the derived kernel on the completed bank',
     ['180 ZEROS BELOW 150; THE BANK LACKS 30, NONE AT SIGMA > 1; THE DERIVED KERNEL VERIFIES 93 OF 93.'], 'MODEL',
     'BORDERLINE -- a count of the zeros of the control function Z_Q0, which is not the object'),
]

# ### THE DEFECTS EACH ACT RECORDS OF ITS OWN INSTRUMENTS, AS ITS CLOSING COUNTS THEM (the word it prints),
# ### and the phrase that carries the count -- matched in the bank by `check`, never typed without a match.
DEFECTS = {
    487: (0, None), 488: (5, 'OWN INSTRUMENTS. ### **FIVE'), 489: (6, 'OWN INSTRUMENTS. ### **SIX'),
    490: (7, 'OWN INSTRUMENTS. ### **SEVEN'), 491: (6, 'OWN INSTRUMENTS. ### **SIX'),
    492: (6, 'OWN INSTRUMENTS. ### **SIX'), 493: (4, 'OWN INSTRUMENTS. ### **FOUR'),
    494: (3, 'THIS ACT`S OWN DEFECTS.'), 495: (5, 'OWN DEFECTS -- FIVE.'), 496: (7, 'OWN DEFECTS -- SEVEN.'),
    497: (5, 'THIS ACT`S OTHER DEFECTS -- FOUR.'), 498: (6, 'OWN DEFECTS -- SIX.'), 499: (4, 'OWN DEFECTS -- FOUR.'),
    500: (3, 'OWN DEFECTS -- THREE.'), 501: (2, 'OWN DEFECTS -- TWO.'), 502: (0, 'OWN DEFECTS -- NONE FOUND.'),
    503: (2, 'OWN DEFECTS -- TWO.'), 504: (1, 'OWN DEFECTS -- ONE, AND ONE OF b504`S FOUND BY IT.'),
    505: (2, 'OWN DEFECTS -- TWO.'), 506: (3, 'OWN DEFECTS -- THREE, AND TWO OF EARLIER RECORDS'),
}

# ### THE RULINGS OF THE SPAN, each with the ferry file that ratifies it -- MATCHED by `check`.
RULINGS = [
    (97, 'b487_ferry.txt', 'THE ERRATA ID COLLISION IS RESOLVED BY APPENDED NOTE'),
    (98, 'b488_ferry.txt', 'A FOLD`S HOME IS FINDINGS'),
    (99, 'b489_ferry.txt', 'OF THE THREE DRAFTS, s2 IS APPLIED AS DRAFTED'),
    (100, 'b490_ferry.txt', 'THE CONJECTURE`S WORDING IS THE SEAT`S REPAIR'),
    (101, 'b491_ferry.txt', 'THE b475 LOG IS READ NOW'),
    (102, 'b493_ferry.txt', 'THE PLATFORM EDITS UNDER (R99) ARE HELD FOR ONE ACT'),
    (103, 'b493_ferry.txt', '(R82) HAVING HELD at b491, SIDE-explicit-formula IS CREATED'),
    (104, 'b493_ferry_clause.txt', None),
    (105, 'b494_ferry.txt', 'THE RECONCILIATION ACT UNDER (R104) CARRIES A SECOND TABLE: the frame check.'),
    (106, 'b495_ferry.txt', 'b494`s Table 2 row 5 is corrected on the record'),
    (107, 'b496_ferry.txt', 'THE KEYSTONE REFRESH PROGRAMME IS OPENED AS ACTS, NOT DOCUMENTS'),
    (108, 'b497_ferry.txt', 'THE GRADE CELL MAY BE SPLIT.'),
    (109, 'b498_ferry.txt', 'THE THREE TITLES ARE REWORDED'),
    (110, 'b499_ferry.txt', 'THE SEAT MAY WRITE METADATA AT ZENODO'),
    (111, 'b499_ferry.txt', 'Two texts of the banked edits are amended in their v2 file'),
    (112, 'b500_ferry.txt', 'THE LADDER`S TAIL MOVES TO THE HEAD OF (R104).'),
    (113, 'b503_ferry.txt', 'A CELL WHOSE TWO-SIDE RESIDUAL EXCEEDS ITS BOUND IS UNVERIFIED'),
    (114, 'b504_ferry.txt', 'ONE INSTRUMENT, ONE TRANSFORM.'),
    (115, 'b505_ferry.txt', 'EVERY EPSTEIN MARGIN THE RECORD HOLDS'),
    (116, 'b506_ferry.txt', 'b505 CLOSES AS REGISTERED'),
]

# ### THE TWO FINDINGS THIS FOLD MAKES ABOUT ACTS IT FOLDS -- each a needle `check` must find where named.
FIND_NEEDLE = '**The span’s mathematics moved little' + NL
OT_SOURCE = '**The span\'s mathematics moved little and its bookkeeping moved a great deal.**'
B504_LABEL = 'b504`S TOOL CARRIES THE SAME PREDICATE'
B504_SUBJECT = 'b503\'s tool carries the same predicate'


def norm(s):
    s = (s or '').replace('’', '').replace("'", '').replace('`', '').replace('*', '').replace('#', '')
    return re.sub(r'\s+', ' ', s).strip().lower()


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def check(verbose=True):
    res = dict(quotes=[], defects=[], rulings=[], findings={})
    for act, _s, quotes, _c, _b in ROWS:
        bank = norm(rd(os.path.join(D, 'b%d_closing.txt' % act)))
        for q in quotes:
            res['quotes'].append(dict(act=act, quote=q, found=norm(q) in bank))
    for act, (n, phrase) in DEFECTS.items():
        bank = rd(os.path.join(D, 'b%d_closing.txt' % act))
        ok = (phrase is None and 'DEFECT' not in bank.upper().replace('DEFECT THE ERRATUM', '')) or \
             (phrase is not None and norm(phrase) in norm(bank))
        res['defects'].append(dict(act=act, n=n, phrase=phrase, found=ok))
    for r, f, opening in RULINGS:
        t = rd(os.path.join(D, f))
        ok = ('RULING (R%d)' % r) in t and (opening is None or norm(opening) in norm(t))
        res['rulings'].append(dict(ruling=r, file=f, found=ok))
    ft = rd(FIND)
    ot = rd(os.path.join(PP, 'OPEN_TRAILS.md'))
    res['findings'] = dict(
        truncated_in_findings=(ft.count(FIND_NEEDLE) == 1),
        whole_in_trail=(ot.count(OT_SOURCE) == 1),
        trail_line=next((i for i, l in enumerate(ot.split(NL), 1) if OT_SOURCE in l), None),
        findings_line=next((i for i, l in enumerate(ft.split(NL), 1) if l + NL == FIND_NEEDLE), None),
        digest_has_no_bookkeeping_block=('THE BOOKKEEPING ARC' not in rd(DIG)),
        b504_label=(B504_LABEL in rd(os.path.join(D, 'b504_closing.txt'))),
        b504_subject=(B504_SUBJECT in os.popen('git -C D:/relay log -1 --format=%B 08439fc5').read()),
    )
    res['span'] = dict(lo=LO, hi=HI, acts=HI - LO + 1, tool_reads=SPAN['current_span'], filed_by=SPAN['filed_by'])
    res['heading_already_present'] = HEADING in ft
    miss_q = [q for q in res['quotes'] if not q['found']]
    miss_d = [d for d in res['defects'] if not d['found']]
    miss_r = [r for r in res['rulings'] if not r['found']]
    miss_f = [k for k, v in res['findings'].items() if v in (False, None)]
    res['ok'] = not (miss_q or miss_d or miss_r or miss_f) and len(ROWS) == HI - LO + 1 \
        and [r[0] for r in ROWS] == list(range(LO, HI + 1)) and not res['heading_already_present']
    if verbose:
        print('  span read from b507_span.json : b%d - b%d, %d acts ; the tool reads %d through this act'
              % (LO, HI, HI - LO + 1, SPAN['current_span']))
        print('  verdict strings : %d ; matched in their own closing bank : %d' % (len(res['quotes']), len(res['quotes']) - len(miss_q)))
        for q in miss_q:
            print('    ### MISS b%d : %s' % (q['act'], q['quote']))
        print('  defect counts : %d acts ; phrase matched : %d ; total recorded : %d'
              % (len(res['defects']), len(res['defects']) - len(miss_d), sum(d['n'] for d in res['defects'])))
        for d in miss_d:
            print('    ### MISS b%d : %s' % (d['act'], d['phrase']))
        print('  rulings : %d ; ratification matched in the named ferry : %d' % (len(res['rulings']), len(res['rulings']) - len(miss_r)))
        for r in miss_r:
            print('    ### MISS (R%d) in %s' % (r['ruling'], r['file']))
        for k, v in res['findings'].items():
            print('  finding %-34s : %s' % (k, v))
        print('  ### ### **CHECK : %s**' % ('PASS' if res['ok'] else 'FAIL'))
    return res


def cols():
    c = dict(OBJECT=0, MODEL=0, RECORD=0)
    for r in ROWS:
        c[r[3]] += 1
    return c


def section(res):
    c = cols()
    tot = sum(d['n'] for d in res['defects'])
    nrec = sum(1 for d in res['defects'] if d['n'])
    f = res['findings']
    L = [HEADING, '',
         '**Twenty acts, b%d through b%d — eleven past `(R1)`’s declared threshold of nine.** `b363_span.py` reads **%d** through this '
         'filing act; the fold’s own span, the filing act excluded as at b434, b444, b453, b463 and b474, is **%d**. **The order named '
         'the span “b475 THROUGH b506”; `(R117)`(2) names it “span 20”, and the navigator chose the tool’s count at the seat on '
         '2026-09-24** — b475 through b485 were folded by b486, written home at b488 under the heading `b475–b479`, and are cited here, '
         'not folded again.' % (LO, HI, res['span']['tool_reads'], res['span']['acts']),
         '', '### The arc in one statement', '',
         '**In this arc the instrument’s margin was charted, bounded and verified cell by cell on one transform, and the control meant '
         'to show what the margin owes to ξ was found not to close until its own zero bank was counted and completed — thirty zeros '
         'short, every one off the line; beside it, the record’s bookkeeping put a fold home, vendored and built a third party’s '
         'explicit formula to the standard three axioms, and read the deposit’s eight records against the claim ceiling.**',
         '', '### The span, act by act, each verdict verified in its own closing bank', '',
         '| act | subject | its verdicts, as its bank prints them | column |', '|:--|:--|:--|:--|']
    for act, subj, quotes, col, bord in ROWS:
        q = ' · '.join('`%s`' % x.replace('`', "'").replace('|', '/') for x in quotes)
        L.append('| **b%d** | %s%s | %s | %s |' % (act, subj, (' — *%s*' % bord) if bord else '', q, col))
    L += ['', '**%d verdict strings across %d acts, every one matched in that act’s own closing bank `data/bNNN_closing.txt`, with '
          'both sides normalised for markup, apostrophes and whitespace**, by `tools/b507_fold.py check` before this section was '
          'written.' % (len(res['quotes']), len(ROWS)),
          '', '### The three columns, kept apart', '',
          '**Statements about the object** — the zeros of ξ, ξ itself, the Euler balance: **%d**. **About the model** — the '
          'instrument’s channels, cells and bounds, kernel terminals and their axiom profiles, the control function’s own zeros: '
          '**%d**. **About the record** — its documents, deposits, rulings, tools and grades: **%d**. Two rows are borderline and each '
          'says so in itself: b497 and b506.' % (c['OBJECT'], c['MODEL'], c['RECORD']),
          '',
          '**The object column is empty.** Twelve of the twenty acts measured the instrument, its bound, its build or its control; '
          '**a measurement of the instrument over a finite chart is not a statement about '
          'ξ**, and every one of those acts closed saying that no cell of it was a statement about RH.',
          '', '### What the arc established, each at its own address', '',
          '- **The margin `m(a) = A − PR` is positive at all 35 ladder widths and has two turning points** (b489); the fitted forms '
          'were retired and the conjecture’s wording set to the measured minimum under `(R100)` (b490).',
          '- **The b475 axiom run completed: 191 exits, every one 0, twenty profiles the standard three; `(R82)` HOLDS** (b491) — and '
          'held again on the vendored kernel’s own build, 57 modules, all three terminals the standard three (b500).',
          '- **The per-`n` prime terms at every rung reproduce b477 bit for bit**, and a prime power entering the window is a '
          'bookkeeping boundary, the split closing to `8.5e-17` (b492).',
          '- **The deposit’s eight records read against the ceiling: 94 rows STAND, 2 REST, 8 EXCEED** (b493); ten metadata edits '
          'were then written at Zenodo under `(R110)` and fetched back, three records MATCH (b499).',
          '- **`SIDE-explicit-formula` was created at pin `v1.0`** (b495), its first build **killed, not broken** (b497), relaunched '
          'in its own console (b498) and read EXIT 0 (b500); **the terminal table carries 1021 rows, 949 with no grade** (b496).',
          '- **The places-side quadrature bound is what the two sides disagree by** (b501); the ladder reached `sqrt 200` with '
          '119 cells and three extrema (b502); the zero side was made alias-free (b503); **on one transform 109 of 119 cells verify** '
          '(b504).',
          '- **The Epstein control for Q0**: the decomposition holds exactly (b505); **its bank below 150 lacked 30 zeros, fifteen '
          'off-line pairs, none at σ > 1, and on the completed bank the derived kernel verifies at 93 of 93 wide cells** (b506).',
          '', '### The findings this fold makes about acts it folds', '',
          '1. **The previous fold section’s one statement is cut mid-sentence in `FINDINGS.md`.** Line %s of the file, under '
          '`THE BOOKKEEPING ARC`, reads `**The span’s mathematics moved little` and stops; its source, b486’s trail record at '
          '`OPEN_TRAILS.md:%s`, is whole — *“The span’s mathematics moved little and its bookkeeping moved a great deal.”* b488 '
          'transcribed the section under `(R98)`; **the fold reports the cut and does not repair it**, since nothing above this '
          'section is edited. **Routed.** And that fold was written home **without an `(R31)` refresh**: the digest carries no block '
          'for it, so this fold’s digest block quotes its statement from the source.' % (f['findings_line'], f['trail_line']),
          '2. **b504’s closing labels its second defect `b504’S TOOL CARRIES THE SAME PREDICATE`**, where its own act commit '
          '(relay `08439fc5`) says *b503’s tool carries the same predicate* — the label names the wrong act. Reported, not edited.',
          '', '### The rulings of the span, with the file that ratifies each', '',
          '| ruling | ratified in | status as the record holds it |', '|:--|:--|:--|']
    status = {
        97: 'executed at b487', 98: 'executed at b488', 99: 'held for one act by `(R102)`', 100: 'executed at b490',
        101: 'executed at b491 and b492', 102: 'executed at b493', 103: 'executed at b495',
        104: 'entered at b493; its reconciliation at b494; its act 3 is next', 105: 'executed at b494',
        106: 'ratified at b495', 107: 'K0 executed at b496', 108: 'ratified at b497', 109: 'ratified at b498',
        110: 'executed at b499', 111: 'executed at b499', 112: 'executed at b500–b502', 113: 'executed at b503',
        114: 'executed at b504', 115: 'ratified at b505; its annotations executed at b506', 116: 'executed at b506'}
    for r in res['rulings']:
        L.append('| `(R%d)` | relay `data/%s` | %s |' % (r['ruling'], r['file'], status[r['ruling']]))
    L += ['', '**Twenty rulings in the span, `(R97)` through `(R116)`, each matched as `RULING (Rnn)` in the file named.** `(R104)` '
          'is the one not ratified in a ferry proper: it was banked as `b493_ferry_clause.txt`, and a count over ferries alone would '
          'have dropped it.',
          '', '### Errors entered as their owners’', '',
          '**The navigator’s, three.** b502’s ferry named the control “x^2 + 5y^2”, a form the record does not hold — named by '
          '`(R115)`(2) and annotated at b506; b506’s ferry put the count’s main term at “178.6”, which omits the `+1` of the two poles '
          '(b506, its READING (2)); and **b507’s own ferry names its span “b475 THROUGH b506” against `(R117)`(2)’s span of 20**, '
          'entered here and resolved at the seat.',
          '',
          '**The seat’s, as its acts entered them: %d defects of their own instruments, recorded by %d of the twenty acts in their '
          'own closings** — b487 records none and b502 records *NONE FOUND*. The most recurrent species of the span is the one '
          '`(R117)`(2) names: `corr_row.py` wrote a row before it validated it, routed since b490. **Not every defect was found inside its own act**: '
          'b504 found b503’s rise predicate, and b506 found b504’s bound figure.' % (tot, nrec),
          '', '### Disposed inside this fold, on `(R117)`', '',
          '- **Beside each `(R115)`(1) note** — in `b477_components.txt`, `b502_components.txt`, `b504_components.txt` — an appended '
          'note that b326’s derived kernel closes on the bank completed at b506 (93 of 93 wide cells) while b325’s does not.',
          '- **b504’s trail line “near 1e-7”** corrected by appended note, in this act’s trail record, to “about 1e-6”.',
          '- **`registration_gate.py`’s bar-floor arm** repaired to catch `>=` as well as `>`, both polarities exercised.',
          '- **`corr_row.py`** repaired to validate the row as it would land before any byte is written.',
          '- **b334’s Epstein crossings** marked UNVERIFIED by a note appended beside them in `b334_the_aim_map.txt`; **no crossing '
          'width is cited here or anywhere in this act.**',
          '', '### Filed with this fold, not done by it', '',
          '**No expectation was registered: a fold registers none.** Nothing compiled. No corpus grade moved and no verdict re-scored. '
          'No ERRATA line written. Row U1 unedited; no bridge typed; **`h2` where the deposit left it**; **the four lists stay OPEN**; '
          'no claim about RH in either direction. **The numerical lane opens for b508 under `(R117)`(4)**, and the kernel lane after it.',
          '', '*Filed by b%d (relay `data/b507_fold.json`, `tools/b507_fold.py`). Nothing above this section was edited; no grade is '
          'conferred by a seat; nothing is minted; nothing is claimed about `h2`.*' % (HI + 1), '']
    return NL.join(L)


def digest_block():
    return NL.join([
        '', DMARK, '',
        '**Orientation refresh — filed b507, 2026-09-24 *(additive)*.** Under `(R31)` a fold refreshes this digest. **b486’s fold, '
        'written home at b488, did not refresh it**, so two arcs are added here, each with its fold’s own one statement quoted:',
        '',
        '- **b475–b485 — THE BOOKKEEPING ARC** (headed `b475–b479` in `FINDINGS.md`), folded at b486 and written home at b488. Its one statement, quoted from its source, '
        'b486’s trail record — **the copy in `FINDINGS.md` is cut mid-sentence**: **The span’s mathematics moved little and its '
        'bookkeeping moved a great deal.**',
        '- **b%d–b%d — %s**, folded at b507. Its one statement, quoted: **In this arc the instrument’s margin was charted, bounded '
        'and verified cell by cell on one transform, and the control meant to show what the margin owes to ξ was found not to close '
        'until its own zero bank was counted and completed — thirty zeros short, every one off the line; beside it, the record’s '
        'bookkeeping put a fold home, vendored and built a third party’s explicit formula to the standard three axioms, and read the '
        'deposit’s eight records against the claim ceiling.**' % (LO, HI, TITLE),
        '',
        '**The governing claim at the head of this document is unchanged by either arc**, whose object columns are empty: the '
        'instrument’s margin measured over a finite chart is a statement about the instrument. `h2` stands where the deposit left it.',
        ''])


def append(path, text):
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    bl, al = before.split(b'\n'), after.split(b'\n')
    return dict(file=os.path.basename(path), before=len(before), added=len(after) - len(before), after=len(after),
                prefix=after.startswith(before), bom=after[:3] == before[:3],
                removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b) - (0 if before.endswith(b'\n') else 1))


def write():
    res = check(verbose=True)
    if not res['ok']:
        print('### REFUSED -- THE CHECK DID NOT PASS; NOTHING WRITTEN.')
        return 2
    sec = section(res)
    dig = digest_block()
    w1 = append(FIND, NL + sec)
    w2 = append(DIG, dig)
    ft, dt = rd(FIND), rd(DIG)
    res['writes'] = [w1, w2]
    res['markers'] = dict(heading=ft.count(HEADING), digest=dt.count(DMARK))
    res['columns'] = cols()
    res['title'] = TITLE
    res['heading'] = HEADING
    d = (json.dumps(res, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(OUT + '.tmp', 'wb').write(d)
    os.replace(OUT + '.tmp', OUT)
    for w in (w1, w2):
        print('  %(file)s : %(before)d + %(added)d = %(after)d bytes ; prefix %(prefix)s ; BOM kept %(bom)s ; lines removed %(removed)d' % w)
    print('  markers : %s' % res['markers'])
    return 0


def preview():
    res = check(verbose=False)
    print(section(res))
    print(digest_block())


if __name__ == '__main__':
    sys.exit({'check': lambda: 0 if check()['ok'] else 1, 'write': write, 'preview': lambda: preview() or 0}[sys.argv[1]]())
