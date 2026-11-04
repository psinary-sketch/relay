# -*- coding: utf-8 -*-
"""standing/nextact.py -- v1.21.0, (R351)(2)(vi): THE CLOSING'S CARRIED ITEM FOR THE NEXT ACT, COMPOSED FROM THE AUTHOR'S ANSWERS BANK. b740's closing
:332 printed (R350)(7)'s three choices from the act module's sealed text, where data/b740_author_answers.txt :17 held the author's word naming b741
as (c7) to SP3. Here, where an answer of the act names the next act -- the author's word verbatim (its "### THE AUTHOR`S WORD" section) saying
"<next> is", or a prompt headed with the next act answered by an option -- the carried item (a) is that answer with its bank and line; where none
names it, the module's item stands as written.

  word(act, data) -> (line, text) or None        carried(act, items, data) -> the items with (a) composed from the answer where one names the next act
"""
import os
import re

S = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(os.path.dirname(S)), 'data')
ITEM = re.compile(r"^    \([a-z]'?\) ")


def _next(act):
    return 'b%d' % (int(act[1:]) + 1)


def word(act, data=D):
    p = os.path.join(data, '%s_author_answers.txt' % act)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8', errors='replace') as f:
        L = f.read().replace('\r', '').split('\n')
    nx = _next(act)
    head = False
    for i, l in enumerate(L):
        if l.startswith('### THE AUTHOR`S WORD'):
            head = True
            continue
        if head and l.strip() and re.search(r'\b%s is\b' % nx, l):
            return i + 1, l.strip()
        if l.startswith('### ') and not l.startswith('### THE AUTHOR`S WORD'):
            head = False
    prompt = None
    for i, l in enumerate(L):
        m = re.match(r'^### PROMPT \d+ \((%s)\): ' % nx, l)
        if m:
            prompt = i
        if prompt is not None and l.startswith('RESULT ') and '"="' in l:
            ans = l.rsplit('"="', 1)[1].rsplit('"', 1)[0]
            if not ans.startswith('BEGIN'):
                return i + 1, 'the author chose: %s' % ans
            prompt = None
    return None


def carried(act, items, data=D):
    w = word(act, data)
    if not w:
        return list(items)
    out, skip = [], False
    for l in items:
        if l.startswith('    (a) '):
            out.append('    (a) ### **THE NEXT, BY THE AUTHOR`S WORD (relay data/%s_author_answers.txt :%d)**: %s' % (act, w[0], w[1]))
            skip = True
            continue
        if skip and not ITEM.match(l) and l.startswith('        '):
            continue
        skip = False
        out.append(l)
    return out
