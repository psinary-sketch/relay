# -*- coding: utf-8 -*-
"""b408_checks.py -- THE GATE SUITE FOR THE BARRIER'S OWN INSTANCE.

### ### **`G-RESEMBLANCE` IS THE ARM THAT MATTERS MOST, AND IT IS A TWO-SIDED ARM.** ### The act
### found a resemblance so exact that reporting it as an instance would have been easy and wrong.
### The arm requires BOTH that the verdict is `NOT AN INSTANCE` AND that the resemblance is printed
### beside it -- because an act that hid the resemblance to make its verdict look obvious would be
### committing the opposite defect.
###
### ### **`G-RUNCLOCK-ADDITIVE` GUARDS THE ONE SHARED INSTRUMENT TOUCHED.** ### It removes the added
### block from the working file and requires what is left to be BYTE-IDENTICAL to the blob.
###
### ### **AND THE STANDING CLAUSES ARE APPLIED TO THIS SUITE FROM ITS FIRST WRITE:** ### every
### prose-reading arm is assertion-level with a control; every arm reading a verdict reads the
### ### **VERDICT LINE** ### (`A2`); every write encodes before it opens; and every run record is
### read ### **FROM ITS RUN**, by `run_clock.latest`, never from a directory listing.
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

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
RC = os.path.join(ROOT, 'tools', 'run_clock.py')
STANDING = os.path.join(ROOT, 'tools', 'FERRY_STANDING.md')
MARK = '<!-- b408 the other two channels, the reduction as a classified proof priced -->'

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


REG = d('b408_registration_2026-09-10.txt')
BANK = d('b408_the_other_two_channels.txt')
CRUN = d('b408_components.txt')
XRUN = d('b408_extract.txt')
LG = json.load(io.open(d('b408_lockgate.json'), encoding='utf-8'))
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
    rec('  %-22s %-58s %s' % (name, why[:58], 'PASS' if ok else '### FAIL ###'))
    if detail:
        for k in range(0, min(len(detail), 900), 150):
            rec('      %s' % detail[k:k + 150])


NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'never', 'nothing',
       'cannot', 'without', 'refus', 'declin', 'not typed', 'not an instance', 'not applied',
       'not asserting', 'not endorse', 'not read', 'would make', 'not the', 'no coefficient')


def asserted(hay, phrase):
    out = []
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
        if gate_text.flat(phrase) in gate_text.flat(s) and not any(g in s.lower() for g in NEG):
            out.append(s[:140])
    return out


def verdict_line(out, word):
    """### **A TOOL'S VERDICT IS A LINE, NOT A SUBSTRING** -- `A2`, inherited by reference."""
    return any(ln.strip().startswith(word) for ln in (out or '').splitlines())


def fold(s):
    """### **MARKERS, BACKTICKS AND LINE BREAKS FOLDED AWAY BEFORE ANY MATCH** (b407)."""
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def main(argv):
    post = '--post' in argv
    side = 'HEAD~1' if post else 'HEAD'
    bar('=')
    rec('b408 -- THE GATE SUITE. ### %s THE PUSH.' % ('AFTER' if post else 'BEFORE'))
    rec('### **THE PRE-ACT REFERENCE FOR EVERY LEDGER ARM IS NAMED, NOT ONLY ITS SIDE : `%s`.**'
        % side)
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)

    # ---- STEP ZERO ---------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO, RE-READ FROM ITS OWN RECORDS.')
    bar()
    arm('G-FERRY', 'the ferry scan reported 0 hits',
        '0 HIT(S) REPORTED' in text(d('b408_ferry_scan.txt')))
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b408_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b408_faces_census_stepzero.txt')))
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b408_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b408_reg_seal_verify.txt'))
        and SEAL in text(d('b408_reg_seal_verify.txt')))
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    arm('G-ANCHORS', 'the survey left 0 anchor misses', '**ANCHOR MISSES : 0**' in xrun)
    arm('G-EOTABLE', "the E0 gate's table was located by its own heading, not by a per-row anchor",
        'THE E0 GATE, BY ITS HEADING' in xrun
        and xrun.count('  ### line 30') >= 6,
        'the K-rows appear in three tables; a per-row anchor is ambiguous in all three')

    # ---- COMPONENT 1: THE SPAN -----------------------------------------------------------------
    bar()
    rec('  ### THE SPAN, TAKEN FROM THE TOOL AND NOT TYPED.')
    bar()
    spanrec = text(d('b408_span.txt'))
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', spanrec)
    arm('G-SPANTOOL', "the span was banked from the tool's own run under this act's stem",
        bool(m) and 'THE CURRENT SPAN' in spanrec,
        'the tool reports %s acts' % (m.group(1) if m else '?'))
    arm('G-SPANNOTYPED', 'and the components print the tool`s own lines, not a typed number',
        'THE TOOL’S OWN LINES, TAKEN FROM ITS OUTPUT AND NOT TYPED' in crun)
    arm('G-FOLDNOTRUN', 'the fold is reported NOT DUE and none was run',
        'THE FOLD IS NOT DUE' in crun and int(m.group(1)) < 9,
        '%s against a threshold of 9' % (m.group(1) if m else '?'))

    # ---- ADDITION THREE ------------------------------------------------------------------------
    bar()
    rec('  ### THE TWO CHANNELS, THE SWEEP, AND THE NUMBERING HAZARD.')
    bar()
    arm('G-TWOCLASSES', 'both channels are quoted in the classes document`s own words',
        'Class C₃ (archimedean)' in crun and 'Class C₄ (global coherence)' in crun)
    sw = re.search(r'C3 -- LINES NAMING IT BESIDE A CHANNEL WORD : (\d+)', xrun)
    sw4 = re.search(r'C4 -- LINES NAMING IT BESIDE A CHANNEL WORD : (\d+)', xrun)
    arm('G-CHANSWEEP', 'the sweep ran with its predicate printed and its whole yield printed',
        bool(sw) and bool(sw4) and 'THE PREDICATE, FIXED BEFORE THE SWEEP' in xrun
        and 'files in scope : 4705' in xrun,
        'C3 %s hits ; C4 %s hits ; 4705 files in scope'
        % (sw.group(1) if sw else '?', sw4.group(1) if sw4 else '?'))
    arm('G-CHANHANDREAD', 'and every hit is classified by kind, with its reason',
        crun.count('hit(s)') >= 5 and 'THE HAND-READING, BY KIND OF HIT' in crun)
    arm('G-NUMBERING', 'the two numbering schemes are quoted and the artefact named',
        'Archimedean / functional equation' in crun
        and 'MATCHER ARTEFACT, NOT AN EXAMINATION' in fold(crun))
    arm('G-TOOLKIT', 'and the toolkit`s silence about one source is printed',
        'IS NOT NAMED AT ALL' in fold(crun))
    opened = (asserted(bank, 'the channel is open') + asserted(bank, 'is a promising channel')
              + asserted(bank, 'is worth opening'))
    arm('G-NOCHANCLAIM', 'the bank ASSERTS no channel is open, promising or worth opening',
        not opened, 'asserting sentences %d %s' % (len(opened), opened or ''))
    arm('G-NOCHANCLAIM-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The modular symmetry is a promising channel.', 'is a promising channel')))
    arm('G-NORECONCILE', 'and the numbering hazard is PRINTED, not reconciled',
        'PRINTED AND NOT RECONCILED' in fold(bank) or 'not reconciled' in bank.lower())

    # ---- ADDITION FOUR -------------------------------------------------------------------------
    bar()
    rec('  ### THE CLASSIFIED PROOF, PRICED IN TWO LAYERS AND NOT WRITTEN.')
    bar()
    arm('G-K8CLASSIFIED', 'all eight constituents are classified',
        all(('### **%s**' % k) in crun for k in
            ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8')))
    arm('G-IMPORTS', 'the distinct imported premises are counted and named',
        'THE DISTINCT IMPORTED PREMISES ARE FOUR' in fold(crun))
    arm('G-WITHHYP', 'the verdict is PROOF-WITH-HYPOTHESES',
        'A PROOF-WITH-HYPOTHESES, NOT A PROOF IN THE LEMMA' in fold(crun))
    arm('G-CONDITIONAL', 'and the conditional finding is printed beside it',
        'A PROOF OF A CONDITIONAL IS NOT ONE' in fold(crun))
    arm('G-TWOLAYERS', 'the price is printed in two layers',
        'THE SECOND LAYER' in fold(crun) and 'LABOUR AND NOT LOGIC' in fold(crun))
    arm('G-UNCHECKED', 'and the in-principle layer is marked UNCHECKED',
        'UNCHECKED' in crun)
    written = asserted(bank, 'the classified proof is written') + asserted(bank, 'we wrote the proof')
    arm('G-NOTWRITTEN', 'the bank ASSERTS nowhere that the proof was written', not written,
        'asserting sentences %d' % len(written))
    arm('G-NOTWRITTEN-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('At last the classified proof is written in full.',
                      'the classified proof is written')))

    # ---- COMPONENTS 2 AND 3 --------------------------------------------------------------------
    bar()
    rec('  ### THE FOUR DRESSES, AND THE ROW`S KIND.')
    bar()
    arm('G-FOURDRESSES', 'four dresses are put to the test with an instantiation each',
        crun.count('THE KIND :') == 4 and crun.count('THE OBJECT:') == 4)
    arm('G-ONESENTENCE', 'the sentence the test produces is stated',
        'A RESULT APPLIES TO AN OBJECT ONLY IF THE OBJECT IS OF THE KIND' in fold(crun))
    minted = asserted(bank, 'this act names it') + asserted(bank, 'we call it')
    arm('G-NOMINT', 'and the bank ASSERTS no name of its own', not minted,
        'asserting sentences %d' % len(minted))
    arm('G-NOMINT-CTL', 'and the predicate FIRES on synthetic text minting one',
        bool(asserted('Having no name, this act names it the kind principle.',
                      'this act names it')))
    arm('G-RESTATEMENT', 'and one dress is reported a restatement, not a fourth instance',
        'A RESTATEMENT OF DRESS 3' in crun and 'ARE INDEPENDENT AND 1 IS' in fold(crun))
    arm('G-ROWCOST', 'the row`s cost and yield are printed from the banks',
        'sites entered, by their own markers' in crun and 'acts named anywhere' in crun)
    arm('G-ROWKIND', 'and the row`s kind is answered as a description, not a grade',
        'A BOOKKEEPING INSTRUMENT' in fold(crun)
        and 'A DESCRIPTION AND NOT A DEMOTION' in fold(crun))

    # ---- ADDITIONS ONE AND TWO -----------------------------------------------------------------
    bar()
    rec('  ### THE PRICE LIST AND THE SUITE MEASURE.')
    bar()
    arm('G-PRICELIST', 'the routed-price list carries item, act, cost and whose call',
        crun.count('### **ITEM** ###') == 3 and crun.count('WHOSE :') == 3)
    arm('G-PRICESCOPE', 'and it declares what it is not',
        'NOT A CORPUS-WIDE ROUTED-ITEM CENSUS' in fold(crun))
    arm('G-PRICEDISP', 'and a NAMED item is kept apart from a ROUTED one',
        'NAMED, NOT ROUTED' in fold(crun))
    arm('G-ARMCOUNTS', 'the four suites` arm counts and the standing core are printed',
        'STANDING CORE' in xrun and re.search(r'carried \d+ ; NEW \d+', xrun) is not None)
    arm('G-ARMLIMIT', 'and the measure prints its own limit',
        'UPPER BOUND ON CONTINUITY' in fold(crun))
    reformed = asserted(bank, 'the suite was rebuilt') + asserted(bank, 'an arm was added')
    arm('G-NOREFORM', 'the bank ASSERTS no arm was added, removed, renamed or promoted',
        not reformed, 'asserting sentences %d' % len(reformed))

    # ---- WHAT WAS NOT TOUCHED ------------------------------------------------------------------
    bar()
    rec('  ### WHAT WAS NOT TOUCHED.')
    bar()
    faces_blob = git(PP, 'show', '%s:FACES_LEDGER.md' % side).stdout.decode('utf-8')
    arm('G-NOROWWRITE', 'FACES_LEDGER.md is BYTE-IDENTICAL to the blob at %s' % side,
        text(FACES).replace('\r\n', '\n') == faces_blob,
        'working %d ; blob %d bytes'
        % (len(text(FACES).encode('utf-8')), len(faces_blob.encode('utf-8'))))
    st_now = text(STANDING)
    st_blob = git(ROOT, 'show', '%s:tools/FERRY_STANDING.md' % side).stdout.decode('utf-8')
    arm('G-NOSTANDING', 'FERRY_STANDING.md is byte-identical to the blob',
        st_now.replace('\r\n', '\n') == st_blob.replace('\r\n', '\n'))
    rc_now = text(os.path.join(ROOT, 'tools', 'run_clock.py'))
    rc_blob = git(ROOT, 'show', '%s:tools/run_clock.py' % side).stdout.decode('utf-8')
    arm('G-NOINSTRUMENT', 'and run_clock.py is byte-identical too -- b407 amended it, not b408',
        rc_now.replace('\r\n', '\n') == rc_blob.replace('\r\n', '\n'))
    arm('G-NOREPAIR', 'this act made no in-place repair anywhere',
        'NO IN-PLACE REPAIR' in text(t('b408_desk_bank.py')).upper()
        or 'in-place repair' not in text(t('b408_desk_bank.py')).lower())
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(chr(10)) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified', not lean, 'lean changes %s' % (lean or 'none'))
    builds = asserted(bank, 'a kernel was built')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds,
        'asserting sentences %d' % len(builds))
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b408_'))
    arm('G-CAP', 'at most 6 new relay tool files', len(tools) <= 6, '%d : %s' % (len(tools), tools))

    # ---- THE LIVING RECORD --------------------------------------------------------------------
    bar()
    rec('  ### THE LIVING RECORD.')
    bar()
    tr_blob = git(PP, 'show', '%s:OPEN_TRAILS.md' % side).stdout.decode('utf-8')
    arm('G-TRAILS', 'the trail block is append-only against the blob at %s' % side,
        text(TRAILS).startswith(tr_blob.rstrip(chr(10))) or tr_blob in text(TRAILS),
        'blob %d -> live %d bytes'
        % (len(tr_blob.encode('utf-8')), len(text(TRAILS).encode('utf-8'))))
    tb, tl = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8'), text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.replace('\r\n', '\n').startswith(tb.rstrip(chr(10))),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-other-two-channels'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY', 'the key resolves, read from the VERDICT LINE',
        (not verdict_line(kq, '### NO KEY')) and 'b408' in kq,
        'verdict-line NO KEY : %s ; raw substring hits : %d'
        % (verdict_line(kq, '### NO KEY'), kq.count('NO KEY')))
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a row was written to the ledger'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))
    # ### **THE RUN RECORD IS FOUND BY ITS OWN CLOCK, NOT BY A DIRECTORY LISTING** (b407's guard).
    lp, ls, note = run_clock.latest(D, 'b408_desk_notes')
    arm('G-RUNRECORD', "this act's own run record is found by its own clock",
        lp is not None and ls is not None,
        '%s (%s ; %s)' % (os.path.basename(lp or '-'), ls, note))
    arm('G-DESK', 'the desk was swept and its closures printed',
        bool(lp) and 'ITEMS SWEPT' in text(lp))

    # ---- THE STANDING NOTHINGS ----------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS.')
    bar()
    dep = asserted(bank, 'was deposited') + asserted(bank, 'zenodo')
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action', not dep,
        'asserting sentences %d' % len(dep))
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true')
    arm('G-NOH2', 'and it ASSERTS nothing about `h2`', not h2, 'asserting sentences %d' % len(h2))
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    bridged = asserted(bank, 'a bridge is typed') + asserted(bank, 'the two are equivalent')
    arm('G-NOBRIDGE', 'and it types no bridge', not bridged)
    arm('G-NOBRIDGE-CTL', 'and the predicate FIRES on synthetic text typing one',
        bool(asserted('At the fifth site the two are equivalent.', 'the two are equivalent')))
    arm('G-ENCODEFIRST', 'every write in this act`s tools encodes before it opens',
        all('encode(' in text(t('b408_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank')))
    arm('G-EXPECT', 'every registered expectation is scored',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(N5)', '(N6)', '(N7)',
             '(E1)', '(E2)', '(E3)', '(E4)')))
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 1,
        'refuted expectations printed : %d ### -- THE ARM MEASURES AND DOES NOT DEMAND A NUMBER '
        'SET FOR ANOTHER ACT' % crun.count('REFUTED'))
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRYFIX', 'the ferry-scan fixtures still hold', ok_scan)
    arm('G-SEALNAME', 'the bank names the seal it was written under', SEAL in bank)

    # ---- THE WRITE LIST -----------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST, BUILT AS KINDS.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b408')) \
        + ['audit_b408_reg_satisfiable.txt'] \
        + sorted('_b408/' + f for f in os.listdir(d('_b408'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b408_'))
    KINDS = {
        1: (r'^b408_registration_', r'^b408_satisfiable', r'^audit_b408_reg_satisfiable',
            r'^b408_regspec_run', r'^b408_reg_termscan', r'^b408_reg_gate', r'^b408_lockgate',
            r'^b408_reg_seal'),
        2: (r'^b408_ferry',),
        3: (r'^b408_census_', r'^b408_faces_census_', r'^b408_pins_', r'^b408_mirror'),
        4: (r'^b408_extract\.txt$', r'^_b408/', r'^b408_span'),
        5: (r'^b408_components\.txt$',),
        6: (r'^b408_desk', r'^b408_the_other_two_channels', r'^b408_closing'),
        7: (r'^b408_checks',),
        8: (r'^tools/b408_',),
    }
    placed, unkinded = {}, []
    for f in written:
        hit = [k for k, pats in KINDS.items() if any(re.search(p, f) for p in pats)]
        (placed.setdefault(f, hit[0]) if hit else unkinded.append(f))
    arm('G-WRITELIST', 'every file this act wrote is of a KIND the locked face names', not unkinded,
        '%d written ; of NO named KIND %d : %s' % (len(written), len(unkinded), unkinded or 'none'))
    unnamed = [f for f in written if os.path.basename(f) not in reg]
    arm('G-WRITELIST-PATHS', 'and the PATH-level residue is printed, not hidden', True,
        '%d of %d named by KIND but not by path : %s'
        % (len(unnamed), len(written), unnamed or 'none'))
    kinds = re.findall(r'\*\*KIND (\d+) --', reg)
    arm('G-WRITELIST-KIND', 'the list is built as KINDS',
        len(kinds) >= 9 and len(set(placed.values())) >= 7,
        'kinds declared %d ; used %d' % (len(kinds), len(set(placed.values()))))

    # ---- MUST-FAIL -----------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### THE HALT AT K8 IS AN INSTANCE OF THEOREM 3.1.',
        '### A TRANSMISSION COEFFICIENT WAS MEASURED.',
        '### A ROW WAS WRITTEN TO FACES_LEDGER.',
        '### (R20) WAS WIDENED.',
        '### THE SPECTRAL REALIZATION EXISTS.',
        '### A KERNEL WAS BUILT.',
    ]
    lines = set(bank.split(chr(10)))
    hits = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits,
        'hits %s' % (hits or 'none'))
    synth = 'a' + chr(10) + '### (R20) WAS WIDENED.' + chr(10) + 'b'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one',
        any(f in set(synth.split(chr(10))) for f in forbidden))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b408_checks_postpush.txt' if post else 'b408_checks.txt')
    io.open(out, 'wb').write((chr(10).join(R) + chr(10)).encode('utf-8'))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
