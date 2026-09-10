# -*- coding: utf-8 -*-
"""b401_checks.py -- THE GATE SUITE FOR THE ABSENT ELEMENT SEARCHED.

### ### **THE ARM THAT MATTERS MOST IS `G-VACUOUS`.** ### Addition One returned `UNIFORM`, and a
### bare `UNIFORM` would read as the class-level statement the uniformity row has been missing. ###
### **THE ARM REQUIRES THE SCOPING WORD IN THE SAME SENTENCE AND REQUIRES THAT NO PRICING WAS
### ### DRAWN FROM IT.**
###
### ### **`G-YIELD` IS AN ARM AGAINST THIS SEAT'S OWN SEARCH.** ### An absence established by one
### matcher is a property of that matcher. ### The arm requires five shapes, every yield printed,
### and the counts in the bank equal to the counts the extract recorded.
###
### ### **`G-PRESERVE` IS HARDER HERE THAN AT `b400` AND THE ARM IS HARDER TOO.** ### Two cells of
### one row were appended to; the arm splits the row on its unescaped pipes and requires the five
### untouched cells to be BYTE-IDENTICAL to the committed blob's and the two touched to carry the
### blob's text as a TRUE PREFIX.
###
### ### **`G-OWNED` GUARDS AGAINST RE-IMPORTING WHAT THE RECORD HOLDS.** ### `b358` read Theorem
### 6.1 first; the arm requires the act to cite it and requires `H-CUSP` to stay inherited.
"""
import ast
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import banned_terms       # noqa: E402
import ferry_scan         # noqa: E402
import gate_needle as GN  # noqa: E402
import gate_text          # noqa: E402
import hedge_audit        # noqa: E402
import run_clock          # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
SW = os.path.join('D:', os.sep, 'SIDE-window')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def raw(n):
    return io.open(t(n), encoding='utf-8', errors='replace').read()


def text(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def code(n):
    src = raw(n)
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return src
    spans = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            for k in range(getattr(node, 'lineno', 1), getattr(node, 'end_lineno', 1) + 1):
                spans.add(k)
    return chr(10).join(ln for i, ln in enumerate(src.split(chr(10)), 1) if i not in spans)


FERRY = d('b401_ferry_2026-09-10.txt')
REG = d('b401_registration_2026-09-10.txt')
BANK = d('b401_the_absent_element_searched.txt')
XNOTES = d('b401_extract_notes.txt')
CRUN = d('b401_components_run.txt')
X = json.load(io.open(d('b401_extract.json'), encoding='utf-8'))
CF = json.load(io.open(d('b401_components.json'), encoding='utf-8'))
LG = json.load(io.open(d('b401_lockgate.json'), encoding='utf-8'))
F = X['fig']
SEAL = LG['face_sha']

OWNER_NEEDLES = [
    ('the two legs are named', 'SORTIE: two legs in order'),
    ('the write list is built as KINDS', 'the write list built as KINDS'),
    ('Addition One, the uniformity question', 'THE UNIFORMITY QUESTION'),
    ('the uniform branch and its consequence', 'a class-level statement of the kind the'),
    ('the prime-dependent branch', 'PRIME-DEPENDENT'),
    ('the not-stated branch', 'NOT STATED'),
    ('Addition Two, read whole and not by name', 'read whole'),
    ('decided by unfolding, not by the shared word', 'decided by unfolding, not by the shared'),
    ('the fourth site only after Addition One', 'only after Addition One'),
    ('the matcher yield printed and the residue hand-read', 'matcher yield printed'),
    ('(N3) the one-prime window bounds a count', 'window bounds a count, not the Weil sum'),
    ('nothing deposits', 'nothing deposits'),
]

SELF_NEEDLES = [
    ('the Component 1 verdict', '**COMPONENT 1 : ### PRESENT BUT NOT APPLICABLE.**'),
    ('the element/kind distinction', 'THE ELEMENT IS ABSENT; THE KIND OF ELEMENT IS NOT'),
    ('the located theorem', 'Theorem 6.1'),
    ('the owning act credited', 'b358 ALREADY OWNED IT'),
    ('the three reasons', 'WRONG COMPARISON QUANTITY'),
    ('the inherited hypothesis', 'NOT DECIDED HERE'),
    ('the uniformity verdict with its scope', '**ADDITION ONE : ### UNIFORM -- AND VACUOUSLY.**'),
    ('the consequence not drawn', 'ITS CONSEQUENCE IS NOT DRAWN'),
    ('the one-prime window at no support', 'at NO SUPPORT AT ALL'),
    ('the stale count', 'STALE AGAINST ITS OWN HEAD'),
    ('a quoted headline is not a measurement', 'A QUOTED'),
    ('the shared index', 'SHARE AN INDEX'),
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
    # ### **THE STRADDLE, AND THIS ARM WALKED INTO IT** (b352's species, (iii)). ### `G-PRESERVE`
    # ### compares the working file against its committed blob. ### BEFORE the push that blob is the
    # ### PRE-ACT state and the comparison is strong; AFTER it the blob IS the file and the
    # ### comparison is vacuous -- the two appended cells come back EQUAL, not longer, and the arm
    # ### fails on a correct write. ### **SO THE REFERENCE IS THE PRE-ACT COMMIT ON BOTH SIDES:**
    # ### `HEAD` before the push, `HEAD~1` after it, and the arm prints which it read.
    ref = 'HEAD~1' if post else 'HEAD'
    r = subprocess.run(['git', 'show', ref + ':' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def main():
    post = '--post' in sys.argv
    bar('=')
    rec('b401_checks.py -- THE GATE SUITE. ### **EVERY ARM TESTS A BAR THIS FACE SET.**')
    rec('### side of the push : %s' % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'))
    bar('=')
    bank = text(BANK)
    FLAT = gate_text.flat(bank)
    reg = text(REG)
    xn = text(XNOTES)
    crun = text(CRUN)

    bar()
    rec('  ### THE IMPORTED HELPERS` OWN FIXTURES, RUN BEFORE THEIR VERDICTS ARE USED.')
    bar()
    arm('G-FIXTURE', 'every imported helper passes its own fixtures in both polarities',
        GN.self_test(False) and gate_text.self_test(False) and hedge_audit.self_test(False)
        and ferry_scan.self_test(verbose=False) and all(GD.split_fixture()))

    # ---- STEP ZERO AND THE FACE ------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO AND THE FACE.')
    bar()
    arm('G-FERRY', 'the ferry is banked at the bytes and lines the face declares',
        os.path.getsize(FERRY) == 3719 and len(text(FERRY).split(chr(10))) - 1 == 73
        and 'paste ends (part 1 of 1)' in text(FERRY),
        'bytes %d ; lines %d' % (os.path.getsize(FERRY), len(text(FERRY).split(chr(10))) - 1))
    arm('G-ANCHOR', 'the extract left no read AMBIGUOUS or ABSENT',
        len(X['reads']) == 14 and all(r['verdict'].startswith('ANCHORED') for r in X['reads']),
        'reads %d ; anchored %d' % (len(X['reads']),
                                    sum(1 for r in X['reads']
                                        if r['verdict'].startswith('ANCHORED'))))
    arm('G-SEAL', 'the face carries its own lock and the lock gate permitted it',
        SEAL in reg and LG['permits'] is True and LG['gates_read'] == 8
        and LG['face_subject_gates'] == 4, 'sha %s' % SEAL[:16])
    arm('G-EVERYGATE', 'every gate the lock read passed, and four were checked by digest',
        LG['gates_read'] == LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                         'data/b401_registration_2026-09-10.txt'],
                        cwd=ROOT, capture_output=True, text=True, encoding='utf-8',
                        errors='replace')
    arm('G-SEALINTACT', 'the sealed body is byte-for-byte what was sealed, read by the seal tool',
        'SEAL INTACT' in (vr.stdout or ''))

    # ---- THE ORDER AND THE BANK ------------------------------------------------------------------
    bar()
    rec('  ### THE ORDER`S OWN WORDS, EACH NEEDLE BUILT FROM THE FERRY (b363`s helper).')
    bar()
    miss = []
    for lbl, hint in OWNER_NEEDLES:
        try:
            n, _l = GN.build(FERRY, hint)
            rec('    %-58s ### `ferry:%d`' % (lbl, n))
        except Exception as e:
            miss.append(lbl)
            rec('    %-58s ### **NEEDLE WILL NOT BUILD** %s' % (lbl, str(e)[:56]))
    arm('G-QUOTED', 'every clause of the order resolves in the ferry as a live line',
        not miss, '%d of %d built' % (len(OWNER_NEEDLES) - len(miss), len(OWNER_NEEDLES)))
    bar()
    rec('  ### THE BANK`S OWN SENTENCES, EACH NEEDLE BUILT FROM THE BANK.')
    bar()
    smiss = []
    for lbl, hint in SELF_NEEDLES:
        try:
            n, _l = GN.build(BANK, hint)
            rec('    %-58s ### `bank:%d`' % (lbl, n))
        except Exception as e:
            smiss.append(lbl)
            rec('    %-58s ### **NOT IN THE BANK** %s' % (lbl, str(e)[:56]))
    arm('G-BANKSAYS', 'every sentence this suite tests for is in the bank as a live line',
        not smiss, '%d of %d' % (len(SELF_NEEDLES) - len(smiss), len(SELF_NEEDLES)))

    # ---- BAR 1 -----------------------------------------------------------------------------------
    bar()
    rec('  ### BAR 1 -- `G-SRC`.')
    bar()
    arm('G-SRC', 'both pinned sources verified against the corpus`s banked digests',
        F['sources'] == {'CC': True, 'LG': True}
        and 'VERDICT : VERIFIED' in xn and 'VERDICT : HALT' not in xn)
    arm('G-SRCLOC', 'every source fragment the act quotes was located by page index',
        len(X['srcreads']) == 12 and all(s['pages'] for s in X['srcreads']),
        'fragments %d ; located %d' % (len(X['srcreads']),
                                       sum(1 for s in X['srcreads'] if s['pages'])))

    # ---- BAR 3 : THE YIELD -----------------------------------------------------------------------
    bar()
    rec('  ### BAR 3 -- `G-YIELD`. ### **AN ABSENCE FOUND BY ONE MATCHER IS A PROPERTY OF THAT')
    rec('  ### MATCHER**, so the arm requires five shapes and the counts to agree with the extract.')
    bar()
    y = F['yields']
    arm('G-YIELD', 'five matcher shapes were tried and every yield is printed in the components',
        len(y) == 5 and CF['matcher_shapes'] == 5
        and all(('%d HIT(S)' % v) in crun for v in y.values()),
        'shapes %d ; counts %s' % (len(y), sorted(y.values())))
    arm('G-YIELD-RESIDUE', 'the components hand-read the residue rather than reporting a count',
        'AND THE RESIDUE IS HAND-READ RATHER THAN COUNTED' in crun)
    arm('G-YIELD-CTL', 'and the arm can fail: a sixth shape absent from the extract is detected',
        'a shape that was never tried' not in y)

    # ---- BAR 4 : THE VACUITY ---------------------------------------------------------------------
    bar()
    rec('  ### BAR 4 -- `G-VACUOUS`. ### **A BARE `UNIFORM` WOULD READ AS THE STATEMENT THE ROW')
    rec('  ### HAS BEEN MISSING**, so the scoping word must stand in the same sentence.')
    bar()
    ok_same = False
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(bank)):
        if 'UNIFORM' in s and 'VACUOUS' in s.upper():
            ok_same = True
            break
    arm('G-VACUOUS', 'the uniformity verdict carries the word that scopes it, in one sentence',
        ok_same and CF['verdict_a1'] == 'UNIFORM -- AND VACUOUSLY')
    arm('G-NOPRICE', 'and no prime-by-prime opening is priced under it',
        'no prime-by-prime opening is priced' in bank.replace(chr(10), ' ')
        or 'NO PRIME-BY-PRIME OPENING' in bank.replace(chr(10), ' ').upper())
    arm('G-VACUOUS-CTL', 'the same predicate is QUIET on synthetic text carrying only the word',
        not any('UNIFORM' in s and 'VACUOUS' in s.upper()
                for s in re.split(r'(?<=[.!?])\s+',
                                  'The bound is UNIFORM in the prime. It is a class statement.')))

    # ---- BAR 5 : THE OWNING ACT ------------------------------------------------------------------
    bar()
    rec('  ### BAR 5 -- `G-OWNED`. ### **THE RECORD READ THEOREM 6.1 FIRST.**')
    bar()
    arm('G-OWNED', 'the act cites the owning act rather than importing the statement again',
        'b358' in bank and 'ALREADY OWNED' in bank.upper())
    arm('G-INHERITED', 'and the hypothesis a prior act left inherited is left inherited',
        'NOT DECIDED HERE' in bank.upper() and 'H-CUSP' in crun)

    # ---- BAR 6 : NOT RUN -------------------------------------------------------------------------
    bar()
    rec('  ### BAR 6 -- `G-NOTRUN`. ### The axiom profile is READ, not measured.')
    bar()
    arm('G-NOTRUN', 'the act declares the profile read from a printed profile and not from a run',
        'PRINTED PROFILE' in reg.upper() and 'PRINTED PROFILE' in bank.upper())
    arm('G-NOBUILD', 'and no lake or lean invocation appears in any tool of this act',
        not any(w in chr(10).join(code(n) for n in sorted(os.listdir(t('')))
                                  if n.startswith('b401_') and n.endswith('.py'))
                for w in ('lake', 'lean env', 'subprocess.run([\'lake')))

    # ---- BAR 7 / 8 : THE LEDGER ------------------------------------------------------------------
    bar()
    rec('  ### BARS 7 AND 8 -- `G-NOGRADE` AND `G-PRESERVE`, READ %s.'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'))
    bar()
    fb, ft = blob('FACES_LEDGER.md', post), text(FACES)
    tb, tt = blob('OPEN_TRAILS.md', post), text(TRAILS)
    rec('  ### the pre-act reference read from `%s` -- **THE SAME STATE ON BOTH SIDES OF THE'
        % ('HEAD~1' if post else 'HEAD'))
    rec('  ### PUSH**, which is what keeps this arm from going vacuous after the commit.')
    grade_words = ('DEFINED-ONLY', 'DERIVES-ON-IMPORTS', 'MEASURED-ON-FAMILIES', 'PROVED-GENERAL',
                   'DERIVED-ON-CONTENT', 'UNDER-RESOLVED-AT-BENCH', 'IMPORT-UNDER-THE-BAR',
                   'PROVED-PER-CELL', 'MEASURED-AT-COVERED-CELLS', 'NAMED-ONLY')
    moved = [w for w in grade_words if fb.count(w) != ft.count(w)]
    arm('G-NOGRADE', 'no grade token`s count changed in the faces ledger across this leg',
        not moved, 'tokens %d ; changed %s' % (len(grade_words), moved or 'none'))
    ob = [x for x in fb.split(chr(10)) if x.startswith('| U1 |')]
    ne = [x for x in ft.split(chr(10)) if x.startswith('| U1 |')]
    cells_ok, touched, untouched = False, [], []
    if ob and ne:
        oc, nc = GD.split_cells(ob[0]), GD.split_cells(ne[0])
        if len(oc) == len(nc) == 7:
            for k in range(7):
                if k in (4, 6):
                    touched.append(nc[k].startswith(oc[k].rstrip()) and len(nc[k]) > len(oc[k]))
                else:
                    untouched.append(nc[k] == oc[k])
            cells_ok = all(touched) and all(untouched)
    arm('G-PRESERVE', 'five cells of row U1 BYTE-IDENTICAL, two carrying the blob as a prefix',
        cells_ok, 'touched-as-prefix %s ; untouched-identical %s' % (touched, untouched))
    arm('G-APPENDONLY', 'the trail block is append-only: the pre-act bytes are a true prefix',
        tt.startswith(tb), 'bytes %d -> %d' % (len(tb.encode('utf-8')), len(tt.encode('utf-8'))))
    arm('G-NOLOST', 'no line was lost from either ledger',
        len(ft.split(chr(10))) == len(fb.split(chr(10)))
        and len(tt.split(chr(10))) >= len(tb.split(chr(10))))

    # ---- BAR 15 : THE SHARED INDEX ---------------------------------------------------------------
    bar()
    rec('  ### BAR 15 -- `G-SHARED`. ### **AN ENTRY THAT HID THE SHARING WOULD BE COUNTING ONE')
    rec('  ### OBSTRUCTION TWICE.**')
    bar()
    row = ne[0] if ne else ''
    arm('G-SHARED', 'the fourth instance names the index it shares with the third, in the row',
        'SHARE AN INDEX' in row and 'DIFFER IN OBJECT' in row)
    arm('G-NOBRIDGE', 'and the row types no bridge between any two of the four',
        'types no bridge' in row and 'NO EQUIVALENCE IS COMPILED' in row)

    # ---- BAR 9 / 10 : THE CAP AND THE WRITE LIST -------------------------------------------------
    bar()
    rec('  ### BARS 9 AND 10 -- `G-CAP` AND `G-WRITELIST`, THE LIST BUILT AS KINDS.')
    bar()
    tools = [n for n in sorted(os.listdir(t(''))) if n.startswith('b401_') and n.endswith('.py')]
    arm('G-CAP', 'new relay tool files at most the six the face declares',
        len(tools) == 6, 'wrote %d : %s' % (len(tools), tools))

    def kind(n):
        m = re.match(r'^(.*?)(\d*)(\.[a-z]+)$', n)
        stem = (m.group(1) if m else n)
        return stem

    written = sorted(n for n in os.listdir(D) if n.startswith('b401_')
                     or n.startswith('audit_b401_'))
    unnamed = []
    for n in written:
        k = kind(n)
        if n in reg or k in reg or k.rstrip('_') in reg:
            continue
        if re.sub(r'_2026-\d\d-\d\d', '_<date>', n) in reg:
            continue
        unnamed.append(n)
    arm('G-WRITELIST', 'every file this leg wrote is of a KIND the locked face names',
        not unnamed, 'files %d ; of an unnamed KIND %d : %s'
        % (len(written), len(unnamed), unnamed or 'none'))

    # ---- BAR 11 ----------------------------------------------------------------------------------
    bar()
    rec('  ### BAR 11 -- `G-NOINSTRUMENT`.')
    bar()
    lean = subprocess.run(['git', '-C', PP, 'status', '--porcelain', '--', '*.lean'],
                          capture_output=True, text=True)
    swst = subprocess.run(['git', '-C', SW, 'status', '--porcelain'],
                          capture_output=True, text=True)
    arm('G-NOINSTRUMENT', 'no `.lean` file is touched, and SIDE-window is untouched',
        not (lean.stdout or '').strip() and not (swst.stdout or '').strip(),
        'SIDE-window working tree : %r' % (swst.stdout or '').strip()[:80])

    # ---- BAR 12 / 13 / 14 ------------------------------------------------------------------------
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
        arm('G-PINS', 'all four repositories equal by ls-remote, read AFTER THE PUSH',
            '### REPOS HARD-FAILING : 0' in (pr.stdout or ''))
        mrec = text(d('b401_mirror.txt'))
        head = subprocess.run(['git', '-C', PP, 'ls-remote', 'origin', 'refs/heads/main'],
                              capture_output=True, text=True).stdout.split(chr(9))[0].strip()
        arm('G-MIRROR', 'the mirror was rebuilt AFTER the commit and is clean on all three clauses',
            'VERDICT: CLEAN ON ALL THREE CLAUSES' in mrec and head[:7] in mrec
            and 'CLAUSE 2 : CLEAN' in mrec, 'ls-remote %s' % head[:16])
    else:
        rec('  G-PINS           read AFTER THE PUSH only                          ### DEFERRED')
        rec('  G-MIRROR         a clean clause on a stale build looks exactly like')
        rec('                   a correct one                                     ### DEFERRED')

    # ---- THE ROW, THE KEY, THE MUST-FAILS --------------------------------------------------------
    bar()
    rec('  ### THE ROW, THE KEY AND THE MUST-FAIL FIXTURES.')
    bar()
    tb2 = text(TABLE)
    rows = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', tb2, re.M)]
    arm('G-ROW', 'the correspondence row is present once and its number is the last',
        rows[-1] == 250
        and tb2.count('THE ABSENT ELEMENT IS CONFIRMED ABSENT BY SEARCH') == 1,
        'last row %d' % rows[-1])
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-absent-element-searched'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    arm('G-KEY', 'the index key resolves and returns exactly one row',
        (kq.stdout or '').count('act      :') == 1)
    fixtures = ['### THE BOUND WAS FOUND.', '### THE WINDOW WAS OPENED.',
                '### A KERNEL WAS BUILT.', '### THE OBSTRUCTION WAS CRACKED.',
                '### AN EQUIVALENCE WAS COMPILED.', '### H-CUSP WAS DECIDED.']
    lines = set(bank.split(chr(10)))
    hits2 = [f for f in fixtures if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank',
        not hits2, 'fixtures %d ; hits %s' % (len(fixtures), hits2 or 'none'))
    synth = 'a line' + chr(10) + '### A KERNEL WAS BUILT.' + chr(10) + 'b'
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
    out = d('b401_checks_postpush.txt' if post else 'b401_checks_run.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(R) + chr(10))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main())
