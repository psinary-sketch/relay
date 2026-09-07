# -*- coding: utf-8 -*-
"""b350_filings.py -- ONE APPENDED BLOCK ON `OPEN_TRAILS.md`: THE TRAIL RESTATED, NOT DISCHARGED.

### ### **IT WRITES ONLY BECAUSE THE TRAIL'S STATE CHANGED**, and it refuses if `b350_price.json` does not say so.
### ### **NOTHING ABOVE THE BLOCK IS EDITED**, and the file is checked as a true prefix of what it was and of its
### committed blob. ### The trail's own two demands are quoted through the sortie's shared normaliser.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock    # noqa: E402
import quote_norm   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b350 trail update -->'
TRAIL = 'W-ORD-FLOOR-HELD-AXES'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def block(P):
    return [
        '', MARK, '',
        '### **`%s` — UPDATED 2026-09-07 (b350): THE PRICE HALF PAID, THE MEASUREMENT HALF OWED**' % TRAIL,
        '',
        ('*The block above is not edited. This one records what b350 paid and what it did not. **No frame was '
         'built, no ladder was run, no cell was evaluated and no axis was moved.***'),
        '',
        ('**What the trail asked for was two things** — the same movement measurement b344 made on `NY`, made on '
         '`tau` and on the taper; and the price, which its own text says can be read off b344’s printed figures '
         'without a single new frame. **b350 paid the second and did not attempt the first.**'),
        '',
        ('**The ladder’s cost, from the walls b344 printed:** `%s` seconds at the reference frame over the sealed '
         'rungs `%s` — **the same for either axis**, because a move is a ladder either way. What that buys is *one '
         'value*: what the residual does at one new threshold, or at one new taper, and not what it does across '
         'either axis.' % (('%.2f' % P['wall_total']), P['ladder'])),
        '',
        ('**The threshold’s room, computed from the printed figures with no new frame:** the intersection across '
         'the rungs of (largest eigenvalue dropped, smallest kept) is **`(%.6e, %.6e)`**, a factor of `%.2f` wide, '
         'and the corpus’s own `tau = %.1e` sits inside it — free to fall by a factor of `%.2f` or rise by a factor '
         'of `%.2f` with the same eigenvalues kept at every rung, and therefore the same rank. **And that is a fact '
         'about the CUT and not about the residual:** the same subspace kept does not mean the same residual, b344 '
         'printed no residual at a second threshold, and so the residual’s response to the threshold is **not '
         'priced by these figures**.'
         % (P['band_lo'], P['band_hi'], P['band_factor'], P['tau'], P['fall_factor'], P['rise_factor'])),
        '',
        ('**The taper’s room is not priceable from the printed figures at all.** `ALPHA` and `BETA` are printed as '
         'constants at every rung with nothing beside them — no second value, no neighbourhood, no interval, no '
         'derivative. **So the pricing is itself priced, as the order required:** two ladders, `%s` seconds of wall '
         'at the reference frame — and even that would yield a *difference* and not a *room*, because the taper has '
         'no analogue of the eigenvalue interval that gives the threshold one.' % ('%.2f' % P['taper_pricing_cost'])),
        '',
        ('**What each move would confound, in the sealed words of the act that declined it.** The threshold would '
         'confound the **rank** with the **floor** — moving it moves the stable cut, and b343 showed the rank '
         'constant across the grid axis, so a residual moving with the threshold could not be told from one moving '
         'with the rank; b319 records that the corpus’s threshold sits *57 times inside that separation*. The taper '
         'would confound the **instrument** with the **object** — `ALPHA` and `BETA` are the source’s own '
         'constants, so a taper moved is no longer the source’s object. **That is the harder confound, and it is '
         'why the cheapness of the ladder is not the whole price.**'),
        '',
        ('**And the floor: UNEXPLAINED.** The one axis that was moved does not account for it — b344 found the '
         'residual converges in `NY` with about a ninth of the floor left to travel — and for the two held axes the '
         'record contains no measurement of the residual at all. **Pricing is not measuring, and nothing priced '
         'here explains anything.** The unexplained part, named: the residual’s response to the threshold anywhere '
         'in its rank-preserving band, and to the taper at any value.'),
        '',
        ('*Species unchanged (**PRICE**); **RESTATED, NOT DISCHARGED** — a trail is not discharged by paying the '
         'cheaper half of it. Trigger: an act that moves either axis, which this one is not. Nothing here is a '
         'route. No grade moves. h2 stands exactly where the deposit left it.*'),
    ]


def main():
    P = json.load(io.open(os.path.join(D, 'b350_price.json'), encoding='utf-8'))
    rec('=' * 100)
    rec('b350_filings.py -- THE TRAIL RESTATED. ### APPEND-ONLY, AND ONLY BECAUSE ITS STATE CHANGED.')
    rec('=' * 100)
    rec('  the trail state as the pricing left it : %s' % P['trail'])
    if 'RESTATED' not in P['trail'] and 'DISCHARGED' not in P['trail']:
        rec('  ### ### **THE STATE DID NOT CHANGE. ### NOTHING IS WRITTEN.**')
        st, det, wrote = 'NOT FIRED', 'the trail state did not change', []
    else:
        txt = io.open(TRAILS, encoding='utf-8').read()
        if MARK in txt:
            st, det, wrote = 'DUPLICATE', 'mark already present -- REFUSED, nothing written', []
        elif TRAIL not in txt:
            st, det, wrote = 'REFUSED', 'the named trail is not in the file', []
        else:
            r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:OPEN_TRAILS.md'], capture_output=True)
            hb = r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None
            before = txt
            io.open(TRAILS, 'w', encoding='utf-8', newline=chr(10)).write(
                before.rstrip(chr(10)) + chr(10) + chr(10).join(block(P)) + chr(10))
            after = io.open(TRAILS, encoding='utf-8').read()
            pw = after.startswith(before.rstrip(chr(10)))
            pb = (hb is not None) and after.startswith(hb.rstrip(chr(10)))
            ok = after.count(MARK) == 1 and pw and pb
            st = 'WRITTEN' if ok else 'READ-BACK FAILED'
            det = 'mark %d time(s); append-only working=%s blob=%s' % (after.count(MARK), pw, pb)
            wrote = ['OPEN_TRAILS.md'] if ok else []
        rec('  OPEN_TRAILS.md : %s -- %s' % (st, det))
    tr = io.open(TRAILS, encoding='utf-8', errors='replace').read()
    blk = tr[tr.index(MARK):] if MARK in tr else ''
    rec("  the trail's two demands quoted through the shared normaliser :")
    rec('    the MEASUREMENT demand present in the file : %s'
        % quote_norm.contains(tr, 'the same movement measurement b344 made on `NY`, made on `tau` and on the taper'))
    rec('    the PRICE demand present in the file       : %s'
        % quote_norm.contains(tr, 'it can be read off the figures above without a single new frame'))
    rec('    the block says RESTATED, NOT DISCHARGED    : %s' % ('RESTATED, NOT DISCHARGED' in blk))
    rec('  ### PLACE-papers files written this run : %d (CAP 1)' % len(wrote))
    rec('=' * 100)
    p = run_clock.write(D, 'b350_filings_run', LINES)
    io.open(os.path.join(D, 'b350_filings.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(trails=st, detail=det, mark=MARK, trail=TRAIL, wrote=wrote,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    return 0 if st in ('WRITTEN', 'DUPLICATE', 'NOT FIRED') else 1


if __name__ == '__main__':
    sys.exit(main())
