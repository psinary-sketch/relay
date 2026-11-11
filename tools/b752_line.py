"""b752 Component 4: THE INTEGRATION LINE FOR THIS ACT'S ENTRY, read from REGISTRY and SPIRAL_MAP with the match of tools/standing/linematch.py.

The line in canon XXIII (A)'s form: INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <...>, the stages XXIII (B). This act's
findings are the plan of W-ORD-MECHANISM-ATTRIBUTION and the banks it stands on -- the cross-reference, the class-group signature control and
the statements (relay data/b752_crossref.txt, data/b752_cq_signature.txt, data/b752_statements.txt, data/b752_attribution_plan.txt); their
names, which the entry's heading is to carry, are FINDING below. The plan's statements are about Z_Q0, the object of the Epstein instance, so
the cluster is that instance's. The stage is read by tools/standing/linematch.py: the finding's names matched against the names the keystone
carries -- its whole text, every dated note and every section -- SYNTHESISED where a name matches, CLUSTERED where none does. No keystone line
is written this act ((R362)(10)), so a match is not expected; the reader decides it. The earlier entries' lines read again by the same match;
no FINDINGS line rewritten. Every map read through relaypath.rows_of/grep_of. The trail names the build's place, not run.

usage: python -X utf8 -u tools/b752_line.py dry|write
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
BANK = os.path.join(RELAY, 'data', 'b752_line.txt')
KEYSTONE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
SIBLING = 'day1/Which_Structure_Confines_v2_4_0.md'
FINDING = ('b752_attribution_plan', 'b752_cq_signature', 'b752_statements', 'b752_crossref')   # ### the act's findings: the plan and its three banks
F2_NEEDLES = ('(R360)`(2)[F2]', 'zq_offline_zero', 'pc_online', 'zeta_box')
EARLIER = ((14145, 'b745'), (14187, 'b746'), (14299, 'b747'), (14427, 'b748'), (14534, 'b749'), (14665, 'b750'), (14783, 'b751'))   # ### FINDINGS lines, as the grep printed them


def main(mode):
    out, R = [], []
    w = R.append
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    w('b752 -- Component 4: THE LINE: THE INTEGRATION LINE FOR THIS ACT`S ENTRY, FROM REGISTRY AND SPIRAL_MAP, READ WITH THE MATCH (%s)' % stamp)
    w('')
    w('### every map read from the PLACE-papers working tree through tools/standing/relaypath.py; the stage read by tools/standing/linematch.py (v1.32.0);')
    w('### nothing written to any map, keystone or FINDINGS line; no Zenodo call; the stages canon XXIII (B).')
    w('')
    canon = RP.grep_of(PP, 'phase1.5/method/THE_METHOD_CANON.md', '## XXIII. The integration line and its stages', out=out)
    seat = RP.grep_of(PP, 'SPIRAL_MAP.md', '| **The Epstein instance** (seated 2026-11-09, b750) |', out=out)
    seat_ok = len(seat) == 1 and KEYSTONE in seat[0][1] and SIBLING in seat[0][1]
    ctab = RP.rows_of(PP, 'SPIRAL_MAP.md', 266, 276, out=out)
    crow = [l for l in ctab if l.startswith('| **')]
    reg = [RP.grep_of(PP, 'REGISTRY.md', '| %s |' % r, out=out) for r in ('1.5c-21', '1.5c-22', '1.5c-23')]
    reg_ok = all(len(x) >= 1 for x in reg)
    knotes = RP.grep_of(PP, KEYSTONE, '*Dated note, ', out=out)
    k9 = RP.grep_of(PP, KEYSTONE, '## 9. Back matter', out=out)
    kall_rows = RP.rows_of(PP, KEYSTONE, 1, k9[0][0] + 1, out=out) if k9 else []
    kall = ' '.join(kall_rows)
    st, hit = LM.stage(list(FINDING), LM.names(kall))
    k_pc = len(RP.grep_of(PP, KEYSTONE, 'Epstein', out=out))      # ### the positive control: the same reader finds the object in the keystone
    pc_st, pc_hit = LM.stage(['zq_offline_zero'], LM.names(kall))  # ### the match's positive control: a name the keystone carries reads SYNTHESISED
    line = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :%d) ; keystone %s ; stage %s'
            % (seat[0][0] if seat else 0, 'THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress)' if seat_ok else 'none yet', st if (seat_ok and reg_ok) else 'BANKED'))

    w('## (A) THE LINE, IN THE FORM OF CANON XXIII (A) (PLACE-papers phase1.5/method/THE_METHOD_CANON.md :%s):' % (canon[0][0] if canon else '?'))
    w('      INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <BANKED | CLUSTERED | SYNTHESISED | DEPOSITED>')
    w('  the line for b752`s entry, its last line, for the act`s findings (the plan of W-ORD-MECHANISM-ATTRIBUTION passed at [P1] and its three banks):')
    w('      ' + line)
    w('')
    w('## (B) ITS SOURCES AND THE MATCH:')
    w('  the canon`s section XXIII heading: %d row(s) %s' % (len(canon), ' '.join(':%d' % i for i, _l in canon)))
    w('  SPIRAL_MAP.md, the cluster row seated at b750: %s ; naming the keystone %s and the sibling anchor %s: %s'
      % (' '.join(':%d' % i for i, _l in seat) or 'NONE', KEYSTONE, SIBLING, 'YES' if seat_ok else 'NO'))
    w('  the cluster table (SPIRAL_MAP.md :266-:276), its cluster rows %d (the control: the table read, not empty)' % len(crow))
    for r, x in zip(('1.5c-21', '1.5c-22', '1.5c-23'), reg):
        w('  REGISTRY.md, rows of %s: %s' % (r, ' '.join(':%d' % i for i, _l in x) or 'NONE'))
    w('  the keystone`s dated notes: %s ; its whole text read to §9`s heading %s, %d rows'
      % (' '.join(':%d' % i for i, _l in knotes) or 'NONE', ' '.join(':%d' % i for i, _l in k9) or 'NONE', len(kall_rows)))
    w('  the findings` names (the entry`s heading to carry them): %s' % ', '.join(FINDING))
    w('  matched in the keystone`s text (linematch.stage): %s ; the positive control, rows naming Epstein by the same reader: %d' % (', '.join(hit) or 'NONE', k_pc))
    w('  the match`s positive control, a name the keystone carries (zq_offline_zero) read by the same call: %s, matched %s' % (pc_st, ', '.join(pc_hit) or 'NONE'))
    w('  stage: %s (%s)' % (st, 'the keystone carries a name of the finding' if hit else
                             'the cluster names the keystone and the keystone carries none of the findings` names: no keystone line written this act, (R362)(10)'))
    w('')
    w('## (C) THE EARLIER ENTRIES` LINES, READ AGAIN WITH THE MATCH (no FINDINGS line rewritten):')
    f2 = RP.grep_of(PP, SIBLING, F2_NEEDLES[0], out=out)
    f2_rows = [(i, l) for i, l in f2 if all(n in l for n in F2_NEEDLES)]
    f2_text = ' '.join(l for _i, l in f2_rows)
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
    w('  these readings are printed for the record and entered in no line.')
    w('')
    w('## (D) THE TRAIL:')
    w('  the build of the plan`s recommendation (T0, then T1; T2 printed as not abstracting at the pin; T3 the printed finding) is an act the author')
    w('  names, placed fourth: after the system refresh (b753), the sitting, and sections 6, 7 and 8 of the Epstein document (relay data/b752_author_answers.txt,')
    w('  [P1] passed); nothing built this act.')
    w('')
    w('## (R) THE READS:')
    R.extend(out)
    w('')
    good = (len(canon) == 1 and seat_ok and len(crow) >= 9 and reg_ok and len(knotes) >= 1 and len(k9) == 1 and kall_rows
            and k_pc > 0 and pc_st == 'SYNTHESISED' and len(f2_rows) == 1 and good_c)
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
