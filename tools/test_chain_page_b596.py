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
NL = chr(10)


def blob(spec):
    r = subprocess.run(['git', '-C', C.PP, 'show', spec], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def regen(nodes, probe):
    rc, page, _meta, log = C.build(nodes, tempfile.mkdtemp(), probe)
    return rc, (page.encode('utf-8') if rc == 0 and page is not None else None)


def main():
    res = []
    zl, zp = os.path.join(D, 'b592_nodes.txt'), os.path.join(D, 'b592_probe_out.txt')
    cl, cp = os.path.join(D, 'b592_nodes_chi.txt'), os.path.join(D, 'b592_chi_probe_out.txt')
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
