"""b754 Component 4: THE INTEGRATION LINE FOR THIS ACT'S ENTRY, read from REGISTRY and SPIRAL_MAP with the match of tools/standing/linematch.py,
as the maps stand after the sitting's writes ((R364)(7)).

The line in canon XXIII (A)'s form: INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <...>, the stages XXIII (B). The act
computes nothing ((R364)(10)); its findings are the three reads of (R364)(4) it banked -- (i) the close's yield (relay
data/b754_close_yield.txt), (ii) the anchors' kernel tags (data/b754_anchor_grades.txt), (vi) the doors' current (data/b754_doors.txt);
(iii) to (v) carried -- and the record of its sitting ((R364)(5), data/b754_sitting.txt). Each is about the system's own record; the tool
searches SPIRAL_MAP and REGISTRY for each bank's name, and where no row or block names one the canon's words apply: "no seat in the cluster
table", keystone "none yet", stage BANKED. The sitting's record lines [R1] and [R3] stand in the Epstein instance's records (INSTRUMENTS
I-109's cross-reference; the keystone's headings and its dated note of b754): the keystone is read to section 9's heading as it stands after
[R3], and the findings' names are matched against the names it carries (linematch.stage), the note's own names printed. No keystone line is
written by this tool; the earlier entries' lines are read again by the same match; no FINDINGS line rewritten. Every map read through
relaypath.rows_of/grep_of, from the PLACE-papers working tree.

usage: python -X utf8 -u tools/b754_line.py dry|write
"""
import io
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'standing'))
import relaypath as RP  # noqa: E402
import linematch as LM  # noqa: E402
import orders as OR  # noqa: E402

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PP = OR.PP
BANK = os.path.join(RELAY, 'data', 'b754_line.txt')
KEYSTONE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
SIBLING = 'day1/Which_Structure_Confines_v2_4_0.md'
READS = ('b754_close_yield', 'b754_anchor_grades', 'b754_doors')     # ### (R364)(4)(i), (ii), (vi); (iii) to (v) carried by (8)
SITTING = ('b754_sitting',)                                           # ### (R364)(5), its record and foot
B754_NOTE = '*Dated note, 2026-11-14, b754:'                          # ### [R3]'s note in the keystone (relay data/b754_sitting.txt [R3])
F2_NEEDLES = ('(R360)`(2)[F2]', 'zq_offline_zero', 'pc_online', 'zeta_box')
EARLIER = ((14145, 'b745'), (14187, 'b746'), (14299, 'b747'), (14427, 'b748'), (14534, 'b749'), (14665, 'b750'), (14783, 'b751'), (14908, 'b752'),
           (15051, 'b753'))   # ### FINDINGS lines, as the search at PLACE-papers dbf8e93c printed them


def main(mode):
    out, R = [], []
    w = R.append
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    w('b754 -- Component 4: THE LINE: THE INTEGRATION LINE FOR THIS ACT`S ENTRY, FROM REGISTRY AND SPIRAL_MAP AFTER THE SITTING`S WRITES, READ WITH THE MATCH (%s)' % stamp)
    w('')
    w('### every map read from the PLACE-papers working tree through tools/standing/relaypath.py; the stage read by tools/standing/linematch.py;')
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
    k754 = RP.grep_of(PP, KEYSTONE, B754_NOTE, out=out)
    k9 = RP.grep_of(PP, KEYSTONE, '## 9. Back matter', out=out)
    kall_rows = RP.rows_of(PP, KEYSTONE, 1, k9[0][0] + 1, out=out) if k9 else []
    kall = ' '.join(kall_rows)
    knames = LM.names(kall)
    findings = list(READS) + list(SITTING)
    st, hit = LM.stage(findings, knames, clustered=False)
    n754 = LM.names(k754[0][1]) if k754 else []
    k_pc = len(RP.grep_of(PP, KEYSTONE, 'Epstein', out=out))        # ### the positive control: the same reader finds the object in the keystone
    pc_st, pc_hit = LM.stage(['zq_offline_zero'], knames)             # ### the match's positive control: a name the keystone carries reads SYNTHESISED
    named = []
    for n in findings:
        a = RP.grep_of(PP, 'SPIRAL_MAP.md', n, out=out)
        b = RP.grep_of(PP, 'REGISTRY.md', n, out=out)
        named.append((n, len(a), len(b)))
    map_pc = len(RP.grep_of(PP, 'SPIRAL_MAP.md', 'Epstein', out=out))   # ### the positive control of that search: the same reader finds a name the map carries
    seated = any(a or b for _n, a, b in named)
    stage = 'CLUSTERED' if seated and not hit else (st if seated else 'BANKED')
    line = ('INTEGRATION: cluster no seat in the cluster table for the act`s three reads and its sitting`s record ; keystone none yet ; stage %s' % stage)

    w('## (A) THE LINE, IN THE FORM OF CANON XXIII (A) (PLACE-papers phase1.5/method/THE_METHOD_CANON.md :%s):' % (canon[0][0] if canon else '?'))
    w('      INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <BANKED | CLUSTERED | SYNTHESISED | DEPOSITED>')
    w('  the line for b754`s entry, its last line, for the act`s findings (the three reads of (R364)(4) and the record of its sitting, each at the stage read):')
    w('      ' + line)
    w('')
    w('## (B) ITS SOURCES AND THE MATCH:')
    w('  the canon`s section XXIII heading: %d row(s) %s' % (len(canon), ' '.join(':%d' % i for i, _l in canon)))
    w('  THE FINDINGS (%s):' % ', '.join(findings))
    for n, a, b in named:
        w('    %s: rows of SPIRAL_MAP.md naming it %d ; rows of REGISTRY.md naming it %d' % (n, a, b))
    w('    the search`s positive control, rows of SPIRAL_MAP.md naming Epstein by the same reader: %d' % map_pc)
    w('    stage: %s (%s)' % (stage, 'a row of the maps names a finding' if seated else
                               'no row or block of the maps names any of them: by the canon`s (B), "no seat in the cluster table", keystone none yet'))
    w('  THE EPSTEIN INSTANCE`S RECORDS, WHERE THE SITTING WROTE [R1] AND [R3] (relay data/b754_sitting.txt):')
    w('    SPIRAL_MAP.md, the cluster row seated at b750: %s ; naming the keystone %s and the sibling anchor %s: %s'
      % (' '.join(':%d' % i for i, _l in seat) or 'NONE', KEYSTONE, SIBLING, 'YES' if seat_ok else 'NO'))
    w('    the cluster table (SPIRAL_MAP.md :266-:276), its cluster rows %d (the control: the table read, not empty)' % len(crow))
    for r, x in zip(('1.5c-21', '1.5c-22', '1.5c-23'), reg):
        w('    REGISTRY.md, rows of %s: %s' % (r, ' '.join(':%d' % i for i, _l in x) or 'NONE'))
    w('    the keystone`s dated notes: %s ; b754`s among them (%r): %s ; its whole text read to section 9`s heading %s, %d rows'
      % (' '.join(':%d' % i for i, _l in knotes) or 'NONE', B754_NOTE, ' '.join(':%d' % i for i, _l in k754) or 'NONE',
         ' '.join(':%d' % i for i, _l in k9) or 'NONE', len(kall_rows)))
    w('    the names b754`s note carries: %s (the author`s answer for [R3] cited; no finding`s bank among them)' % (', '.join(n754) or 'NONE'))
    w('    the findings matched in the keystone`s text (linematch.stage): %s ; the positive control, rows naming Epstein by the same reader: %d' % (', '.join(hit) or 'NONE', k_pc))
    w('    the match`s positive control, a name the keystone carries (zq_offline_zero) read by the same call: %s, matched %s' % (pc_st, ', '.join(pc_hit) or 'NONE'))
    w('    [R1] wrote a cross-reference line to INSTRUMENTS (I-109) and [R3] the keystone`s two headings and its dated note; record lines, no finding entered')
    w('    in the keystone; sections 6 to 8 are written after the walk and the build ((R364)(10)).')
    w('  (R364)(4)(iii) to (v) and the cluster export were carried by (8)`s order and are no finding of this act.')
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
    w('## (D) THE TRAIL, by (R364)(7) and (8), carried to the walk`s act and named there:')
    w('  the navigator`s candidate statements (a) to (h) of data/b753_registrations.txt, each to be reproduced with its planted error; the build of')
    w('  T0 then T1 (data/b752_attribution_plan.txt); the reproduction`s four rows NOT RUN with their prices; W-ORD-VISIBILITY, carried not clean;')
    w('  the draft held at v5; and, by (8)`s order, the cluster export, (4)(iv)`s reading of the navigator`s descriptions, (4)(iii), [R2], [L9] to')
    w('  [L13], with [C1], (4)(v), [B1], [B3] and [H1]`s held part. Nothing built and nothing computed this act.')
    w('')
    w('## (R) THE READS (the PLACE-papers working tree printed as <PLACE-papers>, its path held by tools/standing/orders.py alone):')
    pp_forms = sorted({PP, PP.replace('\\', '/'), PP.replace('/', '\\')}, key=len, reverse=True)
    for l in out:
        for f in pp_forms:
            l = l.replace(f, '<PLACE-papers>')
        R.append(l)
    w('')
    masked = not any(f in '\n'.join(R) for f in pp_forms)              # ### the bank carries no path of the PLACE-papers tree
    w('### the PLACE-papers tree`s path in this bank: %s (its forms sought %d; the reads above carry <PLACE-papers> %d times)'
      % ('ABSENT' if masked else 'PRESENT', len(pp_forms), '\n'.join(R).count('<PLACE-papers>')))
    good = (masked and len(canon) == 1 and seat_ok and len(crow) >= 9 and reg_ok and len(knotes) >= 1 and len(k754) == 1 and len(k9) == 1 and kall_rows
            and k_pc > 0 and pc_st == 'SYNTHESISED' and map_pc > 0 and len(f2_rows) == 1 and good_c and not hit)
    w('### ### **THE LINE: COMPOSED ; FROM REGISTRY AND SPIRAL_MAP WITH THE MATCH, AFTER THE SITTING`S WRITES ; NO SEAT FOR THE READS OR THE SITTING ; '
      'KEYSTONE NONE YET ; STAGE %s ; MATCHED %d OF %d ; THE EPSTEIN KEYSTONE`S b754 NOTE AT %s READ, NO FINDING`S NAME IN IT ; THE EARLIER LINES READ '
      'AGAIN %d, NONE REWRITTEN ; %s.**'
      % (stage, len(hit), len(findings), ' '.join(':%d' % i for i, _l in k754) or 'NONE', len(EARLIER), 'ALL AS READ' if good else 'NOT ALL AS READ'))
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
