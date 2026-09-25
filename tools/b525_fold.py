# -*- coding: utf-8 -*-
"""b525_fold.py -- THE FOLD AT SPAN NINE, b517 THROUGH b524. ### `python tools/b525_fold.py check | write`

### ### **A FOLD RESTATES AND MINTS NOTHING.** ### b507`s pattern, as b516 carried it: every verdict string QUOTED from its
### own act`s closing bank and matched there (markup, apostrophes and whitespace normalised) before `write` runs; every
### ruling matched in its ferry by BEGIN, END and its opening; the errors block`s three sources matched in their ferries;
### `write` REFUSES unless `check` passes, and only APPENDS -- one section to `FINDINGS.md`, one block to the (R31) digest,
### each prior byte string proved a true prefix. ### The span is READ from `b525_span.json`, never typed.
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
OUT = os.path.join(D, 'b525_fold.json')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SPAN = json.load(io.open(os.path.join(D, 'b525_span.json'), encoding='utf-8'))
LO, HI = SPAN['span_starts_at'], SPAN['this_act'] - 1
TITLE = 'THE WITNESS ARC'
HEADING = '## %s, b%d–b%d — THE FOLD' % (TITLE, LO, HI)
DMARK = '<!-- b525 orientation refresh: the witness arc -->'
Q0B = 'BORDERLINE -- a statement about the control function Z_Q0, which is not the object'

ROWS = [
    (517, '(d), the growth bound of `W-ORD-WEIL-CONVERSE`, compiled in the kernel',
     ['(d), THE GROWTH BOUND, COMPILED, UNDER (R126).', 'attempts 1, the first to succeed 1 ; paperFT_growth 24 lines'], 'MODEL', ''),
    (518, 'the two-property window, the zero factor on the cosine window',
     ['THE TWO-PROPERTY WINDOW, UNDER (R127).',
      'Q0 : VERIFIED-EST 119 ; P - PR + A negative NONE ; positive 119 ; pair negative 119, positive 0'], 'MODEL', Q0B),
    (519, 'three variants of the window: notched, edge-weighted, both',
     ['THREE VARIANTS OF THE TWO-PROPERTY WINDOW, UNDER (R128).', 'the witness at Q0 : NONE'], 'MODEL', Q0B),
    (520, 'variant (B) widened past the ladder, to a = 60',
     ['VARIANT (B) WIDENED PAST THE LADDER, UNDER (R129).', 'Q0 : 0 cells read ; xi : VERIFIED-EST 46 of 46, positive 46'], 'MODEL', ''),
    (521, 'Q0’s tail tightened in closed form; the ramp order raised',
     ['Q0`S TAIL TIGHTENED, THEN THE WIDTH PASS RE-RUN, UNDER (R130).',
      'least p : 7 ; new tail below b519`s old majorant at 108 of 119 widths'], 'MODEL', ''),
    (522, 'variant (B) at p = 7, the reach read per width',
     ['VARIANT (B) AT p = 7, THE REACH READ PER WIDTH, UNDER (R131).', 'reach : 33 of 46 IN'], 'MODEL', Q0B),
    (523, 'the witness’s three caveats priced: σ_max, S(t), the shortfall',
     ['THE WITNESS`S THREE CAVEATS PRICED, UNDER (R132).',
      'surviving all three : 24, narrowest 34.0 ; VERIFIED-EST-TAIL at 33 of 33'], 'MODEL', Q0B),
    (524, '(f)(i) stated and proved on variant (B) in the kernel',
     ['(f)(i) STATED ON VARIANT (B) IN THE KERNEL, UNDER (R133) AND (R134).',
      'profile : 10 of 10 theorems the standard three on the whole string'], 'MODEL', ''),
]

RULINGS = [
    (126, 'b517_ferry.txt', 'THE CLASS SHAPES THE CONVERSE', 'executed at b517'),
    (127, 'b518_ferry.txt', 'THE TWO-PROPERTY WINDOW OF (R126)(1) IS MEASURED AT b518', 'executed at b518'),
    (128, 'b519_ferry.txt', "h2_sign IS WEIL'S POSITIVITY CRITERION ON classK", 'executed at b519'),
    (129, 'b520_ferry.txt', 'THE DESIGN IS SETTLED AND THE MISSING DIMENSION IS WIDTH', 'executed at b520'),
    (130, 'b521_ferry.txt', "b518's AND b519's Q0 CELLS ARE RE-MARKED VERIFIED-EST-TAIL", 'executed at b521; its (2) refuted at b522'),
    (131, 'b522_ferry.txt', "b521's result stands as registered", 'executed at b522'),
    (132, 'b523_ferry.txt', "b522's reading is entered in (R127)(2)'s words", 'executed at b523'),
    (133, 'b524_ferry.txt', "b523's numbers are entered", 'executed at b524; its (2) form of words corrected by (R134)'),
    (134, 'b524_ferry_R134.txt', "(R133)(2)'s PERMITTED FORM OF WORDS IS CORRECTED", 'executed at b524'),
    (135, 'b525_ferry.txt', 'b524 is entered', 'executed at b525, this fold'),
]

# ### THE ERRORS BLOCK`S SOURCES, EACH QUOTED FROM ITS FERRY (whitespace normalised in the match).
E130 = ('b521_ferry.txt', 'its\ngrowth in the width is e^{L/2} against the pair\'s e^{2 delta L}')
E131 = ('b522_ferry.txt', 'so (R130)(2)\'s\nclaim that the majorant grows like e^{L/2} on this grid is refuted\nby the record and marked so')
E133 = ('b524_ferry.txt', '"positive for xi at every verified width to 60 with the same\nwindow, where the Epstein control is negative from 34; both\nVERIFIED-EST-TAIL; two constants of the count numerical."')
E134 = ('b524_ferry_R134.txt', '"positive for xi at every verified width to 60 in the same window\nfamily at ramp order 5, where the Epstein control at order 7 is\nnegative from 34; xi VERIFIED-EST, the control VERIFIED-EST-TAIL;\ntwo constants of the count numerical."')
E135 = ('b525_ferry.txt', 'the theorems cover both and the INSTANCES DIFFER')
ERRORS = dict(r130=E130, r131=E131, r133=E133, r134=E134, r135=E135)

WORKORDERS = [
    ('W-ORD-XI-P7', '(R134)(1), b524', 'the next opening of the numerical lane -- (R135)(3)(a), the act after this fold, with the '
     'instance discrepancy', 'OPEN'),
    ('W-ORD-WEIL-CONVERSE', '(R124)(2), b515', '(R135)(3)(b): the kernel lane after (a), for (f)(ii) on the kernel`s instance',
     '(d) DONE at b517; (f)(i) = f1 DONE at b524; f2, f3, f4 OPEN'),
]


def norm(s):
    s = (s or '').replace('’', '').replace("'", '').replace('`', '').replace('*', '').replace('#', '')
    return re.sub(r'\s+', ' ', s).strip().lower()


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def defects(act):
    return len(re.findall(r'^    \([a-z]\) ###', rd(os.path.join(D, 'b%d_defects.txt' % act)), re.M))


def check(verbose=True):
    res = dict(quotes=[], defects=[], rulings=[], errors={})
    for act, _s, quotes, _c, _b in ROWS:
        bank = norm(rd(os.path.join(D, 'b%d_closing.txt' % act)))
        for q in quotes:
            res['quotes'].append(dict(act=act, quote=q, found=norm(q) in bank))
        n = defects(act)
        closing = rd(os.path.join(D, 'b%d_closing.txt' % act))
        res['defects'].append(dict(act=act, n=n, found=n > 0 and 'OWN DEFECTS' in closing))
    for r, f, opening, _st in RULINGS:
        t = rd(os.path.join(D, f))
        res['rulings'].append(dict(ruling=r, file=f, found=('RULING (R%d) BEGIN' % r) in t and ('RULING (R%d) END' % r) in t
                                   and norm(opening) in norm(t)))
    for k, (f, q) in ERRORS.items():
        res['errors'][k] = norm(q) in norm(rd(os.path.join(D, f)))
    res['span'] = dict(lo=LO, hi=HI, acts=HI - LO + 1, tool_reads=SPAN['current_span'], filed_by=SPAN['filed_by'])
    res['heading_already_present'] = HEADING in rd(FIND)
    miss = [x for k in ('quotes', 'defects', 'rulings') for x in res[k] if not x['found']] + [k for k, v in res['errors'].items() if not v]
    res['ok'] = not miss and [r[0] for r in ROWS] == list(range(LO, HI + 1)) and not res['heading_already_present']
    if verbose:
        print('  span read from b525_span.json : b%d - b%d, %d acts ; the tool reads %d through this act'
              % (LO, HI, HI - LO + 1, SPAN['current_span']))
        print('  verdict strings : %d ; matched in their own closing bank : %d' % (len(res['quotes']), sum(q['found'] for q in res['quotes'])))
        print('  defects : %s ; total %d' % ({d['act']: d['n'] for d in res['defects']}, sum(d['n'] for d in res['defects'])))
        print('  rulings : %d ; BEGIN, END and opening matched in the named ferry : %d' % (len(res['rulings']), sum(r['found'] for r in res['rulings'])))
        print('  errors block sources : %s' % res['errors'])
        for x in miss:
            print('    ### MISS : %s' % x)
        print('  ### ### **CHECK : %s**' % ('PASS' if res['ok'] else 'FAIL'))
    return res


def cols():
    c = dict(OBJECT=0, MODEL=0, RECORD=0)
    for r in ROWS:
        c[r[3]] += 1
    return c


def q1(f, q):
    return ' '.join(q.split())


STATEMENT = ('**In this arc the window of (f)(i) — the zero factor (γ₀² + D²) on a cosine-modulated plateau — was designed, widened '
             'and priced until, at Q0, an Epstein zeta function whose off-line zeros are banked, h2_sign’s quantity was negative '
             'beyond its bound from width 34 to 60, the bound surviving the strip, the count and the shortfall re-priced; and the '
             'kernel proved the window’s three properties for every C⁴ compactly supported φ. The witness is exhibited '
             'numerically at one ρ on the control function, not on ζ; no statement about ζ moved.**')


def section(res):
    c = cols()
    tot = sum(d['n'] for d in res['defects'])
    L = [HEADING, '',
         '**Eight acts, b%d through b%d — `(R135)`(2)’s fold at span nine.** `b363_span.py` reads **%d** through this filing act; '
         'the fold’s own span, the filing act excluded as at b507 and b516, is **%d**.' % (LO, HI, res['span']['tool_reads'], res['span']['acts']),
         '', '### The arc in one statement', '', STATEMENT,
         '', '### The span, act by act, each verdict verified in its own closing bank', '',
         '| act | subject | its verdicts, as its bank prints them | column |', '|:--|:--|:--|:--|']
    for act, subj, quotes, col, bord in ROWS:
        q = ' · '.join('`%s`' % x.replace('`', "'").replace('|', '/') for x in quotes)
        L.append('| **b%d** | %s%s | %s | %s |' % (act, subj, (' — *%s*' % bord) if bord else '', q, col))
    L += ['', '**%d verdict strings across %d acts, every one matched in that act’s own closing bank**, by `tools/b525_fold.py '
          'check` before this section was written.' % (len(res['quotes']), len(ROWS)),
          '', '### The three columns, kept apart', '',
          '**Statements about the object: %d. About the model: %d. About the record: %d.** Four rows are borderline and say so — '
          'b518, b519, b522 and b523 measure the control function Z_Q0, which is not the object. **The object column is empty**: '
          'a witness exhibited on an Epstein function is a statement about that function and about the window, and a kernel '
          'theorem about a window is a statement about the window.' % (c['OBJECT'], c['MODEL'], c['RECORD']),
          '', '### What the arc established, each at its own address', '',
          '- **(d), the growth bound, compiled** — ‖paperFT h z‖ ≤ ‖h‖₁·e^{L|Im z|}, standard three (b517).',
          '- **The two-property window turns the pair negative at every ladder width but is not dominant there** (b518); of three '
          'variants the edge-weighted plateau (B) comes nearest, pair/rest −0.416 at the widest ladder cell (b519).',
          '- **Q0’s verifications to b519 were the tail majorant’s** (b520), re-marked VERIFIED-EST-TAIL by appended note: 12 of '
          'b518’s 119, 252 of b519’s 357 (b521).',
          '- **The tail falls with width on a = 15 … 60 at every order scanned**; the least ramp order with the tail below the rest '
          'of the bound at a = 60 is 7 (b521).',
          '- **At p = 7, read per width, 33 of 46 widths are within reach and Q0 is negative beyond its bound at 24, from a = 34**; '
          'the pair’s ratio to the rest crosses −1 there, realized growth 0.275 of (d)’s factor (b522).',
          '- **The three caveats priced: σ_max = 1.425 for Q0, N(T) ≤ M0 + E with E(150) = 22.2 proved (two constants numerical on '
          'grids), the shortfall at most 1.7e-19 of any margin; 24 of 24 survive, narrowest a = 34, every one VERIFIED-EST-TAIL** '
          '(b523).',
          '- **(R118)(1)’s bar lifted with its caveat named, and step (9)’s Epstein sentence gained its bank** — b522 and b523, '
          'quoted, by appended note beside its NO BANK note, which stays (`(R133)`(2), b524).',
          '- **(f)(i) proved in the kernel**: classK membership, the zero at γ₀, the factorisation, for every real C⁴ compactly '
          'supported φ, each DERIVES by statement-read; the (f)(ii) hypothesis a `Prop` with G defined as the integral (b524).',
          '', '### Errors entered as their owners’', '',
          '**`(R130)`(2)’s growth claim, refuted by the record.** b521’s ferry: *“%s”*; b522’s ferry, `(R131)`(1): *“%s”* — the '
          'increasing-width stop rule retired with it, the reach read per width.' % (q1(*E130), q1(*E131)),
          '',
          '**`(R133)`(2)’s form of words, as `(R134)` corrected it.** As pasted: *%s* — two clauses not borne out by the banks '
          '(ξ read at ramp order 5, Q0’s negatives at order 7; ξ VERIFIED-EST, not tail-led). **It reads from b524 on:** *%s*'
          % (q1(*E133), q1(*E134)),
          '',
          '**`(R135)`(1)’s instance discrepancy.** *“%s”*: the kernel’s named instance is Mathlib’s smooth bump, the measured '
          'window an order-7 B-spline; the record says so wherever the two are cited together.' % q1(*E135),
          '',
          '**The seat’s, as its acts entered them: %d defects of their own instruments across all eight acts.** The recurrent '
          'species: **a price taken and not read against the reading it priced** (b520, b521), **a generator’s rename list that '
          'missed or over-reached a string** (b518, b522, b523, b524), and a tool that assumed a file or a cell the run did not '
          'produce (b520, b521).' % tot,
          '', '### The rulings of the span, with the file that ratifies each', '',
          '| ruling | ratified in | status as the record holds it |', '|:--|:--|:--|']
    for (r, f, _o, st), x in zip(RULINGS, res['rulings']):
        L.append('| `(R%d)` | relay `data/%s` | %s |' % (r, f, st))
    L += ['', '### The work-orders, carried with their triggers — `(R135)`(2)', '',
          '| work-order | filed | trigger | status |', '|:--|:--|:--|:--|']
    for w, f, t, s in WORKORDERS:
        L.append('| `%s` | %s | %s | %s |' % (w, f, t, s))
    L += ['', '### Filed with this fold, not done by it', '',
          '- **The host-stop rule, `(R134)`(2): a host stop is not an attempt** — a run the harness stops carries no verdict from Lean '
          'and is recorded STOPPED BY HOST, attempt 0.',
          '- **The order after this fold, `(R135)`(3): (a) then (b)** — one numerical act closing `W-ORD-XI-P7` and the instance '
          'discrepancy together (ξ re-read at order 7 on b520’s widths, and both objects re-read with the kernel’s smooth-bump '
          'instance as φ), then the kernel lane for (f)(ii) on the kernel’s instance. **`(R135)`(4): the B-spline is not '
          'constructed in the kernel.**',
          '',
          '**No expectation of the span is re-scored.** Nothing compiled. No corpus grade moved. No ERRATA line written. Row U1 '
          'unedited; **`h2` where the deposit left it**; **the four lists stay OPEN**; no claim about RH in either direction.',
          '', '*Filed by b%d (relay `data/b525_fold.json`, `tools/b525_fold.py`). Nothing above this section was edited; no grade is '
          'conferred by a seat; nothing is minted; nothing is claimed about `h2`.*' % (HI + 1), '']
    return NL.join(L)


def digest_block():
    return NL.join([
        '', DMARK, '',
        '**Orientation refresh — filed b525, 2026-09-25 *(additive)*.** Under `(R31)` this fold refreshes the digest with one arc:',
        '',
        '- **b%d–b%d — %s**, folded at b525. Its one statement, quoted: %s' % (LO, HI, TITLE, STATEMENT),
        '',
        '**The governing claim at the head of this document is unchanged by this arc**, whose object column is empty: a witness '
        'on a control function is not a statement about ζ, and `h2` stands where the deposit left it.',
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
    blk = digest_block()
    w1 = append(FIND, NL + sec)
    w2 = append(DIG, blk)
    ft, dt = rd(FIND), rd(DIG)
    res.update(writes=[w1, w2], markers=dict(heading=ft.count(HEADING), digest=dt.count(DMARK)), columns=cols(), title=TITLE,
               heading=HEADING, workorders=[list(w) for w in WORKORDERS])
    d = (json.dumps(res, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(OUT + '.tmp', 'wb').write(d)
    os.replace(OUT + '.tmp', OUT)
    for w in (w1, w2):
        print('  %(file)s : %(before)d + %(added)d = %(after)d bytes ; prefix %(prefix)s ; BOM kept %(bom)s ; lines removed %(removed)d' % w)
    print('  markers : %s' % res['markers'])
    return 0


if __name__ == '__main__':
    sys.exit({'check': lambda: 0 if check()['ok'] else 1, 'write': write}[sys.argv[1]]())
