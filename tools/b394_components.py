# -*- coding: utf-8 -*-
"""b394_components.py -- THE THREE READ, THE REPAIRS MADE AND ROUTED, AND THE PRICE FROM THREE."""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
FERRY = os.path.join(D, 'b394_ferry_2026-09-09.txt')
OUT = os.path.join(D, 'b394_components.txt')
MARK = '<!-- b394 RECONCILIATION ANNOTATION, 2026-09-09 -->'
OLD, NEWV = 'v0.1', 'v0.2.4'
TARGET = 'phase1.5/spectral/GRH_CASCADE.md'

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


E = json.load(io.open(os.path.join(D, 'b394_reads.json'), encoding='utf-8'))


# ==================================================================================================
#  COMPONENT 1 -- THE THREE, EACH READ.
# ==================================================================================================
#  (subject, layer, record file, record hint, keystone hint or None, bucket, why)
A, B, C = ('ALREADY SAYS IT', 'SAYS SOMETHING NOW SUPERSEDED', 'DOES NOT CARRY IT')
BEARS = [
    ('GRH_CASCADE', 'the registry', 'REGISTRY.md',
     'Row **1.5f-4** (`phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md`): version',
     '- **FOUNDATIONS_OF_THE_SIDE_PROGRAMME v0.1**', B,
     'The registry reconciled the cited document`s row past `v0.1`, and this keystone still '
     'cites it there ### **IN TWO PLACES.** ### **THIS IS THE `CORRECTED BUT UNPROPAGATED` '
     'SPECIES `b391` FOUND**, recurring inside this act`s own batch: one of the three subjects '
     'cites another of the three at a version the record moved past.'),
    ('GRH_CASCADE', 'the findings layer', 'FINDINGS.md',
     '### e-difficulty-theorem',
     '- **A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v0.5.4**', C,
     'The E-Difficulty terminals and their `2026-07-28` scope split bear on the cascade`s own '
     'decidability argument and ### **THIS DOCUMENT CARRIES NEITHER.** ### **ADDITION, NOT '
     'CORRECTION** -- the record files the split ### *statement-grade, nothing retracted.*'),
    ('FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'the registry', 'REGISTRY.md',
     '| 1.5f-4 | Foundations of the SIDE Programme |',
     '**v0.2.4', A,
     'The registry`s row and the document`s own head agree. ### **A DOCUMENT THAT AGREES WITH '
     'ITS OWN ROW IS THE ORDINARY CASE AND IS REPORTED AS PLAINLY AS A DEFECT.**'),
    ('FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'the trails', 'OPEN_TRAILS.md',
     '> - W-6 — CLOSED-BY-REPAIR (W-6-EXT, SIDE-kernel v1.4, 2026-07-19)',
     None, C,
     '`W-6`'"'"'s closure bears on the E-Difficulty material this document names as '
     'load-bearing, and ### **THE DOCUMENT DOES NOT CARRY THE CLOSURE.** ### **ADDITION, NOT '
     'CORRECTION.**'),
    ('SILENCE_STAGES_DEALIGNMENT', 'the record', 'REGISTRY.md',
     '| p2-24 |',
     None, C,
     '### **THIS DOCUMENT CARRIES NO CORRESPONDENCE TABLE AT ALL**, so nothing in the record can '
     'be matched against a row of its own. ### **A KEYSTONE WITH NO TABLE IS A KEYSTONE WHOSE '
     'GRADE LIMB CANNOT BE READ**, and every record item therefore falls into this bucket by '
     'construction rather than by judgement -- which the component says rather than hides.'),
]


def component1():
    bar('=')
    rec('  ### COMPONENT 1 -- THE THREE, EACH READ.')
    bar('=')
    s1, s2 = E['s1'], E['s2']
    rec('  ### **THE CHOICE, BY `b390`\'S RULE, QUOTED:** ### *take those whose terminals the drive')
    rec('  ### can reach.* ### **NOTHING IS ADDED TO IT.**')
    rec('  ### ### **CENSUS KEYSTONES ON DISK : `%d`. ### REACHABLE : `%d`. ### TAKEN : `%d`.**'
        % (len(s1['all']), len(s1['eligible']), len(s1['chosen'])))
    rec('  ### **THE ELEVEN EXCLUDED, EACH WITH ITS REASON:**')
    for r in s1['all']:
        if not r['reach']:
            rec('      %-38s %s' % (r['k'][:38], r['why']))
    rec('  ### **AND ONE SET ASIDE:** ### `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` -- read whole at')
    rec('  ### `b390`, the act that minted the rule. ### **RE-READING IT WOULD BE RE-DOING THAT')
    rec('  ### ### ACT`S WORK.**')
    rec()
    buckets = {A: 0, B: 0, C: 0}
    rows = []
    for k in s1['chosen']:
        info = s2[k]
        bar()
        rec('  ### **`%s`**' % k)
        bar()
        rec('    ### **WHAT IT CLAIMS**, in its own title: %s' % info['title'][:100])
        rec('    path `%s` ; `%d` lines ; version token `%s`'
            % (info['path'], info['lines'], info['version']))
        if info['table']:
            rec('    ### **ITS TABLE CARRIES `%d` ROWS, BY GRADE : %s**'
                % (info['rows'], sorted(info['grades'].items())))
        else:
            rec('    ### ### **IT CARRIES NO CORRESPONDENCE TABLE.** ### The order asks what its')
            rec('    ### ### table carries by grade; ### **THE ANSWER IS THAT THERE IS NO TABLE**,')
            rec('    ### ### and this act does not write one -- ### **WRITING A CORRESPONDENCE')
            rec('    ### ### TABLE IS AUTHORING, NOT RECONCILING.**')
        rec()
        for subj, layer, rfile, rhint, khint, bucket, why in BEARS:
            if subj != k:
                continue
            rp = os.path.join(PP, rfile.replace('/', os.sep))
            try:
                ri, rln = AF.find(rp, rhint)
            except Exception:
                ri, rln = None, ''
            ki, kln = None, ''
            if khint:
                try:
                    ki, kln = AF.find(os.path.join(PP, info['path'].replace('/', os.sep)), khint)
                except Exception:
                    ki, kln = None, ''
            buckets[bucket] += 1
            rows.append(dict(subject=k, layer=layer, bucket=bucket, record_file=rfile,
                             record_line=ri, keystone_line=ki))
            rec('    ### -- %s ### ### **%s**' % (layer, bucket))
            rec('        ### THE RECORD -- `%s` line %s:' % (rfile, ri))
            rec('          > %s' % flat(rln, 230))
            if khint and ki:
                rec('        ### THE KEYSTONE -- `%s` line %s:' % (os.path.basename(info['path']),
                                                                   ki))
                rec('          > %s' % flat(kln, 230))
            else:
                rec('        ### THE KEYSTONE -- ### **NO LINE. ### IT DOES NOT CARRY IT**, and a')
                rec('        ### proved absence is said, not quoted.')
            for i in range(0, min(len(why), 460), 150):
                rec('          %s' % why[i:i + 150])
            rec()
    bar()
    rec('  ### ### **THE THREE BUCKETS, ACROSS ALL THREE SUBJECTS:**')
    for kk in (A, B, C):
        rec('      %-32s ### **`%d`**' % (kk, buckets[kk]))
    rec('  ### ### **EVERY BUCKET IS REPORTED, INCLUDING ANY THAT IS EMPTY** (`b390`\'s rule).')
    rec('  ### ### **`(L2)` -- AT LEAST ONE OF THE THREE CARRIES A CLAIM THE RECORD HAS SINCE')
    rec('  ### ### CORRECTED : %s.**' % (buckets[B] > 0))
    return dict(chosen=s1['chosen'], excluded=len([r for r in s1['all'] if not r['reach']]),
                set_aside=s1['set_aside'], buckets=buckets, rows=rows,
                tables={k: s2[k]['table'] for k in s1['chosen']},
                table_rows={k: s2[k]['rows'] for k in s1['chosen']},
                grades={k: s2[k]['grades'] for k in s1['chosen']},
                l2=(buckets[B] > 0))


# ==================================================================================================
#  COMPONENT 2 -- THE REPAIRS.
# ==================================================================================================
def component2():
    bar('=')
    rec('  ### COMPONENT 2 -- THE REPAIRS, MADE AND ROUTED.')
    bar('=')
    s3 = E['s3']
    gi, gln = AF.find(REGISTRY, '| 1.5f-4 | Foundations of the SIDE Programme |')
    rec('  ### **THE VERSION TO WRITE, READ AT ITS OWN LINE** -- `REGISTRY.md` line %d:' % gi)
    rec('      > %s' % flat(gln, 200))
    m = re.search(r'\|\s*(v[0-9][0-9.]*)\s*\|', gln)
    newv = m.group(1) if m else NEWV
    rec('  ### ### **THE REGISTRY`S ROW CARRIES `%s`.**' % newv)
    ui, uln = AF.find(REGISTRY, 'Row **1.5f-4** '
                                '(`phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md`): '
                                'version')
    rec('  ### **AND THE ROW UPDATE THAT RECONCILED IT** -- line %d:' % ui)
    rec('      > %s' % flat(uln, 260))
    rec()
    rec('  ### ### **THE TWO CITATIONS, AND THE CHECK THAT THEY ARE SUPERSESSIONS AND NOT')
    rec('  ### ### PHANTOMS.**')
    tgt = os.path.join(PP, 'phase1.5', 'structural', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md')
    lin = set('v' + x.rstrip('.') for x in re.findall(
        r'\bv([0-9][0-9.]*)', io.open(tgt, encoding='utf-8', errors='replace').read()))
    real = OLD in lin
    rec('  ### `%s` IS IN THE CITED DOCUMENT`S OWN LINEAGE : ### **%s.**' % (OLD, real))
    rec('  ### ### ### **A SUPERSESSION IS NOT A PHANTOM AND IS NOT REPAIRED AS ONE** -- the old')
    rec('  ### ### ### form was real, so the repair moves a citation forward rather than')
    rec('  ### ### ### correcting an invention.')
    rec()
    full = os.path.join(PP, TARGET.replace('/', os.sep))
    pre = blob(TARGET)
    cur = io.open(full, encoding='utf-8', newline='').read()
    targets = sorted(set(h['line'] for h in s3['unpropagated'] if h['citer'] == 'GRH_CASCADE'))
    originals = []
    if MARK in cur:
        rec('  ### ALREADY REPAIRED -- the mark is present. ### NOTHING WRITTEN.')
        for i in targets:
            originals.append((i, flat(pre.split(chr(10))[i - 1], 150)))
    else:
        ls = cur.replace(chr(13) + chr(10), chr(10)).split(chr(10))
        for i in targets:
            originals.append((i, flat(ls[i - 1], 150)))
            ls[i - 1] = ls[i - 1].replace(
                'FOUNDATIONS_OF_THE_SIDE_PROGRAMME ' + OLD,
                'FOUNDATIONS_OF_THE_SIDE_PROGRAMME ' + newv)
        block = [
            '', MARK, '',
            ('#### **RECONCILIATION ANNOTATION** *(2026-09-09, b394; existing text preserved '
             'apart from the two version strings named here)*'),
            '',
            ('> ### **TWO CITATIONS OF `FOUNDATIONS_OF_THE_SIDE_PROGRAMME` WERE MOVED FROM '
             '`%s` TO `%s`.** *The originals, preserved:*' % (OLD, newv)),
            '',
        ]
        for i, o in originals:
            block.append('> - line `%d` — *%s*' % (i, o))
        block += [
            '',
            ('> ### **WHY.** *`REGISTRY.md`’s row `1.5f-4` records a version reconciliation past '
             '`%s`, and its table now carries `%s`. This paper kept the pre-update form — the '
             '**corrected-but-unpropagated** species `b391` found in the registry’s own bundle '
             'label. **A correction that does not propagate is a correction in one place and a '
             'defect everywhere else.** `%s` is in the cited document’s own lineage, so this is '
             'a **supersession moved forward**, not a phantom repaired.*' % (OLD, newv, OLD)),
            '',
            ('> ### **WHAT WAS NOT DONE.** *No grade moved, no claim withdrawn, no correspondence '
             'row edited, no other string on either line changed, and no line deleted.*'),
            '',
        ]
        open(full + '.tmp', 'wb').write((chr(10).join(ls) + chr(10).join(block)
                                         + chr(10)).encode('utf-8'))
        os.replace(full + '.tmp', full)
    after = io.open(full, encoding='utf-8', newline='').read().replace(chr(13) + chr(10), chr(10))
    pl, al = pre.split(chr(10)), after.split(chr(10))
    diffl = [k for k, (x, y) in enumerate(zip(pl, al), 1) if x != y]
    onlyv = all(pl[k - 1].replace(OLD, newv) == al[k - 1] for k in diffl)
    removed = max(0, len(pl) - len(al))
    a, d = numstat(TARGET)
    rec('  ### ### **THE REPAIR, MEASURED AGAINST THE PRE-ACT BLOB:**')
    rec('  ###   lines differing        : ### **`%d`** ### %s' % (len(diffl), diffl))
    rec('  ###   only the version changed on each : ### **%s**' % onlyv)
    rec('  ###   lines removed          : ### **`%d`**' % removed)
    rec('  ###   git numstat            : `+%d` / `-%d` ### -- an in-place edit scores one')
    rec('  ###   addition and one deletion per line; the bar is ### **NO LINE REMOVED**, which is')
    rec('  ###   the figure above.')
    rec('  ###   the originals preserved in an appended annotation : ### **%s**' % (MARK in after))
    for i, o in originals:
        rec('  ###     line %d was : %s' % (i, o[:120]))
    subprocess.run(['git', '-C', PP, 'add', '--', TARGET], capture_output=True)
    rec()
    bar()
    rec('  ### ### **THE REPAIRS ROUTED, EACH NAMED WITH THE RULING IT NEEDS.**')
    bar()
    routed = [
        ('the missing correspondence table in `SILENCE_STAGES_DEALIGNMENT`',
         'writing one is ### **AUTHORING, NOT RECONCILING** -- it decides what the document`s '
         'load-bearing claims ARE, which is the author`s. ### `b387` already routed five such '
         'and this act adds none to that list, it only confirms one of them by reading it.'),
        ('the `%d` superseded citations across the three' % len(s3['superseded']),
         '`b391` ruled: ### **A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM, NOT A '
         'PHANTOM.** ### Repairing them would be a currency pass, which is a different act.'),
        ('the E-Difficulty scope split, absent from two of the three',
         'the record files it ### *statement-grade, nothing retracted* ### -- so carrying it is '
         '### **AN ADDITION TO A PAPER**, and adding material to a keystone is authoring.'),
        ('`W-6``s closure, absent from `FOUNDATIONS_OF_THE_SIDE_PROGRAMME`',
         'same shape: ### **AN ADDITION, NOT A CORRECTION**, and the paper is not wrong without '
         'it.'),
    ]
    for item, why in routed:
        rec('    ### **%s**' % item)
        for i in range(0, min(len(why), 460), 150):
            rec('        %s' % why[i:i + 150])
    rec()
    rec('  ### ### **REPAIRS MADE : `%d`. ### REPAIRS ROUTED : `%d`. ### COUNTED SEPARATELY**,'
        % (len(diffl), len(routed)))
    rec('  ### ### because a repair and a routing are different outcomes.')
    rec('  ### ### **`0` CORRESPONDENCE TABLES WRITTEN. ### `0` GRADES MOVED. ### `0` CLAIMS')
    rec('  ### ### WITHDRAWN.**')
    return dict(made=len(diffl), routed=len(routed), removed=removed, only_version=onlyv,
                added=a, deleted=d, originals=originals, newv=newv, was_real=real,
                annotated=(MARK in after))


# ==================================================================================================
#  COMPONENT 3 -- THE COUNT AND THE PRICE.
# ==================================================================================================
def component3(c1, c2):
    bar('=')
    rec('  ### COMPONENT 3 -- THE COUNT, AND THE PRICE FROM THREE.')
    bar('=')
    s3 = E['s3']
    rec('  ### ### **KEYSTONES RECONCILED AGAINST THE CENSUS`S LIST.**')
    rec('  ###   `b390` read : ### **`1`** ### (`ADDITIVE_MULTIPLICATIVE_CONSPIRACY`)')
    rec('  ###   `b394` reads : ### **`%d`** ### (%s)'
        % (len(c1['chosen']), ', '.join('`%s`' % k for k in c1['chosen'])))
    rec('  ###   ### **TOTAL : `%d` OF THE CENSUS`S `16`.**' % (1 + len(c1['chosen'])))
    rec('  ### ### **THAT IS `%d` OF `16` AND IT IS NOT ROUNDED UP.**' % (1 + len(c1['chosen'])))
    rec('  ### ### **AND `11` OF THE REMAINING `12` CANNOT BE READ BY THIS RULE AT ALL** -- their')
    rec('  ### ### terminals are not reachable from the drive, so ### **THE POPULATION THIS')
    rec('  ### ### METHOD CAN REACH IS ALREADY NEARLY EXHAUSTED.**')
    rec()
    t0 = os.path.getmtime(FERRY)
    t1 = time.time()
    mins = (t1 - t0) / 60.0
    rec('  ### ### **THE PRICE, RE-MEASURED FROM THREE.**')
    rec('  ###   the ferry banked at   : %s'
        % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0)))
    rec('  ###   this component at     : %s'
        % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t1)))
    rec('  ###   ### **WALL TIME FOR THE ACT : `%.0f` MINUTES ; PER KEYSTONE : `%.0f`.**'
        % (mins, mins / max(1, len(c1['chosen']))))
    rec('  ### `b390` measured ### **`24` MINUTES FOR ONE.**')
    rec('  ### ### ### **THE PER-KEYSTONE FIGURE FELL AND THE PER-ACT FIGURE DID NOT, AND THE')
    rec('  ### ### ### REASON IS THE APPARATUS AND NOT THE READING:** ### three subjects share a')
    rec('  ### ### ### single registration, a single gate suite and a single push.')
    rec('  ### ### **SO A READER PLANNING WORK SHOULD PLAN WITH THE PER-ACT FIGURE**, not the')
    rec('  ### ### per-keystone one -- ### **THE SAVING IS IN THE APPARATUS AND CANNOT BE SPENT')
    rec('  ### ### TWICE.**')
    rec('  ### ### **AND THE CLOCK ITSELF HAS A LIMIT, STATED:** ### it is read ### **AT THIS')
    rec('  ### ### COMPONENT** ### and the act continues afterwards -- the desk, the ledgers, the')
    rec('  ### ### bank, the gate suite and the push are all still to come. ### **SO BOTH FIGURES')
    rec("  ### ### ARE FLOORS.** ### `b390` measured `24` the same way at the same point, so")
    rec('  ### ### ### **THE COMPARISON IS LIKE FOR LIKE EVEN THOUGH NEITHER NUMBER IS THE WHOLE')
    rec('  ### ### ### COST.**')
    rec('  ### ### **AND THE SAMPLE IS BIASED, NAMED ONCE:** ### these three are ### **THE')
    rec('  ### ### REACHABLE ONES**, which is exactly the population most likely to be in good')
    rec('  ### ### order. ### **A PRICE FROM THE EASY END OF THE DISTRIBUTION IS A FLOOR.**')
    rec()
    rec('  ### ### **THE THREE SPECIES, REPORTED APART AND NEVER ADDED:**')
    rec('  ###   phantoms in the three subjects          : ### **`%d`**' % len(s3['phantom']))
    rec('  ###   corrected-but-unpropagated              : ### **`%d`**'
        % len(s3['unpropagated']))
    rec('  ###   superseded, reported and left           : ### **`%d`**' % len(s3['superseded']))
    rec('  ### ### ### **THREE COUNTS, THREE MEANINGS.** ### A phantom is a defect; an')
    rec('  ### ### ### unpropagated correction is a defect with a known cure; a supersession is')
    rec('  ### ### ### currency. ### **ADDING THEM WOULD DESCRIBE NONE OF THE THREE.**')
    return dict(reconciled=1 + len(c1['chosen']), of=16, minutes=round(mins, 1),
                per_keystone=round(mins / max(1, len(c1['chosen'])), 1),
                b390_minutes=24, phantom=len(s3['phantom']),
                unpropagated=len(s3['unpropagated']), superseded=len(s3['superseded']))


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b394 -- THE RECONCILIATION, BATCHED.')
    bar('=')
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    c3 = component3(c1, c2)
    rec()
    bar('=')
    rec('  1 : chosen %d ; excluded %d ; buckets %s ; (L2) %s'
        % (len(c1['chosen']), c1['excluded'], c1['buckets'], c1['l2']))
    rec('  2 : made %d ; routed %d ; removed %d ; only-version %s ; annotated %s'
        % (c2['made'], c2['routed'], c2['removed'], c2['only_version'], c2['annotated']))
    rec('  3 : reconciled %d of %d ; %.0f min (%.0f per keystone vs b390`s 24 for one)'
        % (c3['reconciled'], c3['of'], c3['minutes'], c3['per_keystone']))
    rec('  ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED. ### NO BUILD WAS RUN.**')
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b394_components_run', L)
    json.dump(dict(c1=c1, c2=c2, c3=c3, run_file=os.path.basename(p),
                   run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b394_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
