# -*- coding: utf-8 -*-
"""b329_kernel.py -- THE FINITE-SIDE SEAL'S BUILD, ITS PROFILE, AND THE BYTE COMPARISONS.

### **EVERY NUMBER THIS ACT REPORTS ABOUT THE KERNEL COMES OUT OF THIS FILE.**

### ### **THE PRIMITIVES ARE IMPORTED FROM `b302_kernel.py`, NEVER COPIED** -- the standing design
### point (b302, b310). ### The byte comparisons that caught b298's BOM are the last thing that
### should exist in two versions.

### ### **TWO PHASES, TWO RUN FILES.** ### `--baseline` regenerates the profile from the UNCHANGED
### `AllPrints.lean` and requires byte-identity with the blob at HEAD, and STOPS -- run before the
### registration's build cap is written (b309's precedent). ### The full run repeats the baseline,
### compiles the module alone, writes the import AFTER the last import and the prints at the END of
### the certification file, regenerates, and requires the banked profile to be a TRUE BYTE PREFIX of
### the new one (b310's addition). ### **IF THE BASELINE CANNOT REPRODUCE WHAT IS BANKED, NOTHING
### AFTER IT IS EVIDENCE.**

### ### **WHAT IS REFUSED IN THE MODULE'S SOURCE, COUNTED HERE:** ### `import` (vanilla), `lemma`
### (the order says `theorem`), `native_decide` (an axiom), `sorry`, `axiom`.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_kernel as K  # noqa: E402  ### the byte checks are READ, never copied

SGS = K.SGS
ALLP = K.ALLP
PROFILE = K.PROFILE
MODNAME = 'FiniteSideSeal'
MODULE = os.path.join(SGS, 'Core', MODNAME + '.lean')
NS = 'B329'
D = os.path.join(ROOT, 'data')
BOM = K.BOM

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def run_name(base):
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    return os.path.join(D, name)


def refused_in_source(src):
    """### THE FIVE REFUSED FORMS, COUNTED ON THE SOURCE WITH ITS COMMENTS STRIPPED (b317: a gate that
    ### greps prose fires on the sentence saying the thing was not done)."""
    code = re.sub(r'/-.*?-/', '', src, flags=re.S)
    code = re.sub(r'--[^\n]*', '', code)
    return {
        'import': len(re.findall(r'^\s*import\s', code, re.M)),
        'lemma': len(re.findall(r'^\s*lemma\s', code, re.M)),
        'native_decide': code.count('native_decide'),
        'sorry': len(re.findall(r'\bsorry\b', code)),
        'axiom': len(re.findall(r'^\s*axiom\s', code, re.M)),
    }


def theorems_in(src):
    return re.findall(r'^theorem\s+([A-Za-z_][A-Za-z0-9_\']*)', src, re.M)


def main(argv):
    baseline_only = '--baseline' in argv
    module_only = '--module' in argv
    K.LINES = LINES
    K.rec = rec
    rec('=' * 100)
    rec('b329 -- THE FINITE-SIDE SEAL. ### %s. ### EVERY NUMBER FROM THIS FILE.'
        % ('THE BASELINE ALONE' if baseline_only else ('THE MODULE ALONE, RECOMPILED' if module_only else 'THE BUILD AND ITS PROFILE')))
    rec('=' * 100)
    if module_only:
        # ### the module recompiled alone (a docstring edit after the profile was written); nothing else touched,
        # ### and the profile on disk is required to carry exactly the module's prints, unchanged.
        src = io.open(MODULE, encoding='utf-8').read()
        olean = os.path.join(SGS, 'build', MODNAME + '.olean')
        raw, rc, err = K.elaborate(MODULE, olean=olean)
        mod = K.normalise(raw)
        nm, zm, om = K.count_prints(mod)
        names = theorems_in(src)
        ref = refused_in_source(src)
        prof = K.normalise(io.open(PROFILE, 'rb').read()).decode('utf-8', 'replace')
        inprof = all(ln in prof for ln in mod.decode('utf-8', 'replace').splitlines())
        rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
        rec('  terminals printed        : %d, %d zero-axiom, %d otherwise ; theorems %d' % (nm, zm, om, len(names)))
        for k in ('import', 'lemma', 'native_decide', 'sorry', 'axiom'):
            rec('  refused form `%-13s` in code (comments stripped) : %d' % (k, ref[k]))
        rec('  every printed line already in the profile on disk, unchanged : %s' % inprof)
        for ln in mod.decode('utf-8').splitlines():
            rec('      %s' % ln)
        rec('=' * 100)
        return 0 if (rc == 0 and om == 0 and nm == len(names) and not any(ref.values()) and inprof) else 2
    rec('\n  SELF-TEST (the byte checks, imported from b302_kernel and re-run here):')
    if not K.self_test():
        rec('\n  ### REFUSING TO REPORT A PROFILE FROM CHECKS THAT FAIL THEIR OWN FIXTURES.')
        return 2

    banked_raw = io.open(PROFILE, 'rb').read()
    head_raw = K.git_show('AXIOM_PRINTS.txt')
    banked = K.normalise(banked_raw)
    head = K.normalise(head_raw) if head_raw is not None else None
    allp = io.open(ALLP, encoding='utf-8').read()
    imported = ('import ' + MODNAME) in allp
    printed = allp.count('#print axioms ' + NS + '.')

    rec('\n' + '-' * 100)
    rec('  THE STATE BEFORE ANYTHING IS CHANGED.')
    rec('-' * 100)
    n0, z0, o0 = K.count_prints(banked)
    rec('  banked profile on disk   : %d prints, %d zero-axiom, %d otherwise, %d bytes' % (n0, z0, o0, len(banked)))
    rec('  banked profile at HEAD   : %s   ### compared NORMALISED (b309 D6)' % ('IDENTICAL' if head == banked else '### DIFFERS FROM DISK ###'))
    rec('  raw bytes on disk / at HEAD : %d / %s   ### they differ by line endings alone' % (len(banked_raw), len(head_raw) if head_raw is not None else 'absent'))
    rec('  BOM on the banked file   : %s   ### read from RAW bytes' % banked_raw.startswith(BOM))
    rec('  AllPrints lines / imports / prints : %d / %d / %d' % (len(allp.splitlines()), allp.count('\nimport ') + allp.startswith('import '), allp.count('#print axioms ')))
    rec('  AllPrints imports %-16s : %s' % (MODNAME, imported))
    rec('  AllPrints prints %s.*     : %d' % (NS, printed))
    rec('  module file present      : %s' % os.path.exists(MODULE))
    if head != banked:
        rec('  ### HARD FAILURE -- the working tree profile already differs from HEAD.')
        return 2
    if banked_raw.startswith(BOM):
        rec('  ### HARD FAILURE -- the banked profile already carries a BOM.')
        return 2

    rec('\n' + '-' * 100)
    rec('  (A) THE BASELINE. ### REGENERATE FROM THE UNCHANGED FILE AND REPRODUCE THE BANKED BYTES.')
    rec('      ### **IF THIS FAILS, NOTHING AFTER IT IS EVIDENCE.**')
    rec('-' * 100)
    if imported:
        rec('  ### AllPrints ALREADY imports the module -- the baseline arm cannot run against an')
        rec('  ### unchanged file. ### **SKIPPED, AND SAID RATHER THAN PASSED SILENTLY.**')
        if baseline_only:
            return 2
    else:
        raw, rc, err = K.elaborate(ALLP)
        got = K.normalise(raw)
        base_ok = (got == banked)
        n, z, o = K.count_prints(got)
        rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
        rec('  regenerated              : %d prints, %d zero-axiom, %d otherwise, %d bytes' % (n, z, o, len(got)))
        rec('  BYTE-IDENTICAL to banked : %s  %s' % (base_ok, 'PASS' if base_ok else '### FAIL ###'))
        if not base_ok:
            rec('  ### REFUSING TO PROCEED. ### A regeneration that cannot reproduce the banked file is')
            rec('  ### not a regeneration this act may build on.')
            return 2
        if baseline_only:
            rec('\n  ### THE BASELINE ALONE WAS ASKED FOR. ### Nothing built, nothing written to the kernel.')
            rec('=' * 100)
            return 0

    rec('\n' + '-' * 100)
    rec('  (B) THE MODULE. ### COMPILED ALONE, AND ITS PROFILE READ FROM ITS OWN OUTPUT.')
    rec('-' * 100)
    if not os.path.exists(MODULE):
        rec('  ### HARD FAILURE -- the module is not on disk: %s' % MODULE)
        return 2
    olean = os.path.join(SGS, 'build', MODNAME + '.olean')
    raw, rc, err = K.elaborate(MODULE, olean=olean)
    mod = K.normalise(raw)
    nm, zm, om = K.count_prints(mod)
    src = io.open(MODULE, encoding='utf-8').read()
    names = theorems_in(src)
    ref = refused_in_source(src)
    rec('  module                   : %s' % os.path.basename(MODULE))
    rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
    if err.strip():
        for ln in err.decode('utf-8', 'replace').splitlines()[:40]:
            rec('      stderr | %s' % ln)
    rec('  terminals printed        : %d, %d zero-axiom, %d otherwise' % (nm, zm, om))
    rec('  theorems declared        : %d ; every one printed : %s' % (len(names), all(('B329.' + nme) in mod.decode('utf-8', 'replace') for nme in names)))
    rec('  compiled object written  : %s   %s' % (os.path.basename(olean), os.path.exists(olean)))
    rec('  BOM on the module source : %s' % io.open(MODULE, 'rb').read().startswith(BOM))
    for k in ('import', 'lemma', 'native_decide', 'sorry', 'axiom'):
        rec('  refused form `%-13s` in code (comments stripped) : %d' % (k, ref[k]))
    if rc != 0 or om != 0 or nm == 0 or any(ref.values()) or nm != len(names):
        rec('  ### HARD FAILURE -- the module did not print a clean all-zero-axiom profile of every theorem,')
        rec('  ### or a refused form is present.')
        return 2
    for ln in mod.decode('utf-8').splitlines():
        rec('      %s' % ln)

    rec('\n' + '-' * 100)
    rec('  (C) THE CERTIFICATION FILE. ### THE IMPORT AFTER THE LAST IMPORT, THE PRINTS AT THE END,')
    rec('      WRITTEN HERE SO THEY CANNOT LAND IN A DIFFERENT COMMIT FROM THE MODULE (b289).')
    rec('-' * 100)
    prints = [ln.split()[-1] for ln in src.splitlines() if ln.startswith('#print axioms ')]
    if imported and printed:
        rec('  ### ALREADY PRESENT -- NOTHING WRITTEN. (idempotent)')
    else:
        lines = allp.rstrip('\n').split('\n')
        last_import = max(i for i, ln in enumerate(lines) if ln.startswith('import '))
        lines.insert(last_import + 1, 'import ' + MODNAME)
        lines += ['#print axioms ' + n for n in prints]
        data = ('\n'.join(lines) + '\n').encode('utf-8')
        open(ALLP + '.tmp', 'wb').write(data)
        os.replace(ALLP + '.tmp', ALLP)
        back = io.open(ALLP, encoding='utf-8').read()
        ok = (('import ' + MODNAME) in back and all(('#print axioms ' + n) in back for n in prints)
              and back.rstrip('\n').split('\n')[-len(prints):] == ['#print axioms ' + n for n in prints])
        rec('  import line added after the last import : %s' % (('import ' + MODNAME) in back))
        rec('  print lines added at the END            : %d' % len(prints))
        rec('  READ BACK from disk                     : %s  %s' % (ok, 'PASS' if ok else '### FAIL ###'))
        if not ok:
            return 1

    rec('\n' + '-' * 100)
    rec('  (D) THE PROFILE, REGENERATED FROM SOURCE AND WRITTEN AS BYTES.')
    rec('-' * 100)
    raw, rc, err = K.elaborate(ALLP)
    new = K.normalise(raw)
    n1, z1, o1 = K.count_prints(new)
    rec('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
    rec('  prints before -> after   : %d -> %d      zero-axiom: %d -> %d      other: %d -> %d' % (n0, n1, z0, z1, o0, o1))
    rec('  bytes  before -> after   : %d -> %d' % (len(banked), len(new)))
    if rc != 0 or o1 != 0:
        rec('  ### HARD FAILURE -- a terminal came back depending on an axiom, or the elaboration failed.')
        return 2
    prefix_ok = new.startswith(banked)
    rec('  ### **THE BANKED PROFILE IS A TRUE BYTE PREFIX OF THE NEW ONE : %s  %s**' % (prefix_ok, 'PASS' if prefix_ok else '### FAIL ###'))
    rec('  ### every pre-existing print line exactly where it was, checked BYTE-WISE (b298, b310).')
    added = n1 - n0
    idem = imported and printed
    rec('  prints added             : %d ; %s : %s'
        % (added, 'zero on the idempotent path (already imported and printed)' if idem else 'equal to the module\'s own terminals',
           (added == 0 and new == banked) if idem else (added == nm)))
    if not prefix_ok or (added != (0 if idem else nm)):
        rec('  ### REFUSING TO WRITE. ### The new profile is not the old one plus this act\'s terminals.')
        return 2
    if new.startswith(BOM):
        rec('  ### HARD FAILURE -- the regenerated profile carries a BOM.')
        return 2
    open(PROFILE + '.tmp', 'wb').write(new)
    os.replace(PROFILE + '.tmp', PROFILE)
    back = io.open(PROFILE, 'rb').read()
    rec('  profile written and READ BACK BYTE-WISE : %s  %s' % (back == new, 'PASS' if back == new else '### FAIL ###'))
    rec('  the act\'s own terminals in the new profile :')
    for ln in back.decode('utf-8').splitlines():
        if NS + '.' in ln:
            rec('      %s' % ln)
    rec('\n' + '=' * 100)
    rec('  ### **COMPILED IS NOT CERTIFIED** (b289): the module is imported AND printed in the same run')
    rec('  ### that wrote the profile. ### **AND WHAT THE TERMINALS CERTIFY IS WHAT THE MODULE\'S OWN')
    rec('  ### HEADER SAYS, GENERAL AND PER-CELL KEPT APART** -- the module header is the statement of')
    rec('  ### scope, and this file does not average it.')
    rec('=' * 100)
    return 0 if (back == new and z1 == n1) else 1


if __name__ == '__main__':
    code = main(sys.argv[1:])
    out = run_name('b329_kernel_baseline' if '--baseline' in sys.argv[1:]
                   else ('b329_kernel_module' if '--module' in sys.argv[1:] else 'b329_kernel_run'))
    with io.open(out, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(LINES) + '\n')
    print('  run file : %s' % os.path.basename(out))
    sys.exit(code)
