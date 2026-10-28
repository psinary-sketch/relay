"""b720 -- THE STANDING REPORT TOOL, (R330)(3): data/b720_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b719's standing report (tools/b719_report.py) by diff and its lines rewritten at Component 7: b719's lines (H-24, H-47,
H-OFFSET, H-SHAPE, the retirement) read banks this act does not write, and are not carried; the lines are b720's: the challenge file and the
pin, each on the runner by its run id (KERNEL), the coefficients at -35 and -40 exact through the cut (CERTIFIED), the prediction, H-DECOMP
and the law, and H-RR not blind (REGISTERED), and the derivation's -2 graded, the REGISTRY cells and the draft with the carried (HELD) --
the derivation a written proof, not compiled, so not a KERNEL or CERTIFIED line (N3).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b720_report.txt and data/b720_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b720_scores_close.json, each HELD or BROKEN, and the root line from
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
import b720_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b720'
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
    import b720_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE CHALLENGE AND THE PIN ((R330)(5)(ii)-(iii)), on the runner
    # ------------------------------------------------------------------ (N1: no lean on the host), each read by its run id
    sx = seat('%s_challenge.txt' % ACT, '  VERDICT: ')
    keys['CHALLENGE'] = ('KERNEL -- THE CHALLENGE FILE FOR h2_sign_iff_rh: on %s of SIDE-explicit-formula at %s, off main, no tag, one dispatch '
                         'read by its run id %s: %s. SOURCE %s.' % (K.CHALLENGE_BRANCH, K.CHALLENGE_TIP[:8], f['ch_run'], f['ch_verdict'], sx['text']))
    seats.append(sx)
    sp = seat('%s_pin.txt' % ACT, 'THE PIN AT ')
    keys['PIN'] = ('KERNEL -- THE PIN`S REMAINDER: %s of %s eligible build (%s); %s pushed, %s dispatched, %s read; %s held as breaks, unrepaired '
                   '(%s); %s excluded (the freeze and SIDE-cosmo), never pushed. SOURCE %s.' % (
                       f['pin_k'], f['pin_m'], ', '.join(f['pin_builds']) or 'NONE', f['pin_pushed'], f['pin_disp'], f['pin_read'], f['pin_held'],
                       ', '.join(f['pin_breaks']) or 'NONE', f['pin_excl'], sp['text']))
    seats.append(sp)
    # ------------------------------------------------------------------ CERTIFIED: THE COEFFICIENTS ((R330)(3)), exact through the cut
    sc = seat('%s_coeffs.txt' % ACT, '### THE CONTROLS: C1 True ; C2 True ; C3 True')
    keys['COEFFS'] = ('CERTIFIED -- THE COEFFICIENTS AT -35 AND -40: exact rationals through 32532, the controls C1-C3 as wanted before the '
                      'figures; n0(-35) = %s, b = %s, with %s negatives; n0(-40) = %s, b = %s, with %s; every sign decided. SOURCE %s.' % (
                          f['n35'], f['b35'], f['neg35'], f['n40'], f['b40'], f['neg40'], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ REGISTERED: THE PREDICTION, H-DECOMP, THE LAW; H-RR AFTER A FIGURE (N2)
    sr = seat('%s_registrations.txt' % ACT, '## (ii) H-DECOMP')
    keys['REGS'] = ('REGISTERED -- THE PREDICTION, H-DECOMP AND THE LAW BEFORE ANY FIGURE: committed alone at %s, the shape rule`s prediction at %s '
                    'before any coefficient (n0(-35) = %s, n0(-40) = %s); read on the coefficients: ROWS %s, HELD %s, REFUTED %s, the forced %s '
                    'apart; THE LAW %s, H-DECOMP %s, PRED-35 %s, PRED-40 %s. SOURCE %s.' % (
                        K.C2_REG[:8], K.C2_PRED[:8], f['pr35'], f['pr40'], f['rows'], f['held'], f['refuted'], f['forced'], f['law'], f['hdecomp'],
                        f['pred35'], f['pred40'], sr['text']))
    seats.append(sr)
    sq = seat('%s_registrations.txt' % ACT, '## H-RR (the seat')
    keys['RR'] = ('REGISTERED, AFTER A FIGURE -- H-RR: written after the seat`s hand reading of b(100) = -1/2 at -40, declared in the bank; read: '
                  '-35 %s, -40 %s, not counted toward the law. SOURCE %s.' % (f['rr35'], f['rr40'], sq['text']))
    seats.append(sq)
    # ------------------------------------------------------------------ HELD: THE DERIVATION; THE REGISTRY CELLS; THE DRAFT AND THE CARRIED
    sv = seat('%s_derivation.txt' % ACT, '## THE GRADE')
    keys['LAW'] = ('HELD -- THE DERIVATION`S -2 IN BOTH CONFIGURATIONS: %s; %s; %s; %s -- a written proof, not compiled (N3). SOURCE %s.' % (
        f['dv_grade'].lower(), f['dv_m40'].lower(), f['dv_c1'].lower(), f['dv_step'].lower(), sv['text']))
    seats.append(sv)
    sg = seat('%s_registry_diff.txt' % ACT, 'REGISTRY.md ')
    keys['REGISTRY'] = ('HELD -- THE REGISTRY CELLS FOR WAVE 1: the attribute block appended at %s, %s -> %s bytes, the old bytes a prefix of the '
                        'new %s, lines removed %s; rows added %s. SOURCE %s.' % (
                            K.C4_PP[:8], f['rg_before'], f['rg_after'], f['rg_prefix'], f['rg_removed'], ', '.join(f['rg_added']) or 'NONE', sg['text']))
    seats.append(sg)
    sh = seat('%s_ferry.txt' % ACT, '(9) THE DRAFT')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits; the surgery under H-SHAPE and the offset`s next tier under '
                    'H-OFFSET, post hoc, carried to b721, priced, nothing run. SOURCE %s.' % (K.DRAFT, sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['CHALLENGE', 'PIN']), ('CERTIFIED', ['COEFFS']), ('REGISTERED', ['REGS', 'RR']), ('HELD', ['LAW', 'REGISTRY', 'HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b720_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R330)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b720_report.py scores`, and written nowhere.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(out)]
    L += ['', '### FOOTINGS NO LINE STANDS ON: %s' % (', '.join(ft for ft, ks in order if not ks) or 'NONE')
          + ' (KERNEL: on the runner only, each by its run id; no lean on the host, N1)']
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
        print('usage: b720_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
