# -*- coding: utf-8 -*-
"""b335_rule6.py -- RULE 6, THE STOP FORMAT, APPENDED ONCE TO THE EXECUTOR'S RULES.

### ### The file `PLACE-papers/protocols/EXECUTOR_RULES.md` gains lines at its end only; Rules 1-5 are byte-identical;
### the write is idempotent (a second run writes nothing) and read back as a true prefix of the working file and of
### the blob. ### The rule's words: the executor's final message for an act (its STOP) carries, after the closing
### summary and the pins, a block headed `DRAFT -- NAVIGATOR EDITS` with a draft of the next ferry; the draft binds
### nothing. ### One path, one run file, numbered on a repeat writing run.
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
RULES = os.path.join(PP, 'protocols', 'EXECUTOR_RULES.md')
MARK = '## Rule 6 \u2014 The STOP format'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RULE = [
    '',
    '## Rule 6 \u2014 The STOP format (filed 2026-09-06, author-ruled at the b335 sortie, leg 0)',
    '',
    "The executor's final message for an act \u2014 its STOP \u2014 has three parts, in this order:",
    '',
    '1. **THE CLOSING SUMMARY** \u2014 what the act found, what it did, what it left undone and why, in its own',
    '   words, with every number from a committed record; for a sortie, one summary paragraph per leg.',
    '2. **THE PINS** \u2014 by ls-remote across all three repos, with the censuses, the hook and the mirror where',
    '   the papers repo moved.',
    '3. **THE DRAFT** \u2014 a block headed `DRAFT \u2014 NAVIGATOR EDITS` carrying a draft of the next ferry in the',
    "   ferry's own shape (the act's name, its scope, its components, its closing, its execution line, its",
    '   foot). **The draft binds nothing.** It is not a ferry, it is not scanned as one, and the next act runs',
    "   only on the navigator's paste \u2014 edited, replaced or discarded. Its purpose is to put the executor's",
    "   reading of the desk in front of the navigator in the ferry's own form, so the navigator edits rather",
    '   than dictates.',
    '',
    'A STOP without the draft is incomplete and says so. The standing clauses a draft would restate are carried',
    'by reference to `relay/tools/FERRY_STANDING.md` at its current version (b335).',
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b335 -- RULE 6, THE STOP FORMAT, APPENDED ONCE.')
    rec('=' * 100)
    before = io.open(RULES, encoding='utf-8', errors='replace').read()
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:protocols/EXECUTOR_RULES.md'], capture_output=True).stdout.decode('utf-8', 'replace')
    if MARK in before:
        rec('  ALREADY PRESENT -- nothing written (idempotent) ; mark once : %s' % (before.count(MARK) == 1))
        rec('=' * 100)
        return 0
    new = before.rstrip(chr(10)) + chr(10) + chr(10).join(RULE) + chr(10)
    open(RULES + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(RULES + '.tmp', RULES)
    after = io.open(RULES, encoding='utf-8', errors='replace').read()
    pw = after.startswith(before.rstrip(chr(10)))
    nb = after.replace(chr(13) + chr(10), chr(10)).startswith(blob.replace(chr(13) + chr(10), chr(10)).rstrip(chr(10)))
    rec('  WRITTEN +%d lines ; working TRUE PREFIX %s ; blob TRUE PREFIX %s ; mark once %s' % (len(after.splitlines()) - len(before.splitlines()), pw, nb, after.count(MARK) == 1))
    rec('=' * 100)
    return 0 if (pw and nb and after.count(MARK) == 1) else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    base = 'b335_rule6_run' if wrote else 'b335_rule6_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
