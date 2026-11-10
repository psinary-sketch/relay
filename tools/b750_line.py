"""b750 Component 3, (R360)(4): THE INTEGRATION LINE FOR THIS ACT'S ENTRY, read from REGISTRY and SPIRAL_MAP as they stand after the sitting's writes.

The line in the form of (R356)(6), now canon XXIII (A): INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <...>. The stages
those of XXIII (B), passed at the sitting as [A1] (relay data/b746_integration_draft.txt :18-:26): CLUSTERED where a REGISTRY row or a
SPIRAL_MAP block or a dated note to one names the finding or the object it is about; SYNTHESISED where a keystone the cluster names (in
REGISTRY's rows or SPIRAL_MAP's cluster table) carries the finding by a dated note or a passed section, citing its bank; DEPOSITED where a
deposited version of a keystone carries it. The act's own finding is the sign of cQ(n) over n <= 3000 (relay data/b750_cq_sign.txt,
INSTRUMENTS I-109), about Z_Q0's recursion, an object of the Epstein instance. Every map read through relaypath.rows_of/grep_of, which
refuse a path the repository does not track. The earlier entries' lines read again by the same stages and printed beside their FINDINGS
lines; no FINDINGS line is rewritten. The literature claim about the b745 box stays unbanked.

usage: python -X utf8 -u tools/b750_line.py dry|write
"""
import io
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'standing'))
import relaypath as RP  # noqa: E402

RELAY = 'D:/relay'
PP = 'D:/MY-DOwnloads/PLACE-papers'
BANK = os.path.join(RELAY, 'data', 'b750_line.txt')
KEYSTONE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
SIBLING = 'day1/Which_Structure_Confines_v2_4_0.md'
FIGURE = ('I-109', 'b750_cq_sign')                     # ### the act's finding's needles: its INSTRUMENTS row, its bank
F2_NEEDLES = ('(R360)`(2)[F2]', 'zq_offline_zero', 'pc_online', 'zeta_box')   # ### [F2]'s note: the ruling, the findings it carries
MONOGRAPH = ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')
EARLIER = ((14145, 'b745'), (14187, 'b746'), (14299, 'b747'), (14427, 'b748'), (14534, 'b749'))   # ### FINDINGS lines, as the grep printed them


def main(mode):
    out, R = [], []
    w = R.append
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    w('b750 -- (R360)(4): THE LINE: THE INTEGRATION LINE FOR THIS ACT`S ENTRY, FROM REGISTRY AND SPIRAL_MAP AFTER THE SITTING`S WRITES (%s)' % stamp)
    w('')
    w('### every map read from the PLACE-papers working tree through tools/standing/relaypath.py (rows_of, grep_of: a path the repository does not')
    w('### track is refused); the reads printed under (R); nothing written to any map, keystone or FINDINGS line; no Zenodo call; the stages canon XXIII (B).')
    w('')
    # ---- the sources
    canon = RP.grep_of(PP, 'phase1.5/method/THE_METHOD_CANON.md', '## XXIII. The integration line and its stages', out=out)
    seat = RP.grep_of(PP, 'SPIRAL_MAP.md', '| **The Epstein instance** (seated 2026-11-09, b750) |', out=out)
    seat_ok = len(seat) == 1 and KEYSTONE in seat[0][1] and SIBLING in seat[0][1]
    ctab = RP.rows_of(PP, 'SPIRAL_MAP.md', 266, 276, out=out)
    crow = [l for l in ctab if l.startswith('| **')]
    reg = [RP.grep_of(PP, 'REGISTRY.md', '| %s |' % r, out=out) for r in ('1.5c-21', '1.5c-22', '1.5c-23')]
    reg_ok = all(len(x) >= 1 for x in reg)
    k_fig = [h for n in FIGURE for h in RP.grep_of(PP, KEYSTONE, n, out=out)]
    s_fig = [h for n in FIGURE for h in RP.grep_of(PP, SIBLING, n, out=out)]
    k_pc = len(RP.grep_of(PP, KEYSTONE, 'cQ', out=out))             # ### the positive control: the same reader finds the object in the keystone
    s_pc = len(RP.grep_of(PP, SIBLING, 'Epstein', out=out))         # ### and in the sibling anchor
    ins = RP.grep_of(PP, 'phase1.5/method/INSTRUMENTS.md', 'b750_cq_sign', out=out)
    f2 = RP.grep_of(PP, SIBLING, F2_NEEDLES[0], out=out)
    f2_rows = [(i, l) for i, l in f2 if all(n in l for n in F2_NEEDLES)]
    mono = [(k, len([h for n in ('23228113', 'Dated note, b749') for h in RP.grep_of(PP, k, n, out=out)]),
             len(RP.grep_of(PP, k, 'Place to Stand', out=out))) for k in MONOGRAPH]
    fl = [(n, a, RP.rows_of(PP, 'FINDINGS.md', n, n, out=out)) for n, a in EARLIER]
    readme = RP.grep_of(PP, 'README.md', '(R360)', out=out)
    regnote = RP.grep_of(PP, 'REGISTRY.md', 'Dated note, b750', out=out)

    fig_nowhere = not k_fig and not s_fig
    stage = 'CLUSTERED' if (seat_ok and reg_ok and fig_nowhere) else ('SYNTHESISED' if (k_fig or s_fig) else 'BANKED')
    line = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :%d) ; keystone %s ; stage %s'
            % (seat[0][0] if seat else 0, 'THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress)' if seat_ok else 'none yet', stage))

    w('## (A) THE LINE, IN THE FORM OF CANON XXIII (A) (PLACE-papers phase1.5/method/THE_METHOD_CANON.md :%s):' % (canon[0][0] if canon else '?'))
    w('      INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <BANKED | CLUSTERED | SYNTHESISED | DEPOSITED>')
    w('  the line for b750`s entry, its last line, for the act`s finding (the sign of cQ(n), n <= 3000; relay data/b750_cq_sign.txt, INSTRUMENTS I-109):')
    w('      ' + line)
    w('')
    w('## (B) ITS SOURCES:')
    w('  the canon`s section XXIII heading: %d row(s) %s' % (len(canon), ' '.join(':%d' % i for i, _l in canon)))
    w('  SPIRAL_MAP.md, the cluster row seated at b750 ([F1], PLACE-papers 6fc025a1): %s ; naming the keystone %s and the sibling anchor %s: %s'
      % (' '.join(':%d' % i for i, _l in seat) or 'NONE', KEYSTONE, SIBLING, 'YES' if seat_ok else 'NO'))
    w('  the cluster table (SPIRAL_MAP.md :266-:276), its cluster rows %d (the control: the table read, not empty)' % len(crow))
    for r, x in zip(('1.5c-21', '1.5c-22', '1.5c-23'), reg):
        w('  REGISTRY.md, rows of %s: %s' % (r, ' '.join(':%d' % i for i, _l in x) or 'NONE'))
    w('  INSTRUMENTS.md, the rows citing the figure`s bank (b750_cq_sign): %s' % (' '.join(':%d' % i for i, _l in ins) or 'NONE'))
    w('  the keystone, rows carrying the figure (needles %s): %d (the positive control, rows naming cQ by the same reader: %d)'
      % (' , '.join(repr(n) for n in FIGURE), len(k_fig), k_pc))
    w('  the sibling anchor, rows carrying the figure: %d (the positive control, rows naming Epstein by the same reader: %d)' % (len(s_fig), s_pc))
    w('  stage: the object named by the cluster row and REGISTRY 1.5c-21 to 1.5c-23 (CLUSTERED); the figure carried by neither file the cluster')
    w('  names (not SYNTHESISED, not DEPOSITED): %s' % stage)
    w('')
    w('## (C) THE EARLIER ENTRIES` LINES, READ AGAIN BY THE SAME STAGES AFTER THE SITTING (no FINDINGS line rewritten):')
    w('  [F2]`s dated note in the sibling anchor, the cluster row naming it, carrying the findings of b738-b749 by name and pin (needles %s): %s'
      % (' , '.join(repr(n) for n in F2_NEEDLES), ' '.join(':%d' % i for i, _l in f2_rows) or 'NONE'))
    syn = bool(f2_rows) and seat_ok
    for n, a, rows in fl:
        txt = rows[0] if rows else ''
        if 'the Epstein instance' in txt:
            now = 'SYNTHESISED' if syn else 'CLUSTERED'
            why = ('by the cluster: [F2]`s note in %s, a file the cluster row names (the entry`s own finding not matched by needle)' % SIBLING
                   if syn else 'no note in a file the cluster names')
        elif 'the deposit line' in txt:
            hit = sum(h for _k, h, _p in mono)
            now = 'SYNTHESISED' if hit else 'CLUSTERED'
            why = '[D] kept, no write; the monograph`s files carry the finding in %d row(s) (positive controls %s)' % (hit, ', '.join(str(p) for _k, _h, p in mono))
        else:
            now, why = '?', 'the line not read'
        w('  FINDINGS :%d (%s): stage as written %s ; as the maps read now %s ; %s' % (n, a, txt.rsplit('stage ', 1)[-1].strip() if txt else '?', now, why))
    w('  THE LIMIT OF (C): the Epstein lines are read by the cluster, the note matched by its four needles; whether each entry`s own finding is')
    w('  among those the note names is not tested here, and these readings are printed for the record, not entered in any line.')
    w('')
    w('## (D) THE CARRIED ITEMS, LANDED AT THE SITTING:')
    w('  the canon text of the stages: XXIII at :%s ([A1], PLACE-papers 7fbaff0d)' % (canon[0][0] if canon else '?'))
    w('  the README item: rows citing (R360): %s ([B1] fd842c0f, [B2] c7bf1443)' % (' '.join(':%d' % i for i, _l in readme) or 'NONE'))
    w('  the 1.5c-21 dated note: REGISTRY rows "Dated note, b750": %s ([C], PLACE-papers 510eeea9)' % (' '.join(':%d' % i for i, _l in regnote) or 'NONE'))
    w('')
    w('## (E) THE LITERATURE CLAIM ABOUT THE BOX OF b745: unbanked, in no door, until a search is banked; nothing searched this act.')
    w('')
    w('## (R) THE READS:')
    R.extend(out)
    w('')
    good = (len(canon) == 1 and seat_ok and len(crow) >= 9 and reg_ok and k_pc > 0 and s_pc > 0 and len(ins) >= 1
            and len(f2_rows) == 1 and all(p > 0 for _k, _h, p in mono) and all(rows for _n, _a, rows in fl)
            and len(readme) >= 1 and len(regnote) >= 1)
    w('### ### **THE LINE: COMPOSED ; FROM REGISTRY 1.5c-21 TO 1.5c-23 AND SPIRAL_MAP AFTER THE SITTING ; KEYSTONE THE_EPSTEIN_CONTROL_OBJECT_v0_1 ; '
      'STAGE %s ; THE EARLIER LINES READ AGAIN %d, NONE REWRITTEN ; THE CARRIED ITEMS LANDED 3 ; %s.**'
      % (stage, len(fl), 'ALL AS READ' if good else 'NOT ALL AS READ'))
    text = '\n'.join(R) + '\n'
    print(text)
    if mode == 'write':
        if not good:
            raise SystemExit('### REFUSED: NOT ALL AS READ, NOTHING WRITTEN')
        tmp = BANK + '.part'
        with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        os.replace(tmp, BANK)
        print('  WROTE %s, %d lines' % (BANK, len(R)))


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('dry', 'write'):
        raise SystemExit(__doc__)
    main(sys.argv[1])
