# -*- coding: utf-8 -*-
"""b759 -- THE HANDOFF PAGE HALTED, ITS REFUSALS BANKED WITH THEIR CONTROLS. tools/standing/handoff.py ((R364)(5)[H1] as (a); the page that
(R369)(11)'s (W) list names as HANDOFF.md) refuses the page at b759: nothing is written, as its own design orders where a needle is not found.
This tool runs the standing tool's build over the live heads and over planted and earlier sources, through handoff.py's own Source, Planted
and build, and banks what each reads. It writes data/b759_handoff_halt.txt alone; HANDOFF.md is not written, read whole or edited; no
standing tool moves. Written by the Write tool at b759 and committed before its run ((R369) N2).

THE QUOTING RULE (data/b754_rules.txt (8)): the word under REGISTRY's section is read by handoff.py at run time and printed nowhere; this tool
prints no line of REGISTRY, of the page or of the yields -- each REGISTRY line by predicate and sha256 (16 hex) alone, each build by its
refusal's message (which carries no ledger line) or by its line count.

THE READS:
  (L)  the live build at relay HEAD and PLACE-papers HEAD: its refusal;
  (A)  planted: REGISTRY at HEAD less its line :180 (the row 1.5c-24 of (R369)(8), PLACE-papers bb146c95, the one line the act added above
       :373): its refusal;
  (B)  planted: (A) and data/b759_ferry.txt's (11) given a line opening "(11) THE DRAFT stands at" (its own words from that phrase on, in
       place of the line opening "(11) THE SIDE RULE"): its refusal;
  (C)  planted: (B) and data/b758_ferry.txt given b757's THE ACT'S PLACE line (data/b757_ferry.txt :31) at its end: built, its line count;
  (D)  the standing tool's own build at b758's handoff commit 86c1f110 with PLACE-papers 4ea41948 (b758's close): built, its line count,
       the positive control that the needles read where the rule places them;
  (S)  handoff.py's control over the live heads: its exit and the exception's class where it raises;
  and REGISTRY :372-:375 at 4ea41948 and at HEAD by predicate, the line 4ea41948 :373 sought at HEAD by its digest, the holds clause
  counted in b759's ferry and THE ACT'S PLACE in each of the twelve newest ferries by handoff.py's two matchers each. ### The first run
  (23:27:53Z) planted (A) and (C) alone and banked NOT AS READ: (A) refused at b759's holds clause, a third needle behind the first.

  python -X utf8 -u tools/b759_handoff_halt.py [--bank]
"""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'standing'))
import handoff as H   # noqa: E402

BANK = os.path.join(ROOT, 'data', 'b759_handoff_halt.txt')
ROW_COMMIT = 'bb146c95'   # ### PLACE-papers: (R369)(8)'s REGISTRY row 1.5c-24 at :180 and the dated note (data/b759_notes.json, step 38)
B758_HANDOFF = ('86c1f110', '4ea41948')   # ### b758's HANDOFF.md commit (data/b758_steps.json) and b758's PLACE-papers record (ferry :3)
h16 = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]   # noqa: E731


def built(src):
    try:
        P, Y = H.build(src)
        return 'BUILT, %d lines (the cap %d), %d yields' % (len(P), H.CAP, len(Y['yields'])), True
    except H.Refuse as e:
        return 'REFUSED: %s' % e, False


def main():
    L = ['b759 -- THE HANDOFF PAGE HALTED: tools/standing/handoff.py`s build read live, planted and at b758`s handoff, each by its refusal or its line count',
         '(no line of REGISTRY, of the page or of its yields printed; REGISTRY by predicate and sha256 (16 hex) alone)', '']
    base = H.Source()
    L.append('## THE HEADS: relay %s ; PLACE-papers %s' % (base.rhead, base.phead))
    reg = base.pp('REGISTRY.md')
    old = H.Source(*B758_HANDOFF).pp('REGISTRY.md')
    L.append('## REGISTRY BY PREDICATE')
    for tag_, r_ in (('4ea41948', old), ('HEAD', reg)):
        L.append('  %s: %d lines ; %s' % (tag_, len(r_), ' ; '.join(':%d heading %s sha %s' % (n, r_[n - 1].startswith('#'), h16(r_[n - 1]))
                                                                      for n in range(372, 376))))
    at = [i for i, l in enumerate(reg, 1) if l == old[372]]
    L.append('  the line 4ea41948 :373 (sha %s) at HEAD: %s' % (h16(old[372]), at))
    hk = [l for l in subprocess.run(['git', '-C', H.OR.PP, 'show', '-U0', '--format=', ROW_COMMIT, '--', 'REGISTRY.md'], capture_output=True)
          .stdout.decode('utf-8', 'replace').split('\n') if l.startswith('@@')]
    L.append('  PLACE-papers %s`s hunks in REGISTRY.md: %s ; HEAD :180 carries 1.5c-24 %s' % (ROW_COMMIT, ' '.join(h_.split(' @@')[0] + ' @@' for h_ in hk),
                                                                                         '1.5c-24' in reg[179]))
    L.append('## THE ACT`S PLACE IN THE TWELVE NEWEST FERRIES (handoff.py`s PLACE and PLACE_WIDE)')
    cs = H._nums(base.relay_list(), H.CLOSING)[-12:]
    for a in cs:
        f = base.relay('data/b%d_ferry.txt' % a) or []
        L.append('  b%d: %d line(s) %s ; the second shape %d' % (a, sum(1 for l in f if H.PLACE.search(l)), [':%d' % k for k, l in enumerate(f, 1) if H.PLACE.search(l)],
                                                             sum(1 for l in f if H.PLACE_WIDE.search(l))))
    b759f = base.relay('data/b759_ferry.txt') or []
    L.append('  b759 (open): %d line(s) ; the second shape %d' % (sum(1 for l in b759f if H.PLACE.search(l)), sum(1 for l in b759f if H.PLACE_WIDE.search(l))))
    hold = [k for k, l in enumerate(b759f, 1) if H.HOLD.search(l)]
    wide = [k for k, l in enumerate(b759f, 1) if H.HOLD_WIDE.search(l)]
    L.append('## THE HOLDS CLAUSE IN b759`S FERRY (handoff.py`s HOLD, a line opening "(n) THE DRAFT stands at", and HOLD_WIDE): %d line(s) %s ; '
             'the second shape %d %s' % (len(hold), [':%d' % k for k in hold], len(wide), [':%d' % k for k in wide]))
    L += ['', '## THE BUILDS']
    lv, lv_ok = built(base)
    L.append('  (L) live: %s' % lv)
    regA = reg[:179] + reg[180:]
    a_, a_ok = built(H.Planted(base, pp={'REGISTRY.md': regA}))
    L.append('  (A) REGISTRY less :180: %s' % a_)
    fB = list(b759f)
    if len(wide) == 1:
        k_ = wide[0] - 1
        fB[k_] = '(11) ' + fB[k_][fB[k_].index('THE DRAFT stands at'):]
    b_, b_ok = built(H.Planted(base, pp={'REGISTRY.md': regA}, relay={'data/b759_ferry.txt': fB}))
    L.append('  (B) (A) and b759`s (11) given a line opening "(11) THE DRAFT stands at": %s' % b_)
    p757 = [l for l in (base.relay('data/b757_ferry.txt') or []) if H.PLACE.search(l)]
    f758 = base.relay('data/b758_ferry.txt') or []
    c_, c_ok = built(H.Planted(base, pp={'REGISTRY.md': regA}, relay={'data/b759_ferry.txt': fB, 'data/b758_ferry.txt': f758 + p757[:1]}))
    L.append('  (C) (B) and b758`s ferry given b757`s line: %s' % c_)
    d_, d_ok = built(H.Source(*B758_HANDOFF))
    L.append('  (D) at relay %s and PLACE-papers %s: %s' % (B758_HANDOFF[0], B758_HANDOFF[1], d_))
    try:
        ok, _cl = H.control()
        s_ = 'exit %d, its controls %s' % (0 if ok else 1, 'ALL AS WANTED' if ok else 'NOT ALL AS WANTED')
    except Exception as e:   # noqa: BLE001
        s_ = 'RAISED %s before its controls were counted' % type(e).__name__
    L.append('  (S) handoff.py control: %s' % s_)
    want = (not lv_ok and ':373' in lv, not a_ok and 'holds clause read 0 times in data/b759_ferry.txt' in a_,
            not b_ok and 'data/b758_ferry.txt' in b_ and 'read 0 times' in b_, c_ok, d_ok)
    L += ['', '## AS WANTED: (L) refused at :373 %s ; (A) refused at b759`s holds clause %s ; (B) refused at b758`s ferry, 0 lines %s ; (C) built %s ; '
          '(D) built %s' % want,
          '', '### ### **THE HANDOFF PAGE: %s ; REFUSALS 3 (REGISTRY :373 NO HEADING AFTER (8)`S ROW AT :180 ; b759`S FERRY NO LINE OPENING THE HOLDS '
          'CLAUSE ; b758`S FERRY NO THE ACT`S PLACE) ; CONTROLS %d OF 5 AS WANTED ; HANDOFF.md NOT WRITTEN.**' % (
              'HALTED' if all(want) else '### NOT AS READ, SEE ABOVE', sum(want))]
    if '--bank' in sys.argv:
        with open(BANK, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
