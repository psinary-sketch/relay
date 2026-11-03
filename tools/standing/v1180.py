# -*- coding: utf-8 -*-
"""standing/v1180.py -- THE CONTROLS OF v1.18.0 ((R348)(2)(i)-(viii)), in v1170.py's form: each instance read through the route as it stood before the repair and through the repaired route; AS WANTED
where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the
repair is read from the blob at BASE (b737's closing), not from disk. Written at b738 by the Write tool.

  python -X utf8 -u tools/standing/v1180.py control [figbank|comparative|inplace|deletes|order|split|vacuous|leanpath ...] [--bank]
"""
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import time
import types

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
BASE = '54cd4f92'   # ### b737's closing, the toolset as v1.17.0 left it
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import cites as CT              # noqa: E402
import compilecontrol as CC     # noqa: E402
import deletes as DL            # noqa: E402
import figbank as FB            # noqa: E402
import hook as HK               # noqa: E402
import prelock as PL            # noqa: E402
import probes as PB             # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _read(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def _rd(n):
    return _read(n[len('data/'):] if n.startswith('data/') else n)


def base_module(rel, name):
    """the module at BASE, read from its blob and run in a fresh namespace, not from disk."""
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(_git('show', '%s:%s' % (BASE, rel)), name, 'exec'), m.__dict__)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.17.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.18.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.18.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def _relay(act='b999', citation=None):
    """a constructed relay: data/act_current.json naming `act`, and the act's citation json where given."""
    tmp = tempfile.mkdtemp(prefix='standing-v1180-')
    os.makedirs(os.path.join(tmp, 'data'))
    with open(os.path.join(tmp, 'data', 'act_current.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps({'act': act, 'next': 'b1000'}) + NL)
    if citation is not None:
        with open(os.path.join(tmp, 'data', '%s_citation_check.json' % act), 'w', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(citation) + NL)
    return tmp


def control_figbank():
    L, g, n = ['### (figbank) (R348)(2)(i), b737 DEFECT (q): A FIGURE BANK OPENS WITH ITS CONTROLS BLOCK; THE RENDER REFUSES ONE WHOSE BLOCK IS ABSENT OR FOLLOWS ITS FIGURES'], 0, 0
    for name in ('b737_offlinezero_criteria.txt', 'b737_offlinezero_box.txt'):
        r = FB.reading(_read(name))
        n += 1
        g += case(L, 'figbank', 'b737`s plan bank data/%s, as committed' % name, 'no reader of the order of controls and figures at %s (tools/standing/figbank.py absent: %s)' % (
            BASE, not _git('ls-tree', '--name-only', BASE, 'tools/standing/figbank.py').strip()), 'figbank.reading: %s ; %s' % ('PASSES' if r['ok'] else 'REFUSED', r['why']),
            not _git('ls-tree', '--name-only', BASE, 'tools/standing/figbank.py').strip(), not r['ok'] and r['figures'] > 0)
    r = FB.reading(_read('b736_sitting.txt'))
    n += 1
    g += guard(L, 'figbank', 'b736`s sitting bank data/b736_sitting.txt passes', '%s ; figures %d ; %s' % ('PASSES' if r['ok'] else 'REFUSED', r['figures'], r['why']), r['ok'])
    r = FB.reading(_read('b737_offlinezero_plan.txt'))
    n += 1
    g += guard(L, 'figbank', 'b737`s plan bank data/b737_offlinezero_plan.txt read beside them (its figures in prose, no block)', '%s ; figures %d ; %s' % ('PASSES' if r['ok'] else 'REFUSED', r['figures'], r['why']), not r['ok'])
    tmp = tempfile.mkdtemp(prefix='standing-v1180-fig-')
    good = 'b999 -- a bank\n\n## THE CONTROLS\n  zeta`s first zero 14.134725, as wanted\n\n## THE FIGURES\n  the margin 0.357096\n'
    bad = 'b999 -- a bank\n\n## THE FIGURES\n  the margin 0.357096\n\n## THE CONTROLS\n  zeta`s first zero 14.134725, as wanted\n'
    p1, p2 = os.path.join(tmp, 'good.txt'), os.path.join(tmp, 'bad.txt')
    FB.write(p1, good)
    try:
        FB.write(p2, bad)
        refused = False
    except SystemExit:
        refused = True
    n += 1
    g += guard(L, 'figbank', 'a constructed pair in %s: the controls first written, the controls after refused and nothing written' % tmp,
               'good written %s ; bad refused %s, its file absent %s' % (os.path.exists(p1), refused, not os.path.exists(p2)), os.path.exists(p1) and refused and not os.path.exists(p2))
    return L, g, n


B737_TRAILS = dict(at=('data/b737_offlinezero_plan.txt', 23), word='trails', subject='off0', better='higher',
                   figures=[('off0', ('line', 'data/b737_offlinezero_criteria.txt', 8, r'zeta_K`s zeros .* the nearest at distance ([0-9.]+)')),
                            ('off12', ('line', 'data/b737_offlinezero_criteria.txt', 13, r'zeta_K`s zeros .* the nearest at distance ([0-9.]+)'))],
                   note='the distance to zeta_K`s zeros, the farther the better')
R347_LOWEST = dict(at=('data/b737_ferry.txt', 13), word='lowest', subject='off0',
                   figures=('table', 'data/b725_interference.txt', 32, r'^\s+(off\d+)\s+[0-9.]+\s+([0-9.]+)\s'), note='gamma over the off-line rows, the table at :31-')


def control_comparative():
    L, g, n = ['### (comparative) (R348)(2)(ii), b737 DEFECT (v): A BANK`S COMPARATIVE SENTENCE READ AGAINST THE TABLE IT CITES, AGREES OR CONTRADICTS, BEFORE THE LOCK'], 0, 0
    oldc = base_module('tools/standing/cites.py', 'old_cites')
    rows = CT.comparative_rows([B737_TRAILS, R347_LOWEST], _rd)
    t, lo = rows[0], rows[1]
    n += 1
    g += case(L, 'comparative', 'b737`s plan :23 "it trails off12 on the distance to zeta_K`s zeros", against data/b737_offlinezero_criteria.txt :8 and :13',
              'the v1.17.0 citation reader carries no comparative read: %s' % (not hasattr(oldc, 'comparative_rows')),
              '%s ; off0 %s, off12 %s' % (t[5], t[4].get('off0'), t[4].get('off12')), not hasattr(oldc, 'comparative_rows'), t[5] == 'CONTRADICTS')
    n += 1
    g += guard(L, 'comparative', '(R347)(3)(a)`s "at the lowest height" against data/b725_interference.txt`s table from :32 (the off-line rows)',
               '%s ; rows %d ; off0 %s, the next least %s' % (lo[5], len(lo[4]), lo[4].get('off0'), min([v for k, v in lo[4].items() if k != 'off0'] or [0])), lo[5] == 'AGREES' and len(lo[4]) == 69)
    hits = CT.comparative_hits('data/b737_offlinezero_plan.txt', _read('b737_offlinezero_plan.txt'))
    un = CT.comparative_unread(hits, rows)
    n += 1
    g += guard(L, 'comparative', 'b737`s plan bank whole: its comparative words, each needing a reading row, the one row above covering :23 alone (the check would halt on the rest UNREAD)',
               'words %d (%s) ; unread %d' % (len(hits), ', '.join(':%d %s' % (l, w) for _b, l, w in hits[:12]), len(un)), len(hits) >= 2 and len(un) == len(hits) - 1)
    n += 1
    g += guard(L, 'comparative', '"at least" and "leads to" are no comparison', str(CT.comparative_hits('x', 'at least two\nit leads to the box\nit leads off12')), CT.comparative_hits('x', 'at least two\nit leads to the box\nit leads off12') == [('x', 3, 'leads')])
    return L, g, n


B737_SED = ("sed -i 's/### Defects (a)-(r) are entered/### Defects (a)-(t) are entered/; s/the checks one, the defects (a)-(r) the seat`s,/the checks one, "
            "the defects (a)-(t) the seat`s,/' D:/relay/tools/b737_face_blocks.txt")


def control_inplace():
    L, g, n = ['### (inplace) (R348)(2)(iii), b737 DEFECT (u): THE HOOK REFUSES AN IN-PLACE EDIT BY THE SHELL; b737`S 16:08:45Z COMMAND REPLAYED (data/b737_commands.json :1641)'], 0, 0
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    present = B737_SED in _read('b737_commands.json')
    o, nw = oldh.judge('Bash', {'command': B737_SED}), HK.judge('Bash', {'command': B737_SED})
    n += 1
    g += case(L, 'inplace', 'b737`s `sed -i` on tools/b737_face_blocks.txt (in the command bank: %s)' % present, 'judge -> %s' % (o,), 'judge -> %s' % (nw and nw[0],), o is None, bool(nw) and nw[0] == 'INPLACE')
    plain = ('sed -n 5p D:/relay/data/x.txt', 'git -C D:/relay grep -n "sed -i" -- data', 'python -X utf8 -u D:/relay/tools/standing/fold.py checks --part act')
    edits = ('perl -pi -e "s/a/b/" f.txt', 'sed -i.bak "s/a/b/" f', 'sed --in-place "s/a/b/" f', 'Set-Content -Path f.txt -Value x')
    rp, re_ = [HK.judge('Bash', {'command': c}) for c in plain], [HK.judge('PowerShell', {'command': c}) for c in edits]
    n += 1
    g += guard(L, 'inplace', 'three reads pass (sed -n, a grep for the words, a suite part); the three sed and perl in-place forms refused INPLACE, Set-Content refused (REDIR by cmdlet, its v1.9.0 kind, read first)',
               '%s ; %s' % ([r and r[0] for r in rp], [r and r[0] for r in re_]), all(r is None for r in rp) and all(r and r[0] == 'INPLACE' for r in re_[:3]) and bool(re_[3]))
    return L, g, n


def control_deletes():
    L, g, n = ['### (deletes) (R348)(2)(iv), b737 DEFECT (d): THE DELETE STEP AFTER A CLEAN CITATION CHECK, BY THE TOOL; b737`S SEQUENCE REPLAYED WITH THE DELETE HELD'], 0, 0
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    cmd = 'git -C D:/relay branch -d push-b736-closing'
    r0 = _relay()
    n += 1
    g += guard(L, 'deletes', 'b737`s 14:32Z order: the delete before any citation check, in a constructed relay %s: the hook and the tool hold it' % r0,
               'hook %s ; deletes.citation_clean %s' % (HK.judge('Bash', {'command': cmd}, relay=r0), DL.citation_clean(r0)),
               (HK.judge('Bash', {'command': cmd}, relay=r0) or ('',))[0] == 'ORDER' and not DL.citation_clean(r0))
    r1 = _relay(citation=dict(at='x', rows=[], misses=[]))
    n += 1
    g += case(L, 'deletes', 'a citation check banked HALTED (its json standing, no `clean`), the delete sent after it (%s)' % r1,
              'citation_done -> %s' % oldh.citation_done(r1), 'citation_done -> %s ; deletes.citation_clean -> %s' % (HK.citation_done(r1), DL.citation_clean(r1)),
              oldh.citation_done(r1) is True, HK.citation_done(r1) is False and DL.citation_clean(r1) is False)
    r2 = _relay(citation=dict(at='x', rows=[], misses=[], clean=True))
    n += 1
    g += guard(L, 'deletes', 'the check banked CLEAN: the delete may run (%s)' % r2, 'hook %s ; deletes.citation_clean %s' % (HK.judge('Bash', {'command': cmd}, relay=r2), DL.citation_clean(r2)),
               HK.judge('Bash', {'command': cmd}, relay=r2) is None and DL.citation_clean(r2))
    return L, g, n


def control_order():
    L, g, n = ['### (order) (R348)(2)(v), b737 EVENTS (1), A REPEAT OF (R346)(3)(vi): A CLOSE STEP BEFORE THE LOCK REFUSES ONCE THE LOCK`S EVIDENCE STANDS'], 0, 0
    old = _git('show', '%s:tools/standing/fold/record.tpl' % BASE)
    i = old.find('def _close_step(n):')
    body = old[i:old.find('\ndef ', i + 10)]
    ev = _read('b737_events.txt')
    import fold as F
    F.install()
    R = F.load(A.current().get('act'), 'record')
    tmp = tempfile.mkdtemp(prefix='standing-v1180-order-')
    keepD, keepR = R.D, R.AC.close_refuses
    out = {}
    try:
        R.D, R.AC.close_refuses = tmp, (lambda a, k: None)
        for tag in ('before', 'after'):
            if tag == 'after':
                with open(os.path.join(tmp, '%s_lockgate.json' % R.ACT), 'w', encoding='utf-8', newline='\n') as f:
                    f.write('{}\n')
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    R._close_step(2)
                out[tag] = ('RUNS', buf.getvalue().strip()[:120])
            except SystemExit as e:
                out[tag] = ('REFUSED %s' % e.code, buf.getvalue().strip()[:160])
    finally:
        R.D, R.AC.close_refuses = keepD, keepR
    n += 1
    g += case(L, 'order', 'b737`s 17:22:02Z `record rootdry` after its lock (events (1): %s)' % ('(1) THE SEAT\'S [CLOSE ; NEW]: 17:22:02Z' in ev),
              'the step guard at %s reads the lock: %s (the bank`s membrane refused, exit 4)' % (BASE, 'lockgate' in body), 'step [2] with the lock`s evidence in %s: %s -- %s' % (tmp, out['after'][0], out['after'][1]),
              'lockgate' not in body, out['after'][0] == 'REFUSED 5')
    n += 1
    g += guard(L, 'order', 'step [2] before the lock runs', '%s -- %s' % out['before'], out['before'][0] == 'RUNS')
    return L, g, n


def control_split():
    L, g, n = ['### (split) (R348)(2)(vi), b737 EVENTS (2), (5), (7), (9): THE LONG PHASES SPLIT UNDER b675 RULES ROW (2); EACH NEW PART`S PHASE REPLAYED (data/b738_split_replay.txt)'], 0, 0
    import importlib
    cur = A.current()
    wl = importlib.import_module('%s_worklist' % cur.get('act'))
    rep = _read('%s_split_replay.txt' % cur.get('act'))
    import re
    ph = [int(x) for x in re.findall(r'THE PHASE \w+ : (\d+) s', rep)]
    old_parts = json.loads(_git('show', '%s:data/act_current.json' % BASE)).get('parts')
    n += 1
    g += case(L, 'split', 'b737`s four phases over 450 s (471, 656, 462, 456 s) under its seven parts, replayed under the ten',
              'the parts at %s: %d %s' % (BASE, len(old_parts), old_parts), 'the six new phases %s s, the longest %s' % (ph, max(ph or [0])),
              len(old_parts) == 7, len(ph) == 6 and max(ph) < 450)
    q = list(wl.CHAIN_QUARTERS)
    contiguous = q[0][0] == wl.CHAIN_HALVES[0][0] and q[-1][1] == wl.CHAIN_HALVES[0][1] and all(int(b[0][1:]) == int(a[1][1:]) + 1 for a, b in zip(q, q[1:]))
    n += 1
    g += guard(L, 'split', 'the quarters cover the first half once, in order, and data/act_current.json`s parts are the worklist`s', '%s ; act_current %s' % (q, cur.get('parts')),
               contiguous and list(cur.get('parts') or []) == list(wl.PARTS) and len(wl.PARTS) == 10)
    import no_sorry_main as NSM
    names = NSM.kernels()
    h = (len(names) + 1) // 2
    n += 1
    g += guard(L, 'split', 'G-NO-SORRY-MAIN`s halves partition the kernels (the suite`s nsm_split)', 'kernels %d ; first %d ; rest %d' % (len(names), h, len(names) - h), h + (len(names) - h) == len(names) and 0 < h < len(names))
    oldp = base_module('tools/standing/prelock.py', 'old_prelock')
    n += 1
    g += case(L, 'split', 'the pre-lock comparison reads each act by its own parts', 'v1.17.0 PARTS %d, fixed' % len(oldp.PARTS),
              'parts_of(%s) %d ; parts_of(%s) %d' % (cur.get('act'), len(PL.parts_of(cur.get('act'))), cur.get('prev'), len(PL.parts_of(cur.get('prev')))),
              not hasattr(oldp, 'parts_of'), len(PL.parts_of(cur.get('act'))) == 10 and len(PL.parts_of(cur.get('prev'))) == 7)
    nm = '%s_probe_standing-b2c.txt' % cur.get('act')
    oldpb = base_module('tools/standing/probes.py', 'old_probes')
    n += 1
    g += case(L, 'split', 'a new part`s probe bank is a probe path', 'is_probe(%s) -> %s' % (nm, oldpb.is_probe(cur.get('act'), nm)), 'is_probe -> %s' % PB.is_probe(cur.get('act'), nm),
              not oldpb.is_probe(cur.get('act'), nm), PB.is_probe(cur.get('act'), nm))
    return L, g, n


def control_vacuous():
    L, g, n = ['### (vacuous) (R348)(2)(vii), b736, b737: G-RUNNER-GATE WITH NO DISPATCH PRINTS VACUOUS BY NAME AND COUNTS NEITHER WAY; THE RULE WRITTEN'], 0, 0
    c737 = _read('b737_checks.txt')
    import re
    vl = [l for l in c737.split(NL) if 'VACUOUS, THE PLANT MUTATED NOTHING' in l]
    n += 1
    g += guard(L, 'vacuous', 'b737`s combined bank names G-RUNNER-GATE on its VACUOUS line, counted neither passing nor failing', (vl[0].strip()[:200] if vl else 'NO LINE'), bool(vl) and 'G-RUNNER-GATE' in vl[0])
    rules = _read('%s_rules.txt' % A.current().get('act'))
    n += 1
    g += guard(L, 'vacuous', 'the rule written: data/%s_rules.txt row (7)' % A.current().get('act'), str(bool(re.search(r'\(7\) A VACUOUS RUNNER GATE', rules))), bool(re.search(r'\(7\) A VACUOUS RUNNER GATE', rules)))
    return L, g, n


def control_leanpath():
    L, g, n = ['### (leanpath) b738 STEP-ZERO DEFECT (e): THE LEAN-PATH READER -- A CLOSED PARENTHESIS ENDS THE WINDOW; THE NEAREST IDENTIFIER IS THE ONE CITED; MATHLIB AT ITS PIN AMONG THE TREES'], 0, 0
    oldc = base_module('tools/standing/cites.py', 'old_cites')
    import importlib
    wl = importlib.import_module('%s_worklist' % A.current().get('act'))
    fer = _read('%s_ferry.txt' % A.current().get('act'))
    ro, rn = oldc.lean_rows(fer, wl.LEAN_TREES), CT.lean_rows(fer, wl.LEAN_TREES)
    ho, hn = [r for r in ro if not r[3]], [r for r in rn if not r[3]]
    n += 1
    g += case(L, 'leanpath', 'the ferry of (R348), its Lean paths against zq-b730 and Mathlib at de5ce8a9', 'rows %d, halts %d: %s' % (len(ro), len(ho), '; '.join('%s %s' % (r[0], r[1]) for r in ho)[:300]),
              'rows %d, halts %d' % (len(rn), len(hn)), bool(ho), not hn)
    import v1120 as V
    with contextlib.redirect_stdout(io.StringIO()):
        LL, gg, nn = V.control_leanpath()
    n += 1
    g += guard(L, 'leanpath', 'v1.12.0`s (leanpath) control under the repaired reader', '%d of %d as wanted' % (gg, nn), gg == nn)
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    n += 1
    g += guard(L, 'leanpath', 'tools/standing/VERSION', ver, ver == 'v1.18.0')
    return L, g, n


CONTROLS = dict(figbank=control_figbank, comparative=control_comparative, inplace=control_inplace, deletes=control_deletes, order=control_order, split=control_split,
                vacuous=control_vacuous, leanpath=control_leanpath)
ORDER = ('figbank', 'comparative', 'inplace', 'deletes', 'order', 'split', 'vacuous', 'leanpath')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.18.0, (R348)(2)(i)-(viii): FIGURES BEFORE CONTROLS, THE SENTENCE AGAINST ITS TABLE, THE IN-PLACE EDIT, THE DELETE AFTER A CLEAN CHECK, THE CLOSE`S ORDER, THE SPLIT, THE VACUOUS GATE, THE LEAN READER (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '## THE CONTROLS',
        '  the bank is its controls: the compile control first, then each repair`s instances through both routes; written through tools/standing/figbank.py ((R348)(2)(i))', '',
        '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + ['', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.18.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1180.txt' % act), NL.join(out))
        print('written data/%s_standing_v1180.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
