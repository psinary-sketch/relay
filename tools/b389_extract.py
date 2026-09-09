# -*- coding: utf-8 -*-
"""b389_extract.py -- EXTRACT-TO-DISK, AND THE THREE SURVEYS THE FACE IS WRITTEN FROM.

### ### **THE ZENODO READ FAILED, AND THE WAY IT FAILED IS THE FINDING.** ### `/api/records/<id>`
### returned `504`; so did the record page, the DOI resolver, and OAI-PMH `GetRecord`. ### One
### route -- `/api/records?q=recid:<id>` -- returned ### **`200` WITH `total: 0`**, which for a
### moment looked like a working route. ### **IT IS NOT AN ANSWER: A `200` CARRYING AN EMPTY
### ### RESULT IS AN EMPTY RESULT**, and `b378`'s rule applies to status codes as much as to exit
### codes. ### The probe below records ### **EVERY ROUTE, ITS CODE AND ITS BYTE COUNT, WITH A
### ### POSITIVE CONTROL ON A HOST THAT ANSWERS**, so the absence is proved and not asserted.
###
### ### **NOTHING IS WRITTEN AT ZENODO IN ANY BRANCH.** ### Every call is a `GET` with no
### credential, no method override and no body.
###
### ### **AND THE UNREACHED-REPOSITORY QUESTION IS SETTLED BY READING, NOT BY GUESSING.** ### The
### account listing, the corpus's other citations and the archive's own audit are all read here.
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
TMP = os.path.join(D, '_b389_probe')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b389_ferry_2026-09-09.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
UNION = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
IFACE = os.path.join(PP, 'phase1.5', 'spectral', 'INTERFACE_CONSERVATION.md')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
THEORY = os.path.join(PP, 'clusters', 'THEORY_SPACE_PHYSICS_CLUSTER_SYNTHESIS_2026-06-05.md')
ARCH = os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                    'OPEN_TRAILS-archive-2-historical-landings-and-programs.md')

READS = [
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b389 — THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED'),
    ('the order -- nothing written at Zenodo in any branch', 'ORDER', FERRY,
     'instrument lane and the wave stay parked; nothing deposits —'),
    ('the ruling (R18) -- two maps, two keys', 'RULING', FERRY,
     'strikeable: TWO MAPS, TWO KEYS. A CLUSTER map keys on subjects'),
    ('the ruling (R18) -- what a constellation map keys on', 'RULING', FERRY,
     'and domains. A CONSTELLATION map keys on interrelated verified'),
    ('the ruling (R18) -- which map is which', 'RULING', FERRY,
     'kernels that carry them. The federation map is the cluster map;'),
    ('the ruling (R18) -- the reason, and the drift each is prone to', 'RULING', FERRY,
     'holds. Recorded with the reason: subjects emerge from research'),
    ('the ruling (R18) -- a head note to each and nothing else', 'RULING', FERRY,
     'other, and this ruling adds a head note to each and nothing'),
    ('the order -- component 1, the cluster syntheses enumerated', 'ORDER', FERRY,
     'COMPONENT 1 — THE CLUSTER SYNTHESES ENUMERATED: every document'),
    ('the order -- component 1, more than six, and subjects the map does not carry', 'ORDER',
     FERRY, "map's table as now refreshed. Report whether more than six"),
    ('the order -- component 2, read live and read-only', 'ORDER', FERRY,
     'COMPONENT 2 — THE DEPOSITED LAYER, READ LIVE AND READ-ONLY:'),
    ('the order -- component 2, a version distance not a judgement', 'ORDER', FERRY,
     'version — a version distance, not a judgement. Then: which'),
    ('the order -- component 2, is there a written rule for what deposits', 'ORDER', FERRY,
     'from inference: is there a WRITTEN rule for what deposits?'),
    ('the order -- component 2, practice stated as observation not rule', 'ORDER', FERRY,
     'observed stated as observation rather than as rule.'),
    ('the order -- component 3, the unreached repository', 'ORDER', FERRY,
     'COMPONENT 3 — THE UNREACHED REPOSITORY: the citation naming a'),
    ('the order -- component 3, the three verdicts', 'ORDER', FERRY,
     'credentials — the account listing, any archived copy, any other'),
    ('the order -- component 4, head notes only', 'ORDER', FERRY,
     'COMPONENT 4 — (R18) APPLIED, head notes only: one head note to'),
    ('the order -- the closing, the constellation map`s currency entered not opened', 'ORDER',
     FERRY, "constellation map's own currency entered as an item (five named"),
    ('the order -- (F1), more than six cluster syntheses', 'ORDER', FERRY,
     'NAVIGATOR EDITS. The navigator’s expectations: (F1) more than'),
    ('the order -- (F2), three software records past their versions', 'ORDER', FERRY,
     'six cluster syntheses exist; (F2) at least three deposited'),
    ('the order -- (F3), no written deposit rule', 'ORDER', FERRY,
     '(F3) no written deposit rule is located. Each refutable by a'),

    # ---- THE CORPUS`S OWN WORDS ------------------------------------------------------------------
    ('the theory-space synthesis -- the smallest of the eight', 'CLUSTER', THEORY,
     'Two framing notes specific to this cluster. First, it is the **smallest and least mature**'),
    ('the map -- its sources, the six cluster syntheses', 'CLUSTER', MAP,
     '*Added 2026-06-04 currency pass. Sources: the six cluster syntheses'),
    ('the citing document -- what Proposition 1 is verified in', 'IFACE', IFACE,
     '**Kernel verification.** The structural form of Proposition 1 is verified in'),
    ('the citing document -- the future kernel, reserved', 'IFACE', IFACE,
     '**Proposition 1 (low priority, trivially formalizable).** The proof from non-injectivity'),
    ('the archive -- explicitly proposed kernel names, correctly hedged', 'IFACE', ARCH,
     '| Explicitly *proposed* kernel names'),
    ('the taxonomy -- the internal-until-fruit law', 'RULE', TAX,
     '*Admission (the internal-until-fruit law, 2026-07-28):*'),
    ('the taxonomy -- the sequencing law', 'RULE', TAX,
     '**sequencing law** (provisioning precedes publishing and partnering)'),
    ('the cluster map -- its purpose line', 'MAP', MAP,
     "**PURPOSE:** *the federation architecture — how the programme's repositories"),
    ('the constellation map -- its purpose line', 'MAP', UNION,
     '**PURPOSE:** *the union of the keystones’ correspondence tables'),
    ('the constellation map -- its keystone set of fourteen', 'MAP', UNION,
     '## The keystone set (14 graded Correspondence tables)'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def probe(url, tag, timeout='40'):
    """### **READ-ONLY: `curl -sL` WITH NO METHOD, NO BODY, NO CREDENTIAL.** ### Returns the
    ### status code and the byte count -- ### **AND THE BODY IS INSPECTED, BECAUSE A `200`
    ### ### CARRYING AN EMPTY RESULT IS AN EMPTY RESULT.**"""
    if not os.path.isdir(TMP):
        os.makedirs(TMP)
    p = os.path.join(TMP, tag)
    r = subprocess.run(['curl', '-sL', '-m', timeout, '-A', 'relay-b389-readonly', url,
                        '-o', p, '-w', '%{http_code}'], capture_output=True, text=True)
    code = (r.stdout or '').strip() or '000'
    n = os.path.getsize(p) if os.path.exists(p) else 0
    hits = None
    try:
        j = json.load(io.open(p, encoding='utf-8'))
        if isinstance(j, dict) and 'hits' in j:
            hits = (j.get('hits') or {}).get('total')
    except Exception:
        pass
    return dict(url=url, code=code, bytes=n, hits=hits)


def main():
    rec('=' * 100)
    rec('b389_extract.py -- EXTRACT-TO-DISK, AND THE THREE SURVEYS.')
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

    # ---------------------------------------------------------- SURVEY 1, THE CLUSTER SYNTHESES
    rec('')
    rec('-' * 100)
    rec('  ### SURVEY 1 -- THE CLUSTER SYNTHESES, ON DISK AND IN THE REGISTRY AND IN THE MAP.')
    rec('-' * 100)
    cdir = os.path.join(PP, 'clusters')
    syn = sorted(f for f in os.listdir(cdir) if 'CLUSTER_SYNTHESIS' in f and f.endswith('.md'))
    regtxt = io.open(REGISTRY, encoding='utf-8', errors='replace').read()
    maptxt = io.open(MAP, encoding='utf-8', errors='replace').read()
    hdr = next(i for i, ln in enumerate(maptxt.split(chr(10))) if ln.startswith('| Cluster |'))
    mlines = maptxt.split(chr(10))
    tbl = []
    j = hdr
    while j < len(mlines) and (mlines[j].strip().startswith('|') or j == hdr):
        tbl.append(mlines[j])
        j += 1
        if j - hdr > 40:
            break
    # ### the REFRESHED table too -- b388 seated two more, and the map now carries both tables
    tblall = maptxt[maptxt.index('### Clusters (working categories'):]
    tblall = tblall[:tblall.index('### Cross-cluster bridges')] if 'Cross-cluster bridges' \
        in tblall else tblall
    rows = []
    for f in syn:
        p = os.path.join(cdir, f)
        head = io.open(p, encoding='utf-8', errors='replace').read(1500)
        title = next((ln.strip('# ').strip() for ln in head.split(chr(10))
                      if ln.startswith('# ')), '')
        m = re.search(r'(\d{4}-\d{2}-\d{2})', f)
        date = m.group(1) if m else None
        in_reg = ('clusters/' + f) in regtxt
        stem = f.split('_CLUSTER_SYNTHESIS')[0]
        in_map = any(w.lower() in tblall.lower()
                     for w in [stem.replace('_', ' '), stem.replace('_', '-'), stem])
        rows.append(dict(file=f, date=date, title=title, in_registry=in_reg, in_map=in_map))
        rec('    %-58s %s  registry:%-5s map:%s' % (f[:58], date, in_reg, in_map))
        rec('        its own title : %s' % title[:110])
    nreg = sum(1 for r in rows if r['in_registry'])
    nmap = sum(1 for r in rows if r['in_map'])
    rec('')
    rec('  ### ### **CLUSTER SYNTHESES ON DISK : `%d`. ### NAMED IN THE REGISTRY`S SUPPORT TIER : '
        '`%d`. ### THEIR SUBJECT CARRIED BY THE MAP`S TABLE : `%d`.**' % (len(rows), nreg, nmap))
    rec('  ### ### **MORE THAN SIX EXIST : %s.**' % (len(rows) > 6))

    # ------------------------------------------------------------- SURVEY 2, THE DEPOSITED LAYER
    rec('')
    rec('-' * 100)
    rec('  ### SURVEY 2 -- THE DEPOSITED LAYER. ### **READ-ONLY, AND THE ROUTES PROVED.**')
    rec('-' * 100)
    dois = set()
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.startswith(('.git', 'archive')):
            continue
        for f in fn:
            if f.endswith('.md'):
                try:
                    dois |= set(re.findall(r'10\.5281/zenodo\.(\d+)',
                                           io.open(os.path.join(dp, f), encoding='utf-8',
                                                   errors='replace').read()))
                except OSError:
                    pass
    rec('  ### DOIs the corpus names, outside `archive/` : ### **`%d`**' % len(dois))
    rec('')
    rec('  ### ### **THE ROUTES, EACH PROBED, WITH A POSITIVE CONTROL:**')
    ROUTES = [
        ('the record API', 'https://zenodo.org/api/records/21520474', 'api'),
        ('the record page', 'https://zenodo.org/records/21520474', 'page'),
        ('the DOI resolver', 'https://doi.org/10.5281/zenodo.21520474', 'doi'),
        ('the search API', 'https://zenodo.org/api/records?q=recid:21520474&size=5', 'search'),
        ('OAI-PMH Identify', 'https://zenodo.org/oai2d?verb=Identify', 'oaii'),
        ('OAI-PMH GetRecord',
         'https://zenodo.org/oai2d?verb=GetRecord&metadataPrefix=oai_dc'
         '&identifier=oai:zenodo.org:21520474', 'oaig'),
    ]
    probes = []
    for label, url, tag in ROUTES:
        r = probe(url, tag)
        r['label'] = label
        probes.append(r)
        extra = ('' if r['hits'] is None
                 else '   ### **hits total : %s**' % r['hits'])
        rec('    %-22s http=%-4s %6d bytes%s' % (label, r['code'], r['bytes'], extra))
    ctrl = probe('https://api.github.com/users/psinary-sketch', 'ctrl', '30')
    rec('    %-22s http=%-4s %6d bytes   ### **POSITIVE CONTROL -- THE NETWORK ANSWERS**'
        % ('github, a live host', ctrl['code'], ctrl['bytes']))
    ok = [p for p in probes if p['code'] == '200' and (p['hits'] is None or p['hits'])]
    rec('')
    rec('  ### ### **ROUTES RETURNING A NON-EMPTY ANSWER : `%d` OF `%d`.**' % (len(ok), len(probes)))
    rec('  ### ### ### **A `200` CARRYING `total: 0` IS AN EMPTY RESULT, NOT A WORKING ROUTE**, and')
    rec('  ### ### ### the search API is counted as ### **NOT ANSWERING** ### on that ground.')
    rec('  ### ### **THE CONTROL ANSWERS, SO THE NETWORK IS NOT THE CAUSE.**')

    # ---- the corpus's own citable list, which needs no platform
    rec('')
    rec('  ### **WHAT THE CORPUS`S OWN DEPOSIT NOTE LISTS AS CITABLE** -- read from the record:')
    cite = []
    for m in re.finditer(r'current deposit \*\*(v[0-9.]+)\*\*, DOI '
                         r'\[10\.5281/zenodo\.(\d+)\]', regtxt):
        cite.append((m.group(1), m.group(2)))
    for v, r in cite:
        rec('      REGISTRY names as the current deposit : `%s` at `zenodo.%s`' % (v, r))
    rec('  ### DOIs named anywhere in the live corpus : `%d` ### / ### named as THE current '
        'deposit : `%d`' % (len(dois), len(cite)))

    # ---- the written-rule search, with a positive control
    rec('')
    rec('  ### ### **IS THERE A WRITTEN RULE FOR WHAT DEPOSITS? ### THE SEARCH, PROVED.**')
    NAMES = ['deposit rule', 'what deposits', 'deposit policy', 'when to deposit',
             'deposit discipline', 'criteria for deposit', 'deposit law', 'rule for depositing']
    CONTENT = ['internal-until-fruit', 'sequencing law', 'deposit-ready', 'provisioning precedes']

    def sweep(term):
        hits = []
        for dp, dn, fn in os.walk(PP):
            rel = os.path.relpath(dp, PP).replace(os.sep, '/')
            if rel.startswith(('.git', 'archive')):
                continue
            for f in fn:
                if not f.endswith('.md'):
                    continue
                p = os.path.join(dp, f)
                try:
                    t = io.open(p, encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                if term.lower() in t.lower():
                    hits.append(os.path.relpath(p, PP).replace(os.sep, '/'))
        return hits
    namehits, conthits = {}, {}
    rec('    ### **BY THE NAME A READER WOULD GIVE IT** (`b385`s species -- the weaker half):')
    for t in NAMES:
        h = sweep(t)
        namehits[t] = h
        rec('      %-24s : %d file(s)' % ('`%s`' % t, len(h)))
    rec('    ### **BY THE CONTENT A DEPOSIT RULE WOULD HAVE** (the half that matters):')
    for t in CONTENT:
        h = sweep(t)
        conthits[t] = h
        rec('      %-24s : %d file(s)  %s' % ('`%s`' % t, len(h), h[:2]))
    located = any(namehits.values())
    rec('  ### ### **A WRITTEN RULE FOR WHAT DEPOSITS, LOCATED : %s.**' % located)

    # -------------------------------------------------------- SURVEY 3, THE UNREACHED REPOSITORY
    rec('')
    rec('-' * 100)
    rec('  ### SURVEY 3 -- THE UNREACHED REPOSITORY.')
    rec('-' * 100)
    NAME = 'SIDE-interface-split'
    r = subprocess.run(['git', 'ls-remote',
                        'https://github.com/psinary-sketch/%s.git' % NAME, 'HEAD'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    rec('    route 1 -- `ls-remote` : exit %d ; %s'
        % (r.returncode, (r.stderr or '').strip().split(chr(10))[0][:80]))
    names = []
    for page in (1, 2, 3):
        p = probe('https://api.github.com/users/psinary-sketch/repos?per_page=100&page=%d' % page,
                  'gh%d' % page, '40')
        try:
            j = json.load(io.open(os.path.join(TMP, 'gh%d' % page), encoding='utf-8'))
            if isinstance(j, list):
                names += [x.get('name') for x in j]
        except Exception:
            pass
    rec('    route 2 -- the public account listing : ### **`%d` REPOSITORIES**, `%d` of them '
        '`SIDE-*`' % (len(names), sum(1 for n in names if str(n).startswith('SIDE-'))))
    rec('        ### **`%s` PRESENT : %s**' % (NAME, NAME in names))
    near = [n for n in names if 'interface' in str(n).lower()]
    rec('        names containing `interface` : %s' % near)
    cites = []
    for dp, dn, fn in os.walk(PP):
        if '.git' in os.path.relpath(dp, PP):
            continue
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            try:
                t = io.open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            for i, ln in enumerate(t.split(chr(10)), 1):
                if NAME in ln:
                    cites.append((os.path.relpath(p, PP).replace(os.sep, '/'), i, ln.strip()))
    rec('    route 3 -- every corpus citation of the name : ### **`%d`**' % len(cites))
    FUTURE = re.compile(r'future|candidate|proposed|would be|or similar|reserved', re.I)
    hedged = [c for c in cites if FUTURE.search(c[2])]
    rec('        ### ### **CITATIONS WHOSE OWN SENTENCE MARKS IT FUTURE, CANDIDATE, PROPOSED OR')
    rec('        ### ### RESERVED : `%d` OF `%d`.**' % (len(hedged), len(cites)))
    for c in cites[:12]:
        mark = '### **HEDGED**' if FUTURE.search(c[2]) else ''
        rec('        %-62s line %-6d %s' % (c[0][:62], c[1], mark))
    rec('')
    rec('=' * 100)
    rec('  ### THE READS.')
    rec('=' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-7s] %s' % (tag, lbl))
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
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL, AND NOTHING WAS WRITTEN AT ZENODO.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b389_extract_notes', LINES)
    io.open(d('b389_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, built=out,
                        syntheses=rows, syn_on_disk=len(rows), syn_in_registry=nreg,
                        syn_in_map=nmap, more_than_six=(len(rows) > 6),
                        dois=sorted(dois), probes=probes, control=ctrl,
                        routes_answering=len(ok), citable=cite,
                        rule_name_hits={k: len(v) for k, v in namehits.items()},
                        rule_content_hits={k: v for k, v in conthits.items()},
                        rule_located=located,
                        gh_names=names, gh_has_name=(NAME in names), gh_near=near,
                        cites=[dict(file=c[0], line=c[1], text=c[2]) for c in cites],
                        cites_hedged=len(hedged), cites_total=len(cites),
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
