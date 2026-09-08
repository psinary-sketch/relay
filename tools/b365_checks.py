# -*- coding: utf-8 -*-
"""b365_checks.py -- THE GATE SUITE FOR THE OWED READ, PAID.

### ### **THIS SUITE USES `gate_needle` (`b363`) AND `gate_text.flat` AND DEFINES NO FLATTENER OF ITS
### ### OWN**, and every `G-NO*`-shaped arm reads STRIPPED CODE or a marked region rather than raw prose --
### `b348`'s rule.
### ### **AND NO ARM HERE COMPARES A LINE NUMBER OF ANY FILE OUTSIDE THIS ACT** -- `b364`'s finding,
### applied the day after it was filed. ### Where an arm must know a source line, it reads it from THIS
### act's own JSON, which moves only if this act is re-run.
### ### **AND EVERY ARM WAS WRITTEN LABEL-FIRST**, under `b365`'s own module: the label was stated as a
### sentence and then the predicate was asked whether it decides that sentence. ### **THAT IS A HABIT AND
### ### NOT A TOOL, AND IT CAUGHT NOTHING BY ITSELF; IT IS RECORDED SO A LATER READER KNOWS WHAT WAS AND
### ### WAS NOT DONE.**
### ### **THE ARMS (locked registration section (F)):** ### `G-QUOTE`, `G-CONVENTION`, `G-CONSTANT`,
### `G-LEDGERPASS`, `G-BRANCH`, `G-SEPARATE`, `G-MINT`, `G-THRESHOLD`, `G-NOGRADE`, `G-NOFETCH`, `G-ROW`,
### `G-KEY` with `G-NOTMOVED`, `G-NOEDIT`, `G-ORDER`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, `G-NOCOMPUTE`,
### the struck-clause and stem sweeps, `G-SHARED`, the hedge audit, the must-fail fixtures.
### ### **THE SIDES, DECLARED BY `b352`'s RULE:** ### `G-NOEDIT`'s working-tree half and `G-ROW`'s and
### `G-MINT`'s ancestry readings are read BEFORE THE PUSH; `G-HOOK`/`G-MIRROR` AFTER THE PUSH; `G-ORDER`
### SIDE-INVARIANT.
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


BANK = d('b365_the_owed_read_paid.txt')
REG = d('b365_registration_2026-09-07.txt')
FERRY = d('b365_ferry_2026-09-07.txt')
SRC = d('b358_source_lagarias0404394.txt')
B358 = d('b358_the_li_asymptotics.txt')
B361 = d('b361_the_held_item.txt')
B360 = d('b360_the_fold.txt')
B362 = d('b362_the_approximation_register.txt')
B363 = d('b363_the_anchored_gate_arms.txt')
B363C = d('b363_closing.txt')
B364 = d('b364_the_copy_that_did_not_reproduce.txt')
CORR, IDX = d('b365_corr_run.txt'), d('b365_index_run.txt')
SCAN, TERMSCAN, GATE = d('b365_ferry_scan.txt'), d('b365_reg_termscan.txt'), d('b365_reg_gate.txt')
CENSUS0, FCEN = d('b365_census_stepzero.txt'), d('b365_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b365_regspec_run.txt'), d('audit_b365_reg_satisfiable.txt')
PINS = d('b365_pins_stepzero.txt')
SEAL = '76e113006dc17de3ec9b09d6dfc9f0f20f940c9d600694433ee7d691279f11f8'
ROWNUM = '214'
TRAIL_MARK = '<!-- b365 li cuspidality read paid -->'
PIN = '86f3d3c49f5a889f121bb1f04f67694cb9066dc8360f6988165788679594a4a7'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b365_reads.json'), ('R', 'b365_read.json'),
                   ('M', 'b365_mint.json'), ('F', 'b365_filing.json'))}

NEW_THIS_ACT = {'tools/b365_regspec.py', 'tools/b365_extract.py', 'tools/b365_read.py',
                'tools/b365_mint.py', 'tools/b365_filing.py', 'tools/b365_correspondence.py',
                'tools/b365_index_append.py', 'tools/b365_checks.py'}

TOOLNUM = [
    ('the convention, the constant and the ledger pass', 'tools/b365_read.py'),
    ('the 37 reads and the 16 source lines', 'tools/b365_extract.py'),
    ('the module and the threshold figures', 'tools/b365_mint.py'),
    ('the paid entry, and its 4553 bytes', 'tools/b365_filing.py'),
    ('the observed spans, counted from FINDINGS headings', 'tools/b363_span.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 214', 'tools/b365_correspondence.py'),
    ('the key', 'tools/b365_index_append.py'),
    ('51 clauses', 'tools/b365_regspec.py'),
    ('16553 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNED = [BANK, REG, FERRY, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
         d('b365_satisfiable.json'), d(_J['E']['run_file']), d(_J['R']['run_file']),
         d(_J['M']['run_file']), d(_J['F']['run_file']),
         t('b365_regspec.py'), t('b365_extract.py'), t('b365_read.py'), t('b365_mint.py'),
         t('b365_filing.py'), t('b365_correspondence.py'), t('b365_index_append.py')]

CARRIERS = [
    (t('b365_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (d(_J['E']['run_file']), "the extract file carries the source's own words"),
    (d(_J['R']['run_file']), "the reading file carries the source's own words"),
    (SRC, 'A PINNED SOURCE -- its words are its own'),
]

OWNER_NEEDLES = [
    ('the order -- the leg', FERRY, 'LEG 2 (b365) - THE OWED READ, PAID. The executor'),
    ('the order -- addition one, the question', FERRY,
     'ADDITION ONE - THE QUESTION, stated before the search: the'),
    ('the order -- the last answer at full prominence', FERRY,
     'not meet - the last at full prominence, since two acts stand on'),
    ('the order -- the circularity finding untouched', FERRY,
     'it. The circularity finding is untouched in every branch.'),
    ('the order -- addition two, the mint', FERRY, 'ADDITION TWO - THE MINT AND THE THRESHOLD. The wrong-arm'),
    ('the order -- no mechanizable half, and why', FERRY,
     'construction, because the needle checks the sentence and the'),
    ('the order -- the module, local-only, with A3 and A10', FERRY,
     'locally, not pushed, with A3 and A10 as its incidents. And the'),
    ('the order -- the threshold, ruled and not by this seat', FERRY,
     'and record that until it is ruled, "the fold is due" is a'),
    ("the order -- the navigator's expectation", FERRY,
     'meet, and the honest grade is IMPORTED-ON-A-HYPOTHESIS-NOT-MET'),
    ("the source -- the paper's own marked exception", SRC, 'representation, all other'),
    ('the source -- the convention itself', SRC, 'GL(1) we have e(0,π'),
    ('the source -- and why it is forced', SRC,
     'if we wish to have entire functions in all cases, for we must re move the poles at s = 0 and'),
    ('the source -- entire in all cases', SRC,
     'whose singularities are simple poles at s = 0, 1. It follows that'),
    ("the source -- Lemma 4.3's cuspidal hypothesis", SRC,
     'Lemma 4.3. For an irreducible cuspidal automorphic representation'),
    ('the source -- and the Remark applying it to the exception', SRC,
     'Remark. For the case πtriv on GL(1) Lemma 4.3 yields'),
    ("the source -- Theorem 5.1's own hypothesis", SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    ('the source -- the implied constant is absolute', SRC,
     'and the implied constant in the O-notation is absolute.'),
    ('the source -- and it evaluates the constant for the exception', SRC, 'C1(πtriv ) = 1'),
    ('b358 -- the grade it gave the hypothesis', B358, '`H-CUSP` (`π` cuspidal on `GL(N)`): the corpus'),
    ('b361 -- it inherits the grade and does not decide it', B361,
     '(i) IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT.'),
    ('A3 -- at its own bank', B360, 'FIRST VERSION DEMANDED A COMPONENT ORDER THIS ACT NEVER PROMISED'),
    ('A10 -- at its own bank', B362,
     'THE WRONG ARM ENTIRELY** -- a true-prefix test on a ledger whose new row is SPLICED INTO THE'),
    ('the sentence the rule is built on, at the bank that holds it', B360,
     'AN ARM THAT CANNOT PASS ON A CORRECT EDIT IS NOT A STRICTER ARM; IT IS THE WRONG ARM.** ### It was'),
    ('b363 -- no needle tool reaches it', B363, 'THE WRONG QUESTION**, and this act says that plainly'),
    ('b364 -- two more, live', B364, 'TWO OF THEM WERE THE WRONG ARM -- IN THE ACT THAT NAMED THE OTHER SPECIES'),
    ('b363 -- no threshold is declared anywhere in the record', B363C,
     'THERE IS NO DECLARED THRESHOLD ANYWHERE IN THE RECORD, AND THE TOOL SAYS SO RATHER THAN'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK,
     'THE CONVENTION IS LOCATED, AND THE SOURCE WORKS THE EXCEPTIONAL CASE ITSELF'),
    ('### the paper names a convention and says why it is forced', BANK,
     'IT NAMES A CONVENTION, CALLS'),
    ('### it carries the exception through its own results', BANK,
     'AND IT CARRIES THE EXCEPTION THROUGH ITS OWN CUSPIDAL-HYPOTHESIS RESULTS'),
    ('### a paper that computes a constant for a case applies the theorem to it', BANK,
     'A PAPER THAT COMPUTES A THEOREM'),
    ('### the negative answer on the ledger pass', BANK,
     'NO BANKED NUMBER OF THIS RECORD IS COMPUTED FROM THEOREM 5.1'),
    ('### the localization, supported with a stated constant', BANK,
     'SO THE ARCHIMEDEAN CHANNEL'),
    ('### and no grade moves, which the cap made absolute', BANK,
     'A READ THAT SUPPORTS A GRADE DOES NOT RAISE IT.**'),
    ('### the verdict on (i)', BANK, 'VERDICT ON (i): `LOCATED`.**'),
    ('### the verdict on (ii)', BANK, 'VERDICT ON (ii): DERIVED INDEPENDENTLY OF CUSPIDALITY.**'),
    ('### the pattern is systematic and explicit', BANK,
     'THE PAPER STATES ITS RESULTS FOR CUSPIDAL'),
    ('### the bounded pass reports what it read', BANK,
     'A PASS THAT REPORTS ONLY A CONCLUSION CANNOT BE CHECKED.**'),
    ('### the honest qualification, which is not a hedge', BANK,
     'AND THE HONEST QUALIFICATION, WHICH IS NOT A HEDGE:** ### Theorem 5.1'),
    ('### support by application, not by quantifier', BANK,
     'SO THE SUPPORT IS BY THE PAPER'),
    ('### the branch taken', BANK, 'TAKEN: `(LOCATED AND COVERS THE CASE)`.**'),
    ('### the trail entry PAID and the prior block not edited', BANK,
     'AND THE TRAIL ENTRY IS `PAID`, NOT RESTATED.**'),
    ('### the mint, local-only, and its rule', BANK,
     'ITS ONLY CURE IS A SECOND READER.**'),
    ('### the absence of a mechanized half is the content', BANK,
     'AND THE ABSENCE OF A MECHANIZED HALF IS THE MODULE'),
    ('### the sentence is banked at b360, not b362', BANK,
     'AND THE SENTENCE THE RULE IS BUILT ON IS BANKED AT `b360`, NOT AT `b362`.**'),
    ('### the threshold proposed', BANK, 'THE NUMBER PROPOSED TO THE AUTHOR: 9 ACTS.**'),
    ('### and the spread is the argument against it', BANK,
     'A HABIT THAT VARIES BY A FACTOR OF FOUR IS NOT A RULE THAT WAS BEING FOLLOWED.**'),
    ('### until it is ruled, the fold is due is a judgement', BANK,
     'AND UNTIL IT IS RULED, `THE FOLD IS DUE` IS A JUDGEMENT AND THE RECORD SAYS SO.**'),
    ('### the rendering seam, sharpened for this act', BANK,
     'IF THE RENDERING DROPPED OR MANGLED A QUALIFYING CLAUSE, THIS ACT WOULD NOT SEE IT.**'),
    ('### the placeholder species, a fourth and fifth time', BANK,
     'THE UNFORMATTED PLACEHOLDER, A FOURTH TIME, AND THEN A FIFTH.**'),
    ('### four hints typed from sense rather than the file', BANK,
     'FOUR HINTS TYPED FROM SENSE RATHER THAN FROM THE FILE.**'),
    ('### the pre-lock grep, declared on the locked face', BANK,
     'THE PRE-LOCK `grep`, AND IT IS DECLARED ON THE LOCKED FACE RATHER THAN HERE.**'),
    ("### the navigator's expectation refuted in its first clause", BANK,
     'REFUTED, AND IN ITS FIRST CLAUSE.**'),
    # ### **`A THEOREM` MATCHED THREE LINES AND THE HELPER REFUSED RATHER THAN CHOOSING**, which is what
    # ### it is for. ### The hint now carries the whole sentence.
    ("### and the lesson that makes the refutation useful", BANK,
     "A THEOREM'S SCOPE IS WHAT ITS PAPER DOES WITH IT, NOT ONLY WHAT ITS QUANTIFIER SAYS.**"),
    ("### this seat's half met and half refuted", BANK,
     'HALF MET AND HALF REFUTED, AND THE REFUTED HALF IS THE HALF THAT MATTERED'),
    ('### no proof is verified', BANK, 'A LOCATED STATEMENT IS NOT A PROVED ONE.**'),
]

MUST_FAIL = [
    ('the bank never says the grade is moved', BANK, '### THE GRADE IS MOVED.'),
    ('the bank never says the theorem is corrected', BANK, '### THE THEOREM IS CORRECTED.'),
    ('the bank never says the threshold is ruled', BANK, '### THE THRESHOLD IS RULED.'),
    ('the bank never says the wrong arm is mechanized', BANK, '### THE WRONG ARM IS MECHANIZED.'),
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
    print('b365 -- GATE SUITE (THE OWED READ, PAID)')
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
    E, R, M, F = _J['E'], _J['R'], _J['M'], _J['F']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    readrun = io.open(d(R['run_file']), encoding='utf-8', errors='replace').read()

    print(chr(10) + '  G-QUOTE (every source statement located by the anchor tool; none retyped):')
    q1 = E['without_anchor'] == 0 and E['reads'] > 0
    q2 = E['source_lines'] >= 16
    q3 = 'A PARAPHRASED' not in bf and 'appears in the extract before it appears in an argument' in ' '.join(
        io.open(t('b365_extract.py'), encoding='utf-8').read().split())
    q4 = 'A HASH ON A PDF DOES NOT CERTIFY' in bf
    gq = q1 and q2 and q4
    print('    %d reads, 0 without an anchor : %s ; source lines located : %d' % (E['reads'], q1, E['source_lines']))
    print('    the extract states the bar it runs under : %s' % q3)
    print('    ### **AND THE RENDERING SEAM IS ON THE BANK\'S FACE** : %s' % q4)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTE')

    print(chr(10) + '  G-CONVENTION ((i): LOCATED / CONTRADICTED / NOT LOCATED, with the quotation):')
    c1 = R['convention'] in ('LOCATED', 'CONTRADICTED', 'NOT LOCATED')
    c2 = 'This convention is forced' in bank
    # ### **THE BANK WRAPS THE QUOTATION ACROSS TWO MARKED LINES**, so the raw text does not carry the
    # ### phrase and the FLATTENED text does. ### The first version of this sub-arm read `bank`; that is
    # ### the needle-wrapping species in this act's own suite, and the cure is the flattener the record
    # ### already owns.
    c3 = 'an entire function in all cases' in bf
    c4 = 'VERDICT ON (i): `LOCATED`' in bank
    # ### **AND THE FIRST VERSION OF THIS ONE TYPED A RENDERING** -- `CONTRADICTED -- UNREACHABLE` --
    # ### that the bank never promised; the bank names both forms in one sentence and calls them
    # ### unreachable together, which is what the registration asked for.
    # ### **AND THE SECOND VERSION TYPED THE CASE**: it asked for `ARE ### **UNREACHABLE**` where the
    # ### bank writes `are`. ### Read the flattened bank for the sentence the bank actually carries.
    c5 = ('`CONTRADICTED` and `NOT LOCATED` -- are' in bf) and ('UNREACHABLE' in bf)
    gc = c1 and c2 and c3 and c4 and c5
    print('    the status is one of the three fixed forms : %s (%r)' % (c1, R['convention']))
    print("    the convention is quoted : %s ; and its consequence : %s" % (c2, c3))
    print('    the bank states the verdict : %s ; the other two shown unreachable : %s' % (c4, c5))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CONVENTION')

    print(chr(10) + '  G-CONSTANT ((ii): derived independently, and evaluated for the exception):')
    k1 = 'the implied constant in the O-notation is absolute' in bank
    k2 = 'C1(πtriv )' in bank
    k3 = 'Q(πtriv) = 1' in bank
    k4 = 'DERIVED INDEPENDENTLY OF CUSPIDALITY' in bf
    gk = k1 and k2 and k3 and k4
    print('    the absolute implied constant is quoted : %s' % k1)
    print("    ### **AND THE PAPER'S OWN EVALUATION FOR THE EXCEPTION IS QUOTED** : %s / %s" % (k2, k3))
    print('    and the verdict is stated : %s' % k4)
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-CONSTANT')

    print(chr(10) + '  G-LEDGERPASS ((iii): bounded, and it reports the blocks it examined):')
    l1 = len(R['faces_blocks']) > 0 and R['faces_headings'] > 0
    l2 = all(b['rows'] for b in R['faces_blocks'])
    l3 = R['banked_numbers_resting_on_the_constant'] == 0
    l4 = all(str(b['line']) in bank for b in R['faces_blocks'])
    l5 = 'NO BANKED NUMBER OF THIS RECORD IS COMPUTED FROM THEOREM' in bf
    gl = l1 and l2 and l3 and l4 and l5
    print('    %d of %d ledger blocks cite b358 or b361 : %s ; each names its row : %s'
          % (len(R['faces_blocks']), R['faces_headings'], l1, l2))
    print('    ### **EVERY BLOCK EXAMINED IS NAMED IN THE BANK BY ITS OWN LINE** : %s' % l4)
    print('    and the negative answer is stated : %s' % l5)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LEDGERPASS')

    print(chr(10) + '  G-BRANCH (one of three, and the others shown unreachable):')
    b1 = R['branch'] == 'LOCATED AND COVERS THE CASE'
    b2 = ('TAKEN: `(%s)`' % R['branch']) in bank
    b3 = 'LOCATED AND DOES NOT COVER THE CASE)` -- UNREACHABLE' in bank
    b4 = '(`NOT LOCATED`)` -- UNREACHABLE' in bank or '`(NOT LOCATED)` -- UNREACHABLE' in bank
    b5 = ('BRANCH, FIXED BEFORE THE READ' in gate_text.flat(reg))
    gb = b1 and b2 and b3 and b4 and b5
    print('    the branch taken : %r ; named in the bank : %s' % (R['branch'], b2))
    print('    the other two shown unreachable : %s / %s' % (b3, b4))
    print('    and the branches were fixed on the locked face : %s' % b5)
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BRANCH')

    print(chr(10) + '  G-SEPARATE (BAR 2: what the source states and what this record concludes, apart):')
    s1 = 'THE FIRST QUOTED, THE SECOND ARGUED' in bf
    s2 = 'A FACT ABOUT THE PAPER' in bf and 'A JUDGEMENT ABOUT THIS RECORD' in bf
    s3 = 'THE FIRST QUOTED, THE SECOND ARGUED' in gate_text.flat(readrun) or \
         'THE FIRST QUOTED, THE SECOND ARGUED' in readrun
    s4 = 'IT KEEPS A JUDGEMENT FROM WEARING A QUOTATION' in gate_text.flat(reg)
    gs = s1 and s2 and s3 and s4
    print('    the bank marks the two apart : %s ; and names them : %s' % (s1, s2))
    print('    the reading run marks them apart too : %s ; the bar is on the locked face : %s' % (s3, s4))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SEPARATE')

    print(chr(10) + '  G-MINT (a judgement rule with NO mechanizable half; local-only) ### READ BEFORE THE PUSH:')
    modpath = os.path.join(TC, M['module'].replace('/', os.sep))
    mtxt = io.open(modpath, encoding='utf-8', errors='replace').read() if os.path.exists(modpath) else ''
    m1 = M['module_ok'] is True and os.path.exists(modpath)
    m2 = 'NO MECHANIZABLE HALF' in mtxt and 'it ships no arm' in mtxt.lower()
    m3 = M['pushed'] is False and int(M['commits_ahead_of_origin'] or 0) > 0
    m4 = all(v['equal'] for v in M['quotes'].values())
    m5 = 'A3' in mtxt and 'A10' in mtxt
    tcstat = git(TC, 'status', '--porcelain').strip()
    m6 = not tcstat
    gm = m1 and m2 and m3 and m4 and m5 and m6
    print('    the module exists and holds its own claims : %s ; no mechanizable half, ships no arm : %s'
          % (m1, m2))
    print('    ### **LOCAL ONLY: %s COMMITS AHEAD OF origin/main, PUSHED : %s**'
          % (M['commits_ahead_of_origin'], M['pushed']))
    print('    every incident quotation equal under the shared normaliser : %s ; A3 and A10 named : %s'
          % (m4, m5))
    print('    TECHNE-Core working tree clean : %s' % m6)
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MINT')

    print(chr(10) + '  G-THRESHOLD (proposed, with the observed spans, and NOT ruled):')
    h1 = M['threshold_ruled'] is False
    h2 = ('THE NUMBER PROPOSED TO THE AUTHOR: %d ACTS' % M['threshold_proposed']) in bank
    h3 = all(str(x) in bank for x in (M['shortest'], M['longest'], M['middle']))
    h4 = 'IT IS FIXED BY RULING AND NOT BY THIS SEAT' in bf
    h5 = 'IS A JUDGEMENT AND THE RECORD SAYS SO' in bf
    h6 = len(M['spans']) == M['folds_run']
    gh = h1 and h2 and h3 and h4 and h5 and h6
    print('    the proposal is %d acts and is NOT ruled : %s / %s' % (M['threshold_proposed'], h2, h1))
    print('    the shortest, longest and middle are all in the bank : %s ; %d spans counted : %s'
          % (h3, len(M['spans']), h6))
    print('    ### **FIXED BY RULING AND NOT BY THIS SEAT** : %s' % h4)
    print('    ### **AND UNTIL IT IS RULED, THE FOLD IS DUE IS A JUDGEMENT** : %s' % h5)
    print('    %s' % ('PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-THRESHOLD')

    print(chr(10) + '  G-NOGRADE (no grade moves in either direction; nothing promoted):')
    n1 = R['grade_moved'] is False and F['grade_moved'] is False and F['face_promoted'] is False
    n2 = 'A READ THAT SUPPORTS A GRADE DOES NOT RAISE IT' in bf
    n3 = 'NO GRADE MOVES IN EITHER DIRECTION' in bf
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    n4 = faces_clean
    n5 = R['circularity_finding'] == 'UNTOUCHED' and 'CIRCULARITY FINDING IS UNTOUCHED' in bf
    gn = n1 and n2 and n3 and n4 and n5
    print('    the act records no grade moved and no face promoted : %s' % n1)
    print('    the bank says a supporting read does not raise a grade : %s ; and says it plainly : %s'
          % (n2, n3))
    print('    ### **FACES_LEDGER.md UNTOUCHED, BECAUSE NO ROW MOVED** : %s' % n4)
    print("    b358's circularity finding untouched : %s" % n5)
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOGRADE')

    print(chr(10) + '  G-NOFETCH (no source fetched; the pinned rendering is the only text read):')
    f1 = R['source_refetched'] is False and R['source_pin'] == PIN
    src2 = strip_prose(t('b365_read.py')) + strip_prose(t('b365_extract.py'))
    f2 = not any(w in src2 for w in ('urllib', 'requests', 'urlopen', 'http://', 'https://'))
    f3 = PIN in bank
    gf2 = f1 and f2 and f3
    print('    the act records no re-fetch, and the pin matches : %s' % f1)
    print("    ### **NO NETWORK CALL IN THIS ACT'S STRIPPED READING SOURCES** : %s" % f2)
    print('    and the pin is on the bank : %s' % f3)
    print('    %s' % ('PASS' if gf2 else '### FAIL ###'))
    if not gf2:
        fails.append('G-NOFETCH')

    print(chr(10) + '  G-NOEDIT (no owner instrument; no other act’s files; only this act’s papers path) '
          '### the working-tree half READ BEFORE THE PUSH:')
    owner = ['tools/e16/b264_eps_decay.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py',
             'tools/anchor_from_file.py', 'tools/quote_norm.py', 'tools/ferry_scan.py',
             'tools/gate_needle.py', 'tools/b327_faces_row.py', 'tools/mirror_roster.json',
             'tools/mirror_verify.py', 'tools/b363_span.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').splitlines()
              if x.strip() and 'b365' not in x and x.strip() != 'tools/banked_index.py']
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'OPEN_TRAILS.md']
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    gne = (not touched and not others and not ppbad and hand and dep and fnd)
    print('    owner instruments modified : %s' % (touched or 'none'))
    print("    ### **TRACKED RELAY FILES OF OTHER ACTS MODIFIED : %s**" % (others or 'none'))
    print('    papers paths beyond OPEN_TRAILS.md : %s' % (ppbad or 'none'))
    print('    HANDOFF clean : %s ; the deposited monograph clean : %s ; FINDINGS clean : %s'
          % (hand, dep, fnd))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason) ### READ BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'A READ IS NOT A RESULT' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-TRAILPAID (the entry named PAID; the block b363 wrote NOT edited) ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    p1 = trails.count(TRAIL_MARK) == 1
    p2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    p3 = F['prefix_of_file'] and F['prefix_of_blob'] and F['names_prior_entry']
    p4 = F['status'] == 'PAID' and ('`%s` — PAID' % F['entry']) in trails
    p5 = trails.count('<!-- b363 li cuspidality read -->') == 1
    gtp = p1 and p2 and p3 and p4 and p5
    print('    the new mark appears once : %s ; the blob is a true prefix : %s' % (p1, p2))
    print('    the block names the prior entry and is append-only : %s ; marked %s : %s'
          % (p3, F['status'], p4))
    print("    ### **AND b363's OWN BLOCK IS STILL THERE, EXACTLY ONCE, UNEDITED** : %s" % p5)
    print('    %s' % ('PASS' if gtp else '### FAIL ###'))
    if not gtp:
        fails.append('G-TRAILPAID')

    print(chr(10) + '  G-KEY / G-NOTMOVED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1b = 'READ BACK : cuspidality-convention returns 1 row(s)' in irun
    k2b = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the grade is moved', 'the theorem is corrected',
               'the hypothesis covers zeta', 'the threshold is ruled'))
    k3b = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gkk = k1b and k2b and k3b
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (k1b, k2b, k3b))
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTMOVED')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock) ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, R, M, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE THE READ' in gate_text.flat(reg)
    go = o1 and o2 and o3 and o4 and o5
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('        lock %s ; extract %s ; read %s ; mint %s ; filing %s'
          % (stampm.group(1) if stampm else '?', E['run_clock'], R['run_clock'],
             M['run_clock'], F['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE THE READ : %s' % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b365_hooks.txt'), d('b365_mirror.txt')
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
        ('reads %d' % E['reads'], ('%d reads' % E['reads']) in bank),
        ('without an anchor %d' % E['without_anchor'],
         ('%d without an anchor' % E['without_anchor']) in bank),
        ('anchors differing %d of %d' % (E['anchors_differing'], E['reads']),
         ('%d of %d anchors differing' % (E['anchors_differing'], E['reads'])) in bf),
        ('source lines %d' % E['source_lines'], ('%d SOURCE LINES' % E['source_lines']) in bank),
        ('ledger blocks %d of %d' % (len(R['faces_blocks']), R['faces_headings']),
         ('`%d` blocks' % R['faces_headings']) in bank),
        ('every ledger block line named', all(('`%d`' % b['line']) in bank for b in R['faces_blocks'])),
        ('the filing grew the file by %d bytes' % F['grew'], str(F['grew']) in bank),
        ('the TECHNE head %s' % M['techne_head'], M['techne_head'] in bank),
        ('the commits ahead %s' % M['commits_ahead_of_origin'],
         ('%s COMMITS AHEAD' % M['commits_ahead_of_origin']) in bank),
        ('the threshold %d' % M['threshold_proposed'], str(M['threshold_proposed']) in bank),
        ('the spread %d to %d' % (M['shortest'], M['longest']),
         ('`%d` TO `%d`' % (M['shortest'], M['longest'])) in bank),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the source pin', PIN in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on read run file', R['run_file'] in bank),
        ('the relied-on mint run file', M['run_file'] in bank),
        ('the relied-on filing run file', F['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks, never by name):')
    once = True
    for lbl, jf in (('extract', E), ('read', R), ('mint', M), ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-8s %-26s clock on disk %s == the JSON's %s : %s"
              % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    repeats = sorted(f for f in os.listdir(D)
                     if re.match(r'^b365_(extract_notes|read_run)\d*\.txt$', f))
    named = all(f in bank for f in repeats)
    once = once and named
    print('    ### **EVERY REPEAT IS NAMED IN THE BANK, SUPERSEDED OR RELIED ON : %s** %s' % (named, repeats))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed about the object, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    mine = ('b365_regspec.py', 'b365_extract.py', 'b365_read.py', 'b365_mint.py', 'b365_filing.py',
            'b365_correspondence.py', 'b365_index_append.py', 'b365_checks.py')
    for p in [t(x) for x in mine]:
        src3 = strip_prose(p)
        for b in banned:
            if b in src3:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b365_read.py', 'b365_extract.py',
                                                       'b365_mint.py', 'b365_filing.py'))]
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

    marker = '# ### THE OWED READ, PAID (b365).'
    nxt = '# ### THE COPY THAT DID NOT REPRODUCE, DIAGNOSED AND NOT REPAIRED (b364).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    blk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row, the module, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk),
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the trail block, the index row,')
    print('  ### and the module):')
    tmpdir = tempfile.mkdtemp(prefix='b365_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk),
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
