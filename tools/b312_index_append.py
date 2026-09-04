# -*- coding: utf-8 -*-
"""b312_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE -- `the-remainder` -- AND SAYS EVERY RESULT KEYED.** ### The act has
### two: the identification's verdict, and the derivation of why a passing cross-check could not
### have seen the difference.

### ### **THE MUST-NOT-HIT ARM IS b202's: ### `the exponent` AND `the archimedean term` STAY
### ### UNKEYED.** ### The first is a fragment of notation and not a result; the second is a TERM
### OF AN IDENTITY that several acts own at their own grades, and ### **AN INDEX THAT ANSWERED
### ### `the archimedean term` WOULD BE OFFERING THIS ACT'S DEFINITIONAL FINDING AS THOUGH IT WERE
### ### A VERDICT ON THAT TERM'S BANKED VALUES, WHICH IS EXACTLY THE READING THE ACT REFUSES.**
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
    "    'the-remainder': ['the corpus eps against the source', 'the scaling convention',\n"
    "                     'the remainder identified', 'is the remainder theirs'],\n"
    "    'remainder-check-at-a-zero': ['why the cross-check passed',\n"
    "                     'a check at a zero', 'the invisible factor'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE REMAINDER IS NOT THE SOURCE'S (b312).\n"
    "    (\"the-remainder\", \"b312 (a decision at definitions)\",\n"
    "     \"the corpus's eps and CC's epsilon unfolded to their base objects and compared\"\n"
    "     \" constituent by constituent, artefact pinned by sha256 b8e0b54a... BEFORE a word of it\"\n"
    "     \" was read. ### **NINE CONSTITUENTS; EIGHT AGREE EXACTLY** -- mode family, auxiliary\"\n"
    "     \" vector, analytic continuation, the coefficient lam^2/(1-lam^2), the interval from\"\n"
    "     \" 1/rho to 1, the integrand, the value zero at the identity, and the one-sided\"\n"
    "     \" derivative. ### **THE NINTH IS THE SCALING ACTION'S NORMALIZATION EXPONENT AND IT\"\n"
    "     \" DISAGREES**: CC's eq (61) defines theta(lam)xi(v) := lam^(-1/2) xi(lam^-1 v), unitary,\"\n"
    "     \" so at the remainder's argument it is rho^(+1/2), and CC's Lemma 5.4 proof writes that;\"\n"
    "     \" the corpus declares theta(a)f(x) = a^(1/2) f(x/a) and its code applies r ** -0.5. ###\"\n"
    "     \" **THE TWO FUNCTIONS DIFFER BY A FACTOR OF rho, WHICH IS NOT A SCALAR. ### VERDICT:\"\n"
    "     \" DIFFERENT**\",\n"
    "     \"### A DECISION AT DEFINITIONS. ### **THIS ACT COMPARED TWO WRITTEN DEFINITIONS AND\"\n"
    "     \" COMPUTED NO ARCHIMEDEAN NUMBER. ### IT DOES NOT CALL ANY BANKED MEASUREMENT WRONG, AND\"\n"
    "     \" EVERY BANKED RESULT STANDS WHERE ITS OWN ACT LEFT IT.** ### The decision is made by\"\n"
    "     \" EXTRACTION (tools/b312_definitions.py, fixtures proving it can report either answer),\"\n"
    "     \" because the corpus's own flattener strips non-alphanumerics and cannot see a sign. ###\"\n"
    "     \" **THE SOURCE IS SELF-CONSISTENT AT THREE INDEPENDENT PLACES; THE CORPUS DISAGREES WITH\"\n"
    "     \" ITSELF** -- its Qeps carries r ** 0.5, matching CC's eq (99), and inside b38_act10.py\"\n"
    "     \" the identity's trace side and its remainder side carry opposite exponents. ### The\"\n"
    "     \" corpus's stated reason does not reach its conclusion: a support condition fixes a\"\n"
    "     \" DOMAIN, not an AMPLITUDE. ### **THE ENTAILMENT DOES NOT RUN** (ordered on SAME only).\"\n"
    "     \" ### M-2 UNCHANGED\",\n"
    "     \"data/b312_the_remainder.txt; data/b312_components_run.txt; data/b312_source_pin.txt;\"\n"
    "     \" CORRESPONDENCE.md row 136\"),\n"
    "    # ### A CHECK TAKEN AT A ZERO CANNOT SEE A FACTOR (b312).\n"
    "    (\"remainder-check-at-a-zero\", \"b312 (a derivation at definitions)\",\n"
    "     \"the corpus's ONE cross-check of its remainder against the source is the one-sided\"\n"
    "     \" derivative at the identity, which its header derives and CC's Lemma 5.4 states; the two\"\n"
    "     \" agree, and **THE AGREEMENT IS EMPTY**. ### Writing the common integral as F(rho), the\"\n"
    "     \" corpus's function is rho^(-1/2) F(rho) and the source's rho^(+1/2) F(rho); the interval\"\n"
    "     \" is empty at the identity so F(1) = 0, and the derivative of rho^s F(rho) there is\"\n"
    "     \" s F(1) + F'(1) = F'(1) **FOR EVERY s WHATEVER**. ### **A CROSS-CHECK TAKEN AT A ZERO OF\"\n"
    "     \" THE FUNCTION CANNOT SEE A MULTIPLICATIVE FACTOR THAT IS FINITE AND NONZERO THERE**\",\n"
    "     \"### A DERIVATION ABOUT WHERE A CHECK WAS TAKEN -- NEITHER AN EXCUSE NOR AN ACCUSATION.\"\n"
    "     \" ### **IT EXPLAINS WHY ONE CHECK WAS INSENSITIVE TO ONE FACTOR; IT IS NOT A CLAIM ABOUT\"\n"
    "     \" ANY OTHER CHECK THE CORPUS RAN, AND IT AUDITS NONE OF THEM.** ### The other channel was\"\n"
    "     \" checked as ordered: carto_atlas.py fixes its archimedean sign BY THE E2 CALIBRATION and\"\n"
    "     \" disclaims any sign claim, **SO THE THING TO BE CHECKED AGAINST IS ITSELF A\"\n"
    "     \" CALIBRATION** -- not a complaint about the atlas, which has always disclaimed it. ###\"\n"
    "     \" **W-ORD-REMAINDER-EXPONENT IS FILED, NOT RUN**, with its exact check named: re-run the\"\n"
    "     \" corpus's identity with the remainder's exponent flipped and nothing else touched, and\"\n"
    "     \" compare the residue -- **A COMPUTATION THIS ACT MAY NOT RUN**. ### It inherits\"\n"
    "     \" W-ORD-ARCH-NORM-READING (b301), still live. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b312_the_remainder.txt; tools/e16/carto_atlas.py (the calibrated sign);\"\n"
    "     \" data/b301_the_object_completed.txt; CORRESPONDENCE.md row 137\"),\n"
)

NEW_KEYS = ('the-remainder', 'remainder-check-at-a-zero')
ALIASES = ('the corpus eps against the source', 'the scaling convention',
           'the remainder identified', 'why the cross-check passed',
           'a check at a zero', 'the invisible factor')
MUST_NOT_HIT = ('the exponent', 'the archimedean term')


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
    print('b312 -- THE INDEX KEYS. ### THE IDENTIFICATION, AND THE INVISIBILITY.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-24s NO KEY before : %s' % (q, pre[q]))

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-28s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
        print('    %-28s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-36s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-24s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the exponent` AND `the archimedean term` STAY UNKEYED.** ### The first is a')
    print('  ### fragment of notation and not a result; the second is a TERM OF AN IDENTITY that')
    print('  ### other acts own at their own grades, and an index answering it would be offering')
    print('  ### this act\'s definitional finding as a verdict on that term\'s banked values --')
    print('  ### which is exactly the reading the act refuses.')

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
