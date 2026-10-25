# -*- coding: utf-8 -*-
"""act_membrane.py -- THE MEMBRANE, standing clauses v2 row (53) ((R321)(2)(ii)), a shared tool from b711.

### "every tool that writes a named bank reads data/act_roots.txt and refuses to write once the act's root is appended, the mirror builder
### excepted as the b670 form has it; locator and read tools write nothing." A NAMED BANK is a bank the act's root names (b710's defect (j),
### quoting its ferry: "no named bank written after it"): every file under relay data/ that the root route's exclusion pattern for the act
### (ROOT_EXCLUDE) does not take out, and every other relay file the root's items carry; the mirror builder's banks (mirror*, the b670 form)
### pass. `guard(act, name, exclude)` is called by the shared writers before any write and exits, writing nothing, where the act's root is
### appended and the bank is named. `roots` is a parameter so the control can read a test copy of the chain; no environment variable is read.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOTS = os.path.join(ROOT, 'data', 'act_roots.txt')
MIRROR = re.compile(r'^(?:b\d{3}_)?mirror')


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


def guard(act, name, exclude=None, roots=None):
    r = refuses(act, name, exclude, roots)
    if r:
        print(r, flush=True)
        sys.exit(4)


def guard_path(act, path, exclude=None, roots=None):
    """the guard for a write named by its path: applied where the path lies directly under relay data/ (the banks); a tool's own file or a
    scratch file elsewhere passes (the seal's hashes guard the tools)."""
    p = os.path.normcase(os.path.abspath(path))
    if os.path.dirname(p) == os.path.normcase(os.path.join(ROOT, 'data')):
        guard(act, os.path.basename(p), exclude, roots)
