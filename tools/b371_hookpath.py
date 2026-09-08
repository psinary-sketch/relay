# -*- coding: utf-8 -*-
"""b371_hookpath.py -- COMPONENT 3: THE GUARD MOVED TO A TRACKED PATH, OR STRUCK.

### ### **THE ORDER ALLOWS TWO OUTCOMES AND FORBIDS BOTH**, and says the choice is made by ### **WHAT
### THE TRACKED PATH CAN ACTUALLY CARRY** -- so the choice is made by a TEST and not by preference.
### ### **WHAT `DURABLE` MEANS HERE, EXACTLY, AND IT IS LESS THAN IT SOUNDS:** ### `core.hooksPath` is
### LOCAL CONFIG. ### **A CLONE STILL RUNS NO GUARD UNTIL SOMEONE SETS IT.** ### What changes is that
### the GUARD ITSELF now travels with the clone, so the residual step is ### **ONE CONFIG COMMAND AND NOT
### ### A FILE NOBODY HAS.** ### The residual step is named, never described as zero.
### ### **THE OLD LOCATION IS NOT DELETED.** ### With the path set, `.git/hooks/pre-push` is inert; if the
### config is ever unset it becomes live again. ### **A SAFETY NET AND ALSO A TRAP**, and the act says so.
### ### **AN UNEXERCISED HOOK IS AN ASSERTION**, so the move and the exercise are the same run.
"""
import io
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
SOURCE = os.path.join(ROOT, 'tools', 'git-hooks', 'pre-push')
TRACKED_DIR = '.githooks'
REPOS = [('relay', os.path.join('D:', os.sep, 'relay')),
         ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section')),
         ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
         ('SIDE-effects', os.path.join('D:', os.sep, 'SIDE-effects'))]
NEG = 'hookcheck-b371'
POS = 'push-b371-hookcheck'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or ''), (r.stderr or '')


def main():
    rec('=' * 100)
    rec('b371 -- COMPONENT 3: THE GUARD MOVED TO A TRACKED PATH.')
    rec('=' * 100)
    src = open(SOURCE, 'rb').read()
    rec('')
    rec('  tracked source : tools/git-hooks/pre-push ; %d bytes' % len(src))

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE TEST THAT DECIDES THE OUTCOME. ### **NOT A PREFERENCE.**')
    rec('-' * 100)
    rec('    ### the question the order poses: ### **CAN A TRACKED DIRECTORY IN EACH REPOSITORY HOLD THE')
    rec('    ### ### GUARD, AND DOES THE REPOSITORY THEN RUN IT?**')
    rec('    ### **IF IT RUNS AND REFUSES AND ALLOWS CORRECTLY, THE ITEM IS MADE DURABLE. ### IF IT')
    rec('    ### ### CANNOT, THE ITEM IS STRUCK WITH THE REASON.**')

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE MOVE. ### **ONE TRACKED COPY PER REPOSITORY, BYTE-IDENTICAL TO THE SOURCE.**')
    rec('-' * 100)
    placed = {}
    for name, path in REPOS:
        dd = os.path.join(path, TRACKED_DIR)
        if not os.path.isdir(dd):
            os.makedirs(dd)
        dst = os.path.join(dd, 'pre-push')
        existed = os.path.exists(dst)
        shutil.copyfile(SOURCE, dst)
        try:
            os.chmod(dst, 0o755)
        except OSError:
            pass
        now = open(dst, 'rb').read()
        # ### **STAGING IS DEFERRED TO AFTER THE EXERCISE, AND THAT IS NOT TIDINESS.** ### The polarity
        # ### exercise puts a throwaway commit on a scratch branch, and discarding that branch discards
        # ### whatever it carried. ### The first version staged here and the suite, re-measuring the
        # ### filesystem instead of trusting this JSON, found ### **NOTHING TRACKED IN ANY REPOSITORY.**
        # ### **A TOOL WHOSE OWN TEST DESTROYS ITS OWN RESULT REPORTS A RESULT IT NO LONGER HAS.**
        placed[name] = dict(path='%s/pre-push' % TRACKED_DIR, bytes=len(now),
                            identical=(now == src), existed_before=existed, tracked=None)
        rec('    %-22s %s/pre-push  %d bytes  identical : %s  ### -- staged AFTER the exercise'
            % (name, TRACKED_DIR, len(now), now == src))
    rec('    ### ### **AND THAT IS THE WHOLE DIFFERENCE FROM `b369`S INSTALL:** ### these copies are')
    rec('    ### ### **INSIDE THE REPOSITORY`S OWN TREE AND STAGED FOR COMMIT**, so a clone carries them.')
    rec('    ### **FOUR COPIES CAN DRIFT**, and the exerciser`s byte-identity arm against the one source')
    rec('    ### is what catches that -- ### **THE DRIFT RISK IS REAL AND IT IS GUARDED.**')

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE CONFIGURATION. ### **THE RESIDUAL MANUAL STEP, NAMED.**')
    rec('-' * 100)
    cfg = {}
    for name, path in REPOS:
        git(path, 'config', 'core.hooksPath', TRACKED_DIR)
        _rc, v, _e = git(path, 'config', '--get', 'core.hooksPath')
        cfg[name] = v.strip()
        rec('    %-22s core.hooksPath = `%s`' % (name, v.strip()))
    rec('    ### ### ### **AND THIS IS THE PART THAT IS NOT DURABLE AND IS SAID SO:** ###')
    rec('    ### `core.hooksPath` lives in `.git/config`, which is ### **NOT TRACKED.**')
    rec('    ### ### **A FRESH CLONE STILL RUNS NO GUARD UNTIL SOMEONE RUNS:**')
    rec('    ###     `git config core.hooksPath %s`' % TRACKED_DIR)
    rec('    ### ### **WHAT CHANGED IS WHICH HALF IS MISSING.** ### Before: the clone had neither the')
    rec('    ### guard nor the wiring, and the guard existed only on this machine. ### Now: the clone has')
    rec('    ### ### **THE GUARD**, and lacks ### **ONE COMMAND.** ### That is a smaller hole and it is')
    rec('    ### not no hole.')

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE EXERCISE. ### **BOTH POLARITIES, IN EACH REPOSITORY, FROM THE TRACKED PATH.**')
    rec('-' * 100)
    # ### ### **THIS TOOL DOES NOT EXERCISE ON A DIRTY TREE, AND THE REASON IS AN INCIDENT IT CAUSED.**
    # ### ### The first version made a throwaway commit on a scratch branch and then `reset --hard`ed it
    # ### away. ### **A THROWAWAY BRANCH CARRIES THE UNCOMMITTED WORK WITH IT, AND DISCARDING THE BRANCH
    # ### ### DISCARDS THE WORK.** ### On its second run it destroyed this act's own trail block, its
    # ### correspondence row, its index key and its one licensed instrument edit -- all uncommitted.
    # ### ### **`b304_hooks.py` NEVER HAD THIS DEFECT**: it checks out back and deletes the branch, and
    # ### it runs AFTER the push, when the tree is clean. ### That is the safe moment, and this tool now
    # ### **DEFERS TO IT** rather than inventing a second exerciser that runs at the wrong one.
    results, deferred = {}, []
    for name, path in REPOS:
        dirty = [x for x in git(path, 'status', '--porcelain')[1].splitlines()
                 if x.strip() and not x.startswith('??')]
        if dirty:
            deferred.append(name)
            results[name] = dict(exercised=False,
                                 reason='the working tree carries uncommitted work; exercising it '
                                        'here would put that work on a throwaway branch',
                                 dirty=len(dirty))
            rec('    %-22s ### **DEFERRED -- %d uncommitted path(s); the post-push exerciser owns this**'
                % (name, len(dirty)))
            continue
        _rc, cur, _e = git(path, 'symbolic-ref', '--short', 'HEAD')
        cur = cur.strip()
        h0 = git(path, 'rev-parse', 'HEAD')[1].strip()
        out = {}
        for br, want in ((NEG, 'REFUSED'), (POS, 'ALLOWED')):
            git(path, 'checkout', '-q', '-b', br)
            git(path, 'commit', '-q', '--allow-empty', '-m', 'b371 hookcheck (throwaway)')
            rc, o, e = git(path, 'push', '--dry-run', 'origin', 'HEAD:main')
            txt = (o + e)
            refused = 'REFUSED' in txt or rc != 0
            out[br] = dict(want=want, refused=refused,
                           got=('REFUSED' if refused else 'ALLOWED'),
                           ok=((want == 'REFUSED') == refused),
                           text=[x for x in txt.split(chr(10)) if 'pre-push' in x][:1])
            git(path, 'checkout', '-q', cur)
            git(path, 'branch', '-q', '-D', br)
        h1 = git(path, 'rev-parse', 'HEAD')[1].strip()
        _rc, br_now, _e = git(path, 'symbolic-ref', '--short', 'HEAD')
        results[name] = dict(exercised=True, negative=out[NEG], positive=out[POS],
                             head_unmoved=(h0 == h1), branch_restored=(br_now.strip() == cur))
        rec('    %-22s NEGATIVE %-8s POSITIVE %-8s head unmoved %s  branch restored %s'
            % (name, out[NEG]['got'], out[POS]['got'], h0 == h1, br_now.strip() == cur))
    failing = [n for n, r in results.items()
               if r.get('exercised') and not (r['negative']['ok'] and r['positive']['ok']
                                              and r['head_unmoved'] and r['branch_restored'])]
    rec('    ### ### **EXERCISED HERE : %d ### / ### DEFERRED TO THE POST-PUSH EXERCISER : %d %s**'
        % (len(results) - len(deferred), len(deferred), deferred or ''))
    rec('    ### ### **FAILING AMONG THOSE EXERCISED HERE : %d %s**' % (len(failing), failing or ''))
    rec('    ### **AND `tools/b304_hooks.py` EXERCISES ALL FOUR AFTER THE PUSH, WHEN EVERY TREE IS')
    rec('    ### ### CLEAN** -- which is where the polarity bar is actually met, and the suite reads')
    rec('    ### that record and not this one for it.')

    rec('')
    rec('-' * 100)
    rec('  ### (4b) THE STAGING, AFTER THE EXERCISE. ### **BECAUSE THE EXERCISE DESTROYS AN INDEX.**')
    rec('-' * 100)
    rec('    ### the exercise puts a throwaway commit on a scratch branch, and a scratch branch carries')
    rec('    ### whatever is uncommitted. ### **SO THE GUARD IS STAGED AFTER IT, AND THE EXERCISE ITSELF')
    rec('    ### ### REFUSES ANY REPOSITORY WHOSE TREE IS DIRTY.**')
    for name, path in REPOS:
        git(path, 'add', '%s/pre-push' % TRACKED_DIR)
        _rc, tr, _e = git(path, 'ls-files', '--', '%s/pre-push' % TRACKED_DIR)
        placed[name]['tracked'] = bool(tr.strip())
        rec('    %-22s TRACKED BY GIT : %s' % (name, bool(tr.strip())))
    rec('    ### ### **TRACKED IN EVERY REPOSITORY : %s**'
        % all(v['tracked'] for v in placed.values()))

    rec('')
    rec('-' * 100)
    rec('  ### (5) THE OLD LOCATION. ### **LEFT IN PLACE, INERT, AND NAMED.**')
    rec('-' * 100)
    old = {}
    for name, path in REPOS:
        p = os.path.join(path, '.git', 'hooks', 'pre-push')
        old[name] = os.path.exists(p)
        rec('    %-22s .git/hooks/pre-push present : %s  ### -- INERT while core.hooksPath is set'
            % (name, old[name]))
    rec('    ### ### **A SAFETY NET AND A TRAP.** ### If the config is unset the old copy becomes live')
    rec('    ### again, which is a net; and two copies can drift, which is a trap. ### **BOTH ARE SAID')
    rec('    ### ### RATHER THAN LEAVING A READER TO FIND THE SECOND COPY.**')

    rec('')
    rec('-' * 100)
    rec('  ### (6) WHAT THIS ACT FOUND AND DID NOT REPAIR.')
    rec('-' * 100)
    txt = io.open(SOURCE, encoding='utf-8', errors='replace').read()
    stale_line = [x for x in txt.split(chr(10)) if 'Install:' in x]
    rec('    the guard`s own front matter still says:')
    for x in stale_line:
        rec('        | %s' % x.strip()[:150])
    rec('    ### ### **THAT INSTALL PATH IS NOW SUPERSEDED**, and the sentence went stale the moment the')
    rec('    ### guard moved. ### **A GUARD`S OWN FRONT MATTER IS A SURFACE TOO** -- which is the exact')
    rec('    ### species this act spent Components 1 and 2 on, committed by this act`s own repair.')
    rec('    ### ### **IT IS NOT REPAIRED HERE**, and the reason is the cap: the registration licensed')
    rec('    ### ### **ONE** ### owner instrument edit, and that one is the exerciser. ### **EDITING THE')
    rec('    ### ### GUARD WOULD BE A SECOND, AND WOULD ALSO CHANGE THE BYTES ALL FOUR COPIES ARE')
    rec('    ### ### COMPARED AGAINST.** ### Reported and routed.')

    ok = (not failing) and all(v['identical'] and v['tracked'] for v in placed.values())
    outcome = 'MADE DURABLE' if ok else 'STRUCK'
    rec('=' * 100)
    rec('  ### ### **COMPONENT 3 OUTCOME : %s**' % outcome)
    rec('  ### **AND `DURABLE` IS THE ORDER`S WORD, NOT A CLAIM THAT A CLONE IS GUARDED.** ### The GUARD')
    rec('  ### travels; the WIRING does not; the residual step is one command and it is named above.')
    rec('=' * 100)
    p = run_clock.write(D, 'b371_hookpath_notes', LINES)
    io.open(os.path.join(D, 'b371_hookpath.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(outcome=outcome, tracked_dir=TRACKED_DIR, source_bytes=len(src),
                        placed=placed, config=cfg, exercise=results, failing=failing, deferred=deferred,
                        exercised_here=len(results) - len(deferred),
                        polarity_bar_met_by='tools/b304_hooks.py, after the push',
                        old_location_present=old, old_location_deleted=False,
                        residual_step='git config core.hooksPath %s' % TRACKED_DIR,
                        residual_named=True, clone_is_guarded=False,
                        guard_front_matter_stale=bool(stale_line), guard_front_matter_repaired=False,
                        repos=[n for n, _ in REPOS],
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
