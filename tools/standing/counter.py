# -*- coding: utf-8 -*-
"""standing/counter.py -- v1.22.0, (R352)(2)(iii), b741 touch row (28): THE COUNTER COMPOSED ONCE, FROM THE DEFECTS AND EVENTS BANKS, AND READ INTO EVERY
PLACE THAT PRINTS IT. b741's touch read (data/b741_touch.txt :35, row (28)) read the entry's counter as CLAIM 5, CLOSE 16, REPEAT 11 of 21 at the locked
bank, and FINDINGS at the record printed CLAIM 5, CLOSE 17, REPEAT 11 of 22; its closing (data/b741_closing.txt :5) CLAIM 5, CLOSE 20, REPEAT 14 OF 25.
Three printers each counted the rows they found at their own moment, and none named the set it counted: 21 defects at the lock; the 21 defects and
event (1), entered after the lock, at the record; and the four events with the defects at the closing. Here the one composer counts both banks and
names its set (defects n, events n, the last item), so two figures that differ carry their cause beside them.

  items(text_defects, text_events)   [(id, CLAIM|CLOSE, repeat bool)] in bank order, defects first; an untagged row raises
  compose(act, data=None, rev=None)  dict(claim, close, repeat, total, defects, events, last, ids) from the working banks, or from relay `rev`
  line(c)                            "CLAIM c, CLOSE d, REPEAT r of t (defects n, events m)"
  cause(a, b)                        the items one composition holds and the other lacks, both ways
"""
import os
import re
import subprocess

S = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(os.path.dirname(S))
ROW = re.compile(r"^    \(((?:[a-z]'?)|\d+)\) (?:THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]")
ANY_ROW = re.compile(r"^    \(((?:[a-z]'?)|\d+)\) ")


def items(text_defects, text_events):
    out = []
    for kind, text in (('defect', text_defects), ('event', text_events)):
        for l in (text or '').replace('\r', '').split('\n'):
            if not ANY_ROW.match(l):
                continue
            m = ROW.match(l)
            if not m:
                raise ValueError('### AN UNTAGGED %s ROW: %s' % (kind.upper(), l[:80]))
            out.append(('%s (%s)' % (kind, m.group(1)), m.group(2), not m.group(3).startswith('NEW')))
    return out


def _text(act, name, data, rev):
    if rev:
        r = subprocess.run(['git', '-C', RELAY, 'show', '%s:data/%s_%s.txt' % (rev, act, name)], capture_output=True)
        return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else ''
    p = os.path.join(data or os.path.join(RELAY, 'data'), '%s_%s.txt' % (act, name))
    if not os.path.exists(p):
        return ''
    with open(p, encoding='utf-8') as f:
        return f.read()


def tally(it, act=None, rev=None):
    """the composition of a list of items (items()' rows, or a subset of them)."""
    return dict(act=act, rev=rev, claim=sum(1 for x in it if x[1] == 'CLAIM'), close=sum(1 for x in it if x[1] == 'CLOSE'),
                repeat=sum(1 for x in it if x[2]), total=len(it), defects=sum(1 for x in it if x[0].startswith('defect')),
                events=sum(1 for x in it if x[0].startswith('event')), last=it[-1][0] if it else None, ids=[x[0] for x in it])


def compose(act, data=None, rev=None):
    return tally(items(_text(act, 'defects', data, rev), _text(act, 'events', data, rev)), act, rev)


def line(c):
    return 'CLAIM %d, CLOSE %d, REPEAT %d of %d (defects %d, events %d)' % (c['claim'], c['close'], c['repeat'], c['total'], c['defects'], c['events'])


def cause(a, b):
    sa, sb = set(a['ids']), set(b['ids'])
    return dict(only_first=[x for x in a['ids'] if x not in sb], only_second=[x for x in b['ids'] if x not in sa])
