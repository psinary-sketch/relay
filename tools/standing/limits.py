# -*- coding: utf-8 -*-
"""standing/limits.py -- v1.31.0, (R361)(3)(ix), b750 defect (t), events (6): THE HOST'S LIMIT.

b750's seat sent the probe-path tool's run (`tools/b750_prepaths.py --bank`) in the foreground with no limit, so with the host's default of two
minutes, and the host moved it to the background when the limit passed (tools/standing/harnessmoves.py reads such moves apart). A run that may
exceed the host's default is sent with the limit the tool prints: this table is that print, and the hook (tools/standing/hook.py, kind LIMIT)
refuses a foreground call of a route in the table sent with no timeout or a timeout beneath the route's limit.

  python -X utf8 -u tools/standing/limits.py          print the table: each route, its limit in milliseconds
  limit_of(cmd) -> (route, ms) or None     fault(cmd, timeout, background) -> None or the refusal's detail
"""
import re
import sys

HOST_DEFAULT_MS = 120000
LONG = (
    ('a suite part or combine (fold.py checks --part / --combine)', re.compile(r'(?:_checks\.py\b|\bstanding/fold\.py\s+checks\b)'), 600000),
    ('a record route (fold.py record ...)', re.compile(r'\bstanding/fold\.py\s+record\b'), 600000),
    ('the citation route (fold.py citation ...)', re.compile(r'\bstanding/fold\.py\s+citation\b'), 600000),
    ('the standing dry (standingdry.py run)', re.compile(r'\bstanding/standingdry\.py\s+run\b'), 600000),
    ('a standing version`s controls (tools/standing/v1NNN.py control)', re.compile(r'\bstanding/v1\d{2,3}\.py\s+control\b'), 600000),
    ('the probe-path tool (tools/<act>_prepaths.py)', re.compile(r'\btools/b\d{3}_prepaths\.py\b'), 600000),
    ('the reproduce run (tools/research/reproduce.py)', re.compile(r'\bresearch/reproduce\.py\b'), 600000),
    ('the root route (tools/act_root.py)', re.compile(r'\btools/act_root\.py\b'), 600000),
    ('the mirror build (mirror_build.ps1)', re.compile(r'\bmirror_build\.ps1\b'), 600000),
)


def limit_of(cmd):
    for what, rx, ms in LONG:
        if rx.search((cmd or '').replace('\\', '/')):
            return what, ms
    return None


def fault(cmd, timeout, background=False):
    """None, or the detail: a route of the table sent in the foreground with no timeout or one beneath its limit."""
    if background:
        return None
    lo = limit_of(cmd)
    if lo is None:
        return None
    what, ms = lo
    try:
        t = int(timeout) if timeout is not None else None
    except (TypeError, ValueError):
        t = None
    if t is None or t < ms:
        return '%s sent with %s, beneath the limit the tool prints (%d ms; the host`s default %d ms) -- send it again with timeout %d' % (
            what, 'no timeout' if t is None else 'timeout %d' % t, ms, HOST_DEFAULT_MS, ms)
    return None


if __name__ == '__main__':
    print('THE HOST`S LIMIT ((R361)(3)(ix)): a route below is sent in the foreground with the timeout printed beside it (the host`s default %d ms)' % HOST_DEFAULT_MS)
    for what, rx, ms in LONG:
        print('  %-70s timeout %d' % (what, ms))
    sys.exit(0)
