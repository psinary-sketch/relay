# -*- coding: utf-8 -*-
"""additive_shared.py -- SHARED DATA FILES ARE ADDITIVE, (R254)(2), written at b644.

### A data file named by more than one act's root (read from every data/<act>_act_root.json's items), and the two the ruling names
### (data/glossary.txt, data/act_roots.txt), is ADDITIVE from (R254): an entry is added or a dated line beneath it, no line edited or
### removed. `check` diffs each such file at a revision against its previous commit (the commit before the last one that touched it) and,
### with `worktree`, the working file against HEAD; a line of the older text that is removed or changed is a failure. Lines are compared
### whole after their line end is dropped (relay's `eol=lf` normalises commits; a working file written CRLF is read line by line).
### Usage: python tools/additive_shared.py [--worktree]   (exit 0 when every shared file is additive)
"""
import difflib
import glob
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
RULED = ('data/glossary.txt', 'data/act_roots.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True).stdout


def shared_files():
    """### the ruled two, and every data/ path named by more than one root's items, sorted."""
    seen = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', '*_act_root.json'))):
        try:
            items = json.load(io.open(f, encoding='utf-8')).get('items') or []
        except Exception:
            continue
        for it in items:
            p = it.split()[0]
            if p.startswith('data/'):
                seen[p] = seen.get(p, 0) + 1
    return sorted(set(RULED) | set(p for p, n in seen.items() if n > 1))


def lines(b):
    """### the text's lines, each line end dropped; a final line feed ends the last line and adds none."""
    if b is None:
        return None
    ls = [l.rstrip('\r') for l in b.decode('utf-8', 'replace').split(NL)]
    return ls[:-1] if ls and ls[-1] == '' else ls


def removed_or_changed(old, new):
    """### [(tag, old lines)] for every opcode of the line diff that removes or changes a line of the older text."""
    if old is None or new is None:
        return []
    sm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    return [(tag, old[i1:i2]) for tag, i1, i2, _j1, _j2 in sm.get_opcodes() if tag in ('delete', 'replace')]


def previous_pair(path, rev='HEAD'):
    """### (the last commit at `rev` that touched `path`, the one before it): the pair the arm diffs."""
    hs = g('log', '--format=%H', '-2', rev, '--', path).decode().split()
    return (hs[0] if hs else None), (hs[1] if len(hs) > 1 else None)


def blob(rev, path):
    r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def check(rev='HEAD', worktree=False, files=None):
    """### [(path, what was compared, [(tag, old lines)])] -- an empty list per file is ADDITIVE."""
    out = []
    for p in (files or shared_files()):
        last, before = previous_pair(p, rev)
        if last and before:
            out.append((p, '%s against %s' % (last[:12], before[:12]), removed_or_changed(lines(blob(before, p)), lines(blob(last, p)))))
        else:
            out.append((p, 'one commit or none (%s)' % ((last or 'none')[:12]), []))
        if worktree:
            fp = os.path.join(ROOT, *p.split('/'))
            wb = open(fp, 'rb').read() if os.path.exists(fp) else None
            out.append((p, 'the working file against %s' % rev, removed_or_changed(lines(blob(rev, p)), lines(wb))))
    return out


def main(argv):
    res = check(worktree='--worktree' in argv)
    bad = 0
    for p, how, rc in res:
        bad += bool(rc)
        print('  %-28s %-48s %s' % (p, how, 'ADDITIVE' if not rc else '### NOT ADDITIVE: ' + '; '.join(
            '%s %r' % (t, ls[:2]) for t, ls in rc)[:300]))
    print('### ### **SHARED FILES %d ; READS %d ; NOT ADDITIVE %d.**' % (len(set(p for p, _h, _r in res)), len(res), bad))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
