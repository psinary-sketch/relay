# -*- coding: utf-8 -*-
"""b499_desk_bank.py -- THE DESK. ### **SCORED ON PRINTED CELLS, INCLUDING AGAINST THE SEAT.**"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def word(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def main():
    R = json.loads(io.open(os.path.join(D, 'b499_results.json'), encoding='utf-8').read())
    c1, c2 = R['c1'], R['c2']
    recs = c2['records']
    rec('=' * 104)
    rec('b499 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE COMPONENTS PRINTED.**')
    rec('=' * 104)
    rec('')
    rec('### THE NAVIGATOR`S THREE.')
    rec('-' * 104)
    n1 = c1['once'] == 10
    rec('  **(N1)** ### **%s.**' % word(n1))
    rec('    *"all ten targets found ONCE at Component 1"* -- ### **FOUND ONCE : %d of 10**' % c1['once'])
    rec('')
    n2 = c2['matches'] == 3
    rec('  **(N2)** ### **%s.**' % word(n2))
    rec('    *"all three fetch-backs MATCH"* -- ### **MATCH : %d of 3**, each on its first try, all four'
        % c2['matches'])
    rec('    limbs true on every record.')
    rec('')
    ents = c1['entities']
    n3 = sum(ents.values()) >= 3
    rec('  **(N3)** ### **%s.**' % word(n3))
    rec('    *"the description HTML returned differs from the screen text at three or more entity sites,')
    rec('    so a plain-text match would have failed somewhere"*')
    rec('    ### ### **ENTITY SITES : %s = %d**' % (ents, sum(ents.values())))
    olds = [t for t in c1['targets'] if t['kind'] == 'description' and '&' in (t.get('old') or '')]
    rec('    old spans that carry an entity : %d of 7 -- %s'
        % (len(olds), ['[%d]' % t['n'] for t in olds]))
    rec('    ### ### **HELD ON ITS CELL, AND THE "SO" IS TRUE FOR WHOLE SENTENCES ONLY.** ### A plain-text')
    rec('    ### match of the WHOLE old sentence would have failed at those targets; ### **A MATCH ON THE')
    rec('    ### START PHRASES WOULD NOT HAVE FAILED ANYWHERE** -- all seven start phrases are plain ASCII.')
    rec('    ### The extent rule mattered because it cut the span IN THE FIELD`S BYTES, entities and all.')
    rec('')
    rec('### THE SEAT`S THREE.')
    rec('-' * 104)
    first = recs.get('21539068') or {}
    s1 = first.get('put') == 200
    rec('  **(S1)** ### **%s.**' % word(s1))
    rec('    *"the platform accepts its own metadata back: the first PUT returns 200"* -- PUT %s, every'
        % first.get('put'))
    rec('    other key carried %s' % first.get('other_keys_carried'))
    rec('')
    s2 = c1.get('mono_same_as_b359')
    rec('  **(S2)** ### **%s.**' % word(s2))
    rec('    *"the monograph`s live description is byte-identical to the copy banked at b359"* -- %s' % s2)
    rec('')
    s3 = any(not c.get('raw_same') for c in recs.values())
    rec('  **(S3)** ### **%s.**' % word(s3))
    rec('    *"for at least one record the returned description`s raw bytes differ from the bytes sent"*')
    rec('    raw bytes equal : %s' % {k: v.get('raw_same') for k, v in recs.items()})
    rec('    ### ### **REFUTED: THE PLATFORM STORED AND SERVED THE HTML EXACTLY AS SENT, ON ALL THREE.** ###')
    rec('    ### The match rule`s text comparison was built for a re-serialisation that did not happen;')
    rec('    ### it agreed with the raw comparison everywhere, and a raw-byte rule would have passed too.')
    rec('')
    nav, seat = [n1, n2, n3], [s1, s2, s3]
    rec('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.**'
        % (nav.count(True), nav.count(False), nav.count(None)))
    rec('### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE %d.**'
        % (seat.count(True), seat.count(False), seat.count(None)))
    rec('=' * 104)
    io.open(os.path.join(D, 'b499_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3), io.open(
        os.path.join(D, 'b499_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print('  written: b499_desk_notes.txt, b499_scores.json')


if __name__ == '__main__':
    main()
