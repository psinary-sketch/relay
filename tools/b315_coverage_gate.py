# -*- coding: utf-8 -*-
"""b315_coverage_gate.py -- THE KERNEL-COVERAGE GATE. ### **IT IS SUPPOSED TO FAIL.**

### ### **WHAT IT COMPARES.** ### The set of `Core/` modules that carry at least one
### `#print axioms` target, against the set of modules the certification file imports.
### ### **A MODULE WITH A TERMINAL IT NEVER CERTIFIES IS THE DEFECT b314 FOUND**, and until b314
### there was no check whose scope included it: `AllPrints.lean` is a hand-maintained import list,
### and ### **NOTHING IN THE BUILD FAILS WHEN A MODULE IS LEFT OUT OF IT.**

### ### ### **THIS GATE IS WRITTEN TO FAIL TODAY, AND ITS FAILING IS THE POINT.** ### A gate added
### in the state where it passes tells nobody anything; ### **A GATE ADDED IN THE STATE WHERE IT
### ### FIRES IS A GATE WHOSE FIRING HAS BEEN SEEN.** ### Nothing is repaired by this act: no module
### is added to the certification file and no `.lean` file is touched.

### ### **AND THE DISTINCTION IT KEEPS, WHICH THE HEADLINE NUMBER BLURS:** ### b314 reported
### **twenty-five modules outside** the certification file. ### One of those carries no print target
### of its own -- its terminals are printed by a separate checker module, which is itself one of the
### twenty-five. ### **SO THE GATE'S OWN CRITERION -- MODULES CARRYING A PRINT TARGET -- SEES ONE
### ### FEWER, AND BOTH NUMBERS ARE PRINTED RATHER THAN ONE CHOSEN.**
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIDE = r'D:\SIDE-global-section'
CORE = os.path.join(SIDE, 'Core')
ALLP = os.path.join(SIDE, 'AllPrints.lean')
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

IMPORT = re.compile(r'^import\s+(\S+)', re.M)
PRINT = re.compile(r'^#print axioms\s+(\S+)', re.M)
NS = re.compile(r'^namespace\s+(\S+)', re.M)
OPEN = re.compile(r'^open\s+(\S+)', re.M)


def read(path):
    return io.open(path, encoding='utf-8', errors='replace').read()


def imports_of(text):
    return IMPORT.findall(text)


def targets_of(text):
    return PRINT.findall(text), NS.findall(text), OPEN.findall(text)


def self_test():
    """### **FIXTURES. ### THE GATE MUST BE ABLE TO PASS, OR ITS FAILURE MEANS NOTHING.**"""
    ok = []
    # ### (i) it SEES a module with a print target that is not imported.
    mods = {'A': '#print axioms A.x\n', 'B': 'def y := 1\n'}
    allp = 'import B\n'
    have = {m for m, s in mods.items() if PRINT.findall(s)}
    ok.append((have - set(imports_of(allp))) == {'A'})
    # ### (ii) it is QUIET when every module with a target is imported.
    allp2 = 'import A\nimport B\n'
    ok.append((have - set(imports_of(allp2))) == set())
    # ### (iii) a module with NO target is not counted against the certification file.
    ok.append('B' not in have)
    # ### (iv) the parsers find what they should and nothing else.
    ok.append(PRINT.findall('#print axioms Foo.bar\n  #print axioms Not.this\n') == ['Foo.bar'])
    ok.append(IMPORT.findall('import X\n-- import Y\n') == ['X'])
    return all(ok), ok


def main(argv):
    print('=' * 100)
    print('b315_coverage_gate.py -- THE KERNEL-COVERAGE GATE. ### **IT IS SUPPOSED TO FAIL.**')
    print('=' * 100)
    good, arms = self_test()
    print('  ### THE GATE\'S OWN FIXTURES, RUN BEFORE IT READS THE KERNEL : %s  %s'
          % (arms, 'PASS' if good else '### FAIL ###'))
    print('  ### **ARM (ii) IS THE ONE THAT MATTERS: THE GATE MUST BE ABLE TO PASS.** ### A gate')
    print('  ### that cannot come back clean is not reporting a defect, it is reporting itself.')
    if not good:
        return 2

    core = sorted(os.path.splitext(f)[0] for f in os.listdir(CORE) if f.endswith('.lean'))
    allp = read(ALLP)
    imported = set(imports_of(allp))
    prof = read(PROFILE)
    certified = set(re.findall(r"^'([^']+)'", prof, re.M))

    with_targets, rows = set(), []
    for m in core:
        txt = read(os.path.join(CORE, m + '.lean'))
        tg, ns, op = targets_of(txt)
        if not tg:
            continue
        with_targets.add(m)
        uncov = []
        for name in tg:
            cands = {name} | {p + '.' + name for p in (ns + op)}
            if not (cands & certified):
                uncov.append(name)
        rows.append((m, len(tg), len(uncov), m in imported))

    outside_all = [m for m in core if m not in imported]
    missing = sorted(with_targets - imported)
    uncertified = sum(u for _m, _t, u, inc in rows if not inc for u in [u])

    print()
    print('  Core modules on disk                         : %d' % len(core))
    print('  Core modules carrying a `#print axioms` target: %d' % len(with_targets))
    print('  modules the certification file imports        : %d' % len(imported))
    print('  ### modules OUTSIDE the certification file    : %d' % len(outside_all))
    print('  ### **MODULES WITH A PRINT TARGET AND NOT IMPORTED : %d**' % len(missing))
    print('  ### **PRINT TARGETS NOT IN THE PROFILE            : %d**' % uncertified)
    print()
    print('  ### THE TWO COUNTS ARE DIFFERENT AND BOTH ARE PRINTED:')
    only = sorted(set(outside_all) - with_targets)
    print('    outside but carrying NO target of its own : %s' % (only or 'NONE'))
    print('    ### -- its terminals are printed by a separate checker, which is itself outside.')
    print()
    print('  ### THE MODULES THE GATE SEES:')
    for m, tg, uncov, inc in rows:
        if inc:
            continue
        print('    %-30s targets=%-3d not-in-profile=%-3d' % (m, tg, uncov))

    print()
    if missing:
        print('  ### ### **GATE FAILS. ### %d MODULE(S) CARRY A TERMINAL THE CERTIFICATION FILE'
              ' NEVER PRINTS.**' % len(missing))
        print('  ### **AND IT IS SUPPOSED TO FAIL TODAY.** ### The order asks for the check to be')
        print('  ### WRITTEN AND RUN, reporting what it now sees, ### **WITH NOTHING REPAIRED.**')
        print('  ### No module is added to `AllPrints.lean`; no `.lean` file is touched; the')
        print('  ### profile does not move. ### **THE REPAIR IS A BUILD, UNDER ITS OWN')
        print('  ### REGISTRATION, AND IT MUST DECIDE MODULE BY MODULE WHETHER A TERMINAL BELONGS')
        print('  ### IN THE PROFILE RATHER THAN ADDING IMPORTS AND RE-RUNNING.**')
    else:
        print('  ### GATE PASSES -- every module carrying a print target is imported.')
    print('  ### ### **WHAT THE GATE CANNOT DO, IN ITS OWN OUTPUT SO IT IS NOT TRUSTED BEYOND IT:**')
    print('  ### it cannot tell whether a terminal is WORTH certifying. ### It compares two sets of')
    print('  ### names. ### **A TERMINAL THAT ELABORATES WITH ZERO AXIOMS IS NOT THEREBY A')
    print('  ### TERMINAL WORTH CERTIFYING**, and that judgement is the author\'s, not a set')
    print('  ### difference\'s.')
    print('=' * 100)
    return 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
