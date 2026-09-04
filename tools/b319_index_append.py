# -*- coding: utf-8 -*-
"""b319_index_append.py -- ONE KEY. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE: ### *stable-rank keyed*.** ### Two rows carry it -- the subspace, and
### the repair with the bar that could not be met -- because a reader asking whether the rank holds
### still must be handed the reach that is STILL EMPTY alongside the rank that stopped moving.

### ### **THE MUST-NOT-HIT ARM IS b202's, AND BOTH ARE THINGS THIS ACT DID NOT DO.** ###
### `the archimedean weil distribution` stays unkeyed -- neither side of the source's inequality was
### computed. ### `the nonempty reach` stays unkeyed -- ### **THE ORDER ASKED FOR ONE AND THIS ACT
### ### DID NOT DELIVER IT**, and an index that answered it would be handing back a rank where a
### reach was asked for.
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
    "    'stable-rank': ['the stable rank', 'why did the rank step',\n"
    "                   'the eigenvalue one subspace', 'the rank stable subspace',\n"
    "                   'does the dimension hold still', 'the kernel coverage repair'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE SUBSPACE (b319).\n"
    "    (\"stable-rank\", \"b319 (an instrument build, act two of the archimedean instrument)\",\n"
    "     \"the archimedean instrument's subspace by the source's own eigenvalue-one\"\n"
    "     \" characterization. ### The paper's (81) reads P P-hat P = SUM lambda(n)^2\"\n"
    "     \" |zeta_n><zeta_n| + R with R the orthogonal projection on Sonin's space, and its page 28\"\n"
    "     \" says S(1,1) IS the eigenvalue-one eigenspace -- so the spectrum is {lambda(n)^2}\"\n"
    "     \" together with 1 and an eigenvalue is DIMENSIONLESS. ### On the free coordinates the\"\n"
    "     \" sandwich is M = I - (hy/h) C^T C. ### **ON THE GRID AXIS THE SELECTED DIMENSION IS 69,\"\n"
    "     \" 69, 69, 69 ACROSS N = 2048 TO 16384, WHERE b316's SCHEME GAVE 80, 80, 79, 79** --\"\n"
    "     \" rank changes: b316 one, this act zero. ### **AND THE DRIFT FELL WITH IT**: 8.6e-05 to\"\n"
    "     \" 4.5e-04 where b318 measured 6.1e-03 to 2.3e-02. ### The threshold TAU = 1e-6 was fixed\"\n"
    "     \" from the source and the corpus's banked lambda(0)^2 BEFORE any spectrum was seen, and\"\n"
    "     \" then landed in a measured void: largest admitted ~2.0e-07, smallest excluded 5.62e-06\",\n"
    "     \"### A RANK THAT HOLDS STILL IS NOT CONVERGENCE. ### **THE GRID HALF OF THE REACH IS\"\n"
    "     \" ATTAINED AND THE DOMAIN HALF IS NOT** -- the noise-floor gate REFUSES all six domain\"\n"
    "     \" pairs, and the domain rank must grow because the space does (20, 37, 69, 133, 262).\"\n"
    "     \" ### **THE SUBSPACE CHANGED**: the stable cut STRICTLY CONTAINS b316's (only-grid 9 to\"\n"
    "     \" 12 at every frame, only-stable 0), so the smear is negative at 3 cells where b318 found\"\n"
    "     \" 5. ### Structural findings survive: square never negative, the identity re-proved at\"\n"
    "     \" 3.3e-06 to 2.6e-05, zeta_n residual 1.0000 on both cuts at all eight frames. ### **THE\"\n"
    "     \" UNIT'S RESIDUAL IS A MEASUREMENT WITH NO VERDICT**: 0.4395 constant on the grid axis\"\n"
    "     \" where the grid cut drifts -- it holds still, and it is still nowhere near zero. ### NO\"\n"
    "     \" ACT RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b319_the_stable_rank.txt; data/b319_components_run.txt;\"\n"
    "     \" tools/b319_stable.py (the emitting file); CORRESPONDENCE.md row 150\"),\n"
    "    # ### THE REPAIR, AND THE BAR THAT COULD NOT BE MET (b319).\n"
    "    (\"stable-rank\", \"b319 (the kernel-coverage repair, and the reach bar's own defect)\",\n"
    "     \"the kernel-coverage defect discharged sixteen acts after b315 filed it. ### The profile\"\n"
    "     \" was regenerated from source and compared **TO THE GIT BLOB, NOT THE WORKING FILE** --\"\n"
    "     \" 33195 bytes each, byte-for-byte identical; the working file is 475 bytes longer, one\"\n"
    "     \" per line, which is core.autocrlf and not the kernel. ### Ten Core modules had no\"\n"
    "     \" compiled artefact; all ten compiled, 0 build errors. ### 24 imports and 91 print lines\"\n"
    "     \" appended. ### **PRINTS 475 TO 566, AND THE OLD PROFILE IS A LITERAL BYTE PREFIX OF THE\"\n"
    "     \" NEW ONE.** ### **AXIOM-BEARING TERMINALS AMONG THE 91 NEWLY CERTIFIED: 0**, read off\"\n"
    "     \" the printed file. ### The gate now PASSES and its fixtures still show it can fail\",\n"
    "     \"### A DEFECT DISCHARGED IS NOT A RESULT: every one of the 91 was already compiling and\"\n"
    "     \" nothing was proved by printing it. ### **AND THE REACH IS STILL EMPTY, 0 OF 6, BECAUSE\"\n"
    "     \" THE BAR THIS ACT SEALED IS DEFECTIVE** -- (B3) requires the rank constant across BOTH\"\n"
    "     \" axes, which on the domain axis is unsatisfiable by the nature of the object. ### The\"\n"
    "     \" second scheme was tried as ordered: **on the grid axis pinning selects the IDENTICAL\"\n"
    "     \" index set**, and **on the domain axis it admits a direction at eigenvalue-distance\"\n"
    "     \" 1.000e+00 from one** -- refuted, not deferred. ### W-ORD-REACH-BAR filed. ### The\"\n"
    "     \" registration was sealed with a banned stem in it and then RE-SEALED, superseded hash in\"\n"
    "     \" the block. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b319_the_stable_rank.txt; data/b319_coverage_repair.txt; data/b319_pin.txt;\"\n"
    "     \" CORRESPONDENCE.md row 151\"),\n"
)

NEW_KEYS = ('stable-rank',)
ALIASES = ('the stable rank', 'why did the rank step', 'the eigenvalue one subspace',
           'the rank stable subspace', 'does the dimension hold still',
           'the kernel coverage repair')
MUST_NOT_HIT = ('the archimedean weil distribution', 'the nonempty reach')


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
    print('b319 -- THE INDEX KEY. ### THE SUBSPACE, AND THE REPAIR.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))

    print('  ### AND THE ALIAS b318 LEFT UNKEYED, MEASURED BEFORE THIS ACT CLAIMS IT:')
    out, _rc = query('the rank stable subspace')
    print('    %-36s NO KEY before : %s' % ('the rank stable subspace', no_key(out)))
    print('    ### **b318 LEFT IT UNKEYED BECAUSE ITS SCHEME WAS SPECIFIED AND NOT BUILT.**')
    print('    ### **THIS ACT BUILT IT AND THEREFORE CLAIMS IT.**')

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
        print('    %-24s returns a row : %s ; returns BOTH halves : %s  %s'
              % (k, good, both, 'PASS' if (good and both) else '### FAIL ###'))
    print('  ### **BOTH HALVES ARE REQUIRED.** ### An index that handed back the rank that stopped')
    print('  ### moving without the reach that is still empty would be answering *what was built*')
    print('  ### and hiding *what it did not buy*, which is the exact shape this record refuses.')

    print('  ### THE ALIASES:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-42s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the nonempty reach` STAYS UNKEYED BECAUSE THE ORDER ASKED FOR ONE AND THIS ACT')
    print('  ### ### DID NOT DELIVER IT.** ### An index that answered it would hand back a rank')
    print('  ### where a reach was asked for.')

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
