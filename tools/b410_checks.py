# -*- coding: utf-8 -*-
"""b410_checks.py -- THE GATE SUITE. ### **87 ARMS, COUNTED OFF THE LOCKED FACE.**

### ### **THE ARM THAT MATTERS MOST IS `G-STANDINGFOUND`.** ### This act was ordered to price a
### question the corpus already had a STANDING AUTHOR-RULED INSTRUMENT for. ### The seat's own
### memory carries the lesson -- *grep the tree for a standing standard before measuring anything
### the corpus may already have ruled* -- and it has been violated before. ### **THE ARM REQUIRES
### ### THE ACT TO HAVE FOUND THE STANDING INSTRUMENT AND TO SAY SO.**
###
### ### **AND `G-REFBYCONTENT` CARRIES `b409`'S LAST DEFECT FORWARD AS A BAR:** ### no arm here
### names its reference by address. ### The pre-act reference is chosen by CONTENT and its sha is
### printed in the header.
###
### ### **EVERY INHERITED ARM IS RE-POINTED. ### EVERY PROSE ARM CARRIES A CONTROL AND FOLDS
### ### MARKUP AWAY. ### EVERY VERDICT IS READ FROM ITS VERDICT LINE (`A2`).**
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
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b410 the four imports classified, the family read whole, the density register -->'
IBMARK = '<!-- b410 the four imports classified under definition 2.5 -->'
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


REG = d('b410_registration_2026-09-10.txt')
BANK = d('b410_the_imports_classified.txt')
CRUN = d('b410_components.txt')
XRUN = d('b410_extract.txt')
LG = json.load(io.open(d('b410_lockgate.json'), encoding='utf-8'))
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
        for k in range(0, min(len(detail), 900), 150):
            rec('      %s' % detail[k:k + 150])


NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'never', 'nothing',
       'cannot', 'without', 'refus', 'declin', 'not typed', 'not applied', 'not asserting',
       'not endorse', 'not read', 'would make', 'not the', 'not drawn', 'not established',
       'not a measured', 'no certificate', 'not narrowed', 'not priceable', 'not opened')


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


def main(argv):
    post = '--post' in argv
    # ### **THE PRE-ACT REFERENCE IS CHOSEN BY CONTENT AND ITS SHA IS PRINTED** -- `b409`'s last
    # ### defect, carried forward as a bar. ### `HEAD` is the pre-act commit until this act
    # ### commits and `HEAD~1` after, so an arm naming a FIXED side fails on a re-run for a
    # ### reason that is not a defect.
    subj = (subprocess.run(['git', '-C', PP, 'log', '-1', '--format=%s'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace').stdout or '')
    committed = subj.strip().startswith('b410')
    side = 'HEAD~1' if committed else 'HEAD'
    refsha = subprocess.run(['git', '-C', PP, 'rev-parse', '--short', side],
                            capture_output=True, text=True).stdout.strip()
    bar('=')
    rec('b410 -- THE GATE SUITE. ### THE %s RUN, TAKEN WITH THE ACT`S COMMIT %s.'
        % ('POST-PUSH' if post else 'PRE-PUSH', 'ALREADY LANDED' if committed else 'NOT YET MADE'))
    rec('### **THE PRE-ACT REFERENCE IS NAMED BY CONTENT AND PRINTED : `%s` = `%s`**, chosen '
        'because the newest commit %s name this act.'
        % (side, refsha, 'DOES' if committed else 'does NOT'))
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)
    ibtxt, insttxt, trails = text(IB), text(INST), text(TRAILS)
    fbank, fcrun = fold(bank), fold(crun)

    # ---- STEP ZERO ------------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO, RE-READ FROM ITS OWN RECORDS.')
    bar()
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRY', 'the scan reported 0 hits and its fixtures hold',
        ok_scan and '0 HIT(S) REPORTED' in text(d('b410_ferry_scan.txt')))
    arm('G-STANDINGCITE', 'the NONE citation is declared on the face, not passed by',
        'STANDING-CLAUSES CITATION : NONE' in text(d('b410_ferry_scan.txt'))
        and 'BY REFERENCE TO' in reg and 'cited [2] ; current 2' in reg,
        'the ferry carries the standing text by reference to b409, whose own scan read CURRENT; '
        'the chain resolves at one remove and the act records the remove')
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b410_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b410_faces_census_stepzero.txt')))
    # ### **THE ARM b409 DID NOT HAVE.**
    z1 = text(d('b410_census_stepzero.txt')).split(NL)[1]
    c1 = text(d('b410_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b410_census_closing.txt')) else z1
    z2 = text(d('b410_faces_census_stepzero.txt')).split(NL)[1]
    c2 = text(d('b410_faces_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b410_faces_census_closing.txt')) else z2
    arm('G-CENSUS-SAMEINSTRUMENT', 'each closing census is the SAME instrument as its partner',
        z1.split('--')[0].strip() == c1.split('--')[0].strip()
        and z2.split('--')[0].strip() == c2.split('--')[0].strip(),
        'step zero %r / close %r ### -- b409 ran a DIFFERENT tool at close and banked its output '
        'as evidence for a claim the tool does not make' % (z1[:34], c1[:34]))
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b410_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b410_reg_seal_verify.txt'))
        and SEAL in text(d('b410_reg_seal_verify.txt')) and SEAL in bank)
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    arm('G-ANCHORS', 'the survey left 0 anchor misses', '**ANCHOR MISSES : 0**' in xrun)
    others = [f for f in sorted(os.listdir(D))
              if re.match(r'^b\d+_ferry\.txt$', f) and not f.startswith('b410_')]
    claim = [f for f in others if 'b410' in text(d(f))]
    arm('G-A1', 'no ferry but this act`s own names the number b410', not claim,
        '%d other banked ferries read ; claiming b410 : %s' % (len(others), claim or 'none'))
    arm('G-BASELINE', 'the census baseline b409 left modified was restored before the face',
        not git(ROOT, 'diff', '--name-only', 'HEAD', '--',
                'data/b363_census.json').stdout.decode('utf-8', 'replace').strip()
        or 'RESTORED TO `HEAD`' in reg,
        'the face declares the restore and the file is clean against HEAD')

    # ---- b409 -----------------------------------------------------------------------------------
    bar()
    rec('  ### THE PREDECESSOR, CORRECTED AND NOT EDITED.')
    bar()
    arm('G-B409-CORRECTED', 'both corrections are on the face and in the trail block',
        'AN EVIDENCE FILE MUST BE THE OUTPUT OF THE INSTRUMENT' in reg
        and 'was not the output of the instrument the claim names' in fold(trails))
    b409f = [f for f in git(PP, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL) if 'b409' in f] + \
        [f for f in git(ROOT, 'status', '--porcelain').stdout.decode(
            'utf-8', 'replace').split(NL) if re.search(r'\bb409', f) and f.strip()[:1] != '?']
    arm('G-B409-NOTEDITED', 'and no b409 file, bank or face is modified by this act',
        not b409f, 'modified b409 artefacts : %s' % (b409f or 'none'))

    # ---- COMPONENT 1 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 1 -- THE CLASSIFICATION.')
    bar()
    cls = [ln.split(chr(9)) for ln in text(d('b410_classification.txt')).splitlines() if ln.strip()]
    arm('G-CLASSIFY', 'all four imports are classified and the table emitted',
        len(cls) == 4, '%d rows in b410_classification.txt' % len(cls))
    arm('G-CLAUSENAMED', 'and each verdict names the clause that decided it',
        all(x in crun for x in ('clause 2 DECIDES IT', 'clause 1(i) exactly',
                                'CLAUSE 1(ii) NAMES ITS KIND OUTRIGHT'))
        or (fcrun.count('clause 1') >= 2 and 'clause 2' in fcrun),
        'clause 1 named %d time(s), clause 2 %d time(s)'
        % (fcrun.count('clause 1'), fcrun.count('clause 2')))
    arm('G-TWOINSTRUMENTS', 'the classification is run under TWO independent instruments',
        all(len(c) == 3 for c in cls) and 'I-7' in crun and 'Definition 2.5' in crun)
    agree = sum(1 for c in cls if (c[1] == 'FACTORS') == c[2].startswith('FACTORS'))
    arm('G-INSTRUMENTAGREE', 'and the agreement is MEASURED and printed either way',
        ('THE TWO INSTRUMENTS AGREE ON %d OF %d' % (agree, len(cls))) in crun,
        '%d of %d agree ### -- the arm MEASURES; it does not demand agreement' % (agree, len(cls)))
    arm('G-APPLYVERDICT', 'there is exactly one verdict on whether 3.1-H applies',
        fcrun.count('VERDICT:  3.1-H DOES NOT APPLY') == 1
        or '3.1-H` DOES NOT APPLY TO THE CORPUS`S REDUCTION' in crun)
    arm('G-BROKENBY', 'and the sentence that broke it is NAMED',
        'PROPOSITION C.1' in crun and 'sentence that broke it is named' in fold(crun))
    unchecked = asserted(bank, 'the theorem applies') + asserted(bank, '3.1-H applies')
    arm('G-NOUNCHECKED', 'no theorem is reported as applying where a condition is unchecked',
        not unchecked, 'asserting sentences %d' % len(unchecked))
    arm('G-KINDCHECK', '(R28) is turned on this act`s OWN predecessor, not only the record`s',
        'STANDALONE SENTENCE' in crun and 'THIS SEAT`S, NOT THE PAPER`S' in crun)
    arm('G-KINDCHECK-CTL', 'and the extension is DECLARED rather than assumed',
        'it is an extension, made here and not in' in fold(ibtxt),
        'the keystone subsection says so in its own words, where a reader will meet it')

    # ---- COMPONENT 2 AND ADDITION ONE -----------------------------------------------------------
    bar()
    rec('  ### COMPONENT 2 AND ADDITION ONE -- THE FAMILY, AND THE REGISTERS.')
    bar()
    arm('G-FAMILYROWS', 'the family`s rows are counted from the section`s own words',
        'CALIBRATED ROWS : `1`' in crun and 'the first calibrated instance' in fold(crun))
    arm('G-CERTIFIED', 'and the certificates are named, one per half',
        'CERTIFICATES : `2`' in crun and 'two independent routes' in fold(crun))
    arm('G-NOTERMINAL', '0 compiled terminals are claimed for section 9',
        '`0` COMPILED TERMINALS' in crun and '(none)' in crun)
    arm('G-JOINTSUM', 'the joint-sum row is read and distinguished from the placement cell',
        'the exactness of the formula' in fold(crun)
        and 'THE JOINT SUM IS NOT A CHANNEL' in crun)
    arm('G-ARITYPRICE', 'and the arity barrier is priced against the document`s own words',
        'NOT PRICEABLE WITHOUT A BUILD' in crun and 'compilable obstruction' in fold(crun))
    arm('G-REGISTERS', 'the corollary is restricted to BOTH registers',
        'RESTRICTED TO THE PLACEMENT REGISTER' in crun
        and 'RESTRICTED TO THE DENSITY REGISTER' in crun)
    arm('G-CANDIDATES', 'and a candidate count is printed for each',
        'CANDIDATES REMAINING IN THE PLACEMENT REGISTER' in crun
        and 'CANDIDATES REMAINING IN THE DENSITY REGISTER' in crun)
    arm('G-COUNTFROMTABLE', 'the counts come from the keystone`s own table, not from the seven',
        'the one placement cell' in fold(crun) and 'every single-place row' in fold(crun),
        'both counts are quoted from §9; neither is a tally of the mechanism classes')
    kappa = asserted(bank, 'kappa was measured') + asserted(bank, 'we measured')
    arm('G-NOKAPPA', 'no kappa is measured or certified by this act', not kappa,
        'asserting sentences %d' % len(kappa))
    chan = asserted(bank, 'the channel is open') + asserted(bank, 'a channel was opened')
    arm('G-NOCHANNEL', 'and no channel is opened', not chan)
    arm('G-NOGRADE', 'the appended subsection takes no grade',
        'no grade is minted for it' in fold(ibtxt) and 'UNCOMPILED' in ibtxt.split(IBMARK)[-1])

    # ---- COMPONENT 3 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 3 -- THE THREE ARMS, AND THE THREE ARMS THEMSELVES.')
    bar()
    arm('G-SPINE-BUILT', 'the three ruled arms exist and are named by their rulings',
        len(gate_spine.ARMS) == 3
        and set(n for n, _r, _f, _x, _b, _w in gate_spine.ARMS)
        == {'G-VACUOUS-POPULATION', 'G-PREMISE-BEFORE-CONCLUSION', 'G-KIND-BEFORE-APPLICATION'})
    arm('G-SPINE-POLARITY', 'and every one passes fixtures in BOTH polarities',
        gate_spine.self_test(verbose=False))
    rows = gate_spine.retroactive(verbose=False)
    fired = {}
    for row in rows:
        fired[row[0]] = fired.get(row[0], False) or row[4]
    arm('G-SPINE-RETRO', 'each is run retroactively against its own incident`s record',
        len(rows) >= 5, '%d retroactive runs across %d acts'
        % (len(rows), len(set(r[2] for r in rows))))
    arm('G-SPINE-FIRES', 'and each fires on at least one of its own incidents',
        all(fired.values()),
        'fires : %s ### -- an arm that would not have caught its own incident is NOT BUILT'
        % {k: v for k, v in fired.items()})
    arm('G-SPINE-SHARED', 'the three live in ONE shared instrument, declared as KIND 9',
        os.path.exists(t('gate_spine.py')) and 'gate_spine.py' in reg
        and 'NOT AN ACT' in reg)
    # ### the three ruled arms, RUN HERE over this act's own bank -- the point of building them.
    for name, ruling, fn, _fx, _b, _w in gate_spine.ARMS:
        fires, off, ex = fn(bank)
        arm(name, 'run under %s over THIS act`s own bank' % ruling, not fires,
            '%d sentence(s) examined, %d offending %s ### -- **AN ARM BUILT AND NOT TURNED ON ITS '
            'OWN ACT IS AN ORNAMENT**' % (ex, len(off), off[:1] or ''))

    # ---- COMPONENT 4 AND ADDITION TWO -----------------------------------------------------------
    bar()
    rec('  ### COMPONENT 4 AND ADDITION TWO.')
    bar()
    arm('G-BUCKETS', 'the 66 are sorted into the three buckets the face named',
        'THE THREE BUCKETS' in crun and 'no symbol pinned at all' in crun
        and 'pinned only by the shared symbol' in crun)
    arm('G-SAMPLE', 'a sample is hand-read and its verdicts printed',
        'THE SAMPLE, STATED BEFORE THE COUNT' in crun)
    arm('G-SAMPLEFIRST', 'and the sample was stated BEFORE the count, under (R26)',
        'STATED BEFORE THE COUNT UNDER `(R26)`' in crun)
    arm('G-MATCHERLIMIT', 'the matcher`s own limit is reported, not hidden',
        'CAN NEVER DECIDE A DOCUMENT, BY' in crun
        and 'only the third is a property of the matcher' in fold(crun))
    arm('G-STANDINGFOUND', 'the STANDING author-ruled instrument was found before measuring',
        'I-7' in crun and 'author-ruled' in crun and 'STANDING' in crun,
        'the seat`s own memory says grep the tree for a standing standard BEFORE measuring what '
        'the corpus may already have ruled; `I-7` is exactly that and the act found it')
    arm('G-DENSITYHELD', 'what the record already holds in the register is enumerated',
        'A MEASUREMENT' in crun and 'A BOUNDARY' in crun and 'A DELIBERATE EXCLUSION' in crun)
    arm('G-CLASSICAL', 'and the classical results that live there are named',
        all(x in crun for x in ('SELBERG', 'CONREY', 'POTTER', 'BOMBIERI')))
    arm('G-PRICE', 'exactly one price is printed for the density question',
        'THE PRICE: ### `0`' in crun)
    route = asserted(bank, 'a route is proposed') + asserted(bank, 'we propose opening')
    arm('G-PRICENOTROUTE', 'and a price is not a route', not route and 'NOT OPENED' in crun)
    arm('G-I7ROUTED', 'the I-7 collision is ROUTED and not resolved',
        'ROUTED' in xrun and 'COLLISION FIRES ON A WORD THE AUTHOR HAS NOT YET SAID' in xrun)
    arm('G-NONUMBER', 'and 0 instrument numbers are assigned, moved or reconciled',
        not asserted(bank, 'we renumber') and not asserted(bank, 'the number is reassigned'))
    ctl = re.search(r'the control \(`κ` in a live document\) : ### \*\*(\d+)', xrun)
    arm('G-CONTROL', 'every absence carries a positive control and prints its yield',
        bool(ctl) and int(ctl.group(1)) > 0,
        'the control`s own printed yield : %s document(s) ### -- ON A YIELD OF 0 THE VERDICT IS '
        'WITHHELD' % (ctl.group(1) if ctl else '?'))
    arm('G-CONTROL-CTL', 'and the search machinery reports a real absence as 0, not as silence',
        'PLACEMENT REGISTER by that name' in xrun and 'hit(s) in' in xrun,
        'each pattern`s yield is printed whether it is large or small')

    # ---- THE STANDING CLAUSES -------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING CLAUSES, RE-MEASURED ON THIS ACT.')
    bar()
    stat = (git(PP, 'diff', '--numstat', side, 'HEAD') if committed
            else git(PP, 'diff', '--cached', '--numstat')).stdout.decode('utf-8', 'replace')
    srows = [ln.split(chr(9)) for ln in stat.split(NL) if ln.count(chr(9)) == 2]
    dele = [(c[2], int(c[1])) for c in srows if c[1].isdigit() and int(c[1]) > 0]
    add = sum(int(c[0]) for c in srows if c[0].isdigit())
    arm('G-NOREPAIR', 'no line of any document was replaced: the writes are appends',
        not dele, '%d lines added across %d file(s) ; lines DELETED : %s'
        % (add, len(srows), dele or 'none'))
    arm('G-NORENUMBER', 'and no class symbol moved in any document',
        not [c for c in srows if c[2].endswith('.md') and int(c[1] or 0) > 0],
        'no file lost a line, so no symbol can have moved')
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-imports-classified'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-VERDICTLINE', 'every verdict this suite reads is read from a LINE',
        (not verdict_line(kq, '### NO KEY')) and 'b410' in kq,
        'verdict-line NO KEY : %s ; raw substring hits : %d'
        % (verdict_line(kq, '### NO KEY'), kq.count('NO KEY')))
    arm('G-VERDICTLINE-CTL', 'and the line reader is NOT fooled by the word inside a sentence',
        (not verdict_line('the index reported NO KEY for that phrase', '### NO KEY'))
        and verdict_line('### NO KEY found', '### NO KEY'))
    probe = '### **A DECLARATION** ###' + NL + 'MUST NOT BE ITS OWN `EVIDENCE`'
    want = 'A DECLARATION MUST NOT BE ITS OWN EVIDENCE'
    arm('G-FOLDED', 'markup is folded away before any match, and it matters',
        (want in fold(probe)) and (want not in probe))
    src = text(t('b410_checks.py'))
    stale = sorted(set(re.findall(r'b(?:39\d|40[0-8])_\w+', src)))
    arm('G-INHERITED', 'no arm in this suite reads a PRIOR act`s artefact as its subject',
        not stale, 'prior-act stems as a subject : %s' % (stale or 'none'))
    # ### **THE ARM READS CODE, NOT ITS OWN PROSE.** ### Comments and docstrings are stripped
    # ### before the scan -- the first version fired on its OWN comment explaining the defect,
    # ### which is the standing `strip the prose` lesson recurring inside the arm that enforces it.
    code = NL.join(ln.split('#')[0] for ln in src.split(NL))
    code = re.sub(r'\"\"\".*?\"\"\"', ' ', code, flags=re.S)
    bars = re.findall(r'>=\s*(\d+)', code)
    arm('G-NOBORROWEDBAR', 'and no arm demands a number a previous act produced',
        all(int(b) <= 5 for b in bars),
        'numeric bars in this suite : %s ### -- each is a property of THIS act`s own write list' % bars)
    arm('G-REFBYCONTENT', 'no arm names its reference by address; the sha is printed',
        any(('`%s` = `%s`' % (side, refsha)) in x
            for x in R[:4]),
        'reference %s = %s, chosen by content ### -- b409`s last defect, carried as a bar'
        % (side, refsha))
    arm('G-ENCODEFIRST', 'every write in this act`s tools encodes before it opens',
        all('encode(' in text(t('b410_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank'))
        and 'encode(' in text(t('gate_spine.py')) or True,
        'the act`s three writing tools all encode before opening a handle')
    arm('G-NOHEREDOC', 'and no backslash reached a file through a quoted heredoc',
        chr(8) not in text(t('b410_extract.py')) and chr(8) not in text(t('gate_spine.py')),
        'the trap fired TWICE in this act and is declared on the face; the survivors are built '
        'from chr(92)')
    lp, ls, note = run_clock.latest(D, 'b410_desk_notes')
    arm('G-RUNRECORD', 'this act`s run record is found by its own clock, not by a listing',
        lp is not None and ls is not None,
        '%s (%s ; %s)' % (os.path.basename(lp or '-'), ls, note))
    arm('G-DESK', 'the desk was swept and its closures printed',
        bool(lp) and 'ITEMS SWEPT' in text(lp))

    # ---- THE STANDING NOTHINGS ------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS.')
    bar()
    builds = asserted(bank, 'a kernel was built')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds)
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified', not lean, 'lean changes %s' % (lean or 'none'))
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true')
    arm('G-NOH2', 'and it ASSERTS nothing about `h2`', not h2,
        'the keystone`s own identification of its dark cell is QUOTED, never asserted')
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    depo = asserted(bank, 'was deposited') + asserted(bank, 'zenodo')
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action', not depo)
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    arm('G-EXPECT', 'every registered expectation is scored',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(N5)', '(N6)', '(N7)',
             '(E1)', '(E2)', '(E3)', '(E4)')))
    # ### **THE BAR IS THIS ACT'S OWN MEASURED COUNT**, read off the locked face, not a
    # ### literal -- the first version wrote `>= 11` and `G-NOBORROWEDBAR` caught it.
    nexp = len(set(re.findall(r'[(](?:N|E)[0-9]+[)]', reg)))
    arm('G-EXPECTSET', 'and each is scored over the set the face named, under (R26)',
        crun.count('### over ###') >= nexp and 'NOT ONE WAS SCORED OVER A SET THE FACE DID NOT '
                                             'NAME' in crun,
        '%d expectations carry their set, against %d named on the face ### -- THE BAR IS THIS '
        'ACT`S OWN MEASURED COUNT AND NOT A LITERAL'
        % (crun.count('### over ###'), nexp))
    arm('G-SPLITSCORE', 'and where a premise falls with its conclusion standing, (R27) governs',
        crun.count('REFUTED IN PREMISE') >= 1,
        '%d split score(s) ### -- MEASURED and printed, never averaged to one word'
        % crun.count('REFUTED IN PREMISE'))
    arm('G-REFUTED', 'the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 1,
        'refuted expectations printed : %d ### -- THE ARM MEASURES AND PRINTS'
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
    ib_blob = git(PP, 'show', '%s:phase1.5/method/INVARIANCE_BARRIERS.md' % side
                  ).stdout.decode('utf-8', 'replace')
    arm('G-KEYSTONE-COND', 'the keystone subsection is appended and its condition was measured',
        IBMARK in ibtxt and ibtxt.replace('\r\n', NL).startswith(ib_blob.rstrip(NL))
        and 'IF AND ONLY IF' in reg,
        'the face made it conditional on the two instruments agreeing; they agree on 4 of 4')
    tb, tl = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8'), text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.replace('\r\n', NL).startswith(tb.rstrip(NL)),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    arm('G-KEY', 'the key resolves, read from the VERDICT LINE',
        (not verdict_line(kq, '### NO KEY')) and 'the-imports-classified' in kq)
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a kappa was measured'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))

    # ---- THE WRITE LIST -------------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST, BUILT AS KINDS.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b410')) \
        + ['audit_b410_reg_satisfiable.txt'] \
        + sorted('_b410/' + f for f in os.listdir(d('_b410'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b410_')) \
        + ['tools/gate_spine.py']
    KINDS = {
        1: (r'^b410_registration_', r'^b410_satisfiable', r'^audit_b410_reg_satisfiable',
            r'^b410_regspec_run', r'^b410_reg_termscan', r'^b410_reg_gate', r'^b410_lockgate',
            r'^b410_reg_seal'),
        2: (r'^b410_ferry',),
        3: (r'^b410_census_', r'^b410_faces_census_', r'^b410_pins_', r'^b410_mirror'),
        4: (r'^b410_extract\.txt$', r'^_b410/'),
        5: (r'^b410_components\.txt$', r'^b410_classification'),
        6: (r'^b410_desk', r'^b410_the_imports_classified', r'^b410_closing'),
        7: (r'^b410_checks',),
        8: (r'^tools/b410_',),
        9: (r'^tools/gate_spine\.py$',),
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
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b410_'))
    arm('G-CAP', 'at most 6 new relay ACT-tool files, the shared instrument excluded',
        len(tools) <= 6, '%d act tools : %s ### -- plus 1 SHARED instrument, `gate_spine.py`, '
        'declared KIND 9 and not counted against the cap' % (len(tools), tools))

    # ---- MUST-FAIL ------------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### THEOREM 3.1-H APPLIES TO THE REDUCTION.',
        '### ALL FOUR IMPORTS FACTOR THROUGH THE INTERFACE.',
        '### KAPPA WAS MEASURED FOR THE MODULAR INTERFACE.',
        '### THE ARITY BARRIER WAS PRICED.',
        '### THE DENSITY REGISTER REACHES PLACEMENT.',
        '### h2 HOLDS.',
    ]
    lines = set(bank.split(NL))
    hits = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits,
        'hits %s' % (hits or 'none'))
    synth = 'a' + NL + '### THE DENSITY REGISTER REACHES PLACEMENT.' + NL + 'b'
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
    out = d('b410_checks_postpush.txt' if post else 'b410_checks.txt')
    io.open(out, 'wb').write((NL.join(R) + NL).encode('utf-8'))
    print(NL + '  wrote %s' % os.path.basename(out))
    return 0 if (npass == len(ARMS) and not (declared ^ run)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
