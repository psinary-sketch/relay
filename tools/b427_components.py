# -*- coding: utf-8 -*-
"""b427_components.py -- THE WITNESS ARC AT SITE (ii): THE CANDIDATE TABLE, AND THE WRITE IT LICENSES.

### ### **EACH CANDIDATE IS READ AT ITS SOURCE OR AT THE RECORD'S QUOTATION OF IT AND ATTEMPTED BY THREE STEPS IN
### THE ORDER b424 FIXED -- S1 CLASS, S2 HELD, S3 FORM -- AND IS FAILED AT THE FIRST STEP IT FAILS, THAT STEP'S
### SENTENCE QUOTED.** ### The cap: TWENTY candidates; no computation, no construction, no search beyond the survey's.
###   --attempt   the table: data/b427_candidates.txt and data/b427_candidates.json.
###   --write     the write the table licenses, through the ledger's writer: data/b427_ledger_write.txt.
###   (no flag)   the report and the expectation, its two clauses apart.
"""
import io
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b327_faces_row as W   # noqa: E402  ### THE LEDGER'S OWN WRITER, IMPORTED, NEVER COPIED.

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
FL = os.path.join(PP, 'FACES_LEDGER.md')
CC = os.path.join(D, 'b328_source_text.txt')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
B351 = os.path.join(D, 'b351_the_partition_question.txt')
B400C = os.path.join(D, 'b400_closing.txt')
B401C = os.path.join(D, 'b401_closing.txt')
B332 = os.path.join(D, 'b332_the_clause_stated.txt')
WSC = os.path.join(PP, 'day1', 'Which_Structure_Confines.md')
SOF = os.path.join(PP, 'day1', 'Silence_of_Foundations.md')
APS = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
RAIL = os.path.join(PP, 'meta', 'RAIL_ONLY_PRESERVATION_2026-08-09.md')
INSTR = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
TECH = os.path.join(PP, 'internal', 'TECHNE_ELEMENTS.md')
CAT = os.path.join(PP, 'internal', 'CATALOGOS.md')
T3PIN = 'SIDE-lv-conservation@93c27ec:SIDELvConservation/T3_StepNineBridge.lean'
SMEAR = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
TABLE = os.path.join(D, 'b427_candidates.txt')
TJSON = os.path.join(D, 'b427_candidates.json')
WREC = os.path.join(D, 'b427_ledger_write.txt')
MARK = '<!-- b427 update -->'
CAP = 20
NL = chr(10)
MISS = []

SHORT = {CC: 'CC 2006.13771v1 (relay data/b328_source_text.txt)',
         LAG: 'Lagarias math/0404394v4 (relay data/b358_source_lagarias0404394.txt)',
         FL: 'FACES_LEDGER.md row U1', T3PIN: 'SIDE-lv-conservation v0.10.0',
         WSC: 'PLACE-papers day1/Which_Structure_Confines.md', SOF: 'PLACE-papers day1/Silence_of_Foundations.md',
         APS: 'PLACE-papers day1/A_Place_to_Stand.md', RAIL: 'PLACE-papers meta/RAIL_ONLY_PRESERVATION_2026-08-09.md',
         INSTR: 'PLACE-papers phase1.5/method/INSTRUMENTS.md I-7', TECH: 'PLACE-papers internal/TECHNE_ELEMENTS.md',
         CAT: 'PLACE-papers internal/CATALOGOS.md',
         SMEAR: 'SIDE-global-section Core/SmearGeneral.lean'}


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def read(p):
    if p == T3PIN:
        return subprocess.run(['git', '-C', LV, 'show', '93c27ec:SIDELvConservation/T3_StepNineBridge.lean'],
                              capture_output=True).stdout.decode('utf-8', 'replace')
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def fold(s):
    """### MARKUP FOLDED BEFORE MATCHING, THE SAME WAY FOR SOURCE AND NEEDLE."""
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')).strip()


def q(path, start, end=None, cap=400):
    src, s0 = fold(read(path)), fold(start)
    i = src.find(s0)
    if i < 0:
        MISS.append('%s : %r' % (os.path.basename(path), start[:48]))
        return '### MISS'
    e0 = fold(end) if end else ''
    j = src.find(e0, i + len(s0)) if end else -1
    return src[i:j + len(e0)] if j > i else src[i:i + cap]


def where(path):
    return SHORT.get(path, 'relay data/%s' % os.path.basename(path))


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


# ### THE SITE'S OWN TEXT, PRINTED ONCE BEFORE ANY CANDIDATE.
SITE = [(FL, '(ii) — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.', 'could not do for the height'),
        (B351, 'THE CLASS THAT WOULD HAVE TO BE PROVED SILENT: `gamma > 150`', 'A CLASS IS NOT MADE OF INSTANCES.')]
CLASS = ('every height `gamma` of the object`s zeros -- and in particular `gamma > 150`, where the record`s only '
         'method stopped; the witness would be ONE ARGUMENT SERVING EVERY HEIGHT')
FORM_NOOBJ = ('FAIL', 'FORM -- no one object meets both clauses here: the candidate supplies no `Phi` serving every '
              'height and no non-degeneracy at it', [])

# ### (id, name, origin, [S1, S2, S3]); each step (outcome, kind -- the reason, [(path, start, end), ...]).
CANDS = [
    ('B1', 'the classical zero-free region, as bounding abscissa and not margin', 'the navigator`s opening list', [
        ('FAIL', 'COORDINATE BOUNDARY -- it is uniform in the height and says nothing at the height: what it bounds is '
                 'the ABSCISSA, and this site`s coordinate is the height`s own enumeration',
         [(WSC, 'The Euler product converges absolutely for σ > 1', 'no zero-free region.'),
          (APS, 'The boundary is exact: Λ(n) ≥ 0 yields the edge of the strip', 'crosses to the critical line.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- de la Vallee-Poussin 1896, cited by the corpus and derived nowhere in it', []),
        FORM_NOOBJ]),
    ('B2', 'a growth bound on the margin in height', 'the navigator`s opening list', [
        ('FAIL', 'BOUNDED BY A MEASUREMENT -- the growth is recorded ACROSS THE COMPUTED RANGE, thirty zeros with '
                 'gamma in [14.13, 101.32]; it is the site`s own disease and not its cure',
         [(RAIL, 'The persistence finding: stripping the Gamma envelope', 'widens without bound.'),
          (B351, 'A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE.', None)]),
        ('PASS', 'OWNED -- the record`s own persistence finding, printed at its own range', []),
        FORM_NOOBJ]),
    ('B3', 'the density theorems, as the register the channels are bright for', 'the navigator`s opening list', [
        ('PASS', 'the density register IS uniform in the height -- an `N(sigma, T)` statement holds at every `T`', []),
        ('FAIL', 'DENSITY-PLACEMENT SPLIT -- the standing screen `I-7` refuses the register for this question by a '
                 'test on the DEFINITION, and its evidence base is four routes to one boundary',
         [(INSTR, 'The screen, one question, asked of the DEFINITION', 'REFUSE THE COMPUTATION, and state why.'),
          (SOF, 'Classical sieve methods operate through this coupling.', 'is κ = 0.'),
          (TECH, 'The sieve operates through the distributive interface', 'through which classical tools operate.')]),
        FORM_NOOBJ]),
    ('B4', 'the abscissa`s convergent sum, b326`s summed bound', 'the survey`s search; row U1 names it', [
        ('FAIL', 'CLASS BOUNDARY -- the abscissa is not a site of this row, and the row says so in its own words',
         [(FL, 'The abscissa’s convergent sum is a witness for no site of this row', 'was therefore never entered.'),
          (B351, 'THE ABSCISSA WAS ALREADY CLOSED, AND HAS BEEN SINCE b326.', 'about the looking.')]),
        ('PASS', 'OWNED -- a one-line summed bound the record holds since b326', []),
        FORM_NOOBJ]),
    ('B5', 'the Riemann-von Mangoldt main term', 'the survey`s search: b351 section (4)', [
        ('PASS', 'it is a statement at every `T` -- the count`s main term, not a count at one height', []),
        ('PASS', 'OWNED -- printed by the record`s own completeness census for its own object', []),
        ('FAIL', 'INSTANCES NOT A CLASS -- it says the instances never run out, which is the reason the site is open '
                 'and not a witness closing it',
         [(B351, 'The same act prints the main term that says the instances never run out', 'A CLASS IS NOT MADE OF INSTANCES.')])]),
    ('B6', 'the completeness census itself, sixty boxes of the argument principle', 'the survey`s search: b351 section (4)', [
        ('FAIL', 'BOUNDED BY A MEASUREMENT -- `150` is where the census stopped and is not a property of the object',
         [(B351, 'THE NUMBER `150` IS WHERE THE CENSUS STOPPED', 'IT IS NOT A PROPERTY OF THE OBJECT.'),
          (B351, 'The completeness census ran the argument principle', "`180` ZEROS OF `Lambda_Q` WITH `0 < t < 150`")]),
        ('PASS', 'OWNED -- the record`s own census, its count closing exactly where it stopped', []),
        FORM_NOOBJ]),
    ('B7', 'Proposition C.1, quantified over the whole set of non-trivial zeros', 'the survey`s read 5', [
        ('PASS', 'it ranges over the set of non-trivial zeros, so over every height',
         [(CC, 'Proposition C.1 Let Z Ă C be the set of non-trivial zeros', '@zPF. (155)')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- page index 51 of the verified artefact, graded by b400',
         [(B400C, 'Proposition C.1 AVAILABLE at the window', 'page index 51')]),
        ('FAIL', 'FORM -- it is the universal quantifier itself, not an object serving it',
         [(B332, 'the quantifiers -- over the class, infinite, and through the explicit formula over', 'they are the clause.')])]),
    ('B8', 'CC`s Theorem 1, positivity under a support hypothesis', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- support inside [2^-1/2, 2^1/2], chosen so that no prime enters; a condition on the '
                 'test function and not on the height',
         [(CC, 'In this paper we consider the simplest instance of this', 'so that rational primes are not involved'),
          (B400C, 'THEOREM 1 CARRIES A SUPPORT HYPOTHESIS AND PROPOSITION C.1', 'CARRIES NONE')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- the source`s theorem, graded by b400', []),
        FORM_NOOBJ]),
    ('B9', 'CC`s Theorem 6.11', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- support inside [2^-1/2, 2^1/2]',
         [(CC, 'Theorem 6.11 LetgPC8', 'with support in the interval r2´1{2, 21{2s')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- a theorem of the verified source, not derived in the record', []),
        FORM_NOOBJ]),
    ('B10', 'CC`s positivity for small enough intervals', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- small enough intervals only, and the smallness is on the interval and not the height',
         [(CC, 'As a preliminary test we prove, using a simple estimate', 'the positivity holds.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- a statement of the verified source', []),
        FORM_NOOBJ]),
    ('B11', 'Lagarias`s Theorem 2.2, Li`s criterion at every n', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- the Li coefficients, indexed by `n >= 1`; `n` is not a height and the family is not '
                 'this object`s',
         [(LAG, 'Theorem 2.2. Letπ be an irreducible cuspidal', '(2.20)')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- an equivalence of the verified source', []),
        FORM_NOOBJ]),
    ('B12', 'Lagarias`s Theorem 5.1, an absolute constant from some n on', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- the archimedean term on the Li family, and row U1 already rules where its constant '
                 'is a witness',
         [(LAG, 'Theorem 5.1. For any irreducible cuspidal', '(5.1)'),
          (FL, 'Theorem 5.1’s absolute constant is a witness for the ARCHIMEDEAN side', 'and not for this one.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- graded at b358', []),
        FORM_NOOBJ]),
    ('B13', 'Lagarias`s Theorem 6.1, an O-term in n', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- the finite-place term on the Li family, its implied constant depending on the '
                 'representation',
         [(LAG, 'Theorem 6.1. For any irreducible cuspidal', 'depends on π.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- its hypothesis on the representation undecided',
         [(B401C, 'HYPOTHESIS QUANTIFYING OVER THE REPRESENTATION', 'NOT DECIDED HERE EITHER.')]),
        FORM_NOOBJ]),
    ('B14', 'the compiled shared-witness theorem, T3prime_shared_witness', 'the survey`s read 3', [
        ('FAIL', 'CLASS BOUNDARY -- a Set Coupling over functions R -> C, identified with no site`s family',
         [(FL, 'not one of the six sites is stated in those terms', 'six sites, zero candidates.')]),
        ('PASS', 'OWNED -- compiled at the pin, both profiles printed',
         [(FL, 'Both profiles printed at the pin', 'at neither terminal.')]),
        ('FAIL', 'FORM -- it takes h1 and h2 as hypotheses and supplies neither', [])]),
    ('B15', 'the finite side`s zero', 'row U1: named by the navigator as found', [
        ('FAIL', 'CLASS BOUNDARY -- a membership test against a seven-cell decided list, not a statement at every height',
         [(FL, 'The finite side’s zero is not a shared witness across places either', 'discharged by `decide`')]),
        ('PASS', 'OWNED -- a kernel clause discharged by `decide`', []),
        FORM_NOOBJ]),
    ('B16', 'the Vinogradov-Korobov shrinkage law in the height', 'the survey`s search: RAIL_ONLY line 166', [
        ('PASS', 'it IS one law at every height -- the region`s width given as a function of `gamma`',
         [(RAIL, 'while the Vinogradov-Korobov zero-free region shrinks as', 'widens without bound.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- a classical theorem the corpus NAMES and never derives; and what it is a law '
                 'about is again the abscissa`s region, not this site`s enumeration',
         [(CAT, 'Classical analytic number theory — Ingham density estimates, Vinogradov-Korobov zero-free regions',
           'confirmed independently by Conservation of Spectra and INTERFACETS).'),
          (APS, 'The boundary is exact: Λ(n) ≥ 0 yields the edge of the strip', 'crosses to the critical line.')]),
        FORM_NOOBJ]),
    ('B17', 'the functional equation`s reflection of b326`s bound', 'the survey`s search: b351 section (3)', [
        ('FAIL', 'COORDINATE BOUNDARY -- it confines `beta` to `(-0.5, 1.5)` for all zeros, which is the coordinate '
                 'that closed and not this one',
         [(B351, '`SUM_{k>=2} r_Q(k) k^{-3/2} = 1.38 < 2`', 'at `Re s <= -0.5`)')]),
        ('PASS', 'OWNED -- the record`s own bound since b326', []),
        FORM_NOOBJ]),
    ('B18', 'the placement screen `I-7` itself', 'the survey`s search: INSTRUMENTS.md', [
        ('PASS', 'it applies to any statistic at any height -- the screen is not height-indexed', []),
        ('PASS', 'OWNED -- standing and author-ruled, filed 2026-08-05', []),
        ('FAIL', 'FORM -- A SCREEN IS NOT A WITNESS: it REFUSES candidates by a test on their definition and supplies '
                 'no object satisfying h1 and h2; a refusal closes nothing',
         [(INSTR, 'The evidence base — four independent derivations of the same boundary',
           'the density register does not reach placement.')])]),
    ('B19', 'the kernel`s general smear, smear_general', 'the survey`s search: b419, the kernel at HEAD', [
        ('FAIL', 'CLASS BOUNDARY -- quantified over bases and levels, not over heights; outside the description',
         [(SMEAR, 'theorem smear_general (p n : Nat)', 'B329.sumAQ p n')]),
        ('PASS', 'OWNED -- proved, 0 axioms, at b419', []),
        FORM_NOOBJ]),
]

# ### READ AND NOT ADMITTED -- every hit of the survey's search that is not a candidate, with its reason.
NOT_ADMITTED = [
    ('H1/H3: CC lines quantifying over `all zeros`', 'Proposition C.1: candidate B7'),
    ('H1: CC, `for all g` at a support', 'candidates B8, B9, B10 -- a condition on the test function, not the height'),
    ('H1: Lagarias, `for all n >= 1`', 'candidate B11 -- the index is `n`, which is not a height'),
    ('H2: Lagarias Theorem 6.1, `unconditionally`', 'candidate B13'),
    ('H3: Lagarias, `n >= K(pi)`', 'candidate B12'),
    ('H1/H2: b326, b334, b351 -- the charted ranges', 'candidates B6 and B17; a charted range is a measurement'),
    ('H2: FINDINGS, b358 -- the Li asymptotics', 'candidates B12, B13; and b358 already owns them'),
    ('H1: row U1 -- the two witnesses the navigator named', 'candidates B4 and B15'),
    ('H3: INSTRUMENTS I-7, TECHNE_ELEMENTS, Silence_of_Foundations', 'candidates B3 and B18'),
    ('H2: RAIL_ONLY -- the persistence finding and the VK law', 'candidates B2 and B16, read apart'),
    ('H1: day1 -- the codimension dichotomy and the surround', 'statements about the mechanism classes, not about a '
     'height; outside the description'),
    ('H3: b304, b305, b312, b317, b321 -- the archimedean window', 'site (i)`s ground, attempted at b424 and not '
     're-attempted here'),
    ('GridTrace.grid_trace_is_signed_count', 'quantified over grids and levels: the same kind as B19, not counted twice'),
]


def first_fail(steps):
    for k, (out, kind, _qs) in enumerate(steps):
        if out == 'FAIL':
            return k, kind.split(' -- ')[0]
    return None, 'HELD'


# ### SITE (i)'S OWN COUNTS, READ OFF b424'S BANKED JSON AND NEVER TYPED.
def site_i_tally():
    try:
        J = json.loads(read(os.path.join(D, 'b424_candidates.json')))
    except Exception:
        return {}, 0
    t = {}
    for c in J.get('candidates', []):
        if c.get('first') is not None:
            t[c['kind']] = t.get(c['kind'], 0) + 1
    return t, len(J.get('candidates', []))


def run_attempt():
    R = ['=' * 100, 'b427 -- THE WITNESS ARC AT SITE (ii): THE CANDIDATE TABLE.', '=' * 100, '  at (UTC) : %s' % utc(),
         '  cap : %d candidates' % CAP, '']
    say = R.append
    say('-' * 100)
    say('### THE SITE`S OWN TEXT, PRINTED ONCE BEFORE ANY CANDIDATE.')
    say('-' * 100)
    say('  the class the site quantifies over :')
    for w in wrap(CLASS, 94):
        say('      %s' % w)
    for p, s, e in SITE:
        say('  %s :' % where(p))
        for w in wrap(q(p, s, e), 94):
            say('      | %s' % w)
    say('')
    say('-' * 100)
    say('### THE CANDIDATES, EACH BY S1 CLASS, S2 HELD, S3 FORM, IN THAT ORDER.')
    say('-' * 100)
    out = []
    for cid, name, origin, steps in CANDS:
        k, kind = first_fail(steps)
        say('  [%s] %s' % (cid, name))
        say('      origin : %s' % origin)
        qrec = []
        for n, (res, why, qs) in enumerate(steps):
            say('      S%d %-5s : %s -- %s' % (n + 1, ('CLASS', 'HELD', 'FORM')[n], res, why))
            for (p, s, e) in qs:
                t = q(p, s, e)
                qrec.append(dict(step=n + 1, path=p, start=s, end=e, text=t))
                say('          %s :' % where(p))
                for w in wrap(t, 90):
                    say('          | %s' % w)
            if n == k and not qs:
                MISS.append('%s: its first failing step carries no quotation' % cid)
        say('      ### VERDICT [%s] : %s' % (cid, ('FAILED AT S%d -- %s' % (k + 1, kind)) if k is not None else 'HELD'))
        say('')
        out.append(dict(id=cid, name=name, origin=origin, first=(k + 1) if k is not None else None, kind=kind,
                        steps=[dict(out=a, why=b) for a, b, _c in steps], quotes=qrec))
    held = [c for c in out if c['first'] is None]
    tally = {}
    for c in out:
        if c['first'] is not None:
            tally[c['kind']] = tally.get(c['kind'], 0) + 1
    say('-' * 100)
    say('### READ AND NOT ADMITTED -- EVERY HIT OF THE SURVEY`S SEARCH THAT IS NOT A CANDIDATE.')
    say('-' * 100)
    for a, b in NOT_ADMITTED:
        say('  %-58s %s' % (a[:58], b))
    say('')
    say('-' * 100)
    say('### THE TALLY.')
    say('-' * 100)
    say('  ### CANDIDATES %d (cap %d) ; FAILED %d ; HELD %d' % (len(out), CAP, len(out) - len(held), len(held)))
    say('  ### TALLY BY FIRST FAILING STEP`S KIND : %s'
        % ' ; '.join('%s %d' % (k2, v) for k2, v in sorted(tally.items(), key=lambda x: (-x[1], x[0]))))
    say('  ### FAILED AT S1 : %d ; AT S2 : %d ; AT S3 : %d' % tuple(sum(1 for c in out if c['first'] == s) for s in (1, 2, 3)))
    say('')
    say('-' * 100)
    say('### THE LINE THE SITE OWES: WHERE ITS FAILURES LAND, AGAINST SITE (i)`S, COUNTED.')
    say('-' * 100)
    ti, ni = site_i_tally()
    say('  site (i), b424, read off its own banked JSON : %d candidates ; %s'
        % (ni, ' ; '.join('%s %d' % (k2, v) for k2, v in sorted(ti.items(), key=lambda x: -x[1]))))
    say('  site (ii), this act                          : %d candidates ; %s'
        % (len(out), ' ; '.join('%s %d' % (k2, v) for k2, v in sorted(tally.items(), key=lambda x: -x[1]))))
    shared = sorted(set(ti) & set(tally))
    onlyii = sorted(set(tally) - set(ti))
    same = sum(tally[k2] for k2 in shared)
    diff = sum(tally[k2] for k2 in onlyii)
    say('  ### KINDS SHARED WITH SITE (i) : %s' % (shared or 'none'))
    say('  ### KINDS THIS SITE ADDS       : %s' % (onlyii or 'none'))
    say('  ### ### **AT A BOUNDARY SITE (i) ALSO USED : %d OF %d. ### AT A BOUNDARY NEW TO THIS SITE : %d OF %d.**'
        % (same, len(out), diff, len(out)))
    cb = tally.get('CLASS BOUNDARY', 0)
    cbi = ti.get('CLASS BOUNDARY', 0)
    say('  ### THE CLASS BOUNDARY ALONE : site (i) %d of %d ; site (ii) %d of %d.' % (cbi, ni, cb, len(out)))
    say('  ### **THE ARC IS CONVERGING ON ONE BOUNDARY ONLY IF THAT SHARE HOLDS; IT IS PRINTED AND NOT ASSERTED.**')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    io.open(TABLE, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), candidates=out, held=len(held), tally=tally, site_i=ti, site_i_n=ni,
                        same=same, diff=diff, misses=MISS), indent=1, ensure_ascii=False)
    open(TJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(TJSON + '.tmp', TJSON)
    print(NL.join(R))
    return 0 if not MISS else 1


def cell(s):
    """### Corpus prose: no pipe, no newline, and an apostrophe is a curly one, never a backtick (b422's lesson)."""
    return s.replace('|', '/').replace(NL, ' ').replace('`', '’')


def clip(s, n=220):
    """### A quotation is cut at a word boundary with an ellipsis, never mid-word; an asterisk is ESCAPED, never dropped."""
    s = s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' …'
    return s.replace('*', chr(92) + '*')


def block_lines(J):
    cands = J['candidates']
    tally, ti, ni = J['tally'], J['site_i'], J['site_i_n']
    L = ['', MARK, '',
         '## UPDATE — filed 2026-09-11 (b427): row U1, entry (ii) — the witness column’s exhausted list', '',
         '*Rows above are never rewritten; an update names the row it bears on. Written through the writer’s '
         '`append_block`. Row U1’s line, entry (ii)’s `WITNESS: NONE KNOWN`, and the freeze at six (b409) stand as they '
         'read; no seventh site is entered.*', '',
         '| candidate | failed at | the step’s sentence, quoted, and where |', '|:--|:--|:--|']
    for c in cands:
        qs = [x for x in c['quotes'] if x['step'] == c['first']]
        cite = '; '.join('*"%s"* (%s)' % (cell(clip(x['text'])), cell(where(x['path']))) for x in qs[:2])
        L.append('| **%s** %s | S%d — %s | %s |' % (c['id'], cell(c['name']), c['first'], cell(c['kind']), cite))
    L += ['',
          '*%d candidates — the navigator’s opening three (the classical zero-free region as bounding abscissa not '
          'margin; a growth bound on the margin in height; the density theorems as the register the channels are '
          'bright for), and %d the search supplied by description (relay `data/b427_extract.txt`, every hit hand-read) '
          '— each read at its source or at the record’s quotation of it and attempted by three steps in b424’s fixed '
          'order: S1 CLASS, S2 HELD, S3 FORM. **No witness held.** First failing steps, by kind: %s. The site’s own '
          'cell was quoted before any candidate and stands: the witness would be **one argument serving every height**, '
          'against a method that produces zeros one at a time.*'
          % (len(cands), len(cands) - 3,
             '; '.join('%s %d' % (k, v) for k, v in sorted(tally.items(), key=lambda x: (-x[1], x[0])))),
          '',
          '*__And the line this site owes the arc, counted rather than recalled.__ Site (i) (b424) failed %d candidates '
          'at %s. Site (ii) fails %d at %s. **%d of %d land at a boundary site (i) also used; %d of %d land at a boundary '
          'new to this site** — %s. **The class boundary alone: %d of %d at site (i), %d of %d at site (ii).** The arc '
          'is not converging on a single boundary: the second site needs %d kinds the first never used, and the '
          'navigator’s expected kind — the density–placement split — accounts for exactly %d of them.*'
          % (ni, '; '.join('%s %d' % (k, v) for k, v in sorted(ti.items(), key=lambda x: -x[1])),
             len(cands), '; '.join('%s %d' % (k, v) for k, v in sorted(tally.items(), key=lambda x: (-x[1], x[0]))),
             J['same'], len(cands), J['diff'], len(cands),
             ', '.join(sorted(set(tally) - set(ti))) or 'none',
             ti.get('CLASS BOUNDARY', 0), ni, tally.get('CLASS BOUNDARY', 0), len(cands),
             len(set(tally) - set(ti)), tally.get('DENSITY-PLACEMENT SPLIT', 0)),
          '',
          '*CC is quoted in its extracted text layer (relay `data/b328_source_text.txt`), the layer the writer verifies '
          'against, so its mathematics reads as that layer renders it. No grade is conferred by a seat, no bridge is '
          'typed between sites, and nothing is claimed about `h2`. Filed by b427 (relay `data/b427_candidates.txt`).*',
          '']
    return L


def run_write():
    R = ['=' * 100, 'b427 -- THE WRITE THE TABLE LICENSES, THROUGH THE LEDGER`S WRITER.', '=' * 100,
         '  at (UTC) : %s' % utc()]
    say = R.append
    try:
        J = json.loads(read(TJSON))
    except Exception as exc:
        say('  ### REFUSED: the table is not banked (%s).' % exc)
        io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
        return 1
    cands = J['candidates']
    before = read(FL)
    u1_before = next((x for x in before.splitlines() if x.startswith('| U1 ')), '')
    say('  candidates %d ; held %d' % (len(cands), J['held']))
    say('  ### THE CELL IS WRITTEN ONLY IF A CANDIDATE HOLDS. ### Otherwise the exhausted list is appended as a block,')
    say('  ### on b424`s pattern, and row U1`s line is not touched.')
    if J['held']:
        say('  ### A CANDIDATE HOLDS -- THIS TOOL DOES NOT WRITE THE WITNESS FIELD; THE ACT STOPS FOR THE WRITER`S ROW PATH.')
        io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
        return 1
    triples = [(x['path'], x['start'], True) for c in cands for x in c['quotes'] if x['step'] == c['first']]
    triples = [t for t in triples if t[0] != T3PIN]
    miss = W.verify_quotes(triples)
    say('  quotations at the first failing steps, verified by the writer`s verify_quotes : %d ; misses : %d %s'
        % (len(triples), len(miss), miss))
    if miss:
        say('  ### REFUSED: a quotation is not in its file. NOTHING WRITTEN.')
        io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
        return 1
    st, det = W.append_block(MARK, block_lines(J))
    after = read(FL)
    u1_after = next((x for x in after.splitlines() if x.startswith('| U1 ')), '')
    say('  append_block : %s -- %s' % (st, det))
    say('  row U1`s line byte-identical before and after : %s' % (u1_before == u1_after and bool(u1_after)))
    say('  entry (ii)`s WITNESS field after : %s' % (re.findall(r'\(ii\)` — KIND: [^.]*\. WITNESS: `([A-Z ]+)`', u1_after)[:1]))
    say('  the six WITNESS fields after : %s' % re.findall(r'WITNESS: *`([A-Z ]+)`', u1_after))
    say('  b424`s own block still present : %s' % ('<!-- b424 update -->' in after))
    say('  NO SEVENTH SITE is entered : %s' % (len(re.findall(r'WITNESS: *`([A-Z ]+)`', u1_after)) == 6))
    say('  the prior ledger a true prefix : %s' % after.startswith(before.rstrip(NL)))
    say('  lines deleted : 0')
    say('  ### ### **LEDGER WRITE : %s**' % st)
    say('')
    say('### THE BLOCK, AS WRITTEN:')
    R += ['  | %s' % x for x in block_lines(J)]
    say('=' * 100)
    io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    print(NL.join(R[:14]))
    return 0 if st == 'WRITTEN' else 1


def main():
    Lr = []
    say = Lr.append
    try:
        J = json.loads(read(TJSON))
    except Exception:
        J = dict(candidates=[], held=0, tally={}, site_i={}, site_i_n=0, same=0, diff=0, misses=['no json'])
    wr = read(WREC)
    fails = [] if wr else ['the write record is absent']
    say('=' * 100)
    say('b427_components.py -- THE WITNESS ARC AT SITE (ii), THE REPORT.')
    say('=' * 100)
    for c in J['candidates']:
        say('  %-5s %-62s FAILED AT S%s -- %s' % (c['id'], c['name'][:62], c['first'], c['kind']))
    n = len(J['candidates'])
    held = J['held']
    say('')
    say('  ### CANDIDATES %d ; HELD %d ; FAILED %d' % (n, held, n - held))
    say('  ### TALLY : %s' % ' ; '.join('%s %d' % (k, v) for k, v in sorted(J['tally'].items(), key=lambda x: (-x[1], x[0]))))
    say('  ### SAME BOUNDARY AS SITE (i) : %d of %d ; NEW TO THIS SITE : %d of %d' % (J['same'], n, J['diff'], n))
    for needle in ('anchor misses : 0', 'NO SEVENTH SITE is entered : True', 'LEDGER WRITE : WRITTEN',
                   'row U1`s line byte-identical before and after : True', 'misses : 0 []'):
        ok = (needle in read(TABLE)) or (needle in wr)
        fails += [] if ok else [needle]
        say('  %-46s %s' % (needle, ok))
    dps = J['tally'].get('DENSITY-PLACEMENT SPLIT', 0)
    newkinds = sorted(set(J['tally']) - set(J['site_i']))
    say('')
    say('### THE EXPECTATION, ITS CLAUSES APART (R27):')
    say('  (L2) *site (ii)`s list is exhausted with no witness held* -- ### **%s** (%d of %d failed at a quoted step; '
        'held %d).' % ('MET' if (n and held == 0) else 'REFUTED', n - held, n, held))
    say('  (L2) *its failures land at a different boundary than site (i)`s -- the density-placement split rather than '
        'the class boundary* -- ### **%s** (%d of %d land at a boundary new to this site, in %d kinds: %s; the '
        'density-placement split accounts for %d; the class boundary still takes %d of %d).'
        % ('MET' if (n and J['diff'] > n / 2 and dps == J['diff']) else
           ('PARTLY MET' if J['diff'] else 'REFUTED'),
           J['diff'], n, len(newkinds), ', '.join(newkinds) or 'none', dps, J['tally'].get('CLASS BOUNDARY', 0), n))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b427_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(Lr) + NL)
    print(NL.join(Lr))
    return 1 if fails else 0


if __name__ == '__main__':
    if '--attempt' in sys.argv:
        sys.exit(run_attempt())
    if '--write' in sys.argv:
        sys.exit(run_write())
    sys.exit(main())
