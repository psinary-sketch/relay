# -*- coding: utf-8 -*-
"""g_chain_page.py -- THE ARM G-CHAIN-PAGE, SHARED. ### (R178)(4): "a suite arm can re-derive it"; written at b568.

### ### **THE ARM.** The page committed at the corpus root (PLACE-papers HEAD's blob of THE_CLAUSE_AND_ITS_COMPILED_FACES.md)
### is compared BYTE FOR BYTE with a fresh run of relay tools/chain_page.py from the same node list. ### (R183)(5), b573: the
### page compared is the one the list names -- THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md for a `# page: dirichlet` list. PASS only when the
### regeneration exits 0 AND the bytes are equal. A regeneration that fails is a FAIL, never a skip: an arm that cannot
### read its source fails (b461's harness rule). `from_output` re-emits from a banked probe output without a lean call
### (the test's fast path); a suite runs the full regeneration.
### Usage: python tools/g_chain_page.py --nodes <nodes.txt> --probe-dir <dir> [--from-output <probe_out.txt>]
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def committed_page(rev='HEAD', name=None):
    r = subprocess.run(['git', '-C', C.PP, 'show', '%s:%s' % (rev, name or C.PAGE_NAME)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def compare(committed, regenerated):
    """### RETURN (ok, first differing line number or None). Both are bytes; None on either side is a FAIL."""
    if committed is None or regenerated is None:
        return False, None
    if committed == regenerated:
        return True, None
    a, b = committed.split(b'\n'), regenerated.split(b'\n')
    for i, (x, y) in enumerate(zip(a, b), 1):
        if x != y:
            return False, i
    return False, min(len(a), len(b)) + 1


def arm(nodes, probe_dir, from_output=None, committed=None):
    rc, page, meta, log = C.build(nodes, probe_dir, from_output)
    regen = page.encode('utf-8') if rc == 0 and page is not None else None
    com = committed if committed is not None else committed_page(name=C.page_name_of(nodes))   # ### (R183)(5): the list names its page
    ok, at = compare(com, regen)
    return dict(ok=ok, rc=rc, first_diff=at, committed_bytes=len(com or b''), regenerated_bytes=len(regen or b''), log=log)


if __name__ == '__main__':
    a = sys.argv[1:]
    get = lambda k: a[a.index(k) + 1] if k in a else None
    res = arm(get('--nodes'), get('--probe-dir'), get('--from-output'))
    for l in res['log']:
        print('g_chain_page: ' + l)
    print('G-CHAIN-PAGE : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s'
          % ('PASS' if res['ok'] else 'FAIL', res['rc'], res['committed_bytes'], res['regenerated_bytes'], res['first_diff']))
    sys.exit(0 if res['ok'] else 1)
