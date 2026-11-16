# -*- coding: utf-8 -*-
"""b757 -- (R367)(8)(iii): N5'S READER OF A REPOSITORY EDIT, TAUGHT TO READ A gh CALL MADE FROM INSIDE A TOOL BY THAT TOOL'S ROWS BANK.

The ruling's words (data/b757_ferry.txt :25): "(iii) (F7): the reader behind N5's line (tools/acts/b756.py :1875) is run over b756's banks,
where two description writes are known to have been sent; where it reads NONE it is taught to read a gh call made from inside a tool by that
tool's rows bank, and its planted control is a script that sends none and a script that sends one."

THE CARRIED READER (`carried`), tools/acts/b756.py :1916 of b757's copy and :1860 of b756's, unchanged: a captured command whose text, its
quoted arguments blanked, runs `gh repo edit`. THE TAUGHT READER (`taught`): the carried reader's rows, and beside them every command that
runs an act tool (tools/b<act>_<name>.py) whose source holds a `gh repo edit` call (the list form ['gh', 'repo', 'edit' ...] or the words
in a string) and imports subprocess at a line's head, with the edit rows of that tool's rows bank (data/b<act>_<name>_rows.json: a row of
kind 'edit', or a row carrying 'edit_rc' as b756's rows do), each with its door, time and exit. A send counts whatever the server answered;
the reader never calls gh. A command runs a tool where the tool is the script python is given in one of its segments (`runs`); a command
naming the tool's path as another script's argument, a git grep's or a count's, does not run it (b757 defect (z): the first reader took
every path named as a run, and read this reader's own planted words as a sender).

THE CONTROLS, planted in a fresh temporary folder outside the relay and removed after: a script that sends none (no gh call in its source,
its rows bank without an edit row) and a script that sends one (a gh repo edit call in its source, never run, and one edit row in its rows
bank), both run by a planted command bank; a command that runs gh repo edit itself; a script holding the call's words in a string and
importing no subprocess, run; and a script that sends one, with an edit row, whose path two commands name and none runs. Wanted: the
carried reader 1 (the direct command alone), the taught reader 2 (the direct command and the script that sends one), the two scripts that
send none read as none, the named script read as no run.

usage: python -X utf8 -u tools/b757_ghcalls.py [--bank]      the controls, then both readers over b756's banks and over b757's
"""
import io
import json
import os
import re
import shutil
import sys
import tempfile
import time

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = '\n'
BANK = os.path.join(RELAY, 'data', 'b757_ghcalls.txt')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
DIRECT = re.compile(r'\bgh\s+repo\s+edit\b')
SRC_CALL = re.compile(r'''['"]gh['"]\s*,\s*['"]repo['"]\s*,\s*['"]edit['"]|['"][^'"\n]*\bgh\s+repo\s+edit\b''')
# ### b757 defect (z): a run read from the script python is given, segment by segment, not from any path the command names; a sender's
# ### source imports subprocess at a line's head (a string holding the call's words, as this reader's own controls do, is no call)
SEG = re.compile(r'&&|\|\||[;|]')
PY = re.compile(r'(?:^|[\\/])(?:python3?|py)(?:\.exe)?$', re.I)
ACT_TOOL = re.compile(r'(?:^|[\\/])tools[\\/](b\d+_[A-Za-z0-9_]+)\.py$')
IMPORTS_SUBPROCESS = re.compile(r'(?m)^[ \t]*(?:import[ \t]+(?:[\w. \t]*,[ \t]*)?subprocess\b|from[ \t]+subprocess[ \t]+import\b)')


def carried(cmd_rows):
    """the reader at tools/acts/b756.py :1860, unchanged: the row numbers of commands running gh repo edit, quoted arguments blanked."""
    return [r['n'] for r in cmd_rows if DIRECT.search(QUOTED.sub('""', r.get('cmd') or ''))]


def runs(cmd):
    """the act tools a command runs: in each segment (cut at &&, ||, ; and |; a quoted argument holding a space blanked first), the script
    the interpreter opening the segment is given -- its first argument after the options, -X and -W taking a value, -c and -m giving no
    script -- where that script is tools/b<act>_<name>.py."""
    out = []
    for seg in SEG.split(QUOTED.sub(lambda m: m.group(0) if ' ' not in m.group(0) else '""', cmd or '')):
        toks = [t.strip('"\'') for t in seg.split()]
        if not toks or not PY.search(toks[0]):
            continue
        j, script = 1, None
        while j < len(toks) and toks[j].startswith('-'):
            if toks[j] in ('-c', '-m'):
                j = len(toks)
                break
            j += 2 if toks[j] in ('-X', '-W') else 1
        if j < len(toks):
            script = toks[j]
        m = ACT_TOOL.search(script or '')
        if m and m.group(1) not in out:
            out.append(m.group(1))
    return out


def source_sends(src):
    """does a tool's source hold a gh repo edit call (comment lines dropped) and import subprocess at a line's head?"""
    body = NL.join(l for l in (src or '').split(NL) if not l.lstrip().startswith('#'))
    return bool(IMPORTS_SUBPROCESS.search(body)) and bool(SRC_CALL.search(body))


def edit_rows(rows_path):
    if not os.path.isfile(rows_path):
        return None
    j = json.load(io.open(rows_path, encoding='utf-8'))
    R = j.get('rows', []) if isinstance(j, dict) else j
    return [r for r in R if isinstance(r, dict) and (r.get('kind') == 'edit' or 'edit_rc' in r)]


def taught(cmd_rows, tools_dir, data_dir):
    """(direct rows, {tool stem: [(door, at, rc)]} for each tool the capture runs whose source sends gh repo edit, tools read and not sending)."""
    direct = carried(cmd_rows)
    stems = []
    for r in cmd_rows:
        for s in runs(r.get('cmd') or ''):
            if s not in stems:
                stems.append(s)
    sends, quiet = {}, []
    for s in stems:
        p = os.path.join(tools_dir, s + '.py')
        src = io.open(p, encoding='utf-8', errors='replace').read() if os.path.isfile(p) else ''
        if not source_sends(src):
            quiet.append(s)
            continue
        er = edit_rows(os.path.join(data_dir, s + '_rows.json'))
        sends[s] = None if er is None else [(r.get('door'), r.get('at'), r.get('rc', r.get('edit_rc'))) for r in er]
    return direct, sends, quiet


def count(direct, sends):
    return len(direct) + sum(len(v or []) for v in sends.values())


def controls():
    tmp = tempfile.mkdtemp(prefix='b757_ghcalls_')
    try:
        td, dd = os.path.join(tmp, 'tools'), os.path.join(tmp, 'data')
        os.makedirs(td)
        os.makedirs(dd)
        io.open(os.path.join(td, 'b999_none.py'), 'w', encoding='utf-8').write(
            'import subprocess\n# gh repo edit is named in this comment only\nsubprocess.run(["git", "status"])\n')
        io.open(os.path.join(td, 'b999_one.py'), 'w', encoding='utf-8').write(
            'import subprocess\nsubprocess.run(["gh", "repo", "edit", "--description", "x"])\n')
        io.open(os.path.join(dd, 'b999_none_rows.json'), 'w', encoding='utf-8').write(json.dumps({'rows': [{'kind': 'read', 'door': 'A'}]}))
        io.open(os.path.join(dd, 'b999_one_rows.json'), 'w', encoding='utf-8').write(
            json.dumps({'rows': [{'kind': 'read', 'door': 'A'}, {'kind': 'edit', 'door': 'A', 'at': 'T', 'rc': 0}]}))
        # ### defect (z)'s two plants: the call's words in a string with no subprocess import, run; a sender named by two commands, never run
        io.open(os.path.join(td, 'b999_words.py'), 'w', encoding='utf-8').write(
            'PLANT = \'subprocess.run(["gh", "repo", "edit", "--description", "w"])\'\nprint(PLANT)\n')
        io.open(os.path.join(td, 'b999_named.py'), 'w', encoding='utf-8').write(
            'import subprocess\nsubprocess.run(["gh", "repo", "edit", "--description", "z"])\n')
        io.open(os.path.join(dd, 'b999_named_rows.json'), 'w', encoding='utf-8').write(
            json.dumps({'rows': [{'kind': 'edit', 'door': 'B', 'at': 'U', 'rc': 0}]}))
        cmds = [dict(n=1, cmd='cd /d/relay && python -X utf8 -u tools/b999_none.py write A'),
                dict(n=2, cmd='cd /d/relay && python -X utf8 -u tools/b999_one.py write A'),
                dict(n=3, cmd='gh repo edit --description "y"'),
                dict(n=4, cmd='python tools/standing/commit.py relay "x" "words naming gh repo edit inside quotes"'),
                dict(n=5, cmd='python -X utf8 -u tools/standing/peek.py count tools/b999_named.py && git grep -n "gh repo" HEAD -- tools/b999_named.py'),
                dict(n=6, cmd='cd /d/relay && python -X utf8 -u tools/b999_words.py')]
        c = carried(cmds)
        d, s, q = taught(cmds, td, dd)
        out = [('the carried reader over the plant: the direct command alone (row 3), the scripts, the named path and the quoted words unread', c == [3]),
               ('the taught reader: the direct command and the script that sends one, its one edit row', d == [3] and s == {'b999_one': [('A', 'T', 0)]}),
               ('the two scripts that send none, read and counted none: one whose source holds no call (a comment naming the words dropped), '
                'one holding the call`s words in a string with no subprocess import', q == ['b999_none', 'b999_words']),
               ('a sending script whose path a count and a git grep name and no command runs: no run, neither a sender nor read',
                'b999_named' not in s and 'b999_named' not in q),
               ('the counts: carried 1, taught 2', len(c) == 1 and count(d, s) == 2)]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out, not os.path.exists(tmp)


def over(act):
    cpath = os.path.join(RELAY, 'data', '%s_commands.json' % act)
    if not os.path.isfile(cpath):
        return None
    rows = json.load(io.open(cpath, encoding='utf-8')).get('rows') or []
    c = carried(rows)
    d, s, q = taught(rows, os.path.join(RELAY, 'tools'), os.path.join(RELAY, 'data'))
    return dict(rows=len(rows), carried=c, direct=d, sends=s, quiet=q)


def main(argv):
    out = ['b757 -- (R367)(8)(iii): N5`S READER OF A REPOSITORY EDIT, TAUGHT TO READ A gh CALL FROM INSIDE A TOOL BY ITS ROWS BANK (%s, '
           'tools/b757_ghcalls.py)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '']
    cs, gone = controls()
    out.append('## THE CONTROLS FIRST (planted in a temporary folder outside the relay, removed after: %s): %d of %d AS WANTED' % (
        'REMOVED' if gone else '### NOT REMOVED', sum(1 for _w, ok in cs if ok), len(cs)))
    out += ['    %s -> %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED') for w, ok in cs]
    res = {}
    for act in ('b756', 'b757'):
        r = over(act)
        res[act] = r
        out.append('')
        if r is None:
            out.append('## %s: data/%s_commands.json NOT WRITTEN -- read at the close, when the commands route has written it' % (act, act))
            continue
        out.append('## %s`S BANKS (data/%s_commands.json, %d captured commands)' % (act, act, r['rows']))
        out.append('  THE CARRIED READER, "gh repo edit in the capture": %s' % (r['carried'] or 'NONE'))
        out.append('  THE TAUGHT READER: commands running gh repo edit %s ; tools the capture runs whose source sends gh repo edit %d' % (
            r['direct'] or 'none', len(r['sends'])))
        for s, v in r['sends'].items():
            if v is None:
                out.append('    tools/%s.py: its source holds the call`s words; NO ROWS BANK data/%s_rows.json, so no send read' % (s, s))
                continue
            out.append('    tools/%s.py, its rows bank data/%s_rows.json: edit rows %d -- %s' % (s, s, len(v), ' ; '.join(
                '%s at %s exit %s' % x for x in v) or 'none'))
        out.append('  THE COUNT: carried %d ; taught %d' % (len(r['carried']), count(r['direct'], r['sends'])))
    ok = all(w for _x, w in cs) and gone
    b6 = res.get('b756')
    out.append('')
    out.append('### ### **(8)(iii): CONTROLS %s ; OVER b756`S BANKS THE CARRIED READER %s, THE TAUGHT READER %s.**' % (
        'AS WANTED' if ok else 'NOT AS WANTED', 'UNREAD' if b6 is None else (len(b6['carried']) or 'NONE'),
        'UNREAD' if b6 is None else count(b6['direct'], b6['sends'])))
    text = NL.join(out) + NL
    print(text)
    if '--bank' in argv:
        io.open(BANK, 'w', encoding='utf-8', newline='\n').write(text)
        print('BANKED: data/b757_ghcalls.txt')
    return 0 if ok else 3


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
