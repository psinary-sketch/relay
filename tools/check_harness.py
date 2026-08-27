# -*- coding: utf-8 -*-
"""check_harness.py -- A CHECK'S PASS IS NOT READ UNTIL THE CHECK HAS FAILED (built b217).

### WHY THIS EXISTS. FOUR TIMES, IN THE SAME SHAPE:
### b142 -- a scanner with no scope control returned 178 "live uses", every one a
###   pre-existing ledger line. ### "A SCANNER WITH NO SCOPE CONTROL DOES NOT REPORT THE
###   RULE -- IT REPORTS THE CORPUS."
### b213 -- a fill-completeness count printed "REMAINING UNFILLED TOKENS: 6", re-matching
###   the ORIGINAL TOKENS the act had deliberately preserved inside its own comments.
### b213 -- a placed-file count returned 1, re-matching the class line the executor had
###   just written.
### b216 -- a query loop ran from the wrong directory, python could not find the module,
###   stdout was empty, "NO KEY" was therefore absent, and EVERY LINE READ "HIT".

### THE COMMON SHAPE, AND IT IS THE WHOLE REASON FOR THIS FILE:
### ### ALL FOUR HAD A FAILURE MODE THAT PRODUCES A **PLAUSIBLE ANSWER** RATHER THAN AN
### ### ERROR. ### A check that throws is caught by the next line of the script.
### ### A CHECK THAT RETURNS A NUMBER IN THE RIGHT RANGE IS CAUGHT BY NOTHING.

### THE RULE THIS TOOL ENFORCES:
### ### **NO ONE-LINE CHECK IS READ UNTIL IT HAS FAILED ON A FIXTURE IN THE SAME RUN.**
### A check that has not been seen to fail has not been seen to work. The fixture is not
### a nicety attached to the check; ### THE FIXTURE IS THE THING THAT LICENSES READING IT.

### ### AND A SECOND GUARD, ADDED BY b217's OWN RETROFIT AND NOT BY ITS DESIGN --
### ### WHICH IS WHAT A RETROFIT IS FOR.
### Running the three historical instances through the must-fail fixture caught ONE of
### them (b216's, a true false PASS) and NOT the other two. ### b213's TWO INSTANCES ARE
### FALSE **ALARMS**, NOT FALSE PASSES: their checks reported failure on a correct state,
### and they report failure on a broken state too. ### A CHECK THAT FAILS IN BOTH
### DIRECTIONS SAILS THROUGH A MUST-FAIL FIXTURE, because failing is all it can do.
### ### SO THE HARNESS ALSO ACCEPTS AN OPTIONAL **WITNESS**: a state where the check MUST
### ### PASS. ### A check that cannot pass on its own witness has not been shown to
### ### discriminate, and the harness REFUSES it exactly as it refuses a fixture that passes.
### ### THE TWO GUARDS ARE MIRRORS: THE FIXTURE PROVES THE CHECK CAN SAY NO, THE WITNESS
### ### PROVES IT CAN SAY YES, AND A CHECK THAT CANNOT DO BOTH IS NOT A CHECK.

# ### THE LIMITS, IN THE HEADER SO THE TOOL IS NOT TRUSTED BEYOND THEM:
# ### (1) ### IT CANNOT TELL A GOOD FIXTURE FROM A BAD ONE. A fixture that fails for the
# ###     wrong reason still licenses the check. ### THE HARNESS CHECKS THAT THE FIXTURE
# ###     FAILED, NOT THAT IT FAILED FOR THE RIGHT REASON, and no tool can check that.
# ### (2) It governs checks ROUTED THROUGH IT. A one-liner typed straight into a shell is
# ###     untouched by it. ### THE HABIT IS STILL THE HAZARD; this lowers its cost.
# ### (3) ### IT CANNOT MAKE A CHECK MEASURE THE RIGHT THING. b213's fill count would pass
# ###     this harness IF its fixture also ignored comments. ### THE HARNESS CLOSES SILENT
# ###     FAILURE, NOT WRONG SCOPE -- and b142's scope lesson is still its own lesson.

Usage:
    from check_harness import Harness, shell
    H = Harness(repo_root=r'D:\relay', act='b217')
    H.run('name', check=..., fixture=...)      # check/fixture: callables or shell(...)
    H.emit()                                    # writes the audit sidecar
"""
import io
import os
import subprocess
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_emit as AE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PASS, FAIL, ERROR = 'PASS', 'FAIL', 'ERROR'


class CwdError(RuntimeError):
    """### RAISED LOUDLY. b209 pushed to the wrong repository and b216 queried from the
       wrong directory; ### BOTH ARE ONE SPECIES AND THIS IS WHERE IT DIES."""


def shell(cmd, must_contain=None, must_not_contain=None, cwd=None):
    """A shell check with an EXPLICIT verdict rule.

    ### AN EMPTY STDOUT IS A **FAIL**, NEVER A PASS. ### That single line is b216's
    ### instance 3: the command did not run, stdout was empty, the forbidden string was
    ### therefore absent, and the absence read as success.
    ### A NONZERO EXIT IS AN **ERROR**, NOT A FAIL -- the difference matters, because an
    ### ERROR means the check did not report on the object at all.
    """
    def _run():
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           encoding='utf-8', errors='replace', cwd=cwd)
        out = (p.stdout or '') + (p.stderr or '')
        if p.returncode != 0:
            return ERROR, 'exit %d; output: %s' % (p.returncode, out.strip()[:200] or '(empty)')
        if not (p.stdout or '').strip():
            return FAIL, '### EMPTY STDOUT -- a FAIL, not a pass'
        if must_contain is not None and must_contain not in p.stdout:
            return FAIL, 'missing %r' % must_contain
        if must_not_contain is not None and must_not_contain in p.stdout:
            return FAIL, 'contains %r' % must_not_contain
        return PASS, 'ok'
    return _run


def _call(fn):
    """Run a check, normalising its verdict. ### AN EXCEPTION IS AN ERROR AND IS PRINTED
       WHOLE -- never swallowed, never silently converted to a FAIL."""
    try:
        r = fn()
    except Exception:
        return ERROR, '### EXCEPTION:\n' + traceback.format_exc().strip()
    if isinstance(r, tuple):
        return r
    if isinstance(r, bool):
        return (PASS if r else FAIL), 'bool'
    return ERROR, '### CHECK RETURNED %r -- not a bool and not (verdict, detail)' % (r,)


class Harness:
    def __init__(self, repo_root, act):
        self.act = act
        self.rows = []
        root = os.path.abspath(repo_root)
        here = os.path.abspath(os.getcwd())
        # ### THE CWD ASSERTION. ### Not a warning. The harness will not run at all.
        if os.path.normcase(here) != os.path.normcase(root):
            raise CwdError(
                '### REFUSED -- cwd is not the declared repo root.\n'
                '###   cwd  : %s\n###   root : %s\n'
                '### b216 ran a query loop from the wrong directory and every line read HIT.\n'
                '### THIS IS THAT SPECIES AND IT DIES HERE.' % (here, root))

    def run(self, name, check, fixture, witness=None):
        """### THE FIXTURE RUNS FIRST AND MUST **FAIL**. ### If it passes, the check is
           NOT RUN AT ALL and the row reads REFUSED.

           ### AND IF A **WITNESS** IS GIVEN IT MUST **PASS**. ### A check that cannot pass
           on a state where it must has not been shown to discriminate, and is refused --
           ### b213's TWO INSTANCES ARE EXACTLY THAT CASE and the must-fail fixture alone
           ### does not catch them."""
        fv, fd = _call(fixture)
        if fv == PASS:
            self.rows.append((name, 'REFUSED', '### FIXTURE PASSED -- the check was NOT RUN'))
            return 'REFUSED'
        if fv == ERROR:
            self.rows.append((name, 'REFUSED', '### FIXTURE ERRORED: %s' % fd))
            return 'REFUSED'
        if witness is not None:
            wv, wd = _call(witness)
            if wv != PASS:
                self.rows.append((name, 'REFUSED',
                                  '### WITNESS DID NOT PASS (%s: %s) -- the check cannot say '
                                  'YES and was NOT RUN' % (wv, wd)))
                return 'REFUSED'
        cv, cd = _call(check)
        self.rows.append((name, cv, 'fixture FAILED as required (%s); check: %s' % (fd, cd)))
        return cv

    # ------------------------------------------------------------------ reporting
    def counts(self):
        c = {PASS: 0, FAIL: 0, ERROR: 0, 'REFUSED': 0}
        for _, v, _ in self.rows:
            c[v] = c.get(v, 0) + 1
        return c

    def table(self):
        out = ['%-46s %-8s %s' % ('check', 'verdict', 'detail')]
        out.append('-' * 110)
        for n, v, d in self.rows:
            out.append('%-46s %-8s %s' % (n[:46], v, d.replace('\n', ' | ')[:120]))
        return '\n'.join(out)

    def emit(self):
        c = self.counts()
        verdict = ('CLEAN' if c[FAIL] == 0 and c[ERROR] == 0 and c['REFUSED'] == 0
                   else 'NOT CLEAN')
        blk, path = AE.emit('check_harness', self.act,
                            ['%d checks routed through the harness' % len(self.rows)],
                            [('checks', len(self.rows)), ('pass', c[PASS]),
                             ('fail', c[FAIL]), ('error', c[ERROR]),
                             ('refused', c['REFUSED'])], verdict)
        return blk, path


if __name__ == '__main__':
    print(__doc__)
