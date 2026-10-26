"""b713 -- THE STANDING REPORT TOOL, (R323)(3): data/b713_report.txt (.json). A REPORT, NOT AN ARM.

Rewritten whole by the Write tool at b713 from b712's throughstone report (tools/b712_report.py), carried forward under (R323)(3): "The
throughstone report of b712 carried forward as a standing report tool, data/b713_report.txt, its four footings KERNEL, CERTIFIED, REGISTERED,
HELD, its lines recomputed from the banks with path, line and sha256, its scores line printed after the root; it is a report and not an arm."
b712's throughstone (the join's statement, the artifact's axioms, the tag, Register4_positivity, the re-cut's distance) read banks this act
does not write -- no kernel is written at b713 -- and is not carried; its lines are b713's: the -15 list, the predictions and onsets, the
coefficients, the source pin, the faces head :8 and the re-cut's additive check.
Two routes:
  bank    (before the root) each line's figures recomputed from the act's JSON banks, beside each its SOURCE -- the bank's path, the row cited
          by line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line
          stands on printed as NONE; written through the membrane to data/b713_report.txt and data/b713_report.json. Nothing else is written.
  scores  (after the root) the scores line: all eight from data/b713_scores_close.json, each HELD or BROKEN, and the root line from
          data/act_roots.txt; PRINTED ONLY -- no bank is written after the root (N4), and the membrane refuses one.
The tool decides nothing: no verdict is gated on its lines (no arm reads its exit code), and a line it cannot recompute prints as such.
"""
import calendar
import hashlib
import io
import json
import os
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
import b713_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b713'
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


def iso_epoch(s):
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except (TypeError, ValueError):
        return None


NONE_TEXT = dict(KERNEL='KERNEL -- NONE: no kernel written this act (port-b707 at b712`s tip, no commit; the join tag %s unmoved; no lean on this '
                        'host, no runner dispatch).' % K.JOIN_TAG[0])


def lines():
    keys, seats = {}, []
    # ------------------------------------------------------------------ CERTIFIED: THE -15 LIST
    li, lc = jl('%s_list.json' % ACT), jl('%s_list_controls.json' % ACT)
    s1, s2 = seat('%s_list.txt' % ACT, '### ### **THE LIST COMPLETE TO'), seat('%s_list_controls.txt' % ACT, '### ### **(C-a)')
    bands = li.get('bands') or []
    over = li.get('re_over_1') or []
    keys['LIST'] = ('CERTIFIED -- THE -15 LIST: Q1 = %s (D = -%s), its Epstein zeros counted to height %s in %d bands (complete %d), on the line %d, '
                    'off the line %d pairs, Re rho > 1 at %d (%s); the list`s controls (C-a, C-b, NEG) %s. A certified count to a height; no '
                    'sentence locates a zero of zeta or of an L-function. SOURCE %s ; %s.' % (
                        li.get('form'), li.get('DQ'), li.get('top'), len(bands), sum(1 for b in bands if b.get('complete')),
                        len(li.get('online') or []), len(li.get('offline') or []), len(over),
                        '; '.join('%s + i %s' % (o.get('re', '')[:10], o.get('im', '')[:10]) for o in over) or '-',
                        'AS WANTED' if lc.get('ok') else '### NOT AS WANTED', s1['text'], s2['text']))
    seats += [s1, s2]
    # ------------------------------------------------------------------ REGISTERED: THE PREDICTIONS, COMMITTED ALONE BEFORE ANY ONSET
    pr, on = jl('%s_predictions.json' % ACT), jl('%s_onsets.json' % ACT)
    sp = seat('%s_predictions.txt' % ACT, '### ### **PAIRS')
    pc = (on.get('pred_commit') or '').split(' ')[0]
    pfiles = sorted(x for x in g(ROOT, 'show', '--name-only', '--format=', pc).split(NL) if x.strip()) if pc else []
    pct = g(ROOT, 'show', '-s', '--format=%ct', pc).strip() if pc else ''
    first = iso_epoch(on.get('first_onset') or '')
    before = bool(pct) and first is not None and int(pct) < first
    prows = pr.get('rows') or []
    predicted = [r['k'] for r in prows if r.get('reach') is None]
    keys['PRED'] = ('REGISTERED -- THE PREDICTIONS COMMITTED ALONE: of %d pairs, %d predicted at T0 %s (pairs %s), the window %s, committed at relay %s '
                    'carrying %s; the commit before the first onset (%s) %s. SOURCE %s.' % (
                        len(prows), len(predicted), pr.get('T0'), predicted, pr.get('window'), pc[:8], pfiles, on.get('first_onset'), before, sp['text']))
    seats.append(sp)
    # ------------------------------------------------------------------ REGISTERED: THE ONSETS
    so = seat('%s_onsets.txt' % ACT, '### ### **PAIRS COMPUTED')
    rows = on.get('rows') or []
    ratios = [r.get('ratio') for r in rows if isinstance(r.get('ratio'), (int, float))]
    keys['ONSETS'] = ('REGISTERED -- THE ONSETS AGAINST [0.99, 1.01]: computed %d, HELD %s, REFUTED %s, the ratios %s to %s; the pairs beyond reach '
                      'at T0 held, not computed. SOURCE %s.' % (
                          len(rows), on.get('held'), on.get('refuted'), ('%.6f' % min(ratios)) if ratios else '-',
                          ('%.6f' % max(ratios)) if ratios else '-', so['text']))
    seats.append(so)
    # ------------------------------------------------------------------ REGISTERED: THE COEFFICIENTS, AN OBSERVATION
    co = jl('%s_coeffs.json' % ACT)
    sc = seat('%s_coeffs.txt' % ACT, '### ### **AN OBSERVATION')
    keys['COEFFS'] = ('REGISTERED -- THE COEFFICIENTS THROUGH n <= %s, AN OBSERVATION: c(n) negative from n = %s (c = %s), negative %s of nonzero %s, '
                      'undecided %d; the controls C1 %s, C2 %s, C2-NEG %s. SOURCE %s.' % (
                          co.get('cut'), co.get('least_negative'), co.get('least_negative_value'), co.get('negatives'), co.get('nonzero'),
                          len(co.get('undecided') or []), co.get('c1'), co.get('c2'), co.get('c2_neg'), sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ REGISTERED: THE SOURCE PIN
    sn = seat('%s_source_pin.txt' % ACT, '### ### **THE TEXT FOUND')
    pin = rd('%s_source_pin.txt' % ACT)
    keys['PIN'] = ('REGISTERED -- THE SOURCE PIN: Murty-Osburn, arXiv:math/0412237v1, Theorem 2.3 (Kronecker`s theorem), registration (i)`s two lines '
                   'read as the theorem at -15`s two decompositions -- %s. SOURCE %s.' % ('AGREES' if 'AGREES.**' in pin else '### NOT READ AGREEING', sn['text']))
    seats.append(sn)
    # ------------------------------------------------------------------ REGISTERED: THE FACES HEAD :8
    sf = seat('%s_faces_head_diff.txt' % ACT, '### ### **THE HEAD`S EDIT')
    fd = rd('%s_faces_head_diff.txt' % ACT)
    keys['FACES'] = ('REGISTERED -- THE FACES HEAD: FACES_LEDGER.md :%d restated ((R323)(2)(ii)), the edit the clause named and nothing else %s. '
                     'SOURCE %s.' % (K.FACES_HEAD, 'True.**' in fd, sf['text']))
    seats.append(sf)
    # ------------------------------------------------------------------ REGISTERED: THE RE-CUT'S ADDITIVE CHECK
    ra = jl('%s_recut_additive.json' % ACT).get('last') or {}
    sr = seat('%s_recut_additive.txt' % ACT, 'FOUND 22 ; MISSING 0')
    remote = g(PP, 'ls-remote', 'origin', 'refs/heads/' + K.RECUT_BRANCH).split('\t')[0].strip()
    merged = 'origin/main' in g(PP, 'branch', '-r', '--contains', K.RECUT_TIP)
    keys['RECUT'] = ('REGISTERED -- THE RE-CUT`S ADDITIVE CHECK ON %s: at %s, found %s, missing %s, in order %s; at the remote %s (equal %s), merged '
                     'into main %s. SOURCE %s.' % (
                         K.RECUT_BRANCH, (ra.get('tip') or '')[:8], ra.get('found'), ra.get('missing'), ra.get('in_order'), remote[:8],
                         remote == K.RECUT_TIP, merged, sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; the re-cut on its branch, not merged, for the author`s word; no lv tag '
                    '(W-ORD-LV-PORT-TAG at OPEN_TRAILS :%s); the -15 pairs beyond reach at T0 %s, %d, not computed; the keystone heads for b714.' % (
                        K.DRAFT, K.ORDER_LV_PORT_TAG, pr.get('T0'), len(prows) - len(predicted)))
    order = [('KERNEL', []), ('CERTIFIED', ['LIST']), ('REGISTERED', ['PRED', 'ONSETS', 'COEFFS', 'PIN', 'FACES', 'RECUT']), ('HELD', ['HELD'])]
    out = []
    for ft, ks in order:
        if not ks:
            out.append(NONE_TEXT[ft])
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b713_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R323)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s JSON',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b713_report.py scores`, and written nowhere.', '']
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


def diff():
    """data/b713_report_diff.txt: (R323)(3)'s carry -- this tool against b712's report at the act's base (tools/b712_report.py at relay
    K.PRE_RELAY), by difflib over the two texts; written through the membrane before the root."""
    import difflib
    import act_membrane as MEM
    import b713_record as REC
    old = g(ROOT, 'show', '%s:tools/b712_report.py' % K.PRE_RELAY).replace('\r', '').split(NL)
    new = io.open(os.path.abspath(__file__), encoding='utf-8').read().replace('\r', '').split(NL)
    body = list(difflib.unified_diff(old, new, 'tools/b712_report.py@%s' % K.PRE_RELAY[:8], 'tools/b713_report.py', lineterm=''))
    add = sum(1 for l in body if l.startswith('+') and not l.startswith('+++'))
    rem = sum(1 for l in body if l.startswith('-') and not l.startswith('---'))
    L = ['%s -- (R323)(3): THE STANDING REPORT TOOL CARRIED FORWARD, ITS DIFF AGAINST b712`S REPORT (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '', '### tools/b713_report.py against tools/b712_report.py at relay %s: +%d -%d. The control of its form: `scores` writes nothing (the membrane' % (K.PRE_RELAY[:8], add, rem),
         '### refuses after the root; the route opens no file for writing), `bank` writes data/b713_report.txt and .json alone.', ''] + body + [
         '', '### ### **THE REPORT TOOL`S DIFF: +%d -%d AGAINST b712`S.**' % (add, rem)]
    p = os.path.join(D, '%s_report_diff.txt' % ACT)
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('bank', 'dry', 'scores', 'diff'):
        print('usage: b713_report.py bank | dry | scores | diff')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores, diff=diff)[r]()
