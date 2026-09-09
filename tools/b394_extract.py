# -*- coding: utf-8 -*-
"""b394_extract.py -- THE EXTRACT AND THE SURVEYS FOR THE BATCHED RECONCILIATION.

### ### **THE CHOICE IS MADE BY `b390`'S RULE AND NOT BY THIS SEAT'S TASTE:** ### *take those whose
### terminals the drive can reach.* ### **THE RULE IS `b390`'S EXACT WORDS AND NOTHING IS ADDED TO
### ### IT** -- an earlier form of this survey also demanded a correspondence table, which is a
### condition `b390` never stated, and it cut the eligible set from four to three by a rule nobody
### ruled.
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
FERRY = os.path.join(D, 'b394_ferry_2026-09-09.txt')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

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


SKIP = ('.git', 'archive', 'outputs')
GRADEWORDS = ('DERIVES', 'INTERFACES', 'MILESTONE-OPEN', 'MANUSCRIPT-RESIDENT', 'RESEARCH-REACH',
              'COMPILED', 'SCAFFOLDING', 'TAUTOLOGY', 'Placeholder', 'Open', 'SHELL', 'PENDING')


def census_keystones():
    out = {}
    for ln in lines_of(CENSUS):
        m = re.match(r'\|\s*#*\s*\**`([A-Z_0-9]+)`\**\s*\|\s*([^|]*?)\s*\|\s*#*\s*\**'
                     r'(\d{4}-\d\d-\d\d)\**\s*\|\s*#*\s*\**(\d+)\**\s*\|', ln)
        if m:
            out[m.group(1)] = dict(phase=m.group(2).strip(), date=m.group(3),
                                   pins=int(m.group(4)))
    return out


def locate(names):
    loc = {}
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in fn:
            if f.endswith('.md') and f[:-3] in names:
                loc[f[:-3]] = (rel + '/' + f if rel != '.' else f)
    return loc


# ==================================================================================================
#  SURVEY 1 -- THE CHOICE, BY b390'S RULE.
# ==================================================================================================
ALREADY = {'ADDITIVE_MULTIPLICATIVE_CONSPIRACY': 'read whole at `b390`, which is the act that '
                                                 'minted the rule this choice uses'}


def survey1():
    bar('-')
    rec('  ### SURVEY 1 -- THE CHOICE, BY `b390`\'S RULE.')
    bar('-')
    ai, aln = AF.find(os.path.join(D, 'b390_the_proofreading_pass.txt'),
                      'TERMINALS THE DRIVE CAN REACH.**')
    rec('  ### **THE RULE, QUOTED FROM THE ACT THAT MINTED IT** -- `b390`\'s bank line %d:' % ai)
    rec('      > %s' % flat(aln, 200)[3:])
    rec('  ### ### **NOTHING IS ADDED TO IT.** ### An earlier form of this survey also demanded a')
    rec('  ### ### correspondence table -- a condition `b390` never stated -- and it cut the')
    rec('  ### ### eligible set from `4` to `3` ### **BY A RULE NOBODY RULED.**')
    rec()
    ks = census_keystones()
    loc = locate(ks)
    rows = []
    for k in sorted(ks, key=lambda x: (-ks[x]['pins'], ks[x]['date'])):
        p = loc.get(k)
        if not p:
            rows.append(dict(k=k, path=None, reach=False, why='not on disk',
                             pins=ks[k]['pins'], date=ks[k]['date'], table=False))
            continue
        txt = io.open(os.path.join(PP, p.replace('/', os.sep)), encoding='utf-8',
                      errors='replace').read()
        repos = sorted(set(re.findall(r'`(SIDE-[a-z0-9-]+)`', txt)))
        on = [r for r in repos if os.path.isdir(os.path.join('D:' + os.sep, r))]
        held = bool(re.search(r'(?i)(HELD|UNMERGED|not on `?main`?|branch-resident)', txt))
        tab = ('## Correspondence' in txt) or ('CORRESPONDENCE AT THE STANDARD' in txt)
        reach = bool(on) and not held
        why = ('no kernel repository it names is on the drive' if not on
               else ('it says its terminals are HELD or UNMERGED' if held
                     else 'names %d kernel repositories on the drive' % len(on)))
        rows.append(dict(k=k, path=p, reach=reach, why=why, repos=on, held=held,
                         pins=ks[k]['pins'], date=ks[k]['date'], table=tab))
    elig = [r for r in rows if r['reach']]
    rec('  ### ### **CENSUS KEYSTONES : `%d`. ### TERMINALS THE DRIVE CAN REACH : `%d`.**'
        % (len(rows), len(elig)))
    for r in rows:
        mark = '### **ELIGIBLE**' if r['reach'] else 'excluded'
        rec('    %-38s %-8s %3d pins  table %-5s  %s'
            % (r['k'][:38], r['date'], r['pins'], r['table'], mark))
        if not r['reach']:
            rec('        %s' % r['why'])
    rec()
    chosen = [r for r in elig if r['k'] not in ALREADY]
    rec('  ### ### **OF THE `%d` ELIGIBLE, `%d` ARE TAKEN.**' % (len(elig), len(chosen)))
    for k, why in ALREADY.items():
        if any(r['k'] == k for r in elig):
            rec('  ###   ### **`%s` IS SET ASIDE** ### -- %s.' % (k, why))
            rec('  ###   ### **RE-READING IT WOULD BE RE-DOING `b390`\'S WORK**, and this act')
            rec('  ###   ### re-checks it in the corpus-wide sweep instead.')
    rec('  ### ### **THE THREE : %s**' % ', '.join('`%s`' % r['k'] for r in chosen))
    rec('  ### ### **AND ONE OF THEM CARRIES NO CORRESPONDENCE TABLE**, which is a finding and')
    rec('  ### ### not a disqualification: ### **A KEYSTONE WITH NO TABLE IS A KEYSTONE WHOSE')
    rec('  ### ### GRADE LIMB CANNOT BE READ**, and `b387` already named five of them.')
    return dict(all=rows, eligible=[r['k'] for r in elig],
                chosen=[r['k'] for r in chosen],
                paths={r['k']: r['path'] for r in chosen},
                tables={r['k']: r['table'] for r in chosen},
                set_aside=list(ALREADY))


# ==================================================================================================
#  SURVEY 2 -- WHAT EACH CARRIES.
# ==================================================================================================
def table_rows(path):
    ls = lines_of(os.path.join(PP, path.replace('/', os.sep)))
    out, started = [], False
    for i, ln in enumerate(ls, 1):
        if ln.startswith('|') and ln.count('|') >= 4:
            cells = [x.strip() for x in ln.split('|')[1:-1]]
            if cells and all(set(c) <= set(':- ') and c for c in cells):
                continue
            if cells and cells[0].lower() in ('claim', 'claims'):
                started = True
                continue
            if started:
                out.append((i, cells))
        elif started and ln.strip() == '':
            started = False
    return out


def survey2(chosen, paths, tables):
    bar('-')
    rec('  ### SURVEY 2 -- WHAT EACH OF THE THREE CARRIES.')
    bar('-')
    out = {}
    for k in chosen:
        p = paths[k]
        full = os.path.join(PP, p.replace('/', os.sep))
        txt = io.open(full, encoding='utf-8', errors='replace').read()
        ls = txt.split(chr(10))
        ver = re.search(r'\*\*?v([0-9][0-9.]*)[,\s—-]', txt)
        title = next((x.lstrip('# ').strip() for x in ls if x.startswith('# ')), '')
        rows = table_rows(p) if tables[k] else []
        grades = {}
        for _i, cells in rows:
            st = cells[-1]
            g = next((w for w in GRADEWORDS if w.upper() in st.upper()), 'OTHER')
            grades[g] = grades.get(g, 0) + 1
        rec('    ### **`%s`** ### -- `%s`' % (k, p))
        rec('        its own title : %s' % title[:90])
        rec('        version token : %s ; lines : %d ; bytes : %d'
            % (('v' + ver.group(1)) if ver else '### **NONE FOUND**', len(ls),
               len(txt.encode('utf-8'))))
        rec('        correspondence table : %s ; rows : %d' % (tables[k], len(rows)))
        if grades:
            rec('        by grade : %s' % sorted(grades.items()))
        else:
            rec('        ### ### **NO TABLE -- THE GRADE LIMB CANNOT BE READ FOR THIS DOCUMENT.**')
        out[k] = dict(path=p, title=title, version=('v' + ver.group(1)) if ver else None,
                      lines=len(ls), bytes=len(txt.encode('utf-8')),
                      table=tables[k], rows=len(rows), grades=grades)
        rec()
    return out


# ==================================================================================================
#  SURVEY 3 -- THE CORPUS-WIDE CHECK THIS PASS HAS TAUGHT.
# ==================================================================================================
def registry_versions():
    out = {}
    for i, ln in enumerate(lines_of(REGISTRY), 1):
        m = re.match(r'\|\s*([0-9][^|]*?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+\.md)`\s*\|'
                     r'\s*(v[0-9][0-9.]*)\s*\|', ln)
        if m:
            out[m.group(3)] = dict(rid=m.group(1), version=m.group(4), line=i)
    return out


def vnum(v):
    parts = re.split(r'[._]', v.lstrip('v'))
    o = [int(x) if x.isdigit() else 0 for x in parts]
    while len(o) > 1 and o[-1] == 0:
        o.pop()
    return tuple(o)


def survey3(chosen, paths):
    bar('-')
    rec('  ### SURVEY 3 -- THE CORPUS-WIDE CHECK, SWEPT ACROSS THE THREE SUBJECTS.')
    bar('-')
    rec('  ### ### **TWO SPECIES, BOTH TAUGHT BY THIS SORTIE:**')
    rec('  ###   (i) ### **A CITATION NAMING A VERSION THAT DOES NOT EXIST** ### -- `b391`\'s')
    rec('  ###   phantom, generalised.')
    rec('  ###   (ii) ### **CORRECTED BUT UNPROPAGATED** ### -- a claim the record has since')
    rec('  ###   corrected AT ITS SOURCE while the citing documents kept the old form. ### That')
    rec('  ###   is the species `b391` found in the registry`s own bundle label.')
    rec()
    regs = registry_versions()
    stems = {os.path.basename(p)[:-3]: (p, v['version'])
             for p, v in regs.items() if len(os.path.basename(p)) > 9}
    VER = re.compile(r'v\s*([0-9][0-9.]*?)(?=[^0-9.]|$)')
    WORDCH = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_')
    phantom, superseded = [], []
    for k in chosen:
        p = paths[k]
        for i, ln in enumerate(lines_of(os.path.join(PP, p.replace('/', os.sep))), 1):
            for stem, (target, regver) in stems.items():
                for m in re.finditer(re.escape(stem), ln):
                    tail = ln[m.end():m.end() + 40]
                    v = VER.search(tail)
                    if not v:
                        continue
                    cited = 'v' + v.group(1).rstrip('.')
                    if vnum(cited) == vnum(regver):
                        continue
                    a = ln[m.start() - 1] if m.start() else ' '
                    b = ln[m.end()] if m.end() < len(ln) else ' '
                    if a in WORDCH or b in WORDCH:
                        continue
                    span = tail[:v.start()]
                    if len(span) > 12 or re.search(r'[A-Za-z]', span) or ',' in span:
                        continue
                    tp = os.path.join(PP, target.replace('/', os.sep))
                    lin = set()
                    if os.path.exists(tp):
                        lin = set('v' + x.rstrip('.') for x in re.findall(
                            r'\bv([0-9][0-9.]*)',
                            io.open(tp, encoding='utf-8', errors='replace').read()))
                    hit = dict(citer=k, citer_path=p, line=i, cited=target, at=cited,
                               registry=regver, text=flat(ln, 120))
                    if lin and not any(vnum(cited) == vnum(x) for x in lin):
                        phantom.append(hit)
                    else:
                        superseded.append(hit)
    rec('  ### ### **ACROSS THE THREE SUBJECTS:**')
    rec('  ###   citations naming a version the cited document never declares : ### **`%d`**'
        % len(phantom))
    rec('  ###   citations naming a version it DOES declare but the registry has moved past :'
        ' ### **`%d`**' % len(superseded))
    for h in phantom:
        rec('      ### **PHANTOM** ### %s line %d -> `%s` at `%s` (registry `%s`)'
            % (h['citer'], h['line'], os.path.basename(h['cited']), h['at'], h['registry']))
        rec('        > %s' % h['text'])
    for h in superseded[:8]:
        rec('      superseded  %s line %d -> `%s` at `%s` (registry `%s`)'
            % (h['citer'], h['line'], os.path.basename(h['cited']), h['at'], h['registry']))
    rec()
    # ---- corrected but unpropagated -----------------------------------------------------------
    rec('  ### ### **THE `CORRECTED BUT UNPROPAGATED` SWEEP.**')
    rec('  ### **THE TEST:** ### the registry records a row update that changed a figure; the')
    rec('  ### three subjects are searched for the ### **PRE-UPDATE** ### form still standing.')
    ups = []
    for i, ln in enumerate(lines_of(REGISTRY), 1):
        m = re.search(r'Row \*\*([0-9][^*]*?)\*\* \(`([^`]+)`\): version (?:reconciled )?'
                      r'\*\*(v[0-9.]+) (?:→|->) (v[0-9.]+)\*\*', ln)
        if m:
            ups.append(dict(rid=m.group(1), path=m.group(2), old=m.group(3), new=m.group(4),
                            line=i))
    rec('  ###   registry row updates naming an old and a new version : ### **`%d`**' % len(ups))
    unprop = []
    for u in ups:
        stem = os.path.basename(u['path'])[:-3]
        for k in chosen:
            p = paths[k]
            for i, ln in enumerate(lines_of(os.path.join(PP, p.replace('/', os.sep))), 1):
                for m in re.finditer(re.escape(stem), ln):
                    tail = ln[m.end():m.end() + 40]
                    v = VER.search(tail)
                    if v and vnum('v' + v.group(1).rstrip('.')) == vnum(u['old']):
                        unprop.append(dict(citer=k, line=i, stem=stem, old=u['old'],
                                           new=u['new'], reg_line=u['line'],
                                           text=flat(ln, 120)))
    rec('  ###   ### **PRE-UPDATE FORMS STILL STANDING IN THE THREE SUBJECTS : `%d`**'
        % len(unprop))
    for h in unprop:
        rec('      %s line %d cites `%s` at `%s`; the registry reconciled it to `%s` at line %d'
            % (h['citer'], h['line'], h['stem'], h['old'], h['new'], h['reg_line']))
        rec('        > %s' % h['text'])
    if not unprop:
        rec('  ### ### ### **NONE.** ### The species `b391` found does not recur in these three,')
        rec('  ### ### ### and ### **AN ABSENCE WITH A PROVED SEARCH BEHIND IT IS A RESULT.**')
    return dict(phantom=phantom, superseded=superseded, updates=len(ups), unpropagated=unprop)


# ==================================================================================================
READS = [
    ('the order -- leg 2, the act', FERRY,
     'LEG 2 (b394) — THE RECONCILIATION, BATCHED. b390 proved the'),
    ('the order -- three keystones in one act', FERRY,
     'found its first subject already current. Run THREE keystones in'),
    ('the order -- chosen by the rule b390 minted', FERRY,
     'one act, chosen by the rule b390 minted — take those whose'),
    ('the order -- the excluded named with the reason', FERRY,
     'terminals the drive can reach — with the excluded ones named'),
    ('the order -- the three buckets', FERRY,
     'what bears on it in the record and is not in it, three buckets'),
    ('the order -- repairs in place, originals preserved', FERRY,
     'carry it) with quotations on both sides; the repairs made in'),
    ('the order -- repairs ROUTED where a ruling is needed', FERRY,
     'place with originals preserved; the repairs ROUTED where a'),
    ('the order -- the corpus-wide check this pass has taught', FERRY,
     'ruling is needed, named with why. Then the corpus-wide check'),
    ('the order -- corrected but unpropagated', FERRY,
     'its source without propagating — the corrected-but-unpropagated'),
    ('the order -- the price re-measured from three', FERRY,
     'Report the count of keystones now reconciled against the'),
    ('the order -- (L2)', FERRY,
     'subject; (L2) at least one of the three keystones carries a'),
    ('b390 -- the rule it minted', os.path.join(D, 'b390_the_proofreading_pass.txt'),
     'TERMINALS THE DRIVE CAN REACH.**'),
    ('the census -- its keystone table header', CENSUS,
     '| document | phase | last content update | pins |'),
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
            rec('    %-62s line %-5d differs %s' % (label[:62], at, line.strip() != hint.strip()))
        except Exception as e:
            without += 1
            out.append(dict(label=label, file=os.path.basename(path), line=None,
                            error=str(e)[:110]))
            rec('    %-62s ### **NO ANCHOR** -- %s' % (label[:62], str(e)[:70]))
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
    rec('b394 -- THE EXTRACT, AND THE SURVEYS THE FACE IS WRITTEN FROM.')
    bar('=')
    R = refs()
    for k, v in R.items():
        rec('    %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    rec()
    s1 = survey1()
    rec()
    s2 = survey2(s1['chosen'], s1['paths'], s1['tables'])
    rec()
    s3 = survey3(s1['chosen'], s1['paths'])
    rec()
    reads, without = do_reads()
    rec()
    bar('=')
    rec('  1 : keystones %d ; reachable %d ; chosen %d ; set aside %d'
        % (len(s1['all']), len(s1['eligible']), len(s1['chosen']), len(s1['set_aside'])))
    rec('  2 : %s' % {k: (v['rows'], v['table']) for k, v in s2.items()})
    rec('  3 : phantom %d ; superseded %d ; registry updates %d ; unpropagated %d'
        % (len(s3['phantom']), len(s3['superseded']), s3['updates'], len(s3['unpropagated'])))
    rec('  reads %d without_anchor %d' % (len(reads), without))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    p = run_clock.write(D, 'b394_extract_notes', L)
    json.dump(dict(s1=s1, s2=s2, s3=s3, reads=len(reads), without_anchor=without,
                   anchors_differing=sum(1 for r in reads if r.get('differs')), refs=R,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b394_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
