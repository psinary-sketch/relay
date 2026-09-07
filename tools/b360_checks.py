# -*- coding: utf-8 -*-
"""b360_checks.py -- THE GATE SUITE FOR THE FOLD, b349-b359.

### ### **THIS SUITE USES `gate_text.flat` AND DEFINES NO FLATTENER OF ITS OWN**, and every `G-NO*`-shaped
### arm reads STRIPPED CODE or a marked region rather than raw prose -- `b348`'s minted rule, which the
### record has now watched fire on five acts running.
### ### **THE ARMS (locked registration section (H)):** ### `G-QUOTE`, `G-NOGRADE`, `G-ADDITIVE`, `G-SPAN`,
### `G-RHYME`, `G-ARC`, `G-DESK`, `G-ROSTER`, `G-ROW`, `G-KEY` with `G-NOTFOLDED`, `G-APPENDONLY`,
### `G-NOEDIT`, `G-ORDER`, `G-HOOK` with `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the struck-clause
### and stem sweeps, `G-SHARED`, the hedge audit, the must-fail fixtures. ### Re-run after the push.
### ### **THE SIDES, DECLARED BY `b352`'s RULE AND NOT LEFT TO BITE:** ### `G-ADDITIVE` and `G-APPENDONLY`
### are read BEFORE THE PUSH; `G-NOEDIT`'s working-tree half BEFORE THE PUSH and its blob half
### SIDE-INVARIANT; `G-HOOK`, `G-MIRROR` and `G-ROSTER` AFTER THE PUSH; `G-ORDER` SIDE-INVARIANT.
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
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import gate_text         # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
ROSTER = os.path.join(ROOT, 'tools', 'mirror_roster.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b360_the_fold.txt')
REG = d('b360_registration_2026-09-07.txt')
FERRY = d('b360_ferry_2026-09-07.txt')
EMIT = d('b360_fold_emitted.md')
CORR, IDX = d('b360_corr_run.txt'), d('b360_index_run.txt')
SCAN, TERMSCAN, GATE = d('b360_ferry_scan.txt'), d('b360_reg_termscan.txt'), d('b360_reg_gate.txt')
CENSUS, FCEN = d('b360_census_stepzero.txt'), d('b360_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b360_regspec_run.txt'), d('audit_b360_reg_satisfiable.txt')
PINS, INDEXQ = d('b360_pins_stepzero.txt'), d('audit_b360_index_query.txt')
SEAL = '67f860655023b40c68f0db2f91c65fe4407b9e2f38f74e8233aa06da72e4a6af'
SECTION = 'THE UNIFORMITY ARC, b349\u2013b359 \u2014 THE FOLD'
ROWNUM = '209'

FJ = d('b360_fold.json')
EJ = d('b360_reads.json')
RJ = d('b360_roster.json')

NEW_THIS_ACT = {'tools/b360_extract.py', 'tools/b360_regspec.py', 'tools/b360_fold.py',
                'tools/b360_roster.py', 'tools/b360_correspondence.py', 'tools/b360_index_append.py',
                'tools/b360_checks.py'}

TOOLNUM = [
    ('the fold, F-QUOTE, F-NOGRADE, F-ADDITIVE and the emission', 'tools/b360_fold.py'),
    ('the span, counted off the record', 'tools/b360_regspec.py'),
    ('the 68 reads and the 39 differing anchors', 'tools/b360_extract.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the roster row, written and read back', 'tools/b360_roster.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('the flattener this suite uses', 'tools/gate_text.py'),
    ('row 209', 'tools/b360_correspondence.py'),
    ('the key', 'tools/b360_index_append.py'),
    ('54 clauses', 'tools/b360_regspec.py'),
    ('23051 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

# ### **THE RELIED-ON RUN FILES ARE NAMED BY THE JSONS THAT RECORD THEM, NEVER TYPED HERE** -- b358's cure,
# ### because `run_clock` numbers repeats and a suite that types a run file reads whichever ran FIRST.
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('F', 'b360_fold.json'), ('E', 'b360_reads.json'), ('R', 'b360_roster.json'))}

OWNED = [BANK, REG, FERRY, EMIT, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, TERMSCAN,
         d('b360_satisfiable.json'), d(_J['E']['run_file']), d(_J['F']['run_file']),
         d(_J['R']['run_file']),
         t('b360_extract.py'), t('b360_regspec.py'), t('b360_fold.py'), t('b360_roster.py'),
         t('b360_correspondence.py'), t('b360_index_append.py')]

CARRIERS = [
    (t('b360_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (d(_J['E']['run_file']), "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b360 \u2014 THE FOLD, b349 through b359. The executor'),
    ('the order -- the ruling on the roster', FERRY,
     'FACES_LEDGER.md is ADDED to the mirror roster. It is a'),
    ('the order -- addition one', FERRY, 'ADDITION ONE \u2014 THE THREE THAT RHYME, as the draft names its'),
    ('the order -- addition two, at the grade the acts support', FERRY,
     'ADDITION TWO \u2014 THE ARC AS ONE STATEMENT, at the grade the acts'),
    ('the order -- addition three', FERRY, 'ADDITION THREE \u2014 THE DESK, one list, written so a reader who'),
    ("the order -- the span's own finding, opening nothing", FERRY,
     'own finding: no move aimed at the quantifier remains on the'),
    ('b350 -- the floor is unexplained', d('b350_the_two_held_axes.txt'),
     '### The one origin that was moved does not account for it, and for the two held origins the record contains'),
    ('b352 -- under-resolved as a fit', d('b352_the_fourth_candidate.txt'),
     '### ### ### **THE FLOOR IS UNDER-RESOLVED AS A FIT.**'),
    ('b356 -- the instrument edge', d('b356_the_boundary.txt'),
     "### ### ### **SO b354's SIXTH RUNG WAS THE INSTRUMENT'S EDGE, AND THE FIVE-FRAME PICTURE STANDS WITH ITS"),
    ('b356 -- the floor question is where b352 left it', d('b356_the_boundary.txt'),
     '### reach, and now the reach has a number on it. ### **THE FLOOR QUESTION IS EXACTLY WHERE b352 LEFT IT**,'),
    ('b332 -- the quantifiers, unowned', d('b332_the_clause_stated.txt'),
     '### the zeros -- are UNOWNED, and they are the clause.'),
    ('b351 -- instances are not a class', d('b351_the_partition_question.txt'),
     '### ### HIGHER BUYS MORE INSTANCES, AND A CLASS IS NOT MADE OF INSTANCES.** ### The registration fixed'),
    ('b353 -- an exhaustion at every width is not an exhaustion across widths',
     d('b353_the_missing_statement.txt'),
     '### ### ### **SO: AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.** ### That sentence is'),
    ('b358 -- the archimedean half unconditional', d('b358_the_li_asymptotics.txt'),
     '### ### **THE ARCHIMEDEAN HALF IS UNCONDITIONAL, AND BOTH SOURCES SAY SO INDEPENDENTLY:**'),
    ('b359 -- the roster finding this act acts on', d('b359_the_currency_pass.txt'),
     '### ### ### **`FACES_LEDGER.md` IS NOT IN THE MIRROR ROSTER.**'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK,
     "### ### ### **THE ARC FOLDS, AND WHAT IT FOLDS INTO IS ABOUT WHAT THE CORPUS'S CHECKS CERTIFY.**"),
    ('### three that rhyme are three, and the fourth is not a fifth', BANK,
     "### **THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS**, and `b358`'s localization is a ### **FOURTH"),
    ('### no bridge typed, in either direction', BANK, '### ### ### **SO NO BRIDGE IS TYPED, IN EITHER DIRECTION.**'),
    ('### an edge located is not a floor explained', BANK,
     "### instrument's ### **EDGE** ### there, and ### **AN EDGE LOCATED IS NOT A FLOOR EXPLAINED**: `b350`'s"),
    ('### the span was counted and the draft was not adopted', BANK,
     "### ### ### **IT COUNTED `11`, AND THE DRAFT'S ASSERTION WAS NEVER ADOPTED.**"),
    ('### the closing sentence is filed as a sentence', BANK,
     '### ### ### **AND THE SENTENCE, FILED AS A SENTENCE AND OPENING NOTHING:**'),
    ('### and it is not a claim that no move exists', BANK,
     '### ### ### THIS SPAN PUT ON THE BOARD AND WHAT IT COST. ### IT IS NOT A CLAIM THAT NO SUCH MOVE EXISTS,'),
    ('### a roster row certifies nothing', BANK,
     '### ### NOTHING ABOUT WHETHER WHAT THE LEDGER SAYS IS TRUE.**'),
    ('### the roster incident, declared', BANK,
     '### ### **(E1) THE ROSTER WRITER LEFT THE ROSTER SYNTACTICALLY BROKEN, AND THE FILE WAS RESTORED FROM ITS'),
    ('### the wrong arm, named rather than quietly replaced', BANK,
     '### **AN ARM THAT CANNOT PASS ON A CORRECT EDIT IS NOT A STRICTER ARM; IT IS THE WRONG ARM.**'),
    ('### the bar refused once before it passed', BANK,
     "### run of the emitter found one quotation of `b355`'s that this seat had typed with the wrong line break"),
    ('### a fold proves nothing', BANK, '### ### **A FOLD PROVES NOTHING, DISCHARGES NOTHING AND MOVES NO GRADE.**'),
    ('### the temptation named', BANK, '### ### **AND THE TEMPTATION THIS ACT HAD TO RESIST IS SPECIFIC:**'),
    ('### the shadow', BANK, '### ### **EXPECTED: NOTHING. ### AND NOTHING IS WHAT A FOLD RETURNS.**'),
    ('### the lock, before any write', BANK,
     '### 2026-09-07T23:30:23Z. ### **LOCKED BEFORE ANY WRITE, WITH THE PRE-LOCK EXTRACT DECLARED ON ITS OWN'),
]

MUST_FAIL = [
    ('the bank never says the fold proves it', BANK, '### THE FOLD PROVES IT.'),
    ('the bank never says the three are equivalent', BANK, '### THE THREE ARE EQUIVALENT.'),
    ('the bank never says the quantifier is closed', BANK, '### THE QUANTIFIER IS CLOSED.'),
    ('the bank never says the roster change repairs the archive', BANK,
     '### THE ROSTER CHANGE REPAIRS THE ARCHIVE.'),
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
    """### THE SOURCE WITH COMMENTS AND STRING LITERALS REMOVED. ### **b348's MINTED RULE, APPLIED.**"""
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
    print('b360 -- GATE SUITE (THE FOLD, b349-b359)')
    print('=' * 100)
    extract = io.open(d(_J['E']['run_file']), encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE RELIED-ON EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    F = json.load(io.open(FJ, encoding='utf-8'))
    E = json.load(io.open(EJ, encoding='utf-8'))
    R = json.load(io.open(RJ, encoding='utf-8'))
    fnd = io.open(FINDINGS, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    emit = io.open(EMIT, encoding='utf-8').read()
    run = io.open(d(F['run_file']), encoding='utf-8').read()

    print(chr(10) + '  G-QUOTE (every quotation located at the act that ORIGINATED it, re-checked here independently):')
    q1 = F['quotes_failing'] == 0
    q2 = 'quotations failing : 0' in run
    SRCMAP = {a: p for a, p in
              [(x, os.path.join(D, y)) for x, y in
               [('b349', 'b349_the_room_relative.txt'), ('b350', 'b350_the_two_held_axes.txt'),
                ('b351', 'b351_the_partition_question.txt'), ('b352', 'b352_the_fourth_candidate.txt'),
                ('b353', 'b353_the_missing_statement.txt'), ('b354', 'b354_the_sixth_frame.txt'),
                ('b355', 'b355_what_the_arrays_are.txt'), ('b356', 'b356_the_boundary.txt'),
                ('b357', 'b357_what_the_ledgers_say.txt'), ('b358', 'b358_the_li_asymptotics.txt'),
                ('b359', 'b359_the_currency_pass.txt')]]}
    recheck, bad_re = 0, []

    def same(s):
        return gate_text.flat(s.replace('###', ' ').replace('**', ' '))

    for m in re.finditer(r'- \*\*(b3\d\d) \u2014 .*?\n  - Its own words: \u201c\u2026(.*?)\u2026\u201d', emit, re.S):
        act, q = m.group(1), m.group(2).strip()
        recheck += 1
        src = same(io.open(SRCMAP[act], encoding='utf-8', errors='replace').read())
        if same(q) not in src:
            bad_re.append((act, q[:60]))
    q3 = recheck == F['n_span'] and not bad_re
    gq = q1 and q2 and q3
    print('    the emitter reported 0 failing : %s ; its run file says so : %s' % (q1, q2))
    print('    re-checked here INDEPENDENTLY against the originating banks : %d of %d found, misses %s'
          % (recheck - len(bad_re), F['n_span'], bad_re or 'none'))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTE')

    print(chr(10) + '  G-NOGRADE (every grade anchored verbatim in its own act\'s bank; MECHANICAL):')
    sec = fnd[fnd.index('## ' + SECTION):] if ('## ' + SECTION) in fnd else ''
    n1 = F['grades_failing'] == 0
    n2 = 'grade anchors failing : 0' in run
    n3 = 'no grade moves here' in sec and 'no act is re-verdicted' in sec
    n4 = 'The no-grade-moved claim is mechanical' in sec
    gn = n1 and n2 and n3 and n4
    print('    0 grade anchors failing : %s ; the run file says so : %s' % (n1, n2))
    print('    the section states the filings law : %s ; and says the check is mechanical : %s' % (n3, n4))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOGRADE')

    print(chr(10) + '  G-ADDITIVE (the findings document a TRUE PREFIX of its blob; the section once) '
          '### READ BEFORE THE PUSH:')
    fb = blob_of(PP, 'FINDINGS.md')
    a1 = (fb is not None) and norm(fnd).startswith(norm(fb).rstrip(chr(10)))
    a2 = fnd.count('## ' + SECTION) == 1
    a3 = F['prefix_working'] and F['prefix_blob'] and F['once']
    a4 = F['lines_added'] > 0
    ga = a1 and a2 and a3 and a4
    print('    a true prefix of its committed blob : %s ; the section present once : %s' % (a1, a2))
    print('    the emitter measured the same at write time : %s ; lines added %d' % (a3, F['lines_added']))
    print('    ### **AFTER THE PUSH THIS ARM IS NEAR-VACUOUS, BECAUSE THE BLOB IS THEN THE FILE.**')
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ADDITIVE')

    print(chr(10) + '  G-SPAN (the span COUNTED off the record, and the result table covering exactly it):')
    s1 = F['span_start'] == 349 and F['n_span'] == 11
    s2 = sorted(F['span']) == sorted(F['acts'])
    s3 = 'ACTS IN THE SPAN : %d' % F['n_span'] in run
    s4 = 'the result table covers exactly the counted span : True' in run
    s5 = 'the span is counted, not typed' in sec.lower()
    gs = s1 and s2 and s3 and s4 and s5
    print('    the span begins at b%d and holds %d acts : %s' % (F['span_start'], F['n_span'], s1))
    print('    the table covers exactly the counted span : %s ; the run says so : %s / %s' % (s2, s3, s4))
    print('    and the section tells the reader the span was counted : %s' % s5)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SPAN')

    print(chr(10) + '  G-RHYME (four entries, each at its own act; the deposit\'s refusal quoted; NO BRIDGE):')
    r1 = F['rhyme_acts'] == ['b332', 'b351', 'b353', 'b358']
    r2 = 'no bridge is typed here, in either direction' in sec.lower()
    r3 = 'three obstructions that rhyme are three obstructions' in sec.lower()
    r4 = 'fourth entry of the same kind and not as a fifth obstruction' in sec.lower()
    r5 = 'compiling the cross-register equivalences' in sec
    r6 = ('not that they are the same problem' in sec.lower()
          and 'not that discharging one would touch another' in sec.lower())
    gr = r1 and r2 and r3 and r4 and r5 and r6
    print('    the four entries at b332, b351, b353, b358 : %s (%s)' % (r1, F['rhyme_acts']))
    print('    no bridge typed : %s ; three are three : %s ; the fourth is not a fifth : %s' % (r2, r3, r4))
    print('    the deposit\'s own refusal quoted : %s ; the three denials spelled out : %s' % (r5, r6))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RHYME')

    print(chr(10) + '  G-ARC (a scope beside every clause; the narrowing DECLARED; no clause above its acts):')
    c1 = sec.lower().count('*scope:*') >= F['arc_clauses']
    c2 = 'an edge located is not a floor explained' in sec.lower()
    c3 = 'runs one step ahead of what the acts support' in sec.lower()
    c4 = 'the floor question is exactly where b352 left it' in sec.lower()
    c5 = 'does not make a convention correct' in sec.lower()
    c6 = 'the clause has not moved' in sec.lower()
    gc = c1 and c2 and c3 and c4 and c5 and c6
    print('    a scope sentence for each of the %d clauses : %s (%d found)'
          % (F['arc_clauses'], c1, sec.lower().count('*scope:*')))
    print('    an edge is not a floor : %s ; the narrowing declared : %s ; b356 quoted on it : %s' % (c2, c3, c4))
    print('    no convention made correct : %s ; the clause has not moved : %s' % (c5, c6))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-ARC')

    print(chr(10) + '  G-DESK (every item with where it stands and what would move it; the finding opens nothing):')
    k1 = all(x in sec for x in ('`M-2`', 'The uniformity row', 'The instrument lane', 'The anchored gate arms',
                                'The wave', 'The routed items', 'The patent receipts'))
    k2 = 'filed as a sentence and opening nothing' in sec.lower()
    k3 = 'it is not a claim that no such move exists' in sec.lower()
    k4 = 'opens nothing, orders nothing and names no work' in sec.lower()
    k5 = 'no routed item is opened by this fold' in sec.lower()
    gk = k1 and k2 and k3 and k4 and k5
    print('    every standing desk item present : %s' % k1)
    print('    the finding is a sentence : %s ; not a claim that none exists : %s' % (k2, k3))
    print('    it opens nothing : %s ; no routed item opened : %s' % (k4, k5))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-DESK')

    print(chr(10) + '  G-ROSTER (the row appended at the END; no existing slot changed) ### READ AFTER THE PUSH '
          'for the archive half:')
    J = json.load(io.open(ROSTER, encoding='utf-8'))
    o1 = J['files'][-1] == 'FACES_LEDGER.md' and J['files'].count('FACES_LEDGER.md') == 1
    o2 = len(J['files']) == R['after'] == R['before'] + 1
    o3 = R['existing_rows_unmoved'] and R['blob_rows_unmoved']
    o4 = os.path.exists(os.path.join(PP, 'FACES_LEDGER.md'))
    o5 = 'does not retroactively place it in any prior mirror' in bank.lower()
    mir = d('b360_mirror.txt')
    o6 = None
    if os.path.exists(mir):
        mt = io.open(mir, encoding='utf-8', errors='replace').read()
        o6 = ('FACES_LEDGER.md' in mt) and ('VERDICT: CLEAN ON ALL THREE CLAUSES' in mt)
        print('    the rebuilt archive carries the new row and is clean on all three clauses : %s' % o6)
    else:
        print('    ### the mirror record is NOT YET WRITTEN (it is written after the push).')
    go = o1 and o2 and o3 and o4 and o5 and (o6 is True)
    print('    the row is LAST and appears once : %s ; count %d -> %d : %s' % (o1, R['before'], R['after'], o2))
    print('    every existing row unmoved, against the working file and the blob : %s' % o3)
    print('    the rostered source file exists : %s ; the bank states the non-retroactivity : %s' % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ### (the archive half is OWED until the push)'))
    if not go:
        fails.append('G-ROSTER (archive half owed until the push)' if o6 is None else 'G-ROSTER')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its '
          'blob) ### READ BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'A FOLD RESTATES ITS ACTS AT THEIR OWN GRADES' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTFOLDED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : uniformity-fold returns 1 row(s)' in irun
    k_2 = all(('%-40s NO KEY after  : True  PASS' % q) in irun for q in
              ('the fold proves it', 'the obstructions are equivalent', 'the quantifier is closed',
               'the roster change repairs the archive'))
    k_3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    k_4 = 'already reaches a banked key : True' in irun
    gkk = k_1 and k_2 and k_3 and k_4
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s' % (k_1, k_2))
    print('    the key run passed : %s ; the colliding alias checked and NOT claimed : %s' % (k_3, k_4))
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTFOLDED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order) '
          '### READ BEFORE THE PUSH:')
    ib = blob_of(ROOT, 'tools/banked_index.py')
    ap = True
    if ib is not None:
        old, new = norm(ib).split(chr(10)), norm(idx).split(chr(10))
        i = 0
        for ln in new:
            if i < len(old) and ln == old[i]:
                i += 1
        ap = (i == len(old))
    print('    %s' % ap)
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (no owner instrument; no keystone; the deposit and HANDOFF clean; only this "
          "act's paths touched) ### the working-tree half READ BEFORE THE PUSH; the blob half SIDE-INVARIANT:")
    owner = ['tools/e16/b264_eps_decay.py', 'tools/b340_li_control.py', 'tools/noise_floor.py',
             'tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py',
             'tools/anchor_from_file.py', 'tools/quote_norm.py', 'tools/ferry_scan.py',
             'tools/mirror_verify.py', 'tools/mirror_build.ps1']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'FINDINGS.md']
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    key = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md').strip()
    faces = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    tech = not git(TC, 'status', '--porcelain').strip() if os.path.isdir(TC) else True
    gne = not touched and not ppbad and hand and dep and key and faces and tech
    print('    owner instruments modified : %s ; papers paths beyond FINDINGS.md : %s' % (touched or 'none', ppbad or 'none'))
    print('    HANDOFF clean : %s ; the deposited monograph clean : %s ; the keystone clean : %s' % (hand, dep, key))
    print('    the faces ledger untouched (no row moves) : %s ; TECHNE-Core clean : %s' % (faces, tech))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the lock verifies through its owning tool; the ordering read from the clocks) '
          '### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o_1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o_1 = o_1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o_2 = stampm is not None
    # ### ### **WHAT THE RITUAL REQUIRES IS THAT THE LOCK PRECEDES EVERY RELIED-ON RUN, AND THAT IS WHAT
    # ### ### THIS ARM CHECKS.** ### It does NOT demand a fixed order among the components: the emitter was
    # ### re-run after the roster was written, so the relied-on emission post-dates the relied-on roster
    # ### write, and the section's content does not depend on the roster. ### **AN ARM THAT DEMANDED A
    # ### ### COMPONENT ORDER THE ACT DID NOT PROMISE WOULD BE MEASURING THE SEAT'S HABITS, NOT THE RITUAL**
    # ### -- its first version did exactly that and is declared on this act's face.
    o_3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, F, R))
    o_4 = (stampm is not None) and E['run_clock'] > stampm.group(1)
    pre = None
    p0 = d('b360_extract_notes.txt')
    if os.path.exists(p0):
        import run_clock
        pre = run_clock.read_stamp(p0)
        o_5 = pre is not None and stampm is not None and pre < stampm.group(1)
    else:
        o_5 = False
    sat = io.open(SATIS, encoding='utf-8').read()
    o_6 = 'JOINTLY SATISFIABLE' in sat
    go2 = o_1 and o_2 and o_3 and o_4 and o_5 and o_6
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s' % (o_1, stampm.group(1) if stampm else 'none', o_2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o_3)
    print('        lock    %s' % (stampm.group(1) if stampm else '?'))
    print('        extract %s   fold %s   roster %s   ### the component order AS MEASURED, not as demanded'
          % (E['run_clock'], F['run_clock'], R['run_clock']))
    print('    ### **AND THE PRE-LOCK EXTRACT IS BEFORE THE LOCK** : %s (%s)' % (o_5, pre))
    print('    the audit reads JOINTLY SATISFIABLE : %s' % o_6)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b360_hooks.txt'), d('b360_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht, mt = io.open(hookp, encoding='utf-8', errors='replace').read(), io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh = h_ok and m_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror: clean on all three clauses : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    cl = re.search(r'clauses\s*:\s*(\d+)', sat)
    sm = re.search(r'### bytes locked : (\d+)', reg)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [
        ('the span %d' % F['n_span'], ('`%d`' % F['n_span']) in bank),
        ('lines added %d' % F['lines_added'], ('`%d`' % F['lines_added']) in bank),
        ('quotations failing %d' % F['quotes_failing'], ('`%d`' % F['quotes_failing']) in bank),
        ('grade anchors failing %d' % F['grades_failing'], ('`%d`' % F['grades_failing']) in bank),
        ('reads %d' % E['reads'], ('`%d`' % E['reads']) in bank),
        ('anchors differing %d' % E['anchors_differing'], ('`%d`' % E['anchors_differing']) in bank),
        ('roster %d -> %d' % (R['before'], R['after']),
         all(('`%d`' % x) in bank for x in (R['before'], R['after']))),
        ('lines differing from the roster blob %s' % R['lines_differing_from_blob'],
         ('`%s`' % R['lines_differing_from_blob']) in bank),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on fold run file', F['run_file'] in bank),
        ('the relied-on roster run file', R['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files named, and each resolved by its own recorded clock):')
    import run_clock
    once = True
    for lbl, jf, key2 in (('extract', E, 'run_file'), ('fold', F, 'run_file'), ('roster', R, 'run_file')):
        p = d(jf[key2])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print('    %-8s %-26s clock on disk %s == the JSON\'s %s : %s' % (lbl, jf[key2], st, jf['run_clock'], ok))
    print('    ### **RESOLVED BY THE CLOCK AND NOT BY THE NAME** -- b358\'s cure, because run_clock numbers repeats.')
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
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
            for hh in (ch + sh)[:6]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE UNIFORMITY ARC, b349-b359 -- THE FOLD (b360).'
    nxt = '# ### THE LEDGER CURRENCY PASS (b359).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the section, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the section', sec),
                      ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-20s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
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
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  G-NOCOMPUTE (this act computes nothing, RE-MEASURED ON STRIPPED CODE, never on prose):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    for p in [t(x) for x in ('b360_extract.py', 'b360_regspec.py', 'b360_fold.py', 'b360_roster.py',
                             'b360_correspondence.py', 'b360_index_append.py', 'b360_checks.py')]:
        src = strip_prose(p)
        for b in banned:
            if b in src:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b360_fold.py', 'b360_roster.py', 'b360_extract.py'))]
    gnc = not hits and not imports
    print('    numerical calls in this act\'s STRIPPED sources : %d %s' % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the section and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b360_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the section', sec),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
