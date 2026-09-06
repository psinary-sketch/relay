# -*- coding: utf-8 -*-
"""b337_errata.py -- THE ERRATA PARTITION, BY ONE APPENDED BLOCK; ENTRIES UNMOVED. AND THE CURRENCY NOTE.

### ### **THE RULING, THE AUTHOR'S, RATIFIED BY THE SORTIE PASTE:** *"ERRATA is partitioned into a deposit-facing section and
### an internal-record section by an append-only header line, entries unmoved."* ### This tool appends ONE block at the
### end of `ERRATA.md` under the mark `<!-- b337 partition -->`: the header line stating the ruling, the two lists of
### entry ids with each entry's own placing words (registration (D)), and the currency note against the head's
### sentence, with the fetch's fields (read from `b337_fetch.json`) and REGISTRY's row. ### Every entry's text is
### byte-identical afterwards; the file is a true prefix of its blob plus the block; idempotent.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
ERR = os.path.join(PP, 'ERRATA.md')
MARK = '<!-- b337 partition -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DEPOSIT_FACING = [
    ('E-2026-07-23-1', 'the claim as deposited, section 18.2'),
    ('E-2026-07-12-1', '"as deposited", Route 1 and the formation certificates'),
    ('E-2026-07-13-1', 'deposit-frozen count claims, with its addendum'),
    ('E-2026-07-18-1', 'deposited monograph v1.1.0'),
    ('E-2026-08-24-2', 'the deposited record TITLES -- platform metadata on immutable records, routed not corrected'),
]
INTERNAL_RECORD = [
    ('E-2026-07-27', 'audit-trail record, additive synthesis; no prior claim corrected'),
    ('E-2026-08-31-1', 'NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY'),
    ('E-2026-08-24-1', "NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY -- REGISTRY's own lines"),
    ('E-2026-08-24-3', 'No deposited artifact is affected -- the patent deadline board'),
    ('E-2026-09-03-1', 'INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED'),
]
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def entry_ids(text):
    return re.findall(r'(?m)^## (E-\d{4}-\d{2}-\d{2}(?:-\d+)?) ', text)


def block(fetch):
    got = fetch['got']
    L = ['', MARK, '',
         '## THE PARTITION \u2014 filed 2026-09-06 (b337, leg 2 of the sortie), per the author\'s ruling ratified by the sortie paste',
         '',
         '**THE RULING, AS RATIFIED:** *"ERRATA is partitioned into a deposit-facing section and an internal-record section by an append-only header line, entries unmoved."* **This block is that header line.** No entry above moves and no entry is edited; each entry is placed by its own words (quoted beside its id), and a reader holding a deposited copy reads the DEPOSIT-FACING list first.',
         '',
         '**DEPOSIT-FACING** \u2014 entries that correct or concern a deposited artifact\'s content or metadata:',
         '']
    for eid, why in DEPOSIT_FACING:
        L.append('- `%s` \u2014 *%s*' % (eid, why))
    L += ['', '**INTERNAL-RECORD** \u2014 entries whose own words place them in the corpus\'s internal record:', '']
    for eid, why in INTERNAL_RECORD:
        L.append('- `%s` \u2014 *%s*' % (eid, why))
    L += ['',
          '**THE CURRENCY NOTE, AGAINST THE HEAD\'S SENTENCE (a drift repair by appending; the head is not edited, the ledger\'s own law).** The head of this file says *"The current deposit is the monograph at manuscript v5.8 / Zenodo v1.1.1 (10.5281/zenodo.21436278)"*. That sentence describes the deposit as it stood when the head was written and is left as written. **The current deposit, per one read-only fetch of the public record on 2026-09-06 (b337) and per REGISTRY\'s governing `d1-1` row (ruled 2026-08-24, b145): Zenodo %s, published %s, DOI %s (concept %s), %d files.** The other two ledgers\' statements (VERIFICATION_LOOM.md\'s gate-1 pin, OPEN_TRAILS.md\'s deposit-voice pin) agree with the record and are CURRENT.'
          % (got['version'], got['date'], got['doi'], got['concept'], got['nfiles']),
          '',
          '*No deposit action is taken or implied by this block; nothing was written at Zenodo. Filed by b337 (relay `data/b337_the_housekeeping.txt`).*']
    return L


def main():
    rec('=' * 100)
    rec('b337 -- THE ERRATA PARTITION, ONE APPENDED BLOCK; ENTRIES UNMOVED; THE CURRENCY NOTE.')
    rec('=' * 100)
    fetch = json.load(io.open(os.path.join(D, 'b337_fetch.json'), encoding='utf-8'))
    before = io.open(ERR, encoding='utf-8', errors='replace').read()
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:ERRATA.md'], capture_output=True).stdout.decode('utf-8', 'replace')
    ids = entry_ids(before)
    listed = [e for e, _w in DEPOSIT_FACING] + [e for e, _w in INTERNAL_RECORD]
    rec('  entries in the file : %s' % ids)
    complete = sorted(ids) == sorted(listed) and len(listed) == len(set(listed))
    rec('  every entry in exactly one list : %s' % complete)
    if not complete:
        rec('  ### REFUSING TO WRITE -- the lists do not cover the entries exactly.')
        rec('=' * 100)
        return 1
    if MARK in before:
        rec('  ALREADY PRESENT -- nothing written (idempotent) ; mark once : %s' % (before.count(MARK) == 1))
        rec('=' * 100)
        return 0
    new = before.rstrip(chr(10)) + chr(10) + chr(10).join(block(fetch)) + chr(10)
    open(ERR + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(ERR + '.tmp', ERR)
    after = io.open(ERR, encoding='utf-8', errors='replace').read()
    pw = after.startswith(before.rstrip(chr(10)))
    pb = after.replace(chr(13) + chr(10), chr(10)).startswith(blob.replace(chr(13) + chr(10), chr(10)).rstrip(chr(10)))
    same_ids = entry_ids(after) == ids
    rec('  WRITTEN +%d lines ; working TRUE PREFIX %s ; blob TRUE PREFIX %s ; mark once %s ; entry headings unchanged %s'
        % (len(after.splitlines()) - len(before.splitlines()), pw, pb, after.count(MARK) == 1, same_ids))
    rec('=' * 100)
    return 0 if (pw and pb and after.count(MARK) == 1 and same_ids) else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    base = 'b337_errata_run' if wrote else 'b337_errata_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
