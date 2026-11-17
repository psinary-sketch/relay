# -*- coding: utf-8 -*-
"""standing/closebound.py -- v1.35.7, (R368)(1) AMENDED ON THE AUTHOR'S WORD (relay data/b758_amendments.json row 1): A CLOSE RUN INSIDE A
LATER ACT READS N2, N4, N5 AND S3 AS AT THE NEXT ACT'S OPENING COMMIT.

b757 stopped at [22] on the author's word (2026-11-16T23:02:40Z). b758 ran [22] for it after b758's own commits (relay 49c58344 to ac6a0a77),
and four of the close's readers, each reading the relay to HEAD, its working tree and the tools on disk, took b758's work as b757's: N2
counted v1.35.6 among b757's commits under tools/standing/, N4 b758's commits after b757's lock, N5 b758's tools and banks beyond b757's
membrane and (W) list and v1.35.6's files as sealed tools not agreeing, S3 the same files (data/b758_put_1.json, data/b757_scores_close.json
as first written). The author's words (transcript line 115131, 2026-11-17T00:31:28Z): "one standing change, VERSION moved, bounding the
readers behind N2, N4, N5 and S3 at the next act's opening commit (49c58344) when a close runs inside a later act."

THE BOUND. Where data/act_current.json names an act other than the one whose scores are read, the next act's opening commit is the first
relay commit after the closed act's PRE_RELAY, oldest first, whose data/act_current.json names another act (b757's: 49c58344, b758's step 1);
the base is that commit's parent (b757's: ff65ccdb, its record push), the cut its committer time. For the length of each of N2, N4 and N5 and
of S3's reading, every git call naming the relay (`git -C <relay>`, or a cwd that is the relay) is read at the base:
  a revision named HEAD (`HEAD`, `<rev>..HEAD`, `HEAD:<path>`, `HEAD~n`, `HEAD^`) names the base; a history read naming no revision (log,
    rev-list) reads from the base;
  the working tree and the index are the later act's: `status` reads clean, a diff naming no commit or HEAD alone reads empty, a diff naming
    one other commit reads that commit against the base, `ls-files` keeps the names the base's tree holds;
  `reflog` drops the entries at or after the cut;
and the sealed tools' hashes read each tool as the base checks it out (`git cat-file --filters <base>:tools/<t>`), over the tools the closed
act's sealed list names that the base's tree holds and every tool its seal recorded, a tool the seal recorded and the base lacks read absent.
Each bounded reading carries the bound at its end. N1, N3, S1 and S2 read as before. Where the close runs inside its own act, or no commit
after PRE_RELAY names another act, or the route is not `scores close`, nothing is bounded and the scores are composed as record.tpl composed them.

THE LIMITS, entered as such: PLACE-papers, the kernels, the remotes and the session's capture are read as they stand, so a close inside a later
act reads them as the closed act's only before that act writes there (the bound line prints PLACE-papers' commits since the cut); an option
taking its value as a separate word (`-n 5`) would be read as a revision -- the readers send none (data/b758_standing_v1357.txt, (calls)).

  opening(act, pre, root, run=None) -> (next act, opening commit, base, cut) or None
  Bound(act, nxt, opening, base, cut, root, run0)    .run(cmd, ...) the bounded subprocess.run; .read(mod, R, fn) fn() read bounded
  sealed_at(K, act, root, base, run0) -> (rec_, now, out)    R.seal_hashes's reading at the base
  bound(act, K, root, run0=None) -> Bound or None
  scores(mod, R, act, close, run0=None) -> the dict record.tpl's scores() writes, N2, N4, N5 and S3 bounded at a close inside a later act
Imports the standard library alone; writes nothing.
"""
import contextlib
import hashlib
import json
import os
import re
import subprocess
import time

TEXT_KEYS = ('text', 'universal_newlines', 'encoding', 'errors')
REFLOG_TIME = re.compile(r'@\{(\d+)\}')


def _same(a, b):
    try:
        return os.path.normcase(os.path.abspath(str(a))).rstrip('\\/') == os.path.normcase(os.path.abspath(str(b))).rstrip('\\/')
    except (TypeError, ValueError):
        return False


def _out(r):
    return r.stdout.decode('utf-8', 'replace') if isinstance(r.stdout, bytes) else (r.stdout or '')


def opening(act, pre, root, run=None):
    """(the act data/act_current.json names after `act`, its opening commit, the base, the cut), or None where data/act_current.json names
    `act` itself or no commit after `pre` names another act."""
    run = run or subprocess.run
    p = os.path.join(root, 'data', 'act_current.json')
    try:
        with open(p, encoding='utf-8') as f:
            cur = json.load(f).get('act')
    except (OSError, ValueError):
        return None
    if not cur or cur == act or not pre:
        return None
    hs = _out(run(['git', '-C', root, 'log', '--reverse', '--format=%H', '%s..HEAD' % pre, '--', 'data/act_current.json'], capture_output=True)).split()
    for h in hs:
        r = run(['git', '-C', root, 'show', '%s:data/act_current.json' % h], capture_output=True)
        try:
            a = json.loads(_out(r)).get('act') if r.returncode == 0 else None
        except ValueError:
            a = None
        if a and a != act:
            base = _out(run(['git', '-C', root, 'rev-parse', '%s^' % h], capture_output=True)).strip()
            ct = _out(run(['git', '-C', root, 'log', '-1', '--format=%ct', h], capture_output=True)).strip()
            if base and ct.isdigit():
                return a, h, base, int(ct)
            return None
    return None


def _sub(x, base):
    """a revision word with HEAD naming the base: `HEAD`, `<a>..HEAD`, `<a>...HEAD`, `HEAD..<b>`, `HEAD:<path>`, `HEAD~n`, `HEAD^`."""
    s = str(x)
    if s.startswith('-'):
        return x
    parts = re.split(r'(\.\.\.?)', s)
    out = [(base + p[4:]) if (p == 'HEAD' or (p.startswith('HEAD') and p[4:5] in ('^', '~', ':'))) else p for p in parts]
    return ''.join(out)


def _revs(args):
    cut = args.index('--') if '--' in args else len(args)
    return cut, [x for x in args[:cut] if not str(x).startswith('-')]


def sealed_at(K, act, root, base, run0):
    """R.seal_hashes's reading with the tools read at the base: (the seal's record, the hashes at the base, [(tool, agree|differ|absent)])."""
    p = os.path.join(root, 'data', '%s_seal_hashes.json' % act)
    rec_ = {}
    if os.path.isfile(p):
        with open(p, encoding='utf-8') as f:
            rec_ = json.load(f).get('tools') or {}
    names = list(K.SEALED) + sorted(t for t in rec_ if t not in set(K.SEALED))
    now, out = {}, []
    for t in names:
        r = run0(['git', '-C', root, 'cat-file', '--filters', '%s:tools/%s' % (base, t)], capture_output=True)
        if r.returncode != 0 and t not in rec_:
            continue   # ### a tool the later act added: not the closed act's
        now[t] = hashlib.sha256(r.stdout).hexdigest() if r.returncode == 0 else None
        out.append((t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')))
    return rec_, now, out


class Bound(object):
    def __init__(self, act, nxt, opening_, base, cut, root, run0):
        self.act, self.nxt, self.opening, self.base, self.cut, self.root, self.run0 = act, nxt, opening_, base, cut, root, run0
        self.calls = 0
        self._tree = None

    def iso(self):
        return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(self.cut))

    def note(self):
        return (' -- READ BOUNDED (tools/standing/closebound.py, v1.35.7, (R368)(1) amended on the author`s word): the relay as at %s, the '
                'parent of %s`s opening commit %s (%s); its working tree, its later commits and its reflog from %s read as %s`s' % (
                    self.base[:8], self.nxt, self.opening[:8], self.iso(), self.iso(), self.nxt))

    def tree(self):
        if self._tree is None:
            r = self.run0(['git', '-C', self.root, 'ls-tree', '-r', '--name-only', '-z', self.base], capture_output=True)
            self._tree = set(x for x in _out(r).split('\0') if x)
        return self._tree

    def _split(self, cmd, k):
        if not isinstance(cmd, (list, tuple)) or not cmd or os.path.basename(str(cmd[0])).lower() not in ('git', 'git.exe'):
            return None
        cmd, i, repo = list(cmd), 1, None
        while i < len(cmd) and str(cmd[i]).startswith('-'):
            if cmd[i] == '-C' and i + 1 < len(cmd):
                repo, i = cmd[i + 1], i + 2
            elif cmd[i] == '-c':
                i += 2
            else:
                i += 1
        if i >= len(cmd) or not _same(repo if repo is not None else (k.get('cwd') or os.getcwd()), self.root):
            return None
        return cmd[:i], str(cmd[i]), cmd[i + 1:]

    def _empty(self, cmd, k):
        e = '' if any(k.get(x) for x in TEXT_KEYS) else b''
        return subprocess.CompletedProcess(cmd, 0, e, e)

    def _filtered(self, cmd, k, keep):
        r = self.run0(cmd, **k)
        if r.stdout is None:
            return r
        txt = isinstance(r.stdout, str)
        s = r.stdout if txt else r.stdout.decode('utf-8', 'replace')
        sep = '\0' if '-z' in cmd else '\n'
        s = sep.join(x for x in s.split(sep) if not x or keep(x))
        return subprocess.CompletedProcess(r.args, r.returncode, s if txt else s.encode('utf-8'), r.stderr)

    def run(self, cmd, *a, **k):
        sp = self._split(cmd, k)
        if sp is None or a:
            return self.run0(cmd, *a, **k)
        self.calls += 1
        head, sub, args = sp
        if sub == 'status' or sub == 'diff-files':
            return self._empty(cmd, k)
        if sub in ('diff', 'diff-index'):
            cut, revs = _revs(args)
            if not revs or revs == ['HEAD']:
                return self._empty(cmd, k)   # ### the working tree or the index against HEAD: the later act's
            if len(revs) == 1 and '..' not in str(revs[0]):
                args = args[:cut] + [self.base] + args[cut:]   # ### the working tree against one commit read as that commit against the base
        elif sub in ('log', 'rev-list', 'shortlog', 'whatchanged'):
            cut, revs = _revs(args)
            if not revs:
                args = args[:cut] + [self.base] + args[cut:]
        elif sub == 'ls-files':
            tr = self.tree()
            return self._filtered(head + [sub] + list(args), k, lambda x: x.strip('"') in tr)
        elif sub == 'reflog':
            return self._filtered(head + [sub] + list(args), k,
                                  lambda x: not (REFLOG_TIME.search(x) and int(REFLOG_TIME.search(x).group(1)) >= self.cut))
        return self.run0(head + [sub] + [_sub(x, self.base) for x in args], **k)

    @contextlib.contextmanager
    def installed(self, mod, R):
        saved = (subprocess.run, mod.get('seal_hashes'), getattr(R, 'seal_hashes', None))
        hs = lambda: sealed_at(mod['K'], self.act, self.root, self.base, self.run0)   # noqa: E731
        subprocess.run = self.run
        if 'seal_hashes' in mod:
            mod['seal_hashes'] = hs
        if saved[2] is not None:
            R.seal_hashes = hs
        try:
            yield self
        finally:
            subprocess.run = saved[0]
            if saved[1] is not None:
                mod['seal_hashes'] = saved[1]
            if saved[2] is not None:
                R.seal_hashes = saved[2]

    def read(self, mod, R, fn):
        with self.installed(mod, R):
            v = fn()
        return (v[0], str(v[1]) + self.note())

    def line(self, pp=None):
        n = None
        if pp:
            n = _out(self.run0(['git', '-C', pp, 'rev-list', '--count', '--since=%d' % self.cut, 'HEAD'], capture_output=True)).strip()
        return ('  ### THE BOUND (v1.35.7, (R368)(1) amended): %s`s close inside %s -- N2, N4, N5 and S3 read the relay as at %s, the parent of %s`s '
                'opening commit %s (%s); N1, N3, S1 and S2 as before; PLACE-papers commits since %s: %s (read as they stand)' % (
                    self.act, self.nxt, self.base[:8], self.nxt, self.opening[:8], self.iso(), self.iso(), n if n is not None else 'unread'))


def bound(act, K, root, run0=None):
    run0 = run0 or subprocess.run
    o = opening(act, getattr(K, 'PRE_RELAY', None), root, run0)
    return Bound(act, o[0], o[1], o[2], o[3], root, run0) if o else None


def scores(mod, R, act, close, run0=None):
    """record.tpl's scores() composition: N1 to N5, then S1 to S3 from _s_scores; at `scores close` inside a later act, N2, N4, N5 and S3
    read bounded, each reading carrying the bound."""
    b = bound(act, mod['K'], mod['ROOT'], run0) if close else None
    if b is None:
        return dict([('N1', mod['_n1']()), ('N2', mod['_n2']()), ('N3', mod['_n3']()), ('N4', mod['_n4']()), ('N5', mod['_n5']())]
                    + list(mod['_s_scores']().items()))
    print(b.line(mod.get('PP')), flush=True)
    n = [('N1', mod['_n1']()), ('N2', b.read(mod, R, mod['_n2'])), ('N3', mod['_n3']()), ('N4', b.read(mod, R, mod['_n4'])),
         ('N5', b.read(mod, R, mod['_n5']))]
    s = dict(mod['_s_scores']())
    s['S3'] = b.read(mod, R, lambda: mod['_s_scores']()['S3'])
    return dict(n + list(s.items()))
