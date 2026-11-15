# -*- coding: utf-8 -*-
"""b756, (R366)(5)(i) and (3)(vi): THE TWELVE READY ORDERS READ AT TODAY'S TREE AND PLACED, AND THE TWO INSTRUMENTS ROWS DRAFTED -- the
material of Component 4's one put ((5): "one put of at most four questions before the lock"). Written by the seat; committed before its run.

THE ORDERS ((5)(i), data/b756_ferry.txt :28): the twelve the triage of b724 read as met, priced and named (relay data/b724_orders_triage.txt
:328-:376), each read at today's tree and placed in one of the ruling's four places -- DONE, with the line that did it; HERE, for tooling of
two hours or under that this act's own work touches; WITH THE BUILD, for the kernel and research orders; LATER, with its trigger written
again. Each order's state is read from PLACE-papers OPEN_TRAILS at HEAD by the standing orders tool (tools/standing/orders.py read(), its rule
printed in its own docstring), its lines after b724's trail head counted outside the roll lines; the reads that decide a place are made at
run time (a kernel's main, a standing tool's lines, the roster reader on the document an order names) and printed beside the seat's words.
The places are the seat's proposals, for the author's pass at the put; nothing here moves a status.
THE INSTRUMENTS ROWS ((3)(vi), :24): drafted in INSTRUMENTS' own row form (its entries I-108 and I-109: a heading, then **Reads.**,
**Decides.**, **Controls.**, **Validated case.**, **Range limits.**, **Entered.** in one paragraph, and a closing italic line), from the
banks the ruling names; every figure checked on the bank line it is cited at, or the draft refuses; each tool's md5 read at its commit.
Nothing is computed at any field; no kernel is written; PLACE-papers is read through git at HEAD and written nowhere.
MODES  controls | orders [--bank] | instruments [--bank]      BANKS data/b756_orders_read.txt, data/b756_instruments_draft.txt
"""
import hashlib
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import orders as OR   # noqa: E402
import roster as RO   # noqa: E402

ACT = 'b756'
PP = OR.PP
NL = '\n'
TRIAGE = 'data/b724_orders_triage.txt'
OBANK = os.path.join(RELAY, 'data', '%s_orders_read.txt' % ACT)
IBANK = os.path.join(RELAY, 'data', '%s_instruments_draft.txt' % ACT)
KERNEL = 'D:/SIDE-kernel'
PLACES = ('DONE', 'HERE', 'WITH THE BUILD', 'LATER')

# ### (name, place, the read that bears on it, the seat's words, the trigger written again for LATER)
ORDERS = (
    ('W-ORD-STORMER-CLASH', 'LATER', 'stormer',
     'a KERNEL order (its row at OT :11261): the rename is a .lean write in SIDE-kernel and a runner build, which (R366)(8) bars at this act; '
     'b724 named it a tooling act of its own, a SIDE-kernel housekeeping commit, and the build of the root question works in the criterion '
     'kernel, not SIDE-kernel, so the seat places it after the build and not in it',
     'the next act that tags SIDE-kernel (its own trigger, "the next SIDE-kernel tag", kept); the rename and its profile written there'),
    ('W-ORD-KEIPER-FACE', 'WITH THE BUILD', 'record',
     'a kernel act of two lemmas of substance (OT :11704, :12132); its place in the research order the author set at b660 (OT :14104) kept',
     None),
    ('W-ORD-LABEL-READER', 'HERE', 'label',
     'tooling: the standing reader of a document`s own version is tools/standing/roster.py version_of (v1.34.5, b754), the reader this act`s '
     'constellation rerun read the roster through (tools/b756_constellation.py :100-:104); it reads the case the order names right today, '
     'and it carries neither the order`s predicate nor its planted control: one predicate (a version after a kernel`s name on a heading is '
     'not the document`s label) and ONE_PAGE_PROOF`s kernel tag planted as its control, under two hours, a standing change with VERSION moved',
     None),
    ('W-ORD-TESTS-WITH-THE-LISTS-IN-FORCE', 'LATER', 'chain',
     'tooling of two to three hours by b724`s price, the step-zero runner`s list arguments and tools/test_chain_page.py; no work of this act '
     'touches the faces-page generator, its lists or its tests',
     'the next act that edits tools/chain_page.py or the node lists it reads, beside W-ORD-CHAIN-PAGE-B638-CASES (that order`s first clause, '
     'in place of "this finding", which every act since b650 has passed)'),
    ('W-ORD-E2-SEPARATION', 'WITH THE BUILD', 'record',
     'research grade, three lemmas of substance on the closed-form route (OT :14134); its own order behind the Epstein control, the Keiper '
     'face and the chi-Li converse kept',
     None),
    ('W-ORD-ROOT-BINARY-BANK', 'LATER', 'root',
     'tooling of 1.5 to 2 hours by b724`s price in the root route; this act banks no binary file and changes no root tool; the order`s second '
     'clause, "or the next tooling act", has been passed by every tooling act since b667',
     'the next act that banks a binary file (the order`s first clause alone)'),
    ('W-ORD-BESSEL-BOUND-TIGHTEN', 'WITH THE BUILD', 'record',
     'research: one research act counting on Q0 (OT :14388, :15108); the next count act on Q0 takes it',
     None),
    ('W-ORD-CHAIN-PAGE-B638-CASES', 'LATER', 'chain',
     'tooling, one component (b724`s price), tools/chain_page.py and its test; no work of this act touches them, and the generator is '
     'unedited since before the order`s entry',
     'the next act that edits tools/chain_page.py or the node lists it reads (its own first clause; the census clause passed at b680)'),
    ('W-ORD-LEDGER-SPLIT-RESOLVER', 'DONE', 'cuts',
     'the order priced a line-offset table and a resolver for a cut that moves the ledger`s lines, its trigger the author`s word "when '
     'FINDINGS` size asks for it"; the author`s pass of (R364)(5)[M2] at b754 met that size with two cuts written beside the archive, the '
     'ledgers not split, no line moving and no cite changing (tools/standing/cuts.py :5-:6, :13; data/b754_author_answers.txt :153), so the '
     'three readers the resolver was for read the ledger itself and no cite needs resolving. The navigator`s reading, HERE against cuts.py, '
     'is printed beside: what HERE would build is no part of the order as written',
     None),
    ('W-ORD-CORRESPONDENCE-BEHIND-SCOPE', 'LATER', 'corr',
     'tooling of three to five hours by b724`s price; its part (2) marks rows on their pages as hand cells, an edit of a paper (R366)(8) bars; '
     'its part (1), the behind count, stands in act tools of the reading acts and not in tools/correspondence_gen.py or in this act`s '
     'constellation rerun, which reads the tables` declarations at their pins and at main and counts no behind. The navigator`s reading, '
     'HERE beside (4)(i), is printed beside',
     'the next re-cut act of a document carrying a Correspondence table (its own trigger, "the next re-cut act after b691", written as the '
     'prose pass and the re-cuts (4)(iii) names)'),
    ('W-ORD-B518-FLOAT', 'WITH THE BUILD', 'record',
     'research: b518`s float route read again at a = 14.106736 against b694`s ball, a computation at a field, which (R366)(8) bars here',
     None),
    ('W-ORD-EXPLICIT-FORMULA-C1', 'WITH THE BUILD', 'record',
     'a kernel order of seven dispatches at the least, a branch of SIDE-explicit-formula (OT :15408); (R366)(8) bars Lean and dispatch here',
     None),
)


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace('\r', '')


def lines_at(repo, rev, path):
    rc, out = git(repo, 'show', '%s:%s' % (rev, path))
    return None if rc else out.split(NL)


def triage_rows():
    L = open(os.path.join(RELAY, TRIAGE), encoding='utf-8').read().replace('\r', '').split(NL)
    out = {}
    for k, (n, *_r) in enumerate(ORDERS):
        at = 329 + 4 * k
        out[n] = (at, L[at - 1].startswith('  %s -- TRIGGER MET' % n) and L[at + 2].lstrip().startswith('price:'))
    return L, out


def trail_state():
    _, head = git(PP, 'rev-parse', 'HEAD')
    O = OR.trail('HEAD')
    rows = dict(OR.read(O))
    b724 = next((k for k, l in enumerate(O, 1) if re.match(r'^### b724 — lane two', l)), None)
    after = {}
    for n, *_r in ORDERS:
        after[n] = [k for k in range(b724 or 1, len(O) + 1) if n in O[k - 1] and not O[k - 1].lstrip().startswith(OR.ROLL)]
    return head.strip(), O, rows, b724, after


def reads():
    """the reads at today's tree that bear on a place, each a printed line."""
    R = {}
    _, kh = git(KERNEL, 'rev-parse', '--short=7', 'main')
    _, g = git(KERNEL, 'grep', '-n', 'def divideOut', 'main', '--', 'Kernel/Stormer.lean', 'Kernel/StormerTest.lean')
    hits = [x.split(':', 1)[1] for x in g.split(NL) if x.strip()]
    R['stormer'] = ('SIDE-kernel main %s: `def divideOut` at %s -- the clash stands' % (kh.strip(), ', '.join(':'.join(h.split(':')[:2]) for h in hits)),
                    len([h for h in hits if h.startswith('Kernel/StormerTest.lean')]) >= 1 and len([h for h in hits if h.startswith('Kernel/Stormer.lean')]) >= 1)
    opp = lines_at(PP, 'HEAD', 'day1/ONE_PAGE_PROOF.md') or []
    k, v = RO.version_of(opp)
    plant = RO.version_of(['# ONE PAGE PROOF', '', '## The proof at SIDE-kernel v1.7'])
    R['label'] = ('roster.version_of over day1/ONE_PAGE_PROOF.md at PLACE-papers HEAD: its own version line :%s, v%s (the label the order '
                  'names); over a planted heading "## The proof at SIDE-kernel v1.7": v%s, a kernel`s tag read as a label -- the predicate absent'
                  % (k, '.'.join(map(str, v or ())), '.'.join(map(str, plant[1] or ()))), k == 5 and v == (1, 0, 1) and plant[1] == (1, 7))
    cu = open(os.path.join(T, 'standing', 'cuts.py'), encoding='utf-8').read().split(NL)
    ok = 'the ledgers themselves are not split, no line of them moves and no cite changes' in cu[5] and 'a line of the ledger and not of' in cu[12]
    R['cuts'] = ('tools/standing/cuts.py :6 "the ledgers themselves are not split, no line of them moves and no cite changes"; :13 a cite '
                 'FINDINGS :N or OPEN_TRAILS :N is a line of the ledger and not of the cut', ok)
    rf = [f for f in git(RELAY, 'ls-files', 'tools/standing')[1].split(NL) if 'root' in os.path.basename(f) and f.endswith(('.py', '.tpl'))] + ['tools/act_root.py']
    nb = 0
    for f in rf:
        nb += sum(1 for l in (lines_at(RELAY, 'HEAD', f) or []) if re.search(r'(?i)binary', l))
    R['root'] = ('the root tools at relay HEAD (%s): lines naming a binary bank %d -- no declared binary-bank list' % (', '.join(rf), nb), nb == 0)
    cg = sum(1 for l in (lines_at(RELAY, 'HEAD', 'tools/correspondence_gen.py') or []) if re.search(r'(?i)behind', l))
    rd = sum(1 for l in (lines_at(RELAY, 'HEAD', 'tools/b700_readings.py') or []) if re.search(r'(?i)behind', l))
    R['corr'] = ('tools/correspondence_gen.py lines naming the behind count %d; tools/b700_readings.py (the reading act`s tool) %d' % (cg, rd), cg == 0 and rd > 0)
    _, cl = git(RELAY, 'log', '-1', '--format=%h %cI', '--', 'tools/chain_page.py')
    R['chain'] = ('tools/chain_page.py last committed %s, before OT :14586`s entry (2026-10-17)' % cl.strip(), cl.strip()[9:19] < '2026-10-17')
    R['record'] = ('the order`s state as the orders tool reads it, printed above; no line after b724`s trail head names it outside a roll line', True)
    return R


def controls():
    out = []
    L, tri = triage_rows()
    out.append(('the twelve names at data/b724_orders_triage.txt :329-:376, each with its price line', all(ok for _, ok in tri.values()) and len(tri) == 12, True))
    head, O, rows, b724, after = trail_state()
    out.append(('each of the twelve OPEN at PLACE-papers HEAD by the orders tool', all(rows.get(n, {}).get('status') == 'OPEN' for n, *_r in ORDERS), True))
    planted = O + ['*Planted, b756:* `W-ORD-STORMER-CLASH` DISCHARGED by the planted line.']
    out.append(('a planted closing line reads the order CLOSED (in memory)', dict(OR.read(planted))['W-ORD-STORMER-CLASH']['status'] == 'CLOSED', True))
    out.append(('b724`s trail head read once in OPEN_TRAILS', b724 is not None, True))
    out.append(('each order in one of the four places, the counts 1 DONE, 1 HERE, 5 WITH THE BUILD, 5 LATER',
                [sum(1 for o in ORDERS if o[1] == p) for p in PLACES] == [1, 1, 5, 5] and all(o[1] in PLACES for o in ORDERS), True))
    out.append(('a LATER order carries its trigger written again, and no other does', all((o[1] == 'LATER') == bool(o[4]) for o in ORDERS), True))
    R = reads()
    out.append(('every read that decides a place as wanted (%d)' % len(R), all(ok for _, ok in R.values()), True))
    rc, _ = git(KERNEL, 'grep', '-n', 'def divideOutPLANTED', 'main')
    out.append(('a planted needle at SIDE-kernel main reads no hit', rc == 1, True))
    cs = [check_fig(b, l, t) for b, l, t in FIGS]
    out.append(('every figure of the two drafts on its cited bank line (%d)' % len(FIGS), all(cs), True))
    out.append(('a planted figure refused', not check_fig('data/b755_walk.txt', 197, '763'), True))
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    good = sum(1 for _, a, b in out if a == b)
    print('### CONTROLS %d OF %d AS WANTED' % (good, len(out)))
    return good == len(out)


def orders_bank():
    L, tri = triage_rows()
    head, O, rows, b724, after = trail_state()
    R = reads()
    out = ['b756 -- (R366)(5)(i): THE TWELVE READY ORDERS READ AT TODAY`S TREE, EACH PLACED DONE, HERE, WITH THE BUILD OR LATER (%s)' % stamp(), '',
           '### by tools/b756_orders.py, committed before its run. THE FOUR PLACES, as (R366)(5)(i) gives them (data/b756_ferry.txt :28): DONE, with',
           '### the line that did it; HERE, for tooling of two hours or under that this act`s own work touches; WITH THE BUILD, for the kernel and',
           '### research orders; LATER, with its trigger written again. Each order`s state is the standing orders tool`s at PLACE-papers HEAD %s' % head[:8],
           '### (tools/standing/orders.py read(), its rule in its docstring); its lines after b724`s trail head (OPEN_TRAILS :%s) counted outside the' % b724,
           '### roll lines. The places are the seat`s proposals for the author`s pass at the put; on the pass the statuses move by the orders tool`s',
           '### route and the HERE work is done. A ledger line is cited by its number; no line of a paper is quoted.', '']
    for k, (n, place, rk, words, trig) in enumerate(ORDERS, 1):
        o = rows.get(n, {})
        at, _ok = tri[n]
        out.append('  (%d) %s -- %s' % (k, n, place))
        out.append('      the record: entry OT :%s ; %s%s ; named %s ; lines after b724`s trail head outside a roll line %d' % (
            o.get('entry'), o.get('status'), (' (its last status line :%s %s)' % (o.get('decided_at'), o.get('why'))) if o.get('decided_at') else ' (no status line after its entry)',
            o.get('named'), len(after[n])))
        out.append('      b724`s triage: %s :%d-:%d (trigger, reading, price)' % (TRIAGE, at, at + 3))
        ok = (len(after[n]) == 0 and o.get('status') == 'OPEN') if rk == 'record' else R[rk][1]
        out.append('      at today`s tree: %s -- %s' % (R[rk][0], 'AS READ' if ok else '### NOT AS READ'))
        out.append('      the seat: %s' % words)
        if trig:
            out.append('      the trigger written again: %s' % trig)
        out.append('')
    cnt = [sum(1 for o in ORDERS if o[1] == p) for p in PLACES]
    out.append('### ### **THE TWELVE ORDERS AT TODAY`S TREE: DONE %d ; HERE %d ; WITH THE BUILD %d ; LATER %d ; OPEN BY THE ORDERS TOOL AT PLACE-papers %s %d OF 12 ; '
               'THE HERE WORK W-ORD-LABEL-READER, ONE PREDICATE AND ITS PLANTED CONTROL, UNDER TWO HOURS.**' % (
                   cnt[0], cnt[1], cnt[2], cnt[3], head[:8], sum(1 for n, *_r in ORDERS if rows.get(n, {}).get('status') == 'OPEN')))
    return out


# ================================================================================ (3)(vi): THE TWO INSTRUMENTS ROWS
FIGS = (
    ('data/b755_walk.txt', 196, 'absolute value at most 12'), ('data/b755_walk.txt', 196, 'the primes below 20000 not dividing D'),
    ('data/b755_walk.txt', 197, 'x^3 - x - 1 (of 38 found)'), ('data/b755_walk.txt', 197, 'primes compared 2261'),
    ('data/b755_walk.txt', 197, 'no root 762'), ('data/b755_walk.txt', 197, 'split, not by Q1 762'), ('data/b755_walk.txt', 197, 'MISMATCHES 0'),
    ('data/b755_walk.txt', 208, '(of 6 found)'), ('data/b755_walk.txt', 234, 'THE SECOND ROUTE: A CUBIC AT 16 OF 16, MISMATCHES 0'),
    ('data/b755_walk.txt', 14, 'x^3 - 2 planted (discriminant -108): mismatches 1014'), ('data/b755_walk.txt', 19, '2, 3, 13'),
    ('data/b755_walk.txt', 196, 'a control of the enumeration and no test of the law'),
    ('data/b755_registrations.txt', 53, 'sum of (-log(1 - p^(-s)) + log(1 - p^(-3s))/3)'),
    ('data/b755_registrations.txt', 56, '(1/3) E1((s - 1) log P) + (1/6) E1((2s - 1) log P)'),
    ('data/b755_registrations.txt', 55, 'P = 10^4, real part from 0.80 to 1.30 by 0.01'), ('data/b755_registrations.txt', 56, 'P = 3 x 10^5'),
    ('data/b755_registrations.txt', 57, '10^(-9)'), ('data/b755_registrations.txt', 62, 'the sums not converging absolutely to the left of Re s = 1'),
    ('data/b755_cand_h_scan_23.txt', 16, 'ROOTS 18, THE MATCH ONE TO ONE'), ('data/b755_cand_h_scan_15.txt', 18, 'ROOTS 24, THE MATCH ONE TO ONE'),
    ('data/b755_cand_h_plant.txt', 66, 'EACH PLANT BREAKS THE MATCH'),
    ('data/b755_cand_h.txt', 9, 'zero 0.953260 + 16.290216 i -> root 0.953362 + 16.290141 i ; distance 0.00013 ; |f| 2.8e-14'),
    ('data/b755_cand_h.txt', 50, 'EVERY ZERO FOUND WITHIN 0.02'), ('data/b755_cand_h.txt', 1, 'NEWTON FROM EACH BANKED ZERO WITH THE TAIL'),
    ('data/b755_roots_59.txt', 8, 'ROOTS WITH Re >= 0.85 0, WITH Re IN [0.83, 0.85) 1'),
    ('data/b755_zeros_from_primes_59.txt', 13, 'HELD ; ZEROS WITH Re >= 0.85 0 AGAINST ROOTS 0'),
)


def check_fig(bank, line, token):
    try:
        L = open(os.path.join(RELAY, bank), encoding='utf-8').read().replace('\r', '').split(NL)
    except OSError:
        return False
    return 1 <= line <= len(L) and token in L[line - 1]


def md5_at(rev, path):
    r = subprocess.run(['git', '-C', RELAY, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return hashlib.md5(r.stdout).hexdigest() if r.returncode == 0 else None


def instruments_bank(date):
    m1, m2 = md5_at('3bdb6561', 'tools/b755_coeffs.py'), md5_at('1b84e4b1', 'tools/b755_zlist.py')
    if not m1 or not m2:
        raise SystemExit('### A TOOL NOT READ AT ITS COMMIT -- NOTHING DONE')
    r1 = [
        '## I-110 — THE THREE PRIMES BY A CUBIC OF DISCRIMINANT D, A SECOND ROUTE BESIDE THE ENUMERATION (entered %s by b756, under `(R366)`(3)(vi) and the author’s pass at (5)(iii); built by b755 under `(R365)`(3); provenance: relay data/b755_walk.txt :196)' % date,
        '',
        '**Reads.** Nothing external: for each discriminant D of the walk’s sixteen rows (the registration’s fourteen and the control rows −23 and −31), a monic cubic with integer coefficients of absolute value at most 12, discriminant D and no integer root, the first found in the order |a|, |b| + |c|, a, b, c; the primes below 20000 not dividing D (relay data/b755_walk.txt :196). '
        '**Decides.** For each such prime, whether the cubic has a root modulo it, beside whether the prime splits and the principal form Q1 does not represent it: at −23, x^3 − x − 1 (of 38 found) over 2261 primes, no root at 762 and split, not represented by Q1 at 762, mismatches 0 (:197); at the sixteen rows, mismatches 0 (:234, “THE SECOND ROUTE: A CUBIC AT 16 OF 16, MISMATCHES 0”). '
        '**Controls.** (CC) x^3 − 2 planted at −23 (discriminant −108): mismatches 1014, the plant failing as wanted (:14). '
        '**Validated case.** D = −23: x^3 − x − 1, 762 primes with no root against 762 split and not represented by Q1, mismatches 0 (:197); the three least such primes 2, 3, 13, the row’s (:19). '
        '**Range limits.** Discriminants with a cubic of discriminant D found under the coefficient bound 12 (38 found at −23, :197; 6 at −499, :208); primes below 20000; a control of the enumeration of the three primes and no test of the coefficient law (:196). '
        '**Entered.** relay `tools/b755_coeffs.py` (md5 `%s` at its commit), committed at relay `3bdb6561` before its run, its bank data/b755_walk.txt at `9a989df8`; its route run by `python -X utf8 -u tools/b755_coeffs.py walk dry` (it prints; without `dry` it writes data/b755_walk.txt and .json).' % m1,
        '',
    ]
    r2 = [
        '## I-111 — THE ROOTS OF 1 + 2 exp(−3 T_P(s)) FROM THE PRIMES, WITH THE TAIL TERM, BESIDE THE CERTIFIED ZEROS (entered %s by b756, under `(R366)`(3)(vi) and the author’s pass at (5)(iii); built by b755 under `(R365)`(4)(h) and (5)(ii); provenance: relay data/b755_registrations.txt :52)' % date,
        '',
        '**Reads.** Nothing external: at class number 3, the primes p up to P that split in Q(√D) and are not represented by the principal form, T_P(s) the sum of (−log(1 − p^(−s)) + log(1 − p^(−3s))/3) over them (relay data/b755_registrations.txt :53-:54), and the tail term (1/3) E1((s − 1) log P) + (1/6) E1((2s − 1) log P) (:56). '
        '**Decides.** The roots of 1 + 2 exp(−3 T_P(s)): its modulus scanned at P = 10^4, real part from 0.80 to 1.30 by 0.01 and height from 2 to H by 0.01, each local minimum under 0.3 refined by Newton’s method at P = 3 x 10^5 with the tail added, the step capped at 0.05, a root kept where the modulus falls under 10^(−9) (:54-:57); and, from each zero of a banked certified list, the root Newton’s method reaches with the tail and its distance (relay data/b755_cand_h.txt :1). '
        '**Controls.** The route at −23 to height 200: roots 18, the match one to one (relay data/b755_cand_h_scan_23.txt :16); at −15 to 199.33: roots 24, the match one to one (data/b755_cand_h_scan_15.txt :18); the tail dropped at −23 and at −15, and a weight planted at −15: each plant breaks the match (data/b755_cand_h_plant.txt :66). '
        '**Validated case.** D = −23: the banked zero 0.953260 + 16.290216 i reaches the root 0.953362 + 16.290141 i, distance 0.00013, |f| 2.8e-14 (data/b755_cand_h.txt :9); every banked zero of real part 0.80 and above at −23 and −15 found within 0.02 (:50). '
        '**Range limits.** The sums do not converge absolutely to the left of Re s = 1, and no sentence says why roots and zeros meet (data/b755_registrations.txt :62); the truncation at P; at −59 to height 200 the list holds no root of real part 0.85 and above and one in [0.83, 0.85) (data/b755_roots_59.txt :8) and the certified list no zero there, so the registered test read HELD with its population empty, a vacuous pass (data/b755_zeros_from_primes_59.txt :13). '
        '**Entered.** relay `tools/b755_zlist.py` (md5 `%s` at its commit), committed at relay `1b84e4b1` before any run, its verdict mode added at `2b4a3942` before any band ran; its banks data/b755_cand_h.txt at `ea99215e` and data/b755_roots_59.txt at `e21b5c8c`; its modes `banked`, `plant`, `scan <D> <H>`, `list -59 <H> <commit>` and `verdict -59 200` (its docstring :20-:32), each writing its own bank.' % m2,
        '',
        '*Entered %s by b756 under `(R366)`(3)(vi) and the author’s pass at (5)(iii), after I-109; no entry above is edited. Nothing deposits.*' % date,
    ]
    head = ['b756 -- (R366)(3)(vi): TWO ROWS FOR THE INSTRUMENTS LEDGER, DRAFTED IN ITS OWN ROW FORM FROM THE BANKS, FOR THE PUT OF (5)(iii) (%s)' % stamp(), '',
            '### by tools/b756_orders.py, committed before its run. The form: INSTRUMENTS` I-108 and I-109 (a heading; **Reads.**, **Decides.**,',
            '### **Controls.**, **Validated case.**, **Range limits.**, **Entered.** in one paragraph; a closing italic line). Every figure checked on',
            '### the bank line it is cited at (%d of %d); each tool`s md5 read at its commit. Entered in INSTRUMENTS only on the author`s pass, as' % (
                sum(1 for b, l, t in FIGS if check_fig(b, l, t)), len(FIGS)),
            '### drafted here; the two rows below are the lines that would be appended at the file`s end, each with a blank line before it.', '']
    return head + r1 + r2 + ['', '### ### **TWO ROWS DRAFTED, I-110 AND I-111, AFTER I-109 ; FIGURES ON THEIR LINES %d OF %d ; FOR THE AUTHOR`S PASS AT (5)(iii).**' % (
        sum(1 for b, l, t in FIGS if check_fig(b, l, t)), len(FIGS))]


def write(path, L):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(NL.join(L) + NL)
    os.replace(tmp, path)


def main(argv):
    step = argv[0] if argv else ''
    if step == 'controls':
        return 0 if controls() else 1
    if step not in ('orders', 'instruments'):
        sys.exit(__doc__)
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    L = orders_bank() if step == 'orders' else instruments_bank(stamp()[:10])
    print(NL.join(L))
    if '--bank' in argv:
        path = OBANK if step == 'orders' else IBANK
        if os.path.exists(path):
            raise SystemExit('### %s STANDS ALREADY -- NOTHING WRITTEN' % os.path.relpath(path, RELAY))
        write(path, L)
        print('### BANKED %s at %s' % (os.path.relpath(path, RELAY), stamp()))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
