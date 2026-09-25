# -*- coding: utf-8 -*-
"""b516_fold.py -- THE FOLD AT SPAN EIGHT, b508 THROUGH b515. ### `python tools/b516_fold.py check | classk | write`

### ### **A FOLD RESTATES AND MINTS NOTHING.** ### b507's pattern: every verdict string QUOTED from its own act's closing
### bank and matched there (markup, apostrophes and whitespace normalised) before `write` runs; `write` REFUSES unless
### `check` passes, and only APPENDS -- one section to `FINDINGS.md`, one block to the (R31) digest, each prior byte string
### proved a true prefix. ### The span is READ from `b516_span.json`, never typed.
### ### `classk` -- (R125)(3)'s reading of classK, PRINTED FROM `H2Sign.lean` AT THE KERNEL'S HEAD, and READING (8)'s
### demonstration: `h = i phi` (not real) gives `h * h~ = phi * phi`, even; `h = e^{i gamma u} phi` gives `h * h~` not even.
"""
import io
import json
import math
import os
import re
import subprocess
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FIND = os.path.join(PP, 'FINDINGS.md')
DIG = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
OUT = os.path.join(D, 'b516_fold.json')
CK = os.path.join(D, 'b516_classk.json')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SPAN = json.load(io.open(os.path.join(D, 'b516_span.json'), encoding='utf-8'))
LO, HI = SPAN['span_starts_at'], SPAN['this_act'] - 1
TITLE = 'THE CHAIN AND THE WINDOW ARC'
HEADING = '## %s, b%d–b%d — THE FOLD' % (TITLE, LO, HI)
DMARK = '<!-- b516 orientation refresh: the chain and the window arc -->'

ROWS = [
    (508, 'the Epstein margin read on the completed Q0 bank, beside ξ',
     ['THE EPSTEIN MARGIN POSITIVE AT ALL 83 CELLS WHERE BOTH KERNELS VERIFY.'], 'MODEL',
     'BORDERLINE -- a statement about the control function Z_Q0, which is not the object'),
    (509, 'b321’s identity derived in `SIDE-explicit-formula`, graded against the ladder',
     ['b321`S IDENTITY DERIVED; INTERFACES AGAINST THE LADDER; THE TABLE ROW NOT MADE.'], 'MODEL', ''),
    (510, 'h2 stated as one `Prop` on the derived class; the table row made',
     ['h2 STATED AS ONE Prop; THE TABLE ROW MADE; W-ORD-PL-CLASS PRICED.'], 'MODEL', ''),
    (511, 'two families inside the compiled class, ξ and Q0',
     ['XI`S MARGIN MONOTONE IN THE B-SPLINE FAMILY; NO NEGATIVE EPSTEIN CELL IN THE NOTCH.'], 'MODEL', ''),
    (512, 'the register-equivalence read at h2_sign; `(R121)`’s rectification',
     ['THE REGISTER-EQUIVALENCE READ; THE RECTIFICATION ENTERED.',
      "weakest : ['CELL'] -- a statement about derivability, not a theorem"], 'MODEL', ''),
    (513, 'RH → h2_sign compiled, and the chain to the cell form',
     ['RH -> h2_sign COMPILED, UNDER (R122).', 'attempts 2, the first to succeed 2 ; the proof 39 lines'], 'MODEL',
     'BORDERLINE -- an implication whose hypothesis is RH; it says nothing of whether RH holds'),
    (514, 'the matched window, cos(γ₀u) times a bump, at Q0’s off-line pair',
     ['THE MATCHED WINDOW, UNDER (R123).',
      'reading : no Q0 cell is negative on a closing bank: the converse`s construction is harder than a modulated bump'],
     'MODEL', ''),
    (515, 'the window with a zero at the on-line point',
     ['fixture : xi MET 6.55e-11 ; q NOT MET 1.24e-10 (bar 1e-10)',
      'P - PR + A negative NONE ; positive 119 ; pair negative 64, positive 55'], 'MODEL', ''),
]

DEFECTS = {508: (1, 'OWN DEFECTS -- ONE.'), 509: (6, 'OWN DEFECTS -- SIX;'), 510: (5, 'OWN DEFECTS -- FIVE.'),
           511: (5, 'OWN DEFECTS -- FIVE (the desk'), 512: (2, 'OWN DEFECTS -- TWO (the desk).'),
           513: (3, 'OWN DEFECTS -- THREE (the desk).'), 514: (4, 'OWN DEFECTS -- FOUR (the desk).'),
           515: (3, 'OWN DEFECTS -- THREE (the desk).')}

RULINGS = [
    (118, 'b509_ferry.txt', 'b508 IS READ AS A NEGATIVE RESULT ABOUT THE INSTRUMENT'),
    (119, 'b510_ferry.txt', 'THE TABLE ROW IS MADE THE FEDERATION`S WAY'),
    (120, 'b511_ferry.txt', 'W-ORD-PL-CLASS IS TAKEN AT DISPOSITION (b)'),
    (121, 'b512_ferry.txt', 'THE LADDER`S SHAPE FINDINGS ARE WITHDRAWN AS WINDOW ARTEFACTS.'),
    (122, 'b513_ferry.txt', 'IS COMPILED BEFORE THE MATCHED WINDOW IS MEASURED'),
    (123, 'b514_ferry.txt', 'IS ENTERED AT ITS MEANING'),
    (124, 'b515_ferry.txt', 'b514 IS ENTERED WITH ITS MECHANISM'),
    (125, 'b516_ferry.txt', 'b515 IS ENTERED AS THE SIGN HALF OF (f)'),
]
STATUS = {118: 'executed at b509', 119: 'executed at b510', 120: 'executed at b511', 121: 'executed at b512',
          122: 'executed at b513 and b514', 123: 'executed at b514', 124: 'executed at b515', 125: 'executed at b516, this fold'}

# ### (R121)(1)'s WITHDRAWALS, QUOTED FROM b512's FERRY, AND (R125)(1)'s READING, QUOTED FROM THIS ACT'S FERRY.
W121 = 'THE LADDER\'S SHAPE FINDINGS ARE WITHDRAWN AS WINDOW ARTEFACTS.'
R125 = 'Neither b514\'s window (second\nproperty alone) nor b515\'s (the zero alone) is the witness'

WORKORDERS = [
    ('W-ORD-TABLE-PROFILE-JSON', '(R123)(2), b514', 'the next fold -- THIS fold', 'EXECUTED inside this fold, `tools/terminal_table.py`'),
    ('W-ORD-TABLE-SHORTNAME-DEDUP', '(R123)(2), b514', 'the next fold -- THIS fold', 'EXECUTED inside this fold, `tools/terminal_table.py`'),
    ('W-ORD-WEIL-CONVERSE', '(R124)(2), b515', 'the kernel lane after this fold; (d) first', 'PRICED here in lemmas, not attempted'),
]

LEMMAS = [
    ('d', 'the growth bound: for h supported in [-L, L], |paperFT h z| <= ||h||_1 exp(L |Im z|) -- in the kernel`s convention '
          'the exponent is |Im z| of the transform`s argument, which is |Re s - 1/2| of the zero',
     'ONE LEMMA from the integral: norm of the integral below the integral of the norm, |e^{izu}| = e^{-u Im z} <= e^{L |Im z|} on '
     'the support; Mathlib`s norm-of-integral bound and the support restriction carry it', 'days'),
    ('f1', 'the two-property window family: (gamma_0^2 - z^2) applied to a window band-limited near gamma_0, and its membership '
           'in classK (real-valued, or complex with h * h~ even -- READING (8))', 'a definition and a classK proof on the '
           'pattern of b513`s obtain/rfl, plus C^2 and compact support of the product', 'about a week'),
    ('f2', 'its term at rho_0 bounded below: the four images of an off-line zero give a negative real part of order '
           'delta^2 (slope)^2, the slope -2 gamma_0 times the band-limited transform at gamma_0', 'a complex-analytic estimate '
           'on a closed form; the leading term and its remainder, both bounded', 'about a week'),
    ('f3', 'the remaining zeros bounded above: the on-line terms away from gamma_0 and the other off-line terms, summed with the '
           'kernel`s `zetaZeroConfig_local_count` and (d)', 'a summation lemma over the zero configuration with a tail from '
           'the local count; the band-limit gives the decay', 'one to two weeks'),
    ('f4', 'the assembly: from not-RH, an off-line rho_0, the window at its ordinate, zeroSide k < 0 for a width large enough, '
           'b321_identity, and not h2_sign', 'composition of f1-f3 with b513`s pieces', 'days'),
]


def norm(s):
    s = (s or '').replace('’', '').replace("'", '').replace('`', '').replace('*', '').replace('#', '')
    return re.sub(r'\s+', ' ', s).strip().lower()


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def classk():
    """### READING (8): the definition printed from the kernel's HEAD, and the two cases computed by discrete convolution."""
    src = subprocess.run(['git', '-C', KER, 'show', 'HEAD:SIDEExplicitFormula/H2Sign.lean'], capture_output=True,
                         text=True, encoding='utf-8').stdout
    i = src.index('def classK')
    j = src.index('weilTest h h', i) + len('weilTest h h')
    defn = src[i:j]
    ts = subprocess.run(['git', '-C', KER, 'show', 'HEAD:Zeta23/ExplicitFormula.lean'], capture_output=True,
                        text=True, encoding='utf-8').stdout
    tl = next(l for l in ts.split(NL) if l.startswith('def tilde'))
    wl = next(l for l in ts.split(NL) if l.startswith('def weilTest'))
    n, L, g = 4001, 1.0, 16.290216
    u = np.linspace(-L, L, n)
    du = u[1] - u[0]
    phi = np.where(np.abs(u) < L, (1 - (u / L) ** 2) ** 3, 0.0)

    def conv_tilde(h):
        ht = np.conj(h[::-1])                      # ### h~(u) = conj(h(-u)) on the symmetric grid
        return np.convolve(h, ht) * du             # ### k on the grid of sums, symmetric about its centre

    out = []
    for name, h in (('h = i phi (not real)', 1j * phi), ('h = exp(i gamma u) phi', np.exp(1j * g * u) * phi),
                    ('h = cos(gamma u) phi (real)', np.cos(g * u) * phi)):
        k = conv_tilde(h)
        scale = float(np.max(np.abs(k)))
        even = float(np.max(np.abs(k - k[::-1]))) / scale
        imag = float(np.max(np.abs(k.imag))) / scale
        hreal = float(np.max(np.abs(h.imag)))
        out.append(dict(case=name, h_imag_max=hreal, k_even_defect=even, k_imag_rel=imag, admitted=even < 1e-12))
    res = dict(definition=defn, tilde=tl, weilTest=wl, h_type=('h : ℝ → ℂ' in defn), cases=out,
               reading=('classK admits complex-valued h: its generating h has type R -> C, and the binding constraint is that '
                        'k = h * h~ be even, which for a Hermitian k means k real'))
    io.open(CK, 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    print(defn)
    print(tl)
    print(wl)
    for c in out:
        print('  %-30s max|Im h| %.2e ; k even-defect %.2e ; |Im k| %.2e ; ADMITTED %s'
              % (c['case'], c['h_imag_max'], c['k_even_defect'], c['k_imag_rel'], c['admitted']))
    return res


def check(verbose=True):
    res = dict(quotes=[], defects=[], rulings=[])
    for act, _s, quotes, _c, _b in ROWS:
        bank = norm(rd(os.path.join(D, 'b%d_closing.txt' % act)))
        for q in quotes:
            res['quotes'].append(dict(act=act, quote=q, found=norm(q) in bank))
    for act, (n, phrase) in DEFECTS.items():
        res['defects'].append(dict(act=act, n=n, phrase=phrase, found=norm(phrase) in norm(rd(os.path.join(D, 'b%d_closing.txt' % act)))))
    for r, f, opening in RULINGS:
        t = rd(os.path.join(D, f))
        res['rulings'].append(dict(ruling=r, file=f, found=('RULING (R%d) BEGIN' % r) in t and ('RULING (R%d) END' % r) in t
                                   and norm(opening) in norm(t)))
    res['errors'] = dict(w121=norm(W121) in norm(rd(os.path.join(D, 'b512_ferry.txt'))),
                         r125=norm(R125) in norm(rd(os.path.join(D, 'b516_ferry.txt'))))
    res['span'] = dict(lo=LO, hi=HI, acts=HI - LO + 1, tool_reads=SPAN['current_span'], filed_by=SPAN['filed_by'])
    ft = rd(FIND)
    res['heading_already_present'] = HEADING in ft
    miss = [x for k in ('quotes', 'defects', 'rulings') for x in res[k] if not x['found']] + [k for k, v in res['errors'].items() if not v]
    res['ok'] = not miss and [r[0] for r in ROWS] == list(range(LO, HI + 1)) and not res['heading_already_present']
    if verbose:
        print('  span read from b516_span.json : b%d - b%d, %d acts ; the tool reads %d through this act'
              % (LO, HI, HI - LO + 1, SPAN['current_span']))
        print('  verdict strings : %d ; matched in their own closing bank : %d' % (len(res['quotes']), sum(q['found'] for q in res['quotes'])))
        print('  defect counts : %d acts ; phrase matched : %d ; total recorded : %d'
              % (len(res['defects']), sum(d['found'] for d in res['defects']), sum(d['n'] for d in res['defects'])))
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


def section(res, ck, table):
    c = cols()
    tot = sum(d['n'] for d in res['defects'])
    L = [HEADING, '',
         '**Eight acts, b%d through b%d — `(R124)`(3)’s fold at span 8.** `b363_span.py` reads **%d** through this filing act; the '
         'fold’s own span, the filing act excluded as at b507, is **%d**.' % (LO, HI, res['span']['tool_reads'], res['span']['acts']),
         '', '### The arc in one statement', '',
         '**In this arc the kernel compiled that RH implies h2_sign and h2_sign the cell form, so h2_sign is at most as strong as RH; '
         'the converse was priced as a construction and then approached by measurement — a window peaked at the off-line zero’s '
         'height made its pair positive, a window vanishing there turned the pair negative but left it ten thousand times smaller '
         'than the low zeros — which is the shape of the classical converse: a zero at the point and concentration near it, at once.**',
         '', '### The span, act by act, each verdict verified in its own closing bank', '',
         '| act | subject | its verdicts, as its bank prints them | column |', '|:--|:--|:--|:--|']
    for act, subj, quotes, col, bord in ROWS:
        q = ' · '.join('`%s`' % x.replace('`', "'").replace('|', '/') for x in quotes)
        L.append('| **b%d** | %s%s | %s | %s |' % (act, subj, (' — *%s*' % bord) if bord else '', q, col))
    L += ['', '**%d verdict strings across %d acts, every one matched in that act’s own closing bank**, by `tools/b516_fold.py '
          'check` before this section was written.' % (len(res['quotes']), len(ROWS)),
          '', '### The three columns, kept apart', '',
          '**Statements about the object: %d. About the model: %d. About the record: %d.** Two rows are borderline and say so: b508 '
          '(the control function) and b513 (an implication whose hypothesis is RH). **The object column is empty**: a compiled '
          'implication from RH is not a statement that RH holds, and a window measured on a finite chart is a statement about the '
          'window.' % (c['OBJECT'], c['MODEL'], c['RECORD']),
          '', '### What the arc established, each at its own address', '',
          '- **The Epstein margin is positive at all 83 cells where both kernels verify** (b508) — the ladder’s positivity does not '
          'separate ξ from an object with off-line zeros (`(R118)`).',
          '- **b321’s identity is derived in the kernel, standard three** (b509); **h2 is one `Prop`** on the class the kernel derives, '
          'the table row made by `AxiomCheck.lean` (b510).',
          '- **On a C² family the old extrema were window artefacts** (b511), withdrawn by `(R121)` (b512).',
          '- **Four of five deposited registers are NOT STATABLE in the kernel; the cell form is the weakest, as derivability** (b512).',
          '- **RH → h2_sign and RH → cell form compile, standard three** (b513); the converse is a `Prop`, its (d) and (f) ABSENT.',
          '- **A window peaked at γ₀ makes the pair positive** (b514); **a window zeroed at γ₀ turns its sign but leaves it about '
          '1e-4 of the rest** (b515).',
          '', '### Errors entered as their owners’', '',
          '**`(R121)`’s withdrawals, carried.** b512’s ferry: *“%s”* — the extrema 4.062, 5.196 and 13.153, their attribution to '
          'zeros 1 and 4, the rise after the minimum and `c/a²`, all readings of b489–b504, withdrawn in this span by notes '
          'appended to their banks.' % W121.replace("'", '’'),
          '',
          '**`(R125)`(1)’s reading, entered.** This act’s ferry: *“Neither b514’s window (second property alone) nor b515’s (the '
          'zero alone) is the witness”* — the witness is their product, `(γ₀² − z²)` applied to a window band-limited near γ₀, '
          'its growth in the width what (d) bounds.',
          '',
          '**The seat’s, as its acts entered them: %d defects of their own instruments across all eight acts.** The recurrent '
          'species: a price stated from a prior act’s cost (b508, b509, b510, b514), and **a fixture floor set below the route’s '
          'own floor** (b515), which `(R125)`(2) now rules on. b515’s NOT CLEAN verdict on `G-FIXTURE-BAR` stands as registered.'
          % tot,
          '', '### The rulings of the span, with the file that ratifies each', '',
          '| ruling | ratified in | status as the record holds it |', '|:--|:--|:--|']
    for r in res['rulings']:
        L.append('| `(R%d)` | relay `data/%s` | %s |' % (r['ruling'], r['file'], STATUS[r['ruling']]))
    L += ['', '### Disposed inside this fold, on `(R125)`(4)', '',
          '- **`W-ORD-TABLE-PROFILE-JSON` and `W-ORD-TABLE-SHORTNAME-DEDUP`**, executed in `tools/terminal_table.py` with fixtures '
          'in both polarities; the regenerated table at this close: rows gone %s, rows added %s, grade-or-profile changed %s. '
          '**The JSON reader was repaired twice inside the fold**: its first two runs read b456’s bank — a search whose verdict '
          'is ABSENT — as three profiles of `SIDE-kernel`, from quotations of documents; a quotation its bank marks not printed '
          'against its ref, and a record carrying a file and a line, are now refused, each with a fixture both ways, and both '
          'runs are banked (`b516_table_first*`, `b516_table_second_run.txt`).'
          % (table.get('gone'), table.get('added'), table.get('changed')),
          '', '### The three work-orders, carried with their triggers', '',
          '| work-order | filed | trigger | status |', '|:--|:--|:--|:--|']
    for w, f, t, s in WORKORDERS:
        L.append('| `%s` | %s | %s | %s |' % (w, f, t, s))
    L += ['', '### `W-ORD-WEIL-CONVERSE`, priced in lemmas, not days — `(R125)`(3)', '',
          '| lemma | statement | how | price |', '|:--|:--|:--|:--|']
    for k, s, how, p in LEMMAS:
        L.append('| (%s) | %s | %s | %s |' % (k, s.replace('|', '/'), how.replace('|', '/'), p))
    L += ['', '**(d) is one lemma. (f) is research-grade: four lemmas, weeks, stated as weeks.**',
          '',
          '**classK, as `H2Sign.lean` states it at the kernel’s head:** `%s`. **Its generating `h` has type `ℝ → ℂ`: classK admits '
          'complex-valued h, the binding constraint being that `k = h ⋆ h~` be even.** Computed on a grid: %s. **So the classical '
          'modulated `e^{iγu}φ` is excluded by evenness, not by type, and its real part `cos(γu)φ` is admitted** — the converse’s '
          'construction needs a real-valued variant or an even combination, not a widened class.'
          % (ck['definition'].replace(NL, ' ').replace('  ', ' '),
             '; '.join('%s — even-defect %.1e, %s' % (x['case'], x['k_even_defect'], 'ADMITTED' if x['admitted'] else 'NOT admitted')
                       for x in ck['cases'])),
          '', '### Filed with this fold, not done by it', '',
          '- **`(R125)`(2), the fixture rule: a fixture floor is priced in the quantity’s own scale — eps times the sum of the '
          'magnitudes of the terms the closed form adds — not as an absolute figure.**',
          '- **The kernel lane reopens for the act after this fold, which is (d).**',
          '',
          '**No expectation of the span is re-scored.** Nothing compiled. No corpus grade moved. No ERRATA line written. Row U1 '
          'unedited; **`h2` where the deposit left it**; **the four lists stay OPEN**; no claim about RH in either direction.',
          '', '*Filed by b%d (relay `data/b516_fold.json`, `tools/b516_fold.py`). Nothing above this section was edited; no grade is '
          'conferred by a seat; nothing is minted; nothing is claimed about `h2`.*' % (HI + 1), '']
    return NL.join(L)


def digest_block():
    return NL.join([
        '', DMARK, '',
        '**Orientation refresh — filed b516, 2026-09-24 *(additive)*.** Under `(R31)` this fold refreshes the digest with one arc:',
        '',
        '- **b%d–b%d — %s**, folded at b516. Its one statement, quoted: **In this arc the kernel compiled that RH implies h2_sign '
        'and h2_sign the cell form, so h2_sign is at most as strong as RH; the converse was priced as a construction and then '
        'approached by measurement — a window peaked at the off-line zero’s height made its pair positive, a window vanishing there '
        'turned the pair negative but left it ten thousand times smaller than the low zeros — which is the shape of the classical '
        'converse: a zero at the point and concentration near it, at once.**' % (LO, HI, TITLE),
        '',
        '**The governing claim at the head of this document is unchanged by this arc**, whose object column is empty: a compiled '
        'implication from RH is a statement about derivability, and `h2` stands where the deposit left it.',
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


def table_diff():
    d = json.loads(rd(os.path.join(D, 'terminal_table_diff.json')) or '{}')
    return dict(gone=len(d.get('gone') or []), added=len(d.get('added') or []), changed=len(d.get('changed') or []))


def write():
    res = check(verbose=True)
    if not res['ok']:
        print('### REFUSED -- THE CHECK DID NOT PASS; NOTHING WRITTEN.')
        return 2
    ck = json.loads(rd(CK))
    tbl = table_diff()
    sec = section(res, ck, tbl)
    w1 = append(FIND, NL + sec)
    w2 = append(DIG, digest_block())
    ft, dt = rd(FIND), rd(DIG)
    res.update(writes=[w1, w2], markers=dict(heading=ft.count(HEADING), digest=dt.count(DMARK)), columns=cols(), title=TITLE,
               heading=HEADING, table=tbl, workorders=[w[0] for w in WORKORDERS], lemmas=[l[0] for l in LEMMAS])
    d = (json.dumps(res, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(OUT + '.tmp', 'wb').write(d)
    os.replace(OUT + '.tmp', OUT)
    for w in (w1, w2):
        print('  %(file)s : %(before)d + %(added)d = %(after)d bytes ; prefix %(prefix)s ; BOM kept %(bom)s ; lines removed %(removed)d' % w)
    print('  markers : %s' % res['markers'])
    return 0


if __name__ == '__main__':
    sys.exit({'check': lambda: 0 if check()['ok'] else 1, 'classk': lambda: 0 if classk() else 1, 'write': write}[sys.argv[1]]())
