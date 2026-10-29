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


def _git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '')


def _log(repo, a, b):
    out = []
    for l in _git(repo, 'log', '--reverse', '--format=%h %ct %s', '%s..%s' % (a, b)).split(NL):
        if l.strip():
            p = l.split(' ', 2)
            out.append((p[0], p[2] if len(p) > 2 else '', int(p[1])))
    return out


def control_iii():
    """(iii) THE LOCK ROW, on b722's steps bank beside b722's event (5): b722's instance of G-SEALED-AFTER-COMPONENTS and b723's (the fold's
    renders, tools/standing/fold.py), each read on b722's bank as banked and on copies changed in memory; b723's phases read from
    data/act_current.json, `lock` among the record tool's step phases."""
    import types
    sys.path.insert(0, T)
    import fold as F
    F.install()
    import importlib
    L = ['  (iii) THE LOCK ROW -- the step recorder takes `lock`; G-SEALED-AFTER-COMPONENTS reads the lock commit by that phase']
    ev = (open(os.path.join(D, 'b722_events.txt'), encoding='utf-8').read().replace('\r', '').split(NL))[20:24]
    L += ['  (iii) b722`s event (5), data/b722_events.txt :21-:24:'] + ['      ' + l.strip() for l in ev]
    C2 = importlib.import_module('b722_checks')
    C3 = importlib.import_module('b723_checks')
    R2 = importlib.import_module('b722_record')
    R3 = importlib.import_module('b723_record')
    ac2 = json.loads(_git(RELAY, 'show', '1607e994:data/act_current.json'))
    head_r, head_p = '65430407', ac2.get('pre_pp') and A.current()['pre_pp']
    rows = json.load(open(os.path.join(D, 'b722_steps.json'), encoding='utf-8'))['rows']
    k26 = [i for i, r in enumerate(rows) if r['commit'].startswith('794b7bc7')]
    L.append('  (iii) b722`s steps bank: %d rows ; the lock commit 794b7bc7 at step %s, phase %r' % (
        len(rows), ', '.join(str(i + 1) for i in k26), rows[k26[0]]['phase'] if k26 else None))
    face = open(C2.FACE, encoding='utf-8').read()
    S = dict(steps=rows, rlog=_log(RELAY, ac2['pre_relay'], head_r), plog=_log(PP, ac2['pre_pp'], head_p),
             lock_epoch=C2.utc_epoch(face, 'locked at (UTC)'), REC=types.SimpleNamespace(PRE_SEAL_PHASES=R2.PRE_SEAL_PHASES))
    L.append('  (iii) b722`s logs read: relay %s..%s %d commits, PLACE-papers %s..%s %d ; the face`s lock %s' % (
        ac2['pre_relay'][:8], head_r, len(S['rlog']), ac2['pre_pp'][:8], head_p[:8], len(S['plog']),
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(S['lock_epoch'])) if S['lock_epoch'] else None))
    plant = [dict(r, phase='lock') if i in k26 else r for i, r in enumerate(rows)]
    gate = [i for i, r in enumerate(rows) if r['phase'] == 'gate' and i not in k26]
    plant2 = [dict(r, phase='lock') if (i in k26 or i == (gate[0] if gate else -1)) else r for i, r in enumerate(rows)]
    cases = [
        ('b722`s instance on b722`s bank as banked (b722 banked it failing, event (5))', C2.sealed_after_ok(S), False),
        ('b723`s instance on b722`s bank as banked: no `lock` row, step 26 reads `gate`', C3.sealed_after_ok(S), False),
        ('b723`s instance on b722`s bank with step 26`s phase `lock` (in memory)', C3.sealed_after_ok(dict(S, steps=plant)), True),
        ('b723`s instance with a second `lock` row, b722`s gate commit %s (in memory)' % (rows[gate[0]]['commit'][:8] if gate else '-'),
         C3.sealed_after_ok(dict(S, steps=plant2)), False),
    ]
    good = 0
    for w, got, want in cases:
        ok = bool(got) == want
        good += ok
        L.append('  (iii) %s: %s -- %s' % (w, 'PASS' if got else 'FAIL', 'AS WANTED' if ok else 'NOT AS WANTED'))
    L.append('  (iii) beside them, not counted: b722`s instance on the step-26 copy %s (b722`s reads the lock by the face`s time alone)' % (
        'PASS' if C2.sealed_after_ok(dict(S, steps=plant)) else 'FAIL'))
    pre, post = R3.PRE_SEAL_PHASES, R3.POST_SEAL_PHASES
    ph_ok = pre[-2:] == ('gate', 'lock') and post == ('seal', 'pre-root', 'root', 'record', 'closing') and 'lock' in R3.STEP_PHASES \
        and 'lock' not in R2.STEP_PHASES
    good += ph_ok
    L.append('  (iii) b723`s phases from data/act_current.json: pre-seal %s ; post-seal %s ; `lock` a step phase of b723`s recorder %s, of b722`s %s -- %s' % (
        list(pre), list(post), 'lock' in R3.STEP_PHASES, 'lock' in R2.STEP_PHASES, 'AS WANTED' if ph_ok else 'NOT AS WANTED'))
    return L, good, len(cases) + 1


def _arms_table(text):
    """[(arm, live predicate text)] -- each ARMS entry of a checks render: its name and the text of its first lambda (the live predicate)."""
    out = []
    # ### the description may run over lines or carry a comment after it: everything to the entry's first `lambda S:` skipped; the live
    # ### predicate runs to the next line opening `lambda S:` (the NEG plant), a comment line between them allowed
    for m in re.finditer(r"(?m)^\s*\(\s*'(G-[A-Z0-9-]+)',(?:(?!^\s*\(\s*'G-).)*?(lambda S: .*?)(?=,\s*(?:#[^\n]*\n\s*)*\n\s*lambda S:|\)\s*,\s*\n)",
                         text, re.S):
        out.append((m.group(1), m.group(2)))
    return out


def _bodies(text):
    """{function name: body text} of a render's top-level functions."""
    out = {}
    for m in re.finditer(r'(?m)^def (\w+)\(.*?(?=^\S)', text + '\nEND\n', re.S):
        out[m.group(1)] = m.group(0)
    return out


def _module_banks(paths):
    """{function name: set of act-bank names} -- each top-level function of the given modules and the act banks it reads by an act-parametric
    name ('%s_<name>' % act, or '<act>_<name>' after a render), the names written with the act as `%s`."""
    out = {}
    for p in paths:
        try:
            src = open(p, encoding='utf-8').read()
        except OSError:
            continue
        mod = os.path.basename(p)[:-3]
        for fn, body in _bodies(src).items():
            bs = set(re.findall(r"'%s_([\w%%.-]+\.(?:txt|json|gz))'", body))
            if bs:
                out.setdefault('%s.%s' % (mod, fn), set()).update('%s_' + b for b in bs)
    return out


# ### the module functions reading a bank no longer written, graded by hand (each read in its module, reason printed); one ungraded fails
HAND_IV_MOD = {
    'act_close.author_words': 'CONDITIONAL: the author`s word after the seal, None where the act has no such bank (its docstring); read by the record tools',
    'allow.words_of': 'CONDITIONAL: the author`s-words banks, written where the author`s words come mid-act; read by G-DELETES-ONE-BRANCH (graded above)',
    'hook.control': 'A WRITER: the hook`s own control writes data/<act>_hook_control.txt when run',
    'hook.instance_constructed': 'THE HOOK CONTROL`S CONSTRUCTED CASE: a planted old bank, written and read in that control alone',
    'readfirst.hand_ok': 'READS FOR ABSENCE: the retirement`s own check (the closure bank absent, the hand list standing), called by v122.py alone',
    'v122.lines': 'b722`S v1.2.2 CONTROLS: reads the closure bank for its absence on b721`s and b722`s banks',
    'v121.main': 'A WRITER: v1.2.1`s controls bank, written by its own route (b721)',
    'classes.main': 'A WRITER: the classes controls bank, written by its own route',
    'replay.main': 'A WRITER: the replay bank, written by its own route',
    'roster.main': 'A WRITER: the roster bank, written by its own route',
    'scan.main': 'A WRITER: the standing scan bank, written by its own route',
    'repairs.main': 'A WRITER: the tool-repairs bank, written by its own route',
    'controls.main': 'A WRITER: the standing controls bank, written by its own route',
    'controls.minted': 'READS THE HISTORY: the first chain act with a standing controls bank, read over every act',
}


# ### THE HAND TABLE of (iv): each arm the trace finds reading a bank no longer written, graded by hand with its reason (v8 row (82)'s
# ### propagation read: a grade the rule cannot give is given here, printed); an arm the trace finds and this table does not grade fails.
HAND_IV = {
    'G-READFIRST-DIFF-BANKED': ('RETIRED THIS ACT', 'reads data/<act>_readfirst_diff.txt, the closure reader`s diff; (R332)(2)(iii) retired the reader '
                                'and b722 wrote no diff (event (6)); (R333)(2)(iv) retires the arm with it'),
    'G-DELETES-ONE-BRANCH': ('STANDS: A CONDITIONAL BANK', 'reads the author`s-words banks through tools/standing/allow.py words_of '
                             '(data/<act>_author_words_preseal.txt, data/<act>_author_words.txt), written where the author`s words come mid-act '
                             '(b714, b715, b718), not retired; b723 owes them for its two mid-act words'),
    'G-MUSTFAIL': ('STANDS: READS FOR ABSENCE', 'the suite`s own control, `a file that must not exist`: passes while data/<act>_mustnotexist.txt is absent'),
    'G-DIFFERS-ERRATA': ('STANDS: READS FOR ABSENCE', 'wants no differs and no errata bank this act (`not S[\'differs\'] and not S[\'errata\']`)'),
    'G-STEPZERO-TESTS': ('STANDS: READS FOR ABSENCE', 'wants no tests bank and nothing withheld at a step zero that ran no test (tests_ok)'),
}


def control_iv():
    """(iv) THE PROPAGATION READ OVER THE SUITE'S ARMS (v8 row (82) run with the object `a bank no longer written`): G-READFIRST-DIFF-BANKED
    retired with the reader (R332)(2)(iii) retired; every arm b722's suite ran, in b723's render, traced to the act banks it reads -- its live
    predicate and the functions it calls to depth three, the checks render's own (their state keys, each to the banks sources() reads into
    it) and the standing and arm modules' (each function's act-parametric bank names) -- and every bank graded by what the acts before
    wrote: WRITTEN (b722, tracked at its close 1607e994), STOPPED (b721, at 30c0b3c8, and not b722), STOPPED EARLY (the newest act bank of
    that name in the history before b721), NEVER. Every arm reading a stopped bank is graded by the hand table HAND_IV with its reason, and
    one the table does not grade fails; the rule printed before the read."""
    import fnmatch
    sys.path.insert(0, T)
    import fold as F
    F.install()
    act = A.current()['act']
    L = ['  (iv) THE RULE, before the read: an arm reads a bank where its live predicate, or a function it calls (to depth three), reads a state',
         '       key sources() fills from data/%s_<name>, or is a module function reading data/<act>_<name>; each bank graded by the acts' % act,
         '       before as written (WRITTEN b722 / STOPPED at b721 / STOPPED EARLY / NEVER); a %s or %d in a name read as any text; every',
         '       arm reading a stopped bank graded by hand (HAND_IV), one ungraded failing.']
    text = F.render(act, 'checks')
    bodies = _bodies(text)
    src = bodies.get('sources', '')
    keys = {}
    pos = [(m.start(), m.group(1)) for m in re.finditer(r'(?m)(?:^\s+|,\s*)([a-z_][a-z0-9_]*)=(?!=)', src)]
    for k, (p, name) in enumerate(pos):
        seg = src[p:pos[k + 1][0] if k + 1 < len(pos) else len(src)]
        bs = set(b.replace(act, '%s', 1) for b in re.findall(r"'(%s_[\w%%.-]+\.(?:txt|json|gz))'" % act, seg))
        if bs:
            keys.setdefault(name, set()).update(bs)
    mods = [os.path.join(S, f) for f in sorted(os.listdir(S)) if f.endswith('.py') and f not in ('v130.py', 'fold.py', 'legacy.py', 'peek.py')] + \
        [os.path.join(T, f) for f in ('rule_arms.py', 'b719_arms.py', 'act_close.py', 'act_letters.py', 'b703_checks.py', 'b704_read_arm.py')]
    mfn = _module_banks(mods)
    tracked = {}
    for rev, a in (('1607e994', 'b722'), ('30c0b3c8', 'b721')):
        tracked[a] = [x[5:] for x in _git(RELAY, 'ls-tree', '-r', '--name-only', rev, '--', 'data/').split(NL) if x.startswith('data/%s_' % a)]
    memo = {}

    def grade(b):
        if b in memo:
            return memo[b]
        glob = b.replace('%s', '*', 1) if b.startswith('%s') else b
        glob = glob.replace('%s', '*').replace('%d', '*')
        g = None
        for a, gr in (('b722', 'WRITTEN'), ('b721', 'STOPPED')):
            if any(fnmatch.fnmatch(x, glob.replace('*', a, 1) if b.startswith('%s') else glob) for x in tracked[a]):
                g = (gr, a)
                break
        if g is None:
            suf = b[2:].replace('%s', '*').replace('%d', '*')
            hist = sorted(set(x for x in _git(RELAY, 'log', '--all', '--name-only', '--format=', '--',
                                              ':(glob)data/b[67][0-9][0-9]%s' % suf).split(NL) if x))
            g = ('STOPPED EARLY', hist[-1][5:9]) if hist else ('NEVER', None)
        memo[b] = g
        return g

    def reads(expr, depth):
        ks = set(re.findall(r"S\['(\w+)'\]", expr))
        bs = set(b for k in ks for b in keys.get(k, ()))
        for fn in set(re.findall(r'\.(\w+)\(', expr)):
            for k, v in mfn.items():
                if k.split('.', 1)[1] == fn:
                    bs |= v
        if depth:
            for fn in set(re.findall(r'(?<![\w.])(\w+)\(', expr)):
                if fn in bodies and fn != 'sources':
                    bs |= reads(bodies[fn], depth - 1)
        return bs

    arms = dict(_arms_table(text))
    banked = []
    for part in ('standing-a', 'standing-c', 'standing-b1', 'standing-b3', 'act'):
        p = os.path.join(D, 'b722_checks_postpush_%s.txt' % part)
        banked += re.findall(r'(?m)^  (G-[A-Z0-9-]+)\s+(?:PASS|FAIL)', open(p, encoding='utf-8').read())
    run = [a.replace('G-R332-', 'G-R333-') for a in banked]           # ### the carry's one rename
    allb = sorted(set(b for v in keys.values() for b in v) | set(b for v in mfn.values() for b in v))
    by = {}
    for b in allb:
        by.setdefault(grade(b)[0], []).append(b)
    L.append('  (iv) b722`s suite ran %d arms ; in b723`s render`s table %d ; act banks read by the checks render or the modules %d: %s' % (
        len(run), sum(1 for a in run if a in arms), len(allb), ', '.join('%s %d' % (g, len(v)) for g, v in sorted(by.items()))))
    for g in ('STOPPED', 'STOPPED EARLY', 'NEVER'):
        for b in by.get(g, []):
            L.append('  (iv) %-13s data/%s%s' % (g, b.replace('%s', '<act>', 1), '' if g != 'STOPPED EARLY' else '   (the newest: %s)' % grade(b)[1]))
    per, untraced = {}, []
    for a in run:
        if a in arms:
            per[a] = sorted(b for b in reads(arms[a], 3) if grade(b)[0] != 'WRITTEN')
        else:
            untraced.append(a)
    readers = dict((a, v) for a, v in per.items() if v)
    good = n = 0
    for a, bs in sorted(readers.items()):
        g = HAND_IV.get(a)
        n += 1
        good += g is not None
        L.append('  (iv) %-26s reads %s ; %s -- %s' % (a, ', '.join('data/' + b.replace('%s', '<act>', 1) for b in bs),
                                                    ('%s: %s' % g) if g else 'NOT GRADED', 'AS WANTED' if g else 'NOT AS WANTED'))
    L.append('  (iv) the arms b722`s suite ran outside the render`s table %d, not traced to banks by this rule: %s' % (len(untraced), ', '.join(untraced)))
    mods_stopped = {}
    for fn, bs in mfn.items():
        for b in bs:
            if grade(b)[0] != 'WRITTEN':
                mods_stopped.setdefault(fn, []).append(b)
    for fn, bs in sorted(mods_stopped.items()):
        g = HAND_IV_MOD.get(fn)
        n += 1
        good += g is not None
        L.append('  (iv) module %-26s names %s ; %s -- %s' % (fn, ', '.join('data/' + b.replace('%s', '<act>', 1) for b in sorted(bs)),
                                                           g or 'NOT GRADED', 'AS WANTED' if g else 'NOT AS WANTED'))
    orphan = sorted(b for b in allb if grade(b)[0] != 'WRITTEN' and not any(b in v for v in readers.values()))
    L.append('  (iv) stopped banks no run arm reads (read by sources() or a module function alone): %s' % (
        ', '.join('data/' + b.replace('%s', '<act>', 1) for b in orphan) or 'NONE'))
    # ### both instances: the arm in b722's render, traced, reads the stopped bank; in b723's render it is gone
    arms722 = dict(_arms_table(F.render('b722', 'checks')))
    rfd = arms722.get('G-READFIRST-DIFF-BANKED')
    c1 = rfd is not None and '%s_readfirst_diff.txt' in reads(rfd, 3) and grade('%s_readfirst_diff.txt')[0] == 'STOPPED'
    in_table = 'G-READFIRST-DIFF-BANKED' in arms
    L.append('  (iv) b722`s instance: G-READFIRST-DIFF-BANKED in its table, traced to data/<act>_readfirst_diff.txt, graded STOPPED: %s -- %s' % (
        c1, 'AS WANTED' if c1 else 'NOT AS WANTED'))
    L.append('  (iv) G-READFIRST-DIFF-BANKED in b723`s arms table: %s -- %s' % (in_table, 'NOT AS WANTED (not yet retired)' if in_table else 'AS WANTED (retired)'))
    return L, good + int(c1) + int(not in_table), n + 2, dict(readers=readers, by=by, orphan=orphan)


def _iv():
    L, g, n, _x = control_iv()
    return L, g, n


def control_b():
    """(b), the root answer's at b723's step zero: (R333)(2)(i) covers the seal route's own list of sealed tools, read from the worklist's
    SEALED, so one list feeds both. b722's instance: its rule's list (close.sealed_list) against its worklist's SEALED, the difference
    tools/research/reproduce.py (event (12)); b723's: the seal route's list (close.worklist_sealed) equal to the worklist's SEALED, the
    compute tool and the fold's files among it."""
    import importlib
    sys.path.insert(0, T)
    import fold as F
    F.install()
    import close as C
    act = A.current()['act']
    L = ['  (b) THE SEAL ROUTE`S LIST READ FROM THE WORKLIST`S SEALED']
    w2 = sorted(importlib.import_module('b722_worklist').SEALED)
    r2 = C.sealed_list('b722')
    d2 = sorted(set(w2) ^ set(r2))
    w3 = sorted(importlib.import_module('%s_worklist' % act).SEALED)
    s3 = C.worklist_sealed(act)
    fold_in = all(x in s3 for x in ('standing/fold.py', 'standing/legacy.py', 'acts/%s.py' % act)) and \
        sum(1 for x in s3 if x.startswith('standing/fold/') and x.endswith('.tpl')) == 7
    cases = [('b722`s instance: the rule`s list %d against the worklist`s SEALED %d, differing by %s (event (12))' % (len(r2), len(w2), d2),
              d2 == ['research/reproduce.py']),
             ('b723`s seal route`s list %d equal to its worklist`s SEALED %d' % (len(s3), len(w3)), s3 == w3),
             ('tools/research/reproduce.py in b723`s sealed list', 'research/reproduce.py' in s3),
             ('the fold`s files in b723`s sealed list (fold.py, legacy.py, the seven templates, tools/acts/%s.py)' % act, fold_in)]
    good = 0
    for w, ok in cases:
        good += ok
        L.append('  (b) %s -- %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED'))
    return L, good, len(cases)


def control_i():
    """(i) THE CLOSE TOOLS TAKE THE ACT (the author's word, Option 2: the seven folded into tools/standing/fold.py): the build's controls run
    by tools/<act>_fold.py and their lines carried here -- the text control (every render of b722 and b721 equal to its file byte for byte,
    b723's base render to its landed tools, a plant differing), the names control (the planted missing name refused), the --prev names
    computed beside the hand list (every name both worklists carry owned alike; the --prev reading itself carried to the pre-seal run,
    its sources reading the components' commits) -- and the run control on b722's banks, read from data/<act>_fold_run.txt."""
    act = A.current()['act']
    L, good, n = ['  (i) THE SEVEN CLOSE TOOLS FOLDED: tools/standing/fold.py, its templates and the act`s arms module'], 0, 0
    for verb in ('text', 'names', 'prevnames'):
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, '%s_fold.py' % act), verb], capture_output=True, cwd=RELAY)
        out = r.stdout.decode('utf-8', 'replace').replace('\r', '').rstrip(NL).split(NL)
        L += ['  (i) %s: %s' % (verb, l.strip()) for l in out]
        n += 1
        good += r.returncode == 0 and bool(out) and 'ALL' in out[-1] and 'NOT AS WANTED' not in out[-1] and 'DIFFERS' not in out[-1]
    p = os.path.join(D, '%s_fold_run.txt' % act)
    run = open(p, encoding='utf-8').read().replace('\r', '').rstrip(NL).split(NL) if os.path.isfile(p) else []
    L += ['  (i) run: %s' % l.strip() for l in run] or ['  (i) run: ### data/%s_fold_run.txt ABSENT' % act]
    n += 1
    good += any('EQUAL ARM FOR ARM -- AS WANTED' in l for l in run)
    return L, good, n


CONTROLS = dict(i=control_i, ii=control_ii, iii=control_iii, iv=_iv, b=control_b)


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
