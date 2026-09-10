# -*- coding: utf-8 -*-
"""b403_checks.py -- THE GATE SUITE FOR THE THREE ROUTED ITEMS.

### ### **`G-RULEQUOTED` IS THE ARM AGAINST THE FERRY.** ### The Addition asserted a rule in words
### the record does not use. ### The arm requires the rule this act applied to be locatable in the
### bank of the act that made it, and requires the ferry's own phrasing to be ABSENT -- because if
### it were present, this act's whole account of how it found the rule would be wrong.
###
### ### **`G-CONTROL` IS THE ARM AGAINST THIS SEAT.** ### Component 1's control was defective twice
### and stopped a correct repair twice. ### The arm requires the act to say so, and requires the
### surviving control to be read-only against read-only at the same moment.
###
### ### **`G-NOSTRENGTHEN` GUARDS THE ONE EDIT ON ANOTHER OWNER'S FILE.** ### Nothing was built, so
### nothing may be certified: the repaired README must assert exactly what it asserted before,
### minus a number.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF     # noqa: E402
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
SW = os.path.join('D:', os.sep, 'SIDE-window')
RM = os.path.join(SW, 'README.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
SPAN = os.path.join(ROOT, 'tools', 'b363_span.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def text(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


FERRY = d('b403_ferry_2026-09-10.txt')
REG = d('b403_registration_2026-09-10.txt')
BANK = d('b403_the_three_routed_items.txt')
CRUN = d('b403_components_run3.txt')
X = json.load(io.open(d('b403_extract.json'), encoding='utf-8'))
CF = json.load(io.open(d('b403_components.json'), encoding='utf-8'))
LG = json.load(io.open(d('b403_lockgate.json'), encoding='utf-8'))
F = X['fig']
SEAL = LG['face_sha']

SELF_NEEDLES = [
    ('the counter repaired', '**(i) THE SPAN COUNTER : ### REPAIRED.**'),
    ('the README repaired', 'THE COUNT REMOVED RATHER THAN RESTATED'),
    ('the face routed', 'RULED AND STILL ROUTED'),
    ('43 exact and undated', 'WAS EXACT AT `v0.4` AND UNDATED, NOT WRONG'),
    ('b401 corrected not edited', 'S BANK IS NOT EDITED AND BOTH READINGS ARE PRINTED'),
    ('the control failed twice',
     'COMPONENT 1 STOPPED A CORRECT REPAIR TWICE, AND BOTH TIMES THE DEFECT WAS IN THE'),
    ('the control species', 'A CONTROL MUST MATCH THE TREATMENT IN EVERYTHING EXCEPT THE'),
    ('nothing may be certified', 'NOTHING WAS BUILT, SO NOTHING MAY'),
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
    rec('  %-16s %-64s %s' % (name, why[:64], 'PASS' if ok else '### FAIL ###'))
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
    rec('b403_checks.py -- THE GATE SUITE. ### **EVERY ARM TESTS A BAR THIS FACE SET.**')
    rec('### side of the push : %s ; the pre-act reference is `%s`'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH', 'HEAD~1' if post else 'HEAD'))
    bar('=')
    bank = text(BANK)
    reg = text(REG)
    crun = text(CRUN)
    rm = text(RM)

    bar()
    rec('  ### THE HELPERS` FIXTURES, AND THE FACE.')
    bar()
    arm('G-FIXTURE', 'every imported helper passes its own fixtures in both polarities',
        GN.self_test(False) and gate_text.self_test(False) and hedge_audit.self_test(False)
        and ferry_scan.self_test(verbose=False) and all(GD.split_fixture()))
    arm('G-FERRY', 'the ferry is banked at the bytes and lines the face declares',
        os.path.getsize(FERRY) == 1697 and 'paste ends (part 1 of 1)' in text(FERRY))
    arm('G-SEAL', 'the face carries its own lock and the lock gate permitted it',
        SEAL in reg and LG['permits'] is True and LG['gates_read'] == 8
        and LG['face_subject_gates'] == 4, 'sha %s' % SEAL[:16])
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                         'data/b403_registration_2026-09-10.txt'], cwd=ROOT,
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    arm('G-SEALINTACT', 'the sealed body is byte-for-byte what was sealed',
        'SEAL INTACT' in (vr.stdout or ''))
    arm('G-ANCHOR', 'the extract left no read AMBIGUOUS or ABSENT',
        len(X['reads']) == 12 and all(r['verdict'].startswith('ANCHORED') for r in X['reads']))
    smiss = []
    for lbl, hint in SELF_NEEDLES:
        try:
            n, _l = GN.build(BANK, hint)
            rec('    %-40s ### `bank:%d`' % (lbl, n))
        except Exception as e:
            smiss.append(lbl)
            rec('    %-40s ### **NOT IN THE BANK** %s' % (lbl, str(e)[:50]))
    arm('G-BANKSAYS', 'every sentence this suite tests for is in the bank as a live line',
        not smiss, '%d of %d' % (len(SELF_NEEDLES) - len(smiss), len(SELF_NEEDLES)))

    # ---- BAR 1 -----------------------------------------------------------------------------------
    bar()
    rec('  ### BAR 1 -- `G-RULEQUOTED`. ### **THE RULE IS THE RECORD`S, NOT THE FERRY`S.**')
    bar()
    ok_loc = True
    for f, h in ((d('b371_the_first_target.txt'), 'THE COUNT IS REMOVED RATHER THAN UPDATED'),
                 (d('b372_registration_2026-09-08.txt'),
                  'REMOVED RATHER THAN RESTATED**, unless the document'),
                 (d('b372_registration_2026-09-08.txt'),
                  'IF THE REPAIR WOULD REWRITE A CLAIM RATHER THAN A NUMBER')):
        try:
            AF.find(f, h)
        except Exception:
            ok_loc = False
    arm('G-RULEQUOTED', 'the rule applied is locatable in the bank of the act that made it', ok_loc)
    # ### **AND THE OTHER POLARITY, WHICH IS WHAT MAKES THE ACCOUNT CHECKABLE.**
    # ### **THIS ARM MEASURES A STATE THIS ACT CHANGED, SO IT NAMES ITS REFERENCE.** ### The first
    # ### version read the record as it stands NOW -- and found the phrase in `OPEN_TRAILS.md`,
    # ### which is where THIS ACT wrote it while saying it was absent. ### **THE THIRD APPEARANCE
    # ### ### OF ONE SPECIES IN ONE SESSION** (`b400`'s `G-ONEQ`, `b401`'s `G-PRESERVE`, this).
    # ### The arm now reads the PRE-ACT state: this act's own files are excluded, and the papers
    # ### ledgers are read from their committed blob rather than from disk.
    PHRASE = 'carries its ref or is not written'
    corpus, where = 0, []
    for dp, _dn, fn in os.walk(D):
        if '.git' in dp:
            continue
        for fn2 in fn:
            if not fn2.endswith('.txt') or fn2.startswith('b403_') \
                    or fn2.startswith('audit_b403_'):
                continue
            try:
                if PHRASE in text(os.path.join(dp, fn2)):
                    corpus += 1
                    where.append(fn2)
            except OSError:
                pass
    for rel in ('OPEN_TRAILS.md', 'FACES_LEDGER.md', 'FINDINGS.md'):
        if PHRASE in blob(PP, rel, post):
            corpus += 1
            where.append(rel + ' (pre-act blob)')
    arm('G-FERRYWORDS', 'the ferry`s phrasing is ABSENT from the record as it stood before this act',
        corpus == 0,
        'sites outside this act, papers read from the `%s` blob : %d %s'
        % ('HEAD~1' if post else 'HEAD', corpus, where or 'none'))

    # ---- BAR 2 / 3 / 4 : THE README --------------------------------------------------------------
    bar()
    rec('  ### BARS 2, 3 AND 4 -- THE ORIGINAL, THE REMOVAL, AND WHAT MAY NOT BE STRENGTHENED.')
    bar()
    orig = text(d('b403_readme_original.txt'))
    arm('G-PRESERVE', 'the original README is banked verbatim and carries the claiming sentence',
        'all 43 terminals are fully axiom-free' in orig,
        'banked original %d bytes' % len(orig.encode('utf-8')))
    swb = blob(SW, 'README.md', post)
    arm('G-PRESERVE-BLOB',
        'and the banked original equals the pre-act committed blob, read against `%s`'
        % ('HEAD~1' if post else 'HEAD'),
        orig.replace(chr(13) + chr(10), chr(10)) == swb,
        'blob %d bytes' % len(swb.encode('utf-8')))
    arm('G-REMOVED', 'the removed figure is absent from the claiming sentence afterwards',
        'all 43 terminals are fully axiom-free**' not in rm
        and 'every terminal the `AxiomCheck*.lean` files in this tree print is axiom-free' in rm)
    arm('G-HISTORY', 'and the superseded wording is preserved in the file, dated',
        'previously read "all 43 terminals are fully axiom-free"' in rm
        and 'Repaired 2026-09-10' in rm)
    arm('G-NOSTRENGTHEN', 'the axiom claim is neither strengthened nor weakened',
        'no axioms at all*' in rm.replace(chr(10), ' ')
        and 'not terminals certified by a run' in rm)
    arm('G-NOBUILD', 'and nothing in SIDE-window was built or touched but its README',
        subprocess.run(['git', '-C', SW, 'status', '--porcelain'], capture_output=True,
                       text=True).stdout.strip() in ('M README.md', ' M README.md', ''),
        'working tree : %r' % subprocess.run(['git', '-C', SW, 'status', '--porcelain'],
                                             capture_output=True, text=True).stdout.strip()[:60])

    # ---- BAR 5 / 6 : THE COUNTER -----------------------------------------------------------------
    bar()
    rec('  ### BARS 5 AND 6 -- `G-NOFIGURE` AND `G-BOTHRUNS`.')
    bar()
    span = text(SPAN)
    arm('G-REPAIRED', 'the counter cites (R1) at b366 and keeps its superseded sentence',
        '(R1)' in span and 'b366' in span
        and 'THERE IS NO DECLARED THRESHOLD ANYWHERE IN THE RECORD' in span)
    arm('G-NOFIGURE', 'no figure the counter prints moved across the repair',
        CF['c1_moved'] == 0 and CF['c1'] == 'REPAIRED',
        'sites %s ; moved %s ; control : %s'
        % (CF['c1_sites'], CF['c1_moved'], CF.get('c1_control')))
    arm('G-BOTHRUNS', 'both runs are banked so a reader can diff them without re-running',
        os.path.exists(d('b403_span_before.txt')) and os.path.exists(d('b403_span_after.txt')))
    sj = json.load(io.open(d('b403_span.json'), encoding='utf-8'))
    arm('G-THRESHOLDNOW', 'and the counter now reports the ruled threshold',
        sj.get('threshold') == 9 and sj.get('threshold_declared') is True
        and sj.get('threshold_ruling') == '(R1) at b366')

    # ---- BAR 7 : THE CORRECTION ------------------------------------------------------------------
    bar()
    rec('  ### BAR 7 -- `G-CORRECTION`. ### **BOTH FIGURES, AND b401`S BANK UNTOUCHED.**')
    bar()
    b401 = text(d('b401_the_absent_element_searched.txt'))
    b401b = blob(ROOT if False else ROOT, 'x') if False else None
    r = subprocess.run(['git', 'show', ('HEAD~1' if post else 'HEAD')
                        + ':data/b401_the_absent_element_searched.txt'],
                       cwd=ROOT, capture_output=True)
    b401blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    arm('G-CORRECTION', 'both figures are in this act`s bank and b401`s bank is byte-identical',
        str(F['prints_without_localmodel']) in bank and str(F['prints_total']) in bank
        and b401 == b401blob,
        'b401 bank %d bytes == its blob : %s' % (len(b401.encode('utf-8')), b401 == b401blob))

    # ---- BAR 8 : NO FIFTH ------------------------------------------------------------------------
    bar()
    rec('  ### BAR 8 -- `G-NOFIFTH`. ### **ROW `U1` GAINS NOTHING.**')
    bar()
    fb = blob(PP, 'FACES_LEDGER.md', post)
    ft = text(FACES)
    arm('G-NOFIFTH', 'the faces ledger is byte-identical: no instance was added', fb == ft)
    arm('G-SAIDFOURTH', 'and the act states that the fifth site is already the fourth',
        'already its fourth' in bank.lower() or 'ALREADY THE ROW`S FOURTH' in bank
        or 'is already its fourth' in text(TRAILS))

    # ---- BAR 9 / 10 ------------------------------------------------------------------------------
    bar()
    rec('  ### BARS 9 AND 10 -- THE CAP AND THE WRITE LIST.')
    bar()
    tools = [n for n in sorted(os.listdir(t(''))) if n.startswith('b403_') and n.endswith('.py')]
    arm('G-CAP', 'new relay tool files at most the six the face declares',
        len(tools) == 6, 'wrote %d : %s' % (len(tools), tools))

    def kind(n):
        m = re.match(r'^(.*?)(\d*)(\.[a-z]+)$', n)
        return m.group(1) if m else n

    written = sorted(n for n in os.listdir(D) if n.startswith('b403_')
                     or n.startswith('audit_b403_'))
    unnamed = [n for n in written
               if n not in reg and kind(n) not in reg
               and re.sub(r'_2026-\d\d-\d\d', '_<date>', n) not in reg]
    # ### **THE FACE SET THIS BAR AS `PRINT THE RESIDUE WHETHER EMPTY OR NOT`, NOT AS `ZERO`.**
    arm('G-WRITELIST', 'the residue is measured and printed, and the bank names it',
        all(n in bank for n in unnamed),
        'files %d ; of an unnamed KIND %d : %s' % (len(written), len(unnamed), unnamed or 'none'))

    # ---- BAR 11 ----------------------------------------------------------------------------------
    bar()
    rec('  ### BAR 11 -- `G-NOINSTRUMENT`.')
    bar()
    lean = subprocess.run(['git', '-C', SW, 'status', '--porcelain', '--', '*.lean'],
                          capture_output=True, text=True)
    arm('G-NOINSTRUMENT', 'no `.lean` file is touched in SIDE-window',
        not (lean.stdout or '').strip())
    arm('G-NOHOOK', 'SIDE-window still has no pre-push guard and none was installed',
        not os.path.exists(os.path.join(SW, '.git', 'hooks', 'pre-push')))

    # ---- BAR 15 : THE CONTROL --------------------------------------------------------------------
    bar()
    rec('  ### BAR 15 -- `G-CONTROL`. ### **AN ARM THAT STOPS A CORRECT REPAIR IS A DEFECT.**')
    bar()
    arm('G-CONTROL', 'the act says its own control was defective twice, and names both',
        'STOPPED A CORRECT REPAIR TWICE' in bank
        and 'BEFORE THE RECORD CHANGED' in bank.upper()
        and 'MEASURES THE FLAG' in bank.upper())
    arm('G-CONTROL-MATCHED', 'and the surviving control is read-only against read-only',
        'READ-ONLY, matching the before run' in crun)

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
        loc = subprocess.run(['git', '-C', SW, 'rev-parse', 'HEAD'], capture_output=True,
                             text=True).stdout.strip()
        rem = subprocess.run(['git', '-C', SW, 'ls-remote', 'origin', 'refs/heads/main'],
                             capture_output=True, text=True).stdout.split(chr(9))[0].strip()
        arm('G-PIN-WINDOW', 'and SIDE-window`s own pin is read back, it not being on the roster',
            loc == rem and len(loc) == 40, 'local %s ; remote %s' % (loc[:12], rem[:12]))
        mrec = text(d('b403_mirror.txt'))
        head = subprocess.run(['git', '-C', PP, 'ls-remote', 'origin', 'refs/heads/main'],
                              capture_output=True, text=True).stdout.split(chr(9))[0].strip()
        arm('G-MIRROR', 'the mirror was rebuilt AFTER the commit and is clean on all three clauses',
            'VERDICT: CLEAN ON ALL THREE CLAUSES' in mrec and head[:7] in mrec)
    else:
        rec('  G-PINS / G-PIN-WINDOW / G-MIRROR   read AFTER THE PUSH only     ### DEFERRED')

    # ---- THE ROW, THE KEY, THE MUST-FAILS --------------------------------------------------------
    bar()
    rec('  ### THE ROW, THE KEY AND THE MUST-FAIL FIXTURES.')
    bar()
    tb2 = text(TABLE)
    rows = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', tb2, re.M)]
    arm('G-ROW', 'the correspondence row is present once and its number is the last',
        rows[-1] == 252 and tb2.count('THE RULE EXISTED, THE FIGURE WAS EXACT AND UNDATED') == 1,
        'last row %d' % rows[-1])
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-three-routed-items'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    arm('G-KEY', 'the index key resolves and returns exactly one row',
        (kq.stdout or '').count('act      :') == 1)
    fixtures = ['### A LOCKED FACE WAS EDITED.', '### THE AXIOM CLAIM WAS CERTIFIED.',
                '### A SPECIES WAS MINTED.', '### THE FIFTH SITE WAS ENTERED.',
                '### A KERNEL WAS BUILT.', '### THE FIGURE WAS RESTATED.']
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
    out = d('b403_checks_postpush.txt' if post else 'b403_checks_run.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(R) + chr(10))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main())
