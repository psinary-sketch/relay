# -*- coding: utf-8 -*-
"""standing/v1160.py -- THE CONTROLS OF v1.16.0 ((R346)(3)(i)-(viii)), in v1150.py's form: each instance read through the route as it stood before the repair and through the repaired route; AS WANTED
where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). Written at b736 by the Write tool.

  python -X utf8 -u tools/standing/v1160.py control [vacuous|lexicon|refused|fsck|watch|dry|counter ...] [--bank]
"""
import io
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
PP = 'D:/MY-DOwnloads/PLACE-papers'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf/scratchpad'
EF, TIP = 'D:/SIDE-explicit-formula', 'b25fd82c'
EZ, MAIN = 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import counterline as CN        # noqa: E402
import dispatchrows as DR       # noqa: E402
import prelock as PL            # noqa: E402
import salthead as SH           # noqa: E402
import scratchfsck as SF        # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _read(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.15.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.16.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.16.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def _stmt(src, name):
    L_ = src.split(NL)
    i = next(k for k, l in enumerate(L_) if l.startswith('theorem %s ' % name))
    j = next(k for k in range(i, len(L_)) if ':=' in L_[k])
    return ' '.join(NL.join(L_[i:j + 1]).split('theorem %s' % name, 1)[1].split(':=', 1)[0].split())


def control_vacuous():
    L, g, n = ['### (vacuous) (R346)(3)(i), data/b735_explicitformula.txt :211: THE CLAUSE "no hypothesis that is the claim" READS THE PROOF TERM, EpsteinZQ.lean :153 READ AS FAIL AND Main.lean :194 AS PASS'], 0, 0
    ez, mn = _git('show', '%s:%s' % (TIP, EZ), repo=EF), _git('show', '%s:%s' % (TIP, MAIN), repo=EF)
    old = _read('b735_explicitformula.txt').split(NL)
    pas = [l for l in old if l.strip().startswith('no hypothesis that is the claim')]
    r = {}
    for src, name in ((ez, 'zq_count'), (ez, 'zq_explicit_formula'), (ez, 'zq_li_nonneg_imp_online'), (mn, 'zq_count_instance'), (mn, 'zq_explicit_formula_instance'), (mn, 'zq_li_nonneg_imp_online_instance')):
        r[name] = SH.read(_stmt(src, name), SH.proof_of(src, name))
        L.append('      %-34s %-5s %-12s %s' % (name, r[name]['verdict'], r[name]['kind'], r[name]['why'][:110]))
    n += 1
    g += case(L, 'vacuous', 'EpsteinZQ.lean :153, zq_count, its proof h.count', 'the text arm read PASS at b735 on every row (%d rows PASS of %d read)' % (sum('PASS' in l for l in pas), len(pas)), 'the proof-head arm reads %s, head %s' % (r['zq_count']['verdict'], r['zq_count']['head']),
              len(pas) == 6 and all('PASS' in l for l in pas), r['zq_count']['verdict'] == 'FAIL' and r['zq_count']['kind'] == 'projection')
    n += 1
    g += guard(L, 'vacuous', 'Main.lean :194, zq_count_instance, its proof zq_count zq_premises, reads PASS', '%s, head %s' % (r['zq_count_instance']['verdict'], r['zq_count_instance']['head']), r['zq_count_instance']['verdict'] == 'PASS' and r['zq_count_instance']['head'] == 'zq_count')
    n += 1
    g += guard(L, 'vacuous', ':157, h.explicitFormula.ef k hk hs he, a projection applied, FAILS', '%s, head %s' % (r['zq_explicit_formula']['verdict'], r['zq_explicit_formula']['head']), r['zq_explicit_formula']['verdict'] == 'FAIL')
    n += 1
    g += guard(L, 'vacuous', ':164 is NO PROJECTION: h.count.elim opens a field and the body applies Wide.li_nonneg_cfg_imp_online_ne_zero, so the arm prints elimination and PASS; (R346)(3)(i) says three projections and the term is two and one', '%s, %s' % (r['zq_li_nonneg_imp_online']['verdict'], r['zq_li_nonneg_imp_online']['kind']),
               r['zq_li_nonneg_imp_online']['kind'] == 'elimination')
    n += 1
    g += guard(L, 'vacuous', 'the other two premise-free forms read PASS, compiled heads', '%s ; %s' % (r['zq_explicit_formula_instance']['head'], r['zq_li_nonneg_imp_online_instance']['head']), r['zq_explicit_formula_instance']['verdict'] == 'PASS' and r['zq_li_nonneg_imp_online_instance']['verdict'] == 'PASS')
    p1 = SH.read('(h : P) : Q', 'h')
    n += 1
    g += guard(L, 'vacuous', 'a bare hypothesis as the proof is no projection and this arm does not read it; the E0 rule`s ENCODES-CONCLUSION does', '%s, %s' % (p1['verdict'], p1['kind']), p1['kind'] == 'compiled')
    return L, g, n


def control_lexicon():
    L, g, n = ['### (lexicon) (R346)(3)(ii): THE EXTENSION IN THE SHARED RULE BY A COMMIT OF ITS OWN, data/b736_e0_landing.txt'], 0, 0
    b = _read('b736_e0_landing.txt')
    lg = _git('log', '--format=%h %s', 'd4e0ea02..HEAD', '--', 'tools/e0_rule.py').strip().split(NL)
    names = _git('show', '--name-only', '--format=', lg[0].split()[0]).split() if lg and lg[0] else []
    tb = io.open(os.path.join(T, 'e0_rule.py'), encoding='utf-8').read()
    n += 1
    g += case(L, 'lexicon', 'the landed lines through the shared rule', 'at d4e0ea02 the rule raises BinderUnclassed on WideConfig, the extension private: %s' % ('RAISED' in b), 'the bank`s foot: %s' % [l for l in b.split(NL) if l.startswith('### ### **')][:1],
              'RAISED' in b and "'WideConfig'" not in _git('show', 'd4e0ea02:tools/e0_rule.py'), 'CONTROLS ALL AS WANTED' in b and "'WideConfig'" in tb)
    n += 1
    g += guard(L, 'lexicon', 'the rule moved at one commit since d4e0ea02, carrying no file of tools/standing/', '%s ; %s' % (lg, names), len(lg) == 1 and 'tools/e0_rule.py' in names and not any(x.startswith('tools/standing/') for x in names))
    n += 1
    g += guard(L, 'lexicon', 'the three forms and the five zeta and Dirichlet rows unchanged', 'unchanged rows %d' % len(re.findall(r'(?m)^  (?!MET )\S+ unchanged\s+AS WANTED', b)), len(re.findall(r'(?m)^  (?!MET )\S+ unchanged\s+AS WANTED', b)) == 8)
    return L, g, n


def control_refused():
    L, g, n = ['### (refused) (R346)(3)(iii): THE READ REFUSED AFTER b735`S CLOSING WAS COMPOSED, ITS ROW AND ITS RULE'], 0, 0
    rows = _read('b736_hook_refusals.txt').split(NL)
    ev = _read('b735_events.txt')
    closing_at = _git('log', '-1', '--format=%cI', 'd4e0ea02').strip()
    hook = io.open(os.path.join(S, 'hook.py'), encoding='utf-8').read()
    n += 1
    g += case(L, 'refused', 'the Read of 2026-11-02T20:49:14Z, data/b735_closing.txt', 'data/b735_events.txt rows carry it: %s; data/b735_hook_refusals.txt carries it: %s' % ('20:49' in ev, '20:49:14' in _read('b735_hook_refusals.txt')),
              'data/b736_hook_refusals.txt :1: %s' % rows[0][:70], '20:49' not in ev, rows[0].startswith('2026-11-02T20:49:14Z') and 'b735_closing.txt' in rows[0])
    n += 1
    g += guard(L, 'refused', 'the hook routes a refusal past a composed closing to the next act', 'the route in tools/standing/hook.py: %s ; the commit of the closing %s' % ('next_of(relay)' in hook, closing_at), 'next_of(relay)' in hook)
    r = _read('b736_rules.txt')
    n += 1
    g += guard(L, 'refused', 'the rule written', 'data/b736_rules.txt row (1): %s' % ('(1) A REFUSAL AFTER THE CLOSING' in r), '(1) A REFUSAL AFTER THE CLOSING' in r)
    return L, g, n


def control_fsck():
    L, g, n = ['### (fsck) (R346)(3)(iv), DEFECT (p): THE SCRATCH CLONE`S FSCK, zqwork2`S TWO READS THE RULED CONTROL, A SECOND LOSS; zqwork THE FIRST; zqwork3, A FRESH CLONE, THE CLEAN ARM ADDED AND DECLARED'], 0, 0
    zq2, zq1, zq3 = SP + '/zqwork2', SP + '/zqwork', SP + '/zqwork3'
    a, b = SF.read(zq2), SF.read(zq2)
    d = SF.read(zq1)
    c, e = SF.read(zq3), SF.read(zq3)
    k = SF.read('D:/SIDE-explicit-formula')
    keep = dict(kind='read', free_mb=4000, free_at='x', clone='zqwork2')
    n += 1
    g += guard(L, 'fsck', 'a read row naming a clone, no fsck, refused before anything is written', str(DR.why(keep)), bool(DR.why(keep)))
    n += 1
    g += guard(L, 'fsck', 'the row carrying both reads stands', str(DR.why(dict(keep, fsck_before='ok', fsck_after='ok'))), DR.why(dict(keep, fsck_before='ok', fsck_after='ok')) is None)
    n += 1
    g += guard(L, 'fsck', 'zqwork2`s two reads, as ruled: NOT clean, both, the pack directory gone at 2026-11-02T21:44:22Z, a second instance of (p)', '%s ; %s' % (a[1][:90], b[1][:90]), not a[0] and not b[0] and a[1] == b[1])
    n += 1
    g += guard(L, 'fsck', 'zqwork3, cut fresh from the kernel at this act, two reads clean: the reader`s clean arm, added, not in the ruling', '%s ; %s' % (c[1], e[1]), c[0] and e[0])
    n += 1
    g += guard(L, 'fsck', 'the kernel itself, clean', k[1], k[0])
    n += 1
    g += guard(L, 'fsck', 'the damaged clone zqwork, left in place, reads not clean', d[1][:120], not d[0])
    return L, g, n


def control_watch():
    L, g, n = ['### (watch) (R346)(3)(v), DEFECT (n): A REAPED WATCH CARRIES ITS CHOICE IN THE ROW'], 0, 0
    rows = json.load(open(os.path.join(D, 'b735_dispatch_rows.json'), encoding='utf-8'))
    five = [r for r in rows if r.get('n') == 5 or r.get('dispatch') == 5]
    plant = dict(kind='dispatch', free_mb=4000, free_at='x', reaped=True)
    n += 1
    g += case(L, 'watch', 'a dispatch row with its watch reaped and no choice', 'b735`s rows for n = 5 (%d) carry a watch field: %s' % (len(five), any('watch' in r for r in five)), 'the writer refuses: %s' % DR.why(plant), not any('watch' in r for r in five), bool(DR.why(plant)))
    n += 1
    g += guard(L, 'watch', 'either choice stands', '%s ; %s' % (DR.why(dict(plant, watch='foreground')), DR.why(dict(plant, watch='restarted'))), DR.why(dict(plant, watch='foreground')) is None and DR.why(dict(plant, watch='restarted')) is None)
    n += 1
    g += guard(L, 'watch', 'b735`s banked rows stand under the writer, no row carrying the new fields', str(DR.check(rows)[:2]), not DR.check(rows))
    return L, g, n


def control_dry():
    L, g, n = ['### (dry) (R346)(3)(vi), EVENT (1): THE SCORE ROUTES` DRY FORM BEFORE THE LOCK, THE FACE`S ORDER AND THE TOOL`S ONE'], 0, 0
    b5, b4 = PL.scores_dry_order('b735'), PL.scores_dry_order('b734')
    src = io.open(os.path.join(S, 'prelock.py'), encoding='utf-8').read()
    n += 1
    g += case(L, 'dry', 'b735`s late run', 'the arm G-RULE-SCORES-BEFORE-SEAL passed it, the bank at %s after the lock %s' % b5[:2], 'the order read: %s ; b734`s %s' % (b5[2], b4[2]), b5[2] == 'OUT OF ORDER', b4[2] == 'IN ORDER')
    n += 1
    g += guard(L, 'dry', 'the gate reads NOT CLEAR while the bank is absent', 'prelock.gate carries the condition: %s' % ('clear = not c[\'missing\'] and not undecl and dry' in src), 'clear = not c[\'missing\'] and not undecl and dry' in src)
    return L, g, n


def control_counter():
    L, g, n = ['### (counter) (R346)(3)(vii), (R345)(2)(vii), READ AGAINST b735: THE HAND SECTION AND THE CLOSING'], 0, 0
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace('\r', '').split(NL)
    hand, closing = ot[17304], _read('b735_closing.txt').split(NL)[4]
    a = CN.read(hand, closing)
    note = hand + ' Dated note, b736: the closing carries the last figure, the eight events landing after the hand section.'
    b = CN.read(note, closing)
    n += 1
    g += case(L, 'counter', 'OPEN_TRAILS :17305 against data/b735_closing.txt :5, the rule of (R345)(2)(vii) not met at b735', 'hand %s, closing %s, equal %s, names the closing %s' % (a['hand'], a['closing'], a['equal'], a['names_closing']), 'with b736`s dated note: names the closing %s' % b['names_closing'], not a['ok'], b['ok'])
    tp = io.open(os.path.join(T, 'acts', 'b736.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'counter', 'b736`s own trail names the closing as the last figure, its section carrying the words', 'the closing carries the last figure in tools/acts/b736.py: %s' % ('the closing carries the last figure' in tp), 'the closing carries the last figure' in tp)
    return L, g, n


CONTROLS = dict(vacuous=control_vacuous, lexicon=control_lexicon, refused=control_refused, fsck=control_fsck, watch=control_watch, dry=control_dry, counter=control_counter)
ORDER = ('vacuous', 'lexicon', 'refused', 'fsck', 'watch', 'dry', 'counter')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.16.0, (R346)(3)(i)-(viii): THE VACUOUS PASS AT THE HEAD, THE LEXICON, THE REFUSED READ, THE CLONE`S FSCK, THE REAPED WATCH, THE SCORE ROUTES` DRY FORM, THE COUNTER (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + ['', '### the instances read at their commits; each case through both routes', '']
    tg = tn = 0
    for k in names:
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.16.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1160.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1160.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
