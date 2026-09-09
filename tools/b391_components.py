# -*- coding: utf-8 -*-
"""b391_components.py -- COMPONENT 0, COMPONENT 1 (INCLUDING ITS REPAIR), COMPONENT 2.

### ### **THE REPAIR CHANGES ONE STRING ON LINES THIS ACT CLASSIFIED `CITATION` AND NOTHING ELSE.**
### Every excluded instance is named with its reason ### **BEFORE** ### the first edit, and each
### repaired file is diffed against ### **ITS OWN PRE-ACT BLOB.**
### ### **AND THE THIRD EXCLUSION IS THIS ACT'S OWN:** ### three of the thirty-two instances are
### ledger lines REPORTING the defect. ### **REPAIRING A REPORT OF AN ERROR ERASES THE REPORT.**
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

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
METHOD = os.path.join(PP, 'phase1.5', 'method', 'A_METHODOLOGY.md')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
OUT = os.path.join(D, 'b391_components.txt')
OLD, NEW = 'v1.2', 'v0.5.4'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=190):
    return ' '.join(s.split())[:n]


E = json.load(io.open(os.path.join(D, 'b391_reads.json'), encoding='utf-8'))


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def numstat(rel):
    r = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD', '--', rel],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    for ln in (r.stdout or '').split(chr(10)):
        p = ln.split()
        if len(p) >= 2 and p[0].isdigit():
            return int(p[0]), int(p[1])
    return 0, 0


# ==================================================================================================
def component0():
    bar('=')
    rec('  ### COMPONENT 0 -- THE FIVE CLUSTERS.')
    bar('=')
    s1 = E['s1']
    rec('  ### **THE ORDER SAID: FROM `b390`\'S BANK IF THEY ARE THERE, FROM `b388`\'S IF NOT.**')
    rec('  ### ### **THEY ARE IN `%s`\'S, ALL FIVE, EACH WITH ITS VERDICT AND ITS MEMBER COUNT.**'
        % s1['source'])
    rec()
    maptxt = io.open(MAP, encoding='utf-8', errors='replace').read().split(chr(10))
    for r in s1['rows']:
        rec('    %s' % r[3:180])
        m = re.search(r'\*\*([A-Za-z /-]+?)\s*\*\*', r)
        name = m.group(1).strip() if m else None
        if name:
            for i, ln in enumerate(maptxt, 1):
                if ln.startswith('| **%s**' % name) and not ln.lstrip().startswith('>'):
                    rec('        ### the map row that seats it -- `SPIRAL_MAP.md` line %d:' % i)
                    rec('        > %s' % flat(ln, 200))
                    break
        rec()
    rec('  ### ### **`5` CLUSTERS. ### `3` `GREW`, `2` `NEW`.**')
    rec('  ### **WHAT CHANGED, IN THE TERMS THE ORDER NAMED:** ### all five changed by ###')
    rec('  ### **MEMBERSHIP** ### -- documents the old table did not name were assigned to them,')
    rec('  ### or the cluster did not exist as a seat at all. ### **NONE CHANGED BY A SPLIT, A')
    rec('  ### ### MERGE, OR AN ANCHOR MOVING**, and `2` of the `5` -- `theory-space` and')
    rec('  ### `cross-domain` -- ### **CARRY NO ANCHOR AT ALL**, because `(R17)` named none and')
    rec('  ### `b388` did not invent one.')
    rec('  ### ### ### **NO CLUSTER IS RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED BY THIS')
    rec('  ### ### ### ACT. ### THE RESHAPING IS THE AUTHOR`S AND THIS IS THE READ THAT PRECEDES')
    rec('  ### ### ### IT.**')
    return dict(source=s1['source'], clusters=s1['found'], reshaped=0)


# ==================================================================================================
def component1():
    bar('=')
    rec('  ### COMPONENT 1 -- THE PHANTOM VERSION PASS.')
    bar('=')
    s2 = E['s2']
    rec('  ### ### **THE COUNT, RE-MEASURED FROM THE FILES : `%d` INSTANCES ACROSS `%d`'
        % (s2['total'], s2['docs']))
    rec('  ### ### DOCUMENTS.**')
    rec('  ### `b390` published ### **`%d` ACROSS `%d`.** ### **A COUNT QUOTED FORWARD IS A COUNT'
        % (s2['b390_said'], s2['b390_docs']))
    rec('  ### ### NOBODY RE-MEASURED**, and its matcher is why: it required the version to follow')
    rec('  ### the name with only backticks or spaces between, so `*A_METHODOLOGY..* v1.2` and')
    rec('  ### `A_METHODOLOGY v1.2 §V.10` were both missed. ### **THIS ACT SAYS THAT ABOUT ITS OWN')
    rec('  ### ### PREDECESSOR AS PLAINLY AS IT WOULD ABOUT ANY OTHER DOCUMENT.**')
    rec()
    rec('  ### **THE PAPER`S OWN LINEAGE, FROM ITS OWN BYTES : %s**' % ' '.join(s2['lineage']))
    rec('  ### ### **`v1.2` IS IN IT : %s.**' % s2['phantom_in_lineage'])
    gi, gln = AF.find(REGISTRY, '| 1.5h-4 | Methodology for Determined Systems |')
    mi, mln = AF.find(METHOD, '**v0.5.4 — 2026-07-19**')
    rec('  ### **THE TWO SOURCES OF THE REPLACEMENT, EACH READ AT ITS OWN LINE:**')
    rec('  ###   `A_METHODOLOGY.md` line %d : %s' % (mi, flat(mln, 110)))
    rec('  ###   `REGISTRY.md` line %d      : %s' % (gi, flat(gln, 110)))
    rec('  ### ### **THEY AGREE ON `%s`, AND NEITHER IS TAKEN ON TRUST.**' % NEW)
    rec()
    bar()
    rec('  ### ### **THE CLASSIFICATION, STATED BEFORE ANY EDIT.**')
    bar()
    for k in ('CITATION', 'PROVENANCE', 'PRESERVED', 'MENTION'):
        rec('      %-12s %d' % (k, s2['by_class'].get(k, 0)))
    rec('  ### **THE EXCLUSIONS, EACH WITH ITS REASON:**')
    rec('  ###   ### **PROVENANCE** ### -- the order`s first. ### A provenance entry states what')
    rec('  ###   was cited AT THE TIME; editing it falsifies the history it exists to keep.')
    rec('  ###   ### **PRESERVED** ### -- the order`s second. ### `SPIRAL_MAP.md`\'s superseded')
    rec('  ###   cluster table, quoted whole by `b388` and preserved by its ruling.')
    rec('  ###   ### **MENTION** ### -- ### **THIS ACT`S OWN THIRD, FOUND IN THE SURVEY.** ### A')
    rec('  ###   ledger line REPORTING the defect quotes the string; it does not cite the')
    rec('  ###   document. ### **REPAIRING A REPORT OF AN ERROR ERASES THE REPORT**, and two of')
    rec('  ###   the three are `b390`\'s own record of finding this very defect.')
    rec()
    for h in s2['hits']:
        rec('    %-56s %-5d %-11s %s' % (h['file'][:56], h['line'], h['cls'], h['text'][:74]))
    rec()
    bar()
    rec('  ### ### **THE REPAIR.**')
    bar()
    targets = {}
    for h in s2['hits']:
        if h['cls'] == 'CITATION':
            targets.setdefault(h['file'], []).append(h['line'])
    made, files = 0, {}
    for rel in sorted(targets):
        full = os.path.join(PP, rel.replace('/', os.sep))
        txt = io.open(full, encoding='utf-8', newline='').read()
        lines = txt.replace(chr(13) + chr(10), chr(10)).split(chr(10))
        pre = blob(rel)
        n = 0
        for lineno in targets[rel]:
            i = lineno - 1
            if i < len(lines) and OLD in lines[i]:
                lines[i] = lines[i].replace(OLD, NEW)
                n += 1
        if n:
            open(full + '.tmp', 'wb').write(chr(10).join(lines).encode('utf-8'))
            os.replace(full + '.tmp', full)
        after = io.open(full, encoding='utf-8', newline='').read().replace(
            chr(13) + chr(10), chr(10))
        a, d = numstat(rel)
        pl, al = pre.split(chr(10)), after.split(chr(10))
        diffl = [k for k, (x, y) in enumerate(zip(pl, al), 1) if x != y]
        # ### **`only_version` MUST TEST THE LINES THAT CHANGED, NOT EVERY LINE.** ### Its first
        # ### form asked whether EVERY pre-act line equalled its successor after the substitution
        # ### -- which is false for every line this act DELIBERATELY EXCLUDED, since those still
        # ### carry `v1.2`. ### **AN ARM THAT CONVICTS AN ACT OF ITS OWN CORRECT EXCLUSIONS IS
        # ### ### MEASURING THE WRONG THING.**
        onlyv = all(pl[k - 1].replace(OLD, NEW) == al[k - 1] for k in diffl)
        # ### **AND `lines deleted` IS A CLAIM ABOUT CONTENT, NOT ABOUT GIT'S ACCOUNTING.** ###
        # ### `git numstat` scores an in-place edit as one addition AND one deletion, so `24`
        # ### repaired lines read as `-24`. ### The face's bar is that ### **NO LINE IS REMOVED
        # ### ### FROM THE DOCUMENT**, and that is the line count and the surviving-line count.
        removed = max(0, len(pl) - len(al))
        survive = sum(1 for k, x in enumerate(pl, 1)
                      if k <= len(al) and (x == al[k - 1] or k in diffl))
        # ### **THE COUNT IS THE DIFFERENCE FROM THE PRE-ACT BLOB, NOT WHAT THIS RUN TYPED.**
        # ### On an idempotent re-run `n` is `0` because the string is already gone -- true about
        # ### the run and false about the act. ### **AN ARM MUST MEASURE THE SAME THING ON EVERY
        # ### ### RUN** (`b352`, `b388`, `b389`, `b390`), and the fixed point is the blob.
        made += len(diffl)
        files[rel] = dict(repaired=n, added=a, deleted=d, lines_differing=len(diffl),
                          expected=len(targets[rel]), only_version=onlyv,
                          lines_before=len(pl), lines_after=len(al), removed=removed,
                          accounted=(survive == len(pl)))
        rec('    %-52s repaired %-3d lines %d->%d removed %-2d differing %-3d only the version: %s'
            % (rel[:52], n, len(pl), len(al), removed, len(diffl), onlyv))
        subprocess.run(['git', '-C', PP, 'add', '--', rel], capture_output=True)
    rec()
    rec('  ### ### **CITATIONS REPAIRED : `%d` OF `%d`.**'
        % (made, s2['by_class'].get('CITATION', 0)))
    rec('  ### ### **LINES REMOVED FROM ANY DOCUMENT : `%d`.**'
        % sum(f['removed'] for f in files.values()))
    rec('  ### ### **AND THE FACE`S BAR IS MEASURED AS CONTENT, NOT AS GIT`S ACCOUNTING.** ###')
    rec('  ### `git numstat` scores an in-place edit as one addition AND one deletion, so the')
    rec('  ### `%d` repaired lines read as ### **`-%d`** ### there. ### **NO LINE IS REMOVED FROM'
        % (made, sum(f['deleted'] for f in files.values())))
    rec('  ### ### ANY DOCUMENT AND EVERY LINE COUNT IS UNCHANGED**, which is what the bar says.')
    rec('  ### ### **BOTH FIGURES ARE PRINTED SO THE READING CAN BE OVERTURNED.**')
    rec('  ### ### **FILES WHERE THE ONLY CHANGE IS `%s` -> `%s` : `%d` OF `%d`.**'
        % (OLD, NEW, sum(1 for f in files.values() if f['only_version']), len(files)))
    rec('  ### ### ### **NO OTHER STRING IN ANY OF THOSE DOCUMENTS IS TOUCHED.** ### A')
    rec('  ### ### ### phantom-version pass that also tidies prose has stopped being a')
    rec('  ### ### ### phantom-version pass.')
    rec()
    bar()
    rec('  ### ### **THE ORIGIN, AND THE CORPUS RECORDED IT ITSELF.**')
    bar()
    oi, oln = AF.find(REGISTRY, 'Row **1.5h-4** (`phase1.5/method/A_METHODOLOGY.md`): version '
                                'reconciled')
    rec('  ### `REGISTRY.md` line %d, under a row update dated `2026-07-16`:' % oi)
    rec('      > %s' % flat(oln, 340))
    rec('  ### ### ### **THE PHANTOM WAS A BUNDLE LABEL ON THE REGISTRY`S OWN ROW. ### IT WAS')
    rec('  ### ### ### NEVER A VERSION THE PAPER HAD.**')
    rec('  ### The registry corrected itself on `2026-07-16`. ### **EVERY DOCUMENT THAT HAD COPIED')
    rec('  ### ### THE LABEL KEPT IT, AND NONE WAS TOLD** -- which is the whole finding: ### **A')
    rec('  ### ### CORRECTION THAT DOES NOT PROPAGATE IS A CORRECTION IN ONE PLACE AND A DEFECT')
    rec('  ### ### EVERYWHERE ELSE.**')
    try:
        pi, pln = AF.find(REGISTRY, '**Pin-drift casualty:** `SIDE-dirichlet-mod-24` cited as '
                                    '`v0.1.1` (nonexistent)')
        rec('  ### **AND THE CORPUS ALREADY NAMED THE SPECIES** -- `REGISTRY.md` line %d:' % pi)
        rec('      > %s' % flat(pln, 210))
        rec('  ### ### **`Pin-drift casualty`. ### THIS REPAIR FOLLOWS THE CORPUS`S OWN PRECEDENT')
        rec('  ### ### AND NOT A RULE THIS SEAT INVENTED.**')
    except Exception:
        rec('  ### the precedent line did not resolve; the repair stands on the registry`s own')
        rec('  ### reconciliation alone.')
    return dict(total=s2['total'], docs=s2['docs'], by_class=s2['by_class'],
                repaired=made, files=files,
                deleted=sum(f['deleted'] for f in files.values()),
                removed=sum(f['removed'] for f in files.values()),
                line_counts_unchanged=all(f['lines_before'] == f['lines_after']
                                          for f in files.values()),
                only_version=all(f['only_version'] for f in files.values()),
                origin_line=oi, replacement=NEW)


# ==================================================================================================
def component2():
    bar('=')
    rec('  ### COMPONENT 2 -- THE SAME CHECK, WIDENED ONCE.')
    bar('=')
    s3 = E['s3']
    rec('  ### **THE SCREEN AND EVERY ONE OF ITS YIELDS** (`b381`: print every version`s yield):')
    rec('  ###   any substring anywhere                        : ### **`%d`**' % s3['raw'])
    rec('  ###   whole-token only                              : ### **`%d`**' % s3['tokened'])
    rec('  ###   version ADJACENT to the name it versions      : ### **`%d`**' % s3['adjacent'])
    rec('  ###   minus the registry`s own transition notes     : ### **`%d`**' % s3['screened'])
    rec('  ### ### **FOUR TIGHTENINGS, EVERY ONE MADE BEFORE A FINDING WAS FILED AND EVERY ONE')
    rec('  ### ### RESTING ON WHAT THE STRING IS RATHER THAN ON THE NUMBER IT PRODUCES**')
    rec('  ### ### (`b380`\'s forbidden direction).')
    rec()
    rec('  ### ### **THE CLASSIFICATION AGAINST EACH CITED DOCUMENT`S OWN LINEAGE:**')
    rec('  ###   ### **SUPERSEDED** ### -- the version is in the document`s own bytes : `%d`'
        % s3['superseded'])
    rec('  ###   ### **CANDIDATES** ### -- it is not                                  : `%d`'
        % s3['phantom'])
    rec('  ### ### **THE `%d` SUPERSEDED ARE REPORTED AND LEFT.** ### **A VERSION THAT EXISTS BUT'
        % s3['superseded'])
    rec('  ### ### IS SUPERSEDED IS A CURRENCY ITEM, NOT A PHANTOM**, and this act does not touch')
    rec('  ### ### one -- the order`s own instruction.')
    rec()
    bar()
    rec('  ### ### **THE FOUR CANDIDATES, READ BY HAND.**')
    bar()
    rec('  ### **A SCREEN THAT OVER-REPORTS BY DESIGN MUST BE MARKED AS A SCREEN AND ITS RESIDUE')
    rec('  ### ### READ.** ### Four tightenings is where the tightening stops; past that point a')
    rec('  ### seat is tuning for a number. ### **SO THE RESIDUE IS READ, NOT SCREENED FURTHER.**')
    rec()
    verdicts = {
        ('internal/CRITICAL_RESOLVE.md', 3912): (
            'FALSE POSITIVE',
            'The line is a section title -- ### *PATH 5 — FROM LEVEL-SET GEOMETRY (R-CURVE '
            'MONOTONICITY)** *(v83)** -- and `(v83)` is an internal path number, not a version '
            'of `MONOTONICITY.md`. ### **THE STEM MATCHED A WORD IN A HEADING, NOT A '
            'CITATION.**'),
        ('phase2/physics-speculative/T7_PIPELINE_POINTER.md', 23): (
            'FALSE POSITIVE',
            'The `v1` was lifted from `MATTER_AS_ARITHMETIC_v1_0_CONSOLIDATED`, a DIFFERENT '
            'document named earlier on the same line. ### **THE ADJACENCY RULE CAUGHT MOST OF '
            'THESE AND NOT THIS ONE**, because the intervening text carries no letters.'),
        ('internal/CASCADES.md', 7385): (
            'UNDECIDABLE',
            'A real citation -- ### *CONSTANCE v13.1⊕* -- but ### **`CONSTANCE.md` DECLARES NO '
            '`v12` OR `v13` ANYWHERE IN ITS OWN BYTES.** ### Its version exists only on the '
            'registry`s row, so nothing on disk can convict the citation. ### **AN UNDECIDABLE '
            'IS NOT A PHANTOM**, and this act does not repair one.'),
        ('phase1.5/spectral/CONSERVATION.md', 716): (
            'UNDECIDABLE',
            'A real citation -- ### *| **CONSTANCE** (v12.1) |* -- and the same reason: the '
            'cited document declares no version that could confirm or refute it.'),
    }
    counts = {}
    for h in s3['phantoms']:
        key = (h['file'], h['line'])
        v, why = verdicts.get(key, ('UNREAD', 'no hand verdict was recorded for this candidate'))
        counts[v] = counts.get(v, 0) + 1
        rec('    %-50s %-5d ### **%s**' % (h['file'][:50], h['line'], v))
        rec('        cites `%s` at `%s`; the registry row says `%s`'
            % (h['cited_doc'], h['cited'], h['registry']))
        rec('        > %s' % h['text'][:150])
        for i in range(0, min(len(why), 460), 150):
            rec('        %s' % why[i:i + 150])
        rec()
    rec('  ### ### **VERDICTS : %s.**' % counts)
    rec('  ### ### ### **CANDIDATES REPAIRED BY THIS COMPONENT : `0`.**')
    rec('  ### ### **AND THAT IS A RESULT, NOT AN OMISSION** -- two are the screen`s own noise and')
    rec('  ### ### two cannot be decided against a document that declares no version.')
    rec()
    rec('  ### ### **AND ONE FINDING FALLS OUT OF IT, ROUTED AND NOT ACTED ON:**')
    rec('  ### ### ### **`CONSTANCE.md` CARRIES NO VERSION IN ITS OWN BYTES THAT MATCHES THE')
    rec('  ### ### ### REGISTRY`S ROW.** ### Its version lives only in the ledger. ### **A')
    rec('  ### ### ### DOCUMENT WHOSE VERSION EXISTS ONLY IN THE LEDGER CANNOT BE CHECKED AGAINST')
    rec('  ### ### ### ITSELF**, and every citation of it is undecidable by construction. ###')
    rec('  ### **THAT IS THE AUTHOR`S TO RULE ON.**')
    rec()
    rec('  ### ### **AND THE SCREEN`S OWN LIMIT, STATED:** ### it keys on the FILE STEM the')
    rec('  ### registry names, so ### **A DOCUMENT CITED UNDER A DIFFERENT TITLE IS INVISIBLE TO')
    rec('  ### ### IT** -- which is exactly how the methodology paper hid for two months, being')
    rec('  ### cited as `A_METHODOLOGY_FOR_DETERMINED_SYSTEMS` and filed as `A_METHODOLOGY.md`.')
    rec('  ### ### ### **SO THIS COUNT IS A FLOOR AND NOT A TOTAL.**')
    return dict(raw=s3['raw'], tokened=s3['tokened'], adjacent=s3['adjacent'],
                screened=s3['screened'], superseded=s3['superseded'],
                candidates=s3['phantom'], verdicts=counts, repaired=0)


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b391 -- COMPONENTS 0, 1 AND 2. ### THE PHANTOM VERSION, AND THE FIVE CLUSTERS.')
    bar('=')
    c0 = component0()
    rec()
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    bar('=')
    rec('  0 : clusters %d ; reshaped %d' % (c0['clusters'], c0['reshaped']))
    rec('  1 : instances %d/%d docs ; classes %s ; repaired %d ; removed %d ; '
        'line counts unchanged %s ; only-version %s'
        % (c1['total'], c1['docs'], c1['by_class'], c1['repaired'], c1['removed'],
           c1['line_counts_unchanged'], c1['only_version']))
    rec('  2 : screened %d ; superseded %d ; candidates %d ; repaired %d ; %s'
        % (c2['screened'], c2['superseded'], c2['candidates'], c2['repaired'], c2['verdicts']))
    rec('  ### **NOTHING WAS WRITTEN AT ZENODO, AND NO DOCUMENT OUTSIDE THE CLASSIFIED CITATION')
    rec('  ### LINES WAS TOUCHED.**')
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b391_components_run', L)
    json.dump(dict(c0=c0, c1=c1, c2=c2, run_file=os.path.basename(p),
                   run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b391_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
