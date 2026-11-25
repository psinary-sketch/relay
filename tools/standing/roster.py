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
  python -X utf8 tools/standing/roster.py project [<rev>]   the Project set's lines for the builder's MANIFEST (v1.34.5, rules (14)-(16))
  python -X utf8 tools/standing/roster.py second <stage>    the second source copied into the builder's stage, its rows and line as JSON
                                                            (v1.35.3, (R366)(6), [H1]'s held part: the relay's HANDOFF.md)

v1.34.5, (R364)(5)[M2], passed by the author 2026-11-13 at the put relay data/b754_put_7.json (data/b754_author_answers.txt :153; the
rules data/b754_rules.txt (13)-(17)). (a) THE CURRENT EDITION, rule (13): from b754's mirror on, each family the roster carries is
carried by its current edition alone, the file on main whose own version line is the highest in the family, whatever its filename; a
family where a file's version line is not read, or two share the highest, stays as the rule above carries it, printed UNDECIDED. The
current edition takes the slot of the family's first carried path, so no other slot moves. A build of an act before b754 is read as it
was built (roster_at's `act`). (b) THE PROJECT SET, rule (14): tools/mirror_project_set.json, a list of its own, each path read as its
family's current edition. (c) rule (15): the `project` route prints the set under the builder's MANIFEST table, each file's bytes and
the total; by rule (16) the two cuts of tools/standing/cuts.py stand in place of FINDINGS.md whole, both totals printed.

v1.34.8, W-ORD-LABEL-READER (OPEN_TRAILS :13605, entered at b644), placed HERE at b756 under (R366)(5)(i) and passed by the author at the
put (relay data/b756_orders_read.txt (3); data/b756_author_answers.txt :4, :18): a version string is a document's label only where it sits
on the document's own label line, never where it follows a kernel's name. version_of passes over a heading's version string that follows a
kernel's name (after_kernel, label_on) for the next on the line; a heading with none other is not the version line and the read goes on.
The other rules are unchanged. Its controls: tools/standing/v1348.py, ONE_PAGE_PROOF's kernel tag planted as a heading at its head.

v1.38.30, (R379)(8) [K30], W-ORD-MAP-MERGE, b769: THE MAP'S ONE NAME. From b769's mirror on the family SPIRAL_MAP.md is carried by its one
name, SPIRAL_MAP.md, whatever the two files' version lines read (they tie at v0.7 after (R379)(4)(b)'s merge); SPIRAL_MAP_v0_7.md stands as
an edition and no roster of b769 on carries it; apply_current refuses a roster of b769 on that carries another name of the family
(one_name_refusal), before any route prints or builds from it. A build of an act before b769 is read as it was built. Its control: relay
tools/b769_repair_controls.py K30.
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


def added(act=None):
    """b753, (R363)(6)[M1], passed by the author 2026-11-11 (data/b753_rules.txt (1)): the families added by a ruling, a list of its own beside
    the base roster, which stays unedited. [] where the list does not stand. v1.34.5: the entries carried from the mirror of `act` (default
    the current act), each read by the list's `added_at` (an entry it does not name added at b753), so a replay of an earlier build reads the
    list as that act built it."""
    if not os.path.isfile(ADDED):
        return []
    with open(ADDED, encoding='utf-8') as f:
        j = json.load(f)
    at = j.get('added_at') or {}
    n = act_number(act)
    return [norm(p) for p in j['files'] if act_number(at.get(p, 'b753')) <= n]


def main_tree(rev='main'):
    """PLACE-papers' tree at `rev` (main, or the source head a build declared), its paths."""
    out = A.gs('pp', 'ls-tree', '-r', '--name-only', rev) or ''
    return [p for p in out.split(NL) if p.strip()]


def roster_at(rev='main', act=None):
    """the roster the builder reads, from the base roster's families and PLACE-papers' tree at `rev` (the class repair (3)(iii): the
    mirror's verifier reads this roster, at the source head the build's MANIFEST declares, not the base roster alone). v1.34.5: for a
    build of `act` (default the current act) from b754 on, the current edition of rule (13) applied."""
    tree = main_tree(rev)
    r = resolve(base(), tree, added(act))[0]
    return apply_current(r, tree, rev, act=act)[0] if current_rule(act) else r


# ================================================================================ v1.34.5, (R364)(5)[M2] (a) to (c), b754
PROJECT = os.path.join(A.T, 'mirror_project_set.json')
CURRENT_FROM = 754   # ### rule (13) of data/b754_rules.txt: in force from b754's mirror
# ### a file's own version line, as the [M2] put read it (tools/b754_agenda.py :84-:88 at relay d6d6f88e): the first 40 lines' version
# ### line, else the file's first edition note "*v<n>.<n>[.<n>], <date>" at any line
VREAD = [re.compile(r'^\W{0,4}v(\d+(?:\.\d+)+)\b'), re.compile(r'(?i)^\W{0,4}version\W{0,6}v?(\d+(?:\.\d+)+)\b'),
         re.compile(r'^#{1,3}\s.*?\bv(\d+(?:\.\d+)+)\b')]
EDNOTE = re.compile(r'^\*v(\d+(?:\.\d+)+), 20\d\d-')
# ================================================================================ v1.34.8, W-ORD-LABEL-READER, b756 (R366)(5)(i)
# ### VSTR: each version string on a line. KERNEL_BEFORE: a kernel's name (SIDE-<name>, the name of every kernel clone the worklist lists)
# ### ending the text before a version string, parted from it by spaces, backticks, a possessive, a colon, "@", a comma or an opening
# ### bracket, and at most one of the words at, tag, main.
VSTR = re.compile(r'\bv(\d+(?:\.\d+)+)\b')
KERNEL_BEFORE = re.compile(r"\bSIDE-[A-Za-z0-9][A-Za-z0-9-]*(?:[`’']s)?[\s`:@,(’']*(?:(?:at|tag|main)\s+)?`?$")


def after_kernel(line, start):
    """v1.34.8: True where the text of `line` before `start` ends with a kernel's name (KERNEL_BEFORE)."""
    return bool(KERNEL_BEFORE.search(line[:start]))


def label_on(line, m, rx):
    """v1.34.8: the version tuple a VREAD match `m` gives as the document's label, or None. For the heading rule (VREAD[2]) the first
    version string on the line that follows no kernel's name; for the other rules the match itself, as before."""
    if rx is not VREAD[2]:
        return tuple(int(x) for x in m.group(1).split('.'))
    for mm in VSTR.finditer(line):
        if not after_kernel(line, mm.start()):
            return tuple(int(x) for x in mm.group(1).split('.'))
    return None


def act_number(act=None):
    a = act or A.current()['act']
    m = re.match(r'^b(\d+)$', a)
    if not m:
        raise SystemExit('### THE ACT %r NOT READ AS b<N>' % a)
    return int(m.group(1))


def current_rule(act=None):
    return act_number(act) >= CURRENT_FROM


# ================================================================================ v1.38.30, (R379)(8) [K30], b769: THE MAP'S ONE NAME
# ### W-ORD-MAP-MERGE (the papers' OPEN_TRAILS :19227, [M4] at :19225, (R376)(6)(a)) and (R379)(4)(b): SPIRAL_MAP.md carries the map. b769's
# ### merge set into it the 81 lines SPIRAL_MAP_v0_7.md alone held (relay data/b769_map_merge.txt), so the two files' own version lines tie
# ### at v0.7 and rule (13) alone would carry both. From b769's mirror on the family is carried by its one name, whatever the version lines
# ### read; SPIRAL_MAP_v0_7.md stands as an edition and is carried by no roster of b769 on. A build of an act before b769 is read as built.
ONE_NAME_FROM = 769
ONE_NAME = {'SPIRAL_MAP.md': 'SPIRAL_MAP.md'}   # ### the family -> its one name
ONE_NAME_RULE, ONE_NAME_VERSION = '(R379)(8) [K30]', 'v1.38.30'


def one_name_rule(act=None):
    return act_number(act) >= ONE_NAME_FROM


def one_name_refusal(r, act=None):
    """v1.38.30, [K30]: the refusal's words where the roster `r` of an act from b769 on carries a name of a ONE_NAME family other than its
    one name, the edition beside the map or alone; else None."""
    if not one_name_rule(act):
        return None
    bad = [norm(p) for p in r if family(p) in ONE_NAME and norm(p) != ONE_NAME[family(p)]]
    if not bad:
        return None
    return '### THE ROSTER CARRIES %s, WHERE THE FAMILY`S ONE NAME IS %s (%s, %s, W-ORD-MAP-MERGE) -- REFUSED, NOTHING PRINTED OR BUILT' % (
        ', '.join(bad), ', '.join(sorted(set(ONE_NAME[family(p)] for p in bad))), ONE_NAME_RULE, ONE_NAME_VERSION)


def version_of(text_lines):
    """(line, version tuple) of a file's own version line, or (None, None). v1.34.8: a heading's version string after a kernel's name is
    not the document's label (label_on); a heading carrying no other is passed over."""
    for k, l in enumerate(text_lines[:40], 1):
        for rx in VREAD:
            m = rx.match(l)
            if m:
                v = label_on(l, m, rx)
                if v:
                    return k, v
                break
    for k, l in enumerate(text_lines, 1):
        m = EDNOTE.match(l)
        if m:
            return k, tuple(int(x) for x in m.group(1).split('.'))
    return None, None


def text_at(rev, path):
    b = A.blob(rev, path, 'pp')
    return None if b is None else b.decode('utf-8', 'replace').replace('\r', '').split(NL)


def current_editions(r, tree, rev, reader=None, act=None):
    """for each family of the roster `r`: (family, candidates on the tree, carried, {path: (line, version)}, current or None, why). The
    current edition is the one candidate where the family has one; else the candidate whose own version line is the highest, every
    candidate's line read and no two sharing the highest; else None, the family undecided. `reader(path)` gives a file's lines (default
    its blob at `rev`). v1.38.30, [K30]: for an act from b769 on (`act`, default the current act) a ONE_NAME family's current edition is
    its one name where the tree holds it, whatever the version lines read; where it does not, the family is undecided."""
    reader = reader or (lambda p: text_at(rev, p) or [])
    one = one_name_rule(act)
    fams = []
    for p in r:
        if family(p) not in fams:
            fams.append(family(p))
    md = [p for p in tree if p.endswith('.md')]
    rows = []
    for f in fams:
        cands = sorted(p for p in md if family(p) == f)
        present = [p for p in r if family(p) == f]
        vers = dict((p, version_of(reader(p))) for p in cands) if len(cands) > 1 else {}
        if one and f in ONE_NAME:
            cur, why = (ONE_NAME[f], 'the family`s one name (%s, %s, W-ORD-MAP-MERGE)' % (ONE_NAME_RULE, ONE_NAME_VERSION)) if ONE_NAME[f] in cands else (
                None, 'the family`s one name %s not on the tree (%s)' % (ONE_NAME[f], ONE_NAME_RULE))
        elif len(cands) == 1:
            cur, why = cands[0], 'one file'
        elif cands and all(vers[p][1] for p in cands):
            top = max(vers[p][1] for p in cands)
            best = [p for p in cands if vers[p][1] == top]
            cur, why = (best[0], 'its own version line above every other of the family') if len(best) == 1 else (
                None, 'a tie at v%s: %s' % ('.'.join(map(str, top)), ', '.join(best)))
        else:
            cur, why = None, ('no version line read in %s' % ', '.join(p for p in cands if not vers[p][1])) if cands else 'no file on the tree'
        rows.append((f, cands, present, vers, cur, why))
    return rows


def apply_current(r, tree, rev, reader=None, act=None):
    """the roster `r` with rule (13) applied: each decided family carried by its current edition at its first slot; (roster, rows).
    v1.38.30, [K30]: `act` (default the current act) gates the one name, and a roster of b769 on that carries another name of a ONE_NAME
    family is refused here, before any route prints or builds from it."""
    rows = current_editions(r, tree, rev, reader, act)
    cur = dict((f, c) for f, _c, _p, _v, c, _w in rows if c)
    out, seen = [], set()
    for p in r:
        f = family(p)
        if f in cur:
            if f not in seen:
                seen.add(f)
                out.append(cur[f])
        else:
            out.append(p)
    x = one_name_refusal(out, act)
    if x:
        raise SystemExit(x)
    return out, rows


def project_list():
    with open(PROJECT, encoding='utf-8') as f:
        return [norm(p) for p in json.load(f)['files']]


def size_at(rev, path):
    s = A.gs('pp', 'cat-file', '-s', '%s:%s' % (rev, path))
    return int(s) if s and s.isdigit() else None


def project(rev='main', act=None, with_cuts=True):
    """the Project set at `rev` (rules (14) and (16)): rows [(name, bytes, note)], the total by (b), the total by (b) and (d), the cuts`
    figures and their meta."""
    tree = main_tree(rev)
    r0 = resolve(base(), tree, added())[0]
    rr, rows_c = (apply_current(r0, tree, rev, act=act) if current_rule(act) else (r0, []))
    cur = dict((f, c) for f, _c, _p, _v, c, _w in rows_c if c)
    rows, seen = [], set()
    for p in project_list():
        if p == 'MANIFEST':
            rows.append(('MANIFEST', None, 'the build`s own'))
            continue
        q = cur.get(family(p), p)
        if q in seen:
            continue
        seen.add(q)
        rows.append((q, size_at(rev, q), ('the current edition of %s' % p if q != p else 'in the archive') if q in rr else '### NOT IN THE ARCHIVE'))
    if act_number(act) >= SECOND_FROM:   # ### v1.35.3, (R366)(6), [H1]'s held part: the relay's page, by the second source
        for p, b in second_rows():
            rows.append((p, len(b), 'in the archive by the second source, the relay`s HEAD ([H1], (R366)(6))'))
    by_b = sum(b for _n, b, _w in rows if b)
    fig, meta, cut_rows = [], {}, []
    if with_cuts:
        import cuts as CU
        cuts, fig, meta = CU.build(rev, act)
        cut_rows = [(n, CU.nbytes(cuts[n]), 'rule (16), beside the archive') for n in CU.NAMES]
    f_b = next((b for n, b, _w in rows if n == 'FINDINGS.md'), 0) or 0
    by_bd = by_b - f_b + sum(b for _n, b, _w in cut_rows) if with_cuts else None
    return rows, by_b, by_bd, cut_rows, fig, meta


def project_lines(rev='main', act=None):
    rows, by_b, by_bd, cut_rows, fig, _m = project(rev, act)
    head = A.gs('pp', 'rev-parse', '--short=8', rev)
    L = ['', '## THE PROJECT SET', '',
         'Rules (14) to (16) of relay data/b754_rules.txt ((R364)(5)[M2]): tools/mirror_project_set.json read by tools/standing/roster.py at '
         'PLACE-papers `%s`, each path as its family`s current edition; by rule (16) the two cuts stand in place of FINDINGS.md whole.' % head, '',
         '| Project file | bytes | note |', '|:--|--:|:--|']
    for n, b, w in rows:
        if n == 'FINDINGS.md' and cut_rows:
            w = 'in the archive whole; in the Project set by its cut (rule (16))'
        L.append('| %s | %s | %s |' % (n, '-' if b is None else b, w))
    for n, b, w in cut_rows:
        L.append('| %s | %d | %s |' % (n, b, w))
    L += ['', 'THE PROJECT SET`S TOTAL, MANIFEST apart: by rule (14) %d bytes ; by rules (14) and (16), the two cuts in place of FINDINGS.md whole, '
          '%s bytes. Read beside the Project`s capacity by the navigator at every refresh (rule (15)).' % (by_b, by_bd if by_bd is not None else '-')]
    miss = [n for n, _b, w in rows if w.startswith('###')]
    if miss:
        L.append('### NOT IN THE ARCHIVE: %s' % ', '.join(miss))
    return L + [''] + ['    ' + x for x in fig]


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


def vtxt(vers, p):
    k, v = vers.get(p, (None, None))
    return ('its own line v%s at :%d' % ('.'.join(map(str, v)), k)) if v else 'its own line not read'


def current_lines(rows, r):
    """v1.34.5: the lines rule (13) adds to the print, each family by its current edition or UNDECIDED."""
    dec = [x for x in rows if x[4]]
    und = [x for x in rows if not x[4] and len(x[1]) > 1]
    L = ['### THE CURRENT EDITION (rule (13) of data/b754_rules.txt; (R364)(5)[M2] (a)), from b754`s mirror on: families %d ; decided %d '
         '(one file %d) ; undecided %d ; the roster %d entries' % (len(rows), len(dec), sum(1 for x in dec if len(x[1]) == 1), len(und), len(r))]
    for f, cands, present, vers, cur, why in dec:
        if len(cands) < 2:
            continue
        if cur not in present:
            L.append('  JOINS BY EDITION %s  (family %s ; %s ; %s)' % (cur, f, vtxt(vers, cur), why))
        for p in present:
            if p != cur:
                L.append('  LEAVES BY EDITION %s  (family %s ; %s ; the current edition %s)' % (p, f, vtxt(vers, p), cur))
    for f, cands, present, vers, cur, why in und:
        L.append('  UNDECIDED %s  (%s ; carried as the rule of data/b715_rules.txt (1) carries it: %s)' % (f, why, ', '.join(present)))
    return L


def print_lines(b=None, tree=None, act=None, rev='main'):
    b = base() if b is None else b
    tree = main_tree(rev) if tree is None else tree
    ad = added()
    r, joins, leaves, nj = resolve(b, tree, ad)
    head = A.gs('pp', 'rev-parse', '--short', rev)
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
    if current_rule(act):
        r, rows = apply_current(r, tree, rev, act=act)
        L += current_lines(rows, r)
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


# ================================================================================ v1.35.3, (R366)(6), [H1]'s held part, b756
# ### [H1] passed as (a) at b754 (relay data/b754_author_answers.txt :131; data/b754_events.txt (31)): the handoff page joins the archive's
# ### roster and the Project set. The roster is read from PLACE-papers' tree alone and the builder copied from PLACE-papers alone, so the
# ### relay's page could not join: the part was held at the [M2] put and carried ("the relay's HANDOFF.md in the archive and the Project set
# ### by a second source", data/b754_rules.txt :107-:108), and (R366)(6) orders it at b756. THE SECOND SOURCE: the relay paths below, each
# ### read as the blob at the relay's HEAD (the committed page, LF, as tools/standing/handoff.py writes it, not a working copy the host may
# ### convert), copied by the builder after the roster's files under the builder's own flat-name rule, declared on one MANIFEST line under
# ### the source line, and read by the verifier's clause 3 beside the roster where the MANIFEST declares it; a build that declares none
# ### (every build before b756's) is read as it was built. The Project set carries the page from b756's build on.
SECOND = ('HANDOFF.md',)   # ### relay paths
SECOND_FROM = 756
SECOND_LINE = re.compile(r'^Second source: the relay at commit ([0-9a-f]{7,40}) \(its HEAD\): (.+?)\.\s*$', re.M)
HEADVER = re.compile(r'\bv\d+(\.\d+)+')   # ### the builder's version read over a file's first 20 lines (tools/mirror_build.ps1 :72-:76)


def second_rows(rev='HEAD'):
    """[(path, bytes)] of the second source at the relay's `rev`; a path the relay does not hold there refuses, nothing copied."""
    out = []
    for p in SECOND:
        b = A.git('relay', 'show', '%s:%s' % (rev, p))
        if b is None:
            raise SystemExit('### THE SECOND SOURCE`S %s IS NOT AT THE RELAY`S %s -- NOTHING COPIED' % (p, rev))
        out.append((p, b))
    return out


def second_line(head, paths=SECOND):
    return 'Second source: the relay at commit %s (its HEAD): %s.' % (head, ', '.join(paths))


def second_declared(man):
    """the paths a MANIFEST declares from the second source, or None where it declares none."""
    m = SECOND_LINE.search(man or '')
    return [x.strip() for x in m.group(2).split(',')] if m else None


def second_paths(declared):
    """the paths clause 3 reads beside the roster: the second source's where the MANIFEST declares one, else none (an earlier build)."""
    return list(SECOND) if declared is not None else []


def second_copy(stage, rev='HEAD'):
    """copy the second source into the builder's stage, every name checked before any file is written; its MANIFEST rows and line."""
    import hashlib
    taken = set(os.listdir(stage))
    rows, plan = [], []
    for p, b in second_rows(rev):
        leaf = p.split('/')[-1]
        parent = p.split('/')[-2] if '/' in p else ''
        if leaf in taken and parent:
            leaf = parent + '__' + leaf
        if leaf in taken:
            raise SystemExit('### ROSTER COLLISION unresolved for the second source`s %s -> %s -- NOTHING COPIED' % (p, leaf))
        taken.add(leaf)
        text = b.decode('utf-8', 'replace').replace('\r', '').split(NL)[:20]
        ver = next((m.group(0) for m in (HEADVER.search(l) for l in text) if m), '-')
        plan.append((leaf, b, dict(file=leaf, bytes=len(b), md5=hashlib.md5(b).hexdigest().lower(), version=ver,
                                   commit=A.gs('relay', 'log', '-1', '--format=%h %ad', '--date=short', rev, '--', p) or '-')))
    for leaf, b, row in plan:
        with open(os.path.join(stage, leaf), 'wb') as f:
            f.write(b)
        rows.append(row)
    return dict(rows=rows, line=second_line(A.gs('relay', 'rev-parse', '--short', rev), SECOND))


def main(route, rev='main'):
    if route == 'second':   # ### v1.35.3: `roster.py second <stage>`, for the builder
        print(json.dumps(second_copy(rev)))
        return 0
    if route == 'project':
        print(NL.join(project_lines(rev)))
        return 0
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
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'print', sys.argv[2] if len(sys.argv) > 2 else 'main'))
