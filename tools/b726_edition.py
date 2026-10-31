# -*- coding: utf-8 -*-
"""b726, (R336)(4): WHICH STRUCTURE CONFINES, THE v2.4.0 EDITION, BY THE FORM OF AN EDITION (I-16, OPEN_TRAILS :11864) AND I-17 TO I-33. Composes
day1/Which_Structure_Confines_v2_4_0.md beside the current version, which stays unedited, from the current bytes: each substitution asserted once
on its own line, each figure the new text carries read at its bank and line before anything is written, the citations re-pinned to the final
file's lines (I-22), the diff banked sentence by sentence, the scores printed by the form's clauses.

  python -X utf8 tools/b726_edition.py dry | write
        dry composes, scores and prints, writing nothing; write writes the edition and data/b726_edition_diff.txt.
THE AUTHOR'S NAME AND ORCID ARE NOT CARRIED ((R336)(8): no identifier of the author in anything this act writes): the byline and two self-citations
read "the author", the back matter says so, and this tool prints neither the old byline nor those references. Writes nothing else."""
import hashlib
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
CUR = PP + '/day1/Which_Structure_Confines.md'
NEW = PP + '/day1/Which_Structure_Confines_v2_4_0.md'
BANK = os.path.join(D, 'b726_edition_diff.txt')
NL = '\n'
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b726_address_scan as SC  # noqa: E402

LLM_NEW = ("*Computational workflow assisted by various LLM instances. Mathematical content, strategies of argument, and editorial decisions are the "
           "author's.*")
TITLE_CUR = '# Which Structure Confines the Zeros?'
TITLE_NEW = ('# Which Structure Confines the Zeros? The Euler Product, the Epstein Family at Class Numbers 2 and 3, and the Weil Form Beside the '
             'Dedekind Zeta')
VERSION_LINE = ('*v2.4.0, 2026-10-30 (b726, under `(R336)`(4): the edition written beside v2.3.1, which is unedited; it adds the figure, the mechanism '
                'and the scope sentence, and its back matter closes the file).*')
BYLINE = '**The author** | v2.4.0, October 2026'

# ### (line of the current version, the words, the edition's words, the clause, why); a NAME row's words are masked in every print
SUBS = [
    (9, 'We identify the Euler product as the structural component responsible for confining zeros of L-functions to the critical line.',
     'We identify the Euler product as the structural component whose removal, in every family tested here, lets zeros leave the critical line.',
     'ceiling', 'the sentence claimed confinement of zeros generally, which nothing here reaches: the object is what the tested removal does'),
    (9, 'every tested function with both properties confines its zeros; every function lacking the Euler product does not.',
     'every tested function with both properties has all its computed zeros on the line; every function lacking the Euler product does not.',
     'ceiling', 'the record is of computed zeros, as :109 says'),
    (109, 'The structural argument — that the Euler product provides the only mechanism for zero confinement, as shown by the discriminating-variable analysis — supplements the correlational evidence.',
     'The structural argument — that among the mechanisms tested the Euler product is the only one present wherever the zeros stayed on the line, as the discriminating-variable analysis reads them — supplements the correlational evidence.',
     'ceiling', '"the only mechanism for zero confinement" is beyond what a comparison of tested families shows'),
    (109, 'since the point is that the functional equation *permits* off-line zeros while the Euler product *prevents* them.',
     'since the point is that the functional equation *permits* off-line zeros while no tested function with an Euler product shows one.',
     'ceiling', '"prevents" would state the open clause as done'),
    (117, 'The Epstein experiment identifies which axiom is doing the work.', 'The Epstein experiment identifies the axiom whose removal changes the outcome.',
     'ceiling', 'the object is the removal, not a confinement the experiment does not show'),
    (121, 'The Euler product confines the actors.', 'Removing the Euler product lets the actors leave it.', 'ceiling', 'as :9'),
    (121, 'correctly identifies which structural component confines zeros, by exhibiting', 'points to the same structural component, by exhibiting', 'ceiling', 'as :9'),
    (121, 'The decomposition is correct.', 'The decomposition stands at this test.', 'ceiling', 'one experiment does not close the exhaustion'),
    (121, 'is the one certified premise — the inter-class conservation step', 'is the one open premise — the inter-class conservation step', 'ceiling',
     'README :106-:108: the premise is undischarged'),
    (158, "*Computational workflow assisted by various LLM instances. Mathematical content, proof strategies, and editorial decisions are the author's.*", LLM_NEW,
     'ruled', '(R336)(6): the monograph\'s words, day1/A_Place_to_Stand.md :2178, in its position, after the references and before the colophon'),
    (163, ' This paper develops one component of a proof of Theorem (RH) presented in the companion monograph *A Place to Stand* (2026).',
     ' This paper develops one component of the work on Theorem (RH), which stays open, presented in the companion monograph *A Place to Stand* (2026).',
     'ceiling', 'README :107: "RH proved" is not supportable'),
]

SECTION = """## The Figure and the Mechanism

### The figure

At the two onset windows of the principal form Q0 = x² + xy + 6y² of discriminant −23 and class number 3, a = 6.838396011 and a = 10.38532711, the Weil form was read twice: with Q0's prime weights, and with those of the Dedekind zeta function ζ_K of K = ℚ(√−23), which carries an Euler product. Everything archimedean is identical between the two: the gamma factor, the conductor, the pole and the form's polar and archimedean terms are Q0's in both, and the prime weights alone differ (relay `data/b723_zetak.txt` :55, `data/b723_registrations.txt` :37-:40). Q0's least eigenvalues are −0.0037191321 and −3.5300862e-5 (relay `data/b709_grid.txt` :441, :4501); ζ_K's are 0.689 and 2.995 (relay `data/b723_zetak.txt` :59, :65).

### The mechanism

For class number 2 and Re s > 1, log(Z_Q/2) = log ζ_K − S + log cosh S, where S is the non-principal prime sum (relay `data/b723_c2_closed_form.txt` :16, :21, :32); this is a written derivation of genus theory's identity, not compiled, and its check is POST HOC, 19 rows of 19 (:70). Its steps Z_Q/2 = (ζ_K + L(s, ψ))/2 and L(s, ψ)/ζ_K = e^(−2S) (:24, :26) give, read through the continuation of that quotient, that the principal form's off-line zeros at which ζ_K does not vanish are the zeros of cosh S, the points where the quotient equals −1. For class number 3 the reading is interference: at Q0's discriminant ζ_K = (Z_Q0 + 2Z_Q1)/2 and L(s, ψ) = (Z_Q0 − Z_Q1)/2, so at a zero of Z_Q0, ζ_K = Z_Q1 = −2L(s, ψ) (relay `data/b725_interference.txt` :31), and Z_Q1 excludes 0 at 69 of 69 certified off-line zeros of Z_Q0 to height 445 (:106; the population, relay `data/b725_registration_2026-10-30.txt` :159). The terms cancel at Q0 without either vanishing.

### Scope

These are statements about the Epstein family and say nothing about where zeta's zeros lie.

*Credit: the two windows and Q0's least eigenvalues are b709's grid; the form beside ζ_K is b723's H-ZETAK and the closed form b723's derivation; the table of 69 is b725's H-INTERFERENCE.*"""

BACK = """<!-- b726 (R336) THE v2.4.0 EDITION`S BACK MATTER, 2026-10-30 -->

---

## Placement *(added 2026-10-30, b726 — each result of the v2.4.0 section with its source and its footing)*

The footings: **REGISTERED** — a registered hypothesis read against its rule at a bank line; **DERIVATION** — written and checked POST HOC, not compiled; **HELD** — stated and open, no terminal reaches it.

| result | source | pin | footing |
|:--|:--|:--|:--|
| ζ_K's form positive definite at Q0's two onset windows, H-ZETAK HELD | relay `data/b723_zetak.txt` :59, :65, :70 | no kernel; the registration `data/b723_registrations.txt` :36 | REGISTERED |
| log(Z_Q/2) = log ζ_K − S + log cosh S at class number 2, Re s > 1 | relay `data/b723_c2_closed_form.txt` :21, :32, :70 | no kernel; genus theory's identity | DERIVATION |
| Z_Q1 excludes 0 at 69 of 69 certified off-line zeros of Z_Q0 to height 445, H-INTERFERENCE HELD | relay `data/b725_interference.txt` :106 | no kernel; the registration `data/b725_registration_2026-10-30.txt` :159 | REGISTERED |
| the Euler product as the discriminating variable | this paper's comparison | no kernel | HELD |

## Correspondence, rows of v2.4.0 *(added 2026-10-30, b726. The section above stays as written: its sentence that this document's evidence is “not a computation this programme performed” stands for the classical theorem, and the rows here are the programme's computations.)*

| claim | kernel | fully-qualified terminal | axiom profile | status | `VERIFY-BY` |
|:--|:--|:--|:--|:--|:--|
| the least eigenvalues at Q0's two windows, Q0's weights against ζ_K's | NONE | — | — | REGISTERED — computed, not compiled | read relay `data/b709_grid.txt` :441, :4501 and `data/b723_zetak.txt` :59, :65 |
| the class number 2 closed form | NONE | — | — | DERIVATION — written, checked POST HOC, not compiled | read relay `data/b723_c2_closed_form.txt` :21-:33, :70 |
| the class number 3 interference reading | NONE | — | — | REGISTERED — computed, not compiled | read relay `data/b725_interference.txt` :31, :106 |

## Back matter of the v2.4.0 edition -- written 2026-10-30 by b726 under the author’s ruling `(R336)`(4), by the form of an edition (I-16, OPEN_TRAILS :11864)

*This file is v2.4.0 of Which Structure Confines, written beside v2.3.1 (`day1/Which_Structure_Confines.md`, unedited). This document has no CP-1b work-list (relay `data/b558_cp1b.json` and `data/b558_editions.json` do not carry it), so no MOVED-IN-MEANING row governs it; it is written from `(R336)`(4)'s three additions. It does not deposit and does not replace v2.3.1. Every line cited below is this file's own.*

### Removals

None.

### The byline

The author's name, ORCID and two self-citations are not carried into this file: `(R336)`(8) bars any identifier of the author from what this act writes. The byline and the two references read “the author”; the current version's stand at its own :3, :142 and :144, for the release sitting to set.

### Ceiling corrections and ruled rewrites

| this edition's line | current wording | v2.4.0 wording | Status |
|:--|:--|:--|:--|
{REWRITES}

### Additions ruled by `(R336)`(4)

| this edition's line | the item | Status |
|:--|:--|:--|
| :{L:SEC} | the section The Figure and the Mechanism: the figure, the mechanism and the scope sentence | ruled citations, counted under H28b |
| :{L:CREDIT} | the credit line for b709, b723 and b725 | inserted beneath the section it credits |
| :{L:VER} | the version line | one version line, counted under H28b |
"""


def rd(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8')


def at(bank, line, needle):
    """a figure the new text carries, read at its bank and line; any miss refuses the whole composition"""
    t = rd(os.path.join(D, bank)).replace('\r', '').split(NL)
    if needle not in t[line - 1]:
        sys.exit('### data/%s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (bank, line, needle))
    return (bank, line, needle)


READS = [('b709_grid.txt', 441, 'a = 6.838396011'), ('b709_grid.txt', 441, 'lambda_min -0.0037191321'),
         ('b709_grid.txt', 4501, 'a = 10.38532711'), ('b709_grid.txt', 4501, 'lambda_min -3.5300862e-5'),
         ('b723_zetak.txt', 55, 'P, A, k(0) Q0`S'), ('b723_zetak.txt', 59, 'lambda_min 0.6888118560'), ('b723_zetak.txt', 65, 'lambda_min 2.995245235'),
         ('b723_zetak.txt', 70, 'HELD'), ('b723_registrations.txt', 37, "Q0's gamma factor, conductor and pole"),
         ('b723_registrations.txt', 39, 'P and A unchanged'), ('b723_c2_closed_form.txt', 16, 'S(s), the non-principal prime sum'),
         ('b723_c2_closed_form.txt', 21, 'log(Z_Q / 2) = log zeta_K - S + log cosh S'), ('b723_c2_closed_form.txt', 24, 'Z_Q / 2 = (zeta_K + L(psi)) / 2'),
         ('b723_c2_closed_form.txt', 26, 'L(psi) / zeta_K = e^(-2S)'), ('b723_c2_closed_form.txt', 32, 'for Re s > 1'),
         ('b723_c2_closed_form.txt', 70, '19 ROWS OF 19'), ('b723_c2_closed_form.txt', 70, 'NOT COMPILED'),
         ('b725_interference.txt', 31, 'zeta_K(rho) = Z_Q1(rho) = -2 L(rho, psi) (FORCED)'), ('b725_interference.txt', 106, 'Z_Q1 EXCLUDES 0 AT 69'),
         ('b725_interference.txt', 104, 'HELD'), ('b725_registration_2026-10-30.txt', 159, '69 certified off-line zeros to height 445')]


def sents(lines):
    """the body's sentences: prose lines only (no table, rule or heading), split at a stop before a space"""
    out = []
    for l in lines:
        s = l.strip()
        if not s or s.startswith(('|', '#', '---', '<!--')):
            continue
        out += [x.strip() for x in re.split(r'(?<=[.!?:;*)])\s+(?=[A-Z*(“])', s) if x.strip()]
    return out


def compose():
    for r in READS:
        at(*r)
    raw = rd(CUR)
    crlf = raw.count('\r\n') * 2 > raw.count('\n')
    cur = raw.replace('\r\n', '\n')
    lines = cur.split(NL)
    name = SC.author_name()
    ed = list(lines)
    for n, old, new, _cl, _why in SUBS:
        if ed[n - 1].count(old) != 1:
            sys.exit('### :%d DOES NOT CARRY ITS WORDS ONCE (%d): %r -- NOTHING WRITTEN' % (n, ed[n - 1].count(old), old[:60]))
        ed[n - 1] = ed[n - 1].replace(old, new)
    if ed[0] != TITLE_CUR:
        sys.exit('### :1 IS NOT THE TITLE -- NOTHING WRITTEN')
    ed[0] = TITLE_NEW
    if '| ORCID:' not in ed[2]:
        sys.exit('### :3 IS NOT THE BYLINE -- NOTHING WRITTEN')
    ed[2] = BYLINE
    for n in (142, 144):
        if name not in ed[n - 1]:
            sys.exit('### :%d CARRIES NO SELF-CITATION -- NOTHING WRITTEN' % n)
        ed[n - 1] = ed[n - 1].replace(name, 'The author')
    # ### the version line beneath the byline; the section before "Why the Functional Equation Is Insufficient"
    i = ed.index('## Why the Functional Equation Is Insufficient')
    body_cut = ed.index('## Symbols')
    new = ed[:3] + ['', VERSION_LINE] + ed[3:i] + SECTION.split(NL) + [''] + ed[i:]
    text = NL.join(new).rstrip(NL) + NL
    # ### I-22: the rows re-pointed to the final file's lines; two passes, the back matter's own length moving nothing above it
    tl = text.split(NL)
    pos = lambda needle: next((k for k, l in enumerate(tl, 1) if needle in l), None)  # noqa: E731
    rows = []
    for n, old, nw, cl, why in SUBS:
        L_ = pos(nw)
        if L_ is None:
            sys.exit('### THE NEW WORDS NOT FOUND: %r' % nw[:60])
        q = lambda s: s.replace('|', '¦').strip()  # noqa: E731
        rows.append('| :%d | %s | %s | %s: %s |' % (L_, q(old), q(nw), {'ceiling': 'a ceiling correction (I-19)', 'ruled': 'a ruled rewrite'}[cl], why))
    rows.insert(0, '| :1 | %s | %s | the form: the title names objects and conditions (OPEN_TRAILS :11864) |' % (TITLE_CUR, TITLE_NEW))
    bm = BACK.replace('{REWRITES}', NL.join(rows))
    for k, nd in (('SEC', '## The Figure and the Mechanism'), ('CREDIT', '*Credit: the two windows'), ('VER', '*v2.4.0, 2026-10-30')):
        bm = bm.replace('{L:%s}' % k, str(pos(nd)))
    text = text.rstrip(NL) + NL + NL + bm
    if SC.count(text, name) or SC.count(text, SC.previous_username()) or SC.count(text, SC.previous_address()) or 'ORCID:' in text:
        sys.exit('### AN IDENTIFIER OF THE AUTHOR IN THE EDITION -- NOTHING WRITTEN')
    return cur, text, crlf, body_cut


CEILING = ('proof of Theorem', 'RH proved', 'certified premise', 'decomposition is correct', '*prevents*', 'confines the actors', 'correctly identifies',
           'only mechanism for zero confinement', 'doing the work', 'responsible for confining', 'confines its zeros', 'reduction machine-verified')
QUESTION = 'Which structural feature is responsible for confining zeros to the critical line?'


def score(cur, text, body_cut):
    cl = cur.split(NL)
    tl = text.split(NL)
    back_e = tl.index('## Symbols')
    a, b = sents(cl[:body_cut]), sents(tl[:back_e])
    stands = sum(1 for s in a if s in set(b))
    sec = SECTION.split(NL)
    ruled = len(sents(sec))
    credit = sum(1 for s in sents(sec) if s.startswith('*Credit'))
    # ### the bound, I-21: the CREDIT count, the removals, the ruled citations and one version line
    d = len(b) - len(a)
    bound = (ruled - credit) + credit + 0 + 1
    # ### :20's "responsible for confining" is the paper's question, which asserts nothing; read by hand and carried, printed in the scores
    ceil = [(w, sum(l.replace(QUESTION, '').count(w) for l in tl[:back_e])) for w in CEILING]
    ceil_hits = [(w, n) for w, n in ceil if n]
    stems = [(i, m.group(0)) for i, l in enumerate(tl, 1) for m in re.finditer(r'\b(gap|blind)\w*', l, re.I)]
    cites = len(re.findall(r'relay `data/', '\n'.join(sec)))
    return dict(body_cur=len(a), body_new=len(b), stands=stands, ruled=ruled, credit=credit, d=d, bound=bound, ceil_hits=ceil_hits, stems=stems, cites=cites,
                back_cur=len(sents(cl[body_cut:])), back_new=len(sents(tl[back_e:])))


def bank(cur, text, s, ok):
    L = ['b726 -- (R336)(4): WHICH STRUCTURE CONFINES v2.4.0 AGAINST v2.3.1, SENTENCE BY SENTENCE, AND ITS SCORES (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### by tools/b726_edition.py from the current bytes; the current version unedited (sha256 %s), the edition sha256 %s.' % (
             hashlib.sha256(cur.encode('utf-8')).hexdigest()[:16], hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]),
         '### THE OFFSET (I-22): lines of v2.3.1 from :6 sit 2 lower in the edition, and from the section at "Why the Functional Equation" lower by the section`s length as well; every',
         '### line in the back matter`s rows is the final file`s. The byline and two self-citations are not reprinted here: the author`s name and ORCID are not carried.', '',
         '## THE CHANGES (line of v2.3.1 | clause | v2.3.1 | v2.4.0 | why)', '  :1 | the form | %s | %s | the title names objects and conditions' % (TITLE_CUR, TITLE_NEW),
         '  :3 | (R336)(8) | [the byline, not reprinted] | %s | no identifier of the author' % BYLINE,
         '  :142, :144 | (R336)(8) | [two self-citations, not reprinted] | The author. ... | no identifier of the author']
    for n, old, nw, cl, why in SUBS:
        L.append('  :%d | %s | %s | %s | %s' % (n, cl, old.strip(), nw.strip(), why))
    L += ['', '## THE ADDITIONS, EACH FIGURE READ AT ITS BANK AND LINE BEFORE COMPOSITION (%d reads, all as wanted)' % len(READS)]
    L += ['  data/%s :%d carries: %s' % r for r in READS]
    L += ['', '## THE SCORES',
          '  H28a: MOVED-IN-MEANING rows 0 (no CP-1b work-list carries this document: data/b558_cp1b.json, data/b558_editions.json); each addition cites its bank and line (%d relay citations in the section, %d reads) -- HELD, VACUOUS on the work-list`s rows and carried on the ruled additions' % (s['cites'], len(READS)),
          '  H28b (I-21): body sentences %d against %d, back matter %d against %d counted beside; difference %d against the bound %d (ruled citations %d, CREDIT %d, removals 0, one version line) -- %s' % (
              s['body_new'], s['body_cur'], s['back_new'], s['back_cur'], s['d'], s['bound'], s['ruled'] - s['credit'], s['credit'], 'HELD' if s['d'] <= s['bound'] else 'REFUTED'),
          '  H28c: live banned stems in the whole file %d (read by this tool`s pattern; tools/banned_terms.py --new read after the write); sentences beyond the ceiling %d, by the list %s -- %s' % (
              len(s['stems']), len(s['ceil_hits']), list(CEILING), 'HELD' if not s['stems'] and not s['ceil_hits'] else 'REFUTED'),
          '  THE ONE HIT READ BY HAND AND CARRIED: current :20, "%s", the paper`s question, which asserts nothing; it is struck from the ceiling count above and stands' % QUESTION,
          '  STANDS: %d of %d sentences of v2.3.1`s body carried unchanged; the ceiling clause (I-19) corrected the rest as listed; the stem clause, the fact clause and the restatement clause touched nothing; the history clause: every dated entry and era annotation carried unchanged' % (s['stands'], s['body_cur']),
          '  THE PAGE CLAUSE (I-28): the two pages name no line of this document in their Placement and the edition moves no node, so neither page is regenerated',
          '  THE LLM LINE: the monograph`s words and position ((R336)(6)); THE VERSION LINE v2.4.0; committed to PLACE-papers, deposited nowhere', '',
          '### ### **WHICH STRUCTURE CONFINES v2.4.0: %s ; H28a HELD (0 WORK-LIST ROWS) ; H28b %s (%d AGAINST %d) ; H28c %s ; STEMS %d ; CEILING %d ; NOT DEPOSITED.**' % (
              'WRITTEN BESIDE v2.3.1, UNEDITED', 'HELD' if s['d'] <= s['bound'] else 'REFUTED', s['d'], s['bound'], 'HELD' if ok else 'REFUTED', len(s['stems']), len(s['ceil_hits']))]
    return L


def main(argv):
    mode = argv[0] if argv else ''
    if mode not in ('dry', 'write'):
        sys.exit(__doc__)
    cur, text, crlf, cut = compose()
    s = score(cur, text, cut)
    ok = not s['stems'] and not s['ceil_hits']
    L = bank(cur, text, s, ok)
    print(NL.join(L))
    if mode == 'dry':
        print(NL.join(text.split(NL)[:9]))
        return
    if not ok or s['d'] > s['bound']:
        sys.exit('### A SCORE REFUTED -- NOTHING WRITTEN')
    with open(NEW + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(NEW + '.tmp', NEW)
    with open(BANK + '.tmp', 'wb') as f:
        f.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    print('written day1/Which_Structure_Confines_v2_4_0.md (%d lines) and data/b726_edition_diff.txt ; the line endings LF, the current version %s' % (len(text.split(NL)), 'CR LF' if crlf else 'LF'))


if __name__ == '__main__':
    main(sys.argv[1:])
