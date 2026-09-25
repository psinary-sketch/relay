# -*- coding: utf-8 -*-
"""b532_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b532_scores.json'))
RW = json.loads(read('b532_rows.json'))
AT = json.loads(read('b532_attempts.json'))
PR = json.loads(read('b532_profile.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
tot = {v: sum(c[v] for c in RW['counts'].values()) for v in ('STANDS', 'RESTS', 'EXCEEDS')}
L = ['=' * 104, 'b532 -- THE CLOSING RECORD. ### **THE DEPOSIT READ, E-2026-09-25-1 DRAFTED, THE TRIVIAL BRIDGE COMPILED, UNDER (R142).**', '=' * 104,
     '    rows : %d -- STANDS %d, RESTS %d, EXCEEDS %d ; RESTS : %s' % (sum(tot.values()), tot['STANDS'], tot['RESTS'], tot['EXCEEDS'], ', '.join(SC['rests'])),
     '    per record : ' + ' ; '.join('%s %d/%d/%d' % (k, v['STANDS'], v['RESTS'], v['EXCEEDS']) for k, v in RW['counts'].items()),
     '    the erratum : DRAFTED, NOT FILED (b532_erratum_draft.md)',
     '    the bridge : ' + ' ; '.join('attempt %d exit %d, %d errors, %.1f s' % (a['attempt'], a['exit'], a['errors'], a['seconds']) for a in AT)
     + ' ; std3 %d of %d' % (sum(1 for v in PR['std3'].values() if v), len(PR['std3'])),
     '    FACES_LEDGER R2 : %s' % read('b532_faces_notes.txt').strip(),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b532_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b532_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'),
             ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b532_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b532_census_closing.txt'), 'TOTAL MISSING'), lw(read('b532_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b532_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT** (R142)(5).',
      '    (b) ### **E-2026-09-25-1 WAITS ON THE AUTHOR`S WORD** at the paste after (R142)(3); the RESTS rows and their drafted',
      '        replacements are in b532_rows.txt; whether any Zenodo description is edited under (R110) is the author`s ruling.',
      '    (c) ### **THE CEILING`S NEXT WORDING IS THE AUTHOR`S** (R142)(2); until then the record may use the sentence printed',
      '        verbatim in b532_components.txt and the trail`s correction note.',
      '=' * 104]
io.open(os.path.join(D, 'b532_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
