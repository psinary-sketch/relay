# -*- coding: utf-8 -*-
"""test_chain_page_b596.py -- THE TEST OF THE TWO GENERATOR CLAUSES b596 ADDED TO tools/chain_page.py, on the author's answers
(relay data/b596_author_answers.txt, prompt 1 before the seal, prompt 3 after the pages' first re-emission).

### (1)-(2) A LIST WITHOUT A `# backmatter:` RECORD REGENERATES BYTE FOR BYTE: b592's ζ and χ lists re-emitted from their v0.16
###   probe outputs by the generator as it stands, against each page's blob at PLACE-papers ba5f0ea (the pages before b596).
### (3) THE CHANNEL: b592's ζ list with two `# backmatter:` records appended, re-emitted from the same probe -- the page is the
###   page of (1) with one paragraph after the Correspondence table, the records' text in list order joined by one space.
### (4) THE READER: backmatter_of reads no record from b592's lists and the two records, in order, from the list of (3).
### (5) THE ENTRY TAG OF A STRUCTURE: entry_tag finds SIDEExplicitFormula.Simplicity.SimpleProportion (a `structure`) at v0.17,
###   and still finds a theorem (simplicity_iff) and a definition (allSimple) of the same file at v0.17.
### Usage: python tools/test_chain_page_b596.py
### ### b597, (R207)(2) and the author's answer before b597's seal (relay data/b597_author_answers.txt): THE CONTROL FROZEN AT WHAT IT
### CONTROLS. Cases (1)-(4) and the suite's control arm G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA read b592's two lists and probe
### outputs by `git show` at relay 12c15c80 (their one commit), and the generator's every HEAD read is redirected for the run: the
### terminal table at relay 12c15c80 (blob 2ce26253, the blob at ac8257a5), README, REGISTRY, the keystone grep and the expected
### pages at PLACE-papers ba5f0ea. One pin per repository; tools/chain_page.py is untouched (its `git` is swapped in this file).
"""
import io
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PRE_PP = 'ba5f0ea'
RELAY_PIN = '12c15c80'
ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
LISTS = (('b592_nodes.txt', 'b592_probe_out.txt', 'PAGE_NAME'), ('b592_nodes_chi.txt', 'b592_chi_probe_out.txt', 'DIR_PAGE_NAME'))
NL = chr(10)


def blob(spec):
    r = subprocess.run(['git', '-C', C.PP, 'show', spec], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def relay_blob(path):
    r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (RELAY_PIN, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def _frozen_git(repo, *a):
    """### the generator's own `git`, every HEAD read redirected: relay HEAD -> 12c15c80, PLACE-papers HEAD -> ba5f0ea."""
    a = list(a)
    r = repo.replace(chr(92), '/')
    if a[:1] == ['show'] and len(a) > 1 and a[1].startswith('HEAD:'):
        if r == ROOT.replace(chr(92), '/'):
            a[1] = RELAY_PIN + a[1][4:]
        elif r == C.PP:
            a[1] = PRE_PP + a[1][4:]
    elif r == C.PP and a[:1] == ['grep'] and 'HEAD' in a:
        a[a.index('HEAD')] = PRE_PP
    return _GIT(repo, *a)


_GIT = C.git


def pinned_lists():
    """### b592's two lists and probe outputs written from relay 12c15c80 into a fresh directory, under their own names."""
    d = tempfile.mkdtemp()
    out = []
    for ln, pn, page in LISTS:
        lb, pb = relay_blob('data/' + ln), relay_blob('data/' + pn)
        if lb is None or pb is None:
            return None
        lp, pp = os.path.join(d, ln), os.path.join(d, pn)
        open(lp, 'wb').write(lb)
        open(pp, 'wb').write(pb)
        out.append((lp, pp, getattr(C, page)))
    return out


def regen(nodes, probe):
    C.git = _frozen_git
    try:
        rc, page, _meta, log = C.build(nodes, tempfile.mkdtemp(), probe)
    finally:
        C.git = _GIT
    return rc, (page.encode('utf-8') if rc == 0 and page is not None else None)


def control():
    """### THE ARM G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA: each list re-emitted frozen, against its page at ba5f0ea."""
    import g_chain_page as GCP
    pl = pinned_lists()
    if pl is None:
        return [dict(ok=False, rc=-1, list=x[0], first_diff=None, committed_bytes=0, regenerated_bytes=0) for x in LISTS]
    res = []
    for lp, pp, page in pl:
        rc, got = regen(lp, pp)
        com = blob('%s:%s' % (PRE_PP, page))
        ok, at = GCP.compare(com, got)
        res.append(dict(ok=ok, rc=rc, list=os.path.basename(lp), first_diff=at, committed_bytes=len(com or b''), regenerated_bytes=len(got or b'')))
    return res


def main():
    res = []
    print('### pins: relay %s (the lists, the probes, the terminal table blob %s) ; PLACE-papers %s (pages, README, REGISTRY, keystones)' % (
        RELAY_PIN, subprocess.run(['git', '-C', ROOT, 'rev-parse', '--short=8', RELAY_PIN + ':data/terminal_table.json'],
                                  capture_output=True).stdout.decode().strip(), PRE_PP))
    (zl, zp, _zn), (cl, cp, _cn) = pinned_lists()
    rc1, z = regen(zl, zp)
    res.append(('(1) b592 ζ list, no record: byte for byte against the page at %s' % PRE_PP, rc1 == 0 and z == blob('%s:%s' % (PRE_PP, C.PAGE_NAME))))
    rc2, c = regen(cl, cp)
    res.append(('(2) b592 χ list, no record: byte for byte against the page at %s' % PRE_PP, rc2 == 0 and c == blob('%s:%s' % (PRE_PP, C.DIR_PAGE_NAME))))
    d = tempfile.mkdtemp()
    tl = os.path.join(d, 'b592_nodes.txt')
    src = io.open(zl, encoding='utf-8').read()
    io.open(tl, 'w', encoding='utf-8', newline=NL).write(src.rstrip(NL) + NL + '# backmatter: first record, its words' + NL + '# backmatter: second record.' + NL)
    rc3, t = regen(tl, zp)
    want = (z or b'') + (NL + 'first record, its words second record.' + NL).encode('utf-8')
    res.append(('(3) two records: the page of (1) with one paragraph after the Correspondence table', rc3 == 0 and z is not None and t == want))
    res.append(('(4) the reader: no record from b592`s lists; the two, in order, from the list of (3)',
                C.backmatter_of(zl) == [] and C.backmatter_of(cl) == [] and C.backmatter_of(tl) == ['first record, its words', 'second record.']))
    rel = 'SIDEExplicitFormula/Simplicity.lean'
    e = [C.entry_tag(rel, n) for n in ('SimpleProportion', 'simplicity_iff', 'allSimple')]
    res.append(('(5) the entry tag of a structure, a theorem and a definition of Simplicity.lean: %s' % e,
                all(x == ('v0.17', '5a1630b') for x in e)))
    for name, ok in res:
        print('  %-120s %s' % (name, 'PASS' if ok else 'FAIL'))
    ok = all(x for _n, x in res)
    print('### %s' % ('ALL PASS' if ok else 'NOT ALL PASS'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
