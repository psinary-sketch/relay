# -*- coding: utf-8 -*-
"""b755, (R365)(7): ONE LINE FOR OPEN_TRAILS -- "on the author's word of 2026-11-14, appended at the file's end under a dated head before this
act's own trail, by one PLACE-papers commit, no line moving" (data/b755_ferry.txt :28). Carried in form from tools/b754_sitting.py's [L] route
(l_append, l_confirm, :777-:932): the line cut whole from the ruling's line at relay HEAD by its two needles, the opening quote after "no line
moving: " and the line's last quote; the dated head the seat's, naming the clause and the cite; a blank line before each of the two; the bytes
before a prefix of the bytes after; read back; then `confirm` after the PLACE-papers commit (HEAD touching OPEN_TRAILS.md alone, 4 lines added
and none removed, the two lines at their numbers). The withheld kinds are tools/b754_doors.py's (the account the clone's remote names, [Q] row
(3)'s word read at run time, an identifier), none of them printed. PLACE-papers' place is read from tools/b754_doors.py; this tool spells none.
MODES  controls | dry | write | confirm     BANK data/b755_l16.json (written at write and at confirm)
"""
import hashlib
import json
import os
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
import b754_doors as DOORS   # noqa: E402

ACT = 'b755'
PP = DOORS.PP
OREL = 'OPEN_TRAILS.md'
OPATH = os.path.join(PP, OREL)
FERRY, FERRY_LINE = 'data/b755_ferry.txt', 28
OPEN_NEEDLE = 'no line moving: "'
BANK = os.path.join(RELAY, 'data', '%s_l16.json' % ACT)
NL = '\n'


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:16]


def count_lines(data):
    parts = data.split(b'\n')
    return len(parts) - (1 if parts[-1] == b'' else 0)


def cut_line(s):
    """the quoted line of (7), cut whole from the ruling's line s; refused where a needle is missing or the cut is not the [L16] line."""
    if not s.startswith('(7) ONE LINE FOR OPEN_TRAILS') or OPEN_NEEDLE not in s or not s.rstrip().endswith('"'):
        raise SystemExit('### THE RULING`S LINE (7) NOT AS READ -- NOTHING DONE')
    i = s.index(OPEN_NEEDLE) + len(OPEN_NEEDLE)
    j = s.rstrip().rindex('"')
    line = s[i:j]
    if not line.startswith('[L16] ') or '"' in line:
        raise SystemExit('### THE CUT IS NOT THE [L16] LINE -- NOTHING DONE')
    return line


def ruling_line():
    rc, out = git(RELAY, 'show', 'HEAD:%s' % FERRY)
    L = out.replace('\r', '').split(NL)
    if rc or len(L) < FERRY_LINE:
        raise SystemExit('### %s NOT READ AT HEAD -- NOTHING DONE' % FERRY)
    return L[FERRY_LINE - 1]


def head_line(date):
    return ('**Dated head, %s, b755, `(R365)`(7): the line for OPEN_TRAILS on the author\'s word of 2026-11-14** (relay %s :%d), appended at '
            'the end of the file before this act\'s own trail, so that no line of the trail moves. The line below is quoted whole from the '
            'ruling.' % (date, FERRY, FERRY_LINE))


def append(data, lines):
    if not data.endswith(b'\n'):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    eol = b'\r\n' if data.endswith(b'\r\n') else b'\n'
    for s in lines:
        if '\n' in s or '\r' in s:
            raise SystemExit('### A LINE CARRIES A LINE BREAK -- NOTHING WRITTEN')
    return data + b''.join(eol + s.encode('utf-8') + eol for s in lines)


def controls():
    acct, word = DOORS.account(PP), DOORS.q_word()
    line = cut_line(ruling_line())
    out = []
    out.append(('the cut from the ruling`s line', line.startswith('[L16] Pattern grade') and line.endswith('(relay data/b755_registrations.txt).'), True))
    try:
        cut_line(ruling_line().rstrip()[:-1])
        refused = False
    except SystemExit:
        refused = True
    out.append(('the cut refused on the line with its closing quote dropped (planted)', refused, True))
    out.append(('the line withheld by no kind', DOORS.withheld(line, acct, word) == [], True))
    out.append(('a planted copy carrying the account withheld', 'the account' in DOORS.withheld(line + ' ' + (acct or 'x'), acct, word), True))
    try:
        append(b'no newline', ['x'])
        refused = False
    except SystemExit:
        refused = True
    out.append(('the append refused on a file not ending with a newline (planted)', refused, True))
    ok = all(a == b for _, a, b in out)
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    print('### CONTROLS %d OF %d AS WANTED ; the account and the word read at run time, neither printed' % (sum(1 for _, a, b in out if a == b), len(out)))
    return ok


def bank(R):
    tmp = BANK + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(R, indent=1, ensure_ascii=False) + NL)
    os.replace(tmp, BANK)


def main(argv):
    step = argv[0] if argv else ''
    if step == 'controls':
        return 0 if controls() else 1
    if step == 'confirm':
        R = json.load(open(BANK, encoding='utf-8'))
        if R.get('confirm'):
            raise SystemExit('### CONFIRMED ALREADY -- NOTHING DONE')
        _, head = git(PP, 'rev-parse', 'HEAD')
        _, files = git(PP, 'show', '--format=', '--name-only', 'HEAD')
        _, num = git(PP, 'show', '--format=', '--numstat', 'HEAD')
        _, blob = git(PP, 'show', 'HEAD:%s' % OREL)
        O = blob.replace('\r', '').split(NL)
        have = [len(O) >= x['line'] and digest(O[x['line'] - 1]) == x['digest'] for x in R['lines']]
        ok = files.strip() == OREL and num.split()[:2] == ['4', '0'] and all(have) and head.strip() != R['pp_head']
        print('### [L16] CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s ; the two lines at HEAD %s ; %s' % (
            head.strip()[:8], files.strip(), num.split()[:2], have, 'AS WANTED' if ok else 'NOT AS WANTED'))
        if not ok:
            raise SystemExit('### THE COMMIT DOES NOT CARRY THE LINE -- NOTHING WRITTEN')
        R['confirm'] = 'PLACE-papers %s at %s, OPEN_TRAILS.md alone, 4 lines appended, none removed' % (head.strip()[:8], stamp())
        bank(R)
        return 0
    if step not in ('dry', 'write'):
        sys.exit(__doc__)
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if os.path.exists(BANK):
        raise SystemExit('### THE BANK STANDS ALREADY (the line written once) -- NOTHING DONE')
    acct, word = DOORS.account(PP), DOORS.q_word()
    line = cut_line(ruling_line())
    _, head = git(PP, 'rev-parse', 'HEAD')
    clean = subprocess.run(['git', '-C', PP, 'diff', '--quiet', 'HEAD', '--', OREL]).returncode == 0
    data = open(OPATH, 'rb').read()
    n0 = count_lines(data)
    present = b'[L16]' in data
    date = stamp()[:10]
    lines = [head_line(date), line]
    wh = [k for s in lines for k in DOORS.withheld(s, acct, word)]
    print('  PLACE-papers HEAD %s ; %s clean against HEAD %s ; %d bytes, %d lines ; an [L16] already in the file %s' % (
        head.strip()[:8], OREL, clean, len(data), n0, present))
    print('  the line cut from relay %s :%d at HEAD: %d characters, digest %s ; withheld by a kind: %s' % (
        FERRY, FERRY_LINE, len(line), digest(line), wh or 'none'))
    if not clean or present or wh:
        raise SystemExit('### %s -- NOTHING WRITTEN' % ('NOT CLEAN' if not clean else 'AN [L16] STANDS' if present else 'A LINE WITHHELD'))
    after = append(data, lines)
    n1 = count_lines(after)
    nums = [n0 + 2, n0 + 4]
    print('  THE LINE COUNT: before %d ; after %d ; appended %d (a blank before each) ; the bytes before a prefix of the bytes after %s' % (
        n0, n1, n1 - n0, after.startswith(data)))
    for k, s in zip(nums, lines):
        print('  :%d digest %s, %d characters: %s' % (k, digest(s), len(s), s))
    if n1 != n0 + 4 or not after.startswith(data):
        raise SystemExit('### THE APPEND NOT AS COMPOSED -- NOTHING WRITTEN')
    if step == 'dry':
        print('  DRY: nothing written')
        return 0
    at = stamp()
    with open(OPATH + '.tmp', 'wb') as f:
        f.write(after)
    os.replace(OPATH + '.tmp', OPATH)
    back = open(OPATH, 'rb').read()
    print('  WRITTEN %s at %s ; read back %s' % (OREL, at, 'EQUAL to the composed' if back == after else 'DIFFERS'))
    if back != after:
        raise SystemExit('### THE READ-BACK DIFFERS -- restore OPEN_TRAILS.md through the one-call tool')
    bank({'act': ACT, 'clause': '(R365)(7)', 'source': '%s :%d at relay HEAD' % (FERRY, FERRY_LINE), 'pp_head': head.strip(), 'written_at': at,
          'count_before': n0, 'count_after': n1, 'sha_before': bdigest(data), 'sha_after': bdigest(after),
          'lines': [{'item': t, 'line': k, 'digest': digest(s), 'chars': len(s)} for t, k, s in zip(('head', '[L16]'), nums, lines)],
          'confirm': None})
    print('  then: `commit.py pp add OPEN_TRAILS.md`, its commit, then `tools/b755_l16.py confirm`')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
