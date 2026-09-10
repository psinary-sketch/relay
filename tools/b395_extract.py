# -*- coding: utf-8 -*-
"""b395_extract.py -- THE EXTRACT AND THE SURVEYS FOR THE CEILING.

### ### **b394 SAID THE ELEVEN NEED `EITHER A CLONE OR A RULING`. ### THAT SENTENCE HAS AN
### ### UNTESTED PREMISE IN IT** -- that reading a terminal needs the repository's contents. ###
### `ls-remote` reads a repository's REFS without cloning it, so the question splits: ### **AN
### ### EXISTENCE QUESTION `ls-remote` ANSWERS, AND A CONTENT QUESTION IT CANNOT.**
###
### ### **THE TERMINAL MATCHER IS WIDENED AND EVERY YIELD IS PRINTED** (`b381`). ### `b394`'s
### shape was a BACKTICKED LOWERCASE name; a keystone naming its terminal any other way read as
### naming none, and `b370`'s own lore says a predicate that knows one shape finds one shape.
###
### ### **THE FEDERATION READ IS LIVE AND ITS AMBIGUITY IS NAMED:** ### an unauthenticated
### `ls-remote` says NOT FOUND for a repository that is absent AND for one that is private, ###
### **SO A NEGATIVE IS REPORTED AS `ABSENT-OR-PRIVATE` AND NEVER AS `ABSENT`.**
###
### ### **NOTHING IS EDITED BY THIS FILE. ### NOTHING IS WRITTEN AT ZENODO.**
"""
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
FERRY = os.path.join(D, 'b395_ferry_2026-09-09.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
ACCOUNT = 'https://github.com/psinary-sketch/%s.git'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


def text_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


SKIP = ('.git', 'archive', 'outputs')

# ### **THE ELEVEN, TAKEN FROM `b394`'S OWN RECORD AND NOT RETYPED.**
B394 = json.load(io.open(os.path.join(D, 'b394_reads.json'), encoding='utf-8'))


# ==================================================================================================
#  SURVEY 1 -- THE ELEVEN, READ AS A POPULATION.
# ==================================================================================================
# ### **THREE MATCHERS, AND EVERY YIELD IS PRINTED** -- `b381`'s rule. ### V1 is `b394`'s own
# ### shape and is carried here so the widening can be MEASURED rather than asserted.
V1 = re.compile(r'`(SIDE-[a-z0-9-]+)`')
V2 = re.compile(r'`?(SIDE-[A-Za-z0-9][A-Za-z0-9-]*)`?')
NOTAREPO = ('SIDE-kernel-session-notes',)

DISPOSITION = [
    ('HELD', re.compile(r'(?i)\bheld\b')),
    ('UNMERGED', re.compile(r'(?i)\bunmerged\b|not (?:yet )?merged|not on `?main`?')),
    ('RETIRED', re.compile(r'(?i)\bretired\b|\bsuperseded branch\b|\bdecommissioned\b')),
    ('BRANCH-RESIDENT', re.compile(r'(?i)branch-resident|on a branch\b|branch `')),
]


def repos_named(txt):
    """### Returns (v1, v2, kept) -- EVERY YIELD, and the residue is hand-read below."""
    v1 = sorted(set(V1.findall(txt)))
    v2 = sorted(set(m for m in V2.findall(txt) if m not in NOTAREPO))
    return v1, v2, sorted(set(v2))


def isrepo(name):
    """### **A DIRECTORY IS NOT A REPOSITORY.** ### The test is a `.git` inside it."""
    return os.path.isdir(os.path.join('D:' + os.sep, name, '.git'))


def localrefs(name):
    """### **THE CLAIM `READABLE WITHOUT A CLONE` IS DEMONSTRATED, NOT ASSERTED.** ### For a
    ### repository the drive holds, this reads its HEAD and counts the refs already present --
    ### including the ones a held or unmerged terminal would live on."""
    d = os.path.join('D:' + os.sep, name)
    h = subprocess.run(['git', '-C', d, 'rev-parse', '--short', 'HEAD'], capture_output=True,
                       text=True, encoding='utf-8', errors='replace')
    b = subprocess.run(['git', '-C', d, 'for-each-ref', '--format=%(refname)'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    refs = [x for x in (b.stdout or '').split(chr(10)) if x.strip()]
    heads = [x for x in refs if x.startswith('refs/heads/')]
    return dict(head=(h.stdout or '').strip(), refs=len(refs), heads=len(heads),
                nonmain=sorted(x.split('/', 2)[-1] for x in heads
                               if x.split('/', 2)[-1] not in ('main', 'master'))[:6],
                ok=h.returncode == 0)


def survey1(live):
    bar('-')
    rec('  ### SURVEY 1 -- THE ELEVEN, READ AS A POPULATION AND NOT AS A QUEUE.')
    bar('-')
    ai, aln = AF.find(os.path.join(D, 'b394_the_reconciliation_batched.txt'),
                      'THE POPULATION THIS METHOD CAN REACH IS ALREADY NEARLY EXHAUSTED')
    rec('  ### **THE ITEM THIS ACT ANSWERS, QUOTED FROM `b394`\'S BANK, line %d:**' % ai)
    rec('      > %s' % flat(aln, 190))
    rec('  ### ### **AND ITS PREMISE IS TESTED HERE, NOT INHERITED:** ### `b394` said the eleven')
    rec('  ### ### need `either a clone or a ruling about reading branches`. ### **`ls-remote`')
    rec('  ### ### READS REFS WITHOUT CLONING**, so the premise holds only for the part of the')
    rec('  ### ### question that is about CONTENT.')
    rec()
    rows = []
    widened = 0
    for r in B394['s1']['all']:
        if r['reach']:
            continue
        p = os.path.join(PP, r['path'].replace('/', os.sep))
        txt = text_of(p)
        v1, v2, kept = repos_named(txt)
        if len(v2) > len(v1):
            widened += 1
        disp = [n for n, pat in DISPOSITION if pat.search(txt)]
        on = [x for x in kept if isrepo(x)]
        residue = [x for x in kept if not isrepo(x)]
        live_yes = [x for x in kept if live.get(x, {}).get('verdict') == 'RESOLVES']
        # ### **THE DEMONSTRATION, PER NAMED REPOSITORY THE DRIVE HOLDS.**
        proof = {x: localrefs(x) for x in on}
        readable = [x for x in on if proof[x]['ok']]
        # ### **THE PARTITION. ### FOUR PLACES, AND EVERY KEYSTONE LANDS IN EXACTLY ONE.**
        if not kept:
            where, why = ('NAMES NO TERMINAL', 'its own text names no federation repository at '
                                               'all, so there is nothing to settle and no clone '
                                               'would help')
        elif readable:
            where, why = ('ON THE DRIVE', 'it names %d repository(ies) the drive holds AS GIT '
                                          'REPOSITORIES and every one of them resolves a HEAD '
                                          'here, so the read needs no clone' % len(readable))
        elif live_yes:
            where, why = ('BY ls-remote', 'the drive holds none of them, but the account resolves '
                                          '%d live -- and a REF question is answered by '
                                          '`ls-remote` without a clone' % len(live_yes))
        else:
            where, why = ('ABSENT-OR-PRIVATE', 'no repository it names is on the drive or resolves '
                                               'at the account unauthenticated, and that answer '
                                               'does not distinguish absent from private')
        rows.append(dict(k=r['k'], path=r['path'], v1=v1, v2=v2, on=on, residue=residue,
                         live=live_yes, disp=disp, where=where, why=why, readable=readable,
                         proof={x: dict(head=proof[x]['head'], refs=proof[x]['refs'],
                                        heads=proof[x]['heads'], nonmain=proof[x]['nonmain'])
                                for x in on},
                         b394_why=r['why'], pins=r['pins'], date=r['date']))
    rec('  ### **EVERY YIELD OF THE THREE MATCHERS, PER KEYSTONE. ### V1 IS `b394`\'S SHAPE.**')
    for x in rows:
        rec('    %-34s V1 %-2d V2 %-2d  drive %-2d  live %-2d  says %s'
            % (x['k'][:34], len(x['v1']), len(x['v2']), len(x['on']), len(x['live']),
               (', '.join(x['disp']) or '-- nothing')))
    rec('  ### ### **THE WIDENING CHANGED THE YIELD FOR `%d` OF THE ELEVEN.**' % widened)
    rec()
    rec('  ### **THE PARTITION -- FIVE PLACES, EACH KEYSTONE IN EXACTLY ONE:**')
    part = {}
    for x in rows:
        part.setdefault(x['where'], []).append(x['k'])
    for w in sorted(part, key=lambda z: -len(part[z])):
        rec('    %-20s %d   %s' % (w, len(part[w]), ', '.join(part[w])))
    rec('  ### ### **THE PARTS SUM TO `%d` AND THE POPULATION IS `%d`.**'
        % (sum(len(v) for v in part.values()), len(rows)))
    rec()
    for x in rows:
        rec('    ### **%s**  (%s pins, %s)' % (x['k'], x['pins'], x['date']))
        rec('        repositories named : %s' % (', '.join(x['on']) or '### **NONE**'))
        rec('        ### the residue, HAND-READ and NOT counted as terminals : %s'
            % (', '.join(x['residue']) or 'none'))
        rec('        its own text says : %s' % (', '.join(x['disp']) or '### **NOTHING -- the '
                                                'terminal is simply ABSENT from its own prose**'))
        for n in x['on']:
            p = x['proof'][n]
            rec('          %-30s HEAD `%s`  refs %-4d branches %-3d  other: %s'
                % (n, p['head'], p['refs'], p['heads'], ', '.join(p['nonmain']) or '--'))
        rec('        b394 said         : %s' % x['b394_why'])
        rec('        ### **%s** -- %s' % (x['where'], x['why']))
    # ### **THE CORRECTION THIS SURVEY OWES ITS OWN PREDECESSOR.**
    rec()
    moved = [x['k'] for x in rows if x['on'] and 'no kernel repository' in x['b394_why']]
    rec('  ### ### **`b394` REPORTED `no kernel repository it names is on the drive` FOR `%d` OF'
        % len(moved))
    rec('  ### ### THESE, AND THE DRIVE HOLDS ONE FOR EVERY ONE OF THEM.** ### The defect is in')
    rec('  ### ### the PREDICATE, not in the corpus: `b394` matched a BACKTICKED LOWERCASE name')
    rec('  ### ### and these documents name their terminals in other shapes. ### **A PREDICATE')
    rec('  ### ### THAT KNOWS ONE SHAPE FINDS ONE SHAPE** -- the corpus\'s own lore, minted at')
    rec('  ### ### `b370`, and this act is the incident that proves it applies to `b394`.')
    rec('  ### **THE FIGURE `b394` LOCKED IS NOT EDITED AND IS RESTATED HERE BESIDE THE')
    rec('  ### CORRECTED ONE:** ### b394 said ELEVEN UNREACHABLE; this act measures ###')
    rec('  ### **`%d` OF THE ELEVEN READABLE WITHOUT A CLONE.**'
        % sum(1 for x in rows if x['where'] in ('ON THE DRIVE', 'BY ls-remote')))
    return rows


# ==================================================================================================
#  SURVEY 2 -- THE FEDERATION'S REACH, READ LIVE.
# ==================================================================================================
def _once(name):
    try:
        r = subprocess.run(['git', 'ls-remote', '--heads', ACCOUNT % name],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', timeout=60,
                           env=dict(os.environ, GIT_TERMINAL_PROMPT='0',
                                    GCM_INTERACTIVE='never'))
        heads = [ln.split('\t')[-1] for ln in (r.stdout or '').split(chr(10)) if ln.strip()]
        return dict(code=r.returncode, heads=heads, bytes=len(r.stdout or ''),
                    verdict=('RESOLVES' if r.returncode == 0 and heads else 'ABSENT-OR-PRIVATE'),
                    err=flat(r.stderr or '', 90))
    except subprocess.TimeoutExpired:
        return dict(code=None, heads=[], bytes=0, verdict='HALTED', err='timeout at 60s')


def lsremote(name):
    """### ### **ONE READ IS NOT A MEASUREMENT.** ### An earlier form of this survey read each
    ### name once and returned `ABSENT-OR-PRIVATE` for `SIDE-archimedean` -- a repository the
    ### drive holds and the account carries -- on a transient `code 128`. ### **A NEGATIVE IS
    ### ### RE-READ BEFORE IT IS BANKED, AND A NAME THAT CHANGED ITS ANSWER IS REPORTED AS
    ### ### HAVING CHANGED IT** rather than quietly taking the second reading."""
    a = _once(name)
    if a['verdict'] == 'RESOLVES':
        return dict(a, attempts=1, flapped=False)
    b = _once(name)
    return dict(b, attempts=2, flapped=(b['verdict'] != a['verdict']), first=a['verdict'])


def corpus_names():
    """### Every `SIDE-*` token the corpus carries, found by content across the tree."""
    seen = set()
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in fn:
            if not f.endswith('.md'):
                continue
            for m in V2.findall(text_of(os.path.join(dp, f))):
                if m not in NOTAREPO:
                    seen.add(m)
    return sorted(seen)


def survey2():
    bar('-')
    rec('  ### SURVEY 2 -- THE FEDERATION\'S REACH. ### **READ LIVE, WITH ITS AMBIGUITY NAMED.**')
    bar('-')
    names = corpus_names()
    rec('  ### **NAMES THE CORPUS CARRIES : `%d`**, found by content across the tree and not'
        % len(names))
    rec('  ### from any roster this seat typed.')
    # ### **THE TWO CONTROLS, RUN BEFORE ANY FINDING IS READ OFF THIS SURVEY.**
    pos = lsremote('PLACE-papers')
    neg = lsremote('SIDE-a-repository-that-does-not-exist-b395')
    rec('  ### **POSITIVE CONTROL** `PLACE-papers` : %s, %d head(s)'
        % (pos['verdict'], len(pos['heads'])))
    rec('  ### **NEGATIVE CONTROL** a name nobody minted : %s' % neg['verdict'])
    ok = pos['verdict'] == 'RESOLVES' and neg['verdict'] == 'ABSENT-OR-PRIVATE'
    rec('  ### ### **THE ROUTE DISCRIMINATES : %s.** ### Without both controls a survey of'
        % ok)
    rec('  ### ### zeroes and a broken route look the same.')
    live = {}
    for n in names:
        live[n] = lsremote(n)
    drive = {n: os.path.isdir(os.path.join('D:' + os.sep, n, '.git')) for n in names}
    res = [n for n in names if live[n]['verdict'] == 'RESOLVES']
    halt = [n for n in names if live[n]['verdict'] == 'HALTED']
    flap = [n for n in names if live[n].get('flapped')]
    retried = [n for n in names if live[n].get('attempts', 1) > 1]
    rec('  ### **NEGATIVES RE-READ : `%d` ; ### NAMES THAT CHANGED THEIR ANSWER ON THE SECOND'
        % len(retried))
    rec('  ### READ : `%d`  %s**' % (len(flap), ', '.join(flap) or '--'))
    if flap:
        rec('  ### ### **A ONE-READ SURVEY WOULD HAVE BANKED %d FALSE NEGATIVE(S).**' % len(flap))
    held = [n for n in names if drive[n]]
    both = [n for n in names if drive[n] and live[n]['verdict'] == 'RESOLVES']
    rec()
    rec('  ### ### **THE DRIVE HOLDS `%d` OF THE `%d` NAMES AS GIT REPOSITORIES.**'
        % (len(held), len(names)))
    rec('  ### ### **THE ACCOUNT RESOLVES `%d` OF THE `%d`, UNAUTHENTICATED.**'
        % (len(res), len(names)))
    rec('  ### ### **BOTH : `%d`. ### ON THE DRIVE AND NOT RESOLVING : `%d`. ### RESOLVING AND'
        % (len(both), len(held) - len(both)))
    rec('  ### ### NOT ON THE DRIVE : `%d`. ### HALTED : `%d`.**'
        % (len(res) - len(both), len(halt)))
    rec('  ### **AND THE NEGATIVE IS `ABSENT-OR-PRIVATE`, NEVER `ABSENT`** -- an unauthenticated')
    rec('  ### read returns the same answer for a repository that is not there and one this')
    rec('  ### account cannot see without credentials.')
    rec()
    rec('  ### **THE CEILING IS A FACT ABOUT THE WORKING MACHINE:** ### the corpus names `%d`'
        % len(names))
    rec('  ### federation repositories and this drive holds `%d` of them. ### **THE `%d` THE'
        % (len(held), len(names) - len(held)))
    rec('  ### ### DRIVE DOES NOT HOLD ARE NOT A DEFECT IN THE CORPUS**, and no corpus document')
    rec('  ### is graded down for them.')
    return dict(names=names, live={k: dict(verdict=v['verdict'], heads=len(v['heads']),
                                           code=v['code']) for k, v in live.items()},
                drive=drive, resolves=res, on_drive=held, both=both, halted=halt,
                controls=dict(pos=pos['verdict'], neg=neg['verdict'], ok=ok))


# ==================================================================================================
#  SURVEY 3 -- THE TWO ANCHORLESS CLUSTERS, FROM THEIR MEMBERS' OWN TEXT.
# ==================================================================================================
CLUSTERS = {
    'theory-space': ['CONSTANCE', 'STRUCTURAL_FRACTION'],
    'cross-domain': ['FORMATION_DISTANCE_DARK_VARIABLE_v0_1', 'INTERFACE_CONSERVATION'],
}
SUBJECT = re.compile(r'(?i)^#\s|^##\s*(abstract|statement|the claim|what this)')


def firstprose(txt, n=3):
    """### The document's own opening claim: its title line and the first non-empty prose."""
    out = []
    for ln in txt.split(chr(10)):
        s = ln.strip()
        if not s or s.startswith(('|', '---', '<!--', '>')):
            continue
        out.append(s)
        if len(out) >= n:
            break
    return out


def survey3():
    bar('-')
    rec('  ### SURVEY 3 -- THE TWO ANCHORLESS CLUSTERS. ### **QUOTED, AND DECIDED BY NOBODY.**')
    bar('-')
    loc = {}
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in fn:
            if f.endswith('.md'):
                loc[f[:-3]] = (rel + '/' + f if rel != '.' else f)
    out = {}
    for cl, mem in CLUSTERS.items():
        rec('  ### **%s** -- %d member(s), seated at `b388` under (R17), NO ANCHOR NAMED.'
            % (cl, len(mem)))
        ms = []
        for m in mem:
            p = loc.get(m)
            if not p:
                rec('      %-40s ### **NOT ON DISK**' % m)
                ms.append(dict(name=m, path=None, lines=[], draws=[]))
                continue
            txt = text_of(os.path.join(PP, p.replace('/', os.sep)))
            ln = firstprose(txt)
            # ### **TWO MATCHERS, BOTH YIELDS PRINTED.** ### The backticked shape returned ZERO
            # ### on all four members, which is the same one-shape defect this act reports of
            # ### `b394` -- so the bare-token shape is run beside it and both are shown.
            tick = sorted(set(re.findall(r'`([A-Z][A-Z_0-9]{4,})(?:\.md)?`', txt)))
            bare = sorted(set(re.findall(r'\b([A-Z][A-Z_0-9]{5,})(?:\.md)?\b', txt)))
            bare = [b for b in bare if b not in ('PLACE', 'SIDE') and not b.startswith('SIDE_')]
            # ### **AND THEN KEPT ONLY WHERE THE NAME IS A DOCUMENT THE CORPUS ACTUALLY HOLDS.**
            # ### The bare shape matches ordinary capitalised words, so the yield is intersected
            # ### with the tree's own basenames: ### **A WORD IN CAPITALS IS NOT A CITATION.**
            draws = sorted(x for x in set(tick) | set(bare) if x in loc)
            rec('      %-40s %s' % (m, p))
            for q in ln:
                rec('          > %s' % flat(q, 150))
            rec('          ### identifiers -- backticked %d ; bare %d ; ### **OF THOSE, NAMES A '
                'DOCUMENT THE CORPUS HOLDS : %d**' % (len(tick), len(bare), len(draws)))
            rec('          ### %s' % (', '.join(draws[:10]) or '### **NONE BY EITHER SHAPE**'))
            ms.append(dict(name=m, path=p, lines=[flat(q, 150) for q in ln], draws=draws,
                           tick=tick, bare=bare))
        # ### **THE READING IS OFFERED AS A READING AND IS NOT A RULING.**
        shared = set(ms[0]['draws']) & set(ms[1]['draws']) if len(ms) == 2 else set()
        out[cl] = dict(members=ms, shared=sorted(shared))
        rec('      ### **WHAT A FIRST SYNTHESIS WOULD DRAW ON** -- identifiers BOTH members')
        rec('      ### name : %d  %s' % (len(shared), ', '.join(sorted(shared)[:8]) or '--'))
        rec('      ### ### **THIS ACT DECIDES NOTHING ABOUT EITHER CLUSTER.** ### Whether each')
        rec('      ### ### reads as a SUBJECT or as a DESTINATION is routed to the author.')
        rec()
    return out


# ==================================================================================================
#  SURVEY 4 -- THE (R21) TARGET ROW, AND THE TWO DEPOSITED RECORDS.
# ==================================================================================================
def survey4():
    bar('-')
    rec('  ### SURVEY 4 -- THE (R21) TARGET, AND THE TWO RECORDS.')
    bar('-')
    lines = text_of(MAP).split(chr(10))
    # ### **THE ROW IS FOUND BY CONTENT AND ONLY THEN INDEXED** -- and the PRESERVED copy in the
    # ### superseded table (a `>` line) is excluded, because editing a quotation is falsification.
    hits = [(i + 1, ln) for i, ln in enumerate(lines)
            if ln.startswith('| **Simplicity / RH cascade**')]
    quoted = [(i + 1, ln) for i, ln in enumerate(lines)
              if ln.startswith('> | **Simplicity / RH cascade**')]
    rec('  ### **LIVE ROW(S) : %s ### PRESERVED-QUOTATION ROW(S) : %s**'
        % ([i for i, _ in hits], [i for i, _ in quoted]))
    rec('  ### ### **THE QUOTED ONE IS NOT A TARGET.** ### It is `b388`\'s preserved prior table')
    rec('  ### ### and (R4) preserves by quotation.')
    assert len(hits) == 1, 'the live row must be exactly one'
    ln_i, row = hits[0]
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    rec('  ### **THE LIVE ROW, line %d, %d cells:**' % (ln_i, len(cells)))
    for j, c in enumerate(cells):
        rec('      cell %d : %s' % (j, flat(c, 155)))
    hdr = [(i + 1, ln) for i, ln in enumerate(lines)
           if ln.startswith('| Cluster | Anchor keystone(s) in this repo')]
    rec('  ### **THE HEADER, line %s:** %s' % ([i for i, _ in hdr][-1], flat(hdr[-1][1], 150)))
    rec('  ### ### **COLUMN 1 IS THE IN-REPO ANCHOR LIST AND COLUMN 2 IS THE EXTERNAL SIBLING.**')
    rec('  ### ### `R_CURVE_CRITERION` SITS IN THE SIBLING COLUMN, NOT THE ANCHOR COLUMN -- so')
    rec('  ### ### **b393\'S `best anchor` AND THE MAP\'S ANCHOR CELL DO NOT DISAGREE**, and')
    rec('  ### ### this act reports that rather than choosing between two readings of one word.')
    # ### THE TWO RECORDS.
    rec()
    # ### **THE RECORDS ARE FOUND BY CONTENT ACROSS THE TREE, NOT ASSUMED INTO ONE LEDGER.**
    # ### An earlier form of this survey looked in `REGISTRY.md` alone and found NEITHER, which
    # ### would have read as `the corpus does not record them`. ### **ABSENCE FROM ONE FILE IS
    # ### ### NOT ABSENCE FROM THE CORPUS.**
    dep = []
    for doi in ('21432399', '19675356'):
        found = []
        for dp, dn, fn in os.walk(PP):
            rel = os.path.relpath(dp, PP).replace(os.sep, '/')
            if rel.split('/')[0] in SKIP:
                continue
            for f in sorted(fn):
                if not f.endswith('.md'):
                    continue
                r = (rel + '/' + f if rel != '.' else f)
                for i, ln in enumerate(text_of(os.path.join(dp, f)).split(chr(10)), 1):
                    if doi in ln:
                        found.append((r, i, flat(ln, 170)))
        rec('  ### **%s** -- `%d` line(s) in `%d` live document(s)'
            % (doi, len(found), len(set(x[0] for x in found))))
        for r, i, ln in found[:4]:
            rec('      %s:%d' % (r, i))
            rec('      > %s' % ln)
        dep.append(dict(doi=doi, hits=[(r, i) for r, i, _ in found],
                        docs=sorted(set(x[0] for x in found)),
                        quotes=[x[2] for x in found[:4]]))
    return dict(row_line=ln_i, row=row, cells=cells, quoted=[i for i, _ in quoted],
                header_line=hdr[-1][0], deposits=dep)


# ==================================================================================================
#  THE READS, AND THE ANCHOR FOR EVERY QUOTED LINE.
# ==================================================================================================
def unique_hint(path, want):
    """### **THE HINT IS GROWN FROM THE FILE'S OWN LINE UNTIL IT MATCHES EXACTLY ONE.**
    ### A bare repository name matches dozens of lines, and `anchor_from_file` refuses a hint
    ### that matches twice -- correctly, because an anchor matching twice anchors nothing. ###
    ### **SO THE HINT IS READ OUT OF THE FILE AND LENGTHENED UNTIL IT IS UNIQUE**, and if no
    ### length makes it unique the caller is told AMBIGUOUS rather than told nothing."""
    lines = text_of(path).split(chr(10))
    hit = next((ln for ln in lines if want in ln), None)
    if hit is None:
        return want
    j = hit.index(want)
    for n in (len(want), 40, 60, 90, 130, 180):
        frag = hit[j:j + n].strip()
        if frag and sum(1 for ln in lines if frag in ln) == 1:
            return frag
    return hit.strip() or want


def do_reads(s1, s4):
    bar('-')
    rec('  ### THE READS. ### **EVERY QUOTED LINE CARRIES AN ANCHOR FOUND BY THE TOOL.**')
    bar('-')
    reads, without = [], 0
    # ### **THE NEEDLE IS A STRING THE DOCUMENT ACTUALLY CARRIES.** ### An earlier form of this
    # ### used each keystone's own NAME, which most of them never write inside themselves, and
    # ### `10` of `15` reads came back NO ANCHOR. ### **THAT WAS THE NEEDLE'S DEFECT AND NOT THE
    # ### ### DOCUMENTS'** -- the evidence line for this act's finding is the line naming the
    # ### first repository the drive holds, so that is what is anchored.
    todo = []
    for x in s1:
        p = os.path.join(PP, x['path'].replace('/', os.sep))
        todo.append((p, x['on'][0] if x['on'] else 'HELD'))
    # ### ### **THE MAP NEEDLE IS THE LIVE ROW'S OWN BYTES AND NOT ITS OPENING CELLS.** ### A
    # ### needle of `| **Simplicity / RH cascade**` anchored at line 258 -- ### **`b388`'S
    # ### ### PRESERVED QUOTATION OF THE SUPERSEDED TABLE**, whose row begins with the same
    # ### cells -- and resolved to it SILENTLY, having found it first. ### **AN ANCHOR THAT
    # ### ### PREFERS A QUOTATION TO THE LIVE LINE IS AN ANCHOR POINTING AT THE WRONG ROW**,
    # ### and the act that edits by it would have edited a preserved quotation.
    todo += [(MAP, s4['row']), (FERRY, 'ADDITION ONE'),
             (FERRY, 'ADDITION TWO'), (FERRY, 'ADDITION THREE')]
    amb = 0
    for p, want in todo:
        needle = unique_hint(p, want)
        try:
            i, ln = AF.find(p, needle)
            verdict = 'ANCHORED'
        except Exception as e:
            # ### **AMBIGUOUS AND ABSENT ARE TWO ANSWERS AND ARE NOT ONE.** ### `b393` was
            # ### corrected for exactly this conflation and the correction is carried here.
            i, ln = 0, ''
            verdict = 'AMBIGUOUS' if 'more than one' in str(e).lower() or 'matches' in str(e) \
                else 'ABSENT'
            if verdict == 'AMBIGUOUS':
                amb += 1
            else:
                without += 1
        reads.append(dict(path=os.path.basename(p), needle=flat(needle, 60), line=i,
                          verdict=verdict, text=flat(ln, 110)))
        rec('    %-40s %-30s %-10s line %s'
            % (os.path.basename(p)[:40], flat(want, 30), verdict, i or '--'))
    rec('  ### **reads %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d**'
        % (len(reads), len(reads) - amb - without, amb, without))
    return reads, without


def refs():
    out = {}
    for name, repo in b303_pins.REPOS:
        b = subprocess.run(['git', '-C', repo, 'rev-parse', '--abbrev-ref', 'HEAD'],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        h = subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        out[name] = dict(branch=(b.stdout or '').strip(), head=(h.stdout or '').strip()[:12])
    return out


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b395 -- THE EXTRACT, AND THE SURVEYS THE FACE IS WRITTEN FROM.')
    bar('=')
    R = refs()
    for k, v in R.items():
        rec('    %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    rec()
    s2 = survey2()
    rec()
    s1 = survey1(s2['live'])
    rec()
    s3 = survey3()
    rec()
    s4 = survey4()
    rec()
    reads, without = do_reads(s1, s4)
    rec()
    bar('=')
    part = {}
    for x in s1:
        part.setdefault(x['where'], []).append(x['k'])
    rec('  1 : eleven %d ; partition %s' % (len(s1), {k: len(v) for k, v in part.items()}))
    rec('  2 : names %d ; drive %d ; account %d ; both %d ; halted %d ; controls %s'
        % (len(s2['names']), len(s2['on_drive']), len(s2['resolves']), len(s2['both']),
           len(s2['halted']), s2['controls']['ok']))
    rec('  3 : clusters %d ; %s' % (len(s3), {k: len(v['shared']) for k, v in s3.items()}))
    rec('  4 : live row line %d ; preserved rows %s' % (s4['row_line'], s4['quoted']))
    rec('  reads %d without_anchor %d' % (len(reads), without))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    p = run_clock.write(D, 'b395_extract_notes', L)
    json.dump(dict(s1=s1, s2=s2, s3=s3, s4=s4, reads=len(reads), without_anchor=without,
                   refs=R, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b395_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
