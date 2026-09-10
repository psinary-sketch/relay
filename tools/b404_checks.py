# -*- coding: utf-8 -*-
"""b404_checks.py -- THE GATE SUITE FOR THE FIFTH AND SIXTH SITES.

### ### **`G-SCOPE` IS THE ARM THAT MATTERS MOST, BECAUSE IT IS THE DEFECT THE ACT REPORTS.** ### An
### act that convicts a keystone of widening a scoped claim, while itself quoting a claim without
### its scope, would have nothing to say. ### The arm requires every foreign claim in the bank to
### appear beside the sentence that scopes it.
###
### ### **`G-NOBRIDGE` GUARDS THE ROW.** ### Two instances were added to a row whose whole law is
### that it types no bridge. ### The arm reads the row as committed and requires the refusal to be
### present and no equivalence claimed.
###
### ### **`G-NOTBUILT` GUARDS THE ONE THING THE ACT COULD NOT DO.** ### One axiom profile could be
### read and one could not. ### The arm requires the unread one to be REPORTED unread, and requires
### the act to make no claim about what it would have said.
###
### ### **AND EVERY ARM READING A REPOSITORY STATE NAMES ITS REFERENCE AND IS TAKEN AT THE SAME
### ### MOMENT AS WHAT IT MEASURES** (`b401`'s species, sharpened at `b403`, which lost two arms to
### it).
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
import gate_needle as GN          # noqa: E402
import gate_text                  # noqa: E402
import hedge_audit                # noqa: E402
import run_clock                  # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
SE = os.path.join('D:', os.sep, 'SIDE-effects')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
CONS = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
M1 = os.path.join(SE, 'SIDEEffects', 'Phase15', 'Module1.lean')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def text(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


FERRY = d('b404_ferry_2026-09-10.txt')
REG = d('b404_registration_2026-09-10.txt')
BANK = d('b404_the_fifth_and_sixth_sites.txt')
CRUN = d('b404_components_run.txt')
X = json.load(io.open(d('b404_extract.json'), encoding='utf-8'))
CF = json.load(io.open(d('b404_components.json'), encoding='utf-8'))
LG = json.load(io.open(d('b404_lockgate.json'), encoding='utf-8'))
F = X['fig']
SEAL = LG['face_sha']

SELF_NEEDLES = [
    ('the fifth entered', '**COMPONENT 1 : ### ENTERED AS `(v)`.**'),
    ('the sixth entered', '**ADDITION ONE : ### ENTERED AS `(vi)`.**'),
    ('the two kinds minted', 'KIND (a) -- EMPTY BECAUSE THERE IS NOTHING TO RANGE OVER'),
    ('(v) is kind (b)', '**`(v)` IS KIND (b), AND THE PREMISE THE DRAFT REASONED FROM IS FALSE'),
    ('two theorems', '**ADDITION TWO : ### TWO THEOREMS, AND `(N5)`S PARTING POINT REFUTED.**'),
    ('the row is strained', '**COMPONENT 3 : ### STRAINED.**'),
    ('the keystone widened it',
     'its *Axiom-free; core Lean only, no Mathlib* to a DIFFERENT module'),
    ('no axiom claim',
     'the terminals carry axioms. ### **AN IMPORT LINE IS NOT A MEASUREMENT**'),
    ('no bridge typed', 'A THEOREM ABOUT A SHAPE IS NOT A THEOREM ABOUT AN'),
    ('nothing deposits', 'NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED'),
]

R = []


def rec(s=''):
    R.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


ARMS = []


def arm(name, why, ok, detail=''):
    ARMS.append((name, bool(ok)))
    rec('  %-18s %-62s %s' % (name, why[:62], 'PASS' if ok else '### FAIL ###'))
    if detail:
        for k in range(0, min(len(detail), 900), 150):
            rec('      %s' % detail[k:k + 150])
    return bool(ok)


def blob(repo, rel, post=False):
    ref = 'HEAD~1' if post else 'HEAD'
    r = subprocess.run(['git', 'show', ref + ':' + rel], cwd=repo, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def main():
    post = '--post' in sys.argv
    bar('=')
    rec('b404_checks.py -- THE GATE SUITE. ### **EVERY ARM TESTS A BAR THIS FACE SET.**')
    rec('### side of the push : %s ; the pre-act reference is `%s`'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH', 'HEAD~1' if post else 'HEAD'))
    bar('=')
    bank = text(BANK)
    reg = text(REG)
    crun = text(CRUN)

    bar()
    rec('  ### THE HELPERS` FIXTURES, AND THE FACE.')
    bar()
    arm('G-FIXTURE', 'every imported helper passes its own fixtures in both polarities',
        GN.self_test(False) and gate_text.self_test(False) and hedge_audit.self_test(False)
        and ferry_scan.self_test(verbose=False) and all(GD.split_fixture()))
    arm('G-FERRY', 'the ferry is banked at the bytes the face declares',
        os.path.getsize(FERRY) == 3405 and 'paste ends (part 1 of 1)' in text(FERRY))
    arm('G-SEAL', 'the face carries its own lock and the lock gate permitted it',
        SEAL in reg and LG['permits'] is True and LG['gates_read'] == 8
        and LG['face_subject_gates'] == 4, 'sha %s' % SEAL[:16])
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                         'data/b404_registration_2026-09-10.txt'], cwd=ROOT,
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    arm('G-SEALINTACT', 'the sealed body is byte-for-byte what was sealed',
        'SEAL INTACT' in (vr.stdout or ''))
    arm('G-ANCHOR', 'the extract left no read AMBIGUOUS or ABSENT',
        len(X['reads']) == 23 and all(r['verdict'] == 'ANCHORED' for r in X['reads']))
    smiss = []
    for lbl, hint in SELF_NEEDLES:
        try:
            n, _l = GN.build(BANK, hint)
            rec('    %-32s ### `bank:%d`' % (lbl, n))
        except Exception as e:
            smiss.append(lbl)
            rec('    %-32s ### **NOT IN THE BANK** %s' % (lbl, str(e)[:50]))
    arm('G-BANKSAYS', 'every sentence this suite tests for is in the bank as a live line',
        not smiss, '%d of %d' % (len(SELF_NEEDLES) - len(smiss), len(SELF_NEEDLES)))

    # ---- BAR 1 : THE SOURCES ---------------------------------------------------------------------
    bar()
    rec('  ### BAR 1 -- `G-SRC`.')
    bar()
    arm('G-SRC', 'both pinned sources verified before any quotation of them',
        F['sources'] == {'CC': True, 'LG': True} and F['srclocated'] == F['srcreads'])

    # ---- BAR 3 : THE SCOPE -----------------------------------------------------------------------
    bar()
    rec('  ### BAR 3 -- `G-SCOPE`. ### **THE ACT CONVICTS A KEYSTONE OF QUOTING WITHOUT SCOPE;')
    rec('  ### DOING THE SAME WOULD FORFEIT THE FINDING.**')
    bar()
    scoped = {
        'the keystone claim appears with the repository it is about':
            'SIDE-effects' in bank and 'c66f3c5' in bank,
        'the README claim appears with the module it scopes to':
            'a DIFFERENT module' in bank or 'DIFFERENT module' in bank,
        'the README grade for Module1 is quoted exactly':
            'Genuine content, 0 sorry' in bank,
        'and the components carry all three side by side':
            'THE KEYSTONE`S CLAIM' in crun and 'read its whole sentence' in crun,
    }
    for k, v in scoped.items():
        rec('      %-58s : %s' % (k, v))
    arm('G-SCOPE', 'every foreign claim in the bank appears beside the sentence that scopes it',
        all(scoped.values()))

    # ---- BAR 4 : NOT BUILT -----------------------------------------------------------------------
    bar()
    rec('  ### BAR 4 -- `G-NOTBUILT`. ### **ONE PROFILE READ, ONE REPORTED UNREAD.**')
    bar()
    arm('G-NOTBUILT', 'the readable profile is read from a printed file and named as such',
        'AXIOM_PRINTS' in crun and 'READ FROM A PRINTED PROFILE' in crun)
    arm('G-UNREAD', 'and the unreadable one is REPORTED unread, not inferred',
        'REPORTED UNREAD' in bank.upper() and 'NOT INFERRED' in bank.upper()
        and F.get('se_axiomcheck_files') == 0 and not F.get('se_profile_files'))
    # ### **AN ASSERTION-LEVEL PREDICATE, NOT A GREP.** ### The first version searched the bank
    # ### for the phrase and fired on the act's OWN sentence saying the claim is not made -- the
    # ### b317 / b348 / b400 species, a FOURTH time in this session. ### A hit counts only in a
    # ### sentence carrying no negator.
    NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'never',
           '### not ###')

    def asserted(hay, phrase):
        out = []
        for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
            if gate_text.flat(phrase) in gate_text.flat(s) \
                    and not any(g in s.lower() for g in NEG):
                out.append(s[:120])
        return out
    claimed = asserted(bank, 'the terminals carry axioms')
    arm('G-NOAXIOMCLAIM', 'the act ASSERTS nowhere that the terminals carry axioms',
        not claimed and 'AN IMPORT LINE IS NOT A MEASUREMENT' in bank,
        'asserting sentences %d %s' % (len(claimed), claimed or ''))
    arm('G-NOAXIOMCLAIM-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The profile shows the terminals carry axioms.',
                      'the terminals carry axioms')))
    # ### **AN ARM THAT REQUIRES A STATE THE ACT DID NOT CREATE IS MEASURING THE PAST.** ### The
    # ### first version demanded an EMPTY working tree; `SIDE-effects` already carried two
    # ### UNTRACKED guard backups (b304's installer writes when run) before this act began. ###
    # ### The arm now requires `0` TRACKED changes and prints the pre-existing files by name.
    lean = subprocess.run(['git', '-C', SE, 'status', '--porcelain'], capture_output=True,
                          text=True)
    st = [x for x in (lean.stdout or '').split(chr(10)) if x.strip()]
    tracked = [x for x in st if not x.startswith('??')]
    arm('G-NOTOUCH', 'SIDE-effects carries 0 TRACKED changes: this act touched nothing there',
        not tracked,
        'tracked %d ; untracked and PRE-EXISTING %d : %s'
        % (len(tracked), len(st) - len(tracked),
           [x[3:] for x in st if x.startswith('??')] or 'none'))

    # ---- BAR 5 : THE TWO KINDS -------------------------------------------------------------------
    bar()
    rec('  ### BAR 5 -- `G-TWOKINDS`. ### **A VERDICT OF `EMPTY` WITHOUT ITS KIND FAILS.**')
    bar()
    arm('G-TWOKINDS', 'both kinds of emptiness are named and (v) is assigned to one',
        'KIND (a)' in bank and 'KIND (b)' in bank and '`(v)` IS KIND (b)' in bank)
    arm('G-PREMISE', 'and the premise the draft reasoned from is checked, not assumed',
        'NOT** ### a one-L-function corpus' in bank or 'not a one-L-function corpus' in bank
        or 'NOT a one-L-function corpus' in bank)

    # ---- BAR 6 / 8 : THE ROW ---------------------------------------------------------------------
    bar()
    rec('  ### BARS 6 AND 8 -- `G-NOBRIDGE` AND `G-REFUSAL`, READ OFF THE ROW AS COMMITTED.')
    bar()
    ft = text(FACES)
    row = [x for x in ft.split(chr(10)) if x.startswith('| U1 |')]
    row = row[0] if row else ''
    arm('G-NOBRIDGE', 'the row types no bridge and says so of all six',
        'types no bridge between' in row and 'NO EQUIVALENCE IS COMPILED' in row
        and 'NOT TYPED AS A BRIDGE' in row)
    arm('G-REFUSAL', 'the row`s refusal is restated and the deposit`s is quoted beside it',
        'NOTHING IS CLAIMED ABOUT THE EQUIVALENCE' in row
        and 'deliberately **not** compiling the cross-register' in row)
    arm('G-SIX', 'the row now carries six instances',
        all(('**(%s)' % r) in row for r in ('i', 'ii', 'iii', 'iv', 'v', 'vi')))

    # ---- BAR 7 : PRESERVATION --------------------------------------------------------------------
    bar()
    rec('  ### BAR 7 -- `G-PRESERVE`, READ AGAINST THE `%s` BLOB.'
        % ('HEAD~1' if post else 'HEAD'))
    bar()
    fb = blob(PP, 'FACES_LEDGER.md', post)
    ob = [x for x in fb.split(chr(10)) if x.startswith('| U1 |')]
    cells_ok, touched, untouched = False, [], []
    if ob and row:
        oc, nc = GD.split_cells(ob[0]), GD.split_cells(row)
        if len(oc) == len(nc) == 7:
            for k in range(7):
                if k in (4, 6):
                    touched.append(nc[k].startswith(oc[k].rstrip()) and len(nc[k]) > len(oc[k]))
                else:
                    untouched.append(nc[k] == oc[k])
            cells_ok = all(touched) and all(untouched)
    arm('G-PRESERVE', 'five cells BYTE-IDENTICAL, two carrying the pre-act blob as a prefix',
        cells_ok, 'touched-as-prefix %s ; untouched-identical %s' % (touched, untouched))
    tb, tt = blob(PP, 'OPEN_TRAILS.md', post), text(TRAILS)
    arm('G-APPENDONLY', 'the trail block is append-only against the same reference',
        tt.startswith(tb))
    arm('G-NOLOST', 'no line was lost from the faces ledger',
        len(ft.split(chr(10))) == len(fb.split(chr(10))))

    # ---- BAR 11 : NO KEYSTONE --------------------------------------------------------------------
    bar()
    rec('  ### BAR 11 -- `G-NOKEYSTONE`.')
    bar()
    cb = blob(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', post)
    arm('G-NOKEYSTONE', 'the conspiracy keystone is byte-identical to its pre-act blob',
        text(CONS) == cb, 'blob %d bytes' % len(cb.encode('utf-8')))
    arm('G-ROUTED', 'and the widened claim is reported as ROUTED rather than repaired',
        'ROUTED' in bank and 'THE KEYSTONE IS NOT EDITED' in bank.upper())

    # ---- BAR 9 / 10 ------------------------------------------------------------------------------
    bar()
    rec('  ### BARS 9 AND 10 -- THE CAP AND THE WRITE LIST.')
    bar()
    tools = [n for n in sorted(os.listdir(t(''))) if n.startswith('b404_') and n.endswith('.py')]
    arm('G-CAP', 'new relay tool files at most the six the face declares',
        len(tools) == 6, 'wrote %d : %s' % (len(tools), tools))

    def kind(n):
        m = re.match(r'^(.*?)(\d*)(\.[a-z]+)$', n)
        return m.group(1) if m else n

    written = sorted(n for n in os.listdir(D) if n.startswith('b404_')
                     or n.startswith('audit_b404_'))
    unnamed = [n for n in written
               if n not in reg and kind(n) not in reg
               and re.sub(r'_2026-\d\d-\d\d', '_<date>', n) not in reg]
    arm('G-WRITELIST', 'every file this act wrote is of a KIND the locked face names',
        not unnamed, 'files %d ; of an unnamed KIND %d : %s'
        % (len(written), len(unnamed), unnamed or 'none'))

    # ---- BARS 12 / 13 / 14 -----------------------------------------------------------------------
    bar()
    rec('  ### BARS 12, 13 AND 14 -- THE CENSUSES, THE PINS AND THE MIRROR, READ %s.'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'))
    bar()
    for nm, tool in (('G-CENSUS', 'b307_handoff_census.py'), ('G-FACES', 'b327_faces_census.py')):
        cr = subprocess.run([sys.executable, t(tool)], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
        arm(nm, 'the census reports TOTAL MISSING 0 after the act',
            'TOTAL MISSING : 0' in (cr.stdout or ''))
    if post:
        pr = subprocess.run([sys.executable, t('b303_pins.py')], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
        arm('G-PINS', 'all four rostered repositories equal by ls-remote, AFTER THE PUSH',
            '### REPOS HARD-FAILING : 0' in (pr.stdout or ''))
        mrec = text(d('b404_mirror.txt'))
        head = subprocess.run(['git', '-C', PP, 'ls-remote', 'origin', 'refs/heads/main'],
                              capture_output=True, text=True).stdout.split(chr(9))[0].strip()
        arm('G-MIRROR', 'the mirror was rebuilt AFTER the commit and is clean on all three clauses',
            'VERDICT: CLEAN ON ALL THREE CLAUSES' in mrec and head[:7] in mrec)
    else:
        rec('  G-PINS / G-MIRROR   read AFTER THE PUSH only                   ### DEFERRED')

    # ---- BAR 15 : THE CONTROL --------------------------------------------------------------------
    bar()
    rec('  ### BAR 15 -- `G-CONTROL`. ### **EVERY REPOSITORY-STATE ARM NAMES ITS REFERENCE.**')
    bar()
    src = text(t('b404_checks.py'))
    arm('G-CONTROL', 'the blob reader takes a `post` flag and switches HEAD / HEAD~1',
        "ref = 'HEAD~1' if post else 'HEAD'" in src)
    arm('G-CONTROL-USED', 'and every call that reads a pre-act state passes it',
        src.count("blob(PP, '") == src.count(", post)"))

    # ---- THE ROW, THE KEY, THE MUST-FAILS --------------------------------------------------------
    bar()
    rec('  ### THE ROW, THE KEY AND THE MUST-FAIL FIXTURES.')
    bar()
    tb2 = text(TABLE)
    rows = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', tb2, re.M)]
    arm('G-ROW', 'the correspondence row is present once and its number is the last',
        rows[-1] == 253 and tb2.count('THE ROW GAINS TWO SITES AND ITS LAW IS STRAINED') == 1,
        'last row %d' % rows[-1])
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-fifth-and-sixth-sites'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    arm('G-KEY', 'the index key resolves and returns exactly one row',
        (kq.stdout or '').count('act      :') == 1)
    fixtures = ['### A BRIDGE WAS TYPED.', '### THE TERMINALS CARRY AXIOMS.',
                '### A KEYSTONE WAS EDITED.', '### THE ROW WAS RESTATED.',
                '### A KERNEL WAS BUILT.', '### THE CORPUS PROVED ITS BOUNDARY TWICE.']
    lines = set(bank.split(chr(10)))
    hits2 = [f for f in fixtures if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits2,
        'hits %s' % (hits2 or 'none'))
    synth = 'a' + chr(10) + '### A KERNEL WAS BUILT.' + chr(10) + 'b'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one of them',
        any(f in set(synth.split(chr(10))) for f in fixtures))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b404_checks_postpush.txt' if post else 'b404_checks_run.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(R) + chr(10))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main())
