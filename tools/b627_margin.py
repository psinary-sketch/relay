# -*- coding: utf-8 -*-
"""b627_margin.py -- THE MARGIN BENCH OF b627, UNDER (R237)(5) AND THE AUTHOR'S THREE ANSWERS BEFORE THE SEAL. ### A T3/T4 BENCH WITH NO CLAIM.

### ### WHAT IT COMPUTES. At each of the lowest N ordinates t of Odlyzko's table, Q(t) = poleTerm k_t - primeSum k_t + archTerm k_t,
### the right side of the kernel's b321_identity, from the prime side, at k_t = weilTest φ_t φ_t, φ_t(u) = cos(t u)·window W h p (u)
### (b519's modulation convention, the author's answer): the explicit formula's left side evaluated at a window centred on a known zero.
### A positive value is the prime side agreeing with the zero side where the zero side is known; the bench measures that agreement's
### margin -- a bench of the identity's two sides, NOT A TEST OF POSITIVITY BEYOND THE TABLE, and no statement about any zero.
### ### HOW. python-flint Arb balls at PREC bits throughout (the author's answer): the window exact (its pieces exact rationals, the
### recursion of PlateauRamp.lean :55-:57 carried out on them); k_t(log n) by exact integration of the pieces' products against
### cos(t v) cos(t (u - v)) (the oscillatory part by the closed antiderivative Σ_k (-1)^k P^(k)(v) / (2it)^(k+1) e^(2itv)); the prime
### sum over every n ≤ NMAX, exact since k_t vanishes beyond |u| = 2L = 10; the pole term at ±i/2 and the archimedean integrand by the
### closed-form transform of PlateauRamp.lean :151-:153; the archimedean integral by acb.integral (Arb's own error bound) on
### [0, t + DELTA], the integrand even, the closed-form tail bound beyond the cut added to the radius:
###     |paperFT w z| ≤ (2/|z|)(2/(|z| h))^p on ℝ, so |k̂_t(r)| ≤ C/(r - t)^14 for r ≥ t + 6, C = (2·6^6)^2 at W = 4, h = 1/3, p = 6;
###     |gammaBracket r| ≤ log(1 + r) + 6 for r ≥ 1 (ψ(z) = ψ(z + 1) - 1/z; Binet: |ψ(z) - log z + 1/(2z)| ≤ 1/12 for Re z ≥ 1);
###     ∫_R^∞ ≤ C (log(1 + R) + 6) / (12 (R - t)^13), both sides, times 1/(2π).
### mpmath only for the midpoint cross-check (the author's answer). Every value printed as midpoint ± radius; positive means the
### whole ball lies above zero, a ball straddling zero is printed STRADDLES and counted neither way.
### ### MODES. `inputs <capture>`: the zero table's one read (the seat's capture), the ordinates taken, the parameters and the kernel
### lines, banked as data/b627_margin_inputs.txt BEFORE ANY COMPUTATION. `run <a> <b> <out>`: ordinates a..b from the inputs bank, one
### row each. `check <out> <j>...`: the mpmath midpoint cross-check at the ordinates named, and the conventions' check at the first.
### `assemble <out> <part>...`: the bank -- the rows, the minimum over N with its ordinate, the nearest-neighbour spacing at each ordinate
### and once the margin's least-squares log-log slope against height, A CENTRE LINE AND NOT A BOUND; nothing is scored against either.
### No platform call; it writes only the file it is given.
"""
import hashlib
import io
import os
import re
import sys

from flint import acb, arb, arb_poly, ctx, fmpq, fmpq_poly

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b627_worklist as K  # noqa: E402

NL = chr(10)
ctx.prec = K.PREC
INPUTS = os.path.join(ROOT, 'data', 'b627_margin_inputs.txt')

# ================================================================================ THE KERNEL'S DEFINITIONS, TRANSCRIBED
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :45: def box (a : ℝ) : ℝ → ℝ := Set.indicator (Set.Icc (-a) a) (fun _ => 1)
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :48: def nbox (h : ℝ) : ℝ → ℝ := fun x => h⁻¹ * box (h / 2) x
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :51: def conv (f g : ℝ → ℝ) : ℝ → ℝ := MeasureTheory.convolution f g (ContinuousLinearMap.lsmul ℝ ℝ) volume
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :55: def window (W h : ℝ) : ℕ → ℝ → ℝ
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :56:   | 0 => box W
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :57:   | p + 1 => conv (window W h p) (nbox h)
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :151: def ClosedFormFT (W h : ℝ) : Prop :=
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :152:   ∀ (p : ℕ) (z : ℂ), z ≠ 0 → Zeta23.paperFT (phiC (window W h p)) z =
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :153:     (2 * Complex.sin (z * (W : ℂ)) / z) * (2 * Complex.sin (z * ((h / 2 : ℝ) : ℂ)) / (z * (h : ℂ))) ^ p
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :156: def WindowInClassK (W h : ℝ) : Prop :=
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :157:   ∀ p : ℕ, 6 ≤ p → ContDiff ℝ 4 (window W h p) ∧ (∀ x, window W h p (-x) = window W h p x) ∧
# v0.20 SIDEExplicitFormula/Schema/PlateauRamp.lean :158:     HasCompactSupport (window W h p) ∧ classK (Zeta23.EF.weilTest (phiC (window W h p)) (phiC (window W h p)))
# v0.20 SIDEExplicitFormula/B321Identity.lean :24: def zeroSide (k : ℝ → ℂ) : ℂ :=
# v0.20 SIDEExplicitFormula/B321Identity.lean :25:   ∑' ρ : Zeta23.zetaZeroConfig.carrier,
# v0.20 SIDEExplicitFormula/B321Identity.lean :26:     (Zeta23.zetaZeroConfig.mult ρ : ℂ) * Zeta23.paperFT k (Zeta23.gammaOf ρ)
# v0.20 SIDEExplicitFormula/B321Identity.lean :29: def poleTerm (k : ℝ → ℂ) : ℂ :=
# v0.20 SIDEExplicitFormula/B321Identity.lean :30:   Zeta23.paperFT k (I / 2) + Zeta23.paperFT k (-I / 2)
# v0.20 SIDEExplicitFormula/B321Identity.lean :33: def primeSum (k : ℝ → ℂ) : ℂ :=
# v0.20 SIDEExplicitFormula/B321Identity.lean :34:   ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (2 * k (Real.log n))
# v0.20 SIDEExplicitFormula/B321Identity.lean :37: def archTerm (k : ℝ → ℂ) : ℂ :=
# v0.20 SIDEExplicitFormula/B321Identity.lean :38:   (1 / (2 * π) : ℂ) * ∫ r : ℝ, Zeta23.paperFT k r * (Zeta23.EF.gammaBracket r : ℂ)
# v0.20 SIDEExplicitFormula/B321Identity.lean :44: theorem b321_identity (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k) (hs : HasCompactSupport k)
# v0.20 SIDEExplicitFormula/B321Identity.lean :45:     (he : ∀ x : ℝ, k (-x) = k x) :
# v0.20 SIDEExplicitFormula/B321Identity.lean :46:     zeroSide k = b321Norm * (poleTerm k - primeSum k + archTerm k) := by
# v0.20 Zeta23/ExplicitFormula.lean :64: def tilde (g : ℝ → ℂ) : ℝ → ℂ := fun u => conj (g (-u))
# v0.20 Zeta23/ExplicitFormula.lean :68: def weilTest (f g : ℝ → ℂ) : ℝ → ℂ := f ⋆[ContinuousLinearMap.mul ℝ ℂ] tilde g
# v0.20 Zeta23/ExplicitFormula.lean :80: def gammaBracket (r : ℝ) : ℝ := (Complex.digamma (1 / 4 + I * r / 2)).re - Real.log π
# v0.20 Zeta23/Defs.lean :60: def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))
# v0.20 SIDEExplicitFormula/H2Sign.lean :24: def classK (k : ℝ → ℂ) : Prop :=
# v0.20 SIDEExplicitFormula/H2Sign.lean :25:   (∀ x : ℝ, k (-x) = k x) ∧ ContDiff ℝ 2 k ∧ HasCompactSupport k ∧
# v0.20 SIDEExplicitFormula/H2Sign.lean :26:     ∃ h : ℝ → ℂ, ContDiff ℝ 2 h ∧ HasCompactSupport h ∧ k = Zeta23.EF.weilTest h h
# ### Read here: φ_t is real and even, so tilde φ_t = φ_t (:64) and k_t = φ_t ⋆ φ_t (:68), even, C², supported in [-2L, 2L];
# ### paperFT k_t = (paperFT φ_t)² (the convolution theorem), paperFT φ_t (z) = (ŵ(z - t) + ŵ(z + t))/2 with ŵ the closed form of
# ### :151-:153 -- in the kernel an obligation (ConvStep, :173), here the classical identity, used for the pole and archimedean terms;
# ### the prime sum reads k_t itself from the window's exact pieces, not from the transform.

W, H, P = fmpq(K.W), fmpq(K.H_NUM, K.H_DEN), K.P
L = W + P * H / 2
assert L == K.L_SUPPORT


def _shift(poly, c):
    return poly(fmpq_poly([c, 1]))


def window_pieces():
    """### window W h p as exact pieces [(a, b, poly)], by the kernel's recursion: window 0 = box W (:56); window (p+1) = conv
    ### (window p) (nbox h) (:57), i.e. x ↦ h⁻¹ ∫_{x-h/2}^{x+h/2} window p (:48, :51)."""
    pcs = [(-W, W, fmpq_poly([1]))]
    for _ in range(P):
        F, acc = [], fmpq(0)
        for a, b, q in pcs:
            Q = q.integral()
            Q = Q - Q(a) + acc
            F.append((a, b, Q))
            acc = Q(b)
        total = acc

        def piece_of(x, F=F, total=total):
            if x <= F[0][0]:
                return fmpq_poly([0])
            if x >= F[-1][1]:
                return fmpq_poly([total])
            for a, b, Q in F:
                if a <= x <= b:
                    return Q
        knots = sorted(set([a + s * H / 2 for a, b, q in pcs for s in (-1, 1)] + [b + s * H / 2 for a, b, q in pcs for s in (-1, 1)]))
        pcs = [(lo, hi, (_shift(piece_of((lo + hi) / 2 + H / 2), H / 2) - _shift(piece_of((lo + hi) / 2 - H / 2), -H / 2)) * (1 / H))
               for lo, hi in zip(knots, knots[1:])]
    return pcs


PCS = window_pieces()
APCS = [(arb(a), arb(b), arb_poly([arb(c) for c in q.coeffs()]), i) for i, (a, b, q) in enumerate(PCS)]
W_, H_ = arb(K.W), arb(K.H_NUM) / K.H_DEN


def per_n(u):
    """### the t-independent data at u = log n: A(u) = (w ⋆ w)(u) and, per endpoint e of the pieces' overlaps, (2e - u, Epoly, Opoly)
    ### with ∫_α^β P(v) cos(t(2v - u)) dv = Σ_e [cos(t(2e - u)) Opoly(y) + sin(t(2e - u)) Epoly(y)], y = 1/(2t)."""
    A = arb(0)
    ends = {}
    for a_i, b_i, Pi, i in APCS:
        for a_j, b_j, Pj, j in APCS:
            lo1, hi1 = u - b_j, u - a_j
            if hi1 <= a_i or b_i <= lo1:
                continue
            if not (hi1 > a_i and b_i > lo1):
                raise ValueError('undecided overlap at u = %s' % u)
            if a_i >= lo1:
                al, ka = a_i, ('k', i)
            elif lo1 > a_i:
                al, ka = lo1, ('u', j + 1)
            else:
                raise ValueError('undecided lower end')
            if b_i <= hi1:
                be, kb = b_i, ('k', i + 1)
            elif hi1 < b_i:
                be, kb = hi1, ('u', j)
            else:
                raise ValueError('undecided upper end')
            R = Pi * Pj(arb_poly([u, -1]))
            Ri = R.integral()
            A += Ri(be) - Ri(al)
            for e, key, sg in ((be, kb, 1), (al, ka, -1)):
                d = ends.setdefault(key, [e, [arb(0)] * 13])
                Rk = R
                for k in range(13):
                    d[1][k] += sg * Rk(e)
                    Rk = Rk.derivative()
    out = []
    for key in sorted(ends):
        e, Dk = ends[key]
        Ec, Oc = [arb(0)] * 14, [arb(0)] * 14
        for k in range(13):
            s = 1 if (k // 2) % 2 == 0 else -1
            if k % 2 == 0:
                Ec[k + 1] = s * Dk[k]
            else:
                Oc[k + 1] = s * Dk[k]
        out.append((2 * e - u, arb_poly(Ec), arb_poly(Oc)))
    return A, out


def prime_powers(N):
    sv = bytearray([1]) * (N + 1)
    sv[0] = sv[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if sv[i]:
            sv[i * i::i] = bytearray(len(sv[i * i::i]))
    out = []
    for p in range(2, N + 1):
        if sv[p]:
            q = p
            while q <= N:
                out.append((q, p))
                q *= p
    return sorted(out)


def what(z):
    """### ŵ(z) = (2 sin(zW)/z)(2 sin(zh/2)/(zh))^p = 2W sinc(zW) sinc(zh/2)^p, :151-:153 (entire; its value at 0 by continuity)."""
    zz = acb(z)
    return 2 * W_ * (zz * W_).sinc() * ((zz * H_ / 2).sinc()) ** P


def phihat(z, t):
    return (what(z - t) + what(z + t)) / 2


def prime_sum(t, pre):
    S = arb(0)
    y = 1 / (2 * t)
    for lam, u, (A, ends) in pre:
        osc = arb(0)
        for th, Ep, Op in ends:
            s, co = (t * th).sin_cos()
            osc += co * Op(y) + s * Ep(y)
        S += lam * ((t * u).cos() * A + osc)       # ### Λ(n)/√n · 2 k_t(log n), k_t = (cos(tu) A + osc)/2
    return S


def arch(t):
    pi = arb.pi()
    lpi = pi.log()

    def f(r, analytic):
        a = acb(0.25) + acb(0, 1) * r / 2
        b = acb(0.25) - acb(0, 1) * r / 2
        g = (a.digamma() + b.digamma()) / 2 - lpi      # ### = gammaBracket r on ℝ (:80), holomorphic in |Im r| < 1/2
        ph = phihat(r, t)
        return ph * ph * g
    R = t + K.DELTA
    I = acb.integral(f, 0, R, abs_tol=arb(2) ** -110)
    C = (2 * arb(6) ** 6) ** 2
    tail = 2 * C * ((R + 1).log() + 6) / (12 * arb(K.DELTA) ** 13) / (2 * pi)
    return I / pi, tail                                  # ### (1/2π) ∫_ℝ = (1/π) ∫_0^∞, the integrand even


def ordinates():
    t = io.open(INPUTS, encoding='utf-8').read()
    return [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^ORD (\d+) (\S+)$', t, re.M)]


def _s(x, n=34):
    return x.mid().str(n, radius=False)


def _r(x):
    return x.rad().str(3, radius=False)


def run(a, b, out):
    ords = [o for o in ordinates() if a <= o[0] <= b]
    pp = prime_powers(K.NMAX)
    assert arb(K.NMAX + 1).log() > 2 * K.L_SUPPORT and arb(K.NMAX).log() < 2 * K.L_SUPPORT
    pre = []
    for n, p in pp:
        u = arb(n).log()
        pre.append((arb(p).log() / arb(n).sqrt(), u, per_n(u)))
    rows = []
    for j, ts in ords:
        t = arb(ts)
        ph = phihat(acb(0, 0.5), t)
        pole = 2 * ph * ph
        S = prime_sum(t, pre)
        A, tail = arch(t)
        Qc = pole - S + A
        Q = Qc.real + arb(0, tail.upper())
        im0 = Qc.imag.contains(0)
        pos = 'YES' if Q > 0 else ('NO' if Q < 0 else 'STRADDLES')
        rows.append('ROW %d t=%s Q=%s rad=%s pole=%s prime=%s arch=%s tail=%s im_contains_0=%s positive=%s' % (
            j, ts[:32], _s(Q), _r(Q), _s(pole.real, 20), _s(S, 20), _s(A.real, 20), tail.upper().str(3, radius=False), im0, pos))
        print(rows[-1][:200], flush=True)
    b_ = (NL.join(['### prime powers %d (n ≤ %d) ; pieces %d' % (len(pp), K.NMAX, len(PCS))] + rows) + NL).encode('utf-8')
    open(out, 'wb').write(b_)


def check(out, *js):
    """### the mpmath midpoint cross-check: k_t(log n) by mpmath.quad over the window's pieces, the archimedean integral by mpmath.quad
    ### on [0, t + 60], dps 30; and, at the first ordinate named, the conventions' check: the zero side summed over the table's
    ### ordinates, Σ_j 2 (paperFT φ_t(γ_j))², beside Q -- unscored, a check that the bench's normalisation is the identity's."""
    import mpmath as mp
    mp.mp.dps = 30
    ords = dict(ordinates())
    pcs = [(mp.mpf(int(a.p)) / int(a.q), mp.mpf(int(b.p)) / int(b.q), [mp.mpf(int(c.p)) / int(c.q) for c in q.coeffs()]) for a, b, q in PCS]

    def w(x):
        for a, b, cs in pcs:
            if a <= x <= b:
                return mp.polyval(cs[::-1], x)
        return mp.mpf(0)
    knots = [a for a, b, c in pcs] + [pcs[-1][1]]

    def wh(z):
        z = mp.mpc(z)
        f1 = 2 * K.W if z == 0 else 2 * mp.sin(z * K.W) / z
        hh = mp.mpf(K.H_NUM) / K.H_DEN
        f2 = 1 if z == 0 else 2 * mp.sin(z * hh / 2) / (z * hh)
        return f1 * f2 ** K.P

    L_ = ['### mpmath %s, dps 30: the midpoint cross-check' % mp.__version__]
    for j in [int(x) for x in js]:
        t = mp.mpf(ords[j])
        S = mp.mpf(0)
        for n, p in prime_powers(K.NMAX):
            u = mp.log(n)
            br = sorted(set([x for x in knots] + [u - x for x in knots]))
            br = [x for x in br if u - K.L_SUPPORT <= x <= K.L_SUPPORT]
            kv = mp.quad(lambda v: mp.cos(t * v) * w(v) * mp.cos(t * (u - v)) * w(u - v), br)
            S += mp.log(p) / mp.sqrt(n) * 2 * kv
        ph = (wh(mp.mpc(0, 0.5) - t) + wh(mp.mpc(0, 0.5) + t)) / 2
        pole = 2 * ph ** 2
        f = lambda r: ((wh(r - t) + wh(r + t)) / 2) ** 2 * (mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2)) - mp.log(mp.pi))
        A = mp.quad(f, mp.linspace(0, t + 60, int(t + 60) * 2 + 1)) / mp.pi
        Q = mp.re(pole) - S + mp.re(A)
        L_.append('CHECK %d t=%s Q_mpmath=%s' % (j, ords[j][:32], mp.nstr(Q, 25)))
        print(L_[-1], flush=True)
        if j == int(js[0]):
            zs = mp.mpf(0)
            for jj, g in sorted(ords.items()):
                gg = mp.mpf(g)
                zs += 2 * mp.re((wh(gg - t) + wh(gg + t)) / 2) ** 2
            L_.append('CONVENTION %d t=%s zero_side_over_the_table=%s' % (j, ords[j][:32], mp.nstr(zs, 25)))
            print(L_[-1], flush=True)
    open(out, 'wb').write((NL.join(L_) + NL).encode('utf-8'))


def inputs(capture):
    import subprocess
    import time
    raw = open(capture, 'rb').read()
    txt = raw.decode('utf-8', 'replace').replace(chr(13), '')
    # ### the table wraps each ordinate over several lines and parts them by a blank line: each block joined, whitespace removed
    nums = [b for b in (''.join(x.split()) for x in re.split(r'\n\s*\n', txt)) if re.fullmatch(r'\d+\.\d{60,}', b)]
    taken = nums[:K.N_ORD]
    me = io.open(os.path.abspath(__file__), encoding='utf-8').read()
    L_ = ['b627 -- THE BENCH`S INPUTS, BANKED BEFORE ANY COMPUTATION (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
          '### THE ZERO TABLE, READ ONCE: %s' % K.ZERO_URL,
          '###   capture %d bytes, sha256 %s ; ordinates in the read %d ; taken %d (the lowest, in the table`s order) ; each kept to 70 digits' % (
              len(raw), hashlib.sha256(raw).hexdigest(), len(nums), len(taken)),
          '###   the table`s own head: %s' % ' '.join(txt.strip().split(NL)[0].split())[:200],
          '### THE PARAMETERS (the author`s answer before the seal): W = %d, h = %d/%d, p = %d (the classK floor of WindowInClassK, '
          'PlateauRamp.lean :156-:158), L = W + p·h/2 = %s, the prime sum over n ≤ %d (log %d < 2L = 10 < log %d), the archimedean cut at '
          't + %d' % (K.W, K.H_NUM, K.H_DEN, K.P, L, K.NMAX, K.NMAX, K.NMAX + 1, K.DELTA),
          '### THE PRECISION AND THE INTERVAL METHOD: python-flint %s, Arb balls at %d bits throughout; the prime sum and the window exact '
          'in balls; the archimedean term by acb.integral with Arb`s own bound and the closed-form tail beyond the cut added to the radius; '
          'mpmath for the midpoint cross-check alone' % (__import__('flint').__version__, K.PREC),
          '### THE TEST FUNCTION: φ_t(u) = cos(t u)·window W h p (u) (b519`s convention), k_t = weilTest φ_t φ_t; Q(t) = poleTerm k_t - '
          'primeSum k_t + archTerm k_t', '', '### THE KERNEL LINES, READ AT %s, AND THEIR TRANSCRIPTION IN THE SCRIPT:' % K.KPIN]
    for f, ns in K.KERNEL_LINES:
        src = subprocess.run(['git', '-C', K.KER, 'show', '%s:%s' % (K.KPIN, f)], capture_output=True).stdout.decode('utf-8').replace(chr(13), '').split(NL)
        same = subprocess.run(['git', '-C', K.KER, 'rev-parse', '%s:%s' % (K.KPIN, f), 'v0.22:%s' % f], capture_output=True, text=True).stdout.split()
        for n in ns:
            line = '# %s %s :%d: %s' % (K.KPIN, f, n, src[n - 1])
            L_.append('  %s :%d %s ; in the script %s' % (f, n, src[n - 1].strip()[:150], line in me))
        L_.append('  (%s: the blob at %s %s the blob at v0.22)' % (f, K.KPIN, 'equals' if len(same) == 2 and same[0] == same[1] else 'DIFFERS FROM'))
    L_ += ['', '### THE ORDINATES TAKEN:'] + ['ORD %d %s' % (i, x[:72]) for i, x in enumerate(taken, 1)]
    open(INPUTS, 'wb').write((NL.join(L_) + NL).encode('utf-8'))
    print(NL.join(L_[2:7]))


def assemble(out, *parts):
    rows, checks, head = [], [], ''
    for p in parts:
        for l in io.open(p, encoding='utf-8').read().split(NL):
            if l.startswith('ROW '):
                rows.append(l)
            elif l.startswith(('CHECK ', 'CONVENTION ', '### mpmath')):
                checks.append(l)
            elif l.startswith('### prime powers'):
                head = l
    rows.sort(key=lambda l: int(l.split()[1]))
    ords = dict(ordinates())
    js = [int(l.split()[1]) for l in rows]
    vals = {int(l.split()[1]): arb(re.search(r' Q=(\S+)', l).group(1)) for l in rows}
    spacings = []
    for j in js:
        g = [abs(arb(ords[j]) - arb(ords[i])) for i in (j - 1, j + 1) if i in ords]
        spacings.append((j, min(g, key=lambda x: float(x.mid())), 'left only, the next ordinate not taken' if j + 1 not in ords else
                         ('right only' if j - 1 not in ords else 'nearer side')))
    jm = min(js, key=lambda j: float(vals[j]))
    xs = [arb(ords[j]).log() for j in js]
    ys = [vals[j].log() for j in js]
    n = len(js)
    mx, my = sum(xs, arb(0)) / n, sum(ys, arb(0)) / n
    slope = sum(((x - mx) * (y - my) for x, y in zip(xs, ys)), arb(0)) / sum(((x - mx) ** 2 for x in xs), arb(0))
    pos = sum(' positive=YES' in l for l in rows)
    strad = sum(' positive=STRADDLES' in l for l in rows)
    neg = sum(' positive=NO' in l for l in rows)
    rads = [float(arb(re.search(r' rad=(\S+)', l).group(1)).mid()) / abs(float(vals[int(l.split()[1])].mid())) for l in rows]
    import math
    digits = int(math.floor(-math.log10(max(rads))))
    L_ = ['b627 -- THE MARGIN BENCH: Q(t) FROM THE PRIME SIDE AT THE LOWEST %d ORDINATES (tools/b627_margin.py ; inputs '
          'data/b627_margin_inputs.txt)' % n,
          '### A bench of the identity`s two sides at known zeros, not a test of positivity beyond the table; no statement about any zero.',
          head, '']
    L_ += rows + ['', '### THE NEAREST-NEIGHBOUR SPACING AT EACH ORDINATE (a companion column; nothing is scored against it):']
    L_ += ['SPACING %d %s (%s)' % (j, g.mid().str(12, radius=False), why) for j, g, why in spacings]
    L_ += ['', '### THE MARGIN`S LEAST-SQUARES LOG-LOG SLOPE AGAINST HEIGHT, ONCE: %s -- A CENTRE LINE, NOT A BOUND; nothing is scored '
                'against it.' % slope.mid().str(8, radius=False), '']
    L_ += checks + ['',
                    '### ### **VALUES %d ; POSITIVE (THE WHOLE BALL ABOVE ZERO) %d ; STRADDLING %d ; NEGATIVE %d ; CERTIFIED DIGITS AT THE WORST '
                    'VALUE %d.**' % (n, pos, strad, neg, digits),
                    '### ### **THE MINIMUM OVER N : %s AT ORDINATE %d, t = %s.**' % (vals[jm].mid().str(20, radius=False), jm, ords[jm][:32])]
    open(out, 'wb').write((NL.join(L_) + NL).encode('utf-8'))
    print(NL.join(L_[-3:]))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'inputs':
        inputs(sys.argv[2])
    elif cmd == 'run':
        run(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif cmd == 'check':
        check(sys.argv[2], *sys.argv[3:])
    elif cmd == 'assemble':
        assemble(sys.argv[2], *sys.argv[3:])
    else:
        print('usage: b627_margin.py inputs <capture> | run <a> <b> <out> | check <out> <j>... | assemble <out> <part>...')
        sys.exit(2)
