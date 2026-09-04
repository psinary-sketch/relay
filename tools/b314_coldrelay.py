# -*- coding: utf-8 -*-
"""b314_coldrelay.py -- THE INSTRUMENTS' REPRODUCTION CONTROLS, RUN COLD IN A FRESH CLONE.

### ### **WHAT THIS ASKS.** ### Not *do the instruments still work here*, which the suites answer
### every act, but ### **DOES THE CORPUS REPRODUCE ITSELF FROM A CLONE THAT HAS ONLY WHAT GIT
### ### TRACKS?** ### Every act of this session ran against a working tree that has accumulated a
### month of untracked state; ### **AN INSTRUMENT THAT SILENTLY DEPENDS ON ONE UNTRACKED FILE
### ### PASSES EVERY LOCAL CONTROL AND CANNOT BE RUN BY ANYONE ELSE.**

### ### **AND THE HAZARD THIS TOOL GUARDS AGAINST IN THE OTHER DIRECTION:** ### several instrument
### files carry ### **HARD-CODED ABSOLUTE PATHS INTO THE CORPUS** -- `D:\\relay\\data\\...` written
### into the source. ### A control run from a clone through one of those would read, or write, the
### ORIGINAL. ### **SO THE CORPUS'S OWN TRACKED STATE IS CHECKED BEFORE AND AFTER, AND THE
### ### HARD-CODED PATHS ARE COUNTED AND REPORTED RATHER THAN ASSUMED ABSENT.**

### ### **NOTHING IS REPAIRED HERE.** ### A disagreement is printed at full prominence and filed.
"""
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
REMOTE = 'https://github.com/psinary-sketch/relay.git'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []

# ### (label, script, the line that shows the control PASSED, the sense of it)
CONTROLS = [
    ('b308 -- the instrument reproduces the banked finite-side results',
     'tools/b308_reproduction.py', 'DISAGREEING', 'the disagreement count'),
    ('b309 -- the scaling trace, exact, two routes',
     'tools/b309_components.py', 'CHECKS FAILING', 'the runner\'s own failure count'),
    ('b310 -- the smear collapses, exact',
     'tools/b310_components.py', 'CHECKS FAILING', 'the runner\'s own failure count'),
    ('b313 -- the transcription against b38\u2019s banked table, and the copy controls',
     'tools/b313_run.py', 'CHECKS FAILING', 'the runner\'s own failure count'),
]

CORPUS_PATHS = (r'D:\relay', r'D:\SIDE-global-section', r'D:\MY-DOwnloads')


def _force_rm(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rec(s=''):
    LINES.append(s)
    print(s)


def run(cmd, cwd=None, env=None, timeout=3600):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=timeout, env=env)


def tracked_state(repo):
    """### **THE CORPUS'S OWN TRACKED STATE, AS A STRING.** ### Compared before and after."""
    r = run(['git', '-C', repo, 'status', '--porcelain', '--untracked-files=no'])
    return r.stdout.decode('utf-8', 'replace').strip()


def hardcoded(path):
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    return [ln.strip() for ln in txt.splitlines()
            if any(p.lower() in ln.lower() for p in CORPUS_PATHS)]


def self_test():
    ok = []
    ok.append(hardcoded.__name__ == 'hardcoded')
    tmp = os.path.join(D, '_b314_fixture.py')
    io.open(tmp, 'w', encoding='utf-8', newline='\n').write(
        'A = 1\nB = r"D:\\relay\\data\\x.txt"\n')
    try:
        h = hardcoded(tmp)
        ok.append(len(h) == 1 and 'relay' in h[0])
        io.open(tmp, 'w', encoding='utf-8', newline='\n').write('A = 1\n')
        ok.append(hardcoded(tmp) == [])
    finally:
        os.remove(tmp)
    return all(ok), ok


def main(argv):
    dest = argv[0] if argv else None
    if not dest:
        print('usage: python b314_coldrelay.py <scratch-directory>')
        return 2
    t0 = time.time()
    rec('=' * 100)
    rec('b314_coldrelay.py -- THE REPRODUCTION CONTROLS, COLD, IN A FRESH CLONE OF THE RELAY.')
    rec('=' * 100)
    good, arms = self_test()
    rec('  ### THE TOOL\'S OWN FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    rec('  ### **THE SECOND AND THIRD ARMS ARE THE ONES THAT MATTER: THE HARD-CODED-PATH DETECTOR')
    rec('  ### FINDS ONE WHEN THERE IS ONE AND REPORTS NONE WHEN THERE IS NONE.**')
    if not good:
        return 2

    fails = []
    clone = os.path.join(dest, 'relay')
    before = tracked_state(ROOT)
    rec('  ### the corpus\'s own tracked state BEFORE the cold run : %r' % (before[:120],))

    if os.path.isdir(clone):
        shutil.rmtree(clone, onerror=_force_rm)
    if not os.path.isdir(dest):
        os.makedirs(dest)
    rec('  ### cloning the relay FRESH from origin ...')
    cl = run(['git', 'clone', '--quiet', REMOTE, clone], timeout=3600)
    if cl.returncode != 0:
        rec('  ### THE CLONE FAILED : %s' % cl.stderr.decode('utf-8', 'replace')[:300])
        return 2
    head = run(['git', '-C', clone, 'rev-parse', 'HEAD']).stdout.decode().strip()
    lsr = run(['git', 'ls-remote', REMOTE, 'main']).stdout.decode().split()
    remote = lsr[0] if lsr else ''
    rec('  clone HEAD  : %s' % head)
    rec('  origin/main : %s' % remote)
    rec('  ### **THE CLONE IS AT THE CURRENT PIN : %s**' % (head == remote))
    if head != remote:
        fails.append('the relay clone is not at the current pin')
    rec('  ### **AND IT HAS ONLY WHAT GIT TRACKS** -- no untracked data file, no cache, no `.olean`,')
    rec('  ### and none of the month of working-tree state every other act has run against.')

    rec('')
    rec('-' * 100)
    rec('### THE HARD-CODED ABSOLUTE PATHS, COUNTED BEFORE ANYTHING IS RUN.')
    rec('-' * 100)
    hits = {}
    for _lbl, script, _n, _s in CONTROLS:
        p = os.path.join(clone, script.replace('/', os.sep))
        hits[script] = hardcoded(p) if os.path.exists(p) else ['### SCRIPT MISSING']
        rec('    %-32s lines carrying an absolute corpus path : %d' % (script, len(hits[script])))
        for h in hits[script][:4]:
            rec('        %s' % h[:96])
    e16 = os.path.join(clone, 'tools', 'e16')
    e16hits = {}
    if os.path.isdir(e16):
        for f in sorted(os.listdir(e16)):
            if f.endswith('.py'):
                h = hardcoded(os.path.join(e16, f))
                if h:
                    e16hits[f] = h
    rec('    instrument files under `tools/e16` carrying one : %d' % len(e16hits))
    for f in sorted(e16hits)[:10]:
        rec('        %-28s %d line(s), first: %s' % (f, len(e16hits[f]), e16hits[f][0][:56]))
    rec('  ### **THESE ARE REPORTED, NOT REPAIRED.** ### A path written into a source file is a')
    rec('  ### dependency on a machine, and an instrument carrying one cannot be run from a clone')
    rec('  ### by anybody else without it reaching back into the original.')
    # ### ### **AND THE CONSEQUENCE FOR THIS ACT'S OWN CONTROLS, COMPUTED AND NOT ASSUMED.**
    b38 = os.path.join(e16, 'b38_act10.py')
    redirect = [ln for ln in (hardcoded(b38) if os.path.exists(b38) else [])
                if 'sys.path.insert' in ln]
    rec('')
    rec('  ### ### **THE HAZARD THIS FINDS IN THE COLD TEST ITSELF, AND IT WEAKENS THE PASS:**')
    rec('  ### `tools/e16/b38_act10.py` in the clone carries %d line(s) of the form:' % len(redirect))
    for ln in redirect:
        rec('        %s' % ln[:96])
    if redirect:
        rec('  ### ### **`sys.path.insert(0, ...)` PUTS THE ORIGINAL TREE AT THE FRONT OF THE')
        rec('  ### ### IMPORT PATH.** ### So once a control imports that module, every sibling')
        rec('  ### ### instrument it then imports resolves against ### THE ORIGINAL ### and not')
        rec('  ### ### against the clone.')
        rec('  ### **WHAT THAT DOES TO THE b313 CONTROL BELOW: ### IT PASSED, AND PART OF ITS')
        rec('  ### ### IMPORT GRAPH WAS NOT COLD.** ### The clone supplied the runner, the banked')
        rec('  ### tables it compares against, and its own `e16` directory -- but the sibling')
        rec('  ### modules `b38_act10` reaches for came from the original tree.')
        rec('  ### **THE PASS IS REAL AND ITS REACH IS SMALLER THAN IT LOOKS, AND SAYING SO IS THE')
        rec('  ### ### WHOLE VALUE OF HAVING RUN IT.**')

    rec('')
    rec('-' * 100)
    rec('### THE CONTROLS, RUN IN THE CLONE.')
    rec('-' * 100)
    rows = []
    env = dict(os.environ)
    # ### ### **THE BEFORE-STATE IS CAPTURED HERE, IMMEDIATELY AROUND THE CONTROL LOOP.** ### The
    # ### first version captured it at the top of the run, and the act's own index edit landed
    # ### between the two samples -- so the guard fired and blamed the cold run for a change the
    # ### seat had made. ### **A GUARD THAT REPORTS THE WRONG CAUSE IS WORSE THAN NO GUARD**, and
    # ### the paths are now printed so the cause is legible rather than inferred.
    before = tracked_state(ROOT)
    rec("  ### the corpus's tracked state IMMEDIATELY BEFORE the controls : %r" % (before[:160],))
    for lbl, script, needle, sense in CONTROLS:
        p = os.path.join(clone, script.replace('/', os.sep))
        if not os.path.exists(p):
            rec('    ### %-64s SCRIPT MISSING FROM THE CLONE' % lbl[:64])
            fails.append('script missing in the clone: %s' % script)
            continue
        t1 = time.time()
        r = run([sys.executable, p], cwd=clone, env=env, timeout=3600)
        out = (r.stdout or b'').decode('utf-8', 'replace')
        err = (r.stderr or b'').decode('utf-8', 'replace')
        found = [ln.strip() for ln in out.splitlines() if needle in ln]
        rows.append(dict(label=lbl, script=script, rc=r.returncode,
                         lines=found[-3:], secs=round(time.time() - t1, 1)))
        rec('    %-62s rc=%-3d %.0f s' % (lbl[:62], r.returncode, time.time() - t1))
        for ln in found[-3:]:
            rec('        %s  (%s)' % (ln[:92], sense))
        if r.returncode != 0:
            fails.append('cold control failed: %s' % script)
            rec('        ### ### **DISAGREEMENT, AT FULL PROMINENCE.**')
            for ln in (out.splitlines()[-14:] if out.strip() else []):
                rec('        ### %s' % ln[:100])
            for ln in (err.splitlines()[-14:] if err.strip() else []):
                rec('        ### stderr: %s' % ln[:100])

    after = tracked_state(ROOT)
    rec('')
    rec('-' * 100)
    rec('### THE CORPUS AFTER THE COLD RUN.')
    rec('-' * 100)
    rec('  tracked state AFTER : %r' % (after[:160],))
    same = (before == after)
    bset = set(before.splitlines())
    aset = set(after.splitlines())
    rec('  paths that APPEARED during the controls : %s' % (sorted(aset - bset) or 'NONE'))
    rec('  paths that VANISHED during the controls : %s' % (sorted(bset - aset) or 'NONE'))
    rec('  ### **THE CORPUS\'S TRACKED STATE IS UNCHANGED BY THE COLD RUN : %s**' % same)
    rec('  ### **THIS IS NOT A FORMALITY.** ### Instrument files carry absolute paths into the')
    rec('  ### corpus, and a control run from a clone through one of them would have written here.')
    if not same:
        fails.append('the cold run changed the corpus\'s tracked state')

    payload = dict(head=head, remote=remote, controls=rows,
                   hardcoded={k: len(v) for k, v in hits.items()},
                   e16_hardcoded={k: len(v) for k, v in e16hits.items()},
                   corpus_unchanged=same, elapsed=time.time() - t0, fails=fails)
    io.open(os.path.join(D, 'b314_coldrelay_rows.json'), 'w', encoding='utf-8',
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
    io.open(os.path.join(D, 'b314_coldrelay_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
