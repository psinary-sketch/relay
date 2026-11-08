# -*- coding: utf-8 -*-
"""standing/relaypath.py -- THE RECORD'S READERS TAKE A RELAY PATH ONCE (v1.27.0, (R357)(3)(vii), b746 defect (p)).

b746's N2 score route read rdn('data/b746_section1.txt'); rdn joined data/ to a name already carrying it and read '' from no file, so the
score's dry form printed "[S1] passed: False" over a bank holding [S1] PASS. Here each reader joins its root once and refuses a path that
resolves to no file, printing the name and the path; a read that may find no file says so at its call (optional=True) and reads ''.

  rdn(name, optional=False)  a bank's name under data/, joined once: rdn('data/x.txt') resolves to data/data/x.txt and is REFUSED
  rdp(rel, optional=False)   a relay-relative path ('data/...', 'tools/...'), joined once to the relay root
  rd(path, optional=False)   an absolute path as it stands
"""
import io
import os

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(RELAY, 'data')


def refuse(name, path):
    raise SystemExit('### REFUSED: %s resolves to no file (%s) -- the record reads no bank that is not there (v1.27.0, (R357)(3)(vii))' % (name, path))


def _read(name, path, optional):
    if not os.path.isfile(path):
        if optional:
            return ''
        refuse(name, path)
    return io.open(path, encoding='utf-8').read().replace(chr(13), '')


def rd(path, optional=False):
    return _read(path, path, optional)


def rdn(name, optional=False):
    return _read(name, os.path.join(D, name), optional)


def rdp(rel, optional=False):
    return _read(rel, os.path.join(RELAY, rel), optional)
