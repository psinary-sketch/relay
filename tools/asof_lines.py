# -*- coding: utf-8 -*-
"""asof_lines.py -- THE PER-REPOSITORY AS-OF LINES, (R179)(3), written at b569.

### ### **THE RULING.** *The closing push-out bank gains one line per repository the suite reads -- its closing head, or
### "deleted at close" for a clone removed by ruling -- and every tree-reading arm reads each repository at the head its
### bank line names.* ### This tool APPENDS those lines to a closing push-out bank, after the closing push:
###   python tools/asof_lines.py <bank> <name>=<path> ... [<name>=clone:<path>] ... [<name>=deleted:<path>] ...
### A repository (`<name>=<path>`) gets a line only when its local main equals its remote main read by `git ls-remote origin
### refs/heads/main` in this run; a clone (`clone:`) gets its HEAD; a deleted clone (`deleted:`) gets `deleted at close`
### only when the path is absent. Any repository that fails its test refuses the whole run: exit 3, NOTHING WRITTEN (the
### lines are composed first and appended in one write). A bank that already carries an as-of line is refused (exit 4).
### Line form and reader: relay tools/asof.py (ASOF_LINE, repo_asof).
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import asof as AF   # noqa: E402


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').strip()


def compose(specs):
    """### RETURN (lines, problems)."""
    lines, bad = [], []
    for spec in specs:
        name, _, path = spec.partition('=')
        if not name or not path:
            bad.append('%s: not <name>=<path>' % spec)
            continue
        if path.startswith('deleted:'):
            p = path[len('deleted:'):]
            if os.path.exists(p):
                bad.append('%s: %s is PRESENT, not deleted' % (name, p))
            else:
                lines.append('push_gated: as-of %s deleted at close   ### %s ABSENT' % (name, p))
        elif path.startswith('clone:'):
            p = path[len('clone:'):]
            rc, h = git(p, 'rev-parse', 'HEAD')
            if rc or len(h) != 40:
                bad.append('%s: no HEAD at %s' % (name, p))
            else:
                lines.append('push_gated: as-of %s %s   ### the clone %s, its HEAD' % (name, h, p))
        else:
            rc, h = git(path, 'rev-parse', 'refs/heads/main')
            rc2, ls = git(path, 'ls-remote', 'origin', 'refs/heads/main')
            r = ls.split()[0] if ls.split() else ''
            if rc or rc2 or len(h) != 40 or h != r:
                bad.append('%s: main %s, remote %s -- not equal' % (name, h[:12], r[:12]))
            else:
                lines.append('push_gated: as-of %s %s   ### main = remote main by ls-remote' % (name, h))
    return lines, bad


def main(argv):
    if len(argv) < 2:
        print('usage: asof_lines.py <bank> <name>=<path|clone:path|deleted:path> ...', file=sys.stderr)
        return 2
    bank, specs = argv[0], argv[1:]
    old = open(bank, 'rb').read().decode('utf-8', 'replace') if os.path.isfile(bank) else ''
    if AF.parse_asof_lines(old):
        print('asof_lines: REFUSED -- %s already carries as-of lines; NOTHING WRITTEN' % bank, file=sys.stderr)
        return 4
    lines, bad = compose(specs)
    for b in bad:
        print('asof_lines: REFUSED -- %s' % b, file=sys.stderr)
    if bad:
        print('asof_lines: NOTHING WRITTEN', file=sys.stderr)
        return 3
    if AF.parse_asof_lines('\n'.join(lines)) is None:
        print('asof_lines: REFUSED -- a repository named twice; NOTHING WRITTEN', file=sys.stderr)
        return 3
    sep = '' if (not old or old.endswith('\n')) else '\n'
    with open(bank, 'ab') as f:
        f.write((sep + '\n'.join(lines) + '\n').encode('utf-8'))
    for ln in lines:
        print(ln)
    print('asof_lines: %d line(s) appended to %s' % (len(lines), bank))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
