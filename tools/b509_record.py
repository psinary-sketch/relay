# -*- coding: utf-8 -*-
"""b509_record.py -- THE STRIKE, THE COMPONENTS BANK, THE DESK AND THE TRAIL.
### `python tools/b509_record.py strike | components | desk | trail` ### Every figure READ from the banks."""
import glob
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
MARK = 'NOTE APPENDED AT b509 UNDER (R118)(3)'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


def strike():
    p = os.path.join(D, 'b508_desk_notes.txt')
    before = open(p, 'rb').read()
    if MARK.encode() in before:
        sys.exit('### REFUSED -- ALREADY STRUCK; NOTHING WRITTEN.')
    note = NL.join(['', '-' * 104, '### %s, 2026-09-24. ### THE TEXT ABOVE IS UNEDITED.' % MARK, '-' * 104,
                    '### ### **(N2) ABOVE IS STRUCK AS VACUOUS.** ### b506 defines the residual as m - (Z - P), so the expectation',
                    '### could not fail; ### *"an expectation that restates a definition is not an expectation"* (R118)(3). ### The',
                    '### navigator`s count above therefore stands at (N1) HELD and (N3) REFUTED, with (N2) STRUCK.', '-' * 104, ''])
    open(p, 'ab').write(note.encode('utf-8'))
    after = open(p, 'rb').read()
    bl, al = before.split(b'\n'), after.split(b'\n')
    out = dict(file='b508_desk_notes.txt', written=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b) - (0 if before.endswith(b'\n') else 1),
               marks=after.decode('utf-8').count(MARK))
    io.open(os.path.join(D, 'b509_strike.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)
    print(out)


def logs(stem):
    return sorted(glob.glob(os.path.join(D, stem + '*.txt')))


def components():
    L = ['=' * 104, 'b509 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '', '### COMPONENT 1 -- THE TERMINAL.',
         '### the statement, from its declaration line to its `:=` :'] + read('b509_statement.txt').rstrip(NL).split(NL)
    for p in logs('b509_compile_log') + logs('b509_profile_log'):
        L += ['', '### RUN FILE %s, VERBATIM:' % os.path.basename(p)] + io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)
    L += ['', '### THE IMPORT PROBE (diagnostic, after the seal): %s' % read('b509_probe_import_out.txt').strip().split(NL)[-1],
          '### the profile record : %s' % read('b509_profile.json').replace(NL, ' '),
          '', '### COMPONENTS 2 AND 3.'] + read('b509_clauses.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENT 4 -- THE (R118)(3) STRIKE : %s' % read('b509_strike.json').strip(), '=' * 104]
    io.open(os.path.join(D, 'b509_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-12:]))


def scores():
    P = json.loads(read('b509_profile.json') or '{}')
    C = json.loads(read('b509_clauses.json') or '{}')
    diff = C.get('differs', [])
    return dict(n1=bool(P.get('new_std3')), n2=(diff == ['normalization']), n3=(C.get('grade') == 'DERIVES'),
                s1=None, s2=(diff == ['class of test functions', 'truncation'] and C.get('norm_constant') == 1),
                s3=(C.get('grade') == 'INTERFACES')), P, C


def desk():
    sc, P, C = scores()
    # ### (S1) read off the proof text: the terminal is the module's only `theorem`, there is no `lemma`, and the
    # ### proof names EF_lit_zetaZeroConfig -- a local `have` is a rewrite step, not an analytic lemma.
    src = io.open(os.path.join('D:', os.sep, 'SIDE-explicit-formula', 'SIDEExplicitFormula', 'B321Identity.lean'), encoding='utf-8').read()
    proof = src[src.index('theorem b321_identity'):]
    own = [l for l in ('have ', 'lemma ', 'theorem ') if proof.count(l) > (1 if l == 'theorem ' else 0) and l != 'have ']
    sc['s1'] = bool(P.get('new_std3')) and not own and 'EF_lit_zetaZeroConfig' in proof
    w = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
    L = ['=' * 104, 'b509 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- the whole string : %s' % (w(sc['n1']), (P.get('new') or ['(none)'])[0]),
         '  **(N2)** ### **%s.** -- the clauses that DIFFER : %s ; the normalization is SAME, its constant `b321Norm := 1`.'
         % (w(sc['n2']), ', '.join(C.get('differs', [])) or 'NONE'),
         '  **(N3)** ### **%s.** -- EF_lit quantifies over `ContDiff R 2` with compact support; the chain`s windows are piecewise'
         % w(sc['n3']),
         '    linear, slope jumps at %s of %s nodes: the class does not contain the family, and the grade is %s.'
         % ((C.get('regularity') or {}).get('nonzero_jumps'), (C.get('regularity') or {}).get('nodes'), C.get('grade')),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the proof specialises EF_lit_zetaZeroConfig and rewrites; no lemma of this programme`s own.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- DIFFERS : %s ; constant %s.' % (w(sc['s2']), ', '.join(C.get('differs', [])), C.get('norm_constant')),
         '  **(S3)** ### **%s.** -- grade %s on %s' % (w(sc['s3']), C.get('grade'), (C.get('premise') or '').split(':')[0]),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc['n1'], sc['n2'], sc['n3']].count(True), [sc['n1'], sc['n2'], sc['n3']].count(False),
            [sc['s1'], sc['s2'], sc['s3']].count(True), [sc['s1'], sc['s2'], sc['s3']].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b509_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b509_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b509_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b509 — b321’s identity derived in SIDE-explicit-formula from EF_lit_zetaZeroConfig'


def trail():
    sc, P, C = scores()
    sc = json.loads(read('b509_scores.json'))
    w = lambda v: 'HELD' if v else 'REFUTED'
    body = """
%(h)s

**(R118) ratified.** (1) b508 is entered as a negative result about the instrument: on the ladder's family to
width 14.1 the Epstein control Q0, with seventeen off-line zero pairs below 150, has a margin positive at all 83
verified cells, so **positivity of m(a) on this family does not, at these widths, distinguish ξ from an object
known to violate Weil positivity.** **By this appended note, the monograph's step (9) Epstein sentence — PROSE, NO
BANK at `OPEN_TRAILS.md:9270` (b495, under (R106)) — is now also UNSUPPORTED BY THE CONTROL AT WIDTH ≤ 14.1**; the
monograph itself is deposited and is not written. **No sentence of the corpus may cite the ladder's positivity as
evidence of the sign clause until a window is exhibited at which Q0's margin is negative on a bank that closes.**
(2) **`W-ORD-FAMILY-SENSITIVITY` is filed:** exhibit, on the completed Q0 bank, a window — in the ladder's family
past width 14.1 with the bank extended to cover it, or in a second family whose transform is designed against the
pair at 0.953 + 16.29i — at which Q0's margin is negative and verified, and ξ's margin at the same window.
Trigger: the act after (R104)'s act 4, or the author's word. (3) b508's (N2) is struck as vacuous, by a note
appended to `b508_desk_notes.txt`. (4) The kernel lane opened for this act.

**COMPONENT 1.** `SIDE-explicit-formula/SIDEExplicitFormula/B321Identity.lean`, this programme's own module (rule 9
in full; no vendored body touched; the lakefile's globs gain `SIDEExplicitFormula.+`), states b321's four-channel
identity for ζ's zero configuration in the kernel's objects — `zeroSide k = b321Norm * (poleTerm k − primeSum k +
archTerm k)` for every even `k` with `ContDiff ℝ 2 k` and compact support — and proves it from
`EF_lit_zetaZeroConfig` as its even case, the prime channel in b321's form `2 k(log n)`. The normalization constant
is the definition **`b321Norm := 1`**. `#print axioms`: `%(prof)s`; the control `EF_lit_zetaZeroConfig` beside it:
`%(ctl)s`.

**COMPONENT 2.** Seven clauses: the sign of each of the four channels SAME; the normalization **SAME, constant 1**;
**the class of test functions DIFFERS** — the terminal quantifies over even `C_c²` functions, and the chain
transforms the ladder's windows as continuous piecewise-linear functions, whose slope jumps at %(jumps)s of %(nodes)s
nodes at a = 5.0 (not C¹); **the truncation DIFFERS** — none in EF_lit, the banked ordinates to T and the u-range
`[−UMAX, UMAX]` in b321.

**COMPONENT 3.** Against "b321's identity holds for every test function of the ladder's family": **%(grade)s**, on
the named premise **P-PL — the explicit formula holds for every even, compactly supported, continuous piecewise-linear
k**, not compiled. The terminal table regenerates at the post-push suite, since it reads committed blobs.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The kernel lane
shuts at this act's close.** The kernel is not tagged; REGISTRY is not written. Nothing at Zenodo written; nothing
deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a
statement about RH.
""" % dict(h=HEADING, prof=(P.get('new') or ['NONE'])[0], ctl=(P.get('control') or ['NONE'])[0],
           jumps=C['regularity']['nonzero_jumps'], nodes=C['regularity']['nodes'], grade=C['grade'],
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
    io.open(os.path.join(D, 'b509_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'strike': strike, 'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
