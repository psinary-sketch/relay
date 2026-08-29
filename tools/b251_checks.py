# -*- coding: utf-8 -*-
"""b251_checks.py -- the b251 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the meanings or the indictment order moved after a number was seen. ### Gates 1-2:
###       ### the HASH is recomputed and the mtimes are ordered.
###   (2) that a PROVEN line was slipped into a bar over a series the theorem does not cover.
###       ### Gates 4 and 5 -- ### **and 4 IS A POSITIVE CONTROL ON AN ABSENCE.**
###   (3) that a RESTATEMENT was reported as evidence. ### Gate 3 runs the decomposition on
###       ### ARBITRARY tuples (it must hold) AND the size claim on arbitrary tuples (it must
###       ### fail). ### **A control with only the first half would prove nothing.**
###   (4) that a number in the prose does not match the arrays. ### Gates 6-9 RE-DERIVE every
###       ### headline figure from the cache rather than reading the act's own sentences.
###   (5) that an owner was silently re-implemented, breaking G-INDEP. ### Gate 10, with the
###       ### `ast` stripper b242 was forced into and b248 forgot at its fourth matcher.
###   (6) that an axis moved after a number was seen. ### Gate 11.
###   (7) that the dossier decided what it was opened not to decide. ### Gate 13.
"""
import hashlib
import io
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

MEAN = os.path.join(D, 'b251_meanings.txt')
REG = os.path.join(D, 'b251_registration_2026-08-29.txt')
RUN = os.path.join(D, 'b251_run.txt')
BANK = os.path.join(D, 'b251_third_face_off.txt')
DOSS = os.path.join(D, 'b251_m2inf_dossier.txt')
CACHE = os.path.join(D, 'b251_cache.npz')
TOOL = os.path.join(E16, 'b251_faceoff.py')
B250 = os.path.join(D, 'b250_m4_derivation.txt')

MEAN_SHA = 'd5284f9e6246e72cfebe1e9642ee52ecd510ffaf1ffeec10a506c06d22aa4b3c'
CELLS = ['2', '3', '4', '8', '9', '12']
ENVELOPE = 1.158e-14


def code_only(path):
    """### SCOPE CONTROL with the `ast` comment/docstring stripper. ### b142.
    ### ### **b242 WAS FORCED INTO THIS REPAIR; b243, b246 AND b250 CARRIED IT; b248 WROTE A
    ### ### FOURTH MATCHER WITHOUT IT AND ITS GATE MATCHED INSIDE A COMMENT.** ### Sixth matcher,
    ### and it starts with the stripper."""
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


def cells():
    """### RE-DERIVE EVERY HEADLINE FIGURE FROM THE CACHED ARRAYS. ### NOT FROM THE ACT'S PROSE."""
    c = dict(np.load(CACHE, allow_pickle=True))
    out = []
    for lab in CELLS:
        A, P, PR, Thq, E2full = c['cell_%s' % lab]
        tr = c['cell_%s_tr_700' % lab]
        Tr_cut, Tr_max = float(tr[:7].sum()), float(tr[:11].sum())
        Dneg = float(tr[1:11:2].sum())
        d2 = Tr_max - A - E2full
        r47 = Tr_cut - A - E2full
        trtail = Tr_max - Tr_cut
        junc = PR - Thq
        LmR = ((Tr_max + E2full - Dneg) - Thq) - (A - PR)
        bar = max(abs((float(c['cell_%s_tr_%d' % (lab, q)][:11].sum()) - A - E2full) - d2)
                  for q in (500, 700, 900, 1100))
        out.append(dict(lab=lab, d2=d2, r47=r47, trtail=trtail, junc=junc, LmR=LmR,
                        third=2.0 * E2full - Dneg, bar=bar))
    return out


def decomposition_is_restatement():
    """### THE TAUTOLOGY CONTROL, BOTH HALVES.

    ### HALF ONE: the decomposition must hold on ARBITRARY tuples -- proving it is RESTATEMENT and
    ### therefore no evidence. ### HALF TWO: the SIZE claim must FAIL on arbitrary tuples --
    ### proving that IT is not restatement and therefore IS evidence.
    ### ### **A CONTROL CARRYING ONLY HALF ONE WOULD ESTABLISH THAT THE ACT PROVED NOTHING,
    ### ### WITHOUT ESTABLISHING THAT ANYTHING IT DID CLAIM HAS CONTENT.**
    """
    rng = np.random.default_rng(20260829)
    ok_restate, size_ever_false = True, False
    for _ in range(400):
        Trc, Trm, A, E2 = rng.normal(size=4) * 10.0
        d2, r47, tail = Trm - A - E2, Trc - A - E2, Trm - Trc
        ok_restate &= abs(r47 - (d2 - tail)) < 1e-9
        if not (abs(tail) < abs(d2)):
            size_ever_false = True
    return bool(ok_restate and size_ever_false)


def main():
    h = Harness(ROOT, 'b251')
    C = cells()

    # 1 -- ### THE MEANINGS FILE IS BYTE-FOR-BYTE WHAT THE REGISTRATION BANKED.
    h.run('meanings-hash-unchanged-since-registration',
          check=lambda: (hashlib.sha256(io.open(MEAN, 'rb').read()).hexdigest() == MEAN_SHA
                         and contains(REG, MEAN_SHA)
                         and os.path.getsize(MEAN) == 11048),
          # ### FIXTURE: the registration's OWN bytes hashed against the meanings' hash.
          # ### FAILS ON A REAL FILE, not on a negation of the check.
          fixture=lambda: hashlib.sha256(io.open(REG, 'rb').read()).hexdigest() == MEAN_SHA,
          witness=lambda: contains(REG, 'd5284f9e'))

    # 2 -- ### MEANINGS -> REGISTRATION -> RUN -> VERDICT, IN THAT ORDER ON DISK.
    h.run('meanings-and-registration-precede-the-run',
          check=lambda: (os.path.getmtime(MEAN) < os.path.getmtime(REG)
                         < os.path.getmtime(RUN) < os.path.getmtime(BANK)),
          fixture=lambda: os.path.getmtime(BANK) < os.path.getmtime(MEAN),
          witness=lambda: os.path.exists(MEAN) and os.path.getsize(MEAN) > 5000)

    # 3 -- ### THE TAUTOLOGY CONTROL, BOTH HALVES.
    h.run('decomposition-is-restatement-and-size-claim-is-not',
          check=decomposition_is_restatement,
          # ### FIXTURE: the vacuous form -- `x == x` on a real cell, true for every input.
          fixture=lambda: bool(abs(C[0]['d2'] - C[0]['d2']) > 1e-30),
          witness=lambda: contains(MEAN, 'ALGEBRAIC-RESTATEMENT AND CARRIES NO'))

    # 4 -- ### POSITIVE CONTROL ON AN ABSENCE. ### THE ENVELOPE IS NAMED AND NOT USED.
    #      ### The figure is shown FINDABLE in the run, so its want of a bar means something.
    h.run('envelope-named-and-not-used-in-any-bar',
          # ### THIS GATE'S FIRST FORM WAS **DECORATIVE AND I CAUGHT IT BEFORE BANKING IT.**
          # ### It read `(A and B and C and D) or E`, and `and` binds tighter than `or` in Python,
          # ### so a true `E` carried the whole conjunction regardless of A..D.
          # ### ### **A GATE THAT PASSES ON ONE DISJUNCT ASSERTS ONLY THAT DISJUNCT.** ### b244
          # ### caught a fixture that was the exact negation of its own check; b248's gate 2 carried
          # ### this same `or` shape. ### **THIRD APPEARANCE OF THE DECORATIVE-GATE SPECIES.**
          # ### Rewritten as a pure conjunction, and the ABSENCE limb made explicit.
          check=lambda: (contains(RUN, '1.158e-14')
                         and contains(RUN, 'NAMED AND DELIBERATELY NOT USED IN ANY BAR')
                         and contains(BANK, 'NO non-measured line at all')
                         and contains(BANK, 'IS MEASURED AND IS LABELLED MEASURED')
                         # ### THE ABSENCE ITSELF: no bar anywhere claims the envelope bounds
                         # ### `TrTail`. ### The phrase is constructed so a slip would trip it.
                         and not contains(RUN, 'TrTail <= 1.158e-14')
                         and not contains(BANK, 'TrTail <= 1.158e-14')),
          fixture=lambda: contains(B250, 'NAMED AND DELIBERATELY NOT USED IN ANY BAR'),
          witness=lambda: contains(RUN, '1.158e-14'))

    # 5 -- ### THE REFUSAL OF THE FERRY'S TAIL CLAUSE WAS BANKED **BEFORE** THE RUN.
    h.run('tail-clause-refusal-registered-before-the-run',
          check=lambda: (contains(MEAN, 'THE FERRY\'S OWN CLAUSE IS REFUSED HERE, BEFORE THE RUN')
                         and contains(REG, 'THE TAIL CLAUSE IS')
                         and contains(REG, 'REFUSED, ON b247')
                         and os.path.getmtime(MEAN) < os.path.getmtime(RUN)),
          fixture=lambda: contains(B250, 'THE FERRY\'S OWN CLAUSE IS REFUSED HERE'),
          witness=lambda: contains(MEAN, 'DOUBLE-NAME'))

    # 6 -- ### `TrTail` VERSUS THE ENVELOPE, RE-DERIVED FROM THE ARRAYS.
    h.run('trtail-is-orders-above-the-envelope-re-derived',
          check=lambda: bool(all(abs(c['trtail']) / ENVELOPE > 1e12 for c in C)),
          # ### FIXTURE: the envelope compared against ITSELF scaled -- a real quantity that
          # ### does NOT clear the same threshold.
          fixture=lambda: (ENVELOPE * 10) / ENVELOPE > 1e12,
          witness=lambda: bool(min(abs(c['trtail']) for c in C) > 0))

    # 7 -- ### LIMB 1 RE-DERIVED: `|resid47 - Delta_2real|` UNDER THE BAR AT EVERY CELL.
    h.run('limb1-holds-under-the-bar-at-every-cell',
          check=lambda: bool(all(abs(c['r47'] - c['d2']) <= c['bar'] for c in C)),
          # ### FIXTURE: the same comparison against a bar ten times too small. ### If it passed,
          # ### the bar would not be doing any work and limb 1 would be unfalsifiable.
          fixture=lambda: bool(all(abs(c['r47'] - c['d2']) <= c['bar'] / 10.0 for c in C)),
          witness=lambda: bool(all(c['bar'] > 0 for c in C)))

    # 8 -- ### THE DOMINANCE CLAIM RE-DERIVED: 61%-70%, AND FIRST AT EVERY CELL.
    h.run('delta2real-dominates-at-every-cell-re-derived',
          # ### THE RANGE'S FIRST FORM WAS 0.61-0.70, TAKEN FROM THE RUN'S ROUNDED TABLE BY
          # ### READING ITS LAST ROW AS THE MINIMUM. ### THE TRUE MINIMUM IS 0.60775 AT a^2 = 8,
          # ### AND THIS GATE FAILED AND CAUGHT THE ACT'S OWN PROSE. ### The bound is now
          # ### re-derived from the arrays, and the DOMINANCE ORDERING is what carries the claim.
          check=lambda: bool(all(0.6 <= c['d2'] / c['LmR'] <= 0.7
                                 and c['d2'] > c['third'] > c['junc'] for c in C)),
          # ### FIXTURE: the junction claimed dominant -- false at every cell, so a gate that
          # ### accepted it would be reading the wrong column.
          fixture=lambda: bool(all(c['junc'] > c['d2'] for c in C)),
          witness=lambda: bool(all(c['LmR'] > 0 for c in C)))

    # 9 -- ### NO FOURTH PIECE. ### (DISSONANT-BEYOND) GENUINELY UNTRIGGERED.
    h.run('leftover-is-machine-zero-re-derived',
          check=lambda: bool(max(abs(c['LmR'] - (c['d2'] + c['third'] + c['junc'])) for c in C) < 1e-12),
          fixture=lambda: bool(max(abs(c['LmR'] - (c['d2'] + c['junc'])) for c in C) < 1e-12),
          witness=lambda: len(C) == 6)

    # 10 -- ### G-INDEP IS STRUCTURAL: NO OWNER IS RE-IMPLEMENTED IN THE RUN TOOL.
    h.run('g-indep-no-owner-re-implemented',
          check=lambda: not re.search(
              r'^\s*def\s+(left_side|trace_modes|e2_of_grid|theta_quotient)\b',
              code_only(TOOL), re.M),
          # ### FIXTURE: b38_act10 DOES define all four -- the matcher finds them there, so its
          # ### silence on this act's tool is a REAL absence and not a broken regex.
          fixture=lambda: not re.search(
              r'^\s*def\s+(left_side|trace_modes|e2_of_grid|theta_quotient)\b',
              code_only(os.path.join(E16, 'b38_act10.py')), re.M),
          witness=lambda: 'import b38_act10' in code_only(TOOL))

    # 11 -- ### NO AXIS MOVED AFTER A NUMBER WAS SEEN.
    h.run('axes-match-the-registration',
          check=lambda: (contains(REG, '(500,8),(700,10),(900,11)')
                         and contains(REG, 'PLUS EXACTLY ONE REFINEMENT')
                         and '[(500, 8), (700, 10), (900, 11), (1100, 11)]' in code_only(TOOL)
                         and 'NU_HALF' not in code_only(TOOL)),
          fixture=lambda: '[(500, 8), (700, 10), (900, 11), (1300, 11)]' in code_only(TOOL),
          witness=lambda: contains(REG, 'EPS_NQ=700'))

    # 12 -- ### THE PRINT FLOOR WAS NAMED BEFORE MEASURING. ### THE b249 EXTENSION, IN FORM.
    h.run('print-floor-named-before-measuring',
          check=lambda: (contains(REG, 'PRINTED TO FOUR\n### DECIMALS AND NO COMPARISON AGAINST '
                                       'IT MAY BE FINER THAN 5e-5')
                         and contains(RUN, 'PRINTS resid47 TO FOUR DECIMALS')
                         and contains(RUN, 'NAMED AND NOT USED')
                         and os.path.getmtime(REG) < os.path.getmtime(RUN)),
          fixture=lambda: contains(B250, 'PRINTS resid47 TO FOUR DECIMALS'),
          witness=lambda: contains(REG, '5e-5'))

    # 13 -- ### THE DOSSIER OPENS AND DOES NOT DECIDE. ### POSITIVE CONTROL ON AN ABSENCE:
    #       ### the three readings are shown PRESENT, so the want of a chosen one means something.
    h.run('dossier-opens-and-does-not-decide',
          check=lambda: (all(contains(DOSS, s) for s in ('(R-I)', '(R-II)', '(R-III)'))
                         and contains(DOSS, 'OPENED AND *NOT* DECIDED')
                         and contains(DOSS, 'EXPRESSES NO PREFERENCE AMONG THE THREE')
                         and contains(DOSS, 'SPECIES: (RULING)')
                         and not contains(DOSS, 'THIS DOSSIER RULES')),
          fixture=lambda: contains(B250, 'EXPRESSES NO PREFERENCE AMONG THE THREE'),
          witness=lambda: contains(DOSS, 'M-2-inf'))

    # 14 -- ### THE WEAKNESS IS DISCLOSED, NOT DRESSED UP.
    h.run('wide-bar-weakness-disclosed',
          check=lambda: (contains(BANK, 'CONSISTENT*, NOT *SHARP*')
                         and contains(BANK, 'THE SPREAD DOES NOT SHRINK MONOTONICALLY')
                         and contains(DOSS, 'CONSISTENT RATHER THAN SHARP')
                         # ### and the disclosure is TRUE: re-derived, not asserted.
                         and bool(max(abs(c['trtail']) / c['bar'] for c in C) > 0.4)),
          fixture=lambda: bool(max(abs(c['trtail']) / c['bar'] for c in C) > 5.0),
          witness=lambda: contains(BANK, 'b229'))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
