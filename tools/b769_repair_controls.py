# -*- coding: utf-8 -*-
"""b769, (R379)(8): THE PLANTED CONTROLS OF THE TWO KEYS, [K29] and [K30], in the form of tools/b768_repair_controls.py (its frame carried:
git, snapshot, probe, version_of, two_revisions, main; [K27]'s probe carried as [K29]'s, set to the new kind). Each key's control is added
to this tool and committed before its first run ([K30]'s at Component 2, after the merge of (4)(b)). The control reads the fault at the
commit before the repair and reads clean at the repair's commit, both printed. Read-only over the relay: each revision's files are taken by
`git show <rev>:<path>` into a scratch folder of the system's temporary directory (removed after), and each revision is probed in its own
interpreter (`python -I`), so no module of one revision is read by the other; the probe executes the standing tool's pure tables and
functions apart, runs no git command (the cadence's two git readers stubbed) and prints one JSON line; it writes nothing outside its own
snapshot folder (the held part's banks written into that folder alone, removed with it). AFTER may be the word WORKTREE: the working
tree's copies of the key's files are read in place of a commit's, for the reading before the repair's commit; that reading is printed and
never banked. --bank appends the reading to data/b769_repair_controls.txt beneath a head naming the key and both commits; nothing else is
written. The repair's commit must have the commit before it as its first parent, read and printed.

  python -X utf8 -u tools/b769_repair_controls.py <K29> <before> <after|WORKTREE> [--bank]
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = '\n'
ACT = 'b769'
BANK = os.path.join(D, 'b769_repair_controls.txt')
WORKTREE = 'WORKTREE'


def git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)
    return r.returncode, r.stdout


def snapshot(rev, paths, dest):
    """the files `paths` at `rev` (or the working tree's copies where rev is WORKTREE) under dest, at their relay paths; [(path, present)]."""
    out = []
    for p in paths:
        if rev == WORKTREE:
            src = os.path.join(ROOT, *p.split('/'))
            ok = os.path.isfile(src)
            b = open(src, 'rb').read() if ok else b''
            rc = 0 if ok else 1
        else:
            rc, b = git('show', '%s:%s' % (rev, p))
        out.append((p, rc == 0))
        if rc == 0:
            q = os.path.join(dest, *p.split('/'))
            os.makedirs(os.path.dirname(q), exist_ok=True)
            with open(q, 'wb') as fh:
                fh.write(b)
    return out


def probe(code, snap, *args):
    r = subprocess.run([sys.executable, '-X', 'utf8', '-I', '-c', code, snap] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    lines = [l for l in r.stdout.split(NL) if l.startswith('{')]
    if r.returncode != 0 or not lines:
        return dict(error='exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[-400:]))
    return json.loads(lines[-1])


def version_of(tmp):
    vp = os.path.join(tmp, 'tools', 'standing', 'VERSION')
    return io.open(vp, encoding='utf-8').read().strip() if os.path.exists(vp) else None


def two_revisions(paths, before, after, code, prefix):
    """[(name, rev, files, probe's json, VERSION)] for BEFORE and AFTER, each snapshot removed after its probe."""
    out = []
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix=prefix)
        try:
            got = snapshot(rev, paths, tmp)
            j = probe(code, tmp)
            ver = version_of(tmp)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith(prefix):
                shutil.rmtree(tmp, ignore_errors=True)
        out.append((name, rev, got, j, ver))
    return out


# ================================================================================ [K29] THE KIND OF AN ACT THAT WRITES NO PAPER AND NO LEAN
K29_PATHS = ('tools/standing/cadence.py', 'tools/standing/prevdry.py', 'tools/standing/close.py', 'tools/standing/fold/checks.tpl',
             'tools/standing/VERSION', 'data/b769_wlist.json', 'data/b768_wlist.json')   # ### tools/standing/ holds no __init__.py: a namespace package
K29_VERSION = 'v1.38.29'
LEAN, PAPER, NEITHER = 'LEAN AND NO PAPER', 'PAPER', 'NO PAPER AND NO LEAN'
QUARTERS = ('standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d')
K29_PROBE = r'''
import json, os, re, sys, types
snap = sys.argv[1]
sys.path.insert(0, os.path.join(snap, 'tools'))
sys.path.insert(1, os.path.join(snap, 'tools', 'standing'))
import standing
fake_l = types.ModuleType('standing.lsrread')
fake_l.verdict = lambda a, b: ('CLASSED', [])
def _exn(act, part, mode, tracked):
    if mode == 'prev':
        return '%s_prevrun_exercise_%s.json' % (act, part)
    if mode == 'mid':
        return '%s_mid_exercise_%s.json' % (act, part)
    n = '%s_exercise_%s.json' % (act, part)
    return '%s_exercise_%s_%s.json' % (act, part, act) if mode == 'prerun' and tracked(n) else n
fake_r = types.ModuleType('standing.repeat')
fake_r.exercise_name = _exn
sys.modules['standing.lsrread'], sys.modules['standing.repeat'] = fake_l, fake_r
standing.lsrread, standing.repeat = fake_l, fake_r
from standing import cadence as C
C._git = lambda *a: None
C._blob = lambda *a: None
QUARTERS = ('standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d')
MODES = ('prerun', 'prev', 'post-push', 'pre-push', 'mid', 'rerun')
wl = json.load(open(os.path.join(snap, 'data', 'b769_wlist.json'), encoding='utf-8'))['patterns']
wl8 = json.load(open(os.path.join(snap, 'data', 'b768_wlist.json'), encoding='utf-8'))['patterns']
out = dict(neither=getattr(C, 'NEITHER', None), hold=list(getattr(C, 'HOLD_KINDS', ()) or ()))
PLANTS = dict(day1=wl + ['PLACE-papers/day1/A_Place_to_Stand.md'], glob=wl + ['PLACE-papers/*'],
              phase15=wl + ['PLACE-papers/phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md'],
              kernel=wl + ['SIDE-explicit-formula/*'], neither=list(wl), empty=[])
kd = lambda patterns=None, act='b769': C.kind_of(act, snap, patterns=patterns)
out['kinds'] = dict(b769=kd()['kind'], b768=kd(act='b768')['kind'], b767=kd(act='b767')['kind'], b770=kd(act='b770')['kind'],
                    b768_nokernel=kd([p for p in wl8 if not p.startswith('SIDE-')], act='b768')['kind'],
                    **dict((k, kd(v)['kind']) for k, v in PLANTS.items()))
k9 = kd()
out['rule'] = [k9.get('rule'), k9.get('version')]
pk = kd(PLANTS['day1'])
def dec(part, mode, kind=None):
    if kind is None:
        return C.decide('b769', part, mode, snap, {})
    return C.decide('b769', part, mode, snap, {}, kind=kind)
out['four'] = dict(('%s %s' % (p, m), dec(p, m)['held']) for p in QUARTERS for m in MODES)
out['four_rule'] = sorted(set(str(dec(p, m).get('kind_rule')) for p in QUARTERS for m in MODES))
out['b3_post_together'] = 'together' in dec('standing-b3', 'post-push')['why']
out['planted_four'] = dict(('%s %s' % (p, m), dec(p, m, pk)['held']) for p in QUARTERS for m in MODES)
out['planted_b3_together'] = 'together' in dec('standing-b3', 'post-push', pk)['why']
import prevdry as PD
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1') + QUARTERS + ('standing-b3', 'act')
def gate_read(kind=None):
    clear, L = PD.gate('b769', parts=PARTS) if kind is None else PD.gate('b769', parts=PARTS, kind=kind)
    got = {}
    for q in PARTS:
        ln = next((l for l in L if l.startswith('    %-14s' % q)), '')
        got[q] = 'HELD' if 'HELD, NOT RUN AT THIS ACT' in ln else ('ABSENT' if 'NOT RUN (data/' in ln else ln.strip()[:60])
    return got
out['gate'] = gate_read()
out['planted_gate'] = gate_read(pk)
dd = os.path.join(snap, 'heldprobe')
os.makedirs(dd)
banks = {}
for part, mode, text in (('standing-b2a', 'pre-push', 'b769_checks_standing-b2a.txt'), ('standing-b2b', 'prerun', 'b769_arms_prerun_standing-b2b.txt'),
                         ('standing-b2c', 'mid', 'b769_checks_mid_standing-b2c.txt'), ('standing-b2d', 'prev', 'b769_prevrun_standing-b2d.txt')):
    d = dec(part, mode)
    if d['run']:
        banks[part] = 'RUNS'
        continue
    seen = set(os.listdir(dd))
    C.held(d, 'b769', snap, dd, text=text, ex_mode=mode, out=lambda *a: None)
    new = sorted(set(os.listdir(dd)) - seen)
    exn = [n for n in new if 'exercise' in n]
    ex = json.load(open(os.path.join(dd, exn[0]), encoding='utf-8')) if len(exn) == 1 else {}
    t = open(os.path.join(dd, text), encoding='utf-8').read() if text in new else ''
    banks[part] = dict(files=new, ex_mode=ex.get('mode'), run=ex.get('run'), foot=('ARMS 0 ;' in t and 'DECLARED EQ RUN NOTRUN' in t),
                       kind=(ex.get('cadence') or {}).get('kind'), kind_version=(ex.get('cadence') or {}).get('kind_version'),
                       head_rule=('(R379)(8) [K29]' in t and 'v1.38.29' in t))
out['held'] = banks
tpl = open(os.path.join(snap, 'tools', 'standing', 'fold', 'checks.tpl'), encoding='utf-8').read()
out['tpl'] = dict(guard=tpl.count("_CAD.chain_quarters_run('⟪ACT⟫', ROOT)"), quarters=tpl.count("ha.get('quarters', True)"),
                  kind_line=tpl.count("_CAD.kind_of('⟪ACT⟫', ROOT)"), lean_named=tpl.count('_CAD.LEAN_ONLY'))
i = tpl.index('def verify_ok(S):')
j = tpl.index('\ndef ', i + 1)
H = 'h' * 40
g = dict(gs=lambda *a: H, ROOT='R', ACT_NOW='b769',
         AC=types.SimpleNamespace(act_figures=lambda dd=None, roots_text=None, act=None: dict(range=list(range(624, 770)), range_last=769)),
         KS=types.SimpleNamespace(CHAIN_HALVES=(('b624', 'b658'), ('b659', 'b769'))))
exec(compile(tpl[i:j], 'verify_k29', 'exec'), g)
second = [('b%d' % k, 'AGREE', []) for k in range(659, 770)]
reads = {'b769': {'crlf': 0}, 'b680': {'corrected': 4}}
held_s = dict(half_a=dict(head=H, acts=[], reads={}, boundary={}, quarters=False), ar_verify=second, ar_reads=reads, boundary=dict(equal=True, root='r1'))
paper = dict(half_a=dict(head=H, acts=[['b%d' % k, 'AGREE'] for k in range(624, 659)], reads={}, boundary=dict(equal=True, root='r1')),
             ar_verify=second, ar_reads=reads, boundary=dict(equal=True, root='r1'))
out['verify'] = dict(held=bool(g['verify_ok'](held_s)), paper=bool(g['verify_ok'](paper)), held_neg=bool(g['verify_ok'](dict(held_s, ar_verify=second[:-1]))),
                     held_unequal=bool(g['verify_ok'](dict(held_s, boundary=dict(equal=False, root='r1')))))
print(json.dumps(out))
'''
K29_HELD = {
    'standing-b2a': dict(files=['b769_checks_standing-b2a.txt', 'b769_exercise_standing-b2a.json', 'b769_lsr_standing-b2a.json'], ex_mode='pre-push'),
    'standing-b2b': dict(files=['b769_arm_seconds_standing-b2b.json', 'b769_arms_prerun_standing-b2b.txt', 'b769_exercise_standing-b2b.json',
                                'b769_lsr_prerun_standing-b2b.json'], ex_mode='prerun'),
    'standing-b2c': dict(files=['b769_checks_mid_standing-b2c.txt', 'b769_lsr_mid_standing-b2c.json', 'b769_mid_exercise_standing-b2c.json'], ex_mode='mid'),
    'standing-b2d': dict(files=['b769_prevrun_exercise_standing-b2d.json', 'b769_prevrun_standing-b2d.json', 'b769_prevrun_standing-b2d.txt'], ex_mode='prev')}
K29_KINDS = dict(b769=NEITHER, b768=LEAN, b767=PAPER, b770=PAPER, b768_nokernel=PAPER, day1=PAPER, glob=PAPER, phase15=PAPER, kernel=LEAN,
                 neither=NEITHER, empty=NEITHER)


def control_k29(before, after):
    """(R379)(8) [K29]: the kind of an act that writes no paper and no Lean, read in each revision in its own interpreter with git stubbed (no
    git command run; the held part's banks written into the probe's own snapshot folder alone, removed with it). FAULT: no such kind; b769,
    whose (W) list names no kernel's files and no paper's path, of the kind PAPER, its four chain parts standing-b2a to standing-b2d required
    (run) in the pre-push mode and required (absent) at the prev-mode dry's gate. CLEAN: b769 of the kind NO PAPER AND NO LEAN from its (W)
    list, the kind's rule (R379)(8) [K29] at v1.38.29; b768 of LEAN AND NO PAPER as before; b768's list with its kernel's patterns taken out,
    read at b768, PAPER (the kind in force from b769); b767 and b770 (no list) PAPER; the planted lists a paper's path under day1/ or
    phase1.5/, or a glob reaching one, PAPER; b769's list with a kernel's pattern LEAN AND NO PAPER; b769's own list and an empty list the
    new kind; b769's four NOT RUN in every mode of the suite, prerun, prev, post-push, pre-push, mid and rerun, each under [K29]'s rule, and
    the planted paper act's four required in every mode; standing-b3's post-push group reduced to itself at b769 and the chain group whole
    at the planted act; the prev-mode dry's gate holding the four at b769 and requiring them at the planted act, the other six parts read as
    before; held() writing each not-run part's banks under the mode's own names (pre-push, prerun, mid, prev), ARMS 0 and NOTRUN in the
    footer, the kind and its version in the exercise bank and the rule and version in the bank's head; the template reading the kind's own
    names at the first half's line and no longer printing LEAN AND NO PAPER there, the kind at the b3 join and the predicate's quarters kept;
    G-ACTROOT-VERIFY's predicate passing b769's second half with the boundary, a whole chain as before, and failing a dropped act or an
    unequal boundary; VERSION v1.38.29."""
    L, res = [], {}
    for name, rev, got, j, ver in two_revisions(K29_PATHS, before, after, K29_PROBE, 'b769k29_'):
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (kind)    the new kind %s ; the kinds held %s ; %s ; the rule at b769 %s' % (
            j['neither'], j['hold'] or 'NONE', ' ; '.join('%s %s' % kv for kv in sorted(j['kinds'].items())), j['rule']))
        fv = sorted(set(j['four'].values()))
        L.append('    (four)    b769`s standing-b2a to standing-b2d in the modes prerun, prev, post-push, pre-push, mid, rerun: %s ; pre-push %s ; '
                 'the rule %s' % (', '.join(fv), ', '.join(j['four']['%s pre-push' % p] for p in QUARTERS), ', '.join(j['four_rule'])))
        L.append('    (planted) the planted act of the other kind (a paper`s path under day1/), its four in the six modes: %s ; standing-b3`s '
                 'post-push group whole %s' % (', '.join(sorted(set(j['planted_four'].values()))), j['planted_b3_together']))
        L.append('    (b3)      b769`s standing-b3 in the post-push mode read with the chain group: %s' % j['b3_post_together'])
        L.append('    (gate)    the prev-mode dry`s gate at b769: %s' % ' ; '.join('%s %s' % (q, j['gate'][q]) for q in sorted(j['gate'])))
        L.append('    (gate)    at the planted act: the four %s' % ', '.join(j['planted_gate'][q] for q in QUARTERS))
        for p in QUARTERS:
            h = j['held'].get(p)
            L.append('    (held)    %s: %s' % (p, h if isinstance(h, str) else 'files %s ; exercise mode %s ; run %s ; footer ARMS 0 and NOTRUN %s ; kind %s at %s ; '
                                                   'the head`s rule and version %s' % (', '.join(h['files']), h['ex_mode'], h['run'], h['foot'], h['kind'],
                                                                                         h['kind_version'], h['head_rule'])))
        L.append('    (tpl)     the kind at the b3 join %d, the predicate`s quarters %d, the first half`s line by the kind`s own names %d, LEAN AND '
                 'NO PAPER named there %d' % (j['tpl']['guard'], j['tpl']['quarters'], j['tpl']['kind_line'], j['tpl']['lean_named']))
        L.append('    (verify)  G-ACTROOT-VERIFY`s predicate: b769`s second half with the boundary %s ; a whole chain %s ; an act dropped %s ; the '
                 'boundary unequal %s' % (j['verify']['held'], j['verify']['paper'], j['verify']['held_neg'], j['verify']['held_unequal']))
        fault = (j['neither'] is None and j['kinds'].get('b769') == PAPER and all(j['four']['%s pre-push' % p] == 'run' for p in QUARTERS)
                 and all(j['gate'][q] == 'ABSENT' for q in QUARTERS))
        held_ok = all(isinstance(j['held'].get(p), dict) and j['held'][p]['files'] == K29_HELD[p]['files'] and j['held'][p]['ex_mode'] == K29_HELD[p]['ex_mode']
                      and j['held'][p]['run'] == 0 and j['held'][p]['foot'] is True and j['held'][p]['kind'] == NEITHER
                      and j['held'][p]['kind_version'] == K29_VERSION and j['held'][p]['head_rule'] is True for p in QUARTERS)
        clean = (j['neither'] == NEITHER and sorted(j['hold']) == sorted([LEAN, NEITHER]) and j['kinds'] == K29_KINDS
                 and j['rule'] == ['(R379)(8) [K29]', K29_VERSION]
                 and set(j['four'].values()) == {'not run'} and j['four_rule'] == ['(R379)(8) [K29]'] and set(j['planted_four'].values()) == {'run'}
                 and j['b3_post_together'] is False and j['planted_b3_together'] is True
                 and all(j['gate'][q] == ('HELD' if q in QUARTERS else 'ABSENT') for q in j['gate'])
                 and all(j['planted_gate'][q] == 'ABSENT' for q in j['planted_gate'])
                 and held_ok and j['tpl']['guard'] >= 2 and j['tpl']['quarters'] >= 1 and j['tpl']['kind_line'] >= 1 and j['tpl']['lean_named'] == 0
                 and j['verify'] == dict(held=True, paper=True, held_neg=False, held_unequal=False) and ver == K29_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


CONTROLS = dict(K29=control_k29)


def main(argv):
    if len(argv) < 3 or argv[0] not in CONTROLS:
        sys.exit(__doc__ + '\nkeys: %s' % ', '.join(sorted(CONTROLS)))
    key, before, after = argv[0], argv[1], argv[2]
    wt = after == WORKTREE
    if wt and '--bank' in argv:
        sys.exit('### THE WORKTREE READING IS NEVER BANKED -- NOTHING READ')
    rc, b = git('rev-parse', before)
    rc2, a = (0, WORKTREE.encode()) if wt else git('rev-parse', after)
    rc3, p = (0, b) if wt else git('rev-parse', '%s^1' % after)
    if rc or rc2 or rc3:
        sys.exit('### A REVISION DOES NOT RESOLVE -- NOTHING READ')
    b, a, p = b.decode().strip(), a.decode().strip(), p.decode().strip()
    head = ['## [%s] THE PLANTED CONTROL (%s): BEFORE relay %s, THE REPAIR`S COMMIT %s, its first parent %s -- %s' % (
        key, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), b[:8], 'THE WORKING TREE' if wt else 'relay ' + a[:8], 'not read' if wt else p[:8],
        'THE WORKING TREE, READ BEFORE THE REPAIR`S COMMIT, NOT BANKED' if wt else ('THE COMMIT BEFORE' if p == b else 'NOT THE COMMIT BEFORE'))]
    L, ok = CONTROLS[key](b, WORKTREE if wt else a)
    ok = ok and p == b
    L = head + L + ['### ### **[%s] THE CONTROL %s: THE FAULT READ BEFORE AND CLEAN AFTER: %s.**' % (key, 'AS WANTED' if ok else 'NOT AS WANTED', ok), '']
    print(NL.join(L))
    if '--bank' in argv:
        prior = io.open(BANK, encoding='utf-8').read() if os.path.exists(BANK) else (
            'b769 -- THE PLANTED CONTROLS OF THE TWO KEYS, (R379)(8), appended by tools/b769_repair_controls.py --bank' + NL + NL)
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(prior.rstrip(NL) + NL + NL + NL.join(L))
        os.replace(BANK + '.tmp', BANK)
        print('appended to data/b769_repair_controls.txt')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main(sys.argv[1:])
