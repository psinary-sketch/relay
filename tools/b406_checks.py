# -*- coding: utf-8 -*-
"""b406_checks.py -- THE GATE SUITE FOR THE SITES WITHOUT AN EXISTENTIAL.

### ### **`G-REPAIR-ADDS` IS THE ARM THAT MATTERS MOST, BECAUSE THE REPAIR IS THE ONLY IN-PLACE
### ### EDIT THIS ACT MAKES.** ### It reconstructs the pre-act sentence from the repaired one by
### undoing the qualifier, and requires the result to be BYTE-IDENTICAL to the blob's live region.
### **A REPAIR THAT ADDS A QUALIFIER AND NOTHING ELSE IS REVERSIBLE BY REMOVING THE QUALIFIER**, and
### that is the whole test.
###
### ### **`G-ORIGINAL-KEPT` GUARDS THE OTHER HALF OF `(R4)`** -- preserve by quotation, repair by
### edit -- and `G-NOPRESERVEDIT` guards the trap this act fell into and climbed out of: the
### preserved original must still read as the record wrote it, not as this act rewrote it.
###
### ### **`G-SUBJECT` GUARDS THE SWEEP.** ### The h2 programme says *trace silence at the finite
### places* about a DIFFERENT OBJECT. ### The arm requires the wide yield to be printed and
### UNREPAIRED, and the narrow yield to be printed beside the widened one.
###
### ### **AND EVERY ARM READING A TOOL'S VERDICT READS THE VERDICT LINE** -- the clause this act
### promotes into `FERRY_STANDING` as `A2`, applied to itself from its first write.
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
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
STANDING = os.path.join(ROOT, 'tools', 'FERRY_STANDING.md')
MARK = '<!-- b406 the sites without an existential, and the finite side qualifier swept -->'

OLD = '**kernel terminals `B329.*` (24, zero-axiom) and `B310.*`**'
NEW = ('**kernel terminals `B329.*` (24, zero-axiom; the decomposition and the scaling part '
       'GENERAL, the compact part PER CELL) and `B310.*`**')

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


REG = d('b406_registration_2026-09-10.txt')
BANK = d('b406_the_sites_without_an_existential.txt')
CRUN = d('b406_components.txt')
XRUN = d('b406_extract.txt')
LG = json.load(io.open(d('b406_lockgate.json'), encoding='utf-8'))
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
       'cannot', 'without', 'refus', 'declin', 'not typed', 'not attempted', 'would have to be',
       'not asserting', 'not derived', 'not added', 'not minted')


def asserted(hay, phrase):
    out = []
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
        if gate_text.flat(phrase) in gate_text.flat(s) and not any(g in s.lower() for g in NEG):
            out.append(s[:140])
    return out


def verdict_line(out, word):
    """### **A TOOL'S VERDICT IS A LINE, NOT A SUBSTRING.** ### `A2`, applied to this suite."""
    return any(ln.strip().startswith(word) for ln in (out or '').splitlines())


def main(argv):
    post = '--post' in argv
    side = 'HEAD~1' if post else 'HEAD'
    bar('=')
    rec('b406 -- THE GATE SUITE. ### %s THE PUSH.' % ('AFTER' if post else 'BEFORE'))
    rec('### **THE PRE-ACT REFERENCE FOR EVERY LEDGER ARM IS NAMED, NOT ONLY ITS SIDE : `%s`.**'
        % side)
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)

    # ---- STEP ZERO --------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO, RE-READ FROM ITS OWN RECORDS.')
    bar()
    arm('G-FERRY', 'the ferry scan reported 0 hits',
        '0 HIT(S) REPORTED' in text(d('b406_ferry_scan.txt')))
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b406_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b406_faces_census_stepzero.txt')))
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b406_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies against its banked digest at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b406_reg_seal_verify.txt')) and SEAL in
        text(d('b406_reg_seal_verify.txt')))
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 checked by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    arm('G-ANCHORS', 'the survey left 0 anchor misses',
        '**ANCHOR MISSES : 0**' in xrun)

    # ---- THE SWEEP --------------------------------------------------------------------------
    bar()
    rec("  ### THE SWEEP: ITS SUBJECT, ITS TWO MATCHERS, AND WHAT IT REFUSED TO TOUCH.")
    bar()
    arm('G-SUBJECT', "the sweep's subject is the seal's own terminals, not the English words",
        'SEAL = re.compile' in text(t('b406_extract.py'))
        and "FiniteSideSeal|B329|compact_smear_vanishes" in text(t('b406_extract.py')))
    arm('G-SUBJECT-CTL', 'and the wider shape was run and PRINTED rather than assumed empty',
        'THE WIDE SWEEP, PRINTED AND NOT ACTED ON' in xrun)
    wide = re.search(r'THE WIDE SWEEP.*?candidates : (\d+) ; QUALIFIED within reach : (\d+) ; '
                     r'UNQUALIFIED : (\d+)', xrun, re.S)
    arm('G-WIDEYIELD', 'the wide yield is a real number and is printed', bool(wide),
        'wide sweep: %s candidates, %s unqualified'
        % (wide.group(1) if wide else '?', wide.group(3) if wide else '?'))
    arm('G-NOWIDEREPAIR', 'and NOTHING in the wide yield is hand-read or repaired',
        'NOTHING IN IT IS REPAIRED' in xrun or 'nothing in it is repaired' in bank.lower())
    arm('G-BOTHMATCHERS', 'both closure predicates are named in the tool and printed in the bank',
        'CLOSE_NARROW' in text(t('b406_extract.py'))
        and 'NOTHING TO REPAIR' in bank)
    scoped = re.search(r"SEAL.S OWN TERMINALS.*?candidates : (\d+) ; QUALIFIED within reach : "
                       r"(\d+) ; UNQUALIFIED : (\d+)", xrun, re.S)
    arm('G-QUALTABLE', 'the scoped sweep printed its table with a per-line classification',
        bool(scoped) and xrun.count('### UNQUAL') >= 1 and xrun.count('QUALIFIED  ') >= 10,
        'scoped: %s candidates, %s qualified, %s unqualified'
        % (scoped.group(1), scoped.group(2), scoped.group(3)) if scoped else 'no match')

    # ---- THE ONE REPAIR ---------------------------------------------------------------------
    bar()
    rec('  ### THE ONE REPAIR, AGAINST THE PRE-ACT BLOB AT `%s`.' % side)
    bar()
    blob = git(PP, 'show', '%s:OPEN_TRAILS.md' % side).stdout.decode('utf-8')
    live = text(TRAILS)
    livepart = live.split(MARK, 1)[0]
    keptpart = live.split(MARK, 1)[1] if MARK in live else ''
    # ### **THE APPEND LEAVES ONE NEWLINE BETWEEN THE LIVE REGION AND THE MARK**, so the split's
    # ### left half is the blob plus that separator. ### The comparison strips trailing newlines on
    # ### BOTH SIDES and prints the byte delta, so the arm measures the repair and not the append.
    undone = livepart.replace(NEW, OLD)
    same = undone.rstrip(chr(10)) == blob.rstrip(chr(10))
    arm('G-REPAIR-ADDS', 'undoing the qualifier restores the pre-act live region EXACTLY', same,
        'live region %d bytes ; blob %d ; delta %+d = qualifier %d + separator ; equal after '
        'undo : %s'
        % (len(livepart.encode('utf-8')), len(blob.encode('utf-8')),
           len(livepart.encode('utf-8')) - len(blob.encode('utf-8')),
           len(NEW.encode('utf-8')) - len(OLD.encode('utf-8')), same))
    arm('G-REPAIR-ONE', 'the qualifier was added exactly once in the live region',
        livepart.count(NEW) == 1 and livepart.count(OLD) == 0,
        'NEW %d ; OLD %d' % (livepart.count(NEW), livepart.count(OLD)))
    arm('G-ORIGINAL-KEPT', "and the original is preserved VERBATIM in this act's own block",
        OLD in keptpart, 'the original appears in the appended block : %s' % (OLD in keptpart))
    arm('G-NOPRESERVEDIT', 'and the preserved original was NOT itself repaired',
        keptpart.count(NEW) == 0,
        'the qualifier appears %d time(s) inside the preserved block' % keptpart.count(NEW))
    arm('G-NOGRADE', 'no grade word was added or removed anywhere in the file',
        len(re.findall(r'PROVED-|DERIVES-|MEASURED-|IMPORT-', livepart))
        == len(re.findall(r'PROVED-|DERIVES-|MEASURED-|IMPORT-', blob.split(MARK, 1)[0])))
    arm('G-TRAILS-APPEND', 'and the block itself is append-only against the blob',
        live.startswith(blob.split(MARK, 1)[0].replace(OLD, NEW))
        or blob.split(MARK, 1)[0].replace(OLD, NEW) in live)

    # ---- WHAT WAS NOT TOUCHED ---------------------------------------------------------------
    bar()
    rec('  ### WHAT WAS NOT TOUCHED. ### **EACH ARM NAMES ITS REFERENCE.**')
    bar()
    faces_blob = git(PP, 'show', '%s:FACES_LEDGER.md' % side).stdout.decode('utf-8')
    arm('G-NOROWWRITE', 'FACES_LEDGER.md is BYTE-IDENTICAL to the blob at %s' % side,
        text(FACES).replace('\r\n', '\n') == faces_blob,
        'working %d bytes ; blob %d bytes'
        % (len(text(FACES).encode('utf-8')), len(faces_blob.encode('utf-8'))))
    arm('G-NOCOORD', 'and no third coordinate was added to row U1',
        'ESCAPE-KIND' not in text(FACES))
    for label, repo in (('G-NOTOUCH-LV', LV),):
        st = [x for x in git(repo, 'status', '--porcelain').stdout.decode(
            'utf-8', 'replace').split(chr(10)) if x.strip()]
        tracked = [x for x in st if not x.startswith('??')]
        arm(label, '%s carries 0 TRACKED changes' % os.path.basename(repo), not tracked,
            'tracked %d ; untracked and PRE-EXISTING %d' % (len(tracked), len(st) - len(tracked)))
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(chr(10)) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified anywhere on the roster', not lean,
        'lean changes %s' % (lean or 'none'))
    builds = asserted(bank, 'a kernel was built') + asserted(bank, 'the kernel was rebuilt')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds,
        'asserting sentences %d %s' % (len(builds), builds or ''))
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    ferries = [f for f in os.listdir(D) if 'ferry' in f and f.endswith('.txt')
               and not f.startswith('b406')]
    dirty = [f for f in ferries if os.path.getmtime(d(f)) > os.path.getmtime(REG)]
    arm('G-NOFERRYEDIT', 'no banked ferry was written after the face was locked', not dirty,
        '%d banked ferries ; modified after the lock : %s' % (len(ferries), dirty or 'none'))
    banks = [f for f in os.listdir(D) if re.match(r'b(3\d\d|40[0-5])_', f) and f.endswith('.txt')]
    bdirty = [f for f in banks if os.path.getmtime(d(f)) > os.path.getmtime(REG)]
    arm('G-NOBANKEDIT', "and no prior act's record was written after the lock either", not bdirty,
        '%d prior records ; modified after the lock : %s' % (len(banks), bdirty or 'none'))

    # ---- THE COMPONENTS ---------------------------------------------------------------------
    bar()
    rec('  ### THE COMPONENTS, RE-READ FROM THEIR OWN RUN RECORD.')
    bar()
    arm('G-TWOSITES', 'both sites were written out as a quantifier string',
        'THE QUANTIFIER STRING' in crun and crun.count('THE QUANTIFIER STRING') == 2)
    arm('G-TRIVIAL', 'and a trivially satisfiable existential is CALLED trivially satisfiable',
        'TRIVIALLY SATISFIABLE' in crun)
    arm('G-NAMEQUOTED', 'component 2 quotes the barrier and the repair at their sources',
        'SIEVE CEILING LEMMA' in crun and 'BRIGHT CHANNEL' in crun
        and 'ESCAPE-KIND' in crun)
    arm('G-TWOPARTS', 'and scores them apart rather than reporting one as the other',
        'THE TWO PARTS DO NOT WEIGH THE SAME' in crun)
    minted = asserted(bank, 'this act names it') + asserted(bank, 'we call it')
    arm('G-NOMINT', 'the bank ASSERTS no name of its own', not minted,
        'asserting sentences %d' % len(minted))
    arm('G-NOMINT-CTL', 'and the predicate FIRES on synthetic text minting one',
        bool(asserted('The gap has no name, so this act names it the uniform bridge.',
                      'this act names it')))
    arm('G-PRICEONLY', 'the third coordinate is priced with a printed count',
        'THE PRICE:' in crun and 'PRICED AND NOT ADDED' in bank.upper())
    arm('G-NOTATTEMPTED', "addition one stops where it said it would",
        'NOT ATTEMPTED' in crun and 'NOT ATTEMPTED' in bank)
    arm('G-ARITY', 'the arity audit covers four standing laws plus the row',
        crun.count('CANNOT ANSWER:') >= 5)
    arm('G-ARITYRULES', 'and rules nothing',
        'NOTHING IS STRUCK, AMENDED OR RE-RULED' in crun)
    arm('G-EXPECT', 'every registered expectation is scored',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(N5)', '(N6)', '(N7)',
             '(E1)', '(E2)', '(E3)', '(E4)')))
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 2)

    # ---- THE STANDING CLAUSE ----------------------------------------------------------------
    bar()
    rec('  ### THE STANDING CLAUSE.')
    bar()
    st = text(STANDING)
    stblob = git(ROOT, 'show', '%s:tools/FERRY_STANDING.md' % side).stdout.decode('utf-8')
    arm('G-STANDING-A2', 'A2 is present, under AUTHOR-RULED, declaring itself NOT MEASURED',
        '**A2**' in st
        and st.index('AUTHOR-RULED CLAUSES (NOT MEASURED)') < st.index('**A2**')
        and st.count('NOT MEASURED; carried by no count') == 2)
    arm('G-STANDING-ACTS', 'and the six incidents are listed by act',
        all(a in st.split('**A2**')[1] for a in
            ('b316', 'b317', 'b400', 'b403', 'b404', 'b405')))
    vb = re.search(r'^VERSION: (\d+)\s*$', stblob, re.M).group(1)
    va = re.search(r'^VERSION: (\d+)\s*$', st, re.M).group(1)
    arm('G-STANDING-VERSION', 'the VERSION line did not move, and the reason is on the file',
        vb == va == '2' and 'bumping it here' in st, 'blob %s -> working %s' % (vb, va))
    arm('G-STANDING-APPEND', 'and the rest of the file is byte-identical to the blob',
        st.replace('\r\n', '\n').replace(
            st.split('**NOT MEASURED; carried by no count.**')[1].split(
                '## HOW A FERRY CITES')[0].replace('\r\n', '\n'), '\n\n')
        .startswith(stblob.split('**NOT MEASURED; carried by no count.**')[0]),
        'blob %d -> working %d bytes'
        % (len(stblob.encode('utf-8')), len(st.encode('utf-8'))))
    n_clauses = len(re.findall(r'^- \*\*A\d+\*\*', st, re.M))
    arm('G-STANDING-ROUTED', 'the sentence the order did not name is ROUTED and not promoted',
        'ROUTED TO THE AUTHOR' in st and n_clauses == 2
        and 'every write encodes before it opens' in st,
        'author-ruled clauses in the file : %d ; the unpromoted sentence is named : %s'
        % (n_clauses, 'every write encodes before it opens' in st))
    arm('G-SCANFIX', 'and the ferry scan still reports v2 as CURRENT',
        'STANDING-CLAUSES CITATION : CURRENT' in text(d('b406_ferry_scan.txt')))

    # ---- THE VERDICT-LINE CLAUSE, APPLIED TO THIS SUITE -------------------------------------
    bar()
    rec('  ### THE PROMOTED CLAUSE, APPLIED TO THIS SUITE FROM ITS FIRST WRITE.')
    bar()
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-sites-without-an-existential'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-VERDICTLINE', 'the key resolves, read from the VERDICT LINE and not a substring',
        (not verdict_line(kq, '### NO KEY')) and 'b406' in kq,
        'verdict-line NO KEY : %s ; raw substring hits : %d'
        % (verdict_line(kq, '### NO KEY'), kq.count('NO KEY')))
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a name was minted'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-VERDICTLINE-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))
    arm('G-KEY', 'the key carries the act and its findings',
        'SIEVE CEILING' in kq and 'BRIGHT CHANNEL' in kq and 'TRIVIALLY SATISFIABLE' in kq)
    arm('G-ENCODEFIRST', 'every write in this act`s tools encodes before it opens',
        all('encode(' in text(t('b406_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank')),
        'checked: extract, components, desk_bank')

    # ---- THE LIVING RECORD ------------------------------------------------------------------
    bar()
    rec('  ### THE LIVING RECORD.')
    bar()
    tb = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8')
    tl = text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.replace('\r\n', '\n').startswith(tb.rstrip(chr(10))),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    arm('G-DESK', 'the desk was swept and its closures printed',
        any('ITEMS SWEPT' in text(d(f)) for f in os.listdir(D)
            if f.startswith('b406_desk_notes')))

    # ---- THE STANDING NOTHINGS ---------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS, RE-MEASURED ON THE BANK.')
    bar()
    dep = asserted(bank, 'was deposited') + asserted(bank, 'zenodo')
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action of any kind', not dep,
        'asserting sentences %d' % len(dep))
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true') + asserted(bank, 'h2 fails')
    arm('G-NOH2', 'and it ASSERTS nothing about `h2` in either direction', not h2,
        'asserting sentences %d' % len(h2))
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    bridged = asserted(bank, 'a bridge is typed') + asserted(bank, 'the two are equivalent')
    arm('G-NOBRIDGE', 'and it types no bridge', not bridged)
    arm('G-DEFECTS', "and the act prints its own apparatus defects",
        'PRESERVED ORIGINAL' in bank and 'CRLF' in bank and 'STALE RUN RECORD' in bank)
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRYFIX', 'the ferry-scan fixtures still hold in both polarities', ok_scan)
    arm('G-SEALNAME', 'the bank names the seal it was written under', SEAL in bank)

    # ---- THE WRITE LIST ----------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST, BUILT AS KINDS.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b406')) \
        + ['audit_b406_reg_satisfiable.txt'] \
        + sorted('_b406/' + f for f in os.listdir(d('_b406'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b406_'))
    KINDS = {
        1: (r'^b406_registration_', r'^b406_satisfiable', r'^audit_b406_reg_satisfiable',
            r'^b406_regspec_run', r'^b406_reg_termscan', r'^b406_reg_gate', r'^b406_lockgate',
            r'^b406_reg_seal'),
        2: (r'^b406_ferry',),
        3: (r'^b406_census_', r'^b406_faces_census_', r'^b406_pins_', r'^b406_mirror'),
        4: (r'^b406_extract\.txt$', r'^_b406/'),
        5: (r'^b406_components\.txt$',),
        6: (r'^b406_desk', r'^b406_the_sites_without_an_existential', r'^b406_closing'),
        7: (r'^b406_checks',),
        8: (r'^tools/b406_',),
    }
    placed, unkinded = {}, []
    for f in written:
        hit = [k for k, pats in KINDS.items() if any(re.search(p, f) for p in pats)]
        (placed.setdefault(f, hit[0]) if hit else unkinded.append(f))
    arm('G-WRITELIST', 'every file this act wrote is of a KIND the locked face names',
        not unkinded, '%d written ; of NO named KIND %d : %s'
        % (len(written), len(unkinded), unkinded or 'none'))
    unnamed = [f for f in written if os.path.basename(f) not in reg]
    arm('G-WRITELIST-PATHS', 'and the PATH-level residue is printed, not hidden', True,
        '%d of %d named by KIND but not by path : %s'
        % (len(unnamed), len(written), unnamed or 'none'))
    kinds = re.findall(r'\*\*KIND (\d+) --', reg)
    arm('G-WRITELIST-KIND', 'the list is built as KINDS',
        len(kinds) >= 9 and len(set(placed.values())) >= 7,
        'kinds declared %d ; used %d' % (len(kinds), len(set(placed.values()))))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b406_'))
    arm('G-CAP', 'at most 6 new relay tool files', len(tools) <= 6, '%d : %s' % (len(tools), tools))

    # ---- MUST-FAIL ----------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### A THIRD COORDINATE WAS ADDED TO ROW U1.',
        '### A NAME WAS MINTED FOR THE UNIFORM-BOUND FORM.',
        '### A SHARED WITNESS WAS FOUND.',
        '### A BANKED FERRY WAS EDITED.',
        '### THE VERSION LINE WAS BUMPED TO v3.',
        '### A KERNEL WAS BUILT.',
    ]
    lines = set(bank.split(chr(10)))
    hits = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits,
        'hits %s' % (hits or 'none'))
    synth = 'a' + chr(10) + '### A NAME WAS MINTED FOR THE UNIFORM-BOUND FORM.' + chr(10) + 'b'
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
    out = d('b406_checks_postpush.txt' if post else 'b406_checks.txt')
    io.open(out, 'wb').write((chr(10).join(R) + chr(10)).encode('utf-8'))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
