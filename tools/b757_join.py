# -*- coding: utf-8 -*-
"""tools/b757_join.py -- (R367)(4): THE JOIN OF THE FOUR BRANCHES IN SIDE-explicit-formula, its reads and its one write. The merges themselves
go through the one-call tool (tools/standing/commit.py SIDE-explicit-formula merge <commit>, concluded by its commit route), one git write a
message; this tool writes nothing in any repository but print_targets.txt in the kernel's working tree, and that only inside a merge
conflicted in that file, the one file (R367)(4) names: "resolved as the union of the lines of main and the four tips, each line kept once".

  union                 print_targets.txt at main 8fbab45d and at each tip (and the base each forks at): lines, changed from the base, the union
  resolve               within a merge on push-b757-join conflicted in print_targets.txt alone: the union written to the working file (LF);
                        the written lines read back against the union
  check [rev]           the joined file's line set at rev (default push-b757-join) against the union: differences 0 wanted, repeats 0
  targets [rev]         the module declaring each line of print_targets.txt at rev, every declaration hit read; a name with no hit or with hits
                        in more than one module after the namespace read is printed and refused; the modules, the dispatch's targets
  merges                each merge commit on push-b757-join read back: its parents, the second the tip (R367)(4) names, in its order
  bank                  data/b757_join.txt through standing.figbank: the controls first, then the merges, the union check, the targets
"""
import io
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b757_worklist as K        # noqa: E402
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b757'
EF = K.EF_DIR
MAIN = K.EF_BASE
JOIN = 'push-b757-join'
NAMED = 'print_targets.txt'
# ### (R367)(4): the four tips in the order of their merges
TIPS = (('detect-b729', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e'), ('keiper-b725', '01fd33c2d7dc62d4702b075de3dda9253c5c2f87'),
        ('c2-b725', '0395f15d3b2906716ccb1f09ca24171d7a921210'), ('zq-b730', '1e6588703732435b34d840bbbb840225932c9b6b'))
BANK = os.path.join(D, 'b757_join.txt')
DECL = r'^(@\[[^]]*\] *)?((private|protected|noncomputable|nonrec|partial|unsafe) +)*(theorem|lemma|def|abbrev|structure|instance|inductive|class|opaque) +([A-Za-z0-9_.\x27]+\.)?%s([ :({\[]|$)'


def g(*a):
    r = subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout


def gr(*a):
    return subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def lines_at(rev, path=NAMED):
    r = gr('show', '%s:%s' % (rev, path))
    if r.returncode != 0:
        return None
    return [l.strip() for l in r.stdout.replace('\r', '').split(NL) if l.strip()]


def union_of(seqs):
    """the lines of each sequence in turn, each line kept once, in the order first met."""
    out, seen = [], set()
    for s in seqs:
        for l in s or ():
            if l not in seen:
                seen.add(l)
                out.append(l)
    return out


def the_union():
    return union_of([lines_at(MAIN)] + [lines_at(sha) for _n, sha in TIPS])


def compare(have, want):
    """(missing from have, extra in have, repeats in have)."""
    hs, ws = set(have), set(want)
    rep = sorted(set(l for l in have if have.count(l) > 1))
    return sorted(ws - hs), sorted(hs - ws), rep


def cmd_union():
    base = g('merge-base', MAIN, TIPS[0][1]).strip()
    b = lines_at(base)
    print('  the base each tip forks at: %s (%s lines in %s)' % (base[:8], len(b or []), NAMED))
    m = lines_at(MAIN)
    print('  main %s: %d lines ; changed from the base %s' % (MAIN[:8], len(m), m != b))
    for n, sha in TIPS:
        t = lines_at(sha)
        fb = g('merge-base', MAIN, sha).strip()
        print('  %-12s %s: %d lines ; changed from the base %s ; forks at %s ; new beside main %d' % (n, sha[:8], len(t or []), t != b, fb[:8], len(set(t or []) - set(m))))
    u = the_union()
    print('### THE UNION OF MAIN AND THE FOUR TIPS: %d LINES, EACH ONCE' % len(u))


def _conflicted():
    return [x for x in g('diff', '--name-only', '--diff-filter=U').split(NL) if x.strip()]


def cmd_resolve():
    br = g('symbolic-ref', '--short', 'HEAD').strip()
    merging = gr('rev-parse', '-q', '--verify', 'MERGE_HEAD').stdout.strip()
    con = _conflicted()
    if br != JOIN or not merging or con != [NAMED]:
        sys.exit('### NOT RESOLVED, NOTHING WRITTEN: the branch %r (want %s) ; MERGE_HEAD %s ; conflicted %s (want [%r] alone)' % (br, JOIN, merging[:8] or 'none', con, NAMED))
    u = the_union()
    p = os.path.join(EF, NAMED)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(u) + NL)
    back = [l.strip() for l in io.open(p, encoding='utf-8').read().split(NL) if l.strip()]
    miss, extra, rep = compare(back, u)
    print('  %s written in the working tree within the merge of %s: %d lines ; against the union of main and the four tips (%d): missing %d, extra %d, repeats %d -> %s' % (
        NAMED, merging[:8], len(back), len(u), len(miss), len(extra), len(rep), 'DIFFERENCES 0' if not (miss or extra or rep) else 'DIFFERS'))
    print('  next: `commit.py SIDE-explicit-formula add %s`, then the commit route concludes the merge' % NAMED)


def check_lines(rev=JOIN):
    have = lines_at(rev)
    u = the_union()
    if have is None:
        return ['  %s at %s: ABSENT' % (NAMED, rev)], False
    raw = gr('show', '%s:%s' % (rev, NAMED)).stdout.replace('\r', '').split(NL)
    reps = len([l for l in raw if l.strip()]) - len(set(l.strip() for l in raw if l.strip()))
    miss, extra, rep = compare([l.strip() for l in raw if l.strip()], u)
    ok = not (miss or extra or rep)
    return ['  %s at %s (%s): %d lines ; the union of main and the four tips %d ; missing %d %s ; extra %d %s ; repeats %d -> %s' % (
        NAMED, rev, g('rev-parse', '--short=8', rev).strip(), len(have), len(u), len(miss), miss[:5], len(extra), extra[:5], reps,
        'DIFFERENCES 0' if ok else 'DIFFERS')], ok


def cmd_check(rev=JOIN):
    L, ok = check_lines(rev)
    print(NL.join(L))


def _esc(s):
    return ''.join('\\' + ch if ch in '.^$*+?()[]{}|\\' else ch for ch in s)


def module_of(path):
    return path[:-5].replace('/', '.') if path.endswith('.lean') else None


def targets_at(rev=JOIN):
    """{name: (module or None, [candidate modules], why)} for each line of print_targets.txt at rev."""
    names = lines_at(rev) or []
    libs = ('SIDEExplicitFormula/', 'Zeta23/')
    out = {}
    for n in names:
        parts = n.split('.')
        short, ns = parts[-1], '.'.join(parts[:-1])
        hit = g('grep', '-n', '-E', '-e', DECL % _esc(short), rev, '--', '*.lean')
        files = sorted(set(h.split(':', 2)[1] for h in hit.split(NL) if h.count(':') >= 2))
        files = [f for f in files if f.startswith(libs)]
        if len(files) > 1:
            keep = []
            for f in files:
                txt = g('show', '%s:%s' % (rev, f))
                opened = re.findall(r'^namespace +(\S+)', txt, re.M)
                if any(ns == o or ns.endswith('.' + o) or o.endswith(ns) or ns.startswith(o + '.') for o in opened) or (ns and module_of(f).startswith(ns)):
                    keep.append(f)
            files = keep if keep else files
        mods = [module_of(f) for f in files]
        out[n] = (mods[0] if len(mods) == 1 else None, mods, 'one' if len(mods) == 1 else 'NO DECLARATION FOUND' if not mods else 'MORE THAN ONE MODULE')
    return out


def cmd_targets(rev=JOIN):
    t = targets_at(rev)
    bad = dict((n, v) for n, v in t.items() if v[0] is None)
    mods = sorted(set(v[0] for v in t.values() if v[0]))
    for n, v in sorted(bad.items()):
        print('  REFUSED %s: %s %s' % (n, v[2], v[1][:4]))
    print('  THE MODULES (%d), the dispatch`s targets:' % len(mods))
    print(' '.join(mods))
    print('### NAMES %d ; RESOLVED TO ONE MODULE %d ; REFUSED %d ; MODULES %d' % (len(t), len(t) - len(bad), len(bad), len(mods)))


def merges_lines():
    L, ok = [], True
    log = [l.split() for l in g('log', '--first-parent', '--reverse', '--format=%H %P', '%s..%s' % (MAIN, JOIN)).split(NL) if l.strip()]
    mc = [x for x in log if len(x) == 3]
    for i, (n, sha) in enumerate(TIPS):
        if i < len(mc):
            c, p1, p2 = mc[i]
            good = p2 == sha
            ok = ok and good
            L.append('  merge %d: %s ; first parent %s ; second parent %s, the tip of %s %s -> %s' % (i + 1, c[:8], p1[:8], p2[:8], n, sha[:8], 'AS ORDERED' if good else 'NOT AS ORDERED'))
        else:
            ok = False
            L.append('  merge %d of %s %s: NOT MADE' % (i + 1, n, sha[:8]))
    L.append('  commits on %s past main %s, first parent: %d (merges %d, others %d)' % (JOIN, MAIN[:8], len(log), len(mc), len(log) - len(mc)))
    return L, ok


def cmd_merges():
    L, ok = merges_lines()
    print(NL.join(L))


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    u = union_of([['a', 'b'], ['b', 'c'], ['a', 'd', 'c']])
    c('the union on planted sequences, each line once in the order first met', u, u == ['a', 'b', 'c', 'd'])
    m, e, r = compare(['a', 'b', 'b', 'x'], ['a', 'b', 'c'])
    c('the comparison on a planted file: missing, extra, repeats', (m, e, r), (m, e, r) == (['c'], ['x'], ['b']))
    c('the escape keeps a prime and escapes a dot', _esc("a.b'"), _esc("a.b'") == "a\\.b'")
    c('a declaration pattern on planted lines', [bool(re.search(DECL % _esc(x), y)) for x, y in (('foo', 'theorem foo : True'), ('foo', 'private lemma foo (h : x)'),
                                                                                                  ('foo', 'theorem foobar : True'), ('bar', 'theorem Foo.bar : True'),
                                                                                                  ('foo', '-- theorem foo'))],
      [bool(re.search(DECL % _esc(x), y)) for x, y in (('foo', 'theorem foo : True'), ('foo', 'private lemma foo (h : x)'), ('foo', 'theorem foobar : True'),
                                                        ('bar', 'theorem Foo.bar : True'), ('foo', '-- theorem foo'))] == [True, True, False, True, False])
    tips = [(n, g('rev-parse', sha).strip() == sha) for n, sha in TIPS]
    c('the four tips (R367)(4) names stand in the kernel at their commits', tips, all(x for _n, x in tips))
    c('main 8fbab45d stands', g('rev-parse', 'main').strip()[:8], g('rev-parse', 'main').strip() == MAIN)
    return L, ok


def cmd_bank():
    L, ok = controls()
    ml, mok = merges_lines()
    cl, cok = check_lines(JOIN)
    t = targets_at(JOIN)
    bad = dict((n, v) for n, v in t.items() if v[0] is None)
    mods = sorted(set(v[0] for v in t.values() if v[0]))
    out = ['%s -- (R367)(4): THE JOIN OF THE FOUR BRANCHES IN SIDE-explicit-formula, READ BACK (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '## THE MERGES, IN (R367)(4)`S ORDER, EACH BY ITS COMMIT'] + ml + [
        '', '## THE JOINED %s AGAINST THE UNION OF MAIN AND THE FOUR TIPS' % NAMED] + cl + [
        '', '## THE DISPATCH`S TARGETS: THE MODULE DECLARING EACH LINE OF THE JOINED %s' % NAMED] + [
        '  REFUSED %s: %s %s' % (n, v[2], v[1][:4]) for n, v in sorted(bad.items())] + [
        '  names %d ; resolved to one module %d ; refused %d ; modules %d:' % (len(t), len(t) - len(bad), len(bad), len(mods)), '  ' + ' '.join(mods), '',
        '### ### **THE JOIN: MERGES %s ; THE UNION %s ; TARGETS %d MODULES FOR %d NAMES, %d REFUSED ; CONTROLS %d OF %d.**' % (
            'AS ORDERED' if mok else 'NOT AS ORDERED', 'DIFFERENCES 0' if cok else 'DIFFERS', len(mods), len(t), len(bad), sum(ok), len(ok))]
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b757_join.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'union': cmd_union, 'resolve': cmd_resolve, 'check': cmd_check, 'targets': cmd_targets, 'merges': cmd_merges, 'bank': cmd_bank,
          'control': lambda: print(NL.join(controls()[0]))}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
