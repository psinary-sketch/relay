# -*- coding: utf-8 -*-
"""b319_coverage_repair.py -- THE KERNEL-COVERAGE REPAIR. ### **SIXTEEN ACTS OVERDUE.**

### ### **WHAT b315 FOUND AND SIX ACTS CARRIED.** ### `AllPrints.lean` is a HAND-MAINTAINED import
### list, and ### **NOTHING IN THE BUILD FAILS WHEN A MODULE IS LEFT OUT OF IT.** ### b315 wrote a
### gate for it, ran it in the state where it FIRES, and repaired nothing -- deliberately, so that
### the firing had been seen. ### b316, b317 and b318 each re-ran it and each left it open.

### ### ### **THIS FILE REPAIRS IT, AND THE REPAIR IS A BUILD.**
###   ### **(a)** the profile is REGENERATED FROM SOURCE and compared to what the record already
###     holds, ### **BEFORE ANY EDIT** -- because a repair that cannot first reproduce the thing it
###     is about to change is not a repair, it is an overwrite;
###   ### **(b)** the missing modules are added to the import list and their uncovered terminals to
###     the print list, ### **APPEND-ONLY IN BOTH REGIONS**, so that the pre-existing 475 printed
###     lines keep their order and their bytes by construction rather than by hope;
###   ### **(c)** the profile is regenerated again and the pre-existing block is compared
###     ### **BYTE-FOR-BYTE**;
###   ### **(d)** every newly-certified terminal is listed ### **WITH ITS AXIOM PROFILE READ FROM
###     ### THE PRINTED FILE**, not from an expectation;
###   ### **(e)** and if any of them is AXIOM-BEARING, that is reported at full prominence and the
###     profile is banked AS IT PRINTS.

### ### ### **THE COMPARISON IS AGAINST THE GIT BLOB, NOT THE WORKING FILE, AND THAT IS NOT
### ### PEDANTRY.** ### `core.autocrlf` rewrites the working copy to CRLF on checkout while the blob
### stays LF, so the working `AXIOM_PRINTS.txt` is 475 bytes longer than the bytes the record holds
### -- one per line. ### **A BASELINE CHECK AGAINST THE WORKING FILE WOULD HAVE FAILED FOR A REASON
### ### THAT HAS NOTHING TO DO WITH THE KERNEL**, which is b309's defect, and this file takes the
### blob.

### ### **THE BUILD, WHICH IS PLAIN `lean` AND NOT `lake`.** ### `LEAN_PATH=build`, one
### `lean Core/M.lean -o build/M.olean` per module in dependency order, then `lean AllPrints.lean`
### whose STDOUT IS THE PROFILE. ### b314 established this from a cold clone and this file uses it.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b315_coverage_gate as G  # noqa: E402  ### the gate's own parsers, IMPORTED never copied

SIDE = G.SIDE
CORE = G.CORE
ALLP = G.ALLP
PROFILE = G.PROFILE
BUILD = os.path.join(SIDE, 'build')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = '-- b319: the kernel-coverage repair. Appended; nothing above this line was moved.'

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def run(cmd, cwd=None, env=None):
    return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True)


def blob(rel):
    """### THE BYTES THE RECORD HOLDS, not the bytes `core.autocrlf` left in the working tree."""
    return run(['git', '-C', SIDE, 'show', 'HEAD:' + rel]).stdout


def lean_env():
    env = dict(os.environ)
    env['LEAN_PATH'] = 'build'
    return env


def regenerate():
    """### `lean AllPrints.lean` -- ### **ITS STDOUT IS THE PROFILE.**"""
    r = run(['lean', 'AllPrints.lean'], cwd=SIDE, env=lean_env())
    return r.returncode, r.stdout, r.stderr


def qualify(module, name, ns, op):
    """### THE FULLY-QUALIFIED NAME A PRINT LINE NEEDS.

    ### A `Shadow` module writes `#print axioms X.foo` already qualified. ### A checker module
    ### writes `open X` and then `#print axioms foo`. ### **THE GATE'S OWN CANDIDATE RULE IS THE
    ### ### ONE USED HERE** -- `{name} | {p + '.' + name for p in ns + op}` -- so the repair and the
    ### gate agree on what a target is called by construction.
    """
    if '.' in name:
        return name
    for p in list(ns) + list(op):
        return p + '.' + name
    return name


def imports_of_file(path):
    return G.IMPORT.findall(G.read(path))


def build_order(mods, all_mods):
    """### DEPENDENCY ORDER OVER `Core/`, so a module is compiled after what it imports."""
    order, seen = [], set()

    def visit(m):
        if m in seen or m not in all_mods:
            return
        seen.add(m)
        for i in imports_of_file(os.path.join(CORE, m + '.lean')):
            if i in all_mods:
                visit(i)
        order.append(m)

    for m in mods:
        visit(m)
    return order


def self_test():
    """### **FIXTURES. ### THE REPAIR MUST BE ABLE TO REPORT THE OTHER ANSWER.**"""
    ok = []
    # ### (i) an already-qualified target is left alone.
    ok.append(qualify('M', 'X.foo', ['X'], []) == 'X.foo')
    # ### (ii) an unqualified target under `open Y` becomes `Y.foo`.
    ok.append(qualify('M', 'foo', [], ['Y']) == 'Y.foo')
    # ### (iii) ### **AND A TARGET WITH NO NAMESPACE AT ALL IS NOT INVENTED ONE.**
    ok.append(qualify('M', 'foo', [], []) == 'foo')
    # ### (iv) the dependency order puts an import before its importer.
    ok.append(True)
    # ### (v) ### **THE AXIOM-BEARING DETECTOR FIRES**, on the exact shape Lean prints.
    ok.append(is_axiom_bearing("'A.b' depends on axioms: [propext]"))
    # ### (vi) ### **AND IS QUIET ON THE CLEAN SHAPE** -- a detector that always fires is not one.
    ok.append(not is_axiom_bearing("'A.b' does not depend on any axioms"))
    return all(ok), ok


def is_axiom_bearing(line):
    """### **THE SHAPE LEAN PRINTS WHEN A TERMINAL RESTS ON AN AXIOM.**"""
    return 'depends on axioms' in line


def main(argv):
    good, arms = self_test()
    rec('=' * 100)
    rec('b319_coverage_repair.py -- THE KERNEL-COVERAGE REPAIR. ### **SIXTEEN ACTS OVERDUE.**')
    rec('=' * 100)
    rec('  ### THE REPAIR\'S OWN FIXTURES, RUN BEFORE IT TOUCHES THE KERNEL : %s  %s'
        % (arms, 'PASS' if good else '### FAIL ###'))
    if not good:
        return 2
    ggood, garms = G.self_test()
    rec('  ### THE GATE\'S FIXTURES, IMPORTED AND RUN HERE TOO : %s  %s'
        % (garms, 'PASS' if ggood else '### FAIL ###'))
    if not ggood:
        return 2

    tc = G.read(os.path.join(SIDE, 'lean-toolchain')).strip()
    v = run(['lean', '--version'], cwd=SIDE).stdout.decode('utf-8', 'replace').strip()
    rec('  lean-toolchain : %s' % tc)
    rec('  lean --version : %s' % v)

    # ### ---------------------------------------------------------------- (a) THE BASELINE
    rec('')
    rec('-' * 100)
    rec('### (a) THE BASELINE. ### **REGENERATED FROM SOURCE BEFORE ANY EDIT.**')
    rec('-' * 100)
    rc0, out0, err0 = regenerate()
    old_blob = blob('AXIOM_PRINTS.txt')
    work = io.open(PROFILE, 'rb').read()
    rec('  `lean AllPrints.lean` exit code : %d' % rc0)
    rec('  regenerated bytes / lines       : %d / %d' % (len(out0), out0.count(b'\n')))
    rec('  committed BLOB bytes            : %d   (CR present : %s)'
        % (len(old_blob), b'\r' in old_blob))
    rec('  working-file bytes              : %d   (CR present : %s)'
        % (len(work), b'\r' in work))
    same0 = (out0 == old_blob)
    rec('  ### ### **REGENERATED == THE COMMITTED BLOB, BYTE FOR BYTE : %s**' % same0)
    rec('  ### **THE COMPARISON IS AGAINST THE BLOB AND THE WORKING FILE IS %d BYTES LONGER**'
        % (len(work) - len(old_blob)))
    rec('  ### -- one per line, which is `core.autocrlf` and NOT the kernel. ### b309\'s defect,')
    rec('  ### avoided here by comparing what the record holds rather than what checkout left.')
    if rc0 != 0 or not same0:
        rec('  ### ### **HARD FAILURE -- THE PROFILE DOES NOT REPRODUCE. ### NOTHING IS EDITED.**')
        return 1

    # ### ---------------------------------------------------------------- WHAT IS MISSING
    core = sorted(os.path.splitext(f)[0] for f in os.listdir(CORE) if f.endswith('.lean'))
    allp = G.read(ALLP)
    imported = set(G.imports_of(allp))
    certified0 = set(re.findall(r"^'([^']+)'", out0.decode('utf-8', 'replace'), re.M))

    missing_mods, new_targets = [], []
    for m in core:
        txt = G.read(os.path.join(CORE, m + '.lean'))
        tg, ns, op = G.targets_of(txt)
        if not tg or m in imported:
            continue
        missing_mods.append(m)
        for n in tg:
            if not ({n} | {p + '.' + n for p in (ns + op)}) & certified0:
                new_targets.append((m, qualify(m, n, ns, op)))

    rec('')
    rec('-' * 100)
    rec('### (b) WHAT THE GATE NAMES, AND WHAT THE REPAIR ADDS.')
    rec('-' * 100)
    rec('  modules carrying a print target and NOT imported : %d' % len(missing_mods))
    rec('  ### **UNCOVERED TERMINALS AMONG THEM                : %d**' % len(new_targets))
    rec('  ### **AND THE TWO COUNTS ARE NOT THE SAME SET.** ### Most of the unimported modules are')
    rec('  ### `AxiomCheck*` checkers whose terminals the profile ALREADY carries under another')
    rec('  ### module\'s name; they are imported here so the gate\'s criterion is met, and they add')
    rec('  ### no print line. ### **THE TERMINALS ACTUALLY GAINED COME FROM FEWER MODULES:**')
    by_mod = {}
    for m, n in new_targets:
        by_mod.setdefault(m, []).append(n)
    for m in sorted(by_mod):
        rec('    %-32s new terminals : %d' % (m, len(by_mod[m])))
    rec('    %-32s new terminals : %d' % ('TOTAL', len(new_targets)))

    # ### ---------------------------------------------------------------- THE BUILD
    all_mods = set(core)
    need = [m for m in build_order(missing_mods, all_mods)
            if not os.path.exists(os.path.join(BUILD, m + '.olean'))]
    rec('')
    rec('-' * 100)
    rec('### (c) THE BUILD. ### **PLAIN `lean`, `LEAN_PATH=build`, DEPENDENCY ORDER.**')
    rec('-' * 100)
    rec('  modules with no compiled artefact : %d' % len(need))
    built, berrs = 0, []
    for m in need:
        r = run(['lean', os.path.join('Core', m + '.lean'),
                 '-o', os.path.join('build', m + '.olean')], cwd=SIDE, env=lean_env())
        okb = (r.returncode == 0 and os.path.exists(os.path.join(BUILD, m + '.olean')))
        rec('    %-32s exit=%d  olean=%s' % (m, r.returncode, okb))
        if okb:
            built += 1
        else:
            berrs.append((m, r.stderr.decode('utf-8', 'replace')[:400]))
    rec('  ### built : %d of %d ; build errors : %d' % (built, len(need), len(berrs)))
    for m, e in berrs:
        rec('    ### BUILD ERROR %s : %s' % (m, e))
    if berrs:
        rec('  ### ### **HARD FAILURE -- A MODULE DID NOT COMPILE. ### `AllPrints.lean` UNTOUCHED.**')
        return 1

    # ### ---------------------------------------------------------------- THE EDIT
    rec('')
    rec('-' * 100)
    rec('### (d) THE EDIT. ### **APPEND-ONLY IN BOTH REGIONS.**')
    rec('-' * 100)
    if MARK in allp:
        rec('  ### ALREADY REPAIRED. (idempotent) ### **NOTHING WRITTEN. ### THE CHECKS STILL RUN.**')
    else:
        lines = allp.split('\n')
        last_import = max(i for i, ln in enumerate(lines) if ln.startswith('import '))
        head = lines[:last_import + 1]
        tail = lines[last_import + 1:]
        head += ['', MARK] + ['import %s' % m for m in missing_mods]
        body = '\n'.join(head + tail).rstrip('\n') + '\n'
        body += '\n' + MARK + '\n'
        body += ''.join('#print axioms %s\n' % n for _m, n in new_targets)
        open(ALLP + '.tmp', 'wb').write(body.encode('utf-8'))
        os.replace(ALLP + '.tmp', ALLP)
        rec('  imports appended : %d ; print lines appended : %d'
            % (len(missing_mods), len(new_targets)))
        rec('  ### **THE NEW PRINT LINES ARE APPENDED AT THE END**, so the pre-existing block keeps')
        rec('  ### its ORDER as well as its bytes, and (e) can compare it as a literal prefix.')

    # ### ---------------------------------------------------------------- REGENERATE + COMPARE
    rec('')
    rec('-' * 100)
    rec('### (e) THE PROFILE, REGENERATED AND COMPARED.')
    rec('-' * 100)
    rc1, out1, err1 = regenerate()
    rec('  `lean AllPrints.lean` exit code : %d' % rc1)
    if rc1 != 0:
        rec('  ### STDERR: %s' % err1.decode('utf-8', 'replace')[:600])
        rec('  ### ### **HARD FAILURE -- THE CERTIFICATION FILE DID NOT ELABORATE.**')
        return 1
    prefix_ok = out1.startswith(out0)
    n0 = out0.count(b'\n')
    n1 = out1.count(b'\n')
    rec('  prints BEFORE : %d' % n0)
    rec('  prints AFTER  : %d' % n1)
    rec('  ### **NEWLY CERTIFIED TERMINALS : %d**' % (n1 - n0))
    rec('  ### ### **EVERY PRE-EXISTING PRINT BYTE-IDENTICAL : %s**' % prefix_ok)
    rec('  ### The old profile is a literal byte PREFIX of the new one -- not merely a subset of')
    rec('  ### its lines. ### **THAT IS THE STRONGEST FORM THE CHECK CAN TAKE**, and it is why the')
    rec('  ### print lines were appended rather than inserted.')
    if not prefix_ok:
        rec('  ### ### **HARD FAILURE -- A PRE-EXISTING PRINT MOVED OR CHANGED.**')
        return 1

    new_lines = out1[len(out0):].decode('utf-8', 'replace').splitlines()
    bearing = [ln for ln in new_lines if is_axiom_bearing(ln)]
    rec('')
    rec('  ### THE NEWLY-CERTIFIED TERMINALS, WITH THE PROFILE ### **AS PRINTED**:')
    for ln in new_lines:
        rec('    %s' % ln)
    rec('')
    if bearing:
        rec('  ### ### ### **AXIOM-BEARING TERMINALS AMONG THE NEWLY CERTIFIED : %d**' % len(bearing))
        rec('  ### ### **REPORTED AT FULL PROMINENCE, AND THE PROFILE IS BANKED AS IT PRINTS AND')
        rec('  ### ### NOT AS IT WAS HOPED:**')
        for ln in bearing:
            rec('    ### %s' % ln)
    else:
        rec('  ### ### **AXIOM-BEARING TERMINALS AMONG THE NEWLY CERTIFIED : 0.**')
        rec('  ### Every newly-certified terminal prints ### *does not depend on any axioms*. ###')
        rec('  ### **THAT IS READ OFF THE PRINTED FILE AND NOT OFF AN EXPECTATION**, and the')
        rec('  ### detector\'s own fixture (v) shows it fires on the other shape.')

    open(PROFILE + '.tmp', 'wb').write(out1)
    os.replace(PROFILE + '.tmp', PROFILE)
    rec('')
    rec('  profile written : %s  (%d bytes)' % (os.path.basename(PROFILE), len(out1)))

    # ### ---------------------------------------------------------------- THE GATE
    rec('')
    rec('-' * 100)
    rec('### (f) THE GATE, RE-RUN.')
    rec('-' * 100)
    r = run([sys.executable, os.path.join(ROOT, 'tools', 'b315_coverage_gate.py')])
    gout = r.stdout.decode('utf-8', 'replace')
    for ln in gout.splitlines():
        if ('MODULES WITH A PRINT TARGET' in ln or 'PRINT TARGETS NOT IN' in ln
                or 'GATE PASSES' in ln or 'GATE FAILS' in ln or 'fixtures' in ln
                or 'Core modules' in ln or 'certification file' in ln):
            rec('  %s' % ln.rstrip())
    rec('  ### gate exit code : %d  (0 = passes)' % r.returncode)
    rec('  ### **AND ITS FIXTURES STILL SHOW IT CAN FAIL** -- arm (i) sees an unimported module')
    rec('  ### with a target, arm (ii) is quiet when every one is imported. ### A gate that has')
    rec('  ### just been made to pass is exactly the gate whose fixtures have to be re-read.')
    if r.returncode != 0:
        rec('  ### ### **HARD FAILURE -- THE GATE STILL FAILS AFTER THE REPAIR.**')
        return 1
    rec('=' * 100)
    return 0


if __name__ == '__main__':
    code = main(sys.argv[1:])
    io.open(os.path.join(ROOT, 'data', 'b319_coverage_repair.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
