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
ROW = re.compile(r"^    \(((?:[a-z]'*)|\d+)\) (?:THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]")   # ### v1.34.0, (R364)(3)(viii): any number of primes
ANY_ROW = re.compile(r"^    \(((?:[a-z]'*)|\d+)\) ")


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
    """v1.34.0, (R364)(3)(v): the post-seal events bank (data/<act>_events_postseal.txt, written by the close by design) read beside the
    events bank: b753's events (1)-(9) and (10)-(14), fourteen."""
    ev = _text(act, 'events', data, rev)
    ps = _text(act, 'events_postseal', data, rev)
    return tally(items(_text(act, 'defects', data, rev), ev + ('\n' + ps if ps else '')), act, rev)


def line(c):
    return 'CLAIM %d, CLOSE %d, REPEAT %d of %d (defects %d, events %d)' % (c['claim'], c['close'], c['repeat'], c['total'], c['defects'], c['events'])


def cause(a, b):
    sa, sb = set(a['ids']), set(b['ids'])
    return dict(only_first=[x for x in a['ids'] if x not in sb], only_second=[x for x in b['ids'] if x not in sa])


# ================================================================================ v1.34.3, (R364)(5)[U3]: THE HOOK'S REFUSALS COUNTED BY KIND
# ### [U3], passed at b754 (relay data/b754_rules.txt (12); data/b754_author_answers.txt :118): "A REFUSAL BEFORE A CALL RUNS IS THE HOOK WORKING:
# ### it is banked in the refusals bank and counted in one line by kind in the entry and the trail; it takes no letter; a kind whose count exceeds
# ### the previous act's is one event." In force from b755 (U3_FROM): at an earlier act the guard prints its reading and refuses nothing.
#   refusal_kinds(text)                     {kind: count} over a refusals bank's rows (tools/standing/hook.py refuse(): "<time> | <KIND> | <tool> | ...")
#   refusals_line(act, prev, kinds, pk)     the one line for the entry and the trail
#   refusals_guard(act, prev, ...texts)     (ok, lines) over texts given: each kind above the previous count an event; no defect row citing
#                                           the act's refusals bank; the act module naming refusals_line( at least twice (the entry, the trail)
#   refusals_gate(act, data=None)           refusals_guard over the working banks and tools/acts/<act>.py (tools/standing/prelock.py's gate)
# ### THE REACH: a defect row is read as a refusal lettered where it cites a line of the act's refusals bank, whatever its own cause (b754's (p),
# ### the (W) list not regenerated, cites the refusal that stopped its edit and reads so); an event row names a kind by the kind's word and the
# ### bank's path; the act module is read by its count of the call, not by where the call stands.
U3_FROM = 755
REFUSAL = re.compile(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \| ([A-Z]+) \| ')
ROW_HEAD = re.compile(r"^    \(((?:[a-z]'*)|\d+)\) ")


def refusal_kinds(text):
    out = {}
    for l in (text or '').replace('\r', '').split('\n'):
        m = REFUSAL.match(l)
        if m:
            out[m.group(1)] = out.get(m.group(1), 0) + 1
    return out


def refusals_above(kinds, pk):
    """[(kind, count, the previous act's count)] for each kind whose count exceeds the previous act's."""
    return [(k, n, pk.get(k, 0)) for k, n in sorted(kinds.items()) if n > pk.get(k, 0)]


def refusals_line(act, prev=None, kinds=None, pk=None, lettered=None, data=None):
    """the one line; with no kinds given, every figure read from the working banks (refusals_gate's texts), the letters among them. The
    lettered clause prints what the defects bank holds -- 'none lettered' only where no defect row cites the act's refusals bank."""
    if kinds is None:
        prev, t = _texts(act, data)
        kinds, pk = refusal_kinds(t['ref']), refusal_kinds(t['prev'])
        lettered = _lettered(act, t['defects'])
    up = refusals_above(kinds, pk or {})
    lt = '' if lettered is None else ('none lettered; ' if not lettered else 'lettered %d, %s; ' % (len(lettered), ', '.join('(%s)' % i for i in lettered)))
    return 'Refusals by the hook before a call ran ([U3]): %d -- %s; %skinds above %s’s count: %s (relay data/%s_hook_refusals.txt).' % (
        sum(kinds.values()), ', '.join('%s %d' % kv for kv in sorted(kinds.items())) or 'none', lt, prev,
        ('; '.join('%s %d against %d' % x for x in up) + ', one event each') if up else 'none', act)


def _lettered(act, defects_text):
    bank = 'data/%s_hook_refusals.txt :' % act
    return [i for i, t in _rows(defects_text) if re.match(r"[a-z]'*$", i) and bank in t]


def _texts(act, data=None):
    d = data or os.path.join(RELAY, 'data')
    prev = 'b%d' % (int(re.sub(r'\D', '', act)) - 1)

    def rd(name):
        p = os.path.join(d, name)
        if not os.path.exists(p):
            return ''
        with open(p, encoding='utf-8', errors='replace') as f:
            return f.read()
    mp = os.path.join(RELAY, 'tools', 'acts', '%s.py' % act)
    mod = open(mp, encoding='utf-8', errors='replace').read() if os.path.exists(mp) else ''
    return prev, dict(ref=rd('%s_hook_refusals.txt' % act), prev=rd('%s_hook_refusals.txt' % prev), defects=rd('%s_defects.txt' % act), module=mod,
                      events=rd('%s_events.txt' % act) + '\n' + rd('%s_events_postseal.txt' % act))


def _rows(text):
    """the rows of an events or defects bank: [(id, the row's lines joined)], a row opening at four spaces and running to the next row or head."""
    out, cur = [], None
    for l in (text or '').replace('\r', '').split('\n'):
        m = ROW_HEAD.match(l)
        if m:
            cur = [m.group(1), l]
            out.append(cur)
        elif cur is not None and l.startswith('     '):
            cur[1] += ' ' + l.strip()
        else:
            cur = None
    return [(a, b) for a, b in out]


def refusals_guard(act, prev, text, prev_text, events_text, defects_text, module_text):
    kinds, pk = refusal_kinds(text), refusal_kinds(prev_text)
    up = refusals_above(kinds, pk)
    bank = 'data/%s_hook_refusals.txt' % act
    ev = _rows(events_text)
    named = [(k, [i for i, t in ev if re.search(r'\b%s\b' % k, t) and bank in t]) for k, _n, _p in up]
    missing = [k for k, ids in named if not ids]
    lettered = _lettered(act, defects_text)
    calls = (module_text or '').count('refusals_line(')
    force = int(re.sub(r'\D', '', act) or 0) >= U3_FROM
    ok_ = not missing and not lettered and calls >= 2
    L = ['  THE REFUSALS BY KIND ((R364)(5)[U3], relay data/b754_rules.txt (12)): ' + refusals_line(act, prev, kinds, pk, lettered),
         '    kinds above %s`s count, each named by an event row naming the kind and %s: %d of %d%s' % (
             prev, bank, len(up) - len(missing), len(up), (' ; NOT NAMED: %s' % ', '.join(missing)) if missing else ''),
         '    defect rows citing %s (a refusal given a letter): %s' % (bank, ', '.join('(%s)' % i for i in lettered) or 'NONE'),
         '    the act module naming refusals_line( %d time(s), wanted 2 or more (the entry and the trail)' % calls]
    if force:
        L.append('    ### [U3] IN FORCE AT %s: %s' % (act, 'CLEAR' if ok_ else 'NOT CLEAR'))
    else:
        L.append('    ### [U3] NOT IN FORCE AT %s (from b%d): read and printed, refusing nothing (%s by its clauses)' % (act, U3_FROM, 'CLEAR' if ok_ else 'NOT CLEAR'))
    return (ok_ or not force), L


def refusals_gate(act, data=None):
    prev, t = _texts(act, data)
    return refusals_guard(act, prev, t['ref'], t['prev'], t['events'], t['defects'], t['module'])
