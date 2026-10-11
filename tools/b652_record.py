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
    ta = jl('b652_table_after.json')
    L += ['', '### NOT ENTERED (no order reaches them): the generated rule`s five D4 OVERREACHES on SIDE-kernel after the cut (relay',
          '### data/b652_table_after.txt), present before it too -- Voice2.lean :48 and Voice6.lean :49 read "holds no ↔" of statements that carry',
          '### `<->`; candidates of the same kind as row 5, for the author:']
    for x in ta.get('not_matches', []):
        L.append('  %s | %s' % (x['source'], (x['findings'] or [''])[0][:160]))
    L += ['', '### ### **OPENING ROWS %d ; THE TABLE`S COUNTS %s ; FAULTS %s ; REAL CONTRADICTIONS MOVED TO INSTRUMENT 0 OF 4.**' % (
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


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b652_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
