# -*- coding: utf-8 -*-
"""act_membrane.py -- THE MEMBRANE, standing clauses v2 row (53) ((R321)(2)(ii)), a shared tool from b711.

### "every tool that writes a named bank reads data/act_roots.txt and refuses to write once the act's root is appended, the mirror builder
### excepted as the b670 form has it; locator and read tools write nothing." A NAMED BANK is a bank the act's root names (b710's defect (j),
### quoting its ferry: "no named bank written after it"): every file under relay data/ that the root route's exclusion pattern for the act
### (ROOT_EXCLUDE) does not take out, and every other relay file the root's items carry; the mirror builder's banks (mirror*, the b670 form)
### pass. `guard(act, name, exclude)` is called by the shared writers before any write and exits, writing nothing, where the act's root is
### appended and the bank is named. `roots` is a parameter so the control can read a test copy of the chain; no environment variable is read.
### v1.26.0, (R356)(3)(iv), b745 events (5)-(6): the refusal's line is composed from the working tree (line(), strays()): a file the refused
### route wrote before the refusal is named in the line and deleted by the tool that refused, by its verified absolute path.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOTS = os.path.join(ROOT, 'data', 'act_roots.txt')
MIRROR = re.compile(r'^(?:b\d{3}_)?mirror')
T0 = __import__('time').time()   # ### v1.26.0: the route's start, read at the membrane's import


def appended(act, roots=None):
    """the act's line in the chain (`<act> <root> <previous>`), or '' where the act's root is not appended."""
    p = roots or ROOTS
    if not os.path.exists(p):
        return ''
    for l in open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(chr(10)):
        if l.split(' ', 1)[0] == act and len(l.split()) >= 3:
            return l
    return ''


def named(name, exclude=None):
    """True where the bank is one the root names: not a mirror builder's bank and not taken out by the act's exclusion pattern."""
    base = os.path.basename(name)
    if MIRROR.match(base):
        return False
    return not (exclude is not None and exclude.match(base))


def refuses(act, name, exclude=None, roots=None):
    """the refusal's text where the write is refused, '' where it may proceed."""
    line = appended(act, roots)
    if line and named(name, exclude):
        return ('### THE MEMBRANE (standing clauses v2 row (53)): %s`S ROOT IS APPENDED (data/act_roots.txt: %s...) AND %s IS A BANK THE ROOT '
                'NAMES -- NOTHING WRITTEN' % (act, line[:20], name))
    return ''


def _untracked(root):
    import subprocess
    out = subprocess.run(['git', '-C', root, 'ls-files', '--others', '--exclude-standard', '--', 'data/'], capture_output=True, text=True,
                         encoding='utf-8', errors='replace').stdout
    return [x for x in out.replace(chr(13), '').split(chr(10)) if x.strip()]


def strays(name, root=None, since=None):
    """v1.26.0, (R356)(3)(iv), b745 events (5)-(6): the files a refused route wrote before the membrane refused it -- read from the working tree,
    not asserted: the untracked files directly under data/ whose names carry the refused name's stem (b745: the bank name `--quiet` refused,
    data/b745_chain_half_nsm1_--quiet.json written). The refused name itself is not among them (it was not written)."""
    base = os.path.basename(name)
    stem = os.path.splitext(base)[0]
    if len(stem) < 3:
        return []
    root = root or ROOT
    t0 = T0 if since is None else since   # ### written by this run of the route: at or after the membrane's import, never an earlier act's file
    return [p for p in _untracked(root) if p.count('/') == 1 and stem in os.path.basename(p) and os.path.basename(p) != base
            and os.path.getmtime(os.path.join(root, p)) >= t0 - 1]


def _delete_verified(root, rel):
    """a stray deleted by its verified absolute path: under <root>/data, a file, untracked; True where gone after."""
    d = os.path.normcase(os.path.abspath(os.path.join(root, 'data')))
    p = os.path.abspath(os.path.join(root, rel))
    if os.path.normcase(os.path.dirname(p)) != d or not os.path.isfile(p) or rel not in _untracked(root):
        return False
    os.remove(p)
    return not os.path.exists(p)


def line(act, name, exclude=None, roots=None, root=None, delete=True, since=None):
    """v1.26.0, (R356)(3)(iv): the membrane's line composed from the working tree: NOTHING WRITTEN only where no stray stands; otherwise each
    stray named, deleted by the tool that refused, and its deletion read back. Returns (text, [(stray, deleted)]) -- ('', []) where it passes."""
    r = refuses(act, name, exclude, roots)
    if not r:
        return '', []
    root = root or ROOT
    st = strays(name, root, since)
    done = [(p, _delete_verified(root, p) if delete else False) for p in st]
    if not st:
        return r + ' (the working tree read: no stray)', done
    r = r.replace(' -- NOTHING WRITTEN', ' -- THE BANK NOT WRITTEN; THE ROUTE WROTE %d STRAY(S) BEFORE THE REFUSAL: %s' % (
        len(st), ', '.join('%s %s' % (p, 'DELETED BY ITS ABSOLUTE PATH' if ok else '### NOT DELETED') for p, ok in done)))
    return r, done


def guard(act, name, exclude=None, roots=None, root=None):
    r, _done = line(act, name, exclude, roots, root)
    if r:
        print(r, flush=True)
        sys.exit(4)


def guard_path(act, path, exclude=None, roots=None):
    """the guard for a write named by its path: applied where the path lies directly under relay data/ (the banks); a tool's own file or a
    scratch file elsewhere passes (the seal's hashes guard the tools)."""
    p = os.path.normcase(os.path.abspath(path))
    if os.path.dirname(p) == os.path.normcase(os.path.join(ROOT, 'data')):
        guard(act, os.path.basename(p), exclude, roots)
