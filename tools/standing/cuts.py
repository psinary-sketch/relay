# -*- coding: utf-8 -*-
"""standing/cuts.py -- THE PROJECT'S CUTS OF THE TWO LARGE LEDGERS ((R364)(5)[M2] (d), passed by the author 2026-11-13 at the put relay
data/b754_put_7.json, data/b754_author_answers.txt :153; the rule data/b754_rules.txt (16)). Landed at b754 as tools/standing/ v1.34.5.

Two files cut from PLACE-papers' ledgers at one commit (the build's), edited by no hand, written beside the archive by the builder
(tools/mirror_build.ps1); the ledgers themselves are not split, no line of them moves and no cite changes.
  FINDINGS_CUT.md     the file's head and its reference layer whole (to the first rule line after `## How findings move`), every
                      level-two heading after it by its line in the ledger ("FINDINGS :N <heading>"), and the entries of the last twenty
                      acts whole, from the heading `## Corrigendum to b<N-20>` the earliest of them wrote (N the act building the cut).
  OPEN_TRAILS_CUT.md  its head (to the first heading of level two or three), its standing items (the section `## Open trails (active)`
                      to the next level-two heading), the trails of the last ten acts whole (from `### b<N-10> — lane two`), and every
                      earlier level-three heading by its line ("OPEN_TRAILS :N <heading>").
Each cut's head says what it is, from which commit, and that a cite FINDINGS :N or OPEN_TRAILS :N is a line of the ledger and not of the
cut. Every needle is read once or the cut refuses: no cut is written short. The cut's logic is the one the [M2] put measured
(tools/b754_agenda.py findings_cut and trails_cut at relay d6d6f88e, its figures at data/b754_agenda.txt :557-:560), read here with refusals
in place of its silent omissions. Written at b754 by the Write tool; no identifier of the author is read into any string here.

  python -X utf8 -u tools/standing/cuts.py dry [<rev>] [--act bNNN]        the two cuts' lines and bytes, nothing written
  python -X utf8 -u tools/standing/cuts.py write <dir> [<rev>] [--act bNNN] the two files written into <dir>, outside every repository
  python -X utf8 -u tools/standing/cuts.py control                          the controls (planted ledgers; the record at 3020ac84)
"""
import os
import re
import sys

S = os.path.dirname(os.path.abspath(__file__))
if S not in sys.path:
    sys.path.insert(0, S)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A      # noqa: E402
import orders as OR  # noqa: E402  (OR.PP, PLACE-papers' place)

NL = '\n'
NAMES = ('FINDINGS_CUT.md', 'OPEN_TRAILS_CUT.md')
LAST_F, LAST_O = 20, 10


class Refuse(Exception):
    pass


def heading_level(l):
    m = re.match(r'^(#+)\s', l)
    return len(m.group(1)) if m else 0


def ledger(rev, path):
    b = A.blob(rev, path, 'pp')
    if b is None:
        raise Refuse('%s not read at PLACE-papers %s' % (path, rev))
    return b.decode('utf-8').replace('\r', '').split(NL)


def findings_cut(F, act_n, last=LAST_F):
    """(lines, the layer's end, the start of the last acts' entries, the headings listed)."""
    hm = [k for k, l in enumerate(F, 1) if l.startswith('## How findings move')]
    if len(hm) != 1:
        raise Refuse('`## How findings move` read %d times in FINDINGS, once wanted' % len(hm))
    end = next((k for k in range(hm[0], len(F) + 1) if F[k - 1].strip() == '---'), None)
    if end is None:
        raise Refuse('no rule line after `## How findings move`: the layer`s end not read')
    rx = re.compile(r'^## Corrigendum to b%d\W' % (act_n - last))
    starts = [k for k in range(end + 1, len(F) + 1) if rx.match(F[k - 1])]
    if len(starts) != 1:
        raise Refuse('`## Corrigendum to b%d` read %d times after the layer, once wanted' % (act_n - last, len(starts)))
    s = starts[0]
    out, heads = F[:end], 0
    for k in range(end + 1, s):
        if F[k - 1].startswith('## '):
            out.append('FINDINGS :%d %s' % (k, F[k - 1]))
            heads += 1
    return out + F[s - 1:], end, s, heads


def trails_cut(O, act_n, last=LAST_O):
    """(lines, the first heading, (the standing items' first and last line), the start of the last acts' trails, the headings listed)."""
    first = next((k for k, l in enumerate(O, 1) if heading_level(l) in (2, 3)), None)
    if first is None:
        raise Refuse('no heading of level two or three in OPEN_TRAILS')
    st = [k for k, l in enumerate(O, 1) if l.startswith('## Open trails (active)')]
    if len(st) != 1:
        raise Refuse('`## Open trails (active)` read %d times in OPEN_TRAILS, once wanted' % len(st))
    st0 = st[0]
    st1 = next((k for k in range(st0 + 1, len(O) + 1) if O[k - 1].startswith('## ')), len(O) + 1) - 1
    rx = re.compile(r'^### b%d — lane two' % (act_n - last))
    tr = [k for k, l in enumerate(O, 1) if rx.match(l)]
    if len(tr) != 1:
        raise Refuse('`### b%d — lane two` read %d times in OPEN_TRAILS, once wanted' % (act_n - last, len(tr)))
    t0 = tr[0]
    out, heads = O[:first - 1] + O[st0 - 1:st1], 0
    for k in range(first, t0):
        if st0 <= k <= st1:
            continue
        if O[k - 1].startswith('### '):
            out.append('OPEN_TRAILS :%d %s' % (k, O[k - 1]))
            heads += 1
    return out + O[t0 - 1:], first, (st0, st1), t0, heads


def head(ledger_name, commit):
    stem = ledger_name[:-3]
    return ['# %s -- THE PROJECT`S CUT, written by relay tools/standing/cuts.py from PLACE-papers %s at %s, edited by no hand' % (
        stem, ledger_name, commit),
        '# a cite of the form %s :N is a line of the ledger and not of this cut; the ledger stands whole in the archive' % stem, '']


def nbytes(ls):
    return len((NL.join(ls) + NL).encode('utf-8'))


def act_number(act=None):
    a = act or A.current()['act']
    m = re.match(r'^b(\d+)$', a)
    if not m:
        raise Refuse('the act %r not read as b<N>' % a)
    return int(m.group(1))


def build(rev='main', act=None, F=None, O=None):
    """the two cuts at `rev` for the act building them: dict(name -> lines) and the figures printed."""
    n = act_number(act)
    commit = A.gs('pp', 'rev-parse', '--short=8', rev) if (F is None or O is None) else rev
    F = ledger(rev, 'FINDINGS.md') if F is None else F
    O = ledger(rev, 'OPEN_TRAILS.md') if O is None else O
    fc, fend, fs, fh = findings_cut(F, n)
    oc, ofirst, (st0, st1), t0, oh = trails_cut(O, n)
    cuts = {NAMES[0]: head('FINDINGS.md', commit) + fc, NAMES[1]: head('OPEN_TRAILS.md', commit) + oc}
    fig = ['THE PROJECT`S CUTS at PLACE-papers %s for b%d ((R364)(5)[M2] (d)):' % (commit, n),
           '  %s: the head and the layer :1-:%d whole, %d level-two headings after it by their lines, the last %d acts` entries from :%d whole: '
           '%d lines, %d bytes (the ledger %d lines)' % (NAMES[0], fend, fh, LAST_F, fs, len(cuts[NAMES[0]]), nbytes(cuts[NAMES[0]]), len(F)),
           '  %s: its head :1-:%d, its standing items :%d-:%d, the last %d acts` trails from :%d whole, %d earlier level-three headings by '
           'their lines: %d lines, %d bytes (the ledger %d lines)' % (NAMES[1], ofirst - 1, st0, st1, LAST_O, t0, oh, len(cuts[NAMES[1]]),
                                                                       nbytes(cuts[NAMES[1]]), len(O))]
    return cuts, fig, dict(commit=commit, fend=fend, fs=fs, fh=fh, ofirst=ofirst, st=(st0, st1), t0=t0, oh=oh, F=F, O=O,
                           fbody=fc, obody=oc)


def cite_check(cut_lines, L, stem):
    """every `<stem> :N <heading>` line of a cut read against the ledger's line N: (listed, agreeing)."""
    rx = re.compile(r'^%s :(\d+) (.*)$' % stem)
    got = [(int(m.group(1)), m.group(2)) for m in (rx.match(l) for l in cut_lines) if m]
    return len(got), sum(1 for k, h in got if 0 < k <= len(L) and L[k - 1] == h)


def outside_repositories(d):
    p = os.path.normcase(os.path.abspath(d))
    for repo in (os.path.dirname(os.path.dirname(S)), OR.PP):
        r = os.path.normcase(os.path.abspath(repo))
        if p == r or p.startswith(r + os.sep):
            return False
    return True


def write(d, rev='main', act=None):
    if not outside_repositories(d):
        raise Refuse('%s stands inside a repository: the cuts are written beside the archive, outside every repository' % d)
    cuts, fig, _m = build(rev, act)
    os.makedirs(d, exist_ok=True)
    for name in NAMES:
        p = os.path.join(d, name)
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(cuts[name]) + NL)
        os.replace(p + '.tmp', p)
    return fig + ['  written: %s' % os.path.join(d, n) for n in NAMES]


# ================================================================================ controls
AGENDA = dict(rev='3020ac84', act='b754', f_lines=3805, f_bytes=646485, o_lines=2115, o_bytes=423551)   # data/b754_agenda.txt :558-:560
AGENDA_HEAD = ['# FINDINGS -- THE PROJECT`S CUT (a cut by a tool from FINDINGS.md at <commit>, edited by no hand)',
               '# a cite of the form FINDINGS :N is a line of the ledger and not of this cut; the ledger stands whole in the archive', '']


def planted(n=754):
    F = ['# FINDINGS', 'head', '## I. the layer', '### an-anchor', '**bold**', '## How findings move', 'rule', '---',
         '## an old entry', 'old body', '## another old entry', 'x', '## Corrigendum to b%d`s record' % (n - LAST_F), 'kept body',
         '## the next entry', 'kept too']
    O = ['# OPEN_TRAILS', 'head', '## Open trails (active)', 'O.1 standing', '## Closed', '### b%d — lane two, old' % (n - 30),
         'old trail', '### b%d — lane two, older' % (n - 20), 'y', '### b%d — lane two, kept' % (n - LAST_O), 'kept trail']
    return F, O


def control():
    rows = []

    def case(what, got, want):
        rows.append(got == want)
        return '  %s : got %s ; wanted %s ; %s' % (what, got, want, 'AS WANTED' if got == want else '### NOT AS WANTED')
    out = ['### THE CUTS` CONTROLS ((R364)(5)[M2] (d))']
    F, O = planted()
    cuts, _fig, m = build('PLANTED', 'b754', F, O)
    fc, oc = cuts[NAMES[0]], cuts[NAMES[1]]
    out.append(case('CONSTRUCTED: FINDINGS` cut keeps the layer to its rule line whole, lists the two headings between it and the last acts by '
                    'line, and keeps the last acts whole', (fc[3:3 + m['fend']] == F[:m['fend']], [l for l in fc if l.startswith('FINDINGS :')],
                                                            fc[-4:]), (True, ['FINDINGS :9 ## an old entry', 'FINDINGS :11 ## another old entry'], F[-4:])))
    out.append(case('CONSTRUCTED: each listed heading read at its ledger line (listed, agreeing)', cite_check(fc, F, 'FINDINGS'), (2, 2)))
    out.append(case('CONSTRUCTED: OPEN_TRAILS` cut keeps the head and the standing items, lists the earlier trails by line, keeps the last '
                    'ten acts whole', (oc[3:5], oc[5:7], [l for l in oc if l.startswith('OPEN_TRAILS :')], oc[-2:]),
                    (['# OPEN_TRAILS', 'head'], ['## Open trails (active)', 'O.1 standing'],
                     ['OPEN_TRAILS :6 ### b724 — lane two, old', 'OPEN_TRAILS :8 ### b734 — lane two, older'], O[-2:])))
    out.append(case('CONSTRUCTED: each head says what it is, from which commit, and that a cite is a line of the ledger',
                    all(('THE PROJECT`S CUT' in c[0] and 'at PLANTED' in c[0] and 'not of this cut' in c[1]) for c in (fc, oc)), True))
    for what, F2, O2 in (('no `## How findings move`', [l for l in F if not l.startswith('## How findings move')], O),
                         ('the last acts` corrigendum heading absent', [l for l in F if not l.startswith('## Corrigendum')], O),
                         ('the standing items` heading twice', F, O + ['## Open trails (active)']),
                         ('the last ten acts` trail heading absent', F, [l for l in O if 'kept' not in l])):
        try:
            build('PLANTED', 'b754', F2, O2)
            got = 'WRITTEN'
        except Refuse as e:
            got = 'REFUSED'
            what += ' (%s)' % str(e)[:80]
        out.append(case('CONSTRUCTED: %s' % what, got, 'REFUSED'))
    out.append(case('CONSTRUCTED: a folder inside the relay refused as the cuts` place', outside_repositories(os.path.join(os.path.dirname(os.path.dirname(S)), 'x')), False))
    try:
        rc, fig, mr = build(AGENDA['rev'], AGENDA['act'])
        ff = nbytes(AGENDA_HEAD + mr['fbody'])
        of = nbytes(AGENDA_HEAD + mr['obody'])
        out.append(case('RECORD: at PLACE-papers %s for b754, the lines and bytes the [M2] put printed (its lines the cut`s body, its bytes '
                        'with the put`s three-line head in place of this tool`s; data/b754_agenda.txt :558-:560)' % AGENDA['rev'],
                        (len(mr['fbody']), ff, len(mr['obody']), of),
                        (AGENDA['f_lines'], AGENDA['f_bytes'], AGENDA['o_lines'], AGENDA['o_bytes'])))
        out.append(case('RECORD: every listed heading read at its ledger line (FINDINGS, OPEN_TRAILS: listed = agreeing)',
                        tuple(a == b for a, b in (cite_check(rc[NAMES[0]], mr['F'], 'FINDINGS'), cite_check(rc[NAMES[1]], mr['O'], 'OPEN_TRAILS'))),
                        (True, True)))
    except Refuse as e:
        out.append(case('RECORD: the cut at %s' % AGENDA['rev'], 'REFUSED: %s' % e, 'built'))
    out.append('### ### **CUTS CONTROLS %d ; AS WANTED %d ; %s.**' % (len(rows), sum(rows), 'ALL AS WANTED' if all(rows) else 'NOT ALL AS WANTED'))
    return all(rows), out


def main(argv):
    act = None
    if '--act' in argv:
        i = argv.index('--act')
        act = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if not argv or argv[0] not in ('dry', 'write', 'control'):
        sys.exit(__doc__)
    try:
        if argv[0] == 'control':
            ok, out = control()
            print(NL.join(out))
            return 0 if ok else 1
        if argv[0] == 'dry':
            _c, fig, _m = build(argv[1] if len(argv) > 1 else 'main', act)
            print(NL.join(fig + ['  dry: nothing written']))
            return 0
        if len(argv) < 2:
            sys.exit('usage: cuts.py write <dir> [<rev>] [--act bNNN]')
        print(NL.join(write(argv[1], argv[2] if len(argv) > 2 else 'main', act)))
        return 0
    except Refuse as e:
        print('### THE CUTS REFUSED: %s -- NOTHING WRITTEN' % e)
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
