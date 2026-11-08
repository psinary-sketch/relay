# -*- coding: utf-8 -*-
"""standing/v1280.py -- THE CONTROLS OF v1.28.0 ((R358)(3)(i)-(xii)), in v1270.py's form: each instance read through the route as it stood before the
repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side.
THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the repair is read from the blob at BASE (b747's
closing), not from disk. The free memory is read and printed before each control. Each class may be run alone, one per call, in the foreground;
`--bank` writes the whole set, every class run in the one call. Written at b748 by the Write tool. Every planted address is synthetic
(planted-token-748-zz in scratch repositories); no identifier of the author is read into any string here.

  python -X utf8 -u tools/standing/v1280.py control [one|scan|gate|write|carry|row|sat|dry|rules|refusals|cite|version ...] [--bank]
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
BASE = '7d34b587'   # ### b747's closing, the toolset as v1.27.1 left it
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
TOKEN = 'planted-token-748-zz'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import citeprint as CP          # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import defectrow as DR          # noqa: E402
import figbank as FB            # noqa: E402
import onereader as OR          # noqa: E402
import repaircommits as RC      # noqa: E402
import standingdry as SD        # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(ref, rel, repo=RELAY):
    return _git('show', '%s:%s' % (ref, rel), repo=repo).replace('\r', '')


def base_src(rel):
    return show(BASE, rel)


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.27.1): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.28.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.28.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _repo(base):
    r = tempfile.mkdtemp(dir=base)
    _git('init', '-q', repo=r)
    _git('-c', 'user.email=x@x.invalid', '-c', 'user.name=x', 'commit', '-q', '--allow-empty', '-m', 'base', repo=r)
    return r


def _rm(p):
    def onerr(fn, path, _e):
        os.chmod(path, 0o700)
        fn(path)
    shutil.rmtree(p, onerror=onerr)


# ================================================================================ (i) THE ONE READER OF A SCORE
def control_one():
    L, g, n = ['### (one) (R358)(3)(i), b747 events (4), N3: A SCORE READING THE ROOT PROMPT READ ONCE; PENDING IN THE RECORD WHILE THE PROMPT IS UNBANKED'], 0, 0
    pre = json.load(io.open(os.path.join(D, 'b747_scores.json'), encoding='utf-8')).get('N3') or ['?']
    clo = json.load(io.open(os.path.join(D, 'b747_scores_close.json'), encoding='utf-8')).get('N3') or ['?']
    unread = OR.ROOT_UNREAD in ' '.join(str(x) for x in pre[1:])
    old_v = 'REFUTED'   # ### the template's line at BASE, ('HELD' if ok else 'REFUTED'), with ok False while the prompt is unread
    old_one, old_why = OR.one_reading([old_v], clo)
    new_v = OR.verdict(False, dict(ok_rest=True, unb_=None))
    new_one, new_why = OR.one_reading([new_v], clo)
    n += 1
    g += case(L, 'one', 'b747`s N3 replayed: the pre-root bank read %s with the root-prompt clause %s, every other clause clean (events (4)); the close read %s' % (
        pre[0], 'UNREAD' if unread else '### NOT UNREAD', clo[0]), 'verdict %s ; %s' % (old_v, old_why), 'verdict %s ; %s' % (new_v, new_why), not old_one, new_one and new_v == 'PENDING')
    for what, scope, ok, want in (('the root prompt banked and clean', dict(ok_rest=True, unb_=[]), True, 'HELD'),
                                  ('the root prompt banked with a fault', dict(ok_rest=True, unb_=['a sentence']), False, 'REFUTED'),
                                  ('another clause failing while the prompt is unread', dict(ok_rest=False, unb_=None), False, 'REFUTED'),
                                  ('an act module before b748 (no ok_rest in its route)', dict(unb_=None), False, 'REFUTED')):
        n += 1
        g += guard(L, 'one', what, 'verdict %s' % OR.verdict(ok, scope), OR.verdict(ok, scope) == want)
    tpl = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    old_tpl = base_src('tools/standing/fold/record.tpl')
    n += 1
    g += guard(L, 'one', 'the record template`s N3 verdict line through the one reader, its line count kept (b747 (j): acts before b735 key overrides by line)',
               'onereader calls %d ; lines %d against %d at %s' % (tpl.count('standing.onereader'), tpl.count(NL), old_tpl.count(NL), BASE),
               tpl.count('standing.onereader') == 1 and tpl.count(NL) == old_tpl.count(NL))
    return L, g, n


# ================================================================================ (ii) THE SCAN OVER THE STAGED SET, RUN BY THE COMMIT TOOL
def _places(src_text, r1, r2, act='b999'):
    ns = {'__name__': 'scan_ctl', '__file__': os.path.join(T, 'b748_address_scan.py')}
    exec(compile(src_text, 'scan_ctl', 'exec'), ns)
    ns['ROOT'], ns['PP'], ns['D'], ns['ACT'], ns['SITTING_REPOS'] = r1, r2, os.path.join(r1, 'data'), act, ()
    ns['K'].PRE_RELAY = _git('rev-parse', 'HEAD', repo=r1).strip()
    ns['K'].PRE_PP = _git('rev-parse', 'HEAD', repo=r2).strip()
    return [(k, l) for k, l, t in ns['places']() if TOKEN in t]


def control_scan():
    L, g, n = ['### (scan) (R358)(3)(ii): THE SCAN READS THE WORKING TREE, THE INDEX AND THE COMMITTED BLOBS; THE COMMIT TOOL RUNS IT OVER THE STAGED SET'], 0, 0
    base = tempfile.mkdtemp(dir=SCRATCH, prefix='v1280_scan_')
    try:
        r1, r2 = _repo(base), _repo(base)
        os.makedirs(os.path.join(r1, 'data'))
        os.makedirs(os.path.join(r1, 'tools'))
        with open(os.path.join(r1, 'data', 'b999_staged.txt'), 'w') as f:
            f.write('a line\n%s\n' % TOKEN)
        _git('add', 'data/b999_staged.txt', repo=r1)
        old_src = show(BASE, 'tools/b748_address_scan.py') or show('a11052da', 'tools/b748_address_scan.py')
        new_src = io.open(os.path.join(T, 'b748_address_scan.py'), encoding='utf-8').read()
        oh, nh = _places(old_src, r1, r2), _places(new_src, r1, r2)
        n += 1
        g += guard(L, 'scan', 'a planted address staged and not committed (a synthetic token in a scratch repository); THE FINDING AFTER b747`S CLOSE, "the scan read no staged file", '
                   'REFUTED by this control: the route before the repair found it too, inside the working tree`s one place per repository, whose count does not move',
                   'BEFORE found at %s ; AFTER found at %s' % (oh or 'NONE', nh or 'NONE'), bool(oh) and any(k == 'staged added lines' for k, _l in nh))
        with open(os.path.join(r1, 'tools', 'b999_new.py'), 'w') as f:
            f.write('# %s\n' % TOKEN)
        oh2 = [x for x in _places(old_src, r1, r2) if x[0] != 'staged added lines' and x[0] != 'working tree added lines']
        nh2 = [x for x in _places(new_src, r1, r2) if x[0] == 'untracked tool']
        n += 1
        g += case(L, 'scan', 'a planted address in the act`s untracked tool (tools/b999_new.py, never added)', 'found at %s' % (oh2 or 'NONE'), 'found at %s' % (nh2 or 'NONE'), not oh2, bool(nh2))
    finally:
        _rm(base)
    old_cm = base_src('tools/standing/commit.py')
    n += 1
    g += case(L, 'scan', 'the commit tool runs the scan before every commit and refuses a count above 0 (a planted foot carrying an occurrence)',
              'run_scan in commit.py at %s: %s' % (BASE, 'def run_scan' in old_cm),
              'scan_refusal on a foot reading address 1: %s' % CM.scan_refusal('### ### **PREVIOUS ADDRESS: 1 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ; PLACES 9 ; CONTROLS 7 OF 7 AS WANTED ; 1 s.**', 0),
              'def run_scan' not in old_cm, bool(CM.scan_refusal('### ### **PREVIOUS ADDRESS: 1 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ; PLACES 9 ; CONTROLS 7 OF 7 AS WANTED ; 1 s.**', 0)))
    base = tempfile.mkdtemp(dir=SCRATCH, prefix='v1280_run_')
    try:
        r = _repo(base)
        dd = os.path.join(r, 'data')
        os.makedirs(dd)
        with open(os.path.join(r, 'x.txt'), 'w') as f:
            f.write('x\n')
        _git('add', 'x.txt', repo=r)
        head0 = _git('rev-parse', 'HEAD', repo=r).strip()

        def refuse_scan(_act):
            raise CM.Refused('THE SCAN FOUND AN OCCURRENCE: address 1 (planted)')
        try:
            CM.run(r, 'component 1', 'a planted commit', act='b999', data=dd, row_writer=lambda *a: (0, 'no row'), scanner=refuse_scan)
            refused = False
        except CM.Refused as e:
            refused = 'THE SCAN FOUND' in str(e)
        head1 = _git('rev-parse', 'HEAD', repo=r).strip()
        n += 1
        g += guard(L, 'scan', 'a commit whose scan finds an occurrence, through run(): refused before git commit', 'refused %s ; HEAD unmoved %s' % (refused, head0 == head1), refused and head0 == head1)
    finally:
        _rm(base)
    return L, g, n


# ================================================================================ (iii) NO STANDING CHANGE BETWEEN THE GATE AND THE LOCK
def control_gate():
    L, g, n = ['### (gate) (R358)(3)(iii), b747 defects (j), (a`): A STANDING TEMPLATE`S REPAIR LANDS WITH ITS VERSION BEFORE THE GATE'], 0, 0
    commits = []
    for row in _git('log', '--reverse', '--format=%h %s', '--abbrev=8', 'f4c286c0^..8b73b2a8').split(NL):
        if row.strip():
            h, sub = row.split(' ', 1)
            commits.append((h, sub, any(x.startswith('tools/standing/') for x in _git('show', '--name-only', '--format=', h).split())))
    old_out = RC.outside('88f39b22', '8b73b2a8')
    late = RC.late(commits, 'f2dd38e0')
    n += 1
    g += case(L, 'gate', 'b747`s sequence replayed: v1.27.0 f4c286c0, the template repair 0c118109, the first gate commit f2dd38e0, VERSION moved alone in the fourth gate commit 88f39b22, the lock 8b73b2a8',
              'outside(VERSION`s 88f39b22) %s -> the lock permitted' % (old_out or 'NONE'), 'late(first gate f2dd38e0) %s -> refused' % ([h for h, _s in late] or 'NONE'), not old_out, [h for h, _s in late] == ['88f39b22'])
    ag = [h for h, _s in RC.after_gate('b747', '8b73b2a8')]
    n += 1
    g += guard(L, 'gate', 'after_gate over b747`s own step bank (six gate rows, the first read), to the lock 8b73b2a8', 'after_gate %s' % (ag or 'NONE'), ag == ['88f39b22'])
    staged = _git('show', '--name-only', '--format=', '88f39b22').split()
    n += 1
    g += case(L, 'gate', 'the gate commit 88f39b22`s staged set at the commit tool', 'the gate at %s: no staged-standing read' % BASE,
              'gate_standing_refusal: %s' % (CM.gate_standing_refusal(staged) or 'NONE')[:110], 'gate_standing_refusal' not in base_src('tools/standing/commit.py'), bool(CM.gate_standing_refusal(staged)))
    moved = [c for c in commits if c[0] != '88f39b22'] + [('88f39b22', 'v1.27.1 by a commit of its own, before the gate', True), ('9e9e9e9e', 'the gate, no standing file', False)]
    n += 1
    g += guard(L, 'gate', 'the same change landed with the version before the gate (VERSION`s commit placed before a gate carrying no standing file)',
               'late(gate 9e9e9e9e) %s' % (RC.late(moved, '9e9e9e9e') or 'NONE'), RC.late(moved, '9e9e9e9e') == [])
    return L, g, n


# ================================================================================ (iv) EVERY GIT WRITE THROUGH THE ONE-CALL TOOL
def control_write():
    L, g, n = ['### (write) (R358)(3)(iv), b747 defects (f), (k), (n), N5: ONE WRITE AT A TIME, EVERY WRITE THROUGH THE TOOL, THE OPEN ONE PRINTED'], 0, 0
    base = tempfile.mkdtemp(dir=SCRATCH, prefix='v1280_write_')
    try:
        mk = os.path.join(base, 'mark.json')
        CM.open_mark('b747 add data/b747_address_scan.txt in relay (k`s first call)', path=mk)
        try:
            CM.open_mark('b747 commit component 1 in pp (k`s second call)', path=mk)
            refused, why = False, ''
        except CM.Refused as e:
            refused, why = True, str(e)
        CM.close_mark(mk)
        old_cm = base_src('tools/standing/commit.py')
        n += 1
        g += case(L, 'write', 'b747`s (k) replayed: the add holding the write mark, the commit sent in the same message',
                  'commit.py at %s: a write mark %s -> the commit proceeds' % (BASE, 'present' if 'open_mark' in old_cm else 'absent'),
                  'refused %s: %s' % (refused, why[:120]), 'open_mark' not in old_cm, refused and 'ANOTHER WRITE OF THE ACT IS OPEN' in why and 'k`s first call' in why)
        with open(mk, 'w', encoding='utf-8') as f:
            json.dump(dict(what='a write whose process exited', pid=999999, at='2026-11-08T00:00:00Z'), f)
        CM.open_mark('the next write', path=mk)
        CM.close_mark(mk)
        n += 1
        g += guard(L, 'write', 'a stale mark (its holder exited) removed and named, the write proceeding', 'mark removed after %s' % (not os.path.exists(mk)), not os.path.exists(mk))
        r = _repo(base)
        with open(os.path.join(r, 'a.txt'), 'w') as f:
            f.write('a\n')
        out_ok = True
        try:
            CM.write_route(r, 'add', ['a.txt'], act='b999')
        except CM.Refused:
            out_ok = False
        staged = _git('diff', '--cached', '--name-only', repo=r).split()
        n += 1
        g += guard(L, 'write', 'an add through the tool in a scratch repository, the mark released', 'staged %s ; mark left %s' % (staged, os.path.exists(CM.MARK)), out_ok and staged == ['a.txt'])
        bad = []
        for verb, args in (('add', ['data/*.txt']), ('delete', ['a', 'b']), ('restore', [])):
            try:
                CM.write_route(r, verb, args, act='b999')
                bad.append(verb)
            except CM.Refused:
                pass
        n += 1
        g += guard(L, 'write', 'a glob, two branches in one delete, a restore naming nothing: each refused', 'not refused: %s' % (bad or 'NONE'), not bad)
    finally:
        _rm(base)
    return L, g, n


# ================================================================================ (v) THE CARRY BEFORE THE ACT'S FIRST COMMIT
def control_carry():
    L, g, n = ['### (carry) (R358)(3)(v), b747 defects (d), (e): THE CARRY RUNS BEFORE THE ACT_CURRENT COMMIT AND ITS SCAN'], 0, 0
    at = '22f59d27'   # ### b747's act_current commit
    ex = lambda rel: subprocess.run(['git', '-C', RELAY, 'cat-file', '-e', '%s:%s' % (at, rel)], capture_output=True).returncode == 0   # noqa: E731
    bad = CM.carry_check('b747', ex)
    n += 1
    g += case(L, 'carry', 'b747`s step-zero order replayed: its act_current commit 22f59d27, the tree at that commit', 'commit.py at %s: carry check %s -> committed' % (
        BASE, 'present' if 'carry_check' in base_src('tools/standing/commit.py') else 'absent'), 'carry_check: %s' % (bad or 'NONE')[:120],
        'carry_check' not in base_src('tools/standing/commit.py'), bool(bad))
    ex2 = lambda rel: os.path.isfile(os.path.join(RELAY, rel))   # noqa: E731  ### the disk, as commit.py's step-zero phase reads it (the carried tools were first committed at a11052da, after e80f7d60, so e80f7d60's tree cannot stand for the disk)
    n += 1
    g += guard(L, 'carry', 'b748`s carried tools on disk, the carry run before e80f7d60 (data/b748_stepzero.txt), read as commit.py reads them', 'carry_check: %s' % (CM.carry_check('b748', ex2) or 'NONE'), CM.carry_check('b748', ex2) is None)
    return L, g, n


# ================================================================================ (vi) A ROW BY ITS LETTER AND TAG; FIGURES FROM BANKS
def _old_row(L, i):
    j = i + 1
    while j < len(L) and L[j].startswith('    ') and not re.match(r"^    \(([a-z]'?)\) ", L[j]) and not L[j].startswith('    ###'):
        j += 1
    m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
    return m.group(0)[:-1] if m else None


def control_row():
    L, g, n = ['### (row) (R358)(3)(vi), b747 defects (u), (x), (l): A DEFECT ROW READ BY ITS LETTER AND TAG; THE SCREENS` FIGURES NOT A ROW`S PROSE'], 0, 0
    row = re.compile(r"^    \(([a-z]'?)\) ")
    revs = [h for h in _git('log', '--reverse', '--format=%h', '--abbrev=8', '--', 'data/b747_defects.txt').split(NL) if h.strip()]
    pick = None
    for h in revs:
        t = show(h, 'data/b747_defects.txt').split(NL)
        idx = [i for i, l in enumerate(t) if row.match(l)]
        if len(idx) >= 20:
            old = [x for x in (_old_row(t, i) for i in idx) if x]
            if len(old) < len(idx):
                pick = (h, t, idx, old)
                break
    if pick:
        h, t, idx, old = pick
        new = [x for x in (DR.read_defect_row(t, i, row) for i in idx) if x]
        tags = [DR.tag_of(x) for x in new]
        n += 1
        g += case(L, 'row', 'b747`s rows as committed at %s, before each took a closing full stop (the trail`s dry read 3 of 20, (u))' % h,
                  'rows read %d of %d' % (len(old), len(idx)), 'rows read %d of %d, each by its letter and tag (%d tagged)' % (len(new), len(idx), sum(1 for x in tags if x)),
                  len(old) < len(idx), len(new) == len(idx) and all(tags))
    else:
        n += 1
        g += guard(L, 'row', 'b747`s rows before their full stops', '### NO REVISION OF data/b747_defects.txt READ SHORT BY THE OLD READER FOUND', False)
    same = diff = 0
    differing = []
    for act in ('b740', 'b741', 'b742', 'b743', 'b744', 'b745', 'b746', 'b747'):
        t = io.open(os.path.join(D, '%s_defects.txt' % act), encoding='utf-8').read().replace('\r', '').split(NL)
        for i, l in enumerate(t):
            if row.match(l):
                o, w = _old_row(t, i), DR.read_defect_row(t, i, row)
                if o is None:
                    continue
                if o == w:
                    same += 1
                else:
                    diff += 1
                    differing.append(('%s %s' % (act, l.strip()[:4]), o.count('`') % 2 == 1 or o.endswith('..')))
    why_ok = all(x for _r, x in differing)
    differing = ['%s%s' % (r_, '' if x else ' ### UNEXPLAINED') for r_, x in differing]
    n += 1
    g += guard(L, 'row', 'every row the old reader read, over b740-b747`s banks: read the same, or differing only where the old cut fell in a backtick pair or an ellipsis',
               'same %d ; differing %d %s' % (same, diff, differing[:8] or ''), why_ok and same > 0)
    line = '**Defects** (relay data/b747_defects.txt): (l) THE SEAT`S [CLAIM ; NEW]: the class first read "The constant None and the commit present read entered"'
    old_fires = 'None' in line
    new_fires = 'None' in DR.figures_text(line)
    n += 1
    g += case(L, 'row', 'b747`s (x) replayed: the trail`s Defects line quoting row (l)`s null constant (the row as first written, (l))',
              'the unread-figure screen over the whole text: fires %s' % old_fires, 'over figures_text: fires %s' % new_fires, old_fires, not new_fires)
    n += 1
    g += guard(L, 'row', 'the null constant outside a Defects line still fires the screen', 'fires %s' % ('None' in DR.figures_text('a figure None in the entry')), 'None' in DR.figures_text('a figure None in the entry'))
    return L, g, n


# ================================================================================ (vii) THE SATISFIABILITY READ BEFORE THE GATE COMMIT
def control_sat():
    L, g, n = ['### (sat) (R358)(3)(vii), b747 defect (z), REPEAT b745 (y): THE GATE`S BANKS READ BEFORE THE GATE COMMIT, THE CONTRADICTORY CLAUSE BY NAME'], 0, 0
    planted = NL.join(['  clause                             declared cap     demand implied   units  verdict',
                       '  artifacts predicted by the face    0                3                banks  ### CONTRADICTORY ###',
                       "  VERDICT          : ### NOT SATISFIABLE -- 1 CONTRADICTORY CLAUSE(S). DO NOT SEAL."])
    old_cm = base_src('tools/standing/commit.py')
    bad = CM.satisfiable_refusal(planted, True)
    n += 1
    g += case(L, 'sat', 'b747`s gate replayed: the audit as it read after f2dd38e0 (NOT SATISFIABLE, one contradictory clause: the face`s "three banks" against a ceiling of 0, (z)); '
              'rewritten before any commit, so planted here in reg_satisfiable.py`s own format strings (:61, :67)',
              'commit.py at %s: a satisfiability read %s -> the gate committed' % (BASE, 'present' if 'satisfiable_refusal' in old_cm else 'absent'),
              'satisfiable_refusal: %s' % (bad or 'NONE')[:140], 'satisfiable_refusal' not in old_cm, bool(bad) and 'artifacts predicted' in bad)
    ok_audit = show('932b6a1d', 'data/audit_b747_reg_satisfiable.txt')
    n += 1
    g += guard(L, 'sat', 'b747`s audit as committed at 932b6a1d (JOINTLY SATISFIABLE), stamped against the face', 'satisfiable_refusal: %s' % (CM.satisfiable_refusal(ok_audit, True) or 'NONE'), CM.satisfiable_refusal(ok_audit, True) is None)
    n += 1
    g += guard(L, 'sat', 'the same audit not stamped against the face as it stands', 'refused %s' % bool(CM.satisfiable_refusal(ok_audit, False)), bool(CM.satisfiable_refusal(ok_audit, False)))
    return L, g, n


# ================================================================================ (viii) A STANDING REPAIR WITH THE RECORD'S DRY
def control_dry():
    L, g, n = ['### (dry) (R358)(3)(viii), b747 defects (r), (v): A STANDING REPAIR LANDS WITH THE RECORD`S DRY COMPOSITION RUN OVER IT'], 0, 0
    names = _git('show', '--name-only', '--format=', 'f4c286c0').split()
    v, why = SD.classify('b747', '### REFUSED: b747_events.txt resolves to no file (D:\\relay\\data\\b747_events.txt) -- the record reads no bank that is not there', 1)
    bad = SD.check(names, '', {})
    n += 1
    g += case(L, 'dry', 'v1.27.0`s (7) replayed: f4c286c0 staging tools/standing/ with no dry; the dry`s halt as (r) printed it (the events bank, written at the close)',
              'commit.py at %s: no dry read -> committed' % BASE, 'check: %s ; the halt classified %s (%s)' % ((bad or 'NONE')[:80], v, why[0][:70]),
              'standing_dry_refusal' not in base_src('tools/standing/commit.py'), bool(bad) and v == 'NOT CLEAN')
    v2, _w = SD.classify('b748', '### REFUSED: b748_corrigendum.txt resolves to no file', 1)
    n += 1
    g += guard(L, 'dry', 'a halt on a bank a component writes before the record (b748`s corrigendum)', 'classified %s' % v2, v2 == 'PENDING')
    txt = '  tools/standing/x.py sha256 %s\n### ### **THE STANDING DRY: PENDING ; FILES 1 ; COMPOSITIONS 1.**\n' % ('a' * 64)
    n += 1
    g += guard(L, 'dry', 'a dry bank naming the staged file at its sha256 accepted; at another sha256 refused',
               'same %s ; other %s' % (SD.check(['tools/standing/x.py', 'data/b748_standing_dry.txt'], txt, {'tools/standing/x.py': 'a' * 64}),
                                       bool(SD.check(['tools/standing/x.py'], txt, {'tools/standing/x.py': 'b' * 64}))),
               SD.check(['tools/standing/x.py'], txt, {'tools/standing/x.py': 'a' * 64}) is None and bool(SD.check(['tools/standing/x.py'], txt, {'tools/standing/x.py': 'b' * 64})))
    return L, g, n


# ================================================================================ (ix) THE NAVIGATOR'S DEFECTS AND THE RULE FROM (o)
def control_rules():
    L, g, n = ['### (rules) (R358)(3)(ix): THE NAVIGATOR`S (g), (h), (o) ENTERED AS THE NAVIGATOR`S; THE RULE FROM (o) IN data/b748_rules.txt'], 0, 0
    act = A.current().get('act')
    t = io.open(os.path.join(D, 'b747_defects.txt'), encoding='utf-8').read().replace('\r', '').split(NL)
    nav = ['(%s)' % m.group(1) for m in (re.match(r"^    \(([a-z]'?)\) THE NAVIGATOR'S ", l) for l in t) if m]
    n += 1
    g += guard(L, 'rules', 'b747`s rows tagged THE NAVIGATOR`S', ' '.join(nav), nav == ['(g)', '(h)', '(o)'])
    p = os.path.join(D, '%s_rules.txt' % act)
    r = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    n += 1
    g += guard(L, 'rules', 'data/%s_rules.txt carries the rule from (o)' % act, 'present %s' % bool(r),
               'a ruling cites a bank line or names the thing as unbanked, and conversation is unbanked' in r)
    return L, g, n


# ================================================================================ (x) THE HOOK'S REFUSALS; A DRY HITTING THE GUARD LETTERED
def control_refusals():
    L, g, n = ['### (refusals) (R358)(3)(x), b747 defects (c), (i), (p), (q), (y), (b`), events (1)-(3), REPEAT: THE INSTANCES PRINTED; THE GUARD`S MESSAGE'], 0, 0
    act = A.current().get('act')
    for a_ in ('b747', act):
        rows = [l for l in io.open(os.path.join(D, '%s_hook_refusals.txt' % a_), encoding='utf-8').read().split(NL) if l.strip()]
        kinds = {}
        for r in rows:
            k = r.split(' | ')[1] if ' | ' in r else '?'
            kinds[k] = kinds.get(k, 0) + 1
        L.append('  REPEAT: data/%s_hook_refusals.txt, %d refusal(s): %s' % (a_, len(rows), ', '.join('%s %d' % kv for kv in sorted(kinds.items()))))
        L += ['    ' + r[:170] for r in rows]
    src = io.open(os.path.join(S, 'prevdry.py'), encoding='utf-8').read()
    n += 1
    g += case(L, 'refusals', 'the prev-mode guard`s timeout message (events (1): a dry that hit the 590 s guard went unlettered)',
              'at %s: %s' % (BASE, 'LETTER IT' in base_src('tools/standing/prevdry.py')), 'now: LETTER IT %s' % ('LETTER IT AS A DEFECT' in src),
              'LETTER IT' not in base_src('tools/standing/prevdry.py'), 'LETTER IT AS A DEFECT' in src)
    return L, g, n


# ================================================================================ (xi) A PRINTED SOURCE LINE IS THE WHOLE LINE
def control_cite():
    L, g, n = ['### (cite) (R358)(3)(xi), b747 defect (w): A PRINTED SOURCE LINE IS THE WHOLE LINE'], 0, 0
    src = io.open(os.path.join(D, 'b725_interference.txt'), encoding='utf-8').read().replace('\r', '').split(NL)
    old = '      %5d  %s' % (11, src[10][:170])   # ### b747's printer (the scratch gen_s2_747.py :72)
    new = CP.lines(src, 11)[0]
    of = CP.check(old[13:], src, 11)
    nf = CP.check(new[13:], src, 11)
    n += 1
    g += case(L, 'cite', 'data/b725_interference.txt :11 replayed (%d characters)' % len(src[10]), 'the [:170] print: %s' % (of or 'WHOLE'), 'citeprint.lines: %s' % (nf or 'WHOLE'), bool(of), nf is None)
    n += 1
    g += guard(L, 'cite', 'a line outside the source refused', 'check :%d -> %s' % (len(src) + 5, CP.check('x', src, len(src) + 5)), bool(CP.check('x', src, len(src) + 5)))
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R358)(3)(xii): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = base_src('tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.27.1', ver == 'v1.28.0')
    return L, g, n


CONTROLS = {'one': control_one, 'scan': control_scan, 'gate': control_gate, 'write': control_write, 'carry': control_carry, 'row': control_row,
            'sat': control_sat, 'dry': control_dry, 'rules': control_rules, 'refusals': control_refusals, 'cite': control_cite, 'version': control_version}
ORDER = ('one', 'scan', 'gate', 'write', 'carry', 'row', 'sat', 'dry', 'rules', 'refusals', 'cite', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.28.0, (R358)(3)(i)-(xii): THE ONE READER OF A SCORE, THE SCAN OVER THE STAGED SET, NO STANDING CHANGE AT THE GATE, '
           'EVERY WRITE THROUGH THE ONE-CALL TOOL, THE CARRY FIRST, A ROW BY ITS LETTER AND TAG, THE SATISFIABILITY READ BEFORE THE GATE, A STANDING REPAIR WITH ITS DRY, '
           'THE NAVIGATOR`S DEFECTS AND THE RULE, THE REFUSALS, THE WHOLE CITE LINE, THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per repair: %s' % ' ; '.join(per))
    out.append('### ### **v1.28.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1280.txt' % act), NL.join(out))
        print('written data/%s_standing_v1280.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
