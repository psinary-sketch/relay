"""b718 -- THE STANDING REPORT TOOL, (R328)(3): data/b718_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b717's standing report (tools/b717_report.py) by diff and its lines rewritten by the Edit tool at Component 7: b717's lines
(the eleven names, Silence's head and its companion, the -39 list and coefficients, the two laws at -39) read banks this act does not
write, and are not carried; the lines are b718's: the federation pin's one build (KERNEL), A0 and the decomposition reproduced (CERTIFIED),
the two discriminants registered (REGISTERED), and the law derived to the step named, the reads and the draft (HELD) -- the derivation's
clause 2 a written proof, not compiled, so not a KERNEL or CERTIFIED line (N3).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b718_report.txt and data/b718_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b718_scores_close.json, each HELD or BROKEN, and the root line from
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
import b718_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b718'
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
    import b718_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE FEDERATION PIN ((R328)(8)), a kernel compiled at the new pin
    sp = seat('%s_pin.txt' % ACT, 'DISPATCHES %s (of twelve at most)' % f['pin_disp'])
    keys['PIN'] = ('KERNEL -- THE FEDERATION PIN AT %s OF 12: SIDE-effects` bump branch built on the hosted runner at Mathlib de5ce8a9a66a '
                   '(leanprover/lean4:v4.34.0-rc1), run 40587516142 read by its id, BUILDS %s of %s read; %s kernels carried to b719 on local '
                   'branches by the author`s word, %s held for their reasons; no kernel`s main touched, no tag cut, no lean on this host. '
                   'SOURCE %s.' % (f['pin_disp'], f['pin_builds'], f['pin_read'], f['pin_carried'], f['pin_held'], sp['text']))
    seats.append(sp)
    # ------------------------------------------------------------------ CERTIFIED: A0 AND THE DECOMPOSITION ((R328)(5)(i), (4)(ii))
    sa = seat('%s_a0.txt' % ACT, '**A0 = %s AT Q1 OF -39' % f['a0'])
    keys['A0'] = ('CERTIFIED -- A0 FOR x^2 + xy + 10y^2: A0 = %s at Q1 of -39 %s by its route in ball arithmetic, both controls as wanted; the '
                  'seven predictions re-read %s, equal to the committed %s; the box beyond Re s = 1 at -15 read as b714 certified it (relay '
                  'data/b714_rect.txt :14). SOURCE %s.' % (f['a0'], f['a0_word'], f['a0_reread'], f['a0_equal'], sa['text']))
    seats.append(sa)
    sd = seat('%s_decomp.txt' % ACT, '**THE CHECKS AGREE')
    keys['DECOMP'] = ('CERTIFIED -- THE NAVIGATOR`S READING REPRODUCED BEFORE USE: %s of %s figures agree, %s differ, at n = 48 (-23), 24 (-15) '
                      'and 120 (-39); the checks %s of %s, the plants failing %s of %s. SOURCE %s.' % (
                          f['dc_agree'], f['dc_n'], f['dc_differ'], f['dc_checks'], f['dc_checks_n'], f['dc_plants'], f['dc_plants_n'], sd['text']))
    seats.append(sd)
    # ------------------------------------------------------------------ REGISTERED: THE TWO DISCRIMINANTS ((R328)(4)(iv), N2)
    sr = seat('%s_registrations.txt' % ACT, 'D = %s: h = %s' % (f['rg_d1'], f['rg_h1']))
    keys['REGS'] = ('REGISTERED -- THE NEXT DISCRIMINANTS: D = %s (h = %s) and D = %s (h = %s), the rule printed before its output, committed '
                    'alone at %s before anything at either, nothing computed beyond the class number and forms; b719 computes them. SOURCE %s.' % (
                        f['rg_d1'], f['rg_h1'], f['rg_d2'], f['rg_h2'], K.C2_REG[:8], sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD: THE LAW'S GRADE, THE READS, THE DRAFT
    sv = seat('%s_derivation.txt' % ACT, '## THE GRADE')
    keys['LAW'] = ('HELD -- THE COEFFICIENT LAW DERIVED TO THE STEP NAMED: %s, its hypotheses stated, not compiled (a Lean statement priced in '
                   'relay data/b718_derivation_price.txt); %s -- the law not derived whole. SOURCE %s.' % (
                       f['dv_c2'].lower(), f['dv_c1'].lower(), sv['text']))
    seats.append(sv)
    sc = seat('%s_count_read.txt' % ACT, '## (3) THE READ')
    keys['READS'] = ('HELD -- THE READS: the count law %s by b705`s contour (T-COUNT carried as FINDINGS :8881 assumed it); the join`s premise %s '
                     'as RegisterPentagon :149-:152 words it; the composition law %s at its registered lines. SOURCE %s.' % (
                         'DISCHARGED' if f['count_read'] == 'DISCHARGES' else 'NOT DISCHARGED', f['join'], f['comp'], sc['text']))
    seats.append(sc)
    sh = seat('%s_ferry.txt' % ACT, '(12) THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; no bench number in a keystone; the surgery across the grid priced with its '
                    'registration for b719; the REGISTRY cells, the challenge file and the touch tool priced, nothing built. SOURCE %s.' % (
                        K.DRAFT, sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['PIN']), ('CERTIFIED', ['A0', 'DECOMP']), ('REGISTERED', ['REGS']), ('HELD', ['LAW', 'READS', 'HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b718_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R328)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b718_report.py scores`, and written nowhere.', '']
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
        print('usage: b718_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
