# -*- coding: utf-8 -*-
"""b651_record.py -- THE RECORD TOOL OF b651, UNDER (R261): THE RE-CUTS OPENED -- THE DATA AND PAGE ROWS, THE SEAM ROW, THE SIMPLICITY ROW;
THE AXIOM-CLAIM RESOLVER; THE CENSUS AT v0.8.1; THE RESTATED LINES; THE LARGEST KERNEL'S DOCSTRINGS; THE NAVIGATOR'S ROWS.

### Written by the Write tool and extended by the Edit tool as the act runs; sealed at Component 7. Its helpers are b649_record's form; its
### routes write relay data/b651_* alone unless a route's docstring names another file.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
RELAY = ROOT
PP = 'D:/MY-DOwnloads/PLACE-papers'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
os.makedirs(SP, exist_ok=True)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### the lists in force at b651: the zeta list b649's (unchanged), the chi list b651's (its backmatter line re-cut, (R261)(3)(b))
NODES = {'zeta': 'b649_nodes_zeta.txt', 'chi': 'b651_nodes_chi.txt'}
PROBE = {'zeta': 'b643_probe_out_zeta.txt', 'chi': 'b643_probe_out_chi.txt'}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _write(path, b):
    open(path + '.tmp', 'wb').write(b)
    os.replace(path + '.tmp', path)


def put_txt(name, L):
    _write(os.path.join(D, name), (NL.join(L) + NL).encode('utf-8'))


def put_json(name, j):
    _write(os.path.join(D, name), (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


# ================================================================================ COMPONENT 2: THE PAGE ARMS
def page_arms(tag='', *a):
    """data/b651_page_arms[_<tag>].txt: the page arms on the lists in force against PLACE-papers HEAD, and the frozen control with the E0 rule
    at its relay pin (b649's page_arms, carried)."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    import chain_page as CP
    import b626_record as R26
    L = ['b651 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s, relay %s (%s)%s' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), utc(), (' -- ' + tag) if tag else '')]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b651_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', NODES[k], r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    rule = CP.E0
    CP.E0 = R26.e0_module(T.RELAY_PIN)
    try:
        c = T.control()
    finally:
        CP.E0 = rule
    L.append('### the control`s E0 rule: loaded at relay %s' % T.RELAY_PIN)
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b651_page_arms%s.txt' % (('_' + tag) if tag else ''), L)
    print(NL.join(l[:220] for l in L))


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn):
        sys.exit('usage: b651_record.py <route> [args]')
    fn(*sys.argv[2:])
