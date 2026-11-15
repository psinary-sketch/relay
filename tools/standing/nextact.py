# -*- coding: utf-8 -*-
"""standing/nextact.py -- v1.21.0, (R351)(2)(vi): THE CLOSING'S CARRIED ITEM FOR THE NEXT ACT, COMPOSED FROM THE AUTHOR'S ANSWERS BANK. b740's closing
:332 printed (R350)(7)'s three choices from the act module's sealed text, where data/b740_author_answers.txt :17 held the author's word naming b741
as (c7) to SP3. Here, where an answer of the act names the next act -- the author's word verbatim (its "### THE AUTHOR`S WORD" section) saying
"<next> is", or a prompt headed with the next act answered by an option -- the carried item (a) is that answer with its bank and line; where none
names it, the module's item stands as written.

v1.34.7, (R366)(1)(i), b755's closing message line 30 (data/b756_events.txt (10), (11)): THE LINE FOR THE ACT THAT FOLLOWS READS "as the author
answers at the root (the answers bank)". An act's entry is composed before the root's answer, and b755's closing carried the module's two routes
where word() found no answer (its root prompt headed "(Next act)", data/b755_author_answers.txt :32). From b756 on the entry's line (each
"**Next.**" or "**Next:**" line the record route lands, tools/standing/fold/record.tpl's findings through entry()) and the closing's item (a)
(carried()) each read PHRASE and the answers bank by its path, the answer's line and words beside it where word() finds one, then the act's own
words for the question as put. word() is unchanged ((R366)(1): "No other repair is ordered here").

  word(act, data) -> (line, text) or None        carried(act, items, data) -> the items with (a) read through line()
  line(act, text, data) -> the line for the act that follows      entry(act, text, data) -> the entry with each Next line read through line()
"""
import os
import re

S = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(os.path.dirname(S)), 'data')
ITEM = re.compile(r"^    \([a-z]'*\) ")   # ### v1.34.0, (R364)(3)(viii): any number of primes
PHRASE = 'as the author answers at the root (the answers bank)'   # ### v1.34.7, (R366)(1)(i): the ruling's words
HEAD = 'the act after this one, ' + PHRASE
NEXT_LINE = re.compile(r'^(\*\*Next[.:]\*\* ?)(.*)$')            # ### v1.34.7: the entry's line for the act that follows, either form
ITEM_A = re.compile(r'^    \(a\) (?:### )?(?:\*\*[^*]*\*\*:? ?)?(.*)$')   # ### v1.34.7: item (a), its bold head (any) apart from its words


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


def line(act, text='', data=D):
    """v1.34.7, (R366)(1)(i): the line for the act that follows: HEAD (PHRASE), the answers bank by its path, the answer's line and words
    where word() finds one naming the next act, then <text> -- the act's own words for the question as put -- unedited. A text already
    opening with HEAD is returned as it stands, so the line read twice is read once."""
    t = (text or '').strip()
    if t.startswith(HEAD):
        return t
    w = word(act, data)
    where = 'relay data/%s_author_answers.txt%s' % (act, (' :%d, %s' % w) if w else '')
    return '%s: %s; as put: %s' % (HEAD, where, t) if t else '%s: %s' % (HEAD, where)


def entry(act, text, data=D):
    """v1.34.7, (R366)(1)(i): the entry with each line opening "**Next.**" or "**Next:**" read through line(), its closing full stop kept;
    every other line as composed."""
    out = []
    for l in (text or '').split('\n'):
        m = NEXT_LINE.match(l)
        if m:
            body = m.group(2).rstrip()
            stop = body.endswith('.')
            l = m.group(1) + line(act, body[:-1] if stop else body, data) + ('.' if stop else '')
        out.append(l)
    return '\n'.join(out)


def carried(act, items, data=D):
    """v1.34.7, (R366)(1)(i): item (a) read through line() -- PHRASE and the bank always, the answer where word() finds one, then the
    module's words for the question as put, its following lines kept. Before v1.34.7 the module's item stood as written where word() found
    no answer, and was replaced by the answer alone where it found one."""
    out = []
    for l in items:
        m = ITEM_A.match(l) if l.startswith('    (a) ') else None
        out.append('    (a) ### **THE NEXT**: %s' % line(act, m.group(1), data) if m else l)
    return out
