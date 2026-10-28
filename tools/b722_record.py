# -*- coding: utf-8 -*-
"""b722_record.py -- THE ACT'S RECORD TOOL, b722 under (R332).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b722 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers, b704's repaired read route and its probe, tie, quote and cut forms, b705's routes (the print-list dispatch, the artifact reader),
### b706's (the runner choosing the run's artifact by name, the prints branch, the probe-step artifact, the mentions re-read) and b721's (the
### declared untracked writes, the root route's dry run, the rowgen roster re-pointed, the previous window in b701's form) are reached through
### tools/b721_record.py (sealed at b721 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### Written by the Write tool at b722 in stages: stage one, step zero's routes (the tie among them); Components 1-6 by the Edit tool.
### Routes: `python tools/b722_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
### UNTRACKED WRITE: data/b722_bank_hashes.json (the hashes bank of (R332)(6)(i): every bank this tool writes, by its sha256, for N4's hand-edit read)
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

import b722_worklist as K          # noqa: E402
import b721_worklist as K707       # noqa: E402  ### b721's data, for the controls on b721's banks
import b721_record as P7           # noqa: E402  ### b721's tool, imported unedited (its import binds b698's R, b703's P3, b704's P4, b705's P5 and b706's P6 to b721: rebound below)
R, P3, P4, P5, P6 = P7.R, P7.P3, P7.P4, P7.P5, P7.P6   # ### b698's routes, b703's to b706's repaired readers, through b721's module

ACT, PREV = 'b722', 'b721'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b721 ran and closed in THIS session (3bbc6267; the ruling pasted after b721's closing, no /clear) -- b711's
# ### same-session form: from b721's post-push combine to this act's anchor (prev_capture below, K.PREV_SESSION the session itself)
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = PREV_SUBAGENTS
FACE = os.path.join(D, 'b722_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b722_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b721_relay_push-b721-closing_push_out.txt', 'b721_steps.json', 'b675_corrigenda.txt', 'standing_clauses_v5.txt',
                   'repo_visibility.txt')
R.N5_RELAY_TOOLS = ('mirror_prevbuild.json',)   # ### (R332)(2): the mirror builder's own state file, written at every build

# ### THE ROOT ROUTE'S EXCLUSION LIST (data/b706_rules.txt row (1)): the kinds b698's route excludes, carried; and every untracked write a
# ### b722_*.py tool declares in its own head, read at import. A tool declares one by a line `### UNTRACKED WRITE: data/b722_<name>`.
# ### (R332)(2): the events bank (row (52): a finding after the seal, written after the seal and after the root) and the step bank (G-SEALED-AFTER-
# ### COMPONENTS, a row per commit written after the commit, the record's and the closing's among them) are the defects bank's kind: not root items
EXCLUDE_KINDS = P7.EXCLUDE_KINDS + r'|events|steps|hook_refusals'   # ### (R332)(4)(iii): the standing hook's bank, an excluded kind
# ### b707's kind `chain_.*` (the suite's chain parts, `<act>_chain_half_<i>_<key>.json`) read as wide as every bank whose name opens `chain_`, so
# ### (R332)(7)'s data/b722_chain_rows.txt was excluded from the root (the suite's import check refused REQUIRED_BANKS on it); narrowed to the
# ### suite's own kind, `chain_half_.*`, the chain parts still excluded. A carry-time repair, banked by diff (data/b722_tool_repairs.txt).
EXCLUDE_KINDS = EXCLUDE_KINDS.replace('|chain_.*|', '|chain_half_.*|')
assert '|chain_half_.*|' in EXCLUDE_KINDS
# ### b721's declaration line read to its first space (b721: `\s*$`, which refused a declaration followed by prose and so read the grid's and the
# ### pairs' declarations as none -- the root's first dry run named 32 untracked units files); a name ending in `*` declares every file with that
# ### prefix (the grid's segment files, the pairs' band files). A carry-time repair, banked by diff (data/b722_tool_repairs.txt).
UNTRACKED_DECL = re.compile(r'^### UNTRACKED WRITE: data/b722_(\S+)', re.M)


def declared_untracked():
    """every b722_*.py tool's declaration of an untracked write (its units file, its download), read from the tools' own heads: [(tool, name)]."""
    out = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b722_') and f.endswith('.py'):
            for m in UNTRACKED_DECL.finditer(rd(os.path.join(T, f)) or ''):
                out.append((f, m.group(1)))
    return out


def _root_exclude():
    names = [(re.escape(n[:-1]) + r'\S*') if n.endswith('*') else re.escape(n) for _f, n in declared_untracked()]
    return re.compile(r'^b722_(' + EXCLUDE_KINDS + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


R.ROOT_EXCLUDE = _root_exclude()

# ### (R332)(2)(ii), standing clauses v2 row (53): THE MEMBRANE in the shared writers -- b698's put_json and put_txt (which every route of this
# ### tool and of b698's to b721's modules writes through) wrapped by tools/act_membrane.py's guard, which refuses a bank the root names once
# ### this act's root is appended to data/act_roots.txt; the mirror builder's banks and the root's exclusions pass (a repair at b722, banked by diff).
import act_membrane as MEM          # noqa: E402
# ### a carry-time repair at b722: b721's module rebound R's writers to its own wrappers, which guard b721 (rooted), so the originals are read
# ### from b721's capture of b698's writers and not from R (a wrapper over a wrapper refuses every bank once the previous root is appended)
_put_json0, _put_txt0 = getattr(P7, '_put_json0', R.put_json), getattr(P7, '_put_txt0', R.put_txt)


import act_close as AC             # noqa: E402  ### (R332)(4): the close's shared functions, one form for every tool (a repair at b722)


def _lock_guard(name):
    """(R332)(4)(iv), standing clauses v4 row (65): THE LOCK AS A MEMBRANE -- a bank of a step before the lock refuses a rewrite once the lock
    is written, as the root's membrane refuses after the root (a repair at b722, banked by diff)."""
    r = AC.lock_refuses(ACT, name)
    if r:
        print(r, flush=True)
        sys.exit(4)


HASHES = '%s_bank_hashes.json' % ACT   # ### (R332)(6)(i), v5 row (74): the hashes bank a hand edit is read against


def _hash_record(name):
    """(R332)(6)(i): the bank just written recorded by its sha256 (tools/act_close.py bank_hashes) in this tool's hashes bank, so a hand edit to
    it is read at N4 (hand_edits). The hashes bank is this tool's own write, outside the root (### UNTRACKED WRITE in the head)."""
    p, hp = os.path.join(D, name), os.path.join(D, HASHES)
    if name == HASHES or not os.path.isfile(p):
        return
    cur = json.load(open(hp, encoding='utf-8')) if os.path.isfile(hp) else {}
    cur[name] = AC.bank_hashes([p])[p]
    with open(hp + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(cur, indent=1, sort_keys=True) + '\n')
    os.replace(hp + '.tmp', hp)


def put_json(name, obj):
    MEM.guard(ACT, name, R.ROOT_EXCLUDE)
    _lock_guard(name)
    _put_json0(name, obj)
    _hash_record(name)


def put_txt(name, lines):
    MEM.guard(ACT, name, R.ROOT_EXCLUDE)
    _lock_guard(name)
    _put_txt0(name, lines)
    _hash_record(name)


R.put_json, R.put_txt = put_json, put_txt
for _m in (P3, P4, P5, P6, P7, getattr(P7, 'P7', None)):   # ### b703's to b721's modules bound b698's writers at their own import
    for _n, _f in (('put_json', put_json), ('put_txt', put_txt)):
        if _m is not None and hasattr(_m, _n):
            setattr(_m, _n, _f)


def rootexclude(*a):
    """prints the declared untracked writes and the exclusion pattern they extend; writes nothing."""
    decl = declared_untracked()
    for f, n in decl:
        print('  %-28s declares data/b722_%s untracked' % (f, n))
    print('  DECLARED UNTRACKED WRITES %d ; ROOT_EXCLUDE %s' % (len(decl), R.ROOT_EXCLUDE.pattern))


_R_anchor_ts = P7._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704 to b721


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

# ================================================================================ b703'S TO b721'S REPAIRED READERS, THROUGH b721'S MODULE
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
roster709 = P7.roster709                        # ### b707's rowgen roster re-pointed through data/b706_partners.json (the fourth path reader), through b721's module (a carry-time repair: the substitution shifted b721's own name for it)


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried; rowgen's roster b721's)
answers = R.answers


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables, each at the file of record after b706's renames (b721's roster707); each tool's verdict lines
    banked with its exit. data/b722_rowgen_<stage>.txt."""
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
         '((R316)(3): %d of the bank`s paths re-pointed from the retired versioned name, data/b706_partners.json, b721`s reader) ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), len(moved), secs), '']
    L += ['### re-pointed: %s -> %s' % (f, p) for _n, f, p in moved]
    L += ['', '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19 ; RE-POINTED %d.**' % (con.returncode, dif.returncode, len(moved))]
    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)
    print(NL.join(L[-14:]))


# ================================================================================ (R332)(2)(i), STANDING CLAUSES v2 ROW (52): THE LETTERS AT THE SEAL
def letters_of(text):
    """the lettered rows of a defects bank's text, each '(x) HEAD' by b703's row reader (pure in its argument)."""
    L = (text or '').replace(chr(13), '').split(NL)
    return [s for s in (read_defect_row(L, i) for i, l in enumerate(L) if DEFECT_ROW.match(l)) if s]


def _letter(s):
    m = re.match(r"^\(([a-z]'?)\)", s or '')
    return m.group(1) if m else None


def letters_at_seal(act):
    """the letters entered before the seal: the list the suite's seal records with the hashes (data/<act>_seal_hashes.json `letters`, from b722);
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
    """data/b722_defects.json from the bank; after the seal (row (52)) it refuses a letter the seal did not record: a finding after the seal is
    entered in data/b722_events.txt for the closing's events section, and the next act's corrigendum letters it."""
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    seal = letters_at_seal(ACT)
    if seal is not None:
        late = [s for s in letters_of(t) if _letter(s) not in set(_letter(x) for x in seal)]
        if late:
            sys.exit('### (R332)(2)(i): %d LETTER(S) ENTERED AFTER THE SEAL (%s) -- A FINDING AFTER THE SEAL IS AN EVENT, ENTERED IN data/%s_events.txt, '
                     'NOT A LETTER -- NOTHING WRITTEN' % (len(late), ', '.join(s[:3] for s in late), ACT))
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ (R332)(2): THE ACT'S STEP BANK (G-SEALED-AFTER-COMPONENTS reads it)
# ### (R332)(3)(ii): 'gate' -- the commit of the gate before the lock, the one commit the face cannot carry (it stamps the face); the suite's
# ### G-NOTHING-RAN-AHEAD reads it from this bank and asks every other commit before the lock to be declared on the face by its hash
PRE_SEAL_PHASES = ('step zero', 'component 1', 'component 2', 'component 3', 'component 4', 'pilot', 'component 5', 'component 6', 'component 7', 'component 8', 'gate')  # pilot: b721's word (2); component 8: act_current.json's Component 8 phases name it (its pre-gate commits); component 7: b722's pre-gate commits of Component 7 (data/act_current.json's component 7 phases), b721's in its component 6
POST_SEAL_PHASES = ('seal', 'pre-root', 'root', 'record', 'closing')
STEP_PHASES = PRE_SEAL_PHASES + POST_SEAL_PHASES
STEP_REPOS = dict(relay=ROOT, pp=PP)


def step(*a):
    """`step <relay|pp> <phase words> [commit ...]`: one row appended to data/b722_steps.json after a step's commits -- the repository, the
    commits (HEAD where none is named), the last one's committer time and subject as read, and the phase the seat names from STEP_PHASES;
    G-SEALED-AFTER-COMPONENTS reads the phase and not the subject. (R332)(4)(ii), standing clauses v4 row (63): EVERY COMMIT OF A STEP -- a
    step of several commits is one row carrying the list of them (`commits`), `commit` its first, and every arm reads the list through
    tools/act_close.py step_commits (a repair at b722). A commit already in the bank is not entered twice."""
    if len(a) < 2 or a[0] not in STEP_REPOS:
        sys.exit('### step <relay|pp> <phase> [commit ...] -- the phases: %s' % ' | '.join(STEP_PHASES))
    rest = list(a[1:])
    commits = []
    while rest and re.match(r'^[0-9a-f]{7,40}$', rest[-1]):
        commits.insert(0, rest.pop())
    commits = commits or ['HEAD']
    phase = ' '.join(rest)
    if phase not in STEP_PHASES:
        sys.exit('### THE PHASE %r IS NOT ONE OF %s -- NOTHING WRITTEN' % (phase, ' | '.join(STEP_PHASES)))
    fulls = []
    for commit in commits:
        full = g(STEP_REPOS[a[0]], 'rev-parse', '--verify', '--quiet', commit + '^{commit}').strip()
        if not full:
            sys.exit('### %s IS NOT A COMMIT OF %s -- NOTHING WRITTEN' % (commit, a[0]))
        fulls.append(full)
    ct, subj = g(STEP_REPOS[a[0]], 'log', '-1', '--format=%ct%x09%s', fulls[-1]).strip().split('\t', 1)
    j = jl('%s_steps.json' % ACT)
    rows = j.get('rows') or []
    have = set(AC.step_commits(rows, repo=a[0]))
    dup = [f[:8] for f in fulls if f in have]
    if dup:
        sys.exit('### %s %s IN THE STEP BANK ALREADY -- NOTHING WRITTEN' % (a[0], dup))
    row = dict(repo=a[0], commit=fulls[0], ct=int(ct), at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(ct))), phase=phase, subject=subj[:120])
    if len(fulls) > 1:
        row['commits'] = fulls
    rows.append(row)
    put_json('%s_steps.json' % ACT, dict(at=utc(), rows=rows))
    print('  step %d: %s %s %s -- %s' % (len(rows), a[0], ' '.join(f[:8] for f in fulls), rows[-1]['at'], phase))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R332)(8); b721's form)
def branches(*a):
    """`branches before`: data/b722_branches_before.json -- b698's route, carried (every branch (R332)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b722_branches.txt (.json) --
    each branch's fate read now against the tips banked before; the kept branch port-b707 read beside them."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b722_branches_before.json IS NOT WRITTEN -- NOTHING READ')
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
    L = ['%s -- STEP ZERO, (R332)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b722_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. (R332)(7) names relay`s four and PLACE-papers` two; port-b707 of',
         '### SIDE-lv-conservation is NOT deleted, local or remote, read beside them.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['  %-22s | %-28s | kept   | local %s ; remote %s ; %s' % (os.path.basename(krepo), kb, kept_local[:12] or 'absent', kept_remote[:12] or 'absent',
                                                                'STANDS' if kept_local == kept_remote == K.PORT_TIP else '### NOT AS KEPT')]   # ### a carry-time repair: b721's tip, K.PORT_TIP
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
    offence. data/b722_read_calls.txt."""
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
    mod = {'b698': R, 'b703': P3, 'b704': P4, 'b705': P5, 'b706': P6, 'b721': P7}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
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


# ================================================================================ THE LATE ROUTES (b721's, carried with b722's names; the previous window in its own session)
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
    """G-EDIT-ROUTE's window over the previous act, b701's form for a previous act in ITS OWN session (b721's carry-time repair, carried): b721's
    capture AFTER ITS POST-PUSH SUITE -- every command of session 0be08567 from the call that combined b721's post-push parts into
    data/b721_checks_postpush.txt to that session's end, its closing's commands among them; this act runs in a session of its own."""
    rows = ER.capture(PREV_SESSION_PATH, K.PREV_ANCHOR, PREV_SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    # ### Component 8, the Edit tool: b721 ran in THIS session (:47-:48), so its window ends where this act's capture begins (the first command
    # ### after 'RULING (R332) BEGIN'), b711's same-session form; the carried '9999' (the own-session form) read this act's commands as b721's
    own = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    if not own:
        sys.exit('### THIS ACT`S CAPTURE IS EMPTY -- THE PREVIOUS ACT`S WINDOW HAS NO END -- NOTHING READ')
    anchor = min(r['ts'] for r in own)
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
# ### b721's pattern read `_record.py dispatch`; this act's one dispatch ran through the `portdispatch` route, so the pattern takes the port prefix too
# ### (a carry-time repair, banked by diff: the command bank's first write read DISPATCHES 0 against the dispatch bank's one row)
# ### b722: the rebuild's dispatches run inside its tool (b722_rebuild.py dispatch <k>, and push_run <k> for SIDE-frobenius's run on push, the
# ### author's two lines), read by its routes; each anchored at a command's head running the tool, its path relative or absolute: the capture
# ### also holds commands the hook refused, which name the routes in their text (Component 8, the Edit tool; b721's pattern named the challenge
# ### and pin tools)
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)'
                          r'|(^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b722_rebuild\.py (?:dispatch|push_run)\b', re.M)


def commands(*a):
    """b721's route with b722's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window (b721's
    session from its post-push combine to its end), the local lean reading (N1), the dispatches (two ordered: the probe branch and the prints
    branch), the detached runs, sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound requests.
    data/b722_commands.txt (.json)."""
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
    L += ['', '### THE RUNNER DISPATCHES ((R332)(7)(iii) and N1: the rebuild`s one per wave 1 kernel through tools/b722_rebuild.py dispatch, SIDE-frobenius`s run on push through push_run) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R332)(8) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel written this act, the %s branches of the six wave 1 kernels kept as b721 pushed them ((R332)(11)); SIDE-lv-conservation`s main '
          'untouched, port-b707 at b712`s tip %s, its checkout at main for this read)' % (len(ks), K.JOIN_NEW_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))


def _standing():
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B711_FACE.split('/')))) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))   # ### a carry-time repair: the previous face b721's (K.B711_FACE; the substitution left b709's name, absent from this act's worklist)


R._standing = _standing


def standing(*a):
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, mbuild, mroot, mverify = R.desk, R.mbuild, R.mroot, R.mverify


def gatebanks(*a):
    """b698's route (tools/b698_record.py :1943, unedited), carried by the Edit tool with one change, b715's author's word (3)(a)
    (data/b715_author_words_preseal.txt (3)): the pins bank the lock gate reads runs `b303_pins.py gate <act>`. The reg gate's record is written before this route runs."""
    import gate_hash as G

    def runb(args, out):
        r = subprocess.run([sys.executable, '-X', 'utf8'] + args, capture_output=True, cwd=ROOT)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], '%s_reg_termscan.txt' % ACT)
    rc2, t2 = runb([os.path.join(T, '%s_regspec.py' % ACT)], '%s_regspec_run.txt' % ACT)
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/%s_satisfiable.json' % ACT, '--emit', ACT], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_%s_reg_satisfiable.txt' % ACT).split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', '%s_census_stepzero.txt' % ACT), ('b327_faces_census.py', '%s_faces_census_stepzero.txt' % ACT),
                      ('b303_pins.py', '%s_pins_stepzero.txt' % ACT)):
        rc, t = runb([os.path.join(T, tool)] + (['gate'] if tool == 'b303_pins.py' else []) + [ACT], out)   # ### b715's word (3)(a): the gate route
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/%s_reg_gate.txt' % ACT, 'data/%s_reg_termscan.txt' % ACT, 'data/%s_regspec_run.txt' % ACT, 'data/audit_%s_reg_satisfiable.txt' % ACT):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


def _one_git_write():
    """(R332)(2)(ii), tools/standing/ v1.2.1: one git write per message, counting WRITES -- each call split into its commands, a listing
    never a write (tools/standing/gitwrite.py) -- over the calls tools/rule_arms.py's sources read for this act (b698's window, unedited)."""
    import rule_arms as RA
    sys.path.insert(0, os.path.join(T, 'standing'))
    import gitwrite as GW
    lock = R._iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(R.FACE)) or [None, ''])[1])
    try:
        S = RA.sources(R.ACT, R.SESSION, K.ANCHOR, K.PARTS, lock, K.PRE_RELAY, K.PRE_PP)
        ok, _n, _over, note = GW.reading(S['calls'])
    except Exception as e:
        return False, 'the rule arm`s sources raised %s' % type(e).__name__
    return ok, note[:200]


def rootdry(*a):
    """data/b706_rules.txt row (1): the root route run DRY on the pre-root tree before the seal -- the banks the route names (ROOT_EXCLUDE
    extended), each read for CR LF, its status and its blob at HEAD; READY where every named bank is clean and equal at HEAD and none is CR LF
    (the push clause, HEAD the remote main, printed beside and not required before the record`s push). data/b722_root_banks_dry.txt (.json)."""
    _close_step(2)   # ### standing clauses v7 row (79): the root's dry run, step [2]
    banks = root_banks()
    s = root_banks_state(banks)
    crlf = [b_ for b_ in banks if os.path.exists(os.path.join(ROOT, *b_.split('/'))) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    missing = [b_ for b_ in banks if not os.path.exists(os.path.join(ROOT, *b_.split('/')))]
    ready = bool(s['rows']) and s['clean'] and not crlf and not missing
    L = ['%s -- THE ROOT ROUTE`S DRY RUN ON THE PRE-ROOT TREE BEFORE THE SEAL (data/b706_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are the banks the root route names (tools/b698_record.py root_banks with ROOT_EXCLUDE rebound at tools/b722_record.py, extended by',
         '### every declared untracked write: %s): status ; carried by HEAD ; HEAD`s blob equal to the file ; CR LF.' % (
             [n for _f, n in declared_untracked()] or 'NONE DECLARED'),
         '### HEAD %s ; the remote main %s ; equal %s (the push clause, read beside: the record`s push comes after the seal)' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %-5s crlf %s' % (r['bank'], r['status'], r['at_head'], r['equal'], r['bank'] in crlf) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; CR LF %s ; MISSING %s ; HEAD THE REMOTE MAIN %s ; THE DRY RUN READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), crlf or 'NONE', missing or 'NONE', s['pushed'], ready)]
    put_txt('%s_root_banks_dry.txt' % ACT, L)
    put_json('%s_root_banks_dry.json' % ACT, dict(at=utc(), ready=ready, crlf=crlf, missing=missing, declared=declared_untracked(), **s))
    print(L[-1])


# ================================================================================ STEP ZERO: THE LICENSED TABLE'S NEXT DOCUMENT, (R332)(6) (b704's tie form)
SUMMARY = re.compile(r'### ### \*\*(\w+): CLAIMS (\d+) ; SKIPPED LINES (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)')


def tie(*a):
    """data/b722_tie.txt: (R332)(6), the licensed table's next document -- b652's order, b674's tie-break rule and data/b705_rules.txt row (2)
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
    L = ['%s -- STEP ZERO, (R332)(6): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER, b674`S TIE-BREAK RULE AND b705`S ROW (2) PRINTED BEFORE IT IS NAMED (%s)' % (ACT, utc()), '',
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
            L.append('    (ii) a declared suite failure on either document: NONE (no arm of b721`s suite names either; data/b721_checks.txt)')
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


# ================================================================================ COMPONENT 2: THE PROBE THROUGH THE WORKFLOW'S STEP, (R332)(4)
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
    """b705's _print_modules (tools/b705_record.py :732) with the carry-time repair of this act (data/b722_tool_repairs.txt row (1)): a hit under a
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
    """`runner <kernel> <run id> <ref> <label> <note...>`: b706's runner706 carried with b722's names -- the run's artifact chosen BY NAME
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
# ================================================================================ COMPONENT 5: THE FOUR STANDING FIGURES (b706`s tool, unedited, against b721`s baselines)
def figures(*a):
    """data/b722_standing_figures.txt (.json): the four figures by relay tools/b706_standing_figures.py, unedited (correspondence() and partners()
    over b706's roster, data/b706_roster_read.json; readme() b705's, pins() b703's), each against b721's figure (data/b721_standing_figures.json),
    the pins baseline b721's rows."""
    import b706_standing_figures as SF6
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b721_standing_figures.json')
    f = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    pr = (f.get('partners') or {}).get('rows') or []
    cr = (f.get('correspondence') or {}).get('papers') or []
    L = ['%s -- COMPONENT 8: THE FOUR STANDING FIGURES AT b722, READ BY b706`S TOOL OVER b706`S ROSTER, AGAINST b721`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b706_standing_figures.py, unedited (correspondence() and partners() over data/b706_roster_read.json, the 20 tables at the',
         '### unversioned names; readme() tools/b705_standing_figures.py`s, pins() tools/b703_standing_figures.py`s), %.0f s; each arm fails on a' % (t1 - t0),
         '### regression from the previous act`s figure (data/b721_standing_figures.json). The re-cut %s merged into main at %s (b714`s), its branch deleted;' % (
             K.RECUT_BRANCH, K.RECUT_MERGE[:8]),
         '### the read is of PLACE-papers %s at %s; day1/Spectral_Inertness.md (cut at b708) is off the roster;' % (
             g(PP, 'rev-parse', '--abbrev-ref', 'HEAD').strip(), g(PP, 'rev-parse', '--short=8', 'HEAD').strip()),
         '### both kernels on main at the read (SIDE-lv-conservation`s checkout at main; port-b707 not checked out this act, b707`s trap).', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        L.append('  %-15s b722 %s ; b721 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE CORRESPONDENCE ROWS PER PAPER (current | behind | changed statement | unread ; the reason where the table is not read):']
    L += ['  %-36s %-66s current %3d behind %3d changed %3d unread %3d%s' % (p['paper'], p['path'], p['current'], p['behind'], p['changed'], p['unread'],
                                                                           (' ; ' + p['reason']) if p.get('reason') else '') for p in cr]
    L += ['', '### THE PARTNERS ROWS, ONE PER ROSTER TABLE:']
    L += ['  %-36s %-66s %s' % (r['paper'], r['path'], r.get('reason') or ('differing %s against %s' % (r.get('differing'), r.get('partner')))) for r in pr]
    one = sum(1 for r in pr if (r.get('reason') or '').startswith('ONE COPY'))
    L += ['', '### ### **FIGURES AT b722: CORRESPONDENCE %s ; README %s ; PARTNERS %s (ONE COPY %d OF %d TABLES) ; PINS %s -- AGAINST b721`S %s, %s, %s, %s ; THE ROSTER b706`S, %d TABLES.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), (f.get('partners') or {}).get('figure'), one, len(pr),
        (f.get('pins') or {}).get('figure'), (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'),
        (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'), len(cr))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), roster='b706_roster_read.json', baseline='b721_standing_figures.json',
                                                        **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:10] + L[-1:]))


def linecheck(*a):
    """`linecheck <record-lines bank> <i> <needle>...`: the suite's landed-line reading (tools/b703_checks.py landed) reproduced piece by piece and
    printed -- the bank's row, the ledger line at its number through the suite's own reader, conv(head), startswith and each needle; print only."""
    import b722_checks as CH
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
    print('### ### **K.<NAME> REFERENCES %d ; MISSING FROM b722_worklist %d: %s.**' % (len(seen), len(missing), missing or 'NONE'))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R332)(1)
WH = ('*Appended 2026-10-27 by b722 to b721’s entry (:%d), under `(R332)`(1) -- b721 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b721_closing.txt):*' % K.B711_ENTRY)   # ### b722: b721's entry read from K.B711_ENTRY (:10686); the carry left b715's line (:10582) as a literal


def _fig(text, pat, what):
    m = re.search(pat, text)
    if not m:
        sys.exit('### b721`S BANKS DO NOT CARRY %s (%s) -- NOTHING COMPOSED' % (what, pat))
    return m.groups() if m.groups() else (m.group(0),)


def _fl(name, pat, what):
    """a figure read from a b721 bank with the line it stands on: (groups, line)."""
    for i, l in enumerate(rdn(name).split(NL), 1):
        m = re.search(pat, l)
        if m:
            return (m.groups() if m.groups() else (m.group(0),)), i
    sys.exit('### data/%s DOES NOT CARRY %s (%s) -- NOTHING COMPOSED' % (name, what, pat))


def _wb_carried():
    """THE CARRIED FORM, NOT CALLED (kept for the diff, data/b722_tool_repairs.txt): b712's objects under b721's names by the carry's
    substitution -- the join, the port, the registrations -- banks b721 did not write. `_wb` below composes b721's own.
    b721's weight line under (R332)(1), every figure read from b721's banks by row and cited by its line: the head from its closing :1,
    the join (its statement at v0.1.0, its grade, its tag), the statement equality, the port, the throughstone, the registrations' one commit
    and their control, the price, the re-cut, the trail and the root, the chain, the scores at the close, the suite from its two banks, the
    mirror, the defects by the repaired reader and the events by their starting lines. A rewrite at b722: the carried form composed b711's
    objects (the pairs, the surgery, the axis, the list), none of them b721's (the repair banked by diff, data/b722_tool_repairs.txt)."""
    c = rdn('b721_closing.txt')
    head = c.split(NL)[0]
    fj = g(K.JOIN_DIR, 'show', 'v0.1.0:FacesJoin.lean').split(NL)
    if len(fj) < 29 or 'faces_join' not in fj[28]:
        sys.exit('### SIDE-faces-join FacesJoin.lean :29 AT v0.1.0 DOES NOT CARRY faces_join -- NOTHING COMPOSED')
    (run,), lrun = _fl('b721_join_grade.txt', r'the run (\d{11})', 'the join`s run')
    _x, lax3 = _fl('b721_join_grade.txt', r"'faces_join' depends on axioms: \[propext, Classical\.choice, Quot\.sound\]", 'the join`s axioms')
    _x, lder = _fl('b721_join_grade.txt', r'faces_join: GATE DERIVES', 'the join`s grade')
    (tobj, peel), ltag = _fl('b721_join_tag.txt', r'local: the tag object ([0-9a-f]{8})[0-9a-f]* ; peeled ([0-9a-f]{8})', 'the tag')
    _x, ltagr = _fl('b721_join_tag.txt', r'PEELED LOCAL 11a472b9 REMOTE 11a472b9', 'the tag read back')
    _x, lrp0 = _fl('b721_regpos.txt', r'between the two commits \(git diff\), 0 lines', 'the statement diff')
    _x, lrp = _fl('b721_regpos.txt', r'Register4_positivity: LINES 152 AND 152', 'the statement equality')
    (built,), lbu = _fl('b721_port.txt', r'THE BUILD COMPLETES, (\d+) of 12', 'the modules built')   # ### the dry form's needle read port1's :16 (11 of 12)
    _x, lthr = _fl('b721_report.txt', r'THE THROUGHSTONE FOR THE KERNEL FOOTING.*DIFFERS NONE ; REGRADE NONE', 'the throughstone')
    reg = g(ROOT, 'log', '--format=%H', '--', K.REGISTRATIONS).split()
    if reg != [K.REG_COMMIT]:
        sys.exit('### %s HAS COMMITS %s, NOT THE ONE %s -- NOTHING COMPOSED' % (K.REGISTRATIONS, [x[:8] for x in reg], K.REG_COMMIT[:8]))
    _x, lgc = _fl('b721_genus_control.txt', r'^\s*THE MISSES THROUGH n = 400: 0\s*$', 'the genus control')
    _x, lgp = _fl('b721_genus_control.txt', r'PLANTED CONTROLS BOTH F', 'the planted controls')
    (t1, t2), lpr = _fl('b721_price.txt', r'the first tier (\d\.\d+) hours ; the second tier (\d\.\d+) hours', 'the tiers')
    (bud,), lbud = _fl('b721_price.txt', r'about (\d+\.\d) foreground hours', 'the budget')
    (cut,), lcut = _fl('b721_price.txt', r'THE CUT FOR \(iii\): n <= (\d+)', 'the cut')
    (d0, d1), lrc = _fl('b721_recut_cut.txt', r'BEFORE (\d+), AFTER (\d+)', 'the re-cut`s distance')
    rtip = g(PP, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.RECUT_BRANCH).strip()
    if rtip != K.RECUT_COMMIT:
        sys.exit('### %s AT %s, NOT %s -- NOTHING COMPOSED' % (K.RECUT_BRANCH, rtip[:8], K.RECUT_COMMIT[:8]))
    ar = jl('b721_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b721_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    _x, lch = _fl('b721_checks_postpush_standing-b3.txt', r'b721 AGREE', 'the chain`s last act')
    _x, lsc = _fl('b721_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) REFUTED ; \(S1\) HELD \(S2\) HELD \(S3\) HELD', 'the scores at the close')
    n_pre, p_pre = _fig(rdn('b721_checks.txt'), r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the pre-push suite')
    n_post, p_post = _fig(rdn('b721_checks_postpush.txt'), r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the post-push suite')
    fails = re.search(r'LIVE FAILING : \d+ \[(.*?)\]', rdn('b721_checks_postpush.txt'))
    fails = ', '.join(re.findall(r"'([A-Z0-9-]+)'", fails.group(1))) if fails else 'NONE'
    (msha, nfiles), lmi = _fl('b721_closing.txt', r'sha256 ([0-9a-f]{8})[0-9a-f]* ; MANIFEST .* ; CLEAN ON ALL THREE CLAUSES.* the roster b711`s, (\d+) entries', 'the mirror')
    short = _defect_short('b721')
    evl = [i for i, l in enumerate(rdn('b721_events.txt').split(NL), 1) if re.match(r'^    [A-Z]', l)]
    if len(evl) != 9:
        sys.exit('### data/b721_events.txt READS %d STARTING LINES, NOT THE RULING`S NINE -- NOTHING COMPOSED' % len(evl))
    return (' “%s” (data/b721_closing.txt :1); “none read” because no push of the act wrote a capture (data/b721_events.txt :48, repaired at '
            '(R332)(4)(v)). As the banks confirm by row: faces_join, h2_sign ↔ SIDELvConservation.RegisterPentagon.Register4_positivity LiCoeff, at '
            'SIDE-faces-join FacesJoin.lean :29 at v0.1.0, built on run %s against lv-conservation at the port’s tip cb0aea56, #print axioms '
            '[propext, Classical.choice, Quot.sound], graded DERIVES from its statement, an equivalence between open statements, neither side proved '
            '(data/b721_join_grade.txt :%d, :%d, :%d); tag object %s, peeled %s, read back at the remote (data/b721_join_tag.txt :%d, :%d; FINDINGS '
            ':10380, :10390; FACES_LEDGER :547); Register4_positivity equal by statement at 93c27ec and at cb0aea56 (data/b721_regpos.txt :%d, :%d); '
            'the port at %s of 12 modules (data/b721_port.txt :%d); the throughstone (a)-(d) EQUAL, DIFFERS NONE, REGRADE NONE (data/b721_report.txt '
            ':%d); data/b721_registrations.txt committed alone at %s, its one commit, with its genus control as wanted (data/b721_genus_control.txt '
            ':%d, :%d); the price in data/b721_price.txt, tier one %s h, tier two %s h, the act’s budget %s h, the coefficient cut n <= %s '
            '(data/b721_price.txt :%d, :%d, :%d; FINDINGS :10394); day1/Silence_of_Foundations.md re-cut on %s %s, local, its distance by the b670 '
            'method %s to %s (data/b721_recut_cut.txt :%d); the entry at FINDINGS :%d; the trail at OPEN_TRAILS :%d carrying the root %s; the '
            'act-root chain b624-b721 AGREE (data/b721_checks_postpush_standing-b3.txt :%d); N1-N4 and S1-S3 HELD, N5 REFUTED on the scorer’s file '
            'list (data/b721_closing.txt :%d); suite %s of %s pre-push and %s of %s post-push, failing %s (data/b721_checks.txt :13, '
            'data/b721_checks_postpush.txt :13); the mirror mirror-refresh-2026-10-25-b721.zip (sha256 %s…) CLEAN on all three clauses over %s files '
            'with the root line (data/b721_closing.txt :%d); %d defects (a)–(%s) lettered before the seal (data/b721_defects.txt); %d events in '
            'data/b721_events.txt. Nothing deposited, nothing published.' % (
                head, run, lrun, lax3, lder, tobj, peel, ltag, ltagr, lrp0, lrp, built, lbu, lthr, K.REG_COMMIT[:8], lgc, lgp, t1, t2, bud, cut,
                lpr, lbud, lcut, K.RECUT_BRANCH, K.RECUT_COMMIT[:8], d0, d1, lrc, K.B711_ENTRY, K.B711_TRAIL, ar['root'][:8], lch, lsc, p_pre, n_pre,
                p_post, n_post, fails, msha, nfiles, lmi, len(short), _letter(short[-1]) if short else '-', len(evl)))


def _wb_carried713():
    """THE SECOND CARRIED FORM, NOT CALLED (kept for the diff, data/b722_tool_repairs.txt): b713's composer under b721's names by the carry's
    substitution -- the list, the predictions, the onsets, the coefficients, pair 7 -- banks b721 did not write (its first call would exit on
    data/b721_list.txt absent). `_wb` below composes b721's own. Its words as carried:
    b721's weight line under (R332)(1), in the clause's order, every figure read from b721's banks by row and cited by its line: the
    head from its closing :1 and the closing's commit from its step bank; the list's foot; the predictions' one commit and its ancestry to
    the onsets' commit; the onsets' rows and foot; Q0's two pairs at b711; the coefficients and the navigator's count; pair 7; Q0's list;
    the source pin; the faces head; the re-cut's check; the entry and the trail; the root and its banks; the scores; the suite; the mirror;
    the defects with their owners and the events by their starting lines. Written at b722 (the carried form composed b712's objects)."""
    c = rdn('b721_closing.txt')
    head = c.split(NL)[0]
    closing = [r for r in (jl('b721_steps.json').get('rows') or []) if r.get('phase') == 'closing']
    if len(closing) != 1:
        sys.exit('### data/b721_steps.json CARRIES %d CLOSING ROWS, NOT ONE -- NOTHING COMPOSED' % len(closing))
    (T, nb, nbc, on, off), llist = _fl('b721_list.txt', r'THE LIST COMPLETE TO ([\d.]+) ; BANDS (\d+) \(COMPLETE (\d+)\) ; ON-LINE ZEROS (\d+) ; '
                                       r'OFF-LINE PAIRS (\d+)', 'the list`s foot')
    pred = g(ROOT, 'log', '--format=%H', '--', 'data/b721_predictions.txt').split()
    if pred != [K.B713_PRED_RELAY]:
        sys.exit('### data/b721_predictions.txt HAS COMMITS %s, NOT THE ONE %s -- NOTHING COMPOSED' % ([x[:8] for x in pred], K.B713_PRED_RELAY[:8]))
    pfiles = sorted(g(ROOT, 'show', '--format=', '--name-only', K.B713_PRED_RELAY).split())
    if pfiles != ['data/b721_predictions.json', 'data/b721_predictions.txt']:
        sys.exit('### %s CARRIES %s, NOT THE PREDICTIONS ALONE -- NOTHING COMPOSED' % (K.B713_PRED_RELAY[:8], pfiles))
    anc = grc(ROOT, 'merge-base', '--is-ancestor', K.B713_PRED_RELAY, K.B713_ONSETS_RELAY) == 0
    if not anc:
        sys.exit('### %s IS NOT AN ANCESTOR OF %s -- NOTHING COMPOSED' % (K.B713_PRED_RELAY[:8], K.B713_ONSETS_RELAY[:8]))
    rows = [(i, float(m.group(1))) for i, l in enumerate(rdn('b721_onsets.txt').split(NL), 1)
            for m in [re.search(r'^\s*pair\s+\d+ \| .* \| ratio (\d\.\d+) \| HELD\s*$', l)] if m]
    (comp, held, ref, beyond), lfoot = _fl('b721_onsets.txt', r'PAIRS COMPUTED (\d+) ; HELD (\d+) ; REFUTED (\d+) ; BEYOND REACH (\d+)', 'the onsets` foot')
    _x, lwin = _fl('b721_onsets.txt', r'window \[0\.99, 1\.01\]', 'the window')
    if len(rows) != int(held) or ref != '0':
        sys.exit('### data/b721_onsets.txt READS %d HELD ROWS BESIDE ITS FOOT %s HELD, %s REFUTED -- NOTHING COMPOSED' % (len(rows), held, ref))
    (q11,), lq11 = _fl('b711_pairs.txt', r'^\s+11 \| .* n\*/F2 (\d\.\d+) \| .* \| WITHIN$', 'pair 11 at b711')
    (q15,), lq15 = _fl('b711_pairs.txt', r'^\s+15 \| .* n\*/F2 (\d\.\d+) \| .* \| WITHIN$', 'pair 15 at b711')
    (n0,), lc0 = _fl('b721_coeffs.txt', r'THE LEAST n WITH c\(n\) < 0: n = (\d+) ; c\(\d+\) = \(-6\) log 2 \+ \(-2\) log 3', 'the least index')
    (nneg,), lcn = _fl('b721_coeffs.txt', r'THE COUNT OF NEGATIVE COEFFICIENTS through 32532: (\d+) ;', 'the negatives through 32532')
    (n3000,), lc3 = _fl('b721_report.txt', r'through n = 3000 from the bank`s rows \(negative_list\) (\d+) beside \1 -- EQUAL', 'the count through 3000')
    _x, lp7 = _fl('b721_list.txt', r"^\s*band \[59\.881486, 75\.0\] \| N 18 .*\('1\.0259726162', '61\.422798308'\).* \| COMPLETE$", 'pair 7`s band')
    _x, lp7r = _fl('b721_report.txt', r'^\s*\(e\) PAIR 7`S ZERO WITH Re rho > 1', 'pair 7 in the report')
    _x, lq0 = _fl('b711_coeffs.txt', r'THE LEAST HEIGHT OF A ZERO WITH Re rho > 1: NONE IN THE LIST TO 325\.0', 'Q0`s list')
    _x, lpin = _fl('b721_source_pin.txt', r'AGREES', 'the source pin')
    _x, lfh = _fl('b721_closing.txt', r'THE FACES HEAD: FACES_LEDGER\.md :8 restated', 'the faces head')
    (rtip, f22, m0), lra = _fl('b721_closing.txt', r'ADDITIVE CHECK ON recut-b712-silence: at ([0-9a-f]{8}), found (\d+), missing (\d+), in order True', 'the re-cut`s check')
    _x, lra2 = _fl('b721_recut_additive.txt', r'FOUND 22 ; MISSING 0 ; IN ORDER True', 'the additive check')
    if not K.RECUT_TIP.startswith(rtip):
        sys.exit('### THE CLOSING`S RE-CUT TIP %s IS NOT %s -- NOTHING COMPOSED' % (rtip, K.RECUT_TIP[:8]))
    ar = jl('b721_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b721_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    (nbanks,), lbk = _fl('b721_closing.txt', r'THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1', 'the root`s banks')
    _x, lsc = _fl('b721_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD', 'the scores at the close')
    (n_pre, p_pre), lpre = _fl('b721_closing.txt', r'^\s*pre-push : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the pre-push suite')
    (n_post, p_post), lpost = _fl('b721_closing.txt', r'^\s*post-push : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the post-push suite')
    (msha,), lmi = _fl('b721_closing.txt', r'mirror-refresh-2026-10-25-b721\.zip ; \d+ bytes ; sha256 ([0-9a-f]{8})[0-9a-f]* ; .*Act root: b721 '
                       + ar['root'] + ' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    short = _defect_short('b721')
    owners = re.findall(r"^    \(([a-z])\) (THE [A-Z’' ]+?)S?:", rdn('b721_defects.txt'), re.M)
    if len(owners) != len(short) or any(o != "THE SEAT'" for _l, o in owners):
        sys.exit('### data/b721_defects.txt OWNERS %s BESIDE %d DEFECTS -- NOTHING COMPOSED' % (owners, len(short)))
    evl = [i for i, l in enumerate(rdn('b721_events.txt').split(NL), 1) if re.match(r'^\(\d+\) ', l)]
    if len(evl) != 16:
        sys.exit('### data/b721_events.txt READS %d STARTING LINES, NOT THE RULING`S SIXTEEN -- NOTHING COMPOSED' % len(evl))
    return (' “%s” (data/b721_closing.txt :1); its relay commit the record’s, the closing’s %s (data/b721_steps.json, the closing row). As the '
            'banks confirm by row: the −15 list complete to %s in %s bands (complete %s), %s on-line zeros and %s off-line pairs, the counts '
            'certified and the off-line points located (data/b721_list.txt :%d); data/b721_predictions.txt committed alone at %s, with its JSON, '
            'an ancestor of the onsets’ commit %s; the refined law met at %s of %s reachable pairs, ratios %.6f to %.6f against the registered '
            'window [0.99, 1.01] (data/b721_onsets.txt :%d-:%d, :%d, :%d); %s pairs beyond reach, owed no prediction; Q0’s pairs 11 and 15 met '
            'at b711 against b710’s committed predictions with the registered window [0.9, 1.1], ratios %s and %s (data/b711_pairs.txt :%d, :%d); '
            'the coefficients negative from n = %s, c(%s) = −2 log 24 (data/b721_coeffs.txt :%d), %s negatives through 3000 equal to the '
            'navigator’s value (data/b721_report.txt :%d), %s through 32532 (data/b721_coeffs.txt :%d); pair 7, Re ρ = 1.025973 at height '
            '61.422798, located by Newton at 200 bits with its band’s count certified (data/b721_list.txt :%d; data/b721_report.txt :%d); Q0 '
            'with no zero of Re ρ > 1 in its list to 325.0 (data/b711_coeffs.txt :%d); the genus factorization pinned at Murty–Osburn '
            'arXiv:math/0412237v1, Theorem 2.3, AGREES (data/b721_source_pin.txt :%d); FACES_LEDGER.md :8 restated (data/b721_closing.txt :%d); '
            'the re-cut’s additive check %s of 22 on recut-b712-silence %s, missing %s, pushed and not merged (data/b721_recut_additive.txt :%d; '
            'data/b721_closing.txt :%d); the entry at FINDINGS :%d; the trail at OPEN_TRAILS :%d; the root %s over %s banks chained from %s '
            '(data/b721_act_root.json; data/b721_closing.txt :%d); N1-N5 and S1-S3 HELD (data/b721_closing.txt :%d); suite %s of %s pre-push '
            'and %s of %s post-push (data/b721_closing.txt :%d, :%d); the mirror mirror-refresh-2026-10-25-b721.zip (sha256 %s…) CLEAN on all '
            'three clauses with the root line (data/b721_closing.txt :%d); %d defects (a)–(%s), all the seat’s (data/b721_defects.txt); %d '
            'events in data/b721_events.txt by their starting lines. Nothing deposited, nothing published.' % (
                head, closing[0]['commit'][:8], T, nb, nbc, on, off, llist, K.B713_PRED_RELAY[:8], K.B713_ONSETS_RELAY[:8], held, comp,
                min(r for _i, r in rows), max(r for _i, r in rows), rows[0][0], rows[-1][0], lwin, lfoot, beyond, q11, q15, lq11, lq15,
                n0, n0, lc0, n3000, lc3, nneg, lcn, lp7, lp7r, lq0, lpin, lfh, f22, rtip, m0, lra2, lra, K.B711_ENTRY, K.B711_TRAIL,
                ar['root'][:8], nbanks, ar['previous'][:8], lbk, lsc, p_pre, n_pre, p_post, n_post, lpre, lpost, msha, lmi, len(short),
                _letter(short[-1]) if short else '-', len(evl)))


def _wb():
    """b721's weight line under (R332)(1), every figure read from b721's own banks by row and cited by its line: the head from its closing
    :1 and the record's and the closing's commits from its step bank; the list's zeros and pairs; the predictions committed alone; the onsets
    HELD and REFUTED; the least negative coefficient and registration (ii); the companion and the hits; the eleven names; the suite pre-push
    and post-push; the counter; the mirror and its manifest control; the root; the ten events and the 25 defects. Written at b722 by the Edit
    tool: the carried composer (now _wb_b716_form, not called) read b716's banks under b721's names -- registrations, genus control,
    coverage, replay, keystone and pins banks b721 did not write -- and wanted nineteen events and eighteen defects."""
    c = rdn('b721_closing.txt')
    head = c.split(NL)[0]
    st = jl('b721_steps.json').get('rows') or []
    rec = [r for r in st if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r for r in st if r.get('phase') == 'closing']
    if len(rec) != 1 or len(clo) != 1:
        sys.exit('### data/b721_steps.json CARRIES %d RELAY RECORD ROWS AND %d CLOSING ROWS, NOT ONE EACH -- NOTHING COMPOSED' % (len(rec), len(clo)))
    (nzero, npair), lls = _fl('b721_list.txt', r'ON-LINE ZEROS (\d+) ; OFF-LINE PAIRS (\d+)', 'the list`s zeros and pairs')
    (npred, nbey), lpd = _fl('b721_predictions.txt', r'PREDICTED (\d+) .*BEYOND REACH AT T0` 200: (\d+)', 'the predictions')
    (nheld, nref), lon = _fl('b721_onsets.txt', r'HELD (\d+) ; REFUTED (\d+)', 'the onsets')
    (nneg, bneg), lco = _fl('b721_coeffs.txt', r'NEGATIVE FROM n = (\d+) .*b\(n\) = (-\d+)\)', 'the least negative coefficient')
    _x, lr2 = _fl('b721_coeffs.txt', r'REGISTRATION \(ii\) HELD', 'registration (ii)')
    (nsen, nker, nhld), lcm = _fl('b721_companion.txt', r'SENTENCES (\d+) ; ROWS \d+ ; KERNEL (\d+) ; HELD (\d+)', 'the companion')
    (nhit, nad, nfa), lli = _fl('b721_lint.txt', r'HITS (\d+) ; AS DESIGNED (\d+) .*FOR THE AUTHOR (\d+)', 'the hits')
    (nnm, nfd, nms), lnm = _fl('b721_names.txt', r'NAMES (\d+) ; FOUND AT A CURRENT TAG (\d+) ; MISSING (\d+)', 'the names')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    (n_pre, p_pre, f_pre), lpre = _fl('b721_closing.txt', suite % 'pre-push', 'the pre-push suite')
    (n_post, p_post, f_post), lpost = _fl('b721_closing.txt', suite % 'post-push', 'the post-push suite')
    (ncl, nco), lct = _fl('b721_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+)\s*$', 'the counter')
    _x, lmv = _fl('b721_mirror.txt', r'CLEAN ON ALL THREE CLAUSES', 'the mirror CLEAN')
    _x, lmc = _fl('b721_mirror.txt', r'NOT AS WANTED', 'the manifest control')
    ar = jl('b721_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b721_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    evr = [int(m.group(1)) for m in re.finditer(r'(?m)^    \((\d+)\) ', rdn('b721_events.txt'))]
    short = _defect_short('b721')
    owners = re.findall(r"^    \(([a-z])\) (THE SEAT'S|THE NAVIGATOR'S) \[", rdn('b721_defects.txt'), re.M)
    if evr != list(range(1, 11)) or len(short) != 25 or len(owners) != 25 or any(o != "THE SEAT'S" for _x, o in owners):
        sys.exit('### b721`S EVENTS %s AND DEFECTS %d (OWNERS %d) NOT THE CLOSING`S TEN AND 25 -- NOTHING COMPOSED' % (evr, len(short), len(owners)))
    return (' “%s” (data/b721_closing.txt :1); its relay commit the record’s %s, the closing’s %s (data/b721_steps.json, the record and '
            'closing rows). As the banks confirm by row: the -39 list to height 200 at %s zeros on the line and %s off-line pairs located, '
            'the rectangles not certified (data/b721_list.txt :%d); %s pairs predicted, committed alone at f47d8ab5 before any onset, %s beyond '
            'reach (data/b721_predictions.txt :%d); HELD %s, REFUTED %s (data/b721_onsets.txt :%d); the least negative coefficient at n = %s, '
            'b(n) = %s (data/b721_coeffs.txt :%d), registration (ii) HELD (:%d); the companion at %s sentences, KERNEL %s, HELD %s '
            '(data/b721_companion.txt :%d); the hits %s, AS DESIGNED %s, FOR THE AUTHOR %s (data/b721_lint.txt :%d); %s names, %s found at a '
            'current tag, %s missing (data/b721_names.txt :%d); the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both '
            '(data/b721_closing.txt :%d, :%d); the counter CLAIM %s, CLOSE %s (data/b721_closing.txt :%d); the mirror CLEAN on all three clauses '
            '(data/b721_mirror.txt :%d), its manifest control NOT AS WANTED against a carried reference (:%d; event (10)); the root %s chained '
            'from %s (data/b721_act_root.json); %d events in data/b721_events.txt, rows (1)-(%d); %d defects (a)–(%s), all the seat’s '
            '(data/b721_defects.txt). Nothing deposited, nothing published.' % (
                head, rec[0]['commit'][:8], clo[0]['commit'][:8], nzero, npair, lls, npred, nbey, lpd, nheld, nref, lon, nneg, bneg, lco,
                lr2, nsen, nker, nhld, lcm, nhit, nad, nfa, lli, nnm, nfd, nms, lnm, p_pre, n_pre, p_post, n_post, lpre, lpost, ncl, nco,
                lct, lmv, lmc, ar['root'][:8], ar['previous'][:8], len(evr), evr[-1], len(short), _letter(short[-1])))


def _wb_b716_form():
    head = rdn('b721_closing.txt').split(NL)[0]
    st = jl('b721_steps.json').get('rows') or []
    rec = [r for r in st if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r for r in st if r.get('phase') == 'closing']
    if len(rec) != 1 or len(clo) != 1:
        sys.exit('### data/b721_steps.json CARRIES %d RELAY RECORD ROWS AND %d CLOSING ROWS, NOT ONE EACH -- NOTHING COMPOSED' % (len(rec), len(clo)))
    cc = clo[0]['commit']
    reg_first = g(ROOT, 'log', '--format=%H', '-1', '--', 'data/b721_registrations.txt').strip()
    reg_files = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.REG_COMMIT).split(NL) if x.strip()]
    _x, lgc = _fl('b721_genus_control.txt', r'MISSES 0', 'the count control`s misses')
    ver = g(ROOT, 'show', '%s:tools/standing/VERSION' % cc).strip()
    (nst, stp), lcov = _fl('b721_toolset_coverage.txt', r'STEPS 25 ; STANDING (\d+) \(([^)]*)\)', 'the coverage table`s STANDING count')
    (nobj, neq, ndf), lrp = _fl('b721_replay.txt', r'OBJECTS (\d+) ; EQUAL (\d+) ; DIFFERS (\d+)', 'the replay`s figure')
    _x, lmv = _fl('b721_mirror_verify.txt', r'CLEAN ON ALL THREE CLAUSES', 'the verification CLEAN')
    _x, lmc = _fl('b721_mirror.txt', r'NOT AS WANTED', 'the manifest control')
    _x, lks = _fl('b721_keystone.txt', r'SIDE-meta', 'Silence :212 to SIDE-meta')
    (nall, npin, ncar), lcp = _fl('b721_correspondence_pins.txt', r'NAMES (\d+) ; PINNED FROM THE CENSUS (\d+) .* ; LISTED AND CARRIED (\d+)', 'the names pinned')
    pr = [(f, len(rdn(f).rstrip(NL).split(NL))) for f in ('b721_price.txt', 'b721_federation_pin_price.txt', 'b721_epstein_count_price.txt')]
    nwords = len(re.findall(r'(?m)^### PROMPT \d+ ', rdn('b721_author_answers.txt')))
    ar = jl('b721_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b721_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    evr = [int(m.group(1)) for m in re.finditer(r'(?m)^    \((\d+)\) ', rdn('b721_events.txt'))]
    short = _defect_short('b721')
    owners = re.findall(r"^    \(([a-z])\) (THE SEAT'S|THE NAVIGATOR'S):", rdn('b721_defects.txt'), re.M)
    if evr != list(range(1, 20)) or len(short) != 18 or len(owners) != 18 or any(o != "THE SEAT'S" for _x, o in owners):
        sys.exit('### b721`S EVENTS %s AND DEFECTS %d (OWNERS %s) NOT THE RULING`S NINETEEN AND EIGHTEEN -- NOTHING COMPOSED' % (evr, len(short), owners))
    return (' “%s” (data/b721_closing.txt :1); its relay commit the record’s %s, the closing’s %s (data/b721_steps.json, the record and '
            'closing rows). As the banks confirm by row: data/b721_registrations.txt committed at the act’s opening commit %s (%s files, '
            'its last change there: %s), its count control at 0 misses (data/b721_genus_control.txt :%d), nothing of -39 computed beyond it; '
            'tools/standing/ at %s at the closing’s commit, %s of 25 steps STANDING (%s) (data/b721_toolset_coverage.txt :%d); the replay at '
            '%s of %s objects EQUAL, %s DIFFERS, b713’s old tool, F-2 (data/b721_replay.txt :%d); the mirror verified CLEAN on all three clauses '
            '(data/b721_mirror_verify.txt :%d), its manifest control NOT AS WANTED against a carried reference (data/b721_mirror.txt :%d; event '
            '(17)); Silence :212 corrected to SIDE-meta (data/b721_keystone.txt :%d); %s of %s unpinned names pinned, %s carried '
            '(data/b721_correspondence_pins.txt :%d); the prices at %s; the author’s words on its %d root prompts banked verbatim (data/b721_author_answers.txt :10, :13); '
            'the root %s chained from %s (data/b721_act_root.json); %d events in data/b721_events.txt, rows (1)-(%d); %d defects (a)–(%s), all '
            'the seat’s (data/b721_defects.txt). Nothing deposited, nothing published.' % (
                head, rec[0]['commit'][:8], cc[:8], K.REG_COMMIT[:8], len(reg_files), reg_first[:8], lgc, ver, nst, stp, lcov, neq, nobj, ndf,
                lrp, lmv, lmc, lks, npin, nall, ncar, lcp, ', '.join('data/%s :%d' % p for p in pr), nwords, ar['root'][:8],
                ar['previous'][:8], len(evr), evr[-1], len(short), _letter(short[-1]), ))


def _wb_b715_form():
    head = rdn('b721_closing.txt').split(NL)[0]
    st = jl('b721_steps.json').get('rows') or []
    rec = [r for r in st if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r for r in st if r.get('phase') == 'closing']
    if len(rec) != 1 or len(clo) != 1:
        sys.exit('### data/b721_steps.json CARRIES %d RELAY RECORD ROWS AND %d CLOSING ROWS, NOT ONE EACH -- NOTHING COMPOSED' % (len(rec), len(clo)))
    cc = clo[0]['commit']
    ver = g(ROOT, 'show', '%s:tools/standing/VERSION' % cc).strip()
    nfiles = len([x for x in g(ROOT, 'ls-tree', '--name-only', cc, 'tools/standing/').split(NL) if x.strip()])
    _x, lscan = _fl('b721_standing_scan.txt', r'LITERALS IN THE CODE 0', 'the scan`s figure')
    (nst, stp), lcov = _fl('b721_toolset_coverage.txt', r'STEPS 25 ; STANDING (\d+) \((\[\d+\])\)', 'the coverage table`s STANDING count')
    _x, lcore = _fl('b721_toolset_coverage.txt', r'AT \[3\], \[7\], \[8\], \[17\], \[20\], \[25\]', 'the core`s steps')
    (nobj, neq, ndf), lrp = _fl('b721_replay.txt', r'OBJECTS (\d+) ; EQUAL (\d+) ; DIFFERS (\d+)', 'the replay`s figure')
    _x, lf1 = _fl('b721_replay.txt', r'^  F-1 \[b714, b713 ; object \(5\)\] THE SEAL', 'F-1')
    _x, lf2 = _fl('b721_replay.txt', r'^  F-2 \[b713 ; object \(6\)\]', 'F-2')
    wh = jl('b721_seal_hashes.json').get('withheld')
    if wh != []:
        sys.exit('### data/b721_seal_hashes.json WITHHELD %r, NOT EMPTY -- NOTHING COMPOSED' % (wh,))
    _x, lro = _fl('b721_roster.txt', r'THE_KEYSTONE_CENSUS_v0_8_1\.md', 'the census v0.8.1 joined to the roster')
    _x, lro0 = _fl('b721_roster.txt', r'THE_KEYSTONE_CENSUS_v0_8\.md', 'the census v0.8 joined to the roster')
    _x, lmv = _fl('b721_mirror_verify.txt', r'NOT CLEAN', 'the verification NOT CLEAN')
    pc = rdn('b721_pins_census.txt').split(NL)
    allrows = [l for l in pc if l.startswith('--- ')]
    npub = sum(1 for l in allrows if 'visibility PUBLIC' in l)
    nprv = sum(1 for l in allrows if 'visibility PRIVATE' in l)
    _x, lhf = _fl('b721_pins_census.txt', r'^\s*### REPOS HARD-FAILING : 0\s*$', 'the census`s hard failures')
    revs = [i for i, l in enumerate(pc, 1) if l.strip().startswith('MATHLIB UPSTREAM PIN')]
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) .*### WITHHELD, NOT EXERCISABLE : (\d+) \.'
    (n_post, p_post, f_post, w_post), lpost = _fl('b721_closing.txt', suite % 'post-push', 'the post-push suite')
    (n_pre, p_pre, f_pre, w_pre), lpre = _fl('b721_closing.txt', suite % 'pre-push', 'the pre-push suite')
    ar = jl('b721_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b721_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    short = _defect_short('b721')
    owners = re.findall(r"^    \(([a-z])\) (THE SEAT'S|THE NAVIGATOR'S):", rdn('b721_defects.txt'), re.M)
    nav = [x for x, o in owners if o == "THE NAVIGATOR'S"]
    if len(owners) != len(short) or len(short) != 17 or nav != ['d']:
        sys.exit('### data/b721_defects.txt OWNERS %s BESIDE %d DEFECTS -- NOTHING COMPOSED' % (owners, len(short)))
    evl = [i for i, l in enumerate(rdn('b721_events.txt').split(NL), 1) if re.match(r'^\(\d+\) ', l)]
    if len(evl) != 11:
        sys.exit('### data/b721_events.txt READS %d STARTING LINES, NOT THE RULING`S ELEVEN -- NOTHING COMPOSED' % len(evl))
    return (' “%s” (data/b721_closing.txt :1); its relay commit the record’s %s, the closing’s %s (data/b721_steps.json, the record and '
            'closing rows). As the banks confirm by row: tools/standing/ at %s, %d files, at the closing’s commit, its code carrying 0 act '
            'literals (data/b721_standing_scan.txt :%d); the coverage table at %s of 25 steps STANDING (%s), the core’s functions called inside '
            '[3], [7], [8], [17], [20], [25] (data/b721_toolset_coverage.txt :%s); the replay over b714 and b713 at %s of %s objects EQUAL, '
            '%s DIFFERS, the old tool’s F-2 (:%d), and F-1 the seal’s recorded head (:%d) (data/b721_replay.txt :%d); the seal’s withheld field '
            'empty, G-RULE-LONG-PHASE-SPLIT sealed by the part-bank repair (data/b721_seal_hashes.json); the mirror’s roster from main by '
            'family, the census v0.8 and v0.8.1 joined (data/b721_roster.txt :%d, :%d), its verification NOT CLEAN at clause 3 by the '
            'verifier’s base roster (data/b721_mirror_verify.txt :%d; event (10)); the pins census at %d repositories, %d PUBLIC and %d '
            'PRIVATE, 0 hard failures (data/b721_pins_census.txt :%d), upstream Mathlib at %d revs read per kernel (:%d-:%d); the suite %s of %s '
            'pre-push and %s of %s post-push, %s withheld (data/b721_closing.txt :%d, :%d); the root %s chained from %s (data/b721_act_root.json); '
            '%d events in data/b721_events.txt by their starting lines (:%s); %d defects (a)–(%s), (%s) the navigator’s, the rest the seat’s '
            '(data/b721_defects.txt). Nothing deposited, nothing published.' % (
                head, rec[0]['commit'][:8], cc[:8], ver, nfiles, lscan, nst, stp, ('%d' % lcov) if lcov == lcore else ('%d, :%d' % (lcov, lcore)), neq, nobj, ndf, lf2, lf1, lrp, lro0, lro, lmv,
                len(allrows), npub, nprv, lhf, len(revs), revs[0] if revs else 0, revs[-1] if revs else 0, p_pre, n_pre, p_post, n_post,
                w_post, lpre, lpost, ar['root'][:8], ar['previous'][:8], len(evl), ', :'.join(str(i) for i in evl), len(short),
                _letter(short[-1]) if short else '-', nav[0]))


def _wb_carried714():
    """b721's weight line under (R332)(1), in the clause's order, every figure read from b721's banks by row and cited by its line: the head
    from its closing :1 and the closing's commit from its step bank; the suite post-push and pre-push with its one withheld arm; that arm's
    defect (p); the lv tag; the re-cut's merge and its additive check; the heads draft held; the pilot's (P1), (P2) and (P3), the chain's rows
    counted from the bank; the entry and the trail; the root and its banks; the scores; the mirror; the defects with their owners and the
    events by their starting lines. Written at b722: both carried forms composed earlier acts' objects, banks b721 did not write -- the class
    the navigator's added item of (R332)(2) names, a close computed in copied tools."""
    c = rdn('b721_closing.txt')
    head = c.split(NL)[0]
    closing = [r for r in (jl('b721_steps.json').get('rows') or []) if r.get('phase') == 'closing']
    if len(closing) != 1:
        sys.exit('### data/b721_steps.json CARRIES %d CLOSING ROWS, NOT ONE -- NOTHING COMPOSED' % len(closing))
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) .*### WITHHELD, NOT EXERCISABLE : (\d+) \[\'G-RULE-LONG-PHASE-SPLIT\'\]'
    (n_post, p_post, f_post, w_post), lpost = _fl('b721_closing.txt', suite % 'post-push', 'the post-push suite')
    (n_pre, p_pre, f_pre, w_pre), lpre = _fl('b721_closing.txt', suite % 'pre-push', 'the pre-push suite')
    _x, ldp = _fl('b721_defects.txt', r"^    \(p\) b713's CLOSE'S: .*G-RULE-LONG-PHASE-SPLIT WITHH", 'defect (p)')
    (tag,), ltag = _fl('b721_closing.txt', r'v0\.14\.0 MADE AT ([0-9a-f]{8}), ANNOTATED, PEEL READ BACK \1 ; NO RELEASE FOR IT', 'the lv tag')
    _x, lra = _fl('b721_closing.txt', r'ORIGINAL LINES 22 .* ; FOUND 22 ; MISSING 0 ; IN ORDER True', 'the additive check on main')
    par = g(PP, 'rev-list', '--parents', '-n', '1', K.RECUT_MERGE).split()
    if len(par) != 3 or par[0] != K.RECUT_MERGE:
        sys.exit('### %s IS NOT A MERGE OF TWO PARENTS ON PLACE-papers (%s) -- NOTHING COMPOSED' % (K.RECUT_MERGE[:8], [x[:8] for x in par]))
    _x, lhd = _fl('b721_closing.txt', r'THE DRAFT HELD, NOT WRITTEN TO MAIN', 'the heads draft held')
    (n1, f1, m1, np1), lp1 = _fl('b721_pilot.txt', r'\(P1\) NAMES (\d+): FOUND (\d+) ; MISSING (\d+) ; NO PIN STATED (\d+)', 'the pilot`s (P1)')
    (h2, ad2, fa2), lp2 = _fl('b721_pilot.txt', r'\(P2\) HITS (\d+): AS DESIGNED (\d+) ; FOR THE AUTHOR (\d+)', 'the pilot`s (P2)')
    (nd3, dis3, hr3), lp3 = _fl('b721_pilot.txt', r'\(P3\) THE CHAIN (\d+) DECLARATIONS ; .* ; (\d+) DISPATCHES ; ABOUT ([\d.]+) HOURS', 'the pilot`s (P3)')
    rows3 = [(i, m.group(1)) for i, l in enumerate(rdn('b721_pilot.txt').split(NL), 1)
             for m in [re.match(r'^    the (?:surround :\d+|seam|target|join)\s+\| \S+\s+\| \S+\s+\| (FOUND|READ|MISSING)\s+\|', l)] if m]
    if len(rows3) != int(nd3):
        sys.exit('### data/b721_pilot.txt (P3) READS %d ROWS BESIDE ITS FOOT`S %s -- NOTHING COMPOSED' % (len(rows3), nd3))
    found3 = sum(1 for _i, s in rows3 if s == 'FOUND')
    read3 = sum(1 for _i, s in rows3 if s == 'READ')
    ar = jl('b721_act_root.json')
    if not ar.get('root') or not ar.get('previous'):
        sys.exit('### data/b721_act_root.json CARRIES NO ROOT -- NOTHING COMPOSED')
    (nbanks,), lbk = _fl('b721_closing.txt', r'THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1', 'the root`s banks')
    _x, lsc = _fl('b721_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD', 'the scores at the close')
    (msha,), lmi = _fl('b721_closing.txt', r'mirror-refresh-2026-10-26-b721\.zip ; \d+ bytes ; sha256 ([0-9a-f]{8})[0-9a-f]* ; .*Act root: b721 '
                       + ar['root'] + ' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    short = _defect_short('b721')
    owners = re.findall(r"^    \(([a-z])\) (THE SEAT'S|THE NAVIGATOR'S|b713's CLOSE'S):", rdn('b721_defects.txt'), re.M)
    nav = [x for x, o in owners if o == "THE NAVIGATOR'S"]
    prv = [x for x, o in owners if o == "b713's CLOSE'S"]
    if len(owners) != len(short) or nav != ['f', 'q'] or prv != ['p']:
        sys.exit('### data/b721_defects.txt OWNERS %s BESIDE %d DEFECTS -- NOTHING COMPOSED' % (owners, len(short)))
    evl = [i for i, l in enumerate(rdn('b721_events.txt').split(NL), 1) if re.match(r'^\(\d+\) ', l)]
    if len(evl) != 12:
        sys.exit('### data/b721_events.txt READS %d STARTING LINES, NOT THE RULING`S TWELVE -- NOTHING COMPOSED' % len(evl))
    return (' “%s” (data/b721_closing.txt :1); its relay commit the record’s, the closing’s %s (data/b721_steps.json, the closing row), pushed '
            'and read back. As the banks confirm by row: the suite %s passing, %s failing and %s WITHHELD, NOT EXERCISABLE of %s post-push, '
            '%s/%s/%s pre-push (data/b721_closing.txt :%d, :%d); G-RULE-LONG-PHASE-SPLIT withheld under the author’s words (5)-(7), defect (p), '
            'b713’s close’s (data/b721_defects.txt :%d); the lv port tagged v0.14.0 at %s, annotated, its peel read back, no release for it '
            '(data/b721_closing.txt :%d); recut-b712-silence merged into PLACE-papers main at %s, its second parent %s, the additive check on '
            'main FOUND 22, MISSING 0, in order (data/b721_closing.txt :%d); the heads draft HELD in data/b721_heads_draft.txt, not written to '
            'main (data/b721_closing.txt :%d); the pilot in data/b721_pilot.txt: %s names, %s FOUND, %s MISSING, %s NO PIN STATED (:%d); %s '
            'lint hits, %s AS DESIGNED, %s FOR THE AUTHOR (:%d); the reduction chain’s %s declarations, %s FOUND at their pins and %s READ '
            'from the faces page (:%d-:%d), a blueprint priced at %s dispatches and about %s hours (:%d); the entry at FINDINGS :%d; the trail '
            'at OPEN_TRAILS :%d; the root %s over %s banks chained from %s (data/b721_act_root.json; data/b721_closing.txt :%d); N1-N5 and '
            'S1-S3 HELD (data/b721_closing.txt :%d); the mirror mirror-refresh-2026-10-26-b721.zip (sha256 %s…) CLEAN on all three clauses '
            'with the root line (data/b721_closing.txt :%d); %d defects (a)–(%s), (%s) and (%s) the navigator’s, (%s) b713’s close’s, the '
            'rest the seat’s (data/b721_defects.txt); %d events in data/b721_events.txt by their starting lines. Nothing deposited, nothing '
            'published.' % (
                head, closing[0]['commit'][:8], p_post, f_post, w_post, n_post, p_pre, f_pre, w_pre, lpost, lpre, ldp, tag, ltag,
                K.RECUT_MERGE[:8], par[2][:8], lra, lhd, n1, f1, m1, np1, lp1, h2, ad2, fa2, lp2, nd3, found3, read3, rows3[0][0],
                rows3[-1][0], dis3, hr3, lp3, K.B711_ENTRY, K.B711_TRAIL, ar['root'][:8], nbanks, ar['previous'][:8], lbk, lsc, msha, lmi,
                len(short), _letter(short[-1]) if short else '-', nav[0], nav[1], prv[0], len(evl)))


def c1(*a):
    """FINDINGS: b721's weight line appended after b721's entry (:10512) through b698's landing and its screens; its line banked in
    data/b722_record_lines.json. `c1 dry` prints the line and writes nothing."""
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + _wb() + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B711_ENTRY,
         check=[('FINDINGS.md', K.B711_ENTRY, '## The -39 control: the certified list to height 200'),
                ('OPEN_TRAILS.md', K.B711_TRAIL, '### b721 — lane two, act one hundred and forty-four, the test act')],
         dry=dry)   # ### b722: the needles b721's entry (:10784) and trail (:16086), read through the Read tool; the carried needles named b716's


# ================================================================================ COMPONENT 1: THE FACES LEDGER HEAD, (R332)(2)(ii)
FACES_OLD = 'and the record states none'
FACES_NEW = ('and the record states one, faces_join (row at :547), an equivalence between two faces of the fourth register compiled through '
             'Mathlib’s RiemannHypothesis, neither face proved; the deposit’s refusal of the cross-register equivalences, quoted above, stands, '
             'and no row compiles one')


def facesdiff(*a):
    """data/b722_faces_head_diff.txt: (R332)(2)(ii)'s edit of FACES_LEDGER.md :8, made by the Edit tool -- the working tree's diff against
    HEAD printed whole, and N3's reading: the line at HEAD with the clause replaced equals the line now, byte for byte, and no other line moved."""
    fl = 'FACES_LEDGER.md'
    d = g(PP, 'diff', '--', fl)
    old = g(PP, 'show', 'HEAD:' + fl).split(NL)
    new = rd(os.path.join(PP, fl)).split(NL)
    h = K.FACES_HEAD - 1
    want = old[h].replace(FACES_OLD, FACES_NEW, 1)
    same_else = len(old) == len(new) and all(old[i] == new[i] for i in range(len(old)) if i != h)
    once = old[h].count(FACES_OLD) == 1 and new[h].count(FACES_OLD) == 0
    ok = new[h] == want and same_else and once
    L = ['%s -- COMPONENT 1, (R332)(2)(ii): THE FACES LEDGER HEAD`S EDIT, FACES_LEDGER.md :%d, BY THE EDIT TOOL (%s)' % (ACT, K.FACES_HEAD, utc()), '',
         '### the clause "%s" replaced by the author`s words, every other word of the head unchanged; the diff of the working tree against' % FACES_OLD,
         '### PLACE-papers HEAD %s printed whole by `git diff`.' % g(PP, 'rev-parse', '--short', 'HEAD').strip(), '']
    L += ['    ' + l for l in d.replace(chr(13), '').rstrip(NL).split(NL)]
    L += ['', '### the old clause once at HEAD :%d %s ; absent now %s' % (K.FACES_HEAD, old[h].count(FACES_OLD) == 1, new[h].count(FACES_OLD) == 0),
          '### the line at HEAD with the clause replaced equals the line now: %s ; lines %d and %d ; every other line equal: %s' % (
              new[h] == want, len(old), len(new), same_else),
          '', '### ### **THE HEAD`S EDIT: THE CLAUSE NAMED AND NOTHING ELSE %s.**' % ('True' if ok else '### False')]
    put_txt('%s_faces_head_diff.txt' % ACT, L)
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RE-CUT'S ADDITIVE CHECK, (R332)(2)(iii)
def _sections(lines):
    """[(start, end, level, title)] for each markdown heading, its section running to the next heading of its level or above (1-based, end inclusive)."""
    hs = [(i + 1, len(m.group(1)), m.group(2).strip()) for i, l in enumerate(lines) for m in [re.match(r'^(#{1,6}) +(.*)$', l)] if m]
    out = []
    for k, (s, lv, t) in enumerate(hs):
        e = next((s2 - 1 for s2, lv2, _t in hs[k + 1:] if lv2 <= lv), len(lines))
        out.append((s, e, lv, t))
    return out


def recutadd(*a):
    """data/b722_recut_additive.txt (.json): every line of the original Correspondence section (the re-cut's base, <RECUT_COMMIT>^, the
    section whose heading names Correspondence) read against the branch's tip: each line with its line at the tip, FOUND (the same bytes on
    one line at or after the tip's back matter) or MISSING; blank lines counted, not searched. `recutadd <rev>` reads another tip (after a
    restore). Writes its bank; edits no document."""
    tip = a[0] if a else 'refs/heads/' + K.RECUT_BRANCH
    tsha = g(PP, 'rev-parse', '--verify', '--quiet', tip + '^{commit}').strip()
    base = g(PP, 'show', '%s^:%s' % (K.RECUT_COMMIT, K.RECUT_DOC)).replace(chr(13), '').split(NL)
    now = g(PP, 'show', '%s:%s' % (tsha, K.RECUT_DOC)).replace(chr(13), '').split(NL)
    secs = [x for x in _sections(base) if 'correspondence' in x[3].lower()]
    if len(secs) != 1:
        sys.exit('### THE BASE CARRIES %d SECTIONS NAMING Correspondence (%s) -- NOTHING WRITTEN' % (len(secs), secs))
    s, e, lv, title = secs[0]
    tsecs = [x for x in _sections(now) if 'correspondence' in x[3].lower()]
    rows, found, missing, blank = [], 0, 0, 0
    for i in range(s, e + 1):
        l = base[i - 1]
        if not l.strip():
            blank += 1
            continue
        at_ = [j + 1 for j, m in enumerate(now) if m == l]
        st = 'FOUND' if at_ else 'MISSING'
        found += bool(at_)
        missing += not at_
        rows.append(dict(base_line=i, text=l, tip_lines=at_, status=st))
    order = [r['tip_lines'][0] for r in rows if r['tip_lines']]
    in_order = order == sorted(order)
    L = ['%s -- COMPONENT 1, (R332)(2)(iii): THE RE-CUT`S ADDITIVE CHECK, THE ORIGINAL CORRESPONDENCE SECTION READ AGAINST %s (%s)' % (ACT, K.RECUT_BRANCH, utc()), '',
         '### the base: PLACE-papers %s^ (%s), %s, the section %r at :%d-:%d (heading level %d), %d lines of which %d blank; the tip: %s %s (%d lines),' % (
             K.RECUT_COMMIT[:8], g(PP, 'rev-parse', '--short', K.RECUT_COMMIT + '^').strip(), K.RECUT_DOC, title, s, e, lv, e - s + 1, blank, tip, tsha[:8], len(now)),
         '### its sections naming Correspondence %s. Rows: the base line | its line(s) at the tip | FOUND or MISSING | the line`s first 110 characters.' % (
             ['%s :%d-:%d' % (t, s2, e2) for s2, e2, _lv, t in tsecs] or 'NONE'), '']
    L += ['  :%-5d | %-14s | %-7s | %s' % (r['base_line'], ','.join(':%d' % j for j in r['tip_lines']) or '--', r['status'], r['text'][:110]) for r in rows]
    L += ['', '### the found lines in the base`s order at the tip: %s' % in_order,
          '', '### ### **ORIGINAL LINES %d (BLANK %d NOT SEARCHED) ; FOUND %d ; MISSING %d ; IN ORDER %s.**' % (len(rows), blank, found, missing, in_order)]
    # ### every run kept in the one bank (W) names: a run at a later tip (after a restore) is appended beneath the earlier, which is not rewritten
    prior = jl('%s_recut_additive.json' % ACT).get('runs') or []
    run = dict(at=utc(), tip=tsha, base=K.RECUT_COMMIT + '^', section=[s, e, title], rows=rows, found=found, missing=missing, in_order=in_order, text=L)
    runs = [r for r in prior if r.get('tip') != tsha] + [run]
    T_ = []
    for k, r in enumerate(runs, 1):
        T_ += (['', '=' * 40 + ' RUN %d OF %d, AT THE TIP %s' % (k, len(runs), r['tip'][:8]), ''] if len(runs) > 1 else []) + r['text']
    put_txt('%s_recut_additive.txt' % ACT, T_ if len(runs) == 1 else T_[1:])
    put_json('%s_recut_additive.json' % ACT, dict(at=utc(), runs=runs, last=dict((k, run[k]) for k in ('tip', 'found', 'missing', 'in_order'))))
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 1: THE REPAIRS' CONTROLS, (R332)(2)
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
    """data/b722_repair_controls.txt (.json), Component 1, (R332)(2): each structural repair (standing clauses v2 rows (52)-(55)) and each item
    repair against the banks its old form failed on, with its NEG control; every reading printed beside the case. The suite's repaired forms are
    read from tools/b722_checks.py itself (imported), the closing's from tools/b722_closing.py, the membrane's from tools/act_membrane.py."""
    import b722_checks as CK
    import b722_closing as CL
    import act_membrane as MEM
    rows, notes, allok = [], [], True

    def case(sec, name, got, want, note=''):
        nonlocal allok
        ok = got == want
        allok = allok and ok
        rows.append(dict(section=sec, case=name, got=got, wanted=want, as_wanted=ok, note=note))

    # ---------------------------------------------------------------- (i) THE EVENTS SECTION
    sj7 = jl('b721_seal_hashes.json')
    seal7 = letters_at_seal('b721') or []
    s_let = [_letter(s) for s in seal7]
    now7 = [_letter(s) for s in letters_of(rdn('b721_defects.txt'))]
    body7 = _trail_defects_body('b721', K.B710_TRAIL) or ''
    t_let = re.findall(r"(?:^|; )\(([a-z]'?)\) ", body7)
    late7 = [x for x in now7 if x not in s_let]
    notes += ['(i) b721`s seal: %s, its relay head %s ; the letters in its defects bank at that head %s ; in the bank now %s ; on its trail`s Defects line '
              '(OPEN_TRAILS from :%d) %s ; after the seal, under the repaired route events: %s' % (
                  sj7.get('at'), (sj7.get('relay_head') or '')[:8], s_let, now7, K.B710_TRAIL, t_let, late7)]
    case('i', 'the ruling`s control: b721`s trail read under the repaired arms (its Defects letters against the letters entered before the seal) '
              'with (i) as an event passes', t_let == s_let, True,
         'the letters (g) and (h) were also entered after b721`s seal (lettered at relay 842ea536, after the seal`s head 71f1c2a0): under the rule`s '
         'cut they are events with (i)-(k), and b721`s trail, landed with (a)-(h), carries two of them -- for the author`s strike')
    case('i', 'NEG: a letter entered before the seal and missing from the trail fails (the seal`s letters with (z) added, the trail`s as entered)',
         s_let == s_let + ['z'], False)
    case('i', 'the trail carrying exactly the letters entered before the seal passes (the seal`s letters against themselves)', s_let == list(s_let), True)
    ev = []
    hl_new = CL.head_line(act='b721', events=ev)
    del CL.HEAD_EVENTS[:]
    CL.head_line(act='b721')
    sect = CL.events_section(act='b721')
    case('i', 'the closing`s events section over b721`s banks: the head-line builder`s failures land there, two (relay and PLACE-papers)',
         len([l for l in sect if l.startswith('    THE HEAD LINE: ')]), 2)
    notes += ['(i) the closing`s events section over b721`s banks: ' + ' | '.join(sect)]
    # ---------------------------------------------------------------- (ii) THE MEMBRANE
    test_roots = os.path.join(K.SP, 'b722_membrane_roots.txt')
    real = rd(MEM.ROOTS)
    with open(test_roots + '.tmp', 'wb') as fh:   # ### the control's own scratch write, outside relay
        fh.write((real.rstrip(NL) + NL + 'b722 %s %s' % ('f' * 64, (jl('b721_act_root.json').get('root') or '0' * 64)) + NL).encode('utf-8'))
    os.replace(test_roots + '.tmp', test_roots)
    probe = os.path.join(D, 'b722_membrane_probe.json')
    try:
        MEM.guard('b722', 'b722_membrane_probe.json', R.ROOT_EXCLUDE, roots=test_roots)
        code = 0
    except SystemExit as e:
        code = e.code
    case('ii', 'a bank write attempted after a test root refuses: the guard exits 4 and the bank is not written', (code, os.path.exists(probe)), (4, False))
    case('ii', 'after the test root a bank the root names is refused (data/b722_reading5.txt, data/b722_repair_controls.txt)',
         (bool(MEM.refuses('b722', 'b722_reading5.txt', R.ROOT_EXCLUDE, test_roots)), bool(MEM.refuses('b722', 'b722_repair_controls.txt', R.ROOT_EXCLUDE, test_roots))),
         (True, True))
    case('ii', 'after the test root the excluded banks pass: the closing, the events, the step bank, the push capture, the mirror builder`s',
         [bool(MEM.refuses('b722', n, R.ROOT_EXCLUDE, test_roots)) for n in ('b722_closing.txt', 'b722_events.txt', 'b722_steps.json', 'b722_relay_push_out.txt', 'b722_mirror.json')],
         [False] * 5)
    case('ii', 'on the real chain (b722 not appended) a write proceeds', bool(MEM.refuses('b722', 'b722_reading5.txt', R.ROOT_EXCLUDE)), False)
    case('ii', 'POS on the real chain: b721 is appended, so a b721 bank the root names is refused', bool(MEM.refuses('b721', 'b721_reading5.txt')), True)
    _wrap = lambda f: getattr(f, '__name__', '') in ('put_json', 'put_txt') and getattr(f, '__module__', '') in ('__main__', 'b722_record')   # noqa: E731
    wired = dict(record=(_wrap(R.put_json) and _wrap(R.put_txt)), citation=rd(os.path.join(T, 'b722_citation.py')).count('MEM.guard('),
                 closing=rd(os.path.join(T, 'b722_closing.py')).count('_guard('), suite=rd(os.path.join(T, 'b722_checks.py')).count('_membrane('),
                 independence=rd(os.path.join(T, 'b722_independence.py')).count('_membrane('), standing=rd(os.path.join(T, 'b722_standing.py')).count('_membrane('),
                 tests=rd(os.path.join(T, 'b722_tests.py')).count('_membrane('), carry=rd(os.path.join(T, 'b722_carry.py')).count('_membrane('))
    notes += ['(ii) the guard wired in the writers (calls in the text, the definition counted): %s' % wired]
    case('ii', 'every b722 writer calls the guard (the record`s shared writers rebound; the citation`s, the closing`s, the suite`s, independence`s, '
               'standing`s, the tests` and the carry`s calls present)', all(wired.values()), True)
    st0, ds0 = _status(), _data_state()
    rc1, o1 = _run(os.path.join(T, 'b722_record.py'), 'defs', 'b722_checks.py')
    rc2, o2 = _run(os.path.join(T, 'b722_record.py'), 'names', 'b722_checks')
    rc3, o3 = _run(os.path.join(T, 'b722_citation.py'), 'replay', 'Root: 1, proceed', K.PREV_SESSION, K.PREV_ANCHOR)
    st1, ds1 = _status(), _data_state()
    changed = sorted(f for f in set(ds0) | set(ds1) if ds0.get(f) != ds1.get(f))
    case('ii', 'three locator and read calls (the record tool`s defs and names routes, the citation tool`s replay) leave the tree unchanged by git '
               'status and relay data/ unchanged file for file', (rc1, rc2, rc3, st0 == st1, changed), (0, 0, 0, True, []))
    # ---------------------------------------------------------------- (iii) ARMS READ STRUCTURE
    g8, g9, g10 = rdn('b708_reg_gate.txt'), rdn('b709_reg_gate.txt'), rdn('b721_reg_gate.txt')
    case('iii', 'G-CLOSING-DRY-STEP: b708`s sealed needle on b708`s honest gate record fails (the bank b708 failed on)', '### NO VERDICT LINE' not in g8, False)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b708`s gate record passes', CK.no_verdict_line_ok(g8), True)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b709`s gate record (three rows) passes', CK.no_verdict_line_ok(g9), True)
    case('iii', 'G-CLOSING-DRY-STEP: the repaired reading on b721`s gate record passes', CK.no_verdict_line_ok(g10), True)
    case('iii', 'NEG: b709`s record with a NO VERDICT LINE row named on a verdict-bearing bank (data/b709_pairs.txt) fails',
         CK.no_verdict_line_ok(g9.replace('data/b709_grid_hashes.txt): ### NO VERDICT LINE', 'data/b709_pairs.txt): ### NO VERDICT LINE')), False)
    case('iii', 'NEG: b709`s record with a NO VERDICT LINE row naming an absent bank fails',
         CK.no_verdict_line_ok(g9.replace('data/b709_grid_hashes.txt): ### NO VERDICT LINE', 'data/b709_nosuch.txt): ### NO VERDICT LINE')), False)
    k9 = ('ONSET', 'ZETA', 'RATIO', 'MODULES', 'FIGURES')
    rj9, rj10 = jl('b709_report.json'), jl('b721_report.json')
    case('iii', 'G-REPORT-UNSEALED: b709`s sealed needle on b709`s report text (the keys in capitals) fails', all(x in rdn('b709_report.txt') for x in k9), False)
    case('iii', 'G-REPORT-UNSEALED: the repaired reading of b709`s report JSON bank (its lines) passes', CK.report_lines_ok(rj9, k9, 5), True)
    case('iii', 'G-REPORT-UNSEALED: the repaired reading of b721`s report JSON bank on b721`s keys passes', CK.report_lines_ok(rj10, CK.REPORT_KEYS, 5), True)
    case('iii', 'NEG: b709`s report JSON with its lines cut to four fails', CK.report_lines_ok(dict(rj9, lines=(rj9.get('lines') or [])[:4]), k9, 5), False)
    case('iii', 'NEG: b709`s report JSON with every `ratio` removed, any case, fails',
         CK.report_lines_ok(dict(rj9, lines=[re.sub('(?i)ratio', 'quotient', x) for x in (rj9.get('lines') or [])]), k9, 5), False)
    q = '(e) representation coordinates (the operator / Toeplitz form) -- 4'
    reg9 = rdn('b709_registrations.txt')
    case('iii', 'G-AXIS-REGISTERED: b709`s sealed needle on b709`s registrations bank (the quotation wrapped) fails', q in reg9, False)
    case('iii', 'G-AXIS-REGISTERED: the repaired reading (joined; the bank has no JSON) passes', q in CK.joined(reg9), True)
    case('iii', 'NEG: the repaired reading on a copy with "Toeplitz" changed to "Hankel" fails', q in CK.joined(reg9.replace('Toeplitz', 'Hankel')), False)
    case('iii', 'each arm run on b721`s banks before the seal: the seal refuses while a part`s run on b721`s banks is not banked', bool(CK.prev_run_missing()), True)
    # ---------------------------------------------------------------- (iv) CONTROLS THAT CAN FAIL
    face7 = rd(os.path.join(ROOT, *K.B711_FACE.split('/')))
    S7 = dict(citation=rdn('b721_citation_check.txt'), lock_epoch=CK.utc_epoch(face7, 'locked at (UTC)'), movesj=jl('b721_moves_lines.json'),
              answers=rdn('b721_author_answers.txt'), files=dict(c3pp=[x for x in g(PP, 'show', '--name-only', '--pretty=format:', K707.C3_PP).split(NL) if x.strip()]))
    live7 = CK.answers_before_ok(dict(S7))
    old7 = CK.answers_before_ok(dict(S7, answers=S7['answers'] + NL + '### PROMPT 9 (planted)'))
    new7 = CK.answers_before_ok(CK.answers_plant(dict(S7)))
    case('iv', 'G-ANSWERS-BEFORE-WRITES on b721`s banks: the live reading passes (the moves answer checked before its landing and the lock)', live7, True)
    case('iv', 'G-ANSWERS-BEFORE-WRITES: b721`s plant (a prompt appended) leaves the arm passing -- the control that cannot fail', old7, True)
    case('iv', 'G-ANSWERS-BEFORE-WRITES: the repaired plant (every check stamp moved after the write it governs) fails the arm', new7, False)
    ex7 = jl('b721_exercise.json').get('exercise') or {}
    case('iv', 'the seal`s refusal over b721`s exercise bank: the arms whose mutated copy passed, the one b721 carried',
         sorted(n for n, e in ex7.items() if e.get('pos')), ['G-ANSWERS-BEFORE-WRITES'])
    shown, bad = CK.neg_shown()
    case('iv', 'the seal refuses now: no pre-run exercise bank is written, so no arm is shown failing (every arm named)', (len(shown), len(bad) == len(CK.ARMS)), (0, True))
    # ---------------------------------------------------------------- THE ITEM REPAIRS: (k) THE HEAD LINE, (i) THE STEP BANK, THE 468
    import b721_closing as CL7
    hl_old = CL7.head_line()
    case('k', 'b721`s builder over b721`s captures: the head line carries the capture-name failure', 'IS NOT THE RECORD`S CAPTURE' in hl_old, True)
    case('k', 'the repaired builder over b721`s captures: the head line carries the record`s commits and no failure text',
         (hl_new.startswith('b721 closed: relay 2c200e8d, PLACE-papers df2dd7c; suite 137 of 143; root 11fe3e21e2fc796a'), '###' in hl_new), (True, False))
    case('k', 'the repaired builder sends both capture-name failures to the events section', len(ev), 2)
    notes += ['(k) the repaired head line over b721`s banks: %s' % hl_new] + ['(k) event: %s' % e for e in ev]
    lock7 = S7['lock_epoch']

    def _log(repo, base, tip):
        return [(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
                g(repo, 'log', '--reverse', '--format=%h %ct %s', '%s..%s' % (base, tip)).split(NL) if l.strip()]
    rl7, pl7 = _log(ROOT, K707.PRE_RELAY, 'b0d874f7'), _log(PP, K707.PRE_PP, 'df2dd7c0')
    ps7 = re.search(r'^POST_SEAL = (\(.*\))$', rd(os.path.join(T, 'b721_checks.py')), re.M)
    import ast
    post7 = ast.literal_eval(ps7.group(1)) if ps7 else ()
    old_sa = all((t < lock7) == (s.startswith('b721') and not s.startswith(post7)) for h, s, t in rl7 + pl7)
    case('i/step', 'G-SEALED-AFTER-COMPONENTS: b721`s subject reading over b721`s commits fails (7c07c5d4 "b721 order", df2dd7c0 "b721 trail")', old_sa, False)
    full = lambda repo, h: g(repo, 'rev-parse', h).strip()   # noqa: E731
    fixture = [dict(repo='relay', commit=full(ROOT, h), phase=('component 5' if t < lock7 else 'record')) for h, s, t in rl7] + \
              [dict(repo='pp', commit=full(PP, h), phase=('component 3' if t < lock7 else 'record')) for h, s, t in pl7]
    S8 = dict(lock_epoch=lock7, steps=fixture, rlog=rl7, plog=pl7, REC=sys.modules[__name__])
    case('i/step', 'the repaired reading over a step bank for b721`s commits (b721 had none: the fixture`s phases set from each commit`s time against '
                   'the lock, so this row shows the reading is by the bank alone) passes', CK.sealed_after_ok(S8), True)
    case('i/step', 'NEG: a PLACE-papers commit after the lock given a component phase fails',
         CK.sealed_after_ok(dict(S8, steps=[dict(r, phase='component 3') if r['repo'] == 'pp' else r for r in fixture])), False)
    case('i/step', 'NEG: a commit with no row in the step bank fails', CK.sealed_after_ok(dict(S8, steps=fixture[1:])), False)
    m82 = re.search(r'b682\s+cut: (\d+) characters', o3)
    mre = re.search(r'repaired cut: (\d+) characters', o3)
    meq = re.search(r'the whole answer (\d+) characters ; the repaired cut equal to the text from its BEGIN to its last END: (\w+)', o3)
    case('468', 'the citation tool`s answer check over b721`s root answer: b682`s cut 468 characters, the repaired cut to the last END, equal to the '
                'text from its BEGIN to its last END (tools/b722_citation.py replay, print only)',
         (m82.group(1) if m82 else None, bool(mre) and int(mre.group(1)) > 468, meq.group(2) if meq else None), ('468', True, 'True'))
    notes += ['(468) %s' % l.strip() for l in o3.split(NL) if l.strip()]
    L = ['%s -- COMPONENT 1, (R332)(2): THE FOUR STRUCTURAL REPAIRS AND THE THREE ITEM REPAIRS AGAINST THEIR OLD FORMS, WITH THEIR CONTROLS (%s)' % (ACT, utc()), '',
         '### rows are cases: the section | the case | the reading got | the reading wanted | AS WANTED. The sections: (i) the events section and the',
         '### letters at the seal (standing clauses v2 row (52)); (ii) the membrane (row (53)); (iii) arms read structure (row (54)); (iv) controls that',
         '### can fail (row (55)); (k) the closing`s head-line builder; (i/step) G-SEALED-AFTER-COMPONENTS by the step bank; (468) the answer check.',
         '### The repaired forms read where they stand: tools/b722_checks.py (no_verdict_line_ok, report_lines_ok, joined, the trail arms, sealed_after_ok,',
         '### answers_plant, neg_shown, prev_run_missing), tools/b722_closing.py (head_line, events_section), tools/act_membrane.py, tools/b722_citation.py.', '']
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


# ================================================================================ COMPONENT 1: THE REPAIRS AND THEIR DIFFS, (R332)(2)
REPAIRS = (
    ('(52)', '(R332)(2)(i), THE EVENTS SECTION',
     'tools/b722_closing.py events_section (the section beneath the defects: data/b722_events.txt`s rows and the head-line builder`s failures); '
     'tools/b722_checks.py the three trail-equality arms and G-TRAIL-DEFECTS-EQUAL`s Defects line read S[letters_seal], the letters entered before '
     'the seal, and the seal records them (`letters`, `defects_sha256`); tools/b722_record.py letters_of, letters_at_seal (the seal`s list, or for '
     'an act sealed before the repair its defects bank at the seal`s relay head), the defects route refusing a letter after the seal; EXCLUDE_KINDS '
     'events and steps. Control: data/b722_repair_controls.txt (i) -- the ruling`s control NOT AS WANTED on b721`s banks, defect (d)'),
    ('(53)', '(R332)(2)(ii), THE MEMBRANE',
     'tools/act_membrane.py (new, shared, whole below): appended, named, refuses, guard, guard_path; tools/b722_record.py b698`s put_json and '
     'put_txt wrapped and rebound in b703`s to b721`s modules; the guard before every bank write of tools/b722_citation.py (its two writers and '
     'the answer route`s rewritten body), tools/b722_closing.py, tools/b722_checks.py, tools/b722_independence.py, tools/b722_standing.py, '
     'tools/b722_tests.py and tools/b722_carry.py. THE READING, FOR THE AUTHOR`S STRIKE: "a named bank" is a bank the act`s root names (b721`s (j) '
     'quotes its ferry: "no named bank written after it") -- every file directly under relay data/ that the act`s ROOT_EXCLUDE does not take out; '
     'the mirror builder`s banks pass by name (the b670 form); the closing, its censuses and pins, the push captures, the defects, events and step '
     'banks are excluded kinds and stay writable after the root. Control: (ii) -- a test root refuses, a locator call leaves git status unchanged'),
    ('(54)', '(R332)(2)(iii), ARMS READ STRUCTURE',
     'tools/b722_checks.py no_verdict_line_ok (the gate`s NO VERDICT LINE rows read by the bank each names, NO_VERDICT_EXEMPT`s list of names '
     'removed -- the carry had turned b721`s entry into data/b721_prints_v0.17.txt, a bank that does not exist); report_lines_ok and '
     'report_unsealed_ok reading data/b722_report.json (its `at` and `lines`); joined kept for the registrations (no JSON bank); `--prev --part <p>` '
     'runs a part`s arms on b721`s banks (_prev_rebind, _PrevWorklist) and banks data/b722_prevrun_<part>.txt and data/b722_prevrun_exercise_<part>.json '
     'beside b721`s own verdicts (_prev_verdicts); the seal refuses while a part`s run is not banked (prev_run_missing). Control: (iii) -- the three '
     'needles pass on their acts` honest output and their NEG copies fail'),
    ('(55)', '(R332)(2)(iv), CONTROLS THAT CAN FAIL',
     'tools/b722_checks.py: the main loop records per arm `pos_raised` and `shown_failing` and per part the run`s `mode`, `at` and relay head; '
     'neg_shown reads the pre-run`s exercise banks; seal() refuses, recording nothing, while any arm`s mutated copy has not been shown failing '
     '(passed, raised, or no pre-run row); G-ANSWERS-BEFORE-WRITES`s plant answers_plant moves every check stamp after the write it governs. '
     'Control: (iv) -- b721`s plant leaves the arm passing, the repaired plant fails it'),
    ('(k)', 'THE CLOSING`S HEAD-LINE BUILDER (b721`s (k))',
     'tools/b722_closing.py head_line and _captures: each repository`s record commit the main its last capture of the act read back (the closing`s '
     'own excluded, ordered by the captures` stamps); a capture-name failure goes to HEAD_EVENTS and the events section, never the head line. '
     'Control: (k) -- over b721`s captures the line reads relay 2c200e8d, PLACE-papers df2dd7c, the two failures in the events section'),
    ('(i)', 'G-SEALED-AFTER-COMPONENTS BY THE STEP BANK (b721`s (i))',
     'tools/b722_record.py step (data/b722_steps.json: the repository, the commit, its time, the phase named from STEP_PHASES), PRE_SEAL_PHASES; '
     'tools/b722_checks.py sealed_after_ok and _step_phase reading the bank, not the subjects. Control: (i/step)'),
    ('468', 'THE CITATION TOOL`S ANSWER CHECK',
     'tools/b722_citation.py answer: b682`s cut `best.find(\'END\', k)` replaced by `best.rfind(\'END\')` in the rewritten body (checked to occur '
     'once); the replay route prints both cuts. Control: (468) -- b721`s root answer, 468 characters by b682`s cut, 1554 by the repaired, equal to '
     'the text from its BEGIN to its last END'),
)
REPAIR_TRACKED = ('tools/b722_record.py', 'tools/b722_citation.py', 'tools/b722_independence.py', 'tools/b722_standing.py', 'tools/b722_tests.py',
                  'tools/b722_carry.py', 'tools/b722_worklist.py')
REPAIR_CARRIED = ('checks', 'closing')


def toolrepairs(*a):
    """data/b722_tool_repairs.txt (.json), Component 1, (R332)(2): each repair's row (the delta's row of standing clauses v2, its objects, its
    control's section in data/b722_repair_controls.txt); the diffs: the tools committed at step zero (relay 4aa6e281) by `git diff HEAD`, the
    carried tools by their repairdiff banks (tools/b722_carry.py repairdiff), the new shared tool tools/act_membrane.py whole."""
    ctl = jl('%s_repair_controls.json' % ACT)
    if not ctl.get('cases'):
        sys.exit('### data/b722_repair_controls.json IS NOT WRITTEN -- THE CONTROLS FIRST; NOTHING WRITTEN')
    nw = [c for c in ctl['cases'] if not c.get('as_wanted')]
    L = ['%s -- COMPONENT 1, (R332)(2): THE FOUR STRUCTURAL REPAIRS (STANDING CLAUSES v2 ROWS (52)-(55)) AND THE THREE ITEM REPAIRS, WITH THEIR DIFFS (%s)' % (ACT, utc()), '',
         '### rows are repairs: the row | what is repaired | its objects, the reading and its control. The controls: relay data/b722_repair_controls.txt',
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


# ================================================================================ COMPONENT 2, (R332)(4): THE PORT (b709's portedit, portdispatch and portrun, :1745-:1932, carried)
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
# ### (R332)(4): the port's edits, one per held line, each in the form Mathlib de5ce8a9 states, each read there and printed before its edit
PORT_EDITS = (
    dict(n=1, line=501, base=K.PORT_TIP,
         old='  rw [completedHurwitzZetaOdd, StrongFEPair.Λ_eq, norm_div, show ‖(2 : ℂ)‖ = 2 by norm_num]',
         new='  rw [completedHurwitzZetaOdd, (isStrong_hurwitzOddFEPair a).Λ_eq, norm_div, show ‖(2 : ℂ)‖ = 2 by norm_num]',
         error='error: SIDELvConservation/DirichletC7Order.lean:501:31: Unknown identifier `StrongFEPair.Λ_eq` (data/b721_port.txt :11)',
         decls=(('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 100, 100, 'the strong pair a predicate on a weak pair'),
                ('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 461, 481, 'IsStrongFEPair.Λ_eq, its hypothesis hP explicit'),
                ('Mathlib/NumberTheory/LSeries/HurwitzZetaOdd.lean', 300, 302, 'the odd pair a WeakFEPair'),
                ('Mathlib/NumberTheory/LSeries/HurwitzZetaOdd.lean', 325, 327, 'the odd pair`s strong proof'),
                ('Mathlib/NumberTheory/LSeries/HurwitzZetaOdd.lean', 339, 340, 'completedHurwitzZetaOdd through the pair`s Λ'))),
    dict(n=2, line=574, base='42da39ea2c03859ef6e74a9b752d9783816b430a',
         old='      (((hurwitzOddFEPair a).hasMellin w).1).norm',
         new='      (((isStrong_hurwitzOddFEPair a).hasMellin w).1).norm',
         error=('error: SIDELvConservation/DirichletC7Order.lean:574:39: Application type mismatch: the argument w : ℂ where '
                '(hurwitzOddFEPair a).k < re ?m is expected, in WeakFEPair.hasMellin (hurwitzOddFEPair a) w (data/b722_buildlog_SIDE-lv-conservation_port1.txt :99-:106)'),
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
    """`portedit <n> pre` -> data/b722_port_decl<n>.txt: the declarations the edit's form rests on, read at Mathlib de5ce8a9 by git show (the pin
    read from SIDE-explicit-formula's checkout, HEAD equal to it), printed BEFORE the Edit tool touches the kernel; the line as it stands, unedited.
    `portedit <n>` -> data/b722_port_edit<n>.txt (.json): the line as it stood at the edit's base and as the Edit tool left it, the diff of the
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
        L = ['%s -- COMPONENT 2, (R332)(4): THE DECLARATIONS AT MATHLIB %s FOR THE PORT`S EDIT %d, PRINTED BEFORE THE EDIT (%s)' % (ACT, MATHLIB_PIN[:8], e['n'], utc()), '',
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
    L = ['%s -- COMPONENT 2, (R332)(4): THE PORT`S EDIT %d AT :%d ON %s, PRINTED BEFORE ITS COMMIT (%s)' % (ACT, e['n'], e['line'], K.PORT_BRANCH, utc()), '',
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
    """data/b722_regpos.txt (.json), (R332)(4): lv-conservation's Register4_positivity read at the deposit 93c27ec and at the port's tip, each by
    git show, its declaration printed with its line and its namespaces; EQUAL BY STATEMENT where the lines are equal character for character
    and the namespaces equal. The module's diff between the two commits printed beside it (git diff --stat and the hunks of the file)."""
    tip = g(LV, 'rev-parse', K.PORT_BRANCH).strip()
    l0, d0, n0 = _decl_at(K.LV_V0100, REGPOS_FILE, REGPOS_NAME)
    l1, d1, n1 = _decl_at(tip, REGPOS_FILE, REGPOS_NAME)
    eq = bool(d0) and d0 == d1 and n0 == n1
    fd = subprocess.run(['git', '-C', LV, 'diff', K.LV_V0100, tip, '--', REGPOS_FILE], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL)
    fdl = fd.split(NL) if fd else []
    L = ['%s -- COMPONENT 2, (R332)(4): lv-conservation`S %s AT THE DEPOSIT AND AT THE PORT`S TIP, BY STATEMENT (%s)' % (ACT, REGPOS_NAME, utc()), '',
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
    """data/b722_join_grade.txt (.json), (R332)(4): faces_join graded against lv-conservation's own declaration -- its statement printed from
    FacesJoin.lean at the built ref (git show), the lakefile's lv-conservation pin read at that ref, Register4_positivity's declaration from
    data/b722_regpos.json, the run's row (data/b722_runner_SIDE-faces-join_join.txt) and its #print axioms (data/b722_axioms_SIDE-faces-join_join.txt);
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
    L = ['%s -- COMPONENT 2, (R332)(4): faces_join GRADED AGAINST lv-conservation`S OWN DECLARATION (%s)' % (ACT, utc()), '',
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
    """data/b722_join_tag.txt (.json), (R332)(4): SIDE-faces-join's tag v0.1.0 read back -- the tag object and its peel locally, the remote's
    tag ref and its peel by one ls-remote; the peel against the graded ref (data/b722_join_grade.json). Reads only; the tag was made by
    tools/push_gated.sh after main read back."""
    jg = jl('%s_join_grade.json' % ACT)
    obj = g(K.JOIN_DIR, 'rev-parse', 'v0.1.0').strip()
    peel = g(K.JOIN_DIR, 'rev-parse', 'v0.1.0^{commit}').strip()
    rem = [l.split() for l in g(K.JOIN_DIR, 'ls-remote', '--tags', 'origin', 'v0.1.0*').split(NL) if l.strip()]
    r_obj = next((h for h, r in rem if r == 'refs/tags/v0.1.0'), '')
    r_peel = next((h for h, r in rem if r == 'refs/tags/v0.1.0^{}'), '')
    ok = bool(peel) and peel == r_peel == jg.get('ref') and obj == r_obj and jg.get('grade') == 'DERIVES'
    L = ['%s -- COMPONENT 2, (R332)(4): SIDE-faces-join TAGGED v0.1.0 ON DERIVES, THE PEELED SHA READ BACK (%s)' % (ACT, utc()), '',
         '### the grade: data/%s_join_grade.txt, %s at %s' % (ACT, jg.get('grade'), (jg.get('ref') or '')[:8]),
         '### local: the tag object %s ; peeled %s' % (obj, peel),
         '### the remote (ls-remote --tags origin): the tag object %s ; peeled %s' % (r_obj or '### ABSENT', r_peel or '### ABSENT'),
         '', '### ### **v0.1.0: PEELED LOCAL %s REMOTE %s ; THE GRADED REF %s ; EQUAL %s.**' % (peel[:8], r_peel[:8], (jg.get('ref') or '')[:8], ok)]
    put_txt('%s_join_tag.txt' % ACT, L)
    put_json('%s_join_tag.json' % ACT, dict(at=utc(), tag='v0.1.0', object=obj, peeled=peel, remote_object=r_obj, remote_peeled=r_peel, ok=ok))
    print(NL.join(L))
    if not ok:
        sys.exit(1)


def _portedit_b721(*a):
    """b721's portedit (:212), carried as read; pruned before the seal."""
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
    L = ['%s -- COMPONENT 2, (R332)(4): THE PORT`S LINE :%d ON %s, PRINTED BEFORE THE ONE COMMIT (%s)' % (ACT, K.PORT_LINE, K.PORT_BRANCH, utc()), '',
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
    tree state (refused where data/b722_dispatches.json carries the tree), at most two dispatches this act ((R332) N1), the branch's tip read back
    at the remote by one ls-remote before the dispatch; the host's free memory printed before it and the hold read ((R332)(8))."""
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
        sys.exit('### %d PORT DISPATCHES ALREADY MADE THIS ACT ((R332)(4)) -- NOT DISPATCHED' % K.MAX_PORT_DISPATCHES)
    if len(rows) >= K.MAX_DISPATCHES:
        sys.exit('### %d DISPATCHES ALREADY MADE THIS ACT ((R332) N1) -- NOT DISPATCHED' % K.MAX_DISPATCHES)
    if not re.match(r'^[A-Za-z0-9_. ]+$', target):
        sys.exit('### THE TARGET %r IS OUTSIDE THE LAKE GRAMMAR -- NOT DISPATCHED' % target)
    remote = (g(LV, 'ls-remote', 'origin', 'refs/heads/' + K.PORT_BRANCH).split() or [''])[0]
    import b722_tests as TT
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
    (R332)(4). data/b722_port.txt (.json)."""
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
    L = ['%s -- COMPONENT 2, (R332)(4): THE PORT RUN OF SIDE-lv-conservation ON %s AT ITS NEW TIP, READ BY ITS RUN ID; THE OUTCOME BY FILE AND LINE (%s)' % (ACT, K.PORT_BRANCH, utc()), '',
         '### the dispatch: the branch %s at its tip (this act`s edit on b721`s %s), the workflow at the branch, target SIDELvConservation (data/b722_dispatches.json)' % (K.PORT_BRANCH, K.PORT_TIP[:8]),
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
          '### where the build completes: %s' % ('THE BUILD COMPLETES, 12 of 12 -- (R332)(4): Register4_positivity read at 93c27ec and at the tip, the join`s lakefile re-pinned, one join dispatch'
                                                  if complete else 'not complete at this run; (R332)(4)`s join not reached, its dispatch not made'),
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
    # ### (R332)(4): up to three port runs, each its own bank by its label (port1, port2, port3); data/b722_port.txt carries them all, in order
    put_txt('%s_port_%s.txt' % (ACT, label), L)
    runs = sorted(f for f in os.listdir(D) if re.match(r'^%s_port_port\d\.txt$' % ACT, f))
    allL = ['%s -- COMPONENT 2, (R332)(4): THE PORT`S RUNS, EACH READ BY ITS RUN ID, EACH HELD LINE BY FILE AND LINE (%s) ; RUNS %d of at most %d' % (
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
ALLOWED_SHARED_DATA = ('act_roots.txt', 'b721_closing_push_out.txt', 'b675_corrigenda.txt', 'standing_clauses_v3.txt')
def _s_scores():
    return dict((k, (v[0], v[1].replace('b698_', ACT + '_'))) for k, v in R._s_scores().items())


def _bfig(name, pat, what):
    """a figure read from this act's bank by its pattern; the composition refuses where the bank does not carry it."""
    m = re.search(pat, rdn(name))
    if not m:
        sys.exit('### data/%s DOES NOT CARRY %s (%s) -- NOTHING COMPOSED' % (name, what, pat))
    return m.groups()


def _genus_ok(gc):
    """the genus control as its bank reads (data/b722_genus_control.json): no miss through n_max, the hand rows read, both planted copies missing."""
    return gc.get('misses') == [] and gc.get('hand') is True and (gc.get('planted_form_misses') or 0) > 0 and (gc.get('planted_sign_misses') or 0) > 0


CLASS_REPAIRS = ('(3i)', '(3ii)', '(3iii)', '(3iv)', '(3v)', '(3vi)', '(i)', '(ii)', '(iv)', '(v)', '(vi)')   # ### (R332)(3) and v1.0.0's, tools/standing/controls.py's


def _section(text, head, nxt):
    """the text of a bank from the line opening `head` to the line opening `nxt` (or the end)."""
    i = text.find(head)
    if i < 0:
        return ''
    j = text.find(nxt, i + len(head)) if nxt else -1
    return text[i:j] if j > 0 else text[i:]


def _pred34(rg, name):
    """one h = 3, 4 prediction as section (5) of the registrations writes it: (D, n0, factorization, a, the pair sum, b, the model's n0, b)."""
    m = re.search(r'(?s)%s \(D = (-\d+);.*?\(a\) the table: n0 = (\d+) = (\S+ \. \S+) .*?a\(\d+\) = (\d+), the pair sum (\d+), b\(\d+\) = (-?[\d/]+)\.'
                  r'.*?\(b\) the model`s own least negative index over every Omega to the cut: n0 = (\d+), b = (-?[\d/]+) -- THE SAME n0' % re.escape(name),
                  rg.replace("model's", 'model`s'))
    if not m:
        sys.exit('### data/b722_registrations.txt DOES NOT CARRY %s`s prediction -- NOTHING COMPOSED' % name)
    return m.groups()


def _figs():
    """every figure the entry, the trail and the components print, read from b722's banks (Component 8, the Edit tool, over b722's objects;
    b721's form over b721's objects in git at b721's record tool): the corrigendum's foot and v1.2.2's controls; -31 and -55 under e8c3dff4;
    the fourteen under H-C2-WALK and the walk's grade; the C2 statement's E0 grade and its price; the instruments' rule and the reproduction
    run; the propagation read and its landing; the axiom step's diagnosis; the LLM-contribution line; the address scan; each by its own lines
    through _bfig, which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
    co = jl('%s_corrigendum.json' % ACT)
    rl = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    fj_, f10 = jl('%s_standing_figures.json' % ACT), jl('b721_standing_figures.json')
    ci = _bfig('%s_corrigendum.txt' % ACT, r'\*\*ITEMS (\d+): EVENTS (\d+), DEFECTS (\d+) ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ;.*THE ENTRY AT FINDINGS :(\d+)\.\*\*',
               'the corrigendum`s foot')
    v2 = _bfig('%s_standing_v122.txt' % ACT, r'\*\*v1\.2\.2: CASES (\d+), AS WANTED (\d+) ;', 'v1.2.2`s controls')
    cf = _bfig('%s_coeffs.txt' % ACT, r'\*\*n0\(-31\) = (\d+), b = (-?[\d/]+) ; n0\(-55\) = (\d+), b = (-?[\d/]+) ; H-C3-31 (HELD|REFUTED) ; '
               r'H-C4-55 (HELD|REFUTED) ;', 'the coefficients` foot')
    cc = jl('%s_coeffs_controls.json' % ACT)
    wk = _bfig('%s_walk.txt' % ACT, r'\*\*H-C2-WALK: (\d+) OF 14 HELD, REFUTED (\d+), NOT SCORABLE (\d+) ; THE CONTROL ROW -15 (HELD|REFUTED) ;', 'the walk`s foot')
    wg, = _bfig('%s_walk.txt' % ACT, r'(?m)^### THE GRADE: (the value law .*)$', 'the walk`s grade')
    e0, = _bfig('%s_c2_price.txt' % ACT, r'(?m)^  THE GRADE: (\w+) -- ', 'the C2 statement`s E0 grade')
    cp = _bfig('%s_c2_price.txt' % ACT, r'\*\*THE C2 STATEMENT: E0 (\w+) ; SCOPE BESIDE IT \(([^)]*)\) ; AS WRITTEN, TRUE IN PYTHON AT (\d+) OF (\d+) ; '
               r'PRICED: \(A\) decide as written (\S+) TO (\S+) LATTICE POINTS, UNMEASURED IN LEAN, \(B\) THE CERTIFICATE ROUTE UNDER (\S+) AT (\d+) OF '
               r'(\d+), TWO LEMMAS NAMED ;', 'the C2 price`s foot')
    ins = _bfig('%s_instruments.txt' % ACT, r'\*\*THE RULE`S OUTPUT: (\d+) INSTRUMENTS \((\d+) NEW, TO BE ENTERED AS I-(\d+) TO I-(\d+)\) ; POPULATION (\d+), '
                r'REUSED (\d+), \(S1\) (\d+), \(S2\) (\d+) ; THE NAVIGATOR`S (\d+): (\d+) IN THE OUTPUT ; UNREAD BY HAND (\d+) ;', 'the instruments` foot')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    pg = _bfig('%s_propagation.txt' % ACT, r'\*\*THE PROPAGATION READ: OBJECTS (\d+) ; HITS (\d+) ; COPY (\d+) ; DATED (\d+) ; NOT THIS OBJECT (\d+) ; '
               r'READS RIGHT (\d+) ; READS WRONG (\d+) ; NOTES TO WRITE (\d+) ; UNREAD (\d+) ;', 'the propagation read`s foot')
    pl = (jl('%s_propagation_landing.json' % ACT).get('lines') or [{}])[0].get('line')
    ax = _bfig('%s_axiom_diag.txt' % ACT, r'\*\*THE AXIOM STEP AT FIVE PINS: TARGETS ABSENT AT THE PIN (\d+) ; BUILD TARGET NOT COVERING THE AXIOM FILE`S '
               r'IMPORTS (\d+) ; STEP NOT THE PIN`S OWN (\d+) ; OTHER (\d+) ; NOTHING COMMITTED, PUSHED OR DISPATCHED ;', 'the axiom diagnosis` foot')
    ll = _bfig('%s_llm_line_drafts.txt' % ACT, r'\*\*THE LLM-CONTRIBUTION LINE \(PLACE-papers day1/A_Place_to_Stand\.md :(\d+)\) AGAINST (\d+) WAVE 1 PAPERS '
               r'AND (\d+) KERNEL READMES: SAME (\d+) ; DIFFERS (\d+) ; ABSENT (\d+) ; DRAFTS (\d+) ; NOTHING EDITED ;', 'the LLM line`s foot')
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PLACES (\d+) ; CONTROLS 3 OF 3 AS WANTED ;',
               'the address scan`s foot')
    ver = (R.rd(os.path.join(ROOT, 'tools', 'standing', 'VERSION')) or '').strip()
    if not re.match(r'^v\d+\.\d+\.\d+$', ver):
        sys.exit('### tools/standing/VERSION DOES NOT CARRY A VERSION (%r) -- NOTHING COMPOSED' % ver)
    ctr = _counter()
    return dict(weight=rl[0], corr_line=ci[6], corr_items=ci[0], corr_events=ci[1], corr_defects=ci[2], corr_claim=ci[3], corr_close=ci[4],
                corr_repeat=ci[5], corr_row=co.get('row'), v122_cases=v2[0], v122_wanted=v2[1],
                n31=cf[0], b31=cf[1], n55=cf[2], b55=cf[3], h31=cf[4], h55=cf[5], ctl_ok=bool(cc) and cc.get('ok') is True and cc.get('c1') is True,
                walk_held=wk[0], walk_refuted=wk[1], walk_unscor=wk[2], walk_ctl=wk[3], walk_grade=wg,
                e0=e0, c2_grade=cp[0], c2_scope=cp[1], c2_true=cp[2], c2_of=cp[3], c2_lo=cp[4], c2_hi=cp[5], c2_bound=cp[6], c2_under=cp[7], c2_under_of=cp[8],
                ins_n=int(ins[0]), ins_new=ins[1], ins_first=ins[2], ins_last=ins[3], ins_pop=ins[4], ins_reused=ins[5], ins_s1=ins[6], ins_s2=ins[7],
                ins_nav=ins[8], ins_nav_in=ins[9],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                pg_obj=pg[0], pg_hits=pg[1], pg_copy=pg[2], pg_dated=pg[3], pg_other=pg[4], pg_right=pg[5], pg_wrong=pg[6], pg_notes=int(pg[7]), pg_unread=pg[8],
                pg_line=pl,
                ax_absent=ax[0], ax_cover=ax[1], ax_notown=ax[2], ax_other=ax[3],
                ll_line=ll[0], ll_papers=ll[1], ll_readmes=ll[2], ll_same=ll[3], ll_differs=ll[4], ll_absent=ll[5], ll_drafts=ll[6],
                addr=ad[0], name=ad[1], addr_places=ad[2],
                ver=ver, claim=ctr['claim'], close=ctr['close'], untagged=ctr['untagged'],
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                figs10=dict((k, (f10.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')))


TAG_ROW = re.compile(r"^    \((?:[a-z]'?|\d+)\) [^\[]*\[(CLAIM|CLOSE)\b", re.M)


def _counter(act=ACT):
    """(R332)(2): the counter CLAIM n, CLOSE m over the act's events and defects together -- every row of data/<act>_defects.txt and
    data/<act>_events.txt opening four spaces and its letter or number, tagged by its first bracket; a row carrying no tag counted apart."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):
        rows += [l for l in rdn(name).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    tags = [TAG_ROW.match(l) for l in rows]
    return dict(claim=sum(1 for m in tags if m and m.group(1) == 'CLAIM'), close=sum(1 for m in tags if m and m.group(1) == 'CLOSE'),
                untagged=[l[:12].strip() for l, m in zip(rows, tags) if not m])


def counter(*a):
    """`counter`: the counter line of (R332)(2), printed; writes nothing."""
    c = _counter()
    print('  CLAIM %d, CLOSE %d%s' % (c['claim'], c['close'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else ''))


def _figs_b721():
    """b721's form over b721's objects, kept for the record and not called (Component 6)."""
    co = jl('%s_corrigendum.json' % ACT)
    rl = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    fj_, f10 = jl('%s_standing_figures.json' % ACT), jl('b721_standing_figures.json')
    fr = co.get('fraction') or []
    ver = (R.rd(os.path.join(ROOT, 'tools', 'standing', 'VERSION')) or '').strip()
    if not re.match(r'^v\d+\.\d+\.\d+$', ver):
        sys.exit('### tools/standing/VERSION DOES NOT CARRY A VERSION (%r) -- NOTHING COMPOSED' % ver)
    sc_files, sc_lit, sc_prose, sc_del = _bfig('%s_standing_scan.txt' % ACT, r'\*\*FILES (\d+) ; LITERALS IN THE CODE (\d+) \(.*?\) ; PROVENANCE IN THE PROSE (\d+) ;'
                                               r' DELETE WORDS IN THE CODE (\d+)\.\*\*', 'the scan`s foot')
    rp = _bfig('%s_replay.txt' % ACT, r'\*\*OBJECTS (\d+) ; EQUAL (\d+) ; DIFFERS (\d+) (\[[^]]*\]) ; NAMED (\d+) ; UNNAMED (\d+) ; FINDINGS (\d+)\.\*\*', 'the replay`s foot')
    cv = _bfig('%s_toolset_coverage.txt' % ACT, r"\*\*STEPS (\d+) ; STANDING (\d+) \(([^)]*)\) BESIDE v1\.0\.0'S (\d+) \(\[18\]\) ; PER-ACT (\d+) ; MOVED BY THIS VERSION (\d+) ",
               'the coverage table`s foot')
    cc = _bfig('%s_standing_controls.txt' % ACT, r'\*\*CASES (\d+) ; AS WANTED (\d+) ; REPAIRS (\d+), EACH WITH BOTH INSTANCES (True|False) ; ALL AS WANTED (True|False)\.\*\*',
               'the class controls` foot')
    ro, = _bfig('%s_roster.txt' % ACT, r'\*\*ROSTER CONTROLS (\d+) ; AS WANTED \1 ; ALL AS WANTED True\.\*\*', 'the roster`s controls')
    joins = re.findall(r'(?m)^\s*JOINS (\S+)', rdn('%s_roster.txt' % ACT))
    gm, = _bfig('%s_genus_control.txt' % ACT, r'\*\*THE FORMS h = 4 AS WANTED ; THE DECOMPOSITION READ THROUGH n = 400 ; MISSES (\d+) ;', 'the count control`s foot')
    ks = _bfig('%s_keystone.txt' % ACT, r'\*\*\(iii\) CORRECTED, ERRATA (E-[\d-]+) ; \(iv\) (\d+) OF (\d+) PINNED, (\d+) CARRIED ; .* FILES EDITED ON MAIN (\d+)\.\*\*', 'the keystone bank`s foot')
    pr = _bfig('%s_price.txt' % ACT, r'BASE AND FIRST TWO TIERS ([\d.]+) h UPPER, ([\d.]+) h LOWER ; THE CUT (\d+) ; THE SEAT`S ACT BUDGET ABOUT ([\d.]+) FOREGROUND HOURS ; NOTHING OF -39 COMPUTED',
               'the -39 price`s foot')
    fp = _bfig('%s_federation_pin_price.txt' % ACT, r'\*\*PUBLIC KERNELS (\d+) ; WITH MATHLIB (\d+) ; REVS (\d+) ; THE TARGET ([0-9a-f]+) ; BELOW IT (\d+) ; DISPATCHES PRICED (\d+), ([\d.]+) RUNNER HOURS ;'
               r'.* REQUESTS (\d+), FAILED (\d+) ; NOTHING BUILT\.\*\*', 'the federation price`s foot')
    ep = _bfig('%s_epstein_count_price.txt' % ACT, r'\*\*THE BAND \[([\d, ]+)\] AT Q0, N (\d+), ALL ON THE LINE ; .* ; (\d+-\d+) DISPATCHES, (\d+-\d+) FOREGROUND HOURS \(THE SEAT`S\) ; THE GRADE (\w+) \(E0\), ONE BAND ; NOTHING BUILT\.\*\*',
               'the Lean count price`s foot')
    nf = int(rp[6])
    return dict(weight=rl[0], corr_line=co.get('entry_line', '-'), corr_row=co.get('row'), corr_n=len(co.get('lettered') or []), corr_rec=len(co.get('records') or []),
                corr_items=len(co.get('starts') or []), rep=('%s of %s' % (fr[0], fr[1])) if len(fr) >= 2 else '-',
                rep_f=('%.2f' % (float(fr[0]) / float(fr[1]))) if len(fr) >= 2 and float(fr[1]) else '-',
                ver=ver, sc_files=sc_files, sc_lit=sc_lit, sc_prose=sc_prose, sc_del=sc_del,
                rp_obj=rp[0], rp_eq=rp[1], rp_diff=rp[2], rp_diffs=rp[3], rp_named=rp[4], rp_unnamed=rp[5], rp_find=rp[6],
                replay_word=('EQUAL' if rp[2] == '0' and nf == 0 else 'with %d finding%s' % (nf, '' if nf == 1 else 's')),
                cv_steps=cv[0], cv_std=cv[1], cv_std_at=cv[2], cv_std_prev=cv[3], cv_per=cv[4], cv_moved=cv[5],
                cc_cases=cc[0], cc_wanted=cc[1], cc_repairs=cc[2], cc_both=cc[3], cc_all=cc[4], n_repairs=int(cc[2]),
                ro_ctl=ro, ro_joins=[os.path.basename(j) for j in joins], g_miss=gm,
                ks_errata=ks[0], ks_pinned=ks[1], ks_names=ks[2], ks_carried=ks[3], ks_files=ks[4],
                pr_up=pr[0], pr_low=pr[1], pr_cut=pr[2], pr_budget=pr[3],
                fp_kern=fp[0], fp_ml=fp[1], fp_revs=fp[2], fp_target=fp[3], fp_below=fp[4], fp_disp=fp[5], fp_hours=fp[6], fp_req=fp[7], fp_fail=fp[8],
                ep_band=ep[0], ep_n=ep[1], ep_disp=ep[2], ep_hours=ep[3], ep_grade=ep[4],
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                figs10=dict((k, (f10.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')))


def _artifacts_read():
    """each dispatch of the dispatch bank paired with its run bank: (label, run id, artifact sha256, agreeing) -- the port's per-label banks
    (data/b722_port_port1.json, data/b722_port.json) and the join's runner bank (data/b722_runner_SIDE-faces-join_join.txt, its artifact row)."""
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


def _rebuild_rows():
    rr = R.rd(os.path.join(ROOT, *K.REBUILD_ROWS.split('/')))
    return json.loads(rr) if rr else []


def _diag_rows():
    """(R332)(10): the axiom step's diagnosis as banked (data/b722_axiom_diag.json), one row per run read by its id."""
    p = os.path.join(D, '%s_axiom_diag.json' % ACT)
    return json.loads(R.rd(p)) if os.path.exists(p) else []


def _n1():
    """N1 (R332): no lean process runs on this host and no runner is dispatched this act; (R332)(10) reads b721's runs by their ids. From the
    command bank (the seat's commands, read live from the capture by the `commands` route: local lean none, dispatches none) and the axiom
    diagnosis (each of the five runs the ruling names read by its id, each read a GET; its foot NOTHING COMMITTED, PUSHED OR DISPATCHED)
    (Component 8, the Edit tool; b721's N1 read its rebuild's dispatches)."""
    cm = jl('%s_commands.json' % ACT)
    seat_lean = cm.get('local_lean') if cm else None
    disp = (cm.get('dispatches') or []) if cm else None
    rows = _diag_rows()
    read = dict((r.get('kernel'), str(r.get('run'))) for r in rows)
    want = dict((k, str(r)) for k, r in K.AXIOM_RUNS)
    foot = 'NOTHING COMMITTED, PUSHED OR DISPATCHED' in rdn('%s_axiom_diag.txt' % ACT)
    ok = bool(cm) and not seat_lean and disp == [] and K.MAX_DISPATCHES == 0 and read == want and foot
    return ('HELD' if ok else 'REFUTED'), (
        'the seat`s commands running lean or lake on this host (relay data/b722_commands.json): %s; dispatch commands in the capture: %s; '
        'b721`s runs read by their ids in the axiom diagnosis (relay data/b722_axiom_diag.json), the ruling`s five: %s (%s); the diagnosis` '
        'foot NOTHING COMMITTED, PUSHED OR DISPATCHED: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', (len(disp) if disp else 'NONE') if cm else 'unread', read == want,
            ', '.join('%s %s' % (k, read.get(k, 'UNREAD')) for k, _r in K.AXIOM_RUNS), foot))


def _order_of(commit, rows):
    return next((i for i, h in enumerate(rows) if h.startswith(commit[:8])), None)


def _ctl_before(text, ctl, fig):
    i, j = (text or '').find(ctl), (text or '').find(fig)
    return 0 <= i < j


# ### N2 (Component 8, the Edit tool, over b722's objects; b721's chain over b721's registrations in git at b721's record tool): each
# ### computation's bank, the registration it names and that registration's commit, an ancestor of the computation's commit
N2_COMPUTED = (('data/b722_coeffs.txt', 'e8c3dff4', 'REG_C3', 'C3_RELAY'), ('data/b722_walk.txt', '15cb6cc4', 'REG_WALK', 'C3_RELAY'))
# ### N2: each tool's controls (or its rule) before its figures, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b722_coeffs.txt', '### THE CONTROLS FIRST', '## D = -31'),
               ('data/b722_walk.txt', 'THE CONTROLS FIRST', '## D = -15'),
               ('data/b722_instruments.txt', 'THE RULE ((R332)(6)), printed before any tool is named', '## THE YIELDS'),
               ('data/b722_axiom_diag.txt', '### THE RULE, PRINTED BEFORE ANY KERNEL', '## SIDE-kernel'),
               ('data/b722_llm_line_drafts.txt', '## THE CONTROLS, BEFORE ANY DOCUMENT', '## paper d1-1'),
               ('data/b722_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'))


def _first_tool_line(text):
    """the first line naming a concrete act-numbered tool (bNNN_<name>), 1-based, or None."""
    for i, l in enumerate((text or '').split(NL), 1):
        if re.search(r'\bb\d{3}_[a-z]\w*', l):
            return i
    return None


def _names_before(text):
    """the propagation bank's objects: each `## OBJECT` section's names line before its first graded row, (object head, True|False)."""
    out = []
    for sec in re.split(r'(?m)^(?=## OBJECT )', text or '')[1:]:
        L = sec.split(NL)
        nm = next((i for i, l in enumerate(L) if 'ITS NAMES, PRINTED BEFORE THE SEARCH' in l), None)
        row = next((i for i, l in enumerate(L) if re.match(r'^  (READS RIGHT|READS WRONG|DATED|NOT THIS OBJECT|COPY)\b', l)), None)
        out.append((L[0][:24], nm is not None and row is not None and nm < row))
    return out


def _n2():
    """N2 (R332): every computation at -31 and -55 names e8c3dff4 as its registration and every computation at the fourteen names H-C2-WALK at
    the commit that landed it (15cb6cc4), each registration's commit an ancestor of the computation's bank; b721's registrations unchanged at
    HEAD; each tool's controls print before its figures (the controls' own commit before the figures' commit); the instruments' rule prints
    before any instrument is named; each propagation object's names print before its search. From git (merge-base, the blob at HEAD against
    the registration's commit) and the banks' own lines."""
    named = [(p, n in rdn(os.path.basename(p))) for p, n, _r, _c in N2_COMPUTED]
    anc = [(p, grc(ROOT, 'merge-base', '--is-ancestor', getattr(K, r), getattr(K, c)) == 0) for p, _n, r, c in N2_COMPUTED]
    reg_same = bool(_show(ROOT, 'HEAD', K.REGISTRATIONS)) and (_show(ROOT, K.REG_C3, K.REGISTRATIONS) or '') == (_show(ROOT, 'HEAD', K.REGISTRATIONS) or '')
    ctl_commit = grc(ROOT, 'merge-base', '--is-ancestor', K.C2_CTL, K.C3_RELAY) == 0 and K.C2_CTL != K.C3_RELAY \
        and 'data/b722_coeffs_controls.json' in g(ROOT, 'show', '--name-only', '--format=', K.C2_CTL).split() \
        and not [x for x in g(ROOT, 'show', '--name-only', '--format=', K.C2_CTL).split() if x in ('data/b722_coeffs.txt', 'data/b722_walk.txt')]
    ctl = [(p, _ctl_before(rdn(os.path.basename(p)), a, b)) for p, a, b in N2_CONTROLS]
    it = rdn('%s_instruments.txt' % ACT)
    rule_at = next((i for i, l in enumerate(it.split(NL), 1) if l.startswith('THE RULE ((R332)(6))')), None)
    first_tool = _first_tool_line(it)
    rule_first = rule_at is not None and first_tool is not None and rule_at < first_tool
    nb = _names_before(rdn('%s_propagation.txt' % ACT))
    ok = all(o for _p, o in named) and all(o for _p, o in anc) and reg_same and ctl_commit and all(o for _p, o in ctl) and rule_first \
        and len(nb) == 3 and all(o for _h, o in nb)
    return ('HELD' if ok else 'REFUTED'), (
        'the computations naming their registrations (relay data/b722_coeffs.txt e8c3dff4, data/b722_walk.txt 15cb6cc4): %s; each registration`s '
        'commit an ancestor of the computation`s %s (git merge-base --is-ancestor): %s; relay data/b721_registrations.txt at HEAD equal to its blob '
        'at e8c3dff4: %s; the controls committed at %s, alone of the figures, before the figures` %s: %s; each tool`s controls or rule before its '
        'figures: %s; the instruments` rule at :%s before the first tool named at :%s: %s; each propagation object`s names before its search: %s' % (
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in named), K.C3_RELAY[:8], ', '.join('%s %s' % (os.path.basename(p), o) for p, o in anc),
            reg_same, K.C2_CTL[:8], K.C3_RELAY[:8], ctl_commit, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl), rule_at, first_tool,
            rule_first, ', '.join('%s %s' % x for x in nb) or 'NONE READ'))


# ### N3 (Component 8, the Edit tool, over b722's objects; b721's over its table, offset and rebuild in git at b721's record tool): the banks
# ### whose grade prints at their end, (bank, the words the foot carries for its grade)
N3_GRADED = (('b722_coeffs.txt', ('H-C3-31 HELD', 'H-C4-55 HELD')), ('b722_walk.txt', ('HELD',)), ('b722_c2_price.txt', ('E0 DERIVES',)),
             ('b722_instruments.txt', ('THE RULE`S OUTPUT',)), ('b722_reproduce.txt', ('REPRODUCES',)), ('b722_propagation.txt', ('READS RIGHT', 'READS WRONG')),
             ('b722_axiom_diag.txt', ('TARGETS ABSENT AT THE PIN', 'STEP NOT THE PIN`S OWN')), ('b722_llm_line_drafts.txt', ('SAME', 'DIFFERS', 'ABSENT')))
# ### N3: a sentence calling the exhaustion compiled -- "compiled" not read with its negation (not, never, nor)
N3_COMPILED = re.compile(r'(?i)\bcompiled\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|never|nor|un)[ -]?(?:yet |been |\w+ and not )?compiled\b')


def _n3():
    """N3 (R332): every grade prints at its end; the exhaustion of (4) is graded as Python-checked over a cited list, and no sentence of the
    entry calls it compiled; the C2 statement's grade is E0's printed reading. From the graded banks (each bank's last line its foot, the foot
    carrying its grade's words; the walk's THE GRADE after every row it grades), the walk's grade (Python, the list cited, not compiled), the
    C2 price (THE GRADE of E0's reading equal to the foot's) and the entry as composed (the findings bank's text, or the composer before it
    is written): no sentence calling anything compiled but in negation; the entry's grade word E0's."""
    graded = []
    for n, words in N3_GRADED:
        t = rdn(n)
        last = [l for l in t.split(NL) if l.strip()][-1:] or ['']
        graded.append((n, last[0].startswith('### ### **') and all(w in last[0] for w in words)))
    wt = rdn('%s_walk.txt' % ACT)
    g_at = wt.rfind('### THE GRADE: ')
    walk_end = g_at > 0 and g_at > wt.rfind('\n## D = ') and g_at < wt.rfind('### ### **')
    f = _figs()
    py = 'in Python, not compiled' in f['walk_grade'] and 'cited and not compiled' in f['walk_grade'] and 'by exhaustion' in f['walk_grade']
    e0_ok = f['e0'] == f['c2_grade']
    fj = jl('%s_findings.json' % ACT)
    text = fj.get('text') or ''
    src = 'the landed entry`s text (relay data/b722_findings.json)'
    if not text:
        text, src = _finding_text()[1], 'the composer`s text (no entry landed yet)'
    sents = [s for s in re.split(r'(?<=[.;])\s+', text) if 'Nothing here is a statement' not in s]
    called = [s.strip()[:120] for s in sents if N3_COMPILED.search(N3_NEGATED.sub('', s))]
    graded_word = ('graded %s' % f['e0']) in text
    ok = all(o for _n, o in graded) and walk_end and py and e0_ok and not called and graded_word
    return ('HELD' if ok else 'REFUTED'), (
        'each bank`s foot its last line carrying its grade: %s; the walk`s grade after its last row and before its foot (relay data/b722_walk.txt): '
        '%s; the exhaustion graded in Python over the list cited, not compiled: %s; the C2 statement`s grade E0`s printed reading (THE GRADE: %s, '
        'the foot E0 %s; relay data/b722_c2_price.txt): %s; the sentences of %s calling anything compiled but in negation: %s; the entry`s grade '
        'word "graded %s": %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), walk_end, py, f['e0'], f['c2_grade'], e0_ok, src, called or 'NONE', f['e0'], graded_word))


def _n2_b721():
    """N2 (R332): data/b722_registrations.txt is committed ahead of every other bank of the act and nothing of -39 is computed beyond its count
    control. From the step bank's first row (its first commit, the act's first relay commit after b721's closing) and that commit's files read
    by git, and the act's banks by name (no list, pairs, zeros, onsets or coefficients bank of b722)."""
    rows = jl('%s_steps.json' % ACT).get('rows') or []
    first = (rows[0].get('commits') or [rows[0].get('commit')])[0] if rows else None
    after = g(ROOT, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_RELAY).split() if K.PRE_RELAY else []
    files = sorted(g(ROOT, 'show', '--name-only', '--format=', first).split()) if first else []
    first_ok = bool(first) and bool(after) and after[0] == first and files == sorted(REG_FILES_N2)
    forbidden = sorted(n for n in os.listdir(D) if N2_FORBIDDEN.match(n))
    f = _figs()
    ok = first_ok and not forbidden and f['g_miss'] == '0'
    return ('HELD' if ok else 'REFUTED'), (
        'the act`s first relay commit after b721`s closing %s (git rev-list %s..HEAD): %s, its files %s -- the registration and its count control '
        'alone: %s; the count control`s misses %s (relay data/b722_genus_control.txt); -39 banks beyond the control (a list, pairs, zeros, onsets, '
        'coefficients or predictions bank of b722): %s' % (
            K.PRE_RELAY[:8], K.PRE_RELAY[:8], (after[0][:8] if after else 'unread'), ', '.join(files) or 'unread', first_ok, f['g_miss'],
            ', '.join(forbidden) or 'NONE'))


def _n3_b721():
    """N3 (R332): every repair of (3) shows its two instances, and the replay over b721, b714 and b713 reads EQUAL or names each difference. From
    the class controls' per-repair line (each repair a record and a constructed instance) and the replay's foot (every DIFFERS object named by a
    finding, none unnamed)."""
    f = _figs()
    per = re.search(r'(?m)^### per repair: (.*)$', rdn('%s_standing_controls.txt' % ACT))
    each = dict((r, bool(per) and ('%s record True constructed True as wanted True' % r) in per.group(1)) for r in CLASS_REPAIRS)
    named_ok = f['rp_unnamed'] == '0' and f['rp_named'] == f['rp_diff'] and int(f['rp_eq']) + int(f['rp_diff']) == int(f['rp_obj'])
    acts = re.findall(r'(?m)^### (b\d{3}) -- the seal`s commit ', rdn('%s_replay.txt' % ACT))
    ok = all(each.values()) and f['cc_all'] == 'True' and f['cc_cases'] == f['cc_wanted'] and named_ok and acts == ['b721', 'b714', 'b713']
    return ('HELD' if ok else 'REFUTED'), (
        'the class repairs` instances (relay data/b722_standing_controls.txt, %s cases, as wanted %s): %s; the replay over %s (relay '
        'data/b722_replay.txt): %s objects, %s EQUAL, %s DIFFERS %s, named %s, unnamed %s, %s F-rows (the old tools`): %s' % (
            f['cc_cases'], f['cc_wanted'], ', '.join('%s %s' % (r, each[r]) for r in CLASS_REPAIRS), ', '.join(acts) or 'unread',
            f['rp_obj'], f['rp_eq'], f['rp_diff'], f['rp_diffs'], f['rp_named'], f['rp_unnamed'], f['rp_find'], named_ok))


# ### (R332)(1), N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build at [23] rewrites by the ferry's (W) list ((R332)(11))
N4_APPENDED = ('data/%s_steps.json' % ACT, 'data/%s_bank_hashes.json' % ACT, 'data/%s_hook_refusals.txt' % ACT, 'tools/mirror_prevbuild.json')


def _post_lock_edits():
    """the lock's time from the face (its `locked at (UTC)` line), the lock commit (the first relay commit at or after it, carrying the face),
    the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    face = rd(FACE) or ''
    m = re.search(r'locked at \(UTC\) : (\S+)', face)
    lock = _iso_epoch(m.group(1)) if m else None
    out = dict(lock=lock, lock_iso=m.group(1) if m else None, lock_commit=None, after=[], edited=[], dirty=[])
    if lock is None:
        return out
    rows = [l.split(' ', 1) for l in g(ROOT, 'log', '--reverse', '--format=%H %ct', '%s..HEAD' % K.PRE_RELAY).split(NL) if l.strip()]
    face_rel = os.path.relpath(FACE, ROOT).replace(os.sep, '/')
    lc = next((h for h, ct in rows if int(ct) >= lock and face_rel in g(ROOT, 'show', '--name-only', '--format=', h).split()), None)
    out['lock_commit'] = lc
    if lc is None:
        return out
    tracked = set(x for x in g(ROOT, 'ls-tree', '-r', '--name-only', lc).split(NL) if x.strip())
    guard = lambda p: p not in N4_APPENDED and (p == face_rel or p.startswith('tools/') or (p.startswith('data/%s_' % ACT) and p in tracked))
    hs = [h for h, _ct in rows]
    out['after'] = hs[hs.index(lc) + 1:]
    for h in out['after']:
        for p in g(ROOT, 'show', '--name-only', '--format=', h).split():
            if guard(p):
                out['edited'].append('%s %s' % (h[:8], p))
    out['dirty'] = [p for p in g(ROOT, 'diff', '--name-only', 'HEAD').split() if guard(p)]
    return out


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
    # ### (R332)(4)(v), N4: every push writes its capture -- each push_gated.sh call of the seat's capture names its repository and branch, and
    # ### the tool's capture for that pair stands (the relay's data/<act>_<repo>_<branch>_push_out.txt, or the per-command capture file named)
    pushes = []
    for r in capture():
        if r.get('tool') not in ('Bash', 'PowerShell'):
            continue
        # ### a push is the tool invoked, at the command's head or after && or ;, its environment prefixes allowed -- not a reader naming it
        # ### a mode flag before the ref (`--existing-tag v0.14.0`, the tag push of (R332)(3)(i)) is not the ref: the capture is named by the ref
        for m in re.finditer(r'(?:^|&&|;)\s*(?:[A-Z_]+=\S*\s+)*(?:bash\s+|sh\s+)?[^\s&;|]*push_gated\.sh\s+"?([^\s"]+)"?\s+(?:--[\w-]+\s+)*"?([^\s"]+)',
                             r.get('cmd') or ''):
            log = re.search(r'PUSH_GATED_LOG=(\S+)', r.get('cmd') or '')
            repo = os.path.basename(m.group(1).rstrip('/\\'))
            want = os.path.join(D, '%s_%s_%s_push_out.txt' % (ACT, repo, m.group(2)))
            cp = want if os.path.isfile(want) else (log.group(1).strip('"\'') if log else '')
            # ### (R332)(2), N4: the capture prints the repository's visibility (push_gated.sh's visibility line, repaired at b722)
            vis = bool(cp) and os.path.isfile(cp) and 'push_gated: visibility -> ' in (R.rd(cp) or '')
            pushes.append((r.get('n'), repo, m.group(2), bool(cp) and os.path.isfile(cp), vis))
    uncaptured = [p for p in pushes if not p[3]]
    unseen = [p[:3] for p in pushes if p[3] and not p[4]]
    # ### (R332)(6)(i), N4: the author's word after the seal printed from its bank, and no bank this tool wrote edited by hand since (its hashes bank)
    hb = jl(HASHES)
    hand = AC.hand_edits(dict((os.path.join(D, k), v) for k, v in (hb or {}).items()))
    aw = AC.author_words(ACT)
    head = rdn('%s_closing.txt' % ACT).split(NL)[0] if os.path.exists(os.path.join(D, '%s_closing.txt' % ACT)) else ''
    head_ok = bool(head) and 'none read' not in head and re.search(r'relay [0-9a-f]{8}', head) is not None
    # ### (R332)(1), N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (Component 8, the Edit tool; b721's
    # ### arm read the drafts and the rebuild branches) -- read from git, not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
    return ('HELD' if ok else ('PENDING' if seal is None else 'REFUTED')), (
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
        'the letters the seal records (relay data/b722_seal_hashes.json) %d, the defects bank`s letters now %d, letters after the seal %s; the step '
        'bank`s commits after the seal (relay data/b722_steps.json) %d, each with a post-seal phase: %s; the events bank for what is found after the seal %s; '
        'no bank after the root (relay data/b722_root_arm.json) %s; the pushes through push_gated.sh in the capture %d, each with its capture: %s, each '
        'capture printing its repository`s visibility: %s; the author`s word after the seal (relay data/b722_author_words.txt) %s, printed from its bank '
        'by the closing, record and trail tools; the banks this tool wrote, by its hashes bank (relay data/b722_bank_hashes.json, %d), edited by hand '
        'since: %s; the closing`s head line carrying commits read from the remotes: %s; the clauses that wait read again at `scores close`' % (
            len(seal or []), len(now), late or 'NONE', len(after), not wrong, 'present' if ev else 'not written (none found)',
            ('late %s' % ra.get('late')) if ra else 'waits on the root', len(pushes), uncaptured or 'every one', unseen or 'every one',
            ('%d lines' % len(aw.rstrip(NL).split(NL))) if aw is not None else 'none received', len(hb or {}),
            [os.path.basename(p) for p, _w, _n in hand] or 'NONE', head_ok if head else 'waits on the closing'))


def _n5():
    """N5 (R332): nothing deposits or publishes; no kernel main touched, no tag; no file beyond the (W) list. From the kernels as the face read
    them and as b721's face read them (each main and each tag set unmoved, b722's only new refs the challenge branch and the pin branches,
    neither on its main), SIDE-explicit-formula (main at badaccc, the challenge branch at its tip, no tag at it, its tip not an ancestor of
    main), and the act's writes read against the face's (W) table."""
    import b633_record as R3
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    prev = jl('b721_kernels_face.json').get('kernels') or {}
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1])]
    ef_main = g(K.EF_DIR, 'rev-parse', 'main').strip()
    ch_tip = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.CHALLENGE_BRANCH).strip()
    ch_ok = ch_tip == K.CHALLENGE_TIP and not g(K.EF_DIR, 'tag', '--points-at', ch_tip).strip() \
        and grc(K.EF_DIR, 'merge-base', '--is-ancestor', ch_tip, 'main') != 0
    # ### (R332)(7)(iii), N5: the rebuild's one kernel commit pair (SIDE-frobenius's copy and the author's two lines) off its main; the other
    # ### branches stand at their pins, commits already on main (Component 8; b721's arm read the pin branches)
    pins_on_main = [k for k, c in (('SIDE-frobenius', K.FROBENIUS_COPY), ('SIDE-frobenius', K.FROBENIUS_TWO_LINES))
                    if grc('D:/' + k, 'merge-base', '--is-ancestor', c, 'main') == 0]
    ef_ok = ef_main == K.EF_MAIN and not g(K.EF_DIR, 'tag', '--contains', K.EF_V037).replace('v0.37', '').strip() and ch_ok \
        and bool(prev) and not moved and not pins_on_main
    lv_main, lv_dep = g(LV, 'rev-parse', 'main').strip(), g(LV, 'rev-parse', 'v0.10.0^{commit}').strip()
    lv_port = g(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH).strip()
    # ### N5: lv-conservation's main and deposit untouched; port-b707 at b721's tip with b721's one tag v0.14.0 at it, no tag moved this act
    lv_ok = lv_main == K.LV_MAIN and lv_dep == K.LV_V0100 and lv_port == K.PORT_NEW_TIP \
        and [t for t in g(LV, 'tag', '--points-at', K.PORT_NEW_TIP).split(NL) if t.strip()] == [K.LV_TAG] \
        and g(LV, 'rev-parse', '--verify', '--quiet', 'refs/tags/' + K.LV_TAG).strip() == K.LV_TAG_OBJECT
    no_release = True   # ### no release route in this act's tools (G-PUBLISH-UNCALLED reads their code); none read here
    join_main, join_tags = g(K.JOIN_DIR, 'rev-parse', 'main').strip(), g(K.JOIN_DIR, 'tag', '--list').strip()
    join_ok = join_main == K.JOIN_NEW_TIP and join_tags == K.JOIN_TAG[0]
    # ### the re-cut merged at b721 (a86c9429) and its branch deleted at this act's step zero: main carries the merge
    recut_ok = grc(PP, 'merge-base', '--is-ancestor', K.RECUT_MERGE, 'HEAD') == 0
    # ### (R332)(4)(i), standing clauses v4 row (62), ONE LIST OF WRITES: every write read against the face's (W) table through
    # ### tools/act_close.py w_patterns, the scorer keeping no list of its own (b721's N5_RELAY_DATA omitted data/b711_steps.json, which its
    # ### (W) named, and refuted N5 on it; a repair at b722, banked by diff)
    W = AC.w_patterns(rd(FACE) or '')
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if not AC.w_allows(x, W, 'PLACE-papers')]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    ruled = sorted(x for x in relay_ch if x.startswith('tools/') and AC.w_allows(x, W, 'relay'))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not AC.w_allows(x, W, 'relay')]
    kinds_beyond = [x for x in relay_ch if not AC.w_allows(x, W, 'relay')]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B711_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE) or '') or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(LV, lock) + _amended_after(K.EF_DIR, lock)) if lock else []
    cj = jl('%s_commands.json' % ACT)
    ob = cj.get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    chained = [d['n'] for d in (cj.get('delete_shapes') or []) if d.get('chained')]
    deleted = sorted(x for d in (cj.get('delete_shapes') or []) for x in (d.get('deletes') or []))
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl == pre_gl
    kept = [b for _r, b in K.KEPT_BRANCHES if b in deleted]
    # ### (R332)(9), (11), N5 (Component 8, the Edit tool): no Lean file written into any kernel -- no ref of any kernel carrying a commit made
    # ### after the act's opening commit, no .lean file changed or untracked in its tree; the rebuild-b721 branches kept, each at its tip; the
    # ### address scan's count from its bank (relay data/b722_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        newest = max([int(x) for x in g(kp, 'for-each-ref', '--format=%(committerdate:unix)', 'refs/heads', 'refs/tags').split() if x.isdigit()] or [0])
        loose = [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]
        if newest > start or loose:
            lean_w.append('%s%s' % (os.path.basename(kp), ' (a commit after the act`s start)' if newest > start else ' (a .lean file in the tree)'))
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
    ok = k_ok and ef_ok and lv_ok and no_release and join_ok and recut_ok and not pp_beyond and not renames and not kinds_beyond and not shared_tools \
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
    return (('HELD' if ok else 'REFUTED'),
            'the address scan (relay data/b722_address_scan.txt): PREVIOUS ADDRESS: %s; a Lean file or commit written into a kernel since the act`s '
            'opening commit (%d kernels read): %s; the branch %s kept on the six wave 1 kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
            'nothing deposits or publishes: the deposit route untouched (draft %s, v5, unpublished); no release route in the act`s tools: %s; every kernel '
            'as the face read it: %s; every kernel`s main and tags as b721`s face read them (relay data/b721_kernels_face.json), moved: %s; the '
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at badaccc, no tag past v0.37, the challenge branch %s at %s with no tag and '
            'off main (%s): %s; SIDE-lv-conservation`s main and deposit '
            'untouched, port-b707 at %s, the one tag %s at it, unmoved: %s; the join kernel`s main at %s with the one tag %s: %s; the re-cut`s merge %s on '
            'PLACE-papers main: %s; the standing '
            'arms added beyond b721`s face, the act arms apart: %s (%s); shared tools edited beyond the membrane %s: %s; sealed tools not agreeing: %s; '
            'commits amended after the seal (relay, PLACE-papers, SIDE-lv-conservation, SIDE-explicit-formula): %s; deletes with anything chained after: %s; a kept branch deleted '
            '(port-b707): %s; one git write per message (%s): %s; PLACE-papers beyond the face`s (W) list: %s; papers moved or renamed: '
            '%s; relay files beyond the face`s (W) list: %s; the glossary unchanged: %s; outbound requests other than git and gh %d, an identifier of the '
            'author in %s; the clauses that wait (the hashes at the close, no bank after the root) read again at `scores close`' % (
                K.DRAFT, no_release, k_ok, moved or 'NONE', pins_on_main or 'NONE', K.CHALLENGE_BRANCH, K.CHALLENGE_TIP[:8], ch_ok, ef_ok,
                K.PORT_NEW_TIP[:8], K.LV_TAG, lv_ok, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0], join_ok,
                K.RECUT_MERGE[:8], recut_ok, added or 'NONE', arms_ok, sorted(ruled), shared_tools or 'NONE', differ or 'NONE',
                amended or 'NONE', chained or 'NONE', kept or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', renames or 'NONE', kinds_beyond or 'NONE', gl,
                len(ob), [r['line'] for r in ident] or 'NONE'))


def TRAIL_HEAD():
    return ('### b722 — lane two, act one hundred and forty-nine, the instruments act under (R332): b721 at its weight, its corrigendum and three '
            'repairs; -31 and -55; the fourteen class-number-2 fields; the C2 statement for Lean graded and priced; the research instruments '
            'entered and their reproduction runner; the propagation read; the author’s name and address; the axiom step diagnosed')


R.TRAIL_HEAD = TRAIL_HEAD


def _h(x):
    """a height as the list prints it (200.0) read as the title writes it (200)."""
    return x[:-2] if x.endswith('.0') else x


def _registry_unread():
    """the REGISTRY rows that read `not yet read` with b722 named (b721's attribute block), counted at PLACE-papers HEAD; none read this act,
    (R332) ordering no read of them."""
    return len(re.findall(r'(?m)^\| `[^`]+` \| not yet read \| not yet read — `%s` \|' % ACT, _show(PP, 'HEAD', 'REGISTRY.md') or ''))


def _held_word(a, b):
    """-31's and -55's readings as the title writes them: one word where they agree, both in order where they do not."""
    return a if a == b else '%s and %s' % (a, b)


def _title():
    """the entry's title by its objects, the ferry's Component 8 form ("the class-number-2 table at its fourteen remaining fields: <k> of 14
    HELD<, the value law at all eighteen by exhaustion over Baker's and Stark's list>; -31 and -55: n0 <n1> and <n2>, <HELD | REFUTED>; the C2
    statement for Lean graded <grade> and priced; <m> research instruments entered as I-41 to I-<40+m>, <j> reproducing; the propagation read
    v8 and its <h> notes; the axiom step diagnosed at five wave 1 pins"), the bracketed clause where the walk's grade states it; every figure
    from the banks (Component 8, the Edit tool; b721's title over b721's objects in git at b721's record tool)."""
    f = _figs()
    law = (', the value law at all eighteen by exhaustion over Baker’s and Stark’s list'
           if 'holds at all eighteen' in f['walk_grade'] and 'by exhaustion' in f['walk_grade'] else '')
    return ('## The class-number-2 table at its fourteen remaining fields: %s of 14 HELD%s; -31 and -55: n0 %s and %s, %s; the C2 statement for '
            'Lean graded %s and priced; %d research instruments entered as I-%s to I-%d, %d reproducing; the propagation read v8 and its %d notes; '
            'the axiom step diagnosed at five wave 1 pins' % (
                f['walk_held'], law, f['n31'], f['n55'], _held_word(f['h31'], f['h55']), f['e0'], f['ins_n'], f['ins_first'],
                40 + f['ins_n'], f['rp_rep'], f['pg_notes']))


def _for_author():
    rows, nav = _owners_now()
    f = _figs()
    seat = AC.defect_owners(rows)['SEAT']   # ### (R332)(4)(iii), v4 row (64): the one counter
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    why = (': the probe enumerates every repository without a cited pin at its HEAD, so its count moves with the kernels -- its entry’s range '
           'limits say so' if f['rp_differs'] == ['I-76'] else ', each read in its entry')
    return ('(1) the instruments by the rule, not by the navigator’s list: %d entered, the navigator’s %s beside the output, %s of them in it, '
            'choosing nothing (relay data/b722_instruments.txt); (2) the reproduction run %s of %s REPRODUCES, DIFFERS %s (%s%s), NOT RUN %s '
            '(%s, each with its reason and price) (relay data/b722_reproduce.txt); (3) the C2 statement graded %s with its scope -- that the list is '
            'complete is Baker (1971) and Stark (1975), cited and not compiled -- and priced by two routes, where the compile lives the author’s '
            'word (relay data/b722_c2_price.txt); (4) the axiom step at five pins: targets absent at the pin %s, the step not the pin’s own %s, each '
            'route priced on its rebuild-b721 branch for %s, nothing dispatched (relay data/b722_axiom_diag.txt); (5) the LLM-contribution line: '
            'SAME %s, DIFFERS %s, ABSENT %s, %s drafts for the release sitting, nothing in a paper or README edited (relay '
            'data/b722_llm_line_drafts.txt); (6) the propagation read’s %s READS WRONG and %s DATED hits noted at FINDINGS :%s, no line rewritten; '
            '(7) the report tool outside the sealed list until the root (relay data/b708_rules.txt row (1)); (8) %s and the seat’s %s defect%s as '
            'lettered' % (
                f['ins_n'], f['ins_nav'], f['ins_nav_in'], f['rp_rep'], f['rp_rows'], f['rp_diff'], ', '.join(f['rp_differs']) or 'none', why,
                f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['e0'], f['ax_absent'], f['ax_notown'], K.NEXT_ACT, f['ll_same'],
                f['ll_differs'], f['ll_absent'], f['ll_drafts'], f['pg_wrong'], f['pg_dated'], f['pg_line'],
                'the %s navigator %s%s' % (num_word(len(nav)), 'miss' if len(nav) == 1 else 'misses', (' (%s)' % letters) if nav else ''),
                num_word(seat), '' if seat == 1 else 's'))


def _diag_line():
    """the axiom diagnosis by kernel, as its json banks it: `<kernel> <class>` for each of the five runs."""
    return '; '.join('%s %s' % (r.get('kernel'), r.get('class')) for r in _diag_rows()) or 'unread'


def _finding_text():
    """the FINDINGS entry, composed before the root: its head line the result sentence, the result before its conditions; its scores line from
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (Component 8, the Edit tool, over b722's objects;
    b721's composer over b721's objects kept below as _finding_text_b721, not called, and in git at b721's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    cut = jl('%s_coeffs_controls.json' % ACT).get('cut')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The fourteen class-number-2 fields left after b721 hold H-C2-WALK through %s by b711’s route -- %s of 14 HELD, the control row -15 %s -- '
         'so the value law at the least negative index stands at all eighteen by exhaustion over the list Baker and Stark proved complete, '
         'checked in Python over that list as cited and not compiled; -31 and -55, under e8c3dff4, read n0 %s and %s with b = %s and %s, '
         'H-C3-31 %s and H-C4-55 %s; the C2 statement for Lean is graded %s by E0 with its scope beside it, true as written in Python at %s of %s '
         'fields, and priced by two routes; %d research instruments are entered as I-%s to I-%d in b618’s form, %d of them reproducing their '
         'banked figure; the propagation read under standing clauses v8 writes %d dated notes; and the axiom step at five wave 1 pins is '
         'diagnosed from b721’s runs by their ids, nothing dispatched.' % (
             cut, f['walk_held'], f['walk_ctl'], f['n31'], f['n55'], f['b31'], f['b55'], f['h31'], f['h55'], f['e0'], f['c2_true'], f['c2_of'],
             f['ins_n'], f['ins_first'], 40 + f['ins_n'], f['rp_rep'], f['pg_notes']), '',
         '*Filed at b722 on the author’s ruling `(R332)`; %d question%s put before the root. Banks: relay `data/b722_corrigendum.txt`, '
         '`data/b722_standing_v122.txt`, `data/b722_coeffs.txt`, `data/b722_walk.txt`, `data/b722_c2_statement.txt`, `data/b722_c2_price.txt`, '
         '`data/b722_instruments.txt`, `data/b722_reproduce.txt`, `data/b722_propagation.txt`, `data/b722_address_scan.txt`, '
         '`data/b722_axiom_diag.txt`, `data/b722_llm_line_drafts.txt`, `data/b722_touch.txt`, `data/b722_standing_figures.txt`, '
         '`data/b722_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the repairs** ((R332)(1)-(2), `%s`, `%s`): b721 entered at its weight (FINDINGS :%s); the corrigendum of '
         'b721’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- at FINDINGS '
         ':%s, the corrigenda bank appended at row (%s); tools/standing/ at %s with the three repairs (the seal’s list from the seal bank; USED '
         'by discriminant and principal form; the closure reader retired, the hand list of record), %s cases, %s as wanted (relay '
         'data/b722_standing_v122.txt).' % (
             K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'],
             f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v122_cases'], f['v122_wanted']), '',
         '**-31 and -55** ((R332)(3), N2, `%s`, `%s`): under their registration at `%s` (H-C3-31 and H-C4-55, relay data/b721_registrations.txt '
         'section (5), read unchanged); the controls first, committed before any figure -- the recursion at zeta’s series returning von Mangoldt, '
         '-23 reproducing b711’s bank, a planted coefficient failing to reproduce, each as wanted: %s; then through %s by b711’s route: '
         'n0(-31) = %s, b = %s and n0(-55) = %s, b = %s, each row on its own clauses with the prime clause -- H-C3-31 %s, H-C4-55 %s (relay '
         'data/b722_coeffs.txt).' % (
             K.C2_CTL[:8], K.C3_RELAY[:8], K.REG_C3[:8], f['ctl_ok'], cut, f['n31'], f['b31'], f['n55'], f['b55'], f['h31'], f['h55']), '',
         '**The fourteen** ((R332)(4), N2, N3, `%s`): under H-C2-WALK at `%s`, the fourteen fields through %s by the same route and controls: '
         '%s of 14 HELD, REFUTED %s, NOT SCORABLE %s, the control row -15 %s; the grade at its end, as banked: “%s” (relay data/b722_walk.txt).' % (
             K.C3_RELAY[:8], K.REG_WALK[:8], cut, f['walk_held'], f['walk_refuted'], f['walk_unscor'], f['walk_ctl'], f['walk_grade']), '',
         '**The C2 statement for Lean** ((R332)(5), N3, `%s`, `%s`): the text committed alone before its grade (relay data/b722_c2_statement.txt); '
         'graded by E0 (relay tools/e0_rule.py, unedited) %s, its one hypothesis a domain condition, the scope beside it (%s); as written, true '
         'in Python at %s of %s; priced per field -- (A) decide as written, %s to %s lattice points, unmeasured in Lean; (B) the certificate '
         'route under %s operations at %s of %s, two general lemmas named and not proved; where the compile lives the author’s word (relay '
         'data/b722_c2_price.txt).' % (
             K.C4_STMT[:8], K.C4_RELAY[:8], f['e0'], f['c2_scope'], f['c2_true'], f['c2_of'], f['c2_lo'], f['c2_hi'], f['c2_bound'], f['c2_under'],
             f['c2_under_of']), '',
         '**The research instruments** ((R332)(6)-(7), N2, `%s`, `%s`, `%s`): the rule printed before any tool was named; its output %d of a '
         'population of %s act-numbered tools (%s reused, (S1) %s, (S2) %s), every one read by hand; the navigator’s %s printed beside it, %s in '
         'the output, choosing nothing (relay data/b722_instruments.txt). Entered at INSTRUMENTS.md :%d onward as I-%s to I-%d in b618’s form -- '
         'reads, decides, controls, the validated case with its bank and line, range limits, entered with its act and its OPEN_TRAILS or bank '
         'line -- nothing above I-41 edited. The runner tools/research/reproduce.py, sealed with the act’s tools, each instrument imported '
         'unedited: %s rows, %d REPRODUCES, %s DIFFERS (%s), %s NOT RUN (%s, each with its reason and price), the planted wrong figure '
         'differing as wanted at %s of %s (relay data/b722_reproduce.txt); the standing arm G-RESEARCH-REPRODUCES joins, the run list 117.' % (
             K.C5_RULE[:8], K.C5_RELAY[:8], K.C5_PP[:8], f['ins_n'], f['ins_pop'], f['ins_reused'], f['ins_s1'], f['ins_s2'], f['ins_nav'],
             f['ins_nav_in'], K.INSTRUMENTS_FIRST, f['ins_first'], 40 + f['ins_n'], f['rp_rows'], f['rp_rep'], f['rp_diff'],
             ', '.join(f['rp_differs']) or 'none', f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The propagation read** ((R332)(8), N2, `%s`, `%s`, `%s`): standing clauses v8, v7 with row (82), landed by a commit of its own; its '
         'opening run on %s objects, each object’s names printed before its search: %s hits -- COPY %s, DATED %s, NOT THIS OBJECT %s, READS RIGHT '
         '%s, READS WRONG %s, unread %s -- and %d dated notes at FINDINGS :%s, each pointing to the line it corrects, no line rewritten (relay '
         'data/b722_propagation.txt).' % (
             K.STANDING_COMMIT[:8], K.C6_RELAY[:8], K.C6_PP[:8], f['pg_obj'], f['pg_hits'], f['pg_copy'], f['pg_dated'], f['pg_other'],
             f['pg_right'], f['pg_wrong'], f['pg_unread'], f['pg_notes'], f['pg_line']), '',
         '**The author’s name and address** ((R332)(9), N5): git’s global user.email the GitHub noreply form; user.name set to the account '
         'login on the author’s answer and printed by its kind alone; the scan over every commit and bank of the act, the previous address read '
         'from history and held in memory: PREVIOUS ADDRESS: %s, the author’s name %s, over %s places, its controls as wanted (relay '
         'data/b722_address_scan.txt).' % (f['addr'], f['name'], f['addr_places']), '',
         '**The axiom step at five wave 1 pins** ((R332)(10), N1, `%s`): b721’s runs read by their ids, GETs alone, each step log and artifact '
         'read and its cause classed -- %s: targets absent at the pin %s, the build target not covering the axiom file’s imports %s, the step '
         'not the pin’s own %s, other %s; a repair route priced per kernel on its rebuild-b721 branch, the dispatches %s’s; nothing committed, '
         'pushed or dispatched (relay data/b722_axiom_diag.txt).' % (
             K.C7_RELAY[:8], _diag_line(), f['ax_absent'], f['ax_cover'], f['ax_notown'], f['ax_other'], K.NEXT_ACT), '',
         '**The release sitting’s list** ((R332)(12), `%s`): the LLM-contribution line quoted from the monograph’s end matter (:%s), and %s wave 1 '
         'papers and %s kernel READMEs read against it -- SAME %s, DIFFERS %s, ABSENT %s; %s drafts in the monograph’s words and position, nothing '
         'in a paper or README edited (relay data/b722_llm_line_drafts.txt).' % (
             K.C7_RELAY[:8], f['ll_line'], f['ll_papers'], f['ll_readmes'], f['ll_same'], f['ll_differs'], f['ll_absent'], f['ll_drafts']), '',
         '**The touch read** (standing clauses v8): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b722_touch.txt). The act’s counter CLAIM %d, CLOSE %d.' % (f['claim'], f['close']), '',
         '**The standing arms**: the four figures at b722 -- %s, %s, %s, %s -- against b721’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b722_standing_figures.txt); one standing arm added by the ruling, G-RESEARCH-REPRODUCES.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each miss raised before the component '
         'citing it; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the computation and its price meet at the C2 statement -- the fourteen read here and '
         'the four read before make the eighteen its list names, and its price is counted on those same n0; the instruments and the propagation '
         'read meet at the record -- each instrument found by its entry and run again against its bank, each corrected statement read again '
         'where it stands and noted beside it.', '',
         '**Carried to:** %s, each from its bank: the axiom step repaired on the rebuild-b721 branches and dispatched at the pins (relay '
         'data/b722_axiom_diag.txt); the C2 compile at the route the author names (relay data/b722_c2_price.txt); the drafts for the release '
         'sitting (relay data/b722_llm_line_drafts.txt); the instruments not reproducing here, each with its entry; the draft held at v5.' % (
             K.NEXT_ACT), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b721():
    """b721's form over b721's objects, kept for the record and not called (Component 8)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    per = '; '.join('%s EXCEEDS %s, STATED %s' % p for p in f['fz_per'])
    e = ['', _title(), '',
         'The C2 table predicts no value not yet seen at any field of class number 2: walked over all %s such fields from decomposition types '
         'alone, every least negative index falls on a shape of value -2 or -1/2, so the rule chose no discriminant and nothing was computed, '
         'the empty output proved by the walk’s reach and a positive control that fires; the table over cyclic h = 3, 4, 5 is written in closed '
         'form and reads -23, -39 and -47 as banked, and from it two predictions stand committed before any figure at their discriminants -- '
         'n0 = %s, b = %s at %s and n0 = %s, b = %s at %s; the offset law is refuted post hoc on its own seventeen first rows (%s held, %s '
         'refuted), its next tier carried with no pair in reach; and %s of %s wave 1 kernels build at their own pins on the runner, '
         'SIDE-lv-conservation with one sorry, SIDE-frobenius by the author’s two workflow lines.' % (
             f['walk_n'], f['c3'][1], f['c3'][5], f['c3'][0], f['c4'][1], f['c4'][5], f['c4'][0], f['or_held'], f['or_refuted'], f['rb_j'],
             f['rb_m']), '',
         '*Filed at b722 on the author’s ruling `(R332)`; %d question%s put before the root. Banks: relay `data/b722_corrigendum.txt`, '
         '`data/b722_standing_v121.txt`, `data/b722_registrations.txt`, `data/b722_derivation.txt`, `data/b722_offset_pred.txt`, '
         '`data/b722_offset_read.txt`, `data/b722_offset_tier.txt`, `data/b722_surgery_carry.txt`, `data/b722_frozen_line.txt`, '
         '`data/b722_frozen_line_drafts.txt`, `data/b722_rebuild.txt`, `data/b722_touch.txt`, `data/b722_standing_figures.txt`, '
         '`data/b722_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the repairs** ((R332)(1)-(2), `%s`, `%s`): b721 entered at its weight (FINDINGS :%s); the corrigendum of '
         'b721’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- at FINDINGS '
         ':%s, the corrigenda bank appended at row (%s); event (12)’s cause re-read from the transcript, the branch and the push in one message '
         'and not the listing; tools/standing/ at %s with the three repairs, %s cases, %s as wanted (relay data/b722_standing_v121.txt).' % (
             K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'],
             f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v121_cases'], f['v121_wanted']), '',
         '**The C2 table’s test** ((R332)(3), N2): the rule committed alone at `%s` before any discriminant was named, its tool alone at `%s` '
         'before it ran; its output NONE at `%s`: of the %s class-number-2 fields (the largest |D| %s; the walk carried to |D| < %s finds no '
         'other), %s already used and %s passed over on a value of -2 or -1/2; the positive control, -2 alone excluded, takes %s (n0 %s) and %s '
         '(n0 %s); the table’s predictions at the fourteen unused fields registered before any figure at them and carried; (3)(ii)’s rows and the coefficients carried to %s on '
         'the author’s word, nothing substituted.' % (
             K.C2_REG[:8], K.C2_SELECT[:8], K.C2_HALT[:8], f['walk_n'], f['walk_largest'], f['walk_reach'], f['walk_used'], f['walk_passed'],
             f['pc'][0], f['pc'][1], f['pc'][2], f['pc'][3], K.NEXT_ACT), '',
         '**The table over h = 3, 4, 5 and two predictions** ((R332)(4), N2, N3): rule (4) printed at `%s` before either discriminant was named; '
         'the table at Omega 1-6 for C3, C4 and C5 (`%s`), its checks before each step and its plants failing as wanted; the grade, at its end, '
         'as banked: “%s ; %s ; %s” (relay data/b722_derivation.txt). By rule (4), committed at `%s` before anything at them: H-C3-31, n0 = %s = %s, a = %s, the '
         'pair sum %s, b = %s; H-C4-55, n0 = %s = %s, a = %s, the pair sum %s, b = %s; the group-ring model naming the same n0 at both; each '
         'with its falsifier; nothing at -31 or -55 computed this act, the computation %s’s. A written table checked against the model, not a '
         'kernel statement.' % (
             K.C3_RULE[:8], K.C3_RELAY[:8], f['dv_grade'], f['dv_table'], f['dv_read'], K.C2_PRED[:8],
             f['c3'][1], f['c3'][2], f['c3'][3], f['c3'][4], f['c3'][5], f['c4'][1], f['c4'][2], f['c4'][3], f['c4'][4], f['c4'][5],
             K.NEXT_ACT), '',
         '**The offset, post hoc** ((R332)(5), N3): every row computed and its onset banked before H-OFFSET was written, so none tests it; the '
         'seventeen, post hoc, scorable %s of %s, delta_pred committed at `%s` from r and n*_pred alone (%s to %s), then the observed n* beside '
         'it: HELD %s, REFUTED %s, NOT SCORABLE %s -- H-OFFSET %s post hoc on its own first rows (relay data/b722_offset_read.txt). The next '
         'tier by r(rho) <= 0.05 alone: %s pairs chosen, delta_pred formed at %s, no n*_pred within reach of its list; no list extended, no '
         'onset run; carried (`%s`).' % (
             f['op_scor'], f['op_of'], K.C4_PRED[:8], f['op_lo'], f['op_hi'], f['or_held'], f['or_refuted'], f['or_unscor'], f['or_word'],
             f['ot_chosen'], f['ot_formed'], K.C4_RELAY[:8]), '',
         '**The surgery** ((R332)(6), `%s`): carried, not started -- b718’s price %s h in %s calls against what remained; H-SHAPE unread, '
         'nothing computed (relay data/b722_surgery_carry.txt).' % (K.C5_RELAY[:8], f['sg_hours'], f['sg_calls']), '',
         '**The frozen line** ((R332)(7)(i)-(ii), N4, `%s`, `%s`): %s statements quoted at their pins and graded by E0 -- %d DERIVES, %d '
         'INTERFACES (monotone_unique_zero, its hypothesis StrictMono; the keystone census lists StrictMono as DOMAIN, the two lists’ '
         'disagreement carried for the author, `%s`); every README sentence and description graded against them by the seat’s hand: %s. '
         'Drafts for the release sitting, %s README paragraphs and %s one-line descriptions with SPIRAL_MAP :104’s sentence, committed to the '
         'relay and to no kernel (relay data/b722_frozen_line.txt, data/b722_frozen_line_drafts.txt).' % (
             K.C6_FROZEN[:8], K.C6_DRAFTS[:8], f['fz_n'].lower(), f['fz_derives'], f['fz_interfaces'], K.C6_CENSUS[:8], per, f['dr_paras'],
             f['dr_descs']), '',
         '**The rebuild** ((R332)(7)(iii), N1, N5, `%s`): one branch `%s` per wave 1 kernel at its own pin, each at the Mathlib its manifest '
         'carries; %s pushed, %s runs, the free memory read before each push, dispatch and read against the hold; SIDE-frobenius, with no '
         'workflow on main, its dispatch refused, then run on push at `%s` by the author’s two lines on its branch alone; each run read by its '
         'id: %s of %s build, %s with a sorry, held %s, nothing repaired; no main or tag touched (relay data/b722_rebuild.txt).' % (
             K.C6_RELAY[:8], K.REBUILD_BRANCH, f['rb_pushed'], f['rb_runs'], K.FROBENIUS_TWO_LINES[:8], f['rb_j'], f['rb_m'], f['rb_sorry'],
             f['rb_held']), '',
         '**The federation pin, closed** ((R332)(8)): at its banked state (relay data/b721_pin.txt), nothing repaired; each kernel cited at the '
         'Mathlib its own manifest carries; the readiness test for a wave the rebuild at each kernel’s own pin, as above.', '',
         '**The touch read** (standing clauses v7): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b722_touch.txt). The act’s counter CLAIM %d, CLOSE %d.' % (f['claim'], f['close']), '',
         '**The standing arms**: the four figures at b722 -- %s, %s, %s, %s -- against b721’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b722_standing_figures.txt); no standing arm added.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each miss raised before the component '
         'citing it; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the halt and the predictions meet at the table -- at class number 2 the least negative '
         'index never lands on a new value, so the table’s first fresh tests stand at h = 3 and 4, where it and the group-ring model name the '
         'same n0; and the rebuild and the frozen line meet at the pins -- the statements the drafts quote are the ones the runner built, each '
         'Python-checked or read from source, none of the act’s figures a kernel statement.', '',
         '**Carried to:** %s, each from its bank: the computation at -31 and -55 under `%s`; the C2 rows of (3)(ii) where the author rules them; '
         'the offset’s new pairs and the surgery where (5)-(6) carried them; the census’s StrictMono row beside the rule; the draft held at v5.' % (
             K.NEXT_ACT, K.C2_PRED[:8]), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


# ### (R332)(8): the federation pin closed, a line of this act's trail naming the trail lines that carried it (OPEN_TRAILS, each read at
# ### PLACE-papers HEAD by the `trail` route's needle before the trail is written)
PIN_TRAIL_LINES = ((16056, '**The prices:** the federation pin at de5ce8a9a66a'), (16124, '**Next:** b718 ((R327)(11)): the federation pin under (7)(i)'),
                   (16142, '**The federation pin:** 1 of 12 dispatched and read'), (16232, '**The pin:** 1 of 6 eligible'))


def _pin_lines_ok():
    """each line of PIN_TRAIL_LINES at PLACE-papers HEAD opening with its needle: (line, True|False)."""
    ot = (_show(PP, 'HEAD', 'OPEN_TRAILS.md') or '').split(NL)
    return [(n, len(ot) >= n and ot[n - 1].startswith(w)) for n, w in PIN_TRAIL_LINES]


def _trail_text():
    """the trail record (Component 8, the Edit tool, over b722's objects; b721's composer over b721's objects kept below as _trail_text_b721,
    not called, and in git at b721's record tool)."""
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R332) ratified.** (1) b721 at its weight. (2) The corrigendum and three repairs, v1.2.2. (3) -31 and -55. (4) The fourteen '
             'class-number-2 fields. (5) The C2 statement for Lean, graded and priced. (6) The research instruments entered. (7) Their '
             'reproduction runner. (8) Standing clauses v8 and the propagation read. (9) The author’s name and address. (10) The axiom step '
             'diagnosed. (11) Step zero. (12) The release sitting’s list, drafts alone. (13) The next act.', '',
             '**Entered:** FINDINGS.md:%s (b721’s weight), :%s (the corrigendum), :%s (the propagation notes), :%s (the entry); INSTRUMENTS.md '
             ':%d (I-41 to I-%d); this record.' % (
                 f['weight'], f['corr_line'], f['pg_line'], fj.get('entry_line'), K.INSTRUMENTS_FIRST, 40 + f['ins_n']), '',
             '**-31 and -55:** under `%s`, n0 %s and %s, b %s and %s, H-C3-31 %s, H-C4-55 %s (relay data/b722_coeffs.txt).' % (
                 K.REG_C3[:8], f['n31'], f['n55'], f['b31'], f['b55'], f['h31'], f['h55']), '',
             '**The fourteen:** under H-C2-WALK at `%s`, %s of 14 HELD, the control row -15 %s; the value law at all eighteen by exhaustion over '
             'the list cited, in Python, not compiled (relay data/b722_walk.txt).' % (K.REG_WALK[:8], f['walk_held'], f['walk_ctl']), '',
             '**The C2 statement:** graded %s by E0, true as written in Python at %s of %s, priced by two routes, the compile’s route the author’s '
             'word (relay data/b722_c2_statement.txt, data/b722_c2_price.txt).' % (f['e0'], f['c2_true'], f['c2_of']), '',
             '**The instruments:** I-%s to I-%d entered (INSTRUMENTS.md :%d); reproduced %d of %s, DIFFERS %s (%s), NOT RUN %s (%s) (relay '
             'data/b722_reproduce.txt); G-RESEARCH-REPRODUCES in the run list, 117.' % (
                 f['ins_first'], 40 + f['ins_n'], K.INSTRUMENTS_FIRST, f['rp_rep'], f['rp_rows'], f['rp_diff'], ', '.join(f['rp_differs']) or 'none',
                 f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The propagation read:** v8 at `%s`; %s hits, %d notes at FINDINGS :%s (relay data/b722_propagation.txt).' % (
                 K.STANDING_COMMIT[:8], f['pg_hits'], f['pg_notes'], f['pg_line']), '',
             '**The axiom step:** %s; routes priced for %s (relay data/b722_axiom_diag.txt).' % (_diag_line(), K.NEXT_ACT), '',
             '**The release sitting’s list:** SAME %s, DIFFERS %s, ABSENT %s, %s drafts (relay data/b722_llm_line_drafts.txt).' % (
                 f['ll_same'], f['ll_differs'], f['ll_absent'], f['ll_drafts']), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b722_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v8.txt from `%s`; the touch read relay data/b722_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d.' % (K.STANDING_COMMIT[:8], f['claim'], f['close']), '',
             '**Act root:** b722 `%s` (previous `%s`, b721’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b722_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v8.txt; tools/standing/ at %s (relay data/b722_standing_v122.txt); the standing '
             'report tool (relay data/b722_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written, no tag cut, no Lean file written into any kernel; the rebuild-b721 branches of the '
              'six wave 1 kernels kept for %s; port-b707 at %s, kept, its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process '
              'on this host, nothing dispatched, b721’s runs read by their ids.' % (
                  K.NEXT_ACT, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b722_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b721’s %s, %s, %s, %s (relay data/b722_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b722_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b721():
    """b721's trail record over b721's objects, kept for the record and not called (Component 8)."""
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    pl = _pin_lines_ok()
    if not all(o for _n, o in pl):
        sys.exit('### OPEN_TRAILS AT HEAD DOES NOT CARRY THE PIN`S LINES AS NAMED (%s) -- NOTHING COMPOSED' % pl)
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R332) ratified.** (1) b721 at its weight. (2) The corrigendum and the v1.2.1 repairs. (3) The C2 table where it predicts a value '
             'not yet seen. (4) The table over h = 3, 4, 5 and the h = 3, 4 predictions. (5) The offset, post hoc, and its next tier. (6) The '
             'surgery. (7) The frozen line: its statements, its drafts, the rebuild at its own pins. (8) The federation pin closed. (9) Step zero. '
             '(10) The draft held at v5. (11) The next act.', '',
             '**Entered:** FINDINGS.md:%s (b721’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The C2 table’s test:** the rule alone at `%s`, its output NONE at `%s` over the %s class-number-2 fields, the positive control '
             'taking %s and %s; halted at (3)(i), proved; (3)(ii) carried to %s (relay data/b722_registrations.txt (2)).' % (
                 K.C2_REG[:8], K.C2_HALT[:8], f['walk_n'], f['pc'][0], f['pc'][2], K.NEXT_ACT), '',
             '**The table and the predictions:** the table over h = 3, 4, 5 at `%s`, its checks as wanted; H-C3-31 n0 = %s, b = %s and H-C4-55 '
             'n0 = %s, b = %s at `%s`, nothing at either computed (relay data/b722_derivation.txt, data/b722_registrations.txt (5)).' % (
                 K.C3_RELAY[:8], f['c3'][1], f['c3'][5], f['c4'][1], f['c4'][5], K.C2_PRED[:8]), '',
             '**The offset, post hoc:** the seventeen HELD %s, REFUTED %s, H-OFFSET %s post hoc on its own first rows; the tier %s chosen, %s '
             'formed, carried (relay data/b722_offset_read.txt, data/b722_offset_tier.txt).' % (
                 f['or_held'], f['or_refuted'], f['or_word'], f['ot_chosen'], f['ot_formed']), '',
             '**The surgery:** carried, not started, under H-SHAPE (relay data/b722_surgery_carry.txt).', '',
             '**The frozen line:** %s statements at their pins, %d DERIVES and %d INTERFACES; the drafts for the release sitting in the relay alone '
             '(relay data/b722_frozen_line.txt, data/b722_frozen_line_drafts.txt).' % (f['fz_n'].lower(), f['fz_derives'], f['fz_interfaces']), '',
             '**The rebuild:** %s of %s wave 1 kernels build at their own pins, %s with a sorry; runs %s (relay data/b722_rebuild.txt).' % (
                 f['rb_j'], f['rb_m'], f['rb_sorry'], ', '.join('%s %s' % (k, r) for k, r in K.REBUILD_RUNS)), '',
             '**The federation pin, closed ((R332)(8)):** at its banked state (relay data/b721_pin.txt), nothing repaired, each kernel cited at '
             'the Mathlib its own manifest carries, the readiness test for a wave the rebuild at its own pins; the lines that carried it, '
             'OPEN_TRAILS %s.' % ', '.join(':%d' % n for n, _o in pl), '',
             '**The standing line:** relay data/standing_clauses_v7.txt; the touch read relay data/b722_touch.txt; the act’s counter CLAIM %d, '
             'CLOSE %d.' % (f['claim'], f['close']), '',
             '**Act root:** b722 `%s` (previous `%s`, b721’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b722_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v7.txt at VERSION 7; tools/standing/ at %s (relay data/b722_standing_v121.txt); '
             'the standing report tool (relay data/b722_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written and no tag cut; the branch `%s` pushed on the six wave 1 kernels, five at their pins '
              'and SIDE-frobenius at the author’s two workflow lines (`%s`); port-b707 at %s, kept, its tag %s at it; SIDE-faces-join at %s with '
              'its one tag %s; no lean process on this host, %d runs, each read by its run id.' % (
                  K.REBUILD_BRANCH, K.FROBENIUS_TWO_LINES[:8], K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0],
                  len(K.REBUILD_RUNS)), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b722_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b721’s %s, %s, %s, %s (relay data/b722_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b722_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _title_b721():
    """b721's title over b721's objects, kept for the record and not called (Component 6)."""
    f = _figs_b721()
    return ('## The -39 law registered before its computation; the standing toolset at %s with %s of %s steps STANDING; Silence’s SIDESystem row '
            'corrected; %s Correspondence rows pinned; the federation pin and the Lean count priced' % (
                f['ver'], f['cv_std'], f['cv_steps'], f['ks_pinned']))


def _letters_now():
    """the letters the trail carries: those the seal records (row (52)); before the seal (a dry run) the defects bank's, by the same reader."""
    seal = letters_at_seal(ACT)
    return seal if seal is not None else _defect_short(ACT)


def _owners_now():
    rows = _letters_now()
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author_b721():
    rows, nav = _owners_now()
    f = _figs_b721()
    seat = AC.defect_owners(rows)['SEAT']   # ### (R332)(4)(iii), v4 row (64): the one counter (b721's form counted every row not the navigator's)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) the citation check’s one miss, (R332)(1)’s “the pins census at 39 public repositories”, read as 39 repositories of which 38 '
            'PUBLIC, PLACE-papers PRIVATE (relay data/b722_citation_check.txt, data/b721_pins_census.txt :27); (2) the -39 price’s third tier, '
            '[200, 300], priced for the author’s word and entered only where b722’s pair rows ask it; its act budget the seat’s estimate, about %s '
            'foreground hours (relay data/b722_price.txt); (3) the federation pin’s breakage not read, a halt: no ref of a kernel below the target '
            '%s carries the bump, and a dry build needs a bump branch on each, a write outside (R332)(8)’s list; SIDE-frobenius, with no run read, '
            'named UNPRICED (relay data/b722_federation_pin_price.txt); (4) the Lean count’s price the seat’s, %s dispatches and %s foreground '
            'hours, its needles printing their yields, four reading 0 in Mathlib at the target (relay data/b722_epstein_count_price.txt); (5) the '
            '%s names the census carries no row of their own for, listed and carried, none pinned from a paper’s own table (relay '
            'data/b722_correspondence_pins.txt); (6) Silence :212’s axiom-profile and status cells carried as they stood, not re-verified, no Lean '
            'process run (relay data/b722_keystone.txt); (7) the price tools’ requests to github.com unauthenticated, each URL carrying the public '
            'repository’s own address and no identifier of the author in any header; (8) the coverage table at %s of %s steps STANDING, only the '
            'seal moved by (3)(ii), the other repairs landing inside the per-act steps they govern (relay data/b722_toolset_coverage.txt); '
            '(9) the report tool outside the sealed list until the root (relay data/b708_rules.txt row (1)); (10) %s and the seat’s %s defect%s '
            'as lettered' % (
                f['pr_budget'], f['fp_target'], f['ep_disp'], f['ep_hours'], f['ks_carried'], f['cv_std'], f['cv_steps'],
                # ### the standing reader's form (the gate's and the suite's RESOLVED): the count as a word, "none" for zero (defect (r))
                'the %s navigator %s%s' % (num_word(len(nav)), 'miss' if len(nav) == 1 else 'misses', (' (%s)' % letters) if nav else ''),
                num_word(seat), '' if seat == 1 else 's'))


def _finding_text_b721():
    """the FINDINGS entry, composed before the root: its head line the result sentence, the result before its conditions; its scores line from the
    scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs_b721()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The prediction for discriminant -39 stands committed before any computation at it: the least index with a negative log-derivative '
         'coefficient has b(n) = -2 and an index divisible by a prime no principal form represents, its count control reading %s misses through '
         'n = 400 in the act’s first commit; the standing toolset at %s rebuilds b721’s, b714’s and b713’s closes at %s of %s objects EQUAL, its '
         '%d class repairs each holding on a record instance and a constructed one, %s of the close’s %s steps now STANDING; Silence’s '
         'SIDESystem row names SIDE-meta’s structure, entered as ERRATA %s; %s of %s Correspondence names gain their pins from the census, %s '
         'carried; and two prices stand, nothing built -- the federation pin at %s for %s kernels below it, %s dispatches and %s runner hours, its '
         'breakage a halt, and the Lean count of one band at Q0, %s dispatches, grading %s.' % (
             f['g_miss'], f['ver'], f['rp_eq'], f['rp_obj'], f['n_repairs'], f['cv_std'], f['cv_steps'], f['ks_errata'], f['ks_pinned'],
             f['ks_names'], f['ks_carried'], f['fp_target'], f['fp_below'], f['fp_disp'], f['fp_hours'], f['ep_disp'], f['ep_grade']), '',
         '*Filed at b722 on the author’s ruling `(R332)`; %d question%s put before the root. Banks: relay `data/b722_registrations.txt`, '
         '`data/b722_genus_control.txt`, `data/b722_price.txt`, `data/b722_standing_scan.txt`, `data/b722_replay.txt`, '
         '`data/b722_toolset_coverage.txt`, `data/b722_standing_controls.txt`, `data/b722_roster.txt`, `data/b722_tool_repairs.txt`, '
         '`data/b722_keystone.txt`, `data/b722_correspondence_pins.txt`, `data/b722_keystone_diffs.txt`, `data/b722_federation_pin_price.txt`, '
         '`data/b722_epstein_count_price.txt`, `data/b722_corrigendum.txt`, `data/b722_standing_figures.txt`, `data/b722_report.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** ((R332)(1), (2)): b721 entered at its weight as its closing prints (FINDINGS :%s); the corrigendum generated from '
         'b721’s defects and events, %d items by their starting lines, each NEW or REPEAT, %d lettered and %d records, the repeat fraction %s (%s), at '
         'FINDINGS :%s; the corrigenda bank appended at row (%s).' % (
             f['weight'], f['corr_items'], f['corr_n'], f['corr_rec'], f['rep'], f['rep_f'], f['corr_line'], f['corr_row']), '',
         '**The -39 registration** ((R332)(4), N2): relay data/b722_registrations.txt, the act’s first commit, alone with its count control: the '
         'forms of discriminant -39 and the class group of order 4, the principal form’s Epstein zeta decomposed by the group’s characters '
         '(Murty-Osburn arXiv:math/0412237v1 Theorem 2.3, as pinned at b713), the decomposition read through n = 400 with %s misses and three '
         'planted controls failing as wanted (relay data/b722_genus_control.txt); the prediction -- the least negative coefficient’s b(n) = -2, '
         'its index divisible by a prime of no principal form -- with its falsifier; b710’s refined detection law carried unchanged, its window '
         '[0.99, 1.01]. Its price: the list’s base and first two tiers %s h upper, %s h lower, the coefficients’ cut %s, the act about %s '
         'foreground hours (relay data/b722_price.txt). Nothing of -39 computed beyond the control.' % (
             f['g_miss'], f['pr_up'], f['pr_low'], f['pr_cut'], f['pr_budget']), '',
         '**The standing toolset** ((R332)(3)): tools/standing/ at %s, %s files, three new (allow.py, rootbanks.py, words.py), every change by '
         'diff (relay data/b722_tool_repairs.txt); the literal scan over the code %s act literals and %s delete words, its planted control as '
         'wanted (relay data/b722_standing_scan.txt); the coverage table rewritten, %s steps of the close in v5’s order, %s STANDING (%s) beside '
         'v1.0.0’s %s, %s PER-ACT, %s step moved by this version (relay data/b722_toolset_coverage.txt).' % (
             f['ver'], f['sc_files'], f['sc_lit'], f['sc_del'], f['cv_steps'], f['cv_std'], f['cv_std_at'], f['cv_std_prev'], f['cv_per'],
             f['cv_moved']), '',
         '**The replay** ((R332)(3), N3): the toolset over b721’s, b714’s and b713’s committed banks, writing nothing but relay '
         'data/b722_replay.txt: %s objects, %s EQUAL, %s DIFFERS %s, named by its finding; %s findings the old tools’ and not copied forward.' % (
             f['rp_obj'], f['rp_eq'], f['rp_diff'], f['rp_diffs'], f['rp_find']), '',
         '**The class repairs** ((R332)(3)(i)-(vi), N3): (i) an arm reads its allowances (deletes, prompts) from the ruling and the words bank; '
         '(ii) the seal commits what it hashes and records that commit as its head; (iii) the mirror’s verifier reads the builder’s roster; (iv) '
         'the answers route reads every word by its “## (n)” head; (v) a word received after a sealed composition printed beside its clause; (vi) '
         'the root’s required banks read against its exclusion at import. Each with its two instances, one from the record and one constructed, '
         'beside v1.0.0’s: %s cases, %s as wanted, %s repairs each with both instances (relay data/b722_standing_controls.txt); the roster’s '
         'controls %s as wanted, %s joining (relay data/b722_roster.txt).' % (
             f['cc_cases'], f['cc_wanted'], f['cc_repairs'], f['ro_ctl'], ', '.join(f['ro_joins'])), '',
         '**The keystone edits** ((R332)(5)(iii), (v)): day1/Silence_of_Foundations.md :212 corrected on PLACE-papers main to SIDE-meta, '
         '`SIDEMeta.SIDESystem` at SIDEMeta/Meta/SIDESystem.lean :99, a structure, at v0.3 = 6bb7b23, entered as ERRATA %s; the census v0.8.2’s '
         'rows as b721’s banks state them, all 24 written, nothing to carry; %s files edited on main, every edit diffed (relay '
         'data/b722_keystone.txt, data/b722_keystone_diffs.txt).' % (f['ks_errata'], f['ks_files']), '',
         '**The Correspondence pins** ((R332)(5)(iv)): of the %s names with no pin (relay data/b714_pilot.txt (P1)), %s pinned from the census '
         'at its edition on main by the Edit tool, %s listed and carried, the census carrying no row of their own (relay '
         'data/b722_correspondence_pins.txt, data/b722_correspondence_census.txt).' % (f['ks_names'], f['ks_pinned'], f['ks_carried']), '',
         '**The prices** ((R332)(6), nothing built): (i) the federation pin -- %s public kernels, %s with Mathlib at %s revs, the target %s, %s '
         'below it, %s dispatches and %s runner hours priced, the modules a bump would break not read (a halt: no ref carries the bump), %s '
         'requests unauthenticated, %s failed (relay data/b722_federation_pin_price.txt); (ii) the Lean count of the band [%s] at Q0, N %s, '
         'Mathlib read at the target, %s dispatches and %s foreground hours, the result grading %s under E0 (relay '
         'data/b722_epstein_count_price.txt).' % (
             f['fp_kern'], f['fp_ml'], f['fp_revs'], f['fp_target'], f['fp_below'], f['fp_disp'], f['fp_hours'], f['fp_req'], f['fp_fail'],
             f['ep_band'], f['ep_n'], f['ep_disp'], f['ep_hours'], f['ep_grade']), '',
         '**The standing arms**: the four figures at b722 -- %s, %s, %s, %s -- against b721’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b722_standing_figures.txt); no standing arm added.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each miss raised before the component '
         'citing it; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the registration and the federation price meet at the same seam -- the -39 prediction '
         'is a Python-certified reading, and the Lean count’s price shows what a KERNEL-footed band would ask once the kernels share the target '
         'rev; the Correspondence pins and the federation census read the same kernels, so a pin the papers now print is a rev the federation '
         'would move.', '',
         '**Carried to:** b722, each from its bank: the computation at -39 under this act’s commit where its price fits one act; the author’s '
         'words on the heads draft’s sections II and III and on the six lint hits, put in this act’s root prompt, applied; the federation pin '
         'where its price fits one act; the %s names the census does not pin; the Lean count of one band, priced; the draft held at v5.' % (
             f['ks_carried']), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _trail_text_b721():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs_b721()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R332) ratified.** (1) b721 at its weight. (2) The corrigendum. (3) The standing toolset at %s. (4) The registration for '
             'discriminant -39. (5) The keystone items carried from b714 and b721. (6) Two prices, nothing built. (7) The branches and carried '
             'files at step zero. (8) The read-first bank, the citation check, the root’s prompt and the write list. (9) The draft held at v5. '
             '(10) The act’s place on the paper path and the next act.' % f['ver'], '',
             '**Entered:** FINDINGS.md:%s (b721’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The registration:** relay data/b722_registrations.txt with its count control the act’s first commit, %s misses through n = 400 '
             '(relay data/b722_genus_control.txt); nothing of -39 computed; its price about %s foreground hours (relay data/b722_price.txt).' % (
                 f['g_miss'], f['pr_budget']), '',
             '**The toolset:** tools/standing/ at %s, %s files, %s act literals and %s delete words in the code (relay data/b722_standing_scan.txt); '
             'the coverage table %s STANDING of %s steps (relay data/b722_toolset_coverage.txt); the replay over b721, b714 and b713 %s of %s EQUAL, '
             '%s DIFFERS named, %s findings (relay data/b722_replay.txt); the class repairs %s cases as wanted %s, %s repairs each with both '
             'instances (relay data/b722_standing_controls.txt); the roster`s controls %s (relay data/b722_roster.txt).' % (
                 f['ver'], f['sc_files'], f['sc_lit'], f['sc_del'], f['cv_std'], f['cv_steps'], f['rp_eq'], f['rp_obj'], f['rp_diff'], f['rp_find'],
                 f['cc_cases'], f['cc_wanted'], f['cc_repairs'], f['ro_ctl']), '',
             '**The keystone items:** Silence :212 to SIDE-meta, ERRATA %s; %s of %s Correspondence names pinned from the census, %s carried; %s '
             'files edited on PLACE-papers main (relay data/b722_keystone.txt, data/b722_correspondence_pins.txt, data/b722_keystone_diffs.txt); the '
             'heads draft`s sections II and III and the six lint hits in the root`s prompt (relay data/b722_author_answers.txt).' % (
                 f['ks_errata'], f['ks_pinned'], f['ks_names'], f['ks_carried'], f['ks_files']), '',
             '**The prices:** the federation pin at %s, %s kernels below it, %s dispatches, %s runner hours, the breakage a halt (relay '
             'data/b722_federation_pin_price.txt); the Lean count of one band at Q0, %s dispatches, %s foreground hours, grading %s (relay '
             'data/b722_epstein_count_price.txt); nothing built.' % (
                 f['fp_target'], f['fp_below'], f['fp_disp'], f['fp_hours'], f['ep_disp'], f['ep_hours'], f['ep_grade']), '',
             '**Act root:** b722 `%s` (previous `%s`, b721’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b722_author_answers.txt): the root’s own prompt, '
             'put once, carrying the heads draft`s sections II and III and the six lint hits ((R332)(5)(i)-(ii)); its answer in the closing '
             'line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses and the repairs:** relay data/standing_clauses_v5.txt at VERSION 5, unchanged this act; every change diffed in '
             'relay data/b722_tool_repairs.txt; the standing report tool (relay data/b722_report.txt).', '']
    aw = AC.author_words_section(ACT)   # ### (R332)(6)(i), v5 row (74): the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** port-b707 at b712’s tip %s, kept local and remote, no commit this act, b714’s tag %s at it; SIDE-faces-join at %s with '
             'its one tag %s; SIDE-explicit-formula and SIDE-lv-conservation’s main and deposit unmoved; no runner dispatch; no lean process on this host.' % (
                 K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
             '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main ((R332)(5)), its name in the '
             'closing (relay data/b722_closing.txt).', '',
             '**The open orders:** `W-ORD-KEYSTONE-HEADS` (the heads draft in the root`s prompt, the word applied at b722); `W-ORD-LV-FORWARD-PORT`; `W-ORD-LV-CLOSURE-JOIN`; '
             '`W-ORD-MOVES-BY-LOCUS`; `W-ORD-ENTRY-TAG-PRINTS`; `W-ORD-EXPLICIT-FORMULA-C1`; `W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-QUASI-RH-FIELD-WATCH`; '
             '`W-ORD-P3-CONTOUR-SIGMA`; `W-ORD-E0-MET-CLASSK`; `W-ORD-README-FIGURE-SCOPE`.', '',
             '**The standing arms:** the four figures %s, %s, %s, %s against b721’s %s, %s, %s, %s (relay data/b722_standing_figures.txt).' % (
                 f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                 f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b722_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _close_step(n):
    """(R332)(4)(vi), standing clauses v4 row (68), THE CLOSE IN ONE ORDER: the route is step [n] of the close and refuses, writing nothing,
    while a lower step's evidence is absent (tools/act_close.py close_refuses; a repair at b722, banked by diff)."""
    r = AC.close_refuses(ACT, n)
    if r:
        print(r, flush=True)
        sys.exit(5)
    print('  ### THE CLOSE IN ONE ORDER: STEP [%d] MAY RUN -- EVERY LOWER STEP`S EVIDENCE STANDS' % n, flush=True)


def closeorder(*a):
    """`closeorder <n>`: step [n] of v4 row (68) read against the lower steps' evidence before the seat runs it by hand (the record commit
    [19] among them); prints and exits 5 where it refuses; writes nothing."""
    if not a or not a[0].isdigit():
        for k, w, e in AC.close_steps():
            print('  [%d] %s (%s)' % (k, w[:90], e.replace('<act>', ACT)))
        return
    _close_step(int(a[0]))


def repaircontrols(*a):
    """data/b722_repair_controls.txt (.json): (R332)(4), each of the six repairs with its two-instance control -- one instance from the record
    (b721's own banks, commits and remotes) and one constructed (rows or banks made by the route in the scratchpad, or throwaway repositories
    made by the scratch control script for (v)) -- every instance printed with what it was wanted to read and what it read."""
    import io
    import subprocess
    import tempfile
    import b722_closing as CL
    SP = os.environ.get('B713_SCRATCH') or 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/3bbc6267-f2de-40fb-b160-263f3c982c61/scratchpad'
    out, J = [], {}

    def row(rep, inst, wanted, got, note=''):
        ok = (wanted == got)
        out.append('  (%s) %-12s wanted %s ; got %s ; %s%s' % (rep, inst, wanted, got, 'PASS' if ok else '### FAIL', (' -- ' + note) if note else ''))
        J.setdefault(rep, []).append(dict(instance=inst, wanted=str(wanted), got=str(got), ok=ok, note=note))

    def git(*args, repo=ROOT):
        return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8').stdout.strip()

    # ### (i) ONE LIST OF WRITES: b721's face (W) read by AC.w_patterns against b721's relay changes 4a383ac8..1290446c; constructed paths
    face12 = io.open(os.path.join(D, 'b721_registration_2026-10-25.txt'), encoding='utf-8').read()
    pats = AC.w_patterns(face12)
    ch = [p for p in git('diff', '--name-only', '4a383ac8', '1290446c').split(NL) if p]
    beyond = [p for p in ch if not AC.w_allows(p, pats, 'relay')]
    out.append('### (i) b721`s face (W): %d patterns read ; relay 4a383ac8..1290446c changed %d paths ; beyond the list %s' % (len(pats), len(ch), beyond or 'NONE'))
    row('i', 'record', 0, len(beyond), 'b721`s relay changes, every one inside its own face`s (W)')
    row('i', 'constructed', (True, False, False), (AC.w_allows('data/b721_x.txt', pats), AC.w_allows('data/zz_outside_b721.txt', pats),
                                                   AC.w_allows('FOUNDATIONS.md', pats, 'PLACE-papers')),
        'data/b721_x.txt inside ; data/zz_outside_b721.txt and PLACE-papers/FOUNDATIONS.md outside')

    # ### (ii) EVERY COMMIT OF A STEP: b721's gate (afe3903a, and dcb3b286 "the gate before the lock" entered under component 5); constructed
    st12 = jl('b721_steps.json')
    rows12 = st12 if isinstance(st12, list) else st12.get('rows', [])
    g_one = [r.get('commit', '')[:8] for r in rows12 if r.get('phase') == 'gate']
    joined = [dict(repo='relay', phase='gate', commits=['afe3903acfd0e4c790a34015d5fa142d1d52b812', 'dcb3b2862324ddbde0bd8ee08a893141fcda38c2'])]
    out.append('### (ii) b721`s step bank: the gate phase`s rows read by their one `commit`: %s ; dcb3b286`s subject names the gate, its phase %r' % (
        g_one, next((r.get('phase') for r in rows12 if r.get('commit', '').startswith('dcb3b286')), None)))
    row('ii', 'record', ['afe3903a', 'dcb3b286'], [c[:8] for c in AC.step_commits(joined, 'gate', 'relay')],
        'the gate`s two commits on one row, read whole (the one-`commit` form reads %s)' % [r.get('commit', '')[:8] for r in joined if r.get('commit')])
    three = [dict(repo='relay', phase='component 9', commit='c1', commits=['c1', 'c2', 'c3']), dict(repo='pp', phase='component 9', commit='c4')]
    row('ii', 'constructed', ['c1', 'c2', 'c3'], AC.step_commits(three, 'component 9', 'relay'),
        'a three-commit step: the one-`commit` form reads [c1], c2 and c3 undeclared; the other repository`s c4 not read')

    # ### (iii) ONE COUNTER: b721's defects bank (b721's record tool counted 22 for the seat, its suite 21); constructed rows
    d12 = [l for l in io.open(os.path.join(D, 'b721_defects.txt'), encoding='utf-8').read().split(NL) if AC.OWNER.match(l.lstrip())]
    c12 = AC.defect_owners(d12)
    row('iii', 'record', (22, 21, 0, 1), (c12['TOTAL'], c12['SEAT'], c12['NAVIGATOR'], c12['OTHER']),
        'TOTAL, SEAT, NAVIGATOR, OTHER: (h) THE CARRIED RECORD TOOL`S FORM is OTHER; both tools now read the one number')
    c3 = AC.defect_owners(["(a) THE SEAT'S: x", "(b) THE NAVIGATOR'S: y", "(c) THE RECORD TOOL'S: z", "(a') THE SEAT’S: w", 'no row'])
    row('iii', 'constructed', (4, 2, 1, 1), (c3['TOTAL'], c3['SEAT'], c3['NAVIGATOR'], c3['OTHER']), 'a primed letter and a curly apostrophe counted')

    # ### (iv) THE LOCK AS A MEMBRANE: b721's lock is written, its dry root bank refuses; a constructed act's banks before and after its lock
    row('iv', 'record', True, bool(AC.lock_refuses('b721', 'b721_root_banks_dry.json')), 'b721_lockgate.json stands; a rewrite of [2]`s bank refused')
    td = tempfile.mkdtemp(prefix='b722_lock_', dir=SP)
    for n_ in ('b999_root_banks_dry.json', 'b999_standing_figures.json'):
        io.open(os.path.join(td, n_), 'w', encoding='utf-8').write('{}')
    before = bool(AC.lock_refuses('b999', 'b999_root_banks_dry.json', td))
    io.open(os.path.join(td, 'b999_lockgate.json'), 'w', encoding='utf-8').write('{}')
    after = (bool(AC.lock_refuses('b999', 'b999_root_banks_dry.json', td)), bool(AC.lock_refuses('b999', 'b999_scores.json', td)))
    row('iv', 'constructed', (False, True, False), (before,) + after,
        'scratch %s: before the lock writable ; after it [2]`s bank refused ; [9]`s scores bank (after the lock) writable' % os.path.basename(td))

    # ### (v) A CAPTURE FOR EVERY PUSH, THE HEAD LINE FROM ls-remote: b721's head line read again; the scratch script's two clones
    ev = []
    hl = CL.head_line(act='b721', events=ev)
    m_ = re.search(r'relay (\w+), PLACE-papers (\w+)', hl)
    out.append('### (v) b721`s head line read again by the repaired builder: %s' % hl)
    out += ['      event: ' + e for e in ev]
    row('v', 'record', True, bool(m_) and 'none' not in (m_.group(1), m_.group(2)),
        'each repository`s main read at the remote (b721`s own head line read "none read" for both, events :48)')
    r_ = subprocess.run(['bash', SP + '/control_v_capture.sh'], capture_output=True, text=True, encoding='utf-8')
    out += ['      ' + l for l in r_.stdout.strip().split(NL)]
    got_v = tuple(re.findall(r'captures written (\d+) ; name \S+ ; the capture carries the read-back (\w+)', r_.stdout))
    row('v', 'constructed', (('1', 'yes'), ('0', 'no')), got_v, 'a file:// origin captured unasked, a plain-path origin (the tests`) not')

    # ### (vi) THE CLOSE IN ONE ORDER: b721's banks replayed by their mtimes at its record commit (755b03aa) and at its scores-close bank
    t_rec = int(git('show', '-s', '--format=%ct', '755b03aa') or 0)
    t_sc = int(os.path.getmtime(os.path.join(D, 'b721_scores_close.json')))
    alias = {'b721_closing_dry.txt': 0, 'b721_scores_dry.txt': 0, 'b721_relay_push-b721-record_push_out.txt': t_rec}

    def at(T):
        def has(p):
            b = os.path.basename(p)
            if b in alias:
                return T >= alias[b]
            return os.path.exists(p) and os.path.getmtime(p) <= T
        return has
    r19, r22 = AC.close_refuses('b721', 19, present=at(t_rec)), AC.close_refuses('b721', 22, present=at(t_sc))
    out.append('### (vi) b721 replayed (its dry runs [3] [4] in the scratchpad, recorded in its gate; [19] its record push 755b03aa, no capture):')
    out += ['      step [19] at %s: %s' % (t_rec, r19 or 'MAY RUN'), '      step [22] at %s: %s' % (t_sc, r22 or 'MAY RUN')]
    row('vi', 'record', True, bool(r19 or r22), 'b721 closed out of v4`s order: a step ran while a lower step`s evidence was absent')
    td2 = tempfile.mkdtemp(prefix='b722_order_', dir=SP)
    for k, w, e in AC.close_steps():
        if k <= 5 and e.startswith('data/'):
            io.open(os.path.join(td2, os.path.basename(e.replace('<act>', 'b999'))), 'w', encoding='utf-8').write('{}')
    g6, g7 = AC.close_refuses('b999', 6, td2), AC.close_refuses('b999', 7, td2)
    row('vi', 'constructed', ('', True, True), (g6, bool(g7), '[6]' in g7), 'banks [1]-[5] in scratch %s: [6] may run ; [7] refused naming [6]' % os.path.basename(td2))

    npass = sum(1 for v in J.values() for x in v if x['ok'])
    ntot = sum(len(v) for v in J.values())
    L = ['%s -- THE SIX REPAIRS OF (R332)(4), EACH WITH ITS TWO-INSTANCE CONTROL (standing clauses v4 rows (62)-(68)) (%s)' % (ACT, utc()), '',
         '### one instance from the record (b721`s banks, commits and remotes), one constructed (rows here, banks in the scratchpad, throwaway',
         '### repositories for (v)); the functions are tools/act_close.py`s, the head line tools/b722_closing.py`s, the capture tools/push_gated.sh`s.',
         '### (vi)`s record instance reads b721`s banks by their file times (a bank rewritten later reads absent at the earlier time).', ''] + out + [
         '', '### ### **CONTROLS %d ; PASSING %d ; THE SIX REPAIRS EACH WITH TWO INSTANCES %s.**' % (ntot, npass, all(len(J.get(x, [])) == 2 for x in
                                                                                                       ('i', 'ii', 'iii', 'iv', 'v', 'vi')))]
    if a and a[0] == 'dry':
        print(NL.join(L))
        return
    put_txt('%s_repair_controls.txt' % ACT, L)
    put_json('%s_repair_controls.json' % ACT, dict(at=utc(), controls=J, passing=npass, total=ntot))
    print(NL.join(L))


REPAIR_KEYS = (('i', 'ONE LIST OF WRITES', '(62)', r'w_patterns|w_allows'),
                ('ii', 'EVERY COMMIT OF A STEP', '(63)', r'step_commits'),
                ('iii', 'ONE COUNTER', '(64)', r'defect_owners'),
                ('iv', 'THE LOCK AS A MEMBRANE', '(65)', r'lock_refuses|_lock_guard'),
                ('v', 'A CAPTURE FOR EVERY PUSH, THE HEAD LINE FROM ls-remote', '(66)', r'read_remotes|PUSH_GATED_CAPTURE_DIR'),
                ('vi', 'THE CLOSE IN ONE ORDER', '(67), (68)', r'close_refuses|_close_step|close_steps'))


def toolrepairs13(*a):
    """data/b722_tool_repairs.txt (.json): (R332)(4), each repair's diff -- the hunks of the carry-time diffs (data/b722_repairdiff_record.txt,
    _checks.txt, _closing.txt) whose added lines name the repair or call its function, tools/push_gated.sh's diff against relay HEAD, and
    tools/act_close.py (a new shared tool, untracked till the component's commit) by its sections -- each repair's control line beside it."""
    import io
    hunks = []
    for n_ in ('record', 'checks', 'closing'):
        cur = None
        for l in io.open(os.path.join(D, '%s_repairdiff_%s.txt' % (ACT, n_)), encoding='utf-8').read().split(NL):
            if l.startswith('@@'):
                cur = dict(tool='tools/%s_%s.py' % (ACT, n_), lines=[l])
                hunks.append(cur)
            elif cur is not None and l[:1] in '+-' and not l.startswith('### ###'):
                cur['lines'].append(l)
            elif cur is not None and not l.strip():
                cur = None
    pg = subprocess.run(['git', '-C', ROOT, 'diff', 'HEAD', '--', 'tools/push_gated.sh'], capture_output=True, text=True, encoding='utf-8').stdout.split(NL)
    ac = io.open(os.path.join(T, 'act_close.py'), encoding='utf-8').read().split(NL)
    cj = jl('%s_repair_controls.json' % ACT).get('controls', {})
    L = ['%s -- THE SIX REPAIRS OF (R332)(4), EACH BY ITS DIFF (standing clauses v4 rows (61)-(68)) (%s)' % (ACT, utc()), '',
         '### per repair: the v4 row ; tools/act_close.py`s section (a new shared tool, every line added) ; the hunks of the carried tools` diffs',
         '### (data/b722_repairdiff_<tool>.txt) whose added lines name the repair or call its function ; tools/push_gated.sh`s diff against relay',
         '### HEAD for (v) ; the two controls (data/b722_repair_controls.txt).', '']
    J = {}
    for k, title, rows, fn in REPAIR_KEYS:
        tag = re.compile(r'\(R332\)\(4\)\(%s\)|%s' % (re.escape(k), fn))
        mine = [h for h in hunks if any(tag.search(l) for l in h['lines'] if l.startswith('+'))]
        L.append('### ### (%s) %s -- v4 row %s' % (k, title, rows))
        sec, on = [], False
        for i, l in enumerate(ac, 1):
            if l.startswith('# ====='):
                on = bool(re.search(r'\(%s\) ' % re.escape(k), l)) or (k == 'vi' and '(vi)' in l)
            if on:
                sec.append('+%s' % l)
        if sec:
            L += ['  --- tools/act_close.py (new) its section, %d lines:' % len(sec)] + ['  ' + s for s in sec]
        for h in mine:
            L += ['  --- %s %s' % (h['tool'], h['lines'][0])] + ['  ' + s for s in h['lines'][1:]]
        if k == 'v':
            L += ['  --- tools/push_gated.sh, git diff HEAD:'] + ['  ' + s for s in pg if s]
        L += ['  CONTROL %s: %s ; got %s ; %s' % (c['instance'], c['wanted'], c['got'], 'PASS' if c['ok'] else '### FAIL') for c in cj.get(k, [])]
        L.append('')
        J[k] = dict(title=title, v4_rows=rows, act_close_lines=len(sec), hunks=[(h['tool'], h['lines'][0]) for h in mine],
                    push_gated_lines=len([s for s in pg if s]) if k == 'v' else 0, controls=cj.get(k, []))
    nh = sum(len(v['hunks']) for v in J.values())
    L.append('### ### **REPAIRS %d ; HUNKS NAMED %d ; WITH tools/act_close.py`s SECTIONS AND push_gated.sh`s DIFF ; CONTROLS PASSING %d OF %d.**' % (
        len(J), nh, sum(1 for v in J.values() for c in v['controls'] if c['ok']), sum(len(v['controls']) for v in J.values())))
    if a and a[0] == 'dry':
        print(NL.join(L[-1:]))
        for k, v in J.items():
            print('  (%s) act_close %d ; hunks %s ; push_gated %d ; controls %d' % (k, v['act_close_lines'], v['hunks'], v['push_gated_lines'], len(v['controls'])))
        return
    put_txt('%s_tool_repairs.txt' % ACT, L)
    put_json('%s_tool_repairs.json' % ACT, dict(at=utc(), repairs=J))
    print(L[-1])


def components(*a):
    """`components [dry]`, step [18]: (R332)(4)(iv), the coverage table's [18] STANDING -- composed by tools/standing/components.py from the
    ruling's components (data/act_current.json) and the step bank; written through this tool's guarded writer (the membrane, the lock guard,
    the hash record); `dry` prints the lines and writes nothing, before the close order is read."""
    from standing import components as STCOMP
    cur = jl('act_current.json')
    L = STCOMP.composed(ACT, cur.get('components') or [], cur.get('ruling'))
    if 'dry' in a:
        print(NL.join(L))
        return
    _close_step(18)
    fj, tj = jl('%s_findings.json' % ACT), jl('%s_trail.json' % ACT)
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def scores(*a):
    """`scores [dry]` writes data/b722_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited (N4's and N5's close clauses, S1, S2) into data/b722_scores_close.json."""
    close = 'close' in a
    if 'dry' not in a:
        _close_step(22 if close else 9)   # ### (R332)(4)(vi): scores [9], scores close [22] (the events bank [21] before it)
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        # ### (R332)(4)(vi), v4 row (68) step [4]: the dry form banks its readings whole as the step's evidence (data/b722_scores_dry.txt),
        # ### which tools/act_close.py names and step [5] reads; the first form printed only (defect (n), a repair before the lock)
        L = ['%s -- THE SCORE ROUTES` DRY FORM, STEP [4] OF v4 ROW (68), ON THE REAL BANKS BEFORE THE LOCK (%s)' % (ACT, utc()), '',
             '### rows are the scores: key | verdict | the reading in full. A PENDING or REFUTED clause that waits on a later step (the seal, the',
             '### root, the closing) is read again at `scores` [9] and `scores close` [22]; this bank is a reading, not a score.', '']
        L += ['%s | %s | %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
        L += ['', '### ### **THE SCORE ROUTES RUN DRY: %s.**' % ' ; '.join('%s %s' % (k2, S[k2][0]) for k2 in SCORE_KEYS)]
        put_txt('%s_scores_dry.txt' % ACT, L)
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
    _close_step(12)   # ### (R332)(4)(vi): the FINDINGS entry, step [12]
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
    _close_step(15)   # ### (R332)(4)(vi): the trail carrying the root, step [15]
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
            oc = AC.defect_owners(rows)   # ### (R332)(4)(iii), v4 row (64): the one counter, the suite's arm's own (a repair at b722)
            wr = (num_word(oc['NAVIGATOR']), num_word(oc['SEAT']))
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
    """(R332)(3)(i), standing clauses v3: THE FACE NAMES THE ROOT'S PROMPT BY FORM -- the face's post-seal row built from the act's order: where
    the order puts the root's prompt after the lock, the row names it (b721's face read NONE with the root's prompt after its lock, events
    :61). Pure in its arguments; the seat writes the row into the face as printed by `facerows`."""
    n = (1 if root_prompt_after_lock else 0) + other_after_lock
    if n == 0:
        return '### POST-SEAL PROMPTS NAMED: NONE'
    return '### POST-SEAL PROMPTS NAMED: %d%s' % (n, ' (the root`s prompt)' if root_prompt_after_lock and not other_after_lock else '')


def facerows(*a):
    """prints the face rows built by form ((R332)(3)(i), (ii), (v)): the post-seal row from the act's order (the root's prompt after the lock,
    (R332)(9)); every relay and PLACE-papers commit of the act's step bank but the gate's, by its 7-hex prefix, for section (0); writes nothing."""
    print(post_seal_row(True))
    rows = jl('%s_steps.json' % ACT).get('rows') or []
    for r in rows:
        if r.get('phase') in PRE_SEAL_PHASES and r.get('phase') != 'gate':
            print('  %-5s %s  %-12s %s' % (r['repo'], r['commit'][:8], r['phase'], r.get('subject', '')[:90]))


def mirror_order(act, rootl, roots=None):
    """(R332)(3)(iv), standing clauses v3: THE MIRROR'S ORDER -- with the act's root appended, the export's MANIFEST must carry the root line
    `Act root: <act> <root>` before the mirror bank is written (b721 banked once with THE ROOT LINE : ### NONE, its mroot not yet run, events
    :75). The refusal's text, or '' where the bank may be written (pure in its arguments; `roots` names a test copy of the chain)."""
    line = MEM.appended(act, roots)
    if not line:
        return ''
    want = 'Act root: %s %s' % (act, line.split()[1])
    if any(l.startswith(want) for l in rootl):
        return ''
    return ('### (R332)(3)(iv) THE MIRROR`S ORDER: %s`S ROOT IS APPENDED AND THE EXPORT`S ROOT LINE READS %s, NOT %s... -- RUN mroot, THEN mverify, '
            'THEN mbank; NOTHING WRITTEN' % (act, (rootl[0][:40] if rootl else 'NONE'), want[:40]))


def mbank(*a):
    """b721's mbank carried with b722's names (the span line read from the mirror bank chain); (R332)(3)(iv): refused where the root is
    appended and the export carries no root line for it."""
    _close_step(23)   # ### (R332)(4)(vi): the mirror, step [23]
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
    # ### (R332)(2)(iii), tools/standing/ v1.2.1: the MANIFEST control reads every roster file against the commit the mirror is built at
    # ### (PLACE-papers HEAD at the build), by tools/standing/manifest.py control_at_build -- the inline loop against the carried
    # ### K.RECUT_MERGE (b716-b721's) removed, so (R328)(7)'s repair, made in the toolset and never wired here, now reaches this route
    sys.path.insert(0, os.path.join(T, 'standing'))
    import manifest as MF
    build = g(PP, 'rev-parse', 'HEAD').strip()
    mc = MF.control_at_build(ZIP, build)
    man_ctl = [dict(path=p, member=mem, raw_equal=raw, lf_equal=lf, state=st) for p, mem, raw, lf, st in mc['rows']]
    man_ok = mc['ok']
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE REPAIRED BUILDER OVER THE ROSTER FROM MAIN, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names_), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         span_line(ACT),
         '### THE ROSTER READ FROM PLACE-papers MAIN AT THE BUILD ((R332)(5); relay data/b722_roster.txt, the families of tools/mirror_roster.json, unedited); the builder`s state file tools/mirror_prevbuild.json written at this build, named in (W) ((R332)(10)); files %d' % len(files_),
         '### (R332)(2)(iii)`S MANIFEST CONTROL (tools/standing/manifest.py control_at_build, v1.2.1): every roster file at the build commit %s, '
         'its zip entry against its blob there, raw and with CR removed; rows %d, AS WANTED %d, NOT AS WANTED %d, NOT IN THE ROSTER %d:' % (
             build[:8], len(man_ctl), sum(1 for c in man_ctl if c['state'] == 'AS WANTED'), sum(1 for c in man_ctl if c['state'] == 'NOT AS WANTED'),
             sum(1 for c in man_ctl if c['state'] == 'NOT IN THE ROSTER'))] + [
         '    %s : zip entry %s ; equal raw %s, with CR removed %s ; %s' % (c['path'], c['member'] or '### NONE', c['raw_equal'], c['lf_equal'], c['state'])
         for c in man_ctl if c['state'] != 'AS WANTED'] + [
         '### ### **THE MANIFEST CONTROL %s**' % ('AS WANTED' if man_ok else '### NOT AS WANTED'),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names_]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names_), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT), manifest_control=man_ctl, manifest_ok=man_ok))
    for l in L[:16]:
        print(l[:240])


def guard(*a):
    """data/b722_guard_dry.txt (.json): the suite's `--guard-dry` run in its own process (it writes nothing), its print banked verbatim; the writes
    by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read by number."""
    import b722_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b722_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b722_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b722_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b722_checks.py :%d `%s`,'
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
    import b722_checks as CH
    src = rd(os.path.join(T, 'b722_record.py'))
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
    import b722_checks as CH
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


# ================================================================================ COMPONENT 1: (R332)(3)'S FIVE REPAIRS AND THE NEXT LINE, THEIR CONTROLS
def _b721_logs():
    """b721's relay and PLACE-papers commits as its step bank records them: [(hash, subject, epoch)]."""
    return [(r['commit'], r.get('subject', ''), int(r['ct'])) for r in jl('b721_steps.json').get('rows') or []]


def _count_pipes(text):
    try:
        return len(json.loads(text).get('any_pipes') or [])
    except Exception:
        return None


def repairctl12(*a):
    """data/b722_repair_controls.txt (.json), Component 1, (R332)(3): each of the five repairs and the NEXT line's repair run on b721's banks,
    each with the control the ruling names and a NEG case; every reading printed beside its case. The repaired forms are read where they
    stand: tools/b722_checks.py (post_seal_named, answers_bank_ok, nothing_ahead_ok), tools/b722_record.py (post_seal_row, mirror_order),
    tools/b722_closing.py (head_line, state_file_sentence), tools/b722_regspec.py (refresh_commands), tools/b722_worklist.py (orders_naming)."""
    import shutil
    import b722_checks as CK
    import b722_closing as CL
    import b721_checks as CK7
    rows, notes = [], []

    def case(sec, name, got, want, note=''):
        rows.append(dict(section=sec, case=name, got=got, wanted=want, as_wanted=got == want, note=note))

    lock = CK.iso_epoch(jl('b721_seal_hashes.json')['lock'])
    face7 = rdn('b721_registration_2026-10-25.txt')
    a7, aj7 = rdn('b721_author_answers.txt'), jl('b721_author_answers.json')
    # ---------------------------------------------------------------- (i) THE FACE NAMES THE ROOT'S PROMPT BY FORM
    row1 = post_seal_row(True)
    face_1 = face7.replace('### POST-SEAL PROMPTS NAMED: NONE', row1)
    case('i', 'the builder`s row where the order puts the root`s prompt after the lock', row1, '### POST-SEAL PROMPTS NAMED: 1 (the root`s prompt)')
    case('i', 'the builder`s row where no prompt follows the lock (NEG of the form)', post_seal_row(False), '### POST-SEAL PROMPTS NAMED: NONE')
    case('i', 'b721`s answers bank under the repaired arm, its face naming 1: passes', CK.answers_bank_ok(a7, aj7, lock, face_1, 'b721', CK7.FLOORS), True)
    case('i', 'b721`s answers bank under the repaired arm, a face naming 0 (b721`s own, NONE): fails', CK.answers_bank_ok(a7, aj7, lock, face7, 'b721', CK7.FLOORS), False)
    case('i', 'the arm reads the row`s figure from the form "1 (the root`s prompt)"', CK.post_seal_named(face_1), 1)
    after = [c.get('ts') for c in aj7.get('calls') or [] if CK.iso_epoch((c.get('ts') or '')[:19] + 'Z') and CK.iso_epoch((c.get('ts') or '')[:19] + 'Z') > lock]
    notes.append('(i) b721`s lock %s ; its answers bank`s calls after the lock %s ; b721`s face row %r' % (
        jl('b721_seal_hashes.json')['lock'], after, (re.search(r'### POST-SEAL PROMPTS NAMED: \S+', face7) or [None])[0]))
    # ---------------------------------------------------------------- (ii) THE GATE'S COMMIT READ FROM THE STEP BANK
    logs = _b721_logs()
    steps7 = jl('b721_steps.json').get('rows') or []
    marked = [dict(r, phase='gate') if r['commit'].startswith('85c26c1c') else r for r in steps7]
    case('ii', 'b721`s banks pass with 85c26c1c read as the gate (its step row marked gate in a copy)', CK.nothing_ahead_ok(face7, lock, logs, marked), True)
    case('ii', 'an undeclared commit before the lock fails (NEG)', CK.nothing_ahead_ok(face7, lock, logs + [('deadbeefcafe', 'x', lock - 60)], marked), False)
    case('ii', 'b721`s step bank as banked, no row marked gate: fails (the gate`s commit undeclared)', CK.nothing_ahead_ok(face7, lock, logs, steps7), False)
    case('ii', 'b721`s old arm on the same banks (every commit before the lock on the face): fails on 85c26c1c',
         all(h[:7] in face7 for h, s, t in logs if t <= lock), False)
    notes.append('(ii) b721`s commits at or before the lock %d ; on the face %d ; not on the face %s' % (
        len([1 for h, s, t in logs if t <= lock]), len([1 for h, s, t in logs if t <= lock and h[:7] in face7]),
        [h[:8] for h, s, t in logs if t <= lock and h[:7] not in face7]))
    # ---------------------------------------------------------------- (iii) THE HEAD LINE BUILT FROM BANKS
    sp = os.path.join(K.SP, 'b722_ctl_headline_%d' % int(time.time()))   # ### a new scratch directory per run; nothing is deleted
    os.makedirs(sp)
    for f in os.listdir(D):
        if f.startswith('b721_') and (f.endswith('push_out.txt') or f in ('b721_checks_postpush.txt', 'b721_act_root.json', 'b721_author_answers.txt',
                                                                          'b721_defects.txt', 'b721_scores_close.json')):
            shutil.copyfile(os.path.join(D, f), os.path.join(sp, f))
    ev = []
    hl = CL.head_line(dd=sp, act='b721', events=ev)
    case('iii', 'b721`s banks rebuild the head line with "1 prompt answered"', '; 1 prompt answered;' in hl, True)
    case('iii', 'b721`s banks rebuild the head line with "scores 8 of 8 HELD"', '; scores 8 of 8 HELD;' in hl, True)
    sc = jl('b721_scores_close.json')
    sc['N2'] = ['BROKEN', 'a planted BROKEN for the control']
    with open(os.path.join(sp, 'b721_scores_close.json'), 'w', encoding='utf-8') as fh:
        json.dump(sc, fh, ensure_ascii=False)
    hl7 = CL.head_line(dd=sp, act='b721', events=[])
    case('iii', 'a scores bank with one BROKEN prints 7 of 8 (NEG)', '; scores 7 of 8 HELD;' in hl7, True)
    case('iii', 'b721`s own head line (data/b721_closing.txt :1) carried 2 prompts and no score', ('2 prompts answered' in rdn('b721_closing.txt').split(NL)[0])
         and 'scores' not in rdn('b721_closing.txt').split(NL)[0], True)
    notes.append('(iii) rebuilt: %s' % hl)
    notes.append('(iii) with one BROKEN: %s' % hl7)
    # ---------------------------------------------------------------- (iv) THE MIRROR'S ORDER
    import zipfile
    zl = zipfile.ZipFile('D:/MY-DOwnloads/mirror-refresh-2026-10-25-b721.zip').read('MANIFEST.md').decode('utf-8-sig').replace(chr(13), '').split(NL)
    root7 = [l for l in zl if l.startswith('Act root: ')]
    case('iv', 'b721`s sequence replayed on a copy: the bank before mroot (the export`s root line NONE, b721`s root appended) refuses',
         bool(mirror_order('b721', [])), True)
    case('iv', 'after mroot (the export`s root line b721`s): the bank may be written', mirror_order('b721', root7), '')
    case('iv', 'a root line naming another act`s root refuses (NEG)', bool(mirror_order('b721', ['Act root: b710 11fe3e21'])), True)
    case('iv', 'before the act`s root is appended the order does not refuse (b722 now)', mirror_order('b722', []), '')
    notes.append('(iv) b721`s export`s root line now %r ; the refusal before mroot: %s' % (root7[:1], mirror_order('b721', [])[:120]))
    # ---------------------------------------------------------------- (v) THE COMMAND SCREEN READS A FRESH BANK; THE STATE FILE'S BLOB
    stale = _count_pipes(g(ROOT, 'show', '85c26c1c:data/b721_commands.json'))
    fresh = _count_pipes(rdn('b721_commands.json'))
    case('v', 'b721`s stale command bank (at its gate commit 85c26c1c) reproduces ANYPIPES 7', stale, 7)
    case('v', 'the fresh bank (refreshed after the seal, 13:04Z) reads 8', fresh, 8)
    blob7, blob11 = g(ROOT, 'rev-parse', 'b5898a61:tools/mirror_prevbuild.json').strip(), g(ROOT, 'rev-parse', '4a383ac8:tools/mirror_prevbuild.json').strip()
    case('v', 'tools/mirror_prevbuild.json`s blob at b721`s closing (4a383ac8) equal to b707`s (b5898a61): b721`s "committed with this closing" false',
         bool(blob7) and blob7 == blob11, True)
    sfs = CL.state_file_sentence()
    case('v', 'the repaired sentence now: "unchanged since its last commit", not "committed"', 'unchanged since its last commit' in sfs and 'not committed' in sfs, True)
    notes.append('(v) ANYPIPES stale %s, fresh %s ; the blob at b707 %s, at b721`s closing %s ; the sentence now: %s' % (stale, fresh, blob7[:8], blob11[:8], sfs))
    # ---------------------------------------------------------------- THE NEXT LINE
    ot = rd(OT)
    found = K.orders_naming(ot, 'b722')
    plant = ot + NL + '*Appended 2026-10-25 by b799 -- THE ORDER **`W-ORD-PLANTED-CONTROL`**: a planted row. Status OPEN, for b722.' + NL
    case('NEXT', 'a planted open-orders row whose status names b722 is printed by the NEXT line', 'W-ORD-PLANTED-CONTROL' in K.next_line(text=plant), True)
    case('NEXT', 'the same row is not printed for another act (NEG)', any(o == 'W-ORD-PLANTED-CONTROL' for _i, o, _s in K.orders_naming(plant, 'b722')), False)
    case('NEXT', 'the NEXT line opens with the ruling`s named items', K.next_line(text=plant).startswith(K.NEXT), True)
    notes.append('(NEXT) the open-orders rows whose status names b722 on OPEN_TRAILS now: %s' % (found or 'NONE'))
    notes.append('(NEXT) the line now: %s' % K.next_line()[:400])
    notes.append('(iii) the scratch copies: %s (left in the scratchpad)' % sp)
    nw = [r for r in rows if not r['as_wanted']]
    L = ['%s -- COMPONENT 1, (R332)(3): THE FIVE REPAIRS AND THE NEXT LINE`S, EACH ON b721`S BANKS WITH ITS CONTROL (%s)' % (ACT, utc()), '',
         '### rows are cases: the section | the case | the reading got | the reading wanted | AS WANTED. The sections: (i) the face names the root`s',
         '### prompt by form; (ii) the gate`s commit from the step bank; (iii) the head line from banks; (iv) the mirror`s order; (v) the command',
         '### screen`s fresh bank and the state file`s blob; NEXT the open-orders rows. Each control is (R332)(3)`s own; a NEG case beside it. The',
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
    ('(56)', '(R332)(3)(i), THE FACE NAMES THE ROOT`S PROMPT BY FORM',
     'tools/b722_record.py post_seal_row and the `facerows` route (the face`s post-seal row built from the act`s order: "### POST-SEAL PROMPTS NAMED: '
     '1 (the root`s prompt)" where the root`s prompt follows the lock); tools/b722_checks.py post_seal_named and answers_bank_ok (G-ANSWERS-BANKED '
     'reading that row, pure in its banks), answers_ok calling it. Answers b721`s events :61. Control: data/b722_repair_controls.txt (i)'),
    ('(57)', '(R332)(3)(ii), THE GATE`S COMMIT READ FROM THE STEP BANK',
     'tools/b722_record.py PRE_SEAL_PHASES with the phase `gate`; tools/b722_checks.py nothing_ahead_ok (the one step-bank row of phase gate exempt, '
     'every other commit at or before the lock declared on the face by its hash), G-NOTHING-RAN-AHEAD calling it. Answers b721`s events :66. Control: (ii)'),
    ('(58)', '(R332)(3)(iii), THE HEAD LINE BUILT FROM BANKS',
     'tools/b722_closing.py head_line: the prompt count the answers bank`s rows with nothing added (b700`s "+ 1" removed), the scores "scores <k> of 8 '
     'HELD" from the scores-close bank. Answers b721`s events :79. Control: (iii)'),
    ('(59)', '(R332)(3)(iv), THE MIRROR`S ORDER',
     'tools/b722_record.py mirror_order and mbank: the mirror bank refused, nothing written, while the act`s root is appended and the export`s root '
     'line does not read the act`s root. Answers b721`s events :75. Control: (iv)'),
    ('(60)', '(R332)(3)(v), THE COMMAND SCREEN READS A FRESH BANK',
     'tools/b722_regspec.py refresh_commands (the command bank rewritten by the record tool`s `commands` route in the spec`s own step, the spec '
     'refused where it is not); tools/b722_closing.py state_file_sentence (the state file`s blob against HEAD and its last commit before "committed"), '
     'mirror_line calling it. Answers b721`s events :3 and the added item of (R332)(2). Control: (v)'),
    ('NEXT', 'THE NEXT LINE',
     'tools/b722_worklist.py orders_naming and next_line (the ruling`s named items, then every open-orders row of OPEN_TRAILS whose status names '
     'the next act, read at closing time); tools/b722_record.py the entry`s and the trail`s Next lines calling it. Answers b721`s events :46. Control: NEXT'),
)
REPAIR712_TRACKED = ('tools/b722_record.py', 'tools/b722_worklist.py', 'tools/b722_checks.py', 'tools/b722_closing.py', 'tools/b722_regspec.py')


def toolrepairs12(*a):
    """data/b722_tool_repairs.txt (.json), Component 1, (R332)(3): each repair's row (its standing clauses v3 row, its objects, its control's
    section in data/b722_repair_controls.txt) and the diffs of the five tools against their commit at step zero (relay 46750da9), each whole.
    The standing report tool's row is appended at Component 5, when its items are written."""
    ctl = jl('%s_repair_controls.json' % ACT)
    if not ctl.get('cases'):
        sys.exit('### data/b722_repair_controls.json IS NOT WRITTEN -- THE CONTROLS FIRST; NOTHING WRITTEN')
    nw = [c for c in ctl['cases'] if not c.get('as_wanted')]
    L = ['%s -- COMPONENT 1, (R332)(3): THE FIVE REPAIRS (STANDING CLAUSES v3 ROWS (56)-(60)) AND THE NEXT LINE`S, WITH THEIR DIFFS (%s)' % (ACT, utc()), '',
         '### rows are repairs: the row | what is repaired | its objects and its control. The controls: relay data/b722_repair_controls.txt (%d cases,' % len(ctl['cases']),
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


def _full_sentence(l, at):
    """the whole sentence about a hit (the pilot's _sent bounds, uncut: the pilot's bank prints 240 characters)."""
    a = max(l.rfind('. ', 0, at), l.rfind('; ', 0, at))
    a = 0 if a < 0 else a + 2
    b = min([p for p in (l.find('. ', at), l.find('; ', at)) if p >= 0] or [len(l)])
    return l[a:b + 1].strip()


HEADS_DRAFT = 'b714_heads_draft.txt'
LINT_BANK = 'b714_pilot.txt'
# ### (R332)(5)(ii): the six lint hits' rows in the pilot's (P2), by line (data/b714_pilot.txt :70, :72, :75, :78, :83, :86)
LINT_ROWS = (70, 72, 75, 78, 83, 86)
LINT_ROW = re.compile(r'^    :(\d+) +(STEM|FRONTDOOR) +\| (.+?) +\| FOR THE AUTHOR \| ')


def _lint_hits():
    """the six FOR THE AUTHOR hits of b714's pilot (P2), each (bank line, file, paper line, kind, hit, the whole sentence at PLACE-papers HEAD),
    the file read from the section head above the row; the sentence the paper's own at HEAD, around the hit, uncut (_full_sentence)."""
    rows = rdn(LINT_BANK).split(NL)
    out = []
    for n in LINT_ROWS:
        m = LINT_ROW.match(rows[n - 1]) if len(rows) >= n else None
        if not m:
            sys.exit('### data/%s :%d IS NOT A FOR THE AUTHOR ROW -- NOTHING PRINTED' % (LINT_BANK, n))
        f_ = next((re.match(r'^  ### (day1/\S+): hits', rows[j]).group(1) for j in range(n - 1, -1, -1) if re.match(r'^  ### (day1/\S+): hits', rows[j])), None)
        line, hit = int(m.group(1)), m.group(3).strip()
        text = (_show(PP, 'HEAD', f_) or '').split(NL)
        l = text[line - 1] if len(text) >= line else ''
        at = l.find(hit)
        out.append((n, f_, line, m.group(2), hit, _full_sentence(l, at) if at >= 0 else '### THE HIT NOT ON THE LINE AT HEAD: ' + l[:200]))
    return out


def rootprompt(*a):
    """[10], the root's prompt, put once ((R332)(8)), carrying (R332)(5)(i)-(ii) for the author's word, applied at b722: I. sections II and III of
    the heads draft (relay data/b714_heads_draft.txt), printed in full, and the question of inline footings or a companion correspondence;
    II. the six lint hits of b714's pilot (P2), each with its file, line and sentence. PRINTS ONLY: the prompt's text is banked by the answers
    route from the transcript; no bank here."""
    hd = rdn(HEADS_DRAFT).split(NL)
    i2 = next((i for i, l in enumerate(hd) if l.startswith('## II. ')), None)
    i3 = next((i for i, l in enumerate(hd) if l.startswith('## III. ')), None)
    end = next((i for i, l in enumerate(hd) if l.startswith('### ### **')), len(hd))
    if i2 is None or i3 is None:
        sys.exit('### data/%s CARRIES NO SECTION II OR III -- NOTHING PRINTED' % HEADS_DRAFT)
    hits = _lint_hits()
    L = ['THE ROOT`S PROMPT (b722, put once; (R332)(5)(i)-(ii), the word applied at b722; nothing written to main without it)', '',
         'I. THE HEADS DRAFT, SECTIONS II AND III IN FULL (relay data/%s :%d-:%d, Silence_of_Foundations.md :15 at a86c9429):' % (HEADS_DRAFT, i2 + 1, end), '']
    L += hd[i2:end]
    L += ['', '  THE QUESTION: the footings inline, in brackets after each sentence as section II prints them, or a companion correspondence',
          '  (the paragraph as it stands, its footings in a table beside it)?', '',
          'II. THE SIX LINT HITS FOR THE AUTHOR (relay data/%s (P2)), each with its file, line and sentence (the sentence read at PLACE-papers HEAD):' % LINT_BANK, '']
    for k, (n, f_, line, kind, hit, sent) in enumerate(hits, 1):
        L += ['  (%d) %s :%d  %s `%s`  (the pilot`s row :%d)' % (k, f_, line, kind, hit, n), '      ' + sent]
    L += ['', '### HEADS DRAFT SECTIONS 2 (II, III) ; LINT HITS %d ; the word is banked in data/b722_author_answers.txt and applied at b722' % len(hits)]
    print(NL.join(L))


# ================================================================================ COMPONENT 5, (R332)(7): THE CHAIN'S CENSUS ROWS
_SK, _LV, _EF, _FJ = 'D:/SIDE-kernel', 'D:/SIDE-lv-conservation', 'D:/SIDE-explicit-formula', 'D:/SIDE-faces-join'
# ### (pilot line, name, repo, pin, path, line, kind, axioms) -- the 24 of data/b721_pilot.txt (P3) :99-:122, the pilot's NO HOMEBREW ROW names first
# ### ((R332)(7)); axioms: ('probe', bank, first line, last line) a b554-form probe bank whose head must name the pin and read no DIFF,
# ### ('cell', bank, line) a print at the pin by its bank's own record, or ('none', why).
CHAIN = [
    (120, 'SIDEExplicitFormula.B321.rh_strip_imp_rh_holds', _EF, '38e2734', 'SIDEExplicitFormula/Seam.lean', 84, 'decl', ('cell', 'b704_probe_out_zeta.txt', 2466)),
    (99, 'techne_kernel.ExhaustiveCatalogue.covers_all', _SK, 'v1.2', 'Kernel/Layer1.lean', 23, 'field', ('none', 'no banked print of the field or its structure at v1.2')),
    (100, 'techne_kernel.SIDE_exclusion', _SK, 'v1.2', 'Kernel/Layer1.lean', 30, 'decl', ('none', 'no banked print at v1.2')),
    (103, 'ProductFormula.conservation_of_spectra', _SK, 'v1.2', 'Kernel/ProductFormula_Rat.lean', 72, 'decl', ('probe', 'b554_probe_k3.txt', 7, 7)),
    (104, 'SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin', _LV, 'v0.2.0', 'SIDELvConservation/T1_MellinFactorization.lean', 36, 'decl', ('probe', 'b554_probe_l3.txt', 8, 10)),
    (105, 'SIDELvConservation.T2b_mellin_exhaustion', _LV, 'v0.2.0', 'SIDELvConservation/T2_SDarkness.lean', 51, 'decl', ('probe', 'b554_probe_l4.txt', 8, 8)),
    (107, 'techne_kernel_voice2.symmetries_agree_iff', _SK, 'v1.2', 'Kernel/Voice2.lean', 52, 'decl', ('none', 'no banked print at v1.2')),
    (108, 'techne_kernel_voice3.reflect_fixed_iff', _SK, 'v1.2', 'Kernel/Voice3.lean', 20, 'decl', ('none', 'no banked print at v1.2')),
    (110, 'CartanBridge.formation_n_3_eq_two', _SK, 'v1.2', 'Bridge/CartanBBridge.lean', 220, 'decl', ('probe', 'b554_probe_k5.txt', 7, 7)),
    (111, 'CartanBridge.output_stage_card', _SK, 'v1.2', 'Bridge/CartanBBridge.lean', 79, 'decl', ('none', 'no banked print at v1.2')),
    (112, 'SIDELvConservation.h1_complete_at_Phi', _LV, 'c80bdc2', 'SIDELvConservation/CouplingsAtPhi.lean', 418, 'decl', ('probe', 'b554_probe_l7.txt', 46, 46)),
    (113, 'SIDELvConservation.RegisterPentagon.goalState_of_h1_h2', _LV, '2d86182', 'SIDELvConservation/RegisterPentagon.lean', 202, 'decl', ('probe', 'b554_probe_l8.txt', 9, 9)),
    (114, 'SIDELvConservation.PartialPositivity.blTerm_nonneg_of_onLine', _LV, '6efa9e5', 'SIDELvConservation/PartialPositivity.lean', 50, 'decl', ('probe', 'b554_probe_l2c.txt', 9, 11)),
    (116, 'SIDELvConservation.exists_norm_completedLFunction_le_exp', _LV, '1767bd6', 'SIDELvConservation/DirichletC7Order.lean', 771, 'decl', ('probe', 'b554_probe_l6.txt', 41, 41)),
    (117, 'SIDELvConservation.C7_finite_type_false', _LV, 'bc4751e', 'SIDELvConservation/C7FiniteTypeFalse.lean', 68, 'decl', ('probe', 'b554_probe_l9.txt', 7, 7)),
    (101, 'SIDELvConservation.T3.T3_perClass_to_combinations', _LV, 'v0.2.0', 'SIDELvConservation/T3_StepNineBridge.lean', 92, 'decl', ('none', 'no banked print at v0.2.0; at v0.11.0 relay data/b557_prints_root.txt :15 reads [propext, sorryAx, Classical.choice, Quot.sound]')),
    (102, 'SIDELvConservation.T3.T3doubleprime_general_commutation_fails', _LV, 'v0.2.0', 'SIDELvConservation/T3_StepNineBridge.lean', 137, 'decl', ('probe', 'b554_probe_l5.txt', 9, 11)),
    (106, 'techne_kernel_voice1.balance_theorem', _SK, 'v1.2', 'Kernel/Voice1.lean', 22, 'decl', ('none', 'no banked print at v1.2')),
    (109, 'SIDEKernel.formation', _SK, 'v1.2', 'Kernel/Core.lean', 53, 'decl', ('probe', 'b554_probe_k4.txt', 7, 7)),
    (115, 'SIDELvConservation.PartialPositivity.partialPositivity_finiteRange', _LV, '6efa9e5', 'SIDELvConservation/PartialPositivity.lean', 105, 'decl', ('probe', 'b554_probe_l2.txt', 12, 14)),
    (118, 'SIDEExplicitFormula.B321.h2_sign', _EF, '38e2734', 'SIDEExplicitFormula/H2Sign.lean', 29, 'decl', ('cell', 'b704_probe_out_zeta.txt', 51)),
    (119, 'SIDEExplicitFormula.B321.h2_sign_iff_rh', _EF, '38e2734', 'SIDEExplicitFormula/Seam.lean', 101, 'decl', ('cell', 'b704_probe_out_zeta.txt', 71)),
    (121, 'RiemannHypothesis', None, 'de5ce8a9', 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', 185, 'mathlib', ('cell', 'b704_probe_out_zeta.txt', 7)),
    (122, 'faces_join', _FJ, '11a472b', 'FacesJoin.lean', 29, 'decl', ('cell', 'b712_join_grade.txt', 16)),
]
_NOHB = (120, 99, 100, 103, 104, 105, 107, 108, 110, 111, 112, 113, 114, 116, 117)   # ### (P3)'s NO HOMEBREW ROW lines
_KW = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|abbrev|structure|class|instance|axiom|opaque)\b')


def _chain_read(repo, pin, path, line, kind):
    """(sha, statement, kind, span end, sorry lines) of the declaration at `path`:`line` at `pin`, from git show; None when unread."""
    sha = (gitc(repo, 'rev-parse', '--short=7', pin + '^{commit}') or '').strip()
    src = gitc(repo, 'show', '%s:%s' % (pin, path))
    if not src:
        return None
    ls = src.replace('\r', '').split(NL)
    i = line - 1
    if kind == 'field':
        ind = len(ls[i]) - len(ls[i].lstrip())
        j = i + 1
        while j < len(ls) and ls[j].strip() and len(ls[j]) - len(ls[j].lstrip()) > ind:
            j += 1
        return sha, NL.join(ls[i:j]), 'field', j, []
    m = _KW.match(ls[i])
    k = m.group(1) if m else '?'
    j = i
    while j < len(ls) and not re.search(r':=|\bwhere\b', ls[j]):
        j += 1
    st = re.split(r':=|\bwhere\b', NL.join(ls[i:j + 1]), 1)[0].rstrip()
    if k in ('def', 'abbrev'):
        e = j + 1
        while e < len(ls) and ls[e].strip() and not _KW.match(ls[e]) and not ls[e].lstrip().startswith('/-'):
            e += 1
        st = NL.join(ls[i:e]).rstrip()
    e = line
    while e < len(ls) and not _KW.match(ls[e]) and not re.match(r'^\s*(end|namespace|section)\b', ls[e]):
        e += 1
    sl = [line + n for n, t in enumerate(ls[line - 1:e]) if re.search(r'(?<![\w`])sorry\b', t.split('--')[0])]
    return sha, st, k, e, sl


def gitc(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, encoding='utf-8', errors='replace')
    return r.stdout if r.returncode == 0 else None


def _chain_axioms(ax, sha):
    """(text, source) of a row's axioms: a probe bank counts only when its head names the pin's commit and reads no DIFF."""
    if ax[0] == 'none':
        return 'axioms not read at this pin', ax[1]
    t = (rdn(ax[1]) or '').split(NL)
    if ax[0] == 'probe':
        head = t[:4]
        if not head or sha not in head[0] or any('DIFF' in h for h in head[1:3]):
            return 'axioms not read at this pin', 'relay data/%s :1-:3 -- %s' % (ax[1], 'the head names another commit' if not head or sha not in head[0]
                                                                                   else 'the pin`s file printed over a checkout whose file or imports DIFF')
        return ' '.join(' '.join(t[ax[2] - 1:ax[3]]).split()), 'relay data/%s :%d%s, its head naming %s with no DIFF' % (
            ax[1], ax[2], '-:%d' % ax[3] if ax[3] != ax[2] else '', sha)
    return ' '.join(t[ax[2] - 1].split()), 'relay data/%s :%d' % (ax[1], ax[2])


def chainrows(*a):
    """(R332)(7)'s evidence for the census v0.8.2's rows: each of the 24 declarations of (P3) read at its pin, its statement, its grade under
    the shared E0 rule (tools/e0_rule.py grade), the sorry lines of its span and its axioms where a banked print at the pin reaches them.
    Banked as data/b722_chain_rows.txt; the census rows are written from it by the Edit tool."""
    import e0_rule as E0
    L = ['b722 -- COMPONENT 5, (R332)(7): THE CHAIN`S 24 DECLARATIONS READ AT THEIR PINS, GRADED AND THEIR AXIOMS READ (%s)' % utc(), '',
         '### rows are declarations, in the order (R332)(7) takes them (the pilot`s NO HOMEBREW ROW names first, rh_strip_imp_rh_holds among them, then',
         '### the rest): the pilot`s line (relay data/b721_pilot.txt), the name, the repository, pin and place, the statement at the pin (git show',
         '### <pin>:<path>, from its line to its `:=`; a def whole), its kind, the E0 rule`s grade and why (tools/e0_rule.py grade, from the statement',
         '### alone), the span`s sorry lines and the axioms. Written by tools/b722_record.py chainrows.', '']
    grades = {}
    for pl, name, repo, pin, path, line, kind, ax in CHAIN:
        if kind == 'mathlib':
            t = (rdn('b704_probe_out_zeta.txt') or '').split(NL)
            sha, st, k, e, sl = 'de5ce8a', NL.join(t[3:5]), 'def', None, []
            where = 'Mathlib de5ce8a9 (SIDE-explicit-formula v0.37 = 38e2734`s lake-manifest.json :10) %s :%d -- the elaborated statement of relay data/b704_probe_out_zeta.txt :4-:5 (run 39721668586 at v0.37; no Mathlib clone at the pin)' % (path, line)
        else:
            got = _chain_read(repo, pin, path, line, kind)
            if got is None:
                L += ['--- (P3) :%d  %s  ### NOT READ AT %s %s:%d' % (pl, name, pin, path, line), '']
                continue
            sha, st, k, e, sl = got
            where = '%s %s = %s : %s :%d' % (os.path.basename(repo), pin, sha, path, line)
        if k == 'field':
            g, why = 'NOT GRADED', 'a structure field: the E0 rule grades a declaration`s statement, and a field is no declaration'
        else:
            short = name.split('.')[-1]
            mm = re.search(r'\b' + re.escape(short) + r'\b', st)
            try:
                g, why, _b = E0.grade(st[mm.end():] if mm else st, 'def' if k in ('def', 'abbrev') else 'theorem')
            except Exception as ex:   # noqa: BLE001
                g, why = 'UNCLASSED', ' '.join(str(ex).split())[:300]
        grades[g] = grades.get(g, 0) + 1
        axt, axs = _chain_axioms(ax, sha if kind != 'mathlib' else '')
        L += ['--- (P3) :%d  %s%s' % (pl, name, '  (NO HOMEBREW ROW)' if pl in _NOHB else ''), '    at   : ' + where]
        L += ['    stmt : ' + s for s in st.split(NL)]
        L += ['    kind %s ; GRADE %s ; %s' % (k, g, why), '    sorry in the span%s : %s' % (' :%d-:%d' % (line, e) if e else '', sl or 'NONE'),
              '    axioms : %s ; %s' % (axt, axs), '']
    L.append('### ### **DECLARATIONS %d ; GRADES %s ; AXIOMS READ AT THE PIN %d ; NOT READ AT THIS PIN %d ; SORRY IN A SPAN %d.**' % (
        len(CHAIN), ', '.join('%s %d' % kv for kv in sorted(grades.items())),
        sum(1 for l in L if l.startswith('    axioms : ') and 'not read at this pin' not in l),
        sum(1 for l in L if l.startswith('    axioms : axioms not read at this pin')),
        sum(1 for l in L if l.startswith('    sorry in the span') and not l.endswith('NONE'))))
    put_txt('%s_chain_rows.txt' % ACT, L)
    print('bank data/%s_chain_rows.txt' % ACT)
    print(L[-1])


_C81 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md'
_C82 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'


def edition82(*a):
    """(R332)(7): the census's next edition, v0.8.2, begun as v0.8.1's bytes at PLACE-papers main (git show main:<v0.8.1>), written once beside
    it; v0.8.1 unedited. Refuses when v0.8.2 exists. The rows and the version lines are then written by the Edit tool."""
    dst = os.path.join(PP, *_C82.split('/'))
    if os.path.exists(dst):
        sys.exit('### %s EXISTS -- NOT WRITTEN' % _C82)
    r = subprocess.run(['git', '-C', PP, 'show', 'main:' + _C81], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        sys.exit('### main:%s NOT READ -- NOT WRITTEN' % _C81)
    with open(dst, 'xb') as f:
        f.write(r.stdout)
    print('wrote %s : %d bytes, sha256 %s ; main:%s sha256 %s' % (_C82, len(r.stdout), hashlib.sha256(open(dst, 'rb').read()).hexdigest(),
                                                               _C81, hashlib.sha256(r.stdout).hexdigest()))


def censusdiff(*a):
    """(R332)(7)'s diff banked: v0.8.1 at main against v0.8.2's working copy, unified, as data/b722_census_diff.txt."""
    old = subprocess.run(['git', '-C', PP, 'show', 'main:' + _C81], capture_output=True).stdout.decode('utf-8').replace('\r', '').split(NL)
    new = open(os.path.join(PP, *_C82.split('/')), encoding='utf-8').read().replace('\r', '').split(NL)
    import difflib
    d = list(difflib.unified_diff(old, new, 'main:' + _C81, _C82 + ' (working copy)', lineterm='', n=1))
    L = ['b722 -- COMPONENT 5, (R332)(7): THE CENSUS v0.8.2 AGAINST v0.8.1, UNIFIED (%s)' % utc(), '',
         '### v0.8.1 read from PLACE-papers main, v0.8.2 its working copy; v0.8.2 begun as v0.8.1`s bytes (tools/b722_record.py edition82), its',
         '### additions written by the Edit tool. Written by tools/b722_record.py censusdiff.', ''] + d + [
        '', '### ### **LINES %d -> %d ; HUNKS %d ; ADDED %d ; REMOVED %d.**' % (len(old), len(new), sum(1 for l in d if l.startswith('@@')),
                                                                         sum(1 for l in d if l.startswith('+') and not l.startswith('+++')),
                                                                         sum(1 for l in d if l.startswith('-') and not l.startswith('---')))]
    put_txt('%s_census_diff.txt' % ACT, L)
    print('bank data/%s_census_diff.txt' % ACT)
    print(L[-1])


def censusscreen(*a):
    """(R332)(7): b698's landing screens (the scanner, no-disclosure, backtick parity, unread figures, outside names, stems) over the lines
    v0.8.2 adds to v0.8.1, dry: the scan file goes to the session scratchpad, nothing to data/. PRINTS ONLY."""
    old = subprocess.run(['git', '-C', PP, 'show', 'main:' + _C81], capture_output=True).stdout.decode('utf-8').replace('\r', '').split(NL)
    new = open(os.path.join(PP, *_C82.split('/')), encoding='utf-8').read().replace('\r', '').split(NL)
    import difflib
    add = [l[1:] for l in difflib.unified_diff(old, new, lineterm='', n=0) if l.startswith('+') and not l.startswith('+++')]
    print('### the screens over the %d lines v0.8.2 adds:' % len(add))
    cells, fired = R.screens([(_C82, 'v0.8.2', NL.join(add) + NL)], 'census82', True)
    print('### table cells %d (the rows table, expected) ; FIRED %s' % (len(cells), fired))


# ### stage one (step zero): b721's Component routes over its own objects pruned (data/b722_prune_record.txt); this act's are added by the Edit tool
ROUTES = dict(chainrows=chainrows, edition82=edition82, censusdiff=censusdiff, censusscreen=censusscreen,rootprompt=rootprompt,verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              ksyms=ksyms, defs=defs, figures=figures, runner=runner,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry, linecheck=linecheck,
              step=step, c1=c1, repairctl=repairctl12, toolrepairs12=toolrepairs12, facerows=facerows, portedit=portedit, portdispatch=portdispatch, portrun=portrun, regpos=regpos, joingrade=joingrade, jointag=jointag,
              scores=scores, findings=findings, trail=trail, drycheck=drycheck, components=components, mbank=mbank, guard=guard,
              scorercheck=scorercheck, armnames=armnames, facesdiff=facesdiff, recutadd=recutadd, closeorder=closeorder,
              repaircontrols=repaircontrols, toolrepairs=toolrepairs13, counter=counter)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b722_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
