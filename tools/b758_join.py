# -*- coding: utf-8 -*-
"""tools/b758_join.py -- (R368)(4): THE JOIN LANDED IN SIDE-explicit-formula, READ BEFORE ITS DISPATCH. Written whole by the Write tool at b758's
Component 2; the reader of b757's join (tools/b757_join.py, committed, imported here and not edited: lines_at, targets_at, libs_at, module_of,
decls_in) read at push-b758-land. Reads only; the one write is the bank data/b758_land.txt (through standing.figbank) and the dispatch's targets
data/b758_land_targets.json, bound to the commit they were read at (tools/b758_controls.py dispatch --targets-json reads them).

(4)'s words (relay data/b758_ferry.txt :15): "The branch push-b758-land is made at push-b757-join's tip 6568e9c7. ONE COMMIT: in
Schema/ZQ/OffZero/Time.lean the definition sRe at :18 is renamed timeSRe, with its uses in that file; Sums.lean :134 keeps its name; no
statement's meaning changes." ... "THE DISPATCH, one, at the branch's tip, its targets each module the joined print_targets.txt names."

  land     the branch read: one commit past 6568e9c7, its parent 6568e9c7; the one file Time.lean; the tip's Time.lean equal to the base's with
           each timeSRe read back as sRe, no sRe left as a word, timeSRe four times; Sums.lean unchanged, its :134 still declaring sRe;
           print_targets.txt unchanged; then the module declaring each line at the tip, the dispatch's targets
  control  the tool's controls, printed
  bank     data/b758_land.txt and data/b758_land_targets.json: the controls first, the branch read, the targets

(5)'s words (ferry :17): "the branch push-b758-coeff is made at main, and push-b757-coeff's tip 596d1c9e is merged into it without
fast-forward. One file is named for a conflicted merge: print_targets.txt, resolved as the union of both sides' lines, each kept once, with
the lines naming a declaration that stands in no module of the merged tree removed and printed ... the union is read against the tree before
the send. A conflict in any other file halts the merge with nothing concluded. THE DISPATCH, one, at the merged tip, the whole tree's targets."
The merge itself goes through the one-call tool (commit.py SIDE-explicit-formula merge 596d1c9e, which aborts on a conflict in any file but
print_targets.txt), concluded by its commit route; this tool writes print_targets.txt in the kernel's working tree inside that merge alone.

  union [ours]      print_targets.txt at ours (default the remote main's read-back, refs/remotes/origin/main) and at 596d1c9e, and at their
                    merge base: lines, the union of both sides, each line once, ours' order first
  resolve           within the merge on push-b758-coeff of 596d1c9e, print_targets.txt alone conflicted: the union's lines each read against the
                    merged working tree (the tracked Lean files on disk, the libraries of lakefile.toml on disk); a line naming a declaration
                    in no module removed and printed; the rest written (LF) and read back
  check [rev]       the file at rev (default push-b758-coeff) against the union of its merge's two parents: no line outside the union, none
                    twice, each union line left out naming no declaration at rev, each kept line resolved at rev
  merges            the merge commit on push-b758-coeff read back: one commit past its first parent, its second parent 596d1c9e
  coeffbank         data/b758_coeff.txt and data/b758_coeff_targets.json: the controls, the merge, the check, the targets at the tip
  coeffcontrol      the merge's controls, printed (the libraries' reader, the five names at 596d1c9e, a planted name, the union, the tip)
"""
import io
import json
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
import b757_join as J            # noqa: E402  (the reader as committed at b757; EF from b757's worklist, the kernel's folder)
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b758'
EF = J.EF
JOIN_TIP = '6568e9c7a5b34a7283a08c55f813c82b3cc54c07'   # ### push-b757-join's tip, (R368)(4) and the SCOPE line
LAND = 'push-b758-land'
TIME = 'SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean'
SUMS = 'SIDEExplicitFormula/Schema/ZQ/OffZero/Sums.lean'
NAMED = J.NAMED
BANK = os.path.join(D, 'b758_land.txt')
TARGETS_JSON = os.path.join(D, 'b758_land_targets.json')
COEFF_TIP = '596d1c9e19f0acada7543526bd831538b2520d73'   # ### push-b757-coeff's tip, (R368)(5) and the SCOPE line
COEFF = 'push-b758-coeff'
COEFF_BANK = os.path.join(D, 'b758_coeff.txt')
COEFF_JSON = os.path.join(D, 'b758_coeff_targets.json')
WORD = re.compile(r'(?<![A-Za-z0-9_.\x27])sRe(?![A-Za-z0-9_\x27])')
NEW = re.compile(r'(?<![A-Za-z0-9_.\x27])timeSRe(?![A-Za-z0-9_\x27])')


def g(*a):
    return J.g(*a)


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def show(rev, path):
    r = J.gr('show', '%s:%s' % (rev, path))
    return r.stdout.replace('\r', '') if r.returncode == 0 else None


def rename_read(base_text, tip_text):
    """(equal after the rename read back, sRe words left at the tip, timeSRe words at the tip, timeSRe words at the base). Pure."""
    if base_text is None or tip_text is None:
        return (False, None, None, None)
    back = NEW.sub('sRe', tip_text)
    return (back == base_text, len(WORD.findall(tip_text)), len(NEW.findall(tip_text)), len(NEW.findall(base_text)))


def land_lines():
    L, ok = [], True
    tip = g('rev-parse', LAND).strip()
    commits = [c for c in g('rev-list', '%s..%s' % (JOIN_TIP, LAND)).split() if c]
    parents = g('log', '-1', '--format=%P', LAND).split()
    files = [f for f in g('diff', '--name-only', JOIN_TIP, LAND).split(NL) if f.strip()]
    one = len(commits) == 1 and parents == [JOIN_TIP] and files == [TIME]
    ok = ok and one
    L.append('  %s at %s: commits past %s %d ; the tip`s parents %s ; files changed %s -> %s' % (
        LAND, tip[:8], JOIN_TIP[:8], len(commits), [p[:8] for p in parents], files, 'ONE COMMIT, Time.lean ALONE' if one else 'NOT AS ORDERED'))
    eq, left, new_t, new_b = rename_read(show(JOIN_TIP, TIME), show(LAND, TIME))
    rn = eq and left == 0 and new_t == 4 and new_b == 0
    ok = ok and rn
    L.append('  %s: the tip`s text with each timeSRe read back as sRe equal to the base`s %s ; sRe left as a word %s ; timeSRe at the tip %s, at the base %s '
             '(the definition :18, its recursion :20, the statement :25-:26) -> %s' % (TIME, eq, left, new_t, new_b, 'THE RENAME ALONE' if rn else 'NOT THE RENAME ALONE'))
    s0, s1 = show(JOIN_TIP, SUMS), show(LAND, SUMS)
    l134 = (s1 or '').split(NL)[133] if s1 and len(s1.split(NL)) > 133 else ''
    sm = s0 is not None and s0 == s1 and bool(re.match(r'^\s*def sRe\b', l134))
    ok = ok and sm
    L.append('  %s: unchanged %s ; :134 declares sRe %s -> %s' % (SUMS, s0 == s1, bool(re.match(r'^\s*def sRe\b', l134)), 'KEEPS ITS NAME' if sm else 'NOT AS ORDERED'))
    p0, p1 = J.lines_at(JOIN_TIP), J.lines_at(LAND)
    pt = p0 is not None and p0 == p1
    ok = ok and pt
    L.append('  %s: %d lines at %s, %d at the tip, equal %s -> %s' % (NAMED, len(p0 or []), JOIN_TIP[:8], len(p1 or []), pt, 'UNCHANGED' if pt else 'CHANGED'))
    return L, ok, tip


def cmd_land():
    L, ok, _tip = land_lines()
    print(NL.join(L))
    print('### THE BRANCH: %s' % ('AS ORDERED' if ok else 'NOT AS ORDERED'))


# ================================================================================ (R368)(5): THE MERGE OF 596d1c9e ONTO THE LANDED MAIN
def libs_of(toml):
    """b757's libs_at read over a lakefile.toml text given (the working tree's, inside the merge). Pure."""
    out = []
    for blk in re.split(r'^\[\[', toml or '', flags=re.M)[1:]:
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


def _disk(path):
    p = os.path.join(EF, path)
    return io.open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.exists(p) else None


def resolve_names(names, rev=None):
    """{name: (module or None, [modules], why)}: each name's declaring module in the tree at rev, or, where rev is None, in the working tree's
    tracked Lean files on disk (inside the merge: the merged tree); b757's reader (decls_in, module_of) over either."""
    libs = J.libs_at(rev) if rev else libs_of(_disk('lakefile.toml'))
    texts, out = {}, {}
    for n in names:
        short = n.split('.')[-1]
        hit = g(*(['grep', '-n', '-E', '-e', J.DECL % J._esc(short)] + ([rev] if rev else []) + ['--', '*.lean']))
        if rev:
            files = sorted(set(h.split(':', 2)[1] for h in hit.split(NL) if h.count(':') >= 2))
        else:
            files = sorted(set(h.split(':', 1)[0] for h in hit.split(NL) if h.count(':') >= 1))
        files = [f for f in files if J.module_of(f, libs)]
        mods = []
        for f in files:
            if f not in texts:
                texts[f] = (g('show', '%s:%s' % (rev, f)) if rev else _disk(f)) or ''
            if n in J.decls_in(texts[f], short):
                mods.append(J.module_of(f, libs))
        mods = sorted(set(mods))
        out[n] = (mods[0] if len(mods) == 1 else None, mods, 'one' if len(mods) == 1 else 'NO DECLARATION FOUND' if not mods else 'MORE THAN ONE MODULE')
    return out


def union_lines(ours=None):
    ours = ours or g('rev-parse', 'refs/remotes/origin/main').strip()
    a, b = J.lines_at(ours), J.lines_at(COEFF_TIP)
    return ours, a, b, J.union_of([a, b])


def cmd_union(ours=None):
    ours, a, b, u = union_lines(ours)
    base = g('merge-base', ours, COEFF_TIP).strip()
    c = J.lines_at(base)
    print('  ours %s: %d lines ; 596d1c9e: %d lines ; their merge base %s: %d lines' % (ours[:8], len(a or []), len(b or []), base[:8], len(c or [])))
    print('  changed from the base: ours %s, theirs %s ; theirs new beside ours %d ; ours new beside theirs %d' % (
        a != c, b != c, len(set(b or []) - set(a or [])), len(set(a or []) - set(b or []))))
    print('### THE UNION OF BOTH SIDES: %d LINES, EACH ONCE' % len(u))


def cmd_resolve():
    br = g('symbolic-ref', '--short', 'HEAD').strip()
    merging = J.gr('rev-parse', '-q', '--verify', 'MERGE_HEAD').stdout.strip()
    con = J._conflicted()
    if br != COEFF or merging != COEFF_TIP or con != [NAMED]:
        sys.exit('### NOT RESOLVED, NOTHING WRITTEN: the branch %r (want %s) ; MERGE_HEAD %s (want 596d1c9e) ; conflicted %s (want [%r] alone)' % (
            br, COEFF, merging[:8] or 'none', con, NAMED))
    ours = g('rev-parse', 'HEAD').strip()
    _o, a, b, u = union_lines(ours)
    t = resolve_names(u)
    gone = [n for n in u if not t[n][1]]
    many = [n for n in u if len(t[n][1]) > 1]
    keep = [n for n in u if t[n][1]]
    p = os.path.join(EF, NAMED)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(keep) + NL)
    back = [l.strip() for l in io.open(p, encoding='utf-8').read().split(NL) if l.strip()]
    miss, extra, rep = J.compare(back, keep)
    for n in gone:
        print('  REMOVED, NO MODULE OF THE MERGED TREE DECLARES IT: %s' % n)
    for n in many:
        print('  KEPT, MORE THAN ONE MODULE: %s %s' % (n, t[n][1][:4]))
    print('  %s written within the merge of %s on %s: the union %d (ours %s %d, theirs %d) ; removed %d ; written %d ; read back: missing %d, extra %d, '
          'repeats %d -> %s' % (NAMED, merging[:8], COEFF, len(u), ours[:8], len(a or []), len(b or []), len(gone), len(keep), len(miss), len(extra), len(rep),
                               'DIFFERENCES 0' if not (miss or extra or rep) else 'DIFFERS'))
    print('  next: `commit.py SIDE-explicit-formula add %s`, then the commit route concludes the merge' % NAMED)


def check_coeff(rev=COEFF):
    tip = g('rev-parse', rev).strip()
    ps = g('log', '-1', '--format=%P', tip).split()
    if len(ps) != 2:
        return ['  %s at %s: NOT A MERGE (parents %s)' % (NAMED, tip[:8], [p[:8] for p in ps])], False
    raw = [l.strip() for l in J.gr('show', '%s:%s' % (tip, NAMED)).stdout.replace('\r', '').split(NL) if l.strip()]
    u = J.union_of([J.lines_at(ps[0]), J.lines_at(ps[1])])
    su, sr = set(u), set(raw)
    outside = [l for l in raw if l not in su]
    reps = len(raw) - len(sr)
    left = [l for l in u if l not in sr]
    tl = resolve_names(sorted(set(left) | sr), tip)
    left_bad = [l for l in left if tl[l][1]]
    kept_bad = [l for l in raw if not tl[l][1]]
    ok = not (outside or reps or left_bad or kept_bad)
    return ['  %s at %s: %d lines ; the union of its parents %s and %s: %d ; outside the union %d %s ; repeats %d ; left out %d, of them declared at the '
            'tip %d %s ; kept naming no declaration %d %s -> %s' % (NAMED, tip[:8], len(raw), ps[0][:8], ps[1][:8], len(u), len(outside), outside[:3], reps,
                                                                    len(left), len(left_bad), left_bad[:3], len(kept_bad), kept_bad[:3],
                                                                    'AS (5) ORDERS' if ok else 'NOT AS (5) ORDERS')] + [
        '    LEFT OUT, NO DECLARATION AT THE TIP: %s' % l for l in left if not tl[l][1]], ok


def coeff_merges():
    tip = g('rev-parse', COEFF).strip()
    ps = g('log', '-1', '--format=%P', tip).split()
    main_now = g('rev-parse', 'refs/remotes/origin/main').strip()
    past = [c for c in g('rev-list', '--first-parent', '%s..%s' % (ps[0], tip)).split() if c] if ps else []
    ok = len(ps) == 2 and ps[1] == COEFF_TIP and ps[0] == main_now and len(past) == 1
    return ['  %s at %s: parents %s ; the first the remote main %s %s ; the second 596d1c9e %s ; commits past the first parent %d -> %s' % (
        COEFF, tip[:8], [p[:8] for p in ps], main_now[:8], bool(ps) and ps[0] == main_now, len(ps) == 2 and ps[1] == COEFF_TIP, len(past),
        'ONE MERGE, AS ORDERED' if ok else 'NOT AS ORDERED')], ok, tip


FIVE = ('zq_coeff_not_multiplicative', 'cQ_forty_eight', 'cQ_not_nonneg', 'wide_detector', 'zq_arith_side_re_neg')   # ### (5): the names the run must print


def coeff_controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    lb0 = J.libs_at(COEFF_TIP)
    lb1 = libs_of(g('show', '%s:lakefile.toml' % COEFF_TIP))
    c('the libraries read over lakefile.toml`s text equal b757`s reader at 596d1c9e', lb1, lb1 == lb0 and bool(lb0))
    pt = J.lines_at(COEFF_TIP) or []
    full = [next((l for l in pt if l.split('.')[-1] == s), None) for s in FIVE]
    r5 = resolve_names([f for f in full if f], COEFF_TIP)
    c('the five names (5) wants printed, each a line of 596d1c9e`s print_targets.txt, each resolved to one module there',
      [(s, (r5.get(f) or (None,))[0]) for s, f in zip(FIVE, full)], all(full) and all(r5[f][0] for f in full))
    pl = resolve_names(['SIDEExplicitFormula.Schema.ZQ.noSuchDeclarationPlanted'], COEFF_TIP)
    c('a planted name declared nowhere read as no declaration', pl, list(pl.values())[0][2] == 'NO DECLARATION FOUND')
    u = J.union_of([['a', 'b', 'c'], ['b', 'd']])
    c('the union of two planted sides, ours first, each line once', u, u == ['a', 'b', 'c', 'd'])
    c('push-b757-coeff`s tip stands at 596d1c9e', g('rev-parse', COEFF_TIP).strip()[:8], g('rev-parse', COEFF_TIP).strip() == COEFF_TIP)
    return L, ok


def cmd_coeffbank():
    L, ok = coeff_controls()
    ml, mok, tip = coeff_merges()
    cl, cok = check_coeff(tip)
    t = J.targets_at(tip)
    bad = dict((n, v) for n, v in t.items() if v[0] is None)
    mods = sorted(set(v[0] for v in t.values() if v[0]))
    five = [(s, next((n for n in t if n.split('.')[-1] == s), None)) for s in FIVE]
    out = ['%s -- (R368)(5): T0, T1 AND THE WIDE DIRECTION MERGED ONTO THE LANDED MAIN, READ BEFORE THE DISPATCH (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '## THE MERGE ON %s' % COEFF] + ml + [
        '', '## THE MERGED %s AGAINST THE UNION OF BOTH SIDES, READ AGAINST THE TREE' % NAMED] + cl + [
        '', '## THE DISPATCH`S TARGETS: THE MODULE DECLARING EACH LINE OF %s AT THE TIP %s (tools/b757_join.py`s reader)' % (NAMED, tip[:8])] + [
        '  REFUSED %s: %s %s' % (n, v[2], v[1][:4]) for n, v in sorted(bad.items())] + [
        '  the five names (5) wants printed: %s' % ' ; '.join('%s %s' % (s, 'a line, its module %s' % t[n][0] if n else 'NOT A LINE') for s, n in five),
        '  names %d ; resolved to one module %d ; refused %d ; modules %d:' % (len(t), len(t) - len(bad), len(bad), len(mods)), '  ' + ' '.join(mods), '',
        '### ### **THE MERGE: %s ; THE UNION %s ; TARGETS %d MODULES FOR %d NAMES, %d REFUSED ; THE FIVE NAMES LINES %d OF 5 ; CONTROLS %d OF %d.**' % (
            'AS ORDERED' if mok else 'NOT AS ORDERED', 'AS (5) ORDERS' if cok else 'NOT AS (5) ORDERS', len(mods), len(t), len(bad),
            sum(1 for _s, n in five if n and t[n][0]), sum(ok), len(ok))]
    r = FB.write(COEFF_BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b758_coeff.txt ; figbank: %s' % r['why'])
    if not (mok and cok and all(ok) and not bad and all(n and t[n][0] for _s, n in five)):
        sys.exit('### THE MERGE, THE UNION, THE FIVE NAMES OR THE CONTROLS NOT AS WANTED -- NO TARGETS FILE WRITTEN')
    tj = dict(rev=tip, branch=COEFF, names=len(t), modules=mods, refused=sorted(bad), union_ok=cok, merges_ok=mok, at=_now())
    tmp = COEFF_JSON + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(tj, f, ensure_ascii=False, indent=1)
        f.write(NL)
    os.replace(tmp, COEFF_JSON)
    print('written data/b758_coeff_targets.json: rev %s ; modules %d ; refused %d' % (tip[:8], len(mods), len(bad)))


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    base = 'def sRe (r : Q) : N\n  | n + 1 => sRe r n + 1\ntheorem time_sRe_18 : sRe 1 92 = 0 := x\n-- foo.sRe kept\n'
    good = base.replace('def sRe', 'def timeSRe').replace('=> sRe', '=> timeSRe').replace(': sRe 1', ': timeSRe 1')
    c('the rename read on a planted file: three uses renamed, the theorem`s own name and a dotted name kept', rename_read(base, good),
      rename_read(base, good) == (True, 0, 3, 0))
    half = base.replace('def sRe', 'def timeSRe')
    c('a planted half rename refused (sRe left as a word)', rename_read(base, half), rename_read(base, half)[1] > 0)
    more = good.replace('= 0 := x', '= 1 := x')
    c('a planted rename that also changes a statement refused (not equal after the read back)', rename_read(base, more)[0], rename_read(base, more)[0] is False)
    pos = J.targets_at(JOIN_TIP)
    dup = [n for n, v in pos.items() if v[0] is None]
    c('the reader at 6568e9c7, as b757`s bank read it: 419 names, each resolved to one module', (len(pos), dup), len(pos) == 419 and not dup)
    c('push-b757-join`s tip stands at 6568e9c7 in the kernel', g('rev-parse', JOIN_TIP).strip()[:8], g('rev-parse', JOIN_TIP).strip() == JOIN_TIP)
    c('main stands at 8fbab45d, unmoved', g('rev-parse', 'main').strip()[:8], g('rev-parse', 'main').strip() == J.MAIN)
    return L, ok


def cmd_bank():
    L, ok = controls()
    bl, bok, tip = land_lines()
    t = J.targets_at(tip)
    bad = dict((n, v) for n, v in t.items() if v[0] is None)
    mods = sorted(set(v[0] for v in t.values() if v[0]))
    out = ['%s -- (R368)(4): THE JOIN LANDED IN SIDE-explicit-formula, READ BEFORE ITS DISPATCH (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '## THE BRANCH %s, ITS ONE COMMIT' % LAND] + bl + [
        '', '## THE DISPATCH`S TARGETS: THE MODULE DECLARING EACH LINE OF %s AT THE TIP %s (tools/b757_join.py`s reader)' % (NAMED, tip[:8])] + [
        '  REFUSED %s: %s %s' % (n, v[2], v[1][:4]) for n, v in sorted(bad.items())] + [
        '  names %d ; resolved to one module %d ; refused %d ; modules %d:' % (len(t), len(t) - len(bad), len(bad), len(mods)), '  ' + ' '.join(mods), '',
        '### ### **THE LANDING`S BRANCH: %s ; TARGETS %d MODULES FOR %d NAMES, %d REFUSED ; CONTROLS %d OF %d.**' % (
            'AS ORDERED' if bok else 'NOT AS ORDERED', len(mods), len(t), len(bad), sum(ok), len(ok))]
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b758_land.txt ; figbank: %s' % r['why'])
    if not (bok and all(ok) and not bad):
        sys.exit('### THE BRANCH OR THE CONTROLS NOT AS WANTED -- NO TARGETS FILE WRITTEN')
    tj = dict(rev=tip, branch=LAND, names=len(t), modules=mods, refused=sorted(bad), union_ok=True, merges_ok=bok, at=_now(),
              note='union_ok: print_targets.txt unchanged from 6568e9c7 (no union at (4)); merges_ok: the one commit as (4) orders')
    tmp = TARGETS_JSON + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(tj, f, ensure_ascii=False, indent=1)
        f.write(NL)
    os.replace(tmp, TARGETS_JSON)
    print('written data/b758_land_targets.json: rev %s ; modules %d ; refused %d' % (tip[:8], len(mods), len(bad)))


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'land': cmd_land, 'bank': cmd_bank, 'control': lambda: print(NL.join(controls()[0])), 'union': cmd_union, 'resolve': cmd_resolve,
          'check': lambda rev=COEFF: print(NL.join(check_coeff(rev)[0])), 'merges': lambda: print(NL.join(coeff_merges()[0])), 'coeffbank': cmd_coeffbank,
          'coeffcontrol': lambda: print(NL.join(coeff_controls()[0]))}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
