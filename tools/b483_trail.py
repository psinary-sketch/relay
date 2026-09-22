# -*- coding: utf-8 -*-
"""b483_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SC = json.load(io.open(os.path.join(D, 'b483_scores.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b483_span.json'), encoding='utf-8'))
S = SC['scores']

ENTRY = """
### b483 — the b477 log read to its end, and the six scored — filed 2026-09-22

**The Gram run finished of its own accord** — `RUN COMPLETE`, `EXIT 0`, **2,337 s against a 2,923 s price** — and this act reads its bank without running a chain, without opening `b475`'s log, and without fetching anything. *The act takes the number `b483`: `b479` is registered by its own ferry and `b482` is banked by its own, so both numbers are claimed.*

#### Component 1 — what the run actually built

**Two within-family Grams, never one joint matrix.** The header declares *aim-plane cells 13 ; ladder cells 22*, and 78 + 231 = **309** off-diagonal entries is exactly the sum of the two within-family pair counts. No cross-family entry exists, and none was invented.

**The diagonal gate that guarded the run passed at every checked cell.** Of 35 cells, the 32 carrying a banked `W` reproduced it with difference **`0.000e+00`, exactly**; the other three printed `NONE`. The runner halts before any off-diagonal on a mismatch, and 309 off-diagonals exist — so the halt did not fire.

#### The finding: a bound the chain *reports* is not the bound it *achieves*

Every zeta entry carries **both sides**, so `|W + Z|` is a per-entry measure of how well they agree. Under Weyl it bounds every eigenvalue.

| | aim plane | ladder |
|:--|--:|--:|
| observed two-side disagreement (spectral norm) | **4.562e-05** | **3.169e-06** |
| reported `trunc_bound` | 1.290e-12 | 6.421e-11 |
| the chain floor, `sqrt(eps)` | 1.490e-08 | 1.490e-08 |

**The reported tail figure under-states the achieved agreement by up to seven orders**, because it bounds the *zero sum's truncation* and says nothing about the *places side's quadrature*. This was stated in the sealed face **before any eigenvalue existed**, so that no threshold could be chosen after seeing a spectrum.

**And the whole verdict turns on that one number.** Zeta's largest wrong-sign excursion is

> **`lam_max(G) = +4.767937e-08`** — at ladder size 22 — **above** the chain floor and the tail figure, **below** the observed agreement.

#### Component 2 — the six, in (R87)'s orientation

| | verdict | the deciding figure |
|:--|:--|:--|
| **(F1)** UNINFORMATIVE | **FIRES** | the control's `-G` at the priced resolving size has the single eigenvalue `+1.606961e+01` |
| **(F2)** HALT | **THRESHOLD-DEPENDENT** | fires on the floor and on the tail figure; **does not fire** on the observed agreement |
| **(F3)** MEASURED | **NOT MET** | conjunct (b) fails: the control is not indefinite *at the priced size* |
| **(N1)** | **REFUTED** | the control is **never** indefinite anywhere in the aim plane |
| **(N2)** | **HELD** at the observed resolution, **REFUTED** at the tail figure | the same `+4.767937e-08` |
| **(N3)** | **REFUTED** | no prime power lies in the step `4.06155 → 4.12311` |

**(F1) fires on form, not on measurement.** `b476` priced the control's resolving family size at **one cell**, from a per-cell test — every cell resolves `t` by five orders or more. But **a one-by-one symmetric matrix cannot be indefinite whatever its entry is**, so a negative index at that size was *arithmetically unavailable before the run started*. **A per-cell resolution test cannot bound the size of a matrix that needs a pair.** The control *does* go indefinite — at ladder size 16 — so **the price was wrong, not the instrument**; and `(F3)` fails on the same defect, which is why the compression register takes **no grade, and in particular not `MEASURED`**.

**One number, read as a halt or as an expectation met, depending on which bound is believed.** `(F2)` and `(N2)` are the same measurement seen from two ends: the excursion sits *between* the reported tail figure and the achieved agreement. **That, and not the number, is this act's finding.**

#### A defect in this act's own scorer, recorded rather than quietly fixed

`(N2)` claims a wrong-signed excursion **that stays within the bound**. The first version of this act's scorer required the excursion to *exceed* the resolution — which is `(F2)`'s test — and scored `(N2)` **REFUTED** on that basis. **A sub-bound claim cannot also be a supra-bound claim.** Caught by re-reading the predicate against `b476`'s own words, and corrected before the components were banked.

#### And a resemblance, named as one

The earliest wrong-sign excursion is at ladder size 8, the cell **`a = 4.12311 = sqrt(17)`** — **the same cell `b446` named as the outlier that refuses**, on a decorrelation-order test with nothing to do with signatures (*"THE OUTLIER 4.123106: order -0.34 against [0.95, 1.95] — REFUSES"*). `b437` has the ladder turning from rung 10 to rung 11 there. **Two unrelated measurements single out one cell — and that is still a resemblance and not a mechanism.** `b446` already refused the obvious reading: *"not the rung alone: 3.605551 = sqrt(13) converged."* Routed; nothing is claimed from it.

#### What this act does not do

**No claim about RH in either direction. No grade above `MEASURED` — and in fact no grade at all.** No chain was run and no entry computed; an entry the bank does not hold is ABSENT, never interpolated. `b475`'s log was not opened and its run was not polled or stopped. Nothing was fetched — **(R90)** assigns the two Zenodo manifests to the author's fetch, and this seat does not attempt them. **(R92)**'s currency repair is routed to the act after this read and is neither performed nor pre-empted here. No corpus grade moved; row U1 is unedited; no bridge typed; `h2` where the deposit left it; the four lists stay OPEN. **The lane closes at this act's end.**

The span by the tool reads **{span}** — **the declared fold threshold**. The desk stands at forty-five, three closed and five minted.
"""

ENTRY = ENTRY.replace('{span}', str(SPAN['current_span']))


def main():
    before = io.open(OT, 'rb').read()
    tail = before.decode('utf-8-sig', 'replace')[-2:]
    sep = '' if tail.endswith(NL + NL) else (NL if tail.endswith(NL) else NL + NL)
    add = (sep + ENTRY.strip(NL) + NL).encode('utf-8')
    io.open(OT, 'ab').write(add)
    after = io.open(OT, 'rb').read()

    print('=' * 96)
    print('b483_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b483 ')]
    print('  b483 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b483_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
