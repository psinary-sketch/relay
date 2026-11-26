# -*- coding: utf-8 -*-
"""standing/hostmask.py -- v1.38.32, (R380)(8) [K32], b770: THE HOST'S FOLDERS MASKED AT THE SOURCE.

b769's closing message, the seat's keys (a) to (c): the papers` repository's parent folder stood in what the act's tools and the standing
tools wrote -- the run cache's map keyed by path (the lsr banks and the act root), the suite's line of the slowest remote read, the pins and
mirror prints, the gated push's captures for the papers` repository (relay data/b769_*, twenty tracked banks with b770's carry bank of the
worklist, counted by name at b770's [K32]); the pass in the previous act's mode printed the two archives of (R379)(4)(d) by their own file
names (data/b769_events_postseal.txt :102-:118); and the components composer listed them (:810-:842). One mask, shared by the writers:

  mask(s)             a text with each form of the papers` repository's path written REPO_ROLE, each form of its parent folder FOLDER_ROLE,
                      the parent's name standing alone FOLDER_ROLE, and each name of an archive's shape ARCHIVE_ROLE; a role carries no
                      space, so a reader's \\S+ reads a role where it read a path; any other value is returned as it is
  mask_lines(lines)   each line masked (a text given whole is masked whole)
  mask_list(items)    a list of paths masked, each distinct archive given a numbered role, so a composer's merge keeps them apart
  mask_obj(o)         a json object masked, its keys and its values
  count(s)            the occurrences mask() changes
  write_text(p, text) the shared writer: the text masked and composed whole, written to p.tmp and moved onto p
  filter              (the command line) each line of stdin masked to stdout, line by line and flushed: the gated push's capture runs it
  control             (the command line) a planted write and a planted capture read masked and a clean line unchanged; counts alone printed

The repository and its folder are read at run time from tools/standing/act.py's REPOS['pp'] beside this file, loaded by its path (no entry
is made on sys.path), and never typed; where the parent is a volume's root, the folder's mask is empty and the repository's alone stands.
An archive's shape is b769's search shape (data/b769_events_postseal.txt :110): an upper-case run of 16 or more letters, digits or
underscores ending in .zip. No archive's name and no folder's name is typed here. The writers (v1.38.32): the record template's put_json,
put_txt and its gate banks; the checks template's rec, its part bank, its lsr bank and its exercise bank; the closing template's census
banks and its record; tools/standing/prevdry.py's bank and prints; tools/standing/components.py's lists and bank; tools/standing/hook.py's
refusal row; tools/push_gated.sh's capture.
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROLE = '<the-papers-repository>'
FOLDER_ROLE = '<the-papers-repository-folder>'
ARCHIVE_ROLE = '<an-archive-of-R379-4d>'
ARCHIVE = re.compile(r'(?<![A-Za-z0-9_])[A-Z0-9_]{16,}\.zip(?![A-Za-z0-9_])')
_KINDS = []


def _act():
    sp = importlib.util.spec_from_file_location('_hostmask_act', os.path.join(HERE, 'act.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def forms(p):
    """a path's spellings: forward and back slashes, back slashes doubled (a json string), and git bash's /d/... form; longest first."""
    p = p.replace('\\', '/').rstrip('/')
    out = {p, p.replace('/', '\\'), p.replace('/', '\\\\')}
    if len(p) > 2 and p[1] == ':':
        out.add('/' + p[0] + p[2:])
    return sorted(out, key=len, reverse=True)


def paths():
    """(the papers` repository's path, its parent folder or None where the parent is a volume's root)."""
    pp = os.path.normpath(_act().REPOS['pp'])
    par = os.path.dirname(pp)
    return pp, (par if len(par.replace('\\', '/').rstrip('/')) > 2 else None)


def kinds():
    if not _KINDS:
        pp, par = paths()
        k = [(re.compile(re.escape(f), re.I), REPO_ROLE) for f in forms(pp)]
        if par:
            k += [(re.compile(re.escape(f), re.I), FOLDER_ROLE) for f in forms(par)]
            k.append((re.compile(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])' % re.escape(os.path.basename(par)), re.I), FOLDER_ROLE))
        k.append((ARCHIVE, ARCHIVE_ROLE))
        _KINDS.extend(k)
    return _KINDS


def _masked(s):
    n = 0
    for p, role in kinds():
        s, k = p.subn(lambda _m, r=role: r, s)
        n += k
    return s, n


def mask(s):
    return _masked(s)[0] if isinstance(s, str) else s


def count(s):
    return _masked(s)[1] if isinstance(s, str) else 0


def mask_lines(lines):
    if isinstance(lines, str):
        return mask(lines)
    return [mask(l) for l in lines]


def mask_list(items):
    """a list of paths masked, each distinct archive's name given its own numbered role ('-1-of-2', '-2-of-2' in order of first
    appearance), so a composer that merges equal entries keeps two archives two (b769's composer read 21 for 22 under one role,
    data/b769_events_postseal.txt :829-:833); every other form masked as mask() does."""
    names = []
    for x in items:
        for n in (ARCHIVE.findall(x) if isinstance(x, str) else ()):
            if n not in names:
                names.append(n)
    out = []
    for x in items:
        if isinstance(x, str):
            for i, n in enumerate(names):
                x = x.replace(n, '%s-%d-of-%d>' % (ARCHIVE_ROLE[:-1], i + 1, len(names)))
        out.append(mask(x))
    return out


def mask_obj(o):
    if isinstance(o, str):
        return mask(o)
    if isinstance(o, dict):
        return dict((mask(k), mask_obj(v)) for k, v in o.items())
    if isinstance(o, (list, tuple)):
        return [mask_obj(x) for x in o]
    return o


def write_text(p, text):
    b = mask(text).encode('utf-8')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    return p


def filter_stream(inp=None, out=None):
    inp = inp or sys.stdin.buffer
    out = out or sys.stdout.buffer
    for raw in iter(inp.readline, b''):
        try:
            out.write(mask(raw.decode('utf-8', 'replace')).encode('utf-8'))
        except Exception:  # noqa: BLE001  ### the capture never stops on the mask
            out.write(raw)
        out.flush()


def control():
    """a planted write through write_text and a planted capture through this file's filter in a child process, each read back; counts."""
    import subprocess
    import tempfile
    pp, par = paths()
    if not par:
        return False, 'the parent of the papers` repository is a volume`s root: no folder to mask, the control not run'
    arch = 'ZZ_PLANTED_ARCHIVE_OF_THE_CONTROL_01.zip'
    planted = 'a planted bank line: %s ; %s ; %s ; %s ; %s' % (pp, par.replace('\\', '/'), os.path.basename(par).upper(), arch,
                                                              forms(par)[-1].replace('\\', '\\\\'))
    clean = 'a clean line: data/b770_events.txt at relay HEAD'
    d = tempfile.mkdtemp(prefix='hostmask_')
    try:
        p = write_text(os.path.join(d, 'planted.txt'), planted + '\n' + clean + '\n')
        back = open(p, encoding='utf-8').read()
    finally:
        for f in os.listdir(d):
            os.remove(os.path.join(d, f))
        os.rmdir(d)
    cap = 'push_gated: repo %s ; branch push-b770-planted\n%s\n' % (pp, clean)
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.abspath(__file__), 'filter'], input=cap.encode('utf-8'), capture_output=True)
    got = r.stdout.decode('utf-8', 'replace')
    ok = (count(planted) >= 5 and count(back) == 0 and FOLDER_ROLE in back and REPO_ROLE in back and ARCHIVE_ROLE in back
          and back.split('\n')[1] == clean and count(cap) >= 1 and count(got) == 0 and REPO_ROLE in got and got.split('\n')[1] == clean
          and r.returncode == 0)
    return ok, ('the planted write: %d before, %d after, its roles %s ; the planted capture: %d before, %d after the filter (exit %d) ; a clean '
                'line unchanged %s' % (count(planted), count(back), all(x in back for x in (FOLDER_ROLE, REPO_ROLE, ARCHIVE_ROLE)), count(cap),
                                       count(got), r.returncode, back.split('\n')[1] == clean and got.split('\n')[1] == clean))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['filter']:
        filter_stream()
    elif a[:1] == ['control']:
        ok_, why_ = control()
        print('### hostmask.py control ((R380)(8) [K32]): %s -> %s' % (why_, 'AS WANTED' if ok_ else 'NOT AS WANTED'))
        sys.exit(0 if ok_ else 1)
    else:
        sys.exit(__doc__)
