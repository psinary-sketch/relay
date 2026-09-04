# -*- coding: utf-8 -*-
"""b325_index_append.py -- TWO KEYS, THREE ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTDISCREDITED`.** ### A reader who asks
### *does the instrument see a failing hypothesis* must be handed ### **NOT AT THE ARC'S CELLS** ###
### together with the STRUCTURAL reason (the form represents nothing between 1 and 4) and the PRICED
### reach (the sign crosses at `a ~ 22`). ### A row that handed back `DOES NOT SEE IT` and stopped
### would turn a scope statement into a capability statement.

### ### **AND THE SECOND ARM IS `G-NOTIMPEACHED`.** ### A reader who asks about the positive
### control must be handed that it FIRED, what it caught, and -- in the same breath -- that
### ### **b321 IS NOT RE-VERDICTED**: the eleven-prime list is sufficient at b321's own cells and the
### two channels agree there to every printed digit.

### ### **`the archimedean membership` AND `the window class` STAY UNKEYED.** ### This act decides
### nothing about either.
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
    "    'negative-control': ['the negative control', 'a failing hypothesis',\n"
    "                         'does the instrument see a failing hypothesis',\n"
    "                         'the priced reach', 'the positive control',\n"
    "                         'the inherited constant', 'what the zeta window was',\n"
    "                         'can the instrument say no'],\n"
    "    'epstein': ['epstein', 'the epstein case', 'the epstein zeta',\n"
    "                'the confinement keystone', 'the class-number-3 form', 'disc -23',\n"
    "                'the off-line zeros', 'the on-line zero library'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE NEGATIVE CONTROL -- THE VERDICT (b325).\n"
    "    (\"negative-control\", \"b325 (a read, a pricing, and the run; the verdict)\",\n"
    "     \"the archimedean instrument aimed at a hypothesis KNOWN TO FAIL: the Epstein zeta of\"\n"
    "     \" x^2 + xy + 6y^2 (disc -23, h = 3), whose corpus census banks two zeros off the line.\"\n"
    "     \" ### The places sum SUM_v W_v = PR_Q - A_Q is **NEGATIVE AT ALL THIRTEEN OF THE ARC'S\"\n"
    "     \" CELLS**, -16.069614947 down to -2.243190916; the order's falsifier asked for the\"\n"
    "     \" forbidden POSITIVE sign and no cell gives one. ### **VERDICT: DOES NOT SEE IT AT THE\"\n"
    "     \" ARC'S CELLS. THE REGISTERED EXPECTATION IS REFUTED AT THE CURRENT REACH.** ### **AND\"\n"
    "     \" THE REASON IS STRUCTURAL**: r_Q(2) = r_Q(3) = 0, so the finite channel is identically\"\n"
    "     \" zero until a = 2 and still 0.006348865 against an archimedean 2.249539781 at a = 3.\"\n"
    "     \" ### **THE REACH IS PRICED**: beyond the arc's cells the sign CROSSES TO POSITIVE AT\"\n"
    "     \" a ~ 22 and stays positive at 24, 28, 32, 50, while zeta stays permitted everywhere\",\n"
    "     \"### A SCOPE STATEMENT IS NOT A CAPABILITY STATEMENT. ### The instrument does not see\"\n"
    "     \" THIS failure AT THE ARC'S CELLS; it is not shown unable to see a failure. ### **THE\"\n"
    "     \" CROSSING IS A PRICE, NOT A SEES-IT VERDICT**: the order's verdict needs the zero side\"\n"
    "     \" as corroboration and the corpus owns only the OFF-line Epstein zeros (its census began\"\n"
    "     \" at sigma = 0.52). ### **WHAT THE ZETA WINDOW WAS, AT EXACTLY ITS SCOPE**: a window\"\n"
    "     \" whose sign carried no arithmetic information at the widths it was taken at -- b321\"\n"
    "     \" said so before counting, and this act confirms that scope from the outside with an\"\n"
    "     \" object whose answer is known. ### NOTHING ABOUT ZETA, h2, OR THE ROSTER. ### NO GRADE\"\n"
    "     \" MOVED. ### NO ACT RE-VERDICTED. ### M-2 UNCHANGED\",\n"
    "     \"data/b325_the_negative_control.txt; data/b325_run.txt; tools/b325_epstein.py;\"\n"
    "     \" data/b325_registration_2026-09-04.txt (section (0) declares the deviation);\"\n"
    "     \" CORRESPONDENCE.md row 162\"),\n"
    "    # ### THE NEGATIVE CONTROL -- THE CONTROL THAT FIRED (b325).\n"
    "    (\"negative-control\", \"b325 (the positive control, and what it caught)\",\n"
    "     \"zeta run through the same channels is a control whose correct answer b321 proved: for\"\n"
    "     \" a lawful f the zeta places sum is -Z with Z a sum of squared moduli, NEVER POSITIVE.\"\n"
    "     \" ### At a = 32 it came out +0.003489041. ### **THE CAUSE IS b321_window.PRIMES =\"\n"
    "     \" (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)**, copied from the atlas's own prime loop and\"\n"
    "     \" sufficient where b321 used it (its widest cell has f supported below 9); at a = 32\"\n"
    "     \" the support reaches 1024. ### **WITH EVERY PRIME THE VALUE IS -0.000389214 AND THE\"\n"
    "     \" CONTROL PASSES AT EVERY WIDTH TESTED.** ### A second latent defect found and NOT\"\n"
    "     \" repaired in the owner: carto_atlas.kernel memoises without keying on its grid --\"\n"
    "     \" guarded in the caller, reported\",\n"
    "     \"### **b321 IS NOT RE-VERDICTED.** ### At the arc's own cells the eleven-prime and\"\n"
    "     \" every-prime channels agree to every printed digit (-0.315810512 at a = 3 from both).\"\n"
    "     \" The constant is scope-bound and the scope was never written down; this is the act\"\n"
    "     \" where it bit. ### **AND THIS ACT DECLARES THREE FAILINGS OF ITS OWN**: (A) the seat\"\n"
    "     \" RAN AHEAD of its own EXECUTION block -- the registration was sealed after the run,\"\n"
    "     \" declared as its section (0) with every bar marked [ORDER] or [SEAT, POST-HOC]; (B)\"\n"
    "     \" the satisfiability checker REFUSED to seal a mis-typed clause and was right; (C) the\"\n"
    "     \" noise-floor gate was first fed adjacent cells rather than a refinement pair, repaired\"\n"
    "     \" to the same cell at two resolutions, all three RESOLVED. ### NO GRADE MOVED. ### NO\"\n"
    "     \" OWNER INSTRUMENT EDITED. ### M-2 UNCHANGED\",\n"
    "     \"data/b325_the_negative_control.txt; data/b325_run.txt (fixtures (viii)-(ix));\"\n"
    "     \" data/b325_regspec_run.txt (the refusal); tools/b321_window.py line 51 (the constant);\"\n"
    "     \" CORRESPONDENCE.md row 163\"),\n"
    "    # ### THE EPSTEIN CASE, READ AT CONTENT AND PRICED (b325).\n"
    "    (\"epstein\", \"b325 (the read and the pricing)\",\n"
    "     \"the confinement keystone's Epstein case: the principal form x^2 + xy + 6y^2, disc -23,\"\n"
    "     \" h(-23) = 3, named in the corpus's own census header. ### The ledger the keystone calls\"\n"
    "     \" positive is the LI one (lambda_n) -- positivity of the coefficient sequence, not of\"\n"
    "     \" the zeros. ### The zeros come from the corpus's argument-principle census,\"\n"
    "     \" epstein_census.py, 2-D by construction: 450 cells over sigma in [0.52, 1.50],\"\n"
    "     \" t in [0.5, 33.0], **TWO ZEROS, BOTH OFF THE LINE** (sigma in [0.94, 1.08] at\"\n"
    "     \" t in [16.0, 16.5]; sigma in [0.66, 0.80] at t in [29.5, 30.0]). ### **THE PRICING,\"\n"
    "     \" TYPED**: the archimedean factor (sqrt23/2pi)^s Gamma(s) is NOT zeta's\"\n"
    "     \" pi^-s/2 Gamma(s/2) -- the corpus says so in its own METHOD header -- so the kernel\"\n"
    "     \" was BUILT from the quoted factor; the finite side is the coefficient sequence of\"\n"
    "     \" -Z_Q'/Z_Q, BUILT from r_Q by Dirichlet inversion (they differ by up to 15.74 below\"\n"
    "     \" n = 60); the lawful class TRANSFERS (poles at s = 0, 1; pole term -5.03e-17)\",\n"
    "     \"### THE FALSIFIER FITS INSIDE THE ACT; THE TWO NAMED CONTROLS DO NOT. ### The\"\n"
    "     \" explicit-formula control is BLOCKED on the on-line zero library, which the corpus\"\n"
    "     \" does not own (the census was hunting off-line zeros and started at sigma = 0.52);\"\n"
    "     \" Theorem 1's archimedean control does not cover Z_Q at all -- a hypothesis, not a\"\n"
    "     \" cost. ### **THE ON-LINE LIBRARY IS PRICED AT ONE ACT WITH THE TOOL ALREADY WRITTEN**:\"\n"
    "     \" re-run the census over sigma in [0.45, 0.52] and refine each winding cell. ### The\"\n"
    "     \" keystone's own finding -- *the functional equation illuminates the critical line; it\"\n"
    "     \" does not confine zeros to it* -- is the PREMISE of this test, not its subject, and\"\n"
    "     \" stands unchanged. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b325_the_negative_control.txt; data/b325_extract_notes.txt;\"\n"
    "     \" tools/e16/epstein_census.py (METHOD header); tools/e16/epstein_census_bank.jsonl;\"\n"
    "     \" PLACE-papers/day1/Which_Structure_Confines.md (the emitting keystone, internal copy);\"\n"
    "     \" CORRESPONDENCE.md row 162\"),\n"
)

NEW_KEYS = ('negative-control', 'epstein')
ALIASES = ('the negative control', 'does the instrument see a failing hypothesis',
           'the priced reach', 'the positive control', 'the inherited constant',
           'what the zeta window was', 'can the instrument say no',
           'epstein', 'the epstein case', 'the confinement keystone', 'the class-number-3 form',
           'the on-line zero library')
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
    print('b325 -- THE INDEX KEYS. ### THE NEGATIVE CONTROL, AND THE EPSTEIN CASE.')
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
    need = {'negative-control': 2, 'epstein': 1}
    for k in NEW_KEYS:
        out, rc = query(k)
        good = (not no_key(out)) and (k in out) and rc == 0
        n = out.count('act      :')
        enough = n >= need[k]
        ok = ok and good and enough
        print('    %-24s returns a row : %s ; returns %d row(s), %d required  %s'
              % (k, good, n, need[k], 'PASS' if (good and enough) else '### FAIL ###'))
    print('  ### **BOTH negative-control ROWS ARE REQUIRED.** ### An index that handed back the')
    print('  ### verdict without the control that fired would be answering *what was found* and')
    print('  ### hiding *what the finding cost*.')

    print('  ### THE ALIASES (each must reach one of THIS act\'s keys, not merely any key):')
    for q in ALIASES:
        out, _rc = query(q)
        good = (not no_key(out)) and any(k in out for k in NEW_KEYS)
        ok = ok and good
        print('    %-46s reaches a b325 key : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### ### **G-NOTDISCREDITED -- THE ARM THIS FILE EXISTS FOR.**')
    out, _rc = query('does the instrument see a failing hypothesis')
    no = 'DOES NOT SEE IT AT THE' in out
    why = 'r_Q(2) = r_Q(3) = 0' in out
    price = 'a ~ 22' in out
    scope = 'A SCOPE STATEMENT IS NOT A CAPABILITY STATEMENT' in out
    ok = ok and no and why and price and scope
    print('    the answer says NOT AT THE ARC\'S CELLS            : %s' % no)
    print('    ### and gives the structural reason               : %s' % why)
    print('    ### and the priced reach                          : %s' % price)
    print('    ### and refuses the capability reading BY NAME    : %s' % scope)
    print('  ### **A ROW THAT HANDED BACK `DOES NOT SEE IT` AND STOPPED WOULD TURN A SCOPE')
    print('  ### ### STATEMENT INTO A CAPABILITY STATEMENT.**')
    print('  ### ### **G-NOTIMPEACHED -- THE SECOND ARM.**')
    out2, _rc2 = query('the positive control')
    fired = '+0.003489041' in out2
    unm = 'b321 IS NOT RE-VERDICTED' in out2
    own = 'THREE FAILINGS OF ITS OWN' in out2
    ok = ok and fired and unm and own
    print('    the answer says the control FIRED, with the value : %s' % fired)
    print('    ### and that b321 is NOT re-verdicted             : %s' % unm)
    print('    ### and carries this act\'s own three failings     : %s' % own)
    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the archimedean membership` AND `the window class` STAY UNKEYED: THIS ACT')
    print('  ### ### DECIDED NOTHING ABOUT EITHER.**')

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
