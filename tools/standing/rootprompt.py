# -*- coding: utf-8 -*-
"""standing/rootprompt.py -- v1.10.0, (R340)(2)(vii): THE ROOT'S PROMPT COMPOSED FROM THE BANKS WITH THE ACT'S OWN OBJECTS; the route carried since b714 retired (b729 event (7)).

The prompt's words are the seat's, in a bank of rows; its figures are not typed: a row is a list of parts, a part a literal string or a cite [bank, line, token], and the
composer prints the token only when the token stands on that line of that bank, and refuses the prompt where one does not. So a prompt cannot carry a figure its bank does not.

  data/<act>_rootprompt_rows.json = {"questions": [{"header": ..., "rows": [[part, ...], ...]}]}
  compose(rows, read) -> text        read(bank, line) -> the line's text, or None; a row's parts joined, the rows joined by one space; SystemExit naming every stale cite
  stale(rows, read) -> [(bank, line, token)]
  ceiling(scores, tracked_at_lock, act, modified) -> (held, of, line)   v1.14.0, (R344)(2)(ii): the ceiling computed as a dry score, never typed: every score that reads REFUTED now, and N4 when a path the suite writes
                                     stood tracked at the lock (the suite's run will read as an edit) or a tracked bank differs from the lock's; PENDING counted as it may yet hold
  rows_from(text, read) -> rows      a text as put, split into rows at its sentences, every number before a cite on the sentence, found on the cited line, turned into a cite
Pure in its arguments; nothing written.
"""
import re

CITE = re.compile(r'\((?:relay )?(data/[\w.\-]+) :(\d+)(?:[,)\- ])')
TOKEN = re.compile(r'\d[\d,.]*\d|\d')


def ceiling(scores, tracked_at_lock, act, modified=()):
    """`modified`: the banks tracked at the lock whose blobs differ from the lock's at prompt time, less the banks the lock excludes by name."""
    import probes as PB
    v = dict((k, (x[0] if isinstance(x, (list, tuple)) else x)) for k, x in scores.items())
    lost = sorted(k for k, x in v.items() if str(x).startswith('REFUTED'))
    if (PB.outputs(act, tracked_at_lock) or modified) and 'N4' in v and 'N4' not in lost:
        lost = sorted(lost + ['N4'])
    return len(v) - len(lost), len(v), 'at most %d of %d (%s REFUTED, by the banks at prompt time)' % (len(v) - len(lost), len(v), ', '.join(lost) or 'none')


def _cites(rows):
    for row in rows:
        for part in row:
            if isinstance(part, (list, tuple)):
                yield part


def stale(rows, read):
    return [tuple(c) for c in _cites(rows) if str(c[2]) not in (read(c[0], int(c[1])) or '')]


def compose(rows, read):
    bad = stale(rows, read)
    if bad:
        raise SystemExit('### THE PROMPT NOT COMPOSED: %d FIGURE(S) NOT ON THEIR BANK LINES: %s' % (len(bad), bad))
    return ' '.join(''.join(str(p[2]) if isinstance(p, (list, tuple)) else p for p in row) for row in rows)


def rows_from(text, read):
    rows = []
    for sent in re.split(r'(?<=[.:]) (?=[A-Z(`])', text):
        cites = [(m.group(1), int(m.group(2)), m.start()) for m in CITE.finditer(sent)]
        parts, at = [], 0
        for bank, line, end in cites:
            on = read(bank, line) or ''
            for m in TOKEN.finditer(sent, at, end):
                if m.group(0) in on:
                    parts += [sent[at:m.start()], [bank, line, m.group(0)]]
                    at = m.end()
        rows.append([p for p in parts + [sent[at:]] if p != ''])
    return rows
