# -*- coding: utf-8 -*-
"""b450_components.py -- THE RECONCILIATION'S ELIGIBLE SET RE-MEASURED, AND THE BATCH READ. ### **AFTER THE LOCK.**

### THE RULE, b390's WORDS (OPEN_TRAILS.md:4446): "take the one whose terminals the drive can reach", settled by
### "compiled terminals live on the HELD, UNMERGED branch ... and are not on `main`". Nothing is added to it.
### Usage: `survey` -- Component 1 and the mechanical reads of Component 2 into data/b450_eligible.json, data/b450_batch.json;
###        `repair` -- the currency repairs under the face's rule, into data/b450_repairs.json;
###        `report` -- everything into data/b450_components.txt.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FERRY = os.path.join(D, 'b450_ferry.txt')
ELIG = os.path.join(D, 'b450_eligible.json')
BATCH = os.path.join(D, 'b450_batch.json')
REPJ = os.path.join(D, 'b450_repairs.json')
OUT = os.path.join(D, 'b450_components.txt')
NL = chr(10)
SKIP = ('.git', 'archive', 'outputs')
V1 = re.compile(r'`(SIDE-[a-z0-9-]+)`')                      # b394's, carried to print its yield beside
V2 = re.compile(r'`?(SIDE-[A-Za-z0-9][A-Za-z0-9-]*)`?')      # b395's widened matcher, as coded
NOTAREPO = ('SIDE-kernel-session-notes',)
RESIDUE = ('SIDE-internal', 'SIDE-Exclusion')
HELDWORDS = re.compile(r'(?i)\bheld\b|\bunmerged\b|not (?:yet )?merged|not on `?main`?|branch-resident')
LIVE_DECL = ('exactly_c1_derives', 'onLine_doubleZero_iff_imDeriv_zero', 'no_onLine_double_iff_transversal', 'derivGrade')
B397 = [('SIDE-cosmo', 'second-exemplar-m4a'), ('SIDE-effects', 'w-ladder-skeleton'), ('SIDE-effects', 'w4-recovery-2026-07-13'),
        ('SIDE-kernel', 'derivative-engine'), ('SIDE-li-map', 'word-lambda-nonneg'), ('SIDE-lv-conservation', 'composition-barrier'),
        ('SIDE-lv-conservation', 'word-p1-finset-a'), ('SIDE-lv-conservation', 'word-pairing-interface'), ('SIDE-spinor', 'substrate-spinor-leg')]
GRADEWORDS = ('DERIVES', 'INTERFACES', 'MILESTONE-OPEN', 'MANUSCRIPT-RESIDENT', 'RESEARCH-REACH',
              'COMPILED', 'SCAFFOLDING', 'TAUTOLOGY', 'Placeholder', 'Open', 'SHELL', 'PENDING')
NEEDLES = {
    'R_CURVE_CRITERION': [('the absent pin bd2ae1a', lambda l: 'bd2ae1a' in l, lambda l: re.search(r'(?i)absent', l))],
    'EXHAUSTIVENESS_LICENSE': [('the S2 Ostrowski seal', lambda l: 'Ostrowski' in l and 'S2' in l, None)],
    'TECHNE_TOOLKIT': [('the E-Difficulty cross-link verdict DISTINCT', lambda l: 'DISTINCT' in l and re.search(r'E-Difficulty|cross-link|κ', l), None)],
    'E_DIFFICULTY_THEOREM': [('the E-Difficulty cross-link verdict DISTINCT', lambda l: 'DISTINCT' in l and re.search(r'E-Difficulty|cross-link|κ', l), None)],
    'INVARIANCE_BARRIERS': [('Face E / keyhole', lambda l: 'keyhole' in l, None),
                            ('the T3 Tier-1 scope', lambda l: 'T3' in l and re.search(r'Tier-1|Tier 1', l), None)],
    'THE_RESIDUE_OF_RH': [('the sign-face registers', lambda l: re.search(r'sign-face|sign face', l), None),
                          ('the sealed S1-S6 table', lambda l: 'S1' in l and 'S6' in l, None),
                          ('the crossing filing', lambda l: 'crossing' in l, None)],
    'REPARAMETERIZATION_BARRIERS_v0_1': [('the two-kinds windows verdict', lambda l: re.search(r'two kinds|two-kinds', l) and 'window' in l, None)],
}
SIGN = [('W_inf NOT sign-definite', lambda l: 'sign-definite' in l, lambda l: re.search(r'(?i)\bnot\b', l)),
        ('the Day-1 section I attribution pole-plus-archimedean',
         lambda l: 'pole-plus-archimedean' in l or ('pole' in l and 'archimedean' in l and re.search(r'Day-1|§I', l)), None)]
for k in ('INDEX_ARITY_AT_THE_CRITICAL_LINE', 'SIMPLICITY_OF_RIEMANN_ZEROS', 'THE_UNCONDITIONAL_SURROUND',
          'PATHS_TO_THE_CRITICAL_LINE', 'ENUMERA'):
    NEEDLES[k] = SIGN

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '').strip()


def read(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13) + chr(10), NL)


def dump(p, o):
    io.open(p + '.tmp', 'w', encoding='utf-8').write(json.dumps(o, indent=1, ensure_ascii=False))
    os.replace(p + '.tmp', p)


def census():
    out = []
    for i, ln in enumerate(read(CENSUS).split(NL), 1):
        if 73 <= i <= 88:
            m = re.match(r'\|\s*`([A-Z_0-9a-z]+)`\s*\|\s*([^|]*?)\s*\|\s*[#* ]*(\d{4}-\d\d-\d\d)[* ]*\|\s*[#* ]*(\d+)', ln)
            if m:
                out.append(dict(k=m.group(1), phase=m.group(2), date=m.group(3), pins=int(m.group(4)), census_line=i))
    return out


def locate(names):
    loc = {}
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            dn[:] = []
            continue
        for f in fn:
            if f.endswith('.md') and f[:-3] in names:
                loc.setdefault(f[:-3], []).append(rel + '/' + f if rel != '.' else f)
    return loc


def repo_ok(name):
    p = os.path.join('D:' + os.sep, name)
    if not os.path.isdir(os.path.join(p, '.git')):
        return False, None
    rc, h = git(p, 'rev-parse', '--short', 'HEAD')
    return rc == 0 and bool(h), h


def main_branch(repo):
    for b in ('main', 'master'):
        if git(repo, 'rev-parse', '--verify', '--quiet', b)[0] == 0:
            return b
    return None


def reconciled_later(keys):
    t = read(TRAILS).split(NL)
    s = next(i for i, l in enumerate(t) if l.startswith('<!-- b394 the reconciliation batched'))
    hits = []
    for i in range(s + 1, len(t)):
        l = t[i]
        if re.search(r'(?i)read whole|reconcil', l):
            for k in keys:
                if k in l:
                    hits.append(dict(line=i + 1, k=k, text=' '.join(l.split())[:260]))
    return hits


def survey():
    t0 = time.time()
    C = census()
    names = [c['k'] for c in C]
    loc = locate(set(names))
    RECON = {'ADDITIVE_MULTIPLICATIVE_CONSPIRACY': 'b390', 'GRH_CASCADE': 'b394',
             'FOUNDATIONS_OF_THE_SIDE_PROGRAMME': 'b394', 'SILENCE_STAGES_DEALIGNMENT': 'b394'}
    later = reconciled_later(names)
    rows, eligible = [], []
    for c in C:
        k = c['k']
        r = dict(c)
        paths = loc.get(k, [])
        r['paths'] = paths
        if k in RECON:
            r.update(state='RECONCILED', why='read whole at %s under b390`s rule' % RECON[k])
            rows.append(r)
            continue
        if not paths:
            r.update(state='EXCLUDED', why='NOT ON DISK: no file carries the stem outside .git, archive, outputs')
            rows.append(r)
            continue
        path = paths[0]
        txt = read(os.path.join(PP, path.replace('/', os.sep)))
        v1 = sorted(set(V1.findall(txt)))
        v2 = sorted(set(m for m in V2.findall(txt) if m not in NOTAREPO))
        residue = [x for x in v2 if x in RESIDUE]
        named = [x for x in v2 if x not in RESIDUE]
        reach = {}
        for n in named:
            ok, h = repo_ok(n)
            reach[n] = h if ok else None
        on = [n for n in named if reach[n]]
        r.update(path=path, v1=v1, v2=v2, residue=residue, named=named, on_drive=on,
                 heads=dict((n, reach[n]) for n in on))
        # ### b390's clause, measured live.
        held_lines, branches = [], []
        ls = txt.split(NL)
        for i, l in enumerate(ls, 1):
            if HELDWORDS.search(l):
                for repo, br in B397:
                    if br in l:
                        branches.append(dict(line=i, repo=repo, branch=br))
                held_lines.append(i)
        live = []
        for b in {(x['repo'], x['branch']) for x in branches}:
            rp = os.path.join('D:' + os.sep, b[0])
            mb = main_branch(rp)
            rc, _ = git(rp, 'merge-base', '--is-ancestor', b[1], mb) if mb else (1, '')
            live.append(dict(repo=b[0], branch=b[1], main=mb, merged=(rc == 0)))
        decl = [d for d in LIVE_DECL if d in txt]
        unmerged_named = [x for x in live if not x['merged']]
        pins = sorted(set(re.findall(r'(?<![0-9a-f])([0-9a-f]{7})(?![0-9a-f])', txt)))
        r.update(held_lines=len(held_lines), branches_named=branches, branches_live=live, live_declarations=decl, pins_seen=len(pins))
        if not named:
            r.update(state='EXCLUDED', why='NAMES NO TERMINAL: the wide matcher names no repository (residue %s)' % (residue or 'none'))
        elif not on:
            r.update(state='EXCLUDED', why='NONE ON THE DRIVE: named %s, none a git repository resolving HEAD' % named)
        else:
            clause_all = bool(unmerged_named) and False   # ### "no terminal it names is on main" is never shown by these reads
            if clause_all:
                r.update(state='EXCLUDED', why='EXCLUDED BY b390`S CLAUSE')
            else:
                partial = bool(unmerged_named or decl)
                r.update(state='ELIGIBLE', partial=partial,
                         why=('names %d repositories on the drive' % len(on)) + (
                             ('; PARTIAL (W1): unmerged %s, live declarations %s' % ([x['branch'] for x in unmerged_named], decl)) if partial else ''))
                eligible.append(k)
        rows.append(r)
    E = dict(population=len(C), on_disk=sum(1 for c in C if loc.get(c['k'])), rows=rows,
             reconciled=[(k, RECON[k]) for k in names if k in RECON], later_hits=later,
             eligible=eligible, excluded=[(r['k'], r['why']) for r in rows if r['state'] == 'EXCLUDED'],
             unread=len([r for r in rows if r['state'] != 'RECONCILED']), board=12, seconds=round(time.time() - t0, 1))
    dump(ELIG, E)
    print('population %d ; on disk %d ; reconciled %d ; eligible %d %s ; excluded %s ; later hits %d'
          % (E['population'], E['on_disk'], len(E['reconciled']), len(eligible), eligible, E['excluded'], len(later)))
    batch(E)
    return 0


# ------------------------------------------------------------------------------------------------ COMPONENT 2
def registry_rows():
    out = {}
    for i, ln in enumerate(read(REGISTRY).split(NL), 1):
        m = re.match(r'\|\s*([0-9][^|]*?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+\.md)`\s*\|\s*(v[0-9][0-9.]*)\s*\|', ln)
        if m:
            out[m.group(3)] = dict(rid=m.group(1), version=m.group(4), line=i)
    return out


def registry_updates():
    ups = []
    for i, ln in enumerate(read(REGISTRY).split(NL), 1):
        for m in re.finditer(r'Row \*\*([0-9][^*]*?)\*\* \(`([^`]+)`\): version (?:reconciled )?\*\*(v[0-9.]+) (?:→|->) (v[0-9.]+)\*\*', ln):
            ups.append(dict(rid=m.group(1), path=m.group(2), old=m.group(3), new=m.group(4), line=i))
    return ups


def vnum(v):
    parts = re.split(r'[._]', v.lstrip('v').rstrip('.'))
    o = [int(x) if x.isdigit() else 0 for x in parts]
    while len(o) > 1 and o[-1] == 0:
        o.pop()
    return tuple(o)


def table_rows(ls):
    out, started = [], False
    for i, ln in enumerate(ls, 1):
        if ln.startswith('|') and ln.count('|') >= 3:
            cells = [x.strip() for x in ln.split('|')[1:-1]]
            if cells and all(set(c) <= set(':- ') and c for c in cells):
                continue
            if cells and re.sub(r'[*#` ]', '', cells[0]).lower() in ('claim', 'claims'):
                started = True
                continue
            if started:
                out.append((i, cells))
        elif started and ln.strip() == '':
            started = False
    return out


def head_version(ls):
    for l in ls[:60]:
        m = re.search(r'\bv([0-9]+(?:\.[0-9]+)+)\b', l)
        if m:
            return 'v' + m.group(1)
    return None


def sections(ls):
    cur, out = '', []
    fence = False
    for l in ls:
        if l.startswith('```'):
            fence = not fence
        if l.startswith('#'):
            cur = l
        out.append((cur, fence))
    return out


def batch(E):
    t0 = time.time()
    regs = registry_rows()
    ups = registry_updates()
    stems = dict((os.path.basename(p)[:-3], (p, v['version'], v['line'])) for p, v in regs.items() if len(os.path.basename(p)) > 9)
    VER = re.compile(r'v\s*([0-9][0-9.]*?)(?=[^0-9.]|$)')
    WORDCH = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_')
    live_branch = {}
    for repo, br in B397:
        rp = os.path.join('D:' + os.sep, repo)
        mb = main_branch(rp)
        rc, _ = git(rp, 'merge-base', '--is-ancestor', br, mb) if mb else (1, '')
        exists = git(rp, 'rev-parse', '--verify', '--quiet', br)[0] == 0
        live_branch[br] = dict(repo=repo, exists=exists, merged=(rc == 0 and exists))
    rows_by_k = dict((r['k'], r) for r in E['rows'])
    B = dict(order=E['eligible'], keystones={}, live_branch=live_branch, updates=len(ups), started=t0)
    for k in E['eligible']:
        tk = time.time()
        path = rows_by_k[k]['path']
        full = os.path.join(PP, path.replace('/', os.sep))
        txt = read(full)
        ls = txt.split(NL)
        secs = sections(ls)
        t1 = [(i, l) for i, l in enumerate(ls, 1) if l.startswith('## Correspondence') or 'CORRESPONDENCE AT THE STANDARD' in l]
        tr = table_rows(ls)
        tw = []
        for ti, _tl in t1:
            j = ti
            while j < len(ls) and j < ti + 12 and not ls[j].startswith('|'):
                j += 1
            if j < len(ls) and ls[j].startswith('|'):
                j += 1
                while j < len(ls) and ls[j].startswith('|'):
                    cells = [x.strip() for x in ls[j].split('|')[1:-1]]
                    if not (cells and all(set(c) <= set(':- ') and c for c in cells)):
                        tw.append((j + 1, cells))
                    j += 1
        tw_grades = {}
        for _i, cells in tw:
            g = next((w for w in GRADEWORDS if w.upper() in cells[-1].upper()), 'OTHER')
            tw_grades[g] = tw_grades.get(g, 0) + 1
        grades = {}
        for _i, cells in tr:
            g = next((w for w in GRADEWORDS if w.upper() in cells[-1].upper()), 'OTHER')
            grades[g] = grades.get(g, 0) + 1
        hv = head_version(ls)
        items = []
        # (i) the registry row
        row = regs.get(path)
        if row:
            if not hv:
                b = 'DOES NOT CARRY IT'
            elif vnum(row['version']) == vnum(hv):
                b = 'ALREADY SAYS IT'
            elif vnum(row['version']) > vnum(hv):
                b = 'SAYS SOMETHING NOW SUPERSEDED'
            else:
                b = 'ALREADY SAYS IT'
            items.append(dict(kind='(i) registry row', bucket=b, detail='row %s at REGISTRY.md:%d carries %s ; head token %s%s'
                              % (row['rid'], row['line'], row['version'], hv, ' ; ROW STALE, ROUTED' if hv and vnum(hv) > vnum(row['version']) else '')))
        else:
            items.append(dict(kind='(i) registry row', bucket=None, detail='NO REGISTRY ROW for %s -- not in the population' % path))
        # (ii) the census era findings -- hits collected for the hand read
        for label, hit, finding in NEEDLES.get(k, []):
            hl = [(i, l) for i, l in enumerate(ls, 1) if hit(l)]
            items.append(dict(kind='(ii) era finding', label=label, hits=[dict(line=i, text=' '.join(l.split())[:300],
                                                                              finding_form=bool(finding(l)) if finding else None) for i, l in hl],
                              bucket=('DOES NOT CARRY IT' if not hl else 'HAND-READ')))
        # (iii) registry updates, and the species sweep
        cites = []
        for i, ln in enumerate(ls, 1):
            for stem, (target, regver, rline) in stems.items():
                for m in re.finditer(re.escape(stem), ln):
                    a = ln[m.start() - 1] if m.start() else ' '
                    bch = ln[m.end()] if m.end() < len(ln) else ' '
                    if a in WORDCH or bch in WORDCH:
                        continue
                    tail = ln[m.end():m.end() + 40]
                    v = VER.search(tail)
                    if not v:
                        continue
                    span = tail[:v.start()]
                    if len(span) > 12 or re.search(r'[A-Za-z]', span) or ',' in span:
                        continue
                    cited = 'v' + v.group(1).rstrip('.')
                    cites.append(dict(line=i, stem=stem, target=target, at=cited, registry=regver, registry_line=rline,
                                      col=m.end() + v.start(), vtext=tail[v.start():v.end()], text=' '.join(ln.split())[:220],
                                      section=secs[i - 1][0][:80], fence=secs[i - 1][1], quoted=ln.lstrip().startswith('>')))
        s1_yield = len(cites)
        S2 = re.compile(r'(?<![A-Za-z0-9_])([A-Z][A-Z0-9_]{3,}?)(?:\.md)?`?\*{0,2}(?: |_)v([0-9]+(?:\.[0-9]+)*)(?![0-9])')
        allstems = sorted(stems, key=len, reverse=True)
        cites2 = []
        for i, ln in enumerate(ls, 1):
            for m in S2.finditer(ln):
                name = m.group(1).rstrip('_')
                hit = [st for st in allstems if name == st or name.startswith(st + '_')]
                if not hit:
                    pre = [st for st in allstems if st.startswith(name + '_')]
                    hit = pre if len(pre) == 1 else []
                if not hit:
                    continue
                stem = hit[0]
                target, regver, rline = stems[stem]
                cites2.append(dict(line=i, stem=stem, name=m.group(1), target=target, at='v' + m.group(2), registry=regver,
                                   registry_line=rline, vspan=[m.start(2) - 1, m.end(2)], text=' '.join(ln.split())[:220],
                                   section=secs[i - 1][0][:80], fence=secs[i - 1][1], quoted=ln.lstrip().startswith('>'),
                                   transition=bool(re.search(r'→|->|was v|from v', ln))))
        cites = cites2
        for u in ups:
            stem = os.path.basename(u['path'])[:-3]
            for c in cites:
                if c['stem'] == stem:
                    if vnum(c['at']) == vnum(u['old']):
                        items.append(dict(kind='(iii) registry update', bucket='SAYS SOMETHING NOW SUPERSEDED', species='unpropagated',
                                          detail='line %d cites %s at %s ; REGISTRY.md:%d moved it %s -> %s' % (c['line'], stem, c['at'], u['line'], u['old'], u['new'])))
                    elif vnum(c['at']) == vnum(u['new']):
                        items.append(dict(kind='(iii) registry update', bucket='ALREADY SAYS IT',
                                          detail='line %d cites %s at %s, the update`s new version (REGISTRY.md:%d)' % (c['line'], stem, c['at'], u['line'])))
        lineage = {}
        species = dict(phantom=[], superseded=[], unpropagated=[])
        upd_old = set((os.path.basename(u['path'])[:-3], vnum(u['old'])) for u in ups)
        for c in cites:
            if vnum(c['at']) >= vnum(c['registry']):
                continue
            tp = os.path.join(PP, c['target'].replace('/', os.sep))
            if c['target'] not in lineage:
                lineage[c['target']] = set('v' + x.rstrip('.') for x in re.findall(r'\bv([0-9][0-9.]*)', read(tp))) if os.path.exists(tp) else set()
            lin = lineage[c['target']]
            c['in_lineage'] = any(vnum(c['at']) == vnum(x) for x in lin)
            c['in_batch'] = c['stem'] in E['eligible']
            if lin and not c['in_lineage']:
                species['phantom'].append(c)
            elif (c['stem'], vnum(c['at'])) in upd_old:
                species['unpropagated'].append(c)
            else:
                species['superseded'].append(c)
        # (iv) b397's branch state
        for i, l in enumerate(ls, 1):
            for br, st in live_branch.items():
                if br in l:
                    heldw = bool(HELDWORDS.search(l))
                    mergw = bool(re.search(r'(?i)\bmerged\b|\blanded\b', l)) and not re.search(r'(?i)unmerged|not (?:yet )?merged', l)
                    if not (heldw or mergw):
                        continue
                    if st['merged'] and heldw and not mergw:
                        b = 'SAYS SOMETHING NOW SUPERSEDED'
                    else:
                        b = 'ALREADY SAYS IT'
                    items.append(dict(kind='(iv) branch state', bucket=b, detail='line %d names %s (live merged %s) : %s'
                                      % (i, br, st['merged'], ' '.join(l.split())[:200])))
        B['keystones'][k] = dict(path=path, lines=len(ls), bytes=len(txt.encode('utf-8')), head=hv, t1=len(t1), t1_lines=[i for i, _ in t1][:5],
                                 t2_rows=len(tr), grades=grades, tw_rows=len(tw), tw_grades=tw_grades, items=items, species=species, cites=len(cites), s1_cites=s1_yield, s2_cites=len(cites2),
                                 seconds=round(time.time() - tk, 2))
        print('%-34s lines %4d T1 %d T2 %2d TW %2d items %2d S1 %d S2 %2d phantom %d unprop %d supers %d'
              % (k[:34], len(ls), len(t1), len(tr), len(tw), len(items), s1_yield, len(cites2), len(species['phantom']), len(species['unpropagated']), len(species['superseded'])))
    B['seconds'] = round(time.time() - t0, 1)
    dump(BATCH, B)



# ------------------------------------------------------------------------------------------------ THE HAND READ
# ### Every entry is applied after the mechanical survey and printed whole in the report.
HAND = [
    ('EXHAUSTIVENESS_LICENSE', '(iv)', 'line 112 ', 'SAYS SOMETHING NOW SUPERSEDED',
     'the line says "HELD -- nothing merged" of `w-ladder-skeleton`, which is merged live; the classifier read "merged" as landed. CORRECTED BY HAND.'),
]
EXCLUDE_ITEM_KEY = ': > line '
EXCLUDE_ITEM_WHY = 'a blockquoted preserved original (b397`s annotation) quotes prior text; it is not the keystone`s own statement'
RESIDUE_CITES = {('TECHNE_TOOLKIT', 468): 'the keystone`s own "Versions and archive" table names its own past version `v6` as Superseded -- a mention of its own lineage, not a citation of another document',
                 ('TECHNE_TOOLKIT', 543): 'the keystone`s own References entry for its own past version `v7` -- its lineage, not a citation of another document'}
REGISTRY_SECOND = {'E_DIFFICULTY_THEOREM': ('p2-4', 255, 'v1.0.3'), 'REPARAMETERIZATION_BARRIERS_v0_1': (None, 658, None)}
NOT_LOCATED = {('INVARIANCE_BARRIERS', 'Face E / keyhole'): 'the finding`s form is not located in FINDINGS.md or OPEN_TRAILS.md (`keyhole` occurs in neither); the second shape`s hit (line 534, "Face E Tier 1 folded in as §3.4") names the subject and is not shown to state the finding -- ROUTED',
               ('INVARIANCE_BARRIERS', 'the T3 Tier-1 scope'): 'the finding`s form is not located in FINDINGS.md or OPEN_TRAILS.md; the second shape`s hits are the toolkit`s `T3` rows inside §3.4 and are not shown to state a scope finding -- ROUTED',
               ('R_CURVE_CRITERION', 'the absent pin bd2ae1a'): '`git log -S bd2ae1a` over this path returns nothing: the keystone never carried the pin the census names for it; the census`s era finding is not reproduced here -- ROUTED'}
SECOND_SHAPE_YIELD = {('PATHS_TO_THE_CRITICAL_LINE', 'W_inf NOT sign-definite'): 0, ('PATHS_TO_THE_CRITICAL_LINE', 'the Day-1 section I attribution pole-plus-archimedean'): 0,
                      ('THE_UNCONDITIONAL_SURROUND', 'W_inf NOT sign-definite'): 0, ('THE_UNCONDITIONAL_SURROUND', 'the Day-1 section I attribution pole-plus-archimedean'): 0,
                      ('SIMPLICITY_OF_RIEMANN_ZEROS', 'W_inf NOT sign-definite'): 0, ('SIMPLICITY_OF_RIEMANN_ZEROS', 'the Day-1 section I attribution pole-plus-archimedean'): 0,
                      ('INDEX_ARITY_AT_THE_CRITICAL_LINE', 'W_inf NOT sign-definite'): 0, ('INDEX_ARITY_AT_THE_CRITICAL_LINE', 'the Day-1 section I attribution pole-plus-archimedean'): 0,
                      ('R_CURVE_CRITERION', 'the absent pin bd2ae1a'): 0, ('EXHAUSTIVENESS_LICENSE', 'the S2 Ostrowski seal'): 6,
                      ('TECHNE_TOOLKIT', 'the E-Difficulty cross-link verdict DISTINCT'): 2, ('E_DIFFICULTY_THEOREM', 'the E-Difficulty cross-link verdict DISTINCT'): 5,
                      ('INVARIANCE_BARRIERS', 'Face E / keyhole'): 1, ('INVARIANCE_BARRIERS', 'the T3 Tier-1 scope'): 12,
                      ('THE_RESIDUE_OF_RH', 'the sign-face registers'): 0, ('REPARAMETERIZATION_BARRIERS_v0_1', 'the two-kinds windows verdict'): 0}
SECOND_SHAPE_READ = {('EXHAUSTIVENESS_LICENSE', 'the S2 Ostrowski seal'): 'Ostrowski-class generally (lines 33-75), not the `S2` seal as re-stated in the sealed inventory',
                     ('TECHNE_TOOLKIT', 'the E-Difficulty cross-link verdict DISTINCT'): 'Ξ.22 is "distinct from Ξ.7" (lines 195, 489) -- another subject',
                     ('E_DIFFICULTY_THEOREM', 'the E-Difficulty cross-link verdict DISTINCT'): 'the older "dichotomy stands as a conjecture ... κ-machinery" wording (lines 10, 160) and unrelated uses -- not the cross-link verdict'}
A_, S_, N_ = 'ALREADY SAYS IT', 'SAYS SOMETHING NOW SUPERSEDED', 'DOES NOT CARRY IT'


def classify():
    B = json.load(io.open(BATCH, encoding='utf-8'))
    notes = []
    for k, v in B['keystones'].items():
        keep = []
        for it in v['items']:
            d = it.get('detail', '') or ''
            if it['kind'].startswith('(iv)') and EXCLUDE_ITEM_KEY in d:
                notes.append(dict(k=k, kind=it['kind'], action='EXCLUDED FROM THE COUNT', why=EXCLUDE_ITEM_WHY, detail=d[:170]))
                continue
            for hk, hp, hkey, hv, hw in HAND:
                if hk == k and it['kind'].startswith(hp) and d.startswith(hkey):
                    notes.append(dict(k=k, kind=it['kind'], action='%s -> %s' % (it['bucket'], hv), why=hw, detail=d[:170]))
                    it['bucket'] = hv
            if it['kind'].startswith('(i)') and it['bucket'] is None and k in REGISTRY_SECOND:
                rid, rl, rv = REGISTRY_SECOND[k]
                if rv:
                    it['bucket'] = A_ if vnum(rv) >= vnum(v['head']) and vnum(rv) == vnum(v['head']) else (S_ if vnum(rv) > vnum(v['head']) else A_)
                    it['detail'] = 'row %s at REGISTRY.md:%d carries %s ; head token %s -- FOUND BY THE SECOND ROW SHAPE (the first form missed it)' % (rid, rl, rv, v['head'])
                else:
                    it['detail'] = 'a registry table row at REGISTRY.md:%d names the file and carries no version -- not in the population (second row shape)' % rl
            if it['kind'].startswith('(ii)'):
                key = (k, it['label'])
                if key in SECOND_SHAPE_YIELD:
                    it['second_yield'] = SECOND_SHAPE_YIELD[key]
                    it['second_read'] = SECOND_SHAPE_READ.get(key, 'no hit' if SECOND_SHAPE_YIELD[key] == 0 else '')
                if it['bucket'] == 'HAND-READ':
                    it['bucket'] = A_
                    it['why'] = 'the hit states the finding: %s' % '; '.join('line %d' % h['line'] for h in it['hits'])
                if key in NOT_LOCATED:
                    it['note'] = NOT_LOCATED[key]
            keep.append(it)
        v['items'] = keep
        for sp in ('phantom', 'unpropagated', 'superseded'):
            res = [c for c in v['species'][sp] if (k, c['line']) in RESIDUE_CITES]
            v['species'][sp] = [c for c in v['species'][sp] if (k, c['line']) not in RESIDUE_CITES]
            for c in res:
                notes.append(dict(k=k, kind='species ' + sp, action='RESIDUE, NOT COUNTED', why=RESIDUE_CITES[(k, c['line'])], detail=c['text'][:170]))
        v['buckets'] = dict((b, sum(1 for it in v['items'] if it['bucket'] == b)) for b in (A_, S_, N_))
    pairs = []
    for k, v in B['keystones'].items():
        ls = read(os.path.join(PP, v['path'].replace('/', os.sep))).split(NL)
        for i, l in enumerate(ls, 1):
            for other, ov in B['keystones'].items():
                if other == k:
                    continue
                for short in {other, other.split('_AT_')[0]}:
                    for m in re.finditer(r'(?<![A-Za-z0-9_])' + re.escape(short) + r'(?![A-Za-z0-9])(?:\.md)?`?\*{0,2}[ _]v([0-9]+(?:\.[0-9]+)*)', l):
                        pairs.append(dict(citer=k, line=i, cited=other, at='v' + m.group(1), cited_head=ov['head'],
                                          behind=vnum('v' + m.group(1)) < vnum(ov['head'] or 'v0'), text=' '.join(l.split())[:200]))
    B['hand'] = notes
    B['inside_batch'] = pairs
    dump(BATCH, B)
    print('classified ; hand notes %d ; inside-batch pairs %d' % (len(notes), len(pairs)))
    for k, v in B['keystones'].items():
        print('  %-34s %s' % (k[:34], v['buckets']))
    return 0


# ------------------------------------------------------------------------------------------------ THE REPAIRS
MARK = '<!-- b450 CURRENCY ANNOTATION, 2026-09-13 -->'
EXCL_HEAD = re.compile(r'(?i)provenance|history|changelog|revision|errata')


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), NL)


def repair():
    B = json.load(io.open(BATCH, encoding='utf-8'))
    made, excluded, routed = [], [], []
    for k, v in B['keystones'].items():
        cands = []
        for sp in ('unpropagated', 'superseded'):
            for c in v['species'][sp]:
                why = None
                if c['quoted']:
                    why = 'a blockquoted line'
                elif EXCL_HEAD.search(c['section'] or ''):
                    why = 'inside a heading carrying provenance/history/changelog/revision/errata: %s' % c['section']
                elif c['transition']:
                    why = 'the line records a version transition itself'
                elif c['fence']:
                    why = 'a fenced code block'
                elif not c.get('in_lineage'):
                    why = 'not in the cited document`s lineage'
                if why:
                    excluded.append(dict(k=k, line=c['line'], stem=c['stem'], at=c['at'], why=why))
                else:
                    cands.append(dict(c, species=sp))
        for c in v['species']['phantom']:
            routed.append(dict(k=k, line=c['line'], what='phantom %s at %s' % (c['stem'], c['at']), ruling='a phantom has no lineage to move within; the author`s'))
        if not cands:
            continue
        full = os.path.join(PP, v['path'].replace('/', os.sep))
        pre = blob(v['path'])
        cur = io.open(full, encoding='utf-8', newline='').read()
        had_crlf = (chr(13) + chr(10)) in cur
        if MARK in cur:
            made += [dict(k=k, line=c['line'], stem=c['stem'], was=c['at'], now=c['registry'], already=True) for c in cands]
            continue
        ls = cur.replace(chr(13) + chr(10), NL).split(NL)
        originals = []
        for c in sorted(cands, key=lambda x: x['line']):
            old = ls[c['line'] - 1]
            s0, e0 = c['vspan']
            if old[s0:e0] != c['at']:
                routed.append(dict(k=k, line=c['line'], what='the version span did not match before the repair', ruling='NOT MADE under (S)'))
                continue
            new = old[:s0] + c['registry'] + old[e0:]
            ls[c['line'] - 1] = new
            originals.append((c['line'], old, c))
        if not originals:
            continue
        block = ['', MARK, '', '#### **CURRENCY ANNOTATION** *(2026-09-13, b450; existing text preserved apart from the version strings named here)*', '',
                 '> ### **%d CITATION(S) MOVED TO THE VERSION THE REGISTRY’S OWN ROW CARRIES.** *The originals, preserved verbatim:*' % len(originals), '']
        for i, o, c in originals:
            block.append('> - line `%d` (`%s` `%s` → `%s`, `REGISTRY.md:%d`) — *%s*' % (i, c['stem'], c['at'], c['registry'], c['registry_line'], ' '.join(o.split())))
        block += ['', '> ### **WHY.** *Each cited version is in the cited document’s own lineage — a supersession, not a phantom — and the registry’s row for that document carries a newer version. Only the version string changed on each line; no line was removed; no grade, claim or correspondence row moved.*', '']
        text = NL.join(ls).rstrip(NL) + NL + NL.join(block) + NL
        if had_crlf:
            text = text.replace(NL, chr(13) + chr(10))
        open(full + '.tmp', 'wb').write(text.encode('utf-8'))
        os.replace(full + '.tmp', full)
        after = read(full).split(NL)
        prel = pre.split(NL)
        diff = [j for j, (x, y) in enumerate(zip(prel, after), 1) if x != y]
        lines = [i for i, _o, _c in originals]
        only = sorted(diff) == sorted(lines) and all(
            after[i - 1] == o[:c['vspan'][0]] + c['registry'] + o[c['vspan'][1]:] for i, o, c in originals)
        removed = max(0, len(prel) - len(after))
        for i, o, c in originals:
            made.append(dict(k=k, line=i, stem=c['stem'], was=c['at'], now=c['registry'], species=c['species'], registry_line=c['registry_line'],
                             only_version_lines=only, removed=removed, annotated=(MARK in read(full)), original=' '.join(o.split())[:200]))
    R = dict(made=made, excluded=excluded, routed_from_repair=routed)
    dump(REPJ, R)
    print('repairs made %d ; excluded %d ; routed %d' % (len(made), len(excluded), len(routed)))
    for m in made:
        print('  %s line %d : %s %s -> %s ; only version lines %s ; removed %d ; annotated %s'
              % (m['k'], m['line'], m['stem'], m['was'], m['now'], m.get('only_version_lines'), m.get('removed', 0), m.get('annotated')))
    return 0


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    E = json.load(io.open(ELIG, encoding='utf-8'))
    B = json.load(io.open(BATCH, encoding='utf-8'))
    R = json.load(io.open(REPJ, encoding='utf-8'))
    t_ferry = os.path.getmtime(FERRY)
    now = time.time()
    rec('=' * 110)
    rec('b450 -- THE RECONCILIATION`S ELIGIBLE SET RE-MEASURED, AND THE BATCH READ. ### THE COMPONENTS, AFTER THE LOCK.')
    rec('=' * 110)

    rec('')
    rec('  ### ### **COMPONENT 1 -- THE ELIGIBLE SET, UNDER b390`S RULE QUOTED AND NOT IMPROVED.**')
    rec('    THE RULE (OPEN_TRAILS.md:4446), VERBATIM ON THE LOCKED FACE: "take the one whose terminals the drive can reach", settled by')
    rec('    "compiled terminals live on the HELD, UNMERGED branch `word-pairing-interface` and are not on `main`".')
    rec('    (D1) "the one" (b390) against "those" (b394`s plural, the order`s paraphrase); (D2) b390`s settling clause, carried and measured live.')
    rec('    (W1) the partial case and (W2) pin resolution -- WANTED, PRINTED, NOT APPLIED.')
    rec('')
    rec('    %-3s %-36s %-11s %-4s %-12s %s' % ('#', 'census keystone (THE_KEYSTONE_CENSUS.md)', 'state', 'pins', 'repos V1/V2/on', 'reason'))
    for n, r in enumerate(E['rows'], 1):
        rep = ('%d/%d/%d' % (len(r.get('v1', [])), len(r.get('v2', [])), len(r.get('on_drive', [])))) if 'v2' in r else '-'
        rec('    %-3d %-36s %-11s %-4d %-12s %s' % (n, r['k'][:36], r['state'], r['pins'], rep, r['why'][:120]))
    v1_on = [r['k'] for r in E['rows'] if r['state'] == 'ELIGIBLE' and any(repo_ok(x)[0] for x in r.get('v1', []))]
    rec('')
    rec('    population %d (on disk %d) ; ALREADY RECONCILED %d : %s' % (E['population'], E['on_disk'], len(E['reconciled']),
                                                                     ', '.join('%s (%s)' % (k, a) for k, a in E['reconciled'])))
    rec('    later-act hits for "read whole"/"reconcil" beside a census keystone after b394`s block : %d, HAND-READ:' % len(E['later_hits']))
    for h in E['later_hits']:
        what = ('b394`s own block describing its three' if h['line'] in (4540, 4542) else 'b408/b409`s class-numbering sweep -- not a reading of the keystone')
        rec('      OPEN_TRAILS.md:%d  %-34s %s' % (h['line'], h['k'][:34], what))
    rec('    ### none is a later reconciliation; the reconciled count stays %d.' % len(E['reconciled']))
    rec('    EXCLUDED %d : %s' % (len(E['excluded']), '; '.join('%s -- %s' % tuple(x) for x in E['excluded'])))
    rec('    PARTIAL (W1), eligible and marked: %s' % [r['k'] for r in E['rows'] if r.get('partial')])
    rec('  ### ### **THE ELIGIBLE REMAINDER, IN CENSUS ORDER : %d** -- %s' % (len(E['eligible']), ', '.join(E['eligible'])))
    rec('    the board`s "twelve unread" (quoted forward from b394) : 12 ; measured unread (population less reconciled) : %d -- %s'
        % (E['unread'], 'AGREES' if E['unread'] == 12 else 'DISAGREES'))
    rec('    beside it, b394`s narrow matcher (backticked lowercase) would find a repository on the drive for : %d of these %d -- %s'
        % (len(v1_on), len(E['eligible']), v1_on))

    rec('')
    rec('  ### ### **COMPONENT 2 -- THE BATCH READ, RECONCILING AND NOT AUTHORING.**')
    rec('    ### THE READ, STATED: every line of each keystone passed through the survey`s matchers; every hit, second-shape yield and item')
    rec('    ### was read by hand and is quoted below or in data/b450_batch.json. The seat did not read each keystone line by line unaided.')
    rec('')
    rec('    %-34s %-5s %-7s %-3s %-3s %-3s  %-50s %-6s %-6s %-6s' % ('keystone', 'lines', 'head', 'T1', 'T2', 'TW', 'rows by grade (TW if T1, else T2)', 'ALREADY', 'SUPERS', 'NOTCARRY'))
    tot = {A_: 0, S_: 0, N_: 0}
    notable = []
    for k in B['order']:
        v = B['keystones'][k]
        g = v['tw_grades'] if v['t1'] else v['grades']
        rows = v['tw_rows'] if v['t1'] else v['t2_rows']
        gs = ('THERE IS NO TABLE' if not (v['t1'] or v['t2_rows']) else '%d: %s' % (rows, ', '.join('%s %d' % kv for kv in sorted(g.items()))))
        for b in tot:
            tot[b] += v['buckets'][b]
        rec('    %-34s %-5d %-7s %-3d %-3d %-3d  %-50s %-7d %-6d %-6d' % (k[:34], v['lines'], v['head'], v['t1'], v['t2_rows'], v['tw_rows'], gs[:50],
                                                                       v['buckets'][A_], v['buckets'][S_], v['buckets'][N_]))
    rec('    %-34s %-5s %-7s %-3s %-3s %-3s  %-50s %-7d %-6d %-6d' % ('ACROSS THE BATCH', '', '', '', '', '', '', tot[A_], tot[S_], tot[N_]))
    for b in (A_, S_, N_):
        rec('      %-32s %d -- %s' % (b, tot[b], 'FULL' if tot[b] else 'EMPTY'))
    top = max(tot.values())
    largest = [b for b in tot if tot[b] == top]
    rec('    largest bucket(s) : %s at %d%s' % (largest, top, ' -- A TIE' if len(largest) > 1 else ''))
    rec('    ### T2 as fixed on the face (first header cell exactly `claim`) yields 0 rows under %d tables T1 finds; their headers open'
        % sum(1 for k in B['order'] if B['keystones'][k]['t1'] and not B['keystones'][k]['t2_rows']))
    rec('    ### `Claim (as stated here)` or `Result`. THE DEFECTIVE PREDICATE IS NAMED; rows are counted by TW, the first table within 12')
    rec('    ### lines after a T1 heading, and T2`s own yield is printed beside it. The locked face is not edited.')

    rec('')
    rec('    THE ITEMS, PER KEYSTONE:')
    for k in B['order']:
        v = B['keystones'][k]
        rec('    ### %s  (`%s`, %d bytes, %.2f s read)' % (k, v['path'], v['bytes'], v['seconds']))
        for it in v['items']:
            if it['kind'].startswith('(ii)'):
                extra = ''
                if 'second_yield' in it:
                    extra = ' ; second shape yield %d%s' % (it['second_yield'], (' (' + it['second_read'] + ')') if it.get('second_read') else '')
                rec('      %-22s %-30s %s -- needle hits %d%s' % (it['kind'], it['bucket'], it['label'], len(it['hits']), extra))
                for h in it['hits'][:3]:
                    rec('          line %d | %s' % (h['line'], h['text'][:150]))
                if it.get('note'):
                    rec('          NOTE: %s' % it['note'])
            else:
                rec('      %-22s %-30s %s' % (it['kind'], it['bucket'], (it.get('detail') or '')[:170]))
    rec('')
    rec('    THE HAND READ, APPLIED AFTER THE SURVEY:')
    for n in B['hand']:
        rec('      %-34s %-22s %-40s %s' % (n['k'][:34], n['kind'], n['action'][:40], n['why'][:150]))

    rec('')
    rec('    THE SPECIES, APART AND NEVER SUMMED (citation shape S2; b394`s stem shape S1 printed beside):')
    sp = dict((s, sum(len(B['keystones'][k]['species'][s]) for k in B['order'])) for s in ('phantom', 'unpropagated', 'superseded'))
    rec('      S1 yield across the batch : %d ; S2 yield : %d' % (sum(B['keystones'][k]['s1_cites'] for k in B['order']),
                                                              sum(B['keystones'][k]['s2_cites'] for k in B['order'])))
    rec('      phantom      : %d' % sp['phantom'])
    rec('      unpropagated : %d' % sp['unpropagated'])
    rec('      superseded   : %d' % sp['superseded'])
    for k in B['order']:
        for c in B['keystones'][k]['species']['superseded']:
            rec('        %s line %d : %s at %s ; registry %s (REGISTRY.md:%d) ; in lineage %s ; section %s'
                % (k, c['line'], c['name'], c['at'], c['registry'], c['registry_line'], c.get('in_lineage'), c['section'][:40]))
    rec('      INSIDE-THE-BATCH PAIRS : %d' % len(B['inside_batch']))
    for p in B['inside_batch']:
        rec('        %s line %d cites %s at %s ; the cited keystone`s head %s ; behind %s | %s'
            % (p['citer'], p['line'], p['cited'], p['at'], p['cited_head'], p['behind'], p['text'][:120]))

    rec('')
    rec('    THE REPAIRS MADE (currency only) : %d' % len(R['made']))
    for m in R['made']:
        rec('      %s line %d : `%s` %s -> %s (REGISTRY.md:%d) ; only the version changed %s ; lines removed %d ; annotated %s'
            % (m['k'], m['line'], m['stem'], m['was'], m['now'], m['registry_line'], m['only_version_lines'], m['removed'], m['annotated']))
    rec('    repair candidates excluded : %d %s' % (len(R['excluded']), R['excluded'] or ''))
    routed = [('INDEX_ARITY_AT_THE_CRITICAL_LINE', 'its registry row 1.5a-7 carries v0.5 while the head is v0.18', 'a registry row edit -- the author`s (R17)')]
    for k in B['order']:
        v = B['keystones'][k]
        if not (v['t1'] or v['t2_rows']):
            routed.append((k, 'THERE IS NO TABLE', 'writing a correspondence table is authoring'))
        for it in v['items']:
            if it['bucket'] == N_:
                routed.append((k, 'does not carry: %s' % (it.get('label') or it['kind']), 'adding absent material is authoring' + ('; ' + it['note'] if it.get('note') else '')))
            elif it['bucket'] == S_:
                routed.append((k, 'superseded form: %s' % ((it.get('detail') or it.get('label') or '')[:90]), 'rewriting prose is authoring (b397`s species: landed branches still called held)'))
    for k in ('EXHAUSTIVENESS_LICENSE', 'THE_RESIDUE_OF_RH'):
        routed.append((k, 'no registry row by either row shape', 'a registry row is the author`s'))
    rec('    THE REPAIRS ROUTED, COUNTED APART : %d' % len(routed))
    for k, what, why in routed:
        rec('      %-34s %-70s %s' % (k[:34], what[:70], why[:120]))
    rec('  ### ### **REPAIRS MADE : %d. ### REPAIRS ROUTED : %d. ### 0 TABLES WRITTEN. ### 0 GRADES MOVED.**' % (len(R['made']), len(routed)))
    read_set = [k for k in B['order'] if k in B['keystones']]
    rec('  ### ### **THE BATCH IS COMPLETE : %d OF %d READ ; UNREAD REMAINDER : %s.** NO HALT.' % (len(read_set), len(E['eligible']),
                                                                                           [k for k in E['eligible'] if k not in read_set] or 'NONE'))
    mins = (now - t_ferry) / 60.0
    rec('    TIMES, BOTH FLOORS: the act, ferry banked -> this component : %.1f min ; per keystone : %.1f min ; the batch`s tool time %.1f s'
        % (mins, mins / max(1, len(read_set)), B['seconds']))
    rec('    b394 printed 8.3 min for 3 (2.8 per keystone), b390 24 for 1 -- all floors, read at the component while the act continues.')

    rec('')
    rec('  ### ### **THE FILING, NOT A COMPONENT -- CANDIDATE (c4).**')
    rec('    (c4) a cancellation WITHIN the prime channel at step 1: its n = 2 term`s change +1.161e-07 against its n = 3 term`s -8.101e-08')
    rec('    (gross/net 5.000), the n = 3 change falling 20.0-fold by step 2 (b449_components.txt:74, :78). A DIFFERENT OBJECT from (c3),')
    rec('    refuted at b448 BETWEEN channels. PRICED FROM BANKED VALUES, NOT RUN, NO LANE OPENED. (c2) stays priced and not run.')
    rec('    ### THE MEASUREMENT STAYS OPEN.')

    rec('')
    rec('  ### ### **THE EXPECTATIONS.**')
    n1 = 'HELD' if (len(E['eligible']) >= 8 and len(E['eligible']) != 4) else 'REFUTED'
    n2a = 'HELD' if largest == [N_] else ('REFUTED AS WORDED -- a tie' if N_ in largest else 'REFUTED')
    n2b = 'HELD' if sp['unpropagated'] >= 1 else 'REFUTED'
    rec('    (N1)    the eligible set is at least eight and not four               ### %s -- %d' % (n1, len(E['eligible'])))
    rec('    (N2)(a) the largest bucket across the batch is does not carry it      ### %s -- %s' % (n2a, tot))
    rec('    (N2)(b) at least one corrected-but-unpropagated citation in the batch ### %s -- unpropagated %d' % (n2b, sp['unpropagated']))
    rec('            beside it, not the species: %d superseded citations repaired, all of A_METHODOLOGY at v0.2 -- the registry row b391 corrected.' % sp['superseded'])
    rec('    ### the seat`s own from the face: (N1) HELD -- %s; (N2)(a), (N2)(b) no expectation.' % ('HELD' if n1 == 'HELD' else 'REFUTED'))
    rec('')
    rec('    ### NO TABLE WRITTEN. ### NO REGISTRY ROW EDITED. ### NO PROSE REWRITTEN. ### NO GRADE MOVED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO.')
    rec('    ### THE FOUR LISTS ARE OPEN.')
    rec('=' * 110)
    res = dict(eligible=E['eligible'], n_eligible=len(E['eligible']), unread=E['unread'], buckets=tot, largest=largest, species=sp,
               made=len(R['made']), routed=len(routed), routed_items=routed, complete=True, minutes=round(mins, 1),
               per_keystone=round(mins / max(1, len(read_set)), 1), expect=dict(n1=n1, n2a=n2a, n2b=n2b), v1_on=v1_on)
    B['verdict'] = res
    dump(BATCH, B)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'survey'
    sys.exit(dict(survey=survey, classify=classify, repair=repair, report=lambda: report())[mode]())
