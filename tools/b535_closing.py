# -*- coding: utf-8 -*-
"""b535_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b535_scores.json'))
ER = json.loads(read('b535_erratum.json'))
PR = json.loads(read('b535_platform_record.json'))
FI = json.loads(read('b535_finding.json'))
CE = json.loads(read('b535_ceiling.json'))
TK = json.loads(read('b535_tokenscan.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b535 -- THE CLOSING RECORD. ### **THE UPDATE ACT, UNDER (R145).**', '=' * 104,
     '    the tag : ' + ' ; '.join(l for l in read('b535_tag.txt').split(NL) if l.startswith('baed4df full') or 'v0.1^{}' in l),
     '    the platform : ' + ' ; '.join('%s %s' % (r['tag'], 'MATCH' if r['match'] else 'MISMATCH') for r in PR['rows'])
     + ' ; E-2026-09-25-2 at ERRATA.md:%s' % PR['entry_first_line'],
     '    the erratum : E-2026-09-25-1 at ERRATA.md:%s ; possessives %s (the ferry said ten) ; backticks outside code spans %s ; '
     'partition bullet at :%s' % (ER['entry_lines'], ER['possessives_found'], ER['backticks_outside_code'], ER['partition']['inserted_at']),
     '    the finding : FINDINGS.md:%s ; %s' % (FI['heading_line'], FI['axioms_line']),
     '    the ceiling : README new at %s (old at %s kept) ; REGISTRY new at %s (none before) ; OPEN_TRAILS old at %s, new in the record'
     % (CE['README']['new_line'], CE['README']['old_line_after'], CE['REGISTRY']['new_line'], CE['OPEN_TRAILS']['old_lines']),
     '    the fold : ' + json.loads(read('b535_fold.json'))['heading'] + ' ; span after : %s' % json.loads(read('b535_span_after.json'))['current_span'],
     '    the token : hits %s over %s files, %s commits, the tag and %s push logs ; limb WARNINGs %s'
     % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE'),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b535_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE TAG, THE CENSUSES. ### NO MIRROR ZIP -- (R145)(7).',
     '    pre-push : %s' % lw(read('b535_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b535_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'),
             ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b535_census_closing.txt'), 'TOTAL MISSING'), lw(read('b535_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b535_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **ON THE AUTHOR`S WORD, (R145)(7)**: the mirror refresh (the author`s export) and the memory refresh; the seam`s',
      '        proof, K1 and the register-depth read are not this act`s.',
      '    (b) ### **(N4) REFUTED AS REGISTERED**: the span tool reads 0 at the filing act and will read 1 at b536; the fold`s',
      '        own heading and `Filed by b535` sentence are what it counts from.',
      '    (c) ### **THE PARTITION LIST STILL OMITS E-2026-09-14-1 AND E-2026-09-22-1**, deposit-facing by their own headings;',
      '        reported, not added -- the author`s to order.',
      '=' * 104]
io.open(os.path.join(D, 'b535_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
