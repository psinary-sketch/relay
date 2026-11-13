# -*- coding: utf-8 -*-
"""standing/v1340.py -- THE CONTROLS OF v1.34.0 ((R364)(3)(i)-(xxi), the amendment rows 1 to 3 of data/b754_amendments.json; b754 defects
(e), (f), (j), (k)), in v1330.py's form: each instance read through the route as it stood before the repair (tools/standing/ at BASE, b753's
closing relay head, read from its blobs) and through the repaired route on disk; AS WANTED where the old route fails the instance and the new
passes it; a GUARD where no old route can fail. THE COMPILE CONTROL RUNS FIRST. The free memory is read and printed before each control. A
replay that needs a repository runs on a scratch clone made under the temp directory by `git clone --local --no-checkout`, its HEAD and index
set by plumbing, removed by its own absolute path after the control; no write reaches the relay or PLACE-papers. Written at b754 by the Write
tool; no identifier of the author is read into any string here.

  python -X utf8 -u tools/standing/v1340.py control [vmove|version ...] [--bank]
"""
import importlib.util
import io
import os
import re
import shutil
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
BASE = '34332a00'   # ### b753's closing relay head (PRE_RELAY of b754): the routes before this repair
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def show(ref, rel, repo=RELAY):
    r = _git('show', '%s:%s' % (ref, rel), repo=repo)
    return r.stdout.replace('\r', '') if r.returncode == 0 else None


def old(rel, name):
    """tools/standing/<rel> as BASE left it, executed from its blob under another name (its own imports resolving on disk); None where BASE
    has no such file."""
    src = show(BASE, 'tools/standing/' + rel)
    if src is None:
        return None
    m = types.ModuleType(name)
    m.__file__ = os.path.join(S, rel)
    exec(compile(src, 'BASE:' + rel, 'exec'), m.__dict__)
    return m


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.33.0): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.34.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


import statedir as SD0          # noqa: E402
STATE = SD0.STATE   # ### the state folder on the data volume, outside every repository ((R364)(3)(xv), (8)), by the one resolver


class Clone(object):
    """a scratch clone of the relay in the state folder on the data volume (a `--local` clone hard-links its objects, which fails across
    volumes), no working tree; HEAD set detached and the index read from a tree by plumbing. Removed on exit, and on a failed clone, by the
    absolute path mkdtemp gave, checked to stand under STATE; no path is printed."""

    def __enter__(self):
        self.root = os.path.abspath(tempfile.mkdtemp(prefix='v1340_', dir=STATE))
        self.path = os.path.join(self.root, 'relay')
        r = subprocess.run(['git', 'clone', '--quiet', '--local', '--no-checkout', RELAY, self.path], capture_output=True, text=True)
        if r.returncode:
            self.__exit__()
            raise RuntimeError('the scratch clone failed, exit %d (its message held: it names a path)' % r.returncode)
        return self

    def stage(self, head, tree):
        """HEAD detached at `head`; the index read from `tree`: the staged set is then exactly the commit's change against its parent."""
        for a in (('update-ref', '--no-deref', 'HEAD', head), ('read-tree', tree)):
            r = _git(*a, repo=self.path)
            if r.returncode:
                raise RuntimeError('%s: %s' % (' '.join(a), (r.stderr or r.stdout).strip()[:300]))
        return [p for p in _git('diff', '--cached', '--name-only', repo=self.path).stdout.split(NL) if p]

    def __exit__(self, *exc):
        sc = os.path.abspath(STATE)
        if os.path.commonpath([sc, self.root]) == sc and os.path.basename(self.root).startswith('v1340_') and self.root != sc:
            remove_tree(self.root)
        return False


def remove_tree(path):
    """shutil.rmtree with git's read-only object files made writable and retried (an ignore_errors removal left seven clones standing at
    b754, data/b754_defects.txt (v)); a path still standing after it raises, naming its leaf only."""
    import stat

    def _again(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)

    shutil.rmtree(path, onerror=_again)
    if os.path.exists(path):
        raise RuntimeError('the scratch clone %s still stands after its removal' % os.path.basename(path))


def _full(c):
    return _git('rev-parse', c).stdout.strip()


class SparseClone(Clone):
    """a Clone with a working tree of the named patterns alone (non-cone sparse checkout), detached at `rev`."""

    def __init__(self, rev, patterns):
        self.rev, self.patterns = rev, list(patterns)

    def __enter__(self):
        Clone.__enter__(self)
        for a in (['sparse-checkout', 'set', '--no-cone'] + self.patterns, ['checkout', '-q', '--detach', _full(self.rev)]):
            r = _git(*a, repo=self.path)
            if r.returncode:
                self.__exit__()
                raise RuntimeError('the sparse clone`s %s failed, exit %d' % (a[0], r.returncode))
        return self


# ================================================================================ (vmove) (R364)(3)(vi)
def control_vmove():
    L, g, n = ['### (vmove) (R364)(3)(vi), (R345)(2)(iv); b753 events (7), (8), (9): THE VERSION MOVES WITH EVERY STANDING CHANGE -- the one-call '
               'tool refuses a relay commit staging a tools/standing/ path without VERSION staged and moved; `carry.py ruled` prints every list of '
               'writes in a ruling naming a standing path without VERSION'], 0, 0
    import commit as C
    import carry as CR
    base_src = show(BASE, 'tools/standing/commit.py') or ''
    old_has = 'def version_refusal' in base_src
    landed = _git('log', '-1', '--format=%h', BASE, '--', 'tools/standing/VERSION').stdout.strip()
    rows = []
    for c, want in (('0f31d31d', True), ('0db31ce3', True), (landed, False)):
        names = [p for p in _git('show', '--name-only', '--format=', c).stdout.split(NL) if p]
        hv, sv = show(c + '^', 'tools/standing/VERSION'), show(c, 'tools/standing/VERSION')
        rows.append((c, want, names, hv, sv, C.version_refusal(names, hv, sv)))
    for c, want, names, hv, sv, got in rows:
        std = [p for p in names if p.startswith('tools/standing/')]
        what = 'b753`s commit %s: %d path(s), %d under tools/standing/ (%s), VERSION %s -> %s' % (
            c, len(names), len(std), ', '.join(std[:3]), (hv or '').strip(), (sv or '').strip())
        n += 1
        if want:
            g += case(L, 'vmove', what + ', BY THE PURE READING', 'no version check at BASE' if not old_has else 'a check at BASE',
                      (got or 'ACCEPTED')[:150], not old_has, bool(got))
        else:
            g += guard(L, 'vmove', 'the commit that landed v1.33.0 (%s), VERSION moved beside its standing paths, accepted' % c,
                       got or 'ACCEPTED', got is None)
    with Clone() as K:
        for c, want, names, hv, sv, got in rows:
            staged = K.stage(_full(c + '^'), _full(c))
            r = C.staged_version_refusal(K.path)
            n += 1
            g += guard(L, 'vmove', 'the same commit %s replayed on a scratch clone (HEAD its parent, the index its tree; staged %d, equal to its '
                       'own list %s) through staged_version_refusal, the reading run() calls: %s' % (
                           c, len(staged), sorted(staged) == sorted(names), 'refused' if want else 'accepted'),
                       (r or 'ACCEPTED')[:150], (bool(r) == want) and sorted(staged) == sorted(names))
    run_src = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read()
    k = run_src.find('def run(')
    n += 1
    g += guard(L, 'vmove', 'run() calls staged_version_refusal over the staged names for the relay, before the scan',
               'in run(): %s' % ('staged_version_refusal(repo, names)' in run_src[k:k + 4000]), 'staged_version_refusal(repo, names)' in run_src[k:k + 4000])
    fer = io.open(os.path.join(D, 'b753_ferry.txt'), encoding='utf-8').read()
    wv = CR.writes_without_version(fer)
    hit = [w for w in wv if 'tools/standing/roster.py' in w[1]]
    old_cr = show(BASE, 'tools/standing/carry.py') or ''
    n += 1
    g += case(L, 'vmove', '(R363)(9)`s list of writes replayed from data/b753_ferry.txt: tools/standing/roster.py named without VERSION',
              'writes_without_version at BASE %s' % ('def writes_without_version' in old_cr), '%d list(s) printed, roster.py at %s' % (
                  len(wv), ', '.join(':%d' % w[0] for w in hit) or 'none'), 'def writes_without_version' not in old_cr, bool(hit))
    for ln_, ps_, ex_ in wv:
        L.append('        :%-4d %s' % (ln_, ', '.join(ps_)))
    named = [i for i, l in enumerate(fer.replace('\r', '').split(NL), 1) if CR.STANDING_PATH.search(l)]
    L.append('        THE MATCHER`S YIELD: lines naming a tools/standing/ path %d (%s) ; printed as lists of writes %d ; not printed %s' % (
        len(named), ', '.join(':%d' % i for i in named), len(wv), ', '.join(':%d' % i for i in named if i not in [w[0] for w in wv]) or 'none'))
    rsrc = io.open(os.path.join(S, 'carry.py'), encoding='utf-8').read()
    k = rsrc.find('def ruled(')
    n += 1
    g += guard(L, 'vmove', '`carry.py ruled` prints the lists before the citation check', 'writes_without_version(ruling_text) in ruled() %s' % (
        'writes_without_version(ruling_text)' in rsrc[k:k + 12000]), 'writes_without_version(ruling_text)' in rsrc[k:k + 12000])
    pl = CR.writes_without_version('(W) the planted list: tools/standing/VERSION, tools/standing/plant.py')
    n += 1
    g += guard(L, 'vmove', 'a planted list naming VERSION beside its standing path prints nothing', '%d printed' % len(pl), not pl)
    return L, g, n


# ================================================================================ (seat) (R364)(3)(i), the amendment row 3 (5)
def control_seat():
    L, g, n = ['### (seat) (R364)(3)(i), the amendment row 3 (5): THE SEAT`S FILE -- CLAUDE.md written by tools/standing/seatfile.py at the relay`s '
               'root and at the session`s project root, each kind of the hook`s table with its refused form and the form to send; the arm comparing '
               'the file`s kinds with the table and the two copies byte for byte'], 0, 0
    import re
    import seatfile as SF
    L.append('      tools/standing/seatfile.py at BASE: %s (a new tool; its cases have no failing side but their plants)' % (
        'ABSENT' if show(BASE, 'tools/standing/seatfile.py') is None else 'PRESENT'))
    ok, out = SF.control()
    for l in out:
        if re.match(r'  \(\d\) ', l):
            n += 1
            g += not l.rstrip().endswith('NOT AS WANTED')
        L.append('    ' + l)
    return L, g, n


# ================================================================================ (carry) (R364)(3)(ii)
def control_carry():
    L, g, n = ['### (carry) (R364)(3)(ii); b751 (b), b752 (b), b753 (b), (t`), (y`): THE ACT MODULE`S CARRIED ROWS -- every section that reads a '
               'ruling or an act`s banks carried as a stub refusing itself until written for the act; a cite inside a comment or a docstring left as '
               'it stands'], 0, 0
    import carry as NEW
    OLD = old('carry.py', 'carry_base')
    SUBS = (('b753', 'b754'), ('b752', 'b753'), ('R363', 'R364'), ('R362', 'R363'))   # ### tools/b754_carry.py :31
    rsubs = (('b753', 'b754'), ('b752', 'b753'))                                         # ### `carry.py ruled b754 b753`, as its main composes them
    old_mod, old_wl = show(BASE, 'tools/acts/b753.py'), show(BASE, 'tools/b753_worklist.py')
    ferry = io.open(os.path.join(D, 'b754_ferry.txt'), encoding='utf-8').read().replace('\r', '')
    ords = dict(x for x in (NEW.ordinal_of(ferry), NEW.ordinal_of(show(BASE, 'data/b753_ferry.txt') or '')) if x)
    L.append('      b753`s module (%d lines) and worklist (%d lines) from their blobs at %s ; the ruling data/b754_ferry.txt ; ordinals %s ; the ferry '
             'routed, no own rows (the opening run`s inputs, R6 held apart)' % (old_mod.count(NL) + 1, old_wl.count(NL) + 1, BASE, ords))
    om, ow = OLD.substitute(old_mod, SUBS), OLD.substitute(old_wl, SUBS)
    _Lo, ro = OLD.ruled(om, old_mod, ow, old_wl, ferry, rsubs, ferry_routed=True, ordinals=ords, own_rows='')
    mod, stubs = NEW.carry_module(old_mod, SUBS, 'b754')
    mod2, res = NEW.stub_check('b754', mod, stubs)
    wl, wnames = NEW.carry_worklist(old_wl, SUBS, 'b754')
    Ln, rn = NEW.ruled(mod2, old_mod, wl, old_wl, ferry, rsubs, ferry_routed=True, ordinals=ords, own_rows='')

    def kinds(r):
        return ', '.join('%s %d' % (k, sum(1 for x in r if x[0] == k)) for k in ('R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7') if any(x[0] == k for x in r)) or 'none'

    n += 1
    g += case(L, 'carry', 'b753`s module and worklist carried to b754, `carry.py ruled` on its opening run', 'REFUSED %d (%s)' % (len(ro), kinds(ro)),
              'REFUSED %d (%s) ; stubs in the module %d, in the worklist %d' % (len(rn), kinds(rn), len(stubs), len(wnames)), len(ro) > 0, len(rn) == 0)
    try:
        compile(wl, 'b754_worklist carried', 'exec')
        wok = True
    except SyntaxError as e:
        wok = 'FAILS: %s' % e
    # ### b747 to b753 each carried one record override, MARK 26666a71fb1e (record.tpl's _counter, the events bank read optional). v1.34.0's
    # ### record.tpl reads the three banks on the line above it ((3)(v), (3)(viii)) and keeps the marked line byte for byte as v1.33.0 left it, its
    # ### loop over nothing, so the older acts' renders find their mark (the standing dry, data/b754_standing_dry.txt, read NOT CLEAN on the
    # ### first form, which edited the marked line). The guard reads the mark found once in the template and every render of the carried module,
    # ### record among them, compiling as carried.
    import fold as F_
    mark = '26666a71fb1e'
    tl = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read().splitlines(keepends=True)
    try:
        found = F_.find_mark(tl, mark, 1, 'record')
    except F_.FoldRefused as e:
        found = 'REFUSED: %s' % e
    n += 1
    g += guard(L, 'carry', 'the carried worklist and every render of the carried module compile as carried, record among them; b753`s override '
               'MARK %s found once in v1.34.0`s record.tpl (carried in the module %d time(s))' % (mark, mod2.count(mark)),
               'worklist %s ; %s ; the mark at %s' % (wok, ', '.join('%s %s' % kv for kv in sorted(res.items())), found),
               wok is True and all(v == 'COMPILES' for v in res.values()) and isinstance(found, tuple))
    NINE = (511, 781, 786, 1835, 1840, 1891, 1912, 2024, 2107)   # ### b753 (y'): the nine comment cites of tools/acts/b753.py
    ol = old_mod.split(NL)
    moved_old = [k for k in NINE if om.split(NL)[k - 1] != ol[k - 1]]
    nl_ = set(mod2.split(NL))
    unmoved = [k for k in NINE if ol[k - 1] in nl_]
    n += 1
    g += case(L, 'carry', 'the nine comment cites of (y`) (tools/acts/b753.py %s)' % ', '.join(':%d' % k for k in NINE),
              'moved %d (%s)' % (len(moved_old), ', '.join(':%d' % k for k in moved_old)), 'unmoved %d of 9' % len(unmoved), len(moved_old) > 0, len(unmoved) == 9)
    n += 1
    g += guard(L, 'carry', '`carry.py ruled` prints the carried stubs', 'THE CARRIED STUBS section %s' % any(l.startswith('## THE CARRIED STUBS') for l in Ln),
               any(l.startswith('## THE CARRIED STUBS') for l in Ln))
    return L, g, n


# ================================================================================ (closescan) (R364)(3)(iii)
def _replay_close(M, label):
    """b753's closing step-row commit replayed through module M's run() on a sparse clone at b753's closing commit 76c2c2ab, the step-row
    commit 34332a00's two files staged; M's RELAY and T pointed at the clone for the call and restored. (state of b753's per-commit bank after
    the commit, whether b754's stands, the run's printed scan lines)."""
    import contextlib
    import subjects as SJ
    import json as _json
    with SparseClone('76c2c2ab', ['/tools/', '/data/b753_*', '/data/act_current.json']) as K:   # ### b753's worklist reads act_current at import
        r = _git('checkout', '-q', _full('34332a00'), '--', 'data/b753_steps.json', 'data/b753_address_scan_commits.txt', repo=K.path)
        if r.returncode:
            raise RuntimeError('staging 34332a00`s two files failed, exit %d' % r.returncode)
        head = _json.loads(show('76c2c2ab', 'data/b753_steps.json') or '{}')
        staged = _json.loads(show('34332a00', 'data/b753_steps.json') or '{}')
        words = SJ.step_rows_words(SJ.step_rows_added(head, staged))
        keep = (M.RELAY, M.T)
        buf = io.StringIO()
        try:
            M.RELAY, M.T = K.path, os.path.join(K.path, 'tools')
            with contextlib.redirect_stdout(buf):
                d = M.run(K.path, 'closing', words, act='b753', row_writer=lambda *a: (0, 'the control writes no row'))
        finally:
            M.RELAY, M.T = keep
        st = _git('status', '--porcelain', '--', 'data/b753_address_scan_commits.txt', repo=K.path).stdout.strip()
        nxt = os.path.join(K.path, 'data', 'b754_address_scan_commits.txt')
        nxt_n = io.open(nxt, encoding='utf-8').read().count(NL) if os.path.exists(nxt) else None
        subj = d.get('subject')
        shown = [l.strip() for l in buf.getvalue().split(NL) if 'appended to' in l]
    return dict(label=label, words=words, subject=subj, b753_status=st or 'clean', b754_lines=nxt_n, shown=shown)


def control_closescan():
    L, g, n = ['### (closescan) (R364)(3)(iii); the closes of b749 to b753, five running: THE SCAN OF THE CLOSING STEP-ROW COMMIT -- taken over its '
               'staged set before the commit as every commit`s is, its rows written to the next act`s per-commit bank as that bank`s opening rows; '
               'nothing appended to a pushed bank'], 0, 0
    import commit as NEW
    OLD = old('commit.py', 'commit_base')
    L.append('      b753`s close replayed on a sparse clone in the state folder (tools/, data/b753_* and data/act_current.json checked out at 76c2c2ab, the closing commit; '
             '34332a00`s data/b753_steps.json and data/b753_address_scan_commits.txt staged), the step-row commit made through run() in the clone')
    o = _replay_close(OLD, 'v1.33.0')
    nw = _replay_close(NEW, 'v1.34.0')
    for x in (o, nw):
        L.append('      %s: subject %r ; data/b753_address_scan_commits.txt after the commit: %s ; data/b754_address_scan_commits.txt: %s ; %s' % (
            x['label'], (x['subject'] or '')[:70], x['b753_status'], 'ABSENT' if x['b754_lines'] is None else '%d lines' % x['b754_lines'],
            ' | '.join(x['shown']) or 'no append printed'))
    n += 1
    g += case(L, 'closescan', 'the tree after the step-row commit, clean of data/b753_address_scan_commits.txt', 'b753`s bank %s' % o['b753_status'],
              'b753`s bank %s, b754`s bank %s' % (nw['b753_status'], 'ABSENT' if nw['b754_lines'] is None else 'written, %d lines' % nw['b754_lines']),
              o['b753_status'] != 'clean', nw['b753_status'] == 'clean' and (nw['b754_lines'] or 0) > 0)
    n += 1
    g += guard(L, 'closescan', 'the replayed commit`s subject is the one b753`s close committed (34332a00)', '%r' % (nw['subject'] or '')[:80],
               (nw['subject'] or '') == _git('log', '-1', '--format=%s', '34332a00').stdout.strip())
    return L, g, n


# ================================================================================ (lean) (R364)(3)(iv)
def control_lean():
    L, g, n = ['### (lean) (R364)(3)(iv); b751 (d), b752 (d), b753 (e): THE CITATION CHECK`S LEAN-PATH READER READS A CLAUSE OF SEVERAL PATHS -- '
               'paired in order where it carries as many declared names as paths, otherwise every name against every path, a halt where no path '
               'holds a name'], 0, 0
    import cites as NEW
    import b753_worklist as W3
    OLD = old('cites.py', 'cites_base')
    trees = tuple(getattr(W3, 'LEAN_TREES', ()))
    fer = io.open(os.path.join(D, 'b753_ferry.txt'), encoding='utf-8').read().replace('\r', '')
    hits = [l for l in fer.split(NL) if 'EpsteinZQ.lean' in l and 'LogDeriv.lean' in l]
    k = hits[0].find('EpsteinZQ.lean')
    clause = hits[0][max(0, k - 200):k + 60]
    L.append('      (R363)`s clause, from data/b753_ferry.txt (%d line(s) carry both paths), b753`s LEAN_TREES %s' % (len(hits), ', '.join('%s@%s' % (
        os.path.basename(r), v) for r, v in trees)))

    def verdict(rows):
        return 'HALT' if not all(r[3] for r in rows) else 'OK', ' ; '.join('%s -> %s' % (r[1][:70], r[3]) for r in rows if ' ' in r[1]) or 'no name rows'   # ### a path row is the path alone

    o, nw = verdict(OLD.lean_rows(clause, trees)), verdict(NEW.lean_rows(clause, trees))
    n += 1
    g += case(L, 'lean', 'the rQ and cQ of the instance (Schema/EpsteinZQ.lean :59; Schema/ZQ/LogDeriv.lean :63-:65)', '%s (%s)' % o, '%s (%s)' % nw,
              o[0] == 'HALT', nw[0] == 'OK')
    for what, src, dst in (('a third name, h2_sign, no path of the clause declaring it: every name read against every path', 'the rQ and cQ of',
                            'the rQ, h2_sign and cQ of'),
                           ('h2_sign in cQ`s place, paired in order with LogDeriv.lean, which does not declare it', 'the rQ and cQ of', 'the rQ and h2_sign of')):
        pl = clause.replace(src, dst)
        v = verdict(NEW.lean_rows(pl, trees))
        n += 1
        g += guard(L, 'lean', 'PLANTED: %s (the clause changed %s)' % (what, pl != clause), '%s (%s)' % v, pl != clause and v[0] == 'HALT')
    return L, g, n


# ================================================================================ (postseal) (R364)(3)(v)
def control_postseal():
    L, g, n = ['### (postseal) (R364)(3)(v); b752`s corrigendum :68, b752`s refusals :26, :27, b753 events (14): THE POST-SEAL EVENTS BANK -- on '
               'the by-design list of tools/standing/act.py, read by the counter and the trail beside the events bank, N4`s clause naming it'], 0, 0
    import counter as NEWC
    import act as NEWA
    import hook as H
    OLDC, OLDA = old('counter.py', 'counter_base'), old('act.py', 'act_base')
    oc, nc = OLDC.compose('b753', rev=BASE), NEWC.compose('b753', rev=BASE)
    n += 1
    g += case(L, 'postseal', 'b753`s banks at %s read by the counter: events (1)-(9) in data/b753_events.txt, (10)-(14) in '
              'data/b753_events_postseal.txt' % BASE, 'events %d, last %s ; %s' % (oc['events'], oc['last'], OLDC.line(oc)),
              'events %d, last %s ; %s' % (nc['events'], nc['last'], NEWC.line(nc)), oc['events'] == 9, nc['events'] == 14)
    ps = 'data/b753_events_postseal.txt'
    op, np_ = OLDA.post_lock_appended('b753'), NEWA.post_lock_appended('b753')
    n += 1
    g += case(L, 'postseal', 'N4`s lock guard reads the post-seal bank as written by design (post_lock_appended)', '%s on the list %s' % (ps, ps in op),
              '%s on the list %s' % (ps, ps in np_), ps not in op, ps in np_)
    n += 1
    g += guard(L, 'postseal', 'N4 reads a hand edit of the events bank after the lock as an edit: data/b753_events.txt off the design list',
               'on the list %s' % ('data/b753_events.txt' in np_), 'data/b753_events.txt' not in np_)
    n += 1
    g += guard(L, 'postseal', 'the hook`s design list (its row (65), the fallback carrying the list whole) names the post-seal bank',
               'hook.by_design names it %s' % (ps in H.by_design('b753')), ps in H.by_design('b753'))
    tp = dict((t, io.open(os.path.join(S, 'fold', t + '.tpl'), encoding='utf-8').read()) for t in ('closing', 'record'))
    n += 1
    g += guard(L, 'postseal', 'the trail`s events section (closing.tpl) and the record`s counter (record.tpl) read the post-seal bank',
               'events_postseal in closing.tpl %d time(s), in record.tpl %d' % (tp['closing'].count('events_postseal'), tp['record'].count('events_postseal')),
               tp['closing'].count('events_postseal') > 0 and tp['record'].count('events_postseal') > 0)
    return L, g, n


# ================================================================================ (letters) (R364)(3)(viii)
def planted_letters(k=80):
    """k planted defect rows lettered (a) to (z), (a') to (z'), (a'') and on, each in the bank's form."""
    out = []
    for p in range(k // 26 + 1):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if len(out) < k:
                out.append("    (%s%s) THE SEAT'S [CLOSE ; NEW]: planted row %d of %d." % (c, "'" * p, len(out) + 1, k))
    return out


def control_letters():
    L, g, n = ['### (letters) (R364)(3)(viii): THE LETTERS AFTER (z`) -- the defects bank`s rows read (a``), (b``) and on, the readers taking any '
               'number of primes'], 0, 0
    import counter as NEWC
    import defectrow as NEWD
    import close as NEWX
    import nextact as NEWN
    rows = planted_letters(80)
    text = NL.join(rows)
    L.append('      the planted bank: %d rows, %s ... %s ; the 53rd %s' % (len(rows), rows[0][4:8], rows[-1][4:11], rows[52][4:10]))
    readers = (('counter.items', 'counter.py', lambda M: len(M.items(text, ''))),
               ('defectrow.tag_of', 'defectrow.py', lambda M: sum(1 for r in rows if M.tag_of(r.strip()))),
               ('close.DEFECT_ROW', 'close.py', lambda M: sum(1 for r in rows if M.DEFECT_ROW.match(r))),
               ('nextact.ITEM', 'nextact.py', lambda M: sum(1 for r in rows if M.ITEM.match(r))))
    for (nm, rel, f), NEWM in zip(readers, (NEWC, NEWD, NEWX, NEWN)):
        o, nw = f(old(rel, rel[:-3] + '_base')), f(NEWM)
        n += 1
        g += case(L, 'letters', 'the planted bank of %d rows read by %s' % (len(rows), nm), '%d of %d read' % (o, len(rows)), '%d of %d read' % (nw, len(rows)),
                  o < len(rows), nw == len(rows))
    ids = NEWC.tally(NEWC.items(text, ''))['ids']
    n += 1
    g += guard(L, 'letters', 'the counter`s ids in bank order, the 53rd (a``) and the last (b```)', '%s ; %s' % (ids[52], ids[-1]),
               ids[52] == "defect (a'')" and ids[-1] == "defect (b''')")
    return L, g, n


# ================================================================================ (subject) (R364)(3)(vii), the amendment row 3 (2)
def control_subject():
    L, g, n = ['### (subject) (R364)(3)(vii), the amendment row 3 (2); (R364)(2)(ii): THE SUBJECT READ`S CORPUS -- beside the `## ` headings and '
               'the entry heads, the reference layer`s `### ` headings with the bold line beneath each, the standing clauses, the rules banks, the lock '
               'gate`s rule lines and the head lines of the banks of four kinds; every hit printed by its place, no line quoted'], 0, 0
    import subject as NEW
    OLD = old('subject.py', 'subject_base')
    items, fig, ri = NEW.corpus()
    whole = items + ri
    oh = OLD.heads()
    L.append('      the corpus: %s' % ' ; '.join('%s %d' % (k.replace('_', ' '), v) for k, v in sorted(fig.items())))
    f753 = io.open(os.path.join(D, 'b753_ferry.txt'), encoding='utf-8').read()
    f754 = io.open(os.path.join(D, 'b754_ferry.txt'), encoding='utf-8').read()
    t363 = NEW.ruling(f753, 'RULING (R363) BEGIN', 'RULING (R363) END')
    t364 = NEW.ruling(f754, 'RULING (R364) BEGIN', 'RULING (R364) END')

    def st(r, w):
        return ('HIT' if w in r['hit'] else 'NO HIT') if 'hit' in r else ('HIT' if w in r['uncited'] else 'NOT AMONG THE UNCITED')

    sp = ('head:standing version=version',)
    W = (('relay:data/b748_rules.txt', 9), ('relay:tools/b378_lockgate.py', 237))
    o, nw = OLD.run(sp, t363, oh), NEW.run(sp, t363, whole, quote=False)
    n += 1
    g += case(L, 'subject', '(R363) replayed with its (9)`s noun, the standing version: (R345)(2)(iv) where the relay holds it, data/b748_rules.txt :9 and '
              'tools/b378_lockgate.py :237, uncited hits', '%s ; hits %d' % ([st(o, w) for w in W], o['hits']), '%s ; hits %d' % ([st(nw, w) for w in W], nw['hits']),
              not any(w in o['uncited'] for w in W), all(w in nw['uncited'] for w in W))
    sp = ('head:minimal negative=minimal', 'head:class number 3=class')
    o, nw = OLD.run(sp, t363, oh), NEW.run(sp, t363, whole, quote=False)
    ob = sorted(x for d, x in o['uncited'] if d == 'relay:data/b721_derivation.txt')
    nb = sorted(x for d, x in nw['hit'] if d == 'relay:data/b721_derivation.txt')
    n += 1
    g += case(L, 'subject', 'the nouns minimal negative and class number 3: data/b721_derivation.txt a hit ((R364)(2)(ii))', 'lines %s' % ob,
              'lines %s, cited by (R363) as a file %s' % (nb, bool(nb) and all(('relay:data/b721_derivation.txt', x) in nw['cited_hits'] for x in nb)), not ob, bool(nb))
    for what, sp, W in (('two-leg: the anchors at :900 and :978 a hit by their bold lines :901 and :979', ('head:two-leg',), (('FINDINGS', 901), ('FINDINGS', 979))),
                        ('simplicity: the anchor at :904 a hit', ('word:simplicity=simplicit',), (('FINDINGS', 904),))):
        o, nw = OLD.run(sp, t364, oh), NEW.run(sp, t364, whole, quote=False)
        oset = set((d, x) for d, x, _l in oh)
        n += 1
        g += case(L, 'subject', 'the amendment row 3 (2), ' + what, 'the lines in the corpus read %s ; hits %d' % ([w in oset for w in W], o['hits']),
                  '%s ; hits %d' % ([NEW._state(nw, w) for w in W], nw['hits']), not any(w in oset for w in W), all(w in nw['hit'] for w in W))
    ly = [x for x in items if x[0] == 'FINDINGS' and NEW.LAYER[0] <= x[1] <= NEW.LAYER[1]]
    p1, p2 = NEW.run((NEW.PLANTED,), t364, ly, quote=False), NEW.run((NEW.PLANTED,), t364, whole, quote=False)
    n += 1
    g += guard(L, 'subject', 'the amendment row 3 (2): a planted noun standing in no anchor (%s) no hit, in the layer`s %d items or the corpus`s %d' % (
        NEW.PLANTED, len(ly), len(whole)), 'hits %d and %d' % (p1['hits'], p2['hits']), p1['hits'] == 0 and p2['hits'] == 0)
    n += 1
    g += guard(L, 'subject', 'the layer`s `### ` headings in FINDINGS :762-:1096 as the amendment row 3 (2) counts them, 76, each with its bold line',
               'headings %d ; bold lines %d' % (fig['layer_headings'], fig['layer_bold']), fig['layer_headings'] == 76 and fig['layer_bold'] == 76)
    t362 = NEW.ruling(io.open(os.path.join(D, 'b752_ferry.txt'), encoding='utf-8').read(), 'RULING (R362) BEGIN', 'RULING (R362) END')
    r = NEW.run(NEW.R362_SPECS, t362, whole, quote=False)
    got = [x for x in NEW.FLOOR if x in r['uncited']]
    n += 1
    g += guard(L, 'subject', 'the floor of (R362) over the corpus whole: FINDINGS :10858, :11072, :11178, :11359, INSTRUMENTS :750, :758 among the uncited',
               '%d of %d ; hits %d' % (len(got), len(NEW.FLOOR), r['hits']), len(got) == len(NEW.FLOOR))
    q, nq = NEW.run(('head:two-leg',), '', whole, quote=True), NEW.run(('head:two-leg',), '', whole, quote=False)
    frag = [l[:40] for d, x, l in whole if (d, x) in q['hit'] and len(l.strip()) >= 20]
    leak = sum(1 for f in frag if any(f in y for y in nq['lines']))
    shown = sum(1 for f in frag if any(f in y for y in q['lines']))
    n += 1
    g += guard(L, 'subject', 'the print by place: quote off, no hit`s words in the print; quote on, every hit`s (the guard`s own control)',
               'off %d of %d ; on %d of %d' % (leak, len(frag), shown, len(frag)), bool(frag) and leak == 0 and shown == len(frag))
    return L, g, n


# ================================================================================ (n3) (R364)(3)(ix)
def _const(src, name):
    """an act module's string constant `name = (...)` read by its literal (the module holds section marks and is no Python file whole)."""
    import ast
    L_ = src.split(NL)
    i0 = [i for i, l in enumerate(L_) if l.startswith(name + ' = ')][0]
    piece = []
    for l in L_[i0:i0 + 12]:
        piece.append(l)
        if l.rstrip().endswith("')") or l.rstrip().endswith('")'):
            break
    return ast.literal_eval(NL.join(piece).split('=', 1)[1].strip()), i0 + 1


def control_n3():
    L, g, n = ['### (n3) (R364)(3)(ix); b753`s N3 at the close: THE ENTRY`S LAST LINE READ AGAINST THE ACT MODULE`S CONSTANT, BOTH THROUGH THE RECORD '
               'TOOL`S OWN CONVERTER (standing.act.entry_ends_with, conv passed by the record module; the composer`s text converted as it would land)'], 0, 0
    import json
    import b652_record as R
    import act as NEWA
    const, at = _const(show(BASE, 'tools/acts/b753.py'), 'INTEGRATION_LINE')
    fj = json.loads(show(BASE, 'data/b753_findings.json'))
    text = NEWA.landed_entry('b753', fj)
    ls = [l for l in text.split(NL) if l.strip()]
    L.append('      b753`s constant: tools/acts/b753.py :%d at %s, %d characters, %d backtick(s) ; the landed entry: FINDINGS :%s, %d lines, its last line %d '
             'backtick(s), %d ’' % (at, BASE, len(const), const.count('`'), fj['line'], len(ls), ls[-1].count('`'), ls[-1].count('’')))
    o_ = ls[-1].strip() == const
    nw_ = NEWA.entry_ends_with(text, const, R.conv)
    n += 1
    g += case(L, 'n3', 'b753`s landed entry`s last line against b753`s constant (the clause that refuted N3 at the close)', 'raw comparison %s' % o_,
              'entry_ends_with %s' % nw_, not o_, nw_)
    sc = json.loads(show(BASE, 'data/b753_scores_close.json'))['N3']
    cl = [c for c in str(sc[1]).split('; ') if ': ' in c]

    def holds(c):
        v = c.rsplit(': ', 1)[1].replace(' [record]', '').strip()
        toks = re.findall(r'\b(True|False|NONE)\b', v)
        return bool(toks) and all(t_ != 'False' for t_ in toks)

    ki = [i for i, c in enumerate(cl) if 'the INTEGRATION line' in c]
    pp = 'D:/MY-DOwnloads/PLACE-papers'
    rg = (_git('show', 'HEAD:REGISTRY.md', repo=pp).stdout or '').split(NL)
    sm = _git('show', 'HEAD:SPIRAL_MAP.md', repo=pp).stdout or ''
    rows_ = any(l.startswith('| 1.5c-21 |') for l in rg) and '| **The Epstein instance** (seated 2026-11-09, b750) |' in sm and 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md' in sm
    others = [holds(c) for i, c in enumerate(cl) if i not in ki]
    integ_new = nw_ and rows_
    new_v = 'HELD' if all(others) and len(ki) == 1 and integ_new else 'REFUTED'
    n += 1
    g += case(L, 'n3', 'b753`s N3 at the close replayed from data/b753_scores_close.json at %s: its %d clauses, the INTEGRATION clause read again by the '
              'repaired check, REGISTRY 1.5c-21 and SPIRAL_MAP`s Epstein row read at PLACE-papers HEAD' % (BASE, len(cl)),
              '%s as banked ; the INTEGRATION clause %s ; the other %d holding %d' % (sc[0], [holds(cl[i]) for i in ki], len(others), sum(others)),
              '%s ; the INTEGRATION clause %s (the rows %s)' % (new_v, integ_new, rows_), sc[0] == 'REFUTED', new_v == 'HELD')
    raw_text = 'a line of the entry' + NL + const + NL
    n += 1
    g += guard(L, 'n3', 'one function for both: the composer`s raw text ending on the constant, its backtick unturned, read equal; a planted last line read not equal',
               'raw text %s ; planted %s' % (NEWA.entry_ends_with(raw_text, const, R.conv), NEWA.entry_ends_with(text + 'a planted line' + NL, const, R.conv)),
               NEWA.entry_ends_with(raw_text, const, R.conv) and not NEWA.entry_ends_with(text + 'a planted line' + NL, const, R.conv))
    tpl = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    act_src = io.open(os.path.join(T, 'acts', '%s.py' % A.current().get('act')), encoding='utf-8').read()
    n += 1
    g += guard(L, 'n3', 'the record template converts the composer`s text (`conv(_finding_text()[1])`) and the act module`s N3 reads entry_ends_with, no raw '
               '`lines_[-1].strip() == INTEGRATION_LINE`', 'template %s ; module entry_ends_with %s, raw %s' % (
                   'conv(_finding_text()[1])' in tpl, 'entry_ends_with(text, INTEGRATION_LINE, conv)' in act_src, "lines_[-1].strip() == INTEGRATION_LINE" in act_src),
               'conv(_finding_text()[1])' in tpl and 'entry_ends_with(text, INTEGRATION_LINE, conv)' in act_src and "lines_[-1].strip() == INTEGRATION_LINE" not in act_src)
    return L, g, n


# ================================================================================ (rootparts) (R364)(3)(x)
def control_rootparts():
    L, g, n = ['### (rootparts) (R364)(3)(x): THE ROOT ROUTE`S LIMIT -- its expected seconds printed from the previous act`s run; at four fifths of '
               'the host`s limit or unread, the route in parts, each a foreground call under the limit, the root computed last from the parts` bank'], 0, 0
    import json
    import act_root as AR
    import rootparts as RP
    at_base = show(BASE, 'tools/standing/rootparts.py') is not None
    sec, how = RP.expected('b753', D)
    n += 1
    g += case(L, 'rootparts', 'b753`s root route (called 03:27:05Z, moved to the background by the host at its 600 s limit) read as the expectation',
              'tools/standing/rootparts.py at %s: %s ; the route whole, no expectation printed' % (BASE, 'present' if at_base else 'ABSENT'),
              'expected %s s (%s) -> %s' % ('%.0f' % sec if sec is not None else 'UNREAD', how[:150], RP.decide(sec)), not at_base, RP.decide(sec) == 'parts')
    J = json.loads(show(BASE, 'data/b753_act_root.json'))
    RB = json.loads(show(BASE, 'data/b753_root_banks.json'))
    commit = J['commit']['relay']
    banks = sorted(J['reads']['banks'])
    part2 = dict(ready=True, head=RB['head'], remote=RB['remote'], banks=RP.blob_shas(RELAY, commit, banks))
    files_at_compute = dict(J['reads']['banks'])
    why = RP.confirm(part2, banks, commit, commit, [], files_at_compute)
    items = [it for it in J['items'] if not it.startswith('data/')] + ['%s %s' % (b, part2['banks'][b]) for b in banks]
    root = AR.root_of(items, J['previous'])
    L.append('      b753`s banks %d at its recorded commit %s ; the first reading`s HEAD %s, the remote %s ; repositories and tags %d from its items' % (
        len(banks), commit[:12], RB['head'][:12], RB['remote'][:12], len([i for i in J['items'] if not i.startswith('data/')])))
    n += 1
    g += case(L, 'rootparts', 'b753`s root replayed in parts: the second reading`s part from the blobs at its recorded commit, confirmed against the files` '
              'sha256s at its compute, the root computed from the parts` bank', 'no parts route at %s' % BASE,
              'confirm %s ; root %s (banked %s)' % (why or 'HOLDS', root[:16], J['root'][:16]), not at_base, not why and root == J['root'] and RB['head'] == commit)
    b0 = banks[0]
    planted = (('one named bank`s file not its blob', dict(files_at_compute, **{b0: '0' * 64}), commit, commit, banks, part2),
               ('HEAD moved after the second reading', files_at_compute, 'f' * 40, 'f' * 40, banks, part2),
               ('the remote main not HEAD', files_at_compute, commit, '0' * 40, banks, part2),
               ('a bank named now that the reading did not name', files_at_compute, commit, commit, banks + ['data/b753_planted.txt'], part2),
               ('the second reading not banked', files_at_compute, commit, commit, banks, None))
    for what, fn, head, rem, bk, p2 in planted:
        w = RP.confirm(p2, bk, head, rem, [], fn)
        n += 1
        g += guard(L, 'rootparts', 'PLANTED: %s -- the compute refuses' % what, '%s' % (w[:1] or 'HOLDS'), bool(w))
    n += 1
    g += guard(L, 'rootparts', 'the decision: unread -> parts ; 100 s -> whole ; 480 s (the margin) -> parts',
               '%s ; %s ; %s' % (RP.decide(None), RP.decide(100), RP.decide(480)), (RP.decide(None), RP.decide(100), RP.decide(480)) == ('parts', 'whole', 'parts'))
    import fold as F
    act = A.current().get('act')
    txt = F.render(act, 'record')
    b707 = show(BASE, 'tools/b707_record.py') or ''
    m = re.search(r"EXCLUDE_KINDS = \((r'[^\n]*\n\s*r'[^\n]*\n\s*r'[^\n]*)\)", b707)
    kinds = ''.join(re.findall(r"r'([^']*)'", m.group(1))) if m else ''
    excl = bool(kinds) and re.match(r'^%s_((%s)\.?(txt|json|md|jsonl|))$' % (act, kinds), RP.PARTS % act) is not None
    n += 1
    g += guard(L, 'rootparts', 'the rendered record module routes `rootpart` and binds root through standing.rootparts; the parts` bank (%s) a kind the root '
               'excludes (b707`s EXCLUDE_KINDS, carried by every record module after it)' % (RP.PARTS % act),
               'route %s ; binding %s ; excluded %s' % ('rootpart=rootpart' in txt, "'standing.rootparts'" in txt, excl),
               'rootpart=rootpart' in txt and "'standing.rootparts'" in txt and excl)
    return L, g, n


# ================================================================================ (table) (R364)(3)(xi)
def _fn_src(text, name):
    """a top-level function's source cut from a template's text: its def line to the next line at column 0 that is not blank."""
    L_ = text.split(NL)
    i = [k for k, l in enumerate(L_) if l.startswith('def %s(' % name)][0]
    j = i + 1
    while j < len(L_) and (not L_[j].strip() or L_[j].startswith((' ', '\t'))):
        j += 1
    return NL.join(L_[i:j])


def control_table():
    L, g, n = ['### (table) (R364)(3)(xi); b752 (d), b753 (d): THE TERMINAL TABLE -- the suite`s act part regenerates to the act`s scratch folder in '
               'the state folder (tools/standing/tablescratch.py, the generator`s build and emit imported) and compares; the tracked table moves by the '
               'record`s table_final in a commit of the close'], 0, 0
    import json
    act = A.current().get('act')
    FIVE = ['data/' + f for f in ('terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table.md', 'terminal_table_diff.json')]
    old_src = _fn_src(show(BASE, 'tools/standing/fold/checks.tpl'), 'regenerate').replace('⟪ACT⟫', act)
    new_src = _fn_src(io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read(), 'regenerate').replace('⟪ACT⟫', act)
    pats = ['/tools/', '/data/elab_types.txt', '/data/table_retire.json', '/data/table_repoint.json', '/data/b636_elab_sec.txt', '/data/b544_ei.json',
            '/data/terminal_table*']

    def run(src, root):
        ns = dict(subprocess=subprocess, sys=sys, os=os, json=json, T=os.path.join(root, 'tools'),
                  rd=lambda nm: (io.open(os.path.join(root, 'data', nm), encoding='utf-8').read() if os.path.isfile(os.path.join(root, 'data', nm)) else None))
        exec(compile(src, 'regenerate', 'exec'), ns)
        t0 = time.time()
        rc, diff = ns['regenerate']()
        st = [l for l in _git('status', '--porcelain', '--', *FIVE, repo=root).stdout.split(NL) if l.strip()]
        return rc, diff, st, time.time() - t0

    with SparseClone('HEAD', pats) as c:
        pre = [l for l in _git('status', '--porcelain', '--', *FIVE, repo=c.path).stdout.split(NL) if l.strip()]
        o = run(old_src, c.path)
        _git('checkout', '-q', '--', *FIVE, repo=c.path)   # ### the clone's own tree restored between the two runs; the clone is scratch
        mid = [l for l in _git('status', '--porcelain', '--', *FIVE, repo=c.path).stdout.split(NL) if l.strip()]
        os.makedirs(os.path.join(c.path, 'tools', 'standing'), exist_ok=True)
        # ### the two new tools the repaired step imports, untracked until v1.34.0's commit: tablescratch.py and, since (xv), its resolver statedir.py
        for f_ in ('tablescratch.py', 'statedir.py'):
            shutil.copyfile(os.path.join(S, f_), os.path.join(c.path, 'tools', 'standing', f_))
        nw = run(new_src, c.path)
    L.append('      a sparse scratch clone at relay HEAD (tools/ and the table`s data files), its tree clean before: %s ; restored between the runs: %s' % (
        not pre, not mid))
    n += 1
    g += case(L, 'table', 'the act part`s regeneration step (checks.tpl regenerate()) run on a clean tree: the tracked table files clean after it',
              'exit %s in %.0f s ; the tree after: %s' % (o[0], o[3], ' ; '.join(o[2]) or 'CLEAN'),
              'exit %s in %.0f s ; the tree after: %s ; the diff read from the scratch folder: added %d, gone %d, changed %d' % (
                  nw[0], nw[3], ' ; '.join(nw[2]) or 'CLEAN', len(nw[1].get('added') or []), len(nw[1].get('gone') or []), len(nw[1].get('changed') or [])),
              bool(o[2]) and not pre, not nw[2] and nw[0] == 0 and not mid)
    before = [l for l in _git('status', '--porcelain', '--', *FIVE).stdout.split(NL) if l.strip()]
    rl = run(new_src, RELAY)
    import tablescratch as TS
    cmp_ = TS.compare(act)
    n += 1
    g += guard(L, 'table', 'the repaired step on the relay itself: the five tracked files clean before and after; the scratch table compared with the '
               'tracked one', 'before %s ; after %s ; exit %s ; rows %d against %d, added %d, gone %d, moved %d' % (
                   ' ; '.join(before) or 'CLEAN', ' ; '.join(rl[2]) or 'CLEAN', rl[0], cmp_['scratch'], cmp_['tracked'], len(cmp_['added']),
                   len(cmp_['gone']), len(cmp_['moved'])), not before and not rl[2] and rl[0] == 0 and cmp_['scratch'] > 0)
    return L, g, n


# ================================================================================ (delread) (R364)(3)(xii)
def _b698_ns(names):
    """b698's record tool's module-level matchers (record.tpl binds them from R), read from its blob at BASE and executed alone, as v1300.py
    read b698's delete_shape: each from its `NAME = ` line to the next line at column 0."""
    src = show(BASE, 'tools/b698_record.py')
    ns = dict(re=re)
    for nm in names:
        m = re.search(r'(?ms)^%s = .*?(?=^\S)' % nm, src)
        exec(compile(m.group(0), 'BASE:tools/b698_record.py ' + nm, 'exec'), ns)   # noqa: S102
    return ns


def _cut(text, needle):
    """the template's one line opening with `needle` (stripped), or a refusal naming the needle and its yield."""
    hits = [l.strip() for l in text.split(NL) if l.startswith(needle)]
    if len(hits) != 1:
        raise RuntimeError('the needle %r took %d lines of the template, not one' % (needle, len(hits)))
    return hits[0]


BANK_NEEDLES = ("    mv = [r for r in sh_ if", "    shapes = [(r['n'],) + delete_shape", "    chained = [r['n'] for r in mv if",
                "    good = sum(1 for n, d, gl, vs in shapes")
COUNT = 'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d'


def control_delread():
    L, g, n = ['### (delread) (R364)(3)(xii), b753 (u`): THE DELETE READER READS A RUN OF THE ONE-CALL TOOL THROUGH tools/standing/gitwrite.py`s '
               'RUNS_COMMIT, imported and not copied; the record`s command bank counts those deletes (record.tpl`s mv); the kept clause read in the '
               'ferries` three wordings (tools/standing/allow.py); b753`s capture and its three branch arms replayed'], 0, 0
    import json
    import allow as STW
    import b703_checks as C3
    import b753_worklist as K
    import delread as DRN
    import fold as F
    DRO = old('delread.py', 'delread_v1330')
    rows = json.loads(show(BASE, 'data/b753_commands.json'))['rows']
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    named = sorted(b for _r, bs in K.DELETE for b in bs)
    tool = [r for r in sh_ if 'commit.py' in r['cmd'] and re.search(r'\sdelete\s', r['cmd'])]
    o_names = [x for r in sh_ for x in DRO.delete_shape(r['cmd'])[0]]
    n_names = [x for r in sh_ for x in DRN.delete_shape(r['cmd'])[0]]
    n_chain = [r['n'] for r in sh_ if DRN.delete_shape(r['cmd'])[0] and DRN.chained_after(r['cmd'])]
    ps = [r['n'] for r in tool if r['cmd'].lstrip().startswith('&')]
    n += 1
    g += case(L, 'delread', 'b753`s five step-zero deletes through the tool (capture rows %s, %d of them in PowerShell`s quoted-interpreter form), the '
              'ruled five %s' % (', '.join(str(r['n']) for r in tool), len(ps), ', '.join(named)),
              'v1.33.0`s delete_shape over the %d shell commands: %d names' % (len(sh_), len(o_names)),
              'v1.34.0`s: %d names (%s), chained after %s' % (len(n_names), ', '.join(n_names), n_chain or 'none'),
              len(tool) == 5 and not o_names, sorted(n_names) == named and not n_chain)
    src = io.open(os.path.join(S, 'delread.py'), encoding='utf-8').read()
    gw = io.open(os.path.join(S, 'gitwrite.py'), encoding='utf-8').read()
    one = 'RUNS_COMMIT = re.compile' not in src and DRN.GW.RUNS_COMMIT.pattern in gw and 'RUNS_COMMIT' in src
    n += 1
    g += guard(L, 'delread', 'one matcher: delread.py carries no RUNS_COMMIT of its own and asks the pattern gitwrite.py holds',
               'a RUNS_COMMIT assignment in delread.py %s ; the pattern it asks found in gitwrite.py %s' % (
                   'RUNS_COMMIT = re.compile' in src, DRN.GW.RUNS_COMMIT.pattern in gw), one)
    plants = [('& "X:/py/python.exe" -X utf8 -u tools/standing/commit.py relay delete push-x', ['push-x'], False),
              ('python -X utf8 -u tools/standing/commit.py pp delete push-y', ['push-y'], False),
              ('python -X utf8 -u tools/standing/commit.py relay delete push-v && git status', ['push-v'], True),
              ('python -c "print(\'python tools/standing/commit.py relay delete push-z\')"', [], False),
              ('echo python tools/standing/commit.py relay delete push-w', [], False),
              ('python -X utf8 -u tools/standing/commit.py relay add data/x.txt', [], False),
              ('git -C D:/relay branch -d "push-u"', ['push-u'], False)]
    got = [(DRN.delete_shape(c)[0], DRN.chained_after(c)) for c, _w, _ch in plants]
    n += 1
    g += guard(L, 'delread', 'seven planted forms: the quoted interpreter and the bare one each one branch; a delete chained before `git status` '
               'read chained; a program quoting the route, an echo of it and the tool`s add none; git`s own form as before',
               ' ; '.join('%s%s' % (d or '[]', ' CHAINED' if c else '') for d, c in got),
               all(d == w and c == ch for (d, c), (_c, w, ch) in zip(got, plants)))
    b698 = _b698_ns(('QUOTED', 'MOVE_OR_DELETE'))
    banked = [l for l in (show(BASE, 'data/b753_commands.txt') or '').split(NL) if 'BRANCH DELETES OF ONE BRANCH' in l]

    def count(tpl, reader):
        ns = dict(re=re, sh_=sh_, MOVE_OR_DELETE=b698['MOVE_OR_DELETE'], QUOTED=b698['QUOTED'], delete_shape=reader.delete_shape,
                  chained_after=reader.chained_after)
        exec(compile(NL.join(_cut(tpl, nd) for nd in BANK_NEEDLES), 'record.tpl lines', 'exec'), ns)   # noqa: S102
        return ns['good'], len(ns['shapes'])

    rt_old = show(BASE, 'tools/standing/fold/record.tpl')
    rt_new = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    co, cn = count(rt_old, DRO), count(rt_new, DRN)
    n += 1
    g += case(L, 'delread', 'the record`s command bank over b753`s capture: record.tpl`s own lines (mv, shapes, chained, good, each cut by its needle, '
              'one line each) with b698`s matchers read from its blob; the bank as committed reads %s' % (
                  re.search(r'AFTER \d+ OF \d+', banked[0]).group(0) if banked else 'NO COUNT LINE'),
              'the template at %s with v1.33.0`s reader: %d OF %d' % (BASE, co[0], co[1]),
              'the template now with v1.34.0`s reader: %d OF %d' % cn, co == (0, 0), cn == (5, 5))
    tpl = show(BASE, 'tools/standing/fold/checks.tpl')
    secs, ovs = F._parse('b753', show(BASE, 'tools/acts/b753.py'))
    ck = F.render('b753', 'checks', secs=secs, ovs=ovs, tpl=tpl)
    fns = NL.join(_fn_src(ck, f) for f in ('_first_ts', 'branches_banked_ok', 'deletes_one_ok', 'listings_before_ok'))
    firsts = [l.strip() for l in ck.split(NL) if re.match(r"^\s*S\['first_(delete|listing)_ts'\] = ", l)]
    cit = json.loads(show(BASE, 'data/b753_citation_check.json') or '{}')
    port_repo = [r_ for r_, b in K.KEPT_BRANCHES if b == K.PORT_BRANCH]
    tip = _git('rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH, repo=port_repo[0]).stdout.strip() if port_repo else ''
    cmdt0 = show(BASE, 'data/b753_commands.txt') or ''

    ALO = old('allow.py', 'allow_v1330')
    fer = [(a, show(BASE, 'data/%s_ferry.txt' % a) or '') for a in ('b744', 'b745', 'b746', 'b747', 'b748', 'b749', 'b750', 'b751', 'b752', 'b753')]
    fer.append(('b754', io.open(os.path.join(D, 'b754_ferry.txt'), encoding='utf-8').read()))
    ko = [a for a, t in fer if ALO.kept_clause(t)]
    kn = [a for a, t in fer if STW.kept_clause(t)]
    n += 1
    g += case(L, 'delread', 'the kept clause of G-DELETES-ONE-BRANCH read from eleven ferries, b744 to b754, in their three wordings (names and "the '
              'rest as banked" to b745; "as banked" b746 to b752; the previous closing`s carried list (f) from b753)',
              'v1.33.0`s allow.kept_clause reads %d: %s' % (len(ko), ', '.join(ko) or 'none'),
              'v1.34.0`s reads %d: %s' % (len(kn), ', '.join(kn)), ko == ['b744', 'b745'], len(kn) == len(fer))
    nil = ('port-b707 kept; the rest deleted.', 'the branches as banked.', 'kept as data/b753_closing.txt says.')
    n += 1
    g += guard(L, 'delread', 'three sentences carrying no kept clause read none, so the disjunct cannot pass on nothing',
               ' ; '.join('%r' % STW.kept_clause(s) for s in nil), not any(STW.kept_clause(s) for s in nil))

    def arms(reader, cmdt, stw):
        ns = dict(re=re, os=os, K=K, NAMED_PUSH=named, unwrap=C3.unwrap, files_of=C3.files_of, iso_epoch=C3.iso_epoch, ROOT=RELAY, STW=stw,
                  ACTN='b753', cmds=rows, REC=types.SimpleNamespace(delete_shape=reader.delete_shape, chained_after=reader.chained_after))
        exec(compile(fns, 'b753 checks, rendered at BASE', 'exec'), ns)   # noqa: S102
        ns['S'] = dict(stepz=show(BASE, 'data/b753_stepzero.txt') or '', ferry=show(BASE, 'data/b753_ferry.txt') or '', cmds=rows, REC=ns['REC'],
                       cmdt=cmdt, cit_at=C3.iso_epoch(cit.get('first_at') or cit.get('at') or ''), kept_tips={K.PORT_BRANCH: tip}, files={'stepzero': []})
        exec(compile(NL.join(firsts), 'b753 checks, the two first times', 'exec'), ns)   # noqa: S102
        Sx = ns['S']
        return [bool(ns[f](Sx)) for f in ('branches_banked_ok', 'listings_before_ok', 'deletes_one_ok')], Sx['first_delete_ts'], Sx['first_listing_ts']

    cmdt1 = re.sub(r'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER \d+ OF \d+', COUNT % cn, cmdt0)
    ao, ad_o, al_o = arms(DRO, cmdt0, ALO)
    an, ad_n, al_n = arms(DRN, cmdt1, STW)
    nm3 = ('G-BRANCHES-BANKED', 'G-LISTINGS-BEFORE-CLAUSES', 'G-DELETES-ONE-BRANCH')
    L.append('      b753`s checks rendered from the template at %s with b753`s module at %s (functions cut: 4, the two first-time lines: %d); the '
             'capture`s rows as banked (%d), not the suite`s live capture; %s kept at %s; the citation check`s first time %s' % (
                 BASE, BASE, len(firsts), len(rows), K.PORT_BRANCH, (tip or 'ABSENT')[:8], cit.get('first_at') or cit.get('at')))
    n += 1
    g += case(L, 'delread', 'b753`s three branch arms over its capture: %s' % ', '.join(nm3),
              'v1.33.0`s reader and kept clause and the bank as committed: %s ; the first delete %s, the first listing %s' % (
                  ', '.join('%s %s' % (a, 'PASS' if v else 'FAIL') for a, v in zip(nm3, ao)), ad_o, al_o),
              'v1.34.0`s reader and kept clause and the count line as the repaired route writes it: %s ; the first delete %s, the first listing %s' % (
                  ', '.join('%s %s' % (a, 'PASS' if v else 'FAIL') for a, v in zip(nm3, an)), ad_n, al_n),
              not any(ao), all(an))
    return L, g, n


# ================================================================================ (limit) (R364)(3)(xiii)
def control_limit():
    L, g, n = ['### (limit) (R364)(3)(xiii), b753 (s`): THE HOOK`S LIMIT MATCHER READS THE PROGRAM A COMMAND RUNS (tools/standing/limits.py '
               'runs_split and limit_of: a route`s pattern opening in the script or the .ps1 file), NOT A TOOL`S PATH INSIDE A COMMIT`S WORDS'], 0, 0
    import json
    import hook as H
    LMO = old('limits.py', 'limits_v1330')
    rows = json.loads(show(BASE, 'data/b753_commands.json'))['rows']
    hit = [r for r in rows if r['ts'].startswith('2026-11-11T20:35:41')]
    cmd = hit[0]['cmd'] if hit else ''
    bank = [k for k, l in enumerate((show(BASE, 'data/b753_hook_refusals.txt') or '').split(NL), 1) if l.startswith('2026-11-11T20:35:41Z | LIMIT')]
    of = LMO.fault(cmd, None)
    nj = H.judge('PowerShell', {'command': cmd})
    n += 1
    g += case(L, 'limit', 'b753`s commit of 20:35:41Z, sent with no timeout (capture row %s, %d characters, the tool`s path in its words; its refusal '
              'at data/b753_hook_refusals.txt :%s)' % (hit[0]['n'] if hit else 'ABSENT', len(cmd), ', :'.join(str(k) for k in bank) or 'ABSENT'),
              'v1.33.0`s limits.fault: %s' % ((of or 'None')[:110],),
              'v1.34.0, the hook`s own judge: %s' % ('ALLOWED' if nj is None else '%s %s' % (nj[0], nj[1][:90])), bool(of) and bool(bank), bool(hit) and nj is None)
    plants = [('Bash', 'python -X utf8 -u tools/research/reproduce.py', None, 'LIMIT'),
              ('PowerShell', '& "X:/py/python.exe" -X utf8 -u tools/research/reproduce.py --all', None, 'LIMIT'),
              ('Bash', 'python -X utf8 -u tools/research/reproduce.py', 600000, None),
              ('Bash', 'python -X utf8 -u tools/standing/fold.py checks --part act', None, 'LIMIT'),
              ('Bash', 'python -X utf8 -u tools/standing/v1340.py control delread', None, 'LIMIT'),
              ('Bash', 'python -X utf8 -u tools/standing/commit.py relay "component 1" "words naming tools/research/reproduce.py and tools/b753_prepaths.py"', None, None),
              ('Bash', 'git grep -n reproduce -- tools/research/reproduce.py', None, None)]
    got = []
    for tool, c, to, want in plants:
        inp = dict(command=c)
        if to is not None:
            inp['timeout'] = to
        v = H.judge(tool, inp)
        got.append((v[0] if v else None, want))
    n += 1
    g += guard(L, 'limit', 'seven planted calls through the hook`s judge: the reproduction tool run bare and by PowerShell`s quoted interpreter with no '
               'limit refused, with 600000 allowed; a suite part and a version`s controls still refused (their arguments read where the match '
               'opens in the program); a commit naming two routes in its words and a search naming the tool allowed',
               ' ; '.join('%s' % (k or 'ALLOWED') for k, _w in got), all(k == w for k, w in got))
    return L, g, n


# ================================================================================ (words) (R364)(3)(xiv)
B753_SESSION = '5a4228ab-091d-4515-b5ab-95a5e34e1e18'   # ### b753's seat session (tools/b753_worklist.py SESSION_ID)


def _row(path, line):
    import json
    with io.open(path, encoding='utf-8') as f:
        for i, raw in enumerate(f, 1):
            if i == line:
                return json.loads(raw)
    return None


def control_words():
    L, g, n = ['### (words) (R364)(3)(xiv), b753 (q`): THE ANSWERS ROUTE WRITES EACH PARAGRAPH OF A WORD ONCE -- tools/standing/authorwords.py`s '
               '_word_blocks cuts a word row by the word`s own lines, its blank lines inside it included'], 0, 0
    import authorwords as AWN
    AWO = old('authorwords.py', 'authorwords_v1330')
    import chain as CH
    path = CH.path_of(B753_SESSION)
    rows = [(k, _row(path, k), None, B753_SESSION) for k in (7049, 11488)]
    rows = [r for r in rows if r[1] is not None]
    words = AWN.author_words(rows, B753_SESSION, 'RULING (R363) BEGIN')
    nine = [w for w in words if str(w[0]) == '7049']
    body = nine[0][1].replace('\r', '').split(NL) if nine else []
    paras = [p for p in body if p.strip()]
    composed = ['b753 -- THE AUTHOR`S ANSWERS (a replay), 0 prompt(s) and %d word(s) of the author' % len(words), '']
    for ln, w, _ts in words:
        composed += [AWN.HEAD % ln] + w.replace('\r', '').split(NL) + ['']
    composed += ['### NOTE (transcript line 1): a planted closing row', '']

    def counts(mod):
        out, _r = mod.rekey(composed, words)
        return [out.count(p) for p in paras], len(out)

    co, cn = counts(AWO), counts(AWN)
    n += 1
    g += case(L, 'words', 'b753`s ninth word (its session`s row 7049, %d lines, %d paragraphs) and the word of row 11488 (one paragraph), composed as '
              'the route composes word rows and re-keyed; each paragraph`s count in the re-keyed bank' % (len(body), len(paras)),
              'v1.32.0`s rekey: %s, %d lines' % (co[0], co[1]), 'v1.34.0`s: %s, %d lines' % (cn[0], cn[1]),
              len(paras) == 4 and co[0][0] == 1 and all(c == 2 for c in co[0][1:]), len(paras) == 4 and all(c == 1 for c in cn[0]))
    one = [w for w in words if str(w[0]) == '11488']
    single = [l for l in (one[0][1].replace('\r', '').split(NL) if one else []) if l.strip()]
    out_n, _r = AWN.rekey(composed, words)
    n += 1
    g += guard(L, 'words', 'the one-paragraph word and the planted NOTE row each stand once after the repair, the head`s count 2',
               'the word`s lines %s ; the NOTE %d ; the head %r' % ([out_n.count(l) for l in single], out_n.count('### NOTE (transcript line 1): a planted closing row'),
                                                                   out_n[0][-30:]),
               bool(single) and all(out_n.count(l) == 1 for l in single) and out_n.count('### NOTE (transcript line 1): a planted closing row') == 1
               and out_n[0].endswith('and 2 word(s) of the author'))
    same = _git('diff', '--quiet', BASE, '--', 'data/b753_author_answers.txt').returncode == 0
    head = _git('diff', '--quiet', BASE, 'HEAD', '--', 'data/b753_author_answers.txt').returncode == 0
    n += 1
    g += guard(L, 'words', 'data/b753_author_answers.txt, a pushed bank, not rewritten: the tree`s file and HEAD`s blob each equal to its blob at %s (its '
               'lines :132-:204 standing, named in the corrigendum)' % BASE, 'the tree equal %s ; HEAD equal %s' % (same, head), same and head)
    return L, g, n


# ================================================================================ (state) (R364)(3)(xv)
SWITCH = '2026-11-13T17:28:43'   # ### the first record the hook wrote to the state folder's calls ledger, after hook.py read statedir.py


def control_state():
    L, g, n = ['### (state) (R364)(3)(xv): THE HOOK`S STATE OUT OF THE TEMP DIRECTORY -- tools/standing/statedir.py the one resolver of the state '
               'folder on the data volume; the hook`s calls ledger and git-write state and the one-call tool`s calls ledger read through it (a place '
               'printed by its kind; no path under the temp directory printed)'], 0, 0
    import glob
    import json
    import statedir as SD
    import hook as H
    import commit as CM
    import gitwrite as GW
    HO = old('hook.py', 'hook_v1330')
    tmp = os.path.abspath(tempfile.gettempdir()).lower()
    st = os.path.abspath(SD.STATE).lower()

    def place(p):
        a = os.path.abspath(p).lower()
        if a.startswith(st + os.sep):
            return 'the state folder (%s)' % os.path.relpath(p, os.path.dirname(SD.STATE)).replace('\\', '/')
        return 'the temp directory' if a.startswith(tmp + os.sep) else 'elsewhere'

    osrc = show(BASE, 'tools/standing/commit.py') or ''
    m = re.search(r'^CALLS = (.*)$', osrc, re.M)
    otool = 'the temp directory' if m and 'gettempdir()' in m.group(1) and "'standing-calls.jsonl'" in m.group(1) else 'NOT READ'
    n += 1
    g += case(L, 'state', 'the calls ledger: the hook appends one record a shell call, the one-call tool reads its tail (message_refusal)',
              'the hook %s ; the tool %s (its own path, built again)' % (place(HO.CALLS), otool),
              'the hook %s ; the tool %s ; one path %s' % (place(H.CALLS), place(CM.CALLS), H.CALLS == CM.CALLS == SD.calls_path()),
              place(HO.CALLS) == 'the temp directory' and otool == 'the temp directory',
              H.CALLS == CM.CALLS == SD.calls_path() and place(H.CALLS).startswith('the state folder'))
    x = 'a planted transcript path'
    n += 1
    g += case(L, 'state', 'the git-write state of a session`s transcript (the hook`s ledger_over), its name kept',
              'the hook %s' % place(HO.ledger_path(x)),
              'the hook %s ; the resolver`s path %s ; the name kept %s' % (place(H.ledger_path(x)), H.ledger_path(x) == SD.ledger_path(x),
                                                                        os.path.basename(H.ledger_path(x)) == os.path.basename(HO.ledger_path(x))),
              place(HO.ledger_path(x)) == 'the temp directory',
              H.ledger_path(x) == SD.ledger_path(x) and place(H.ledger_path(x)).startswith('the state folder')
              and os.path.basename(H.ledger_path(x)) == os.path.basename(HO.ledger_path(x)))
    live = SD.outside()
    keep = SD.STATE
    try:
        SD.STATE = os.path.join(RELAY, 'data', 'planted-state')
        in_repo = SD.outside()
        SD.STATE = os.path.join(tempfile.gettempdir(), 'planted-state')
        in_tmp = SD.outside()
    finally:
        SD.STATE = keep
    n += 1
    g += guard(L, 'state', 'statedir.outside() reads (outside every repository, outside the temp directory): the state folder as it stands both; '
               'a planted folder inside the relay not outside a repository; a planted folder under the temp directory not outside it',
               'the state folder %s ; planted in the relay %s ; planted under the temp directory %s' % (live, in_repo, in_tmp),
               live == (True, True) and in_repo[0] is False and in_tmp[1] is False)
    saved = sys.modules.get('statedir')
    try:
        sys.modules['statedir'] = None   # ### `import statedir` raises ImportError while this stands
        hs, hc = H._state()
        tc = CM._calls_path()
    finally:
        sys.modules['statedir'] = saved
    n += 1
    g += guard(L, 'state', 'the fallback alike: the resolver made unimportable, the hook and the tool each fall back to the temp directory and '
               'still read one ledger (the hook still refuses on it)',
               'the hook %s (resolver %s) ; the tool %s ; one path %s' % (place(hc), 'none' if hs is None else 'IMPORTED', place(tc), hc == tc),
               hs is None and hc == tc and place(hc) == 'the temp directory')
    oldp = os.path.join(tempfile.gettempdir(), 'standing-calls.jsonl')
    ol = [l for l in io.open(oldp, encoding='utf-8', errors='replace').read().split(NL) if l.strip()] if os.path.exists(oldp) else []
    nl_ = [l for l in io.open(SD.calls_path(), encoding='utf-8', errors='replace').read().split(NL) if l.strip()]
    gws = glob.glob(os.path.join(tempfile.gettempdir(), 'standing-gitwrite-*.json'))
    got = [os.path.exists(os.path.join(os.path.dirname(SD.calls_path()), os.path.basename(p))) for p in gws]
    n += 1
    g += guard(L, 'state', 'the carry: the temp directory`s calls ledger read whole into the state folder`s, its records first, and its git-write '
               'states copied by name; the temp directory`s files kept, none removed',
               'the temp ledger %d records, kept %s ; its records in the state folder`s %s, before the first record after the switch %s ; the '
               'state folder`s %d records ; git-write states %d of %d by name' % (
                   len(ol), os.path.exists(oldp), bool(ol) and nl_[:len(ol)] == ol,
                   bool(ol) and len(nl_) > len(ol) and json.loads(nl_[len(ol)]).get('at', '') >= SWITCH, len(nl_), sum(got), len(gws)),
               bool(ol) and nl_[:len(ol)] == ol and len(nl_) > len(ol) and json.loads(nl_[len(ol)]).get('at', '') >= SWITCH and all(got))
    by = {}
    for l in nl_:
        r = json.loads(l)
        if r.get('at', '') >= SWITCH and r.get('request') and GW.writes(r.get('cmd') or ''):
            by.setdefault(r['request'], []).append(r)
    two = {k: v for k, v in by.items() if len(v) >= 2}
    shape = []
    for k, v in sorted(two.items()):
        sub = []
        for r in v:
            mm = re.search(r'commit\.py[\'"]?\s+(\w+)\s+(\w+)\s+(\S+)', r.get('cmd') or '')
            sub.append('%s %s %s' % (r['at'][11:19], ' '.join(mm.groups()) if mm else 'NOT THE TOOL', r.get('refused') or 'ALLOWED'))
        shape.append('request %s: %s' % (k, ' ; '.join(sub)))
    refrows = [k for k, l in enumerate(io.open(os.path.join(D, 'b754_hook_refusals.txt'), encoding='utf-8').read().split(NL), 1)
               if '| GITWRITE |' in l and l[:19] >= SWITCH]
    ok = (len(two) == 1 and [r.get('refused') for r in list(two.values())[0]][:2] == [None, 'GITWRITE'] and len(refrows) == 1)
    n += 1
    g += guard(L, 'state', 'THE LIVE FORM, once, after the switch (the form of data/b753_events.txt (2)): one message carrying two runs of the tool, '
               'the earlier an add of a tracked file not differing, the later planted, refused by the hook through the state folder`s ledger before '
               'it ran; its refusal in this act`s refusals bank',
               '%d message(s) carrying two git writes since %sZ: %s ; the refusals bank`s GITWRITE rows since then %s' % (
                   len(two), SWITCH, ' | '.join(shape) or 'none', ', '.join(':%d' % k for k in refrows) or 'none'), ok)
    return L, g, n


# ================================================================================ (beyond) (R364)(3)(xvi)
M1_PASS = '0db31ce3'   # ### b753's [M1] pass commit (component 3): tools/mirror_roster_added.json written beside the base roster


def control_beyond():
    L, g, n = ['### (beyond) (R364)(3)(xvi), b753 (v`): A PASSED ITEM`S WRITE BEYOND THE (W) LIST -- tools/standing/amend.py`s item route banks '
               'the amendment row before the write, regenerates the (W) bank and writes act_current`s shared_edits in the same step'], 0, 0
    import json
    import amend as AM
    import wlist as WL
    import act as A_
    P = M1_PASS + '^'
    ruling = show(P, 'data/b753_ferry.txt') or ''
    rows = json.loads(show(P, 'data/b753_amendments.json') or '{"rows": []}').get('rows') or []
    pats = json.loads(show(P, 'data/b753_wlist.json') or '{}').get('patterns') or []
    base = json.loads(show(P, 'data/act_current.json') or '{}').get('pre_relay') or ''
    files = [f for f in _git('show', '--name-only', '--format=', M1_PASS).stdout.split(NL) if f.strip()]
    paths = ['relay/%s' % f for f in files if not f.startswith('data/b753_')]
    added = 'relay/tools/mirror_roster_added.json'
    at_pass = json.loads(show(M1_PASS, 'data/act_current.json') or '{}').get('shared_edits')
    rows_pass = json.loads(show(M1_PASS, 'data/b753_amendments.json') or '{"rows": []}').get('rows') or []
    later = [r for r in json.loads(show(BASE, 'data/b753_amendments.json') or '{"rows": []}').get('rows') or [] if added in (r.get('widens') or ())]
    committed = A_.shared_edits('b753', base, P)
    after_commit = A_.shared_edits('b753', base, M1_PASS)
    cov0 = WL.allows('relay', 'tools/mirror_roster_added.json', pats)
    row_then = any(added in (r.get('widens') or ()) for r in rows_pass)
    PL = AM.plan('b753', 'R363', '[M1]', '2026-11-11T17:55:38.033Z', 'data/b753_amendments.json, the row banked at the face', paths, pats,
                 committed, '2026-11-11T17:55:39Z', landed=lambda p: False)
    pats2 = list(pats) + ['%s/%s' % AM._split(w) for w in AM.writes(ruling, rows + ([PL['row']] if PL['row'] else []))]
    cov1 = not AM.beyond(paths, pats2)
    n += 1
    g += case(L, 'beyond', 'b753`s [M1] pass (relay %s: %s) replayed over b753`s banks at its parent: the (W) bank of 16:53:09Z (%d patterns), %d '
              'amendment rows, act_current`s base %s' % (M1_PASS, ', '.join(paths), len(pats), len(rows), base[:8]),
              'no route: the (W) bank covers the added list %s ; a row widening to it in the pass`s commit %s ; act_current`s shared_edits at the '
              'pass %s, the committed list after it %s' % (cov0, row_then, at_pass, after_commit),
              'the route: beyond %s ; a row widening %s ; covered after the row %s ; shared_edits written %s, equal to the committed list after the '
              'pass %s' % (PL['beyond'], (PL['row'] or {}).get('widens'), cov1, PL['shared'], PL['shared'] == after_commit),
              not cov0 and not row_then and added[6:] not in (at_pass or []) and added[6:] in after_commit,
              PL['beyond'] == [added] and (PL['row'] or {}).get('widens') == [added] and cov1 and PL['shared'] == after_commit)
    L.append('      BESIDE: the row b753 banked later, at the face`s composition: %s' % (
        '; '.join('%s widens %s narrows %s' % (r.get('at'), r.get('widens'), r.get('narrows')) for r in later) or 'none'))
    cur = WL._cur()
    lp, _src, _s = WL.patterns(cur['act'])
    lc = A_.shared_edits(cur['act'], cur['pre_relay'])
    PA = AM.plan(cur['act'], cur.get('ruling') or '', '[A1]', 'a planted time', 'a planted cite', ['PLACE-papers/FINDINGS.md'], lp, lc, 'now',
                 landed=lambda p: False)
    n += 1
    g += guard(L, 'beyond', 'a pass the list covers (b754`s live (W) bank, [A1]`s write of PLACE-papers/FINDINGS.md): no row owed, the shared list '
               'the committed one', 'beyond %s ; row %s ; shared %s, the committed list %s' % (PA['beyond'], PA['row'], PA['shared'], lc),
               PA['beyond'] == [] and PA['row'] is None and PA['shared'] == lc)
    PR = AM.plan(cur['act'], cur.get('ruling') or '', '[X0]', 'a planted time', 'a planted cite',
                 ['relay/data/b754_events.txt', 'relay/data/b754_ferry.txt', 'relay/tools/planted_absent_tool.json'], [], lc, 'now')
    n += 1
    g += guard(L, 'beyond', 'the refusal: a planted (W) list covering nothing; a path already written (data/b754_events.txt, differing from HEAD) '
               'refuses the route; one tracked and unchanged (data/b754_ferry.txt) and one absent and untracked do not',
               'beyond %d ; written before the row %s ; refused %s' % (len(PR['beyond']), PR['landed'], PR['refused']),
               PR['refused'] and PR['landed'] == ['relay/data/b754_events.txt'])
    t = io.open(os.path.join(D, 'act_current.json'), encoding='utf-8', newline='').read()
    t1, k1 = AM.SHARED_LINE.subn(lambda m: ' "shared_edits": %s%s' % (json.dumps(['tools/planted.json']), m.group(1)), t)
    t2, k2 = AM.SHARED_LINE.subn(lambda m: ' "shared_edits": %s%s' % (json.dumps(json.loads(t)['shared_edits'], ensure_ascii=False), m.group(1)), t1)
    same = sorted(json.loads(t)['shared_edits']) == lc
    n += 1
    g += guard(L, 'beyond', 'the field`s write: one line replaced, every other byte as it stands (a planted list in and the field back, in memory); '
               'the live field equal to the committed list after (c`)`s write',
               'lines replaced %d, %d ; the text back equal %s ; the planted list read %s ; the live field equal %s' % (
                   k1, k2, t2 == t, json.loads(t1)['shared_edits'], same),
               k1 == 1 and k2 == 1 and t2 == t and json.loads(t1)['shared_edits'] == ['tools/planted.json'] and same)
    return L, g, n


# ================================================================================ (harness) (R364)(3)(xvii)
B754_SEAT = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### the seat's session after the restart of 2026-11-12T18:38:28Z (data/b754_events.txt (7))
STEP_ZERO_HARNESS = dict(version='2.1.322', installed='2026-11-10T16:44:56Z', model='claude-opus-5-5', effort='xhigh', window=400000, channel='latest',
                         d1='1')   # ### step zero's print in this session, 15:33:40Z (data/b754_events.txt (7)), by scratch readers


def control_harness():
    L, g, n = ['### (harness) (R364)(3)(xvii): THE STEP-ZERO PRINT OF THE HARNESS -- tools/standing/harness.py: the version with its install date, '
               'the model by the transcript`s rows, the effort level and the window for that model, the update channel and [D1]`s key; a change '
               'against an earlier record an event'], 0, 0
    import json
    import harness as HN
    had = show(BASE, 'tools/standing/harness.py')
    HL, hok = HN.control(B754_SEAT)
    n += 1
    g += case(L, 'harness', 'the print as a standing route, with its planted settings, planted records and the live read of this session',
              'tools/standing/harness.py at %s: %s (step zero printed it by scratch readers, b753 and b754)' % (BASE, 'PRESENT' if had else 'ABSENT'),
              '; '.join(l.strip() for l in HL[1:]), had is None, hok)
    rec = HN.read(B754_SEAT)
    live = HN.changes(STEP_ZERO_HARNESS, rec)
    fd, tmp = tempfile.mkstemp(prefix='v1340_harness_', suffix='.txt', dir=STATE)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write('a planted bank\n' + HN.MARK + json.dumps(dict(STEP_ZERO_HARNESS, model='claude-fable-5-2', at='planted', session='planted')) + '\n')
        back = HN.record_at(tmp, 2)
        none_at = HN.record_at(tmp, 1)
    finally:
        os.remove(tmp)
    planted = HN.changes(back or {}, rec)
    n += 1
    g += guard(L, 'harness', 'the comparison: the live read against step zero`s figures in this session (data/b754_events.txt (7)) no change; a '
               'planted record line read back from a bank with the model changed one change, the model; a line carrying no record none',
               'against step zero %s ; against the planted record %s ; the line with no record %s' % (live or 'NO CHANGE', planted, none_at),
               live == [] and planted == [('model', 'claude-fable-5-2', rec.get('model'))] and none_at is None)
    return L, g, n


# ================================================================================ (hookctl) (R364)(3)(xix), b754 defects (e), (f)
def control_hookctl():
    L, g, n = ['### (hookctl) (R364)(3)(xix), b754 (e), (f): THE HOOK`S CONTROL AT STEP ZERO -- its table moved with PLAINGIT and LIMIT and the '
               'five intents added in their current forms; its verdict read from the table and the constructed instance, the record`s instance '
               'printed as not reachable since the repair'], 0, 0
    import hook as H
    HO = old('hook.py', 'hook_v1330')
    act = A.current().get('act')

    def score(cs):
        got = [(t, i, w, (H.judge(t, i) or (None,))[0]) for t, i, w in cs]
        return sum(1 for _t, _i, w, k in got if w == k), len(got), [(t, w, k) for t, _i, w, k in got if w != k]

    so, sn = score(HO.cases(act)), score(H.cases(act))
    n += 1
    g += case(L, 'hookctl', 'the control`s table judged by the hook as it stands (every kind of the table enforced)',
              '%d of %d, not as wanted %s' % (so[0], so[1], so[2]), '%d of %d, not as wanted %s' % (sn[0], sn[1], sn[2] or 'none'),
              so[0] < so[1], sn[0] == sn[1] and sn[1] == so[1] + 5)
    bank = (show('HEAD', 'data/%s_hook_control.txt' % act) or '').rstrip(NL).split(NL)
    vb = [l for l in bank if 'THE REPAIR HOLDS' in l]
    LN = H.control_lines(act)
    vn = [l for l in LN if 'THE REPAIR HOLDS' in l]
    tmpd = os.path.abspath(tempfile.gettempdir()).lower()
    n += 1
    g += case(L, 'hookctl', 'the verdict: THE REPAIR HOLDS, and no path under the temp directory in the lines',
              'step zero`s bank (data/%s_hook_control.txt at HEAD, v1.33.0): %s' % (act, (vb[-1][-60:] if vb else 'ABSENT')),
              'control_lines now: %s ; a path under the temp directory %s' % (vn[-1][-110:] if vn else 'ABSENT', any(tmpd in l.lower() for l in LN)),
              bool(vb) and vb[-1].rstrip('*. ').endswith('False'), bool(vn) and vn[-1].rstrip('*. ').endswith('True') and not any(tmpd in l.lower() for l in LN))
    keep = H.cases
    try:
        H.cases = lambda a: keep(a) + [('Bash', {'command': 'git status | head'}, None)]
        LP = H.control_lines(act)
    finally:
        H.cases = keep
    vp = [l for l in LP if 'THE REPAIR HOLDS' in l]
    n += 1
    g += guard(L, 'hookctl', 'a planted case wanting a piped command allowed: the table one short and the verdict False',
               (vp[-1][-80:] if vp else 'ABSENT'), bool(vp) and vp[-1].rstrip('*. ').endswith('False') and 'THE TABLE %d OF %d' % (sn[1], sn[1] + 1) in vp[-1])
    return L, g, n


# ================================================================================ (flag) (R364)(3)(xxi), the amendment rows 1 (1) and 3 (1)
def _capture(fn):
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        r = fn()
    return r, buf.getvalue()


def control_flag():
    L, g, n = ['### (flag) (R364)(3)(xxi): THE RESTART FLAG AFTER STEP ZERO -- tools/standing/hold.py`s refuses() reads it where it reads the '
               'memory and the volumes (each record route, each suite part, the lock); a flag set an event printed with the keys` last writes, '
               'the route not run, the one-call tool printing the stop at the next commit'], 0, 0
    import hold as HN
    import commit as CM
    HO = old('hold.py', 'hold_v1330')
    planted = (True, 'RebootPending, RebootRequired')
    times = {'RebootPending': '2026-11-12T16:35:36Z', 'RebootRequired': '2026-11-12T16:38:07Z'}   # ### b754's own, data/b754_events.txt (5)
    ok_mem = dict(hold=0, free=10 ** 6, disks={'C:\\': 30000, 'D:\\': 600000}, floor=5000)
    keep = HO.restart_pending
    try:
        HO.restart_pending = lambda read=None: planted
        ro, po = _capture(lambda: HO.refuses('record step', **ok_mem))
    finally:
        HO.restart_pending = keep
    rn, pn = _capture(lambda: HN.refuses('record step', flag=planted, times=times, **ok_mem))
    n += 1
    g += case(L, 'flag', 'a record route with the flag planted set after step zero (b754`s keys and times, events (5)), the memory and both volumes '
              'above their holds', 'refuses %s, printed %r' % (ro, po.strip()[:60] or 'nothing'),
              'refuses %s, printed %s' % (rn, pn.strip()[22:200]),
              ro is False, rn is True and 'AN EVENT OF THE ACT' in pn and '2026-11-12T16:38:07Z' in pn and 'NEXT COMMIT BOUNDARY' in pn)
    tpl_o = show(BASE, 'tools/standing/fold/checks.tpl') or ''
    tpl_n = io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()

    def part_guard(t):
        k = t.find("if PART not in KS.PARTS:")
        return t[k:k + 900]
    n += 1
    g += case(L, 'flag', 'a suite part`s guard before it runs, read from the template`s text (checks.tpl main): the memory alone, or hold.refuses '
              'with the volumes and the flag', 'standing.hold called %s' % ('standing.hold' in part_guard(tpl_o)),
              'standing.hold called %s, after the memory`s own line %s' % ('standing.hold' in part_guard(tpl_n), 'free_mb()' in part_guard(tpl_n)),
              'standing.hold' not in part_guard(tpl_o), 'standing.hold' in part_guard(tpl_n) and 'free_mb()' in part_guard(tpl_n))
    osrc = show(BASE, 'tools/standing/commit.py') or ''
    k = osrc.find('def run(')
    old_reads = 'restart' in osrc[k:osrc.find('\ndef ', k + 1)]
    try:
        CM.run('relay', 'lock', 'a planted lock', flag=planted + (times,))
        lock = 'RAN'
    except CM.Refused as e:
        lock = 'REFUSED: %s' % str(e)[:150]
    n += 1
    g += case(L, 'flag', 'the lock with the flag planted set (the one-call tool`s run, refused before any read or write)',
              'run() reads the flag %s (read from its text at %s; not run)' % (old_reads, BASE), lock,
              not old_reads, lock.startswith('REFUSED: THE RESTART FLAG SET') and '16:38:07Z' in lock)
    b1, b0 = HN.boundary_line(True, planted[1], times), HN.boundary_line(False, 'none', {})
    r4, _p4 = _capture(lambda: HN.refuses('record step', flag=(False, 'none'), **ok_mem))
    n += 1
    g += guard(L, 'flag', 'the stop at the boundary: the one-call tool`s line at a commit with the flag set names the commit the boundary; with none, '
               'none; a route with no flag set runs', '%s | %s | the route refused %s' % (b1[:150], b0, r4),
               'THIS COMMIT IS THE BOUNDARY' in b1 and b0.endswith(': none') and r4 is False)
    (hok, hl), _ph = _capture(HN.control)
    n += 1
    g += guard(L, 'flag', 'hold.py`s own control, its planted flag among its cases', hl[0][-170:], hok)
    return L, g, n


# ================================================================================ (clauses) b754 defect (j)
CLAUSE_SITES = (('citation.tpl', 'THE COMPARATIVE SENTENCES AGAINST THE TABLES THEY CITE', 'R348'),
                ('citation.tpl', 'OK or NONE at HEAD, by the text alone', 'R362'),
                ('citation.tpl', 'EVERY PATH THE RULING AND THE FERRY NAME, AT HEAD', 'R362'),
                ('citation.tpl', 'the branch deletes wait on CLEAN', 'R348'),
                ('checks.tpl', 'THE REMOTE READS OF THIS SUITE RUN', 'R352'),
                ('checks.tpl', 'THE REMOTE READS CLASSED', 'R356'),
                ('record.tpl', 'THE BANK WRITTEN BEFORE THE LOCK STANDS -- NOTHING RUN', 'R348'))
CLAUSE_RULINGS = (('v1.18.0', 'b738', 'R348'), ('v1.22.0', 'b742', 'R352'), ('v1.26.0', 'b746', 'R356'), ('v1.32.0', 'b752', 'R362'))
RUL_FORM = '(\u27eaRUL\u27eb)('
TEMPLATES = ('checks.tpl', 'closing.tpl', 'citation.tpl', 'regspec.tpl', 'record.tpl', 'report.tpl')


def _line_with(text, needle):
    return next((l for l in (text or '').split(NL) if needle in l), None)


def control_clauses():
    L, g, n = ['### (clauses) b754 defect (j): THE TEMPLATES NAME THE ACT`S OWN RULING FOR AN OLDER RULING`S CLAUSE -- each printed clause the seat '
               'repaired named by the ruling that made it; the form `(\u27eaRUL\u27eb)(` elsewhere carried with its count, no mechanical source naming '
               'their rulings'], 0, 0
    olds = dict((t, show(BASE, 'tools/standing/fold/' + t) or '') for t in TEMPLATES)
    news = dict((t, io.open(os.path.join(S, 'fold', t), encoding='utf-8').read()) for t in TEMPLATES)
    rows, of, np_ = [], 0, 0
    for t, needle, rul in CLAUSE_SITES:
        lo, ln = _line_with(olds[t], needle), _line_with(news[t], needle)
        f = lo is not None and RUL_FORM in lo
        p = ln is not None and RUL_FORM not in ln and ('(%s)' % rul) in ln
        of, np_ = of + f, np_ + p
        rows.append('%s %r: before %s, after (%s) %s' % (t, needle[:40], 'the act`s ruling' if f else 'NOT FOUND', rul, 'named' if p else 'NOT NAMED'))
    n += 1
    g += case(L, 'clauses', 'the seven sites the seat repaired (four in the citation template, two in the checks template, one in the record '
              'template), each read on the line its needle stands on', '%d of %d carry `(\u27eaRUL\u27eb)(`' % (of, len(CLAUSE_SITES)),
              '%d of %d name their ruling -- %s' % (np_, len(CLAUSE_SITES), ' | '.join(rows)), of == len(CLAUSE_SITES), np_ == len(CLAUSE_SITES))
    got = []
    for ver, act, rul in CLAUSE_RULINGS:
        first = (show('HEAD', 'data/%s_ferry.txt' % act) or '').split(NL, 1)[0].strip()
        got.append((ver, act, rul, first == 'RULING (%s) BEGIN' % rul))
    n += 1
    g += guard(L, 'clauses', 'each ruling named is the ruling of the act whose version made the section (the version`s act`s ferry opening '
               'on that ruling`s marker, read at HEAD)', ' ; '.join('%s %s %s %s' % (v, a, r, 'AGREES' if ok else 'DIFFERS') for v, a, r, ok in got),
               all(ok for _v, _a, _r, ok in got))
    co = dict((t, olds[t].count(RUL_FORM)) for t in TEMPLATES)
    cn = dict((t, news[t].count(RUL_FORM)) for t in TEMPLATES)
    n += 1
    g += guard(L, 'clauses', 'the form`s count by template, before and after: lower by the seven repaired and by nothing else; the rest carried '
               'with the count', ' ; '.join('%s %d -> %d' % (t, co[t], cn[t]) for t in TEMPLATES) + ' ; total %d -> %d' % (sum(co.values()), sum(cn.values())),
               sum(co.values()) - sum(cn.values()) == len(CLAUSE_SITES))
    return L, g, n


# ================================================================================ (nouns) b754 defect (k)
def control_nouns():
    L, g, n = ['### (nouns) b754 defect (k): THE COMPARATIVE READER TAKES A NOUN FOR A COMPARISON -- "lead" and "trail" after a determiner or a '
               'possessive read as nouns and printed apart; the comparisons still read'], 0, 0
    import cites as CI
    OCI = old('cites.py', 'cites_v1330')
    inst = 'a read of b753' + chr(39) + 's trail heading in OPEN_TRAILS.md'   # ### row (g)`s form at 17:09:30Z (defect (k)), planted
    ho, hn, nn = OCI.comparative_hits('planted', inst), CI.comparative_hits('planted', inst), CI.comparative_nouns('planted', inst)
    n += 1
    g += case(L, 'nouns', 'a line naming b753`s record heading by the possessive and the noun, in the form of row (g) at the halt',
              'comparisons %s' % ho, 'comparisons %s ; nouns apart %s' % (hn, nn), len(ho) == 1, not hn and len(nn) == 1)
    comp = NL.join(('b754 trails b753 by 3 rows and leads b752', 'the least of them', 'the trail of b752', 'at least two ; leads to none'))
    hc, nc = CI.comparative_hits('planted', comp), CI.comparative_nouns('planted', comp)
    n += 1
    g += guard(L, 'nouns', 'the comparisons still read (trails, leads, the least); "at least" and "leads to" none; "the trail" a noun',
               'comparisons %s ; nouns %s' % ([w for _b, _i, w in hc], [w for _b, _i, w in nc]),
               sorted(w for _b, _i, w in hc) == ['leads', 'least', 'trails'] and [w for _b, _i, w in nc] == ['trail'])
    to = show(BASE, 'tools/standing/fold/citation.tpl') or ''
    tn = io.open(os.path.join(S, 'fold', 'citation.tpl'), encoding='utf-8').read()
    n += 1
    g += case(L, 'nouns', 'the citation bank prints the nouns apart, not halting (read from the template`s text)',
              'comparative_nouns in the template %s' % ('comparative_nouns' in to), 'comparative_nouns in the template %s' % ('comparative_nouns' in tn),
              'comparative_nouns' not in to, 'comparative_nouns' in tn)
    return L, g, n


# ================================================================================ (readers) the amendment row 3 (6)
def control_readers():
    L, g, n = ['### (readers) (R364) amendment row 3 (6): THE TWO READERS -- tools/standing/cites.py`s ferry_paths resolves a bare name by the '
               'trees (the relay`s root, PLACE-papers, both; in neither and ordered by a clause, TO BE WRITTEN with the clause; otherwise NONE); '
               'the (W) entries a ruling gives in words entered as rows of the (W) bank, each with its clause, printed before the lock'], 0, 0
    import cites as CI
    import wlist as WL
    OCI = old('cites.py', 'cites_v1330')
    OWL = old('wlist.py', 'wlist_v1330')
    act = A.current()['act']
    pp = 'D:/MY-DOwnloads/PLACE-papers'
    t = io.open(os.path.join(D, '%s_ferry.txt' % act), encoding='utf-8').read()
    po, _so, _x = OWL.patterns(act)
    # ### the route before the repair reads its (W) list as v1.33.0 regenerated it (no word rows), not the bank on disk, which v1.34.0 wrote
    OCI._wlist_relay = lambda act_, relay_: [p_[len('relay/'):] for p_ in po if p_.startswith('relay/')]
    fo = dict((p, (r, s)) for p, r, s in OCI.ferry_paths(t, act, RELAY, pp))
    fn = CI.ferry_paths(t, act, RELAY, pp)
    fd = dict((p, (r, s)) for p, r, s in fn)
    want = ('CLAUDE.md', 'HANDOFF.md')
    n += 1
    g += case(L, 'readers', 'CLAUDE.md and HANDOFF.md as b754`s ferry names them: the relay`s seat file ((3)(i)) and the relay`s handoff page',
              ' ; '.join('%s %s %s' % (p, fo.get(p, ('?', '?'))[0], fo.get(p, ('?', '?'))[1]) for p in want),
              ' ; '.join('%s %s %s' % (p, fd.get(p, ('?', '?'))[0], fd.get(p, ('?', '?'))[1]) for p in want),
              all(fo.get(p, ('', ''))[1] == 'NONE' for p in want),
              fd.get('HANDOFF.md') == ('relay', 'OK') and fd.get('CLAUDE.md', ('', ''))[0] == 'relay'
              and (fd['CLAUDE.md'][1] == 'OK' or fd['CLAUDE.md'][1].startswith(CI.TO_BE_WRITTEN + '(R364)(3)(i)')))
    q = 'data/b755_address_scan_commits.txt'
    n += 1
    g += case(L, 'readers', 'the next act`s per-commit scan bank, named in (8)`s words: by the worklist`s W_WORDS row, TO BE WRITTEN with its clause',
              '%s %s' % fo.get(q, ('?', '?')), '%s %s' % fd.get(q, ('?', '?')), fo.get(q, ('', ''))[1] == 'NONE',
              fd.get(q, ('', ''))[1].startswith(CI.TO_BE_WRITTEN + '(R364)(8)'))
    pl = CI.ferry_paths('PLANTED_NOWHERE.md', act, RELAY, pp)
    pw = CI.ferry_paths('PLANTED_NOWHERE.md', act, RELAY, pp, words=(('relay/PLANTED_NOWHERE.md', '(planted) a clause ordering it'),))
    n += 1
    g += guard(L, 'readers', 'a planted name in no tree and ordered by no clause reads NONE; the same name with a planted word row reads TO BE '
               'WRITTEN with that clause', '%s | %s' % (pl, pw),
               pl == [('PLANTED_NOWHERE.md', 'neither', 'NONE')] and pw == [('PLANTED_NOWHERE.md', 'relay', CI.TO_BE_WRITTEN + '(planted) a clause ordering it')])
    n += 1
    g += guard(L, 'readers', '%s`s ferry by the new reader: no path NONE' % act,
               'paths %d ; OK %d ; NONE %d ; the act`s own %d ; by a clause %d' % (len(fn), sum(s == 'OK' for _p, _r, s in fn), sum(s == 'NONE' for _p, _r, s in fn),
                                                                                    sum(s.startswith('THE ACT') for _p, _r, s in fn), sum(s.startswith(CI.TO_BE_WRITTEN) for _p, _r, s in fn)),
               not any(s == 'NONE' for _p, _r, s in fn))
    pn, _sn, srcs = WL.patterns(act)
    wr = WL.word_rows(act)
    shown = NL.join(WL.regenerate(act, write=False))
    n += 1
    g += case(L, 'readers', 'the (W) list regenerated for %s: the entries (8) gives in words, as rows with their clauses' % act,
              'patterns %d ; relay/CLAUDE.md %s' % (len(po), 'relay/CLAUDE.md' in po),
              'patterns %d ; word rows %d, each a pattern %s and printed with its clause %s ; the worklist`s W_WORDS a source %s' % (
                  len(pn), len(wr), all(q_ in pn for q_, _c in wr), all(('%s -- %s' % r) in shown for r in wr), 'tools/%s_worklist.py#W_WORDS' % act in srcs),
              'relay/CLAUDE.md' not in po, bool(wr) and all(q_ in pn for q_, _c in wr) and all(('%s -- %s' % r) in shown for r in wr)
              and 'tools/%s_worklist.py#W_WORDS' % act in srcs)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED AND ITS CONTROLS TALLIED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.33.0', ver == 'v1.34.0')
    return L, g, n


CONTROLS = dict(seat=control_seat, carry=control_carry, closescan=control_closescan, lean=control_lean, postseal=control_postseal, vmove=control_vmove,
                subject=control_subject, letters=control_letters, n3=control_n3, rootparts=control_rootparts, table=control_table, delread=control_delread,
                limit=control_limit, words=control_words, state=control_state, beyond=control_beyond, harness=control_harness,
                hookctl=control_hookctl, flag=control_flag, clauses=control_clauses, nouns=control_nouns, readers=control_readers,
                version=control_version)
ORDER = ('seat', 'carry', 'closescan', 'lean', 'postseal', 'vmove', 'subject', 'letters', 'n3', 'rootparts', 'table', 'delread', 'limit', 'words',
         'state', 'beyond', 'harness', 'hookctl', 'flag', 'clauses', 'nouns', 'readers', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.0, (R364)(3) AND THE AMENDMENT ROWS 1 TO 3 (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
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
    out.append('### ### **v1.34.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1340.txt' % act), NL.join(out))
        print('written data/%s_standing_v1340.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
