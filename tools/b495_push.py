# -*- coding: utf-8 -*-
"""b495_push.py -- COMPONENT 4. ### **THE PUSH, READ BACK; AND THE BUILD, LAUNCHED DETACHED.**

### ### **A PUSH IS NOT A VERIFICATION AND A LAUNCH IS NOT A BUILD.** ### This component proves
### exactly two things: that the remote holds the SHA the local tree holds, read back by
### `ls-remote`; and that a process exists with a pid, writing to a named log. ### **THE LOG IS
### NOT READ IN THIS ACT** -- (R106)(3) gives it to the next one.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
# ### ### **THE GUARD'S SINGLE SOURCE IS `relay/.githooks/pre-push`, AND THE MECHANISM IS
# ### ### `core.hooksPath` -- NOT `.git/hooks`.** ### b371 moved it to a TRACKED directory so the
# ### guard travels with the repository; b386's (R15) made that the one source. ### The first
# ### version of this component wrote into `.git/hooks/` from a path that does not exist,
# ### ### **REINVENTING A CURE THAT ALREADY HAD A TOOL** -- b435's species, caught by the crash.
HOOK_SRC = os.path.join(ROOT, '.githooks', 'pre-push')
HOOKS_DIR = '.githooks'
LOG = os.path.join(D, 'b495_ef_build.log')
REPO = 'psinary-sketch/SIDE-explicit-formula'
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def g(*a, **kw):
    return subprocess.run(['git', '-C', kw.get('repo', KERNEL)] + list(a), capture_output=True,
                          text=True, encoding='utf-8', errors='replace')


def gs(*a, **kw):
    return g(*a, **kw).stdout.strip()


DESC = ('Vendored Lean 4 kernel (PLACE TO STAND): the 57-module local import closure of '
        'Zeta23.WeilEF.Main from anthropics/formal-math at v1.0 = 3635e748, byte-identical '
        'bodies with per-file attribution headers, Apache 2.0. NO PROFILE YET -- nothing here '
        'has been built or #print axioms-ed by this programme, and no corpus document cites '
        'any terminal in it.')


def main():
    cj = json.loads(io.open(os.path.join(D, 'b495_create.json'), encoding='utf-8').read())

    rec('=' * 104)
    rec('b495 COMPONENT 4 -- THE PUSH AND THE LAUNCH.')
    rec('=' * 104)

    # ---------------------------------------------------------------- the hook, first
    # ### ### **A FRESH REPOSITORY HAS NO HOOK**: `.git/hooks/` is not tracked, so the guard the
    # ### federation relies on is ABSENT until it is installed. ### b304's lesson, applied at the
    # ### one moment it matters most -- the first push a repository ever takes.
    if not os.path.isdir(os.path.join(KERNEL, '.git')):
        g('init', '-b', 'main')
        gs('config', 'user.email', 'psinary@hotmail.com')
        gs('config', 'user.name', 'psinary-sketch')
    import hashlib

    def nl(x):
        return x.replace(bytes([13, 10]), bytes([10]))

    hooks = os.path.join(KERNEL, HOOKS_DIR)
    os.makedirs(hooks, exist_ok=True)
    dst = os.path.join(hooks, 'pre-push')
    with open(HOOK_SRC, 'rb') as fh:
        srcb = nl(fh.read())
    with open(dst, 'wb') as fh:
        fh.write(srcb)
    os.chmod(dst, 0o755)
    g('config', 'core.hooksPath', HOOKS_DIR)
    with open(dst, 'rb') as fh:
        h = hashlib.sha256(nl(fh.read())).hexdigest()
    hsrc = hashlib.sha256(srcb).hexdigest()
    rec('  ### THE PRE-PUSH GUARD, INSTALLED BEFORE THE FIRST PUSH EVER TAKEN.')
    rec('    single source  : relay/.githooks/pre-push   sha256 %s' % hsrc[:32])
    rec('    installed at   : %s/pre-push               sha256 %s' % (HOOKS_DIR, h[:32]))
    rec('    `core.hooksPath` : %s' % (gs('config', '--get', 'core.hooksPath') or '### UNSET'))
    rec('    ### ### **IDENTICAL : %s.**' % (h == hsrc))
    rec('    ### ### **A FRESH REPOSITORY HAS NO GUARD UNTIL ONE IS PUT THERE** -- b304. ### And')
    rec('    ### the directory is ### **TRACKED** (b371): `.git/hooks/` is not, so a guard placed')
    rec('    ### there would not survive a clone. ### (R15): ONE GUARD, ONE SOURCE -- this is a')
    rec('    ### copy of `relay/.githooks/pre-push` and not a second guard.')
    rec('')

    # ---------------------------------------------------------------- the commit
    files = gs('status', '--porcelain')
    if files:
        g('add', '-A')  # ### permitted: `-A` is BANNED IN relay (b381), not in a kernel of copies
        g('commit', '-q', '-m',
          'SIDE-explicit-formula v0 -- %d modules vendored from zeta23 at %s = %s, '
          'byte-identical bodies with attribution headers. NO PROFILE.'
          % (cj['modules'], cj['pin'], cj['pin_sha'][:12]))
    head = gs('rev-parse', 'HEAD')
    tracked = [x for x in gs('ls-files').split(NL) if x.strip()]
    leans = [x for x in tracked if x.endswith('.lean')]
    rec('  ### THE COMMIT.')
    rec('    HEAD          : %s' % head)
    rec('    files tracked : %d  (%d `.lean`, of which %d vendored bodies and 1 library root)'
        % (len(tracked), len(leans), cj['modules']))
    rec('    ### `.lake/` is ignored; ### **NO BUILD ARTEFACT IS COMMITTED.**')
    rec('')

    # ---------------------------------------------------------------- the remote
    exists = subprocess.run(['gh', 'repo', 'view', REPO, '--json', 'name'],
                            capture_output=True, text=True).returncode == 0
    if not exists:
        r = subprocess.run(['gh', 'repo', 'create', REPO, '--public', '--description', DESC],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        rec('  ### the remote did not exist and was created : exit %d %s'
            % (r.returncode, (r.stderr or '').strip()[:80]))
    else:
        rec('  ### the remote already existed; not re-created.')
    if 'origin' not in gs('remote').split():
        g('remote', 'add', 'origin', 'https://github.com/%s.git' % REPO)

    # ### ### **THE PUSH GOES FROM A `push-*` BRANCH**, as the federation's procedure requires and
    # ### as the hook enforces: it reads the CHECKED-OUT branch, not the refspec's source (b423).
    g('checkout', '-q', '-b', 'push-b495')
    pr = subprocess.run(['git', '-C', KERNEL, 'push', 'origin', 'push-b495:main'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    g('checkout', '-q', 'main')
    g('branch', '-D', 'push-b495')
    remote = gs('ls-remote', 'origin', 'main').split()[0] if gs('ls-remote', 'origin', 'main') else ''
    rec('  ### THE PUSH, FROM A `push-*` BRANCH AS THE PROCEDURE REQUIRES.')
    rec('    push exit  : %d %s' % (pr.returncode, (pr.stderr or '').strip().split(NL)[-1][:70]))
    rec('    local HEAD : %s' % head)
    rec('    ### **`ls-remote` origin/main : %s**' % (remote or '### UNRESOLVED'))
    rec('    ### ### **AGREE : %s.** ### The remote SHA is READ BACK, never inferred from a'
        % (head == remote and bool(remote)))
    rec('    ### successful exit code -- a push can exit 0 having pushed a different ref.')
    rec('')

    # ---------------------------------------------------------------- the launch
    launcher = os.path.join(T, 'b495_launch.py')
    flags = 0
    kw = {}
    if os.name == 'nt':
        flags = subprocess.CREATE_NEW_PROCESS_GROUP | getattr(subprocess, 'DETACHED_PROCESS', 8)
        kw['creationflags'] = flags
    p = subprocess.Popen([sys.executable, launcher], cwd=KERNEL,
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL, close_fds=True, **kw)
    rec('  ### THE LAUNCH. ### **DETACHED; THIS ACT DOES NOT WAIT AND DOES NOT READ.**')
    rec('    launcher : tools/b495_launch.py')
    rec('    ### ### **pid : %d**' % p.pid)
    rec('    ### ### **log : %s**' % os.path.relpath(LOG, ROOT).replace(os.sep, '/'))
    rec('    ### the launcher stamps ### **AN INSTANT TAKEN AT EACH LINE, FROM THE CLOCK** --')
    rec('    ### b480 precomputed one instant and stamped every mark with it, so its log could')
    rec('    ### not say how long anything took or in what order it happened. ### Repaired here.')
    rec('    ### after the build it runs `#print axioms` on the three names the order gives,')
    rec('    ### ### **WHETHER OR NOT THE BUILD EXITED 0** -- a partial build still profiles what')
    rec('    ### it has, and a launcher that skips the profile hands the next act nothing.')
    rec('    ### ### **THE LOG IS NOT READ IN THIS ACT.** ### (R106)(3) gives it to b496.')
    rec('=' * 104)

    io.open(os.path.join(D, 'b495_push.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(head=head, remote=remote, agree=(head == remote and bool(remote)),
                   push_exit=pr.returncode, repo=REPO, created=not exists, pid=p.pid,
                   log=os.path.relpath(LOG, ROOT).replace(os.sep, '/'),
                   tracked=len(tracked), leans=len(leans), hook_identical=(h == hsrc)),
              io.open(os.path.join(D, 'b495_push.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b495_push.txt, b495_push.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
