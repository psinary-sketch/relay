# b168 — THE LEFT-ENDPOINT REPAIR

**Registration `9ac1f2b`, banked after the owner reads and before any computation.**
2026-08-25. Ferry part 1 of 1, receipt confirmed in full before execution.

> ### **ALL THREE GATES PASS. `Δ` IS BANKED. THE ONE-SIGN VERDICT IS DECIDED ACROSS THE
> FAMILY: IT HOLDS EXACTLY FOR `μ > 0.48370`, AND THE ADMISSIBLE SET IS A HALF-LINE.**
> *Core `288 → 292/292`, correspondence row 75, 75 of 75 rows parsing at six cells.*

---

## THE HEADLINE — **THE ROUTINE WAS NEVER AT FAULT**

b38's `per_mode_eps_grids`, read at content, takes its own empty-range branch at `ρ = 1`:

```
lo, hi = 1.0 / r, 1.0
if hi - lo <= 0:
    continue
```

and leaves the entry at **zero** — which *is* b115 (2g)'s derived `e_n(0) = 0`.
### **THE DERIVED ANSWER WAS ALREADY IMPLEMENTED IN THE INSTRUMENT AND NOBODY HAD EVER ASKED
IT.** b167's defect was in the **grid handed to it**, whose first node is `exp(1e-4)`, and in
`np.interp` clamping below that node.

---

## COMPONENT 1 — THE REPAIR AND ITS GATES

**The route taken, fixed at registration before it was built:** ### **prepend `ρ = 1.0`, take
its value FROM THE ROUTINE, leave every incumbent node in place.** So `np.interp` at any
`ρ ≥ exp(1e-4)` uses the same neighbours and returns the same number — ### **the
incumbent-preservation law is satisfied by construction, not by luck.**

**The route not taken, recorded:** rebuilding as `linspace(0, ln(ρ_max), n)` also reaches
`ρ = 1` but **redistributes every node**, shifting every interpolated value in the record.

### **`e_n(0)` was NOT set to zero by hand** — b167 named that in advance as the thing a repair
must not do. And ### **`b134_wroute.py` was not modified**: its `E` is *injected* through
`psi_W`'s own parameter, so a prior act's instrument stays reproducible exactly as that act ran
it.

```
--- G-L  THE REPAIRED GRID EVALUATES AT rho = 1, NO CLAMP, NO EXTRAPOLATION ---
  incumbent first node : 1.0001000050   ### the defect
  repaired  first node : 1.0000000000
  sum_n e_n at the repaired first node : 0
  ### the value came FROM THE ROUTINE's own empty-range branch, not by hand.
  node is exactly 1.0 : True ; sum is exactly 0.0 : True
### G-L : PASS

--- G-K  Delta(0) = 10, THE DERIVED KNOWN ANSWER (the gate that fired at b167) ---
  incumbent Delta(0) = 9.997700582621   |dev| = 2.299e-03   ### b167's failure, reproduced
  repaired  Delta(0) = 10.000000000001   |dev| = 9.877e-13   tol 1e-9
### G-K : PASS

--- G-R  THE INCUMBENT REPRODUCES (to printed digits), AND EVERY MOVEMENT IS SHOWN ---
object                                 repaired     banked/incumbent       movement
Psi_W(0) vs banked              -1.165002987410         -1.165002987     -4.101e-10
Psi_W(0) rep vs incumbent       -1.165002987410      -1.165002987396     -1.422e-11
sum_n A_n(UMAX)              1.443987342550e-01      1.443987343e-01     -4.498e-11

  b134's I_W column:
     a^2         I_W repaired           I_W banked      vs banked   vs incumbent
       2      -0.141878140014         -0.141878140     -1.441e-11     -1.343e-13
       3      -0.101477079811         -0.101477080      1.886e-10     -8.485e-14
       4      -0.094958249834         -0.094958250      1.663e-10     -6.720e-14
       8      -0.096080945837         -0.096080946      1.630e-10     -4.494e-14
       9      -0.096586799482         -0.096586799     -4.824e-10     -4.247e-14
      12      -0.097074298101         -0.097074298     -1.014e-10     -3.761e-14
      16      -0.096237114469         -0.096237114     -4.694e-10     -3.360e-14
      24      -0.092834734594         -0.092834735      4.059e-10     -2.939e-14
      48      -0.082552767163         -0.082552767     -1.629e-10     -2.408e-14

  worst |I_W repaired - banked|    = 4.824e-10   (b167's incumbent run: 4.824e-10)
  ### worst |repaired - incumbent| = 1.343e-13   ### THE REPAIR'S OWN FOOTPRINT

  ### THE PREDICTED MOVEMENT (registered before the run, e2):
      Psi_W(0) moves by phi_e(0), the cancellation residue b115 banked at -1.42e-11
      and b167 reproduced at -1.422267621e-11.
      ### MEASURED movement of Psi_W(0), repaired - incumbent = -1.422262307926e-11

### G-R : PASS   ### criterion: reproduction TO PRINTED DIGITS
### ALL THREE GATES PASS. THE MEASUREMENT IS LICENSED, AND NOT BEFORE.
```

> ### **THE PREDICTED MOVEMENT, REGISTERED BEFORE THE RUN, LANDED ON THE NUMBER RATHER THAN THE
> DIRECTION.** (e2) said `Ψ_W(0)` would move by `φ_e(0)` — the cancellation residue b115 banked
> at `−1.42e-11` and b167 reproduced at `−1.422267621e-11`.
> ### **MEASURED: `−1.422262307926e-11`.**
> ### **THE REPAIR'S ONLY FOOTPRINT ON THE RECORD IS EXACTLY THE RESIDUE THAT HID THE DEFECT.**
> *Four orders below that value's printed precision — so G-R passes on the ferry's own
> criterion — and* ### **reported rather than hidden, because a repair must not improve
> anything silently.**

---

## COMPONENT 2 — Δ, ITS FLOOR, AND THE FAMILY

### Δ ON THE LICENSED RANGE — bench grade

```
         u            sum_n A_n            sum_n e_n                Delta
   0.00000         10.000000000          0.000000000         10.000000000
   0.09702          4.697196819          1.837666040          2.859530779
   0.25226          2.218815249          2.277481837         -0.058666588
   0.50452          1.222883878          0.562085144          0.660798734
   0.99934          0.701841186          0.266629279          0.435211907
   1.50386          0.495958744          0.109732635          0.386226108
   1.99868          0.375009827          0.050409393          0.324600434
   2.50320          0.287975315          0.023121120          0.264854195
   2.99801          0.223909073          0.010992109          0.212916964
   3.50253          0.173711511          0.005207257          0.168504253
   3.87122          0.144398734          0.002987733          0.141411001

  Delta(0) = 10.000000000 ; Delta(umax) = 0.141411001 ; gross change = -9.858588999
  max|Delta| = 10.000000000 ; min Delta = -0.068056008 ; sign changes = 2
```

### **`Δ` is not a small perturbation of anything:** it falls by an order within a tenth of the
range and dips negative near `u = 0.25`.

### Δ'S FLOOR, EVERY AXIS, WITH ITS AXIS NAMED

```
     u-grid 200 vs 400      : 4.671449e-02
     u-grid 800 vs 400      : 1.557044e-04
     n_rho 400 vs 800       : 6.592388e-05
     n_rho 1600 vs 800      : 2.578172e-05
     NGQ 240 vs 160         : 1.314504e-12
     NGQ 80 vs 160          : 1.117328e-12
     NLEG 400 vs 300        : 6.994405e-15
     NLEG 200 vs 300        : 6.328271e-15
     NQ 600 vs 700          : 0.000000e+00
     NQ 800 vs 700          : 0.000000e+00
     NQ 900 vs 700          : 0.000000e+00

  ### DELTA'S FLOOR = MAX OVER ALL AXES = 4.671449e-02
  ### ITS AXIS = u-grid 200 vs 400
  Psi_W's floor for comparison = 8.195851e-10, axis NQ via sigma_even (b134 G-D)
  ### DELTA'S NQ AXIS MEASURES 0.000e+00   ### Delta contains no sigma_even
```

### **(e4) SPLITS, AND IS REPORTED SPLIT RATHER THAN AS A PARTIAL WIN.**

- ### **The axis half lands, on precisely the reasoning given:** `Δ` contains no `σ_even`, and
  the NQ axis measures ### **exactly `0.000000e+00` at all three variations** — not "small",
  zero.
- ### **The magnitude half misses by seven orders:** `4.671e-02` against `Ψ_W`'s `8.196e-10`,
  and the prediction said *lower*.

> ### **THE LESSON, WORTH MORE THAN THE PREDICTION WAS: REMOVING THE AXIS THAT DOMINATED ONE
> OBJECT'S FLOOR DOES NOT LOWER ANOTHER OBJECT'S FLOOR, BECAUSE THE NEW OBJECT HAS ITS OWN
> STRUCTURE.** *`Δ` plunges from 10 to 2.86 within a tenth of the range; `Ψ` does not. The u
> grid that resolves `Ψ` cannot resolve `Δ`, and that has nothing to do with which axis carried
> `Ψ`'s floor.* ### **The executor reasoned about what he was removing and not about what was
> left** — the same species b119 scored against him: *an amplitude argument is not a pairing
> argument.*

### THE FLOOR ON THE QUANTITY THE VERDICT ACTUALLY DEPENDS ON

*`Δ`'s pointwise floor is not the verdict's floor. The verdict depends on
`J(L) = ⟨Φ_K, Δ(L·)⟩` and on the subrange endpoint. Measured over nine configurations:*

```
  u-grid  200  n_rho   400 :  mu_lo = 0.483689186   J in [0.235526556, 1.071967034]
  u-grid  200  n_rho   800 :  mu_lo = 0.483686706   J in [0.235528304, 1.071949687]
  u-grid  200  n_rho  1600 :  mu_lo = 0.483683172   J in [0.235528643, 1.071927194]
  u-grid  400  n_rho   400 :  mu_lo = 0.483699369   J in [0.234603382, 1.068350062]
  u-grid  400  n_rho   800 :  mu_lo = 0.483698412   J in [0.234599094, 1.068344313]
  u-grid  400  n_rho  1600 :  mu_lo = 0.483697891   J in [0.234599677, 1.068340588]
  u-grid  800  n_rho   400 :  mu_lo = 0.483740728   J in [0.234427441, 1.067691455]
  u-grid  800  n_rho   800 :  mu_lo = 0.483702028   J in [0.234376090, 1.067451279]
  u-grid  800  n_rho  1600 :  mu_lo = 0.483701148   J in [0.234374057, 1.067446048]

  reference (u-grid 400, n_rho 800) : mu_lo = 0.483698412
  ### SPREAD OF THE ENDPOINT OVER ALL NINE CONFIGURATIONS = 5.755675e-05
  ### range: [0.483683172, 0.483740728]
  worst |mu_lo - reference| = 4.231586e-05

  ### AND THE VERDICT'S TWO STANDING FACTS AGAINST THAT SPREAD:
     b38's member 0.616500299 sits 0.132802 above the endpoint
     the free end 0.000000000 sits 0.483698 below it
  ### BOTH DISTANCES EXCEED THE SPREAD BY ORDERS, so the VERDICT is robust
  ### to the floor even where the ENDPOINT's later digits are not.
```

### **Endpoint spread `5.755675e-05` — four orders below `Δ`'s own floor**, because the `Φ_K`
pairing integrates the plunge that the pointwise floor is made of.
### **A FLOOR QUOTED ON THE WRONG QUANTITY IS NOT THE FLOOR THAT GOVERNS THE VERDICT.** Both
are reported, with their axes, and neither is dropped.

### THE VERDICT — **HOLDS ON A NAMED SUBRANGE**

```
     a^2              L           I_sigma(L)                 J(L)
       2       0.346574      -0.141878140014       1.068344313137
       3       0.549306      -0.101477079811       0.677840421280
       4       0.693147      -0.094958249834       0.540571529946
       8       1.039721      -0.096080945837       0.371318540385
       9       1.098612      -0.096586799482       0.353989310753
      12       1.242453      -0.097074298101       0.319441864457
      16       1.386294      -0.096237114469       0.293121139854
      24       1.589027      -0.092834734594       0.265584214351
      48       1.935601      -0.082552767163       0.234599094014

  sweep: max I_sigma = -0.082552767 ; J in [+0.234599094, +1.068344313] ; J sign changes = 0

  ### d = sigma_even - mu admissible for I_mu(L) < 0 at EVERY swept L:
      d in (-inf, 0.132801886)
  ### THEREFORE THE ONE-SIGN PROPERTY HOLDS EXACTLY FOR
      ### mu in (0.483698412, +inf)
      binding L at the lower end = 0.346574  (a^2 = 2.0000)

  b38's member mu = 0.616500299  : INSIDE = True
  the free end   mu = 0        : INSIDE = False
  mu = 1                       : INSIDE = True
  the illustrative bracket [0,1] wholly inside = False

  margins at named members (max I_mu over the sweep; Delta's floor 4.671e-02):
     b38's member     max I_mu = -0.082552767   strictly negative: True
     mu = 0           max I_mu = +0.516756448   strictly negative: False
     mu = 1           max I_mu = -0.172521450   strictly negative: True
     mu = 0.5         max I_mu = -0.017165264   strictly negative: True
```

> ### **THE ONE-SIGN PROPERTY HOLDS EXACTLY FOR `μ > 0.483698412`** *(spread `5.8e-05`)*,
> ### **and the admissible set is a HALF-LINE rather than an interval — because `J` keeps ONE
> SIGN across the sweep**, so the constraint binds from one side only. The binding cell is
> `a² = 2`, the smallest.
>
> **b38's member, `μ = ½` and `μ = 1` lie inside. ### The family's free end `μ = 0` lies
> OUTSIDE**, with `max I_μ = +0.516756448`. **The illustrative bracket `[0,1]` is not wholly
> inside.**

> ### **THE GUARD, AT FULL PROMINENCE, BECAUSE THIS IS THE MOST OVER-READABLE RESULT THE LANE
> HAS PRODUCED. THAT THE PROPERTY FAILS AT `μ = 0` IS NOT EVIDENCE AGAINST `μ = 0`.**
> *The inference “this member breaks the lane, so this member is wrong” requires a premise*
> ### **nobody has — that the lane's monotonicity is a REQUIREMENT. It never was:** b115, b116
> and b117 were finding out **whether** it holds, not assuming it must. A member outside the
> subrange simply leaves the balanced window's uniqueness **underived** — nothing is
> contradicted.
> ### **AND THE SYMMETRIC WARNING: that b38's member lies inside is not evidence FOR it
> either.** ### **THE SUBRANGE IS A FACT ABOUT THE FAMILY AND NEVER AN ARGUMENT FOR A MEMBER.**
> ### **NOTICED IS NOT EARNED.**

**Conditionality, carried verbatim and not softened:** every `I` value is an enclosure
*"rigorous over the quadrature and conditional on the samples"*; the prolate error bound remains
the named blocker to any higher grade; ### **601 sweep points sample the range, they do not
certify a continuum.** Nothing here is certified-numerics and nothing here is called it.

**The post-derivation check:** the shift law needs `dμ = 0.004411214` to erase the `a²=12`
deviation; b155 banks `0.004435`. ### **Residual `2.379e-05`, and its source is stated** — b155
computed from b109's *rounded* `−0.0073`. Neither is wrong at its own input, and ### **this
check is independent of `Δ`.**

**Dominance: ### not evaluated and not approached.** The ferry declines a second asking, which
### **answers b167's routed question in the direction of NOT SPENDING**, and the executor
records that the author has now answered it.

---

## COMPONENT 3 — THE FILINGS

The brief's addendum gains its **measured** section; the register's route-A row now carries the
subrange; and ### **the left-endpoint defect is filed at the loom with its species and its
scope**:

| | |
|:--|:--|
| ### **PROTECTED** | b115's `Ψ` and collapse, b116's orientation, b117's enclosure, b119's split, b121's excursion, b134's repaired re-runs — ### **and G-R MEASURED that protection rather than assuming it** |
| ### **BLOCKED** | any **raw-sum** object over the ε modes; `Δ` was the first ever asked for, and ### **any future one would have hit the same wall** |

### **THE SPECIES: A CANCELLATION THAT PROTECTS ONE OBJECT IS NOT A PROPERTY OF THE INSTRUMENT.**

**Core:** `FamilySignShadow`, four terminals, zero axioms, **first build**. Witnesses
polarity-verified before any Lean was written — 6 positive, 6 negative, including a `d` just
past the threshold (`0.133` breaks it) and one just inside (`0.132` does not). The binding cell
is decided by **cross-multiplication**, so no division and no rounding enters.
### **The inputs are BENCH values carrying their instrument's grade; deciding them in Core does
not upgrade them.**

---

## THE SEATS, SCORED

**NAVIGATOR: P1, P2 and P3 all land** — branch (a) on the repair, `Δ` banked, and the three-way
rubric resolving to *holds on a named subrange*.

**EXECUTOR: four land, one splits, and one clause of a landing was too strong.**

- **(e1)** G-L by direct evaluation — **lands**.
- **(e2)** G-R to printed digits but not exactly, movement named in advance at `~1.42e-11` and
  identified as `φ_e(0)` — ### **lands, measured `−1.422262307926e-11`.** ### **The sharpest
  registered call this seat has made, and it came from another act's banked number rather than
  from intuition.** ### **One clause was too strong and is corrected rather than re-worded:**
  I wrote that every other banked object would move by *"exactly nothing"*; the `I_W` column
  moved by up to `1.343e-13`. That is round-off in the pairing, not the ε repair — ### **but
  "exactly nothing" is not what was measured.**
- **(e3)** `Δ(0) = 10` to about `5e-10` — **lands, and conservatively**: measured `9.877e-13`.
- **(e4)** ### **splits** — axis half exact, magnitude half wrong by seven orders.
- **(e5)** *holds on a named subrange*, containing b38's member — **lands**. ### **And the
  decline to predict whether `μ = 0` lies inside was the right call: it does not**, and a guess
  either way would have been decoration.
- **(e6)** something enters Core — **lands**, four terminals.

---

## THE THIRTY-FIFTH SEAM'S DEBT

### **DISCHARGED THIS ACT: the ε grid's left endpoint, and `Δ` on the licensed range.**

**Still standing:** whatever the next arc lands; the rulings if any come — item 1's, route B's,
and the methodology day's; b157's six findings; the three front-door items, drafted at b166 and
still the author's to apply; ### **the Q-route `Ψ` instability, still UNLOCATED and untouched by
this act**; ### **and the dominance second asking, not spent**; and the deep items reserved for
a session with breadth.

---

## THE AUDITS — EMITTED, NOT TYPED

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b168
  run at    : 2026-08-25T18:41:09 (local)
  input     : whole file b168_registration_2026-08-25.txt (created this act)
  input     : whole file b168_left_endpoint.txt (created this act)
  stems     : gap, blind
  files     : 2
  lines     : 357
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 b641d55437aeba63a1bf6cebb0f73012
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b168-docs
  run at    : 2026-08-25T18:41:09 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 1
  lines     : 74
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 92ae2e9c25027c40e656af2112df0bfb
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b168
  run at    : 2026-08-25T18:43:36 (local)
  input     : mirror-refresh-2026-08-25.zip
  files     : 33
  rows      : 33
  mismatch  : 0
  declared  : b1b1f95
  ls-remote : b1b1f95f0c8f
  VERDICT   : CLEAN ON BOTH CLAUSES
  self-hash : sha256/32 718f79d2b60944d248e44697ecb2bbdb
=== END AUDIT SIDECAR ===
```

*The relay self-description check was run at the commit and is not embedded: its subject is the
commit that would contain it, so embedding it cannot reach a fixed point. It appears in the
verifier as **UNUSED**, which is run-but-not-quoted and not a failure.*

---

## PINS AT CLOSE — by `ls-remote`, never from recall

| repository | pin |
|:--|:--|
| `PLACE-papers` `main` | `b1b1f95f0c8f6a51b241412be6dd9df4c6401d9f` — the measured addendum and the defect filing |
| `SIDE-global-section` `main` | `d705a9fb22b66f1940e1159508f02dc2c2d047e1` — ### **Core 292/292, row 75** |
| `relay` `main` | *the pin line below, read back after the push* |
| mirror | `mirror-refresh-2026-08-25.zip` — **33 files**, rebuilt at `b1b1f95`, **CLEAN ON BOTH CLAUSES** |
| HELD | `held/carrier-acts` = `6eada6a` — **LOCAL-ONLY, unpushed** |

**Load this export:** `mirror-refresh-2026-08-25.zip`.

*STOP — the ferry's end.*
