# -*- coding: utf-8 -*-
"""b361_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THIS ACT'S WHOLE EVIDENCE IS QUOTATION**, and its locked registration says why the step matters
### more here than usual: ### **THIS SEAT READ `b358`'s BANK ONE ACT AGO AND THEREFORE CARRIES A
### ### RECOLLECTION OF THE HELD ITEM.** ### The extract is what keeps the recollection out of the record:
### every sentence this act quotes is the anchor tool's output, read from the file that ORIGINATED it.
### ### **BAR 1: A SENTENCE THIS ACT CANNOT LOCATE IS NOT QUOTED.**
### ### **BAR 2: THE CONSTANT'S DEFINITION MUST BE LOCATED AT CONTENT IN THE PINNED SOURCE.** ### The
### source reads below are that bar's evidence, and a value read from anywhere else is not a value.
"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b361_ferry_2026-09-07.txt')
B358 = d('b358_the_li_asymptotics.txt')
DRAFT = d('b360_closing.txt')
SRC = d('b358_source_lagarias0404394.txt')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- leg 1', 'ORDER', FERRY, 'LEG 1 (b361) \u2014 THE HELD ITEM, QUOTED THEN BRANCHED.'),
    ('the order -- (a), the quotation step', 'ORDER', FERRY,
     '(a) Quote from its own bank, verbatim with its location: the'),
    ('the order -- (b), the branch fixed before the quotation is seen', 'ORDER', FERRY,
     '(b) BRANCH, fixed here before the quotation is seen: if the'),
    ('the order -- the circularity clause governing both branches', 'ORDER', FERRY,
     'branch the circularity finding stands untouched: the tail'),
    ('the order -- the ledger condition', 'ORDER', FERRY,
     'grading table gives it, and the Li row updated through the'),

    # ---- (1) THE ITEM, AT ITS OWN BANK ---------------------------------------------------------------
    ('the item -- b358 gives it its own sentence', 'ITEM', B358, 'H-NGEK` DESERVES ITS OWN SENTENCE.'),
    ('the item -- the constant and where its determinant sits', 'ITEM', B358,
     '`K(\u03c0) = max_j |\u03ba_j(\u03c0)|\u00b2`, and the corpus HAS the gamma factor that determines'),
    ('the item -- one evaluation would decide it, and it is NOT ordered', 'ITEM', B358,
     'it, and ### **ONE EVALUATION WOULD DECIDE IT.** ### That is named here and is NOT ordered.'),

    # ---- (2) ITS GRADE, AS ITS OWN ACT LEFT IT -------------------------------------------------------
    ('the grade -- axis 2 counts, as b358 wrote them', 'GRADE', B358,
     "ON AXIS 2, AGAINST THE CORPUS'S OWN OBJECTS: `MET` 3"),
    ('the grade -- axis 1 counts, as b358 wrote them', 'GRADE', B358, 'ON AXIS 1, AGAINST THE SOURCES'),
    ('the grade -- the five that are UNDECIDABLE-FROM-THE-RECORD', 'GRADE', B358,
     'THE FIVE THAT ARE `UNDECIDABLE-FROM-THE-RECORD`'),
    ('the grade -- H-NGEK named among them, and why', 'GRADE', B358,
     'refute it; and ### `H-NGEK` is the interesting one'),
    ('the grade -- H-CUSP, which this act inherits and does not disturb', 'GRADE', B358,
     '`H-CUSP` (`\u03c0` cuspidal on `GL(N)`): the corpus'),

    # ---- (3) THE CAP CLAUSE THAT FORBADE DECIDING IT -------------------------------------------------
    ('the cap clause -- determined is not computed', 'CAP', B358,
     'THE RECORD ALREADY HOLDS. ### DETERMINED IS NOT COMPUTED**, the cap forbids this act'),

    # ---- (4) THE DRAFT'S PARKING CLAIM, QUOTED AS A CLAIM AND NOT AS A RULING ------------------------
    ('the draft -- the item it names', 'DRAFT', DRAFT, 'b361 -- `H-NGEK` DECIDED. ### **ONE EVALUATION'),
    ('the draft -- the claim that it lies outside the parking ruling', 'DRAFT', DRAFT,
     'the record already holds, ### **AND IT IS NOT AN INSTRUMENT RUN** -- no frame'),

    # ---- BAR 2: THE DEFINITION, AT CONTENT IN THE PINNED SOURCE --------------------------------------
    ('source -- the Euler product factorization (2.1)', 'SOURCE', SRC, '\u039b(s,\u03c0 ) := Q(\u03c0)'),
    ('source -- the archimedean factor (2.2)', 'SOURCE', SRC, '\u0393 R(s +\u03baj(\u03c0)), (2.2)'),
    ('source -- the kappa are certain constants', 'SOURCE', SRC,
     'in which \u03baj(\u03c0) are certain constants and'),
    ('source -- Gamma_R defined (2.3)', 'SOURCE', SRC, '\u0393 R(s) := \u03c0\u2212 s'),
    ('source -- the completed L-function of the trivial representation', 'SOURCE', SRC,
     '\u039b(s,\u03c0 triv ) = \u03c0\u2212 s'),
    ('source -- and it is the one representation that is not entire', 'SOURCE', SRC,
     '2 )\u03b6(s). This function has simple poles at s = 0 and s = 1.'),
    ("source -- the conductor of the trivial representation, stated", 'SOURCE', SRC,
     'using Q(\u03c0triv) = 1.'),
    ('source -- Theorem 5.1, and its own hypothesis', 'SOURCE', SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    ('source -- the index condition of Theorem 5.1', 'SOURCE', SRC,
     'the quantities S\u221e(n,\u03c0 ) are real-valued. There is a constant K(\u03c0) such that for n'),
    ('source -- the error term of (5.1)', 'SOURCE', SRC,
     'n logn +C1(\u03c0) n +O (N (K(\u03c0) + 1)). (5.1)'),
    ('source -- K(pi) defined (5.3), first half', 'SOURCE', SRC, 'K(\u03c0) = max'),
    ('source -- K(pi) defined (5.3), second half', 'SOURCE', SRC, '|\u03baj(\u03c0)|2, (5.3)'),
    ('source -- and the implied constant is ABSOLUTE', 'SOURCE', SRC,
     'and the implied constant in the O-notation is absolute.'),
    ('source -- the same condition restated inside the proof', 'SOURCE', SRC,
     'Now we suppose that n \u2265K(\u03c0) := max {|\u03bak(\u03c0)|2 : 1 \u2264k \u2264N }'),
    ("source -- the introduction's own version, for all n >= 1", 'SOURCE', SRC, 'that for all n \u2265 1,'),
    ("source -- the introduction's error term (1.12)", 'SOURCE', SRC,
     '2n logn +C1(\u03c0) n +O (1), (1.12)'),
    ("source -- and ITS implied constant DEPENDS ON pi", 'SOURCE', SRC,
     'and the implied constant in the O(1) term depends on \u03c0. Here'),

    # ---- THE LEDGER ROW THE ORDER CONDITIONS ON ------------------------------------------------------
    ('the row -- U1, where b358 and b359 put the tail finding', 'ROW', FACES, 'THE COUNTABLE FACE'),
    ("the row -- the deposit's refusal, which governs the ledger", 'ROW', FACES,
     "THE DEPOSIT'S REFUSAL GOVERNS THIS LEDGER"),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b361 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b361_extract_notes', LINES)
        return 2
    # ### **THE LOCAL SOURCE EXTRACT IS PINNED BY ITS OWN HASH.** ### `b358` pinned the PDF at
    # ### `86f3d3c4...`, 423379 bytes; the quotations below come from the TEXT EXTRACTED from it, and
    # ### **A HASH ON THE PDF DOES NOT CERTIFY THE RENDERING** (b353's seam). ### So the rendering this
    # ### act reads is pinned here too, and both pins are printed.
    h = hashlib.sha256(open(SRC, 'rb').read()).hexdigest()
    rec('')
    rec('  ### THE PIN ON THE RENDERING THIS ACT ACTUALLY READS:')
    rec('      %s' % os.path.basename(SRC))
    rec('      sha256 %s   %d bytes' % (h, os.path.getsize(SRC)))
    rec("      ### **b358 PINNED THE PDF AT `86f3d3c4...`, 423379 BYTES. ### A HASH ON A PDF DOES NOT")
    rec('      ### CERTIFY THAT ITS EXTRACTED TEXT IS A FAITHFUL RENDERING OF IT** -- b353\'s seam, and it')
    rec('      ### stands here: no bar in this act checks a transcription against the typeset original.')
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % str(e).replace(chr(10), ' | ')[:180])
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n, differs=bool(differs)))
        rec('')
        rec('  [%-6s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('=' * 100)
    p = run_clock.write(D, 'b361_extract_notes', LINES)
    io.open(d('b361_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built,
             source_file=os.path.basename(SRC), source_sha256=h, source_bytes=os.path.getsize(SRC),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
