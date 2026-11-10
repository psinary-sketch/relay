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


# ### v1.32.0, (R362)(7)(viii), b751 defects (g), (p): THE LIMIT ROW READS THE COMMAND'S OWN ARGUMENTS. v1.31.0 matched a route's name anywhere in
# ### the command (with quoted text blanked after (g)): a line count over the tool (b751 (p), `wc -l tools/b750_prepaths.py ...`) and a search
# ### naming a suite's module (b752, `git grep ... -- tools/b703_checks.py`, refused twice at 22:1xZ) read as runs. A route is read in the
# ### interpreter's place alone: for each simple command (split at &&, ||, ; and line ends), the script a python interpreter runs with the
# ### arguments after it (its options skipped; `-c` runs code and no script; `-m` a module, not read), or a .ps1 file in the run position.
import shlex   # noqa: E402

SEP = re.compile(r'&&|\|\||;|\n')
PY = re.compile(r'(?i)^(?:.*/)?(?:python(?:3(?:\.\d+)?)?|py)(?:\.exe)?$')
PY_TAKES = ('-X', '-W', '--check-hash-based-pycs')


def _tokens(seg):
    try:
        return shlex.split(seg, posix=True)
    except ValueError:
        return seg.split()


def runs(cmd):
    """[the run's text]: each script an interpreter runs, with its arguments, and each .ps1 run, read from the command's own arguments."""
    out = []
    for seg in SEP.split((cmd or '').replace('\\', '/')):
        t = _tokens(seg)
        for i, tok in enumerate(t):
            if PY.match(tok):
                j = i + 1
                while j is not None and j < len(t) and t[j].startswith('-'):
                    if t[j] in ('-c', '-m'):
                        j = None
                        break
                    j += 2 if t[j] in PY_TAKES else 1
                if j is not None and j < len(t):
                    out.append(' '.join(t[j:]))
                break
            if tok.lower().endswith('.ps1') and (i == 0 or t[i - 1] in ('&', '.', '-File', '-file')):
                out.append(' '.join(t[i:]))
                break
    return out


def limit_of(cmd):
    for r in runs(cmd):
        for what, rx, ms in LONG:
            if rx.search(r):
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
