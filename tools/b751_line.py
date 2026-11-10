"""b751 Component 3, (R361)(4): THE INTEGRATION LINE FOR THIS ACT'S ENTRY, read from REGISTRY and SPIRAL_MAP with the match of (3)(iv).

The line in canon XXIII (A)'s form: INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <...>, the stages XXIII (B). This act's
finding is §5 of the keystone, the located zero, passed at [S5] and written at PLACE-papers b07cd7d3 (relay data/b751_section5.txt); its names,
which the entry's heading is to carry, are FINDING below. The stage is read by tools/standing/linematch.py: the finding's names matched
against the names the keystone carries for it (its dated note for §5 and §5's body) -- SYNTHESISED where a name matches, CLUSTERED where none
does. The earlier entries' lines read again by the same match, each entry's heading names against [F2]'s note in the sibling anchor and the
keystone's text; no FINDINGS line rewritten. Every map read through relaypath.rows_of/grep_of. The trail names the plan act's opening, not run.

usage: python -X utf8 -u tools/b751_line.py dry|write
"""
import io
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'standing'))
import relaypath as RP  # noqa: E402
import linematch as LM  # noqa: E402

RELAY = 'D:/relay'
PP = 'D:/MY-DOwnloads/PLACE-papers'
BANK = os.path.join(RELAY, 'data', 'b751_line.txt')
KEYSTONE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
SIBLING = 'day1/Which_Structure_Confines_v2_4_0.md'
FINDING = ('zq_offline_zero', 'b751_section5', 'b751_literature')   # ### the act's finding: the statement §5 reports, its section bank, its literature bank
F2_NEEDLES = ('(R360)`(2)[F2]', 'zq_offline_zero', 'pc_online', 'zeta_box')
EARLIER = ((14145, 'b745'), (14187, 'b746'), (14299, 'b747'), (14427, 'b748'), (14534, 'b749'), (14665, 'b750'))   # ### FINDINGS lines, as the grep printed them


def main(mode):
    out, R = [], []
    w = R.append
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    w('b751 -- (R361)(4): THE LINE: THE INTEGRATION LINE FOR THIS ACT`S ENTRY, FROM REGISTRY AND SPIRAL_MAP, READ WITH THE MATCH OF (3)(iv) (%s)' % stamp)
    w('')
    w('### every map read from the PLACE-papers working tree through tools/standing/relaypath.py; the stage read by tools/standing/linematch.py (v1.31.0);')
    w('### nothing written to any map, keystone or FINDINGS line; no Zenodo call; the stages canon XXIII (B).')
    w('')
    canon = RP.grep_of(PP, 'phase1.5/method/THE_METHOD_CANON.md', '## XXIII. The integration line and its stages', out=out)
    seat = RP.grep_of(PP, 'SPIRAL_MAP.md', '| **The Epstein instance** (seated 2026-11-09, b750) |', out=out)
    seat_ok = len(seat) == 1 and KEYSTONE in seat[0][1] and SIBLING in seat[0][1]
    ctab = RP.rows_of(PP, 'SPIRAL_MAP.md', 266, 276, out=out)
    crow = [l for l in ctab if l.startswith('| **')]
    reg = [RP.grep_of(PP, 'REGISTRY.md', '| %s |' % r, out=out) for r in ('1.5c-21', '1.5c-22', '1.5c-23')]
    reg_ok = all(len(x) >= 1 for x in reg)
    knote = RP.grep_of(PP, KEYSTONE, 'Dated note, 2026-11-10, b751', out=out)
    khead = RP.grep_of(PP, KEYSTONE, '## 5. The located zero', out=out)
    k6 = RP.grep_of(PP, KEYSTONE, '## 6. The corollary', out=out)
    body = RP.rows_of(PP, KEYSTONE, khead[0][0] + 1, k6[0][0] - 1, out=out) if (khead and k6) else []
    note_text = ' '.join(l for _i, l in knote) + ' ' + ' '.join(body)
    st, hit = LM.stage(list(FINDING), LM.names(note_text))
    k_pc = len(RP.grep_of(PP, KEYSTONE, 'Epstein', out=out))      # ### the positive control: the same reader finds the object in the keystone
    line = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :%d) ; keystone %s ; stage %s'
            % (seat[0][0] if seat else 0, 'THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress)' if seat_ok else 'none yet', st if (seat_ok and reg_ok) else 'BANKED'))

    w('## (A) THE LINE, IN THE FORM OF CANON XXIII (A) (PLACE-papers phase1.5/method/THE_METHOD_CANON.md :%s):' % (canon[0][0] if canon else '?'))
    w('      INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <BANKED | CLUSTERED | SYNTHESISED | DEPOSITED>')
    w('  the line for b751`s entry, its last line, for the act`s finding (§5 of the keystone, the located zero; relay data/b751_section5.txt):')
    w('      ' + line)
    w('')
    w('## (B) ITS SOURCES AND THE MATCH:')
    w('  the canon`s section XXIII heading: %d row(s) %s' % (len(canon), ' '.join(':%d' % i for i, _l in canon)))
    w('  SPIRAL_MAP.md, the cluster row seated at b750: %s ; naming the keystone %s and the sibling anchor %s: %s'
      % (' '.join(':%d' % i for i, _l in seat) or 'NONE', KEYSTONE, SIBLING, 'YES' if seat_ok else 'NO'))
    w('  the cluster table (SPIRAL_MAP.md :266-:276), its cluster rows %d (the control: the table read, not empty)' % len(crow))
    for r, x in zip(('1.5c-21', '1.5c-22', '1.5c-23'), reg):
        w('  REGISTRY.md, rows of %s: %s' % (r, ' '.join(':%d' % i for i, _l in x) or 'NONE'))
    w('  the keystone`s dated note for §5: %s ; §5`s heading %s, its body %d rows to §6`s heading %s'
      % (' '.join(':%d' % i for i, _l in knote) or 'NONE', ' '.join(':%d' % i for i, _l in khead) or 'NONE', len(body),
         ' '.join(':%d' % i for i, _l in k6) or 'NONE'))
    w('  the finding`s names (the entry`s heading to carry them): %s' % ', '.join(FINDING))
    w('  matched in the keystone`s note and §5 (linematch.stage): %s ; the positive control, rows naming Epstein by the same reader: %d' % (', '.join(hit) or 'NONE', k_pc))
    w('  stage: %s (a keystone the cluster names carries the finding by a passed section and a dated note citing its bank)' % st)
    w('')
    w('## (C) THE EARLIER ENTRIES` LINES, READ AGAIN WITH THE MATCH (no FINDINGS line rewritten):')
    f2 = RP.grep_of(PP, SIBLING, F2_NEEDLES[0], out=out)
    f2_rows = [(i, l) for i, l in f2 if all(n in l for n in F2_NEEDLES)]
    f2_text = ' '.join(l for _i, l in f2_rows)
    kall = ' '.join(RP.rows_of(PP, KEYSTONE, 1, k6[0][0] - 1, out=out)) if k6 else ''
    w('  [F2]`s dated note in the sibling anchor (needles %s): %s ; its names %d' % (' , '.join(repr(n) for n in F2_NEEDLES),
                                                                                    ' '.join(':%d' % i for i, _l in f2_rows) or 'NONE', len(LM.names(f2_text))))
    flines = RP.rows_of(PP, 'FINDINGS.md', 1, max(n for n, _a in EARLIER), out=out)
    good_c = True
    for n, a in EARLIER:
        txt = flines[n - 1] if len(flines) >= n else ''
        if not txt.startswith('INTEGRATION:'):
            good_c = False
        rd = LM.read(flines, n, f2_text + ' ' + kall)
        w('  FINDINGS :%d (%s): stage as written %s ; heading :%s names %s ; matched %s ; as the match reads now %s'
          % (n, a, txt.rsplit('stage ', 1)[-1].strip() if txt else '?', rd['heading'], ', '.join(rd['names']) or 'NONE',
             ', '.join(rd['matched']) or 'NONE', rd['stage']))
    w('  these readings are printed for the record and entered in no line; b750`s (C) read b745-b748 SYNTHESISED by the cluster alone.')
    w('')
    w('## (D) THE TRAIL:')
    w('  the plan act`s opening, named and not run: I-109`s figure and the class-group signature of the negative n (the twenty smallest negative n of')
    w('  relay data/b750_cq_sign.txt each carry the factor 2 or 3, the primes whose ideals in Q(√−23) lie outside the principal class; whether every')
    w('  negative n does is the plan act`s control).')
    w('  the literature claim about the box of b745: unbanked and in no door.')
    w('  the navigator`s search of 2026-11-10 for a located zero of ζ in a proof assistant: no such result and no result saying there is none, entered in')
    w('  relay data/b751_literature.txt (V2) as a search with no finding; the claim stays out.')
    w('  the located zero against the classical theorem: an instance of Voronin`s theorem numerically, the certificate`s enclosure containing Re s = 1')
    w('  (relay data/b751_literature.txt L1-L4; data/b751_section5.txt D1; defect (h)).')
    w('')
    w('## (R) THE READS:')
    R.extend(out)
    w('')
    good = (len(canon) == 1 and seat_ok and len(crow) >= 9 and reg_ok and len(knote) == 1 and len(khead) == 1 and len(k6) == 1 and body
            and k_pc > 0 and len(f2_rows) == 1 and good_c)
    w('### ### **THE LINE: COMPOSED ; FROM REGISTRY 1.5c-21 TO 1.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE THE_EPSTEIN_CONTROL_OBJECT_v0_1 ; '
      'STAGE %s ; MATCHED %d OF %d ; THE EARLIER LINES READ AGAIN %d, NONE REWRITTEN ; %s.**'
      % (st, len(hit), len(FINDING), len(EARLIER), 'ALL AS READ' if good else 'NOT ALL AS READ'))
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
