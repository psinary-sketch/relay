# -*- coding: utf-8 -*-
"""b314_errata.py -- THE CONVENTION ERRATUM, WRITTEN BY THE AUTHOR'S RULING.

### ### **THE RULING, VERBATIM:** ### *"E1 pattern -- an internal-record ERRATA entry for the
### remainder's normalization convention: the owner instrument untouched, b313's bank the
### correction of record, and banked remainder values quotable only with their convention named."*

### ### **THE `E1` PRECEDENT, AND WHY IT IS THE RIGHT ONE.** ### At `E-2026-08-31-1` a clause was
### withdrawn and ### **THE FOUR SITES CARRYING IT WERE LEFT BYTE-IDENTICAL AND NOT REWRITTEN**, on
### the stated ground that ### **THE RECORD DOES NOT SILENTLY OVERWRITE ITSELF.** ### The same
### shape holds here: the instrument computes what it computes, the acts that used it said what
### they said, and what is corrected is ### **THE RECORD'S ACCOUNT OF WHAT THOSE NUMBERS ARE
### COMPUTATIONS OF.**

### ### **WHAT THIS TOOL WILL NOT DO:** ### it will not edit an owner instrument, it will not
### restate an earlier entry, and it will not write twice. ### **THE ENTRY IS READ BACK FROM THE
### FILE AFTER THE WRITE, AND THE ID IS TAKEN FROM WHAT THE FILE HOLDS RATHER THAN FROM WHAT THIS
### TOOL INTENDED.**
"""
import io
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r'D:\relay'
PP = r'D:\MY-DOwnloads\PLACE-papers'
ERRATA = os.path.join(PP, 'ERRATA.md')
EID = 'E-2026-09-03-1'
TITLE = ("The archimedean remainder's normalization convention is the corpus's own, not the "
         "source's (INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED)")

OWNERS = ['tools/e16/qeps_layer.py', 'tools/e16/b38_act10.py', 'tools/e16/b264_eps_decay.py']

ENTRY = """
---

## %s — %s

**Filed 2026-09-03 (b314), on the author's ruling of the same day. ### NO DEPOSITED ARTIFACT IS AFFECTED.** This is an **internal-record** entry: it concerns an instrument convention and the record's account of what certain banked numbers are computations *of*. **It is not a claim that any banked number is wrong, and it is not a retraction of anything.**

**What was found (b312, by unfolding definitions).** The corpus's archimedean remainder `eps` is declared in its own instrument header to be the source's equation — *"eps(rho), their (85)"*, under formulas *"AS SUPPLIED"*. Unfolded to base objects, **eight of its nine constituents agree with the source exactly** — the mode family, the auxiliary vector, the analytic continuation, the coefficient `λ²/(1−λ²)`, the interval, the integrand, the value zero at the identity, and the one-sided derivative at the identity. **The ninth is the scaling action's normalization exponent, and it disagrees.**

> The source defines its scaling action at its own eq. (61): **`(ϑ(λ)ξ)(v) := λ^(−1/2) ξ(λ^(−1) v)`** — unitary, obtained by conjugating a unitary representation — so at the remainder's argument it is **`ρ^(+1/2)`**; and the source's Lemma 5.4 proof writes exactly that, as does its own worked unfolding of an inner product of the same shape. The corpus's header declares **`θ(a) f(x) = a^(1/2) f(x/a)`** and its code applies **`r ** -0.5`**.

**The two functions therefore differ by a factor of `ρ`, which is not a scalar.**

**Why it was not seen.** The corpus's one cross-check of this object against the source is the one-sided derivative at the identity, and the two agree. **The agreement is empty.** The integration interval is empty at the identity, so the common integral vanishes there, and the derivative of `ρ^s F(ρ)` at `ρ = 1` is `F′(1)` **for every `s` whatever**. ***A cross-check taken at a zero of the function cannot see a multiplicative factor that is finite and nonzero there.***

**And the divergence is internal as well as external.** In the same instrument, `Qeps` carries `r ** 0.5`, which agrees with the source's eq. (99); and inside `b38_act10.py` **the identity's trace side applies the square root of the scaling — the source's convention — while its remainder side applies `r ** -0.5`.** *One identity, two conventions, one file.*

**What was measured (b313).** The remainder was recomputed under the source's exponent **in a copy of the instrument, the owner files untouched**, everything else byte-identical and shown by diff. The residue `Tr − A − E2` fell from `(4.0486, 3.3740, 3.0478, 2.5208, 2.4540, 2.3134)` to `(3.7150, 2.9792, 2.6347, 2.0917, 2.0242, 1.8834)` at `a² = 2, 3, 4, 8, 9, 12` — **a shrinkage of 8%% to 19%%, with the order of magnitude kept at every cell.** The archimedean term `A` and the trace `Tr` do not move at all. **So the convention accounts for part of the residue and not for the rest, and nothing says what accounts for the rest.**

**The correction, and the form it takes.** ### **NO OWNER INSTRUMENT FILE IS EDITED.** `qeps_layer.py`, `b38_act10.py` and `b264_eps_decay.py` stand byte-identical. **The correction of record is b313's bank**, `relay data/b313_the_exponent.txt`, with b312's identification at `data/b312_the_remainder.txt`. This follows the **`E1` precedent** (`E-2026-08-31-1`), where the sites carrying a superseded clause were left byte-identical and not rewritten, because ***the record does not silently overwrite itself.***

> ### **THE STANDING CLAUSE THIS ENTRY IMPOSES, AND IT TRAVELS WITH THE RECORD RATHER THAN WITH ANY ACT'S MEMORY:**
>
> ### ***A banked value of the archimedean remainder — `eps`, `eps_even`, `E2`, or any quantity computed through them — is quotable only with its convention named.*** The banked values are computed under the corpus's own `ρ^(−1/2)`; the source's object carries `ρ^(+1/2)`; and a value quoted without saying which is a value whose object is not determined.

**Scope, stated so it is not read wider than it is.** This entry concerns **an instrument convention and the record's description of it**. *It is not a claim that the deposited mathematics is wrong, not a claim that any banked number is wrong, and not a retraction.* No grade moves and no act is re-verdicted; every banked measurement stands exactly where its own act left it, at its own grade. **What may change is what a banked number is a computation of, and that is an instrument statement.** Whether the corpus meant the source's function and missed, or defined its own object and mis-described it, is **not decided** — a corpus may define its own object; what it may not do is call that object the source's.

**Still open, and named here rather than left implicit:** the remaining share of the residue (`relay` `W-ORD-REMAINDER-EXPONENT`, discharged as a computation and re-filed as a routing); the archimedean term's own sign, which `carto_atlas.py` fixes *"BY the E2 calibration"* while disclaiming any sign claim (`W-ORD-A-PLUS-E2`); and the fact that **two of five convention sites already carried the source's exponent and nobody has swept the instrument for others** (`W-ORD-CONVENTION-SWEEP`).
""" % (EID, TITLE)


def main():
    print('=' * 100)
    print('b314_errata.py -- THE CONVENTION ERRATUM. ### THE OWNER INSTRUMENT IS NOT EDITED.')
    print('=' * 100)

    # ### ### **THE OWNER FILES, CHECKED BEFORE THE ENTRY IS WRITTEN AND AGAIN AFTER.**
    def owners_clean():
        r = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True)
        return r.stdout.strip()

    pre = owners_clean()
    print('  owner instrument files, `git status` BEFORE : %r' % pre)
    if pre:
        print('  ### REFUSING TO WRITE AN ENTRY THAT SAYS THE OWNERS ARE UNTOUCHED WHILE THEY ARE')
        print('  ### MODIFIED. ### The entry\'s central claim would be false as written.')
        return 2

    cur = io.open(ERRATA, encoding='utf-8').read()
    if EID in cur:
        print('  ### ENTRY ALREADY PRESENT -- NOTHING WRITTEN. (idempotent)')
    else:
        io.open(ERRATA, 'w', encoding='utf-8', newline='\n').write(cur.rstrip('\n') + '\n' + ENTRY)
        print('  entry appended : %s' % EID)

    # ### ### **READ BACK FROM THE FILE. ### THE ID IS TAKEN FROM WHAT THE FILE HOLDS.**
    back = io.open(ERRATA, encoding='utf-8').read()
    ids = re.findall(r'^## (E-\d{4}-\d{2}-\d{2}-\d+) \u2014 ', back, re.M)
    print()
    print('  ### READ BACK FROM THE FILE:')
    print('  entry IDs in `ERRATA.md` : %d' % len(ids))
    print('  ### **THIS ACT\'S ENTRY ID, TAKEN FROM THE FILE : %s**'
          % (EID if EID in ids else '### NOT FOUND ###'))
    ok = EID in ids and len(ids) == len(set(ids))
    print('  every ID unique : %s' % (len(ids) == len(set(ids))))
    body = back.split('## %s' % EID, 1)[-1] if EID in back else ''
    clauses = [
        ('the internal-record marking', 'NO DEPOSITED ARTIFACT IS AFFECTED'),
        ('the owner instrument untouched', 'NO OWNER INSTRUMENT FILE IS EDITED'),
        ("b313's bank as the correction of record", 'data/b313_the_exponent.txt'),
        ('the quotability clause', 'quotable only with its convention named'),
        ('the E1 precedent cited', 'E-2026-08-31-1'),
        ('the refusal to read it wider', 'not a claim that any banked number is wrong'),
    ]
    print()
    print('  ### THE RULING\'S OWN CLAUSES, EACH LOCATED IN THE WRITTEN ENTRY:')
    for lbl, needle in clauses:
        got = needle in body
        ok = ok and got
        print('    %-44s %s  %s' % (lbl, got, 'PASS' if got else '### FAIL ###'))

    post = owners_clean()
    print()
    print('  owner instrument files, `git status` AFTER : %r' % post)
    same = (post == pre == '')
    print('  ### **THE OWNER INSTRUMENT FILES ARE BYTE-IDENTICAL, BEFORE AND AFTER : %s**' % same)
    ok = ok and same

    p = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD', '--', 'ERRATA.md'],
                       capture_output=True, text=True)
    added = removed = 0
    if p.stdout.strip():
        parts = p.stdout.split()
        added, removed = int(parts[0]), int(parts[1])
    print('  `ERRATA.md` vs HEAD : ### **+%d / -%d**' % (added, removed))
    print('  ### ### **PURELY ADDITIVE : %s** ### -- an errata ledger that deletes a line is a'
          % (removed == 0 and added > 0))
    print('  ### ledger restating itself, which this ledger\'s own header forbids: *"Entries are')
    print('  ### retained across deposits and are never restated to the current line."*')
    ok = ok and removed == 0 and added > 0
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
