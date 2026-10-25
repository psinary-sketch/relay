# -*- coding: utf-8 -*-
"""b711_record.py -- THE ACT'S RECORD TOOL, b711 under (R321).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b711 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers, b704's repaired read route and its probe, tie, quote and cut forms, b705's routes (the print-list dispatch, the artifact reader),
### b706's (the runner choosing the run's artifact by name, the prints branch, the probe-step artifact, the mentions re-read) and b710's (the
### declared untracked writes, the root route's dry run, the rowgen roster re-pointed, the previous window in b701's form) are reached through
### tools/b710_record.py (sealed at b710 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### Written by the Write tool at b711 in stages: stage one, step zero's routes (the tie among them); Components 1-6 by the Edit tool.
### Routes: `python tools/b711_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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

import b711_worklist as K          # noqa: E402
import b710_worklist as K707       # noqa: E402  ### b710's data, for the controls on b710's banks
import b710_record as P7           # noqa: E402  ### b710's tool, imported unedited (its import binds b698's R, b703's P3, b704's P4, b705's P5 and b706's P6 to b710: rebound below)
R, P3, P4, P5, P6 = P7.R, P7.P3, P7.P4, P7.P5, P7.P6   # ### b698's routes, b703's to b706's repaired readers, through b710's module

ACT, PREV = 'b711', 'b710'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b710 ran and closed in ANOTHER session (0be08567; this act opens c9e4ce2d after the author's /clear) -- b701's
# ### form: from b710's post-push combine in that session to that session's end (prev_capture below; a carry-time repair of b710's same-session bound)
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = PREV_SUBAGENTS
FACE = os.path.join(D, 'b711_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b711_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b710_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('mirror_prevbuild.json',)   # ### (R321)(2): the mirror builder's own state file, written at every build

# ### THE ROOT ROUTE'S EXCLUSION LIST (data/b706_rules.txt row (1)): the kinds b698's route excludes, carried; and every untracked write a
# ### b711_*.py tool declares in its own head, read at import. A tool declares one by a line `### UNTRACKED WRITE: data/b711_<name>`.
# ### (R321)(2): the events bank (row (52): a finding after the seal, written after the seal and after the root) and the step bank (G-SEALED-AFTER-
# ### COMPONENTS, a row per commit written after the commit, the record's and the closing's among them) are the defects bank's kind: not root items
EXCLUDE_KINDS = P7.EXCLUDE_KINDS + r'|events|steps'
# ### b710's declaration line read to its first space (b710: `\s*$`, which refused a declaration followed by prose and so read the grid's and the
# ### pairs' declarations as none -- the root's first dry run named 32 untracked units files); a name ending in `*` declares every file with that
# ### prefix (the grid's segment files, the pairs' band files). A carry-time repair, banked by diff (data/b711_tool_repairs.txt).
UNTRACKED_DECL = re.compile(r'^### UNTRACKED WRITE: data/b711_(\S+)', re.M)


def declared_untracked():
    """every b711_*.py tool's declaration of an untracked write (its units file, its download), read from the tools' own heads: [(tool, name)]."""
    out = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b711_') and f.endswith('.py'):
            for m in UNTRACKED_DECL.finditer(rd(os.path.join(T, f)) or ''):
                out.append((f, m.group(1)))
    return out


def _root_exclude():
    names = [(re.escape(n[:-1]) + r'\S*') if n.endswith('*') else re.escape(n) for _f, n in declared_untracked()]
    return re.compile(r'^b711_(' + EXCLUDE_KINDS + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


R.ROOT_EXCLUDE = _root_exclude()

# ### (R321)(2)(ii), standing clauses v2 row (53): THE MEMBRANE in the shared writers -- b698's put_json and put_txt (which every route of this
# ### tool and of b698's to b710's modules writes through) wrapped by tools/act_membrane.py's guard, which refuses a bank the root names once
# ### this act's root is appended to data/act_roots.txt; the mirror builder's banks and the root's exclusions pass (a repair at b711, banked by diff).
import act_membrane as MEM          # noqa: E402
_put_json0, _put_txt0 = R.put_json, R.put_txt


def put_json(name, obj):
    MEM.guard(ACT, name, R.ROOT_EXCLUDE)
    _put_json0(name, obj)


def put_txt(name, lines):
    MEM.guard(ACT, name, R.ROOT_EXCLUDE)
    _put_txt0(name, lines)


R.put_json, R.put_txt = put_json, put_txt
for _m in (P3, P4, P5, P6, P7, getattr(P7, 'P7', None)):   # ### b703's to b710's modules bound b698's writers at their own import
    for _n, _f in (('put_json', put_json), ('put_txt', put_txt)):
        if _m is not None and hasattr(_m, _n):
            setattr(_m, _n, _f)


def rootexclude(*a):
    """prints the declared untracked writes and the exclusion pattern they extend; writes nothing."""
    decl = declared_untracked()
    for f, n in decl:
        print('  %-28s declares data/b711_%s untracked' % (f, n))
    print('  DECLARED UNTRACKED WRITES %d ; ROOT_EXCLUDE %s' % (len(decl), R.ROOT_EXCLUDE.pattern))


_R_anchor_ts = P7._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704 to b710


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

# ================================================================================ b703'S TO b710'S REPAIRED READERS, THROUGH b710'S MODULE
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
roster709 = P7.roster709                        # ### b707's rowgen roster re-pointed through data/b706_partners.json (the fourth path reader), through b710's module (a carry-time repair: the substitution shifted b710's own name for it)


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried; rowgen's roster b710's)
answers = R.answers


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables, each at the file of record after b706's renames (b710's roster707); each tool's verdict lines
    banked with its exit. data/b711_rowgen_<stage>.txt."""
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
         '((R316)(3): %d of the bank`s paths re-pointed from the retired versioned name, data/b706_partners.json, b710`s reader) ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), len(moved), secs), '']
    L += ['### re-pointed: %s -> %s' % (f, p) for _n, f, p in moved]
    L += ['', '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19 ; RE-POINTED %d.**' % (con.returncode, dif.returncode, len(moved))]
    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)
    print(NL.join(L[-14:]))


# ================================================================================ (R321)(2)(i), STANDING CLAUSES v2 ROW (52): THE LETTERS AT THE SEAL
def letters_of(text):
    """the lettered rows of a defects bank's text, each '(x) HEAD' by b703's row reader (pure in its argument)."""
    L = (text or '').replace(chr(13), '').split(NL)
    return [s for s in (read_defect_row(L, i) for i, l in enumerate(L) if DEFECT_ROW.match(l)) if s]


def _letter(s):
    m = re.match(r"^\(([a-z]'?)\)", s or '')
    return m.group(1) if m else None


def letters_at_seal(act):
    """the letters entered before the seal: the list the suite's seal records with the hashes (data/<act>_seal_hashes.json `letters`, from b711);
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
    """data/b711_defects.json from the bank; after the seal (row (52)) it refuses a letter the seal did not record: a finding after the seal is
    entered in data/b711_events.txt for the closing's events section, and the next act's corrigendum letters it."""
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    seal = letters_at_seal(ACT)
    if seal is not None:
        late = [s for s in letters_of(t) if _letter(s) not in set(_letter(x) for x in seal)]
        if late:
            sys.exit('### (R321)(2)(i): %d LETTER(S) ENTERED AFTER THE SEAL (%s) -- A FINDING AFTER THE SEAL IS AN EVENT, ENTERED IN data/%s_events.txt, '
                     'NOT A LETTER -- NOTHING WRITTEN' % (len(late), ', '.join(s[:3] for s in late), ACT))
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ (R321)(2): THE ACT'S STEP BANK (G-SEALED-AFTER-COMPONENTS reads it)
PRE_SEAL_PHASES = ('step zero', 'component 1', 'component 2', 'component 3', 'component 4', 'component 5')
POST_SEAL_PHASES = ('seal', 'pre-root', 'root', 'record', 'closing')
STEP_PHASES = PRE_SEAL_PHASES + POST_SEAL_PHASES
STEP_REPOS = dict(relay=ROOT, pp=PP)


def step(*a):
    """`step <relay|pp> <phase words> [commit]`: one row appended to data/b711_steps.json after a commit -- the repository, the commit (HEAD where
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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R321)(8); b710's form)
def branches(*a):
    """`branches before`: data/b711_branches_before.json -- b698's route, carried (every branch (R321)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b711_branches.txt (.json) --
    each branch's fate read now against the tips banked before; the kept branch port-b707 read beside them."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b711_branches_before.json IS NOT WRITTEN -- NOTHING READ')
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
    L = ['%s -- STEP ZERO, (R321)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b711_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. (R321)(7) names relay`s four and PLACE-papers` two; port-b707 of',
         '### SIDE-lv-conservation is NOT deleted, local or remote, read beside them.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['  %-22s | %-28s | kept   | local %s ; remote %s ; %s' % (os.path.basename(krepo), kb, kept_local[:12] or 'absent', kept_remote[:12] or 'absent',
                                                                'STANDS' if kept_local == kept_remote == K.PORT_TIP else '### NOT AS KEPT')]   # ### a carry-time repair: b710's tip, K.PORT_TIP
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
    offence. data/b711_read_calls.txt."""
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
    mod = {'b698': R, 'b703': P3, 'b704': P4, 'b705': P5, 'b706': P6, 'b710': P7}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
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
WF = getattr(K, 'WORKFLOW', '')   # ### a carry-time repair: no dispatch this act ((R321)(7)), the worklist names no workflow


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


# ================================================================================ THE LATE ROUTES (b710's, carried with b711's names; the previous window in its own session)
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
    """G-EDIT-ROUTE's window over the previous act, b701's form for a previous act in ITS OWN session (b710's carry-time repair, carried): b710's
    capture AFTER ITS POST-PUSH SUITE -- every command of session 0be08567 from the call that combined b710's post-push parts into
    data/b710_checks_postpush.txt to that session's end, its closing's commands among them; this act runs in a session of its own."""
    rows = ER.capture(PREV_SESSION_PATH, K.PREV_ANCHOR, PREV_SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    anchor = '9999'   # ### b711's carry-time repair: the previous act ran in ITS OWN session (b710 bounded it at this act's anchor, b700's same-session form), so its window runs to that session's end (b701's form)
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
# ### b710's pattern read `_record.py dispatch`; this act's one dispatch ran through the `portdispatch` route, so the pattern takes the port prefix too
# ### (a carry-time repair, banked by diff: the command bank's first write read DISPATCHES 0 against the dispatch bank's one row)
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)


def commands(*a):
    """b710's route with b711's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window (b710's
    session from its post-push combine to its end), the local lean reading (N1), the dispatches (two ordered: the probe branch and the prints
    branch), the detached runs, sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound requests.
    data/b711_commands.txt (.json)."""
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
    L += ['', '### THE RUNNER DISPATCHES (one ordered this act, N1: the port branch of SIDE-lv-conservation at its tip, through the portdispatch route) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R321)(8) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
    print('  kernels read: %d (SIDE-faces-join among them; no kernel main written this act; SIDE-lv-conservation`s port-b707 at this act`s one commit, its checkout at main for this read)' % len(ks))


def _standing():
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B709_FACE.split('/')))) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))   # ### a carry-time repair: the previous face b710's (the upper-case name the substitution left)


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
    (the push clause, HEAD the remote main, printed beside and not required before the record`s push). data/b711_root_banks_dry.txt (.json)."""
    banks = root_banks()
    s = root_banks_state(banks)
    crlf = [b_ for b_ in banks if os.path.exists(os.path.join(ROOT, *b_.split('/'))) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    missing = [b_ for b_ in banks if not os.path.exists(os.path.join(ROOT, *b_.split('/')))]
    ready = bool(s['rows']) and s['clean'] and not crlf and not missing
    L = ['%s -- THE ROOT ROUTE`S DRY RUN ON THE PRE-ROOT TREE BEFORE THE SEAL (data/b706_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are the banks the root route names (tools/b698_record.py root_banks with ROOT_EXCLUDE rebound at tools/b711_record.py, extended by',
         '### every declared untracked write: %s): status ; carried by HEAD ; HEAD`s blob equal to the file ; CR LF.' % (
             [n for _f, n in declared_untracked()] or 'NONE DECLARED'),
         '### HEAD %s ; the remote main %s ; equal %s (the push clause, read beside: the record`s push comes after the seal)' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %-5s crlf %s' % (r['bank'], r['status'], r['at_head'], r['equal'], r['bank'] in crlf) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; CR LF %s ; MISSING %s ; HEAD THE REMOTE MAIN %s ; THE DRY RUN READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), crlf or 'NONE', missing or 'NONE', s['pushed'], ready)]
    put_txt('%s_root_banks_dry.txt' % ACT, L)
    put_json('%s_root_banks_dry.json' % ACT, dict(at=utc(), ready=ready, crlf=crlf, missing=missing, declared=declared_untracked(), **s))
    print(L[-1])


# ================================================================================ STEP ZERO: THE LICENSED TABLE'S NEXT DOCUMENT, (R321)(6) (b704's tie form)
SUMMARY = re.compile(r'### ### \*\*(\w+): CLAIMS (\d+) ; SKIPPED LINES (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)')


def tie(*a):
    """data/b711_tie.txt: (R321)(6), the licensed table's next document -- b652's order, b674's tie-break rule and data/b705_rules.txt row (2)
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
    L = ['%s -- STEP ZERO, (R321)(6): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER, b674`S TIE-BREAK RULE AND b705`S ROW (2) PRINTED BEFORE IT IS NAMED (%s)' % (ACT, utc()), '',
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
            L.append('    (ii) a declared suite failure on either document: NONE (no arm of b710`s suite names either; data/b710_checks.txt)')
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


# ================================================================================ COMPONENT 2: THE PROBE THROUGH THE WORKFLOW'S STEP, (R321)(4)
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
    """b705's _print_modules (tools/b705_record.py :732) with the carry-time repair of this act (data/b711_tool_repairs.txt row (1)): a hit under a
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
    """`runner <kernel> <run id> <ref> <label> <note...>`: b706's runner706 carried with b711's names -- the run's artifact chosen BY NAME
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
# ================================================================================ COMPONENT 5: THE FOUR STANDING FIGURES (b706`s tool, unedited, against b710`s baselines)
def figures(*a):
    """data/b711_standing_figures.txt (.json): the four figures by relay tools/b706_standing_figures.py, unedited (correspondence() and partners()
    over b706's roster, data/b706_roster_read.json; readme() b705's, pins() b703's), each against b710's figure (data/b710_standing_figures.json),
    the pins baseline b710's rows."""
    import b706_standing_figures as SF6
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b710_standing_figures.json')
    f = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    pr = (f.get('partners') or {}).get('rows') or []
    cr = (f.get('correspondence') or {}).get('papers') or []
    L = ['%s -- COMPONENT 5: THE FOUR STANDING FIGURES AT b711, READ BY b706`S TOOL OVER b706`S ROSTER, AGAINST b710`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b706_standing_figures.py, unedited (correspondence() and partners() over data/b706_roster_read.json, the 20 tables at the',
         '### unversioned names; readme() tools/b705_standing_figures.py`s, pins() tools/b703_standing_figures.py`s), %.0f s; each arm fails on a' % (t1 - t0),
         '### regression from the previous act`s figure (data/b710_standing_figures.json). No document is cut this act; day1/Spectral_Inertness.md (cut at b708) is off the roster;',
         '### both kernels on main at the read (SIDE-lv-conservation`s checkout at main; port-b707 not checked out this act, b707`s trap).', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        L.append('  %-15s b711 %s ; b710 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE CORRESPONDENCE ROWS PER PAPER (current | behind | changed statement | unread ; the reason where the table is not read):']
    L += ['  %-36s %-66s current %3d behind %3d changed %3d unread %3d%s' % (p['paper'], p['path'], p['current'], p['behind'], p['changed'], p['unread'],
                                                                           (' ; ' + p['reason']) if p.get('reason') else '') for p in cr]
    L += ['', '### THE PARTNERS ROWS, ONE PER ROSTER TABLE:']
    L += ['  %-36s %-66s %s' % (r['paper'], r['path'], r.get('reason') or ('differing %s against %s' % (r.get('differing'), r.get('partner')))) for r in pr]
    one = sum(1 for r in pr if (r.get('reason') or '').startswith('ONE COPY'))
    L += ['', '### ### **FIGURES AT b711: CORRESPONDENCE %s ; README %s ; PARTNERS %s (ONE COPY %d OF %d TABLES) ; PINS %s -- AGAINST b710`S %s, %s, %s, %s ; THE ROSTER b706`S, %d TABLES.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), (f.get('partners') or {}).get('figure'), one, len(pr),
        (f.get('pins') or {}).get('figure'), (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'),
        (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'), len(cr))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), roster='b706_roster_read.json', baseline='b710_standing_figures.json',
                                                        **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:10] + L[-1:]))


def linecheck(*a):
    """`linecheck <record-lines bank> <i> <needle>...`: the suite's landed-line reading (tools/b703_checks.py landed) reproduced piece by piece and
    printed -- the bank's row, the ledger line at its number through the suite's own reader, conv(head), startswith and each needle; print only."""
    import b711_checks as CH
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
    print('### ### **K.<NAME> REFERENCES %d ; MISSING FROM b711_worklist %d: %s.**' % (len(seen), len(missing), missing or 'NONE'))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R321)(1)
WH = ('*Appended 2026-10-25 by b711 to b710’s entry (:10246), under `(R321)`(1) -- b710 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b710_closing.txt):*')


def _fig(text, pat, what):
    m = re.search(pat, text)
    if not m:
        sys.exit('### b710`S BANKS DO NOT CARRY %s (%s) -- NOTHING COMPOSED' % (what, pat))
    return m.groups() if m.groups() else (m.group(0),)


def _wb():
    """b710's weight line, every figure read from b710's banks by row: the head from its closing :1, the suite from its two banks, the sealed
    hashes and the citation check from the closing, reading 5 and the moves from its verdict, the standing clauses' control, the root and its
    banks, the mirror, the scores (a PENDING row read from the close bank), the defects by the repaired reader; the record's commits by the
    repaired head-line builder over b710's own captures (tools/b711_closing.py head_line), the capture-name failure named as defect (k)."""
    c = rdn('b710_closing.txt')
    head = c.split(NL)[0]
    n_pre, p_pre = _fig(rdn('b710_checks.txt'), r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the pre-push suite')
    n_post, p_post = _fig(rdn('b710_checks_postpush.txt'), r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the post-push suite')
    chain, = _fig(rdn('b710_checks_postpush.txt'), r'(?m)^\s+G-ACTROOT-VERIFY\s+(PASS)\s', 'the chain`s arm passing post-push')
    agree, of_a = _fig(c, r'### AGREE (\d+) of (\d+)', 'the sealed hashes')
    cites, ok, miss = _fig(c, r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', 'the citation check')
    r5 = ' '.join(rdn('b710_reading5.txt').split())
    comp, ctl = _fig(r5, r'WITH A COMPILED THEOREM (\d) OF 4 .*?WITH A CONTROL OBJECT (\d) OF 4', 'reading 5`s principles')
    rows, tried, untried = _fig(r5, r'THE MOVES TABLE (\d+) ROWS, TRIED (\d+), UNTRIED (\d+)', 'the moves table')
    sc_ok, = _fig(rdn('b710_standing_control.txt'), r'THE CONTROL AS WANTED (True)', 'the standing clauses` control')
    banks, = _fig(rdn('b710_root_banks.txt'), r'BANKS (\d+) ; CLEAN AND EQUAL AT HEAD', 'the root banks')
    mi = rdn('b710_mirror.txt')
    files, = _fig(mi, r'entries in the zip \d+ \(files (\d+) \+ MANIFEST\)', 'the mirror`s files')
    _fig(mi, r'THE VERIFICATION : CLEAN ON ALL THREE CLAUSES', 'the mirror`s verification')
    ar = jl('b710_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b710_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    sr, scl = jl('b710_scores.json'), jl('b710_scores_close.json')
    keys = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    sv = dict((k, ((scl.get(k) if (sr.get(k) or ['-'])[0] == 'PENDING' else sr.get(k)) or ['-'])[0]) for k in keys)
    n1 = (sr.get('N1') or ['', ''])[1]
    if 'running lean or lake (relay data/b710_commands.json): []' not in n1 or 'runner dispatches banked 0' not in n1:
        sys.exit('### b710`S N1 DOES NOT READ NO LEAN AND NO DISPATCH -- NOTHING COMPOSED')
    if not (sr.get('N5') or ['', ''])[1].startswith('nothing deposits: the deposit route untouched'):
        sys.exit('### b710`S N5 DOES NOT READ NOTHING DEPOSITED -- NOTHING COMPOSED')
    short = _defect_short('b710')
    seat = sum(1 for s in short if "THE SEAT'S" in s)
    regc = g(ROOT, 'log', '--diff-filter=A', '--format=%h', '--', 'data/b710_registrations.txt').strip()
    import b711_closing as CL
    ev = []
    hl = CL.head_line(act='b710', events=ev)
    mc = re.match(r'^b710 closed: relay (\w+), PLACE-papers (\w+);', hl)
    if not mc or len(ev) != 2:
        sys.exit('### THE REPAIRED HEAD LINE OVER b710`S CAPTURES DID NOT READ BOTH COMMITS (%r ; events %d) -- NOTHING COMPOSED' % (hl[:80], len(ev)))
    return (' “%s” (data/b710_closing.txt :1). The head line carries the closing tool’s capture-name failure text where the record’s commits '
            'belong, defect (k); the record’s commits, read by this act’s repaired builder from b710’s own push captures, are relay %s and '
            'PLACE-papers %s (data/b711_repair_controls.txt). Reading 5 in data/b710_reading5.txt: the four principles against the corpus, %s '
            'of 4 with a compiled theorem and %s with a control object; the moves-by-locus table, %s rows (%s tried, %s untried), entered as '
            'W-ORD-MOVES-BY-LOCUS at OPEN_TRAILS :%d; W-ORD-READING5-INDEPENDENCE at :%d on the author’s word at the root’s prompt; the entry at '
            'FINDINGS :%d, the trail at OPEN_TRAILS :%d. The standing clauses banked at data/standing_clauses_v1.txt, the re-assembly control '
            'as wanted %s (data/b710_standing_control.txt). data/b710_registrations.txt committed at relay %s (the refined detection law, the '
            'surgery, the coefficient observation). The root %s over %s banks chained from %s (data/b710_act_root.json, data/b710_root_banks.txt), '
            'the chain b624–b710 read AGREE by G-ACTROOT-VERIFY post-push (%s); the mirror mirror-refresh-2026-10-24-b710.zip CLEAN on all three clauses over %s files (data/b710_mirror.txt). '
            'N1 %s, N2 %s, N3 %s, N4 %s, N5 %s, S1 %s, S2 %s, S3 %s (data/b710_scores.json, data/b710_scores_close.json); the sealed tools’ '
            'hashes %s of %s equal at the close; the citation check %s cites, %s OK, %s missed; suite %s of %s '
            'pre-push and %s of %s post-push (data/b710_checks.txt, data/b710_checks_postpush.txt); no dispatch and no lean on the host (N1); %d defects '
            '(a)–(%s), %s the seat’s (data/b710_defects.txt). Nothing deposited.' % (
                head, mc.group(1), mc.group(2), comp, ctl, rows, tried, untried, K.ORDER_MOVES, K.ORDER_INDEPENDENCE, K.B710_ENTRY, K.B710_TRAIL,
                sc_ok, regc, ar['root'][:8], banks, ar['previous'][:8], chain, files, sv['N1'], sv['N2'], sv['N3'], sv['N4'], sv['N5'], sv['S1'],
                sv['S2'], sv['S3'], agree, of_a, cites, ok, miss, p_pre, n_pre, p_post, n_post, len(short), _letter(short[-1]) if short else '-',
                'all' if seat == len(short) else '%d of them' % seat))


def c1(*a):
    """FINDINGS: b710's weight line beneath b710's entry (:10246) through b698's landing and its screens; its line banked in
    data/b711_record_lines.json. `c1 dry` prints the line and writes nothing."""
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + _wb() + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B710_ENTRY,
         check=[('FINDINGS.md', K.B710_ENTRY, '## Reading 5: the four principles against the corpus'), ('OPEN_TRAILS.md', K.B710_TRAIL, '### b710'),
                ('OPEN_TRAILS.md', K.ORDER_MOVES, '`W-ORD-MOVES-BY-LOCUS`'), ('OPEN_TRAILS.md', K.ORDER_INDEPENDENCE, '`W-ORD-READING5-INDEPENDENCE`')],
         dry=dry)


# ================================================================================ COMPONENT 1: THE REPAIRS' CONTROLS, (R321)(2)
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
    """data/b711_repair_controls.txt (.json), Component 1, (R321)(2): each structural repair (standing clauses v2 rows (52)-(55)) and each item
    repair against the banks its old form failed on, with its NEG control; every reading printed beside the case. The suite's repaired forms are
    read from tools/b711_checks.py itself (imported), the closing's from tools/b711_closing.py, the membrane's from tools/act_membrane.py."""
    import b711_checks as CK
    import b711_closing as CL
    import act_membrane as MEM
    rows, notes, allok = [], [], True

    def case(sec, name, got, want, note=''):
        nonlocal allok
        ok = got == want
        allok = allok and ok
        rows.append(dict(section=sec, case=name, got=got, wanted=want, as_wanted=ok, note=note))

    # ---------------------------------------------------------------- (i) THE EVENTS SECTION
    sj7 = jl('b710_seal_hashes.json')
    seal7 = letters_at_seal('b710') or []
    s_let = [_letter(s) for s in seal7]
    now7 = [_letter(s) for s in letters_of(rdn('b710_defects.txt'))]
    body7 = _trail_defects_body('b710', K.B710_TRAIL) or ''
    t_let = re.findall(r"(?:^|; )\(([a-z]'?)\) ", body7)
    late7 = [x for x in now7 if x not in s_let]
    notes += ['(i) b710`s seal: %s, its relay head %s ; the letters in its defects bank at that head %s ; in the bank now %s ; on its trail`s Defects line '
              '(OPEN_TRAILS from :%d) %s ; after the seal, under the repaired route events: %s' % (
                  sj7.get('at'), (sj7.get('relay_head') or '')[:8], s_let, now7, K.B710_TRAIL, t_let, late7)]
    case('i', 'the ruling`s control: b710`s trail read under the repaired arms (its Defects letters against the letters entered before the seal) '
              'with (i) as an event passes', t_let == s_let, True,
         'the letters (g) and (h) were also entered after b710`s seal (lettered at relay 842ea536, after the seal`s head 71f1c2a0): under the rule`s '
         'cut they are events with (i)-(k), and b710`s trail, landed with (a)-(h), carries two of them -- for the author`s strike')
    case('i', 'NEG: a letter entered before the seal and missing from the trail fails (the seal`s letters with (z) added, the trail`s as entered)',
         s_let == s_let + ['z'], False)
    case('i', 'the trail carrying exactly the letters entered before the seal passes (the seal`s letters against themselves)', s_let == list(s_let), True)
    ev = []
    hl_new = CL.head_line(act='b710', events=ev)
    del CL.HEAD_EVENTS[:]
    CL.head_line(act='b710')
    sect = CL.events_section(act='b710')
    case('i', 'the closing`s events section over b710`s banks: the head-line builder`s failures land there, two (relay and PLACE-papers)',
         len([l for l in sect if l.startswith('    THE HEAD LINE: ')]), 2)
    notes += ['(i) the closing`s events section over b710`s banks: ' + ' | '.join(sect)]
    # ---------------------------------------------------------------- (ii) THE MEMBRANE
    test_roots = os.path.join(K.SP, 'b711_membrane_roots.txt')
    real = rd(MEM.ROOTS)
    with open(test_roots + '.tmp', 'wb') as fh:   # ### the control's own scratch write, outside relay
        fh.write((real.rstrip(NL) + NL + 'b711 %s %s' % ('f' * 64, (jl('b710_act_root.json').get('root') or '0' * 64)) + NL).encode('utf-8'))
    os.replace(test_roots + '.tmp', test_roots)
    probe = os.path.join(D, 'b711_membrane_probe.json')
    try:
        MEM.guard('b711', 'b711_membrane_probe.json', R.ROOT_EXCLUDE, roots=test_roots)
        code = 0
    except SystemExit as e:
        code = e.code
    case('ii', 'a bank write attempted after a test root refuses: the guard exits 4 and the bank is not written', (code, os.path.exists(probe)), (4, False))
    case('ii', 'after the test root a bank the root names is refused (data/b711_reading5.txt, data/b711_repair_controls.txt)',
         (bool(MEM.refuses('b711', 'b711_reading5.txt', R.ROOT_EXCLUDE, test_roots)), bool(MEM.refuses('b711', 'b711_repair_controls.txt', R.ROOT_EXCLUDE, test_roots))),
         (True, True))
    case('ii', 'after the test root the excluded banks pass: the closing, the events, the step bank, the push capture, the mirror builder`s',
         [bool(MEM.refuses('b711', n, R.ROOT_EXCLUDE, test_roots)) for n in ('b711_closing.txt', 'b711_events.txt', 'b711_steps.json', 'b711_relay_push_out.txt', 'b711_mirror.json')],
         [False] * 5)
    case('ii', 'on the real chain (b711 not appended) a write proceeds', bool(MEM.refuses('b711', 'b711_reading5.txt', R.ROOT_EXCLUDE)), False)
    case('ii', 'POS on the real chain: b710 is appended, so a b710 bank the root names is refused', bool(MEM.refuses('b710', 'b710_reading5.txt')), True)
    _wrap = lambda f: getattr(f, '__name__', '') in ('put_json', 'put_txt') and getattr(f, '__module__', '') in ('__main__', 'b711_record')   # noqa: E731
    wired = dict(record=(_wrap(R.put_json) and _wrap(R.put_txt)), citation=rd(os.path.join(T, 'b711_citation.py')).count('MEM.guard('),
                 closing=rd(os.path.join(T, 'b711_closing.py')).count('_guard('), suite=rd(os.path.join(T, 'b711_checks.py')).count('_membrane('),
                 independence=rd(os.path.join(T, 'b711_independence.py')).count('_membrane('), standing=rd(os.path.join(T, 'b711_standing.py')).count('_membrane('),
                 tests=rd(os.path.join(T, 'b711_tests.py')).count('_membrane('), carry=rd(os.path.join(T, 'b711_carry.py')).count('_membrane('))
    notes += ['(ii) the guard wired in the writers (calls in the text, the definition counted): %s' % wired]
    case('ii', 'every b711 writer calls the guard (the record`s shared writers rebound; the citation`s, the closing`s, the suite`s, independence`s, '
               'standing`s, the tests` and the carry`s calls present)', all(wired.values()), True)
    st0, ds0 = _status(), _data_state()
    rc1, o1 = _run(os.path.join(T, 'b711_record.py'), 'defs', 'b711_checks.py')
    rc2, o2 = _run(os.path.join(T, 'b711_record.py'), 'names', 'b711_checks')
    rc3, o3 = _run(os.path.join(T, 'b711_citation.py'), 'replay', 'Root: 1, proceed', K.PREV_SESSION, K.PREV_ANCHOR)
    st1, ds1 = _status(), _data_state()
    changed = sorted(f for f in set(ds0) | set(ds1) if ds0.get(f) != ds1.get(f))
    case('ii', 'three locator and read calls (the record tool`s defs and names routes, the citation tool`s replay) leave the tree unchanged by git '
               'status and relay data/ unchanged file for file', (rc1, rc2, rc3, st0 == st1, changed), (0, 0, 0, True, []))
    # ---------------------------------------------------------------- (iii) ARMS READ STRUCTURE
    g8, g9, g10 = rdn('b708_reg_gate.txt'), rdn('b709_reg_gate.txt'), rdn('b710_reg_gate.txt')
    case('iii', 'G-CLOSING-DRY-STEP: b708`s sealed needle on b708`s honest gate record fails (the bank b708 failed on)', '### NO VERDICT LINE' not in g8, False)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b708`s gate record passes', CK.no_verdict_line_ok(g8), True)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b709`s gate record (three rows) passes', CK.no_verdict_line_ok(g9), True)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b710`s gate record passes', CK.no_verdict_line_ok(g10), True)
    case('iii', 'NEG: b709`s record with a NO VERDICT LINE row named on a verdict-bearing bank (data/b709_pairs.txt) fails',
         CK.no_verdict_line_ok(g9.replace('data/b709_grid_hashes.txt): ### NO VERDICT LINE', 'data/b709_pairs.txt): ### NO VERDICT LINE')), False)
    case('iii', 'NEG: b709`s record with a NO VERDICT LINE row naming an absent bank fails',
         CK.no_verdict_line_ok(g9.replace('data/b709_grid_hashes.txt): ### NO VERDICT LINE', 'data/b709_nosuch.txt): ### NO VERDICT LINE')), False)
    k9 = ('ONSET', 'ZETA', 'RATIO', 'MODULES', 'FIGURES')
    rj9, rj10 = jl('b709_report.json'), jl('b710_report.json')
    case('iii', 'G-REPORT-UNSEALED: b709`s sealed needle on b709`s report text (the keys in capitals) fails', all(x in rdn('b709_report.txt') for x in k9), False)
    case('iii', 'G-REPORT-UNSEALED: the repaired reading of b709`s report JSON bank (its lines) passes', CK.report_lines_ok(rj9, k9, 5), True)
    case('iii', 'G-REPORT-UNSEALED: the repaired reading of b710`s report JSON bank on b710`s keys passes', CK.report_lines_ok(rj10, CK.REPORT_KEYS, 5), True)
    case('iii', 'NEG: b709`s report JSON with its lines cut to four fails', CK.report_lines_ok(dict(rj9, lines=(rj9.get('lines') or [])[:4]), k9, 5), False)
    case('iii', 'NEG: b709`s report JSON with every `ratio` removed, any case, fails',
         CK.report_lines_ok(dict(rj9, lines=[re.sub('(?i)ratio', 'quotient', x) for x in (rj9.get('lines') or [])]), k9, 5), False)
    q = '(e) representation coordinates (the operator / Toeplitz form) -- 4'
    reg9 = rdn('b709_registrations.txt')
    case('iii', 'G-AXIS-REGISTERED: b709`s sealed needle on b709`s registrations bank (the quotation wrapped) fails', q in reg9, False)
    case('iii', 'G-AXIS-REGISTERED: the repaired reading (joined; the bank has no JSON) passes', q in CK.joined(reg9), True)
    case('iii', 'NEG: the repaired reading on a copy with "Toeplitz" changed to "Hankel" fails', q in CK.joined(reg9.replace('Toeplitz', 'Hankel')), False)
    case('iii', 'each arm run on b710`s banks before the seal: the seal refuses while a part`s run on b710`s banks is not banked', bool(CK.prev_run_missing()), True)
    # ---------------------------------------------------------------- (iv) CONTROLS THAT CAN FAIL
    face7 = rd(os.path.join(ROOT, *K.B710_FACE.split('/')))
    S7 = dict(citation=rdn('b710_citation_check.txt'), lock_epoch=CK.utc_epoch(face7, 'locked at (UTC)'), movesj=jl('b710_moves_lines.json'),
              answers=rdn('b710_author_answers.txt'), files=dict(c3pp=[x for x in g(PP, 'show', '--name-only', '--pretty=format:', K707.C3_PP).split(NL) if x.strip()]))
    live7 = CK.answers_before_ok(dict(S7))
    old7 = CK.answers_before_ok(dict(S7, answers=S7['answers'] + NL + '### PROMPT 9 (planted)'))
    new7 = CK.answers_before_ok(CK.answers_plant(dict(S7)))
    case('iv', 'G-ANSWERS-BEFORE-WRITES on b710`s banks: the live reading passes (the moves answer checked before its landing and the lock)', live7, True)
    case('iv', 'G-ANSWERS-BEFORE-WRITES: b710`s plant (a prompt appended) leaves the arm passing -- the control that cannot fail', old7, True)
    case('iv', 'G-ANSWERS-BEFORE-WRITES: the repaired plant (every check stamp moved after the write it governs) fails the arm', new7, False)
    ex7 = jl('b710_exercise.json').get('exercise') or {}
    case('iv', 'the seal`s refusal over b710`s exercise bank: the arms whose mutated copy passed, the one b710 carried',
         sorted(n for n, e in ex7.items() if e.get('pos')), ['G-ANSWERS-BEFORE-WRITES'])
    shown, bad = CK.neg_shown()
    case('iv', 'the seal refuses now: no pre-run exercise bank is written, so no arm is shown failing (every arm named)', (len(shown), len(bad) == len(CK.ARMS)), (0, True))
    # ---------------------------------------------------------------- THE ITEM REPAIRS: (k) THE HEAD LINE, (i) THE STEP BANK, THE 468
    import b710_closing as CL7
    hl_old = CL7.head_line()
    case('k', 'b710`s builder over b710`s captures: the head line carries the capture-name failure', 'IS NOT THE RECORD`S CAPTURE' in hl_old, True)
    case('k', 'the repaired builder over b710`s captures: the head line carries the record`s commits and no failure text',
         (hl_new.startswith('b710 closed: relay 2c200e8d, PLACE-papers df2dd7c; suite 137 of 143; root 11fe3e21e2fc796a'), '###' in hl_new), (True, False))
    case('k', 'the repaired builder sends both capture-name failures to the events section', len(ev), 2)
    notes += ['(k) the repaired head line over b710`s banks: %s' % hl_new] + ['(k) event: %s' % e for e in ev]
    lock7 = S7['lock_epoch']

    def _log(repo, base, tip):
        return [(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
                g(repo, 'log', '--reverse', '--format=%h %ct %s', '%s..%s' % (base, tip)).split(NL) if l.strip()]
    rl7, pl7 = _log(ROOT, K707.PRE_RELAY, 'b0d874f7'), _log(PP, K707.PRE_PP, 'df2dd7c0')
    ps7 = re.search(r'^POST_SEAL = (\(.*\))$', rd(os.path.join(T, 'b710_checks.py')), re.M)
    import ast
    post7 = ast.literal_eval(ps7.group(1)) if ps7 else ()
    old_sa = all((t < lock7) == (s.startswith('b710') and not s.startswith(post7)) for h, s, t in rl7 + pl7)
    case('i/step', 'G-SEALED-AFTER-COMPONENTS: b710`s subject reading over b710`s commits fails (7c07c5d4 "b710 order", df2dd7c0 "b710 trail")', old_sa, False)
    full = lambda repo, h: g(repo, 'rev-parse', h).strip()   # noqa: E731
    fixture = [dict(repo='relay', commit=full(ROOT, h), phase=('component 5' if t < lock7 else 'record')) for h, s, t in rl7] + \
              [dict(repo='pp', commit=full(PP, h), phase=('component 3' if t < lock7 else 'record')) for h, s, t in pl7]
    S8 = dict(lock_epoch=lock7, steps=fixture, rlog=rl7, plog=pl7, REC=sys.modules[__name__])
    case('i/step', 'the repaired reading over a step bank for b710`s commits (b710 had none: the fixture`s phases set from each commit`s time against '
                   'the lock, so this row shows the reading is by the bank alone) passes', CK.sealed_after_ok(S8), True)
    case('i/step', 'NEG: a PLACE-papers commit after the lock given a component phase fails',
         CK.sealed_after_ok(dict(S8, steps=[dict(r, phase='component 3') if r['repo'] == 'pp' else r for r in fixture])), False)
    case('i/step', 'NEG: a commit with no row in the step bank fails', CK.sealed_after_ok(dict(S8, steps=fixture[1:])), False)
    m82 = re.search(r'b682\s+cut: (\d+) characters', o3)
    mre = re.search(r'repaired cut: (\d+) characters', o3)
    meq = re.search(r'the whole answer (\d+) characters ; the repaired cut equal to the text from its BEGIN to its last END: (\w+)', o3)
    case('468', 'the citation tool`s answer check over b710`s root answer: b682`s cut 468 characters, the repaired cut to the last END, equal to the '
                'text from its BEGIN to its last END (tools/b711_citation.py replay, print only)',
         (m82.group(1) if m82 else None, bool(mre) and int(mre.group(1)) > 468, meq.group(2) if meq else None), ('468', True, 'True'))
    notes += ['(468) %s' % l.strip() for l in o3.split(NL) if l.strip()]
    L = ['%s -- COMPONENT 1, (R321)(2): THE FOUR STRUCTURAL REPAIRS AND THE THREE ITEM REPAIRS AGAINST THEIR OLD FORMS, WITH THEIR CONTROLS (%s)' % (ACT, utc()), '',
         '### rows are cases: the section | the case | the reading got | the reading wanted | AS WANTED. The sections: (i) the events section and the',
         '### letters at the seal (standing clauses v2 row (52)); (ii) the membrane (row (53)); (iii) arms read structure (row (54)); (iv) controls that',
         '### can fail (row (55)); (k) the closing`s head-line builder; (i/step) G-SEALED-AFTER-COMPONENTS by the step bank; (468) the answer check.',
         '### The repaired forms read where they stand: tools/b711_checks.py (no_verdict_line_ok, report_lines_ok, joined, the trail arms, sealed_after_ok,',
         '### answers_plant, neg_shown, prev_run_missing), tools/b711_closing.py (head_line, events_section), tools/act_membrane.py, tools/b711_citation.py.', '']
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


# ================================================================================ COMPONENT 1: THE REPAIRS AND THEIR DIFFS, (R321)(2)
REPAIRS = (
    ('(52)', '(R321)(2)(i), THE EVENTS SECTION',
     'tools/b711_closing.py events_section (the section beneath the defects: data/b711_events.txt`s rows and the head-line builder`s failures); '
     'tools/b711_checks.py the three trail-equality arms and G-TRAIL-DEFECTS-EQUAL`s Defects line read S[letters_seal], the letters entered before '
     'the seal, and the seal records them (`letters`, `defects_sha256`); tools/b711_record.py letters_of, letters_at_seal (the seal`s list, or for '
     'an act sealed before the repair its defects bank at the seal`s relay head), the defects route refusing a letter after the seal; EXCLUDE_KINDS '
     'events and steps. Control: data/b711_repair_controls.txt (i) -- the ruling`s control NOT AS WANTED on b710`s banks, defect (d)'),
    ('(53)', '(R321)(2)(ii), THE MEMBRANE',
     'tools/act_membrane.py (new, shared, whole below): appended, named, refuses, guard, guard_path; tools/b711_record.py b698`s put_json and '
     'put_txt wrapped and rebound in b703`s to b710`s modules; the guard before every bank write of tools/b711_citation.py (its two writers and '
     'the answer route`s rewritten body), tools/b711_closing.py, tools/b711_checks.py, tools/b711_independence.py, tools/b711_standing.py, '
     'tools/b711_tests.py and tools/b711_carry.py. THE READING, FOR THE AUTHOR`S STRIKE: "a named bank" is a bank the act`s root names (b710`s (j) '
     'quotes its ferry: "no named bank written after it") -- every file directly under relay data/ that the act`s ROOT_EXCLUDE does not take out; '
     'the mirror builder`s banks pass by name (the b670 form); the closing, its censuses and pins, the push captures, the defects, events and step '
     'banks are excluded kinds and stay writable after the root. Control: (ii) -- a test root refuses, a locator call leaves git status unchanged'),
    ('(54)', '(R321)(2)(iii), ARMS READ STRUCTURE',
     'tools/b711_checks.py no_verdict_line_ok (the gate`s NO VERDICT LINE rows read by the bank each names, NO_VERDICT_EXEMPT`s list of names '
     'removed -- the carry had turned b710`s entry into data/b710_prints_v0.17.txt, a bank that does not exist); report_lines_ok and '
     'report_unsealed_ok reading data/b711_report.json (its `at` and `lines`); joined kept for the registrations (no JSON bank); `--prev --part <p>` '
     'runs a part`s arms on b710`s banks (_prev_rebind, _PrevWorklist) and banks data/b711_prevrun_<part>.txt and data/b711_prevrun_exercise_<part>.json '
     'beside b710`s own verdicts (_prev_verdicts); the seal refuses while a part`s run is not banked (prev_run_missing). Control: (iii) -- the three '
     'needles pass on their acts` honest output and their NEG copies fail'),
    ('(55)', '(R321)(2)(iv), CONTROLS THAT CAN FAIL',
     'tools/b711_checks.py: the main loop records per arm `pos_raised` and `shown_failing` and per part the run`s `mode`, `at` and relay head; '
     'neg_shown reads the pre-run`s exercise banks; seal() refuses, recording nothing, while any arm`s mutated copy has not been shown failing '
     '(passed, raised, or no pre-run row); G-ANSWERS-BEFORE-WRITES`s plant answers_plant moves every check stamp after the write it governs. '
     'Control: (iv) -- b710`s plant leaves the arm passing, the repaired plant fails it'),
    ('(k)', 'THE CLOSING`S HEAD-LINE BUILDER (b710`s (k))',
     'tools/b711_closing.py head_line and _captures: each repository`s record commit the main its last capture of the act read back (the closing`s '
     'own excluded, ordered by the captures` stamps); a capture-name failure goes to HEAD_EVENTS and the events section, never the head line. '
     'Control: (k) -- over b710`s captures the line reads relay 2c200e8d, PLACE-papers df2dd7c, the two failures in the events section'),
    ('(i)', 'G-SEALED-AFTER-COMPONENTS BY THE STEP BANK (b710`s (i))',
     'tools/b711_record.py step (data/b711_steps.json: the repository, the commit, its time, the phase named from STEP_PHASES), PRE_SEAL_PHASES; '
     'tools/b711_checks.py sealed_after_ok and _step_phase reading the bank, not the subjects. Control: (i/step)'),
    ('468', 'THE CITATION TOOL`S ANSWER CHECK',
     'tools/b711_citation.py answer: b682`s cut `best.find(\'END\', k)` replaced by `best.rfind(\'END\')` in the rewritten body (checked to occur '
     'once); the replay route prints both cuts. Control: (468) -- b710`s root answer, 468 characters by b682`s cut, 1554 by the repaired, equal to '
     'the text from its BEGIN to its last END'),
)
REPAIR_TRACKED = ('tools/b711_record.py', 'tools/b711_citation.py', 'tools/b711_independence.py', 'tools/b711_standing.py', 'tools/b711_tests.py',
                  'tools/b711_carry.py', 'tools/b711_worklist.py')
REPAIR_CARRIED = ('checks', 'closing')


def toolrepairs(*a):
    """data/b711_tool_repairs.txt (.json), Component 1, (R321)(2): each repair's row (the delta's row of standing clauses v2, its objects, its
    control's section in data/b711_repair_controls.txt); the diffs: the tools committed at step zero (relay 4aa6e281) by `git diff HEAD`, the
    carried tools by their repairdiff banks (tools/b711_carry.py repairdiff), the new shared tool tools/act_membrane.py whole."""
    ctl = jl('%s_repair_controls.json' % ACT)
    if not ctl.get('cases'):
        sys.exit('### data/b711_repair_controls.json IS NOT WRITTEN -- THE CONTROLS FIRST; NOTHING WRITTEN')
    nw = [c for c in ctl['cases'] if not c.get('as_wanted')]
    L = ['%s -- COMPONENT 1, (R321)(2): THE FOUR STRUCTURAL REPAIRS (STANDING CLAUSES v2 ROWS (52)-(55)) AND THE THREE ITEM REPAIRS, WITH THEIR DIFFS (%s)' % (ACT, utc()), '',
         '### rows are repairs: the row | what is repaired | its objects, the reading and its control. The controls: relay data/b711_repair_controls.txt',
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


# ================================================================================ COMPONENT 2, (R321)(4): THE PORT (b709's portedit, portdispatch and portrun, :1745-:1932, carried)
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


def portedit(*a):
    """data/b711_port_edit.txt (.json): the line (R321)(4) names, printed BEFORE the one commit -- :212 as it stood at b709's tip 92af8a34 and as
    the Edit tool left it, to the signature data/b709_port.txt :40-:47 reads (WeakFEPair.hasMellin wants the hypothesis `k < re s` where the
    kernel passed `w`), in b709's form at C7OrderBounds.lean :277 (the strong pair's hasMellin, which takes `s` alone; its error cleared at b709's
    run); the diff of the module against the tip by git diff, one hunk; every other tracked file unchanged (git status)."""
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
    L = ['%s -- COMPONENT 2, (R321)(4): THE PORT`S LINE :%d ON %s, PRINTED BEFORE THE ONE COMMIT (%s)' % (ACT, K.PORT_LINE, K.PORT_BRANCH, utc()), '',
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
    tree state (refused where data/b711_dispatches.json carries the tree), at most two dispatches this act ((R321) N1), the branch's tip read back
    at the remote by one ls-remote before the dispatch; the host's free memory printed before it and the hold read ((R321)(8))."""
    label, target = a[0], a[1]
    repo = 'psinary-sketch/' + K.KERNEL
    full = g(LV, 'rev-parse', K.PORT_BRANCH).strip()
    tree = g(LV, 'rev-parse', full + '^{tree}').strip()
    j = jl('%s_dispatches.json' % ACT) if os.path.isfile(os.path.join(D, '%s_dispatches.json' % ACT)) else {}
    rows = j.get('rows') or []
    seen = [r for r in rows if r.get('tree') == tree]
    if seen:
        sys.exit('### THE TREE %s IS ALREADY BUILT (run %s) -- NOT DISPATCHED' % (tree[:12], seen[0].get('run_id')))
    if len(rows) >= 2:
        sys.exit('### TWO DISPATCHES ALREADY MADE THIS ACT ((R321) N1) -- NOT DISPATCHED')
    if not re.match(r'^[A-Za-z0-9_. ]+$', target):
        sys.exit('### THE TARGET %r IS OUTSIDE THE LAKE GRAMMAR -- NOT DISPATCHED' % target)
    remote = (g(LV, 'ls-remote', 'origin', 'refs/heads/' + K.PORT_BRANCH).split() or [''])[0]
    import b711_tests as TT
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
    (R321)(4). data/b711_port.txt (.json)."""
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
    L = ['%s -- COMPONENT 2, (R321)(4): THE PORT RUN OF SIDE-lv-conservation ON %s AT ITS NEW TIP, READ BY ITS RUN ID; THE OUTCOME BY FILE AND LINE (%s)' % (ACT, K.PORT_BRANCH, utc()), '',
         '### the dispatch: the branch %s at its tip (this act`s one commit on b709`s %s), the workflow at the branch, target SIDELvConservation (data/b711_dispatches.json)' % (K.PORT_BRANCH, K.PORT_TIP[:8]),
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
          '### where the build completes: %s' % ('THE BUILD COMPLETES, 12 of 12 -- (R321)(4): Register4_positivity read at 93c27ec and at the tip, the join`s lakefile re-pinned, one join dispatch'
                                                  if complete else 'not complete at this run; (R321)(4)`s join not reached, its dispatch not made'),
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
    put_txt('%s_port.txt' % ACT, L)
    if agree:
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, K.KERNEL, label), blog.rstrip(NL).split(NL))
    put_json('%s_port.json' % ACT, dict(at=utc(), run_id=run_id, run=run, artifact=dict(id=art.get('id'), name=art.get('name'), sha256=sha, digest=digest, agree=agree), ref_built=ref_built,
                                        mem_low=mem_low, stopped=stopped, build_exit=bexit, errors=errors, built=built, held=held, first_error=first_err, kinds=kinds, remaining=remaining,
                                        modules=list(LV_MODULES), grade_claimed=False, complete=complete))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (K.KERNEL, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[2:10] + L[-1:]))


PORT_TAG_HEAD = '*Appended 2026-10-25 by b711 beneath b710’s trail record (:15808), under `(R321)`(4) -- THE ORDER **`W-ORD-LV-PORT-TAG`**, FOR THE AUTHOR’S WORD:*'


def c2order(*a):
    """`c2order [dry]`: (R321)(4) -- "The naming of the port's tip in lv-conservation's tags entered as W-ORD-LV-PORT-TAG for the author's word, no
    lv tag this act": one OPEN_TRAILS record through b698's guarded landing, every figure read from data/b711_port.json and data/b711_port_edit.json
    and the kernel's refs (the port's tip, lv's main and the deposit's tag read back, each against the worklist)."""
    pj, ej = jl('%s_port.json' % ACT), jl('%s_port_edit.json' % ACT)
    tip = g(LV, 'rev-parse', K.PORT_BRANCH).strip()
    main = g(LV, 'rev-parse', 'main').strip()
    dep = g(LV, 'rev-parse', 'v0.10.0^{commit}').strip()
    tags_at_tip = [t for t in (g(LV, 'tag', '--points-at', tip) or '').split(NL) if t.strip()]
    fe = pj.get('first_error') or ''
    m = re.match(r'^error: (SIDELvConservation/\w+\.lean):(\d+):(\d+): (.*)$', fe)
    after = [k for k in (pj.get('kinds') or [])[1:]]
    bad = [k for k, v in (('the run read', pj.get('run_id') and (pj.get('artifact') or {}).get('agree')), ('the edit as ordered', ej.get('ok') is True),
                          ('the tip built', (pj.get('run') or {}).get('headSha') == tip), ('lv main', main == K.LV_MAIN), ('the deposit', dep == K.LV_V0100),
                          ('no tag at the tip', not tags_at_tip), ('the failing line', m), ('not complete', pj.get('complete') is False)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING LANDED' % bad)
    text = (NL + PORT_TAG_HEAD + ' the naming of the port’s tip in SIDE-lv-conservation’s tags. The port at b711: %s at %s '
            '(b709’s %s with one edit at %s :%d to the strong pair’s hasMellin, b709’s form at C7OrderBounds.lean :277, relay data/b711_port_edit.txt), '
            'its one run %s read by its id (relay data/b711_port.txt, the artifact’s sha256 %s… equal to the platform’s digest): %d of 12 modules built, '
            '%s held at :%s:%s (%s, %s)%s. The join (W-ORD-LV-CLOSURE-JOIN, :%d) is not reached: SIDE-faces-join’s lakefile is not re-pinned, no join '
            'is dispatched and no tag is made. No lv tag at b711: SIDE-lv-conservation’s main (%s) and its deposit v0.10.0 (%s) untouched, the tip '
            'carrying no tag. Where the port builds 12 of 12 and the join derives, the tip’s name among lv’s tags is the author’s to give. Status OPEN.' % (
                K.PORT_BRANCH, tip[:8], K.PORT_TIP[:8], K.PORT_FILE.split('/')[-1], K.PORT_LINE, pj['run_id'], pj['artifact']['sha256'][:16],
                len(pj.get('built') or []), m.group(1).split('/')[-1], m.group(2), m.group(3), m.group(4).strip(), pj['kinds'][0][1],
                ('; after it ' + ', '.join(':%s (%s)' % (re.search(r'\.lean:(\d+:\d+):', l).group(1), k) for l, k in after)) if after else '',
                K.ORDER_LV_JOIN, main[:8], dep[:8]) + NL)
    land([('OPEN_TRAILS.md', PORT_TAG_HEAD, text)], '%s_order_lines.json' % ACT, 'order', entry=None, dry='dry' in a)
    if 'dry' in a:
        print(conv(text))


# ### stage one (step zero): b710's Component routes over its own objects pruned (data/b711_prune_record.txt); this act's are added by the Edit tool
ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              ksyms=ksyms, defs=defs, figures=figures, runner=runner,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry, linecheck=linecheck,
              step=step, c1=c1, repairctl=repairctl, toolrepairs=toolrepairs, portedit=portedit, portdispatch=portdispatch, portrun=portrun, c2order=c2order)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b711_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
