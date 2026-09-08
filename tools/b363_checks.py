# -*- coding: utf-8 -*-
"""b363_checks.py -- THE GATE SUITE FOR THE ANCHORED GATE ARMS.

### ### **THIS SUITE IS THE FIRST CONSUMER OF `tools/gate_needle.py`**, which is the helper this act built.
### ### **THAT IS A DEMONSTRATION AND IT IS NOT EVIDENCE ABOUT THE HELPER'S REACH.** ### The reach was
### measured by the census over eleven arms in three banks; a suite passing its own needles proves only
### that this suite's needles were built from files rather than typed.
### ### **AND THE HELPER DOES NOT CHANGE WHAT ANY ARM ASKS.** ### `G-CLASSIFY` and `G-CONTROL` would fail
### exactly as loudly with the helper as without it, because their predicates are about counts.
### ### **THIS SUITE USES `gate_text.flat` AND DEFINES NO FLATTENER OF ITS OWN**, and every `G-NO*`-shaped
### arm reads STRIPPED CODE or a marked region rather than raw prose -- `b348`'s rule.
### ### **THE ARMS (locked registration section (G)):** ### `G-COUNT`, `G-CLASSIFY`, `G-REACH`,
### `G-FIXTURE`, `G-CONTROL`, `G-NOEDIT`, `G-TRAIL`, `G-ROW`, `G-KEY` with `G-NOTCURED`, `G-ORDER`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, `G-NOCOMPUTE`, the struck-clause and stem sweeps, `G-SHARED`, the
### hedge audit, the must-fail fixtures. ### Re-run after the push.
### ### **THE SIDES, DECLARED BY `b352`'s RULE:** ### `G-NOEDIT`'s working-tree half and `G-TRAIL`'s and
### `G-ROW`'s ancestry readings are read BEFORE THE PUSH; `G-HOOK` and `G-MIRROR` AFTER THE PUSH;
### `G-ORDER` SIDE-INVARIANT.
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
import gate_needle as GN  # noqa: E402  ### THE HELPER THIS ACT BUILT, USED HERE FOR THE FIRST TIME

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b363_the_anchored_gate_arms.txt')
REG = d('b363_registration_2026-09-07.txt')
FERRY = d('b363_ferry_2026-09-07.txt')
DRAFT = d('b362_closing.txt')
B360, B361, B362 = d('b360_the_fold.txt'), d('b361_the_held_item.txt'), d('b362_the_approximation_register.txt')
B358 = d('b358_the_li_asymptotics.txt')
SRC = d('b358_source_lagarias0404394.txt')
CORR, IDX = d('b363_corr_run.txt'), d('b363_index_run.txt')
SCAN, TERMSCAN, GATE = d('b363_ferry_scan.txt'), d('b363_reg_termscan.txt'), d('b363_reg_gate.txt')
CENSUS0, FCEN = d('b363_census_stepzero.txt'), d('b363_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b363_regspec_run.txt'), d('audit_b363_reg_satisfiable.txt')
PINS = d('b363_pins_stepzero.txt')
SEAL = '6b80dfea957c4a877b6e6d8cf355170975e9181aa5df93b7ebf3401d38d48eb8'
ROWNUM = '212'
TRAIL_MARK = '<!-- b363 li cuspidality read -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b363_reads.json'), ('N', 'b363_census.json'), ('T', 'b363_trail.json'))}

NEW_THIS_ACT = {'tools/gate_needle.py', 'tools/b363_regspec.py', 'tools/b363_extract.py',
                'tools/b363_census.py', 'tools/b363_trail.py', 'tools/b363_correspondence.py',
                'tools/b363_index_append.py', 'tools/b363_checks.py'}

TOOLNUM = [
    ('the helper, and its seven fixtures', 'tools/gate_needle.py'),
    ('11 / 11 / 7 / 4, and the 152 needles', 'tools/b363_census.py'),
    ('the 28 reads and the 20 differing anchors', 'tools/b363_extract.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the shared normaliser both sides pass through', 'tools/quote_norm.py'),
    ('W-ORD-LI-CUSP, and the 4797 bytes', 'tools/b363_trail.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 212', 'tools/b363_correspondence.py'),
    ('the key', 'tools/b363_index_append.py'),
    ('48 clauses', 'tools/b363_regspec.py'),
    ('16623 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

# ### **THE SUITES THIS ACT COPIED AND RAN.** ### `G-NOEDIT` proves each is byte-identical to its blob.
BANKED_SUITES = ['tools/b355_checks.py', 'tools/b356_checks.py', 'tools/b357_checks.py',
                 'tools/b360_checks.py', 'tools/b361_checks.py', 'tools/b362_checks.py']

OWNED = [BANK, REG, FERRY, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
         d('b363_satisfiable.json'), d(_J['E']['run_file']), d(_J['N']['run_file']),
         d(_J['T']['run_file']),
         t('gate_needle.py'), t('b363_regspec.py'), t('b363_extract.py'), t('b363_census.py'),
         t('b363_trail.py'), t('b363_correspondence.py'), t('b363_index_append.py')]

CARRIERS = [
    (t('b363_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (d(_J['E']['run_file']), "the extract file carries three other acts' own words"),
    (SRC, 'A PINNED SOURCE -- its words are its own'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b363 — THE ANCHORED GATE ARMS. The executor'),
    ('the order -- addition one, the count', FERRY, 'ADDITION ONE — THE EVIDENCE IS THE ACT'),
    ('the order -- addition two, the control', FERRY,
     'ADDITION TWO — THE CONTROL IS THE BANKED SUITES, UNEDITED: the'),
    ('the order -- addition three, the owed read', FERRY,
     'ADDITION THREE — THE OWED READ IS FILED, NOT RUN: a trail entry'),
    ('the order -- the fourth species is untouched by any needle tool', FERRY,
     'tool, and the act says plainly that the helper does not reach'),
    ("the order -- the navigator's expectation", FERRY,
     'fewer arms than the draft estimates, because at least one of'),
    ('the order -- the next draft, counted and not typed', FERRY, 'onward when the span reaches the fold'),
    ("the draft -- its own population figure", DRAFT, 'NINE ARMS THAT FIRED ON THEIR OWN ACTS'),
    ("the draft -- its own retirement estimate", DRAFT,
     'census of thirteen incidents should convert to a cure covering nine or ten'),
    ('b360 -- its own headline figure', B360, '(E7) FOUR ARMS OF THIS ACT'),
    ('b361 -- its own headline figure', B361, '(E4) TWO ARMS OF THIS ACT'),
    ('b362 -- its own headline figure', B362, '(E5) FIVE ARMS OF THIS ACT'),
    ('b362 -- the wrong arm, in its own act’s words', B362,
     'THE WRONG ARM ENTIRELY** -- a true-prefix test on a ledger whose new row is SPLICED INTO THE'),
    ('b361 -- the missing sentence, in its own act’s words', B361,
     'and `G-NUMBERS` asked for the correspondence row'),
    ('the trail -- b358 grades the hypothesis', B358, '`H-CUSP` (`π` cuspidal on `GL(N)`): the corpus'),
    ('the trail -- b361 inherits it and does not decide it', B361,
     '(i) IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT.'),
    ("the trail -- the theorem's own hypothesis, at the pinned source", SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK,
     'THE HELPER IS BUILT AND IT IS NARROWER THAN THE RULE IT WAS PROPOSED UNDER'),
    ('### the draft refuted in its input as well as its output', BANK,
     'AND THE DRAFT IS REFUTED IN ITS INPUT AS WELL AS IN ITS OUTPUT'),
    ('### the survivors split into two kinds, not one', BANK,
     'AND THE FOUR THAT ARE NOT RETIRED SPLIT INTO TWO KINDS, NOT ONE'),
    ('### a helper that quietened a right arm would be a defect', BANK,
     'A HELPER THAT MADE EITHER OF THEM QUIET WOULD BE A DEFECT'),
    ("### the navigator's expectation met, and met twice over", BANK, 'SO THE NAVIGATOR'),
    ('### the control held five of six', BANK,
     'AND THE CONTROL HELD FIVE TIMES OUT OF SIX, WITH THE SIXTH REPORTED'),
    ("### the helper's shape in one sentence", BANK, 'A HINT IS TYPED; THE FILE'),
    ('### the helper does not reach a wrong arm', BANK, 'IT DOES NOT REACH A WRONG ARM'),
    ('### seven fixtures, both polarities', BANK, 'SEVEN FIXTURES, BOTH POLARITIES, ALL PASS'),
    ('### the headline sum', BANK, 'FOUR PLUS TWO PLUS FIVE IS ELEVEN'),
    ('### the census refuses to emit on a disagreement', BANK,
     'THE TOOL REFUSES TO EMIT IF THE TWO DISAGREE'),
    ('### arms and not lines', BANK, 'THE CENSUS COUNTS ARMS AND NOT LINES'),
    ('### why the classification is declared and not inferred', BANK,
     'SCANNER THAT INFERS A JUDGEMENT FROM PROSE IS A CHECK THAT CAN CONFIRM'),
    ('### the retirement count', BANK, 'RETIRED BY THE HELPER : 7'),
    ("### the draft's input figure was a count it could have made", BANK,
     'THE INPUT FIGURE WAS A COUNT THE DRAFT COULD HAVE MADE AND DID NOT'),
    ('### the fourth species, named', BANK,
     'THE WRONG ARM -- AN ARM WHOSE PREDICATE TESTS SOMETHING OTHER THAN WHAT ITS LABEL SAYS'),
    ('### and no needle tool reaches it', BANK, 'THE WRONG QUESTION**, and this act says that plainly'),
    ("### the control's one exception, reported not adjusted", BANK, 'REPORTED, NOT ADJUSTED'),
    ('### the exercise figure', BANK, '152 NEEDLES DECLARED, 152 BUILT, 0 REFUSED'),
    ('### the trail filed and not performed', BANK,
     'NAMING A READ IS NOT PERFORMING ONE, AND THIS ACT PERFORMED NONE OF IT'),
    ('### the ledger NOT written, because no row moved', BANK,
     'NO FACE IS PROMOTED AND NO LEDGER ROW MOVED'),
    ("### this act's own species, committed by its own tool", BANK,
     'AN ABSENCE THAT WAS NOT THERE, PRODUCED BY A NAME TYPED RATHER'),
    ('### and the same species one layer down', BANK,
     'A SECOND ABSENCE THAT WAS NOT THERE, ONE LAYER DOWN'),
    ('### the heredoc, a fourth time, in a new shape', BANK, 'CAUGHT BY AN `ls`'),
    ('### the expectation met, and worth very little', BANK,
     'ALL THREE MET -- AND THAT IS WORTH VERY LITTLE'),
    ('### the branch taken', BANK, 'TAKEN: (BUILT AND FOUND NARROWER THAN ITS RULE)'),
    ('### and the branches shown unreachable', BANK, 'UNAFFORDABLE) -- UNREACHABLE'),
    ('### what the helper is not claimed to do', BANK,
     'It says nothing about whether any gate asks the right question'),
    ('### 7 of 11 is not a rate and not a forecast', BANK, 'IS NOT A RATE AND NOT A FORECAST'),
]

MUST_FAIL = [
    ('the bank never says the wrong arm is cured', BANK, '### THE WRONG ARM IS CURED.'),
    ('the bank never says every arm is retired', BANK, '### EVERY ARM IS RETIRED.'),
    ('the bank never says a banked suite was edited', BANK, '### A BANKED SUITE WAS EDITED.'),
    ('the bank never says a sharper instrument is a result', BANK,
     '### A SHARPER INSTRUMENT IS A RESULT.'),
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
    print('b363 -- GATE SUITE (THE ANCHORED GATE ARMS)')
    print('=' * 100)
    extract = io.open(d(_J['E']['run_file']), encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
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
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES ### BUILT BY `gate_needle` FROM THIS ACT’S OWN BANK:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            unpullable += 1
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
    E, N, T = _J['E'], _J['N'], _J['T']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    cen = io.open(d(N['run_file']), encoding='utf-8', errors='replace').read()

    print(chr(10) + '  G-COUNT (the population counted TWICE and the two halves made to agree):')
    c1 = N['headline_sum'] == N['enumerated'] and N['agree'] is True
    c2 = N['enumerated'] == len(N['arms'])
    c3 = ('REFUSES TO EMIT IF THE ENUMERATION AND THE HEADLINES DISAGREE'
          in gate_text.flat(io.open(t('b363_census.py'), encoding='utf-8').read()))
    c4 = E['without_anchor'] == 0 and E['population_lines'] > 0
    c5 = N['enumerated'] != N['draft_population']
    gc = c1 and c2 and c3 and c4 and c5
    print('    headline sum %d == enumerated %d, and the tool says they agree : %s'
          % (N['headline_sum'], N['enumerated'], c1))
    print('    the enumeration has as many entries as it counts : %s' % c2)
    print('    ### **THE TOOL REFUSES TO EMIT IF THE TWO DISAGREE** (in its own source) : %s' % c3)
    print('    every population line located by the anchor tool, 0 without an anchor : %s' % c4)
    print("    ### and the count is NOT the draft's figure (%d vs %d) : %s"
          % (N['enumerated'], N['draft_population'], c5))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-COUNT')

    print(chr(10) + '  G-CLASSIFY (two values only; the partition closes; the two kinds kept apart):')
    vals = sorted(set(a['classification'] for a in N['arms'])) if N['arms'] else []
    k1 = N['retired'] + N['not_retired'] == N['enumerated']
    k2 = len(vals) <= 2 and all(v in ('RETIRED BY THE HELPER', 'NOT RETIRED') for v in vals)
    k3 = len(N['wrong_arms']) + len(N['missing_sentences']) == N['not_retired']
    k4 = not (set(N['wrong_arms']) & set(N['missing_sentences']))
    k5 = 'THE CLASSIFICATION IS' in gate_text.flat(reg) and 'DECLARED DATA' in gate_text.flat(reg)
    gcl = k1 and k2 and k3 and k4 and k5
    print('    retired %d + not retired %d == %d : %s' % (N['retired'], N['not_retired'], N['enumerated'], k1))
    print('    exactly the two declared values are used : %s %s' % (k2, vals))
    print('    ### **THE SURVIVORS PARTITION: %d WRONG ARMS %s + %d MISSING SENTENCES %s = %d** : %s'
          % (len(N['wrong_arms']), N['wrong_arms'], len(N['missing_sentences']), N['missing_sentences'],
             N['not_retired'], k3))
    print('    and no arm is in both kinds : %s ; the locked face fixed the two values : %s' % (k4, k5))
    print('    %s' % ('PASS' if gcl else '### FAIL ###'))
    if not gcl:
        fails.append('G-CLASSIFY')

    print(chr(10) + '  G-REACH (the helper’s limits are stated, and the wrong arm is named as OUT OF REACH):')
    hsrc = io.open(t('gate_needle.py'), encoding='utf-8').read()
    r1 = 'DOES NOT REACH A WRONG ARM' in gate_text.flat(hsrc)
    r2 = 'DOES NOT REACH A MISSING SENTENCE' in gate_text.flat(hsrc)
    r3 = 'IT DOES NOT REACH A WRONG ARM' in bf
    r4 = 'A NEEDLE BUILT FROM A FILE IS STILL A NEEDLE FOR THE WRONG QUESTION' in bf
    r5 = N['retired'] < N['enumerated']
    gr = r1 and r2 and r3 and r4 and r5
    print("    the helper's own header states it does not reach a wrong arm : %s" % r1)
    print('    ### nor a missing sentence : %s' % r2)
    print('    the bank says both in its own words : %s / %s' % (r3, r4))
    print('    ### **AND THE CENSUS PUTS THE REACH BELOW THE POPULATION (%d < %d)** : %s'
          % (N['retired'], N['enumerated'], r5))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-REACH')

    print(chr(10) + '  G-FIXTURE (the helper holds its own fixtures, BOTH POLARITIES, re-run here):')
    f1 = GN.self_test(False)
    f2 = 'an arm whose sentence is ABSENT still FIRES' in hsrc
    f3 = 'a DROPPED POSSESSIVE is still a MISS' in hsrc
    f4 = GN.absent_exact(t('gate_needle.py'), '### THE HELPER IS COMPLETE.')
    gf = f1 and f2 and f3 and f4
    print('    every fixture passes on a fresh run : %s' % f1)
    print('    ### **THE POSITIVE POLARITY INCLUDES AN ARM THAT SHOULD FIRE AND STILL DOES** : %s' % f2)
    print('    ### and a changed word is still a MISS : %s' % f3)
    print('    and the helper claims no completeness : %s' % f4)
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FIXTURE')

    print(chr(10) + '  G-CONTROL (six banked suites copied and run; the one that does not reproduce is NAMED):')
    n1 = N['copies'] == len(BANKED_SUITES)
    n2 = N['copies_reproducing'] <= N['copies']
    ctl = N['control'] if isinstance(N.get('control'), list) else []
    n3 = len(ctl) == N['copies']
    bad = [c for c in ctl if not c.get('reproduced')]
    n4 = (('REPRODUCED : False' in cen) if bad else ('REPRODUCED : False' not in cen))
    n5 = all(str(c.get('act')) in cen and str(c.get('copy')) is not None for c in bad)
    leftovers = [f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b363_copy_')]
    n6 = not leftovers
    gcn = n1 and n2 and n3 and n4 and n5 and n6
    print('    %d suites copied, %d reproducing their own act’s banked verdict' % (N['copies'], N['copies_reproducing']))
    print('    every copy has a row in the record : %s' % n3)
    print('    ### **EACH NON-REPRODUCING COPY IS NAMED WITH ITS REASON, NOT ADJUSTED** : %s %s'
          % (n4 and n5, [c.get('act') for c in bad] or 'none'))
    print('    ### **NO COPY SURVIVED THE RUN** (tools/b363_copy_*) : %s %s' % (n6, leftovers or ''))
    print('    %s' % ('PASS' if gcn else '### FAIL ###'))
    if not gcn:
        fails.append('G-CONTROL')

    print(chr(10) + '  G-NOEDIT (no owner instrument; NO BANKED SUITE EDITED; only this act’s papers path) '
          '### the working-tree half READ BEFORE THE PUSH:')
    owner = ['tools/e16/b264_eps_decay.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py',
             'tools/anchor_from_file.py', 'tools/quote_norm.py', 'tools/ferry_scan.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    suites_touched = [p for p in BANKED_SUITES if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
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

    print(chr(10) + '  G-TRAIL (one append-only block, filed and NOT attempted) ### READ BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    t3 = T['prefix_of_file'] and T['prefix_of_blob'] and T['attempted'] is False and T['priced'] is True
    t4 = all(q['equal'] for q in T['quotes']) and len(T['quotes']) == 4
    # ### **THE NEEDLES FOR THIS ARM ARE BUILT FROM THE FILE, NOT TYPED.** ### The first version typed
    # ### `NOT ATTEMPTED` in capitals; the entry says it in lower case. ### That is a needle typed rather
    # ### than read -- **THE FIRST LIVE INSTANCE OF THE SPECIES THIS ACT COUNTED IN THREE OTHER ACTS**,
    # ### and the helper retired it, which is what the census said it would do.
    blk5 = trails.split(TRAIL_MARK)[-1]
    try:
        t5 = (GN.present_needle(blk5, GN.build(TRAILS, 'FILED AND NOT RUN.')[1])
              and GN.present_needle(blk5, GN.build(TRAILS, 'It is affordable and it is not attempted here.')[1]))
    except GN.NeedleError:
        t5 = False
    t6 = 'W-ORD-LI-CUSP' in trails and 'W-ORD-LI-CUSP' in bank
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    the mark appears exactly once : %s ; the committed blob is a true prefix : %s' % (t1, t2))
    print('    the writing tool recorded append-only both ways, priced, NOT attempted : %s' % t3)
    print('    ### **ALL %d QUOTATIONS EQUAL TO THEIR FILES UNDER THE SHARED NORMALISER** : %s'
          % (len(T['quotes']), t4))
    print('    the entry says, in ITS OWN WORDS, that it is filed and not run and not attempted : %s'
          % t5)
    print('    ### **BOTH NEEDLES BUILT FROM THE FILE BY THE HELPER, NOT TYPED**; named in the bank : %s'
          % t6)
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason) ### READ BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'A GATE HELPER IS NOT EVEN AN INSTRUMENT' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTCURED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1b = 'READ BACK : anchored-gate-arms returns 1 row(s)' in irun
    k2b = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the gate is cured', 'every arm is retired',
               'a sharper instrument is a result', 'a banked suite was edited'))
    k3b = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1b and k2b and k3b
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (k1b, k2b, k3b))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTCURED')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock) ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, N, T))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    go = o1 and o2 and o3 and o4 and o5
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('        lock    %s' % (stampm.group(1) if stampm else '?'))
    print('        extract %s   census %s   trail %s' % (E['run_clock'], N['run_clock'], T['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE ANY WRITE : %s' % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b363_hooks.txt'), d('b363_mirror.txt')
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
        ('the headline sum %d' % N['headline_sum'], 'FOUR PLUS TWO PLUS FIVE IS ELEVEN' in bf),
        ('enumerated %d' % N['enumerated'], ('%d ARMS' % N['enumerated']) in bf or 'ELEVEN' in bf),
        ('retired %d of %d' % (N['retired'], N['enumerated']),
         ('%d OF %d' % (N['retired'], N['enumerated'])) in bf),
        ('wrong arms %s' % N['wrong_arms'], all(('`%s`' % a) in bank for a in N['wrong_arms'])),
        ('missing sentences %s' % N['missing_sentences'],
         all(('`%s`' % a) in bank for a in N['missing_sentences'])),
        ("the draft's population %d" % N['draft_population'], str(N['draft_population']) in bank),
        ("the draft's estimate %r" % N['draft_retirement'], N['draft_retirement'] in bank),
        ('control %d of %d' % (N['copies_reproducing'], N['copies']),
         ('%d of %d' % (N['copies_reproducing'], N['copies'])) in bank),
        ('needles %d/%d/%d' % (N['needles_declared'], N['needles_built'], N['needles_refused']),
         ('%d NEEDLES DECLARED, %d BUILT, %d REFUSED'
          % (N['needles_declared'], N['needles_built'], N['needles_refused'])) in bf),
        ('reads %d' % E['reads'], ('%d READS' % E['reads']) in bf),
        ('without an anchor %d' % E['without_anchor'], ('%d WITHOUT AN ANCHOR' % E['without_anchor']) in bf),
        ('anchors differing %d' % E['anchors_differing'],
         ('%d OF %d ANCHORS DIFFERING' % (E['anchors_differing'], E['reads'])) in bf),
        ('the trail entry grew the file by %d bytes' % T['grew'], str(T['grew']) in bank),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on census run file', N['run_file'] in bank),
        ('the relied-on trail run file', T['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks, never by name):')
    once = True
    for lbl, jf in (('extract', E), ('census', N), ('trail', T)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-8s %-26s clock on disk %s == the JSON's %s : %s" % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    repeats = sorted(f for f in os.listdir(D) if re.match(r'^b363_(census_run|extract_notes)\d*\.txt$', f))
    named = all(f in bank for f in repeats)
    once = once and named
    print('    ### **EVERY REPEAT IS NAMED IN THE BANK, SUPERSEDED OR RELIED ON : %s** %s' % (named, repeats))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed about the object, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    mine = ('gate_needle.py', 'b363_regspec.py', 'b363_extract.py', 'b363_census.py', 'b363_trail.py',
            'b363_correspondence.py', 'b363_index_append.py', 'b363_checks.py')
    for p in [t(x) for x in mine]:
        src2 = strip_prose(p)
        for b in banned:
            if b in src2:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b363_census.py', 'b363_extract.py', 'b363_trail.py'))]
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

    marker = '# ### THE ANCHORED GATE ARMS, COUNTED AND NOT ASSERTED (b363).'
    nxt = '# ### THE APPROXIMATION REGISTER, READ UNDER A CAP (b362).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    blk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
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
    tmpdir = tempfile.mkdtemp(prefix='b363_hedge_')
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
    print('  ### needles refused : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
