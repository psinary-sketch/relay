# -*- coding: utf-8 -*-
"""b507_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
F = json.loads(read('b507_fold.json'))
N = json.loads(read('b507_notes.json'))
X = json.loads(read('b507_fixtures.json'))
L = ['=' * 104, 'b507 -- THE CLOSING RECORD. ### **THE MARGIN AND ITS CONTROL ARC FOLDED, b487-b506; (R117)`S REPAIRS AND NOTES INSIDE IT.**', '=' * 104,
     '    fold : %s ; quotes matched %d of %d ; rulings %d of %d ; columns %s'
     % (F['heading'], sum(q['found'] for q in F['quotes']), len(F['quotes']), sum(r['found'] for r in F['rulings']), len(F['rulings']), F['columns']),
     '    writes : ' + ' ; '.join('%(file)s +%(added)d prefix %(prefix)s removed %(removed)d' % w for w in F['writes']),
     '    notes : ' + ' ; '.join('%(file)s prefix %(prefix)s marks %(marks)d' % n for n in N),
     '    repairs : %s ; census %d registrations, %d newly firing' % (lw(read('b507_fixtures.txt'), 'VERDICT :'), X['census']['registrations'], X['census']['fire_only_new']),
     '    correspondence row 356 : written by the repaired writer, read back six cells',
     '    expectations : NONE REGISTERED -- a fold registers none',
     '', '### THIS ACT`S OWN DEFECTS -- FIVE, THREE BEFORE THE SEAL AND TWO AFTER (the desk, `b507_desk_notes.txt`).',
     '    (a) the face`s first draft tripped the prediction counter ; (b) the fold`s first draft carried a sentence the span refutes ;',
     '    (c) a heredoc failed to parse ; (d) ### **`G-NOTES-PREFIX` COMPARED A CRLF WORKING COPY WITH AN LF BLOB** ; (e) a heredoc collapsed `\\r\\n`.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b507_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b507_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b507_census_closing.txt'), 'TOTAL MISSING'), lw(read('b507_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b507_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE INSTRUMENT LANE IS SHUT**; the numerical lane opens for b508 under (R117)(4), the kernel lane after it.',
      '    (b) ### **ROUTED BY THE FOLD, NOT REPAIRED:** the cut one-statement at FINDINGS.md:4136, and b504`s mislabelled defect.',
      '    (c) ### **b334`S CROSSINGS ARE UNVERIFIED** until re-read on the completed bank; no crossing width is cited.',
      '=' * 104]
io.open(os.path.join(D, 'b507_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
