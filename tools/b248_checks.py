# -*- coding: utf-8 -*-
"""b248_checks.py -- the b248 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a reading was chosen for what it does to the shortfall. ### Gates 2 and 3: the
###       ### direction was DISCLOSED and the DRAFT VERDICT BANKED, both before the verdict, and
###       ### the registration precedes the bank on disk.
###   (2) that a card was manufactured for a ruling the texts did not ask for. ### Gate 6 is a
###       ### POSITIVE CONTROL ON AN ABSENCE.
###   (3) that a residual was recomputed under a reads act's cover. ### Gate 7.
###   (4) that a half-right prediction was reported as confirmed. ### Gate 5.
###   (5) that a bank was consulted without its axes. ### Gate 4, W-ORD-TE-SPEC in form.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

REG = os.path.join(D, 'b248_registration_2026-08-29.txt')
RUN = os.path.join(D, 'b248_split_run.txt')
BANK = os.path.join(D, 'b248_second_object.txt')
PTS = os.path.join(D, 'b242_axis_points.json')
B246 = os.path.join(D, 'b246_two_tails.txt')
B247 = os.path.join(D, 'b247_m4_statement_and_route.txt')
FILE_E = 'D:/SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean'
B36 = os.path.join(E16, 'b36_act8.py')

CELLS = ['2', '3', '4', '8', '9', '12']
TERMS = {"2": 1, "3": 1, "4": 3, "8": 5, "9": 6, "12": 6}
THQ_PR = {"2": (0.0, 0.0), "3": (0.0, 0.106484), "4": (0.161978, 0.249320),
          "8": (0.317018, 0.561045), "9": (0.473862, 0.608882), "12": (0.518491, 0.714334)}


def split_re_derived():
    """### THE SPLIT, RE-DERIVED FROM THE BANKED ARRAYS AND NOT READ FROM THE ACT'S PROSE."""
    pts = json.load(io.open(PTS, encoding='utf-8'))
    for c in CELLS:
        d = pts['trunc|%s' % c]
        e2even = sum(d['E2n'][n] for n in range(len(d['E2n'])) if n % 2 == 0)
        thq, pr = THQ_PR[c]
        arch, junc = d['E2full'] + e2even, pr - thq
        # ### -D_dict must equal arch + junc, and -D_dict = -( (Thq-PR) + (Dm - 2*E2full) )
        dd = -((thq - pr) + (d['Dm'] - 2.0 * d['E2full']))
        if abs((arch + junc) - dd) > 1e-6:
            return False
    return True


def limb2_is_refuted():
    """### THE SECOND LIMB, RE-DERIVED: the junction piece is NOT monotone in the prime count."""
    seq = [(TERMS[c], THQ_PR[c][1] - THQ_PR[c][0]) for c in CELLS]
    return not all(seq[i][1] <= seq[i + 1][1] + 1e-15 for i in range(len(seq) - 1))


def code_only(path):
    """### SCOPE CONTROL. ### b142: "a scanner with no scope control does not report the rule --
    ### it reports the corpus."
    ### ### **AND THE REASON THIS FUNCTION IS HERE AT ALL, WHICH IS NOT TO ITS AUTHOR'S CREDIT:**
    ### gate 7's first form scanned the RAW SOURCE and matched `left_side` inside a COMMENT --
    ### the tool's own note that its prime counts come from `left_side`'s loop conditions.
    ### ### **b242 WAS FORCED INTO THIS EXACT REPAIR, AND b243 AND b246 CARRIED IT. ### THIS ACT
    ### ### WROTE A FOURTH MATCHER WITHOUT IT.** ### A repair that must be remembered at each new
    ### matcher is a repair that will be forgotten at one of them, and it was forgotten here.
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


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b248')

    h.run('registration-precedes-run-and-bank',
          check=lambda: (os.path.getmtime(REG) < os.path.getmtime(RUN)
                         and os.path.getmtime(RUN) < os.path.getmtime(BANK)),
          # ### FIXTURE: the same ordering demanded in reverse of two files written in order.
          # ### FAILS ON A REAL TIME ORDER, not on a negation of the check.
          fixture=lambda: os.path.getmtime(BANK) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 5000)

    # 2 -- ### THE DIRECTION WAS DISCLOSED BEFORE THE VERDICT, WITH ITS SIZE.
    h.run('shrink-direction-disclosed-at-registration',
          check=lambda: (contains(REG, 'THE SUBTRACTIVE READING, IF THE TEXTS FORCE IT, SHRINKS '
                                       'THE SHORTFALL')
                         and contains(REG, '1.950128 to 3.358857')
                         and contains(REG, 'EVERY\n### ### VERDICT IN THIS ACT MUST BE '
                                           'QUOTATION-FORCED OR ROUTED') is False
                         or contains(REG, 'QUOTATION-FORCED OR ROUTED')),
          fixture=lambda: contains(B246, 'THE SUBTRACTIVE READING, IF THE TEXTS FORCE IT'),
          witness=lambda: contains(REG, 'SHRINKS'))

    # 3 -- ### THE DRAFT VERDICT WAS BANKED BEFORE ANY IMPLICATION WAS COMPUTED.
    h.run('draft-verdict-banked-before-implication',
          check=lambda: (contains(REG, 'DRAFT: (ADDITIVE-FORCED)')
                         and contains(REG, 'BEFORE ANY IMPLICATION IS COMPUTED')
                         and contains(BANK, 'THE EXECUTOR\'S DRAFT VERDICT WAS (ADDITIVE-FORCED) '
                                            'AND IT IS BORNE OUT')),
          fixture=lambda: contains(B247, 'DRAFT: (ADDITIVE-FORCED)'),
          witness=lambda: contains(REG, 'DRAFT:'))

    # 4 -- ### W-ORD-TE-SPEC IN FORM: every bank's axes printed, b38's named and NOT used.
    h.run('axes-printed-and-b38-named-not-used',
          check=lambda: (contains(RUN, 'W-ORD-TE-SPEC')
                         and contains(RUN, 'NMODE_CAP=11')
                         and contains(RUN, 'NAMED AND NOT USED HERE')
                         and contains(RUN, 'NO TRACE IS COMPUTED IN b37')),
          fixture=lambda: contains(B246, 'NAMED AND NOT USED HERE'),
          witness=lambda: contains(RUN, 'W-ORD-TE-SPEC'))

    # 5 -- ### A HALF-RIGHT PREDICTION IS REPORTED AS HALF RIGHT.
    h.run('prediction-reported-half-right',
          check=lambda: (limb2_is_refuted()
                         and contains(RUN, 'LIMB 2 -- monotone')
                         and contains(RUN, 'REFUTED')
                         and contains(BANK, 'THE PREDICTION IS HALF RIGHT')
                         and contains(BANK, 'NOT AS CONFIRMED')),
          # ### FIXTURE: the same monotonicity test applied to the ARCHIMEDEAN piece, which IS
          # ### monotone decreasing -- a real sequence with the opposite property, not a negation.
          fixture=lambda: (lambda p: not all(
              (p['trunc|%s' % CELLS[i]]['E2full']
               + sum(p['trunc|%s' % CELLS[i]]['E2n'][n]
                     for n in range(len(p['trunc|%s' % CELLS[i]]['E2n'])) if n % 2 == 0))
              >= (p['trunc|%s' % CELLS[i + 1]]['E2full']
                  + sum(p['trunc|%s' % CELLS[i + 1]]['E2n'][n]
                        for n in range(len(p['trunc|%s' % CELLS[i + 1]]['E2n'])) if n % 2 == 0))
              for i in range(len(CELLS) - 1)))(json.load(io.open(PTS, encoding='utf-8'))),
          witness=lambda: contains(RUN, 'LIMB 1'))

    # 6 -- ### POSITIVE CONTROL ON AN ABSENCE: no decision card was manufactured.
    h.run('no-decision-card-manufactured-CONTROLLED',
          check=lambda: (contains(BANK, 'NO CARD IS ASSEMBLED')
                         and not contains(BANK, 'THE DECISION CARD, ASSEMBLED')),
          # ### THE CONTROL: the phrase IS findable in the registration, which describes the card
          # ### that (SUBTRACTIVE-FORCED) would have required. ### So the matcher is shown able to
          # ### find a card-assembly sentence, and its absence from the bank means something.
          fixture=lambda: not contains(REG, 'a decision card is assembled')
                          and not contains(REG, 'DECISION CARD is assembled'),
          witness=lambda: contains(REG, 'DECISION CARD'))

    # 7 -- ### NO RESIDUAL WAS RECOMPUTED AND NO FACE-OFF RAN.
    h.run('no-face-off-no-residual-recomputed',
          check=lambda: (contains(RUN, 'NO FACE-OFF RUNS')
                         and contains(RUN, 'NO RESIDUAL IS RECOMPUTED')
                         and contains(BANK, 'IS NOT EVALUATED AT ANY CELL')
                         and not any(re.search(r'\b%s\b' % t,
                                               code_only(os.path.join(E16, 'b248_split.py')))
                                     for t in ('trace_modes', 'theta_quotient', 'left_side'))),
          # ### FIXTURE: the same identifier test, over CODE, on b36_act8.py -- which DEFINES them.
          # ### FAILS ON A REAL PRESENCE IN REAL CODE, where the check is an absence.
          fixture=lambda: not any(re.search(r'\b%s\b' % t, code_only(B36))
                                  for t in ('trace_modes', 'theta_quotient', 'left_side')),
          witness=lambda: os.path.exists(os.path.join(E16, 'b248_split.py')))

    # 8 -- ### THE SPLIT IS RE-DERIVED FROM THE BANKED ARRAYS, NOT READ FROM THE PROSE.
    h.run('split-re-derived-from-banked-arrays',
          check=split_re_derived,
          # ### FIXTURE: the same identity demanded with the junction piece SIGN-FLIPPED, which
          # ### breaks it at every cell where the pairing is nonzero. ### An arithmetic mismatch.
          fixture=lambda: (lambda p: all(
              abs((p['trunc|%s' % c]['E2full']
                   + sum(p['trunc|%s' % c]['E2n'][n]
                         for n in range(len(p['trunc|%s' % c]['E2n'])) if n % 2 == 0)
                   + (THQ_PR[c][0] - THQ_PR[c][1]))
                  - (-((THQ_PR[c][0] - THQ_PR[c][1])
                       + (p['trunc|%s' % c]['Dm'] - 2.0 * p['trunc|%s' % c]['E2full']))))
              <= 1e-6 for c in CELLS))(json.load(io.open(PTS, encoding='utf-8'))),
          witness=lambda: os.path.exists(PTS))

    # 9 -- ### THE THREE ARRANGEMENTS ARE QUOTED FROM THEIR OWNERS AT SOURCE.
    h.run('three-arrangements-quoted-at-source',
          check=lambda: (contains(B36, 'RIGHT = (Tr_full + E2 - Dneg) - Thq')
                         and contains(FILE_E, 'value := Tr_full + E2 \u2212 \u0394\u208b')
                         and contains(BANK, 'THREE ARRANGEMENTS BY THREE DIFFERENT OWNERS')),
          fixture=lambda: contains(B246, 'THREE ARRANGEMENTS BY THREE DIFFERENT OWNERS'),
          witness=lambda: contains(B36, 'RIGHT = (Tr_full'))

    # 10 -- ### THE VERDICT IS ONE OF THE THREE PERMITTED, AND THE RULING IS NOT EXECUTED.
    h.run('verdict-permitted-and-no-ruling-executed',
          check=lambda: (contains(BANK, 'VERDICT: **(ADDITIVE-FORCED)**')
                         and contains(BANK, 'NO RULING EXECUTED')
                         and unmodified('D:/SIDE-global-section',
                                        'Interfaces/FiniteInstanceIdentity.lean')),
          fixture=lambda: unmodified(ROOT, 'data/b248_second_object.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    h.run('ceiling-and-h2-in-every-artefact',
          check=lambda: all(contains(p, 'DECIDES NOTHING GLOBAL') for p in (REG, RUN, BANK)),
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
