"""b712 -- THE REPORT, WITH THE THROUGHSTONE CHECK (the ferry's Component 6; the author's word at the root's prompt, data/b712_author_answers.txt :11).

Written by the Write tool after the author's word at the root's prompt and run before the root, outside the sealed list (data/b708_rules.txt
row (1), carried). The author's word names the check: every one of the six lines seated in both faces of the wall -- the sentence the closing
prints and the bank or kernel it comes from. Its items, as worded:
  (a) each line's figures recomputed from the banks themselves, not copied from the root's prompt; beside each line the source bank's path, the
      row cited by line, and that bank's sha256 as its hashes bank records it; then the prompt's figure beside the recomputed one, EQUAL or
      DIFFERS (the prompt's figures read from the answers bank, PROMPT 1);
  (b) each line opened by its footing, KERNEL, CERTIFIED, REGISTERED or HELD, printed in that order;
  (c) the join HELD: DirichletC7Order.lean :501:31, the modules, the run id, the artifact's sha256, the error text by line; no grade for
      faces_join; :212:55 as repaired with the commit of its diff;
  (d) the axis: the falsifier's text as data/b709_registrations.txt registers it, the computed figure that met it, REFUTED;
  (e) the list: the reached height, the bands closed, the on-line and off-line counts above 325; pairs 11 and 15: the refined prediction read
      unchanged from data/b711_registrations.txt (i), the computed onset, the ratio to six places;
  (f) the coefficients: the least negative index with its value in closed form; beside it the navigator's exact value carried in the ruling,
      EQUAL or DIFFERS;
  (g) the scores: all eight, each HELD or BROKEN.
The check writes nothing beyond this tool's own bank (data/b712_report.txt, data/b712_report.json), each through the membrane. Under standing
clauses v2 row (52) a DIFFERS, or a line the word's form cannot hold, is printed here, entered by the seat in data/b712_events.txt, and not
lettered; the root waits on the author's word for that item.
"""
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
import b712_worklist as K          # noqa: E402
import b712_record as REC          # noqa: E402  ### the scorers and ROOT_EXCLUDE, read, not edited
import act_membrane as MEM         # noqa: E402

NL = '\n'
ACT = 'b712'
FOOTINGS = ('KERNEL', 'CERTIFIED', 'REGISTERED', 'HELD')


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


def recorded(hashes, name):
    """the sha256 a hashes bank records for data/<name>; None where the bank carries no row for it."""
    m = re.search(r'(?m)^  ([0-9a-f]{64})  data/%s\s*$' % re.escape(name), rd(hashes))
    return m.group(1) if m else None


def line_of(name, needle):
    for i, l in enumerate(rd(name).split(NL), 1):
        if needle in l:
            return i
    return None


def seat(name, needle, hashes=None):
    """the line's footing in the bank: its path, the cited row by line, its sha256 now and as its hashes bank records it."""
    now = sha(name)
    rec = recorded(hashes, name) if hashes else None
    hs = ('as data/%s records it %s… ; now %s… ; %s' % (hashes, (rec or '### NO ROW')[:16], (now or '-')[:16],
                                                       'EQUAL' if rec and rec == now else 'DIFFERS') if hashes
          else 'no hashes bank for it ; sha256 now %s…' % (now or '-')[:16])
    return dict(bank='data/' + name, row=line_of(name, needle), sha_now=now, sha_recorded=rec,
                text='relay data/%s :%s ; %s' % (name, line_of(name, needle), hs),
                ok=(rec == now) if hashes else now is not None)


def cmp(label, prompt, got):
    eq = prompt is not None and str(prompt) == str(got)
    return dict(item=label, prompt=prompt, recomputed=got, equal=eq, word='EQUAL' if eq else ('DIFFERS' if prompt is not None else 'NOT NAMED IN THE PROMPT'))


def prompt_figures():
    t = rd('%s_author_answers.txt' % ACT)
    m = re.search(r'(?m)^### PROMPT 1 \(Root\): (.*)$', t)
    p = m.group(1) if m else ''

    def f(pat, n=1):
        x = re.search(pat, p)
        return (x.group(n) if n == 1 else x.groups()) if x else None
    return dict(text=p, join=f(r'held at (\S+ :\d+:\d+) \((\d+) of (\d+) modules built\)', 0), surgery=f(r'The surgery is (\w+)'),
                coeff=f(r'negative from n = (\d+)'), axis=f(r'The axis \(e\) is (\w+)'), top=f(r'complete to (\d+)'),
                ratios=f(r'within the refined law \((0\.\d{6}), (0\.\d{6})\)', 0), scores=f(r'Scores: N1-N5 (\w+), S3 (\w+)', 0))


def unchanged(path, commit):
    now = (io.open(os.path.join(ROOT, *path.split('/')), encoding='utf-8').read()).replace('\r', '')
    then = g(ROOT, 'show', '%s:%s' % (commit, path)).replace('\r', '')
    return bool(now) and now == then


def factor(n):
    out, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def closed_form(s):
    """'(-8) log 2 + (-2) log 3' as {2: -8, 3: -2}; None where the text is not of that form."""
    terms = re.findall(r'\((-?\d+)\) log (\d+)', s or '')
    if not terms or re.sub(r'\((-?\d+)\) log (\d+)', '', s).replace('+', '').strip():
        return None
    out = {}
    for c, b in terms:
        for p, e in factor(int(b)).items():
            out[p] = out.get(p, 0) + int(c) * e
    return dict((p, e) for p, e in out.items() if e)


def navigator_value():
    """the navigator's exact value as the author's word at the root carries it (data/b712_author_answers.txt, THE AUTHOR`S WORD: "the navigator's
    exact value, -2 log 48"), else the registration's expectation as the coefficient bank prints it: '<c> log <n>', as {prime: exponent}."""
    w = rd('%s_author_answers.txt' % ACT)
    k = w.find('### THE AUTHOR`S WORD')
    m = re.search(r'navigator[’\']s exact value, (-?\d+) log (\d+)', w[k:] if k >= 0 else '')
    if not m:
        m = re.search(r'(-\d+) log (\d+)', jl('%s_coeffs.json' % ACT).get('expectation') or '')
    if not m:
        return None, None
    c, n = int(m.group(1)), int(m.group(2))
    return '%d log %d' % (c, n), dict((p, c * e) for p, e in factor(n).items())


def main():
    PF = prompt_figures()
    rows, lines, keys, odd = [], [], {}, []
    # ------------------------------------------------------------------ THE JOIN (c): HELD
    pj = jl('%s_port.json' % ACT)
    fe = re.match(r'^error: SIDELvConservation/(\w+\.lean):(\d+):(\d+): (.*)$', pj.get('first_error') or '')
    held_at = '%s :%s:%s' % (fe.group(1), fe.group(2), fe.group(3)) if fe else '-'
    built, mods = len(pj.get('built') or []), len(pj.get('modules') or [])
    art = pj.get('artifact') or {}
    errs = [e for e in pj.get('errors') or []]
    err_rows = ['%s (data/b712_port.txt :%s)' % (e[len('error: '):], line_of('%s_port.txt' % ACT, e)) for e in errs]
    diff_files = [l for l in g(K.LV_DIR, 'diff', '--name-only', K.PORT_TIP, K.PORT_NEW_TIP).split(NL) if l.strip()]
    pe = jl('%s_port_edit.json' % ACT)
    join_graded = os.path.exists(os.path.join(D, '%s_join_grade.txt' % ACT))
    c_join = [cmp('the held line', PF['join'][0] if PF['join'] else None, held_at),
              cmp('the modules built', ('%s of %s' % (PF['join'][1], PF['join'][2])) if PF['join'] else None, '%d of %d' % (built, mods))]
    s_join = seat('%s_port.txt' % ACT, pj.get('first_error') or '\x00')
    keys['JOIN'] = ('HELD -- THE JOIN: not reached; the port of SIDE-lv-conservation built %d of %d modules on its one dispatch, run %s (read by its id), '
                    'the artifact %s sha256 %s (equal to the platform`s digest %s), and held at %s; the error text by line: %s; no grade printed for faces_join '
                    '(a join grade bank %s; SIDE-faces-join unmoved); :212:55, b711`s held line, REPAIRED by the edit at %s :%s (the strong pair`s hasMellin), '
                    'the commit of its diff %s on port-b707 (files %s). SOURCE %s. THE PROMPT: %s.' % (
                        built, mods, pj.get('run_id'), art.get('name'), art.get('sha256'), art.get('agree'), held_at, ' | '.join(err_rows),
                        'present' if join_graded else 'absent', pe.get('file'), pe.get('line'), K.PORT_NEW_TIP[:8], diff_files, s_join['text'],
                        '; '.join('%s %s (prompt %s, recomputed %s)' % (c['item'], c['word'], c['prompt'], c['recomputed']) for c in c_join)))
    rows += c_join
    # ------------------------------------------------------------------ THE SURGERY: CERTIFIED
    sj = jl('%s_surgery.json' % ACT)
    fam = dict((r['fam'], r) for r in sj.get('figures') or [])
    s_ok = [f_ for f_ in ('band', 'rho0') if f_ in fam and (fam[f_].get('reading') or '').startswith('POSITIVE DEFINITE')]
    s_verdict = 'HELD' if len(s_ok) == 2 else 'REFUTED'
    lm = dict((f_, '%.7f ± %s' % (float(fam[f_]['lmin'][0]), fam[f_]['lmin'][1])) for f_ in fam)
    shr = dict((f_, ' / '.join('%.4f' % float(fam[f_]['shares'][w][0]) for w in ('C', 'N', 'CN'))) for f_ in fam)
    c_s = [cmp('the surgery`s verdict', PF['surgery'], s_verdict), cmp('the bank`s own verdict', sj.get('verdict'), s_verdict)]
    s_s = seat('%s_surgery.txt' % ACT, '### ### **', '%s_surgery_hashes.txt' % ACT)
    keys['SURGERY'] = ('CERTIFIED -- THE SURGERY at Q0`s onsets (data/b711_registrations.txt (ii), read unchanged at %s %s): the operated form %s at the band '
                       'zero`s onset (%s, λmin %s) and %s at ρ₀`s (%s, λmin %s), each in balls; the composite share of the prime side (C / N / CN) %s and %s; '
                       'the controls first %s; the falsifier (NEGATIVE DIRECTION at either onset) not fired: %s. The certificate: the balls in data/b712_surgery.json. '
                       'SOURCE %s. THE PROMPT: %s.' % (
                           K.REG_B710[:8], unchanged('data/b711_registrations.txt', K.REG_B710),
                           fam['band'].get('reading', '-')[:40], fam['band'].get('point'), lm.get('band'), fam['rho0'].get('reading', '-')[:40],
                           fam['rho0'].get('point'), lm.get('rho0'), shr.get('band'), shr.get('rho0'), sj.get('controls_ok'), s_verdict, s_s['text'],
                           '; '.join('%s %s (prompt %s, recomputed %s)' % (c['item'], c['word'], c['prompt'], c['recomputed']) for c in c_s)))
    rows += c_s
    # ------------------------------------------------------------------ THE COEFFICIENTS (f): CERTIFIED
    cj = jl('%s_coeffs.json' % ACT)
    neg = cj.get('negative_list') or []
    n0 = min(neg) if neg else None
    cf = closed_form(cj.get('least_negative_value'))
    nav_text, nav = navigator_value()
    c_c = [cmp('the least negative index', PF['coeff'], n0), cmp('the bank`s least negative index', cj.get('least_negative'), n0),
           cmp('the negative count', cj.get('negatives'), len(neg)),
           dict(item='c(48) against the navigator`s exact value', prompt=nav_text, recomputed=cj.get('least_negative_value'), equal=bool(cf) and cf == nav,
                word='EQUAL' if (cf and cf == nav) else 'DIFFERS')]
    val = sum(e * math.log(p) for p, e in (cf or {}).items())
    s_c = seat('%s_coeffs.txt' % ACT, 'NEGATIVE FROM n', '%s_coeffs_hashes.txt' % ACT)
    keys['COEFFICIENTS'] = ('CERTIFIED -- THE COEFFICIENTS of Q0`s log-derivative (data/b711_registrations.txt (iii), an observation), exact through %s: the least '
                            'negative index n = %s, c(%s) = %s (= %s by its prime exponents, %.12f; the bank`s ball %s); %d negative in all, %s nonzero; beside it '
                            'the navigator`s exact value as the ruling carries it, %s (= %s): %s. SOURCE %s. THE PROMPT: %s.' % (
                                cj.get('cut'), n0, n0, cj.get('least_negative_value'), ' + '.join('(%d) log %d' % (e, p) for p, e in sorted((cf or {}).items())),
                                val, cj.get('least_negative_ball'), len(neg), cj.get('nonzero'), nav_text,
                                ' + '.join('(%d) log %d' % (e, p) for p, e in sorted((nav or {}).items())), c_c[3]['word'], s_c['text'],
                                '; '.join('%s %s (prompt %s, recomputed %s)' % (c['item'], c['word'], c['prompt'], c['recomputed']) for c in c_c[:3])))
    rows += c_c
    # ------------------------------------------------------------------ THE AXIS (d): REGISTERED
    aj = jl('%s_axis.json' % ACT)
    reg9 = rd('b709_registrations.txt')
    fm = re.search(r'      FALSIFIER: (.*?)\n      CONTROLS', reg9, re.S)
    fals = re.sub(r'\s+', ' ', fm.group(1)).strip() if fm else '### NOT FOUND'
    ords = [float(x) for x in re.findall(r'\((\d+\.\d+)\.\.\. or (\d+\.\d+)\.\.\.\)', reg9)[0]] if re.search(r'\((\d+\.\d+)\.\.\. or (\d+\.\d+)\.\.\.\)', reg9) else []
    pr = aj.get('profile') or {}
    tp, hw = pr.get('t_peak'), pr.get('half_width')
    near = [o for o in ords if tp is not None and abs(tp - o) <= hw]
    a_verdict = 'REFUTED' if (tp is not None and not near) else 'HELD'
    c_a = [cmp('the axis`s verdict', PF['axis'], a_verdict), cmp('the bank`s own verdict', aj.get('verdict'), a_verdict)]
    s_a = seat('%s_axis.txt' % ACT, '### ### **', '%s_axis_hashes.txt' % ACT)
    keys['AXIS'] = ('REGISTERED -- THE AXIS (e), representation coordinates (data/b709_registrations.txt (i), read unchanged at %s %s): the falsifier as '
                    'registered (:41-:44) -- "%s"; the computed figure that met it: at the onset radius (W_a^16, onset %s) the least eigenvector`s peak '
                    't_peak %s with half-width %.2f, the interval [%.2f, %.2f], against the off-line ordinates %s: within one half-width of %s -- %s. '
                    'SOURCE %s. THE PROMPT: %s.' % (
                        K.PRE_RELAY[:8], unchanged('data/b709_registrations.txt', K.PRE_RELAY), fals, aj.get('onset'), tp, hw, tp - hw, tp + hw, ords,
                        near or 'NONE', a_verdict, s_a['text'],
                        '; '.join('%s %s (prompt %s, recomputed %s)' % (c['item'], c['word'], c['prompt'], c['recomputed']) for c in c_a)))
    rows += c_a
    # ------------------------------------------------------------------ THE LIST AND THE PAIRS (e): REGISTERED
    lj = jl('%s_list.json' % ACT)
    bands = lj.get('bands') or []
    closed = [b_ for b_ in bands if b_.get('complete')]
    on_, off_ = sum(int(b_.get('on') or 0) for b_ in bands), sum(int(b_.get('off') or 0) for b_ in bands)
    top = int(float(lj.get('top') or 0))
    reg10 = rd('b711_registrations.txt')
    pred = dict(re.findall(r'pair (11|15) \(t = .*?\): F2 n\* = (\d+)', reg10))
    lt = rd('%s_list.txt' % ACT)
    t_on = sum(int(x) for x in re.findall(r'(?m)^  band \[[^]]*\] \| N \d+ \| on-line (\d+) \|', lt))
    t_off = sum(int(x) for x in re.findall(r'(?m)^  band \[[^]]*\] \| N \d+ \| on-line \d+ \| off-line (\d+) ', lt))
    pt = rd('%s_pairs.txt' % ACT)
    nstar = dict(re.findall(r'(?m)^  (11|15) \| T0` \d+ \| n\* (\d+) \|', pt))
    ratio = dict((k, '%.6f' % (int(nstar[k]) / int(pred[k]))) for k in ('11', '15') if k in nstar and k in pred)
    within = dict((k, 0.9 <= float(v) <= 1.1) for k, v in ratio.items())
    c_l = [cmp('the reached height', PF['top'], top), cmp('pair 11`s ratio', (PF['ratios'] or [None, None])[0], ratio.get('11')),
           cmp('pair 15`s ratio', (PF['ratios'] or [None, None])[1], ratio.get('15')),
           dict(cmp('the on-line count above 325, the JSON bands against the text`s band rows', t_on, on_), word='EQUAL' if t_on == on_ else 'DIFFERS'),
           dict(cmp('the off-line count above 325, the JSON bands against the text`s band rows', t_off, off_), word='EQUAL' if t_off == off_ else 'DIFFERS')]
    s_l = seat('%s_list.txt' % ACT, 'THE LIST COMPLETE TO', '%s_list_hashes.txt' % ACT)
    s_p = seat('%s_pairs.txt' % ACT, '### ### **PAIRS 11 AND 15', '%s_pairs_hashes.txt' % ACT)
    keys['LIST'] = ('REGISTERED -- THE LIST AND THE PAIRS (W-ORD-Q0-ZEROS-443; data/b711_registrations.txt (i), read unchanged at %s %s): the certified list '
                    'reached height %d, bands closed %d of %d above 325, on-line zeros added %d and off-line %d (the list itself interval-certified); pair 11 -- '
                    'the refined prediction F2 n* = %s (:34), the computed onset n* = %s, the ratio %s, within [0.9, 1.1] %s; pair 15 -- F2 n* = %s (:36), '
                    'n* = %s, the ratio %s, within %s. SOURCE %s ; %s. THE PROMPT: %s.' % (
                        K.REG_B710[:8], unchanged('data/b711_registrations.txt', K.REG_B710), top, len(closed), len(bands), on_, off_,
                        pred.get('11'), nstar.get('11'), ratio.get('11'), within.get('11'), pred.get('15'), nstar.get('15'), ratio.get('15'),
                        within.get('15'), s_l['text'], s_p['text'],
                        '; '.join('%s %s (prompt %s, recomputed %s)' % (c['item'], c['word'], c['prompt'], c['recomputed']) for c in c_l)))
    rows += c_l
    # ------------------------------------------------------------------ THE FOUR STANDING FIGURES: REGISTERED (b711's baseline read at its commit)
    fj = jl('%s_standing_figures.json' % ACT)
    f10_now = jl('b711_standing_figures.json')
    t10 = g(ROOT, 'show', '%s:data/b711_standing_figures.json' % K.PRE_RELAY)
    f10_then = json.loads(t10) if t10.strip() else {}
    names = ('correspondence', 'readme', 'partners', 'pins')
    fig = dict((k, (fj.get(k) or {}).get('figure')) for k in names)
    base = dict((k, (f10_then.get(k) or {}).get('figure')) for k in names)
    c_f = [cmp('b711`s %s baseline, now against its commit' % k, base[k], (f10_now.get(k) or {}).get('figure')) for k in names]
    s_f = seat('%s_standing_figures.txt' % ACT, '### ### **')
    keys['FIGURES'] = ('REGISTERED -- THE FOUR STANDING FIGURES (b711`s figures the baseline, read unchanged at relay %s): correspondence %s, readme %s, partners %s, '
                       'pins %s at b712, beside b711`s %s, %s, %s, %s; no standing arm added. SOURCE %s. THE PROMPT named none.' % (
                           K.PRE_RELAY[:8], fig['correspondence'], fig['readme'], fig['partners'], fig['pins'], base['correspondence'], base['readme'],
                           base['partners'], base['pins'], s_f['text']))
    rows += c_f
    # ------------------------------------------------------------------ THE SCORES (g)
    scj = jl('%s_scores.json' % ACT)
    live = REC._s_scores()
    word = lambda v: {'HELD': 'HELD', 'REFUTED': 'BROKEN'}.get(v)   # noqa: E731
    sc = {}
    for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S3'):
        sc[k] = (scj.get(k) or ['?'])[0]
    for k in ('S1', 'S2'):
        sc[k] = live[k][0]
    sc_words = dict((k, word(v) or ('NOT SCORABLE BEFORE THE ROOT' if v == 'PENDING' else v)) for k, v in sc.items())
    for k, v in sc_words.items():
        if v not in ('HELD', 'BROKEN'):
            odd.append('%s %s: (g) asks HELD or BROKEN; %s reads %s (%s)' % (k, v, k, sc[k], live.get(k, ['', ''])[1] if k in live else ''))
    ps = PF['scores'] or (None, None)
    c_g = [cmp('N1-N5 as the prompt named them', ps[0], 'HELD' if all(sc[k] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5')) else 'NOT ALL HELD'),
           cmp('S3 as the prompt named it', ps[1], sc['S3'])]
    keys['SCORES'] = ('THE SCORES (g), all eight (relay data/b712_scores.json for N1-N5 and S3, written once before the entry; S1 and S2 read now by the record '
                      'tool`s scorer, data/b712_table_final.json and data/b712_root_arm.json): %s. THE PROMPT: %s.' % (
                          ' ; '.join('%s %s' % (k, sc_words[k]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')),
                          '; '.join('%s %s (prompt %s, recomputed %s)' % (c['item'], c['word'], c['prompt'], c['recomputed']) for c in c_g)))
    rows += c_g
    # ------------------------------------------------------------------ THE WALL, IN FOOTING ORDER
    order = [('KERNEL', []), ('CERTIFIED', ['SURGERY', 'COEFFICIENTS']), ('REGISTERED', ['AXIS', 'LIST', 'FIGURES']), ('HELD', ['JOIN'])]
    for ft, ks in order:
        if not ks:
            lines.append('%s -- no line of the six stands on a kernel statement this act (no statement read at a commit with its #print axioms '
                         'output banked among them).' % ft)
        lines += [keys[k] for k in ks]
    lines.append(keys['SCORES'])
    seats = [s_join, s_s, s_c, s_a, s_l, s_p, s_f]
    differs = [r for r in rows if r['word'] == 'DIFFERS']
    seat_bad = [s_['bank'] for s_ in seats if not s_['ok']]
    verdict = ('EVERY LINE EQUAL' if not differs and not odd and not seat_bad else 'NOT EVERY LINE EQUAL: %d DIFFERS, %d NOT IN THE WORD`S FORM, %d BANKS '
               'UNSEATED -- THE ROOT WAITS ON THE AUTHOR`S WORD FOR %s' % (len(differs), len(odd), len(seat_bad), 'THOSE ITEMS' if (len(differs) + len(odd) + len(seat_bad)) > 1 else 'THAT ITEM'))
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE REPORT, WITH THE THROUGHSTONE CHECK, BEFORE THE ROOT (the author`s word at the root`s prompt, data/b712_author_answers.txt :11) (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), then the scores; each line`s figures recomputed from its',
         '### banks, its SOURCE the bank by path, row and sha256 against its hashes bank, its PROMPT the root prompt`s figure (PROMPT 1 in the answers',
         '### bank) beside the recomputed one. Written by tools/b712_report.py, unsealed (data/b708_rules.txt row (1)), after the root`s word and before the root.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(lines)]
    L += ['', '### THE COMPARISONS (%d): %s' % (len(rows), ' ; '.join('%s %s' % (r['item'], r['word']) for r in rows))]
    L += ['### DIFFERS: %s' % ('; '.join('%s (prompt %s, recomputed %s)' % (r['item'], r['prompt'], r['recomputed']) for r in differs) or 'NONE')]
    L += ['### NOT IN THE WORD`S FORM: %s' % ('; '.join(odd) or 'NONE')]
    L += ['### BANKS NOT SEATED (the hashes bank`s row unequal to the bank now): %s' % (seat_bad or 'NONE')]
    L += ['', '### ### **THE THROUGHSTONE CHECK: %s.**' % verdict]
    J = dict(at=at, lines=lines, keys=keys, comparisons=rows, differs=differs, odd=odd, seats=seats, unseated=seat_bad, verdict=verdict,
             footing=dict((ft, ks) for ft, ks in order), prompt=PF['text'])
    for name, b in (('%s_report.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                    ('%s_report.json' % ACT, (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(b)
        os.replace(p + '.tmp', p)
    print(NL.join(L[6:]))
    print('  written: %s_report.txt, %s_report.json' % (ACT, ACT))
    return 0 if verdict == 'EVERY LINE EQUAL' else 1


if __name__ == '__main__':
    sys.exit(main())
