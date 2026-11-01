# -*- coding: utf-8 -*-
"""standing/v1120.py -- THE CONTROLS OF v1.12.0 ((R342)(2)(i)-(iv)), in v1110.py's form: each instance read through the route as it stood before the repair (at BASE, the commit before this version) and through
the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side. Written at b732 by the Write tool.

  python -X utf8 tools/standing/v1120.py control [module|reprice|leanpath|n3 ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v1120.txt with every control run, nothing else.
"""
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import actmodule as AM          # noqa: E402
import cites as CT              # noqa: E402
import fold as F                # noqa: E402
import pricebank as PB          # noqa: E402
import reportdry as RD          # noqa: E402

BASE = '9aa8e011'               # ### relay's step-zero tip: every route of v1.11.0 as it stood
EF = 'D:/SIDE-explicit-formula'
ZQ_TIP = '23b006df'             # ### zq-b730 at b731's close, the tip the rows of (R342) read
LOCK_BLOB = 'd7a0c14e'          # ### tools/acts/b731.py at the lock, the index line of b731 event (3)
RESTORED_BLOB = '94062937'      # ### the same after the author's word
B731_CARRIED = '64f0d801'       # ### b731's step-zero tip: its module as carried, the function standing
SPLIT = re.compile(r'(?<=[.;])\s+')


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rd(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def base(rel):
    return _git('show', '%s:%s' % (BASE, rel))


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.11.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.12.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.12.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def control_module():
    L, g, n = ['### (module) THE ACT MODULE RENDERED, THE DROPPED NAME FAILING THE PRE-LOCK DRY, (R342)(2)(i); THE INSTANCE, b731`S MODULE AT ITS LOCK AND research_reproduces_ok'], 0, 0
    bad = _git('cat-file', '-p', LOCK_BLOB)
    good = _git('cat-file', '-p', RESTORED_BLOB)
    sb, ob = F._parse('b731', bad)
    sg, og = F._parse('b731', good)
    rb, rg = RD.rendered('b731', sb, ob), RD.rendered('b731', sg, og)
    oldrep = RD.undefined(F.render('b731', 'report', sb, ob))
    n += 1
    g += case(L, 'module', 'blob %s, tools/acts/b731.py as the lock took it; its checks tool %d lines' % (LOCK_BLOB, rb['checks'][2]),
              'report dry read the report tool alone: undefined %s, CLEAN, and the lock passed; the name surfaced at the pre-run, 15:49Z, and `close.py dry` refused at about 16:38Z (b731 event (1)); `unbound` at BASE: %s' % (oldrep or 'NONE', 'def unbound' in base('tools/standing/reportdry.py')),
              'the seven tools read before any lock: live %s' % sorted((t, x) for t, v in rb.items() for x in v[0]),
              not oldrep and 'def unbound' not in base('tools/standing/reportdry.py'), [(t, x) for t, v in rb.items() for x in v[0]] == [('checks', 'research_reproduces_ok')])
    n += 1
    g += guard(L, 'module', 'blob %s, after the author`s word: no live name in any of the seven' % RESTORED_BLOB, 'live %s ; printed as a dead route %s' % (sorted((t, x) for t, v in rg.items() for x in v[0]), sorted((t, x) for t, v in rg.items() for x in v[1])),
               not any(v[0] for v in rg.values()))
    carried = _git('show', '%s:tools/acts/b731.py' % B731_CARRIED)
    k = ('SECTION', 'checks', 40)
    s0, e0 = next((s, e) for key, s, e in AM.blocks(bad) if key == k)
    own = bad[s0:e0]
    drop = AM.dropped(carried, AM.compose(carried, own))
    n += 1
    g += case(L, 'module', 'the applier`s section checks 40 put over b731`s carried module, %s' % B731_CARRIED, 'the applier wrote the section whole; no render stood between it and the file: actmodule at BASE %s' % bool(base('tools/standing/actmodule.py')),
              'the render refuses, nothing written: dropped %s, read at %s' % (sorted(drop), [h[0][:80] for h in drop.values()]), not base('tools/standing/actmodule.py'), sorted(drop) == ['research_reproduces_ok'])
    same = AM.compose(carried, '')
    round_ = AM.compose(carried, carried[s0:s0] + ''.join(carried[s:e] for key, s, e in AM.blocks(carried) if key == k))
    n += 1
    g += guard(L, 'module', 'no own block leaves the module byte for byte; a block put back as it stood leaves it byte for byte', '%s ; %s' % (same == carried, round_ == carried), same == carried and round_ == carried)
    tpl = open(os.path.join(S, 'fold', 'reg_gate.tpl'), encoding='utf-8').read()
    cl = open(os.path.join(S, 'close.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'module', 'the dry stands where v1.9.0 set it: the gate writes the bank at step [5a], the seal refuses without it; a live name now fails the bank`s foot', 'in reg_gate.tpl %s ; in close.py %s ; the foot on a live name %s' % ('reportdry' in tpl, 'STEP [5a]' in cl, "'CLEAN' if ok" in open(os.path.join(S, 'reportdry.py'), encoding='utf-8').read() and 'not live' in open(os.path.join(S, 'reportdry.py'), encoding='utf-8').read()),
               'reportdry' in tpl and 'STEP [5a]' in cl and 'not live' in open(os.path.join(S, 'reportdry.py'), encoding='utf-8').read())
    return L, g, n


def control_reprice():
    L, g, n = ['### (reprice) THE RE-PRICE COMPUTED FROM THE BANKS, (R342)(2)(ii); THE INSTANCE, b731`S TWO PLANS'], 0, 0
    price, meas = rd('b729_count_price.txt'), rd('b731_price_measured.txt')
    for field, by, plan, typed, want in (('logDeriv', 'continuation', 'b731_logderiv_plan.txt', '56-223', (55, 223, 1, 2)), ('zeros', 'continuation', 'b731_zeros_plan.txt', '83-335', (83, 334, 1, 3))):
        pl = rd(plan).split(NL)[36]
        r = PB.reprice_read(price, meas, field, by)
        n += 1
        g += case(L, 'reprice', '%s by %s`s measured ratio' % (field, by), 'data/%s :37 by hand from the rounded ratios, carries %s: %s ; reprice_read at BASE: %s' % (plan, typed, typed in pl, 'reprice_read' in base('tools/standing/pricebank.py')),
                  'read from the two banks, no figure typed: %d-%d lines, %d-%d dispatches' % r, typed in pl and 'reprice_read' not in base('tools/standing/pricebank.py'), r == want)
    rows = (('count', 'logDeriv', (1572, 7860, 5, 35)), ('explicitFormula', 'zeros', (1700, 5667, 4, 16)))
    got = [(f, b, PB.reprice_read(price, meas, f, b)) for f, b, _w in rows]
    n += 1
    g += guard(L, 'reprice', 'two rows data/b731_price_measured.txt prints, :29 and :35, read back', '%s' % got, all(x[2] == r[2] for x, r in zip(got, rows)))
    try:
        PB.reprice_read(price, meas, 'nofield', 'zeros')
        ref = False
    except ValueError:
        ref = True
    n += 1
    g += guard(L, 'reprice', 'a field the banks lack raises, no figure printed', 'raises %s' % ref, ref)
    return L, g, n


def control_leanpath():
    L, g, n = ['### (leanpath) EVERY LEAN PATH A RULING NAMES AGAINST THE TREE AT THE PIN, (R342)(2)(iii); THE INSTANCE, (R341)`S Chi/Generic.lean', '  PRINTED FIRST: Chi/Generic.lean STANDS in the tree at the pin. A read of absent paths alone passes that citation; the fault is the declaration beside it, so the repair reads the declaration too.'], 0, 0
    trees = ((EF, ZQ_TIP),)
    rows = CT.lean_rows(rd('b731_ferry.txt'), trees)
    for r in rows:
        L.append('    %-5s %-44s %-60s %s' % (r[0], r[1], r[2], 'OK' if r[3] else 'HALT'))
    miss = [r for r in rows if not r[3]]
    n += 1
    g += case(L, 'leanpath', 'data/b731_ferry.txt at the pin %s, its (R341)(4) reading "zetaZeroConfig and chiZeroConfig`s form (Chi/Generic.lean)"' % ZQ_TIP, 'the check read no Lean path: lean_rows at BASE %s ; citation.tpl at BASE %s, and the b731 check read %s' % ('def lean_rows' in base('tools/standing/cites.py'), 'lean_rows' in base('tools/standing/fold/citation.tpl'), re.findall(r'\*\*CITES CHECKED[^*]*\*\*', rd('b731_citation_check.txt'))[-1:]),
              'rows %d, halts %d, among them chiZeroConfig declared at SIDEExplicitFormula/Chi/ZeroConfig.lean: %s' % (len(rows), len(miss), any('chiZeroConfig' in r[1] and 'Chi/ZeroConfig.lean' in r[2] for r in miss)),
              'def lean_rows' not in base('tools/standing/cites.py'), any('chiZeroConfig' in r[1] and 'Chi/ZeroConfig.lean' in r[2] for r in miss))
    right = CT.lean_rows('chiZeroConfig stands (Chi/ZeroConfig.lean)', trees)
    n += 1
    g += guard(L, 'leanpath', 'the same declaration beside its own file reads OK', '%s' % [(r[1], r[3]) for r in right], len(right) == 2 and all(r[3] for r in right))
    abs_ = CT.lean_rows('see Chi/NoSuchModule.lean', trees)
    n += 1
    g += guard(L, 'leanpath', 'a path no tree holds halts', '%s' % [(r[1], r[2], r[3]) for r in abs_], len(abs_) == 1 and not abs_[0][3])
    own = CT.lean_rows(rd('b732_ferry.txt'), trees)
    for r in own:
        L.append('    %-5s %-44s %-60s %s' % (r[0], r[1], r[2], 'OK' if r[3] else 'HALT'))
    n += 1
    g += guard(L, 'leanpath', 'this act`s ruling read the same way, its Lean paths each in the tree; the instance it names is the path alone and takes no declaration row', 'rows %d, halts %d' % (len(own), sum(1 for r in own if not r[3])), own and all(r[3] for r in own))
    tpl = open(os.path.join(S, 'fold', 'citation.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'leanpath', 'the check`s halt takes the rows: an absent row exits 3 where the nouns` halts did', '`if hl:` reads rows joined: %s' % ('[r[:3] for r in LN if not r[3]]' in tpl), '[r[:3] for r in LN if not r[3]]' in tpl)
    return L, g, n


def sentences(text):
    return [s for s in SPLIT.split(text) if 'Nothing here is a statement' not in s]


def control_n3():
    L, g, n = ['### (n3) THE N3 READER KEYED TO THE LANDED ENTRY`S LINES, WITH A PLANT, (R342)(2)(iv); THE INSTANCES, b731`S AND b730`S ENTRIES, THE HAND READ BESIDE'], 0, 0
    raw = _git('show', 'HEAD:FINDINGS.md', repo=A.REPOS['pp'])
    bt = raw.encode('utf-8')
    for act in ('b731', 'b730'):
        fj = json.loads(rd('%s_findings.json' % act))
        text = A.landed_entry(act, fj)
        ap = fj['append']
        hand = bt[ap['before']:ap['before'] + ap['added']].decode('utf-8')   # ### the hand read: by the bank's byte span and not its line, a second route to the same bytes
        sc = rd('%s_scores_close.json' % act)
        ts, hs = sentences(text), sentences(hand.strip() + NL)
        n += 1
        g += case(L, 'n3', '%s`s entry, FINDINGS :%d, %d lines' % (act, fj['line'], text.count(NL)), 'the bank carries `text`: %s ; its scores print the composer: %s, the entry never read' % ('text' in fj, 'no entry landed yet' in sc),
                  'the landed lines, %d characters, %d sentences; the hand read beside, the byte span the bank records: %d characters, %d sentences; equal %s' % (len(text), len(ts), len(hand.strip()) + 1, len(hs), text == hand.strip() + NL),
                  'text' not in fj and 'no entry landed yet' in sc, text == hand.strip() + NL and len(ts) == len(hs) and len(ts) > 0)
    fj = json.loads(rd('b731_findings.json'))
    text = A.landed_entry('b731', fj)
    plain = dict(fj, line=fj['line'] + 1)
    try:
        A.landed_entry('b731', plain)
        mv = False
    except ValueError:
        mv = True
    n += 1
    g += guard(L, 'n3', 'PLANT, THE KEY MOVED: the bank`s line one down raises, never falling to the composer', 'raises %s' % mv, mv)
    body = text.split(NL, 1)[1].strip()
    n += 1
    g += guard(L, 'n3', 'b731 event (10)`s hand read, the entry`s body split at . and ;: 53 sentences, the bare DERIVES 0', '%d sentences by the tool`s lines ; bare DERIVES %d' % (len(SPLIT.split(body)), sum(1 for s in SPLIT.split(body) if re.search(r'\bDERIVES\b', s) and 'W-ORD-ZQ-DERIVES' not in s)),
               len(SPLIT.split(body)) == 53 and not any(re.search(r'\bDERIVES\b', s) and 'W-ORD-ZQ-DERIVES' not in s for s in SPLIT.split(body)))
    plant = text.replace('\n\n', '\n\nThe instance DERIVES the zeros fields CLOSED with nothing further.\n\n', 1)
    rx = lambda s_: re.search(r'\binstance\b[^.;]*(?<!-)\bDERIVES\b', s_)   # noqa: E731
    before, after = [s for s in sentences(text) if rx(s)], [s for s in sentences(plant) if rx(s)]
    n += 1
    g += guard(L, 'n3', 'PLANT, THE SENTENCE: a planted sentence in the landed text is what b731`s clause reads: hits before %d, after %d' % (len(before), len(after)), '%s' % [s[:70] for s in after], not before and len(after) == 1)
    tpl = open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'n3', 'the reader reads the key; fj.get(`text`) is gone from the template, its line count kept', '%s ; %s' % ("fj.get('text')" not in tpl, 'landed_entry' in tpl), "fj.get('text')" not in tpl and 'landed_entry' in tpl and tpl.count(NL) == base('tools/standing/fold/record.tpl').count(NL))
    return L, g, n


CONTROLS = dict(module=control_module, reprice=control_reprice, leanpath=control_leanpath, n3=control_n3)
ORDER = ('module', 'reprice', 'leanpath', 'n3')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.12.0, (R342)(2)(i)-(iv): THE ACT MODULE RENDERED, THE RE-PRICE FROM THE BANKS, THE LEAN PATHS AGAINST THE TREE, THE N3 READER ON THE LANDED LINES (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.12.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1120.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1120.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
