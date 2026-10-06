# -*- coding: utf-8 -*-
"""test_record_findings_b632.py -- THE TEST OF THE RECORD TOOL'S FINDINGS WRITER, RESTORED AT b632 UNDER (R242)(2).

### The writer (tools/b632_record.py `findings`) is pointed at a SCRATCH COPY of PLACE-papers FINDINGS.md in a fresh temporary
### directory, its banks routed there too; it writes one entry and the entry is read back. The live ledger and relay data/ are read
### before and after and must not move.
###   (1) the copy after the write starts with the copy's bytes before it (append only);
###   (2) the bytes added are the entry's own, as the guarded appender writes it;
###   (3) the writer's bank names the entry's line, and that line holds the title: the copy's line count before + 2;
###   (4) a second write of the same entry is refused (the title stands) and the copy does not move;
###   (5) THE NEGATIVE CONTROL: an entry carrying one of the scanner's stems is refused and the copy does not move;
###   (6) the live FINDINGS.md and relay data/b632_findings.json are untouched by the test.
### Usage: python tools/test_record_findings_b632.py
"""
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b632_record as R   # noqa: E402

NL = chr(10)
LIVE = os.path.join(R.PP, 'FINDINGS.md')
LIVE_BANK = os.path.join(ROOT, 'data', 'b632_findings.json')
TITLE = '## A test entry of the restored findings writer, written to a scratch copy and read back'
BODY = ('*Written by tools/test_record_findings_b632.py to a scratch copy of the ledger; the live ledger is not written.* One '
        'paragraph of plain text, no table cell and no grade word, to be read back byte for byte.')


def digest(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def run_writer(entry):
    """### the writer once, against the scratch copy; RETURN its exit (None when it returned, the SystemExit's code otherwise)."""
    R._finding_text = lambda: (entry[1], entry[0])
    try:
        R.findings()
        return None
    except SystemExit as e:
        return e.code


def main():
    res = []
    live0, bank0 = digest(LIVE), digest(LIVE_BANK)
    tmp = tempfile.mkdtemp(prefix='b632_findings_test_', dir=os.path.splitdrive(R.PP)[0] + '/')   # ### the appender's relpath wants one drive
    copy = os.path.join(tmp, 'FINDINGS.md')
    shutil.copy(LIVE, copy)
    Q = R.R2._Q()
    find0, d0, dry0, ft0 = Q.FIND, R.D, R.DRY, R._finding_text
    Q.FIND, R.D, R.DRY = copy, tmp, False
    try:
        before = open(copy, 'rb').read()
        n_before = len(R.lines_of(before.decode('utf-8').replace(chr(13), '')))
        entry = (NL + TITLE + NL + NL + BODY + NL, TITLE)
        rc = run_writer(entry)
        after = open(copy, 'rb').read()
        res.append(('(1) the writer returned (exit %s) and the copy after the write starts with the copy before it' % rc,
                    rc is None and after.startswith(before) and len(after) > len(before)))
        want = Q.poss(entry[0]).encode('utf-8')
        if not before.endswith(b'\n'):
            want = b'\n' + want
        res.append(('(2) the bytes added (%d) are the entry`s own as the guarded appender writes it' % (len(after) - len(before)),
                    after[len(before):] == want))
        bank = json.load(io.open(os.path.join(tmp, 'b632_findings.json'), encoding='utf-8')) if os.path.exists(os.path.join(tmp, 'b632_findings.json')) else {}
        ls = after.decode('utf-8').replace(chr(13), '').split(NL)
        el = bank.get('entry_line')
        res.append(('(3) the bank names line %s; it holds the title; the copy`s line count before + 2 = %d' % (el, n_before + 2),
                    el == n_before + 2 and ls[el - 1] == TITLE if el else False))
        rc4 = run_writer(entry)
        res.append(('(4) a second write of the same entry is refused (exit %r) and the copy does not move' % (str(rc4)[:60],),
                    rc4 is not None and open(copy, 'rb').read() == after))
        stem = 'g' + 'ap'
        bad = (NL + '## A planted entry of the test, refused' + NL + NL + 'It names a %s, one of the scanner`s stems.' % stem + NL,
               '## A planted entry of the test, refused')
        rc5 = run_writer(bad)
        res.append(('(5) the negative control: an entry carrying a stem is refused (exit %r) and the copy does not move' % (str(rc5)[:60],),
                    rc5 is not None and open(copy, 'rb').read() == after))
    finally:
        Q.FIND, R.D, R.DRY, R._finding_text = find0, d0, dry0, ft0
        shutil.rmtree(tmp, ignore_errors=True)
    res.append(('(6) the live FINDINGS.md and relay data/b632_findings.json untouched by the test',
                digest(LIVE) == live0 and digest(LIVE_BANK) == bank0))
    for name, ok in res:
        print('  %-120s %s' % (name, 'PASS' if ok else 'FAIL'))
    ok = all(x for _n, x in res)
    print('### %s' % ('ALL PASS' if ok else 'NOT ALL PASS'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
