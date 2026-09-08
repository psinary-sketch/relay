# -*- coding: utf-8 -*-
"""b364_checks.py -- THE GATE SUITE FOR THE COPY THAT DID NOT REPRODUCE.

### ### **THIS SUITE USES `gate_needle` (`b363`) AND `gate_text.flat` AND DEFINES NO FLATTENER OF ITS
### ### OWN**, and every `G-NO*`-shaped arm reads STRIPPED CODE or a marked region rather than raw prose --
### `b348`'s rule.
### ### **AND IT IS WRITTEN UNDER THE FINDING ITS OWN ACT FILED.** ### `b364` found a gate arm that had
### aged out because its pass condition was a literal in a frozen file compared against a quantity
### recomputed at every run. ### **SO NO ARM HERE COMPARES A LINE NUMBER OF ANY FILE OUTSIDE THIS ACT.**
### Where this suite must know a number, it reads it from this act's own JSON, which is this act's own
### output and moves only if this act is re-run.
### ### **THE ARMS (locked registration section (E)):** ### `G-PREDICATE`, `G-COPY`, `G-BANKED`,
### `G-BRANCH`, `G-NOEDIT`, `G-UNCHANGED`, `G-RESTATED`, `G-ROW`, `G-KEY` with `G-NOREPAIR`, `G-ORDER`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, `G-NOCOMPUTE`, the struck-clause and stem sweeps, `G-SHARED`, the
### hedge audit, the must-fail fixtures. ### Re-run after the push.
### ### **THE SIDES, DECLARED BY `b352`'s RULE:** ### `G-NOEDIT`'s and `G-UNCHANGED`'s working-tree halves
### and `G-ROW`'s and `G-RESTATED`'s ancestry readings are read BEFORE THE PUSH; `G-HOOK` and `G-MIRROR`
### AFTER THE PUSH; `G-ORDER` SIDE-INVARIANT.
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
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import gate_text         # noqa: E402
import run_clock         # noqa: E402
import gate_needle as GN  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b364_the_copy_that_did_not_reproduce.txt')
REG = d('b364_registration_2026-09-07.txt')
FERRY = d('b364_ferry_2026-09-07.txt')
SUITE = t('b357_checks.py')
B357 = d('b357_what_the_ledgers_say.txt')
B363 = d('b363_the_anchored_gate_arms.txt')
CEN363 = d('b363_census_run3.txt')
B314 = d('b314_the_fold_and_the_cold_clone.txt')
CORR, IDX = d('b364_corr_run.txt'), d('b364_index_run.txt')
SCAN, TERMSCAN, GATE = d('b364_ferry_scan.txt'), d('b364_reg_termscan.txt'), d('b364_reg_gate.txt')
CENSUS0, FCEN = d('b364_census_stepzero.txt'), d('b364_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b364_regspec_run.txt'), d('audit_b364_reg_satisfiable.txt')
PINS = d('b364_pins_stepzero.txt')
SEAL = '5e78a12c4733de389e4e2f698ea3e51175310bf78d3a502e9e8f39b954b880ee'
ROWNUM = '213'
TRAIL_MARK = '<!-- b364 dated arm finding -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b364_reads.json'), ('J', 'b364_diagnose.json'), ('F', 'b364_filing.json'))}

NEW_THIS_ACT = {'tools/b364_regspec.py', 'tools/b364_extract.py', 'tools/b364_diagnose.py',
                'tools/b364_filing.py', 'tools/b364_correspondence.py', 'tools/b364_index_append.py',
                'tools/b364_checks.py'}

TOOLNUM = [
    ('the branch, both runs and the unchanged bar', 'tools/b364_diagnose.py'),
    ('the 21 reads and the 5 predicate lines', 'tools/b364_extract.py'),
    ('the filing, and its 4778 bytes', 'tools/b364_filing.py'),
    ('the arm under diagnosis, READ AND NEVER WRITTEN', 'tools/b357_checks.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper, built one act ago and used here', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 213', 'tools/b364_correspondence.py'),
    ('the key', 'tools/b364_index_append.py'),
    ('49 clauses', 'tools/b364_regspec.py'),
    ('12769 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

# ### **THE FILES THE DIAGNOSIS READ AND MUST NOT HAVE WRITTEN.** ### `G-UNCHANGED` re-proves it here.
UNTOUCHABLE = ['tools/b357_checks.py', 'tools/banked_index.py',
               'data/b357_what_the_ledgers_say.txt', 'data/b357_read.json',
               'data/b357_read_run2.txt', 'data/b363_census_run3.txt']

OWNED = [BANK, REG, FERRY, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
         d('b364_satisfiable.json'), d(_J['E']['run_file']), d(_J['J']['run_file']),
         d(_J['F']['run_file']),
         t('b364_regspec.py'), t('b364_extract.py'), t('b364_diagnose.py'), t('b364_filing.py'),
         t('b364_correspondence.py'), t('b364_index_append.py')]

CARRIERS = [
    (t('b364_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (d(_J['E']['run_file']), "the extract file carries other acts' own words"),
    (d(_J['J']['run_file']), "the diagnosis file carries b357's suite's own output"),
]

OWNER_NEEDLES = [
    ('the order -- the leg', FERRY, 'LEG 1 (b364) - THE COPY THAT DID NOT REPRODUCE. Diagnose, do'),
    ('the order -- do not repair-to-pass', FERRY,
     'not repair-to-pass. Report what the failing locating arm'),
    ('the order -- what must be reported', FERRY,
     'checked, what it found in the copy, and what it finds in the'),
    ('the order -- the environmental branch', FERRY,
     'here before the diagnosis: (ENVIRONMENTAL - the copy fails for'),
    ('the order -- and what it requires be SHOWN', FERRY,
     'suite at its own location still passes, shown by running it'),
    ('the order -- the real branch', FERRY,
     "/ (REAL - the arm fails at the banked suite's own location too;"),
    ('the order -- the undecided branch', FERRY, '/ (UNDECIDED - the resisting step named). In every'),
    ('the order -- nothing edited, no verdict moved', FERRY,
     'branch the banked suite is not edited and no verdict is moved'),
    ("the order -- the navigator's expectation", FERRY, "navigator's expectations: (L1) ENVIRONMENTAL"),
    ("the arm's own label, at its own suite", SUITE,
     'G-LOCATED (every classified row located by the anchor tool at its own ledger, NOW)'),
    ("the arm's own pass condition, at its own suite", SUITE,
     "ok_dec = ('%d' % was) in bank and ('%d' % now) in bank and 'STRADDLE THIS ACT' in bf"),
    ('the four ledgers the arm reads', SUITE, "LEDGERS = {'FINDINGS.md': FINDINGS,"),
    ("b363's control row for b357", CEN363, 'b357  banked GATES FAILING 0'),
    ('b357 -- its own straddle declaration', B357, 'AND TWO LINE NUMBERS STRADDLE THIS ACT, DECLARED BY'),
    ('b357 -- the move its own append caused', B357, "`b357`'S OWN INDEX KEY MOVED THAT ROW TO `1054`.**"),
    ('b314 -- the absolute-paths work-order, by its own ID', B314,
     'W-ORD-ABSOLUTE-PATHS`.** ### Instrument files carry hard-coded'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK, 'THE BRANCH IS `REAL`, AND THE COPY WAS INNOCENT'),
    ('### run at its own location, unedited', BANK,
     'reports the same failure, the same arm and the same four rows' if False else
     'AT ITS OWN LOCATION, UNEDITED**, reports'),
    ("### the navigator's expectation refuted by a run", BANK,
     'SO THE NAVIGATOR'),
    ('### and this seat refuted in the same word', BANK,
     "AND THIS SEAT'S EXPECTATION IS REFUTED TOO, IN THE SAME WORD"),
    ('### the two halves, and only one failed', BANK,
     'WHAT THE ARM WAS CERTIFYING -- TWO THINGS, AND ONLY ONE OF THEM HAS FAILED'),
    ('### the half that holds, in the run own words', BANK, 'rows re-located at their ledgers : 12 of 12'),
    ('### the half that cannot hold', BANK, 'THIS HALF CANNOT HOLD AND CANNOT BE MADE TO'),
    ('### the species named', BANK, 'AND THE SPECIES IS NAMED: A DATED ARM'),
    ('### it does not become wrong, it becomes old', BANK, 'IT DOES NOT BECOME WRONG. ### IT BECOMES OLD'),
    ('### nothing repaired, nothing edited, no verdict moved', BANK,
     'NOTHING IS REPAIRED, NOTHING IS EDITED, AND NO VERDICT IS MOVED BY THIS SEAT.**'),
    ('### the predicate quoted, bar 1', BANK,
     "A PARAPHRASED PREDICATE IS THIS SEAT'S READING OF AN ARM AND"),
    ('### the whole defect in one line', BANK, 'THAT IS THE WHOLE OF THE DEFECT, IN ONE LINE'),
    ('### bar 2, run where it lives', BANK,
     'A SUITE RUN SOMEWHERE ELSE IS THE COPY AGAIN, AND THE COPY IS THE THING BEING'),
    ('### b357 predicted the shape and could not predict the future', BANK,
     'ARITHMETIC OF THE FUTURE, AND NOTHING COULD.**'),
    ("### b363's sentence right, its placing misleading", BANK,
     "AND `b363`'s READING OF THE INCIDENT WAS RIGHT IN ITS SENTENCE AND MISLEADING IN ITS PLACE"),
    ('### the absolute-path work-order NOT restated, and why', BANK,
     'ATTACHING IT HERE WOULD HAVE FILED A TRUE WORK-ORDER AGAINST A FALSE CAUSE'),
    ('### the filing proposes nothing', BANK, 'IT PROPOSES NOTHING.**'),
    ('### not an errata entry', BANK, 'AND IT IS NOT AN ERRATA ENTRY.** ### ERRATA is for defects'),
    ('### a dated arm is not a wrong arm', BANK,
     'THEY ARE NOT THE SAME AND THE RECORD SHOULD NOT CONFUSE THEM'),
    ('### the choice named and not made', BANK,
     'DOES NOT DECIDE IT EITHER -- IT NAMES THE CHOICE'),
    ('### the drift reaches the prose', BANK,
     'A BANKED ACT THAT CITES A LINE NUMBER IS CITING A MOVING TARGET'),
    ('### the unchanged bar and its floor', BANK,
     'IT PROVES NO EDIT WAS MADE. ### IT DOES NOT PROVE THE DIAGNOSIS IS'),
    ('### the registration gate fired on this act own registration', BANK,
     "THE REGISTRATION GATE FIRED ON THIS ACT'S OWN REGISTRATION, AND IT WAS RIGHT"),
    ('### two hints typed from sense rather than line breaks', BANK,
     'TWO HINTS TYPED FROM THE ORDER'),
    ('### a shape assumed rather than read, again', BANK,
     "THE GATE RUNNER'S RETURN SHAPE WAS ASSUMED AND NOT READ"),
    ('### the reasoning true and the conclusion not following', BANK,
     'ALSO REFUTED -- AND THE REASONING WAS THE TRAP'),
    ("### the credit belongs to the order's test", BANK,
     'BRANCH TEST -- RUN IT WHERE IT LIVES -- IS THE WHOLE OF WHY THIS CAME OUT DIFFERENTLY'),
    ('### the other suites were not audited', BANK,
     'THIS ACT DID NOT AUDIT THE OTHER FIVE SUITES FOR ARMS OF THE SAME SHAPE'),
]

MUST_FAIL = [
    ('the bank never says the arm is repaired', BANK, '### THE ARM IS REPAIRED.'),
    ('the bank never says the banked verdict is withdrawn', BANK, '### THE BANKED VERDICT IS WITHDRAWN.'),
    ('the bank never says a banked suite was edited', BANK, '### A BANKED SUITE WAS EDITED.'),
    ('the bank never says the copy was made to pass', BANK, '### THE COPY WAS MADE TO PASS.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def blob_sha(rel):
    r = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD:' + rel], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    r2 = subprocess.run(['git', '-C', ROOT, 'cat-file', 'blob', r.stdout.strip()], capture_output=True)
    return hashlib.sha256(r2.stdout).hexdigest() if r2.returncode == 0 else None


def worktree_sha(rel):
    b = io.open(os.path.join(ROOT, rel.replace('/', os.sep)), 'rb').read()
    return hashlib.sha256(b.replace(b'\r\n', b'\n')).hexdigest()


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
    print('b364 -- GATE SUITE (THE COPY THAT DID NOT REPRODUCE)')
    print('=' * 100)
    extract = io.open(d(_J['E']['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### BUILT BY `gate_needle` FROM THE FILE THAT EMITTED THEM, AND EACH')
    print('  ### ALSO PRESENT IN THE RELIED-ON EXTRACT FILE:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, _line = GN.present(extract, path, hint)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES ### BUILT BY `gate_needle` FROM THIS ACT’S OWN BANK:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, NEVER normalised and never a substring):')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    E, J, F = _J['E'], _J['J'], _J['F']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()

    print(chr(10) + '  G-PREDICATE (the arm is QUOTED from its own suite, never paraphrased):')
    p1 = E['predicate_lines'] >= 5 and E['without_anchor'] == 0
    p2 = J['predicate_missing'] == 0 and len(J['predicate']) >= 5
    # ### **THE FIRST VERSION OF THIS SUB-ARM ASKED THE BANK FOR A `print(...)` STATEMENT.** ### The
    # ### bank quotes the arm's LABEL, which is what a bank should quote; the suite's line is python.
    # ### **AN ARM THAT CANNOT PASS ON CORRECT WRITING IS NOT A STRICTER ARM; IT IS THE WRONG ARM**
    # ### (b362's banked sentence), and this is its live instance in this act's own suite.
    p3 = 'G-LOCATED (every classified row located by the anchor tool at its own ledger, NOW)' in bank
    p4 = "ok_dec = ('%d' % was) in bank" in bank
    p5 = 'A PARAPHRASED PREDICATE' in bf
    gp = p1 and p2 and p3 and p4 and p5
    print('    %d predicate lines located at the suite, 0 without an anchor : %s'
          % (E['predicate_lines'], p1))
    print('    the diagnosis quoted every one of them : %s' % p2)
    print("    ### **THE PASS CONDITION IS IN THE BANK VERBATIM** : %s" % p4)
    print('    and the bank states the bar it is under : %s' % p5)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PREDICATE')

    print(chr(10) + '  G-COPY (the copy was re-made, run and DELETED; its finding recorded):')
    c1 = J['copy_failing'] is not None and J['copy_failing'] > 0
    c2 = 'G-LOCATED' in (J['copy_names'] or '')
    c3 = not J['copies_left']
    c4 = 'b357  banked GATES FAILING 0' in io.open(CEN363, encoding='utf-8', errors='replace').read()
    gc = c1 and c2 and c3 and c4
    print('    the copy fails : %s %s ; on G-LOCATED : %s' % (J['copy_failing'], J['copy_names'], c2))
    print("    ### **NO COPY SURVIVED THE RUN** : %s %s ; b363's banked row still reads as it did : %s"
          % (c3, J['copies_left'] or '', c4))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-COPY')

    print(chr(10) + '  G-BANKED (the banked suite RUN AT ITS OWN LOCATION, unedited) ### BAR 2:')
    b1 = J['home_failing'] is not None
    b2 = J['home_failing'] == J['copy_failing'] and J['home_names'] == J['copy_names']
    b3 = 'rows re-located at their ledgers' in (J['home_section'] or '')
    b4 = J['suite'] == 'tools/b357_checks.py'
    gb = b1 and b2 and b3 and b4
    print('    the banked suite produced a verdict at its own location : %s (%s %s)'
          % (b1, J['home_failing'], J['home_names']))
    print('    ### ### **AND IT IS THE SAME VERDICT THE COPY GAVE : %s**' % b2)
    print('    its G-LOCATED block was captured whole : %s ; the suite is %s : %s'
          % (b3, J['suite'], b4))
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BANKED')

    print(chr(10) + '  G-BRANCH (one of three, decided by the run at home, the others shown unreachable):')
    r1 = J['branch'] in ('ENVIRONMENTAL', 'REAL', 'UNDECIDED')
    r2 = (J['branch'] == 'REAL') == (J['home_failing'] != 0)
    r3 = ('BRANCH : %s' % J['branch']) in io.open(d(J['run_file']), encoding='utf-8',
                                                  errors='replace').read()
    r4 = all(('%s` -- UNREACHABLE' % b) in bank or ('%s** -- UNREACHABLE' % b) in bank
             for b in ('ENVIRONMENTAL', 'UNDECIDED') if b != J['branch'])
    r5 = 'TAKEN: `REAL`' in bank or ('TAKEN: `%s`' % J['branch']) in bank
    gr = r1 and r2 and r3 and r4 and r5
    print('    the branch is one of the three fixed forms : %s (%r)' % (r1, J['branch']))
    print('    ### **AND IT FOLLOWS FROM THE RUN AT HOME AND NOT FROM THE COPY** : %s' % r2)
    print('    the run file says so : %s ; the branch taken is named in the bank : %s' % (r3, r5))
    print('    ### **AND EVERY BRANCH NOT TAKEN IS SHOWN UNREACHABLE** : %s' % r4)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-BRANCH')

    print(chr(10) + '  G-UNCHANGED (every file the diagnosis read is byte-identical to its blob) '
          '### the working-tree half READ BEFORE THE PUSH:')
    # ### ### **ONE FILE IS BOTH READ BY THE DIAGNOSIS AND APPENDED TO BY THE CLOSING**, and the first
    # ### version of this arm did not allow for that: `tools/banked_index.py` is one of the four ledgers
    # ### `G-LOCATED` reads, AND it is where every act writes its own key. ### **THE CLAIM THE
    # ### ### REGISTRATION MADE IS THAT THE DIAGNOSIS DID NOT WRITE IT** -- which the diagnosis recorded
    # ### at BOTH of its own ends -- ### **NOT THAT THE ACT NEVER TOUCHES IT.** ### An arm demanding the
    # ### latter fires on this act's own correct closing, which is the wrong arm again.
    # ### **AND THE KEY IS SPLICED, NOT APPENDED** (b362's G-LEDGER incident), so the invariant here is
    # ### ORDER-PRESERVING PRESENCE and not a true prefix.
    IDXREL = 'tools/banked_index.py'
    rows_u = []
    for rel in UNTOUCHABLE:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        same = os.path.exists(p) and worktree_sha(rel) == blob_sha(rel)
        rows_u.append((rel, same))
        note = '' if rel != IDXREL else '   ### THIS ACT APPENDS ITS OWN KEY HERE, AT THE CLOSING'
        print('    %-40s worktree==blob : %-5s%s' % (rel, same, note))
    u1 = all(sm2 for r2, sm2 in rows_u if r2 != IDXREL)
    blobtxt = blob_of(ROOT, IDXREL) or ''
    worktxt = io.open(os.path.join(ROOT, IDXREL.replace('/', os.sep)), encoding='utf-8').read()
    bl = [x for x in norm(blobtxt).split(chr(10)) if x.strip()]
    wl = norm(worktxt).split(chr(10))
    it = iter(wl)
    u_idx = bool(bl) and all(any(x == ln for x in it) for ln in bl)
    u_key = 'READ BACK : dated-arm returns 1 row(s)' in io.open(IDX, encoding='utf-8').read()
    u2 = J['unchanged_ok'] is True
    u3 = len(J['unchanged_before']) == len(UNTOUCHABLE) == len(J['unchanged_after'])
    gu = u1 and u_idx and u_key and u2 and u3
    print('    ### ### **EVERY FILE BUT THE INDEX IS BYTE-IDENTICAL TO ITS BLOB NOW : %s**' % u1)
    print('    ### **AND THE INDEX: EVERY LINE OF ITS BLOB IS STILL PRESENT, IN ORDER : %s** ### -- the'
          % u_idx)
    print('    ### key is SPLICED, not appended, so a true-prefix test could not pass on a correct write.')
    print("    ### and the change is this act's own closing, which its run file records : %s" % u_key)
    print('    ### the diagnosis recorded every file unchanged at BOTH of its own ends : %s ; %d files : %s'
          % (u2, len(UNTOUCHABLE), u3))
    print('    ### **AND THE COMPARISON NORMALISES LINE ENDINGS AND NOTHING ELSE** (b309s autocrlf trap).')
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNCHANGED')

    print(chr(10) + '  G-NOEDIT (no owner instrument; no banked suite; only this act’s papers path) '
          '### the working-tree half READ BEFORE THE PUSH:')
    owner = ['tools/e16/b264_eps_decay.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py',
             'tools/anchor_from_file.py', 'tools/quote_norm.py', 'tools/ferry_scan.py',
             'tools/gate_needle.py', 'tools/b327_faces_row.py', 'tools/mirror_roster.json',
             'tools/mirror_verify.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    suites = ['tools/b355_checks.py', 'tools/b356_checks.py', 'tools/b357_checks.py',
              'tools/b360_checks.py', 'tools/b361_checks.py', 'tools/b362_checks.py',
              'tools/b363_checks.py']
    suites_touched = [p for p in suites if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'OPEN_TRAILS.md']
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    tech = not git(TC, 'status', '--porcelain').strip() if os.path.isdir(TC) else True
    gne = (not touched and not suites_touched and not ppbad and faces_clean and hand and dep and fnd and tech)
    print('    owner instruments modified : %s' % (touched or 'none'))
    print('    ### **BANKED SUITES MODIFIED : %s**' % (suites_touched or 'none'))
    print('    papers paths beyond OPEN_TRAILS.md : %s' % (ppbad or 'none'))
    print('    ### **FACES_LEDGER.md UNTOUCHED, BECAUSE NO ROW MOVED** : %s' % faces_clean)
    print('    HANDOFF clean : %s ; the deposited monograph clean : %s ; FINDINGS clean : %s ; TECHNE clean : %s'
          % (hand, dep, fnd, tech))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-RESTATED (the finding is FILED for the author and proposes nothing) '
          '### the ancestry half READ BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    f1 = trails.count(TRAIL_MARK) == 1
    f2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    f3 = F['prefix_of_file'] and F['prefix_of_blob']
    f4 = (F['verdict_withdrawn'] is False and F['arm_repaired'] is False
          and F['suite_edited'] is False)
    blk = trails.split(TRAIL_MARK)[-1]
    try:
        f5 = (GN.present_needle(blk, GN.build(TRAILS, 'FILED FOR THE AUTHOR AND NOT ACTED ON.')[1])
              and GN.present_needle(blk, GN.build(TRAILS, 'The choices are the author')[1]))
    except GN.NeedleError:
        f5 = False
    f6 = F['entry'] in bank and F['entry'] in trails
    # ### **AND THE WORK-ORDER THAT IS *NOT* RESTATED IS NAMED, WITH ITS REASON.**
    f7 = 'W-ORD-ABSOLUTE-PATHS' in bank and 'AGAINST A FALSE CAUSE' in bf
    gf = f1 and f2 and f3 and f4 and f5 and f6 and f7
    print('    the mark appears exactly once : %s ; the committed blob is a true prefix : %s' % (f1, f2))
    print('    the writing tool recorded append-only both ways : %s' % f3)
    print('    ### **NO VERDICT WITHDRAWN, NO ARM REPAIRED, NO SUITE EDITED (recorded)** : %s' % f4)
    print('    the entry says it is filed for the author and proposes nothing : %s' % f5)
    print('    ### **AND THE ABSOLUTE-PATH WORK-ORDER IS NAMED AS *NOT* RESTATED, WITH ITS REASON** : %s'
          % f7)
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-RESTATED')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason) ### READ BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'A DIAGNOSIS IS NOT A CURE' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOREPAIR:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : dated-arm returns 1 row(s)' in irun
    k2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
             ('the arm is repaired', 'the banked verdict is withdrawn',
              'b357 is re-verdicted', 'the copy was at fault'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (k1, k2, k3))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOREPAIR')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock) ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, J, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY READ OF THE SUITE UNDER DIAGNOSIS AND BEFORE ANY RUN OF IT' in gate_text.flat(reg)
    go = o1 and o2 and o3 and o4 and o5
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('        lock    %s' % (stampm.group(1) if stampm else '?'))
    print('        extract %s   diagnosis %s   filing %s' % (E['run_clock'], J['run_clock'], F['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE ANY READ : %s' % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b364_hooks.txt'), d('b364_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh = h_ok and m_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror clean on all three : %s'
              % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    cl = re.search(r'clauses\s*:\s*(\d+)', sat)
    sm = re.search(r'### bytes locked : (\d+)', reg)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [
        ('the home verdict %s %s' % (J['home_failing'], J['home_names']),
         ("`GATES FAILING : %d %s`" % (J['home_failing'], J['home_names'])) in bank),
        ('the located half, verbatim', 'rows re-located at their ledgers : 12 of 12' in bank),
        ('every moved row, both numbers',
         all(('`%d`, now `%d`' % (b, c)) in bank for _a, b, c in F['moved'])),
        ('the moved-row count %d' % len(F['moved']), len(F['moved']) == 4),
        ("b357's own declared moves 1054 and 645", '1054' in bank and '645' in bank),
        ('the trail entry grew the file by %d bytes' % F['grew'], str(F['grew']) in bank),
        ('reads %d' % E['reads'], ('%d reads' % E['reads']) in bank),
        ('without an anchor %d' % E['without_anchor'],
         ('%d without an anchor' % E['without_anchor']) in bank),
        # ### **THE FIRST VERSION BUILT THIS NEEDLE WITH A LINE BREAK IN IT** and asked a
        # ### whitespace-collapsed bank for it. ### The bank says the phrase; the arm asked for a
        # ### rendering. ### **THE FLATTENED BANK IS WHAT A PROSE FIGURE IS READ FROM.**
        ('anchors differing %d of %d' % (E['anchors_differing'], E['reads']),
         ('%d of %d anchors differing' % (E['anchors_differing'], E['reads'])) in bf),
        ('predicate lines %d' % E['predicate_lines'],
         ('%d PREDICATE LINES' % E['predicate_lines']) in bank),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on diagnosis run file', J['run_file'] in bank),
        ('the relied-on filing run file', F['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks, never by name):')
    once = True
    for lbl, jf in (('extract', E), ('diagnosis', J), ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-10s %-26s clock on disk %s == the JSON's %s : %s"
              % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    repeats = sorted(f for f in os.listdir(D) if re.match(r'^b364_extract_notes\d*\.txt$', f))
    named = all(f in bank for f in repeats)
    once = once and named
    print('    ### **EVERY REPEAT IS NAMED IN THE BANK, SUPERSEDED OR RELIED ON : %s** %s' % (named, repeats))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed about the object, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    mine = ('b364_regspec.py', 'b364_extract.py', 'b364_diagnose.py', 'b364_filing.py',
            'b364_correspondence.py', 'b364_index_append.py', 'b364_checks.py')
    for p in [t(x) for x in mine]:
        src2 = strip_prose(p)
        for b in banned:
            if b in src2:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b364_diagnose.py', 'b364_extract.py',
                                                       'b364_filing.py'))]
    gnc = not hits and not imports
    print("    numerical calls in this act's STRIPPED sources : %d %s" % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

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

    marker = '# ### THE COPY THAT DID NOT REPRODUCE, DIAGNOSED AND NOT REPAIRED (b364).'
    nxt = '# ### THE ANCHORED GATE ARMS, COUNTED AND NOT ASSERTED (b363).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk),
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the trail block and the index row):')
    tmpdir = tempfile.mkdtemp(prefix='b364_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk),
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
    print('  ### needles refused : %d ; owner needles not in the extract file : %d' % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
