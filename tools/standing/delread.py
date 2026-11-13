# -*- coding: utf-8 -*-
"""standing/delread.py -- v1.30.0, (R360)(3)(xii), b749 defect (n): THE CAPTURE'S DELETE READER TAUGHT THE TOOL'S ROUTE.

v1.29.0 gave the one-call tool its branch-delete route (`commit.py <repo> delete <branch>`) and left the capture's reader, b698's delete_shape
(tools/b698_record.py :1084), reading `git branch -d` and `git push origin --delete` alone, every quoted string unquoted first: b749's five
step-zero deletes through the tool read as none ("BRANCH DELETES OF ONE BRANCH ... 0 OF 0"), and two one-line programs quoting a delete in
their test strings read as deletes with a glob. Here a command is read segment by segment (split at && || ; outside quotes): a segment
running git is read as b698 read it (its quoted names unquoted); a segment running tools/standing/commit.py with the word delete names the
one branch after it; any other segment -- an interpreter program, an echo -- names nothing, its quoted text a string and not a command.
(tools/standing/deletes.py is the --merged listing's route, v1.15.0; this module reads the capture.)

v1.34.0, (R364)(3)(xii), b753 defect (u'): A RUN OF THE TOOL READ THROUGH THE ONE MATCHER. v1.30.0's TOOL_DEL took a segment opening on
`python` alone, so PowerShell's quoted interpreter (`& "...python.exe" ... commit.py relay delete <branch>`) read as no delete: b753's five
step-zero deletes, all in that form, read as none, and G-BRANCHES-BANKED, G-LISTINGS-BEFORE-CLAUSES and G-DELETES-ONE-BRANCH failed on it.
The commit tool and the hook had taken that form since b753's (i) through tools/standing/gitwrite.py's RUNS_COMMIT; this reader now asks
the same matcher, imported and not copied, whether a segment runs the tool (its quoted strings blanked as gitwrite blanks them), and reads
`<repo> delete <branch>` after the tool's path from the segment's own text.

  delete_shape(cmd) -> (names, globs, variables)      chained_after(cmd) -> bool      b698's signatures
  tool_delete(segment) -> (repo, branch) or None       a run of the one-call tool's delete route, by gitwrite's RUNS_COMMIT
"""
import re

try:
    from standing import gitwrite as GW
except ImportError:   # ### a caller with tools/standing/ itself on the path (the v1NNN controls tools)
    import gitwrite as GW

QUOTED = re.compile(r'"(?:[^"\\`]|[\\`].)*"|\'[^\']*\'')
SHELL_VAR = re.compile(r'\$\{?\w+\}?|%\w+%')
SPLIT = re.compile(r'&&|\|\||;')
GIT_DEL = re.compile(r'^\s*git\s+(?:-C\s+\S+\s+)?(?:branch\s+(?:-[dD]|--delete)\s+((?:[^\s&;|]+\s*)+)|push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+))')
# ### v1.34.0: the words after the tool's path; whether the segment runs the tool is gitwrite's RUNS_COMMIT's to say (tool_delete)
TOOL_ARGS = re.compile(r'\bcommit\.py[\'"]?\s+(\S+)\s+delete\s+(\S+)\s*$')


def tool_delete(seg):
    """(repo, branch) where the segment runs the one-call tool -- gitwrite's RUNS_COMMIT over the segment's commands, quoted strings
    blanked by gitwrite.commands -- with the words `<repo> delete <branch>` closing it; None otherwise. An interpreter program quoting
    the route in a string, or an echo of it, runs no tool and reads None."""
    if not any(GW.RUNS_COMMIT.match(c) for c in GW.commands(seg or '')):
        return None
    m = TOOL_ARGS.search((seg or '').rstrip())
    return (m.group(1).strip('\'"'), m.group(2).strip('\'"')) if m else None


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
        t = tool_delete(seg)
        if t:
            b = t[1]
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
