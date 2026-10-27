# -*- coding: utf-8 -*-
"""standing/roster.py -- THE MIRROR'S ROSTER, READ FROM PLACE-papers MAIN AT BUILD TIME ((R325)(5) of the toolset act, on the author's word
(2) there, the rule data/b715_rules.txt (1)).

The rule: the roster is the b707 roster's families, read from main; a file on main joins when it is a new edition of a family already in
the roster; no family is added or dropped by this rule; a new family enters only by a ruling. The definition of "current edition" stays the
author's to rule; until then every edition in a family is carried.
As read here: the b707 roster is relay tools/mirror_roster.json, kept unedited as the families' source; a family is a roster path with its
`_v<n>[_<n>...]` suffix removed; a file on main joins when it is in a family the roster carries and its filename's version is above the
newest filename version the roster carries in that family, appended at the roster's end so no slot changes; a roster file absent on main
leaves; an edition older than the family's newest carried, or in a family the roster carries only unversioned, does not join and is printed
for the author's ruling. The excluded archive kinds, the flat names and MANIFEST's columns are the builder's, untouched.

  python -X utf8 tools/standing/roster.py print      the joins, the leaves, the editions not joined and the diff against the b707 roster
  python -X utf8 tools/standing/roster.py json       the roster as JSON {files: [...]}, for the builder (tools/mirror_build.ps1)
  python -X utf8 tools/standing/roster.py control    the rule's controls, record and constructed; prints
  python -X utf8 tools/standing/roster.py bank       print's lines and the controls, banked as data/<act>_roster.txt
"""
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

NL = '\n'
BASE = os.path.join(A.T, 'mirror_roster.json')
VER = re.compile(r'_v(\d+(?:_\d+)*)(\.md)$')


def norm(p):
    return p.replace('\\', '/')


def family(p):
    return VER.sub(r'\2', norm(p))


def vkey(p):
    m = VER.search(norm(p))
    return tuple(int(x) for x in m.group(1).split('_')) if m else None


def base():
    with open(BASE, encoding='utf-8') as f:
        return [norm(p) for p in json.load(f)['files']]


def main_tree():
    out = A.gs('pp', 'ls-tree', '-r', '--name-only', 'main') or ''
    return [p for p in out.split(NL) if p.strip()]


def resolve(b, tree):
    """the roster from the b707 roster `b` and main's tree: (roster, joins [(path, family, reason)], leaves [(path, reason)], not joined
    [(path, family, reason)])."""
    on = set(tree)
    kept = [p for p in b if p in on]
    leaves = [(p, 'absent on main') for p in b if p not in on]
    fams = []
    for p in b:
        if family(p) not in fams:
            fams.append(family(p))
    joins, nj = [], []
    for f in fams:
        carried = [vkey(p) for p in b if family(p) == f and vkey(p) is not None]
        newest = max(carried) if carried else None
        for m in sorted((p for p in tree if family(p) == f and p not in b), key=lambda p: vkey(p) or ()):
            k = vkey(m)
            if k is not None and newest is not None and k > newest:
                joins.append((m, f, 'filename edition v%s above the family`s newest carried v%s' % (
                    '.'.join(map(str, k)), '.'.join(map(str, newest)))))
            elif k is None:
                nj.append((m, f, 'unversioned by its filename; the family carries %s' % (
                    'v' + '.'.join(map(str, newest)) if newest else 'no versioned edition')))
            elif newest is None:
                nj.append((m, f, 'v%s, the family carried only unversioned: "current edition" the author`s to rule' % '.'.join(map(str, k))))
            else:
                nj.append((m, f, 'v%s, not above the family`s newest carried v%s' % ('.'.join(map(str, k)), '.'.join(map(str, newest)))))
    return kept + [j[0] for j in joins], joins, leaves, nj


def print_lines(b=None, tree=None):
    b = base() if b is None else b
    tree = main_tree() if tree is None else tree
    r, joins, leaves, nj = resolve(b, tree)
    head = A.gs('pp', 'rev-parse', '--short', 'main')
    L = ['### THE ROSTER READ FROM PLACE-papers MAIN %s BY FAMILY (the roster rule of the rules bank): the base roster (tools/mirror_roster.json) '
         '%d entries in %d families ; the roster %d entries' % (head, len(b), len(set(family(p) for p in b)), len(r))]
    L += ['  JOINS %s  (family %s ; %s)' % (p, f, why) for p, f, why in joins] or ['  JOINS none']
    L += ['  LEAVES %s  (%s)' % (p, why) for p, why in leaves] or ['  LEAVES none']
    L += ['  NOT JOINED %s  (family %s ; %s)' % (p, f, why) for p, f, why in nj]
    added, removed = sorted(set(r) - set(b)), sorted(set(b) - set(r))
    L.append('### THE DIFF AGAINST THE BASE ROSTER (tools/mirror_roster.json, lastChanged %s): added %d %s ; removed %d %s' % (
        json.load(open(BASE, encoding='utf-8')).get('lastChanged'),
        len(added), added or '', len(removed), removed or ''))
    return L, r


def control_lines():
    b = base()
    tree = main_tree()
    out, res = [], []

    def case(kind, what, got, want):
        res.append(got == want)
        out.append('  %-11s %s : got %s ; wanted %s ; %s' % (kind, what, got, want, 'AS WANTED' if got == want else '### NOT AS WANTED'))
    r, joins, leaves, nj = resolve(b, tree)
    census = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md'
    case('RECORD', 'main`s tree: the joins', [j[0] for j in joins],
         ['phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', census])
    case('RECORD', 'main`s tree: the census v0.8.1 and day1/Silence_of_Foundations.md in the roster', (census in r, 'day1/Silence_of_Foundations.md' in r), (True, True))
    case('RECORD', 'main`s tree: leaves ; families before and after', (len(leaves), len(set(family(p) for p in b)), len(set(family(p) for p in r))),
         (0, len(set(family(p) for p in b)), len(set(family(p) for p in b))))
    gone = 'day1/Spectral_Inertness.md'
    r2, _j, l2, _n = resolve(b, [p for p in tree if p != gone])
    case('CONSTRUCTED', 'a tree without %s: it leaves the roster, nothing else changes' % gone, ([x[0] for x in l2], len(r) - len(r2)), ([gone], 1))
    newfam = 'phase2/method/A_NEW_FAMILY_v0_1.md'
    r3, j3, _l, _n = resolve(b, tree + [newfam])
    case('CONSTRUCTED', 'a tree with a file of no roster family: not added (a new family enters only by a ruling)', (newfam in r3, len(r3) == len(r)), (False, True))
    newed = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md'
    r4, j4, _l, _n = resolve(b, tree + [newed])
    case('CONSTRUCTED', 'a tree with a newer edition of a carried family: it joins after every kept slot (the slots unchanged)',
         (newed in r4 and r4.index(newed) >= len(b), r4[:len(b)] == b, newed in [j[0] for j in j4]), (True, True, True))
    old = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md'
    case('RECORD', 'an older edition on main (%s): not joined' % old, old in r, False)
    out.append('### ### **ROSTER CONTROLS %d ; AS WANTED %d ; ALL AS WANTED %s.**' % (len(res), sum(res), all(res)))
    return out, all(res)


def main(route):
    if route == 'json':
        _L, r = print_lines()
        if not r:
            sys.exit('### THE ROSTER READ FROM MAIN IS EMPTY -- NOTHING PRINTED')
        print(json.dumps({'files': [p.replace('/', '\\') for p in r]}))
        return 0
    L, _r = print_lines()
    if route in ('control', 'bank'):
        c, ok = control_lines()
        L += ['', '### THE RULE`S CONTROLS:'] + c
    if route == 'bank':
        cur = A.current()
        p = os.path.join(A.D, '%s_roster.txt' % cur['act'])
        head = ['%s -- THE MIRROR`S ROSTER READ FROM MAIN, ITS JOINS AND ITS CONTROLS (%s)' % (cur['act'], time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
                '### Written by tools/standing/roster.py bank (the roster rule of data/%s_rules.txt (1)).' % cur['act'], '']
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(head + L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'print'))
