"""b753 Component 4: THE INTEGRATION LINE FOR THIS ACT'S ENTRY, read from REGISTRY and SPIRAL_MAP with the match of tools/standing/linematch.py.

The line in canon XXIII (A)'s form: INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <...>, the stages XXIII (B). By (R363)(8)
this act's findings are the registration of (4) and the reads of (5), "at the stage the tool reads". They are of two kinds and the tool reads
each by its own:
  the registration (relay data/b753_registrations.txt) is about the walk of the Epstein instance's object at class number 3; its cluster is that
    instance's, read from the seat in SPIRAL_MAP's cluster table and REGISTRY's rows, and its stage by the match: its name against the names the
    keystone carries -- SYNTHESISED where it matches, CLUSTERED where it does not;
  the refresh's reads (relay data/b753_kernels.txt, data/b753_branch_map.txt, data/b753_head_read.txt, data/b753_anchors.txt,
    data/b753_store.txt) are about the system's own state; the tool searches SPIRAL_MAP and REGISTRY for each name, and where no row or block
    names one the canon's words apply: "no seat in the cluster table", keystone "none yet", stage BANKED.
No keystone line is written this act ((R363)(10)), so no match is expected; the reader decides it. The earlier entries' lines are read again by
the same match; no FINDINGS line rewritten. Every map read through relaypath.rows_of/grep_of.

usage: python -X utf8 -u tools/b753_line.py dry|write
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
BANK = os.path.join(RELAY, 'data', 'b753_line.txt')
KEYSTONE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
SIBLING = 'day1/Which_Structure_Confines_v2_4_0.md'
REGISTRATION = ('b753_registrations',)                                                           # ### (R363)(4)
READS = ('b753_kernels', 'b753_branch_map', 'b753_head_read', 'b753_anchors', 'b753_store')      # ### (R363)(5)(i)-(iv), (vii); (v) and (vi) carried
F2_NEEDLES = ('(R360)`(2)[F2]', 'zq_offline_zero', 'pc_online', 'zeta_box')
EARLIER = ((14145, 'b745'), (14187, 'b746'), (14299, 'b747'), (14427, 'b748'), (14534, 'b749'), (14665, 'b750'), (14783, 'b751'), (14908, 'b752'))   # ### FINDINGS lines, as the search printed them


def main(mode):
    out, R = [], []
    w = R.append
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    w('b753 -- Component 4: THE LINE: THE INTEGRATION LINE FOR THIS ACT`S ENTRY, FROM REGISTRY AND SPIRAL_MAP, READ WITH THE MATCH (%s)' % stamp)
    w('')
    w('### every map read from the PLACE-papers working tree through tools/standing/relaypath.py; the stage read by tools/standing/linematch.py (v1.33.0);')
    w('### nothing written to any map, keystone or FINDINGS line; no Zenodo call; the stages canon XXIII (B). Lines and counts alone are printed of the maps.')
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
    st, hit = LM.stage(list(REGISTRATION), LM.names(kall))
    k_pc = len(RP.grep_of(PP, KEYSTONE, 'Epstein', out=out))      # ### the positive control: the same reader finds the object in the keystone
    pc_st, pc_hit = LM.stage(['zq_offline_zero'], LM.names(kall))  # ### the match's positive control: a name the keystone carries reads SYNTHESISED
    # the reads: is any of them named by a row or block of the maps
    named = []
    for n in READS:
        a = RP.grep_of(PP, 'SPIRAL_MAP.md', n, out=out)
        b = RP.grep_of(PP, 'REGISTRY.md', n, out=out)
        named.append((n, len(a), len(b)))
    map_pc = len(RP.grep_of(PP, 'SPIRAL_MAP.md', 'Epstein', out=out))   # ### the positive control of that search: the same reader finds a name the map carries
    reads_seated = any(a or b for _n, a, b in named)
    reg_stage = st if (seat_ok and reg_ok) else 'BANKED'
    reads_stage = 'CLUSTERED' if reads_seated else 'BANKED'
    line = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :%d) for the registration, no seat in the '
            'cluster table for the refresh`s reads ; keystone %s for the registration, none yet for the reads ; stage %s (the registration), %s (the reads)'
            % (seat[0][0] if seat else 0, 'THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress)' if seat_ok else 'none yet', reg_stage, reads_stage))

    w('## (A) THE LINE, IN THE FORM OF CANON XXIII (A) (PLACE-papers phase1.5/method/THE_METHOD_CANON.md :%s):' % (canon[0][0] if canon else '?'))
    w('      INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <BANKED | CLUSTERED | SYNTHESISED | DEPOSITED>')
    w('  the line for b753`s entry, its last line, for the act`s findings ((R363)(8): the registration of (4) and the reads of (5), each at the stage read):')
    w('      ' + line)
    w('')
    w('## (B) ITS SOURCES AND THE MATCH:')
    w('  the canon`s section XXIII heading: %d row(s) %s' % (len(canon), ' '.join(':%d' % i for i, _l in canon)))
    w('  THE REGISTRATION (%s):' % ', '.join(REGISTRATION))
    w('    SPIRAL_MAP.md, the cluster row seated at b750: %s ; naming the keystone %s and the sibling anchor %s: %s'
      % (' '.join(':%d' % i for i, _l in seat) or 'NONE', KEYSTONE, SIBLING, 'YES' if seat_ok else 'NO'))
    w('    the cluster table (SPIRAL_MAP.md :266-:276), its cluster rows %d (the control: the table read, not empty)' % len(crow))
    for r, x in zip(('1.5c-21', '1.5c-22', '1.5c-23'), reg):
        w('    REGISTRY.md, rows of %s: %s' % (r, ' '.join(':%d' % i for i, _l in x) or 'NONE'))
    w('    the keystone`s dated notes: %s ; its whole text read to section 9`s heading %s, %d rows'
      % (' '.join(':%d' % i for i, _l in knotes) or 'NONE', ' '.join(':%d' % i for i, _l in k9) or 'NONE', len(kall_rows)))
    w('    matched in the keystone`s text (linematch.stage): %s ; the positive control, rows naming Epstein by the same reader: %d' % (', '.join(hit) or 'NONE', k_pc))
    w('    the match`s positive control, a name the keystone carries (zq_offline_zero) read by the same call: %s, matched %s' % (pc_st, ', '.join(pc_hit) or 'NONE'))
    w('    stage: %s (%s)' % (reg_stage, 'the keystone carries the registration`s name' if hit else
                               'the cluster names the keystone and the keystone does not carry the registration`s name: no keystone line written this act, (R363)(10); the walk registered, not run'))
    w('  THE REFRESH`S READS (%s):' % ', '.join(READS))
    for n, a, b in named:
        w('    %s: rows of SPIRAL_MAP.md naming it %d ; rows of REGISTRY.md naming it %d' % (n, a, b))
    w('    the search`s positive control, rows of SPIRAL_MAP.md naming Epstein by the same reader: %d' % map_pc)
    w('    stage: %s (%s)' % (reads_stage, 'a row of the maps names a read' if reads_seated else
                               'no row or block of the maps names any of them: by the canon`s (B), "no seat in the cluster table", keystone none yet'))
    w('  (R363)(5)(v) and (5)(vi), the shelves` listing and the cluster export, were carried by the author`s amendment and are no finding of this act.')
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
    w('## (D) THE TRAIL, by (R363)(8), carried to the sitting and named there:')
    w('  every door of (5)(iii) not reading AGREES (relay data/b753_head_read.txt); every anchor of (5)(iv) moved by a later line (relay')
    w('  data/b753_anchors.txt), by the author`s eighth word (4) the two whose words the remote main`s tree did not hold at the head of the list')
    w('  (FINDINGS :901, :979; relay data/b753_waiver.txt) and PLACE-papers` description with them; I-109`s cross-reference to I-106, I-108 and')
    w('  data/b711_coeffs.txt; the Epstein document`s section 8; the items (R362)(8) carried; the line between what the relay quotes of PLACE-papers')
    w('  and what it cites by line and digest (the eighth word (3)); the temp directory read (the sixth word (4)). Nothing built this act.')
    w('')
    w('## (R) THE READS:')
    R.extend(out)
    w('')
    good = (len(canon) == 1 and seat_ok and len(crow) >= 9 and reg_ok and len(knotes) >= 1 and len(k9) == 1 and kall_rows
            and k_pc > 0 and pc_st == 'SYNTHESISED' and map_pc > 0 and len(f2_rows) == 1 and good_c)
    w('### ### **THE LINE: COMPOSED ; FROM REGISTRY 1.5c-21 TO 1.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE THE_EPSTEIN_CONTROL_OBJECT_v0_1 ; '
      'STAGE %s/%s ; MATCHED %d OF %d ; THE REGISTRATION %s, THE READS %s (%d NAMES, %d SEATED) ; THE EARLIER LINES READ AGAIN %d, NONE REWRITTEN ; %s.**'
      % (reg_stage, reads_stage, len(hit), len(REGISTRATION) + len(READS), reg_stage, reads_stage, len(READS), sum(1 for _n, a, b in named if a or b),
         len(EARLIER), 'ALL AS READ' if good else 'NOT ALL AS READ'))
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
