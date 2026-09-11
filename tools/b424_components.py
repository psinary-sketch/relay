# -*- coding: utf-8 -*-
"""b424_components.py -- THE WITNESS ARC AT SITE (i): THE CANDIDATE TABLE, AND THE WRITE IT LICENSES.

### ### **EACH CANDIDATE IS READ AT ITS SOURCE OR AT THE RECORD'S QUOTATION OF IT AND ATTEMPTED BY THREE STEPS IN
### THE ORDER THE LOCKED FACE FIXES -- S1 CLASS, S2 HELD, S3 FORM -- AND IS FAILED AT THE FIRST STEP IT FAILS,
### THAT STEP'S SENTENCE QUOTED.** ### The cap: no computation, no construction, no search beyond the survey's.
###   --attempt   the table: data/b424_candidates.txt and data/b424_candidates.json.
###   --write     the write the table licenses, through the ledger's writer: data/b424_ledger_write.txt.
###   (no flag)   the report and the expectation, its three clauses apart.
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
FL = os.path.join(PP, 'FACES_LEDGER.md')
CC = os.path.join(D, 'b328_source_text.txt')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
B400C = os.path.join(D, 'b400_closing.txt')
B401C = os.path.join(D, 'b401_closing.txt')
B353 = os.path.join(D, 'b353_the_missing_statement.txt')
B362 = os.path.join(D, 'b362_the_approximation_register.txt')
B406 = os.path.join(D, 'b406_the_sites_without_an_existential.txt')
B312 = os.path.join(D, 'b312_the_remainder.txt')
B398 = os.path.join(D, 'b398_the_li_weil_bridge.txt')
B399 = os.path.join(D, 'b399_the_sign_and_the_refutation.txt')
B332 = os.path.join(D, 'b332_the_clause_stated.txt')
T3PIN = 'SIDE-lv-conservation@93c27ec:SIDELvConservation/T3_StepNineBridge.lean'
TABLE = os.path.join(D, 'b424_candidates.txt')
TJSON = os.path.join(D, 'b424_candidates.json')
WREC = os.path.join(D, 'b424_ledger_write.txt')
MARK = '<!-- b424 update -->'
NL = chr(10)
MISS = []

SHORT = {CC: 'CC 2006.13771v1 (relay data/b328_source_text.txt)', LAG: 'Lagarias math/0404394v4 (relay data/b358_source_lagarias0404394.txt)',
         FL: 'FACES_LEDGER.md row U1', T3PIN: 'SIDE-lv-conservation v0.10.0'}


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


# ### THE SITE'S OWN TEXT, PRINTED ONCE BEFORE ANY CANDIDATE -- reading (1).
SITE = [(FL, 'the witness form does not transpose here at all', 'THE RIGHT KIND OF THING TO LOOK FOR HERE.'),
        (B406, 'SO `b405`’S CELLS STAND AND ITS REASON GAINS ONE CLAUSE', 'THE SHARED-WITNESS FORM CAN REPAIR')]
FORM = ('FAIL', 'FORM -- no one object meets both clauses here: the site carries no inner existential the shared-witness '
        'form can repair (the site`s own text, above)', [])
CLASS = 'C_c^inf(R*_+) with the transform vanishing on F -- Proposition C.1`s class'

# ### (id, name, origin, [S1, S2, S3]); each step (outcome, kind -- the reason, [(path, start, end), ...]).
CANDS = [
    ('C1', 'the lawful-class bound as a witness on the wrong class', 'b422`s list', [
        ('FAIL', 'CLASS BOUNDARY -- support inside [2^-1/2, 2^1/2], chosen so that no prime enters',
         [(CC, 'In this paper we consider the simplest instance of this', 'so that rational primes are not involved'),
          (B400C, 'THEOREM 1 CARRIES A SUPPORT HYPOTHESIS AND PROPOSITION C.1', 'CARRIES NONE')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- the source`s theorem, graded by b400',
         [(B400C, '`C-I` THE CLASS IS PRIME-FREE BY DESIGN', 'IMPORT-UNDER-THE-BAR.')]),
        FORM]),
    ('C2', 'the wide-support bound confirmed absent', 'b422`s list', [
        ('FAIL', 'CLASS BOUNDARY -- as described, a statement at one support with a^2 >= 2',
         [(B400C, 'THE QUESTION.** ### At a support with', 'not identically zero:')]),
        ('FAIL', 'ABSENT -- five matcher shapes over the corpus and both sources found none',
         [(B401C, 'NOTHING EVALUATES OR', 'or in the corpus.')]),
        FORM]),
    ('C3', 'exhaustion at each radius not across', 'b422`s list', [
        ('FAIL', 'CLASS BOUNDARY -- one support width at a time, while the class is the union over widths; and the '
                 'existential it carries belongs to site (iii)',
         [(B353, 'There exists g in Cc^infty(R)', 'f = g * g^*'),
          (B353, 'SO: AN EXHAUSTION AT EVERY WIDTH', 'ACROSS WIDTHS.'),
          (B406, 'THAT EXISTENTIAL IS REAL AND IT BELONGS TO SITE', 'counted one existential twice.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- Boas-Kac, trusted at cite',
         [(B353, 'Boas-Kac internally means proving a factorisation theorem.', None)]),
        FORM]),
    ('C4', 'the approximation register closed', 'b422`s list', [
        ('FAIL', 'CLASS BOUNDARY -- another space and family: a Hilbert-space distance over dilations of the fractional part',
         [(B362, 'the space is `K = L2(]0, inf[, dt)`', 'over the complex numbers;')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- trusted at cite', [(B362, 'Every located statement is graded', 'TRUSTED-AT-CITE')]),
        ('FAIL', 'FORM -- a criterion is a translation, not a witness',
         [(B362, 'A CRITERION IS A TRANSLATION AND NOT A', 'CONDITIONAL RESULT.')])]),
    ('C5', 'CC`s Theorem 6.11', 'the survey`s search: CC line 3630; the record at b306', [
        ('FAIL', 'CLASS BOUNDARY -- support inside [2^-1/2, 2^1/2]',
         [(CC, 'Theorem 6.11 LetgPC8', 'with support in the interval r2´1{2, 21{2s')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- a theorem of the verified source, not derived in the record', []),
        FORM]),
    ('C6', 'CC`s positivity for small enough intervals', 'the survey`s search: CC lines 291 and 1789', [
        ('FAIL', 'CLASS BOUNDARY -- small enough intervals only',
         [(CC, 'As a preliminary test we prove, using a simple estimate', 'the positivity holds.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- a statement of the verified source', []),
        FORM]),
    ('C7', 'CC`s Theorem 4.7 identity with its positive trace term', 'the survey`s search: b312, b317, b321, b304', [
        ('PASS', 'stated for every f in the class, with no support condition',
         [(B312, 'Tr(theta(f) S) = W_inf(f) + INT f(rho^-1) eps(rho) d*rho', 'for every `f in C_c^infinity(R*_+)`')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- graded with the margin it fixes, measured only at covered cells',
         [(B400C, '`C-II` THE MARGIN IS MINUS THE REMAINDER INTEGRAL', 'IMPORT-UNDER-THE-BAR.')]),
        ('FAIL', 'FORM -- the positive term is the trace; what separates it from the site`s quantity is a remainder '
                 'integral with no sign across the class', [(B400C, '`C-II` THE MARGIN IS MINUS THE REMAINDER INTEGRAL', 'EQUALITY.')])]),
    ('C8', 'Proposition C.1, the clause itself', 'the survey`s search: b328, b332, b353, row S1, FINDINGS', [
        ('PASS', 'it states the class', [(CC, 'Proposition C.1 Let Z Ă C be the set of non-trivial zeros', '@zPF. (155)')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- page index 51 of the verified artefact',
         [(B400C, 'Proposition C.1 AVAILABLE at the window', 'page index 51')]),
        ('FAIL', 'FORM -- it is the universal quantifier itself, not an object serving it',
         [(B332, 'the quantifiers -- over the class, infinite, and through the explicit formula over', 'they are the clause.')])]),
    ('C9', '(M), typed at b398', 'the survey`s search: b398, b399', [
        ('PASS', 'typed over the source`s class', [(B398, '(M)** ### For every `g` in the source`s class', 'g~(1) = 0`')]),
        ('FAIL', 'REFUTED -- by a printed value at every banked lawful seed',
         [(B399, '(M) IS REFUTED.', 'AT EVERY BANKED LAWFUL SEED.')]),
        FORM]),
    ('C10', 'Lagarias`s Weil scalar product, positive under the hypothesis', 'the survey`s search: Lagarias line 726', [
        ('FAIL', 'CLASS BOUNDARY -- Lagarias`s test function vector space A, for each cuspidal representation, not stated '
                 'as the site`s class',
         [(LAG, 'The Riemann hypothesis for Λ( s,π ) implies that the Weil scalar product', 'test function vector space A.')]),
        ('FAIL', 'CONDITIONAL ON THE HYPOTHESIS -- the same sentence opens with it', []),
        FORM]),
    ('C11', 'Lagarias`s Theorem 2.2, Li`s criterion', 'the survey`s reads: Lagarias line 621', [
        ('FAIL', 'CLASS BOUNDARY -- the Li coefficients, indexed by n >= 1',
         [(LAG, 'Theorem 2.2. Letπ be an irreducible cuspidal', '(2.20)')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- an equivalence of the verified source', []),
        FORM]),
    ('C12', 'Lagarias`s Theorem 5.1', 'the survey`s reads: Lagarias line 1207; row U1 (v)', [
        ('FAIL', 'CLASS BOUNDARY -- the archimedean term on the Li family',
         [(LAG, 'Theorem 5.1. For any irreducible cuspidal', '(5.1)'),
          (FL, 'Theorem 5.1’s absolute constant is a witness for the ARCHIMEDEAN side', 'and not for this one.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- graded at b358', []),
        FORM]),
    ('C13', 'Lagarias`s Theorem 6.1', 'the survey`s reads: Lagarias line 1994', [
        ('FAIL', 'CLASS BOUNDARY -- the finite-place term on the Li family',
         [(LAG, 'Theorem 6.1. For any irreducible cuspidal', 'depends on π.')]),
        ('FAIL', 'IMPORT UNDER THE BAR -- its hypothesis on the representation undecided',
         [(B401C, 'HYPOTHESIS QUANTIFYING OVER THE REPRESENTATION', 'NOT DECIDED HERE EITHER.')]),
        FORM]),
    ('C14', 'the compiled shared-witness theorem, T3prime_shared_witness', 'the survey`s search: b404, b405, row U1, b422', [
        ('FAIL', 'CLASS BOUNDARY -- a Set Coupling over functions R -> C, identified with no site`s family',
         [(FL, 'not one of the six sites is stated in those terms', 'six sites, zero candidates.')]),
        ('PASS', 'OWNED -- compiled at the pin, both profiles printed', [(FL, 'Both profiles printed at the pin', 'at neither terminal.')]),
        ('FAIL', 'FORM -- it takes h1 and h2 as hypotheses and supplies neither',
         [(T3PIN, 'the hypotheses `h1, h2` name the extra information that', 'Determination supplies.')])]),
    ('C15', 'the abscissa`s convergent sum', 'row U1: named by the navigator as found', [
        ('FAIL', 'CLASS BOUNDARY -- a coordinate that closed, never a site of the row',
         [(FL, 'The abscissa’s convergent sum is a witness for no site of this row', 'never entered.')]),
        ('PASS', 'OWNED -- the coordinate closed at b326', []),
        FORM]),
    ('C16', 'the finite side`s zero', 'row U1: named by the navigator as found', [
        ('FAIL', 'CLASS BOUNDARY -- a seven-cell decided list, not the class',
         [(FL, 'The finite side’s zero is not a shared witness across places either', 'discharged by `decide`')]),
        ('PASS', 'OWNED -- a kernel clause discharged by decide', []),
        FORM]),
]

# ### READ AND NOT ADMITTED -- every hit of the survey's search that is not a candidate, with its reason.
NOT_ADMITTED = [
    ('CC lines 101, 134', 'Weil`s inequality on (1/2, 2): candidate C1'),
    ('CC line 1318', 'Boas-Kac on R*_+ at one symmetric interval: candidate C3'),
    ('CC line 1789', 'the estimate at a support [-s, s]: candidate C6'),
    ('CC lines 1512, 1769', 'definitions -- of a positive functional, and of positive definite'),
    ('CC line 3891', 'a decay lemma on the derivatives of g'),
    ('Lagarias line 726', 'candidate C10'),
    ('Lagarias line 2928', 'a definition -- the Weil distribution well-defined'),
    ('W1: b303, b309, FINDINGS', 'other objects -- a document`s own claim, the scaling regime, an old prediction'),
    ('W1: b404, b405, b422, row U1', 'the shared-witness form itself: candidate C14'),
    ('W1/W3: b406', 'the manufactured existential of site (iv) -- another site'),
    ('W2: b305', 'the definition of W_v'),
    ('W2: b306', 'candidate C5'),
    ('W2: b312, b317, b321; W3: b304', 'candidate C7'),
    ('W2: b324', 'a functional`s limit over L-functions -- another family'),
    ('W2: b328, b332, b353, row S1, FINDINGS', 'the clause itself: candidate C8'),
    ('W2: b398, b399', 'candidate C9'),
    ('W3: b340', 'a must-not-hit query phrase'),
    ('W3: b358', 'the Li-family asymptotics: candidates C12, C13'),
    ('SmearGeneral.smear_general, GridTrace.grid_trace_is_signed_count', 'quantified over bases, levels and grids, not '
     'over the test functions -- outside the description'),
]


def first_fail(steps):
    for k, (out, kind, _qs) in enumerate(steps):
        if out == 'FAIL':
            return k, kind.split(' -- ')[0]
    return None, 'HELD'


def run_attempt():
    R = ['=' * 100, 'b424 -- THE WITNESS ARC AT SITE (i): THE CANDIDATE TABLE.', '=' * 100, '  at (UTC) : %s' % utc(), '']
    say = R.append
    say('-' * 100)
    say('### THE SITE`S OWN TEXT, PRINTED ONCE BEFORE ANY CANDIDATE.')
    say('-' * 100)
    say('  the class the site quantifies over : %s' % CLASS)
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
    say('  ### CANDIDATES %d ; FAILED %d ; HELD %d' % (len(out), len(out) - len(held), len(held)))
    say('  ### TALLY BY FIRST FAILING STEP : %s' % ' ; '.join('%s %d' % (k2, v) for k2, v in sorted(tally.items(), key=lambda x: -x[1])))
    say('  ### FAILED AT S1 : %d ; AT S2 : %d ; AT S3 : %d' % tuple(sum(1 for c in out if c['first'] == s) for s in (1, 2, 3)))
    say('  ### SITES ATTEMPTED : 1 ; CHECKPOINT : after site (i) ; no second site in this act')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    io.open(TABLE, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), candidates=out, held=len(held), tally=tally, misses=MISS), indent=1, ensure_ascii=False)
    open(TJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(TJSON + '.tmp', TJSON)
    print(NL.join(R))
    return 0 if not MISS else 1


def cell(s):
    """### Corpus prose: no pipe, no newline, and an apostrophe is a curly one, never a backtick (b422's lesson)."""
    return s.replace('|', '/').replace(NL, ' ').replace('`', '’')


def clip(s, n=220):
    """### A quotation is cut at a word boundary with an ellipsis, never mid-word; an asterisk is ESCAPED, never
    ### dropped -- run 2 dropped one and turned `ballQ p n * sumAN p n` into a different expression."""
    s = s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' …'
    return s.replace('*', chr(92) + '*')


def block_lines(cands):
    L = ['', MARK, '',
         '## UPDATE — filed 2026-09-11 (b424): row U1, entry (i) — the witness column’s exhausted list', '',
         '*Rows above are never rewritten; an update names the row it bears on. Written through the writer’s '
         '`append_block`. Row U1’s line, entry (i)’s `WITNESS: UNSTATED`, and the freeze at six (b409) stand as they '
         'read; no seventh site is entered.*', '',
         '| candidate | failed at | the step’s sentence, quoted, and where |', '|:--|:--|:--|']
    for c in cands:
        qs = [x for x in c['quotes'] if x['step'] == c['first']]
        cite = '; '.join('*"%s"* (%s)' % (cell(clip(x['text'])), cell(where(x['path']))) for x in qs[:2])
        L.append('| **%s** %s | S%d — %s | %s |' % (c['id'], cell(c['name']), c['first'], cell(c['kind']), cite))
    tally = {}
    for c in cands:
        tally[c['kind']] = tally.get(c['kind'], 0) + 1
    L += ['',
          '*Sixteen candidates — b422’s four, and twelve the search supplied by description (relay '
          '`data/b424_extract.txt`, every hit hand-read) — each read at its source or at the record’s quotation of it '
          'and attempted by three steps in a fixed order: S1 CLASS, S2 HELD, S3 FORM. **No witness held.** First '
          'failing steps: %s. The site’s own cell was quoted before any candidate and stands: the witness form does '
          'not transpose at (i), where the quantifiers are a `∀` with no `∃` inside; every candidate fails S3 as well. '
          'CC is quoted in its extracted text layer (relay `data/b328_source_text.txt`), the layer the writer verifies '
          'against, so its mathematics reads as that layer renders it. No grade is conferred by a seat, no bridge is typed between sites, and nothing is claimed about `h2`. Filed '
          'by b424 (relay `data/b424_candidates.txt`).*' % '; '.join('%s %d' % (k, v) for k, v in sorted(tally.items(), key=lambda x: -x[1])),
          '']
    return L


def run_write():
    R = ['=' * 100, 'b424 -- THE WRITE THE TABLE LICENSES, THROUGH THE LEDGER`S WRITER.', '=' * 100, '  at (UTC) : %s' % utc()]
    say = R.append
    try:
        T = json.loads(io.open(TJSON, encoding='utf-8').read())
    except Exception as exc:
        say('  ### REFUSED: the table is not banked (%s).' % exc)
        io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
        return 1
    cands = T['candidates']
    before = read(FL)
    u1_before = next((x for x in before.splitlines() if x.startswith('| U1 ')), '')
    say('  candidates %d ; held %d' % (len(cands), T['held']))
    if T['held']:
        say('  ### A CANDIDATE HOLDS -- THIS TOOL DOES NOT WRITE THE WITNESS FIELD; THE ACT STOPS FOR THE WRITER`S ROW PATH.')
        io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
        return 1
    triples = [(x['path'], x['start'], True) for c in cands for x in c['quotes'] if x['step'] == c['first']]
    miss = W.verify_quotes(triples)
    say('  quotations at the first failing steps, verified by the writer`s verify_quotes : %d ; misses : %d %s'
        % (len(triples), len(miss), miss))
    if miss:
        say('  ### REFUSED: a quotation is not in its file. NOTHING WRITTEN.')
        io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
        return 1
    st, det = W.append_block(MARK, block_lines(cands))
    after = read(FL)
    u1_after = next((x for x in after.splitlines() if x.startswith('| U1 ')), '')
    say('  append_block : %s -- %s' % (st, det))
    say('  row U1`s line byte-identical before and after : %s' % (u1_before == u1_after and bool(u1_after)))
    say('  entry (i)`s WITNESS field after : %s' % (re.findall(r'WITNESS: *`([A-Z ]+)`', u1_after)[:1]))
    say('  the prior ledger a true prefix : %s' % after.startswith(before.rstrip(NL)))
    say('  ### ### **LEDGER WRITE : %s**' % st)
    say('')
    say('### THE BLOCK, AS WRITTEN:')
    R += ['  | %s' % x for x in block_lines(cands)]
    say('=' * 100)
    io.open(WREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    print(NL.join(R[:12]))
    return 0 if st == 'WRITTEN' else 1


def main():
    L = []
    say = L.append
    tab, wr = read(TABLE), read(WREC)
    fails = [nm for nm, t in (('table', tab), ('write', wr)) if not t]
    try:
        T = json.loads(read(TJSON))
    except Exception:
        T = dict(candidates=[], held=-1, tally={})
    say('=' * 100)
    say('b424_components.py -- THE WITNESS ARC AT SITE (i), THE REPORT.')
    say('=' * 100)
    cands = T['candidates']
    for c in cands:
        say('  [%-3s] %-62s %s' % (c['id'], c['name'][:62], ('FAILED AT S%d -- %s' % (c['first'], c['kind'])) if c['first'] else 'HELD'))
    for needle in ('LEDGER WRITE : WRITTEN', 'row U1`s line byte-identical before and after : True', 'misses : 0 []'):
        ok = needle in wr
        fails += [] if ok else [needle]
        say('  %-64s %s' % (needle, ok))
    kinds = set(c['kind'] for c in cands if c['first'])
    other = sorted(set(k for k in kinds if k not in ('CLASS BOUNDARY', 'IMPORT UNDER THE BAR')))
    say('')
    say('### THE EXPECTATION, ITS CLAUSES APART (R27):')
    say('  (L2) *site (i)`s list exhausted* -- ### **%s** (%d of %d failed at a quoted step).'
        % ('MET' if cands and all(c['first'] for c in cands) else 'REFUTED', sum(1 for c in cands if c['first']), len(cands)))
    say('  (L2) *no witness held* -- ### **%s** (held %d).' % ('MET' if T['held'] == 0 else 'REFUTED', T['held']))
    bad = [c['id'] for c in cands if c['first'] and c['kind'] not in ('CLASS BOUNDARY', 'IMPORT UNDER THE BAR')]
    say('  (L2) *every failure at a named import or a named class boundary* -- ### **%s** (%d of %d; the other kind%s: %s at %s).'
        % ('MET' if not bad else 'REFUTED', len(cands) - len(bad), len(cands), '' if len(other) == 1 else 's',
           ', '.join(other) or 'none', ', '.join(bad) or '-'))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b424_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    if '--attempt' in sys.argv:
        sys.exit(run_attempt())
    if '--write' in sys.argv:
        sys.exit(run_write())
    sys.exit(main())
