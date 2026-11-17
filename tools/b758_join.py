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
    fn = {'land': cmd_land, 'bank': cmd_bank, 'control': lambda: print(NL.join(controls()[0]))}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
