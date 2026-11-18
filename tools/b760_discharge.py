# -*- coding: utf-8 -*-
"""tools/b760_discharge.py -- (R370)(6), COMPONENT 3: W-ORD-MECHANISM-ATTRIBUTION DISCHARGED BY ITS SECOND CLAUSE, its texts read from the
banks and not retyped, banked before the edition is composed.

The ruling's words (relay data/b760_ferry.txt :19): "W-ORD-MECHANISM-ATTRIBUTION, DISCHARGED BY ITS SECOND CLAUSE, on the author's pass of
[P1] (relay data/b752_author_answers.txt :7) and the author's word in this delivery. ... FINDINGS takes, in the act's entry, the two printed
lines, each in the plan's own words read from the bank and not retyped: T2's, that the edge does not abstract at the pin (:67-:76), and
T3-f's finding (:78-:80). OPEN_TRAILS takes the discharge sentence as the plan fixed it (:90-:92), the words between its quotation marks,
under one dated head, no line moving, with the pins as they stand: zq_coeff_not_multiplicative and cQ_not_nonneg on SIDE-explicit-formula's
main at v0.41. ... WHERE THE AUTHOR STRIKES THIS CLAUSE: the order stays open, W14 is not applied, the fields ORDERLINE and CLASSROW are
empty, and ERRATA 2 takes its other DISCHARGE text."

This tool writes no ledger: OPEN_TRAILS takes its sentence at Component 5 under (10)'s one dated head, FINDINGS its two lines in the act's
entry at the record, and the edition W14, ORDERLINE and CLASSROW at Component 4, each from this bank. It reads, and refuses on any miss:
  (a) the clause's standing: STANDS, the author's word since part 2 being none (events (40), (45)); a strike would set STRUCK here by hand.
  (b) the author's pass of [P1] at data/b752_author_answers.txt :7, at the relay's HEAD: the line carries "Pass [P1]".
  (c) the plan at the relay's HEAD: T2's lines :67-:76 (the first opening "(T2) THE EDGE"), T3-f's :78-:80 (the first opening "(T3-f) THE
      FINDING", the finding the words between the line's first quotation mark and the next), the discharge :90-:92 (the words between
      the quotation mark after "WOULD THEN READ:" and the next); each line's sha256 banked.
  (d) the pins at SIDE-explicit-formula through its clone, no network: the tag v0.41 peeling to main's commit (refs/remotes/origin/main,
      read after b760's removal route read the remote's main at a3aad4cc), and each of the two theorems declared once in a `.lean` file at
      v0.41 and at v0.40, by path and line; no line of the kernel printed.
  (e) the order's line at PLACE-papers HEAD, OPEN_TRAILS :17932, carrying the order's name; by its digest alone, no word printed.
  (f) BLOCK F of the text bank (read where its sha256 equals (R370) PATHS): ORDERLINE, CLASSROW and the DISCHARGE for the clause's
      standing, each one line between NEW>> and <<NEW.

  python -X utf8 -u tools/b760_discharge.py dry      the reads and the bank printed; nothing written
  python -X utf8 -u tools/b760_discharge.py write    data/b760_discharge.txt and data/b760_discharge.json written whole
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
D = os.path.join(RELAY, 'data')
NL = '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
KERNEL = 'D:/SIDE-explicit-formula'
STANDING = 'STANDS'   # ### (R370)(6): no word of the author since part 2 (data/b760_events.txt (40), (45)); STRUCK only on the author's strike
TEXT = 'b760_text.txt'
TEXT_SHA = '7c8fe2f89718604a4cc13b61b6f5b94b0dcd2582044694557f2741d233ef3472'   # ### (R370) PATHS, data/b760_ferry.txt :7
PLAN = 'data/b752_attribution_plan.txt'
ANSWERS = 'data/b752_author_answers.txt'
SPANS = dict(T2=(67, 76, '(T2) THE EDGE'), T3F=(78, 80, '(T3-f) THE FINDING'), DISCHARGE=(90, 92, 'THE ORDER\'S DISCHARGE WOULD THEN READ:'))
PINS = ('zq_coeff_not_multiplicative', 'cQ_not_nonneg')
TAGS = ('v0.41', 'v0.40')
MAIN_041 = 'a3aad4cc'
ORDER, ORDER_LINE = 'W-ORD-MECHANISM-ATTRIBUTION', 17932
OUT, OUTJ = 'b760_discharge.txt', 'b760_discharge.json'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace('\r', '')


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def relay_lines(path):
    rc, t = git(RELAY, 'show', 'HEAD:%s' % path)
    if rc:
        die('relay HEAD:%s unreadable (exit %d)' % (path, rc))
    return t.split(NL)


def quoted(text, after=None):
    """the words between the first quotation mark (after `after`, where given) and the next."""
    i = text.index(after) + len(after) if after else 0
    a = text.index('"', i)
    b = text.index('"', a + 1)
    return text[a + 1:b]


def read_answer():
    L = relay_lines(ANSWERS)
    ok = 'Pass [P1]' in L[6]
    if not ok:
        die('%s :7 carries no "Pass [P1]"' % ANSWERS)
    return dict(path=ANSWERS, line=7, sha256=sha(L[6]), carries='Pass [P1]')


def read_plan():
    L = relay_lines(PLAN)
    out = {}
    for k, (a, b, head) in SPANS.items():
        span = L[a - 1:b]
        if not span[0].strip().startswith(head) and not (k == 'DISCHARGE' and head in span[0]):
            die('%s :%d does not open "%s"' % (PLAN, a, head))
        joined = ' '.join(l.strip() for l in span)
        if k == 'T2':
            words = joined
        elif k == 'T3F':
            words = quoted(joined)
        else:
            words = quoted(joined, head)
        out[k] = dict(path=PLAN, lines=[a, b], line_sha256=[sha(l) for l in span], words=words, words_sha256=sha(words))
    return out


def read_pins():
    rc, main = git(KERNEL, 'rev-parse', 'refs/remotes/origin/main')
    rc2, peel = git(KERNEL, 'rev-parse', 'v0.41^{commit}')
    if rc or rc2 or not main.startswith(MAIN_041) or not peel.startswith(MAIN_041):
        die('SIDE-explicit-formula: origin/main %s, v0.41 peels to %s, %s wanted at both' % (main.strip()[:8], peel.strip()[:8], MAIN_041))
    out = []
    for name in PINS:
        row = dict(name=name)
        for tag in TAGS:
            rc, t = git(KERNEL, 'grep', '-n', '-E', r'^\s*(private\s+)?(theorem|lemma)\s+%s(\s|$|:)' % re.escape(name), tag, '--', '*.lean')
            hits = [l.split(':', 3)[1:3] for l in t.split(NL) if l.strip()]
            if len(hits) != 1:
                die('SIDE-explicit-formula %s: %s declared %d times, once wanted' % (tag, name, len(hits)))
            row[tag] = '%s :%s' % (hits[0][0], hits[0][1])
        out.append(row)
    return dict(main=main.strip()[:8], v041_peel=peel.strip()[:8], pins=out)


def read_order():
    rc, t = git(PP, 'show', 'HEAD:OPEN_TRAILS.md')
    rc2, head = git(PP, 'rev-parse', 'HEAD')
    if rc or rc2:
        die('PLACE-papers HEAD:OPEN_TRAILS.md unreadable')
    L = t.split(NL)
    line = L[ORDER_LINE - 1] if len(L) >= ORDER_LINE else ''
    if ORDER not in line:
        die('PLACE-papers OPEN_TRAILS :%d does not carry %s' % (ORDER_LINE, ORDER))
    return dict(path='OPEN_TRAILS.md', line=ORDER_LINE, sha256=sha(line), at=head.strip()[:8], carries=ORDER)


def read_block_f():
    b = open(os.path.join(D, TEXT), 'rb').read()
    if hashlib.sha256(b).hexdigest() != TEXT_SHA:
        die('data/%s is not the text bank of (R370) PATHS' % TEXT)
    L = b.decode('utf-8').split(NL)
    want = {'ORDERLINE': '@@ ORDERLINE WHERE (6) STANDS', 'CLASSROW': '@@ CLASSROW WHERE (6) STANDS',
            'DISCHARGE_STANDS': '@@ DISCHARGE WHERE (6) STANDS', 'DISCHARGE_STRUCK': '@@ DISCHARGE WHERE THE AUTHOR STRIKES (6)'}
    out = {}
    for k, marker in want.items():
        at = [i for i, l in enumerate(L, 1) if l == marker]
        if len(at) != 1 or L[at[0]] != 'NEW>>' or L[at[0] + 2] != '<<NEW':
            die('BLOCK F`s %s not one line between NEW>> and <<NEW' % marker)
        t = L[at[0] + 1]
        out[k] = dict(path='data/' + TEXT, line=at[0] + 2, words=t, sha256=sha(t))
    return out


def compose():
    ans, plan, pins, order, f = read_answer(), read_plan(), read_pins(), read_order(), read_block_f()
    stands = STANDING == 'STANDS'
    J = dict(act='b760', clause='(R370)(6)', standing=STANDING, order=ORDER, answer=ans, plan=plan, kernel=pins, order_line=order,
             w14='APPLY' if stands else 'NOT APPLIED',
             orderline=f['ORDERLINE'] if stands else None, classrow=f['CLASSROW'] if stands else None,
             errata_discharge=f['DISCHARGE_STANDS'] if stands else f['DISCHARGE_STRUCK'],
             findings=[plan['T2'], plan['T3F']] if stands else [], open_trails=plan['DISCHARGE'] if stands else None)
    pinline = ' ; '.join('%s at v0.41 %s, at v0.40 %s' % (p['name'], p['v0.41'], p['v0.40']) for p in pins['pins'])
    B = ['b760 -- (R370)(6), COMPONENT 3: W-ORD-MECHANISM-ATTRIBUTION %s (%s)' % (
             'DISCHARGED BY ITS SECOND CLAUSE' if stands else 'OPEN, THE CLAUSE STRUCK', time.strftime('%Y-%m-%d', time.gmtime())),
         '',
         '### written by tools/b760_discharge.py; read by the edition (W14, ORDERLINE, CLASSROW), Component 5 (OPEN_TRAILS, ERRATA 2) and the record',
         '### (FINDINGS). Every text below is read from the bank it names, not retyped; PLACE-papers and the kernel by path, line and digest alone.',
         '',
         '## THE READS',
         '  (a) THE CLAUSE: %s -- the author`s word since part 2 none (data/b760_events.txt (40), (45))' % STANDING,
         '  (b) THE PASS: %s :%d carries "%s" (sha256 %s), at the relay`s HEAD' % (ans['path'], ans['line'], ans['carries'], ans['sha256']),
         '  (c) THE PLAN: %s at the relay`s HEAD -- T2 :%d-:%d, T3-f :%d-:%d, the discharge :%d-:%d' % (
             PLAN, plan['T2']['lines'][0], plan['T2']['lines'][1], plan['T3F']['lines'][0], plan['T3F']['lines'][1],
             plan['DISCHARGE']['lines'][0], plan['DISCHARGE']['lines'][1]),
         '  (d) THE PINS: SIDE-explicit-formula origin/main %s, v0.41 peeling to %s ; %s' % (pins['main'], pins['v041_peel'], pinline),
         '  (e) THE ORDER: PLACE-papers %s OPEN_TRAILS :%d carries %s (sha256 %s), no word printed' % (order['at'], order['line'], ORDER, order['sha256']),
         '  (f) BLOCK F: %s' % ' ; '.join('%s data/%s :%d sha256 %s' % (k, TEXT, v['line'], v['sha256']) for k, v in f.items()),
         '',
         '## WHAT THE ACT ENTERS, BY DESTINATION',
         '  W14 OF THE EDITION: %s' % J['w14'],
         '  ORDERLINE (data/%s :%d): %s' % (TEXT, f['ORDERLINE']['line'], J['orderline']['words'] if stands else 'empty'),
         '  CLASSROW (data/%s :%d): %s' % (TEXT, f['CLASSROW']['line'], J['classrow']['words'] if stands else 'empty'),
         '  ERRATA 2`s DISCHARGE (data/%s :%d): %s' % (TEXT, J['errata_discharge']['line'], J['errata_discharge']['words']),
         '  OPEN_TRAILS, UNDER (10)`S ONE DATED HEAD, THE PINS BESIDE IT: %s' % (('"%s" (%s :%d-:%d, words sha256 %s) ; pins %s' % (
             plan['DISCHARGE']['words'], PLAN, plan['DISCHARGE']['lines'][0], plan['DISCHARGE']['lines'][1], plan['DISCHARGE']['words_sha256'], pinline))
             if stands else 'nothing'),
         '  FINDINGS, IN THE ACT`S ENTRY, T2`S LINE (%s :%d-:%d, words sha256 %s): %s' % (PLAN, plan['T2']['lines'][0], plan['T2']['lines'][1],
                                                                                    plan['T2']['words_sha256'], plan['T2']['words'] if stands else 'nothing'),
         '  FINDINGS, IN THE ACT`S ENTRY, T3-f`S FINDING (%s :%d-:%d, words sha256 %s): %s' % (PLAN, plan['T3F']['lines'][0], plan['T3F']['lines'][1],
                                                                                          plan['T3F']['words_sha256'], plan['T3F']['words'] if stands else 'nothing'),
         '',
         '## WHAT THE DISCHARGE DOES NOT SAY ((R370)(6))',
         '  nothing about zeta; nothing on whether the analysis of the seven classes is complete; B3 stands as PATHS_TO_THE_CRITICAL_LINE has it',
         '',
         '### ### **THE ORDER: %s ; W14 %s ; ORDERLINE AND CLASSROW %s ; THE PINS %d OF 2 AT v0.41 AND v0.40 ; NOTHING WRITTEN TO A LEDGER BY THIS TOOL.**' % (
             'DISCHARGED BY ITS SECOND CLAUSE' if stands else 'OPEN, STRUCK', J['w14'], 'FILLED' if stands else 'EMPTY', len(pins['pins']))]
    return B, J


def main(argv):
    if not argv or argv[0] not in ('dry', 'write'):
        sys.exit(__doc__)
    B, J = compose()
    print(NL.join(B))
    if argv[0] == 'dry':
        return
    for name, data in ((OUT, (NL.join(B) + NL).encode('utf-8')), (OUTJ, (json.dumps(J, ensure_ascii=False, indent=1) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(p + '.tmp', p)
        print('written data/%s: %d bytes, sha256 %s' % (name, len(data), hashlib.sha256(data).hexdigest()[:16]))


if __name__ == '__main__':
    main(sys.argv[1:])
