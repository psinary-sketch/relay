# -*- coding: utf-8 -*-
"""standing/v122.py -- THE THREE REPAIRS OF v1.2.2 ((R332)(2)), EACH WITH ITS CONTROL ON THE PREVIOUS ACT'S BANKS, BOTH INSTANCES SHOWN.

  (i)   sealcheck.py: G-SEAL-HASHES reads its list of sealed tools from the seal bank it checks.
        RECORD: the previous act's seal bank against its tools at its closing commit -- the old reading (the suite's carried list, the
        previous act's worklist SEALED) failing on the list alone, the new reading passing with every hash agreeing.
        CONSTRUCTED: a planted name absent from the tree (failing, as wanted); a planted hash that differs (failing, as wanted).
  (ii)  used.py: the reader that marks a discriminant USED reads each coefficient bank by the discriminant and by its principal form in
        every wording the banks b711-b721 carry.
        RECORD: the old reading (`D = ` and `n0(` alone) against the new, the seven discriminants -15, -20, -23, -35, -39, -40, -47 wanted.
        CONSTRUCTED: b711's bank with its form's name planted away (-23 then not USED from it, as wanted).
  (iii) readfirst.py: the closure reader retired, the hand list the bank of record.
        RECORD: the previous act (its closure bank written: the old practice, failing the new reading) and this act at step zero (the
        hand list alone, passing). CONSTRUCTED: a planted closure bank beside this act's hand list (failing, as wanted).

  python -X utf8 tools/standing/v122.py          prints; writes nothing
  python -X utf8 tools/standing/v122.py bank     writes data/<act>_standing_v122.txt
"""
import os
import shutil
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A           # noqa: E402
import readfirst as RF    # noqa: E402
import sealcheck as SC    # noqa: E402
import used as U          # noqa: E402

NL = '\n'
WANT_USED = [-47, -40, -39, -35, -23, -20, -15]


def _prev_close(prev):
    cs = [r['commit'] for r in A.steps(prev) if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    return cs[-1] if cs else None


def _old_sealed(prev):
    """the previous act's suite list (its worklist's SEALED tuple), read by importing its worklist (data and read-only helpers alone)."""
    sys.path.insert(0, A.T)
    mod = __import__('%s_worklist' % prev)
    return tuple(mod.SEALED)


def lines():
    cur = A.current()
    act, prev = cur['act'], cur['prev']
    ok_all = []
    L = ['%s -- THE STANDING TOOLSET AT v1.2.2: THE THREE REPAIRS OF %s(2), EACH CONTROLLED ON %s`S BANKS, BOTH INSTANCES SHOWN (%s)' % (
        act, cur['ruling'], prev, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows are cases: the repair, the instance (RECORD or CONSTRUCTED), what is read, the figure got, the figure wanted, AS WANTED.',
         '### Written by tools/standing/v122.py.', '']

    def case(rep, kind, what, got, want):
        ok = got == want
        ok_all.append(ok)
        L.append('  (%s) %-11s %s : got %s ; wanted %s ; %s' % (rep, kind, what, got, want, 'AS WANTED' if ok else '### NOT AS WANTED'))

    # ================================================================ (i)
    close = _prev_close(prev)
    sj = A.jl('%s_seal_hashes.json' % prev)
    old = _old_sealed(prev)
    new = SC.read(prev, close)
    L += ['## (i) G-SEAL-HASHES READS ITS LIST FROM THE SEAL BANK (tools/standing/sealcheck.py)',
          '    %s`s seal bank (relay data/%s_seal_hashes.json): tools %d ; read at %s`s closing commit %s' % (prev, prev, len(sj.get('tools') or {}), prev, (close or '')[:8]),
          '    the old reading`s list (%s`s worklist SEALED): %d ; in the seal and not the list: %s' % (prev, len(old), sorted(set(sj.get('tools') or {}) - set(old))),
          '    the new reading: listed %d, agree %d, absent %s, differ %s' % (new['listed'], new['agree'], new['absent'] or 'NONE', new['differ'] or 'NONE')]
    case('i', 'RECORD', 'the old reading: the seal`s list equal to the suite`s carried list', sorted(sj.get('tools') or {}) == sorted(old), False)
    case('i', 'RECORD', 'the new reading: every name of the seal bank in the tree at its hash (%d of %d)' % (new['agree'], new['listed']), new['ok'], True)
    planted = dict(sj, tools=dict(sj.get('tools') or {}, **{'%s_absent_plant.py' % prev: '0' * 64}))
    pa = SC.read(prev, close, seal=planted)
    case('i', 'CONSTRUCTED', 'a planted name absent from the tree (%s)' % pa['absent'], pa['ok'], False)
    t0 = sorted(sj.get('tools') or {})[0]
    pd = SC.read(prev, close, seal=dict(sj, tools=dict(sj.get('tools') or {}, **{t0: 'f' * 64})))
    case('i', 'CONSTRUCTED', 'a planted hash that differs (%s)' % pd['differ'], pd['ok'], False)
    L.append('')

    # ================================================================ (ii)
    nu = U.used()
    ou = U.old_reading()
    L += ['## (ii) THE USED READER BY DISCRIMINANT AND BY PRINCIPAL FORM (tools/standing/used.py), over %s' % ', '.join('data/' + b for b in U.BANKS)]
    for d in sorted(nu, reverse=True):
        L.append('    %d USED: %s' % (d, ' ; '.join('%s %s' % (b, '+'.join(k)) for b, k in sorted(nu[d].items()))))
    L.append('    the old reading (tools/%s_select.py used_set`s needle, `D = ` and `n0(`): %s' % (prev, sorted(ou, reverse=True)))
    case('ii', 'RECORD', 'the old reading`s USED set %s equal to the seven' % sorted(ou, reverse=True), sorted(ou) == sorted(WANT_USED), False)
    case('ii', 'RECORD', 'the new reading`s USED set', sorted(nu, reverse=True), sorted(WANT_USED, reverse=True))
    t711 = A.rd('b711_coeffs.txt')
    pu = U.used(banks=('b711_coeffs.txt',), texts={'b711_coeffs.txt': t711.replace('Q0', 'QX')})
    case('ii', 'CONSTRUCTED', 'b711`s bank with its form`s name planted away: -23 USED from it', -23 in pu, False)
    case('ii', 'CONSTRUCTED', 'b711`s bank as written: -23 USED from it', -23 in U.used(banks=('b711_coeffs.txt',)), True)
    L.append('')

    # ================================================================ (iii)
    rp, ra = RF.hand_ok(prev), RF.hand_ok(act)
    L += ['## (iii) THE READFIRST CLOSURE READER RETIRED, THE HAND LIST THE BANK OF RECORD (tools/standing/readfirst.py)',
          '    %s: %s' % (prev, rp), '    %s: %s' % (act, ra)]
    case('iii', 'RECORD', '%s (its closure bank written, the old practice) under the new reading' % prev, rp['ok'], False)
    case('iii', 'RECORD', '%s at step zero (the hand list alone, unchanged since %s)' % (act, ra['first']), ra['ok'], True)
    tmp = tempfile.mkdtemp(prefix='v122_')
    try:
        open(os.path.join(tmp, '%s_readfirst_closure.txt' % act), 'w', encoding='utf-8').write('plant\n')
        case('iii', 'CONSTRUCTED', 'a planted closure bank beside %s`s hand list' % act, RF.hand_ok(act, closure_dir=tmp)['ok'], False)
    finally:
        shutil.rmtree(tmp)
    callers = [l for l in (A.gs('relay', 'grep', '-n', '-E', '-e', r'(import circuit_read|circuit_read\.readfirst\(|circuit_read\.py readfirst [a-z0-9_]+\.txt)',
                                 '--', 'tools/standing', 'tools/%s_*.py' % act) or '').split(NL) if l.strip()]
    L.append('    the calls of the closure reader (an import of circuit_read, a call of its readfirst, or its command line) in tools/standing/ and '
             'the act`s tools: %s' % (callers or 'NONE'))
    case('iii', 'RECORD', 'the closure reader called by the standing toolset or the act`s tools', bool(callers), False)
    n_ok = sum(ok_all)
    L += ['', '### ### **v1.2.2: CASES %d, AS WANTED %d ; (i) THE SEAL`S LIST FROM THE SEAL BANK ; (ii) USED BY DISCRIMINANT AND PRINCIPAL FORM ; '
          '(iii) THE CLOSURE READER RETIRED, THE HAND LIST OF RECORD.**' % (len(ok_all), n_ok)]
    return L, act, all(ok_all)


def main(route):
    L, act, ok = lines()
    if route == 'bank':
        p = os.path.join(A.D, '%s_standing_v122.txt' % act)
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p)
    for l in L:
        print(l[:300])
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
