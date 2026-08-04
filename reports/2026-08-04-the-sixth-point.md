# THE SIXTH POINT — K = 256, the discriminator (author-called) — 2026-08-04

Staged/banked/resumable; the validated engine; uniform-object discipline (all six points
from ONE object at the K = 256 sizing — no mixed comparison possible). Pins at open:
PLACE-papers = `4a9b2f0`; relay = `b54c44c`; lv `14720d9`, kernel `44895f9` — unmoved; rail
at the post-rename baseline. Nothing deposits.

## THE STANDING ADJUDICATOR, RESTATED VERBATIM BEFORE ANY NUMBER

*"(d) A/logK predicts c(256) = 0.942744, implied limit 1.3044; (a) geometric predicts
c(256) = 0.960941, implied limit 0.9927; separation 0.0182 ≈ 3× the demonstrated error
scale."*

**The adjudication rule, fixed now:** the measured c(256) is compared to both; **the nearer
family wins the law, and its implied limit becomes the currency's status** — with the honest
clause: **if c(256) lands between the predictions such that neither is nearer by more than
the demonstrated error scale (~0.006), the verdict is UNDISCRIMINATED and the seventh point
re-prices** — no forcing, no post-hoc family invention.

**The three outcomes, mapped in advance (the completion protocol binds as filed, relay
`7e85834`):** law-(d)-wins → the denominator is wrong, π₀ re-normalizes, the saturation
reading stays unused · law-(a)-wins → the unit constant stands at six-point instrument grade
and the saturation test opens · UNDISCRIMINATED → the seventh point prices. No
interpretation beyond the mapping; the saturation reading, the joint-reading license, and
the keystone cargo stay HELD.

## THE SIZING

K = 256 → dps ≈ 2,700 (the precision law); J = 1,200 atoms, both objects; the banked
detached worker for Stage A; the checkpointed blocked factorizations for Stage B; the
dps-60 read for Stage C under the uniform-object check (the Stage-C precedent governs: the
check PASSES before any number is read, or the run halts and files); Stage D per the rule
above.

## PRE-REGISTERED FREE RIDER — THE CONTROL'S CONVERGENCE LAW (filed mid-Stage-A; executed
## at Stage C alongside the six-point read; no new heavy compute beyond that stage's window)

**The construction, fixed now so no post-hoc freedom exists:** the rider's object is the
HEIGHT-MATCHED SURMISE CONTROL from the height-confound guard's standing spec — positions
built on the banked smooth atoms' density with unfolded gaps sampled from the GUE
(Wigner-surmise) law, mean-normalized, deterministic seed = 20260804 (atoms derive from the
banked smooth cache by cumulative sums — no zero-finding; the i.i.d.-sampling caveat stands
on its face). Its RELATIVE c-sequence against the smooth control (pair-structure WITHOUT
arithmetic) is extracted at the same K-ladder and fitted against the same pre-committed
family set under the same criterion. Cost: one cheap atom derivation + moments + one
checkpointed dps-2700 factorization riding the Stage B/C window.

**Registered expectations (VERBATIM from the ferry):** *"(i) if ζ's law is logarithmic and
the control's is NOT, the log is arithmetic in origin — a difference between objects,
informative; (ii) if BOTH are logarithmic, the log is the density's own and the harmonic
pair-weight normalization is under-corrected — the diagnostic names the missing factor and
the corrected denominator becomes π₀'s next candidate; (iii) if ζ's law is geometric, the
control's law is reported as context only."* No interpretation beyond the mapping.

## THE ENSEMBLE OBSERVATION (Tier N, unpromoted; filed BEFORE the verdict so it cannot be
## retro-fitted)

**The arithmetic fact of the estimator table:** four of six limit estimators cluster in
[0.974, 1.019] (the geometric pair 0.9927/1.0186, the power 0.9945, the log-corrected
0.9738; the first two Aitken windows add 0.989/0.995) while the two criterion front-runners
BRACKET unity from far sides (1.3044 and 0.9927). **Both readings stated, explicitly
undecidable on present data:** (reading 1) unity is the sequence's true limit and the
outlying estimator is a noisy extrapolator of a slowly-converging tail; (reading 2) unity is
an attractor of the ESTIMATOR FAMILY (most simple families extrapolate this data shape to
≈1 regardless of the true limit) and the clustering is method-artifact. **Decided by
c(256); filed now.**

## THE SLEEP-RESILIENCE CHECK (filed mid-Stage-A; the running worker untouched)

**(a) Resume validation — WAS NOT SAFE, RESUME PATH PATCHED:** the original
resume-by-linecount trusted any non-empty final line; a hard cut mid-write would leave a
truncated line that resume would count and Stage B would parse as a wrong atom. The patch
(resume path only; the running worker's in-memory code unaffected): `validate_tail()` on
startup — the final line must be ≥ 2,000 chars, mpf-parseable, and in the sane atom range,
else it is DROPPED and recomputed. **(b) Flush posture, verified from code:** per-line
`f.flush()` (process-kill-safe: at most the in-flight zero is lost); `os.fsync` is not
called, so a hard POWER cut could lose OS-buffered tail lines — exactly the case the new
validation guard absorbs (dropped and recomputed on resume). **(c) The resume command,
verbatim — one paste restarts the worker from the banked state:**

```
Start-Process -FilePath python -ArgumentList "D:\relay\tools\e16\k256_atoms_loop.py" -WindowStyle Hidden
```

**The machine's sleep posture (reported; the author's machine, the author's call):** standby
on AC = 60 minutes; hibernate on AC = 180 minutes. Standby SUSPENDS the worker (it resumes
on wake — banked and safe, but the 18-hour clock stretches by the sleep); a power event
mid-write is the truncation case now guarded. **The one-line command that would set both to
Never, if wanted — recommendation only:**

```
powercfg /change standby-timeout-ac 0; powercfg /change hibernate-timeout-ac 0
```

## STAGE A — THE ATOM WORKER

### A-PENDING

## STAGE B — THE FACTORIZATIONS

### B-PENDING

## STAGE C — THE SIX-POINT READ

### C-PENDING

## STAGE D — THE ADJUDICATION

### D-PENDING
