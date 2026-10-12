# -*- coding: utf-8 -*-
"""b652_record.py -- THE ACT'S RECORD TOOL, b652 under (R262). ### **THE ONE CONVERSION OF A BACKTICK POSSESSIVE LIVES HERE** ((R262)(2)).

### b651's defects (m) and (n) had one cause: a ledger text landed through b641_record._poss (:255; a backtick before a lower-case letter
### written ’) while the look-ups ran through b551_record.poss (:678; `s written 's, straight) -- in guard_absent (:699), line_of (:704),
### append_to (:684) and the suite's poss (b651_checks :382). From this act `conv` below is the one function: the landing, the guard against a
### second landing, the line look-up, and every suite arm or reader that finds a landed line import it from here and convert by nothing else.
### Its rule is the union of the two it replaces, written typographic: a backtick between a letter, a digit or a closing parenthesis and a
### lower-case letter becomes ’. Applied twice it changes nothing more (a text with no such backtick passes through unchanged).

### Routes: `python tools/b652_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CONV = re.compile(r'(?<=[A-Za-z0-9)])`(?=[a-z])')


def conv(t):
    """### THE ONE CONVERSION ((R262)(2)): a backtick standing as an apostrophe -- after a letter, a digit or `)`, before a lower-case letter --
    ### written ’. Every landing and every look-up of a landed line goes through this function."""
    return CONV.sub('’', t)


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '')


def odd_lines(text):
    return [l[:60] for l in text.split(NL) if l.count('`') % 2]


def append_to(path, text):
    """the text converted by conv alone, refused on an odd-backtick line or a live banned stem, appended as bytes; returns the byte counts."""
    text = conv(text)
    if odd_lines(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s: %s' % (path, odd_lines(text)))
    import banned_terms as BT
    live = [m.group(0) for l in text.split(NL) for m in BT.PAT.finditer(l)]
    if live:
        sys.exit('### A BANNED STEM IN THE APPEND TO %s: %s' % (path, live))
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.basename(path), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def guard_absent(path, head):
    if conv(head).encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), head[:80]))


def line_of(path, head):
    """the first line of the ledger that starts with the head, both read through conv."""
    h = conv(head)
    ls = [i + 1 for i, l in enumerate(rd(path).split(NL)) if l.startswith(h)]
    return ls[0] if ls else None


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


# ================================================================================ THE GUARDED LANDING, THE SCREENS OF b633 AND b641
def screens(items, tag, dry):
    """the screens of b633_record and b641_record over the converted texts: table cells, no-disclosure, the scanner, odd backticks by line,
    unread figures, outside names, the two stems; returns (cells, fired) and prints them."""
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b652_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    """items [(file, head, text)]: each converted by conv, screened, each head guarded absent and looked up by conv after its append at the
    line the ledger's length predicts; stops at the first line that lands elsewhere; banks [file, head, line, append]."""
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    print('  cells expected: %s ; equal to the predicted: %s' % (list(expect_cells) or 'NONE', cells == [tuple(x) for x in expect_cells]))
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R262)(1) AND (2)
WH = ('*Appended 2026-10-11 by b652 to b651’s entry (:8229), under `(R262)`(1) -- b651 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b651_closing.txt), ITS FOURTEEN DEFECTS NAMED BY SEAT:*')
CH = ('*Appended 2026-10-11 by b652 beneath b651’s trail record (:13874), under `(R262)`(2) -- THE CONVERSION RULE FOR RECORD LOOK-UPS, '
      'STANDING FROM b652:*')


def _weight():
    return ('\n' + WH + ' relay 6b5cbcfa (the act) and 1a4caf67 (the closing); PLACE-papers a6e63c1; the root 51df0cb6… over 50 banks; the suite '
            '85 arms, sealed at relay be271f14, 78 of 85 before and after the push. The data and page rows repaired and the seam row re-graded '
            'DERIVES in the terminal table and the lattice bank (N1 held). The axiom-claim resolver re-binding a claim said of another named '
            'object: b649’s row 2 re-bound to TraceSilence and graded, row 5 UNBOUND, the four real contradictions unchanged, the planted test '
            '7 of 7. The census at v0.8.1 with CLUSTERS-SERVED: 4 of the 14 split kernels serving fewer than two clusters, SIDE-window served '
            'by one; the glossary’s six entries; both pages re-emitted. The four restated lines read against the build banks, none merged. '
            'SIDE-kernel’s 116 blocks read into 396 sentence rows (relay d7ab2fdb), no docstring edited; the two plain comments re-cut on a '
            'local branch, unmerged. The navigator’s 39 rows printed (relay data/b651_navigator_rows.txt: 33 OVERREACHES, 6 UNDERSTATES). '
            'Fourteen defects (relay data/b651_defects.txt): nine the seat’s -- (a) a probe that ran a whole scan, (b) a resolver grammar '
            'first too wide, (c) backticks split across a line, (d) a heredoc that collapsed a backslash, (e) a glossary source misread, (k) a '
            'commit hash read from the wrong end of a log, (l) a positive control that passed, (m) and (n) the record look-ups by the wrong '
            'conversion; five the navigator’s -- (f) the b650_closing citation, (g) the block-for-row wording of (R261)(7), (h) the sentence-row '
            'assumption, (i) the resolver clause, (j) the row count (the ruling letters the citation (g); the bank letters it (f)). After the '
            'closing the seat’s pass over the b651 banks removed a lone carriage return from relay data/b651_author_answers.txt, a bank the '
            'root names; restored from git, its bytes equal the root’s entry and its write time is later than the root’s (relay '
            'data/b652_defects.txt). Nothing deposited.\n')


def _conv_rule():
    return ('\n' + CH + ' one function converts a backtick possessive in a ledger text -- `conv` in the act’s record tool (relay '
            'tools/b652_record.py): a backtick between a letter, a digit or a closing parenthesis and a lower-case letter is written ’ -- and '
            'the same function converts the head a look-up searches for. The landing, the guard against a second landing, the line look-up, and '
            'every suite arm or reader that finds a landed line import it from the record tool and convert by nothing else. b651’s defects '
            '(m) and (n) had one cause: the record landed through b641_record’s conversion (’) while the look-ups ran through b551_record’s '
            '(a straight apostrophe), so the trail route banked no line and five suite arms failed on a record that stood as written '
            '(FINDINGS :8229, OPEN_TRAILS :13874). The suite carries a planted case: a head with a backtick possessive landed in a scratch '
            'ledger and found by the look-up at the line it landed on, the straight conversion read beside it as the control that misses '
            '(relay tools/test_conversion_b652.py).\n')


def c1(*a):
    dry = 'dry' in a
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', CH, _conv_rule())]
    land(items, 'b652_record_lines.json', 'c1', entry=8229,
         check=[('FINDINGS.md', 8229, '## The re-cuts opened'), ('OPEN_TRAILS.md', 13874, '### b651 — lane three, act seventy-eight')],
         dry=dry)


MH = ('*Appended 2026-10-11 by b652 beneath W-ORD-LV-BUILD-HOST (:13798), under `(R262)`(3) and the author’s word after the strike -- THE '
      'MARGIN TERM CORRECTED, STANDING FROM b652:*')


def _margin_rule():
    return ('\n' + MH + ' the rule (R262)(3) acted -- a module builds under the hold when the free memory at its start less its measured tree '
            'peak stays at or above the hold -- is refuted by b651’s run of Kernel.PerpendicularCrossing (relay '
            'data/b651_docstrings_SIDE-kernel.txt :18-:19, data/b651_build_peaks.json rows 3-4): free 3365 MB at its start, above the 3252 the '
            'rule needed, and the host fell 906 MB to 2459 beneath the hold while the tree’s peak was 683 MB. From this act the margin needed is '
            'the host’s measured loss -- free memory at the start less the host’s low, as the watchdog prints them -- where a run has recorded '
            'one, the largest of its attempts; the tree peak is not a substitute; a module with no recorded loss reads UNMEASURED and no build is '
            'attempted on it. A loss from a run stopped at the hold is a lower bound. The hold stays 2560 MB. Measured at b652: '
            'T3_StepNineBridge 1428 MB, Milestones 1255, PerpendicularCrossing 906; seen 184 and 651 MB above the hold at two readings; no '
            'build started (relay data/b652_build_margin.txt). The navigator’s term, corrected on the author’s word.\n')


def c2(*a):
    land([('OPEN_TRAILS.md', MH, _margin_rule())], 'b652_margin_line.json', 'c2', entry=13798,
         check=[('OPEN_TRAILS.md', 13798, 'W-ORD-LV-BUILD-HOST')], dry='dry' in a)


# ================================================================================ COMPONENT 2: THE MARGIN, (R262)(3)
HOLD = 2560
# ### per module the three unmerged branches touch: (kernel, branch, module, the build command's target, tree peak MB, the bank and line)
MODULES = [
    ('SIDE-lv-conservation', 'b648-restate-SIDE-lv-conservation', 'SIDELvConservation/T3_StepNineBridge.lean', 'SIDELvConservation.T3_StepNineBridge',
     1644, 'relay data/b649_lv_build.txt :16, :43 (attempt 2, tree peak 1644 MB)'),
    ('SIDE-effects', 'b648-restate-SIDE-effects', 'SIDEEffects/Milestones.lean', 'SIDEEffects.Milestones',
     1410, 'relay data/b648_build_peaks.json rows 3-4 (attempt 2, tree peak 1410 MB); data/b648_build_watch.json row 2'),
    ('SIDE-kernel', 'docstrings-SIDE-kernel', 'Kernel/PerpendicularCrossing.lean', 'Kernel.PerpendicularCrossing',
     692, 'relay data/b651_build_peaks.json rows 3-4 (attempt 2, tree peak 692 MB); data/b651_docstrings_SIDE-kernel.txt :17-:22'),
]


# ### THE TERM CORRECTED BY THE AUTHOR`S WORD AFTER THE STRIKE: the margin needed is the host`s measured loss (free at start minus host low, as
# ### the watchdog prints it) where a run has recorded one -- the largest recorded; the tree peak is not a substitute; none recorded: UNMEASURED.
# ### Every loss below is from a run the watchdog stopped at the hold, so it is a lower bound of the run`s whole loss.
LOSS = {
    'SIDELvConservation.T3_StepNineBridge': (1428, 'relay data/b649_lv_build.txt :16: 3545-2135 = 1410 ; 3532-2104 = 1428'),
    'SIDEEffects.Milestones': (1255, 'b648`s log w_b648_milestones.log :1, :31, :34 (data/b648_build_peaks.json rows 3-4): 3788-2533 = 1255 ; 3616-2529 = 1087'),
    'Kernel.PerpendicularCrossing': (906, 'relay data/b651_docstrings_SIDE-kernel.txt :18-:19: 3365-2459 = 906 ; 3151-2441 = 710'),
}


def free_mb():
    import build_watch as BW
    return BW.free_mb()


def _lake_libs():
    """SIDE-kernel's lean_libs (lakefile.lean): Kernel and Bridge by submodules, MetaKernel by root."""
    return ('Kernel/', 'Bridge/'), ('MetaKernel.lean',)


def _procs():
    r = subprocess.run(['powershell', '-NoProfile', '-Command',
                        'Get-Process | Sort-Object WorkingSet64 -Descending | ForEach-Object { "{0}`t{1}`t{2}" -f $_.Name,$_.Id,[math]::Round($_.WorkingSet64/1MB) }'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    rows = []
    for l in (r.stdout or '').split(NL):
        x = l.strip().split('\t')
        if len(x) == 3 and x[2].isdigit():
            rows.append(dict(name=x[0], pid=int(x[1]), ws_mb=int(x[2])))
    return rows


def margin3(*a):
    """the author's answer to the margin prompt: one reading on this host after the author closes every application but Claude Code, printed
    with the processes named. a[0] = 'open' (taken before the author's closing, banked as such) or 'closed' (on the author's word that it is done)."""
    state = a[0] if a else 'open'
    j = jl('b652_build_margin.json') or {'hold': HOLD, 'readings': []}
    fm = free_mb()
    seen = fm - HOLD
    procs = _procs()
    by = {}
    for p in procs:
        by[p['name']] = by.get(p['name'], 0) + p['ws_mb']
    at = utc()
    rows = []
    for k, br, f, tgt, peak, src in MODULES:
        need, lsrc = LOSS[tgt]
        rows.append(dict(reading='3-' + state, at=at, kernel=k, branch=br, module=f, target=tgt, term='host loss', needed=need, free=fm, seen=seen,
                         allows=seen >= need, source=lsrc))
    j['readings'] += rows
    j.setdefault('procs', {})['3-' + state] = dict(at=at, free=fm, by_name=sorted(by.items(), key=lambda kv: -kv[1])[:25], n=len(procs))
    put_json('b652_build_margin.json', j)
    print('  reading 3-%s %s free %d MB, seen %d above the hold ; processes %d' % (state, at, fm, seen, len(procs)))
    for n_, mb in sorted(by.items(), key=lambda kv: -kv[1])[:12]:
        print('    %-40s %6d MB' % (n_, mb))
    for r in rows:
        print('    %-38s needed %4d ; seen %4d ; %s' % (r['target'], r['needed'], r['seen'], 'ALLOWS' if r['allows'] else 'DOES NOT ALLOW'))


def build_row(*a):
    """data/b652_build_results.json: one row per module of the author's build order -- `build_row <target> key=value ...` (slot_seen, outcome
    BUILT / STOPPED / RUN-BENEATH-HOLD / UNBUILT, gate, merged, note); the watchdog's figures (free at start, low, tree peak, seconds) read
    from data/b652_build_peaks.json and the log, the host's loss computed."""
    tgt = a[0]
    kv = dict(x.split('=', 1) for x in a[1:])
    j = jl('b652_build_results.json') or {'rows': []}
    row = next((r for r in j['rows'] if r['target'] == tgt), None)
    if row is None:
        row = dict(target=tgt, needed=LOSS[tgt][0])
        j['rows'].append(row)
    for k_, v in kv.items():
        row[k_] = int(v) if v.lstrip('-').isdigit() else (None if v == 'None' else v)
    pk = [p for p in jl('b652_build_peaks.json').get('rows') or [] if p.get('module') == tgt]
    if pk:
        row['started'] = True
        row['attempts'] = [dict(attempt=p['attempt'], at=p['at'], seconds=p['seconds'], tree_peak=p['tree_peak'], host_low=p['host_low'], rc=p['rc'],
                                stopped=p['stopped']) for p in pk]
        log = rd(pk[-1]['log']) if os.path.exists(pk[-1]['log']) else ''
        starts = [int(m) for m in re.findall(r'^### START attempt \d+ \S+ free (\d+) MB', log, re.M)]
        row['free_at_start'] = starts
        row['loss'] = [s - p['host_low'] for s, p in zip(starts, pk)]
    row.setdefault('started', False)
    put_json('b652_build_results.json', j)
    print(json.dumps(row, ensure_ascii=False))


def gate(*a):
    """the gate reading of one built module before its merge: `gate <target> <kernel> <branch> <file> <log>` -- the watchdog's EXIT 0, no
    `declaration uses 'sorry'` warning in the build's own output, and tools/no_sorry_main.py's code scan of the file at the branch reading no
    `sorry` (sorry_hits); PASS only on all three. Banked into data/b652_build_results.json's row as gate and gate_detail."""
    import no_sorry_main as NSM
    tgt, k, br, f, log = a[:5]
    t = rd(log) if os.path.exists(log) else ''
    exit0 = bool(re.search(r'^### EXIT 0 ', t, re.M))
    warn = [l for l in t.split(NL) if "declaration uses 'sorry'" in l]
    src = subprocess.run(['git', '-C', 'D:/' + k, 'show', '%s:%s' % (br, f)], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '')
    hits = NSM.sorry_hits(src) if src else ['### UNREAD']
    ok = exit0 and not warn and not hits and bool(src)
    j = jl('b652_build_results.json') or {'rows': []}
    row = next((r for r in j['rows'] if r['target'] == tgt), None)
    detail = dict(exit0=exit0, sorry_warnings=warn[:5], code_sorry_hits=[list(h) if isinstance(h, tuple) else h for h in hits][:5], file=f, branch=br,
                  at=utc())
    if row is not None:
        row['gate'] = 'PASS' if ok else 'FAIL'
        row['gate_detail'] = detail
        put_json('b652_build_results.json', j)
    print('  gate %s : %s ; %s' % (tgt, 'PASS' if ok else 'FAIL', json.dumps(detail, ensure_ascii=False)[:600]))


def margin2(*a):
    """the second reading under the corrected term: per module of the three branches, per file of the cut branch; banked, the text too."""
    j = jl('b652_build_margin.json') or {'hold': HOLD, 'readings': []}
    fm = free_mb()
    seen = fm - HOLD
    at = utc()
    for k, br, f, tgt, peak, src in MODULES:
        need, lsrc = LOSS[tgt]
        j['readings'].append(dict(reading=2, at=at, kernel=k, branch=br, module=f, target=tgt, term='host loss', needed=need, free=fm, seen=seen,
                                  allows=seen >= need, source=lsrc))
    plan = jl('b652_sentence_cut_plan.json')['blocks']
    files = sorted(set(b['file'] for b in plan if b.get('kept') is not None) | {'Kernel/PerpendicularCrossing.lean'})
    subs, roots = _lake_libs()
    cut = []
    for f in files:
        in_lib = f.startswith(subs) or f in roots
        tgt = f[:-5].replace('/', '.')
        if tgt in LOSS:
            need, lsrc = LOSS[tgt]
            cut.append(dict(file=f, lib=in_lib, needed=need, seen=seen, allows=seen >= need, source=lsrc))
        else:
            cut.append(dict(file=f, lib=in_lib, needed=None, seen=seen, allows=False,
                            source='UNMEASURED: no recorded host loss' if in_lib else 'UNMEASURED: in no lean_lib (legacy/), nothing builds it'))
    j['cut_branch'] = dict(at=at, branch=PC_BRANCH, free=fm, seen=seen, files=cut)
    put_json('b652_build_margin.json', j)
    print('  reading 2 %s free %d MB, seen %d above the hold' % (at, fm, seen))
    for r in [r for r in j['readings'] if r['reading'] == 2]:
        print('    %-38s needed %4d ; seen %4d ; %s' % (r['target'], r['needed'], r['seen'], 'ALLOWS' if r['allows'] else 'DOES NOT ALLOW'))
    print('    cut branch: files %d ; measured %d ; UNMEASURED in a lean_lib %d ; in no lean_lib %d' % (
        len(cut), sum(1 for c in cut if c['needed']), sum(1 for c in cut if not c['needed'] and c['lib']), sum(1 for c in cut if not c['lib'])))


def margin(*a):
    """one reading per module at its slot's start: the margin needed (the tree peak, MB above the hold) beside the margin seen (free memory
    less the hold); ALLOWS where seen >= needed. Appended to data/b652_build_margin.json under the reading's number (a[0], 1 or 2)."""
    n = a[0] if a else '1'
    j = jl('b652_build_margin.json') or {'hold': HOLD, 'readings': []}
    for k, br, f, tgt, peak, src in MODULES:
        fm = free_mb()
        seen = fm - HOLD
        row = dict(reading=int(n), at=utc(), kernel=k, branch=br, module=f, target=tgt, needed=peak, free=fm, seen=seen,
                   allows=seen >= peak, source=src)
        j['readings'].append(row)
        print('  reading %s %s %-36s needed %4d MB ; seen %4d MB (free %d, hold %d) ; %s' % (n, row['at'], tgt, peak, seen, fm, HOLD,
                                                                                         'ALLOWS' if row['allows'] else 'DOES NOT ALLOW'))
    put_json('b652_build_margin.json', j)


# ================================================================================ COMPONENT 3: THE SENTENCE GRADES AND THE CUT, (R262)(4)
SENT = 'b651_table_SIDE-kernel_sentences.json'       # ### b651's sentence rows, relay d7ab2fdb
PARENTS = 'b647_table_SIDE-kernel.json'              # ### the parent blocks' HAND cells
GRADES = 'b652_sentence_grades.json'                 # ### the hand grades per sentence, bound to the parent's LICENSED cell


def _ws(s):
    return ' '.join(s.split())


def blocks():
    """[(k, parent id, parent row, [sentence rows])] in the sentence bank's order, k from 1."""
    import collections
    s = jl(SENT)['rows']
    t = dict((r['id'], r) for r in jl(PARENTS)['rows'])
    by = collections.OrderedDict()
    for r in s:
        by.setdefault(r['parent'], []).append(r)
    return [(k, p, t[p], rs) for k, (p, rs) in enumerate(by.items(), 1)]


def cut(rs, graded, action):
    """the mechanical rule of the author's answer: a graded OVERREACHES or UNDERSTATES sentence replaced in place by the ACTION sentence(s), an
    UNLICENSED one removed, MATCHES untouched; then a sentence that repeats one already earlier in the block dropped and returned."""
    import b647_record as R47
    act = action[len('RE-CUT: '):] if action.startswith('RE-CUT: ') else action
    out = []
    for r in rs:
        g = graded.get(r['n'])
        if g is None:
            out.append(r['sentence'])
        elif g == 'UNLICENSED':
            continue
        else:
            out += [x for x in R47._MSPLIT.split(act.strip()) if x.strip()]
    kept, dropped, seen = [], [], set()
    for x in out:
        if _ws(x) in seen:
            dropped.append(x)
            continue
        seen.add(_ws(x))
        kept.append(x)
    return kept, dropped


def grades(*a):
    g = jl(GRADES)['grades']
    L = ['b652 -- COMPONENT 3, (R262)(4) AND THE AUTHOR`S ANSWER BEFORE THE SEAL: SIDE-kernel`S SENTENCE ROWS GRADED BY HAND, BOUND TO THE PARENT '
         'BLOCK`S HAND CELLS; BANKED FOR THE AUTHOR`S STRIKE BEFORE ANY EDIT (%s)' % utc(), '',
         '### the rule (the author`s answer): a sentence row is graded OVERREACHES, UNDERSTATES or UNLICENSED where the parent block`s HAND LICENSED or',
         '### CITED cell names, quotes or paraphrases that sentence`s claim, the grade citing the cell`s words beside it; a sentence those cells do not',
         '### reach stays MATCHES; a block graded OVERREACHES with no sentence its cells reach is UNRESOLVED, not cut, printed for b653. The grade is the',
         '### parent`s verdict. Each graded row carries the parent`s ACTION verbatim. The sources: relay data/%s (b651, d7ab2fdb), data/%s' % (SENT, PARENTS),
         '### (b647); the grades: data/%s. Every quoted cell word read as a substring of the parent`s LICENSED cell before the bank was written.' % GRADES,
         '### Below each block: the block as the mechanical rule leaves it -- graded rows replaced in place by the ACTION, repeats dropped and printed.', '']
    n_rows = n_graded = n_unres = n_drop = n_cell = 0
    by_v = {}
    elided = []
    J = []
    for k, p, q, rs in blocks():
        n_rows += len(rs)
        mine = dict((int(n), w) for n, w in g.get(str(k), []))
        bad = [w for w in mine.values() if w not in q['licensed']]
        if bad:
            sys.exit('### BLOCK %d: A QUOTED WORD NOT IN THE LICENSED CELL -- NOTHING WRITTEN: %s' % (k, bad))
        v = q['verdict']
        L.append('== #%d %s (b647`s bank line :%s ; %s ; HAND %s ; %d sentences)' % (k, p.split(':', 1)[1], rs[0]['parent_line'], q['kind'], v, len(rs)))
        L.append('   LICENSED : ' + q['licensed'])
        L.append('   ACTION   : ' + q['action'])
        if '...' in q['action']:
            elided.append(k)
            L.append('   ### the ACTION cell carries an elision (...) as written in b647`s table; the rule places it verbatim -- flagged for the strike.')
        graded = {}
        for r in rs:
            if r['n'] in mine:
                graded[r['n']] = v
                n_graded += 1
                by_v[v] = by_v.get(v, 0) + 1
                L.append('  s%-3d %-11s %s' % (r['n'], v, r['sentence']))
                L.append('       %-11s cell: "%s"' % ('', mine[r['n']]))
            else:
                L.append('  s%-3d %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
        if '...' in q['action']:
            n_cell += 1
            L.append('   ### UNRESOLVED-CELL (the author`s word after the strike): an ACTION carrying "..." is an incomplete cell, not a sentence; nothing '
                     'with "..." enters a docstring; not cut; b653 completes the cell from the block`s own LICENSED words, banked for the strike.')
            J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], bank_line=rs[0]['parent_line'], verdict=v, graded=sorted(graded),
                          action=q['action'], unresolved_cell=True))
            L.append('')
            continue
        if not graded and v in ('OVERREACHES', 'UNDERSTATES'):
            n_unres += 1
            L.append('   ### UNRESOLVED: no sentence the cells reach; not cut; for b653.')
            J.append(dict(k=k, parent=p, unresolved=True))
            L.append('')
            continue
        kept, dropped = cut(rs, graded, q['action'])
        n_drop += len(dropped)
        L.append('   -> THE BLOCK AFTER THE CUT (%d sentences; repeats dropped %d):' % (len(kept), len(dropped)))
        for x in kept:
            L.append('        ' + x)
        for x in dropped:
            L.append('        ### DROPPED AS A REPEAT: ' + x)
        J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], bank_line=rs[0]['parent_line'], verdict=v,
                      graded=sorted(graded), action=q['action'], kept=kept, dropped=dropped))
        L.append('')
    n_cut = len([b for b in J if b.get('kept') is not None])
    files = sorted(set(b['file'] for b in J if b.get('kept') is not None))
    L.append('### ### **PARENT BLOCKS %d ; SENTENCE ROWS %d ; GRADED %d (%s) ; MATCHES %d ; UNRESOLVED BLOCKS %d ; UNRESOLVED-CELL %d (%s) ; '
             'BLOCKS TO CUT %d IN %d FILES ; REPEATS DROPPED BY THE RULE %d.**' % (
                 len(J), n_rows, n_graded, ', '.join('%s %d' % kv for kv in sorted(by_v.items())), n_rows - n_graded, n_unres, n_cell,
                 ', '.join('#%d' % e for e in elided), n_cut, len(files), n_drop))
    put_txt('b652_sentence_grades.txt', L)
    put_json('b652_sentence_cut_plan.json', dict(at=utc(), blocks=J))
    print(L[-1])


CUT_BRANCH, PC_BRANCH = 'docstrings-cut-SIDE-kernel', 'docstrings-SIDE-kernel'


def _table_at(ref):
    """b647's generator (_kdoc_rows) over SIDE-kernel's docstrings at a ref -- its _kmain read as the ref's commit, nothing else changed."""
    import b647_record as B7
    rev = subprocess.run(['git', '-C', 'D:/SIDE-kernel', 'rev-parse', '--short=7', ref], capture_output=True, text=True).stdout.strip()
    orig = B7._kmain
    B7._kmain = lambda k: rev
    try:
        return rev, B7._kdoc_rows('SIDE-kernel')
    finally:
        B7._kmain = orig


def table_after(*a):
    """(R262)(4): SIDE-kernel's docstrings re-run through the table after the cut -- the generated reading at main (before) and at the
    branch carrying both the cut and the plain comments (after); counts by verdict; every row not MATCHES printed; the cut blocks' rows apart."""
    import collections
    plan = jl('b652_sentence_cut_plan.json')['blocks']
    cut_files = set(b['file'] for b in plan if b.get('kept') is not None)
    r0, before = _table_at('main')
    r1, after = _table_at(PC_BRANCH)
    c0 = collections.Counter(r['verdict'] for r in before)
    c1 = collections.Counter(r['verdict'] for r in after)
    cf = collections.Counter(r['verdict'] for r in after if r['file'] in cut_files)
    L = ['b652 -- COMPONENT 3, (R262)(4): SIDE-kernel`S DOCSTRINGS RE-RUN THROUGH THE TABLE AFTER THE CUT (%s)' % utc(), '',
         '### the reader: b647_record._kdoc_rows (the generated rule, licensed_table.docstring_row), unedited, its kernel commit read as the ref`s;',
         '### before at main %s, after at %s %s (the cut, 33 commits, and the two plain comments rebased onto it).' % (r0, PC_BRANCH, r1),
         '### ### **THE GENERATED RULE IS THE ONLY READER HERE.** b651 found it reads 395 of 396 sentence rows MATCHES where the HAND reading',
         '### faulted 152 (relay data/b651_table_SIDE-kernel_sentences.txt; this act`s grades): a MATCHES count from it does not show what the HAND',
         '### reading would read after the cut. Its counts are printed as what they are.', '',
         '  before (main %s) : rows %d ; %s' % (r0, len(before), ', '.join('%s %d' % kv for kv in sorted(c0.items()))),
         '  after  (%s %s) : rows %d ; %s' % (PC_BRANCH, r1, len(after), ', '.join('%s %d' % kv for kv in sorted(c1.items()))),
         '  after, the 33 cut files alone : rows %d ; %s' % (sum(cf.values()), ', '.join('%s %d' % kv for kv in sorted(cf.items()))), '',
         '### ROWS NOT MATCHES AFTER THE CUT, printed and left (the author`s answer: not re-cut by hand this act):']
    n = 0
    for r in after:
        if r['verdict'] != 'MATCHES':
            n += 1
            L.append('  %s | %s | %s' % (r['source'], r['verdict'], '; '.join(r.get('findings') or [])[:400]))
            L.append('      STATED %s' % ' '.join(r['stated'].split())[:500])
    if not n:
        L.append('  none')
    L += ['', '### ### **BEFORE: ROWS %d, NOT MATCHES %d ; AFTER: ROWS %d, NOT MATCHES %d (%s) -- THE GENERATED RULE`S READING.**' % (
        len(before), len(before) - c0.get('MATCHES', 0), len(after), n, ', '.join('%s %d' % kv for kv in sorted(c1.items()) if kv[0] != 'MATCHES') or 'none')]
    put_txt('b652_table_after.txt', [l.replace('\r', '') for l in L])
    put_json('b652_table_after.json', dict(at=utc(), before=dict(rev=r0, counts=dict(c0)), after=dict(rev=r1, counts=dict(c1)),
                                           not_matches=[dict(source=r['source'], verdict=r['verdict'], findings=r.get('findings') or [])
                                                        for r in after if r['verdict'] != 'MATCHES']))
    print(NL.join(L[8:11] + L[-1:]))


# ================================================================================ COMPONENT 4: THE INSTRUMENT VERDICT'S OPENING ROWS, (R262)(5)
def _irows():
    import licensed_table as LT
    A = 'G-FINDINGS-ENTRY, G-TRAIL-RECORD, G-TRAIL-CARRIES-ROOT, G-TRAIL-CARRIES-SEAL, G-NEXT-ACT-NAMED'
    rows = [
        dict(id='b652-in-1', source='tools/b651_checks.py:848', arm='G-RESOLVER-COUNTS', said='PASS (its positive control)',
             stated='the positive control of G-RESOLVER-COUNTS: the after bank with its last row popped, read by the arm',
             licensed='the popped row was a MENTION, which the arm does not count, so the mutated bank still passed; the arm`s pass on its control '
                      'came from what it reads, not from the bank (relay data/b651_checks_mid1.txt; b651`s defect (l))',
             action='TO THE ARM: the control mutates a row the predicate counts -- a CONTRADICTED row`s verdict (repaired before b651`s seal, '
                    'relay f133eaf5)',
             cited=['relay@f133eaf5:tools/b651_checks.py:848', 'relay@be271f14:data/b651_defects.txt:14'], source_of='b651 defect (l)'),
        dict(id='b652-in-2', source='tools/b651_checks.py:382', arm=A, said='FAIL (five arms, pre-push and post-push)',
             stated='the five arms looked the entry`s title and the trail`s head up through b566_record`s poss (a backtick possessive written straight)',
             licensed='the record was landed through b641_record`s _poss (typographic); FINDINGS :8229 and OPEN_TRAILS :13874 stand as the record '
                      'tool wrote them, and read through the landing`s conversion all five pass (relay data/b652_conversion.txt; b651`s defect (n))',
             action='TO THE ARM: look a landed line up through conv, the one conversion held in the record tool (relay tools/b652_record.py; '
                    'OPEN_TRAILS :13896)',
             cited=['relay@be271f14:tools/b651_checks.py:382', 'relay@be271f14:tools/b651_checks.py:917', 'relay@be271f14:data/b651_defects.txt:16'],
             source_of='b651 defect (n)'),
        dict(id='b652-in-3', source='SIDE-global-section/Interfaces/LocalLimit.lean:226', arm='G-AXIOM-CLAIM', said='CONTRADICTED',
             stated='This is the general-p core of trace silence and of the escape hypothesis` arithmetic: the banked p = 2, 3 instances '
                    '(TraceSilence, no axioms) are its shadows; ...',
             licensed='"no axioms" is said of the TraceSilence instances, whose six declarations print no axioms; b649`s resolver bound it to '
                      'general_p_no_fixed_cell, whose print reads the standard three (b649`s ARM-MATCHING row 2)',
             action='TO THE ARM: re-bind a claim said of another named object to that object (relay 6bb2ed06; at b651 VERIFIED, BOUND-TO '
                    'TraceSilence)',
             cited=['SIDE-global-section@17ce9ff:Interfaces/LocalLimit.lean:226', 'relay@86d61573:data/b649_axiom_claim_rows.txt:16'],
             source_of='b649 ARM-MATCHING row 2'),
        dict(id='b652-in-4', source='SIDE-kernel/MetaKernel.lean:140', arm='G-AXIOM-CLAIM', said='CONTRADICTED',
             stated='The same conclusion, from the same two hypotheses with the finiteness assumption deleted and no imports at all, compiles and '
                    'depends on no axioms.',
             licensed='"no axioms" is said of a variant with no imports, an object not in the tree; b649`s resolver bound it to the headed '
                      'declaration (b649`s ARM-MATCHING row 5)',
             action='TO THE ARM: a claim said of an object that resolves nowhere reads UNBOUND, counted apart (relay 6bb2ed06)',
             cited=['SIDE-kernel@b0f2a3a:MetaKernel.lean:140', 'relay@86d61573:data/b649_axiom_claim_rows.txt:41'], source_of='b649 ARM-MATCHING row 5'),
        dict(id='b652-in-5', source='SIDE-kernel/legacy/SchwarzReflection_PR.lean:116', arm='licensed_table.docstring_row D4 (the generated rule)',
             said='OVERREACHES on s6, MATCHES on s7',
             stated='s6: Therefore conj(Λ₀(s)) = Λ₀(s), which holds iff Im(Λ₀(s)) = 0. s7: This establishes that zeros of Λ₀ on the critical line '
                    'are sign changes of a real-valued function (codimension 1), ...',
             licensed='s6 is a true remark (a complex number equals its conjugate exactly when its imaginary part is 0), not a claim that the '
                      'theorem is an equivalence; the block`s HAND licence faults s7 (sign changes, false at even-order zeros), which the rule '
                      'read MATCHES',
             action='TO THE ARM: D4 reads an equivalence claimed of the declaration`s statement, not any "iff" in the block; the faulted '
                    'sentence was cut by the HAND grades (relay data/b652_sentence_grades.txt, #116 s7)',
             cited=['relay@d7ab2fdb:data/b651_table_SIDE-kernel_sentences.txt:632', 'relay@0256e9e:data/b647_table_SIDE-kernel.txt:595'],
             source_of='the author`s answer before b652`s cut'),
    ]
    # ### the author's word during the builds: the generated rule's five OVERREACHES on SIDE-kernel's block table after the cut, and its identical
    # ### reading before and after the cut, entered as the same instrument's rows
    TA = 'data/b652_table_after.txt'
    ls = rd(os.path.join(D, 'b652_table_after.txt')).split(NL)
    st = {}
    for i, l in enumerate(ls):
        if ' | OVERREACHES | ' in l and i + 1 < len(ls):
            st[l.split(' | ')[0].strip()] = ls[i + 1].strip()[len('STATED '):]
    D4 = 'licensed_table.docstring_row D4 (the generated rule)'
    five = [
        ('Bridge/OstrowskiBridge.lean:37', 14, D4, 'D4 OVERREACHES',
         '"equivalent" is the equivalence of absolute values (f.IsEquiv), the relation the elaborated statement states; no logical biconditional is '
         'claimed, so D4 read a mathematical word as an "iff"'),
        ('Bridge/OstrowskiBridge.lean:46', 16, D4, 'D4 OVERREACHES',
         '"not equivalent" is the negated IsEquiv the statement carries (¬ real.IsEquiv (padic p)); D4 read the word as a claimed biconditional'),
        ('Kernel/Formation.lean:29', 18, 'licensed_table.docstring_row D2 (the generated rule)', 'D2 OVERREACHES',
         '"SIDE_exclusion proves ¬P from ExhaustiveCatalogue + NoneProduces" names the theorem`s hypotheses with its conclusion, which is what its '
         'statement says; D2 read the verb "proves" as a claim that the row derives unconditionally'),
        ('Kernel/Voice2.lean:48', 20, D4, 'D4 OVERREACHES',
         'the elaborated statement carries the biconditional, written ASCII `<->` (symmetries_agree_iff ... <-> sigma = 1 / 2); D4 looks for ↔ and '
         'reads "holds no ↔" of a statement that holds one'),
        ('Kernel/Voice6.lean:49', 22, D4, 'D4 OVERREACHES',
         'the elaborated statement carries the biconditional, written ASCII `<->` (offset_zero_iff ... <-> sigma = 1 / 2); D4 reads "holds no ↔" of '
         'a statement that holds one'),
    ]
    for j, (src, ln, arm, said, lic) in enumerate(five, 6):
        rows.append(dict(id='b652-in-%d' % j, source='SIDE-kernel/' + src, arm=arm, said=said, stated=st.get(src) or '(read at %s :%d)' % (TA, ln),
                         licensed=lic, action='TO THE ARM: read the statement`s own connective, ASCII and Unicode, and the sense of the word before '
                                              'grading an equivalence or a derivation',
                         cited=['SIDE-kernel@b0f2a3a:%s' % src, 'relay@4c886f8b:%s:%d' % (TA, ln)], source_of='the generated rule after the cut'))
    rows.append(dict(id='b652-in-11', source='data/b652_table_after.txt:10', arm='licensed_table.docstring_row rule (the generated reading over b647_record._kdoc_rows)',
                     said='MATCHES 428, OVERREACHES 5 before the cut and the same after it',
                     stated='the generated reading of SIDE-kernel`s 433 docstring rows at main b0f2a3a and at docstrings-SIDE-kernel 5033909',
                     licensed='113 blocks were cut between the two readings (152 sentences graded by hand against their parents` LICENSED cells); a '
                              'reader whose counts do not move when the text it grades is re-cut cannot register the edit it is asked to grade',
                     action='TO THE ARM: a reader asked to grade a cut reads the cut sentences themselves against the hand cells, or is replaced by '
                            'the hand reading for that purpose',
                     cited=['relay@4c886f8b:data/b652_table_after.txt:9', 'relay@4c886f8b:data/b652_table_after.txt:10'],
                     source_of='the author`s word during the builds'))
    for r in rows:
        r['verdict'] = LT.arm_verdict(r['arm'], r['said'], True)
        r['by'] = 'HAND'
    return rows


def instrument_rows(*a):
    import licensed_table as LT
    rows = _irows()
    counts, faults = LT.table(rows)
    real = [('SIDE-cosmo/SIDECosmo/SteaneExemplar.lean:6', 'row 1'), ('SIDE-kernel/Kernel/Integration.lean:215', 'row 3'),
            ('SIDE-kernel/MetaKernel.lean:3', 'row 4'), ('SIDE-lv-conservation/AxiomCheck.lean:8', 'row 6')]
    L = ['b652 -- COMPONENT 4, (R262)(5): THE INSTRUMENT VERDICT`S OPENING ROWS, IN THE TABLE`S CELLS WITH THE ARM (%s)' % utc(), '',
         '### the verdict added at relay eb3141f7 (tools/licensed_table.py: VERDICTS, ARM_RE, arm_verdict, label, check, table); its planted test',
         '### tools/test_licensed_table_instrument_b652.py 10 of 10. The rows: b651`s defects (l) and (n), b649`s ARM-MATCHING rows 2 and 5, and the',
         '### generated rule`s reading of SchwarzReflection_PR.lean :116 (the author`s answer before the cut). Each verdict through arm_verdict.', '']
    for r in rows:
        L += ['### %s (%s)' % (r['id'], r['source_of']),
              '  source   : ' + r['source'], '  stated   : ' + r['stated'], '  licensed : ' + r['licensed'],
              '  verdict  : %s (the arm said: %s)' % (LT.label(r), r['said']), '  arm      : ' + r['arm'], '  action   : ' + r['action'],
              '  by HAND, cited ' + ', '.join(r['cited']), '  check    : %s' % (LT.check(r) or 'taken'), '']
    L += ['### the real contradictions of b651`s resolver (relay data/b651_axiom_claim_rows.txt rows 1, 3, 4, 6), through arm_verdict with no mis-binding:']
    for s, n in real:
        L.append('  %s (%s) : %s' % (s, n, LT.arm_verdict('G-AXIOM-CLAIM', 'CONTRADICTED', False)))
    L += ['', '### rows 6-11 entered on the author`s word during the builds: the generated rule`s five OVERREACHES on SIDE-kernel`s block table',
          '### after the cut (relay data/b652_table_after.txt :14-:22), and its identical reading before and after the cut (:9-:10).',
          '', '### ### **OPENING ROWS %d ; THE TABLE`S COUNTS %s ; FAULTS %s ; REAL CONTRADICTIONS MOVED TO INSTRUMENT 0 OF 4.**' % (
        len(rows), dict(counts or {}), faults or 'NONE')]
    put_txt('b652_instrument_rows.txt', L)
    put_json('b652_instrument_rows.json', dict(at=utc(), rows=rows, counts=dict(counts or {}), faults=faults))
    print(L[-1])


def margin_bank(*a):
    """data/b652_build_margin.txt: the two readings, the corrected term, the cut branch per file, the branches' diffs whole."""
    j = jl('b652_build_margin.json')
    L = ['b652 -- COMPONENT 2, (R262)(3) AND THE AUTHOR`S WORD AFTER THE STRIKE: THE BUILD MARGIN, PER MODULE (%s)' % utc(), '',
         '### the hold %d MB, not lowered. The rule as (R262)(3) wrote it: a module builds under the hold when the free memory at its start less its' % HOLD,
         '### measured tree peak stays at or above the hold. Refuted by b651`s PerpendicularCrossing run (relay data/b651_docstrings_SIDE-kernel.txt',
         '### :18-:19): free 3365 MB at start, above the 3252 the rule needed, and the host fell 906 MB to 2459 against a tree peak of 683.',
         '### The term corrected by the author`s word: the margin needed is the host`s measured loss (free at start minus host low, as the watchdog',
         '### prints it) where a run recorded one, the largest of its attempts; the tree peak is not a substitute; none recorded: UNMEASURED.',
         '### Every loss is from a run the watchdog stopped at the hold: a lower bound of the whole run`s loss.', '',
         '### READING 1 (the slot`s start, the term as (R262)(3) wrote it, before the correction):']
    for r in [r for r in j['readings'] if r['reading'] == 1]:
        L.append('  %s %-38s needed %4d (tree peak) ; seen %4d (free %d) ; %s ; %s' % (r['at'], r['target'], r['needed'], r['seen'], r['free'],
                                                                                   'ALLOWS' if r['allows'] else 'DOES NOT ALLOW', r['source']))
    L += ['  read again under the corrected term, the same free memory: needed %s ; seen %d ; none allows.' % (
        ', '.join('%s %d' % (t.split('.')[-1], LOSS[t][0]) for t in LOSS), [r for r in j['readings'] if r['reading'] == 1][0]['seen']), '',
          '### READING 2 (later in the act, the corrected term):']
    for r in [r for r in j['readings'] if r['reading'] == 2]:
        L.append('  %s %-38s needed %4d (host loss) ; seen %4d (free %d) ; %s ; %s' % (r['at'], r['target'], r['needed'], r['seen'], r['free'],
                                                                                    'ALLOWS' if r['allows'] else 'DOES NOT ALLOW', r['source']))
    c = j['cut_branch']
    L += ['', '### THE CUT BRANCH (%s, the cut and the plain comments), per file, at reading 2 (seen %d MB above the hold):' % (c['branch'], c['seen'])]
    for x in c['files']:
        L.append('  %-44s %s' % (x['file'], ('needed %d ; seen %d ; %s ; %s' % (x['needed'], x['seen'], 'ALLOWS' if x['allows'] else 'DOES NOT ALLOW', x['source']))
                                 if x['needed'] else x['source']))
    nm = sum(1 for x in c['files'] if x['needed'])
    nu = sum(1 for x in c['files'] if not x['needed'] and x['lib'])
    nl = sum(1 for x in c['files'] if not x['lib'])
    L += ['', '### no build started: no module`s margin seen reached its margin needed at either reading, and no build is attempted on a file with no',
          '### measured need (the author`s word); no RUN-BENEATH-HOLD this act. The branches stay unmerged, their margins banked here.', '']
    KD = {'SIDE-lv-conservation': 'D:/SIDE-lv-conservation', 'SIDE-effects': 'D:/SIDE-effects', 'SIDE-kernel': 'D:/SIDE-kernel'}
    for k, br, base in (('SIDE-lv-conservation', 'b648-restate-SIDE-lv-conservation', 'main'), ('SIDE-effects', 'b648-restate-SIDE-effects', 'main'),
                        ('SIDE-kernel', PC_BRANCH, CUT_BRANCH)):
        d = subprocess.run(['git', '-C', KD[k], 'diff', '%s...%s' % (base, br)], capture_output=True).stdout.decode('utf-8').replace('\r', '')
        L += ['=== THE DIFF, %s %s over %s, whole:' % (k, br, base)] + d.rstrip(NL).split(NL) + ['']
    L += ['### the cut itself (33 commits) is printed block by block in relay data/b652_sentence_grades.txt and listed in data/b652_sidekernel_cut.txt.',
          '### ### **MODULES OF THE THREE BRANCHES 3, MEASURED 3, ALLOWING 0 AT EITHER READING ; CUT-BRANCH FILES %d: MEASURED %d, UNMEASURED IN A LEAN_LIB %d, '
          'IN NO LEAN_LIB %d ; BUILDS STARTED 0 ; MERGED 0.**' % (len(c['files']), nm, nu, nl)]
    put_txt('b652_build_margin.txt', L)
    print(L[-1])


def cut_bank(*a):
    """data/b652_sidekernel_cut.txt: the branch, the commits one per file with their blocks, the code-only check, the rebase, the table."""
    KD = 'D:/SIDE-kernel'
    gk = lambda *x: subprocess.run(['git', '-C', KD] + list(x), capture_output=True, text=True, encoding='utf-8').stdout   # noqa: E731
    plan = jl('b652_sentence_cut_plan.json')['blocks']
    log = [l.split(' ', 1) for l in gk('log', '--reverse', '--format=%h %s', 'main..' + CUT_BRANCH).split(NL) if l.strip()]
    pc = [l.split(' ', 1) for l in gk('log', '--reverse', '--format=%h %s', CUT_BRANCH + '..' + PC_BRANCH).split(NL) if l.strip()]
    ta = jl('b652_table_after.json')
    L = ['b652 -- COMPONENT 3, (R262)(4) AND THE AUTHOR`S WORD AFTER THE STRIKE: SIDE-kernel`S DOCSTRINGS CUT FROM THE SENTENCE ROWS (%s)' % utc(), '',
         '### the grades: relay data/b652_sentence_grades.txt (152 rows graded by hand, bound to the parent`s LICENSED cell); the rule: each graded',
         '### sentence replaced in place by its parent`s ACTION, repeats dropped, nothing composed; UNRESOLVED-CELL #56, #57, #69 not cut (an ACTION',
         '### with "..." is an incomplete cell), for b653. The branch %s from main %s; one commit per file by the Edit tool,' % (CUT_BRANCH, gk('rev-parse', '--short=7', 'main').strip()),
         '### each verified before its commit as main`s blob with the planned replacements applied (CR aside), byte for byte.', '']
    for h, s in log:
        f = s.split('Component 3: ', 1)[1].split(' -- ', 1)[0]
        ks = [b['k'] for b in plan if b.get('file') == f and b.get('kept') is not None]
        L.append('  %s  %-42s blocks %s' % (h, f, ', '.join('#%d' % k for k in ks)))
    L += ['', '### COMMITS %d ; FILES %d ; BLOCKS CUT %d ; UNRESOLVED-CELL 3 (#56 SimplicityRouteD, #57 SimplicityRouteE, #69 TriviumCode :9).' % (
        len(log), len(set(b['file'] for b in plan if b.get('kept') is not None)), len([b for b in plan if b.get('kept') is not None])),
          '### the code outside comments, every touched file, main against the branch: %s' % (a[0] if a else 'see the record'),
          '', '### the plain-comment branch rebased onto the cut (one branch carries both): %s at %s over %s' % (
              PC_BRANCH, gk('rev-parse', '--short=7', PC_BRANCH).strip(), CUT_BRANCH)]
    for h, s in pc:
        L.append('  %s  %s' % (h, s[:150]))
    L += ['', '### the table after the cut (relay data/b652_table_after.txt), the generated reader alone: before %s ; after %s ; rows not MATCHES after %d,' % (
        ta['before']['counts'], ta['after']['counts'], len(ta['not_matches'])),
          '### all in blocks the cut did not touch and all present before it; the generated reading did not move.',
          '', '### the merge: not made this act (the author`s word): its margins UNMEASURED per file (relay data/b652_build_margin.txt); no build attempted.',
          '### ### **COMMITS %d ; BLOCKS CUT %d ; BRANCH UNMERGED ; MAIN UNMOVED.**' % (len(log), len([b for b in plan if b.get('kept') is not None]))]
    put_txt('b652_sidekernel_cut.txt', L)
    print(NL.join(L[-12:]))


# ================================================================================ THE LATE ROUTES: ANSWERS, CAPTURE, KERNELS, DEFECTS, THE SEAL, THE
# ================================================================================ ROOT, THE TABLE, THE SCORES, THE RECORD (b651's, carried; look-ups by conv)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import b652_worklist as K          # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rdn(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def answers(*a):
    """data/b652_author_answers.txt: every prompt put by the seat in this act, from the ruling's delivery in this session, banked verbatim with
    its options and the answer; and every word of the author delivered between BEGIN and END lines after the ruling, verbatim."""
    calls, results, words, plain, start = [], {}, [], [], None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if start is None and K.ANCHOR in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
            start = i
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        if start is not None and att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif start is not None and o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
            for t in texts:
                if t and not t.lstrip().startswith(('<', 'BEGIN', 'RULING')) and len(t) < 400 and i > start:
                    plain.append((i, t.strip()))
        else:
            texts = []
        if texts:
            for t in texts:
                for mm in re.finditer(r'(?ms)^BEGIN\s*\n(.*?)\nEND\s*$', t or ''):
                    if K.ANCHOR not in mm.group(1):
                        words.append((i, mm.group(1)))
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and start is not None:
                calls.append((i, c['id'], c['input']))
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, K.SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    seen = set()
    W = []
    for i, w in words:
        if w in seen:
            continue
        seen.add(w)
        W += ['### THE AUTHOR`S WORD (transcript line %d), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    head = ['### b652 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, len(W and [x for x in W if x.startswith('### THE AUTHOR`S WORD')]), K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b652_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    print('  prompts banked: %d ; words banked: %d' % (n, len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])))


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


def commands(*a):
    """data/b652_commands.txt and .json: the act's command bank and G-EDIT-ROUTE's reading."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    L = ['b652 -- THE ACT`S COMMAND BANK AND THE ARM G-EDIT-ROUTE`S READING (tools/edit_route.py) (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d.**' % (len(rows), len(hits))]
    put_txt('b652_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b652_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits]))
    print(L[-1])


def kernels(*a):
    """data/b652_kernels_face.json: every kernel's main, tags, branches and tracked status, read before the seal for N5."""
    import b641_record as R41
    put_json('b652_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1].lower() for l in rdn('b652_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b652_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b652_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b652_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b652 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-38s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    put_txt('b652_seal_check_%s.txt' % (a[0] if a else 'record'), L)
    print(NL.join(L[2:]))


ROOT_EXCLUDE = re.compile(r'^b652_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b652_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    """(R251)(3): the act root, the last step of the act; every bank it names written LF. `dry`: computed, not written."""
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b652_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b652'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b652_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b652 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b652_root_arm.txt', L)
    put_json('b652_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b652 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b652_table_final.txt', L)
    put_json('b652_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = NK + SK
N5_RELAY_TOOLS = K.EDITED_SHARED + K.NEW_TESTS
N5_RELAY_DATA = ('act_roots.txt', 'b651_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')


def TRAIL_HEAD():
    return ('### b652 — lane three, act seventy-nine under (R262): b651 at its weight; the conversion rule; the build margin measured and the '
            'branches retried under it; SIDE-kernel’s docstrings cut from the sentence rows; the instrument verdict')


def _builds():
    """the build bank: per module its outcome (BUILT, STOPPED, UNBUILT) from data/b652_build_results.json, written by `builds`."""
    return jl('b652_build_results.json').get('rows') or []


def _n5():
    face = jl('b652_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    merged = [r for r in _builds() if r.get('merged')]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b652_|audit_b652_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS) or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched and no request made to the deposit service (draft %s, v5, unsubmitted); kernel mains '
            'written only by merges under Component 2`s rule: %s; every kernel as the face read it %s; sealed tools not agreeing %s; PLACE-papers '
            'beyond FINDINGS and OPEN_TRAILS: %s; relay files of a kind beyond the tool edits, their tests, the banks and the root list: %s; no '
            'identifier of the author in any outbound request (the act`s outbound calls git pushes and remote reads alone)' % (
                K.DRAFT, ', '.join('%s %s' % (r['kernel'], r['merged']) for r in merged) or 'NONE', kern_ok, differ or 'NONE', pp_beyond or 'NONE',
                kinds_beyond or 'NONE'))


def _tests():
    out = {}
    for t in K.NEW_TESTS + ('test_licensed_table_b645.py',):
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', t)], capture_output=True, text=True, encoding='utf-8', errors='replace',
                           env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        m = re.search(r'(\d+) of (\d+) cases as wanted', r.stdout or '')
        out[t] = (r.returncode, m.group(0) if m else '?')
    return out


def _conv_alone():
    """every b652 tool's code: no conversion of a backtick possessive but conv (no poss/_poss defined or called; the suite imports conv)."""
    bad = []
    for f in sorted(os.listdir(os.path.join(ROOT, 'tools'))):
        if f.startswith('b652_') and f.endswith('.py'):
            t = io.open(os.path.join(ROOT, 'tools', f), encoding='utf-8').read()
            if re.search(r'\bdef _?poss\(|\b_?poss\(|R41\._poss|Q\.poss|Q\.line_of|Q\.guard_absent|Q\.append_to', t):
                bad.append(f)
    suite = io.open(os.path.join(ROOT, 'tools', 'b652_checks.py'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, 'tools', 'b652_checks.py')) else ''
    return bad, 'from b652_record import conv' in suite or 'REC.conv' in suite


def scores(*a):
    TF, RA = jl('b652_table_final.json'), jl('b652_root_arm.json')
    _r, _n, sh = seal_hashes()
    tests = _tests()
    bad, suite_imports = _conv_alone()
    B = _builds()
    M = jl('b652_build_margin.json')
    two = all(len([r for r in M.get('readings') or [] if r['target'] == t]) >= 2 for t in LOSS)
    started_under = [r['target'] for r in B if r.get('started') and not r.get('allowed')]
    rbh = [r['target'] for r in B if r.get('outcome') == 'RUN-BENEATH-HOLD']
    stopped = [r['target'] for r in B if r.get('outcome') in ('STOPPED', 'RUN-BENEATH-HOLD')]
    TA = jl('b652_table_after.json')
    ac = collections.Counter(TA.get('after', {}).get('counts') or {})
    IR = jl('b652_instrument_rows.json')
    import licensed_table as LT
    real_kept = all(LT.arm_verdict('G-AXIOM-CLAIM', 'CONTRADICTED', False) == 'CONTRADICTED' for _ in range(4))
    S = {
        'N1': (('HELD' if not bad and suite_imports and tests['test_conversion_b652.py'][0] == 0 else 'REFUTED'),
               'one conversion: b652 tools defining or calling another %s; the suite importing conv %s; the planted backtick case %s; the five arms '
               'of defect (n) read at HEAD by the suite (their counts in the closing)' % (bad or 'NONE', suite_imports, tests['test_conversion_b652.py'][1])),
        'N2': (('HELD' if two and not started_under and not rbh else ('REFUTED IN ONE CLAUSE' if two and not started_under else 'REFUTED')),
               'every module of the three branches with two or more margins printed %s (readings %d); builds started beneath their needed margin %s; '
               'RUN-BENEATH-HOLD %s; stopped beneath the hold %s; outcomes %s' % (two, len(M.get('readings') or []), started_under or 'NONE', rbh or 'NONE',
                                                                                stopped or 'NONE', '; '.join('%s %s' % (r['target'].split('.')[-1], r['outcome']) for r in B) or 'none')),
        'N3': (('HELD' if not ac.get('OVERREACHES') and not ac.get('UNLICENSED') else 'REFUTED'),
               'after the cut SIDE-kernel`s block table read by the generated reader: %s -- OVERREACHES %d, UNLICENSED %d; the five rows were present '
               'before the cut and the reader`s counts did not move with it, entered as INSTRUMENT rows (data/b652_instrument_rows.txt rows 6-11): '
               'the table that scores N3 cannot see the cut' % (dict(ac), ac.get('OVERREACHES', 0), ac.get('UNLICENSED', 0))),
        'N4': (('HELD' if tests['test_licensed_table_instrument_b652.py'][0] == 0 and real_kept and not IR.get('faults') else 'REFUTED'),
               'the INSTRUMENT verdict`s planted cases %s; the four real contradictions through arm_verdict CONTRADICTED %s; the opening rows %d, the '
               'table`s faults %s' % (tests['test_licensed_table_instrument_b652.py'][1], real_kept, len(IR.get('rows') or []), IR.get('faults') or 'NONE')),
        'N5': _n5(),
        'S1': ('HELD' if all(rc == 0 for rc, _x in tests.values()) else 'REFUTED', 'the act`s planted tests and the table`s earlier test: %s' % '; '.join(
            '%s exit %d, %s' % (t, rc, x) for t, (rc, x) in tests.items())),
        'S2': ('HELD' if 'COMMITS 33 ; BLOCKS CUT 113' in rdn('b652_sidekernel_cut.txt') and 'code changed outside comments: NONE' in rdn('b652_sidekernel_cut.txt')
               else 'REFUTED', 'the cut one commit per file, 113 blocks, the code outside comments unchanged (data/b652_sidekernel_cut.txt)'),
        'S3': (('HELD' if not TF.get('gone') and not TF.get('added') and not TF.get('moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s' % (len(TF.get('moved') or []), len(TF.get('gone') or []),
                                                                                       len(TF.get('added') or []))),
        'S4': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S5': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    put_json('b652_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:400]))


NEXT_LINE = ('b653, the author`s word pending, per `(R262)`(8): the next kernel by descending count under the same rules, then the '
             'companions; with the author`s answers of this act carried -- the three elided ACTION cells (#56, #57, #69) completed from their LICENSED '
             'words for the strike before any cut, the hosted-runner workflow for the builds this host cannot hold, and test_chain_page_b638.py`s '
             'expectation read from the glossary file')


def _title():
    B = _builds()
    plan = jl('b652_sentence_cut_plan.json').get('blocks') or []
    nc = len([b for b in plan if b.get('kept') is not None])
    ta = jl('b652_table_after.json').get('after', {}).get('counts') or {}
    nout = sum(v for k_, v in ta.items() if k_ != 'MATCHES')
    ni = len(jl('b652_instrument_rows.json').get('rows') or [])
    nm = len([r for r in B if r.get('merged')])
    return ('## The build margin at %d modules, %d branches merged; SIDE-kernel’s docstrings at %d blocks cut, %d rows outside MATCHES after; the '
            'instrument verdict with %d opening rows; the conversion rule' % (len(LOSS), nm, nc, nout, ni))


def _finding_text():
    S, rl, J = jl('b652_scores.json'), jl('b652_record_lines.json'), jl('b652_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b652_author_answers.txt'), re.M))
    n_w = len(re.findall(r'^### THE AUTHOR`S WORD ', rdn('b652_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}]
    ml = (jl('b652_margin_line.json').get('lines') or [{}])[0]
    sc = lambda k: (S.get(k) or ['?'])[0]   # noqa: E731
    B = _builds()
    ta = jl('b652_table_after.json')
    e = ['', _title(), '',
         '*Filed at b652 on the author’s ruling `(R262)` and the author’s answers (%d prompts, %d words). Banks: relay `data/b652_conversion.txt`, '
         '`data/b652_build_margin.txt`, `data/b652_sentence_grades.txt`, `data/b652_sidekernel_cut.txt`, `data/b652_table_after.txt`, '
         '`data/b652_instrument_rows.txt`, `data/b652_act_root.txt`.*' % (n_ans, n_w), '',
         '**The conversion rule** (`(R262)`(2)): one function, `conv` in the record tool, converts a backtick possessive for the landing, the guard and '
         'every look-up; the suite imports it; the planted case finds a landed head the straight conversion misses; b651’s entry and trail found by '
         'it. The rule beneath b651’s trail (OPEN_TRAILS :%s). N1 %s.' % (ls[1].get('line'), sc('N1')), '',
         '**The build margin** (`(R262)`(3) and the author’s word): the rule as written -- free memory at a start less the tree’s peak -- refuted by '
         'b651’s own run, the host losing 906 MB against a peak of 683; the term corrected to the host’s measured loss (OPEN_TRAILS :%s): '
         'T3_StepNineBridge 1428 MB, Milestones 1255, PerpendicularCrossing 906, each a stopped run’s lower bound. Readings with the host`s own '
         'applications open allowed none; after the author closed them, %s. The cut branch`s 28 files with no recorded loss and the four in no '
         'lean_lib go to a hosted runner, b653’s to write. N2 %s.' % (ml.get('line'), '; '.join('%s %s' % (r['target'].split('.')[-1], r['outcome'])
                                                                                               for r in B) or 'no module built', sc('N2')), '',
         '**The docstrings** (`(R262)`(4) and the author’s answers): the sentence rows carried generated grades alone, so the 396 were graded by hand '
         'where the parent block’s licence reaches them -- 152 rows, 149 OVERREACHES and 3 UNDERSTATES -- and cut by the mechanical rule: 113 blocks in '
         '33 files on a branch, one commit a file, the code outside comments unchanged; three elided ACTION cells left UNRESOLVED-CELL; the plain '
         'comments rebased onto the cut. The block table read after the cut %s, as before it: N3 %s.' % (
             dict(ta.get('after', {}).get('counts') or {}), sc('N3')), '',
         '**The instrument verdict** (`(R262)`(5)): INSTRUMENT, with an ARM cell, in the licensed-statement table; a mis-binding reads '
         'INSTRUMENT(<arm>), a real contradiction keeps the arm`s verdict; %d opening rows -- b651’s (l) and (n), b649’s two ARM-MATCHING rows, and '
         'the generated docstring rule’s six readings, one of them its blindness to the cut. N4 %s.' % (
             len(jl('b652_instrument_rows.json').get('rows') or []), sc('N4')), '',
         '**The record lines** (`(R262)`(1)): b651 at its weight (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The root.** b652 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, sc(k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): each instrument the act leaned on was read against what it was asked to do -- a converter '
         'against the line it lands, a margin against the host’s whole loss, a table against the edit it grades -- and where one could not see its '
         'object the reading became a row rather than a verdict. It strengthens the programme’s offering of statements a reader can check: a '
         'docstring on the branch now says what its declaration states, and the table that grades it names its own blind spots.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a verdict compares a sentence with a licence and confers none.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the one conversion is the union of the two it replaces, written typographic; (2) the sentence grades bound to the parent`s '
              'LICENSED cell by quoted words; (3) a repeat is the later of two identical sentences in a block`s order; (4) the margin needed is the '
              'largest loss of a module`s recorded attempts; (5) the ruled reading taken when the author said the applications were closed')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b652_scores.json', 'b652_findings.json', 'b652_record_lines.json', 'b652_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b652_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}]
    ml = (jl('b652_margin_line.json').get('lines') or [{}])[0]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R262) ratified.** (1) b651 at its weight. (2) The conversion rule. (3) W-ORD-LV-BUILD-HOST acted as a measured margin. (4) SIDE-kernel’s '
             'docstrings cut from the sentence rows. (5) The instrument verdict. (6) The draft held at v5. (7) The navigator’s rows, its own. (8) The act '
             'after: b653.', '',
             '**Entered:** FINDINGS.md:%s (b651’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the conversion rule), :%s (the margin term corrected); this '
             'record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ml.get('line')), '',
             '**Act root:** b652 `%s` (previous `%s`, b651’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b652_author_answers.txt, with the author’s words), none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b652_defects.txt): %s.' % '; '.join(_defect_short()), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b652_scores.json')
    L = ['=' * 104, 'b652 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b652_defects.txt').rstrip(NL).split(NL)
    put_txt('b652_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b652_scores.json', 'b652_findings.json', 'b652_trail.json', 'b652_record_lines.json', 'b652_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}]
    L = ['b652 -- THE COMPONENTS, BANKED UNDER (R262).', '',
         '### COMPONENT 0 : step zero (data/b652_ferry.txt, data/b652_stepzero.txt, data/b652_tests_stepzero.txt, data/b652_readfirst.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b651`s weight FINDINGS :%s ; the conversion rule OPEN_TRAILS :%s ; data/b652_conversion.txt ; N1 %s' % (
             ls[0].get('line'), ls[1].get('line'), S['N1'][0]),
         '### COMPONENT 2 : the margin (data/b652_build_margin.txt, data/b652_build_results.json) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the docstrings (data/b652_sentence_grades.txt, data/b652_sidekernel_cut.txt, data/b652_table_after.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 4 : the instrument verdict (data/b652_instrument_rows.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 5 : the seal (data/b652_seal_hashes.json) ; S5 %s' % S['S5'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N5 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b652_components.txt', L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = line_of(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b652_findings.json', dict(title=t))
    j = jl('b652_findings.json')
    j['entry_line'] = ln
    put_json('b652_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b652_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


# ================================================================================ THE MIRROR, AT THE CLOSE (the author's word after the strike)
# ### after the last PLACE-papers push and before the closing: the unedited builder (-DateTag only) on the standing roster, the roots file's last
# ### line (b652's root) added to MANIFEST in the stage, verified from PLACE-papers by mirror_verify.py, banked; the closing prints its MANIFEST
# ### md5 and last commit. Its banks are written after the root and are not named by it. b644's routes, carried.
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-11-b652'
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % MIRROR_TAG)


def mbuild(*a):
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag',
                        MIRROR_TAG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b652_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b652':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b652`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b652_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b652_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-600:])


def mbank(*a):
    import zipfile
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b652_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b652 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b652_mirror.txt', L)
    put_json('b652_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:8]:
        print(l[:240])


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b652_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
