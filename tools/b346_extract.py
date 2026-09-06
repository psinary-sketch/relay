# -*- coding: utf-8 -*-
"""b346_extract.py -- THE EXTRACT STEP FOR THE EXPONENT BY RATE. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### b339's verdict and its floor reading, which this act's premise is;
### b344's ladder result for the one axis of the floor that has been priced, which is what makes the premise
### TESTABLE rather than assumed; b264's banked decay table with its converged / not-converged marking and its sharp
### rate, which is the object the rate is measured on; b315's sentence that along the ARGUMENT the rate moves a full
### power while along the cutoff it does not move at all, which is why the argument is the axis; b313's branch-two
### verdict and the standing clause that the exponent is fixed by the source's definition and not by a residue, which
### is the guard this act must not cross; b312's ninth constituent; the erratum's standing clause and the sentence
### about one identity carrying two conventions in one file; b322's resolving-power rule; the flip's own declared
### substitutions, so the two conventions are read from the copy-maker and not from memory; and the order's own
### sentences with the author's framing note. ### b283's law: every quotation located at its emitting file and its
### line before it is written anywhere else.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b346_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


E16 = os.path.join(ROOT, 'tools', 'e16')
FERRY = d('b346_ferry_2026-09-06.txt')
RULING = d('b346_ruling_2026-09-06.txt')
ERRATA = os.path.join(PP, 'ERRATA.md')

WANTED = [
    # ### ---- b339: the verdict this act's premise comes from, and the floor reading itself
    ('b339 -- the verdict, UNAFFORDABLE at the sealed ceiling', d('b339_the_exponent_resolved.txt'),
     '### ### **(1) THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.**'),
    ('### the price at the cheapest cell', d('b339_the_exponent_resolved.txt'),
     '###     a = 1.41 : R(128)/s =  4.71 ; rate X^-1.214 (rms 0.054 ; the last step X^-1.015) ; X_req =  812 ; ratio  6.34 (by the last step 1168)'),
    ('### the limit sits ABOVE BOTH CANDIDATES', d('b339_the_exponent_resolved.txt'),
     '### limit reading (R2) applied to the five frames the record already holds -- the margin\'s descent'),
    ('### a floor and not zero, and the price is an UNDER-estimate', d('b339_the_exponent_resolved.txt'),
     '### ### What it says is that the residual the price extrapolated is descending toward a FLOOR and not'),
    ("### the floor's three candidate origins", d('b339_the_exponent_resolved.txt'),
     '### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut\'s `tau`, the'),
    # ### ---- b344: the one axis that HAS been priced, which is what makes the premise testable
    ('b344 -- the residual moves with NY, of the size the floor requires', d('b344_the_floor_priced.txt'),
     '### ### **(1) THE RESIDUAL MOVES WITH `NY`, AND BY THE SEALED RULE THE MOVEMENT IS OF THE SIZE THE FLOOR'),
    ('### and it CONVERGES: from NY = 512 the remaining travel is about a ninth of the floor', d('b344_the_floor_priced.txt'),
     "### CORPUS'S OWN `NY = 512` THE REMAINING TRAVEL IS `7.059e-04`, about a ninth of the floor**; from"),
    ('### one axis moved is one axis moved', d('b344_the_floor_priced.txt'),
     '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    # ### ---- b264: the banked decay table, its marking, and its sharp rate -- the object the rate is measured on
    ('b264 -- the sharp rate, separately graded', d('b264_eps_even_decay.txt'),
     '### **THE SHARP RATE, SEPARATELY GRADED:** ### **`x^{3/2} eps_even(x) -> K_even = 1.568231065`**'),
    ("### the corpus's own formula, with its exponent in front", d('b264_eps_even_decay.txt'),
     '###   ### **`eps_n(rho) = [lam^2/(1-lam^2)] rho^{-1/2} INT_{1/rho}^{1} A_n(u) A_n(rho u) du`**'),
    ('### and after the substitution, the -3/2', d('b264_eps_even_decay.txt'),
     '###   ### ### **`eps_n(rho) = [lam^2/(1-lam^2)] rho^{-3/2} INT_1^{rho} A_n(v/rho) A_n(v) dv`.**'),
    ('### 3/2 is not an unsighted prediction', d('b264_eps_even_decay.txt'),
     '### `3/2` IS NOT AN UNSIGHTED PREDICTION AND IS NOT REGISTERED AS ONE.**'),
    ('b264 -- the decay table head', d('b264_run.txt'),
     '  rho       NG       eps_even         envelope C/rho   rel(NG,2NG)  rel(NQ,2NQ)  rho^1.5*eps    converged'),
    ('### the top converged cell', d('b264_run.txt'),
     '  100       800      1.559480084e-03  1.327819084e+00  2.49e-09     1.21e-09     1.559480084    True'),
    ('### the first cell above it is NOT converged', d('b264_run.txt'),
     '  200       1600     5.529529290e-04  6.639095421e-01  1.44e-08     1.36e-09     1.563987063    False'),
    ('### the void rows are not evidence about eps', d('b264_run.txt'),
     '  ### ### VALUE THAT IS WRONG BY ORDERS OF MAGNITUDE. ### THEY ARE NOT EVIDENCE ABOUT'),
    # ### ---- b315: why the ARGUMENT is the axis and the cutoff is not
    ('b315 -- along the argument a full power, along the cutoff none', d('b315_components_run.txt'),
     '    ### ARGUMENT the rate moves a full power; ### **ALONG THE CUTOFF IT DOES NOT MOVE AT'),
    ('### the same leading order in both, along the cutoff', d('b315_components_run.txt'),
     '    ### ### ### CONVENTION, AND AT THE SAME LEADING ORDER: ### `E2even(a) ~ CONST / log a`'),
    ("### the two conventions' argument asymptotics, side by side", d('b315_components_run.txt'),
     '    ###   banked  : `eps_even ~ K rho^(-3/2)`, so `INT_1^inf eps_even drho/rho` converges;'),
    # ### ---- b313 and b312: the guard this act must not cross
    ('b313 -- branch two, the residue is not the exponent', d('b313_the_exponent.txt'),
     '### ### ### **THE RESIDUE DOES NOT COLLAPSE. ### BRANCH TWO: ### THE RESIDUE IS NOT THE EXPONENT.**'),
    ('### the exponent is fixed by the source\'s own definition', d('b313_the_exponent.txt'),
     '### THE EXPONENT IS FIXED BY THE SOURCE\'S OWN DEFINITION OF THE OBJECT THE CORPUS'),
    ('### a residue is not a vote on that', d('b313_the_exponent.txt'),
     '### ### THAT.**'),
    ('b312 -- eight agree, the ninth is the whole of the act', d('b312_the_remainder.txt'),
     '### ### **EIGHT AGREE. ### THE NINTH IS THE WHOLE OF THIS ACT.**'),
    # ### ---- the erratum: the standing clause, and the one-identity-two-conventions sentence
    ('the erratum -- the standing clause it imposes', ERRATA,
     '> ### ***A banked value of the archimedean remainder — `eps`, `eps_even`, `E2`, or any quantity computed through them — is quotable only with its convention named.***'),
    ('### one identity, two conventions, one file', ERRATA,
     'the identity\'s trace side applies the square root of the scaling \u2014 the source\'s convention'),
    ('### the two functions differ by a factor of rho, which is not a scalar', ERRATA,
     '**The two functions therefore differ by a factor of `\u03c1`, which is not a scalar.**'),
    # ### ---- the flip's own declared substitutions: the two conventions read from the copy-maker
    ("the flip -- b264's evaluator, the FLIP line", t('b313_flip.py'),
     "             'return lam2 / (1 - lam2) * (r ** -0.5) * I',"),
    ('### and what it becomes in the copy', t('b313_flip.py'),
     "             'return lam2 / (1 - lam2) * (r ** 0.5) * I',"),
    ('### the copy writes its output somewhere else', t('b313_flip.py'),
     "             r\"BANK = r'D:\\relay\\data\\b313f_b264_scratch.txt'\","),
    ("the owner's evaluator, unedited", os.path.join(E16, 'b264_eps_decay.py'),
     '    return lam2 / (1 - lam2) * (r ** -0.5) * I'),
    ("the flipped copy, which is the source's convention", os.path.join(E16, 'b313f_b264_eps_decay.py'),
     '    return lam2 / (1 - lam2) * (r ** 0.5) * I'),
    # ### ---- b322's rule, which the verdict is stated under
    ("b322 -- under-resolved is the weaker of the two", d('b322_components_run.txt'),
     '  ### ### ### **THE ACT TAKES THE WEAKER OF THE TWO: ### UNDER-RESOLVED.** ###'),
    ('### and it carries its price', d('b322_the_membership.txt'),
     '### ### ### **(5) SO THE VERDICT IS `UNDER-RESOLVED`, AND IT CARRIES ITS PRICE.**'),
    # ### ---- the order, and the author's framing note
    ('the order -- leg 2, the exponent by rate', FERRY,
     'LEG 2 (b345) \u2014 THE EXPONENT BY RATE: the value-based split is'),
    ('### the premise, tested not assumed', FERRY,
     'premise, tested not assumed \u2014 first, measure the residual\'s'),
    ('### the alternative discriminator', FERRY,
     'even sector\'s decay rate along the argument, which the record'),
    ('### the three verdicts', FERRY,
     'the rate. Verdicts: (RESOLVED, the convention named, the'),
    ('the ruling -- the rate is the principled discriminator', RULING,
     'reading makes the rate the principled discriminator rather than'),
    ('### and the framing confers nothing', RULING,
     'a second attempt at the value \u2014 and that this framing confers'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b346_extract.py -- THE EXPONENT BY RATE. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
