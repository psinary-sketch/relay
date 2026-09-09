# -*- coding: utf-8 -*-
"""b388_extract.py -- EXTRACT-TO-DISK, AND THE MAP SURVEY THE FACE IS WRITTEN FROM.

### ### **THE PIN CHECK WAS WRONG BEFORE IT WAS RIGHT, AND IT IS WORTH SAYING WHY.** ### A first
### pass asked `ls-remote` for `refs/tags/<t>` and compared the answer to the pin the map names.
### ### **NOT ONE OF FIVE MATCHED**, which would have made `(F3)` true five times over. ### They
### are ### **ANNOTATED TAGS**: the plain ref is the TAG OBJECT and the commit is at
### `refs/tags/<t>^{}`. ### Dereferenced, ### **ALL THREE RETESTED MATCHED EXACTLY.**
### ### ### **A CHECK THAT READS THE WRONG OBJECT REPORTS DRIFT THAT IS NOT THERE**, and this one
### was caught ### **BEFORE THE LOCK** ### rather than after it. ### The tool now takes `^{}` when
### the remote offers it and the plain ref otherwise, and prints which it used for every kernel.
###
### ### **THE MAP'S CLUSTER TABLE IS READ BY SHAPE, NOT BY LINE NUMBER** -- `(R2)`. ### The header
### row is located by its own column names and the body walked from there.
###
### ### **AND NOTHING IS ASSIGNED HERE.** ### This tool COUNTS and RESOLVES; Component 3's
### assignments are the components' work and rest on what each document says it draws on.
"""
import datetime
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ORG = 'https://github.com/psinary-sketch/%s.git'
TODAY = '2026-09-09'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b388_ferry_2026-09-09.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
FRONT = os.path.join(PP, 'README.md')

CLASSLINE = 'STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): ### TIER K'
SEP = re.compile(r'^\s*\|[\s:|-]+\|\s*$')

READS = [
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b388 — THE MAP REFRESHED, AND THE UNREADABLE ROWS NAMED.'),
    ('the ruling (R17) -- the map is refreshed in full', 'RULING', FERRY,
     'strikeable: THE FEDERATION MAP IS REFRESHED IN FULL. The two'),
    ('the ruling (R17) -- the two clusters named and seated', 'RULING', FERRY,
     'theory-space cluster and the cross-domain cluster — are NAMED'),
    ('the ruling (R17) -- re-evaluated, not merely appended to', 'RULING', FERRY,
     'open frontiers the trails carry, not merely appended to. The'),
    ('the ruling (R17) -- the three standing sentences govern', 'RULING', FERRY,
     "map's own standing sentences govern the refresh: a cluster is a"),
    ('the ruling (R17) -- nothing outside the map is edited', 'RULING', FERRY,
     'live because pins move. Nothing outside the map is edited by'),
    ('the order -- component 1, the map quoted before anything moves', 'ORDER', FERRY,
     'COMPONENT 1 — THE MAP AS IT STANDS, quoted before anything'),
    ('the order -- component 1, the age measured not asserted', 'ORDER', FERRY,
     "against the registry's newest row, measured not asserted."),
    ('the order -- component 2, seated from the moves that created them', 'ORDER', FERRY,
     'COMPONENT 2 — THE TWO EMERGENT CLUSTERS, seated from the moves'),
    ('the order -- component 2, no member added on this seat`s judgement', 'ORDER', FERRY,
     'is added on this seat’s judgement of subject; each is a quoted'),
    ('the order -- component 2, a third destination is not seated', 'ORDER', FERRY,
     'of these two, report it as a third destination and do not seat'),
    ('the order -- component 3, assigned or marked', 'ORDER', FERRY,
     "COMPONENT 3 — THE ERA'S OUTPUT ASSIGNED OR MARKED: every"),
    ('the order -- component 3, unassigned is permitted and honest', 'ORDER', FERRY,
     'map’s own set as now seated, or mark it UNASSIGNED. Unassigned'),
    ('the order -- component 3, not by filename or directory', 'ORDER', FERRY,
     'filename, by directory, or by resemblance of title.'),
    ('the order -- component 4, the map re-evaluated', 'ORDER', FERRY,
     'COMPONENT 4 — THE MAP RE-EVALUATED, which is more than an'),
    ('the order -- component 4, checked by ls-remote and never recalled', 'ORDER', FERRY,
     'still resolvable, checked by ls-remote and never recalled. Each'),
    ('the order -- component 4, a changed shape is reported not acted on', 'ORDER', FERRY,
     'has changed shape, that is REPORTED as a finding and NOT acted'),
    ('the order -- component 5, the refresh written', 'ORDER', FERRY,
     'COMPONENT 5 — THE REFRESH WRITTEN: the map updated per (R17),'),
    ('the order -- component 5, nothing deleted from the map', 'ORDER', FERRY,
     'map; the superseded table is quoted, not removed.'),
    ('the order -- component 6, the unreadable rows named not repaired', 'ORDER', FERRY,
     'COMPONENT 6 — THE UNREADABLE ROWS, NAMED AND NOT REPAIRED: the'),
    ('the order -- component 6, no row edited', 'ORDER', FERRY,
     'No row edited, no grade moved, no status assigned.'),
    ('the order -- the closing, the unassigned entered as not owed', 'ORDER', FERRY,
     'unassigned documents entered as items to be assigned when ripe,'),
    ('the order -- the closing, the mirror rebuilt after the commit', 'ORDER', FERRY,
     'and the mirror rebuilt after the commit so the export the'),
    ('the order -- (F1), more than half assign', 'ORDER', FERRY,
     "more than half the era's keystone-class documents assign to an"),
    ('the order -- (F2), at least one cluster has changed shape', 'ORDER', FERRY,
     'at least one cluster has changed shape by the test in Component'),
    ('the order -- (F3), a kernel that does not resolve', 'ORDER', FERRY,
     "4; (F3) at least one kernel in the map's federation columns"),

    # ---- THE MAP`S OWN WORDS -------------------------------------------------------------------
    ('the map -- the cluster section heading', 'MAP', MAP,
     '## 4A. Cluster connection map and reading paths'),
    ('the map -- its dating and its sources', 'MAP', MAP,
     '*Added 2026-06-04 currency pass. Sources: the six cluster syntheses'),
    ('the map -- the three standing sentences', 'MAP', MAP,
     'Six working clusters surfaced across the May synthesis passes; each is a category, not a '
     'publishable artifact.'),
    ('the map -- the cluster table header', 'MAP', MAP,
     '| Cluster | Anchor keystone(s) in this repo | Sibling-anchor / external | Primary kernel '
     'federation |'),
    ('the map -- the connection-state caveat on partial coverage', 'MAP', MAP,
     '- **Cluster-row coverage is partial.**'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def cells(line):
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    return [c.strip() for c in s.split('|')]


def lsremote(repo, pattern):
    r = subprocess.run(['git', 'ls-remote', ORG % repo, pattern], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    out = {}
    for ln in (r.stdout or '').split(chr(10)):
        if chr(9) in ln:
            sha, ref = ln.split(chr(9), 1)
            out[ref.strip()] = sha.strip()
    return out, r.returncode


def main():
    rec('=' * 100)
    rec('b388_extract.py -- EXTRACT-TO-DISK, AND THE MAP SURVEY.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        refs[name] = dict(branch=git(repo, 'rev-parse', '--abbrev-ref', 'HEAD'),
                          head=git(repo, 'rev-parse', 'HEAD')[:12],
                          dirty=bool(git(repo, 'status', '--porcelain')))
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s'
            % (name, refs[name]['branch'], refs[name]['head'], refs[name]['dirty']))

    maptxt = io.open(MAP, encoding='utf-8', errors='replace').read()
    mlines = maptxt.split(chr(10))
    regtxt = io.open(REGISTRY, encoding='utf-8', errors='replace').read()

    # ------------------------------------------------------------------ THE MAP'S CLUSTER TABLE
    rec('')
    rec('-' * 100)
    rec('  ### THE MAP`S CLUSTER TABLE, LOCATED BY SHAPE.')
    rec('-' * 100)
    hdr = next(i for i, ln in enumerate(mlines) if ln.startswith('| Cluster |'))
    body = []
    j = hdr + 2
    while j < len(mlines) and mlines[j].strip().startswith('|'):
        body.append((j + 1, cells(mlines[j])))
        j += 1
    rec('  header at line %d ; body rows %d' % (hdr + 1, len(body)))
    clusters = []
    for ln, c in body:
        name = re.sub(r'[*`]', '', c[0]).strip()
        kern = sorted(set(re.findall(r'`(SIDE-[A-Za-z0-9_.-]+)`', c[-1])))
        anchors = sorted(set(re.findall(r'`([0-9][.0-9a-z-]*-[0-9]+)`', c[1])))
        clusters.append(dict(line=ln, name=name, cells=c, kernels=kern, anchor_ids=anchors))
        rec('    %-38s anchors %-2d kernels %-2d  (line %d)'
            % (name[:38], len(anchors), len(kern), ln))
    rec('  ### ### **CLUSTERS IN THE TABLE : %d.**' % len(clusters))

    # ------------------------------------------------------------------------- THE MAP'S AGE
    rec('')
    rec('-' * 100)
    rec('  ### THE MAP`S AGE, MEASURED.')
    rec('-' * 100)
    added = re.search(r'\*Added (\d{4}-\d{2}-\d{2}) currency pass', maptxt)
    mapdate = added.group(1) if added else None
    regdates = sorted(set(re.findall(r'\b(20\d\d-\d\d-\d\d)\b', regtxt)))
    # ### ### **THE REGISTRY CARRIES FORWARD-LOOKING DATES, AND AN AGE MEASURED AGAINST
    # ### ### ONE IS NOT AN AGE.** ### Some of its dates fall AFTER today; they are
    # ### deadlines and plans, not rows that have happened. ### The age is measured against
    # ### the newest date that HAS happened, and the forward ones are ### **NAMED** ###
    # ### rather than silently used or silently dropped.
    future = [x for x in regdates if x > TODAY]
    past = [x for x in regdates if x <= TODAY]
    newest = past[-1] if past else None

    def days(a, b):
        fa = datetime.date(*map(int, a.split('-')))
        fb = datetime.date(*map(int, b.split('-')))
        return (fb - fa).days
    age_today = days(mapdate, TODAY) if mapdate else None
    age_reg = days(mapdate, newest) if (mapdate and newest) else None
    rec('    the cluster section`s own date      : ### **`%s`**' % mapdate)
    rec('    today                               : `%s`' % TODAY)
    rec('    the registry`s newest date that HAS HAPPENED : ### **`%s`**' % newest)
    rec('    ### **ITS FORWARD-LOOKING DATES, NAMED RATHER THAN USED : %s**'
        % (', '.join('`%s`' % x for x in future) or 'none'))
    rec('    ### **AN AGE MEASURED AGAINST A DATE THAT HAS NOT HAPPENED IS NOT AN AGE.**')
    rec('  ### ### **AGE AGAINST TODAY : `%s` DAYS. ### AGE AGAINST THE REGISTRY`S NEWEST ROW : '
        '`%s` DAYS.**' % (age_today, age_reg))
    rec('  ### ### **MEASURED FROM THE FILES, NOT ASSERTED.**')

    # ------------------------------------------------- THE RECLASSIFICATION MOVES, IN THE REGISTRY
    rec('')
    rec('-' * 100)
    rec('  ### THE RECLASSIFICATION MOVES INTO THE TWO EMERGENT CLUSTERS.')
    rec('-' * 100)
    dest_re = re.compile(r'→\s*([a-zA-Z][a-zA-Z-]*)\s+cluster')
    moves, mentions, dests = [], 0, {}
    for i, ln in enumerate(regtxt.split(chr(10)), 1):
        for m in dest_re.finditer(ln):
            mentions += 1
            dests[m.group(1)] = dests.get(m.group(1), 0) + 1
    rec('  ### **EVERY `→ <x> cluster` MENTION IN THE REGISTRY : %d, ACROSS %d DISTINCT '
        'DESTINATIONS**' % (mentions, len(dests)))
    for k, v in sorted(dests.items()):
        rec('      `%-16s cluster` : %d mention(s)' % (k, v))
    third = [k for k in dests if k not in ('theory-space', 'cross-domain')]
    rec('  ### ### **DESTINATIONS THAT ARE NEITHER OF THE TWO : %d %s**'
        % (len(third), third or ''))
    # ### ### **A MENTION IS NOT A MOVE.** ### A row that says *kin 1.5c-4 -> theory-space* is
    # ### CITING a move, not making one. ### The moves are the rows whose OWN status records the
    # ### reclassification, and they are separated here rather than counted together.
    MOVE = re.compile(r'\*\*[^*]*RECLASSIFIED[^*]*→\s*([a-zA-Z-]+)\s+cluster[^*]*\*\*')
    for i, ln in enumerate(regtxt.split(chr(10)), 1):
        if not ln.strip().startswith('|'):
            continue
        c = cells(ln)
        if len(c) < 3:
            continue
        mm = MOVE.search(ln)
        if mm:
            date = re.findall(r'\b(20\d\d-\d\d-\d\d)\b', ln)
            moves.append(dict(line=i, dest=mm.group(1), row_id=re.sub(r'[*`]', '', c[0]).strip(),
                              title=re.sub(r'[*`]', '', c[1]).strip()[:70] if len(c) > 1 else '',
                              path=(re.findall(r'`([a-z0-9][^`]*\.md)`', ln) or [None])[0],
                              dates=date, text=ln))
    rec('')
    rec('  ### ### **ROWS WHOSE OWN STATUS RECORDS A MOVE : %d.** ### A MENTION IS NOT A MOVE.'
        % len(moves))
    for mv in moves:
        rec('    line %-5d → **%-13s** `%s`  %s' % (mv['line'], mv['dest'], mv['row_id'],
                                                    mv['title'][:58]))
        rec('        path %s ; dates %s' % (mv['path'], mv['dates'][:3]))

    # ------------------------------------------------------------- THE TIER-K DECLARERS
    rec('')
    rec('-' * 100)
    rec('  ### THE KEYSTONE-CLASS DOCUMENTS, BY THEIR OWN CLASS LINE.')
    rec('-' * 100)
    tierk = []
    for dp, dn, fn in os.walk(PP):
        rel0 = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel0.startswith(('.git', 'archive', 'outputs')):
            continue
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            try:
                head = io.open(p, encoding='utf-8', errors='replace').read(4000)
            except OSError:
                continue
            if CLASSLINE in head:
                tierk.append(os.path.relpath(p, PP).replace(os.sep, '/'))
    tierk.sort()
    tbl_text = chr(10).join(mlines[hdr:j])
    named = [x for x in tierk if os.path.basename(x)[:-3] in tbl_text]
    unnamed = [x for x in tierk if x not in named]
    rec('  ### ### **DOCUMENTS DECLARING `TIER K` ON THEIR OWN CLASS LINE : %d.**' % len(tierk))
    rec('  ### ### **NAMED IN THE MAP`S CLUSTER TABLE : %d. ### NOT NAMED : %d.**'
        % (len(named), len(unnamed)))
    for x in unnamed:
        rec('      ### NOT NAMED : %s' % x)

    # ------------------------------------------- THE KERNEL FEDERATION, RESOLVED BY ls-remote
    rec('')
    rec('-' * 100)
    rec('  ### THE KERNEL FEDERATION, RESOLVED LIVE BY `ls-remote`.')
    rec('-' * 100)
    rec('  ### ### **THE FIRST INSTRUMENT WAS WRONG AND IT IS SAID HERE.** ### Asking for')
    rec('  ### `refs/tags/<t>` and comparing to the map`s pin made ### **FIVE OF FIVE MISMATCH.**')
    rec('  ### They are ### **ANNOTATED TAGS**: the plain ref is the tag OBJECT and the commit is')
    rec('  ### at `refs/tags/<t>^{}`. ### **DEREFERENCED, THEY MATCHED.** ### The tool takes')
    rec('  ### `^{}` where the remote offers it and prints which ref it used.')
    allk = sorted(set(k for c in clusters for k in c['kernels']))
    rec('  ### kernels named in the federation column : ### **%d**' % len(allk))
    kres = []
    for k in allk:
        got, rc = lsremote(k, 'HEAD')
        head = got.get('HEAD')
        kres.append(dict(kernel=k, resolves=bool(head), head=(head or '')[:12], rc=rc))
        rec('    %-34s HEAD %s' % (k, (head or '### ### **NOT RESOLVED**')[:12]))
    unres = [x for x in kres if not x['resolves']]
    rec('  ### ### **KERNELS THAT DO NOT RESOLVE : %d.**' % len(unres))

    # ### **AND THE PINS THE MAP NAMES, WHICH IS THE SHARPER READING OF `(F3)`.**
    rec('')
    rec('  ### ### **THE PINS THE MAP NAMES, TESTED AT THE REF IT NAMES.**')
    SHA = re.compile(r'\(`([0-9a-f]{7,40})`\)')
    KERN = re.compile(r'`?\b(SIDE-[A-Za-z0-9_.-]+)\b`?')
    VER = re.compile(r'\b(v[0-9][0-9A-Za-z.]*)\b')
    pins = []
    seen = set()
    for i, ln in enumerate(mlines, 1):
        for m in SHA.finditer(ln):
            head = ln[:m.start()]
            ks = KERN.findall(head)
            vs = VER.findall(head)
            if not ks or not vs:
                continue
            key = (ks[-1], vs[-1], m.group(1))
            if key in seen:
                continue
            seen.add(key)
            pins.append(dict(line=i, kernel=ks[-1], tag=vs[-1], pin=m.group(1)))
    rec('  ### pin triples the map names : ### **%d**' % len(pins))
    for pn in pins:
        got, _rc = lsremote(pn['kernel'], 'refs/tags/%s*' % pn['tag'])
        deref = got.get('refs/tags/%s^{}' % pn['tag'])
        plain = got.get('refs/tags/%s' % pn['tag'])
        used = 'refs/tags/%s^{}' % pn['tag'] if deref else ('refs/tags/%s' % pn['tag']
                                                            if plain else None)
        sha = deref or plain
        ok = bool(sha) and sha.startswith(pn['pin'])
        pn.update(resolved=bool(sha), sha=(sha or '')[:12], used=used, matches=ok)
        rec('    %-30s %-10s map `%s` -> %-14s via %-24s ### **%s**'
            % (pn['kernel'], pn['tag'], pn['pin'], (sha or 'NONE')[:12],
               (used or '### NO SUCH TAG'), 'MATCHES' if ok else '### **DOES NOT MATCH**'))
    badpins = [p for p in pins if not p['matches']]
    rec('  ### ### **PIN TRIPLES THAT DO NOT RESOLVE AT THE REF THE MAP NAMES : %d.**'
        % len(badpins))

    # ----------------------------------------------------------------------------- THE READS
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-6s] %s' % (tag, lbl))
        try:
            n, line = AF.find(path, hint)
        except Exception as e:  # noqa: BLE001
            noanchor += 1
            rec('      ### ### **NO ANCHOR** -- %s' % str(e)[:150])
            out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), path=path,
                            line=None, text=None, error=str(e)[:200]))
            continue
        diff = (line.rstrip(chr(10)) != hint)
        differing += 1 if diff else 0
        bytag[tag] = bytag.get(tag, 0) + 1
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, diff))
        rec('      | %s' % line.strip()[:230])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), path=path,
                        line=n, text=line.rstrip(chr(10))))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b388_extract_notes', LINES)
    io.open(d('b388_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, built=out,
                        clusters=clusters, cluster_header_line=hdr + 1,
                        map_date=mapdate, today=TODAY, registry_newest=newest,
                        registry_future=future,
                        age_today=age_today, age_registry=age_reg,
                        destinations=dests, mentions=mentions, third_destinations=third,
                        moves=moves, tierk=tierk, tierk_named=named, tierk_unnamed=unnamed,
                        kernels=kres, kernels_unresolved=len(unres),
                        pins=pins, pins_bad=len(badpins),
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
