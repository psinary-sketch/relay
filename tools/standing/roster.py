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
ADDED = os.path.join(A.T, 'mirror_roster_added.json')
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


def added():
    """b753, (R363)(6)[M1], passed by the author 2026-11-11 (data/b753_rules.txt (1)): the families added by a ruling, a list of its own beside
    the base roster, which stays unedited. [] where the list does not stand."""
    if not os.path.isfile(ADDED):
        return []
    with open(ADDED, encoding='utf-8') as f:
        return [norm(p) for p in json.load(f)['files']]


def main_tree(rev='main'):
    """PLACE-papers' tree at `rev` (main, or the source head a build declared), its paths."""
    out = A.gs('pp', 'ls-tree', '-r', '--name-only', rev) or ''
    return [p for p in out.split(NL) if p.strip()]


def roster_at(rev='main'):
    """the roster the builder reads, from the base roster's families and PLACE-papers' tree at `rev` (the class repair (3)(iii): the
    mirror's verifier reads this roster, at the source head the build's MANIFEST declares, not the base roster alone)."""
    return resolve(base(), main_tree(rev), added())[0]


def build_joins(act):
    """the joins an act's mirror build printed (data/<act>_mirror_build.json `out`, its JOINS rows) and the source head it built from."""
    j = A.jl('%s_mirror_build.json' % act)
    return re.findall(r'^  JOINS (\S+)', j.get('out') or '', re.M), j.get('pp_head')


def resolve(b, tree, add=None):
    """the roster from the b707 roster `b` and main's tree: (roster, joins [(path, family, reason)], leaves [(path, reason)], not joined
    [(path, family, reason)]). With `add` (the families added by a ruling, b753 [M1]): the base roster's entries and their joins keep their
    slots, and each added family follows them in the list's order with its later editions, read by the same rule."""
    if add:
        r0, j0, l0, n0 = resolve(b, tree)
        fresh = [p for p in add if p not in b and family(p) not in set(family(x) for x in b)]
        r1, j1, l1, n1 = resolve(fresh, tree)
        return r0 + [p for p in r1 if p not in r0], j0 + j1, l0 + l1, n0 + n1
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
    ad = added()
    r, joins, leaves, nj = resolve(b, tree, ad)
    head = A.gs('pp', 'rev-parse', '--short', 'main')
    L = ['### THE ROSTER READ FROM PLACE-papers MAIN %s BY FAMILY (the roster rule of the rules bank): the base roster (tools/mirror_roster.json) '
         '%d entries in %d families ; the roster %d entries' % (head, len(b), len(set(family(p) for p in b)), len(r))]
    if ad:
        L.append('### THE FAMILIES ADDED BY A RULING (tools/mirror_roster_added.json; b753, (R363)(6)[M1], data/b753_rules.txt (1)): %d listed ; in the roster %d, '
                 'after the base roster`s entries and their joins' % (len(ad), sum(1 for p in ad if p in r)))
        L += ['  FAMILY ADDED %s  (family %s ; %s)' % (p, family(p), 'in the roster at slot %d' % (r.index(p) + 1) if p in r else '### NOT IN THE ROSTER: absent on main, or its family already carried')
              for p in ad]
    L += ['  JOINS %s  (family %s ; %s)' % (p, f, why) for p, f, why in joins] or ['  JOINS none']
    L += ['  LEAVES %s  (%s)' % (p, why) for p, why in leaves] or ['  LEAVES none']
    L += ['  NOT JOINED %s  (family %s ; %s)' % (p, f, why) for p, f, why in nj]
    plus, removed = sorted(set(r) - set(b)), sorted(set(b) - set(r))
    L.append('### THE DIFF AGAINST THE BASE ROSTER (tools/mirror_roster.json, lastChanged %s): added %d %s ; removed %d %s' % (
        json.load(open(BASE, encoding='utf-8')).get('lastChanged'),
        len(plus), plus or '', len(removed), removed or ''))
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
    # ### v1.1.0: the record's joins read from the previous act's build bank at the source head it built from (v1.0.0 wrote the two joins
    # ### of its own act's main into the case, and main has gained an edition since)
    prev = A.prev_of(A.current()['act'])
    bj, bhead = build_joins(prev)
    case('RECORD', '%s`s build at its source head: the joins as its build printed them' % prev,
         ([j[0] for j in resolve(b, main_tree(bhead), added())[1]] if bhead else None), bj)
    # ### b753 [M1]: the families added by a ruling follow the base roster's entries and joins, in the list's order; the rule is otherwise b715's
    ad = added()
    if ad:
        ra = resolve(b, tree, ad)[0]
        case('RECORD', 'the families added by a ruling (%d): the base roster`s entries and joins keep their slots, the added follow in the list`s order' % len(ad),
             (ra[:len(r)] == r, [p for p in ra[len(r):] if p in ad] == [p for p in ad if p in tree]), (True, True))
    pl = ['phase9/x/PLANTED_FAMILY_v0_1.md']
    rp = resolve(b, tree + pl + ['phase9/x/PLANTED_FAMILY_v0_2.md'], pl)
    case('CONSTRUCTED', 'a planted added family with a later edition on the tree: both enter after every base slot, the later edition a join',
         (rp[0][:len(r)] == r, rp[0][len(r):], [j[0] for j in rp[1] if 'PLANTED' in j[0]]), (True, pl + ['phase9/x/PLANTED_FAMILY_v0_2.md'], ['phase9/x/PLANTED_FAMILY_v0_2.md']))
    case('CONSTRUCTED', 'a planted added family absent on the tree: it leaves, nothing enters ; one whose family the base roster carries: not taken twice',
         (resolve(b, tree, pl)[0] == r, [x[0] for x in resolve(b, tree, pl)[2]], resolve(b, tree, [b[0]])[0] == r), (True, pl, True))
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
