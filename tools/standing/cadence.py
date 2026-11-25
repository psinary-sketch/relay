# -*- coding: utf-8 -*-
"""tools/standing/cadence.py -- v1.34.9, (R366)(6)[U1]: THE CADENCE OF THE PASSES (relay data/b754_rules.txt (10)), in force from b757,
the act that follows its change (the author's word beside the row, relay data/b754_author_answers.txt :121).

THE RULE, as the row quotes it: "What tests the record's own machinery runs when that machinery changed and at every sitting: the arms'
pre-run where tools/standing/ or the act part moved since the bank it would repeat, the sealed hashes saying so, and otherwise read from the
last pre-run's bank with a line naming it; the pass in the previous act's mode at sittings; the pass after the push held to the arms that
read a remote, the others read from the pass before the push where no bank they read changed between the two. The seat fits these three to
the yield table -- a pass or an arm that printed, in the acts the table reads, a failure no other pass printed keeps its place -- ..."

THE FIT, printed before the put (relay data/b754_agenda.txt :358-:380), is KEEP below, mode by mode. One part joins each mode beside the fit:
standing-a1, which holds no arm, because standing-a2 joins standing-a1's half bank of G-NO-SORRY-MAIN at the same HEAD (the suite's main,
the a1 join) and reads too few kernels without it. In the pass after the push the chain parts standing-b2b to standing-b2d and standing-b3
are run or read together: standing-b3 joins the four chain parts' half banks of its own run, so it runs only where all four ran.

HOW A PART IS HELD. The seat still calls every part in the standing order; the close order, the part order, the combine and the seal read the
banks they read before this change, under the same names.
  prerun     a part outside KEEP runs where tools/standing/ moved since the run its last pre-run bank repeats (the tree id of tools/standing/
             at that run's relay head against HEAD's, and no tracked change of tools/standing/ in the working tree), and is otherwise read
             from that bank: the previous act's pre-run bank of the part, read at the commit that added it;
  prev       a part outside KEEP runs at a sitting (the act's ferry title -- its ACT line before the first colon -- carrying the word
             SITTING; a ferry or an ACT line not read counts as a sitting) and is otherwise not run, its banks saying so;
  post-push  a part outside KEEP runs where a bank its pre-push run read changed, or where that run left no read record, and is otherwise
             read from the pass before the push;
  pre-push, mid, probe and --rerun-postpush: every part runs, as before.
A part read from a bank writes the banks its run would write under the mode's names: the part bank (the cadence's naming lines, then the
source's lines whole, its footer's seconds this read's and the source's printed beside), the remote reads' bank (no read), the exercise bank
(the source's verdicts; the mode, time and head this read's; the source named) and, in the pre-run alone, the per-part seconds bank (each arm
0.0 s, the source's seconds beside). A part not run at a non-sitting act writes the part bank, the remote reads' bank and the exercise bank in
the mode `prev` with no arm run, so the seal's read of the runs on the previous act's banks finds the part and counts nothing for it.

THE READ RECORD, for the pass after the push. Every part run from b757 records, from the cadence's decision to its exercise bank, the files it
opened for reading (outside the Python installation) and the git reads it made of a repository at a revision its hash does not fix -- a blob
at a named revision (`HEAD:path`), a listing or history of the tracked set (ls-files, diff, log, ls-tree, show, status and the like) -- and
its exercise bank carries them with their state at the run's end: each file's size and sha256, each blob's id, each repository's tree id at
HEAD for its listings and its status digest for `status` and `ls-files`. A file is keyed by its root (the relay, PLACE-papers, the session
store, a kernel's clone by the kernel's name) and its path under it; a file under no root is keyed by its path's digest, cannot be read again,
and so counts as changed. A bare `rev-parse` of a ref and an ancestry read (`merge-base`) read no bank and are not recorded. A remote read is
the parts' that keep their place.

v1.38.27, (R378)(8) [K27], THE KIND OF AN ACT THAT WRITES LEAN AND NO PAPER, in force from b768 (the second price of (R377)(7)(d) as the root
printed it, data/b767_put_2.json, taken by the author's ratification of the clause). The act's kind is read from its (W) list
(data/<act>_wlist.json, its patterns): LEAN AND NO PAPER where a pattern names a kernel's files (a path under SIDE-<name>/) and no pattern
reaches a path under day1/, phase1.5/, phase2/ or internal/ of PLACE-papers, by a name under one of them or as a glob that matches one;
PAPER otherwise, a list not read among them. At LEAN AND NO PAPER the act-root chain's four parts, standing-b2a to standing-b2d, which
recompute b624 to b658 from those acts' own banks, are not run in any mode of the suite (prerun, prev, post-push, pre-push, mid and rerun),
each writing its banks under the mode's own names with no arm run; standing-b3's group after the push is itself alone; and standing-b3 runs
its own half, b659 to the act, with the boundary's two lines of data/act_roots.txt read as before (tools/standing/fold/checks.tpl). The
prev-mode dry and the lock gate's read of it hold the four likewise (tools/standing/prevdry.py). The four run again at the next act of the
other kind.

v1.38.29, (R379)(8) [K29], THE KIND OF AN ACT THAT WRITES NO PAPER AND NO LEAN, in force from b769: where no pattern of the (W) list names a
kernel's files and none reaches a path under day1/, phase1.5/, phase2/ or internal/ of PLACE-papers, the kind is NO PAPER AND NO LEAN (an
act before b769 reads PAPER there, as [K27] read it). At it the four parts are held in each mode as at LEAN AND NO PAPER (HOLD_KINDS, the
kinds at which they are held), standing-b3's group after the push is itself alone, and G-ACTROOT-VERIFY reads standing-b3's own half and the
boundary's two lines of data/act_roots.txt as [K27] was repaired to read them at b768 (relay 690c4238). From b769 the kind's dict carries
the rule that gives the kind ([K27]'s for LEAN AND NO PAPER, [K29]'s for the others) and the version that read it, and a held part's banks
name both. The four run again at the next act that writes a paper.

  python -X utf8 -u tools/standing/cadence.py show <act>     (prints the act's kind and each part's decision in each held mode; writes nothing)
"""
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
import time

NL = '\n'
VERSION = 'v1.34.9'
FROM_ACT = 757
RULE = 'relay data/b754_rules.txt (10)'
FIT = 'relay data/b754_agenda.txt :358-:380'
KEEP = {'prerun': ('act', 'standing-a1', 'standing-a2'),
        'prev': ('act', 'standing-a1', 'standing-a2'),
        'post-push': ('act', 'standing-a1', 'standing-a2', 'standing-b2a')}
JOINED = ('standing-a1',)   # ### beside the fit: standing-a2's half bank, at the same HEAD
CHAIN_GROUP = ('standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3')
HELD_MODES = ('prerun', 'prev', 'post-push')
HEX = re.compile(r'^[0-9a-fA-F]{7,40}$')
NAMED = re.compile(r'^([^:\s-][^:\s]*):(.+)$')
LISTING = ('ls-files', 'diff', 'log', 'ls-tree', 'status', 'show', 'grep', 'blame', 'rev-list', 'whatchanged', 'cat-file', 'diff-tree',
           'diff-index', 'diff-files', 'shortlog', 'name-rev', 'describe')
STATUS_KINDS = ('status', 'ls-files', 'diff-files', 'diff-index')
# ### v1.38.27, (R378)(8) [K27]: THE KIND OF AN ACT THAT WRITES LEAN AND NO PAPER
KIND_FROM = 768
KIND_VERSION = 'v1.38.27'
KIND_RULE = '(R378)(8) [K27]'
LEAN_ONLY, PAPER = 'LEAN AND NO PAPER', 'PAPER'
# ### v1.38.29, (R379)(8) [K29]: THE KIND OF AN ACT THAT WRITES NO PAPER AND NO LEAN
NEITHER_FROM = 769
NEITHER_VERSION = 'v1.38.29'
NEITHER_RULE = '(R379)(8) [K29]'
NEITHER = 'NO PAPER AND NO LEAN'
HOLD_KINDS = (LEAN_ONLY, NEITHER)   # ### the kinds at which the act-root chain's four parts are held
CHAIN_QUARTERS = ('standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d')
PAPER_DIRS = ('day1/', 'phase1.5/', 'phase2/', 'internal/')
KERNEL_PATTERN = re.compile(r'^SIDE-[A-Za-z0-9-]+/')
RELAY_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUITE_LABEL = {'prerun': 'PRE-SEAL (R202)(3)', 'post-push': 'POST-PUSH', 'pre-push': 'PRE-PUSH', 'mid': 'MID-ACT', 'rerun': 'POST-PUSH'}


def in_force(act):
    try:
        return int(str(act).lstrip('b')) >= FROM_ACT
    except ValueError:
        return False


def mode_of(prev, prerun, mid, probe, rerun, pushed):
    """the cadence's mode of a part run, from the suite's flags: prev, prerun, mid (a probe too), rerun, post-push or pre-push."""
    if prev:
        return 'prev'
    if prerun:
        return 'prerun'
    if mid or probe:
        return 'mid'
    if rerun:
        return 'rerun'
    return 'post-push' if pushed else 'pre-push'


def prev_act(act):
    return 'b%d' % (int(str(act).lstrip('b')) - 1)


def _git(root, *a):
    r = subprocess.run(['git', '-C', root] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').strip() if r.returncode == 0 else None


def _blob(root, rev, path):
    r = subprocess.run(['git', '-C', root, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '') if r.returncode == 0 else None


def sitting(root, act):
    """True or False from the act's ferry title (its ACT line before the first colon carrying the word SITTING); None where the ferry or its
    ACT line is not read."""
    p = os.path.join(root, 'data', '%s_ferry.txt' % act)
    try:
        with open(p, encoding='utf-8') as fh:
            for line in fh:
                if line.startswith('ACT %s ' % act):
                    return bool(re.search(r'\bSITTING\b', line.split(':')[0]))
    except OSError:
        return None
    return None


# ================================================================================ v1.38.27, (R378)(8) [K27]: THE KIND OF AN ACT
def kind_in_force(act):
    try:
        return int(str(act).lstrip('b')) >= KIND_FROM
    except ValueError:
        return False


def neither_in_force(act):
    """v1.38.29, (R379)(8) [K29]: True from b769, where the kind NO PAPER AND NO LEAN is read."""
    try:
        return int(str(act).lstrip('b')) >= NEITHER_FROM
    except ValueError:
        return False


def wlist_patterns(root, act):
    """the act's (W) patterns from data/<act>_wlist.json, or None where the list is not read."""
    try:
        with open(os.path.join(root, 'data', '%s_wlist.json' % act), encoding='utf-8') as fh:
            p = json.load(fh).get('patterns')
        return list(p) if isinstance(p, list) else None
    except (OSError, ValueError, AttributeError):
        return None


def kind_from_patterns(patterns, neither=False):
    """(kind, why) from (W) patterns: LEAN AND NO PAPER where a pattern names a kernel's files and none reaches a path under day1/, phase1.5/,
    phase2/ or internal/ of PLACE-papers (a name under one of them, or a glob matching one); PAPER otherwise, a list not read among them.
    v1.38.29, (R379)(8) [K29]: with `neither` (an act from b769), NO PAPER AND NO LEAN where no pattern names a kernel's files and none
    reaches such a path, an empty list among them."""
    if patterns is None:
        return PAPER, 'the (W) list not read: an act of the other kind, the four parts required'
    kern = [x for x in patterns if KERNEL_PATTERN.match(x)]
    paper = [x for x in patterns if any(x.startswith('PLACE-papers/' + d) or fnmatch.fnmatchcase('PLACE-papers/%sx.md' % d, x) for d in PAPER_DIRS)]
    if paper:
        return PAPER, 'the (W) list reaches a paper`s path (%s)' % ', '.join(paper[:3])
    if not kern:
        if neither:   # ### v1.38.29 [K29]
            return NEITHER, 'the (W) list names no kernel`s files and no path under %s of PLACE-papers (%d patterns)' % (', '.join(PAPER_DIRS), len(patterns))
        return PAPER, 'the (W) list names no kernel`s files'
    return LEAN_ONLY, 'the (W) list names a kernel`s files (%d patterns) and no path under %s of PLACE-papers' % (len(kern), ', '.join(PAPER_DIRS))


def kind_of(act, root=None, patterns=None):
    """dict(kind, why, version, rule): [K27]'s kind of an act, in force from b768, every act before it of the other kind; `patterns` read in
    place of the act's (W) list (a planted list). v1.38.29, (R379)(8) [K29]: from b769 the kind NO PAPER AND NO LEAN beside the two, the
    dict's version [K29]'s and its rule the one that gives the kind, [K27]'s for LEAN AND NO PAPER and [K29]'s for the others."""
    d = dict(version=KIND_VERSION, rule=KIND_RULE)
    if not kind_in_force(act):
        return dict(d, kind=PAPER, why='the kind is in force from b%d' % KIND_FROM)
    nf = neither_in_force(act)
    k, why = kind_from_patterns(wlist_patterns(root or RELAY_ROOT, act) if patterns is None else patterns, neither=nf)
    if nf:
        d = dict(version=NEITHER_VERSION, rule=KIND_RULE if k == LEAN_ONLY else NEITHER_RULE)
    return dict(d, kind=k, why=why)


def chain_quarters_run(act, root=None, kind=None):
    """True where the act-root chain's four parts, standing-b2a to standing-b2d, run (an act that writes a paper); False at LEAN AND NO
    PAPER and, v1.38.29 [K29], at NO PAPER AND NO LEAN (HOLD_KINDS), where standing-b3 joins no half bank of theirs and G-ACTROOT-VERIFY
    reads standing-b3's half and the boundary."""
    return (kind or kind_of(act, root))['kind'] not in HOLD_KINDS


# ================================================================================ the bank names, as the suite's writer composes them
def text_name(act, mode, part):
    base = {'prerun': '%s_arms_prerun.txt', 'prev': '%s_prevrun.txt', 'pre-push': '%s_checks.txt', 'post-push': '%s_checks_postpush.txt'}[mode] % act
    return base.replace('.txt', '_%s.txt' % part)


def lsr_of(act, tn):
    """the remote reads' bank of a part bank named tn, as the suite's writer derives it (v1.38.27: from the name the suite gives)."""
    return tn.replace('%s_arms_prerun' % act, '%s_lsr_prerun' % act).replace('%s_checks' % act, '%s_lsr' % act).replace('.txt', '.json')


def lsr_name(act, mode, part):
    return lsr_of(act, text_name(act, mode, part))


def exercise_name(act, part, mode, tracked):
    from standing import repeat as RP
    return RP.exercise_name(act, part, mode, tracked)


# ================================================================================ THE READ RECORD
def roots(relay, pp, proj):
    """the named roots a read is keyed by: the relay, PLACE-papers, the session store."""
    return dict((k, v) for k, v in (('relay', relay), ('pp', pp), ('proj', proj)) if v)


_KERNEL = re.compile(r'^([A-Za-z]:)[\\/](SIDE-[A-Za-z0-9-]+)[\\/](.+)$')


def key_of(path, rts):
    """(key, rel) for an absolute path: a named root and the path under it, a kernel's clone (D:/SIDE-x) and the path under it, or
    ('other', the path's digest)."""
    ap = os.path.abspath(path)
    nc = os.path.normcase(ap)
    for k, r in rts.items():
        rr = os.path.normcase(os.path.abspath(r))
        if nc.startswith(rr + os.sep):
            return k, ap[len(rr) + 1:].replace('\\', '/')
    m = _KERNEL.match(ap)
    if m:
        return '%s/%s' % (m.group(1).upper(), m.group(2)), m.group(3).replace('\\', '/')
    return 'other', hashlib.sha256(nc.encode('utf-8')).hexdigest()[:16]


def path_of(key, rel, rts):
    if key == 'other':
        return None
    if key in rts:
        return os.path.join(rts[key], *rel.split('/'))
    return os.path.join(key + '/', *rel.split('/'))


def file_state(p):
    if p is None:
        return 'UNREADABLE'
    try:
        h, n = hashlib.sha256(), 0
        with open(p, 'rb') as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b''):
                h.update(chunk)
                n += len(chunk)
        return '%d:%s' % (n, h.hexdigest())
    except OSError:
        return 'ABSENT'


def list_state(root, kind):
    if kind == 'status':
        s = _git(root, 'status', '--porcelain', '--untracked-files=no')
        return 'status:%s' % (hashlib.sha256((s or '').encode('utf-8')).hexdigest() if s is not None else 'UNREAD')
    return 'tree:%s' % (_git(root, 'rev-parse', 'HEAD^{tree}') or 'UNREAD')


def split_cmdline(s):
    """the arguments of a Windows command line as subprocess.list2cmdline joins them: white space outside double quotes separates; a
    double quote opens or closes a quoted span; backslashes before a double quote halve, an odd one escaping the quote; others are literal."""
    out, cur, i, q, have = [], [], 0, False, False
    while i < len(s):
        c = s[i]
        if c == '\\':
            j = i
            while j < len(s) and s[j] == '\\':
                j += 1
            nb = j - i
            if j < len(s) and s[j] == '"':
                cur.append('\\' * (nb // 2))
                if nb % 2:
                    cur.append('"')
                    i = j + 1
                else:
                    i = j
                have = True
                continue
            cur.append('\\' * nb)
            i, have = j, True
            continue
        if c == '"':
            q, have, i = not q, True, i + 1
            continue
        if c in ' \t' and not q:
            if have:
                out.append(''.join(cur))
                cur, have = [], False
            i += 1
            continue
        cur.append(c)
        i, have = i + 1, True
    if have:
        out.append(''.join(cur))
    return out


class Reads(object):
    """the reads of one part run: files opened for reading and git reads at a named revision, keyed by root; started at the cadence's
    decision and read (and stopped) at the exercise bank."""

    def __init__(self, rts):
        self.rts = dict(rts)
        skip = set()
        for x in (sys.prefix, sys.base_prefix, sys.exec_prefix, getattr(sys, 'base_exec_prefix', None)):
            if x:
                skip.add(os.path.normcase(os.path.abspath(x)))
        try:
            import site
            u = site.getusersitepackages()
            if u:
                skip.add(os.path.normcase(os.path.abspath(u)))
        except Exception:   # noqa: BLE001
            pass
        self.skip = tuple(sorted(skip))
        self.files, self.blobs, self.listings = set(), set(), set()
        self.on, self.hooked = False, False

    def start(self):
        if not self.hooked:
            sys.addaudithook(self._hook)
            self.hooked = True
        self.on = True
        return self

    def _hook(self, ev, args):
        if not self.on:
            return
        try:
            if ev == 'open':
                self._open(args)
            elif ev == 'subprocess.Popen':
                self._popen(args)
        except Exception:   # noqa: BLE001  ### the record never stops the part
            pass

    def _open(self, args):
        path, mode, flags = (list(args) + [None, None, None])[:3]
        if path is None or isinstance(path, int):
            return
        if isinstance(mode, str):
            if any(c in mode for c in 'wax+'):
                return
        elif isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT):
            return
        p = os.fsdecode(os.fspath(path))
        nc = os.path.normcase(os.path.abspath(p))
        if any(nc.startswith(s + os.sep) for s in self.skip):
            return
        k, rel = key_of(p, self.rts)
        if k == 'relay' and rel.startswith('.git/'):
            return
        self.files.add((k, rel))

    def _popen(self, args):
        argv, cwd = (list(args) + [None, None, None])[1:3]
        if not argv:
            return
        if isinstance(argv, (str, bytes)):   # ### on Windows the event carries the command line subprocess.list2cmdline joined
            a = split_cmdline(os.fsdecode(argv) if isinstance(argv, bytes) else argv)
        else:
            a = [os.fsdecode(x) if isinstance(x, bytes) else str(x) for x in argv]
        if not a:
            return
        if not os.path.basename(a[0]).lower().startswith('git'):
            return
        repo, i = (os.fsdecode(cwd) if cwd else os.getcwd()), 1
        while i < len(a) and a[i].startswith('-'):
            if a[i] in ('-C', '-c') and i + 1 < len(a):
                repo = a[i + 1] if a[i] == '-C' else repo
                i += 2
                continue
            i += 1
        if i >= len(a):
            return
        sub, rest = a[i], a[i + 1:]
        key = next((k for k, r in self.rts.items() if os.path.normcase(os.path.abspath(repo)) == os.path.normcase(os.path.abspath(r))), None)
        if key is None:
            return
        named = [x for x in rest if NAMED.match(x) and not x.startswith('-')]
        for x in named:
            rev, path = x.split(':', 1)
            if not HEX.match(rev):
                self.blobs.add((key, rev, path))
        if sub in ('rev-parse', 'merge-base') or sub not in LISTING:
            return
        if sub in STATUS_KINDS:
            self.listings.add((key, 'status'))
            if sub == 'status':
                return
        cut = rest.index('--') if '--' in rest else len(rest)
        revs = [x for x in rest[:cut] if not x.startswith('-') and not NAMED.match(x)]
        if named and not revs:
            return
        if revs and all(HEX.match(x) for x in revs):
            return
        self.listings.add((key, 'tree'))

    def state(self):
        was, self.on = self.on, False
        try:
            files = dict(('%s|%s' % kr, file_state(path_of(kr[0], kr[1], self.rts))) for kr in sorted(self.files))
            blobs = dict(('%s|%s:%s' % b, _git(self.rts[b[0]], 'rev-parse', '--verify', '-q', '%s:%s' % (b[1], b[2])) or 'ABSENT')
                         for b in sorted(self.blobs))
            lists = dict(('%s|%s' % lk, list_state(self.rts[lk[0]], lk[1])) for lk in sorted(self.listings))
            return dict(files=files, blobs=blobs, listings=lists)
        finally:
            self.on = was

    def stop(self):
        self.on = False


def changed(rec, rts):
    """[(kind, key, then, now)] for every read of a record whose state differs now (the first 40 printed by the caller)."""
    out = []
    for k, then in sorted((rec.get('files') or {}).items()):
        key, rel = k.split('|', 1)
        now = file_state(path_of(key, rel, rts))
        if now != then or then in ('UNREADABLE',):
            out.append(('file', k, then, now))
    for k, then in sorted((rec.get('blobs') or {}).items()):
        key, rb = k.split('|', 1)
        rev, path = rb.split(':', 1)
        now = _git(rts[key], 'rev-parse', '--verify', '-q', '%s:%s' % (rev, path)) or 'ABSENT' if key in rts else 'UNREADABLE'
        if now != then:
            out.append(('blob', k, then, now))
    for k, then in sorted((rec.get('listings') or {}).items()):
        key, kind = k.split('|', 1)
        now = list_state(rts[key], kind) if key in rts else 'UNREADABLE'
        if now != then:
            out.append(('listing', k, then, now))
    return out


# ================================================================================ THE DECISION
def _jload(t):
    try:
        return json.loads(t) if t else {}
    except ValueError:
        return {}


def prerun_source(root, act, part, tracked_at=None):
    """the last pre-run bank of `part`: the previous act's, read at the commit that added its part bank; (dict or None, why)."""
    pa = prev_act(act)
    tn = 'data/%s' % text_name(pa, 'prerun', part)
    c = _git(root, 'log', '--diff-filter=A', '--format=%H', '-1', '--', tn)
    if not c:
        return None, 'no pre-run bank of %s at %s committed (%s)' % (part, pa, tn)
    text = _blob(root, c, tn)
    exn = None
    for n in ('data/%s_exercise_%s_%s.json' % (pa, part, pa), 'data/%s_exercise_%s.json' % (pa, part)):
        j = _jload(_blob(root, c, n))
        if j:
            exn = (n, j)
            break
    if text is None or exn is None:
        return None, 'the pre-run banks of %s at %s not read at relay %s' % (part, pa, c[:8])
    if exn[1].get('mode') != 'prerun' or exn[1].get('part') != part:
        return None, 'relay %s:%s holds mode %s part %s, not a pre-run of %s' % (c[:8], exn[0], exn[1].get('mode'), exn[1].get('part'), part)
    cad = exn[1].get('cadence') or {}
    run_head = cad.get('run_head') or exn[1].get('relay_head')
    return dict(text=text, ex=exn[1], text_name=tn, ex_name=exn[0], commit=c, run_head=run_head, act=pa), None


def standing_moved(root, run_head):
    then = _git(root, 'rev-parse', '%s:tools/standing' % run_head) if run_head else None
    now = _git(root, 'rev-parse', 'HEAD:tools/standing')
    dirty = _git(root, 'diff', '--name-only', 'HEAD', '--', 'tools/standing')
    moved = then is None or now is None or then != now or bool(dirty)
    return moved, dict(then=then, now=now, dirty=(dirty or '').split(NL) if dirty else [])


def prepush_source(root, act, part):
    """this act's pre-push banks of `part` (the working tree): (dict or None, why)."""
    tn, en = text_name(act, 'pre-push', part), '%s_exercise_%s.json' % (act, part)
    try:
        text = open(os.path.join(root, 'data', tn), encoding='utf-8').read()
        ex = json.load(open(os.path.join(root, 'data', en), encoding='utf-8'))
    except (OSError, ValueError):
        return None, 'the pre-push banks of %s not read (data/%s, data/%s)' % (part, tn, en)
    return dict(text=text, ex=ex, text_name='data/' + tn, ex_name='data/' + en, commit=None, run_head=ex.get('relay_head'), act=act), None


def _post_state(root, act, part, rts):
    """one part's standing in the pass after the push: ('read', src, why) | ('run', None, why) | ('ran', None, why) | ('copied', None, why)."""
    try:
        ex = json.load(open(os.path.join(root, 'data', '%s_exercise_%s.json' % (act, part)), encoding='utf-8'))
    except (OSError, ValueError):
        return 'run', None, 'no exercise bank of %s' % part
    if ex.get('mode') == 'post-push':
        return ('copied', None, '%s read from its pre-push bank already' % part) if (ex.get('cadence') or {}).get('held') == 'read' else \
            ('ran', None, '%s run after the push already' % part)
    if ex.get('mode') != 'pre-push':
        return 'run', None, 'the exercise bank of %s holds mode %s, not pre-push' % (part, ex.get('mode'))
    rec = (ex.get('cadence') or {}).get('reads')
    if not rec:
        return 'run', None, 'the pre-push run of %s left no read record' % part
    ch = changed(rec, rts)
    if ch:
        return 'run', None, '%d read(s) of %s changed since its pre-push run: %s' % (len(ch), part, '; '.join('%s %s' % (k, n) for k, n, _a, _b in ch[:3]))
    src, why = prepush_source(root, act, part)
    if src is None:
        return 'run', None, why
    return 'read', src, 'no read of %s changed since its pre-push run (%d files, %d blobs, %d listings)' % (
        part, len(rec.get('files') or {}), len(rec.get('blobs') or {}), len(rec.get('listings') or {}))


def decide(act, part, mode, root, rts, kind=None):
    """dict(run, held, mode, part, why, source): the cadence's decision for one part run. Not in force before b757. v1.38.27, (R378)(8)
    [K27]: at an act of the kind LEAN AND NO PAPER (from b768) standing-b2a to standing-b2d are not run in any mode and standing-b3's group
    after the push is itself alone; `kind` read in place of the act's own (a planted kind, kind_of's dict). v1.38.29, (R379)(8) [K29]: the
    same at NO PAPER AND NO LEAN (from b769), the decision naming the kind's own rule and version."""
    d = dict(run=True, held='run', mode=mode, part=part, why='', source=None, version=VERSION, rule=RULE, fit=FIT)
    if not in_force(act):
        d['why'] = 'the cadence is in force from b%d' % FROM_ACT
        return d
    lean = False
    if part in CHAIN_QUARTERS or part in CHAIN_GROUP:
        kd = kind or kind_of(act, root)
        lean = kd['kind'] in HOLD_KINDS   # ### v1.38.29 [K29]: NO PAPER AND NO LEAN held as LEAN AND NO PAPER
        if lean and part in CHAIN_QUARTERS:
            kr = kd.get('rule') or KIND_RULE
            d.update(run=False, held='not run', kind=kd['kind'], kind_rule=kr, kind_version=kd.get('version') or KIND_VERSION,
                     why='%s, the act writes %s (%s): the act-root chain`s four parts, standing-b2a to standing-b2d, not run in the '
                         'mode %s; standing-b3 runs its own half with the boundary`s two lines read as before' % (
                             kr, 'Lean and no paper' if kd['kind'] == LEAN_ONLY else 'no paper and no Lean', kd['why'], mode))
            return d
    if mode not in HELD_MODES:
        d['why'] = 'every part runs in the mode %s' % mode
        return d
    if part in KEEP[mode]:
        d['why'] = '%s keeps its place in the mode %s (%s%s)' % (part, mode, FIT, '; joined beside the fit: standing-a2 joins its half bank at the same HEAD' if part in JOINED else '')
        return d
    if mode == 'prerun':
        src, why = prerun_source(root, act, part)
        if src is None:
            d['why'] = why
            return d
        moved, st = standing_moved(root, src['run_head'])
        if moved:
            d['why'] = 'tools/standing/ moved since the run %s repeats (relay %s): tree %s then, %s now%s' % (
                src['text_name'], (src['run_head'] or '-')[:8], (st['then'] or '-')[:12], (st['now'] or '-')[:12],
                ' ; tracked changes %s' % st['dirty'] if st['dirty'] else '')
            return d
        d.update(run=False, held='read', source=src, why='tools/standing/ unmoved since the run %s repeats (relay %s): tree %s at both, no tracked change' % (
            src['text_name'], (src['run_head'] or '-')[:8], (st['now'] or '-')[:12]))
        return d
    if mode == 'prev':
        s = sitting(root, act)
        if s is None or s:
            d['why'] = 'a sitting (data/%s_ferry.txt%s)' % (act, ' not read, counted a sitting' if s is None else ': its title carries SITTING')
            return d
        d.update(run=False, held='not run', why='not a sitting (data/%s_ferry.txt: its title carries no SITTING): the pass in the previous act`s mode '
                                                'held to the parts that keep their place' % act)
        return d
    group = CHAIN_GROUP if (part in CHAIN_GROUP and not lean) else (part,)   # ### v1.38.27 [K27]: standing-b3 alone at LEAN AND NO PAPER; v1.38.29 [K29] at NO PAPER AND NO LEAN
    states = [(p, _post_state(root, act, p, rts)) for p in group]
    mine = dict(states)[part]
    if any(s[0] in ('run', 'ran') for _p, s in states):
        d['why'] = '; '.join(s[2] for _p, s in states if s[0] in ('run', 'ran')) + ('' if group == (part,) else ' (the chain parts run together)')
        return d
    if mine[0] != 'read':
        d['why'] = mine[2]
        return d
    d.update(run=False, held='read', source=mine[1], why=mine[2] + ('' if group == (part,) else ' ; the chain parts read together, none changed'))
    return d


# ================================================================================ THE BANKS OF A HELD PART
LABEL = {'prerun': 'PRE-SEAL (R202)(3)', 'post-push': 'POST-PUSH'}


def _put(p, b, membrane):
    if membrane:
        membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def _footer_now(text, secs):
    """the source's lines with its part footer's seconds set to this read's; (lines, the source's seconds) or (None, None) with no footer."""
    from standing import close as STC
    m = STC.PART_FOOT.search(text)
    if not m:
        return None, None
    t = text[:m.start(10)] + str(int(secs)) + text[m.end(10):]
    return t.rstrip(NL).split(NL), int(m.group(10))


def held(d, act, root, d_dir, rc_key=None, membrane=None, t0=None, out=print, carried=(), text=None, ex_mode=None):
    """write a held part's banks under the mode's names; returns the exit code the part's run would return on the source's verdicts (0
    clean; 4 where every live failure is a carried failure declared on the face and no control misbehaves; else 1). v1.38.27, (R378)(8)
    [K27]: `text`, the part bank's name as the suite composes it (_part_name of its base: every mode's, mid and rerun among them), and
    `ex_mode`, the exercise bank's mode as the suite writes it; a part not run writes its exercise bank in that mode (prev where not given in
    the prev mode, as before)."""
    if d.get('run') or d.get('held') not in ('read', 'not run') or (d['held'] == 'read' and not d.get('source')):
        raise SystemExit('### THE CADENCE: held() CALLED WITH A DECISION THAT RUNS THE PART (%s, %s) -- NOTHING WRITTEN' % (d.get('held'), d.get('why')))
    t0 = t0 or time.time()
    part, mode = d['part'], d['mode']
    now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    head = _git(root, 'rev-parse', 'HEAD')
    tracked = lambda n: bool(_git(root, 'ls-files', 'data/' + n))   # noqa: E731
    from standing import lsrread as LSRD
    lsv = LSRD.verdict({}, {})
    bar = '=' * 104
    src = d.get('source') or {}
    cad = dict(version=VERSION, rule=RULE, fit=FIT, held=d['held'], why=d['why'], at=now)
    if d.get('kind'):
        cad.update(kind=d['kind'], kind_rule=d.get('kind_rule'), kind_version=d.get('kind_version') or KIND_VERSION)   # ### v1.38.29 [K29]: the kind's own
    tn = text or text_name(act, mode, part)
    if d['held'] == 'read':
        secs = time.time() - t0
        lines, src_secs = _footer_now(src['text'], secs)
        if lines is None:
            raise SystemExit('### THE CADENCE: THE SOURCE %s HAS NO PART FOOTER -- NOTHING WRITTEN; run the part with the cadence`s source repaired' % src['text_name'])
        cad.update(source=src['text_name'], source_exercise=src['ex_name'], source_commit=src.get('commit'), source_mode=src['ex'].get('mode'),
                   source_at=src['ex'].get('at'), source_head=src['ex'].get('relay_head'), run_head=src.get('run_head'), source_seconds=src_secs)
        L = [bar, '%s -- THE SUITE. ### **%s READING.** ### PART %s ### READ FROM A BANK BY THE CADENCE, NOT RUN (%s, tools/standing/cadence.py %s).' % (
                 act, LABEL[mode], part, RULE, VERSION),
             '### THE CADENCE: %s.' % d['why'],
             '### the source: relay %s%s (sha256 %s), its run at relay %s, %s s; its lines below whole, the footer`s seconds this read`s (%d s)' % (
                 src['text_name'], ' at %s' % src['commit'][:8] if src.get('commit') else ' (the working tree)',
                 hashlib.sha256(src['text'].encode('utf-8')).hexdigest()[:16], (src.get('run_head') or '-')[:8], src_secs, int(secs)),
             bar] + lines
        ex = dict(src['ex'])
        ex.pop('cadence', None)
        ex.update(part=part, mode=mode, at=now, relay_head=head, cadence=cad)
        lf, df, nf = list(ex.get('live_failing') or []), list(ex.get('defective') or []), int(ex.get('neg_failures') or 0)
        code = 0 if not (lf or df or nf) else (4 if (not df and nf == 0 and all(f in tuple(carried or ()) for f in lf)) else 1)
    else:
        secs = time.time() - t0
        if mode == 'prev':
            h1 = '%s -- THE SUITE. ### **ON %s`S BANKS.** ### PART %s ### NOT RUN BY THE CADENCE (%s, tools/standing/cadence.py %s).' % (
                act, prev_act(act), part, d.get('kind_rule') or RULE, (d.get('kind_version') or KIND_VERSION) if d.get('kind') else VERSION)
        else:   # ### v1.38.27 [K27]: a part not run outside the prev mode, its reading named as the suite names it
            h1 = '%s -- THE SUITE. ### **%s READING.** ### PART %s ### NOT RUN BY THE CADENCE (%s, tools/standing/cadence.py %s).' % (
                act, SUITE_LABEL.get(mode, mode.upper()), part, d.get('kind_rule') or RULE, (d.get('kind_version') or KIND_VERSION) if d.get('kind') else VERSION)
        L = [bar, h1, '### THE CADENCE: %s.' % d['why'], bar, '  (no arm run in this part at this act)', '',
             '  ### PART %s : ARMS 0 ; LIVE PASSING 0 ; LIVE FAILING 0 NONE ; NEGATIVE-CONTROL FAILURES 0 ; POSITIVE-CONTROL PASSES 0 NONE ; '
             'DECLARED EQ RUN NOTRUN ; %d s ; WITHHELD, NOT EXERCISABLE 0 NONE' % (part, int(secs)), bar]
        ex = dict(exercise={}, run=0, live_failing=[], defective=[], neg_failures=0, withheld=[], part=part,
                  mode=ex_mode or {'rerun': 'post-push'}.get(mode, mode), at=now, relay_head=head,
                  pass_on_prev=[], fail_as_prev=[], diverge=[], not_run_by_prev=[], cadence=cad)
        code = 0
    _put(os.path.join(d_dir, tn), (NL.join(L) + NL).encode('utf-8'), membrane)
    ln = lsr_of(act, tn)
    _put(os.path.join(d_dir, ln), (json.dumps(dict(run=tn, lsr={}, key=rc_key, times={}, classed=lsv[0], events=lsv[1], cadence=cad),
                                              indent=1, ensure_ascii=False) + NL).encode('utf-8'), membrane)
    en = exercise_name(act, part, ex['mode'], tracked)
    _put(os.path.join(d_dir, en), (json.dumps(ex, indent=1, ensure_ascii=False) + NL).encode('utf-8'), membrane)
    written = [tn, ln, en]
    if mode == 'prerun':
        arms = sorted((src.get('ex') or {}).get('exercise') or {})
        sp = '%s_arm_seconds_%s.json' % (act, part)
        try:
            src_secs_bank = _jload(_blob(root, src['commit'], 'data/%s_arm_seconds_%s.json' % (src['act'], part))) if src.get('commit') else {}
        except Exception:   # noqa: BLE001
            src_secs_bank = {}
        _put(os.path.join(d_dir, sp), (json.dumps(dict(at=now, part=part, arms=dict((n, 0.0) for n in arms), phases={}, run_secs=int(secs),
                                                       cadence=dict(cad, source_arms=src_secs_bank.get('arms') or {},
                                                                    source_run_secs=src_secs_bank.get('run_secs'))),
                                                  indent=1, ensure_ascii=False) + NL).encode('utf-8'), membrane)
        written.append(sp)
    out('### THE CADENCE (%s, %s): PART %s %s IN THE MODE %s -- %s' % (RULE, VERSION, part, 'READ FROM A BANK' if d['held'] == 'read' else 'NOT RUN', mode, d['why']))
    out('  written: %s' % ', '.join(written))
    return code


def run_fields(d, reads):
    """the exercise bank's field for a part that ran, from b757 (`reads` None before): the decision and the read record."""
    if d is None or reads is None:
        return {}
    c = dict(version=VERSION, held='run', why=d.get('why'), mode=d.get('mode'))
    if reads is not None:
        c['reads'] = reads.state()
        reads.stop()
    return dict(cadence=c)


def show(act, root, rts):
    from importlib import import_module
    parts = import_module('%s_worklist' % act).PARTS
    k = kind_of(act, root)
    print('  THE KIND (%s, %s): %s -- %s' % (k['rule'], k['version'], k['kind'], k['why']))
    for mode in HELD_MODES:
        for p in parts:
            d = decide(act, p, mode, root, rts)
            print('  %-9s %-13s %-8s %s' % (mode, p, d['held'].upper(), d['why'][:200]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'show':
        R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        sys.path.insert(0, os.path.join(R, 'tools'))
        show(sys.argv[2], R, roots(R, None, None))
    else:
        sys.exit(__doc__)
