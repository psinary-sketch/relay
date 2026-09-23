# -*- coding: utf-8 -*-
"""b493_trail.py -- THE TRAIL RECORD. ### APPEND-ONLY, PREFIX PROVED, BOM KEPT."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
HEAD = '### b493 — the eight records read whole against the ceiling — filed 2026-09-23'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R = json.loads(io.open(os.path.join(D, 'b493_results.json'), encoding='utf-8').read())
per = R['per_record']

BODY = [
    HEAD,
    '',
    '**Ruling `(R104)` is ratified and entered here.** It fixes the forward order of acts and '
    '**opens nothing by itself**; the census it calls for belongs to the act after this one. '
    '`(R102)` holds the platform edits for one act, and **this act is not the platform session** '
    '— it prepares the disposition that session would apply.',
    '',
    '#### The source',
    '',
    'The author’s Zenodo screen of 2026-09-14 is banked verbatim at '
    '`relay data/zenodo_listing_2026-09-14_author_screen.txt` — **72 lines, 20,334 bytes, '
    'sha256 `7528bd858616ccd116dbc52ea86b17a6f4b96a962efe5ef4d1a215c2dfaecb0b`**, eight records. '
    '**Nothing was fetched.**',
    '',
    '**No description is truncated.** The first test said three were — records 5, 6 and 7, '
    'which end `Author: J. York Seale ORCID: 0009-0008-7993-0310`. **That is a template’s '
    'trailer, not a cut**: those three are 779, 899 and 704 characters long, and *a screen '
    'truncation cuts at a width, not at a trailer*. So the clause’s fallback was not '
    'invoked; and the four May-2026 repositories carry no `.zenodo.json` at all, so it would have '
    'had no source for them had one been needed.',
    '',
    'The monograph’s screen text agrees with `b359_fetch_F2.json` **entity for entity** '
    '— every divergence is `&xi;` against `ξ`, `&sigma;` against `σ`, `&sect;` '
    'against `§`; the 107-character difference is encoding, not content.',
    '',
    '#### The disposition — 104 rows',
    '',
    '96 sentences plus 8 titles, against the ceiling quoted from `(R102)`: *“Supportable: RH '
    'reduced to a single located clause, reduction machine-verified; not supportable: RH '
    'proved.”*',
    '',
    '| record | STANDS | RESTS | EXCEEDS |',
    '|:--|--:|--:|--:|',
    '| 1 T₇ Matched-Arc CMB Search | %d | %d | %d |' % (per['1']['stands'], per['1']['rests'],
                                                            per['1']['exceeds']),
    '| 2 A Place To Stand | %d | %d | **%d** |' % (per['2']['stands'], per['2']['rests'],
                                                   per['2']['exceeds']),
    '| 3 SIDE-lv-conservation | %d | %d | **%d** |' % (per['3']['stands'], per['3']['rests'],
                                                       per['3']['exceeds']),
    '| 4 SIDE-kernel | %d | %d | **%d** |' % (per['4']['stands'], per['4']['rests'],
                                              per['4']['exceeds']),
    '| 5 SIDE-cosmo | %d | %d | %d |' % (per['5']['stands'], per['5']['rests'],
                                         per['5']['exceeds']),
    '| 6 SIDE-effects | %d | %d | %d |' % (per['6']['stands'], per['6']['rests'],
                                           per['6']['exceeds']),
    '| 7 SIDE-trivium | %d | %d | %d |' % (per['7']['stands'], per['7']['rests'],
                                           per['7']['exceeds']),
    '| 8 SIDE-interfaces | %d | %d | %d |' % (per['8']['stands'], per['8']['rests'],
                                              per['8']['exceeds']),
    '| **TOTAL** | **%d** | **%d** | **%d** |' % (R['stands'], R['rests'], R['exceeds']),
    '',
    '**The %d EXCEEDS rows carry no replacement.** The order is explicit: a title or headline '
    'that exceeds the ceiling is **the author’s to reword, and this act names it and '
    'stops**. Three are titles — the monograph’s, the kernel’s, and '
    '**`SIDE-lv-conservation`’s, which the order did not name**; two more are headline-led '
    'sentences; five of the eight in all sit in a title or a headline. **A headline compresses, '
    'and compression is where a ceiling is breached.**' % R['exceeds'],
    '',
    '#### The correction to b487',
    '',
    '**The kernel’s deposited description is not the text in its repository.** `SIDE-kernel` '
    'at tag `v1.5` ships a `.zenodo.json` whose description is **1,143 characters**, opening '
    '*“Lean 4 formalization of the SIDE Exclusion Principle applied to the Riemann zeta '
    'function.”* The deposited record carries **3,143 characters**, opening '
    '*“SIDE-kernel: the machine-verified architecture…”*. **They are different '
    'texts.**',
    '',
    'b487 read the repository’s file and graded *“The kernel proves that no off-line '
    'zero exists by exhaustively excluding every mechanism class…”* as resting on '
    '`E-2026-09-14-1`. **That sentence is in the `.zenodo.json` and not in the record.** '
    '`(R99)` ruled it *applied as drafted* — and applying it would edit a sentence the '
    'record does not contain. **This act names it and stops**: the kernel carries no RESTS row '
    'here, its `(R99)` text is held for the author’s ruling, and the paste-ready block '
    'carries the monograph’s two rows only. **A source that ships beside a deposit is not '
    'the deposit.**',
    '',
    '#### The expectations',
    '',
    '**`(N1)` HELD** — and a third title exceeds that the order did not name. '
    '**`(N2)` HELD** — though the first ceiling matcher used `[^.]` and could not cross the '
    'full stop in `MAIN THEOREM. The Riemann Hypothesis:`, and would have scored it refuted. '
    '**A matcher that cannot cross a full stop cannot read a headline.** '
    '**`(N3)` HELD** — and at records 3 and 4 that is a *correction* to b487, not agreement '
    'with it.',
    '',
    '**`(S1)` HELD**, **`(S2)` REFUTED**, **`(S3)` HELD.** The four May-2026 kernels exceed at '
    '**zero** rows: they describe their own subject matter and make no claim about RH at all. '
    '**The seat expected age to correlate with overreach; it does not.** Overreach tracks the '
    '**subject being RH**, not the age of the text.',
    '',
    '#### What this act does not do',
    '',
    '**Nothing is fetched and nothing at Zenodo is written.** Nothing compiled; no lane opened; '
    'no repository created — `(R103)`’s creation belongs to the act after this one. '
    'No corpus grade moved; no FINDINGS section; no ERRATA line; row U1 unedited; the four lists '
    'stay OPEN; **h2 where the deposit left it**. **A disposition is a reading of words against a '
    'ceiling, not a judgement on mathematics, and nothing about RH follows from any row of it.**',
    '',
]


def main():
    raw = io.open(OT, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    print('=' * 100)
    print('b493 -- THE TRAIL RECORD.')
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
    print('  headings named b493 : %d (must be 1)' % new.count(HEAD))
    print('  the ceiling is quoted     : %s' % ('not supportable: RH proved' in new))
    print('  the b487 correction filed : %s' % ('is not the text in its repository' in new))
    ok = (after.startswith(raw) and not missing and new.count(HEAD) == 1
          and 'not supportable: RH proved' in new
          and 'is not the text in its repository' in new)
    print('  ### ### **%s**' % ('PASS.' if ok else 'NOT CLEAN.'))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
