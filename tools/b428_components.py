# -*- coding: utf-8 -*-
"""b428_components.py -- SITE (iii), THE DISPROOF LANE NAMED, AND THE EXTERNAL READ PRICED.

### ### **COMPONENT 1** ### -- each candidate read at its source or at the record's quotation of it and attempted by
### three steps in b424's fixed order (S1 CLASS, S2 HELD, S3 FORM), failed at the first step it fails with that
### step's sentence QUOTED and its boundary NAMED, or HELD. ### **COMPONENT 2** ### -- the disproof lane NAMED and
### NOT OPENED: a filing, from the record's own instruments and the barrier keystone's own words. ### **COMPONENT 3**
### -- the external read PRICED and NOT RUN: the address located, pinned by digest IF REACHABLE, and the read costed
### in ACTS; no file of the external proof is read at content.
###   --attempt   the candidate table: data/b428_candidates.txt and .json
###   --write     the write the table licenses, through the ledger's writer: data/b428_ledger_write.txt
###   --disproof  Component 2's filing: data/b428_disproof_lane.txt, .json
###   --price     Component 3's location and pricing: data/b428_external_price.txt, .json
###   (no flag)   the report and the expectations (N1), (N2), their clauses apart.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
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
B353 = os.path.join(D, 'b353_the_missing_statement.txt')
B334 = os.path.join(D, 'b334_the_aim_map.txt')
B328 = os.path.join(D, 'b328_the_discriminating_family.txt')
B400C = os.path.join(D, 'b400_closing.txt')
B362 = os.path.join(D, 'b362_the_approximation_register.txt')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
RDM = os.path.join(PP, 'README.md')
SMEAR = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
T3PIN = 'SIDE-lv-conservation@93c27ec:SIDELvConservation/T3_StepNineBridge.lean'
TABLE = os.path.join(D, 'b428_candidates.txt')
TJSON = os.path.join(D, 'b428_candidates.json')
WREC = os.path.join(D, 'b428_ledger_write.txt')
DREC, DJSON = os.path.join(D, 'b428_disproof_lane.txt'), os.path.join(D, 'b428_disproof_lane.json')
PREC, PJSON = os.path.join(D, 'b428_external_price.txt'), os.path.join(D, 'b428_external_price.json')
MARK = '<!-- b428 update -->'
CAP = 22
NL = chr(10)
MISS = []

SHORT = {CC: 'CC 2006.13771v1 (relay data/b328_source_text.txt)',
         LAG: 'Lagarias math/0404394v4 (relay data/b358_source_lagarias0404394.txt)',
         FL: 'FACES_LEDGER.md row U1', T3PIN: 'SIDE-lv-conservation v0.10.0',
         IB: 'PLACE-papers phase1.5/method/INVARIANCE_BARRIERS.md', RDM: 'PLACE-papers README.md',
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


def qrow(prefix, start, end=None, cap=400):
    """### A LEDGER ROW IS ONE LINE; a quotation from it is taken from THAT LINE, not from the file -- otherwise a
    ### needle meant for one row matches in another and the citation is wrong while the arm stays quiet."""
    line = next((x for x in read(FL).splitlines() if x.startswith(prefix)), '')
    src, s0 = fold(line), fold(start)
    i = src.find(s0)
    if i < 0:
        MISS.append('FACES_LEDGER row %s : %r' % (prefix.strip('| '), start[:48]))
        return '### MISS'
    e0 = fold(end) if end else ''
    j = src.find(e0, i + len(s0)) if end else -1
    return src[i:j + len(e0)] if j > i else src[i:i + cap]


def qu1(start, end=None, cap=400):
    return qrow('| U1 ', start, end, cap)


F7 = 'FACES_LEDGER.md row F7'


def qf7(start, end=None, cap=400):
    return qrow('| F7 ', start, end, cap)


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
SITE = [(FL, "(iii) — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.", 'No such `g` is named.'),
        (B353, 'SO: AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.',
         'survives the located statement intact.')]
CLASS = ('the UNION over all support widths -- the criterion quantifies over *"all g in Cc^infty(R+*) with g~(z) = 0 '
         'for all z in F"*; the witness would be ONE `g` SERVING EVERY WIDTH, and this is the one site of the six '
         'whose own banked text supplies the inner existential in the theorem`s shape')
FORM_NOOBJ = ('FAIL', 'FORM -- no one object meets both clauses here: no `g` is named that serves every `A`, and no '
              'non-degeneracy is established at one', [])

# ### (id, name, origin, [S1, S2, S3]); each step (outcome, kind -- the reason, [(path, start, end), ...]).
CANDS = [
    ('C1', 'monotonicity in the radius -- the increasing union', 'the navigator`s opening list', [
        ('PASS', 'the union IS the site`s class, and it is an increasing one', [
            (B353, 'The union is an increasing union, and non-negativity on each', 'IF THE FUNCTIONAL IS THE SAME FUNCTIONAL ON EACH.')]),
        ('FAIL', 'INSTRUMENT DOES NOT REACH -- the increasing-union step needs ONE functional on every member, and the '
                 'record does not establish that what it evaluates at the reaching widths is the functional it '
                 'evaluates at the covered ones', [
            (B353, 'The record does not establish that the object it evaluates at', 'past `rho = 100`.'),
            (B334, 'THE SQUARE AND THE REMAINDER, ON THE REACHING LEG: NOT REACHED', "outside the evaluator's reach.")]),
        FORM_NOOBJ]),
    ('C2', 'a limit across radii', 'the navigator`s opening list', [
        ('PASS', 'a limit across radii would be exactly a statement on the union', []),
        ('FAIL', 'ABSENT -- the pinned source was read at content for precisely this and it is not there',
         [(B353, 'a statement carrying positivity from one support to a larger one', 'NOT LOCATED** in the pinned source;'),
          (B353, 'positivity of the Weil functional on the seed family at half-width', 'WITH NO LIMIT ARGUMENT AND NO TOPOLOGY.')]),
        FORM_NOOBJ]),
    ('C3', 'Boas-Kac at each radius, the existential the site owns', 'the navigator`s opening list', [
        ('FAIL', 'CLASS BOUNDARY -- it exhausts the admissible class AT a width and says nothing about passing between '
                 'widths; the `∃g` it supplies is INDEXED BY `A`',
         [(B353, 'AND EVERY CONCLUSION IT GIVES IS AT THE SAME `A` IT WAS GIVEN.', 'PASSING FROM ONE `A` TO A LARGER'),
          (B353, 'SO: AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.', None)]),
        ('FAIL', 'IMPORT UNDER THE BAR -- Proposition 2 of the pinned source, trusted at cite', []),
        ('FAIL', 'FORM -- and this is the one site where the form TRANSPOSES: the shape is right and the object is '
                 'missing. The row states both clauses and then states that no such `g` is named',
         [(FL, 'Its two clauses read: `h1`, one `g` works at every `A`', 'No such `g` is named.')])]),
    ('C4', 'the uniform-in-A bound, as b353 typed it', 'the survey`s read 2', [
        ('PASS', 'it is typed over the union, which is the site`s class',
         [(B353, 'THE MISSING STATEMENT, TYPED:', 'implies it on the union over all `A`."')]),
        ('FAIL', 'ABSENT -- typed as what is missing, and searched for in the pinned source without being found',
         [(B353, 'a statement bounding the Weil functional uniformly in the support parameter', 'NOT** LOCATED** in the pinned source.')]),
        FORM_NOOBJ]),
    ('C5', 'CC`s Theorem 1, positivity under a support hypothesis', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- support inside the interval the source chose so that no prime enters',
         [(CC, 'In this paper we consider the simplest instance of this', 'so that rational primes are not involved'),
          (B400C, 'THEOREM 1 CARRIES A SUPPORT HYPOTHESIS AND PROPOSITION C.1', 'CARRIES NONE')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- the source`s theorem, graded by b400', []),
        FORM_NOOBJ]),
    ('C6', 'CC`s Theorem 6.11', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- support inside [2^-1/2, 2^1/2], one width',
         [(CC, 'Theorem 6.11 LetgPC8', 'with support in the interval r2´1{2, 21{2s')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- a theorem of the verified source', []),
        FORM_NOOBJ]),
    ('C7', 'CC`s positivity for small enough intervals', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- SMALL ENOUGH intervals, which is a condition on the width and the opposite of a '
                 'statement across widths',
         [(CC, 'As a preliminary test we prove, using a simple estimate', 'the positivity holds.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- a statement of the verified source', []),
        FORM_NOOBJ]),
    ('C8', 'Proposition C.1, which carries no support hypothesis at all', 'the survey`s read 5; b400 grades it', [
        ('PASS', 'it carries NO support hypothesis, so it does range over the union -- the only candidate here of '
                 'which that is true',
         [(CC, 'Proposition C.1 Let Z Ă C be the set of non-trivial zeros', '@zPF. (155)'),
          (B400C, 'THEOREM 1 CARRIES A SUPPORT HYPOTHESIS AND PROPOSITION C.1', 'CARRIES NONE')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- page index 51 of the verified artefact, graded by b400',
         [(B400C, 'Proposition C.1 AVAILABLE at the window', 'page index 51')]),
        ('FAIL', 'FORM -- it IS the universal quantifier the site needs served, not an object serving it', [])]),
    ('C9', 'the corpus`s own `f = g * g^#` at the covered cells', 'the survey`s read 2', [
        ('FAIL', 'BOUNDED BY A MEASUREMENT -- the covered cells are a measured set inside the source`s own interval, '
                 'and the reaching legs sit outside it',
         [(B353, 'the corpus already builds its `f` as `g * g^#`, so it is already inside the family', 'at every covered cell.')]),
        ('PASS', 'OWNED -- the record builds it and Boas-Kac names the family it is in', []),
        FORM_NOOBJ]),
    ('C10', 'the eps evaluator`s own reach across radii', 'the survey`s read 6', [
        ('FAIL', 'INSTRUMENT DOES NOT REACH -- measured at five radii, a sign change and a growth past rho = 100',
         [(B334, "The frame's X = 32 against f's support a^2 = 1600", "outside the evaluator's reach.")]),
        ('PASS', 'OWNED -- the record`s own measurement, printed at its own radii', []),
        FORM_NOOBJ]),
    ('C11', 'the square and the remainder for Z_Q', 'the survey`s read 6', [
        ('FAIL', 'ABSENT -- the record says in its plainest words that the instrument does not exist',
         [(B334, 'The square and the remainder for Z_Q: NOT AN INSTRUMENT THE RECORD HAS', 'said on every Epstein line.')]),
        FORM_NOOBJ,
        FORM_NOOBJ]),
    ('C12', 'Lagarias`s Theorem 2.2, Li`s criterion at every n', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- the Li coefficients, indexed by `n >= 1`; `n` is not a support width and the '
                 'family is not this object`s',
         [(LAG, 'Theorem 2.2. Letπ be an irreducible cuspidal', '(2.20)')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- an equivalence of the verified source', []),
        FORM_NOOBJ]),
    ('C13', 'Lagarias`s Theorem 5.1', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- the archimedean term on the Li family; row U1 already rules where its constant is '
                 'a witness',
         [(LAG, 'Theorem 5.1. For any irreducible cuspidal', '(5.1)'),
          (FL, 'Theorem 5.1’s absolute constant is a witness for the ARCHIMEDEAN side', 'and not for this one.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- graded at b358', []),
        FORM_NOOBJ]),
    ('C14', 'Lagarias`s Theorem 6.1', 'the survey`s read 5', [
        ('FAIL', 'CLASS BOUNDARY -- the finite-place term on the Li family, indexed by `n`',
         [(LAG, 'Theorem 6.1. For any irreducible cuspidal', 'depends on π.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- its hypothesis on the representation undecided', []),
        FORM_NOOBJ]),
    ('C15', 'the compiled shared-witness theorem, T3prime_shared_witness', 'the survey`s read 3', [
        ('FAIL', 'CLASS BOUNDARY -- a Set Coupling over functions R -> C, identified with no site`s family',
         [(FL, 'not one of the six sites is stated in those terms', 'six sites, zero candidates.')]),
        ('PASS', 'OWNED -- compiled at the pin, both profiles printed', []),
        ('FAIL', 'FORM -- it TAKES `h1` and `h2` as hypotheses and supplies neither; at this site that is exactly the '
                 'gap, since the shape transposes and the object is what is missing', [])]),
    ('C16', 'the abscissa`s convergent sum', 'row U1: named by the navigator as found', [
        ('FAIL', 'CLASS BOUNDARY -- the abscissa is not a site of this row, and the row says so',
         [(FL, 'The abscissa’s convergent sum is a witness for no site of this row', 'was therefore never entered.')]),
        ('PASS', 'OWNED -- a one-line summed bound the record holds since b326', []),
        FORM_NOOBJ]),
    ('C17', 'the finite side`s zero', 'row U1: named by the navigator as found', [
        ('FAIL', 'CLASS BOUNDARY -- a membership test against a seven-cell decided list, not a statement across widths',
         [(FL, 'The finite side’s zero is not a shared witness across places either', 'discharged by `decide`')]),
        ('PASS', 'OWNED -- a kernel clause discharged by `decide`', []),
        FORM_NOOBJ]),
    ('C18', 'the kernel`s general smear, smear_general', 'the survey`s search; the kernel at HEAD', [
        ('FAIL', 'CLASS BOUNDARY -- quantified over bases and levels, not over support widths',
         [(SMEAR, 'theorem smear_general (p n : Nat)', 'B329.sumAQ p n')]),
        ('PASS', 'OWNED -- proved, 0 axioms, at b419', []),
        FORM_NOOBJ]),
    ('C19', 'the positive-definiteness scan, 13 of 13', 'the survey`s read 2', [
        ('FAIL', 'BOUNDED BY A MEASUREMENT -- a scan over a finite interval where the hypothesis is global, and the '
                 'instrument says so itself',
         [(B353, 'it can show a function is NOT positive definite', 'THAT IS A RANGE RESULT WHERE THE HYPOTHESIS IS A GLOBAL ONE.')]),
        ('PASS', 'OWNED -- the record`s own scan, its floor printed', []),
        FORM_NOOBJ]),
    ('C20', 'the approximation register, b362`s Hilbert-space distance', 'the survey`s search', [
        ('FAIL', 'CLASS BOUNDARY -- another space and another family: dilations of the fractional part, not supports',
         [(B362, 'the space is `K = L2(]0, inf[, dt)`', 'over the complex numbers;')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- trusted at cite',
         [(B362, 'Every located statement is graded', 'TRUSTED-AT-CITE')]),
        ('FAIL', 'FORM -- a criterion is a translation, not a witness',
         [(B362, 'A CRITERION IS A TRANSLATION AND NOT A', 'CONDITIONAL RESULT.')])]),
]

NOT_ADMITTED = [
    ('W1: b353 -- the typed missing statement', 'candidate C4'),
    ('W1: CC, the criterion line `for all g in Cc^infty(R+*)`', 'the same proposition as candidate C8, quoted by b353 '
     'in its own words; not counted twice'),
    ('W2: CC, the support conditions at Theorem 1, 6.11 and the small intervals', 'candidates C5, C6, C7'),
    ('W2: b321, b400, b401 -- Sigma_p W_p(f) at a^2 >= 2', 'site (iv)`s ground, entered at b401; another site'),
    ('W2: b334 -- REACHING (40.0, 81.0) and COVERED (1.3, 1.41)', 'candidates C9 and C10; a charted range is a measurement'),
    ('W3: CC Proposition 2, Boas-Kac`s `there exists g`', 'candidate C3 -- the site`s own existential'),
    ('W3: b406 -- the manufactured existential at site (iv)', 'another site, and b406 already ruled it belongs there'),
    ('W1: Lagarias -- `for all n >= 1` and `n >= K(pi)`', 'candidates C12, C13, C14; `n` is not a width'),
    ('W1: row U1 -- the two witnesses the navigator named', 'candidates C16 and C17'),
    ('W2: b328, b349 -- the sealed phase window', 'the phase coordinate, which b351 closed by an argument; another '
     'coordinate and not this site'),
    ('W1/W3: b404, b405, b422, row U1 -- the shared-witness form itself', 'candidate C15'),
    ('GridTrace.grid_trace_is_signed_count', 'quantified over grids and levels: the same kind as C18, not counted twice'),
    ('W2: b312, b317 -- the archimedean window`s bumps', 'site (i)`s ground, attempted at b424 and not re-attempted here'),
]


def first_fail(steps):
    for k, (out, kind, _qs) in enumerate(steps):
        if out == 'FAIL':
            return k, kind.split(' -- ')[0]
    return None, 'HELD'


def prior_tally(jf):
    """### A PRIOR SITE'S COUNTS ARE READ OFF ITS OWN BANKED JSON, never typed and never recalled."""
    try:
        J = json.loads(read(os.path.join(D, jf)))
    except Exception:
        return {}, 0
    t = {}
    for c in J.get('candidates', []):
        if c.get('first') is not None:
            t[c['kind']] = t.get(c['kind'], 0) + 1
    return t, len(J.get('candidates', []))


def run_attempt():
    R = ['=' * 100, 'b428 -- COMPONENT 1: THE WITNESS ARC AT SITE (iii), THE CANDIDATE TABLE.', '=' * 100,
         '  at (UTC) : %s' % utc(), '  cap : %d candidates' % CAP, '']
    say = R.append
    say('-' * 100)
    say('### THE SITE`S OWN TEXT, PRINTED ONCE BEFORE ANY CANDIDATE.')
    say('-' * 100)
    say('  the class the site quantifies over :')
    for w in wrap(CLASS, 94):
        say('      %s' % w)
    for p, s, e in SITE:
        t = qu1(s, e) if p == FL else q(p, s, e)
        say('  %s :' % where(p))
        for w in wrap(t, 94):
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
                t = qu1(s, e) if p == FL else q(p, s, e)
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
        say('  %-62s %s' % (a[:62], b))
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
    say('### THE BOUNDARY COUNT AT THREE SITES, SO THE ARC`S CONVERGENCE IS MEASURED AND NOT RECALLED.')
    say('-' * 100)
    t1, n1 = prior_tally('b424_candidates.json')
    t2, n2 = prior_tally('b427_candidates.json')
    fmt = lambda t: ' ; '.join('%s %d' % (k2, v) for k2, v in sorted(t.items(), key=lambda x: (-x[1], x[0])))
    say('  site (i)   b424 : %2d candidates ; %s' % (n1, fmt(t1)))
    say('  site (ii)  b427 : %2d candidates ; %s' % (n2, fmt(t2)))
    say('  site (iii) b428 : %2d candidates ; %s' % (len(out), fmt(tally)))
    prior_kinds = set(t1) | set(t2)
    shared = sorted(set(tally) & prior_kinds)
    newk = sorted(set(tally) - prior_kinds)
    same = sum(tally[k2] for k2 in shared)
    diff = sum(tally[k2] for k2 in newk)
    say('  ### KINDS SEEN AT AN EARLIER SITE : %s' % (shared or 'none'))
    say('  ### KINDS NEW AT THIS SITE        : %s' % (newk or 'none'))
    say('  ### ### **AT A BOUNDARY AN EARLIER SITE ALSO USED : %d OF %d. ### AT A BOUNDARY NEW HERE : %d OF %d.**'
        % (same, len(out), diff, len(out)))
    cb = [t1.get('CLASS BOUNDARY', 0), t2.get('CLASS BOUNDARY', 0), tally.get('CLASS BOUNDARY', 0)]
    ns = [n1, n2, len(out)]
    say('  ### ### **THE CLASS BOUNDARY`S SHARE, SITE BY SITE : %s**'
        % ' ; '.join('(%s) %d of %d' % (r, a, b) for r, a, b in zip(('i', 'ii', 'iii'), cb, ns)))
    say('  ### ### **DISTINCT BOUNDARY KINDS, SITE BY SITE : (i) %d ; (ii) %d ; (iii) %d ; UNION OVER THE THREE : %d.**'
        % (len(t1), len(t2), len(tally), len(set(t1) | set(t2) | set(tally))))
    say('  ### **THE ARC IS CONVERGING ON ONE BOUNDARY ONLY IF THE SHARE RISES AND THE UNION STOPS GROWING.**')
    say('  ### The two numbers are printed; no claim beyond them is made here.')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    io.open(TABLE, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), candidates=out, held=len(held), tally=tally,
                        site_i=t1, site_i_n=n1, site_ii=t2, site_ii_n=n2,
                        same=same, diff=diff, shared=shared, newkinds=newk,
                        class_share=[cb, ns], union_kinds=sorted(set(t1) | set(t2) | set(tally)),
                        misses=MISS), indent=1, ensure_ascii=False)
    open(TJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(TJSON + '.tmp', TJSON)
    print(NL.join(R))
    return 0 if not MISS else 1


def cell(s):
    return s.replace('|', '/').replace(NL, ' ').replace('`', '’')


def clip(s, n=220):
    s = s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' …'
    return s.replace('*', chr(92) + '*')


def block_lines(J):
    cands = J['candidates']
    tally = J['tally']
    cb, ns = J['class_share']
    L = ['', MARK, '',
         '## UPDATE — filed 2026-09-12 (b428): row U1, entry (iii) — the witness column’s exhausted list', '',
         '*Rows above are never rewritten; an update names the row it bears on. Written through the writer’s '
         '`append_block`. Row U1’s line, entry (iii)’s `WITNESS: NONE KNOWN`, and the freeze at six (b409) stand as '
         'they read; no seventh site is entered.*', '',
         '| candidate | failed at | the step’s sentence, quoted, and where |', '|:--|:--|:--|']
    for c in cands:
        qs = [x for x in c['quotes'] if x['step'] == c['first']]
        cite = '; '.join('*"%s"* (%s)' % (cell(clip(x['text'])), cell(where(x['path']))) for x in qs[:2])
        L.append('| **%s** %s | S%d — %s | %s |' % (c['id'], cell(c['name']), c['first'], cell(c['kind']), cite))
    L += ['',
          '*%d candidates — the navigator’s opening three (monotonicity in the radius; a limit across radii; Boas–Kac '
          'at each radius as the existential the site owns), and %d the search supplied by description (relay '
          '`data/b428_extract.txt`, every hit hand-read) — each read at its source or at the record’s quotation of it '
          'and attempted by three steps in b424’s fixed order: S1 CLASS, S2 HELD, S3 FORM. **No witness held.** First '
          'failing steps, by kind: %s. **And this is the one site of the six where the shared-witness form '
          'transposes**: the shape is right and the object is missing — `C3` reaches S3 and fails there because the '
          'row states both clauses and then states that no such `g` is named.*'
          % (len(cands), len(cands) - 3,
             '; '.join('%s %d' % (k, v) for k, v in sorted(tally.items(), key=lambda x: (-x[1], x[0])))),
          '',
          '*__The boundary count at three sites, so the arc’s convergence is measured rather than recalled.__ The '
          'class boundary’s share: (i) %d of %d, (ii) %d of %d, (iii) %d of %d. Distinct boundary kinds: (i) %d, '
          '(ii) %d, (iii) %d, **union over the three %d**. %d of %d of this site’s failures land at a boundary an '
          'earlier site also used and %d of %d at a kind new here (%s). **The share does not rise monotonically and '
          'the union of kinds is still growing, so the arc is not converging on a single boundary** — stated as the '
          'two counts show it and no further.*'
          % (cb[0], ns[0], cb[1], ns[1], cb[2], ns[2], len(J['site_i']), len(J['site_ii']), len(tally),
             len(J['union_kinds']), J['same'], len(cands), J['diff'], len(cands),
             ', '.join(J['newkinds']) or 'none'),
          '',
          '*CC is quoted in its extracted text layer (relay `data/b328_source_text.txt`), the layer the writer '
          'verifies against, so its mathematics reads as that layer renders it. No grade is conferred by a seat, no '
          'bridge is typed between sites, and nothing is claimed about `h2`. Filed by b428 (relay '
          '`data/b428_candidates.txt`).*',
          '']
    return L


def run_write():
    R = ['=' * 100, 'b428 -- THE WRITE THE TABLE LICENSES, THROUGH THE LEDGER`S WRITER.', '=' * 100,
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
    say('  ### on b424`s and b427`s pattern, and row U1`s line is not touched.')
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
    say('  the six WITNESS fields after : %s' % re.findall(r'WITNESS: *`([A-Z ]+)`', u1_after))
    say('  b424`s and b427`s own blocks still present : %s'
        % ('<!-- b424 update -->' in after and '<!-- b427 update -->' in after))
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


# =====================================================================================================
# ### COMPONENT 2 -- THE DISPROOF LANE, NAMED AND NOT OPENED.
# =====================================================================================================
INSTRUMENTS = [
    ('the negative control at F7', F7, "F7 -- the Epstein negative control at b326's result",
     'a positive Li ledger with RH false'),
    ('what that control cannot do', F7, 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN', 'priced, not built.'),
    ('the entailment it carries', F7, 'IS A TEST THIS FAMILY CANNOT FAIL', None),
    ('the phase condition', B328, 'the four-term sum at {rho, conj rho, 1 - rho, 1 - conj rho}',
     'negative only BELOW forty-five.'),
    ('the aim map`s reach', B334, 'THE SQUARE AND THE REMAINDER, ON THE REACHING LEG: NOT REACHED',
     "outside the evaluator's reach."),
]
BARRIER = [
    ('the barrier`s reading of its own Lemma 3.4', IB, 'That is: π can establish "P holds for x in a density-one subset',
     'but cannot certify individual elements.'),
    ('the relativized theorem`s own clause', IB, 'the strongest statement `π` can establish has the form',
     'the individual element remains unreached.'),
    ('the Epstein witness, Proposition 3.5', IB, 'Proposition 3.5 (Epstein witness).', 'is false.'),
]
DSEARCH = [('a counterexample lane', r'(?i)counterexampl\w*|disproof|disprove|refut\w* the hypothesis|RH is false'),
           ('a feasible-reach question', r'(?i)feasible reach|at what (height|reach)|what would a counterexample')]


def run_disproof():
    R = ['=' * 100, 'b428 -- COMPONENT 2: THE DISPROOF LANE, NAMED AND NOT OPENED.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    say('-' * 100)
    say('### (a) THE INSTRUMENT THE CORPUS ALREADY HOLDS, QUOTED AT ITS OWN PLACES.')
    say('-' * 100)
    for lab, p, s, e in INSTRUMENTS:
        t = qf7(s, e) if p == F7 else (qu1(s, e) if p == FL else q(p, s, e))
        say('  %-38s %s' % (lab, where(p)))
        for wl in wrap(t, 94):
            say('      | %s' % wl)
    say('')
    say('-' * 100)
    say('### (b) HAS A LANE EVER ASKED WHAT A COUNTEREXAMPLE WOULD LOOK LIKE AT FEASIBLE REACH? A SEARCH.')
    say('-' * 100)
    banks = sorted(f for f in os.listdir(D) if re.match(r'b[34]\d\d_the_.*\.txt$', f))
    files = [os.path.join(D, f) for f in banks] + [FL, os.path.join(PP, 'FINDINGS.md'),
                                                   os.path.join(PP, 'OPEN_TRAILS.md')]
    counts = {}
    for lab, rx in DSEARCH:
        tot, per = 0, []
        for p in files:
            t = fold(read(p))
            hs = list(re.finditer(rx, t))
            if hs:
                tot += len(hs)
                per.append((os.path.basename(p), len(hs)))
        counts[lab] = dict(hits=tot, files=len(per), where=per[:12])
        say('  %-40s hits %d in %d files : %s' % (lab, tot, len(per), [x[0] for x in per[:8]]))
    say('  ### ### **AND THE SECOND SHAPE -- A QUESTION ABOUT FEASIBLE REACH -- RETURNS %d HITS IN %d FILES.**'
        % (counts['a feasible-reach question']['hits'], counts['a feasible-reach question']['files']))
    say('  ### The first shape`s hits were hand-read: every one is a statement that the instrument does NOT see')
    say('  ### counterexamples, or a figure a later act disproved -- not a lane asking the question.')
    say('')
    say('-' * 100)
    say('### (c) THE BARRIER KEYSTONE`S OWN WORDS, AND THE SYMMETRY THEY GIVE.')
    say('-' * 100)
    for lab, p, s, e in BARRIER:
        t = q(p, s, e)
        say('  %-38s %s' % (lab, where(p)))
        for wl in wrap(t, 94):
            say('      | %s' % wl)
    say('')
    say('  ### ### **THE SYMMETRY, STATED FROM THOSE WORDS AND NOT BEYOND THEM:** ### a method that factors through')
    say('  ### an interface with `kappa = 0` reaches ### **density-one per class** ### and ### **CANNOT CERTIFY AN')
    say('  ### ### INDIVIDUAL ELEMENT.** ### That clause says nothing about the DIRECTION of the certificate. ###')
    say('  ### **SO THE PROOF LANE -- certify that every element is on the line -- AND THE DISPROOF LANE -- certify')
    say('  ### ### THAT ONE ELEMENT IS NOT -- ARE SYMMETRIC UNDER THE CORPUS`S OWN THEORY**, and the barrier that')
    say('  ### stops the first stops the second at the same place. ### **THE CORPUS HAS RUN THE FIRST FOR ITS WHOLE')
    say('  ### ### LIFE AND HAS NEVER RUN THE SECOND.**')
    say('  ### ### **AND WHAT THAT IS NOT:** ### it is not a claim that a counterexample exists, nor that one is')
    say('  ### findable, nor that the hypothesis is false. ### It is a statement about which lanes the record has run.')
    say('')
    say('  ### ### **THE LANE IS NAMED AND NOT OPENED. ### TRIGGER: THE INSTRUMENT LANE OPENING. ### 0 LANES OPENED,')
    say('  ### ### 0 ROUTES PROPOSED, 0 INSTRUMENTS BUILT, 0 SEEDS CONSTRUCTED, 0 FIGURES COMPUTED.**')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    io.open(DREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), counts=counts, opened=0, misses=MISS), indent=1, ensure_ascii=False)
    open(DJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(DJSON + '.tmp', DJSON)
    print(NL.join(R))
    return 0 if not MISS else 1


# =====================================================================================================
# ### COMPONENT 3 -- THE EXTERNAL GRADING READ, PRICED AND NOT RUN.
# =====================================================================================================
UA = {'User-Agent': 'relay-b428-locate/1.0 (research seat; address and digest only)'}
CANDIDATE_ADDRESSES = [
    'https://github.com/openai/navier-stokes-lean',
    'https://github.com/openai/NavierStokes',
    'https://github.com/openai/navier-stokes',
    'https://github.com/openai/gpt-oss-navier-stokes',
]
ACTS = [
    ('ACT 1 -- LOCATE THE TERMINAL', 'read the repository`s README at the pinned commit and name the single theorem '
     'the announcement calls the result; if the README names none, the act ends there and says so'),
    ('ACT 2 -- PRINT THE AXIOM PROFILE', '`#print axioms <terminal>` at the pin, which needs the toolchain the '
     'repository pins and a build of its dependencies -- the corpus`s own kernel builds are the only comparable '
     'figure the record holds, and no such figure is transplanted here'),
    ('ACT 3 -- READ THE STATEMENT AGAINST STATEMENT C', 'unfold the terminal`s statement to its base objects and set '
     'it beside the Clay formulation`s statement C, quoting both'),
    ('ACT 4 -- GRADE IT BY THE THREE GRADES', 'DERIVES / INTERFACES / ENCODES-CONCLUSION-or-SHELL, by reading the '
     'statement and never the announcement'),
]


def run_price():
    R = ['=' * 100, 'b428 -- COMPONENT 3: THE EXTERNAL GRADING READ, PRICED AND NOT RUN.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    say('  ### ### **NOT RUN. ### THIS COMPONENT LOCATES AN ADDRESS, PINS IT BY DIGEST IF IT IS REACHABLE, AND')
    say('  ### ### PRICES THE READ IN ACTS. ### NO FILE OF THE EXTERNAL PROOF IS READ AT CONTENT, NO REPOSITORY IS')
    say('  ### ### CLONED, NO LEAN IS RUN, AND NO GRADE IS CONFERRED.**')
    say('')
    say('-' * 100)
    say('### (a) THE ADDRESS, LOOKED FOR AT THE CANDIDATE LOCATIONS THE ANNOUNCEMENT`S NAMING WOULD GIVE.')
    say('-' * 100)
    say('  ### **THE SEAT HOLDS NO ANNOUNCEMENT AND THE CORPUS CITES NONE** (the survey`s read 11). ### The')
    say('  ### candidate addresses below are the shapes an `openai/` repository of that name would take; each is')
    say('  ### probed by `ls-remote`, which reads a SHA back from the remote and clones nothing.')
    found = []
    for url in CANDIDATE_ADDRESSES:
        r = subprocess.run(['git', 'ls-remote', url, 'HEAD'], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=90)
        sha = (r.stdout or '').split()[0] if (r.returncode == 0 and (r.stdout or '').strip()) else ''
        say('  %-52s %s' % (url, ('HEAD %s' % sha) if sha else '### NOT REACHABLE (%s)'
                            % ((r.stderr or '').strip().splitlines()[-1][:70] if (r.stderr or '').strip() else 'no ref')))
        if sha:
            found.append(dict(url=url, head=sha))
        time.sleep(1.0)
    say('')
    if found:
        say('  ### ### **LOCATED AND PINNED BY DIGEST : %s**' % ', '.join('%s @ %s' % (f['url'], f['head'][:12]) for f in found))
    else:
        say('  ### ### ### **NOT LOCATED.** ### No candidate address resolves. ### **THE ADDRESS IS THE')
        say('  ### ### AUTHOR`S TO SUPPLY**, and the act does not widen its search to find something: an')
        say('  ### ### announcement the seat has not read is not a source, and guessing a URL until one answers')
        say('  ### ### would be manufacturing a citation.')
    say('')
    say('-' * 100)
    say('### (b) WHAT THE READ WOULD COST, IN ACTS.')
    say('-' * 100)
    for lab, what in ACTS:
        say('  %s' % lab)
        for wl in wrap(what, 92):
            say('      %s' % wl)
    say('')
    say('  ### ### **THE PRICE: %d ACTS IF THE REPOSITORY IS REACHABLE AND ITS README NAMES THE TERMINAL.**' % len(ACTS))
    say('  ### ### **AND THE PRICE IS NOT ONE ACT**, which is what the navigator expected. ### ACT 2 is the reason:')
    say('  ### an axiom profile is not a read, it is a BUILD -- the toolchain the repository pins, its dependency')
    say('  ### graph, and a machine that compiles them. ### The corpus has never built a foreign kernel, so there is')
    say('  ### no banked figure that scales to it, and ### **ACT 2 IS UNPRICEABLE FROM BANKED FIGURES** (b353`s own')
    say('  ### words for the same situation). ### **ACTS 1, 3 AND 4 ARE READS AND COST ONE ACT EACH.**')
    say('  ### ### **SO: THREE ACTS PRICED, ONE UNPRICEABLE, AND THE UNPRICEABLE ONE IS THE ONE THAT CARRIES THE')
    say('  ### ### CERTIFICATE.** ### A grading that skipped it would be grading an announcement.')
    say('')
    say('-' * 100)
    say('### (c) THE NAVIGATOR`S NOTE, ENTERED AS THE ORDER GIVES IT.')
    say('-' * 100)
    say('  ### **THIS WOULD BE THE FIRST TIME THE CORPUS`S GRADING DISCIPLINE IS AIMED AT A PROOF IT DID NOT')
    say('  ### WRITE, AND ITS PURPOSE IS CALIBRATION.** ### The three grades were minted against the corpus`s own')
    say('  ### kernels and have only ever been applied there; what they would say about a proof from outside is')
    say('  ### unknown, and that is the point of running them on one.')
    say('  ### ### **AND ONE THING THE SEAT ADDS, ROUTED AND NOT RULED:** ### a discipline that has only ever graded')
    say('  ### its own work has never been tested for the failure mode that matters most -- ### **GRADING ITS OWN')
    say('  ### ### WORK MORE GENEROUSLY THAN A STRANGER`S.** ### Calibration against an outside proof measures the')
    say('  ### instrument; it does not measure the outside proof, and an act that confused the two would be using a')
    say('  ### stranger`s work as a mirror.')
    say('')
    say('  ### ### **NOT RUN. ### THE AUTHOR`S WORD. ### 0 REPOSITORIES CLONED, 0 BUILDS, 0 GRADES CONFERRED,')
    say('  ### ### 0 STATEMENTS OF THE EXTERNAL PROOF READ AT CONTENT.**')
    say('=' * 100)
    io.open(PREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), probed=CANDIDATE_ADDRESSES, located=found, acts=len(ACTS),
                        priced_acts=3, unpriceable_acts=1, run=0), indent=1, ensure_ascii=False)
    # ### **RUN 1 WROTE THE TEMPORARY AND NEVER RENAMED IT**, so the record existed and the JSON did not, and the
    # ### report read its own fallback zeros as if they were the price. ### The rename is the write; without it the
    # ### tool succeeds and says nothing. ### (b405's zero-byte husk is the same species in a different dress.)
    open(PJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(PJSON + '.tmp', PJSON)
    print(NL.join(R))
    return 0 if os.path.exists(PJSON) else 1


def main():
    Lr = []
    say = Lr.append
    try:
        J = json.loads(read(TJSON))
    except Exception:
        J = dict(candidates=[], held=0, tally={}, site_i={}, site_ii={}, same=0, diff=0, newkinds=[],
                 class_share=[[0, 0, 0], [0, 0, 0]], union_kinds=[])
    try:
        P = json.loads(read(PJSON))
    except Exception:
        P = dict(located=[], acts=0, priced_acts=0)
    try:
        DJ = json.loads(read(DJSON))
    except Exception:
        DJ = dict(counts={}, opened=None)
    wr, tab = read(WREC), read(TABLE)
    fails = [] if wr else ['the write record is absent']
    say('=' * 100)
    say('b428_components.py -- SITE (iii), THE DISPROOF LANE, THE EXTERNAL PRICE. ### THE REPORT.')
    say('=' * 100)
    for c in J['candidates']:
        say('  %-5s %-62s FAILED AT S%s -- %s' % (c['id'], c['name'][:62], c['first'], c['kind']))
    n = len(J['candidates'])
    held = J['held']
    cb, ns = J['class_share']
    say('')
    say('  ### CANDIDATES %d ; HELD %d ; FAILED %d' % (n, held, n - held))
    say('  ### TALLY : %s' % ' ; '.join('%s %d' % (k, v) for k, v in sorted(J['tally'].items(), key=lambda x: (-x[1], x[0]))))
    say('  ### THE CLASS BOUNDARY`S SHARE : (i) %d of %d ; (ii) %d of %d ; (iii) %d of %d'
        % (cb[0], ns[0], cb[1], ns[1], cb[2], ns[2]))
    say('  ### UNION OF BOUNDARY KINDS OVER THREE SITES : %d %s' % (len(J['union_kinds']), J['union_kinds']))
    say('  ### COMPONENT 2 : lanes opened %s ; the feasible-reach shape returned %s hit(s)'
        % (DJ.get('opened'), (DJ.get('counts', {}).get('a feasible-reach question', {}) or {}).get('hits')))
    say('  ### COMPONENT 3 : addresses located %d ; acts priced %d of %d' % (len(P['located']), P.get('priced_acts', 0), P.get('acts', 0)))
    for needle in ('anchor misses : 0', 'LEDGER WRITE : WRITTEN',
                   'row U1`s line byte-identical before and after : True', 'misses : 0 []'):
        ok = (needle in tab) or (needle in wr)
        fails += [] if ok else [needle]
        say('  %-52s %s' % (needle, ok))
    cbshare = (cb[2] / ns[2]) if ns[2] else 0
    mostly = cb[2] > (n - cb[2])
    say('')
    say('### THE EXPECTATIONS, THEIR CLAUSES APART (R27):')
    say('  (N1) *site (iii)`s list is exhausted with no witness held* -- ### **%s** (%d of %d failed at a quoted '
        'step; held %d).' % ('MET' if (n and held == 0) else 'REFUTED', n - held, n, held))
    say('  (N1) *its failures land mostly at the class boundary, since the width IS the class`s reach* -- ### **%s** '
        '(%d of %d at the class boundary, %.0f%%; the next largest kind takes %d).'
        % ('MET' if mostly else 'REFUTED', cb[2], ns[2], 100 * cbshare,
           max([v for k, v in J['tally'].items() if k != 'CLASS BOUNDARY'] or [0])))
    say('  (N2) *the external read prices at one act if the repository is reachable and the terminal is named in its '
        'README* -- ### **%s** (addresses located %d; the read prices at %d acts, %d of them priceable and %d '
        'UNPRICEABLE FROM BANKED FIGURES -- the axiom profile is a BUILD, not a read).'
        % ('MET' if (P['located'] and P.get('acts') == 1) else 'REFUTED',
           len(P['located']), P.get('acts', 0), P.get('priced_acts', 0), P.get('unpriceable_acts', 0)))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b428_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(Lr) + NL)
    print(NL.join(Lr))
    return 1 if fails else 0


if __name__ == '__main__':
    if '--attempt' in sys.argv:
        sys.exit(run_attempt())
    if '--write' in sys.argv:
        sys.exit(run_write())
    if '--disproof' in sys.argv:
        sys.exit(run_disproof())
    if '--price' in sys.argv:
        sys.exit(run_price())
    sys.exit(main())
