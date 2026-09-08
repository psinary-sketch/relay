# -*- coding: utf-8 -*-
"""b369_checks.py -- THE GATE SUITE FOR THE LIST REPAIRED, THE ROSTER MENDED, THE PASS PRICED.

### ### **EVERY ARM IS WRITTEN BY CONTENT AND NOT BY ADDRESS** (`(R2)`), and `G-BYCONTENT` re-measures
### that with `b366`'s own detector.
### ### **`G-NOEDIT` IS RESTATED, NOT SOFTENED.** ### This act was SENT to edit two owner instruments.
### The arm now names those two on its own face and ### **STILL FAILS ON ANY OTHER** -- a cap that says
### `0` where the order says `do it` is not a discipline, and an arm that stops checking is not an arm.
### ### **THE SIDES, BY `b352`:** ### `G-BOUNDED`, `G-NOEDIT` and `G-NOLEAN`'s working-tree halves and
### `G-ROW`'s and `G-TRAIL`'s ancestry readings are BEFORE THE PUSH; the hook, the polarity exercise and
### the mirror are AFTER; `G-ORDER` is SIDE-INVARIANT; ### **`G-REF` IS SIDE-DEPENDENT AND SAYS SO**
### (`b368`'s incident (vii)).
### ### **AND THE RUN FILES ARE RESOLVED BY THEIR OWN RECORDED CLOCKS, NEVER BY NAME** (`b358`'s cure).
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import hedge_audit        # noqa: E402
import ferry_scan         # noqa: E402
import banned_terms       # noqa: E402
import b306_stem_scope    # noqa: E402
import b317_checks as K7   # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN   # noqa: E402
import b366_sweep as SW    # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b369_the_list_repaired.txt')
REG = d('b369_registration_2026-09-08.txt')
FERRY = d('b369_ferry_2026-09-08.txt')
CORR, IDX = d('b369_corr_run.txt'), d('b369_index_run.txt')
SCAN, TERMSCAN, GATE = d('b369_ferry_scan.txt'), d('b369_reg_termscan.txt'), d('b369_reg_gate.txt')
CENSUS0, FCEN = d('b369_census_stepzero.txt'), d('b369_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b369_regspec_run.txt'), d('audit_b369_reg_satisfiable.txt')
PINS0 = d('b369_pins_stepzero.txt')
SEAL = 'b8ad7a66662e8cbe3960f50747781f63a760802c0e92174d85e1609a8f854dad'
ROWNUM = '218'
MARK = '<!-- b369 (R4): the original list preserved verbatim, and the list repaired -->'
B368_MARK = '<!-- b368 currency block: layer-1 export list vs source -->'
TRAIL_MARK = '<!-- b369 the list repaired in place, the original preserved -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b369_reads.json'), ('R', 'b369_repair.json'),
                   ('K', 'b369_hygiene.json'), ('P', 'b369_pass.json'),
                   ('Q', 'b369_desk.json'), ('F', 'b369_filing.json'))}

# ### **THE TWO OWNER INSTRUMENTS THIS ACT WAS SENT TO EDIT. ### NAMED HERE, AND NOWHERE WIDER.**
LICENSED = {'tools/b303_pins.py', 'tools/b304_hooks.py'}

NEW_THIS_ACT = {'tools/b369_regspec.py', 'tools/b369_extract.py', 'tools/b369_reg_gate.py',
                'tools/b369_repair.py', 'tools/b369_hygiene.py', 'tools/b369_pass.py',
                'tools/b369_desk.py', 'tools/b369_filing.py', 'tools/b369_bank.py',
                'tools/b369_correspondence.py', 'tools/b369_index_append.py', 'tools/b369_checks.py'}

TOOLNUM = [
    ('the located rows, the split and the three bars', 'tools/b369_repair.py'),
    ('the roster mend and the hook', 'tools/b369_hygiene.py'),
    ('the live enumeration, the price and the ranking', 'tools/b369_pass.py'),
    ('the 43 reads', 'tools/b369_extract.py'),
    ('the desk marks', 'tools/b369_desk.py'),
    ('the trail block and its bytes', 'tools/b369_filing.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b369_bank.py'),
    ('the three-arm registration gate', 'tools/b369_reg_gate.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 218', 'tools/b369_correspondence.py'),
    ('the key', 'tools/b369_index_append.py'),
    ('the clause spec', 'tools/b369_regspec.py'),
    ('20103 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('the pins, now across four', 'tools/b303_pins.py'),
    ('the hook, now across four', 'tools/b304_hooks.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b369 - THE LIST REPAIRED, THE ROSTER MENDED, THE PASS'),
    ('the order -- (R4)', FERRY, '(R4) THE LIST IS REPAIRED IN PLACE. The original list is quoted'),
    ('the order -- preserve by quotation, repair by edit', FERRY,
     'the list. Preserve by quotation, repair by edit. The kernel'),
    ('the order -- (R5)', FERRY, "(R5) THE RETIREMENT LEDGER'S OWN LACUNAE are filed, not"),
    ('the order -- component 1', FERRY, 'COMPONENT 1 - (R4) executed against the kernel at a live ref'),
    ('the order -- component 2', FERRY, 'COMPONENT 2 - THE TWO HYGIENE ITEMS: the exclusion kernel added'),
    ('the order -- component 3', FERRY, 'COMPONENT 3 - THE REFINEMENT PASS, PRICED AND NOT RUN. Enumerate'),
    ('the order -- audit nothing', FERRY, 'and the ranking; audit nothing.'),
    ('the order -- the fold is next', FERRY, 'NAVIGATOR EDITS, and it is the FOLD, b361 through b369, nine'),
    ("the order -- the navigator's expectations", FERRY,
     "The navigator's expectations: (F1) the repair is one edit and"),
    ('the kernel -- the retirement ledger heading', STRUCT,
     '-- RETIREMENT LEDGER (audit Phase S.2–S.4)'),
    ('the front document -- the list opener, still there once', AGENTS, 'Named theorems include:'),
    ('the front document -- the paragraph that bounds the edit', AGENTS,
     '`SIDEEffects/Milestones.lean` carries the analytic-existence statements'),
]

SELF_NEEDLES = [
    ('the bank states the answer first', BANK,
     'THE LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED IN THE SAME FILE'),
    ('### an edit is not an append', BANK, 'AN EDIT IS NOT AN APPEND, AND THIS ACT DOES NOT CLAIM A'),
    ('### the finding nobody registered', BANK,
     'AND THE FINDING THIS ACT DID NOT EXPECT: `b368`S SHARPER CLAIM IS WRONG'),
    ('### a predicate that knows one shape', BANK,
     'BOTH FAILURES ARE THE SAME SENTENCE: A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE'),
    ('### every retired name is reached by the ledger', BANK,
     'EVERY RETIRED NAME IS REACHED BY THE LEDGER'),
    ('### the abbreviation group is a judgement', BANK,
     'AND THAT GROUP IS KEPT APART BECAUSE READING AN ABBREVIATION AS NAMING ITS EXPANSIONS IS A'),
    ('### the cost (R4) imposed', BANK,
     'AND THE COST `(R4)` IMPOSED, REPORTED AT FULL PROMINENCE RATHER THAN LEFT TO BE'),
    ('### a past record is named and superseded', BANK,
     'A PAST RECORD IS NAMED AND SUPERSEDED, NEVER REWRITTEN'),
    ('### the count claim is out of scope and reported', BANK,
     'WHAT IS NOT IN SCOPE, AND IS SAID RATHER THAN SILENTLY LEFT'),
    ('### (R5) observed', BANK, '`(R5)` IS OBSERVED THROUGHOUT: NO REASON IS ASSERTED FOR ANY'),
    ('### the wording mended with the roster', BANK,
     'AND THE WORDING WAS MENDED WITH THE ROSTER, NOT AFTER IT'),
    ('### the two repairs are not equal in durability', BANK,
     'THE TWO REPAIRS ARE NOT'),
    ('### the pass priced and not run', BANK, 'THE PASS IS PRICED AND NOT RUN'),
    ('### the split a price usually hides', BANK, 'THE SPLIT, WHICH IS THE PART A PRICE USUALLY HIDES'),
    ('### exposure, not error', BANK, 'IT IS A RANKING OF EXPOSURE, NOT OF ERROR'),
    ('### what the ranking cannot see', BANK, 'AND WHAT THE RANKING CANNOT SEE, REPORTED BECAUSE IT IS'),
    ('### a criterion is only as wide as its surface', BANK,
     'A CRITERION IS ONLY AS'),
    ('### the hint scored against what was found', BANK,
     'THE HINT, SCORED AGAINST WHAT WAS FOUND AND NEVER THE OTHER WAY ROUND'),
    ('### an age is not a staleness', BANK, 'AN AGE IS NOT A STALENESS'),
    ('### the desk measurement nobody is using', BANK,
     'A MEASUREMENT WHOSE RESULT AND WHOSE CAVEAT BOTH NEVER'),
    ('### the incident: a tuple tested for truth', BANK,
     'THE REGISTRATION GATE DRIVER TESTED A TUPLE FOR TRUTH'),
    ('### the incident: CRLF against LF', BANK,
     'THE WORKING FRONT DOCUMENT IS CRLF AND ITS BLOB IS LF'),
    ('### the incident: the quotation nearly broke its own anchor', BANK,
     'THE PRESERVED QUOTATION NEARLY BROKE ITS OWN ANCHOR'),
    ('### the incident: the detector fired on a language version', BANK,
     'THE COUNT-SHAPE DETECTOR FIRED ON A LANGUAGE VERSION'),
    ('### the incident: the ranking sentence was false', BANK,
     'THE RANKING`S FIRST CLOSING SENTENCE WAS FALSE'),
    ('### (F1) confirmed', BANK, 'BOTH HALVES ARE MEASURED, NOT ASSERTED'),
    ('### (F2) partly scored, and registered in advance', BANK,
     'PARTLY SCORED, AND THE UNREACHABLE HALF WAS REGISTERED IN'),
    ('### the seat predicted the easy half', BANK,
     'A SEAT THAT PREDICTS THE LIMITS OF ITS OWN CAP HAS PREDICTED THE EASY'),
]

MUST_FAIL = [
    ('the bank never says a Lean file was written', BANK, '### A LEAN FILE WAS WRITTEN.'),
    ('the bank never says the original was not preserved', BANK,
     '### THE ORIGINAL LIST WAS NOT PRESERVED.'),
    ('the bank never says a repository was audited', BANK, '### A REPOSITORY WAS AUDITED.'),
    ('the bank never says a desk item is closed', BANK, '### A DESK ITEM IS CLOSED.'),
    ('the bank never supplies a retirement reason', BANK, '### A RETIREMENT REASON WAS SUPPLIED.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
    src2 = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src2)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and hasattr(n, 'lineno'):
            spans.append((n.lineno, n.end_lineno))
    keep = []
    for i, ln in enumerate(src2.split(chr(10)), 1):
        if any(a <= i <= b for a, b in spans):
            continue
        keep.append(ln.split('#')[0])
    return chr(10).join(keep)


def main():
    fails = []
    print('=' * 100)
    print('b369 -- GATE SUITE (THE LIST REPAIRED, THE ROSTER MENDED, THE PASS PRICED)')
    print('=' * 100)
    E, R, K, P, Q, F = _J['E'], _J['R'], _J['K'], _J['P'], _J['Q'], _J['F']
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### BUILT BY `gate_needle` FROM THE FILE THAT EMITTED THEM:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 200:
                inx = line.rstrip()[:200] in extract
                trunc = bool(inx)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '  ### -- ITS RECORDED PREFIX (the extract truncates at 200)'
                                    if trunc else ('' if inx else '  -- NOT IN THE EXTRACT FILE')))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES ### BUILT FROM THIS ACT’S OWN BANK:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never normalised):')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    agents = norm(io.open(AGENTS, encoding='utf-8', newline='').read())

    print(chr(10) + '  G-REF (the read is live, pinned, and its ref named) ### SIDE-DEPENDENT:')
    now = git(KERNEL, 'rev-parse', 'HEAD').strip()
    since = [x for x in git(KERNEL, 'log', '--format=%H %s', '%s..HEAD' % R['head']).splitlines()
             if x.strip()]
    anc = subprocess.run(['git', '-C', KERNEL, 'merge-base', '--is-ancestor', R['head'], 'HEAD'],
                         capture_output=True).returncode == 0
    r1 = R['head'] in bank and R['ref'] in bank
    r2 = R['pinned'] is True and R['ls_remote'] == R['head'] and R['dirty'] is False
    # ### **THE ARM TESTS AUTHORSHIP, NOT A PUNCTUATION FORM.** ### The first version asked for the
    # ### literal `(b369)` and this act's own commit subject reads `(b369, ruling (R4))` -- so the arm
    # ### failed on a comma. ### **A MARKER TYPED INTO AN ARM IS A MARKER NOBODY READ FROM THE RECORD.**
    r3 = anc and all(re.search(r'\bb369\b', x) for x in since)
    side = 'BEFORE THE PUSH' if now == R['head'] else 'AFTER THE PUSH'
    gr = r1 and r2 and r3
    print('    the ref `%s` = `%s` is named in the bank : %s' % (R['ref'], R['head'][:7], r1))
    print('    ### **LOCAL HEAD == ls-remote AT THE READ, TREE CLEAN** : %s' % r2)
    print('    ### **THE READ HEAD IS AN ANCESTOR AND EVERY COMMIT SINCE IS THIS ACT’S** : %s (%s, %d)'
          % (r3, side, len(since)))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-REF')

    print(chr(10) + '  G-REDERIVED (the count is this act’s own; no prior figure is an input):')
    src = strip_prose(t('b369_repair.py'))
    e1 = R['n_present'] + R['n_absent'] == R['exported']
    e2 = R['agrees_with_b368'] is True and R['b368_absent_constant'] == 18
    e3 = ('B368_ABSENT' in src) and not re.search(r'absent\s*=\s*.*B368_ABSENT', src)
    e4 = 'COMPARISON ONLY' in bank and 're-derived split' in bank and 'THIRD TIME' in bf
    ge = e1 and e2 and e3 and e4
    print('    the kinds partition the list (%d + %d == %d) : %s'
          % (R['n_present'], R['n_absent'], R['exported'], e1))
    print('    ### **AND THE THIRD DERIVATION AGREES** : %s' % e2)
    print('    ### **THE PRIOR FIGURE IS A COMPARISON, NEVER AN INPUT** (stripped code) : %s' % e3)
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-REDERIVED')

    print(chr(10) + '  G-PRESERVED (BAR 1: the original rows survive verbatim) ### BEFORE THE PUSH:')
    blk = agents.split(MARK)[-1] if MARK in agents else ''
    quoted = [x['text'] for x in R['rows_located']]
    p1 = agents.count(MARK) == 1
    p2 = all(q in blk for q in quoted)
    p3 = R['bar1_preserved'] is True and len(quoted) == R['rows_replaced']
    gp = p1 and p2 and p3
    print('    the mark appears once : %s ; all %d located rows appear verbatim in the block : %s'
          % (p1, len(quoted), p2))
    print('    ### **AND THE WRITER MEASURED THE SAME THING BEFORE IT EDITED** : %s' % p3)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRESERVED')

    print(chr(10) + '  G-EXPORTS (BAR 2: the repaired list exports no absent name) ### CONTENT PREDICATE:')
    lines = agents.split(chr(10))
    op = next(i for i, x in enumerate(lines) if x.strip() == 'Named theorems include:')
    cl = next(i for i, x in enumerate(lines)
              if x.startswith('`SIDEEffects/Milestones.lean` carries'))
    rows_now = [x for x in lines[op:cl] if re.match(r'^- \*\*[^*]+\*\*:', x)]
    still = sorted({m.group(1) for x in rows_now
                    for m in re.finditer(r'`([A-Za-z_][A-Za-z0-9_.]*)`', x)} & set(R['absent']))
    x1 = not still and not R['still_absent']
    x2 = len(rows_now) == R['rows_written']
    x3 = all(n in ' '.join(rows_now) for n in R['present'])
    gx = x1 and x2 and x3
    print('    absent names remaining in the repaired rows : %d %s' % (len(still), still or ''))
    print('    rows now : %d (writer said %d) : %s' % (len(rows_now), R['rows_written'], x2))
    print('    ### **AND BOTH SURVIVING DECLARATIONS ARE STILL EXPORTED** : %s' % x3)
    print('    ### **THIS IS A CONTENT PREDICATE OVER THE ROWS, NOT A COUNT OF EDITED LINES.**')
    print('    %s' % ('PASS' if gx else '### FAIL ###'))
    if not gx:
        fails.append('G-EXPORTS')

    print(chr(10) + '  G-BOUNDED (BAR 3: the edit went where it said) ### BEFORE THE PUSH:')
    b1 = R['bar3_above'] is True and R['bar3_below'] is True and R['side'] == 'BEFORE THE PUSH'
    blob = norm(blob_of(KERNEL, 'AGENTS.md') or '').split(chr(10))
    lo = R['rows_located'][0]['line'] - 1
    b2 = lines[:lo] == blob[:lo]
    gb = b1 and b2
    print('    the writer recorded both halves before the push : %s' % b1)
    print('    ### **AND RE-MEASURED HERE: EVERYTHING ABOVE THE ROWS IS ITS BLOB’S** : %s' % b2)
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BOUNDED')

    print(chr(10) + "  G-SUPERSEDED (b368's two sentences are NAMED, and NOT edited):")
    s1 = agents.count(B368_MARK) == 1
    s2 = 'Appended, not edited. Nothing above this line has been changed.' in agents
    s3 = '**The list above this block is left exactly as it was**' in agents
    s4 = 'supersedes two sentences in the block below it' in agents
    s5 = 'b368\'s block is left exactly as b368 wrote it' in agents
    gs = s1 and s2 and s3 and s4 and s5
    print("    b368's mark and both sentences still present, unedited : %s / %s / %s" % (s1, s2, s3))
    print('    ### **AND THE NEW BLOCK NAMES THEM AND MARKS THEM SUPERSEDED** : %s / %s' % (s4, s5))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SUPERSEDED')

    print(chr(10) + '  G-NOLEAN (### **NO `.lean` FILE TOUCHED, NO BUILD RUN**) ### BEFORE THE PUSH:')
    kstat = [x for x in git(KERNEL, 'status', '--porcelain').splitlines() if x.strip()]
    leanish = [x for x in kstat if x.strip().endswith('.lean')]
    n1 = not leanish
    n2 = R['lean_touched'] == 0 and K['lean_touched'] == 0 and R['build_run'] is False
    n3 = [x[3:].strip() for x in kstat] in ([], ['AGENTS.md'])
    gn = n1 and n2 and n3
    print('    `.lean` files dirty : %s ; writers recorded it : %s' % (leanish or 'none', n2))
    print('    ### **AND THE ONLY DIRTY PATH IS THE FRONT DOCUMENT** : %s %s'
          % (n3, [x[3:].strip() for x in kstat]))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOLEAN')

    print(chr(10) + "  G-LACUNAE ((R5): the ledger's groups are read from the evidence):")
    l1 = (R['n_named'] + R['n_by_abbr'] + R['n_layer_only'] + R['n_silent']) == R['n_absent']
    l2 = R['b368_silent_claim_refuted'] is True and R['n_silent'] == 0
    l3 = len(R['ledger_headings']) >= 7
    l4 = 'HEADED BY THAT DECLARATION`S OWN NAME' in bf or 'HEADED BY THAT DECLARATION' in bf
    l5 = all(n in R['abbreviations'] for n in R['ledger_by_abbreviation'])
    gl = l1 and l2 and l3 and l4 and l5
    print('    the four groups partition the absent set (%d+%d+%d+%d == %d) : %s'
          % (R['n_named'], R['n_by_abbr'], R['n_layer_only'], R['n_silent'], R['n_absent'], l1))
    print("    ### **b368's `no entry at all` CLAIM IS REFUTED** : %s ; ledger headings read : %d"
          % (l2, len(R['ledger_headings'])))
    print('    the bank gives the reason : %s ; every abbreviated name has its source string : %s'
          % (l4, l5))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LACUNAE')

    print(chr(10) + '  G-NOREASON ((R5): no retirement reason is supplied):')
    z1 = R['reasons_asserted'] == 0 and R['successors_named'] == 0
    z2 = 'note does not supply one' in agents
    z3 = 'where the record is silent, the silence is reported rather than filled' in agents
    z4 = 'NO REASON IS ASSERTED FOR ANY' in bf
    gz = z1 and z2 and z3 and z4
    print('    reasons asserted : %d ; successors named : %d' % (R['reasons_asserted'],
                                                                 R['successors_named']))
    print('    ### **AND THE DOCUMENT ITSELF SAYS SO** : %s / %s ; the bank too : %s' % (z2, z3, z4))
    print('    %s' % ('PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-NOREASON')

    print(chr(10) + '  G-ROSTER (the exclusion kernel is in both rosters):')
    o1 = all('SIDE-effects' in v for v in K['rosters'].values())
    o2 = len(K['rosters']['b303_pins.py']) == 4 and len(K['rosters']['b304_hooks.py']) == 4
    o3 = sum(K['wording_pairs'].values()) >= 5
    o4 = 'ALL 4 BYTE-IDENTICAL' in io.open(d('b369_hooks.txt'), encoding='utf-8',
                                           errors='replace').read()
    go = o1 and o2 and o3 and o4
    print('    both rosters name it : %s ; both are 4 long : %s' % (o1, o2))
    print('    ### **AND THE PROSE THAT COUNTED THEM WAS MENDED IN THE SAME PASS** : %s (%d pairs)'
          % (o3, sum(K['wording_pairs'].values())))
    print('    ### **THE TOOL NOW ANNOUNCES FOUR, NOT THREE** : %s' % o4)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ROSTER')

    print(chr(10) + '  G-HOOKINSTALLED / G-POLARITY (BAR 4) ### AFTER THE INSTALL:')
    hookp = os.path.join(KERNEL, '.git', 'hooks', 'pre-push')
    srcb = open(t(os.path.join('git-hooks', 'pre-push')), 'rb').read()
    h1 = os.path.exists(hookp) and open(hookp, 'rb').read() == srcb
    h2 = K['hook_identical'] is True and K['hook_existed_before'] is False
    h3 = K['repos_failing'] == 0 and K['polarities_exercised'] is True
    h4 = K['tracked_hooks_dir'] is False and 'UNTRACKED' in bf
    gh = h1 and h2 and h3 and h4
    print('    installed and byte-identical to the tracked source : %s (writer: %s)' % (h1, h2))
    print('    ### **EXERCISED IN BOTH POLARITIES, REPOS FAILING %d** : %s' % (K['repos_failing'], h3))
    print('    ### **AND THE ACT SAYS `.git/hooks/` IS UNTRACKED** : %s' % h4)
    print('    %s' % ('PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-HOOKINSTALLED/G-POLARITY')

    print(chr(10) + '  G-ENUM / G-NOAUDIT (live enumeration; nothing audited):')
    m1 = P['enumerated_live'] is True and P['repos_on_account'] >= P['programme'] > 0
    m2 = (P['repositories_audited'] == 0 and P['surfaces_read_for_correctness'] == 0
          and P['repositories_graded'] == 0)
    m3 = 'AUDIT NOTHING' in gate_text.flat(reg)
    m4 = 'A COUNT-SHAPED STRING IS NOT A CLAIM' in bf or 'count shape is not a claim' in bank
    src3 = strip_prose(t('b369_pass.py'))
    m5 = 'contents' not in src3 and 'raw.githubusercontent' not in src3
    gm = m1 and m2 and m3 and m4 and m5
    print('    enumerated live : %s (%d on the account, %d programme)'
          % (m1, P['repos_on_account'], P['programme']))
    print('    ### **AUDITED %d / READ FOR CORRECTNESS %d / GRADED %d** : %s'
          % (P['repositories_audited'], P['surfaces_read_for_correctness'],
             P['repositories_graded'], m2))
    print('    the cap is on the registration : %s ; a shape is not a claim : %s' % (m3, m4))
    print('    ### **AND THE TOOL FETCHES NO FILE CONTENT** (stripped code) : %s' % m5)
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-ENUM/G-NOAUDIT')

    print(chr(10) + '  G-HINT (both clauses scored against what was found):')
    i1 = P['h1'].split(' --')[0] in ('CONFIRMED', 'CORRECTED', 'NOT LOCATED')
    i2 = P['h2'] in ('CONFIRMED', 'CORRECTED', 'NOT LOCATED')
    i3 = len(P['construction_candidates']) == 1
    i4 = 'NOT BY SEARCHING FOR A NUMBER' in bf
    i5 = 'NOT LOCATED` IS AN ANSWER, NOT A FAILURE' in bank or 'IS AN ANSWER, NOT A FAILURE' in bf
    gi = i1 and i2 and i3 and i4 and i5
    print('    (H1) %s ; (H2) %s' % (P['h1'], P['h2']))
    print('    ### **THE CONSTRUCTION KERNEL WAS IDENTIFIED FROM DESCRIPTIONS, NOT FROM A NUMBER** : %s'
          % i4)
    print('    exactly one candidate : %s ; NOT LOCATED is an answer : %s' % (i3, i5))
    print('    %s' % ('PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-HINT')

    print(chr(10) + '  G-PRICE (three parts, reported separately, with the split named):')
    c1 = P['price_parts'] == 3
    c2 = all(x in bf for x in ('ONE REPOSITORY', 'THE WHOLE FEDERATION', 'THE SPLIT'))
    c3 = 'NOTHING IN THIS PASS MAKES THE READ CHEAPER' in bf
    c4 = P['ranking_criterion'] == ['age since last touch', 'counts rather than terminals', 'public']
    c5 = 'EXPOSURE, NOT OF ERROR' in bf
    gc = c1 and c2 and c3 and c4 and c5
    print('    three parts : %s ; all three named in the bank : %s' % (c1, c2))
    print('    ### **AND THE READ HALF IS NAMED AS THE PART THAT DOES NOT SCALE** : %s' % c3)
    print("    the criterion is the order's : %s ; exposure not error : %s" % (c4, c5))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-PRICE')

    print(chr(10) + '  G-DESKSWEEP / G-NOCLOSE (marks, not verdicts; nothing closed):')
    k1 = Q['items_closed'] == 0 and Q['module_written'] is False
    k2 = Q['rule_read_from_module'] is True
    k3 = (Q['confirmed'] + Q['unconfirmed']) == Q['items']
    k4 = all(m['hit'] is None or not m['hit']['file'].startswith('data/b369_') for m in Q['marks'])
    k5 = 'file that MENTIONS' in bf
    gk = k1 and k2 and k3 and k4 and k5
    print('    items closed : %d ; module written : %s' % (Q['items_closed'], Q['module_written']))
    print("    ### **THE RULE WAS READ FROM b368'S MODULE, NOT RESTATED** : %s" % k2)
    print("    ### **AND NO ITEM IS CONFIRMED FROM THIS ACT'S OWN FILES** : %s ; caveat printed : %s"
          % (k4, k5))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-DESKSWEEP/G-NOCLOSE')

    print(chr(10) + '  G-TRAIL (one append-only block; no block above edited) ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    t3 = F['prefix_of_file'] and F['prefix_of_blob'] and F['closed'] is False
    t4 = F['names_b367'] and F['names_b368']
    t5 = trails.count("THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED") == 1
    t6 = F['naked_kernel_names'] == 0
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    the mark appears once : %s ; blob is a true prefix : %s' % (t1, t2))
    print('    append-only both ways, and NOT CLOSED : %s ; names b367 and b368 : %s' % (t3, t4))
    print("    b157's sentence still there exactly once : %s ; names backticked : %s" % (t5, t6))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW (row %s) ### BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    ancr = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'REPAIRED IN PLACE' in rows[0]
            and 'IS NOT NOW CORRECT' in rows[0] and 'PRICED AND NOT RUN' in rows[0] and ancr)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, ancr))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW')

    print(chr(10) + '  G-KEY / G-NOTAUDITED:')
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    kk1 = 'READ BACK : list-repaired-in-place returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the federation is audited', 'the front document is correct',
               'the count claim is repaired', 'b368 is re-verdicted'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    kk4 = 'THE FRONT DOCUMENT IS NOT NOW CORRECT' in idx and 'AN EDIT IS NOT AN APPEND' in idx
    gkk = kk1 and kk2 and kk3 and kk4
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; run passed : %s'
          % (kk1, kk2, kk3))
    print('    ### **AND THE KEY SAYS THE DOCUMENT IS NOT NOW CORRECT** : %s' % kk4)
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTAUDITED')

    print(chr(10) + '  G-ORDER (the lock verifies; every relied-on run is AFTER it) ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1b = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1b = o1b and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o3b = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (R, K, P, Q, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4b = 'JOINTLY SATISFIABLE' in sat
    o5b = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6b = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    gob = o1b and stampm and o3b and o4b and o5b and o6b
    print('    the lock recomputes : %s ; clock %s' % (o1b, stampm.group(1) if stampm else 'none'))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3b)
    print('    audit JOINTLY SATISFIABLE : %s ; face says LOCKED BEFORE ANY WRITE : %s' % (o4b, o5b))
    print('    ### **AND THE THREE-ARM REGISTRATION GATE READ CLEAR** : %s' % o6b)
    print('    %s' % ('PASS' if gob else '### FAIL ###'))
    if not gob:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### AFTER THE PUSH:')
    hookp2, mirrorp = d('b369_hooks.txt'), d('b369_mirror.txt')
    gh2 = os.path.exists(hookp2) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp2, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 failing, all byte-identical : %s ; mirror clean : %s' % (h_ok, m_ok))
    else:
        print('    ### the mirror record is NOT YET WRITTEN (it is written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producer):')
    checks = [
        ('rows replaced %d' % R['rows_replaced'], ('`%d` export rows' % R['rows_replaced']) in bf),
        ('rows written %d' % R['rows_written'], len(rows_now) == R['rows_written']),
        ('exported %d' % R['exported'], ('of `%d` names' % R['exported']) in bf),
        ('present %d / absent %d' % (R['n_present'], R['n_absent']),
         ('`%d` declared and `%d`' % (R['n_present'], R['n_absent'])) in bf),
        ('named %d' % R['n_named'], ('NAMED OUTRIGHT `%d`' % R['n_named']) in bf),
        ('by abbreviation %d' % R['n_by_abbr'], ('ABBREVIATION `%d`' % R['n_by_abbr']) in bf),
        ('layer-only %d' % R['n_layer_only'], ('LAYER ENTRY `%d`' % R['n_layer_only']) in bf),
        ('silent %d' % R['n_silent'], ('AT ALL `%d`' % R['n_silent']) in bf),
        ('repos on the account %d' % P['repos_on_account'],
         ('`%d` repositories' % P['repos_on_account']) in bf),
        ('programme %d' % P['programme'], ('`%d` of them programme' % P['programme']) in bf),
        ('cheap surfaces %d' % P['cheap_surfaces'],
         ('`%d` SURFACES OF THE THREE CHEAP KINDS' % P['cheap_surfaces']) in bf),
        ('lean files %d' % P['lean_files'], str(P['lean_files']) in bank),
        ('repos failing %d' % K['repos_failing'], ('REPOS FAILING `%d`' % K['repos_failing']) in bf),
        ('hook bytes %d' % K['hook_bytes'], str(K['hook_bytes']) in bank),
        ('desk items %d' % Q['items'], ('ITEMS SWEPT `%d`' % Q['items']) in bf),
        ('desk closed %d' % Q['items_closed'], ('CLOSED `%d`' % Q['items_closed']) in bf),
        ('trail grew %d' % F['grew'], str(F['grew']) in bank),
        ('row %s' % ROWNUM, re.search(r'row to append : (\d+)',
                                      io.open(CORR, encoding='utf-8').read()).group(1) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on repair run', R['run_file'] in bank),
        ('the relied-on pass run', P['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (relied-on run files resolved by their own recorded clocks):')
    once = True
    for lbl, jf in (('extract', E), ('repair', R), ('hygiene', K), ('pass', P), ('desk', Q),
                    ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-9s %-26s clock on disk %s == the JSON's %s : %s"
              % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    for pat, jf in ((r'^b369_pass_notes\d*\.txt$', P), (r'^b369_repair_notes\d*\.txt$', R),
                    (r'^b369_filing_notes\d*\.txt$', F)):
        got = sorted(f for f in os.listdir(D) if re.match(pat, f))
        named = jf['run_file'] in bank
        once = once and named
        print('    ### **%d REPEAT(S); THE RELIED-ON ONE IS NAMED IN THE BANK : %s** %s'
              % (len(got), named, got))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed about the object, on STRIPPED code):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b369_') and x.endswith('.py')))
    hits = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits and not imports
    print("    numerical calls in this act's STRIPPED sources : %d %s" % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-BYCONTENT ((R2): no arm of this act is written by address):')
    selfhits = []
    for p in [t(x) for x in mymods]:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    DECLARED = {
        'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE -- to '
                          'count its cells; `b366` classified this shape NOT AN ADDRESS PREDICATE.',
        'the located row span': 'the row span is LOCATED by content (the list opener and the paragraph '
                                'after it) and only THEN used as an index; the index is a consequence '
                                'of the content read, not a typed address.',
    }

    def which(code):
        if '[-1:]' in code or '[-1]' in code:
            return 'last-row cells'
        if 'lo' in code or 'hi' in code or 'rows[0]' in code or 'rows[-1]' in code:
            return 'the located row span'
        return None
    undeclared = []
    for fn, i, code in selfhits:
        key = which(code)
        print('    %-26s line %-6d | %s' % (fn, i, code))
        if key is None:
            undeclared.append((fn, i))
            print('        ### ### **UNDECLARED HIT.**')
        else:
            print('        %s' % DECLARED[key])
    gbc = not undeclared
    print('    ### hits : %d ; declared with a reason : %d ; UNDECLARED : %d'
          % (len(selfhits), len(selfhits) - len(undeclared), len(undeclared)))
    print('    %s' % ('PASS' if gbc else '### FAIL ###'))
    if not gbc:
        fails.append('G-BYCONTENT')

    print(chr(10) + '  G-NOEDIT (### **RESTATED FOR THE TWO LICENSED INSTRUMENTS, NOT SOFTENED**) ###'
                    ' BEFORE THE PUSH:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/gate_content.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    unlicensed = [p for p in touched if p not in LICENSED]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').splitlines()
              if x.strip() and 'b369' not in x and x.strip() != 'tools/banked_index.py'
              and x.strip() not in LICENSED]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines()
              if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'OPEN_TRAILS.md']
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    gne = not unlicensed and not others and not ppbad and faces_clean and fnd
    print('    owner instruments modified : %s' % (touched or 'none'))
    print('    ### **LICENSED BY THE REGISTRATION : %s**' % sorted(LICENSED))
    print('    ### ### **MODIFIED WITHOUT A LICENCE : %s**' % (unlicensed or 'none'))
    print('    tracked relay files of other acts modified : %s' % (others or 'none'))
    print('    papers paths beyond OPEN_TRAILS.md : %s' % (ppbad or 'none'))
    print('    ### **FACES_LEDGER.md UNTOUCHED, BECAUSE NO ROW MOVED** : %s ; FINDINGS clean : %s'
          % (faces_clean, fnd))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b369_satisfiable.json'),
             t('b369_regspec.py'), t('b369_extract.py'), t('b369_reg_gate.py'),
             t('b369_bank.py'), t('b369_correspondence.py'), t('b369_index_append.py')]
    CARRIERS = [
        (t('b369_checks.py'), 'its own fixtures'),
        (FERRY, "IT IS THE ORDER -- not this act's writing"),
        (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
        (d(E['run_file']), "the extract carries the kernel's own words"),
        (d(R['run_file']), "the repair carries the ledger's and the list's own lines"),
        (d(K['run_file']), "the hygiene run carries the hook's own refusal text"),
        (d(P['run_file']), "the pass carries the account's own descriptions"),
        (d(Q['run_file']), "the desk run carries the fold's own sentence"),
        (d(F['run_file']), "the filing carries the kernel's own quoted heading"),
        (d('b369_hooks.txt'), "the hook tool's own log"),
        (t('b369_repair.py'), "ITS SEARCH STRINGS ARE THE FRONT DOCUMENT'S AND THE LEDGER'S OWN"),
        (t('b369_hygiene.py'), "IT QUOTES THE TWO INSTRUMENTS' OWN LINES, EXACTLY"),
        (t('b369_pass.py'), "ITS NOUN LIST IS THE PROGRAMME'S OWN ARTIFACT VOCABULARY"),
        (t('b369_desk.py'), "ITS DESK ROWS ARE THE FOLD'S OWN ITEM NAMES"),
        (t('b369_filing.py'), "it quotes the kernel's own ledger heading"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned, live_bad = 0, 0, 0, []
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
        if sh:
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', p],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            live = re.search(r'live uses\s*:\s*(\d+)', rr.stdout or '')
            print('        ### **HANDED TO THE SHARED SCANNER -- live uses : %s ; CLEAN : %s**'
                  % (live.group(1) if live else '?', clean))
            if not clean:
                live_bad.append(os.path.basename(p))
    print('    files scanned %d   struck %d   stem %d   ### **LIVE AFTER THE SHARED SCANNER : %d** %s'
          % (scanned, total, stem_total, len(live_bad),
             'PASS' if not (total or live_bad) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in
                [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                 ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                 ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [],
                                     stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or live_bad or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE LIST REPAIRED IN PLACE, THE ROSTER MENDED, THE PASS PRICED (b369).'
    nxt = '# ### THE FRONT DOCUMENT RECONCILED, APPEND-ONLY (b368).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the preserved block, the index row):'
          % ROWNUM)
    for lbl, b2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', tblk),
                    ('the preserved block', blk), ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(b2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(b2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(b2)))
        if ch or not b2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            tmp = os.path.join(tempfile.mkdtemp(prefix='b369_stem_'), 'blk.txt')
            io.open(tmp, 'w', encoding='utf-8', newline=chr(10)).write(b2)
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', tmp],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **%d STEM HIT(S) HANDED TO THE SHARED SCANNER: CLEAN : %s**'
                  % (len(sh), clean))
            if not clean:
                fails.append('G-STEM-APPENDED live ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b369_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', tblk),
                      ('the preserved block', blk), ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles refused : %d ; owner needles not in the extract file : %d'
          % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
