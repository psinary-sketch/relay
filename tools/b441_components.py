# -*- coding: utf-8 -*-
"""b441_components.py -- THE COMPONENTS. ### **RUN AFTER THE LOCK, NEVER BEFORE.**

### ### **COMPONENT 1** -- three lines restated, the kernel half quoted, the counting half measured by
### two routes that share no code, against tolerances the face stated first.
### ### **COMPONENT 2** -- five verified-source statements priced, each with its source's own
### quantifier; site (ii)'s two failure steps quoted and read against the identification.
### ### **COMPONENT 3** -- (i) the pole's double role, from b440's banked record only; (ii) the push-side
### predicate of every suite b430-b440, READ FROM GIT HISTORY AS FIRST COMMITTED; (iii) the lore's text,
### written by `b441_filings.py`, not here.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
CC = os.path.join(D, 'b328_source_text.txt')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
OUT = os.path.join(D, 'b441_components.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
MISS = []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('=' * 100)
    rec('  ### ### **%s -- %s**' % (n, t))
    rec('=' * 100)


def sub(t):
    rec('')
    rec('-' * 100)
    rec('  ### %s' % t)
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def wrap(s, n=84):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, after=0, clip=600, indent='      '):
    lines = read(path).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rel = os.path.relpath(path, os.path.dirname(os.path.dirname(path))).replace(os.sep, '/')
            rec('%s%s:%d' % (indent, rel, i + 1))
            for b in lines[i:i + after + 1]:
                for c in wrap(b.strip()[:clip], 82):
                    rec('%s  | %s' % (indent, c))
            return i + 1
    MISS.append('%s : %r' % (os.path.basename(path), needle[:50]))
    rec('%s### **NOT LOCATED** : %s' % (indent, needle[:60]))
    return None


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return (r.stdout or b'').decode('utf-8', 'replace').replace(chr(13) + NL, NL)


# ### ==============================================================================================
def component_1():
    head('COMPONENT 1', 'THE IDENTIFICATION FILED AS ABSENT, NOT AS DENIED')

    sub('b440`S THREE NEAR LINES -- EACH QUOTED WHOLE, EACH SAID IN ONE SENTENCE (`K` BAR 2)')
    LINES = [
        (os.path.join(PP, 'SPIRAL_MAP.md'), 'its `W` is a prime-power COUNTING FUNCTION',
         'It DENIES that SIDE-window`s `W` -- a function counting PRIME POWERS -- is related to '
         '`W_2`/`W_inf`, a true disclaimer about a name collision; it says NOTHING about the zeros or '
         'about any density of them, so it neither denies nor asserts the identification.'),
        (os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                      'FINDINGS-archive-1-entries-through-2026-08-20c.md'),
         'NO open term: the odd-sector W_inf mass',
         'It is an open-term inventory for a different sector decomposition, in which `W_inf` names '
         'an odd-sector mass and `density` belongs to the even sector`s epsilon question; it makes no '
         'statement about `h+` as a counting density.'),
        (os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                      'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'),
         "ERA ANNOTATIONS FOLDED WITH PROVENANCE, NO §-TEXT REWRITTEN:** the sign reconciliation's",
         'It is an era-annotation list that cites the sign reconciliation`s `W_inf` repair by name; '
         'it states no density and no identification.'),
    ]
    for path, ndl, said in LINES:
        rec('')
        quote(path, ndl, clip=900)
        rec('      ### **WHAT IT SAYS:**')
        for c in wrap(said, 84):
            rec('        %s' % c)
    rec('')
    rec('    ### ### **`SPIRAL_MAP.md:114` IS LEFT UNEDITED.** ### It is true, and it is about a different')
    rec('    ### object. ### **THE DISTINCTION:** a prime-power counting function (SIDE-window`s `W`) and a')
    rec('    ### zero-ordinate counting density (`h+/2 pi`) count different point sets.')
    rec('    ### ### **AND THE SENTENCE THAT CALLED IT A DENIAL WAS THIS SEAT`S** -- `b440_components.py`')
    rec('    ### and b440`s closing record -- and the navigator`s premise repeated it (`K` BAR 1).')
    txt440 = read(os.path.join(D, 'b440_components.txt')) + read(os.path.join(D, 'b440_closing.txt'))
    rec('      the phrase in b440`s own records : %d occurrence(s)'
        % len(re.findall(r'DENIES THE', txt440)))

    sub('THE KERNEL HALF -- A VERIFIED SOURCE`S STATEMENT, QUOTED (`K` BAR 4)')
    quote(CC, 'The function h`p', after=1, clip=200)
    quote(CC, 'It is the derivative of 2', after=4, clip=200)
    rec('    ### **AND THE RECORD HAS CARRIED IT:** b333`s survey quoted this line and b333 filed the digamma')
    rec('    ### kernel under row S1, constituent K5, at DERIVES-ON-IMPORTS:')
    quote(os.path.join(D, 'b333_extract_notes.txt'), 'It is the derivative of 2', clip=240)
    quote(os.path.join(PP, 'FACES_LEDGER.md'), '(152)–(153) the digamma kernel', clip=300)
    rec('    ### ### **SO THE KERNEL HALF IS CARRIED -- IN RELAY`S BANKS AND AT K5 -- AND b440`S "NOT CARRIED')
    rec('    ### ### BY THE CORPUS" HELD ONLY OVER PLACE-papers PROSE** (`K` BAR 3).')
    rec('    ### It stays CC`s statement; this act checks it numerically below and grades it no higher.')

    sub('THE COUNTING HALF -- TWO ROUTES THAT SHARE NO CODE, AGAINST TOLERANCES STATED ON THE FACE')
    from mpmath import mp, mpf, mpc, log, pi, digamma, loggamma, quad, im, re as mre
    mp.dps = 40
    rec('    ### ROUTE A : `INT_0^T h+(u)/(2 pi) du` by `mpmath.quad` over `digamma` (b440`s route)')
    rec('    ### ROUTE B : `theta(T)/pi`, `theta(T) = Im loggamma(1/4 + iT/2) - (T/2) log pi`, NO QUADRATURE,')
    rec('    ###           NO `digamma`')
    rec('    ### TOLERANCE 1 (face, BAR 5) : |A - B| < 1e-12 at every T')
    rec('    ### TOLERANCE 2 (face, BAR 5) : |deficit x 48 pi T - 1| < 1e-6 at every T >= 1000')
    rec('')
    rec('      %-7s %-26s %-26s %-10s %-22s %s' % ('T', 'route A', 'route B', '|A-B|',
                                                   '1-(RvM-B)', 'x 48 pi T'))
    rows, ok1, ok2 = [], True, True
    for Tt in (50, 100, 500, 1000, 5000, 20000):
        A = quad(lambda u: (mre(digamma(mpc(mpf(1) / 4, u / 2))) - log(pi)) / (2 * pi), [0, Tt])
        th = im(loggamma(mpc(mpf(1) / 4, mpf(Tt) / 2))) - (mpf(Tt) / 2) * log(pi)
        B = th / pi
        rvm = mpf(Tt) / (2 * pi) * log(mpf(Tt) / (2 * pi)) - mpf(Tt) / (2 * pi) + mpf(7) / 8
        deficit = 1 - (rvm - B)
        scaled = deficit * 48 * pi * Tt
        dAB = abs(A - B)
        ok1 = ok1 and dAB < mpf('1e-12')
        if Tt >= 1000:
            ok2 = ok2 and abs(scaled - 1) < mpf('1e-6')
        rec('      %-7d %-26s %-26s %-10.2e %-22s %s'
            % (Tt, mp.nstr(A, 20), mp.nstr(B, 20), float(dAB), mp.nstr(deficit, 12),
               mp.nstr(scaled, 12)))
        rows.append(dict(T=Tt, routeA=str(A), routeB=str(B), absdiff=float(dAB),
                         deficit=str(deficit), scaled=str(scaled)))
    rec('')
    rec('      ### ### **TOLERANCE 1 : %s. ### TOLERANCE 2 : %s.**'
        % ('MET' if ok1 else 'NOT MET', 'MET' if ok2 else 'NOT MET'))
    rec('      ### The residual in the last column is the `O(T^-3)` term, `7/(5760 pi T^3)`, which moves')
    rec('      ### `x 48 pi T` by `7 x 48 / (5760 T^2)` -- `5.8e-08` at `T = 1000` -- the floor BAR 5 names.')
    rec('')
    rec('    ### ### **THE COUNTING HALF, AS MEASURED:** `RvM main term - theta(T)/pi = 1 - 1/(48 pi T)')
    rec('    ### ### + O(T^-3)`, by two routes sharing no code agreeing to the stated `1e-12`, the deficit')
    rec('    ### ### agreeing with `1/(48 pi T)` to `1e-6` relative at `T >= 1000`. ### **THE `1` IS THE POLE')
    rec('    ### ### OF ZETA AT `s = 1`.** ### **MEASURED -- NOT A THEOREM OF THIS RECORD** (`K` BAR 6).')
    rec('    ### And the counting half is ### **ABSENT** ### from PLACE-papers prose, from relay`s banks, and')
    rec('    ### from both verified sources: CC`s counting vocabulary counts `0`, Lagarias names no theta.')
    json.dump(dict(rows=rows, tol1_met=ok1, tol2_met=ok2),
              io.open(os.path.join(D, 'b441_routes.json'), 'w', encoding='utf-8'), indent=1)
    return ok1, ok2


# ### ==============================================================================================
def component_2():
    head('COMPONENT 2', 'WHAT THE IDENTIFICATION BUYS -- PRICED, FROM THE VERIFIED SOURCES ONLY')
    CANDS = [
        ('c1', CC, 'It is the derivative of 2', 4,
         'READ', 'the numeric check of the kernel half (b440`s route A table, and route B above)',
         'EXACT AT EVERY HEIGHT -- an identity, "defined as", with no height restriction'),
        ('c2', CC, 'its derivative', 0,
         'IMPORT', 'nothing the arc measures: the arc tabulated `h+` against `log(u/2 pi)` at six '
                   'heights (b440), and an `O(log|s|)` fixes the order and not the constant',
         'UNIFORM FOR LARGE HEIGHT ONLY IN THE O-SENSE -- the source says "when |s| -> infinity"'),
        ('c3', CC, 'Binet', 3,
         'IMPORT plus a derivation', 'b440`s table of `h+` against `log(u/2 pi)` and its `O(u^-2)` '
                                     'reading -- Binet`s formula would derive the expansion rather '
                                     'than measure it',
         'NOT STATED BY THE SOURCE -- CC quotes the formula only as a tool, "One controls the growth '
         'of the higher derivatives of theta by using Binet`s first formula", and states no domain in '
         'the quoted text; the first writing of this line called it exact at every height, which was '
         'this seat`s and not CC`s, and the suite`s uniformity arm caught it'),
        ('c4', LAG, '(4) The counting function N', 6,
         'IMPORT', 'nothing measured: b351`s census counts instances and this states their count',
         'UNIFORM FOR LARGE HEIGHT IN THE O-SENSE -- "as T -> infinity", "the O-constant depends on pi"'),
        ('c5', LAG, 'The zero-counting estimate in Theorem 2.1(4) implies', 1,
         'IMPORT', 'nothing measured',
         'UNIFORM IN THE O-SENSE -- "at height T", "the O-constant depends on the representation"'),
    ]
    price = []
    for cid, path, ndl, after, kind, repl, unif in CANDS:
        sub('(%s)' % cid)
        at = quote(path, ndl, after=after, clip=220)
        if at is None:
            rec('      ### **NOT QUOTABLE -- DROPPED FROM THE PRICE** (section (S)).')
            continue
        rec('      price     : %s' % kind)
        rec('      replaces  : %s' % repl)
        rec('      uniformity: %s' % unif)
        price.append(dict(id=cid, source=os.path.basename(path), line=at, price=kind,
                          replaces=repl, uniformity=unif))

    sub('SITE (ii)`S OWN FAILURE STEPS, QUOTED FROM THE WRITER`S b427 BLOCK')
    quote(os.path.join(PP, 'FACES_LEDGER.md'), '| **B3** the density theorems', clip=900)
    quote(os.path.join(PP, 'FACES_LEDGER.md'), '| **B5** the Riemann-von Mangoldt main term', clip=600)
    rec('')
    rec('    ### ### **B3 -- DOES THE IDENTIFICATION CHANGE THE STEP? NO.** ### I-7`s screen asks one question')
    rec('    ### of a statistic`s DEFINITION: *does it contain the zeros` REAL PARTS?* ### `h+/2 pi` is built')
    rec('    ### from the gamma factor alone and contains no zero at all; `N(T)` counts zeros by ORDINATE.')
    rec('    ### ### **SO THE IDENTIFIED CHANNEL IS DENSITY-REGISTER BY CONSTRUCTION, AND IDENTIFYING IT AS THE')
    rec('    ### ### ORDINATE DENSITY CONFIRMS THE SPLIT RATHER THAN CROSSING IT.** ### B3 stands at S2.')
    rec('    ### ### **B5 -- DOES IT CHANGE THE STEP? NO, THOUGH IT CHANGES WHAT B5 IS.** ### After this act the')
    rec('    ### main term is the corpus`s own integrated channel plus the pole. ### But c4 and c5, the')
    rec('    ### uniform statements, are still COUNTS: a count uniform in the height says how many instances')
    rec('    ### lie below every height, and still places none. ### **B5 stands at S3, INSTANCES NOT A CLASS.**')
    uniform = [p['id'] for p in price if 'EVERY HEIGHT' in p['uniformity'] or 'O-SENSE' in p['uniformity']]
    exact = [p['id'] for p in price if 'EVERY HEIGHT' in p['uniformity']]
    unstated = [p['id'] for p in price if 'NOT STATED' in p['uniformity']]
    rec('')
    rec('      candidates quotable : %d of 5 ; exact at every height : %s ; uniform only in the O-sense : %s ; not stated : %s'
        % (len(price), exact, [x for x in uniform if x not in exact], unstated))
    rec('    ### **NOTHING IMPORTED, NO CELL REPLACED, NO SITE REOPENED.**')
    json.dump(dict(candidates=price, B3='STANDS', B5='STANDS', exact=exact),
              io.open(os.path.join(D, 'b441_price.json'), 'w', encoding='utf-8'), indent=1)
    return price


# ### ==============================================================================================
def component_3():
    head('COMPONENT 3', 'TWO FILINGS AND ONE MEASUREMENT')

    sub('(i) THE POLE`S DOUBLE ROLE -- FROM b440`S BANKED RECORD, AND NO FURTHER')
    B440 = os.path.join(D, 'b440_components.txt')
    for ndl in ('THE LAWFULNESS CONDITION `h-hat(i/2) = 0`',
                'THE `1` IS THE POLE OF ZETA AT `s = 1`',
                'IT IS EXACTLY `(1 + 1/c) / 2`'):
        quote(B440, ndl, clip=240)
    quote(os.path.join(T, 'b317_smear.py'), 'test function is the single condition', clip=200)
    rec('')
    rec('    ### ### **THE FILING, AT THE GRADE THOSE LINES SUPPORT:** the aim`s second moment condition is the')
    rec('    ### lawfulness condition, which is the requirement that the test function not register the pole')
    rec('    ### (READ, the instrument`s header, eq. (54)); the constant separating the integrated channel from')
    rec('    ### the classical main term is that pole (MEASURED, Component 1); and that same condition is what')
    rec('    ### breaks the seed family`s self-similarity, by the exact factor `(1 + 1/c)/2` (MEASURED at b439,')
    rec('    ### the factor derived at b440 and checked to nine figures). ### **SO THE OBJECT THAT BREAKS THE')
    rec('    ### SELF-SIMILARITY IS THE OBJECT THE COUNTING FORMULA CARRIES AS ITS CONSTANT.** ### A')
    rec('    ### juxtaposition of three graded lines; ### **NO MECHANISM LINKING THEM IS CLAIMED.**')

    sub('(ii) THE PUSH-SIDE DEFECT`S REACH -- READ FROM GIT HISTORY AS FIRST COMMITTED (`K` BAR 8)')
    rec('    ### For each act: the push-side predicate in its suite AS FIRST COMMITTED; every commit that')
    rec('    ### touched its pre-push file; the header of the pre-push file as FIRST committed; whether the')
    rec('    ### banked pre-push and post-push files differ.')
    rec('')
    rec('      %-5s %-34s %-9s %-10s %-10s %-9s %s'
        % ('act', 'predicate as first committed', 'pre-cmts', 'pre head', 'post head', 'differ', 'readings'))
    reach = []
    for n in range(430, 441):
        tool = 'tools/b%d_checks.py' % n
        first = git(ROOT, 'log', '--reverse', '--format=%H', '--', tool).split()
        src = git(ROOT, 'show', '%s:%s' % (first[0], tool)) if first else ''
        m = re.search(r'def _pushed\(\):(.*?)\n(?=\S)', src, re.S)
        body = m.group(1) if m else ''
        kind = ('branch --contains, SHA in names' if "'--contains'" in body else
                'act subject + merge-base' if ('is-ancestor' in body and "not in subj" in body) else
                'merge-base only' if 'is-ancestor' in body else
                'remote ref == HEAD' if "'origin/main'" in body else
                ('NONE -- one output path' if ('POSTPUSH' not in src and 'checks.txt' in src)
                 else 'NOT LOCATED'))
        prec = git(ROOT, 'log', '--format=%h', '--', 'data/b%d_checks.txt' % n).split()
        firstpre = (git(ROOT, 'show', '%s:data/b%d_checks.txt' % (prec[-1], n)) if prec else '')
        post = read(os.path.join(D, 'b%d_checks_postpush.txt' % n))
        pre = read(os.path.join(D, 'b%d_checks.txt' % n))
        hpre = re.search(r'(PRE-PUSH|POST-PUSH)', firstpre[:600])
        hpost = re.search(r'(PRE-PUSH|POST-PUSH)', post[:600])
        differ = (pre != post)
        two = differ and not (hpre and hpre.group(1) == 'POST-PUSH')
        rec('      b%-4d %-34s %-9d %-10s %-10s %-9s %s'
            % (n, kind, len(prec), hpre.group(1) if hpre else 'no header',
               hpost.group(1) if hpost else 'no header', differ, 'TWO' if two else 'ONE'))
        reach.append(dict(act='b%d' % n, predicate_first_committed=kind, pre_commits=prec,
                          pre_header_first=hpre.group(1) if hpre else None,
                          post_header=hpost.group(1) if hpost else None, differ=differ,
                          readings='TWO' if two else 'ONE'))
    broken = [r['act'] for r in reach if r['predicate_first_committed'].startswith('branch')]
    nopred = [r['act'] for r in reach if r['predicate_first_committed'].startswith('NONE')]
    rec('')
    rec('      ### ### **SUITES FIRST COMMITTED WITH NO PUSH-SIDE PREDICATE AT ALL : %s**' % nopred)
    rec('    ### b430 is the origin incident: its first suite wrote one file, the post-push run overwrote the')
    rec('    ### pre-push record in the working tree, and the commit `2be1943` had already banked the pre-push')
    rec('    ### reading; `81127eb` added the predicate and the second file. ### b440 wrote the broken')
    rec('    ### predicate, its post-push runs overwrote `b440_checks.txt` in the working tree TWICE, and both')
    rec('    ### times the committed pre-push blob from `74808c7` was restored before any further commit.')
    rec('    ### ### **IN BOTH, THE BANK`S PRE-PUSH READING IS THE ONE COMMITTED BEFORE THE PUSH -- EACH')
    rec('    ### ### PRE-PUSH FILE WAS COMMITTED EXACTLY ONCE -- AND IN BOTH, ONLY THE COMMIT SAVED IT.**')
    multi = [(r['act'], len(r['pre_commits'])) for r in reach if len(r['pre_commits']) > 1]
    one = [r['act'] for r in reach if r['readings'] == 'ONE']
    rec('')
    rec('      ### ### **SUITES WHOSE FIRST-COMMITTED PREDICATE WAS THE BROKEN ONE : %s**' % broken)
    rec('      ### ### **PRE-PUSH FILES TOUCHED BY MORE THAN ONE COMMIT : %s**' % multi)
    rec('      ### ### **ACTS WHOSE BANK SHOWS ONE READING : %d of %d %s**' % (len(one), len(reach), one))
    rec('')
    rec('    ### **WHAT THE LIST SAYS, AND NOTHING IS RE-VERDICTED:** the broken predicate was committed in')
    rec('    ### b440`s suite alone -- a regression this seat wrote when it typed b440`s suite fresh instead of')
    rec('    ### carrying b439`s `merge-base` predicate, which is `(R46)`\'s species exactly: a cure that lived')
    rec('    ### in one tool per act, and was dropped the first time a tool was not copied. ### b440`s closing')
    rec('    ### sentence -- *"b430`s defect, still live in every act since"* -- is ### **FALSE, AND CORRECTED')
    rec('    ### HERE**; b440`s bank is not edited.')
    rec('')
    rec('    ### ### **AND WHY THE DISCIPLINE EXISTS:** a pre-push reading is the suite`s verdict on the tree')
    rec('    ### ### BEFORE the work reached the remote. ### If the post-push run lands in the same file, the')
    rec('    ### ### banked verdict is dated by the commit after it, and nobody can tell from the bank whether')
    rec('    ### ### the act was clean before it pushed or only afterward. ### **TWO READINGS IN TWO FILES')
    rec('    ### ### ARE HOW A VERDICT KEEPS ITS DATE.**')
    sub('(ii, continued) THE PREDICATE b440 LEFT IN ITS TREE, AND WHAT IT DID TO THIS ACT')
    wt = read(os.path.join(T, 'b440_checks.py'))
    m = re.search(r'def _pushed\(\):(.*?)\n(?=\S)', wt, re.S)
    rec('    ### b440`s suite at HEAD decides the side by: %s'
        % ("remote ref == HEAD" if m and "'origin/main'" in m.group(1) and 'subj' not in m.group(1)
           else 'something else'))
    head_sha = git(ROOT, 'rev-parse', 'HEAD').strip()
    remote = git(ROOT, 'rev-parse', 'origin/main').strip()
    subj = git(ROOT, 'log', '-1', '--format=%s').strip()
    rec('    ### measured now, BEFORE this act commits : HEAD == origin/main is %s ; HEAD`s subject names '
        'b441 : %s' % (head_sha == remote, 'b441' in subj))
    rec('    ### ### **SO THAT PREDICATE CALLS AN UNCOMMITTED TREE PUSHED.** ### It is b434`s documented')
    rec('    ### species -- *"HEAD is trivially on the remote"* -- retyped by this seat at b440 as a repair.')
    rec('    ### b440 escaped it only because its pre-push reading was already committed when the repair')
    rec('    ### landed. ### **b441 DID NOT ESCAPE IT:** its suite, typed from b440`s helpers, wrote its first')
    rec('    ### pre-push reading into the POST-push file. That file, as written before any b441 commit:')
    mis = read(os.path.join(D, 'b441_checks_postpush.txt'))
    for ln in mis.splitlines()[:3] + [x for x in mis.splitlines() if 'ARMS RUN' in x]:
        rec('      | %s' % ln)
    rec('    ### ### **AND THE LOCKED FACE ENCODES THE SAME DEFECT** -- BAR 11 and arm')
    rec('    ### `G-PUSH-SIDE-BY-REMOTE-REF` name the rule as *"the push side decided by the remote ref"*.')
    rec('    ### The face is not edited; the suite now carries b439`s predicate -- a commit naming THIS act')
    rec('    ### made and on the remote -- and the arm checks that, with this breach printed beside it.')
    rec('    ### **THE REACH TABLE ABOVE IS OF PREDICATES AS FIRST COMMITTED; THIS SECTION ADDS THE ONE LEFT')
    rec('    ### IN b440`S TREE, WHICH NO COMMITTED PRE-PUSH FILE OF b430-b440 WAS WRITTEN UNDER.**')
    json.dump(reach, io.open(os.path.join(D, 'b441_reach.json'), 'w', encoding='utf-8'), indent=1)

    sub('(iii) THE AXIOM-FORM LORE -- WRITTEN BY `b441_filings.py` INTO TECHNE-Core, LOCAL')
    rec('    ### The incident, quoted from b440`s own axiom profile:')
    for ndl in ("'edge_16' depends on axioms", "'edge_16_bool' does not depend"):
        quote(B440, ndl, clip=160)
    quote(os.path.join(PP, 'README.md'), 'Axiom profiles are recorded at the corpus', after=2, clip=200)
    return broken, one, reach


def main():
    rec('=' * 100)
    rec('b441 -- THE IDENTIFICATION FILED, THE OVERSTATEMENT CORRECTED, AND TWO FILINGS.')
    rec('### ### **THE COMPONENTS. ### RUN AFTER THE LOCK.**')
    rec('=' * 100)
    ok1, ok2 = component_1()
    price = component_2()
    broken, one, reach = component_3()
    rec('')
    rec('=' * 100)
    rec('  ### ### **COMPONENT 1 : kernel half CARRIED (CC 153-154, b333, K5) ; counting half ABSENT and MEASURED,')
    rec('  ### ### tolerance 1 %s, tolerance 2 %s ; SPIRAL_MAP.md:114 UNEDITED.**'
        % ('MET' if ok1 else 'NOT MET', 'MET' if ok2 else 'NOT MET'))
    rec('  ### ### **COMPONENT 2 : %d of 5 candidates quotable ; B3 STANDS ; B5 STANDS.**' % len(price))
    rec('  ### ### **COMPONENT 3(ii) : broken predicate first committed in %s ; one-reading banks %d of %d.**'
        % (broken, len(one), len(reach)))
    rec('  ### MISSES : %d %s' % (len(MISS), MISS or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
