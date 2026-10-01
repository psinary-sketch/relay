# -*- coding: utf-8 -*-
"""asof.py -- THE SUITE'S AS-OF COMMIT, (R178)(2)(ii), written at b568.

### ### **THE RULING.** *A sealed face is a statement about the tree at its closing push. The suite gains an as-of commit:
### each arm that reads the relay tree reads it at the commit named in the face's closing push-out bank, not at HEAD.*
### ### **THE OCCASION.** b566's suite, re-run after b567 closed, failed G-NUMBER-UNCLAIMED (it globbed the live data
### directory for a successor's registration) and, after b567's appended lines, G-PRIORBANK-UNCHANGED (it compared the
### live prior banks with origin/main): each compared a sealed face against the tree as it stands.
### ### **WHAT THIS MODULE GIVES A SUITE.** `relay_asof(root, data, act)`: the relay commit a face's closing push-out bank
### names -- the `tip` of the `push_gated: repo ...` line, accepted only when the bank's `main read back at the remote`
### line names the same SHA and the commit exists locally; `None` when the bank is absent (the act's own closing run, before
### its push) or does not read back equal, and the suite then reads live, as before. `names_at`, `blob_at` and `ids_at`
### read the tree at that commit. `from_argv` lets a test point a suite at another commit (`--as-of <sha>`), which is how
### the test shows a claim false at a commit still fails. ### **SCOPE, AS THE FERRY GIVES IT: THE TREE-READING ARMS.** An
### arm that reads a named bank's content (an addendum line a later ruling appended) is not re-pointed by this module.
"""
import os
import re
import subprocess

TIP = re.compile(r'^push_gated: repo .* ; branch (\S+) ; tip ([0-9a-f]{40}) ;', re.M)
BACK = re.compile(r'^push_gated: main read back at the remote: ([0-9a-f]{40})\s*$', re.M)


def _git(root, *a):
    r = subprocess.run(['git', '-C', root] + list(a), capture_output=True)
    return r.returncode, r.stdout


def parse_pushout(text):
    """### RETURN the SHA when the bank's tip and its read-back agree, else None."""
    t, b = TIP.findall(text or ''), BACK.findall(text or '')
    if len(t) == 1 and len(b) == 1 and t[0][1] == b[0]:
        return b[0]
    return None


def relay_asof(root, data, act):
    p = os.path.join(data, '%s_closing_push_out.txt' % act)
    if not os.path.isfile(p):
        return None
    sha = parse_pushout(open(p, 'rb').read().decode('utf-8', 'replace').replace('\r', ''))
    if sha and _git(root, 'cat-file', '-e', sha + '^{commit}')[0] == 0:
        return sha
    return None


def from_argv(argv, default):
    """### `--as-of <sha>` on the command line, else the bank's commit."""
    if '--as-of' in argv:
        return argv[argv.index('--as-of') + 1]
    return default


def names_at(root, rev, prefix):
    """### the paths under `prefix` (a directory, no trailing slash) in the tree at `rev`, relative to it."""
    rc, out = _git(root, 'ls-tree', '-r', '--name-only', rev, '--', prefix + '/')
    if rc:
        return []
    n = len(prefix) + 1
    return [x[n:] for x in out.decode('utf-8', 'replace').split('\n') if x.strip()]


def blob_at(root, rev, path):
    rc, out = _git(root, 'show', '%s:%s' % (rev, path))
    return None if rc else out


def ids_at(root, rev, prefix):
    """### {path: blob id} under `prefix` at `rev`."""
    rc, out = _git(root, 'ls-tree', '-r', rev, '--', prefix + '/')
    res = {}
    if rc:
        return res
    for line in out.decode('utf-8', 'replace').split('\n'):
        if '\t' in line:
            meta, path = line.split('\t', 1)
            res[path] = meta.split()[2]
    return res


# ### ### **(R179)(3), b569: THE AS-OF COMMIT, EXTENDED TO EVERY REPOSITORY THE SUITE READS.** *The closing push-out bank
# ### gains one line per repository the suite reads -- its closing head, or "deleted at close" for a clone removed by ruling
# ### -- and every tree-reading arm reads each repository at the head its bank line names.* ### The line:
# ###     push_gated: as-of <repository> <40-hex sha>
# ###     push_gated: as-of <repository> deleted at close
# ### (anything after the head, from `###` on, is a source note and not read). `tools/asof_lines.py` appends the lines to an
# ### act's closing push-out bank after its closing push. For an act whose push-out bank was committed before the extension
# ### (b566, b567) the lines are in a COMPANION bank `data/bNNN_asof_<act>.txt` written by a later act, because a committed
# ### prior bank is not edited; `repo_asof` reads the act's own bank first and the newest companion only when the act's own
# ### bank carries no line. `--as-of-lines <file>` points a suite at another set of lines (the test's false-claim case).
ASOF_LINE = re.compile(r'^push_gated: as-of (\S+) (?:([0-9a-f]{40})|(deleted at close)|(present at close))(?:\s+###.*)?\s*$', re.M)
DELETED = 'DELETED AT CLOSE'
# ### b569's defect (d): a DIRECTORY that is not a repository (b567's old build tree, present at its close and deleted at
# ### b568 by (R178)(2)(iv)) has no head; its line reads `present at close`. A third form, routed to the author.
PRESENT = 'PRESENT AT CLOSE'


def parse_asof_lines(text):
    """### RETURN {repository: sha or DELETED}; a repository named twice is refused (None for the whole bank)."""
    out = {}
    for m in ASOF_LINE.finditer(text or ''):
        if m.group(1) in out:
            return None
        out[m.group(1)] = m.group(2) or (DELETED if m.group(3) else PRESENT)
    return out


def repo_asof(data, act):
    """### RETURN ({repository: head}, the bank read) -- the act's closing push-out bank's lines, else its newest companion."""
    p = os.path.join(data, '%s_closing_push_out.txt' % act)
    if os.path.isfile(p):
        r = parse_asof_lines(open(p, 'rb').read().decode('utf-8', 'replace').replace('\r', ''))
        if r:
            return r, os.path.basename(p)
    comps = sorted(f for f in os.listdir(data) if re.match(r'^b\d+_asof_%s\.txt$' % re.escape(act), f))
    if comps:
        r = parse_asof_lines(open(os.path.join(data, comps[-1]), 'rb').read().decode('utf-8', 'replace').replace('\r', ''))
        if r:
            return r, comps[-1]
    return {}, None


def repos_from_argv(argv, default):
    """### `--as-of-lines <file>` on the command line, else the bank's lines."""
    if '--as-of-lines' in argv:
        p = argv[argv.index('--as-of-lines') + 1]
        return (parse_asof_lines(open(p, 'rb').read().decode('utf-8', 'replace').replace('\r', '')) or {}), p
    return default


def head_of(lines, name, live):
    """### the head an arm reads a repository at: the line's sha, or `live` (a ref name) when no line names it."""
    v = lines.get(name)
    return v if v and v not in (DELETED, PRESENT) else live


def self_test():
    """### the parsers on synthetic banks, both polarities."""
    a, b = '1' * 40, '2' * 40
    ok = parse_pushout('push_gated: repo /d/relay ; branch push-x ; tip %s ; checkout before main\n'
                       'push_gated: main read back at the remote: %s\n' % (a, a)) == a
    ok = ok and parse_pushout('push_gated: repo /d/relay ; branch push-x ; tip %s ; checkout before main\n'
                              'push_gated: main read back at the remote: %s\n' % (a, b)) is None
    ok = ok and parse_pushout('push_gated: main read back at the remote: %s\n' % a) is None
    ok = ok and parse_pushout('') is None
    ok = ok and parse_asof_lines('push_gated: as-of PLACE-papers %s ### source x\npush_gated: as-of bulka deleted at close\n'
                                 % a) == {'PLACE-papers': a, 'bulka': DELETED}
    ok = ok and parse_asof_lines('push_gated: as-of P %s\npush_gated: as-of P %s\n' % (a, b)) is None
    ok = ok and parse_asof_lines('push_gated: as-of P %s\n' % a[:12]) == {}
    ok = ok and head_of({'P': a, 'C': DELETED}, 'P', 'main') == a and head_of({'C': DELETED}, 'C', 'main') == 'main'
    ok = ok and parse_asof_lines('push_gated: as-of T present at close\n') == {'T': PRESENT}
    return ok
