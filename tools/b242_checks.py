# -*- coding: utf-8 -*-
"""b242_checks.py -- the b242 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that an envelope was fitted to a residual, or an axis chosen for smallness.
###       ### Gates 1-3: the registration precedes everything, the envelope precedes the
###       ### confirming run BY HASH **AND** MTIME, and the act banked NO envelope at all.
###   (2) that the scope wall was crossed. ### Gate 4 reads every tool of this act and
###       ### requires the right-side objects to be ABSENT from all of them.
###   (3) that a convergence verdict came from a method that cannot see convergence.
###       ### Gate 5: the positive controls must converge, and gate 6 is their must-fail twin.
###   (4) that this act's own algebra was 'verified' by a check that cannot fail.
###       ### Gate 7 runs the act's cumulative-sum identity on ARBITRARY INPUTS -- the
###       ### tautology control the ferry requires -- and shows what a REAL check looks like
###       ### beside it.
###   (5) that a claimed absence was never shown to be detectable. ### Gates 8 and 9 are
###       ### positive controls on absences.
###   (6) that the act overclaimed its own registered expectation. ### Gate 11 requires the
###       ### bank to say BOTH seats were wrong.
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

REG = os.path.join(D, 'b242_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b242_left_mode_axis.txt')
ENV = os.path.join(D, 'b242_envelope.txt')
RUN1 = os.path.join(D, 'b242_mode_axis_run.txt')
RUN1B = os.path.join(D, 'b242_floor_grid.txt')
CONF = os.path.join(D, 'b242_confirm_run.txt')
PTS = os.path.join(D, 'b242_floor_points.json')
B240RUN = os.path.join(D, 'b240_faceoff_run.txt')
B241BANK = os.path.join(D, 'b241_residual_ledger.txt')

TOOLS = [os.path.join(E16, f) for f in
         ('b242_mode_axis.py', 'b242_floor_grid.py', 'b242_envelope.py', 'b242_confirm.py')]

RIGHT_SIDE_TOKENS = ('theta_quotient', 'Thq', 'PR', 'wPrimes', 'A - PR')


def sha_of(path):
    import hashlib
    return hashlib.sha256(io.open(path, encoding='utf-8').read().encode('utf-8')).hexdigest()


def env_precedes_confirm():
    """### BOTH LIMBS. ### The confirming run carries the envelope's OWN hash, and the envelope
    ### is OLDER on disk than the tool that consumed it. ### EITHER LIMB ALONE IS FORGEABLE."""
    if not (os.path.exists(ENV) and os.path.exists(CONF)):
        return False
    return (sha_of(ENV) in io.open(CONF, encoding='utf-8').read()
            and os.path.getmtime(ENV) < os.path.getmtime(os.path.join(E16, 'b242_confirm.py')))


def code_only(path):
    """### SCOPE CONTROL, AND IT IS b142's OWN LESSON APPLIED TO THIS ACT'S OWN GATE:
    ### "A SCANNER WITH NO SCOPE CONTROL DOES NOT REPORT THE RULE -- IT REPORTS THE CORPUS."
    ### The first run of gate 4 FAILED partly on the tool's own SCOPE DECLARATION, which names
    ### the forbidden objects in order to forbid them. ### A gate that cannot tell a prohibition
    ### from a violation is not a gate. ### THIS STRIPS DOCSTRINGS AND COMMENTS AND SCANS CODE.
    """
    import ast
    src = io.open(path, encoding='utf-8').read()
    doc_lines = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.body and isinstance(node.body[0], ast.Expr) \
                    and isinstance(node.body[0].value, ast.Constant) \
                    and isinstance(node.body[0].value.value, str):
                s0 = node.body[0]
                for ln in range(s0.lineno, (s0.end_lineno or s0.lineno) + 1):
                    doc_lines.add(ln)
    keep = []
    for i, line in enumerate(src.split('\n'), 1):
        if i in doc_lines:
            continue
        keep.append(line.split('#', 1)[0])
    return '\n'.join(keep)


def right_side_absent(paths):
    """### THE SCOPE WALL, OVER CODE, AND MATCHED AS **IDENTIFIERS** RATHER THAN SUBSTRINGS.

    ### `A` is licensed by the registration as the constant inside resid47 and is NOT in this
    ### list; the objects that would make a face-off ARE.
    ### ### THE SECOND REPAIR, AND IT IS b164's OWN SPECIES: ### the substring form matched `PR`
    ### ### inside "S**PR**EAD" and "**PR**ICED" and reported a scope breach in two tools that
    ### ### have none. ### "RETRIEVAL BY STRING IS NOT RETRIEVAL BY OBJECT." ### A gate that
    ### ### cannot tell an identifier from four letters of an English word reports the corpus.
    """
    import re
    for p in paths:
        s = code_only(p)
        for t in RIGHT_SIDE_TOKENS:
            pat = r'\b%s\b' % re.escape(t) if re.match(r'^\w+$', t) else re.escape(t)
            if re.search(pat, s):
                return False
    return True


def controls_converge():
    """### THE POSITIVE CONTROLS MUST BE SEEN TO CONVERGE. ### Read from the run, not re-derived:
    ### control A's partial-sum error must fall below 1e-14 by mode 7."""
    s = io.open(RUN1, encoding='utf-8').read()
    return ('CONTROL A' in s and 'CONTROL B' in s
            and '3.331e-15' in s and '1.999e+00' in s)


def cumsum_identity(shuffle):
    """### THE ARBITRARY-INPUTS TAUTOLOGY CONTROL THE FERRY REQUIRES, ON THIS ACT'S OWN ALGEBRA.

    ### This act's truncation axis rests on ONE algebraic step: the partial sums of `tr` are the
    ### cumulative sums of `tr`. ### That is a TAUTOLOGY -- it holds for ANY array -- and this
    ### function demonstrates it on random data rather than letting the act cite its own table
    ### as if it were evidence.
    ### ### THE POINT OF SHOWING IT: ### the act's REAL content is NOT that identity. ### It is
    ### the GATE in b242_mode_axis.py that `trace_modes(NMODE=5) == trace_modes(NMODE=11)[:5]`,
    ### which is an empirical claim about the instrument and CAN fail. ### `shuffle=True`
    ### breaks the cumulative-sum step and must be caught, proving the test discriminates.
    """
    import numpy as np
    rng = np.random.default_rng(20260829)
    worst = 0.0
    for _ in range(400):
        tr = rng.normal(0.0, 1.0, 11)
        c = np.cumsum(tr)
        for n in range(11):
            direct = float(np.sum(tr[:n + 1] if not shuffle else tr[:max(1, n)]))
            worst = max(worst, abs(direct - c[n]))
    return bool(worst <= 1e-12)


def floor_jump_is_at_eight():
    """### THE ACT'S CENTRAL EMPIRICAL CLAIM, RE-DERIVED FROM THE BANKED POINTS, NOT READ FROM
    ### THE PROSE: the NQ-spread at NMODE<=7 is small and at NMODE>=8 is two orders larger."""
    pts = json.load(io.open(PTS, encoding='utf-8'))
    nqs = [500, 700, 900, 1100, 1300]
    for cell in ('2', '3', '4', '8', '9', '12'):
        def spread(nm):
            v = [pts['%s|%d|%d' % (cell, q, nm)] for q in nqs]
            return max(v) - min(v)
        if not (spread(7) < 2e-3 and spread(8) > 2e-2 and spread(8) / spread(7) > 20):
            return False
    return True


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b242')

    # 1 -- ### THE REGISTRATION PRECEDES EVERY MEASUREMENT FILE.
    h.run('registration-precedes-every-measurement',
          check=lambda: all(os.path.getmtime(REG) < os.path.getmtime(p)
                            for p in (RUN1, RUN1B, ENV, CONF)),
          fixture=lambda: os.path.getmtime(RUN1) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 6000)

    # 2 -- ### THE ENVELOPE PRECEDES THE CONFIRMING RUN, BY HASH **AND** BY MTIME.
    h.run('envelope-precedes-confirm-both-limbs',
          check=env_precedes_confirm,
          fixture=lambda: sha_of(ENV) in io.open(RUN1, encoding='utf-8').read(),
          witness=lambda: os.path.exists(ENV) and os.path.getsize(ENV) > 3000)

    # 3 -- ### NO ENVELOPE WAS BANKED, AND THE REFUSAL IS REASONED IN THE FILE ITSELF.
    # ### An act that could have banked a number and did not must show WHY in the artefact,
    # ### not only in the report.
    h.run('envelope-refused-with-reasons-in-the-artefact',
          check=lambda: all(contains(ENV, s) for s in
                            ('THE ENVELOPE THAT WOULD FOLLOW -- AND WHY IT IS **NOT** BANKED',
                             'THE RATIO IS RISING',
                             'UNVERIFIABLE AT THIS INSTRUMENT IN PRINCIPLE',
                             'NO OWNER PROVES THE TRACE SERIES CONVERGES AT ALL')),
          fixture=lambda: contains(B240RUN, 'THE RATIO IS RISING'),
          witness=lambda: contains(ENV, 'THE RATIO IS RISING'))

    # 4 -- ### THE SCOPE WALL. ### The right side appears in NO tool of this act.
    h.run('right-side-absent-from-every-tool',
          check=lambda: right_side_absent(TOOLS),
          # ### THE FIXTURE: the SAME test against b38_act10.py, which does contain them --
          # ### so the test is shown able to SEE a right-side object when one is there.
          fixture=lambda: right_side_absent([os.path.join(E16, 'b38_act10.py')]),
          witness=lambda: os.path.exists(TOOLS[0]))

    # 5 -- ### THE POSITIVE CONTROLS CONVERGE AND THE METHOD SEES IT.
    h.run('positive-controls-converge-and-are-seen',
          check=controls_converge,
          fixture=lambda: contains(B240RUN, 'CONTROL A'),
          witness=lambda: contains(RUN1, 'CONTROL A'))

    # 6 -- ### AND THE CONTROLS FOUND THE FLOOR BEFORE THE TRACE SERIES WAS LOOKED AT.
    h.run('controls-flatten-at-the-same-floor',
          check=lambda: both(RUN1, '3.331e-15', '1.647e-08'),
          fixture=lambda: both(B240RUN, '3.331e-15', '1.647e-08'),
          witness=lambda: contains(RUN1, '1.647e-08'))

    # 7 -- ### THE ARBITRARY-INPUTS TAUTOLOGY CONTROL ON THIS ACT'S OWN ALGEBRA.
    h.run('cumsum-step-is-a-tautology-DEMONSTRATED',
          check=lambda: cumsum_identity(shuffle=False),
          fixture=lambda: cumsum_identity(shuffle=True),
          witness=lambda: contains(RUN1, 'partial-sum invariance'))

    # 8 -- ### POSITIVE CONTROL ON AN ABSENCE: the empirical gate that DOES carry content --
    # ### tr[n] independent of NMODE -- was run and passed at 0.00e+00.
    h.run('partial-sum-invariance-gate-ran-and-passed',
          check=lambda: contains(RUN1, 'partial-sum invariance  max|tr(NMODE=5) - '
                                       'tr(NMODE=11)[:5]| = 0.00e+00  PASS'),
          fixture=lambda: contains(B240RUN, 'partial-sum invariance'),
          witness=lambda: contains(RUN1, 'PASS'))

    # 9 -- ### POSITIVE CONTROL ON THE SECOND ABSENCE: sec 25(a)'s non-negativity is
    # ### RE-VERIFIED at source at all six cells, not leaned on as an import.
    h.run('mode-terms-nonneg-reverified-six-cells',
          check=lambda: io.open(RUN1, encoding='utf-8').read().count(
              'mode terms negative at n = NONE') == 6,
          fixture=lambda: io.open(B240RUN, encoding='utf-8').read().count(
              'mode terms negative at n = NONE') == 6,
          witness=lambda: contains(RUN1, 'mode terms negative at n = NONE'))

    # 10 -- ### THE CENTRAL EMPIRICAL CLAIM, RE-DERIVED FROM THE BANKED POINTS.
    h.run('floor-jump-re-derived-from-banked-points',
          check=floor_jump_is_at_eight,
          # ### THE FIXTURE: the same test with the threshold inverted must fail, or the
          # ### predicate is answering yes to everything.
          fixture=lambda: (lambda p: all(
              (lambda s7, s8: s7 > 2e-3 and s8 < 2e-2)(
                  max([p['%s|%d|7' % (c, q)] for q in (500, 700, 900, 1100, 1300)])
                  - min([p['%s|%d|7' % (c, q)] for q in (500, 700, 900, 1100, 1300)]),
                  max([p['%s|%d|8' % (c, q)] for q in (500, 700, 900, 1100, 1300)])
                  - min([p['%s|%d|8' % (c, q)] for q in (500, 700, 900, 1100, 1300)]))
              for c in ('2', '3', '4', '8', '9', '12')))(
                  json.load(io.open(PTS, encoding='utf-8'))),
          witness=lambda: os.path.exists(PTS))

    # 11 -- ### THE ACT SAYS BOTH SEATS' REGISTERED EXPECTATIONS WERE WRONG.
    # ### An act whose own prediction always survives is an act that predicted late.
    h.run('both-registered-expectations-reported-wrong',
          check=lambda: (contains(REG, "THE EXECUTOR'S EXPECTED BRANCH: ### (BOUNDED-BY-FLOOR)")
                         and contains(BANK, 'ALSO NOT BORNE OUT')
                         and contains(BANK, 'A FLOOR HIDES A TAIL; IT DOES NOT BOUND ONE')),
          fixture=lambda: contains(B241BANK, 'A FLOOR HIDES A TAIL'),
          witness=lambda: contains(BANK, 'NOT BORNE OUT'))

    # 12 -- ### THE DIRECTION OF THE REFUSED EXTRAPOLATION IS DISCLOSED, AND ITS CONSEQUENCE
    # ### IS ROUTED RATHER THAN DRAWN. ### Both halves, because either alone is a defect.
    h.run('bar_L-direction-disclosed-consequence-routed',
          check=lambda: (contains(BANK, 'IT IS TOO SMALL')
                         and contains(BANK, 'THIS ACT DOES NOT DRAW THE CONSEQUENCE FOR ANY '
                                            'FACE-OFF BRANCH, AND MAY NOT')
                         and contains(BANK, 'ROUTED TO THE CLOSE (b244)')),
          fixture=lambda: contains(B240RUN, 'IT IS TOO SMALL'),
          witness=lambda: contains(BANK, 'b244'))

    # 13 -- ### W-ORD-LEFT-MODE-AXIS DISCHARGED, AND M-4 **NOT** CLAIMED PAID.
    h.run('work-order-discharged-M4-not-claimed-paid',
          check=lambda: (contains(BANK, '`W-ORD-LEFT-MODE-AXIS` IS **DISCHARGED**')
                         and contains(BANK, 'M-4 IS **NOT** PAID AT BENCH')
                         and not contains(BANK, 'M-4 ANNOTATED PAID-AT-BENCH')),
          fixture=lambda: contains(B240RUN, 'M-4 IS **NOT** PAID AT BENCH'),
          witness=lambda: contains(BANK, 'W-ORD-LEFT-MODE-AXIS'))

    # 14 -- ### NOTHING THE SCOPE FORBIDS WAS TOUCHED.
    h.run('handoff-place-kernel-untouched',
          check=lambda: (unmodified(ROOT, 'HANDOFF.md')
                         and unmodified('D:/SIDE-global-section', 'Interfaces')
                         and unmodified('D:/SIDE-global-section', 'Core')
                         and contains(BANK, 'PLACE-papers, HANDOFF, THE LOOM AND THE MIRROR')),
          fixture=lambda: unmodified(ROOT, 'data/b242_left_mode_axis.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    # 15 -- ### THE CEILING AND h2 IN EVERY BANKED ARTEFACT OF THIS ACT.
    h.run('ceiling-and-h2-in-every-artefact',
          check=lambda: all(contains(p, 'DECIDES NOTHING GLOBAL')
                            for p in (REG, BANK, RUN1, RUN1B, ENV, CONF)),
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
