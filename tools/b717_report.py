"""b717 -- THE STANDING REPORT TOOL, (R327)(3): data/b717_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b716's standing report (tools/b716_report.py) by diff at Component 6 and its lines rewritten by the Edit tool: b716's lines
(the Correspondence pins, the -39 law registered, the toolset at v1.1.0, the two prices) read banks this act does not write, and are not
carried; the lines are b717's: the eleven names and Silence's head with its companion (KERNEL), the -39 list and coefficients (CERTIFIED),
the two laws tested at -39 (REGISTERED), and what the act holds (HELD).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b717_report.txt and data/b717_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b717_scores_close.json, each HELD or BROKEN, and the root line from
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
import b717_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b717'
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
    import b717_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE ELEVEN NAMES PINNED ((R327)(6))
    sn = seat('%s_names.txt' % ACT, '### ### **NAMES')
    keys['NAMES'] = ('KERNEL -- THE ELEVEN NAMES PINNED: %s of %s names the Day-1 Correspondence sections cited with no pin found at their '
                     'kernels` current tags, %s MISSING; each statement printed and graded under E0 from the statement, DERIVES %s, INTERFACES %s, '
                     'not graded %s; each given a row of the census v0.8.3 on main and its paper line pinned to it, ERRATA %s. No axioms read, no '
                     'build on this host. SOURCE %s.' % (f['nm_found'], f['nm_n'], f['nm_missing'], f['cen_derives'], f['cen_interfaces'],
                                                          f['cen_ungraded'], K.ERRATA_IDS[1], sn['text']))
    seats.append(sn)
    sp = seat('%s_companion.txt' % ACT, '### ### **SENTENCES')
    keys['COMPANION'] = ('KERNEL -- SILENCE`S HEAD AND ITS COMPANION: :15 standing as section II without its brackets (equal %s), its %s '
                         'sentences each with its footing and source in day1/Silence_of_Foundations_CORRESPONDENCE.md, KERNEL %s and HELD %s; '
                         'the six hits settled, FOR THE AUTHOR %s, ERRATA %s. SOURCE %s.' % (
                             f['head_eq'], f['cp_s'], f['cp_kernel'], f['cp_held'], f['lt_author'], K.ERRATA_IDS[0], sp['text']))
    seats.append(sp)
    # ------------------------------------------------------------------ CERTIFIED: THE -39 LIST AND THE COEFFICIENTS ((R327)(4)(i), (iv))
    sl = seat('%s_list.txt' % ACT, '### ### **THE LIST COMPLETE')
    keys['LIST'] = ('CERTIFIED -- THE -39 LIST, the counts certified and the off-line points located: Q1 = x^2 + xy + 10y^2 to height %s, %s '
                    'bands each closed by its count, %s zeros on the line, %s off-line pairs located by Newton candidates (point values, the '
                    'rectangles not certified), none with Re rho > 1; its controls before its figures. SOURCE %s.' % (
                        REC._h(f['li_h']), f['li_bands'], f['li_on'], f['li_pairs'], sl['text']))
    seats.append(sl)
    sc = seat('%s_coeffs.txt' % ACT, '### ### **c(n) NEGATIVE FROM')
    keys['COEFFS'] = ('CERTIFIED -- THE -39 COEFFICIENTS, exact through %s: the least n with c(n) < 0 is %s = %s, c(n) = %s, b(n) = %s; %s '
                      'negative coefficients through the cut; the controls (von Mangoldt, the three lines and the Hecke laws with a NEG copy, Q0`s '
                      'and -15`s least negatives) before the figures. SOURCE %s.' % (
                          f['cf_cut'], f['cf_n'], f['cf_fac'], f['cf_c'], f['cf_b'], f['cf_neg'], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ REGISTERED: THE TWO LAWS AT -39 ((R327)(4)(ii)-(iv))
    so = seat('%s_onsets.txt' % ACT, '### ### **PAIRS COMPUTED')
    keys['DETECTION'] = ('REGISTERED -- THE DETECTION LAW AT -39, its predictions committed alone (relay %s) before any onset: HELD at %s of %s '
                         'computed pairs, REFUTED at %s, every ratio in [0.99, 1.01] (%s to %s), the offsets %s to %s; %s pairs beyond reach at '
                         'height %s. SOURCE %s.' % (K.C3_PRED[:8], f['on_held'], f['on_n'], f['on_ref'], f['r_lo'], f['r_hi'], f['of_lo'],
                                                   f['of_hi'], f['pd_beyond'], REC._h(f['li_h']), so['text']))
    seats.append(so)
    keys['COEFFLAW'] = ('REGISTERED -- THE COEFFICIENT LAW AT -39 (registration (ii), data/b716_registrations.txt read unchanged from dc5e808f): '
                        'clause 1, b(n) = -2, %s; clause 2, n divisible by a prime no principal form represents (%s), %s; the registration %s. '
                        'SOURCE %s.' % (f['cl1'], f['cf_reps'], f['cl2'], f['cf_law'], sc['text']))
    # ------------------------------------------------------------------ HELD
    sh = seat('%s_ferry.txt' % ACT, '(10) THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; no bench number in a keystone; the %s -39 pairs beyond reach at height %s, '
                    'scored for nothing; the companion`s %s HELD rows, stated and open; the federation pin scheduled for b718 and the Lean count '
                    'entered at its price, nothing built. SOURCE %s.' % (K.DRAFT, f['pd_beyond'], REC._h(f['li_h']), f['cp_held'], sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['NAMES', 'COMPANION']), ('CERTIFIED', ['LIST', 'COEFFS']), ('REGISTERED', ['DETECTION', 'COEFFLAW']), ('HELD', ['HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b717_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R327)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b717_report.py scores`, and written nowhere.', '']
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
        print('usage: b717_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
