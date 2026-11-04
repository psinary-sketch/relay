# -*- coding: utf-8 -*-
"""standing/phases.py -- v1.19.0, (R349)(2)(ii), b738 events (5): THE POST-PUSH READ AGAINST THE PRE-PUSH READ, PART BY PART, BEFORE ANY GUARD MOVES.

b738's post-push parts standing-b2b and standing-b2c ran their act-root chain phases at 275 s and 493 s, where the pre-push runs of the same
parts ran 139 s and 171 s. This reader puts each part's two banks side by side: the phase table (THE PHASES, IN SECONDS), the free memory at
the part's start, the remote reads per repository (data/<act>_lsr_<mode>_<part>.json), the reads at commit, and each phase's ratio; it says
whether the post-push read did work the pre-push read did not (another remote read, another repository, another read at commit) and, by the
ratios, whether the time grew in the chain phase alone or in every phase of the part. Read-only; the finding is printed, no guard moved.

  python -X utf8 -u tools/standing/phases.py <act>        prints the table and the finding
  compare(act, parts, read) -> (lines, finding)
"""
import json
import os
import re
import sys

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(os.path.dirname(T), 'data')
PHASE_LINE = re.compile(r'THE PHASES, IN SECONDS: (.*)$', re.M)
FREE_LINE = re.compile(r'free memory at the part`s start (\d+) MB')
READS_LINE = re.compile(r'### the reads at commit, (b\d+): (\{[^}]*\})')
NAMES = (('the banks and the state', 'state'), ('the written files, the public bytes and the prior banks', 'files'), ('the act-root chain`s part', 'chain'))


def _read(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def part_reading(text, lsr):
    """(phases {short: s}, free MB, reads at commit, remote reads {repo: n}) of one part's bank and its ls-remote bank."""
    ph = {}
    m = PHASE_LINE.search(text or '')
    for seg in (m.group(1).split('; ') if m else []):
        for long_, short in NAMES:
            if seg.startswith(long_):
                ph[short] = int(seg.rsplit(' ', 1)[1])
    fm = FREE_LINE.search(text or '')
    rd = READS_LINE.search(text or '')
    try:
        lj = (json.loads(lsr).get('lsr') or {}) if lsr else {}
    except ValueError:
        lj = {}
    return ph, int(fm.group(1)) if fm else None, (rd.group(1), rd.group(2)) if rd else None, lj


def compare(act, parts, read=_read):
    L, rows = [], []
    L.append('  %-14s | %-26s | %-26s | %-18s | %s' % ('part', 'pre-push state/files/chain', 'post-push state/files/chain', 'ratio s/f/c', 'free MB pre, post ; remote reads equal ; reads at commit equal'))
    for p in parts:
        a = part_reading(read('%s_checks_%s.txt' % (act, p)), read('%s_lsr_%s.json' % (act, p)))
        b = part_reading(read('%s_checks_postpush_%s.txt' % (act, p)), read('%s_lsr_postpush_%s.json' % (act, p)))
        if not a[0] or not b[0]:
            L.append('  %-14s | UNREAD (pre %s, post %s)' % (p, bool(a[0]), bool(b[0])))
            continue
        r = dict((k, (b[0].get(k, 0) / a[0][k]) if a[0].get(k) else None) for k in ('state', 'files', 'chain'))
        same_lsr, same_reads = a[3] == b[3], a[2] == b[2]
        rows.append((p, a, b, r, same_lsr, same_reads))
        f = lambda x: '%s/%s/%s' % (x.get('state'), x.get('files'), x.get('chain'))   # noqa: E731
        L.append('  %-14s | %-26s | %-26s | %-18s | %s, %s ; %s (%d repositories) ; %s' % (
            p, f(a[0]), f(b[0]), '/'.join('%.2f' % v if v else '-' for v in (r['state'], r['files'], r['chain'])), a[1], b[1], same_lsr, len(b[3]), same_reads))
    more_work = [p for p, _a, _b, _r, sl, sr in rows if not (sl and sr)]
    slow = [p for p, _a, _b, r, _sl, _sr in rows if (r['chain'] or 0) > 1.3]
    whole = [p for p, _a, _b, r, _sl, _sr in rows if (r['chain'] or 0) > 1.3 and (r['state'] or 0) > 1.3]
    chain_only = [p for p in slow if p not in whole]
    finding = ('THE POST-PUSH READ DID THE PRE-PUSH READ`S WORK: the same remote reads per repository and the same reads at commit in %d of %d parts%s ; '
               'THE TIME GREW IN %s ; %s ; THE OTHER PARTS AT THEIR PRE-PUSH TIMES ; NO GUARD MOVED' % (
                   len(rows) - len(more_work), len(rows), (' (more work in %s)' % ', '.join(more_work)) if more_work else '',
                   ', '.join(slow) or 'NO PART',
                   ('EVERY PHASE OF %s, the local phases with the chain: the slowdown the host`s while those parts ran, not the post-push route' % ', '.join(whole)) if whole else 'NO PART`S LOCAL PHASES',
               ) + ((' ; THE CHAIN PHASE ALONE IN %s' % ', '.join(chain_only)) if chain_only else ''))
    return L, finding


if __name__ == '__main__':
    act = sys.argv[1] if len(sys.argv) > 1 else None
    parts = ('standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3')
    L, finding = compare(act, parts)
    print('\n'.join(L + ['', '### ' + finding]))
