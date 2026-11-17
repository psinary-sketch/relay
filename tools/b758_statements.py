# -*- coding: utf-8 -*-
"""tools/b758_statements.py -- (R368)(7): THE STATEMENTS FOR SECTIONS 6 TO 8, BANKED AND NOT WRITTEN. Written whole by the Write tool at b758's
Component 4, committed before it runs; reads only, the one write the bank data/b758_epstein_statements.txt (through standing.figbank).

(7)'s words (relay data/b758_ferry.txt :21): "It banks data/b758_epstein_statements.txt from the kernel at the tag (5) cuts, or at 596d1c9e where
(5) did not land: for each of zq_offline_zero, zq_count_instance, zq_explicitFormula, zq_explicit_formula_instance, zq_premises, rQ_one,
zq_coeff_not_multiplicative, cQ_eq, cQ_four, cQ_six, cQ_forty_eight, cQ_not_nonneg, wide_detector and zq_arith_side_re_neg, its file and line,
its statement as written, its docstring, and its axioms line with the run that printed it; and from THE_EPSTEIN_CONTROL_OBJECT_v0_1.md the heads
of sections 6 to 8 with their line ranges."

THE FORMS: each name's head line `<file>.lean :<line> -- <the full name>` ((R368)(9)'s head of a line reporting a dated record); its docstring
and its statement as quote rows, `      :<n> "<the line as written>"` (the record's own words, dropped by the act's matchers as quotations);
its axioms line as the run's axioms file reads it, with the run's id, or NO AXIOMS LINE with the runs read. The document's sections by
PLACE-papers path, line range and the head line's sha256 (16 hex), the head's words not copied: a PLACE-papers line enters a relay bank by
path, line and digest. The declarations are found by b757's reader (tools/b757_join.py: DECL, decls_in, libs_at, module_of), each name's
line where decls_in over the file to that line ends with the name's declaration; the axioms by tools/b758_controls.py's reader over each
run's downloaded artifact.

  control                       the tool's controls, printed
  bank <rev> <run> [<run> ...]  data/b758_epstein_statements.txt: the kernel at rev (the tag (5) cuts, read by its peel, or 596d1c9e),
                                the axioms from the runs named, the first that prints a name's line giving it; `b757:<run>` names a b757
                                run, its artifact under b757's folder
"""
import hashlib
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
import b757_join as J            # noqa: E402  (the reader as committed at b757)
import b758_controls as C        # noqa: E402  (the axioms reader over a run's artifact)
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b758'
EF = J.EF
PP = 'D:/MY-DOwnloads/PLACE-papers'
DOC = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
BANK = os.path.join(D, 'b758_epstein_statements.txt')
COEFF_TIP = '596d1c9e19f0acada7543526bd831538b2520d73'
NAMES = ('zq_offline_zero', 'zq_count_instance', 'zq_explicitFormula', 'zq_explicit_formula_instance', 'zq_premises', 'rQ_one',
         'zq_coeff_not_multiplicative', 'cQ_eq', 'cQ_four', 'cQ_six', 'cQ_forty_eight', 'cQ_not_nonneg', 'wide_detector', 'zq_arith_side_re_neg')
SECTIONS = ('6', '7', '8')
ATTR = re.compile(r'^\s*(?:@\[|set_option\b.*\bin\s*$|attribute\b)')


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def show(rev, path):
    r = J.gr('show', '%s:%s' % (rev, path))
    return r.stdout.replace('\r', '') if r.returncode == 0 else None


def find(rev, short):
    """[(file, line, full name)] of each declaration of `short` in the library modules at rev."""
    libs = J.libs_at(rev)
    hit = J.g('grep', '-n', '-E', '-e', J.DECL % J._esc(short), rev, '--', '*.lean')
    out = []
    for h in hit.split(NL):
        p = h.split(':', 3)
        if len(p) < 4 or not J.module_of(p[1], libs):
            continue
        text = show(rev, p[1]) or ''
        ls = text.split(NL)
        i = int(p[2])
        names = J.decls_in(NL.join(ls[:i]), short)
        if names:
            out.append((p[1], i, names[-1]))
    return out


def statement(ls, i):
    """the declaration at line i (1-based) as written, from its head to its `:=` (cut there), its `where`, or the blank line ending it:
    [(line, text)]."""
    out = []
    for k in range(i - 1, min(len(ls), i + 59)):
        l = ls[k]
        code = l.split('--', 1)[0]
        if k > i - 1 and not l.strip():
            break
        if ':=' in code:
            out.append((k + 1, l[:l.index(':=')].rstrip() + ' :='))
            break
        out.append((k + 1, l.rstrip()))
        if re.search(r'\bwhere\s*$', code):
            break
    return out


def docstring(ls, i):
    """the `/-- ... -/` block before the declaration at line i, attribute and set_option lines between skipped: [(line, text)], or []."""
    j = i - 2
    while j >= 0 and ATTR.match(ls[j]):
        j -= 1
    if j < 0 or not ls[j].rstrip().endswith('-/'):
        return []
    k = j
    while k >= 0 and '/--' not in ls[k]:
        k -= 1
    return [(n + 1, ls[n].rstrip()) for n in range(k, j + 1)] if k >= 0 else []


def axioms_in(runs):
    """[(run, {full name: axioms})] from each run's downloaded artifact, in the order named; a run not downloaded read as absent."""
    out = []
    for run in runs:
        if str(run).startswith('b757:'):   # ### a b757 run, its artifact under b757's folder (tools/b757_controls.py RUNS), for (7)'s fallback at 596d1c9e
            rid = str(run).split(':', 1)[1]
            art = os.path.join('D:/b757-runs', 'ef-%s' % rid, 'build-module-%s' % rid)
        else:
            art = C._art('ef', run)
        p = os.path.join(art, 'axioms.txt')
        out.append((run, C.axioms_of(C._f(art, 'axioms.txt')) if os.path.exists(p) else None))
    return out


def axiom_line(full, short, ax):
    for run, a in ax:
        if a is None:
            continue
        if full in a:
            return run, full, a[full]
        tail = [n for n in a if n.split('.')[-1] == short]
        if len(tail) == 1:
            return run, tail[0], a[tail[0]]
    return None


def sections():
    """[(section, first line, last line, sha256 of the head line)] of THE_EPSTEIN_CONTROL_OBJECT_v0_1.md at PLACE-papers HEAD: a head line
    `#`-led whose first word is the section's number; each range to the line before the next head of its level or above."""
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:%s' % DOC], capture_output=True)
    ls = r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL)
    heads = [(i, len(re.match(r'^(#+)', l).group(1)), l) for i, l in enumerate(ls) if re.match(r'^#+\s', l)]
    out = []
    for s in SECTIONS:
        m = [(i, lv, l) for i, lv, l in heads if re.match(r'^#+\s+(?:§\s*)?%s(?:[.:)\s]|$)' % s, l)]
        if len(m) != 1:
            out.append((s, None, None, 'FOUND %d HEADS' % len(m)))
            continue
        i, lv, l = m[0]
        nxt = next((k for k, lv2, _l in heads if k > i and lv2 <= lv), len(ls))
        last = nxt
        while last > i + 1 and not ls[last - 1].strip():
            last -= 1
        out.append((s, i + 1, last, hashlib.sha256(l.encode('utf-8')).hexdigest()[:16]))
    return out


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    f = find(COEFF_TIP, 'cQ_forty_eight')
    c('cQ_forty_eight at 596d1c9e: one declaration, its file in the coefficient module', [(a, b, n) for a, b, n in f],
      len(f) == 1 and f[0][0].endswith('CoeffSign.lean') and f[0][2].endswith('.cQ_forty_eight'))
    ls = (show(COEFF_TIP, f[0][0]) or '').split(NL) if f else []
    st = statement(ls, f[0][1]) if f else []
    c('its statement read from its head to its `:=`', '%d lines, the last ending %r' % (len(st), st[-1][1][-12:] if st else ''),
      bool(st) and st[-1][1].endswith(':=') and st[0][0] == f[0][1])
    pl = ['/-- a planted docstring', '   over two lines -/', '@[simp]', 'theorem t : 1 = 1 := rfl']
    c('a planted docstring read across an attribute line', docstring(pl, 4), [n for n, _t in docstring(pl, 4)] == [1, 2])
    c('a planted declaration with no docstring', docstring(['', 'theorem t : 1 = 1 := rfl'], 2), docstring(['', 'theorem t : 1 = 1 := rfl'], 2) == [])
    nf = find(COEFF_TIP, 'noSuchDeclarationPlanted')
    c('a planted name declared nowhere', nf, nf == [])
    sx = sections()
    c('the document`s sections 6 to 8, each one head with its range, the head`s words not printed', [(s, a, b) for s, a, b, _h in sx],
      all(a and b and b >= a for _s, a, b, _h in sx))
    al = axiom_line('X.Y.cQ_four', 'cQ_four', [('1', None), ('2', {'X.Y.cQ_four': ('propext',)})])
    c('the axioms line from the first run that prints it, a run not downloaded passed over', al, al == ('2', 'X.Y.cQ_four', ('propext',)))
    return L, ok


def cmd_bank(rev, *runs):
    full_rev = J.g('rev-parse', '%s^{commit}' % rev).strip()
    if not full_rev or not runs:
        sys.exit('### usage: bank <rev> <run> [<run> ...] -- the rev %r read %r' % (rev, full_rev))
    L, ok = controls()
    ax = axioms_in(runs)
    out = ['%s -- (R368)(7): THE STATEMENTS FOR SECTIONS 6 TO 8, BANKED AND NOT WRITTEN, FROM SIDE-explicit-formula AT %s (%s)' % (ACT, full_rev[:8], _now()),
           '', '## THE CONTROLS'] + L + ['', '## THE RUNS READ FOR THE AXIOMS LINES'] + [
           '  run %s: %s' % (r, 'its axioms file read, %d lines' % len(a) if a is not None else 'NOT DOWNLOADED, NOT READ') for r, a in ax] + [
           '', '## THE FOURTEEN NAMES, EACH AT ITS FILE AND LINE: ITS DOCSTRING AND ITS STATEMENT AS WRITTEN (quote rows), ITS AXIOMS LINE WITH ITS RUN']
    found = noax = 0
    for short in NAMES:
        f = find(full_rev, short)
        out.append('')
        if len(f) != 1:
            out.append('  %s -- %s DECLARATIONS AT %s: %s' % (short, 'NO' if not f else len(f), full_rev[:8], ['%s :%d %s' % x for x in f]))
            continue
        found += 1
        path, i, full = f[0]
        ls = (show(full_rev, path) or '').split(NL)
        ds, st = docstring(ls, i), statement(ls, i)
        out.append('  %s :%d -- %s (the module %s)' % (path, i, full, J.module_of(path, J.libs_at(full_rev))))
        out.append('    its docstring%s' % ('' if ds else ': none'))
        out += ['      :%d "%s"' % (n, t) for n, t in ds]
        out.append('    its statement as written, :%d-:%d' % (st[0][0], st[-1][0]) if st else '    its statement: NOT READ')
        out += ['      :%d "%s"' % (n, t) for n, t in st]
        a = axiom_line(full, short, ax)
        if a:
            out.append('    its axioms line, run %s: %s [%s]%s' % (a[0], a[1], ', '.join(a[2]), '' if set(a[2]) <= set(C.STANDARD) else '  OUTSIDE THE STANDARD THREE'))
        else:
            noax += 1
            out.append('    its axioms line: NO AXIOMS LINE in the runs read (%s)' % ', '.join(str(r) for r, _a in ax))
    sx = sections()
    out += ['', '## THE DOCUMENT`S SECTIONS 6 TO 8, AT PLACE-papers HEAD, BY PATH, LINE RANGE AND THE HEAD LINE`S DIGEST (the words not copied)'] + [
        '  PLACE-papers %s :%s-:%s -- section %s, its head at :%s, sha256 %s' % (DOC, a, b, s, a, h) if a else '  section %s: %s' % (s, h)
        for s, a, b, h in sx]
    out += ['', '### ### **THE STATEMENTS BANK: AT %s ; NAMES %d, FOUND ONE DECLARATION %d ; NO AXIOMS LINE %d ; SECTIONS %d OF 3 ; CONTROLS %d OF %d.**' % (
        full_rev[:8], len(NAMES), found, noax, sum(1 for _s, a, _b, _h in sx if a), sum(ok), len(ok))]
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b758_epstein_statements.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        print(NL.join(controls()[0]))
    elif a[:1] == ['bank']:
        cmd_bank(*a[1:])
    else:
        sys.exit(__doc__)
