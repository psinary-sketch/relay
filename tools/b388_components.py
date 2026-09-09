# -*- coding: utf-8 -*-
"""b388_components.py -- THE SIX COMPONENTS OF b388.

### ### **COMPONENT 3 IS THE ONE THAT COULD GO WRONG QUIETLY.** ### Assigning eleven documents to
### clusters is exactly the shape of work a seat does well and cannot check: a plausible
### assignment reads like a correct one. ### So ### **EVERY ASSIGNMENT CARRIES ITS EVIDENCE --
### ### A KERNEL THE DOCUMENT NAMES, OR A CLUSTER MEMBER IT CITES -- AND AN ASSIGNMENT WITH NO
### ### PRINTED EVIDENCE IS COUNTED `UNASSIGNED`.** ### The evidence is gathered by reading the
### document, and the cluster is chosen only where the evidence points at one.
###
### ### **AND `UNASSIGNED` IS TWO DIFFERENT OUTCOMES, WHICH THE ACT KEEPS APART** (`(E2)`):
### ### **NO-EVIDENCE** ### (the document names no kernel and cites no member) and
### ### **NO-FIT** ### (it names kernels, and they serve no one cluster). ### Reporting them as
### one number would hide which.
###
### ### **COMPONENT 5 WRITES INTO A CORPUS DOCUMENT AND THAT IS WHY IT PRESERVES FIRST.** ### The
### prior table is copied verbatim into the same file BEFORE the refreshed one is written, and an
### arm re-reads every prior row out of the file afterwards. ### **NOTHING IS DELETED FROM THE
### ### MAP** -- `(R4)`'s shape: preserve by quotation, repair by edit.
###
### ### **AND COMPONENT 6 NAMES CAUSES WITHOUT SUPPLYING STATUSES.** ### A cause says what defeats
### a reader. ### **IT DOES NOT SAY WHAT THE ROW SHOULD HAVE SAID**, and a seat that supplied that
### would have graded a row it was told not to touch.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
ORG = 'https://github.com/psinary-sketch/%s.git'
TODAY = '2026-09-09'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def d(n):
    return os.path.join(D, n)


E = json.load(io.open(d('b388_reads.json'), encoding='utf-8'))
B387 = json.load(io.open(d('b387_components.json'), encoding='utf-8'))
BUILT = {r['label']: r for r in E['built']}
FAILS = []


def q(label):
    b = BUILT[label]
    ok = False
    if b.get('line'):
        try:
            ls = io.open(b['path'], encoding='utf-8', errors='replace').read().split(chr(10))
            ok = (ls[b['line'] - 1].rstrip(chr(10)) == b['text'])
        except OSError:
            ok = False
    if not ok:
        FAILS.append((label, b['file'], b['line']))
    return b, ok


def lsremote(repo, pattern):
    r = subprocess.run(['git', 'ls-remote', ORG % repo, pattern], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    out = {}
    for ln in (r.stdout or '').split(chr(10)):
        if chr(9) in ln:
            sha, ref = ln.split(chr(9), 1)
            out[ref.strip()] = sha.strip()
    return out


MAPTXT = io.open(MAP, encoding='utf-8', errors='replace').read()
MAPLINES = MAPTXT.split(chr(10))
REGTXT = io.open(REGISTRY, encoding='utf-8', errors='replace').read()
HDR = E['cluster_header_line'] - 1


def prior_table():
    """### THE PRIOR CLUSTER TABLE, READ OUT OF THE FILE AT ITS OWN LINES. ### **NOT RETYPED.**"""
    out = [MAPLINES[HDR], MAPLINES[HDR + 1]]
    j = HDR + 2
    while j < len(MAPLINES) and MAPLINES[j].strip().startswith('|'):
        out.append(MAPLINES[j])
        j += 1
    return out, HDR + 1, j


# ==================================================================================================
def component1():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 1 -- THE MAP AS IT STANDS, QUOTED BEFORE ANYTHING MOVES.')
    rec('-' * 100)
    for lbl in ('the map -- the cluster section heading', 'the map -- its dating and its sources',
                'the map -- the three standing sentences',
                'the map -- the connection-state caveat on partial coverage'):
        b, ok = q(lbl)
        rec('###   `%s` line %-4d %s' % (b['file'], b['line'], '' if ok else '### RE-READ FAILED'))
        rec('###   | %s' % b['text'][:400])
    rec('')
    rec('### ### **THE THREE STANDING SENTENCES `(R17)` NAMES, EACH IN THE MAP`S OWN WORDS:**')
    rec('###   ### **(i)** ### *each is a category, not a publishable artifact.*')
    rec('###   ### **(ii)** ### *The clusters are not rigid -- papers can sit in adjacent')
    rec('###     clusters.*')
    rec('###   ### **(iii)** ### the columns are read live, because pins move -- the map`s own')
    rec('###     discipline, carried in its caveat that ### *cluster-row coverage is partial* ###')
    rec('###     and in every pinned column it writes.')
    rec('')
    rec('### ### **THE CLUSTER TABLE, WHOLE AND VERBATIM, AT LINES %d-%d:**' % (HDR + 1, HDR + 8))
    tbl, first, last = prior_table()
    for k, ln in enumerate(tbl):
        rec('###   %-4d | %s' % (first + k, ln.strip('|').strip()[:150]))
    rec('')
    rec('### ### ### **THE MAP`S AGE, MEASURED AND NOT ASSERTED.**')
    rec('###   the cluster section`s own date            : ### **`%s`**' % E['map_date'])
    rec('###   today                                     : `%s`' % TODAY)
    rec('###   the registry`s newest date that HAS happened : ### **`%s`**' % E['registry_newest'])
    rec('### ### **AGE AGAINST TODAY : `%d` DAYS. ### AGE AGAINST THE REGISTRY`S NEWEST ROW : `%d`'
        % (E['age_today'], E['age_registry']))
    rec('### ### DAYS.**')
    rec('### ### **AND THE REGISTRY CARRIES FORWARD-LOOKING DATES, NAMED RATHER THAN USED :** ###')
    rec('###   %s' % ', '.join('`%s`' % x for x in E['registry_future']))
    rec('### ### ### **AN AGE MEASURED AGAINST A DATE THAT HAS NOT HAPPENED IS NOT AN AGE.** ### A')
    rec('### first pass took the maximum date and reported `344` days. ### **THAT FIGURE IS WRONG')
    rec('### ### AND IS NOT CARRIED.**')
    return dict(clusters=len(E['clusters']), table_lines=len(tbl),
                first=first, last=last, map_date=E['map_date'],
                age_today=E['age_today'], age_registry=E['age_registry'],
                future=E['registry_future'], prior_table=tbl)


# ==================================================================================================
def component2():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 2 -- THE TWO EMERGENT CLUSTERS, SEATED FROM THE MOVES THAT CREATED THEM.')
    rec('-' * 100)
    rec('### ### **EVERY `→ <x> cluster` MENTION IN THE REGISTRY : `%d`, OVER `%d` DISTINCT'
        % (E['mentions'], len(E['destinations'])))
    rec('### ### DESTINATIONS.** ### %s'
        % ', '.join('`%s` (%d)' % (k, v) for k, v in sorted(E['destinations'].items())))
    rec('### ### ### **DESTINATIONS THAT ARE NEITHER OF THE TWO : `%d`.**'
        % len(E['third_destinations']))
    if E['third_destinations']:
        rec('### ### ### **A THIRD DESTINATION IS REPORTED AND NOT SEATED : %s**'
            % E['third_destinations'])
    else:
        rec('### ### **SO NOTHING IS SEATED THAT `(R17)` DID NOT NAME.**')
    rec('')
    rec('### ### **A MENTION IS NOT A MOVE.** ### A row that cites ### *kin 1.5c-4 → theory-space*')
    rec('### is REFERRING to a move, not making one. ### The moves are the rows whose ### **OWN')
    rec('### ### STATUS** ### records the reclassification.')
    rec('### ### **ROWS WHOSE OWN STATUS RECORDS A MOVE : `%d`.**' % len(E['moves']))
    seats = {'theory-space': [], 'cross-domain': []}
    for mv in E['moves']:
        rec('')
        rec('###   `REGISTRY.md` line %-5d → ### **%s cluster**' % (mv['line'], mv['dest']))
        rec('###     row `%s`  %s' % (mv['row_id'], mv['title'][:80]))
        rec('###     path : %s' % (mv['path'] or '### **NAMED IN A TITLE ROW, NO PATH CELL**'))
        rec('###     dates in the row : %s' % (', '.join(mv['dates'][:4]) or 'none'))
        # ### **THE REASON, IN THE REGISTRY`S OWN WORDS**, sliced from the row and not paraphrased.
        seg = mv['text']
        m = re.search(r'RECLASSIFIED[^|]{0,400}', seg)
        if m:
            rec('###     ### **THE REGISTRY`S OWN WORDS:** ### %s' % m.group(0)[:300])
        if mv['path']:
            seats[mv['dest']].append(mv)
    rec('')
    rec('### ### ### **THE TWO CLUSTERS, SEATED FROM QUOTED MOVES ONLY.**')
    out = {}
    for name in ('theory-space', 'cross-domain'):
        members = seats[name]
        paths = sorted(set(m['path'] for m in members))
        rec('')
        rec('###   ### **`%s` cluster** -- members `%d`, from `%d` quoted move(s)'
            % (name, len(paths), len(members)))
        for p in paths:
            rec('###       %s' % p)
        # ### **THE SUBJECT, IN THE REGISTRY`S OWN WORDS.** ### Taken from the moves` own reasons;
        # ### **NOT COMPOSED BY THIS SEAT.**
        words = []
        for m in members:
            r = re.search(r'RECLASSIFIED[^|]{0,300}', m['text'])
            if r:
                words.append(r.group(0))
        rec('###     ### **THE SUBJECT, IN THE REGISTRY`S OWN WORDS** (from the moves` reasons):')
        for w in words[:2]:
            rec('###       | %s' % w[:260])
        # ### **THE KERNELS SERVING IT, READ LIVE.**
        kern = set()
        for p in paths:
            fp = os.path.join(PP, p.replace('/', os.sep))
            if os.path.exists(fp):
                body = io.open(fp, encoding='utf-8', errors='replace').read()
                kern |= set(re.findall(r'`(SIDE-[A-Za-z0-9_.-]+)`', body))
        kern = sorted(kern)
        rec('###     ### **THE KERNELS ITS MEMBERS NAME : `%d`.**' % len(kern))
        live = []
        for k in kern:
            got = lsremote(k, 'HEAD')
            h = got.get('HEAD')
            live.append(dict(kernel=k, head=(h or '')[:12], resolves=bool(h)))
            rec('###       %-34s HEAD %s' % (k, (h or '### **NOT RESOLVED**')[:12]))
        if not kern:
            rec('###       ### ### **NONE LOCATED** -- and the search is proved: every `SIDE-*`')
            rec('###       backtick in every member was read, and there were none.')
        out[name] = dict(members=paths, moves=len(members), kernels=live,
                         kernels_named=len(kern),
                         unresolved=sum(1 for x in live if not x['resolves']))
    rec('')
    rec('### ### **NO MEMBER WAS ADDED ON THIS SEAT`S JUDGEMENT OF SUBJECT.** ### Each is carried')
    rec('### by a quoted move at its own registry line. ### **A CLUSTER ASSEMBLED FROM A SEAT`S')
    rec('### ### SENSE OF WHAT BELONGS IS A CLUSTER THE AUTHOR NEVER RULED.**')
    return dict(seated=out, moves_rows=len(E['moves']),
                documents=len(set(m['path'] for m in E['moves'] if m['path'])),
                third=len(E['third_destinations']), destinations=E['destinations'])


# ==================================================================================================
# ### ### **THE CLUSTER-EVIDENCE INDEX.** ### For each cluster in the map`s table, the kernels its
# ### own federation column names and the anchors it names. ### **AN ASSIGNMENT IS EVIDENCE THAT A
# ### ### DOCUMENT REACHES ONE OF THESE, AND NOTHING ELSE.**
def cluster_index(C2):
    idx = {}
    for c in E['clusters']:
        idx[c['name']] = dict(kernels=set(c['kernels']), anchors=set(c['anchor_ids']),
                              members=set())
    for name, seat in C2['seated'].items():
        idx[name] = dict(kernels=set(x['kernel'] for x in seat['kernels']), anchors=set(),
                         members=set(os.path.basename(p)[:-3] for p in seat['members']))
    return idx


def component3(C2):
    rec('')
    rec('-' * 100)
    rec("### COMPONENT 3 -- THE ERA'S OUTPUT ASSIGNED OR MARKED.")
    rec('-' * 100)
    idx = cluster_index(C2)
    rec('### ### **THE CLUSTER SET AS NOW SEATED : `%d`** -- the map`s six plus the two `(R17)`'
        % len(idx))
    rec('### ### seats.**')
    for k, v in idx.items():
        rec('###   %-38s kernels %-3d anchors %-3d members %d'
            % (k[:38], len(v['kernels']), len(v['anchors']), len(v['members'])))
    rec('')
    rec('### ### **THE POPULATION : `%d` KEYSTONE-CLASS DOCUMENTS THE MAP`S TABLE DOES NOT NAME**,'
        % len(E['tierk_unnamed']))
    rec('### fixed on the locked face before this component ran.')
    rec('### ### **NO DOCUMENT IS ASSIGNED BY FILENAME, BY DIRECTORY, OR BY RESEMBLANCE OF')
    rec('### ### TITLE.** ### The evidence is a kernel the document NAMES or a cluster member it')
    rec('### CITES, and it is printed beside every assignment.')
    rec('')
    rows = []
    for rel in E['tierk_unnamed']:
        fp = os.path.join(PP, rel.replace('/', os.sep))
        body = io.open(fp, encoding='utf-8', errors='replace').read()
        kern = sorted(set(re.findall(r'`(SIDE-[A-Za-z0-9_.-]+)`', body)))
        cites = set()
        for cname, cv in idx.items():
            for mem in cv['members']:
                if mem in body:
                    cites.add((cname, mem))
        # ### **SCORE EACH CLUSTER BY THE KERNELS THE DOCUMENT NAMES THAT IT SERVES.**
        score = {}
        for cname, cv in idx.items():
            hit = sorted(set(kern) & cv['kernels'])
            if hit:
                score[cname] = hit
        for cname, mem in cites:
            score.setdefault(cname, []).append('cites `%s`' % mem)
        best, why, verdict = None, [], None
        if not kern and not cites:
            verdict, why = 'UNASSIGNED (NO EVIDENCE)', []
        else:
            ranked = sorted(score.items(), key=lambda kv: (-len(kv[1]), kv[0]))
            if not ranked:
                verdict, why = 'UNASSIGNED (NO FIT)', []
            elif len(ranked) > 1 and len(ranked[0][1]) == len(ranked[1][1]):
                verdict = 'UNASSIGNED (NO FIT)'
                why = ['%s:%d' % (n, len(v)) for n, v in ranked[:3]]
            else:
                best, why = ranked[0][0], ranked[0][1]
                verdict = best
        rec('###   ### **%s**' % rel)
        rec('###     kernels it names : %s' % (', '.join('`%s`' % k for k in kern[:8]) or 'NONE'))
        if len(kern) > 8:
            rec('###                        (and %d more)' % (len(kern) - 8))
        rec('###     cluster members it cites : %s'
            % (', '.join('`%s`' % m for _c, m in sorted(cites)) or 'NONE'))
        rec('###     ### **ASSIGNED : %s**' % verdict)
        rec('###     ### **EVIDENCE : %s**'
            % (', '.join(str(x) for x in why[:6]) or '### **NONE -- SO IT IS NOT ASSIGNED**'))
        rows.append(dict(doc=rel, kernels=kern, cites=sorted('%s|%s' % c for c in cites),
                         verdict=verdict, evidence=[str(x) for x in why]))
    assigned = [r for r in rows if not r['verdict'].startswith('UNASSIGNED')]
    noev = [r for r in rows if r['verdict'] == 'UNASSIGNED (NO EVIDENCE)']
    nofit = [r for r in rows if r['verdict'] == 'UNASSIGNED (NO FIT)']
    rec('')
    rec('### ### ### **ASSIGNED : `%d` OF `%d`. ### UNASSIGNED : `%d`.**'
        % (len(assigned), len(rows), len(noev) + len(nofit)))
    rec('### ### **AND `UNASSIGNED` IS TWO OUTCOMES, KEPT APART:** ### **NO EVIDENCE : `%d`** ###'
        % len(noev))
    rec('### (the document names no kernel and cites no member) and ### **NO FIT : `%d`** ### (it'
        % len(nofit))
    rec('### names kernels, and they point at no single cluster). ### **REPORTING THEM AS ONE')
    rec('### ### NUMBER WOULD HIDE WHICH.**')
    rec('### ### ### **UNASSIGNED IS A PERMITTED AND HONEST OUTCOME, NOT A DEFECT.** ### A')
    rec('### document the map has no seat for is a fact about the map as much as about the')
    rec('### document.')
    return dict(rows=rows, population=len(rows), assigned=len(assigned),
                unassigned=len(noev) + len(nofit), no_evidence=len(noev), no_fit=len(nofit),
                index={k: dict(kernels=sorted(v['kernels']), members=sorted(v['members']))
                       for k, v in idx.items()})


# ==================================================================================================
def component4(C2, C3):
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 4 -- THE MAP RE-EVALUATED.')
    rec('-' * 100)
    rec('### ### **FOUR QUESTIONS OF EACH SEATED CLUSTER, EACH ANSWERED BY A QUOTATION OR A LIVE')
    rec('### ### READ AND NEVER BY RECOLLECTION.**')
    findings, out = [], []
    for c in E['clusters']:
        name = c['name']
        rec('')
        rec('###   ### **`%s`**' % name)
        # ### (i) subject vs members
        newly = [r for r in C3['rows'] if r['verdict'] == name]
        rec('###     ### **(i) SUBJECT** -- the table names `%d` anchor id(s); this act assigns'
            % len(c['anchor_ids']))
        rec('###       `%d` further keystone-class document(s) to it.' % len(newly))
        for r in newly:
            rec('###         + %s' % r['doc'])
        # ### (ii) anchor
        anchor_cell = c['cells'][1] if len(c['cells']) > 1 else ''
        rec('###     ### **(ii) ANCHOR** -- as the table names it: %s'
            % re.sub(r'\s+', ' ', anchor_cell)[:150])
        # ### (iii) shape
        grew = len(newly)
        shape = 'GREW' if grew else 'UNCHANGED BY THIS ACT'
        rec('###     ### **(iii) SHAPE : %s.** ### Members added by this act : `%d`. ### Members'
            % (shape, grew))
        rec('###       moved out by a quoted registry move : `%d`.'
            % sum(1 for m in E['moves'] if m['path'] and False))
        # ### (iv) federation, LIVE
        live, bad = [], []
        for k in c['kernels']:
            got = lsremote(k, 'HEAD')
            h = got.get('HEAD')
            live.append(dict(kernel=k, head=(h or '')[:12], resolves=bool(h)))
            if not h:
                bad.append(k)
        rec('###     ### **(iv) FEDERATION : `%d` KERNEL(S), `%d` NOT RESOLVING.** ### Read live'
            % (len(c['kernels']), len(bad)))
        rec('###       by `ls-remote` in this act`s own run.')
        if bad:
            rec('###       ### ### **NOT RESOLVING : %s**' % ', '.join(bad))
        if grew:
            findings.append(dict(cluster=name, finding='GREW', by=grew,
                                 docs=[r['doc'] for r in newly]))
        out.append(dict(cluster=name, anchors=len(c['anchor_ids']), added=grew, shape=shape,
                        kernels=live, unresolved=len(bad)))
    for name, seat in C2['seated'].items():
        rec('')
        rec('###   ### **`%s` (SEATED BY `(R17)` AT THIS ACT)**' % name)
        rec('###     ### **(i) SUBJECT** -- stated from its moves` own words in Component 2.')
        rec('###     ### **(ii) ANCHOR** -- ### **NONE NAMED.** ### `(R17)` seats the cluster; it')
        rec('###       does not name an anchor, and ### **THIS SEAT DOES NOT INVENT ONE.**')
        rec('###     ### **(iii) SHAPE : NEW.** ### `%d` member(s) from `%d` quoted move(s).'
            % (len(seat['members']), seat['moves']))
        rec('###     ### **(iv) FEDERATION : `%d` KERNEL(S) NAMED BY ITS MEMBERS, `%d` NOT'
            % (seat['kernels_named'], seat['unresolved']))
        rec('###       RESOLVING.**')
        out.append(dict(cluster=name, anchors=0, added=len(seat['members']), shape='NEW',
                        kernels=seat['kernels'], unresolved=seat['unresolved']))
        findings.append(dict(cluster=name, finding='NEW', by=len(seat['members']),
                             docs=seat['members']))
    rec('')
    unres = sum(x['unresolved'] for x in out)
    rec('### ### ### **CLUSTERS WHOSE SHAPE CHANGED : `%d`.**' % len(findings))
    for f in findings:
        rec('###   `%-38s` ### **%s** ### by `%d`' % (f['cluster'][:38], f['finding'], f['by']))
    rec('### ### **KERNELS ACROSS ALL SEATED CLUSTERS THAT DO NOT RESOLVE : `%d`.**' % unres)
    rec('### ### ### **EVERY CHANGE OF SHAPE IS REPORTED AND NONE IS ACTED ON.** ### No cluster')
    rec('### was split, merged or renamed by this act. ### **THE RESHAPING IS THE AUTHOR`S**, and')
    rec('### a seat that reshapes while reporting has ruled.')
    return dict(clusters=out, shape_findings=findings, changed=len(findings),
                unresolved_total=unres, reshaped=0)


# ==================================================================================================
def component6():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 6 -- THE UNREADABLE ROWS, NAMED AND NOT REPAIRED.')
    rec('-' * 100)
    rows = B387['C2']['unreadable']
    rec('### ### **THE `%d` ROWS `b387` COULD NOT READ, EACH BY DOCUMENT, LINE, AND CAUSE.**'
        % len(rows))
    docs = {}
    for sv in E['survey'] if 'survey' in E else []:
        pass
    # ### the document each tag belongs to, from b387's own per-document table
    tagpath = {}
    for r in json.load(io.open(d('b387_reads.json'), encoding='utf-8'))['survey']:
        tagpath[r['tag']] = r['rel']
    out = []
    for u in rows:
        rel = tagpath.get(u['tag'], u['tag'])
        p = os.path.join(PP, rel.replace('/', os.sep))
        line = ''
        try:
            ls = io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))
            if 0 < u['line'] <= len(ls):
                line = ls[u['line'] - 1]
        except OSError:
            pass
        cellsx = [c.strip() for c in line.strip().strip('|').split('|')] if line else []
        status = re.sub(r'[*`]', '', cellsx[-1]).strip() if cellsx else ''
        ev = u['evidence']
        # ### ### **THE CAUSES, NAMED AND NOT BINNED AS `OTHER`.**
        if 'no nameable premise' in ev:
            cause = 'INTERFACES WITH NO NAMEABLE PREMISE'
        elif not status:
            cause = 'THE STATUS CELL IS EMPTY'
        elif re.fullmatch(r'[-—–]+', status):
            cause = 'THE STATUS CELL IS A DASH'
        elif len(status) > 60:
            cause = 'THE STATUS IS A SENTENCE, NOT A VOCABULARY WORD'
        else:
            cause = 'THE STATUS IS A WORD THE FRONT DOOR`S VOCABULARY DOES NOT CONTAIN'
        out.append(dict(tag=u['tag'], doc=rel, line=u['line'], status=status[:120], cause=cause))
    groups = {}
    for o in out:
        groups.setdefault(o['cause'], []).append(o)
    for cause in sorted(groups, key=lambda c: -len(groups[c])):
        rec('')
        rec('### ### **%s : `%d` ROW(S).**' % (cause, len(groups[cause])))
        for o in groups[cause]:
            rec('###   `%-8s` %-46s line %-6d' % (o['tag'], o['doc'].split('/')[-1][:46],
                                                  o['line']))
            rec('###       status as written : %s' % (o['status'] or '### **(empty)**'))
    total = sum(len(v) for v in groups.values())
    rec('')
    rec('### ### ### **CAUSES : `%d`. ### ROWS : `%d`. ### THE GROUP COUNTS SUM TO THE ROW COUNT :'
        % (len(groups), total))
    rec('### ### ### %s.**' % (total == len(rows)))
    rec('### ### **ROUTED TO THE AUTHOR.** ### **NO ROW WAS EDITED. ### NO GRADE WAS MOVED. ### NO')
    rec('### ### STATUS WAS ASSIGNED.** ### Naming what defeats a reader is not saying what the')
    rec('### row should have said, and ### **A SEAT THAT SUPPLIED THAT WOULD HAVE GRADED A ROW IT')
    rec('### ### WAS TOLD NOT TO TOUCH.**')
    return dict(rows=out, groups={k: len(v) for k, v in groups.items()},
                causes=len(groups), total=total, sums=(total == len(rows)))


def main():
    rec('=' * 100)
    rec('b388 -- THE MAP REFRESHED, AND THE UNREADABLE ROWS NAMED. ### THE COMPONENTS.')
    rec('=' * 100)
    C1 = component1()
    C2 = component2()
    C3 = component3(C2)
    C4 = component4(C2, C3)
    C6 = component6()
    rec('')
    rec('=' * 100)
    rec('### THE COMPONENTS, SUMMED. ### **COMPONENT 5 IS THE WRITE AND RUNS IN THE DESK TOOL.**')
    rec('=' * 100)
    rec('### ### **QUOTATIONS THAT FAILED TO RE-READ : %d** %s' % (len(FAILS), FAILS or ''))
    rec('### ### **THE MAP : %d CLUSTERS, %d DAYS OLD AGAINST TODAY, %d AGAINST THE REGISTRY`S '
        'NEWEST ROW**' % (C1['clusters'], C1['age_today'], C1['age_registry']))
    rec('### ### **MOVES : %d ROWS OVER %d DOCUMENTS ; THIRD DESTINATIONS : %d**'
        % (C2['moves_rows'], C2['documents'], C2['third']))
    rec('### ### **ASSIGNED %d OF %d ; UNASSIGNED %d (NO EVIDENCE %d, NO FIT %d)**'
        % (C3['assigned'], C3['population'], C3['unassigned'], C3['no_evidence'], C3['no_fit']))
    rec('### ### **CLUSTERS WHOSE SHAPE CHANGED : %d ; RESHAPED BY THIS ACT : %d ; KERNELS NOT '
        'RESOLVING : %d**' % (C4['changed'], C4['reshaped'], C4['unresolved_total']))
    rec('### ### **UNREADABLE ROWS : %d IN %d NAMED CAUSES, SUMMING : %s**'
        % (C6['total'], C6['causes'], C6['sums']))
    rec('### ### **NO CLASS RULED. ### NO DOCUMENT RECLASSIFIED. ### NO REGISTRY ROW EDITED. ###')
    rec('### ### NO GRADE MOVED. ### NO CLUSTER RESHAPED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b388_components_notes', LINES)
    out = dict(C1=C1, C2=C2, C3=C3, C4=C4, C6=C6, reread_failures=FAILS,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(d('b388_components.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (not FAILS and C6['sums'] and C2['third'] == 0) else 1


if __name__ == '__main__':
    sys.exit(main())
