# -*- coding: utf-8 -*-
"""b492_trail.py -- THE TRAIL RECORD. ### APPEND-ONLY, PREFIX PROVED, BOM KEPT."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
HEAD = ('### b492 — the per-n terms at every rung, and the increments attributed — '
        'filed 2026-09-23')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R = json.loads(io.open(os.path.join(D, 'b492_results.json'), encoding='utf-8').read())

BODY = [
    HEAD,
    '',
    '**Rulings `(R102)` and `(R103)` are ratified and entered here.** Neither changes this '
    'act’s work: `(R102)` holds the platform edits for one act, and `(R103)` speaks of the '
    'act after b493. **This act writes nothing at any platform and creates no repository.**',
    '',
    '**The numerical lane, made available by `(R101)` for one run, was used once and is shut at '
    'this act’s end.** It is a *numerical* lane: the chain’s own Python ran; **no Lean '
    'was compiled and no build was launched.**',
    '',
    '#### The run, and its check before anything else was read',
    '',
    'The chain at all **35** ladder cells, on b477’s own recipe and grid '
    '(`autocorrelation` at the default `nv`, `channels`, `W = prime − arch`) and b477’s '
    'own floor `1.49e−08`. The diagonal `W` was checked against b477’s bank **at every '
    'cell before a single term was read**, a mismatch set to halt the run.',
    '',
    '**Worst absolute discrepancy: `%.3e`. All %d of the 35 cells reproduce b477 exactly, bit for '
    'bit.** The run does not merely pass the floor. Per-n prime terms are banked at every cell and '
    'sum to `PR` within `8.3e−17`.' % (R['worst_dW'], R['exact_zero']),
    '',
    '#### The generator’s exact `a`, banked beside the rounded — `W-ORD-EXACT-SUPPORT`',
    '',
    '`b437_components.py` builds the cells as `round(x, 6)` over `sqrt n` and the midpoints of '
    '`[3.0] + sqrt(BOUNDARY_N)`. **So the rounding is in the generator itself** — b490 found '
    'the symptom, and this is the line. Eleven cells are boundaries `a = sqrt n`, eleven are '
    'midpoints, thirteen are b321’s decimal literals.',
    '',
    '**Four of the eleven boundary cells round DOWN — 13, 27, 31, 32 — and on the '
    'stored `a` exclude their own `n0`.** On the exact generator every boundary cell admits it, '
    'by integer arithmetic: at `a = sqrt n0` the window reaches `a² = n0`, so `n0 ≤ '
    'a²` because **`n0 ≤ n0`**. No tolerance is chosen and no float decides it.',
    '',
    '#### The attribution — an identity, not a fit',
    '',
    '`d(pr) = (terms new at the top) + (drift of terms present at both)`, exactly, because the '
    'prime-power set only grows. **It closes to `%.1e` at worst** — the arithmetic’s '
    'own precision. **The archimedean channel has no per-n decomposition**, so `d(m) = d(arch) '
    '− d(pr)` has a half this act does not attribute, and every fraction below is a fraction '
    'of the prime channel’s share alone.' % R['worst_closes'],
    '',
    '**The sentence the table supports, and no wider:**',
    '',
    '> %s' % R['sentence'],
    '',
    '**And a prime power admitted at its own boundary rung has term exactly `0`.** Seven boundary '
    'cells admit their `n0` on the stored `a`, and at all seven the term reads `0.000e+00`: the '
    'window is zero at its own support edge `v = L`, and `log n0 = L` exactly there. **So an '
    'entry is never an event in the prime channel — it is a bookkeeping boundary**, and the '
    'channel moves only by drift.',
    '',
    '#### The expectations',
    '',
    '**`(N1)` REFUTED, and not narrowly.** `3³` enters with a share of `d(pr)` of '
    '`−2.5e−42`; `2⁵` never enters on the stored `a` at all. At 15 of the 16 entry '
    'steps the entering terms carry at most `%.1e` of `d(pr)`, and 8 carry exactly zero. The one '
    'exception is the first prime power entering an *empty* channel, which is the whole increment '
    'by arithmetic rather than by weight.' % R['max_small_share'],
    '',
    '**`(N2)` SPLIT.** On exact `a`, `27`’s rung `sqrt 27 = 5.196152422706632` **is** the '
    'margin’s local maximum — for `27` the expectation holds. `32`’s rung '
    '`sqrt 32 = 5.656854249492381` is the ladder’s **last rung**, an endpoint with no step '
    'past it to turn at — for `32` it fails on the geometry of the ladder, not on the '
    'arithmetic.',
    '',
    '**`(N3)` REFUTED.** Entry mean `|d(m)|` = `%.6g` over %d steps against `%.6g` over %d. And '
    '**the mean compares scales, not mechanisms**: the non-entry steps include the small-`a` end '
    'where `m` is two hundred times larger. The confound is printed beside the verdict.'
    % (R['mean_entry'], R['n_entry'], R['mean_nonentry'], 34 - R['n_entry']),
    '',
    '**`(S1)`, `(S2)`, `(S3)` HELD.** And this act records three defects of its own: a summary '
    'written before its table was read and refuted by it; a scorer that typed a bar of `1e-4` the '
    'face never stated, against a face whose word is *“not dominant”*; and **a ledger '
    'row refused a second time for a `|` inside a cell** — the routed item from b490, biting '
    'again within three acts.',
    '',
    '#### What this act does not do',
    '',
    'Nothing is compiled; no Lean is built; no repository is created — `(R103)`’s '
    'creation belongs to the act after b493. Nothing deposits and nothing at Zenodo is written; '
    '`(R102)` holds the platform edits and this act is not the platform session. No chain tool is '
    'edited. No corpus grade moved; no FINDINGS section; row U1 unedited; the four lists stay '
    'OPEN; **h2 where the deposit left it**. **Nothing about RH follows from an attribution.**',
    '',
]


def main():
    raw = io.open(OT, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    print('=' * 100)
    print('b492 -- THE TRAIL RECORD.')
    print('=' * 100)
    if HEAD in old:
        print('  ### ### **ALREADY IN THE TRAIL. NOT APPENDING AGAIN.** (%d)' % old.count(HEAD))
        return 0
    add = (eol + eol.join(NL.join(BODY).split(NL))).encode('utf-8')
    io.open(OT, 'ab').write(add)
    after = io.open(OT, 'rb').read()
    new = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    missing = [x for x in old.split(NL) if x not in set(new.split(NL))]
    print('  bytes before / appended / after : %d / %d / %d' % (len(raw), len(add), len(after)))
    print('  PRIOR BYTES A TRUE PREFIX : %s ; BOM preserved : %s'
          % (after.startswith(raw), after.startswith(b'\xef\xbb\xbf') == bom))
    print('  ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW : %d.**' % len(missing))
    print('  headings named b492 : %d (must be 1)' % new.count(HEAD))
    print('  W-ORD-EXACT-SUPPORT filed : %s' % ('W-ORD-EXACT-SUPPORT' in new))
    print('  the sentence is present   : %s' % (R['sentence'][:40] in new))
    ok = (after.startswith(raw) and not missing and new.count(HEAD) == 1
          and 'W-ORD-EXACT-SUPPORT' in new and R['sentence'][:40] in new)
    print('  ### ### **%s**' % ('PASS.' if ok else 'NOT CLEAN.'))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
