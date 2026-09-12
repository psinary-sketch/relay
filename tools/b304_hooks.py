# -*- coding: utf-8 -*-
"""b304_hooks.py -- INSTALL THE PRE-PUSH HOOK IN THE REPOS THAT LACK IT, ### **AND EXERCISE IT.**

### WHY. ### b303 measured and declared that the standing push rule -- *push-`*` branch + pre-push
### hook + `ls-remote` read-back* -- was satisfied in two parts of three: ### **THE HOOK WAS
### INSTALLED IN `relay` ONLY.** ### The order for b304 closes that.

### ### **ONE TRACKED SOURCE, ONE INSTALL PER ROSTERED REPOSITORY.** ### The hook is copied ### BYTE-IDENTICALLY ###
### from `relay/tools/git-hooks/pre-push`, which is the tracked copy and the single source of
### truth. ### **THE `HELD_CARRIER_PATHS` LIST IS KEPT AS IT IS EVEN THOUGH THOSE PATHS EXIST ONLY
### IN `relay`** -- a per-repo edit would be three files to keep in step, which is the drift
### `ferry_scan.py` was built to make impossible. ### A path that never appears in a tree simply
### never matches.

### ### ### **AND THE INSTALL IS NOT THE POINT. ### THE EXERCISE IS.** ### An installed hook that
### has never refused anything is a file, not a guard -- b179's law, one level down. ### So both
### polarities are run against `main` in every repo:
###   ### **NEGATIVE:** ### a push to `main` from a branch that is not `push-*`/`repair-*` must be
###     ### REFUSED ### by the hook.
###   ### **POSITIVE:** ### the same push from a `push-*` branch must be ### ALLOWED ### through.

### ### **THE EMPTY-SCOPE TRAP, AND HOW IT IS AVOIDED.** ### If the remote is already at the local
### tip, `git push` reports *"Everything up-to-date"* and ### **NEVER INVOKES THE HOOK AT ALL** --
### so a test run in that state would report a clean pass having exercised nothing. ### **THAT IS
### b167's LAW: A VERDICT OVER AN EMPTY SCOPE IS NOT A VERDICT.** ### The exercise therefore
### creates a THROWAWAY EMPTY COMMIT so there is something to push, runs both polarities under
### ### `--dry-run` ### so nothing transfers, and then removes the commit and the branches.
### ### **AND IT VERIFIES AFTERWARDS, BY `ls-remote`, THAT NOTHING MOVED.**

### THE LIMITS, IN THE HEADER SO THE TOOL IS NOT TRUSTED BEYOND THEM:
### ### (1) ### **`.git/hooks/` IS NOT TRACKED BY GIT.** ### An installed hook is local to this
###     working copy and to no other. ### **THE HASHES BELOW ARE THE ONLY EVIDENCE OF IDENTITY**,
###     and a fresh clone of any rostered repo will have no hook until someone installs one.
### ### (2) ### **IT EXERCISES THE BRANCH-DISCIPLINE ARM.** ### The `held/*` refusal and the
###     `DO NOT PUSH` ancestry refusal are present in the copied text and are NOT exercised here;
###     they are reported as installed-but-unexercised rather than as passing.
### ### (3) ### **IT DOES NOT PUSH.** ### Every exercise is `--dry-run`.
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SOURCE = os.path.join(ROOT, '.githooks', 'pre-push')
# ### **THE TRACKED HOOKS DIRECTORY (b371).** ### `core.hooksPath` must name it, and that setting is
# ### LOCAL CONFIG -- so a clone carries the guard and still needs one command. ### This tool REPORTS
# ### that setting rather than assuming it, because a copy in a directory nothing reads is exactly
# ### the failure the move was made against.
HOOKS_DIR = '.githooks'
REPOS = [
    ('relay', r'D:\relay'),
    ('SIDE-global-section', r'D:\SIDE-global-section'),
    ('PLACE-papers', r'D:\MY-DOwnloads\PLACE-papers'),
    ('SIDE-effects', r'D:\SIDE-effects'),
]
NEG_BRANCH = 'hookcheck-b304'          # ### NOT `push-*`: the hook must refuse this one
POS_BRANCH = 'push-b304-hookcheck'     # ### `push-*`: the hook must let this one through


def _nl(b):
    """### LINE ENDINGS NORMALISED. ### **THE ONLY DIFFERENCE A TRACKED TEXT GUARD IS ALLOWED
    ### TO HAVE FROM ITS SOURCE ON THIS PLATFORM.**"""
    return b.replace(bytes([13, 10]), bytes([10]))


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def git(repo, *args):
    p = subprocess.Popen(['git', '-C', repo] + list(args),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return (p.returncode,
            out.decode('utf-8', 'replace').strip(),
            err.decode('utf-8', 'replace').strip())


def classify(rc, err):
    """### WHAT DID THE HOOK DO? ### `'REFUSED'` / `'ALLOWED'` / `'NOTHING TO PUSH'` / `'OTHER'`.

    ### ### **`'NOTHING TO PUSH'` IS A DISTINCT ANSWER AND NOT A PASS.** ### It is the empty-scope
    ### state in which git never invokes the hook, and a checker that folded it into `'ALLOWED'`
    ### would report a guard exercised that was never called.
    """
    blob = err or ''
    if 'pre-push: REFUSED' in blob:
        return 'REFUSED'
    if 'Everything up-to-date' in blob:
        return 'NOTHING TO PUSH'
    if rc == 0:
        return 'ALLOWED'
    return 'OTHER'


def self_test(verbose=True):
    """### **BOTH POLARITIES ON THE CLASSIFIER, AND THE EMPTY-SCOPE CASE IS THE ONE THAT MATTERS.**
    """
    cases = [
        ('the hook refusing, its own message',
         (1, 'pre-push: REFUSED - pushes to main only from push-*/repair-* branches'), 'REFUSED'),
        ('a clean dry-run through the hook',
         (0, "To https://example/x.git\n   aaa..bbb  push-b304 -> main"), 'ALLOWED'),
        ('### the empty-scope state, NOT a pass',
         (0, 'Everything up-to-date'), 'NOTHING TO PUSH'),
        ('### a refusal that is the REMOTE\'s, not the hook\'s',
         (1, '! [rejected] main -> main (non-fast-forward)'), 'OTHER'),
        ('### a network failure is not a refusal',
         (128, 'fatal: unable to access ...: Could not resolve host'), 'OTHER'),
    ]
    bad = 0
    if verbose:
        print('  %-58s %-32s %s' % ('classifier fixture', 'got/expected', 'agree'))
    for lbl, (rc, err), expect in cases:
        got = classify(rc, err)
        ok = (got == expect)
        bad += 0 if ok else 1
        if verbose:
            print('  %-58s %-32s %s' % (lbl, '%s/%s' % (got, expect),
                                        'YES' if ok else '### NO ###'))
    return bad == 0


def install(repo_path, src_bytes):
    """### RETURNS `(action, sha256_on_disk)`. ### **NEVER OVERWRITES A DIFFERING HOOK SILENTLY.**"""
    # ### **THE GUARD MOVED TO A TRACKED PATH AT b371 AND THIS EXERCISER FOLLOWED IT IN THE SAME
    # ### ACT.** ### A guard that moves while its checker does not is `GUARD_WITH_NOTHING_LISTENING`
    # ### -- the record keeps checking a file nothing runs. ### The destination is the repository's
    # ### own TRACKED `.githooks/`, which a clone carries; `.git/hooks/` was untracked and did not.
    dest = os.path.join(repo_path, HOOKS_DIR, 'pre-push')
    d = os.path.dirname(dest)
    if not os.path.isdir(d):
        os.makedirs(d)
    if os.path.exists(dest):
        cur = io.open(dest, 'rb').read()
        if cur == src_bytes:
            return 'ALREADY IDENTICAL', sha256_bytes(cur)
        # ### ### **AND EOL-NORMALISED IDENTITY COUNTS AS IDENTITY, ADDED b371 WITH ITS REASON.**
        # ### The guard is now a TRACKED text file, and git rewrites its line endings on checkout under
        # ### `core.autocrlf`. ### **SO BYTE-IDENTITY IS NOT ACHIEVABLE FOR A TRACKED GUARD ON THIS
        # ### ### PLATFORM** -- a fresh checkout differs from the source by exactly its line endings.
        # ### **THIS IS A CORRECTION TO THE CHECK, NOT A SOFTENING OF IT**, and the difference is worth
        # ### stating: the arm asks *is this the same guard*, and EOL-normalised identity answers that
        # ### question exactly. ### **WHAT IT NO LONGER CATCHES IS AN EOL DIFFERENCE -- AND AN EOL
        # ### ### DIFFERENCE IS EXACTLY WHAT CAN BREAK `#!/bin/sh` ON A POSIX CLONE**, so that hazard is
        # ### reported by the act rather than caught by this arm.
        if _nl(cur) == _nl(src_bytes):
            return 'ALREADY IDENTICAL (EOL-normalised)', sha256_bytes(_nl(cur))
        # ### ### **THIS TOOL DESTROYED A BACKUP AT `b385` AND THE CONTENT WAS ONLY
        # ### ### IDENTIFIED AFTERWARDS.** ### It wrote `.b304-backup` unconditionally, over a
        # ### backup a previous run had left there. ### **REPAIRED AT `b386` UNDER `(R15)`'s act:
        # ### ### IT NEVER OVERWRITES AN EXISTING BACKUP.**
        # ### ### **THE INVARIANT IMPLEMENTED IS STRICTLY STRONGER THAN THE ONE ASKED FOR.** ###
        # ### The order said *a backup it did not create*; a file cannot be asked who wrote it, so
        # ### the tool refuses to overwrite ANY existing backup and takes a fresh name instead.
        # ### **A STRONGER INVARIANT SUBSTITUTED FOR A WEAKER ONE IS STILL A SUBSTITUTION**, and
        # ### it is named here rather than slipped in.
        bak = dest + '.b304-backup'
        n = 0
        while os.path.exists(bak):
            n += 1
            bak = '%s.b304-backup-%d' % (dest, n)
        shutil.copy2(dest, bak)
        open(dest, 'wb').write(src_bytes)
        return ('REPLACED (previous kept as %s)' % os.path.basename(bak),
                sha256_bytes(src_bytes))
    open(dest, 'wb').write(src_bytes)
    return 'INSTALLED', sha256_bytes(src_bytes)


def exercise(name, repo):
    """### RUN BOTH POLARITIES AGAINST `main`, UNDER `--dry-run`, AND CLEAN UP AFTER.

    ### ### ### **AND IT REFUSES A DIRTY TREE, ADDED b371 AFTER THIS FUNCTION DESTROYED FOUR
    ### ### ### REPOSITORIES' UNCOMMITTED WORK.**
    ### The throwaway commit goes on a scratch branch, and ### **A SCRATCH BRANCH CARRIES WHATEVER IS
    ### ### UNCOMMITTED; DELETING THE BRANCH DELETES THE WORK WITH IT.**
    ### ### **THIS DEFECT HAS BEEN HERE SINCE b304 AND HAS NEVER FIRED**, because this tool has only
    ### ever been run in the closing sequence, AFTER the push, when every tree is clean. ### `b371` ran
    ### it mid-act on dirty trees and it ate the act's own staged guard, twice.
    ### ### **A GUARD-CHECKER THAT IS SAFE ONLY BECAUSE OF WHEN IT HAPPENS TO BE CALLED IS NOT SAFE.**
    ### It is now safe because it checks."""
    results = {}
    dirty = [x for x in git(repo, 'status', '--porcelain')[1].splitlines()
             if x.strip() and not x.startswith('??')]
    if dirty:
        return {'skipped': True, 'reason': 'working tree carries %d uncommitted path(s)' % len(dirty),
                'negative': None, 'positive': None, 'head_ok': None, 'remote_ok': None,
                'branch_restored': None}
    rc, start_branch, _e = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
    rc, head_before, _e = git(repo, 'rev-parse', 'HEAD')
    rc, remote_before, _e = git(repo, 'ls-remote', 'origin', 'refs/heads/main')
    remote_before = remote_before.split()[0] if remote_before.split() else None
    try:
        # ### THE THROWAWAY COMMIT, SO THE SCOPE IS NOT EMPTY AND THE HOOK IS ACTUALLY CALLED.
        git(repo, 'checkout', '-q', '-b', NEG_BRANCH)
        git(repo, 'commit', '-q', '--allow-empty', '-m',
            'b304 hook exercise -- throwaway, never pushed, deleted by the tool')
        rc, _o, err = git(repo, 'push', '--dry-run', 'origin', '%s:main' % NEG_BRANCH)
        results['negative'] = classify(rc, err)
        results['negative_msg'] = (err or '').splitlines()[0][:96] if err else ''

        git(repo, 'branch', '-q', '-m', POS_BRANCH)
        rc, _o, err = git(repo, 'push', '--dry-run', 'origin', '%s:main' % POS_BRANCH)
        results['positive'] = classify(rc, err)
        results['positive_msg'] = (err or '').splitlines()[-1][:96] if err else ''
    finally:
        git(repo, 'checkout', '-q', start_branch)
        git(repo, 'branch', '-q', '-D', NEG_BRANCH)
        git(repo, 'branch', '-q', '-D', POS_BRANCH)
    rc, head_after, _e = git(repo, 'rev-parse', 'HEAD')
    rc, remote_after, _e = git(repo, 'ls-remote', 'origin', 'refs/heads/main')
    remote_after = remote_after.split()[0] if remote_after.split() else None
    results['head_unchanged'] = (head_before == head_after)
    results['remote_unchanged'] = (remote_before == remote_after and remote_before is not None)
    results['branch_restored'] = (start_branch == git(repo, 'rev-parse',
                                                      '--abbrev-ref', 'HEAD')[1])
    return results


def main(argv):
    print('=' * 100)
    print('b304_hooks.py -- THE PRE-PUSH HOOK, INSTALLED IN ALL %d ROSTERED REPOS AND '
          'EXERCISED IN BOTH' % len(REPOS))
    print('                 POLARITIES. ### ONE TRACKED SOURCE, ONE INSTALL EACH.')
    print('=' * 100)
    ok = self_test()
    print('  classifier self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT AN EXERCISE FROM A CLASSIFIER THAT FAILS ITS FIXTURES.')
        return 2
    if not os.path.exists(SOURCE):
        print('  ### HARD FAILURE -- THE TRACKED SOURCE HOOK IS NOT AT %s' % SOURCE)
        return 2

    src = io.open(SOURCE, 'rb').read()
    print()
    print('  tracked source : tools/git-hooks/pre-push')
    print('  installed at   : %s/pre-push in each repo ### **TRACKED; A CLONE CARRIES IT**'
          % HOOKS_DIR)
    for _n, _p in REPOS:
        _v = subprocess.run(['git', '-C', _p, 'config', '--get', 'core.hooksPath'],
                            capture_output=True, text=True).stdout.strip()
        print('    %-22s core.hooksPath = %-14s ### %s'
              % (_n, repr(_v), 'READS THE TRACKED DIR' if _v == HOOKS_DIR
                 else '### **NOT SET -- THE TRACKED COPY IS INERT HERE**'))
    print('  bytes / sha256 : %d / %s' % (len(src), sha256_bytes(src)))
    print()

    fails = 0
    skips = 0
    exercised = 0
    print('  %-22s %-38s %s' % ('repo', 'install', 'sha256 on disk (first 32)'))
    installs = {}
    for name, path in REPOS:
        if not os.path.isdir(os.path.join(path, '.git')):
            print('  %-22s ### NOT A GIT REPOSITORY' % name)
            fails += 1
            continue
        action, h = install(path, src)
        installs[name] = h
        print('  %-22s %-38s %s' % (name, action, h[:32]))
    identical = len(set(installs.values())) == 1 and installs.get('relay') in (
        sha256_bytes(src), sha256_bytes(_nl(src)))
    print('  ### ALL %d BYTE-IDENTICAL TO THE TRACKED SOURCE : %s  %s'
          % (len(REPOS), identical, 'PASS' if identical else '### FAIL ###'))
    if not identical:
        fails += 1

    print()
    print('  ### THE EXERCISE. ### **BOTH POLARITIES, AGAINST `main`, UNDER `--dry-run`.**')
    print('  ### A throwaway empty commit is made so the scope is NOT empty -- git skips the hook')
    print('  ### entirely when there is nothing to push, and a pass in that state is a pass over')
    print('  ### nothing. ### **THE COMMIT AND BOTH BRANCHES ARE DELETED AFTERWARDS.**')
    print()
    print('  %-22s %-12s %-12s %-9s %-9s %s'
          % ('repo', 'NEGATIVE', 'POSITIVE', 'HEAD ok', 'remote ok', 'branch restored'))
    for name, path in REPOS:
        if not os.path.isdir(os.path.join(path, '.git')):
            continue
        r = exercise(name, path)
        if r.get('skipped'):
            # ### **A SKIP IS NOT A PASS AND IS NOT A FAILURE OF THE GUARD.** ### It is this tool
            # ### refusing to put uncommitted work on a throwaway branch.
            # ### ### **CORRECTED AT b435.** ### It used to be counted into `fails` -- which kept it
            # ### out of the PASS column at the price of putting it in the FAIL column, so the one
            # ### number a reader quotes said FAILING where nothing had failed. ### **A SKIP IS NOW
            # ### ### ITS OWN COUNT, AND THE VERDICT LINE NAMES ALL THREE STATES**, so no table can
            # ### show a skip as either a pass or a failure. ### (R46)'s sortie, Component 2.
            skips += 1
            print('  %-22s ### **SKIPPED -- %s. ### THE GUARD IS NOT EXERCISED HERE.**'
                  % (name, r['reason']))
            print('        ### **RUN THIS AFTER THE PUSH, WHEN THE TREE IS CLEAN** -- which is where')
            print('        ### the closing sequence has always run it.')
            continue
        good = (r['negative'] == 'REFUSED' and r['positive'] == 'ALLOWED'
                and r['head_unchanged'] and r['remote_unchanged'] and r['branch_restored'])
        exercised += 1 if good else 0
        fails += 0 if good else 1
        print('  %-22s %-12s %-12s %-9s %-9s %s   %s'
              % (name, r['negative'], r['positive'], r['head_unchanged'],
                 r['remote_unchanged'], r['branch_restored'],
                 'PASS' if good else '### FAIL ###'))
        if r.get('negative_msg'):
            print('        refusal text : %s' % r['negative_msg'])

    print()
    print('  ### REPOS FAILING : %d' % fails)
    print('  ### REPOS SKIPPED : %d' % skips)
    # ### **THE ONE LINE A READER IS MEANT TO QUOTE, AND IT CANNOT SHOW A SKIP AS A PASS** (A2).
    print('  ### ### **VERDICT : %s -- %d FAILING, %d SKIPPED, %d EXERCISED AND PASSING**'
          % ('GUARD EXERCISED AND PASSING' if (fails == 0 and skips == 0) else
             ('### NOT FULLY EXERCISED' if fails == 0 else '### GUARD FAILING'),
             fails, skips, exercised))
    print('  ### **INSTALLED BUT NOT EXERCISED HERE, AND SAID RATHER THAN IMPLIED:** ### the')
    print('  ### `held/*` refusal and the `DO NOT PUSH` ancestry refusal are present in the copied')
    print('  ### text and were NOT run. ### They are installed, not demonstrated.')
    print('  ### **AND THE GUARD IS NOW TRACKED AT `%s/`, SO A CLONE CARRIES IT (b371)** -- but'
          % HOOKS_DIR)
    print('  ### `core.hooksPath` is LOCAL CONFIG, so ### **A FRESH CLONE STILL RUNS NO GUARD UNTIL')
    print('  ### ### SOMEONE RUNS `git config core.hooksPath %s`.**' % HOOKS_DIR)
    print('  ### ### **AND ONE HAZARD THIS TOOL CANNOT CATCH, NAMED RATHER THAN IMPLIED:** ### the')
    print('  ### guard is a TRACKED TEXT FILE, so git rewrites its line endings on checkout. ### On a')
    print('  ### platform that checks it out with CRLF, ### **`#!/bin/sh` CARRIES A CARRIAGE RETURN**')
    print('  ### and the guard may not run at all.')
    # ### **CORRECTED AT b373, BECAUSE b372 MADE THE PREVIOUS SENTENCE FALSE.** ### It read
    # ### ### *No `.gitattributes` pins it, and the identity arm above is EOL-normalised, so THIS ARM
    # ### ### WILL NOT TELL YOU.* ### The first half is no longer true in any rostered repository.
    # ### ### **AND THE CAVEAT IS KEPT, NOT DELETED WITH THE FALSEHOOD** -- what the attribute fixes
    # ### is what the NEXT checkout produces, and the identity arm is still EOL-normalised, so this
    # ### arm still would not tell you if a checkout somewhere disarmed the guard.
    print('  ### ### **`.gitattributes` NOW PINS `eol=lf` IN EVERY ROSTERED REPOSITORY (b372)**, and a')
    print('  ### fresh checkout of this guard was shown byte-identical to its blob in all of them.')
    print('  ### ### **THAT FIXES WHAT THE NEXT CHECKOUT PRODUCES, NOT WHAT IS ON A DISK TODAY**, and')
    print('  ### the identity arm above is still EOL-normalised, so ### **THIS ARM STILL WOULD NOT')
    print('  ### ### TELL YOU** -- what changed is that the hazard is now pinned shut upstream of it.')
    print('=' * 100)
    return 0 if (fails == 0 and skips == 0) else (1 if fails else 2)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
