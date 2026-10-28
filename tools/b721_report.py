"""b721 -- THE STANDING REPORT TOOL, (R331)(3): data/b721_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b720's standing report (tools/b720_report.py) by diff and its lines rewritten at Component 8: b720's lines (the challenge,
the pin, the coefficients at -35 and -40, H-DECOMP, H-RR, the REGISTRY cells) read banks this act does not write, and are not carried; the
lines are b721's: the rebuild at each wave 1 kernel's own pin, on the runner by its run ids (KERNEL), the table over h = 3, 4, 5 exact and
the C2 rule's output NONE from decomposition types (CERTIFIED -- Python-checked, not a kernel statement, N3), the h = 3, 4 predictions and
the fourteen blind (REGISTERED), and the offset post hoc, the frozen line and its drafts, the draft and the carried (HELD).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b721_report.txt and data/b721_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b721_scores_close.json, each HELD or BROKEN, and the root line from
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
import b721_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b721'
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
    import b721_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE REBUILD ((R331)(7)(iii)), on the runner (N1: no lean on
    # ------------------------------------------------------------------ the host), each run read by its id
    sk = seat('%s_rebuild.txt' % ACT, 'PUSHED ')
    keys['REBUILD'] = ('KERNEL -- THE REBUILD AT EACH WAVE 1 KERNEL`S OWN PIN: %s of %s build at the Mathlib each manifest carries (%s with a '
                       'sorry, not complete); %s pushed, %s runs read by their ids, %s dispatch refused (SIDE-frobenius, no workflow on main) '
                       'and its run on push at the author`s two lines (%s); held %s, nothing repaired, no main or tag touched. SOURCE %s.' % (
                           f['rb_j'], f['rb_m'], f['rb_sorry'], f['rb_pushed'], f['rb_runs'], f['rb_refused'], K.FROBENIUS_TWO_LINES[:8],
                           f['rb_held'], sk['text']))
    seats.append(sk)
    # ------------------------------------------------------------------ CERTIFIED: THE TABLE OVER h = 3, 4, 5 ((R331)(4)), exact; THE HALT'S
    # ------------------------------------------------------------------ WALK ((R331)(3)), from decomposition types alone
    sd = seat('%s_derivation.txt' % ACT, '### CHECK (4): ALL AS WANTED')
    keys['TABLE'] = ('CERTIFIED -- THE TABLE OVER CYCLIC h = 3, 4, 5 AT OMEGA 1-6: %s ; %s ; %s; its checks before each step and its plants '
                     'failing as wanted; Python-checked against the group-ring model, a written table and not a kernel statement (N3). SOURCE %s.' % (
                         f['dv_grade'], f['dv_table'], f['dv_read'], sd['text']))
    seats.append(sd)
    sw = seat('%s_registrations.txt' % ACT, 'THE OUTPUT: NONE')
    keys['HALT'] = ('CERTIFIED -- THE C2 RULE`S OUTPUT NONE ((R331)(3) HALTED AT (i), PROVED): the %s class-number-2 fields walked from '
                    'decomposition types (the largest |D| %s, the walk to |D| < %s), %s used and %s passed over on -2 or -1/2; the positive '
                    'control taking %s and %s; no coefficient computed. SOURCE %s.' % (
                        f['walk_n'], f['walk_largest'], f['walk_reach'], f['walk_used'], f['walk_passed'], f['pc'][0], f['pc'][2], sw['text']))
    seats.append(sw)
    # ------------------------------------------------------------------ REGISTERED: THE h = 3, 4 PREDICTIONS AND THE FOURTEEN BLIND (N2)
    sp = seat('%s_registrations.txt' % ACT, '## (5) THE PREDICTIONS BY RULE (4)')
    keys['PRED'] = ('REGISTERED -- THE h = 3 AND h = 4 PREDICTIONS, committed at %s before anything at them: H-C3-31 n0 = %s, b = %s; H-C4-55 '
                    'n0 = %s, b = %s; the model naming the same n0 at both: %s; nothing at -31 or -55 computed, the computation %s`s. SOURCE %s.' % (
                        K.C2_PRED[:8], f['c3'][1], f['c3'][5], f['c4'][1], f['c4'][5], f['h34_same'], K.NEXT_ACT, sp['text']))
    seats.append(sp)
    sb = seat('%s_registrations.txt' % ACT, '## (3) THE TABLE')
    keys['BLIND'] = ('REGISTERED -- THE TABLE`S PREDICTIONS AT THE FOURTEEN UNUSED CLASS-NUMBER-2 FIELDS, blind, with their falsifier; read not '
                     'this act. SOURCE %s.' % sb['text'])
    seats.append(sb)
    # ------------------------------------------------------------------ HELD: THE OFFSET POST HOC; THE CARRIED; THE FROZEN LINE AND ITS DRAFTS
    so = seat('%s_offset_read.txt' % ACT, '## THE GRADE (POST HOC)')
    keys['OFFSET'] = ('HELD -- THE OFFSET, POST HOC: the seventeen HELD %s, REFUTED %s, NOT SCORABLE %s, H-OFFSET %s post hoc on its own first '
                      'rows, testing nothing; the tier %s chosen, %s formed, carried. SOURCE %s.' % (
                          f['or_held'], f['or_refuted'], f['or_unscor'], f['or_word'], f['ot_chosen'], f['ot_formed'], so['text']))
    seats.append(so)
    sf = seat('%s_frozen_line.txt' % ACT, '## THE GRADE')
    keys['FROZEN'] = ('HELD -- THE FROZEN LINE: %s statements at their pins, %d DERIVES and %d INTERFACES by E0; the sentences graded by the seat`s '
                      'hand, a reading; %s README paragraphs and %s descriptions drafted for the release sitting, in the relay alone. SOURCE %s.' % (
                          f['fz_n'].lower(), f['fz_derives'], f['fz_interfaces'], f['dr_paras'], f['dr_descs'], sf['text']))
    seats.append(sf)
    sh = seat('%s_ferry.txt' % ACT, '(10) THE DRAFT')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits; the surgery under H-SHAPE carried, nothing run; the federation '
                    'pin closed at its banked state. SOURCE %s.' % (K.DRAFT, sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['REBUILD']), ('CERTIFIED', ['TABLE', 'HALT']), ('REGISTERED', ['PRED', 'BLIND']), ('HELD', ['OFFSET', 'FROZEN', 'HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b721_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R331)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b721_report.py scores`, and written nowhere.', '']
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
        print('usage: b721_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
