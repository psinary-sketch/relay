# -*- coding: utf-8 -*-
"""b503_record.py -- THE DESK, AND THE TRAIL: THIS ACT`S RECORD, THE 33 MARKS, AND b502`S ANNOTATION.

### `python tools/b503_record.py desk | trail`
### The trail receives THREE headed blocks in ONE append, as the face registered; no prior line is
### edited, and b501`s and b502`s banks are not touched.
"""
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

R = json.loads(io.open(os.path.join(D, 'b503_results.json'), encoding='utf-8').read())
F = json.loads(io.open(os.path.join(D, 'b503_fixture.json'), encoding='utf-8').read())
MK = json.loads(io.open(os.path.join(D, 'b503_marks.json'), encoding='utf-8').read())
C = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b503_cells.jsonl'), encoding='utf-8') if l.strip()),
           key=lambda r: r['a'])
w = lambda v: 'HELD' if v else 'REFUTED'
n1 = R['verified'] >= 105
n2 = R['n_mz_big'] == 0
n3 = R['m13_z1']
n4 = R['rise'] is True
s1 = len(R['aliased_now_verified']) == len(R['aliased_before'])
s2 = len(R['short_now_verified']) < len(R['short_before']) / 2.0
s3 = R['rise'] is True
big = [(r['a'], r['m_minus_Z'], r['B']) for r in C if r['verified'] and abs(r['m_minus_Z']) >= 1e-6]


def desk():
    L = ['=' * 104, 'b503 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE COMPONENTS PRINTED.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- *"at least 105 of 119 cells verify"* -- ### **%d**, on the ordered residual the face'
         % (w(n1), R['verified']),
         '    scores; ### beside it, on the CONSISTENT residual, %d. ### Neither reaches 105. ### The ordered residual mixes'
         % R['consistent_verified'],
         '    the exact Z with the trapezoid A, and their ~1e-5 relative difference breaks cells whose bounds are 1e-8 --',
         '    only 4 of the old 35 verify on it. ### And eight cells from a = 13.637 stay unverified on EITHER residual:',
         '    the exact transform of a piecewise-linear w still carries a sinc^2-scaled copy of its main lobe near',
         '    2 pi / dv, straddling T = 9877.78, and the part above T is truncation the 10,000-zero bank cannot reach.',
         '  **(N2)** ### **%s.** -- *"|m - Z| below 1e-06 at every verified cell"* -- at or above 1e-06 at %d: %s'
         % (w(n2), len(big), ['a=%.2f m-Z %.2e (B %.2e)' % x for x in big]),
         '    ### the pole term is at most %.1e, so m - Z is the residual itself; at those three cells the bound is large'
         % max(abs(r['P']) for r in C),
         '    (the u-grid of A at small a) and admits them as verified while |m - Z| exceeds 1e-6.',
         '  **(N3)** ### **%s.** -- *"the minimum at 13.152946 within one cell of an extremum of the lowest zero`s term"* --'
         % w(n3),
         '    zero terms with an extremum within one cell : %s (z1`s minimum is at 13.266017, the next verified cell).'
         % R['match'].get(R['m13'], []),
         '  **(N4)** ### **%s.** -- *"the rise after 13.153 survives at the verified cells"* -- %d verified cells after it,'
         % (w(n4), R['after13']),
         '    m increasing across all of them.',
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- every ALIASED cell verifies : %d of %d do (%s).'
         % (w(s1), len(R['aliased_now_verified']), len(R['aliased_before']), [round(a, 6) for a in R['aliased_now_verified']]),
         '    ### The image was not the whole failure: its sinc^2 copy survives the exact transform above a = 13.6.',
         '  **(S2)** ### **%s.** -- the ESTIMATE-SHORT cells mostly stay unverified : %d of %d now verify on the ordered'
         % (w(s2), len(R['short_now_verified']), len(R['short_before'])),
         '    residual, and %d of %d on the consistent one -- most shortfalls were the trapezoid transform`s.'
         % (R['short_consistent_ok'], len(R['short_before'])),
         '  **(S3)** ### **%s.** -- the rise after 13.153 survives.' % w(s3),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.**' % ([n1, n2, n3, n4].count(True), [n1, n2, n3, n4].count(False)),
         '### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE 0.**' % ([s1, s2, s3].count(True), [s1, s2, s3].count(False)),
         '=' * 104]
    io.open(os.path.join(D, 'b503_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, n4=n4, s1=s1, s2=s2, s3=s3),
              io.open(os.path.join(D, 'b503_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b503 — the transform made alias-free: the residual of 7 gone, 64 of 119 verified as ordered, 86 consistent'
H_MARKS = '### (R113)(1) — the 33 unverified cells of b501 and b502, marked by appended note, with their kinds'
H_ANNOT = '### b502 — annotation by appended note, under (R113)(1)'


def trail():
    marks = NL.join('| %s | `%.6f` | %.3e | %.3e | ×%.3g | **%s** |' % (m['set'], m['a'], m['res'], m['B'], m['res'] / m['B'], m['kind'])
                    for m in MK)
    body = """
%(h)s

**(R113), as amended, ratified.** A cell whose two-side residual exceeds its bound is UNVERIFIED, and no
reading of m(a) at such a cell enters a finding, a fit or a digest; the rule governs, over the 33 cells
marked below. The navigator's reading that m(a) equals Z(a) was entered as an expectation, (N2).

**COMPONENT 1.** The chain's zero bank is `carto_atlas.GAM`, **10,000 ordinates to 9877.78**;
`b326_closure.json` is a different bank. The trapezoid transform carries an image of its main lobe at
`2 pi / dv`, which enters `[T, T+200]` at a = 12.845 (trunc 2.2e+02) and falls among the zeros from
a = 13.637 (residual about 7); `trunc_bound` reads it while it is in its window and is blind after.

**COMPONENT 2.** The zero side re-formed by `b326_closure.hhat_exact` at all 119 cells, the bank unchanged.
Fixture at a = 4.061553: the identity `exact = sinc^2(u dv/2) x trapezoid` holds to **%(fid).1e** relative,
inside the 1e-12 bar; the raw difference is %(fraw).1e — the two transforms are not the same number, as the
face said before it ran. **The residual of 7 is gone everywhere.** Verified on the ORDERED residual (exact
Z against the chain's trapezoid A): **%(ver)d of 119**; on the CONSISTENT residual (both sides exact),
printed beside: **%(cver)d of 119**. The ordered residual mixes two transforms whose ~1e-5 relative
difference breaks cells bounded at 1e-8 — only 4 of the old 35 verify on it. **Eight cells from a =
13.637 stay unverified on either residual**, near 1.6e-06: the exact transform of a piecewise-linear `w`
carries a sinc²-scaled copy of its main lobe near `2 pi / dv`, straddling T, and the part above T is
truncation the 10,000-zero bank does not reach. Of the 22 ESTIMATE-SHORT cells, %(sok)d are within their
bound on the consistent residual — their shortfall was the transform's — and %(snot)d are the estimate's.

**COMPONENT 3 — THE TAIL, ON VERIFIED CELLS ALONE.** On the ordered set: the minimum at **13.152946**
stands, and **the rise after it survives** at the %(after)d verified cells beyond it. On the consistent set, all
three extrema — 4.061553, 5.196152, 13.152946 — are verified. c/a² still has the least RMS residual.

**COMPONENT 4 — THE ATTRIBUTION.** The pole term is at most 1.3e-16, so m − Z is the residual itself. The
minimum at 13.152946 sits within one cell of extrema of the lowest zero's term (14.1347, its minimum at
13.266017) and of the fourth's (30.4249).

**(N1) %(n1)s · (N2) %(n2)s · (N3) %(n3)s · (N4) %(n4)s.** The seat's own: **(S1) %(s1)s, (S2) %(s2)s, (S3) %(s3)s.**
**The numerical lane shuts at this act's close.** No grade conferred; nothing deposits; row U1 unedited;
`h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement about RH.

%(hm)s

Appended, not inserted: b501's and b502's banks are prior acts' banks and are not edited. **ALIASED**
where the residual exceeds the bound by more than ten times, **ESTIMATE-SHORT** where it does not.
Their status after b503's exact transform is in b503's own record above.

| set | a | residual (trapezoid) | bound | ratio | kind |
|:--|--:|--:|--:|--:|:--|
%(marks)s

%(ha)s

**b502's closing said no defect of its own instruments was found. It was wrong:** b502 banked each new
cell's two-side residual and never set it against the cell's bound, the comparison b501 made. **Its
Component 2 and Component 3 readings that rest on aliased cells are withdrawn until b503 re-read them**,
and b503 has: the rise after 13.153 survives on the verified cells, and c/a² still has the least
residual. b502's own record and banks are not edited.
""" % dict(h=HEADING, fid=F['identity_max'], fraw=F['raw_max'], ver=R['verified'], cver=R['consistent_verified'],
           sok=R['short_consistent_ok'], snot=len(R['short_before']) - R['short_consistent_ok'], after=R['after13'],
           n1=w(n1), n2=w(n2), n3=w(n3), n4=w(n4), s1=w(s1), s2=w(s2), s3=w(s3),
           hm=H_MARKS, marks=marks, ha=H_ANNOT)
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b),
               headings=[after.decode('utf-8').count(h) for h in (HEADING, H_MARKS, H_ANNOT)])
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, headings %(headings)s' % out)
    io.open(os.path.join(D, 'b503_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'desk': desk, 'trail': trail}[sys.argv[1]]()
