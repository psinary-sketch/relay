# -*- coding: utf-8 -*-
"""tools/b758_presend.py -- (R368)(4): THE TWO PRE-SEND READS IN SIDE-explicit-formula, each of which b757's run met unread (b757 defect (l)).
Reads only: nothing is written in any repository; the one write is the bank data/b758_presend.txt (through standing.figbank).

  (i)  over the modules the dispatch names (the module declaring each line of print_targets.txt, tools/b757_join.py's reader) and over their
       import closure in the kernel's tree, which is what out/Axioms.lean loads (build-module.yml :85 imports every target): each fully
       qualified declaration name read to occur in one module; the duplicates printed, 0 wanted. A private declaration is the module's own
       and is not read; the namespace at each declaration read by the namespace, section, mutual and end lines outside block comments.
  (ii) each line of print_targets.txt read against the workflow's filter, the case pattern at build-module.yml :91 read from the file at the
       revision (the class between `*[!` and `]*)`, ranges and escapes expanded); the lines it refuses printed by line number. The file is not
       edited for them and the workflow is not widened ((R368)(4)).

  control               the controls, printed
  read <rev>            both reads at a revision, printed
  bank <before> <tip>   the controls, both reads at each revision, written to data/b758_presend.txt with the foot read at the tip
"""
import io
import os
import re
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
import b757_join as J            # noqa: E402  ### b757's reader of the targets, the libraries and the namespaces, read and not changed
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b758'
BANK = os.path.join(D, 'b758_presend.txt')
WORKFLOW = '.github/workflows/build-module.yml'
DECL_ANY = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?((?:(?:private|protected|noncomputable|nonrec|partial|unsafe|scoped|local)\s+)*)'
                      r'(theorem|lemma|def|abbrev|structure|instance|inductive|class|opaque|axiom)\s+([^\s:({\[⦃]+)')
# ### an instance the first pattern does not name: a priority before its name, or no name (Lean generates one from the type, so two
# ### anonymous instances on one type in one namespace in two modules collide as two declarations of one name do)
INST = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?((?:(?:private|protected|noncomputable|scoped|local)\s+)*)instance\b\s*(?:\(priority\s*:=\s*[^)]*\)\s*)?(.*)$')


def _inst_type(rest):
    """the type of an anonymous instance as its first line writes it: after the first colon outside brackets, before := or where;
    '' where the line holds no such colon (the type on a later line, unread)."""
    s = re.split(r'\swhere\b', rest.split(':=')[0])[0]
    depth = 0
    for i, ch in enumerate(s):
        if ch in '([{⦃⟨':
            depth += 1
        elif ch in ')]}⦄⟩':
            depth -= 1
        elif ch == ':' and depth == 0:
            return ' '.join(s[i + 1:].split())
    return ''
IMPORT = re.compile(r'^\s*(?:public\s+|meta\s+|private\s+)*import\s+(.+?)\s*(?:--.*)?$')


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def all_decls(text, anon=None):
    """[(full name, line)] of every declaration in a Lean file that is not private: the namespace at each by tools/b757_join.py's lines
    (namespace, section, mutual, end) outside block comments; `_root_.` honoured; `class inductive` read as its name; an instance named
    after its priority read as named. Each anonymous instance that is not private is appended to `anon` as (namespace, type, line)."""
    stack, out, depth = [], [], 0
    for k, l in enumerate(text.split(NL), 1):
        if depth == 0:
            m = J.NS_OPEN.match(l)
            if m:
                stack.append(m.group(1).split('.'))
            elif J.MUT_OPEN.match(l) or J.SEC_OPEN.match(l):
                stack.append([])
            elif J.END.match(l):
                if stack:
                    stack.pop()
            else:
                d = DECL_ANY.match(l)
                if d and 'private' not in d.group(1).split():
                    nm = d.group(3).rstrip('.')
                    if d.group(2) == 'class' and nm == 'inductive':
                        m2 = re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:\w+\s+)*class\s+inductive\s+([^\s:({\[⦃]+)', l)
                        nm = m2.group(1).rstrip('.') if m2 else ''
                    if nm and nm != 'where':
                        ns = [c for grp in stack for c in grp]
                        if nm.startswith('_root_.'):
                            ns, nm = [], nm[len('_root_.'):]
                        out.append(('.'.join(ns + [nm]), k))
                elif not d:
                    i = INST.match(l)
                    if i and 'private' not in i.group(1).split():
                        rest = i.group(2)
                        ns = [c for grp in stack for c in grp]
                        nmm = re.match(r'([^\s:({\[⦃]+)', rest)
                        if nmm and nmm.group(1) != 'where':
                            nm = nmm.group(1).rstrip('.')
                            if nm.startswith('_root_.'):
                                ns, nm = [], nm[len('_root_.'):]
                            out.append(('.'.join(ns + [nm]), k))
                        elif anon is not None:
                            anon.append(('.'.join(ns), _inst_type(rest), k))
        depth = max(0, depth + l.count('/-') - l.count('-/'))
    return out


def anon_pairs(anon_by_module):
    """{(namespace, type): [(module, line), ...]} for each anonymous instance type read in one namespace in more than one module."""
    seen = {}
    for mod, rows in anon_by_module.items():
        for ns, ty, ln in rows:
            if ty:
                seen.setdefault((ns, ty), [])
                if mod not in [m for m, _l in seen[(ns, ty)]]:
                    seen[(ns, ty)].append((mod, ln))
    return dict((k, v) for k, v in seen.items() if len(v) > 1)


def duplicates(decls_by_module):
    """{full name: [(module, line), ...]} for each name declared in more than one module."""
    seen = {}
    for mod, decls in decls_by_module.items():
        for nm, ln in decls:
            seen.setdefault(nm, [])
            if mod not in [m for m, _l in seen[nm]]:
                seen[nm].append((mod, ln))
    return dict((nm, v) for nm, v in seen.items() if len(v) > 1)


def tree_files(rev):
    return set(x for x in J.g('ls-tree', '-r', '--name-only', rev).split(NL) if x.endswith('.lean'))


def path_of(mod, libs, files):
    """the file of a module in the tree, as Lake names it (tools/b757_join.py's module_of, inverted); None for a module outside the tree."""
    for pre, sd in libs:
        p = (sd + '/' if sd else '') + mod.replace('.', '/') + '.lean'
        if p in files and p.startswith(pre):
            return p
    p = mod.replace('.', '/') + '.lean'
    return p if p in files else None


def imports_of(text):
    out = []
    for l in text.split(NL):
        m = IMPORT.match(l)
        if m:
            out += [x for x in m.group(1).split() if x not in ('runtime',)]
        elif l.strip() and not l.strip().startswith(('--', '/-', '-/', 'module', 'prelude')) and out:
            break
    return out


def closure(mods, rev, libs, files):
    """(the modules in the tree reached from `mods` by their imports, with their texts; the imports outside the tree, counted)."""
    todo, seen, texts, outside = list(mods), set(), {}, set()
    while todo:
        m = todo.pop()
        if m in seen:
            continue
        seen.add(m)
        p = path_of(m, libs, files)
        if not p:
            outside.add(m)
            continue
        texts[m] = (p, J.g('show', '%s:%s' % (rev, p)))
        todo += [x for x in imports_of(texts[m][1]) if x not in seen]
    return texts, outside


def filter_class(rev):
    """(line number, the class's text, the set of characters it passes) from the workflow at rev; (0, '', set()) where unread."""
    yml = J.g('show', '%s:%s' % (rev, WORKFLOW)).replace('\r', '').split(NL)
    for k, l in enumerate(yml, 1):
        if 'print target refused' in l:
            m = re.search(r'\*\[!([^\]]*)\]\*\)', l)
            if m:
                return k, m.group(1), class_chars(m.group(1))
    return 0, '', set()


def target_class(rev):
    """(line number, the class's text, the set it passes) of the workflow's target filter (`target refused`, the module list's case)."""
    yml = J.g('show', '%s:%s' % (rev, WORKFLOW)).replace('\r', '').split(NL)
    for k, l in enumerate(yml, 1):
        if 'echo "target refused' in l:
            m = re.search(r'\*\[!([^\]]*)\]\*', l)
            if m:
                return k, m.group(1), class_chars(m.group(1))
    return 0, '', set()


def class_chars(cls):
    ok, i = set(), 0
    while i < len(cls):
        ch = cls[i]
        if ch == '\\' and i + 1 < len(cls):
            ok.add(cls[i + 1])
            i += 2
        elif i + 2 < len(cls) and cls[i + 1] == '-':
            ok |= set(chr(o) for o in range(ord(ch), ord(cls[i + 2]) + 1))
            i += 3
        else:
            ok.add(ch)
            i += 1
    return ok


def filter_read(rev):
    """(the workflow's line, the class, [(line number, name, passed)]) over print_targets.txt at rev, each line as the workflow reads it
    (carriage return removed, spaces trimmed at both ends, an empty line passed over)."""
    k, cls, ok = filter_class(rev)
    raw = J.g('show', '%s:%s' % (rev, J.NAMED)).split(NL)
    rows = []
    for n, l in enumerate(raw, 1):
        s = l.replace('\r', '').strip()
        if s:
            rows.append((n, s, bool(ok) and all(c in ok for c in s)))
    return k, cls, rows


def read_at(rev):
    """the two reads at a revision, as lines, and the figures of the foot."""
    sha = J.g('rev-parse', rev).strip()
    libs = J.libs_at(rev)
    files = tree_files(rev)
    t = J.targets_at(rev)
    bad = sorted(n for n, v in t.items() if v[0] is None)
    mods = sorted(set(v[0] for v in t.values() if v[0]))
    texts, outside = closure(mods, rev, libs, files)
    by_t = dict((m, all_decls(texts[m][1])) for m in mods if m in texts)
    an_c = dict((m, []) for m in texts)
    by_c = dict((m, all_decls(tx, an_c[m])) for m, (_p, tx) in texts.items())
    dup_t, dup_c = duplicates(by_t), duplicates(by_c)
    an_n = sum(len(v) for v in an_c.values())
    an_u = sum(1 for v in an_c.values() for _ns, ty, _l in v if not ty)
    an_p = anon_pairs(an_c)
    k, cls, rows = filter_read(rev)
    refused = [(n, s) for n, s, okk in rows if not okk]
    L = ['## AT %s (%s)' % (rev, sha[:8]),
         '  THE TARGETS (tools/b757_join.py`s reader): names %d ; resolved to one module %d ; refused %d %s ; modules %d' % (len(t), len(t) - len(bad), len(bad), bad[:4], len(mods)),
         '  THE IMPORT CLOSURE IN THE TREE: modules %d (the targets` %d among them, %d of them read) ; imports outside the tree %d (Mathlib and the toolchain`s, not read)' % (
             len(texts), len(mods), len(by_t), len(outside)),
         '  (i) THE FULLY QUALIFIED DECLARATION NAMES, NONE PRIVATE: over the targets` modules %d names, duplicates %d ; over the closure %d names, duplicates %d (0 wanted)' % (
             sum(len(v) for v in by_t.values()), len(dup_t), sum(len(v) for v in by_c.values()), len(dup_c))]
    for nm, v in sorted(dup_c.items()):
        L.append('    DUPLICATE %s: %s' % (nm, ' ; '.join('%s :%d (%s)' % (m, ln, 'a target' if m in by_t else 'imported') for m, ln in v)))
    L.append('  (i), THE NAMES LEAN GENERATES, BOUNDED: anonymous instances over the closure %d (the type read on its first line %d, on a later line %d, '
             'unread) ; one namespace and one type text in two modules %d (0 wanted)' % (an_n, an_n - an_u, an_u, len(an_p)))
    for (ns, ty), v in sorted(an_p.items()):
        L.append('    ANONYMOUS PAIR namespace %s, type %s: %s' % (ns or '(root)', ty, ' ; '.join('%s :%d' % (m, ln) for m, ln in v)))
    L.append('  (ii) THE FILTER (%s :%d at %s): the class %r passes %s ; lines %d ; passed %d ; refused %d' % (
        WORKFLOW, k, sha[:8], cls, describe(class_chars(cls)), len(rows), len(rows) - len(refused), len(refused)))
    for n, s in refused:
        bad_c = sorted(set('U+%04X' % ord(c) for c in s if c not in class_chars(cls)))
        L.append('    REFUSED print_targets.txt :%d %s (characters outside the class: %s) -- a line no print can reach by this workflow' % (n, s, ', '.join(bad_c)))
    tk, tcls, tok = target_class(rev)
    tbad = [m for m in mods if not all(c in tok for c in m)]
    L.append('  BESIDE (ii), THE DISPATCH`S INPUT: the modules against the target filter (%s :%d, the class %r, a refusal exiting 2 before any build): passed %d of %d%s' % (
        WORKFLOW, tk, tcls, len(mods) - len(tbad), len(mods), (' ; REFUSED ' + ' '.join(tbad)) if tbad else ''))
    return L, dict(sha=sha, names=len(t), refused_targets=len(bad), modules=len(mods), closure=len(texts), dup_t=len(dup_t), dup_c=len(dup_c),
                   filtered=[n for n, _s in refused], lines=len(rows), anon=an_n, anon_unread=an_u, anon_pairs=len(an_p), target_refused=len(tbad))


def describe(ok):
    parts = []
    for lo, hi, w in (('A', 'Z', 'A-Z'), ('a', 'z', 'a-z'), ('0', '9', '0-9')):
        if all(chr(o) in ok for o in range(ord(lo), ord(hi) + 1)):
            parts.append(w)
    rest = sorted(c for c in ok if not (c.isascii() and c.isalnum()))
    return ', '.join(parts + [repr(c) for c in rest]) + ' (%d characters)' % len(ok)


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    planted = NL.join(['namespace A', 'def x : Nat := 0', 'private def y : Nat := 1', '/- def w := 2', 'end -/', 'section', 'namespace B',
                       'theorem x : True := trivial', 'end B', 'end', 'theorem _root_.z : True := trivial', 'instance : Inhabited Nat := ⟨0⟩',
                       'instance instFoo : Inhabited Nat := ⟨0⟩', '@[simp] lemma v : 1 = 1 := rfl', 'class inductive K | a', 'end A', '-- def q := 0'])
    got = [n for n, _k in all_decls(planted)]
    c('every declaration on a planted file (a private one, a commented one, an anonymous instance and a line comment not read; a section, a '
      'nested namespace, _root_, an attribute, a class inductive read)', got, got == ['A.x', 'A.B.x', 'z', 'A.instFoo', 'A.v', 'A.K'])
    an = []
    got2 = [n for n, _k in all_decls(planted + NL + NL.join(['namespace C', 'instance (priority := 100) [Foo α] : Bar α := x',
                                                             'instance (priority := 100) named : Baz := x', 'private instance : Qux := x',
                                                             'scoped instance sc : Baz := x', 'instance :', '  Long := x', 'end C']), an)]
    c('the instances on planted lines (the anonymous one, one after a priority with a binder, a private one not taken, a named one after a '
      'priority and a scoped one read as named, a type on the next line unread)', (got2[6:], an),
      got2[6:] == ['C.named', 'C.sc'] and an == [('A', 'Inhabited Nat', 12), ('C', 'Bar α', 19), ('C', '', 23)])
    ap = anon_pairs({'M1': [('A', 'Inhabited Nat', 3), ('A', '', 5)], 'M2': [('A', 'Inhabited Nat', 7), ('B', 'Inhabited Nat', 8)], 'M3': [('A', '', 2)]})
    c('the anonymous pairs on planted modules (one namespace and type in two modules taken; another namespace, and two unread types, not)', ap,
      ap == {('A', 'Inhabited Nat'): [('M1', 3), ('M2', 7)]})
    dp = duplicates({'M1': [('A.x', 3), ('A.y', 4)], 'M2': [('A.x', 9)], 'M3': [('B.x', 1)]})
    c('the duplicates on planted modules (the same name in one namespace in two modules; the same short name in two namespaces not)', dp,
      dp == {'A.x': [('M1', 3), ('M2', 9)]})
    c('the imports of a planted header (two lines, a comment between, the body after not read)', imports_of(NL.join(['import A.B', '-- c', 'import C', '', 'namespace X', 'import D'])),
      imports_of(NL.join(['import A.B', '-- c', 'import C', '', 'namespace X', 'import D'])) == ['A.B', 'C'])
    cc = class_chars("A-Za-z0-9_.\\'")
    c('the class of the workflow`s pattern as written, expanded: A-Z, a-z, 0-9, underscore, full stop, the prime', describe(cc),
      cc == set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.\''))
    k, cls, _ok = filter_class(K_JOIN)
    c('the class read from %s at %s, the line the ruling names' % (WORKFLOW, K_JOIN[:8]), (k, cls), k == 91 and class_chars(cls) == cc)
    tk, tcls, tok = target_class(K_JOIN)
    c('the target filter read from %s at %s (:44: letters, digits, underscore, full stop and the space parting the modules)' % (WORKFLOW, K_JOIN[:8]),
      (tk, tcls), tk == 44 and tok == (cc - set("'")) | set(' '))
    pl = [(s, all(ch in cc for ch in s)) for s in ('Foo.bar', "Foo.bar'", 'Foo.zqPair_Λ_one', 'Foo-bar', 'Foo.b₁')]
    c('the filter on planted names (a dotted name and a prime passed; the Greek capital lambda, a hyphen and a subscript refused)', pl,
      [x for _s, x in pl] == [True, True, False, False, False])
    lb = J.libs_at(K_JOIN)
    fs = tree_files(K_JOIN)
    po = (path_of('SIDEExplicitFormula.Schema.ZQ.OffZero.Time', lb, fs), path_of('Lc.LiCriterion.ReverseDirection', lb, fs), path_of('Mathlib.Tactic', lb, fs))
    c('the module`s file as Lake names it, inverted (the default library, the vendored srcDir, a module outside the tree)', po,
      po == ('SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean', 'Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean', None))
    tm = all_decls(J.g('show', '%s:SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean' % K_JOIN))
    sm = all_decls(J.g('show', '%s:SIDEExplicitFormula/Schema/ZQ/OffZero/Sums.lean' % K_JOIN))
    pos = duplicates({'Time': tm, 'Sums': sm})
    c('THE POSITIVE CONTROL, b757`s break (data/b757_events.txt (17)): at %s the reader finds SIDEExplicitFormula.Schema.ZQ.OffZero.sRe in '
      'OffZero.Time :18 and OffZero.Sums :134' % K_JOIN[:8], sorted(pos.items())[:2],
      pos.get('SIDEExplicitFormula.Schema.ZQ.OffZero.sRe') == [('Time', 18), ('Sums', 134)])
    return L, ok


K_JOIN = '6568e9c7a5b34a7283a08c55f813c82b3cc54c07'   # ### push-b757-join's tip, (R368)(4)'s base


def cmd_read(rev):
    L, f = read_at(rev)
    print(NL.join(L))
    print('### AT %s: DUPLICATES OVER THE CLOSURE %d ; OVER THE TARGETS %d ; ANONYMOUS PAIRS %d (OF %d, %d UNREAD) ; REFUSED BY THE FILTER %d %s ; MODULES REFUSED %d' % (
        f['sha'][:8], f['dup_c'], f['dup_t'], f['anon_pairs'], f['anon'], f['anon_unread'], len(f['filtered']), f['filtered'], f['target_refused']))


def cmd_bank(before, tip):
    L, ok = controls()
    lb, fb = read_at(before)
    lt, ft = read_at(tip)
    out = ['%s -- (R368)(4): THE TWO PRE-SEND READS IN SIDE-explicit-formula, BEFORE THE DISPATCH (%s)' % (ACT, _now()), '',
           '### (i) each fully qualified declaration name in one module, over the targets` modules and their import closure in the tree, the',
           '### duplicates printed, 0 wanted at the tip; (ii) each line of print_targets.txt against build-module.yml :91`s filter, the lines it',
           '### refuses printed, two expected (:358 and :359, each carrying the Greek capital lambda); the file not edited, the workflow not widened.',
           '', '## THE CONTROLS'] + L + ['', '### the join`s tip as b757 left it, before (4)`s one commit'] + lb + [
           '', '### the tip the dispatch is sent at'] + lt + ['',
           '### ### **THE PRE-SEND READS AT %s: DUPLICATES %d (OVER THE TARGETS %d) ; ANONYMOUS PAIRS %d (OF %d, %d UNREAD) ; REFUSED BY THE FILTER %d (%s) ; '
           'TARGETS %d MODULES FOR %d NAMES, %d REFUSED, MODULES REFUSED %d ; CONTROLS %d OF %d.**' % (
               ft['sha'][:8], ft['dup_c'], ft['dup_t'], ft['anon_pairs'], ft['anon'], ft['anon_unread'], len(ft['filtered']),
               ', '.join(':%d' % n for n in ft['filtered']) or 'none', ft['modules'], ft['names'], ft['refused_targets'], ft['target_refused'], sum(ok), len(ok))]
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b758_presend.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L_, ok_ = controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok_), len(ok_)))
    elif a[:1] == ['read'] and len(a) == 2:
        cmd_read(a[1])
    elif a[:1] == ['bank'] and len(a) == 3:
        cmd_bank(a[1], a[2])
    else:
        sys.exit(__doc__)
