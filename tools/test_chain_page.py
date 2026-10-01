# -*- coding: utf-8 -*-
"""test_chain_page.py -- THE TEST OF tools/chain_page.py's PARSER AND EMITTER, written at b568 under (R178)(4).

### ### Runs `chain_page.build` with `from_output` on a BANKED probe output (no lean call) and its mutations:
###   (1) the banked output re-emitted       -> exit 0 and the page byte-identical to the page given (the generated page);
###   (2) one node's block removed            -> exit 6 (unresolved), no page -- a missing print is refused;
###   (3) one theorem's axioms given sorryAx  -> the page shows sorryAx in that node's axioms cell and its tier is NOT T0
###                                              -- a print beyond the three is never read as T0;
###   (4) one node's statement changed        -> the emitted page differs from the generated page at that node's line
###                                              (g_chain_page.compare reports it) -- a changed statement is refused;
###   (5) one CELL line cut short             -> exit 6.
### Usage: python tools/test_chain_page.py <nodes.txt> <probe_out.txt> <page.md>
"""
import io
import os
import re
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402
import g_chain_page as G   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main(argv):
    nodes, out_path, page_path = argv[0], argv[1], argv[2]
    out = io.open(out_path, encoding='utf-8').read().replace('\r', '')
    page = open(page_path, 'rb').read()
    tmp = tempfile.mkdtemp()
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-96s %s' % (label, 'PASS' if cond else '### FAIL'))

    def build_from(text):
        p = os.path.join(tmp, 'o%d.txt' % len(res))
        io.open(p, 'w', encoding='utf-8', newline='\n').write(text)
        return C.build(nodes, tmp, p)

    rc, pg, meta, log = build_from(out)
    want('(1) the banked output re-emitted: exit 0', rc == 0)
    want('(1) and the page byte-identical to the generated page', rc == 0 and pg.encode('utf-8') == page)

    victim = 'SIDEExplicitFormula.B321.h2_sign_iff_rh'
    cut = re.sub(r'^@@BEGIN %s\n.*?^@@END %s\n' % (re.escape(victim), re.escape(victim)), '', out, flags=re.M | re.S)
    want('(2) mutation applied: %s`s block removed' % victim, cut != out)
    rc2, pg2, _m, log2 = build_from(cut)
    want('(2) a missing print: exit 6, no page (read %s)' % rc2, rc2 == 6 and pg2 is None)

    ax = re.sub(r"^('%s' depends on axioms: \[)propext" % re.escape(victim), r'\1propext, sorryAx', out, flags=re.M)
    want('(3) mutation applied: sorryAx injected into %s`s print' % victim, ax != out)
    rc3, pg3, m3, _l = build_from(ax)
    line3 = [l for l in (pg3 or '').split('\n') if ('`%s`' % victim) in l]
    want('(3) a print beyond the three: the axioms cell shows sorryAx', rc3 == 0 and line3 and 'sorryAx' in line3[0])
    want('(3) and the tier is NOT T0 (read %s)' % (m3['cells'][victim]['tier'] if m3 else None),
         rc3 == 0 and m3['cells'][victim]['tier'] != 'T0')

    st = out.replace('theorem %s : SIDEExplicitFormula.B321.h2_sign ↔ RiemannHypothesis' % victim,
                     'theorem %s : SIDEExplicitFormula.B321.h2_sign → RiemannHypothesis' % victim)
    want('(4) mutation applied: the statement`s ↔ made →', st != out)
    rc4, pg4, _m4, _l4 = build_from(st)
    ok4, at4 = G.compare(page, pg4.encode('utf-8') if pg4 else None)
    want('(4) a changed statement: the page differs (first differing line %s)' % at4, rc4 == 0 and not ok4 and at4 is not None)

    sh = re.sub(r'^(@@CELL @@KIND theorem @@MODULE SIDEExplicitFormula\.Seam) .*?(?=^@@STMT$)', r'\1\n', out, count=1, flags=re.M | re.S)
    want('(5) mutation applied: one CELL line cut short', sh != out)
    rc5, pg5, _m5, _l5 = build_from(sh)
    want('(5) a cut CELL: exit 6 (read %s)' % rc5, rc5 == 6 and pg5 is None)

    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
