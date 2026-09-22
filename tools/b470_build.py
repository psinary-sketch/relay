# -*- coding: utf-8 -*-
"""b470_build.py -- COMPONENT 3: THE SERIALIZED FOREGROUND BUILD, THEN THE AXIOM RUN.

### ### **`lake build -j1` DOES NOT EXIST IN LAKE 5.0.0** (the face quotes both refusals). ### So the
### one-job-at-a-time intent is met by hand: the project modules `Solution` needs are put in import
### order, and each unbuilt one gets ITS OWN `lake build <module>` invocation with
### `LEAN_NUM_THREADS=1`, so no two Lean processes run at once.
### ### **EACH CALL IS BOUNDED** -- it starts no new module after `BUDGET` seconds -- so a foreground
### tool call stays under its ten-minute limit, and the next call resumes: a built module stays built.
### ### **A MODULE THAT FAILS STOPS THE RUN**, and its name and error tail are banked; the grade then
### stays conditional. ### When everything is built, `scripts/PrintAxioms.lean` AS SHIPPED is run, and
### then the seat's own file for the Component-1 theorems, written in the scratchpad, never the clone.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
LOG = os.path.join(D, 'b470_build_log.txt')
STATE = os.path.join(D, 'b470_build_state.json')
NAMED = os.path.join('C:' + os.sep, 'Users', 'ECHOCH~1', 'AppData', 'Local', 'Temp', 'claude', 'D--',
                     '49943484-5ff3-4a99-9f75-0f3a8ae0d39a', 'scratchpad', 'B470NamedAxioms.lean')
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 480.0
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ENV = dict(os.environ, LEAN_NUM_THREADS='1',
           MATHLIB_CACHE_DIR=r'D:\lean-cache-b468r\mathlib', XDG_CACHE_HOME=r'D:\lean-cache-b468r\xdg')


def log(s):
    with io.open(LOG, 'a', encoding='utf-8', newline=NL) as fh:
        fh.write(s + NL)
    print(s)


def src(mod):
    return os.path.join(Z, *mod.split('.')) + '.lean'


def olean(mod):
    return os.path.join(Z, '.lake', 'build', 'lib', 'lean', *mod.split('.')) + '.olean'


def imports(mod):
    out = []
    for l in io.open(src(mod), encoding='utf-8', errors='replace'):
        m = re.match(r'^\s*import\s+(\S+)', l)
        if m:
            out.append(m.group(1))
        elif l.strip() and not l.strip().startswith(('--', '/-', 'import', '-/', 'module')) and out:
            break
    return [x for x in out if os.path.exists(src(x))]      # project modules only


def order(root):
    seen, out = set(), []

    def visit(m):
        if m in seen:
            return
        seen.add(m)
        for x in imports(m):
            visit(x)
        out.append(m)
    sys.setrecursionlimit(10000)
    visit(root)
    return out


def main():
    st = json.load(io.open(STATE, encoding='utf-8')) if os.path.exists(STATE) else dict(calls=0, done=[], failed=None)
    if st.get('failed'):
        print('### THE RUN STOPPED EARLIER AT A FAILED MODULE: %s' % st['failed']['module'])
        return 2
    st['calls'] += 1
    seq = order('Solution')
    todo = [m for m in seq if not os.path.exists(olean(m))]
    log('=== [%s] CALL %d : %d project modules in Solution`s closure ; %d built ; %d to build'
        % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), st['calls'], len(seq), len(seq) - len(todo), len(todo)))
    t0 = time.time()
    for m in todo:
        if time.time() - t0 > BUDGET:
            log('    ### budget reached; resume on the next call')
            break
        t1 = time.time()
        r = subprocess.run(['lake', 'build', m], cwd=Z, env=ENV, capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        dt = time.time() - t1
        if r.returncode != 0 or not os.path.exists(olean(m)):
            tail = [l for l in (r.stdout + r.stderr).split(NL) if l.strip()][-25:]
            log('    ### FAILED : %s (%.0fs) exit %d' % (m, dt, r.returncode))
            for l in tail:
                log('      | %s' % l[:220])
            st['failed'] = dict(module=m, exit=r.returncode, tail=tail)
            break
        log('    built %-60s %6.0fs' % (m, dt))
        st['done'].append(m)
    remaining = [m for m in seq if not os.path.exists(olean(m))]
    st['remaining'] = len(remaining)
    st['closure'] = len(seq)
    if not remaining and not st.get('failed') and not st.get('axioms_done'):
        log('=== ALL %d MODULES BUILT -- running the axiom files' % len(seq))
        a = subprocess.run(['lake', 'env', 'lean', 'scripts/PrintAxioms.lean'], cwd=Z, env=ENV,
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        io.open(os.path.join(D, 'b470_print_axioms_shipped.txt'), 'w', encoding='utf-8',
                newline=NL).write(a.stdout + a.stderr)
        b = subprocess.run(['lake', 'env', 'lean', NAMED], cwd=Z, env=ENV,
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        io.open(os.path.join(D, 'b470_print_axioms_named.txt'), 'w', encoding='utf-8',
                newline=NL).write(b.stdout + b.stderr)
        log('    shipped script exit %d ; named file exit %d' % (a.returncode, b.returncode))
        st['axioms_done'] = True
    json.dump(st, io.open(STATE, 'w', encoding='utf-8', newline=NL), indent=1)
    log('    ### remaining after this call : %d' % len(remaining))
    return 0


if __name__ == '__main__':
    sys.exit(main())
