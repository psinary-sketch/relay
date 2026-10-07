# -*- coding: utf-8 -*-
"""test_chain_page_b638.py -- THE TEST OF tools/chain_page.py's GLOSSARY BLOCK, (R248)(4), written at b638.

###   (1) the glossary's entries read from relay data/glossary.txt: one per line that is no comment, each a name, a definition and a source;
###   (2) a line that is not name, definition and source raises ValueError (a file written to a fresh temporary directory);
###   (3) b632's two lists carry no mark; the same lists with the one line `# glossary` appended carry it;
###   (4) A LIST WITHOUT THE MARK EMITS EXACTLY AS BEFORE: b632's ζ list, re-emitted from b635's probe by the generator as it stands and by the
###       generator as it stood at relay 2aa41700, reads byte for byte the same page;
###   (5) a list with the mark: its page is the unmarked page with the block inserted beneath the head line, the head line naming its own list
###       and nothing else moving;
###   (6) the block reads byte for byte alike on the ζ page and the χ page, each from its marked list;
###   (7) the block is its heading, its introduction and one line per entry.
### The marked lists are written to a fresh temporary directory; nothing in relay or PLACE-papers is written. Usage: python tools/test_chain_page_b638.py
"""
import io
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import chain_page as C  # noqa: E402
import b627_record as R27  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PRE_RELAY = '2aa41700'
OLD = {'zeta': 'b632_nodes_zeta.txt', 'chi': 'b632_nodes_chi.txt'}
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}
res = []


def want(label, ok):
    res.append(bool(ok))
    print('  (%d) %s -- %s' % (len(res), label, 'PASS' if ok else 'FAIL'))


def marked(k, tmp):
    old = io.open(os.path.join(D, OLD[k]), encoding='utf-8').read().replace(chr(13), '')
    p = os.path.join(tmp, 'b638_test_nodes_%s.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=NL).write(old + ('' if old.endswith(NL) else NL) + C.GLOSSARY_MARK + NL)
    return p


def block(page):
    ls = page.split(NL)
    if C.GLOSSARY_HEAD not in ls:
        return []
    i = ls.index(C.GLOSSARY_HEAD)
    j = i + 4
    while j < len(ls) and ls[j].startswith('- **'):
        j += 1
    return ls[i:j]


def main():
    ents = C.glossary_entries()
    raw = io.open(C.GLOSSARY_FILE, encoding='utf-8').read().replace(chr(13), '')
    lines = [l for l in raw.split(NL) if l.strip() and not l.startswith('#')]
    want('the glossary`s entries %d, its lines that are no comment %d, each a name, a definition and a source' % (len(ents), len(lines)),
         ents and len(ents) == len(lines) and all(len(e) == 3 and all(e) for e in ents))
    tmp = tempfile.mkdtemp()
    bad = os.path.join(tmp, 'bad_glossary.txt')
    io.open(bad, 'w', encoding='utf-8', newline=NL).write('# a comment' + NL + 'a name\tits definition alone' + NL)
    try:
        C.glossary_entries(bad)
        raised = False
    except ValueError:
        raised = True
    want('a line with two fields raises ValueError', raised)
    mz, mx = marked('zeta', tmp), marked('chi', tmp)
    want('b632`s lists carry no mark (%s, %s); the marked lists carry it (%s, %s)' % (
        C.node_glossary(os.path.join(D, OLD['zeta'])), C.node_glossary(os.path.join(D, OLD['chi'])), C.node_glossary(mz), C.node_glossary(mx)),
         not C.node_glossary(os.path.join(D, OLD['zeta'])) and not C.node_glossary(os.path.join(D, OLD['chi'])) and C.node_glossary(mz) and C.node_glossary(mx))
    old_gen = R27.cp_module(PRE_RELAY)
    rc_a, page_a, _m, _l = C.build(os.path.join(D, OLD['zeta']), os.path.join(tmp, 'a'), os.path.join(D, PROBE['zeta']))
    rc_b, page_b, _m, _l = old_gen.build(os.path.join(D, OLD['zeta']), os.path.join(tmp, 'b'), os.path.join(D, PROBE['zeta']))
    want('b632`s ζ list without the mark: the generator as it stands (exit %d, %d bytes) and as it stood at relay %s (exit %d, %d bytes) emit '
         'the same page' % (rc_a, len(page_a or ''), PRE_RELAY, rc_b, len(page_b or '')), rc_a == 0 and rc_b == 0 and page_a == page_b and page_a)
    rc_m, page_m, _m, _l = C.build(mz, os.path.join(tmp, 'm'), os.path.join(D, PROBE['zeta']))
    la, lm = (page_a or '').split(NL), (page_m or '').split(NL)
    blk = block(page_m or '')
    rebuilt = lm[:4] + lm[4 + len(blk) + 1:] if blk else []
    want('the marked ζ page (exit %d): the unmarked page with the block (%d lines) and one blank inserted beneath the head line, the head line '
         'naming its own list' % (rc_m, len(blk)),
         rc_m == 0 and lm[:2] == la[:2] and lm[2] == la[2].replace('data/%s' % OLD['zeta'], 'data/%s' % os.path.basename(mz)) and lm[3] == ''
         and lm[4:4 + len(blk)] == blk and rebuilt[4:] == la[4:] and len(lm) == len(la) + len(blk) + 1)
    rc_x, page_x, _m, _l = C.build(mx, os.path.join(tmp, 'x'), os.path.join(D, PROBE['chi']))
    bx = block(page_x or '')
    want('the block on the marked ζ page and the marked χ page (exit %d): %d and %d lines, byte for byte alike' % (rc_x, len(blk), len(bx)),
         rc_x == 0 and blk and blk == bx)
    want('the block is its heading, its introduction and one line per entry (%d lines, %d entries)' % (len(blk), len(ents)),
         blk == C.glossary_block() and len(blk) == len(ents) + 4 and blk[0] == C.GLOSSARY_HEAD and blk[2] == C.GLOSSARY_INTRO)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
