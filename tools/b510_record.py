# -*- coding: utf-8 -*-
"""b510_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b510_record.py components | desk | trail`
### Every figure READ from the banks, not retyped."""
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


def binder():
    """### READ OFF THE PRINTED STATEMENT: where the class quantifier is, and whether any zero quantifier is there."""
    st = read('b510_definitions.txt')
    h2 = st[st.index('def h2_sign :'):st.index('def h2_sign_aim')] if 'def h2_sign :' in st else ''
    return dict(class_forall=('∀ k : ℝ → ℂ, classK k →' in h2), zeros_in_text=bool(re.search(r'zeroSide|carrier|ρ', h2)))


SENTENCE = ('In `h2_sign` the class quantifier is its one `∀ k : ℝ → ℂ, classK k →`, and the zero quantifier does NOT '
            'appear in its text: it sits inside `zeroSide k` as `∑\' ρ : Zeta23.zetaZeroConfig.carrier`, and reaches '
            '`h2_sign` only through `b321_identity`, which equates `zeroSide k` with `b321Norm * (poleTerm k - primeSum k + '
            'archTerm k)` on the even `C_c^2` functions, a class containing K.')


def components():
    L = ['=' * 104, 'b510 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '', '### COMPONENT 0 -- AxiomCheck.lean, AS RUN IN THE KERNEL:']
    for p in sorted(glob.glob(os.path.join(D, 'b510_axiomcheck_log*.txt'))):
        L += ['### RUN FILE %s:' % os.path.basename(p)] + io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)
    L += ['### the table row and b509`s arm are read POST-PUSH, by the closing suite.', '',
          '### COMPONENT 1 -- THE Prop, FROM EACH DECLARATION LINE TO ITS `:=` (as ordered) :'] + read('b510_statement.txt').rstrip(NL).split(NL)
    L += ['', '### AND EACH DECLARATION WHOLE -- a `def`s content is after its `:=` :'] + read('b510_definitions.txt').rstrip(NL).split(NL)
    for p in sorted(glob.glob(os.path.join(D, 'b510_compile_log*.txt'))) + sorted(glob.glob(os.path.join(D, 'b510_profile_log*.txt'))):
        L += ['', '### RUN FILE %s:' % os.path.basename(p)] + io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)
    L += ['', '### COMPONENT 2 -- THE BINDER READ.', '    ' + SENTENCE, '    read off the statement : %s' % binder(),
          '', '### COMPONENT 3.'] + read('b510_search.txt').rstrip(NL).split(NL) + read('b510_search_widening.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENT 4.'] + read('b510_price.txt').rstrip(NL).split(NL) + ['=' * 104]
    io.open(os.path.join(D, 'b510_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-6:]))


def scores():
    P = json.loads(read('b510_profile.json') or '{}')
    S = json.loads(read('b510_search.json') or '{}')
    R = json.loads(read('b510_price.json') or '{}')
    mod = io.open(os.path.join(KER, 'SIDEExplicitFormula', 'H2Sign.lean'), encoding='utf-8').read()
    none3 = (not S.get('needle1') and not S.get('needle2') and 'VERDICT : NONE' in read('b510_search_widening.txt'))
    needs = R.get('needs') or []
    decay_absent = any(n['name'] == 'fourier_piecewiseLinear_isBigO' and not n['found'] for n in needs)
    others_found = sum(1 for n in needs if n['name'] != 'fourier_piecewiseLinear_isBigO' and n['found'])
    b = binder()
    return dict(n1=bool(P.get('new_std3')) and not P.get('sorry') and 'sorry' not in mod,
                n2=none3, n3=bool(R.get('under_one_hour_xi')),
                s1=b['class_forall'] and not b['zeros_in_text'],
                s2=decay_absent and others_found >= 5,
                s3=R.get('b504_cell_seconds', 0) > 3600), P, S, R, others_found


def desk():
    sc, P, S, R, of = scores()
    w = lambda v: 'HELD' if v else 'REFUTED'
    L = ['=' * 104, 'b510 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- h2_sign and h2_sign_aim elaborate; the theorem, whole string : %s' % (w(sc['n1']), (P.get('new') or ['(none)'])[0]),
         '  **(N2)** ### **%s.** -- needle 1 : %d ; needle 2 : %d ; the widening pass`s hand-read : NONE.'
         % (w(sc['n2']), len(S.get('needle1') or []), len(S.get('needle2') or [])),
         '  **(N3)** ### **%s.** -- b504`s per-cell seconds sum to %.0f cell-seconds, %.0f s under the hour, ON XI ALONE; with the Q0 control'
         % (w(sc['n3']), R['b504_cell_seconds'], 3600 - R['b504_cell_seconds']),
         '    that (R119)(2) takes with it, %.0f cell-seconds. ### The margin is %.0f s on a recorded figure, not a priced bound.'
         % (R['joint_cell_seconds'], 3600 - R['b504_cell_seconds']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- %s' % (w(sc['s1']), binder()),
         '  **(S2)** ### **%s.** -- the decay lemma ABSENT; of the other seven, %d FOUND.' % (w(sc['s2']), of),
         '  **(S3)** ### **%s.** -- %.0f cell-seconds, not above 3600.' % (w(sc['s3']), R['b504_cell_seconds']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc['n1'], sc['n2'], sc['n3']].count(True), [sc['n1'], sc['n2'], sc['n3']].count(False),
            [sc['s1'], sc['s2'], sc['s3']].count(True), [sc['s1'], sc['s2'], sc['s3']].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b510_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b510_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b510_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b510 — h2 stated as one Prop on the class the kernel derives; the table row made; W-ORD-PL-CLASS priced'


def trail():
    sc, P, S, R, of = scores()
    w = lambda v: 'HELD' if v else 'REFUTED'
    body = """
%(h)s

**(R119) ratified.** (1) The table row is made the federation's way, by `AxiomCheck.lean` in SIDE-explicit-formula's
own tree; no ledger cell is written to satisfy a matcher. (2) **`W-ORD-PL-CLASS` is filed**: every cell of the ladder
sits outside the class the kernel derives (even `C_c²`), the windows being piecewise-linear and not C¹; disposition
(a) P-PL proved by a limit of `C²` approximants inside the vendored kernel, disposition (b) the ladder's family
replaced by a `C²` family and the 119 cells re-measured, taken together with `W-ORD-FAMILY-SENSITIVITY`'s second
family if chosen; both priced here, neither taken; trigger the act after b510, on the author's word. (3) h2 is stated
on the class the kernel derives, the pole term carried; the ladder's "sign of A − PR" is the pole-annihilated
specialization, defined beside the Prop and not in its place. (4) The kernel lane opened for this act.

**COMPONENT 0.** `SIDE-explicit-formula/AxiomCheck.lean` prints `b321_identity`, `EF_lit_zetaZeroConfig`, `EF_lit` and
`EF_lit_zeta`; its run is banked. The table row and b509's arm are read at the post-push suite.

**COMPONENT 1.** `SIDEExplicitFormula/H2Sign.lean`: `classK` (even, `C²`, compact support, and `k = weilTest h h` for a
`C²` compactly supported `h`); **`h2_sign : Prop := ∀ k, classK k → 0 ≤ poleTerm k − primeSum k + archTerm k`**, the
order being Mathlib's `ComplexOrder` (real and nonnegative); `h2_sign_aim`, the same under `poleTerm k = 0`; and
`h2_sign_imp_aim`, one line, profile `%(prof)s`. **Stated, not proved: h2 where the deposit left it — stated now as
one Prop, and no truer for it.**

**COMPONENT 2, the binder read.** %(sent)s

**COMPONENT 3.** The fifty-seven modules, %(decls)d declarations: no statement of the shape "zeros on the line →
zeroSide k ≥ 0 for k = h ⋆ h~" nor its contrapositive — **NONE**, the two needles at 0 and a widening pass hand-read
(the residue is counting and location: `RH_implies_on_line`, `RH_implies_all_on_line`, the `N0` counts).

**COMPONENT 4, `W-ORD-PL-CLASS` priced.** (a) Mollify, apply `b321_identity`, pass to the limit by dominated
convergence; of the Mathlib lemmas it needs, %(of)d of 7 are FOUND by the stated search, the compact-support lemma for a
convolution is ABSENT under it, and **the one analytic input outside EF_lit's class — the `O(|r|⁻²)` decay of a
piecewise-linear transform — is ABSENT**. (b) Cubic B-splines in place of the three bumps: `k_a` in K, `C⁶`, transform
`O(|r|⁻⁸)` in closed form; **cost %(xs).0f cell-seconds on ξ from b504's own timing — under one hour by %(mg).0f s** —
and %(js).0f jointly with the Q0 control.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The kernel lane
shuts at this act's close.** The kernel is not tagged; REGISTRY is not written. Nothing at Zenodo written; nothing
deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a
statement about RH.
""" % dict(h=HEADING, prof=(P.get('new') or ['NONE'])[0], sent=SENTENCE, decls=S.get('decls', 0), of=of,
           xs=R['b504_cell_seconds'], mg=3600 - R['b504_cell_seconds'], js=R['joint_cell_seconds'],
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
    io.open(os.path.join(D, 'b510_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
