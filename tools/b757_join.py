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


# ### the first reader (as committed at relay da4fcbcd) kept a candidate file where the name's namespace began with any namespace the file
# ### opened, and read the default library alone: at push-b757-join 0cc23db8 it resolved 399 of 419 names and refused 20 (no declaration 1,
# ### the vendored LiCriterion.positivity_implies_RH; more than one module 19). This reader reads the namespace at each declaration by the
# ### file's namespace, section and end lines outside comments, and names a module as Lake does, relative to its library's srcDir.
FIRST_READER = 'relay da4fcbcd: resolved 399 of 419, refused 20 (no declaration 1, more than one module 19)'
NS_OPEN = re.compile(r'^\s*namespace\s+([A-Za-z0-9_.\x27]+)\s*$')
SEC_OPEN = re.compile(r'^\s*(?:noncomputable\s+)?section\b')
MUT_OPEN = re.compile(r'^\s*mutual\s*$')
END = re.compile(r'^\s*end\b(?:\s+[A-Za-z0-9_.\x27]+)?\s*(?:--.*)?$')


def libs_at(rev):
    """[(prefix, srcDir or '')]: each lean_lib of lakefile.toml at rev -- its srcDir, or the roots of its globs where it has none."""
    toml = g('show', '%s:lakefile.toml' % rev)
    out = []
    for blk in re.split(r'^\[\[', toml, flags=re.M)[1:]:
        if not blk.startswith('lean_lib]]'):
            continue
        sd = re.search(r'^srcDir\s*=\s*"([^"]+)"', blk, re.M)
        if sd:
            out.append((sd.group(1).rstrip('/') + '/', sd.group(1).rstrip('/')))
            continue
        gl = re.search(r'^globs\s*=\s*\[([^\]]*)\]', blk, re.M)
        for x in re.findall(r'"([^"]+)"', gl.group(1) if gl else ''):
            out.append((re.sub(r'\.[+*]$', '', x).replace('.', '/') + '/', ''))
    return out


def module_of(path, libs=None):
    if not path.endswith('.lean'):
        return None
    for pre, sd in libs or ():
        if path.startswith(pre):
            return (path[len(sd) + 1:] if sd else path)[:-5].replace('/', '.')
    return None if libs else path[:-5].replace('/', '.')


def decls_in(text, short):
    """the full names of the declarations of `short` in a Lean file: the namespace at each read by the namespace, section, mutual and end
    lines outside block comments (nested /- -/ counted); `_root_.` honoured; a dotted declaration name taken whole."""
    stack, out, depth = [], [], 0
    pat = re.compile(DECL % _esc(short))
    for l in text.split(NL):
        if depth == 0:
            m = NS_OPEN.match(l)
            if m:
                stack.append(m.group(1).split('.'))
            elif MUT_OPEN.match(l) or SEC_OPEN.match(l):
                stack.append([])
            elif END.match(l):
                if stack:
                    stack.pop()
            else:
                d = pat.match(l)
                if d:
                    pre = (d.group(5) or '').rstrip('.')
                    ns = [c for grp in stack for c in grp]
                    if pre.startswith('_root_'):
                        ns, pre = [], pre[len('_root_'):].lstrip('.')
                    out.append('.'.join(ns + ([pre] if pre else []) + [short]))
        depth = max(0, depth + l.count('/-') - l.count('-/'))
    return out


def targets_at(rev=JOIN):
    """{name: (module or None, [candidate modules], why)} for each line of print_targets.txt at rev: a module whose file declares the full name."""
    names = lines_at(rev) or []
    libs = libs_at(rev)
    texts, out = {}, {}
    for n in names:
        short = n.split('.')[-1]
        hit = g('grep', '-n', '-E', '-e', DECL % _esc(short), rev, '--', '*.lean')
        files = sorted(set(h.split(':', 2)[1] for h in hit.split(NL) if h.count(':') >= 2))
        files = [f for f in files if module_of(f, libs)]
        mods = []
        for f in files:
            if f not in texts:
                texts[f] = g('show', '%s:%s' % (rev, f))
            if n in decls_in(texts[f], short):
                mods.append(module_of(f, libs))
        mods = sorted(set(mods))
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
    planted = NL.join(['namespace A.B', '/- namespace X', 'end -/', 'theorem foo : True := trivial', 'section', 'namespace C', 'lemma foo : 1 = 1 := rfl',
                       'end C', 'end', 'theorem D.foo : True := trivial', 'theorem _root_.foo : True := trivial', 'end A.B', '-- theorem foo', 'def foo := 0'])
    got = decls_in(planted, 'foo')
    c('the namespace read on a planted file (a comment holding namespace and end, a section, a nested namespace, a dotted name, _root_, a line '
      'comment, a top-level def)', got, got == ['A.B.foo', 'A.B.C.foo', 'A.B.D.foo', 'foo', 'foo'])
    lb = libs_at(MAIN)
    mo = (module_of('Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean', lb), module_of('SIDEExplicitFormula/Schema/Detector.lean', lb),
          module_of('AxiomCheck.lean', lb))
    c('the libraries of lakefile.toml at main and a module named as Lake names it (the vendored srcDir, the default library, a root file in no '
      'library)', (lb, mo), mo == ('Lc.LiCriterion.ReverseDirection', 'SIDEExplicitFormula.Schema.Detector', None))
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
        '  names %d ; resolved to one module %d ; refused %d ; modules %d:' % (len(t), len(t) - len(bad), len(bad), len(mods)), '  ' + ' '.join(mods),
        '  the reader`s lineage: the first reader, %s ; this reader, resolved %d of %d, refused %d' % (FIRST_READER, len(t) - len(bad), len(t), len(bad)), '',
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
