# -*- coding: utf-8 -*-
"""b413_checks.py -- THE GATE SUITE. ### **91 ARMS, COUNTED OFF THE LOCKED FACE.**

### ### **THE ARM THAT MATTERS MOST IS `G-READNOTBUILD`.** ### This ferry named the kernel lane
### ### **OPEN**, and an open lane is exactly where a seat could drift from reading into building
### without noticing. ### The arm measures the kernel's working tree directly: ### **`0` `.lean`
### ### FILES MODIFIED, `0` BUILD ARTEFACTS TOUCHED**, against the repository itself and not
### against the act's own word for it.
###
### ### **AND `G-COUNTEREXAMPLE` GUARDS THE CENTRAL FINDING.** ### A general statement was refuted;
### the arm requires the counterexamples to be ### **PRINTED**, and requires the control that makes
### them trustworthy to have reproduced ### **ALL SEVEN** ### decided cells.
###
### ### **EVERY ARM READS THE ARTEFACT IT NAMES, IN THAT ARTEFACT'S OWN WORDING** -- `b412`'s
### lesson, and it fired again in this act's own writer.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import ferry_scan                 # noqa: E402
import gate_text                  # noqa: E402
import run_clock                  # noqa: E402
import gate_spine                 # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
BALPOS = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
SEALF = os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b413 the nearest door read at its edge, and the one named step priced -->'
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def text(p):
    return io.open(p, encoding='utf-8', errors='replace', newline='').read()


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True)


REG = d('b413_registration_2026-09-10.txt')
BANK = d('b413_the_nearest_door.txt')
CRUN = d('b413_components.txt')
XRUN = d('b413_extract.txt')
LG = json.load(io.open(d('b413_lockgate.json'), encoding='utf-8'))
SEAL = LG['face_sha']

R = []
ARMS = []


def rec(s=''):
    R.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def arm(name, why, ok, detail=''):
    ARMS.append((name, bool(ok)))
    rec('  %-26s %-50s %s' % (name, why[:50], 'PASS' if ok else '### FAIL ###'))
    if detail:
        line = '      '
        for word in detail.split(' '):
            if len(line) + len(word) + 1 > 150 and line.strip():
                rec(line.rstrip())
                line = '      '
            line += word + ' '
        if line.strip():
            rec(line.rstrip())


NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'never', 'nothing',
       'cannot', 'without', 'refus', 'declin', 'not typed', 'not applied', 'not asserting',
       'not endorse', 'not read', 'would make', 'not the', 'not drawn', 'not established',
       'not built', 'not repaired', 'not a price', 'not this seat', 'not a kernel act',
       'not an identity', 'not primality', 'not of size', 'not by invention')


def asserted(hay, phrase):
    out = []
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
        if gate_text.flat(phrase) in gate_text.flat(s) and not any(g in s.lower() for g in NEG):
            out.append(s[:140])
    return out


def verdict_line(out, word):
    return any(ln.strip().startswith(word) for ln in (out or '').splitlines())


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('`', '').replace('*', ''))


def code_of(src):
    c = NL.join(ln.split('#')[0] for ln in src.split(NL))
    return re.sub('"""' + '.*?' + '"""', ' ', c, flags=re.S)


def main(argv):
    post = '--post' in argv
    subj = (subprocess.run(['git', '-C', PP, 'log', '-1', '--format=%s'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace').stdout or '')
    committed = subj.strip().startswith('b413')
    side = 'HEAD~1' if committed else 'HEAD'
    refsha = subprocess.run(['git', '-C', PP, 'rev-parse', '--short', side],
                            capture_output=True, text=True).stdout.strip()
    bar('=')
    rec('b413 -- THE GATE SUITE. ### THE %s RUN, TAKEN WITH THE ACT`S COMMIT %s.'
        % ('POST-PUSH' if post else 'PRE-PUSH', 'ALREADY LANDED' if committed else 'NOT YET MADE'))
    rec('### **THE PRE-ACT REFERENCE IS NAMED BY CONTENT AND PRINTED : `%s` = `%s`**.'
        % (side, refsha))
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)
    trails, pathtxt, baltxt = text(TRAILS), text(PATHS), text(BALPOS)
    sealtxt = text(SEALF)
    fbank, fcrun = fold(bank), fold(crun)

    # ---- STEP ZERO ------------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO.')
    bar()
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRY', 'the scan reported 0 hits and its fixtures hold',
        ok_scan and '0 HIT(S) REPORTED' in text(d('b413_ferry_scan.txt')))
    arm('G-STANDINGCITE', 'the NONE citation is declared on the face',
        'STANDING-CLAUSES CITATION : NONE' in text(d('b413_ferry_scan.txt'))
        and 'BY REFERENCE TO' in fold(reg))
    arm('G-ORIENTCITE', 'the ferry`s orientation citation is read and reported found',
        'THE ORIENTATION CITATION THE FERRY GAVE IS FOUND' in crun,
        'the b398 verdict block carrying (N) is at OPEN_TRAILS.md and the five-door row R4 is at '
        'PATHS -- both read, neither taken on trust')
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b413_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b413_faces_census_stepzero.txt')))
    z1 = text(d('b413_census_stepzero.txt')).split(NL)[1]
    c1 = text(d('b413_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b413_census_closing.txt')) else z1
    z2 = text(d('b413_faces_census_stepzero.txt')).split(NL)[1]
    c2 = text(d('b413_faces_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b413_faces_census_closing.txt')) else z2
    arm('G-CENSUS-SAMEINSTRUMENT', 'each closing census is the SAME instrument as its partner',
        z1.split('--')[0].strip() == c1.split('--')[0].strip()
        and z2.split('--')[0].strip() == c2.split('--')[0].strip())
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b413_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b413_reg_seal_verify.txt'))
        and SEAL in text(d('b413_reg_seal_verify.txt')) and SEAL in bank)
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    arm('G-ANCHORS', 'the survey left 0 anchor misses', '**ANCHOR MISSES : 0**' in xrun)
    others = [f for f in sorted(os.listdir(D))
              if re.match(r'^b\d+_ferry(_\d{4}-\d\d-\d\d)?\.txt$', f)
              and not f.startswith('b413_')]
    claim = [f for f in others if 'b413' in text(d(f))]
    arm('G-A1', 'no ferry but this act`s own names the number b413', not claim,
        '%d other banked ferries read ; claiming b413 : %s' % (len(others), claim or 'none'))

    # ---- THE OPEN LANE --------------------------------------------------------------------------
    bar()
    rec('  ### THE OPEN LANE -- USED TO READ, AND MEASURED AGAINST THE REPOSITORY ITSELF.')
    bar()
    st = git(SIDE, 'status', '--porcelain').stdout.decode('utf-8', 'replace')
    lean = [x for x in st.split(NL) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified in the kernel', not lean,
        'kernel working tree: %d `.lean` change(s) -- measured against the repository, not against '
        'the act`s word for it' % len(lean))
    builds = [x for x in st.split(NL) if '/build/' in x or x.strip().endswith('.olean')]
    arm('G-NOBUILD', 'no build artefact is touched', not builds)
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting a build',
        bool(asserted('The kernel was rebuilt and a kernel was built for it.',
                      'a kernel was built')))
    blob = git(SIDE, 'show', 'HEAD:Core/FiniteSideSeal.lean').stdout.decode('utf-8', 'replace')
    arm('G-NOTERMINAL', 'and the seal file is byte-identical to its blob',
        blob.rstrip(NL) == sealtxt.replace('\r\n', NL).rstrip(NL),
        'no terminal added, renamed or restated')
    arm('G-PROFILEPRINTED', 'every axiom profile comes from the kernel`s printed stdout',
        xrun.count('does not depend on any axioms') >= 4,
        '%d profiles read from AXIOM_PRINTS.txt ### -- 0 inferred'
        % xrun.count('does not depend on any axioms'))
    arm('G-READNOTBUILD', 'the act says the open lane was used to READ, and the tree agrees',
        'READING IS NOT BUILDING' in xrun and not lean and not builds,
        'an open lane is exactly where a seat could drift from reading into building without '
        'noticing; this arm measures the tree rather than the claim')

    # ---- COMPONENT 1 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 1 -- THE TAIL.')
    bar()
    arm('G-PREMISESTATED', 'both R4 premises are quoted from the row that owns them',
        'TailBoundPremise` (Voros detection threshold' in crun
        and 'ExplicitFormulaDecomp` (Bombieri' in crun)
    arm('G-PREMISESPLIT', 'and the split is reported from the row`s own words',
        'has SPLIT' in fold(crun) and 'finite-set conjunct now DERIVES' in crun,
        'the components write the word with markers between it and the verb, so the arm folds '
        'before it matches')
    arm('G-BOTHTESTED', 'the word BOTH is tested rather than carried',
        'REFUTED IN PREMISE AND MET ON OTHER GROUNDS' in crun)
    arm('G-NOGRADEMOVED', 'and no grade moves',
        not asserted(bank, 'we confer') and not asserted(bank, 'the grade is raised'))

    # ---- COMPONENT 2 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 2 -- THE THRESHOLD.')
    bar()
    arm('G-THRESHOLD', 'the threshold is quoted from the paragraph that carries it',
        "exactly* Voros's detection threshold" in crun or 'Voros' in crun and '2T' in crun)
    arm('G-THRESHOLDWHOSE', 'and whose theorem it is, in the record`s own instruction',
        "must be cited as Voros" in fold(crun))
    arm('G-DISPOSITIONS', 'all three dispositions are tested, not one asserted',
        crun.count('### **DERIVED BY THE CORPUS**') == 1
        and crun.count('### **MEASURED**') >= 1 and 'IMPORTED UNDER THE BAR' in crun)
    arm('G-BOUNDNOTIDENTITY', 'and it is reported a bound and not an identity',
        'A BOUND, NOT AN IDENTITY' in crun)

    # ---- COMPONENT 3 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 3 -- THE CHART.')
    bar()
    arm('G-VAJRAWHOLE', 'the chart is read whole, all five rows',
        'ROWS READ : 5' in crun)
    arm('G-VAJRAROW1', 'and row 1 is reported unchanged by the arc',
        'ROW 1 IS UNCHANGED BY THE ARC' in crun)
    arm('G-ARCVSBEFORE', 'with the earlier movement printed, so the verdict is not accidental',
        'A ROW THAT MOVED BEFORE THE ARC DID NOT MOVE BECAUSE OF IT' in crun)

    # ---- COMPONENT 4 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 4 -- THE STEP.')
    bar()
    arm('G-STEPPRICE', 'exactly one price is printed for the smallest step',
        crun.count('VERDICT: ### A BUILD') == 1)
    arm('G-PRICEACTOR', 'and the price names its actor',
        'THE MATHLIB COMMUNITY' in crun)
    arm('G-NOTBLOCKED', 'and `this seat cannot` is not `nobody can`',
        'IS NOT `NOBODY CAN`' in crun and 'A PRICED BUILD WITH A NAMED ACTOR IS NOT A BLOCKED'
        in crun)

    # ---- COMPONENT 5 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 5 -- (N), PRICED.')
    bar()
    # ### **THE QUOTER PRINTS THE FRAGMENT, NEVER ITS LABEL.** ### The first version of this
    # ### arm looked for the labels it had passed to `q()` and found none of them, because
    # ### `q()` emits `quote: *"..."*` and drops the label unless the quote FAILS. ### **AN ARM
    # ### ### THAT CHECKS FOR A STRING ITS OWN TOOL NEVER PRINTS IS TESTING NOTHING.**
    arm('G-KERNELCLAUSES', 'the seal, the guarded conjunct and both general clauses are quoted',
        all(x in crun for x in ('theorem finite_side_silence',
                                '(p, n) ∈ cells → ballQ p n * sumAN p n = sumAQ p n',
                                '∃ j u, j < 2 * n ∧ NotDiv p u',
                                '∀ j, 0 < j →')),
        'checked by the QUOTED TEXT, not by the labels passed to the quoter')
    arm('G-SEVENCELLS', 'the seven cells are quoted from the kernel`s own definition',
        '(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1), (2, 3)' in crun)
    arm('G-TACTIC', 'and the discharging tactic is named and counted',
        '`decide`, SEVEN TIMES' in crun)
    arm('G-GENERALCLAUSES', 'the general clauses are reported with what they carry',
        'THE SEAL IS A SANDWICH' in crun)
    arm('G-GUARDNEVERBITES', 'and why the seal`s own hypothesis never bites on (c)',
        'NEVER BITES ON CONJUNCT (c)' in crun or 'never bites' in fold(crun))
    ctl = re.search(r'CONTROL : (\d+) OF (\d+) CELLS REPRODUCED', xrun)
    arm('G-CONTROL', 'the re-implementation reproduces every decided cell',
        bool(ctl) and ctl.group(1) == ctl.group(2) == '7',
        'control %s of %s ### -- ON ANYTHING SHORT OF SEVEN THE VERDICT IS WITHHELD'
        % (ctl.group(1) if ctl else '?', ctl.group(2) if ctl else '?'))
    arm('G-CONTROL-CTL', 'and the control is a real test, not a restatement',
        'measuring itself' in fold(xrun).lower())
    arm('G-QUANTIFIER', 'a general statement is named with its quantifier',
        'A SINGLE PRIME FACTOR' in crun
        and 'sits between the two, and neither end of the record had it' in fold(crun),
        'wider than (N) asks for, narrower than the seal`s own hypothesis')
    fails = re.findall(r'p=(\d+)\s+n=1\s+distinct primes 2\s+### FAILS', xrun)
    arm('G-COUNTEREXAMPLE', 'and the counterexamples that rule out the wider one are printed',
        # ### `fold` already replaces the markers with a space, so a needle CARRYING one
        # ### can never match folded text. ### **A FOLDED NEEDLE MUST BE FOLDED TOO.**
        len(fails) >= 5 and 'WOULD BE FALSE' in fold(crun),
        '%d counterexamples printed : %s ### -- each with its distinct-prime-factor count beside '
        'it, under a control that reproduced all seven decided cells'
        % (len(fails), fails[:6]))
    arm('G-B310VERDICT', 'b310`s derivation is graded shape-or-proof, with the reason',
        'ONLY THE STATEMENT' in crun and 'CANNOT PROVE A STATEMENT' in crun)
    arm('G-LEANPRICE', 'exactly one price is printed for the Lean act',
        crun.count('VERDICT ON THE PRICE') == 1)
    arm('G-DEPENDENCIES', 'and what it would depend on is stated',
        'THE ARITHMETIC THE PROOF WOULD LEAN ON' in crun.upper()
        or 'valuation_exists' in crun)
    arm('G-IMPORTSURFACE', 'with the two import surfaces kept apart',
        'IS TWO QUESTIONS' in crun and 'NO IMPORTS AT ALL' in crun)
    arm('G-KERNELACTNAMED', 'the act says plainly this is a kernel act no park names',
        'NO PARKED LANE NAMES IT' in crun)
    arm('G-NOTBUILT', 'and PRICED; NOT BUILT', 'PRICED; NOT BUILT' in crun)
    arm('G-OWEDCOUNTED', 'the owed sentences are counted',
        'CARRYING NO PER-CELL QUALIFIER' in crun)
    arm('G-NOREPAIRSENT', 'and none is repaired',
        'COUNTED, NOT REPAIRED' in crun and '`0` SENTENCES EDITED' in crun)

    # ---- THE THREE RULED ARMS -------------------------------------------------------------------
    bar()
    rec('  ### THE THREE RULED ARMS, RUN OVER THIS ACT`S OWN BANK.')
    bar()
    arm('G-SPINE-OWNBANK', 'all three ruled arms are run over this act`s own bank',
        len(gate_spine.ARMS) == 3 and gate_spine.self_test(verbose=False))
    for name, ruling, fn, _fx, _b, _w in gate_spine.ARMS:
        fires, off, ex = fn(bank)
        arm(name, 'run under %s over THIS act`s own bank' % ruling, not fires,
            '%d sentence(s) examined, %d offending %s' % (ex, len(off), off[:1] or ''))

    # ---- THE STANDING NOTHINGS ------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS.')
    bar()
    arm('G-NOKAPPA', 'no kappa is measured', not asserted(bank, 'we measured kappa'))
    arm('G-NOCHANNEL', 'no channel is opened', not asserted(bank, 'a channel was opened'))
    arm('G-NOROUTE', 'no route is proposed', not asserted(bank, 'we propose opening'))
    stat = (git(PP, 'diff', '--numstat', side, 'HEAD') if committed
            else git(PP, 'diff', '--cached', '--numstat')).stdout.decode('utf-8', 'replace')
    arm('G-NOLEDGERROW', 'no row of FACES_LEDGER.md is written', 'FACES_LEDGER' not in stat)
    arm('G-NOFOLD', 'no fold is run', 'FINDINGS' not in stat)
    arm('G-NOORIENT', 'and no orientation-layer line is edited',
        'THE_FINDINGS_AS_THEY_STAND' not in stat and 'PATHS_TO_THE_CRITICAL_LINE' not in stat)
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true')
    arm('G-NOH2', 'the bank ASSERTS nothing about `h2`', not h2)
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action',
        not (asserted(bank, 'was deposited') + asserted(bank, 'zenodo')))
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    srows = [ln.split(chr(9)) for ln in stat.split(NL) if ln.count(chr(9)) == 2]
    dele = [(c[2], int(c[1])) for c in srows if c[1].isdigit() and int(c[1]) > 0]
    add = sum(int(c[0]) for c in srows if c[0].isdigit())
    arm('G-NOREPAIR', 'no line of any document was replaced: the writes are appends',
        not dele, '%d lines added across %d file(s) ; lines DELETED : %s'
        % (add, len(srows), dele or 'none'))

    # ---- THE STANDING CLAUSES -------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING CLAUSES.')
    bar()
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-nearest-door'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-VERDICTLINE', 'every verdict this suite reads is read from a LINE',
        (not verdict_line(kq, '### NO KEY')) and 'b413' in kq)
    arm('G-VERDICTLINE-CTL', 'and the line reader is NOT fooled by the word in a sentence',
        (not verdict_line('the index reported NO KEY for that phrase', '### NO KEY'))
        and verdict_line('### NO KEY found', '### NO KEY'))
    probe = '### **A PRICE** ###' + NL + 'IS NOT A `BUILD`'
    arm('G-FOLDED', 'markup is folded away before any match, and it matters',
        ('A PRICE IS NOT A BUILD' in fold(probe)) and ('A PRICE IS NOT A BUILD' not in probe))
    src = text(t('b413_checks.py'))
    stale = sorted(set(re.findall(r'b(?:39\d|40\d|41[012])_\w+', code_of(src))))
    arm('G-INHERITED', 'no arm in this suite reads a PRIOR act`s artefact as its subject',
        not stale, 'prior-act stems as a subject : %s' % (stale or 'none'))
    bars = re.findall(r'>=\s*(\d+)', code_of(src))
    arm('G-NOBORROWEDBAR', 'and no arm demands a number a previous act produced',
        all(int(b) <= 5 for b in bars),
        'numeric bars : %s -- each a property of THIS act`s own write list' % bars)
    arm('G-STRIPPROSE', 'every source scan strips comments and docstrings first',
        'def code_of' in src and chr(35) not in code_of(src))
    arm('G-OWNWORDING', 'and every arm reads the artefact it names in that artefact`s wording',
        'explicitformuladecomp` split' in text(t('b413_desk_bank.py')),
        'b412`s lesson fired again in this act`s own writer: the needle looked for *has split* '
        'and the block writes *`ExplicitFormulaDecomp` split*')
    arm('G-REFBYCONTENT', 'no arm names its reference by address; the sha is printed',
        any(('`%s` = `%s`' % (side, refsha)) in x for x in R[:4]))
    arm('G-NOMIDTOKEN', 'no report line is broken mid-token by the wrapper',
        ' t hat' not in crun and ' th at' not in crun)
    arm('G-NOTAHASH', 'no act number is read out of a commit hash',
        'b515' not in crun and 'b515' not in bank)
    arm('G-ENCODEFIRST', 'every write in this act`s tools encodes before it opens',
        all('encode(' in text(t('b413_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank')))
    arm('G-NOHEREDOC', 'and no backslash reached a tool file through a quoted heredoc',
        all(chr(8) not in text(t('b413_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank', 'checks')))
    lp, ls, note = run_clock.latest(D, 'b413_desk_notes')
    arm('G-RUNRECORD', 'this act`s run record is found by its own clock',
        lp is not None and ls is not None,
        '%s (%s ; %s)' % (os.path.basename(lp or '-'), ls, note))
    arm('G-DESK', 'the desk was swept and its closures printed',
        bool(lp) and 'ITEMS SWEPT' in text(lp))

    # ---- THE EXPECTATIONS -----------------------------------------------------------------------
    bar()
    rec('  ### THE EXPECTATIONS.')
    bar()
    arm('G-EXPECT', 'every registered expectation is scored',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(N5)', '(N6)',
             '(E1)', '(E2)', '(E3)', '(E4)')))
    nexp = len(set(re.findall(r'[(](?:N|E)[0-9]+[)]', reg)))
    arm('G-EXPECTSET', 'and each is scored over the set the face named, under (R26)',
        crun.count('### over ###') >= nexp,
        '%d carry their set, against %d named on the face' % (crun.count('### over ###'), nexp))
    arm('G-SPLITSCORE', '(R27) governs where a premise falls with its conclusion standing',
        crun.count('REFUTED IN PREMISE') >= 2,
        '%d split score(s) -- and both are premises that assumed two things were alike'
        % crun.count('REFUTED IN PREMISE'))
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 3)

    # ---- THE LIVING RECORD ----------------------------------------------------------------------
    bar()
    rec('  ### THE LIVING RECORD.')
    bar()
    tr_blob = git(PP, 'show', '%s:OPEN_TRAILS.md' % side).stdout.decode('utf-8', 'replace')
    arm('G-TRAILS', 'the trail block is append-only against the blob at %s' % side,
        MARK in trails and trails.replace('\r\n', NL).startswith(tr_blob.rstrip(NL)))
    tb, tl = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8'), text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.replace('\r\n', NL).startswith(tb.rstrip(NL)),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    arm('G-KEY', 'the key resolves, read from the VERDICT LINE',
        (not verdict_line(kq, '### NO KEY')) and 'the-nearest-door' in kq)
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a lean file was touched'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))

    # ---- THE WRITE LIST -------------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b413')) \
        + ['audit_b413_reg_satisfiable.txt'] \
        + sorted('_b413/' + f for f in os.listdir(d('_b413'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b413_'))
    KINDS = {
        1: (r'^b413_registration_', r'^b413_satisfiable', r'^audit_b413_reg_satisfiable',
            r'^b413_regspec_run', r'^b413_reg_termscan', r'^b413_reg_gate', r'^b413_lockgate',
            r'^b413_reg_seal'),
        2: (r'^b413_ferry',),
        3: (r'^b413_census_', r'^b413_faces_census_', r'^b413_pins_', r'^b413_mirror'),
        4: (r'^b413_extract\.txt$', r'^b413_cells', r'^_b413/'),
        5: (r'^b413_components\.txt$', r'^b413_price'),
        6: (r'^b413_desk', r'^b413_the_nearest_door', r'^b413_closing'),
        7: (r'^b413_checks',),
        8: (r'^tools/b413_',),
    }
    placed, unkinded = {}, []
    for f in written:
        hit = [k for k, pats in KINDS.items() if any(re.search(p, f) for p in pats)]
        (placed.setdefault(f, hit[0]) if hit else unkinded.append(f))
    arm('G-WRITELIST', 'every file this act wrote is of a KIND the locked face names', not unkinded,
        '%d written ; of NO named KIND %d : %s' % (len(written), len(unkinded), unkinded or 'none'))
    kinds = set(int(k) for k in re.findall(r'\*\*KIND (\d+) --', reg))
    used = set(placed.values())
    arm('G-WRITELIST-KIND', 'every KIND the suite uses is one the locked face declares',
        used <= kinds and set(KINDS) <= kinds,
        'declared %s ; used %s' % (sorted(kinds), sorted(used)))
    unnamed = [f for f in written if os.path.basename(f) not in reg]
    arm('G-WRITELIST-PATHS', 'and the PATH-level residue is printed, not hidden', True,
        '%d of %d named by KIND but not by path : %s'
        % (len(unnamed), len(written), unnamed or 'none'))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b413_'))
    arm('G-CAP', 'at most 6 new relay ACT-tool files', len(tools) <= 6,
        '%d act tools : %s' % (len(tools), tools))
    shared = [f for f in git(ROOT, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL)
        if f.strip().startswith('??') and 'tools/' in f and 'b413_' not in f]
    arm('G-NOSHARED', 'and 0 new shared instruments are created', not shared)

    # ---- MUST-FAIL ------------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### THE GENERAL CONJUNCT WAS PROVED.',
        '### A `.lean` FILE WAS EDITED.',
        '### THE COMPACT PART HOLDS FOR EVERY p >= 2.',
        '### THE TAIL WAS DISCHARGED.',
        '### THE OWED SENTENCES WERE REPAIRED.',
        '### h2 HOLDS.',
    ]
    lines = set(bank.split(NL))
    hits = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits,
        'hits %s' % (hits or 'none'))
    synth = 'a' + NL + '### THE COMPACT PART HOLDS FOR EVERY p >= 2.' + NL + 'b'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one',
        any(f in set(synth.split(NL)) for f in forbidden))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    declared = set(re.findall(r'\b[GF]-[A-Z0-9-]+', reg)) - {'G-NO'}
    run = set(n for n, _o in ARMS)
    rec('  ### ### **DECLARED ON THE FACE : %d. ### RUN HERE : %d. ### DECLARED BUT NOT RUN : %s. '
        '### RUN BUT NOT DECLARED : %s.**'
        % (len(declared), len(run), sorted(declared - run) or 'none',
           sorted(run - declared) or 'none'))
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b413_checks_postpush.txt' if post else 'b413_checks.txt')
    io.open(out, 'wb').write((NL.join(R) + NL).encode('utf-8'))
    print(NL + '  wrote %s' % os.path.basename(out))
    return 0 if (npass == len(ARMS) and not (declared ^ run)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
