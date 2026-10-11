# -*- coding: utf-8 -*-
"""test_name_b649.py -- THE TEST OF THE NAME, under (R259)(5): the bare phrase "the clause" leaves generated text.

### (1) relay data/glossary.txt carries the entry `the positivity clause`, its opening mention "the positivity clause (h2_sign: ...)" read
### from it; (2) the ζ page emitted from b648's list with the one line `# positivity clause` (a temporary copy) holds no bare "the clause",
### its first lower-case mention of the name is the opening mention in the glossary's words and every later one reads "the positivity
### clause"; (3) the χ page the same; (4) b648's lists without the line emit the pages as before -- the old titles, no mention of the name
### in the head line (their glossary block carries the new entry, as every list marked `# glossary` does);
### (5) v5's composer with the name's edit holds no bare "the clause", its first mention the glossary form; (6) the positive control: v4 as
### b647 composed it holds the bare phrase, and the grep finds it. The pages are emitted from b643's banked probes, no Lean call.
"""
import os
import re
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.argv = sys.argv[:1]
import chain_page as CP   # noqa: E402
import b649_record as R   # noqa: E402
import b647_record as B7   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
D = os.path.join(ROOT, 'data')
BARE = re.compile(r'\bthe clause\b', re.I)


def mentions_ok(text, mention):
    """the first lower-case "the positivity clause" is the opening mention; every later one is followed by no parenthesis."""
    idx = [m.start() for m in re.finditer(r'the positivity clause', text)]
    if not idx or not text.startswith(mention, idx[0]):
        return False
    return all(not text.startswith(mention, i) for i in idx[1:])


def emit(src, mark):
    tmp = tempfile.mkdtemp(prefix='b649_name_')
    lp = os.path.join(tmp, os.path.basename(src))
    body = open(os.path.join(D, src), encoding='utf-8').read().rstrip('\n') + ('\n#\n' + CP.POSITIVITY_MARK if mark else '') + '\n'
    open(lp, 'w', encoding='utf-8', newline='\n').write(body)
    probe = os.path.join(D, 'b643_probe_out_%s.txt' % ('zeta' if 'zeta' in src else 'chi'))
    rc, page, _m, _l = CP.build(lp, os.path.join(tmp, 'probe'), probe)
    return rc, page or ''


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-96s %s' % (label, 'PASS' if cond else '### FAIL'))

    m = CP.positivity_mention()
    want('(1) the glossary`s entry read: %s' % m[:80], m.startswith('the positivity clause (h2_sign: Weil positivity on classK'))
    for k, title in (('zeta', CP.POSITIVITY_TITLE), ('chi', CP.POSITIVITY_DIR_TITLE)):
        rc, page = emit('b648_nodes_%s.txt' % k, True)
        want('(%d) the %s page with the line: exit %d, bare "the clause" %d, title %s, opening mention in the glossary`s words %s' % (
            2 if k == 'zeta' else 3, k, rc, len(BARE.findall(page)), page.startswith(title), mentions_ok(page, m)),
             rc == 0 and not BARE.findall(page) and page.startswith(title) and mentions_ok(page, m))
    rz, pz = emit('b648_nodes_zeta.txt', False)
    rx, px = emit('b648_nodes_chi.txt', False)
    hz, hx = pz.split('\n')[2] if pz else '', px.split('\n')[2] if px else ''
    want('(4) b648`s lists without the line: the old titles, no mention of the name in the head line (exit %d, %d; the glossary block carries '
         'the entry)' % (rz, rx),
         rz == 0 and rx == 0 and pz.startswith('# THE CLAUSE AND ITS COMPILED FACES') and px.startswith(CP.DIR_TITLE)
         and 'positivity clause' not in hz and 'positivity clause' not in hx and hz.startswith('This page is generated'))
    h = R.compose_v5(('e',))
    want('(5) v5`s composer with the name: bare "the clause" %d, unread %s, opening mention in the glossary`s words %s' % (
        len(BARE.findall(h)), 'NOT READ' in h, mentions_ok(h, m)), not BARE.findall(h) and 'NOT READ' not in h and mentions_ok(h, m))
    v4 = B7.compose_v4()
    want('(6) the control: v4 holds the bare phrase and the grep finds it (%d)' % len(BARE.findall(v4)), len(BARE.findall(v4)) >= 1)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
