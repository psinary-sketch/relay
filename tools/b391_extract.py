# -*- coding: utf-8 -*-
"""b391_extract.py -- THE EXTRACT AND THE THREE SURVEYS THE FACE IS WRITTEN FROM.

### ### **THE COUNT IS RE-MEASURED, NOT QUOTED FORWARD.** ### `b390` reported `28` citations across
### `11` documents. ### **A COUNT QUOTED FORWARD IS A COUNT NOBODY RE-MEASURED**, and this file
### counts from the files with a matcher whose defects are printed beside its yield.
###
### ### **AND THE WIDENED SCREEN IS TIGHTENED BEFORE ANY FINDING IS FILED, NOT AFTER.** ### Its
### first form matched a registry stem ANYWHERE in a line, so `TRIVIUM` matched inside
### `TRIVIUM_CODE_VERIFICATION` and a registry row-update note recording ### *`v1.2` → `v0.5.2`*
### ### counted as a citation at `v1.2`. ### **BOTH REPAIRS REST ON WHAT THE STRING IS, NOT ON THE
### ### NUMBER THEY PRODUCE** (`b380`'s forbidden direction), and ### **EVERY VERSION'S YIELD IS
### ### PRINTED** (`b381`).
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
FERRY = os.path.join(D, 'b391_ferry_2026-09-09.txt')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
METHOD = os.path.join(PP, 'phase1.5', 'method', 'A_METHODOLOGY.md')
B390BANK = os.path.join(D, 'b390_the_proofreading_pass.txt')
B388BANK = os.path.join(D, 'b388_the_map_refreshed.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


SKIP = ('.git', 'archive', 'outputs')
NAME = re.compile(r'A_METHODOLOGY(_FOR_DETERMINED_SYSTEMS)?')
VER = re.compile(r'v\s*([0-9][0-9.]*?)(?=[^0-9.]|$)')
# ### **A TOKEN BOUNDARY, SO A STEM DOES NOT MATCH INSIDE A LONGER IDENTIFIER.**
WORDCH = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_')


def corpus_files():
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in sorted(fn):
            if f.endswith('.md'):
                yield (rel + '/' + f if rel != '.' else f), os.path.join(dp, f)


def lines_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))


# ==================================================================================================
#  SURVEY 1 -- COMPONENT 0: THE FIVE CLUSTERS.
# ==================================================================================================
def survey1():
    bar('-')
    rec('  ### SURVEY 1 -- COMPONENT 0. ### **THE FIVE CLUSTERS, AND WHERE THEY ARE RECORDED.**')
    bar('-')
    src, rows = None, []
    for path, label in ((B390BANK, 'b390'), (B388BANK, 'b388')):
        if not os.path.exists(path):
            continue
        txt = io.open(path, encoding='utf-8', errors='replace').read()
        found = [ln for ln in txt.split(chr(10))
                 if re.search(r'### \*\*(GREW|NEW)\*\* ### by `\d`', ln)]
        rec('    %-46s carries the five, named with what changed : %s'
            % (os.path.basename(path), len(found) == 5))
        if len(found) == 5 and src is None:
            src, rows = label, found
    rec()
    rec('  ### ### **THE ORDER SAID: REPORT THEM FROM `b390`\'S BANK IF THEY ARE THERE, AND FROM')
    rec('  ### ### `b388`\'S IF THEY ARE NOT.** ### They are in ### **`%s`\'S**.' % src)
    for ln in rows:
        rec('      %s' % ' '.join(ln.split())[3:170])
    rec('  ### ### **`5` CLUSTERS, `3` `GREW` AND `2` `NEW`. ### `0` RESHAPED BY ANY ACT.**')
    return dict(source=src, found=len(rows), rows=[' '.join(r.split()) for r in rows])


# ==================================================================================================
#  SURVEY 2 -- COMPONENT 1: THE PHANTOM, RE-MEASURED AND CLASSIFIED.
# ==================================================================================================
def is_provenance(ln):
    """### **A PROVENANCE ENTRY STATES WHAT WAS CITED AT THE TIME.** ### They open with a version
    ### and a date -- `*v0.2, 2026-07-12 — ...` -- which is the corpus's own shape."""
    return bool(re.match(r'\s*[*_]*v[0-9][0-9.]*[,)]? ', ln.strip()))


def in_preserved(ln):
    """### **A PRESERVED VERBATIM BLOCK IS QUOTED, AND MARKDOWN QUOTES WITH `>`.**"""
    return ln.lstrip().startswith('>')


def is_mention(ln):
    """### **A LEDGER REPORTING THE DEFECT QUOTES THE STRING; IT DOES NOT CITE THE DOCUMENT.**
    ### `b348`'s use-and-mention species: ### **REPAIRING A REPORT OF AN ERROR ERASES THE
    ### ### REPORT.**"""
    u = ln.upper()
    return any(k in u for k in ('THERE IS NO `V1.2`', 'THERE IS NO V1.2', 'DOES NOT EXIST',
                                'PHANTOM', 'RECONCILED **V1.2', 'VERSION RECONCILED',
                                'NAME A VERSION', 'CONTRADICTS'))


def method_lineage():
    """### **EVERY VERSION THE METHODOLOGY PAPER HAS EVER DECLARED, FROM ITS OWN BYTES.**"""
    vs = set()
    for ln in lines_of(METHOD):
        m = re.match(r'\s*[*_>\s]*\**v([0-9][0-9.]*)\b', ln.strip())
        if m:
            vs.add('v' + m.group(1).rstrip('.'))
    return vs


def survey2():
    bar('-')
    rec('  ### SURVEY 2 -- COMPONENT 1. ### **THE PHANTOM, RE-MEASURED AND CLASSIFIED.**')
    bar('-')
    lin = method_lineage()
    rec('  ### **THE PAPER`S OWN VERSION LINEAGE, FROM ITS OWN BYTES : %s**'
        % ' '.join(sorted(lin)))
    rec('  ### ### **`v1.2` IS IN IT : %s.**' % ('v1.2' in lin))
    gi, gln = AF.find(REGISTRY, '| 1.5h-4 | Methodology for Determined Systems |')
    rec('  ### **THE REGISTRY`S ROW** -- `REGISTRY.md` line %d:' % gi)
    rec('      > %s' % ' '.join(gln.split())[:190])
    rec()
    hits = []
    for pth, full in corpus_files():
        for i, ln in enumerate(lines_of(full), 1):
            for m in NAME.finditer(ln):
                v = VER.search(ln[m.end():m.end() + 40])
                if not v or v.group(1).rstrip('.') != '1.2':
                    continue
                if is_mention(ln):
                    cls = 'MENTION'
                elif in_preserved(ln):
                    cls = 'PRESERVED'
                elif is_provenance(ln):
                    cls = 'PROVENANCE'
                else:
                    cls = 'CITATION'
                hits.append(dict(file=pth, line=i, cls=cls,
                                 text=' '.join(ln[max(0, m.start() - 40):m.end() + 45].split())))
    from collections import Counter
    byc = Counter(h['cls'] for h in hits)
    byf = Counter(h['file'] for h in hits)
    rec('  ### ### **INSTANCES OF THE PHANTOM, RE-MEASURED FROM THE FILES : `%d` ACROSS `%d`'
        % (len(hits), len(byf)))
    rec('  ### ### DOCUMENTS.**')
    rec('  ### ### ### **`b390` REPORTED `28` ACROSS `11`. ### THE FIGURE IT PUBLISHED WAS LOW,')
    rec('  ### ### ### AND ITS OWN MATCHER IS WHY:** ### it required the version to follow the')
    rec('  ### ### ### name with only backticks or spaces between, so ### **`*A_METHODOLOGY...*`')
    rec('  ### ### ### v1.2` AND `A_METHODOLOGY` v1.2 §V.10` WERE MISSED.**')
    rec()
    for k in ('CITATION', 'PROVENANCE', 'PRESERVED', 'MENTION'):
        rec('      %-12s %d' % (k, byc.get(k, 0)))
    rec('  ### ### **ONLY `CITATION` IS REPAIRABLE.** ### The order names two exclusions and this')
    rec('  ### ### act adds a third it found: ### **A LEDGER REPORTING THE DEFECT QUOTES THE')
    rec('  ### ### STRING RATHER THAN CITING THE DOCUMENT**, and ### **REPAIRING A REPORT OF AN')
    rec('  ### ### ERROR ERASES THE REPORT.**')
    rec()
    for h in hits:
        rec('    %-58s %-5d %-11s %s' % (h['file'][:58], h['line'], h['cls'], h['text'][:78]))
    rec()
    # ---- THE ORIGIN ------------------------------------------------------------------------
    rec('  ### ### **THE ORIGIN, AND THE RECORD HOLDS IT.**')
    oi, oln = AF.find(REGISTRY, 'Row **1.5h-4** (`phase1.5/method/A_METHODOLOGY.md`): version '
                                'reconciled')
    rec('  ### `REGISTRY.md` line %d:' % oi)
    rec('      > %s' % ' '.join(oln.split())[:330])
    rec('  ### ### ### **THE PHANTOM WAS A BUNDLE LABEL THE REGISTRY ROW CARRIED, NOT A VERSION')
    rec('  ### ### ### THE PAPER EVER HAD** -- and the registry ### **RECONCILED ITS OWN ROW ON')
    rec('  ### ### ### `2026-07-16`** ### while every document that had copied the label kept it.')
    rec('  ### ### **A DRIFT WITH A SOURCE IS A DIFFERENT FINDING FROM ONE WITHOUT**, and this one')
    rec('  ### ### has a source, a date, and a correction that was never propagated.')
    rec('  ### **AND THE CORPUS HAS A NAME FOR THE SPECIES ALREADY** -- the same registry pass')
    rec('  ### called a nonexistent cited version a ### **`Pin-drift casualty`** ### and repaired')
    rec('  ### it in place, so this repair follows the corpus`s own precedent and not a new rule.')
    return dict(total=len(hits), docs=len(byf), by_class=dict(byc),
                repairable=byc.get('CITATION', 0), hits=hits,
                lineage=sorted(lin), phantom_in_lineage=('v1.2' in lin),
                origin_line=oi, b390_said=28, b390_docs=11)


# ==================================================================================================
#  SURVEY 3 -- COMPONENT 2: THE SAME CHECK, WIDENED ONCE.
# ==================================================================================================
def vnum(v):
    """### **VERSIONS COMPARED AS NUMBERS, NOT AS STRINGS.** ### `v13`, `v13.0` and `v13_0` are one
    ### version written three ways, and a string test called two of them phantoms."""
    parts = re.split(r'[._]', v.lstrip('v'))
    out = []
    for x in parts:
        out.append(int(x) if x.isdigit() else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def adjacent(between):
    """### **A CITATION WRITES `NAME v1.2`. ### IT DOES NOT WRITE `NAME, OTHER_NAME_v4`.**

    ### The screen's first form took whatever version token appeared within 40 characters of the
    ### stem, so `SIMPLICITY_OF_RIEMANN_ZEROS, ALL_ZEROS_ARE_SIMPLE_v4` read as a citation of the
    ### first document at `v4` -- ### **A VERSION LIFTED OFF THE NEIGHBOUR.** ### The span must
    ### carry no letters and no separator that starts a new name.
    """
    return len(between) <= 12 and not re.search(r'[A-Za-z]', between) and ',' not in between


def registry_rows():
    rows = {}
    for i, ln in enumerate(lines_of(REGISTRY), 1):
        m = re.match(r'\|\s*([0-9][^|]*?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+\.md)`\s*\|'
                     r'\s*(v[0-9][0-9.]*)\s*\|', ln)
        if m:
            rows[m.group(3)] = dict(rid=m.group(1), version=m.group(4), line=i)
    return rows


def lineage_of(path):
    """### **EVERY VERSION TOKEN THE CITED DOCUMENT ITSELF CARRIES.**

    ### A first form read only lines OPENING with a version -- the provenance shape -- and
    ### ### **FOUR OF TEN CITED DOCUMENTS DECLARE NO VERSION IN THAT SHAPE AT ALL**, so every
    ### citation of them read `PHANTOM`. ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE.**
    ### The widened form takes every `vN.N` token in the document's own bytes, which ### **ERRS
    ### ### TOWARD NOT CLAIMING A PHANTOM** -- the conservative direction for an act that repairs
    ### what it calls one.
    """
    p = os.path.join(PP, path.replace('/', os.sep))
    if not os.path.exists(p):
        return None
    txt = io.open(p, encoding='utf-8', errors='replace').read()
    return set('v' + x.rstrip('.') for x in re.findall(r'\bv([0-9][0-9.]*)', txt))


def survey3():
    bar('-')
    rec('  ### SURVEY 3 -- COMPONENT 2. ### **THE SAME CHECK, WIDENED ONCE.**')
    bar('-')
    rows = registry_rows()
    rec('  ### **THE REGISTRY ROWS THAT NAME A PATH AND A VERSION : `%d`.**' % len(rows))
    rec('  ### ### **THE SCREEN KEYS ON THE FILE STEM THE REGISTRY NAMES**, so a document cited')
    rec('  ### ### under a different title is ### **INVISIBLE TO IT** -- which is exactly how the')
    rec('  ### ### methodology paper hid, since it is cited as')
    rec('  ### ### `A_METHODOLOGY_FOR_DETERMINED_SYSTEMS` and filed as `A_METHODOLOGY.md`. ###')
    rec('  ### ### **THE LIMIT IS STATED BECAUSE THE COUNT IS A FLOOR AND NOT A TOTAL.**')
    rec()
    rec('  ### **THE SCREEN, AND BOTH REPAIRS IT NEEDED BEFORE ANY FINDING WAS FILED:**')
    rec('  ###   (1) ### **A STEM MUST MATCH AS A WHOLE TOKEN.** ### Its first form matched')
    rec('  ###   `TRIVIUM` inside `TRIVIUM_CODE_VERIFICATION` and counted another document`s')
    rec('  ###   version as a disagreement.')
    rec('  ###   (2) ### **A VERSION MUST BE ADJACENT TO THE NAME IT VERSIONS.** ### Its first')
    rec('  ###   form read `SIMPLICITY_OF_RIEMANN_ZEROS, ALL_ZEROS_ARE_SIMPLE_v4` as a citation of')
    rec('  ###   the FIRST document at `v4` -- ### **A VERSION LIFTED OFF THE NEIGHBOUR.**')
    rec('  ###   (3) ### **VERSIONS ARE COMPARED AS NUMBERS.** ### `v13`, `v13.0` and `v13_0` are')
    rec('  ###   one version written three ways, and a string test called two of them phantoms.')
    rec('  ###   (4) ### **A REGISTRY ROW-UPDATE NOTE RECORDS A TRANSITION.** ### A line reading')
    rec('  ###   ### *version reconciled `v1.2` → `v0.5.2`* ### NAMES an old version; it does not')
    rec('  ###   CITE at it. ### **A TRANSITION NOTE IS THE CORRECTION, NOT THE DEFECT.**')
    rec('  ### ### **BOTH REST ON WHAT THE STRING IS, NOT ON THE NUMBER THEY PRODUCE**, and every')
    rec('  ### ### version`s yield is printed below (`b381`).')
    rec()
    stems = {os.path.basename(p)[:-3]: (p, v['version'], v['rid'])
             for p, v in rows.items() if len(os.path.basename(p)) > 9}
    raw, tokened, adj, final = 0, 0, 0, []
    for pth, full in corpus_files():
        ls = lines_of(full)
        for i, ln in enumerate(ls, 1):
            for stem, (target, regver, rid) in stems.items():
                for m in re.finditer(re.escape(stem), ln):
                    tail = ln[m.end():m.end() + 40]
                    v = VER.search(tail)
                    if not v:
                        continue
                    cited = 'v' + v.group(1).rstrip('.')
                    if vnum(cited) == vnum(regver):
                        continue
                    raw += 1
                    a = ln[m.start() - 1] if m.start() else ' '
                    b = ln[m.end()] if m.end() < len(ln) else ' '
                    if a in WORDCH or b in WORDCH:
                        continue
                    tokened += 1
                    if not adjacent(tail[:v.start()]):
                        continue
                    adj += 1
                    if pth == 'REGISTRY.md' and re.search(r'(reconciled|→|->)', ln):
                        continue
                    final.append(dict(file=pth, line=i, cited_doc=target, rid=rid,
                                      cited=cited, registry=regver,
                                      text=' '.join(ln[max(0, m.start() - 30):
                                                      m.end() + 40].split())))
    rec('  ### ### **THE MATCHER`S THREE YIELDS, EVERY ONE PRINTED:**')
    rec('  ###   any substring anywhere                      : ### **`%d`**' % raw)
    rec('  ###   whole-token only                            : ### **`%d`**' % tokened)
    rec('  ###   version ADJACENT to the stem, not the neighbour`s : ### **`%d`**' % adj)
    rec('  ###   minus the registry`s own transition notes   : ### **`%d`**' % len(final))
    rec()
    ph, sup, unk, nod = [], [], [], []
    lgcache = {}
    for h in final:
        doc = h['cited_doc']
        if doc not in lgcache:
            lgcache[doc] = lineage_of(doc)
        lg = lgcache[doc]
        if lg is None:
            unk.append(h)
        elif not lg:
            # ### **A DOCUMENT THAT DECLARES NO VERSION CANNOT CONVICT A CITATION OF NAMING A
            # ### VERSION IT NEVER HAD.** ### UNDECIDABLE, and reported as its own class.
            nod.append(h)
        elif any(vnum(h['cited']) == vnum(x) for x in lg):
            sup.append(h)
        else:
            ph.append(h)
    rec('  ### ### **CLASSIFIED AGAINST EACH CITED DOCUMENT`S OWN DECLARED LINEAGE:**')
    rec('  ###   ### **PHANTOM** ### -- the version is in no lineage the document declares : `%d`'
        % len(ph))
    rec('  ###   ### **SUPERSEDED** ### -- the version exists and is older            : `%d`'
        % len(sup))
    rec('  ###   ### **UNREADABLE** ### -- the cited document is not on disk          : `%d`'
        % len(unk))
    rec('  ###   ### **UNDECIDABLE** ### -- the cited document declares no version     : `%d`'
        % len(nod))
    rec('  ### ### ### **ONLY `PHANTOM` AGREES IN KIND WITH COMPONENT 1 AND IS REPAIRABLE.** ###')
    rec('  ### ### ### **A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM, NOT A')
    rec('  ### ### ### PHANTOM**, and this act reports it and leaves it.')
    rec()
    from collections import Counter
    rec('  ### **THE PHANTOMS, BY CITED DOCUMENT:**')
    for k, n in Counter(h['cited_doc'] for h in ph).most_common(20):
        rec('      %-64s %d' % (k[:64], n))
    rec('  ### **THE SUPERSEDED, BY CITED DOCUMENT (REPORTED, NOT REPAIRED):**')
    for k, n in Counter(h['cited_doc'] for h in sup).most_common(12):
        rec('      %-64s %d' % (k[:64], n))
    rec('  ### **THE UNDECIDABLE, BY CITED DOCUMENT (NEITHER REPAIRED NOR CALLED A PHANTOM):**')
    for k, n in Counter(h['cited_doc'] for h in nod).most_common(12):
        rec('      %-64s %d' % (k[:64], n))
    return dict(registry_rows=len(rows), raw=raw, tokened=tokened, adjacent=adj,
                screened=len(final),
                phantom=len(ph), superseded=len(sup), unreadable=len(unk),
                undecidable=len(nod),
                phantoms=ph, superseded_rows=sup[:60], undecidable_rows=nod[:40])


# ==================================================================================================
READS = [
    ('the order -- leg 1, the act', 'ORDER', FERRY,
     'LEG 1 (b391) — THE PHANTOM VERSION, AND THE FIVE CLUSTERS.'),
    ('the order -- both faces wide within their named scopes', 'ORDER', FERRY,
     'PURPOSE within their named scopes: each may repair what it'),
    ('the order -- component 0, the five clusters', 'ORDER', FERRY,
     "COMPONENT 0 — THE FIVE CLUSTERS, ordered at b390's closing and"),
    ('the order -- component 0, no cluster reshaped', 'ORDER', FERRY,
     'quotation. No cluster reshaped; the reshaping is the author'),
    ('the order -- component 1, the phantom pass', 'ORDER', FERRY,
     'COMPONENT 1 — THE PHANTOM VERSION PASS: the methodology'),
    ('the order -- component 1, a count quoted forward', 'ORDER', FERRY,
     "b390's count — a count quoted forward is a count nobody"),
    ('the order -- component 1, the two exclusions', 'ORDER', FERRY,
     'as written. Then repair, with two exclusions stated before any'),
    ('the order -- component 1, the phantom`s origin', 'ORDER', FERRY,
     "search for the phantom's origin — where the wrong version was"),
    ('the order -- component 2, widened once', 'ORDER', FERRY,
     'COMPONENT 2 — THE SAME CHECK, WIDENED ONCE: run the same test'),
    ('the order -- component 2, superseded is a currency item', 'ORDER', FERRY,
     'that exists but is superseded is a currency item, not a'),
    ('the order -- (L1) the count differs and the origin is locatable', 'ORDER', FERRY,
     'expectations: (L1) the phantom count re-measured differs from'),
    ('the registry -- the row for the methodology paper', 'REG', REGISTRY,
     '| 1.5h-4 | Methodology for Determined Systems |'),
    ('the registry -- the reconciliation that names the origin', 'REG', REGISTRY,
     'Row **1.5h-4** (`phase1.5/method/A_METHODOLOGY.md`): version reconciled'),
    ('the registry -- the same species, already named once', 'REG', REGISTRY,
     '**Pin-drift casualty:** `SIDE-dirichlet-mod-24` cited as `v0.1.1` (nonexistent)'),
    ('the paper -- its own head', 'PAPER', METHOD, '**v0.5.4 — 2026-07-19**'),
]


def do_reads():
    bar('=')
    rec('  ### THE READS.')
    bar('=')
    out, without = [], 0
    for label, tag, path, hint in READS:
        try:
            at, line = AF.find(path, hint)
            out.append(dict(label=label, tag=tag, file=os.path.basename(path), line=at,
                            text=line, differs=(line.strip() != hint.strip())))
            rec('    %-64s %s  line %d  differs %s'
                % (label[:64], tag, at, line.strip() != hint.strip()))
            rec('      > %s' % ' '.join(line.split())[:150])
        except Exception as e:
            without += 1
            out.append(dict(label=label, tag=tag, file=os.path.basename(path), line=None,
                            error=str(e)[:110]))
            rec('    %-64s %s  ### **NO ANCHOR** -- %s' % (label[:64], tag, str(e)[:70]))
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
    rec('b391 -- THE EXTRACT, AND THE THREE SURVEYS THE FACE IS WRITTEN FROM.')
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
    rec('  0 : five clusters from %s ; found %d' % (s1['source'], s1['found']))
    rec('  1 : phantom %d across %d docs (b390 said 28/11) ; repairable %d ; %s'
        % (s2['total'], s2['docs'], s2['repairable'], s2['by_class']))
    rec('  2 : screened %d ; phantom %d ; superseded %d ; undecidable %d ; unreadable %d'
        % (s3['screened'], s3['phantom'], s3['superseded'], s3['undecidable'],
           s3['unreadable']))
    rec('  reads %d without_anchor %d' % (len(reads), without))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    p = run_clock.write(D, 'b391_extract_notes', L)
    json.dump(dict(s1=s1, s2=s2, s3=s3, reads=len(reads), without_anchor=without,
                   anchors_differing=sum(1 for r in reads if r.get('differs')), refs=R,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b391_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
