# W-ATTEMPT-1 — SITTING 19: THE SANDWICHED TRACE — **HS BY CONSTRUCTION; MY GRID CANNOT RESOLVE IT**

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · diagnostic COMPLETE before characterization**
**Nothing deposits.**

---

## §1 — SITTING 18's FINDING, RE-GRADED AS THE FERRY DIRECTS

**The object was wrong, not the arithmetic.** *`Tr(ϑ(f)PP̂P)` in the bare diagonal order is not trace-class;
cyclicity needs a trace-class factor.* ### **The finite object is the SANDWICHED form
`L(f) = Tr(ϑ(g)PP̂Pϑ(g)*) = ‖P̂Pϑ(g)*‖²_HS` — manifestly ≥ 0, because it is a norm.**

> ### **SITTING 18's `ln X` DIVERGENCE IS THEREFORE EXPECTED, NOT ANOMALOUS — the PV structure of the
> un-sandwiched order. Its fingerprint (`0.974 / 0.615` against `1.4427 / 0.9102`) is filed as that
> structure's signature and is no longer an open discrepancy.** *One blockage retired.*

---

## §2 — ### **THE HS DIAGNOSTIC: PASSES AT SMALL `X`, FAILS BEYOND — AND THE CAUSE IS MINE**

| `a` | `X` | `N = 400` | `N = 600` | rel-spread |
|:--|:--|:--|:--|:--|
| `√2` | `4` | `+2.063330` | `+2.061686` | ### **`8.0×10⁻⁴`** |
| `√2` | `6` | `+1.917903e+01` | `+7.608075e+00` | ### **`1.5`** |
| `√2` | `8` | `+3.037411e+03` | `+1.293546e+03` | ### **`1.35`** |
| `√3` | `4` | `+1.260634` | `+1.259740` | ### **`7.1×10⁻⁴`** |
| `√3` | `6` | `+1.146049e+01` | `+4.555797e+00` | `1.5` |
| `√3` | `8` | `+1.830173e+03` | `+7.787660e+02` | `1.35` |

> ### **AT `X = 4` THE INTEGRAL IS STABLE TO `10⁻⁴`. BEYOND IT, `N`-REFINEMENT CHANGES THE ANSWER BY A
> FACTOR OF TWO — THAT IS NOT A DIVERGENT INTEGRAL, IT IS AN UNRESOLVED ONE.**

### **THE CAUSE, IDENTIFIED**

*In log coordinates the sinc kernel carries `sin(2π(e^s − e^u))` — **oscillation frequency growing like
`e^s`** — against a uniform `s`-grid.* ### **At `X = 4` the multiplicative variable already reaches `e⁴ ≈ 55`,
where `N = 600` gives spacing `≈ 0.37` in `x` against a sinc period of `1`. THE GRID IS UNDER-RESOLVED
EXACTLY WHERE THE VALUES DIVERGE.**

> ### **SO `X = 4`'s STABILITY IS NOT CONVERGENCE IN `X` — IT IS THE LARGEST WINDOW MY GRID STILL RESOLVES.
> I DECLINE TO REPORT `2.0617` AND `1.2597` AS VALUES OF `L`.** *They are the correct integral over a
> truncation that has not been shown large enough, computed on a grid that fails just past it.*

**THE NAMED FIX:** ### **discretize in the MULTIPLICATIVE variable `x` with spacing set by the sinc period
(`Δx ≪ 1`), not in `log x`. The log grid is natural for the scaling action and wrong for this kernel; the two
want different meshes and the build must carry both.**

---

## §3 — DOWNSTREAM

**Gate: NOT RUN** *(no converged `L`)* · **floor by subtraction: NOT RUN** · **cross-route floor: NOT RUN** ·
### **THE LEDGER: NOT RUN — seventh consecutive sitting.**

**Positivity sanity rail: trivially satisfied** — every value is a squared norm and every computed value is
positive. ### **As the ferry said, this is a rail and not the gate.**

---

## §4 — CHECKPOINT-5, UPDATED

* ### **RETIRED:** sitting 18's `ln X` mismatch — explained as the un-sandwiched order's PV structure, at the ferry's cite.
* ### **NEW BLOCKAGE NAME:** ***the two-mesh problem*** *— the scaling action wants a log grid, the sinc kernel wants a linear one, and my build has only the first.* **Not a mathematical obstruction; an instrument one, with a named fix.**
* **Corrections table: no prior conclusion overturned this sitting.**

---

## CLOSING

**Returning for the author's word:**
1. ### **THE SANDWICHED OBJECT IS RIGHT AND IS HS BY CONSTRUCTION — sitting 18's divergence is retired as expected structure, not a defect.**
2. ### **THE HS DIAGNOSTIC PASSES AT `X = 4` (`10⁻⁴`) AND FAILS AT `X ≥ 6` (factor-2 under `N`-refinement).**
3. ### **CAUSE IDENTIFIED AS MY DISCRETIZATION, NOT THE MATHEMATICS: sinc oscillation at frequency `e^s` on a uniform log grid.**
4. ### **I DECLINE TO BANK THE `X = 4` NUMBERS AS `L`.** *Stability inside the resolved region is not convergence in truncation, and reporting them would repeat sitting 16's error in a new coordinate.*
5. **The ledger is unrun for a seventh sitting. `h2` is exactly where it was.**

**`h2` UNCHANGED. NO SIGN. NOTHING DEPOSITS.**
