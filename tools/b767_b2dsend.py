# -*- coding: utf-8 -*-
"""tools/b767_b2dsend.py -- b767, Component 5: THE ONE SEND OF standing-b2d UNDER A LONGER LIMIT, BY THE AUTHOR'S ANSWER (option 4,
typed, to the question banked as data/b767_put_1.json; data/b767_author_words_preseal.txt :2). Written by the Write tool and committed
before its run (N2).

tools/standing/prevdry.py's own exercise() for b767 and standing-b2d with timeout=900 in place of its default, its result banked by the
same file's write_bank(), as the run route banks it (prevdry.py :161-:176), the memory hold read first as that route reads it
(b703_checks.free_mb, the hold 2,560 MB). Nothing in tools/standing/ moves and the guard's constant stays at 590 (prevdry.py :97).

ONE SEND, NO SECOND: the send's mark, data/b767_b2dsend.json, is created before the send (opened 'x', so a second run refuses even where
the first was stopped) and holds the send's start, its end and the verdict after it. Where the part reads SOURCES OK the bank stands with
its true seconds, printed beside the guard's 590; where it ends at 900 s, or fails, the tool prints it and the act halts before the lock on
the answer's terms (option 3's), with no further send.

  python -X utf8 -u tools/b767_b2dsend.py send
"""
import json
import os
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, os.path.join(T, 'standing'))
sys.path.insert(1, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT, PART, LIMIT, GUARD = 'b767', 'standing-b2d', 900, 590
MARK = os.path.join(D, '%s_b2dsend.json' % ACT)


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _write(p, j):
    s = json.dumps(j, indent=1, ensure_ascii=False) + '\n'   # composed whole before the file opens (b328's zero-byte husk)
    with open(p + '.tmp', 'wb') as f:
        f.write(s.encode('utf-8'))
    os.replace(p + '.tmp', p)


def send():
    import prevdry as PD
    import b703_checks as C3
    if PD._cur().get('act') != ACT:
        sys.exit('### REFUSED: data/act_current.json names %s, not %s -- NOTHING SENT' % (PD._cur().get('act'), ACT))
    if os.path.exists(MARK):
        sys.exit('### REFUSED: THE ONE SEND STANDS (data/%s) -- NO SECOND SEND, BY THE AUTHOR`S ANSWER' % os.path.basename(MARK))
    fm = C3.free_mb()
    print('  free %s MB, the hold 2560 %s' % (fm, 'MET' if isinstance(fm, int) and fm >= 2560 else '### NOT MET'))
    if not isinstance(fm, int) or fm < 2560:
        return 3
    started = _now()
    with open(MARK, 'x', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(dict(act=ACT, part=PART, limit=LIMIT, guard=GUARD, started=started), indent=1) + '\n')
    print('  THE ONE SEND of %s %s under the limit %d s (the guard`s constant %d s unmoved), started %s' % (ACT, PART, LIMIT, GUARD, started))
    out = PD.exercise(ACT, PART, timeout=LIMIT)
    p = PD.write_bank(ACT, PART, out)
    secs = out.get('secs')
    beyond = isinstance(secs, (int, float)) and secs > GUARD
    _write(MARK, dict(act=ACT, part=PART, limit=LIMIT, guard=GUARD, started=started, ended=_now(), ok=bool(out.get('ok')),
                      secs=secs, err=out.get('err'), blob=out.get('blob'), bank=os.path.relpath(p, RELAY).replace('\\', '/')))
    print('  %s %s: %s%s (%s s%s) -> %s' % (ACT, PART, 'SOURCES OK' if out['ok'] else '### FAILS',
                                            '' if out['ok'] else ' %s at line %s: %s' % (out.get('err'), out.get('line'), out.get('at')),
                                            secs, ', above the guard`s %d s, under the answer`s %d s' % (GUARD, LIMIT) if beyond and out['ok'] else '',
                                            os.path.relpath(p, RELAY)))
    print('  ### THE ONE SEND: %s' % ('SOURCES OK -- THE LOCK GATE READS THE BANK' if out['ok'] else
                                     'NOT OK -- LETTER IT AND HALT BEFORE THE LOCK ON THE ANSWER`S TERMS, NO FURTHER SEND'))
    return 0 if out['ok'] else 1


if __name__ == '__main__':
    if sys.argv[1:] == ['send']:
        sys.exit(send())
    sys.exit(__doc__)
