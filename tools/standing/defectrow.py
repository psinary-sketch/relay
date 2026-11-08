# -*- coding: utf-8 -*-
"""standing/defectrow.py -- v1.28.0, (R358)(3)(vi), b747 defects (u), (x), (l): A DEFECT ROW READ BY ITS LETTER AND TAG; THE SCREENS' FIGURES
FROM THE BANKS AND NOT FROM A ROW'S PROSE.

(u) the record's reader of a row (tools/b703_record.py read_defect_row, and its copy in tools/standing/close.py) took a row's text to its first
full stop followed by a space or the end: a row with no closing full stop read as nothing (17 of b747's 20 rows), and a row was cut at a stop
inside a backtick pair or at the dots of an ellipsis. `head(text)` reads the row by its letter and tag: the text to the first full stop outside a
backtick pair and not one of three dots, or the whole row where there is none; a row the old reader read whole to a plain stop reads the same.
(x), (l) the landing's unread-figure screen fired on the null constant inside a row's prose (the trail's Defects line quotes the rows); the
Defects line is the bank's own prose, not a figure the record composes. `figures_text(text)` is the text the unread-figure screen reads: the
landing's text less its Defects lines; every other screen reads the whole.
"""
import re

ROW = re.compile(r"^\(([a-z]'?)\) ")
TAG = re.compile(r"^\(([a-z]'?)\) THE [A-Z]+(?:'S|S') \[(CLAIM|CLOSE) ; (NEW|REPEAT [^\]]+)\]")


def _cut(s):
    """the index of the first full stop that ends a sentence: followed by a space or the end, outside a backtick pair, not part of '...'."""
    tick = False
    for i, ch in enumerate(s):
        if ch == '`':
            tick = not tick
        elif ch == '.' and not tick:
            nxt = s[i + 1] if i + 1 < len(s) else ''
            prv = s[i - 1] if i else ''
            if (nxt in ('', ' ')) and prv != '.' and nxt != '.':
                return i
    return -1


def head(text):
    """'(x) HEAD' for one row's joined text: by its letter (and tag where it carries one), to its first sentence's stop, or whole."""
    m = ROW.match(text or '')
    if not m:
        return None
    i = _cut(text)
    return text[:i] if i >= 0 else text.rstrip()


def read_defect_row(L, i, row_re):
    """one lettered row of a defects bank, its continuation lines joined, read by head()."""
    j = i + 1
    while j < len(L) and L[j].startswith('    ') and not row_re.match(L[j]) and not L[j].startswith('    ###'):
        j += 1
    return head(' '.join(x.strip() for x in L[i:j]))


def tag_of(text):
    """(letter, CLAIM|CLOSE, NEW|REPEAT ...) of a row, or None where it carries no tag."""
    m = TAG.match(text or '')
    return (m.group(1), m.group(2), m.group(3)) if m else None


def figures_text(text):
    """the landing's text less its Defects lines (the bank's row prose), for the unread-figure screen alone."""
    return '\n'.join(l for l in (text or '').split('\n') if not l.lstrip().startswith('**Defects**'))
