# -*- coding: utf-8 -*-
"""b712_record.py -- THE ACT'S RECORD TOOL, b712 under (R322).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b712 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers, b704's repaired read route and its probe, tie, quote and cut forms, b705's routes (the print-list dispatch, the artifact reader),
### b706's (the runner choosing the run's artifact by name, the prints branch, the probe-step artifact, the mentions re-read) and b711's (the
### declared untracked writes, the root route's dry run, the rowgen roster re-pointed, the previous window in b701's form) are reached through
### tools/b711_record.py (sealed at b711 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### Written by the Write tool at b712 in stages: stage one, step zero's routes (the tie among them); Components 1-6 by the Edit tool.
### Routes: `python tools/b712_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import hashlib
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

import b712_worklist as K          # noqa: E402
import b711_worklist as K707       # noqa: E402  ### b711's data, for the controls on b711's banks
import b711_record as P7           # noqa: E402  ### b711's tool, imported unedited (its import binds b698's R, b703's P3, b704's P4, b705's P5 and b706's P6 to b711: rebound below)
R, P3, P4, P5, P6 = P7.R, P7.P3, P7.P4, P7.P5, P7.P6   # ### b698's routes, b703's to b706's repaired readers, through b711's module

ACT, PREV = 'b712', 'b711'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b711 ran and closed in ANOTHER session (0be08567; this act opens c9e4ce2d after the author's /clear) -- b701's
# ### form: from b711's post-push combine in that session to that session's end (prev_capture below; a carry-time repair of b711's same-session bound)
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = PREV_SUBAGENTS
FACE = os.path.join(D, 'b712_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b712_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b711_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('mirror_prevbuild.json',)   # ### (R322)(2): the mirror builder's own state file, written at every build

# ### THE ROOT ROUTE'S EXCLUSION LIST (data/b706_rules.txt row (1)): the kinds b698's route excludes, carried; and every untracked write a
# ### b712_*.py tool declares in its own head, read at import. A tool declares one by a line `### UNTRACKED WRITE: data/b712_<name>`.
# ### (R322)(2): the events bank (row (52): a finding after the seal, written after the seal and after the root) and the step bank (G-SEALED-AFTER-
# ### COMPONENTS, a row per commit written after the commit, the record's and the closing's among them) are the defects bank's kind: not root items
EXCLUDE_KINDS = P7.EXCLUDE_KINDS + r'|events|steps'
# ### b711's declaration line read to its first space (b711: `\s*$`, which refused a declaration followed by prose and so read the grid's and the
# ### pairs' declarations as none -- the root's first dry run named 32 untracked units files); a name ending in `*` declares every file with that
# ### prefix (the grid's segment files, the pairs' band files). A carry-time repair, banked by diff (data/b712_tool_repairs.txt).
UNTRACKED_DECL = re.compile(r'^### UNTRACKED WRITE: data/b712_(\S+)', re.M)


def declared_untracked():
    """every b712_*.py tool's declaration of an untracked write (its units file, its download), read from the tools' own heads: [(tool, name)]."""
    out = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b712_') and f.endswith('.py'):
            for m in UNTRACKED_DECL.finditer(rd(os.path.join(T, f)) or ''):
                out.append((f, m.group(1)))
    return out


def _root_exclude():
    names = [(re.escape(n[:-1]) + r'\S*') if n.endswith('*') else re.escape(n) for _f, n in declared_untracked()]
    return re.compile(r'^b712_(' + EXCLUDE_KINDS + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


R.ROOT_EXCLUDE = _root_exclude()

# ### (R322)(2)(ii), standing clauses v2 row (53): THE MEMBRANE in the shared writers -- b698's put_json and put_txt (which every route of this
# ### tool and of b698's to b711's modules writes through) wrapped by tools/act_membrane.py's guard, which refuses a bank the root names once
# ### this act's root is appended to data/act_roots.txt; the mirror builder's banks and the root's exclusions pass (a repair at b712, banked by diff).
import act_membrane as MEM          # noqa: E402
# ### a carry-time repair at b712: b711's module rebound R's writers to its own wrappers, which guard b711 (rooted), so the originals are read
# ### from b711's capture of b698's writers and not from R (a wrapper over a wrapper refuses every bank once the previous root is appended)
_put_json0, _put_txt0 = getattr(P7, '_put_json0', R.put_json), getattr(P7, '_put_txt0', R.put_txt)


def put_json(name, obj):
    MEM.guard(ACT, name, R.ROOT_EXCLUDE)
    _put_json0(name, obj)


def put_txt(name, lines):
    MEM.guard(ACT, name, R.ROOT_EXCLUDE)
    _put_txt0(name, lines)


R.put_json, R.put_txt = put_json, put_txt
for _m in (P3, P4, P5, P6, P7, getattr(P7, 'P7', None)):   # ### b703's to b711's modules bound b698's writers at their own import
    for _n, _f in (('put_json', put_json), ('put_txt', put_txt)):
        if _m is not None and hasattr(_m, _n):
            setattr(_m, _n, _f)


def rootexclude(*a):
    """prints the declared untracked writes and the exclusion pattern they extend; writes nothing."""
    decl = declared_untracked()
    for f, n in decl:
        print('  %-28s declares data/b712_%s untracked' % (f, n))
    print('  DECLARED UNTRACKED WRITES %d ; ROOT_EXCLUDE %s' % (len(decl), R.ROOT_EXCLUDE.pattern))


_R_anchor_ts = P7._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704 to b711


def _anchor_ts(anchor, session=None):
    """b698's _anchor_ts bound its session at definition (b699's trap 1): this one reads this act's session unless another is named."""
    return _R_anchor_ts(anchor, session or SESSION)


R._anchor_ts = _anchor_ts


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        '%s_scores.json' % ACT: dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        '%s_findings.json' % ACT: dict(entry_line=99999, title='stand-in'),
        '%s_trail.json' % ACT: dict(line=99999),
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='11fe3e21' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S TO b711'S REPAIRED READERS, THROUGH b711'S MODULE
_deps = P3._deps                   # ### the primed names read (b703 (f))
R._deps = _deps
DEFECT_ROW = R.DEFECT_ROW
read_defect_row = P3.read_defect_row
_defect_short = P3._defect_short   # ### the act PASSED AT THE CALL (b700's repair)
R._defect_short = _defect_short
_last_export, span_line = P3._last_export, P3.span_line
_read_verdict, CAP = P4._read_verdict, P4.CAP   # ### b704's repaired verdict (offset, limit VALUES, the cap of two hundred)
_print_modules = P5._print_modules              # ### b705's print-list reader (every name mapped to its module by git grep bounded to the tree)
_artifact_named = P6._artifact_named            # ### b706's: the run's artifact chosen by name
roster709 = P7.roster709                        # ### b707's rowgen roster re-pointed through data/b706_partners.json (the fourth path reader), through b711's module (a carry-time repair: the substitution shifted b711's own name for it)


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried; rowgen's roster b711's)
answers = R.answers


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables, each at the file of record after b706's renames (b711's roster707); each tool's verdict lines
    banked with its exit. data/b712_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
    Ro = roster709()
    paths = [os.path.join(PP, p) for _n, p, _f in Ro]
    miss = [p for p in paths if not os.path.exists(p)]
    if len(Ro) != 19 or miss:
        sys.exit('### THE ROSTER IS NOT 19 PATHS AT HEAD: %d, missing %s' % (len(Ro), miss))
    moved = [(n, f, p) for n, p, f in Ro if f]
    t0 = time.time()
    con = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'rowgen.py'), 'constellation', PP] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    dif = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'diff_rowpin.py'), os.path.join(T, 'rowgen', 'namemap.json')] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    secs = int(time.time() - t0)
    co, do = (con.stdout or '') + (con.stderr or ''), (dif.stdout or '') + (dif.stderr or '')
    tail = lambda t: [l for l in t.replace(chr(13), '').split(NL) if l.strip()][-12:]   # noqa: E731
    L = ['%s -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (ACT, stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s, each at its file of record after b706`s renames '
         '((R316)(3): %d of the bank`s paths re-pointed from the retired versioned name, data/b706_partners.json, b711`s reader) ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), len(moved), secs), '']
    L += ['### re-pointed: %s -> %s' % (f, p) for _n, f, p in moved]
    L += ['', '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19 ; RE-POINTED %d.**' % (con.returncode, dif.returncode, len(moved))]
    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)
    print(NL.join(L[-14:]))


# ================================================================================ (R322)(2)(i), STANDING CLAUSES v2 ROW (52): THE LETTERS AT THE SEAL
def letters_of(text):
    """the lettered rows of a defects bank's text, each '(x) HEAD' by b703's row reader (pure in its argument)."""
    L = (text or '').replace(chr(13), '').split(NL)
    return [s for s in (read_defect_row(L, i) for i, l in enumerate(L) if DEFECT_ROW.match(l)) if s]


def _letter(s):
    m = re.match(r"^\(([a-z]'?)\)", s or '')
    return m.group(1) if m else None


def letters_at_seal(act):
    """the letters entered before the seal: the list the suite's seal records with the hashes (data/<act>_seal_hashes.json `letters`, from b712);
    for an act sealed before the repair, its defects bank as committed at the seal's relay head (`relay_head`, read by b698's _show). None where
    the act is not sealed or the bank is not read."""
    sj = jl('%s_seal_hashes.json' % act)
    if not sj:
        return None
    if isinstance(sj.get('letters'), list):
        return list(sj['letters'])
    t = _show(ROOT, sj['relay_head'], 'data/%s_defects.txt' % act) if sj.get('relay_head') else None
    return letters_of(t) if t is not None else None


def defects(*a):
    """data/b712_defects.json from the bank; after the seal (row (52)) it refuses a letter the seal did not record: a finding after the seal is
    entered in data/b712_events.txt for the closing's events section, and the next act's corrigendum letters it."""
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    seal = letters_at_seal(ACT)
    if seal is not None:
        late = [s for s in letters_of(t) if _letter(s) not in set(_letter(x) for x in seal)]
        if late:
            sys.exit('### (R322)(2)(i): %d LETTER(S) ENTERED AFTER THE SEAL (%s) -- A FINDING AFTER THE SEAL IS AN EVENT, ENTERED IN data/%s_events.txt, '
                     'NOT A LETTER -- NOTHING WRITTEN' % (len(late), ', '.join(s[:3] for s in late), ACT))
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ (R322)(2): THE ACT'S STEP BANK (G-SEALED-AFTER-COMPONENTS reads it)
# ### (R322)(3)(ii): 'gate' -- the commit of the gate before the lock, the one commit the face cannot carry (it stamps the face); the suite's
# ### G-NOTHING-RAN-AHEAD reads it from this bank and asks every other commit before the lock to be declared on the face by its hash
PRE_SEAL_PHASES = ('step zero', 'component 1', 'component 2', 'component 3', 'component 4', 'component 5', 'gate')
POST_SEAL_PHASES = ('seal', 'pre-root', 'root', 'record', 'closing')
STEP_PHASES = PRE_SEAL_PHASES + POST_SEAL_PHASES
STEP_REPOS = dict(relay=ROOT, pp=PP)


def step(*a):
    """`step <relay|pp> <phase words> [commit]`: one row appended to data/b712_steps.json after a commit -- the repository, the commit (HEAD where
    none is named), its committer time and subject as read, and the phase the seat names from STEP_PHASES; G-SEALED-AFTER-COMPONENTS reads the
    phase and not the subject. A commit already in the bank is not entered twice."""
    if len(a) < 2 or a[0] not in STEP_REPOS:
        sys.exit('### step <relay|pp> <phase> [commit] -- the phases: %s' % ' | '.join(STEP_PHASES))
    rest = list(a[1:])
    commit = rest.pop() if rest and re.match(r'^[0-9a-f]{7,40}$', rest[-1]) else 'HEAD'
    phase = ' '.join(rest)
    if phase not in STEP_PHASES:
        sys.exit('### THE PHASE %r IS NOT ONE OF %s -- NOTHING WRITTEN' % (phase, ' | '.join(STEP_PHASES)))
    full = g(STEP_REPOS[a[0]], 'rev-parse', '--verify', '--quiet', commit + '^{commit}').strip()
    if not full:
        sys.exit('### %s IS NOT A COMMIT OF %s -- NOTHING WRITTEN' % (commit, a[0]))
    ct, subj = g(STEP_REPOS[a[0]], 'log', '-1', '--format=%ct%x09%s', full).strip().split('\t', 1)
    j = jl('%s_steps.json' % ACT)
    rows = j.get('rows') or []
    if any(r.get('repo') == a[0] and r.get('commit') == full for r in rows):
        sys.exit('### %s %s IS IN THE STEP BANK ALREADY -- NOTHING WRITTEN' % (a[0], full[:8]))
    rows.append(dict(repo=a[0], commit=full, ct=int(ct), at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(ct))), phase=phase, subject=subj[:120]))
    put_json('%s_steps.json' % ACT, dict(at=utc(), rows=rows))
    print('  step %d: %s %s %s -- %s' % (len(rows), a[0], full[:8], rows[-1]['at'], phase))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R322)(8); b711's form)
def branches(*a):
    """`branches before`: data/b712_branches_before.json -- b698's route, carried (every branch (R322)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b712_branches.txt (.json) --
    each branch's fate read now against the tips banked before; the kept branch port-b707 read beside them."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b712_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    krepo, kb = K.KEPT_BRANCH
    kept_local = g(krepo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + kb).strip()
    kept_remote = R._remote_heads(krepo).get(kb, '')
    L = ['%s -- STEP ZERO, (R322)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b712_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. (R322)(7) names relay`s four and PLACE-papers` two; port-b707 of',
         '### SIDE-lv-conservation is NOT deleted, local or remote, read beside them.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['  %-22s | %-28s | kept   | local %s ; remote %s ; %s' % (os.path.basename(krepo), kb, kept_local[:12] or 'absent', kept_remote[:12] or 'absent',
                                                                'STANDS' if kept_local == kept_remote == K.PORT_TIP else '### NOT AS KEPT')]   # ### a carry-time repair: b711's tip, K.PORT_TIP
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s ; port-b707 STANDS %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows),
        kept_local == kept_remote == K.PORT_TIP)]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[], kept=dict(repo=krepo, branch=kb, local=kept_local, remote=kept_remote)))
    print(NL.join(L[7:]))


# ================================================================================ THE READ BANK (b704's repaired route; the word's time the anchor's, from b705)
def reads(*a):
    """b704's repaired route (tools/b704_record.py :392) with the author's word at b704's arm-baseline prompt applied: from b705 the word's time
    is the act's anchor and every call counts -- every Read call of the seat since the anchor with its offset and limit VALUES, the file's line
    count read now beside it; a call of a file of two hundred lines or more with no offset, or no limit, or a limit above two hundred is an
    offence. data/b712_read_calls.txt."""
    word = _anchor_ts(K.ANCHOR)
    rows = []
    for i, o, _st, _sid in R._session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                p = inp.get('file_path') or ''
                rows.append(dict(line=i, ts=o.get('timestamp'), path=p, offset=inp.get('offset'), limit=inp.get('limit'), lines=R._lines_now(p)))
    for r in rows:
        r['verdict'] = _read_verdict(r, word)
    bad = [r for r in rows if r['verdict'] == '### AN OFFENCE']
    pre = [r for r in rows if r['verdict'].startswith('BEFORE THE WORD')]
    L = ['%s -- THE READ CALLS SINCE THE ANCHOR, BY data/b698_rules.txt ROW (2) AND THE AUTHOR`S WORD AT b704`S SORT (%s)' % (ACT, utc()), '',
         '### the rule: whole where the file is under two hundred lines; otherwise an offset and a limit, the limit no greater than two hundred (the',
         '### cap, the author`s word at %s). Rows are Read calls: transcript line | time | the file`s lines read now | offset | limit | the verdict |' % (word or '### NOT READ'),
         '### path. From b705 the word`s time is the act`s anchor and every call counts (the author`s word at b704`s arm-baseline prompt).']
    L += ['  %s | %s | %s | offset %s | limit %s | %s | %s' % (r['line'], r['ts'], r['lines'], r['offset'], r['limit'], r['verdict'], r['path']) for r in rows] or ['  NONE']
    L += ['', '### ### **READ CALLS %d ; ON FILES OF 200 LINES OR MORE %d ; OFFENCES %d ; THE CAP`S PRECURSORS %d ; THE WORD AT %s.**' % (
        len(rows), sum(1 for r in rows if r['lines'] is None or r['lines'] >= CAP), len(bad), len(pre), word or '### NOT READ')]
    if 'dry' not in a:
        put_txt('%s_read_calls.txt' % ACT, L)
        put_json('%s_read_calls.json' % ACT, dict(at=utc(), word=word, cap=CAP, rows=rows))
    print(NL.join([l for l in L if '### AN OFFENCE' in l or 'PRECURSOR' in l][:40] + L[-1:]))


def names(*a):
    """the functions of an imported record module (b698's by default) with the line each opens at -- names and numbers, no source printed."""
    import importlib
    import inspect
    mod = {'b698': R, 'b703': P3, 'b704': P4, 'b705': P5, 'b706': P6, 'b711': P7}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
    for n, f in sorted(vars(mod).items(), key=lambda kv: inspect.getsourcelines(kv[1])[1] if inspect.isfunction(kv[1]) and kv[1].__module__ == mod.__name__ else 0):
        if inspect.isfunction(f) and f.__module__ == mod.__name__:
            print('  %-28s :%d' % (n, inspect.getsourcelines(f)[1]))


def verdicts(*a):
    """prints each named bank's verdict line (its last `### ### **...**` line), for the suite's predicates to quote; writes nothing."""
    for n_ in a:
        m = re.findall(r'(?ms)^\s*### ### \*\*(.*?)\*\*\s*$', rdn(n_))
        print('  %s | %s' % (n_, ' '.join(m[-1].split()) if m else '### NO VERDICT LINE'))


# ================================================================================ THE DISPATCH, THE RUNNER (b698's routes; b705's print-list check; b706's artifact by name)
runstatus, runner = R.runstatus, R.runner
STD3 = P3.STD3
EF = K.EF_DIR
WF = getattr(K, 'WORKFLOW', '')   # ### a carry-time repair: the worklist names no workflow constant; the dispatches name build-module.yml in the route


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: b698's dispatch (one dispatch per tree state, the run id read), with b705's check
    (data/b705_rules.txt row (1)): every name of print_targets.txt at the ref mapped to its module by git grep bounded to the kernel's tree; a
    target not covering every module is REFUSED, nothing dispatched; the row banked carries `whole` True with the modules the list needs."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    mods = _print_modules708('D:/' + kernel, ref)
    need = sorted(set(m for m in mods.values() if m))
    unmapped = [n for n, m in mods.items() if not m]
    tgt = target.split()
    whole = bool(need) and not unmapped and all(m in tgt for m in need)
    print('  the print list %d names ; their modules %d %s ; unmapped %s ; the target %d modules ; whole %s' % (len(mods), len(need), need[:6], unmapped or 'NONE', len(tgt), whole))
    if not whole:
        sys.exit('### THE TARGET DOES NOT COVER THE PRINT LIST`S MODULES (data/b705_rules.txt row (1)) -- NOT DISPATCHED')
    R.dispatch(*a)
    if 'dry' in a[4:]:
        return
    j = jl('%s_dispatches.json' % ACT)
    rows = j.get('rows') or []
    if rows:
        rows[-1].update(whole=True, print_names=len(mods), print_modules=need)
        put_json('%s_dispatches.json' % ACT, dict(rows=rows))
    print('  the row banked with whole True ; print modules %d' % len(need))


def runwait(*a):
    """`runwait <kernel> <run id> [seconds]`: the run's status read every 30 s in the FOREGROUND until it completes or the seconds pass (at most
    560, under the 590 s guard); each read printed. No wait is backgrounded."""
    end = time.time() + min(int(a[2]) if len(a) > 2 else 540, 560)
    while True:
        rc, out, err = R._gh('run', 'view', a[1], '-R', 'psinary-sketch/' + a[0], '--json', 'status,conclusion,updatedAt')
        j = json.loads(out or b'{}')
        print('  %s  status %s ; conclusion %s ; updated %s' % (utc(), j.get('status'), j.get('conclusion') or '-', j.get('updatedAt')), flush=True)
        if j.get('status') == 'completed' or time.time() + 30 > end:
            return
        time.sleep(30)


# ================================================================================ THE LATE ROUTES (b711's, carried with b712's names; the previous window in its own session)
import edit_route as ER            # noqa: E402


def capture():
    """b701's capture: the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER) from its own anchor."""
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
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after = R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act, b701's form for a previous act in ITS OWN session (b711's carry-time repair, carried): b711's
    capture AFTER ITS POST-PUSH SUITE -- every command of session 0be08567 from the call that combined b711's post-push parts into
    data/b711_checks_postpush.txt to that session's end, its closing's commands among them; this act runs in a session of its own."""
    rows = ER.capture(PREV_SESSION_PATH, K.PREV_ANCHOR, PREV_SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    anchor = '9999'   # ### b712's carry-time repair: the previous act ran in ITS OWN session (b711 bounded it at this act's anchor, b700's same-session form), so its window runs to that session's end (b701's form)
    out = [dict(r, src='%s %s' % (PREV, r['src'])) for r in rows if first[0] <= r['ts'] < anchor]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


R.prev_capture = prev_capture
edit_route_offences = R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)
local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final
# ### b711's pattern read `_record.py dispatch`; this act's one dispatch ran through the `portdispatch` route, so the pattern takes the port prefix too
# ### (a carry-time repair, banked by diff: the command bank's first write read DISPATCHES 0 against the dispatch bank's one row)
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)


def commands(*a):
    """b711's route with b712's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window (b711's
    session from its post-push combine to its end), the local lean reading (N1), the dispatches (two ordered: the probe branch and the prints
    branch), the detached runs, sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound requests.
    data/b712_commands.txt (.json)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if DISPATCH_CMD.search(QUOTED.sub('""', r['cmd']))]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if R.sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    anypipe = [r for r in sh_ if '|' in QUOTED.sub('""', r['cmd']).replace('||', '')]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if delete_shape(r['cmd'])[0] and chained_after(r['cmd'])]
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
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, its own session %s, from its post-push combine to that session`s end): '
              '%d commands from %s, its offences printed whole (%d):' % (PREV, R.PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (at most three port dispatches and the join`s, (R322)(4) and N1: port-b707 of SIDE-lv-conservation through the portdispatch route, SIDE-faces-join`s main through the dispatch route) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R322)(8) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
        for r, o in hits:
            print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
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


_kerns = R._kerns                  # ### b703's list (b698's and SIDE-substrate-cluster), rebound by b703's import


def kernels(*a):
    ks = list(dict.fromkeys(_kerns() + ['SIDE-faces-join']))
    import b633_record as R3
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-faces-join among them, its main written this act (the lakefile, %s) and tagged v0.1.0; SIDE-lv-conservation`s main '
          'untouched, port-b707 at this act`s two commits, its checkout at main for this read)' % (len(ks), K.JOIN_NEW_TIP[:8]))


def _standing():
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B711_FACE.split('/')))) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))   # ### a carry-time repair: the previous face b711's (K.B711_FACE; the substitution left b709's name, absent from this act's worklist)


R._standing = _standing


def standing(*a):
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, gatebanks, mbuild, mroot, mverify = R.desk, R.gatebanks, R.mbuild, R.mroot, R.mverify


def _one_git_write():
    return R._one_git_write()


def rootdry(*a):
    """data/b706_rules.txt row (1): the root route run DRY on the pre-root tree before the seal -- the banks the route names (ROOT_EXCLUDE
    extended), each read for CR LF, its status and its blob at HEAD; READY where every named bank is clean and equal at HEAD and none is CR LF
    (the push clause, HEAD the remote main, printed beside and not required before the record`s push). data/b712_root_banks_dry.txt (.json)."""
    banks = root_banks()
    s = root_banks_state(banks)
    crlf = [b_ for b_ in banks if os.path.exists(os.path.join(ROOT, *b_.split('/'))) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    missing = [b_ for b_ in banks if not os.path.exists(os.path.join(ROOT, *b_.split('/')))]
    ready = bool(s['rows']) and s['clean'] and not crlf and not missing
    L = ['%s -- THE ROOT ROUTE`S DRY RUN ON THE PRE-ROOT TREE BEFORE THE SEAL (data/b706_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are the banks the root route names (tools/b698_record.py root_banks with ROOT_EXCLUDE rebound at tools/b712_record.py, extended by',
         '### every declared untracked write: %s): status ; carried by HEAD ; HEAD`s blob equal to the file ; CR LF.' % (
             [n for _f, n in declared_untracked()] or 'NONE DECLARED'),
         '### HEAD %s ; the remote main %s ; equal %s (the push clause, read beside: the record`s push comes after the seal)' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %-5s crlf %s' % (r['bank'], r['status'], r['at_head'], r['equal'], r['bank'] in crlf) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; CR LF %s ; MISSING %s ; HEAD THE REMOTE MAIN %s ; THE DRY RUN READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), crlf or 'NONE', missing or 'NONE', s['pushed'], ready)]
    put_txt('%s_root_banks_dry.txt' % ACT, L)
    put_json('%s_root_banks_dry.json' % ACT, dict(at=utc(), ready=ready, crlf=crlf, missing=missing, declared=declared_untracked(), **s))
    print(L[-1])


# ================================================================================ STEP ZERO: THE LICENSED TABLE'S NEXT DOCUMENT, (R322)(6) (b704's tie form)
SUMMARY = re.compile(r'### ### \*\*(\w+): CLAIMS (\d+) ; SKIPPED LINES (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)')


def tie(*a):
    """data/b712_tie.txt: (R322)(6), the licensed table's next document -- b652's order, b674's tie-break rule and data/b705_rules.txt row (2)
    printed verbatim before the document is named; the agenda's rows as b704's tie bank read them (data/b704_tie.txt, b702's cut entered there),
    b704's cut entered from its own bank (data/b704_cut.json); the documents at the top count, each table's summary line verbatim, each
    document's sha256 at PLACE-papers HEAD against its table's read; b674's rule step by step in its written order, b705's row (2) where its
    condition is not met."""
    f52 = rdn('b652_ferry.txt').split(NL)
    r74 = rdn('b674_rules.txt').split(NL)
    r05 = rdn('b705_rules.txt').split(NL)
    t04 = rdn('b704_tie.txt').split(NL)
    cut = jl('b704_cut.json')
    rows = []
    for i, l in enumerate(t04, 1):
        m = re.match(r'^\s+(\d+) \| (\w[\w ]*?)\s+\| (.*?)(?:\s+### b702`s cut: .*)?$', l)
        if m and ' (b702_tie :' in l:
            rows.append(dict(line=i, count=int(m.group(1)), kind=m.group(2).strip(), row=m.group(3)))
    for r in rows:
        if r['row'].startswith('day1/ONE_PAGE_PROOF.md') and cut.get('after') is not None:
            r['count_b704'], r['count'] = r['count'], cut['after']
    kern = [r for r in rows if r['kind'] == 'kernel']
    comp = sorted([r for r in rows if r['kind'] == 'companion'], key=lambda r: -r['count'])
    top = comp[0]['count'] if comp else None
    at_top = [r for r in comp if r['count'] == top]
    L = ['%s -- STEP ZERO, (R322)(6): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER, b674`S TIE-BREAK RULE AND b705`S ROW (2) PRINTED BEFORE IT IS NAMED (%s)' % (ACT, utc()), '',
         '### b652`S ORDER, VERBATIM FROM relay data/b652_ferry.txt :19:', '    ' + f52[18].strip(), '',
         '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:'] + [r74[k] for k in range(7, 11)] + ['',
         '### data/b705_rules.txt ROW (2), VERBATIM FROM :11-:14:'] + [r05[k] for k in range(10, 14)] + ['',
         '### THE AGENDA`S ROWS, VERBATIM FROM b704`S TIE BANK (relay data/b704_tie.txt :14-:46, b702`s cut entered there), b704`S CUT ENTERED FROM relay data/b704_cut.json',
         '### (%s %s -> %s); rows are documents: the count now | the kind | the row (its line in b704`s bank):' % (cut.get('document'), cut.get('before'), cut.get('after'))]
    L += ['  %4d | %-9s | %s (b704_tie :%d)%s' % (r['count'], r['kind'], r['row'], r['line'], ('   ### b704`s cut: %d -> %d' % (r['count_b704'], r['count'])) if 'count_b704' in r else '')
          for r in rows]
    L += ['', '### THE KERNELS BY DESCENDING COUNT: the top count %s ; kernels at 0 %d of %d -- the order passes to the companions ("then the companions")' % (
        max([r['count'] for r in kern] or [0]), sum(1 for r in kern if r['count'] == 0), len(kern)),
          '### THE COMPANIONS BY DESCENDING COUNT: %s' % '; '.join('%s %d' % (r['row'].split('   ')[0].strip(), r['count']) for r in comp),
          '### THE TOP COUNT %s ; the documents standing at it %d' % (top, len(at_top)), '### the tables of the documents at the top count, their summary lines verbatim, and the document at HEAD against the table`s read:']
    tabs = []
    for r in at_top:
        tb = re.search(r'\[data/(b646_table_\w+\.txt)\]', r['row'])
        tl = rdn(tb.group(1)).split(NL) if tb else []
        sm = next((SUMMARY.match(x) for x in tl if SUMMARY.match(x)), None)
        dm = re.search(r'PLACE-papers (\S+) at (\w+), (\d+) lines, sha256 ([0-9a-f]{64})', NL.join(tl[:4]))
        doc = dm.group(1) if dm else '?'
        head_sha = hashlib.sha256((_show(PP, 'HEAD', doc) or '').encode('utf-8')).hexdigest() if dm else ''
        x = dict(row=r, bank=tb.group(1) if tb else None, summary=sm.group(0) if sm else '### NO SUMMARY LINE', doc=doc,
                 claims=int(sm.group(2)) if sm else 0, und=int(sm.group(5)) if sm else 0, over=int(sm.group(6)) if sm else 0,
                 unl=int(sm.group(7)) if sm else 0, read_sha=dm.group(4) if dm else '', head_sha=head_sha, read_at=dm.group(2) if dm else '')
        x['outside'] = x['over'] + x['unl'] + x['und']
        tabs.append(x)
        L += ['    relay data/%s : %s' % (x['bank'], x['summary']),
              '      the document %s: sha256 at the table`s read (%s) %s ; at PLACE-papers HEAD %s ; %s' % (
                  doc, x['read_at'], x['read_sha'][:16], head_sha[:16], 'UNMOVED' if x['read_sha'] == head_sha else '### MOVED SINCE ITS READ')]
    L += ['### b674`s rule, step by step in its written order:']
    pick = None
    if len(tabs) == 1:
        pick = tabs[0]
        L.append('    NOT REACHED: one document at the top count (b705`s row (2) not reached either: no tie to close)')
    elif tabs:
        ov = sorted(set(t['over'] for t in tabs))
        L.append('    (i) the rule`s condition, equal OVERREACHES counts: %s -- %s' % (', '.join('%s %d' % (t['doc'], t['over']) for t in tabs), 'MET' if len(ov) == 1 else 'NOT MET'))
        cand = tabs
        if len(ov) > 1:
            mo = max(t['over'] for t in tabs)
            cand = [t for t in tabs if t['over'] == mo]
            L.append('    data/b705_rules.txt row (2): b674`s measures in their written order, OVERREACHES first, the first that separates deciding: %s' % ', '.join(
                '%s %d' % (t['doc'], t['over']) for t in tabs))
        if len(cand) > 1:
            L.append('    (ii) a declared suite failure on either document: NONE (no arm of b711`s suite names either; data/b711_checks.txt)')
            mo = max(t['outside'] for t in cand)
            L.append('    (iii) the rows outside LICENSED/CITED of any kind (OVERREACHES + UNLICENSED + UNDERSTATES): %s' % ', '.join(
                '%s %d (%d + %d + %d)' % (t['doc'], t['outside'], t['over'], t['unl'], t['und']) for t in cand))
            c2 = [t for t in cand if t['outside'] == mo]
            if len(c2) > 1:
                mc = max(t['claims'] for t in c2)
                L.append('    (iv) the larger table (CLAIMS): %s' % ', '.join('%s %d' % (t['doc'], t['claims']) for t in c2))
                c2 = [t for t in c2 if t['claims'] == mc]
            cand = c2
        pick = cand[0] if len(cand) == 1 else None
        if pick is None and cand:
            L.append('    ### THE RULE ENDS IN A TIE -- RAISED, NOTHING NAMED')
    nxt = [r for r in comp if r['count'] < (top or 0)][:2]
    L += ['', '### ### **THE NEXT DOCUMENT BY b652`S ORDER, b674`S TIE-BREAK AND b705`S ROW (2): %s (A COMPANION ; THE TOP COUNT %s, %d DOCUMENT%s AT IT ; %s ; THE NEXT BY COUNT %s).**' % (
        pick['doc'] if pick else '### NONE NAMED', top, len(at_top), '' if len(at_top) == 1 else 'S', 'NO TIE' if len(tabs) == 1 else ('THE RULES READ IN THEIR WRITTEN ORDER' if pick else '### THE RULES DO NOT REACH THE TIE'),
        '; '.join('%s %d' % (r['row'].split('   ')[0].strip(), r['count']) for r in nxt))]
    if 'dry' not in a:
        put_txt('%s_tie.txt' % ACT, L)
        put_json('%s_tie.json' % ACT, dict(at=utc(), top=top, at_top=[t['doc'] for t in tabs], pick=pick['doc'] if pick else None,
                                          tables=[dict((k, v) for k, v in t.items() if k != 'row') for t in tabs]))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE PROBE THROUGH THE WORKFLOW'S STEP, (R322)(4)
def _lib_srcdirs(kernel_dir, rev='HEAD'):
    """the lakefile's lean_lib blocks with a srcDir, at rev: [(srcDir, name)] -- a module under a lib's srcDir is named relative to it (the
    vendored lib BulkaVendored at srcDir Vendored/Bulka: Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean is the module
    Lc.LiCriterion.ReverseDirection)."""
    txt = _show(kernel_dir, rev, 'lakefile.toml') or ''
    out = []
    name = None
    for l in txt.split(NL):
        m = re.match(r'^\s*name\s*=\s*"([^"]+)"', l)
        if m:
            name = m.group(1)
        m = re.match(r'^\s*srcDir\s*=\s*"([^"]+)"', l)
        if m:
            out.append((m.group(1).strip('/'), name))
    return out


def _print_modules708(kernel_dir, rev='HEAD'):
    """b705's _print_modules (tools/b705_record.py :732) with the carry-time repair of this act (data/b712_tool_repairs.txt row (1)): a hit under a
    lean_lib's srcDir is named relative to that srcDir, as Lake names it; every other hit as b705 named it (the path with / for . and no .lean)."""
    names = [l.strip() for l in (_show(kernel_dir, rev, 'print_targets.txt') or '').split(NL) if l.strip()]
    dirs = _lib_srcdirs(kernel_dir, rev)
    out = {}
    for n in names:
        short = n.split('.')[-1]
        hit = g(kernel_dir, 'grep', '-n', '-E', '-e', r'^(@\[[^]]*\] *)?((private|protected|noncomputable|nonrec) +)*(theorem|lemma|def|abbrev|structure|instance) +%s([ :({\[]|$)' % re.escape(short),
                rev, '--', '*.lean').strip()
        f = hit.split(':', 2)[1] if hit.count(':') >= 2 else ''
        if not f.endswith('.lean'):
            out[n] = None
            continue
        rel = f[:-5]
        for sd, _nm in dirs:
            if rel.startswith(sd + '/'):
                rel = rel[len(sd) + 1:]
                break
        out[n] = rel.replace('/', '.')
    return out


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: b706's runner706 carried with b712's names -- the run's artifact chosen BY NAME
    (build-module-<run id>; a run of the workflow uploads a second artifact, chain-probe-<run id>), its sha256 against the platform's digest
    before any reading, the build's exit and error lines, the memory log, the print step read, the gate."""
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    art, arts = _artifact_named(repo, run_id, 'build-module-')
    art = art or {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['%s -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (ACT, kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt')),
         '### the artifacts listed %d: %s ; the run`s own chosen by name (build-module-)' % (len(arts), [x.get('name') for x in arts])]
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
    print(NL.join(L[:15] + L[-3:]))


R.runner = runner


# ================================================================================ COMPONENT 5: THE CARRY-TIME REPAIR AND ITS CONTROLS
# ================================================================================ COMPONENT 5: THE FOUR STANDING FIGURES (b706`s tool, unedited, against b711`s baselines)
def figures(*a):
    """data/b712_standing_figures.txt (.json): the four figures by relay tools/b706_standing_figures.py, unedited (correspondence() and partners()
    over b706's roster, data/b706_roster_read.json; readme() b705's, pins() b703's), each against b711's figure (data/b711_standing_figures.json),
    the pins baseline b711's rows."""
    import b706_standing_figures as SF6
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b711_standing_figures.json')
    f = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    pr = (f.get('partners') or {}).get('rows') or []
    cr = (f.get('correspondence') or {}).get('papers') or []
    L = ['%s -- COMPONENT 5: THE FOUR STANDING FIGURES AT b712, READ BY b706`S TOOL OVER b706`S ROSTER, AGAINST b711`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b706_standing_figures.py, unedited (correspondence() and partners() over data/b706_roster_read.json, the 20 tables at the',
         '### unversioned names; readme() tools/b705_standing_figures.py`s, pins() tools/b703_standing_figures.py`s), %.0f s; each arm fails on a' % (t1 - t0),
         '### regression from the previous act`s figure (data/b711_standing_figures.json). The re-cut ((R322)(7)) is on PLACE-papers branch %s, unmerged;' % K.RECUT_BRANCH,
         '### the read is of PLACE-papers %s at %s; day1/Spectral_Inertness.md (cut at b708) is off the roster;' % (
             g(PP, 'rev-parse', '--abbrev-ref', 'HEAD').strip(), g(PP, 'rev-parse', '--short=8', 'HEAD').strip()),
         '### both kernels on main at the read (SIDE-lv-conservation`s checkout at main; port-b707 not checked out this act, b707`s trap).', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        L.append('  %-15s b712 %s ; b711 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE CORRESPONDENCE ROWS PER PAPER (current | behind | changed statement | unread ; the reason where the table is not read):']
    L += ['  %-36s %-66s current %3d behind %3d changed %3d unread %3d%s' % (p['paper'], p['path'], p['current'], p['behind'], p['changed'], p['unread'],
                                                                           (' ; ' + p['reason']) if p.get('reason') else '') for p in cr]
    L += ['', '### THE PARTNERS ROWS, ONE PER ROSTER TABLE:']
    L += ['  %-36s %-66s %s' % (r['paper'], r['path'], r.get('reason') or ('differing %s against %s' % (r.get('differing'), r.get('partner')))) for r in pr]
    one = sum(1 for r in pr if (r.get('reason') or '').startswith('ONE COPY'))
    L += ['', '### ### **FIGURES AT b712: CORRESPONDENCE %s ; README %s ; PARTNERS %s (ONE COPY %d OF %d TABLES) ; PINS %s -- AGAINST b711`S %s, %s, %s, %s ; THE ROSTER b706`S, %d TABLES.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), (f.get('partners') or {}).get('figure'), one, len(pr),
        (f.get('pins') or {}).get('figure'), (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'),
        (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'), len(cr))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), roster='b706_roster_read.json', baseline='b711_standing_figures.json',
                                                        **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:10] + L[-1:]))


def linecheck(*a):
    """`linecheck <record-lines bank> <i> <needle>...`: the suite's landed-line reading (tools/b703_checks.py landed) reproduced piece by piece and
    printed -- the bank's row, the ledger line at its number through the suite's own reader, conv(head), startswith and each needle; print only."""
    import b712_checks as CH
    bank, i = a[0], int(a[1])
    need = list(a[2:])
    rl = jl(bank)
    x = (rl.get('lines') or [])[i]
    find = CH.read(os.path.join(CH.PP, 'FINDINGS.md'))
    ot_ = CH.read(os.path.join(CH.PP, 'OPEN_TRAILS.md'))
    S_ = dict(find=find, ot=ot_)
    o = (CH.fline if x.get('file') == 'FINDINGS.md' else CH.oline)(S_, x.get('line'))
    h = conv(x.get('head', '\x00'))
    print('  row %d: file %s line %s ; the ledger text %d lines, %d chars' % (i, x.get('file'), x.get('line'), len(find.split(NL)), len(find)))
    print('  the line at that number (%d chars): %r' % (len(o), o[:160]))
    print('  conv(head) (%d chars): %r' % (len(h), h[:160]))
    print('  startswith %s ; first differing index %s' % (o.startswith(h), next((k for k in range(min(len(o), len(h))) if o[k] != h[k]), None)))
    for n_ in need:
        print('  needle %r in the line: %s' % (n_, n_ in o))
    if os.environ.get('LINECHECK_SUITE') == '1' or 'suite' in a:
        S = CH.sources(())
        xs = (S['rl'].get('lines') or [{}])[i]
        os_ = CH.fline(S, xs.get('line')) if xs.get('file') == 'FINDINGS.md' else CH.oline(S, xs.get('line'))
        print('  THE SUITE`S SOURCES: rl row %s ; find %d chars ; the line at its number (%d chars): %r' % (xs, len(S['find']), len(os_), os_[:120]))
        print('  CH.landed(S, %d, need) %s ; CH.weight_ok(S) %s' % (i, CH.landed(S, i, [n_ for n_ in need if n_ != 'suite']), CH.weight_ok(S)))


def defs(*a):
    """`defs <tool.py>`: the tool's top-level def names with their lines (print only) -- the span finder for a read by offset and limit."""
    src = rd(os.path.join(T, a[0])).split(NL)
    for i, l in enumerate(src, 1):
        if l.startswith('def ') or l.startswith('class ') or l.startswith('# ====='):
            print('  :%d %s' % (i, l[:100]))


def ksyms(*a):
    """`ksyms <tool.py>`: the worklist attributes a carried tool names as K.<NAME>, each with its lines, and which this act's worklist lacks --
    the carry's reading of what the previous act's objects were (print only, no bank)."""
    src = rd(os.path.join(T, a[0])).split(NL)
    seen = {}
    for i, l in enumerate(src, 1):
        for m in re.finditer(r'\bK\.([A-Z_0-9]+)', l):
            seen.setdefault(m.group(1), []).append(i)
    missing = sorted(n for n in seen if not hasattr(K, n))
    for n in sorted(seen):
        print('  %-28s %s lines %s' % (n, '### MISSING' if n in missing else 'present   ', seen[n][:12]))
    print('### ### **K.<NAME> REFERENCES %d ; MISSING FROM b712_worklist %d: %s.**' % (len(seen), len(missing), missing or 'NONE'))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R322)(1)
WH = ('*Appended 2026-10-25 by b712 to b711’s entry (:10306), under `(R322)`(1) -- b711 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b711_closing.txt):*')


def _fig(text, pat, what):
    m = re.search(pat, text)
    if not m:
        sys.exit('### b711`S BANKS DO NOT CARRY %s (%s) -- NOTHING COMPOSED' % (what, pat))
    return m.groups() if m.groups() else (m.group(0),)


def _fl(name, pat, what):
    """a figure read from a b711 bank with the line it stands on: (groups, line)."""
    for i, l in enumerate(rdn(name).split(NL), 1):
        m = re.search(pat, l)
        if m:
            return (m.groups() if m.groups() else (m.group(0),)), i
    sys.exit('### data/%s DOES NOT CARRY %s (%s) -- NOTHING COMPOSED' % (name, what, pat))


def _wb():
    """b711's weight line, every figure read from b711's banks by row and cited by its line: the head from its closing :1, the pairs, the
    coefficients, the surgery, the axis, the list, the report's comparisons, the port's held line, the root and its banks, the mirror, the
    scores at the close, the suite from its two banks, the defects by the repaired reader and the events by their starting lines."""
    c = rdn('b711_closing.txt')
    head = c.split(NL)[0]
    (r11,), l11 = _fl('b711_pairs.txt', r'^\s*11 \|.*n\*/F2 (0\.\d+)', 'pair 11`s ratio')
    (r15,), l15 = _fl('b711_pairs.txt', r'^\s*15 \|.*n\*/F2 (0\.\d+)', 'pair 15`s ratio')
    _x, lpv = _fl('b711_pairs.txt', r'THE LAW HELD', 'the pairs` verdict')
    (cn, cv), lc = _fl('b711_coeffs.txt', r'THE LEAST n WITH c\(n\) < 0: n = (\d+) ; c\(\d+\) = (\(-8\) log 2 \+ \(-2\) log 3)', 'the least negative index')
    (thru, neg), lneg = _fl('b711_coeffs.txt', r'THE COUNT OF NEGATIVE COEFFICIENTS through (\d+): (\d+)', 'the negative count')
    _x, lsu = _fl('b711_surgery.txt', r'THE SURGERY HELD', 'the surgery`s verdict')
    _x, lax = _fl('b711_axis.txt', r'THE AXIS \(e\) REFUTED', 'the axis`s verdict')
    (reach,), lli = _fl('b711_list.txt', r'THE LIST COMPLETE TO (\d+)\.0 ; BANDS ABOVE 325', 'the reached height')
    bands = [l for l in rdn('b711_list.txt').split(NL) if l.strip().startswith('band [')]
    on = sum(int(re.search(r'on-line (\d+)', l).group(1)) for l in bands)
    off = sum(int(re.search(r'off-line (\d+)', l).group(1)) for l in bands)
    (ncmp,), lcmp = _fl('b711_report.txt', r'^### THE COMPARISONS \((\d+)\)', 'the report`s comparisons')
    _x, ldif = _fl('b711_report.txt', r'^### DIFFERS: NONE', 'the report`s DIFFERS row')
    _x, lseat = _fl('b711_report.txt', r'^### BANKS NOT SEATED .*: NONE', 'the report`s seated row')
    _x, lport = _fl('b711_port.txt', r':501:31', 'the port`s held line')
    (built,), lbu = _fl('b711_port.txt', r'(\d+) of 12', 'the modules built')
    (banks,), lrb = _fl('b711_root_banks.txt', r'BANKS (\d+) ; CLEAN AND EQUAL AT HEAD', 'the root banks')
    (msha,), lmi = _fl('b711_closing.txt', r'sha256 ([0-9a-f]{8})[0-9a-f]* ; MANIFEST .* ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, lsc = _fl('b711_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD', 'the scores at the close')
    n_pre, p_pre = _fig(rdn('b711_checks.txt'), r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the pre-push suite')
    n_post, p_post = _fig(rdn('b711_checks_postpush.txt'), r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the post-push suite')
    ar = jl('b711_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b711_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    short = _defect_short('b711')
    evl = [i for i, l in enumerate(rdn('b711_events.txt').split(NL), 1) if re.match(r'^    \S', l)]
    if len(evl) != 16:
        sys.exit('### data/b711_events.txt READS %d STARTING LINES, NOT THE RULING`S SIXTEEN -- NOTHING COMPOSED' % len(evl))
    return (' “%s” (data/b711_closing.txt :1); its prompt count reads one prompt as two and it carries no score (data/b711_events.txt :79, '
            'repaired at (R322)(3)(iii)). As the banks confirm by row: the refined detection law of data/b710_registrations.txt (i) met at pair 11 '
            '(n*/F2 %s) and pair 15 (%s) (data/b711_pairs.txt :%d, :%d, :%d); Q0’s log-derivative coefficients negative from n = %s, c(%s) = %s, '
            '%s negative through %s (data/b711_coeffs.txt :%d, :%d); the surgery HELD (data/b711_surgery.txt :%d); the axis (e) REFUTED by its '
            'registered falsifier (data/b711_axis.txt :%d); the certified list complete to height %s, %d on-line and %d off-line zeros added above '
            '325 in %d bands (data/b711_list.txt :%d, the band rows); the Independence supplement in data/b711_independence.txt; the throughstone '
            'report’s %s comparisons, DIFFERS NONE, every bank seated, S2 not scorable before the root on the author’s word (data/b711_report.txt '
            ':%d, :%d, :%d); the port at %s of 12 modules, held at DirichletC7Order.lean :501:31 (data/b711_port.txt :%d), the join not dispatched; '
            'the entry at FINDINGS :%d; the trail at OPEN_TRAILS :%d carrying the root %s over %s banks (data/b711_root_banks.txt :%d); N1-N5 and '
            'S1-S3 HELD at scores close (data/b711_closing.txt :%d); the mirror mirror-refresh-2026-10-25-b711.zip (sha256 %s…) CLEAN on all three '
            'clauses with the root line (data/b711_closing.txt :%d); suite %s of %s pre-push and %s of %s post-push, NOT CLEAN (data/b711_checks.txt, '
            'data/b711_checks_postpush.txt); %d defects (a)–(%s) lettered before the seal (data/b711_defects.txt); %d events in data/b711_events.txt. '
            'Nothing deposited.' % (
                head, r11, r15, l11, l15, lpv, cn, cn, cv, neg, thru, lc, lneg, lsu, lax, reach, on, off, len(bands), lli, ncmp, lcmp, ldif, lseat,
                built, lport, K.B711_ENTRY, K.B711_TRAIL, ar['root'][:8], banks, lrb, lsc, msha, lmi, p_pre, n_pre, p_post, n_post, len(short),
                _letter(short[-1]) if short else '-', len(evl)))


def c1(*a):
    """FINDINGS: b711's weight line beneath b711's entry (:10306) through b698's landing and its screens; its line banked in
    data/b712_record_lines.json. `c1 dry` prints the line and writes nothing."""
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + _wb() + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B711_ENTRY,
         check=[('FINDINGS.md', K.B711_ENTRY, '## The faces’ join by closure at SIDE-faces-join held at DirichletC7Order.lean :501:31'),
                ('OPEN_TRAILS.md', K.B711_TRAIL, '### b711'), ('OPEN_TRAILS.md', K.ORDER_LV_PORT_TAG, '*Appended 2026-10-25 by b711')],
         dry=dry)


# ================================================================================ COMPONENT 1: THE REPAIRS' CONTROLS, (R322)(2)
def _data_state():
    """every file directly under relay data/: its size and its mtime_ns."""
    out = {}
    for f in os.listdir(D):
        p = os.path.join(D, f)
        if os.path.isfile(p):
            st = os.stat(p)
            out[f] = (st.st_size, st.st_mtime_ns)
    return out


def _trail_defects_body(act, start):
    """the body of the act's trail record's **Defects** line at OPEN_TRAILS, read from the record's head line `start` on."""
    ls = rd(OT).split(NL)
    for l in ls[start - 1:start + 120]:
        m = re.match(r'^\*\*Defects\*\* \(relay data/%s_defects\.txt\): (.*)\.$' % act, l)
        if m:
            return m.group(1)
    return None


def _run(*args):
    r = subprocess.run([sys.executable, '-X', 'utf8'] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT, timeout=300)
    return r.returncode, ((r.stdout or '') + (r.stderr or '')).replace(chr(13), '')


def _status():
    return g(ROOT, 'status', '--porcelain', '--untracked-files=all')


def repairctl(*a):
    """data/b712_repair_controls.txt (.json), Component 1, (R322)(2): each structural repair (standing clauses v2 rows (52)-(55)) and each item
    repair against the banks its old form failed on, with its NEG control; every reading printed beside the case. The suite's repaired forms are
    read from tools/b712_checks.py itself (imported), the closing's from tools/b712_closing.py, the membrane's from tools/act_membrane.py."""
    import b712_checks as CK
    import b712_closing as CL
    import act_membrane as MEM
    rows, notes, allok = [], [], True

    def case(sec, name, got, want, note=''):
        nonlocal allok
        ok = got == want
        allok = allok and ok
        rows.append(dict(section=sec, case=name, got=got, wanted=want, as_wanted=ok, note=note))

    # ---------------------------------------------------------------- (i) THE EVENTS SECTION
    sj7 = jl('b711_seal_hashes.json')
    seal7 = letters_at_seal('b711') or []
    s_let = [_letter(s) for s in seal7]
    now7 = [_letter(s) for s in letters_of(rdn('b711_defects.txt'))]
    body7 = _trail_defects_body('b711', K.B710_TRAIL) or ''
    t_let = re.findall(r"(?:^|; )\(([a-z]'?)\) ", body7)
    late7 = [x for x in now7 if x not in s_let]
    notes += ['(i) b711`s seal: %s, its relay head %s ; the letters in its defects bank at that head %s ; in the bank now %s ; on its trail`s Defects line '
              '(OPEN_TRAILS from :%d) %s ; after the seal, under the repaired route events: %s' % (
                  sj7.get('at'), (sj7.get('relay_head') or '')[:8], s_let, now7, K.B710_TRAIL, t_let, late7)]
    case('i', 'the ruling`s control: b711`s trail read under the repaired arms (its Defects letters against the letters entered before the seal) '
              'with (i) as an event passes', t_let == s_let, True,
         'the letters (g) and (h) were also entered after b711`s seal (lettered at relay 842ea536, after the seal`s head 71f1c2a0): under the rule`s '
         'cut they are events with (i)-(k), and b711`s trail, landed with (a)-(h), carries two of them -- for the author`s strike')
    case('i', 'NEG: a letter entered before the seal and missing from the trail fails (the seal`s letters with (z) added, the trail`s as entered)',
         s_let == s_let + ['z'], False)
    case('i', 'the trail carrying exactly the letters entered before the seal passes (the seal`s letters against themselves)', s_let == list(s_let), True)
    ev = []
    hl_new = CL.head_line(act='b711', events=ev)
    del CL.HEAD_EVENTS[:]
    CL.head_line(act='b711')
    sect = CL.events_section(act='b711')
    case('i', 'the closing`s events section over b711`s banks: the head-line builder`s failures land there, two (relay and PLACE-papers)',
         len([l for l in sect if l.startswith('    THE HEAD LINE: ')]), 2)
    notes += ['(i) the closing`s events section over b711`s banks: ' + ' | '.join(sect)]
    # ---------------------------------------------------------------- (ii) THE MEMBRANE
    test_roots = os.path.join(K.SP, 'b712_membrane_roots.txt')
    real = rd(MEM.ROOTS)
    with open(test_roots + '.tmp', 'wb') as fh:   # ### the control's own scratch write, outside relay
        fh.write((real.rstrip(NL) + NL + 'b712 %s %s' % ('f' * 64, (jl('b711_act_root.json').get('root') or '0' * 64)) + NL).encode('utf-8'))
    os.replace(test_roots + '.tmp', test_roots)
    probe = os.path.join(D, 'b712_membrane_probe.json')
    try:
        MEM.guard('b712', 'b712_membrane_probe.json', R.ROOT_EXCLUDE, roots=test_roots)
        code = 0
    except SystemExit as e:
        code = e.code
    case('ii', 'a bank write attempted after a test root refuses: the guard exits 4 and the bank is not written', (code, os.path.exists(probe)), (4, False))
    case('ii', 'after the test root a bank the root names is refused (data/b712_reading5.txt, data/b712_repair_controls.txt)',
         (bool(MEM.refuses('b712', 'b712_reading5.txt', R.ROOT_EXCLUDE, test_roots)), bool(MEM.refuses('b712', 'b712_repair_controls.txt', R.ROOT_EXCLUDE, test_roots))),
         (True, True))
    case('ii', 'after the test root the excluded banks pass: the closing, the events, the step bank, the push capture, the mirror builder`s',
         [bool(MEM.refuses('b712', n, R.ROOT_EXCLUDE, test_roots)) for n in ('b712_closing.txt', 'b712_events.txt', 'b712_steps.json', 'b712_relay_push_out.txt', 'b712_mirror.json')],
         [False] * 5)
    case('ii', 'on the real chain (b712 not appended) a write proceeds', bool(MEM.refuses('b712', 'b712_reading5.txt', R.ROOT_EXCLUDE)), False)
    case('ii', 'POS on the real chain: b711 is appended, so a b711 bank the root names is refused', bool(MEM.refuses('b711', 'b711_reading5.txt')), True)
    _wrap = lambda f: getattr(f, '__name__', '') in ('put_json', 'put_txt') and getattr(f, '__module__', '') in ('__main__', 'b712_record')   # noqa: E731
    wired = dict(record=(_wrap(R.put_json) and _wrap(R.put_txt)), citation=rd(os.path.join(T, 'b712_citation.py')).count('MEM.guard('),
                 closing=rd(os.path.join(T, 'b712_closing.py')).count('_guard('), suite=rd(os.path.join(T, 'b712_checks.py')).count('_membrane('),
                 independence=rd(os.path.join(T, 'b712_independence.py')).count('_membrane('), standing=rd(os.path.join(T, 'b712_standing.py')).count('_membrane('),
                 tests=rd(os.path.join(T, 'b712_tests.py')).count('_membrane('), carry=rd(os.path.join(T, 'b712_carry.py')).count('_membrane('))
    notes += ['(ii) the guard wired in the writers (calls in the text, the definition counted): %s' % wired]
    case('ii', 'every b712 writer calls the guard (the record`s shared writers rebound; the citation`s, the closing`s, the suite`s, independence`s, '
               'standing`s, the tests` and the carry`s calls present)', all(wired.values()), True)
    st0, ds0 = _status(), _data_state()
    rc1, o1 = _run(os.path.join(T, 'b712_record.py'), 'defs', 'b712_checks.py')
    rc2, o2 = _run(os.path.join(T, 'b712_record.py'), 'names', 'b712_checks')
    rc3, o3 = _run(os.path.join(T, 'b712_citation.py'), 'replay', 'Root: 1, proceed', K.PREV_SESSION, K.PREV_ANCHOR)
    st1, ds1 = _status(), _data_state()
    changed = sorted(f for f in set(ds0) | set(ds1) if ds0.get(f) != ds1.get(f))
    case('ii', 'three locator and read calls (the record tool`s defs and names routes, the citation tool`s replay) leave the tree unchanged by git '
               'status and relay data/ unchanged file for file', (rc1, rc2, rc3, st0 == st1, changed), (0, 0, 0, True, []))
    # ---------------------------------------------------------------- (iii) ARMS READ STRUCTURE
    g8, g9, g10 = rdn('b708_reg_gate.txt'), rdn('b709_reg_gate.txt'), rdn('b711_reg_gate.txt')
    case('iii', 'G-CLOSING-DRY-STEP: b708`s sealed needle on b708`s honest gate record fails (the bank b708 failed on)', '### NO VERDICT LINE' not in g8, False)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b708`s gate record passes', CK.no_verdict_line_ok(g8), True)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b709`s gate record (three rows) passes', CK.no_verdict_line_ok(g9), True)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b711`s gate record passes', CK.no_verdict_line_ok(g10), True)
    case('iii', 'NEG: b709`s record with a NO VERDICT LINE row named on a verdict-bearing bank (data/b709_pairs.txt) fails',
         CK.no_verdict_line_ok(g9.replace('data/b709_grid_hashes.txt): ### NO VERDICT LINE', 'data/b709_pairs.txt): ### NO VERDICT LINE')), False)
    case('iii', 'NEG: b709`s record with a NO VERDICT LINE row naming an absent bank fails',
         CK.no_verdict_line_ok(g9.replace('data/b709_grid_hashes.txt): ### NO VERDICT LINE', 'data/b709_nosuch.txt): ### NO VERDICT LINE')), False)
    k9 = ('ONSET', 'ZETA', 'RATIO', 'MODULES', 'FIGURES')
    rj9, rj10 = jl('b709_report.json'), jl('b711_report.json')
    case('iii', 'G-REPORT-UNSEALED: b709`s sealed needle on b709`s report text (the keys in capitals) fails', all(x in rdn('b709_report.txt') for x in k9), False)
    case('iii', 'G-REPORT-UNSEALED: the repaired reading of b709`s report JSON bank (its lines) passes', CK.report_lines_ok(rj9, k9, 5), True)
    case('iii', 'G-REPORT-UNSEALED: the repaired reading of b711`s report JSON bank on b711`s keys passes', CK.report_lines_ok(rj10, CK.REPORT_KEYS, 5), True)
    case('iii', 'NEG: b709`s report JSON with its lines cut to four fails', CK.report_lines_ok(dict(rj9, lines=(rj9.get('lines') or [])[:4]), k9, 5), False)
    case('iii', 'NEG: b709`s report JSON with every `ratio` removed, any case, fails',
         CK.report_lines_ok(dict(rj9, lines=[re.sub('(?i)ratio', 'quotient', x) for x in (rj9.get('lines') or [])]), k9, 5), False)
    q = '(e) representation coordinates (the operator / Toeplitz form) -- 4'
    reg9 = rdn('b709_registrations.txt')
    case('iii', 'G-AXIS-REGISTERED: b709`s sealed needle on b709`s registrations bank (the quotation wrapped) fails', q in reg9, False)
    case('iii', 'G-AXIS-REGISTERED: the repaired reading (joined; the bank has no JSON) passes', q in CK.joined(reg9), True)
    case('iii', 'NEG: the repaired reading on a copy with "Toeplitz" changed to "Hankel" fails', q in CK.joined(reg9.replace('Toeplitz', 'Hankel')), False)
    case('iii', 'each arm run on b711`s banks before the seal: the seal refuses while a part`s run on b711`s banks is not banked', bool(CK.prev_run_missing()), True)
    # ---------------------------------------------------------------- (iv) CONTROLS THAT CAN FAIL
    face7 = rd(os.path.join(ROOT, *K.B711_FACE.split('/')))
    S7 = dict(citation=rdn('b711_citation_check.txt'), lock_epoch=CK.utc_epoch(face7, 'locked at (UTC)'), movesj=jl('b711_moves_lines.json'),
              answers=rdn('b711_author_answers.txt'), files=dict(c3pp=[x for x in g(PP, 'show', '--name-only', '--pretty=format:', K707.C3_PP).split(NL) if x.strip()]))
    live7 = CK.answers_before_ok(dict(S7))
    old7 = CK.answers_before_ok(dict(S7, answers=S7['answers'] + NL + '### PROMPT 9 (planted)'))
    new7 = CK.answers_before_ok(CK.answers_plant(dict(S7)))
    case('iv', 'G-ANSWERS-BEFORE-WRITES on b711`s banks: the live reading passes (the moves answer checked before its landing and the lock)', live7, True)
    case('iv', 'G-ANSWERS-BEFORE-WRITES: b711`s plant (a prompt appended) leaves the arm passing -- the control that cannot fail', old7, True)
    case('iv', 'G-ANSWERS-BEFORE-WRITES: the repaired plant (every check stamp moved after the write it governs) fails the arm', new7, False)
    ex7 = jl('b711_exercise.json').get('exercise') or {}
    case('iv', 'the seal`s refusal over b711`s exercise bank: the arms whose mutated copy passed, the one b711 carried',
         sorted(n for n, e in ex7.items() if e.get('pos')), ['G-ANSWERS-BEFORE-WRITES'])
    shown, bad = CK.neg_shown()
    case('iv', 'the seal refuses now: no pre-run exercise bank is written, so no arm is shown failing (every arm named)', (len(shown), len(bad) == len(CK.ARMS)), (0, True))
    # ---------------------------------------------------------------- THE ITEM REPAIRS: (k) THE HEAD LINE, (i) THE STEP BANK, THE 468
    import b711_closing as CL7
    hl_old = CL7.head_line()
    case('k', 'b711`s builder over b711`s captures: the head line carries the capture-name failure', 'IS NOT THE RECORD`S CAPTURE' in hl_old, True)
    case('k', 'the repaired builder over b711`s captures: the head line carries the record`s commits and no failure text',
         (hl_new.startswith('b711 closed: relay 2c200e8d, PLACE-papers df2dd7c; suite 137 of 143; root 11fe3e21e2fc796a'), '###' in hl_new), (True, False))
    case('k', 'the repaired builder sends both capture-name failures to the events section', len(ev), 2)
    notes += ['(k) the repaired head line over b711`s banks: %s' % hl_new] + ['(k) event: %s' % e for e in ev]
    lock7 = S7['lock_epoch']

    def _log(repo, base, tip):
        return [(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
                g(repo, 'log', '--reverse', '--format=%h %ct %s', '%s..%s' % (base, tip)).split(NL) if l.strip()]
    rl7, pl7 = _log(ROOT, K707.PRE_RELAY, 'b0d874f7'), _log(PP, K707.PRE_PP, 'df2dd7c0')
    ps7 = re.search(r'^POST_SEAL = (\(.*\))$', rd(os.path.join(T, 'b711_checks.py')), re.M)
    import ast
    post7 = ast.literal_eval(ps7.group(1)) if ps7 else ()
    old_sa = all((t < lock7) == (s.startswith('b711') and not s.startswith(post7)) for h, s, t in rl7 + pl7)
    case('i/step', 'G-SEALED-AFTER-COMPONENTS: b711`s subject reading over b711`s commits fails (7c07c5d4 "b711 order", df2dd7c0 "b711 trail")', old_sa, False)
    full = lambda repo, h: g(repo, 'rev-parse', h).strip()   # noqa: E731
    fixture = [dict(repo='relay', commit=full(ROOT, h), phase=('component 5' if t < lock7 else 'record')) for h, s, t in rl7] + \
              [dict(repo='pp', commit=full(PP, h), phase=('component 3' if t < lock7 else 'record')) for h, s, t in pl7]
    S8 = dict(lock_epoch=lock7, steps=fixture, rlog=rl7, plog=pl7, REC=sys.modules[__name__])
    case('i/step', 'the repaired reading over a step bank for b711`s commits (b711 had none: the fixture`s phases set from each commit`s time against '
                   'the lock, so this row shows the reading is by the bank alone) passes', CK.sealed_after_ok(S8), True)
    case('i/step', 'NEG: a PLACE-papers commit after the lock given a component phase fails',
         CK.sealed_after_ok(dict(S8, steps=[dict(r, phase='component 3') if r['repo'] == 'pp' else r for r in fixture])), False)
    case('i/step', 'NEG: a commit with no row in the step bank fails', CK.sealed_after_ok(dict(S8, steps=fixture[1:])), False)
    m82 = re.search(r'b682\s+cut: (\d+) characters', o3)
    mre = re.search(r'repaired cut: (\d+) characters', o3)
    meq = re.search(r'the whole answer (\d+) characters ; the repaired cut equal to the text from its BEGIN to its last END: (\w+)', o3)
    case('468', 'the citation tool`s answer check over b711`s root answer: b682`s cut 468 characters, the repaired cut to the last END, equal to the '
                'text from its BEGIN to its last END (tools/b712_citation.py replay, print only)',
         (m82.group(1) if m82 else None, bool(mre) and int(mre.group(1)) > 468, meq.group(2) if meq else None), ('468', True, 'True'))
    notes += ['(468) %s' % l.strip() for l in o3.split(NL) if l.strip()]
    L = ['%s -- COMPONENT 1, (R322)(2): THE FOUR STRUCTURAL REPAIRS AND THE THREE ITEM REPAIRS AGAINST THEIR OLD FORMS, WITH THEIR CONTROLS (%s)' % (ACT, utc()), '',
         '### rows are cases: the section | the case | the reading got | the reading wanted | AS WANTED. The sections: (i) the events section and the',
         '### letters at the seal (standing clauses v2 row (52)); (ii) the membrane (row (53)); (iii) arms read structure (row (54)); (iv) controls that',
         '### can fail (row (55)); (k) the closing`s head-line builder; (i/step) G-SEALED-AFTER-COMPONENTS by the step bank; (468) the answer check.',
         '### The repaired forms read where they stand: tools/b712_checks.py (no_verdict_line_ok, report_lines_ok, joined, the trail arms, sealed_after_ok,',
         '### answers_plant, neg_shown, prev_run_missing), tools/b712_closing.py (head_line, events_section), tools/act_membrane.py, tools/b712_citation.py.', '']
    L += ['  %-6s | %-150s | got %-34s | wanted %-34s | %s' % (r['section'], r['case'][:150], str(r['got'])[:34], str(r['wanted'])[:34],
                                                            'AS WANTED' if r['as_wanted'] else '### NOT AS WANTED -- ' + r['note']) for r in rows]
    L += ['', '### THE READINGS BESIDE THE CASES:'] + ['  ' + n for n in notes]
    nw = [r for r in rows if not r['as_wanted']]
    L += ['', '### ### **CASES %d ; AS WANTED %d ; NOT AS WANTED %d%s.**' % (
        len(rows), len(rows) - len(nw), len(nw), (' (' + '; '.join('%s: %s' % (r['section'], r['case'].split(' (')[0]) for r in nw) + ', for the author`s strike)') if nw else '')]
    if 'dry' not in a:
        put_txt('%s_repair_controls.txt' % ACT, L)
        put_json('%s_repair_controls.json' % ACT, dict(at=utc(), cases=rows, as_wanted=allok, not_as_wanted=len(nw), changed=changed, events=ev))
    print(NL.join(L[8:]))


# ================================================================================ COMPONENT 1: THE REPAIRS AND THEIR DIFFS, (R322)(2)
REPAIRS = (
    ('(52)', '(R322)(2)(i), THE EVENTS SECTION',
     'tools/b712_closing.py events_section (the section beneath the defects: data/b712_events.txt`s rows and the head-line builder`s failures); '
     'tools/b712_checks.py the three trail-equality arms and G-TRAIL-DEFECTS-EQUAL`s Defects line read S[letters_seal], the letters entered before '
     'the seal, and the seal records them (`letters`, `defects_sha256`); tools/b712_record.py letters_of, letters_at_seal (the seal`s list, or for '
     'an act sealed before the repair its defects bank at the seal`s relay head), the defects route refusing a letter after the seal; EXCLUDE_KINDS '
     'events and steps. Control: data/b712_repair_controls.txt (i) -- the ruling`s control NOT AS WANTED on b711`s banks, defect (d)'),
    ('(53)', '(R322)(2)(ii), THE MEMBRANE',
     'tools/act_membrane.py (new, shared, whole below): appended, named, refuses, guard, guard_path; tools/b712_record.py b698`s put_json and '
     'put_txt wrapped and rebound in b703`s to b711`s modules; the guard before every bank write of tools/b712_citation.py (its two writers and '
     'the answer route`s rewritten body), tools/b712_closing.py, tools/b712_checks.py, tools/b712_independence.py, tools/b712_standing.py, '
     'tools/b712_tests.py and tools/b712_carry.py. THE READING, FOR THE AUTHOR`S STRIKE: "a named bank" is a bank the act`s root names (b711`s (j) '
     'quotes its ferry: "no named bank written after it") -- every file directly under relay data/ that the act`s ROOT_EXCLUDE does not take out; '
     'the mirror builder`s banks pass by name (the b670 form); the closing, its censuses and pins, the push captures, the defects, events and step '
     'banks are excluded kinds and stay writable after the root. Control: (ii) -- a test root refuses, a locator call leaves git status unchanged'),
    ('(54)', '(R322)(2)(iii), ARMS READ STRUCTURE',
     'tools/b712_checks.py no_verdict_line_ok (the gate`s NO VERDICT LINE rows read by the bank each names, NO_VERDICT_EXEMPT`s list of names '
     'removed -- the carry had turned b711`s entry into data/b711_prints_v0.17.txt, a bank that does not exist); report_lines_ok and '
     'report_unsealed_ok reading data/b712_report.json (its `at` and `lines`); joined kept for the registrations (no JSON bank); `--prev --part <p>` '
     'runs a part`s arms on b711`s banks (_prev_rebind, _PrevWorklist) and banks data/b712_prevrun_<part>.txt and data/b712_prevrun_exercise_<part>.json '
     'beside b711`s own verdicts (_prev_verdicts); the seal refuses while a part`s run is not banked (prev_run_missing). Control: (iii) -- the three '
     'needles pass on their acts` honest output and their NEG copies fail'),
    ('(55)', '(R322)(2)(iv), CONTROLS THAT CAN FAIL',
     'tools/b712_checks.py: the main loop records per arm `pos_raised` and `shown_failing` and per part the run`s `mode`, `at` and relay head; '
     'neg_shown reads the pre-run`s exercise banks; seal() refuses, recording nothing, while any arm`s mutated copy has not been shown failing '
     '(passed, raised, or no pre-run row); G-ANSWERS-BEFORE-WRITES`s plant answers_plant moves every check stamp after the write it governs. '
     'Control: (iv) -- b711`s plant leaves the arm passing, the repaired plant fails it'),
    ('(k)', 'THE CLOSING`S HEAD-LINE BUILDER (b711`s (k))',
     'tools/b712_closing.py head_line and _captures: each repository`s record commit the main its last capture of the act read back (the closing`s '
     'own excluded, ordered by the captures` stamps); a capture-name failure goes to HEAD_EVENTS and the events section, never the head line. '
     'Control: (k) -- over b711`s captures the line reads relay 2c200e8d, PLACE-papers df2dd7c, the two failures in the events section'),
    ('(i)', 'G-SEALED-AFTER-COMPONENTS BY THE STEP BANK (b711`s (i))',
     'tools/b712_record.py step (data/b712_steps.json: the repository, the commit, its time, the phase named from STEP_PHASES), PRE_SEAL_PHASES; '
     'tools/b712_checks.py sealed_after_ok and _step_phase reading the bank, not the subjects. Control: (i/step)'),
    ('468', 'THE CITATION TOOL`S ANSWER CHECK',
     'tools/b712_citation.py answer: b682`s cut `best.find(\'END\', k)` replaced by `best.rfind(\'END\')` in the rewritten body (checked to occur '
     'once); the replay route prints both cuts. Control: (468) -- b711`s root answer, 468 characters by b682`s cut, 1554 by the repaired, equal to '
     'the text from its BEGIN to its last END'),
)
REPAIR_TRACKED = ('tools/b712_record.py', 'tools/b712_citation.py', 'tools/b712_independence.py', 'tools/b712_standing.py', 'tools/b712_tests.py',
                  'tools/b712_carry.py', 'tools/b712_worklist.py')
REPAIR_CARRIED = ('checks', 'closing')


def toolrepairs(*a):
    """data/b712_tool_repairs.txt (.json), Component 1, (R322)(2): each repair's row (the delta's row of standing clauses v2, its objects, its
    control's section in data/b712_repair_controls.txt); the diffs: the tools committed at step zero (relay 4aa6e281) by `git diff HEAD`, the
    carried tools by their repairdiff banks (tools/b712_carry.py repairdiff), the new shared tool tools/act_membrane.py whole."""
    ctl = jl('%s_repair_controls.json' % ACT)
    if not ctl.get('cases'):
        sys.exit('### data/b712_repair_controls.json IS NOT WRITTEN -- THE CONTROLS FIRST; NOTHING WRITTEN')
    nw = [c for c in ctl['cases'] if not c.get('as_wanted')]
    L = ['%s -- COMPONENT 1, (R322)(2): THE FOUR STRUCTURAL REPAIRS (STANDING CLAUSES v2 ROWS (52)-(55)) AND THE THREE ITEM REPAIRS, WITH THEIR DIFFS (%s)' % (ACT, utc()), '',
         '### rows are repairs: the row | what is repaired | its objects, the reading and its control. The controls: relay data/b712_repair_controls.txt',
         '### (%d cases, %d as wanted, %d not as wanted -- %s). The diffs follow the rows.' % (
             len(ctl['cases']), len(ctl['cases']) - len(nw), len(nw), '; '.join(c['case'].split(' (')[0] for c in nw) or 'none'), '']
    for n, what, objs in REPAIRS:
        L += ['  %s %s.' % (n, what)] + ['      ' + x for x in _wrap_words(objs, 140)] + ['']
    L += ['### THE DIFFS OF THE TOOLS COMMITTED AT STEP ZERO (relay 4aa6e281), `git diff HEAD`, each whole:']
    stat = []
    for p in REPAIR_TRACKED:
        d = g(ROOT, 'diff', 'HEAD', '--', p).replace(chr(13), '').rstrip(NL)
        add = sum(1 for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))
        rem = sum(1 for l in d.split(NL) if l.startswith('-') and not l.startswith('---'))
        stat.append((p, add, rem))
        L += ['', '### %s : +%d -%d' % (p, add, rem)] + (['    ' + l for l in d.split(NL)] if d else ['    (unchanged)'])
    L += ['', '### THE CARRIED TOOLS` REPAIRS, BY THEIR REPAIRDIFF BANKS (the carried form against the file now; every carry-time change of the tool):']
    for n in REPAIR_CARRIED:
        v = (re.findall(r'^### ### \*\*(.*)\*\*\s*$', rdn('%s_repairdiff_%s.txt' % (ACT, n)), re.M) or ['### NO REPAIRDIFF BANK'])[-1]
        L += ['  tools/%s_%s.py -- data/%s_repairdiff_%s.txt: %s' % (ACT, n, ACT, n, v)]
    mem = rd(os.path.join(T, 'act_membrane.py')).rstrip(NL)
    L += ['', '### THE NEW SHARED TOOL tools/act_membrane.py, WHOLE (%d lines):' % len(mem.split(NL))] + ['    ' + l for l in mem.split(NL)]
    L += ['', '### ### **REPAIRS 7 (THE FOUR OF v2 ROWS (52)-(55), THE THREE ITEMS) ; CONTROLS %d, AS WANTED %d, FOR THE AUTHOR`S STRIKE %d ; TRACKED TOOLS DIFFED %d ; '
              'CARRIED TOOLS BY REPAIRDIFF %d ; ONE NEW SHARED TOOL ; NO SEALED TOOL OF AN EARLIER ACT EDITED.**' % (
                  len(ctl['cases']), len(ctl['cases']) - len(nw), len(nw), len(REPAIR_TRACKED), len(REPAIR_CARRIED))]
    if 'dry' in a:
        print(NL.join(L[:40] + L[-1:]))
        return
    put_txt('%s_tool_repairs.txt' % ACT, L)
    put_json('%s_tool_repairs.json' % ACT, dict(at=utc(), repairs=[dict(row=n, what=w) for n, w, _o in REPAIRS], tracked=stat, carried=list(REPAIR_CARRIED),
                                                 controls=len(ctl['cases']), not_as_wanted=len(nw)))
    print(L[-1])


def _wrap_words(text, width):
    out, cur = [], ''
    for w in text.split(' '):
        if cur and len(cur) + 1 + len(w) > width:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w) if cur else w
    return out + ([cur] if cur else [])


# ================================================================================ COMPONENT 2, (R322)(4): THE PORT (b709's portedit, portdispatch and portrun, :1745-:1932, carried)
LV = K.LV_DIR
LV_MODULES = ('C7FiniteTypeFalse', 'C7OrderBounds', 'CouplingsAtPhi', 'DirichletC7Order', 'GammaBounds', 'PartialPositivity', 'RegisterPentagon', 'Smoke',
              'T1_MellinFactorization', 'T2_SDarkness', 'T3_StepNineBridge', 'ZeroCarrier')   # ### b709's twelve (data/b709_port.txt :19-:20)
LV_OTHER_LEAN = ('AxiomCheck.lean', 'PinnedGoal.lean', 'lakefile.lean')
OLD212 = '      (((hurwitzEvenFEPair a).toStrongFEPair.hasMellin w).1).norm'
NEW212 = '      (((hurwitzEvenFEPair a).isStrongFEPair_toStrongFEPair.hasMellin w).1).norm'
FORM_FILE, FORM_LINE = 'SIDELvConservation/C7OrderBounds.lean', 277   # ### b709's edit of the same form, its error cleared at run 40123142437


def _artifact_named(repo, run_id, prefix):
    rc, out, err = R._gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, int(run_id)))
    arts = (json.loads(out or b'{}') or {}).get('artifacts') or []
    art = next((x for x in arts if (x.get('name') or '').startswith(prefix)), None)
    return art, arts


MATHLIB_DIR = os.path.join(K.EF_DIR, '.lake', 'packages', 'mathlib')   # ### SIDE-explicit-formula's Mathlib checkout, at de5ce8a9 (the port's pin)
MATHLIB_PIN = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'
# ### (R322)(4): the port's edits, one per held line, each in the form Mathlib de5ce8a9 states, each read there and printed before its edit
PORT_EDITS = (
    dict(n=1, line=501, base=K.PORT_TIP,
         old='  rw [completedHurwitzZetaOdd, StrongFEPair.Λ_eq, norm_div, show ‖(2 : ℂ)‖ = 2 by norm_num]',
         new='  rw [completedHurwitzZetaOdd, (isStrong_hurwitzOddFEPair a).Λ_eq, norm_div, show ‖(2 : ℂ)‖ = 2 by norm_num]',
         error='error: SIDELvConservation/DirichletC7Order.lean:501:31: Unknown identifier `StrongFEPair.Λ_eq` (data/b711_port.txt :11)',
         decls=(('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 100, 100, 'the strong pair a predicate on a weak pair'),
                ('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 461, 481, 'IsStrongFEPair.Λ_eq, its hypothesis hP explicit'),
                ('Mathlib/NumberTheory/LSeries/HurwitzZetaOdd.lean', 300, 302, 'the odd pair a WeakFEPair'),
                ('Mathlib/NumberTheory/LSeries/HurwitzZetaOdd.lean', 325, 327, 'the odd pair`s strong proof'),
                ('Mathlib/NumberTheory/LSeries/HurwitzZetaOdd.lean', 339, 340, 'completedHurwitzZetaOdd through the pair`s Λ'))),
    dict(n=2, line=574, base='42da39ea2c03859ef6e74a9b752d9783816b430a',
         old='      (((hurwitzOddFEPair a).hasMellin w).1).norm',
         new='      (((isStrong_hurwitzOddFEPair a).hasMellin w).1).norm',
         error=('error: SIDELvConservation/DirichletC7Order.lean:574:39: Application type mismatch: the argument w : ℂ where '
                '(hurwitzOddFEPair a).k < re ?m is expected, in WeakFEPair.hasMellin (hurwitzOddFEPair a) w (data/b712_buildlog_SIDE-lv-conservation_port1.txt :99-:106)'),
         decls=(('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 402, 406, 'WeakFEPair.hasMellin, its hypothesis k < re s'),
                ('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 483, 485, 'IsStrongFEPair.hasMellin, s alone'),
                ('Mathlib/NumberTheory/LSeries/HurwitzZetaOdd.lean', 325, 327, 'the odd pair`s strong proof'))),
)


def _port_edit(n):
    e = next((x for x in PORT_EDITS if x['n'] == int(n)), None)
    if not e:
        sys.exit('### NO PORT EDIT %s IN PORT_EDITS -- NOTHING WRITTEN' % n)
    return e


def _decl_lines(e):
    """each declaration of the edit read at Mathlib de5ce8a9 by `git show <pin>:<path>`, its lines by number."""
    out = []
    for path, a0, a1, what in e['decls']:
        src = (g(MATHLIB_DIR, 'show', '%s:%s' % (MATHLIB_PIN, path)) or '').replace(chr(13), '').split(NL)
        out.append(('%s :%d-:%d (%s)' % (path, a0, a1, what), ['%5d  %s' % (i, src[i - 1]) for i in range(a0, a1 + 1) if i <= len(src)]))
    return out


def portedit(*a):
    """`portedit <n> pre` -> data/b712_port_decl<n>.txt: the declarations the edit's form rests on, read at Mathlib de5ce8a9 by git show (the pin
    read from SIDE-explicit-formula's checkout, HEAD equal to it), printed BEFORE the Edit tool touches the kernel; the line as it stands, unedited.
    `portedit <n>` -> data/b712_port_edit<n>.txt (.json): the line as it stood at the edit's base and as the Edit tool left it, the diff of the
    module against the base by git diff, one hunk, one line; every other tracked file unchanged (git status), the declarations' bank cited."""
    e = _port_edit(a[0])
    head = g(LV, 'rev-parse', 'HEAD').strip()
    br = g(LV, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    pin_head = g(MATHLIB_DIR, 'rev-parse', 'HEAD').strip()
    src = (rd(os.path.join(LV, *K.PORT_FILE.split('/'))) or '').replace(chr(13), '').split(NL)
    n_ = e['line'] - 1
    if 'pre' in a[1:]:
        dl = _decl_lines(e)
        ok = (pin_head == MATHLIB_PIN and head == e['base'] and br == K.PORT_BRANCH and len(src) > n_ and src[n_] == e['old']
              and all(x[1] for x in dl))
        L = ['%s -- COMPONENT 2, (R322)(4): THE DECLARATIONS AT MATHLIB %s FOR THE PORT`S EDIT %d, PRINTED BEFORE THE EDIT (%s)' % (ACT, MATHLIB_PIN[:8], e['n'], utc()), '',
             '### the held line: %s' % e['error'],
             '### the Mathlib checkout read: %s at %s (the port`s lake-manifest pins %s) ; equal %s' % (MATHLIB_DIR.replace(chr(92), '/'), pin_head[:8], MATHLIB_PIN[:8], pin_head == MATHLIB_PIN),
             '### the kernel: %s on %s at %s (the edit`s base %s) ; :%d as it stands, unedited:' % (K.KERNEL, br, head[:8], e['base'][:8], e['line']),
             '    %s' % (src[n_] if len(src) > n_ else '### ABSENT'), '']
        for title, lines in dl:
            L += ['### %s at %s:' % (title, MATHLIB_PIN[:8])] + ['  ' + x for x in lines] + ['']
        L += ['### the form the edit takes: %s' % e['new'].strip(),
              '', '### ### **DECLARATIONS READ %d AT MATHLIB %s ; THE LINE UNEDITED %s ; READY FOR THE EDIT %s.**' % (len(dl), MATHLIB_PIN[:8], len(src) > n_ and src[n_] == e['old'], ok)]
        put_txt('%s_port_decl%d.txt' % (ACT, e['n']), L)
        print(NL.join(L))
        if not ok:
            sys.exit(1)
        return
    base = e['base']
    old = (g(LV, 'show', '%s:%s' % (base, K.PORT_FILE)) or '').replace(chr(13), '').split(NL)
    d = subprocess.run(['git', '-C', LV, 'diff', base, '--', K.PORT_FILE], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL)
    dl = d.split(NL) if d else []
    hunks = [l for l in dl if l.startswith('@@')]
    changed = [l for l in (g(LV, 'status', '--short') or '').split(NL) if l.strip() and not l.endswith('.lp.log')]
    l_old, l_new = old[n_] if len(old) > n_ else '', src[n_] if len(src) > n_ else ''
    nchg = sum(1 for i in range(min(len(src), len(old))) if src[i] != old[i])
    decl_bank = os.path.isfile(os.path.join(D, '%s_port_decl%d.txt' % (ACT, e['n'])))
    ok = (l_old == e['old'] and l_new == e['new'] and len(hunks) == 1 and changed == [' M ' + K.PORT_FILE] and head == base
          and br == K.PORT_BRANCH and len(old) == len(src) and nchg == 1 and decl_bank)
    L = ['%s -- COMPONENT 2, (R322)(4): THE PORT`S EDIT %d AT :%d ON %s, PRINTED BEFORE ITS COMMIT (%s)' % (ACT, e['n'], e['line'], K.PORT_BRANCH, utc()), '',
         '### the branch %s at %s (the edit`s base), HEAD unmoved before the commit; the one module %s edited by the Edit tool at one line' % (br, head[:8], K.PORT_FILE),
         '### the held line: %s' % e['error'],
         '### the declarations read at Mathlib %s before the edit: data/%s_port_decl%d.txt (banked %s)' % (MATHLIB_PIN[:8], ACT, e['n'], decl_bank), '',
         '### :%d at %s:  %s' % (e['line'], base[:8], l_old.strip()),
         '### :%d now:         %s' % (e['line'], l_new.strip()), '',
         '### the diff against %s (git diff), %d hunk(s):' % (base[:8], len(hunks))] + ['    ' + x for x in dl] + [
         '', '### the working tree (git status --short, the untracked .lp.log aside): %s' % changed,
         '', '### ### **EDIT %d: :%d TO THE FORM MATHLIB %s STATES ; HUNKS %d ; LINES CHANGED %d ; FILES CHANGED %s ; AS THE RULING ORDERS %s.**' % (
             e['n'], e['line'], MATHLIB_PIN[:8], len(hunks), nchg, changed, ok)]
    put_txt('%s_port_edit%d.txt' % (ACT, e['n']), L)
    put_json('%s_port_edit%d.json' % (ACT, e['n']), dict(at=utc(), n=e['n'], branch=br, base=base, head=head, file=K.PORT_FILE, line=e['line'], old=l_old,
                                                         new=l_new, hunks=len(hunks), diff=dl, changed=changed, ok=ok))
    print(NL.join(L[2:8] + L[-1:]))
    if not ok:
        sys.exit(1)


REGPOS_FILE = 'SIDELvConservation/RegisterPentagon.lean'
REGPOS_NAME = 'Register4_positivity'


def _decl_at(commit, path, name):
    """the declaration of <name> at <commit>:<path> by git show: from its `def`/`theorem` line to the line before the next blank line; with
    the namespaces open at its head. Returns (line, lines, namespaces)."""
    src = (g(LV, 'show', '%s:%s' % (commit, path)) or '').replace(chr(13), '').split(NL)
    i0 = next((i for i, l in enumerate(src) if re.match(r'^\s*(noncomputable\s+)?(def|theorem|abbrev)\s+%s\b' % re.escape(name), l)), None)
    if i0 is None:
        return 0, [], []
    i1 = next((i for i in range(i0, len(src)) if not src[i].strip()), len(src))
    ns = []
    for l in src[:i0]:
        m = re.match(r'^namespace\s+(\S+)', l)
        if m:
            ns.append(m.group(1))
        m = re.match(r'^end\s+(\S+)', l)
        if m and ns and ns[-1] == m.group(1):
            ns.pop()
    return i0 + 1, src[i0:i1], ns


def regpos(*a):
    """data/b712_regpos.txt (.json), (R322)(4): lv-conservation's Register4_positivity read at the deposit 93c27ec and at the port's tip, each by
    git show, its declaration printed with its line and its namespaces; EQUAL BY STATEMENT where the lines are equal character for character
    and the namespaces equal. The module's diff between the two commits printed beside it (git diff --stat and the hunks of the file)."""
    tip = g(LV, 'rev-parse', K.PORT_BRANCH).strip()
    l0, d0, n0 = _decl_at(K.LV_V0100, REGPOS_FILE, REGPOS_NAME)
    l1, d1, n1 = _decl_at(tip, REGPOS_FILE, REGPOS_NAME)
    eq = bool(d0) and d0 == d1 and n0 == n1
    fd = subprocess.run(['git', '-C', LV, 'diff', K.LV_V0100, tip, '--', REGPOS_FILE], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL)
    fdl = fd.split(NL) if fd else []
    L = ['%s -- COMPONENT 2, (R322)(4): lv-conservation`S %s AT THE DEPOSIT AND AT THE PORT`S TIP, BY STATEMENT (%s)' % (ACT, REGPOS_NAME, utc()), '',
         '### at the deposit v0.10.0 = %s: %s :%d, namespaces %s' % (K.LV_V0100[:8], REGPOS_FILE, l0, '.'.join(n0) or 'NONE')] + ['    ' + x for x in d0] + [
         '### at the port`s tip %s (port-b707): %s :%d, namespaces %s' % (tip[:8], REGPOS_FILE, l1, '.'.join(n1) or 'NONE')] + ['    ' + x for x in d1] + [
         '', '### the module %s between the two commits (git diff), %d lines:' % (REGPOS_FILE, len(fdl))] + (['    ' + x for x in fdl] or ['    (unchanged)']) + [
         '', '### ### **%s: LINES %d AND %d ; DECLARATION LINES %d AND %d ; NAMESPACES %s AND %s ; EQUAL BY STATEMENT %s.**' % (
             REGPOS_NAME, l0, l1, len(d0), len(d1), '.'.join(n0), '.'.join(n1), eq)]
    put_txt('%s_regpos.txt' % ACT, L)
    put_json('%s_regpos.json' % ACT, dict(at=utc(), deposit=K.LV_V0100, tip=tip, line_deposit=l0, line_tip=l1, decl_deposit=d0, decl_tip=d1,
                                          ns_deposit=n0, ns_tip=n1, equal=eq, file_diff_lines=len(fdl)))
    print(NL.join(L))
    if not eq:
        sys.exit(1)


def joingrade(*a):
    """data/b712_join_grade.txt (.json), (R322)(4): faces_join graded against lv-conservation's own declaration -- its statement printed from
    FacesJoin.lean at the built ref (git show), the lakefile's lv-conservation pin read at that ref, Register4_positivity's declaration from
    data/b712_regpos.json, the run's row (data/b712_runner_SIDE-faces-join_join.txt) and its #print axioms (data/b712_axioms_SIDE-faces-join_join.txt);
    DERIVES where the run's gate reads DERIVES, the statement names RegisterPentagon.Register4_positivity, the pin is the port's tip and the
    declaration equal by statement."""
    ref = g(K.JOIN_DIR, 'rev-parse', 'HEAD').strip()
    fj = (g(K.JOIN_DIR, 'show', '%s:FacesJoin.lean' % ref) or '').replace(chr(13), '').split(NL)
    i0 = next((i for i, l in enumerate(fj) if l.startswith('theorem faces_join')), None)
    stmt = fj[i0:i0 + 5] if i0 is not None else []
    lk = (g(K.JOIN_DIR, 'show', '%s:lakefile.toml' % ref) or '').replace(chr(13), '')
    m = re.search(r'name = "sideLvConservation"\s*\ngit = "[^"]+"\s*\nrev = "([0-9a-f]{40})"', lk)
    pin = m.group(1) if m else ''
    tip = g(LV, 'rev-parse', K.PORT_BRANCH).strip()
    rp = jl('%s_regpos.json' % ACT)
    run = rd(os.path.join(D, '%s_runner_SIDE-faces-join_join.txt' % ACT))
    ax = rd(os.path.join(D, '%s_axioms_SIDE-faces-join_join.txt' % ACT)).rstrip(NL)
    gate = re.search(r'GATE (DERIVES|NOT DERIVES)\.\*\*', run)
    rid = re.search(r'### the run: id (\d+)', run)
    names_lv = any('SIDELvConservation.RegisterPentagon.Register4_positivity' in l for l in stmt)
    ok = bool(gate) and gate.group(1) == 'DERIVES' and names_lv and pin == tip and rp.get('equal') is True
    L = ['%s -- COMPONENT 2, (R322)(4): faces_join GRADED AGAINST lv-conservation`S OWN DECLARATION (%s)' % (ACT, utc()), '',
         '### the built ref: SIDE-faces-join main %s ; the run %s (data/%s_runner_SIDE-faces-join_join.txt)' % (ref[:8], rid.group(1) if rid else '### UNREAD', ACT),
         '### the lakefile at the ref requires SIDE-lv-conservation at %s ; the port`s tip %s ; equal %s (the run`s log does not print the revision Lake resolved;'
         % (pin[:8], tip[:8], pin == tip),
         '###   the pin is read from the lakefile the runner checked out at the ref)',
         '### the statement (FacesJoin.lean at %s :%d):' % (ref[:8], (i0 or -1) + 1)] + ['    ' + x for x in stmt] + [
         '### lv-conservation`s own declaration, at the deposit and at the port`s tip (data/%s_regpos.txt), EQUAL BY STATEMENT %s:' % (ACT, rp.get('equal'))] + [
         '    ' + x for x in rp.get('decl_tip') or []] + [
         '### #print axioms (data/%s_axioms_SIDE-faces-join_join.txt):' % ACT] + ['    ' + x for x in ax.split(NL)] + [
         '', '### ### **faces_join: GATE %s ; NAMES lv-conservation`S RegisterPentagon.Register4_positivity %s ; THE PIN THE PORT`S TIP %s ; GRADE %s.**' % (
             gate.group(1) if gate else '### UNREAD', names_lv, pin == tip, 'DERIVES AT THE STANDARD THREE' if ok else 'NOT DERIVES')]
    put_txt('%s_join_grade.txt' % ACT, L)
    put_json('%s_join_grade.json' % ACT, dict(at=utc(), ref=ref, run_id=int(rid.group(1)) if rid else None, pin=pin, tip=tip, statement=stmt, names_lv=names_lv,
                                              regpos_equal=rp.get('equal'), axioms=ax.split(NL), grade='DERIVES' if ok else 'NOT DERIVES'))
    print(NL.join(L))
    if not ok:
        sys.exit(1)


def jointag(*a):
    """data/b712_join_tag.txt (.json), (R322)(4): SIDE-faces-join's tag v0.1.0 read back -- the tag object and its peel locally, the remote's
    tag ref and its peel by one ls-remote; the peel against the graded ref (data/b712_join_grade.json). Reads only; the tag was made by
    tools/push_gated.sh after main read back."""
    jg = jl('%s_join_grade.json' % ACT)
    obj = g(K.JOIN_DIR, 'rev-parse', 'v0.1.0').strip()
    peel = g(K.JOIN_DIR, 'rev-parse', 'v0.1.0^{commit}').strip()
    rem = [l.split() for l in g(K.JOIN_DIR, 'ls-remote', '--tags', 'origin', 'v0.1.0*').split(NL) if l.strip()]
    r_obj = next((h for h, r in rem if r == 'refs/tags/v0.1.0'), '')
    r_peel = next((h for h, r in rem if r == 'refs/tags/v0.1.0^{}'), '')
    ok = bool(peel) and peel == r_peel == jg.get('ref') and obj == r_obj and jg.get('grade') == 'DERIVES'
    L = ['%s -- COMPONENT 2, (R322)(4): SIDE-faces-join TAGGED v0.1.0 ON DERIVES, THE PEELED SHA READ BACK (%s)' % (ACT, utc()), '',
         '### the grade: data/%s_join_grade.txt, %s at %s' % (ACT, jg.get('grade'), (jg.get('ref') or '')[:8]),
         '### local: the tag object %s ; peeled %s' % (obj, peel),
         '### the remote (ls-remote --tags origin): the tag object %s ; peeled %s' % (r_obj or '### ABSENT', r_peel or '### ABSENT'),
         '', '### ### **v0.1.0: PEELED LOCAL %s REMOTE %s ; THE GRADED REF %s ; EQUAL %s.**' % (peel[:8], r_peel[:8], (jg.get('ref') or '')[:8], ok)]
    put_txt('%s_join_tag.txt' % ACT, L)
    put_json('%s_join_tag.json' % ACT, dict(at=utc(), tag='v0.1.0', object=obj, peeled=peel, remote_object=r_obj, remote_peeled=r_peel, ok=ok))
    print(NL.join(L))
    if not ok:
        sys.exit(1)


def _portedit_b711(*a):
    """b711's portedit (:212), carried as read; pruned before the seal."""
    base = K.PORT_TIP
    head = g(LV, 'rev-parse', 'HEAD').strip()
    br = g(LV, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    src = (rd(os.path.join(LV, *K.PORT_FILE.split('/'))) or '').replace(chr(13), '').split(NL)
    old = (g(LV, 'show', '%s:%s' % (base, K.PORT_FILE)) or '').replace(chr(13), '').split(NL)
    form = (rd(os.path.join(LV, *FORM_FILE.split('/'))) or '').replace(chr(13), '').split(NL)
    d = subprocess.run(['git', '-C', LV, 'diff', base, '--', K.PORT_FILE], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL)
    dl = d.split(NL) if d else []
    hunks = [l for l in dl if l.startswith('@@')]
    changed = [l for l in (g(LV, 'status', '--short') or '').split(NL) if l.strip() and not l.endswith('.lp.log')]
    n = K.PORT_LINE - 1
    l_old, l_new = old[n] if len(old) > n else '', src[n] if len(src) > n else ''
    l_form = form[FORM_LINE - 1] if len(form) >= FORM_LINE else ''
    nchg = sum(1 for i in range(min(len(src), len(old))) if src[i] != old[i])
    ok = (l_old == OLD212 and l_new == NEW212 and l_form.replace('hurwitzEvenFEPair 0', 'hurwitzEvenFEPair a') == NEW212 and len(hunks) == 1
          and changed == [' M ' + K.PORT_FILE] and head == base and br == K.PORT_BRANCH and len(old) == len(src) and nchg == 1)
    L = ['%s -- COMPONENT 2, (R322)(4): THE PORT`S LINE :%d ON %s, PRINTED BEFORE THE ONE COMMIT (%s)' % (ACT, K.PORT_LINE, K.PORT_BRANCH, utc()), '',
         '### the branch %s checked out at %s (b709`s one commit, the base), HEAD unmoved before the commit; the one module %s edited by the Edit tool' % (br, head[:8], K.PORT_FILE),
         '### at one line, the line b709`s run names first (data/b709_port.txt :11, :21: "Application type mismatch", a changed signature).', '',
         '### :%d at %s:  %s' % (K.PORT_LINE, base[:8], l_old.strip()),
         '### :%d now:         %s' % (K.PORT_LINE, l_new.strip()),
         '###   the signature (data/b709_port.txt :40-:47): WeakFEPair.hasMellin (hurwitzEvenFEPair a).toStrongFEPair w -- the argument w : ℂ where',
         '###   `(hurwitzEvenFEPair a).toStrongFEPair.k < re ?m` is expected; the strong pair`s hasMellin takes `s` alone, its instance given by',
         '###   WeakFEPair.isStrongFEPair_toStrongFEPair -- b709`s form at %s :%d:  %s' % (FORM_FILE, FORM_LINE, l_form.strip()),
         '###   beside it b709`s second error at :212:6 (a heartbeat timeout at isDefEq, data/b709_port.txt :12) is read at the dispatch, not pre-judged.', '',
         '### the diff against %s (git diff), %d hunk(s):' % (base[:8], len(hunks))] + ['    ' + x for x in dl] + [
         '', '### the working tree (git status --short, the untracked .lp.log aside): %s' % changed,
         '', '### ### **:%d EDITED TO THE STRONG PAIR`S hasMellin (b709`S FORM AT %s :%d) ; HUNKS %d ; LINES CHANGED %d ; FILES CHANGED %s ; AS THE RULING ORDERS %s.**' % (
             K.PORT_LINE, FORM_FILE.split('/')[-1], FORM_LINE, len(hunks), nchg, changed, ok)]
    put_txt('%s_port_edit.txt' % ACT, L)
    put_json('%s_port_edit.json' % ACT, dict(at=utc(), branch=br, base=base, head=head, file=K.PORT_FILE, line=K.PORT_LINE, old=l_old, new=l_new,
                                              form=dict(file=FORM_FILE, line=FORM_LINE, text=l_form), hunks=len(hunks), diff=dl, changed=changed, ok=ok))
    print(NL.join(L[5:10] + L[-1:]))
    if not ok:
        sys.exit(1)


def portdispatch(*a):
    """`portdispatch <label> <target> [dry]`: b709's form -- the workflow run AT THE BRANCH with the ref input the branch's tip, one dispatch per
    tree state (refused where data/b712_dispatches.json carries the tree), at most two dispatches this act ((R322) N1), the branch's tip read back
    at the remote by one ls-remote before the dispatch; the host's free memory printed before it and the hold read ((R322)(8))."""
    label, target = a[0], a[1]
    repo = 'psinary-sketch/' + K.KERNEL
    full = g(LV, 'rev-parse', K.PORT_BRANCH).strip()
    tree = g(LV, 'rev-parse', full + '^{tree}').strip()
    j = jl('%s_dispatches.json' % ACT) if os.path.isfile(os.path.join(D, '%s_dispatches.json' % ACT)) else {}
    rows = j.get('rows') or []
    seen = [r for r in rows if r.get('tree') == tree]
    if seen:
        sys.exit('### THE TREE %s IS ALREADY BUILT (run %s) -- NOT DISPATCHED' % (tree[:12], seen[0].get('run_id')))
    if len([r for r in rows if r.get('label') == 'port']) >= K.MAX_PORT_DISPATCHES and label == 'port':
        sys.exit('### %d PORT DISPATCHES ALREADY MADE THIS ACT ((R322)(4)) -- NOT DISPATCHED' % K.MAX_PORT_DISPATCHES)
    if len(rows) >= K.MAX_DISPATCHES:
        sys.exit('### %d DISPATCHES ALREADY MADE THIS ACT ((R322) N1) -- NOT DISPATCHED' % K.MAX_DISPATCHES)
    if not re.match(r'^[A-Za-z0-9_. ]+$', target):
        sys.exit('### THE TARGET %r IS OUTSIDE THE LAKE GRAMMAR -- NOT DISPATCHED' % target)
    remote = (g(LV, 'ls-remote', 'origin', 'refs/heads/' + K.PORT_BRANCH).split() or [''])[0]
    import b712_tests as TT
    free = TT.mem('the dispatch')
    print('  kernel %s ; branch %s ; tip %s ; the remote`s tip %s ; equal %s ; tree %s ; target %s' % (K.KERNEL, K.PORT_BRANCH, full, remote, remote == full, tree, target))
    if remote != full:
        sys.exit('### THE REMOTE`S %s IS NOT THE LOCAL TIP -- NOT DISPATCHED' % K.PORT_BRANCH)
    if free < K.HOLD:
        sys.exit('### FREE MEMORY %d MB BENEATH THE HOLD -- NOT DISPATCHED' % free)
    if 'dry' in a[2:]:
        return
    t0 = utc()
    rc, out, err = R._gh('workflow', 'run', 'build-module.yml', '-R', repo, '--ref', K.PORT_BRANCH, '-f', 'ref=' + full, '-f', 'target=' + target)
    if rc != 0:
        sys.exit('### THE DISPATCH REFUSED: %s' % err[-400:])
    run_id = None
    for _i in range(12):
        time.sleep(5)
        rc, out, err = R._gh('run', 'list', '-R', repo, '--workflow', 'build-module.yml', '--event', 'workflow_dispatch', '--limit', '5', '--json', 'databaseId,createdAt,status')
        new = [r for r in json.loads(out or b'[]') if r.get('createdAt', '') >= t0]
        if new:
            run_id = sorted(new, key=lambda r: r['createdAt'])[-1]['databaseId']
            break
    rows.append(dict(kernel=K.KERNEL, label=label, ref=full, tree=tree, target=target, dispatched=t0, run_id=run_id, whole=False, branch=K.PORT_BRANCH, free_mb=free,
                     print_list='ABSENT at the branch`s tree -- the print step read as not run, no grade claimed (b707`s reading, W-ORD-LV-FORWARD-PORT)'))
    put_json('%s_dispatches.json' % ACT, dict(rows=rows))
    print('  dispatched %s at --ref %s ; run id %s' % (t0, K.PORT_BRANCH, run_id))


def _kind(line):
    """b709's kinds of a failing line, read from its error text."""
    if 'Application type mismatch' in line or 'type mismatch' in line:
        return 'a changed signature'
    if 'unknown constant' in line or 'unknown identifier' in line or 'Unknown identifier' in line:
        return 'a cascade of an earlier failure (the kernel`s own declaration)' if 'SIDELvConservation.' in line else 'a renamed Mathlib declaration'
    if 'timeout' in line:
        return 'a heartbeat timeout (a proof grown costlier at the pin)'
    return 'a broken proof'


def portrun(*a):
    """`portrun <run id> <label>`: b709's form -- the run read by its id, its artifact by name with the sha256 against the platform's digest
    before any reading, the build's exit, the memory log, the error lines; THE OUTCOME BY FILE AND LINE: the modules built of 12, the module
    held, the next failing line with its error and its kind, the count remaining; where the build completes, the join named for this act's
    (R322)(4). data/b712_port.txt (.json)."""
    import io as _io
    import zipfile
    run_id, label = int(a[0]), a[1]
    repo = 'psinary-sketch/' + K.KERNEL
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    art, arts = _artifact_named(repo, run_id, 'build-module-')
    art = art or {}
    T_ = {}
    sha = digest = None
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        if digest and digest == sha:
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for nm in z.namelist():
                    T_[nm] = z.read(nm).decode('utf-8', 'replace').replace(chr(13), '')
    agree = bool(art) and bool(digest) and digest == sha
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    mem_low = int(low[-1]) if low else None
    stopped = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    bexit = T_.get('build_exit.txt', '').strip() or None
    errors = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    built = sorted(set(m.group(1) for m in re.finditer(r'^[✔⚠] \[\d+/\d+\] Built SIDELvConservation\.(\w+)', blog, re.M)))
    held = [m.group(1) for m in re.finditer(r'^✖ \[\d+/\d+\] Building SIDELvConservation\.(\w+)', blog, re.M)]
    file_errs = [l for l in blog.split(NL) if re.match(r'^error: SIDELvConservation/\w+\.lean:\d+:\d+:', l)]
    first_err = file_errs[0] if file_errs else None
    kinds = [(l, _kind(l)) for l in file_errs[:12]]
    remaining = [m for m in LV_MODULES if m not in built]
    cache = T_.get('cache.log', '')
    ref_built = ' '.join(T_.get('ref.txt', '').split())
    complete = bool(agree) and bexit == '0' and not remaining
    row = dict(kernel=K.KERNEL, label=label, ref=run.get('headSha') or '', run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=sha if agree else None,
               mem_low=mem_low, stopped=stopped, build_exit=bexit, errors=errors, axioms_sha256=None, gate='NOT DERIVES',
               note='no grade claimed on the port: the print step read as not run (print_targets.txt absent at the branch), W-ORD-LV-FORWARD-PORT')
    L = ['%s -- COMPONENT 2, (R322)(4): THE PORT RUN OF SIDE-lv-conservation ON %s AT ITS NEW TIP, READ BY ITS RUN ID; THE OUTCOME BY FILE AND LINE (%s)' % (ACT, K.PORT_BRANCH, utc()), '',
         '### the dispatch: the branch %s at its tip (this act`s edit on b711`s %s), the workflow at the branch, target SIDELvConservation (data/b712_dispatches.json)' % (K.PORT_BRANCH, K.PORT_TIP[:8]),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'), run.get('updatedAt')),
         '### the artifacts listed %d: %s ; the run`s own chosen by name (build-module-)' % (len(arts), [x.get('name') for x in arts]),
         '### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
             art.get('id'), art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN', 'AGREE' if agree else '### NOTHING READ FROM IT'),
         '### the ref built (out/ref.txt): %s' % (ref_built or '### UNREAD'),
         '### the cache (out/cache.log, last line): %s' % ' | '.join(l for l in cache.rstrip(NL).split(NL)[-1:] if l)[:300],
         '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (mem_low, K.HOLD, stopped),
         '### the build: exit %s ; error lines %d:' % (bexit, len(errors))] + ['    ' + l for l in errors[:40]]
    L += ['### THE OUTCOME BY FILE AND LINE: modules built %d of %d: %s' % (len(built), len(LV_MODULES), built),
          '### the module held: %s' % (held or 'NONE'),
          '### THE NEXT FAILING LINE, its error and its kind: %s' % ((' ; '.join('%s -- %s' % (l, k) for l, k in kinds[:1])) if kinds else 'NONE (no file error line)'),
          '### the failing lines after it (error, kind): %s' % ([(l[:90], k) for l, k in kinds[1:]] or 'NONE'),
          '### the count remaining (not built by this run): %d %s' % (len(remaining), remaining),
          '### the files: built %d of 15 (the 12 modules, with %s beside them, not built by the target SIDELvConservation)' % (len(built), ', '.join(LV_OTHER_LEAN)),
          '### where the build completes: %s' % ('THE BUILD COMPLETES, 12 of 12 -- (R322)(4): Register4_positivity read at 93c27ec and at the tip, the join`s lakefile re-pinned, one join dispatch'
                                                  if complete else 'not complete at this run; (R322)(4)`s join not reached, its dispatch not made'),
          '### the lines after the held module (the log`s context, up to 24 lines):']
    if held:
        i0 = next((i for i, l in enumerate(blog.split(NL)) if ('Building SIDELvConservation.%s' % held[0]) in l), 0)
        L += ['    ' + l[:200] for l in blog.split(NL)[i0:i0 + 24]]
    else:
        L += ['    ' + l[:200] for l in blog.rstrip(NL).split(NL)[-12:]]
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; MODULES BUILT %d OF 12 (FILES %d OF 15) ; THE NEXT FAILING LINE %s (%s) ; '
              'REMAINING %d ; NO GRADE CLAIMED ON THE PORT%s.**' % (
                  run_id, label, run.get('conclusion'), 'AGREE' if agree else '### UNREAD', bexit, len(errors), len(built), len(built),
                  (first_err.split(': ')[1] if first_err else 'NONE'), (kinds[0][1] if kinds else '-'), len(remaining), ' ; THE BUILD COMPLETES, THE JOIN NEXT' if complete else '')]
    R.read_runner_row(row)
    # ### (R322)(4): up to three port runs, each its own bank by its label (port1, port2, port3); data/b712_port.txt carries them all, in order
    put_txt('%s_port_%s.txt' % (ACT, label), L)
    runs = sorted(f for f in os.listdir(D) if re.match(r'^%s_port_port\d\.txt$' % ACT, f))
    allL = ['%s -- COMPONENT 2, (R322)(4): THE PORT`S RUNS, EACH READ BY ITS RUN ID, EACH HELD LINE BY FILE AND LINE (%s) ; RUNS %d of at most %d' % (
        ACT, utc(), len(runs), K.MAX_PORT_DISPATCHES), '']
    for f in runs:
        allL += ['### ======== data/%s' % f] + rd(os.path.join(D, f)).rstrip(NL).split(NL) + ['']
    put_txt('%s_port.txt' % ACT, allL)
    if agree:
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, K.KERNEL, label), blog.rstrip(NL).split(NL))
    put_json('%s_port_%s.json' % (ACT, label), dict(at=utc(), run_id=run_id, label=label, ref=run.get('headSha'), built=built, held=held, first_error=first_err,
                                                    kinds=kinds, remaining=remaining, complete=complete, artifact_sha256=sha, agree=agree))
    put_json('%s_port.json' % ACT, dict(at=utc(), run_id=run_id, run=run, artifact=dict(id=art.get('id'), name=art.get('name'), sha256=sha, digest=digest, agree=agree), ref_built=ref_built,
                                        mem_low=mem_low, stopped=stopped, build_exit=bexit, errors=errors, built=built, held=held, first_error=first_err, kinds=kinds, remaining=remaining,
                                        modules=list(LV_MODULES), grade_claimed=False, complete=complete))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (K.KERNEL, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[2:10] + L[-1:]))


# ================================================================================ COMPONENT 6: THE SCORES (b686's order), THE RECORD, THE TRAIL, THE DRY RUN, THE MIRROR
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
_sv, scores_line = R._sv, R.scores_line
_calls, _rl_lines = R._calls, R._rl_lines
num_word = P3.num_word
_trail_resolved = P3._trail_resolved
ALLOWED_SHARED_DATA = ('act_roots.txt', 'b711_closing_push_out.txt', 'b675_corrigenda.txt', 'standing_clauses_v3.txt')
def _s_scores():
    return dict((k, (v[0], v[1].replace('b698_', ACT + '_'))) for k, v in R._s_scores().items())


def _bfig(name, pat, what):
    """a figure read from this act's bank by its pattern; the composition refuses where the bank does not carry it."""
    m = re.search(pat, rdn(name))
    if not m:
        sys.exit('### data/%s DOES NOT CARRY %s (%s) -- NOTHING COMPOSED' % (name, what, pat))
    return m.groups()


def _genus_ok(gc):
    """the genus control as its bank reads (data/b712_genus_control.json): no miss through n_max, the hand rows read, both planted copies missing."""
    return gc.get('misses') == [] and gc.get('hand') is True and (gc.get('planted_form_misses') or 0) > 0 and (gc.get('planted_sign_misses') or 0) > 0


def _figs():
    """every figure the entry, the trail and the components print, read from b712's JSON banks (standing clauses v2 row (54): arms and composers
    read structure); nothing typed."""
    co = jl('%s_corrigendum.json' % ACT)
    rl = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    pj, p1 = jl('%s_port.json' % ACT), jl('%s_port_port1.json' % ACT)
    fe1 = re.match(r'^error: SIDELvConservation/(\w+\.lean):(\d+):(\d+): (.*)$', p1.get('first_error') or '')
    jg, jt, rp = jl('%s_join_grade.json' % ACT), jl('%s_join_tag.json' % ACT), jl('%s_regpos.json' % ACT)
    pr, cj, cu = jl('%s_price.json' % ACT), jl('%s_recut_compile.json' % ACT), jl('%s_recut_cut.json' % ACT)
    qj = jl('%s_recut_quote.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    gc = jl('%s_genus_control.json' % ACT)
    sc = jl('%s_standing_control.json' % ACT)
    rc = jl('%s_repair_controls.json' % ACT)
    fj_, f10 = jl('%s_standing_figures.json' % ACT), jl('b711_standing_figures.json')
    fl = (_show(PP, K.C3_PP, 'FACES_LEDGER.md') or '').replace('\r', '').split(NL)
    ax = (jg.get('axioms') or [''])[0]
    return dict(weight=rl[0], corr_line=co.get('entry_line', '-'), corr_row=co.get('row'),
                built=len(pj.get('built') or []), mods=len(pj.get('modules') or []), run=pj.get('run_id'), art=((pj.get('artifact') or {}).get('sha256') or '')[:16],
                agree=(pj.get('artifact') or {}).get('agree'), run1=p1.get('run_id'),
                e1=('%s :%s:%s' % (fe1.group(1), fe1.group(2), fe1.group(3))) if fe1 else '-',
                disp=len(dj), disp_port=sum(1 for r in dj if r.get('label') == 'port'), disp_join=sum(1 for r in dj if r.get('label') == 'join'),
                grade=jg.get('grade'), j_run=jg.get('run_id'), j_names=jg.get('names_lv'), three=ax.endswith('[propext, Classical.choice, Quot.sound]'),
                j_stmt=' '.join(x.strip() for x in (jg.get('statement') or [])[:3]), tag=jt.get('tag'), tag_obj=(jt.get('object') or '')[:8],
                tag_peel=(jt.get('peeled') or '')[:8], tag_ok=jt.get('ok'), rp_eq=rp.get('equal'), rp_line=rp.get('line_tip'),
                face_line=next((i for i, l in enumerate(fl, 1) if l.startswith('## UPDATE') and '(b712)' in l), '-'),
                t1='%.2f' % (pr.get('t1') or 0), t2='%.2f' % (pr.get('t2') or 0), budget='%.1f' % (pr.get('budget') or 0), cut=pr.get('cut'),
                g_ok=_genus_ok(gc), pins=len(cj.get('pins') or []), pins_ok=sum(1 for p_ in cj.get('pins') or [] if p_.get('stands')),
                d_before=cu.get('before'), d_after=cu.get('after'), lost=cu.get('matches_lost') or [], residues=len(qj.get('quoting') or []),
                held=', '.join(':%d' % x for x in sorted(set(cu.get('held') or []))),
                std_ok=sc.get('ok'), std_n=sc.get('n'), ctl_n=len(rc.get('cases') or []), ctl_not=rc.get('not_as_wanted'),
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                figs10=dict((k, (f10.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')))


def _artifacts_read():
    """each dispatch of the dispatch bank paired with its run bank: (label, run id, artifact sha256, agreeing) -- the port's per-label banks
    (data/b712_port_port1.json, data/b712_port.json) and the join's runner bank (data/b712_runner_SIDE-faces-join_join.txt, its artifact row)."""
    out = []
    p1, p2 = jl('%s_port_port1.json' % ACT), jl('%s_port.json' % ACT)
    jr = rdn('%s_runner_SIDE-faces-join_join.txt' % ACT)
    m = re.search(r'(?m)^### the artifact: id \d+ ; \S+ ; \d+ bytes ; sha256 ([0-9a-f]{64})', jr)
    for r in jl('%s_dispatches.json' % ACT).get('rows') or []:
        rid = r.get('run_id')
        if r.get('label') == 'port' and rid == p1.get('run_id'):
            out.append(('port', rid, p1.get('artifact_sha256'), p1.get('agree') is True))
        elif r.get('label') == 'port' and rid == p2.get('run_id'):
            out.append(('port', rid, (p2.get('artifact') or {}).get('sha256'), (p2.get('artifact') or {}).get('agree') is True))
        elif r.get('label') == 'join':
            out.append(('join', rid, m.group(1) if m else None, bool(m) and 'ARTIFACT AGREE' in jr and str(rid) in jr))
        else:
            out.append((r.get('label'), rid, None, False))
    return out


def _n1():
    """N1 (R322): no lean process runs on this host; at most four runner dispatches, up to three for the port and one for the join, each read by
    its run id with its artifact's sha256 verified. From the command bank, the dispatch bank and each run's bank."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    seat_lean = cm.get('local_lean') if cm else None
    disp = (cm.get('dispatches') or []) if cm else ['unread']
    arts = _artifacts_read()
    n_port, n_join = sum(1 for a_ in arts if a_[0] == 'port'), sum(1 for a_ in arts if a_[0] == 'join')
    read_ok = len(arts) == len(dj) and all(a_[2] and a_[3] for a_ in arts)
    ok = bool(cm) and not seat_lean and len(dj) <= K.MAX_DISPATCHES and n_port <= K.MAX_PORT_DISPATCHES and n_join <= 1 and len(disp) == len(dj) and read_ok
    return ('HELD' if ok else 'REFUTED'), (
        'the seat`s commands running lean or lake on this host (relay data/b712_commands.json): %s; runner dispatches banked %d of at most four, the '
        'port`s %d of at most three and the join`s %d of at most one (relay data/b712_dispatches.json), in the capture %d; each run read by its id with '
        'its artifact`s sha256 agreeing: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(dj), n_port, n_join, len(disp),
            '; '.join('%s %s %s… %s' % (a_[0], a_[1], (a_[2] or '-')[:16], a_[3]) for a_ in arts) or 'NONE'))


def _n2():
    """N2 (R322): the join states lv-conservation's own Register4_positivity, its statement read equal at 93c27ec and at the port's tip; its
    grade reads DERIVES at the standard three, or the join holds with the error banked by line. From the join's grade, tag and regpos banks
    and the kernel's refs read live."""
    jg, rp, jt = jl('%s_join_grade.json' % ACT), jl('%s_regpos.json' % ACT), jl('%s_join_tag.json' % ACT)
    ax = (jg.get('axioms') or [''])[0]
    three = ax.endswith('[propext, Classical.choice, Quot.sound]')
    names_lv = jg.get('names_lv') is True and 'SIDELvConservation.RegisterPentagon.Register4_positivity' in ' '.join(jg.get('statement') or [])
    regpos = rp.get('equal') is True and rp.get('deposit') == K.LV_V0100 and rp.get('tip') == K.PORT_NEW_TIP
    pinned = jg.get('pin') == K.PORT_NEW_TIP and jg.get('ref') == K.JOIN_NEW_TIP
    peel = g(K.JOIN_DIR, 'rev-parse', '%s^{commit}' % K.JOIN_TAG[0]).strip()
    ok = names_lv and regpos and pinned and three and jg.get('grade') == 'DERIVES' and jt.get('ok') is True and peel == K.JOIN_TAG[2]
    return ('HELD' if ok else 'REFUTED'), (
        'faces_join names lv-conservation`s own Register4_positivity %s; that declaration read equal by statement at %s and at the port`s tip %s: %s '
        '(relay data/b712_regpos.json); the join built at %s against lv at %s (the port`s tip) %s, run %s; #print axioms %s -- the standard three %s; '
        'the grade %s (relay data/b712_join_grade.json); tag %s peeled %s, read back %s (relay data/b712_join_tag.json) -- the first form of N2' % (
            names_lv, (rp.get('deposit') or '')[:8], (rp.get('tip') or '')[:8], regpos, (jg.get('ref') or '')[:8], (jg.get('pin') or '')[:8], pinned,
            jg.get('run_id'), ax.split(':', 1)[-1].strip(), three, jg.get('grade'), K.JOIN_TAG[0], peel[:8], jt.get('ok')))


NOTHING_COMPUTED = re.compile(r'^(data/b712_(epstein|zeros|pairs|list|coeffs|axis|surgery|onset|certify)[\w.-]*|tools/b71[23]_(epstein|pairs|coeffs|list|certify)\w*\.py)$')   # ### defect (u): the bank's extension read


def _n3():
    """N3 (R322): data/b712_registrations.txt is committed ahead of every other bank of the act and nothing of the -15 control is computed. From
    the relay's log since the act's base (the first commit's files) and the tracked and working trees (no bank or tool of a -15 computation)."""
    revs = [x for x in g(ROOT, 'log', '--format=%H', '--reverse', '%s..HEAD' % K.PRE_RELAY).split(NL) if x.strip()]
    first = revs[0] if revs else ''
    ff = sorted(x for x in g(ROOT, 'show', '--name-only', '--format=', first).split(NL) if x.strip()) if first else []
    banks_first = [x for x in ff if x.startswith('data/')]
    alone = first[:8] == K.REG_COMMIT[:8] and K.REGISTRATIONS in ff and all(x in (K.REGISTRATIONS, 'data/b712_genus_control.txt', 'data/b712_genus_control.json')
                                                                             for x in banks_first)
    tracked = [x for x in g(ROOT, 'ls-files').split(NL) if x.strip()]
    untracked = [x for x in g(ROOT, 'ls-files', '--others', '--exclude-standard').split(NL) if x.strip()]
    computed = sorted(x for x in tracked + untracked if NOTHING_COMPUTED.match(x))
    gc = jl('%s_genus_control.json' % ACT)
    ok = alone and not computed
    return ('HELD' if ok else 'REFUTED'), (
        'the act`s first relay commit %s is the registrations` %s, its banks %s, the genus control banked beside the row as the author`s word at the first '
        'prompt ordered (its control %s through n = %s, an identity between Dirichlet coefficients, no zero); a bank or tool of a -15 computation '
        'tracked or in the working tree: %s' % (first[:8], K.REG_COMMIT[:8], banks_first, _genus_ok(gc), gc.get('n_max'), computed or 'NONE'))


def _n4():
    """N4: the trail's lines equal the defects lettered before the seal; post-seal findings stand as events; no bank is written after the root.
    From the seal's record of the letters, the defects bank now and the step bank; the clauses that wait read again at `scores close`."""
    seal = letters_at_seal(ACT)
    now = letters_of(rdn('%s_defects.txt' % ACT))
    late = [s[:3] for s in now if seal is not None and _letter(s) not in set(_letter(x) for x in seal)]
    steps = jl('%s_steps.json' % ACT).get('rows') or []
    sj = jl('%s_seal_hashes.json' % ACT)
    sealed_at = _iso_epoch(sj.get('at') or '') if sj else None
    after = [r for r in steps if sealed_at is not None and r.get('ct', 0) > sealed_at]
    wrong = [r['commit'][:8] for r in after if r.get('phase') not in POST_SEAL_PHASES]
    ra = jl('%s_root_arm.json' % ACT)
    ev = os.path.exists(os.path.join(D, '%s_events.txt' % ACT))
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late'))
    return ('HELD' if ok else ('PENDING' if seal is None else 'REFUTED')), (
        'the letters the seal records (relay data/b712_seal_hashes.json) %d, the defects bank`s letters now %d, letters after the seal %s; the step '
        'bank`s commits after the seal (relay data/b712_steps.json) %d, each with a post-seal phase: %s; the events bank for what is found after the seal %s; '
        'no bank after the root (relay data/b712_root_arm.json) %s, read again at `scores close`' % (
            len(seal or []), len(now), late or 'NONE', len(after), not wrong, 'present' if ev else 'not written (none found)',
            ('late %s' % ra.get('late')) if ra else 'waits on the root'))


def _n5():
    import b633_record as R3
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ef_main = g(K.EF_DIR, 'rev-parse', 'main').strip()
    ef_ok = ef_main == K.EF_MAIN and not g(K.EF_DIR, 'tag', '--contains', K.EF_V037).replace('v0.37', '').strip()
    lv_main, lv_dep = g(LV, 'rev-parse', 'main').strip(), g(LV, 'rev-parse', 'v0.10.0^{commit}').strip()
    lv_port = g(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH).strip()
    lv_ok = lv_main == K.LV_MAIN and lv_dep == K.LV_V0100 and lv_port == K.PORT_NEW_TIP and not [t for t in g(LV, 'tag', '--points-at', K.PORT_NEW_TIP).split(NL) if t.strip()]
    join_main, join_tags = g(K.JOIN_DIR, 'rev-parse', 'main').strip(), g(K.JOIN_DIR, 'tag', '--list').strip()
    join_ok = join_main == K.JOIN_NEW_TIP and join_tags == K.JOIN_TAG[0]
    rc_main = g(PP, 'rev-parse', '%s:%s' % ('HEAD', K.RECUT_DOC)).strip() == g(PP, 'rev-parse', '%s:%s' % (K.PRE_PP, K.RECUT_DOC)).strip()
    rc_branch = g(PP, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.RECUT_BRANCH).strip() == K.RECUT_COMMIT
    rc_remote = g(PP, 'ls-remote', 'origin', 'refs/heads/' + K.RECUT_BRANCH).strip() == ''
    recut_ok = rc_main and rc_branch and rc_remote
    allowed = set(K.PP_WRITTEN)
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in allowed]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    ruled = set('tools/' + t for t in tuple(K.REPAIRED_TOOLS) + tuple(K.NEW_TOOLS))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b712_', x) and x[6:] not in R.N5_RELAY_TOOLS and x not in ruled]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b712_|audit_b712_)', x) or re.match(r'^data/terminal_table', x) or x in ruled
                                                or (x.startswith('data/') and x[5:] in ALLOWED_SHARED_DATA) or (x.startswith('tools/') and x[6:] in R.N5_RELAY_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B711_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE) or '') or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(LV, lock)) if lock else []
    cj = jl('%s_commands.json' % ACT)
    ob = cj.get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    chained = [d['n'] for d in (cj.get('delete_shapes') or []) if d.get('chained')]
    deleted = sorted(x for d in (cj.get('delete_shapes') or []) for x in (d.get('deletes') or []))
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl == pre_gl
    ok = k_ok and ef_ok and lv_ok and join_ok and recut_ok and not pp_beyond and not renames and not kinds_beyond and not shared_tools and not differ \
        and arms_ok and not amended and not ident and not chained and K.PORT_BRANCH not in deleted and gw_ok and gl
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits or publishes: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; SIDE-explicit-formula`s main at '
            'badaccc, no tag past v0.37, unmoved: %s; SIDE-lv-conservation`s main and deposit untouched, port-b707 at this act`s tip %s, no tag at it: %s; the join kernel`s '
            'main at %s with the one tag %s: %s; the re-cut on its branch %s at %s, not at the remote, the document unmoved on main: %s; the standing arms added beyond '
            'b711`s face, the act arms apart: %s (%s); shared tools edited beyond the membrane %s: %s; sealed tools not agreeing: %s; commits amended after the seal '
            '(relay, PLACE-papers, SIDE-lv-conservation): %s; deletes with anything chained after: %s; port-b707 deleted: %s; one git write per message (%s): %s; '
            'PLACE-papers beyond the three ledgers: %s; papers moved or renamed: %s; relay files of a kind beyond the act`s banks and tools, the table, the root list, '
            'the corrigenda bank, b711`s push-out bank, standing clauses v3, the membrane and tools/mirror_prevbuild.json: %s; the glossary unchanged: %s; outbound '
            'requests other than git and gh %d, an identifier of the author in %s; the clauses that wait (the hashes at the close, no bank after the root) read '
            'again at `scores close`' % (
                K.DRAFT, k_ok, ef_ok, K.PORT_NEW_TIP[:8], lv_ok, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0], join_ok, K.RECUT_BRANCH, K.RECUT_COMMIT[:8], recut_ok,
                added or 'NONE', arms_ok, sorted(ruled), shared_tools or 'NONE', differ or 'NONE', amended or 'NONE', chained or 'NONE', K.PORT_BRANCH in deleted,
                gw_note, gw_ok, pp_beyond or 'NONE', renames or 'NONE', kinds_beyond or 'NONE', gl, len(ob), [r['line'] for r in ident] or 'NONE'))


def TRAIL_HEAD():
    return ('### b712 — lane two, act one hundred and thirty-nine, the re-cut act under (R322): b711 at its weight; the corrigendum; the standing '
            'clauses at v3; the port and the join; the faces row; the −15 control registered and priced; the next document re-cut')


R.TRAIL_HEAD = TRAIL_HEAD


def _title():
    """the entry's title by its objects, Component 6's form ("the faces joined by closure at SIDE-faces-join <v0.1.0 | held at <line>>; the port at
    <k> of 12 modules; the -15 control registered with its price; <document> re-cut"), every figure from the banks."""
    f = _figs()
    joined = ('v0.1.0' if f['grade'] == 'DERIVES' and f['tag_ok'] else 'held at %s' % f['e1'])
    return ('## The faces joined by closure at SIDE-faces-join %s; the port at %d of %d modules; the −15 control registered with its price; '
            '%s re-cut' % (joined, f['built'], f['mods'], K.RECUT_DOC.split('/')[-1][:-3].replace('_', ' ')))


def _letters_now():
    """the letters the trail carries: those the seal records (row (52)); before the seal (a dry run) the defects bank's, by the same reader."""
    seal = letters_at_seal(ACT)
    return seal if seal is not None else _defect_short(ACT)


def _owners_now():
    rows = _letters_now()
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author():
    rows, nav = _owners_now()
    f = _figs()
    seat = len(rows) - len(nav)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) N5’s “no identifier of the author in any outbound request or workflow file” read as the requests’ headers and payloads and the '
            'workflow files, not the git identity every commit and the tag %s carry as author and tagger -- for the strike; (2) the faces ledger head’s '
            ':8 sentence (“the record states none”) no longer describing the record once the row names faces_join, a compiled equivalence; the head '
            'not edited, the row’s note naming it -- for the author’s word; (3) the re-cut alters lines above and within the Correspondence section '
            'whose header reads ADDITIVE ONLY, by the table’s actions under (R322)(7) as b708 cut Spectral_Inertness, the header not edited '
            '(W-ORD-KEYSTONE-HEADS); (4) the genus decomposition registered on the author’s word at the first prompt with no text cited, its source pin '
            'priced for b713; (5) the port’s run reading failure at its axiom step, the print list absent at the tree (b707’s reading), the build 12 of '
            '12 and no grade claimed on the port; W-ORD-LV-PORT-TAG stands, no lv tag; (6) the price’s act budget (%s h) the seat’s estimate; (7) the '
            'Correspondence cells %s of the re-cut held (b708’s form), the distance %s after the cut by them alone; (8) the report tool outside the '
            'sealed list until the root (relay data/b708_rules.txt row (1)); (9) %s and the seat’s %s defect%s as lettered' % (
                f['tag'], f['budget'], f['held'], f['d_after'],
                ('the %s navigator %s (%s)' % (num_word(len(nav)), 'miss' if len(nav) == 1 else 'misses', letters)) if nav else 'the none navigator misses',
                num_word(seat), '' if seat == 1 else 's'))


def _finding_text():
    """the FINDINGS entry, composed before the root: its head line the result sentence, the result before its conditions; its scores line from the
    scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The faces are joined by closure: faces_join, h2_sign ↔ SIDE-lv-conservation’s own Register4_positivity of the Li coefficients through RH, '
         'derives at the standard three at SIDE-faces-join %s (tag object %s, peeled %s), built on run %s against lv-conservation at the port’s tip; '
         'the forward port of SIDE-lv-conservation builds %d of %d modules at %s, the two lines repaired by the Edit tool to the form Mathlib de5ce8a9 '
         'states; the class-number-2 control at discriminant −15 is registered and priced, nothing of it computed; and %s is re-cut in keystone form '
         'on a PLACE-papers branch, its distance by the b670 method %s to %s.' % (
             f['tag'], f['tag_obj'], f['tag_peel'], f['j_run'], f['built'], f['mods'], K.PORT_NEW_TIP[:8], K.RECUT_DOC, f['d_before'], f['d_after']), '',
         '*Filed at b712 on the author’s ruling `(R322)`; %d question%s put before the root. Banks: relay `data/b712_port.txt`, `data/b712_port_edit1.txt`, '
         '`data/b712_port_edit2.txt`, `data/b712_dispatches.json`, `data/b712_regpos.txt`, `data/b712_join_grade.txt`, `data/b712_join_tag.txt`, '
         '`data/b712_registrations.txt`, `data/b712_genus_control.txt`, `data/b712_price.txt`, `data/b712_recut_compile.txt`, `data/b712_recut_quote.txt`, '
         '`data/b712_recut_cut.txt`, `data/b712_recut_diff.txt`, `data/standing_clauses_v3.txt`, `data/b712_tool_repairs.txt`, '
         '`data/b712_repair_controls.txt`, `data/b712_corrigendum.txt`, `data/b712_standing_figures.txt`, `data/b712_report.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** ((R322)(1)-(2)): b711 entered at its weight as its closing prints (FINDINGS :%s); the corrigendum generated from '
         'b711’s events by their sixteen starting lines with the item the navigator adds, at FINDINGS :%s; the corrigenda bank appended at row '
         '(%s).' % (f['weight'], f['corr_line'], f['corr_row']), '',
         '**The standing clauses and the repairs** ((R322)(3)): relay data/standing_clauses_v3.txt at VERSION 3 -- v2’s 55 rows unchanged and rows '
         '(56)-(60) the five deltas, %s rows in all, its control as wanted %s; the five repairs and the NEXT line’s, %d control cases, %s not as '
         'wanted (relay data/b712_tool_repairs.txt, data/b712_repair_controls.txt); the throughstone report carried forward as the standing report '
         'tool (relay data/b712_report.txt, its diff in data/b712_report_diff.txt).' % (f['std_n'], f['std_ok'], f['ctl_n'], f['ctl_not']), '',
         '**The port** ((R322)(4), N1): port-b707 of SIDE-lv-conservation, DirichletC7Order.lean :501 repaired to `(isStrong_hurwitzOddFEPair a).Λ_eq` '
         'at %s, its run %s held at %s; :574 repaired to the strong pair’s `hasMellin` at %s, its run %s built %d of %d modules, the artifact’s '
         'sha256 %s… agreeing %s; the run’s axiom step finding no print list at the tree, no grade claimed on the port. Two port dispatches of three.' % (
             K.PORT_EDIT1[:8], f['run1'], f['e1'], K.PORT_NEW_TIP[:8], f['run'], f['built'], f['mods'], f['art'], f['agree']), '',
         '**The join** ((R322)(4), N2): lv-conservation’s Register4_positivity read at the deposit 93c27ec and at the port’s tip, equal by statement '
         '%s (RegisterPentagon.lean :%s); SIDE-faces-join’s lakefile re-pinned to lv-conservation at %s by revision, lv’s main and deposit untouched; '
         'the one join dispatch, run %s; faces_join names lv’s own declaration %s, its #print axioms the standard three %s, the grade %s; '
         'SIDE-faces-join tagged %s, the peeled SHA %s read back %s. No lv tag; W-ORD-LV-PORT-TAG stands for the author’s word.' % (
             f['rp_eq'], f['rp_line'], K.PORT_NEW_TIP[:8], f['j_run'], f['j_names'], f['three'], f['grade'], f['tag'], f['tag_peel'], f['tag_ok']), '',
         '**The faces row** ((R322)(5)): the faces ledger’s update block at FACES_LEDGER.md :%s (PLACE-papers %s), by the Edit tool, naming the join, '
         'faces_join’s statement, its grade and the peeled SHA, every cell filled.' % (f['face_line'], K.C3_PP[:7]), '',
         '**The −15 control** ((R322)(6), N3): data/b712_registrations.txt committed alone at %s, ahead of every other bank -- the forms x²+xy+4y² and '
         '2x²+xy+2y² and the genus decomposition on the author’s word (its control as wanted %s), the refined law carried unchanged with its falsifier '
         'outside [0.99, 1.01], the coefficient observation; the price in data/b712_price.txt -- the first tier %s h, the second %s h, the seat’s '
         'estimate of the act’s budget %s h, the cut for (iii) n ≤ %s. Nothing of the −15 zeros computed.' % (
             K.REG_COMMIT[:8], f['g_ok'], f['t1'], f['t2'], f['budget'], f['cut']), '',
         '**The re-cut** ((R322)(7)): %s, the licensed table’s next document; the compile steps banked before any prose -- %d pins of %d standing at '
         'their tags, a control one line off reading false; the table’s actions applied by the Edit tool, every MATCHES quotation standing (lost %s), '
         'the Correspondence cells %s held, three sentences retired to an Errata section and the result lines placed with their pins and footings in '
         'a Placement section; %d quoting lines entered as residues; the commit %s on %s, not pushed, its diff banked.' % (
             K.RECUT_DOC, f['pins_ok'], f['pins'], f['lost'] or 'none', f['held'], f['residues'], K.RECUT_COMMIT[:7], K.RECUT_BRANCH), '',
         '**The standing arms**: the four figures at b712 -- %s, %s, %s, %s -- against b711’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b712_standing_figures.txt); no standing arm added.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the join and the re-cut read one clause from two sides -- the kernel closes h2_sign against '
         'lv-conservation’s positivity register through RH, and the re-cut document now states that clause where it stands, RH equivalent to '
         'h2_sign and not conditional on it, each result line placed at its pin. It strengthens the programme’s offering of a located clause by '
         'compiling two of its faces into one equivalence and by a document that no longer reads past them.', '',
         '**Carried to:** b713 (the research act at discriminant −15, its registrations read unchanged from %s, the source pin priced); '
         'W-ORD-LV-PORT-TAG for the author’s word; the faces ledger head’s :8 sentence for the author’s word; the draft held at v5.' % K.REG_COMMIT[:8], '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R322) ratified.** (1) b711 at its weight. (2) The corrigendum. (3) The standing clauses at v3, the five repairs, the standing report '
             'tool and the NEXT line. (4) The port at up to three dispatches and the join by closure. (5) The faces row. (6) The −15 control registered '
             'and priced. (7) The licensed table’s next document re-cut. (8) The branches and carried files. (9) The read-first bank, the citation '
             'check, the answers and the write list. (10) The draft held at v5. (11) The next act.', '',
             '**Entered:** FINDINGS.md:%s (b711’s weight), :%s (the corrigendum), :%s (the entry); FACES_LEDGER.md:%s (the faces row); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), f['face_line']), '',
             '**Act root:** b712 `%s` (previous `%s`, b711’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b712_author_answers.txt): the first at step zero (the '
             '−15 decomposition’s text, answered and checked, defect (f)) and the root’s own prompt, its answer in the closing line.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses and the repairs:** relay data/standing_clauses_v3.txt at VERSION 3, %s rows, its control as wanted %s; the five '
             'repairs and the NEXT line’s, %s control cases, %s not as wanted (relay data/b712_repair_controls.txt, data/b712_tool_repairs.txt); the '
             'standing report tool (relay data/b712_report.txt).' % (f['std_n'], f['std_ok'], f['ctl_n'], f['ctl_not']), '',
             '**The port and the join:** %d of %d modules at %s on run %s (its artifact verified), the first run %s held at %s; Register4_positivity '
             'equal by statement %s; faces_join %s at the standard three %s on run %s; SIDE-faces-join %s peeled %s; no lv tag.' % (
                 f['built'], f['mods'], K.PORT_NEW_TIP[:8], f['run'], f['run1'], f['e1'], f['rp_eq'], f['grade'], f['three'], f['j_run'], f['tag'],
                 f['tag_peel']), '',
             '**The faces row:** FACES_LEDGER.md :%s, by the Edit tool.' % f['face_line'], '',
             '**The −15 control:** registered alone at %s, priced (%s h and %s h; the seat’s act budget %s h); nothing of it computed.' % (
                 K.REG_COMMIT[:8], f['t1'], f['t2'], f['budget']), '',
             '**The re-cut:** %s on %s at %s, not pushed; the compile steps first (%d of %d pins); the distance %s to %s, the MATCHES rows lost %s, '
             'the cells %s held.' % (K.RECUT_DOC, K.RECUT_BRANCH, K.RECUT_COMMIT[:7], f['pins_ok'], f['pins'], f['d_before'], f['d_after'],
                                     f['lost'] or 'none', f['held']), '',
             '**The kernels:** port-b707 at this act’s tip %s, kept local and remote; SIDE-faces-join at %s tagged %s; SIDE-explicit-formula and '
             'SIDE-lv-conservation’s main and deposit unmoved; %d runner dispatches (%d port, %d join); no lean process on this host.' % (
                 K.PORT_NEW_TIP[:8], K.JOIN_NEW_TIP[:8], f['tag'], f['disp'], f['disp_port'], f['disp_join']), '',
             '**The mirror:** the export made after this root in the b670 form over b706’s roster, its name in the closing (relay data/b712_closing.txt).', '',
             '**The open orders:** `W-ORD-LV-FORWARD-PORT` (restated: %d of %d modules at %s, the port reached; the join derived at SIDE-faces-join %s); '
             '`W-ORD-LV-CLOSURE-JOIN` (the join made by closure, faces_join %s); `W-ORD-LV-PORT-TAG` (for the author’s word, no lv tag); '
             '`W-ORD-KEYSTONE-HEADS` (the re-cut’s title, labels and version line untouched); `W-ORD-MOVES-BY-LOCUS`; `W-ORD-ENTRY-TAG-PRINTS`; '
             '`W-ORD-EXPLICIT-FORMULA-C1`; `W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-QUASI-RH-FIELD-WATCH`; `W-ORD-P3-CONTOUR-SIGMA`; `W-ORD-E0-MET-CLASSK`; '
             '`W-ORD-README-FIGURE-SCOPE`.' % (f['built'], f['mods'], K.PORT_NEW_TIP[:8], f['tag'], f['grade']), '',
             '**The standing arms:** the four figures %s, %s, %s, %s against b711’s %s, %s, %s, %s (relay data/b712_standing_figures.txt).' % (
                 f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                 f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b712_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R322).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b712_citation_check.txt), the registrations alone (data/b712_registrations.txt, relay %s ; N3 %s), '
         'step zero (data/b712_ferry.txt, data/b712_readfirst.txt, data/b712_stepzero.txt, data/b712_tests_stepzero.txt, data/b712_rowgen_stepzero.txt, '
         'data/b712_branches.txt), standing clauses v3 (data/standing_clauses_v3.txt, relay %s)' % (K.REG_COMMIT[:8], S['N3'][0], K.STANDING_COMMIT[:8]),
         '### COMPONENT 1 : b711`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s (data/b712_corrigendum.txt, the corrigenda row (%s)) ; the repairs and '
         'their controls (data/b712_tool_repairs.txt, data/b712_repair_controls.txt)' % (f['weight'], f['corr_line'], f['corr_row']),
         '### COMPONENT 2 : the port (data/b712_port_edit1.txt, data/b712_port_edit2.txt, data/b712_dispatches.json, data/b712_port.txt): %d of %d at %s ; '
         'the join (data/b712_regpos.txt, data/b712_join_grade.txt, data/b712_join_tag.txt): %s, %s ; N1 %s ; N2 %s' % (
             f['built'], f['mods'], K.PORT_NEW_TIP[:8], f['grade'], f['tag'], S['N1'][0], S['N2'][0]),
         '### COMPONENT 3 : the faces row FACES_LEDGER.md :%s ; the price (data/b712_price.txt)' % f['face_line'],
         '### COMPONENT 4 : the re-cut of %s on %s at %s (data/b712_recut_compile.txt, data/b712_recut_quote.txt, data/b712_recut_cut.txt, '
         'data/b712_recut_diff.txt): %s -> %s' % (K.RECUT_DOC, K.RECUT_BRANCH, K.RECUT_COMMIT[:8], f['d_before'], f['d_after']),
         '### COMPONENT 5 : the figures (data/b712_standing_figures.txt), the report (data/b712_report.txt), the root route dry '
         '(data/b712_root_banks_dry.txt), the dry-run steps (data/b712_reg_gate.txt), the seal (data/b712_seal_hashes.json), the suite in seven parts, the '
         'per-part seconds (data/b712_arm_seconds.txt) ; S3 %s ; N4 %s' % (S['S3'][0], S['N4'][0]),
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def scores(*a):
    """`scores [dry]` writes data/b712_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited (N4's and N5's close clauses, S1, S2) into data/b712_scores_close.json."""
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
    through the screens their landing runs, the needles the face names read in each; the trail's Defects line AND its Resolved line read against
    the letters the trail carries (the seal's, row (52); the defects bank's before the seal). Writes no bank."""
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
            m = re.search(r'^\*\*Defects\*\* \(relay data/%s_defects\.txt\): (.*)\.$' % ACT, text, re.M)
            got = m.group(1) if m else None
            want = '; '.join(_letters_now()) or 'none'
            eq = got == want
            print('  THE TRAIL`S DEFECTS LINE: %s' % got)
            print('  THE LETTERS THE TRAIL CARRIES (the seal`s record, else relay data/%s_defects.txt by the repaired reader): %s' % (ACT, want))
            print('  ### THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK %s' % eq)
            rows, nav = _owners_now()
            gr = _trail_resolved(t)
            wr = (num_word(len(nav)), num_word(len(rows) - len(nav)))
            eqr = gr == wr
            print('  THE TRAIL`S RESOLVED LINE`S COUNTS: %s ; THE BANK`S OWNERS (navigator, seat): %s' % (gr, wr))
            print('  ### THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK %s' % eqr)
            clean = clean and eq and eqr
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


def post_seal_row(root_prompt_after_lock, other_after_lock=0):
    """(R322)(3)(i), standing clauses v3: THE FACE NAMES THE ROOT'S PROMPT BY FORM -- the face's post-seal row built from the act's order: where
    the order puts the root's prompt after the lock, the row names it (b711's face read NONE with the root's prompt after its lock, events
    :61). Pure in its arguments; the seat writes the row into the face as printed by `facerows`."""
    n = (1 if root_prompt_after_lock else 0) + other_after_lock
    if n == 0:
        return '### POST-SEAL PROMPTS NAMED: NONE'
    return '### POST-SEAL PROMPTS NAMED: %d%s' % (n, ' (the root`s prompt)' if root_prompt_after_lock and not other_after_lock else '')


def facerows(*a):
    """prints the face rows built by form ((R322)(3)(i), (ii), (v)): the post-seal row from the act's order (the root's prompt after the lock,
    (R322)(9)); every relay and PLACE-papers commit of the act's step bank but the gate's, by its 7-hex prefix, for section (0); writes nothing."""
    print(post_seal_row(True))
    rows = jl('%s_steps.json' % ACT).get('rows') or []
    for r in rows:
        if r.get('phase') in PRE_SEAL_PHASES and r.get('phase') != 'gate':
            print('  %-5s %s  %-12s %s' % (r['repo'], r['commit'][:8], r['phase'], r.get('subject', '')[:90]))


def mirror_order(act, rootl, roots=None):
    """(R322)(3)(iv), standing clauses v3: THE MIRROR'S ORDER -- with the act's root appended, the export's MANIFEST must carry the root line
    `Act root: <act> <root>` before the mirror bank is written (b711 banked once with THE ROOT LINE : ### NONE, its mroot not yet run, events
    :75). The refusal's text, or '' where the bank may be written (pure in its arguments; `roots` names a test copy of the chain)."""
    line = MEM.appended(act, roots)
    if not line:
        return ''
    want = 'Act root: %s %s' % (act, line.split()[1])
    if any(l.startswith(want) for l in rootl):
        return ''
    return ('### (R322)(3)(iv) THE MIRROR`S ORDER: %s`S ROOT IS APPENDED AND THE EXPORT`S ROOT LINE READS %s, NOT %s... -- RUN mroot, THEN mverify, '
            'THEN mbank; NOTHING WRITTEN' % (act, (rootl[0][:40] if rootl else 'NONE'), want[:40]))


def mbank(*a):
    """b711's mbank carried with b712's names (the span line read from the mirror bank chain); (R322)(3)(iv): refused where the root is
    appended and the export carries no root line for it."""
    import hashlib as _hl
    import zipfile
    import b616_record as R6
    ZIP = R.ZIP
    z = zipfile.ZipFile(ZIP)
    names_ = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    refusal = mirror_order(ACT, rootl)
    if refusal:
        sys.exit(refusal)
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names_), R6.nd_sets())[0]
    files_ = [n for n in names_ if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names_), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         span_line(ACT),
         '### THE ROSTER b711`S (tools/mirror_roster.json unedited this act); the builder`s state file tools/mirror_prevbuild.json written at this build, named in (W) ((R322)(9)); files %d' % len(files_),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names_]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names_), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT)))
    for l in L[:10]:
        print(l[:240])


def guard(*a):
    """data/b712_guard_dry.txt (.json): the suite's `--guard-dry` run in its own process (it writes nothing), its print banked verbatim; the writes
    by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read by number."""
    import b712_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b712_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b712_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b712_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b712_checks.py :%d `%s`,'
         % (k, src[k - 1].strip() if k else '?'), '### the line above the per-part seconds write at :%d.' % ((k or 0) + 1), '',
         '### THE PRINT, VERBATIM (exit %d):' % r.returncode]
    L += [x for x in r.stdout.rstrip(NL).split(NL)]
    L += ['', '### THE WRITES BY MODE, READ FROM THE SUITE`S writer_plan: %s' % '; '.join('%s %s' % (m, w or 'NONE') for m, w in writes.items()), '',
          '### ### **%s**' % ('THE GUARD HELD ; THE POST-ROOT PATH WRITES NONE OF THE PER-PART SECONDS BANKS ; THE PRE-RUN WRITES THEM ALONE'
                               if ok else '### THE GUARD IS NOT AS READ -- SEE ABOVE')]
    if 'dry' not in a:
        put_txt('%s_guard_dry.txt' % ACT, L)
        put_json('%s_guard_dry.json' % ACT, dict(at=utc(), writes=writes, guard_line=k, exit=r.returncode, ok=ok))
    print(NL.join(L))


def scorercheck(*a):
    """a print only: the suite's G-SCORER-READS-BANKS reading over this tool's own source, each clause named; writes nothing."""
    import b712_checks as CH
    src = rd(os.path.join(T, 'b712_record.py'))
    n = ''.join(CH.strip_prose(CH._fn_src(src, f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = CH.strip_prose(CH._fn_src(src, 'scores'))
    ft = CH.strip_prose(CH._fn_src(src, '_finding_text'))
    m = re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n)
    print('  n %d chars ; needles %s ; ledger needle %r at %s' % (
        len(n), dict((x, x in n) for x in ('_commands.json', '_dispatches.json', '_port.json', '_registrations_reread', '_steps.json')),
        m.group(0) if m else None, n[max(0, m.start() - 80):m.end() + 40] if m else '-'))
    print('  sc isfile %s ; ft scores_line %s ; ft jl %s' % ("os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc, 'scores_line(S)' in ft, "jl('%s_scores.json' % ACT)" in ft))


def armnames(*a):
    """the suite's arm names in its order, for the face's (G2) block -- names alone, no source printed."""
    import b712_checks as CH
    names_ = [x[0] for x in CH.ARMS]
    st = set(_standing())
    print('  ARMS %d ; standing among them %d ; the act`s %d ; beyond both %s' % (
        len(names_), len(st & set(names_)), len(set(names_) & set(K.ACT_ARMS)), sorted(set(names_) - st - set(K.ACT_ARMS)) or 'NONE'))
    print('  standing not in the suite: %s' % (sorted(st - set(names_)) or 'NONE'))
    print('  act arms not in the suite: %s' % (sorted(set(K.ACT_ARMS) - set(names_)) or 'NONE'))
    for i in range(0, len(names_), 7):
        print('### ' + ' '.join('`%s`' % n for n in names_[i:i + 7]))
    for i in range(0, len(names_), 7):
        print('### ' + ' '.join('`%s`' % n for n in names_[i:i + 7]))


# ================================================================================ COMPONENT 1: (R322)(3)'S FIVE REPAIRS AND THE NEXT LINE, THEIR CONTROLS
def _b711_logs():
    """b711's relay and PLACE-papers commits as its step bank records them: [(hash, subject, epoch)]."""
    return [(r['commit'], r.get('subject', ''), int(r['ct'])) for r in jl('b711_steps.json').get('rows') or []]


def _count_pipes(text):
    try:
        return len(json.loads(text).get('any_pipes') or [])
    except Exception:
        return None


def repairctl12(*a):
    """data/b712_repair_controls.txt (.json), Component 1, (R322)(3): each of the five repairs and the NEXT line's repair run on b711's banks,
    each with the control the ruling names and a NEG case; every reading printed beside its case. The repaired forms are read where they
    stand: tools/b712_checks.py (post_seal_named, answers_bank_ok, nothing_ahead_ok), tools/b712_record.py (post_seal_row, mirror_order),
    tools/b712_closing.py (head_line, state_file_sentence), tools/b712_regspec.py (refresh_commands), tools/b712_worklist.py (orders_naming)."""
    import shutil
    import b712_checks as CK
    import b712_closing as CL
    import b711_checks as CK7
    rows, notes = [], []

    def case(sec, name, got, want, note=''):
        rows.append(dict(section=sec, case=name, got=got, wanted=want, as_wanted=got == want, note=note))

    lock = CK.iso_epoch(jl('b711_seal_hashes.json')['lock'])
    face7 = rdn('b711_registration_2026-10-25.txt')
    a7, aj7 = rdn('b711_author_answers.txt'), jl('b711_author_answers.json')
    # ---------------------------------------------------------------- (i) THE FACE NAMES THE ROOT'S PROMPT BY FORM
    row1 = post_seal_row(True)
    face_1 = face7.replace('### POST-SEAL PROMPTS NAMED: NONE', row1)
    case('i', 'the builder`s row where the order puts the root`s prompt after the lock', row1, '### POST-SEAL PROMPTS NAMED: 1 (the root`s prompt)')
    case('i', 'the builder`s row where no prompt follows the lock (NEG of the form)', post_seal_row(False), '### POST-SEAL PROMPTS NAMED: NONE')
    case('i', 'b711`s answers bank under the repaired arm, its face naming 1: passes', CK.answers_bank_ok(a7, aj7, lock, face_1, 'b711', CK7.FLOORS), True)
    case('i', 'b711`s answers bank under the repaired arm, a face naming 0 (b711`s own, NONE): fails', CK.answers_bank_ok(a7, aj7, lock, face7, 'b711', CK7.FLOORS), False)
    case('i', 'the arm reads the row`s figure from the form "1 (the root`s prompt)"', CK.post_seal_named(face_1), 1)
    after = [c.get('ts') for c in aj7.get('calls') or [] if CK.iso_epoch((c.get('ts') or '')[:19] + 'Z') and CK.iso_epoch((c.get('ts') or '')[:19] + 'Z') > lock]
    notes.append('(i) b711`s lock %s ; its answers bank`s calls after the lock %s ; b711`s face row %r' % (
        jl('b711_seal_hashes.json')['lock'], after, (re.search(r'### POST-SEAL PROMPTS NAMED: \S+', face7) or [None])[0]))
    # ---------------------------------------------------------------- (ii) THE GATE'S COMMIT READ FROM THE STEP BANK
    logs = _b711_logs()
    steps7 = jl('b711_steps.json').get('rows') or []
    marked = [dict(r, phase='gate') if r['commit'].startswith('85c26c1c') else r for r in steps7]
    case('ii', 'b711`s banks pass with 85c26c1c read as the gate (its step row marked gate in a copy)', CK.nothing_ahead_ok(face7, lock, logs, marked), True)
    case('ii', 'an undeclared commit before the lock fails (NEG)', CK.nothing_ahead_ok(face7, lock, logs + [('deadbeefcafe', 'x', lock - 60)], marked), False)
    case('ii', 'b711`s step bank as banked, no row marked gate: fails (the gate`s commit undeclared)', CK.nothing_ahead_ok(face7, lock, logs, steps7), False)
    case('ii', 'b711`s old arm on the same banks (every commit before the lock on the face): fails on 85c26c1c',
         all(h[:7] in face7 for h, s, t in logs if t <= lock), False)
    notes.append('(ii) b711`s commits at or before the lock %d ; on the face %d ; not on the face %s' % (
        len([1 for h, s, t in logs if t <= lock]), len([1 for h, s, t in logs if t <= lock and h[:7] in face7]),
        [h[:8] for h, s, t in logs if t <= lock and h[:7] not in face7]))
    # ---------------------------------------------------------------- (iii) THE HEAD LINE BUILT FROM BANKS
    sp = os.path.join(K.SP, 'b712_ctl_headline_%d' % int(time.time()))   # ### a new scratch directory per run; nothing is deleted
    os.makedirs(sp)
    for f in os.listdir(D):
        if f.startswith('b711_') and (f.endswith('push_out.txt') or f in ('b711_checks_postpush.txt', 'b711_act_root.json', 'b711_author_answers.txt',
                                                                          'b711_defects.txt', 'b711_scores_close.json')):
            shutil.copyfile(os.path.join(D, f), os.path.join(sp, f))
    ev = []
    hl = CL.head_line(dd=sp, act='b711', events=ev)
    case('iii', 'b711`s banks rebuild the head line with "1 prompt answered"', '; 1 prompt answered;' in hl, True)
    case('iii', 'b711`s banks rebuild the head line with "scores 8 of 8 HELD"', '; scores 8 of 8 HELD;' in hl, True)
    sc = jl('b711_scores_close.json')
    sc['N2'] = ['BROKEN', 'a planted BROKEN for the control']
    with open(os.path.join(sp, 'b711_scores_close.json'), 'w', encoding='utf-8') as fh:
        json.dump(sc, fh, ensure_ascii=False)
    hl7 = CL.head_line(dd=sp, act='b711', events=[])
    case('iii', 'a scores bank with one BROKEN prints 7 of 8 (NEG)', '; scores 7 of 8 HELD;' in hl7, True)
    case('iii', 'b711`s own head line (data/b711_closing.txt :1) carried 2 prompts and no score', ('2 prompts answered' in rdn('b711_closing.txt').split(NL)[0])
         and 'scores' not in rdn('b711_closing.txt').split(NL)[0], True)
    notes.append('(iii) rebuilt: %s' % hl)
    notes.append('(iii) with one BROKEN: %s' % hl7)
    # ---------------------------------------------------------------- (iv) THE MIRROR'S ORDER
    import zipfile
    zl = zipfile.ZipFile('D:/MY-DOwnloads/mirror-refresh-2026-10-25-b711.zip').read('MANIFEST.md').decode('utf-8-sig').replace(chr(13), '').split(NL)
    root7 = [l for l in zl if l.startswith('Act root: ')]
    case('iv', 'b711`s sequence replayed on a copy: the bank before mroot (the export`s root line NONE, b711`s root appended) refuses',
         bool(mirror_order('b711', [])), True)
    case('iv', 'after mroot (the export`s root line b711`s): the bank may be written', mirror_order('b711', root7), '')
    case('iv', 'a root line naming another act`s root refuses (NEG)', bool(mirror_order('b711', ['Act root: b710 11fe3e21'])), True)
    case('iv', 'before the act`s root is appended the order does not refuse (b712 now)', mirror_order('b712', []), '')
    notes.append('(iv) b711`s export`s root line now %r ; the refusal before mroot: %s' % (root7[:1], mirror_order('b711', [])[:120]))
    # ---------------------------------------------------------------- (v) THE COMMAND SCREEN READS A FRESH BANK; THE STATE FILE'S BLOB
    stale = _count_pipes(g(ROOT, 'show', '85c26c1c:data/b711_commands.json'))
    fresh = _count_pipes(rdn('b711_commands.json'))
    case('v', 'b711`s stale command bank (at its gate commit 85c26c1c) reproduces ANYPIPES 7', stale, 7)
    case('v', 'the fresh bank (refreshed after the seal, 13:04Z) reads 8', fresh, 8)
    blob7, blob11 = g(ROOT, 'rev-parse', 'b5898a61:tools/mirror_prevbuild.json').strip(), g(ROOT, 'rev-parse', '4a383ac8:tools/mirror_prevbuild.json').strip()
    case('v', 'tools/mirror_prevbuild.json`s blob at b711`s closing (4a383ac8) equal to b707`s (b5898a61): b711`s "committed with this closing" false',
         bool(blob7) and blob7 == blob11, True)
    sfs = CL.state_file_sentence()
    case('v', 'the repaired sentence now: "unchanged since its last commit", not "committed"', 'unchanged since its last commit' in sfs and 'not committed' in sfs, True)
    notes.append('(v) ANYPIPES stale %s, fresh %s ; the blob at b707 %s, at b711`s closing %s ; the sentence now: %s' % (stale, fresh, blob7[:8], blob11[:8], sfs))
    # ---------------------------------------------------------------- THE NEXT LINE
    ot = rd(OT)
    found = K.orders_naming(ot, 'b712')
    plant = ot + NL + '*Appended 2026-10-25 by b799 -- THE ORDER **`W-ORD-PLANTED-CONTROL`**: a planted row. Status OPEN, for b713.' + NL
    case('NEXT', 'a planted open-orders row whose status names b713 is printed by the NEXT line', 'W-ORD-PLANTED-CONTROL' in K.next_line(text=plant), True)
    case('NEXT', 'the same row is not printed for another act (NEG)', any(o == 'W-ORD-PLANTED-CONTROL' for _i, o, _s in K.orders_naming(plant, 'b714')), False)
    case('NEXT', 'the NEXT line opens with the ruling`s named items', K.next_line(text=plant).startswith(K.NEXT), True)
    notes.append('(NEXT) the open-orders rows whose status names b712 on OPEN_TRAILS now: %s' % (found or 'NONE'))
    notes.append('(NEXT) the line now: %s' % K.next_line()[:400])
    notes.append('(iii) the scratch copies: %s (left in the scratchpad)' % sp)
    nw = [r for r in rows if not r['as_wanted']]
    L = ['%s -- COMPONENT 1, (R322)(3): THE FIVE REPAIRS AND THE NEXT LINE`S, EACH ON b711`S BANKS WITH ITS CONTROL (%s)' % (ACT, utc()), '',
         '### rows are cases: the section | the case | the reading got | the reading wanted | AS WANTED. The sections: (i) the face names the root`s',
         '### prompt by form; (ii) the gate`s commit from the step bank; (iii) the head line from banks; (iv) the mirror`s order; (v) the command',
         '### screen`s fresh bank and the state file`s blob; NEXT the open-orders rows. Each control is (R322)(3)`s own; a NEG case beside it. The',
         '### head-line copies are made in the scratchpad and removed after the reading.', '']
    L += ['  %-5s | %-150s | got %-34s | wanted %-34s | %s' % (r['section'], r['case'][:150], str(r['got'])[:34], str(r['wanted'])[:34],
                                                           'AS WANTED' if r['as_wanted'] else '### NOT AS WANTED -- ' + r['note']) for r in rows]
    L += ['', '### THE READINGS BESIDE THE CASES:'] + ['  ' + n for n in notes]
    L += ['', '### ### **CASES %d ; AS WANTED %d ; NOT AS WANTED %d.**' % (len(rows), len(rows) - len(nw), len(nw))]
    if 'dry' not in a:
        put_txt('%s_repair_controls.txt' % ACT, L)
        put_json('%s_repair_controls.json' % ACT, dict(at=utc(), cases=rows, as_wanted=not nw, not_as_wanted=len(nw), notes=notes))
    print(NL.join(L[7:]))


REPAIRS712 = (
    ('(56)', '(R322)(3)(i), THE FACE NAMES THE ROOT`S PROMPT BY FORM',
     'tools/b712_record.py post_seal_row and the `facerows` route (the face`s post-seal row built from the act`s order: "### POST-SEAL PROMPTS NAMED: '
     '1 (the root`s prompt)" where the root`s prompt follows the lock); tools/b712_checks.py post_seal_named and answers_bank_ok (G-ANSWERS-BANKED '
     'reading that row, pure in its banks), answers_ok calling it. Answers b711`s events :61. Control: data/b712_repair_controls.txt (i)'),
    ('(57)', '(R322)(3)(ii), THE GATE`S COMMIT READ FROM THE STEP BANK',
     'tools/b712_record.py PRE_SEAL_PHASES with the phase `gate`; tools/b712_checks.py nothing_ahead_ok (the one step-bank row of phase gate exempt, '
     'every other commit at or before the lock declared on the face by its hash), G-NOTHING-RAN-AHEAD calling it. Answers b711`s events :66. Control: (ii)'),
    ('(58)', '(R322)(3)(iii), THE HEAD LINE BUILT FROM BANKS',
     'tools/b712_closing.py head_line: the prompt count the answers bank`s rows with nothing added (b700`s "+ 1" removed), the scores "scores <k> of 8 '
     'HELD" from the scores-close bank. Answers b711`s events :79. Control: (iii)'),
    ('(59)', '(R322)(3)(iv), THE MIRROR`S ORDER',
     'tools/b712_record.py mirror_order and mbank: the mirror bank refused, nothing written, while the act`s root is appended and the export`s root '
     'line does not read the act`s root. Answers b711`s events :75. Control: (iv)'),
    ('(60)', '(R322)(3)(v), THE COMMAND SCREEN READS A FRESH BANK',
     'tools/b712_regspec.py refresh_commands (the command bank rewritten by the record tool`s `commands` route in the spec`s own step, the spec '
     'refused where it is not); tools/b712_closing.py state_file_sentence (the state file`s blob against HEAD and its last commit before "committed"), '
     'mirror_line calling it. Answers b711`s events :3 and the added item of (R322)(2). Control: (v)'),
    ('NEXT', 'THE NEXT LINE',
     'tools/b712_worklist.py orders_naming and next_line (the ruling`s named items, then every open-orders row of OPEN_TRAILS whose status names '
     'the next act, read at closing time); tools/b712_record.py the entry`s and the trail`s Next lines calling it. Answers b711`s events :46. Control: NEXT'),
)
REPAIR712_TRACKED = ('tools/b712_record.py', 'tools/b712_worklist.py', 'tools/b712_checks.py', 'tools/b712_closing.py', 'tools/b712_regspec.py')


def toolrepairs12(*a):
    """data/b712_tool_repairs.txt (.json), Component 1, (R322)(3): each repair's row (its standing clauses v3 row, its objects, its control's
    section in data/b712_repair_controls.txt) and the diffs of the five tools against their commit at step zero (relay 46750da9), each whole.
    The standing report tool's row is appended at Component 5, when its items are written."""
    ctl = jl('%s_repair_controls.json' % ACT)
    if not ctl.get('cases'):
        sys.exit('### data/b712_repair_controls.json IS NOT WRITTEN -- THE CONTROLS FIRST; NOTHING WRITTEN')
    nw = [c for c in ctl['cases'] if not c.get('as_wanted')]
    L = ['%s -- COMPONENT 1, (R322)(3): THE FIVE REPAIRS (STANDING CLAUSES v3 ROWS (56)-(60)) AND THE NEXT LINE`S, WITH THEIR DIFFS (%s)' % (ACT, utc()), '',
         '### rows are repairs: the row | what is repaired | its objects and its control. The controls: relay data/b712_repair_controls.txt (%d cases,' % len(ctl['cases']),
         '### %d as wanted, %d not as wanted). The diffs follow the rows: each tool against its blob at relay %s (the step-zero commit), `git diff`.' % (
             len(ctl['cases']) - len(nw), len(nw), K.STEPZERO_BANKS[:8]), '']
    for n, what, objs in REPAIRS712:
        L += ['  %s %s.' % (n, what)] + ['      ' + x for x in _wrap_words(objs, 140)] + ['']
    stat = []
    for p in REPAIR712_TRACKED:
        d = g(ROOT, 'diff', K.STEPZERO_BANKS, '--', p).replace(chr(13), '').rstrip(NL)
        add = sum(1 for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))
        rem = sum(1 for l in d.split(NL) if l.startswith('-') and not l.startswith('---'))
        stat.append((p, add, rem))
        L += ['', '### %s : +%d -%d' % (p, add, rem)] + (['    ' + l for l in d.split(NL)] if d else ['    (unchanged)'])
    L += ['', '### ### **REPAIRS %d (FIVE OF v3 ROWS (56)-(60) AND THE NEXT LINE) ; CONTROLS %d, AS WANTED %d, NOT AS WANTED %d ; TOOLS DIFFED %d ; '
              'NO SEALED TOOL OF AN EARLIER ACT EDITED.**' % (len(REPAIRS712), len(ctl['cases']), len(ctl['cases']) - len(nw), len(nw), len(REPAIR712_TRACKED))]
    if 'dry' in a:
        print(NL.join(L[:30] + L[-1:]))
        return
    put_txt('%s_tool_repairs.txt' % ACT, L)
    put_json('%s_tool_repairs.json' % ACT, dict(at=utc(), repairs=[dict(row=n, what=w) for n, w, _o in REPAIRS712], tracked=stat,
                                                 controls=len(ctl['cases']), not_as_wanted=len(nw)))
    print(L[-1])


# ### stage one (step zero): b711's Component routes over its own objects pruned (data/b712_prune_record.txt); this act's are added by the Edit tool
ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              ksyms=ksyms, defs=defs, figures=figures, runner=runner,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry, linecheck=linecheck,
              step=step, c1=c1, repairctl=repairctl12, toolrepairs=toolrepairs12, facerows=facerows, portedit=portedit, portdispatch=portdispatch, portrun=portrun, regpos=regpos, joingrade=joingrade, jointag=jointag,
              scores=scores, findings=findings, trail=trail, drycheck=drycheck, components=components, mbank=mbank, guard=guard,
              scorercheck=scorercheck, armnames=armnames)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b712_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
