# -*- coding: utf-8 -*-
"""b764, (R374)(6): THE CLOSE'S HOURS AND YIELD, MEASURED, data/b764_close_yield.txt. tools/b754_yield.py carried as a tool of this act and
run over b754 to b763; committed before its run; its controls printed before its figures; nothing removed on what it reads.

  (A) from the step rows of b754 to b763 (data/<act>_steps.json): the hours from the act's opening row to the lock (its first row of phase
      lock) and from the lock to the closing (its last row of phase closing), with the hours of each phase beside them -- a row's hours the
      span from the row before it to the row, set to the row's phase, the opening row's none, so that the phases sum to the opening row's
      span to the last row; where the rows carry no lock or no closing row, the span is printed NOT A ROW and no figure estimated.
  (C) from the suite banks of b754 to b763, pass by pass -- the arms' pre-run (data/<act>_arms_prerun_<part>.txt), the run before the push
      (data/<act>_checks_<part>.txt), the run after it (data/<act>_checks_postpush_<part>.txt), the previous act's mode
      (data/<act>_prevrun_<part>.txt): THE STANDING ARMS of an act are the arms of its part banks less the act's arms over its own banks, as
      its act part's FREEZE line lists them ((R264)(2)); an arm READ A FAULT at an act where its LIVE column reads FAIL in a part bank of the
      run before the push or of the run after it, the two readings that grade the act; the pre-run, before the record stands, and the
      previous act's mode, which reads the act before, printed beside each arm and not counted. For each standing arm the number of the ten
      acts at which it read a fault, those acts by number; the standing arms that read a fault at none of them, by name.
  Carried from tools/b754_yield.py: (A)'s step-row reader and (C)'s part-bank reader, its summary matcher and its row comparison. Not
  carried: (B), (D), (E) and (F), the bank of (R374)(6) holding (A) and (C) alone. THE ROW FORM WIDENED: b754's row form wanted PASS or FAIL
  in the NEG and POS columns and missed G-RUNNER-GATE's row where its POS reads VAC (b754, b755, b756, b760, b761 and b762, standing-a2),
  read at 21:3xZ (scratch yfacts764.py and yodd764.py, read-only); the widened form takes any token there, its yield printed against a loose
  form's.

Controls, before the figures: (A) the spans of b744 to b753 recomputed from their step rows equal to data/b754_close_yield.txt :44-:53, the
three figures of each act; at each of b754 to b763 the phases' seconds summed equal to the opening row's span to the last row; a planted set
of rows read to its known phases. (C) the row reader against each part bank's own LIVE FAILING list, b754 to b763, every pass; the summary
matcher's yield; the row form's yield against a loose form, b754's strict form beside it; the standing arms by the act's list equal to its
FREEZE line's figure, before and after the push, at each act; a planted FAIL row in a bank whose summary prints NONE read as a disagreement;
a planted fault on a standing arm that read none moved from the none to the one or more.
argv: control | run."""
import io, json, os, re, subprocess, sys, datetime
R = r'D:\relay'
D = os.path.join(R, 'data')
NL = '\n'
OUT = os.path.join(D, 'b764_close_yield.txt')
OWN = 'data/b764_close_yield.txt'
ACTS = ['b%d' % n for n in range(754, 764)]
ACTS_B754 = ['b%d' % n for n in range(744, 754)]   # ### the acts of data/b754_close_yield.txt (A), the control's
PASSES = [('pre-run', 'arms_prerun'), ('pre-push', 'checks'), ('post-push', 'checks_postpush'), ('prev-mode', 'prevrun')]
GRADING = ('pre-push', 'post-push')   # ### the passes whose FAIL is a fault read at the act
PART = re.compile(r'^(act|standing-[a-z0-9]+)$')
ROW = re.compile(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL)\s+(\S+)\s+(\S+)\s+([0-9.]+)\s+(.*)$')   # ### widened: NEG and POS any token (VAC)
ROW_B754 = re.compile(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+([0-9.]+)\s+(.*)$')   # ### b754's, its yield printed beside
LOOSE = re.compile(r'^  (G-[A-Z0-9-]+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)')
SUMMARY = re.compile(r'^  ### PART (\S+) : ARMS (\d+) ; LIVE PASSING (\d+) ; LIVE FAILING (\d+) (\[[^\]]*\]|NONE)')
SUMHEAD = re.compile(r'^  ### PART \S+ : ARMS ')
FREEZE = re.compile(r'THE FREEZE: the standing arms \([^)]*\) (\d+) ; carried here (\d+) ; the act`s arms over its own banks (\[[^\]]*\])')
T = lambda s: datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')   # noqa: E731
SEC = lambda a, b: int((T(b) - T(a)).total_seconds())   # noqa: E731
H = lambda a, b: round(SEC(a, b) / 3600.0, 2)   # noqa: E731


def rd(name):
    return io.open(os.path.join(D, name), encoding='utf-8').read().replace('\r', '')


def git(*a):
    return subprocess.run(['git', '-C', R] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# ---------------------------------------------------------------- (A)
def steps(act):
    return json.load(io.open(os.path.join(D, act + '_steps.json'), encoding='utf-8'))['rows']


def phases(rows):
    """{phase: seconds}: each row's span from the row before it set to its phase, the opening row's none; and the phases' order of first use."""
    out, order = {}, []
    for i, r in enumerate(rows):
        if r['phase'] not in out:
            out[r['phase']] = 0
            order.append(r['phase'])
        if i:
            out[r['phase']] += SEC(rows[i - 1]['at'], r['at'])
    return out, order


def spans(act, rows=None):
    rows = steps(act) if rows is None else rows
    lock = [r for r in rows if r['phase'] == 'lock']
    clo = [r for r in rows if r['phase'] == 'closing']
    o, last = rows[0], rows[-1]
    ph, order = phases(rows)
    d = dict(act=act, rows=len(rows), open=(o['commit'][:8], o['at']), last=(last['commit'][:8], last['at'], last['phase']),
             phases=ph, order=order, open_last_s=SEC(o['at'], last['at']))
    if lock:
        d['lock'] = (lock[0]['commit'][:8], lock[0]['at'])
        d['open_lock'] = H(o['at'], lock[0]['at'])
    if clo:
        d['closing'] = (clo[-1]['commit'][:8], clo[-1]['at'])
        d['open_closing'] = H(o['at'], clo[-1]['at'])
    if lock and clo:
        d['lock_closing'] = H(lock[0]['at'], clo[-1]['at'])
    return d


B754_LINE = re.compile(r'^  (b\d{3})  open (\w{8}) \S+ -> (?:line \w{8} \S+ : +[0-9.]+ h ; line -> )?lock (\w{8})(?: \S+)? : +([0-9.]+) h.*? ; '
                       r'lock -> closing (\w{8}) : +([0-9.]+) h ; open -> closing +([0-9.]+) h')


def control_a():
    out, ok, n = [], 0, 0
    lines = rd('b754_close_yield.txt').split(NL)
    got = {}
    for i, l in enumerate(lines, 1):
        m = B754_LINE.match(l)
        if m and m.group(1) in ACTS_B754:
            got[m.group(1)] = (i, m)
    for act in ACTS_B754:
        n += 1
        if act not in got:
            out.append('  (A) data/b754_close_yield.txt: no line read for %s : ### NOT AS WANTED' % act)
            continue
        i, m = got[act]
        s = spans(act)
        rows = steps(act)
        lk = [r for r in rows if r['phase'] == 'lock'][0]
        line = [r for r in rows[:rows.index(lk)] if re.search(r'INTEGRATION line', r['subject'])]
        # ### b754's open -> lock: from the line's row where one names it, the line -> lock span; else the whole span
        b_lock = H(line[0]['at'], lk['at']) if line else s['open_lock']
        want = (float(m.group(4)), float(m.group(6)), float(m.group(7)))
        mine = (b_lock, s.get('lock_closing'), s.get('open_closing'))
        good = want == mine and m.group(2) == s['open'][0] and m.group(3) == s['lock'][0] and m.group(5) == s['closing'][0]
        ok += good
        out.append('  (A) data/b754_close_yield.txt :%d %s %s ; this reader %s from the same rows (commits %s, %s, %s) : %s' % (
            i, act, want, mine, s['open'][0], s['lock'][0], s['closing'][0], 'AS WANTED' if good else '### NOT AS WANTED'))
    for act in ACTS:
        n += 1
        s = spans(act)
        tot = sum(s['phases'].values())
        good = tot == s['open_last_s']
        ok += good
        out.append('  (A) %s: the phases` seconds summed %d ; the opening row to the last row %d s : %s' % (act, tot, s['open_last_s'],
                                                                                                       'AS WANTED' if good else '### NOT AS WANTED'))
    planted = [dict(commit='a' * 8, at='2026-01-01T00:00:00Z', phase='step zero', subject='x'),
               dict(commit='b' * 8, at='2026-01-01T01:00:00Z', phase='component 1', subject='x'),
               dict(commit='c' * 8, at='2026-01-01T01:30:00Z', phase='lock', subject='x'),
               dict(commit='d' * 8, at='2026-01-01T02:00:00Z', phase='component 1', subject='x'),
               dict(commit='e' * 8, at='2026-01-01T03:15:00Z', phase='closing', subject='x')]
    s = spans('b999', planted)
    n += 1
    good = s['phases'] == {'step zero': 0, 'component 1': 5400, 'lock': 1800, 'closing': 4500} and s['open_lock'] == 1.5 \
        and s['lock_closing'] == 1.75 and s['open_closing'] == 3.25
    ok += good
    out.append('  (A) a planted set of five rows: phases %s ; open -> lock %s h, lock -> closing %s h, open -> closing %s h (wanted component 1 5400 s, '
               'lock 1800 s, closing 4500 s ; 1.5, 1.75, 3.25) : %s' % (s['phases'], s['open_lock'], s['lock_closing'], s['open_closing'],
                                                                         'AS WANTED' if good else '### NOT AS WANTED'))
    return out, ok, n


# ---------------------------------------------------------------- (C)
def parts_of(act, prefix):
    pat = re.compile(r'^%s_%s_(.+)\.txt$' % (act, prefix))
    out = []
    for nm in sorted(os.listdir(D)):
        m = pat.match(nm)
        if m and PART.match(m.group(1)):
            out.append(m.group(1))
    return out


_TRACKED = {}


def tracked(path):
    if not _TRACKED:
        for l in git('ls-files', '--', 'data/').split(NL):
            if l.strip():
                _TRACKED[l.strip()] = True
    return path in _TRACKED


def read_part(text):
    """the part bank's arm rows {arm: LIVE} and its summary (part, LIVE FAILING count, list)."""
    rows, summ = {}, None
    for l in text.split(NL):
        m = ROW.match(l)
        if m:
            rows[m.group(1)] = m.group(2)
            continue
        m = SUMMARY.match(l)
        if m:
            summ = (m.group(1), int(m.group(4)), [] if m.group(5) == 'NONE' else json.loads(m.group(5)))
    return rows, summ


def yields(text):
    """(rows the widened form takes, rows b754's form takes, rows the loose form takes, the summary lines taken, summary heads not taken)."""
    L = text.split(NL)
    heads = [l for l in L if SUMHEAD.match(l)]
    taken = sum(1 for l in heads if SUMMARY.match(l))
    return (sum(1 for l in L if ROW.match(l)), sum(1 for l in L if ROW_B754.match(l)), sum(1 for l in L if LOOSE.match(l)), taken, len(heads) - taken)


def compare(text):
    rows, summ = read_part(text)
    f = set(a for a, live in rows.items() if live == 'FAIL')
    if summ is None:
        return False, False, []
    ok = set(summ[2]) == f and summ[1] == len(f)
    return True, ok, sorted(f ^ set(summ[2]))


_PASS = {}


def read_pass(act, prefix):
    if (act, prefix) in _PASS:
        return _PASS[(act, prefix)]
    parts = parts_of(act, prefix)
    fails, arms, agree, disagree, raw, nosum = set(), set(), 0, [], {}, []
    y = [0, 0, 0, 0, 0]
    for p in parts:
        name = '%s_%s_%s.txt' % (act, prefix, p)
        if not tracked('data/' + name):
            continue
        t = rd(name)
        raw[p] = t
        rows, _s = read_part(t)
        arms |= set(rows)
        fails |= set(a for a, live in rows.items() if live == 'FAIL')
        y = [a + b for a, b in zip(y, yields(t))]
        read, ok, diff = compare(t)
        if not read:
            nosum.append(name)
        elif ok:
            agree += 1
        else:
            disagree.append((name, diff))
    r = dict(parts=sorted(raw), fails=fails, arms=arms, agree=agree, disagree=disagree, raw=raw, nosum=nosum, yields=y)
    _PASS[(act, prefix)] = r
    return r


def own_arms(act):
    """(the FREEZE line's standing figure, its carried figure, the act's arms over its own banks), from the act part before the push."""
    m = FREEZE.search(rd('%s_checks_act.txt' % act))
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), set(json.loads(m.group(3).replace("'", '"')))


def tally(acts, fails_of=None):
    """{standing arm: (acts present, acts at which it read a fault, {pass: acts failing})} over the acts."""
    out = {}
    for act in acts:
        own = own_arms(act)[2]
        rs = dict((pn, read_pass(act, pre)) for pn, pre in PASSES)
        standing = set().union(*[rs[pn]['arms'] for pn in GRADING]) - own
        for a in standing:
            present, fault, by = out.setdefault(a, ([], [], dict((pn, []) for pn, _ in PASSES)))
            present.append(act)
            f = fails_of(act, a, rs) if fails_of else any(a in rs[pn]['fails'] for pn in GRADING)
            if f:
                fault.append(act)
            for pn, _ in PASSES:
                if a in rs[pn]['fails']:
                    by[pn].append(act)
    return out


def control_c():
    out, ok, n = [], 0, 0
    agree, dis, banks, y, nosum = 0, [], 0, [0, 0, 0, 0, 0], []
    for act in ACTS:
        for _pn, prefix in PASSES:
            r = read_pass(act, prefix)
            agree += r['agree']
            dis += r['disagree']
            banks += len(r['parts'])
            y = [a + b for a, b in zip(y, r['yields'])]
            nosum += r['nosum']
    n += 1
    good = not dis
    ok += good
    out.append('  (C) the row reader against each part bank`s own LIVE FAILING list, b754 to b763, every pass: part banks %d ; agreeing %d ; disagreeing %d %s : %s' % (
        banks, agree, len(dis), dis[:3], 'AS WANTED' if good else '### NOT AS WANTED'))
    n += 1
    good = y[4] == 0 and y[3] == banks - len(nosum)
    ok += good
    out.append('  (C) THE SUMMARY MATCHER`S YIELD: summary lines taken %d ; lines with a summary`s head not taken %d (wanted 0) ; banks with no summary line %d %s : %s' % (
        y[3], y[4], len(nosum), nosum[:3], 'AS WANTED' if good else '### NOT AS WANTED'))
    n += 1
    good = y[0] == y[2]
    ok += good
    out.append('  (C) THE ROW FORM`S YIELD: rows taken by the widened form %d ; by a loose form (any four tokens after the arm) %d (wanted equal) ; by b754`s form %d, '
               'beside it and no condition : %s' % (y[0], y[2], y[1], 'AS WANTED' if good else '### NOT AS WANTED'))
    for act in ACTS:
        fr = own_arms(act)
        for pn, pre in PASSES:
            if pn not in GRADING:
                continue
            n += 1
            r = read_pass(act, pre)
            st = len(r['arms'] - fr[2]) if fr else None
            good = fr is not None and st == fr[0]
            ok += good
            out.append('  (C) %s %s: the standing arms by the act`s list %s ; the FREEZE line`s figure %s (the act`s own %d) : %s' % (
                act, pn, st, fr and fr[0], len(fr[2]) if fr else -1, 'AS WANTED' if good else '### NOT AS WANTED'))
    n += 1
    pick = None
    for p in read_pass('b763', 'checks')['parts']:
        t = rd('b763_checks_%s.txt' % p)
        m = re.search(r'(?m)^  (G-[A-Z0-9-]+\s+)PASS', t)
        if m and re.search(r'(?m)^  ### PART \S+ : .*LIVE FAILING 0 NONE', t):
            pick = (p, t, m)
            break
    if pick:
        p, t, m = pick
        planted = t[:m.start()] + '  ' + m.group(1) + 'FAIL' + t[m.end():]
        b, q = compare(t), compare(planted)
        good = b[0] and b[1] and q[0] and not q[1] and q[2] == [m.group(1).strip()]
        out.append('  (C) a planted FAIL row in a bank whose summary prints NONE (b763`s pre-push %s, %s): read %s, agreeing %s -> read %s, agreeing %s, differing %s : %s' % (
            p, m.group(1).strip(), b[0], b[1], q[0], q[1], q[2], 'AS WANTED' if good else '### NOT AS WANTED'))
    else:
        good = False
        out.append('  (C) a planted FAIL row in a bank whose summary prints NONE: no such bank at b763 before the push : ### NOT AS WANTED')
    ok += good
    n += 1
    t0 = tally(ACTS)
    none0 = sorted(a for a, v in t0.items() if not v[1])
    if none0:
        arm = none0[0]
        t1 = tally(ACTS, fails_of=lambda act, a, rs: (a == arm and act == 'b763') or any(a in rs[pn]['fails'] for pn in GRADING))
        good = not t1[arm][1] == [] and t1[arm][1] == ['b763'] and arm not in [a for a, v in t1.items() if not v[1]] \
            and len([a for a, v in t1.items() if not v[1]]) == len(none0) - 1
        out.append('  (C) a planted fault on a standing arm that read none (%s at b763): at none %d -> %d, the arm`s acts %s : %s' % (
            arm, len(none0), len([a for a, v in t1.items() if not v[1]]), t1[arm][1], 'AS WANTED' if good else '### NOT AS WANTED'))
    else:
        good = False
        out.append('  (C) a planted fault on a standing arm that read none: no arm read none -- VACUOUS : ### NOT AS WANTED')
    ok += good
    return out, ok, n


# ---------------------------------------------------------------- the bank
def controls():
    out, ok, n = ['## THE CONTROLS, BEFORE THE FIGURES'], 0, 0
    for f in (control_a, control_c):
        o, k, m = f()
        out += o
        ok += k
        n += m
    out.append('### ### **CONTROLS %d OF %d AS WANTED**' % (ok, n))
    return out, ok, n


def figures():
    L = ['', '## (A) THE HOURS BY THE STEP ROWS, b754 TO b763 (the opening row -> the lock -> the closing), each phase`s hours beside them',
         '## a phase`s hours: the spans from each row`s predecessor to the row, summed by the row`s phase, the opening row`s none; rounded to 0.01 h']
    ol, lc, oc = [], [], []
    for act in ACTS:
        s = spans(act)
        if 'lock' in s and 'closing' in s:
            L.append('  %s  open %s %s -> lock %s %s : %5.2f h ; lock -> closing %s %s : %5.2f h ; open -> closing %5.2f h ; rows %d' % (
                act, s['open'][0], s['open'][1], s['lock'][0], s['lock'][1], s['open_lock'], s['closing'][0], s['closing'][1], s['lock_closing'],
                s['open_closing'], s['rows']))
            ol.append(s['open_lock'])
            lc.append(s['lock_closing'])
            oc.append(s['open_closing'])
        else:
            L.append('  %s  open %s %s -> lock %s : %s ; ### THE STEP ROWS CARRY NO %s ROW: lock -> closing NOT A ROW, open -> closing NOT A ROW ; '
                     'the last row %s %s (phase %s), %.2f h from the opening row ; rows %d' % (
                         act, s['open'][0], s['open'][1], s['lock'][0] if 'lock' in s else '-', ('%5.2f h' % s['open_lock']) if 'open_lock' in s else 'NOT A ROW',
                         'CLOSING' if 'closing' not in s else 'LOCK', s['last'][0], s['last'][1], s['last'][2], s['open_last_s'] / 3600.0, s['rows']))
        L.append('        phases: %s' % ' ; '.join('%s %.2f h' % (p, s['phases'][p] / 3600.0) for p in s['order']))
    L.append('  (each span from its two rows; open -> closing from its own two rows, so the two spans may sum 0.01 h apart from it)')
    L.append('  ### ### **(A) ACTS WITH A LOCK ROW AND A CLOSING ROW %d OF %d ; OPEN -> CLOSING %.2f TO %.2f h ; LOCK -> CLOSING %.2f TO %.2f h ; OPEN -> LOCK %.2f TO %.2f h**' % (
        len(oc), len(ACTS), min(oc), max(oc), min(lc), max(lc), min(ol), max(ol)))
    L += ['', '## (C) THE STANDING ARMS, b754 TO b763: each with the acts at which it read a fault (LIVE FAIL before or after the push), by number;',
          '## beside it, not counted: the acts at which it read FAIL in the pre-run and in the previous act`s mode; present: the acts whose banks carry it']
    t = tally(ACTS)
    for act in ACTS:
        fr = own_arms(act)
        L.append('  %s: the FREEZE line`s standing arms %d, carried %d ; the act`s own %d, not standing' % (act, fr[0], fr[1], len(fr[2])))
    some = sorted((a for a, v in t.items() if v[1]), key=lambda a: (-len(t[a][1]), a))
    none = sorted(a for a, v in t.items() if not v[1])
    L.append('  -- THE STANDING ARMS THAT READ A FAULT AT ONE ACT OR MORE (%d), most acts first:' % len(some))
    for a in some:
        present, fault, by = t[a]
        L.append('  %-34s faults at %2d of %2d present: %s | pre-run %s | prev-mode %s' % (
            a, len(fault), len(present), ' '.join(x[1:] for x in fault), ' '.join(x[1:] for x in by['pre-run']) or '-',
            ' '.join(x[1:] for x in by['prev-mode']) or '-'))
    L.append('  -- THE STANDING ARMS THAT READ A FAULT AT NONE OF THE TEN (%d), for the author`s strike ((R374)(6); nothing removed on it by b764):' % len(none))
    for a in none:
        present, fault, by = t[a]
        L.append('  %-34s present at %2d ; pre-run %s | prev-mode %s' % (a, len(present), ' '.join(x[1:] for x in by['pre-run']) or '-',
                                                                     ' '.join(x[1:] for x in by['prev-mode']) or '-'))
    L.append('  ### ### **(C) STANDING ARMS %d ; READ A FAULT AT ONE ACT OR MORE %d ; AT NONE %d ; sum equal %s**' % (len(t), len(some), len(none),
                                                                                                             len(some) + len(none) == len(t)))
    L += ['', '## THE SENTENCE OF (R374)(6), its fields filled from (A) and (C) above (the acts with both rows for the hours):',
          '  From b754 to b763 an act ran %.2f to %.2f hours from its opening row to its closing, %.2f to %.2f of them from the lock to the closing; of %d standing '
          'arms %d read a fault at one act or more of the ten and %d at none, the %d listed in relay data/b764_close_yield.txt for the author\'s strike' % (
              min(oc), max(oc), min(lc), max(lc), len(t), len(some), len(none), len(none))]
    return L


def main():
    mode = sys.argv[1] if sys.argv[1:] else 'control'
    out, ok, n = controls()
    head = ['b764 -- THE CLOSE`S HOURS AND YIELD, (R374)(6): (A) the hours by the step rows, (C) the standing arms` faults, b754 to b763 (written %sZ by '
            'tools/b764_yield.py, carried from tools/b754_yield.py)' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S'),
            '', '### every figure read from a step row or a suite bank; none estimated. The controls print before the figures. Nothing is removed on this bank.', '']
    print(NL.join(out))
    if mode == 'control':
        return
    if ok != n:
        sys.exit('### CONTROLS %d OF %d -- NO FIGURE PRINTED, NOTHING WRITTEN' % (ok, n))
    L = head + out + figures()
    text = NL.join(L) + NL
    if mode == 'run':
        with open(OUT + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)
        os.replace(OUT + '.tmp', OUT)
        print('WRITTEN data/b764_close_yield.txt, %d lines' % len(L))
    else:
        print(text)


if __name__ == '__main__':
    main()
