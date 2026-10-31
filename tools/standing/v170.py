# -*- coding: utf-8 -*-
"""standing/v170.py -- THE CONTROLS OF v1.7.0 ((R337)(2)), in v160.py's form: each instance replayed through the route as it stood at HEAD before
the repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. Written at b727 by the Write
tool.

  python -X utf8 tools/standing/v170.py control [actcur|branches|answers ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v170.txt with every control run, nothing else.
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
for p_ in (S, T):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402

B726_BASE, B726_CLOSE = 'e2246a8e', '9fac0a1d'
B725_LOCK, B725_CLOSE = 'e86dbcd5', 'e2246a8e'
B726_FIRST_BANK = '2026-10-30T23:36:45Z'   # ### data/b726_commands.txt #19, `citation check`, the first banking
B726_FIRST_DELETE = '2026-10-30T23:39:57Z'  # ### data/b726_commands.txt :132, #38


def _git(*a):
    return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.6.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.7.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def shared_at(base, tip, act):
    """shared_tools_changed's reading between two named commits."""
    out = _git('diff', '--name-only', base, tip, '--', 'tools/').split()
    return sorted(p for p in out if not p.startswith(('tools/%s_' % act, 'tools/acts/', 'tools/standing/')))


# ================================================================================ (actcur) THE ONE HAND LIST, READ AGAINST GIT
def control_actcur():
    """b726 event (2): data/act_current.json read shared_edits [] where tools/b726_worklist.py read REPAIRED_TOOLS ('rule_arms.py',), two hand
    lists; the repair of one arm failed another. The worklist now reads the json; the arm reads the json against git."""
    L = ['### (actcur) G-ACT-CURRENT -- checks.tpl act_current_ok; instance: b726`s two lists at %s (event (2))' % B726_CLOSE]
    aj = json.loads(_git('show', '%s:data/act_current.json' % B726_CLOSE))
    wl = re.search(r"(?m)^REPAIRED_TOOLS = (\(.*?\))", _git('show', '%s:tools/b726_worklist.py' % B726_CLOSE)).group(1)
    listed = ['tools/' + f for f in eval(wl)]
    truth = shared_at(B726_BASE, B726_CLOSE, 'b726')
    L.append('  the json %s ; the worklist %s ; git %s' % (aj['shared_edits'], listed, truth))
    g1 = case(L, 'actcur', 'b726`s two hand lists, a repair recorded in one', 'the json against the worklist: %s' % (aj['shared_edits'] == listed),
              'the worklist read from the json: one list, equal by construction', aj['shared_edits'] != listed, True)
    # ### both lists stale together, a plant: the old route compared the lists alone and passes it, the new reads git and refuses it
    plant = []
    old_misses, new_catches = plant == plant, plant != truth and bool(truth)
    g2 = old_misses and new_catches
    L += ['  (actcur) both lists stale, a plant: each [] while git shows %s changed' % truth,
          '      BEFORE (v1.6.0): the two lists compared with each other -> %s' % ('PASSES THE STALE PAIR' if old_misses else 'REFUSES IT'),
          '      AFTER  (v1.7.0): the json compared with git -> %s' % ('REFUSES IT' if new_catches else 'PASSES THE STALE PAIR'),
          '      %s' % ('AS WANTED' if g2 else 'NOT AS WANTED')]
    g3 = case(L, 'actcur', 'the json naming git`s list', 'the worklist a second list to keep', 'the json %s against git %s' % (truth, truth), True, sorted(truth) == truth)
    return L, int(g1) + int(g2) + int(g3), 3


# ================================================================================ (branches) THE FIRST BANKING'S TIME
def control_branches():
    """b726 event (3): the citation bank re-banked after the deletes wrote over the time of the check run before them."""
    L = ['### (branches) G-BRANCHES-BANKED -- checks.tpl cit_at, citation.tpl _write; instance: data/b726_citation_check.json (event (3))']
    cj = json.loads(_git('show', '%s:data/b726_citation_check.json' % B726_CLOSE))
    at = cj['at']
    first = A.first_stamp({'at': B726_FIRST_BANK}, at)
    g1 = case(L, 'branches', 'the check run before the deletes, re-banked after them', 'the bank`s time %s against the first delete %s: before %s' % (at, B726_FIRST_DELETE, at < B726_FIRST_DELETE),
              'the first banking`s time kept through the re-bank %s: before %s' % (first, first < B726_FIRST_DELETE), not at < B726_FIRST_DELETE, first < B726_FIRST_DELETE)
    late = A.first_stamp({}, at)
    g2 = case(L, 'branches', 'a check first banked after the deletes, a plant', 'read as above: before %s' % (at < B726_FIRST_DELETE),
              'the first banking %s: before %s, the arm still refuses' % (late, late < B726_FIRST_DELETE), not at < B726_FIRST_DELETE, not late < B726_FIRST_DELETE)
    tpl = open(os.path.join(S, 'fold', 'citation.tpl'), encoding='utf-8').read()
    ck = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    acts = open(os.path.join(T, 'acts', 'b727.py'), encoding='utf-8').read()
    g3 = case(L, 'branches', 'the arm`s NEG plant, inert at b726 (the literal f4ab9491 where the bank read e2246a8e)', 'the old literal over b726`s bank: changes it %s' % ('f4ab9491' in _git('show', '%s:data/b726_stepzero.txt' % B726_CLOSE)),
              'the regular plant over this act`s bank: changes it %s' % (re.sub(r'(push-b726-\w+) \([0-9a-f]{7,8}\)', r'\1', open(os.path.join(D, 'b727_stepzero.txt'), encoding='utf-8').read()) != open(os.path.join(D, 'b727_stepzero.txt'), encoding='utf-8').read()),
              'f4ab9491' not in _git('show', '%s:data/b726_stepzero.txt' % B726_CLOSE), 'first_at' in tpl and "cit.get('first_at')" in ck and 're.sub(r\'(push-b726-' in acts)
    return L, int(g1) + int(g2) + int(g3), 3


# ================================================================================ (answers) b725'S EVENT (4) REPLAYED
def control_answers():
    """b725 event (4): `citation answer` appended to data/b725_citation_check.txt, tracked at the lock, and N4 read REFUTED. Replayed: b725's
    commits after its lock through N4's guard as it stood, and through the repaired names, the check's output in its own bank."""
    L = ['### (answers) N4 -- tools/acts/b727.py N4_APPENDED, citation.tpl answer; instance: b725`s commits after its lock %s (event (4))' % B725_LOCK]
    act = 'b725'
    old_list = ('data/%s_steps.json' % act, 'data/%s_bank_hashes.json' % act, 'data/%s_hook_refusals.txt' % act, 'tools/mirror_prevbuild.json')
    tracked = set(_git('ls-tree', '-r', '--name-only', B725_LOCK).split())
    face = 'data/b725_registration_2026-10-30.txt'
    hs = _git('log', '--reverse', '--format=%H', '%s..%s' % (B725_LOCK, B725_CLOSE)).split()

    def reads(appended, mapped):
        out = []
        for h in hs:
            for p in _git('show', '--name-only', '--format=', h).split():
                q = mapped.get(p, p)
                if q not in appended and (q == face or q.startswith('tools/') or (q.startswith('data/%s_' % act) and q in tracked)):
                    out.append('%s %s' % (h[:8], q))
        return out
    old = reads(old_list, {})
    new = reads(A.post_lock_appended(act), {'data/b725_citation_check.txt': 'data/b725_answer_check.txt'})
    tpl = open(os.path.join(S, 'fold', 'citation.tpl'), encoding='utf-8').read()
    g1 = case(L, 'answers', 'b725`s post-lock commits, %d of them' % len(hs), 'edited %s' % (old or 'NONE'), 'edited %s' % (new or 'NONE'),
              any('b725_citation_check' in x for x in old), not any('answer_check' in x or 'citation_check' in x for x in new))
    gate = open(os.path.join(T, 'b378_lockgate.py'), encoding='utf-8').read()
    g2 = case(L, 'answers', 'the route and the lock gate', 'the route writes the citation bank ; the gate prints no exclusion', 'the route writes %s ; the gate prints post_lock_appended: %s' % (
        A.answer_banks('bNNN')[2], ', '.join(A.post_lock_appended('bNNN'))), 'answer_check' not in _git('show', '%s:tools/standing/fold/citation.tpl' % B726_CLOSE),
        "_answer_check.txt'" in tpl and 'post_lock_appended(act)' in gate)
    L.append('  what the replay leaves: %s' % (new or 'NONE'))
    return L, int(g1) + int(g2), 2


CONTROLS = dict(actcur=control_actcur, branches=control_branches, answers=control_answers)
ORDER = ('actcur', 'branches', 'answers')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.7.0, (R337)(2): shared_edits ONE LIST READ AGAINST GIT, THE CITATION BANK`S FIRST TIME, THE ANSWER CHECK`S BANK (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
        '### the instances read at their commits; each case through both routes', '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.7.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (
        ', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v170.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v170.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
