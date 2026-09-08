# -*- coding: utf-8 -*-
"""b366_checks.py -- THE GATE SUITE FOR THE DATED-ARM SWEEP.

### ### **THIS SUITE IS WRITTEN UNDER THE RULING IT EXECUTES.** ### `(R2)` splits arms into STANDING and
### DATED, and ### **NOT ONE ARM HERE IS WRITTEN BY ADDRESS AGAINST THE LIVING RECORD.** ### An act that
### swept for dated arms and shipped one would have refuted itself, and `G-SELFCLEAN` re-measures that on
### this file with the sweep's own detector rather than taking it on the seat's word.
### ### **IT USES `gate_needle` (`b363`), `gate_text.flat` AND `gate_content` (`b366`) AND DEFINES NO
### ### FLATTENER OF ITS OWN**, and every `G-NO*`-shaped arm reads STRIPPED CODE or a marked region
### rather than raw prose -- `b348`'s rule.
### ### **THE ARMS (locked registration section (G)):** ### `G-QUOTED`, `G-PLACED`, `G-COUNT`, `G-DETECT`,
### `G-DECLARED`, `G-SUBST`, `G-RULE`, `G-MINT`, `G-RELABEL`, `G-LEDGER`, `G-THRESHOLD`, `G-UNEDITED`,
### `G-SELFCLEAN`, `G-NOEDIT`, `G-ROW`, `G-KEY` with `G-NOTREPAIRED`, `G-ORDER`, `G-NUMBERS`,
### `G-TOOLNUM`, `G-ONCE`, `G-NOCOMPUTE`, the struck-clause and stem sweeps, `G-SHARED`, the hedge audit,
### the must-fail fixtures.
### ### **THE SIDES, DECLARED BY `b352`'s RULE:** ### `G-UNEDITED`'s and `G-NOEDIT`'s working-tree halves
### and `G-ROW`'s and `G-LEDGER`'s ancestry readings are read BEFORE THE PUSH; `G-HOOK`/`G-MIRROR` AFTER
### THE PUSH; `G-ORDER` SIDE-INVARIANT.
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
import gate_content as GC  # noqa: E402  ### THE RULE THIS ACT WRITES, EXERCISED HERE
import b366_sweep as SW   # noqa: E402  ### THE DETECTOR, TURNED ON THIS FILE

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b366_the_dated_arm_sweep.txt')
REG = d('b366_registration_2026-09-07.txt')
FERRY = d('b366_ferry_2026-09-07.txt')
DRAFT = d('b365_closing.txt')
SRC = d('b358_source_lagarias0404394.txt')
B357S = t('b357_checks.py')
B363 = d('b363_the_anchored_gate_arms.txt')
B364 = d('b364_the_copy_that_did_not_reproduce.txt')
B365 = d('b365_the_owed_read_paid.txt')
CORR, IDX = d('b366_corr_run.txt'), d('b366_index_run.txt')
SCAN, TERMSCAN, GATE = d('b366_ferry_scan.txt'), d('b366_reg_termscan.txt'), d('b366_reg_gate.txt')
CENSUS0, FCEN = d('b366_census_stepzero.txt'), d('b366_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b366_regspec_run.txt'), d('audit_b366_reg_satisfiable.txt')
PINS = d('b366_pins_stepzero.txt')
SEAL = '1f8ead5abdb5534f165413f1f48ac4f357764349e1a4919582931080ed277d9f'
ROWNUM = '215'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b366_reads.json'), ('S', 'b366_sweep.json'),
                   ('F', 'b366_faces_row.json'), ('M', 'b366_mint.json'))}

NEW_THIS_ACT = {'tools/b366_regspec.py', 'tools/b366_extract.py', 'tools/b366_sweep.py',
                'tools/gate_content.py', 'tools/b366_faces_row.py', 'tools/b366_mint.py',
                'tools/b366_correspondence.py', 'tools/b366_index_append.py', 'tools/b366_checks.py'}

TOOLNUM = [
    ('146 suites, 1255 arms, 3 dated', 'tools/b366_sweep.py'),
    ('the rewrite rule and its six fixtures', 'tools/gate_content.py'),
    ('the 35 reads and the 16 differing anchors', 'tools/b366_extract.py'),
    ('the U1 update block', 'tools/b366_faces_row.py'),
    ('the ledger writer it imports', 'tools/b327_faces_row.py'),
    ('the module and the TECHNE head', 'tools/b366_mint.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 215', 'tools/b366_correspondence.py'),
    ('the key', 'tools/b366_index_append.py'),
    ('56 clauses', 'tools/b366_regspec.py'),
    ('18225 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b366 - THE DATED-ARM SWEEP. The executor'),
    ('(R1) -- the fold threshold', FERRY, '(R1) THE FOLD THRESHOLD is NINE acts. Until a span'),
    ('(R1) -- and the spans stay beside it', FERRY,
     '"the fold is due" is not said. The nine observed spans stay on'),
    ('(R2) -- what a gate suite is for', FERRY,
     '(R2) WHAT A GATE SUITE IS FOR, split by predicate. An arm'),
    ('(R2) -- the standing half', FERRY,
     'the act wrote - is a STANDING CHECK and must reproduce at any'),
    ('(R2) -- the content/address test', FERRY,
     'by CONTENT rather than by ADDRESS: a predicate asking whether a'),
    ('(R2) -- prospective, nothing rewritten', FERRY,
     'row sits at a line number is dated. Prospective. No past suite'),
    ("(R2) -- b363's control relabelled here", FERRY,
     'correctness on its standing ones - relabelled in this act'),
    ('(R3) -- the grade word', FERRY, '(R3) THE GRADE WORD: where a source applies its own theorem to'),
    ('the order -- addition one', FERRY, 'ADDITION ONE - THE RULING THE DRAFT NAMES IS QUOTED FIRST:'),
    ('the order -- addition two', FERRY, 'ADDITION TWO - THE SWEEP AS A REWRITE RULE, NOT A REPAIR:'),
    ('the order -- the helper-or-work-order test', FERRY,
     'by tool; write the rewrite rule (address predicates become'),
    ('the order -- the two figures asked for apart', FERRY,
     'exist and how many are one substitution from standing.'),
    ('the order -- addition three', FERRY,
     'ADDITION THREE - THE TWO SPECIES KEPT APART, as b364 kept them:'),
    ('the draft -- the ruling it named', DRAFT,
     'AND THE ONE THING THAT WOULD MAKE THE SWEEP UNNECESSARY, NAMED:'),
    ('the draft -- and what it says would follow', DRAFT,
     'that a banked suite is a certificate of its own moment and is not re-run.'),
    ('the confirmed instance -- its own label', B357S,
     'G-LOCATED (every classified row located by the anchor tool at its own ledger, NOW)'),
    ('the confirmed instance -- the address comparison', B357S, "if n != r['line']:"),
    ("b363 -- the control's figure", B363, "COPIES REPRODUCING THEIR OWN ACT'S VERDICT : 5 of 6"),
    ('b364 -- the species named', B364, 'AND THE SPECIES IS NAMED: A DATED ARM'),
    ('b364 -- the choice it named and did not make', B364,
     'DOES NOT DECIDE IT EITHER -- IT NAMES THE CHOICE'),
    ('b365 -- the other species and its cure', B365, 'ITS ONLY CURE IS A SECOND READER.**'),
    ("the source -- Theorem 5.1's own quantifier", SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    ('the source -- it evaluates the constant for the exception', SRC, 'C1(πtriv ) = 1'),
]

SELF_NEEDLES = [
    ('the bank states the counts first', BANK,
     'THREE DATED ARMS IN THE WHOLE RECORD, OUT OF 1255 ARMS ACROSS 146 SUITES'),
    ('### and the third is missing its content, not harder', BANK,
     'AND THE THIRD IS NOT HARDER TO WRITE. ### IT IS MISSING ITS CONTENT'),
    ('### the species is real and is not a class', BANK,
     'IT IS NOT A CLASS THIS RECORD IS RIDDLED WITH'),
    ("### addition one's answer", BANK, 'IS NOT THE RULING THE DRAFT NAMED'),
    ('### the draft quoted at its own file', BANK,
     'AND THE ONE THING THAT WOULD MAKE THE SWEEP UNNECESSARY, NAMED: a ruling that a banked suite is'),
    ('### the split, and where it agrees and contradicts', BANK, 'ON THE DATED HALF THEY AGREE'),
    ('### one incident does not show you a partition', BANK,
     'PARTITION.** ### That is this act'),
    ('### the population, counted from the suites', BANK,
     '146 GATE SUITES IN THE RELAY REPOSITORY.** ### **1255 ARMS REGISTERED BY THEIR OWN SUITES'),
    ('### the unattributed are reported, not dropped', BANK,
     'AND 243 REGISTRATIONS WHOSE NAME IS NOT A LITERAL ARE REPORTED AS `UNATTRIBUTED`'),
    ('### the borrowed flattener, and the zero it produced', BANK,
     'AN ABSENCE PRODUCED BY A TOOL BORROWED FOR THE WRONG JOB'),
    ("### the detector's reach, stated before it ran", BANK,
     "IT CANNOT DECIDE WHETHER THE FILE BEING INDEXED IS THE ACT'S OWN ARTIFACT OR THE LIVING RECORD"),
    ('### the tool refuses to emit on a disagreement', BANK,
     'AND THE TOOL REFUSES TO EMIT IF THE FLAGS AND THE DECLARATIONS DISAGREE'),
    ('### it found the confirmed instance', BANK,
     'AND IT FOUND THE ONE CONFIRMED INSTANCE THE RECORD HOLDS'),
    ('### the standing exception that proves the rule', BANK,
     'IS THE ACT’S OWN ARTIFACT AND THE ARM IS STANDING'),
    ("### the net's precision, and what a wide net costs", BANK,
     "SO THE NET'S PRECISION ON THIS POPULATION IS 4 OF 7"),
    ("### the order's own test of the rule's form", BANK, 'IT IS ONE LINE, SO IT IS A HELPER'),
    ('### the branch not taken, shown unreachable', BANK,
     '(A WORK-ORDER WITH ITS PRICE) -- UNREACHABLE'),
    ('### the fixture that matters is not the one that agrees', BANK,
     'ON A MOVED FILE THE ADDRESS FORM SILENTLY READS A DIFFERENT LINE'),
    ('### and a rewrite that only quietened arms would be a softener', BANK,
     'A REWRITE THAT ONLY EVER QUIETENED ARMS WOULD BE A SOFTENER'),
    ('### the two species, and why they are apart', BANK,
     'A RECORD THAT COLLAPSED THE TWO WOULD LOOK FOR A SECOND READER WHERE A RULING WAS NEEDED'),
    ("### the relabelling: two measurements reported as one", BANK,
     'THE RELABELLING: THAT FIGURE IS TWO MEASUREMENTS REPORTED AS ONE'),
    ("### and b363's verdict is not withdrawn", BANK,
     'A RELABELLING NAMES'),
    ('### (R3) applied, and its reach bounded', BANK,
     'AND ITS REACH IS BOUNDED IN THE BLOCK:'),
    ('### no grade is conferred by a seat', BANK,
     'AND NO GRADE IS CONFERRED BY A SEAT.** ### `(R3)` fixes the word'),
    ('### (R1) recorded, and the fold not due', BANK,
     'SIX AGAINST NINE: THE FOLD'),
    ('### what a ruling buys that an argument cannot', BANK,
     'AND THAT IS THE SMALL THING A RULING BUYS THAT AN ARGUMENT CANNOT'),
    ('### the unedited bar and its floor', BANK,
     'IT PROVES NO SUITE WAS EDITED. ### IT DOES NOT PROVE THE'),
    ('### the heredoc, a fifth and sixth time', BANK,
     'THE HEREDOC, A FIFTH AND SIXTH TIME, AND THE SECOND ONE COST THE ZERO ABOVE'),
    ('### the expectation half met and half refuted', BANK,
     'THE SECOND HALF IS REFUTED, AND IT IS REFUTED BY THE ARITHMETIC OF ITS OWN WORD'),
    ('### three consecutive acts in the same shape', BANK,
     'IT SHOULD BE READ AS A PROPERTY OF THIS SEAT AND NOT AS A RUN OF BAD LUCK'),
    ('### the detector is not a decision procedure', BANK,
     'PREDICATE WRITTEN IN A SHAPE IT DOES NOT NAME WOULD NOT BE FOUND'),
]

MUST_FAIL = [
    ('the bank never says a past suite was edited', BANK, '### A PAST SUITE WAS EDITED.'),
    ('the bank never says the dated arms are repaired', BANK, '### THE DATED ARMS ARE REPAIRED.'),
    ('the bank never says the sweep is unnecessary', BANK, '### THE SWEEP IS UNNECESSARY.'),
    ('the bank never says this seat rules the threshold', BANK, '### THIS SEAT RULES THE THRESHOLD.'),
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
    print('b366 -- GATE SUITE (THE DATED-ARM SWEEP)')
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
    E, S, F, M = _J['E'], _J['S'], _J['F'], _J['M']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    faces = io.open(FACES, encoding='utf-8', newline='').read()

    print(chr(10) + '  G-QUOTED (Addition One: the draft’s ruling quoted verbatim, with its location):')
    # ### **THE BANK WRAPS THE QUOTATION ACROSS TWO MARKED LINES**, so the raw text does not carry the
    # ### phrase and the FLATTENED text does. ### The needle-wrapping species, in the suite of the act
    # ### that swept for arm defects; the cure is the flattener the record already owns.
    q1 = 'a ruling that a banked suite is a certificate of its own moment and is not re-run' in bf
    q2 = 'data/b365_closing.txt' in bank
    q3 = any(b['tag'] == 'DRAFT' for b in E['built'])
    q4 = E['without_anchor'] == 0
    gq = q1 and q2 and q3 and q4
    print('    the ruling is quoted verbatim in the bank : %s ; with its file named : %s' % (q1, q2))
    print('    and re-pulled from that file by the anchor tool : %s (0 without an anchor : %s)' % (q3, q4))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED')

    print(chr(10) + '  G-PLACED (Addition One: (R2) placed against it -- same, different, or compatible):')
    p1 = 'IS NOT THAT RULING' in bf and 'IT IS A DIFFERENT ONE' in bf
    p2 = 'ON THE DATED HALF THEY AGREE' in bf and 'ON THE STANDING HALF THEY CONTRADICT' in bf
    p3 = 'SO THE SWEEP IS NOT UNNECESSARY' in bf
    p4 = 'ALL THREE ADDITIONS RAN' in bf
    gp = p1 and p2 and p3 and p4
    print('    it says which of the three it is : %s ; and where it agrees and contradicts : %s' % (p1, p2))
    print('    ### **AND IT SAYS THE SWEEP IS NOT UNNECESSARY** : %s ; all three additions ran : %s'
          % (p3, p4))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PLACED')

    print(chr(10) + '  G-COUNT (the population counted from the suites’ own code, not estimated):')
    c1 = S['suites'] > 0 and S['arms'] > 0
    c2 = len(S['rows']) == S['flagged']
    c3 = S['dated'] + S['standing'] + S['not_address'] == len(S['rows'])
    c4 = not S['untokenizable']
    c5 = ('%d GATE SUITES' % S['suites']) in bank and ('%d ARMS REGISTERED' % S['arms']) in bank
    c6 = ('%d REGISTRATIONS WHOSE NAME IS NOT A LITERAL' % S['unattributed']) in bank
    gc = c1 and c2 and c3 and c4 and c5 and c6
    print('    %d suites, %d arms : %s ; every flagged line has a row : %s' % (S['suites'], S['arms'], c1, c2))
    print('    ### **THE THREE CLASSES PARTITION THE FLAGGED SET** : %s' % c3)
    print('    no suite failed to tokenize : %s ; the figures are on the bank : %s / %s' % (c4, c5, c6))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-COUNT')

    print(chr(10) + '  G-DETECT (the detector scored before it is believed; both polarities):')
    d1 = SW.self_test(False)
    d2 = S['detector_fixtures'] is True
    d3 = S['confirmed_instance_found'] is True
    d4 = any(r['suite'] == 'b357_checks.py' and r['arm'] == 'G-LOCATED'
             and r['classification'] == 'DATED' for r in S['rows'])
    d5 = len(S['shapes']) == 3
    gd = d1 and d2 and d3 and d4 and d5
    print('    the fixtures pass on a fresh run : %s ; the sweep recorded them : %s' % (d1, d2))
    print('    ### **AND IT FOUND THE ONE CONFIRMED INSTANCE (b357 G-LOCATED)** : %s / %s' % (d3, d4))
    print('    three named shapes, and the reach stated : %s' % d5)
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-DETECT')

    print(chr(10) + '  G-DECLARED (every flagged arm classified by this seat, with its code beside it):')
    e1 = all(r['why'].strip() for r in S['rows'])
    e2 = all(r['code'].strip() for r in S['rows'])
    e3 = all(r['classification'] in ('DATED', 'STANDING', 'NOT AN ADDRESS PREDICATE') for r in S['rows'])
    e4 = 'CLASSIFICATION IS DECLARED' in bf or 'THE CLASSIFICATION IS DECLARED' in bf
    e5 = all(('`%s`' % r['arm']) in bank for r in S['rows'] if r['classification'] != 'NOT AN ADDRESS PREDICATE')
    ge = e1 and e2 and e3 and e4 and e5
    print('    every row carries a reason : %s ; and its own code line : %s' % (e1, e2))
    print('    every class is one of the three : %s ; the bank says it is declared : %s' % (e3, e4))
    print('    every DATED and STANDING arm is named in the bank : %s' % e5)
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-DECLARED')

    print(chr(10) + '  G-SUBST (the two figures the order asked for, reported APART):')
    s1 = S['dated'] >= S['one_substitution']
    s2 = ('%d DATED ARMS' % S['dated']) in bank or ('THREE DATED ARMS' in bank and S['dated'] == 3)
    s3 = 'ONE SUBSTITUTION FROM STANDING' in bank
    s4 = 'IT IS MISSING ITS CONTENT' in bf
    s5 = S['dated'] != S['one_substitution']
    gs = s1 and s2 and s3 and s4 and s5
    print('    dated %d ; one substitution from standing %d : %s' % (S['dated'], S['one_substitution'], s1))
    print('    ### **AND THEY ARE DIFFERENT NUMBERS, REPORTED APART** : %s' % s5)
    print('    and the reason the third is not one : %s' % s4)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SUBST')

    print(chr(10) + '  G-RULE (the rewrite rule, on the side the order’s own test put it):')
    r1 = GC.self_test(False)
    gcs = io.open(t('gate_content.py'), encoding='utf-8').read()
    r2 = 'line_by_content' in gcs and 'line_by_address' in gcs
    r3 = 'IT IS ONE LINE, SO IT IS A HELPER' in bf
    r4 = '(A WORK-ORDER WITH ITS PRICE) -- UNREACHABLE' in bank
    r5 = 'IT DOES NOT MAKE THE ARM RIGHT' in gate_text.flat(gcs)
    try:
        GC.line_by_content(BANK, 'A LINE THIS BANK DOES NOT CARRY AT ALL, ANYWHERE.')
        r6 = False
    except GC.ContentError:
        r6 = True
    gr = r1 and r2 and r3 and r4 and r5 and r6
    print('    six fixtures pass on a fresh run : %s ; both forms are written out : %s' % (r1, r2))
    print("    the bank states which side the order's test put it on : %s ; other branch unreachable : %s"
          % (r3, r4))
    print('    the helper states what it does NOT buy : %s ; and it RAISES on an absent text : %s'
          % (r5, r6))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RULE')

    print(chr(10) + '  G-MINT (the two species kept APART; local-only) ### READ BEFORE THE PUSH:')
    modpath = os.path.join(TC, M['module'].replace('/', os.sep))
    mtxt = io.open(modpath, encoding='utf-8', errors='replace').read() if os.path.exists(modpath) else ''
    other = os.path.join(TC, 'modules', '2026-09', 'WRONG_ARM.md')
    m1 = M['module_ok'] is True and os.path.exists(modpath)
    m2 = os.path.exists(other) and 'WRONG_ARM.md' in mtxt
    m3 = M['pushed'] is False and int(M['commits_ahead_of_origin'] or 0) > 0
    m4 = all(v['equal'] for v in M['quotes'].values())
    m5 = 'it was right that day' in mtxt and 'a decision about what a suite is for' in mtxt.lower()
    m6 = not git(TC, 'status', '--porcelain').strip()
    m7 = 'and b366 cured none' in mtxt
    gm = m1 and m2 and m3 and m4 and m5 and m6 and m7
    print('    the module exists and holds its own claims : %s' % m1)
    print('    ### **AND THE OTHER SPECIES IS BESIDE IT, NOT INSIDE IT** : %s' % m2)
    print('    ### **LOCAL ONLY: %s COMMITS AHEAD, PUSHED : %s** ; tree clean : %s'
          % (M['commits_ahead_of_origin'], M['pushed'], m6))
    print('    every quotation equal under the normaliser : %s ; the table’s two cures differ : %s' % (m4, m5))
    print('    and it says no arm was cured by it : %s' % m7)
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MINT')

    print(chr(10) + '  G-RELABEL ((R2)’s relabelling done HERE, not by editing b363):')
    b363txt = io.open(B363, encoding='utf-8').read()
    l1 = 'TWO MEASUREMENTS REPORTED AS ONE' in bf
    l2 = 'CORRECTNESS' in bf and 'DRIFT' in bf
    l3 = 'A RELABELLING NAMES WHAT AN EARLIER MEASUREMENT WAS MEASURING' in bf
    l4 = not git(ROOT, 'diff', '--name-only', 'HEAD', '--', 'data/b363_the_anchored_gate_arms.txt').strip()
    l5 = "COPIES REPRODUCING THEIR OWN ACT'S VERDICT : 5 of 6" in b363txt
    gl = l1 and l2 and l3 and l4 and l5
    print('    the relabelling is stated : %s ; both kinds named : %s' % (l1, l2))
    print('    and it says a relabelling is not a correction : %s' % l3)
    print("    ### **AND b363's BANK IS UNTOUCHED** : %s ; its own figure still reads as it did : %s"
          % (l4, l5))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-RELABEL')

    print(chr(10) + '  G-LEDGER ((R3) applied through the writer; append-only) ### READ BEFORE THE PUSH:')
    fb = blob_of(PP, 'FACES_LEDGER.md')
    k1 = F['status'] in ('WRITTEN', 'DUPLICATE')
    k2 = F['grade_conferred_by_seat'] is False and F['grade_ruled_by'].startswith('the author')
    k3 = F['row'] == 'U1' and F['half'] == 'ARCHIMEDEAN'
    blines = [x for x in norm(fb or '').split(chr(10)) if x.strip()]
    wlines = [x for x in norm(faces).split(chr(10)) if x.strip()]
    it = iter(wlines)
    k4 = bool(blines) and all(any(x == ln for x in it) for ln in blines)
    # ### **THE JSON CARRIES A STRAIGHT APOSTROPHE AND THE LEDGER CARRIES A CURLY ONE.** ### A raw
    # ### `in` test called that a missing grade word. ### **A PRESENTATION MISMATCH, WHICH IS EXACTLY
    # ### WHAT `gate_needle` EXISTS FOR**, and the comparison goes through it.
    k5 = GN.present_needle(faces, F['grade'])
    k6 = 'NO GRADE IS CONFERRED BY A SEAT' in faces
    gk = k1 and k2 and k3 and k4 and k5 and k6
    print('    the writer reports %s : %s ; row %s, %s half : %s' % (F['status'], k1, F['row'], F['half'], k3))
    print('    ### **EVERY LINE OF THE BLOB IS STILL PRESENT, IN ORDER** : %s' % k4)
    print('    ### the writer SPLICES its table rows, so a true-prefix test is not the arm used.')
    print('    the grade word is on the ledger : %s ; and the footer refuses conferral : %s' % (k5, k6))
    print('    the grade is ruled by %s, conferred by a seat : %s' % (F['grade_ruled_by'], not k2))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-LEDGER')

    print(chr(10) + '  G-THRESHOLD ((R1) recorded, the spans beside it, and the fold NOT due):')
    h1 = 'THE FOLD THRESHOLD IS NINE ACTS' in bf
    h2 = all(x in bank for x in ('`b266`-`b281` 16', '`b349`-`b359` 11'))
    h3 = 'SIX AGAINST NINE' in bf
    h4 = 'THE FOLD' in bf and 'IS NOT DUE' in bf
    h5 = GN.absent_exact(BANK, '### THIS SEAT RULES THE THRESHOLD.')
    gh = h1 and h2 and h3 and h4 and h5
    print('    the ruled number is recorded : %s ; the observed spans stay beside it : %s' % (h1, h2))
    print('    ### **AND THE FOLD IS NOT DUE, AS A COUNT** : %s / %s' % (h3, h4))
    print('    and the bank does not claim to have ruled it : %s' % h5)
    print('    %s' % ('PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-THRESHOLD')

    print(chr(10) + '  G-UNEDITED (every gate suite byte-identical to its blob) ### BEFORE THE PUSH:')
    dirty = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD', '--', 'tools/').splitlines()
             if x.strip().endswith('_checks.py') and 'b366' not in x]
    u1 = not dirty
    u2 = S['suites_dirty'] == []
    gu = u1 and u2
    print('    suite files differing from their committed blobs, now : %d %s' % (len(dirty), dirty or 'none'))
    print('    ### and the sweep recorded the same at its own run : %s' % u2)
    print('    ### **ITS FLOOR: IT PROVES NO SUITE WAS EDITED. ### IT DOES NOT PROVE THE CLASSIFICATION')
    print('    ### IS RIGHT.**')
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNEDITED')

    print(chr(10) + '  G-SELFCLEAN (### **THIS SUITE SHIPS NO DATED ARM** -- the detector, turned on itself):')
    mine = [t(x) for x in sorted(os.listdir(os.path.join(ROOT, 'tools'))) if x.startswith('b366_')]
    mine.append(t('gate_content.py'))
    selfhits = []
    for p in mine:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    # ### ### **THE FIRST VERSION OF THIS ARM WAS A WRONG ARM, IN THE ACT THAT SWEPT FOR ARM DEFECTS.**
    # ### Its label says ### *this suite ships no dated arm*; ### its predicate said ### *this act
    # ### contains none of the detector's shapes*. ### **THOSE ARE DIFFERENT SENTENCES**, and the sweep
    # ### had already established the difference: the net is wide and flags things that are not address
    # ### predicates at all -- 3 of 7 across the record. ### **AN ARM THAT TREATED EVERY HIT AS A DATED
    # ### ### ARM WOULD CONTRADICT ITS OWN ACT'S FINDING.**
    # ### **SO IT IS DECLARED HERE THE WAY THE SWEEP DECLARES THE RECORD'S**, and the arm fails only on
    # ### a hit this seat has NOT read and classified.
    SELF_DECLARED = {
        ('gate_content.py', 'line_by_address'):
            'the helper WRITES OUT the shape being replaced so its own fixtures can compare the two. '
            '### **A CONTROL, NOT AN ARM**, and its docstring says it is not for use in an arm.',
        ('b366_correspondence.py', 'last-row cells'):
            'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE -- to count its cells. '
            '### **A CONSTANT INDEX INTO THE ACT’S OWN FRESH OUTPUT**, which is the same shape the '
            'sweep classified NOT AN ADDRESS PREDICATE at `b326` and `b335`.',
    }

    def which(fn, code):
        if fn == 'gate_content.py':
            return 'line_by_address'
        if fn == 'b366_correspondence.py' and '[-1:]' in code:
            return 'last-row cells'
        return None

    undeclared = []
    for fn, i, code in selfhits:
        key = (fn, which(fn, code))
        print('    %-26s line %-6d | %s' % (fn, i, code))
        if key[1] is None or key not in SELF_DECLARED:
            undeclared.append((fn, i))
            print('        ### ### **UNDECLARED HIT.**')
        else:
            print('        %s' % SELF_DECLARED[key])
    gsc = not undeclared
    print('    ### hits in this act’s own files : %d ; declared with a reason : %d'
          % (len(selfhits), len(selfhits) - len(undeclared)))
    print('    ### ### **UNDECLARED HITS : %d** ### -- an act that swept for dated arms and shipped one'
          % len(undeclared))
    print('    ### would have refuted itself; and an act that flagged its own correct code as one would')
    print('    ### have refuted its own finding that the net is wide.')
    print('    %s' % ('PASS' if gsc else '### FAIL ###'))
    if not gsc:
        fails.append('G-SELFCLEAN')

    print(chr(10) + '  G-NOEDIT (no owner instrument; only this act’s papers path) ### BEFORE THE PUSH:')
    owner = ['tools/e16/b264_eps_decay.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py',
             'tools/anchor_from_file.py', 'tools/quote_norm.py', 'tools/ferry_scan.py',
             'tools/gate_needle.py', 'tools/b327_faces_row.py', 'tools/mirror_roster.json',
             'tools/mirror_verify.py', 'tools/b363_span.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').splitlines()
              if x.strip() and 'b366' not in x and x.strip() != 'tools/banked_index.py']
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'FACES_LEDGER.md']
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    trl = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'OPEN_TRAILS.md').strip()
    gne = (not touched and not others and not ppbad and hand and dep and fnd and trl)
    print('    owner instruments modified : %s' % (touched or 'none'))
    print('    ### **TRACKED RELAY FILES OF OTHER ACTS MODIFIED : %s**' % (others or 'none'))
    print('    papers paths beyond FACES_LEDGER.md : %s' % (ppbad or 'none'))
    print('    HANDOFF clean : %s ; monograph clean : %s ; FINDINGS clean : %s ; OPEN_TRAILS clean : %s'
          % (hand, dep, fnd, trl))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason) ### BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'A CLASSIFICATION IS NOT A CURE' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTREPAIRED:')
    irun = io.open(IDX, encoding='utf-8').read()
    kk1 = 'READ BACK : dated-arm-sweep returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the suites are repaired', 'the dated arms are cured',
               'this seat ruled the threshold', 'the detector decides'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gkk = kk1 and kk2 and kk3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (kk1, kk2, kk3))
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTREPAIRED')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock) ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, S, F, M))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    go = o1 and o2 and o3 and o4 and o5
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('        lock %s ; extract %s ; sweep %s ; ledger %s ; mint %s'
          % (stampm.group(1) if stampm else '?', E['run_clock'], S['run_clock'],
             F['run_clock'], M['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE ANY WRITE : %s'
          % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b366_hooks.txt'), d('b366_mirror.txt')
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
        ('suites %d' % S['suites'], ('%d GATE SUITES' % S['suites']) in bank),
        ('arms %d' % S['arms'], ('%d ARMS' % S['arms']) in bank),
        ('unattributed %d' % S['unattributed'], ('%d REGISTRATIONS' % S['unattributed']) in bank),
        ('flagged %d' % S['flagged'], ('%d, IN %d SUITES' % (S['flagged'], 7)) in bank),
        ('dated %d / substitution %d' % (S['dated'], S['one_substitution']),
         'THREE DATED ARMS' in bank and 'TWO OF THEM' in bank),
        ('precision %d of %d' % (S['dated'] + S['standing'], S['flagged']),
         ('%d OF %d' % (S['dated'] + S['standing'], S['flagged'])) in bank),
        ('the TECHNE head %s' % M['techne_head'], M['techne_head'] in bank),
        ('the commits ahead %s' % M['commits_ahead_of_origin'],
         ('%s COMMITS AHEAD' % M['commits_ahead_of_origin']) in bank),
        ('reads %d' % E['reads'], ('%d reads' % E['reads']) in bank),
        ('without an anchor %d' % E['without_anchor'],
         ('%d without an anchor' % E['without_anchor']) in bank),
        ('anchors differing %d of %d' % (E['anchors_differing'], E['reads']),
         ('%d of %d anchors differing' % (E['anchors_differing'], E['reads'])) in bf),
        ('ruling lines %d' % E['ruling_lines'], ('%d ruling lines' % E['ruling_lines']) in bank),
        ('(R3) lines %d' % E['r3_lines'], ('%d `(R3)` lines' % E['r3_lines']) in bank),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on sweep run file', S['run_file'] in bank),
        ('the relied-on ledger run file', F['run_file'] in bank),
        ('the relied-on mint run file', M['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks, never by name):')
    once = True
    for lbl, jf in (('extract', E), ('sweep', S), ('ledger', F), ('mint', M)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-8s %-26s clock on disk %s == the JSON's %s : %s"
              % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    repeats = sorted(f for f in os.listdir(D) if re.match(r'^b366_extract_notes\d*\.txt$', f))
    named = all(f in bank for f in repeats)
    once = once and named
    print('    ### **EVERY REPEAT IS NAMED IN THE BANK, SUPERSEDED OR RELIED ON : %s** %s' % (named, repeats))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed about the object, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    mymods = ('b366_regspec.py', 'b366_extract.py', 'b366_sweep.py', 'gate_content.py',
              'b366_faces_row.py', 'b366_mint.py', 'b366_correspondence.py',
              'b366_index_append.py', 'b366_checks.py')
    for p in [t(x) for x in mymods]:
        src3 = strip_prose(p)
        for b in banned:
            if b in src3:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b366_sweep.py', 'b366_extract.py',
                                                       'b366_mint.py', 'gate_content.py'))]
    gnc = not hits and not imports
    print("    numerical calls in this act's STRIPPED sources : %d %s" % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, FERRY, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
             d('b366_satisfiable.json'), d(E['run_file']), d(S['run_file']), d(F['run_file']),
             d(M['run_file']), t('b366_regspec.py'), t('b366_extract.py'), t('b366_sweep.py'),
             t('gate_content.py'), t('b366_faces_row.py'), t('b366_mint.py'),
             t('b366_correspondence.py'), t('b366_index_append.py')]
    CARRIERS = [
        (t('b366_checks.py'), 'its own fixtures'),
        (FERRY, "IT IS THE ORDER -- not this act's writing"),
        (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
        (d(E['run_file']), "the extract file carries other files' own words"),
        (SRC, 'A PINNED SOURCE -- its words are its own'),
    ]
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

    marker = '# ### THE DATED-ARM SWEEP (b366).'
    nxt = '# ### THE OWED READ, PAID (b365).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    fblk = faces.split('(b366): row U1')[-1] if '(b366): row U1' in faces else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the ledger block, the index row, the module, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', fblk),
                      ('the index row', ib2), ('the module', mtxt)):
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the ledger block, the index')
    print('  ### row and the module):')
    tmpdir = tempfile.mkdtemp(prefix='b366_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', fblk),
                      ('the index row', ib2), ('the module', mtxt)):
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
