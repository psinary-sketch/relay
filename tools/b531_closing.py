# -*- coding: utf-8 -*-
"""b531_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b531_scores.json'))
RD = json.loads(read('b531_read.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b531 -- THE CLOSING RECORD. ### **THE BRIDGE READ: ConservationHypothesis AGAINST h2_sign, UNDER (R141).**', '=' * 104,
     '    SIDE-kernel : pin %s %s ; HEAD %s ; the premise`s files identical : %s' % (RD['pin'][:12], RD['pin_tags'], RD['head'][:12],
                                                                              all(RD['files_identical'][f] for f in ('Bridge/ConservationBridge.lean', 'Kernel/XiDef.lean', 'Kernel/Voice1.lean'))),
     '    statability : %s (both forms elaborate in the banked probe, no new definition)' % ('STATABLE' if SC['statable'] else 'NOT STATABLE'),
     '    the grade against "h2_sign -> RH" : ENCODES-CONCLUSION ; the relation : EQUIVALENT (in the corpus, one direction open at f4)',
     '    the table : ConservationBridge.riemann_hypothesis %s' % lw(read('terminal_table.md'), '`ConservationBridge.riemann_hypothesis`').split('|')[7].strip(),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b531_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b531_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'),
             ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b531_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b531_census_closing.txt'), 'TOTAL MISSING'), lw(read('b531_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b531_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT** (R141)(4).',
      '    (b) ### **W-ORD-H2-BRIDGE, AS READ**: ConservationHypothesis is RH restated (compiled balance_theorem); it implies',
      '        h2_sign now (COMPILABLE-NOW in SIDE-explicit-formula); the converse is f4. The bridge is priced, not built.',
      '    (c) ### **FACES_LEDGER R2`s "the converse is not compiled"** is reported against two compiled lemmas; not edited.',
      '=' * 104]
io.open(os.path.join(D, 'b531_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
