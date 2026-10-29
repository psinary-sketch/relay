# -*- coding: utf-8 -*-
"""standing/peek.py -- A PIPE-FREE READER ((R333)(2)(ii), v1.3.0): search, head, tail, count and list, each with no shell pipe and no
redirect. Every option is an argument; the source is a file, a directory, or the output of one command run without a shell (`--of`), so a
read that once needed `| head`, `| cut`, `| grep -c` or `> file` is one call. It reads and prints; it writes nothing.

  peek.py search <pattern> <path>... [-i] [--fixed] [--max N] [--cut W] [--lines A-B] [--of "<command>"]
        the lines matching a regular expression (or a fixed string), each "path:line: text"; a directory read through `git ls-files`
        where it is a repository's, else walked (.git, .lake, build, __pycache__ skipped)
  peek.py head <path> [N] [--cut W] [--bytes N] [--of "<command>"]       the first N lines (10), or the first N bytes
  peek.py tail <path> [N] [--cut W] [--of "<command>"]                    the last N lines (10)
  peek.py count <path>... [--pattern P] [-i] [--fixed] [--of "<command>"] the lines, or the lines matching P, per source and in all
  peek.py list <dir> [--glob G] [--sort name|time|size] [--max N] [--long]  the entries of one directory
`--of` runs its command split by shlex with no shell (no pipe, redirect or expansion can act), in the current directory, and reads its
stdout and stderr together as the source; the command's exit code is printed after.
"""
import fnmatch
import os
import re
import shlex
import subprocess
import sys
import time

NL = '\n'
SKIP = {'.git', '.lake', 'build', '__pycache__', 'node_modules'}
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def opts(argv):
    """(positional, options): an option a word opening '-'; -i and --fixed and --long are flags, the others take the next word."""
    flags = {'-i', '--fixed', '--long'}
    pos, o, i = [], {}, 0
    while i < len(argv):
        a = argv[i]
        if a in flags:
            o[a] = True
        elif a.startswith('-') and len(a) > 1 and not re.match(r'^-\d', a):
            if i + 1 >= len(argv):
                sys.exit('peek: %s takes a value' % a)
            o[a] = argv[i + 1]
            i += 1
        else:
            pos.append(a)
        i += 1
    return pos, o


def cut(s, o):
    w = o.get('--cut')
    return s[:int(w)] if w else s


def run_of(cmd):
    """the output of one command run with no shell, and its exit code."""
    argv = shlex.split(cmd, posix=True)
    r = subprocess.run(argv, capture_output=True)
    return (r.stdout + r.stderr).decode('utf-8', 'replace').replace('\r', ''), r.returncode


def read(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8', 'replace').replace('\r', '')


def tracked(d):
    r = subprocess.run(['git', '-C', d, 'ls-files', '-z'], capture_output=True)
    if r.returncode != 0:
        return None
    return [os.path.join(d, x) for x in r.stdout.decode('utf-8', 'replace').split('\0') if x]


def files_of(paths):
    out = []
    for p in paths:
        if os.path.isfile(p):
            out.append(p)
        elif os.path.isdir(p):
            t = tracked(p)
            if t is not None:
                out += [x for x in t if os.path.isfile(x)]
                continue
            for root, dirs, fs in os.walk(p):
                dirs[:] = sorted(x for x in dirs if x not in SKIP)
                out += [os.path.join(root, f) for f in sorted(fs)]
        else:
            print('peek: %s ABSENT' % p)
    return out


def sources(pos, o):
    """[(label, text)] -- the command's output where --of is given, else each file."""
    if '--of' in o:
        text, rc = run_of(o['--of'])
        return [('(of)', text)], rc
    return [(p, read(p)) for p in files_of(pos)], None


def matcher(pat, o):
    if pat is None:
        return None
    flags = re.I if o.get('-i') else 0
    return re.compile(re.escape(pat) if o.get('--fixed') else pat, flags)


def search(pos, o):
    if not pos:
        sys.exit('peek search: a pattern')
    rx, mx = matcher(pos[0], o), int(o.get('--max', 0) or 0)
    lo, hi = (int(x) for x in o['--lines'].split('-')) if '--lines' in o else (1, 10 ** 12)
    n = 0
    srcs, rc = sources(pos[1:], o)
    for label, text in srcs:
        for i, l in enumerate(text.split(NL), 1):
            if lo <= i <= hi and rx.search(l):
                print(cut('%s:%d: %s' % (label, i, l), o))
                n += 1
                if mx and n >= mx:
                    print('peek: --max %d reached' % mx)
                    return done(n, rc)
    return done(n, rc)


def head(pos, o, tail=False):
    if '--of' in o:          # no path: the one positional, where given, is N
        n, pos = (int(pos[0]) if pos else 10), []
    else:
        n = int(pos[1]) if len(pos) > 1 else 10
    srcs, rc = sources(pos[:1], o)
    for label, text in srcs:
        if '--bytes' in o and not tail:
            print(text.encode('utf-8')[:int(o['--bytes'])].decode('utf-8', 'replace'))
            continue
        L = text.split(NL)
        if L and L[-1] == '':
            L = L[:-1]
        for l in (L[-n:] if tail else L[:n]):
            print(cut(l, o))
    return done(None, rc)


def count(pos, o):
    rx = matcher(o.get('--pattern'), o)
    tot = 0
    srcs, rc = sources(pos, o)
    for label, text in srcs:
        L = text.split(NL)
        if L and L[-1] == '':
            L = L[:-1]
        k = sum(1 for l in L if rx.search(l)) if rx else len(L)
        tot += k
        print('%7d %s' % (k, label))
    if len(srcs) > 1:
        print('%7d in all' % tot)
    return done(tot, rc)


def listing(pos, o):
    d = pos[0] if pos else '.'
    es = [e for e in os.scandir(d) if fnmatch.fnmatch(e.name, o.get('--glob', '*'))]
    key = o.get('--sort', 'name')
    es.sort(key={'time': lambda e: -e.stat().st_mtime, 'size': lambda e: -e.stat().st_size}.get(key, lambda e: e.name))
    mx = int(o.get('--max', 0) or 0)
    for e in es[:mx] if mx else es:
        if o.get('--long'):
            st = e.stat()
            print('%10d %s %s%s' % (st.st_size, time.strftime('%Y-%m-%d %H:%M', time.localtime(st.st_mtime)), e.name, '/' if e.is_dir() else ''))
        else:
            print(e.name + ('/' if e.is_dir() else ''))
    return done(len(es), None)


def done(n, rc):
    if rc is not None:
        print('peek: the command exited %d' % rc)
    return n


def main(argv):
    if not argv:
        sys.exit(__doc__)
    verb, (pos, o) = argv[0], opts(argv[1:])
    fn = dict(search=search, head=head, tail=lambda p, o: head(p, o, tail=True), count=count, list=listing).get(verb)
    if fn is None:
        sys.exit('peek: search | head | tail | count | list')
    return fn(pos, o)


if __name__ == '__main__':
    main(sys.argv[1:])
