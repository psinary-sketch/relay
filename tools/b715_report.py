"""b715 -- THE STANDING REPORT TOOL, (R325)(3): data/b715_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b714's standing report (tools/b714_report.py) by diff at Component 6 and its lines rewritten by the Edit tool: b714's lines
(the lv port's tag, pair 7's rectangle, the merge, the law, the residual, the Sonin price, the pilot) read banks this act does not write,
and are not carried; the lines are b715's: the census rows at their pins (KERNEL), none certified (CERTIFIED), the standing toolset and its
replay, the class repairs, the roster from main and the pins census (REGISTERED), and what the act holds (HELD).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b715_report.txt and data/b715_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b715_scores_close.json, each HELD or BROKEN, and the root line from
          data/act_roots.txt; PRINTED ONLY -- no bank is written after the root (N4), and the membrane refuses one.
The tool decides nothing: no verdict is gated on its lines (no arm reads its exit code), and a line it cannot recompute prints as such.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
import b715_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b715'
FOOTINGS = ('KERNEL', 'CERTIFIED', 'REGISTERED', 'HELD')
PP = K.PP
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace')


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.exists(p) else ''


def jl(name):
    t = rd(name)
    return json.loads(t) if t else {}


def sha(name):
    p = os.path.join(D, name)
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def line_of(name, needle):
    for i, l in enumerate(rd(name).split(NL), 1):
        if needle in l:
            return i
    return None


def seat(name, needle):
    """the line's SOURCE: the bank's path, the row cited by line (the first line carrying the needle), its sha256 now."""
    ln, now = line_of(name, needle), sha(name)
    return dict(bank='data/' + name, row=ln, sha256=now, ok=bool(now) and ln is not None,
                text='relay data/%s :%s ; sha256 %s' % (name, ln if ln is not None else '### NEEDLE NOT FOUND', (now or '### ABSENT')[:16]))


def lines():
    import b715_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE CHAIN'S ROWS AT THEIR PINS ((R325)(7))
    sc = seat('%s_chain_rows.txt' % ACT, '### ### **DECLARATIONS')
    keys['ROWS'] = ('KERNEL -- THE CENSUS ROWS AT THEIR PINS: the reduction chain`s %s declarations each read at its pin by git show and graded '
                    'under the E0 gate -- DERIVES %s, INTERFACES %s, not graded %s -- %d of them written to the census v0.8.2 on PLACE-papers main; '
                    'axioms read at the pin %s, not read at this pin %s; one proved by `sorry` in its span. A reading of statements at pins, no '
                    'build on this host. SOURCE %s.' % (f['cr_n'], f['cr_der'], f['cr_int'], int(f['cr_def']) + int(f['cr_ng']), f['cr_reached'],
                                                         f['cr_ax'], f['cr_noax'], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ CERTIFIED: NONE THIS ACT
    keys['CERT'] = ('CERTIFIED -- NONE this act: no certified count computed; pair 7`s rectangle certification carried to b716 ((R325)(8)), '
                    'as b714`s banks state it.')
    # ------------------------------------------------------------------ REGISTERED: THE STANDING TOOLSET AND ITS REPLAY ((R325)(3))
    st = seat('%s_replay.txt' % ACT, '### ### **OBJECTS')
    keys['TOOLSET'] = ('REGISTERED -- THE STANDING CLOSE TOOLSET AT %s: %s files under tools/standing/, %s act literals in the code, the act read '
                       'from data/act_current.json; the replay over b714 and b713 %s of %s objects EQUAL, %s DIFFERS named, %s findings the old '
                       'tools`; the coverage table %s STANDING of %s steps. SOURCE %s.' % (
                           f['ver'], f['sc_files'], f['sc_lit'], f['rp_eq'], f['rp_obj'], f['rp_diff'], f['rp_find'], f['cv_std'], f['cv_steps'],
                           st['text']))
    seats.append(st)
    # ------------------------------------------------------------------ REGISTERED: THE CLASS REPAIRS ((R325)(4))
    sk = seat('%s_standing_controls.txt' % ACT, '### ### **CASES')
    keys['REPAIRS'] = ('REGISTERED -- THE CLASS REPAIRS, %d WITH TWO INSTANCES EACH: %s cases as wanted %s for (i), (ii), (iv)-(vi); the hook`s '
                       '%s of %s for (iii), its repair holding %s. SOURCE %s.' % (
                           f['n_repairs'], f['cc_cases'], f['cc_wanted'], f['hc_wanted'], f['hc_cases'], f['hc_holds'], sk['text']))
    seats.append(sk)
    # ------------------------------------------------------------------ REGISTERED: THE ROSTER FROM MAIN ((R325)(5))
    sr = seat('%s_roster.txt' % ACT, '### ### **ROSTER CONTROLS')
    keys['ROSTER'] = ('REGISTERED -- THE MIRROR`S ROSTER FROM MAIN: the b707 roster`s families read from PLACE-papers main, %s joining, controls %s; '
                      'the builder reads it at build time. SOURCE %s.' % (', '.join(f['ro_joins']), f['ro_ctl'], sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ REGISTERED: THE PINS CENSUS ((R325)(6))
    sp = seat('%s_pins_census.txt' % ACT, '### ### **PINS ROSTER CONTROLS')
    keys['PINS'] = ('REGISTERED -- THE PINS CENSUS AT %s REPOSITORIES: read from %s texts on main, %s hard failures named and carried, controls %s. '
                    'SOURCE %s.' % (f['pins_n'], f['pins_texts'], f['pins_hard'], f['pins_ctl'], sp['text']))
    seats.append(sp)
    # ------------------------------------------------------------------ HELD
    sh = seat('%s_ferry.txt' % ACT, '(11) THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; no bench number in a keystone; the items of (R325)(8) carried to b716 from their '
                    'banks, none acted on here: the heads draft and its footings question, the six lint hits, the 19 names with no pin, the '
                    'SIDESystem finding, the composition law and its -39 registration, the residual, the rectangle, the Sonin price and the law`s '
                    'identity reading. SOURCE %s.' % (K.DRAFT, sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['ROWS']), ('CERTIFIED', ['CERT']), ('REGISTERED', ['TOOLSET', 'REPAIRS', 'ROSTER', 'PINS']), ('HELD', ['HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b715_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R325)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b715_report.py scores`, and written nowhere.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(out)]
    L += ['', '### SOURCES NOT SEATED (a needle not found or a bank absent): %s' % (bad or 'NONE'),
          '### ### **THE STANDING REPORT: %d LINES IN FOOTING ORDER ; SOURCES %d, SEATED %d ; THE SCORES LINE AFTER THE ROOT.**' % (
              len(out), len(seats), len(seats) - len(bad))]
    J = dict(at=at, lines=out, keys=keys, seats=seats, unseated=bad, footing=dict(order))
    for name, b in (('%s_report.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                    ('%s_report.json' % ACT, (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(b)
        os.replace(p + '.tmp', p)
    print(NL.join(L[6:]))


def dry():
    out, _k, seats, _o = lines()
    print(NL.join('  (%d) %s' % (i + 1, l) for i, l in enumerate(out)))
    print('### SOURCES NOT SEATED: %s' % ([s['bank'] for s in seats if not s['ok']] or 'NONE'))


def scores():
    sc = jl('%s_scores_close.json' % ACT)
    keys = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    word = dict(HELD='HELD', REFUTED='BROKEN')
    roots = [l for l in rd('act_roots.txt').split(NL) if l.startswith(ACT + ' ')]
    print('### THE ROOT: %s' % (roots[-1] if roots else '### NOT APPENDED -- the scores line waits on the root'))
    print('### THE SCORES (relay data/%s_scores_close.json, sha256 %s…): %s' % (ACT, (sha('%s_scores_close.json' % ACT) or '### ABSENT')[:16],
          ' ; '.join('%s %s' % (k, word.get((sc.get(k) or ['?'])[0], (sc.get(k) or ['?'])[0])) for k in keys)))
    print('### ### **SCORES %d OF %d HELD -- PRINTED AFTER THE ROOT, WRITTEN NOWHERE.**' % (sum(1 for k in keys if (sc.get(k) or [''])[0] == 'HELD'), len(keys)))


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('bank', 'dry', 'scores'):
        print('usage: b715_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
