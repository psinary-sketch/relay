# -*- coding: utf-8 -*-
"""b723 -- THE CONTROLS OF COMPONENT 7'S REPAIRS (standing clauses v9 row (83): a defect of a class a previous act recorded is met with a
repair, its control printed). Each repair made by the Edit tool in tools/acts/b723.py before the lock -- an override of a template line that
carried an earlier act's object -- read as the folded tools render it, its live reading beside a planted case that must read the other way.

  python -X utf8 tools/b723_repctl.py          prints the controls; writes nothing
  python -X utf8 tools/b723_repctl.py --bank   the same, written to data/b723_c7_repair_controls.txt through the membrane

(Not data/b723_repair_controls.txt: that name is cited by prose and routes carried from earlier acts for other cases, which no b723 route
wrote; a separate name keeps those citations from reading as met. Lettered in data/b723_defects.txt.)

Reads the folded tools (tools/standing/fold.py), the command capture and git; writes nothing else.
"""
import io
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
import standing.fold as F   # noqa: E402

F.install()
import b723_worklist as K   # noqa: E402

NL = '\n'
ACT = 'b723'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = []


def case(rep, what, got, want):
    ROWS.append((rep, what, got, want, got == want))


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def main():
    chk = F.render(ACT, 'checks')
    rec = F.render(ACT, 'record')
    M = F.load(ACT, 'checks')
    R = F.load(ACT, 'record')
    # ### (needle) G-CONVERSION-ONE: the needle as rendered, on the one-argument text conversion it guards and on the c2 check's convolution
    m = re.search(r"(?m)^\s*one_arg = re\.compile\((.+)\)$", chk)
    rx = re.compile(eval(m.group(1))) if m else None
    c2 = io.open(os.path.join(T, 'b723_c2_check.py'), encoding='utf-8').read()
    case('(needle) G-CONVERSION-ONE', 'the needle meets a planted one-argument conversion `def conv(t):`', bool(rx and rx.search('def conv(t):\n')), True)
    case('(needle) G-CONVERSION-ONE', 'the needle passes tools/b723_c2_check.py`s convolution `def conv(A, B, cut)`', bool(rx and rx.search(c2)), False)
    # ### (needle) G-SCORER-READS-BANKS: the record tool as rendered, and a copy whose N1 reads an earlier act's pin rows in place of the axiom rows
    case('(needle) G-SCORER-READS-BANKS', 'the scorers as rendered read b723`s banks', bool(M.scorer_banks_ok({'rec_src': rec})), True)
    case('(needle) G-SCORER-READS-BANKS', 'planted: N1 reading the pin rows in place of the axiom rows',
         bool(M.scorer_banks_ok({'rec_src': rec.replace("'%s_axiom_rows.json' % ACT", "'%s_pin_rows.json' % ACT")})), False)
    # ### the dispatch pattern (record 524-525): b723's dispatch route meets it, b722's rebuild route does not; the capture's count beside the rows'
    case('(dispatch) DISPATCH_CMD', 'meets `python -X utf8 tools/b723_axiom.py dispatch SIDE-spinor`',
         bool(R.DISPATCH_CMD.search('python -X utf8 tools/b723_axiom.py dispatch SIDE-spinor')), True)
    case('(dispatch) DISPATCH_CMD', 'passes `python -X utf8 tools/b723_rebuild.py dispatch SIDE-spinor` (the carried route)',
         bool(R.DISPATCH_CMD.search('python -X utf8 tools/b723_rebuild.py dispatch SIDE-spinor')), False)
    sh_ = [r for r in R.capture() if r['tool'] in ('Bash', 'PowerShell')]
    disp = [r for r in sh_ if R.DISPATCH_CMD.search(R.QUOTED.sub('""', r['cmd']))]
    import json
    rows = json.loads(io.open(os.path.join(D, '%s_axiom_rows.json' % ACT), encoding='utf-8').read())
    by_cmd = [r for r in rows if r.get('kind') == 'dispatch' and not r.get('via')]
    case('(dispatch) DISPATCH_CMD', 'the capture`s dispatch commands (%d: %s) equal the axiom rows` dispatches by command (%d)' % (
        len(disp), ', '.join('#%s' % r['n'] for r in disp) or 'none', len(by_cmd)), len(disp) == len(by_cmd), True)
    # ### (fold) the face's date: the regspec and the gate read the face the record and the checks read
    rs = F.load(ACT, 'regspec')
    gate_src = F.render(ACT, 'reg_gate')
    gm = re.search(r"(?m)^REG = (.+?)(?:\s+#.*)?$", gate_src)
    face = os.path.normcase(os.path.normpath(R.FACE))
    case('(fold) the face`s date', 'the regspec`s REG is the record`s FACE (%s)' % os.path.basename(R.FACE),
         os.path.normcase(os.path.normpath(rs.REG)) == face, True)
    case('(fold) the face`s date', 'the gate`s REG names the worklist`s DATE, not 2026-10-28 (%s)' % (gm.group(1)[:90] if gm else 'UNREAD'),
         bool(gm) and 'K.DATE' not in gm.group(1) and '.DATE' in gm.group(1) and '2026-10-28' not in gm.group(1), True)
    # ### (fold) b709's carry row read for a folded act through the fold bank: the live reading, and a fold bank without the act's sections row
    fold_bank = io.open(os.path.join(D, '%s_fold.txt' % ACT), encoding='utf-8').read()
    case('(fold) the carry row', 'the fold bank carries `tools/acts/b723.py: sections `', 'tools/acts/b723.py: sections ' in fold_bank, True)
    case('(fold) the carry row', 'planted: the bank with that row cut',
         'tools/acts/b723.py: sections ' in fold_bank.replace('tools/acts/b723.py: sections ', 'tools/acts/b723.py: ---- '), False)
    # ### (regspec 78) the OPEN_TRAILS row measured: the lines (R333)(3)(ii)'s commit and the author's word (5)'s added, read by numstat
    ot = [(c, (g(K.PP, 'show', '--numstat', '--format=', c, '--', 'OPEN_TRAILS.md').split() or ['0', '0'])[:2]) for c in (K.C2_PP, K.C2_WEED_PP)]
    case('(regspec) the OPEN_TRAILS row', 'lines added at OPEN_TRAILS before the seal, removed none (%s)' % '; '.join(
        '%s +%s -%s' % (c[:8], a, d) for c, (a, d) in ot), sum(int(a) for _c, (a, _d) in ot) > 0 and all(d == '0' for _c, (_a, d) in ot), True)
    # ### (needle, plant) G-DELETES-ONE-BRANCH on the suite's own sources: the arm live, its plant, and the ruling's form "port-b707 kept;" cut
    sys.argv = [sys.argv[0], '--part', 'act']
    S = M.sources()
    arm = [x for x in M.ARMS_ALL if x[0] == 'G-DELETES-ONE-BRANCH'][0]
    case('(needle) G-DELETES-ONE-BRANCH', 'live: the five step-zero deletes against (R333)(9)`s "kept: port-b707, …"', bool(arm[2](S)), True)
    case('(plant) G-DELETES-ONE-BRANCH', 'the arm`s plant ("deleted by name" set to "kept by name" in the ruling`s own words)', bool(arm[2](arm[3](dict(S)))), False)
    S2 = dict(S)
    S2['ferry'] = S['ferry'].replace('kept: port-b707,', 'kept: challenge-b720-h2-sign-iff-rh,')
    case('(needle) G-DELETES-ONE-BRANCH', 'planted: the ruling`s kept clause without port-b707', bool(arm[2](S2)), False)
    case('(carried) CARRIED_FAILING', 'the face`s carried failures as rendered: %s' % (M.CARRIED_FAILING,), M.CARRIED_FAILING == ('G-AXIOM-CLAIM',), True)
    # ### (repeat) v9 row (83)'s three acts running, the record's _runs3 (new at Component 7): live, and b722's bank with (u)'s tag planted NEW
    live = R._runs3()
    case('(repeat) three acts running', 'live: b723 (a) read as b721 (q) -> b722 (u) -> b723 (a); %d rows' % len(live),
         ('a', 'b721 (q) -> b722 (u) -> b723 (a)') in live, True)
    rdn0 = R.rdn
    R.rdn = lambda name: (rdn0(name).replace("(u) THE SEAT'S [CLOSE ; REPEAT b721 (q)]", "(u) THE SEAT'S [CLOSE ; NEW]")
                          if name == 'b722_defects.txt' else rdn0(name))
    try:
        planted = R._runs3()
    finally:
        R.rdn = rdn0
    case('(repeat) three acts running', 'planted: b722 (u) tagged NEW, so b723 (a) is a repeat of two acts only (%d rows)' % len(planted),
         any(l == 'a' for l, _c in planted) or len(planted) != len(live) - 1, False)
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE CONTROLS OF COMPONENT 7`S REPAIRS (standing clauses v9 row (83)), EACH ON THE FOLDED TOOLS AS RENDERED (%s)' % (ACT, at), '',
         '### by tools/b723_repctl.py; each repair an override in tools/acts/b723.py made by the Edit tool before the lock; each case its reading',
         '### and the reading wanted. The defects these repairs meet are lettered in data/b723_defects.txt.', '']
    for rep, what, got, want, ok in ROWS:
        L.append('  %-32s %-118s %-5s wanted %-5s -- %s' % (rep, what, got, want, 'AS WANTED' if ok else '### NOT AS WANTED'))
    n_ok = sum(1 for r in ROWS if r[4])
    L += ['', '### ### **REPAIR CONTROLS: CASES %d ; AS WANTED %d ;%s**' % (len(ROWS), n_ok, ' ALL AS WANTED.' if n_ok == len(ROWS) else ' NOT ALL AS WANTED.')]
    print(NL.join(L))
    if '--bank' in sys.argv:
        import act_membrane as MEM
        p = os.path.join(D, '%s_c7_repair_controls.txt' % ACT)
        MEM.guard_path(ACT, p, R.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written: data/%s_c7_repair_controls.txt' % ACT)
    return 0 if n_ok == len(ROWS) else 1


if __name__ == '__main__':
    sys.exit(main())
