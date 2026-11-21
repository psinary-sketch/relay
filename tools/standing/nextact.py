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

v1.38.3, (R374)(5) [K8], b763 events (100) and (103), b762 events (22) (the class of (R372)(11)): THE ANSWER IN THE NEXT, CARRIED-TO AND
RESOLVED LINES. Three faults, one class. (i) line() returned a text opening with HEAD as it stood, "so the line read twice is read once"; an
act's own next_line() opens with HEAD and a clause cite (b763's "... (the answers bank) ((R373)(13)): one act of ..."), so the answer and
the bank were never put in it: b762's and b763's entries and trails listed the ruling's options beside an answers bank that held the
author's choice (b763's :8, read at 12:09:12Z, the entry composed at 12:11:13Z). From here a text opening with HEAD is returned as it
stands only where it already carries the bank's path with the answer that word() finds; otherwise HEAD and its cite are kept and the bank,
the answer and the act's words as put follow, as for any other text. (ii) the entry's "**Carried to:**" line was read by nothing here;
carried_to() puts the next act, PHRASE, the bank and the answer before the line as composed, where word() finds an answer, and leaves it as
composed where none. (iii) the trail's "**Next:**" line was composed from the act's next_line() and read by nothing here (the entry's wrap
at record.tpl's foot read the entry alone); trail() reads it through line(), the template binding it over the trail's composition. And
count_word(): the Resolved line's item "the <n> navigator misses" took num_word(0), "none", the word for no count, where its words want a
count (b763's item (14)); from b764 a count of 0 reads "zero", before it num_word's word as landed.

  carried_to(act, text, data) -> the Carried-to line's body     trail(act, text, data) -> the trail with its Next line read through line()
  count_word(n, act, nw) -> the Resolved line's count word (nw the record's num_word)

v1.38.19, (R375)(8) [K20], b764's post-seal row (78) (data/b764_events_postseal.txt :82): THE ROOT'S ANSWER IN THE AUTHOR'S WORDS. word()
took an answer only where an author's word said "<next act> is", or where the RESULT of a prompt headed with the next act did not open with
BEGIN; b764's root answer opened with BEGIN and named the next act as "The act after b764", so word() returned None and the entry's
Carried-to and Next lines and the trail's Next line stood as composed beside a bank that held the answer. From here word() reads, in this
order: (1) a line of an author's word saying "<next act> is", as before; (2) a prompt headed with the next act: an answer chosen among the
options as before ("the author chose: ..."), and an answer given in the author's words between BEGIN and END, taken as "the author answered
in words: " with its first sentence and, where a later sentence names the next act (by its name, or as "the act after <act>"), that
sentence beside it (begin_answer()); (3) a line of an author's word that names the next act as "the act after <act>" with no "<next act>
is". The prompt is read before (3), so the root's answer stands before a word that only mentions the act after.

  begin_answer(ans, act) -> the words word() takes from an answer given between BEGIN and END, or None
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
CARRIED_LINE = re.compile(r'^(\*\*Carried to:\*\* ?)(.*)$')       # ### v1.38.3, [K8] (ii): the entry's Carried-to line
HEAD_CITE = re.compile(r'^\s*(\(\(R\d{3}\)(?:\([^()]*\))*\))?\s*:?\s*')   # ### v1.38.3, [K8] (i): the clause cite an act puts after HEAD
COUNT_FROM = 764   # ### v1.38.3, [K8]: the first act whose Resolved line reads a count of 0 as "zero"


def _next(act):
    return 'b%d' % (int(act[1:]) + 1)


def _names_next(s, act):
    """v1.38.19, [K20]: a sentence names the act that follows by its name or as "the act after <act>"."""
    return bool(re.search(r'\b%s\b' % _next(act), s) or re.search(r'(?i)\bthe act after %s\b' % act, s))


def begin_answer(ans, act):
    """v1.38.19, [K20]: an answer given in the author's words between BEGIN and END (a RESULT line holds it with its line breaks taken out,
    so a sentence may follow a full stop with no space): its sentences, the first kept and, where a later one names the act that follows,
    that one beside it; None where it holds no words."""
    t = ans[len('BEGIN'):] if ans.startswith('BEGIN') else ans
    t = (t[:-len('END')] if t.endswith('END') else t).strip()
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s*(?=[A-Z(])', t) if s.strip()]
    if not sents:
        return None
    named = next((s for s in sents[1:] if _names_next(s, act)), None)
    return 'the author answered in words: %s' % (sents[0] + (' ' + named if named else ''))


def word(act, data=D):
    p = os.path.join(data, '%s_author_answers.txt' % act)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8', errors='replace') as f:
        L = f.read().replace('\r', '').split('\n')
    nx = _next(act)
    head = False
    after = None   # ### v1.38.19, [K20] (3): the first word line naming "the act after <act>", read after the prompts
    for i, l in enumerate(L):
        if l.startswith('### THE AUTHOR`S WORD'):
            head = True
            continue
        if head and l.strip() and re.search(r'\b%s is\b' % nx, l):
            return i + 1, l.strip()
        if head and l.strip() and after is None and re.search(r'(?i)\bthe act after %s\b' % act, l):
            after = (i + 1, l.strip())
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
            b = begin_answer(ans, act)   # ### v1.38.19, [K20] (2): the answer in the author's words, before (3)
            if b:
                return i + 1, b
            prompt = None
    return after


def line(act, text='', data=D):
    """v1.34.7, (R366)(1)(i): the line for the act that follows: HEAD (PHRASE), the answers bank by its path, the answer's line and words
    where word() finds one naming the next act, then <text> -- the act's own words for the question as put -- unedited. v1.38.3, [K8] (i):
    a text opening with HEAD is returned as it stands only where it already carries the bank and the answer word() finds, so the line read
    twice is read once; a text opening with HEAD without them keeps HEAD and its clause cite, the bank and the answer put after them."""
    t = (text or '').strip()
    w = word(act, data)
    where = 'relay data/%s_author_answers.txt%s' % (act, (' :%d, %s' % w) if w else '')
    head = HEAD
    if t.startswith(HEAD):
        if where in t:
            return t
        m = HEAD_CITE.match(t[len(HEAD):])
        head = HEAD + ((' ' + m.group(1)) if m.group(1) else '')
        t = t[len(HEAD) + m.end():].strip()
    return '%s: %s; as put: %s' % (head, where, t) if t else '%s: %s' % (head, where)


def carried_to(act, text, data=D):
    """v1.38.3, [K8] (ii): the Carried-to line's body: where word() finds an answer naming the next act, the next act, PHRASE, the bank by
    its path with the answer's line and words, then the line as composed; where none, the line as composed. Read twice, read once."""
    t = (text or '').strip()
    w = word(act, data)
    if not w:
        return t
    where = 'relay data/%s_author_answers.txt :%d, %s' % (act, w[0], w[1])
    if where in t:
        return t
    return '%s %s: %s; as put: %s' % (_next(act), PHRASE, where, t)


def count_word(n, act, nw):
    """v1.38.3, [K8]: the Resolved line's count word: from b764 a count of 0 reads "zero" (num_word's "none" is the word for no count);
    every other count, and every count before b764, num_word's word, as landed."""
    try:
        an = int(str(act).lstrip('b'))
    except ValueError:
        an = 0
    return 'zero' if n == 0 and an >= COUNT_FROM else nw(n)


def entry(act, text, data=D):
    """v1.34.7, (R366)(1)(i): the entry with each line opening "**Next.**" or "**Next:**" read through line(), its closing full stop kept;
    every other line as composed."""
    out = []
    for l in (text or '').split('\n'):
        m = NEXT_LINE.match(l)
        c = None if m else CARRIED_LINE.match(l)   # ### v1.38.3, [K8] (ii): the Carried-to line read through carried_to()
        if m:
            body = m.group(2).rstrip()
            stop = body.endswith('.')
            l = m.group(1) + line(act, body[:-1] if stop else body, data) + ('.' if stop else '')
        elif c:
            l = c.group(1) + carried_to(act, c.group(2).rstrip(), data)
        out.append(l)
    return '\n'.join(out)


def trail(act, text, data=D):
    """v1.38.3, [K8] (iii): the trail with its "**Next:**" line read through line(), its full stop kept; every other line as composed (the
    trail holds no Carried-to line). Bound over the trail's composition at tools/standing/fold/record.tpl's foot, after the ledgers' wrap."""
    return entry(act, text, data)


def carried(act, items, data=D):
    """v1.34.7, (R366)(1)(i): item (a) read through line() -- PHRASE and the bank always, the answer where word() finds one, then the
    module's words for the question as put, its following lines kept. Before v1.34.7 the module's item stood as written where word() found
    no answer, and was replaced by the answer alone where it found one."""
    out = []
    for l in items:
        m = ITEM_A.match(l) if l.startswith('    (a) ') else None
        out.append('    (a) ### **THE NEXT**: %s' % line(act, m.group(1), data) if m else l)
    return out
