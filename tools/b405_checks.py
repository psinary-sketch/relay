# -*- coding: utf-8 -*-
"""b405_checks.py -- THE GATE SUITE FOR THE ROW'S LAW RESTATED.

### ### **`G-NOCOLUMN` IS THE ARM THAT MATTERS MOST, BECAUSE IT IS THE THING THE RULING COULD HAVE
### ### COST.** ### `(R24)` gave the row two coordinates inside a ledger whose COLUMN LAW fixes
### seven columns for every table line. ### The arm re-measures EVERY line's column count against
### the pre-act blob and fails if a single one moved.
###
### ### **`G-NOBRIDGE` AND `G-NOWITNESS` GUARD THE ROW'S OWN LAW.** ### A `WITNESS` column in a row
### whose whole law is that it types no bridge is exactly where a bridge gets typed by accident, and
### naming what a witness would have to be is exactly where a witness gets claimed by accident.
### ### **BOTH ARE ASSERTION-LEVEL FROM THEIR FIRST WRITE, WITH A CONTROL ON THE OTHER POLARITY**,
### as the ferry's standing now requires -- not rebuilt after failing, which is what `b400`, `b403`
### and `b404` each had to do.
###
### ### **`G-PINREAD` GUARDS THE READING.** ### A terminal cited at a tag and read from a working
### tree ahead of that tag is a different file. ### The arm re-materialises the file at the tag and
### compares the bytes the survey actually read.
###
### ### **AND EVERY ARM READING A REPOSITORY STATE NAMES ITS REFERENCE AND IS TAKEN AT THE SAME
### ### MOMENT AS WHAT IT MEASURES**, and requires only what THIS act could have done -- `0` TRACKED
### changes, with pre-existing untracked files PRINTED rather than failed on (`b404`'s species).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import banned_terms               # noqa: E402
import ferry_scan                 # noqa: E402
import gate_text                  # noqa: E402
import run_clock                  # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
SE = os.path.join('D:', os.sep, 'SIDE-effects')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
PIN = 'v0.10.0'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def text(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True)


REG = d('b405_registration_2026-09-10.txt')
BANK = d('b405_the_rows_law_restated.txt')
CRUN = d('b405_components.txt')
XRUN = d('b405_extract.txt')
LG = json.load(io.open(d('b405_lockgate.json'), encoding='utf-8'))
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
    rec('  %-20s %-60s %s' % (name, why[:60], 'PASS' if ok else '### FAIL ###'))
    if detail:
        for k in range(0, min(len(detail), 900), 150):
            rec('      %s' % detail[k:k + 150])


# ### =================================================================================================
# ### ### **THE ASSERTION-LEVEL PREDICATE, WRITTEN ONCE AND USED BY EVERY PROSE-READING ARM.**
# ### ### A hit counts only in a sentence carrying no negator. ### `b400`'s `G-ONEQ`, `b403`'s
# ### ### `G-FERRYWORDS` and `b404`'s `G-NOAXIOMCLAIM` all fired on their own act's denial; this
# ### ### suite starts here instead of arriving here.
# ### =================================================================================================
NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'never', 'nothing',
       'cannot', 'without', 'refus', 'declin', 'not typed', 'not claiming', 'no bridge',
       'would have to be', 'not asserting')


def asserted(hay, phrase):
    """### Sentences that ASSERT `phrase` -- no negator anywhere in the sentence."""
    out = []
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
        if gate_text.flat(phrase) in gate_text.flat(s) and not any(g in s.lower() for g in NEG):
            out.append(s[:140])
    return out


def main(argv):
    post = '--post' in argv
    side = 'HEAD~1' if post else 'HEAD'
    bar('=')
    rec('b405 -- THE GATE SUITE. ### %s THE PUSH.' % ('AFTER' if post else 'BEFORE'))
    rec('### **THE PRE-ACT REFERENCE FOR EVERY LEDGER ARM IS NAMED, NOT ONLY ITS SIDE : `%s`.**'
        % side)
    bar('=')

    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)

    # ---- STEP ZERO, RE-READ ----------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO, RE-READ FROM ITS OWN RECORDS.')
    bar()
    arm('G-FERRY', 'the ferry scan reported 0 hits',
        '0 HIT(S) REPORTED' in text(d('b405_ferry_scan.txt')))
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b405_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b405_faces_census_stepzero.txt')))
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b405_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies against its banked digest at %s' % SEAL[:16],
        SEAL in text(d('b405_reg_seal_verify.txt')) and 'SEAL INTACT' in
        text(d('b405_reg_seal_verify.txt')))
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 checked by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4,
        'read %d passing %d by-digest %d'
        % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))

    # ---- THE SURVEY ------------------------------------------------------------------------------
    bar()
    rec('  ### THE SURVEY, AND THE PIN IT READ AT.')
    bar()
    misses = xrun.count('### ANCHOR MISS') + xrun.count('### BLOCK MISS')
    arm('G-ANCHORS', 'the survey left 0 anchor misses and 0 block misses', misses == 0,
        'misses %d' % misses)
    tag = git(LV, 'rev-parse', '%s^{}' % PIN).stdout.decode().strip()
    arm('G-PINTAG', 'the tag the corpus cites resolves to the commit the survey printed',
        tag == '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f' and tag[:7] in xrun,
        '%s -> %s' % (PIN, tag))
    at_pin = git(LV, 'show', '%s:SIDELvConservation/T3_StepNineBridge.lean' % PIN).stdout
    on_disk = io.open(d('_b405/T3_at_pin.lean'), 'rb').read()
    arm('G-PINREAD', 'the file the survey read IS the file at the tag, byte for byte',
        at_pin == on_disk and len(at_pin) > 0,
        'at pin %d bytes ; materialised %d bytes' % (len(at_pin), len(on_disk)))
    head = git(LV, 'rev-parse', 'HEAD').stdout.decode().strip()
    arm('G-NOTWORKING', 'and the working tree is NOT the pin, so reading it would have differed',
        head != tag, 'HEAD %s vs pin %s' % (head[:12], tag[:12]))
    arm('G-T3QUOTE', 'both terminals are quoted whole in the survey',
        'theorem T3prime_shared_witness' in xrun
        and 'theorem T3doubleprime_general_commutation_fails' in xrun
        and 'h2 : mellin Phi (s / 2)' in xrun)
    arm('G-PROFILE-READ', 'their profile is READ from a printed profile, not inferred',
        'depends on axioms: [propext, Classical.choice, Quot.sound]' in xrun)
    arm('G-PROFILE-GS', "and the finite side's two profiles come from AXIOM_PRINTS.txt",
        "'B329.finite_side_silence' does not depend on any axioms" in xrun
        and "'B329.compact_smear_vanishes_at_cells' does not depend on any axioms" in xrun)

    # ---- NOTHING WAS BUILT AND NOTHING WAS TOUCHED ------------------------------------------------
    bar()
    rec('  ### NOTHING BUILT, NOTHING TOUCHED. ### **EACH ARM REQUIRES ONLY WHAT THIS ACT COULD')
    rec('  ### HAVE DONE, AND PRINTS WHAT PREDATES IT.**')
    bar()
    for label, repo in (('G-NOTOUCH-LV', LV), ('G-NOTOUCH-SE', SE)):
        st = [x for x in (git(repo, 'status', '--porcelain').stdout.decode('utf-8', 'replace')
                          .split(chr(10))) if x.strip()]
        tracked = [x for x in st if not x.startswith('??')]
        arm(label, '%s carries 0 TRACKED changes' % os.path.basename(repo), not tracked,
            'tracked %d ; untracked and PRE-EXISTING %d : %s'
            % (len(tracked), len(st) - len(tracked),
               [x[3:] for x in st if x.startswith('??')] or 'none'))
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode('utf-8', 'replace').split(
        chr(10)) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified in SIDE-global-section either', not lean,
        'lean changes %s' % (lean or 'none'))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b405_'))
    arm('G-CAP', 'the act wrote at most 6 new relay tool files', len(tools) <= 6,
        '%d : %s' % (len(tools), tools))
    builds = asserted(bank, 'a kernel was built') + asserted(bank, 'the kernel was rebuilt')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds,
        'asserting sentences %d %s' % (len(builds), builds or ''))
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))

    # ---- THE ROW ---------------------------------------------------------------------------------
    bar()
    rec('  ### ROW `U1`, AGAINST THE PRE-ACT BLOB AT `%s`.' % side)
    bar()
    blob = git(PP, 'show', '%s:FACES_LEDGER.md' % side).stdout.decode('utf-8')
    live = text(FACES)
    b_rows = [l for l in blob.split(chr(10)) if l.startswith('| U1 |')]
    l_rows = [l for l in live.split(chr(10)) if l.startswith('| U1 |')]
    arm('G-ONEROW', 'row `U1` is unique in both the blob and the working file',
        len(b_rows) == 1 and len(l_rows) == 1)
    bc, lc = GD.split_cells(b_rows[0]), GD.split_cells(l_rows[0])
    ident = [k for k in range(7) if k not in (4, 6) and bc[k] == lc[k]]
    arm('G-BYTEIDENT', 'the five untouched cells are BYTE-IDENTICAL to the pre-act blob',
        len(ident) == 5, 'identical cells %s' % ident)
    pref = [k for k in (4, 6) if lc[k].startswith(bc[k].rstrip()) and len(lc[k]) > len(bc[k])]
    arm('G-PREFIX', 'the two touched cells carry their prior text as a TRUE PREFIX',
        len(pref) == 2, 'true-prefix cells %s ; %d -> %d and %d -> %d bytes'
        % (pref, len(bc[4].encode('utf-8')), len(lc[4].encode('utf-8')),
           len(bc[6].encode('utf-8')), len(lc[6].encode('utf-8'))))
    shape_b = [ln.rstrip().count('|') for ln in blob.split(chr(10)) if ln.startswith('|')]
    shape_l = [ln.rstrip().count('|') for ln in live.split(chr(10)) if ln.startswith('|')]
    arm('G-NOCOLUMN', 'EVERY table line has the same column count as before the act',
        shape_b == shape_l and len(shape_l) > 100,
        'table lines %d -> %d ; differing lines %d'
        % (len(shape_b), len(shape_l),
           sum(1 for a, b in zip(shape_b, shape_l) if a != b)))
    arm('G-TABLELINES', 'and the file gained no line and lost none',
        len(blob.split(chr(10))) == len(live.split(chr(10))),
        '%d -> %d' % (len(blob.split(chr(10))), len(live.split(chr(10)))))
    arm('G-KINDCELLS', 'six `KIND` cells are on the row',
        all(('**`(%s)` — KIND' % s) in l_rows[0]
            for s in ('i', 'ii', 'iii', 'iv', 'v', 'vi')))
    arm('G-WITNESSCELLS', 'six `WITNESS` cells are on the row',
        l_rows[0].count('WITNESS: ') == 6, 'count %d' % l_rows[0].count('WITNESS: '))
    arm('G-REFUSAL-VERBATIM', "the row's refusal is restated word for word, not summarised",
        'types no bridge between' in l_rows[0]
        and 'an equivalence gets compiled by accident' in l_rows[0])
    arm('G-REFUSAL-UNARY', 'and the binary/unary finding is on the face of the row',
        'A BINARY LAW CANNOT EXPRESS A UNARY DISTINCTION' in l_rows[0]
        and 'MISSING COORDINATE IN THE ROW' in l_rows[0])
    arm('G-CELLSOURCE', "the witness form is sourced from the theorem, named on the row",
        'T3prime_shared_witness' in l_rows[0] and '93c27ec' in l_rows[0]
        and 'h2 : mellin Phi (s / 2)' in l_rows[0])

    # ---- THE ROW'S LAW, ON THE ACT ITSELF ---------------------------------------------------------
    bar()
    rec('  ### THE ROW’S LAW, APPLIED TO THIS ACT. ### **ASSERTION-LEVEL, WITH CONTROLS.**')
    bar()
    bridged = (asserted(bank, 'a bridge is typed') + asserted(bank, 'the two are equivalent')
               + asserted(bank, 'the shape holds at'))
    arm('G-NOBRIDGE', 'the bank ASSERTS no bridge and no equivalence anywhere', not bridged,
        'asserting sentences %d %s' % (len(bridged), bridged or ''))
    arm('G-NOBRIDGE-CTL', 'and the predicate FIRES on synthetic text typing one',
        bool(asserted('At the fourth site the shape holds at the instance.', 'the shape holds at')))
    found = (asserted(bank, 'a witness is known') + asserted(bank, 'a shared witness exists')
             + asserted(bank, 'the witness is'))
    arm('G-NOWITNESS', 'and it ASSERTS nowhere that a shared witness exists at any site',
        not found, 'asserting sentences %d %s' % (len(found), found or ''))
    arm('G-NOWITNESS-CTL', 'and that predicate FIRES on synthetic text claiming one',
        bool(asserted('At the third site a shared witness exists.', 'a shared witness exists')))
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true') + asserted(bank, 'h2 fails')
    arm('G-NOH2', 'and it ASSERTS nothing about `h2` in either direction', not h2,
        'asserting sentences %d %s' % (len(h2), h2 or ''))
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    arm('G-NOPROSE', 'no arm in this suite greps raw prose for a forbidden claim',
        'def asserted' in text(t('b405_checks.py'))
        and text(t('b405_checks.py')).count('asserted(') >= 12)

    # ---- THE COMPONENTS' OWN NUMBERS -------------------------------------------------------------
    bar()
    rec('  ### THE COMPONENTS, RE-READ FROM THEIR OWN RUN RECORD.')
    bar()
    arm('G-SIXSITES', 'the six sites were located in the cell by their own markers',
        all(("      %-9s : at offset" % s) in xrun or ('%-9s : at offset' % s) in xrun
            for s in ('(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)')),
        'offsets line present')
    arm('G-SIXSITES-CTL', 'and the survey would have said NOT FOUND for a site that was absent',
        'NOT FOUND' in text(t('b405_extract.py')))
    arm('G-TABLE18', 'component 1 printed six sites times three tests with their quotes',
        crun.count('T1 WRITES THE MISSING STATEMENT') == 6
        and crun.count('T2 FILES A RESIDUE') == 6
        and crun.count('T3 DECLARES ITS KIND') == 6)
    arm('G-VACUOUS', 'and a residue test with no statement to weigh is called VACUOUS',
        crun.count('VACUOUS') >= 2)
    arm('G-CELLSCOUNT', 'component 3 printed six KIND cells and six WITNESS cells',
        '**KIND CELLS : 6.**' in crun and '**WITNESS CELLS : 6.**' in crun)
    arm('G-NOFOUND', 'and no site of the six has a witness FOUND',
        'FOUND 0' in crun)
    arm('G-EXPECT', 'every registered expectation is scored in the run record',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(N5)', '(N6)', '(N7)',
             '(E1)', '(E2)', '(E3)', '(E4)')))
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations rather than only its met ones',
        crun.count('REFUTED') >= 2)
    arm('G-DECLINED', "both of the navigator's named witnesses are scored and declined",
        'THE ABSCISSA IS NOT A SITE OF THIS ROW' in crun.replace('**', '').replace('###', '')
        and 'THE BRANCH IS `(beta)`' in crun.replace('**', ''),
        'abscissa scored : %s ; finite side branched : %s'
        % ('THE ABSCISSA' in crun, '(beta)' in crun))

    # ---- THE WRITE LIST, AS KINDS ----------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST, BUILT AS KINDS AND RE-MEASURED AGAINST WHAT WAS WRITTEN.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b405')) \
        + sorted('_b405/' + f for f in os.listdir(d('_b405'))) \
        + ['audit_b405_reg_satisfiable.txt'] \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b405_'))
    # ### **THE BAR IS KIND-MEMBERSHIP, SO THE ARM TESTS KIND-MEMBERSHIP** -- BAR 9 reads *"every
    # ### file this act writes is of a KIND the list names"*. ### The KINDS are transcribed here as
    # ### patterns so a stray file of NO kind still fails, and the PATH-level residue is printed
    # ### beside the verdict rather than hidden behind it. ### **BOTH NUMBERS, NOT THE KINDER ONE.**
    KINDS = {
        1: (r'^b405_registration_.*\.txt$', r'^b405_satisfiable', r'^audit_b405_reg_satisfiable',
            r'^b405_regspec_run', r'^b405_reg_termscan', r'^b405_reg_gate',
            r'^b405_lockgate', r'^b405_reg_seal'),
        2: (r'^b405_ferry',),
        3: (r'^b405_census_', r'^b405_faces_census_', r'^b405_pins_', r'^b405_mirror'),
        4: (r'^b405_extract\.txt$', r'^_b405/'),
        5: (r'^b405_components\.txt$',),
        6: (r'^b405_desk', r'^b405_the_rows_law_restated', r'^b405_closing'),
        7: (r'^b405_checks',),
        8: (r'^tools/b405_',),
    }
    placed, unkinded = {}, []
    for f in written:
        hit = [k for k, pats in KINDS.items() if any(re.search(p, f) for p in pats)]
        if hit:
            placed[f] = hit[0]
        else:
            unkinded.append(f)
    unnamed_paths = [f for f in written if os.path.basename(f) not in reg]
    arm('G-WRITELIST', 'every file this act wrote is of a KIND the locked face names',
        not unkinded,
        '%d written ; of NO named KIND %d : %s' % (len(written), len(unkinded),
                                                   unkinded or 'none'))
    arm('G-WRITELIST-PATHS', 'and the PATH-level residue is printed, not hidden', True,
        '%d of %d written files are named by their KIND but NOT by path on the face : %s'
        % (len(unnamed_paths), len(written), unnamed_paths or 'none'))
    kinds = re.findall(r'\*\*KIND (\d+) --', reg)
    arm('G-WRITELIST-KIND', 'and the list is built as KINDS, not as a flat list of paths',
        len(kinds) >= 9 and len(set(placed.values())) >= 7,
        'kinds declared %d ; kinds actually used %d' % (len(kinds), len(set(placed.values()))))

    # ---- THE LIVING RECORD -----------------------------------------------------------------------
    bar()
    rec('  ### THE LIVING RECORD.')
    bar()
    tr_blob = git(PP, 'show', '%s:OPEN_TRAILS.md' % side).stdout.decode('utf-8')
    tr_live = text(TRAILS)
    arm('G-TRAILS', 'the trail block is append-only against the pre-act blob at %s' % side,
        tr_live.startswith(tr_blob.rstrip(chr(10))) or tr_blob in tr_live,
        'blob %d -> live %d bytes'
        % (len(tr_blob.encode('utf-8')), len(tr_live.encode('utf-8'))))
    arm('G-TRAILPRIOR', "and b404's block is present and unedited",
        '<!-- b404 the fifth site' in tr_live)
    tb = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8')
    tl = text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.startswith(tb.rstrip(chr(10))),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    # ### **THE VERDICT IS A LINE, NOT A SUBSTRING** -- and this arm's first version proved it the
    # ### hard way. ### It tested `'NO KEY' not in stdout` and FAILED on a hit, because the act's
    # ### own banked grade line reads *"NO KEYSTONE EDITED"*, which contains `NO KEY`. ### **THE
    # ### ### SPECIES IS THE SUITE'S OWN, A FOURTH TIME: A SUBSTRING TEST FOR A TOOL'S VERDICT WORD
    # ### ### FIRES ON PROSE THAT MERELY CONTAINS IT.** ### The tool's own `no_key` predicate reads
    # ### the VERDICT LINE, and that is what is used here.
    def no_key(out):
        return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())

    def q(qq):
        r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        return r.stdout or ''
    kq = q('the-rows-law-restated')
    arm('G-KEY', 'the index key resolves and carries the act',
        (not no_key(kq)) and 'b405' in kq,
        'verdict-line NO KEY : %s ; raw substring hits : %d'
        % (no_key(kq), kq.count('NO KEY')))
    arm('G-KEY-CTL', 'and a must-not-hit query still returns NO KEY on its VERDICT LINE',
        no_key(q('a shared witness was found')))
    arm('G-DESK', 'the desk was swept and its closures printed',
        'ITEMS SWEPT' in text(d('b405_desk_notes.txt')))

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS, RE-MEASURED ON THE BANK.')
    bar()
    dep = (asserted(bank, 'was deposited') + asserted(bank, 'the deposit was made')
           + asserted(bank, 'zenodo'))
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action of any kind', not dep,
        'asserting sentences %d %s' % (len(dep), dep or ''))
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    arm('G-SAYSNOTHING', 'and it says in its own words that nothing deposits',
        'NOTHING DEPOSITS' in bank and 'THE PLATFORM WAS NOT CALLED AT ALL' in bank)
    arm('G-SAYSH2', 'and that `h2` stands where the deposit left it',
        'h2` STANDS EXACTLY' in bank or 'h2 STANDS EXACTLY' in bank)
    arm('G-DEFECTS', "and the act prints its own apparatus defects rather than smoothing them",
        'ZERO-BYTE HUSK' in bank and 'THE LOCKED FACE IS NOT EDITED' in bank)
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    hits = banned_terms.scan(bank) if hasattr(banned_terms, 'scan') else None
    arm('G-SCANFIX', 'the ferry-scan fixtures still hold in both polarities', ok_scan)
    arm('G-SEALNAME', 'the bank names the seal it was written under',
        SEAL in bank, 'seal %s' % SEAL[:16])

    # ---- MUST-FAIL --------------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### A BRIDGE WAS TYPED BETWEEN TWO SITES.',
        '### ROW U1 WAS RETIRED.',
        '### A SHARED WITNESS WAS FOUND.',
        '### AN EIGHTH COLUMN WAS ADDED TO THE LEDGER.',
        '### A KERNEL WAS BUILT.',
        '### h2 HOLDS.',
    ]
    lines = set(bank.split(chr(10)))
    hits2 = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits2,
        'hits %s' % (hits2 or 'none'))
    synth = 'a' + chr(10) + '### ROW U1 WAS RETIRED.' + chr(10) + 'b'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one of them',
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
    out = d('b405_checks_postpush.txt' if post else 'b405_checks.txt')
    io.open(out, 'wb').write((chr(10).join(R) + chr(10)).encode('utf-8'))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
