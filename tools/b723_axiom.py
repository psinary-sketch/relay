# -*- coding: utf-8 -*-
"""b723_axiom.py -- (R333)(7): WAVE 1'S AXIOM STEP, STOPPABLE. Written whole at b723 by the Write tool.

The step "Axioms of the named terminals" repaired on each rebuild-b721 branch by the route b722's (R332)(10) bank priced
(data/b722_axiom_diag.txt), one dispatch per kernel read by its run id (six at most), the host's free memory read before each push,
dispatch and read under the 2,560 MB hold (b718's routes: tools/b718_pin.py hold_or_exit, dispatch, read; rows in
data/b723_axiom_rows.json; artifacts in %TEMP%/b723_axiom_artifacts, outside the relay). The branch commit is git plumbing on the
branch's tip (the pin), its author and committer the seat's neutral identity, no identifier of the author in it. No kernel main or tag
touched; no lean or lake process on this host.

THE ROUTES AS PRICED, BY CLASS: TARGETS ABSENT AT THE PIN (SIDE-archimedean, SIDE-spinor, SIDE-rcurve) -- one commit adding
print_targets.txt, one push, one dispatch of main's build-module.yml at the branch's sha. b722's price leaves to the author's word: the
six SIDESpinorLeg names not declared at SIDE-spinor's pin (dropped or kept); SIDE-frobenius's target list (the kernel never carried one);
SIDE-kernel's changed workflow, each line. The author's word (6) (data/b723_author_words_preseal.txt (6)) routes them: (a) SIDE-spinor's
six SIDESpinorLeg names dropped (added past the pin, REGISTRY's 1.2-C exception), the nine the pin declares printed; (b) SIDE-frobenius's
list the declarations behind the README sentences data/b721_frozen_line.txt grades STATED for it, each checked declared at the pin, its
branch's own workflow running on the push (b721's two lines), so the push is its run; (c) SIDE-kernel's workflow on rebuild-b721 changed
in three places and nothing else (a push trigger, the axiom step's imports cut to the pin's modules, its #print list cut to terminals
declared at the pin), the diff printed before any commit, and the step halting to ask if it touches anything else (`kdraft`).
SIDE-lv-conservation's step ran clean at b721 (data/b721_rebuild.txt :17-:24); its route is `lv`, the sorry's statement and position.

  plan                 per kernel: the pin, the branch's local and origin tips, b722's class, the route, the print_targets.txt drafted (main's
                       blob verbatim) and each name re-read as declared at the pin by `git grep`; nothing written
  commit <kernel>      one plumbing commit on rebuild-b721 (its tip the pin) adding print_targets.txt; one ref moved (old value checked)
  push <kernel>        free memory read; the branch pushed; ls-remote read; one row
  dispatch <kernel>    b718's dispatch (main's build-module.yml, -f ref=<the branch's sha>, -f target=<the pin's target>); one row
  read <kernel> <id>   b718's read route over b723's rows; the axioms lines printed whole
  push_run <kernel>    SIDE-frobenius: the push is the run's trigger (its branch's workflow runs on push); the run found by branch, event
                       and head sha, rowed as a dispatch via push
  kdraft               SIDE-kernel: the three-place diff formed in memory and printed, each kept import and name checked at the pin, and the
                       file's own refusal step read under the TARGET a push carries; HALTED (one row) if the three places cannot build alone
  lv                   SIDE-lv-conservation at its pin: T3_perClass_to_combinations's statement and the sorry's position; nothing written
  bank                 data/b723_axiom.txt from the rows
"""
import io
import json
import os
import re
import sys
import time

NL = chr(10)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b721_rebuild as R   # noqa: E402  ### the pins, full(), target_at_pin() (b721's; importing it points b718's routes at b721's rows)
import b718_pin as P       # noqa: E402

BRANCH = 'rebuild-b721'
ROWS = os.path.join(D_, 'b723_axiom_rows.json')
OUT = os.path.join(D_, 'b723_axiom.txt')
P.ROWS = ROWS                                      # ### repointed after R's import: b723's rows, never b721's
P.DL = os.path.join(os.environ.get('TEMP', ROOT), 'b723_axiom_artifacts')
P.BRANCH = BRANCH
P.MAX_DISPATCH = 6
P.target_of = R.target_at_pin
SEAT = ['-c', 'user.name=b723 axiom seat', '-c', 'user.email=b723-axiom@relay.invalid']
DIAG = os.path.join(D_, 'b722_axiom_diag.json')
READY = ('SIDE-archimedean', 'SIDE-rcurve', 'SIDE-spinor', 'SIDE-frobenius')
VERBATIM = ('SIDE-archimedean', 'SIDE-rcurve')      # ### main's blob verbatim; spinor main's names less the dropped; frobenius from the bank
DROP_REASON = 'added in the two commits past the pin (REGISTRY`s 1.2-C exception); not declared at the pin, cannot be printed there'
FRO_FIX = '6b06215745'                              # ### b721's rebranch commit (the two lines), the frobenius branch's tip
WORD = {'SIDE-kernel': 'the changed workflow in three places alone (the author`s word (6)(c)); see the kdraft row'}
WF_PATH = '.github/workflows/build-module.yml'
LV = ('SIDE-lv-conservation', 'T3_perClass_to_combinations')


def diag():
    d = json.load(io.open(DIAG, encoding='utf-8'))
    rows = d if isinstance(d, list) else d.get('rows', d.get('kernels', []))
    return dict((x['kernel'], x) for x in rows)


def declared_at_pin(k, names):
    repo, f = 'D:/' + k, R.full(k)
    out = {}
    for n in names:
        short = n.split('.')[-1]
        c, o, e = P.g(repo, 'grep', '-n', '-E', r'(theorem|lemma|def|abbrev|structure|inductive|class|instance)[[:space:]]+([^[:space:]]+\.)?%s\b'
                      % re.escape(short), f, '--', '*.lean')
        hits = [l for l in o.split(NL) if l.strip()]
        out[n] = ':'.join(hits[0].split(':', 3)[1:3]) if hits else None
    return out


def qualified_at_pin(k, rev, short, want=None):
    """### the declaration of `short` in the .lean files at rev (git grep), qualified by the namespaces open at its line (namespace X /
    ### end X read down the file); None where no declaration is found. A name ending in a prime is matched to its end."""
    ### every hit read (a short name may be declared in several namespaces), a dotted declaration name (theorem Ns.short) taken whole;
    ### with `want` the hit whose full name equals it or ends with it is returned, else the first.
    repo = 'D:/' + k
    pat = (r'^(private |protected |noncomputable )*(theorem|lemma|def|abbrev|structure|inductive|class|instance)[[:space:]]+'
           r'([^[:space:]]+\.)?%s([[:space:]]|:|$)' % re.escape(short).replace("\\'", "'"))
    hits = [l for l in P.g(repo, 'grep', '-n', '-E', pat, rev, '--', '*.lean')[1].split(NL) if l.strip()]
    if not hits:
        return None, None
    cands = []
    for h in hits:
        _r, path, ln, text = h.split(':', 3)
        L = (P.show(repo, rev, path) or '').split(NL)
        st = []
        for l in L[:int(ln) - 1]:
            m = re.match(r'^namespace\s+(\S+)', l)
            if m:
                st.append(m.group(1))
            m = re.match(r'^end\s+(\S+)', l)
            if m and st and st[-1] == m.group(1):
                st.pop()
        dn = re.match(r'^(?:(?:private|protected|noncomputable) )*\S+\s+(\S+?)(?=[\s:]|$)', text).group(1)
        cands.append(('.'.join(st + [dn]), '%s:%s' % (path, ln)))
    if want:
        for q, at in cands:
            if q == want or q.endswith('.' + want):
                return q, at
    return cands[0] if not want else (' | '.join(q for q, _a in cands), None)


def frozen_names():
    """### (6)(b): the declarations named under the README sentences data/b721_frozen_line.txt grades STATED for SIDE-frobenius -- the
    ### "`name` at the pin :N" lines beneath a STATED row in its block, read in order, each once."""
    L = io.open(os.path.join(D_, 'b721_frozen_line.txt'), encoding='utf-8').read().split(NL)
    i = next(m for m, l in enumerate(L) if l.startswith('## SIDE-frobenius'))
    j = next((m for m in range(i + 1, len(L)) if L[m].startswith('## ')), len(L))
    grade, out = None, []
    for m in range(i, j):
        g = re.match(r'^\s{4}\d+\.\d+\s+(STATED|NO CLAIM|OUTSIDE|SCOPE|EXCEEDS)\s*\|', L[m])
        if g:
            grade = g.group(1)
            continue
        n = re.match(r'^\s+`([A-Za-z0-9_\']+)` at the pin :(\d+)', L[m])
        if n and grade == 'STATED' and n.group(1) not in [x[0] for x in out]:
            out.append((n.group(1), m + 1))
    return out


def drafted(k):
    """### the print_targets.txt each READY kernel's commit carries: (text, names, dropped [(name, reason)], source line)."""
    if k in VERBATIM:
        t = P.show('D:/' + k, 'main', 'print_targets.txt') or ''
        return t, [n.strip() for n in t.split(NL) if n.strip()], [], 'main`s blob verbatim'
    if k == 'SIDE-spinor':
        names = [n.strip() for n in (P.show('D:/' + k, 'main', 'print_targets.txt') or '').split(NL) if n.strip()]
        dec = declared_at_pin(k, names)
        keep = [n for n in names if dec[n]]
        drop = [n for n in names if not dec[n]]
        assert len(drop) == 6 and all(n.startswith('SIDESpinorLeg.') for n in drop), drop
        return NL.join(keep) + NL, keep, [(n, DROP_REASON) for n in drop], 'main`s names, the six SIDESpinorLeg dropped (the author`s word (6)(a))'
    if k == 'SIDE-frobenius':
        names = []
        for short, ln in frozen_names():
            q, at = qualified_at_pin(k, R.full(k), short)
            assert q, '%s not declared at the pin' % short
            names.append(q)
        return NL.join(names) + NL, names, [], 'the STATED rows` declarations, data/b721_frozen_line.txt (the author`s word (6)(b))'
    raise SystemExit('## %s: no drafted list' % k)


def plan():
    print('### free memory %d MB (hold %d) ; branch %s ; rows %s' % (P.free_mb(), P.HOLD_MB, BRANCH, os.path.relpath(ROWS, ROOT)))
    dg = diag()
    for k, tag, p in R.PINS:
        repo = 'D:/' + k
        f = R.full(k)
        tip = P.gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH)
        rem = P.g(repo, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)[1].strip()
        cls = (dg.get(k) or {}).get('class') or (dg.get(k) or {}).get('cls')
        route = 'lv (the step ran clean at b721)' if k == LV[0] else ('READY: commit, push, dispatch, read' if k in READY else
                                                                      'READY ON THE AUTHOR`S WORD: ' + WORD[k])
        print('## %-21s pin %s = %s ; %s local %s, origin %s ; b722 class %s ; ROUTE %s' % (k, tag, f[:12], BRANCH, tip[:12], rem[:12],
                                                                                          cls, route))
        if k in READY:
            t, names, drop, src = drafted(k)
            dec = dict((n, qualified_at_pin(k, f, n.split('.')[-1], want=n)) for n in names)
            print('   print_targets.txt drafted: %s, %d bytes, %d names ; declared at the pin under that full name: %d of %d' % (
                src, len(t.encode('utf-8')), len(names), sum(1 for n in names if dec[n][0] == n), len(names)))
            for n in names:
                print('     %-48s %s' % (n, ('AT ' + dec[n][1]) if dec[n][0] == n else 'NOT AT THE PIN UNDER THIS NAME (%s)' % (dec[n],)))
            for n, why in drop:
                print('     %-48s DROPPED: %s' % (n, why))


def commit(k):
    if k not in READY:
        sys.exit('## %s: not READY (%s); nothing written' % (k, WORD.get(k, 'the lv route')))
    if [r for r in P.rows_load() if r.get('kind') == 'commit' and r['kernel'] == k]:
        sys.exit('## %s: committed already at b723; nothing written' % k)
    repo = 'D:/' + k
    f = R.full(k)
    tip = P.gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH)
    base_ok = tip == f or (k == 'SIDE-frobenius' and tip.startswith(FRO_FIX) and P.gs(repo, 'rev-parse', tip + '^^') == f)
    if not base_ok:
        sys.exit('## %s: the tip %s is not the pin %s (nor frobenius`s b721 two-line commit over it); nothing written' % (k, tip[:12], f[:12]))
    if P.g(repo, 'ls-tree', tip, 'print_targets.txt')[1].strip():
        sys.exit('## %s: the tip carries print_targets.txt; nothing written' % k)
    t, names, drop, src = drafted(k)
    for n in names:                                    # ### each name declared at the pin under its full name, before any write
        q = qualified_at_pin(k, f, n.split('.')[-1], want=n)[0]
        if q != n:
            sys.exit('## %s: %s not declared at the pin under that name (%s); nothing written' % (k, n, q))
    b = P.blob(repo, t)
    if k in VERBATIM:
        mb = P.gs(repo, 'rev-parse', 'main:print_targets.txt')
        assert b == mb, (b, mb)
    rows = [l for l in P.gs(repo, 'ls-tree', tip).split(NL) if l.strip()] + ['100644 blob %s\tprint_targets.txt' % b]
    rows.sort(key=lambda l: l.split('\t', 1)[1] + ('/' if ' tree ' in l else ''))
    c, tree, e = P.g(repo, 'mktree', inp=(NL.join(rows) + NL).encode('utf-8'))
    assert c == 0, e
    msg = ('b723 under (R333)(7): the axiom step`s target list print_targets.txt over %s (the pin %s), %d names, %s; nothing else' % (
        tip[:12], f[:12], len(names), src))
    c, cm, e = P.g(repo, *(SEAT + ['commit-tree', tree.strip(), '-p', tip, '-m', msg]))
    assert c == 0, e
    cm = cm.strip()
    c, _o, e = P.g(repo, 'update-ref', 'refs/heads/' + BRANCH, cm, tip)
    assert c == 0, e
    print('## %s : %s at %s, parent %s, adding print_targets.txt (blob %s, %d names: %s) and nothing else; author and committer %s'
          % (k, BRANCH, cm[:12], tip[:12], b[:12], len(names), src, P.gs(repo, 'log', '-1', '--format=%an <%ae> / %cn <%ce>', cm)))
    print(P.g(repo, 'diff', '--stat', tip, cm)[1].rstrip())
    P.rows_add({'kind': 'commit', 'kernel': k, 'sha': cm, 'parent': tip, 'blob': b, 'names': names, 'dropped': drop, 'source': src,
                'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})


def push(k):
    repo = 'D:/' + k
    cm = [r for r in P.rows_load() if r.get('kind') == 'commit' and r['kernel'] == k]
    if not cm or [r for r in P.rows_load() if r.get('kind') == 'push' and r['kernel'] == k]:
        sys.exit('## %s: no commit row, or pushed already at b723; nothing pushed' % k)
    tip = P.gs(repo, 'rev-parse', 'refs/heads/' + BRANCH)
    if tip != cm[-1]['sha']:
        sys.exit('## %s: the tip is not b723`s commit; nothing pushed' % k)
    fm = P.hold_or_exit('the push of ' + k)
    print('### free memory %d MB (hold %d) ; pushing %s %s at %s (fast-forward from its parent %s)' % (fm, P.HOLD_MB, k, BRANCH, tip[:12],
                                                                                                  cm[-1]['parent'][:12]))
    c, o, e = P.g(repo, 'push', 'origin', BRANCH)
    print('   git push origin %s: exit %d %s' % (BRANCH, c, (o + e).strip().replace(NL, ' / ')[:300]))
    if c != 0:
        sys.exit('push refused; no row')
    remote = P.g(repo, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)[1].strip()
    print('   ls-remote origin %s: %s ; equal to the tip %s' % (BRANCH, remote[:12], remote.startswith(tip)))
    P.rows_add({'kind': 'push', 'kernel': k, 'sha': tip, 'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'free_mb': fm,
                'remote_equal': remote.startswith(tip)})


def dispatch(k):
    if not [r for r in P.rows_load() if r.get('kind') == 'push' and r['kernel'] == k]:
        sys.exit('## %s: not pushed at b723; nothing dispatched' % k)
    if k == 'SIDE-frobenius':
        sys.exit('## %s: no workflow on main; its branch`s workflow runs on the push -- use findrun; nothing dispatched' % k)
    P.dispatch(k)


def findrun(k):
    """### SIDE-frobenius: the run its push triggered, found by branch, event push and head sha (b721's push_run form), rowed as a dispatch
    ### via push; counted toward the six."""
    pu = [r for r in P.rows_load() if r.get('kind') == 'push' and r['kernel'] == k]
    done = [r for r in P.rows_load() if r.get('kind') == 'dispatch']
    if not pu or [r for r in done if r['kernel'] == k] or len(done) >= P.MAX_DISPATCH:
        sys.exit('## %s: not pushed, its run rowed already, or six reached; nothing rowed' % k)
    tip, t0 = pu[-1]['sha'], pu[-1]['at']
    rid = None
    for _i in range(24):
        c, o, e = P.gh('run', 'list', '-R', '%s/%s' % (P.OWNER, k), '--branch', BRANCH, '--event', 'push', '-L', '5',
                       '--json', 'databaseId,createdAt,status,headSha')
        new = [r for r in json.loads(o or '[]') if r['createdAt'] >= t0 and r['headSha'] == tip]
        if new:
            rid = new[-1]['databaseId']
            break
        time.sleep(5)
    print('   run id %s (event push, head %s, created at or after %s)' % (rid, tip[:12], t0))
    if rid:
        P.rows_add({'kind': 'dispatch', 'kernel': k, 'sha': tip, 'target': R.target_at_pin(k), 'at': t0, 'run': rid, 'free_mb': P.free_mb(),
                    'via': 'push'})


def kdraft():
    """### (6)(c): SIDE-kernel's workflow for rebuild-b721, main's build-module.yml changed in three places alone -- (1) a push trigger beside
    ### workflow_dispatch, (2) the axiom step's imports cut to the modules present at the pin, (3) its #print list cut to the terminals
    ### declared at the pin under the printed name -- formed in memory, the diff printed. Then the file's own refusal step read (bash on
    ### this host) under the TARGET a push carries: TARGET is `${{ inputs.target }}` and a push has no inputs. If the three places cannot
    ### build alone, HALTED: nothing committed, one row, the fourth line the author's to rule."""
    import difflib
    import subprocess
    k = 'SIDE-kernel'
    repo, f = 'D:/' + k, R.full(k)
    L = (P.show(repo, 'main', WF_PATH) or '').split(NL)
    pin_files = set(x for x in P.gs(repo, 'ls-tree', '-r', '--name-only', f).split(NL) if x.strip())
    M = list(L)
    assert M.count('on:') == 1
    M.insert(M.index('on:') + 1, '  push: { branches: [%s] }' % BRANCH)
    kept_i, cut_i, kept_n, cut_n = [], [], [], []
    out = []
    for l in M:
        mi = re.match(r'^ {10}import (\S+)$', l)
        mp = re.match(r'^ {10}#print axioms (\S+)$', l)
        if mi:
            (kept_i if mi.group(1).replace('.', '/') + '.lean' in pin_files else cut_i).append(mi.group(1))
            if mi.group(1).replace('.', '/') + '.lean' not in pin_files:
                continue
        if mp:
            n = mp.group(1)
            q, at = qualified_at_pin(k, f, n.split('.')[-1], want=n)
            ok = at is not None
            (kept_n if ok else cut_n).append((n, at if ok else q))
            if not ok:
                continue
        out.append(l)
    diff = [x for x in difflib.unified_diff(L, out, 'main:' + WF_PATH, BRANCH + ':' + WF_PATH, lineterm='', n=0)]
    places = set()
    for x in diff:
        if x.startswith(('---', '+++', '@@')):
            continue
        if x.startswith('+  push:'):
            places.add('trigger')
        elif re.match(r'^- {10}import ', x):
            places.add('imports')
        elif re.match(r'^- {10}#print axioms ', x):
            places.add('targets')
        else:
            places.add('OTHER: ' + x)
    print('### SIDE-kernel: main`s %s (%d lines) changed in memory for %s, the pin %s' % (WF_PATH, len(L), BRANCH, f[:12]))
    print('   imports kept %d, cut %d (%s) ; #print names kept %d, cut %d' % (len(kept_i), len(cut_i), ', '.join(cut_i), len(kept_n), len(cut_n)))
    for n, why in cut_n:
        print('     cut: %-58s %s' % (n, 'NOT DECLARED AT THE PIN' if why is None else 'declared as %s' % why))
    print('   THE DIFF (formed in memory, not committed): %d lines ; the places it touches: %s' % (len(diff), sorted(places)))
    for x in diff:
        print('     ' + x)
    i = L.index('      - name: Refuse a target outside the lake grammar')
    case = NL.join(l[10:] for l in L[i + 2:i + 5])
    p = subprocess.run(['bash', '-c', "TARGET=''%s%s%secho PASSED" % (NL, case, NL)], capture_output=True, text=True)
    ctl = subprocess.run(['bash', '-c', "TARGET='%s'%s%s%secho PASSED" % (R.target_at_pin(k), NL, case, NL)], capture_output=True, text=True)
    env_t = [l.strip() for l in L if l.strip().startswith('TARGET:')]
    print('   env %s ; the refusal step under the TARGET a push carries (empty): exit %d %s ; under the dispatch target %r (the control): '
          'exit %d %s' % (env_t, p.returncode, (p.stdout + p.stderr).strip(), R.target_at_pin(k), ctl.returncode, (ctl.stdout + ctl.stderr).strip()))
    other = [x for x in places if x.startswith('OTHER')]
    halt = bool(other) or (p.returncode != 0 and ctl.returncode == 0)
    why = ('the diff touches another place: %s' % other) if other else (
        'the three places alone cannot build: on a push inputs.target is empty and the file`s own refusal step exits %d before elan, the cache '
        'or lake; a fourth line (TARGET fixed, as b721`s frobenius second word) or a dispatch at the branch with its inputs (no push '
        'trigger) is the author`s to rule' % p.returncode) if halt else 'NOT HALTED'
    print('   %s' % (('HALTED: ' + why + '; nothing committed, pushed or run') if halt else why))
    keep = [r for r in P.rows_load() if not r.get('kind', '').startswith('kdraft')]
    if len(keep) != len(P.rows_load()):              # ### a draft, no kernel touched: the earlier draft row replaced
        io.open(ROWS + '.tmp', 'w', encoding='utf-8', newline='\n').write(json.dumps(keep, indent=1, ensure_ascii=False) + NL)
        os.replace(ROWS + '.tmp', ROWS)
        print('   the earlier kdraft row replaced')
    P.rows_add({'kind': 'kdraft_halt' if halt else 'kdraft_clear', 'kernel': k, 'diff': diff, 'places': sorted(places), 'imports_cut': cut_i,
                'names_kept': len(kept_n), 'names_cut': cut_n, 'empty_exit': p.returncode, 'empty_out': (p.stdout + p.stderr).strip(),
                'control_exit': ctl.returncode, 'why': why, 'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})


def read(k, rid):
    P.read(k, rid)
    r = [x for x in P.rows_load() if x.get('kind') == 'read' and x['kernel'] == k and str(x['run']) == str(rid)]
    if r:
        print('   THE AXIOMS LINES (%d):' % len(r[-1]['axioms_lines']))
        for l in r[-1]['axioms_lines']:
            print('     ax | ' + l)


LV_FILE = 'SIDELvConservation/T3_StepNineBridge.lean'
NEG = 'T3doubleprime_general_commutation_fails'


def _ws(t):
    return ' '.join(t.split())


def _decl(L, name):
    """### the text of a declaration from its keyword line to its ':=' (the statement), whitespace folded; its first line number."""
    i = next(m for m, l in enumerate(L) if re.match(r'^(theorem|lemma|def|abbrev)\s+%s\b' % re.escape(name), l))
    j = i
    while ':=' not in L[j]:
        j += 1
    return i + 1, _ws(' '.join(L[i:j + 1]).split(':=')[0]), _ws(L[j].split(':=', 1)[1] + ' ' + (L[j + 1] if j + 1 < len(L) else ''))


def closure_check(repo, f):
    """### the seat's check, by text: T3_perClass_to_combinations's statement with PerClassExcludes and CombinationsExclude unfolded by
    ### their definitions' bodies (parameters as named at the use), closed over its binders, set beside NEG's statement after its `¬ `.
    ### EQUAL means NEG proves the negation of the closure: a discharge as stated would derive False with it. Its planted control: the
    ### same check against T3prime_shared_witness's statement, which must read NOT EQUAL."""
    L = (P.show(repo, f, LV_FILE) or '').split(NL)
    _a, pce, pce_body = _decl(L, 'PerClassExcludes')
    _b, cbe, cbe_body = _decl(L, 'CombinationsExclude')
    ln, st, _x = _decl(L, LV[1])
    m = re.match(r'theorem \S+ \((𝒞 : Set Coupling)\) \((s : ℂ)\) \(h : (.*)\) : (.*)$', st)
    hyp = m.group(3).replace('PerClassExcludes C s', '∃ Φ : ℝ → ℂ, C Φ ∧ mellin Φ (s / 2) ≠ 0')
    con = m.group(4).replace('CombinationsExclude 𝒞 s', '∃ Φ : ℝ → ℂ, (∀ C ∈ 𝒞, C Φ) ∧ mellin Φ (s / 2) ≠ 0')
    # ### the substituted bodies are the definitions' own, read back and compared, so the replacement text is not the seat's invention
    assert _ws(pce_body.split(' /--')[0]) .startswith('∃ Φ : ℝ → ℂ, C Φ ∧ mellin Φ (s / 2) ≠ 0'), pce_body
    assert _ws(cbe_body.split(' /--')[0]).startswith('∃ Φ : ℝ → ℂ, (∀ C ∈ 𝒞, C Φ) ∧ mellin Φ (s / 2) ≠ 0'), cbe_body
    closure = _ws('∀ (%s) (%s), (%s) → %s' % (m.group(1), m.group(2), hyp, con))
    nl, nst, _y = _decl(L, NEG)
    neg = _ws(nst.split(':', 1)[1]) if nst.startswith('theorem %s :' % NEG) else nst
    eq = neg == '¬ ' + closure
    pl, pst, _z = _decl(L, 'T3prime_shared_witness')
    ctrl = _ws(pst.split(':', 1)[1]) == '¬ ' + closure
    print('### THE CLOSURE CHECK (the seat`s, by text): %s :%d unfolded and closed: %s' % (LV[1], ln, closure))
    print('    %s :%d after its `¬ `: %s' % (NEG, nl, neg[2:] if neg.startswith('¬ ') else neg))
    print('    %s ; its control (T3prime_shared_witness :%d set in NEG`s place) %s -- %s' % (
        'EQUAL: the kernel proves the negation of the statement`s closure, so a discharge as stated would derive False with it' if eq
        else 'NOT EQUAL', pl, 'NOT EQUAL' if not ctrl else 'EQUAL', 'AS WANTED' if not ctrl else 'NOT AS WANTED'))
    return {'statement_line': ln, 'neg_line': nl, 'closure': closure, 'neg': neg, 'equal': eq, 'control_equal': ctrl}


def lv():
    k, name = LV
    repo = 'D:/' + k
    f = R.full(k)
    c, o, e = P.g(repo, 'grep', '-n', '-E', r'(theorem|lemma)[[:space:]]+%s\b' % name, f, '--', '*.lean')
    hits = [l for l in o.split(NL) if l.strip()]
    print('### %s at its pin %s = %s ; the declaration of %s by git grep: %d hit(s)' % (k, R.PIN[k][0], f[:12], name, len(hits)))
    out = []
    for h in hits:
        _rev, path, ln, _t = h.split(':', 3)
        L = (P.show(repo, f, path) or '').split(NL)
        i = int(ln) - 1
        j = i
        while j < len(L) and ':=' not in L[j]:
            j += 1
        end = next((m for m in range(j + 1, len(L)) if re.match(r'^(theorem|lemma|def|end|namespace|section|/--|@\[|noncomputable|abbrev)\b', L[m])),
                   len(L))
        sor = [m + 1 for m in range(i, end) if re.search(r'\bsorry\b', L[m].split('--', 1)[0])]   # ### the tactic, not a comment's word
        print('## %s :%d-:%d (the statement), the proof to :%d' % (path, i + 1, j + 1, end))
        for m in range(i, j + 1):
            print('   %5d| %s' % (m + 1, L[m]))
        print('## THE SORRY`S POSITION: %s' % (', '.join('%s:%d' % (path, s) for s in sor) or 'NONE IN THE DECLARATION'))
        for s in sor:
            print('   %5d| %s' % (s, L[s - 1]))
        out.append({'path': path, 'line': i + 1, 'statement': L[i:j + 1], 'sorry_lines': sor, 'proof_end': end})
    neg = closure_check(repo, f)
    uses = [l.split(':', 1)[1] for l in P.g(repo, 'grep', '-n', '-w', name, f, '--', '*.lean')[1].split(NL) if l.strip()]
    dep = [u for u in uses if not re.search(r'(theorem|lemma)\s+%s\b|#print axioms' % name, u.split(':', 2)[2])]
    print('### the name in the pin`s .lean files: %d lines (%s) ; used by another declaration: %d%s' % (
        len(uses), ' ; '.join(u[:90] for u in uses), len(dep), (' -- ' + ' ; '.join(dep)) if dep else ''))
    neg['uses'], neg['dependents'] = uses, dep
    allw = [l for l in P.g(repo, 'grep', '-n', '-w', 'sorry', f, '--', '*.lean')[1].split(NL) if l.strip()]
    allsor = [l for l in allw if re.match(r'^\s*sorry\b', l.split(':', 3)[3])]          # ### a line opening with the tactic
    print('### the `sorry` word in the pin`s .lean files: %d lines ; of them a line opening with the tactic: %d -- %s (the build`s target '
          'SIDELvConservation reported one sorry warning at b721, data/b721_rebuild.txt :16)' % (
              len(allw), len(allsor), ' ; '.join(l.split(':', 1)[1][:160] for l in allsor)))
    old = [r for r in P.rows_load() if r.get('kind') == 'lv']
    if old:                                            # ### a read, no kernel touched: the row replaced, the count printed
        keep = [r for r in P.rows_load() if r.get('kind') != 'lv']
        io.open(ROWS + '.tmp', 'w', encoding='utf-8', newline='\n').write(json.dumps(keep, indent=1, ensure_ascii=False) + NL)
        os.replace(ROWS + '.tmp', ROWS)
        print('### the lv row replaced (%d before)' % len(old))
    P.rows_add({'kind': 'lv', 'kernel': k, 'pin': f, 'decls': out, 'all_sorry': [l.split(':', 1)[1] for l in allsor], 'closure': neg,
                'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})


def b721_axioms():
    """### b721's read row of SIDE-lv-conservation's run, its axioms lines joined where Lean wrapped them."""
    rs = json.load(io.open(os.path.join(D_, 'b721_rebuild_rows.json'), encoding='utf-8'))
    ax = [r for r in rs if r.get('kind') == 'read' and r['kernel'] == LV[0]][-1]['axioms_lines']
    out = []
    for l in ax:
        if l.startswith(' ') and out:
            out[-1] += l
        else:
            out.append(l)
    return out


def bank():
    rs = P.rows_load()
    by = lambda kind: dict((r['kernel'], r) for r in rs if r.get('kind') == kind)   # noqa: E731
    cm, pu, di, rd = by('commit'), by('push'), by('dispatch'), by('read')
    out = ['b723 -- (R333)(7): WAVE 1`S AXIOM STEP AT THE SIX PINS, STOPPABLE -- repaired on rebuild-b721 by b722`s priced route, one dispatch '
           'per kernel read by its run id (%s)' % time.strftime('%Y-%m-%d', time.gmtime()), '',
           '### Written by tools/b723_axiom.py bank from data/b723_axiom_rows.json. The free memory read before each push, dispatch and read',
           '### against the 2,560 MB hold (b718`s hold_or_exit); no main or tag touched; no lean or lake process on this host; the branch commits',
           '### by git plumbing, author and committer the seat`s neutral identity (b723 axiom seat <b723-axiom@relay.invalid>).', '',
           'COMMITTED %d ; PUSHED %d ; DISPATCHED %d (six at most) ; READ %d' % (len(cm), len(pu), len(di), len(rd)), '']
    done = 0
    for k, tag, p in R.PINS:
        line = '  %-21s %s = %s' % (k, tag, p)
        if k == LV[0]:
            lvr = [r for r in rs if r.get('kind') == 'lv']
            out.append(line + ' ; the step ran clean at b721 (run 40706311269, data/b721_rebuild.txt :17-:24), not re-dispatched')
            for d in (lvr[-1]['decls'] if lvr else []):
                out.append('      %s :%d, the statement:' % (d['path'], d['line']))
                out += ['      | ' + s for s in d['statement']]
                out.append('      THE SORRY`S POSITION: %s' % (', '.join('%s:%d' % (d['path'], s) for s in d['sorry_lines']) or 'NONE'))
            for c in [r['closure'] for r in lvr if r.get('closure')][-1:]:
                ax = [l for l in b721_axioms() if NEG in l]
                out += ['      THE CLOSURE CHECK (the seat`s, by text): the statement :%d with PerClassExcludes and CombinationsExclude unfolded by their '
                        'bodies and closed over its binders --' % c['statement_line'], '      | ' + c['closure'],
                        '      %s :%d reads `¬ ` and that closure: %s ; its control (T3prime_shared_witness in its place) %s, AS %s' % (
                            NEG, c['neg_line'], 'EQUAL' if c['equal'] else 'NOT EQUAL', 'EQUAL' if c['control_equal'] else 'NOT EQUAL',
                            'NOT WANTED' if c['control_equal'] else 'WANTED'),
                        '      %s at b721`s run 40706311269: %s' % (NEG, ' '.join(ax) or 'NOT READ'),
                        '      the name in the pin`s .lean files: %d lines ; used by another declaration: %d (%s)' % (
                            len(c.get('uses', [])), len(c.get('dependents', [])), ' ; '.join(c.get('dependents', [])) or 'none: its own '
                            'declaration and AxiomCheck.lean`s #print alone'),
                        '      THE DISCHARGE, PRICED: NOT AVAILABLE AS STATED -- T3_perClass_to_combinations is false as stated: the kernel proves its '
                        'negation sorry-free (:137), so a proof of it would derive False; no other declaration depends on it. THE READING FOR THE '
                        'ROOT`S PROMPT (the author`s word (6)(d)): an ERRATA entry with the deposit`s wording corrected at the release sitting, and '
                        'the statement replaced by its proved negation or removed at lv`s next version; the author`s word at the root chooses.']
            if not lvr:
                out.append('      the lv route NOT RUN')
            done += 1
            continue
        if k not in cm:
            kd = [r for r in rs if r.get('kind', '').startswith('kdraft') and r['kernel'] == k]
            if kd:
                d = kd[-1]
                out.append(line + ' ; %s (the author`s word (6)(c)): the diff formed in memory, places %s ; imports cut %d (%s) ; #print names '
                           'kept %d, cut %d' % ('HALTED' if d['kind'] == 'kdraft_halt' else 'DRAFT CLEAR', d['places'], len(d['imports_cut']),
                                                ', '.join(d['imports_cut']), d['names_kept'], len(d['names_cut'])))
                out += ['      cut | %s (%s)' % (n, 'not declared at the pin' if w is None else w) for n, w in d['names_cut']]
                out += ['      diff | ' + x for x in d['diff']]
                out.append('      the refusal step under the TARGET a push carries: exit %d "%s" ; under the dispatch target: exit %d' % (
                    d['empty_exit'], d['empty_out'], d['control_exit']))
                out.append('      ' + d['why'] + '; nothing committed, pushed or run')
            else:
                out.append(line + ' ; NOT COMMITTED: %s' % ('READY, not run' if k in READY else WORD[k]))
            continue
        nn = len(cm[k]['names']) if cm[k].get('names') else len([x for x in rd.get(k, {}).get('axioms_lines', []) if x.startswith("'")])
        out.append(line + ' ; committed %s over %s (print_targets.txt, blob %s, %d names: %s)' % (
            cm[k]['sha'][:10], cm[k]['parent'][:10], cm[k]['blob'][:10], nn, cm[k].get('source', 'main`s blob verbatim')))
        if cm[k].get('names') and k not in VERBATIM:
            out.append('      names | ' + ' ; '.join(cm[k]['names']))
        for n, why in cm[k].get('dropped', []):
            out.append('      DROPPED | %s -- %s' % (n, why))
        if k in pu:
            out.append('      pushed %s (host free %d MB, origin equal %s)' % (pu[k]['sha'][:10], pu[k]['free_mb'], pu[k]['remote_equal']))
        d = di.get(k)
        if not d:
            out.append('      NOT DISPATCHED, carried')
            continue
        r = rd.get(k)
        if not r:
            out.append('      run %s (target %s): NOT READ, carried' % (d['run'], d['target']))
            continue
        st = [s for s in r.get('steps', []) if s[0] == 'Axioms of the named terminals']
        out.append('      run %s at %s (target %s, host free %d MB): %s %s ; build exit %s ; sorry warnings %d ; the axiom step %s ; host free %d MB '
                   'at the read' % (r['run'], d['at'], d['target'], d['free_mb'], r['status'], r['conclusion'], r['build_exit'], r['sorry_warnings'],
                                    st[0][1] if st else 'NOT FOUND', r['free_mb']))
        out += ['      ax | ' + l[:240] for l in r.get('axioms_lines', [])]
        if st and st[0][1] == 'success' and any('depends on axioms' in l or 'does not depend on any axioms' in l for l in r.get('axioms_lines', [])):
            done += 1
    halted = [r['kernel'] for r in rs if r.get('kind') == 'kdraft_halt']
    out += ['', '### ### **THE AXIOM STEP AT %d OF 6 PINS (%d REPAIRED AND RUN THIS ACT, SIDE-lv-conservation CLEAN AT b721) ; HALTED %d (%s) ; '
            'RUNS %d ; THE lv SORRY`S DISCHARGE NOT AVAILABLE AS STATED ; NO MAIN OR TAG TOUCHED.**' % (
                done, done - 1, len(halted), ', '.join(halted) or 'none', len(di))]
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline='\n').write(NL.join(out) + NL)
    os.replace(OUT + '.tmp', OUT)
    print(NL.join(out))
    print('written data/b723_axiom.txt')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'plan':
        plan()
    elif a[0] == 'commit':
        commit(a[1])
    elif a[0] == 'push':
        push(a[1])
    elif a[0] == 'dispatch':
        dispatch(a[1])
    elif a[0] == 'read':
        read(a[1], a[2])
    elif a[0] == 'findrun':
        findrun(a[1])
    elif a[0] == 'kdraft':
        kdraft()
    elif a[0] == 'lv':
        lv()
    elif a[0] == 'bank':
        bank()
