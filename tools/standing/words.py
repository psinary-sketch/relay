# -*- coding: utf-8 -*-
"""standing/words.py -- THE AUTHOR'S WORDS, READ BY THEIR HEADS ((R326)(3)(iv)-(v) of the registrations act; events (3), (4) and (6) of the
toolset act).

(iv) THE ANSWERS ROUTE READS EVERY WORD. An answers bank's RESULT rows (each from its "RESULT (transcript line N, <time>):" line to the
harness's tail that closes the answer) carry the author's word between BEGIN and END wherever it stands -- after the answer's `="`, or inside an option's notes
after a preview, as the toolset act's word (2) arrived. Each word is written as a "## (n)" head with its time and transcript line, the word
verbatim beneath it, and the words are read back by those heads alone; a line opening "## (" that is not a well-formed head in sequence is
refused with its line. Provenance: tools/b698_record.py's answers route (:321) matched a word at the answer's start or after `="` and read
three of the toolset act's four.
(v) A WORD AFTER A SEALED COMPOSITION. A clause a sealed tool composed (the entry's, the trail's) is printed beside every word received
after the composition's time, read from the words' heads; a word received before it is not printed. Provenance: the toolset act's entry
and trail landed clauses its sealed record tool composed before the root word that ruled them.

  results(answers) -> [dict(line, transcript, at, text)]     word_of(text) -> str or None
  heads_text(words) -> str                                   read_heads(text) -> dict(words [dict(n, at, transcript, word)], refused)
  after(words, at) -> [word]                                 beside(clauses, words, at) -> [str]
"""
import re

RESULT = re.compile(r'^RESULT \(transcript line (\d+), ([0-9T:.\-]+Z)\):')
HEAD_LINE = re.compile(r'^## \((\d+)\) (\S+Z), transcript line (\d+)\s*$')
HEAD_START = re.compile(r'^## \(')
TAIL = ' Read the answers carefully'


def results(answers):
    """the RESULT rows of an answers bank, each with its own line, its transcript line, its time and its text to the next '### ' row."""
    L = (answers or '').replace('\r', '').split('\n')
    out, i = [], 0
    while i < len(L):
        m = RESULT.match(L[i])
        if not m:
            i += 1
            continue
        # the row runs to the harness's tail, which closes every answer; a quoted question carries "### " lines of its own (the toolset
        # act's root prompt quoted its FINDINGS line), so a "### " line ends the row only where no tail follows before the next RESULT
        j = i
        while j < len(L) and TAIL not in L[j] and not (j > i and RESULT.match(L[j])):
            j += 1
        if j < len(L) and TAIL in L[j]:
            j += 1
        else:
            j = i + 1
            while j < len(L) and not L[j].startswith('### ') and not RESULT.match(L[j]):
                j += 1
        out.append(dict(line=i + 1, transcript=int(m.group(1)), at=m.group(2), text='\n'.join(L[i:j]).rstrip()))
        i = j
    return out


def word_of(text):
    """the author's word in a RESULT's text: from its first BEGIN to the last END before the harness's tail, wherever the word stands."""
    t = text or ''
    b = t.find('BEGIN')
    if b < 0:
        return None
    k = t.find(TAIL)
    e = t.rfind('END', b + 5, k if k >= 0 else len(t))
    return t[b + 5:e] if e > b else None


def words(answers):
    """[dict(at, transcript, word)] for every RESULT carrying a word."""
    out = []
    for r in results(answers):
        w = word_of(r['text'])
        if w is not None:
            out.append(dict(at=r['at'], transcript=r['transcript'], word=w))
    return out


def heads_text(ws):
    """the words written as "## (n) <time>, transcript line <N>" heads, each word verbatim beneath its head."""
    L = []
    for n, w in enumerate(ws, 1):
        L += ['## (%d) %s, transcript line %d' % (n, w['at'], w['transcript']), w['word'], '']
    return '\n'.join(L)


def read_heads(text):
    """the words read back by their heads alone: each "## (n)" head well formed and in sequence, its word the lines beneath it to the next
    head. A line opening "## (" that is not a well-formed head, or a head out of sequence, is refused with its line."""
    L = (text or '').replace('\r', '').split('\n')
    ws, refused, cur = [], [], None
    for i, l in enumerate(L, 1):
        if HEAD_START.match(l):
            m = HEAD_LINE.match(l)
            if not m:
                refused.append((i, l, 'not a well-formed head'))
                cur = None
                continue
            if int(m.group(1)) != len(ws) + 1:
                refused.append((i, l, 'out of sequence: (%d) after %d head(s)' % (int(m.group(1)), len(ws))))
                cur = None
                continue
            cur = dict(n=int(m.group(1)), at=m.group(2), transcript=int(m.group(3)), word=[])
            ws.append(cur)
        elif cur is not None:
            cur['word'].append(l)
    for w in ws:
        w['word'] = '\n'.join(w['word']).strip('\n')
    return dict(words=ws, refused=refused)


def after(ws, at):
    """the words received after a composition's time `at` (ISO times compared to the second)."""
    return [w for w in ws if w['at'][:19] > (at or '')[:19]]


def beside(clauses, ws, at):
    """each clause a sealed tool composed at `at`, printed with every word received after it beside it."""
    late = after(ws, at)
    out = []
    for c in clauses:
        out.append('  THE CLAUSE (composed %s): %s' % (at, c))
        if not late:
            out.append('      no word received after its composition')
        for w in late:
            out.append('      THE AUTHOR`S WORD RECEIVED AFTER IT (%s, transcript line %d): %s' % (w['at'], w['transcript'], w['word'][:300]))
    return out
