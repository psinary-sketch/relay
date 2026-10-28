# -*- coding: utf-8 -*-
"""standing/manifest.py -- THE MIRROR'S MANIFEST CONTROL READING EACH FILE THE ACT EDITS AGAINST HEAD (v1.2.0; (R328)(7), b717's event
(10), the class CONTROL). The control's files are the PLACE-papers files the act's own commits changed (from the act's base to the head
the mirror was built at, read from git), and its reference is that head: each file the roster carries must stand in the zip at that
head's bytes (compared raw and with CR removed, the builder copying working files, autocrlf's trap). A carried reference is not read.
Provenance: b716's control compared day1/Silence_of_Foundations.md against b716's merge a86c9429, carried into b717 unchanged; b717's C5
edited the file on main (84dbbf3e), so the control read NOT AS WANTED while the zip's entry stood at the file's bytes at HEAD (b716's
event (17), b717's event (10)).

  edited(base, head, repo='pp') -> [paths]       member(names, path) -> [zip entries]
  control(zip_path, base, head, repo='pp') -> dict(rows, ok, head, files)
  control_at_build(zip_path, build, repo='pp') -> control over every roster file at `build` (v1.2.1, (R331)(2)(iii)); the record tool's
  mbank route calls it, the repair of v1.2.0 never having reached that route (b720's event (15))
"""
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

NL = '\n'


def edited(base, head, repo='pp'):
    out = A.gs(repo, 'diff', '--name-only', base, head)
    return sorted(p for p in (out or '').split(NL) if p.strip())


def member(names, path):
    """the zip's entries for a path: by its path, else the builder's `<parent>__<name>` form, else its flat name (the builder's); v1.2.1:
    the first form that finds an entry, so a root README.md and an archive's flattened README each find their own (b720's zip, read at
    its build commit by control_at_build)."""
    base = path.split('/')[-1]
    parent = path.split('/')[-2] if '/' in path else ''
    for want in (lambda n: n == path, lambda n: bool(parent) and n == parent + '__' + base, lambda n: n == base):
        got = [n for n in names if want(n)]
        if got:
            return got
    return []


def control(zip_path, base, head, repo='pp', files=None, ref=None):
    """each file the act edited (base..head) that the zip carries, its entry against the blob at `ref` (default `head`). Files the zip does
    not carry are listed NOT IN THE ROSTER and not failed. Returns dict(rows [(path, entries, raw_equal, lf_equal, state)], ok, head)."""
    z = zipfile.ZipFile(zip_path)
    names = [n for n in z.namelist() if n != 'MANIFEST.md']
    man = z.read('MANIFEST.md').decode('utf-8-sig', 'replace') if 'MANIFEST.md' in z.namelist() else ''
    ref = ref or head
    rows = []
    for p in (files if files is not None else edited(base, head, repo)):
        mem = member(names, p)
        if not mem:
            rows.append((p, [], None, None, 'NOT IN THE ROSTER'))
            continue
        b = A.blob(ref, p, repo) or b''
        zb = z.read(mem[0]) if len(mem) == 1 else b''
        raw_eq = bool(zb) and zb == b
        lf_eq = bool(zb) and zb.replace(b'\r', b'') == b.replace(b'\r', b'')
        listed = p.split('/')[-1] in man
        rows.append((p, mem, raw_eq, lf_eq, 'AS WANTED' if (len(mem) == 1 and lf_eq and listed) else 'NOT AS WANTED'))
    return dict(rows=rows, ok=all(r[4] != 'NOT AS WANTED' for r in rows) and any(r[4] == 'AS WANTED' for r in rows), head=head, ref=ref)


def control_at_build(zip_path, build, repo='pp', files=None):
    """v1.2.1 ((R331)(2)(iii), b720's event (15)): every file of the roster the builder read at `build` -- the commit the mirror is built at,
    the source head its MANIFEST declares -- read in the zip against its blob at `build`; never a carried reference and not only the files
    the act edited. The record tool's mirror bank calls this (its mbank route), so the repair reaches the route that writes the bank."""
    import roster as RO
    return control(zip_path, None, build, repo, files=RO.roster_at(build) if files is None else files, ref=build)
