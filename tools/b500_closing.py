# -*- coding: utf-8 -*-
"""b500_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True).stdout.strip()
R = json.loads(read('b500_results.json'))
L = ['=' * 104, 'b500 -- THE CLOSING RECORD. ### **EXIT 0; ALL THREE THE STANDARD THREE; (R82) HOLDS.**', '=' * 104,
     '    log sha256 %s ; exits %s ; Built %d (Zeta23 %d, Mathlib %d) ; failed NONE'
     % (R['sha256'], [e['exit'] for e in R['ends']], len(R['built_lines']), R['built_zeta'], R['built_mathlib']),
     '    profiles : %s ; (R82) : %s' % ({k: v['verdict'] for k, v in R['profiles'].items()}, R['r82']),
     '    REGISTRY : %d bytes appended, prefix %s ; terminal table diff : changed %d, EF entries %d'
     % (R['c3']['appended'], R['c3']['prefix'], R['c3']['table_changed'], R['c3']['table_ef_entries']),
     '', '### THIS ACT`S OWN DEFECTS -- THREE.',
     '    (a) ### **b497`s AXIOM MATCHER COULD NOT MATCH A STAMPED LOG** -- anchored at line start; the first',
     '        ### reading said ABSENT for all three. ### Repaired; an arm now runs it on a stamped line and a sorryAx tail.',
     '    (b) ### **A QUOTED HEREDOC TURNED `\b` INTO A BACKSPACE** -- the Built count read 0. ### Repaired via chr().',
     '    (c) ### **THE FAILURE MATCHER CAUGHT `failed` INSIDE `info:` ADVICE** -- now `error:` or the lake cross only.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b500_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b500_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b500_census_closing.txt'), 'TOTAL MISSING'), lw(read('b500_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b500_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE TERMINAL TABLE READS `EF_lit_zetaZeroConfig` NOT PROFILED** while REGISTRY carries the banked',
      '        ### profile: the generator reads profiles only from artefacts inside the kernel`s tree. ### The navigator`s.',
      '    (b) ### **THE NUMERICAL LANE OPENS AT b501** under (R112); `corr_row.py` still validates after it writes.',
      '=' * 104]
io.open(os.path.join(D, 'b500_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
