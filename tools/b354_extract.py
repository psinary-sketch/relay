# -*- coding: utf-8 -*-
"""b354_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR IS BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THIS IS THE FIRST ACT TO USE THE SORTIE'S STEP-ZERO TOOL.** ### The table below carries HINTS, not
### anchors. ### `anchor_from_file.anchor(path, hint)` finds the one line the hint matches after normalisation
### and returns ### **THE LINE AS THE FILE HOLDS IT, BYTE FOR BYTE**; that string is the anchor handed to
### `needle_pull`. ### A hint that matches nothing RAISES, and a hint that matches twice RAISES.
### ### **SO A MIS-TYPED ANCHOR IS NO LONGER POSSIBLE HERE.** ### A mis-typed HINT is still possible, and it
### fails loudly as a miss rather than quietly as a wrong quotation.
### ### **AND IT ALSO SIZES THE SIXTH FRAME BEFORE THE SEAL**, off the instrument's own shapes and not off
### prose, so the registration's chosen ceiling has a stated basis.
"""
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


# ### (label, tag, file, HINT -- typed however the seat likes; the anchor is READ from the file)
READS = [
    # ---- THE ORDER -------------------------------------------------------------------------------
    ('the order -- the sixth frame, as drafted, with two additions', 'ORDER', d('b354_ferry_2026-09-07.txt'),
     'LEG 1 (b354) - THE SIXTH FRAME, as drafted, with two additions.'),
    ('the order -- the ceiling is a CHOSEN number', 'ORDER', d('b354_ferry_2026-09-07.txt'),
     'ceiling is a CHOSEN number and the registration says so in'),
    ('the order -- a chosen ceiling is not a read one', 'ORDER', d('b354_ferry_2026-09-07.txt'),
     "act's measured walls, scaled) and the sentence that a chosen"),
    ('the order -- the SAME sealed criterion, not a new one', 'ORDER', d('b354_ferry_2026-09-07.txt'),
     'three models are refitted on six frames under the SAME sealed'),
    ('the order -- overrun is abandoned and reported as the finding', 'ORDER', d('b354_ferry_2026-09-07.txt'),
     'chosen ceiling it is abandoned and the overrun reported as the'),
    ('the order -- the anchor cure is BUILT in step zero', 'ORDER', d('b354_ferry_2026-09-07.txt'),
     'the cure b353 named is BUILT in this sortie'),

    # ---- WHAT b352 PRICED AND DID NOT RUN ---------------------------------------------------------
    ('b352 -- the binding cell needs six frames', 'b352', d('b352_the_fourth_candidate.txt'),
     'THE BINDING CELL NEEDS SIX FRAMES WHERE THE RECORD'),
    ('b352 -- the sixth frame sits inside the ceiling b339 sealed', 'b352', d('b352_the_fourth_candidate.txt'),
     'AND THAT SITS INSIDE THE CEILING b339 SEALED AT'),
    ('b352 -- unaffordable is a verdict about a question', 'b352', d('b352_the_fourth_candidate.txt'),
     'UNAFFORDABLE IS A VERDICT ABOUT A QUESTION AND NOT ABOUT A'),
    ('b352 -- a model winning a score is not a floor existing', 'b352', d('b352_the_fourth_candidate.txt'),
     'A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING.** ### The registration fixed'),
    ('b352 -- the third parameter costs 20 units at n = 5', 'b352', d('b352_the_fourth_candidate.txt'),
     'corrected information criterion charges'),
    ('b352 -- and it is a price and not a prediction', 'b352', d('b352_the_fourth_candidate.txt'),
     'AND IT IS A PRICE AND NOT A PREDICTION'),
    ('b352 -- the deafness of the five-frame ladder', 'b352', d('b352_the_fourth_candidate.txt'),
     'SO THIS LADDER IS DEAF TO ANY FLOOR SMALLER THAN ABOUT ONE PART IN A HUNDRED'),

    # ---- THE SEALED CRITERION, WHICH THIS ACT REUSES AND DOES NOT REPLACE -------------------------
    ('b352 -- the models, sealed before any fit', 'CRIT', d('b352_registration_2026-09-07.txt'),
     'M2 -- THE POWER LAW PLUS A CONSTANT FLOOR'),
    ('b352 -- the one criterion for all three', 'CRIT', d('b352_registration_2026-09-07.txt'),
     'ALL THREE MODELS ARE FITTED BY MINIMISING THE SUM OF SQUARED RESIDUALS OF'),
    ('b352 -- the selection criterion and its undefined case', 'CRIT', d('b352_registration_2026-09-07.txt'),
     'THE SELECTION CRITERION:'),
    ('b352 -- bar 1, distinguishable by score', 'CRIT', d('b352_registration_2026-09-07.txt'),
     'BAR 1 -- DISTINGUISHABLE BY SCORE'),
    ('b352 -- bar 2, a positive floor as one parameter', 'CRIT', d('b352_registration_2026-09-07.txt'),
     'BAR 2 -- A POSITIVE FLOOR, AS A STATEMENT ABOUT ONE PARAMETER'),

    # ---- THE INSTRUMENT, AND THE LADDER IT SITS ON -----------------------------------------------
    ('the domain axis, as b317 fixes it', 'INST', t('b317_smear.py'),
     'DOMAIN_AXIS = ((1024, 8.0, NY_FIXED), (2048, 16.0, NY_FIXED), (4096, 32.0, NY_FIXED),'),
    ('the transform matrix is NY by N', 'INST', t('b316_instrument.py'),
     'return 2.0 * np.cos(2.0 * math.pi * np.outer(self.y, self.x)) * self.w'),
    ('both cuts from ONE decomposition', 'INST', t('b319_stable.py'),
     'BOTH CUTS FROM ONE SVD'),
    ('b339 -- the domain ladder and its frames', 'INST', d('b339_price_run.txt'),
     "the domain ladder, b317's DOMAIN_AXIS : X = [8.0, 16.0, 32.0, 64.0, 128.0]"),
    ('b339 -- the verdict that stands', 'INST', d('b339_price_run.txt'),
     'THE GATE ON THE RUN (sealed): the cells whose X_req <= 512 : NONE -- UNAFFORDABLE'),
    ("b320 -- the frames table with each frame's rank", 'INST', d('b320_components_run.txt'),
     "(2a) THE FRAMES, ON b319's STABLE CUT, WITH THE RANK PRINTED."),

    # ---- THE STANDING RULES ----------------------------------------------------------------------
    ('b322 -- a price is not a prediction', 'RULE', d('b322_the_membership.txt'),
     'A PRICE IS NOT A PREDICTION.'),
    ('b345 -- a stopped run is banked as it stood', 'RULE', d('b345_the_li_control_rerun.txt'),
     'STOPPED'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b354 -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.** ### AND THE SIXTH FRAME, SIZED.')
    rec('=' * 100)

    # ================================================== THE TOOL'S OWN FIXTURES, BEFORE IT IS TRUSTED.
    rec('')
    rec("  ### ### **THE STEP-ZERO TOOL'S FIXTURES, RUN HERE BEFORE IT IS TRUSTED:**")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        rec('  ### ### **REFUSING TO BUILD ANCHORS FROM A TOOL THAT FAILS ITS OWN FIXTURES.**')
        run_clock.write(D, 'b354_extract_notes', LINES)
        return 2

    # ================================================== THE SIXTH FRAME, SIZED OFF THE INSTRUMENT.
    rec('')
    rec('  ### ### **THE SIXTH FRAME, SIZED BEFORE THE SEAL, OFF THE INSTRUMENT AND NOT OFF PROSE.**')
    import b316_instrument as INS
    import b317_smear as SM
    rec('    the ladder as b317 fixes it : %s' % (SM.DOMAIN_AXIS,))
    sizes = []
    for N, X in ((16384, 128.0), (32768, 256.0)):
        fr = INS.Frame(N, X, SM.NY_FIXED)
        lo_x, lo_y = fr.masks()
        free = int((~lo_x).sum())
        rows = int(lo_y.sum())
        cbytes = rows * free * 8
        sizes.append(dict(N=N, X=X, NY=SM.NY_FIXED, rows=rows, free=free, C_bytes=cbytes))
        rec('    N=%-6d X=%-6.1f NY=%-4d  C is %d x %d = %.1f MB'
            % (N, X, SM.NY_FIXED, rows, free, cbytes / 1e6))
    ratio = sizes[1]['C_bytes'] / float(sizes[0]['C_bytes'])
    rec('    ### ### **THE DECOMPOSED MATRIX IS `NY x free` WITH `NY = %d` FIXED**, so it grows LINEARLY'
        % SM.NY_FIXED)
    rec('    ### ### in `N` and not quadratically. ### The sixth frame is `%.2f` times the fifth by size,'
        % ratio)
    rec('    ### ### and its decomposition is `O(NY^2 * free)`, which scales the same way.')
    rec('    ### ### **THAT IS A SHAPE READ FROM THE CODE. ### IT IS NOT A MEASURED WALL, AND THE RECORD')
    rec('    ### ### CONTAINS NO MEASURED WALL FOR THIS LADDER.**')

    # ================================================== THE READS.
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
            rec('      %s' % e)
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE (this would be a real defect)** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.relpath(path, ROOT).replace(os.sep, '/'),
                          line=n, differs=bool(differs)))
        rec('')
        rec('  [%-5s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.relpath(path, ROOT).replace(os.sep, '/'), n, differs))
        rec('      | %s' % line.rstrip())
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### ### **ANCHORS THAT DIFFER FROM THE HINT THAT FOUND THEM : %d OF %d.**' % (ndiff, len(built)))
    rec('  ### ### Each of those is a sentence this seat would have mis-typed under the old method, and')
    rec('  ### ### **EACH WOULD HAVE READ AS A MISSING SENTENCE.**')
    rec('  ### ### **AN EXTRACT IS A QUOTATION AT A LINE. ### IT IS NOT A READING OF THE ARGUMENT AROUND IT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b354_extract_notes', LINES)
    io.open(d('b354_frames.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(sizes=sizes, size_ratio=ratio, ny=SM.NY_FIXED, ladder=[list(f) for f in SM.DOMAIN_AXIS],
             reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
