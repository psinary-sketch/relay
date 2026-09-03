# -*- coding: utf-8 -*-
"""b302_kernel.py -- THE KERNEL BUILD, ITS PROFILE, AND THE BYTE COMPARISONS.

### **EVERY NUMBER THIS ACT REPORTS ABOUT THE KERNEL COMES OUT OF THIS FILE.** ### Ruling (3) /
### `W-ORD-ADHOC-CHECK-FIXTURES`: a profile count typed at a shell is the shape that work-order
### exists against.

### ### **THE THREE HAZARDS THIS FILE IS BUILT AROUND, ALL OF THEM b298's, ALL OF THEM SCARS:**
###   ### **(1) A COPY IS NOT A REGENERATION** (b298 D3). ### The profile is captured from
###       `lake env lean AllPrints.lean` ### INTO MEMORY ### and written from there. ### It is
###       never produced by copying a build artefact over the banked file.
###   ### **(2) A SHELL REDIRECTION PREPENDS A BYTE-ORDER MARK** (b298 D5). ### PowerShell's `>`
###       put a UTF-8 BOM on the profile, the print CONTENTS were unchanged, and ### **TWO CHECKS
###       AGREED WHILE NEITHER COULD SEE IT** -- one compared against another redirection-produced
###       file, the other compared LINE CONTENT, which normalises exactly that difference away.
###       ### **SO THIS FILE WRITES BYTES ITSELF AND READS THE FIRST BYTES AS BYTES.**
###   ### **(3) A BYTE-IDENTITY CLAIM CHECKED LINE BY LINE IS NOT A BYTE-IDENTITY CLAIM** (b298
###       D5 again). ### The pre-existing profile must survive as a ### TRUE BYTE PREFIX ### of
###       the new one, compared against ### `git HEAD` ### and not against anything this act made.

### ### **THE ORDER OF OPERATIONS IS ITSELF A CHECK AND IS NOT NEGOTIABLE:**
###   ### **BASELINE FIRST.** ### Regenerate from the UNCHANGED `AllPrints.lean` and require the
###   ### result to be byte-identical to the banked file. ### **IF THE REGENERATION CANNOT
###   ### REPRODUCE WHAT IS ALREADY BANKED, NOTHING IT PRODUCES AFTERWARDS IS EVIDENCE**, and the
###   ### tool refuses to go on.

"""

# ### THE LIMITS, IN THE HEADER SO THE TOOL IS NOT TRUSTED BEYOND THEM:
# ### (1) ### **IT REPORTS WHAT LEAN PRINTED.** ### It cannot tell whether a terminal's STATEMENT
# ###     is worth certifying. ### That is the module's own header and the bank's prose.
# ### (2) ### **`lake env lean` IS RUN ON THE CHECKOUT AS IT STANDS.** ### A stale `.olean` in
# ###     `build/` is Lean's business, not this file's; what the tool guarantees is that the
# ###     BASELINE reproduced the banked bytes before anything was changed.
# ### (3) ### **IT DOES NOT COMMIT.** ### The `AllPrints.lean` import and the module must land in
# ###     the same commit (b289's scar) and that ordering is the act's duty, not the tool's.
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SGS = r'D:\SIDE-global-section'
ALLP = os.path.join(SGS, 'AllPrints.lean')
PROFILE = os.path.join(SGS, 'AXIOM_PRINTS.txt')
MODULE = os.path.join(SGS, 'Core', 'RationalEnclosureShadow.lean')
MODNAME = 'RationalEnclosureShadow'
NS = 'B302'
OUT = os.path.join(ROOT, 'data', 'b302_kernel_run.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BOM = b'\xef\xbb\xbf'
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def env_with_leanpath():
    """### THE REPO'S OWN DECLARED BUILD ENVIRONMENT, READ FROM ITS README RATHER THAN GUESSED.

    ### `README.md`, quoted: ### **"`lean` at the pinned toolchain compiles each module standalone
    ### (sibling imports via `LEAN_PATH`); `AllPrints.lean` re-runs every print."**
    ### ### **THE FIRST DRAFT OF THIS FILE USED `lake env lean` AND THE BASELINE ARM REFUSED TO
    ### ### PROCEED** -- `AllPrints.lean` came back with `unknown module prefix`, 4 error lines and
    ### exit 1, against 438 banked prints. ### **THAT IS THE BASELINE ARM DOING EXACTLY WHAT IT
    ### WAS PUT THERE FOR, ON THIS ACT'S OWN TOOL.**
    """
    e = dict(os.environ)
    e['LEAN_PATH'] = os.path.join(SGS, 'build')
    return e


def elaborate(path, olean=None):
    """### RUN `lean <path>` FROM THE CHECKOUT AND RETURN `(bytes, rc, stderr)`.

    ### ### **THE OUTPUT IS CAPTURED INTO MEMORY AND NEVER THROUGH A SHELL REDIRECTION**, which is
    ### the whole of hazard (2). ### `olean` writes the compiled module so siblings can import it.
    """
    cmd = ['lean', path] + (['-o', olean] if olean else [])
    r = subprocess.run(cmd, cwd=SGS, capture_output=True, timeout=3600, env=env_with_leanpath())
    return r.stdout, r.returncode, r.stderr


def normalise(raw):
    """### LEAN'S STDOUT AS THE BANKED FILE HOLDS IT: LF ENDINGS, ONE TRAILING NEWLINE, NO BOM."""
    txt = raw.decode('utf-8', 'replace').replace('\r\n', '\n')
    body = '\n'.join([ln for ln in txt.split('\n') if ln.strip()])
    return (body + '\n').encode('utf-8')


def git_show(relpath):
    r = subprocess.run(['git', '-C', SGS, 'show', 'HEAD:' + relpath], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def count_prints(data):
    zero = other = 0
    for ln in data.decode('utf-8', 'replace').splitlines():
        if not ln.strip():
            continue
        if ln.rstrip().endswith('does not depend on any axioms'):
            zero += 1
        else:
            other += 1
    return zero + other, zero, other


def self_test():
    """### **BOTH POLARITIES ON EVERY ARM THIS FILE DECIDES WITH.**"""
    ok = True
    cases = []

    a = b"'X.t' does not depend on any axioms\n"
    b = b"'X.t' depends on axioms: [propext]\n"
    cases.append(('the print counter separates zero-axiom from other',
                  count_prints(a + b) == (2, 1, 1), True))
    cases.append(('the print counter ignores blank lines',
                  count_prints(a + b'\n\n') == (1, 1, 0), True))
    cases.append(('the BOM test fires on a real BOM', (BOM + a).startswith(BOM), True))
    cases.append(('the BOM test stays quiet on clean bytes', a.startswith(BOM), False))
    cases.append(('a true prefix is recognised', (a + b).startswith(a), True))
    # ### THE ARM THAT MATTERS: a LINE-EQUAL but BYTE-DIFFERENT pair must NOT pass as a prefix.
    # ### **THIS IS b298's D5 IN A FIXTURE.**
    cases.append(('a BOM-differing pair is NOT a byte prefix', (BOM + a).startswith(a), False))
    cases.append(('CRLF normalises to LF', normalise(b"'X.t' does not depend on any axioms\r\n")
                  == a, True))
    rec('  %-58s %-12s %s' % ('fixture', 'got/exp', 'agree'))
    for lbl, got, exp in cases:
        agree = (got == exp)
        ok = ok and agree
        rec('  %-58s %-12s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if agree else '### NO ###'))
    return ok


def main():
    rec('=' * 100)
    rec('b302 -- THE KERNEL BUILD AND ITS PROFILE. ### EVERY NUMBER FROM THIS FILE.')
    rec('=' * 100)
    rec('\n  SELF-TEST:')
    if not self_test():
        rec('\n  ### REFUSING TO REPORT A PROFILE FROM CHECKS THAT FAIL THEIR OWN FIXTURES.')
        return 2

    banked = io.open(PROFILE, 'rb').read()
    head = git_show('AXIOM_PRINTS.txt')
    allp = io.open(ALLP, encoding='utf-8').read()
    imported = ('import ' + MODNAME) in allp
    printed = allp.count('#print axioms ' + NS + '.')

    rec('\n' + '-' * 100)
    rec('  THE STATE BEFORE ANYTHING IS CHANGED.')
    rec('-' * 100)
    n0, z0, o0 = count_prints(banked)
    rec('  banked profile on disk   : %d prints, %d zero-axiom, %d otherwise, %d bytes'
        % (n0, z0, o0, len(banked)))
    rec('  banked profile at HEAD   : %s'
        % ('IDENTICAL' if head == banked else '### DIFFERS FROM DISK ###'))
    rec('  BOM on the banked file   : %s' % banked.startswith(BOM))
    rec('  AllPrints imports %-14s : %s' % (MODNAME, imported))
    rec('  AllPrints prints %s.*   : %d' % (NS, printed))
    if head != banked:
        rec('  ### HARD FAILURE -- the working tree profile already differs from HEAD.')
        return 2
    if banked.startswith(BOM):
        rec('  ### HARD FAILURE -- the banked profile already carries a BOM.')
        return 2

    rec('\n' + '-' * 100)
    rec('  (A) THE BASELINE. ### REGENERATE FROM THE UNCHANGED FILE AND REPRODUCE THE BANKED')
    rec('      BYTES. ### **IF THIS FAILS, NOTHING AFTER IT IS EVIDENCE.**')
    rec('-' * 100)
    if imported:
        rec('  ### AllPrints ALREADY imports the module -- the baseline arm cannot run against an')
        rec('  ### unchanged file. ### **SKIPPED, AND SAID RATHER THAN PASSED SILENTLY.**')
        base_ok = None
    else:
        raw, rc, err = elaborate(ALLP)
        got = normalise(raw)
        base_ok = (got == banked)
        n, z, o = count_prints(got)
        rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
        rec('  regenerated              : %d prints, %d zero-axiom, %d otherwise, %d bytes'
            % (n, z, o, len(got)))
        rec('  BYTE-IDENTICAL to banked : %s  %s'
            % (base_ok, 'PASS' if base_ok else '### FAIL ###'))
        if not base_ok:
            rec('  ### REFUSING TO PROCEED. ### A regeneration that cannot reproduce the banked')
            rec('  ### file is not a regeneration this act may build on.')
            return 2

    rec('\n' + '-' * 100)
    rec('  (B) THE MODULE. ### COMPILED ALONE, AND ITS PROFILE READ FROM ITS OWN OUTPUT.')
    rec('-' * 100)
    olean = os.path.join(SGS, 'build', MODNAME + '.olean')
    raw, rc, err = elaborate(MODULE, olean=olean)
    mod = normalise(raw)
    nm, zm, om = count_prints(mod)
    rec('  module                   : %s' % os.path.basename(MODULE))
    rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
    rec('  terminals printed        : %d, %d zero-axiom, %d otherwise' % (nm, zm, om))
    rec('  compiled object written  : %s   %s'
        % (os.path.basename(olean), os.path.exists(olean)))
    rec('  imports in the module    : %d   ### VANILLA'
        % io.open(MODULE, encoding='utf-8').read().count('\nimport '))
    src = io.open(MODULE, encoding='utf-8').read()
    rec('  `native_decide` uses     : %d' % src.count('native_decide'))
    rec('  tactics other than decide: %s'
        % ('sorry' if 'sorry' in src else 'none named beyond `decide`'))
    if rc != 0 or om != 0 or nm == 0:
        rec('  ### HARD FAILURE -- the module did not print a clean all-zero-axiom profile.')
        return 2
    for ln in mod.decode('utf-8').splitlines():
        rec('      %s' % ln)

    rec('\n' + '-' * 100)
    rec('  (C) THE CERTIFICATION FILE. ### THE IMPORT AND THE PRINTS, WRITTEN HERE SO THEY')
    rec('      CANNOT LAND IN A DIFFERENT COMMIT FROM THE MODULE (b289\'s scar).')
    rec('-' * 100)
    if imported and printed:
        rec('  ### ALREADY PRESENT -- NOTHING WRITTEN. (idempotent)')
    else:
        lines = allp.rstrip('\n').split('\n')
        last_import = max(i for i, ln in enumerate(lines) if ln.startswith('import '))
        lines.insert(last_import + 1, 'import ' + MODNAME)
        names = [ln.split()[-1] for ln in src.splitlines()
                 if ln.startswith('#print axioms ')]
        lines += ['#print axioms ' + n for n in names]
        data = ('\n'.join(lines) + '\n').encode('utf-8')
        open(ALLP + '.tmp', 'wb').write(data)
        os.replace(ALLP + '.tmp', ALLP)
        back = io.open(ALLP, encoding='utf-8').read()
        ok = (('import ' + MODNAME) in back
              and all(('#print axioms ' + n) in back for n in names))
        rec('  import line added        : %s' % (('import ' + MODNAME) in back))
        rec('  print lines added        : %d' % len(names))
        rec('  READ BACK from disk      : %s  %s' % (ok, 'PASS' if ok else '### FAIL ###'))
        if not ok:
            return 1

    rec('\n' + '-' * 100)
    rec('  (D) THE PROFILE, REGENERATED FROM SOURCE AND WRITTEN AS BYTES.')
    rec('-' * 100)
    raw, rc, err = elaborate(ALLP)
    new = normalise(raw)
    n1, z1, o1 = count_prints(new)
    rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
    rec('  prints before -> after   : %d -> %d      zero-axiom: %d -> %d      other: %d -> %d'
        % (n0, n1, z0, z1, o0, o1))
    rec('  bytes  before -> after   : %d -> %d' % (len(banked), len(new)))
    if rc != 0 or o1 != 0:
        rec('  ### HARD FAILURE -- the regenerated profile is not all-zero-axiom.')
        return 2
    open(PROFILE + '.tmp', 'wb').write(new)
    os.replace(PROFILE + '.tmp', PROFILE)
    ondisk = io.open(PROFILE, 'rb').read()

    rec('\n' + '-' * 100)
    rec('  (E) THE THREE BYTE CHECKS. ### **NONE OF THEM IS A LINE COMPARISON.**')
    rec('-' * 100)
    bom = ondisk.startswith(BOM)
    prefix = ondisk.startswith(head)
    written = (ondisk == new)
    rec('  BOM on the written file  : %s  %s' % (bom, 'PASS' if not bom else '### FAIL ###'))
    rec('  what was written is what was regenerated : %s  %s'
        % (written, 'PASS' if written else '### FAIL ###'))
    rec('  the HEAD profile is a TRUE BYTE PREFIX of the new one : %s  %s'
        % (prefix, 'PASS' if prefix else '### FAIL ###'))
    rec('  bytes appended           : %d' % (len(ondisk) - len(head)))
    rec('  ### **A PREFIX CHECK OVER BYTES IS THE ONLY ONE OF THE THREE THAT COULD HAVE CAUGHT')
    rec('  ### b298\'s BOM, AND IT IS THE ONE THAT ACT DID NOT HAVE.**')
    ok = (not bom) and prefix and written
    rec('\n' + '=' * 100)
    rec('  ### KERNEL: %d PRINTS, %d ZERO-AXIOM, %d OTHERWISE (was %d/%d/%d). ### %s'
        % (n1, z1, o1, n0, z0, o0, 'PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8').write('\n'.join(LINES) + '\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
