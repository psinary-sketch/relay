# -*- coding: utf-8 -*-
"""b756, (R366)(3)(i) to (v) and the ferry's Component 3: THE FIVE WRITES OF WHAT b755 FOUND, "in these words and no others, each by one
PLACE-papers commit through the one-call tool with its scan" (data/b756_ferry.txt :13), "each cut from this ruling's text and read against it
before the commit" (:51). Carried in form from tools/b755_l16.py (cut_line, append, controls, write, confirm): each text cut whole from the
ruling's line at relay HEAD between its opening quotation mark and its last, no quotation mark inside; written beside the text, the bytes
before the place kept whole and the bytes after it kept whole; read back; then `confirm <item>` after its PLACE-papers commit (HEAD touching
that file alone, the lines added and none removed, HEAD's blob equal to the composed bytes, and each written line at HEAD equal to a cut made
again from the ruling at relay HEAD).

THE PLACES, as (3) gives them:
  (i)   THE_EPSTEIN_CONTROL_OBJECT_v0_1.md: inserted after the note at :13 with a blank line, in the form of the five above it (:5, :7, :9,
        :11, :13 each a dated note, a blank line between); the lines after :13 move down by two, no line before it moves
  (ii)  SIMPLICITY_OF_RIEMANN_ZEROS.md, (iii) Which_Structure_Confines_v2_4_0.md, (iv) THE_FINDINGS_AS_THEY_STAND_v0_7.md: appended at the
        file's end after a blank line -- one blank line between the file's last text and the note: where the file ends with a blank line
        already (SIMPLICITY ends so), the note follows it and no second blank is added; otherwise a blank line, then the note
  (v)   OPEN_TRAILS.md: five lines [L17] to [L21] appended at the file's end under one dated head, after (1)(i)'s line (the file's last line,
        checked to be it) and before this act's own trail, a blank line before the head and before each line (b755's form), no line moving;
        each line closing "(the navigator's)": the ruling's quoted line, one space, then the closing words cut from (3)(v)'s own line (:18)
        between their quotation marks. The dated head is the seat's, naming the clause and the cite.

THE ORDER: (i) to (v), one at a time; a write is refused until the item before it is confirmed. The withheld kinds are tools/b754_doors.py's
(the account the clone's remote names, [Q] row (3)'s word read at run time, an identifier), none of them printed. PLACE-papers' place is read
from tools/b754_doors.py; this tool spells none. The bank carries digests and line numbers alone: no line of a paper is quoted in it.
MODES  controls | dry <item|all> | write <item> | confirm <item>      BANK data/b756_notes.json (written at write and at confirm)
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

ACT = 'b756'
PP = DOORS.PP
FERRY = 'data/b756_ferry.txt'
BANK = os.path.join(RELAY, 'data', '%s_notes.json' % ACT)
NL = '\n'
ORDER = ('i', 'ii', 'iii', 'iv', 'v')
ITEMS = {
    'i': {'fline': 14, 'starts': '(i) THE_EPSTEIN_CONTROL_OBJECT_v0_1.md, one dated note inserted after the note at :13',
          'rel': 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md', 'how': 'insert', 'after': 13,
          'opens': '*Dated note, 2026-11-15, b756: results banked at b755 that ', 'closes': ' The version stays v0.1.*'},
    'ii': {'fline': 15, 'starts': '(ii) SIMPLICITY_OF_RIEMANN_ZEROS.md, appended at the file\'s end after a blank line',
           'rel': 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'how': 'append',
           'opens': '*Dated note, 2026-11-15, b756, under the author’s ruling `(R366)`(3): three statements of this document',
           'closes': ' The next edition takes these up.*'},
    'iii': {'fline': 16, 'starts': '(iii) Which_Structure_Confines_v2_4_0.md, appended at the file\'s end after a blank line',
            'rel': 'day1/Which_Structure_Confines_v2_4_0.md', 'how': 'append',
            'opens': '*Dated note, 2026-11-15, b756, under the author’s ruling `(R366)`(3): the remark at :133',
            'closes': ' the next edition takes this up.*'},
    'iv': {'fline': 17, 'starts': '(iv) THE_FINDINGS_AS_THEY_STAND_v0_7.md, appended at the file\'s end after a blank line',
           'rel': 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', 'how': 'append',
           'opens': '*Dated note, 2026-11-15, b756, under the author’s ruling `(R366)`(3): :45 reads',
           'closes': ' the next edition takes this up.*'},
    'v': {'fline': 18, 'starts': '(v) OPEN_TRAILS, five lines appended at the file\'s end under one dated head',
          'rel': 'OPEN_TRAILS.md', 'how': 'trail', 'lines': (19, 20, 21, 22, 23), 'closing_needle': 'each closing "',
          'prior': '*Appended 2026-11-15 by b756 to b755'},
}
EPS_NOTE_LINES = (5, 7, 9, 11, 13)


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout


def gitb(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:16]


def ferry_at_head():
    rc, out = git(RELAY, 'show', 'HEAD:%s' % FERRY)
    L = out.replace('\r', '').split(NL)
    if rc or len(L) < 23:
        raise SystemExit('### %s NOT READ AT HEAD -- NOTHING DONE' % FERRY)
    return L


def quoted(s):
    """the text between a line's opening quotation mark and its last, refused where either is missing or one stands inside."""
    s = s.rstrip()
    if '"' not in s or not s.endswith('"'):
        raise SystemExit('### THE RULING`S LINE HAS NO CLOSING QUOTATION MARK -- NOTHING DONE')
    i, j = s.index('"'), s.rindex('"')
    t = s[i + 1:j]
    if i == j or not t or '"' in t:
        raise SystemExit('### THE CUT IS EMPTY OR CARRIES A QUOTATION MARK INSIDE -- NOTHING DONE')
    return t


def cut_note(L, k):
    """(i) to (iv): the one quoted note of the ruling's line, checked by its opening words and its closing words."""
    it = ITEMS[k]
    s = L[it['fline'] - 1]
    if not s.startswith(it['starts']):
        raise SystemExit('### THE RULING`S LINE :%d NOT AS READ -- NOTHING DONE' % it['fline'])
    t = quoted(s)
    if not t.startswith(it['opens']) or not t.endswith(it['closes']):
        raise SystemExit('### THE CUT OF (%s) DOES NOT OPEN AND CLOSE AS READ -- NOTHING DONE' % k)
    return t


def cut_trail(L):
    """(v): the closing words between their quotation marks on (3)(v)'s line, and the five quoted lines, each [L17] to [L21] in turn."""
    it = ITEMS['v']
    s = L[it['fline'] - 1]
    if not s.startswith(it['starts']) or it['closing_needle'] not in s:
        raise SystemExit('### THE RULING`S LINE :%d NOT AS READ -- NOTHING DONE' % it['fline'])
    a = s.index(it['closing_needle']) + len(it['closing_needle'])
    b = s.index('"', a)
    closing = s[a:b]
    if closing != "(the navigator's)":
        raise SystemExit('### THE CLOSING WORDS NOT AS READ -- NOTHING DONE')
    out = []
    for n, fl in zip(range(17, 22), it['lines']):
        t = quoted(L[fl - 1])
        if not L[fl - 1].startswith('"[L%d] ' % n) or not t.startswith('[L%d] ' % n):
            raise SystemExit('### THE RULING`S LINE :%d IS NOT [L%d] -- NOTHING DONE' % (fl, n))
        out.append(t)
    return closing, out


def eol_of(data):
    cr, crlf = data.count(b'\r'), data.count(b'\r\n')
    if cr == 0:
        return b'\n'
    if cr == crlf == data.count(b'\n'):
        return b'\r\n'
    raise SystemExit('### THE FILE MIXES LINE ENDINGS -- NOTHING WRITTEN')


def count_lines(data, eol):
    parts = data.split(eol)
    return len(parts) - (1 if parts[-1] == b'' else 0)


def check_lines(lines):
    for s in lines:
        if '\n' in s or '\r' in s:
            raise SystemExit('### A LINE CARRIES A LINE BREAK -- NOTHING WRITTEN')


def append_note(data, s):
    """one blank line between the file's last text and the note; returns (after, the note's line number)."""
    eol = eol_of(data)
    if not data.endswith(eol):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    check_lines([s])
    n0 = count_lines(data, eol)
    if data.endswith(eol + eol):
        return data + s.encode('utf-8') + eol, n0 + 1
    return data + eol + s.encode('utf-8') + eol, n0 + 2


def insert_note(data, s, after):
    """the note inserted after line `after` with a blank line, where that line and the four before it two apart are dated notes."""
    eol = eol_of(data)
    if not data.endswith(eol):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    check_lines([s])
    L = data.split(eol)[:-1]
    form = all(len(L) > x and L[x - 1].startswith(b'*Dated note, ') and L[x - 1].endswith(b'*') and L[x] == b'' for x in EPS_NOTE_LINES)
    if after != EPS_NOTE_LINES[-1] or not form or not L[after - 1].startswith(b'*Dated note, 2026-11-14, b754:'):
        raise SystemExit('### THE NOTE AT :%d AND THE FOUR ABOVE IT NOT IN THE FORM READ -- NOTHING WRITTEN' % after)
    head = eol.join(L[:after]) + eol
    after_b = head + eol + s.encode('utf-8') + eol + data[len(head):]
    return after_b, after + 2


def head_line(date, prior_at):
    return ('**Dated head, %s, b756, `(R366)`(3)(v): five lines for OPEN_TRAILS, the navigator\'s, in the ruling\'s words** (relay %s '
            ':18-:23), appended at the end of the file after `(R366)`(1)(i)\'s line (:%d) and before this act\'s own trail, so that no line '
            'of the trail moves. Each line below is quoted whole from the ruling and closes with the words (3)(v) gives it.' % (date, FERRY, prior_at))


def compose_trail(data, L, date):
    eol = eol_of(data)
    if not data.endswith(eol):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    lines_now = data.split(eol)[:-1]
    n0 = len(lines_now)
    if not lines_now[-1].decode('utf-8').startswith(ITEMS['v']['prior']):
        raise SystemExit('### THE FILE`S LAST LINE IS NOT (1)(i)`S -- NOTHING WRITTEN')
    closing, five = cut_trail(L)
    lines = [head_line(date, n0)] + ['%s %s' % (t, closing) for t in five]
    check_lines(lines)
    after = data + b''.join(eol + s.encode('utf-8') + eol for s in lines)
    nums = [n0 + 2 * (k + 1) for k in range(len(lines))]
    return after, lines, nums, five, closing


def compose(k, L, data, date):
    """(after, [(line number, text, the ruling's cut it carries)], lines added)."""
    it = ITEMS[k]
    eol = eol_of(data)
    n0 = count_lines(data, eol)
    if it['how'] == 'trail':
        after, lines, nums, five, closing = compose_trail(data, L, date)
        rows = [(nums[0], lines[0], None)] + [(n, s, t) for n, s, t in zip(nums[1:], lines[1:], five)]
    else:
        note = cut_note(L, k)
        after, at = insert_note(data, note, it['after']) if it['how'] == 'insert' else append_note(data, note)
        rows = [(at, note, note)]
    return after, rows, count_lines(after, eol) - n0


def kept_whole(k, data, after):
    """the bytes before the place a prefix of the bytes after, and (at the insert) the bytes after the place a suffix."""
    if ITEMS[k]['how'] != 'insert':
        return after.startswith(data)
    eol = eol_of(data)
    head = eol.join(data.split(eol)[:ITEMS[k]['after']]) + eol
    return after.startswith(head) and after.endswith(data[len(head):]) and len(after) > len(data)


def controls():
    acct, word = DOORS.account(PP), DOORS.q_word()
    L = ferry_at_head()
    out = []
    cuts = [cut_note(L, k) for k in ('i', 'ii', 'iii', 'iv')]
    closing, five = cut_trail(L)
    out.append(('the four notes cut from the ruling`s lines :14-:17, each opening and closing as read', len(cuts) == 4, True))
    out.append(('the closing words and [L17] to [L21] cut from :18-:23', closing == "(the navigator's)" and len(five) == 5, True))
    for name, bad in (('its closing quotation mark dropped', L[14].rstrip()[:-1]), ('a quotation mark planted inside', L[14][:-20] + '"' + L[14][-20:])):
        try:
            quoted(bad)
            refused = False
        except SystemExit:
            refused = True
        out.append(('the cut refused on (ii)`s line with %s (planted)' % name, refused, True))
    out.append(('the nine cuts and the closing words withheld by no kind',all(DOORS.withheld(t, acct, word) == [] for t in cuts + five + [closing]), True))
    out.append(('a planted copy carrying the account withheld', 'the account' in DOORS.withheld(cuts[0] + ' ' + (acct or 'x'), acct, word), True))
    try:
        append_note(b'no newline', 'x')
        refused = False
    except SystemExit:
        refused = True
    out.append(('the append refused on a file not ending with a newline (planted)', refused, True))
    out.append(('one blank line before an appended note, a blank already at the end or not (planted)',
                append_note(b'a\n', 'X') == (b'a\n\nX\n', 3) and append_note(b'a\n\n', 'X') == (b'a\n\nX\n', 3), True))
    try:
        eol_of(b'a\r\nb\n')
        refused = False
    except SystemExit:
        refused = True
    out.append(('a file mixing line endings refused (planted)', refused, True))
    plant = (b'h\n\n*v0.1*\n\n' + b''.join(b'*Dated note, 2026-11-0%d, x*\n\n' % n for n in range(1, 5))
             + b'*Dated note, 2026-11-14, b754: y*\n\n## 1\n')
    ins, at = insert_note(plant, 'N', 13)
    out.append(('the insert on a planted file in the form: the note at :15, the bytes before and after the place kept whole',
                at == 15 and ins.split(b'\n')[14] == b'N' and ins.split(b'\n')[13] == b'' and kept_whole('i', plant, ins), True))
    try:
        insert_note(plant.replace(b'2026-11-14, b754', b'2026-11-14, b75X'), 'N', 13)
        refused = False
    except SystemExit:
        refused = True
    out.append(('the insert refused where :13 is not b754`s note (planted)', refused, True))
    ok = all(a == b for _, a, b in out)
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    print('### CONTROLS %d OF %d AS WANTED ; the account and the word read at run time, neither printed' % (sum(1 for _, a, b in out if a == b), len(out)))
    return ok


def load():
    return json.load(open(BANK, encoding='utf-8')) if os.path.exists(BANK) else {'act': ACT, 'clause': '(R366)(3)(i)-(v)', 'items': {}}


def bank(R):
    tmp = BANK + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(R, indent=1, ensure_ascii=False) + NL)
    os.replace(tmp, BANK)


def show(k, rows, added, data, after, acct, word):
    it = ITEMS[k]
    print('  (%s) %s ; %d bytes before, %d after ; lines added %d ; the bytes before and after the place kept whole %s' % (
        k, it['rel'], len(data), len(after), added, kept_whole(k, data, after)))
    for n, s, t in rows:
        wh = DOORS.withheld(s, acct, word)
        print('    :%d digest %s, %d characters ; %s ; withheld by a kind: %s' % (
            n, digest(s), len(s), 'the seat`s dated head' if t is None else ('EQUAL to the ruling`s cut' if s == t else
                                                                          'the ruling`s cut and its closing words' if s.startswith(t + ' ') else 'NOT THE CUT'), wh or 'none'))
        print('      %s' % s)


def item_arg(argv):
    k = argv[1] if len(argv) > 1 else ''
    if k not in ORDER and not (argv[0] == 'dry' and k == 'all'):
        sys.exit(__doc__)
    return k


def main(argv):
    step = argv[0] if argv else ''
    if step == 'controls':
        return 0 if controls() else 1
    if step not in ('dry', 'write', 'confirm'):
        sys.exit(__doc__)
    k = item_arg(argv)
    acct, word = DOORS.account(PP), DOORS.q_word()
    L = ferry_at_head()
    if step == 'confirm':
        R = load()
        e = R['items'].get(k)
        if not e or e.get('confirm'):
            raise SystemExit('### (%s) NOT WRITTEN, OR CONFIRMED ALREADY -- NOTHING DONE' % k)
        rel = ITEMS[k]['rel']
        _, head = git(PP, 'rev-parse', 'HEAD')
        _, files = git(PP, 'show', '--format=', '--name-only', 'HEAD')
        _, num = git(PP, 'show', '--format=', '--numstat', 'HEAD')
        _, blob = gitb(PP, 'show', 'HEAD:%s' % rel)
        O = blob.decode('utf-8').replace('\r', '').split(NL)
        if k == 'v':
            closing, five = cut_trail(L)
            want = [None] + ['%s %s' % (t, closing) for t in five]
        else:
            want = [cut_note(L, k)]
        have = [len(O) >= x['line'] and digest(O[x['line'] - 1]) == x['digest'] and (w is None or O[x['line'] - 1] == w)
                for x, w in zip(e['lines'], want)]
        ok = (files.strip() == rel and num.split()[:2] == [str(e['added']), '0'] and bdigest(blob) == e['sha_after']
              and all(have) and head.strip() != e['pp_head'])
        print('### (%s) CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s (wanted %d 0) ; HEAD`s blob the composed bytes %s ; '
              'each line at HEAD the ruling`s cut made again %s ; %s' % (k, head.strip()[:8], files.strip(), num.split()[:2], e['added'],
                                                                      bdigest(blob) == e['sha_after'], have, 'AS WANTED' if ok else 'NOT AS WANTED'))
        if not ok:
            raise SystemExit('### THE COMMIT DOES NOT CARRY (%s) AS COMPOSED -- NOTHING WRITTEN' % k)
        e['confirm'] = 'PLACE-papers %s at %s, %s alone, %d lines added, none removed' % (head.strip()[:8], stamp(), rel, e['added'])
        bank(R)
        return 0
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    _, head = git(PP, 'rev-parse', 'HEAD')
    staged = subprocess.run(['git', '-C', PP, 'diff', '--cached', '--quiet']).returncode == 0
    date = stamp()[:10]
    todo = ORDER if k == 'all' else (k,)
    if step == 'write':
        R = load()
        i = ORDER.index(k)
        if k in R['items']:
            raise SystemExit('### (%s) WRITTEN ALREADY -- NOTHING DONE' % k)
        if i and not (R['items'].get(ORDER[i - 1]) or {}).get('confirm'):
            raise SystemExit('### (%s) NOT CONFIRMED -- (%s) WAITS FOR IT -- NOTHING DONE' % (ORDER[i - 1], k))
    print('  PLACE-papers HEAD %s ; nothing staged %s ; the date %s' % (head.strip()[:8], staged, date))
    for q in todo:
        rel = ITEMS[q]['rel']
        path = os.path.join(PP, rel)
        clean = subprocess.run(['git', '-C', PP, 'diff', '--quiet', 'HEAD', '--', rel]).returncode == 0
        data = open(path, 'rb').read()
        present = (b'[L17]' in data) if q == 'v' else (b'*Dated note, 2026-11-15, b756' in data)
        after, rows, added = compose(q, L, data, date)
        print('  (%s) clean against HEAD %s ; written already %s' % (q, clean, present))
        show(q, rows, added, data, after, acct, word)
        wh = [w for _, s, _ in rows for w in DOORS.withheld(s, acct, word)]
        bad = not clean or present or wh or not kept_whole(q, data, after) or not staged
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
        print('  WRITTEN %s at %s ; read back %s' % (rel, at, 'EQUAL to the composed' if back == after else 'DIFFERS'))
        if back != after:
            raise SystemExit('### THE READ-BACK DIFFERS -- restore %s through the one-call tool' % rel)
        R['items'][q] = {'file': rel, 'source': '%s :%s at relay HEAD' % (FERRY, ITEMS[q]['fline'] if q != 'v' else '18-23'),
                         'how': ITEMS[q]['how'], 'pp_head': head.strip(), 'written_at': at, 'added': added,
                         'count_before': count_lines(data, eol_of(data)), 'count_after': count_lines(after, eol_of(after)),
                         'sha_before': bdigest(data), 'sha_after': bdigest(after),
                         'lines': [{'line': n, 'digest': digest(s), 'chars': len(s), 'kind': 'head' if t is None else 'the ruling`s text'}
                                   for n, s, t in rows], 'confirm': None}
        bank(R)
        print('  then: `commit.py pp add %s`, its commit, then `tools/b756_notes.py confirm %s`' % (rel, q))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
