# -*- coding: utf-8 -*-
"""b309_kernel.py -- THE SHADOW'S BUILD, ITS PROFILE, AND THE BYTE COMPARISONS.

### **EVERY NUMBER THIS ACT REPORTS ABOUT THE KERNEL COMES OUT OF THIS FILE.**

### ### **THE PRIMITIVES ARE IMPORTED FROM `b302_kernel.py`, NEVER COPIED** -- the standing design
### point. ### The byte comparisons that caught b298's BOM are the last thing that should exist in
### two versions.

### ### **THE ORDER OF OPERATIONS IS INHERITED AND IS NOT NEGOTIABLE: ### BASELINE FIRST.** ###
### Regenerate from the UNCHANGED `AllPrints.lean` and require byte-identity with the banked file.
### **IF THE REGENERATION CANNOT REPRODUCE WHAT IS ALREADY BANKED, NOTHING AFTER IT IS EVIDENCE.**

### ### **AND THE ONE THING THIS ACT ADDS TO THE INHERITED PROCEDURE: ### A TRUE-PREFIX CHECK ON
### ### THE PROFILE.** ### A build that ADDS terminals must leave every existing print line exactly
### where it was; if an old line moved or changed, the new profile is not the old one plus three,
### and the print count alone would not show it. ### **CHECKED BYTE-WISE, NOT LINE-WISE** -- b298's
### incident, where a byte-order mark passed two checks that could not see it.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_kernel as K  # noqa: E402  ### the byte checks are READ, never copied

SGS = K.SGS
ALLP = K.ALLP
PROFILE = K.PROFILE
MODULE = os.path.join(SGS, 'Core', 'ScalingTraceShadow.lean')
MODNAME = 'ScalingTraceShadow'
NS = 'B309'
OUT = os.path.join(ROOT, 'data', 'b309_kernel_run.txt')
BOM = K.BOM

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    K.LINES = LINES
    K.rec = rec
    rec('=' * 100)
    rec('b309 -- THE SHADOW BUILD AND ITS PROFILE. ### EVERY NUMBER FROM THIS FILE.')
    rec('=' * 100)
    rec('\n  SELF-TEST (the byte checks, imported from b302_kernel and re-run here):')
    if not K.self_test():
        rec('\n  ### REFUSING TO REPORT A PROFILE FROM CHECKS THAT FAIL THEIR OWN FIXTURES.')
        return 2

    banked = io.open(PROFILE, 'rb').read()
    head = K.git_show('AXIOM_PRINTS.txt')
    allp = io.open(ALLP, encoding='utf-8').read()
    imported = ('import ' + MODNAME) in allp
    printed = allp.count('#print axioms ' + NS + '.')

    rec('\n' + '-' * 100)
    rec('  THE STATE BEFORE ANYTHING IS CHANGED.')
    rec('-' * 100)
    n0, z0, o0 = K.count_prints(banked)
    rec('  banked profile on disk   : %d prints, %d zero-axiom, %d otherwise, %d bytes'
        % (n0, z0, o0, len(banked)))
    rec('  banked profile at HEAD   : %s'
        % ('IDENTICAL' if head == banked else '### DIFFERS FROM DISK ###'))
    rec('  BOM on the banked file   : %s' % banked.startswith(BOM))
    rec('  AllPrints imports %-18s : %s' % (MODNAME, imported))
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
    else:
        raw, rc, err = K.elaborate(ALLP)
        got = K.normalise(raw)
        base_ok = (got == banked)
        n, z, o = K.count_prints(got)
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
    raw, rc, err = K.elaborate(MODULE, olean=olean)
    mod = K.normalise(raw)
    nm, zm, om = K.count_prints(mod)
    src = io.open(MODULE, encoding='utf-8').read()
    rec('  module                   : %s' % os.path.basename(MODULE))
    rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
    rec('  terminals printed        : %d, %d zero-axiom, %d otherwise' % (nm, zm, om))
    rec('  compiled object written  : %s   %s'
        % (os.path.basename(olean), os.path.exists(olean)))
    rec('  imports in the module    : %d   ### VANILLA' % src.count('\nimport '))
    rec('  `native_decide` uses     : %d   ### **IT WOULD ADD AN AXIOM AND IS REFUSED**'
        % src.count('native_decide'))
    rec('  `sorry` occurrences      : %d' % src.count('sorry'))
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
        names = [ln.split()[-1] for ln in src.splitlines() if ln.startswith('#print axioms ')]
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
    raw, rc, err = K.elaborate(ALLP)
    new = K.normalise(raw)
    n1, z1, o1 = K.count_prints(new)
    rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
    rec('  prints before -> after   : %d -> %d      zero-axiom: %d -> %d      other: %d -> %d'
        % (n0, n1, z0, z1, o0, o1))
    rec('  bytes  before -> after   : %d -> %d' % (len(banked), len(new)))
    if rc != 0 or o1 != 0:
        rec('  ### HARD FAILURE -- a terminal came back depending on an axiom.')
        return 2

    # ### ### **THE TRUE-PREFIX CHECK, THIS ACT'S ADDITION.**
    prefix_ok = new.startswith(banked)
    rec('  ### **THE BANKED PROFILE IS A TRUE BYTE PREFIX OF THE NEW ONE : %s  %s**'
        % (prefix_ok, 'PASS' if prefix_ok else '### FAIL ###'))
    rec('  ### A build that ADDS terminals must leave every existing print line exactly where it')
    rec('  ### was. ### **THE PRINT COUNT ALONE WOULD NOT SHOW A LINE THAT MOVED OR CHANGED**, and')
    rec('  ### this is checked BYTE-WISE rather than line-wise -- b298\'s incident.')
    if not prefix_ok:
        rec('  ### REFUSING TO WRITE. ### The new profile is not the old one plus this act\'s')
        rec('  ### terminals, and that is a different build from the one the act registered.')
        return 2
    if new.startswith(BOM):
        rec('  ### HARD FAILURE -- the regenerated profile carries a BOM.')
        return 2

    open(PROFILE + '.tmp', 'wb').write(new)
    os.replace(PROFILE + '.tmp', PROFILE)
    back = io.open(PROFILE, 'rb').read()
    rec('  profile written and READ BACK BYTE-WISE : %s  %s'
        % (back == new, 'PASS' if back == new else '### FAIL ###'))
    rec('  the act\'s own terminals in the new profile :')
    for ln in back.decode('utf-8').splitlines():
        if NS + '.' in ln:
            rec('      %s' % ln)
    rec('\n' + '=' * 100)
    rec('  ### **COMPILED IS NOT CERTIFIED** (b289): the module is imported AND printed in the')
    rec('  ### same run that wrote the profile, so neither can land without the other.')
    rec('  ### **AND WHAT THE TERMINALS CERTIFY IS ARITHMETIC, NOT THE BARRIER.** ### The step from')
    rec('  ### them to the vanishing of the trace is the bank\'s derivation and is UNCOMPILED.')
    rec('=' * 100)
    return 0 if (back == new and z1 == n1) else 1


if __name__ == '__main__':
    code = main()
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(LINES) + '\n')
    sys.exit(code)
