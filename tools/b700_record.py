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

READERS = ['read_branch_row', 'read_defect_row']
read_branch_row = R.read_branch_row


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
capture, reads, edit_route_offences = R.capture, R.reads, R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)


def commands(*a):
    """b699's route with b700's names in its bank text: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's
    window (same session), the local lean reading (N1), the dispatches, the detached runs, sed, the redirects, the pipes, the one-line programs,
    the moves and deletes by shape, the outbound requests. data/b700_commands.txt (.json)."""
    rows = R.capture()
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
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
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


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, commands=commands, reads=reads,
              rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, c1=c1, repairs=repairs, slate=slate)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b700_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
