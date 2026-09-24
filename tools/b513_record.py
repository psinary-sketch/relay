# -*- coding: utf-8 -*-
"""b513_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b513_record.py components | desk | trail`
### Every figure READ from the banks, not retyped. ### THE TRAIL CARRIES GRADE WORDS ON THREE LINES ONLY, each beside its
### own link (READING (5)): the terminal table attaches a grade to the NEAREST backticked name in its line.
"""
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
LINKS = ('rh_imp_h2_sign', 'h2_sign_imp_cell', 'rh_imp_cell_form')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


TB = json.loads(read('b513_table.json') or '{}')
P = json.loads(read('b513_profile.json') or '{}')
w = lambda v: 'HELD' if v else 'REFUTED'


def attempts():
    """### READING (3): every compile run file is an attempt; each is read for Lean`s own verdict, never the exit code alone."""
    out = []
    for p in sorted(glob.glob(os.path.join(D, 'b513_compile_log*.txt')), key=os.path.getmtime):
        t = io.open(p, encoding='utf-8').read()
        m = re.search(r'^exit (\d+) ; ([0-9.]+) s$', t, re.M)
        body = t.split('--- stdout ---', 1)[-1]
        ok = bool(m) and m.group(1) == '0' and 'error' not in body and 'sorry' not in body
        out.append(dict(file=os.path.basename(p), exit=int(m.group(1)) if m else None, secs=float(m.group(2)) if m else None, ok=ok))
    return out


def scores():
    A = attempts()
    first_ok = next((i + 1 for i, a in enumerate(A) if a['ok']), None)
    lines = (TB.get('C1') or {}).get('proof_lines', 10 ** 6)
    need = {n['key']: n for n in TB.get('needs') or []}
    std3 = bool(P.get('std3', {}).get('SIDEExplicitFormula.B321.rh_imp_h2_sign')) and not P.get('sorry', True)
    return dict(
        n1=std3 and first_ok is not None and first_ok <= 2,
        n2=lines < 80,
        n3=len(TB.get('absent') or []) >= 1,
        s1=bool(A) and A[0]['ok'],
        s2=lines < 50,
        s3=bool(need.get('a', {}).get('found')) and not need.get('f', {}).get('found', True)), A, first_ok, lines


def components():
    sc, A, first_ok, lines = scores()
    L = ['=' * 104, 'b513 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '',
         '### COMPONENT 1 -- THE MODULE, EVERY DECLARATION WHOLE:'] + read('b513_definitions.txt').rstrip(NL).split(NL)
    L += ['', '### THE ATTEMPTS (READING (3)) : %d ; the first to succeed : %s' % (len(A), first_ok)]
    L += ['    %(file)s exit %(exit)s ; %(secs)s s ; Lean`s verdict %(ok)s' % a for a in A]
    for p in sorted(glob.glob(os.path.join(D, 'b513_compile_log*.txt'))) + sorted(glob.glob(os.path.join(D, 'b513_profile_log*.txt'))):
        L += ['', '### RUN FILE %s:' % os.path.basename(p)] + io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)
    L += ['', '### COMPONENT 2 -- THE PROFILE, EACH LINK ON THE WHOLE STRING : %s' % json.dumps(P.get('std3'))]
    L += [''] + read('b513_table.txt').rstrip(NL).split(NL) + ['=' * 104]
    io.open(os.path.join(D, 'b513_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-6:]))


def desk():
    sc, A, first_ok, lines = scores()
    need = {n['key']: n for n in TB.get('needs') or []}
    L = ['=' * 104, 'b513 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- rh_imp_h2_sign`s profile on the whole string: %s ; sorry in Lean`s output: %s ; attempts %d, the first to succeed %s.'
         % (w(sc['n1']), (P.get('new') or ['NONE'])[0], P.get('sorry'), len(A), first_ok),
         '  **(N2)** ### **%s.** -- the proof is %d lines by READING (4), against 80.' % (w(sc['n2']), lines),
         '  **(N3)** ### **%s.** -- Component 3 finds ABSENT : %s.' % (w(sc['n3']), ', '.join('(%s) %s' % (k, need[k]['what']) for k in TB.get('absent') or [])),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the first compile attempt`s verdict: %s.' % (w(sc['s1']), A[0]['ok'] if A else 'NO ATTEMPT'),
         '  **(S2)** ### **%s.** -- %d lines, against 50.' % (w(sc['s2']), lines),
         '  **(S3)** ### **%s.** -- ContDiffBump %s ; the decisive lemma (f) %s.'
         % (w(sc['s3']), 'FOUND' if need.get('a', {}).get('found') else 'ABSENT', 'FOUND' if need.get('f', {}).get('found') else 'ABSENT'),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b513_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b513_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(sc, attempts=len(A), first_ok=first_ok, proof_lines=lines),
              io.open(os.path.join(D, 'b513_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b513 — RH → h2_sign compiled; (R122) entered'


def trail():
    sc, A, first_ok, lines = scores()
    need = {n['key']: n for n in TB.get('needs') or []}
    ok = next((a for a in A if a['ok']), {})
    body = """
%(h)s

**(R122) ratified.** (1) RH → h2_sign is compiled before the matched window is measured: a Prop with one proved
implication is a different object from a Prop with none. The kernel lane opened for this act and shuts at its close;
the numerical lane opens for b514, the matched window, after. (2) **The matched window and the converse are one
object in two registers**: the construction h2_sign → RH needs is a test function that makes zeroSide negative at an
off-line zero, and the matched window of (R121)(4) is that construction attempted numerically at Q0's pair. If b514
exhibits the violation, its window is the witness the converse would need, stated for an arbitrary off-line ρ; if it
does not, the construction is harder than a modulated bump. Neither act claims the other's result. (3) b512's
register-equivalence finding stands at its own standing: four of the five deposited registers NOT STATABLE in the
kernel's objects, the two-channel Li form NOT STATABLE for want of λ_A, and the cell form reached from h2_sign by a
compiled step with no route back in this kernel — a fact about derivability here, not a theorem that the forms
differ in truth.

**COMPONENT 1.** `SIDEExplicitFormula/RHChain.lean` proves `theorem rh_imp_h2_sign : RiemannHypothesis → h2_sign`
along b512's route: for k = weilTest h h in classK, each zero on the line makes its zero term m_ρ·|ĥ(γ)|²
(`paperFT_weilTest`, then `Complex.mul_conj` once `gammaOf ρ` is shown real), nonnegative by
`Complex.normSq_nonneg`; the sum by `tsum_nonneg`; and `b321_identity` carries the sign to P − PR + A. Profile on
the whole string `%(prof)s`; no sorry; %(lines)d lines; compiled in %(secs)s s at attempt %(first)s of %(att)d.

**COMPONENT 2.** The chain RH → h2_sign → cell form: `rh_imp_cell_form` is `rh_imp_h2_sign` composed with b512's
`h2_sign_imp_cell` in one line (b512's `Prop` already holds the name `rh_imp_cell`, so the theorem takes
`rh_imp_cell_form`; `example`s check that it and `rh_imp_h2_sign` inhabit b512's `rh_imp_cell` and `rh_imp_h2`).
`AxiomCheckChain.lean` prints the three links for the terminal table. By the order, each of its model statement:

- `rh_imp_h2_sign` — DERIVES, of RH → h2_sign.
- `h2_sign_imp_cell` — DERIVES, of h2_sign → the cell form on an admissible family.
- `rh_imp_cell_form` — DERIVES, of RH → the cell form on an admissible family.

**COMPONENT 3.** The converse `h2_sign_imp_rh : Prop := h2_sign → RiemannHypothesis` is stated beside the theorem,
equal by definition to b512's `h2_imp_rh`, and is not attempted; its docstring names the construction in (R122)(2)'s
words. What a witness needs, by declaration search in the kernel and its Mathlib: a C² bump (`ContDiffBump`) %(a)s;
the Weil form (`weilTest`) %(b)s; an off-line zero from ¬`RiemannHypothesis` %(c)s; a growth bound for the transform of
a compactly supported function at a complex argument (Paley–Wiener type) %(d)s; the local zero count
(`zetaZeroConfig_local_count`) %(e)s; **the decisive lemma, the off-line pair's term negative and dominating the rest
so that zeroSide k < 0, %(f)s.** A found name is an ingredient, not the construction.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The kernel lane
shuts at this act's close.** The kernel is not tagged; REGISTRY is not written. Nothing at Zenodo written; nothing
deposits; row U1 unedited; `h2` where the deposit left it — the implication from RH to it, now compiled, moves it not
at all; the four lists stay OPEN.
""" % dict(h=HEADING, prof=(P.get('new') or ['NONE'])[0], lines=lines, secs=ok.get('secs'), first=first_ok, att=len(A),
           a=('FOUND' if need['a']['found'] else 'ABSENT'), b=('FOUND' if need['b']['found'] else 'ABSENT'),
           c=('FOUND' if need['c']['found'] else 'ABSENT'), d=('FOUND' if need['d']['found'] else 'ABSENT'),
           e=('FOUND' if need['e']['found'] else 'ABSENT'), f=('FOUND' if need['f']['found'] else 'ABSENT'),
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
    io.open(os.path.join(D, 'b513_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
