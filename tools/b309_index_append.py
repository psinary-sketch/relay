# -*- coding: utf-8 -*-
"""b309_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER SAYS `scaling-trace keyed` AND EVERY RESULT KEYED.** ### This act has two: the
### value, and the mechanism that explains it.

### ### **THE MUST-NOT-HIT ARM IS b202's, MEASURED BEFORE AND AFTER: ### `zero` AND `the trace`
### ### STAY UNKEYED BECAUSE THEY ARE A VALUE AND A GENERIC OBJECT, NOT THIS RECORD'S OBJECTS.**
### An index answering `zero` would be answering a question about a number rather than about a
### result, and `the trace` would collide with every trace the corpus has ever taken.
### ### **AND THE INDEX IS SWEPT FOR STEMS AFTER THE WRITE** (b305's defect, caught at b306).
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
    "    'scaling-trace': ['the scaling trace', 'the compressed trace', 'the smeared trace',\n"
    "                     'the trace of the scaling action'],\n"
    "    'no-offball-fixed-point': ['the fixed point', 'the mechanism', 'the unit argument',\n"
    "                              'p^j minus one'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE SCALING TRACE, COMPUTED (b309).\n"
    "    (\"scaling-trace\", \"b309 (a computation on the b308 instrument)\",\n"
    "     \"Tr(theta(p^k) Pi) for k != 0 -- the compression of the SCALING part of Q_p^x against the\"\n"
    "     \" projection onto the object's own space. ### b304 computed the compact part and REFUSED\"\n"
    "     \" this one because the model folds it; b308 built the frame where it does not fold and\"\n"
    "     \" NAMED this computation without performing it. ### **THE FIRST THING ESTABLISHED IS THAT\"\n"
    "     \" THE TRACE IS NOT DEFINED UNTIL AN AMBIENT IS NAMED**: theta(p^k) carries V(n,n) to\"\n"
    "     \" V(n-k, n+k), so the composed map is no frame's endomorphism, and the smallest frame\"\n"
    "     \" containing both is V(max(n,n-k), max(n,n+k)). ### **THE VALUE: EXACTLY ZERO AT EVERY\"\n"
    "     \" NONZERO POWER IN [-2n, 2n] AT ALL SEVEN BANKED CELLS**, by two independent routes -- 34\"\n"
    "     \" cell/power pairs by both, 10 by the reduced route only where the ambient exceeds 1024\"\n"
    "     \" chart points and the bound is PRINTED. ### 0 disagreeing\",\n"
    "     \"### A COMPUTATION, AND ITS VALUE IS ZERO. ### **NOT AN OBSTRUCTION THEOREM, AND NEITHER\"\n"
    "     \" A ROUTE NOR AN ANTI-ROUTE** -- the order forbids reading a nonzero as a route and this\"\n"
    "     \" act adds that the converse reading is forbidden too. ### **SCOPE: one trace of one map\"\n"
    "     \" against one projection, at the cells and powers listed, in the smallest ambient\"\n"
    "     \" containing source and target -- a different ambient is a different number.** ### It says\"\n"
    "     \" nothing about any other functional on the instrument and nothing about the source's own\"\n"
    "     \" functional, which smears against a test function over the whole group: a vanishing of\"\n"
    "     \" every individual term is a statement about terms. ### **b273's A at k = n IS A DIFFERENT\"\n"
    "     \" OPERATOR; the barrier and the compression are neither extended nor weakened.** ###\"\n"
    "     \" NOTHING ABOUT THE ARCHIMEDEAN PLACE (b285's boundary stands). ### NO AGGREGATION IS\"\n"
    "     \" STATED. ### M-2 UNCHANGED\",\n"
    "     \"data/b309_the_scaling_trace.txt; data/b309_components_run.txt;\"\n"
    "     \" tools/b309_scaling_trace.py; tools/b309_components.py; CORRESPONDENCE.md row 130\"),\n"
    "    # ### THE MECHANISM (b309).\n"
    "    (\"no-offball-fixed-point\", \"b309 (a derivation, with three arithmetic terminals)\",\n"
    "     \"WHY the scaling trace vanishes, in TWO REGIMES WITH TWO MECHANISMS. ### ABOVE THE LEVEL\"\n"
    "     \" (abs(k) >= n) the object's support and its image's are DISJOINT -- the object vanishes\"\n"
    "     \" on the ball, so its support sits at absolute values p^1..p^n and the image's at\"\n"
    "     \" p^(1+k)..p^(n+k) -- and **the COMPRESSION is the ZERO OPERATOR**, measured. ### BELOW IT\"\n"
    "     \" (1 <= abs(k) <= n-1) **THE SUPPORTS GENUINELY MEET AND THE TRACE IS STILL ZERO**: against\"\n"
    "     \" the projector's closed form the trace is a sum over t off the ball of two congruence\"\n"
    "     \" indicators in (p^j - 1) t, and **p^j - 1 IS A UNIT**, so each congruence forces t = 0\"\n"
    "     \" modulo the grid and modulo the ball's modulus -- and both of those sets are EXACTLY THE\"\n"
    "     \" BALL, which the sum excludes. ### **THE SCALING MAP FIXES NOTHING OFF THE BALL, AND THE\"\n"
    "     \" ONLY THING IT FIXES IS THE ONE PLACE THE OBJECT MUST VANISH**\",\n"
    "     \"### A DERIVATION, GENERAL IN p, n AND k, WITH A FINITE SWEEP AS ITS CHECK -- **AND THE\"\n"
    "     \" ACT SAYS WHICH IS WHICH: A SWEEP OVER SEVEN CELLS IS NOT A PROOF OVER ALL OF THEM.**\"\n"
    "     \" ### THREE TERMINALS, ALL ZERO AXIOMS, Core/ScalingTraceShadow.lean (vanilla Lean, no\"\n"
    "     \" imports, no native_decide, no sorry): B309.frame_arithmetic,\"\n"
    "     \" B309.support_ranges_split_at_the_level (BOTH arms -- the meeting arm keeps the disjoint\"\n"
    "     \" arm from reading as vacuous), B309.no_offball_fixed_point_of_scaling. ### **EACH RANGES\"\n"
    "     \" OVER AN EXPLICIT LIST NAMED IN ITS OWN STATEMENT, SO NONE CAN BE READ AS A LAW ABOUT ALL\"\n"
    "     \" p, n, k. ### AND WHAT THEY CERTIFY IS ARITHMETIC AND NOT THE BARRIER: the step from the\"\n"
    "     \" counts to the vanishing of the trace is the bank's derivation and IS UNCOMPILED.** ###\"\n"
    "     \" Profile 470 -> 473, all zero-axiom, the banked profile a TRUE BYTE PREFIX of the new\"\n"
    "     \" one. ### M-2 UNCHANGED\",\n"
    "     \"data/b309_the_scaling_trace.txt; data/b309_kernel_run.txt;\"\n"
    "     \" SIDE-global-section/Core/ScalingTraceShadow.lean; CORRESPONDENCE.md row 131\"),\n"
)

NEW_KEYS = ('scaling-trace', 'no-offball-fixed-point')
ALIASES = ('the scaling trace', 'the compressed trace', 'the smeared trace',
           'the fixed point', 'the mechanism', 'the unit argument')
MUST_NOT_HIT = ('zero', 'the trace')


def no_key(out):
    """### TRUE IFF THE INDEX'S OWN VERDICT LINE SAYS `NO KEY`. ### **LINE-SCOPED** -- b302's D7."""
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
    print('b309 -- THE INDEX KEYS. ### THE TRACE, AND THE MECHANISM.')
    print('=' * 100)

    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-22s NO KEY before : %s' % (q, pre[q]))

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-26s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
        ok = ok and good
        print('    %-26s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-28s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-22s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`zero` AND `the trace` STAY UNKEYED: one is a VALUE and the other is a GENERIC')
    print('  ### OBJECT this record takes many of** -- b202\'s reason, and b164\'s limit is not')
    print('  ### retired: KEYS CLOSE FALSE HITS, NOT FALSE MISSES.')

    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE (b305\'s defect, not repeated) : %d stem hit(s)'
          % len(sh))
    for h in sh:
        print('      line %d  %s' % (h[1], h[3][:96]))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
