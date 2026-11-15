# -*- coding: utf-8 -*-
"""b756, (R366)(5)(ii) and (iii) on the author's pass at the put (data/b756_put_1.json; data/b756_author_answers.txt): THE WRITES THE ANSWERS
ORDER. Carried in form from tools/b756_notes.py (cut, append, controls, write, confirm), each by one PLACE-papers commit through the one-call
tool with its scan:
  cp           OPEN_TRAILS.md: the two checkpoint lines, CP-7 and CP-6, each cut whole from the ruling's line (5) at relay HEAD
               (data/b756_ferry.txt :28) between its quotation marks -- the line's only two quoted spans, each checked by its opening words --
               appended at the file's end under one dated head (the seat's, naming the clause, the ruling's line and the answer's line),
               a blank line before the head and before each line, no line moving; passed "Pass both" at PROMPT 2
  instruments  phase1.5/method/INSTRUMENTS.md: I-110 and I-111 appended at the file's end as drafted, the draft's lines :8-:16 at relay HEAD
               (data/b756_instruments_draft.txt, committed at f56557dd) taken whole, a blank line before them, each row's lines as the draft
               spaces them; passed "Pass both" at PROMPT 3; refused where the file holds an I-110 or I-111 already or its last entry is not I-109
THE ORDER: cp, then instruments; a write is refused until the item before it is confirmed. The withheld kinds are tools/b754_doors.py's
(the account the clone's remote names, [Q] row (3)'s word read at run time, an identifier), none printed. PLACE-papers' place is read from
tools/b754_doors.py. The bank carries digests and line numbers alone.
MODES  controls | dry <item|all> | write <item> | confirm <item>      BANK data/b756_passed.json (written at write and at confirm)
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
import b754_doors as DOORS   # noqa: E402

ACT = 'b756'
PP = DOORS.PP
FERRY, FLINE = 'data/b756_ferry.txt', 28
DRAFT, DRAFT_LINES = 'data/b756_instruments_draft.txt', (8, 16)
ANSWERS = 'data/b756_author_answers.txt'
BANK = os.path.join(RELAY, 'data', '%s_passed.json' % ACT)
NL = '\n'
ORDER = ('cp', 'instruments')
REL = {'cp': 'OPEN_TRAILS.md', 'instruments': 'phase1.5/method/INSTRUMENTS.md'}
CP_OPENS = ('CP-7 closed by this line, on the author’s word: its editions ran from b576 to b599', 'CP-6, the Phase 2 inheritance, was not run')


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:16]


def relay_head_lines(path):
    rc, out = git(RELAY, 'show', 'HEAD:%s' % path)
    if rc:
        raise SystemExit('### %s NOT READ AT RELAY HEAD -- NOTHING DONE' % path)
    return out.decode('utf-8').replace('\r', '').split(NL)


def cut_cp(s):
    """the two quoted spans of the ruling's line (5), each opening as read; refused otherwise."""
    if not s.startswith('(5) THE TWELVE READY ORDERS AND THE TWO CHECKPOINTS') or '(ii) TWO LINES FOR OPEN_TRAILS, passed or struck: "' not in s:
        raise SystemExit('### THE RULING`S LINE (5) NOT AS READ -- NOTHING DONE')
    q = re.findall(r'"([^"]*)"', s)
    if len(q) != 2 or s.count('"') != 4 or not all(x.startswith(o) for x, o in zip(q, CP_OPENS)):
        raise SystemExit('### THE TWO CHECKPOINT LINES NOT CUT AS READ (%d spans) -- NOTHING DONE' % len(q))
    return q


def answer_line(n, label):
    A = relay_head_lines(ANSWERS)
    k = next((i for i, l in enumerate(A, 1) if l.startswith('### PROMPT %d (' % n)), None)
    r = next((i for i, l in enumerate(A, 1) if l.startswith('RESULT (')), None)
    if not k or not r or ('"="%s"' % label) not in A[r - 1].replace('"=\'', '"="'):
        raise SystemExit('### THE ANSWER TO PROMPT %d NOT READ AS "%s" AT RELAY HEAD -- NOTHING DONE' % (n, label))
    return k, r


def eol_of(data):
    cr, crlf = data.count(b'\r'), data.count(b'\r\n')
    if cr == 0:
        return b'\n'
    if cr == crlf == data.count(b'\n'):
        return b'\r\n'
    raise SystemExit('### THE FILE MIXES LINE ENDINGS -- NOTHING WRITTEN')


def check_lines(lines):
    for s in lines:
        if '\n' in s or '\r' in s:
            raise SystemExit('### A LINE CARRIES A LINE BREAK -- NOTHING WRITTEN')


def head_cp(date, k, r):
    return ('**Dated head, %s, b756, `(R366)`(5)(ii): the two checkpoint lines, passed by the author at the put** (relay %s :%d; '
            '%s :%d, :%d), appended at the end of the file before this act\'s own trail, so that no line of the trail moves. Each line '
            'below is quoted whole from the ruling.' % (date, FERRY, FLINE, ANSWERS, k, r))


def compose(item, data, date):
    """(after, [(line number, text, the source text it carries or None for the seat's head)], lines added)."""
    eol = eol_of(data)
    if not data.endswith(eol):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    L = data.split(eol)[:-1]
    n0 = len(L)
    if item == 'cp':
        two = cut_cp(relay_head_lines(FERRY)[FLINE - 1])
        k, r = answer_line(2, 'Pass both (Recommended)')
        lines = [head_cp(date, k, r)] + two
        check_lines(lines)
        after = data + b''.join(eol + s.encode('utf-8') + eol for s in lines)
        rows = [(n0 + 2, lines[0], None), (n0 + 4, two[0], two[0]), (n0 + 6, two[1], two[1])]
        return after, rows, 6
    answer_line(3, 'Pass both (Recommended)')
    D = relay_head_lines(DRAFT)
    blk = D[DRAFT_LINES[0] - 1:DRAFT_LINES[1]]
    if not (blk[0].startswith('## I-110 — ') and blk[4].startswith('## I-111 — ') and blk[8].startswith('*Entered ') and blk[1] == blk[3] == blk[5] == blk[7] == ''):
        raise SystemExit('### THE DRAFT`S LINES :%d-:%d NOT AS DRAFTED -- NOTHING WRITTEN' % DRAFT_LINES)
    heads = [l for l in L if re.match(r'^## I-\d+ ', l.decode('utf-8'))]
    if not heads or not heads[-1].decode('utf-8').startswith('## I-109 ') or any(re.match(r'^## I-11[01] ', h.decode('utf-8')) for h in heads):
        raise SystemExit('### INSTRUMENTS` LAST ENTRY IS NOT I-109, OR AN I-110/I-111 STANDS -- NOTHING WRITTEN')
    check_lines(blk)
    after = data + eol + eol.join(s.encode('utf-8') for s in blk) + eol
    rows = [(n0 + 2 + i, s, s) for i, s in enumerate(blk) if s]
    return after, rows, 1 + len(blk)


def controls():
    acct, word = DOORS.account(PP), DOORS.q_word()
    out = []
    F = relay_head_lines(FERRY)
    two = cut_cp(F[FLINE - 1])
    out.append(('the two checkpoint lines cut from the ruling`s line :28, each opening as read', len(two) == 2, True))
    try:
        cut_cp(F[FLINE - 1].replace('"CP-6', '"CQ-6'))
        refused = False
    except SystemExit:
        refused = True
    out.append(('the cut refused where a line does not open as read (planted)', refused, True))
    try:
        cut_cp(F[FLINE - 1] + ' "planted"')
        refused = False
    except SystemExit:
        refused = True
    out.append(('the cut refused on a third quoted span (planted)', refused, True))
    D = relay_head_lines(DRAFT)
    blk = D[DRAFT_LINES[0] - 1:DRAFT_LINES[1]]
    out.append(('the draft`s lines :8-:16 at relay HEAD: I-110, I-111 and the closing line, blank lines between', blk[0].startswith('## I-110 — ')
                and blk[4].startswith('## I-111 — ') and blk[8].startswith('*Entered '), True))
    out.append(('the answers at relay HEAD: PROMPT 2 and PROMPT 3 passed "Pass both"', bool(answer_line(2, 'Pass both (Recommended)')) and bool(answer_line(3, 'Pass both (Recommended)')), True))
    out.append(('every line withheld by no kind', all(DOORS.withheld(t, acct, word) == [] for t in two + [b for b in blk if b]), True))
    out.append(('a planted copy carrying the account withheld', 'the account' in DOORS.withheld(two[0] + ' ' + (acct or 'x'), acct, word), True))
    try:
        compose('cp', b'no newline', '2026-11-15')
        refused = False
    except SystemExit:
        refused = True
    out.append(('the append refused on a file not ending with a newline (planted)', refused, True))
    try:
        compose('instruments', b'## I-109 x\n\n## I-110 y\n', '2026-11-15')
        refused = False
    except SystemExit:
        refused = True
    out.append(('the instruments write refused where an I-110 stands (planted)', refused, True))
    ok = all(a == b for _, a, b in out)
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    print('### CONTROLS %d OF %d AS WANTED ; the account and the word read at run time, neither printed' % (sum(1 for _, a, b in out if a == b), len(out)))
    return ok


def load():
    return json.load(open(BANK, encoding='utf-8')) if os.path.exists(BANK) else {'act': ACT, 'clause': '(R366)(5)(ii), (iii) on the author`s pass', 'items': {}}


def bank(R):
    tmp = BANK + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(R, indent=1, ensure_ascii=False) + NL)
    os.replace(tmp, BANK)


def main(argv):
    step = argv[0] if argv else ''
    if step == 'controls':
        return 0 if controls() else 1
    if step not in ('dry', 'write', 'confirm'):
        sys.exit(__doc__)
    k = argv[1] if len(argv) > 1 else ''
    if k not in ORDER and not (step == 'dry' and k == 'all'):
        sys.exit(__doc__)
    acct, word = DOORS.account(PP), DOORS.q_word()
    if step == 'confirm':
        R = load()
        e = R['items'].get(k)
        if not e or e.get('confirm'):
            raise SystemExit('### (%s) NOT WRITTEN, OR CONFIRMED ALREADY -- NOTHING DONE' % k)
        _, head = git(PP, 'rev-parse', 'HEAD')
        _, files = git(PP, 'show', '--format=', '--name-only', 'HEAD')
        _, num = git(PP, 'show', '--format=', '--numstat', 'HEAD')
        _, blob = git(PP, 'show', 'HEAD:%s' % REL[k])
        O = blob.decode('utf-8').replace('\r', '').split(NL)
        have = [len(O) >= x['line'] and digest(O[x['line'] - 1]) == x['digest'] for x in e['lines']]
        head, files, num = head.decode().strip(), files.decode().strip(), num.decode().split()
        ok = files == REL[k] and num[:2] == [str(e['added']), '0'] and bdigest(blob) == e['sha_after'] and all(have) and head != e['pp_head']
        print('### (%s) CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s (wanted %d 0) ; HEAD`s blob the composed bytes %s ; each line at '
              'HEAD %s ; %s' % (k, head[:8], files, num[:2], e['added'], bdigest(blob) == e['sha_after'], have, 'AS WANTED' if ok else 'NOT AS WANTED'))
        if not ok:
            raise SystemExit('### THE COMMIT DOES NOT CARRY (%s) AS COMPOSED -- NOTHING WRITTEN' % k)
        e['confirm'] = 'PLACE-papers %s at %s, %s alone, %d lines added, none removed' % (head[:8], stamp(), REL[k], e['added'])
        bank(R)
        return 0
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    _, head = git(PP, 'rev-parse', 'HEAD')
    head = head.decode().strip()
    staged = subprocess.run(['git', '-C', PP, 'diff', '--cached', '--quiet']).returncode == 0
    date = stamp()[:10]
    R = load()
    if step == 'write':
        i = ORDER.index(k)
        if k in R['items']:
            raise SystemExit('### (%s) WRITTEN ALREADY -- NOTHING DONE' % k)
        if i and not (R['items'].get(ORDER[i - 1]) or {}).get('confirm'):
            raise SystemExit('### (%s) NOT CONFIRMED -- (%s) WAITS FOR IT -- NOTHING DONE' % (ORDER[i - 1], k))
    print('  PLACE-papers HEAD %s ; nothing staged %s ; the date %s' % (head[:8], staged, date))
    for q in (ORDER if k == 'all' else (k,)):
        path = os.path.join(PP, REL[q])
        clean = subprocess.run(['git', '-C', PP, 'diff', '--quiet', 'HEAD', '--', REL[q]]).returncode == 0
        data = open(path, 'rb').read()
        present = (b'CP-7 closed by this line' in data) if q == 'cp' else (b'## I-110 ' in data)
        after, rows, added = compose(q, data, date)
        kept = after.startswith(data)
        wh = [w for _, s, _ in rows for w in DOORS.withheld(s, acct, word)]
        print('  (%s) %s ; clean against HEAD %s ; written already %s ; %d bytes before, %d after ; lines added %d ; the bytes before a prefix %s ; '
              'withheld %s' % (q, REL[q], clean, present, len(data), len(after), added, kept, wh or 'none'))
        for n, s, t in rows:
            print('    :%d digest %s, %d characters ; %s' % (n, digest(s), len(s), 'the seat`s dated head' if t is None else 'EQUAL to its source'
                                                               if s == t else 'NOT ITS SOURCE'))
            print('      %s' % s[:400])
        bad = not clean or present or wh or not kept or not staged
        if step == 'dry':
            print('  (%s) DRY: nothing written%s' % (q, ' ; WOULD BE REFUSED' if bad else ''))
            continue
        if bad:
            raise SystemExit('### (%s) NOT CLEAN, WRITTEN ALREADY, WITHHELD, NOT KEPT WHOLE OR SOMETHING STAGED -- NOTHING WRITTEN' % q)
        at = stamp()
        with open(path + '.tmp', 'wb') as f:
            f.write(after)
        os.replace(path + '.tmp', path)
        back = open(path, 'rb').read()
        print('  WRITTEN %s at %s ; read back %s' % (REL[q], at, 'EQUAL to the composed' if back == after else 'DIFFERS'))
        if back != after:
            raise SystemExit('### THE READ-BACK DIFFERS -- restore %s through the one-call tool' % REL[q])
        R['items'][q] = {'file': REL[q], 'source': '%s :%d' % (FERRY, FLINE) if q == 'cp' else '%s :%d-:%d' % ((DRAFT,) + DRAFT_LINES),
                         'pp_head': head, 'written_at': at, 'added': added, 'sha_before': bdigest(data), 'sha_after': bdigest(after),
                         'lines': [{'line': n, 'digest': digest(s), 'chars': len(s), 'kind': 'head' if t is None else 'the source`s text'} for n, s, t in rows],
                         'confirm': None}
        bank(R)
        print('  then: `commit.py pp add %s`, its commit, then `tools/b756_passed.py confirm %s`' % (REL[q], q))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
