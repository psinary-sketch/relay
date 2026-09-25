# -*- coding: utf-8 -*-
"""b535_fold.py -- THE FOLD AT (R145)(5), b526 THROUGH b534. ### `python tools/b535_fold.py check | write`

### ### **A FOLD RESTATES AND MINTS NOTHING.** ### b525`s form, carried: every verdict string QUOTED from its own act`s closing
### bank and matched there (markup, apostrophes and whitespace normalised) before `write` runs; every ruling matched in its
### ferry by BEGIN, END and its opening; the errors block`s sources matched in their ferries; `write` REFUSES unless `check`
### passes, and only APPENDS -- one section to `FINDINGS.md`, one block to the (R31) digest, each prior byte string proved a true
### prefix. ### The span is READ from `b535_span.json`, never typed. ### This act`s finding (filed before the fold) is its last item.
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
OUT = os.path.join(D, 'b535_fold.json')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SPAN = json.load(io.open(os.path.join(D, 'b535_span.json'), encoding='utf-8'))
LO, HI = SPAN['span_starts_at'], SPAN['this_act'] - 1
TITLE = 'THE WEIL CONVERSE ARC'
HEADING = '## %s, b%d–b%d — THE FOLD' % (TITLE, LO, HI)
DMARK = '<!-- b535 orientation refresh: the Weil converse arc -->'
FTITLE = ("Weil positivity on classK and RH on the kernel's zero configuration: the equivalence compiled both ways; the seam "
          "to Mathlib's RiemannHypothesis named")
KB = 'a theorem relating two premises about the zeros of zeta -- Weil`s criterion; not a statement about where they are'

ROWS = [
    (526, 'ξ at ramp order 7 (`W-ORD-XI-P7` closed); the kernel’s plateau found to be a `Classical.choice`',
     ['XI AT ORDER 7; THE KERNEL`S phi FOUND TO BE A CHOICE, UNDER (R136).',
      'xi at order 7 : IN 46 of 46 ; VERIFIED-EST 46 ; positive 46 ; negative NONE'], 'MODEL', ''),
    (527, 'the kernel’s plateau made concrete (two `Real.smoothTransition` factors)',
     ['THE PLATEAU MADE CONCRETE, UNDER (R137).', 'profile : 11 of 11 theorems the standard three on the whole string'], 'MODEL', ''),
    (528, 'both objects re-read on the kernel’s plateau',
     ['BOTH OBJECTS ON THE KERNEL`S PLATEAU, UNDER (R138).', 'xi : IN 46 of 46 ; VERIFIED-EST 46 ; positive 46 ; negative NONE'],
     'MODEL', ''),
    (529, '(f)(ii), the pair’s term, compiled as far as it derives',
     ['(f)(ii), THE PAIR`S TERM, AS FAR AS IT DERIVES, UNDER (R139).',
      'profile : 19 of 19 theorems the standard three on the whole string'], 'MODEL', ''),
    (530, 'f3, the other zeros bounded above, with its limit printed',
     ['f3, THE OTHER ZEROS BOUNDED ABOVE, WITH ITS LIMIT PRINTED, UNDER (R140).',
      'profile : 30 of 30 theorems the standard three on the whole string'], 'MODEL', ''),
    (531, 'the bridge read: `ConservationHypothesis` against `h2_sign`',
     ['THE BRIDGE READ: ConservationHypothesis AGAINST h2_sign, UNDER (R141).',
      'the grade against "h2_sign -> RH" : ENCODES-CONCLUSION'], 'RECORD', ''),
    (532, 'the deposit read against b531; E-2026-09-25-1 drafted; the trivial bridge compiled',
     ['THE DEPOSIT READ, E-2026-09-25-1 DRAFTED, THE TRIVIAL BRIDGE COMPILED, UNDER (R142).',
      'rows : 31 -- STANDS 17, RESTS 14, EXCEEDS 0'], 'RECORD', ''),
    (533, 'f4, the power-window route, act one: the window and the dominant zero',
     ['f4, THE POWER-WINDOW ROUTE, ACT ONE OF TWO: THE WINDOW AND THE DOMINANT ZERO, UNDER (R143).',
      'std3 34 of 34 ; halted NONE'], 'MODEL', ''),
    (534, 'f4, act two: the limit and the assembly -- `h2_sign ↔ rh_strip` compiled',
     ['f4, THE POWER-WINDOW ROUTE, ACT TWO OF TWO: THE LIMIT AND THE ASSEMBLY, UNDER (R144).',
      'SIDEExplicitFormula.B321.h2_sign_iff_rh_strip : SIDEExplicitFormula.B321.h2_sign ↔ SIDEExplicitFormula.B321.rh_strip'],
     'MODEL', KB),
]

RULINGS = [
    (136, 'b526_ferry.txt', "b525's fold is entered", 'executed at b526'),
    (137, 'b527_ferry.txt', 'b526 is entered', 'executed at b527'),
    (138, 'b528_ferry.txt', 'b527 is entered', 'executed at b528'),
    (139, 'b529_ferry.txt', 'b528 is entered', 'executed at b529'),
    (140, 'b530_ferry.txt', 'b529 is entered', 'executed at b530; its component-4 dichotomy withdrawn by (R143)(2)'),
    (141, 'b531_ferry.txt', 'b530 is entered', 'executed at b531'),
    (142, 'b532_ferry.txt', "b531 IS ENTERED AS THE WEEK'S MOST CONSEQUENTIAL READ", 'executed at b532'),
    (143, 'b533_ferry.txt', 'THE LAST STEP IS ATTEMPTED BEFORE ANY UPDATE', 'executed at b533'),
    (144, 'b534_ferry.txt', 'THE SECOND ACT OF THE ATTEMPT, WITH TWO CORRECTIONS TO THE ROUTE', 'executed at b534'),
    (145, 'b535_ferry.txt', 'THE UPDATE ACT, AFTER THE ATTEMPT CLOSED', 'executed at b535, this fold'),
]

E143 = ('b533_ferry.txt', "The dichotomy of (R140)'s component 4 - that f4 needs\neither H-MAX (a zero of maximal real part,\n"
        "RestBound.lean:389) or a sequence toward the supremum of\nreal parts - is withdrawn as the wrong dichotomy. It was the\n"
        "navigator's.")
E144 = ('b534_ferry.txt', 'is L3\'s standing window context, as the seat read\nit. The reading is ratified and the DERIVES grades stand.')
E145 = ('b535_ferry.txt', "its ten backtick possessives become apostrophes")
ERRORS = dict(r143=E143, r144=E144, r145=E145)

WORKORDERS = [
    ('W-ORD-XI-P7', '(R134)(1), b524', '(R135)(3)(a)', 'CLOSED at b526, (R137)(1)'),
    ('W-ORD-SMOOTH-TAIL', '(R138), b528', 'a rigorous tail on the kernel`s plateau', 'OPEN'),
    ('W-ORD-WEIL-CONVERSE', '(R124)(2), b515', '(R135)(3)(b), then (R139)-(R144)',
     '(d) b517; f1 b524; f2 b529 (INTERFACES on farSmall); f3 b530; f4 b533-b534 -- h2_sign ↔ rh_strip compiled; CLOSED, '
     'the seam rh_strip_imp_rh named and not proved'),
]


def norm(s):
    s = (s or '').replace('’', '').replace("'", '').replace('`', '').replace('*', '').replace('#', '')
    return re.sub(r'\s+', ' ', s).strip().lower()


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def defects(act):
    t = rd(os.path.join(D, 'b%d_defects.txt' % act))
    return len(re.findall(r'^    \([a-z]\) ###', t, re.M)) + len(re.findall(r'^### \(D\d+\)', t, re.M))


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
    ft = rd(FIND)
    res['heading_already_present'] = HEADING in ft
    res['finding_present'] = ('## ' + FTITLE) in ft
    res['finding_line'] = ft.split(NL).index('## ' + FTITLE) + 1 if res['finding_present'] else None
    miss = [x for k in ('quotes', 'defects', 'rulings') for x in res[k] if not x['found']] + [k for k, v in res['errors'].items() if not v]
    res['ok'] = (not miss and [r[0] for r in ROWS] == list(range(LO, HI + 1)) and not res['heading_already_present']
                 and res['finding_present'])
    if verbose:
        print('  span read from b535_span.json : b%d - b%d, %d acts ; the tool reads %d through this act'
              % (LO, HI, HI - LO + 1, SPAN['current_span']))
        print('  verdict strings : %d ; matched in their own closing bank : %d' % (len(res['quotes']), sum(q['found'] for q in res['quotes'])))
        print('  defects : %s ; total %d' % ({d['act']: d['n'] for d in res['defects']}, sum(d['n'] for d in res['defects'])))
        print('  rulings : %d ; BEGIN, END and opening matched in the named ferry : %d' % (len(res['rulings']), sum(r['found'] for r in res['rulings'])))
        print('  errors block sources : %s' % res['errors'])
        print('  this act`s finding present in FINDINGS : %s (line %s)' % (res['finding_present'], res['finding_line']))
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


STATEMENT = ('**In this arc the kernel’s plateau was found to be a choice and then made concrete (b526, b527), ξ read positive at '
             'order 7 on both windows (b526, b528), the pair’s term and the rest of the zero sum bounded in the kernel (b529, b530), '
             'the deposit’s Route 3 premise read as RH restated and the deposited sentences read against it (b531, b532), and '
             'Weil’s criterion compiled in the kernel’s own objects — `h2_sign ↔ rh_strip` at the standard three, `h2_sign → '
             'RiemannHypothesis` compiled from the seam `rh_strip_imp_rh`, which is not proved (b533, b534). No statement about '
             'where the zeros of ζ lie moved.**')


def section(res):
    c = cols()
    tot = sum(d['n'] for d in res['defects'])
    L = [HEADING, '',
         '**Nine acts, b%d through b%d — `(R145)`(5)’s fold.** `b363_span.py` reads **%d** through this filing act; the fold’s own '
         'span, the filing act excluded as at b507, b516 and b525, is **%d**.' % (LO, HI, res['span']['tool_reads'], res['span']['acts']),
         '', '### The arc in one statement', '', STATEMENT,
         '', '### The span, act by act, each verdict verified in its own closing bank', '',
         '| act | subject | its verdicts, as its bank prints them | column |', '|:--|:--|:--|:--|']
    for act, subj, quotes, col, bord in ROWS:
        q = ' · '.join('`%s`' % x.replace('`', "'").replace('|', '/') for x in quotes)
        L.append('| **b%d** | %s%s | %s | %s |' % (act, subj, (' — *%s*' % bord.replace('`', "'")) if bord else '', q, col))
    L += ['', '**%d verdict strings across %d acts, every one matched in that act’s own closing bank**, by `tools/b535_fold.py '
          'check` before this section was written.' % (len(res['quotes']), len(ROWS)),
          '', '### The three columns, kept apart', '',
          '**Statements about the object: %d. About the model: %d. About the record: %d.** b534’s row is a theorem relating two '
          'premises about the zeros of ζ — Weil’s criterion in the kernel’s objects — and says so; it places no zero. **The object '
          'column is empty.**' % (c['OBJECT'], c['MODEL'], c['RECORD']),
          '', '### What the arc established, each at its own address', '',
          '- **`W-ORD-XI-P7` closed: ξ positive beyond its bound at ramp order 7 at 46 of 46 widths to 60**; the kernel’s plateau '
          'found to be a `Classical.choice` base with no values (b526).',
          '- **The plateau made concrete**: two `Real.smoothTransition` factors, `#print` showing so; b524’s statements unchanged (b527).',
          '- **On the kernel’s plateau ξ positive at 46 of 46 widths; Q0 within reach at none**, every tail an estimate — '
          '`W-ORD-SMOOTH-TAIL` filed (b528).',
          '- **(f)(ii) compiled as far as it derives**: the pair’s algebra and near factor DERIVES, the far factor INTERFACES on '
          '`farSmall` (b529). **f3 compiled**: `rest_bound` under H-COUNT, `rest_bound_zeta` hypothesis-free; `not_f4_needs` for '
          'the widening route (b530).',
          '- **`ConservationHypothesis` is RH restated** by the kernel’s own `balance_theorem`; the Route 3 terminal ENCODES-CONCLUSION '
          'against "h2_sign → RH" (b531); 31 deposited sentences read, 14 RESTS, E-2026-09-25-1 drafted, `ch_iff_rh` compiled (b532).',
          '- **f4 in two acts**: the window, the powers, the dominant zero and the interpolant (b533, 34 of 34 at the standard '
          'three); the limit and the assembly, `h2_sign ↔ rh_strip` and `h2_sign_imp_rh_of_seam` (b534, 89 of 89).',
          '- **The finding, filed at b535, the fold’s last item**: *%s* (`FINDINGS.md`:%s), with SIDE-explicit-formula tagged '
          '`v0.1` = `baed4df`, E-2026-09-25-1 filed deposit-facing, the three descriptions edited and fetched back (E-2026-09-25-2), '
          'and the ceiling reworded under `(R145)`(2).' % (FTITLE, res['finding_line']),
          '', '### Errors entered as their owners’', '',
          '**`(R140)`’s component-4 dichotomy, withdrawn.** b533’s ferry, `(R143)`(2): *“%s”*' % q1(*E143),
          '',
          '**b533’s undeclared hypothesis, ratified.** b534’s ferry, `(R144)`(1): the support hypothesis on `power_contDiff` and '
          '`paperFT_power` *“%s”*' % q1(*E144),
          '',
          '**`(R145)`(3)’s count.** *“%s”* — the draft carries nine; the filed entry says so (b535).' % q1(*E145),
          '',
          '**The seat’s, as its acts entered them: %d defects of their own instruments across all nine acts.** The recurrent '
          'species: **a name or a form the seat assumed and the kernel or the ledger already held** (b534’s `window`, b534’s `|` '
          'in a row cell, b532’s backtick in a verbatim sentence), and **a transient stop taken as a verdict** (b527’s own timeout).'
          % tot,
          '', '### The rulings of the span, with the file that ratifies each', '',
          '| ruling | ratified in | status as the record holds it |', '|:--|:--|:--|']
    for (r, f, _o, st), x in zip(RULINGS, res['rulings']):
        L.append('| `(R%d)` | relay `data/%s` | %s |' % (r, f, st))
    L += ['', '### The work-orders, carried with their triggers', '',
          '| work-order | filed | trigger | status |', '|:--|:--|:--|:--|']
    for wo, f, t, s in WORKORDERS:
        L.append('| `%s` | %s | %s | %s |' % (wo, f, t.replace('`', "'"), s))
    L += ['', '### Filed with this fold, not done by it', '',
          '- **The ceiling, reworded, `(R145)`(2)**: in README beside its older sentence, in REGISTRY pinned to the tag, in the '
          'trail beside b532’s interim sentence; the older sentences stand.',
          '- **Not this act, `(R145)`(7)**: the seam’s proof; K1; the register-depth read; the mirror refresh (the author’s '
          'export) and the memory refresh, on the author’s word.',
          '',
          '**No expectation of the span is re-scored.** No corpus grade moved by the fold. Row U1 unedited; **`h2` where the deposit '
          'left it**; **the four lists stay OPEN**; no claim about RH in either direction.',
          '', '*Filed by b%d (relay `data/b535_fold.json`, `tools/b535_fold.py`). Nothing above this section was edited; no grade is '
          'conferred by a seat; nothing is minted; nothing is claimed about `h2`.*' % (HI + 1), '']
    return NL.join(L)


def digest_block():
    return NL.join([
        '', DMARK, '',
        '**Orientation refresh — filed b535, 2026-09-25 *(additive)*.** Under `(R31)` this fold refreshes the digest with one arc:',
        '',
        '- **b%d–b%d — %s**, folded at b535. Its one statement, quoted: %s' % (LO, HI, TITLE, STATEMENT),
        '',
        '**The object column of this arc is empty**: the equivalence it compiled is Weil’s criterion in the kernel’s objects, not a '
        'statement about where the zeros are; `h2` stands where the deposit left it. The claim ceiling now reads as `(R145)`(2) '
        'words it (README, REGISTRY at tag `v0.1`).',
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
               heading=HEADING, workorders=[list(x) for x in WORKORDERS])
    d = (json.dumps(res, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(OUT + '.tmp', 'wb').write(d)
    os.replace(OUT + '.tmp', OUT)
    for x in (w1, w2):
        print('  %(file)s : %(before)d + %(added)d = %(after)d bytes ; prefix %(prefix)s ; BOM kept %(bom)s ; lines removed %(removed)d' % x)
    print('  markers : %s' % res['markers'])
    return 0


if __name__ == '__main__':
    sys.exit({'check': lambda: 0 if check()['ok'] else 1, 'write': write}[sys.argv[1]]())
