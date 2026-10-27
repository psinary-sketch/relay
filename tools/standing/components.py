# -*- coding: utf-8 -*-
"""standing/components.py -- THE COMPONENTS COMPOSER, reading the ruling (the class repair (4)(iv) of the toolset act): the components
bank built from the components the ruling names as data (data/act_current.json `components`, each {n, title, clauses, phases}) and the
act's step bank. A new act copies nothing: its ruling's components are its data.

Extracted, not imported (the author's word (1)(a)). Provenance: tools/b714_components_standin.py lines (:64-:95), files_of and banks_of
(:50-:61), its COMPONENTS phases (:34-:36) made the ruling's field, its score placement by the banks a reading names; the head line is the
toolset's own (the stand-in's prose head named its own cause).

  composed(act, components)  -> [head, '', one line per component]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

NL = '\n'
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')


def files_of(repo, commit):
    """the files a commit changes against its first parent (a merge's own files: `git show` prints none for a merge)."""
    out = A.gs(repo, 'diff', '--name-only', commit + '^1', commit) or ''
    return [x for x in out.split(NL) if x.strip()]


def banks_of(act, repo, commit):
    """the banks a commit carries: relay's data/ files less the step bank itself; PLACE-papers' files by name."""
    fs = files_of(repo, commit)
    if repo == 'relay':
        return [f for f in fs if f.startswith('data/') and f != 'data/%s_steps.json' % act]
    return ['%s %s' % (A.NAMES['pp'], f) for f in fs]


def title_of(c):
    return 'COMPONENT %d' % c['n'] if isinstance(c.get('n'), int) else c['title']


def composed(act, components, ruling=None, rev=None):
    """the components bank's lines: each component's commits from the act's step bank by its phases, the banks they carry, each N and S
    reading placed on the first component whose banks its reading names (the rest on the last component's), and the last component's
    entry, root and trail lines. `rev` (v1.1.0): the banks as they stood at a commit (the replay's: the commit that first carries the
    components bank), else now."""
    rows = A.steps(act, rev)
    sc = A.jl('%s_scores.json' % act, rev)
    fj, tj, rj = A.jl('%s_findings.json' % act, rev), A.jl('%s_trail.json' % act, rev), A.jl('%s_act_root.json' % act, rev)
    comp = []
    for c in components:
        name, phases = title_of(c), tuple(c.get('phases') or ())
        cs = [(i + 1, r) for i, r in enumerate(rows) if r.get('phase') in phases]
        banks = []
        for _n, r in cs:
            for b in banks_of(act, r['repo'], r['commit']):
                if b not in banks:
                    banks.append(b)
        comp.append((name, phases, cs, banks))
    last = comp[-1][0] if comp else None
    pat = re.compile(r'data/(%s_[\w.-]+)' % re.escape(act))
    placed = {}
    for k in SCORE_KEYS:
        v = sc.get(k) or ['NOT IN THE SCORES BANK', '']
        named = set('data/' + m for m in pat.findall(str(v[1])))
        at = next((name for name, _p, _c, banks in comp if named & set(banks)), last)
        placed.setdefault(at, []).append('%s %s' % (k, v[0]))
    out = []
    for name, phases, cs, banks in comp:
        commits = ' ; '.join('step row %d %s %s (%s)' % (n, r['repo'], r['commit'][:8], r['phase']) for n, r in cs) or 'NO STEP ROW'
        extra = ''
        if name == last:
            extra = ' ; FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root' % (
                fj.get('entry_line'), (rj.get('root') or '### NOT COMPUTED')[:16], tj.get('line'))
        out.append('### %s : %s ; the banks they carry (%d): %s%s ; %s' % (
            name, commits, len(banks), ', '.join(banks) or 'NONE', extra, ' ; '.join(placed.get(name, [])) or 'no score reading names these banks'))
    head = '%s -- THE COMPONENTS, BANKED UNDER (%s), composed by the standing toolset from the ruling`s components and the step bank.' % (
        act, ruling or '?')
    return [head, ''] + out


def main(route):
    """step [18] of the close (standing clauses v5 row (79)): `bank` writes data/<act>_components.txt for the act data/act_current.json
    names, once (a bank present is never written twice); `dry` prints the lines."""
    cur = A.current()
    L = composed(cur['act'], cur.get('components') or [], cur.get('ruling'))
    if route == 'bank':
        p = os.path.join(A.D, '%s_components.txt' % cur['act'])
        if os.path.exists(p):
            print('### data/%s EXISTS -- NOTHING WRITTEN TWICE' % os.path.basename(p))
            return 3
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p, A.sha256_file(p))
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
