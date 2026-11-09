"""b749 Component 3, (R359)(4): THE INTEGRATION LINE FOR THIS ACT'S ENTRY, read from REGISTRY d1-1 and SPIRAL_MAP through relaypath.

The cluster, the deposit line (REGISTRY d1-1); the keystone, the monograph A_Place_to_Stand; the stage as the maps read, by the stages of
data/b746_integration_draft.txt (B): CLUSTERED where a REGISTRY row or a dated note to one names the finding; SYNTHESISED only where the
keystone carries it; DEPOSITED only where a deposited version of the keystone carries it. Every map read through relaypath.rows_of/grep_of,
which refuse a path the repository does not track. Carried to b750: data/b746_integration_draft.txt (md5 9e760351), the README :164 item,
the 1.5c-21 dated note. The literature claim about the b745 box stays unbanked.

usage: python -X utf8 -u tools/b749_line.py dry|write
"""
import hashlib
import io
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'standing'))
import relaypath as RP  # noqa: E402

RELAY = 'D:/relay'
PP = 'D:/MY-DOwnloads/PLACE-papers'
BANK = os.path.join(RELAY, 'data', 'b749_line.txt')
DRAFT = 'data/b746_integration_draft.txt'
DRAFT_MD5 = '9e760351971eab06b176176dc02643ab'
FINDING = ('23228113', 'Dated note, b749')   # ### the finding's needles: the draft's id, the act's dated note
KEYSTONES = ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')


def main(mode):
    out, R = [], []
    w = R.append
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    w('b749 -- (R359)(4): THE LINE: THE INTEGRATION LINE FOR THIS ACT`S ENTRY, FROM REGISTRY d1-1 AND SPIRAL_MAP, THE CARRIED ITEMS NAMED (%s)' % stamp)
    w('')
    w('### every map read from the PLACE-papers working tree through tools/standing/relaypath.py (rows_of, grep_of: a path the repository does not')
    w('### track is refused); the reads printed under (R); nothing written to the canon; no Zenodo call; the stages those of %s (B).' % DRAFT)
    w('')
    # ---- (B) the sources
    d1 = RP.grep_of(PP, 'REGISTRY.md', '| d1-1 |', out=out)
    note = RP.grep_of(PP, 'REGISTRY.md', FINDING[1], out=out)
    names_finding = [(i, l) for i, l in note if FINDING[0] in l and 'd1-1' in l and 'discarded' in l]
    sm_dep = RP.grep_of(PP, 'SPIRAL_MAP.md', 'A Place to Stand', out=out)
    sm_key = RP.grep_of(PP, 'SPIRAL_MAP.md', 'A_Place_to_Stand.md', out=out)
    sm_d11 = RP.grep_of(PP, 'SPIRAL_MAP.md', '`d1-1`', out=out)
    ctab = RP.rows_of(PP, 'SPIRAL_MAP.md', 264, 286, out=out)
    crow = [l for l in ctab if l.startswith('| **')]
    carry = []
    for k in KEYSTONES:
        hits = [h for n in FINDING for h in RP.grep_of(PP, k, n, out=out)]
        pc = len(RP.grep_of(PP, k, 'Place to Stand', out=out))   # ### the positive control: the same reader finds the title in the same file
        carry.append((k, len(hits), pc))
    readme = RP.rows_of(PP, 'README.md', 164, 164, out=out)
    rr = RP.grep_of(PP, 'REGISTRY.md', '1.5c-21', out=out)
    dm = hashlib.md5(io.open(os.path.join(RELAY, DRAFT), 'rb').read()).hexdigest()

    ok_d1 = len(d1) == 2 and d1[0][1].startswith('| d1-1 | A Place to Stand (monograph)')
    ok_note = len(names_finding) == 1
    ok_key = bool(sm_key) and any('Methodology' in l for _i, l in sm_key)
    ok_tab = len(crow) >= 1
    carried_nowhere = all(n == 0 for _k, n, _p in carry)
    ok_pc = all(p > 0 for _k, _n, p in carry)
    stage = ('CLUSTERED' if ok_note else 'BANKED') if carried_nowhere else 'SYNTHESISED'
    line = 'INTEGRATION: cluster the deposit line (REGISTRY d1-1) ; keystone A_Place_to_Stand (the monograph) ; stage %s' % stage

    w('## (A) THE LINE, IN THE FORM OF (R356)(6) (relay %s :11):' % DRAFT)
    w('      INTEGRATION: cluster <name> ; keystone <file or none yet> ; stage <BANKED | CLUSTERED | SYNTHESISED | DEPOSITED>')
    w('  the line for b749`s entry, its last line:')
    w('      ' + line)
    w('')
    w('## (B) ITS SOURCES:')
    w('  REGISTRY.md, the rows of d1-1 (by the cell "| d1-1 |"): %d' % len(d1))
    for i, l in d1:
        w('      :%d  %s ...' % (i, l[:90]))
    w('      the first the monograph`s row ("| d1-1 | A Place to Stand (monograph)"): %s' % ('YES' if ok_d1 else 'NO'))
    w('  REGISTRY.md, the act`s dated note naming the finding (the draft 23228113 discarded, to row d1-1): %d' % len(names_finding))
    for i, l in names_finding:
        w('      :%d  %s ...' % (i, l[:110]))
    w('  SPIRAL_MAP.md, the rows naming the monograph by its title: %s' % ', '.join(':%d' % i for i, _l in sm_dep))
    w('  SPIRAL_MAP.md, the rows naming A_Place_to_Stand.md: %s ; one in the cluster table`s Methodology row (a keystone-class document by b388): %s'
      % (', '.join(':%d' % i for i, _l in sm_key), 'YES' if ok_key else 'NO'))
    w('  SPIRAL_MAP.md, the rows naming REGISTRY row `d1-1`: %s' % ', '.join(':%d' % i for i, _l in sm_d11))
    w('  the cluster table (SPIRAL_MAP.md :264-:286), its cluster rows %d (the control: the table read, not empty)' % len(crow))
    w('  the keystone`s files, the rows carrying the finding (needles %s):' % ' , '.join(repr(n) for n in FINDING))
    for k, n, p in carry:
        w('      %s: %d (the positive control, rows naming "Place to Stand" by the same reader: %d)' % (k, n, p))
    w('  stage: the finding named by a dated note to REGISTRY d1-1 (CLUSTERED); carried by no file of the keystone, the working copy or the')
    w('  deposited v1.1.2 copy (not SYNTHESISED, not DEPOSITED): %s' % stage)
    w('')
    w('## (C) CARRIED TO THE SYNTHESIS SITTING AT b750, UNCHANGED:')
    w('  %s md5 %s against %s: %s' % (DRAFT, dm, DRAFT_MD5[:12], 'EQUAL' if dm == DRAFT_MD5 else 'DIFFERS'))
    w('  README.md :164, the deposit note, untouched this act ((R359)(2)(v)); it reads: %s' % readme[0][:150])
    w('  the 1.5c-21 dated note (whether REGISTRY 1.5c-21 should carry the grade, b748 defect (i)): carried; REGISTRY rows naming 1.5c-21 now %d,'
      % len(rr))
    w('  no note to the row written this act')
    w('')
    w('## (D) THE LITERATURE CLAIM ABOUT THE BOX OF b745: unbanked, in no door, until a search is banked; nothing searched this act.')
    w('')
    w('## (R) THE READS:')
    R.extend(out)
    w('')
    good = ok_d1 and ok_note and ok_key and ok_tab and ok_pc and dm == DRAFT_MD5 and len(readme) == 1
    w('### ### **THE LINE: COMPOSED ; FROM REGISTRY d1-1 AND SPIRAL_MAP ; KEYSTONE A_Place_to_Stand ; STAGE %s ; THE CANON TEXT CARRIED, md5 %s %s ; '
      'THE README ITEM CARRIED ; THE 1.5c-21 NOTE CARRIED ; %s.**' % (stage, dm[:12], 'EQUAL' if dm == DRAFT_MD5 else 'DIFFERS',
                                                                         'ALL AS READ' if good else 'NOT ALL AS READ'))
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
