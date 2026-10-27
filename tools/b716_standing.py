# -*- coding: utf-8 -*-
"""b716_standing.py -- (R326)(2) and (6): THE STANDING CLAUSES AT v5, written at step zero as data/standing_clauses_v5.txt -- v4 unchanged (its 68
rows copied from data/standing_clauses_v4.txt byte for byte, its LINE sections and its row lines as banked) with (R326)(2)'s rows appended as
numbered rows (69)-(72) -- the three tiers of a move and the visibility map, each the ruling's own words cut from (R326)(2) as banked (relay
data/b716_ferry.txt :9) -- then (R326)(6)'s rows (73)-(78) -- the row that governs the deltas and the five deltas (i)-(v), each cut from
(R326)(6) as banked (:17), each delta carrying its control within it -- and row (79), THE CLOSE IN ONE ORDER AT v5, v4's row (68) with the two
steps delta (iii) names given their evidence as the seal's (the seat's composition, for the author's strike; where a row and an earlier row
speak to one object the later row is the version's reading); and the control: v5's rows read back by b710's parser (tools/b710_standing.py
parse), its first 68 equal to v4's row for row, each cut row equal to its span of the ferry, the version line 5, a NEG copy with one delta
altered differing.
Carried from tools/b715_standing.py by diff (data/b716_carry_standing.txt) and rewritten whole by the Write tool: the base v3 -> v4, the bank
v4 -> v5, two cut lines (:9, :17) in place of one, the heads and stops of (R326)(2) and (6), the order row at v5, the NEG alteration on delta
(ii), the version 4 -> 5.

### THE CUTS: (R326)(2) at :9 of the banked ferry, from "TIER ONE, RESEARCH MOVES:" to "TIER TWO", "TIER TWO" to "TIER THREE", "TIER THREE" to
### "THE VISIBILITY MAP,", that to the line's end; (R326)(6) at :17, from "(6) THE CLOSE REPAIRED BY CLASS" (the governing row) to "(i) THE
### AUTHOR’S WORD AFTER THE SEAL", each numeral's head to the next, (v) to the line's end. Each row: KIND STANDING, SEP STOP (the last END).
### Routes: `write [dry]` -> data/standing_clauses_v5.txt ; `control [dry]` -> data/b716_standing_control.txt (.json). Writes only those banks.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b710_standing as S1   # noqa: E402  ### b710's parser and re-assembly, imported unchanged

NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

V1, BANK, FERRY = 'standing_clauses_v4.txt', 'standing_clauses_v5.txt', 'b716_ferry.txt'
# ### each cut: (the ferry's line, the line's opening, the heads in order, the section's title, the source tag, the numerals)
CUTS = (
    (9, '(2) THE THREE TIERS OF A MOVE', ('TIER ONE, RESEARCH MOVES:', 'TIER TWO, CURRENCY MOVES:', 'TIER THREE, DEPOSIT AND PUBLICATION:', 'THE VISIBILITY MAP,'),
     '(R326)(2), the three tiers of a move and the visibility map', 'SOURCE (R326)(2)', ('tier one', 'tier two', 'tier three', 'the visibility map')),
    (17, '(6) THE CLOSE REPAIRED BY CLASS', ('(6) THE CLOSE REPAIRED BY CLASS', '(i) THE AUTHOR’S WORD AFTER THE SEAL', '(ii) THE ACT’S FIGURES FROM ONE SOURCE',
                                           '(iii) EVERY STEP OF THE CLOSE IN THE ORDER', '(iv) THE STANDING ROWS ENFORCED BY THE HARNESS', '(v) ONE LETTERING'),
     '(R326)(6), the close repaired by class (the deltas of v5)', 'SOURCE (R326)(6)', ('governing', 'i', 'ii', 'iii', 'iv', 'v')),
)
VERSION = 5
NEG_FROM, NEG_TO = 'no figure carried as a constant', 'a figure carried as a constant'   # ### delta (ii), altered in the NEG copy

# ### row (79): THE CLOSE IN ONE ORDER AT v5 -- v4's row (68) with delta (iii)'s two steps given their evidence as the seal's: the root route's dry
# ### run READY True and the suite's combined pre-run bank, each read by the seal before it writes (the seat's composition, for the author's strike).
ORDER = (
    ('standing figures', 'the four standing figures against the previous act`s baselines', 'data/<act>_standing_figures.json'),
    ('rootdry', 'the root route`s dry run, READY True, the seal`s evidence ((R326)(6)(iii))', 'data/<act>_root_banks_dry.json reading ready True'),
    ('closing dry', 'the closing tool`s dry run, its head line rebuilt from the remotes', 'data/<act>_closing_dry.txt'),
    ('scores dry', 'the score routes` dry form', 'data/<act>_scores_dry.txt'),
    ('gate', 'the gate, every commit of its step listed on its step row', 'data/<act>_reg_gate.txt'),
    ('lock', 'the lock', 'data/<act>_lockgate.json'),
    ('prerun', 'the suite`s pre-run on the previous act`s banks and at HEAD, in seven parts, and its combined bank, the seal`s evidence ((R326)(6)(iii))',
     'data/<act>_arms_prerun.txt'),
    ('seal', 'the seal, its NEG controls shown failing, refusing while [2] or [7] lacks its evidence', 'data/<act>_seal_hashes.json'),
    ('scores', 'the scores, written once', 'data/<act>_scores.json'),
    ('prompt', 'the root`s prompt, put once, and the answers bank, written once', 'data/<act>_author_answers.txt'),
    ('report', 'the standing report`s bank, its lines in footing order', 'data/<act>_report.txt'),
    ('entry', 'the FINDINGS entry, pushed', 'data/<act>_findings.json'),
    ('table', 'the final table', 'data/<act>_table_final.json'),
    ('root', 'the root, computed last of the banks it names', 'data/<act>_act_root.json'),
    ('trail', 'the trail carrying the root', 'data/<act>_trail.json'),
    ('desk', 'the desk', 'data/<act>_desk_notes.txt'),
    ('prepush', 'the pre-push suite in seven parts', 'data/<act>_checks.txt'),
    ('components', 'the components bank', 'data/<act>_components.txt'),
    ('record', 'the record commit and its pushes, each push with its capture and its repository`s visibility', 'data/<act>_relay_push-<act>-record_push_out.txt'),
    ('postpush', 'the post-push suite in seven parts', 'data/<act>_checks_postpush.txt'),
    ('events', 'the events bank (an event found after it appended by the Edit tool before the closing)', 'data/<act>_events.txt'),
    ('scores close', 'scores close', 'data/<act>_scores_close.json'),
    ('mirror', 'the mirror after the root and the last PLACE-papers push, CLEAN with the root line', 'data/<act>_mirror.txt'),
    ('report scores', 'the standing report`s scores line, printed after the root and written nowhere', 'the commands bank'),
    ('closing', 'the closing and its push, captured', 'data/<act>_closing.txt'),
)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def cut(fline, opening, heads, numerals):
    """[(numeral, text)] -- each head to the next head, the last to the line's end, verbatim from the banked ferry's line <fline>."""
    line = S1.rd(FERRY).split(NL)[fline - 1]
    if not line.startswith(opening):
        sys.exit('### THE BANKED FERRY`S :%d DOES NOT OPEN %r -- NOTHING WRITTEN' % (fline, opening))
    idx = [line.find(h) for h in heads] + [len(line)]
    if min(idx) < 0 or idx != sorted(idx):
        sys.exit('### A HEAD NOT FOUND IN ORDER ON :%d (%s) -- NOTHING WRITTEN' % (fline, idx))
    return [(numerals[k], line[idx[k]:idx[k + 1]].strip()) for k in range(len(heads))]


def cuts():
    """[(fline, title, tag, [(numeral, text)])] for both cuts."""
    return [(fl, title, tag, cut(fl, op, heads, nums)) for fl, op, heads, title, tag, nums in CUTS]


def order_text():
    return ('THE CLOSE IN ONE ORDER AT v5, THE STEPS NUMBERED (the seat`s row under (R326)(6)(iii), for the author`s strike; v4`s row (68) with the '
            'root route`s dry run READY True and the combined pre-run bank named as the evidence the seal requires): a step is done when its '
            'evidence stands, <act> the act`s name, and each closing tool reads its own step here and refuses while a lower step`s evidence is '
            'absent: ' + '; '.join('[%d] %s (%s)' % (k + 1, t, ev) for k, (_n, t, ev) in enumerate(ORDER)) + '.')


def v1_body():
    """v4's lines from its first LINE section to its last row (the head and the verdict line excluded), byte for byte."""
    L = S1.rd(V1).split(NL)
    a = next(i for i, l in enumerate(L) if l.startswith('## LINE '))
    b = max(i for i, l in enumerate(L) if l.startswith('      '))
    return L[a:b + 1]


def text_of():
    cs = cuts()
    body = v1_body()
    rows1 = S1.parse(S1.rd(V1))
    n0 = rows1[-1][0]
    n2 = len(cs[0][3])
    n6 = len(cs[1][3])
    L = ['b716 -- THE STANDING CLAUSES, VERSION 5, WRITTEN ONCE AT STEP ZERO UNDER (R326)(2) AND (6): VERSION 4 UNCHANGED (relay data/standing_clauses_v4.txt, its rows '
         '(1)-(%d) copied byte for byte) WITH (R326)(2)`S FOUR ROWS AS ROWS (%d)-(%d), (R326)(6)`S GOVERNING ROW AND FIVE DELTAS AS ROWS (%d)-(%d) AND THE CLOSE`S '
         'ORDER AT v5 AS ROW (%d) (%s)' % (n0, n0 + 1, n0 + n2, n0 + n2 + 1, n0 + n2 + n6, n0 + n2 + n6 + 1, utc()), '',
         'VERSION: 5',
         'THE CITATION FORM: a ferry names "standing clauses v5" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
         '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
         '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(%d) are v4`s, unchanged. Rows (%d)-(%d) are (R326)(2)`s three tiers and visibility map, cut' % (n0, n0 + 1, n0 + n2),
         '### from relay data/b716_ferry.txt :9; row (%d) governs the deltas and rows (%d)-(%d) are (R326)(6)`s five deltas, cut from :17, each delta' % (
             n0 + n2 + 1, n0 + n2 + 2, n0 + n2 + n6),
         '### carrying its control in its own clause ("control: ..."); row (%d) is the close`s order at v5, v4`s row (68) with delta (iii)`s two steps' % (n0 + n2 + n6 + 1),
         '### given their evidence as the seal`s, the seat`s composition, for the author`s strike. The repairs` diffs and printed controls are the',
         '### repairs`, not rows. Where a row and an earlier row speak to one object the later row is the version`s reading; no earlier row is edited.', '']
    L += body
    n = n0
    for fl, title, tag, dl in cs:
        L += ['', '## LINE %d OF data/b716_ferry.txt -- %s' % (fl, title)]
        for num, t in dl:
            n += 1
            tg = '%s, the row that governs the deltas' % tag if num == 'governing' else ('%s(%s)' % (tag, num) if num in ('i', 'ii', 'iii', 'iv', 'v') else '%s, %s' % (tag, num))
            L.append('  (%d) STANDING STOP %s ; first carried in data/b716_ferry.txt under (R326)' % (n, tg))
            L.append('      ' + t)
    L += ['', '## THE CLOSE`S ORDER AT v5 -- (R326)(6)(iii): the steps as one numbered row (the seat`s row, for the author`s strike)']
    L.append('  (%d) STANDING END SOURCE (R326)(6)(iii), the seat`s row ; written at b716 under (R326)' % (n + 1))
    L.append('      ' + order_text())
    L += ['', '### ### **ROWS %d ; v4`S ROWS %d UNCHANGED ; THE THREE TIERS AND THE VISIBILITY MAP ; THE GOVERNING ROW AND FIVE DELTAS (THE AUTHOR`S WORD AFTER '
          'THE SEAL, THE ACT`S FIGURES FROM ONE SOURCE, EVERY STEP OF THE CLOSE IN THE ORDER, THE STANDING ROWS ENFORCED BY THE HARNESS, ONE LETTERING), EACH '
          'DELTA WITH ITS CONTROL ; THE CLOSE`S ORDER AT v5, %d STEPS ; VERSION 5.**' % (n + 1, n0, len(ORDER))]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b716', p, None)


def write(*a):
    L = text_of()
    if 'dry' in a:
        print(NL.join(L[:12] + L[-34:]))
        return
    p = os.path.join(D, BANK)
    import subprocess
    tracked = subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch', 'data/' + BANK], capture_output=True).returncode == 0
    if tracked or os.path.exists(p):
        sys.exit('### data/%s EXISTS%s -- A VERSION IS WRITTEN ONCE; NOTHING WRITTEN' % (BANK, ' AND IS COMMITTED' if tracked else ''))
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


def control(*a):
    v1, v2 = S1.rd(V1), S1.rd(BANK)
    r1, r2 = S1.parse(v1), S1.parse(v2)
    cs = cuts()
    flat = [(fl, num, t) for fl, _ti, _tg, dl in cs for num, t in dl]
    n0 = len(r1)
    first_equal = r2[:n0] == r1
    v1_lines_equal = all(l in v2.split(NL) for l in v1_body())
    dres = []
    for k, (fl, num, t) in enumerate(flat):
        row = r2[n0 + k] if len(r2) > n0 + k else None
        is_delta = fl == 17 and num != 'governing'
        dres.append(dict(n=n0 + 1 + k, line=fl, row=num, equal=bool(row) and row[4] == t, control_in=(not is_delta) or (bool(row) and 'control:' in row[4]), chars=len(t)))
    orow = r2[n0 + len(flat)] if len(r2) > n0 + len(flat) else None
    order_equal = bool(orow) and orow[4] == order_text()
    neg = v2.replace(NEG_FROM, NEG_TO, 1)
    neg_rows = S1.parse(neg)
    k_ii = next(k for k, (fl, num, _t) in enumerate(flat) if fl == 17 and num == 'ii')
    neg_equal = len(neg_rows) > n0 + k_ii and neg_rows[n0 + k_ii][4] == flat[k_ii][2]
    ver = re.search(r'^VERSION: (\d+)$', v2, re.M)
    ok = (first_equal and v1_lines_equal and all(d['equal'] and d['control_in'] for d in dres) and order_equal and len(r2) == n0 + len(flat) + 1
          and NEG_FROM in v2 and not neg_equal and bool(ver) and ver.group(1) == str(VERSION))
    L = ['b716 -- STEP ZERO, (R326)(2) AND (6): THE CONTROL OF THE STANDING CLAUSES v5 -- v4`S ROWS UNCHANGED, THE TEN CUT ROWS EQUAL TO THE RULING`S WORDS AND THE ORDER ROW (%s)' % utc(), '',
         '### rows are checks. v5 read back by b710`s parser (tools/b710_standing.py parse): %d rows ; v4 %d rows. The rows cut from relay data/b716_ferry.txt :9 and :17.' % (len(r2), n0),
         '### The NEG control: a copy of v5 with delta (ii)`s "%s" altered to "%s", its row compared again.' % (NEG_FROM, NEG_TO), '',
         '  v5`s rows (1)-(%d) equal to v4`s row for row (number, kind, separator, tag, clause, source line): %s' % (n0, first_equal),
         '  v4`s body lines (its LINE sections and rows) present in v5 line for line: %s' % v1_lines_equal]
    L += ['  (%d) :%d %s: equal to its span of the ferry %s ; its control within it %s ; %d characters' % (
        d['n'], d['line'], 'the governing row' if d['row'] == 'governing' else ('delta (%s)' % d['row'] if d['line'] == 17 else d['row']), d['equal'],
        d['control_in'] if (d['line'] == 17 and d['row'] != 'governing') else 'n/a (not a delta)', d['chars']) for d in dres]
    L += ['  (%d) the close`s order at v5: equal to the tool`s ORDER (%d steps) %s' % (n0 + len(flat) + 1, len(ORDER), order_equal),
          '  NEG: the altered copy`s delta (ii) equal to the ferry %s (wanted False ; the phrase present in v5 %s)' % (neg_equal, NEG_FROM in v2),
          '  VERSION %s (wanted %d)' % (ver.group(1) if ver else 'NONE', VERSION), '',
          '### ### **ROWS %d ; v4`S %d UNCHANGED %s ; ROWS CUT %d EQUAL %s ; THE ORDER ROW %s ; THE NEG COPY DIFFERS %s ; VERSION 5 %s ; THE CONTROL AS WANTED %s.**' % (
              len(r2), n0, first_equal and v1_lines_equal, len(dres), all(d['equal'] for d in dres), order_equal, not neg_equal, bool(ver) and ver.group(1) == str(VERSION), ok)]
    if 'dry' not in a:
        for name, data in (('b716_standing_control.txt', NL.join(L) + NL),
                           ('b716_standing_control.json', json.dumps(dict(at=utc(), rows=dres, first_equal=first_equal, v1_lines_equal=v1_lines_equal, neg_equal=neg_equal,
                                                                          order_equal=order_equal, n=len(r2), ok=ok), indent=1) + NL)):
            p = os.path.join(D, name)
            _membrane(p)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(data.encode('utf-8'))
            os.replace(p + '.tmp', p)
    print(NL.join(L[5:]))
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    fn = {'write': write, 'control': control}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b716_standing.py write [dry] | control [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
