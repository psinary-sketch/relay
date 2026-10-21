# -*- coding: utf-8 -*-
"""b701_record.py -- THE ACT'S RECORD TOOL, b701 under (R311).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b701 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly; b700's repaired _defect_short (the act PASSED AT THE CALL) carried by copy and
### rebound over b698's; b700's own late routes (capture over continuation sessions, reads, commands) carried here with b701's names and not
### imported, so that no b700 module rebinds b698's names after this tool's. The research routes -- the correspondence reading, the dispatch,
### the runner, the prints and the grade -- are b698's and b689's, carried by copy with b701's names (the runner's bank text names the act).
### Every python child is started as `python -X utf8`.
### Written by the Write tool at b701 in stages: stage one, step zero's routes; Components 2-5 by the Edit tool.
### Routes: `python tools/b701_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b701_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited
import b700_worklist as K700       # noqa: E402  ### data only

ACT, PREV = 'b701', 'b700'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b700 closed in its continuation session b858e03f (its post-push combine and closing there); this act opens a
# ### new session -- b698's form for a previous act in its own session: from the combine call to that session's end
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, 'b858e03f-d343-4bf2-9bb6-16946a3c8a59', 'RESUME b700 after a host reboot'
R.PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, R.PREV_SESSION)
R.PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, R.PREV_SESSION)
FACE = os.path.join(D, 'b701_registration_2026-10-21.txt')
FACE_REL = 'data/b701_registration_2026-10-21.txt'
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b700_closing_push_out.txt')
R.N5_RELAY_TOOLS = ()
R.ROOT_EXCLUDE = re.compile(r'^b701_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                            r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                            r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')


def _anchor_ts(anchor, session=None):
    """b698's _anchor_ts bound its session at definition (b699's trap 1): this one reads this act's session unless another is named."""
    return R._anchor_ts(anchor, session or SESSION)


R._anchor_ts = _anchor_ts


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        '%s_scores.json' % ACT: dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        '%s_findings.json' % ACT: dict(entry_line=99999, title='stand-in'),
        '%s_trail.json' % ACT: dict(line=99999),
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='6f32698e' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row, _deps = R.read_branch_row, R.read_runner_row, R._deps
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ (R310)(2), CARRIED: THE DEFECTS ROW READER, ITS ACT PASSED AT THE CALL
DEFECT_ROW = R.DEFECT_ROW


def read_defect_row(L, i):
    """one lettered defect row of a defects bank, its continuation lines joined: returns '(x) HEAD' -- the row's text to its first full stop."""
    j = i + 1
    while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
        j += 1
    m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
    return m.group(0)[:-1] if m else None


def _defect_short(act):
    """b700's repair, carried: the act PASSED AT THE CALL -- no default, so nothing is bound at import."""
    if not re.match(r'^b\d{3}$', act or ''):
        raise ValueError('### _defect_short NEEDS THE ACT AT THE CALL, read %r' % (act,))
    L = rdn('%s_defects.txt' % act).split(NL)
    return [s for s in (read_defect_row(L, i) for i, l in enumerate(L) if DEFECT_ROW.match(l)) if s]


R._defect_short = _defect_short
CLOSING_DEFECT = re.compile(r"and \(([a-z])\), (THE [A-Z']+), entered here[^:]*: (.*?) -- ")


def closing_defects(act):
    """b700's route, carried: the defects an act's closing enters in its (g) line and not in its defects bank."""
    L = rdn('%s_closing.txt' % act).split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('    (g) ')), None)
    if i is None:
        return []
    j = i + 1
    while j < len(L) and L[j].startswith('        '):
        j += 1
    text = ' '.join(x.strip() for x in L[i:j])
    return [('(%s) %s: %s' % (m.group(1), m.group(2), m.group(3)), 'data/%s_closing.txt :%d-:%d' % (act, i + 1, j)) for m in CLOSING_DEFECT.finditer(text)]


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    nb = len(out)
    out += closing_defects(act)
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt %d, FROM THE CLOSING`S (g) LINE %d.**' % (act, len(out), act, nb, len(out) - nb))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried)
rowgen, answers = R.rowgen, R.answers


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R311)(5); b700's form)
def branches(*a):
    """`branches before`: data/b701_branches_before.json -- b698's route, carried (every branch (R311)(5) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b701_branches.txt (.json) --
    each branch's fate read now against the tips banked before, in (R311)(5)'s words."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b701_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R311)(5): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b701_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[5:]))


# ================================================================================ THE LATE ROUTES (b700's, carried with b701's names)
import edit_route as ER            # noqa: E402


def capture():
    """b700's capture with the act's continuation sessions (K.SESSIONS_AFTER, b671's form): the seat's session from K.ANCHOR, then each
    continuation from its own anchor; a continuation that reads no command refuses."""
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in K.SESSIONS_AFTER:
        more = ER.capture('%s/%s.jsonl' % (PROJ, sid), anc, '%s/%s/subagents' % (PROJ, sid))
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
    rows.sort(key=lambda r: r['ts'])
    bg = R._bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


R.capture = capture
prev_capture = R.prev_capture      # ### b698's form: the previous act in its own session, from its post-push combine to that session's end


def reads(*a):
    """b700's route (data/b698_rules.txt row (2)) over the seat's session and its continuations."""
    rows = []
    for i, o, _st, sid in R._session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                p = inp.get('file_path') or ''
                rows.append(dict(line=i if sid == K.SESSION_ID else '%s:%d' % (sid[:8], i), ts=o.get('timestamp'), path=p, offset='offset' in inp,
                                 limit='limit' in inp, lines=R._lines_now(p)))
    whole = [r for r in rows if not (r['offset'] and r['limit'])]
    bad = [r for r in whole if r['lines'] is None or r['lines'] >= 200]
    L = ['%s -- THE READ CALLS SINCE THE ANCHOR, BY data/b698_rules.txt ROW (2) (%s)' % (ACT, utc()), '',
         '### the rule: whole where the file is under two hundred lines, by offset and limit otherwise. Rows are Read calls without both offset and',
         '### limit: transcript line | time | the file`s lines read now | WITHIN THE RULE or ### AN OFFENCE | path']
    L += ['  %s | %s | %s | %s | %s' % (r['line'], r['ts'], r['lines'], '### AN OFFENCE' if r in bad else 'WITHIN THE RULE', r['path']) for r in whole] or ['  NONE']
    L += ['', '### ### **READ CALLS %d ; WITH OFFSET AND LIMIT %d ; WHOLE %d ; WHOLE OF A FILE OF 200 LINES OR MORE %d.**' % (
        len(rows), len(rows) - len(whole), len(whole), len(bad))]
    if 'dry' not in a:
        put_txt('%s_read_calls.txt' % ACT, L)
    print(NL.join(L[-1 - len(bad):]) if bad else L[-1])


R.reads = reads
edit_route_offences = R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)


def commands(*a):
    """b700's route with b701's names in its bank text: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's
    window (b700's continuation session, from its post-push combine to that session's end), the local lean reading (N1), the dispatches (two
    at the most, N1), the detached runs, sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound
    requests. data/b701_commands.txt (.json)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if R.local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b(?![^\n]*\bdry\b)', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if R.sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    anypipe = [r for r in sh_ if '|' in QUOTED.sub('""', r['cmd']).replace('||', '')]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + R.delete_shape(r['cmd']) for r in mv if R.delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if R.delete_shape(r['cmd'])[0] and R.chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = R.outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES, THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts%s' % (
             K.SESSION_ID, K.ANCHOR, ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a_) for s, a_ in K.SESSIONS_AFTER)),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, its continuation session %s, from its post-push combine to that session`s '
              'end): %d commands from %s, its offences printed whole (%d):' % (PREV, R.PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, ONE PER TREE STATE, TWO AT THE MOST (N1; relay data/b701_dispatches.json) (%d):' % len(disp)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A PIPE OF ANY KIND, read outside quoted strings (%d):' % len(anypipe)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in anypipe] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R311)(5) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git AND gh (web searches, subagent prompts and fetches), each with the author`s identifiers found '
              'in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; PIPES OF ANY KIND %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(anypipe), len(pyreads), len(mv), good,
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    if 'dry' in a:
        print(L[-1])
        return
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act=PREV, session=R.PREV_SESSION, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], any_pipes=[r['n'] for r in anypipe], py_programs=[r['n'] for r in pyreads],
                                           moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after = R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after
_KERNS_698 = R._kerns


def _kerns():
    return _KERNS_698() + ['SIDE-substrate-cluster']     # ### b700's list, carried


R._kerns = _kerns


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    import b633_record as R3
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-explicit-formula read after its merges and tags; no kernel written after this read)' % len(ks))


def _standing():
    return sorted(set(R._g2_of(os.path.join(ROOT, *K.B700_FACE.split('/')))) - set(K700.ACT_ARMS))


R._standing = _standing


def standing(*a):
    """the standing arms b701 carries: b700's face's (G2) arms less b700's act arms (R264)(2); printed only."""
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, gatebanks, mbuild, mroot, mverify = R.desk, R.gatebanks, R.mbuild, R.mroot, R.mverify


def _one_git_write():
    """b698's reading with this act's session (its SESSION global is rebound above; the function reads the module global)."""
    return R._one_git_write()


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R311)(1)
WH = ('*Appended 2026-10-21 by b701 to b700’s entry (:9768), under `(R311)`(1) -- b700 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b700_closing.txt):*')
WB = (' “b700 closed: relay ac29fa81, PLACE-papers 71b23ac; suite 118 of 119; root 6f32698e1c7c0d9e…; 2 prompts answered; 2 defects” '
      '(data/b700_closing.txt :1), the closing 5623191e pushed and read back at relay main (data/b700_closing_push_out.txt :5). The act '
      'resumed after a host reboot with Components 0-3 found done, Component 4 partial and Component 5 not started, no memory file damaged '
      '(data/b700_resume.txt); the session repair in b671’s form at a7a85b41, the continuation b858e03f named in the worklist’s SESSIONS_AFTER '
      '(tools/b700_worklist.py :23), the capture and read routes over both sessions, repairs (7)-(9) at the carry -- the citation tool reading '
      'the new session, the rule arms’ trace over both sessions with rule_arms.py unedited, the closing’s head line counting correctly '
      '(data/b700_tool_repairs.txt). The corrigendum for b699’s trail line, head counts and the navigator’s root-named claim at FINDINGS :9752; '
      'the record tool’s _defect_short carried with its act at the call, its dry run printing four from two named sources '
      '(tools/b700_record.py :69). Reading 4 banked with the b680 and b690 values beside and its five added readings -- the defects by class '
      'with recurrence lag (185 in 18 classes, 17 standing sources, data/b700_reading4.txt :78), the roster-currency rows (35 papers, :90), the '
      'tags by ls-remote against the papers (:102), the circuit readings as census rows (:112), the regularity counts beside the bridge’s price '
      '(:121): 338 rows outside LICENSED/CITED, Correspondence 58 behind by b670’s method and 0 by the generator’s count, ONE-COPY 131 lines by '
      'cause. The slate for b701 priced (data/b700_slate.txt :54-:55). The gate CLEAR with both dry runs CLEAN and the trail’s Defects line equal '
      'to the defects bank (data/b700_reg_gate.txt), the lock gate 8 of 8, the face locked at sha256 ec20ccf2 with ten tools’ hashes at ecbbc502, '
      'the gate’s banks committed before the lock at a8c25b23 and named on the face; the entry at FINDINGS :9768, the trail at OPEN_TRAILS :15370, '
      'the root 6f32698e over 93 banks with the chain b624-b700 AGREE; suite 118 of 119 pre- and post-push, G-EDIT-ROUTE declared before the lock '
      'on the one sed of the resume’s memory check; all eight scores HELD (data/b700_scores_close.json); the closing written twice, the second '
      'carrying the scores read at the close (relay 5623191e); mirror-refresh-2026-10-21-b700.zip CLEAN with the root line (data/b700_mirror.txt). '
      'Two defects, the seat’s -- (a) the resume’s shell reads, pipes, redirects and the one sed, (b) two whole reads of files of two hundred lines '
      'or more before the reboot, entered late (data/b700_defects.txt :6-:20); the author’s root answer entered in the carried-forward (a), its '
      'check VACUOUS (data/b700_closing.txt :232-:236). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B700_ENTRY,
         check=[('FINDINGS.md', K.B700_ENTRY, '## Reading 4: 338 rows outside license'), ('OPEN_TRAILS.md', K.B700_TRAIL, '### b700')], dry=dry)


# ================================================================================ COMPONENT 2: THE RESTATEMENT READ BY THE CORRESPONDENCE READER, (R311)(2), N2
import circuit_correspondence as CC   # noqa: E402  ### the reader, imported unedited (its own main writes b698's banks; not called)
EF, LV = K.EF_DIR, K.LV_DIR
EF_RESTATE = ('SIDEExplicitFormula/ResidueDischarge.lean', 'Register4_positivity')
LV_STATE = ('SIDELvConservation/RegisterPentagon.lean', 'Register4_positivity')
EF_K4 = ('SIDEExplicitFormula/ResidueDischarge.lean', 'register4_positivity_liCoeff_imp_rh')


def _def_sig(src, name):
    """a `def NAME <binders> : Prop := <body>` read as a statement for the reader: '<binders> : <body>' (the Prop-valued definition's binders and
    its body as the proposition), with its line span."""
    L = src.split(NL)
    i = next(k for k, l in enumerate(L) if l.startswith('def %s ' % name) or l.startswith('def %s(' % name))
    j = next(k for k in range(i, len(L)) if ':=' in L[k])
    m = j
    while m + 1 < len(L) and L[m + 1].startswith('  ') and L[m + 1].strip():
        m += 1
    head = ' '.join(NL.join(L[i:j + 1]).split('def %s' % name, 1)[1].rsplit(':=', 1)[0].split())
    body = ' '.join((NL.join(L[j:m + 1]).split(':=', 1)[1]).split())
    # ### the source writes `∀ n : ℕ,` where #print writes `∀ (n : ℕ),`: the one bracketing the reader's from_pi reads, applied to both sides alike
    body = re.sub(r'∀ ([^(){}\[\]∀,]+?) : ([^,]+?),', r'∀ (\1 : \2),', body)
    binders = head.rsplit(': Prop', 1)[0].strip()
    return i + 1, m + 1, '%s : %s' % (binders, body), NL.join(L[i:m + 1])


def _thm_sig(src, name):
    L = src.split(NL)
    i = next(k for k, l in enumerate(L) if l.startswith('theorem %s ' % name))
    j = next(k for k in range(i, len(L)) if ':= by' in L[k] or L[k].rstrip().endswith(':='))
    st = NL.join(L[i:j + 1])
    head = st.split('theorem %s' % name, 1)[1].rsplit(':=', 1)[0]
    return i + 1, j + 1, ' '.join(head.split()).lstrip(': ').strip(), st


def _show_rows(rows, a_name, b_name):
    out = []
    for r in rows:
        if r[0] == 'conclusion':
            out += ['  conclusion | %s: %s' % (a_name, r[1]), '             | %s: %s' % (b_name, r[2]), '             | %s | %s' % (r[3], r[4])]
        else:
            out += ['  binder %-3s | %s: %s' % (r[0], a_name, CC.show_binder(r[1])), '             | %s: %s' % (b_name, CC.show_binder(r[2])),
                    '             | %s | %s' % (r[3], r[4])]
    return out


def corr(*a):
    """`corr` (before the theorem is written) / `corr after <tag> <run id>` (the CLAUSE-DOMINANCE re-read after the merge): the restatement
    SIDEExplicitFormula.ResidueDischarge.Register4_positivity (source text at the kernel's main, the hosted print step printing axioms alone) read
    by tools/circuit_correspondence.py against SIDE-lv-conservation's Register4_positivity at v0.13.0 (source text at the tag, as b698 read the
    face), binder by binder; the K4 theorem against the face's binder 13 at lam := LiCoeff; and b698's direct reading (h2_sign against
    residue_irreducible) re-run. Controls first. data/b701_correspondence_restatement.txt (.json) / data/b701_clause_dominance.txt (.json)."""
    after = bool(a) and a[0] == 'after'
    tag, run_id = (a[1], a[2]) if after and len(a) > 2 else ('', '')
    ef_rev = tag if after else 'main'
    ei, ej, esig, etext = _def_sig(_show(EF, ef_rev, EF_RESTATE[0]), EF_RESTATE[1])
    li, lj, lsig, ltext = _def_sig(_show(LV, K.LV_V0130, LV_STATE[0]), LV_STATE[1])
    A = CC.from_signature(esig) + ('SIDE-explicit-formula',)
    B = CC.from_signature(lsig) + ('SIDE-lv-conservation',)
    # ### the controls
    r1, v1 = CC.compare(A, A)
    planted = (list(B[0]), B[1], B[2])
    planted[0][0] = (planted[0][0][0], planted[0][0][1], 'ℕ → ℤ')
    r2, v2 = CC.compare(A, tuple(planted))
    c1_ok = v1 == 'HOLDS-BY-CORRESPONDENCE' and all(r[3] == 'AGREE' for r in r1)
    c2_ok = v2 == 'DIFFERS at binder 1' and [r[3] for r in r2] == ['DIFFERS'] + ['AGREE'] * (len(r2) - 1)
    # ### reading 1: the restatement against lv's statement
    rows, v = CC.compare(A, B)
    # ### reading 2: K4 against the face's binder 13 at lam := LiCoeff
    fi_, fj_, fsig = CC.lv_source()
    F = CC.from_signature(fsig)
    b13 = F[0][12]
    b13t = re.sub(r'(?<![\w.])lam(?![\w])', 'LiCoeff', b13[2])
    ki, kj, ksig, ktext = _thm_sig(_show(EF, ef_rev, EF_K4[0]), EF_K4[1])
    K4 = CC.from_pi(ksig) + ('SIDE-explicit-formula',)
    B13 = CC.from_pi(b13t) + ('SIDE-lv-conservation',)
    rows2, vb = CC.compare(K4, B13)
    # ### reading 3: b698's direct reading, re-run
    a1, b1_, stmt, value = CC.h2_print()
    H2 = CC.from_pi(value) + ('SIDE-explicit-formula',)
    FR = F + ('SIDE-lv-conservation',)
    rows3, v3 = CC.compare(H2, FR)
    fd = next((r for r in rows3 if r[3] == 'DIFFERS'), None)
    bridge = ''
    if after:
        bi, bj, bsig, btext = _thm_sig(_show(EF, ef_rev, K.BRIDGE_FILE), K.BRIDGE_NAMES[0].rsplit('.', 1)[1])
        rr = [r for r in (jl('%s_runner_rows.json' % ACT).get('rows') or []) if str(r.get('run_id')) == str(run_id)]
        bridge = 'the bridge theorem %s at %s %s :%d-:%d: %s -- its run %s %s' % (K.BRIDGE_NAMES[0], tag, K.BRIDGE_FILE, bi, bj, bsig, run_id,
                                                                                   rr[0].get('gate') if rr else '### NO RUNNER ROW')
    name = '%s_clause_dominance' % ACT if after else '%s_correspondence_restatement' % ACT
    L = ['%s -- %s (%s)' % (ACT, ('CLAUSE-DOMINANCE RE-READ BY CORRESPONDENCE OVER BOTH FACES` KERNELS AFTER THE BRIDGE, (R311)(2)' if after else
                                'THE RESTATEMENT READ BY THE CORRESPONDENCE READER BEFORE THE BRIDGE THEOREM IS WRITTEN, (R311)(2), N2'), utc()), '',
         '### the reader: relay tools/circuit_correspondence.py, imported unedited (from_signature, from_pi, compare; spec relay data/b695_circuit_spec.txt',
         '### :53-:64). Rows are binders aligned by position: position | the first statement`s binder | the second`s | AGREE or DIFFERS | why (namespaces',
         '### stripped, bound names read by position). A Prop-valued definition is read as its binders and its body; SOURCE AGAINST SOURCE: the hosted',
         '### print step prints #print axioms alone, so neither definition has a hosted #print sig (b698`s reading of lv`s face, the same fallback).', '',
         '== THE CONTROLS, PRINTED BEFORE THE REAL READING',
         '  (C1) the restatement against itself: %s' % v1]
    L += ['       %-10s | %-40s | %-40s | %s' % (r[0], CC.show_binder(r[1]) if r[0] != 'conclusion' else r[1][:40], CC.show_binder(r[2]) if r[0] != 'conclusion' else r[2][:40], r[3]) for r in r1]
    L += ['  (C2) the restatement against a planted lv statement, binder 1`s type ℕ → ℝ changed to ℕ → ℤ: %s' % v2]
    L += ['       %-10s | %-40s | %-40s | %s' % (r[0], CC.show_binder(r[1]) if r[0] != 'conclusion' else r[1][:40], CC.show_binder(r[2]) if r[0] != 'conclusion' else r[2][:40], r[3]) for r in r2]
    L += ['  ### ### **CONTROLS: C1 HOLDS AT EVERY BINDER %s ; C2 DIFFERS AT THE PLANTED BINDER (1) AND THERE ALONE %s.**' % (c1_ok, c2_ok), '',
          '== THE SOURCES',
          '  the restatement: SIDE-explicit-formula %s %s :%d-:%d (%s), source text:' % (ef_rev, EF_RESTATE[0], ei, ej, g(EF, 'rev-parse', '--short=7', ef_rev).strip())]
    L += ['      ' + x for x in etext.split(NL)]
    L += ['  lv-conservation`s statement: SIDE-lv-conservation v0.13.0 = %s %s :%d-:%d, source text (b698 read the face at ZeroActingPartial.lean :%d-:%d):' % (
        K.LV_V0130[:7], LV_STATE[0], li, lj, fi_, fj_)]
    L += ['      ' + x for x in ltext.split(NL)]
    L += ['  the face`s binder 13 (ZeroActingPartial.lean, residue_irreducible): %s ; at lam := LiCoeff: %s' % (CC.show_binder(b13), b13t),
          '  K4: SIDE-explicit-formula %s %s :%d-:%d: %s' % (ef_rev, EF_K4[0], ki, kj, ksig)]
    if bridge:
        L += ['  ' + bridge]
    L += ['', '== READING 1: THE RESTATEMENT (SIDE-explicit-formula, SOURCE) AGAINST Register4_positivity (SIDE-lv-conservation, SOURCE) -- binders %d against %d' % (len(A[0]), len(B[0]))]
    L += _show_rows(rows, 'restatement', 'lv')
    L += ['', '== READING 2: K4 (SIDE-explicit-formula) AGAINST THE FACE`S BINDER 13 AT lam := LiCoeff (SIDE-lv-conservation)']
    L += _show_rows(rows2, 'K4', 'binder 13')
    L += ['', '== READING 3: b698`S DIRECT READING RE-RUN -- h2_sign (PRINT, relay data/b643_probe_out_zeta.txt :%d-:%d) AGAINST residue_irreducible (SOURCE)' % (a1, b1_)]
    L += ['  %s' % ('%s: h2_sign`s %s against residue_irreducible`s %s' % (v3, CC.show_binder(fd[1]), CC.show_binder(fd[2])) if fd is not None and fd[0] != 'conclusion' else v3),
          '  AGREE %d ; DIFFERS %d of %d rows -- unchanged from data/b698_correspondence_dominance.txt :76-:77' % (
              sum(1 for r in rows3 if r[3] == 'AGREE'), sum(1 for r in rows3 if r[3] != 'AGREE'), len(rows3))]
    holds = v == 'HOLDS-BY-CORRESPONDENCE' and vb == 'HOLDS-BY-CORRESPONDENCE'
    if after:
        verdict = ('CLAUSE-DOMINANCE BY CORRESPONDENCE OVER BOTH FACES` KERNELS: 2 OF 2 THROUGH THE RESTATEMENT -- THE RESTATEMENT AGAINST lv`S STATEMENT %s ; '
                   'K4 AGAINST BINDER 13 AT lam := LiCoeff %s ; THE JOIN h2_sign ↔ Register4_positivity LiCoeff COMPILED AT %s ; THE DIRECT READING OF THE TWO '
                   'STATEMENTS %s AS b698 READ IT ; CONTROLS C1 %s, C2 %s' % (v, vb, tag, v3, c1_ok, c2_ok)) if holds else (
                   'CLAUSE-DOMINANCE BY CORRESPONDENCE: THE RESTATEMENT %s ; K4 AGAINST BINDER 13 %s ; CONTROLS C1 %s, C2 %s' % (v, vb, c1_ok, c2_ok))
    else:
        verdict = ('THE RESTATEMENT AGAINST lv-CONSERVATION`S STATEMENT: %s AT EVERY BINDER (%d BINDERS AND THE CONCLUSION) ; K4 AGAINST THE FACE`S BINDER 13 AT '
                   'lam := LiCoeff: %s ; b698`S DIFFERS AT BINDER 1 LOCATED IN THE RESTATEMENT AND CLOSED: THE CLAUSE REACHES THE FACE AT BINDER 13 THROUGH THE '
                   'RESTATED PREDICATE, THE JOIN TO BE COMPILED AS S1 ; CONTROLS C1 %s, C2 %s ; THE THEOREM MAY BE WRITTEN %s' % (
                       v, len(A[0]), vb, c1_ok, c2_ok, holds and c1_ok and c2_ok)) if holds else (
                   'THE RESTATEMENT AGAINST lv-CONSERVATION`S STATEMENT: %s ; K4 AGAINST BINDER 13: %s ; THE ACT STOPS HERE WITH THE READING BANKED (N2) ; CONTROLS '
                   'C1 %s, C2 %s' % (v, vb, c1_ok, c2_ok))
    L += ['', '### ### **%s.**' % verdict]
    put_txt('%s.txt' % name, L)
    put_json('%s.json' % name, dict(at=utc(), reading1=v, reading2=vb, reading3=v3, controls=dict(c1=c1_ok, c2=c2_ok), holds=holds, after=after, tag=tag, run_id=run_id,
                                    rows1=[[r[0], CC.show_binder(r[1]) if r[0] != 'conclusion' else r[1], CC.show_binder(r[2]) if r[0] != 'conclusion' else r[2], r[3], r[4]] for r in rows],
                                    rows2=[[r[0], CC.show_binder(r[1]) if r[0] != 'conclusion' else r[1], CC.show_binder(r[2]) if r[0] != 'conclusion' else r[2], r[3], r[4]] for r in rows2]))
    print(NL.join(L[6:9] + L[-1:]))
    if not (holds and c1_ok and c2_ok) and not after:
        sys.exit(1)


# ================================================================================ COMPONENT 2: THE ORDERS' ANNOTATION ON THE AUTHOR'S WORD AT THE DISCHARGE PROMPT, (R311)(2)
ORDER_H = ('*Appended 2026-10-21 by b701 beneath `W-ORD-H2-BRIDGE-THEOREM` (:15334; `W-ORD-H2-BRIDGE` :10257, annotated at :15200 and :15294), under '
           '`(R311)`(2) and the author’s word at the discharge prompt -- THE ORDERS **`W-ORD-H2-BRIDGE`** AND **`W-ORD-H2-BRIDGE-THEOREM`** DISCHARGED:*')
ORDER_B = (' the bridge compiled at SIDE-explicit-formula v0.35 = d4e046a (SIDEExplicitFormula/RegisterBridge.lean, merged from bridge-b701 on the '
           'gate’s reading): h2_sign_iff_register4_positivity_liCoeff, h2_sign ↔ Register4_positivity LiCoeff := h2_sign_iff_rh.trans '
           'register4_positivity_liCoeff_iff_rh.symm, the hosted run 39635057369 DERIVES (the artifact’s sha256 agreeing with the platform’s digest, 74 '
           'of 74 terminals at the standard three), the grade read from the statement DERIVES with every salt-check passed (relay data/b701_grade.txt). '
           'The reader’s readings (relay data/b701_correspondence_restatement.txt, before the theorem was written; data/b701_clause_dominance.txt, after '
           'the merge): the restatement ResidueDischarge.Register4_positivity against SIDE-lv-conservation v0.13.0’s Register4_positivity '
           'HOLDS-BY-CORRESPONDENCE at every binder, K4 against the face’s binder 13 at lam := LiCoeff HOLDS-BY-CORRESPONDENCE, CLAUSE-DOMINANCE by '
           'correspondence 2 of 2 through the restatement; the direct reading of h2_sign against residue_irreducible DIFFERS at binder 1 as b698 read '
           'it. In the author’s words: the join is an equivalence compiled through RH between h2_sign and the register face as restated in '
           'SIDE-explicit-formula, the restatement reading HOLDS-BY-CORRESPONDENCE against lv-conservation’s statement at every binder, and not an '
           'object-to-object translation, the direct reading at binder 1 standing as b698 read it; and lv-conservation’s own kernel still holds no '
           'import of the bridge, its lakefile forbidding it, so for that kernel the link remains the faces page’s Correspondence row, now pointing at '
           'a compiled theorem by tag (the successor row drafted in relay data/b701_faces_rows.txt, held for b702’s regeneration prompt). Status '
           'DISCHARGED.')


def order(*a):
    """the orders' annotation at OPEN_TRAILS on the author's word (discharge): landed by the guarded route beneath W-ORD-H2-BRIDGE-THEOREM's line;
    refuses where the readings' banks do not carry their verdicts."""
    cd = rdn('%s_clause_dominance.txt' % ACT)
    gr = rdn('%s_grade.txt' % ACT)
    if '2 OF 2 THROUGH THE RESTATEMENT' not in cd or 'EVERY SALT-CHECK PASSED True' not in gr or 'v0.35' not in cd:
        sys.exit('### THE READINGS` BANKS DO NOT CARRY THEIR VERDICTS -- NOTHING WRITTEN')
    land([('OPEN_TRAILS.md', ORDER_H, NL + ORDER_H + ORDER_B + NL)], '%s_order_line.json' % ACT, 'order', entry=10257,
         check=[('OPEN_TRAILS.md', 10257, '(2) **`W-ORD-H2-BRIDGE`**'), ('OPEN_TRAILS.md', K.BRIDGE_ORDER, 'beneath `W-ORD-H2-BRIDGE`')],
         dry='dry' in a)


# ================================================================================ COMPONENTS 2-3: THE DISPATCH, THE RUNNER, THE PRINTS (b698's routes; the runner's text with this act's name)
dispatch, runstatus = R.dispatch, R.runstatus
STD3 = ('Classical.choice', 'Quot.sound', 'propext')


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: b698's route carried by copy with this act's name in its bank text (b699's trap 3)."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = R._gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['%s -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (ACT, kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
        if digest and digest == sha:
            row['artifact_sha256'] = sha
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    row['stopped'] = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    row['build_exit'] = T_.get('build_exit.txt', '').strip() or None
    row['errors'] = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    ax = T_.get('axioms.txt', '').rstrip(NL)
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = _deps(ax)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d ; refused %s' % (
              len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), row['gate'])]
    read_runner_row(row)
    put_txt('%s_runner_%s_%s.txt' % (ACT, kernel, label), L)
    if row['artifact_sha256']:
        put_txt('%s_axioms_%s_%s.txt' % (ACT, kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, kernel, label), blog.rstrip(NL).split(NL))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank> <stem>`: the 'before' terminals' lines compared with the same names' lines in the 'after' bank
    by name; the new names listed apart (b689's form). data/b701_prints_<stem>.txt."""
    kernel, bb, ab, stem = a[0], a[1], a[2], a[3]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['%s -- THE PRINTS OF %s: THE TERMINALS PRINTED BEFORE AND AFTER THE BRANCH, BY NAME (%s)' % (ACT, kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; rows are the terminals that differ:' % (bb, len(bd), ab, len(fd))] + (
             ['    %s : %s | %s' % d for d in diff] or ['    NONE']) + ['### the names printed after and not before (the branch`s new names): %d' % len(new)] + [
             '    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL BY NAME %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), not diff)]
    put_txt('%s_prints_%s.txt' % (ACT, stem), L)
    print(L[-1])


# ================================================================================ COMPONENTS 2-3: THE GRADE AND THE SALT-CHECK (b689's route, generalized by name)
# ### the seat's reading of each statement's binders by hand, BEFORE the E0 check (b689's form): name -> (file, [(binder, class, why)], grade, premise)
GRADES = {
    'h2_sign_iff_register4_positivity_liCoeff': (K.BRIDGE_FILE, 'SIDEExplicitFormula.RegisterBridge.', [],
                                                 'DERIVES', 'NONE (no binder; an equivalence of two closed propositions of this kernel)'),
    'h2_sign_imp_pairing_rh': (K.BRIDGE_FILE, 'SIDEExplicitFormula.RegisterBridge.',
                               [('Pairing', '(ℕ → ℝ) → (ℕ → ℝ) → (ℕ → ℝ) → Prop', 'a predicate on two channels and a ledger, data: lv`s ZeroActingPairing left free'),
                                ('lam_A lam_Z', 'ℕ → ℝ', 'two real sequences, data, no hypothesis')],
                               'DERIVES', 'NONE (h2_sign is the antecedent inside the stated implication, not a binder; S2 adds nothing beyond S1)'),
}
E0_EXTENSION = {'h2_sign': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2Sign.lean :29'),
                'Register4_positivity': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/ResidueDischarge.lean :30'),
                'RiemannHypothesis': ('prop', 'Mathlib RiemannHypothesis'),
                'ZeroActingPairing': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2Bridge.lean (restated from SIDE-lv-conservation v0.13.0)')}


def grade(*a):
    """`grade <rev> <stem> <name> [<name> ...]`: data/b701_grade_<stem>.txt -- each theorem's statement verbatim from the branch at rev, the seat's
    reading of its binders by hand and the grade it gives, the shared E0 rule's grade as the check (its lexicon extended here, the shared file not
    edited), the salt-check of REGISTRY.md :544 clause by clause, the runner's print of the name."""
    import e0_rule as E
    rev, stem, names = a[0], a[1], list(a[2:])
    E.LEXICON.update(E0_EXTENSION)
    rows_ = jl('%s_runner_rows.json' % ACT).get('rows') or []
    run = next((r for r in rows_ if (r.get('ref') or '').startswith(g(EF, 'rev-parse', rev).strip()[:7])), None)
    ax = rdn('%s_axioms_%s_%s.txt' % (ACT, run['kernel'], run['label'])) if run else ''
    AX = dict(_deps(ax))
    L = ['%s -- THE GRADE OF EACH THEOREM, READ FROM ITS STATEMENT, AND THE SALT-CHECK, (R311)(2)-(3) (%s)' % (ACT, utc()), '',
         '### rows are, per theorem: the statement verbatim, the binders with their class read by hand, the grade they give, the E0 rule`s check, and',
         '### the salt-check`s clauses with their readings. The statements at SIDE-explicit-formula %s (%s); the profile from run %s.' % (
             rev[:7], g(EF, 'rev-parse', '--short=7', rev).strip(), run['run_id'] if run else '### NO RUN'), '']
    allok, summ = True, []
    for name in names:
        fpath, ns, hand, hgrade, hprem = GRADES[name]
        i, j, head, st = _thm_sig(_show(EF, rev, fpath), name)
        eg, why, read = E.grade(' ' + head + ' ', 'theorem')
        prof = AX.get(ns + name)
        concl = E.conclusion(E.statement_only(' ' + head + ' ')) or head
        salt = [('no True-typed conclusion, no uniformly-True predicate', not re.search(r'\bTrue\b', concl), 'the conclusion %r is an iff or an implication between named Props of two kernels, neither True' % concl.strip()[:80]),
                ('no X = X', not re.search(r'\b(\w+)\s*=\s*\1\b', concl), 'no equation in the conclusion'),
                ('no hypothesis that is the claim', all(concl.strip() not in (t or '') for _n, t in read) if read else True, 'hypotheses %s' % ([n for n, _t in read] or 'none')),
                ('no fabricated witness', '∃' not in concl, 'the conclusion constructs nothing'),
                ('hypotheses named', all(n for n, _t in read) if read else True, ', '.join('%s : %s' % x for x in read) or 'no binder'),
                ('#print axioms profiled after the first three', prof is not None and set(prof) <= set(STD3), 'run %s: %s' % (run['run_id'] if run else '### NO RUN', prof))]
        ok = all(s[1] for s in salt)
        allok = allok and ok
        L += ['== %s (%s :%d-:%d):' % (name, fpath, i, j)] + ['    ' + l for l in st.split(NL)]
        L += ['  THE BINDERS, READ BY HAND (the seat`s reading, before the check): %s' % ('NONE -- a closed statement' if not hand else '')]
        L += ['    %-12s : %-28s %s' % b for b in hand]
        L += ['  THE GRADE READ FROM THE STATEMENT: %s ; THE NAMED PREMISE: %s' % (hgrade, hprem),
              '  THE CHECK: relay tools/e0_rule.py`s grade() on the header, its LEXICON extended in this tool (E0_EXTENSION; the shared file not edited):',
              '    E0 GRADE %s ; its reason: %s ; the hypotheses it read: %s' % (eg, why, read),
              '    THE HAND READING AND THE CHECK %s' % ('AGREE' if eg == hgrade else '### DIFFER (%s against %s)' % (hgrade, eg)),
              '  THE SALT-CHECK (REGISTRY.md :544), clause by clause:']
        L += ['    %-55s %s -- %s' % (c, 'PASS' if ok_ else '### FAIL', how) for c, ok_, how in salt]
        L += ['  PROFILE %s ; SALT-CHECK %s' % (prof, 'PASS' if ok else '### FAIL'), '']
        summ.append('%s GRADE %s (E0 %s) SALT %s PROFILE %s' % (name, hgrade, eg, 'PASS' if ok else 'FAIL', 'STD3' if prof is not None and set(prof) <= set(STD3) else prof))
    L += ['### ### **THEOREMS %d ; %s ; EVERY SALT-CHECK PASSED %s.**' % (len(names), ' ; '.join(summ), allok)]
    put_txt(('%s_grade.txt' % ACT) if stem == 'bridge' else ('%s_grade_%s.txt' % (ACT, stem)), L)   # ### (R311)(2) names data/b701_grade.txt for the bridge
    print(NL.join(L[-3:]))


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, commands=commands, reads=reads,
              rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, c1=c1, kernels=kernels, standing=standing,
              armsecs=armsecs, desk=desk, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, corr=corr, dispatch=dispatch,
              runstatus=runstatus, runner=runner, prints=prints, grade=grade, order=order)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b701_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
