# -*- coding: utf-8 -*-
"""b565_synonym_test.py -- COMPONENT 2: THE SYNONYM ENTRY'S TEST AND THE SUPERSEDING ROW'S READ, UNDER (R175)(4).
### `python tools/b565_synonym_test.py unit | regen <noop|after>`. `regen` runs tools/terminal_table.py (unedited but for the
### ruled entry) and compares the regenerated table with the committed one (relay HEAD). Writes relay data/b565_synonym_*
### and data/b565_supersede_*; deletes nothing.
"""
import io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
TERM = 'li_identity_of_exchange'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def put(name, L):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


def unit():
    import terminal_table as TT
    cases = [('fires: the new string maps to the grade', 'INTERFACES-on-false-premise', 'INTERFACES'),
             ('the old entry: INTERFACES-on-named-premise', 'INTERFACES-on-named-premise', 'INTERFACES'),
             ('the old entry: ENCODES-CONCLUSION', 'ENCODES-CONCLUSION', 'ENCODES'),
             ('the old entry: the compound ENCODES-CONCLUSION \\ SHELL', 'ENCODES-CONCLUSION ' + chr(92) + ' SHELL', 'ENCODES'),
             ('quiet: an unknown string maps to itself', 'INTERFACES-on-true-premise', 'INTERFACES-on-true-premise'),
             ('quiet: a plain grade maps to itself', 'SHELL', 'SHELL'),
             ('quiet: the tier word is no grade and maps to itself', 'T2', 'T2')]
    L = ['b565 -- COMPONENT 2 (i): THE SYNONYM ENTRY, UNIT FIXTURES ON synonym(), BOTH POLARITIES', '',
         '### SYNONYMS as the tool now holds it: %s' % TT.SYNONYMS, '']
    ok = []
    for label, arg, want in cases:
        got = TT.synonym(arg)
        ok.append(got == want)
        L.append('  %-60s %-34r -> %-12r %s' % (label, arg, got, 'AGREES' if got == want else '### DISAGREES'))
    L += ['', '### ### **FIXTURES %d ; AGREEING %d : %s**' % (len(ok), sum(ok), 'PASS' if all(ok) else 'FAIL')]
    put('b565_synonym_unit.txt', L)
    return 0 if all(ok) else 1


def rows_of(j):
    rows = j['rows'] if isinstance(j, dict) else j
    return {(r['repo'], r['name']): r for r in rows}


def regen(stage):
    before = rows_of(json.loads(subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/terminal_table.json'],
                                               capture_output=True).stdout.decode('utf-8')))
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    after = rows_of(json.loads(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8').read()))
    run = io.open(os.path.join(D, 'terminal_table_run.txt'), encoding='utf-8').read()
    cb = sorted('%s|%s' % k for k, v in before.items() if v['grade'] == 'CONFLICT')
    ca = sorted('%s|%s' % k for k, v in after.items() if v['grade'] == 'CONFLICT')
    changed = sorted('%s|%s %s -> %s' % (k[0], k[1], before[k]['grade'], after[k]['grade']) for k in before
                     if k in after and before[k]['grade'] != after[k]['grade'])
    L = ['b565 -- COMPONENT 2 (%s): THE TABLE REGENERATED %s' % (
             'ii' if stage == 'noop' else 'iii', 'WITH THE SYNONYM ENTRY AND NO ROW' if stage == 'noop' else 'AFTER THE SUPERSEDING ROW'), '',
         '### regenerated: exit %d ; rows %d (committed %d) ; rows gone %s ; rows added %s' % (
             r.returncode, len(after), len(before), sorted('%s|%s' % k for k in before if k not in after) or 'NONE',
             sorted('%s|%s' % k for k in after if k not in before) or 'NONE'),
         '### the run`s synonym line: ' + (' | '.join(l.strip() for l in run.split(NL) if 'THE SYNONYM MAP' in l) or '### ABSENT'),
         '### ### **CONFLICT committed %d -> regenerated %d**' % (len(cb), len(ca)),
         '### ### **TERMINALS WHOSE GRADE CHANGED : %s**' % (changed or 'NONE')]
    term = {}
    for lab, tab in (('committed', before), ('regenerated', after)):
        for k, v in tab.items():
            if k[1].endswith(TERM):
                L.append('### %s -- %s|%s grade %s' % (lab, k[0], k[1], v['grade']))
                L += ['    cell %-22s %s:%s' % (c['grade'], c['ledger'], c['line']) for c in v['grade_cells']]
                term[lab] = dict(grade=v['grade'], cells=[dict(grade=c['grade'], ledger=c['ledger'], line=c['line']) for c in v['grade_cells']])
    put('b565_supersede_%s.txt' % stage, L)
    json.dump(dict(rc=r.returncode, rows=len(after), conflict_committed=cb, conflict_regenerated=ca, changed=changed, term=term),
              io.open(os.path.join(D, 'b565_supersede_%s.json' % stage), 'w', encoding='utf-8', newline=NL), ensure_ascii=False, indent=1)
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'unit':
        sys.exit(unit())
    if a and a[0] == 'regen' and len(a) == 2 and a[1] in ('noop', 'after'):
        sys.exit(regen(a[1]))
    sys.exit('usage: b565_synonym_test.py unit | regen <noop|after>')
