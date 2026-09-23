# -*- coding: utf-8 -*-
"""b499_guard.py -- STEP (G): THE TOKEN-SCAN LIMB, ADDED TO THE SINGLE-SOURCE GUARD AND EXERCISED.

### (R110) says *"the pre-push guard scans every commit for it."* ### When the ferry arrived the guard
### had no such limb; the author chose to have it added here, BEFORE ANY USE OF THE TOKEN.
### ### **THE REAL TOKEN NEVER ENTERS THIS TOOL.** ### The exercise runs in a scratch clone with a
### FAKE value set in the child's environment only; the tool never reads `ZENODO_TOKEN` itself.
"""
import hashlib
import io
import json
import os
import shutil
import stat
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
REPOS = [os.path.join('D:', os.sep, 'relay'),
         os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers'),
         os.path.join('D:', os.sep, 'SIDE-global-section'),
         os.path.join('D:', os.sep, 'SIDE-explicit-formula')]
SRC = os.path.join(REPOS[0], '.githooks', 'pre-push')
SCRATCH = os.environ.get('B499_SCRATCH') or os.path.join(os.environ.get('TEMP', 'C:\\Temp'), 'b499_guard_scratch')
FAKE = 'FAKE-TOKEN-b499-' + 'x' * 44            # ### a 60-character string that is NOT the token
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ANCHOR = '  if [ "$remote_ref" = "refs/heads/main" ]; then'
HEADER_OLD = '# Tracked at .githooks/pre-push (moved there b371, 2026-09-08).'
HEADER_NEW = ('# (v) refuse any outgoing commit whose patch or message carries the ZENODO_TOKEN string\n'
              '#     (added b499, 2026-09-23, under ruling (R110)); the string is read by awk from\n'
              '#     ENVIRON, never passed as an argument and never written to a file; if the variable\n'
              '#     is not set in the pushing shell the scan cannot run, and the guard SAYS SO.\n'
              + HEADER_OLD)
LIMB = r'''  # (v) the token scan -- added b499 under (R110). Every outgoing commit on every pushed ref,
  # its patch AND its message. The token is read by awk from ENVIRON and never printed.
  if [ "$local_sha" != "0000000000000000000000000000000000000000" ]; then
    if [ -n "$ZENODO_TOKEN" ]; then
      if [ "$remote_sha" = "0000000000000000000000000000000000000000" ]; then
        if git log -p --format='%H%n%B' "$local_sha" --not --remotes="$remote" 2>/dev/null \
            | awk 'BEGIN{t=ENVIRON["ZENODO_TOKEN"]; f=0} index($0,t){f=1} END{exit f?0:1}'; then
          echo "pre-push: REFUSED — an outgoing commit carries the ZENODO_TOKEN string (R110). It is not printed." >&2
          exit 1
        fi
      else
        if git log -p --format='%H%n%B' "$remote_sha..$local_sha" 2>/dev/null \
            | awk 'BEGIN{t=ENVIRON["ZENODO_TOKEN"]; f=0} index($0,t){f=1} END{exit f?0:1}'; then
          echo "pre-push: REFUSED — an outgoing commit carries the ZENODO_TOKEN string (R110). It is not printed." >&2
          exit 1
        fi
      fi
    else
      echo "pre-push: WARNING — ZENODO_TOKEN is not set in this shell; the (R110) token scan did NOT run." >&2
    fi
  fi

'''


def rec(s=''):
    L.append(s)
    print(s)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def git(cwd, *a, env=None):
    return subprocess.run(['git'] + list(a), cwd=cwd, capture_output=True, text=True,
                          encoding='utf-8', errors='replace', env=env)


def rmtree(p):
    def onerr(f, path, _):
        os.chmod(path, stat.S_IWRITE)
        f(path)
    if os.path.exists(p):
        shutil.rmtree(p, onerror=onerr)


def main():
    rec('=' * 104)
    rec('b499 -- STEP (G): THE TOKEN-SCAN LIMB. ### **ADDED BEFORE ANY USE OF THE TOKEN.**')
    rec('=' * 104)
    exercise_only = '--exercise-only' in sys.argv[1:]
    before = {r: sha(os.path.join(r, '.githooks', 'pre-push')) for r in REPOS}
    for r, h in before.items():
        rec('    before : %s  %s' % (h[:16], r))
    if len(set(before.values())) != 1:
        rec('    ### THE FOUR COPIES DISAGREE BEFORE THE EDIT -- STOP.')
        return 2
    src = open(SRC, 'rb').read().decode('utf-8')
    if exercise_only:
        rec('    ### --exercise-only : the limb was added by the first run; NOTHING IS WRITTEN NOW.')
        kept = ident = ('(v) the token scan' in src and len(set(before.values())) == 1)
        after = before
        rec('    limb present and four copies identical : %s' % ident)
    elif '(v) the token scan' in src:
        rec('    ### THE LIMB IS ALREADY PRESENT -- REFUSING A SECOND ONE.')
        return 2
    if not exercise_only and (src.count(ANCHOR) != 1 or src.count(HEADER_OLD) != 1):
        rec('    ### ANCHOR NOT FOUND EXACTLY ONCE -- STOP.')
        return 2
    if not exercise_only:
        new = src.replace(HEADER_OLD, HEADER_NEW).replace(ANCHOR, LIMB + ANCHOR)
        old_lines, new_lines = src.split(NL), new.split(NL)
        it = iter(new_lines)
        kept = all(any(o == n for n in it) for o in old_lines)
        rec('    every prior line kept, in order : %s ; lines %d -> %d' % (kept, len(old_lines), len(new_lines)))
        if not kept:
            return 2
        for r in REPOS:
            with open(os.path.join(r, '.githooks', 'pre-push'), 'wb') as fh:
                fh.write(new.encode('utf-8'))
        after = {r: sha(os.path.join(r, '.githooks', 'pre-push')) for r in REPOS}
        for r, h in after.items():
            rec('    after  : %s  %s' % (h[:16], r))
        ident = len(set(after.values())) == 1
        rec('    ### ### **BYTE-IDENTICAL IN ALL FOUR : %s**' % ident)

    # ------------------------------------------------------------------ the exercise
    rec('')
    rec('### THE EXERCISE, IN A SCRATCH CLONE, WITH A FAKE VALUE. ### **THE REAL TOKEN IS NOT USED.**')
    rec('-' * 104)
    rmtree(SCRATCH)
    c = git(os.path.dirname(SCRATCH), 'clone', '-q', '--no-checkout', REPOS[0], SCRATCH)
    rec('    clone exit : %d  (%s)' % (c.returncode, SCRATCH))
    git(SCRATCH, 'config', 'core.hooksPath', '.githooks')
    git(SCRATCH, 'config', 'user.email', 'b499@scratch')
    git(SCRATCH, 'config', 'user.name', 'b499 scratch')
    os.makedirs(os.path.join(SCRATCH, '.githooks'), exist_ok=True)
    git(SCRATCH, 'checkout', '-q', '-b', 'push-b499-test', 'origin/main')
    shutil.copyfile(SRC, os.path.join(SCRATCH, '.githooks', 'pre-push'))   # ### the NEW guard
    base = {k: v for k, v in os.environ.items() if k != 'ZENODO_TOKEN'}
    fake_env = dict(base, ZENODO_TOKEN=FAKE)
    probe = os.path.join(SCRATCH, 'b499_probe.txt')
    cases = []

    def attempt(label, content, env, expect_refuse, expect_warn):
        # ### ### **THE NEW GUARD IS COPIED IN BEFORE EVERY CASE, AND ITS DIGEST PRINTED.** ### The
        # ### first run copied it once; `reset --hard` after the first case restored the COMMITTED
        # ### (old) guard, so the second and third cases ran the old hook and proved nothing.
        hook = os.path.join(SCRATCH, '.githooks', 'pre-push')
        shutil.copyfile(SRC, hook)
        hook_is_new = sha(hook) == sha(SRC)
        io.open(probe, 'w', encoding='utf-8', newline=NL).write(content + NL)
        git(SCRATCH, 'add', 'b499_probe.txt')
        git(SCRATCH, 'commit', '-q', '-m', 'b499 guard exercise: ' + label)
        p = git(SCRATCH, 'push', '--dry-run', 'origin', 'push-b499-test:main', env=env)
        err = p.stderr or ''
        refused = 'REFUSED' in err and 'ZENODO_TOKEN' in err
        warned = 'the (R110) token scan did NOT run' in err
        leaked = FAKE in (p.stdout or '') + err
        ok = (hook_is_new and refused == expect_refuse and warned == expect_warn and not leaked
              and (p.returncode != 0) == expect_refuse)
        rec('    %-44s hook %s exit %-3d refused %-5s warned %-5s value printed %-5s ### %s'
            % (label, sha(hook)[:12], p.returncode, refused, warned, leaked,
               'AS EXPECTED' if ok else 'NOT AS EXPECTED'))
        cases.append(dict(label=label, hook_is_new=hook_is_new, exit=p.returncode, refused=refused, warned=warned,
                          leaked=leaked, ok=ok))
        git(SCRATCH, 'reset', '-q', '--hard', 'origin/main')

    attempt('POSITIVE: a commit carrying the fake value', 'key = ' + FAKE, fake_env, True, False)
    attempt('NEGATIVE: a commit without it, variable set', 'nothing secret here', fake_env, False, False)
    attempt('UNSET: the variable absent', 'nothing secret here', base, False, True)
    allok = all(x['ok'] for x in cases)
    rec('    ### ### **ALL THREE AS EXPECTED : %s**' % allok)
    rmtree(SCRATCH)
    rec('    scratch clone removed : %s' % (not os.path.exists(SCRATCH)))
    rec('=' * 104)
    io.open(os.path.join(D, 'b499_guard.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(before=before, after=after, identical=ident, kept=kept, cases=cases, allok=allok,
                   scratch_removed=not os.path.exists(SCRATCH)),
              io.open(os.path.join(D, 'b499_guard.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print('  written: b499_guard.txt, b499_guard.json')
    return 0 if (ident and allok and kept) else 1


if __name__ == '__main__':
    sys.exit(main())
