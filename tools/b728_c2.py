# -*- coding: utf-8 -*-
"""b728_c2.py -- (R338)(4): THE LAST THREE C2 FIELDS ON c2-b725, EACH SPLIT BY CERTIFICATE WITHIN THE FIELD.

### WHY THE SPLIT: `cert D n0 v q = true` by one decide +kernel holds the whole evaluation in one declaration's kernel caches: D=-235 (n0 4225) left the
### runner 3942 MB, D=-267 and D=-427 stopped under the 2,560 MB hold (data/b726_c2.txt :32-:34). THE SPLIT: the same evaluation cut at checkpoints.
### A checkpoint is the literal value of the state (a Tab) after a block of sweep rows or a block of wLoop steps, printed by a Python mirror of C2Walk.lean's
### definitions; each block is one declaration in one module, `tabEq (sweepAll .. k x S_i) S_{i+1} = true` or `tabEq (wLoop .. k n W_i) W_{i+1} = true`,
### each by decide +kernel, so no block sees more than its own evaluation; the modules form a line, one process at a time. A checkpoint the mirror got wrong
### fails its block: the mirror is trusted for nothing. SIDEExplicitFormula/C2Chain.lean carries tabEq, its soundness and the chain lemmas, by term and
### rewriting, no simp and no omega; SIDEExplicitFormula/C2Field/M<|D|>.lean concludes `cert D n0 v q = true`, the statement of b726, unchanged.
### C2Walk.lean is not edited. Nothing here runs Lean; no lean process on this host.
### Routes: count (the blocks per field, printed) ; gen <|D|> <clone dir> (writes the modules into a clone of the branch) ; chain <clone dir> (writes C2Chain.lean).
### Written by the Write tool at b728; it writes those Lean files and nothing else.
"""
import math
import os
import sys

NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.setrecursionlimit(10000)

FIELDS = {267: (4761, -2, 1), 427: (14161, -2, 1), 403: (17303, -2, 1)}
REFERENCE = (-235, 4225)      # ### the largest field compiled in one declaration (data/b726_c2.txt :32): the blocks are sized against it
PARTS = 6                     # ### a block costs at most a sixth of that field's phase, in the mirror's own step counts


# ================================================================================ THE MIRROR OF C2Walk.lean
def pform(D, x, y):
    return x * x + (-D // 4) * y * y if D % 4 == 0 else x * x + x * y + ((1 - D) // 4) * y * y


def get(t, n):
    while True:
        if t is None:
            return 0
        if n == 0:
            return t[1]
        if n % 2 == 1:
            t, n = t[0], n // 2
        else:
            t, n = t[2], n // 2 - 1


def tset(k, t, n, x):
    if k == 0:
        return t
    l, v, r = t if t is not None else (None, 0, None)
    if n == 0:
        return (l, x, r)
    if n % 2 == 1:
        return (tset(k - 1, l, n // 2, x), v, r)
    return (l, v, tset(k - 1, r, n // 2 - 1, x))


def side(N):
    s = 0
    while not 2 * N < s * s:
        s += 1
    return s


def sweep_row(D, N, x, s, t):
    """one row of sweepAll; returns the table, its step cost."""
    cost, depth = 2 * s + 1, 2 * int(math.log2(N + 1))
    for y in range(-s, s + 1):
        p = pform(D, x, y)
        if 0 <= p <= N:
            t = tset(64, t, p, get(t, p) + 1)
            cost += depth
    return t, cost


def big_omega(n):
    f, p, c = 0, 2, 0
    while n >= 2:
        c += 1
        if n < p * p:
            return f + 1, c
        if n % p == 0:
            n //= p
            f += 1
        else:
            p += 1
    return f, c


def w_step(R, W, n):
    """wStep (aOf R) W n; returns the value, its step cost."""
    om, c = big_omega(n)
    s, d, cost = 0, 2, c + 30
    while d * d <= n:
        cost += 1
        if n % d == 0:
            e = n // d
            cost += 4
            if e == d:
                s += get(W, d) * (get(R, d) // 2)
            else:
                s += get(W, d) * (get(R, e) // 2) + get(W, e) * (get(R, d) // 2)
        d += 1
    return om * 360360 * (get(R, n) // 2) - s, cost


def walk(D, N):
    """the full evaluation: the row states with costs, the step states with costs."""
    s = side(N)
    t, rows = None, []
    for i in range(2 * s + 1):
        t, c = sweep_row(D, N, -s + i, s, t)
        rows.append((t, c))
    R, W, steps = t, None, []
    for n in range(2, N + 1):
        v, c = w_step(R, W, n)
        W = tset(64, W, n, v)
        steps.append((W, c, v))
    return s, rows, steps


def phase_costs(D, N):
    s, rows, steps = walk(D, N)
    return sum(c for _t, c in rows), sum(c for _t, c, _v in steps)


def blocks(costs, budget):
    """(start, count) over the list, greedily, each at most the budget unless one item alone exceeds it."""
    out, st, acc = [], 0, 0
    for i, c in enumerate(costs):
        if acc and acc + c > budget:
            out.append((st, i - st))
            st, acc = i, 0
        acc += c
    out.append((st, len(costs) - st))
    return out


# ================================================================================ THE LITERALS
def lit_int(x):
    return '(ip %d)' % x if x >= 0 else '(im %d)' % (-x - 1)


def lit(t):
    """the term of a table, iteratively kind enough for depth 64 and below."""
    if t is None:
        return 'lf'
    return '(nd %s %s %s)' % (lit(t[0]), lit_int(t[1]), lit(t[2]))


HEAD = 'import %s' + NL + NL + 'namespace C2Walk' + NL + NL + 'namespace F%d' + NL + NL + 'set_option maxRecDepth 100000' + NL + 'set_option maxHeartbeats 0' + NL + NL
TAIL = NL + 'end F%d' + NL + NL + 'end C2Walk' + NL


def mod(d, kind, i):
    return 'SIDEExplicitFormula.C2Field.P%d.%s%03d' % (d, kind, i)


def path(root, d, kind, i):
    return os.path.join(root, 'SIDEExplicitFormula', 'C2Field', 'P%d' % d, '%s%03d.lean' % (kind, i))


def put(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb') as fh:
        fh.write(s.encode('utf-8'))


def gen(d, root):
    n0, v, q = FIELDS[d]
    D = -d
    s, rows, steps = walk(D, n0)
    cs, cw = phase_costs(*REFERENCE)
    bs_, bw = blocks([c for _t, c in rows], cs / PARTS), blocks([c for _t, c, _v in steps], cw / PARTS)
    if steps[-1][2] % big_omega(n0)[0] != 0 or q * (steps[-1][2] // big_omega(n0)[0]) != v * 360360 or any(x < 0 for _t, _c, x in steps[:-1]):
        sys.exit('### THE MIRROR DOES NOT REACH THE CERTIFICATE AT D=%d -- REFUSED' % D)
    bytes_ = 0
    prev_mod, prev_name, K = 'SIDEExplicitFormula.C2Chain', None, 0
    for i, (st, ct) in enumerate(bs_, 1):
        T = rows[st + ct - 1][0]
        x = -s + st
        body = ['/-- (R338)(4), D = %d: the sweep after row %d of %d. -/' % (D, st + ct, 2 * s + 1), 'noncomputable def S%d : Tab := %s' % (i, lit(T)), '']
        start = 'Tab.leaf' if prev_name is None else prev_name
        body += ['theorem stepS%d : tabEq (sweepAll (%d) %d %d %d (%d) %s) S%d = true := by' % (i, D, n0, s, ct, x, start, i), '  decide +kernel', '']
        if prev_name is None:
            body += ['theorem reachS%d : sweepAll (%d) %d %d %d (%d) Tab.leaf = S%d := tabEq_sound _ _ stepS%d' % (i, D, n0, s, ct, -s, i, i)]
        else:
            body += ['theorem reachS%d : sweepAll (%d) %d %d %d (%d) Tab.leaf = S%d :=' % (i, D, n0, s, K + ct, -s, i),
                     '  sweep_chain reachS%d (tabEq_sound _ _ stepS%d) rfl (by decide +kernel)' % (i - 1, i)]
        txt = HEAD % (prev_mod, d) + NL.join(body) + NL + TAIL % d
        put(path(root, d, 'S', i), txt)
        bytes_ += len(txt)
        prev_mod, prev_name, K = mod(d, 'S', i), 'S%d' % i, K + ct
    last_s = len(bs_)
    final_s = 'S%d' % last_s
    prev_name, K = None, 0
    for i, (st, ct) in enumerate(bw, 1):
        T = steps[st + ct - 1][0]
        n = 2 + st
        body = ['/-- (R338)(4), D = %d: W to n = %d. -/' % (D, n + ct - 1), 'noncomputable def W%d : Tab := %s' % (i, lit(T)), '']
        start = 'Tab.leaf' if prev_name is None else prev_name
        body += ['theorem stepW%d : tabEq (wLoop (aOf %s) %d %d %s) W%d = true := by' % (i, final_s, ct, n, start, i), '  decide +kernel', '']
        if prev_name is None:
            body += ['theorem reachW%d : wLoop (aOf %s) %d 2 Tab.leaf = W%d := tabEq_sound _ _ stepW%d' % (i, final_s, ct, i, i)]
        else:
            body += ['theorem reachW%d : wLoop (aOf %s) %d 2 Tab.leaf = W%d :=' % (i, final_s, K + ct, i),
                     '  wLoop_chain reachW%d (tabEq_sound _ _ stepW%d) rfl rfl' % (i - 1, i)]
        txt = HEAD % (prev_mod, d) + NL.join(body) + NL + TAIL % d
        put(path(root, d, 'W', i), txt)
        bytes_ += len(txt)
        prev_mod, prev_name, K = mod(d, 'W', i), 'W%d' % i, K + ct
    fin = ['/- b728, (R338)(4): the certificate at D = %d, split within the field, %d sweep blocks and %d step blocks, one module each. -/' % (D, len(bs_), len(bw)),
           'import %s' % prev_mod, '', 'namespace C2Walk', '', 'set_option maxHeartbeats 5000000 in', 'theorem cert_m%d : cert (%d) %d (%d) %d = true := by' % (d, D, n0, v, q),
           '  (exact cert_of_tabs (rTab_of (s := %d) (by decide +kernel) F%d.reachS%d) F%d.reachW%d (by decide +kernel); trace "CERT D=%d KERNEL")' % (s, d, last_s, d, len(bw), D),
           '', 'end C2Walk', '']
    put(os.path.join(root, 'SIDEExplicitFormula', 'C2Field', 'M%d.lean' % d), NL.join(fin))
    print('D=%d: s %d ; sweep blocks %d ; step blocks %d ; %d bytes ; the mirror reaches the certificate' % (D, s, len(bs_), len(bw), bytes_))


def count():
    cs, cw = phase_costs(*REFERENCE)
    print('the reference D=%d n0 %d: sweep cost %d, step cost %d ; a block at most a %dth of each' % (REFERENCE[0], REFERENCE[1], cs, cw, PARTS))
    for d in (267, 427, 403):
        n0 = FIELDS[d][0]
        s, rows, steps = walk(-d, n0)
        bs_, bw = blocks([c for _t, c in rows], cs / PARTS), blocks([c for _t, c, _v in steps], cw / PARTS)
        print('D=-%d n0 %d: side %d ; sweep cost %d in %d blocks ; step cost %d in %d blocks ; W(n0) %d ; table entries %d' % (
            d, n0, s, sum(c for _t, c in rows), len(bs_), sum(c for _t, c, _v in steps), len(bw), steps[-1][2], len(lit(steps[-1][0]))), flush=True)


CHAIN = r'''/-
b728, (R338)(4): THE CHAIN OF A CERTIFICATE SPLIT WITHIN ITS FIELD. Vanilla Lean 4, no Mathlib, no native_decide; by term and rewriting.

  * tabEq and its soundness: a table's value is checked against a literal by decide +kernel in one declaration.
  * sweepAll_add, wLoop_add: a loop of k1 + k2 steps is k1 steps then k2; sweep_chain, wLoop_chain: the same as a step of a module line.
  * rTab_of, cert_of_tabs: the literal tables conclude `cert D n0 v q = true`, C2Walk.lean's own statement, unedited.
-/
import SIDEExplicitFormula.C2Walk

namespace C2Walk

/-- the short names of the literal tables -/
def nd : Tab → Int → Tab → Tab := Tab.node
def lf : Tab := Tab.leaf
def ip (n : Nat) : Int := Int.ofNat n
def im (n : Nat) : Int := Int.negSucc n

def tabEq : Tab → Tab → Bool
  | Tab.leaf, Tab.leaf => true
  | Tab.node l x r, Tab.node l' x' r' => decide (x = x') && (tabEq l l' && tabEq r r')
  | Tab.leaf, Tab.node _ _ _ => false
  | Tab.node _ _ _, Tab.leaf => false

theorem false_elim' {P : Prop} (h : false = true) : P := nomatch h

theorem and_left' : ∀ (a b : Bool), (a && b) = true → a = true
  | true, _, _ => rfl
  | false, _, h => false_elim' h

theorem and_right' : ∀ (a b : Bool), (a && b) = true → b = true
  | true, _, h => h
  | false, _, h => false_elim' h

theorem tabEq_sound : ∀ (s t : Tab), tabEq s t = true → s = t
  | Tab.leaf, Tab.leaf, _ => rfl
  | Tab.leaf, Tab.node _ _ _, h => false_elim' h
  | Tab.node _ _ _, Tab.leaf, h => false_elim' h
  | Tab.node l x r, Tab.node l' x' r', h => by
    have h0 : (decide (x = x') && (tabEq l l' && tabEq r r')) = true := h
    have hx : x = x' := of_decide_eq_true (and_left' _ _ h0)
    have hl : l = l' := tabEq_sound l l' (and_left' _ _ (and_right' _ _ h0))
    have hr : r = r' := tabEq_sound r r' (and_right' _ _ (and_right' _ _ h0))
    rw [hx, hl, hr]

/-- x after k rows -/
def shift : Nat → Int → Int
  | 0, x => x
  | k + 1, x => shift k (x + 1)

theorem sweepAll_succ (D : Int) (N s k : Nat) (x : Int) (t : Tab) :
    sweepAll D N s (k + 1) x t = sweepAll D N s k (x + 1) (sweepRow D N x (2 * s + 1) (-(s : Int)) t) := by
  first
    | (rw [sweepAll]; cases sweepRow D N x (2 * s + 1) (-(s : Int)) t <;> rfl)
    | (unfold sweepAll; cases sweepRow D N x (2 * s + 1) (-(s : Int)) t <;> rfl)
    | (simp only [sweepAll]; split <;> rfl)

theorem sweepAll_add (D : Int) (N s k2 : Nat) : ∀ (k1 : Nat) (x : Int) (t : Tab),
    sweepAll D N s (k1 + k2) x t = sweepAll D N s k2 (shift k1 x) (sweepAll D N s k1 x t) := by
  intro k1
  induction k1 with
  | zero =>
    intro x t
    show sweepAll D N s (0 + k2) x t = sweepAll D N s k2 x t
    rw [Nat.zero_add]
  | succ k ih =>
    intro x t
    have h : k + 1 + k2 = (k + k2) + 1 := Nat.succ_add k k2
    rw [h, sweepAll_succ, sweepAll_succ]
    exact ih (x + 1) _

theorem sweep_chain {D : Int} {N s K k K' : Nat} {x0 x : Int} {t0 t t' : Tab}
    (h0 : sweepAll D N s K x0 t0 = t) (h1 : sweepAll D N s k x t = t') (hK : K + k = K') (hx : shift K x0 = x) :
    sweepAll D N s K' x0 t0 = t' := by
  subst hK
  subst hx
  rw [sweepAll_add, h0]
  exact h1

theorem wLoop_succ (a : Nat → Int) (k n : Nat) (W : Tab) :
    wLoop a (k + 1) n W = wLoop a k (n + 1) (Tab.set 64 W n (wStep a W n)) := by
  first
    | (rw [wLoop]; cases Tab.set 64 W n (wStep a W n) <;> rfl)
    | (unfold wLoop; cases Tab.set 64 W n (wStep a W n) <;> rfl)
    | (simp only [wLoop]; split <;> rfl)

theorem wLoop_add (a : Nat → Int) (k2 : Nat) : ∀ (k1 n : Nat) (W : Tab),
    wLoop a (k1 + k2) n W = wLoop a k2 (n + k1) (wLoop a k1 n W) := by
  intro k1
  induction k1 with
  | zero =>
    intro n W
    show wLoop a (0 + k2) n W = wLoop a k2 n W
    rw [Nat.zero_add]
  | succ k ih =>
    intro n W
    have h : k + 1 + k2 = (k + k2) + 1 := Nat.succ_add k k2
    have h2 : n + 1 + k = n + (k + 1) := by
      first
        | exact Nat.add_right_comm n 1 k
        | omega
    rw [h, wLoop_succ, wLoop_succ, ← h2]
    exact ih (n + 1) _

theorem wLoop_chain {a : Nat → Int} {n0 K k K' n : Nat} {W0 W W' : Tab}
    (h0 : wLoop a K n0 W0 = W) (h1 : wLoop a k n W = W') (hK : K + k = K') (hn : n0 + K = n) :
    wLoop a K' n0 W0 = W' := by
  subst hK
  subst hn
  rw [wLoop_add, h0]
  exact h1

theorem rTab_of {D : Int} {N s : Nat} {R : Tab} (hs : side N = s)
    (hw : sweepAll D N s (2 * s + 1) (-(s : Int)) Tab.leaf = R) : rTab D N = R := by
  subst hs
  exact hw

theorem cert_of_tabs {D : Int} {n0 : Nat} {v : Int} {q : Nat} {R T : Tab}
    (hr : rTab D n0 = R) (hw : wLoop (aOf R) (n0 - 1) 2 Tab.leaf = T)
    (hf : (Tab.get T n0 % (bigOmega n0 : Int) == 0 &&
      (q : Int) * (Tab.get T n0 / (bigOmega n0 : Int)) == v * 360360 &&
      allNonneg T (n0 - 2) 2) = true) : cert D n0 v q = true := by
  subst hr
  subst hw
  exact hf

end C2Walk
'''


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('count', 'gen', 'chain'):
        sys.exit('usage: b728_c2.py count | gen <|D|> <clone dir> | chain <clone dir>')
    if sys.argv[1] == 'count':
        count()
    elif sys.argv[1] == 'chain':
        put(os.path.join(sys.argv[2], 'SIDEExplicitFormula', 'C2Chain.lean'), CHAIN)
        print('written C2Chain.lean')
    else:
        gen(int(sys.argv[2]), sys.argv[3])
