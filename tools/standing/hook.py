"""standing/hook.py -- the PreToolUse hook of standing clauses v5 row (77), the standing toolset's copy.

Copied from tools/b714_hook.py (provenance), its act constants removed: the act is read at run time from data/act_current.json.
Installed in the seat's project settings (D:/.claude/settings.json) on the matcher Read|Bash|PowerShell.
Reads the hook's JSON from stdin and refuses, each refusal printed with the v5 row it enforces:
  READ   a Read call with no limit, or a limit above 200            -- rows (77) and (19)
  PIPE   a Bash or PowerShell command carrying a pipe outside quotes   -- rows (77) and (14)
  REDIR  a Bash or PowerShell command carrying a redirect outside quotes -- rows (77) and (14)
  ENV    a command prefixed by an environment-variable assignment     -- rows (77) and (20)
Quoted strings (single, double, PowerShell here-strings) are stripped before the scan, so a regex
argument such as "a|b" is not read as a pipe.

THE CLASS REPAIR (4)(iii) of the toolset act (provenance: the b714 hook appended to a bank its act's root names, so a refusal after the
root changed a rooted bank): each refusal is appended to data/<act>_hook_refusals.txt, <act> read from data/act_current.json at the
call, a bank of the excluded kind `hook_refusals` the root route takes out. Allowed calls print nothing and write nothing.

  python -I -X utf8 tools/standing/hook.py            the hook (stdin JSON)
  python -I -X utf8 tools/standing/hook.py control    the offline control: the judge's cases, and the (4)(iii) two instances in a scratch
                                                      directory outside data/ and tools/, bank data/<act>_hook_control.txt
"""
import datetime
import hashlib
import json
import os
import re
import sys
import tempfile

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIMIT = 200
EXCLUDED_KIND = 'hook_refusals'   # the kind the root route excludes (the act's record tool lists it in its EXCLUDE_KINDS)

ROW77 = ('(77) THE STANDING ROWS ENFORCED BY THE HARNESS: a PreToolUse hook in the seat’s project '
         'settings refusing a Read call with no limit or a limit above 200, a shell command carrying a pipe or a '
         'redirect, and a command prefixed by an environment variable, each refusal printed with the row it enforces')
ROWS = {
    'READ': ROW77 + ' ; (19) files read through the Read tool, whole where under two hundred lines and by '
                    'offset and a limit of at most two hundred otherwise',
    'PIPE': ROW77 + ' ; (14) no redirect of any stream and no pipe in any command, scratch, listings and '
                    'diagnostics included',
    'REDIR': ROW77 + ' ; (14) no redirect of any stream and no pipe in any command, scratch, listings and '
                     'diagnostics included',
    'ENV': ROW77 + ' ; (20) environment variables left as they are',
}

ASSIGN = re.compile(r'^\s*(?:env\s+)?[A-Za-z_][A-Za-z0-9_]*=')
PS_ENV = re.compile(r'(?i)^\s*\$env:[A-Za-z_][A-Za-z0-9_]*\s*=')


def act_of(relay=RELAY):
    """the act named by <relay>/data/act_current.json, or None where the file is absent or unreadable."""
    try:
        with open(os.path.join(relay, 'data', 'act_current.json'), encoding='utf-8') as f:
            return json.load(f).get('act')
    except (OSError, ValueError):
        return None


def refusals_path(relay=RELAY):
    act = act_of(relay)
    return os.path.join(relay, 'data', '%s_%s.txt' % (act, EXCLUDED_KIND) if act else 'act_unread_%s.txt' % EXCLUDED_KIND)


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


def lines_of(path):
    """v1.4.0: the file's line count (its line feeds, and a last line without one), or None where it is not a readable file."""
    try:
        with open(path, 'rb') as f:
            b = f.read()
    except OSError:
        return None
    return b.count(b'\n') + (1 if b and not b.endswith(b'\n') else 0)


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
        # ### v1.4.0, (R334)(2)(ii): row (19)'s "by offset and a limit" on a file of two hundred lines or more -- a limit with no offset
        # ### on such a file is refused (the class the record tool's reads route counted after the fact, b721 (y), b722 (y), b723 (b'))
        if inp.get('offset') is None:
            n = lines_of(inp.get('file_path') or '')
            if n is not None and n >= LIMIT:
                return 'READ', 'a Read call with a limit and no offset on a file of %d lines' % n
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


def refuse(kind, detail, tool, inp, relay=RELAY):
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    shown = inp.get('command') if tool != 'Read' else inp.get('file_path')
    reason = 'REFUSED %s: %s. ROW ENFORCED: %s' % (kind, detail, ROWS[kind])
    try:
        with open(refusals_path(relay), 'a', encoding='utf-8', newline='\n') as f:
            f.write('%s | %s | %s | %s | %s\n' % (stamp, kind, tool, json.dumps(shown, ensure_ascii=False)[:300],
                                                   detail))
    except OSError:
        pass
    return reason


def hook():
    try:
        data = json.load(sys.stdin)
    except ValueError as e:
        print('standing hook: unreadable hook input: %s' % e, file=sys.stderr)
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


def cases(act):
    ferry = 'D:/relay/data/%s_ferry.txt' % act
    return [
        ('Read', {'file_path': ferry}, 'READ'),
        ('Read', {'file_path': ferry, 'offset': 1, 'limit': 201}, 'READ'),
        ('Read', {'file_path': ferry, 'offset': 1, 'limit': 200}, None),
        ('Read', {'file_path': os.path.join(RELAY, 'tools', 'standing', 'hook.py'), 'limit': 60}, 'READ'),   # ### v1.4.0, (2)(ii)
        ('Read', {'file_path': os.path.join(RELAY, 'tools', 'standing', 'hook.py'), 'offset': 1, 'limit': 60}, None),
        ('Bash', {'command': 'git status | head'}, 'PIPE'),
        ('Bash', {'command': 'git log --oneline -3 2>&1'}, 'REDIR'),
        ('Bash', {'command': 'cat a > b'}, 'REDIR'),
        ('Bash', {'command': 'PYTHONIOENCODING=utf-8 python x.py'}, 'ENV'),
        ('Bash', {'command': 'cd /d/relay && FOO=1 python x.py'}, 'ENV'),
        ('Bash', {'command': 'cd /d/relay && python -I -X utf8 tools/locate.py data/x.txt "a|b>c"'}, None),
        ('Bash', {'command': 'git -C /d/relay commit -m "%s: a -> b, x|y"' % act}, None),
        ('PowerShell', {'command': 'Get-ChildItem D:/relay | Select-Object -First 3'}, 'PIPE'),
        ('PowerShell', {'command': 'git status > out.txt'}, 'REDIR'),
        ('PowerShell', {'command': '$env:PYTHONIOENCODING = "utf-8"; python x.py'}, 'ENV'),
        ('PowerShell', {'command': "git commit -m @'\nline | with > marks\n'@"}, None),
        ('PowerShell', {'command': 'Get-PSDrive'}, None),
        ('Grep', {'pattern': 'a|b'}, None),
    ]


def sha256(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def instance_record(prev):
    """(4)(iii)'s instance from the record: the previous act's hook bank, read against the sha256 its act's root names."""
    root = os.path.join(RELAY, 'data', '%s_act_root.json' % prev)
    rel = 'data/%s_%s.txt' % (prev, EXCLUDED_KIND)
    try:
        rj = json.load(open(root, encoding='utf-8'))
    except (OSError, ValueError):
        return dict(named=False, rel=rel, root=root)
    banks = dict(rj.get('banks') or {})   # a root's banks: its `banks` map, or its `items` rows "data/<name> <sha256>"
    for it in rj.get('items') or []:
        parts = it.split(' ')
        if len(parts) == 2 and parts[0].startswith('data/'):
            banks.setdefault(parts[0], parts[1])
    p = os.path.join(RELAY, *rel.split('/'))
    return dict(named=rel in banks, rel=rel, root=root, rooted=banks.get(rel), now=sha256(p) if os.path.isfile(p) else None)


def instance_constructed(act):
    """(4)(iii)'s constructed instance, in a scratch directory outside data/ and tools/: a test relay holding act_current.json, three
    banks and a test root naming them by sha256; one refusal sent through refuse() with the standing path, then one through a refuse
    bound to a rooted bank (the old form). Returns each run's changed root-named banks. Nothing is deleted; the scratch stays."""
    scratch = tempfile.mkdtemp(prefix='standing-hook-control-')
    d = os.path.join(scratch, 'data')
    os.makedirs(d)
    with open(os.path.join(d, 'act_current.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps({'act': act}) + '\n')
    named = ['%s_closing.txt' % act, '%s_defects.txt' % act, '%s_old_hook_bank.txt' % act]
    for n in named:
        with open(os.path.join(d, n), 'w', encoding='utf-8', newline='\n') as f:
            f.write('a test bank %s\n' % n)
    test_root = {'data/' + n: sha256(os.path.join(d, n)) for n in named}

    def changed():
        return sorted(r for r, h in test_root.items() if sha256(os.path.join(scratch, *r.split('/'))) != h)

    refuse('PIPE', 'the control`s refused call', 'Bash', {'command': 'git status | head'}, relay=scratch)
    new = changed()
    out = refusals_path(scratch)
    old_path = os.path.join(d, named[2])
    with open(old_path, 'a', encoding='utf-8', newline='\n') as f:   # the old form: the refusal appended to a bank the root names
        f.write('a refusal line, the old form\n')
    old = changed()
    return dict(scratch=scratch, new_changed=new, new_bank=os.path.relpath(out, scratch).replace(os.sep, '/'),
                new_bank_named='data/' + os.path.basename(out) in test_root, old_changed=old)


def control():
    act = act_of()
    prev = None
    try:
        prev = json.load(open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8')).get('prev')
    except (OSError, ValueError):
        pass
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines = ['%s STANDING HOOK CONTROL -- v5 row (77) and the class repair (4)(iii), tools/standing/hook.py at %s' % (act, stamp),
             '### each case: tool | input | wanted | got | AS WANTED']
    ok = 0
    cs = cases(act)
    for tool, inp, want in cs:
        got = judge(tool, inp)
        got_kind = got[0] if got else None
        good = got_kind == want
        ok += good
        lines.append('%s | %s | %s | %s | %s' % (tool, json.dumps(inp, ensure_ascii=False), want or 'ALLOWED',
                                                 got_kind or 'ALLOWED', good))
    kinds = sorted({w for _t, _i, w in cs if w})
    lines.append('### ### **CASES %d ; AS WANTED %d ; REFUSAL KINDS %s ; ALLOWED CASES %d ; ALL AS WANTED %s**'
                 % (len(cs), ok, ','.join(kinds), sum(1 for c in cs if c[2] is None), ok == len(cs)))
    rec = instance_record(prev)
    con = instance_constructed(act)
    rec_class = bool(rec.get('named')) and rec.get('rooted') is not None and rec.get('now') != rec.get('rooted')
    con_ok = con['new_changed'] == [] and not con['new_bank_named'] and con['old_changed'] != []
    lines += ['', '### (4)(iii) INSTANCE 1, FROM THE RECORD: %s, named by %s: %s ; its sha256 at the root %s ; now %s ; the class (a refusal '
              'after the root changed a rooted bank) %s' % (rec['rel'], os.path.basename(rec['root']), rec.get('named'),
                                                            (rec.get('rooted') or '-')[:16], (rec.get('now') or '-')[:16],
                                                            'SHOWN' if rec_class else 'NOT SHOWN'),
              '### (4)(iii) INSTANCE 2, CONSTRUCTED in %s: the standing refuse() wrote %s (named by the test root %s) and changed root-named '
              'banks %s ; the old form (the refusal appended to a root-named bank) changed %s ; AS WANTED %s' % (
                  con['scratch'], con['new_bank'], con['new_bank_named'], con['new_changed'] or 'none', con['old_changed'] or 'none', con_ok),
              '### ### **(4)(iii) CONTROL: THE RECORD`S INSTANCE %s ; THE CONSTRUCTED %s ; THE REPAIR HOLDS %s.**' % (
                  'SHOWN' if rec_class else 'NOT SHOWN', 'AS WANTED' if con_ok else 'NOT AS WANTED', rec_class and con_ok and ok == len(cs))]
    bank = os.path.join(RELAY, 'data', '%s_hook_control.txt' % act)
    with open(bank + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    os.replace(bank + '.tmp', bank)
    print('\n'.join(lines[-4:]))
    print('bank', bank)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'control':
        control()
    else:
        hook()
