# -*- coding: utf-8 -*-
"""b507_repairs.py -- (R117)(1) AND (3) INSIDE THE FOLD. ### `python tools/b507_repairs.py notes | fixtures`

### `notes`    -- ONE note APPENDED to each of `b477_components.txt`, `b502_components.txt`,
###               `b504_components.txt` (beside b506`s (R115)(1) note, which must already be there once), and
###               ONE to `b334_the_aim_map.txt` (beside the crossings); each prior byte string proved a TRUE
###               PREFIX of the result, and the lines removed counted. ### Refuses on a second run.
### `fixtures` -- the two repaired instruments exercised in BOTH POLARITIES on synthetic text and a temporary
###               ledger, never on a live registration or on `CORRESPONDENCE.md`; and the old bar-floor pattern
###               kept beside the new so the fixture can DISCRIMINATE (b347`s `gate_text` convention). ### A
###               census of every banked registration under both patterns is printed; it re-verdicts nothing.
"""
import glob
import io
import json
import os
import re
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R115 = 'ANNOTATION APPENDED AT b506 UNDER (R115)(1)'
MARK1 = 'NOTE APPENDED AT b507 UNDER (R117)(1)'
MARK3 = 'NOTE APPENDED AT b507 UNDER (R117)(3)'
RULE = '-' * 100

NOTE1 = NL.join(['', RULE,
    '### %s, 2026-09-24. ### THE TEXT ABOVE, AND b506`S ANNOTATION, ARE UNEDITED.' % MARK1, RULE,
    '### ### **BESIDE THE (R115)(1) NOTE ABOVE: b326`S DERIVED KERNEL CLOSES ON THE BANK COMPLETED AT b506 -- 93 OF 93 WIDE',
    '### CELLS VERIFIED (`relay/data/b506_c3.txt`, `b506_cells.jsonl`) -- WHILE b325`S DOES NOT.** ### The note above carries',
    '### (R115)(1)`s words that the kernel "does not close the explicit formula ... at any cell"; on the completed bank that holds',
    '### of b325`s kernel and not of the derived one. ### b325`s kernel was shown not to close at b504 (residual 0.53 to 9.4, on',
    '### the incomplete bank); the derived kernel is exactly twice it (b504); b506 ran the derived kernel alone. ### The Epstein',
    '### margins above were read on the incomplete bank, and the (R115)(1) note above stands on them.', RULE, ''])

NOTE3 = NL.join(['', RULE,
    '### %s, 2026-09-24. ### THE TEXT ABOVE IS UNEDITED.' % MARK3, RULE,
    '### ### **THE EPSTEIN CROSSINGS OF ANSWER (3) AND OF THE CHART-READY BLOCK ABOVE ARE UNVERIFIED.** ### They were computed',
    '### on the Epstein bank that b506`s count below height 150 found short by 30 zeros (180 against the bank`s 150;',
    '### `relay/data/b506_c2_results.json`). ### They stay UNVERIFIED until re-read on the completed bank, and no crossing',
    '### width is cited until then.', RULE, ''])

TARGETS = [('b477_components.txt', MARK1, NOTE1, True), ('b502_components.txt', MARK1, NOTE1, True),
           ('b504_components.txt', MARK1, NOTE1, True), ('b334_the_aim_map.txt', MARK3, NOTE3, False)]


def notes():
    out = []
    for name, mark, note, needs_r115 in TARGETS:
        p = os.path.join(D, name)
        before = open(p, 'rb').read()
        t = before.decode('utf-8')
        if mark in t:
            sys.exit('### REFUSED -- %s ALREADY CARRIES THE NOTE; NOTHING WRITTEN.' % name)
        if needs_r115 and t.count(R115) != 1:
            sys.exit('### REFUSED -- %s DOES NOT CARRY b506`S (R115)(1) NOTE EXACTLY ONCE.' % name)
        add = note.encode('utf-8')
        if not before.endswith(b'\n'):
            add = b'\n' + add
        open(p, 'ab').write(add)
        after = open(p, 'rb').read()
        bl, al = before.split(b'\n'), after.split(b'\n')
        out.append(dict(file=name, written=len(after) - len(before), prefix=after.startswith(before),
                        removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b) - (0 if before.endswith(b'\n') else 1),
                        marks=after.decode('utf-8').count(mark),
                        after_r115=(not needs_r115) or after.decode('utf-8').index(mark) > after.decode('utf-8').index(R115)))
        print('  %(file)-24s written %(written)4d ; prefix %(prefix)s ; removed %(removed)d ; marks %(marks)d ; after the (R115) note %(after_r115)s' % out[-1])
    d = (json.dumps(out, indent=1) + NL).encode('utf-8')
    open(os.path.join(D, 'b507_notes.json.tmp'), 'wb').write(d)
    os.replace(os.path.join(D, 'b507_notes.json.tmp'), os.path.join(D, 'b507_notes.json'))
    return 0


# ### THE BAR-FLOOR PATTERN AS b347 BUILT IT, KEPT HERE SO THE FIXTURE CAN DISCRIMINATE OLD FROM NEW.
_NUM = r'\d+(?:\.\d+)?[eE][-+]?\d+'
THRESHOLD_B347 = re.compile(
    r'(?:\bbar\b|\bthreshold\b|\btolerance\b|\bagree(?:s|d)?\s+to\b|\bwithin\b|<=|≤)'
    r'[^\n]{0,80}?`?' + _NUM, re.I)


def fixtures():
    import registration_gate as RG
    import corr_row as CR
    res = dict()
    # ### (A) THE BAR-FLOOR ARM. ### b505`s own bar is the positive control, quoted from its sealed face.
    b505_face = io.open(os.path.join(D, 'b505_registration_2026-09-23.txt'), encoding='utf-8').read()
    b505_bar = [ln for ln in b505_face.split(NL) if '>= 1e-10' in ln]
    cases = [
        ('b505`s own sealed bar line, alone (the positive control)', (b505_bar[0] if b505_bar else ''), True),
        ('a bare `>=` bar', '### THE BAR: every cell must hold `|r| >= 1e-10`.', True),
        ('a bare `>` bar', '### THE CELL REFUSES when `|r| > 1e-9`.', True),
        ('a bare `≥` bar', '### THE CELL REFUSES when |r| ≥ 1e-9.', True),
        ('a `>=` bar with its floor beside it', '### THE BAR: `|r| >= 1e-10`, against a floor of `6.1e-11` the bank carries.', False),
        ('a `>` bar marked UNPRICED', '### THE CELL REFUSES when `|r| > 1e-9`. ### UNPRICED.', False),
        ('an arrow `->` beside a number (not a bar)', '### `ferry_scan.py` -> `b303_pins.py`, run at step zero; 3e-9 s.', False),
        ('an arrow `=>` beside a number (not a bar)', '### (a) => (b) at 2e-9.', False),
    ]
    rows = []
    for label, text, fires in cases:
        new = bool(RG.bar_floor_check(text)[0])
        old_thr = bool(THRESHOLD_B347.search(text))
        old = old_thr and not RG.FLOOR_WORD.search(text)
        rows.append(dict(case=label, expect_fire=fires, new_fires=new, old_fires=old, ok=(new == fires)))
    res['bar_floor'] = rows
    res['bar_floor_discriminates'] = any(r['new_fires'] and not r['old_fires'] for r in rows)
    res['bar_floor_carried_fixture'] = RG.bar_floor_self_test(False)
    res['b505_bar_found'] = bool(b505_bar)
    # ### the census: every banked registration, old pattern against new. ### IT RE-VERDICTS NOTHING.
    regs = sorted(glob.glob(os.path.join(D, 'b[0-9][0-9][0-9]*_registration_*.txt')))
    old_fire = new_fire = only_new = 0
    only_new_names = []
    for p in regs:
        t = io.open(p, encoding='utf-8', errors='replace').read()
        n = bool(RG.bar_floor_check(t)[0])
        o = any(THRESHOLD_B347.search(para) and not RG.FLOOR_WORD.search(para) for _s, para in RG._paragraphs(t))
        old_fire += o
        new_fire += n
        if n and not o:
            only_new += 1
            only_new_names.append(os.path.basename(p))
    res['census'] = dict(registrations=len(regs), fire_old=old_fire, fire_new=new_fire, fire_only_new=only_new,
                         only_new=only_new_names)
    # ### (B) THE ROW WRITER. ### A temporary ledger; the live ledger is never touched.
    tmp = tempfile.mkdtemp(prefix='b507cr_')
    p = os.path.join(tmp, 'CORRESPONDENCE_fixture.md')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(
        '| # | a | b | c | d | e |\n|:--|:--|:--|:--|:--|:--|\n| 1 | x | x | x | x | x |\n')
    before = open(p, 'rb').read()
    code_pipe, msg_pipe = CR.write_row(p, ['2', 'a cell carrying |r| <= B, whose pipes split it', 't', 'p', 'g', 's'])
    unchanged_pipe = open(p, 'rb').read() == before
    code_ok, _m = CR.write_row(p, ['2', 'a cell carrying ‖r‖ ≤ B', 't', 'p', 'g', 's'])
    grew = open(p, 'rb').read() != before
    carried_ok, carried_lines = CR.self_test(tmp)
    res['corr_row'] = dict(pipe_code=code_pipe, pipe_file_unchanged=unchanged_pipe, pipe_message=msg_pipe[:2],
                           clean_code=code_ok, clean_file_grew=grew, carried_self_test=carried_ok)
    ok = (all(r['ok'] for r in rows) and res['bar_floor_discriminates'] and res['bar_floor_carried_fixture']
          and res['b505_bar_found'] and code_pipe == 2 and unchanged_pipe and code_ok == 0 and grew and carried_ok)
    res['ok'] = ok
    L = ['=' * 104, 'b507 -- THE TWO REPAIRED INSTRUMENTS, EXERCISED IN BOTH POLARITIES. ### (R117)(1) AND (2).', '=' * 104,
         '### (A) `registration_gate.py` -- THE BAR-FLOOR ARM, NEW PATTERN AGAINST b347`S.',
         '    %-58s %-7s %-7s %-7s %s' % ('case', 'EXPECT', 'NEW', 'OLD', 'verdict')]
    for r in rows:
        L.append('    %-58s %-7s %-7s %-7s %s' % (r['case'][:58], 'FIRE' if r['expect_fire'] else 'QUIET',
                                                   'FIRE' if r['new_fires'] else 'QUIET', 'FIRE' if r['old_fires'] else 'QUIET',
                                                   'OK' if r['ok'] else '### WRONG'))
    L += ['    ### the new pattern fires where b347`s did not : %s' % res['bar_floor_discriminates'],
          '    ### b347`s carried fixtures (six cases) still pass : %s' % res['bar_floor_carried_fixture'],
          '    ### CENSUS, RE-VERDICTING NOTHING : %(registrations)d registrations ; fire under b347 %(fire_old)d ; under the repair %(fire_new)d ; newly firing %(fire_only_new)d' % res['census'],
          '      newly firing : %s' % (', '.join(res['census']['only_new']) or 'NONE'),
          '', '### (B) `corr_row.py` -- VALIDATE BEFORE WRITE, ON A TEMPORARY LEDGER.',
          '    POSITIVE CONTROL -- a cell carrying `|` : code %d (must be 2) ; file unchanged : %s' % (code_pipe, unchanged_pipe),
          '      its refusal : %s' % (msg_pipe[0] if msg_pipe else ''),
          '    NEGATIVE CONTROL -- the same cell with `‖`  : code %d (must be 0) ; file grew : %s' % (code_ok, grew),
          '    b488`s carried controls (a taken number refused, the next free accepted) : %s' % carried_ok,
          '', '### ### **VERDICT : %s**' % ('BOTH REPAIRS BEHAVE IN BOTH POLARITIES' if ok else 'NOT CLEAN'), '=' * 104]
    io.open(os.path.join(D, 'b507_fixtures.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    d = (json.dumps(res, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(os.path.join(D, 'b507_fixtures.json.tmp'), 'wb').write(d)
    os.replace(os.path.join(D, 'b507_fixtures.json.tmp'), os.path.join(D, 'b507_fixtures.json'))
    print(NL.join(L))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit({'notes': notes, 'fixtures': fixtures}[sys.argv[1]]())
