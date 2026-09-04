# -*- coding: utf-8 -*-
"""b324_index_append.py -- ONE KEY, TWO ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTMOVED`.** ### A reader who asks
### *did the arc move the wall* must be handed ### **NO** ### -- and the reason, which is that the
### two spaces are different objects at seven of seven constituents. ### A row that answered that
### question with the arc's three certified theorems and stopped would be a true sentence assembled
### to give a false impression.

### ### **AND THE SECOND ARM IS `G-NOTOVERSIGHT`.** ### A reader who asks about the missing bridge
### must be handed that the deposit withholds the cross-register equivalences ### **DELIBERATELY**,
### and why: compiling them would be compiling RH-equivalence itself.

### ### **`the archimedean membership` STAYS UNKEYED.** ### b321, b322 and b323 all left it so, and
### this act decides nothing about it either.
### ### **THE INDEX IS SWEPT FOR STEMS AFTER THE WRITE** (b305's defect, caught at b306).
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NL = chr(10)

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'keystones-reread': ['the keystones reread', 'the wall', 'the margin',\n"
    "                        'did the arc move the wall', 'the two margins',\n"
    "                        'is the arc space the wall space', 'the bridging statement',\n"
    "                        'what did the deposit already say'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE WALL (b324).\n"
    "    (\"keystones-reread\", \"b324 (reads and definitional decisions; the wall)\",\n"
    "     \"the residue keystone's object and the arc's constructed space, decided constituent by\"\n"
    "     \" constituent. ### The keystone's is **the positive space on the zeros** -- *positivity\"\n"
    "     \" has no zeros, the operator has no space, and the space is exactly what neither\"\n"
    "     \" supplies. The space is the wall* -- defined by the requirement that a self-adjoint\"\n"
    "     \" operator's spectrum REALIZE the zeta-zeros. ### The arc's is Connes-Consani's S(1,1):\"\n"
    "     \" two homogeneous vanishing conditions on a function and its transform, **with no\"\n"
    "     \" operator and no zeros in the definition at all**. ### **VERDICT: DIFFERENT, SEVEN OF\"\n"
    "     \" SEVEN**, differing at the FIRST constituent walked. ### **SO NO: THE ARC DID NOT MOVE\"\n"
    "     \" THE WALL**, and the second half of the registered expectation does not arise -- an act\"\n"
    "     \" that did not build the keystone's object cannot have moved the wall that object IS\",\n"
    "     \"### A DIFFERENT VERDICT ON TWO OBJECTS IS NOT A CONFLICT BETWEEN TWO RECORDS. ###\"\n"
    "     \" **THE VERDICT RESTS ON NO SHARED WORD**: the order refused resemblance BY NAME and the\"\n"
    "     \" registration gave the test -- if the argument would survive replacing one side's term\"\n"
    "     \" with a synonym the other does not use, it was resemblance. ### **THE KEYSTONE HAD\"\n"
    "     \" ALREADY PLACED THE ARC'S SOURCE**: its realization-candidate map grades\"\n"
    "     \" *Connes-Consani (reduces RH to a Weil positivity left open)* among routes that STALL\"\n"
    "     \" AT THE REALIZATION CLAUSE. ### **AND A MEASURED PROVENANCE FINDING RIDES WITH IT:**\"\n"
    "     \" *the space is the wall*, *the positive space* and **Sonin** -- the name of the arc's\"\n"
    "     \" entire space -- EACH APPEAR ZERO TIMES IN THE DEPOSITED MONOGRAPH. ### The deposit is\"\n"
    "     \" ms v5.10.2; the wall's naming is v5.13 and INTERNAL. ### NO GRADE MOVED. ### NO ACT\"\n"
    "     \" RE-VERDICTED. ### M-2 UNCHANGED\",\n"
    "     \"data/b324_the_keystones_reread.txt; data/b324_reread_run.txt;\"\n"
    "     \" PLACE-papers/phase1.5/proofs/THE_RESIDUE_OF_RH.md (the emitting keystone);\"\n"
    "     \" CORRESPONDENCE.md row 160\"),\n"
    "    # ### THE MARGIN (b324).\n"
    "    (\"keystones-reread\", \"b324 (reads and definitional decisions; the margin)\",\n"
    "     \"the balance keystone's margin against the arc's. ### The keystone's is M(n) :=\"\n"
    "     \" lambda_Z(n) + lambda_A(n) = lambda_n, positive throughout 1 <= n <= 300, minimum at\"\n"
    "     \" n = 1 (lambda_1 = 0.0230957089661), growing like (n/2) ln n. ### The arc's is\"\n"
    "     \" W_8(f) - Tr(theta(g) S theta(g)*), equal by Theorem 4.7 to minus a remainder integral:\"\n"
    "     \" +0.271444634, +0.285510313, +0.309777648, growing toward the boundary. ### **THEY\"\n"
    "     \" DIFFER AT SIX OF SEVEN CONSTITUENTS** -- different index, different decomposition, and\"\n"
    "     \" **only the keystone's margin contains the zeros**. ### The seventh keeps it alive: the\"\n"
    "     \" monograph names positivity of the Weil functional and lambda_n >= 0 as classical faces\"\n"
    "     \" of ONE obligation h2. ### **VERDICT: UNDECIDED**\",\n"
    "     \"### EQUIVALENCE OF THE OBLIGATIONS IS NOT EQUIVALENCE OF THE MARGINS. ### **AND THE\"\n"
    "     \" BRIDGE IS ABSENT BY DESIGN, NOT BY OVERSIGHT**: the deposit records that the register\"\n"
    "     \" pentagon compiles the five faces' structure *while **deliberately not** compiling the\"\n"
    "     \" cross-register equivalences, since to compile 'discharge one and you discharge all\"\n"
    "     \" five' would be to compile RH-equivalence itself*. ### **THE BRIDGING STATEMENT IS\"\n"
    "     \" TYPED AND FILED AS THE ARC'S MOST VALUABLE OPEN ITEM**: a formula carrying the\"\n"
    "     \" archimedean margin at a lawful test function to the Li margin at an index n, or a\"\n"
    "     \" proof that no such formula exists. ### **ITS HONEST PRICE RIDES WITH IT**: the\"\n"
    "     \" keystone's margin is positive AT THE BENCH to n = 300, lambda_Z measured NEGATIVE\"\n"
    "     \" across n = 156..186 and 247..287, and Voros's threshold puts discrimination beyond\"\n"
    "     \" n ~ 10^18. ### The seven contacts came out 3 CORROBORATED, 4 UNTOUCHED, 0 IN TENSION.\"\n"
    "     \" ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b324_the_keystones_reread.txt; data/b324_filings_run.txt;\"\n"
    "     \" PLACE-papers/phase1.5/spectral/BALANCE_AND_POSITIVITY.md (the emitting keystone);\"\n"
    "     \" CORRESPONDENCE.md row 161\"),\n"
)

NEW_KEYS = ('keystones-reread',)
ALIASES = ('the keystones reread', 'the wall', 'the margin', 'did the arc move the wall',
           'the two margins', 'is the arc space the wall space', 'the bridging statement',
           'what did the deposit already say')
MUST_NOT_HIT = ('the archimedean membership', 'the window class')
def no_key(out):
    for ln in (out or '').splitlines():
        if ln.strip().startswith('### NO KEY'):
            return True
    return False


def verdict_fixture():
    real = no_key('=====' + NL + '  ### NO KEY.' + NL + '  ### matched no DECLARED key')
    quoted = no_key('    grade    : ... every query that would have found b268 returned NO KEY.')
    return real, quoted


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b324 -- THE INDEX KEY. ### THE WALL, AND THE MARGIN.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-24s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
    written = not (all(have_key.values()) and all(have_row.values()))
    if not written:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2

    if written:
        new = txt
        if not all(have_key.values()):
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not all(have_row.values()):
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)

    rv, qv = verdict_fixture()
    print('  VERDICT FIXTURE : fires on the index\'s own NO KEY line : %s ;'
          ' quiet on the phrase quoted inside a row : %s' % (rv, not qv))
    ok = rv and not qv

    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    for k in NEW_KEYS:
        out, rc = query(k)
        good = (not no_key(out)) and (k in out) and rc == 0
        both = out.count('act      :') >= 2
        ok = ok and good and both
        print('    %-24s returns a row : %s ; returns BOTH rows : %s  %s'
              % (k, good, both, 'PASS' if (good and both) else '### FAIL ###'))
    print('  ### **BOTH ROWS ARE REQUIRED.** ### An index that handed back the filing without the')
    print('  ### defective-bars table would be answering *what was filed* and hiding *what the')
    print('  ### filing had to admit*.')

    print('  ### THE ALIASES:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-42s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### ### **G-NOTMOVED -- THE ARM THIS FILE EXISTS FOR.**')
    out, _rc = query('did the arc move the wall')
    no = 'THE ARC DID NOT MOVE' in out
    why = 'DIFFERENT, SEVEN OF' in out
    ok = ok and no and why
    print('    the answer says the arc did NOT move the wall : %s' % no)
    print('    ### and gives the reason -- seven of seven      : %s' % why)
    print("  ### **A ROW THAT ANSWERED *did the arc move the wall* WITH THE ARC'S THREE CERTIFIED")
    print('  ### ### THEOREMS AND STOPPED WOULD BE A TRUE SENTENCE ASSEMBLED TO GIVE A FALSE')
    print('  ### ### IMPRESSION.**')
    print('  ### ### **G-NOTOVERSIGHT -- THE SECOND ARM.**')
    out2, _rc2 = query('the bridging statement')
    delib = 'BY DESIGN, NOT BY OVERSIGHT' in out2
    ok = ok and delib
    print('    the answer says the bridge is withheld BY DESIGN : %s' % delib)
    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the archimedean membership` STAYS UNKEYED: A FOLD THAT CLAIMED IT WOULD BE')
    print('  ### ### FILING A VERDICT NOBODY REACHED.**')

    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    for h in sh:
        print('      line %d  %s' % (h[1], h[3][:96]))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
