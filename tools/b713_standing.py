# -*- coding: utf-8 -*-
"""b713_standing.py -- (R323)(4): THE STANDING CLAUSES AT v4, written at step zero as data/standing_clauses_v4.txt -- v3 unchanged (its 60 rows
copied from data/standing_clauses_v3.txt byte for byte, its LINE sections and its row lines as banked) with (R323)(4)'s rows appended as
numbered rows (61)-(67) -- the row that governs the deltas and the six deltas (i)-(vi), each the ruling's own words cut from (R323)(4) as banked
(relay data/b713_ferry.txt :14), each delta's control the ruling's own clause within it -- and row (68), THE CLOSE IN ONE ORDER, the steps
numbered, which delta (vi) orders written "as one numbered row of the standing clauses" (the seat's composition from the ferry's Components 5-6
and b712's close, for the author's strike); and the control: v4's rows read back by b710's parser (tools/b710_standing.py parse), its first 60
equal to v3's row for row, each delta equal to its span of the ferry, the version line 4, a NEG copy with one delta altered differing.
Carried from tools/b712_standing.py by diff (data/b713_carry_standing.txt): the base v2 -> v3, the bank v3 -> v4, the ferry's line :11 -> :14,
the heads and the stop of (R323)(4), the governing row and the order row, the NEG alteration on delta (ii), the version 3 -> 4.

### THE CUT OF THE DELTAS: (R323)(4) at :14 of the banked ferry, from "The row that governs them:" to "(i) ONE LIST OF WRITES", and each numeral's
### head to the next ("(ii) EVERY COMMIT OF A STEP", "(iii) ONE COUNTER", "(iv) THE LOCK AS A MEMBRANE", "(v) A CAPTURE FOR EVERY PUSH", "(vi) THE
### CLOSE IN ONE ORDER"), the last to the sentence "Each repair’s diff in data/b713_tool_repairs.txt" (the diffs and the printed controls are the
### repairs', not rows of the clauses). Each row: KIND STANDING, SEP STOP (the last END), TAG SOURCE (R323)(4)...
### Routes: `write [dry]` -> data/standing_clauses_v4.txt ; `control [dry]` -> data/b713_standing_control.txt (.json). Writes only those banks.
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

# ### the ferry's (R323)(4) at :13: v4 was written (89bea621) when the bank carried the paste's outer BEGIN line and (4) stood at :14, the line
# ### v4's head and LINE section name; the bank was then cut to b712's form (the anchor to the tail, equal to the transcript) and (4) moved to
# ### :13 -- the reference in v4 is one line off, a defect of the seat's (data/b713_defects.txt); the rows' words are unchanged by the cut.
V1, BANK, FERRY, FLINE = 'standing_clauses_v3.txt', 'standing_clauses_v4.txt', 'b713_ferry.txt', 13
HEADS = ('The row that governs them:', '(i) ONE LIST OF WRITES', '(ii) EVERY COMMIT OF A STEP', '(iii) ONE COUNTER', '(iv) THE LOCK AS A MEMBRANE',
         '(v) A CAPTURE FOR EVERY PUSH', '(vi) THE CLOSE IN ONE ORDER')
STOP = ' Each repair’s diff in data/b713_tool_repairs.txt'
NUMERALS = ('governing', 'i', 'ii', 'iii', 'iv', 'v', 'vi')
VERSION = 4

# ### row (68): THE CLOSE IN ONE ORDER -- the seat's composition under delta (vi), for the author's strike. Each step names the evidence that
# ### shows it done (<act> the act's name); a closing tool reads its own step here and refuses while a lower step's evidence is absent.
ORDER = (
    ('standing figures', 'the four standing figures against the previous act`s baselines', 'data/<act>_standing_figures.json'),
    ('rootdry', 'the root route`s dry run, run once, READY', 'data/<act>_root_banks_dry.json'),
    ('closing dry', 'the closing tool`s dry run, its head line rebuilt from the remotes', 'data/<act>_closing_dry.txt'),
    ('scores dry', 'the score routes` dry form', 'data/<act>_scores_dry.txt'),
    ('gate', 'the gate, every commit of its step listed on its step row', 'data/<act>_reg_gate.txt'),
    ('lock', 'the lock', 'data/<act>_lockgate.json'),
    ('prerun', 'the suite`s pre-run on the previous act`s banks and at HEAD, in seven parts', 'data/<act>_prevrun_act.txt'),
    ('seal', 'the seal, its NEG controls shown failing', 'data/<act>_seal_hashes.json'),
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
    ('record', 'the record commit and its pushes, each push with its capture', 'data/<act>_relay_push-<act>-record_push_out.txt'),
    ('postpush', 'the post-push suite in seven parts', 'data/<act>_checks_postpush.txt'),
    ('events', 'the events bank (an event found after it appended by the Edit tool before the closing)', 'data/<act>_events.txt'),
    ('scores close', 'scores close', 'data/<act>_scores_close.json'),
    ('mirror', 'the mirror after the root and the last PLACE-papers push, CLEAN with the root line', 'data/<act>_mirror.txt'),
    ('report scores', 'the standing report`s scores line, printed after the root and written nowhere', 'the commands bank'),
    ('closing', 'the closing and its push, captured', 'data/<act>_closing.txt'),
)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def deltas():
    """[(numeral, text)] -- the governing row and the six deltas verbatim from the banked ferry's :14, each ending at its full stop."""
    line = S1.rd(FERRY).split(NL)[FLINE - 1]
    if not line.startswith('(4) THE CLOSE REPAIRED BY CLASS'):
        sys.exit('### THE BANKED FERRY`S :%d IS NOT (R323)(4) -- NOTHING WRITTEN' % FLINE)
    idx = [line.find(h) for h in HEADS] + [line.find(STOP)]
    if min(idx) < 0 or idx != sorted(idx):
        sys.exit('### A DELTA`S HEAD OR THE STOP NOT FOUND IN ORDER (%s) -- NOTHING WRITTEN' % idx)
    return [(NUMERALS[k], line[idx[k]:idx[k + 1]].strip()) for k in range(len(HEADS))]


def order_text():
    return ('THE CLOSE IN ONE ORDER, THE STEPS NUMBERED (the seat`s row under (R323)(4)(vi), for the author`s strike): a step is done when its '
            'evidence stands, <act> the act`s name, and each closing tool reads its own step here and refuses while a lower step`s evidence is '
            'absent: ' + '; '.join('[%d] %s (%s)' % (k + 1, t, ev) for k, (_n, t, ev) in enumerate(ORDER)) + '.')


def v1_body():
    """v3's lines from its first LINE section to its last row (the head and the verdict line excluded), byte for byte."""
    L = S1.rd(V1).split(NL)
    a = next(i for i, l in enumerate(L) if l.startswith('## LINE '))
    b = max(i for i, l in enumerate(L) if l.startswith('      '))
    return L[a:b + 1]


def text_of():
    dl = deltas()
    body = v1_body()
    rows1 = S1.parse(S1.rd(V1))
    n0 = rows1[-1][0]
    nd = len(dl)
    L = ['b713 -- THE STANDING CLAUSES, VERSION 4, WRITTEN ONCE AT STEP ZERO UNDER (R323)(4): VERSION 3 UNCHANGED (relay data/standing_clauses_v3.txt, its rows (1)-(%d) '
         'copied byte for byte) WITH THE GOVERNING ROW AND THE SIX DELTAS APPENDED AS ROWS (%d)-(%d) AND THE CLOSE`S ORDER AS ROW (%d) (%s)' % (
             n0, n0 + 1, n0 + nd, n0 + nd + 1, utc()), '',
         'VERSION: 4',
         'THE CITATION FORM: a ferry names "standing clauses v4" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
         '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
         '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(%d) are v3`s, unchanged. Row (%d) is the row that governs the deltas and rows (%d)-(%d) are' % (n0, n0 + 1, n0 + 2, n0 + nd),
         '### (R323)(4)`s six deltas, each the ruling`s own words cut from relay data/b713_ferry.txt :14, each delta carrying its control in its own',
         '### clause ("control: ..."); row (%d) is the close`s order that delta (vi) orders written as one numbered row, the seat`s composition, for the' % (n0 + nd + 1),
         '### author`s strike. The repairs` diffs and printed controls are the repairs`, not rows. Where a row and an earlier row speak to one object',
         '### the later row is the version`s reading; no earlier row is edited.', '']
    L += body
    L += ['', '## LINE %d OF data/b713_ferry.txt -- (R323)(4), the close repaired by class (the deltas of v4)' % FLINE]
    for k, (num, t) in enumerate(dl):
        tag = 'SOURCE (R323)(4), the row that governs the deltas' if num == 'governing' else 'SOURCE (R323)(4)(%s)' % num
        L.append('  (%d) STANDING STOP %s ; first carried in data/b713_ferry.txt under (R323)' % (n0 + 1 + k, tag))
        L.append('      ' + t)
    L += ['', '## THE CLOSE`S ORDER -- (R323)(4)(vi): the steps as one numbered row (the seat`s row, for the author`s strike)']
    L.append('  (%d) STANDING END SOURCE (R323)(4)(vi), the seat`s row ; written at b713 under (R323)' % (n0 + nd + 1))
    L.append('      ' + order_text())
    L += ['', '### ### **ROWS %d ; v3`S ROWS %d UNCHANGED ; THE GOVERNING ROW AND SIX DELTAS (ONE LIST OF WRITES, EVERY COMMIT OF A STEP, ONE COUNTER, THE LOCK '
          'AS A MEMBRANE, A CAPTURE FOR EVERY PUSH, THE CLOSE IN ONE ORDER), EACH DELTA WITH ITS CONTROL ; THE CLOSE`S ORDER, %d STEPS ; VERSION 4.**' % (
              n0 + nd + 1, n0, len(ORDER))]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b713', p, None)


def write(*a):
    L = text_of()
    if 'dry' in a:
        print(NL.join(L[:12] + L[-24:]))
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
    dl = deltas()
    n0 = len(r1)
    first_equal = r2[:n0] == r1
    v1_lines_equal = all(l in v2.split(NL) for l in v1_body())
    dres = []
    for k, (num, t) in enumerate(dl):
        row = r2[n0 + k] if len(r2) > n0 + k else None
        dres.append(dict(n=n0 + 1 + k, delta=num, equal=bool(row) and row[4] == t, control_in=(num == 'governing') or (bool(row) and 'control:' in row[4]), chars=len(t)))
    orow = r2[n0 + len(dl)] if len(r2) > n0 + len(dl) else None
    order_equal = bool(orow) and orow[4] == order_text()
    neg = v2.replace('every arm reading a step reads all of them', 'every arm reading a step reads its first', 1)
    neg_rows = S1.parse(neg)
    neg_equal = len(neg_rows) > n0 + 2 and neg_rows[n0 + 2][4] == dl[2][1]
    ver = re.search(r'^VERSION: (\d+)$', v2, re.M)
    ok = (first_equal and v1_lines_equal and all(d['equal'] and d['control_in'] for d in dres) and order_equal and len(r2) == n0 + len(HEADS) + 1
          and not neg_equal and bool(ver) and ver.group(1) == str(VERSION))
    L = ['b713 -- STEP ZERO, (R323)(4): THE CONTROL OF THE STANDING CLAUSES v4 -- v3`S ROWS UNCHANGED, THE SEVEN ROWS EQUAL TO THE RULING`S WORDS AND THE ORDER ROW (%s)' % utc(), '',
         '### rows are checks. v4 read back by b710`s parser (tools/b710_standing.py parse): %d rows ; v3 %d rows. The rows cut from relay data/b713_ferry.txt :14.' % (len(r2), n0),
         '### The NEG control: a copy of v4 with delta (ii)`s "every arm reading a step reads all of them" altered to "... reads its first", its row compared again.', '',
         '  v4`s rows (1)-(%d) equal to v3`s row for row (number, kind, separator, tag, clause, source line): %s' % (n0, first_equal),
         '  v3`s body lines (its LINE sections and rows) present in v4 line for line: %s' % v1_lines_equal]
    L += ['  (%d) %s: equal to its span of the ferry %s ; its control within it %s ; %d characters' % (
        d['n'], 'the governing row' if d['delta'] == 'governing' else 'delta (%s)' % d['delta'], d['equal'], 'n/a (the governing row)' if d['delta'] == 'governing' else d['control_in'], d['chars'])
        for d in dres]
    L += ['  (%d) the close`s order: equal to the tool`s ORDER (%d steps) %s' % (n0 + len(dl) + 1, len(ORDER), order_equal),
          '  NEG: the altered copy`s delta (ii) equal to the ferry %s (wanted False)' % neg_equal,
          '  VERSION %s (wanted %d)' % (ver.group(1) if ver else 'NONE', VERSION), '',
          '### ### **ROWS %d ; v3`S %d UNCHANGED %s ; ROWS CUT %d EQUAL %s ; THE ORDER ROW %s ; THE NEG COPY DIFFERS %s ; VERSION 4 %s ; THE CONTROL AS WANTED %s.**' % (
              len(r2), n0, first_equal and v1_lines_equal, len(dres), all(d['equal'] for d in dres), order_equal, not neg_equal, bool(ver) and ver.group(1) == str(VERSION), ok)]
    if 'dry' not in a:
        for name, data in (('b713_standing_control.txt', NL.join(L) + NL),
                           ('b713_standing_control.json', json.dumps(dict(at=utc(), rows=dres, first_equal=first_equal, v1_lines_equal=v1_lines_equal, neg_equal=neg_equal,
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
        print('usage: b713_standing.py write [dry] | control [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
