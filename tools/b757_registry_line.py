# -*- coding: utf-8 -*-
"""b757 -- (R367)(8)(iv): REGISTRY'S HEADER AT :13 REPLACED IN PLACE, NO LINE MOVING.

The ruling's words (data/b757_ferry.txt :25): "REGISTRY's header at :13, which reads 2026-08-24, is replaced in place, no line moving, by:
"**Last updated:** **<the commit's UTC date>** (b757, under the author's ruling `(R367)`(8)(iv): this line brought to the date of the
ledger's latest dated note; the dated notes at the ledger's end are the record of each change since b145). *Prior line, retained:* "
followed by the prior line whole from its opening "2026-08-24" to its end."

The new head is cut at run time from the ferry bank (the quoted text after "is replaced in place, no line moving, by:"), its one field filled
with the UTC date of the run, the commit following in the same hour; the retained text is the prior line from its first "2026-08-24" to its
end, cut as the ruling words it (the bold marks after that date kept as they stand). Bytes read and written whole: the line's own ending kept,
every other line equal byte for byte, the line count equal. The controls first: the cut on the line as it stands, and two plants -- a line
13 not opening "**Last updated:**" refused; a line 13 with no "2026-08-24" refused.

usage: python -X utf8 -u tools/b757_registry_line.py dry|write
"""
import datetime
import hashlib
import io
import os
import re
import sys

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RELAY, 'tools'))
import b757_worklist as K  # noqa: E402

PP = K.PP
REG = os.path.join(PP, 'REGISTRY.md')
FERRY = os.path.join(RELAY, 'data', 'b757_ferry.txt')
BANK = os.path.join(RELAY, 'data', 'b757_registry_line.txt')
LINE = 13
OPEN = '**Last updated:**'
PRIOR = '2026-08-24'
LEAD = 'is replaced in place, no line moving, by: "'
TAIL = '" followed by the prior line whole from its opening "2026-08-24" to its end.'


def head_from_ferry():
    t = io.open(FERRY, encoding='utf-8').read().replace('\r', '')
    i = t.find(LEAD)
    j = t.find(TAIL, i + len(LEAD)) if i >= 0 else -1
    if i < 0 or j < 0 or t.count(LEAD) != 1:
        return None
    return t[i + len(LEAD):j]


def compose(prior_line, head, date):
    """the new line from the prior line (text, no ending), the ferry's head and the date; or (None, why)."""
    if not prior_line.startswith(OPEN):
        return None, 'the line does not open %r' % OPEN
    k = prior_line.find(PRIOR)
    if k < 0:
        return None, 'the line carries no %r' % PRIOR
    if head is None or head.count('<the commit\'s UTC date>') != 1:
        return None, 'the ferry`s head not cut once, or its field not once in it'
    return head.replace('<the commit\'s UTC date>', date) + prior_line[k:], None


def main(mode):
    out = ['b757 -- (R367)(8)(iv): REGISTRY`S HEADER AT :13 REPLACED IN PLACE (tools/b757_registry_line.py %s, %s)' % (
        mode, datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')), '']
    head = head_from_ferry()
    date = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    out.append('## THE CONTROLS FIRST')
    c1 = compose('Not a header line 2026-08-24', head, date)
    c2 = compose(OPEN + ' **2026-06-04** (no prior date here)', head, date)
    out.append('  a line 13 not opening the header`s words: %s' % ('REFUSED (%s), AS WANTED' % c1[1] if c1[0] is None else '### COMPOSED, NOT AS WANTED'))
    out.append('  a line 13 with no %s: %s' % (PRIOR, 'REFUSED (%s), AS WANTED' % c2[1] if c2[0] is None else '### COMPOSED, NOT AS WANTED'))
    ctl_ok = c1[0] is None and c2[0] is None
    raw = io.open(REG, 'rb').read()
    parts = raw.split(b'\n')
    old = parts[LINE - 1]
    cr = old.endswith(b'\r')
    old_t = (old[:-1] if cr else old).decode('utf-8')
    new_t, why = compose(old_t, head, date)
    out.append('')
    out.append('## THE READ')
    out.append('  REGISTRY.md: %d bytes, %d lines, line %d %d characters, ending %s ; sha256 %s' % (
        len(raw), raw.count(b'\n'), LINE, len(old_t), 'CRLF' if cr else 'LF', hashlib.sha256(raw).hexdigest()[:16]))
    out.append('  the head cut from the ferry bank: %s' % ('%d characters' % len(head) if head else '### NOT CUT'))
    if new_t is None:
        out.append('### NOT COMPOSED: %s -- NOTHING WRITTEN' % why)
        print('\n'.join(out))
        return 2
    k = old_t.find(PRIOR)
    out.append('  the retained text: the prior line from character %d (its first %s) to its end, %d characters; opening %r' % (
        k, PRIOR, len(old_t) - k, old_t[k:k + 14]))
    out.append('  THE NEW LINE (%d characters): %s' % (len(new_t), new_t))
    new_b = new_t.encode('utf-8') + (b'\r' if cr else b'')
    parts2 = parts[:LINE - 1] + [new_b] + parts[LINE:]
    raw2 = b'\n'.join(parts2)
    diff = [i + 1 for i, (a, b) in enumerate(zip(parts, parts2)) if a != b]
    out.append('  AFTER: %d bytes, %d lines (before %d) ; lines differing %s ; the retained text the line`s tail %s' % (
        len(raw2), raw2.count(b'\n'), raw.count(b'\n'), diff, new_t.endswith(old_t[k:])))
    ok = ctl_ok and diff == [LINE] and raw2.count(b'\n') == raw.count(b'\n') and new_t.endswith(old_t[k:])
    if mode == 'write' and ok:
        if old_t.startswith(OPEN + ' **' + date) and '(b757,' in old_t:
            out.append('### THE LINE ALREADY CARRIES b757`S HEAD -- NOTHING WRITTEN')
            ok = False
        else:
            with open(REG, 'wb') as f:
                f.write(raw2)
            back = io.open(REG, 'rb').read()
            out.append('  WRITTEN AND READ BACK: equal %s ; sha256 %s' % (back == raw2, hashlib.sha256(back).hexdigest()[:16]))
            ok = back == raw2
    out.append('')
    out.append('### ### **(8)(iv): CONTROLS %s ; LINE %d %s ; LINES MOVED 0 ; %s.**' % (
        '2 OF 2 AS WANTED' if ctl_ok else 'NOT AS WANTED', LINE, 'REPLACED' if mode == 'write' and ok else 'COMPOSED' if ok else 'REFUSED',
        'DATE ' + date))
    text = '\n'.join(out) + '\n'
    print(text)
    if mode == 'write':
        io.open(BANK, 'w', encoding='utf-8', newline='\n').write(text)
        print('BANKED: data/b757_registry_line.txt')
    return 0 if ok else 3


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('dry', 'write'):
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
