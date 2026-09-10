# -*- coding: utf-8 -*-
"""b407_checks.py -- THE GATE SUITE FOR THE BARRIER'S OWN INSTANCE.

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
MARK = '<!-- b407 the barrier own instance, and the repair priced where it is thin -->'

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


REG = d('b407_registration_2026-09-10.txt')
BANK = d('b407_the_barriers_own_instance.txt')
CRUN = d('b407_components.txt')
XRUN = d('b407_extract.txt')
LG = json.load(io.open(d('b407_lockgate.json'), encoding='utf-8'))
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


def main(argv):
    post = '--post' in argv
    side = 'HEAD~1' if post else 'HEAD'
    bar('=')
    rec('b407 -- THE GATE SUITE. ### %s THE PUSH.' % ('AFTER' if post else 'BEFORE'))
    rec('### **THE PRE-ACT REFERENCE FOR EVERY LEDGER ARM IS NAMED, NOT ONLY ITS SIDE : `%s`.**'
        % side)
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)

    # ---- STEP ZERO ---------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO, RE-READ FROM ITS OWN RECORDS.')
    bar()
    arm('G-FERRY', 'the ferry scan reported 0 hits',
        '0 HIT(S) REPORTED' in text(d('b407_ferry_scan.txt')))
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b407_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b407_faces_census_stepzero.txt')))
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b407_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b407_reg_seal_verify.txt'))
        and SEAL in text(d('b407_reg_seal_verify.txt')))
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    arm('G-ANCHORS', 'the survey left 0 anchor misses', '**ANCHOR MISSES : 0**' in xrun)
    arm('G-EOTABLE', "the E0 gate's table was located by its own heading, not by a per-row anchor",
        'THE E0 GATE, LOCATED BY ITS OWN HEADING' in xrun
        and xrun.count('  ### line 30') >= 6,
        'the K-rows appear in three tables; a per-row anchor is ambiguous in all three')

    # ---- COMPONENT 1 -------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 1 -- BOTH COUNTS, AND NO COEFFICIENT.')
    bar()
    m = re.search(r'STRICT -- SITES NAMING AN INTERFACE IN DEFINITION 2\.2.S SENSE : (\d+) OF 6',
                  crun)
    m2 = re.search(r': (\d+) OF 6 \[', crun)
    arm('G-BOTHCOUNTS', 'the strict and the loose counts are BOTH printed', bool(m) and bool(m2),
        'strict %s of 6 ; loose %s of 6' % (m.group(1) if m else '?', m2.group(1) if m2 else '?'))
    arm('G-STRICTGOVERNS', 'and the strict one is said to govern, with the reason',
        'NOT ONE OF THE SIX SITES NAMES A SPECIFICATION' in crun)
    kappa = (asserted(bank, 'kappa is zero') + asserted(bank, 'the interface is dark')
             + asserted(crun, 'we measure kappa'))
    arm('G-NOKAPPA', 'the act ASSERTS no transmission coefficient of its own', not kappa,
        'asserting sentences %d %s' % (len(kappa), kappa or ''))
    arm('G-NOKAPPA-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('At the fourth site the interface is dark.', 'the interface is dark')))
    arm('G-KAPPA-REPORTED', "and where the RECORD asserts it, that is reported as the record's",
        'IS ASSERTED BY THE RECORD ITSELF' in bank
        and 'IT REPORTS THAT THE RECORD ASSERTS IT' in bank)

    # ---- ADDITION THREE ----------------------------------------------------------------------
    bar()
    rec('  ### ADDITION THREE -- THE VERDICT, THE FAILING HYPOTHESIS, AND THE RESEMBLANCE.')
    bar()
    arm('G-HYPOTHESES', 'all five hypotheses are put to the halt, each quoted',
        crun.count('### **(') >= 5 and 'THEOREM 3.1' in crun
        and 'HYPOTHESIS BY HYPOTHESIS' in crun)
    arm('G-VERDICT', 'the verdict is one of the three the order allows',
        'NOT AN INSTANCE OF THEOREM 3.1' in crun)
    arm('G-FAILINGHYP', 'and the failing hypothesis is named and quoted',
        'THE FAILING' in crun and 'formal first-order proof in ZFC' in crun
        and 'AN IMPORT UNDER THE BAR IS NOT AN INFERENCE STEP' in crun.replace('\n', ' ')
        .replace('      ### ### ', ' ').replace('###', ' '))
    arm('G-RESEMBLANCE', 'AND the resemblance is printed BESIDE the verdict, not instead of it',
        'cumulative invariants of I' in crun
        and 'PRECISELY WHERE DEFINITION 2.5' in crun.replace('\n', ' ').replace('### ', ''))
    arm('G-RESEMBLANCE-CTL', 'and the act says in its own words that a resemblance is not an '
                             'instance',
        'A RESEMBLANCE, NOT AN INSTANCE' in bank.replace('\n### ', ' ').replace('### ', ''))
    faces_blob = git(PP, 'show', '%s:FACES_LEDGER.md' % side).stdout.decode('utf-8')
    arm('G-NOROWWRITE', 'FACES_LEDGER.md is BYTE-IDENTICAL to the blob at %s' % side,
        text(FACES).replace('\r\n', '\n') == faces_blob,
        'working %d ; blob %d bytes'
        % (len(text(FACES).encode('utf-8')), len(faces_blob.encode('utf-8'))))

    # ---- ADDITION FOUR -----------------------------------------------------------------------
    bar()
    rec('  ### ADDITION FOUR -- A CHANNEL NAMED, AND A DISCLAIMER NOT READ AS ITS CONVERSE.')
    bar()
    conv = (asserted(bank, 'the zeros are the spectrum')
            + asserted(bank, 'the realization exists')
            + asserted(bank, 'a positive pairing is known'))
    arm('G-NOCONVERSE', 'the bank ASSERTS nowhere what the deposit disclaims', not conv,
        'asserting sentences %d %s' % (len(conv), conv or ''))
    arm('G-NOCONVERSE-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('By the fifth register the zeros are the spectrum of that operator.',
                      'the zeros are the spectrum')))
    arm('G-ONEOFTHREE', 'and the existential-over-three reason is printed',
        'ONE OF THREE IS NOT THE NEGATION OF AN EXISTENTIAL OVER THREE'
        in crun.replace('\n', ' ').replace('### ', ''))

    # ---- COMPONENTS 2 AND 3 ------------------------------------------------------------------
    bar()
    rec('  ### THE PRICE CORRECTED, AND THE BLOCKER NAMED BY KIND.')
    bar()
    arm('G-PRICEMOVED', "b406's price is re-measured and the movement printed with its reason",
        'THE PRICE, RE-MEASURED: `4` OF 6 FILLABLE, NOT `5`' in crun
        and 'OPTIMISTIC BY ONE' in crun)
    arm('G-PRICEFIXED', 'and the seat says a price is not protected by having been its own',
        'NOT PROTECTED BY HAVING BEEN THIS SEAT' in crun.replace('’', "'"))
    arm('G-BOTHSIDES', 'the escape-kind finding is quoted from the record, both kinds',
        'RH-sign' in crun and 'RH-derivative' in crun
        and 'PROPERTY OF THE QUESTION' in crun)
    arm('G-SMALLEST', 'the smallest statement is named',
        'TIER-2 FORM OF THE BARRIER' in crun)
    # ### **A NEEDLE THAT SURVIVES THE BANK'S OWN MARKUP.** ### The prose carries `###` markers,
    # ### backticks and hard wraps THROUGH the sentence, so a raw substring test on it is the same
    # ### mistake in a new dress. ### The comparison folds markers, backticks and line breaks away
    # ### first -- and the arm PRINTS whether the folded needle was found.
    def fold(s):
        return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))
    needle = 'IT IS NOT UNPRICEABLE FOR WANT OF THE PARKED LANE'
    arm('G-BLOCKERKIND', 'and the blocker is named by KIND, not left ambiguous',
        needle in fold(crun) and 'research-frontier' in crun,
        'folded needle found : %s ; the document`s own word present : %s'
        % (needle in fold(crun), 'research-frontier' in crun))

    # ---- ADDITION ONE ------------------------------------------------------------------------
    bar()
    rec('  ### `(R20)` ROUTED, NOT RULED.')
    bar()
    arm('G-R20ROUTED', 'the limb is named and the cost stated in the rule`s own words',
        'THE LIMB IS THE SECOND' in crun and 'descriptive before it is prescriptive' in crun
        and 'discovered, not imposed' in crun)
    widened = asserted(bank, 'the rule is widened') + asserted(bank, 'limb 2 now covers')
    arm('G-NORULE', 'and the bank ASSERTS no widening', not widened,
        'asserting sentences %d' % len(widened))
    arm('G-NORULE-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('By this act the rule is widened to cover uncited kernels.',
                      'the rule is widened')))

    # ---- ADDITION TWO ------------------------------------------------------------------------
    bar()
    rec('  ### THE GUARD, AND THAT THE INSTRUMENT IT LIVES IN DID NOT MOVE.')
    bar()
    rc_now = text(RC)
    rc_blob = git(ROOT, 'show', '%s:tools/run_clock.py' % side).stdout.decode('utf-8')
    i = rc_now.find('def latest(')
    j = rc_now.find("if __name__ == '__main__':")
    added = rc_now[i:j] if (i > 0 and j > i) else ''
    stripped = (rc_now[:i] + rc_now[j:]) if added else rc_now
    arm('G-RUNCLOCK-ADDITIVE', 'removing the added block leaves the blob BYTE-IDENTICAL',
        stripped.replace('\r\n', '\n') == rc_blob,
        'working %d ; added block %d ; remainder %d ; blob %d bytes'
        % (len(rc_now.encode('utf-8')), len(added.encode('utf-8')),
           len(stripped.encode('utf-8')), len(rc_blob.encode('utf-8'))))
    arm('G-RUNCLOCK-CALLERS', 'and every existing function is still present, unrenamed',
        all(('def %s(' % f) in rc_now for f in
            ('stamp', 'next_path', 'write', 'read_stamp', 'self_test')))
    arm('G-RUNCLOCK-FIXTURE', 'the guard carries fixtures in BOTH polarities and they hold',
        run_clock.latest_self_test(verbose=False) and run_clock.self_test(verbose=False))
    lp, ls, note = run_clock.latest(D, 'b407_desk_notes')
    arm('G-RUNRECORD', "and this act's own run record is read FROM ITS RUN, by the guard",
        lp is not None and ls is not None,
        '%s (%s ; %s)' % (os.path.basename(lp or '-'), ls, note))
    arm('G-RUNRECORD-CTL', 'and the guard REFUSES rather than guesses on an unstamped candidate',
        'REFUSED' in run_clock.latest(os.path.join(ROOT, 'tools'), 'run_clock', '.py')[2]
        or run_clock.latest(os.path.join(ROOT, 'tools'), 'run_clock', '.py')[0] is None)

    # ---- WHAT WAS NOT TOUCHED ----------------------------------------------------------------
    bar()
    rec('  ### WHAT WAS NOT TOUCHED.')
    bar()
    arm('G-NOREPAIR', 'this act made no in-place repair anywhere',
        'in-place repair' not in text(t('b407_desk_bank.py')).lower().replace(
            'makes no in-place repair', '')
        or 'MAKES NO IN-PLACE REPAIR' in text(t('b407_desk_bank.py')))
    st_now, st_blob = text(STANDING), git(ROOT, 'show', '%s:tools/FERRY_STANDING.md'
                                          % side).stdout.decode('utf-8')
    arm('G-NOSTANDING', 'FERRY_STANDING.md is byte-identical to the blob',
        st_now.replace('\r\n', '\n') == st_blob.replace('\r\n', '\n'))
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(chr(10)) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified', not lean, 'lean changes %s' % (lean or 'none'))
    builds = asserted(bank, 'a kernel was built')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds,
        'asserting sentences %d' % len(builds))
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b407_'))
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
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-barriers-own-instance'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY', 'the key resolves, read from the VERDICT LINE',
        (not verdict_line(kq, '### NO KEY')) and 'b407' in kq,
        'verdict-line NO KEY : %s ; raw substring hits : %d'
        % (verdict_line(kq, '### NO KEY'), kq.count('NO KEY')))
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a row was written to the ledger'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))
    arm('G-DESK', 'the desk was swept and its closures printed',
        'ITEMS SWEPT' in text(lp) if lp else False)

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
        all('encode(' in text(t('b407_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank')))
    arm('G-EXPECT', 'every registered expectation is scored',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(N5)', '(N6)', '(N7)',
             '(E1)', '(E2)', '(E3)', '(E4)')))
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 2)
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRYFIX', 'the ferry-scan fixtures still hold', ok_scan)
    arm('G-SEALNAME', 'the bank names the seal it was written under', SEAL in bank)

    # ---- THE WRITE LIST -----------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST, BUILT AS KINDS.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b407')) \
        + ['audit_b407_reg_satisfiable.txt'] \
        + sorted('_b407/' + f for f in os.listdir(d('_b407'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b407_'))
    KINDS = {
        1: (r'^b407_registration_', r'^b407_satisfiable', r'^audit_b407_reg_satisfiable',
            r'^b407_regspec_run', r'^b407_reg_termscan', r'^b407_reg_gate', r'^b407_lockgate',
            r'^b407_reg_seal'),
        2: (r'^b407_ferry',),
        3: (r'^b407_census_', r'^b407_faces_census_', r'^b407_pins_', r'^b407_mirror'),
        4: (r'^b407_extract\.txt$', r'^_b407/'),
        5: (r'^b407_components\.txt$',),
        6: (r'^b407_desk', r'^b407_the_barriers_own_instance', r'^b407_closing'),
        7: (r'^b407_checks',),
        8: (r'^tools/b407_',),
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
        len(kinds) >= 10 and len(set(placed.values())) >= 7,
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
    out = d('b407_checks_postpush.txt' if post else 'b407_checks.txt')
    io.open(out, 'wb').write((chr(10).join(R) + chr(10)).encode('utf-8'))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
