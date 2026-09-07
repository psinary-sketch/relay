# -*- coding: utf-8 -*-
"""b350_extract.py -- THE EXTRACT STEP FOR THE FLOOR'S TWO HELD AXES, PRICED. ### **EVERY READ, TO DISK.**

### ### **WHAT THIS ACT IS READING FOR.** ### b344's TWO SEALED REASONS for not moving the cut's threshold and the
### taper, each quoted at the sealed file that states it, because the leg must say what each move would CONFOUND and
### the reasons are not this seat's to paraphrase. ### b319's own line on where the threshold sits relative to the
### separation it was chosen against. ### b316's naming of the taper's two constants as the source's own. ### b344's
### own conclusion about the one axis it did move, so the leg can say what remains unexplained without re-verdicting
### it. ### The trail's own text, since this leg either discharges it or restates it and must quote what it asked
### for. ### And the order's own sentences for this leg.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b350_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b350_ferry_2026-09-07.txt')

WANTED = [
    # ### ---- b344's TWO SEALED REASONS, AT THE SEALED FILE THAT STATES THEM
    ("b344 -- why NY and not the cut's tau", d('b344_registration_2026-09-06.txt'),
     "### ### **WHY `NY` AND NOT THE CUT'S `tau`:** ### moving `tau` moves the stable cut, and the cut's rank is"),
    ('b344 -- why NY and not the taper', d('b344_registration_2026-09-06.txt'),
     '### ### **WHY `NY` AND NOT THE TAPER:** ### the taper is `ALPHA` and `BETA`, and b316 records them as the'),
    ("### the taper's constants are the source's own", d('b344_registration_2026-09-06.txt'),
     "### source's own -- *\"Definition 4.4's `a`, at the source's own `S(1,1)`\"* and *\"Definition 4.4's `b`\"*."),
    ('b319 -- where the threshold sits inside the separation', t('b319_stable.py'),
     '# ### `TAU = 1e-6` therefore sits ### **57 TIMES INSIDE THAT SEPARATION** ### and ten orders of'),
    ("b316 -- the taper ALPHA at the source's own constant", t('b316_instrument.py'),
     "ALPHA = 1.0   # ### Definition 4.4's `a`, at the source's own `S(1,1)`"),
    # ### ---- b344's OWN CONCLUSION ABOUT THE AXIS IT DID MOVE
    ('b344 -- the residual moves with NY, of the size the floor requires', d('b344_the_floor_priced.txt'),
     '### ### **(1) THE RESIDUAL MOVES WITH `NY`, AND BY THE SEALED RULE THE MOVEMENT IS OF THE SIZE THE FLOOR'),
    ('b344 -- and it converges, the remaining travel about a ninth of the floor', d('b344_the_floor_priced.txt'),
     "### CORPUS'S OWN `NY = 512` THE REMAINING TRAVEL IS `7.059e-04`, about a ninth of the floor**; from"),
    ('b344 -- one axis moved is one axis moved', d('b344_the_floor_priced.txt'),
     '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    ('b344 -- the held axes printed at every rung', d('b344_the_floor_priced.txt'),
     "### later act can price them without re-running this one: the cut's `tau = 1.0e-06` in force, with `2`"),
    ('b339 -- the floor and its three candidate origins', d('b339_the_exponent_resolved.txt'),
     "### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut's `tau`, the"),
    # ### ---- THE TRAIL'S OWN TEXT
    ('the trail -- what is owed and the price as the record states it', os.path.join(PP, 'OPEN_TRAILS.md'),
     '**What is owed:** the same movement measurement b344 made on `NY`, made on `tau` and on the taper'),
    ('the trail -- nothing here is a route', os.path.join(PP, 'OPEN_TRAILS.md'),
     '*Nothing here is a route. No grade moves. h2 stands exactly where the deposit left it.*'),
    # ### ---- THE ORDER
    ('the order -- leg 2', FERRY, "LEG 2 (b350) — THE FLOOR'S TWO HELD AXES, PRICED from b344's"),
    ('### no frame built and no re-run', FERRY, 'printed figures with no frame built and no re-run: what'),
    ('### explained, partly explained, or unexplained', FERRY, 'moving them, quoted). Then state whether the floor is now'),
    ('### and if an axis cannot be priced, price the pricing', FERRY, 'axis, say so and price the pricing. The open trail is'),
    ("### the navigator's (L2)", FERRY, '(L2) the printed figures price one'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec("b350_extract.py -- THE FLOOR'S TWO HELD AXES, PRICED. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.")
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(TC, '<techne>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
