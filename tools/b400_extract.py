# -*- coding: utf-8 -*-
"""b400_extract.py -- THE SURVEY THE FACE IS WRITTEN FROM. ### **A READ, AND NOTHING ELSE.**

### ### **WHAT THIS ACT IS.** ### `b399` refuted `(M)` -- the one relation the record held between
### the compressed square on the Sonin family and the finite-place channel on the Li family -- and
### refused to name a replacement, because naming one was not in its order. ### **THIS ACT'S ORDER
### ### IS EXACTLY THAT**, and the ferry adds two constraints and a fourth verdict.

### ### **THE ORDER OF THIS FILE IS THE ORDER'S OWN.** ### The two pinned sources are acquired and
### verified against the corpus's banked digests ### BEFORE A WORD OF EITHER IS READ (`b399`'s
### Addition Two, carried into this ferry's head by name); then the constraint set is assembled from
### the acts that own each constraint, by the anchor tool, at a file and a line; then the window;
### then Component 3's population.

### ### **WHAT COMPUTES HERE AND WHAT DOES NOT.** ### No instrument is run, no kernel is built, no
### object is recomputed. ### The one arithmetic this file performs is `PRIME POWERS IN A CLOSED
### INTERVAL`, on the record's own `a`-grid -- and it is performed ### **SO THAT A BANKED LIST CAN
### ### BE CHECKED AGAINST A ROUTE THAT SHARES NO CODE WITH IT**, not so that a new number can be
### banked. ### Both routes are printed side by side and a disagreement would be a hit.

### ### **THE DEAFNESSES, IN THE INSTRUMENT.** ### (1) It cannot tell a correct quotation from an
### invented one; it fails loudly when a fragment is not where it is claimed to be, and that is all.
### (2) The PDF flattener strips punctuation and case, so a SIGN read through it is read from its
### surrounding sentence and never from its glyphs. ### (3) Where two acts print different columns
### for one name it prints BOTH and chooses neither.
"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import b305_source as S5        # noqa: E402  ### the flattener is IMPORTED, never copied
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FL = os.path.join(PP, 'FACES_LEDGER.md')
FI = os.path.join(PP, 'FINDINGS.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')

CC_SHA = 'b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726935b58e0'
CC_BYTES = 1213504
LG_SHA = '86f3d3c49f5a889f121bb1f04f67694cb9066dc8360f6988165788679594a4a7'
LG_BYTES = 423379
SEARCH_ROOTS = [os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects'),
                os.path.join('C:', os.sep, 'Users', 'ECHOCH~1', 'AppData', 'Local', 'Temp',
                             'claude')]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=240):
    return ' '.join(s.split())[:n]


READS = []
SRCREADS = []
FIG = {}


def q(path, hint, label, n=320, span=False):
    """### **EVERY QUOTATION IS PULLED BY THE ANCHOR TOOL FROM THE FILE THAT EMITTED IT.**"""
    i, ln, v = 0, '', 'ABSENT'
    if span:
        try:
            i, runs = AF.find_span(path, hint)
            ln = ' '.join(' '.join(r.split()) for r in runs)
            v = 'ANCHORED-SPAN'
        except Exception as e:
            v = 'AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT'
    else:
        try:
            i, ln = AF.find(path, hint)
            v = 'ANCHORED'
        except Exception as e:
            v = 'AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT'
    READS.append(dict(path=os.path.basename(path), label=flat(label, 160), line=i, verdict=v,
                      text=flat(ln, 900)))
    rec('    %s  ### `%s:%s`' % (label, os.path.basename(path), i or '--'))
    if v.startswith('ANCHORED'):
        rec('      > %s' % flat(ln, n))
    else:
        rec('      ### **%s** -- the hint matched %s' % (v, 'many lines' if v == 'AMBIGUOUS'
                                                         else 'nothing'))
    return i, ln


# ==================================================================================================
#  (0) THE SOURCES, BEFORE ANY QUOTATION.
# ==================================================================================================
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def acquire(want_sha, want_bytes):
    hits, scanned = [], 0
    for r in SEARCH_ROOTS:
        for dp, _dn, fn in os.walk(r):
            for f in fn:
                p = os.path.join(dp, f)
                try:
                    if os.path.getsize(p) != want_bytes:
                        continue
                except OSError:
                    continue
                scanned += 1
                try:
                    if sha256_file(p) == want_sha:
                        hits.append(p)
                except OSError:
                    continue
    return hits, scanned


def survey0():
    bar('=')
    rec('  ### (0) THE SOURCES, ACQUIRED AND VERIFIED BEFORE A WORD IS READ.')
    bar('=')
    rec('  ### The ferry carries `b399`s Addition Two by name -- *the two pinned sources verified')
    rec('  ### against their banked digests before any quotation, as b399 did.* ### **A DERIVATION')
    rec('  ### ### QUOTED FROM AN UNVERIFIED COPY IS NOT A DERIVATION**, and this act reads no')
    rec('  ### source sentence until the artefact carrying it has matched the corpus`s pin.')
    rec()
    out = {}
    for key, sha, nby, cite in [
            ('CC', CC_SHA, CC_BYTES,
             'Connes & Consani, "Weil positivity and Trace formula the archimedean place", '
             'arXiv:2006.13771v1'),
            ('LG', LG_SHA, LG_BYTES,
             'J. C. Lagarias, "Li coefficients for automorphic L-functions", arXiv:math/0404394v4')]:
        hits, scanned = acquire(sha, nby)
        rec('  ### **%s** -- %s' % (key, cite))
        rec('      banked pin        : %d bytes, sha256 `%s`' % (nby, sha))
        rec('      files of that size examined by digest : %d' % scanned)
        rec('      byte-identical copies located         : %d' % len(hits))
        if hits:
            got = sha256_file(hits[0])
            rec('      re-computed digest : `%s`' % got)
            rec('      ### ### **VERDICT : VERIFIED.** ### `got == banked : %s`' % (got == sha))
            out[key] = hits[0]
        else:
            rec('      ### ### **VERDICT : HALT.** ### No copy on this machine matches the pin,')
            rec('      ### ### and no word of this source is read.')
            out[key] = None
        rec()
    FIG['sources'] = {k: bool(v) for k, v in out.items()}
    return out


def pdf_pages(p):
    from pypdf import PdfReader
    r = PdfReader(p)
    return [S5.flatten(pg.extract_text() or '') for pg in r.pages]


def qsrc(pages, needle, label, after=520, page=None):
    """### **A SOURCE FRAGMENT IS LOCATED BY PAGE INDEX AND ITS SURROUNDING SENTENCE PRINTED.**"""
    nn = S5.flatten(needle)
    found = []
    for i, t in enumerate(pages, 1):
        if page and i != page:
            continue
        j = t.find(nn)
        if j >= 0:
            found.append((i, t[j:j + after]))
    SRCREADS.append(dict(label=flat(label, 160), needle=nn[:90],
                         pages=[i for i, _ in found]))
    rec('    %s' % label)
    if found:
        i, txt = found[0]
        rec('      ### page index `%d` -- %d hit(s) : %s' % (i, len(found), [x for x, _ in found]))
        rec('      > %s' % txt[:after])
    else:
        rec('      ### **NOT LOCATED IN THE VERIFIED ARTEFACT** -- and nothing is quoted from it.')
    rec()
    return found


# ==================================================================================================
#  (1) THE CONSTRAINT SET, FROM THE ACTS THAT OWN EACH CONSTRAINT.
# ==================================================================================================
def survey1():
    bar('=')
    rec('  ### (1) THE CONSTRAINT SET -- WHAT `b399` LEFT STANDING, EACH CONSTRAINT AT A LINE.')
    bar('=')
    rec('  ### **THE FERRY ENTERS ONE CONSTRAINT BY ORDER AND PLACES IT FIRST**, so it is `C-I`;')
    rec('  ### the rest are the draft`s Component 1 as it states them. ### **NO CONSTRAINT IS TAKEN')
    rec('  ### ### FROM THE NAVIGATOR: each is quoted from the act that owns it.**')
    rec()
    rec('  --- **C-I. THE CLASS IS PRIME-FREE BY DESIGN** (the ferry`s Addition One) ---')
    q(os.path.join(D, 'b306_the_difference.txt'), 'RATIONAL PRIMES ARE NOT INVOLVED',
      '### the SOURCE`s own sentence, as `b306` carried it', 300)
    q(os.path.join(D, 'b306_the_difference.txt'), 'SO EVERY TERM OF (149)',
      '### and the MECHANISM, which is arithmetic and not a measurement', 300)
    q(os.path.join(D, 'b306_the_difference.txt'), 'A CONSTITUENT',
      '### ZEROED, not EXCLUDED -- and widening the window turns it back on', 300)
    q(os.path.join(D, 'b306_the_difference.txt'),
      'THE SOURCE PICKS ITS WINDOW SO THAT NO PRIME ENTERS',
      '### the two windows are COMPLEMENTARY CHOICES OF THE SAME KNOB', 300)
    q(os.path.join(D, 'b306_the_difference.txt'),
      'PRIME SIDE TRAVELS; THE ARCHIMEDEAN SIDE DOES NOT',
      '### and `b306`s own finding about WHICH SIDE TRAVELS', 300)
    rec()
    rec('  --- **C-II. THE MARGIN IS MINUS THE REMAINDER INTEGRAL** (Theorem 4.7, an EQUALITY) ---')
    q(FL, "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME",
      '### row `F2` of the ledger: the Sonin margin, its class, its grade', 700)
    rec()
    rec('  --- **C-III. THE PLACES SPLIT, AND THE ASSUMED STEP IS DISCLOSED** ---')
    q(os.path.join(D, 'b232_sign_of_A.txt'), 'SPLIT THE PLACES-SUM BY CC',
      '### `b232` step 4', 300)
    q(os.path.join(D, 'b232_sign_of_A.txt'), 'step 4 assumes the finite places carry',
      '### and the step it assumes, DISCLOSED RATHER THAN HIDDEN', 300)
    rec()
    rec('  --- **C-IV. TWO BOUNDS ON ONE QUANTITY, ORDERED ON THE BANKED CLASS** (`b399`) ---')
    q(os.path.join(D, 'b399_the_sign_and_the_refutation.txt'), '(M) IS REFUTED',
      '### `b399`s verdict, at its own line', 400, span=True)
    q(os.path.join(D, 'b399_the_sign_and_the_refutation.txt'),
      'THE STATEMENT IT WAS WAITING FOR', '### and the owed row, left OWED and RETYPED', 400,
      span=True)
    rec()
    rec('  --- **C-V. TWO FAMILIES, AND THE SONIN MARGIN IS NOT DEFINED ON THE LI ONE** ---')
    q(FL, 'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL',
      '### row `L1`: the bridge, its derivation, and what it still owes', 900)
    rec()
    rec('  --- **C-VI. THE POLE CONSTANT SEPARATES THE TWO ARCHIMEDEAN CHANNELS** ---')
    q(FL, 'two evaluations of one distribution and are not one functional',
      '### row `L2`: the relation the record STATES, at cost zero', 700)
    rec()
    rec('  --- **C-VII. THE LI MARGIN CARRIES THE FINITE PLACES, AND THEY ARE NOT SILENT** ---')
    q(FL, 'nevertheless stays positive throughout',
      '### row `F3`: the Li margin, its split, and the bench`s two negative ranges', 800)
    rec()
    rec('  --- **C-VIII. THE CLAUSE, AND WHAT IN IT IS UNOWNED** ---')
    q(FI, 'Stable anchor: `clause-stated`', '### the clause`s stable anchor in `FINDINGS.md`', 300)
    q(FL, 'are UNOWNED, and they are the clause',
      '### row `U1` (i): the quantifier, and it is the clause', 400)
    rec()


# ==================================================================================================
#  (2) THE WINDOW -- THE FERRY'S ADDITION TWO.
# ==================================================================================================
def survey2():
    bar('=')
    rec('  ### (2) THE WINDOW -- WHERE A BRIDGE WOULD HAVE TO LIVE, AND WHAT THE RECORD FOUND THERE.')
    bar('=')
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'SO THE PRIMES ENTER THROUGH THE LOCAL DISTRIBUTION',
      '### the window act: above the boundary, the primes ENTER', 340)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'THAT THE COVERED CELLS ARE SILENT IS A FACT ABOUT A SUPPORT',
      '### and below it they are SILENT, which is a fact about a support', 300)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE OF ANYTHING',
      '### **AND WHAT THE WINDOW ACT FOUND THERE -- ITS OWN REAL FINDING, A NEGATIVE ONE**', 300)
    q(os.path.join(D, 'b321_the_window_opened.txt'), 'BOTH FACTS ARE',
      '### both facts PROPERTIES OF THE COMPUTATION, neither a property of the primes', 300)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'they carry no information the zero side did not already carry',
      '### and the numbers carry NO INFORMATION the zero side did not already carry', 300)
    rec()
    rec('  ### **AND THE ORDER`S OWN PHRASE FOR THE WINDOW IS TESTED AGAINST THE SOURCE RATHER')
    rec('  ### ### THAN ADOPTED.** ### The ferry says the window is *"outside the source`s class and')
    rec('  ### where neither Theorem 1 nor Proposition C.1 applies."* ### **THE TWO HALVES OF THAT')
    rec('  ### ### PHRASE ARE NOT THE SAME CLAIM AND THIS SURVEY SEPARATES THEM**, by reading each')
    rec('  ### theorem`s own hypotheses out of the VERIFIED artefact -- section (3) below.')
    rec()


# ==================================================================================================
#  (3) COMPONENT 3's POPULATION -- THE LAWFUL SEEDS AND THE PRIMES.
# ==================================================================================================
def prime_powers_in(lo, hi, pmax=64, closed=True):
    """### **A SECOND ROUTE TO `b321`s PRINTED LIST, SHARING NO CODE WITH IT.** ### Every prime
    ### power `p^k` in the closed interval, by trial division. ### It banks nothing; it exists so a
    ### banked list can be checked."""
    out = []
    for p in range(2, pmax + 1):
        if any(p % d == 0 for d in range(2, int(p ** 0.5) + 1)):
            continue
        v = p
        while v <= hi:
            inside = (v >= lo and v <= hi) if closed else (v > lo and v < hi)
            if inside:
                out.append(v)
            v *= p
    return sorted(out)


def survey3():
    bar('=')
    rec('  ### (3) COMPONENT 3`s POPULATION -- EVERY BANKED CELL, ITS LAWFULNESS, ITS PRIMES.')
    bar('=')
    rec('  ### **THE GRID IS THE RECORD`S OWN THIRTEEN CELLS** (`b318` 1c / `b320` / `b321`), and')
    rec('  ### the lawfulness test is Theorem 1`s support condition as `b318` applied it:')
    rec('  ### `supp(f) = [a^-2, a^2] SUBSET (1/2, 2)`, i.e. ### **`a^2 < 2`.**')
    rec()
    grid = [1.30, 1.35, 1.41, 1.5, 1.7, 1.9, 1.99, 2.0, 2.01, 2.1, 2.4, 2.8, 3.0]
    rec('    a       a^2        supp = [a^-2, a^2]           lawful   prime powers in the support')
    rows = []
    for a in grid:
        hi = a * a
        lo = 1.0 / hi
        law = hi < 2.0
        pw = prime_powers_in(lo, hi)
        pwo = prime_powers_in(lo, hi, closed=False)
        rows.append(dict(a=a, a2=hi, lawful=law, primes=pw, primes_open=pwo))
        rec('    %-6.2f  %-9.5f  [%.6f, %.6f]     %-7s  %-18s %s'
            % (a, hi, lo, hi, 'YES' if law else 'no', pw if pw else '[] ### NONE',
               ('' if pw == pwo else '### OPEN-INTERVAL READING: %s' % (pwo or '[]'))))
    FIG['grid'] = rows
    nlaw = sum(1 for r in rows if r['lawful'])
    nlawp = sum(1 for r in rows if r['lawful'] and r['primes'])
    rec()
    rec('    ### LAWFUL CELLS : %d   ### LAWFUL CELLS ADMITTING A PRIME POWER : %d' % (nlaw, nlawp))
    rec('    ### UNLAWFUL CELLS : %d  ### UNLAWFUL CELLS ADMITTING ONE : %d'
        % (len(rows) - nlaw, sum(1 for r in rows if not r['lawful'] and r['primes'])))
    FIG['lawful'] = nlaw
    FIG['lawful_with_prime'] = nlawp
    rec()
    rec('  ### **AND THE COMPUTED LIST IS SET AGAINST THE BANKED ONE, WHICH SHARES NO CODE WITH')
    rec('  ### ### IT.** ### `b321` printed the prime powers actually admitted, at its own line:')
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'SO THE PRIMES ENTER THROUGH THE LOCAL DISTRIBUTION',
      '### `b321`s printed list, the banked route', 360)
    BANKED = {1.5: [2], 1.7: [2], 1.9: [2, 3], 1.99: [2, 3], 2.0: [2, 3], 2.01: [2, 4, 3],
              2.1: [2, 4, 3], 2.4: [2, 4, 3, 5], 2.8: [2, 4, 3, 5, 7], 3.0: [2, 4, 8, 3, 5, 7]}
    rec('      a       BANKED (b321)          CLOSED route          OPEN route')
    dis_c, dis_o = [], []
    for r in rows:
        bk = BANKED.get(round(r['a'], 2))
        if bk is None:
            continue
        if sorted(bk) != sorted(r['primes']):
            dis_c.append(r['a'])
        if sorted(bk) != sorted(r['primes_open']):
            dis_o.append(r['a'])
        rec('      %-6.2f  %-22s %-22s %s'
            % (r['a'], sorted(bk), sorted(r['primes']), sorted(r['primes_open'])))
    rec()
    rec('      ### CELLS WHERE THE BANKED LIST DISAGREES WITH THE **CLOSED** ROUTE : %d %s'
        % (len(dis_c), dis_c))
    rec('      ### CELLS WHERE THE BANKED LIST DISAGREES WITH THE **OPEN** ROUTE   : %d %s'
        % (len(dis_o), dis_o))
    rec()
    rec('  ### **AND THE DISAGREEMENT IS AT A CLOSED ENDPOINT, WHICH IS A CONVENTION AND NOT A')
    rec('  ### ### DISCREPANCY -- BUT `b321` PRINTED THE OTHER CONVENTION IN ITS OWN RULE.** ###')
    rec('  ### Its Component 3 states the rule as *a prime power `p^m` enters exactly when')
    rec('  ### `p^m <= a^2`* and its printed list omits `4` at `a = 2` and `9` at `a = 3`, which is')
    rec('  ### the STRICT reading. ### **THE RULE AND THE LIST ON THAT FACE ARE TWO CONVENTIONS**,')
    rec('  ### and this act prints both rather than choosing for it or editing it.')
    rec('  ### ### **AND IT MOVES NO VALUE.** ### `f = g conv g^#` is a self-convolution supported')
    rec('  ### in `[a^-2, a^2]` and VANISHES AT ITS ENDPOINTS, so an endpoint prime power')
    rec('  ### contributes `0` to (149) under either reading. ### **THE `PR` COLUMN IS UNAFFECTED;')
    rec('  ### ### WHAT DIFFERS IS A PRINTED MEMBERSHIP LIST AT `2` OF `13` CELLS.**')
    FIG['banked_vs_closed_disagree'] = dis_c
    FIG['banked_vs_open_disagree'] = dis_o
    FIG['two_routes_agree'] = (len(dis_o) == 0)
    rec()
    rec('  ### **THE STRUCTURAL READING, SEPARATED FROM THE CENSUS BECAUSE IT IS A DIFFERENT KIND')
    rec('  ### ### OF FACT.** ### The least prime power is `2`. ### Theorem 1`s support condition is')
    rec('  ### exactly `supp(f) SUBSET (1/2, 2)`. ### **SO A PRIME POWER IN THE SUPPORT REQUIRES')
    rec('  ### ### `a^2 >= 2`, WHICH IS EXACTLY THE FAILURE OF THE SUPPORT CONDITION.** ### The')
    rec('  ### census above therefore could not have come out any other way, ### **AND THAT IS THE')
    rec('  ### ### FINDING RATHER THAN THE COUNT.**')
    rec()
    rec('  ### **AND THE OTHER BANKED FAMILIES, NAMED SO THE SCOPE IS NOT OVERSTATED.**')
    q(FL, 'the finite family constructed, the archimedean family read at its source',
      '### row `F6`: the two-radius family', 400)
    q(FL, 'a positive Li ledger with RH false',
      '### row `F7`: the Epstein negative control', 400)
    rec()


# ==================================================================================================
#  (4) IS THE BRIDGE THE CLAUSE? -- ASKED OF THE RECORD, NOT ANSWERED FROM THE ORDER.
# ==================================================================================================
def survey4():
    bar('=')
    rec('  ### (4) DOES THE RECORD`S OWN WORDS SAY THE BRIDGE AND THE CLAUSE ARE ONE QUESTION?')
    bar('=')
    rec('  ### **THE FERRY FORBIDS THE CLAIM UNLESS THE RECORD MAKES IT**, so this is a search and')
    rec('  ### not an argument. ### The needles are the ones a record making that claim would carry.')
    rec()
    hay = []
    for p in (FL, FI, OT):
        try:
            hay.append((os.path.basename(p),
                        io.open(p, encoding='utf-8', errors='replace').read()))
        except OSError:
            pass
    needles = ['the bridge and the clause', 'one question', 'the same question',
               'equivalent to the clause', 'is the clause itself']
    tot = 0
    for nd in needles:
        for name, txt in hay:
            n = txt.lower().count(nd.lower())
            tot += n
            rec('    needle `%s` in `%s` : %d' % (nd, name, n))
    rec()
    rec('    ### ### **TOTAL HITS : %d**' % tot)
    FIG['one_question_hits'] = tot
    rec()


def main():
    bar('=')
    rec('b400 -- THE BRIDGE RESTATED, OR THE PAIR DECLARED TWO OBJECTS. ### THE EXTRACT.')
    rec('### **A SURVEY. ### NOTHING IS WRITTEN BY THIS FILE EXCEPT ITS OWN TWO RUN RECORDS.**')
    bar('=')
    rec()
    src = survey0()
    if src.get('CC'):
        bar('=')
        rec('  ### (0b) THE SOURCE FRAGMENTS, LOCATED IN THE VERIFIED ARTEFACT.')
        bar('=')
        pages = pdf_pages(src['CC'])
        rec('    CC pages flattened : %d' % len(pages))
        rec()
        qsrc(pages, 'so that rational primes are not involved',
             '### **(S1) THE SOURCE`S OWN PRIME-FREE SENTENCE** -- `C-I``s import')
        qsrc(pages, 'the support condition', '### **(S2) THE WIDENING THE SOURCE NAMES AND DOES '
             'NOT TAKE**')
        qsrc(pages, 'a finite set disjoint from Z and containing',
             '### **(S3) PROPOSITION C.1 / (155) -- THE CRITERION, AND ITS HYPOTHESES.** ### '
             '**READ FOR A SUPPORT CONDITION, BECAUSE THE ORDER ASSERTS ONE**')
        qsrc(pages, 'theorem 1', '### **(S4) THEOREM 1 -- AND ITS SUPPORT HYPOTHESIS**')
        qsrc(pages, 'have support in the interval',
             '### **(S7) AND THEOREM 1`S SUPPORT HYPOTHESIS, ISOLATED**', after=300)
        qsrc(pages, 'involves only finitely many primes',
             '### **(S8) THE SOURCE ON WHAT COMPACT SUPPORT BUYS**', after=300)
    if src.get('LG'):
        pages = pdf_pages(src['LG'])
        rec('    Lagarias pages flattened : %d' % len(pages))
        rec()
        qsrc(pages, 'correspond to the contributions of the archimedean place',
             '### **(S5) THE LI SPLIT** -- `lambda_n = S_inf(n) - S_f(n) + 1`')
        qsrc(pages, 'the special test functions',
             '### **(S6) THE LI TEST FAMILY `G_n`** -- and its support')
    survey1()
    survey2()
    survey3()
    survey4()
    bar('=')
    rec('  ### THE SURVEY, COUNTED.')
    bar('=')
    anc = sum(1 for r in READS if r['verdict'].startswith('ANCHORED'))
    rec('    reads          : %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d'
        % (len(READS), anc, sum(1 for r in READS if r['verdict'] == 'AMBIGUOUS'),
           sum(1 for r in READS if r['verdict'] == 'ABSENT')))
    loc = sum(1 for r in SRCREADS if r['pages'])
    rec('    source fragments : %d ; LOCATED %d ; NOT LOCATED %d'
        % (len(SRCREADS), loc, len(SRCREADS) - loc))
    FIG['reads'] = len(READS)
    FIG['anchored'] = anc
    FIG['srcreads'] = len(SRCREADS)
    FIG['srclocated'] = loc
    bar('=')
    p = run_clock.write(D, 'b400_extract_notes', L)
    j = os.path.join(D, 'b400_extract.json')
    payload = json.dumps(dict(reads=READS, srcreads=SRCREADS, fig=FIG), indent=1,
                         ensure_ascii=False)
    io.open(j, 'w', encoding='utf-8', newline=chr(10)).write(payload)
    print('  written: %s' % os.path.basename(p))
    print('  written: %s' % os.path.basename(j))
    return 0


if __name__ == '__main__':
    sys.exit(main())
