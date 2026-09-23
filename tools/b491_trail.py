# -*- coding: utf-8 -*-
"""b491_trail.py -- THE TRAIL RECORD. ### APPEND-ONLY, PREFIX PROVED, BOM KEPT."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
HEAD = ('### b491 — the b475 log read, and `(R82)` decided on it — filed 2026-09-23')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R = json.loads(io.open(os.path.join(D, 'b491_results.json'), encoding='utf-8').read())

BODY = [
    HEAD,
    '',
    '**Ruling `(R101)` is ratified and entered here.** The b475 log is read, its process having '
    'been measured dead at b490; `(R82)` is decided on it; and **the numerical lane opens for one '
    'run**, which is b492 and not this act. **This act compiles nothing and launches no build** '
    '— it reads a log as text and commits it as bytes.',
    '',
    '#### The run completed',
    '',
    '**%d `=== EXIT` lines and every one is `EXIT 0`**, across **%d** MODULE marks and three '
    'further STEP marks, ending `=== [Tue 09/22/2026 21:33:50.73] RUN COMPLETE`. '
    '**Non-zero exits: 0.**' % (R['exits'], R['modules']),
    '',
    '**Modules that failed: NONE.** Lines matching an error shape: **0**. Lines naming `sorryAx` '
    'or a `declaration uses ‘sorry’` warning: **0**. That is the answer, printed — '
    '**a clean document is a result**, and an empty bucket is reported as plainly as a full one.',
    '',
    '**The wall time, from two independent marks.** Start to `RUN COMPLETE`: **%d s = %.2f '
    'hours**. lake’s own target durations sum to **%d s = %.2f hours**; the **shortfall of '
    '%d s** is untimed targets and process overhead, and is stated rather than explained away. '
    '**And b480’s launcher defect stands**: 193 timestamped `===` marks carry only **%d '
    'distinct instants**, because a batch `FOR` block expands `%%TIME%%` once — so **no '
    'per-module duration is recoverable from those marks**.'
    % (R['wall_s'], R['wall_s'] / 3600.0, R['dur_sum'], R['dur_sum'] / 3600.0,
       R['shortfall'], R['distinct_instants']),
    '',
    '#### The profiles — twenty lines, seventeen and three',
    '',
    'Two steps the log names produced them: `lake env lean scripts\\PrintAxioms.lean (as shipped)` '
    'at `21:32:34.30`, printing the **seventeen** Challenge theorems, and '
    '`lake env lean B471NamedAxioms.lean` at `21:33:23.92`, printing **three** '
    '— `Zeta23.WeilEF.EF_lit_zetaZeroConfig`, `Zeta23.EF.EF_lit`, '
    '`Zeta23.WeilEF.EF_lit_zeta`. **None is ABSENT.**',
    '',
    '**Every one of the twenty reads** `depends on axioms: [propext, Classical.choice, '
    'Quot.sound]`, matched on the **whole axiom string** and not by counting names, so a fourth '
    'axiom or a missing one would have shown as `OTHER` and been quoted in full. '
    '**STANDARD THREE: 20. OTHER: 0.**',
    '',
    '#### The verdict on `(R82)`: **HOLDS**',
    '',
    'It was **VOID at b473** — the build died of memory — and **VOID again at b480**, '
    'where the log was read as a snapshot with the run still live, at mark 169 of 188. '
    '**Both voidings were FOR WANT OF A RUN; neither was for want of a profile.** That run has '
    'now completed and its profiles are printed, so this is not a third void of the same kind: '
    '**it is the condition being met.**',
    '',
    '**And the verdict’s scope is bounded.** It holds **of the twenty names the log prints, '
    'at the commit b475 built**, and of nothing else. A standard-three profile says the '
    'declaration’s proof term closes without `sorryAx` and without a user axiom. **It does '
    'not say the statement is strong, that its hypotheses are discharged, or that it means what '
    'its name suggests.** b482 found six zeta23 declarations closed by `sorry` elsewhere in that '
    'repository; **those are not these twenty**. **Nothing about RH follows from a profile.**',
    '',
    '#### A check of this seat’s that could never have fired',
    '',
    'After every `reg_satisfiable` run since b487 the seat grepped for the word **`UNSATISFIABLE`** '
    '— which that tool **never prints**. Its vocabulary is `JOINTLY SATISFIABLE`, '
    '`NOT SATISFIABLE` and `CONTRADICTORY`, so **the grep returned 0 for a clean audit and for a '
    'refusing one alike**. It passed b487–b490 by luck; those four audits are genuinely '
    'satisfiable, checked here by reading their verdict lines. **b491’s own first audit read '
    '`NOT SATISFIABLE — DO NOT SEAL`, and the grep reported it clean.** What caught it was '
    'the **lock gate**, whose pass phrase is the tool’s own words. **A check that cannot '
    'fire is not a check, and a habit is not a gate.**',
    '',
    '#### The expectations',
    '',
    '**`(N1)` HELD**, **`(N2)` HELD**, **`(N3)` HELD**; **`(S1)`, `(S2)`, `(S3)` HELD**.',
    '',
    '#### What this act does not do',
    '',
    '**Nothing is compiled and no lane is opened by this act.** `(R101)` opens the numerical lane '
    'for one run, and that run is b492. The log is committed **unchanged** — added to the '
    'index, not written; not one byte altered. `relay/data/anthropic-zeta23/` stays uncommitted. '
    'No corpus grade moved; no FINDINGS section; no ERRATA line; row U1 unedited; the four lists '
    'stay OPEN; nothing deposits; nothing at Zenodo is written; **h2 where the deposit left it**.',
    '',
]


def main():
    raw = io.open(OT, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    print('=' * 100)
    print('b491 -- THE TRAIL RECORD.')
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
    print('  headings named b491 : %d (must be 1)' % new.count(HEAD))
    print('  the verdict is present : %s' % ('`(R82)`: **HOLDS**' in new))
    print('  the scope is bounded  : %s' % ('at the commit b475 built' in new))
    ok = (after.startswith(raw) and not missing and new.count(HEAD) == 1
          and 'at the commit b475 built' in new)
    print('  ### ### **%s**' % ('PASS.' if ok else 'NOT CLEAN.'))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
