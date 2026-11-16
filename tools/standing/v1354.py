# -*- coding: utf-8 -*-
"""standing/v1354.py -- THE CONTROLS OF v1.35.4, (R367)(3): THE ROUTE FOR KERNEL WRITES, in v1353.py's form.
b745 committed in a kernel by plain git from a scratch clone (relay data/b745_commands.txt :375-:376); since v1.29.0 the hook refuses a git
write by plain git and tools/standing/commit.py took two repositories, so no kernel was written after b745 and b756's README route halted
there. v1.35.4 teaches the one-call tool SIDE-explicit-formula and SIDE-dirichlet-mod-24, opened for b757 alone. BEFORE is the tree as BASE
left it (relay 858b906f, the c1 route's banks); AFTER the working tree. THE COMPILE CONTROL RUNS FIRST; the free memory is printed before each
control. The planted cases run in temporary repositories this tool makes, each standing for a kernel under the kernel's key, with the relay's
commit identity copied into their own config (read, never printed); nothing is written but this bank and those folders, which it removes.

  (third)    a write ordered in a third kernel refused by name before anything is read, at the tool's own entry; a kernel refused while an
             act its ruling does not open runs; relay and PLACE-papers unmoved.
  (branch)   the push-<act>-<word> form; a kernel branch made at a named commit and checked out; a name outside the form refused.
  (merge)    a merge ordered on a branch outside the form refused; a clean merge left open and concluded by the commit route, its second parent
             read back; a conflict in the file the ruling names left for the seat, a commit refused while it stands conflicted, the union
             resolved, added and concluded; a conflict in a file the ruling does not name aborted with nothing concluded.
  (commit)   a kernel's commit refused on main, with another identity, with a scan that does not name the kernel, and at the gate phase;
             made on the push branch with every condition met; the delete route forced for the control's branch alone.
  (scan)     the act's scan names both kernels among the repositories it read; tools/standing/commit.py run_scan returns the run's text.
  (record)   fold/record.tpl's step route carries the kernels of commit.py KERNELS.
  (identity) the kernel's identity against the relay's; both kernels resolve the relay's noreply identity.
  (version)  tools/standing/VERSION moved to v1.35.4.
  (live)     after the standing commit and the seat's calls, read only: the commit on push-b757-control in each kernel, its row, its parent the
             kernel's main, the branch deleted, the kernel back on main and clean; banked apart (data/<act>_standing_v1354_live.txt).

  python -X utf8 -u tools/standing/v1354.py control [third|branch|merge|commit|scan|record|identity|version ...] [--bank]
  python -X utf8 -u tools/standing/v1354.py control live [--bank]
"""
import ast
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '858b906f'   # ### the relay's HEAD before this change (b757 component 1, step 9)
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)
import commit as NEW            # noqa: E402

FLAG = (False, 'a planted clear flag', {})
STUB_ROW = (lambda *a: (0, 'no row (a control)'))


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.3): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.35.4): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.35.3): %s -> (alike at both is wanted)' % at_base,
          '      AFTER  (v1.35.4): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def after(L, cls, what, on_disk, holds):
    L += ['  (%s) %s' % (cls, what), '      AFTER  (v1.35.4): %s -> %s' % (on_disk, 'PASSES' if holds else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def old_commit():
    """BASE's tools/standing/commit.py as a module (its source from git, executed in a fresh namespace)."""
    m = types.ModuleType('commit_v1353')
    m.__file__ = os.path.join(S, 'commit.py')
    exec(compile(V.show(BASE, 'tools/standing/commit.py'), 'commit.py@' + BASE, 'exec'), m.__dict__)   # noqa: S102
    return m


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout.strip()


def _rm(path):
    def onerr(fn, p, _e):
        os.chmod(p, stat.S_IWRITE)
        fn(p)
    shutil.rmtree(path, onerror=onerr)


def trial(fn):
    """(refused, the message) for a call that may raise commit.Refused or SystemExit."""
    try:
        r = fn()
        return False, str(r)[:200]
    except SystemExit as e:
        return True, str(e)[:220]
    except Exception as e:  # noqa: BLE001  (BASE's module raises its own Refused class; any other exception is raised on)
        if type(e).__name__ == 'Refused':
            return True, str(e)[:220]
        raise


class Planted(object):
    """a temporary repository standing for a kernel: main with print_targets.txt, A.lean and B.lean; branches each changing one file; the
    relay's identity in its own config; its own write mark and data folder."""

    def __init__(self):
        self.root = tempfile.mkdtemp(prefix='v1354_')
        self.repo = os.path.join(self.root, 'k')
        self.data = os.path.join(self.root, 'data')
        self.mark = os.path.join(self.root, 'mark.json')
        os.mkdir(self.repo)
        os.mkdir(self.data)
        r = self.repo
        g(r, 'init', '-q', '-b', 'main')
        e, n = NEW._identity(RELAY)
        g(r, 'config', 'user.email', e)
        g(r, 'config', 'user.name', n)
        g(r, 'config', 'core.autocrlf', 'false')
        self.put({'print_targets.txt': 'Mod.A\nMod.B\n', 'A.lean': 'x\n', 'B.lean': 'y\n'}, 'base')
        self.main = g(r, 'rev-parse', 'HEAD')
        for name, files in (('t-clean', {'B.lean': 'y2\n'}), ('t-named', {'print_targets.txt': 'Mod.A\nMod.B\nMod.C\n'}),
                            ('t-named2', {'print_targets.txt': 'Mod.A\nMod.B\nMod.D\n'}), ('t-unnamed', {'A.lean': 'x1\n'}),
                            ('t-unnamed2', {'A.lean': 'x2\n'})):
            g(r, 'checkout', '-q', '-b', name, self.main)
            self.put(files, name)
        g(r, 'checkout', '-q', 'main')

    def put(self, files, msg):
        for k, v in files.items():
            with open(os.path.join(self.repo, k), 'w', encoding='utf-8', newline='\n') as f:
                f.write(v)
        g(self.repo, 'add', '--', *files)
        g(self.repo, 'commit', '-q', '-m', msg)

    def tip(self, b):
        return g(self.repo, 'rev-parse', b)

    def write(self, verb, args, act='b757', key=EF):
        return trial(lambda: NEW.write_route(key, verb, args, act=act, repo=self.repo, mark_path=self.mark))

    def commit(self, words, phase='component 1', scanner=None, act='b757', key=EF):
        sc = scanner or (lambda a: '## THE REPOSITORIES READ (a control): relay; PLACE-papers; %s' % key)
        return trial(lambda: NEW.run(key, phase, words, act=act, data=self.data, row_writer=STUB_ROW, scanner=sc, flag=FLAG, repo=self.repo))

    def state(self):
        return dict(head=g(self.repo, 'rev-parse', 'HEAD'), branch=NEW._head_branch(self.repo), merging=NEW._merging(self.repo),
                    dirty=len(NEW._dirty(self.repo)))

    def close(self):
        _rm(self.root)


# ================================================================================ (third)
def control_third():
    L, gd, n = ['### (third): A WRITE ORDERED IN A THIRD KERNEL, OR IN A KERNEL THE ACT DOES NOT OPEN'], 0, 0
    old = old_commit()
    ro, mo = trial(lambda: old.main(['SIDE-kernel', 'add', 'README.md']))
    rn, mn = trial(lambda: NEW.main(['SIDE-kernel', 'add', 'README.md']))
    rc, mc = trial(lambda: NEW.main(['SIDE-kernel', 'component 2', 'a planted commit']))
    n += 1
    gd += both(L, 'third', 'the tool`s own entry, `commit.py SIDE-kernel add README.md` and `SIDE-kernel "component 2" ...`',
               'refused %s by the usage text, the name unprinted (%s)' % (ro, 'SIDE-kernel' in mo),
               'add refused %s (%s) ; commit refused %s ; nothing read beyond the act record' % (rn, mn[:110], rc),
               ro, rn and rc and 'NOT A REPOSITORY THE TOOL WRITES' in mn and 'NOT A REPOSITORY THE TOOL WRITES' in mc)
    reads = dict(((k, a), NEW.repo_refusal(k, a)) for k, a in ((EF, 'b757'),(M24, 'b757'), (EF, 'b758'), (M24, 'b756'), ('relay', 'b758'), ('pp', 'b758'),
                                                          ('SIDE-kernel', 'b757'), ('SIDE-lv-conservation', 'b757')))
    n += 1
    gd += case(L, 'third', 'repo_refusal by act: the two kernels at b757, at b758 and b756; relay and pp at b758; two other kernels at b757',
               'the kernels in REPOS: %s' % sorted(k for k in old.REPOS if k not in ('relay', 'pp')),
               'opened %s ; refused %s' % (sorted('%s@%s' % k for k, v in reads.items() if v is None), sorted('%s@%s' % k for k, v in reads.items() if v)),
               EF not in old.REPOS,
               reads[(EF, 'b757')] is None and reads[(M24, 'b757')] is None and reads[('relay', 'b758')] is None and reads[('pp', 'b758')] is None
               and all(reads[k] for k in ((EF, 'b758'), (M24, 'b756'), ('SIDE-kernel', 'b757'), ('SIDE-lv-conservation', 'b757'))))
    return L, gd, n


# ================================================================================ (branch)
def control_branch():
    L, gd, n = ['### (branch): THE ACT`S PUSH BRANCH IN A KERNEL, MADE AT A NAMED COMMIT AND CHECKED OUT'], 0, 0
    old = old_commit()
    names = ('push-b757-join', 'push-b757-coeff', 'push-b757-control-ef', 'main', 'push-b756-join', 'push-b757-', 'join', 'push-b757-Join', 'push-b7570-x')
    got = dict((k, NEW.push_branch_ok('b757', k)) for k in names)
    n += 1
    gd += after(L, 'branch', 'the form push-<act>-<word> over %d names' % len(names), 'taken %s' % sorted(k for k, v in got.items() if v),
                sorted(k for k, v in got.items() if v) == ['push-b757-coeff', 'push-b757-control-ef', 'push-b757-join'])
    p = Planted()
    try:
        tc = p.tip('t-clean')
        bo, mo = trial(lambda: old.write_route(p.repo, 'branch', ['push-b757-ctl', p.main], act='b757'))
        r1, m1 = p.write('branch', ['feature-x', p.main])
        r2, m2 = p.write('branch', ['push-b757-ctl', tc])
        s2 = p.state()
        r3, m3 = p.write('branch', ['push-b757-ctl', p.main])
        r4, m4 = p.write('branch', ['push-b757-two'])
    finally:
        p.close()
    n += 1
    gd += case(L, 'branch', 'a kernel branch at a named commit (the planted kernel`s t-clean tip), checked out',
               'BASE`s branch write: refused %s (%s)' % (bo, mo[:90]),
               'outside the form refused %s ; made %s, checked out %s, HEAD the named tip %s ; again refused %s ; no commit named refused %s' % (
                   r1, not r2, s2['branch'], s2['head'] == tc, r3, r4),
               bo, r1 and not r2 and s2['branch'] == 'push-b757-ctl' and s2['head'] == tc and r3 and r4)
    return L, gd, n


# ================================================================================ (merge)
def control_merge():
    L, gd, n = ['### (merge): ONE NAMED COMMIT MERGED INTO THE PUSH BRANCH, NO FAST-FORWARD, CONCLUDED BY THE COMMIT ROUTE'], 0, 0
    old = old_commit()
    p = Planted()
    try:
        t = dict((b, p.tip(b)) for b in ('t-clean', 't-named', 't-named2', 't-unnamed', 't-unnamed2'))
        r0, m0 = p.write('merge', [t['t-clean']])
        s0 = p.state()
        n += 1
        gd += case(L, 'merge', 'a merge ordered while main is checked out', 'merge among the writes: %s' % ('merge' in old.WRITES),
                   'refused %s (%s) ; HEAD unmoved %s ; MERGE_HEAD %s' % (r0, m0[:100], s0['head'] == p.main, s0['merging'] or 'none'),
                   'merge' not in old.WRITES, r0 and 'OUTSIDE THE push-b757-* FORM' in m0 and s0['head'] == p.main and not s0['merging'])
        p.write('branch', ['push-b757-ctl', p.main])
        r1, m1 = p.write('merge', [t['t-clean']])
        r1c, m1c = p.commit('the clean merge concluded')
        h1 = g(p.repo, 'rev-parse', 'HEAD')
        par1 = g(p.repo, 'log', '-1', '--format=%P', h1).split()
        n += 1
        gd += after(L, 'merge', 'a clean merge left open, then concluded by the commit route',
                    'merge %s (%s) ; concluded %s (%s) ; parents %s ; second parent the merged tip %s' % (
                        not r1, m1[:70], not r1c, m1c[:60], len(par1), par1[1:] == [t['t-clean']]),
                    not r1 and 'MERGED WITHOUT CONFLICT' in m1 and not r1c and len(par1) == 2 and par1[1] == t['t-clean'])
        p.write('merge', [t['t-named']])
        p.commit('the named file merged clean')
        h2 = g(p.repo, 'rev-parse', 'HEAD')
        r3, m3 = p.write('merge', [t['t-named2']])
        s3 = p.state()
        r3e, m3e = p.commit('a commit while the named file stands conflicted')
        with open(os.path.join(p.repo, 'print_targets.txt'), 'w', encoding='utf-8', newline='\n') as f:
            f.write('Mod.A\nMod.B\nMod.C\nMod.D\n')
        ra, ma = p.write('add', ['print_targets.txt'])
        r3c, m3c = p.commit('the named conflict resolved as the union')
        h3 = g(p.repo, 'rev-parse', 'HEAD')
        par3 = g(p.repo, 'log', '-1', '--format=%P', h3).split()
        lines = g(p.repo, 'show', 'HEAD:print_targets.txt').split('\n')
        n += 1
        gd += after(L, 'merge', 'a conflict in print_targets.txt, the file (R367)(4) names: left open; a commit refused while it stands '
                    'conflicted; resolved as the union, added and concluded',
                    'left open %s (%s) ; MERGE_HEAD %s ; the commit refused %s (%s) ; added %s ; concluded %s ; parents %s, the second the merged '
                    'tip %s ; the lines %s' % (not r3, m3[:60], bool(s3['merging']), r3e, m3e[:50], not ra, not r3c, len(par3), par3[1:] == [t['t-named2']], lines),
                    not r3 and 'THE RULING NAMES' in m3 and s3['merging'] and r3e and 'LEFT CONFLICTED' in m3e and not ra and not r3c
                    and len(par3) == 2 and par3[0] == h2 and par3[1] == t['t-named2'] and lines == ['Mod.A', 'Mod.B', 'Mod.C', 'Mod.D'])
        p.write('merge', [t['t-unnamed']])
        p.commit('the unnamed file merged clean')
        h4 = g(p.repo, 'rev-parse', 'HEAD')
        r4, m4 = p.write('merge', [t['t-unnamed2']])
        s4 = p.state()
        n += 1
        gd += after(L, 'merge', 'a conflict in A.lean, a file the ruling does not name: aborted, nothing concluded',
                    'refused %s (%s) ; HEAD unmoved %s ; MERGE_HEAD %s ; tracked changes %d' % (r4, m4[:120], s4['head'] == h4, s4['merging'] or 'none', s4['dirty']),
                    r4 and 'DOES NOT NAME' in m4 and s4['head'] == h4 and not s4['merging'] and s4['dirty'] == 0)
        pure = (NEW.conflict_refusal('b757', EF, ['print_targets.txt']), NEW.conflict_refusal('b757', EF, ['print_targets.txt', 'A.lean']),
                NEW.conflict_refusal('b757', M24, ['print_targets.txt']), NEW.conflict_refusal('b758', EF, ['print_targets.txt']))
        n += 1
        gd += after(L, 'merge', 'conflict_refusal: the named file alone at b757 in SIDE-explicit-formula; with A.lean beside it; in SIDE-dirichlet-mod-24; at b758',
                    'refused: %s' % [bool(x) for x in pure], [bool(x) for x in pure] == [False, True, True, True])
        r5, m5 = trial(lambda: NEW.write_route('relay', 'merge', ['HEAD'], act='b757', mark_path=p.mark))
        n += 1
        gd += after(L, 'merge', 'a merge ordered in the relay', 'refused %s (%s)' % (r5, m5[:90]), r5 and 'A KERNEL`S ALONE' in m5)
    finally:
        p.close()
    return L, gd, n


# ================================================================================ (commit)
def control_commit():
    L, gd, n = ['### (commit): A KERNEL`S COMMIT AND ITS CONDITIONS; THE DELETE ROUTE'], 0, 0
    old = old_commit()
    p = Planted()
    try:
        with open(os.path.join(p.repo, 'B.lean'), 'a', encoding='utf-8', newline='\n') as f:
            f.write('z\n')
        g(p.repo, 'add', '--', 'B.lean')
        r0, m0 = p.commit('a planted commit on main')
        n += 1
        gd += case(L, 'commit', 'a staged change committed while main is checked out',
                   'BASE`s run in a kernel key: %s' % (EF in old.REPOS), 'refused %s (%s) ; HEAD unmoved %s' % (r0, m0[:90], p.state()['head'] == p.main),
                   EF not in old.REPOS, r0 and 'OUTSIDE THE push-b757-* FORM' in m0 and p.state()['head'] == p.main)
        g(p.repo, 'reset', '-q', '--hard', 'HEAD')
        p.write('branch', ['push-b757-ctl', p.main])
        with open(os.path.join(p.repo, 'B.lean'), 'a', encoding='utf-8', newline='\n') as f:
            f.write('z\n')
        p.write('add', ['B.lean'])
        e, nm = NEW._identity(RELAY)
        g(p.repo, 'config', 'user.email', 'someone@example.org')
        r1, m1 = p.commit('a commit under another identity')
        g(p.repo, 'config', 'user.email', e)
        r2, m2 = p.commit('a commit whose scan does not name the kernel', scanner=lambda a: '## THE REPOSITORIES READ (a control): relay; PLACE-papers')
        r3, m3 = p.commit('', phase='gate')
        r4, m4 = trial(lambda: NEW.run(EF, 'component 1', 'a commit of another act', act='b758', data=p.data, row_writer=STUB_ROW,
                                       scanner=lambda a: '## THE REPOSITORIES READ: %s' % EF, flag=FLAG, repo=p.repo))
        held = p.state()['head'] == p.main
        n += 1
        gd += after(L, 'commit', 'refused with another identity, with a scan not naming the kernel, at the gate phase, and at b758; nothing committed',
                    'identity %s ; scan %s ; gate %s ; b758 %s ; HEAD unmoved %s' % (r1, r2, r3, r4, held),
                    r1 and 'IDENTITY' in m1 and r2 and 'DID NOT READ THE KERNEL' in m2 and r3 and 'NO GATE IN A KERNEL' in m3 and r4 and 'DOES NOT OPEN' in m4 and held)
        r5, m5 = p.commit('a planted kernel commit')
        h5 = g(p.repo, 'rev-parse', 'HEAD')
        n += 1
        gd += after(L, 'commit', 'every condition met: made on the push branch, its subject read back, its parent the branch`s base',
                    'made %s (%s) ; parent %s ; subject %r' % (not r5, m5[:60], g(p.repo, 'log', '-1', '--format=%P', h5) == p.main, g(p.repo, 'log', '-1', '--format=%s', h5)),
                    not r5 and g(p.repo, 'log', '-1', '--format=%P', h5) == p.main and g(p.repo, 'log', '-1', '--format=%s', h5) == 'b757 component 1: a planted kernel commit')
        rd0, md0 = p.write('delete', ['push-b757-ctl'])
        p.write('switch', ['main'])
        rd1, md1 = p.write('delete', ['push-b757-ctl'])
        g(p.repo, 'branch', 'push-b757-control-ef', h5)
        rd2, md2 = p.write('delete', ['push-b757-control-ef'])
        gone = not NEW._commit_of(p.repo, 'refs/heads/push-b757-control-ef')
        rd3, md3 = p.write('delete', ['t-clean'])
        n += 1
        gd += after(L, 'commit', 'the delete route: the checked-out branch refused; an unmerged push branch refused by -d; the control`s branch '
                    'forced; a branch outside the form refused',
                    'checked out %s ; unmerged %s (%s) ; control deleted %s ; outside %s' % (rd0, rd1, md1[:60], not rd2 and gone, rd3),
                    rd0 and rd1 and not rd2 and gone and rd3)
    finally:
        p.close()
    return L, gd, n


# ================================================================================ (scan)
def control_scan():
    L, gd, n = ['### (scan): THE ACT`S SCAN NAMES THE KERNELS IT READ'], 0, 0
    act = A.current().get('act')
    rel = 'tools/%s_address_scan.py' % act
    base_src = V.show(BASE, rel) or ''
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(RELAY, *rel.split('/')), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=RELAY)
    out = r.stdout or ''
    line = [l for l in out.split('\n') if l.startswith('## THE REPOSITORIES READ')]
    n += 1
    gd += case(L, 'scan', 'the act`s scan run without --bank (writes nothing): its repositories line',
               'the line in BASE`s scan: %s' % ('## THE REPOSITORIES READ' in base_src),
               'exit %d ; %s ; names %s %s, %s %s, SIDE-kernel %s' % (r.returncode, (line[0][:150] if line else 'NO LINE'), EF, NEW.scan_names(out, EF),
                                                                    M24, NEW.scan_names(out, M24), NEW.scan_names(out, 'SIDE-kernel')),
               '## THE REPOSITORIES READ' not in base_src,
               r.returncode == 0 and NEW.scan_names(out, EF) and NEW.scan_names(out, M24) and not NEW.scan_names(out, 'SIDE-kernel'))
    src = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read()
    old_src = V.show(BASE, 'tools/standing/commit.py') or ''
    n += 1
    gd += case(L, 'scan', 'run_scan returns the run`s text, which a kernel`s commit reads', 'returns it: %s' % ('return out   # ### v1.35.4' in old_src),
               'returns it: %s' % ('return out   # ### v1.35.4' in src), 'return out   # ### v1.35.4' not in old_src, 'return out   # ### v1.35.4' in src)
    return L, gd, n


# ================================================================================ (record)
def control_record():
    L, gd, n = ['### (record): THE STEP ROUTE`S REPOSITORIES (tools/standing/fold/record.tpl)'], 0, 0
    src = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    old_src = V.show(BASE, 'tools/standing/fold/record.tpl') or ''
    head = 'STEP_REPOS = dict(relay=ROOT, pp=PP, **'
    ln = [l for l in src.split('\n') if l.startswith(head)]
    got = ast.literal_eval(ln[0][len(head):ln[0].index(')   #')]) if ln else None
    count = (len(src.split('\n')), len(old_src.split('\n')))
    n += 1
    gd += case(L, 'record', 'STEP_REPOS beside relay and pp, in the one line (the template`s line count kept: the act modules override it by number)',
               'the kernels: %s' % any(l.startswith(head) for l in old_src.split('\n')),
               'the kernels %s ; equal to commit.py KERNELS %s ; lines %d against BASE`s %d' % (sorted(got or {}), got == NEW.KERNELS, count[0], count[1]),
               not any(l.startswith(head) for l in old_src.split('\n')), got == NEW.KERNELS and count[0] == count[1])
    return L, gd, n


# ================================================================================ (identity)
def control_identity():
    L, gd, n = ['### (identity): THE KERNEL`S COMMIT IDENTITY (read, never printed)'], 0, 0
    rel = NEW._identity(RELAY)
    pure = (NEW.identity_refusal(rel, rel), NEW.identity_refusal(('someone@example.org', rel[1]), rel), NEW.identity_refusal((rel[0], 'Someone'), rel),
            NEW.identity_refusal(('', ''), rel), NEW.identity_refusal(('a@example.org', 'A'), ('a@example.org', 'A')))
    n += 1
    gd += after(L, 'identity', 'identity_refusal: equal; another address; another name; none; equal but not the noreply form',
                'refused: %s' % [bool(x) for x in pure], [bool(x) for x in pure] == [False, True, True, True, True])
    live = dict((k, NEW.identity_refusal(NEW._identity(NEW.KERNELS[k]), rel)) for k in sorted(NEW.KERNELS))
    n += 1
    gd += after(L, 'identity', 'the two kernels as they stand, against the relay', 'refused: %s' % dict((k, bool(v)) for k, v in live.items()),
                not any(live.values()))
    return L, gd, n


# ================================================================================ (version)
def control_version():
    L, gd, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    gd += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.3', ver == 'v1.35.4')
    return L, gd, n


# ================================================================================ (live), after the standing commit and the seat's calls
def control_live():
    L, gd, n = ['### (live): THE COMMIT ON push-b757-control IN EACH KERNEL, READ BACK AFTER THE SEAT`S CALLS (nothing written here)'], 0, 0
    act = A.current().get('act')
    rows = (A.jl('%s_steps.json' % act) or {}).get('rows') or []
    for k in sorted(NEW.KERNELS):
        repo = NEW.KERNELS[k]
        mine = [r for r in rows if r.get('repo') == k and 'control' in (r.get('subject') or '')]
        main = g(repo, 'rev-parse', 'main')
        c = mine[-1]['commit'] if mine else ''
        typ = g(repo, 'cat-file', '-t', c) if c else ''
        par = g(repo, 'log', '-1', '--format=%P', c) if c else ''
        subj = g(repo, 'log', '-1', '--format=%s', c) if c else ''
        br = [b for b in g(repo, 'for-each-ref', '--format=%(refname:short)', 'refs/heads/push-%s-*' % act).split('\n') if b.strip()]
        st = NEW._dirty(repo)
        n += 1
        gd += after(L, 'live', '%s: the control commit by the tool`s route, its row, read back, the branch deleted by the tool`s route' % k,
                    'rows %d ; commit %s a %s ; parent the kernel`s main %s ; subject %r ; push-%s-* branches now %s ; HEAD %s on %s ; tracked changes %d ; '
                    'main %s' % (len(mine), c[:8] or 'NONE', typ or 'nothing', par == main, subj[:90], act, br or 'NONE', g(repo, 'rev-parse', '--short=8', 'HEAD'),
                                 NEW._head_branch(repo), len(st), main[:8]),
                    len(mine) == 1 and typ == 'commit' and par == main and subj.startswith('%s component 1: ' % act) and not br
                    and NEW._head_branch(repo) == 'main' and not st)
    return L, gd, n


CONTROLS = dict(third=control_third, branch=control_branch, merge=control_merge, commit=control_commit, scan=control_scan,
                record=control_record, identity=control_identity, version=control_version, live=control_live)
ORDER = ('third', 'branch', 'merge', 'commit', 'scan', 'record', 'identity', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    live = 'live' in argv[1:]
    names = ['live'] if live else ([a for a in ORDER if a in argv[1:]] or list(ORDER))
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.4, (R367)(3): THE ROUTE FOR KERNEL WRITES%s (%s)' % (
               act, ', THE LIVE COMMIT IN EACH KERNEL' if live else '', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py; the planted cases in temporary repositories standing for a kernel, removed after; '
           'no kernel written by this tool', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before and after, the tools before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, gd, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, gd, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + gd, tn + c
        per.append('(%s) %d of %d' % (k, gd, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.35.4: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1354%s.txt' % (act, '_live' if live else '')
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
