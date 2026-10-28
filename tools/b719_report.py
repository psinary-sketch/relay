"""b719 -- THE STANDING REPORT TOOL, (R329)(3): data/b719_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b718's standing report (tools/b718_report.py) by diff and its lines rewritten at Component 7: b718's lines (the pin, A0, the
decomposition, the reads) read banks this act does not write, and are not carried; the lines are b719's: no KERNEL line (no kernel compiled,
N1), the coefficients exact through the cut (CERTIFIED), H-24 and H-47 with the prediction, H-OFFSET post hoc and H-SHAPE (REGISTERED), and
the law derived to the step named, the arms retired and the draft (HELD) -- the derivation a written proof, not compiled, so not a KERNEL or
CERTIFIED line (N3).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b719_report.txt and data/b719_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b719_scores_close.json, each HELD or BROKEN, and the root line from
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
import b719_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b719'
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
    import b719_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: none this act (N1: no lean, no dispatch); the footing prints NONE
    # ------------------------------------------------------------------ CERTIFIED: THE COEFFICIENTS ((R329)(6)(ii)), exact through the cut
    sc = seat('%s_coeffs.txt' % ACT, '### THE CONTROLS: C1 True ; C2 True ; C3 True')
    keys['COEFFS'] = ('CERTIFIED -- THE COEFFICIENTS AT -20 AND -47: exact rationals through 32532 by b711`s route, the controls C1-C3 as wanted '
                      'before the figures; n0(-20) = %s with %s negatives, n0(-47) = %s with %s, b(n0) = %s at each, every sign decided. SOURCE %s.' % (
                          f['n20'], f['neg20'], f['n47'], f['neg47'], f['b20'], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ REGISTERED: H-24, H-47 AND THE PREDICTION; H-OFFSET; H-SHAPE (N2)
    sr = seat('%s_registrations.txt' % ACT, '## H-24 (the navigator')
    keys['REGS'] = ('REGISTERED -- H-24 AND H-47 BEFORE ANY FIGURE: committed alone at %s, the rule`s prediction at %s before any coefficient '
                    '(PRED-20 %s, PRED-47 %s); read on the coefficients: H-24 %s, H-47 %s, PRED-20 and PRED-47 held. SOURCE %s.' % (
                        K.C2_REG[:8], K.C2_PRED[:8], f['pr20'], f['pr47'], f['h24'], f['h47'], sr['text']))
    seats.append(sr)
    so = seat('%s_registrations.txt' % ACT, 'H-OFFSET, POST HOC')
    keys['OFFSET'] = ('REGISTERED -- H-OFFSET, POST HOC: written after -39`s offsets were seen (%s to %s, read post hoc against 60), committed '
                      'alone at %s for the next tier, its falsifier at r <= 0.05, computed at no pair. SOURCE %s.' % (
                          f['off_lo'], f['off_hi'], K.C4_REG[:8], so['text']))
    seats.append(so)
    ss = seat('%s_registrations.txt' % ACT, ': H-SHAPE')
    keys['SHAPE'] = ('REGISTERED -- H-SHAPE: committed alone at %s before any surgery number, its controls written; the surgery %s to b720. '
                     'SOURCE %s.' % (K.C5_REG[:8], f['surgery'].lower(), ss['text']))
    seats.append(ss)
    # ------------------------------------------------------------------ HELD: THE LAW AND ITS GRADE; THE RETIREMENT; THE DRAFT
    sv = seat('%s_derivation.txt' % ACT, '## THE GRADE')
    keys['LAW'] = ('HELD -- THE COEFFICIENT LAW AT -20 AND -47 ON CLAUSES 1 AND 2 AND THE STRONG FORM, DERIVED TO THE STEP NAMED: %s; %s -- not '
                   'compiled, the law not derived whole. SOURCE %s.' % (f['dv_c2'].lower(), f['dv_c1'].lower(), sv['text']))
    seats.append(sv)
    sa = seat('%s_arm_retire.txt' % ACT, '**RETIRED %s CLOSE ARMS' % f['rt_n'])
    keys['ARMS'] = ('HELD -- THE ARMS RETIRED: %s CLOSE arms out of the run list (%s -> %s) by tools/standing/arms.py RETIRED, the history banked '
                    'first, no guard retired, the claim arms %s untouched. SOURCE %s.' % (f['rt_n'], f['rt_before'], f['rt_after'], f['rt_claim'], sa['text']))
    seats.append(sa)
    sh = seat('%s_ferry.txt' % ACT, '(13) THE DRAFT')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; the count law`s route priced (%s unit bands), nothing built; the REGISTRY cells, '
                    'the pin`s remainder and the challenge file moved to b720. SOURCE %s.' % (K.DRAFT, f['cr_bands'], sh['text']))
    seats.append(sh)
    order = [('KERNEL', []), ('CERTIFIED', ['COEFFS']), ('REGISTERED', ['REGS', 'OFFSET', 'SHAPE']), ('HELD', ['LAW', 'ARMS', 'HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b719_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R329)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b719_report.py scores`, and written nowhere.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(out)]
    L += ['', '### FOOTINGS NO LINE STANDS ON: %s' % (', '.join(ft for ft, ks in order if not ks) or 'NONE')
          + ' (KERNEL: no kernel compiled and no runner dispatched this act, N1)']
    L += ['### SOURCES NOT SEATED (a needle not found or a bank absent): %s' % (bad or 'NONE'),
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
        print('usage: b719_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
