# -*- coding: utf-8 -*-
"""b322_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE -- `membership` -- AND THE ACT ADDS `resolving-power`**, because the
### lore gained a rule here and a rule nobody can find is a rule nobody has.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTSETTLED`.** ### A reader who asks *is the unit in
### the space* must be handed, in the same breath, that this act ### **DID NOT SETTLE IT** ### and
### what it would cost to. ### The row that answered *the residual falls, and its exponent matches
### the truncation prediction* and stopped would be a true sentence assembled to give a false
### impression: the arms disagree, the noise gate refuses every step, and no unit is adopted.

### ### **`the archimedean membership` STAYS UNKEYED, AND THAT IS DELIBERATE.** ### b321 left it
### unkeyed because it decided nothing about it. ### **THIS ACT ALSO DECIDES NOTHING ABOUT IT** --
### it prices the question instead -- so the alias that would answer *is it a member* must keep
### returning NO KEY while the alias that asks *what would settle it* returns a row.
### ### **THE INDEX IS SWEPT FOR STEMS AFTER THE WRITE** (b305's defect, caught at b306).
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NL = chr(10)

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'membership': ['the membership', 'the residual ladder', 'the two realizations',\n"
    "                   'why is the residual not zero', 'is the unit in the space',\n"
    "                   'the truncation tail'],\n"
    "    'resolving-power': ['the resolving power', 'under-resolved',\n"
    "                        'what would settle it', 'the price of a question',\n"
    "                        'is it open or under-resolved'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE LADDER, AND THE TRUNCATION TAIL THAT PREDICTS IT (b322).\n"
    "    (\"membership\", \"b322 (reads at owners, a definitional decision, and one measurement)\",\n"
    "     \"the unit's membership residual run along the DOMAIN ladder at stable rank, and fitted.\"\n"
    "     \" ### b319 measured it constant at 0.4395 across four GRID refinements and reported a\"\n"
    "     \" domain course without fitting it. ### **THE RESIDUAL FALLS AT EVERY STEP** -- 0.797250,\"\n"
    "     \" 0.644963, 0.439502, 0.286136, 0.197491 at X = 8 to 128, ranks 20, 37, 69, 133, 262 --\"\n"
    "     \" so by a bar sealed BEFORE any definition was unfolded, **THE RESIDUAL IS THE\"\n"
    "     \" TRUNCATION'S AND b300's DERIVATION IS NOT CONTRADICTED BY IT**. ### Fitted exponent\"\n"
    "     \" **p = -0.519901**, and a SECOND ROUTE SHARING NO CODE predicts it: max x u(x) beyond\"\n"
    "     \" X/2 is 1.118582, so u decays like 1/x, so the L2 mass beyond X goes like X^-1/2 --\"\n"
    "     \" predicted -0.500000, **AGREE**. ### Eight constituents unfolded side by side, neither in\"\n"
    "     \" the other's language; two differ, CONDITION TWO and THE DOMAIN, and **THEY ARE NOT\"\n"
    "     \" INDEPENDENT**: the first is what the second produces\",\n"
    "     \"### A FALLING COURSE AT FIVE FRAMES IS A FALLING COURSE AT FIVE FRAMES. ### **THE ACT\"\n"
    "     \" DID NOT SETTLE THE MEMBERSHIP AND DOES NOT CLAIM TO** -- the arms DISAGREE, the\"\n"
    "     \" noise-floor gate REFUSES 4 of 4 steps, and the SIZE of no value on the ladder is\"\n"
    "     \" certified. ### **THE RATE HALF OF THE REGISTERED EXPECTATION IS REFUTED**: against\"\n"
    "     \" b321's instrument exponent q = -1.324018 by the same fitter on the same domains,\"\n"
    "     \" p/q = 0.392669, outside the sealed band [0.5, 2.0]. ### **NO UNIT IS ADOPTED AND NONE\"\n"
    "     \" IS REPLACED.** ### b300 stands at DERIVES-on-IMPORTS; b316 and b319 stand at theirs.\"\n"
    "     \" ### W-ORD-PHI-MU-L2 stays OPEN and the instrument cannot see it. ### NO ACT\"\n"
    "     \" RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b322_the_membership.txt; data/b322_components_run.txt;\"\n"
    "     \" tools/b322_ladder.py (the emitting file); CORRESPONDENCE.md row 156\"),\n"
    "    # ### THE RULE, AND THE VERDICT THAT TOOK THE WEAKER BRANCH (b322).\n"
    "    (\"resolving-power\", \"b322 (the verdict, and two of its own sealed bars found defective)\",\n"
    "     \"a question is UNDER-RESOLVED, not open, when the candidates sit closer together than the\"\n"
    "     \" instrument's distance from the answer -- **AND THE PRICE IS THE RATIO**. ### b321 bought\"\n"
    "     \" the rule one act earlier: its identity control HELD and still could not tell two\"\n"
    "     \" exponent copies apart, which were 0.000981 to 0.003994 apart where the instrument sat\"\n"
    "     \" 0.018808 to 0.023224 from the answer. ### **THIS ACT IS ITS FIRST DELIBERATE\"\n"
    "     \" APPLICATION**: the membership question is priced rather than decided -- from\"\n"
    "     \" p = -0.519901 and the residual 0.197491 at X = 128, the domain at which it would reach\"\n"
    "     \" 0.01 is **X = 3.973e+04, a factor of 3.104e+02** beyond what was reached, labelled as an\"\n"
    "     \" extrapolation of a fitted slope\",\n"
    "     \"### A QUESTION THAT CARRIES ITS PRICE IS NOT A QUESTION ANSWERED. ### **TWO OF THIS\"\n"
    "     \" ACT'S OWN SEALED BARS WERE FOUND DEFECTIVE AND NEITHER WAS EDITED.** ### (B2)'s\"\n"
    "     \" dichotomy IS NOT A PARTITION: b316's taper smooths the DISCONTINUITY at the domain's\"\n"
    "     \" end and does not restore the mass BEYOND it, so a reading of THE VECTOR means NOT THE\"\n"
    "     \" EDGE DISCONTINUITY and not NOT THE TRUNCATION. ### (B5)'s branches ARE NOT MUTUALLY\"\n"
    "     \" EXCLUSIVE: two fired at once and the seal did not order them, so the runner's if/elif\"\n"
    "     \" chain picked DIFFERENT VECTORS on an ordering that was the tool's and not the seal's.\"\n"
    "     \" ### **THE ACT TOOK THE WEAKER BRANCH, UNDER-RESOLVED**, because between two branches a\"\n"
    "     \" defective rule licenses equally an act may not help itself to the stronger one. ###\"\n"
    "     \" W-ORD-ARCH-MEMBERSHIP IS NOT CLOSED. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b322_the_membership.txt; data/b322_registration_2026-09-04.txt (sealed);\"\n"
    "     \" data/b321_the_window_opened.txt (the incident); CORRESPONDENCE.md row 157\"),\n"
)

NEW_KEYS = ('membership', 'resolving-power')
ALIASES = ('the membership', 'the residual ladder', 'the two realizations',
           'why is the residual not zero', 'is the unit in the space', 'the truncation tail',
           'the resolving power', 'under-resolved', 'what would settle it',
           'the price of a question', 'is it open or under-resolved')
MUST_NOT_HIT = ('the archimedean membership', 'the window class')


def no_key(out):
    for ln in (out or '').splitlines():
        if ln.strip().startswith('### NO KEY'):
            return True
    return False


def verdict_fixture():
    real = no_key('=====' + NL + '  ### NO KEY.' + NL + '  ### matched no DECLARED key')
    quoted = no_key('    grade    : ... every query that would have found b268 returned NO KEY.')
    return real, quoted


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b322 -- THE INDEX KEYS. ### THE MEMBERSHIP, AND THE RESOLVING POWER.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-24s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
    written = not (all(have_key.values()) and all(have_row.values()))
    if not written:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2

    if written:
        new = txt
        if not all(have_key.values()):
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not all(have_row.values()):
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)

    rv, qv = verdict_fixture()
    print('  VERDICT FIXTURE : fires on the index\'s own NO KEY line : %s ;'
          ' quiet on the phrase quoted inside a row : %s' % (rv, not qv))
    ok = rv and not qv

    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    for k in NEW_KEYS:
        out, rc = query(k)
        good = (not no_key(out)) and (k in out) and rc == 0
        ok = ok and good
        print('    %-24s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-42s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### ### **G-NOTSETTLED -- THE ARM THIS FILE EXISTS FOR.**')
    out, _rc = query('is the unit in the space')
    unsettled = 'DID NOT SETTLE THE MEMBERSHIP' in out
    disagree = 'DISAGREE' in out
    ok = ok and unsettled and disagree
    print('    the answer says the act did NOT settle it     : %s' % unsettled)
    print('    ### and that the arms disagree                 : %s' % disagree)
    out2, _rc2 = query('what would settle it')
    priced = '3.973e+04' in out2 or '3.104e+02' in out2
    ok = ok and priced
    print('    and *what would settle it* returns the price   : %s' % priced)
    print('  ### **A ROW THAT ANSWERED *is the unit in the space* WITH A FALLING COURSE AND STOPPED')
    print('  ### ### WOULD BE A TRUE SENTENCE ASSEMBLED TO GIVE A FALSE IMPRESSION.**')

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the archimedean membership` STAYS UNKEYED BECAUSE THIS ACT DECIDED NOTHING')
    print('  ### ### ABOUT IT.** ### It priced the question; it did not answer it.')

    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    for h in sh:
        print('      line %d  %s' % (h[1], h[3][:96]))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
