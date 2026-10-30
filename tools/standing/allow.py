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

v1.2.0 ((R328)(7), b717's event (2), the class CONTROL): A BRANCH PATTERN READ AS A PATTERN. A ruling's "the push-b716-* branches ...
deleted" names a pattern; v1.1.0's BRANCH dropped the star and read it as the one name `push-b716`, so the act's five deletes by name read
as outside the ruling. The name now keeps its glob tail (`-*` or `*`), and a delete is allowed where its branch matches a delete name or
pattern (fnmatch, case-sensitive) and no kept name or pattern.

v1.5.0 ((R335)(2)(ii), b724's events (9)-(10)): A SHORT NAME READ AFTER ITS FULL ONE, AND THE PLANT'S NEEDLE FROM THE ACT'S OWN FERRY.
A ruling names branches as "push-b724-preroot, -record and -closing": v1.4.0 read the first name alone, so the act's deletes of the other two
read outside (b724 wrote the short forms out in its own module, a hand-kept regex). `names_in` reads each short tail (`-word` after a comma or
"and", directly after a full name or another tail) as the full name's prefix with that word. And G-DELETES-ONE-BRANCH's plant replaced a
hand-kept sentence ("the push-<prev>-* branches of relay and PLACE-papers deleted by name") that b724's ferry did not carry, so the plant
changed nothing and the seal refused: `delete_clause` locates the ruling's delete clause by the branch names it must carry, and
`plant_kept` turns that clause's "deleted" into "kept"; where no clause carries them it returns None, and the plant then changes nothing
(the arm's positive control read DEFECTIVE, never a silent pass of a plant that was placed).

  deletes_allowed(ruling, words) -> [names]        prompts_read(answers, ruling, heads) -> dict(rows, allowed, unbanked, ok)
  deletes_read(deleted, ruling, words) -> dict(rows, outside, ok)
  names_in(clause) -> [names]   delete_clause(ruling, must) -> clause or ''   plant_kept(ruling, must) -> the ruling, whitespace collapsed, with
  that clause's "deleted" read "kept", or None
"""
import fnmatch
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

BRANCH = re.compile(r'(?<![\w/.-])((?:push|recut|port|merge)-[A-Za-z0-9][A-Za-z0-9.-]*[A-Za-z0-9](?:-\*|\*)?)')
BRANCH_V110 = re.compile(r'(?<![\w/.-])((?:push|recut|port|merge)-[A-Za-z0-9][A-Za-z0-9.-]*[A-Za-z0-9])')   # v1.1.0's, for the control
NOT_DELETED = re.compile(r'\bNOT\s+deleted\b|\bnot\s+deleted\b|\bnot\s+be\s+deleted\b')
DELETED = re.compile(r'\bdeleted?\b', re.I)
ROOT_ONCE = re.compile(r'root[’\']s prompt put once', re.I)
PROMPT_ROW = re.compile(r'^### PROMPT \d+ \(([^)]*)\):', re.M)
HEAD = re.compile(r'^## \((\d+)\) ', re.M)


def clauses(text):
    """the ruling's text cut at sentence ends and semicolons, each part with its whitespace collapsed."""
    flat = re.sub(r'\s+', ' ', text or '')
    return [c.strip() for c in re.split(r'(?<=[.;])\s+(?=[A-Za-z(])', flat) if c.strip()]


TAIL = re.compile(r'(?:,\s*(?:and\s+)?|\s+and\s+)-([A-Za-z0-9][A-Za-z0-9.]*[A-Za-z0-9]|[A-Za-z0-9])(?![\w*-])')


def names_in(clause, pattern=BRANCH):
    """v1.5.0: the branch names of a clause, each short tail after a full name read as that name's prefix with the tail's word
    ("push-b724-preroot, -record and -closing" -> push-b724-preroot, push-b724-record, push-b724-closing); a pattern (`-*`) takes no tail.
    `pattern` BRANCH_V110 reads no tails, as v1.1.0 did."""
    out = []
    for m in pattern.finditer(clause):
        b = m.group(1)
        out.append(b)
        if pattern is BRANCH_V110 or b.endswith('*') or '-' not in b:
            continue
        pre, i = b.rsplit('-', 1)[0], m.end()
        while True:
            t = TAIL.match(clause, i)
            if not t:
                break
            out.append('%s-%s' % (pre, t.group(1)))
            i = t.end()
    return out


def deletes_allowed(ruling, words='', pattern=BRANCH):
    """the branch names and patterns the ruling's delete clauses and the author's words name, in order, each once."""
    out = []
    for c in clauses(ruling) + clauses(words):
        if DELETED.search(c) and not NOT_DELETED.search(c):
            for b in names_in(c, pattern):
                if b not in out:
                    out.append(b)
    return out


def deletes_kept(ruling, words='', pattern=BRANCH):
    """the branch names and patterns a clause says are NOT deleted."""
    out = []
    for c in clauses(ruling) + clauses(words):
        if NOT_DELETED.search(c):
            out += [b for b in names_in(c, pattern) if b not in out]
    return out


def delete_clause(ruling, must):
    """v1.5.0: the first clause of the ruling that says branches are deleted (and not NOT deleted) and whose names cover every branch in
    `must` (each equal to a name or matched by a pattern of the clause); '' where none does."""
    for c in clauses(ruling):
        if DELETED.search(c) and not NOT_DELETED.search(c):
            ns = names_in(c)
            if must and all(matches(b, ns) for b in must):
                return c
    return ''


def plant_kept(ruling, must):
    """v1.5.0: the plant of G-DELETES-ONE-BRANCH -- the ruling with its whitespace collapsed (the form clauses() reads) and the located
    delete clause's first "deleted" read "kept", so the clause no longer allows its branches; None where no clause carries `must`."""
    c = delete_clause(ruling, must)
    if not c:
        return None
    flat = re.sub(r'\s+', ' ', ruling or '')
    return flat.replace(c, DELETED.sub('kept', c, count=1), 1)


def matches(branch, names):
    """the branch is one of `names`, each a name or a glob pattern (v1.2.0)."""
    return any(branch == n or fnmatch.fnmatchcase(branch, n) for n in names)


def deletes_read(deleted, ruling, words='', pattern=BRANCH):
    """each delete [(repository, branch)] read against the allowance: allowed where its branch matches a delete name or pattern of the
    ruling and no kept one. Returns dict(rows [(repo, branch, allowed)], outside [(repo, branch)], allowed names, ok). `pattern`
    BRANCH_V110 reads as v1.1.0 did (the control's record instance)."""
    allowed, kept = deletes_allowed(ruling, words, pattern), deletes_kept(ruling, words, pattern)
    if pattern is BRANCH_V110:
        rows = [(r, b, b in allowed and b not in kept) for r, b in deleted]
    else:
        rows = [(r, b, matches(b, allowed) and not matches(b, kept)) for r, b in deleted]
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
