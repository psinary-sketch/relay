# -*- coding: utf-8 -*-
"""standing/title.py -- THE LANDED TITLE WHEN THE AUTHOR REWORDS IT (v1.2.1; (R331)(2)(i), b720's events (7) and (9)).

The entry's title as G-FINDINGS-ENTRY and G-ENTRY-TITLE-FORM compare it: the record tool's composition with each change the author's word
orders applied. The word is read from the act's answers bank (data/<act>_author_answers.txt), in its verbatim block (the line opening
"### THE AUTHOR`S WORD" and ending "verbatim:", to the next blank line); a change is a phrase of the form "<old>" reads "<new>" inside it.
Each old phrase must stand in the composition exactly once; a straight apostrophe between a letter and a lower-case letter is written in
the ledger's form (the conversion's), in both phrases. No word, or a word naming no change: the composition unchanged. A change whose old
phrase is not found once: None -- the arm fails; it never guesses.
Provenance: at b720 the author's word (option 3) reworded "the law REFUTED"; the entry landed by the sealed route and its title line was
changed by the Edit tool (FINDINGS :11072), and both arms compared the landed line with the composition alone, failing on the word itself.

  words(answers_text) -> [the verbatim words]
  changes(word) -> [(old, new)]
  landed(composed, answers_text) -> (title or None, notes)
"""
import re

NL = '\n'
WORD_HEAD = re.compile(r'^### THE AUTHOR.S WORD\b.*verbatim:\s*$')
CHANGE = re.compile(r'"([^"]+)" reads "([^"]+)"')
APOS = re.compile(r"(?<=[A-Za-z0-9)])'(?=[a-z])")


def ledger(t):
    """a straight apostrophe between a letter and a lower-case letter, and the conversion's backtick, in the ledger's form."""
    return re.sub(r'(?<=[A-Za-z0-9)])`(?=[a-z])', '’', APOS.sub('’', t))


def words(answers_text):
    out, cur = [], None
    for l in (answers_text or '').replace('\r', '').split(NL):
        if WORD_HEAD.match(l):
            cur = []
            out.append(cur)
            continue
        if cur is not None:
            if not l.strip() or l.startswith('###'):
                cur = None
                continue
            cur.append(l)
    return [NL.join(w) for w in out if w]


def changes(word):
    return [(ledger(a), ledger(b)) for a, b in CHANGE.findall(word or '')]


def landed(composed, answers_text):
    """the title the entry stands under: the composition, with each change of each word applied in order."""
    t, notes = ledger(composed or ''), []
    for w in words(answers_text):
        for old, new in changes(w):
            n = t.count(old)
            if n != 1:
                notes.append('the old phrase %r found %d times in the composition, not once' % (old, n))
                return None, notes
            t = t.replace(old, new)
            notes.append('%r -> %r' % (old, new))
    return t, notes or ['no change ordered: the composition']
