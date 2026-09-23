# -*- coding: utf-8 -*-
"""b488_trail.py -- THE TRAIL RECORD. ### APPEND-ONLY, PREFIX PROVED, BOM KEPT."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
HEAD = '### b488 — the fold’s section written home, and the row writer guarded — filed 2026-09-23'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BODY = [
    HEAD,
    '',
    '**A fold’s home is FINDINGS, by ruling `(R98)`.** b486 filed its fold of eleven acts to '
    'the trail alone, and `b363_span.py` — which reads `FINDINGS.md` — went on naming '
    '`b474` as the last fold. **The section is written home from b486’s own bank; the tool is '
    'not edited; and its reading moved because its input did.**',
    '',
    '#### Component 1 — the section, transcribed',
    '',
    '`## THE BOOKKEEPING ARC, b475–b479 — THE FOLD`, appended to `FINDINGS.md` as its '
    '**nineteenth** fold section. Every block is lifted from `relay data/b486_the_fold.txt` and '
    'b486’s record in this file: the eleven-act span table, the six digest clauses with their '
    'cited acts (**two from outside the span** — b110 and b469), the thirteen rulings, the '
    'seven acts recording a defect of their own instruments, and the fold’s own sentences.',
    '',
    '**Not re-folded.** No verdict is re-read, no act is re-scored, and no figure is typed that '
    'b486’s bank does not carry. **b486’s trail record stands and the section cites it.** '
    'The section is dated as written at b488 for b486.',
    '',
    '**76 lines added, 0 removed**, prior bytes a true prefix, BOM preserved — by git’s '
    'own `--numstat` as well as by byte comparison.',
    '',
    '**The span tool, the same command, unedited:** before, *last fold `b464 - b473`, filed by '
    '`b474`, folds 19, current span 14*; after, *last fold `b475 - b479`, **filed by `b486`**, '
    'folds 20, current span 2*.',
    '',
    '#### Component 2 — `corr_row.py` guarded',
    '',
    '`corr_row.py` gains the guard `errata_append.py` already carries: **it reads the ledger and '
    'refuses a row whose number is already there, before any byte is written.** The refusal is a '
    'return code, not an exception, and it names the next free number without choosing one.',
    '',
    '**Both controls run on a fixture, never on the live ledger** — a positive control that '
    'refuses is safe, but a negative control that *accepts* writes a row. First run, no repair: a '
    'taken number → **code 2, file unchanged**; the next free number → **code 0, file '
    'grew**.',
    '',
    'Its header carries the two new limits beside the three it had: **it checks the number, not '
    'the content**, and **it does not assign numbers**. The tool’s prior behaviour is quoted '
    'in the act’s bank so the change is legible.',
    '',
    '#### The expectations',
    '',
    '**`(N1)` HELD** — the span tool reads `b486` as the act that filed the last fold, from '
    'the section’s own `Filed by bNNN` sentence. **`(N2)` HELD** — the guard’s '
    'positive control refused on its initial run, without repair. **`(S1)`, `(S2)`, `(S3)` HELD.**',
    '',
    '**And the first `(N1)` scorer said REFUTED, reading the wrong line.** The tool prints the '
    'span a fold *covers* and, separately, *the act that filed it*; **a fold heading carries the '
    'span and never the filing act**, so a score taken off the heading can never find `b486`. '
    'Three predicates in two acts have now reported a fault in their subject because their own '
    'needle was absent. **A predicate’s yield is printed before its verdict is trusted.**',
    '',
    '#### What this act does not do',
    '',
    'Nothing compiled. No corpus grade moved and **no verdict of any folded act was re-scored**. '
    'No ERRATA line written. No registry row. Row U1 unedited; the four lists stay OPEN; nothing '
    'deposits; nothing at Zenodo is written; **h2 where the deposit left it**.',
    '',
    '*The span since b486 is **2** — b487 and b488 — counted by the tool.*',
    '',
]


def main():
    raw = io.open(OT, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    print('=' * 100)
    print('b488 -- THE TRAIL RECORD.')
    print('=' * 100)
    if HEAD in old:
        print('  ### ### **THIS ACT`S RECORD IS ALREADY IN THE TRAIL. ### NOT APPENDING AGAIN.**')
        print('  headings named b488 : %d' % old.count(HEAD))
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
    print('  headings named b488 : %d (must be 1)' % new.count(HEAD))
    ok = after.startswith(raw) and not missing and new.count(HEAD) == 1
    print('  ### ### **%s**' % ('PASS.' if ok else 'NOT CLEAN.'))
    json.dump(dict(before=len(raw), added=len(add), after=len(after), removed=len(missing),
                   prefix=after.startswith(raw), headings=new.count(HEAD)),
              io.open(os.path.join(D, 'b488_trail_notes.json'), 'w', encoding='utf-8', newline=NL),
              indent=1)
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
