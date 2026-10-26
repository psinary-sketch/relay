"""b714_hook.py -- the PreToolUse hook of (R324)(6)(iv), standing clauses v5 row (77).

Installed in the seat's project settings (D:/.claude/settings.json) on the matcher Read|Bash|PowerShell.
Reads the hook's JSON from stdin and refuses, each refusal printed with the v5 row it enforces:
  READ   a Read call with no limit, or a limit above 200            -- rows (77) and (19)
  PIPE   a Bash or PowerShell command carrying a pipe outside quotes   -- rows (77) and (14)
  REDIR  a Bash or PowerShell command carrying a redirect outside quotes -- rows (77) and (14)
  ENV    a command prefixed by an environment-variable assignment     -- rows (77) and (20)
Quoted strings (single, double, PowerShell here-strings) are stripped before the scan, so a regex
argument such as "a|b" is not read as a pipe. Each refusal is appended to data/b714_hook_refusals.txt
(the hook's own bank). Allowed calls print nothing and write nothing.

  python -I -X utf8 tools/b714_hook.py            the hook (stdin JSON)
  python -I -X utf8 tools/b714_hook.py control    the offline control, bank data/b714_hook_control.txt
"""
import datetime
import json
import os
import re
import sys

RELAY = 'D:/relay'
REFUSALS = os.path.join(RELAY, 'data', 'b714_hook_refusals.txt')
CONTROL = os.path.join(RELAY, 'data', 'b714_hook_control.txt')
LIMIT = 200

ROW77 = ('(77) (R324)(6)(iv) THE STANDING ROWS ENFORCED BY THE HARNESS: a PreToolUse hook in the seat’s project '
         'settings refusing a Read call with no limit or a limit above 200, a shell command carrying a pipe or a '
         'redirect, and a command prefixed by an environment variable, each refusal printed with the row it enforces')
ROWS = {
    'READ': ROW77 + ' ; (19) (R319) files read through the Read tool, whole where under two hundred lines and by '
                    'offset and a limit of at most two hundred otherwise',
    'PIPE': ROW77 + ' ; (14) (R317) no redirect of any stream and no pipe in any command, scratch, listings and '
                    'diagnostics included',
    'REDIR': ROW77 + ' ; (14) (R317) no redirect of any stream and no pipe in any command, scratch, listings and '
                     'diagnostics included',
    'ENV': ROW77 + ' ; (20) (R274) environment variables left as they are',
}

ASSIGN = re.compile(r'^\s*(?:env\s+)?[A-Za-z_][A-Za-z0-9_]*=')
PS_ENV = re.compile(r'(?i)^\s*\$env:[A-Za-z_][A-Za-z0-9_]*\s*=')


def strip_quotes(cmd):
    """The command with every quoted span replaced by a blank, quotes kept as markers."""
    out = []
    i, n = 0, len(cmd)
    while i < n:
        if cmd.startswith("@'", i) or cmd.startswith('@"', i):
            q = cmd[i + 1]
            end = cmd.find('\n' + q + '@', i + 2)
            if end < 0:
                return ''.join(out) + ' QQ', False
            out.append(' QQ ')
            i = end + 3
            continue
        c = cmd[i]
        if c == "'":
            end = cmd.find("'", i + 1)
            if end < 0:
                return ''.join(out) + ' QQ', False
            out.append(' QQ ')
            i = end + 1
            continue
        if c == '"':
            j = i + 1
            while j < n and cmd[j] != '"':
                j += 2 if cmd[j] in '\\`' else 1
            if j >= n:
                return ''.join(out) + ' QQ', False
            out.append(' QQ ')
            i = j + 1
            continue
        if c in '\\`' and i + 1 < n:
            out.append('  ')
            i += 2
            continue
        out.append(c)
        i += 1
    return ''.join(out), True


def judge(tool, inp):
    """(kind, detail) for a refusal, or None for an allowed call."""
    if tool == 'Read':
        lim = inp.get('limit')
        if lim is None:
            return 'READ', 'a Read call with no limit'
        try:
            if int(lim) > LIMIT:
                return 'READ', 'a Read call with limit %s, above %d' % (lim, LIMIT)
        except (TypeError, ValueError):
            return 'READ', 'a Read call with an unreadable limit %r' % (lim,)
        return None
    if tool in ('Bash', 'PowerShell'):
        cmd = inp.get('command') or ''
        bare, _closed = strip_quotes(cmd)
        if '|' in bare:
            return 'PIPE', 'a %s command carrying a pipe outside quotes' % tool
        if '>' in bare or '<' in bare:
            return 'REDIR', 'a %s command carrying a redirect outside quotes' % tool
        for seg in re.split(r'&&|;|\n', bare):
            if ASSIGN.match(seg) or PS_ENV.match(seg):
                return 'ENV', 'a %s command prefixed by an environment-variable assignment' % tool
        return None
    return None


def refuse(kind, detail, tool, inp):
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    shown = inp.get('command') if tool != 'Read' else inp.get('file_path')
    reason = 'REFUSED %s: %s. ROW ENFORCED: %s' % (kind, detail, ROWS[kind])
    try:
        with open(REFUSALS, 'a', encoding='utf-8', newline='\n') as f:
            f.write('%s | %s | %s | %s | %s\n' % (stamp, kind, tool, json.dumps(shown, ensure_ascii=False)[:300],
                                                   detail))
    except OSError:
        pass
    return reason


def hook():
    try:
        data = json.load(sys.stdin)
    except ValueError as e:
        print('b714_hook: unreadable hook input: %s' % e, file=sys.stderr)
        sys.exit(2)
    tool = data.get('tool_name', '')
    inp = data.get('tool_input') or {}
    verdict = judge(tool, inp)
    if verdict is None:
        sys.exit(0)
    reason = refuse(verdict[0], verdict[1], tool, inp)
    print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'deny',
                                             'permissionDecisionReason': reason}}, ensure_ascii=False))
    sys.exit(0)


CASES = [
    ('Read', {'file_path': 'D:/relay/data/b714_ferry.txt'}, 'READ'),
    ('Read', {'file_path': 'D:/relay/data/b714_ferry.txt', 'offset': 1, 'limit': 201}, 'READ'),
    ('Read', {'file_path': 'D:/relay/data/b714_ferry.txt', 'offset': 1, 'limit': 200}, None),
    ('Bash', {'command': 'git status | head'}, 'PIPE'),
    ('Bash', {'command': 'git log --oneline -3 2>&1'}, 'REDIR'),
    ('Bash', {'command': 'cat a > b'}, 'REDIR'),
    ('Bash', {'command': 'PYTHONIOENCODING=utf-8 python x.py'}, 'ENV'),
    ('Bash', {'command': 'cd /d/relay && FOO=1 python x.py'}, 'ENV'),
    ('Bash', {'command': 'cd /d/relay && python -I -X utf8 tools/b712_locate.py data/x.txt "a|b>c"'}, None),
    ('Bash', {'command': 'git -C /d/relay commit -m "b714: a -> b, x|y"'}, None),
    ('PowerShell', {'command': 'Get-ChildItem D:/relay | Select-Object -First 3'}, 'PIPE'),
    ('PowerShell', {'command': 'git status > out.txt'}, 'REDIR'),
    ('PowerShell', {'command': '$env:PYTHONIOENCODING = "utf-8"; python x.py'}, 'ENV'),
    ('PowerShell', {'command': "git commit -m @'\nline | with > marks\n'@"}, None),
    ('PowerShell', {'command': 'Get-PSDrive'}, None),
    ('Grep', {'pattern': 'a|b'}, None),
]


def control():
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines = ['B714 HOOK CONTROL -- (R324)(6)(iv), v5 row (77), the offline cases of tools/b714_hook.py at %s' % stamp,
             '### each case: tool | input | wanted | got | AS WANTED']
    ok = 0
    for tool, inp, want in CASES:
        got = judge(tool, inp)
        got_kind = got[0] if got else None
        good = got_kind == want
        ok += good
        lines.append('%s | %s | %s | %s | %s' % (tool, json.dumps(inp, ensure_ascii=False), want or 'ALLOWED',
                                                 got_kind or 'ALLOWED', good))
    kinds = sorted({w for _t, _i, w in CASES if w})
    lines.append('### ### **CASES %d ; AS WANTED %d ; REFUSAL KINDS %s ; ALLOWED CASES %d ; ALL AS WANTED %s**'
                 % (len(CASES), ok, ','.join(kinds), sum(1 for c in CASES if c[2] is None), ok == len(CASES)))
    with open(CONTROL, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    print('bank', CONTROL)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'control':
        control()
    else:
        hook()
