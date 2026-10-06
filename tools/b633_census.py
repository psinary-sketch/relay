# -*- coding: utf-8 -*-
"""b633_census.py -- THE ACT'S CENSUS READS, UNDER (R243)(6): THE_KEYSTONE_CENSUS AT v0.5.

### b619's resolvers (tools/b619_census.py, which imports b610's) are IMPORTED, never copied, and pointed at this act's pins: REGISTRY.md,
### the documents, SPIRAL_MAP.md, the sieve's v0.6 and OPEN_TRAILS.md at PLACE-papers e67c43b; the mirror roster at relay aabdee5e (this
### act's step zero); a dated append read since v0.4's commit 6a3069e. Every repository of the act root's list is read by ONE
### `git ls-remote origin` (its heads and its tags), cached, and the resolvers' tag reader is given the cache, so no repository is read
### twice. This module writes nothing: tools/b633_record.py banks what it returns.
### The act's own reads, beside b619's:
###   (i)   THE KERNEL COLUMN AT THE ROOT'S LIST -- every repository act_root.repositories() names at PLACE-papers e67c43b, its local main,
###         its remote main, its current tag at the remote by the peel, the tags its clone carries and the remote does not, the census rows
###         naming it, and its rows in the terminal table by provenance; relay and PLACE-papers read as the corpus's own repositories.
###   (ii)  THE FACES -- the explicit-formula kernel's rows at v0.22-v0.25 from the table, each at its grade with its named premises.
###   (iii) PROVENANCE PER CLUSTER -- for each census row, the table's rows of the kernels its kernel cell names, counted cell / rule / none.
###   (iv)  PHASE 2 AGAINST SEC -- SEC's theorems at v0.2.2 against the four syntheses, by two matchers (the short name as an identifier;
###         the name read as words), every hit printed with the seat's reading of it.
###   (v)   THE ANNEX -- the intake pilot's summary banks by digest, their figures; the paper's text absent.
###   (vi)  THE 42 NAMED PREMISES -- b632's census heads, each with the rows resting on it now, its kernel, the commits the table read those
###         rows at, and the ledger lines naming its discharge.
"""
import collections
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b619_census as C9  # noqa: E402
import b633_worklist as K  # noqa: E402

C = C9.C
NL = chr(10)
RELAY = ROOT.replace('\\', '/')

# ### b619's and b610's resolvers at this act's pins
C.PRE_PP = C9.PRE_PP = K.PRE_PP
C.STEPZERO = C9.STEPZERO = K.STEPZERO
C.SIEVE4 = C9.SIEVE5 = K.SIEVE6
C.TRACKED = None
C9.V03_PP = K.CEN4_PP

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '')


def repo_path(name):
    return {'relay': RELAY, 'PLACE-papers': K.PP}.get(name, 'D:/' + name)


# ================================================================================ (i) THE REMOTES, ONE READ EACH
LSR = {}
REMOTE = {}


def root_list():
    import act_root as AR
    return AR.repositories(K.PRE_PP)


def read_remote(name):
    """### ONE `git ls-remote origin` for a repository: its heads and its tags (peeled where the remote peels)."""
    if name in REMOTE:
        return REMOTE[name]
    p = repo_path(name)
    for _attempt in (1, 2):      # ### OPEN_TRAILS :12703: one read per repository, retried once alone when it returns nothing, both counted
        LSR[name] = LSR.get(name, 0) + 1
        r = subprocess.run(['git', '-C', p, 'ls-remote', 'origin'], capture_output=True, timeout=90)
        if r.returncode == 0 and b'\t' in r.stdout:
            break
    out = dict(repo=name, ok=r.returncode == 0 and b'\t' in r.stdout, heads={}, tags={}, err=r.stderr.decode('utf-8', 'replace').strip()[:160])
    tg = {}
    for l in r.stdout.decode('utf-8', 'replace').split(NL):
        if '\t' not in l:
            continue
        sha, ref = l.split('\t', 1)
        ref = ref.strip()
        if ref.startswith('refs/heads/'):
            out['heads'][ref[len('refs/heads/'):]] = sha
        elif ref.startswith('refs/tags/'):
            n = ref[len('refs/tags/'):]
            if n.endswith('^{}'):
                tg.setdefault(n[:-3], {})['peeled'] = sha
            else:
                tg.setdefault(n, {})['obj'] = sha
    out['tags'] = {k: v.get('peeled', v.get('obj')) for k, v in tg.items()}
    REMOTE[name] = out
    return out


def remote_tags(repo):
    """### b610's tag reader, answered from the one read: the same shape it returned."""
    r = read_remote(repo)
    return dict(repo=repo, via='origin of %s (one read)' % repo_path(repo), ok=r['ok'], err=r['err'], tags=dict(r['tags']))


C.remote_tags = remote_tags


def kernel_column(table_rows, J):
    out = []
    by_prov = collections.defaultdict(collections.Counter)
    for t in table_rows:
        by_prov[t['repo']][t.get('provenance') or 'none'] += 1
    naming = collections.defaultdict(list)
    for row in J:
        for k in row['kernel_src']:
            naming[k].append(row['n'])
    for name in root_list():
        rt = read_remote(name)
        p = repo_path(name)
        corpus = name in ('relay', 'PLACE-papers')
        cur = C.current_tag(dict(tags=rt['tags'])) if (rt['ok'] and rt['tags'] and not corpus) else None
        local_only = C.local_only_tags(name, dict(ok=rt['ok'], tags=rt['tags'])) if not corpus else []
        out.append(dict(repo=name, corpus=corpus, ok=rt['ok'], err=rt['err'], local_main=g(p, 'rev-parse', 'main').strip(),
                        remote_main=rt['heads'].get('main'), current=cur, peel=rt['tags'].get(cur) if cur else None,
                        local_peel=(C.local_peel(name, cur) if cur else None), local_only=local_only, rows=naming.get(name, []),
                        table=dict(by_prov.get(name, {}))))
    return out


# ================================================================================ THE TABLE, THE RULE'S READING
def table_rows(rev='HEAD'):
    return json.loads(subprocess.run(['git', '-C', RELAY, 'show', '%s:data/terminal_table.json' % rev], capture_output=True).stdout.decode('utf-8'))['rows']


def rule_full(statement, name):
    import b632_record as R2
    return R2.rule_full(statement, name)


def premise_name(t, head):
    import b632_record as R2
    return R2.premise_name(t, head)


# ================================================================================ (ii) THE FACES
def faces(rows):
    out = []
    for fid, label, tag, sha, prefix, path in K.FACES:
        rs = [r for r in rows if r['repo'] == 'SIDE-explicit-formula' and (r['name'].startswith(prefix) if prefix.endswith('.') else r['name'] == prefix)]
        items = []
        for r in sorted(rs, key=lambda x: x['name']):
            k, gr, why, prem, head = rule_full(r.get('statement'), r['name'])
            items.append(dict(name=r['name'], grade=r['grade'], provenance=r.get('provenance'), premises=['%s : %s' % bt for bt in prem]))
        tagc = g(K.KER, 'rev-parse', '--short=7', tag + '^{commit}').strip()
        out.append(dict(id=fid, label=label, tag=tag, commit=tagc, want=sha, path=path, items=items))
    return out


# ================================================================================ (iii) PROVENANCE PER CLUSTER
def provenance_by_row(J, rows):
    by = collections.defaultdict(collections.Counter)
    for t in rows:
        by[t['repo']][t.get('provenance') or 'none'] += 1
    out = {}
    for row in J:
        c = collections.Counter()
        for k in row['kernel_src']:
            c.update(by.get(k, {}))
        out[row['n']] = dict(cell=c.get('cell', 0), rule=c.get('rule', 0), none=c.get('none', 0), kernels=sorted(row['kernel_src']))
    return out


# ================================================================================ (iv) PHASE 2 AGAINST SEC
SEC_READ = {   # ### the seat's reading of each hit the matchers can return, keyed by (synthesis, SEC name); an unread hit is printed UNREAD
    ('2B', 'interface_dark'): 'the words name the cognitive variable "Interface Darkness" (its title and its rows UC and ID, :1, :18, :20, :50), '
                              'a different object from SEC`s interface_dark, the statement interface_size = 0 over the code`s own defined size',
    ('2F', 'formation_total_seven'): 'the name is SIDE-bsd-formation-transfer`s own declaration (its Basic.lean :67, cited at 2F :216), not '
                                     'SEC`s formation_total_seven; two kernels carry the short name',
}


def sec_against_phase2(rows):
    sec = [r for r in rows if r['repo'] == 'SIDE-structural-error-correction' and (r.get('statement') or '').lstrip().startswith(('theorem', 'lemma'))]
    heads = sorted(set(r['head'][:7] for r in sec))
    out = []
    for rid, key, path in K.PHASE2:
        t = K.show(path) or ''
        tl = t.lower()
        hits = []
        for r in sec:
            s = r['name'].split('.')[-1]
            ident = [i for i, l in enumerate(t.split(NL), 1) if re.search(r'(?<![\w.])' + re.escape(s) + r'(?![\w])', l)]
            words = s.replace('_', ' ').lower()
            phrase = [i for i, l in enumerate(tl.split(NL), 1) if len(words.split()) >= 2 and words in l]
            if ident or phrase:
                hits.append(dict(name=s, ident=ident, phrase=phrase, statement=' '.join((r.get('statement') or '').split()),
                                 reading=SEC_READ.get((key, s), 'UNREAD')))
        kv = [h for h in hits if h['reading'] == 'UNREAD']
        out.append(dict(row=rid, key=key, path=path, sec_mentions=len(re.findall(r'structural-error-correction|StructuralErrorCorrection|DeAlignment', t)),
                        hits=hits, names=False if not kv else None,
                        why=('no SEC terminal is named: the text carries no SEC repository or module name, and %s' % (
                            '; '.join('%s -- %s' % (h['name'], h['reading']) for h in hits) if hits else 'neither matcher returns a hit'))))
    return dict(theorems=len(sec), heads=heads, rows=out)


# ================================================================================ (v) THE ANNEX
def intake():
    out = []
    for p in K.INTAKE:
        b = subprocess.run(['git', '-C', RELAY, 'show', 'HEAD:' + p], capture_output=True).stdout
        out.append(dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b)))
    J = json.loads(subprocess.run(['git', '-C', RELAY, 'show', 'HEAD:' + K.INTAKE[1]], capture_output=True).stdout.decode('utf-8'))
    return dict(banks=out, claims=J.get('claims'), grades=J.get('grades'), kv=J.get('kv'), clusters=J.get('clusters'))


# ================================================================================ (vi) THE 42 NAMED PREMISES
def premise_table(rows):
    M = json.loads(subprocess.run(['git', '-C', RELAY, 'show', '%s:data/b632_rule_moves.json' % K.PRE_RELAY], capture_output=True).stdout.decode('utf-8'))
    heads = sorted(M['named'])
    rest = collections.defaultdict(list)
    for r in rows:
        if r.get('provenance') != 'rule' or r['grade'] != 'INTERFACES':
            continue
        k, gr, why, prem, head = rule_full(r.get('statement'), r['name'])
        for _b, t in prem:
            nm, _w = premise_name(t, head)
            if nm:
                rest[nm].append(r)
    ledgers = {}
    for f in ('FINDINGS.md', 'OPEN_TRAILS.md'):
        ledgers[f] = (K.show(f) or '').split(NL)
    out = []
    for h in heads:
        rs = {(r['repo'], r['name']): r for r in rest.get(h, [])}
        disc = []
        for f, ls in ledgers.items():
            for i, l in enumerate(ls, 1):
                if re.search(r'(?<![\w.])' + re.escape(h) + r'(?![\w])', l) and re.search(r'discharg', l, re.I):
                    disc.append('%s :%d' % (f.replace('.md', ''), i))
        out.append(dict(head=h, b632_rows=M['named'][h], rows=len(rs), names=sorted(n for _r, n in rs),
                        kernels=sorted(set(r for r, _n in rs)), commits=sorted(set(x['head'][:7] for x in rs.values())), discharge=disc))
    ung = [r for r in rows if r.get('provenance') == 'rule' and r['grade'] == 'INTERFACES']
    return dict(heads=out, sum_rows=sum(x['rows'] for x in out), rule_interfaces=len(ung),
                table_interfaces=sum(1 for r in rows if r['grade'] == 'INTERFACES'))


# ================================================================================ v0.4'S CELLS
def v04_cells(rev=K.PRE_PP):
    """### census v0.4's §1 rows at the pin, each split to its eight cells: {R01: {col: text}}"""
    out = {}
    for l in C.lines_of(K.show(K.CEN4, rev)):
        m = re.match(r'^\| (R\d\d) \| ', l)
        if not m or not l.endswith(' |') or m.group(1) in out:
            continue
        c = [x.strip() for x in l.strip().strip('|').split(' | ')]
        if len(c) != 8:
            continue
        out[m.group(1)] = dict(line=l, label=c[1], documents=c[2], keystones=c[3], editions=c[4], sieve=c[5], kernels=c[6], deposit=c[7])
    return out


def build():
    """### every read at once: b619's build at this act's pins with the one-read cache, and (i)-(vi); RETURN a dict for the bank."""
    for name in root_list():
        read_remote(name)
    B = C9.build(read_remotes=True)
    rows = table_rows('HEAD')
    J = B['J']
    for row in J:          # ### b619's renderer names its own edition in the census row; the edition this act writes is v0.5
        row['editions'] = [e.replace('(v0.4 this edition, beside it)', '(v0.5 this edition, beside it)') for e in row['editions']]
        row['table_line'] = C9.table_line(row)
    return dict(B=B, J=J, old=v04_cells(), column=kernel_column(rows, J), faces=faces(rows), prov=provenance_by_row(J, rows),
                sec=sec_against_phase2(rows), intake=intake(), premises=premise_table(rows), lsr=dict(LSR), roots=root_list())


if __name__ == '__main__':
    X = build()
    print('### root list: %d ; reads %s' % (len(X['roots']), sum(X['lsr'].values())))
    for row in X['J']:
        o = X['old'].get(row['n'], {})
        diff = [c for c in C9.COLS if (' ; '.join(row[c]) if isinstance(row[c], list) else row[c]) != o.get(c)]
        print('%s %-40s changed %s' % (row['n'], row['label'][:40], diff))
