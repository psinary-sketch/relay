# -*- coding: utf-8 -*-
"""tools/b752_crossref.py -- (R362)(3): THE CROSS-REFERENCE. The six questions the navigator listed on 2026-11-10, each against the order or
finding that holds it: every corpus line the ruling cites re-read at PLACE-papers HEAD (or the relay's) and printed; every figure the ruling
attaches to a line searched for in that line, FOUND or NOT IN THE LINE; each order's state read by tools/standing/orders.py. A bank of this act
and no ledger: no order entered, no candidate written as an entry. Written at b752 by the Write tool; no identifier of the author read into any
string here; day1/Which_Structure_Confines.md :3 is not read.

  python -X utf8 -u tools/b752_crossref.py [--bank]      data/b752_crossref.txt
"""
import io
import os
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import orders as OR   # noqa: E402

PATHS = 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md'


def show(repo, rel, rev='HEAD'):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, rel)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL) if not r.returncode else None


HEADS = dict(pp=subprocess.run(['git', '-C', PP, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()[:8],
             relay=subprocess.run(['git', '-C', RELAY, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()[:8])
TRAIL = OR.trail('HEAD')
FILES = {('pp', 'OPEN_TRAILS.md'): TRAIL, ('pp', PATHS): show(PP, PATHS), ('relay', 'data/b723_dial_price.txt'): show(RELAY, 'data/b723_dial_price.txt'),
         ('pp', 'FINDINGS.md'): show(PP, 'FINDINGS.md')}
ORD = dict(OR.read(TRAIL))
# ### the state the ruling's words give each order it names ((R362)(3)), set beside the tool's: OPEN for "entered", "priced", "open on it",
# ### "priced, not started"; CLOSED for "discharged"
RULING_STATE = {'W-ORD-LI-ARITH': 'OPEN', 'W-ORD-KEIPER-FACE': 'OPEN', 'W-ORD-ZQ-FAMILY': 'OPEN', 'W-ORD-MECHANISM-TABLE': 'OPEN',
                'W-ORD-PLATT-RUNG': 'OPEN', 'W-ORD-ZETA-BOX': 'CLOSED', 'W-ORD-ADMISSIBLE-CONE': 'OPEN', 'W-ORD-QUASI-RH-FIELD-WATCH': 'OPEN',
                'W-ORD-MECHANISM-ATTRIBUTION': 'OPEN'}


def squash(s):
    """a figure compared with its line with the white space taken out of both (the line's "σ=1" is the ruling's "σ = 1")."""
    return ''.join((s or '').split())

# ### (question, title, the ruling's reading, [(repo, file, line, needle, [figures the ruling attaches])], [orders named], the ruling's class)
Q = [
    (1, 'a named n with a negative Li coefficient of Z_Q0', 'W-ORD-LI-ARITH, entered b743, with W-ORD-KEIPER-FACE beside it',
     [('pp', 'OPEN_TRAILS.md', 17714, 'W-ORD-LI-ARITH', ['b743'])], ['W-ORD-LI-ARITH', 'W-ORD-KEIPER-FACE'], 'HELD'),
    (2, 'Re ρ < 1 certified by a tighter box', 'no order; the candidate of OPEN_TRAILS :18148; the numerical narrowing of b671 named as numerics',
     [('pp', 'OPEN_TRAILS.md', 18148, 'candidate', ['W-ORD-ZQ-FAMILY']), ('pp', 'OPEN_TRAILS.md', 14396, 'b671', ['146', '17', '10'])], [], 'CANDIDATE'),
    (3, 'where zeros leave the line in ζ_K + t·L(s, ψ)', 'no such object in the corpus; beside it H-DIAL (registered b723, priced and not run), W-ORD-ZQ-FAMILY and W-ORD-MECHANISM-TABLE`s row; a candidate, as an instance under that table',
     [('relay', 'data/b723_dial_price.txt', None, 'H-DIAL', ['b723']), ('pp', 'OPEN_TRAILS.md', 17716, 'W-ORD-ZQ-FAMILY', ['b743']),
      ('pp', 'OPEN_TRAILS.md', 16589, 'W-ORD-MECHANISM-TABLE', ['b725'])], ['W-ORD-ZQ-FAMILY', 'W-ORD-MECHANISM-TABLE'], 'CANDIDATE'),
    (4, 'the 3-4-1 argument in general form', 'A9, B3, C1 of PATHS_TO_THE_CRITICAL_LINE, as in (R362)(2)(i)',
     [('pp', PATHS, 389, 'A9', ['vonMangoldt', 'σ = 1']), ('pp', PATHS, 396, 'B3', ['Λ≥0 → σ']), ('pp', PATHS, 410, 'C1', ['σ = 1'])], [], 'HELD'),
    (5, 'Turing`s method inside a proof assistant', 'no order; beside it W-ORD-PLATT-RUNG (priced, not started, the verification imported as a cited premise) and W-ORD-ZETA-BOX (discharged); a candidate, a horizon item',
     [('pp', 'OPEN_TRAILS.md', 12891, 'PLATT', ['b623']), ('pp', 'OPEN_TRAILS.md', 15074, 'W-ORD-PLATT-RUNG', ['DISCHARGED']),
      ('pp', 'FINDINGS.md', 7567, 'W-ORD-PLATT-RUNG', ['PlattRung.lean', 'rh_upto_platt', 'INTERFACES'])], ['W-ORD-PLATT-RUNG', 'W-ORD-ZETA-BOX'], 'CANDIDATE'),
    (6, 'the weakest arithmetic premise that gives positivity', 'B3`s sign layer, with W-ORD-ADMISSIBLE-CONE (Q0`s exit direction), W-ORD-QUASI-RH-FIELD-WATCH (the Davenport-Heilbronn discriminator), W-ORD-MECHANISM-TABLE and W-ORD-MECHANISM-ATTRIBUTION open on it',
     [('pp', PATHS, 396, 'B3', []), ('pp', 'OPEN_TRAILS.md', 16591, 'W-ORD-ADMISSIBLE-CONE', ['exit direction']),
      ('pp', 'OPEN_TRAILS.md', 15502, 'QUASI-RH-FIELD-WATCH', ['Davenport']), ('pp', 'OPEN_TRAILS.md', 17932, 'MECHANISM-ATTRIBUTION', ['b747'])],
     ['W-ORD-ADMISSIBLE-CONE', 'W-ORD-QUASI-RH-FIELD-WATCH', 'W-ORD-MECHANISM-TABLE', 'W-ORD-MECHANISM-ATTRIBUTION'], 'HELD'),
]


def line_of(repo, f, ln, needle):
    L = FILES.get((repo, f))
    if L is None:
        return None, None
    if ln is None:
        ln = next((i for i, l in enumerate(L, 1) if needle in l), None)
        if ln is None:
            return None, None
    return ln, (L[ln - 1] if ln <= len(L) else None)


def order_line(n):
    o = ORD.get(n)
    if not o:
        return ['%s: NOT AN ORDER OF THE TRAIL (orders.py at PLACE-papers %s)' % (n, HEADS['pp'])]
    rs = RULING_STATE.get(n)
    L = ['%s: %s ; entered :%d ; the status line :%s ; closed :%s%s ; the ruling`s words read %s -- %s' % (
        n, o['status'], o['entry'], o['decided_at'] or '-', o['closed_at'] or '-', ' ; reopened :%d' % o['reopened_at'] if o['reopened_at'] else '',
        rs or '-', 'AGREES' if rs == o['status'] else '### DIFFERS')]
    for at, what in ((o['entry'], 'its entry by the tool'), (o['decided_at'], 'its status line')):
        if at:
            l = TRAIL[at - 1]
            L.append('        %s :%d | %s' % (what, at, l if len(l) <= 300 else l[:300] + ' [cut at 300 of %d]' % len(l)))
    return L


def main(argv):
    out = ['b752 -- THE CROSS-REFERENCE, (R362)(3): THE SIX QUESTIONS AGAINST THE ORDERS AND FINDINGS THAT HOLD THEM (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
           '### a bank of this act and no ledger; every corpus line the ruling cites re-read at PLACE-papers HEAD %s or relay HEAD %s and printed (to 600 characters, '
           'cut marked); each figure the ruling attaches searched for in its line; each order`s state by tools/standing/orders.py (v1.32.0) over OPEN_TRAILS at HEAD, '
           '%d orders, %d open. No order entered; no candidate written as an entry; entering any is the author`s word at a sitting.' % (
               HEADS['pp'], HEADS['relay'], len(ORD), sum(1 for o in ORD.values() if o['status'] == 'OPEN')), '']
    bad, held, cand = [], 0, 0
    for k, title, reading, cites, ords, cls in Q:
        out += ['## [%d] %s' % (k, title), '  the ruling`s reading: %s ; its class: %s' % (reading, cls)]
        for repo, f, ln, needle, figs in cites:
            at, l = line_of(repo, f, ln, needle)
            ok = l is not None and needle in l
            out.append('  %s %s :%s -- the needle %r %s' % ('PLACE-papers' if repo == 'pp' else 'relay', f, at or '?', needle, 'IN THE LINE' if ok else '### NOT IN THE LINE'))
            if not ok:
                bad.append('[%d] %s :%s needle %r' % (k, f, at, needle))
            if l is not None:
                out.append('      | %s' % (l if len(l) <= 600 else l[:600] + ' [cut at 600 of %d]' % len(l)))
            for fg in figs:
                fo = l is not None and squash(fg) in squash(l)
                out.append('      figure %r: %s' % (fg, 'FOUND' if fo else '### NOT IN THE LINE'))
                if not fo:
                    bad.append('[%d] %s :%s figure %r' % (k, f, at, fg))
        for n in ords:
            ol = order_line(n)
            out += ['  order ' + ol[0]] + ol[1:]
            if n not in ORD:
                bad.append('[%d] %s not an order' % (k, n))
            elif RULING_STATE.get(n) != ORD[n]['status']:
                bad.append('[%d] %s: the ruling`s words read %s, the trail %s at :%s' % (k, n, RULING_STATE.get(n), ORD[n]['status'], ORD[n]['decided_at']))
        held += cls == 'HELD'
        cand += cls == 'CANDIDATE'
        out.append('')
    note = []
    if any('W-ORD-PLATT-RUNG' in b for b in bad):
        note = ['  [5]: the ruling`s "priced, not started" are the entry`s own words (:12891); the order was built and discharged: SIDE-explicit-formula v0.22 '
                '(e939c92) adds SIDEExplicitFormula/PlattRung.lean, rh_upto_platt at T = 3·10¹² INTERFACES on the structure PlattTrudgianHeight T, the verification '
                'entering as a named premise (FINDINGS :7567), and b692 discharged the order by that reading (:15074). The question [5] asks, Turing`s method inside a '
                'proof assistant, is not what the rung built: the rung imports the verification and does not run it. The class the ruling gives [5] (a candidate) is '
                'printed as given; the reading of PLATT-RUNG beside it is the trail`s.']
    out += ['## THE READS THAT DID NOT MATCH THE RULING`S CITE (printed, none repaired): %s' % ('; '.join(bad) if bad else 'NONE')] + note + ['',
            '## BY THE AUTHOR`S WORD OF 2026-11-10 TO THE NAVIGATOR (entered by (R362)`s delivery): open questions are filed in OPEN_TRAILS and the clusters and not as an outward '
            'list; the translation table, the statement sheets and the figures go to the prose pass at b760, where a problem list in the paper is decided; no pull request to Mathlib '
            'is proposed, planned or priced; the kernels keep the field`s conventions as practice.', '',
            '### ### **THE CROSS-REFERENCE: QUESTIONS 6 ; HELD %d ; CANDIDATES %d ; CITES NOT MATCHED %d ; NO ORDER ENTERED.**' % (held, cand, len(bad))]
    print(NL.join(out))
    if '--bank' in argv:
        text = NL.join(out) + NL
        io.open(os.path.join(RELAY, 'data', 'b752_crossref.txt'), 'w', encoding='utf-8', newline='\n').write(text)
        print('written data/b752_crossref.txt (%d lines)' % text.count(NL))


if __name__ == '__main__':
    main(sys.argv[1:])
