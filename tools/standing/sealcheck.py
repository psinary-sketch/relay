# -*- coding: utf-8 -*-
"""standing/sealcheck.py -- v1.2.2 ((R332)(2)(i)): G-SEAL-HASHES READS ITS LIST OF SEALED TOOLS FROM THE SEAL BANK IT CHECKS.

The arm compared the seal bank's tools with a list kept in the suite (the worklist's SEALED tuple); when tools/standing/ gained three files
at v1.2.1 the carried list held 33 against the seal's 36 and the arm failed on the list alone, every hash agreeing (b721's event (11)).
Here the list is the seal bank's own `tools` map: each name is read in the tree (now, or at a commit for a closed act) and its sha256
compared with the sealed one; a name the tree does not carry fails, as does a hash that differs. Nothing written.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402


def read(act, rev=None, seal=None):
    """the seal bank's tools against the tree. `rev` None reads the working tree (the act's own suite); a commit reads that commit's blobs
    (a closed act's control). `seal` may pass a seal bank's dict in place of data/<act>_seal_hashes.json (a plant).
    Returns dict(ok, listed, agree, absent, differ)."""
    sj = seal if seal is not None else A.jl('%s_seal_hashes.json' % act)
    tools = sj.get('tools') or {}
    agree, absent, differ = [], [], []
    for t in sorted(tools):
        if rev is None:
            p = os.path.join(A.T, *t.split('/'))
            b = open(p, 'rb').read() if os.path.isfile(p) else None
        else:
            b = A.blob(rev, 'tools/' + t)
        if b is None:
            absent.append(t)
        elif A.sha256_bytes(b) != tools[t]:
            differ.append(t)
        else:
            agree.append(t)
    return dict(ok=bool(tools) and not absent and not differ, listed=len(tools), agree=len(agree), absent=absent, differ=differ)
