# -*- coding: utf-8 -*-
"""b448_r61_trigger.py -- RULING (R61) EXECUTED: THE FAILURE-MODE PARTITION GETS A TRIGGER, NOT A SHELF.

### One record appended to `PLACE-papers/OPEN_TRAILS.md`, after b448's mark, the prior text proved a true prefix.
### Every count beside the trigger is read from the six candidate banks, never typed. `FINDINGS.md` is not edited.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
RUN = os.path.join(D, 'b448_r61_trigger_run.txt')
MARK = '<!-- (R61) the failure-mode partition gets a trigger, not a shelf -->'
PRIOR = '<!-- b448 the partition read against the taxonomy, and the outlier`s free candidate -->'
SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def line_of(path, needle):
    for i, l in enumerate(io.open(path, encoding='utf-8-sig', errors='replace').read().splitlines()):
        if needle in l:
            return i + 1
    return None


def main():
    out = []
    per, tot, cb, imp, held = [], 0, 0, 0, 0
    for s, p in SITES:
        d = json.load(io.open(os.path.join(D, p), encoding='utf-8'))
        cs = d['candidates']
        n = len(cs)
        c = sum(1 for x in cs if x['kind'] == 'CLASS BOUNDARY')
        im = sum(1 for x in cs if x['kind'] == 'IMPORT UNDER THE BAR')
        h = d.get('held')
        held += (len(h) if isinstance(h, list) else int(h or 0))
        per.append((s, c, n))
        tot, cb, imp = tot + n, cb + c, imp + im
    maj = [s for s, c, n in per if 2 * c > n]
    kinds = len(set(x['kind'] for s, p in SITES for x in json.load(io.open(os.path.join(D, p), encoding='utf-8'))['candidates']))
    fnd = os.path.join(PP, 'FINDINGS.md')
    l_part = line_of(fnd, '| **The failure-mode partition** | **NAMED HERE AS A RESEARCH PROPOSAL AND NOT OPENED**')
    l_r23 = line_of(TRAILS, '**RULING (R23), THE AUTHOR’S, RATIFIED BY THE FERRY AND STRIKEABLE: AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS SHELVED.**')
    out.append('counts read from the banks: candidates %d ; held %d ; kinds %d ; class boundary %d ; import under the bar %d'
               % (tot, held, kinds, cb, imp))
    out.append('class boundary per site: %s ; a majority at %d of 6 sites %s' % (['(%s) %d/%d' % x for x in per], len(maj), maj))
    out.append('anchors: FINDINGS.md:%s (the partition) ; OPEN_TRAILS.md:%s ((R23))' % (l_part, l_r23))
    if not (l_part and l_r23) or tot != 82 or kinds != 11:
        out.append('### REFUSED -- an anchor or a banked count is not what b448 read; nothing appended.')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(out) + NL)
        print(NL.join(out))
        return 1
    block = [
        '', MARK, '',
        '### (R61) — the failure-mode partition gets a trigger, not a shelf — filed 2026-09-13',
        '',
        '**RULING (R61), THE AUTHOR’S, RATIFIED AND STRIKEABLE: THE FAILURE-MODE PARTITION GETS A TRIGGER, NOT A SHELF.** '
        'b448 read the partition (`FINDINGS.md:%d`, named at b348, UNDECIDED at b351) as RELATED to the witness arc’s taxonomy: '
        'the arc gave it vocabulary and not its answer. Under `(R23)` (`OPEN_TRAILS.md:%d`) an item with no trigger is shelved; '
        'this item is the record’s only one aimed at the quantifier, so by the author’s ruling it is not shelved by default.' % (l_part, l_r23),
        '',
        '**Trigger: a source enters the record under the import bar that ranges over a class containing the corpus’s own objects. '
        'Also fires on the author’s word.**',
        '',
        '**What the trigger is waiting for, in the arc’s own count** (read from the six candidate banks, b424 to b443r): '
        '**%d** candidates over six sites, **%d** held, **%d** failure kinds. The class boundary — a source whose class does not '
        'contain the corpus’s objects — is the largest kind, **%d of %d**, a majority overall and at **%d of 6** sites '
        '(%s); it is not the majority at %s. A further **%d** failed as imports under the bar. So no site had a source that both '
        'passed the bar and ranged over a class containing the corpus’s objects; that pairing is what this trigger names.'
        % (tot, held, kinds, cb, tot, len(maj), ', '.join('(%s) %d of %d' % x for x in per),
           ' and '.join('(%s)' % s for s, c, n in per if s not in maj), imp),
        '',
        '*The partition row in `FINDINGS.md` is not edited; this record carries its trigger. No bridge is typed; row `U1`’s '
        'refusal governs. No grade moved; nothing claimed about `h2`.*',
        '',
    ]
    t = io.open(TRAILS, 'rb').read().decode('utf-8')
    if MARK in t:
        out.append('already present; not re-appended')
    elif PRIOR not in t:
        out.append('### REFUSED -- b448`s mark is absent; nothing appended.')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(out) + NL)
        print(NL.join(out))
        return 1
    else:
        t2 = t.rstrip(NL) + NL + NL.join(block) + NL
        open(TRAILS + '.tmp', 'wb').write(t2.encode('utf-8'))
        os.replace(TRAILS + '.tmp', TRAILS)
        back = io.open(TRAILS, 'rb').read().decode('utf-8')
        out.append('appended %d lines ; prior text a TRUE PREFIX : %s ; mark count %d'
                   % (len(back.splitlines()) - len(t.splitlines()), back.startswith(t.rstrip(NL)), back.count(MARK)))
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(out) + NL)
    print(NL.join(out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
