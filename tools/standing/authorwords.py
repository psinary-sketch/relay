# -*- coding: utf-8 -*-
"""standing/authorwords.py -- v1.32.0, (R362)(7)(iv), b751 events (4): THE APPEND KEYED ON WORDS ALONE. b698's answers route
(tools/b698_record.py :337-:341) keeps one row per distinct text: a word of the author word for word an earlier one is dropped. b751's go of
16:47:23Z, the first user line of the continuation session 43048615, is word for word the go of 6151c0de transcript line 20339; the bank carried
one row for the two. A word stands when its place (its transcript line, which fixes its time) and its words both match; two identical words at
two places are two rows. tools/b698_record.py stands outside the act's (W) list, so the repair stands here and the record template's answers route
reads through it.

  author_words(rows, session_id, anchor) -> [(line, text, timestamp)]   every BEGIN..END word, b698's reading, none dropped for its text
  rekey(lines, words) -> (lines, restored)   the composed bank with its word rows re-keyed by place: the rows b698 dropped restored in order
"""
import re

NL = '\n'
WORD = re.compile(r'(?s)(?:\A\s*|="|="\(for the seat, verbatim\):\s*)BEGIN\s*(.*?)\s*END(?=\s*\Z|")')
HEAD = '### THE AUTHOR`S WORD (transcript line %s), BEGIN to END, verbatim:'
HEAD_RE = re.compile(r'^### THE AUTHOR`S WORD \(transcript line ([^)]+)\), BEGIN to END, verbatim:$')
COUNT_RE = re.compile(r'and \d+ word\(s\) of the author')


def author_words(rows, session_id, anchor):
    """b698's word reading (tools/b698_record.py :295-:323) over the same rows (b698's _session_rows), each word with its line and time; the
    text-keyed `seen` of :337-:341 not applied."""
    ask, out = set(), []
    for i, o, _st, sid in rows:
        ln = i if sid == session_id else '%s:%d' % (sid[:8], i)
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        texts = []
        if att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and o.get('type') == 'assistant':
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask and o.get('type') == 'user':
                t = c.get('content')
                texts.append(''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or ''))
        for t in texts:
            for mm in WORD.finditer(t or ''):
                if anchor not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    out.append((ln, mm.group(1), o.get('timestamp')))
    return out


def _word_blocks(lines):
    """the composed bank's word rows: [(start, end)] spans, each a heading through its last text line (the blank after it excluded)."""
    spans, i = [], 0
    while i < len(lines):
        if HEAD_RE.match(lines[i]):
            j = i + 1
            while j < len(lines) and lines[j] != '' and not lines[j].startswith('### '):
                j += 1
            spans.append((i, j))
            i = j
        else:
            i += 1
    return spans


def rekey(lines, words):
    """the composed lines with every word row rebuilt from `words` in order, at the place of the first word row (or before the first NOTE or
    MESSAGE row, or at the end); the head's word count set to the rows written. Returns (lines, restored lines' places)."""
    lines = list(lines)
    spans = _word_blocks(lines)
    had = [HEAD_RE.match(lines[s]).group(1) for s, _e in spans]
    keep, cut = [], set()
    for s, e in spans:
        cut.update(range(s, e + (1 if e < len(lines) and lines[e] == '' else 0)))
    at = spans[0][0] if spans else next((k for k, l in enumerate(lines) if l.startswith(('### NOTE (transcript line', '### THE AUTHOR`S MESSAGE'))), len(lines))
    W = []
    for ln, w, _ts in words:
        W += [HEAD % ln] + w.replace('\r', '').split(NL) + ['']
    for k, l in enumerate(lines):
        if k == at:
            keep += W
        if k not in cut:
            keep.append(l)
    if at >= len(lines):
        keep += W
    if keep and COUNT_RE.search(keep[0]):
        keep[0] = COUNT_RE.sub('and %d word(s) of the author' % len(words), keep[0], count=1)
    restored = [str(ln) for ln, _w, _t in words if str(ln) not in had]
    return keep, restored
