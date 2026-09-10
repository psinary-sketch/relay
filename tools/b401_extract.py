# -*- coding: utf-8 -*-
"""b401_extract.py -- THE SURVEY THE FACE IS WRITTEN FROM. ### **A READ, AND NOTHING ELSE.**

### ### **WHAT THIS LEG IS.** ### `b400` typed `(Q400)` and named its one absent element -- any
### statement evaluating or bounding `SUM_p W_p(f)` at `a^2 >= 2` against an archimedean quantity --
### and it named that element absent ### **FROM A CONSTRAINT SET AND NOT FROM A SEARCH.** ### This
### leg searches. ### **A LIMIT FOUND BY A MATCHER IS A PROPERTY OF THE MATCHER UNTIL A SECOND
### ### SHAPE HAS BEEN TRIED**, so every matcher here prints its whole yield and the residue is
### hand-read in the components.

### ### **AND THE ORDER PUTS THE UNIFORMITY QUESTION BEFORE THE FOURTH SITE**, because the answer
### decides whether `(Q400)` is a fourth instance of the obstruction or the first crack in it.

### ### **THE INSTRUMENT LANE IS PARKED, SO NO KERNEL IS BUILT.** ### `SIDE-window`'s axiom profile
### is read from ### **THE PROFILE THE REPOSITORY PRINTS IN ITS OWN README AND FROM THE `#print
### ### axioms` LINES ITS OWN CHECK FILES CARRY** -- not from a run. ### That is a weaker reading
### than a build and this file says so rather than letting a quoted headline pass for a measurement.
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import b305_source as S5        # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SW = os.path.join('D:', os.sep, 'SIDE-window')
FL = os.path.join(PP, 'FACES_LEDGER.md')
RM = os.path.join(SW, 'README.md')

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
        rec('      ### **%s**' % v)
    return i, ln


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
    out = {}
    for key, sha, nby, cite in [
            ('CC', CC_SHA, CC_BYTES, 'Connes & Consani, arXiv:2006.13771v1'),
            ('LG', LG_SHA, LG_BYTES, 'J. C. Lagarias, arXiv:math/0404394v4')]:
        hits, scanned = acquire(sha, nby)
        rec('  ### **%s** -- %s' % (key, cite))
        rec('      banked pin : %d bytes, sha256 `%s`' % (nby, sha))
        rec('      files of that size examined by digest : %d ; byte-identical copies : %d'
            % (scanned, len(hits)))
        if hits:
            got = sha256_file(hits[0])
            rec('      re-computed digest : `%s`' % got)
            rec('      ### ### **VERDICT : VERIFIED.** ### `got == banked : %s`' % (got == sha))
            out[key] = hits[0]
        else:
            rec('      ### ### **VERDICT : HALT.** ### No copy matches the pin.')
            out[key] = None
        rec()
    FIG['sources'] = {k: bool(v) for k, v in out.items()}
    return out


def pdf_pages(p):
    from pypdf import PdfReader
    return [S5.flatten(pg.extract_text() or '') for pg in PdfReader(p).pages]


def qsrc(pages, needle, label, after=560, tag=''):
    nn = S5.flatten(needle)
    found = [(i, t[t.find(nn):t.find(nn) + after]) for i, t in enumerate(pages, 1) if nn in t]
    SRCREADS.append(dict(label=flat(label, 160), needle=nn[:90], tag=tag,
                         pages=[i for i, _ in found]))
    rec('    %s' % label)
    if found:
        i, txt = found[0]
        rec('      ### page index `%d` -- %d hit(s) : %s' % (i, len(found), [x for x, _ in found]))
        rec('      > %s' % txt[:after])
    else:
        rec('      ### **NOT LOCATED IN THE VERIFIED ARTEFACT.**')
    rec()
    return found


# ==================================================================================================
#  COMPONENT 1 -- THE SEARCH. ### **THE MATCHER PRINTS ITS WHOLE YIELD.**
# ==================================================================================================
def survey1(src):
    bar('=')
    rec('  ### (1) COMPONENT 1 -- THE ABSENT ELEMENT, SEARCHED FOR RATHER THAN ASSUMED ABSENT.')
    bar('=')
    rec('  ### **WHAT IS BEING SEARCHED FOR, STATED BEFORE THE SEARCH SO THE YIELD CAN BE JUDGED')
    rec('  ### ### AGAINST IT:** ### any statement EVALUATING or BOUNDING a finite-place sum at a')
    rec('  ### support wide enough that primes enter, against a quantity of another kind.')
    rec('  ### ### **`b400` CALLED THIS ABSENT FROM A CONSTRAINT SET. ### THIS IS THE SEARCH.**')
    rec()
    rec('  --- **(1a) THE SOURCES, BY CONTENT.** ---')
    if src.get('CC'):
        pages = pdf_pages(src['CC'])
        rec('    CC pages flattened : %d' % len(pages))
        rec()
        qsrc(pages, 'so that rational primes are not involved',
             '### **(S1) THE NARROW WINDOW, AND WHY IT IS NARROW**', tag='CC-narrow')
        qsrc(pages, 'the support condition',
             '### **(S2) THE WIDENING THE SOURCE NAMES -- `Support(f) SUBSET (p^-1, p)`**',
             tag='CC-widen')
        qsrc(pages, 'have support in the interval',
             '### **(S3) THEOREM 1`S SUPPORT HYPOTHESIS**', after=300, tag='CC-thm1')
        qsrc(pages, 'suchthatforanygpc8cpr212212sq',
             '### **(S4) THEOREM 6.11 AND ITS CORRECTION TERM `c` WITH `13 < c < 17`**',
             after=420, tag='CC-thm611')
        qsrc(pages, 'a fixed compact interval',
             '### **(S5) THE ESSENTIAL NEGATIVITY, ON A FIXED COMPACT INTERVAL**',
             after=520, tag='CC-fixedI')
        qsrc(pages, 'for small enough intervals',
             '### **(S6) AND WHERE THE SOURCE`S OWN PRELIMINARY POSITIVITY HOLDS**',
             after=320, tag='CC-small')
        qsrc(pages, 'a positivity result for the distribution',
             '### **(S7) APPENDIX B ON WHERE THE ARCHIMEDEAN POSITIVITY IS PROVEN**',
             after=320, tag='CC-appB')
    if src.get('LG'):
        pages = pdf_pages(src['LG'])
        rec('    Lagarias pages flattened : %d' % len(pages))
        rec()
        qsrc(pages, 'we obtain a bound for',
             '### **(S8) SECTION 6 -- A BOUND FOR THE FINITE-PLACE CONTRIBUTION**',
             after=760, tag='LG-thm61')
        qsrc(pages, 'we obtain an unconditional estimate for the finite place',
             '### **(S9) THE ABSTRACT`S OWN SENTENCE ABOUT IT**', after=420, tag='LG-abstract')
        qsrc(pages, 'there is a constant',
             '### **(S10) THEOREM 5.1 -- THE ARCHIMEDEAN HALF, FOR CONTRAST**',
             after=420, tag='LG-thm51')
    rec()
    rec('  --- **(1b) THE CORPUS, BY A MATCHER WHOSE WHOLE YIELD IS PRINTED.** ---')
    pats = [('bound.{0,40}prime sum', 'a bound on the prime sum'),
            ('bound.{0,40}finite.place', 'a bound on the finite places'),
            ('SUM_p W_p.{0,30}<=', 'the prime sum bounded above'),
            ('unconditional.{0,60}(bound|estimate)', 'an unconditional bound or estimate'),
            ('widen.{0,40}(support|window)', 'a widened support or window')]
    files = []
    for base in (D, PP):
        for dp, _dn, fn in os.walk(base):
            if '.git' in dp or 'archive' in dp:
                continue
            for f in fn:
                if f.endswith('.txt') or f.endswith('.md'):
                    files.append(os.path.join(dp, f))
    rec('    files in scope : %d  (relay `data/` and the papers repository, `.txt` and `.md`)'
        % len(files))
    yields = {}
    for pat, lbl in pats:
        rx = re.compile(pat, re.I)
        hits = []
        for p in files:
            try:
                txt = io.open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            for i, ln in enumerate(txt.split(chr(10)), 1):
                if rx.search(ln):
                    hits.append((os.path.basename(p), i, flat(ln, 150)))
        yields[lbl] = hits
        rec('    ### matcher `%s` -- **%s** : ### **%d HIT(S)**' % (pat, lbl, len(hits)))
        for h in hits[:14]:
            rec('        %-42s :%-6d %s' % (h[0][:42], h[1], h[2][:110]))
        if len(hits) > 14:
            rec('        ### ... and %d more, all in the run record` s json' % (len(hits) - 14))
    FIG['yields'] = {k: len(v) for k, v in yields.items()}
    FIG['yield_rows'] = {k: v[:60] for k, v in yields.items()}
    rec()
    rec('  --- **(1c) WHAT THE RECORD ALREADY OWNS, BEFORE THIS ACT CLAIMS ANYTHING.** ---')
    q(os.path.join(D, 'b358_closing.txt'), 'NO UNCONDITIONAL BOUND AT ALL',
      '### `b358` ALREADY READ LAGARIAS `6.1` AND BANKED A VERDICT ON IT', 400)
    q(os.path.join(D, 'b358_the_li_asymptotics.txt'), 'H-CUSP',
      '### and `b358` graded the CUSPIDALITY hypothesis on the corpus`s own object', 300)
    q(os.path.join(D, 'b361_the_held_item.txt'), 'IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT',
      '### `b361` INHERITED it and did not decide it', 300)
    rec()


# ==================================================================================================
#  ADDITION ONE -- THE UNIFORMITY QUESTION.
# ==================================================================================================
def survey2(src):
    bar('=')
    rec('  ### (2) ADDITION ONE -- THE UNIFORMITY QUESTION, ASKED OF WHAT (1) LOCATES.')
    bar('=')
    rec('  ### The order: *quote its correction term and state, from the theorem`s own text,')
    rec('  ### whether that term depends on the prime or is uniform in it.*')
    rec()
    if src.get('LG'):
        pages = pdf_pages(src['LG'])
        qsrc(pages, 'in which the implied constant',
             '### **(S11) THE CORRECTION TERM`S OWN SENTENCE, WORD FOR WORD**',
             after=340, tag='LG-implied')
    if src.get('CC'):
        pages = pdf_pages(src['CC'])
        qsrc(pages, 'the best constant',
             '### **(S12) AND CC`S OWN CORRECTION CONSTANT, FOR CONTRAST**',
             after=300, tag='CC-bestc')
    rec()


# ==================================================================================================
#  ADDITION TWO -- THE CORPUS'S OWN ONE-PRIME WINDOW, READ WHOLE.
# ==================================================================================================
def survey3():
    bar('=')
    rec('  ### (3) ADDITION TWO -- THE CORPUS`S OWN ONE-PRIME WINDOW, READ WHOLE AND NOT BY NAME.')
    bar('=')
    rec('  --- **(3a) THE ACT THAT BUILT IT.** ---')
    q(os.path.join(D, 'b16_2026-08-18.txt'), 'the archimedean support bound a (window',
      '### `b16`: the archimedean support bound and the effective cutoff', 340)
    q(os.path.join(D, 'b16_2026-08-18.txt'), 'a^2 = 2.0  -> effective cutoffs',
      '### `b16`: the staircase`s second step IS the one-prime rung', 300)
    rec()
    rec('  --- **(3b) THE KERNEL`S OWN README: WHAT IT CLAIMS.** ---')
    q(RM, 'window_one_prime', '### the one-prime terminal, as the README states it', 300)
    q(RM, 'all 43 terminals are fully axiom-free', '### the axiom headline', 320)
    rec()
    rec('  --- **(3c) THE KERNEL`S OWN README: WHAT IT DISCLAIMS.** ---')
    q(RM, 'Nothing here bears on the sign of',
      '### ### **THE DISCLAIMER THAT DECIDES ADDITION TWO**', 340)
    q(RM, 'HAS NOTHING TO DO WITH THE CORPUS', '### and the name collision, flagged by the repo',
      300)
    q(RM, 'It proves nothing about real intervals', '### and what it proves instead', 340)
    q(RM, 'the lower endpoint never binds', '### and the windows are HALF-VACUOUS', 340, span=True)
    q(RM, 'tabulated, not characterized', '### `W` is tabulated, not characterized', 300)
    rec()
    rec('  --- **(3d) THE AXIOM PROFILE, READ FROM A PRINTED PROFILE AND NOT FROM A RUN.** ---')
    rec('  ### ### **THE INSTRUMENT LANE IS PARKED, SO NOTHING IS BUILT HERE.** ### What is')
    rec('  ### available is the profile the repository PRINTS -- its README`s quoted block, and the')
    rec('  ### `#print axioms` invocations its own check files carry. ### **A QUOTED HEADLINE IS')
    rec('  ### ### NOT A MEASUREMENT AND THIS SURVEY SAYS SO.**')
    tot = 0
    per = {}
    for f in sorted(os.listdir(SW)):
        if f.startswith('AxiomCheck') and f.endswith('.lean'):
            txt = io.open(os.path.join(SW, f), encoding='utf-8', errors='replace').read()
            n = len(re.findall(r'#print\s+axioms', txt))
            per[f] = n
            tot += n
            rec('      %-32s `#print axioms` invocations : %d' % (f, n))
    rec('      ### ### **TOTAL `#print axioms` INVOCATIONS IN THE REPOSITORY : %d**' % tot)
    rec('      ### ### **AND THE README`S HEADLINE SAYS `43` TERMINALS.**')
    FIG['axiom_prints'] = per
    FIG['axiom_prints_total'] = tot
    heads = [ln for ln in io.open(RM, encoding='utf-8', errors='replace').read().split(chr(10))
             if ln.startswith('## ')]
    rec('      README sections : %s' % [h[3:][:34] for h in heads])
    FIG['readme_sections'] = [h[3:] for h in heads]
    rec()


# ==================================================================================================
#  COMPONENT 2 -- THE FOURTH SITE.
# ==================================================================================================
def survey4():
    bar('=')
    rec('  ### (4) COMPONENT 2 -- ROW `U1`, ITS THREE INSTANCES, AND THEIR INDICES.')
    bar('=')
    q(FL, 'U1 -- the uniformity obstruction', '### the row, whole', 1500)
    q(os.path.join(D, 'b353_the_missing_statement.txt'),
      'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION',
      '### instance (iii): the WIDTH coordinate, and its index', 300)
    rec()


def main():
    bar('=')
    rec('b401 -- THE ABSENT ELEMENT SEARCHED, AND THE FOURTH SITE. ### THE EXTRACT.')
    rec('### **A SURVEY. ### NO INSTRUMENT IS RUN AND NO KERNEL IS BUILT.**')
    bar('=')
    rec()
    src = survey0()
    survey1(src)
    survey2(src)
    survey3()
    survey4()
    bar('=')
    rec('  ### THE SURVEY, COUNTED.')
    bar('=')
    anc = sum(1 for r in READS if r['verdict'].startswith('ANCHORED'))
    loc = sum(1 for r in SRCREADS if r['pages'])
    rec('    reads            : %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d'
        % (len(READS), anc, sum(1 for r in READS if r['verdict'] == 'AMBIGUOUS'),
           sum(1 for r in READS if r['verdict'] == 'ABSENT')))
    rec('    source fragments : %d ; LOCATED %d ; NOT LOCATED %d'
        % (len(SRCREADS), loc, len(SRCREADS) - loc))
    FIG['reads'] = len(READS)
    FIG['anchored'] = anc
    FIG['srcreads'] = len(SRCREADS)
    FIG['srclocated'] = loc
    bar('=')
    p = run_clock.write(D, 'b401_extract_notes', L)
    io.open(os.path.join(D, 'b401_extract.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(dict(reads=READS, srcreads=SRCREADS, fig=FIG),
                                              indent=1, ensure_ascii=False) + chr(10))
    print('  written: %s' % os.path.basename(p))
    print('  written: b401_extract.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
