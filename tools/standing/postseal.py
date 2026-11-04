# -*- coding: utf-8 -*-
"""standing/postseal.py -- v1.21.0, (R351)(2)(iv), b740 events (5), REPEAT b736 (8): G-RULE-POSTSEAL-READ'S FAILURE PRINTED AS SUCH. The arm counts a
shell call naming the entry or the trail after the seal, a call the hook refused included (b740's `git grep` over OPEN_TRAILS ran nothing and the
arm read FAIL). Two parts:
  - the exclude list is printed before any read after the seal: tools/standing/commit.py prints `hook.py excludes` after the seal commit it makes;
  - the arm's failing reading carries its ordinal: the acts whose suite bank (data/<act>_checks.txt) lists the arm among LIVE FAILING are counted,
    and the failure is printed as the next of them, with the acts named, read from the banks and not typed.

  failed_before(act) -> [acts]        note(act) -> the ordinal clause        wrap(pred, act) -> the arm's predicate with the clause on a failure
"""
import os
import re

S = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(os.path.dirname(S)), 'data')
ARM = 'G-RULE-POSTSEAL-READ'
BANK = re.compile(r'^(b\d+)_checks\.txt$')
FAILING = re.compile(r'LIVE FAILING : \d+ \[([^\]]*)\]')
ORD = ('first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth').split()


def failed_before(act, data=D):
    n = int(act[1:])
    out = []
    for f in sorted(os.listdir(data)):
        m = BANK.match(f)
        if not m or int(m.group(1)[1:]) >= n:
            continue
        with open(os.path.join(data, f), encoding='utf-8', errors='replace') as fh:
            t = fh.read()
        if any("'%s'" % ARM in x for x in FAILING.findall(t)):
            out.append(m.group(1))
    return sorted(out, key=lambda a: int(a[1:]))


def note(act, data=D):
    prior = failed_before(act, data)
    k = len(prior) + 1
    return ' ; THE ARM`S %s FAILURE BY THE SUITE BANKS (LIVE FAILING before at %s)' % ((ORD[k - 1] if k <= len(ORD) else '%dth' % k).upper(), ', '.join(prior) or 'none')


def wrap(pred, act):
    def p(*a):
        r = pred(*a)
        if r and not r[0]:
            r = tuple(r[:3]) + (r[3] + note(act),) + tuple(r[4:])
        return r
    return p
