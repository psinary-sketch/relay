# -*- coding: utf-8 -*-
"""b495_waiver.py -- COMPONENT 3. ### **THE RULE-9 WAIVER, APPENDED BESIDE RULE 9.**

### ### **APPENDED, AND NOTHING ABOVE IT REWRITTEN.** ### The proof is not the intention: the
### file's bytes before the append are hashed, and the append is verified to be a PREFIX-PRESERVING
### write -- every byte before is a byte after, in the same order, and 0 lines are removed.
"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SPIRAL = os.path.join(PP, 'SPIRAL_MAP.md')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


HEADING = '## Waiver — 2026-09-23 — rule 9 for vendored namespaces (act b495)'

NOTE = """
---

%s

**SECTION 7, BESIDE RULE 9.** Rule 9 — *"Vanilla Lean 4 syntax discipline. No `lemma` keyword
(Mathlib alias) — always `theorem`. Prefer `by omega` for finite arithmetic over `Eq.subst` (▸)
when direction is unclear."* — is **WAIVED FOR VENDORED NAMESPACES**.

**THE REASON IS ACT b495**, which created `SIDE-explicit-formula` by vendoring %d modules of
the `zeta23` formalization at pin `%s` = `%s`. Every body in that kernel is a
byte-identical copy, proved per module by a pair of digests (source at the pin, copy on disk
before any header). **A VENDORED FILE IS NOT EDITED.** Rule 9 governs how this programme writes
Lean; it cannot govern text this programme did not write, and enforcing it on a vendored body
would require the one thing vendoring forbids — **changing the body**.

**THE WAIVER IS NARROW AND IT NAMES ITS BOUNDARY.** It covers namespaces vendored under rule 7
(*"Composites vendor with attribution"*), and it covers them **only as long as the body stays
unedited**. The moment a line of a vendored file is changed by this programme, the file stops
being vendored, rule 7's header stops being true of it, and rule 9 applies to it in full.

**WHAT THIS WAIVER IS NOT.** It is not a licence to write non-vanilla Lean anywhere in the
federation. It is not retroactive to any existing kernel. It confers no grade, and it says
nothing whatever about whether any vendored terminal is correct, compiles, or has been
profiled — at the time of writing `SIDE-explicit-formula` has **no profile at all**.
"""


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    cj = json.loads(io.open(os.path.join(D, 'b495_create.json'), encoding='utf-8').read())

    with open(SPIRAL, 'rb') as fh:
        before = fh.read()
    before_lines = before.decode('utf-8', 'replace').replace(chr(13), '').split(NL)

    rec('=' * 104)
    rec('b495 COMPONENT 3 -- THE WAIVER. ### **APPENDED BESIDE RULE 9; NOTHING ABOVE IT REWRITTEN.**')
    rec('=' * 104)
    rec('  file   : PLACE-papers/SPIRAL_MAP.md')
    rec('  before : %d bytes, %d lines, sha256 %s' % (len(before), len(before_lines), sha(before)))

    # ### ### **RULE 9 IS LOCATED BEFORE IT IS CITED**, and its own words are quoted from the file.
    idx = next((i for i, l in enumerate(before_lines)
                if l.lstrip().startswith('9.') and 'Vanilla Lean 4 syntax discipline' in l), None)
    sec = next((i for i, l in enumerate(before_lines)
                if l.startswith('## 7. Federation discipline')), None)
    rec('  rule 9 found at line %s ; section 7 heading at line %s'
        % ((idx + 1) if idx is not None else '### NOT FOUND',
           (sec + 1) if sec is not None else '### NOT FOUND'))
    if idx is None or sec is None:
        rec('  ### ### **HALT. ### THE RULE THE WAIVER NAMES IS NOT AT ITS ADDRESS.**')
        return 2
    rec('  rule 9, quoted from the file : %s' % before_lines[idx].strip()[:88])
    rec('')

    if HEADING in before.decode('utf-8', 'replace'):
        rec('  ### ### **THE WAIVER IS ALREADY PRESENT. ### REFUSING TO APPEND A SECOND.**')
        return 2

    note = (NOTE % (HEADING, cj['modules'], cj['pin'], cj['pin_sha'])).encode('utf-8')
    with open(SPIRAL, 'ab') as fh:
        fh.write(note)
    with open(SPIRAL, 'rb') as fh:
        after = fh.read()
    after_lines = after.decode('utf-8', 'replace').replace(chr(13), '').split(NL)

    prefix_ok = after.startswith(before)
    removed = len(before_lines) - sum(1 for a, b in zip(after_lines, before_lines) if a == b)
    headings = after.decode('utf-8', 'replace').count(HEADING)

    rec('  after  : %d bytes, %d lines, sha256 %s' % (len(after), len(after_lines), sha(after)))
    rec('  ### ### **PREFIX PROOF : %s** -- every byte before the write is a byte after it, in'
        % prefix_ok)
    rec('  ### order. ### **LINES REMOVED : %d.** ### **HEADINGS ADDED : %d.**' % (removed, headings))
    rec('  ### ### **NOTHING ABOVE THE APPEND WAS REWRITTEN**, and that is proved by the prefix,')
    rec('  ### not asserted by the tool that did the writing.')
    rec('  ### the waiver NAMES ITS BOUNDARY: it lapses for any file this programme edits, and it')
    rec('  ### is not retroactive to any existing kernel. ### It confers no grade.')
    rec('=' * 104)

    io.open(os.path.join(D, 'b495_waiver.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(before_sha=sha(before), after_sha=sha(after), prefix=prefix_ok,
                   lines_removed=removed, headings=headings, rule9_line=idx + 1,
                   section7_line=sec + 1, bytes_added=len(after) - len(before)),
              io.open(os.path.join(D, 'b495_waiver.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b495_waiver.txt, b495_waiver.json')
    return 0 if (prefix_ok and removed == 0 and headings == 1) else 1


if __name__ == '__main__':
    sys.exit(main())
