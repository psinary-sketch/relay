# -*- coding: utf-8 -*-
"""b489_trail.py -- THE TRAIL RECORD. ### APPEND-ONLY, PREFIX PROVED, BOM KEPT.
### It carries the conjecture's sentence AS THE ORDER WORDS IT, with the refutation beside it.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
HEAD = ('### b489 — the margin’s law over support, read from the banks and registered as '
        'a conjecture — filed 2026-09-23')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R = json.loads(io.open(os.path.join(D, 'b489_results.json'), encoding='utf-8').read())

BODY = [
    HEAD,
    '',
    '**Ruling `(R99)` is ratified and entered here.** Of the three b487 drafts, `s2` is applied as '
    'drafted; `s14` is applied with its surround restored; **`s15` is not applied** — its '
    'draft presents a stand-in grade as the concordance’s assignment, which b467 found the '
    'concordance does not make. The author applies `s14` and `s2` at the platform. **This act '
    'applies nothing, fetches nothing, and writes no ERRATA line**; the fetch-back belongs to the '
    'act after the author applies.',
    '',
    '#### Component 1 — the margin, cell by cell',
    '',
    'By `(R87)`, `W = PR − A`, so the margin is **m(a) = −W(f_a) = A − PR**. The '
    'ladder’s 35 cells are read from `relay data/b477_entries.jsonl` (`kind == "diagonal"`), '
    'each with its **independently banked zero side** and the two-side residual printed beside it. '
    'The aim map’s 56 cells are read from the three `b334` leg banks as `room_z`.',
    '',
    '**Every margin is positive** — minimum `0.024337988`, maximum `8.78115282` — so '
    '`W(f_a) < 0` at every cell the ladder reaches.',
    '',
    '**And the margin has two turning points, not one.** It falls monotonically over 19 steps to a '
    '**minimum `m = 0.024337988` at `a = 4.061553`**; rises over 9 steps to a **local maximum '
    '`m = 0.0422898584` at `a = 5.196152`**; then falls again over the last 6 steps to '
    '`0.0382311845` at `a = 5.656854`. **9 of the 34 steps rise, all of them between the two '
    'turns.** The minimum sits one rung before `a = 4.123106` — the cell `b446` and `b447` '
    'already called an outlier.',
    '',
    '**On the aim map the margin is not a function of `a` at all.** At a fixed width it varies more '
    'than it varies between widths, so that family carries four distinct widths with fourteen-fold '
    'replication, and a fit of `m` against `a` there fits through a spread it does not model.',
    '',
    '**`(R70)`’s rehearsal earned its place.** Its first reading of the aim map took '
    '`places_z` for the prime slot and got a **negative** margin where the map prints a positive '
    'room; `places_z` is already the signed places sum — that family’s `W` — and '
    'the prime slot is `prime_z`. **A sign error would have run through every aim-map cell.**',
    '',
    '#### Component 2 — the shape, fitted and not believed',
    '',
    'Three forms were fixed on the sealed face **before any fit**, and the loss was fixed with '
    'them. Least squares on `m` is primary; least squares on `log m` is reported beside it, '
    'because a preference stated without its loss is not a result.',
    '',
    '| form | pars | RMS on `m` | RMS on `log m` |',
    '|:--|--:|--:|--:|',
    '| **(i) `C · a^(−p)`** | 2 | **0.139525** | 0.559248 |',
    '| (ii) `C · (log a)^(−q)` | 2 | 0.281395 | 0.612822 |',
    '| (iii) `c0 + C · exp(−k a)` | 3 | 0.209401 | **0.311239** |',
    '',
    '**The ladder prefers a power of `a` on the primary loss and a constant-plus-decay on the log '
    'loss; the aim map prefers the third form on `m` by a factor of 1.01 and the second on '
    '`log m`.** The two losses **disagree on both families**, and form (iii) carries a third '
    'constant the others do not. **The ranking is not robust.**',
    '',
    '**A fit over thirty-five cells is a description, not a law.** Every one of the three forms is '
    'monotone in `a` by construction, and the ladder’s margin turns twice — so all three '
    'mis-describe the shape whatever their residual.',
    '',
    '#### Component 3 — the conjecture, its falsifier and its prediction',
    '',
    '**The sentence, as the order words it:** *For every support width `a` in the class, '
    '`W(f_a) ≤ −m_fit(a)`, with `m_fit(a) = 23.823147 · a^(−3.98372886)` '
    '— graded **CONJECTURED**, from a finite-reach chart of 35 support widths in '
    '`[1.3, 5.656854]`, and no higher.*',
    '',
    '**And it is false on the very chart it was fitted to.** The measured `m` falls below '
    '`m_fit(a)` at **17 of the 35 cells**. **A least-squares fit is a centre line, not a bound**, '
    'and roughly half its own data lies below it by construction. The repair the data supports '
    '— `m_min = 0.024337988` in place of `m_fit` — **is true at all 35 cells** and is a '
    'statement about a finite chart rather than a law over a class. **It is offered and not '
    'adopted; the choice is the author’s.**',
    '',
    '**The falsifier is out of range, not unmet.** The Epstein control’s margin, '
    '`m_Q = arch − finite`, is **positive at all 35 cells with zero sign changes**, falling '
    'monotonically from `16.0696` to a minimum `1.16912` at the last rung. But the falsifier names '
    'a support *resolving `t = 16.29`*, and `16.290216` is a **gamma** — an aim’s height '
    '— which the aim map reaches only at widths `40` and `81`. **The ladder stops at '
    '`5.656854`.** So this table cannot fire the falsifier in either direction. **An untested '
    'falsifier is not a passed one.**',
    '',
    '**The prediction, so a later measurement can refute it.** The next cell at the ladder’s '
    'own last ratio is **`a = 5.701753`**. Form (i) predicts `m = 0.023188186`; form (ii) '
    '`0.231932268`; form (iii) `0.085854237`. **They disagree by a factor of 10 one step past the '
    'data**, and the second turn says the measured value is likelier to fall than to follow any of '
    'them.',
    '',
    '#### The expectations',
    '',
    '**`(N1)` REFUTED** — 9 of 34 steps rise. **`(N2)` REFUTED** — form (ii) wins the '
    'primary loss on neither family. **`(N3)` REFUTED** — zero sign changes, zero negative '
    'cells. **`(S1)` HELD**, **`(S2)` HELD**, **`(S3)` SPLIT**: every form is monotone as '
    'expected, but the residual is concentrated at the **small-`a`** end (RMS `0.183` before the '
    'turn against `0.0247` after), not past the turn — an absolute residual is dominated by '
    'the cells where `m` is largest. **Where a fit is wrong and where its residual lives are '
    'different questions.**',
    '',
    '#### What this act does not do',
    '',
    '**No chain was run and no lane was opened.** Every value is read from a bank; the only '
    'arithmetic is a prime-power sieve and a least-squares fit over banked numbers. Nothing '
    'compiled. No corpus grade moved. No FINDINGS section, no ERRATA line, no registry row. Row U1 '
    'unedited; the four lists stay OPEN; nothing deposits; nothing at Zenodo is written; **h2 where '
    'the deposit left it**. **Nothing about RH follows from a fit.**',
    '',
]


def main():
    raw = io.open(OT, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    print('=' * 100)
    print('b489 -- THE TRAIL RECORD.')
    print('=' * 100)
    if HEAD in old:
        print('  ### ### **THIS ACT`S RECORD IS ALREADY IN THE TRAIL. ### NOT APPENDING AGAIN.**')
        print('  headings named b489 : %d' % old.count(HEAD))
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
    print('  headings named b489 : %d (must be 1)' % new.count(HEAD))
    print('  the conjecture`s sentence is present : %s'
          % ('W(f_a) ≤ −m_fit(a)' in new))
    print('  and its refutation beside it : %s' % ('17 of the 35 cells' in new))
    ok = (after.startswith(raw) and not missing and new.count(HEAD) == 1
          and '17 of the 35 cells' in new)
    print('  ### ### **%s**' % ('PASS.' if ok else 'NOT CLEAN.'))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
