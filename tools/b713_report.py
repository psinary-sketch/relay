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
import re
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


def throughstone():
    """the root's prompt, the author's word (data/b713_author_answers.txt, transcript line 17285): THE THROUGHSTONE FOR THE ACT'S REGISTERED
    LINES AND ITS CERTIFIED OBSERVATION, read before the root and printed beside the report's lines -- (a) the order of the predictions,
    be4db146 an ancestor of every commit of an onset bank, with timestamps, and data/b713_predictions.txt at be4db146 and at HEAD by sha256;
    (b) the eight pairs, n* from the predictions at be4db146, the onset, the ratio to six places, the window from data/b712_registrations.txt
    at 67a02388, HELD or REFUTED, and the 29 beyond reach by height with what the banks commit for them; (c) the coefficient against the
    navigator's value (n = 24, c(24) = -2 log 24, 90 negatives through n = 3000); (d) the source pin in its own words beside registration
    (i); (e) pair 7's zero with Re rho > 1 with the rows that certify it. Reads git and the act's banks; writes nothing (the bank route
    writes the report's own two files). Returns (lines, items): items the readings that are not EQUAL, YES, HELD or AGREES."""
    import math
    out, items = [], []
    pc = (jl('%s_onsets.json' % ACT).get('pred_commit') or '').split(' ')[0]
    head = g(ROOT, 'rev-parse', 'HEAD').strip()
    # ---------------------------------------------------------------- (a) THE ORDER OF THE PREDICTIONS
    banks = ['data/%s_onsets.json' % ACT, 'data/%s_onsets.txt' % ACT]
    commits = [c for c in g(ROOT, 'log', '--format=%H', '--reverse', '%s..HEAD' % K.PRE_RELAY, '--', *banks).split(NL) if c.strip()]
    rows = []
    for c in commits:
        anc = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', pc, c], capture_output=True).returncode == 0
        rows.append('%s %s %s' % (c[:8], g(ROOT, 'show', '-s', '--format=%cI', c).strip(), 'YES' if anc else 'NO'))
        if not anc:
            items.append('(a) %s not after be4db146' % c[:8])
    units = os.path.join(D, '%s_onsets_units.jsonl' % ACT)
    p_at = hashlib.sha256(subprocess.run(['git', '-C', ROOT, 'show', '%s:data/%s_predictions.txt' % (pc, ACT)], capture_output=True).stdout).hexdigest()
    p_hd = hashlib.sha256(subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/%s_predictions.txt' % ACT], capture_output=True).stdout).hexdigest()
    if p_at != p_hd:
        items.append('(a) the predictions bank DIFFERS')
    out.append('(a) THE ORDER OF THE PREDICTIONS: be4db146 (%s) an ancestor of every commit of an onset bank (%s): %s ; the onsets` units file '
               'data/%s_onsets_units.jsonl untracked by the face`s declaration, no commit (its first unit 2026-10-26T01:18:58Z, after the '
               'predictions` commit); data/%s_predictions.txt at be4db146 %s and at HEAD %s %s -- %s' % (
                   g(ROOT, 'show', '-s', '--format=%cI', pc).strip(), ', '.join(banks), ' ; '.join(rows) or '### NONE FOUND', ACT, ACT, p_at[:16],
                   head[:8], p_hd[:16], 'EQUAL' if p_at == p_hd else '### DIFFERS'))
    # ---------------------------------------------------------------- (b) THE EIGHT PAIRS AND THE 29 BEYOND REACH
    ptxt = subprocess.run(['git', '-C', ROOT, 'show', '%s:data/%s_predictions.txt' % (pc, ACT)], capture_output=True).stdout.decode('utf-8').replace('\r', '').split(NL)
    reg = subprocess.run(['git', '-C', ROOT, 'show', '67a02388:data/b712_registrations.txt'], capture_output=True).stdout.decode('utf-8').replace('\r', '').split(NL)
    hyp = next((i for i, l in enumerate(reg, 1) if l.strip().startswith('HYPOTHESIS:') and '[0.99, 1.01]' in l), None)
    fal = next((i for i, l in enumerate(reg, 1) if l.strip().startswith('FALSIFIER:') and '[0.99, 1.01]' in l), None)
    lo, hi = 0.99, 1.01
    onr = dict((r['k'], r) for r in jl('%s_onsets.json' % ACT).get('rows') or [])
    pairs, beyond = [], []
    for i, l in enumerate(ptxt, 1):
        m = re.match(r'^\s+pair\s+(\d+) \| rho ([\d.]+) \+ ([\d.]+) i \|.*\| n\*_pred ([\d.]+) \|', l)
        b = re.match(r'^\s+pair\s+(\d+) \| rho ([\d.]+) \+ ([\d.]+) i \| r \S+ \| BEYOND REACH at T0` 199: the rule needs T0` > ([\d.]+)', l)
        if m:
            k, npred = int(m.group(1)), float(m.group(4))
            ns = (onr.get(k) or {}).get('n_star')
            ratio = (ns / npred) if ns else None
            v = 'HELD' if ratio is not None and lo <= ratio <= hi else 'REFUTED'
            if v != 'HELD':
                items.append('(b) pair %d %s' % (k, v))
            pairs.append('pair %d (predictions :%d) n*_pred %s, onset %s, ratio %s, %s' % (k, i, m.group(4), ns, ('%.6f' % ratio) if ratio else '-', v))
        elif b:
            beyond.append('pair %s at %s (:%d): n*_pred NONE COMMITTED, the reach it exceeds T0` 199 < %s' % (b.group(1), b.group(3), i, b.group(4)))
    if beyond:
        items.append('(b) the %d pairs beyond reach carry no committed n*_pred' % len(beyond))
    out.append('(b) THE EIGHT PAIRS against the window [%s, %s] (data/b712_registrations.txt at 67a02388, HYPOTHESIS :%s, FALSIFIER :%s): %s. '
               'THE %d PAIRS BEYOND REACH, by height, as data/%s_predictions.txt at be4db146 commits them and data/%s_onsets.txt states the '
               'reach: %s -- the bank commits no n*_pred for a pair beyond reach (b709`s modulus rule fails at T0` 199, so no prediction is '
               'formed); THE WORD`S "committed prediction n*" FOR THESE 29 IS NOT IN THE BANK' % (
                   lo, hi, hyp, fal, ' ; '.join(pairs), len(beyond), ACT, ACT, ' ; '.join(beyond)))
    # ---------------------------------------------------------------- (c) THE COEFFICIENT AGAINST THE NAVIGATOR'S VALUE
    co = jl('%s_coeffs.json' % ACT)
    ball = re.match(r'^\[(-?[\d.]+) \+/- ([\d.e-]+)\]$', co.get('least_negative_ball') or '')
    want = -2 * math.log(24)
    v_eq = bool(ball) and abs(float(ball.group(1)) - want) < 1e-12
    n3000 = sum(1 for n in co.get('negative_list') or [] if n <= 3000)
    for ok, what in ((co.get('least_negative') == 24, 'the least index'), (v_eq, 'c(24)'), (n3000 == 90, 'the count through 3000')):
        if not ok:
            items.append('(c) %s DIFFERS' % what)
    out.append('(c) THE COEFFICIENT, against the navigator`s value in the word: the least index with c(n) < 0 %s beside 24 -- %s ; c(24) %s, '
               'the ball %s, beside -6 log 2 - 2 log 3 = -2 log 24 = %.15f -- %s ; the count of negative coefficients through n = 3000 from '
               'the bank`s rows (negative_list) %d beside 90 -- %s ; through %s, %s, the seat`s. SOURCE %s' % (
                   co.get('least_negative'), 'EQUAL' if co.get('least_negative') == 24 else '### DIFFERS', co.get('least_negative_value'),
                   co.get('least_negative_ball'), want, 'EQUAL' if v_eq else '### DIFFERS', n3000, 'EQUAL' if n3000 == 90 else '### DIFFERS',
                   co.get('cut'), co.get('negatives'), seat('%s_coeffs.txt' % ACT, '### ### **AN OBSERVATION')['text']))
    # ---------------------------------------------------------------- (d) THE SOURCE PIN IN ITS OWN WORDS
    pin = rd('%s_source_pin.txt' % ACT).split(NL)
    th = next((i for i, l in enumerate(pin, 1) if l.strip().startswith('Theorem 2.3.')), None)
    quote = ' '.join(pin[th - 1:th + 1]).strip().rstrip('"').split() if th else []
    agrees = 'AGREES.**' in NL.join(pin)
    if not agrees:
        items.append('(d) the pin not read AGREES')
    i_lines = [l.strip() for l in reg[15:21] if l.strip().startswith(('Z_Q1(s) + Z_Q2(s) =', 'Z_Q1(s) - Z_Q2(s) ='))]
    out.append('(d) THE SOURCE PIN: M. Ram Murty and Robert Osburn, "Representations of integers by certain positive definite binary quadratic '
               'forms", arXiv:math/0412237v1, page 3 -- "%s" (data/%s_source_pin.txt :%s-:%s; the text`s sha256 5de0ba03...3dac; the bank`s '
               'sha256 %s); registration (i) beside it (data/b712_registrations.txt at 67a02388 :16-:21): %s; the instance at dK = -15 = '
               '(-3)(5), the bridge zeta(s, C) = Z_Q / 2 the seat`s step and named (the bank :38-:41) -- %s' % (
                   ' '.join(quote), ACT, th, (th or 0) + 1, (sha('%s_source_pin.txt' % ACT) or '')[:16], ' ; '.join(i_lines) or '### NOT FOUND',
                   'AGREES' if agrees else '### DIFFERS'))
    # ---------------------------------------------------------------- (e) PAIR 7'S ZERO BEYOND THE STRIP'S RIGHT EDGE
    li = jl('%s_list.json' % ACT)
    p7 = (li.get('re_over_1') or [{}])[0]
    ltxt = rd('%s_list.txt' % ACT).split(NL)
    l_pair = next((i for i, l in enumerate(ltxt, 1) if l.strip().startswith('pair 7 :')), None)
    l_band = next((i for i, l in enumerate(ltxt, 1) if l.strip().startswith('band [59.881486, 75.0]')), None)
    l_meth = next((i for i, l in enumerate(ltxt, 1) if 'RECT_CERTIFY False' in l), None)
    if not p7.get('certified'):
        items.append('(e) pair 7`s point not box-certified: located by Newton inside a band certified by count')
    out.append('(e) PAIR 7`S ZERO WITH Re rho > 1: rho = %s + %s i (data/%s_list.txt :%s), Re rho %.6f ; ITS ROW IN data/%s_list.json (re_over_1): '
               'certified %s, count %s, located "%s", h %s x %s ; WHAT CERTIFIES IT: the band [59.881486, 75.0] (:%s) by its certified count, N 18 '
               '= on-line 12 + 2 x off-line 3, COMPLETE -- the count certified, the off-line points Newton candidates with RECT_CERTIFY False (:%s); '
               'NO BANK AND LINE CERTIFIES THE POINT ITSELF (no rectangle count about it); THE WORD`S "its certificate`s row" IS THE BAND`S COUNT, '
               'NOT A CERTIFICATE OF THE POINT' % (
                   p7.get('re', '')[:20], p7.get('im', '')[:20], ACT, l_pair, float(p7.get('re') or 'nan'), ACT, p7.get('certified'), p7.get('count'),
                   p7.get('located'), p7.get('h_re'), p7.get('h_im'), l_band, l_meth))
    return out, items


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
                    'off the line %d pairs, Re rho > 1 at %d (%s, pair 7: located by Newton at 200 bits, the band`s count certified); every '
                    'off-line point of the list located, not certified -- the counts are certified and the points are located (the author`s word '
                    'after the root`s prompt, event (9)); the list`s controls (C-a, C-b, NEG) %s. A certified count to a height; no '
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
                    '(W-ORD-LV-PORT-TAG at OPEN_TRAILS :%s); the -15 pairs beyond reach at T0 %s, %d, not computed and owed no prediction; the '
                    'rectangle certification of pair 7`s point (an argument-principle count of one zero in a box with Re > 1) carried to b714 to '
                    'be priced there, not run in this act; the keystone heads for b714.' % (
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
    ts, items = throughstone()
    L += ['', '### THE THROUGHSTONE, BESIDE THE LINES (the author`s word at the root`s prompt, relay data/%s_author_answers.txt): the act`s two '
          'REGISTERED lines and its one CERTIFIED observation, read before the root.' % ACT] + ['  %s' % l for l in ts] + [
          '### THE READINGS NOT EQUAL, YES, HELD OR AGREES -- for the events section, the root waiting on the author`s word: %s' % (items or 'NONE'),
          '### THE AUTHOR`S WORD ON THEM (event (9), after the root`s prompt): both stand as the banks state them, the misreadings the navigator`s; '
          '(b) no prediction owed a pair beyond reach; (e) pair 7 located by Newton at 200 bits, the band`s count certified, its rectangle '
          'certification carried to b714; the act proceeds from the entry [12] through the closing as option 1 reads.']
    L += ['', '### SOURCES NOT SEATED (a needle not found or a bank absent): %s' % (bad or 'NONE'),
          '### ### **THE STANDING REPORT: %d LINES IN FOOTING ORDER ; SOURCES %d, SEATED %d ; THE SCORES LINE AFTER THE ROOT.**' % (
              len(out), len(seats), len(seats) - len(bad))]
    J = dict(at=at, lines=out, keys=keys, seats=seats, unseated=bad, footing=dict(order), throughstone=dict(lines=ts, items=items))
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
    ts, items = throughstone()
    print(NL.join('  ' + l for l in ts))
    print('### THE READINGS NOT EQUAL, YES, HELD OR AGREES: %s' % (items or 'NONE'))


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
