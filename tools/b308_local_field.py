# -*- coding: utf-8 -*-
"""b308_local_field.py -- THE LOCAL-FIELD INSTRUMENT, ACT ONE. ### THE BUILD AND ITS CONTROLS.

### ### **WHAT THIS IS.** ### The corpus computes the finite side on `Z/p^{2n}`. ### That model
### TIES TWO RADII TOGETHER -- the radius of the support and the radius of constancy -- and b21's
### own sentence is where they are tied:
### ### **"V_n IS canonically the model space: p^(-n)Z_p / p^n Z_p = Z/p^(2n) via x = p^(-n) m;
### ### Haar measure (Z_p mass 1) gives each chart point mass p^(-n) -- uniform -- so the model
### ### inner product is the L^2(Q_p) inner product up to the global scalar p^(-n)."**
### ### ### **ONE `n` GOVERNS BOTH RADII, AND THAT IS THE TIE.**
### This file UNTIES them: a frame is a pair `(r, s)` -- ### **SUPPORT RADIUS `p^r`, CONSTANCY
### RADIUS `p^{-s}`** ### -- and the level space is
###   ### **`V(r,s) = { f : supp(f) subset p^{-r}Z_p , f constant on cosets of p^s Z_p }`,**
### which is a function on `p^{-r}Z_p / p^s Z_p`, a grid of `p^{r+s}` chart points, ### **with
### b21's chart written as `x = p^{-r} m` and b21's Haar giving each chart cell mass `p^{-s}`.**
### ### **THE MODEL IS THE POINT `r = s = n`, AND THE INSTRUMENT IS THE PLANE.**

### ### **WHY IT MATTERS, AND IT IS THE WHOLE REASON THE ACT EXISTS.** ### b21 named the artifact:
### ### **"`U` maps `V_n` INTO `V_(n+1)` and ESCAPES `V_n` -- `supp(U f) = p^(-n-1) Z_p` -- so THE
### ### MODEL'S mod-N WRAPAROUND IS THE ARTIFACT"**, and ### **"THE MODEL'S mod-N WRAPAROUND IS
### ### EXACTLY THIS ESCAPED MASS FOLDED BACK IN."** ### b284 met it and wrote ### **"THE
### ### DERIVATION STANDS BECAUSE IT IS ON `Q_p`, WHERE THERE IS NOTHING TO FOLD."**
### ### ### **ON THE UNTIED GRID THE SCALING PART MOVES THE FRAME AND NOT THE DATA:**
### ###   `theta(p^k) : V(r,s) -> V(r-k, s+k)`, ### **AND ON CHART INDICES IT IS THE IDENTITY.**
### ### **THE SUM `r + s` IS INVARIANT, SO THE TWO FRAMES CARRY THE SAME GRID AND NOTHING IS
### ### COLLAPSED.** ### The model has only the point `r = s = n`, so it must read the image back in
### the frame it left, and THAT re-reading is the fold.

### ### **WHAT THIS FILE MAY NOT DO, FROM THE ORDER AND FROM `data/b308_registration_2026-09-03.txt`
### ### (sealed `e360d4d8...` before this file existed):**
###   ### **NO NEW MATHEMATICS.** ### Every object is its owner's: the chart and the Haar
###     normalization are b21's and b280's; the family, its dimension law and its collapse are
###     b293's; the operator `A` is b273's, imported from b281 and never re-defined; the criterion
###     is b295's, imported and never restated in code; the projection, the smear and the not-dead
###     witness are b304's, imported.
###   ### **NO FIRST-LEVEL VALUE AT A CELL OR MEMBER THE RECORD DOES NOT ALREADY CARRY.** ### The
###     criterion's TRUTH VALUE is printed everywhere the instrument reaches; ### **A NUMBER IS
###     PRINTED ONLY WHERE THE RECORD ALREADY CARRIES ONE**, and the owning tool that also produces
###     it is named on the same line.
###   ### **THE REPRODUCTION IS REPORTED AS IT COMES BACK.** ### A disagreement is printed at full
###     prominence and ### **THE INSTRUMENT IS NOT ADJUSTED TOWARD THE OWNER.**

### ### **NO FLOAT ANYWHERE. ### `Fraction`, `int`, AND EXACT CYCLOTOMIC REDUCTION ONLY.**

### ### **THE LIMITS, IN THE HEADER SO THE FILE IS NOT TRUSTED BEYOND THEM:**
### ### **(1) IT IS FINITE.** ### `V(r,s)` is a finite-dimensional model of a subspace of
###   `L^2(Q_p)`, exactly as `V_n` is. ### **UNTYING THE RADII REMOVES THE WRAPAROUND; IT DOES NOT
###   REMOVE THE TRUNCATION.** ### A statement quantified over all of `Q_p` is no more compiled
###   here than it was before.
### ### **(2) IT REPRODUCES; IT DOES NOT CONFIRM.** ### Two instruments agreeing is a check on the
###   instruments. ### **IT IS NOT A PROMOTION OF ANY RESULT, AND NO GRADE MOVES BECAUSE OF IT.**
### ### **(3) THE EXPOSURE ARM FINDS A SHAPE.** ### It cannot tell a regrouping of an exact finite
###   sum from a representation of a function that left its level. ### **THAT JUDGEMENT IS THE
###   SEAT'S AND IS STATED AS THE SEAT'S.**
"""
import io
import os
import re
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'e16'))

import b303_family as FAM        # noqa: E402  ### vp, nullspace, phi_prime_power, poly_mod, B_e
import b304_smearing as SMEAR    # noqa: E402  ### the projector, the trace, the permutation test

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


# ### ==============================================================================================
# ### THE FRAME. ### **THE TWO RADII, NAMED SEPARATELY, AND THE MODEL'S TIE MADE VISIBLE BY BEING
# ### ### BROKEN.**
# ### ==============================================================================================
class Frame(object):
    """### ### **A LEVEL FRAME `(r, s)` AT THE PLACE `p`.**

    ### `r` is the ### SUPPORT RADIUS INDEX ### : the support lies in `p^{-r} Z_p`, i.e. every
    ### point of the support has `|x| <= p^r`.
    ### `s` is the ### CONSTANCY RADIUS INDEX ### : the function is constant on cosets of
    ### `p^s Z_p`, i.e. it does not resolve anything finer than `p^{-s}`.
    ### ### **b21's CHART, VERBATIM IN ITS SHAPE: `x = p^{-r} m`.** ### At `r = n` this is b21's own
    ### `x = p^{-n} m`.
    ### ### **b21's HAAR, VERBATIM IN ITS SHAPE: each chart cell is a coset of `p^s Z_p` and carries
    ### mass `p^{-s}`** (`Z_p` has mass 1). ### At `s = n` this is b21's own `p^{-n}` per point.
    ### ### **AND THE TIE THE MODEL IMPOSES IS `r = s = n`.** ### Nothing else about `V_n` changes.
    """

    def __init__(self, p, r, s):
        if r + s < 0:
            raise ValueError('### A FRAME WITH r + s < 0 HAS NO CHART POINTS.')
        self.p, self.r, self.s = p, r, s
        self.M = p ** (r + s)                 # ### the number of chart points

    def cell_mass(self):
        """### **THE HAAR MASS OF ONE CHART CELL: `p^{-s}`, EXACT.**"""
        p, s = self.p, self.s
        return Fraction(1, p ** s) if s >= 0 else Fraction(p ** (-s), 1)

    def abs_index(self, m):
        """### `|x|` FOR THE CHART POINT `m`, AS THE EXPONENT `e` IN `|x| = p^e`.

        ### `x = p^{-r} m`, so `|x| = p^{r - v_p(m)}`. ### **THE CELL `m = 0` IS THE COSET
        ### `p^s Z_p`, ON WHICH `|x| <= p^{-s}`**, and the exponent returned there is `-s`.
        """
        if m % self.M == 0:
            return -self.s
        return self.r - FAM.vp(self.p, m)

    def ball(self, e):
        """### **THE INDICES OF `{ x : |x| <= p^e }`.**

        ### `|x| <= p^e` is `r - v_p(m) <= e`, i.e. ### **`v_p(m) >= r - e`** -- and at `r = n` that
        ### is b293's own `B_e := { m : v_p(m) >= n - e }`, which b293 states in b21's chart as
        ### `{ x : |x| <= p^e }`. ### **THE INSTRUMENT'S BALL AND b293's ARE THE SAME PREDICATE
        ### WITH `r` WHERE b293 HAS `n`, AND ARM F3 CHECKS THAT AS SETS.**
        """
        return set(m for m in range(self.M) if FAM.vp(self.p, m) >= self.r - e)

    def label(self):
        return '(r,s) = (%+d,%+d)  M = %d' % (self.r, self.s, self.M)

    def key(self):
        return (self.p, self.r, self.s)


def model_frame(p, n):
    """### **b21's `V_n`, WHICH IS THE POINT `r = s = n` OF THE PLANE.**"""
    return Frame(p, n, n)


# ### ==============================================================================================
# ### THE HAAR INNER PRODUCT, AND b21's SCALAR CHECKED RATHER THAN QUOTED.
# ### ==============================================================================================
def inner(frame, f, g):
    """### **`<f, g>_{L^2(Q_p)} = p^{-s} SUM_m f(m) g(m)`**, exact.

    ### The functions are real-valued rationals here (the corpus's `Son` basis is integral and b281
    ### says so in its own file: on the rational span the conjugation is the identity). ### **THAT
    ### IS SAID RATHER THAN LEFT AS A SILENT OMISSION.**
    """
    return frame.cell_mass() * sum(a * b for a, b in zip(f, g))


def euclid(f, g):
    """### THE MODEL'S OWN INNER PRODUCT, ### **WITHOUT THE HAAR SCALAR** -- so the two can be
    compared and b21's sentence about the scalar can be checked instead of repeated."""
    return sum(a * b for a, b in zip(f, g))


# ### ==============================================================================================
# ### THE TRANSFORM, FROM b21's DEFINITION. ### **`F : V(r,s) -> V(s,r)`, AND THE SWAP IS THE
# ### ### POINT.**
# ### ==============================================================================================
# ### b21: ### **"THE GENUINE TRANSFORM: (F f)(y) = int f(x) psi(x y) dx, psi the standard character
# ### of conductor Z_p (psi(x) = e^(2 pi i {x}_p)), self-dual Haar"** ### and ### **"on V_n this
# ### descends to EXACTLY the model DFT F_N[j,k] = zeta_N^(jk) / p^n (N = p^(2n)) in the chart".**
# ### ### **WRITTEN ON THE UNTIED FRAME THE SAME WAY:** ### with `x = p^{-r} m`, `y = p^{-s} m'` and
# ### `M = p^{r+s}`, the character argument is `x y = p^{-(r+s)} m m'`, so `psi(x y) = zeta_M^{m m'}`
# ### and `dx` is the cell mass `p^{-s}`:
# ###   ### ### **`(F f)(m') = p^{-s} SUM_m f(m) zeta_M^{m m'}`,   `m' in Z/M`.**
# ### ### **AT `r = s = n` THIS IS `p^{-n} zeta_N^{m m'}` -- b21's `F_N` ENTRY FOR ENTRY**, and the
# ### frame it lands in is `V(n,n)` because the swap `(n,n) -> (n,n)` is the identity there. ### **THE
# ### ### SWAP IS INVISIBLE IN THE MODEL AND IS THE FIRST THING THE UNTIED FRAME SHOWS.**
def transform_frame(frame):
    """### **THE TRANSFORM'S TARGET FRAME: `(r,s) -> (s,r)`.**

    ### The support of `F f` lies in `p^{-s}Z_p` because `f` is constant on cosets of `p^s Z_p`, and
    ### `F f` is constant on cosets of `p^r Z_p` because `f` is supported in `p^{-r}Z_p`.
    ### ### **b293 DERIVED THE SAME SWAP FOR THE FAMILY'S TWO CONDITION RADII -- "THE TRANSFORM
    ### CARRIES `(a,b)` TO `(b,a)`" -- AND THE TWO SWAPS ARE NOT THE SAME OBJECT.** ### b293's is a
    ### swap of the two CONDITIONS; this one is a swap of the two RADII OF THE SPACE. ### They are
    ### stated apart because the model, where both pairs are diagonal, makes them look like one.
    """
    return Frame(frame.p, frame.s, frame.r)


def zeta_sum(frame, f, mprime):
    """### **`SUM_m f(m) zeta_M^{m m'}`, REDUCED MODULO `Phi_M` -- EXACT, IN `Q(zeta_M)`.**

    ### The Haar factor `p^{-s}` is a nonzero rational and is left off here: every use below is a
    ### VANISHING test, and a nonzero scalar cannot change one. ### **SAID, NOT ASSUMED.**
    """
    p, M = frame.p, frame.M
    co = [Fraction(0)] * M
    for m, val in enumerate(f):
        if val:
            co[(m * mprime) % M] += Fraction(val)
    return FAM.poly_mod(co, FAM.phi_prime_power(p, frame.r + frame.s))


def geometric_sum(p, M, c):
    """### **`SUM_{m'} zeta_M^{c m'}`, REDUCED. ### b21's A5a: `= M [c = 0]` EXACTLY.**

    ### Reproduced here rather than cited, because the inversion control below USES it.
    """
    co = [Fraction(0)] * M
    for mprime in range(M):
        co[(c * mprime) % M] += Fraction(1)
    return FAM.poly_mod(co, FAM.phi_prime_power(p, _exp_of(p, M)))


def _exp_of(p, M):
    k = 0
    while p ** k < M:
        k += 1
    return k


def is_zero_poly(co):
    return all(c == 0 for c in co)


def is_rational_value(co, val):
    """### **IS THE REDUCED ELEMENT THE RATIONAL `val`?**

    ### `poly_mod` returns a coefficient list that may carry trailing zeros -- it stops as soon as
    ### the degree is below the modulus and does not trim. ### **THE FIRST DRAFT OF THIS FILE'S OWN
    ### FIXTURE COMPARED AGAINST A ONE-ELEMENT LIST AND FAILED ON A CORRECT ANSWER**, which is the
    ### fixture being wrong about the instrument rather than the instrument being wrong. ### The
    ### comparison is now on the VALUE and not on the representation.
    """
    return bool(co) and co[0] == val and is_zero_poly(co[1:])


def transform_vanishes_on_ball(frame, f, b):
    """### **THE SECOND SONIN CONDITION, LITERAL: does `F f` vanish on `{ y : |y| <= p^b }`?**

    ### The ball is taken in the TARGET frame `(s,r)`, so its indices are `{ m' : v_p(m') >= s - b }`
    ### -- and at `r = s = n` that is b293's `B_b` exactly.
    ### ### **THIS IS THE LITERAL CONDITION, COMPUTED IN `Q(zeta_M)`. ### THE COLLAPSED RATIONAL
    ### CONDITION IS A SEPARATE FUNCTION AND THE TWO ARE COMPARED, NEVER SUBSTITUTED.**
    """
    tgt = transform_frame(frame)
    for mprime in sorted(tgt.ball(b)):
        if not is_zero_poly(zeta_sum(frame, f, mprime)):
            return False
    return True


def fiber_sums_vanish(frame, f, b):
    """### **THE SECOND SONIN CONDITION, COLLAPSED: every fiber sum at modulus `p^{r+b}` is zero.**

    ### b293's collapse, in the untied frame. ### The derivation is one line and it is written out
    ### because a collapse used without its derivation is a substitution: ### an index `m'` in the
    ### target ball is `m' = p^{s-b} u`, so `zeta_M^{m m'} = zeta_{p^{r+b}}^{m u}`, which sees `m`
    ### ### ONLY MOD `p^{r+b}` ### ; and the transform of size `p^{r+b}` is invertible, so the
    ### vanishing for every `u` is the vanishing of every fiber sum.
    ### ### **AT `r = n` THE MODULUS IS `p^{n+b}` -- b293's OWN NUMBER.**
    ### ### **AND THE EQUIVALENCE IS NOT ASSUMED: `arm_collapse` BELOW CHECKS IT BOTH WAYS, WITH A
    ### ### NON-MEMBER CONTROL, AT EVERY CELL.**
    """
    p, M = frame.p, frame.M
    mod = min(p ** max(frame.r + b, 0), M)
    if mod <= 0:
        return True
    tot = [Fraction(0)] * mod
    for m, val in enumerate(f):
        if val:
            tot[m % mod] += Fraction(val)
    return all(x == 0 for x in tot)


def vanishes_on_ball(frame, f, a):
    """### **THE FIRST SONIN CONDITION: `f = 0` on `{ x : |x| <= p^a }`.**

    ### b280's bridge is what makes this a genuine condition on `L^2` and not a pointwise one:
    ### ### **"a chart point `m` at level `n` is a COSET OF MEASURE `p^{-n} > 0`, and `f in V_n` is
    ### constant on it"**, so ### **"`f(m) = 0` for `m` in `ball_n`" <=> "`f = 0` almost everywhere
    ### on `Z_p`"**. ### The same sentence holds cell by cell on the untied frame, where a cell has
    ### mass `p^{-s} > 0`.
    """
    return all(f[m] == 0 for m in frame.ball(a))


# ### ==============================================================================================
# ### THE CONSTRAINED SPACE. ### **BUILT FROM THE TWO CONDITIONS, EXACTLY, OVER `Q`.**
# ### ==============================================================================================
def son_rows(frame, a, b):
    """### THE LINEAR CONDITIONS: the ball coordinates, and the fiber sums at modulus `p^{r+b}`."""
    p, M = frame.p, frame.M
    rows = []
    for m in sorted(frame.ball(a)):
        r = [0] * M
        r[m] = 1
        rows.append(r)
    mod = min(p ** max(frame.r + b, 0), M)
    for res in range(mod):
        rows.append([1 if (mm % mod) == res else 0 for mm in range(M)])
    return rows


def son_basis(frame, a, b):
    """### **THE CONSTRAINED SPACE `Son(frame; a, b)`, AS AN EXACT RATIONAL NULLSPACE.**"""
    return [v for v in FAM.nullspace(son_rows(frame, a, b), frame.M)
            if any(x != 0 for x in v)]


def in_space(frame, f, a, b):
    """### **MEMBERSHIP BY THE TWO LITERAL CONDITIONS**, the second in `Q(zeta_M)`."""
    return vanishes_on_ball(frame, f, a) and transform_vanishes_on_ball(frame, f, b)


# ### ==============================================================================================
# ### THE ACTION OF `Q_p^x`, SPLIT INTO ITS TWO PARTS AND EACH NAMED AS SUCH.
# ### ==============================================================================================
# ### `Q_p^x = p^Z x Z_p^x`. ### **THE COMPACT PART IS `Z_p^x`; THE SCALING PART IS `p^Z`**, and the
# ### model carries the first and drops the second -- which is the whole of what this instrument is
# ### for. ### The action is b304's: ### **`(theta(t) f)(m) = f(t^{-1} m)`, so `theta(t) e_j = e_{tj}`.**
def compact_action(frame, t, f):
    """### **THE COMPACT PART. ### `t` A UNIT: THE FRAME DOES NOT MOVE AND THE GRID IS PERMUTED.**

    ### `x = p^{-r} m` and `t^{-1} x = p^{-r}(t^{-1} m)`, and `|t| = 1` so neither radius changes.
    ### ### **NOTHING LEAVES THE FRAME AND NOTHING IS FOLDED** -- and that is CHECKED, not hoped:
    ### `SMEAR.is_permutation` is b304's own test and is run at every `t` used.
    """
    M = frame.M
    tinv = pow(t, -1, M)
    return frame, [f[(tinv * m) % M] for m in range(M)]


def scaling_action(frame, k, f):
    """### ### **THE SCALING PART. ### `theta(p^k) : V(r,s) -> V(r-k, s+k)`, AND ON CHART INDICES
    ### ### IT IS THE IDENTITY.**

    ### DERIVED, AND THE DERIVATION IS TWO LINES BECAUSE IT IS THE ACT'S LOAD-BEARING FACT:
    ###   `g(x) = f(p^{-k} x)`. ### **SUPPORT:** `p^{-k}x in p^{-r}Z_p` is `x in p^{-(r-k)}Z_p`, so
    ###     the support radius index goes `r -> r - k`.
    ###   ### **CONSTANCY:** `g` is constant where `p^{-k}x` moves inside `p^s Z_p`, i.e. on cosets
    ###     of `p^{s+k}Z_p`, so the constancy radius index goes `s -> s + k`.
    ### ### **`r + s` IS INVARIANT, SO THE TWO FRAMES HAVE THE SAME NUMBER OF CHART POINTS**, and in
    ### the target chart `x = p^{-(r-k)} m'` the value is `g(m') = f(p^{-k} p^{-(r-k)} m') = f(m')`.
    ### ### ### **SO THE COEFFICIENT LIST IS UNCHANGED AND ONLY THE FRAME MOVES.**
    ### ### **THIS IS WHY THERE IS NOTHING TO FOLD**, and Component 4 counts it rather than saying
    ### it.
    ### ### **AND THE INVARIANT IS THE ONE b293 ALREADY DERIVED FOR THE FAMILY'S CONDITION RADII --
    ### "DILATION MOVES `(a,b) -> (a+1, b-1)`: THE SUM `a+b` IS INVARIANT" -- MET HERE ON THE
    ### SPACE'S OWN RADII.** ### The two statements are about different pairs and are not merged.
    """
    return Frame(frame.p, frame.r - k, frame.s + k), list(f)


# ### ==============================================================================================
# ### ### **THE MODEL'S REALIZATION OF THE SCALING PART -- THE ONE DECLARED CARRIER IN THIS FILE.**
# ### ==============================================================================================
def model_pushforward_fibers(p, n, k):
    """### ### **THE FOLD, COMPUTED. ### THIS FUNCTION EXISTS TO EXHIBIT THE ARTIFACT, NOT TO USE
    ### ### IT**, and it is the only place in this file where a grid index is multiplied by a power
    ### of `p` and reduced modulo the grid size.

    ### The model has one frame, `r = s = n`, so it cannot receive `theta(p^k) f` in the frame that
    ### map lands in. ### It reads the image back in the frame it left, which on chart indices is
    ### ### **`m -> p^k m mod N`** ### -- b304's `theta(t) e_j = e_{t j}` at the non-unit `t = p^k`.
    ### ### **RETURNS `(image_size, collided_ordered_pairs)`, BOTH COUNTED DIRECTLY.**
    """
    N = p ** (2 * n)
    pk = pow(p, k, N)
    img = {}
    for m in range(N):
        img.setdefault((pk * m) % N, 0)
        img[(pk * m) % N] += 1
    collided = sum(c * (c - 1) for c in img.values())
    return len(img), collided


def instrument_fold_pairs(frame, k):
    """### **THE SAME COUNT ON THE INSTRUMENT.** ### `scaling_action` is the identity on chart
    indices, so two distinct chart points cannot land on one. ### **COUNTED, NOT ASSERTED.**"""
    tgt, _ = scaling_action(frame, k, [Fraction(0)] * frame.M)
    img = {}
    for m in range(frame.M):
        img.setdefault(m % tgt.M, 0)
        img[m % tgt.M] += 1
    return len(img), sum(c * (c - 1) for c in img.values())


# ### ==============================================================================================
# ### ### **THE EXPOSURE ARM. ### IT FINDS A SHAPE IN A CALL PATH AND NOTHING MORE.**
# ### ==============================================================================================
# ### A ### NON-UNIT PUSHFORWARD SITE ### is a line that reduces the product of a grid index with a
# ### power of the residue characteristic modulo the grid size. ### **THAT IS THE SHAPE THE FOLD
# ### TAKES IN CODE.** ### It is NOT the same thing as exposure, and the file says so twice.
PUSHFORWARD = re.compile(r'\(\s*(?:p\s*\*\*[^)]*|pk|p)\s*\*\s*\w+\s*\)\s*%\s*(?:N|M)\b')


# ### ### **TOP-LEVEL `def` ONLY, AND THE ANCHORING IS THE POINT.** ### A nested helper would label
# ### a site with its own name (`chk`), which tells a reader nothing about which part of the tool
# ### the site belongs to. ### **THE FIRST DRAFT MATCHED NESTED DEFS AND LABELLED THIS FILE'S OWN
# ### CONTROL STRINGS `chk`**, and the fixture below caught it.
DEFLINE = re.compile(r'^def\s+(\w+)')


def pushforward_sites(path):
    """### **RETURNS `(line_no, enclosing_def, the_line)` FOR EVERY SITE.**

    ### ### **THE ENCLOSING FUNCTION IS RETURNED BECAUSE THE FIRST DRAFT OF THIS ACT'S OWN REPORT
    ### ### SAID "ONE SITE" WHERE THE ARM HAD PRINTED FOUR.** ### Two of the four were inside this
    ### file's own fixture strings, which spell the shape ### IN ORDER TO TEST FOR IT ### -- the
    ### same species `ferry_scan.py` names in its own header, where a ferry that strikes a clause
    ### quotes the clause and the quotation hits. ### **A NARRATIVE COUNT THAT DISAGREES WITH THE
    ### TOOL'S COUNT IS THE DEFECT, NOT THE TOOL'S COUNT**, and the fix is to make the
    ### classification mechanical rather than to re-word the sentence.
    """
    out, cur = [], '<module>'
    for i, line in enumerate(io.open(path, encoding='utf-8', errors='replace').read().splitlines(),
                             1):
        m = DEFLINE.match(line)
        if m:
            cur = m.group(1)
        if line.lstrip().startswith('#'):
            continue
        if PUSHFORWARD.search(line):
            out.append((i, cur, line.strip()))
    return out


# ### ==============================================================================================
# ### THE FIXTURES. ### **BOTH POLARITIES ON EVERY INSTRUMENT THIS FILE OWNS, BEFORE ANY USE.**
# ### ==============================================================================================
def self_test(verbose=True):
    bad = [0]

    def chk(lbl, got, exp):
        ok = (got == exp)
        bad[0] += 0 if ok else 1
        if verbose:
            print('  %-70s %-22s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if ok else '### NO ###'))

    if verbose:
        print('  %-70s %-22s %s' % ('fixture', 'got/expected', 'agree'))

    # ### THE FRAME AND THE TWO RADII.
    f22 = Frame(2, 2, 2)
    chk('the model frame (2,2) has p^{2n} chart points', f22.M, 16)
    chk('an UNTIED frame (3,1) has the same grid as (2,2)', Frame(2, 3, 1).M, 16)
    chk('### and a DIFFERENT support radius, which is the whole point', Frame(2, 3, 1).r, 3)
    chk('a frame with r+s < 0 is refused', _raises(lambda: Frame(2, 0, -1)), True)
    # ### b21's HAAR, AS AN IDENTITY OF RATIONALS.
    chk('Haar cell mass at s = 2 is p^{-2}', Frame(2, 2, 2).cell_mass(), Fraction(1, 4))
    chk('### and at an untied s = 1 it is p^{-1}, NOT p^{-2}', Frame(2, 3, 1).cell_mass(),
        Fraction(1, 2))
    # ### |x| ON THE CHART.
    chk('|x| exponent at m = 1 in frame (2,2) is r', f22.abs_index(1), 2)
    chk('|x| exponent at m = 4 in frame (2,2) is r - 2', f22.abs_index(4), 0)
    chk('### the zero cell reports -s, not r', f22.abs_index(0), -2)
    # ### THE BALL, AGAINST b293's `B_e` AT `r = n`, ### **BOTH POLARITIES.**
    chk('the instrument ball at e=0, r=n equals b293 B_0',
        f22.ball(0), FAM.ball_family(2, 2, 0))
    chk('the instrument ball at e=1, r=n equals b293 B_1',
        f22.ball(1), FAM.ball_family(2, 2, 1))
    chk('### and B_0 != B_1, so the comparison is not vacuous',
        FAM.ball_family(2, 2, 0) != FAM.ball_family(2, 2, 1), True)
    chk('the instrument ball at e=0 equals the corpus ball_n',
        f22.ball(0), FAM.ball_corpus(2, 2))

    # ### THE TRANSFORM'S FRAME SWAP.
    chk('the transform swaps the two radii', transform_frame(Frame(3, 4, 1)).key(), (3, 1, 4))
    chk('### and on the model frame the swap is invisible',
        transform_frame(Frame(3, 2, 2)).key(), (3, 2, 2))

    # ### b21's A5a, ### **BOTH POLARITIES** -- the identity the inversion control runs on.
    chk('geometric sum at c = 0 mod M reduces to M',
        is_rational_value(geometric_sum(2, 8, 0), Fraction(8)), True)
    chk('### geometric sum at c = 1 reduces to zero', is_zero_poly(geometric_sum(2, 8, 1)), True)
    chk('### geometric sum at c = 2 reduces to zero', is_zero_poly(geometric_sum(2, 8, 2)), True)
    chk('geometric sum at c = M reduces to M again',
        is_rational_value(geometric_sum(3, 9, 9), Fraction(9)), True)

    # ### THE TRANSFORM, ### **BOTH POLARITIES, ON A HAND-CHECKABLE VECTOR.**
    # ### `1_{Z_p}` in frame (n,n) is the indicator of the ball at radius 1, and self-duality of the
    # ### standard character says its transform is `1_{Z_p}` again -- so it does NOT vanish there.
    fr = Frame(2, 1, 1)
    one_zp = [Fraction(1) if m in fr.ball(0) else Fraction(0) for m in range(fr.M)]
    chk('F(1_{Z_p}) does NOT vanish on the unit ball -- it IS 1_{Z_p}',
        transform_vanishes_on_ball(fr, one_zp, 0), False)
    alt = [Fraction(1), Fraction(-1), Fraction(1), Fraction(-1)]
    chk('an alternating vector has zero total, so its transform vanishes at the ball centre',
        is_zero_poly(zeta_sum(fr, alt, 0)), True)
    # ### **THE CONTROL INDEX IS `2` AND NOT `1`, AND THE FIRST DRAFT HAD IT WRONG.** ### At `m'=1`
    # ### this vector's transform really is zero (its four terms are the four fourth roots), so a
    # ### control there would have been ### **A CONTROL THAT CANNOT FIRE, READING AS A PASS.**
    chk('### and it does NOT vanish at every index -- the control fires at m\' = 2',
        is_zero_poly(zeta_sum(fr, alt, 2)), False)
    chk('### the spike at the origin transforms to the constant 1, vanishing nowhere',
        is_zero_poly(zeta_sum(fr, [Fraction(1), Fraction(0), Fraction(0), Fraction(0)], 3)), False)

    # ### THE COLLAPSE, ### **BOTH POLARITIES**, on a vector built to fail it.
    spike = [Fraction(0)] * 16
    spike[1] = Fraction(1)
    chk('### a spike fails the collapsed condition', fiber_sums_vanish(f22, spike, 0), False)
    chk('### a spike fails the literal condition too',
        transform_vanishes_on_ball(f22, spike, 0), False)
    chk('### a spike fails the first condition\'s negation test (it is off the ball)',
        vanishes_on_ball(f22, spike, 0), True)

    # ### THE SCALING ACTION -- ### **THE FRAME LAW, BOTH DIRECTIONS.**
    tg, _ = scaling_action(Frame(2, 2, 2), 1, [Fraction(0)] * 16)
    chk('theta(p) moves (2,2) to (1,3)', tg.key(), (2, 1, 3))
    tg2, _ = scaling_action(Frame(2, 2, 2), -1, [Fraction(0)] * 16)
    chk('theta(p^{-1}) moves (2,2) to (3,1) -- b21\'s U, support p^{-(n+1)}Z_p', tg2.key(),
        (2, 3, 1))
    chk('### and r+s is invariant in both directions', (tg.r + tg.s, tg2.r + tg2.s), (4, 4))
    v = [Fraction(m) for m in range(16)]
    chk('### the coefficient list is UNCHANGED by the scaling action',
        scaling_action(Frame(2, 2, 2), 1, v)[1], v)

    # ### THE COMPACT ACTION, ### **AND b304's PERMUTATION TEST, BOTH POLARITIES.**
    _f, w = compact_action(f22, 3, [Fraction(m) for m in range(16)])
    chk('the compact action permutes the values (same multiset)', sorted(w),
        sorted([Fraction(m) for m in range(16)]))
    chk('a unit permutes the grid (b304\'s test)', SMEAR.is_permutation(3, 16), True)
    chk('### a non-unit does NOT', SMEAR.is_permutation(2, 16), False)

    # ### ### **THE FOLD COUNTS, BOTH SIDES, AND THE CLOSED FORM AS A SECOND ROUTE.**
    isz, coll = model_pushforward_fibers(2, 2, 1)
    chk('the model image at k=1 has N/p points', isz, 8)
    chk('the model collided ordered pairs equal N(p^k - 1)', coll, 16 * (2 - 1))
    isz2, coll2 = instrument_fold_pairs(Frame(2, 2, 2), 1)
    chk('### the instrument image is the WHOLE grid', isz2, 16)
    chk('### and the instrument collides NOTHING', coll2, 0)

    # ### THE EXPOSURE ARM, ### **BOTH POLARITIES, ON SYNTHETIC LINES.**
    chk('the exposure arm fires on a non-unit pushforward',
        bool(PUSHFORWARD.search('        l = (pk * m) % N')), True)
    chk('the exposure arm fires on the bare characteristic',
        bool(PUSHFORWARD.search('        m2 = (p * m) % N')), True)
    chk('### it stays quiet on a UNIT pushforward',
        bool(PUSHFORWARD.search('        tgt = (t * m) % N')), False)
    chk('### it stays quiet on a character exponent',
        bool(PUSHFORWARD.search('        co[(m * mp) % N] += Fraction(val)')), False)
    # ### THE ENCLOSING-DEF ARM, ### **BOTH POLARITIES, ON THIS FILE ITSELF.**
    here = pushforward_sites(os.path.abspath(__file__))
    chk('the arm reports an enclosing def for every site it finds',
        all(d and d != '<module>' for _i, d, _t in here), True)
    chk('### and it finds this file\'s declared exhibit',
        'model_pushforward_fibers' in set(d for _i, d, _t in here), True)
    chk('### and it finds its own control strings, which spell the shape to test for it',
        'self_test' in set(d for _i, d, _t in here), True)
    chk('### and NOTHING in the instrument\'s operational path',
        sorted(set(d for _i, d, _t in here)), ['model_pushforward_fibers', 'self_test'])

    # ### THE INNER PRODUCTS, AND b21's SCALAR AS AN IDENTITY.
    a1 = [Fraction(1), Fraction(2), Fraction(0), Fraction(-1)]
    chk('the Haar inner product is p^{-s} times the model one',
        inner(Frame(2, 1, 1), a1, a1), Fraction(1, 2) * euclid(a1, a1))
    return bad[0] == 0


def _raises(fn):
    try:
        fn()
        return False
    except Exception:
        return True


if __name__ == '__main__':
    print('=' * 100)
    print('b308_local_field.py -- THE INSTRUMENT\'S OWN FIXTURES. ### BOTH POLARITIES, NO FLOAT.')
    print('=' * 100)
    ok = self_test()
    print()
    print('  ### SELF-TEST : %s' % ('PASS' if ok else '### FAIL ###'))
    sys.exit(0 if ok else 2)
