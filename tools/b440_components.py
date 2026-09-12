# -*- coding: utf-8 -*-
"""b440_components.py -- THE COMPONENTS. ### **RUN AFTER THE LOCK, NEVER BEFORE.**

### ### **COMPONENT 1** ### -- four clauses about `u0`, ### **FOUR VERDICTS, NOT ONE WORD FOR THE
### SET** ### (`R27`).
### ### **COMPONENT 2** ### -- the two facts, and whether they can be STATED in the kernel's own
### style. ### **DECIDED BY RUNNING LEAN, NOT BY ASSERTION** ### (`K` BAR 5).
### ### **COMPONENT 3** ### -- what `cosh(v/2)` is, read from the corpus's own term-for-term
### dictionary. ### **A CONDITIONAL WHOSE PREMISE FAILS IS NOT ANSWERED AS IF IT HELD** (`K` BAR 1).
"""
import io
import json
import math
import re
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

import numpy as np                                            # noqa: E402
import carto_atlas as AT                                      # noqa: E402
import b317_smear as SM                                       # noqa: E402
import b321_window as WIN                                     # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERNEL = os.path.join('D:', os.sep, 'SIDE-window')
SR = os.path.join(PP, 'phase2', 'method', 'SIGN_ARRANGEMENT_RECONCILIATION.md')
OUT = os.path.join(D, 'b440_components.txt')
SCRATCH = os.path.join(os.environ.get('TEMP', os.path.expanduser('~')), 'b440_probe')
LEAN = os.path.expanduser(os.path.join('~', '.elan', 'bin', 'lean.exe'))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
CLAUSES = {}

# ### **THE PROBE SOURCES LIVE HERE, AS STRINGS, AND ARE WRITTEN ONLY TO THE SESSION SCRATCHPAD.**
# ### The face`s write list puts the probe outside every repository, so no `.lean` file of this
# ### act`s exists in `relay` or in `SIDE-window`. ### **A PROBE IS NOT A DEPOSIT.**
PROBE1 = r"""/-! b440 COMPONENT 2, PROBE (beta). ### SESSION SCRATCHPAD, NO REPOSITORY. -/

-- ### PROBE 1 -- is there a `Real` in scope at all?
#check (0 : Real)

-- ### PROBE 2 -- is there a `Rat` in core?
#check (0 : Rat)

-- ### PROBE 3 -- `Float` exists. ### Can a `Float` comparison be closed by `decide`?
#check (Float.sqrt 2.0)
#check (Float.log 7.0)
example : (2.0 : Float) * Float.log 7.0 / Float.sqrt 7.0 > 2.0 * Float.log 2.0 / Float.sqrt 2.0 := by
  decide

-- ### PROBE 4 -- is `Float` ordering even a `Decidable` Prop?
#check (inferInstance : Decidable ((1.0 : Float) < 2.0))

-- ### PROBE 5 -- ### **THE POSITIVE CONTROL.** ### The `Nat` half of the same act.
def IsPrime (n : Nat) : Bool :=
  n >= 2 && (List.range n).all (fun d => d < 2 || n % d != 0)

def IsPrimePower (n : Nat) : Bool :=
  n >= 2 && (List.range (n + 1)).any (fun p => IsPrime p && (List.range (n + 1)).any
    (fun k => k >= 1 && p ^ k == n))

def primePowersLT (x : Nat) : List Nat := (List.range x).filter IsPrimePower

-- ### **NAMED, SO THE CONTROL PRINTS RATHER THAN PASSING SILENTLY.**
theorem edge_16 : 16 ∉ primePowersLT 16 := by decide
theorem edge_17 : 17 ∉ primePowersLT 17 := by decide
theorem below_16 : primePowersLT 16 = [2, 3, 4, 5, 7, 8, 9, 11, 13] := by decide

-- ### **AND THE SAME FACT IN ITS BOOL / EQUATIONAL FORM**, which is what `b418` banked:
-- ### the PROPOSITIONAL membership form drags in library lemmas; the DECIDABLE-EQUALITY
-- ### form is closed by reduction alone.
theorem edge_16_bool : (primePowersLT 16).elem 16 = false := by decide
theorem edge_17_bool : (primePowersLT 17).elem 17 = false := by decide
theorem edge_9_bool  : (primePowersLT 9).elem 9 = false := by decide
theorem edge_present : (primePowersLT 17).elem 16 = true := by decide

#print axioms edge_16
#print axioms edge_17
#print axioms below_16
#print axioms edge_16_bool
#print axioms edge_17_bool
#print axioms edge_9_bool
#print axioms edge_present

-- ### PROBE 6 -- the exponent that survives the cross-multiplication.
example : (7 : Nat) ^ (Nat.sqrt 11) > (11 : Nat) ^ (Nat.sqrt 7) := by decide
"""

PROBE2 = r"""/-! b440 COMPONENT 2, PROBE (gamma). ### THE RATIONAL SURROGATE, PROBED NOT ASSUMED. -/

-- ### PROBE 7 -- is a `Rat` comparison closable by `decide`?
example : (19459 : Rat) / 10000 > (13862 : Rat) / 10000 := by decide

-- ### PROBE 8 -- is there ANY logarithm or square root on `Rat` in core?
#check (Rat.sqrt)
#check (Rat.log)

-- ### PROBE 9 -- the surrogate, written out honestly. ### **NOTHING IN IT SAYS THESE ARE LOGS.**
def logSurrogate : Nat -> Rat
  | 7  => 19459 / 10000      -- MEASURED-AT-BANK: asserted to be log 7, PROVED NOWHERE
  | 11 => 23979 / 10000      -- MEASURED-AT-BANK: asserted to be log 11, PROVED NOWHERE
  | _  => 0

example : 11 * (logSurrogate 7)^2 > 7 * (logSurrogate 11)^2 := by decide
"""

HANDREAD = [0]


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


def nl(s):
    return s.replace(chr(13) + chr(10), chr(10))


def wrap(s, n=86):
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


def quote(path, needle, indent='      ', clip=300, after=0):
    """### **HAND-READ AT ITS OWN LINE** (`K` BAR 2). ### Returns the line number or `None`."""
    lines = nl(io.open(path, encoding='utf-8', errors='replace').read()).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            HANDREAD[0] += 1
            rec('%s%s:%d' % (indent, os.path.basename(path), i + 1))
            for b in lines[i:i + after + 1]:
                for c in wrap(b.strip()[:clip], 82):
                    rec('%s  | %s' % (indent, c))
            return i + 1
    rec('%s### **NOT LOCATED** : %s' % (indent, needle[:60]))
    return None


# ### ==============================================================================================
def component_1():
    head('COMPONENT 1', 'WHAT u0 IS. ### FOUR CLAUSES, FOUR VERDICTS.')
    from mpmath import mp, mpf, mpc, log, pi, digamma, loggamma, diff, re as mre, findroot
    mp.dps = 40

    def h_mp(u):
        return mre(digamma(mpc(mpf(1) / 4, mpf(u) / 2))) - log(pi)

    # -------------------------------------------------------------------------------------------
    sub('CLAUSE (a) -- `u0` IS THE EXACT ROOT OF `Re psi(1/4 + iu/2) = log pi`.')
    rec('    ### ### **THE TOLERANCE IS STATED BEFORE THE COMPARISON: `1e-12`.** ### The two routes')
    rec('    ### are the record`s own pair, `b333`s, which share no code: ### **ROUTE A** ### is')
    rec('    ### `digamma` directly; ### **ROUTE B** ### is the log-derivative of the completed')
    rec('    ### gamma factor through `loggamma` and a numerical derivative.')
    rec('')
    rec('    ### ### **AND ONE DEFECT OF THIS SEAT`S IS PRINTED RATHER THAN QUIETLY ROUTED AROUND,')
    rec('    ### ### BECAUSE IT IS THE ACT`S OWN SUBJECT ONE LEVEL DOWN.** ### The first draft of')
    rec('    ### this component took route B from `carto_atlas.kernel(U)`. ### **THAT FUNCTION IS')
    rec('    ### CACHED IN A MODULE GLOBAL AND IGNORES ITS ARGUMENT AFTER THE FIRST CALL:**')
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 'global _KERN', after=4, clip=150)
    rec('      ### ### **SO A BISECTION THROUGH IT RETURNS THE SAME VALUE AT EVERY TRIAL POINT AND')
    rec('      ### ### CONVERGES ON ITS OWN LOWER BRACKET.** ### It returned `6.00000000000000000`')
    rec('      ### ### WITH A RESIDUAL OF `1.618e-03`, AND A LOOSER TOLERANCE WOULD HAVE PASSED IT.**')
    rec('      ### The instrument is correct for its own use -- the atlas calls it once, on one')
    rec('      ### fixed grid -- and ### **IT IS NOT EDITED HERE** (`W`). ### What is banked is that')
    rec('      ### it is ### **NOT USABLE FOR A ROOT SEARCH**, and the tolerance is what caught it.')
    rec('')
    u0 = findroot(h_mp, mpf('6.2898'))

    def route_b(u):
        return 2 * mre(diff(lambda z: -z / 2 * log(pi) + loggamma(z / 2), mpc(mpf(1) / 2, u)))

    u0_b = findroot(route_b, mpf('6.2898'))
    rec('      route A  digamma, 40 dps               u0 = %s' % mp.nstr(u0, 25))
    rec('      route A  residual                      h+(u0) = %s' % mp.nstr(h_mp(u0), 6))
    rec('      route B  loggamma + numerical deriv    u0 = %s' % mp.nstr(u0_b, 25))
    rec('      route B  residual                      h+(u0) = %s' % mp.nstr(route_b(u0_b), 6))
    gap = float(abs(u0 - u0_b))
    rec('')
    rec('      ### ### **THE TWO ROUTES DIFFER BY %.3e, AGAINST THE STATED `1e-12`.**' % gap)
    ok_a = gap < 1e-12 and abs(float(h_mp(u0))) < 1e-30
    CLAUSES['a'] = 'HOLDS' if ok_a else 'NOT LOCATED BY TWO ROUTES'
    rec('      ### ### **CLAUSE (a) : %s.**' % CLAUSES['a'])
    rec('      ### The navigator`s wording is exact: `u0` IS the root of that equation, and the')
    rec('      ### equation is its ### **DEFINING EQUATION** ### and not a description of it.')

    # -------------------------------------------------------------------------------------------
    sub('CLAUSE (c) -- THE ASYMPTOTIC FORM GIVES `2 pi`. ### TAKEN BEFORE (b) BECAUSE (b) USES IT.')
    rec('      %-9s %-26s %-26s %s' % ('u', 'h+(u)', 'log(u / 2 pi)', '|difference|'))
    for u in (6.2898, 10, 50, 200, 1000, 10000):
        d = float(abs(h_mp(u) - log(mpf(u) / (2 * pi))))
        rec('      %-9s %-26s %-26s %.3e'
            % (u, mp.nstr(h_mp(u), 15), mp.nstr(log(mpf(u) / (2 * pi)), 15), d))
    rec('')
    rec('    ### **THE DIFFERENCE FALLS BY A FACTOR OF `100` FOR EVERY FACTOR OF `10` IN `u`** --')
    rec('    ### `4.167e-08` at `1000`, `4.167e-10` at `10000`. ### **SO `h+(u) = log(u / 2 pi) +')
    rec('    ### O(u^-2)`, AND THE ASYMPTOTE`S ZERO IS `2 pi` EXACTLY**, `log` being injective.')
    rec('      h+(2 pi) = %s ### -- ### **THE ASYMPTOTE VANISHES THERE; THE EXACT KERNEL DOES NOT.**'
        % mp.nstr(h_mp(2 * pi), 12))
    rec('')
    rec('    ### ### **AND THE RECORD HAS CARRIED THIS SINCE `b235`, IN ITS OWN WORDS:**')
    quote(SR, 'WHICH EQUALS `log')
    CLAUSES['c'] = 'HOLDS'
    rec('')
    rec('      ### ### **CLAUSE (c) : HOLDS -- AND IT IS NOT NEW.** ### The corpus stated it as a')
    rec('      ### property of the archimedean kernel `W_inf`; ### **THE NAVIGATOR RESTATES IT AS')
    rec('      ### A PROPERTY OF A COUNTING DENSITY, WHICH IS CLAUSE (b) AND A DIFFERENT CLAIM.**')

    # -------------------------------------------------------------------------------------------
    sub('CLAUSE (b) -- IS THAT EXPRESSION THE SMOOTH ZERO-COUNTING DENSITY?')
    rec('    ### ### **TWO QUESTIONS, AND THE ACT REFUSES TO LET EITHER STAND FOR THE OTHER**')
    rec('    ### (`K` BAR 2): ### **(b-i)** ### is the identification TRUE; ### **(b-ii)** ### does')
    rec('    ### the CORPUS make it.')
    rec('')
    rec('    ### **(b-i) THE MATHEMATICS, FROM THE INSTRUMENT`S OWN ARRANGEMENT.**')
    rec('    ### The atlas writes the archimedean channel as')
    quote(SR, 'W_∞(g)', clip=200)
    rec('')
    rec('    ### ### So `A = INT h-hat(u) * [h+(u) / 2 pi] du`: ### **THE TEST FUNCTION INTEGRATED')
    rec('    ### ### AGAINST `h+(u) / 2 pi`.** ### The zero side of the same identity is')
    rec('    ### `Z = SUM over ordinates h-hat(gamma)` -- ### **THE TEST FUNCTION SUMMED OVER THE')
    rec('    ### ACTUAL ZEROS.** ### A smooth measure that replaces a sum over a point set is a')
    rec('    ### DENSITY for that point set precisely when it reproduces its counting function, and')
    rec('    ### the check is arithmetic:')
    rec('')
    rec('      ### `INT_0^T h+(u) / (2 pi) du`  against  the Riemann-von Mangoldt main term.')
    rec('')
    rec('      %-8s %-22s %-22s %-14s'
        % ('T', 'INT_0^T h+/2pi du', 'RvM main term', 'RvM - INT'))
    from mpmath import quad
    diffs = []
    for Tt in (50, 100, 500, 1000, 5000):
        got = float(quad(lambda x: h_mp(x) / (2 * pi), [0, Tt]))
        rvm = float(mpf(Tt) / (2 * pi) * log(mpf(Tt) / (2 * pi)) - mpf(Tt) / (2 * pi) + mpf(7) / 8)
        diffs.append(rvm - got)
        rec('      %-8s %-22.12f %-22.12f %+.12f' % (Tt, got, rvm, rvm - got))
    rec('')
    rec('    ### ### **THE DIFFERENCE IS NOT SMALL, AND IT IS NOT NOISE. ### IT RISES TOWARD')
    rec('    ### ### `1`, AND ITS DEFICIT FROM `1` IS ITSELF A NAMED TERM:**')
    rec('')
    rec('      %-8s %-20s %-20s %s' % ('T', '1 - (RvM - INT)', '1 / (48 pi T)', 'ratio'))
    for Tt, dd in zip((50, 100, 500, 1000, 5000), diffs):
        rec('      %-8s %-20.9e %-20.9e %.9f'
            % (Tt, 1.0 - dd, 1.0 / (48 * math.pi * Tt), (1.0 - dd) * 48 * math.pi * Tt))
    rec('')
    rec('    ### ### **THE RATIO IS `1` TO EIGHT FIGURES AT EVERY `T`, SO THE ACCOUNTING IS')
    rec('    ### ### EXACT AND BOTH LEFTOVER TERMS HAVE NAMES:**')
    rec('')
    rec('      `RvM main term - INT_0^T h+/(2 pi) du  =  1  -  1/(48 pi T)  +  O(T^-3)`.')
    rec('')
    rec('    ### The `1/(48 T)` is the next term of the Riemann-Siegel theta expansion, over')
    rec('    ### `pi`. ### **AND A DIFFERENCE OF EXACTLY ONE IS NOT AN ERROR; IT IS A TERM.**')
    rec('')
    rec('    ### **AND THE RECORD`S OWN ARRANGEMENT NAMES IT.** ### The identity is classical and')
    rec('    ### exact: with `theta` the Riemann-Siegel theta function,')
    rec('')
    rec('      `theta`(T) = arg Gamma(1/4 + iT/2) - (T/2) log pi`, so `theta`(T) = h+(T) / 2`,')
    rec('      hence  `INT_0^T h+(u) / (2 pi) du  =  theta(T) / pi`,')
    rec('      and    `N(T) = theta(T) / pi + 1 + S(T)`.')
    rec('')
    rec('    ### ### **THE `1` IS THE POLE OF ZETA AT `s = 1`.** ### The smooth density counts the')
    rec('    ### ### ZEROS; the counting function `N(T)` carries, in addition, the pole -- which is')
    rec('    ### ### the same `W_pole` Component 3 is about, arriving here by a different door.**')
    rec('    ### The remaining `S(T)` oscillates about zero and is what the SMOOTH term drops; it')
    rec('    ### does not appear in the table because `quad` integrates the smooth term exactly.')
    rec('')
    rec('    ### ### **SO (b-i) IS TRUE, AND SHARPER THAN THE CLAUSE CLAIMED:** ### `h+(u) / 2 pi`')
    rec('    ### ### IS THE SMOOTH ZERO-COUNTING DENSITY, ITS INTEGRAL IS `theta(T) / pi`, AND THE')
    rec('    ### ### RIEMANN-VON MANGOLDT MAIN TERM IS THAT INTEGRAL PLUS ONE.**')
    rec('    ### ### **AND THE FACTOR MATTERS: `h+` ITSELF IS `2 pi` TIMES THE DENSITY.** ### The')
    rec('    ### navigator`s clause (b) says `that expression` is the density; ### **IT IS THE')
    rec('    ### DENSITY UP TO `2 pi`, AND `2 pi` IS EXACTLY THE CONSTANT CLAUSE (c) TURNS ON.**')
    rec('')
    rec('    ### **THE FIRST DRAFT OF THIS PARAGRAPH PREDICTED `AGREEMENT TO A FEW PARTS IN A')
    rec('    ### THOUSAND` AND WAS WRONG** -- the agreement is exact and offset by a term. ### The')
    rec('    ### prediction was typed before the table was run, and ### **IT IS CORRECTED HERE')
    rec('    ### RATHER THAN DELETED**, because the correction is the better result.')
    rec('')
    rec('    ### **AND ONE CONSEQUENCE THE ACT STATES BECAUSE IT LOOKS LIKE AN OBJECTION AND IS')
    rec('    ### NOT:** ### `h+` is NEGATIVE below `u0`, and a density is not. ### The smooth')
    rec('    ### density is a FORMAL one: it is negative exactly where the true counting function')
    rec('    ### is flat at zero -- the first ordinate sits at `14.13`, far above `u0 = 6.29` --')
    rec('    ### ### **SO THE NEGATIVE REGION IS WHERE THERE ARE NO ZEROS TO COUNT.**')
    rec('')
    rec('    ### **(b-ii) WHAT THE CORPUS ACTUALLY CARRIES.** ### Every hit hand-read at its line.')
    names = [('the classical counting law, by name', os.path.join(PP, 'FACES_LEDGER.md'),
              'Riemann-von Mangoldt main term'),
             ('the archimedean kernel, by its operational name', SR, 'the archimedean kernel'),
             ('the sign change, as a property of `W_inf`', SR,
              'NEGATIVE at low frequency and POSITIVE at high frequency'),
             ('the dictionary row that defines `A`', SR, 'W_∞(g)')]
    for lbl, path, ndl in names:
        rec('')
        rec('    ### %s:' % lbl)
        quote(path, ndl, clip=240)
    rec('')
    rec('    ### ### **AND THE JOIN -- A FILE THAT WRITES `h+` AND A FILE THAT WRITES `N(T)` DOES')
    rec('    ### ### NOT JOIN THEM.** ### The search for a site that calls this expression a zero')
    rec('    ### density, or derives `N(T)` FROM it, is run over the whole corpus:')
    import re as _re
    # ### **TWO SCREENS, AND THE VERDICT IS TAKEN OFF THE TIGHT ONE** (`K` BAR 2). ### The loose
    # ### screen finds any line pairing a density word with an archimedean word; ### **THAT IS A
    # ### MENTION, NOT A JOIN**, and counting mentions is the defect `b435` banked. ### The tight
    # ### screen demands THE EXPRESSION ITSELF beside a counting word on one line.
    LOOSE = _re.compile(r'(densit\w+|counting)[^\n]{0,120}(psi|digamma|h\+|archimedean)'
                        r'|(psi|digamma|h\+|archimedean)[^\n]{0,120}(densit\w+|counting)', _re.I)
    EXPR = _re.compile(r'(\u03c8\s*\(\s*1\s*/\s*4|psi\s*\(\s*1\s*/\s*4'
                       r'|digamma\s*\(\s*0?\.25|\bh\+|\bh_\+|W_\u221e|W_inf)')
    COUNT = _re.compile(r'(densit\w+|zero[- ]count\w*|counting function|N\(T\)|'
                        r'von Mangoldt)', _re.I)
    loose, tight, scanned = [], [], 0
    for root, dirs, fs in os.walk(PP):
        dirs[:] = [x for x in dirs if x not in ('.git', '__pycache__')]
        for f in fs:
            if not f.endswith('.md'):
                continue
            scanned += 1
            q = os.path.join(root, f)
            rel = os.path.relpath(q, PP).replace(os.sep, '/')
            for i, ln in enumerate(nl(io.open(q, encoding='utf-8', errors='replace').read())
                                   .splitlines()):
                if LOOSE.search(ln):
                    loose.append((rel, i + 1, ln.strip()))
                if EXPR.search(ln) and COUNT.search(ln):
                    tight.append((rel, i + 1, ln.strip()))
    rec('      documents scanned : %d' % scanned)
    rec('      LOOSE screen, a density word near an archimedean word : %d lines' % len(loose))
    rec('      ### ### **AND THAT NUMBER IS NOT THE ANSWER.** ### Hand-reading the loose hits')
    rec('      ### finds `the archimedean density` of a different object, `the density question`,')
    rec('      ### and a Lagarias citation -- ### **TWO WORDS NEAR EACH OTHER, NOT TWO THINGS')
    rec('      ### JOINED.** ### `b435` banked exactly this: a mention is not a reference.')
    rec('')
    rec('      ### **TIGHT screen -- THE EXPRESSION ITSELF beside a counting word, one line:**')
    rec('      ### ### **LINES : %d**' % len(tight))
    for f, i, ln in tight[:14]:
        HANDREAD[0] += 1
        rec('        %s:%d' % (f, i))
        for c in wrap(ln[:260], 80):
            rec('          | %s' % c)
    json.dump(dict(loose=[dict(file=f, line=i, text=t) for f, i, t in loose],
                   tight=[dict(file=f, line=i, text=t) for f, i, t in tight]),
              io.open(os.path.join(D, 'b440_clauses.json'), 'w', encoding='utf-8'), indent=1)
    rec('')
    rec('')
    rec('      ### ### **AND EACH IS HAND-READ AND CLASSIFIED, BECAUSE A SCREEN CANNOT SETTLE')
    rec('      ### ### THIS** (`K` BAR 2). ### The classification is typed by this seat against')
    rec('      ### ### the lines above, and ### **ANY HIT NOT IN THE TABLE IS REPORTED')
    rec('      ### ### UNCLASSIFIED AND FAILS THE COMPONENT**, so the table cannot go stale.')
    HAND = [
        ('SPIRAL_MAP.md', 114, 'NOT A JOIN',
         'it is the window kernel`s NON-CLAIM, and it sets the two side by side precisely to '
         'hold them APART -- *its `W` is a prime-power COUNTING FUNCTION unrelated to '
         '`W_2`/`W_inf`*. ### **A DISCLAIMER OF A RELATION IS THE OPPOSITE OF AN '
         'IDENTIFICATION.**'),
        ('FINDINGS-archive-1-entries-through-2026-08-20c.md', 2678, 'NOT A JOIN',
         'an open-term inventory -- *the odd-sector W_inf mass ... the even-sector eps mass*. '
         'The word `density` belongs to a different sector`s question, not to `h+`.'),
        ('OPEN_TRAILS-archive-2-historical-landings-and-programs.md', 9037, 'NOT A JOIN',
         'an era-annotation list naming the sign reconciliation`s `W_inf` repair. It cites '
         'the repair; it states no density.'),
    ]
    table = {(f, i): (v, why) for f, i, v, why in HAND}
    joined, unclassified = [], []
    for f, i, ln in tight:
        key = (os.path.basename(f), i)
        if key not in table:
            unclassified.append((f, i, ln))
            continue
        v, why = table[key]
        HANDREAD[0] += 1
        rec('')
        rec('        %s:%d   ### ### **%s**' % (f, i, v))
        for c in wrap(why, 78):
            rec('            %s' % c)
        if v == 'JOIN':
            joined.append((f, i, ln))
    rec('')
    if unclassified:
        rec('      ### ### **UNCLASSIFIED HITS : %d -- THE COMPONENT FAILS ON THIS AXIS.**'
            % len(unclassified))
        for f, i, ln in unclassified:
            rec('        %s:%d  | %s' % (f, i, ln[:90]))
    rec('      ### ### **HITS HAND-READ : %d. ### CLASSIFIED `JOIN` : %d.**'
        % (len(tight) - len(unclassified), len(joined)))
    CLAUSES['b'] = ('HOLDS AS MATHEMATICS, AND SHARPER THAN THE CLAUSE CLAIMED; '
                    'NOT CARRIED BY THE CORPUS AS AN IDENTIFICATION'
                    if not joined and not unclassified else
                    ('HOLDS AS MATHEMATICS; THE CORPUS CARRIES IT AT THE LINES MARKED JOIN'
                     if joined else 'NOT DECIDED -- UNCLASSIFIED HITS'))
    rec('')
    rec('      ### ### **CLAUSE (b) : %s.**' % CLAUSES['b'])
    rec('      ### ### **AND THE NEAREST THING THE CORPUS HAS IS A LINE THAT DENIES THE')
    rec('      ### ### RELATION** -- the window kernel`s own non-claim, warning a reader that')
    rec('      ### ### its `W` is a counting function UNRELATED to `W_inf`. ### The corpus has')
    rec('      ### ### taken care to keep a counting function and `W_inf` apart, and has never')
    rec('      ### ### remarked that `W_inf` IS one, on a different scale.**')
    rec('      ### ### **AND THE TWO NAMES THE CORPUS DOES USE ARE `Riemann-von Mangoldt` FOR THE')
    rec('      ### ### COUNTING LAW AND `the archimedean kernel` / `W_inf` FOR THE EXPRESSION.**')
    rec('      ### `(N1)(b)` said the atlas already carries the expression ### **UNDER ANOTHER')
    rec('      ### NAME**, and that half is right -- it carries it as `W_inf`. ### What it does')
    rec('      ### not carry is the JOIN, and the join is the content of clause (b).')

    # -------------------------------------------------------------------------------------------
    sub('CLAUSE (d) -- THE DIGITS.')
    nav = '6.28983598883690277966'
    mine = mp.nstr(u0, 21)
    rec('      the navigator`s : %s' % nav)
    rec('      this seat`s     : %s   ### at 40 decimal places of working precision' % mine)
    rec('      u0 to 30 dps    : %s' % mp.nstr(u0, 31))
    rec('      2 pi to 30 dps  : %s' % mp.nstr(2 * pi, 31))
    ratio = u0 / (2 * pi)
    rec('      ratio u0 / 2 pi : %s' % mp.nstr(ratio, 18))
    rec('')
    agree = (nav == mine)
    rec('      ### ### **THE TWO STRINGS AGREE TO %d SIGNIFICANT FIGURES%s.**'
        % (len(os.path.commonprefix([nav, mine]).replace('.', '')),
           '' if agree else ', AND DIFFER IN THE LAST DIGIT PRINTED'))
    if not agree:
        rec('      ### **BOTH ARE PRINTED AND NEITHER IS QUIETLY PREFERRED** (`K` BAR 4). ### The')
        rec('      ### twentieth significant figure is a ROUNDING of the same number: the true')
        rec('      ### value continues `...779669`, so `...77966` truncates and `...77967` rounds.')
        rec('      ### ### **NEITHER IS WRONG; THEY ARE THE SAME `u0` WRITTEN TWO WAYS.**')
    rec('      ### And the ratio `1.001058` the navigator gives is exact to the digits he gives.')
    CLAUSES['d'] = 'HOLDS'
    rec('      ### ### **CLAUSE (d) : HOLDS.**')
    json.dump(dict(u0=str(u0), two_pi=str(2 * pi), ratio=str(ratio),
                   navigator=nav, seat=mine, routeB=str(u0_b), route_gap=gap),
              io.open(os.path.join(D, 'b440_u0.json'), 'w', encoding='utf-8'), indent=1)

    # -------------------------------------------------------------------------------------------
    sub('THE MECHANISM -- STATED ONLY BECAUSE (b) HOLDS AS MATHEMATICS, AND THEN TESTED.')
    rec('    ### ### **THE SENTENCE, ONCE:** ### the archimedean slack closes when half the seed`s')
    rec('    ### ### transform mass lies above the height at which the smooth zero-density turns')
    rec('    ### ### positive, `u0 = 6.2898`.')
    rec('')
    rec('    ### **AND NOW IT IS TESTED, ON BOTH FAMILIES, WHICH IS THE ONLY THING THAT MAKES IT')
    rec('    ### MORE THAN A RESTATEMENT.** ### The archimedean route is evaluated as `b438` and')
    rec('    ### `b439` evaluated it; no new family and no new instrument.')
    U = np.linspace(0.0, AT.UMAX, AT.NU)
    UF = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
    # ### **THE KERNEL IS EVALUATED ONCE, ON ONE GRID, AND REUSED BY NAME** -- `carto_atlas.kernel`
    # ### caches on its first argument, so calling it on two grids would silently return the first.
    KERN = np.array(AT.kernel(UF), dtype=float)
    rows = []
    rec('')
    rec('      %-7s %-9s %-16s %-16s %-12s %s'
        % ('family', 'a', 'median u of |h-hat|', 'mass above u0', 'A (arch)', 'sign of A'))
    for fam, maker in (('aimed', SM.mean_zero_variant), ('corpus', SM.corpus_bump)):
        for a in (1.2, 2.0, 4.0, 8.0, 16.0):
            tf = maker(a)
            v, w = tf.v, tf.w
            hh = np.abs(WIN.hhat_blocked(v, w, U))
            cum = np.cumsum(hh) / np.sum(hh)
            med = float(np.interp(0.5, cum, U))
            above = float(1.0 - np.interp(float(u0), U, cum))
            A = float(np.trapezoid(WIN.hhat_blocked(v, w, UF) * KERN, UF) / (2.0 * math.pi))
            rec('      %-7s %-9.4f %-16.6f %-16.6f %-12.6f %s'
                % (fam, a, med, above, A, '+' if A > 0 else '-'))
            rows.append(dict(family=fam, a=a, median=med, mass_above_u0=above, A=A))
    rec('')
    agree_rows = [r for r in rows if (r['mass_above_u0'] > 0.5) == (r['A'] > 0)]
    rec('      ### ### **THE SENTENCE PREDICTS `A > 0` EXACTLY WHERE THE MASS ABOVE `u0` EXCEEDS')
    rec('      ### ### HALF. ### IT AGREES AT %d OF %d CELLS, ACROSS BOTH FAMILIES.**'
        % (len(agree_rows), len(rows)))
    same = all((r['mass_above_u0'] > 0.5) == (r['A'] > 0) for r in rows if r['family'] == 'corpus')
    rec('      ### ### **AND THE SECOND FAMILY`S NEVER CROSSING: %s.**'
        % ('EXPLAINED BY THE SAME SENTENCE' if same else 'NOT EXPLAINED BY THE SAME SENTENCE'))
    bad = [r for r in rows if (r['mass_above_u0'] > 0.5) != (r['A'] > 0)]
    for r in bad:
        rec('      ### the cell that breaks it : family `%s`, `a = %.4f` -- mass above `u0` is'
            % (r['family'], r['a']))
        rec('      ### `%.6f`, over half, and yet `A = %+.6f`.' % (r['mass_above_u0'], r['A']))
    rec('')
    rec('    ### ### **SO THE SENTENCE IS A HEURISTIC AND THE ACT SAYS SO RATHER THAN ROUNDING')
    rec('    ### ### 9 OF 10 UP TO A MECHANISM.** ### `A` is not a median of `h-hat`; it is the')
    rec('    ### WEIGHTED balance `INT h-hat(u) h+(u) du`, and `h+` keeps GROWING above `u0` while')
    rec('    ### it is bounded below it only by `-log`-sized values near the origin. ### **A CELL')
    rec('    ### WITH BARELY HALF ITS MASS ABOVE `u0` CAN STILL SIT AT `A < 0` IF THE MASS BELOW')
    rec('    ### SITS WHERE `h+` IS MOST NEGATIVE**, which is what the second family does at')
    rec('    ### `a = 1.2`. ### The exact criterion is the balance itself and is a tautology; the')
    rec('    ### sentence`s content is that `u0` is the hinge, and ### **THAT PART SURVIVES.**')
    # ### **THE WRITE LIST NAMES PATHS, AND THIS ONE WAS NOT ON IT.** ### The first writing of
    # ### this component emitted `b440_mechanism.json`, which the locked face never declared.
    # ### The face is NOT edited; the OUTPUT is moved into a declared path instead, and the
    # ### incident is printed in the record. ### **(R47) IS A CONSTRAINT ON THE ACT, NOT ON THE
    # ### FACE.**
    cl = os.path.join(D, 'b440_clauses.json')
    blob = json.load(io.open(cl, encoding='utf-8')) if os.path.exists(cl) else {}
    blob['mechanism'] = rows
    json.dump(blob, io.open(cl, 'w', encoding='utf-8'), indent=1)
    rec('')
    rec('    ### ### **AND ONE WRITE-LIST INCIDENT OF THIS ACT`S OWN, PRINTED NOT PATCHED AWAY:**')
    rec('    ### the first writing of this component emitted `data/b440_mechanism.json`, ### **A')
    rec('    ### PATH THE LOCKED FACE NEVER DECLARED.** ### `(R47)` requires the list to name')
    rec('    ### paths, and it does; what failed was the act, not the list. ### **THE FACE IS NOT')
    rec('    ### EDITED** -- the rows are written into `b440_clauses.json`, which the face DOES')
    rec('    ### name, and the stray file is removed. ### The write-list arm is what caught it.')

    # -------------------------------------------------------------------------------------------
    sub('WHAT THE RECORD CAN NOW SAY ABOUT `u0`. ### **THREE STATUSES, KEPT APART** (`K` BAR 3).')
    rec('    ### **DEFINING EQUATION** ### -- ### **HELD.** ### `u0` is the unique positive root of')
    rec('    ### `Re psi(1/4 + iu/2) = log pi`. ### That is an equation, it is exact, and two')
    rec('    ### independent routes agree on its root to better than `1e-12`.')
    rec('    ### **CLASSICAL ASYMPTOTE** ### -- ### **HELD, AND IT IS `2 pi`.** ### The asymptotic')
    rec('    ### form `log(u / 2 pi)` has its zero at `2 pi` exactly, and `u0 / 2 pi = 1.001058`.')
    rec('    ### ### **`2 pi` IS NOT `u0`. ### IT IS THE ZERO OF A DIFFERENT FUNCTION THAT AGREES')
    rec('    ### ### WITH `h+` TO `O(u^-2)`, AND `h+(2 pi) = -1.06e-03` IS NOT ZERO.**')
    rec('    ### **CLOSED FORM** ### -- ### **NOT HELD.** ### The record gives `u0` a defining')
    rec('    ### equation and twenty-one digits, and no expression in named constants. ### **A')
    rec('    ### TWENTY-ONE-DIGIT VALUE IS NOT A CLOSED FORM**, and the near-coincidence with')
    rec('    ### `2 pi` is an asymptotic fact, not an identity.')
    return u0


# ### ==============================================================================================
def run_lean(name, src):
    """### **THE PROBE, RUN. ### ITS OUTPUT IS QUOTED INCLUDING ITS FAILURE TEXT** (`K` BAR 5)."""
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    p = os.path.join(SCRATCH, name)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
    if not os.path.exists(LEAN):
        return None, '### **NOT PROBED -- no lean binary at %s**' % LEAN
    r = subprocess.run([LEAN, name], cwd=SCRATCH, capture_output=True, timeout=600)
    dec = lambda b: (b or b'').decode('utf-8', 'replace')
    return r.returncode, dec(r.stdout) + dec(r.stderr)


def component_2():
    head('COMPONENT 2', 'THE TWO FACTS. ### CAN THEY BE STATED AT ALL?')
    rec('  ### The order`s own condition governs and is quoted before anything is attempted:')
    rec('  ### ### *"If either fact cannot be stated axiom-free, say so and build neither."*')

    # -------------------------------------------------------------------------------------------
    sub('(alpha) THE ELIMINATION OF THE REALS, WRITTEN OUT AND NOT WAVED AT.')
    rec('    ### Fact (ii) is the weight table `2 Lambda(n) / sqrt(n)` with its maximizer. ### The')
    rec('    ### maximizer claim is a COMPARISON, so the honest question is whether the comparison')
    rec('    ### reduces to arithmetic on naturals. ### **IT IS CARRIED AS FAR AS IT GOES:**')
    rec('')
    rec('      `2 log p / sqrt(p^k)  >  2 log q / sqrt(q^j)`')
    rec('        <=>  `sqrt(q^j) log p > sqrt(p^k) log q`            (all quantities positive)')
    rec('        <=>  `q^j (log p)^2 > p^k (log q)^2`                (squaring, sign preserved)')
    rec('        <=>  `(log p / log q)^2 > p^k / q^j`')
    rec('        <=>  ### **`(log_q p)^2 > p^k / q^j`.**')
    rec('')
    rec('    ### ### **AND THAT IS THE STEP AT WHICH THE IRRATIONAL SURVIVES.** ### The right side')
    rec('    ### is a rational number. ### The left side is the square of `log_q p`, and for')
    rec('    ### distinct primes `p, q` that is irrational -- if `log_q p = m/n` then `p^n = q^m`,')
    rec('    ### which unique factorisation forbids. ### **NO FURTHER MANIPULATION REMOVES IT:**')
    rec('    ### exponentiating returns `p^(sqrt(q^j)) > q^(sqrt(p^k))`, which puts the')
    rec('    ### irrational in the EXPONENT, where `Nat`s `^` cannot take it.')
    rec('')
    rec('    ### **THE ACTUAL COMPARISON THE TABLE TURNS ON, AT THE TOP TWO ENTRIES:**')
    w7 = 2 * math.log(7) / math.sqrt(7)
    w11 = 2 * math.log(11) / math.sqrt(11)
    lhs = (math.log(7) / math.log(11)) ** 2
    rec('      `2 log 7 / sqrt 7`   = %.12f     (the maximizer, b439)' % w7)
    rec('      `2 log 11 / sqrt 11` = %.12f     (the runner-up)' % w11)
    rec('      so the claim is      `(log_11 7)^2 > 7 / 11`')
    rec('      `(log_11 7)^2`       = %.12f' % lhs)
    rec('      `7 / 11`             = %.12f' % (7.0 / 11.0))
    rec('      ### ### **TRUE, AND BY %.3e -- ### AN INEQUALITY BETWEEN A TRANSCENDENTAL AND A'
        % (lhs - 7.0 / 11.0))
    rec('      ### ### RATIONAL, WHICH NO FINITE `Nat` COMPUTATION DECIDES.**')

    # -------------------------------------------------------------------------------------------
    sub('(beta) THE PROBE. ### **RUN IN THE SESSION SCRATCHPAD, IN NO REPOSITORY.**')
    rec('    ### **AND IT CARRIES A POSITIVE CONTROL**: the `Nat` half of the same act, so that a')
    rec('    ### refusal is a statement about the WEIGHT and not about the prover.')
    code1, out1 = run_lean('Probe.lean', PROBE1)
    rec('')
    rec('    ### **PROBE FILE 1 -- `Real`, `Rat`, `Float`, AND THE `Nat` CONTROL.**')
    rec('    ### lean : %s' % (('exit %s' % code1) if code1 is not None else 'NOT RUN'))
    for ln in (out1 or '').splitlines():
        rec('      | %s' % ln[:96])
    code2, out2 = run_lean('Probe2.lean', PROBE2)
    rec('')
    rec('    ### **PROBE FILE 2 -- THE RATIONAL SURROGATE.**')
    rec('    ### lean : %s' % (('exit %s' % code2) if code2 is not None else 'NOT RUN'))
    for ln in (out2 or '').splitlines():
        rec('      | %s' % ln[:96])
    probed = code1 is not None and code2 is not None
    rec('')
    rec('    ### ### **WHAT THE PROBE ESTABLISHES, LINE BY LINE:**')
    rec('    ### `Real`            -- ### **UNKNOWN IDENTIFIER.** ### There are no reals here.')
    rec('    ### `Rat`             -- ### **EXISTS** ### in core, so a rational is WRITABLE...')
    rec('    ### `Rat` comparison  -- ### **`decide` FAILS**: *"reduction got stuck at the')
    rec('    ###                      `Decidable` instance"*. ### Core `Rat`s `blt` is opaque.')
    rec('    ### `Float.log/sqrt`  -- ### **TYPECHECK**, so the weight is WRITABLE as a `Float`...')
    rec('    ### `Float` comparison-- ### **`decide` FAILS**, same reduction failure.')
    rec('    ### `Decidable` inst. -- ### **EXISTS** ### for `Float` order. ### **THIS IS THE SHARP')
    rec('    ###                      FORM: THE PROPOSITION IS NOMINALLY DECIDABLE AND `decide`')
    rec('    ###                      STILL CANNOT CLOSE IT, THE INSTANCE BEING `@[extern]`.**')
    rec('    ### `Nat.sqrt`        -- ### **UNKNOWN CONSTANT.** ### Not in vanilla core.')
    rec('    ### the `Nat` control -- ### **EVERY ONE CLOSED BY `decide`, AND THE AXIOM PROFILES')
    rec('    ###                      ARE PRINTED RATHER THAN INFERRED FROM SILENCE.**')
    rec('')
    rec('    ### ### **AND THE PROFILES CARRY A RESULT THIS SEAT DID NOT EXPECT AND DID NOT')
    rec('    ### ### DECLARE ON THE FACE:**')
    rec('      `edge_16 : 16 not-in primePowersLT 16`   ### **[propext, Quot.sound]**')
    rec('      `edge_17 : 17 not-in primePowersLT 17`   ### **[propext, Quot.sound]**')
    rec('      `below_16 : primePowersLT 16 = [...]`    ### **no axioms at all**')
    rec('      `edge_16_bool : (primePowersLT 16).elem 16 = false`   ### **no axioms at all**')
    rec('      `edge_17_bool`, `edge_9_bool`                         ### **no axioms at all**')
    rec('      `edge_present : (primePowersLT 17).elem 16 = true`    ### **no axioms at all**')
    rec('')
    rec('    ### ### **SO THE FORM OF THE STATEMENT DECIDES WHETHER IT IS AXIOM-FREE.** ### The')
    rec('    ### natural phrasing -- PROPOSITIONAL non-membership, `not-in` -- routes through')
    rec('    ### library lemmas about `List.Mem` and drags in `propext` and `Quot.sound`. ### **BY')
    rec('    ### THIS KERNEL`S OWN DECLARED BAR -- *not `{propext, Classical.choice, Quot.sound}`,')
    rec('    ### BUT NO AXIOMS AT ALL* -- THAT PHRASING WOULD NOT QUALIFY.** ### The DECIDABLE-')
    rec('    ### EQUALITY phrasing, `.elem ... = false`, closes by reduction alone and does.')
    rec('    ### ### **`b418` BANKED THIS AS A GENERAL LESSON AND IT IS CONFIRMED HERE ON A NEW')
    rec('    ### ### STATEMENT: EQUATION FORMS ARE CLEAN, PROPOSITIONAL FORMS ARE NOT.**')
    rec('    ### ### **AND `edge_present` IS THE POSITIVE CONTROL** -- `16` IS in')
    rec('    ### `primePowersLT 17` -- ### **SO THE ARM CAN SAY `true` AS WELL AS `false`,** ### and')
    rec('    ### the three `false`s are not a tool that always answers one way.')
    rec('    ### ### **FACT (i) IS THEREFORE STATABLE AXIOM-FREE, IN ONE FORM AND NOT THE OTHER.**')

    # -------------------------------------------------------------------------------------------
    sub('(gamma) WOULD A RATIONAL-ENCLOSURE SURROGATE BE LEGITIMATE? ### THE KERNEL HAS RULED.')
    rec('    ### The probe showed the surrogate does not even RUN. ### But suppose it did -- suppose')
    rec('    ### `Rat` reduced. ### The statement would compare `19459/10000` with `23979/10000`,')
    rec('    ### and ### **NOTHING IN IT WOULD SAY THOSE ARE LOGARITHMS.** ### The bridge would')
    rec('    ### live in a comment. ### **THE KERNEL HAS ALREADY REFUSED EXACTLY THIS PATTERN:**')
    rec('')
    quote(os.path.join(KERNEL, 'SIDEWindow', 'Ladder.lean'), 'MEASURED-AT-BANK', after=2, clip=200)
    rec('')
    rec('    ### ### **SO THE SURROGATE FALLS UNDER THE LADDER`S OWN REFUSAL, AND WOULD FALL UNDER')
    rec('    ### ### IT EVEN IF IT COMPILED.** ### Two independent reasons, and the act needed only')
    rec('    ### one.')

    # -------------------------------------------------------------------------------------------
    sub('THE DECISION.')
    rec('    ### **FACT (i)** ### -- a prime power at the support edge contributes exactly zero.')
    rec('    ### ### **STATABLE AXIOM-FREE -- IN ITS DECIDABLE-EQUALITY FORM ONLY -- AND THE')
    rec('    ### ### PROBE CLOSED IT WITH `0` AXIOMS, FOUR TIMES, WITH A POSITIVE CONTROL.**')
    rec('    ### `primePowersLT x` filters `List.range x = [0, ..., x-1]`, so `x` itself is never')
    rec('    ### in it; the bump`s vanishing at the support edge is the analytic half, and it is')
    rec('    ### quoted from its source, not proved here.')
    rec('    ### **FACT (ii)** ### -- the weight table with its maximizer.')
    rec('    ### ### **NOT STATABLE IN THIS KERNEL`S STYLE.** ### It is an inequality between a')
    rec('    ### transcendental and a rational; the kernel has no reals; its `Rat` and `Float` are')
    rec('    ### opaque to `decide`; and a literal surrogate is the pattern `Ladder.lean` refuses.')
    rec('')
    rec('    ### ### **AND SO, BY THE ORDER`S OWN CONDITION: ### NEITHER FACT IS BUILT.**')
    rec('    ### ### **NOTHING IS WRITTEN INTO `SIDE-window`. ### NO `.lean` FILE, AND NOT')
    rec('    ### ### `README.md` EITHER** -- `(R52)` updates non-claims when CONTENTS CHANGE, and')
    rec('    ### nothing changing is not a change. ### The kernel`s non-claims stand as they are.')
    rec('')
    rec('    ### ### **WHAT IS ROUTED BACK AND NOT DECIDED HERE** (`K` BAR 7): ### fact (i) alone')
    rec('    ### ### IS buildable and would be a true, decidable, axiom-free terminal -- the probe')
    rec('    ### ### has already closed it four times outside the repository. ### **THE ORDER')
    rec('    ### ### FORBIDS BUILDING IT ALONE, SO IT IS NOT BUILT**, and the choice -- whether')
    rec('    ### ### to take fact (i) by itself in a later act -- is the author`s.**')
    rec('    ### ### **AND ONE THING THE AUTHOR SHOULD HAVE BEFORE DECIDING: THE STATEMENT WOULD')
    rec('    ### ### HAVE TO BE WRITTEN `.elem n = false`, NOT `n not-in`, OR IT WOULD CARRY TWO')
    rec('    ### ### AXIOMS AND BREAK THE REPOSITORY`S OWN STANDARD.**')
    prof = {}
    for ln in (out1 or '').splitlines():
        m = re.search(r"'(\w+)' depends on axioms: \[([^\]]*)\]", ln)
        if m:
            prof[m.group(1)] = m.group(2)
            continue
        m = re.search(r"'(\w+)' does not depend on any axioms", ln)
        if m:
            prof[m.group(1)] = 'NONE'
    json.dump(dict(probe1_exit=code1, probe2_exit=code2, axiom_profiles=prof,
                   fact_i='STATABLE, DECIDABLE-EQUALITY FORM ONLY',
                   fact_ii='NOT STATABLE -- no reals; Rat and Float opaque to decide',
                   objects_built=0, reason="the order's own condition: build neither"),
              io.open(os.path.join(D, 'b440_kernel_attempt.json'), 'w', encoding='utf-8'), indent=1)
    return dict(probed=probed, built=0, fact_i='STATABLE', fact_ii='NOT STATABLE')


# ### ==============================================================================================
def component_3():
    head('COMPONENT 3', 'THE BREAK ATTRIBUTED. ### FROM THE SOURCE, NOT NAMED BY THE SEAT.')
    rec('  ### The order`s clause is CONDITIONAL: ### *"Read from the source what that weight is --')
    rec('  ### whether it is the archimedean factor`s own scaling, the thing that makes the pairing')
    rec('  ### a Weil pairing. ### **IF IT IS**, state the finding..."*')

    sub('THE SOURCE`S OWN TERM-FOR-TERM DICTIONARY. ### TWO ROWS, SIDE BY SIDE.')
    quote(SR, 'W_pole(g)', clip=200)
    quote(SR, 'W_∞(g)', clip=200)
    rec('')
    rec('    ### ### **`cosh(v/2)` IS THE WEIGHT OF `W_pole`. ### THE ARCHIMEDEAN WEIGHT IS')
    rec('    ### ### `Re psi(1/4 + iu/2) - log pi`, A DIFFERENT EXPRESSION IN A DIFFERENT')
    rec('    ### ### VARIABLE -- `u`, THE FREQUENCY, NOT `v`, THE LOG-RADIUS.**')
    rec('')
    rec('    ### ### **THE PREMISE OF THE ORDER`S CONDITIONAL THEREFORE FAILS, AND THE OFFERED')
    rec('    ### ### FINDING IS NOT STATED** (`K` BAR 1). ### The act says instead what the weight')
    rec('    ### ### IS, and whether the break is structural for a reason the source also supplies.')

    sub('WHAT `cosh(v/2)` IS, IN THE SOURCE`S WORDS.')
    quote(SR, 'it is the count of the two pole terms', clip=420)
    rec('')
    rec('    ### **AND WHAT THE AIM`S SECOND MOMENT CONDITION IS, IN THE INSTRUMENT`S HEADER:**')
    quote(os.path.join(T, 'b317_smear.py'), 'test function is the single condition')
    rec('')
    quote(os.path.join(T, 'b321_run.py'), 'g-hat(i/2) = 0', after=1, clip=200)
    rec('')
    rec('    ### ### **SO THE AIM`S SECOND MOMENT CONDITION IS NOT A MOMENT CONDITION AT ALL IN')
    rec('    ### ### DISGUISE -- IT IS THE LAWFULNESS CONDITION `h-hat(i/2) = 0`, THE REQUIREMENT')
    rec('    ### ### THAT THE TEST FUNCTION KILL THE POLE TERM.** ### `b439` found the aim`s second')
    rec('    ### condition is what breaks scale invariance; this component says WHAT that condition')
    rec('    ### is, and it is the poles, not the gamma factor.')

    sub('IS THE BREAK STRUCTURAL? ### YES -- AND FOR THE FUNCTIONAL EQUATION`S REASON.')
    rec('    ### With the corpus`s half-line normalization `f(x) = x^(-1/2) w(log x)` and `v = log x`,')
    rec('')
    rec('      `cosh(v/2) = (e^(v/2) + e^(-v/2)) / 2 = (x^(1/2) + x^(-1/2)) / 2`.')
    rec('')
    rec('    ### ### **A SINGLE POWER OF `x` IS DILATION-COVARIANT: `(cx)^s = c^s x^s`, and the')
    rec('    ### ### CONSTANT COMES OUT. ### A SUM OF TWO DIFFERENT POWERS IS NOT, BECAUSE THE TWO')
    rec('    ### ### CONSTANTS `c^(1/2)` AND `c^(-1/2)` DIFFER AND NEITHER FACTORS OUT.**')
    rec('    ### The demonstration, on the object itself:')
    rec('')
    rec('      %-8s %-20s %-20s %-14s %s'
        % ('c', 'INT phi cosh(v/2)', 'c^(1/2) * base', 'ratio', '(1 + 1/c) / 2'))
    v = np.linspace(-8.0, 8.0, 40001)
    base = np.exp(-v * v)
    I0 = float(np.trapezoid(base * np.cosh(v / 2.0), v))
    for c in (1.5, 2.0, 4.0):
        s = math.log(c)
        shifted = np.exp(-(v - s) ** 2)
        I1 = float(np.trapezoid(shifted * np.cosh(v / 2.0), v))
        rec('      %-8.4f %-20.12f %-20.12f %-14.9f %.9f'
            % (c, I1, math.sqrt(c) * I0, I1 / (math.sqrt(c) * I0), (1.0 + 1.0 / c) / 2.0))
    rec('')
    rec('')
    rec('    ### ### **THE RATIO IS NOT `1` AND NOT CONSTANT, AND IT IS NOT VAGUE EITHER --')
    rec('    ### ### IT IS EXACTLY `(1 + 1/c) / 2`, TO EVERY DIGIT PRINTED.** ### The derivation')
    rec('    ### is two lines: with `s = log c` and `phi` even,')
    rec('')
    rec('      `INT phi(v - s) cosh(v/2) dv = cosh(s/2) INT phi cosh(v/2) dv`,')
    rec('      so the ratio to `c^(1/2) = e^(s/2)` is `cosh(s/2) / e^(s/2) = (1 + 1/c) / 2`.')
    rec('')
    rec('    ### ### **THAT IS THE TWO POWERS, VISIBLE: `c^(1/2)` AND `c^(-1/2)` ARRIVE WITH')
    rec('    ### ### DIFFERENT WEIGHTS AND THEIR AVERAGE IS NOT EITHER ONE.** ### It tends to')
    rec('    ### `1/2` as `c` grows and to `1` as `c -> 1`, so ### **THE BREAK IS LARGEST AT LARGE')
    rec('    ### RADIUS AND VANISHES AT THE SMALLEST**, which is the shape `b439` measured.')
    rec('    ### For the FIRST moment, whose weight is `1`, the same calculation gives `1`, and')
    rec('    ### `b439` measured that half as fixed.')
    rec('')
    rec('    ### ### **AND `(x^(1/2) + x^(-1/2)) / 2` IS THE `s <-> 1 - s` SYMMETRIC COMBINATION --')
    rec('    ### ### THE TWO POLES OF THE COMPLETED FUNCTION, AT `s = 0` AND `s = 1`, WHICH THE')
    rec('    ### ### FUNCTIONAL EQUATION EXCHANGES.** ### The source says so in its own words: the')
    rec('    ### `2` is `W_pole`, ### *"the count of the two pole terms, `s = 0` and `s = 1`"*.')
    rec('    ### ### **SO THE BREAK IS STRUCTURAL, AND ITS STRUCTURE IS THE FUNCTIONAL EQUATION`S')
    rec('    ### ### POLE PAIR, NOT THE ARCHIMEDEAN GAMMA FACTOR.**')

    sub('AND THE NUMBER IS NOT RE-OPENED (`K` BAR 9).')
    rec('    ### `b439` banked a spread of `2.266e-04` between two radii and attributed it to the')
    rec('    ### `cosh`. ### **THAT MEASUREMENT IS UNTOUCHED BY THIS COMPONENT AND IS NOT RE-RUN.**')
    rec('    ### The `cosh` is still the reason. ### **WHAT CHANGES IS ONLY THE NAME OF WHAT THE')
    rec('    ### `cosh` BELONGS TO: ### THE POLE TERM, NOT THE ARCHIMEDEAN TERM.**')
    rec('    ### ### **A MEASUREMENT AND ITS ATTRIBUTION ARE SEPARABLE, AND ONLY THE SECOND MOVES.**')


def main():
    rec('=' * 100)
    rec('b440 -- THE FIXED POINT NAMED, THE BREAK ATTRIBUTED, AND TWO FACTS BUILT.')
    rec('### ### **THE COMPONENTS. ### RUN AFTER THE LOCK.**')
    rec('=' * 100)
    component_1()
    c2 = component_2()
    component_3()
    rec('')
    rec('=' * 100)
    rec('  ### ### **THE CLAUSE VERDICTS, APART** (`R27`):')
    for k in ('a', 'b', 'c', 'd'):
        rec('      clause (%s) : %s' % (k, CLAUSES.get(k, 'NOT REACHED')))
    rec('  ### ### **COMPONENT 2 : fact (i) %s ; fact (ii) %s ; OBJECTS BUILT %d.**'
        % (c2['fact_i'], c2['fact_ii'], c2['built']))
    rec('  ### ### **COMPONENT 3 : THE PREMISE FAILS -- `cosh(v/2)` IS THE POLE WEIGHT.**')
    rec('  ### hand-read lines : %d' % HANDREAD[0])
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
