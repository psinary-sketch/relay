# -*- coding: utf-8 -*-
r"""edit_route.py -- THE EDIT-ROUTE ARM, W-ORD-EDIT-ROUTE-ARM acted at b646 under (R256)(2).

### The suite reads the act's command bank (the shell commands the record tool captures from the seat's session from the ruling's line
### onward) and reads as a failure of the arm G-EDIT-ROUTE:
###   (S) any `sed -i` (or `--in-place`, or a flag cluster carrying i, e.g. `-Ei`);
###   (H) any heredoc or redirect writing under tools/: a shell redirect (`>`, `>>`, `n>`) outside quotes whose target is under tools/;
###       a `tee` whose path is under tools/; PowerShell `Out-File`, `Set-Content`, `Add-Content` or `Copy-Item`/`cp` whose path is under
###       tools/ (the redirect's PowerShell forms); and a heredoc body that writes (open(..., 'w'/'a'), write_text, write_bytes, shutil
###       copy, os.replace, Out-File, Set-Content) with a tools path on the same line;
###   (R) any rm (shell `rm`, `git rm`) or Remove-Item (and its aliases `ri`, `del`, `rmdir`, `rd`) whose path operand is not absolute
###       (a literal `/x/...` or `X:/`/`X:\` path, no glob character, no variable), and any branch deletion (`git branch -d|-D`,
###       `git push <remote> --delete`) whose operand is not an explicit branch name (no glob, no variable, no substitution).
### `offences(cmd)` returns [(kind, fragment)]; `scan(bank_rows)` returns the offending rows. Each offending command is printed by the
### caller. The planted test is tools/test_edit_route_b646.py, one command of each kind.
"""
import re

TOOLS_PATH = re.compile(r'''(?:^|[\s"'/\\=(])tools[/\\]''')
ABS_PATH = re.compile(r'^(?:/[A-Za-z0-9_.~-]|[A-Za-z]:[/\\])')
BRANCH = re.compile(r'^[A-Za-z0-9._/-]+$')
SEP = re.compile(r'(?:&&|\|\||;|\||\n|\(|\{|`|\$\()')


def _heredocs(cmd):
    """Split a command into (shell text, [heredoc bodies]); a body runs from the line after `<<[-]'TAG'` to the line that is TAG."""
    lines = cmd.split('\n')
    shell, bodies, i = [], [], 0
    while i < len(lines):
        ln = lines[i]
        shell.append(ln)
        tags = re.findall(r'''<<-?\s*['"]?([A-Za-z_][A-Za-z0-9_]*)['"]?''', ln)
        i += 1
        for tag in tags:
            body = []
            while i < len(lines) and lines[i].strip() != tag:
                body.append(lines[i])
                i += 1
            i += 1
            bodies.append('\n'.join(body))
    return '\n'.join(shell), bodies


def _unquoted(s):
    """The text with quoted spans blanked (so a `>` inside a quoted python -c program or a commit message is not a redirect); the
    quoted span's text is kept where it is the target of a redirect, by returning both views."""
    out, q = [], None
    for ch in s:
        if q:
            out.append(ch if ch == q else ' ')
            if ch == q:
                q = None
        elif ch in '"\'':
            q = ch
            out.append(ch)
        else:
            out.append(ch)
    return ''.join(out)


def _redirect_targets(shell):
    blank = _unquoted(shell)
    targets = []
    for m in re.finditer(r'(?<![-=<>])(\d?>>?|&>)(?!&)', blank):
        if m.start() > 0 and blank[m.start() - 1] == '-':
            continue
        rest = shell[m.end():].lstrip()
        if rest[:1] in '"\'':
            q = rest[0]
            end = rest.find(q, 1)
            targets.append(rest[1:end if end > 0 else None])
        else:
            targets.append(re.split(r'[\s;|&)]', rest, 1)[0] if rest else '')
    return targets


def _words(seg):
    return re.findall(r'''"[^"]*"|'[^']*'|\S+''', seg)


def _strip(w):
    return w[1:-1] if len(w) >= 2 and w[0] == w[-1] and w[0] in '"\'' else w


def _segments(shell):
    return [s.strip() for s in SEP.split(_unquoted_keep(shell)) if s.strip()]


def _unquoted_keep(shell):
    # ### separators inside quotes are not separators: replace them inside quoted spans by a placeholder, split, then restore.
    out, q = [], None
    for ch in shell:
        if q:
            out.append({'&': '\x01', '|': '\x02', ';': '\x03', '\n': '\x04', '(': '\x05', '{': '\x06', '`': '\x07', '$': '\x08'}.get(ch, ch))
            if ch == q:
                q = None
        else:
            if ch in '"\'':
                q = ch
            out.append(ch)
    return ''.join(out)


def _restore(s):
    for a, b in (('\x01', '&'), ('\x02', '|'), ('\x03', ';'), ('\x04', '\n'), ('\x05', '('), ('\x06', '{'), ('\x07', '`'), ('\x08', '$')):
        s = s.replace(a, b)
    return s


def _abs_ok(p):
    return bool(ABS_PATH.match(p)) and not re.search(r'[*?\[$]', p)


def offences(cmd):
    found = []
    shell, bodies = _heredocs(cmd)
    segs = [_restore(s) for s in _segments(shell)]
    for seg in segs:
        w = [_strip(x) for x in _words(seg)]
        if not w:
            continue
        head = w[0].lower()
        # ### (S) sed in place
        if head == 'sed' or (head in ('xargs', 'find') and 'sed' in w):
            k = w.index('sed') if 'sed' in w else 0
            for a in w[k + 1:]:
                if a == '--in-place' or a.startswith('--in-place=') or re.match(r'^-[A-Za-z]*i', a):
                    found.append(('S sed -i', seg))
                    break
        # ### (H) PowerShell writers and tee under tools/
        if head in ('out-file', 'set-content', 'add-content', 'tee', 'tee-object', 'copy-item', 'cp', 'copy', 'move-item', 'mv'):
            tgt = [a for a in w[1:] if not a.startswith('-')]
            if head in ('cp', 'copy', 'copy-item', 'move-item', 'mv'):
                tgt = tgt[-1:]
            if any(TOOLS_PATH.search(' ' + t) for t in tgt):
                found.append(('H write under tools/', seg))
        for k, a in enumerate(w):
            if a.lower() in ('out-file', 'set-content', 'add-content', 'tee-object', 'tee') and k > 0:
                if any(TOOLS_PATH.search(' ' + t) for t in w[k + 1:] if not t.startswith('-')):
                    found.append(('H write under tools/', seg))
                    break
        # ### (R) rm / git rm / Remove-Item, and branch deletion
        ops = None
        if head in ('rm', 'rmdir', 'remove-item', 'ri', 'del', 'rd', 'erase'):
            ops = w[1:]
        elif head == 'xargs' and 'rm' in w:
            found.append(('R rm without an explicit absolute path', seg))
        elif head == 'xargs' and 'branch' in w and any(a in ('-d', '-D', '--delete') for a in w):
            found.append(('R branch deletion without an explicit name', seg))
        elif head == 'git':
            g = [a for a in w[1:]]
            if g[:1] == ['-C'] and len(g) > 1:
                g = g[2:]
            if g[:1] == ['rm']:
                ops = g[1:]
            elif g[:1] == ['branch'] and any(a in ('-d', '-D', '--delete') for a in g):
                names = [a for a in g[1:] if not a.startswith('-')]
                bad = [a for a in names if not BRANCH.match(a)] or ([] if names else ['<none>'])
                if bad:
                    found.append(('R branch deletion without an explicit name', seg))
            elif g[:1] == ['push'] and ('--delete' in g or '-d' in g):
                names = [a for a in g[1:] if not a.startswith('-')][1:]
                bad = [a for a in names if not BRANCH.match(a.lstrip(':'))] or ([] if names else ['<none>'])
                if bad:
                    found.append(('R branch deletion without an explicit name', seg))
        if ops is not None:
            paths, skip = [], False
            for a in ops:
                if skip:
                    skip = False
                    paths.append(a)
                    continue
                if a.lower() in ('-path', '-literalpath'):
                    skip = True
                    continue
                if a.startswith('-'):
                    continue
                paths.append(a)
            if not paths or any(not _abs_ok(p) for p in paths):
                found.append(('R rm without an explicit absolute path', seg))
    for t in _redirect_targets(shell):
        if TOOLS_PATH.search(' ' + t):
            found.append(('H redirect under tools/', '> ' + t))
    for b in bodies:
        for ln in b.split('\n'):
            if TOOLS_PATH.search(' ' + ln) or re.search(r'''['"]tools['"]''', ln):
                if re.search(r'''open\([^)]*,\s*['"][wa]b?['"]|write_text|write_bytes|shutil\.copy|os\.replace|Out-File|Set-Content|\.write\(''', ln):
                    found.append(('H heredoc writing under tools/', ln.strip()))
    return found


def capture(jsonl, anchor, subagent_dir=None):
    """The act's command bank: every Bash and PowerShell tool_use command in the seat's session transcript from the first user line
    holding `anchor` (the ruling's BEGIN line) onward, and in its subagents' transcripts whose entries are timestamped at or after it.
    Returns [{'n', 'tool', 'ts', 'src', 'cmd'}] in transcript order."""
    import io
    import json
    import os
    rows, start = [], None

    def take(path, label, since):
        out = []
        for ln in io.open(path, encoding='utf-8', errors='replace'):
            try:
                j = json.loads(ln)
            except ValueError:
                continue
            ts = j.get('timestamp') or ''
            if since is not None and ts < since:
                continue
            msg = j.get('message') or {}
            for c in (msg.get('content') or []) if isinstance(msg.get('content'), list) else []:
                if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('Bash', 'PowerShell'):
                    out.append({'tool': c['name'], 'ts': ts, 'src': label, 'cmd': (c.get('input') or {}).get('command', '')})
        return out

    for ln in io.open(jsonl, encoding='utf-8', errors='replace'):
        if anchor in ln:
            try:
                j = json.loads(ln)
            except ValueError:
                continue
            if j.get('type') == 'user' and not j.get('isCompactSummary'):
                start = j.get('timestamp')
                break
    if start is None:
        return []
    rows += take(jsonl, 'seat', start)
    if subagent_dir and os.path.isdir(subagent_dir):
        for f in sorted(os.listdir(subagent_dir)):
            if f.endswith('.jsonl'):
                rows += take(os.path.join(subagent_dir, f), 'subagent ' + f[:-6], start)
    rows.sort(key=lambda r: r['ts'])
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


def scan(rows):
    """rows: [{'n': int, 'tool': str, 'cmd': str}] -> [(row, offences)] for the offending rows."""
    return [(r, o) for r in rows for o in [offences(r['cmd'])] if o]
