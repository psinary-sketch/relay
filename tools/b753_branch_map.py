# -*- coding: utf-8 -*-
"""b753_branch_map.py -- (R363)(5)(ii): THE CRITERION KERNEL'S BRANCH MAP, data/b753_branch_map.txt.

For every branch of SIDE-explicit-formula at the remote, as (5)(i)'s one remote read banked them (data/b753_kernels.json; no remote read
here, nothing fetched): its head, its merge-base with main, its commits ahead of main, the modules it adds or changes by path, the tags on
it, and the declarations of record it carries that main does not, by name and path as FINDINGS cites them; for each pair of the four
branches of record, whether either carries the other's modules. Beside it THE TWIN READ: the rQ, aQ and bL of SIDEExplicitFormula/C2Walk.lean
on c2-b725 and the rQ and cQ of the instance on zq-b730 printed whole from their trees, with one line saying whether any declaration on any
branch relates them. Read from the clone's objects by `git show`, `git diff --name-status`, `git grep`; nothing merged, nothing created, no
branch moved, no Lean file written, nothing built. The definitions are printed as source text; no form and no coefficient is evaluated.

  python -X utf8 -u tools/b753_branch_map.py control      the controls alone
  python -X utf8 -u tools/b753_branch_map.py run          the controls printed, then the map and the bank (refuses unless this file is committed
                                                          and unchanged, and under the memory and disk holds)
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
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b753'
EF = 'D:/SIDE-explicit-formula'
NAME = 'SIDE-explicit-formula'
BANK = os.path.join(RELAY, 'data', '%s_branch_map.txt' % ACT)
KERNELS = os.path.join(RELAY, 'data', '%s_kernels.json' % ACT)
# ### the declarations of record, by branch, as (R363)(5)(ii) names them; where FINDINGS cites a statement by its words and not by a
# ### declaration's name, the names are the seat's reading of the branch's tree and the row says so
RECORD = (
    ('c2-b725', 'c2_value_law', 'FINDINGS :12224 by name'),
    ('c2-b725', 'c2_least_negative', 'FINDINGS :12224 by name'),
    ('zq-b730', 'zq_premises', '(R363)(5)(ii) by name'),
    ('zq-b730', 'zq_offline_zero', '(R363)(5)(ii) by name'),
    ('zq-b730', 'zq_li_nonneg_fails', '(R363)(5)(ii) by name'),
    ('zq-b730', 'pc_online', 'FINDINGS :14027 by name'),
    ('zq-b730', 'zeta_box', '(R363)(5)(ii) by name'),
    ('keiper-b725', 'liCoeff_two_pos', 'FINDINGS :12216, :12226 by its words "lambda_2 > 0", the name the seat`s reading of the tree'),
    ('keiper-b725', 'stieltjes_one_lt', 'FINDINGS :12226 by its words "(stieltjes 1).re < -1/20", the name the seat`s reading of the tree'),
    ('detect-b729', 'SupportDetection', 'FINDINGS :12228 by name, the detection statement, a def, not compiled and not proved'),
    ('detect-b729', 'StripCertificate', 'FINDINGS :12228 by name, its certificate'),
)
FOUR = ('c2-b725', 'zq-b730', 'keiper-b725', 'detect-b729')
TWIN = (('c2-b725', 'SIDEExplicitFormula/C2Walk.lean', ('rQ', 'aQ', 'bL')),
        ('zq-b730', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', ('rQ',)),
        ('zq-b730', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', ('cQ',)))
TWIN_CITED = {('zq-b730', 'rQ'): 59, ('zq-b730', 'cQ'): 63}   # ### the ruling's lines for the def's own line
KNOWN = (('c2-b725', '0395f15d'), ('zq-b730', '1e658870'), ('main', '8fbab45d'))
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma|def|abbrev|structure|instance)\s+([^\s:({\[]+)')


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def g(*a):
    r = subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout, r.returncode


def refs():
    row = json.load(io.open(KERNELS, encoding='utf-8'))['rows'][NAME]
    if row.get('code'):
        raise SystemExit('### (5)(i)`s read of %s FAILED; no map' % NAME)
    return row['heads'], row['tags'], row['at']


def have(sha):
    return g('cat-file', '-e', sha + '^{commit}')[1] == 0


def is_anc(a, b):
    return g('merge-base', '--is-ancestor', a, b)[1] == 0


def changed(base, sha):
    """[(status letter, path)] of base..sha."""
    out = []
    for l in g('diff', '--name-status', '--no-renames', base, sha)[0].split('\n'):
        if '\t' in l:
            out.append((l.split('\t')[0][:1], l.split('\t')[-1]))
    return out


def tree(sha):
    return set(x for x in g('ls-tree', '-r', '--name-only', sha)[0].split('\n') if x)


def find_decl(name, sha):
    """[(path, line, text)]: the declarations named `name` in the .lean files of the tree at sha."""
    out = []
    pat = r'^\s*(@\[[^]]*\]\s*)?((private|protected|noncomputable)\s+)*(theorem|lemma|def|abbrev|structure|instance)\s+%s($|[^A-Za-z0-9_.\x27])' % re.escape(name)
    for l in g('grep', '-n', '-E', pat, sha, '--', '*.lean')[0].split('\n'):
        p = l.split(':', 3)
        if len(p) == 4:
            out.append((p[1], int(p[2]), p[3].strip()))
    return out


def decls_in(text):
    return [(i, m.group(1), m.group(2)) for i, l in enumerate(text.split('\n'), 1) for m in [DECL.match(l)] if m]


def block(text, name):
    """the def `name` printed whole: (first line, last line, lines) -- the contiguous non-blank lines above the def's own line (its docstring
    and attributes) down to the line before the next blank line; (None, None, []) where the file holds no such def."""
    L = text.split('\n')
    at = [i for i, l in enumerate(L) for m in [DECL.match(l)] if m and m.group(2) == name]
    if not at:
        return None, None, [], None
    i = a = at[0]
    while a > 0 and L[a - 1].strip():
        a -= 1
    b = i
    while b + 1 < len(L) and L[b + 1].strip():
        b += 1
    return a + 1, b + 1, L[a:b + 1], i + 1


def both(sha, x, y):
    """the .lean files of the tree at sha naming both x and y as whole words."""
    def files(w):
        return set(l.split(':', 1)[1] for l in g('grep', '-l', '-w', '-F', w, sha, '--', '*.lean')[0].split('\n') if ':' in l)
    return sorted(files(x) & files(y))


def importers(sha, mods):
    """the .lean files of the tree at sha importing every module of mods."""
    sets = [set(l.split(':', 1)[1] for l in g('grep', '-l', '-E', r'^import\s+%s\s*$' % re.escape(m), sha, '--', '*.lean')[0].split('\n') if ':' in l) for m in mods]
    return sorted(set.intersection(*sets)) if sets else []


def controls(heads, tags):
    L, ok = [], True

    def case(what, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        L.append('  %s: %r %s' % (what, got, 'AS WANTED' if good else '### NOT AS WANTED, wanted %r' % (want,)))
    main = heads['main']
    case('(the refs) (5)(i)`s banked read of the kernel: (branches, tags), every head an object of the clone',
         (len(heads), len(tags), all(have(s) for s in heads.values())), (31, 40, True))
    case('(the refs) the heads the ruling names: ' + ', '.join('%s %s' % k for k in KNOWN), tuple(heads[b][:8] for b, _h in KNOWN), tuple(h for _b, h in KNOWN))
    case('(main against itself) (ahead, modules changed)', (g('rev-list', '--count', '%s..%s' % (main, main))[0].strip(), len(changed(main, main))), ('0', 0))
    case('(a merged branch) cite-b628: (an ancestor of main, ahead, its head the tag v0.23)',
         (is_anc(heads['cite-b628'], main), g('rev-list', '--count', '%s..%s' % (main, heads['cite-b628']))[0].strip(), tags.get('v0.23') == heads['cite-b628']), (True, '0', True))
    case('(a tag off main) v0.38 at 14ca5725: (in main, reachable from zq-b730)', (tags['v0.38'][:8], is_anc(tags['v0.38'], main), is_anc(tags['v0.38'], heads['zq-b730'])),
         ('14ca5725', False, True))
    fx = 'theorem a_b : X :=\n  noncomputable def cQ (n : ℕ) : ℝ :=\n-- theorem commented : X\n@[simp] lemma l1 (x) : y\nprivate theorem p.q\' : z\n'
    case('(the declaration matcher) a planted text', [(k, n) for _i, k, n in decls_in(fx)], [('theorem', 'a_b'), ('def', 'cQ'), ('lemma', 'l1'), ('theorem', "p.q'")])
    case('(a declaration of record) c2_value_law: (on c2-b725, on main)', (len(find_decl('c2_value_law', heads['c2-b725'])), len(find_decl('c2_value_law', main))), (1, 0))
    case('(a planted name) no_such_declaration_b753 on every branch', sum(len(find_decl('no_such_declaration_b753', s)) for s in set(heads.values())), 0)
    first = [l for l in g('grep', '-n', '-E', r'^theorem\s+[A-Za-z_][A-Za-z0-9_]*', main, '--', '*.lean')[0].split('\n') if l][:1]
    nm = DECL.match(first[0].split(':', 3)[3]).group(2) if first else None
    case('(a declaration main carries) the first theorem `git grep` prints on main, %s, found by the reader on main' % nm, bool(nm) and len(find_decl(nm, main)) >= 1, True)
    t = g('show', '%s:%s' % (heads['zq-b730'], TWIN[2][1]))[0]
    a, b, body, own = block(t, 'cQ')
    case('(the block reader) cQ on zq-b730: the def`s own line and its last -- the ruling`s :63-:65 and the def`s termination clause at :66',
         (own, b, body[-1].strip() if body else None), (63, 66, 'termination_by n'))
    t = g('show', '%s:%s' % (heads['zq-b730'], TWIN[1][1]))[0]
    case('(the block reader) rQ on zq-b730: the def`s own line, the ruling`s :59; a name the file lacks', (block(t, 'rQ')[3], block(t, 'no_such_def')[3]), (59, None))
    case('(the relation search) the files of zq-b730 naming both rQ and cQ include the instance`s own module',
         TWIN[2][1] in both(heads['zq-b730'], 'rQ', 'cQ'), True)
    case('(the relation search) a planted pair of names no file holds', both(heads['zq-b730'], 'no_such_name_b753', 'cQ'), [])
    L.append('  ### THE CONTROLS: %d ; %s' % (len(L), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED'))
    return ok, L


def compose(heads, tags, at, gen):
    ok, CL = controls(heads, tags)
    main = heads['main']
    L = ['%s -- (R363)(5)(ii): THE CRITERION KERNEL`S BRANCH MAP -- every branch of %s at the remote, and THE TWIN READ (%s)' % (ACT, NAME, stamp()[:10]), '',
         '### Written by tools/%s_branch_map.py at relay %s (the generator committed before its run) at %s. The branches and tags are the remote`s, as' % (ACT, gen, stamp()),
         '### (5)(i)`s one remote read banked them at %s (data/%s_kernels.json); every head is an object of the clone at %s and is read there.' % (at, ACT, EF),
         '### A bank of this act and no ledger; nothing fetched, merged, created or moved; no Lean file written; nothing built.', '',
         '## THE CONTROLS, printed before any figure'] + CL + ['']
    info, mods = {}, {}
    L += ['## THE BRANCHES: branch | head | merge-base with main | ahead ; behind | modules (.lean) added ; changed ; removed (other files) | tags on it | state']
    off = []
    for b in sorted(heads):
        s = heads[b]
        mb = g('merge-base', main, s)[0].strip()
        ah = int(g('rev-list', '--count', '%s..%s' % (main, s))[0].strip())
        bh = int(g('rev-list', '--count', '%s..%s' % (s, main))[0].strip())
        ch = changed(mb, s)
        lean = [(k, p) for k, p in ch if p.endswith('.lean')]
        own = sorted((t, c) for t, c in tags.items() if c == s or (is_anc(c, s) and not is_anc(c, main)))
        state = 'main' if b == 'main' else ('MERGED: its head an ancestor of main' if ah == 0 else 'OFF MAIN')
        if ah:
            off.append(b)
        info[b] = dict(head=s, mb=mb, ahead=ah, behind=bh, changed=ch, lean=lean)
        mods[b] = set(p for k, p in lean if k == 'A')
        L.append('  %s | %s | %s | %d ; %d | %d ; %d ; %d (%d) | %s | %s' % (
            b, s[:8], mb[:8], ah, bh, sum(1 for k, _p in lean if k == 'A'), sum(1 for k, _p in lean if k == 'M'), sum(1 for k, _p in lean if k == 'D'),
            len(ch) - len(lean), ', '.join('%s%s' % (t, ' (its head)' if c == s else ' at %s' % c[:8]) for t, c in own) or 'none', state))
    L += ['', '## THE MODULES EACH BRANCH OFF MAIN ADDS OR CHANGES, BY PATH (against its merge-base with main; A added, M changed, D removed)']
    for b in off:
        i = info[b]
        L.append('  %s (%s, %d ahead of main, merge-base %s): %d paths' % (b, i['head'][:8], i['ahead'], i['mb'][:8], len(i['changed'])))
        for k, p in i['changed']:
            L.append('      %s %s' % (k, p))
    L += ['', '## THE DECLARATIONS OF RECORD: declaration | its branch | path :line there | on main | named by']
    r_off = 0
    for b, nm, why in RECORD:
        here = find_decl(nm, heads[b])
        on_main = find_decl(nm, main)
        if here and not on_main:
            r_off += 1
        else_ = [x for x in sorted(heads) if x not in (b, 'main') and find_decl(nm, heads[x])]
        L.append('  %s | %s | %s | %s | %s%s' % (
            nm, b, ' ; '.join('%s :%d' % (p, n) for p, n, _t in here) or '### NOT FOUND ON ITS BRANCH',
            ('### CARRIED BY MAIN at ' + ' ; '.join('%s :%d' % (p, n) for p, n, _t in on_main)) if on_main else 'MAIN DOES NOT CARRY IT', why,
            (' ; also on ' + ', '.join(else_)) if else_ else ''))
    L += ['', '## DECLARATIONS IN THE MODULES A BRANCH ADDS (counted by the matcher; names where twelve or fewer)']
    for b in off:
        n = []
        for p in sorted(mods[b]):
            n += [x[2] for x in decls_in(g('show', '%s:%s' % (heads[b], p))[0])]
        L.append('  %s: %d declarations in %d added modules%s' % (b, len(n), len(mods[b]), (' -- ' + ', '.join(n)) if 0 < len(n) <= 12 else ''))
    L += ['', '## THE FOUR BRANCHES OF RECORD, PAIR BY PAIR: whether either carries the other`s modules (the modules a branch adds, sought by path in the other`s tree)']
    trees = dict((b, tree(heads[b])) for b in FOUR)
    npair = 0
    for i, x in enumerate(FOUR):
        for y in FOUR[i + 1:]:
            xy, yx = sorted(mods[y] & trees[x]), sorted(mods[x] & trees[y])
            if xy or yx:
                npair += 1
            L.append('  %s and %s: %s carries %d of the %d modules %s adds ; %s carries %d of the %d modules %s adds ; ancestor either way: %s%s' % (
                x, y, x, len(xy), len(mods[y]), y, y, len(yx), len(mods[x]), x, 'YES' if is_anc(heads[x], heads[y]) or is_anc(heads[y], heads[x]) else 'NO',
                (' -- shared: ' + ', '.join((xy + yx)[:8])) if xy or yx else ''))
    L.append('  one merge-base for the four: %s' % ', '.join(sorted(set(info[b]['mb'][:8] for b in FOUR))))
    L += ['', '## THE TWIN READ: the definitions printed whole from their trees, each with its path and lines']
    for b, p, names_ in TWIN:
        t = g('show', '%s:%s' % (heads[b], p))[0]
        for nm in names_:
            a, z, body, own = block(t, nm)
            cited = TWIN_CITED.get((b, nm))
            L.append('  %s on %s (%s), %s :%s-:%s, the def`s own line :%s%s' % (
                nm, b, heads[b][:8], p, a, z, own, '' if cited is None else (' -- the ruling`s :%d: %s' % (cited, 'AGREES' if cited == own else '### DIFFERS'))))
            L += ['      %4d  %s' % (a + k, l) for k, l in enumerate(body)] if body else ['      ### NOT FOUND']
    c2w, zq1, zq2 = TWIN[0][1], TWIN[1][1], TWIN[2][1]
    L += ['', '## WHETHER ANY DECLARATION ON ANY BRANCH RELATES THEM (searched over the %d branch heads)' % len(heads)]
    has = dict((b, (c2w in tree(heads[b]), zq1 in tree(heads[b]), zq2 in tree(heads[b]))) for b in sorted(heads))
    L.append('  branches whose tree holds %s: %s' % (c2w, ', '.join(b for b in sorted(has) if has[b][0]) or 'none'))
    L.append('  branches whose tree holds %s and %s: %s' % (zq1, zq2, ', '.join(b for b in sorted(has) if has[b][1] and has[b][2]) or 'none'))
    L.append('  branches whose tree holds all three: %s' % (', '.join(b for b in sorted(has) if all(has[b])) or 'none'))
    hits, homonyms = [], []
    for b in sorted(heads):
        for x, y in (('bL', 'cQ'), ('aQ', 'cQ')):
            for f in both(heads[b], x, y):
                # ### a name of the branch's own: where the tree does not hold C2Walk.lean and defines x itself, the x named beside cQ is that
                # ### definition, another of the same name, and no relation to C2Walk's (the first run's one hit, read by hand, was this)
                own = find_decl(x, heads[b])
                if not has[b][0] and own:
                    homonyms.append('%s: %s names both %s and %s -- %s is this branch`s own definition (%s), its tree holding no C2Walk.lean: '
                                    'ANOTHER DEFINITION OF THE SAME NAME, NO RELATION' % (b, f, x, y, x, ' ; '.join('%s :%d `%s`' % o for o in own)))
                else:
                    hits.append('%s: %s names both %s and %s' % (b, f, x, y))
        for f in importers(heads[b], ('SIDEExplicitFormula.C2Walk', 'SIDEExplicitFormula.Schema.ZQ.LogDeriv')) + importers(
                heads[b], ('SIDEExplicitFormula.C2Walk', 'SIDEExplicitFormula.Schema.EpsteinZQ')):
            hits.append('%s: %s imports both modules' % (b, f))
    L += ['  ' + h for h in homonyms + hits]
    L.append('  THE LINE: %s' % (
        'NO DECLARATION ON ANY BRANCH RELATES THEM, by this search: no .lean file of any of the %d heads names C2Walk`s bL or aQ together with cQ (%d file(s) '
        'naming a same-named definition of the branch`s own, printed above), and none imports C2Walk together with the instance`s modules; the two rQ are '
        'separate definitions on separate branches, no tree holding both files' % (len(heads), len(homonyms)) if not hits else
        '### %d FILE(S) NAME OR IMPORT BOTH, listed above; each to be read before a sentence says they are related' % len(hits)))
    L += ['', '### ### **THE CRITERION KERNEL`S BRANCHES MAPPED: %d ; OFF MAIN %d (%s) ; MERGED %d ; RESULTS OF RECORD OFF MAIN %d OF %d ; PAIRS OF THE FOUR SHARING A MODULE %d OF 6 ; '
          'THE TWIN READ: %s ; CONTROLS %s.**' % (len(heads), len(off), ', '.join(off), len(heads) - 1 - len(off), r_off, len(RECORD), npair,
                                                'NO RELATING DECLARATION FOUND' if not hits else '%d FILE(S) TO READ' % len(hits),
                                                'ALL AS WANTED' if ok else '### NOT ALL AS WANTED')]
    return L


def committed():
    rel = 'tools/%s_branch_map.py' % ACT
    r = subprocess.run(['git', '-C', RELAY, 'ls-files', '--error-unmatch', rel], capture_output=True, text=True)
    d = subprocess.run(['git', '-C', RELAY, 'status', '--porcelain', '--', rel], capture_output=True, text=True).stdout.strip()
    h = subprocess.run(['git', '-C', RELAY, 'rev-parse', '--short=8', 'HEAD'], capture_output=True, text=True).stdout.strip()
    return r.returncode == 0 and not d, h


def main(argv):
    heads, tags, at = refs()
    if argv[:1] == ['control']:
        ok, L = controls(heads, tags)
        print('\n'.join(L))
        return 0 if ok else 1
    if argv[:1] != ['run']:
        raise SystemExit(__doc__)
    done, gen = committed()
    if not done:
        raise SystemExit('### REFUSED: tools/%s_branch_map.py is not committed or differs from its commit; the generator commits before its run ((R363)(5))' % ACT)
    import hold
    if hold.refuses('the branch map ((R363)(5)(ii))'):
        return 3
    L = compose(heads, tags, at, gen)
    if '### NOT ALL AS WANTED' in L[-1]:
        print('\n'.join(L[:40]))
        raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NOTHING BANKED')
    tmp = BANK + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')
    os.replace(tmp, BANK)
    skip = False
    for l in L:
        if l.startswith('## THE MODULES EACH BRANCH'):
            skip = True
            print(l + '  [in the bank; not printed here]')
        elif l.startswith('## '):
            skip = False
        if not skip:
            print(l)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
