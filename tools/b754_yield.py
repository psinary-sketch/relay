# -*- coding: utf-8 -*-
"""b754, (R364)(4)(i): THE CLOSE'S YIELD, data/b754_close_yield.txt. Committed before its run; its controls printed before its figures.

  (A) from the step rows of b744 to b753 (data/<act>_steps.json): the hours from the act's opening row to the line's commit (the first row
      before the lock whose subject names the INTEGRATION line), from there to the lock (the row of phase lock), and from the lock to the
      closing (the row of phase closing); where no row before the lock names the line, the opening-to-lock span is printed whole and its
      split NOT A ROW OF ITS OWN -- no figure estimated.
  (B) from the arm-seconds and suite banks of b753: each part's seconds by pass, int() of the run's seconds as each part bank's summary
      line prints it (tools/standing/fold/checks.tpl :2364), the figure the arm-seconds banks carry (:2388); amended after the opening
      control run read the rounded "the run took N s" (:2360) against the floored :93 and printed NOT AS WANTED (data/b754_defects.txt (h'));
      amended again after the second run read the int() for 2 parts of 10, the summary matcher taking a list and not NONE ((i')).
  (C) from the suite banks of b724 to b753, by pass -- the arms' pre-run (data/<act>_arms_prerun_<part>.txt), the run before the push
      (data/<act>_checks_<part>.txt), the run after it (data/<act>_checks_postpush_<part>.txt), the previous act's mode
      (data/<act>_prevrun_<part>.txt): an arm reads failing in a pass where its LIVE column reads FAIL in a part bank of that pass; for each
      arm the acts at which it read failing, pass by pass; for each act and pass the failures no other pass of the same act printed; an act
      whose banks do not tell the passes apart (a pass absent, or two passes' part banks byte for byte the same) printed as such.
  (D) the hook's refusals by kind and act, b744 to b753 (data/<act>_hook_refusals.txt, one refusal a line, its kind the second field).
  (E) the act module's lines and the lines the carry changed, b744 to b753: the carry bank's head (data/<act>_carry_acts.txt :3) beside
      its diff body's own count, and the module's lines at the act's closing commit.
  (F) the relay's untracked residue by act and kind (git ls-files --others --exclude-standard --directory; a kind is a name less its act
      prefix, each run of digits read as #), with its writer candidates -- the tracked tools one of whose lines holds the kind's pieces in
      order, the name cut at the act, each # and a suite part's name (amended from a reading by one stem, b754 (j')) -- and whether a later
      act's tracked tool names one of its files by its whole name; nothing removed, no file name printed.

Controls: (A) b753's component spans whose two ends are step rows, recomputed equal to data/b753_dayend.txt's; (B) b753's pre-run part
seconds equal to data/b753_arm_seconds.txt :93; (C) the row reader agreeing with each part bank's own LIVE FAILING list, the summary
matcher's yield (every line with a summary's head taken), a planted failing row counted, and a planted FAIL row in a bank whose summary
prints NONE read as a disagreement; (D) a planted refusal line counted, b753's lines 39; (E) each carry head equal to its diff body; (F) a planted name
classified, root entries among them, and the writer reading on two kinds whose writers are read by line (tools/standing/repeat.py :99,
tools/b709_pairs.py :133), a planted kind no tool names, this generator never its own candidate, and a short kind below the floor.
argv: control | run."""
import io, json, os, re, subprocess, sys, datetime
R = r'D:\relay'
D = os.path.join(R, 'data')
NL = '\n'
OUT = os.path.join(D, 'b754_close_yield.txt')
ACTS_A = ['b%d' % n for n in range(744, 754)]
ACTS_C = ['b%d' % n for n in range(724, 754)]
PASSES = [('pre-run', 'arms_prerun'), ('pre-push', 'checks'), ('post-push', 'checks_postpush'), ('prev-mode', 'prevrun')]
PART = re.compile(r'^(act|standing-[a-z0-9]+)$')
ROW = re.compile(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+([0-9.]+)\s+(.*)$')
SUMMARY = re.compile(r'^  ### PART (\S+) : ARMS (\d+) ; LIVE PASSING (\d+) ; LIVE FAILING (\d+) (\[[^\]]*\]|NONE)')   # ### NONE where no arm fails (b754 (i'))
SUMHEAD = re.compile(r'^  ### PART \S+ : ARMS ')   # ### a summary line's head, its yield beside SUMMARY's (b754 (i'))
TOOK = re.compile(r'^  ### the run took (\d+) s')   # ### %.0f of the run's seconds (tools/standing/fold/checks.tpl :2360), printed beside
INTSECS = re.compile(r'^  ### PART \S+ : .* ; (\d+) s ; WITHHELD')   # ### int() of the same seconds (checks.tpl :2364), as the arm-seconds banks (:2388)
T = lambda s: datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')   # noqa: E731
H = lambda a, b: round((T(b) - T(a)).total_seconds() / 3600, 2)   # noqa: E731


def rd(name):
    return io.open(os.path.join(D, name), encoding='utf-8').read().replace('\r', '')


def git(*a):
    return subprocess.run(['git', '-C', R] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# ---------------------------------------------------------------- (A)
def steps(act):
    return json.load(io.open(os.path.join(D, act + '_steps.json'), encoding='utf-8'))['rows']


def spans(act):
    rows = steps(act)
    lock = [r for r in rows if r['phase'] == 'lock']
    clo = [r for r in rows if r['phase'] == 'closing']
    if not lock or not clo:
        return dict(act=act, rows=len(rows), missing='lock' if not lock else 'closing')
    lk = lock[0]
    before = rows[:rows.index(lk)]
    line = [r for r in before if re.search(r'INTEGRATION line', r['subject'])]
    o = rows[0]
    d = dict(act=act, rows=len(rows), open=(o['commit'][:8], o['at']), lock=(lk['commit'][:8], lk['at']), closing=(clo[-1]['commit'][:8], clo[-1]['at']))
    if line:
        d['line'] = (line[0]['commit'][:8], line[0]['at'])
        d['open_line'] = H(o['at'], line[0]['at'])
        d['line_lock'] = H(line[0]['at'], lk['at'])
    d['open_lock'] = H(o['at'], lk['at'])
    d['lock_closing'] = H(lk['at'], clo[-1]['at'])
    d['open_closing'] = H(o['at'], clo[-1]['at'])   # ### from the rows, not the sum of rounded spans (b754 (j'))
    return d


DAYEND = [  # (the dayend's line, its needle, its figure, the step rows' commits whose span it is)
    (30, 'COMPONENT 1      15:44:38Z to 16:34:46Z (step row 13, c68fab6b): 0.84 h', 0.84, ('46123070', 'c68fab6b')),
    (36, 'COMPONENT 2      16:34:46Z to 17:43:20Z (step row 29, 08751eb1): 1.14 h', 1.14, ('c68fab6b', '08751eb1')),
    (45, 'COMPONENT 3      17:43:20Z to 19:19:10Z (step row 34, 576255e0): 1.60 h', 1.60, ('08751eb1', '576255e0')),
    (53, 'COMPONENT 4      19:19:10Z to the lock, 00:37:54Z (step row 45, dcc3116b): 5.31 h', 5.31, ('576255e0', 'dcc3116b')),
]


def control_a():
    L = rd('b753_dayend.txt').split(NL)
    at = dict((r['commit'][:8], r['at']) for r in steps('b753'))
    out, ok = [], 0
    for ln, needle, fig, (a, b) in DAYEND:
        carries = needle in L[ln - 1]
        got = H(at[a], at[b])
        good = carries and got == fig
        ok += good
        out.append('  (A) data/b753_dayend.txt :%d carries its figure %s ; %.2f h there, %.2f h by this reader from step rows %s to %s : %s' % (
            ln, carries, fig, got, a, b, 'AS WANTED' if good else '### NOT AS WANTED'))
    s = spans('b753')
    out.append('  (A) beside it, not a control: the dayend reads THE DAY from the ruling`s row 14:27:21Z to its own writing 05:20Z (:71); the step rows'
               ' run from %s to %s, %.2f h ; the close from the lock to 05:20Z (:62), the step rows to the closing row %s' % (s['open'][1], s['closing'][1],
                                                                                                                   H(s['open'][1], s['closing'][1]), s['closing'][1]))
    return out, ok, len(DAYEND)


# ---------------------------------------------------------------- (B), (C)
def parts_of(act, prefix):
    pat = re.compile(r'^%s_%s_(.+)\.txt$' % (act, prefix))
    out = []
    for n in sorted(os.listdir(D)):
        m = pat.match(n)
        if m and PART.match(m.group(1)):
            out.append(m.group(1))
    return out


def tracked(path):
    return bool(git('ls-files', '--', path).strip())


def read_part(text):
    """the part bank's arm rows {arm: LIVE}, its summary (part, LIVE FAILING count, list) and its seconds: int() from the summary line, the
    figure the arm-seconds banks carry, or where the summary carries none the rounded "the run took" (marked by a trailing ~)."""
    rows, summ, took, isecs = {}, None, None, None
    for l in text.split(NL):
        m = ROW.match(l)
        if m:
            rows[m.group(1)] = m.group(2)
            continue
        mi = INTSECS.match(l)   # ### read on every line, apart from SUMMARY (b754 (i'))
        if mi:
            isecs = int(mi.group(1))
        m = SUMMARY.match(l)
        if m:
            summ = (m.group(1), int(m.group(4)), [] if m.group(5) == 'NONE' else json.loads(m.group(5)))
            continue
        m = TOOK.match(l)
        if m:
            took = int(m.group(1))
    return rows, summ, (isecs, took)


def summary_yield(text):
    """(summary lines SUMMARY takes, lines with a summary's head it does not take): the matcher's yield, printed beside its count."""
    heads = [l for l in text.split(NL) if SUMHEAD.match(l)]
    taken = sum(1 for l in heads if SUMMARY.match(l))
    return taken, len(heads) - taken


def compare(text):
    """one part bank: (summary read, agreeing, the arms where the rows and the summary's list differ)."""
    rows, summ, _ = read_part(text)
    f = set(a for a, live in rows.items() if live == 'FAIL')
    if summ is None:
        return False, False, []
    ok = set(summ[2]) == f and summ[1] == len(f)
    return True, ok, sorted(f ^ set(summ[2]))


def read_pass(act, prefix):
    parts = parts_of(act, prefix)
    fails, secs, rounded, agree, disagree, raw = set(), {}, {}, 0, [], {}
    taken, untaken, nosum = 0, 0, []
    for p in parts:
        name = '%s_%s_%s.txt' % (act, prefix, p)
        if not tracked('data/' + name):
            continue
        t = rd(name)
        raw[p] = t
        rows, summ, took = read_part(t)
        f = set(a for a, live in rows.items() if live == 'FAIL')
        fails |= f
        secs[p] = took[0]
        rounded[p] = took[1]
        y = summary_yield(t)
        taken += y[0]
        untaken += y[1]
        read, ok, diff = compare(t)
        if not read:
            nosum.append(name)
        elif ok:
            agree += 1
        else:
            disagree.append((name, diff))
    return dict(parts=sorted(raw), fails=fails, secs=secs, rounded=rounded, agree=agree, disagree=disagree, raw=raw,
                taken=taken, untaken=untaken, nosum=nosum)


def control_b():
    head = rd('b753_arm_seconds.txt').split(NL)[92]
    want = dict((p, int(s)) for p, s in re.findall(r'(act|standing-[a-z0-9]+) (\d+) s', head))
    r = read_pass('b753', 'arms_prerun')
    got = r['secs']
    ok = bool(want) and all(got.get(p) == s for p, s in want.items()) and set(got) == set(want)
    return ['  (B) b753`s pre-run part seconds by this reader, int() from each part`s summary line, %s ; data/b753_arm_seconds.txt :93 %s ; summed %d and %d : %s' % (
        sorted(got.items()), sorted(want.items()), sum(v for v in got.values() if v), sum(want.values()), 'AS WANTED' if ok else '### NOT AS WANTED'),
            '  (B) beside it, not a control: the same seconds rounded, each part`s "the run took" line (checks.tpl :2360), %s, summed %d' % (
                sorted(r['rounded'].items()), sum(v for v in r['rounded'].values() if v))], int(ok), 1


def control_c():
    out, ok, n = [], 0, 0
    tot_agree, tot_dis, banks, taken, untaken, nosum = 0, [], 0, 0, 0, []
    for act in ACTS_C:
        for _pn, prefix in PASSES:
            r = read_pass(act, prefix)
            tot_agree += r['agree']
            tot_dis += r['disagree']
            banks += len(r['parts'])
            taken += r['taken']
            untaken += r['untaken']
            nosum += r['nosum']
    n += 1
    good = not tot_dis
    ok += good
    out.append('  (C) the row reader against each part bank`s own LIVE FAILING list, b724 to b753, every pass: agreeing %d ; disagreeing %d %s : %s' % (
        tot_agree, len(tot_dis), tot_dis[:3], 'AS WANTED' if good else '### NOT AS WANTED'))
    n += 1
    good = untaken == 0
    ok += good
    out.append('  (C) THE SUMMARY MATCHER`S YIELD (b754 (i`)): part banks read %d ; summary lines taken %d ; lines with a summary`s head not taken %d (wanted 0) ; '
               'banks compared %d ; banks with no summary line %d %s, printed for the hand read and no condition : %s' % (
                   banks, taken, untaken, tot_agree + len(tot_dis), len(nosum), nosum[:3], 'AS WANTED' if good else '### NOT AS WANTED'))
    t = rd('b753_arms_prerun_standing-c.txt')
    m = re.search(r'(?m)^  (G-[A-Z0-9-]+\s+)PASS', t)
    sm = re.search(r'(?m)^  ### PART standing-c : .*LIVE FAILING 0 NONE', t)
    n += 1
    if m and sm:
        planted = t[:m.start()] + '  ' + m.group(1) + 'FAIL' + t[m.end():]
        b, p = compare(t), compare(planted)
        good = b[0] and b[1] and p[0] and not p[1] and p[2] == [m.group(1).strip()]
        out.append('  (C) a planted FAIL row in a bank whose summary prints NONE (b753`s pre-run standing-c, %s): read %s, agreeing %s -> read %s, agreeing %s, '
                   'differing %s : %s' % (m.group(1).strip(), b[0], b[1], p[0], p[1], p[2], 'AS WANTED' if good else '### NOT AS WANTED'))
    else:
        good = False
        out.append('  (C) a planted FAIL row in a bank whose summary prints NONE: the bank`s row or its NONE summary not found (row %s, summary %s) : ### NOT AS WANTED' % (
            bool(m), bool(sm)))
    ok += good
    t = rd('b753_checks_act.txt')
    m = re.search(r'(?m)^  (G-DRY-STEP-CLEAN\s+)PASS', t)
    planted = t[:m.start()] + '  ' + m.group(1) + 'FAIL' + t[m.end():]
    before = set(a for a, v in read_part(t)[0].items() if v == 'FAIL')
    after = set(a for a, v in read_part(planted)[0].items() if v == 'FAIL')
    n += 1
    good = after - before == {'G-DRY-STEP-CLEAN'} and len(after) == len(before) + 1
    ok += good
    out.append('  (C) a planted failing row (b753`s act part before the push, G-DRY-STEP-CLEAN`s LIVE set to FAIL): failing %d -> %d, the planted arm counted %s : %s' % (
        len(before), len(after), 'G-DRY-STEP-CLEAN' in after, 'AS WANTED' if good else '### NOT AS WANTED'))
    return out, ok, n


# ---------------------------------------------------------------- (D)
KIND = re.compile(r'^\S+ \| ([A-Z]+) \| ')


def kinds_of(text):
    c = {}
    for l in text.split(NL):
        m = KIND.match(l)
        if m:
            c[m.group(1)] = c.get(m.group(1), 0) + 1
    return c


def control_d():
    t = rd('b753_hook_refusals.txt')
    k = kinds_of(t)
    planted = t.rstrip(NL) + NL + '2026-11-12T00:00:00Z | PLANTED | Bash | "x" | a planted line' + NL
    k2 = kinds_of(planted)
    good = sum(k.values()) == 39 and sum(k2.values()) == 40 and k2.get('PLANTED') == 1
    return ['  (D) b753`s refusals by this reader %d (wanted 39, data/b754_corrigendum.txt`s count) ; a planted line: %d -> %d, its kind counted %s : %s' % (
        sum(k.values()), sum(k.values()), sum(k2.values()), k2.get('PLANTED') == 1, 'AS WANTED' if good else '### NOT AS WANTED')], int(good), 1


# ---------------------------------------------------------------- (E)
def carry(act):
    t = rd(act + '_carry_acts.txt').split(NL)
    m = re.search(r'(\d+) lines, (\d+) lines changed', t[2]) if len(t) > 2 else None
    plus = sum(1 for l in t if l.startswith('  +') and not l.startswith('  +++'))
    minus = sum(1 for l in t if l.startswith('  -') and not l.startswith('  ---'))
    return (int(m.group(1)), int(m.group(2))) if m else None, plus, minus


def control_e():
    out, ok = [], 0
    for act in ACTS_A:
        head, plus, minus = carry(act)
        good = head is not None and head[1] == plus == minus
        ok += good
        out.append('  (E) data/%s_carry_acts.txt :3 %s ; its diff body + %d - %d : %s' % (act, head, plus, minus, 'AS WANTED' if good else '### NOT AS WANTED'))
    return out, ok, len(ACTS_A)


# ---------------------------------------------------------------- (F)
ACTNAME = re.compile(r'(?:^|/)(?:_|audit_)?(b\d{3})[_./-]')


def classify(path):
    base = path.rstrip('/')
    m = ACTNAME.search(base)
    act = m.group(1) if m else 'none'
    rest = base.split('/')[-1]
    if m:
        rest = rest.replace(act, '<act>', 1)
    kind = re.sub(r'\d+(?:\.\d+)?', '#', rest) + ('/' if path.endswith('/') else '')
    if '/' not in base:   # ### an entry at the repository's root: its own name, no folder doubled (b754 (j'))
        return act, kind
    top = base.split('/')[0]
    return act, top + '/' + kind


PARTNAME = re.compile(r'(?<=_)(?:act|standing-[a-z#]+)(?=[_.]|$)')   # ### a suite part's name inside a kind, cut as a builder's field
SELF = 'tools/b754_yield.py'   # ### this generator, whose own controls name planted kinds: never a candidate (b754 (j'))


def pieces(kind):
    """the kind's literal pieces, in order: its name less the folder, cut at <act>, at each # and at a suite part's name; pieces under 3
    characters dropped. A tool that builds the name puts these pieces on one line around its fields."""
    name = kind.rstrip('/').split('/')[-1]
    name = PARTNAME.sub('\0', name).replace('<act>', '\0').replace('#', '\0')   # ### the part first, its own # inside it
    return [p for p in name.split('\0') if len(p) >= 3]


def names_kind(text, ps):
    """True where one line of the text holds every piece, in order."""
    for l in text.split(NL):
        i = 0
        for p in ps:
            j = l.find(p, i)
            if j < 0:
                break
            i = j + len(p)
        else:
            return True
    return False


FLOOR = 5   # ### the longest piece under 5 characters names nothing: printed BELOW THE FLOOR, not NONE


def candidates(kind, texts):
    ps = pieces(kind)
    if not ps or max(len(p) for p in ps) < FLOOR:
        return ps, None
    return ps, sorted(p for p, t in texts.items() if p != SELF and all(x in t for x in ps) and names_kind(t, ps))


def control_f():
    cases = [('data/b999_scanfile_c1.md', ('b999', 'data/<act>_scanfile_c#.md')),
             ('data/audit_b999_reg_satisfiable.txt', ('b999', 'data/audit_<act>_reg_satisfiable.txt')),
             ('data/_b999_probe/', ('b999', 'data/_<act>_probe/')),
             ('data/b999_list_units_band_15.0_30.jsonl', ('b999', 'data/<act>_list_units_band_#_#.jsonl'))]
    cases += [('records.json', ('none', 'records.json')), ('scratch/', ('none', 'scratch/'))]   # ### root entries (b754 (j'))
    out, ok = [], 0
    for p, want in cases:
        got = classify(p)
        ok += got == want
        out.append('  (F) a planted name classified %s -> %s : %s' % (want[1].replace('<act>', 'b999'), got, 'AS WANTED' if got == want else '### NOT AS WANTED'))
    texts = tool_texts()
    wcases = [   # ### (kind, a tool wanted among its candidates or None for none, a tool wanted absent): the writer reading's controls (b754 (j'))
        ('data/<act>_mid_exercise_standing-b#a.json', 'tools/standing/repeat.py', None),   # ### repeat.py :99 builds the name from its part
        ('data/<act>_pairs_units_band_#_#.jsonl', 'tools/b709_pairs.py', None),            # ### b709_pairs.py :133
        ('data/<act>_zq_planted_nowhere.txt', None, None),                                 # ### a planted kind no tool names
        ('data/<act>_scanfile_c#.md', '', SELF),                                           # ### this generator never its own candidate
    ]
    for kind, want, absent in wcases:
        ps, cs = candidates(kind, texts)
        if want is None:
            good = cs == []
        elif want == '':
            good = cs is not None and absent not in cs
        else:
            good = cs is not None and want in cs
        ok += good
        out.append('  (F) the writer reading on %s, pieces %s: %s candidate(s)%s : %s' % (
            kind, ps, 'BELOW THE FLOOR' if cs is None else len(cs),
            (' ; %s among them %s' % (want, want in (cs or []))) if want else (' ; %s among them %s' % (absent, absent in (cs or []))) if absent else '',
            'AS WANTED' if good else '### NOT AS WANTED'))
    ps, cs = candidates('tools/_a#.txt', texts)
    good = cs is None
    ok += good
    out.append('  (F) a kind whose longest piece is under %d characters (tools/_a#.txt, pieces %s) printed BELOW THE FLOOR %s : %s' % (
        FLOOR, ps, cs is None, 'AS WANTED' if good else '### NOT AS WANTED'))
    stands = os.path.exists(OUT) and not tracked(OWN)
    listed = OWN in residue_lines()
    read = OWN in residue_read()
    good = (not stands or listed) and not read
    ok += good
    out.append('  (F) this bank`s own path (%s): stands untracked %s, in git`s listing %s, read as residue %s (wanted False) : %s%s' % (
        OWN, stands, listed, read, 'AS WANTED' if good else '### NOT AS WANTED',
        '' if stands else ' -- VACUOUS, the bank not standing untracked, the exclusion not exercised'))
    return out, ok, len(cases) + len(wcases) + 2


OWN = 'data/b754_close_yield.txt'


def residue_lines():
    return [l for l in git('ls-files', '--others', '--exclude-standard', '--directory').split(NL) if l.strip()]


def residue_read():
    """the residue (F) reads: git's listing less this bank's own path, never its own residue (b754 (k'))."""
    return [l for l in residue_lines() if l != OWN]


def tool_texts():
    texts = {}
    for p in [l for l in git('ls-files', '--', 'tools/').split(NL) if l.strip()]:
        try:
            texts[p] = io.open(os.path.join(R, p), encoding='utf-8', errors='replace').read()
        except OSError:
            pass
    return texts


def residue():
    lines = residue_read()
    texts = tool_texts()
    by = {}
    for p in lines:
        act, kind = classify(p)
        by.setdefault((act, kind), []).append(p)
    rows = []
    memo = {}
    for (act, kind), ps in sorted(by.items()):
        if kind not in memo:
            memo[kind] = candidates(kind, texts)
        stem, writers = memo[kind]   # ### stem: the kind's pieces; writers: the candidates, or None below the floor (b754 (j'))
        n = int(act[1:]) if act != 'none' else None
        later = 0
        if n is not None:
            names = [x.rstrip('/').split('/')[-1] for x in ps]
            lt = [p for p in texts if re.search(r'(?:^|/)b(\d{3})[_.]', p) and int(re.search(r'(?:^|/)b(\d{3})[_.]', p).group(1)) > n]
            later = sum(1 for nm in names if any(nm in texts[p] for p in lt))
        rows.append((act, kind, len(ps), stem, writers, later))
    return lines, rows


# ---------------------------------------------------------------- the bank
def controls():
    out, ok, n = ['## THE CONTROLS, BEFORE THE FIGURES'], 0, 0
    for f in (control_a, control_b, control_c, control_d, control_e, control_f):
        o, k, m = f()
        out += o
        ok += k
        n += m
    out.append('### ### **CONTROLS %d OF %d AS WANTED**' % (ok, n))
    return out, ok, n


def figures():
    L = ['', '## (A) THE HOURS BY THE STEP ROWS, b744 TO b753 (opening row -> the line`s commit -> the lock -> the closing)']
    for act in ACTS_A:
        s = spans(act)
        if 'missing' in s:
            L.append('  %s  ### the step rows carry no %s row' % (act, s['missing']))
            continue
        if 'line' in s:
            L.append('  %s  open %s %s -> line %s %s : %5.2f h ; line -> lock %s : %5.2f h ; lock -> closing %s : %5.2f h ; open -> closing %5.2f h' % (
                act, s['open'][0], s['open'][1], s['line'][0], s['line'][1], s['open_line'], s['lock'][0], s['line_lock'], s['closing'][0], s['lock_closing'],
                s['open_closing']))
        else:
            L.append('  %s  open %s %s -> lock %s %s : %5.2f h, the line`s commit NOT A ROW OF ITS OWN (no row before the lock names it) ; lock -> closing %s : %5.2f h ; open -> closing %5.2f h' % (
                act, s['open'][0], s['open'][1], s['lock'][0], s['lock'][1], s['open_lock'], s['closing'][0], s['lock_closing'], s['open_closing']))
    L.append('  (each span from its two rows, rounded to 0.01 h; open -> closing from its own two rows, so the three spans may sum 0.01 h apart from it)')
    L += ['', '## (B) b753`S PART SECONDS BY PASS (int() of each part`s seconds from its summary line, the arm-seconds banks` figure; the rounded "the run took" differs by 1 s at most)']
    allp = {}
    for pn, prefix in PASSES:
        allp[pn] = read_pass('b753', prefix)
    parts = sorted(set(p for r in allp.values() for p in r['secs']))
    L.append('  %-14s %s' % ('part', '  '.join('%10s' % pn for pn, _ in PASSES)))
    def cell(pn, p):   # ### int() from the summary line; where it carries none, the rounded "the run took" marked ~ (b754 (i'))
        r = allp[pn]
        if r['secs'].get(p) is not None:
            return r['secs'][p], ''
        if r['rounded'].get(p) is not None:
            return r['rounded'][p], '~'
        return None, '-'
    for p in parts:
        L.append('  %-14s %s' % (p, '  '.join('%10s' % (('%d%s' % c) if c[0] is not None else '-') for c in (cell(pn, p) for pn, _ in PASSES))))
    sums = []
    for pn, _ in PASSES:
        cs = [cell(pn, p) for p in parts]
        sums.append('%d%s' % (sum(c[0] for c in cs if c[0] is not None), '~' if any(c[1] == '~' for c in cs) else ''))
    L.append('  %-14s %s' % ('a pass', '  '.join('%10s' % s for s in sums)))
    L.append('  (a figure marked ~ is the rounded "the run took" of a part whose summary line carries no int(); a pass`s sum marked ~ holds one; - no bank)')
    L += ['', '## (C) THE PASSES` FAILURES, b724 TO b753 (an arm failing where its LIVE column reads FAIL in a part bank of the pass)',
          '## per act: each pass`s failing arms counted, and those no other pass of the act printed, by name']
    per = {}
    for act in ACTS_C:
        rs = dict((pn, read_pass(act, prefix)) for pn, prefix in PASSES)
        per[act] = rs
        absent = [pn for pn, r in rs.items() if not r['parts']]
        same = []
        names = [pn for pn, _ in PASSES]
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                a, b = rs[names[i]], rs[names[j]]
                if a['parts'] and a['parts'] == b['parts'] and all(a['raw'][p] == b['raw'][p] for p in a['parts']):
                    same.append('%s=%s' % (names[i], names[j]))
        head = '  %s  %s' % (act, ' ; '.join('%s %d' % (pn, len(rs[pn]['fails'])) if rs[pn]['parts'] else '%s ABSENT' % pn for pn in names))
        if absent or same:
            head += '  ### NOT TOLD APART: %s' % ', '.join(['absent ' + x for x in absent] + ['byte-equal ' + x for x in same])
        L.append(head)
        for pn in names:
            others = set().union(*[rs[q]['fails'] for q in names if q != pn])
            only = sorted(rs[pn]['fails'] - others)
            if only:
                L.append('      only the %s pass: %s' % (pn, ', '.join(only)))
    L += ['', '## (C) EACH ARM THAT READ FAILING, THE ACTS AT WHICH IT DID, PASS BY PASS (acts by number)']
    arms = sorted(set(a for act in ACTS_C for r in per[act].values() for a in r['fails']))
    for a in arms:
        cells = []
        for pn, _ in PASSES:
            acts = [act[1:] for act in ACTS_C if a in per[act][pn]['fails']]
            cells.append('%s %s' % (pn, ' '.join(acts) if acts else '-'))
        L.append('  %-34s %s' % (a, ' | '.join(cells)))
    L.append('  arms that read failing in any pass, b724 to b753: %d' % len(arms))
    L += ['', '## (D) THE HOOK`S REFUSALS BY KIND AND ACT, b744 TO b753']
    ks = {}
    for act in ACTS_A:
        ks[act] = kinds_of(rd(act + '_hook_refusals.txt'))
    allk = sorted(set(k for v in ks.values() for k in v))
    L.append('  %-6s %s  total' % ('act', ' '.join('%9s' % k for k in allk)))
    for act in ACTS_A:
        L.append('  %-6s %s  %5d' % (act, ' '.join('%9s' % (ks[act].get(k, '-')) for k in allk), sum(ks[act].values())))
    L.append('  %-6s %s  %5d' % ('all', ' '.join('%9d' % sum(ks[a].get(k, 0) for a in ACTS_A) for k in allk), sum(sum(v.values()) for v in ks.values())))
    L += ['', '## (E) THE ACT MODULE`S LINES AND THE LINES THE CARRY CHANGED, b744 TO b753 (the carry bank`s head; the module at the act`s closing commit)']
    for act in ACTS_A:
        head, plus, _m = carry(act)
        s = spans(act)
        clo = s.get('closing', (None,))[0]
        n_close = len(git('show', '%s:tools/acts/%s.py' % (clo, act)).split(NL)) - 1 if clo else None
        L.append('  %s  carried %s lines, %s changed by the carry (%.0f%%) ; at the closing %s %s lines' % (
            act, head[0], head[1], 100.0 * head[1] / head[0], clo, n_close))
    L += ['', '## (F) THE RELAY`S UNTRACKED RESIDUE BY ACT AND KIND (git ls-files --others --exclude-standard --directory, read %sZ; nothing removed)' %
          datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S'),
          '## a kind: the name less its act, each run of digits read as #; WRITER CANDIDATES: the tracked tools (this generator not among them) one',
          '## of whose lines holds the kind`s pieces in order -- the name cut at the act, at each # and at a suite part`s name, as a tool that builds',
          '## the name writes it around its fields; a line that names a kind does not tell its writer from a reader, and a name built across lines',
          '## or from a table is not seen: NONE is no line found, not no writer; BELOW THE FLOOR where the longest piece is under %d characters;' % FLOOR,
          '## READ LATER: of the kind`s entries, those a later act`s tracked tool names by their whole name; this bank`s own path is not read']
    lines, rows = residue()
    tot = 0
    for act, kind, n, stem, writers, later in rows:
        tot += n
        if writers is None:
            w = 'BELOW THE FLOOR, pieces %s' % (stem,)
        elif writers:
            w = '%d, e.g. %s' % (len(writers), ', '.join(writers[:2]))
        else:
            w = 'NONE, pieces %s' % (stem,)
        L.append('  %-6s %-48s %4d ; WRITER CANDIDATES %s ; READ LATER %d of %d' % (act, kind[:48], n, w, later, n))
    acts_n = len(set(r[0] for r in rows))
    kinds = {}
    for r in rows:
        kinds[r[1]] = r[4]
    found = sum(1 for v in kinds.values() if v)
    none = sum(1 for v in kinds.values() if v == [])
    floor = sum(1 for v in kinds.values() if v is None)
    L.append('  ### ### **UNTRACKED ENTRIES %d ; ROWS (act and kind) %d ; ACTS %d ; the table`s sum %d, equal %s**' % (len(lines), len(rows), acts_n, tot, tot == len(lines)))
    L.append('  ### THE WRITER READING`S YIELD, by distinct kind: %d kinds ; with candidates %d ; NONE %d ; BELOW THE FLOOR %d ; sum equal %s' % (
        len(kinds), found, none, floor, found + none + floor == len(kinds)))
    return L


def main():
    mode = sys.argv[1] if sys.argv[1:] else 'control'
    out, ok, n = controls()
    head = ['b754 -- THE CLOSE`S YIELD, (R364)(4)(i): (A) the hours by the step rows, (B) b753`s part seconds by pass, (C) the passes` failures,',
            '(D) the hook`s refusals by kind, (E) the act module and the carry, (F) the untracked residue (written %sZ by tools/b754_yield.py)' %
            datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S'),
            '', '### every figure read from a bank, a step row or the tree; none estimated. The controls print before the figures.', '']
    print(NL.join(out))
    if mode == 'control':
        return
    if ok != n:
        sys.exit('### CONTROLS %d OF %d -- NO FIGURE PRINTED, NOTHING WRITTEN' % (ok, n))
    L = head + out + figures()
    text = NL.join(L) + NL
    if mode == 'run':
        io.open(OUT, 'w', encoding='utf-8', newline='\n').write(text)
        print('WRITTEN data/b754_close_yield.txt, %d lines' % len(L))
    else:
        print(text)


if __name__ == '__main__':
    main()
