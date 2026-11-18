# -*- coding: utf-8 -*-
"""tools/b761_lines.py -- b761, (R371)(6): THE INTEGRATION LINES IN THE CANON'S FORM, b755 TO b760 AND THIS ACT'S OWN, in the form of
tools/b754_line.py. Written by the Write tool at b761's Component 5 and committed before its first run, dry included (b761 defect (h)).

  python -X utf8 -u tools/b761_lines.py dry|write     data/b761_lines.txt and .json; writes nothing else

THE SIX LINES: for each act from b755 to b760, one line in canon XXIII (A)'s form (THE_METHOD_CANON.md :351), prefixed '<act>, FINDINGS
:<line>:', the line its entry's heading's, read as the sitting's passed items read them (data/b761_sitting_agenda.json; the author's answer,
data/b761_author_answers.txt, the navigator's recommendation applied): the maps read again at PLACE-papers HEAD, as they stand after (7), (8)
and (9), by the sitting tool's placement and carrying (tools/b761_sitting.py place, carried) and by tools/standing/linematch.py's stage over
the entry's names and its keystone's names; each reading compared with the agenda's passed reading, and each heading with its digest there.
A finding the maps place nowhere: "no seat in the cluster table", keystone none yet, stage BANKED (canon XXIII (B)).
THIS ACT'S OWN LINE: the entry's last line, for the act's findings named by their banks (FINDINGS_NAMES, the names its heading is to carry),
read the same way; beside it, b754's search (the lines of SPIRAL_MAP and REGISTRY naming each name) printed, not graded.
No FINDINGS line is written by this tool; the act's entry takes the six lines under one head at its composition (tools/acts/b761.py), its own
line last; no line of an earlier entry rewritten, the tallies those entries carry standing as written. No PLACE-papers line printed but the
names, the cluster's label and the stage words; the protected word neither printed nor stored; no git write.
"""
import json
import os
import re
import sys

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import linematch as LM      # noqa: E402
import b761_sitting as ST   # noqa: E402
import b761_registry as RG  # noqa: E402

ACT, NL = 'b761', '\n'
BANK = os.path.join(D, 'b761_lines.txt')
BJSON = os.path.join(D, 'b761_lines.json')
LINE_ACTS = ('b755', 'b756', 'b757', 'b758', 'b759', 'b760')
FINDINGS_NAMES = ('b761_corrigendum', 'b761_author_rulings', 'b761_ledgers', 'b761_orders', 'b761_registry_cells', 'b761_sitting_agenda',
                  'b761_recut_inputs', 'b761_lines')
FORM = 'INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <BANKED | CLUSTERED | SYNTHESISED | DEPOSITED>'
FORM_AT = 351
NOSEAT = 'no seat in the cluster table'


def line_of(cluster, keys, stage):
    return 'INTEGRATION: cluster %s ; keystone %s ; stage %s' % (cluster or NOSEAT, ', '.join(keys) or 'none yet', stage)


def read_at_head(heading, names, ct, rr, ktexts):
    """the sitting's placement at HEAD, then linematch's stage over the names and the placed keystone's names: (cluster, keys, stage, why)."""
    found = ST.place(heading, ct, rr, ktexts)
    if not found:
        st, _m = LM.stage(list(names), [], clustered=False)
        return None, [], st, 'no rule places it'
    best = None
    for row, why in found:
        kn = set()
        for kp in row['keys']:
            kn |= set(ktexts[kp][1])
        st, m = LM.stage(list(names), sorted(kn), clustered=bool(row['keys']))
        cand = (row['name'], row['keys'], st, '; '.join(why) + (' ; matched %s' % ', '.join(m) if m else ''))
        if best is None or (st == 'SYNTHESISED' and best[2] != 'SYNTHESISED'):
            best = cand
    return best


def main(mode):
    A = json.load(open(ST.AJSON, encoding='utf-8'))
    W = ST.relay_lines(ST.ANSWERS)
    res = [l for l in W if l.startswith('RESULT (')]
    chosen = len(res) == 1 and ST.CHOSEN in res[0]
    F, S, R, C = ST.show('FINDINGS.md'), ST.show('SPIRAL_MAP.md'), ST.show('REGISTRY.md'), ST.show('phase1.5/method/THE_METHOD_CANON.md')
    head = ST.subprocess.run(['git', '-C', ST.PP, 'rev-parse', '--short=8', 'HEAD'], capture_output=True).stdout.decode().strip()
    ct, rr = ST.cluster_table(S), ST.reg_rows(R)
    ktexts = {}
    for row in ct:
        for kp in row['keys']:
            if kp not in ktexts:
                KL = ST.show(kp)
                ktexts[kp] = (KL, LM.names(NL.join(KL)))
    items = dict((i['act'], i) for i in A['items'])
    P = ['%s -- (R371)(6): THE INTEGRATION LINES IN THE CANON`S FORM, b755 TO b760 AND THIS ACT`S OWN (%s)' % (ACT, ST.utc()), '',
         '### tools/b761_lines.py %s; PLACE-papers HEAD %s (after (7), (8) and (9)); REGISTRY, SPIRAL_MAP`s cluster table and the keystones read at HEAD by' % (mode, head),
         '### the sitting`s placement (tools/b761_sitting.py) and tools/standing/linematch.py`s stage; each reading compared with the sitting`s passed reading',
         '### (data/b761_sitting_agenda.json; the author`s answer %s :%d, %s); no FINDINGS line written here; no PLACE-papers line quoted.' % (
             ST.ANSWERS, next((k for k, l in enumerate(W, 1) if l.startswith('RESULT (')), 0),
             'the navigator`s recommendation applied' if chosen else 'THE ANSWER NOT READ'), '',
         '## THE FORM (phase1.5/method/THE_METHOD_CANON.md :%d): %s' % (FORM_AT, FORM), '']
    lines, ok_rows, rows_txt = [], [], []
    for a in LINE_ACTS:
        i = items[a]
        h = F[i['line'] - 1]
        same_h = ST.sha(h) == i['sha']
        passed = 'BANKED, NO SEAT' if (a in ST.NAV and chosen) else i['reading']
        want = passed.split(',')[0].split(' ')[0]
        cl, keys, st, why = read_at_head(h, i['names'], ct, rr, ktexts)
        same = (st == want and (cl or None) == (i['cluster'] if want != 'BANKED' else None) and list(keys) == (list(i['keys']) if want != 'BANKED' else []))
        text = line_of(cl, keys, st)
        lines.append(dict(act=a, line=i['line'], text='%s, FINDINGS :%d: %s' % (a, i['line'], text), stage=st, item=i['n'],
                          path_only=bool(i['path_only']) and st == 'SYNTHESISED'))
        ok_rows.append(same and same_h)
        rows_txt.append('  [%d] %s: heading FINDINGS :%d %s ; passed %s ; at HEAD %s, by %s ; %s' % (
            i['n'], a, i['line'], 'by its digest as the agenda read it' if same_h else 'MOVED FROM THE AGENDA`S DIGEST', passed, st, why,
            'AS THE SITTING READ IT' if same else 'NOT AS THE SITTING READ IT'))
    own_head = '## ' + ' '.join(FINDINGS_NAMES)
    own_names = LM.names(own_head)
    ocl, okeys, ost, owhy = read_at_head(own_head, own_names, ct, rr, ktexts)
    own = line_of(ocl, okeys, ost)
    b754 = [(n, sum(1 for l in S if n in l), [k for k, l in enumerate(R, 1) if n in l], [k for k, l in enumerate(C, 1) if n in l]) for n in FINDINGS_NAMES]
    P.append('## THE LINES FOR THIS ACT`S FINDINGS ENTRY, UNDER ONE HEAD, IN THE ACTS` ORDER ((R371)(6)):')
    P += ['  ' + x['text'] for x in lines]
    P += ['', '## THIS ACT`S OWN LINE, THE ENTRY`S LAST LINE (its findings named by their banks: %s):' % ', '.join(FINDINGS_NAMES), '  ' + own, '']
    P.append('## THE READINGS AT HEAD BESIDE THE SITTING`S')
    P += rows_txt
    P.append('  b761: names %s ; at HEAD %s, by %s' % (', '.join(own_names), ost, owhy))
    P.append('  b754`s search beside it, printed and not graded (lines of SPIRAL_MAP, REGISTRY and the canon naming each name): %s' % '; '.join(
        '%s %d/%s/%s' % (n, s, ','.join(':%d' % k for k in r) or '0', ','.join(':%d' % k for k in c) or '0') for n, s, r, c in b754))
    P.append('    a name in REGISTRY`s dated block of [A1] or in the canon`s section XXIV is no cluster row`s and no keystone`s of the cluster table; the')
    P.append('    canon`s (B) reads CLUSTERED where a REGISTRY row or a SPIRAL_MAP block names the finding, so the line reads as above.')
    P.append('  beside the lines: items %s read SYNTHESISED by relay paths alone, which canon XXIV sends out of the paper at its re-cut' % (
        ', '.join('%d (%s)' % (x['item'], x['act']) for x in lines if x['path_only']) or 'none'))
    P.append('')
    epn = next((v[1] for k, v in ktexts.items() if 'EPSTEIN' in k), [])
    ctl = [('the answer read: one RESULT line, the option chosen the navigator`s recommendation', chosen),
           ('the canon`s form at :%d equal to the form written here' % FORM_AT, C[FORM_AT - 1].strip() == FORM),
           ('the six read at HEAD as the sitting read them, each heading by its digest (%d of 6)' % sum(ok_rows), all(ok_rows) and len(ok_rows) == 6),
           ('linematch`s control: pc_online over the Epstein keystone`s names SYNTHESISED, b999_planted CLUSTERED',
            LM.stage(['pc_online'], epn)[0] == 'SYNTHESISED' and LM.stage(['b999_planted'], epn)[0] == 'CLUSTERED'),
           ('the placement`s control: a heading naming zq_offline_zero placed (the Epstein keystone carries it), b999_planted_bank nowhere',
            bool(ST.place('## zq_offline_zero', ct, rr, ktexts)) and not ST.place('## b999_planted_bank', ct, rr, ktexts)),
           ('this act`s names read by linematch from its stand-in heading: %d of %d' % (len(own_names), len(FINDINGS_NAMES)), own_names == list(FINDINGS_NAMES)),
           ('every line in the form: the prefix, then INTEGRATION: cluster ; keystone ; stage', all(
               re.match(r'^b7\d\d, FINDINGS :\d+: INTEGRATION: cluster [^;]+ ; keystone [^;]+ ; stage (BANKED|CLUSTERED|SYNTHESISED|DEPOSITED)$', x['text'])
               for x in lines) and bool(re.match(r'^INTEGRATION: cluster [^;]+ ; keystone [^;]+ ; stage (BANKED|CLUSTERED|SYNTHESISED|DEPOSITED)$', own)))]
    text = NL.join(P)
    I = RG.ids()
    qw = RG.qword(R)
    ctl.append(('the identifiers 0 and the protected word 0', RG.idcount(text, I) == 0 and qw.lower() not in text.lower()))
    ok = all(o for _w, o in ctl)
    P += ['## THE CONTROLS'] + ['  %-140s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    st_c = dict((s, sum(1 for x in lines if x['stage'] == s)) for s in ('SYNTHESISED', 'CLUSTERED', 'BANKED'))
    P += ['', '### ### **THE LINES: 6 FOR b755 TO b760 (SYNTHESISED %d, CLUSTERED %d, BANKED %d) AND THIS ACT`S OWN (%s) ; AS THE SITTING READ THEM %d OF 6 ; '
          'CONTROLS %d OF %d AS WANTED ; %s.**' % (st_c['SYNTHESISED'], st_c['CLUSTERED'], st_c['BANKED'], ost, sum(ok_rows), sum(1 for _w, o in ctl if o), len(ctl),
                                                  ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    out = NL.join(P) + NL
    print(out)
    if mode == 'write':
        if not ok:
            ST.die('A CONTROL NOT AS WANTED')
        ST.put(BANK, out)
        ST.put(BJSON, json.dumps(dict(at=ST.utc(), act=ACT, pp_head=head, head='THE INTEGRATION LINES OF b755 TO b760, IN THE CANON`S FORM ((R371)(6))',
                                      lines=lines, own=own, own_names=list(FINDINGS_NAMES), counts=st_c, controls=[[w, o] for w, o in ctl]),
                                 ensure_ascii=False, indent=1) + NL)
        print('written data/b761_lines.txt (%d lines) and data/b761_lines.json' % len(P))


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('dry', 'write'):
        sys.exit(__doc__)
    main(sys.argv[1])
