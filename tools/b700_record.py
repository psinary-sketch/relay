# -*- coding: utf-8 -*-
"""b700_record.py -- THE ACT'S RECORD TOOL, b700 under (R310).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b700 -- its worklist
### module K, ACT and PREV -- as b699 imported it; b699's own routes (its branches, commands and late routes) are carried here with b700's
### names and not imported, so that no b699 module rebinds b698's names after this tool's. (R310)(2): the record tool's _defect_short is
### carried with its act PASSED AT THE CALL and not bound at import (b698_record.py :367 bound `act=ACT` at definition, 'b698', and b699's
### sealed trail landed b698's four defects for b699's); b698's own function is rebound here to the repaired one, which takes no default, so
### any carried call that omits the act refuses instead of reading another act's bank. Every python child is started as `python -X utf8`.
### Written by the Write tool at b700 in stages: stage one, step zero's routes; Components 1-5 by the Edit tool.
### Routes: `python tools/b700_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b700_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited

ACT, PREV = 'b700', 'b699'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show

READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row']
read_branch_row = R.read_branch_row
read_runner_row, _deps = R.read_runner_row, R._deps   # ### the standing runner arms read b699's runs (no runner this act) through b698's reader


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank (b699's, with b700's names)."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        '%s_scores.json' % ACT: dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        '%s_findings.json' % ACT: dict(entry_line=99999, title='stand-in'),
        '%s_trail.json' % ACT: dict(line=99999),
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='4f7afcb3' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins


# ================================================================================ (R310)(2): THE DEFECTS ROW READER, ITS ACT PASSED AT THE CALL
DEFECT_ROW = R.DEFECT_ROW


def read_defect_row(L, i):
    """one lettered defect row of a defects bank, its continuation lines joined: returns '(x) HEAD' -- the row's text to its first full stop,
    as b698's _defect_short composed it."""
    j = i + 1
    while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
        j += 1
    m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
    return m.group(0)[:-1] if m else None


def _defect_short(act):
    """(R310)(2): b698_record._defect_short with its act PASSED AT THE CALL -- no default, so nothing is bound at import; the bank read is
    data/<act>_defects.txt for the act the caller names."""
    if not re.match(r'^b\d{3}$', act or ''):
        raise ValueError('### _defect_short NEEDS THE ACT AT THE CALL, read %r' % (act,))
    L = rdn('%s_defects.txt' % act).split(NL)
    return [s for s in (read_defect_row(L, i) for i, l in enumerate(L) if DEFECT_ROW.match(l)) if s]


R._defect_short = _defect_short    # ### the carried function rebound to the repaired one: a call without the act now refuses


CLOSING_DEFECT = re.compile(r"and \(([a-z])\), (THE [A-Z']+), entered here[^:]*: (.*?) -- ")


def closing_defects(act):
    """(R310)(2) on the author's answer at b700 (Option 1): the defects an act's closing enters in its (g) line and not in its defects bank --
    b699's (d), entered there on the author's word at the root's prompt. Returns [(row, 'data/<act>_closing.txt :<first>-:<last>')]."""
    L = rdn('%s_closing.txt' % act).split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('    (g) ')), None)
    if i is None:
        return []
    j = i + 1
    while j < len(L) and L[j].startswith('        '):
        j += 1
    text = ' '.join(x.strip() for x in L[i:j])
    return [('(%s) %s: %s' % (m.group(1), m.group(2), m.group(3)), 'data/%s_closing.txt :%d-:%d' % (act, i + 1, j))
            for m in CLOSING_DEFECT.finditer(text)]


def defshort(*a):
    """the repair's dry run: `defshort <act>` prints the act's lettered defects as the trail route composes them -- the defects bank by the
    repaired reader (its act at the call), then any defect the closing's (g) line enters outside the bank, each row with its source; writes
    nothing."""
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    nb = len(out)
    out += closing_defects(act)
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt %d, FROM THE CLOSING`S (g) LINE %d.**' % (act, len(out), act, nb, len(out) - nb))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS (b698's routes, carried)
rowgen, answers = R.rowgen, R.answers


def defects(*a):
    """b698's route with the act passed at the call (its own call at b698_record.py :384 read the default)."""
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R310)(5); b699's form)
def branches(*a):
    """`branches before`: data/b700_branches_before.json -- b698's route, carried (every branch (R310)(5) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b700_branches.txt (.json) --
    each branch's fate read now against the tips banked before, in (R310)(5)'s words."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b700_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R310)(5): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b700_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[4:]))


# ================================================================================ THE LATE ROUTES (b698's, carried with b700's names)
import b699_worklist as K699       # noqa: E402  ### data only
import edit_route as ER            # noqa: E402
SESSION, SUBAGENTS = R.SESSION, R.SUBAGENTS
# ### the previous act's window: b699 ran in this same session (c677eaf2) -- the same-session form (b695's, b699's): b699's capture from the
# ### call that combined its post-push parts to this act's anchor
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.SESSION_ID, K699.ANCHOR
R.PREV_SESSION_PATH, R.PREV_SUBAGENTS = SESSION, SUBAGENTS


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act, same-session form: b699's capture AFTER ITS POST-PUSH SUITE -- every command of this session
    from the call that combined b699's post-push parts into data/b699_checks_postpush.txt to the first user line carrying (R310)'s anchor."""
    rows = ER.capture(SESSION, K699.ANCHOR, SUBAGENTS)
    first = [r['ts'] for r in rows if 'b699_checks_postpush' in r['cmd'] and '--combine' in r['cmd']]
    end = R._anchor_ts(K.ANCHOR)
    if not first or not end:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE OR THIS ACT`S ANCHOR IS NOT IN THE SESSION -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV, r['src'])) for r in rows if first[0] <= r['ts'] < end]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


R.prev_capture = prev_capture
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'


def capture():
    """b698's capture with the act's continuation sessions (K.SESSIONS_AFTER, b671's form): the seat's session from K.ANCHOR, then each
    continuation from its own anchor, its source labelled by the session; a continuation that reads no command refuses."""
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


def reads(*a):
    """b698's route (data/b698_rules.txt row (2)) over the seat's session and its continuations: a continuation's transcript line labelled by
    its session (b698's answers form), the rule and the bank unchanged."""
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
    """b699's route with b700's names in its bank text: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's
    window (same session), the local lean reading (N1), the dispatches, the detached runs, sed, the redirects, the pipes, the one-line programs,
    the moves and deletes by shape, the outbound requests. data/b700_commands.txt (.json)."""
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
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts%s' % (
             K.SESSION_ID, K.ANCHOR, ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a_) for s, a_ in K.SESSIONS_AFTER)),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, this same session %s, from its post-push combine to this act`s '
              'anchor): %d commands from %s, its offences printed whole (%d):' % (PREV, K.SESSION_ID[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (NONE ORDERED THIS ACT, (N1)) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R310)(5) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
                                           prev=dict(act=PREV, session=K.SESSION_ID, rows=len(prev),
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
read_score_row, read_head, _anchor_ts = R.read_score_row, R.read_head, R._anchor_ts
READERS += ['read_score_row', 'read_head']

R.ROOT_EXCLUDE = re.compile(r'^b700_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                            r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                            r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R310)(1)
WH = ('*Appended 2026-10-21 by b700 to b699’s entry (:9726), under `(R310)`(1) -- b699 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b699_closing.txt):*')
WB = (' “b699 closed: relay 144cc457, PLACE-papers 049855a; suite 121 of 121; root 4f7afcb30a75e63c…; 4 prompts answered; 3 defects” '
      '(data/b699_closing.txt :1), the closing 85dd43d7 pushed and read back at relay main (data/b699_closing_push_out.txt :5); the head '
      'line undercounting on both counts -- five prompts put, the fifth, at the trail, after the answers bank’s one write; four defects, (d) '
      'in the closing’s (g) line alone (:240-:244) -- each count corrected by b700’s generated corrigendum (FINDINGS :9752). b698’s weight '
      'line at :9710 and its corrigendum at :9712 naming the two pre-lock commits 2d19edd3 and 069778f6 by hash, the answers bank’s bytes '
      'equal to the root’s row, ONE-COPY 6 stored and 18 counted, corrigenda rows (11)-(13). SIDE-substrate-cluster re-cut alone at the top '
      'count, b674’s tie-break printed and not reached: T7Labeling.lean :19-:20 retired to the errata, comment lines alone, both runs DERIVES '
      'with the prints equal line for line, 0 quoting lines, merged at 0c98a9a and tagged v0.4.1 naming v0.4, the distance 1 to 0 '
      '(data/b699_cut.txt :40); no roster table naming the kernel, nothing written, THE_TWO_THREE_SUBSTRATE’s pinned rows entered as a '
      'roster-currency row for b700. The SIDE-archimedean cells written by the generator alone at PATHS_TO_THE_CRITICAL_LINE_v0_7 :285 '
      '(v0.1.1, the profile, DERIVES); the partner copy differing in 24 lines against the 4 stored, entered beneath W-ORD-ONE-COPY '
      '(OPEN_TRAILS :15332). W-ORD-H2-BRIDGE-THEOREM entered at :15334, priced in data/b699_bridge_plan.txt with all 14 binders and their '
      'translations -- at binder 1 no translation object to object in either kernel; S1, h2_sign ↔ Register4_positivity LiCoeff, DERIVES '
      'expected through RH by two theorems v0.34 already compiles; one dispatch; nothing compiled. Suite 121 of 121 pre- and post-push, 93 '
      'standing and 28 act arms, every control behaving, section (0) naming every pre-lock commit by hash; all eight scores HELD '
      '(data/b699_scores_close.json); mirror-refresh-2026-10-21-b699.zip CLEAN with the root line. Four defects, all the seat’s -- (a) a '
      'pipe in an opening read, (b) two banks read through the shell’s grep, (c) a glob in the --list branch listings before the deletes '
      '(data/b699_defects.txt :6-:20), (d) the trail at OPEN_TRAILS :15336 listing b698’s four defects for b699’s, from a default bound at '
      'import in b698_record._defect_short carried by reference in the sealed b699_record, landed as composed on the author’s word; the '
      'navigator’s claim that the defects bank is root-named read as wrong, the root naming the answers and citation banks and not the '
      'defects bank (the corrigendum’s (e)). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B699_ENTRY,
         check=[('FINDINGS.md', K.B699_ENTRY, '## SIDE-substrate-cluster re-cut: 1 row outside LICENSED/CITED to 0, v0.4.1'),
                ('OPEN_TRAILS.md', K.B699_TRAIL, '### b699')], dry=dry)


# ================================================================================ COMPONENT 3: THE SLATE FOR b701, (R310)(4)
SLATE_SOURCES = (   # ### (the slate's figure, the bank, the needle on its line, the line)
    ('the bridge`s price, 1 dispatch', 'b699_bridge_plan.txt', 'PRICE: 1 dispatch', 85),
    ('the bridge`s statement S1 and its grade', 'b699_bridge_plan.txt', 'S1  theorem', 67),
    ('P3 DERIVED, not compiled', 'b687_p3_status.txt', 'P3: DERIVED', 35),
    ('the count`s steps (1)-(9)', 'b685_count_plan.txt', '== 1. THE STEPS', 15),
    ('the constants in balls', 'b685_count.txt', 'a = 0.432571915432', 21),
    ('the RE-PROVED rows by column', 'b698_regularity_uses.txt', 'W1 DISCHARGED 11, RE-PROVED 6, OBSTRUCTED 0', 85),
    ('b689`s form: one run at the branch tip', 'b689_runner_rows.json', '"label": "run1"', 5),
)


def slate(*a):
    """Component 3: the slate banked at step zero (data/b700_slate.txt) printed whole, each figure it cites re-read at its source line first;
    data/b700_slate_check.txt. Nothing compiled."""
    rows = []
    for what, bank, nd, ln in SLATE_SOURCES:
        L0 = rdn(bank).split(NL)
        rows.append((what, bank, ln, nd in (L0[ln - 1] if len(L0) >= ln else '')))
    s = rdn('%s_slate.txt' % ACT).split(NL)
    vi = next((i for i, l in enumerate(s) if l.startswith('### ### **')), None)
    v = [' '.join(x.replace('### ### **', '').replace('### ###', '').strip() for x in s[vi:] if x.startswith('### ###'))] if vi is not None else []
    L = ['%s -- COMPONENT 3, (R310)(4): THE SLATE FOR b701 PRINTED FROM ITS BANKS, EACH SOURCE RE-READ AT ITS LINE (%s)' % (ACT, utc()), '',
         '### rows are the slate`s sources: the figure | the bank :line | read there:']
    L += ['  %-44s | data/%s :%d | %s' % (w, b, ln, ok) for w, b, ln, ok in rows]
    L += ['', '### THE SLATE, AS BANKED AT STEP ZERO (relay data/%s_slate.txt), ITS ORDERS:' % ACT]
    L += [l for l in s if l.startswith('== ') or l.lstrip().startswith('PRICE')]
    L += ['', '### ### **SOURCES %d, READ AT THEIR LINES %d ; %s.**' % (
        len(rows), sum(1 for r in rows if r[3]), (v[-1] if v else '### NO VERDICT').replace('### ### **', '').rstrip('*').rstrip('.'))]
    if 'dry' not in a:
        put_txt('%s_slate_check.txt' % ACT, L)
    print(NL.join(L[3:]))


# ================================================================================ THE REPAIRS ((R310)(2) and the carry-time reading)
REPAIR_ROWS = [      # ### (text, carried tool, carried function, this act's tool, this act's function)
    ('(1) tools/b700_record.py _defect_short, carried from tools/b698_record.py _defect_short (sealed at b698, :367) -- ANSWERS b699`s defect '
     '(d) under (R310)(2): the act PASSED AT THE CALL and not bound at import (`act=ACT` bound \'b698\' when b698_record was imported, and '
     'b699`s sealed trail route, calling it with no argument, landed b698`s four defects); no default, a malformed act refused; b698`s '
     'function rebound to this one, so a carried call that omits the act refuses instead of reading another act`s bank. The row reader '
     'split out as read_defect_row, its text unchanged.', 'b698_record.py', '_defect_short', 'b700_record.py', '_defect_short'),
    ('(2) tools/b700_record.py closing_defects and defshort, new -- ANSWERS (R310)(2) on the author`s answer at b700 (Option 1): the dry run '
     'reads the defects bank by the repaired reader and then the defects a closing`s (g) line enters outside the bank, each row with its '
     'source.', None, None, 'b700_record.py', 'closing_defects'),
    ('(3) tools/b700_record.py prev_capture, carried from tools/b699_record.py prev_capture -- ANSWERS the session: b699 ran in this act`s own '
     'session (c677eaf2), so the previous act`s window is the same-session form: b699`s capture from the call that combined its post-push '
     'parts to this act`s anchor.', 'b699_record.py', 'prev_capture', 'b700_record.py', 'prev_capture'),
    ('(4) tools/b700_corrigendum.py compose, carried from tools/b699_corrigendum.py compose -- ANSWERS (R310)(2): b699`s trail Defects line, '
     'its head line`s two counts and the navigator`s root-named claim, each read from its bank.', 'b699_corrigendum.py', 'compose',
     'b700_corrigendum.py', 'compose'),
    ('(5) tools/b700_record.py capture, carried from tools/b698_record.py capture -- ANSWERS the session change after the host reboot, on the '
     'author`s word (b671`s form): the continuation b858e03f named in the worklist`s SESSIONS_AFTER with its anchor "RESUME b700 after a host '
     'reboot", its commands read from that anchor and labelled by the session, a continuation reading no command refused.', 'b698_record.py',
     'capture', 'b700_record.py', 'capture'),
    ('(6) tools/b700_record.py reads, carried from tools/b698_record.py reads -- ANSWERS the same: the Read calls of both sessions (b698`s '
     '_session_rows already walks SESSIONS_AFTER at b698_record.py :275), a continuation`s transcript line labelled by its session. The '
     'answers route needs no diff: it reads through the same _session_rows.', 'b698_record.py', 'reads', 'b700_record.py', 'reads'),
    ('(7) tools/b700_citation.py continuation_sessions, new -- ANSWERS the same for the (R278)(4) check: b677`s helpers read C.SESSIONS_AFTER '
     'after the seat`s session, so the answers given after the reboot are read in the session that received them; made before the check on the '
     'author`s word that ordered the repair, which could not otherwise read it.', None, None, 'b700_citation.py', 'continuation_sessions'),
    ('(8) tools/b700_checks.py ra_sources, new -- ANSWERS the session change for the rule arms: tools/rule_arms.py`s sources read one session`s '
     'transcript; the suite extends their call trace by the continuation`s through rule_arms.transcript, from its own anchor, so the rule arms '
     'read the calls made after the reboot; tools/rule_arms.py unedited.', None, None, 'b700_checks.py', 'ra_sources'),
    ('(9) tools/b700_closing.py head_line, carried from tools/b699_closing.py head_line -- ANSWERS (R310)(2), b699`s head line undercounting on '
     'both counts: the prompts the answers bank`s rows plus one for the root`s prompt, its answer in the closing line (N4); the defects the defects '
     'bank`s lettered rows read now, not a stored count.', 'b699_closing.py', 'head_line', 'b700_closing.py', 'head_line'),
]


def repairs(*a):
    """data/b700_tool_repairs.txt: the repairs, each with the defect or order it answers, its diff written by this route (difflib over the
    carried function's source at relay HEAD against this act's), and the (R310)(2) repair's dry run on b699's bank beneath its row."""
    import difflib
    import io
    import contextlib
    L = ['%s -- THE REPAIRS: (R310)(2) AND THE CARRY-TIME READING (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect or order they answer: the tool and its part ; what it answers ; the form. Each diff beneath its',
         '### row, written by this route (difflib over the function`s source, relay HEAD`s carried tool against this act`s).', '']
    n = 0
    for text, src_tool, fn, new_tool, new_fn in REPAIR_ROWS:
        old = R._fn_src(_show(ROOT, 'HEAD', 'tools/' + src_tool) or '', fn).split(NL) if src_tool else []
        new = R._fn_src(rd(os.path.join(T, new_tool)), new_fn).split(NL)
        if new_fn == 'closing_defects':
            new += [''] + R._fn_src(rd(os.path.join(T, new_tool)), 'defshort').split(NL)
        d = list(difflib.unified_diff(old, new, ('tools/%s %s (sealed)' % (src_tool, fn)) if src_tool else '(none)',
                                      'tools/%s %s (this act)' % (new_tool, new_fn), lineterm=''))
        n += len(d)
        L += ['  ' + text, ''] + ['      ' + x for x in d] + ['']
        if new_fn == '_defect_short':
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                defshort('b699')
            L += ['  ### ITS DRY RUN ON b699`S BANK, `python -X utf8 tools/b700_record.py defshort b699` (the author`s answer at b700, Option 1: '
                  'the bank by the repaired reader, then the closing`s (g) line as a second, named source):'] + [
                      '      ' + x for x in buf.getvalue().rstrip(NL).split(NL)] + ['']
    L += ['### ### **REPAIRS %d ; THE ONE EDIT TO A SHARED ROUTE (R310)(2)`S, IN THIS ACT`S TOOL, b698`S SEALED TOOL UNEDITED ; DIFF LINES %d ; THE DRY '
          'RUN ON b699`S BANK PRINTING FOUR (3 FROM THE BANK, 1 FROM THE CLOSING LINE) ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(L[-1])


# ================================================================================ THE LATE ROUTES (b699's, carried with b700's names)
_KERNS_698 = R._kerns


def _kerns():
    return _KERNS_698() + ['SIDE-substrate-cluster']     # ### b699's list, carried: b698's and SIDE-substrate-cluster


R._kerns = _kerns


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    import b633_record as R3
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (no kernel written this act; no kernel written after this read)' % len(ks))


def _standing():
    return sorted(set(R._g2_of(os.path.join(ROOT, *K.B699_FACE.split('/')))) - set(K699.ACT_ARMS))


R._standing = _standing


def standing(*a):
    """the standing arms b700 carries: b699's face's (G2) arms less b699's act arms (R264)(2); printed only."""
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


def armsecs(*a):
    st = _standing()
    rows, phases, runs = [], {}, {}
    for p in K.PARTS:
        j = jl('%s_arm_seconds_%s.json' % (ACT, p))
        phases[p] = j.get('phases') or {}
        runs[p] = j.get('run_secs')
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['%s -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): the per-part seconds of the six parts' % (ACT, utc()), '',
         '### the source: data/%s_arm_seconds_<part>.json, written by tools/%s_checks.py at its pre-run, each arm`s seconds the sum of its' % (ACT, ACT),
         '### three readings (LIVE on the sources, NEG on a copy, POS on a mutated copy); each part`s run seconds and its phases -- the sources',
         '### built once for all its arms -- printed beside, not divided among them. standing-b2 carries no arm and is clocked by its run alone.',
         '### Rows are standing arms, slowest first:']
    L += ['  %-46s %-11s %8.3f s' % (r['arm'], r['part'], r['secs']) for r in srows]
    L += ['', '### THE PARTS` SECONDS: ' + ' | '.join('%s %s s' % (p, runs[p]) for p in K.PARTS),
          '### THE PARTS` PHASES (seconds): ' + ' | '.join('%s: %s' % (p, '; '.join('%s %.0f' % kv for kv in ph.items())) for p, ph in phases.items()),
          '### the standing arms not clocked: %s' % (miss or 'NONE'),
          '', '### ### **STANDING ARMS CLOCKED %d OF %d ; THE THREE SLOWEST %s ; THEIR SECONDS SUMMED %.1f.**' % (
              len(srows), len(st), ', '.join('%s (%s, %.2f s)' % (r['arm'], r['part'], r['secs']) for r in srows[:3]) or 'NONE',
              sum(r['secs'] for r in srows))]
    put_txt('%s_arm_seconds.txt' % ACT, L)
    put_json('%s_arm_seconds.json' % ACT, dict(at=utc(), rows=srows, phases=phases, run_secs=runs, standing=len(st), clocked=len(srows), missing=miss,
                                              slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R310)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b700_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK, SK, SCORE_KEYS = R.NK, R.SK, R.SCORE_KEYS
N5_RELAY_DATA = ('act_roots.txt', 'b699_closing_push_out.txt', 'b675_corrigenda.txt')
N5_RELAY_TOOLS = ()
FACE = os.path.join(D, 'b700_registration_2026-10-21.txt')
FACE_REL = 'data/b700_registration_2026-10-21.txt'
R.FACE, R.FACE_REL = FACE, FACE_REL
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after, _one_git_write = (
    R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after, R._one_git_write)
R4_ROUTES = ('licensed', 'corr', 'ceiling', 'orders', 'methods', 'lag', 'residues', 'rules', 'arms', 'p3', 'faces', 'onecopy', 'pair', 'defects',
             'roster', 'tagsread', 'circuit', 'regularity')


def _s_scores():
    """the seat's (S1)-(S3), b699's readings with b700's bank names."""
    import collections
    TF, RA_ = jl('%s_table_final.json' % ACT), jl('%s_root_arm.json' % ACT)
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b700_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b700_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def _n1():
    """N1: no lean process on this host; no runner dispatched."""
    cm = jl('%s_commands.json' % ACT)
    ok = bool(cm) and not cm.get('local_lean') and not cm.get('dispatches') and not os.path.exists(os.path.join(D, '%s_dispatches.json' % ACT))
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches: %s; no dispatches bank written (relay data/b700_commands.txt, '
        '%d commands read)' % (cm.get('local_lean') if cm else 'unread', cm.get('dispatches') if cm else 'unread', len(cm.get('rows') or [])))


def _n2():
    """N2: every reading a tool reads printed by that tool before any hand count beside it is written -- each route's bank timed before the
    gathered bank's first commit; every tag read from ls-remote, one call per repository."""
    first = g(ROOT, 'log', '--diff-filter=A', '--format=%ct', '--', 'data/%s_reading4.txt' % ACT).split()
    t4 = int(first[-1]) if first and first[-1].isdigit() else None
    ats = dict((r, _iso_epoch(jl('%s_r4_%s.json' % (ACT, r)).get('at'))) for r in R4_ROUTES)
    before = all(v and t4 and v < t4 for v in ats.values())
    tj = jl('%s_r4_tags.json' % ACT).get('kernels') or {}
    import b700_readings as RD
    tags_ok = sorted(tj) == sorted(k for k, _n in RD.TAGS_NAMED) and all(v.get('highest') and v.get('commit') and not v.get('empty') for v in tj.values())
    cm = jl('%s_commands.json' % ACT).get('rows') or []
    calls = [r for r in cm if re.search(r'b700_readings\.py tags SIDE-[\w-]+\s*$', r['cmd'].strip())]
    per = sorted(r['cmd'].strip().split()[-1] for r in calls)
    one = len(calls) == len(set(per)) == len(RD.TAGS_NAMED) and all(r['cmd'].count('ls-remote') == 0 and r['cmd'].count(' tags ') == 1 for r in calls)
    ok = t4 is not None and before and tags_ok and one
    return ('HELD' if ok else 'REFUTED'), (
        'the %d route banks (relay data/b700_r4_<route>.json) each timed before the gathered bank`s first commit (%s): %s; the tags of %d kernels '
        'read by ls-remote (relay data/b700_r4_tags.json), every one with its peeled commit and none empty: %s; the tag calls, one repository per '
        'call, %d calls for %d kernels: %s' % (len(ats), R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(t4)) if t4 else '-', before, len(tj), tags_ok,
                                               len(calls), len(set(per)), one))


def _n3():
    """N3: every defect of b673-b699 by letter under one class, the classes' counts summing to the banks' totals, each standing source naming
    the rule or tool that answered it."""
    j = jl('%s_r4_defects.json' % ACT)
    rows, cls, series = j.get('rows') or [], j.get('classes') or [], j.get('series') or []
    one = bool(rows) and all(r.get('class') for r in rows) and len(set((r['act'], r['letter']) for r in rows)) == len(rows)
    sums = sum(c['n'] for c in cls) == len(rows) == sum(v for _a, v in series)
    banks = sum(len(re.findall(r"^    \([a-z]'?\) ", rdn('b%d_defects.txt' % n), re.M)) for n in range(673, 700)) + 1   # ### b699's (d), its closing line
    named = all(c['answer'] and not c['answer'].startswith('NONE') for c in cls if c['standing'])
    ok = one and sums and len(rows) == banks and named
    return ('HELD' if ok else 'REFUTED'), (
        'relay data/b700_r4_defects.json: %d defects, each under one class: %s; the classes` counts %d, the series` %d, the banks` lettered rows read '
        'now %d (b699`s (d) from its closing line among them): %s; standing sources %d, each naming its answer: %s' % (
            len(rows), one, sum(c['n'] for c in cls), sum(v for _a, v in series), banks, sums and len(rows) == banks,
            sum(1 for c in cls if c['standing']), named))


def _trail_defects(text):
    m = re.search(r'^\*\*Defects\*\* \(relay data/%s_defects\.txt\): (.*)\.$' % ACT, text, re.M)
    return m.group(1) if m else None


def _n4():
    """N4: the trail's Defects line in the dry run equal to the defects bank before the seal (the gate's record, its commit before the lock);
    the head line's prompt count equal to the answers bank's rows plus one for the root's answer (read at the close, from the closing tool)."""
    gate = rdn('%s_reg_gate.txt' % ACT)
    eq = 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in gate
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    gc = g(ROOT, 'log', '--diff-filter=A', '--format=%ct', '--', 'data/%s_reg_gate.txt' % ACT).split()
    gate_before = bool(gc) and gc[-1].isdigit() and bool(lock) and int(gc[-1]) <= lock
    rows = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cl = rdn('%s_closing.txt' % ACT)
    hm = re.search(r'; (\d+) prompts? answered;', cl.split(NL)[0]) if cl else None
    if not hm:
        return ('PENDING' if eq and gate_before else 'REFUTED'), (
            'the dry run`s trail Defects line against the defects bank (relay data/b700_reg_gate.txt, committed before the lock %s): %s; the head '
            'line`s prompt count waits on the closing (relay data/b700_closing.txt), the answers bank`s rows now %d' % (gate_before, eq, rows))
    ok = eq and gate_before and int(hm.group(1)) == rows + 1
    return ('HELD' if ok else 'REFUTED'), (
        'the dry run`s trail Defects line equal to the defects bank, committed before the lock: %s, %s; the head line (relay data/b700_closing.txt :1) '
        'prints %s prompts against the answers bank`s %d rows plus one for the root`s answer: %s' % (eq, gate_before, hm.group(1), rows,
                                                                                                     int(hm.group(1)) == rows + 1))


def _n5():
    import rule_arms as RA
    import b633_record as R3
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = R._kernels_moved()
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b700_', x) and x not in N5_RELAY_TOOLS]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b700_|audit_b700_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in N5_RELAY_TOOLS)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    arms_added = sorted(set(RA.NAMES) - set(K.STANDING_ADDED) - set(R._g2_of(os.path.join(ROOT, *K.B699_FACE.split('/')))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    rep = rdn('%s_tool_repairs.txt' % ACT)
    one_edit = '(1) tools/b700_record.py _defect_short' in rep and 'b698`S SEALED TOOL UNEDITED' in rep
    ok = k_ok and not moved and not tags and not pp_beyond and not kinds_beyond and not shared_tools and not differ and not arms_added \
        and not amended and not ident and not pat and not chained and gw_ok and one_edit
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began: %s; tags made: %s; no standing arm added (tools/rule_arms.py`s names beyond b699`s face): %s; the (R310)(2) repair '
            'the one edit to a shared route, in this act`s record tool, b698`s sealed tool unedited (relay data/b700_tool_repairs.txt): %s; shared '
            'tools edited: %s; sealed tools not agreeing: %s; commits amended after the seal: %s; deletes with anything chained after: %s; one git '
            'write per message (G-RULE-ONE-GIT-WRITE`s reading: %s): %s; PLACE-papers beyond the two ledgers: %s; relay files of a kind beyond the '
            'act`s banks and tools, the table, the root list, b699`s push-out bank and the corrigenda bank`s rows: %s; "patent" in the lines written: '
            '%s; outbound requests other than git and gh %d, an identifier of the author in %s' % (
                K.DRAFT, k_ok, moved or 'NONE', tags or 'NONE', arms_added or 'NONE', one_edit, shared_tools or 'NONE', differ or 'NONE',
                amended or 'NONE', chained or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE', len(ob),
                [r['line'] for r in ident] or 'NONE'))


def scores(*a):
    """`scores [dry]` writes data/b700_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b700_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


_sv, scores_line = R._sv, R.scores_line


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b700 — lane two, act one hundred and twenty-seven, the reading act under (R310): b699 at its weight; the trail`s Defects line, the '
            'head line`s counts and the root-named claim by corrigendum; reading 4 with five readings added; the slate for b701 priced')


R.TRAIL_HEAD = TRAIL_HEAD
_calls, _rl_lines = R._calls, R._rl_lines


def _v(route):
    return ([x for x in rdn('%s_r4_%s.txt' % (ACT, route)).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


def _figs():
    """the figures the title and the entry carry, each read from its bank."""
    lic, cor, res, rul, lag = (jl('%s_r4_%s.json' % (ACT, r)) for r in ('licensed', 'corr', 'residues', 'rules', 'lag'))
    dfc, oc, ros, cir, tg = (jl('%s_r4_%s.json' % (ACT, r)) for r in ('defects', 'onecopy', 'roster', 'circuit', 'tagsread'))
    cr = dict((r['reading'], r['value']) for r in cir.get('rows') or [])
    co = jl('%s_corrigendum.json' % ACT)
    sl = rdn('%s_slate_check.txt' % ACT)
    return dict(outside=lic.get('total', '-'), outside90=lic.get('b690', '-'), residues=len(res.get('rows') or []), carried=len(res.get('carried') or []),
                rules=len(rul.get('rows') or []), armed=rul.get('armed', '-'), arms=len(rul.get('arms') or []), median=lag.get('median', '-'),
                behind=cor.get('behind', '-'), gen=cor.get('generator', '-'), defects=len(dfc.get('rows') or []), classes=len(dfc.get('classes') or []),
                standing=sum(1 for c in dfc.get('classes') or [] if c.get('standing')), onecopy=oc.get('total', '-'),
                causes=', '.join('%s %d' % kv for kv in sorted((oc.get('causes') or {}).items())), papers=len(ros.get('rows') or []),
                closure=cr.get('CLAUSE-DOMINANCE by closure', '-'), corrd=cr.get('CLAUSE-DOMINANCE by correspondence', '-'),
                tags_behind=tg.get('behind_outside', '-'), tags_current=tg.get('current', '-'), corr_line=co.get('entry_line') or '-',
                slate='SOURCES 7, READ AT THEIR LINES 7' in sl)


def _title():
    f = _figs()
    return ('## Reading 4: %s rows outside license, %s residues, %s rules with %s arms, keystone lag median %s, Correspondence behind %s by b670’s method '
            'and %s by the generator’s count; defects by class, %s standing sources named; ONE-COPY %s lines by cause; %s papers outside the roster; '
            'CLAUSE-DOMINANCE %s by closure, %s by correspondence; b699’s trail line and head counts by corrigendum' % (
                f['outside'], f['residues'], f['rules'], f['arms'], f['median'], f['behind'], f['gen'], f['standing'], f['onecopy'], f['papers'],
                f['closure'], f['corrd']))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The census of b680 and b690 re-taken by their own code, with five readings added. The rows outside LICENSED/CITED fall from %s to %s by the '
         'five re-cuts since b690. The Correspondence is %s rows behind by b670’s method and %s by the generator’s own count; the difference is '
         'scope -- b670’s method reads every commit in a row, the generator the kernel cell’s leading clause, and no row is behind at the clause '
         'the generator reads. The defects of b673 through b699, %s of them, fall into %s classes, %s of them standing sources that recurred after '
         'the rule or tool that answered them, all but one. The one-copy partner tables differ in %s lines, nearly all from the generator writing a '
         'roster copy and leaving its partner.' % (f['outside90'], f['outside'], f['behind'], f['gen'], f['defects'], f['classes'], f['standing'],
                                                   f['onecopy']), '',
         '*Filed at b700 on the author’s ruling `(R310)` and the author’s words at its prompts; %d question%s put. Banks: relay `data/b700_reading4.txt` '
         'and its route banks `data/b700_r4_*`, `data/b700_corrigendum.txt`, `data/b700_tool_repairs.txt`, `data/b700_slate.txt`, '
         '`data/b700_slate_check.txt`; the readings tool `tools/b700_readings.py`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**Reading 4** (`(R310)`(3), each reading by code where a tool reads it, the hand beside): %s rows outside LICENSED/CITED, %s documents of 33 '
         'at zero; the Correspondence %s behind by b670’s method, %s by the generator’s count; the orders at OPEN_TRAILS read by b670’s queue reader; '
         'the keystone lag median %s; %s residues, %s of them carried with their triggers; %s rules over the rules banks b674-b699, %s of them with an '
         'arm among %s arms, the rest sorted in the sort rule’s own words; the arms census by act, the standing arms’ seconds and the chain halves; '
         'P3 read DERIVED at every line outside the ledgers by hand; the faces page’s header tag v0.26 against the kernel’s v0.34.1, not carried; '
         'the pair rule 1 of 4.' % (f['outside'], jl('%s_r4_licensed.json' % ACT).get('zero', '-'), f['behind'], f['gen'], f['median'], f['residues'],
                                     f['carried'], f['rules'], f['armed'], f['arms']), '',
         '**The five readings added**: (a) the defects by class -- %s defects in %s classes, every one under one class, %s standing sources each named '
         'with its answer; (b) %s papers in the mirror roster carry kernel citations outside b672’s generator roster, THE_TWO_THREE_SUBSTRATE among '
         'them; (c) eight kernel tags read by ls-remote, one call each, against the papers -- %s lines naming an older tag outside the ledgers, %s '
         'of them in current files; (d) the circuit readings as census rows, CLAUSE-DOMINANCE %s by closure and %s by correspondence; (e) the '
         'regularity bank’s counts beside the bridge plan’s price. ONE-COPY by line: %s lines over the partner pairs, by cause %s.' % (
             f['defects'], f['classes'], f['standing'], f['papers'], f['tags_behind'], f['tags_current'], f['closure'], f['corrd'], f['onecopy'],
             f['causes']), '',
         '**The corrigendum** (`(R310)`(2)): b699’s trail Defects line, listing b698’s four, entered with b699’s four as the defects bank and the '
         'closing line give them; its head line’s counts, 4 prompts as printed and 5 as put, 3 defects as printed and 4 as entered; the navigator’s '
         'root-named claim corrected to the root’s named banks, lettered (e) (FINDINGS :%s). b699 at its weight (FINDINGS :%s).' % (f['corr_line'], c1_[0]), '',
         '**The repair** (`(R310)`(2)): the record tool’s `_defect_short` carried into b700’s record tool with its act passed at the call and no '
         'default, b698’s sealed tool unedited; its dry run on b699’s bank printing four, three from the bank and one from the closing line, on the '
         'author’s answer.', '',
         '**The slate for b701** (`(R310)`(4)), priced from its banks: W-ORD-H2-BRIDGE-THEOREM one dispatch; W-ORD-EPSTEIN-COUNT-LEAN six dispatches '
         'at the least, Z_Q not yet in Lean; the classK widening to W1 ∪ W3 one dispatch in b689’s form, ten uses and four path leaves re-proved. '
         'Nothing compiled.', '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answer check%s, each before its answer '
         'was acted on.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b680’s and b690’s readings by their own code, b691’s scope finding '
         'against the generator’s count, b683’s sort against the rules banked since, b692’s and b698’s circuit readings and b698’s regularity '
         'bank against b699’s bridge price. It is re-read by b701’s research act, which takes the slate on the author’s word, and by b702’s re-cut. '
         'It strengthens the programme’s offering of a located clause: its record held to what its own code reads, the defects read as classes '
         'with their answers, and the next research priced.', '',
         '**Carried to:** b701 (the slate: the bridge, the Epstein count in Lean, the classK widening); W-ORD-ONE-COPY (the partner pairs by '
         'line); W-ORD-CORRESPONDENCE-BEHIND-SCOPE (the 58 by scope); the roster-currency rows; the faces page’s header tag; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the Correspondence’s hand count read as b691’s scope categories over b670’s BEHIND rows, the generator’s count its fresh dry; '
              '(2) the rules census’s rows read by a second shape joining a wrapped head, the sorts in the sort rule’s own words; (3) the one-copy '
              'causes read from each line’s two commits, the generator’s word on the whole subject and the re-cut and archive words on its head; '
              '(4) the roster-currency rows resolved to the tracked files outside outputs/, the MANIFEST naming basenames alone; (5) a line naming an '
              'older tag counted, not judged, the superseded copies set apart; (6) the defects’ classes the seat’s hand sort, each class’s answer '
              'named with the act it answered from; (7) the Epstein count priced at six dispatches at the least, Z_Q not yet in Lean; (8) the act '
              'resumed after a host reboot in a second session, named as its continuation on the author’s word')


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R310) ratified.** (1) b699 at its weight. (2) The corrigendum and the repair. (3) Reading 4, five readings added. (4) The slate for '
             'b701. (5) The branches. (6) The readfirst bank. (7) The draft held at v5. (8) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum), :%s (b699`s weight), :%s (the entry); this record.' % (f['corr_line'], c1_[0], fj.get('entry_line')), '',
             '**Act root:** b700 `%s` (previous `%s`, b699`s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b700_author_answers.txt); the root`s own prompt, '
             'the slate for b701, its answer in the closing line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**Reading 4:** %s rows outside license; Correspondence %s behind by b670`s method, %s by the generator`s count; residues %s; rules %s '
             'with %s arms; keystone lag median %s (relay data/b700_reading4.txt).' % (f['outside'], f['behind'], f['gen'], f['residues'], f['rules'],
                                                                                    f['arms'], f['median']), '',
             '**The readings added:** defects %s in %s classes, %s standing sources; %s papers outside the roster; tags by ls-remote; the circuit '
             'rows; ONE-COPY %s lines by cause (relay data/b700_r4_defects.txt, b700_r4_roster.txt, b700_r4_tagsread.txt, b700_r4_onecopy.txt).' % (
                 f['defects'], f['classes'], f['standing'], f['papers'], f['onecopy']), '',
             '**The corrigendum:** b699`s trail Defects line, its head counts and the navigator`s (e) (FINDINGS :%s; relay data/b675_corrigenda.txt '
             'rows (14)-(16)).' % f['corr_line'], '',
             '**The repair:** _defect_short with its act at the call, its dry run on b699`s bank printing four (relay data/b700_tool_repairs.txt).', '',
             '**The slate:** the bridge 1 dispatch; the Epstein count 6 dispatches at the least; the classK widening 1 dispatch in b689`s form '
             '(relay data/b700_slate.txt, data/b700_slate_check.txt).', '',
             '**The kernels:** none written; no runner dispatched; no lean or lake on this host.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b700_closing.txt).', '',
             '**The open orders:** `W-ORD-H2-BRIDGE-THEOREM`, `W-ORD-EPSTEIN-COUNT-LEAN` and the classK widening (b701, on the author`s word); '
             '`W-ORD-ONE-COPY`; `W-ORD-CORRESPONDENCE-BEHIND-SCOPE`; `W-ORD-B518-FLOAT`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b700_defects.txt): %s.' % ('; '.join(_defect_short(ACT)) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


desk = R.desk


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R310).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b700_citation_check.txt), step zero (data/b700_ferry.txt, data/b700_readfirst.txt, '
         'data/b700_stepzero.txt, data/b700_tests_stepzero.txt, data/b700_rowgen_stepzero.txt, data/b700_branches.txt, data/b700_slate.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b699`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s (data/b700_corrigendum.txt) ; the corrigenda bank`s rows ; the '
         'repair (data/b700_tool_repairs.txt) ; N4 %s' % (c1_[0], f['corr_line'], S['N4'][0]),
         '### COMPONENT 2 : reading 4 (data/b700_reading4.txt, data/b700_r4_*) ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the slate for b701 (data/b700_slate.txt, data/b700_slate_check.txt)',
         '### COMPONENT 4 : the carry-time reading (data/b700_tool_repairs.txt), the dry-run steps (data/b700_reg_gate.txt), the seal '
         '(data/b700_seal_hashes.json), the suite in six parts, the per-part seconds (data/b700_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def findings(*a):
    t, e = _finding_text()
    e = R.conv(e)
    dry = 'dry' in a
    cells_, fired = R.screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = R.conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = R.screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; DRY-RUN STEP : CLEAN only when both screens are quiet and
    every needle is found. And, under the ferry's Component 4: the trail's Defects line read against the defects bank in the dry run and printed
    equal. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = R.conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = R.screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = R._face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        if which == 'TRAIL':
            got = _trail_defects(text)
            want = '; '.join(_defect_short(ACT)) or 'none'
            eq = got == want
            print('  THE TRAIL`S DEFECTS LINE: %s' % got)
            print('  THE DEFECTS BANK`S ROWS (relay data/%s_defects.txt, by the repaired reader): %s' % (ACT, want))
            print('  ### THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK %s' % eq)
            clean = clean and eq
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


gatebanks = R.gatebanks
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
mbuild, mroot, mverify = R.mbuild, R.mroot, R.mverify


def mbank(*a):
    import zipfile
    import hashlib as _hl
    import b616_record as R6
    z = zipfile.ZipFile(R.ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(R.ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (R.ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b700 (the last export b699`s, D:/MY-DOwnloads/mirror-refresh-2026-10-21-b699.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=R.ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, commands=commands, reads=reads,
              rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, c1=c1, repairs=repairs, slate=slate, kernels=kernels,
              standing=standing, armsecs=armsecs, scores=scores, desk=desk, components=components, findings=findings, trail=trail,
              drycheck=drycheck, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b700_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
