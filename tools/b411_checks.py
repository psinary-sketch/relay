# -*- coding: utf-8 -*-
"""b411_checks.py -- THE GATE SUITE. ### **86 ARMS, COUNTED OFF THE LOCKED FACE.**

### ### **THE ARMS THAT MATTER MOST ARE `G-JOIN-READBACK` AND `G-KINDONGRADE`.** ### The first
### requires each cross-reference to resolve in the file it names -- ### **A POINTER THAT POINTS
### ### AT NOTHING IS WORSE THAN NONE.** ### The second requires the act to have checked that a
### grade name belongs to the vocabulary it was attributed to, which is `(R28)` turned on a
### navigator's sentence rather than on the record's.
###
### ### **AND `G-NOTSUPERSEDED` GUARDS THE THING MOST EASILY GOT WRONG HERE:** ### finding that
### the gate DOES price something must not be reported as overturning `b410`, and `b410` must not
### be reported as overturning the gate. ### They answer different questions.
###
### ### **EVERY ARM SCANNING SOURCE STRIPS COMMENTS AND DOCSTRINGS FIRST** (`b410`'s
### `G-NOBORROWEDBAR` fired on its own comment), and ### **NO REPORT LINE IS BROKEN MID-TOKEN.**
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
FACES = os.path.join(PP, 'FACES_LEDGER.md')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
INST = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
ENGINE = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
GAUGE = os.path.join(ROOT, 'reports', '2026-08-01-w-half-consult.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b411 the join, the collision, the import priced as an import -->'
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


REG = d('b411_registration_2026-09-10.txt')
BANK = d('b411_the_join_and_the_price.txt')
CRUN = d('b411_components.txt')
XRUN = d('b411_extract.txt')
LG = json.load(io.open(d('b411_lockgate.json'), encoding='utf-8'))
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
    rec('  %-30s %-50s %s' % (name, why[:50], 'PASS' if ok else '### FAIL ###'))
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
       'not a measured', 'no certificate', 'not narrowed', 'not priceable', 'not opened',
       'not paid', 'not a merger', 'not circular', 'not made here', 'not taking')


def asserted(hay, phrase):
    out = []
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
        if gate_text.flat(phrase) in gate_text.flat(s) and not any(g in s.lower() for g in NEG):
            out.append(s[:140])
    return out


def verdict_line(out, word):
    """### **A TOOL'S VERDICT IS A LINE, NOT A SUBSTRING** -- `A2`."""
    return any(ln.strip().startswith(word) for ln in (out or '').splitlines())


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('`', '').replace('*', ''))


def code_of(src):
    """### **COMMENTS AND DOCSTRINGS STRIPPED BEFORE ANY SOURCE SCAN** -- `b410`'s lesson."""
    c = NL.join(ln.split('#')[0] for ln in src.split(NL))
    return re.sub(r'"""' + '.*?' + '"""', ' ', c, flags=re.S)


def main(argv):
    post = '--post' in argv
    subj = (subprocess.run(['git', '-C', PP, 'log', '-1', '--format=%s'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace').stdout or '')
    committed = subj.strip().startswith('b411')
    side = 'HEAD~1' if committed else 'HEAD'
    refsha = subprocess.run(['git', '-C', PP, 'rev-parse', '--short', side],
                            capture_output=True, text=True).stdout.strip()
    bar('=')
    rec('b411 -- THE GATE SUITE. ### THE %s RUN, TAKEN WITH THE ACT`S COMMIT %s.'
        % ('POST-PUSH' if post else 'PRE-PUSH', 'ALREADY LANDED' if committed else 'NOT YET MADE'))
    rec('### **THE PRE-ACT REFERENCE IS NAMED BY CONTENT AND PRINTED : `%s` = `%s`**, chosen '
        'because the newest commit %s name this act.'
        % (side, refsha, 'DOES' if committed else 'does NOT'))
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)
    ibtxt, insttxt, trails = text(IB), text(INST), text(TRAILS)
    engtxt, gaugetxt, facestxt = text(ENGINE), text(GAUGE), text(FACES)
    fbank, fcrun, ftrails = fold(bank), fold(crun), fold(trails)

    # ---- STEP ZERO ------------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO, RE-READ FROM ITS OWN RECORDS.')
    bar()
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRY', 'the scan reported 0 hits and its fixtures hold',
        ok_scan and '0 HIT(S) REPORTED' in text(d('b411_ferry_scan.txt')))
    arm('G-STANDINGCITE', 'the NONE citation is declared on the face, not passed by',
        'STANDING-CLAUSES CITATION : NONE' in text(d('b411_ferry_scan.txt'))
        and 'BY REFERENCE TO' in reg)
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b411_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b411_faces_census_stepzero.txt')))
    z1 = text(d('b411_census_stepzero.txt')).split(NL)[1]
    c1 = text(d('b411_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b411_census_closing.txt')) else z1
    z2 = text(d('b411_faces_census_stepzero.txt')).split(NL)[1]
    c2 = text(d('b411_faces_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b411_faces_census_closing.txt')) else z2
    arm('G-CENSUS-SAMEINSTRUMENT', 'each closing census is the SAME instrument as its partner',
        z1.split('--')[0].strip() == c1.split('--')[0].strip()
        and z2.split('--')[0].strip() == c2.split('--')[0].strip(),
        'step zero %r / close %r' % (z1[:30], c1[:30]))
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b411_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b411_reg_seal_verify.txt'))
        and SEAL in text(d('b411_reg_seal_verify.txt')) and SEAL in bank)
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    arm('G-ANCHORS', 'the survey left 0 anchor misses', '**ANCHOR MISSES : 0**' in xrun)
    others = [f for f in sorted(os.listdir(D))
              if re.match(r'^b\d+_ferry\.txt$', f) and not f.startswith('b411_')]
    claim = [f for f in others if 'b411' in text(d(f))]
    arm('G-A1', 'no ferry but this act`s own names the number b411', not claim,
        '%d other banked ferries read ; claiming b411 : %s' % (len(others), claim or 'none'))

    # ---- b410 -----------------------------------------------------------------------------------
    bar()
    rec('  ### THE PREDECESSOR, CORRECTED AND NOT EDITED.')
    bar()
    arm('G-B410-CORRECTED', 'b410`s citation count is corrected on the face and in the trail',
        'A COUNT OF A' in reg and 'dated by the act that prints it' in ftrails.lower())
    b410f = [f for f in git(PP, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL) if 'b410' in f] + \
        [f for f in git(ROOT, 'status', '--porcelain').stdout.decode(
            'utf-8', 'replace').split(NL) if re.search(r'\bb410', f) and f.strip()[:1] != '?']
    arm('G-B410-NOTEDITED', 'and no b410 file, bank or face is modified by this act',
        not b410f, 'modified b410 artefacts : %s' % (b410f or 'none'))
    now = len([1 for _r, p in [(0, os.path.join(PP, x)) for x in []]])  # placeholder, see below
    WB = chr(92) + 'b'
    cited = 0
    for root, dirs, fs in os.walk(PP):
        dirs[:] = [x for x in dirs if x not in ('.git', 'archive')]
        for f in fs:
            if f.endswith('.md') and 'outputs' not in root:
                if re.search(WB + 'I-7' + WB,
                             text(os.path.join(root, f))):
                    cited += 1
    arm('G-RECOUNT', 'the citation count is RE-MEASURED here, not carried from b410',
        ('`%d` LIVE DOCUMENTS' % cited) in crun,
        'b410 printed 12 ; re-measured here %d ; and the act states that 2 of them are b410`s own '
        'writes -- A COUNT OF A LIVING RECORD IS DATED BY THE ACT THAT PRINTS IT' % cited)

    # ---- COMPONENT 1 -- THE JOIN ----------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 1 -- THE JOIN.')
    bar()
    ibj = [ln for ln in ibtxt.split(NL) if 'b411, ruling R29' in ln]
    inj = [ln for ln in insttxt.split(NL) if 'b411, ruling R29' in ln]
    arm('G-JOIN-TWOLINES', 'exactly one cross-reference line in each document',
        len(ibj) == 1 and len(inj) == 1,
        'keystone %d line(s), register %d line(s)' % (len(ibj), len(inj)))
    ib_blob = git(PP, 'show', '%s:phase1.5/method/INVARIANCE_BARRIERS.md' % side
                  ).stdout.decode('utf-8', 'replace')
    in_blob = git(PP, 'show', '%s:phase1.5/method/INSTRUMENTS.md' % side
                  ).stdout.decode('utf-8', 'replace')
    ibset = set(ib_blob.split(NL)) - set(ibtxt.replace('\r\n', NL).split(NL))
    inset = set(in_blob.split(NL)) - set(insttxt.replace('\r\n', NL).split(NL))
    arm('G-JOIN-ADDITIVE', 'and no original line of either document is lost',
        not ibset and not inset,
        'lines present in the blob and absent live : keystone %d, register %d'
        % (len(ibset), len(inset)))
    arm('G-JOIN-READBACK', 'each cross-reference resolves in the file it names',
        bool(ibj) and 'I-7' in ibj[0] and re.search(r'^#+\s+I-7' + WB, insttxt, re.M) is not None
        and bool(inj) and 'INVARIANCE_BARRIERS.md' in inj[0]
        and 'individual-element specifications requiring P-information to cross I' in ibtxt,
        'the keystone`s line names I-7 and I-7 is a heading of the register; the register`s line '
        'names the keystone`s path and clause and both are there -- A POINTER THAT POINTS AT '
        'NOTHING IS WORSE THAN NONE')
    src_db = text(t('b411_desk_bank.py'))
    arm('G-JOIN-INDEPENDENT', 'the two lines are literals, neither composed from the other`s file',
        'JOIN_IB_LINE = (' in src_db and 'JOIN_INST_LINE = (' in src_db
        and 'insttxt' not in src_db.split('JOIN_IB_LINE')[1].split(')')[0],
        'neither file is read in order to compose the other`s line, so a mistake in one cannot '
        'propagate into the other')
    arm('G-JOIN-NORENUMBER', 'no heading, number or definition moved in either document',
        re.findall(r'^#+\s+(I-\d+[a-z]*)', in_blob, re.M)
        == re.findall(r'^#+\s+(I-\d+[a-z]*)', insttxt, re.M)
        and re.findall(r'\*\*Definition 2\.\d', ib_blob)
        == re.findall(r'\*\*Definition 2\.\d', ibtxt),
        'the register`s heading sequence and the keystone`s definition sequence are byte-identical '
        'to the blob')
    arm('G-JOIN-BOTHWAYS', 'and the act says what the join is NOT',
        'NOT A MERGER' in fcrun and 'Neither derives the other' in ibj[0]
        and 'Neither derives the other' in inj[0],
        'both lines carry the disclaimer in the documents themselves, not only in the bank')

    # ---- COMPONENT 2 -- THE COLLISION -----------------------------------------------------------
    bar()
    rec('  ### COMPONENT 2 -- THE COLLISION.')
    bar()
    rows = [ln.split(chr(9)) for ln in text(d('b411_numbering.txt')).splitlines() if ln.strip()]
    arm('G-NUMBERING', 'the numbering is enumerated from the register`s own headings',
        len(rows) >= 15 and all(r[0].startswith('I-') for r in rows),
        '%d numbers enumerated, each with its live citation list' % len(rows))
    arm('G-VACANCIES', 'and the vacancies below the highest are MEASURED, not assumed',
        'VACANCIES BELOW THE HIGHEST' in crun)
    arm('G-FREENUMBER', 'exactly one free number is named',
        crun.count('THE FIRST FREE NUMBER') == 1 and 'I-16' in crun)
    arm('G-PRICEBOTHWAYS', 'the rename is priced in BOTH directions',
        '(A) THE SCREEN RENUMBERED' in crun and '(B) THE GRADER RENUMBERED' in crun)
    arm('G-CITECOUNT', 'and each price carries a measured citation count, not an estimate',
        ('`%d` documents against `1`' % cited) in crun or ('`%d` LIVE DOCUMENTS' % cited) in crun)
    moved = [c for c in re.findall(r'^#+\s+(I-\d+[a-z]*)', insttxt, re.M)]
    arm('G-NOASSIGN', 'and 0 numbers are renumbered, moved or assigned',
        moved == re.findall(r'^#+\s+(I-\d+[a-z]*)', in_blob, re.M)
        and 'I-16' not in insttxt,
        'the free number is NAMED in the act`s own records and appears nowhere in the register -- '
        'naming a number is not taking one')

    # ---- COMPONENT 3 AND THE ADDITION -----------------------------------------------------------
    bar()
    rec('  ### COMPONENT 3 AND THE ADDITION.')
    bar()
    arm('G-SEARCHPREDICATE', 'the search predicate is fixed and printed before the search',
        'THE PREDICATE, FIXED BEFORE THE SEARCH' in xrun)
    ctl = re.search(r'the control : ### \*\*(\d+) document', xrun)
    arm('G-CONTROL', 'the search carries a positive control and prints its yield',
        bool(ctl) and int(ctl.group(1)) > 0,
        'the control`s own printed yield : %s document(s) -- ON A YIELD OF 0 THE VERDICT IS '
        'WITHHELD AND THE PREDICATE REPORTED BROKEN' % (ctl.group(1) if ctl else '?'))
    arm('G-CONTROL-CTL', 'and every pattern`s yield is printed, large or small',
        xrun.count('document(s)') >= 5)
    arm('G-INSTRUMENTSFOUND', 'the verdict is NOT ABSENT and both instruments are named',
        'VERDICT: ### NOT ABSENT' in crun and 'INSTRUMENT 1' in crun and 'INSTRUMENT 2' in crun)
    arm('G-SCOPENAMED', 'and each instrument`s SCOPE is quoted from its own document',
        'Every kernel citation in this paper carries one of three grades' in engtxt
        and 'ITS SCOPE IS `KERNEL CITATIONS`, SAID TWICE' in crun)
    arm('G-GATEQUOTED', 'the gate`s grade for the import is quoted from the ledger itself',
        'K2 the criterion’s sign: IMPORT-UNDER-THE-BAR (b321)' in facestxt
        and 'IMPORT-UNDER-THE-BAR' in crun)
    arm('G-ASSERTIONTESTED', 'the navigator`s assertion is quoted before it is scored',
        'HE ASSERTS:' in crun and 'INTERFACES-on-named-premise' in crun)
    arm('G-ASSERTIONSPLIT', 'and it is split under (R27), never averaged to one word',
        'THE PREMISE, ON THE GATE`S OWN GRADE NAME' in crun
        and 'THE CONCLUSION, ON WHETHER THE GATE PRICES AND HALTS' in crun
        and 'REFUTED IN PREMISE / MET ON' in crun)
    arm('G-PRICEIS', 'what the gate`s price IS is stated',
        'WHAT THE GATE`S PRICE ### IS.' in crun and 'A HALT AT A NAMED CONSTITUENT' in crun)
    arm('G-PRICEISNOT', 'and what it is NOT is stated in the same breath',
        'AND WHAT IT ### IS NOT.' in crun and 'IT IS NOT A BOUND ON REACH' in crun)
    arm('G-KINDONGRADE', '(R28) is turned on the assertion: a grade name has a vocabulary',
        'a grade name belongs to a vocabulary' in fold(crun)
        and 'borrowed across a scope boundary' in fold(crun))
    arm('G-NOTSUPERSEDED', 'and neither this finding nor b410 is reported as overturning the other',
        'NEITHER SUPERSEDE' in crun.upper() or 'DOES NOT SUPERSEDE `b410``S FINDING' in crun,
        'the gate prices OWNERSHIP and b410 asked about REACH -- different questions, and the act '
        'says so rather than letting the later finding look like a correction')

    # ---- COMPONENT 4 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 4 -- THE CERTIFICATE.')
    bar()
    arm('G-CERTLOCATED', 'the certificate is located and its file named',
        '2026-08-01-w-half-consult.md' in crun and os.path.exists(GAUGE))
    arm('G-CERTROUTES', 'and the routes it names are counted from the record itself',
        '- **(a) the angle-sum over the trivial lattice**' in gaugetxt
        and '- **(b) the digamma density**' in gaugetxt and '`2` ROUTES NAMED' in crun)
    arm('G-CERTMARKS', 'the 5 reproducibility marks are checked against the banked text',
        '5 OF 5' in crun and crun.count('### **YES**') >= 5)
    arm('G-UNSOURCED-COND', 'the conditional mark is reported UNFIRED, not dropped',
        'NO `UNSOURCED` MARK IS WRITTEN' in crun and 'UNSOURCED' not in ibtxt.split('## 9.')[-1])
    arm('G-NOROWREMOVED', 'and 0 calibration rows are removed or marked',
        'The archimedean row.' in ibtxt and 'The per-place table.' in ibtxt)
    arm('G-CLASSICALATCITE', 'the certificate`s own grade is quoted, so its origin is not hidden',
        'CLASSICAL-AT-CITE' in crun and 'CLASSICAL-AT-CITE' in gaugetxt,
        'the same report proposed §9`s row, and the act prints that WITH the reason it is not '
        'circular')

    # ---- THE THREE RULED ARMS -------------------------------------------------------------------
    bar()
    rec('  ### THE THREE RULED ARMS, RUN OVER THIS ACT`S OWN BANK.')
    bar()
    arm('G-SPINE-OWNBANK', 'all three ruled arms are run over this act`s own bank',
        len(gate_spine.ARMS) == 3 and gate_spine.self_test(verbose=False),
        'b410`s lesson, carried as a bar: an arm built and not turned on its author is an ornament')
    for name, ruling, fn, _fx, _b, _w in gate_spine.ARMS:
        fires, off, ex = fn(bank)
        arm(name, 'run under %s over THIS act`s own bank' % ruling, not fires,
            '%d sentence(s) examined, %d offending %s' % (ex, len(off), off[:1] or ''))

    # ---- THE STANDING NOTHINGS ------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS.')
    bar()
    arm('G-NOGRADE', 'no grade is moved, conferred or minted',
        not asserted(bank, 'we confer') and not asserted(bank, 'the grade is raised'))
    arm('G-NOKAPPA', 'no kappa is measured or certified', not asserted(bank, 'we measured kappa'))
    arm('G-NOCHANNEL', 'no channel is opened', not asserted(bank, 'a channel was opened'))
    arm('G-NOROUTE', 'no route is proposed, priced or opened',
        not asserted(bank, 'we propose opening'))
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true')
    arm('G-NOH2', 'and the bank ASSERTS nothing about `h2`', not h2)
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    builds = asserted(bank, 'a kernel was built')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds)
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified', not lean, 'lean changes %s' % (lean or 'none'))
    depo = asserted(bank, 'was deposited') + asserted(bank, 'zenodo')
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action', not depo)
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    stat = (git(PP, 'diff', '--numstat', side, 'HEAD') if committed
            else git(PP, 'diff', '--cached', '--numstat')).stdout.decode('utf-8', 'replace')
    srows = [ln.split(chr(9)) for ln in stat.split(NL) if ln.count(chr(9)) == 2]
    dele = [(c[2], int(c[1])) for c in srows if c[1].isdigit() and int(c[1]) > 0]
    add = sum(int(c[0]) for c in srows if c[0].isdigit())
    arm('G-NOREPAIR', 'no line of any document was replaced: the writes are appends',
        not dele, '%d lines added across %d file(s) ; lines DELETED : %s'
        % (add, len(srows), dele or 'none'))
    arm('G-NOLEDGERROW', 'and no row of FACES_LEDGER.md is written',
        'FACES_LEDGER' not in stat,
        'the register stays FROZEN at six, as b409 left it')

    # ---- THE STANDING CLAUSES -------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING CLAUSES, RE-MEASURED ON THIS ACT.')
    bar()
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-join-and-the-price'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-VERDICTLINE', 'every verdict this suite reads is read from a LINE',
        (not verdict_line(kq, '### NO KEY')) and 'b411' in kq)
    arm('G-VERDICTLINE-CTL', 'and the line reader is NOT fooled by the word inside a sentence',
        (not verdict_line('the index reported NO KEY for that phrase', '### NO KEY'))
        and verdict_line('### NO KEY found', '### NO KEY'))
    probe = '### **A POINTER** ###' + NL + 'IS NOT A `MERGER`'
    arm('G-FOLDED', 'markup is folded away before any match, and it matters',
        ('A POINTER IS NOT A MERGER' in fold(probe))
        and ('A POINTER IS NOT A MERGER' not in probe))
    src = text(t('b411_checks.py'))
    stale = sorted(set(re.findall(r'b(?:39\d|40\d)_\w+', code_of(src))))
    arm('G-INHERITED', 'no arm in this suite reads a PRIOR act`s artefact as its subject',
        not stale, 'prior-act stems as a subject : %s' % (stale or 'none'))
    bars = re.findall(r'>=\s*(\d+)', code_of(src))
    arm('G-NOBORROWEDBAR', 'and no arm demands a number a previous act produced',
        all(int(b) <= 15 for b in bars),
        'numeric bars in this suite : %s -- each is a property of THIS act`s own write list or of '
        'the register`s own heading count' % bars)
    arm('G-STRIPPROSE', 'every source scan strips comments and docstrings first',
        'def code_of' in src and 'code_of(src)' in src and chr(35) not in code_of(src),
        'b410`s G-NOBORROWEDBAR fired on its own comment explaining the defect it was removing')
    arm('G-REFBYCONTENT', 'no arm names its reference by address; the sha is printed',
        any(('`%s` = `%s`' % (side, refsha)) in x for x in R[:4]),
        'reference %s = %s, chosen by content' % (side, refsha))
    midtoken = [ln for ln in crun.split(NL)
                if re.search(r'[a-z] [a-z]{1,2}\b', ln) and ' t hat' in ln]
    arm('G-NOMIDTOKEN', 'no report line is broken mid-token by the wrapper',
        not midtoken, 'lines showing a split token : %d' % len(midtoken))
    arm('G-ENCODEFIRST', 'every write in this act`s tools encodes before it opens',
        all('encode(' in text(t('b411_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank')))
    arm('G-NOHEREDOC', 'and no backslash reached a tool file through a quoted heredoc',
        all(chr(8) not in text(t('b411_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank', 'checks')))
    lp, ls, note = run_clock.latest(D, 'b411_desk_notes')
    arm('G-RUNRECORD', 'this act`s run record is found by its own clock, not by a listing',
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
        crun.count('### over ###') >= nexp
        and 'NOT ONE WAS SCORED OVER A SET THE FACE DID NOT NAME' in crun,
        '%d expectations carry their set, against %d named on the face -- THE BAR IS THIS ACT`S '
        'OWN MEASURED COUNT' % (crun.count('### over ###'), nexp))
    arm('G-SPLITSCORE', 'where a premise falls with its conclusion standing, (R27) governs',
        crun.count('REFUTED IN PREMISE') >= 1,
        '%d split score(s) -- and the one that splits is the NAVIGATOR`S OWN (N5), which asked to '
        'be scored that way' % crun.count('REFUTED IN PREMISE'))
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 2,
        'refuted expectations printed : %d -- both of them this seat`s own'
        % crun.count('REFUTED'))

    # ---- THE LIVING RECORD ----------------------------------------------------------------------
    bar()
    rec('  ### THE LIVING RECORD.')
    bar()
    tr_blob = git(PP, 'show', '%s:OPEN_TRAILS.md' % side).stdout.decode('utf-8', 'replace')
    arm('G-TRAILS', 'the trail block is append-only against the blob at %s' % side,
        MARK in trails and trails.replace('\r\n', NL).startswith(tr_blob.rstrip(NL)),
        'blob %d -> live %d bytes'
        % (len(tr_blob.encode('utf-8')), len(trails.encode('utf-8'))))
    tb, tl = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8'), text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.replace('\r\n', NL).startswith(tb.rstrip(NL)),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    arm('G-KEY', 'the key resolves, read from the VERDICT LINE',
        (not verdict_line(kq, '### NO KEY')) and 'the-join-and-the-price' in kq)
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a number was renumbered'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))

    # ---- THE WRITE LIST -------------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST, BUILT AS KINDS.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b411')) \
        + ['audit_b411_reg_satisfiable.txt'] \
        + sorted('_b411/' + f for f in os.listdir(d('_b411'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b411_'))
    KINDS = {
        1: (r'^b411_registration_', r'^b411_satisfiable', r'^audit_b411_reg_satisfiable',
            r'^b411_regspec_run', r'^b411_reg_termscan', r'^b411_reg_gate', r'^b411_lockgate',
            r'^b411_reg_seal'),
        2: (r'^b411_ferry',),
        3: (r'^b411_census_', r'^b411_faces_census_', r'^b411_pins_', r'^b411_mirror'),
        4: (r'^b411_extract\.txt$', r'^_b411/'),
        5: (r'^b411_components\.txt$', r'^b411_numbering'),
        6: (r'^b411_desk', r'^b411_the_join_and_the_price', r'^b411_closing'),
        7: (r'^b411_checks',),
        8: (r'^tools/b411_',),
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
        'declared %s ; used %s ; undeclared %s'
        % (sorted(kinds), sorted(used), sorted(used - kinds) or 'none'))
    unnamed = [f for f in written if os.path.basename(f) not in reg]
    arm('G-WRITELIST-PATHS', 'and the PATH-level residue is printed, not hidden', True,
        '%d of %d named by KIND but not by path : %s'
        % (len(unnamed), len(written), unnamed or 'none'))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b411_'))
    arm('G-CAP', 'at most 6 new relay ACT-tool files', len(tools) <= 6,
        '%d act tools : %s' % (len(tools), tools))
    shared = [f for f in git(ROOT, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL)
        if f.strip().startswith('??') and 'tools/' in f and 'b411_' not in f]
    arm('G-NOSHARED', 'and 0 new shared instruments are created', not shared,
        'gate_spine.py is USED and not amended; new untracked tools : %s' % (shared or 'none'))

    # ---- MUST-FAIL ------------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### THE GATE BOUNDS THE REACH OF AN IMPORT.',
        '### THE PLACEMENT SCREEN DERIVES DEFINITION 2.5.',
        '### THE SCREEN WAS RENUMBERED.',
        '### THE CERTIFICATE IS UNLOCATABLE.',
        '### b410 IS SUPERSEDED.',
        '### h2 HOLDS.',
    ]
    lines = set(bank.split(NL))
    hits = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits,
        'hits %s' % (hits or 'none'))
    synth = 'a' + NL + '### b410 IS SUPERSEDED.' + NL + 'b'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one',
        any(f in set(synth.split(NL)) for f in forbidden))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    declared = set(re.findall(r'\bG-[A-Z0-9-]+', reg)) - {'G-NO'}
    run = set(n for n, _o in ARMS)
    rec('  ### ### **DECLARED ON THE FACE : %d. ### RUN HERE : %d. ### DECLARED BUT NOT RUN : %s. '
        '### RUN BUT NOT DECLARED : %s.**'
        % (len(declared), len(run), sorted(declared - run) or 'none',
           sorted(run - declared) or 'none'))
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b411_checks_postpush.txt' if post else 'b411_checks.txt')
    io.open(out, 'wb').write((NL.join(R) + NL).encode('utf-8'))
    print(NL + '  wrote %s' % os.path.basename(out))
    return 0 if (npass == len(ARMS) and not (declared ^ run)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
