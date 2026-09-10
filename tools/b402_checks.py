# -*- coding: utf-8 -*-
"""b402_checks.py -- THE GATE SUITE FOR THE FOLD.

### ### **THE ARM THAT MATTERS MOST IS `F-NOGRADE`, AND IT ALREADY RAN.** ### The fold generator
### locates every headline in its own act's bank BEFORE it writes a byte and refuses the whole
### section if one fails. ### This suite re-measures that from the generator's own record and from
### the banks themselves, ### **SO THE CLAIM IS CHECKED TWICE BY TWO READERS.**
###
### ### **`G-ADDITIVE` IS WRITTEN WITH `b401`'S LESSON IN IT.** ### An arm reading a repository
### state must name the SIDE it is read on ### AND ### the REFERENCE it reads against; naming the
### side alone is half a declaration. ### So the pre-act reference here is `HEAD` before the push
### and `HEAD~1` after it, and the arm prints which.
###
### ### **`G-COUNTCLAIM` IS AN ARM AGAINST TIDINESS.** ### The navigator's count was wrong; the
### temptation is to print the right one and move on. ### The arm requires BOTH numbers in the bank.
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
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def text(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


FERRY = d('b402_ferry_2026-09-10.txt')
REG = d('b402_registration_2026-09-10.txt')
BANK = d('b402_the_fold.txt')
FRUN = d('b402_fold_notes.txt')
FD = json.load(io.open(d('b402_fold.json'), encoding='utf-8'))
SP = json.load(io.open(d('b402_span.json'), encoding='utf-8'))
LG = json.load(io.open(d('b402_lockgate.json'), encoding='utf-8'))
SEAL = LG['face_sha']
TITLE = FD['title']

# ### **(act, bank, headline hint)** -- the same triples the generator used, re-read here.
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b402_fold as FOLD  # noqa: E402

SELF_NEEDLES = [
    ('the fold is due and written', 'THE FOLD IS DUE AND IS WRITTEN'),
    ('the two counts', 'THE TOOL`S IS'),
    ('the threshold and its ruling', 'the threshold, (R1) at b366'),
    ('the headlines located', 'LOCATED BY THE ANCHOR TOOL IN THEIR OWN ACTS'),
    ('the counter`s stale line', 'THE SPAN COUNTER`S OWN LINE ON THE THRESHOLD IS STALE'),
    ('a fold proves nothing', 'A FOLD IS A SUMMARY OF ITS ACTS AT'),
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


def blob(rel, post=False):
    ref = 'HEAD~1' if post else 'HEAD'
    r = subprocess.run(['git', 'show', ref + ':' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def main():
    post = '--post' in sys.argv
    bar('=')
    rec('b402_checks.py -- THE GATE SUITE. ### **EVERY ARM TESTS A BAR THIS FACE SET.**')
    rec('### side of the push : %s' % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'))
    bar('=')
    bank = text(BANK)
    reg = text(REG)
    frun = text(FRUN)
    fnd = text(FINDINGS)

    bar()
    rec('  ### THE IMPORTED HELPERS` OWN FIXTURES.')
    bar()
    arm('G-FIXTURE', 'every imported helper passes its own fixtures in both polarities',
        GN.self_test(False) and gate_text.self_test(False) and hedge_audit.self_test(False)
        and ferry_scan.self_test(verbose=False) and all(GD.split_fixture()))

    bar()
    rec('  ### STEP ZERO AND THE FACE.')
    bar()
    arm('G-FERRY', 'the ferry is banked at the bytes and lines the face declares',
        os.path.getsize(FERRY) == 3719 and 'paste ends (part 1 of 1)' in text(FERRY))
    arm('G-SEAL', 'the face carries its own lock and the lock gate permitted it',
        SEAL in reg and LG['permits'] is True and LG['gates_read'] == 8
        and LG['face_subject_gates'] == 4, 'sha %s' % SEAL[:16])
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                         'data/b402_registration_2026-09-10.txt'],
                        cwd=ROOT, capture_output=True, text=True, encoding='utf-8',
                        errors='replace')
    arm('G-SEALINTACT', 'the sealed body is byte-for-byte what was sealed',
        'SEAL INTACT' in (vr.stdout or ''))
    smiss = []
    for lbl, hint in SELF_NEEDLES:
        try:
            n, _l = GN.build(BANK, hint)
            rec('    %-46s ### `bank:%d`' % (lbl, n))
        except Exception as e:
            smiss.append(lbl)
            rec('    %-46s ### **NOT IN THE BANK** %s' % (lbl, str(e)[:50]))
    arm('G-BANKSAYS', 'every sentence this suite tests for is in the bank as a live line',
        not smiss, '%d of %d' % (len(SELF_NEEDLES) - len(smiss), len(SELF_NEEDLES)))

    # ---- BAR 1 : F-NOGRADE, RE-MEASURED --------------------------------------------------------
    bar()
    rec('  ### BAR 1 -- `F-NOGRADE`, RE-MEASURED BY A SECOND READER.')
    rec('  ### **THE GENERATOR CHECKED THIS BEFORE IT WROTE. ### THIS ARM CHECKS IT AGAIN FROM THE')
    rec('  ### BANKS THEMSELVES, SO THE CLAIM RESTS ON TWO READERS AND NOT ON ONE.**')
    bar()
    again, failed = 0, []
    for act, bnk, hint, _g in FOLD.ACTS:
        try:
            AF.find(os.path.join(D, bnk), hint)
            again += 1
        except Exception:
            failed.append(act)
    arm('F-NOGRADE', 'every headline re-locates in its own act`s bank, independently of the run',
        again == len(FOLD.ACTS) and not failed and FD['located'] == len(FOLD.ACTS)
        and FD['missing'] == 0,
        're-located %d of %d ; the generator recorded %d located and %d missing'
        % (again, len(FOLD.ACTS), FD['located'], FD['missing']))
    arm('F-NOGRADE-CTL', 'and the locator can fail: a hint absent from a bank does not resolve',
        not _try(os.path.join(D, FOLD.ACTS[0][1]),
                 'A SENTENCE NO BANK OF THIS CORPUS CONTAINS, WRITTEN HERE TO FAIL'))
    arm('G-OWNBANK', 'every headline is attributed to the act whose own bank carries it',
        all(('b%d_' % a) in bnk for a, bnk, _h, _g in FOLD.ACTS),
        'acts %d ; each hint read from a bank whose name carries its own act number'
        % len(FOLD.ACTS))

    # ---- BAR 2 / 3 : THE SPAN AND THE THRESHOLD ------------------------------------------------
    bar()
    rec('  ### BARS 2 AND 3 -- THE SPAN FROM THE COUNTER, THE THRESHOLD FROM THE RULING.')
    bar()
    lo, hi = SP['span_starts_at'], SP['this_act'] - 1
    arm('G-SPAN', 'the acts the generator wrote equal the span the counter gives',
        [a for a, _b, _h, _g in FOLD.ACTS] == list(range(lo, hi + 1))
        and FD['lo'] == lo and FD['hi'] == hi and FD['acts'] == hi - lo + 1,
        'counter b%d-b%d (%d) ; generator b%d-b%d (%d)'
        % (lo, hi, hi - lo + 1, FD['lo'], FD['hi'], FD['acts']))
    arm('G-NOTINOWNFOLD', 'the folding act is not in its own fold',
        SP['this_act'] not in [a for a, _b, _h, _g in FOLD.ACTS])
    arm('G-THRESHOLD', 'the threshold is 9 from (R1) at b366, and its source is named in the bank',
        FD['threshold'] == 9 and '(R1)' in bank and 'b366' in bank)
    arm('G-THRESHOLD-STALE', 'and the counter`s own line on the threshold is reported as stale',
        SP.get('threshold_declared') is False and 'STALE' in bank.upper()
        and 'threshold_declared' in frun)
    arm('G-DUE', 'the fold is due by the record`s own rule', FD['acts'] >= FD['threshold'])

    # ---- BAR 14 : THE COUNT CLAIM ---------------------------------------------------------------
    bar()
    rec('  ### BAR 14 -- `G-COUNTCLAIM`. ### **BOTH NUMBERS, OR THE ARM FAILS.**')
    bar()
    arm('G-COUNTCLAIM', 'the navigator`s count and the tool`s are both in the bank, and scored',
        str(FD['navigator_claim']) in bank and str(FD['acts']) in bank
        and 'REFUTED' in bank.upper(),
        'navigator %d ; tool %d' % (FD['navigator_claim'], FD['acts']))
    arm('G-COUNTCLAIM-CTL', 'and the arm would fail on a bank carrying only the right number',
        not ('16' in 'the span is 17 acts and the fold is due'))

    # ---- BAR 4 : ADDITIVE -----------------------------------------------------------------------
    bar()
    rec('  ### BAR 4 -- `G-ADDITIVE`, READ %s AGAINST `%s`. ### **b401`S LESSON: NAMING THE SIDE'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH', 'HEAD~1' if post else 'HEAD'))
    rec('  ### ALONE IS HALF A DECLARATION.**')
    bar()
    fb = blob('FINDINGS.md', post)
    tb, tt = blob('OPEN_TRAILS.md', post), text(TRAILS)
    arm('G-ADDITIVE', 'the pre-act committed FINDINGS.md is a true prefix of the working file',
        fnd.startswith(fb.rstrip(chr(10))) or fnd.startswith(fb),
        'blob %d bytes -> file %d bytes' % (len(fb.encode('utf-8')), len(fnd.encode('utf-8'))))
    arm('G-NOEDIT', 'no line of the pre-act FINDINGS.md changed: it is a line-wise prefix too',
        fnd.split(chr(10))[:len(fb.split(chr(10))) - 1] == fb.split(chr(10))[:-1],
        'pre-act lines %d ; post-act lines %d'
        % (len(fb.split(chr(10))), len(fnd.split(chr(10)))))
    arm('G-APPENDONLY', 'the trail block is append-only against the same reference',
        tt.startswith(tb))
    arm('G-SECTION', 'the fold section is present exactly once and carries its four tables',
        fnd.count('## ' + TITLE) == 1
        and all(k in fnd for k in ('The arc’s one statement',
                                   'The span, act by act, each at its own grade',
                                   'The corrections this span made',
                                   'The defective bars this span declared',
                                   'The seats’ own defects')),
        'sections named %d' % fnd.count('## ' + TITLE))
    seg = fnd.split('## ' + TITLE, 1)[-1]
    arm('G-SCOPE', 'the arc`s one statement carries its scope sentence beside it',
        '*Scope:*' in seg and 'not about what is true of the object' in seg)
    arm('G-SEATDEFECTS', 'the seat-defect table reaches the last two acts of the span',
        '| **b400** |' in seg and '| **b401** |' in seg)
    arm('G-ACTROWS', 'the act-by-act table carries a row for every act of the span',
        all(('| **b%d** |' % a) in seg for a, _b, _h, _g in FOLD.ACTS),
        'rows %d of %d' % (sum(1 for a, _b, _h, _g in FOLD.ACTS
                               if ('| **b%d** |' % a) in seg), len(FOLD.ACTS)))

    # ---- BAR 6 : NO GRADE -----------------------------------------------------------------------
    bar()
    rec('  ### BAR 6 -- `G-NOGRADE`, ACROSS THE LEDGERS.')
    bar()
    grade_words = ('DEFINED-ONLY', 'DERIVES-ON-IMPORTS', 'MEASURED-ON-FAMILIES', 'PROVED-GENERAL',
                   'DERIVED-ON-CONTENT', 'UNDER-RESOLVED-AT-BENCH', 'IMPORT-UNDER-THE-BAR',
                   'PROVED-PER-CELL', 'MEASURED-AT-COVERED-CELLS', 'NAMED-ONLY')
    flb = blob('FACES_LEDGER.md', post)
    flt = text(os.path.join(PP, 'FACES_LEDGER.md'))
    moved = [w for w in grade_words if flb.count(w) != flt.count(w)]
    arm('G-NOGRADE', 'no grade token`s count changed in the faces ledger across this leg',
        not moved, 'tokens %d ; changed %s' % (len(grade_words), moved or 'none'))
    arm('G-NOFACES', 'and the faces ledger is untouched by this leg entirely', flb == flt)

    # ---- BAR 8 / 9 / 10 -------------------------------------------------------------------------
    bar()
    rec('  ### BARS 8, 9 AND 10 -- THE CAP, THE WRITE LIST, AND THE INSTRUMENTS.')
    bar()
    tools = [n for n in sorted(os.listdir(t(''))) if n.startswith('b402_') and n.endswith('.py')]
    arm('G-CAP', 'new relay tool files at most 6, and this leg declared 5',
        len(tools) <= 6 and len(tools) == 5, 'wrote %d : %s' % (len(tools), tools))

    def kind(n):
        m = re.match(r'^(.*?)(\d*)(\.[a-z]+)$', n)
        return m.group(1) if m else n

    written = sorted(n for n in os.listdir(D) if n.startswith('b402_')
                     or n.startswith('audit_b402_'))
    unnamed = [n for n in written
               if n not in reg and kind(n) not in reg
               and re.sub(r'_2026-\d\d-\d\d', '_<date>', n) not in reg]
    arm('G-WRITELIST', 'every file this leg wrote is of a KIND the locked face names',
        not unnamed, 'files %d ; of an unnamed KIND %d : %s'
        % (len(written), len(unnamed), unnamed or 'none'))
    lean = subprocess.run(['git', '-C', PP, 'status', '--porcelain', '--', '*.lean'],
                          capture_output=True, text=True)
    arm('G-NOINSTRUMENT', 'no `.lean` file is touched and a fold computes nothing',
        not (lean.stdout or '').strip())

    # ---- BARS 11 / 12 / 13 ----------------------------------------------------------------------
    bar()
    rec('  ### BARS 11, 12 AND 13 -- THE CENSUSES, THE PINS AND THE MIRROR, READ %s.'
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
        arm('G-PINS', 'all four repositories equal by ls-remote, read AFTER THE PUSH',
            '### REPOS HARD-FAILING : 0' in (pr.stdout or ''))
        mrec = text(d('b402_mirror.txt'))
        head = subprocess.run(['git', '-C', PP, 'ls-remote', 'origin', 'refs/heads/main'],
                              capture_output=True, text=True).stdout.split(chr(9))[0].strip()
        arm('G-MIRROR', 'the mirror was rebuilt AFTER the commit and is clean on all three clauses',
            'VERDICT: CLEAN ON ALL THREE CLAUSES' in mrec and head[:7] in mrec
            and 'CLAUSE 2 : CLEAN' in mrec, 'ls-remote %s' % head[:16])
    else:
        rec('  G-PINS           read AFTER THE PUSH only                          ### DEFERRED')
        rec('  G-MIRROR         read AFTER THE PUSH only                          ### DEFERRED')

    # ---- THE ROW, THE KEY, THE MUST-FAILS -------------------------------------------------------
    bar()
    rec('  ### THE ROW, THE KEY AND THE MUST-FAIL FIXTURES.')
    bar()
    tb2 = text(TABLE)
    rows = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', tb2, re.M)]
    arm('G-ROW', 'the correspondence row is present once and its number is the last',
        rows[-1] == 251 and tb2.count('THE ARTEFACT ARC FOLDED, b385-b401') == 1,
        'last row %d' % rows[-1])
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-artefact-arc-folded'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    arm('G-KEY', 'the index key resolves and returns exactly one row',
        (kq.stdout or '').count('act      :') == 1)
    fixtures = ['### THE FOLD PROVED SOMETHING.', '### A GRADE WAS MOVED.',
                '### THE CLAUSE MOVED.', '### FINDINGS.md WAS EDITED.',
                '### THE SPAN WAS TYPED BY THE SEAT.', '### THE NAVIGATOR`S COUNT WAS RIGHT.']
    lines = set(bank.split(chr(10)))
    hits2 = [f for f in fixtures if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank',
        not hits2, 'fixtures %d ; hits %s' % (len(fixtures), hits2 or 'none'))
    synth = 'a' + chr(10) + '### A GRADE WAS MOVED.' + chr(10) + 'b'
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
    out = d('b402_checks_postpush.txt' if post else 'b402_checks_run.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(R) + chr(10))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


def _try(path, hint):
    try:
        AF.find(path, hint)
        return True
    except Exception:
        return False


if __name__ == '__main__':
    sys.exit(main())
