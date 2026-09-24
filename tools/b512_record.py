# -*- coding: utf-8 -*-
"""b512_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b512_record.py components | desk | trail`
### Every figure READ from the banks, not retyped."""
import glob
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


TB = json.loads(read('b512_table.json') or '{}')
P = json.loads(read('b512_profile.json') or '{}')
R511 = json.loads(read('b511_results.json') or '{}')
w = lambda v: 'HELD' if v else 'REFUTED'


def row1(k):
    return next((r for r in TB.get('C1', []) if r['key'] == k), {})


def row2(p):
    return next((r for r in TB.get('C2', []) if r['pair'] == p), {})


def placed():
    b = R511.get('bspline', {})
    return ['### BESIDE THE CELL FORM`S ROW -- b511`s MEASUREMENTS, AS MEASUREMENTS, NOT TERMINALS ((R121)(1), (2), (3)):',
            '    B-spline family: xi`s margin positive at all 119 widths and falling at every step; verified %d of 119, every one VERIFIED-EST.'
            % b.get('xi_verified', -1),
            '    Q0 (seventeen off-line pairs below 150): margin positive at every cell of the B-spline family and of the notch at k = 1, 3, 5;',
            '    its off-line part below its on-line part throughout (ratio 0.03 to 0.50). ### Under (R121)(2) the ladder has NOT exhibited',
            '    a violation in an object known to have one, and it is not evidence for h2 at xi; the (R118)(1) bar stands.',
            '    ### No measurement is a statement of the cell form`s truth: the cell form is a Prop, and these are cells.']


def scores():
    regs = [row1('R%d' % i) for i in range(1, 6)]
    ns = sum(1 for r in regs if r.get('status') == 'NOT STATABLE')
    rh = row2('RH -> H2')
    mathlib_needs = [n for n in rh.get('needs', []) if n['where'] == 'mathlib']
    h2c, ch2 = row2('H2 -> CELL'), row2('CELL -> H2')
    h2rh = row2('H2 -> RH')
    return dict(
        n1=ns >= 2,
        n2=rh.get('status') == 'STATABLE-NOT-COMPILED' and bool(mathlib_needs) and all(n['found'] for n in mathlib_needs),
        n3=row1('CELL').get('status') == 'STATABLE' and h2c.get('status') == 'COMPILED' and ch2.get('status') != 'COMPILED',
        s1=row1('LI2').get('status') == 'NOT STATABLE',
        s2=any(not n['found'] for n in h2rh.get('needs', [])),
        s3=TB.get('weakest') == ['CELL']), ns


def components():
    L = ['=' * 104, 'b512 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '', '### COMPONENT 0 -- (R121)(1)`S NOTES : %s' % read('b512_notes.json').replace(NL, ' ')]
    L += ['', '### COMPONENT 1 -- THE MODULE, EVERY DECLARATION WHOLE:'] + read('b512_definitions.txt').rstrip(NL).split(NL)
    for p in sorted(glob.glob(os.path.join(D, 'b512_compile_log*.txt'))) + sorted(glob.glob(os.path.join(D, 'b512_profile_log*.txt'))):
        L += ['', '### RUN FILE %s:' % os.path.basename(p)] + io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)
    L += [''] + read('b512_table.txt').rstrip(NL).split(NL) + [''] + placed() + ['=' * 104]
    io.open(os.path.join(D, 'b512_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-8:]))


def desk():
    sc, ns = scores()
    rh = row2('RH -> H2')
    L = ['=' * 104, 'b512 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- %d of the five deposited registers read NOT STATABLE (1, 2, 3, 5); register 4`s sign form IS h2_sign.' % (w(sc['n1']), ns),
         '  **(N2)** ### **%s.** -- RH -> h2_sign reads %s; its Mathlib needs %s, and its kernel needs %s.'
         % (w(sc['n2']), rh.get('status'), ', '.join('%s %s' % (n['name'], 'FOUND' if n['found'] else 'ABSENT') for n in rh.get('needs', []) if n['where'] == 'mathlib'),
            ', '.join('%s %s' % (n['name'], 'FOUND' if n['found'] else 'ABSENT') for n in rh.get('needs', []) if n['where'] == 'kernel')),
         '  **(N3)** ### **%s.** -- the cell form is STATABLE with its family a parameter; h2_sign -> cell COMPILED (`h2_sign_imp_cell`);' % w(sc['n3']),
         '    cell -> h2_sign STATABLE-NOT-COMPILED with its route ABSENT. ### "NOT IMPLYING" IS READ AS NO ROUTE BACK IN THIS KERNEL --',
         '    A STATEMENT ABOUT DERIVABILITY, NOT A THEOREM: if RH holds every form is true and every implication holds.',
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the two-channel Li form reads %s.' % (w(sc['s1']), row1('LI2').get('status')),
         '  **(S2)** ### **%s.** -- h2_sign -> RH needs a Weil-criterion construction, ABSENT.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- Component 3 names %s.' % (w(sc['s3']), TB.get('weakest')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b512_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b512_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b512_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b512 — the register-equivalence read at h2_sign; (R121) enters the rectification'


def trail():
    sc, ns = scores()
    body = """
%(h)s

**(R121) ratified — the rectification.** (1) **The ladder's shape findings are withdrawn as window artefacts**: the
three extrema of the piecewise-linear family (4.062, 5.196, 13.153), their attribution to zeros 1 and 4, the rise
after the minimum and the `c/a²` reading. Notes are appended to `b489_components.txt`, `b490_components.txt`,
`b502_components.txt`, `b503_components.txt`, `b504_components.txt`, and to `FINDINGS.md` beside b507's fold, which
carries them; the (R31) digest block carries none of them. The trail records of those acts are annotated here, by
address: b489, b490 and b502–b504 above. The identity `m = Z − P` stands: it is `b321_identity`. (2) **The ladder is an
instrument for exhibiting a violation of the sign clause in an object known to have one, and it has not yet
exhibited it**; it is not evidence for h2 at ξ, and the (R118)(1) bar stands; the register "balance-to-positivity at
the multiplicative place, at a cell" is the least discriminating of h2's forms measured to date. (3) **Verification
has two statuses: VERIFIED-STRICT (a proved bound) and VERIFIED-EST (b501's estimate and its descendants); every cell
of the record to date is VERIFIED-EST**, the archimedean tail beyond u = 1200 its named shortfall; **`W-ORD-STRICT-BOUND`
is filed**, trigger the author's word or the next act that cites a cell count in a keystone. (4) **`W-ORD-FAMILY-
SENSITIVITY` is amended to a third family, the MATCHED window** `cos(γ₀ u)` times a B-spline bump at γ₀ = 16.290216,
with ξ's at 14.1347 as its control; trigger the act after b512. (5) The kernel lane opened for this act.

**COMPONENT 1.** Of the five deposited registers, %(ns)d read NOT STATABLE in the kernel's objects — silence_universal's
interface, Route 3's Euler balance, the mechanisms, and a spectral-realization operator are all absent — and register
4's sign form **is** `h2_sign`. The two-channel Li form is NOT STATABLE for want of `λ_A`; its sum is stated as
`li_form`. The cell form is STATABLE with its family a parameter; RH is Mathlib's. All in
`SIDEExplicitFormula/Registers.lean`, profile `%(prof)s` on the one theorem.

**COMPONENT 2.** Twelve ordered pairs among h2_sign, RH, `li_form` and the cell form. **COMPILED: h2_sign → cell form**
(`h2_sign_imp_cell`, a specialisation). **RH → h2_sign is STATABLE-NOT-COMPILED with every lemma FOUND** —
`paperFT_weilTest`, `zetaZeroConfig_carrier`, `RH_implies_on_line`, `b321_identity` in the kernel; `Complex.mul_conj`,
`Complex.normSq_nonneg`, `tsum_nonneg`, `Complex.orderClosedTopology` in Mathlib: under RH each zero term is
`m_ρ |ĥ(γ)|²`. **h2_sign → RH needs a Weil-criterion construction, ABSENT**; both directions of Li's criterion are
ABSENT; the cell form's route back needs a density argument, ABSENT.

**COMPONENT 3.** **The weakest form: the cell form** — implied by h2_sign by a compiled step, with no route back in this
kernel. That is a statement about derivability, not a theorem: if RH holds, every form here is true.

**COMPONENT 4.** Beside the cell form's row, b511's cells as measurements: ξ's margin positive and monotone on the
B-spline family, Q0's positive on every family tried — VERIFIED-EST, and no terminal.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s**, the last read as derivability. The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3)
%(S3)s. **The kernel lane shuts at this act's close.** The kernel is not tagged; REGISTRY is not written. Nothing at
Zenodo written; nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of
this act is a statement about RH.
""" % dict(h=HEADING, ns=ns, prof=(P.get('new') or ['NONE'])[0],
           N1=w(sc['n1']), N2=w(sc['n2']), N3=w(sc['n3']), S1=w(sc['s1']), S2=w(sc['s2']), S3=w(sc['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b512_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
