# -*- coding: utf-8 -*-
"""standing/delread.py -- v1.30.0, (R360)(3)(xii), b749 defect (n): THE CAPTURE'S DELETE READER TAUGHT THE TOOL'S ROUTE.

v1.29.0 gave the one-call tool its branch-delete route (`commit.py <repo> delete <branch>`) and left the capture's reader, b698's delete_shape
(tools/b698_record.py :1084), reading `git branch -d` and `git push origin --delete` alone, every quoted string unquoted first: b749's five
step-zero deletes through the tool read as none ("BRANCH DELETES OF ONE BRANCH ... 0 OF 0"), and two one-line programs quoting a delete in
their test strings read as deletes with a glob. Here a command is read segment by segment (split at && || ; outside quotes): a segment
running git is read as b698 read it (its quoted names unquoted); a segment running tools/standing/commit.py with the word delete names the
one branch after it; any other segment -- an interpreter program, an echo -- names nothing, its quoted text a string and not a command.
(tools/standing/deletes.py is the --merged listing's route, v1.15.0; this module reads the capture.)

  delete_shape(cmd) -> (names, globs, variables)      chained_after(cmd) -> bool      b698's signatures
"""
import re

QUOTED = re.compile(r'"(?:[^"\\`]|[\\`].)*"|\'[^\']*\'')
SHELL_VAR = re.compile(r'\$\{?\w+\}?|%\w+%')
SPLIT = re.compile(r'&&|\|\||;')
GIT_DEL = re.compile(r'^\s*git\s+(?:-C\s+\S+\s+)?(?:branch\s+(?:-[dD]|--delete)\s+((?:[^\s&;|]+\s*)+)|push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+))')
TOOL_DEL = re.compile(r'^\s*python\S*\s+(?:\S+\s+)*?\S*tools[/\\]standing[/\\]commit\.py\s+(\S+)\s+delete\s+(\S+)\s*$')


def segments(cmd):
    """the command's segments split at && || ; outside quotes, each its own text (quotes kept), a leading `cd <dir>` its own segment."""
    out, cur, i, n = [], [], 0, len(cmd or '')
    while i < n:
        m = QUOTED.match(cmd, i)
        if m:
            cur.append(m.group(0))
            i = m.end()
            continue
        s = SPLIT.match(cmd, i)
        if s:
            out.append(''.join(cur))
            cur = []
            i = s.end()
            continue
        cur.append(cmd[i])
        i += 1
    out.append(''.join(cur))
    return [x for x in out if x.strip()]


def delete_shape(cmd):
    names, globs, vs = [], [], []
    for seg in segments(cmd or ''):
        t = TOOL_DEL.match(seg)
        if t:
            b = t.group(2).strip('\'"')
            names.append(b)
            globs += [ch for ch in '*?[' if ch in b]
            vs += SHELL_VAR.findall(b)
            continue
        if not re.match(r'^\s*git\b', seg):
            continue   # ### an interpreter program, an echo, a listing: its quoted text is a string, not a delete
        c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), seg)
        g = GIT_DEL.match(c)
        if g:
            got = (g.group(1) or g.group(2) or '').split()
            names += got
            globs += [ch for ch in '*?[' if ch in SHELL_VAR.sub('', ' '.join(got))]
            vs += SHELL_VAR.findall(' '.join(got))
    return names, sorted(set(globs)), vs


def chained_after(cmd):
    """anything chained after a delete segment in the same command (`;`, `&&`, `||`, `|`), read outside quoted strings."""
    segs = segments(cmd or '')
    for k, seg in enumerate(segs):
        if delete_shape(seg)[0]:
            return k < len(segs) - 1 or bool(re.search(r'\|', QUOTED.sub('""', seg)))
    return False
