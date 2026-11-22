# -*- coding: utf-8 -*-
"""tools/b766_sweep.py -- b766, (R376)(5)(c): THE FINDINGS LEDGER AGAINST THE KEYSTONES, THE TOOL'S PASS.

Written by the Write tool at b766's Component 3 and committed before its first run, dry included ((R376)(5)(c), N2).

  dry      prints the bank's text; writes nothing
  write    data/b766_sweep.txt and .json

THE READER, carried: tools/b761_sitting.py imported as committed, its rules unedited (its docstring :10-:24): each entry of FINDINGS.md
above :14027 (a heading `## ` that is no corrigendum, the form of linematch.entry_heading), its names as tools/standing/linematch.py
reads them from the heading, its cluster by rules R1-R4 against SPIRAL_MAP's cluster table and REGISTRY's rows at PLACE-papers HEAD
(b761's place()), the keystone the row names (b761's cluster_table()), and whether that keystone carries a name of it (b761's carried(),
read here over each keystone's lines read once, its control printed: equal to b761's own at each pair of a sample); the reading as b761
gives it: SYNTHESISED, CLUSTERED (an input of that keystone's re-cut), CLUSTERED (no keystone named), BANKED, NO SEAT; an entry placed in
several clusters takes the highest reading. Only the population moves: the entries above :14027 in place of b745's to b760's.
THE BANK: for each keystone, the entries it carries and the entries of its cluster it does not (an entry placed in several clusters stands
under each); the entries with no keystone; THE SIZES, the entries whose heading carries no name of the reader's form, counted by cluster
with their lines (an entry's lines from its heading to the next heading of the ledger, or to :14026), which is the reading a later act
delegates. Each entry by its line and its heading's sha256; no line of a paper printed or stored but the names, the cluster's label and
the keystone's path; the protected word neither printed nor stored; no stage line written into an entry ((R376)(5)(c)); no git write.
"""
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b761_sitting as S61   # noqa: E402  ### the reader, its rules unedited
import b761_registry as RG   # noqa: E402
import linematch as LM       # noqa: E402

ACT, NL = 'b766', '\n'
BOUND = 14027                # ### (R376)(5)(c): the entries that stand above FINDINGS :14027
BANK = os.path.join(D, 'b766_sweep.txt')
BJSON = os.path.join(D, 'b766_sweep.json')
EPS = 'THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'
SYN = 'SYNTHESISED'
NOKEY = ('BANKED, NO SEAT', 'CLUSTERED, NO KEYSTONE NAMED')


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def lines_of(ks, cap=60):
    ks = sorted(set(ks))
    return (', '.join(':%d' % k for k in ks[:cap]) + (' and %d more' % (len(ks) - cap) if len(ks) > cap else '')) or '-'


def run(mode):
    F, S, R = S61.show('FINDINGS.md'), S61.show('SPIRAL_MAP.md'), S61.show('REGISTRY.md')
    I = RG.ids()
    qw = RG.qword(R)
    host = os.path.basename(os.path.dirname(S61.PP))   # ### PLACE-papers' parent folder, from b761's constant: read, never printed
    head = subprocess.run(['git', '-C', S61.PP, 'rev-parse', '--short=8', 'HEAD'], capture_output=True).stdout.decode().strip()
    rhead = subprocess.run(['git', '-C', RELAY, 'rev-parse', '--short=8', 'HEAD'], capture_output=True).stdout.decode().strip()
    allh = [k for k in range(1, len(F) + 1) if F[k - 1].startswith('## ')]
    hs = [k for k in allh if k < BOUND and not F[k - 1].startswith('## Corrigendum')]
    ncorr = sum(1 for k in allh if k < BOUND and F[k - 1].startswith('## Corrigendum'))

    def span(h):
        return min([k for k in allh if k > h] + [BOUND]) - h

    ct = S61.cluster_table(S)
    rr = S61.reg_rows(R)
    ktexts, kcache = {}, {}
    for row in ct:
        for kp in row['keys']:
            if kp not in ktexts:
                KL = S61.show(kp)
                ktexts[kp] = (KL, LM.names(NL.join(KL)))
                kcache[kp] = [set(LM.names(l)) for l in KL]

    def carried(name, kp):
        # ### b761's carried() (tools/b761_sitting.py :261-:267), its names per line read once for each keystone
        KL = ktexts[kp][0]
        if name not in ktexts[kp][1]:
            return [], False
        at = [k for k, s in enumerate(kcache[kp], 1) if name in s]
        occ = r'(?<![\w`.-])`?' + re.escape(name) + r'`?(?![\w-])'
        pth = r'/' + re.escape(name) + r'\.[a-z]'
        path = bool(at) and all(len(re.findall(pth, KL[k - 1])) == len(re.findall(occ, KL[k - 1])) for k in at)
        return at, path

    def item(h, hd, sp):
        nm = LM.names(hd)
        reads = []
        for row, why in S61.place(hd, ct, rr, ktexts):
            keys = row['keys']
            per = [(kp, [(x,) + carried(x, kp) for x in nm]) for kp in keys]
            hit = [(kp, x, at, p) for kp, rows in per for x, at, p in rows if at]
            rd = 'CLUSTERED, NO KEYSTONE NAMED' if not keys else (SYN if hit else 'CLUSTERED, AN INPUT OF THAT KEYSTONE`S RE-CUT')
            reads.append(dict(cluster=row['name'], row=row['line'], why=why, keys=keys, reading=rd,
                              carriers=sorted(set(kp for kp, _x, _a, _p in hit)), path_only=bool(hit) and all(p for _k, _x, _a, p in hit)))
        r0 = sorted(reads, key=lambda r: 0 if r['reading'] == SYN else 1)[0] if reads else None
        return dict(line=h, sha=S61.sha(hd), names=nm, span=sp, reads=reads, reading=r0['reading'] if r0 else 'BANKED, NO SEAT',
                    cluster=r0['cluster'] if r0 else None, crow=r0['row'] if r0 else None, keys=r0['keys'] if r0 else [],
                    carriers=r0['carriers'] if r0 else [], path_only=r0['path_only'] if r0 else False, several=len(reads) > 1)

    items = [item(h, F[h - 1], span(h)) for h in hs]
    # ### the counts of [X3], each entry once by its highest reading
    named = [i for i in items if i['names']]
    nameless = [i for i in items if not i['names']]
    n_car = sum(1 for i in named if i['reading'] == SYN)
    n_nokey = sum(1 for i in items if i['reading'] in NOKEY)
    l_nameless = sum(i['span'] for i in nameless)
    # ### by keystone, an entry under each cluster that places it
    perk = {}
    for row in ct:
        for kp in row['keys']:
            perk.setdefault(kp, dict(clusters=[], carried=[], not_carried=[]))
            if row['name'] not in perk[kp]['clusters']:
                perk[kp]['clusters'].append(row['name'])
    for i in items:
        for r in i['reads']:
            for kp in r['keys']:
                d = perk[kp]['carried'] if kp in r['carriers'] else perk[kp]['not_carried']
                if i['line'] not in d:
                    d.append(i['line'])
    # ### the sizes: the nameless entries by cluster
    sizes = {}
    for i in nameless:
        c = i['cluster'] or '(no seat in the cluster table)'
        s = sizes.setdefault(c, dict(entries=[], lines=0))
        s['entries'].append(i['line'])
        s['lines'] += i['span']
    nk = {}
    for i in items:
        if i['reading'] in NOKEY:
            nk.setdefault(i['reading'], []).append(i['line'])
    sentence = ('of %d entries above FINDINGS :%d, %d carry a name the reader takes, %d of them carried by a keystone and %d not; %d have no '
                'keystone; %d entries of %d lines carry no such name and wait on a reader (relay data/b766_sweep.txt); no stage line written'
                % (len(items), BOUND, len(named), n_car, len(named) - n_car, n_nokey, len(nameless), l_nameless))
    # ### the controls
    eps = [k for k in ktexts if k.endswith(EPS)]
    sample = [(x, kp) for i in named[:60] for x in i['names'] for kp in ktexts]
    same = all(carried(x, kp) == S61.carried(x, ktexts[kp][0]) for x, kp in sample)
    pl_syn = item(0, '## planted pc_online read', 1)
    pl_none = item(0, '## A PLANTED HEADING OF NO NAME', 1)
    ctl = [('the population: the headings of FINDINGS above :%d that are no corrigendum, %d (corrigenda %d set apart), the first at :%s and the last at :%s, '
            'the heading at :%d read as the first beyond' % (BOUND, len(hs), ncorr, hs[0] if hs else '-', hs[-1] if hs else '-', BOUND),
            bool(hs) and max(hs) < BOUND and F[BOUND - 1].startswith('## ') and not F[BOUND - 1].startswith('## Corrigendum')),
           ('the cluster table read (SPIRAL_MAP :%d-:%d): rows %d (at least 9), the Epstein instance`s keystone read at HEAD' % (S61.CT_HEAD, S61.CT_LAST, len(ct)),
            len(ct) >= 9 and bool(eps)),
           ('the match`s positive control: pc_online read carried by the Epstein keystone, a planted name b999_planted not',
            any(carried('pc_online', k)[0] for k in eps) and not any(carried('b999_planted', k)[0] for k in ktexts)),
           ('the carried test read once per keystone equal to b761`s own at each of %d pairs (name, keystone) of the first 60 entries with names' % len(sample),
            same and len(sample) > 0),
           ('the placement`s planted control (b761`s): a heading naming nothing of the maps (b999_planted_bank) placed nowhere',
            not S61.place('## b999_planted_bank read', ct, rr, ktexts)),
           ('a planted entry naming pc_online read %s by %s; a planted heading with no name read with names %s, counted among the sizes` form' % (
               pl_syn['reading'], ', '.join(pl_syn['carriers']) or 'none', pl_none['names'] or 'none'),
            pl_syn['reading'] == SYN and any(k.endswith(EPS) for k in pl_syn['carriers']) and not pl_none['names']),
           ('the sums: carried + not = with names (%d + %d = %d); with names + without = entries (%d + %d = %d); the sizes by cluster %d entries and %d lines' % (
               n_car, len(named) - n_car, len(named), len(named), len(nameless), len(items), sum(len(s['entries']) for s in sizes.values()),
               sum(s['lines'] for s in sizes.values())),
            len(named) + len(nameless) == len(items) and sum(len(s['entries']) for s in sizes.values()) == len(nameless)
            and sum(s['lines'] for s in sizes.values()) == l_nameless)]
    # ### the bank
    P = ['%s -- (R376)(5)(c): THE FINDINGS LEDGER AGAINST THE KEYSTONES, THE TOOL`S PASS (%s)' % (ACT, utc()), '',
         '### tools/b766_sweep.py %s; the relay HEAD %s; PLACE-papers HEAD %s; FINDINGS, SPIRAL_MAP`s cluster table (:%d-:%d), REGISTRY and the keystones read at HEAD;' % (
             mode, rhead, head, S61.CT_HEAD, S61.CT_LAST),
         '### the reader of tools/b761_sitting.py imported as committed, its rules R1-R4, its keystones and its carried test unedited (its docstring :10-:24),',
         '### run over the entries above FINDINGS :%d; each entry by its heading`s line and sha256, no line of a paper quoted; the names as' % BOUND,
         '### tools/standing/linematch.py reads them from the heading; no stage line written into an entry, no line of FINDINGS written ((R376)(5)(c)).', '',
         '## THE POPULATION: %d entries above :%d (corrigenda %d set apart), from :%s to :%s; their lines %d' % (
             len(items), BOUND, ncorr, hs[0] if hs else '-', hs[-1] if hs else '-', sum(i['span'] for i in items)),
         '## THE CLUSTER TABLE: rows %d; the keystones it names read: %s' % (
             len(ct), ', '.join('%s (%d lines, %d names)' % (k, len(v[0]), len(v[1])) for k, v in ktexts.items()) or 'none'), '',
         '## THE COUNTS, EACH ENTRY ONCE BY ITS HIGHEST READING: ENTRIES %d ; WITH A NAME THE READER TAKES %d, CARRIED BY A KEYSTONE %d, NOT %d ; '
         'NO KEYSTONE %d ; WITH NO SUCH NAME %d, OF %d LINES' % (len(items), len(named), n_car, len(named) - n_car, n_nokey, len(nameless), l_nameless),
         '  the readings: %s' % ' ; '.join('%s %d' % (r, sum(1 for i in items if i['reading'] == r)) for r in dict.fromkeys(i['reading'] for i in items)),
         '  placed in more than one cluster: %d' % sum(1 for i in items if i['several']), '',
         '## BY KEYSTONE (an entry placed in several clusters stands under each): keystone | its clusters | carried | of its cluster, not carried']
    for kp, d in perk.items():
        P.append('  %s | %s | %d | %d' % (kp, '; '.join(d['clusters']), len(d['carried']), len(d['not_carried'])))
        P.append('      carried: %s' % lines_of(d['carried']))
        P.append('      not carried: %s' % lines_of(d['not_carried']))
    P += ['', '## THE ENTRIES WITH NO KEYSTONE: %d' % n_nokey]
    for r, ks in nk.items():
        P.append('  %s %d: %s' % (r, len(ks), lines_of(ks)))
    P += ['', '## THE SIZES: THE ENTRIES WHOSE HEADING CARRIES NO NAME OF THE READER`S FORM, BY CLUSTER (entries | lines), THE READING A LATER ACT DELEGATES']
    for c, s in sorted(sizes.items(), key=lambda kv: -kv[1]['lines']):
        P.append('  %-60s %5d | %6d' % (c, len(s['entries']), s['lines']))
        P.append('      at %s' % lines_of(s['entries']))
    P += ['', '## THE ENTRIES (FINDINGS :line | sha256 | names | reading | cluster | keystone)']
    for i in items:
        P.append('  :%d | %s | %s | %s | %s | %s%s' % (i['line'], i['sha'], ', '.join(i['names']) or '-', i['reading'], i['cluster'] or '-',
                                                       ', '.join(i['carriers'] if i['reading'] == SYN else i['keys']) or '-',
                                                       ' (a relay path alone)' if i['path_only'] else ''))
    P.append('')
    text = NL.join(P)
    ctl.append(('the identifiers, the protected word, a profile path and the host folder 0 in the bank',
                RG.idcount(text, I) == 0 and qw.lower() not in text.lower() and 'users/' not in text.lower().replace('\\', '/')
                and (not host or host.lower() not in text.lower())))
    ok = all(o for _w, o in ctl)
    P.append('## THE CONTROLS')
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## [X3]`S FIELDS: %s' % sentence, '',
          '### ### **THE LEDGER AGAINST THE KEYSTONES: ENTRIES %d ; WITH A NAME %d (CARRIED %d, NOT %d) ; NO KEYSTONE %d ; NO SUCH NAME %d OF %d LINES ; '
          'CONTROLS %d OF %d AS WANTED ; %s.**' % (len(items), len(named), n_car, len(named) - n_car, n_nokey, len(nameless), l_nameless,
                                                   sum(1 for _w, o in ctl if o), len(ctl),
                                                   ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD, NOTHING WRITTEN')]
    final = NL.join(P) + NL
    if RG.idcount(final, I) or qw.lower() in final.lower():
        die('AN IDENTIFIER OR THE PROTECTED WORD IN THE PRINT')
    print(final, end='')
    if mode != 'write' or not ok:
        return 0 if ok else 1
    JS = dict(at=utc(), act=ACT, relay_head=rhead, pp_head=head, bound=BOUND, entries=len(items), named=len(named), carried=n_car,
              not_carried=len(named) - n_car, no_keystone=n_nokey, nameless=len(nameless), nameless_lines=l_nameless, sentence=sentence,
              by_keystone=perk, no_keystone_lines=nk, sizes=sizes,
              items=[dict((k, v) for k, v in i.items() if k != 'reads') for i in items], controls=[[w, o] for w, o in ctl])
    S61.put(BANK, final)
    S61.put(BJSON, json.dumps(JS, ensure_ascii=False, indent=1) + NL)
    print('written data/b766_sweep.txt (%d lines) and .json' % len(final.split(NL)))
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] not in (['dry'], ['write']):
        sys.exit(__doc__)
    sys.exit(run(a[0]))
