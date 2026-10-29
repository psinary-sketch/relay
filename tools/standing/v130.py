# -*- coding: utf-8 -*-
"""standing/v130.py -- THE CONTROLS OF v1.3.0 ((R333)(2)), each on b722's banks with both instances shown. Written at b723 by the Write tool.

  python -X utf8 tools/standing/v130.py control [ii|iii|iv|i ...] [--bank]
        runs the named controls (all where none is named) and prints each case AS WANTED or NOT AS WANTED; --bank writes
        data/<act>_standing_v130.txt (the act read from data/act_current.json) with every control run, nothing else.

(ii) THE PIPE-FREE READER, tools/standing/peek.py: every hook refusal line of b720-b722 (data/b720_hook_refusals.txt,
     data/b721_hook_refusals.txt, data/b722_hook_refusals.txt) re-run through it, the hook unchanged. For each line: the hook's own
     judge() (tools/standing/hook.py, imported, its refusal writer never called) read on the logged call gives the logged kind; the line's
     peek calls (written by hand from what the refused call read, below) each judged ALLOWED by the same judge() as the shell line the seat
     would type, and each run (no shell) to exit 0. A refused call that was not a read -- an edit, a tool's run captured to a file -- is
     classed NOT A READ, its route named, and has no peek call; a read peek covers only in part is COVERED IN PART, what it leaves named.
     hook.py's sha256 read before and after, equal to its blob at HEAD. The bank prints the calls by verb and argument count and the
     output's line count; a memory file's path or text, never.
"""
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
sys.path.insert(0, S)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A          # noqa: E402
import hook as H         # noqa: E402

PP = 'D:/MY-DOwnloads/PLACE-papers'
PEEK = 'tools/standing/peek.py'
SCR = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/02c7cf38-4c6a-4f88-b813-a7e15e9b85b4/scratchpad'
LOGGED = object()   # ### a READ row's peek path: the path the refusal line logged, read from the line at run time
COVERED, PART, NOT_READ = 'COVERED', 'COVERED IN PART', 'NOT A READ'

# ### (bank, line): (class, [peek argv, ...], what is left or the route)
PLAN = {
    ('b720', 1): (COVERED, [['search', 'SIDE-[a-z-]+ [^|]{0,40}', PP + '/REGISTRY.md', '--lines', '700-770', '--cut', '160']], ''),
    ('b720', 2): (COVERED, [['head', PP + '/day1/A_Place_to_Stand.md', '14', '--cut', '260']], ''),
    ('b720', 3): (COVERED, [['search', '-i', 'tier KC', '--of', "git -C %s grep -n -i -E 'tier KC|KC =' -- '*.md' ':!internal' ':!meta'" % PP, '--max', '40']], ''),
    ('b720', 4): (COVERED, [['head', '--of', "git -C D:/relay log --format='%h %s' -12", '12', '--cut', '90'],
                            ['head', '--of', "git -C %s log --format='%%H %%s' -3" % PP, '3', '--cut', '90']], ''),
    ('b720', 5): (NOT_READ, [], 'an edit of tools/b720_record.py by a heredoc: the Edit tool'),
    ('b720', 6): (COVERED, [['list', 'D:/relay/tools', '--glob', 'b720_*.py']], ''),
    ('b720', 7): (NOT_READ, [], 'a tool`s dry run with its output discarded: the tool run plainly, its output read'),
    ('b720', 8): (COVERED, [['search', 'GATE VERDICT', 'D:/relay/data/b720_reg_gate.txt']], ''),
    ('b720', 9): (COVERED, [['head', '--of', "git -C D:/relay log --format='%h %s' -40 --grep=b719", '40']], ''),
    ('b720', 10): (COVERED, [['count', '--of', 'git -C %s diff -U0 1553808a~1 1553808a -- FINDINGS.md' % PP, '--pattern', '^-[^-]']], ''),
    ('b720', 11): (COVERED, [['head', LOGGED, '200']], ''),
    ('b720', 12): (COVERED, [['head', LOGGED, '200']], ''),
    ('b720', 13): (COVERED, [['head', '--of', "git -C D:/relay log --format='%h %s' -45 --reverse", '45', '--cut', '200']], ''),
    ('b721', 1): (COVERED, [['count', 'D:/relay/tools/b720_c1.py']], ''),
    ('b721', 2): (COVERED, [['search', r'n\*_pred|r\(rho\)', 'D:/relay/data/b713_predictions.txt', 'D:/relay/data/b717_predictions.txt',
                             'D:/relay/data/b717_onsets.txt', 'D:/relay/data/b714_residual.txt', 'D:/relay/data/b719_registrations.txt', '--cut', '260']], ''),
    ('b721', 3): (COVERED, [['search', 'theorem (archimedean_forces_half|indicial_forces_half)', '--of',
                             "git -C D:/SIDE-archimedean grep -n -E 'theorem archimedean_forces_half' 8019d9d"]], ''),
    ('b721', 4): (NOT_READ, [], 'a tool`s bank run captured to a scratch file: the tool`s own bank route, its bank read by peek tail'),
    ('b721', 5): (COVERED, [['search', 'NOTHING COMPOSED', 'D:/relay/tools', '--max', '20']], ''),
    ('b721', 6): (PART, [['search', r'K\.[A-Z][A-Z0-9_]*', 'D:/relay/tools/b721_record.py', '--max', '20'],
                         ['search', '^[A-Z][A-Z0-9_]* *=', 'D:/relay/tools/b721_worklist.py', '--cut', '150']],
                  'the tally by name (`sort | uniq -c`) is not a peek verb: a scratch reader'),
    ('b721', 7): (PART, [['list', 'D:/relay/data', '--glob', 'b71*_count_route*']], 'the inline `python -c` read of data/arm_tags.json: a scratch reader'),
    ('b721', 8): (COVERED, [['search', '-i', '^"(python|lean|lake)', '--of', 'tasklist /fo csv /nh']], ''),
    ('b721', 9): (COVERED, [['head', LOGGED, '200']], ''),
    ('b721', 10): (COVERED, [['head', LOGGED, '200']], ''),
    ('b721', 11): (COVERED, [['list', SCR, '--sort', 'time', '--max', '80'], ['head', 'D:/relay/data/b721_ferry_scan.txt', '--bytes', '1500']], ''),
    ('b721', 12): (COVERED, [['list', 'D:/relay/tools/standing'], ['head', 'D:/relay/tools/standing/VERSION', '1'], ['list', 'D:/relay/tools/research']], ''),
    ('b722', 1): (COVERED, [['count', 'D:/relay/tools/b711_coeffs.py', 'D:/relay/tools/b720_coeffs.py']], ''),
    ('b722', 2): (NOT_READ, [], 'a tool`s dry run captured to a scratch file, then an inline `python -c`: the tool`s own bank route'),
    ('b722', 3): (COVERED, [['list', 'D:/relay/tools/research'], ['list', 'D:/relay/tools/standing']], ''),
    ('b722', 4): (COVERED, [['search', '-i', 'coverage table', 'D:/relay/tools/standing', 'D:/relay/tools/act_close.py', '--cut', '220', '--max', '20']], ''),
    ('b722', 5): (COVERED, [['head', LOGGED, '200']], ''),
    ('b722', 6): (COVERED, [['head', LOGGED, '200']], ''),
    ('b722', 7): (COVERED, [['search', r'^### ### \*\*', 'D:/relay/data/b722_propagation.txt', 'D:/relay/data/b722_axiom_diag.txt',
                             'D:/relay/data/b722_llm_line_drafts.txt', 'D:/relay/data/b722_reproduce.txt', '--cut', '200'],
                            ['list', 'D:/relay/data', '--glob', 'b722_*'], ['search', r'^VERSION|^  \(82\)', 'D:/relay/data/standing_clauses_v8.txt']], ''),
    ('b722', 8): (COVERED, [['search', r'^if __name__|^def sources|NEED\[', 'D:/relay/tools/b722_checks.py', '--max', '5']], ''),
    ('b722', 9): (PART, [['search', '-i', 'score', 'D:/relay/tools/b722_record.py', '--max', '40', '--cut', '160'],
                         ['head', '--of', 'git -C D:/relay show 30c0b3c8:tools/b721_record.py', '40']],
                  'the read by byte offset (`body[229845:241338]`) is not a peek verb: peek reads by line (--lines)'),
    ('b722', 10): (COVERED, [['search', '.', PP + '/phase1.5/method/INSTRUMENTS.md', '--lines', '634-634', '--cut', '170'],
                             ['search', '.', PP + '/phase1.5/method/INSTRUMENTS.md', '--lines', '762-762', '--cut', '170'],
                             ['search', '.', PP + '/FINDINGS.md', '--lines', '11284-11286', '--cut', '170']], ''),
}


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def parse_line(l):
    """(stamp, kind, tool, the logged call's text, detail) of one refusal line; the text json-decoded where it decodes, else as logged
    (the hook cut it at 300 characters, which can leave the quotation open)."""
    p = l.split(' | ')
    if len(p) < 5:
        return None
    stamp, kind, tool, detail = p[0], p[1], p[2], p[-1]
    shown = ' | '.join(p[3:-1])
    try:
        text = json.loads(shown)
    except ValueError:
        try:
            text = json.loads(shown + '"')
        except ValueError:
            text = shown.strip('"')
    return stamp, kind, tool, text, detail


def logged_input(tool, text, detail):
    if tool == 'Read':
        m = re.search(r'limit (\d+)', detail)
        return {'file_path': text, 'limit': int(m.group(1)) if m else None}
    return {'command': text}


def shell_line(argv):
    return 'python -X utf8 %s %s' % (PEEK, ' '.join(shlex.quote(a) for a in argv))


def control_ii():
    L = ['## (ii) THE PIPE-FREE READER, tools/standing/peek.py: the hook refusals of b720-b722 re-run through it, the hook unchanged']
    hp = os.path.join(S, 'hook.py')
    h0, hb = sha(hp), hashlib.sha256(A.git('relay', 'show', 'HEAD:tools/standing/hook.py') or b'').hexdigest()
    cases = []
    for act in ('b720', 'b721', 'b722'):
        lines = [x for x in A.rd('%s_hook_refusals.txt' % act).split(NL) if x.strip()]
        for n, l in enumerate(lines, 1):
            pl = parse_line(l)
            plan = PLAN.get((act, n))
            if pl is None or plan is None:
                cases.append((act, n, '?', False, 'the line unread or unplanned'))
                continue
            stamp, kind, tool, text, detail = pl
            j = H.judge(tool, logged_input(tool, text, detail))
            same = j is not None and j[0] == kind
            cls, calls, left = plan
            runs = []
            for argv in calls:
                argv = [text if a is LOGGED else a for a in argv]
                allowed = H.judge('Bash', {'command': shell_line(argv)}) is None
                r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(S, 'peek.py')] + argv, capture_output=True, cwd=RELAY)
                out = r.stdout.decode('utf-8', 'replace').replace('\r', '')   # ### the child prints CRLF on this host: an anchored match needs the CR gone
                n_out = len([x for x in out.split(NL) if x.strip()])
                shown_args = [('<the logged path>' if a == text and tool == 'Read' else a) for a in argv]
                # ### a source peek could not read prints its own line "peek: <path> ABSENT"; a bank's text carrying the word is not one
                absent = any(re.match(r'^peek: .* ABSENT$', x) for x in out.split(NL))
                # ### search and count may find nothing in sources read (a clean read is a result); head and list must print
                need = argv[0] in ('head', 'tail', 'list')
                runs.append(dict(verb=argv[0], args=len(argv) - 1, allowed=allowed, rc=r.returncode, lines=n_out, absent=absent,
                                 printed_ok=n_out > 0 or not need, shown=shown_args))
            # ### the hook cuts the logged call at 300 characters (hook.py refuse(), json.dumps(...)[:300]): where the cut fell before the
            # ### refused character the line cannot show its own kind -- printed TRUNCATED, a finding of the bank's form, not a change of the hook
            cut_at = len(json.dumps(text, ensure_ascii=False)) >= 299 and len(l.split(' | ', 3)[3].rsplit(' | ', 1)[0]) >= 300
            trunc = j is None and cut_at
            same = same or trunc
            ok = same and (cls == NOT_READ and not calls or cls != NOT_READ and runs and all(
                x['allowed'] and x['rc'] == 0 and x['printed_ok'] and not x['absent'] for x in runs))
            why = 'the logged %s call judged %s (logged %s)%s' % (tool, j[0] if j else 'ALLOWED', kind,
                                                                  ' -- TRUNCATED: the hook`s 300-character cut fell before the refused character' if trunc else '')
            cases.append((act, n, cls, ok, why, runs, left))
    for c in cases:
        if len(c) == 5:
            L.append('  (ii) %s :%d %-16s %s -- NOT AS WANTED' % c[:3] + (c[4],))
            continue
        act, n, cls, ok, why, runs, left = c
        L.append('  (ii) %s_hook_refusals.txt :%-2d %-16s %s ; %s -- %s' % (
            act, n, cls, why, '; '.join('peek %s (%d args): %s, exit %d, %d lines' % (x['verb'], x['args'], 'ALLOWED' if x['allowed'] else 'REFUSED',
                                                                                         x['rc'], x['lines']) for x in runs) or 'no peek call',
            'AS WANTED' if ok else 'NOT AS WANTED'))
        if left:
            L.append('       %s' % left)
    # ### the plants: the judge and the ABSENT reading each shown able to fire
    pj = H.judge('Bash', {'command': shell_line(['head', 'D:/relay/data/b722_closing.txt', '5']) + ' | head -3'})
    pr = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(S, 'peek.py'), 'head', 'D:/relay/data/b723_planted_absent.txt', '5'], capture_output=True, cwd=RELAY)
    pa = any(re.match(r'^peek: .* ABSENT$', x) for x in pr.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL))
    plants = [('a peek line with a pipe appended, judged PIPE', bool(pj) and pj[0] == 'PIPE'),
              ('a peek read of a path that does not exist, printing ABSENT', pa)]
    for w, ok in plants:
        L.append('  (ii) PLANTED: %s -- %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED'))
    h1 = sha(hp)
    hook_ok = h0 == h1 == hb and all(ok for _w, ok in plants)
    L.append('  (ii) the hook unchanged: tools/standing/hook.py sha256 %s before, %s after, its blob at HEAD %s -- %s' % (
        h0[:16], h1[:16], hb[:16], 'AS WANTED' if hook_ok else 'NOT AS WANTED'))
    by = {}
    for c in cases:
        by[c[2]] = by.get(c[2], 0) + 1
    good = sum(1 for c in cases if len(c) > 5 and c[3]) + (1 if hook_ok else 0)
    L.append('  (ii) LINES %d (b720 %d, b721 %d, b722 %d) ; %s ; CASES AS WANTED %d OF %d' % (
        len(cases), sum(1 for c in cases if c[0] == 'b720'), sum(1 for c in cases if c[0] == 'b721'), sum(1 for c in cases if c[0] == 'b722'),
        ', '.join('%s %d' % (k, v) for k, v in sorted(by.items())), good, len(cases) + 1))
    return L, good, len(cases) + 1


CONTROLS = dict(ii=control_ii)


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in argv[1:] if a in CONTROLS] or sorted(CONTROLS)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.3.0, (R333)(2), ON b722`S BANKS (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '']
    tg = tn = 0
    for k in names:
        L, g, n = CONTROLS[k]()
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.3.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v130.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v130.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
