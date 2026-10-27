# -*- coding: utf-8 -*-
"""standing/allow.py -- AN ARM READS ITS ALLOWANCES FROM THE RULING ((R326)(3)(i) of the registrations act; events (7) and (8) of the
toolset act): the branches an act may delete and the prompts it may put are read from the act's ruling (data/<act>_ferry.txt) and its
author's-words banks, not from floors in an arm's code.

The deletes: every clause of the ruling (a sentence or a semicolon's part) that says a branch is deleted, and does not say NOT deleted,
names its branches; a delete is allowed when its branch's name is among them. A word of the author's that names a deletion adds its
branches the same way. Provenance: the toolset act's G-DELETES-ONE-BRANCH admitted a fixed tuple of names (its NAMED_PUSH), and its two
push branches deleted after the entry's and the pre-root pushes failed it.
The prompts: the ruling's "root's prompt put once" allows one root prompt; every other prompt is allowed when the author's word that
answers it is banked under its "## (n)" head (data/<act>_author_words_preseal.txt, data/<act>_author_words.txt), the k-th prompt by the
k-th head. Provenance: the toolset act's G-ANSWERS-BEFORE-WRITES wanted FLOORS['prompts'] = 1 PROMPT row where the act put four.

  deletes_allowed(ruling, words) -> [names]        prompts_read(answers, ruling, heads) -> dict(rows, allowed, unbanked, ok)
  deletes_read(deleted, ruling, words) -> dict(rows, outside, ok)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

BRANCH = re.compile(r'(?<![\w/.-])((?:push|recut|port|merge)-[A-Za-z0-9][A-Za-z0-9.-]*[A-Za-z0-9])')
NOT_DELETED = re.compile(r'\bNOT\s+deleted\b|\bnot\s+deleted\b|\bnot\s+be\s+deleted\b')
DELETED = re.compile(r'\bdeleted?\b', re.I)
ROOT_ONCE = re.compile(r'root[’\']s prompt put once', re.I)
PROMPT_ROW = re.compile(r'^### PROMPT \d+ \(([^)]*)\):', re.M)
HEAD = re.compile(r'^## \((\d+)\) ', re.M)


def clauses(text):
    """the ruling's text cut at sentence ends and semicolons, each part with its whitespace collapsed."""
    flat = re.sub(r'\s+', ' ', text or '')
    return [c.strip() for c in re.split(r'(?<=[.;])\s+(?=[A-Za-z(])', flat) if c.strip()]


def deletes_allowed(ruling, words=''):
    """the branch names the ruling's delete clauses and the author's words name, in order, each once."""
    out = []
    for c in clauses(ruling) + clauses(words):
        if DELETED.search(c) and not NOT_DELETED.search(c):
            for b in BRANCH.findall(c):
                if b not in out:
                    out.append(b)
    return out


def deletes_kept(ruling, words=''):
    """the branch names a clause says are NOT deleted."""
    out = []
    for c in clauses(ruling) + clauses(words):
        if NOT_DELETED.search(c):
            out += [b for b in BRANCH.findall(c) if b not in out]
    return out


def deletes_read(deleted, ruling, words=''):
    """each delete [(repository, branch)] read against the allowance: allowed where its name is among the ruling's delete names and not
    among the kept. Returns dict(rows [(repo, branch, allowed)], outside [(repo, branch)], allowed names, ok)."""
    allowed, kept = deletes_allowed(ruling, words), deletes_kept(ruling, words)
    rows = [(r, b, b in allowed and b not in kept) for r, b in deleted]
    outside = [(r, b) for r, b, ok in rows if not ok]
    return dict(rows=rows, outside=outside, allowed=allowed, kept=kept, ok=not outside)


def prompts_read(answers, ruling, heads_text):
    """each PROMPT row of an answers bank read against the allowance: a root prompt against the ruling's "put once" (one allowed), every
    other prompt against the author's-words heads, the k-th by the k-th. Returns dict(rows [(label, kind, allowed)], allowed, unbanked, ok)."""
    labels = PROMPT_ROW.findall(answers or '')
    root_allowed = 1 if ROOT_ONCE.search(re.sub(r'\s+', ' ', ruling or '')) else 0
    heads = len(HEAD.findall(heads_text or ''))
    rows, roots, others = [], 0, 0
    for lab in labels:
        if lab.strip().lower().startswith('root'):
            roots += 1
            rows.append((lab, 'root', roots <= root_allowed))
        else:
            others += 1
            rows.append((lab, 'word', others <= heads))
    unbanked = [lab for lab, _k, ok in rows if not ok]
    return dict(rows=rows, allowed=root_allowed + heads, unbanked=unbanked, ok=not unbanked)


def ruling_of(act):
    return A.rd('%s_ferry.txt' % act)


def words_of(act):
    """the author's-words banks of an act, joined: the pre-seal bank and the post-seal bank, each by its "## (n)" heads."""
    return A.rd('%s_author_words_preseal.txt' % act) + '\n' + A.rd('%s_author_words.txt' % act)
