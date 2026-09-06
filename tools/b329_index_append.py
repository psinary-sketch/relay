# -*- coding: utf-8 -*-
"""b329_index_append.py -- ONE KEY, TWO ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTAVERAGED`.** ### A reader who asks *is the finite side's
### silence compiled* must be handed the answer WITH its two scope words -- GENERAL for the decomposition
### and the scaling part, PER CELL for the compact part -- and never a sentence that averages them.
### ### **`a general compact-part silence` AND `the archimedean silence` STAY UNKEYED.** ### The index is
### swept for stems after the write.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')
D = os.path.join(ROOT, 'data')
import b329_correspondence as R  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

K = R.read_kernel()

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'finite-side-seal': ['finite-side seal', 'the finite-side seal', 'finite side seal', 'the finite-side sealing module',\n"
    "                         'FiniteSideSeal', 'the exhaustiveness theorem', 'the unit decomposition', 'the scaling shift inverse',\n"
    "                         'general and per-cell', 'the axiom finding', 'the compact part per cell', 'the scaling part general'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE FINITE-SIDE SEAL -- THE MODULE AND ITS TWO SCOPES (b329).\n"
    "    (\"finite-side-seal\", \"b329 (a kernel build of banked derivations)\",\n"
    "     \"Core/FiniteSideSeal.lean (B329), vanilla Lean, no imports, no native_decide, no sorry: GENERAL over every\"\n"
    "     \" base p >= 2, level, power and index -- the decomposition of a nonzero index as a non-multiple of p times a\"\n"
    "     \" power of p with the exponent below the level (existence, uniqueness), the action factoring through the two\"\n"
    "     \" parts, p^j - 1 invertible modulo every p^m with the inverse exhibited, the fixed-point congruence forcing\"\n"
    "     \" the index into the ball in either congruence (b309's law, compiled). PER CELL, decided over the seven banked\"\n"
    "     \" cells and no other -- the compressed smear over the units vanishes (b304's zero in b310's signed-count\"\n"
    "     \" form), the not-dead witness, b304's refusal, the polarity controls. ONE exhaustiveness theorem whose\"\n"
    "     \" hypotheses name which is which. ### The profile " + str(K['before']) + " -> " + str(K['after']) + " prints, all zero-axiom, the banked\"\n"
    "     \" profile a true byte prefix\",\n"
    "     \"### GENERAL FOR THE SCALING PART, PER CELL FOR THE COMPACT PART -- STATED IN THE MODULE HEADER AND NEVER\"\n"
    "     \" AVERAGED. ### Faces ledger F5: PROVED-GENERAL (scaling) / PROVED-AT-CELLS (compact). ### What is compiled\"\n"
    "     \" is the model's arithmetic and the counting form of the trace; the identification with the source's trace\"\n"
    "     \" is b310's derivation, uncompiled. ### NOTHING ABOUT THE ARCHIMEDEAN PLACE. ### NO GRADE MOVED. ### M-2\"\n"
    "     \" UNCHANGED\",\n"
    "     \"D:/SIDE-global-section/Core/FiniteSideSeal.lean; AXIOM_PRINTS.txt (B329.*); data/b329_kernel_run.txt;\"\n"
    "     \" data/b329_the_finite_side_seal.txt; data/b329_registration_2026-09-05.txt (sealed before any build);\"\n"
    "     \" CORRESPONDENCE.md rows 170-174; FACES_LEDGER.md (the b329 update)\"),\n"
    "    # ### THE FINITE-SIDE SEAL -- THE AXIOM FINDING AND THE THREE BARS NOT MET IN THEIR REGISTERED FORM (b329).\n"
    "    (\"finite-side-seal\", \"b329 (a measurement on the toolchain; three declared deviations)\",\n"
    "     \"the core library's lemmas about divisibility, modulus and Nat.Coprime -- and Nat.mul_assoc -- carry\"\n"
    "     \" propext (and often Quot.sound), as do omega, simp, ac_rfl and by_cases on divisibility; the audit bar is\"\n"
    "     \" zero axioms, so the general theorems are stated as equations with witnesses (NotDiv p u := forall c,\"\n"
    "     \" u != p * c; the congruence p^j t = t + p^m c; the ball t = p^m d) and proved from the axiom-free part of\"\n"
    "     \" core plus helpers proved by induction. ### THREE REGISTERED BARS NOT MET IN THEIR REGISTERED FORM, SAID:\"\n"
    "     \" (T1.4) the coprimality form of 'unit' (primality used nowhere in the module); (T1.6) the factorization\"\n"
    "     \" before reduction; (T2.1) the explicit inverse rather than Nat.Coprime\",\n"
    "     \"### NOTHING SORRIED, NOTHING WEAKENED SILENTLY; the first draft's general proofs printed [propext,\"\n"
    "     \" Quot.sound] and were rewritten BEFORE any profile was written. ### The per-cell arm was not promoted to\"\n"
    "     \" cover for a general bar. ### NO GRADE MOVED\",\n"
    "     \"data/b329_axiom_probe.txt; data/b329_axiom_probe.lean; tools/b329_axiom_probe.py;\"\n"
    "     \" data/b329_the_finite_side_seal.txt (the deviations); CORRESPONDENCE.md row 174\"),\n"
)

ALIASES = ('the finite-side seal', 'the finite-side sealing module', 'FiniteSideSeal', 'the exhaustiveness theorem',
           'the unit decomposition', 'general and per-cell', 'the axiom finding', 'the scaling part general')
MUST_NOT_HIT = ('a general compact-part silence', 'the archimedean silence')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b329 -- THE INDEX KEY. ### THE FINITE-SIDE SEAL.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'finite-side-seal'" in txt)
    have_row = ('"finite-side-seal"' in txt)
    print('  finite-side-seal    key/row already present : %s / %s' % (have_key, have_row))
    written = not (have_key and have_row)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2
    if written:
        new = txt
        if not have_key:
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not have_row:
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
    else:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    ok = True
    out, rc = query('finite-side-seal')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 2
    ok = ok and good
    print('  READ BACK : finite-side-seal returns %d row(s), 2 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'finite-side-seal' in o
        ok = ok and g
        print('    %-40s reaches the b329 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTAVERAGED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'GENERAL FOR THE SCALING PART, PER CELL FOR THE COMPACT PART' in out
    a2 = 'NEVER' in out and 'AVERAGED' in out
    a3 = 'THREE REGISTERED BARS NOT MET IN THEIR REGISTERED FORM' in out
    ok = ok and a1 and a2 and a3
    print('    the answer carries both scope words, each for its part     : %s' % a1)
    print('    ### and says they are never averaged                       : %s' % a2)
    print('    ### and carries the three declared deviations              : %s' % a3)
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        quiet = no_key(o)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s' % (q, quiet, pre[q], 'PASS' if good else '### FAIL ###'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
