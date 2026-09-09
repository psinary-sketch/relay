# -*- coding: utf-8 -*-
"""b393_extract.py -- THE EXTRACT AND THE THREE SURVEYS THE FACE IS WRITTEN FROM.

### ### **COMPONENT 1'S REAL WORK IS A MEASUREMENT NOBODY HAS TAKEN.** ### `b388` found the five
### clusters and `b391` reported them, but ### **BOTH MEASURED MEMBERSHIP ONLY.** ### The order names
### five kinds of change and one of them -- ### *anchor no longer the document a reader meets first*
### -- ### **HAS NEVER BEEN TESTED.** ### This file tests it.
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
FERRY = os.path.join(D, 'b393_ferry_2026-09-09.txt')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
ERRATA = os.path.join(PP, 'ERRATA.md')
README = os.path.join(PP, 'README.md')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
B388 = os.path.join(D, 'b388_components.json')
B387 = os.path.join(D, 'b387_closing.txt')

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


def lines_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))


# ==================================================================================================
#  SURVEY 1 -- THE FIVE CLUSTERS, AND THE ANCHOR DIMENSION NOBODY MEASURED.
# ==================================================================================================
def census_keystones():
    """### **THE SIXTEEN, WITH THEIR DATES AND PIN COUNTS, OUT OF THE CENSUS'S OWN TABLE.**"""
    out = {}
    for ln in lines_of(CENSUS):
        m = re.match(r'\|\s*#*\s*\**`([A-Z_0-9]+)`\**\s*\|\s*([^|]*?)\s*\|\s*#*\s*\**'
                     r'(\d{4}-\d\d-\d\d)\**\s*\|\s*#*\s*\**(\d+)\**\s*\|', ln)
        if m:
            out[m.group(1)] = dict(phase=m.group(2).strip(), date=m.group(3),
                                   pins=int(m.group(4)))
    return out


def refreshed_rows():
    """### **THE REFRESHED TABLE'S ROWS: THE CLUSTER, ITS ANCHOR CELL, AND ITS NOTE.**"""
    ls = lines_of(MAP)
    mark = '**REFRESHED CLUSTER TABLE — 2026-09-09 (b388), under RULING (R17).**'
    at = next((i for i, ln in enumerate(ls) if mark in ln), None)
    rows = []
    if at is None:
        return rows
    for i in range(at, min(at + 30, len(ls))):
        ln = ls[i]
        if ln.startswith('|') and ln.count('|') >= 5 and '---' not in ln:
            c = [x.strip() for x in ln.split('|')[1:-1]]
            if c and c[0].lower() != 'cluster':
                rows.append(dict(line=i + 1, name=re.sub(r'\*+|\(emergent\)', '', c[0]).strip(),
                                 anchor=c[1], note=c[-1], raw=ln))
    return rows


def survey1():
    bar('-')
    rec('  ### SURVEY 1 -- THE FIVE CLUSTERS, AND THE ANCHOR DIMENSION.')
    bar('-')
    ks = census_keystones()
    rec('  ### **THE CENSUS`S SIXTEEN, READ OUT OF ITS OWN TABLE : `%d`.**' % len(ks))
    shape = json.load(io.open(B388, encoding='utf-8'))['C4']['shape_findings']
    rows = {r['name']: r for r in refreshed_rows()}
    rec('  ### **THE REFRESHED TABLE`S ROWS : `%d`.**' % len(rows))
    rec()
    rec('  ### ### **`b388` AND `b391` BOTH MEASURED MEMBERSHIP. ### THE ORDER NAMES FIVE KINDS')
    rec('  ### ### OF CHANGE AND ONE OF THEM -- *ANCHOR NO LONGER THE DOCUMENT A READER MEETS')
    rec('  ### ### FIRST* -- HAS NEVER BEEN TESTED.** ### It is tested here, by the census`s own')
    rec('  ### two figures: ### **DATE AND PIN COUNT.**')
    rec('  ### **THE TEST:** ### a cluster changed by anchor if a member it GAINED is a census')
    rec('  ### keystone that is ### **NEWER** ### than the anchor and carries ### **MORE PINS**,')
    rec('  ### because a reader meeting the cluster first meets the document the corpus has most')
    rec('  ### recently and most heavily pinned. ### **A CHANGE OF MEMBERSHIP IS NOT A CHANGE OF')
    rec('  ### ### ANCHOR**, and the two are counted apart.')
    rec()
    out = []
    for s in shape:
        name = s['cluster']
        row = rows.get(name) or rows.get(name.replace(' / ', ' / '))
        anchor_cell = row['anchor'] if row else ''
        # ### the anchor cell's keystone names, and the gained members' keystone names.
        anames = [k for k in ks if k in anchor_cell]
        gained = [os.path.basename(d)[:-3] for d in s['docs']]
        gks = [g for g in gained if g in ks]
        rec('    ### **%s** ### -- `%s` by `%d`' % (name, s['finding'], s['by']))
        rec('        map row line %s' % (row['line'] if row else '?'))
        rec('        anchor cell keystones : %s' % (anames or '### **NONE**'))
        rec('        gained members        : %s' % gained)
        rec('        of which census keystones : %s' % (gks or 'none'))
        # ### **TWO DIFFERENT THINGS WERE BEING CONFLATED.** ### A first form called a cluster
        # ### `NO ANCHOR AT ALL` whenever the anchor cell named no CENSUS KEYSTONE -- so
        # ### `Methodology`, whose cell names three anchors by registry id, read as anchorless.
        # ### ### **"THE ANCHOR IS NOT A KEYSTONE" IS NOT "THERE IS NO ANCHOR"**, and the two
        # ### now carry separate verdicts.
        named = bool(re.search(r'`1\.5[a-z]?-|`p2-', anchor_cell))
        verdict, why = 'MEMBERSHIP ONLY', 'no gained member outranks an anchor'
        if not named:
            verdict = 'NO ANCHOR NAMED'
            why = ('the cell holds member filenames, not an anchor; `(R17)` named none and '
                   '`b388` did not invent one. ### **YOU CANNOT MEET AN ANCHOR THAT WAS NEVER '
                   'NAMED**, so the anchor question is VACUOUS here rather than answered')
        elif not anames:
            verdict = 'ANCHOR NOT A KEYSTONE'
            why = ('the cell names anchors by registry id -- %s -- but ### **NONE OF THEM IS '
                   'AMONG THE CENSUS`S SIXTEEN KEYSTONES**, so the census`s two figures cannot '
                   'rank them against the members. ### The anchor question is ### **UNDECIDABLE '
                   'FROM THE CENSUS** ### here, and a gained member that IS a keystone -- %s -- '
                   'makes that worth the author`s attention'
                   % (anchor_cell[:70], (gks or ['none'])[0]))
        else:
            best_a = max((ks[a] for a in anames), key=lambda x: (x['date'], x['pins']))
            for g in gks:
                if (ks[g]['date'], ks[g]['pins']) > (best_a['date'], best_a['pins']) and \
                        ks[g]['pins'] > best_a['pins']:
                    verdict = 'ANCHOR OVERTAKEN'
                    why = ('`%s` (%s, %d pins) is newer than the best anchor `%s` (%s, %d pins) '
                           'AND carries more pins' % (g, ks[g]['date'], ks[g]['pins'],
                                                      max(anames, key=lambda a: ks[a]['pins']),
                                                      best_a['date'], best_a['pins']))
        rec('        ### ### **VERDICT : %s**' % verdict)
        for k in range(0, min(len(why), 300), 150):
            rec('        %s' % why[k:k + 150])
        out.append(dict(cluster=name, finding=s['finding'], by=s['by'], gained=gained,
                        gained_keystones=gks, anchors=anames, verdict=verdict, why=why,
                        map_line=(row['line'] if row else None)))
        rec()
    from collections import Counter
    c = Counter(o['verdict'] for o in out)
    rec('  ### ### **BY VERDICT : %s**' % dict(c))
    rec('  ### ### **CHANGED BY ANCHOR : `%d` OF `%d`.**'
        % (c.get('ANCHOR OVERTAKEN', 0), len(out)))
    rec('  ### ### **NO ANCHOR NAMED : `%d`. ### ANCHOR NOT A CENSUS KEYSTONE : `%d`.**'
        % (c.get('NO ANCHOR NAMED', 0), c.get('ANCHOR NOT A KEYSTONE', 0)))
    rec('  ### ### ### **THOSE ARE THREE DIFFERENT ANSWERS TO ONE QUESTION AND THEY ARE NOT')
    rec('  ### ### ### ADDED.**')
    rec('  ### ### **`(L1)` EXPECTS AT LEAST TWO. ### THE COUNT IS `%d`.**'
        % c.get('ANCHOR OVERTAKEN', 0))
    return dict(clusters=out, by_verdict=dict(c),
                anchor_changed=c.get('ANCHOR OVERTAKEN', 0),
                no_anchor=c.get('NO ANCHOR NAMED', 0),
                anchor_not_keystone=c.get('ANCHOR NOT A KEYSTONE', 0),
                keystones=len(ks))


# ==================================================================================================
#  SURVEY 2 -- THE TWO RECORDS.
# ==================================================================================================
def survey2():
    bar('-')
    rec('  ### SURVEY 2 -- THE TWO RECORDS FAILING BOTH LIMBS.')
    bar('-')
    out = {}
    ei, eln = AF.find(ERRATA, 'The deposited monograph (Zenodo record 21432399')
    rec('  ### **`21432399`** -- `ERRATA.md` line %d:' % ei)
    rec('      > %s' % flat(eln, 330))
    ri, rln = AF.find(REGISTRY, '| d1-1 | A Place to Stand (monograph) |')
    rec('  ### the repository`s own row -- `REGISTRY.md` line %d:' % ri)
    rec('      > %s' % flat(rln, 210))
    mv = re.search(r'manuscript v([0-9.]+)', eln)
    rv = re.search(r'\|\s*(v[0-9.]+)\s*\|', rln)
    out['21432399'] = dict(what='the monograph, A Place to Stand',
                           deposited_at=('v' + mv.group(1)) if mv else '?',
                           repo_now=rv.group(1) if rv else '?',
                           errata_line=ei, registry_line=ri)
    rec('  ### ### **DEPOSITED AT MANUSCRIPT `%s`; THE REPOSITORY NOW CARRIES `%s`.**'
        % (out['21432399']['deposited_at'], out['21432399']['repo_now']))
    rec()
    bi, bln = AF.find(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md'),
                      'The Silence of Foundations. PLACE TO STAND programme, Day-1 deposit')
    rec('  ### **`19675356`** -- `INVARIANCE_BARRIERS.md` line %d, its only naming:' % bi)
    rec('      > %s' % flat(bln, 260))
    di, dln = AF.find(REGISTRY, '| d1-7 | Silence of Foundations |')
    rec('  ### the repository`s own row -- `REGISTRY.md` line %d:' % di)
    rec('      > %s' % flat(dln, 210))
    dv = re.search(r'\|\s*(v[0-9.]+)\s*\|', dln)
    out['19675356'] = dict(what='The Silence of Foundations (Day-1)',
                           deposited_at='### **NOT RECORDED ANYWHERE IN THE CORPUS**',
                           repo_now=dv.group(1) if dv else '?',
                           cite_line=bi, registry_line=di)
    rec('  ### ### **THE VERSION IT WAS DEPOSITED AT IS NOT RECORDED ANYWHERE IN THE CORPUS.** ###')
    rec('  ### ### The repository now carries `%s`.**' % out['19675356']['repo_now'])
    rec('  ### ### ### **AND THAT IS WHY IT FAILS BOTH LIMBS AT ONCE:** ### with no recorded')
    rec('  ### ### ### version, ### **NOTHING CAN SAY WHETHER IT IS CURRENT**, and with no note,')
    rec('  ### ### ### nothing says it is historical.')
    return out


# ==================================================================================================
#  SURVEY 3 -- TIER KC, AND WHAT THE RECORD DOES NOT HOLD.
# ==================================================================================================
def survey3():
    bar('-')
    rec('  ### SURVEY 3 -- `Tier KC`, UNAPPLIED.')
    bar('-')
    ti, tln = AF.find(TAX, '**Tier KC — the finished keystone.**')
    oi, oln = AF.find(TAX, '*Obligation.* **Every load-bearing claim is stated clearly in the '
                           'body**')
    rec('  ### **THE CLASS** -- `THE_DOCUMENT_CLASS_TAXONOMY.md` line %d:' % ti)
    rec('      > %s' % flat(tln, 260))
    rec('  ### **ITS OBLIGATION** -- line %d:' % oi)
    rec('      > %s' % flat(oln, 400))
    rec()
    # ---- what the record HOLDS ---------------------------------------------------------------
    b387 = io.open(B387, encoding='utf-8', errors='replace').read()
    rows = re.search(r'`(\d+)` ROWS COUNTED', b387)
    nm = re.search(r'`(\d+)` OF `(\d+)` ROWS', b387)
    tbl = re.search(r'THE UNION NAMES (\d+)', io.open(
        os.path.join(D, 'b387_checks_postpush.txt'), encoding='utf-8', errors='replace').read())
    rec('  ### ### **WHAT THE RECORD ALREADY HOLDS, FROM `b387`:**')
    rec('  ###   correspondence rows counted by what backs them : ### **`%s`**'
        % (rows.group(1) if rows else '?'))
    rec('  ###   of those, NOT machine-verified and labelled    : ### **`%s`**'
        % (nm.group(1) if nm else '?'))
    rec('  ###   the union names `%s` keystones; `9` carry a table, `5` carry none.'
        % (tbl.group(1) if tbl else '?'))
    rec()
    # ---- what the record DOES NOT hold --------------------------------------------------------
    rec('  ### ### **AND WHAT THE OBLIGATION TESTS THAT THE RECORD DOES NOT HOLD.**')
    rec('  ### The obligation has ### **THREE LIMBS**, and `b387` measured ### **ONE OF THEM.**')
    amc = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
    ls = lines_of(amc)
    prov = next((i for i, x in enumerate(ls, 1) if x.strip() == '## Provenance'), None)
    t1 = next((i for i, x in enumerate(ls, 1) if x.strip() == '## Correspondence'), None)
    t2 = next((i for i, x in enumerate(ls, 1)
               if 'CORRESPONDENCE AT THE STANDARD' in x), None)
    rec('  ###   (i) ### **PLACEMENT** ### -- *a correspondence table placed after the front')
    rec('  ###   matter, where a reader meets it.* ### **THE RECORD HOLDS NO TABLE POSITION FOR')
    rec('  ###   ### ANY DOCUMENT.** ### `b387` counted rows; it did not ask where they sit.')
    rec('  ###   ### **AND THE ONE DOCUMENT `b390` READ WHOLE WOULD FAIL IT:**')
    rec('  ###   `ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md` -- `## Correspondence` at line %s,'
        % t1)
    rec('  ###   `## Provenance` at line %s, the standard`s table at line %s ### **-- BOTH TABLES'
        % (prov, t2))
    rec('  ###   ### SIT AT THE END, AND THE STANDARD`S IS BELOW THE PROVENANCE.**')
    rec('  ###   (ii) ### **COVERAGE** ### -- *every load-bearing claim carried by a row.* ###')
    rec('  ###   **THE RECORD HOLDS ROW COUNTS AND NOT CLAIM COUNTS**, so the ratio a reader')
    rec('  ###   would need -- claims carried over claims made -- ### **CANNOT BE COMPUTED FROM')
    rec('  ###   ### WHAT IS BANKED.**')
    rec('  ###   (iii) ### **FURNITURE** ### -- *glossary, bibliography, and other tables as the')
    rec('  ###   document needs them.* ### **THE RECORD HOLDS NO FURNITURE CENSUS.**')
    rec()
    # ---- what CAN be measured cheaply, as a floor ---------------------------------------------
    rec('  ### ### **WHAT A CHEAP SWEEP COULD ESTABLISH, AS A FLOOR AND NOT A VERDICT:**')
    have = []
    for name in ('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md',):
        pass
    ks = census_keystones()
    n_tab = n_gloss = n_bib = 0
    found = []
    for k in ks:
        hits = []
        for dp, dn, fn in os.walk(PP):
            rel = os.path.relpath(dp, PP).replace(os.sep, '/')
            if rel.split('/')[0] in ('.git', 'archive', 'outputs'):
                continue
            for f in fn:
                if f[:-3] == k and f.endswith('.md'):
                    hits.append(os.path.join(dp, f))
        if not hits:
            continue
        txt = io.open(hits[0], encoding='utf-8', errors='replace').read()
        tab = '## Correspondence' in txt or 'CORRESPONDENCE AT THE STANDARD' in txt
        gl = bool(re.search(r'(?i)^#+ .*glossar', txt, re.M))
        bb = bool(re.search(r'(?i)^#+ .*(references|bibliograph)', txt, re.M))
        n_tab += tab
        n_gloss += gl
        n_bib += bb
        found.append(dict(keystone=k, table=tab, glossary=gl, bibliography=bb))
    rec('  ###   census keystones found on disk        : ### **`%d` of `%d`**'
        % (len(found), len(ks)))
    rec('  ###   carrying a correspondence table       : ### **`%d`**' % n_tab)
    rec('  ###   carrying a glossary heading           : ### **`%d`**' % n_gloss)
    rec('  ###   carrying a references/bibliography    : ### **`%d`**' % n_bib)
    rec('  ### ### **THAT IS A FLOOR ON THE FURNITURE LIMB AND SAYS NOTHING ABOUT THE OTHER TWO.**')
    return dict(rows=int(rows.group(1)) if rows else None,
                not_machine=int(nm.group(1)) if nm else None,
                union_names=int(tbl.group(1)) if tbl else None,
                amc_corr=t1, amc_prov=prov, amc_standard=t2,
                found=len(found), with_table=n_tab, with_glossary=n_gloss,
                with_bib=n_bib, detail=found)


# ==================================================================================================
READS = [
    ('the order -- leg 1, the act', FERRY,
     'LEG 1 (b393) — THE FIVE CLUSTERS, SURFACED; AND TWO PRICINGS.'),
    ('the order -- the first leg`s suite is dated at its own close', FERRY,
     "each locked and closed as its own act; the first leg's suite"),
    ('the order -- component 1, the five clusters', FERRY,
     'COMPONENT 1 — THE FIVE CLUSTERS, ordered at b390 and at b391'),
    ('the order -- component 1, printed in the closing message', FERRY,
     'message and not only in its bank: each cluster NAMED, and what'),
    ('the order -- component 1, the kinds of change', FERRY,
     'changed in it — subject drifted from members, anchor no longer'),
    ('the order -- component 1, a list a reader can act on', FERRY,
     "of the closing message can act on."),
    ('the order -- component 2, the two records', FERRY,
     'COMPONENT 2 — THE TWO RECORDS FAILING BOTH LIMBS: named, with'),
    ('the order -- component 2, the two remediations priced separately', FERRY,
     'a historical note added to the record, or a new version'),
    ('the order -- component 3, Tier KC priced', FERRY,
     'COMPONENT 3 — TIER KC, UNAPPLIED, PRICED: the class exists and'),
    ('the order -- component 3, what the record does not hold', FERRY,
     'application would need that the record does not hold. Priced,'),
    ('the order -- (L1)', FERRY,
     'two of the five clusters changed by anchor rather than by'),
    ('the class -- Tier KC itself', TAX, '**Tier KC — the finished keystone.**'),
    ('the class -- its obligation', TAX,
     '*Obligation.* **Every load-bearing claim is stated clearly in the body**'),
    ('the record -- the monograph record at v5.8', ERRATA,
     'The deposited monograph (Zenodo record 21432399'),
    ('the record -- the Day-1 Silence deposit', REGISTRY,
     '| d1-7 | Silence of Foundations |'),
]


def do_reads():
    bar('=')
    rec('  ### THE READS.')
    bar('=')
    out, without = [], 0
    for label, path, hint in READS:
        try:
            at, line = AF.find(path, hint)
            out.append(dict(label=label, file=os.path.basename(path), line=at,
                            differs=(line.strip() != hint.strip())))
            rec('    %-64s line %-5d differs %s' % (label[:64], at, line.strip() != hint.strip()))
        except Exception as e:
            without += 1
            out.append(dict(label=label, file=os.path.basename(path), line=None,
                            error=str(e)[:110]))
            rec('    %-64s ### **NO ANCHOR** -- %s' % (label[:64], str(e)[:70]))
    rec()
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), without))
    return out, without


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
    rec('b393 -- THE EXTRACT, AND THE THREE SURVEYS THE FACE IS WRITTEN FROM.')
    bar('=')
    R = refs()
    for k, v in R.items():
        rec('    %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    rec()
    s1 = survey1()
    rec()
    s2 = survey2()
    rec()
    s3 = survey3()
    rec()
    reads, without = do_reads()
    rec()
    bar('=')
    rec('  1 : clusters %d ; by verdict %s ; changed by anchor %d'
        % (len(s1['clusters']), s1['by_verdict'], s1['anchor_changed']))
    rec('  2 : records %d ; %s' % (len(s2), {k: v['repo_now'] for k, v in s2.items()}))
    rec('  3 : rows %s ; not machine-verified %s ; keystones on disk %s ; with a table %s'
        % (s3['rows'], s3['not_machine'], s3['found'], s3['with_table']))
    rec('  reads %d without_anchor %d' % (len(reads), without))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    p = run_clock.write(D, 'b393_extract_notes', L)
    json.dump(dict(s1=s1, s2=s2, s3=s3, reads=len(reads), without_anchor=without,
                   anchors_differing=sum(1 for r in reads if r.get('differs')), refs=R,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b393_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
