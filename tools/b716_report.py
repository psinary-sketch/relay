"""b716 -- THE STANDING REPORT TOOL, (R326)(3): data/b716_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b715's standing report (tools/b715_report.py) by diff at Component 5 and its lines rewritten by the Edit tool: b715's lines
(the census rows, the toolset at v1.0.0, the roster, the pins census) read banks this act does not write, and are not carried; the lines are
b716's: the Correspondence rows pinned (KERNEL), none certified (CERTIFIED), the -39 law, the toolset at v1.1.0 and the two prices
(REGISTERED), and what the act holds (HELD).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b716_report.txt and data/b716_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b716_scores_close.json, each HELD or BROKEN, and the root line from
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
import b716_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b716'
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
    import b716_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE CORRESPONDENCE ROWS PINNED ((R326)(5)(iii)-(iv))
    sc = seat('%s_correspondence_pins.txt' % ACT, '### ### **NAMES')
    keys['PINS'] = ('KERNEL -- THE CORRESPONDENCE ROWS PINNED: %s of %s names with no pin given their repository and pin from the census at its '
                    'edition on main, %s listed and carried; Silence :212 corrected to SIDE-meta`s SIDEMeta.SIDESystem, a structure, ERRATA %s; '
                    '%s files edited on PLACE-papers main by the Edit tool, every edit diffed. A reading of the census, no build on this host. '
                    'SOURCE %s.' % (f['ks_pinned'], f['ks_names'], f['ks_carried'], f['ks_errata'], f['ks_files'], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ CERTIFIED: NONE THIS ACT
    keys['CERT'] = ('CERTIFIED -- NONE this act: no count certified, nothing of -39 computed beyond the registration`s count control (N2).')
    # ------------------------------------------------------------------ REGISTERED: THE -39 LAW ((R326)(4))
    sg = seat('%s_genus_control.txt' % ACT, '### ### **THE FORMS h = 4')
    keys['LAW'] = ('REGISTERED -- THE -39 LAW, committed before its computation (relay data/b716_registrations.txt, the act`s first commit): the '
                   'least index with a negative log-derivative coefficient has b(n) = -2, and its index is divisible by a prime no principal form '
                   'represents; its count control %s misses through n = 400; its price about %s foreground hours, the list`s base and first '
                   'two tiers %s h upper. SOURCE %s.' % (f['g_miss'], f['pr_budget'], f['pr_up'], sg['text']))
    seats.append(sg)
    # ------------------------------------------------------------------ REGISTERED: THE STANDING TOOLSET AT v1.1.0 ((R326)(3))
    st = seat('%s_replay.txt' % ACT, '### ### **OBJECTS')
    keys['TOOLSET'] = ('REGISTERED -- THE STANDING TOOLSET AT %s: %s files under tools/standing/, %s act literals in the code; the replay over '
                       'b715, b714 and b713 %s of %s objects EQUAL, %s DIFFERS named, %s findings the old tools`; %s class repairs each with two '
                       'instances, %s cases as wanted %s; the coverage table %s STANDING of %s steps. SOURCE %s.' % (
                           f['ver'], f['sc_files'], f['sc_lit'], f['rp_eq'], f['rp_obj'], f['rp_diff'], f['rp_find'], f['cc_repairs'],
                           f['cc_cases'], f['cc_wanted'], f['cv_std'], f['cv_steps'], st['text']))
    seats.append(st)
    # ------------------------------------------------------------------ REGISTERED: THE TWO PRICES ((R326)(6))
    sf = seat('%s_federation_pin_price.txt' % ACT, '### ### **PUBLIC KERNELS')
    se = seat('%s_epstein_count_price.txt' % ACT, '### ### **THE BAND')
    keys['PRICES'] = ('REGISTERED -- THE FEDERATION PIN AND THE LEAN COUNT, PRICED, nothing built: the pin at %s for %s kernels below it, %s '
                      'dispatches, %s runner hours, the breakage a halt; the Lean count of the band [%s] at Q0, %s dispatches, %s foreground hours, '
                      'grading %s under E0. SOURCES %s ; %s.' % (
                          f['fp_target'], f['fp_below'], f['fp_disp'], f['fp_hours'], f['ep_band'], f['ep_disp'], f['ep_hours'], f['ep_grade'],
                          sf['text'], se['text']))
    seats += [sf, se]
    # ------------------------------------------------------------------ HELD
    sh = seat('%s_ferry.txt' % ACT, '(9) THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; no bench number in a keystone; the heads draft`s sections II and III and the six '
                    'lint hits put in the root`s prompt, nothing written to main without the author`s word; the %s names the census does not pin '
                    'carried to b717. SOURCE %s.' % (K.DRAFT, f['ks_carried'], sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['PINS']), ('CERTIFIED', ['CERT']), ('REGISTERED', ['LAW', 'TOOLSET', 'PRICES']), ('HELD', ['HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b716_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R326)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b716_report.py scores`, and written nowhere.', '']
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
        print('usage: b716_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
