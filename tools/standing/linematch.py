# -*- coding: utf-8 -*-
"""standing/linematch.py -- v1.31.0, (R361)(3)(iv), data/b750_line.txt :31-:32 (the limit of (C)): THE LINE READER'S MATCH.

b750's line tool read the Epstein entries of b745-b748 SYNTHESISED by the cluster alone: [F2]'s dated note stood in a file the cluster row names,
and every entry about the instance read SYNTHESISED, its own finding not matched (the bank's own limit: "whether each entry's own finding is among
those the note names is not tested here"). The reader now matches each entry's findings against the names the keystone's note carries before it
reads SYNTHESISED, and reads CLUSTERED where no name matches.

An entry's findings are the names its heading carries -- a Lean name or a bank's stem, a lower-case word joined by underscores (pc_online,
zq_offline_zero, b750_cq_sign) -- the heading being the entry's own, the nearest "## " line above its INTEGRATION line that is not a corrigendum's.
The note's names are read the same way from its text.

  NAME                              the name's pattern
  names(text) -> [names]            each once, in order
  entry_heading(lines, n) -> (line number, text)   the entry's heading above line n (1-based), a corrigendum's heading skipped
  stage(entry_names, note_names, clustered=True) -> (stage, matched)   SYNTHESISED where a name matches, CLUSTERED where none does
  read(lines, n, note) -> dict(heading, names, matched, stage)
Pure in its arguments.
"""
import re

NAME = re.compile(r'(?<![\w`.-])`?([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`?(?![\w-])')


def names(text):
    out = []
    for m in NAME.finditer(text or ''):
        if m.group(1) not in out:
            out.append(m.group(1))
    return out


def entry_heading(lines, n):
    i = min(n, len(lines)) - 1
    while i >= 0:
        l = lines[i]
        if l.startswith('## ') and not l.startswith('## Corrigendum'):
            return i + 1, l
        i -= 1
    return None, ''


def stage(entry_names, note_names, clustered=True):
    hit = [x for x in entry_names if x in set(note_names)]
    if hit:
        return 'SYNTHESISED', hit
    return ('CLUSTERED' if clustered else 'BANKED'), []


def read(lines, n, note, clustered=True):
    at, head = entry_heading(lines, n)
    nm = names(head)
    st, hit = stage(nm, names(note), clustered)
    return dict(heading=at, names=nm, matched=hit, stage=st)
