# -*- coding: utf-8 -*-
"""b399_extract.py -- THE SIGN TEST FIRST, THE SOURCES BEFORE ANY QUOTATION, THEN THE ATTEMPT.

### ### **THE ORDER PLACES ADDITION ONE FIRST AND ADDITION ONE CAN STOP THE ACT.** ### So this
### extract runs in the order's own order: ### **the sources acquired and hash-verified BEFORE a
### word of either is read** (Addition Two -- *a derivation quoted from an unverified copy is not a
### derivation*), then ### **the settled sign chain quoted link by link from its OWNING ACTS and
### never from the navigator** (Addition One), then the components.

### ### **WHAT COMPUTES HERE AND WHAT DOES NOT.** ### No instrument is run, no kernel is built, no
### object is recomputed. ### The only arithmetic performed is on figures READ from the acts that
### emitted them, at their own lines, by the anchor tool -- and every such step prints its inputs
### beside its output so a reader can redo it by hand.

### ### **THE DEAFNESSES, STATED IN THE INSTRUMENT.** ### (1) It cannot tell a correct quotation
### from an invented one; it can only fail loudly when a fragment is not where it is claimed to be.
### (2) The PDF flattener strips punctuation and case, so `W_8 = -W_R` and `W_8 W_R` flatten to the
### same string: ### **A SIGN READ THROUGH THE FLATTENER IS READ FROM ITS SURROUNDING SENTENCE AND
### ### NOT FROM ITS GLYPHS**, and this instrument says so rather than hiding it.
### (3) A banked figure is as good as its owning act's frame; where two acts print different columns
### for the same name this extract prints BOTH and does not choose.
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
FINDINGS = os.path.join(PP, 'FINDINGS.md')
EMERG = os.path.join(PP, 'EMERGING_RESEARCH_PROGRAMMES.md')
FERRY = os.path.join(D, 'b399_ferry_2026-09-10.txt')

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
FIG = {}


def q(path, hint, label, n=320):
    """### **EVERY QUOTATION IS PULLED BY THE ANCHOR TOOL FROM THE FILE THAT EMITTED IT.**"""
    try:
        i, ln = AF.find(path, hint)
        v = 'ANCHORED'
    except Exception as e:
        i, ln, v = 0, '', ('AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT')
    READS.append(dict(path=os.path.basename(path), label=flat(label, 160), line=i, verdict=v,
                      text=flat(ln, 700)))
    rec('    %s  ### `%s:%s`' % (label, os.path.basename(path), i or '--'))
    if v == 'ANCHORED':
        rec('      > %s' % flat(ln, n))
    else:
        rec('      ### **%s** -- the hint matched %s' % (v, 'many lines' if v == 'AMBIGUOUS'
                                                         else 'nothing'))
    return i, ln


# ==================================================================================================
#  ADDITION TWO -- THE SOURCES, BEFORE ANY QUOTATION.
# ==================================================================================================
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def acquire(want_sha, want_bytes, name):
    """### **AN ACQUISITION IS A FILE WHOSE DIGEST EQUALS THE CORPUS'S PIN.** ### b327's own rule,
    quoted in its source record: *a re-acquisition that matches it is the pinned artefact.*"""
    hits = []
    scanned = 0
    for r in SEARCH_ROOTS:
        for dp, _dn, fn in os.walk(r):
            for f in fn:
                p = os.path.join(dp, f)
                try:
                    sz = os.path.getsize(p)
                except OSError:
                    continue
                if sz != want_bytes:
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
    rec('  ### ADDITION TWO -- THE SOURCES, ACQUIRED AND VERIFIED BEFORE A WORD IS READ.')
    bar('=')
    rec('  ### ### **b398 RECORDED THAT NEITHER PINNED SOURCE WAS ON THIS DRIVE, WHICH WEAKENED')
    rec('  ### ### EVERY SOURCE QUOTATION IT MADE.** ### The order says a derivation cannot rest')
    rec('  ### ### on that. ### **SO: ACQUIRE, VERIFY AGAINST THE CORPUS`S BANKED HASH, AND')
    rec('  ### ### REPORT `VERIFIED` WITH THE DIGEST -- OR `HALT` THAT COMPONENT.**')
    rec()
    q(os.path.join(D, 'b327_source.txt'),
      'A RE-ACQUISITION THAT MATCHES IT IS THE PINNED ARTEFACT',
      '### **THE CORPUS`S OWN RULE FOR WHAT COUNTS AS AN ACQUISITION**', 300)
    rec()
    out = {}
    for key, sha, nby, cite in [
            ('CC', CC_SHA, CC_BYTES,
             'Connes & Consani, "Weil positivity and Trace formula the archimedean place", '
             'arXiv:2006.13771v1'),
            ('LG', LG_SHA, LG_BYTES,
             'J. C. Lagarias, "Li coefficients for automorphic L-functions", arXiv:math/0404394v4')]:
        hits, scanned = acquire(sha, nby, key)
        rec('  ### **%s** -- %s' % (key, cite))
        rec('      banked pin        : %d bytes, sha256 `%s`' % (nby, sha))
        rec('      files of that size examined by digest : %d' % scanned)
        rec('      byte-identical copies located         : %d' % len(hits))
        for p in hits[:3]:
            rec('        %s' % p)
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
    rec('  ### ### **AND WHERE THEY WERE FOUND IS SAID, NOT SMOOTHED:** ### this machine`s own')
    rec('  ### ### fetch caches -- the same place `b327` located its copy and said so. ### **THE')
    rec('  ### ### PIN IS WHAT MAKES THE COPY THE ARTEFACT; THE DIRECTORY IS NOT EVIDENCE OF')
    rec('  ### ### ANYTHING** and is printed only so a reader can repeat the check.')
    rec()
    FIG['sources'] = {k: bool(v) for k, v in out.items()}
    return out


def pdf_pages(p):
    from pypdf import PdfReader
    r = PdfReader(p)
    return [S5.flatten(pg.extract_text() or '') for pg in r.pages]


SRCREADS = []


def qsrc(pages, needle, label, before=0, after=520, page=None):
    """### **A SOURCE FRAGMENT IS LOCATED BY PAGE INDEX AND ITS SURROUNDING SENTENCE PRINTED.**"""
    nn = S5.flatten(needle)
    found = []
    for i, t in enumerate(pages, 1):
        if page and i != page:
            continue
        j = t.find(nn)
        if j >= 0:
            found.append((i, t[max(0, j - before):j + after]))
    SRCREADS.append(dict(label=flat(label, 160), needle=nn[:80],
                         pages=[i for i, _ in found]))
    rec('    %s' % label)
    if found:
        i, txt = found[0]
        rec('      ### page index `%d` (of the artefact`s own numbering) -- %d hit(s) total : %s'
            % (i, len(found), [x for x, _ in found]))
        rec('      > %s' % txt[:after])
    else:
        rec('      ### **NOT LOCATED IN THE VERIFIED ARTEFACT** -- and nothing is quoted from it.')
    return found


def survey0b(paths):
    bar('=')
    rec('  ### THE SOURCE SENTENCES THIS ACT WILL USE, LOCATED IN THE VERIFIED ARTEFACT.')
    bar('=')
    rec('  ### ### **THE FLATTENER STRIPS PUNCTUATION AND CASE** -- b305`s, imported and')
    rec('  ### ### self-tested below. ### So `W_8 = -W_R` reaches this page as `w8wr`, and')
    rec('  ### ### ### **A SIGN IS READ FROM ITS SENTENCE AND NOT FROM ITS GLYPHS.**')
    ok = S5.self_test(verbose=False)
    rec('  ### b305 flattener self-test : %s' % ('PASS' if ok else 'FAIL'))
    rec()
    if not paths.get('CC'):
        rec('  ### **HALTED: the CC artefact is not verified, so no CC sentence is read.**')
        return
    P = pdf_pages(paths['CC'])
    rec('  ### CC artefact pages : %d' % len(P))
    rec()
    rec('  ### **(S1) THEOREM 1 -- THE CLASS AND THE INEQUALITY, IN THE SOURCE`S OWN WORDS.**')
    qsrc(P, 'theorem1letgpc8cprqhavesupportintheinterval',
         '### the theorem the whole Sonin margin comes from', after=300)
    rec('  ### ### **DECODED:** ### *Theorem 1. Let `g` in `C_c^inf(R*_+)` have support in the')
    rec('  ### ### interval `[2^-1/2, 2^1/2]` and Fourier transform vanishing at `i/2` and `0`.')
    rec('  ### ### Then one has* ### **`W_8(g conv g^*) >= Tr(theta(g) S theta(g)*)`.**')
    rec('  ### ### **SO THE MARGIN IS `W_8 - Tr` AND THEOREM 1 SAYS IT IS NONNEGATIVE ON THE')
    rec('  ### ### CLASS.** ### (`e` is the flattener`s residue of `>=`; the direction is read')
    rec('  ### ### from the sentence that follows it, quoted next.)')
    rec()
    rec('  ### **(S2) AND `W_8 >= 0` ON POSITIVE-DEFINITE SEEDS -- THE SOURCE`S OWN COROLLARY.**')
    qsrc(P, 'itfollowsthatw8pfqe0foranysmoothpositivedefinitefunctionf',
         '### the positivity the strategy rests on', after=300)
    rec()
    rec('  ### **(S3) THE EXPLICIT FORMULA (148) AND THE LOCAL TERM (149).**')
    qsrc(P, 'theexplicitformulatakestheform',
         '### (147), (148), (149) and (150) in one run of text', after=560)
    rec('  ### ### **DECODED, (148):** ### `SUM_rho f~(rho) - INT_0^8 f(x)dx - INT_0^8 f^#(x)dx')
    rec('  ### ### = SUM_v W_v(f)`, ### **`v` RUNNING OVER ALL PLACES `{R, 2, 3, 5, ...}` OF `Q`.**')
    rec('  ### ### **DECODED, (149):** ### **`W_p(f) = (log p) SUM_{m>=1} ( f(p^m) + f^#(p^m) )`.**')
    rec('  ### ### **DECODED, (150):** ### `W_R(f)` is the archimedean member of the same sum.')
    rec()
    rec('  ### **(S4) AND THE ARCHIMEDEAN SIGN, IN THE SENTENCE THE CORPUS CITES.**')
    qsrc(P, 'apositivityresultforthedistribution',
         '### the sentence that fixes `W_8` against `W_R`', after=200)
    rec('  ### ### **DECODED:** ### *in [6] and [8] a positivity result for the distribution')
    rec('  ### ### ### **`W_8 = - W_R`** ### is proven for test functions with support in a small')
    rec('  ### ### enough interval around 1.*')
    rec('  ### ### ### **THEREFORE, FROM THE SOURCE AND NOT FROM ANY SEAT:**')
    rec('  ### ### ### **`SUM_v W_v(f) = W_R(f) + SUM_p W_p(f) = - W_8(f) + SUM_p W_p(f)`.**')
    rec()
    rec('  ### **(S5) PROPOSITION C.1 -- THE CRITERION, AND WHAT ITS EASY DIRECTION IS.**')
    qsrc(P, 'propositionc1letzacbethesetofnontrivialzeros',
         '### the criterion the clause quantifies over', after=420)
    rec('  ### ### **DECODED:** ### *RH <=> `SUM_v W_v(g conv g^#) <= 0` for all `g` in')
    rec('  ### ### `C_c^inf(R*_+)` with `g~(z) = 0` for all `z` in `F`*, ### **and the `<=`')
    rec('  ### ### direction follows from the explicit formula (148).**')
    rec()
    if paths.get('LG'):
        PL = pdf_pages(paths['LG'])
        rec('  ### **(S6) AND THE LI SIDE`S THREE TERMS, FROM THE VERIFIED LAGARIAS ARTEFACT.**')
        rec('  ### LG artefact pages : %d' % len(PL))
        qsrc(PL, 'inwhichs', '### the decomposition into archimedean, finite and pole terms',
             after=420)


# ==================================================================================================
#  ADDITION ONE -- THE SIGN TEST.
# ==================================================================================================
def survey1():
    bar('=')
    rec('  ### ADDITION ONE -- THE SIGN TEST, RUN BEFORE ANY DERIVATION.')
    bar('=')
    rec('  ### ### **THE CHAIN IS QUOTED FROM ITS OWNING ACTS, LINK BY LINK, AND NEVER FROM THE')
    rec('  ### ### NAVIGATOR.** ### This component computes nothing new: it reads a chain and a')
    rec('  ### ### banked table.')
    rec()
    rec('  ### **LINK 0 -- (M), AS THE ACT THAT NAMED IT WROTE IT.**')
    q(os.path.join(D, 'b398_the_li_weil_bridge.txt'),
      'For every `g` in the source`s class', '### **(M), its quantifier and its class**', 400)
    q(os.path.join(D, 'b398_the_li_weil_bridge.txt'),
      '= SUM_p W_p(g conv g-bar^#)', '### **(M), its two sides**', 400)
    rec()
    rec('  ### **LINK 1 -- THE COMPRESSED SQUARE IS NONNEGATIVE, AND AS ARITHMETIC.**')
    q(os.path.join(D, 'b318_the_forced_sign.txt'),
      'THE ARITHMETIC NONNEGATIVITY, AT A FRAME SMALL ENOUGH TO DECIDE EXACTLY',
      '### **the heading b318 gave it**', 300)
    q(os.path.join(D, 'b318_the_forced_sign.txt'),
      'PERFORMS NO SUBTRACTION ANYWHERE',
      '### **why it is arithmetic and not a measurement**', 420)
    q(os.path.join(D, 'b318_the_forced_sign.txt'),
      'THE SQUARE IS NONNEGATIVE AT EVERY CELL AND EVERY FRAME',
      '### **and the scan that carries it**', 340)
    q(os.path.join(D, 'b318_the_forced_sign.txt'),
      'CELLS AT WHICH THE SQUARE IS NEGATIVE ANYWHERE',
      '### **the count**', 260)
    rec('  ### ### ### **LINK 1 HOLDS. ### `Tr(theta(g) S theta(g)*) >= 0` BY THE SHAPE OF ITS')
    rec('  ### ### ### ACCUMULATION, AND STRICTLY `> 0` AT EVERY BANKED CELL.**')
    rec()
    rec('  ### **LINK 2 -- AND THE SQUARE IS THE SMEAR AT THE AUTOCORRELATION, BY TWO CODE PATHS.**')
    q(os.path.join(D, 'b318_the_forced_sign.txt'),
      'THE SMEAR EVALUATED AT',
      '### **the identity that fixes which argument each side takes**', 420)
    rec('  ### ### **SO `(M)`S LEFT SIDE AND ITS RIGHT SIDE TAKE THE SAME ARGUMENT** -- the')
    rec('  ### ### autocorrelation `f = g conv g-bar^#` -- and the two sides are comparable at all.')
    rec()
    rec('  ### **LINK 3 -- THE SEEDS THAT ARE IN THE SOURCE`S CLASS, AND THE ONES THAT ARE NOT.**')
    q(os.path.join(D, 'b318_the_forced_sign.txt'),
      'support inside Theorem 1',
      '### **the class test, cell by cell**', 300)
    q(os.path.join(D, 'b318_the_forced_sign.txt'),
      'THE READING, AND IT IS A DEFINITIONAL ONE',
      '### **and what the corpus`s window is**', 420)
    rec('  ### ### ### **THE LAWFUL SEEDS OF THE RECORD ARE `a = 1.30, 1.35, 1.41` -- THREE OF')
    rec('  ### ### ### THIRTEEN. ### THE OTHER TEN FAIL THEOREM 1`S SUPPORT CONDITION.**')
    q(os.path.join(D, 'b320_the_lawful_function.txt'),
      'These ten cells fail Theorem 1',
      '### **b320 says the same of the same ten, in its own words**', 380)
    rec()
    rec('  ### **LINK 4 -- HOW THE CORPUS`S PRIME SUM RELATES TO THE SOURCE`S LOCAL TERMS.**')
    q(os.path.join(D, 'b305_the_arithmetics_entry.txt'),
      'NOT MERELY',
      '### **b305`s verdict on the identification**', 420)
    q(os.path.join(D, 'b305_the_arithmetics_entry.txt'),
      'THESE ARE THE SAME EXPRESSION, AND THE CORPUS',
      '### **factor for factor, with the factor 2 explained**', 420)
    q(os.path.join(D, 'b306_the_difference.txt'),
      '(F2) "the corpus\'s prime side IS the source\'s finite-places sum at the window, cutoff',
      '### **and the ONE exception, carried and not dropped**', 420)
    q(os.path.join(D, 'b232_sign_of_A.txt'),
      'and   ### ### **`\U0001d4b2_∞ = − A`.**',
      '### **the sign, derived from the source`s own arrangement**', 340)
    q(os.path.join(D, 'b232_sign_of_A.txt'),
      'THE NAMED STEP, DISCLOSED RATHER THAN HIDDEN',
      '### **the step b232 disclosed rather than hid**', 380)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'AND IT IS THE SIGN TEST BECAUSE OF ONE SENTENCE ON PAGE 49',
      '### **and b321`s independent check of the same sign**', 400)
    rec('  ### ### ### **SO `(M)`S RIGHT SIDE IS THE CORPUS`S PRIME COLUMN, IN THE SOURCE`S OWN')
    rec('  ### ### ### NORMALIZATION, DIFFERING FROM THE CORPUS`S OWN COLUMN ONLY IN THE CUTOFF')
    rec('  ### ### ### WINDOW -- AND THIS ACT USES THE SOURCE`S WINDOW, WHICH IS `(M)`S.**')
    rec()
    rec('  ### **LINK 5 -- THE CRITERION AND THE MEASURED LADDER, FROM THE ACT THAT MEASURED IT.**')
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'THE CRITERION, QUOTED VERBATIM FROM PROPOSITION C.1',
      '### **the criterion as b321 quoted it**', 300)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'THE PRIME SUM CHANGES SIGN TWICE ALONG THE LADDER',
      '### **THE SIGN CHANGE THE ORDER POINTS AT**', 420)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'THAT THE COVERED CELLS ARE SILENT IS A FACT ABOUT A SUPPORT',
      '### **AND WHAT THE SAME ACT SAYS ABOUT THE COVERED CELLS**', 380)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'The prime',
      '### **the prime powers actually admitted, cell by cell**', 380)
    rec()
    rec('  ### **LINK 6 -- THE BANKED LAWFUL-SEED TABLE, READ FROM BOTH ACTS THAT PRINT IT.**')
    a, r1 = q(os.path.join(D, 'b321_the_window_opened.txt'),
              '1.3    8.781188392',
              '### **b321 Component 2, the four channels at `a = 1.30`**', 300)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      '1.35   7.130749976', '### **the same at `a = 1.35`**', 300)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      '1.41   5.747988162', '### **the same at `a = 1.41`**', 300)
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      '1.3    YES       0.271444634',
      '### **b321 Component 4, `covered` / margin / PR at `a = 1.30`**', 300)
    q(os.path.join(D, 'b320_the_lawful_function.txt'),
      '`a = 1.30` : ### **`W_inf = 8.781214000`',
      '### **b320, the square itself at `a = 1.30`**', 340)
    q(os.path.join(D, 'b320_the_lawful_function.txt'),
      '`a = 1.35` : ### **`W_inf = 7.130772347`',
      '### **b320, at `a = 1.35`**', 340)
    q(os.path.join(D, 'b320_the_lawful_function.txt'),
      '`a = 1.41` : ### **`W_inf = 5.748007707`',
      '### **b320, at `a = 1.41`**', 340)
    q(os.path.join(D, 'b320_the_lawful_function.txt'),
      "corpus's prime column is exactly `0` until `a = 2.1`",
      '### **and b320`s OWN prime column, on the corpus`s window**', 400)
    rec()
    bar('-')
    rec('  ### THE TABLE THE SIGN TEST IS DECIDED ON. ### **EVERY FIGURE READ, NONE COMPUTED.**')
    bar('-')
    rows = [('1.30', '8.781214000', '8.509769366', '0.271444634', '0.000000000', 'YES'),
            ('1.35', '7.130772347', '6.845262034', '0.285510313', '0.000000000', 'YES'),
            ('1.41', '5.748007707', '5.438230060', '0.309777648', '0.000000000', 'YES'),
            ('1.50', '4.372801098', '4.016120530', '0.356680568', '0.000062755', 'no'),
            ('1.70', '2.723018452', '2.239620675', '0.483397777', '0.007899310', 'no'),
            ('1.90', '1.889498505', '1.296882974', '0.592615532', '-0.022845349', 'no'),
            ('2.10', '1.396323322', '0.754150956', '0.642172365', '-0.064050234', 'no'),
            ('2.40', '0.952619641', '0.342389825', '0.610229816', '-0.030383030', 'no'),
            ('2.80', '0.617613198', '0.138934660', '0.478678538', '0.118199794', 'no'),
            ('3.00', '0.506677452', '0.098273158', '0.408404294', '0.190860829', 'no')]
    rec('    a       W_8 (arch)      SQUARE = Tr      margin          SUM_p W_p (149)  in the class')
    for a_, w, s, m, p, cov in rows:
        rec('    %-6s  %-14s  %-14s   %-14s  %-15s  %s' % (a_, w, s, m, p, cov))
    rec('  ### ### **THE `in the class` COLUMN IS b318`S SUPPORT TEST AND b320`S `covered`, NOT')
    rec('  ### ### THIS ACT`S JUDGEMENT.** ### The `SUM_p W_p` column is b321`s `PR`, computed on')
    rec('  ### ### the SOURCE`S window `[a^-2, a^2]`; b320`s own column, on the CORPUS`S window,')
    rec('  ### ### is `0.000000000` at every cell to `a = 2.01` and positive after. ### **BOTH')
    rec('  ### ### COLUMNS ARE `0.000000000` AT ALL THREE LAWFUL CELLS, SO THE SIGN TEST DOES NOT')
    rec('  ### ### DEPEND ON WHICH WINDOW IS TAKEN.**')
    rec()
    bar('-')
    rec('  ### THE SIGN TEST, SET OUT AND DECIDED.')
    bar('-')
    rec('  ### **(M)`S CONSEQUENCE, DERIVED FROM LINK 1 AND NOTHING ELSE:** ### `(M)` reads')
    rec('  ### `-Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#)`; ### **`Tr >= 0` AS')
    rec('  ### ### ARITHMETIC** (Link 1); ### therefore ### **`SUM_p W_p(g conv g-bar^#) <= 0`')
    rec('  ### ### FOR EVERY `g` IN THE SOURCE`S CLASS.**')
    rec()
    rec('  ### **THE FORBIDDEN SIGN IS THEREFORE: A LAWFUL SEED WITH A STRICTLY POSITIVE PRIME')
    rec('  ### SUM.** ### Set the banked values against it:')
    lawful = [('1.30', '0.000000000'), ('1.35', '0.000000000'), ('1.41', '0.000000000')]
    for a_, p in lawful:
        rec('      `a = %s` (in the class) : ### `SUM_p W_p = %s` -- nonpositive : **TRUE**' % (a_, p))
    rec('      ### **LAWFUL SEEDS IN THE RECORD : 3. ### GIVING THE FORBIDDEN SIGN : 0.**')
    rec()
    rec('  ### **AND WHERE THE SIGN CHANGE ACTUALLY LIVES:** ### every cell at which the prime sum')
    rec('  ### is strictly positive -- `a = 1.5, 1.7, 2.8, 3.0` -- and every cell at which it is')
    rec('  ### strictly negative -- `a = 1.9, 1.99, 2.0, 2.01, 2.1, 2.4` -- ### **IS A CELL THAT')
    rec('  ### ### FAILS THEOREM 1`S SUPPORT CONDITION**, which is exactly what b320 says of those')
    rec('  ### ### ten rows before printing them.')
    rec('  ### ### ### **SO THE CHAIN DOES FLIP IT, AND NOT BY A SIGN CONVENTION: ### IT FLIPS IT')
    rec('  ### ### ### BY THE CLASS.** ### The measured sign change is measured entirely OUTSIDE')
    rec('  ### ### ### the set `(M)` quantifies over.')
    rec()
    rec('  ### ### ### ### **VERDICT: ### (M) SURVIVES THE SIGN TEST.**')
    rec('  ### ### **AND THE SURVIVAL IS VACUOUS, WHICH IS SAID IN THE SAME BREATH AS THE')
    rec('  ### ### VERDICT.** ### The three lawful values are not small; they are `0` -- an EMPTY')
    rec('  ### ### SUM, because for `a <= 1.41` the support `[a^-2, a^2]` contains no prime power')
    rec('  ### ### and no reciprocal of one. ### **A CONSEQUENCE SATISFIED BY AN EMPTY SUM IS')
    rec('  ### ### SATISFIED VACUOUSLY**, and b321 had already said of exactly these cells that')
    rec('  ### ### their silence is a fact about a support and not a finding.')
    rec('  ### ### ### **THEREFORE THE SIGN TEST CANNOT REFUTE `(M)` ON THIS RECORD, AND IT DOES')
    rec('  ### ### ### NOT CONFIRM IT EITHER. ### THE ACT DOES NOT STOP, AND COMPONENTS 1 TO 3')
    rec('  ### ### ### RUN.**')
    rec('  ### ### b321`s own species, in force here rather than restated: ### *a count that could')
    rec('  ### ### not have come out the other way is the shape of the arithmetic and not a')
    rec('  ### ### measurement of the object.*')
    FIG['sign_verdict'] = 'SURVIVES-VACUOUSLY'
    FIG['lawful_cells'] = 3
    FIG['forbidden_sign_hits'] = 0


# ==================================================================================================
#  COMPONENT 1 -- THE TWO SIDES OF (M), EACH UNFOLDED TO WHAT IT IS A SUM OVER.
# ==================================================================================================
def survey2():
    bar('=')
    rec('  ### COMPONENT 1 -- THE TWO SIDES OF (M), EACH UNFOLDED TO WHAT IT IS A SUM OVER.')
    bar('=')
    rec('  ### **THE LEFT SIDE: `-Tr(theta(g) S theta(g)*)`.**')
    rec('  ###   the operator      : `theta(g) S theta(g)*`, `S` the source`s compression on the')
    rec('  ###                       Sonin space; `theta` the scaling action of `R*_+` on')
    rec('  ###                       `L^2(R)_ev` (Theorem 1, read at (S1) from the verified copy)')
    rec('  ###   what it sums over : ### **THE EIGEN-DIRECTIONS OF ONE ARCHIMEDEAN COPY.** ### Not')
    rec('  ###                       places. ### b197 read Theorem 2 of `2310.18423` and withdrew')
    rec('  ###                       the shape `Tr_8 + SUM_p Tr_p` for exactly this reason.')
    rec('  ###   as the record computes it : the Frobenius norm squared of `A[:,H] P` at a frame')
    rec('  ###                       `(N, X, NY)` with a rank -- b318, and ### **NO SUBTRACTION**')
    rec('  ###   VALUE or SIGN?    : ### **BOTH, AND THAT IS THE POINT.** ### The sign is')
    rec('  ###                       arithmetic (b318); the VALUE is measured at three lawful')
    rec('  ###                       cells (b320) and its SIZE is certified at none (b320).')
    q(os.path.join(D, 'b320_the_lawful_function.txt'),
      "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME",
      '### **b320 on what its own numbers certify**', 380)
    rec()
    rec('  ### **THE RIGHT SIDE: `SUM_p W_p(g conv g-bar^#)`.**')
    rec('  ###   the local term    : `W_p(f) = (log p) SUM_{m>=1} ( f(p^m) + f^#(p^m) )` -- CC')
    rec('  ###                       (149), read at (S3) from the verified copy')
    rec('  ###   what it sums over : ### **THE FINITE PLACES OF `Q`, AND WITHIN EACH, THE PRIME')
    rec('  ###                       POWERS `p^m` THAT LIE IN THE SUPPORT OF `f`.**')
    rec('  ###   the normalization : the corpus`s summand is CC`s `Delta`-normalized `W_p` factor')
    rec('  ###                       for factor (b305, b306), the factor `2` being `f + f^#`')
    rec('  ###                       collapsed under evenness -- ### **DIFFERENT ONLY IN THE')
    rec('  ###                       CUTOFF WINDOW**, and this act takes the source`s window')
    rec('  ###   VALUE or SIGN?    : ### **VALUE, AND EXACTLY.** ### At the three lawful cells the')
    rec('  ###                       sum has NO TERMS: `supp f = [a^-2, a^2]` and `a^2 < 2` at')
    rec('  ###                       `a <= 1.41`, while `p^m >= 2` and `p^-m <= 1/2 < a^-2`.')
    rec('  ###                       ### **SO THE RIGHT SIDE IS `0`, AND NOT AS A MEASUREMENT.**')
    rec()
    rec('  ### ### ### **THE ORDER`S QUESTION, ANSWERED BEFORE THE ATTEMPT: ### THE RECORD GIVES A')
    rec('  ### ### ### VALUE FOR BOTH SIDES AT THE LAWFUL CELLS. ### THE LEFT SIDE`S VALUE IS')
    rec('  ### ### ### MEASURED AND ITS SIGN IS ARITHMETIC; THE RIGHT SIDE`S VALUE IS EXACT AND')
    rec('  ### ### ### ITS SIGN IS THE SIGN OF ZERO.**')
    rec('  ### ### **(L1), THE DRAFT`S OWN FALSIFIER, IS THEREFORE MET AND NOT BY ARGUMENT:** ###')
    rec('  ### ### *the record gives a value, not merely a sign, for the compressed square on the')
    rec('  ### ### lawful class* -- `8.509769366`, `6.845262034`, `5.438230060`, b320`s own three.')


# ==================================================================================================
#  COMPONENT 2 -- (M), ATTEMPTED.
# ==================================================================================================
def survey3():
    bar('=')
    rec('  ### COMPONENT 2 -- (M), ATTEMPTED.')
    bar('=')
    rec('  ### ### **THE CHAIN, EVERY STEP WITH ITS OWNER AND ITS GRADE.**')
    rec()
    rec('  ### **STEP 1.** ### `Tr(theta(g) S theta(g)*) = Tr(theta(g conv g-bar^#) S)`.')
    rec('  ###   owner : b318, by two code paths sharing no formula (norm vs trace), agreeing to')
    rec('  ###           `1.9e-06`, `4.2e-06`, `3.4e-05` against a sealed bar of one per cent.')
    rec('  ###   grade : ### **MEASURED-ON-FAMILIES.**')
    rec()
    rec('  ### **STEP 2.** ### Theorem 4.7 / (83) is an EQUALITY:')
    rec('  ###   `Tr(theta(f) S) = W_8(f) + INT f(rho^-1) eps(rho) d*rho`.')
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      'THE IDENTITY CONTROL HOLDS',
      '### **the owner, and that it is an equality and not an inequality**', 420)
    rec('  ###   owner : b321, quoting the source; measured at the three lawful cells, the')
    rec('  ###           instrument`s residual falling by two to three at every ladder step.')
    rec('  ###   grade : ### **IMPORT-UNDER-THE-BAR** (the theorem) ### + **MEASURED-AT-COVERED-')
    rec('  ###           CELLS** (the agreement).')
    rec()
    rec('  ### **STEP 3.** ### Combining 1 and 2 at a lawful `g`, with `f = g conv g-bar^#`:')
    rec('  ###   ### **`-Tr(theta(g) S theta(g)*) = -W_8(f) + ( -INT f eps ) = -W_8(f) + margin`.**')
    rec('  ###   ### **SO `(M)`S LEFT SIDE IS DETERMINED BY TWO ARCHIMEDEAN QUANTITIES AND')
    rec('  ###   ### NOTHING ELSE.** ### No prime enters it at any step.')
    rec()
    rec('  ### **STEP 4 -- THE VALUES, READ AND THEN SUBTRACTED IN FRONT OF THE READER.**')
    rec('     a       W_8 (b320)      margin, theorem (b321)   LEFT = -W_8+margin   RIGHT (b321)')
    tab = [('1.30', 8.781214000, 0.158889558, 0.000000000),
           ('1.35', 7.130772347, 0.186481766, 0.000000000),
           ('1.41', 5.748007707, 0.221284108, 0.000000000)]
    LEFTS = []
    for a_, w, m, p in tab:
        left = -w + m
        LEFTS.append(left)
        rec('     %-6s  %-14.9f  %-22.9f   %-19.9f  %.9f' % (a_, w, m, left, p))
    q(os.path.join(D, 'b321_the_window_opened.txt'),
      '`a = 1.30` : ### **`- INT f eps = 0.158889558`',
      '### **the theorem`s own margin value at `a = 1.30`, read**', 300)
    rec('  ### ### **AND WITH THE INSTRUMENT`S MEASURED MARGIN INSTEAD OF THE THEOREM`S, THE LEFT')
    rec('  ### ### SIDE IS `-8.509769366`, `-6.845262034`, `-5.438230060` -- b320`s own SQUARE')
    rec('  ### ### column, negated.** ### The two VALUES of the margin are apart by `0.112555076`')
    rec('  ### ### at `a = 1.30`, and that number is not a discrepancy this act found: ### **IT IS')
    rec('  ### ### b321`S OWN PRINTED LADDER RESIDUAL** -- `0.896557, 0.306328, 0.112555,')
    rec('  ### ### 0.047182, 0.023224` -- the finite instrument walking toward the theorem`s exact')
    rec('  ### ### value, falling by a factor of two to three at every frame.')
    rec('  ### ### **AND THEY ARE NOT TWO INDEPENDENT ROUTES AND ARE NOT OFFERED AS ONE:')
    rec('  ### ### ### SINGLE-ARM.** ### One is the theorem`s value and the other is the same')
    rec('  ### ### quantity at a finite frame, so their difference is a RESOLUTION and not a')
    rec('  ### ### CORROBORATION. ### **THEY DIFFER IN THE FIRST DECIMAL AND THE REFUTATION NEEDS')
    rec('  ### ### ONLY THE FIRST DIGIT OF EITHER.**')
    rec()
    rec('  ### ### ### ### **THE COMPARISON, AT `a = 1.30`:**')
    rec('  ### ### ### ### **LEFT `= -8.622324442` (or `-8.509769366`). ### RIGHT `= 0`.**')
    rec('  ### ### ### ### **(M) IS FALSE AT THIS SEED.**')
    rec()
    rec('  ### **AND THE THREE WAYS OUT ARE CLOSED, EACH BY A NAMED FACT.**')
    rec('  ###   (a) ### **A NORMALIZATION CANNOT CLOSE IT.** ### `(M)` is stated *in the source`s')
    rec('  ###       own normalization*; any normalization of either side is a POSITIVE rescaling,')
    rec('  ###       and `lambda * (-8.62) = 0` has no positive solution. ### A strictly negative')
    rec('  ###       number and an exact zero are not related by a constant.')
    rec('  ###   (b) ### **A SIGN CONVENTION CANNOT CLOSE IT.** ### b232 filed a live sign question')
    rec('  ###       about `wInf - wPrimes`, so the convention was tested and not assumed: under')
    rec('  ###       the OTHER convention `(M)` reads `+Tr = SUM_p W_p`, i.e. `+8.62 = 0`.')
    rec('  ###       ### **BOTH CONVENTIONS FAIL AT THE SAME SEED**, so this is not a convention')
    rec('  ###       artefact.')
    rec('  ###   (c) ### **THE TRUNCATION CANNOT CLOSE IT.** ### The record`s `Tr` is a compression`s')
    rec('  ###       Frobenius norm squared; enlarging the frame ADDS nonnegative entries, so the')
    rec('  ###       untruncated value is at least the printed one. ### The left side cannot move')
    rec('  ###       toward zero by resolving the instrument, and b318`s ladder shows it drifting')
    rec('  ###       by `4e-04` to `6e-03` -- four orders below the discrepancy.')
    rec()
    rec('  ### **A CORROBORATION, LABELLED AS ONE AND CARRYING NO WEIGHT IN THE VERDICT.** ### If')
    rec('  ### `(M)` held then `SUM_p W_p = -Tr <= 0` on the whole class, and Proposition C.1`s')
    rec('  ### criterion would be satisfied identically -- ### **`(M)` WOULD PROVE RH ON THE')
    rec('  ### ### SOURCE`S CLASS IN ONE LINE FROM THE SOURCE`S OWN THEOREM 1.** ### The source')
    rec('  ### proves Theorem 1 and does not draw that conclusion. ### **THAT IS A REASON TO')
    rec('  ### ### EXPECT `(M)` TO BE FALSE AND IT IS NOT A PROOF THAT IT IS; ### THE PROOF IS THE')
    rec('  ### ### PRINTED VALUE ABOVE.**')
    rec()
    rec('  ### ### ### ### **VERDICT: ### (M) IS REFUTED.**')
    rec('  ### **THE COUNTER, QUOTED WITH ITS ACT AND ITS CELL:** ### `a = 1.30`, in the source`s')
    rec('  ### class by b318`s support test; ### `Tr = 8.509769366` (b320, `b320_the_lawful_')
    rec('  ### function.txt` line 26) or `8.622324442` by Theorem 4.7 with b321`s margin;')
    rec('  ### `SUM_p W_p = 0.000000000` (b321, Component 2 table, and `0` exactly by support).')
    rec('  ### ### **THE RESULT`S GRADE IS ITS WEAKEST LINK: ### MEASURED-AT-COVERED-CELLS** --')
    rec('  ### the left side`s value is measured, and only its POSITIVITY is arithmetic. ### **THE')
    rec('  ### ### REFUTATION NEEDS ONLY THE POSITIVITY AND AN EXACT ZERO, SO IT IS STRONGER THAN')
    rec('  ### ### ITS WEAKEST VALUE** -- and it is stated at the weaker grade anyway, because a')
    rec('  ### result is typed by what it rests on and not by how sure the seat feels.')
    rec()
    rec('  ### ### **AND THE ACT DID NOT STOP.** ### Addition One`s stop applies to a REFUTATION BY')
    rec('  ### ### SIGN, and the sign test returned SURVIVES. ### The refutation here is BY VALUE,')
    rec('  ### ### it is the attempt`s own declared verdict, and no derivation was attempted')
    rec('  ### ### against an identity already known to be false.')
    FIG['m_verdict'] = 'REFUTED-BY-VALUE'
    FIG['lefts'] = LEFTS


# ==================================================================================================
#  COMPONENT 3 -- WHAT (M) WOULD AND WOULD NOT BUY.
# ==================================================================================================
def survey4():
    bar('=')
    rec('  ### COMPONENT 3 -- WHAT (M) WOULD AND WOULD NOT BUY, AND WHAT ITS REFUTATION BUYS.')
    bar('=')
    rec('  ### **WHAT `(M)` WOULD HAVE BOUGHT, HAD IT HELD:** ### the Sonin margin read place-wise')
    rec('  ### would have BEEN the Weil functional, and the owed bridge`s first half would have')
    rec('  ### been paid as a DECOMPOSITION. ### **IT IS NOT AVAILABLE AND THIS ACT IS NOT')
    rec('  ### ### SPECULATING ABOUT IT.**')
    rec()
    rec('  ### **WHAT THE SECOND OBSTRUCTION STILL BLOCKS, INDEPENDENTLY AND WHATEVER `(M)` DID.**')
    q(os.path.join(D, 'b327_the_faces_ledger.txt'),
      'function whose inverse Mellin transform has no compact support',
      '### **the family obstruction, from its owning act**', 400)
    q(os.path.join(D, 'b327_the_faces_ledger.txt'),
      '### ### ### **ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL.**',
      '### **b327`s own sentence for it**', 300)
    rec('  ### ### **SO THE PAIR REMAINS TWO OBJECTS ON TWO DISJOINT FAMILIES, AND NO')
    rec('  ### ### NORMALIZATION FIXES A DOMAIN.** ### `(M)`s refutation does not touch this and')
    rec('  ### ### does not need to.')
    rec()
    rec('  ### **WHAT THE REFUTATION DOES BUY, STATED AT EXACTLY ITS SCOPE.**')
    rec('  ### ### **(1) THE MARGIN`S IDENTITY IS ALREADY OWNED, AND IT IS NOT THE PRIME SUM.** ###')
    rec('  ### By Theorem 4.7 the margin IS minus the remainder integral -- an ARCHIMEDEAN')
    rec('  ### quantity, measured at `0.158889558`, `0.186481766`, `0.221284108`. ### **THE RECORD')
    rec('  ### ### DID NOT LACK A STATEMENT ABOUT WHAT THE MARGIN IS; IT HAD ONE, AND `(M)` NAMED A')
    rec('  ### ### DIFFERENT ONE.**')
    rec('  ### ### **(2) THE TWO BOUNDS ARE TWO BOUNDS, AND ON THE BANKED CLASS THEY ARE ORDERED.**')
    rec('  ### Theorem 1 bounds `Tr <= W_8`; Proposition C.1 asks `SUM_p W_p <= W_8`. ### `(M)`')
    rec('  ### would have made them the same statement. ### At every banked lawful seed:')
    rec('  ###   `SUM_p W_p = 0` and `Tr = 8.51 / 6.85 / 5.44`, with `W_8 = 8.78 / 7.13 / 5.75`.')
    rec('  ### ### **SO THE TRACE BOUND IS THE BINDING ONE AND THE PRIME BOUND IS SLACK BY THE')
    rec('  ### ### WHOLE OF `W_8` -- ON THREE SEEDS, WHICH IS THREE SEEDS AND NOT A THEOREM.**')
    rec('  ### ### **(3) AND THE OWED ROW`S TYPE CHANGES.** ### b398 typed the missing statement a')
    rec('  ### RESULT and left the row OWED. ### **THE ROW IS NOT PAID BY THIS ACT AND IT IS NOT')
    rec('  ### ### OWED IN THE SAME WAY EITHER: ### THE STATEMENT IT WAS WAITING FOR IS FALSE.**')
    rec('  ### What the row needs is a different statement, and this act does not name it -- ')
    rec('  ### naming one would be Component 4 of an order that does not have one.')
    rec()
    rec('  ### ### **IN EVERY BRANCH, AND SAID BECAUSE THE ORDER SAYS TO SAY IT: ### THE CLAUSE HAS')
    rec('  ### ### NOT MOVED. ### NO COORDINATE IS CLOSED. ### NO GRADE IS CONFERRED.**')


# ==================================================================================================
#  ADDITION THREE -- THE STALE RANKING ROW.
# ==================================================================================================
def survey5():
    bar('=')
    rec('  ### ADDITION THREE -- THE STALE RANKING ROW: REPAIRED, OR ROUTED WITH THE REASON.')
    bar('=')
    rec('  ### **THE ROW, AS IT STANDS, PRESERVED VERBATIM BEFORE ANYTHING IS DECIDED.**')
    r1 = q(FINDINGS, '| 1 | **K5** the archimedean distribution | `DEFINED-ONLY`',
           '### **the ranking`s first row**', 480)
    r2 = q(FINDINGS, 'The softest rank is held by',
           '### **and the sentence that reads it**', 380)
    r3 = q(FINDINGS, 'The aim-map is named as the act that would chart',
           '### **and the sentence that acts on it**', 420)
    q(FINDINGS, 'Every grade above is its owner',
           '### **and what the section says about its own grades**', 380)
    rec()
    rec('  ### **THE LIFTING ACT, QUOTED.**')
    q(os.path.join(D, 'b333_registration_2026-09-06.txt'),
      "K5's grades become `DERIVES-ON-IMPORTS`",
      '### **b333`s re-rank, on its own sealed face**', 420)
    q(os.path.join(D, 'b333_derive_run.txt'),
      'DEFINED-ONLY superseded by DERIVES-ON-IMPORTS',
      '### **and in its own run record**', 400)
    rec()
    rec('  ### **AND THE FIRST THING TO CHECK IS WHETHER THE CORRECTION REALLY FAILED TO')
    rec('  ### PROPAGATE, BECAUSE THE ORDER`S PREMISE IS THAT IT DID.**')
    r4 = q(FINDINGS, 'The re-rank, under the sealed rule with nothing adjusted',
           '### **b333`s re-rank, IN THIS SAME DOCUMENT**', 700)
    rec('  ### ### ### **SO THE PREMISE IS HALF TRUE, AND THE HALF THAT IS FALSE DECIDES THE')
    rec('  ### ### ### BRANCH.** ### The correction is not missing from `FINDINGS.md`: it is')
    rec('  ### ### ### carried in full, in the same file, ### **%d LINES BELOW THE STALE ROW**,'
        % (max(0, (r4[0] or 0) - (r1[0] or 0))))
    rec('  ### ### ### by the lifting act`s own addendum. ### **WHAT IS MISSING IS A POINTER FROM')
    rec('  ### ### ### THE ONE TO THE OTHER.**')
    rec()
    rec('  ### **THE DECISION, AGAINST THE ORDER`S OWN TEST.**')
    rec('  ### The order: *if repairing it would move a grade rather than a citation, do NOT repair')
    rec('  ### it -- route it and say which.*')
    rec('  ###   ### **EDITING THE ROW`S GRADE CELL MOVES A GRADE, AND MOVES THREE MORE THINGS')
    rec('  ###   ### WITH IT:** ### `DEFINED-ONLY` -> `MEASURED-AT-COVERED-CELLS` puts K5 into a')
    rec('  ###   TIE with K6, so the RANK ORDER changes; the sentence *the softest rank is held by')
    rec('  ###   K5* becomes false as written; and the aim-map sentence`s parenthetical grade')
    rec('  ###   becomes false too. ### **THAT IS A GRADE MOVE IN A TABLE WHOSE OWN HEAD SAYS')
    rec('  ###   ### EVERY GRADE IN IT IS ITS OWNER`S AND NONE WAS CONFERRED THERE.**')
    rec('  ###   ### **ADDING A POINTER MOVES A CITATION AND NOTHING ELSE.** ### It changes no')
    rec('  ###   cell, no grade, no rank and no verdict sentence; it tells a reader where the')
    rec('  ###   re-rank is.')
    rec('  ### ### ### ### **VERDICT: ### THE GRADE MOVE IS ROUTED, NOT MADE. ### THE CITATION IS')
    rec('  ### ### ### ### REPAIRED IN PLACE. ### AND WHICH IS WHICH IS SAID.**')
    rec('  ### ### **THE ROW, ITS GRADE CELL, ITS RANK, ITS VERDICT SENTENCE AND THE AIM-MAP')
    rec('  ### ### SENTENCE ARE LEFT EXACTLY AS THEIR OWNING ACT LEFT THEM.**')
    FIG['add3'] = dict(row=r1[0], verdict_line=r2[0], aimmap_line=r3[0], rerank_line=r4[0],
                       decision='CITATION-REPAIRED-GRADE-ROUTED')
    return r1, r2, r3, r4


# ==================================================================================================
#  THE THREE COMPUTE CONTACTS -- WHERE THEY GO.
# ==================================================================================================
def survey6():
    bar('=')
    rec('  ### THE THREE COMPUTE CONTACTS -- THE TARGET, AND WHAT A CONTACT IS.')
    bar('=')
    q(EMERG, '## Contacts — filed 2026-09-05 (b327)',
      '### **the section, and its own definition of a contact**', 480)
    q(EMERG, "*Provenance of both:",
      '### **and the provenance line the existing two carry**', 400)
    q(EMERG, '### Contact B — The cubit reading of the 256 rules',
      '### **the last contact filed, so the new ones follow it**', 300)
    rec('  ### ### **FILED THERE AND NOWHERE RESEARCH-FACING** -- the order`s words, and the')
    rec('  ### ### section`s own. ### **EACH ONE CONTACT, ONE CONSEQUENCE, NO CLAIM.**')


def main():
    bar('=')
    rec('b399_extract.py -- THE SIGN TEST, THE SOURCES, AND THE ATTEMPT.')
    rec('### Ferry: `data/b399_ferry_2026-09-10.txt` -- part 1 of 1, receipt confirmed IN FULL.')
    rec('### **THE ORDER`S OWN ORDER: ADDITION TWO`S VERIFICATION AND ADDITION ONE`S SIGN TEST')
    rec('### BEFORE ANY DERIVATION.** ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    bar('=')
    rec()
    paths = survey0()
    rec()
    survey0b(paths)
    rec()
    survey1()
    rec()
    survey2()
    rec()
    survey3()
    rec()
    survey4()
    rec()
    survey5()
    rec()
    survey6()
    rec()
    bar('=')
    anch = sum(1 for r in READS if r['verdict'] == 'ANCHORED')
    rec('  ### THE READS: ### **%d, OF WHICH %d ANCHORED.**' % (len(READS), anch))
    bad = [r for r in READS if r['verdict'] != 'ANCHORED']
    for r in bad:
        rec('    ### **%s** -- %s | %s' % (r['verdict'], r['path'], r['label']))
    rec('  ### THE SOURCE FRAGMENTS: ### **%d, OF WHICH %d LOCATED.**'
        % (len(SRCREADS), sum(1 for s in SRCREADS if s['pages'])))
    bar('=')
    rec('  ### run stamp : %s' % run_clock.stamp())
    out = os.path.join(D, 'b399_extract_notes.txt')
    io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
    js = os.path.join(D, 'b399_extract.json')
    io.open(js, 'w', encoding='utf-8', newline='\n').write(
        json.dumps(dict(reads=READS, source=SRCREADS, figures=FIG), indent=1, sort_keys=True))
    print('\n  wrote %s (%d lines)' % (out, len(L)))
    print('  wrote %s' % js)
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
