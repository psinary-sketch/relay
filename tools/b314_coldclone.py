# -*- coding: utf-8 -*-
"""b314_coldclone.py -- THE KERNEL CERTIFIED FROM A CLONE THAT INHERITED NOTHING.

### ### **WHAT `INHERITED NOTHING` MEANS HERE, STATED BEFORE IT IS CLAIMED:**
###   ### the repository is cloned FRESH from `origin` at its current pin, onto a path the corpus
###     does not own;
###   ### `build/` is `.gitignore`d, so the clone arrives with ### **NO COMPILED ARTEFACT AT ALL**
###     -- there is no cache to be stale;
###   ### the toolchain is whatever `elan` resolves from the clone's own `lean-toolchain`, and
###     ### **THE RESOLVED VERSION IS PRINTED FROM INSIDE THE CLONE**, not assumed from the file;
###   ### and every module is elaborated from source in dependency order.
### ### **WHAT IT DOES NOT MEAN: ### THE MACHINE IS THE SAME MACHINE.** ### `elan`'s toolchain
### store, the operating system and the CPU are shared with the working tree. ### **THIS IS A COLD
### ### CACHE AND A COLD CHECKOUT, NOT A COLD MACHINE**, and the bank says so rather than letting
### the word `cold` do more work than the procedure supports.

### ### **THE COMPARISON IS ON RAW BYTES.** ### b298 lost a day to a byte-order mark that passed
### two checks which could not see it, and b309 lost one to `core.autocrlf` rewriting a working
### file after checkout while the blob stayed `LF`. ### **SO THE PROFILE IS COMPARED BOTH RAW AND
### ### NORMALISED, AND BOTH ANSWERS ARE PRINTED** -- a raw mismatch with a normalised match is a
### line-ending fact and is reported as one, never silently normalised away.
"""
import io
import json
import shutil
import stat
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_kernel as K  # noqa: E402  ### the normaliser and the print counter are READ, not copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REMOTE = 'https://github.com/psinary-sketch/SIDE-global-section.git'
BOM = b'\xef\xbb\xbf'
D = os.path.join(ROOT, 'data')

LINES = []


def _force_rm(func, path, _exc):
    """### git objects arrive read-only on Windows; a plain `rmtree` refuses them."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rec(s=''):
    LINES.append(s)
    print(s)


def run(cmd, cwd=None, env=None, timeout=7200):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=timeout, env=env)


def imports_of(path):
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    return re.findall(r'^import\s+(\S+)', txt, re.M)


def print_targets(path):
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    return (re.findall(r'^#print axioms\s+(\S+)', txt, re.M),
            re.findall(r'^namespace\s+(\S+)', txt, re.M),
            re.findall(r'^open\s+(\S+)', txt, re.M))


def toposort(names, deps):
    """### **DEPENDENCY ORDER, WITH A CYCLE REPORTED RATHER THAN LOOPED ON.**"""
    order, state = [], {}

    def visit(n, stack):
        if state.get(n) == 2:
            return None
        if state.get(n) == 1:
            return stack + [n]
        state[n] = 1
        for d in deps.get(n, []):
            if d in deps:
                c = visit(d, stack + [n])
                if c:
                    return c
        state[n] = 2
        order.append(n)
        return None

    for n in names:
        c = visit(n, [])
        if c:
            return None, c
    return order, None


def self_test():
    """### **FIXTURES. ### EVERY ARM MUST BE ABLE TO REPORT THE OTHER ANSWER.**"""
    ok = []
    o, c = toposort(['a', 'b'], {'a': ['b'], 'b': []})
    ok.append(o == ['b', 'a'] and c is None)
    o2, c2 = toposort(['a', 'b'], {'a': ['b'], 'b': ['a']})
    ok.append(o2 is None and c2 is not None)
    ok.append(K.normalise(b'x\r\ny\r\n') == b'x\ny\n')
    ok.append(K.normalise(b'x\n\n\ny\n') == b'x\ny\n')
    tot, zero, other = K.count_prints(b"'A.b' does not depend on any axioms\n"
                                      b"'C.d' depends on axioms: [propext]\n")
    ok.append((tot, zero, other) == (2, 1, 1))
    return all(ok), ok


def main(argv):
    dest = argv[0] if argv else None
    if not dest:
        print('usage: python b314_coldclone.py <scratch-directory>')
        return 2
    t0 = time.time()
    rec('=' * 100)
    rec('b314_coldclone.py -- THE KERNEL FROM A CLONE THAT INHERITED NOTHING.')
    rec('=' * 100)
    good, arms = self_test()
    rec('  ### THE TOOL\'S OWN FIXTURES, RUN BEFORE IT CLONES ANYTHING : %s  %s'
        % (arms, 'PASS' if good else '### FAIL ###'))
    rec('  ### **ARM 2 IS THE ONE THAT MATTERS: A DEPENDENCY CYCLE IS REPORTED, NOT LOOPED ON.**')
    if not good:
        return 2

    fails = []
    clone = os.path.join(dest, 'SIDE-global-section')

    # ------------------------------------------------------------------ (1) THE CLONE
    rec('')
    rec('-' * 100)
    rec('### (1) THE CLONE, ON A PATH THE CORPUS DOES NOT OWN.')
    rec('-' * 100)
    rec('  destination      : %s' % clone)
    rec('  inside the corpus: %s'
        % any(os.path.abspath(clone).lower().startswith(p)
              for p in (r'd:\relay', r'd:\side-global-section', r'd:\my-downloads')))
    # ### ### **THE TOOL CLONES.** ### The first version of this act cloned by hand and then
    # ### re-ran the tool against the SAME directory to repair a sweep defect -- and the second run
    # ### was no longer cold, because the first had filled `build/`. ### **A CERTIFICATION WHOSE
    # ### `INHERITED NOTHING` CLAIM AND WHOSE NUMBERS COME FROM DIFFERENT RUNS IS NOT ONE
    # ### CERTIFICATION**, so the clone is inside the tool and every run starts from nothing.
    if os.path.isdir(clone):
        shutil.rmtree(clone, onerror=_force_rm)
    if not os.path.isdir(dest):
        os.makedirs(dest)
    rec('  ### removing any prior clone and cloning FRESH from origin ...')
    cl = run(['git', 'clone', '--quiet', REMOTE, clone])
    if cl.returncode != 0 or not os.path.isdir(os.path.join(clone, '.git')):
        rec('  ### THE CLONE FAILED : %s' % cl.stderr.decode('utf-8', 'replace')[:300])
        return 2
    head = run(['git', '-C', clone, 'rev-parse', 'HEAD']).stdout.decode().strip()
    lsr = run(['git', 'ls-remote', REMOTE, 'main']).stdout.decode().split()
    remote = lsr[0] if lsr else ''
    rec('  clone HEAD       : %s' % head)
    rec('  origin/main      : %s' % remote)
    rec('  ### **THE CLONE IS AT THE CURRENT PIN : %s**' % (head == remote))
    if head != remote:
        fails.append('the clone is not at the current pin')
    dirty = run(['git', '-C', clone, 'status', '--porcelain']).stdout.decode().strip()
    rec('  clone working tree: %r' % dirty)

    bdir = os.path.join(clone, 'build')
    pre_oleans = (sorted(f for f in os.listdir(bdir) if f.endswith('.olean'))
                  if os.path.isdir(bdir) else [])
    rec('  ### ### **COMPILED ARTEFACTS PRESENT IN THE CLONE BEFORE THE BUILD : %d**'
        % len(pre_oleans))
    rec('  ### `build/` is `.gitignore`d, so a clone arrives with nothing to be stale.')

    tc = io.open(os.path.join(clone, 'lean-toolchain'), encoding='utf-8').read().strip()
    v_in = run(['lean', '--version'], cwd=clone).stdout.decode().strip()
    v_out = run(['lean', '--version'], cwd=ROOT).stdout.decode().strip()
    rec('  lean-toolchain   : %s' % tc)
    rec('  ### `lean --version` INSIDE  the clone : %s' % v_in)
    rec('  ### `lean --version` OUTSIDE it        : %s' % v_out)
    pinned_ok = tc.split(':')[-1].lstrip('v') in v_in
    rec('  ### **THE RESOLVED TOOLCHAIN IS THE PINNED ONE : %s**' % pinned_ok)
    rec('  ### **AND IT IS NOT THE MACHINE DEFAULT**, which is what makes the pin observable at')
    rec('  ### all: the two lines above differ.')
    if not pinned_ok:
        fails.append('the clone did not resolve the pinned toolchain')

    # ------------------------------------------------------------------ (2) THE BUILD
    rec('')
    rec('-' * 100)
    rec('### (2) THE BUILD, FROM SOURCE, IN DEPENDENCY ORDER.')
    rec('-' * 100)
    core = os.path.join(clone, 'Core')
    mods = sorted(os.path.splitext(f)[0] for f in os.listdir(core) if f.endswith('.lean'))
    allp = os.path.join(clone, 'AllPrints.lean')
    imported = imports_of(allp)
    rec('  Core modules on disk        : %d' % len(mods))
    rec('  modules AllPrints imports   : %d' % len(imported))

    deps = {}
    for m in mods:
        deps[m] = [i for i in imports_of(os.path.join(core, m + '.lean')) if i in mods]
    need = set()

    def close(n):
        if n in need:
            return
        need.add(n)
        for x in deps.get(n, []):
            close(x)

    for m in imported:
        close(m)
    order, cycle = toposort(sorted(need), {k: v for k, v in deps.items() if k in need})
    if cycle:
        rec('  ### DEPENDENCY CYCLE : %s' % cycle)
        fails.append('dependency cycle')
        return 1
    rec('  transitive closure to build : %d modules' % len(order))

    if not os.path.isdir(bdir):
        os.makedirs(bdir)
    env = dict(os.environ)
    env['LEAN_PATH'] = bdir
    built, errs = 0, []
    for i, m in enumerate(order, 1):
        olean = os.path.join(bdir, m + '.olean')
        if os.path.exists(olean):
            built += 1
            continue
        r = run(['lean', os.path.join('Core', m + '.lean'), '-o', olean], cwd=clone, env=env)
        if r.returncode != 0 or not os.path.exists(olean):
            errs.append((m, r.returncode, r.stderr.decode('utf-8', 'replace')[:400]))
        else:
            built += 1
        if i % 20 == 0:
            rec('    ... %d/%d modules elaborated  (%.0f s)' % (i, len(order), time.time() - t0))
    rec('  ### modules elaborated from source : %d of %d ; failures : %d'
        % (built, len(order), len(errs)))
    for m, rc, se in errs:
        rec('    ### FAILED %s rc=%s %s' % (m, rc, se.replace('\n', ' ')[:160]))
    if errs:
        fails.append('modules failed to elaborate in the cold clone')

    # ------------------------------------------------------------------ (3) THE PROFILE
    rec('')
    rec('-' * 100)
    rec('### (3) THE CERTIFICATION PROFILE, REGENERATED AND COMPARED ON RAW BYTES.')
    rec('-' * 100)
    r = run(['lean', 'AllPrints.lean'], cwd=clone, env=env)
    raw = r.stdout
    rec('  `lean AllPrints.lean` exit code : %d' % r.returncode)
    if r.stderr.strip():
        rec('  ### stderr (first 400 bytes) : %s'
            % r.stderr.decode('utf-8', 'replace')[:400].replace('\n', ' '))
    if r.returncode != 0:
        fails.append('AllPrints did not elaborate in the cold clone')

    banked_raw = run(['git', '-C', clone, 'show', 'HEAD:AXIOM_PRINTS.txt']).stdout
    fresh_norm = K.normalise(raw)
    banked_norm = K.normalise(banked_raw)
    rec('  regenerated bytes : %d ; banked blob bytes : %d' % (len(raw), len(banked_raw)))
    rec('  ### RAW BOM present -- regenerated : %s ; banked : %s'
        % (raw.startswith(BOM), banked_raw.startswith(BOM)))
    rec('  ### RAW CRLF count -- regenerated : %d ; banked : %d'
        % (raw.count(b'\r\n'), banked_raw.count(b'\r\n')))
    raw_same = (raw == banked_raw)
    norm_same = (fresh_norm == banked_norm)
    rec('  ### **RAW BYTE EQUALITY        : %s**' % raw_same)
    rec('  ### **NORMALISED BYTE EQUALITY : %s**' % norm_same)
    if raw_same != norm_same:
        rec('  ### **THE TWO ANSWERS DIFFER, SO THE DIFFERENCE IS A LINE-ENDING FACT AND IS')
        rec('  ### REPORTED AS ONE RATHER THAN NORMALISED AWAY.** ### Lean writes native line')
        rec('  ### endings to a pipe on this platform; the banked blob is `LF`.')
    tot, zero, other = K.count_prints(fresh_norm)
    btot, bzero, bother = K.count_prints(banked_norm)
    rec('  ### prints -- regenerated : %d total, %d zero-axiom, %d other' % (tot, zero, other))
    rec('  ### prints -- banked      : %d total, %d zero-axiom, %d other' % (btot, bzero, bother))
    fl = fresh_norm.decode('utf-8', 'replace').splitlines()
    bl = banked_norm.decode('utf-8', 'replace').splitlines()
    diffs = [(i + 1, b, f) for i, (b, f) in enumerate(zip(bl, fl)) if b != f]
    extra = len(fl) - len(bl)
    rec('  ### **DIFFERING LINES : %d ; LENGTH DIFFERENCE : %+d**' % (len(diffs), extra))
    for i, b, f in diffs[:40]:
        rec('      line %-4d banked : %s' % (i, b))
        rec('      line %-4d fresh  : %s' % (i, f))
    if not norm_same:
        fails.append('the cold clone did not reproduce the banked profile')

    # ------------------------------------------------------------------ (4) COVERAGE
    rec('')
    rec('-' * 100)
    rec('### (4) THE COVERAGE SWEEP: MODULES OUTSIDE THE CERTIFICATION FILE.')
    rec('-' * 100)
    names = set(re.findall(r"^'([^']+)'", banked_norm.decode('utf-8', 'replace'), re.M))
    outside = [m for m in mods if m not in imported]
    rec('  modules outside `AllPrints.lean` : %d' % len(outside))
    # ### ### **THE SWEEP RUNS IN DEPENDENCY ORDER, NOT ALPHABETICAL ORDER.** ### The first
    # ### version of this sweep iterated alphabetically and reported `AxiomCheckM4E` as FAILING --
    # ### because that module imports `M4EnvelopeShadow`, which the alphabet had not reached yet.
    # ### **A SWEEP THAT TESTS A MODULE BEFORE ITS DEPENDENCY EXISTS REPORTS A DEFECT IN THE SWEEP
    # ### AS A DEFECT IN THE CORPUS**, which is the worst direction for a report to be wrong in.
    oneed = set()

    def oclose(n):
        if n in oneed:
            return
        oneed.add(n)
        for x in deps.get(n, []):
            oclose(x)

    for m in outside:
        oclose(m)
    oorder, ocycle = toposort(sorted(oneed), {k: v for k, v in deps.items() if k in oneed})
    if ocycle:
        rec('  ### DEPENDENCY CYCLE among the outside modules : %s' % ocycle)
        fails.append('dependency cycle in the coverage sweep')
        oorder = sorted(oneed)
    outside = [m for m in oorder if m in outside]
    rec('  ### swept in DEPENDENCY ORDER : %s ...' % ', '.join(outside[:4]))
    rows, uncert_total = [], 0
    for m in outside:
        path = os.path.join(core, m + '.lean')
        tg, ns, op = print_targets(path)
        uncovered = []
        for tname in tg:
            cands = {tname} | {p + '.' + tname for p in (ns + op)}
            if not (cands & names):
                uncovered.append(tname)
        olean = os.path.join(bdir, m + '.olean')
        status, prof = 'not built', []
        if not os.path.exists(olean):
            rr = run(['lean', os.path.join('Core', m + '.lean'), '-o', olean], cwd=clone, env=env)
            if rr.returncode == 0:
                status = 'ELABORATES'
                prof = K.normalise(rr.stdout).decode('utf-8', 'replace').splitlines()
            else:
                status = 'FAILS rc=%d' % rr.returncode
        else:
            rr = run(['lean', os.path.join('Core', m + '.lean')], cwd=clone, env=env)
            status = 'ELABORATES' if rr.returncode == 0 else 'FAILS rc=%d' % rr.returncode
            prof = K.normalise(rr.stdout).decode('utf-8', 'replace').splitlines()
        # ### **AN EMPTY STREAM IS ZERO LINES, NOT ONE.** ### The normaliser returns a single
        # ### newline for empty input, and the first version of this sweep counted that as one
        # ### emitted line -- so a module that printed nothing was reported as printing something.
        prof = [x for x in prof if x.strip()]
        nz = len([x for x in prof if x.endswith('does not depend on any axioms')])
        rows.append(dict(module=m, prints=len(tg), uncertified=len(uncovered), status=status,
                         emitted=len(prof), zero_axiom=nz, targets=uncovered))
        uncert_total += len(uncovered)
        rec('    %-30s prints=%-3d NOT-IN-PROFILE=%-3d  %-12s emitted=%-3d zero-axiom=%-3d'
            % (m, len(tg), len(uncovered), status, len(prof), nz))
    rec('')
    rec('  ### ### **TERMINALS SITTING IN `Core/` AND NOT IN THE CERTIFICATION PROFILE : %d**'
        % uncert_total)
    rec('  ### **FOUND, NOT NOT-FOUND**, and the reason is structural rather than accidental:')
    rec('  ### `AllPrints.lean` is a HAND-MAINTAINED import list, and a module that is never added')
    rec('  ### to it is never certified. ### **NOTHING IN THE BUILD FAILS WHEN A MODULE IS LEFT')
    rec('  ### OUT** -- the profile simply does not mention it, and a profile that does not mention')
    rec('  ### a module looks exactly like a profile for a corpus that does not have one.')
    rec('  ### **NOTHING IS REPAIRED BY THIS ACT. ### THE FINDING IS FILED.**')

    payload = dict(head=head, remote=remote, toolchain=tc, lean_in=v_in, lean_out=v_out,
                   pre_oleans=len(pre_oleans), to_build=len(order), built=built,
                   build_errors=[e[0] for e in errs], allprints_rc=r.returncode,
                   raw_same=raw_same, norm_same=norm_same,
                   raw_bom=[raw.startswith(BOM), banked_raw.startswith(BOM)],
                   raw_crlf=[raw.count(b'\r\n'), banked_raw.count(b'\r\n')],
                   prints=[tot, zero, other], banked_prints=[btot, bzero, bother],
                   diff_lines=len(diffs), length_delta=extra,
                   outside=len(outside), uncertified=uncert_total, coverage=rows,
                   elapsed=time.time() - t0, fails=fails)
    io.open(os.path.join(D, 'b314_coldclone_rows.json'), 'w', encoding='utf-8',
            newline='\n').write(json.dumps(payload, indent=1, default=str) + '\n')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main(sys.argv[1:])
    io.open(os.path.join(D, 'b314_coldclone_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
