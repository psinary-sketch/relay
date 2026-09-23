# -*- coding: utf-8 -*-
"""b490_trail.py -- THE TRAIL RECORD. ### APPEND-ONLY, PREFIX PROVED, BOM KEPT.
### It enters the TESTED-AT-b334 citation beside the conjecture's falsifier.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
HEAD = ('### b490 — the margin’s increments, the sensitivity ratio, and the '
        'falsifier’s prior test — filed 2026-09-23')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R = json.loads(io.open(os.path.join(D, 'b490_results.json'), encoding='utf-8').read())

BODY = [
    HEAD,
    '',
    '**Ruling `(R100)` is ratified and entered here.** The conjecture’s wording is the '
    'seat’s repair: **for every support width `a` in `[1.3, 5.656854]` on the ladder, '
    '`W(f_a) ≤ −0.024337988`** — graded **MEASURED** on that chart and no higher. '
    '**The three fitted forms of b489 are retired** as descriptions of a margin that turns twice.',
    '',
    '#### Component 0 — pid 27508',
    '',
    '**Neither branch of the order’s conditional holds.** Two readings sixty seconds apart: '
    '**pid 27508 is absent from the process table at both**, and **no `lean` or `lake` process '
    'exists at either**. The order provides for children existing, and for 27508 being alive with '
    'none; it is neither.',
    '',
    '`27508` is **b475’s detached axiom run** (`data/b475_launch.json`, started '
    '`2026-09-22T19:02:24Z`, serialized, `LEAN_NUM_THREADS 1`). Its log is **403,049 bytes by '
    '`stat`, never opened**, last written `2026-09-22T21:33:50` — **idle over three hours**.',
    '',
    '**So a standing exclusion carried since b481 is false.** Every suite from b481 to b489 '
    'excused that log from `G-NOPRIORBANK` because *“another act’s live process is '
    'still appending to it”*. The process died and **nine acts did not re-test the ground**. '
    'The exception is retired here. **An exception is a claim about the world and decays like '
    'one.**',
    '',
    '#### Component 1 — the 34 increments, and what is not available',
    '',
    'All 34 steps are printed with the prime powers entering each — **16 steps admit one, '
    '18 admit none, and those are printed as `(none)` rather than left blank**. The channel split '
    '`d(m) = d(arch) − d(pr)` closes to **6.1e−06** at worst.',
    '',
    '**The decomposition the order asks for is not available.** Splitting an increment into the '
    'newly entered terms’ contribution and the drift of terms already present needs per-`n` '
    'term *values* at both ends of every step. They are banked at **exactly one of the 35 cells** '
    '— `data/b449_integrand.json`, at `a = 4.123106`, the outlier — and **neither `27` '
    'nor `32` is among its eleven terms**, that cell’s window reaching only to `a² = 17`. '
    'The only other route evaluates the smeared window, which is **running the chain**, forbidden '
    'by this order’s own closing line. **`(N1)` is therefore not decidable from the banks — '
    'neither held nor refuted.**',
    '',
    '**And the first draft of that halt was wrong.** It was about to report that *no* bank carried '
    'per-`n` terms. One does. **A halt proved over the wrong population is not a halt**, and the '
    'survey’s own finder caught it, with a positive control showing the finder sees an '
    '`n → value` mapping when one exists and calls a bare list of `n` an index.',
    '',
    '**A six-place rounding decides membership at the edge.** The rungs are `sqrt n` to six '
    'places. `sqrt 17`, `19`, `23`, `29` round **up**, so those powers fall inside their own '
    'rungs; **`sqrt 25`, `27`, `31` and `32` round down** and fall just outside — including '
    'both the order names. On the stored floats **`2^5` never enters the ladder at all**; on the '
    'generator, `3^3` sits exactly at the margin’s local maximum and `2^5` exactly at the '
    'last rung, which is what `(N1)` presumes. **Both readings are printed; neither is silently '
    'chosen.**',
    '',
    '#### Component 2 — the sensitivity ratio',
    '',
    'The two-side disagreement over the margin it prices, at all 35 cells. **It peaks at '
    '`1.07095e−05` at `a = 3.802776`, index 17**, while the margin’s minimum is at '
    '`a = 4.061553`, index 19. **The one verdict: the ratio does not peak within one rung of the '
    'margin’s minimum — the distance is two.** The second-highest ratio *is* at the '
    'minimum cell itself, so the expectation fails by one rung, not by a mile. The whole column '
    'stays below **1.1e−05**: the disagreement never reaches a part in 93,375 of the margin.',
    '',
    '#### Component 3 — the falsifier’s prior test: **TESTED-AT-b334**',
    '',
    '**The conjecture’s falsifier was tested at b334**, and is cited at its bank: '
    '`relay data/b334_the_aim_map.txt`, the paragraph headed *“THE EPSTEIN CROSSING REGION '
    '— THE NEGATIVE CONTROL CHARTED — IS THREE AIMS”*. The three aims, each with '
    'its height and the support that resolved it:',
    '',
    '| aim | height `gamma` | support `a` | `places_q` |',
    '|:--|--:|--:|--:|',
    '| 1 | `16.290216` | **40** | `+0.655053` |',
    '| 2 | `16.290216` | **81** | `+1.362830` |',
    '| 3 | `46.960994` | **81** | `+0.194219` |',
    '',
    '**Every member is at an off-line zero’s height and none is elsewhere**, and b334 records '
    'the region as *empty* on the covered leg, whose widths are `1.3` and `1.41`. **The crossings '
    'exist only where the support resolves the height.**',
    '',
    '**And that is why this ladder could not test it.** The ladder’s last rung is '
    '`a = 5.656854`; the crossings were resolved at `a = 40` and `a = 81`, **seven and fourteen '
    'times wider**. The falsifier is out of range on this chart — not unfired. **An untested '
    'falsifier is not a passed one, and a falsifier tested elsewhere is cited where it was '
    'tested.**',
    '',
    '#### The expectations',
    '',
    '**`(N1)` NOT DECIDABLE FROM THE BANKS** — an absence is a printed result, and scoring it '
    'either way would have invented evidence. **`(N2)` REFUTED** — two rungs, not one. '
    '**`(N3)` HELD.** **`(S1)` REFUTED** — the seat priced its own instrument too cheaply, '
    'allowing `1e−4` where the split closes to `6.1e−06`. **`(S2)` HELD**, '
    '**`(S3)` HELD** — the largest increments sit at the small-`a` end, where no prime power '
    'enters at all and the archimedean channel alone moves the margin.',
    '',
    '#### What this act does not do',
    '',
    '**No chain was run and no lane was opened.** Every value is read from a bank; the arithmetic '
    'is a prime-power sieve, subtraction and division. Nothing compiled. No corpus grade moved. No '
    'FINDINGS section, no ERRATA line, no registry row. Row U1 unedited; the four lists stay OPEN; '
    'nothing deposits; nothing at Zenodo is written; **h2 where the deposit left it**. **Nothing '
    'about RH follows.**',
    '',
]


def main():
    raw = io.open(OT, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    print('=' * 100)
    print('b490 -- THE TRAIL RECORD.')
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
    print('  headings named b490 : %d (must be 1)' % new.count(HEAD))
    print('  the citation TESTED-AT-b334 is present : %s' % ('TESTED-AT-b334' in new))
    print('  the three crossings are tabled : %s' % (new.count('16.290216') >= 2
                                                     and '46.960994' in new))
    print('  the ladder`s reach is stated : %s' % ('seven and fourteen' in new))
    ok = (after.startswith(raw) and not missing and new.count(HEAD) == 1
          and 'TESTED-AT-b334' in new and 'seven and fourteen' in new)
    print('  ### ### **%s**' % ('PASS.' if ok else 'NOT CLEAN.'))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
