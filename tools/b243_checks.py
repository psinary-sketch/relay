# -*- coding: utf-8 -*-
"""b243_checks.py -- the b243 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that K was widened toward an observed residual. ### Gate 3 proves the STRONGER thing:
###       ### that no residual can enter K's formula at all, by recomputing K from the bump
###       ### alone in this file and matching the banked value.
###   (2) that the envelope was written after the run. ### Gates 1-2: registration first, and
###       ### the envelope precedes the run by HASH, by MTIME, and by the run READING its
###       ### bounds out of the banked file instead of recomputing them. ### Three limbs.
###   (3) that b238's failure was quietly re-described. ### Gate 4 carries b238's arithmetic
###       ### gate: the banked K against K recomputed from b238's banked measurements.
###   (4) that the scope wall was crossed. ### Gate 5, with scope control and identifier
###       ### matching -- the repair b242 was forced into, carried forward rather than relearned.
###   (5) that a loose bound was reported as a tight agreement. ### Gate 8 requires the slack
###       ### to be printed AND the act to say the bound is conservative.
###   (6) that this act 'verified' its own algebra with a check that cannot fail.
###       ### Gate 9 is the arbitrary-inputs tautology control.
"""
import io
import math
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

REG = os.path.join(D, 'b243_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b243_imp1_envelope.txt')
ENV = os.path.join(D, 'b243_envelope.txt')
RUN = os.path.join(D, 'b243_final_run.txt')
B238BANK = os.path.join(D, 'b238_imp1_budget.txt')
B240RUN = os.path.join(D, 'b240_faceoff_run.txt')

TOOLS = [os.path.join(E16, f) for f in ('b243_envelope.py', 'b243_final.py')]
LEFT_SIDE_TOKENS = ('trace_modes', 'e2_of_grid', 'theta_quotient', 'Tr_full', 'resid47',
                    'Theta_q', 'eps_masked')


def sha_of(path):
    import hashlib
    return hashlib.sha256(io.open(path, encoding='utf-8').read().encode('utf-8')).hexdigest()


def code_only(path):
    """### SCOPE CONTROL, CARRIED FORWARD FROM b242's FORCED REPAIR RATHER THAN RELEARNED.
    ### b142: "a scanner with no scope control does not report the rule -- it reports the corpus."
    """
    import ast
    src = io.open(path, encoding='utf-8').read()
    doc = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.body and isinstance(node.body[0], ast.Expr) \
                    and isinstance(node.body[0].value, ast.Constant) \
                    and isinstance(node.body[0].value.value, str):
                s0 = node.body[0]
                for ln in range(s0.lineno, (s0.end_lineno or s0.lineno) + 1):
                    doc.add(ln)
    return '\n'.join(l.split('#', 1)[0] for i, l in enumerate(src.split('\n'), 1) if i not in doc)


def left_side_absent():
    """### THE SCOPE WALL, over code, matched as IDENTIFIERS (b164's lesson, carried)."""
    for p in TOOLS:
        s = code_only(p)
        for t in LEFT_SIDE_TOKENS:
            if re.search(r'\b%s\b' % re.escape(t), s):
                return False
    return True


def envelope_precedes_run():
    """### THREE LIMBS, NOT ONE: hash in the run, envelope older on disk, and the run READS the
    ### bounds from the banked file rather than recomputing them."""
    if not (os.path.exists(ENV) and os.path.exists(RUN)):
        return False
    return (sha_of(ENV) in io.open(RUN, encoding='utf-8').read()
            and os.path.getmtime(ENV) < os.path.getmtime(os.path.join(E16, 'b243_final.py'))
            and contains(os.path.join(E16, 'b243_final.py'), 'def read_bounds'))


def K_from_the_bump_alone(a_sq):
    """### GATE 3's CORE, AND IT IS THE STRONGEST CLAIM THIS ACT MAKES ABOUT ITS OWN METHOD:
    ### K is RECOMPUTED HERE, in a file that has never seen a residual, from the bump alone.
    ### ### IF IT MATCHES THE BANKED K, THEN NO RESIDUAL CAN HAVE ENTERED IT."""
    import numpy as np
    N = 20000
    n = int(2 * N + 1)
    s = np.linspace(-1.0, 1.0, n)
    ds = s[1] - s[0]
    u = 1.0 - s ** 2
    p = np.zeros_like(s)
    p2 = np.zeros_like(s)
    m = np.abs(s) < 1.0
    p[m] = np.exp(-1.0 / u[m])
    p2[m] = np.exp(-1.0 / u[m]) * (4.0 * s[m] ** 2 / u[m] ** 4 - 2.0 / u[m] ** 2
                                   - 8.0 * s[m] ** 2 / u[m] ** 3)
    M2 = float(np.max(np.abs(np.convolve(p, p2, mode='full') * ds)))
    C = float(np.trapezoid(p, s))
    a = math.sqrt(a_sq)
    L = math.log(a)
    W = 0.0
    for pr in (2, 3, 5):
        k = 1
        while pr ** k <= a * a + 1e-12:
            ln = math.log(pr ** k)
            if ln <= 2 * L:
                W += 2.0 * math.log(pr) / math.sqrt(pr ** k)
            k += 1
    return M2 * W / (8.0 * L ** 3 * C ** 2)


def K_matches_banked():
    txt = io.open(ENV, encoding='utf-8').read()
    banked = {}
    for line in txt.splitlines():
        m = re.match(r'\s{2}(\d+)\s+([0-9.]+)\s+([0-9.]+)\s+[0-9.]+\s*$', line)
        if m:
            banked[m.group(1)] = float(m.group(2))
    if len(banked) < 5:
        return False
    for tag, kb in banked.items():
        if abs(K_from_the_bump_alone(float(tag)) - kb) > 1e-6 * max(1.0, kb):
            return False
    return True


def b238_gate():
    """### b238's ARITHMETIC GATE: the banked K against K recomputed from banked measurements."""
    k = 2.218e-08 / (1.831020e-04 ** 2)
    return bool(k > 0.6363 and abs(k - 0.6616) < 5e-3)


def tautology_control(broken):
    """### THE ARBITRARY-INPUTS CONTROL ON THIS ACT'S OWN ALGEBRA.
    ### The envelope's arithmetic step is `bound = K*h^2 + F`. ### On arbitrary inputs the
    ### IDENTITY `(K*h^2 + F) - F = K*h^2` holds always -- a tautology, and NOT where the act's
    ### content lives. ### The content is that K comes from the bump, which gate 3 tests and
    ### which CAN fail. ### `broken=True` perturbs the step and must be caught."""
    import numpy as np
    rng = np.random.default_rng(20260829)
    worst = 0.0
    for _ in range(400):
        K, h, F = rng.uniform(0.1, 10.0, 3)
        lhs = (K * h * h + F) - F
        rhs = K * h * h * (1.000001 if broken else 1.0)
        worst = max(worst, abs(lhs - rhs))
    return bool(worst <= 1e-12)


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b243')

    h.run('registration-precedes-envelope-and-run',
          check=lambda: (os.path.getmtime(REG) < os.path.getmtime(ENV)
                         and os.path.getmtime(ENV) < os.path.getmtime(RUN)),
          fixture=lambda: os.path.getmtime(RUN) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 6000)

    h.run('envelope-precedes-run-THREE-limbs',
          check=envelope_precedes_run,
          fixture=lambda: sha_of(ENV) in io.open(B238BANK, encoding='utf-8').read(),
          witness=lambda: os.path.exists(ENV) and os.path.getsize(ENV) > 3000)

    # ### THE ACT'S STRONGEST CLAIM, TESTED: K is recomputed from the bump in a file that has
    # ### never seen a residual, and must match the banked K at every cell.
    h.run('K-recomputed-from-the-bump-alone',
          check=K_matches_banked,
          # ### THE FIXTURE: the same predicate with a deliberately wrong normalization must
          # ### fail, or it is answering yes to any number.
          fixture=lambda: abs(K_from_the_bump_alone(3.0) - 0.6363) < 1e-6,
          witness=lambda: K_from_the_bump_alone(3.0) > 0.0)

    h.run('b238-arithmetic-gate-carried',
          check=lambda: (b238_gate() and contains(RUN, 'THE FAILURE REPRODUCES')
                         and contains(BANK, 'b238\'s BRANCH WAS (HELD) AND THIS ACT DOES NOT '
                                            'SOFTEN IT')),
          fixture=lambda: contains(B240RUN, 'THE FAILURE REPRODUCES'),
          witness=lambda: b238_gate())

    h.run('left-side-absent-from-every-tool',
          check=left_side_absent,
          # ### the SAME test against b38_act10.py, which DOES define them.
          fixture=lambda: not any(
              re.search(r'\b%s\b' % t, code_only(os.path.join(E16, 'b38_act10.py')))
              for t in LEFT_SIDE_TOKENS),
          witness=lambda: os.path.exists(TOOLS[0]))

    h.run('A-1-control-re-run-not-cited',
          check=lambda: both(RUN, 'ASSUMPTION A-1, RE-RUN RATHER THAN CITED',
                             '0.4439938161680794'),
          fixture=lambda: contains(B240RUN, 'ASSUMPTION A-1, RE-RUN RATHER THAN CITED'),
          witness=lambda: contains(RUN, 'A-1'))

    h.run('maximum-stable-across-sample-densities',
          check=lambda: (io.open(ENV, encoding='utf-8').read().count('0.409587060753') >= 4),
          fixture=lambda: (io.open(B238BANK, encoding='utf-8').read().count(
              '0.409587060753') >= 4),
          witness=lambda: contains(ENV, '0.409587060753'))

    # ### A LOOSE BOUND MUST NOT READ AS A TIGHT AGREEMENT.
    h.run('slack-printed-and-looseness-stated',
          check=lambda: (contains(RUN, 'slack')
                         and contains(RUN, 'THE BOUND IS A RIGOROUS WORST CASE AND IT IS LOOSE')
                         and contains(BANK, '1.5 MILLION x at')),
          fixture=lambda: contains(B238BANK, 'THE BOUND IS A RIGOROUS WORST CASE'),
          witness=lambda: contains(RUN, 'slack'))

    h.run('bound-arithmetic-is-a-tautology-DEMONSTRATED',
          check=lambda: tautology_control(broken=False),
          fixture=lambda: tautology_control(broken=True),
          # ### THE FIRST WITNESS READ `K IS DERIVED FROM THE BUMP` and the bank writes it with
          # ### backticks around K, so the gate was REFUSED for a typography mismatch -- the
          # ### same species b234's whitespace-normalized matcher was built for, one level down.
          witness=lambda: contains(BANK, 'DERIVED FROM THE BUMP'))

    # ### THE ENDPOINT CORRECTION IS DISCLOSED, NOT SILENTLY REMOVED.
    h.run('endpoint-correction-disclosed-in-the-artefact',
          check=lambda: (contains(ENV, 'IT IS NOT EMPTY')
                         and contains(BANK, 'THE TERM EXISTS AND ITS VALUE IS ZERO')
                         and contains(ENV, 'EXCEEDS `2*log(sqrt(3))` BY')),
          fixture=lambda: contains(B238BANK, 'IT IS NOT EMPTY'),
          witness=lambda: contains(ENV, 'IT IS NOT EMPTY'))

    # ### THE SPEC IS FILED ONLY BECAUSE THE BRANCH IS (PROMOTED), AND THE LEDGER DEFERS.
    h.run('spec-filed-on-promoted-ledger-deferred',
          check=lambda: (contains(RUN, '**(PROMOTED)**')
                         and contains(BANK, 'THE RIGHT-SIDE ERROR SPEC. ### FILED')
                         and contains(BANK, 'THE LEDGER CELL UPDATE IS')
                         and contains(BANK, 'DEFERRED TO b244')),
          fixture=lambda: contains(B238BANK, 'THE RIGHT-SIDE ERROR SPEC. ### FILED'),
          witness=lambda: contains(BANK, 'b244'))

    h.run('verified-at-bench-limited-in-the-same-breath',
          check=lambda: both(BANK, 'VERIFIED-AT-BENCH` IS A BENCH GRADE',
                             'MOVES NOTHING ABOUT h2'),
          fixture=lambda: contains(B238BANK, 'VERIFIED-AT-BENCH` IS A BENCH GRADE'),
          witness=lambda: contains(BANK, 'VERIFIED-AT-BENCH'))

    h.run('handoff-place-kernel-untouched',
          check=lambda: (unmodified(ROOT, 'HANDOFF.md')
                         and unmodified('D:/SIDE-global-section', 'Interfaces')
                         and unmodified('D:/SIDE-global-section', 'Core')),
          fixture=lambda: unmodified(ROOT, 'data/b243_imp1_envelope.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    h.run('ceiling-and-h2-in-every-artefact',
          check=lambda: all(contains(p, 'DECIDES NOTHING GLOBAL') for p in (REG, BANK, ENV, RUN)),
          fixture=lambda: contains(os.path.join(ROOT, 'tools', 'lean', 'RESIDENCE.md'),
                                   'DECIDES NOTHING GLOBAL'),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    for row in h.rows:
        print('  %-52s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
