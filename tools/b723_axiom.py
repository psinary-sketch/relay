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
SIDE-kernel's changed workflow, each line. Those three are READY ON THE AUTHOR'S WORD: drafted and printed by `plan`, not committed.
SIDE-lv-conservation's step ran clean at b721 (data/b721_rebuild.txt :17-:24); its route is `lv`, the sorry's statement and position.

  plan                 per kernel: the pin, the branch's local and origin tips, b722's class, the route, the print_targets.txt drafted (main's
                       blob verbatim) and each name re-read as declared at the pin by `git grep`; nothing written
  commit <kernel>      one plumbing commit on rebuild-b721 (its tip the pin) adding print_targets.txt; one ref moved (old value checked)
  push <kernel>        free memory read; the branch pushed; ls-remote read; one row
  dispatch <kernel>    b718's dispatch (main's build-module.yml, -f ref=<the branch's sha>, -f target=<the pin's target>); one row
  read <kernel> <id>   b718's read route over b723's rows; the axioms lines printed whole
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
READY = ('SIDE-archimedean', 'SIDE-rcurve')
WORD = {'SIDE-spinor': 'the six SIDESpinorLeg names not declared at the pin, dropped or kept (b722`s price, data/b722_axiom_diag.txt :37)',
        'SIDE-frobenius': 'the target list: the kernel never carried one (data/b722_axiom_diag.txt :28)',
        'SIDE-kernel': 'the changed workflow, each line, a push trigger and the pin`s imports (data/b722_axiom_diag.txt :11)'}
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


def targets_text(k):
    return P.show('D:/' + k, 'main', 'print_targets.txt') or ''


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
        if k in READY or k == 'SIDE-spinor':
            t = targets_text(k)
            names = [n.strip() for n in t.split(NL) if n.strip()]
            dec = declared_at_pin(k, names)
            print('   print_targets.txt drafted: main`s blob verbatim, %d bytes, %d names ; declared at the pin by git grep: %d of %d' % (
                len(t.encode('utf-8')), len(names), sum(1 for v in dec.values() if v), len(names)))
            for n in names:
                print('     %-48s %s' % (n, ('AT ' + dec[n]) if dec[n] else 'NOT FOUND'))


def commit(k):
    if k not in READY:
        sys.exit('## %s: not READY (%s); nothing written' % (k, WORD.get(k, 'the lv route')))
    if [r for r in P.rows_load() if r.get('kind') == 'commit' and r['kernel'] == k]:
        sys.exit('## %s: committed already at b723; nothing written' % k)
    repo = 'D:/' + k
    f = R.full(k)
    tip = P.gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH)
    if tip != f:
        sys.exit('## %s: the tip %s is not the pin %s; nothing written' % (k, tip[:12], f[:12]))
    if P.g(repo, 'ls-tree', f, 'print_targets.txt')[1].strip():
        sys.exit('## %s: the pin carries print_targets.txt; nothing written' % k)
    t = targets_text(k)
    b = P.blob(repo, t)
    mb = P.gs(repo, 'rev-parse', 'main:print_targets.txt')
    assert b == mb, (b, mb)
    rows = [l for l in P.gs(repo, 'ls-tree', f).split(NL) if l.strip()] + ['100644 blob %s\tprint_targets.txt' % b]
    rows.sort(key=lambda l: l.split('\t', 1)[1] + ('/' if ' tree ' in l else ''))
    c, tree, e = P.g(repo, 'mktree', inp=(NL.join(rows) + NL).encode('utf-8'))
    assert c == 0, e
    msg = ('b723 under (R333)(7): the axiom step`s target list print_targets.txt at the pin %s, main`s blob %s verbatim, nothing else '
           '(b722`s class TARGETS ABSENT AT THE PIN)' % (f[:12], b[:12]))
    c, cm, e = P.g(repo, *(SEAT + ['commit-tree', tree.strip(), '-p', f, '-m', msg]))
    assert c == 0, e
    cm = cm.strip()
    c, _o, e = P.g(repo, 'update-ref', 'refs/heads/' + BRANCH, cm, f)
    assert c == 0, e
    print('## %s : %s at %s, parent the pin %s, adding print_targets.txt (blob %s, equal to main`s) and nothing else; author and committer %s'
          % (k, BRANCH, cm[:12], f[:12], b[:12], P.gs(repo, 'log', '-1', '--format=%an <%ae> / %cn <%ce>', cm)))
    print(P.g(repo, 'diff', '--stat', f, cm)[1].rstrip())
    P.rows_add({'kind': 'commit', 'kernel': k, 'sha': cm, 'parent': f, 'blob': b, 'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})


def push(k):
    repo = 'D:/' + k
    cm = [r for r in P.rows_load() if r.get('kind') == 'commit' and r['kernel'] == k]
    if not cm or [r for r in P.rows_load() if r.get('kind') == 'push' and r['kernel'] == k]:
        sys.exit('## %s: no commit row, or pushed already at b723; nothing pushed' % k)
    tip = P.gs(repo, 'rev-parse', 'refs/heads/' + BRANCH)
    if tip != cm[-1]['sha']:
        sys.exit('## %s: the tip is not b723`s commit; nothing pushed' % k)
    fm = P.hold_or_exit('the push of ' + k)
    print('### free memory %d MB (hold %d) ; pushing %s %s at %s (fast-forward from the pin %s)' % (fm, P.HOLD_MB, k, BRANCH, tip[:12],
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
    P.dispatch(k)


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
                        '      THE DISCHARGE, PRICED: NOT AVAILABLE AS STATED -- the kernel proves, sorry-free, the negation of the statement`s closure, so '
                        'a proof of it would derive False; the routes the file itself names: T3prime_shared_witness (:121, Determination`s two '
                        'hypotheses, a changed statement the work order`s "no weakened statement" bars) or the deposit`s wording corrected at the '
                        'release sitting. The author`s word at the root`s prompt chooses.']
            if not lvr:
                out.append('      the lv route NOT RUN')
            done += 1
            continue
        if k not in cm:
            out.append(line + ' ; NOT COMMITTED: %s' % ('READY, not run' if k in READY else 'READY ON THE AUTHOR`S WORD -- ' + WORD[k]))
            continue
        out.append(line + ' ; committed %s (print_targets.txt, blob %s, main`s verbatim)' % (cm[k]['sha'][:10], cm[k]['blob'][:10]))
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
    out += ['', '### ### **THE AXIOM STEP AT %d OF 6 PINS (%d REPAIRED AND RUN THIS ACT, SIDE-lv-conservation CLEAN AT b721) ; READY ON THE AUTHOR`S '
            'WORD %d (%s) ; DISPATCHED %d ; THE lv SORRY`S DISCHARGE NOT AVAILABLE AS STATED ; NO MAIN OR TAG TOUCHED.**' % (
                done, done - 1, len([k for k in WORD if k not in cm]), ', '.join(k for k in WORD if k not in cm) or 'none', len(di))]
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
    elif a[0] == 'lv':
        lv()
    elif a[0] == 'bank':
        bank()
