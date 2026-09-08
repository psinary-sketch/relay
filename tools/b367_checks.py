# -*- coding: utf-8 -*-
"""b367_checks.py -- THE GATE SUITE FOR THE SCAFFOLD REPAIR, NOT LOCATED.

### ### **EVERY ARM IS WRITTEN BY CONTENT AND NOT BY ADDRESS**, which is `b366`'s `(R2)` and is now law.
### `G-BYCONTENT` re-measures that on this act's own files with `b366`'s own detector, so the claim is a
### measurement and not a promise.
### ### ### **AND TWO ARMS ARE NAMED FOR WHAT THEY TEST, NOT FOR WHAT THE REGISTRATION EXPECTED.** ### The
### locked face listed `G-ROUTES` and `G-NOTBUY` against a priced pricing. ### **THE VERDICT REMOVED THEIR
### ### SUBJECT**, so they test what is actually true -- that the routes were NOT priced and that the bank
### says which branch was taken and why. ### **AN ARM KEPT POINTING AT A SUBJECT THAT NO LONGER EXISTS
### ### WOULD BE THE WRONG ARM** (`b365`'s module), and renaming it is not softening it: the predicate is
### strictly harder, because it now demands the absence be explained.
### ### **IT USES `gate_needle` AND `gate_text.flat` AND DEFINES NO FLATTENER OF ITS OWN** -- `b348`'s rule.
### ### **THE SIDES, BY `b352`:** ### `G-NOEDIT`'s and `G-NOBUILD`'s working-tree halves and `G-ROW`'s and
### `G-TRAIL`'s ancestry readings are read BEFORE THE PUSH; `G-HOOK`/`G-MIRROR` AFTER; `G-ORDER` is
### SIDE-INVARIANT.
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import gate_text         # noqa: E402
import run_clock         # noqa: E402
import gate_needle as GN  # noqa: E402
import b366_sweep as SW   # noqa: E402  ### (R2)'s DETECTOR, TURNED ON THIS ACT

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
GRHK = os.path.join('D:', os.sep, 'SIDE-grh-transfer')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b367_the_scaffold_repair.txt')
REG = d('b367_registration_2026-09-07.txt')
FERRY = d('b367_ferry_2026-09-07.txt')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
README = os.path.join(PP, 'README.md')
CORR, IDX = d('b367_corr_run.txt'), d('b367_index_run.txt')
SCAN, TERMSCAN, GATE = d('b367_ferry_scan.txt'), d('b367_reg_termscan.txt'), d('b367_reg_gate.txt')
CENSUS0, FCEN = d('b367_census_stepzero.txt'), d('b367_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b367_regspec_run.txt'), d('audit_b367_reg_satisfiable.txt')
PINS = d('b367_pins_stepzero.txt')
SEAL = '87c30063df6f1e0ef5ce50f1af807a378b7e8fc0e3496a4596b39de882c1b356'
ROWNUM = '216'
TRAIL_MARK = '<!-- b367 scaffold terminals not located -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b367_reads.json'), ('J', 'b367_locate.json'), ('F', 'b367_filing.json'))}

NEW_THIS_ACT = {'tools/b367_regspec.py', 'tools/b367_extract.py', 'tools/b367_locate.py',
                'tools/b367_filing.py', 'tools/b367_correspondence.py',
                'tools/b367_index_append.py', 'tools/b367_checks.py'}

TOOLNUM = [
    ('the refs, the live-vs-mention split and the sweep', 'tools/b367_locate.py'),
    ('the 35 reads and the 11 kernel lines', 'tools/b367_extract.py'),
    ('the trail block and its 4667 bytes', 'tools/b367_filing.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 216', 'tools/b367_correspondence.py'),
    ('the key', 'tools/b367_index_append.py'),
    ('54 clauses', 'tools/b367_regspec.py'),
    ('16953 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b367 - THE SCAFFOLD REPAIR: READ AND PRICED, NEVER A'),
    ('the order -- the cap', FERRY, 'CAP, quoted in the registration: ONE act; a location, a read'),
    ('the order -- NOT LOCATED stops the act', FERRY,
     'statement proved; NOT LOCATED stops the act, as the draft'),
    ('the order -- (H1) and (H2)', FERRY, 'from RECALL and NOT from any file: the kernel is SIDE-effects;'),
    ('the order -- (H3)', FERRY, 'excluding the generalized hypothesis and excluding an'),
    ('the order -- (H4)', FERRY, "exceptional real zero; and the kernel's working head may sit on"),
    ('the order -- why the ref must be stated', FERRY,
     'act read, since a read of main would miss a head that is not'),
    ('the order -- addition two', FERRY, 'ADDITION TWO - WHAT THEY ARE, quoted: each terminal'),
    ('the order -- addition three', FERRY, 'ADDITION THREE - THE THREE ROUTES, priced separately and none'),
    ('the order -- route (b) and the architecture it names', FERRY,
     'premise named in the row, which the record calls a legitimate'),
    ('the order -- addition four', FERRY, 'ADDITION FOUR - THE RECOMMENDATION IS THE AUTHOR'),
    ("the order -- the navigator's expectations", FERRY,
     'registered here: (F1) the terminals are located, on a non-main'),
    ("the kernel -- the module's own title", STRUCT, 'SIDE-EFFECTS — STRUCTURAL CONTENT'),
    ('the kernel -- what the audit found', STRUCT,
     'A Phase S.2–S.4 audit found those skeletons were either True-valued'),
    ('the kernel -- they compiled clean and said nothing', STRUCT,
     '0 sorry and 0 axioms but said nothing about their named problems,'),
    ('the kernel -- the retirement ledger heading', STRUCT,
     '-- RETIREMENT LEDGER (audit Phase S.2–S.4)'),
    ('the kernel -- the GRH entry', STRUCT,
     'exhaustiveness analog). (Retired: opaque-Prop `grh_exclusion`,'),
    ('the kernel -- the Landau-Siegel entry', STRUCT,
     'Classical-reduction from GRH; no dedicated kernel. (Retired:'),
    ('the front document -- its GRH layer line', AGENTS,
     '- **GRH layer**: `twist_cancels`, `formation_preserved_grh`, `grh_exclusion`'),
    ('the front document -- its Landau-Siegel layer line', AGENTS,
     '- **Landau-Siegel layer**: `no_ls_zero`'),
    ("the record -- the ferry's premise superseded once already", TRAILS,
     "THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED"),
    ('the record -- and the ban stands anyway', TRAILS,
     'exist cannot be cited — **and it stands anyway, because a name can return.***'),
    ('the record -- INTERFACES, and the architecture it sanctions', README,
     '- **INTERFACES** — the theorem takes the claim as a **named hypothesis**, discharged'),
    ('the record -- ENCODES-CONCLUSION / SHELL', README,
     '- **ENCODES-CONCLUSION / SHELL** — the theorem stipulates what the paper claims, or'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK,
     'NOT LOCATED. ### THE TERMINALS DO NOT EXIST, AND THE KERNEL SAYS SO ITSELF'),
    ('### every mention is inside a comment', BANK,
     'EVERY ONE OF THEM IS INSIDE A COMMENT** -- specifically inside'),
    ('### the record already found it', BANK,
     'AND THE RECORD ALREADY FOUND THIS, THIRTEEN DAYS AGO, AND SAID SO IN THESE WORDS'),
    ('### the cap stops the act', BANK, 'SO THE CAP GOVERNS: `NOT LOCATED stops the act`'),
    ('### the live defect is not the scaffold', BANK,
     'AND THERE IS A LIVE DEFECT HERE, BUT IT IS NOT THE ONE THE FERRY WAS SENT FOR'),
    ('### the refs, named', BANK, 'BRANCHES CARRYING WORK THE READ REF DOES NOT HAVE'),
    ('### and the hazard did not bite, as a measurement', BANK,
     'DID NOT BITE HERE**, and that is a measurement rather than an assurance'),
    ('### (H4) corrected', BANK, 'CORRECTED.** ### The'),
    ('### (H5) corrected, and the count never assumed', BANK,
     'CORRECTED, AND THE COUNT WAS NEVER ASSUMED'),
    ('### the right terminals and the wrong defect', BANK,
     'SO THE HINT NAMED THE RIGHT'),
    ('### there is no statement to quote', BANK,
     'THERE IS NO STATEMENT TO QUOTE, BECAUSE THERE IS NO DECLARATION'),
    ('### the species in one line', BANK,
     'AND THAT SENTENCE IS THE WHOLE SPECIES IN ONE LINE'),
    ('### no printed profile, and the reason', BANK,
     'A PROFILE IS A STATEMENT ABOUT A DECLARATION, AND NO SUCH DECLARATION EXISTS'),
    ('### no paper cites either as evidence', BANK,
     'AND THE FULL-PROMINENCE CLAUSE, ANSWERED: NO PAPER CITES EITHER ONE AS EVIDENCE'),
    ('### the ban stands because a name can return', BANK,
     'THAT LAST CLAUSE IS WHY THIS ACT IS NOT A WASTED ONE'),
    ('### the front document exports what the source dropped', BANK,
     'A DOCUMENT THAT SUMMARISES A SOURCE DRIFTS IN ONE DIRECTION ONLY'),
    ('### the routes are not priced, and the reason is not timidity', BANK,
     'AND THE REASON IS NOT TIMIDITY'),
    ('### route (c) is already what happened', BANK, 'AND ROUTE (c) IS ALREADY WHAT HAPPENED'),
    ('### the sanction reported, the recommendation withheld', BANK,
     'NO ROUTE IS RECOMMENDED. ### THE'),
    ('### and the class rule was always in force', BANK,
     'IT IS THE GENERAL RULE FOR'),
    ('### the branch taken', BANK, 'TAKEN: `(NOT LOCATED)`'),
    ('### and both others shown unreachable', BANK, '`(PARTLY LOCATED)` -- UNREACHABLE'),
    ('### not one byte of either kernel', BANK,
     'NOT ONE BYTE OF `SIDE-effects` OR `SIDE-grh-transfer`'),
    ('### the struck-clause counter was right beyond the lexical', BANK,
     'THE COUNT WAS PART OF THE HINT, AND A REGISTRATION THAT WROTE IT AS SETTLED'),
    ('### the scan that walked a vendored dependency', BANK,
     'A search that walks a vendored dependency is not searching the thing it was pointed at'),
    ('### the banned-stem scan fired inside a quotation', BANK,
     'A ### ### QUOTATION IS NOT AN EXEMPTION' if False else 'QUOTATION IS NOT AN EXEMPTION'),
    ("### b366's own bounded count was wrong, and did not say where its bound fell", BANK,
     'A BOUNDED SEARCH'),
    ('### (F1) refuted twice over', BANK, 'REFUTED TWICE OVER'),
    ('### (F2) unreachable, and the order’s own bar is why', BANK,
     'THERE IS NO STATEMENT TO READ**, so the act cannot'),
    ('### the seat predicted only its own procedure', BANK,
     'A SEAT THAT PREDICTS ONLY ITS OWN PROCEDURE HAS PREDICTED THE EASY'),
    ('### nothing claimed about the mathematics', BANK,
     'IT DOES NOT SAY EITHER IS OPEN, CLOSED, HARD OR EASY'),
]

MUST_FAIL = [
    ('the bank never says a terminal is replaced', BANK, '### A TERMINAL IS REPLACED.'),
    ('the bank never says the route is chosen', BANK, '### THE ROUTE IS CHOSEN.'),
    ('the bank never says a Lean file was written', BANK, '### A LEAN FILE WAS WRITTEN.'),
    ('the bank never says the scaffold is repaired', BANK, '### THE SCAFFOLD IS REPAIRED.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
    src2 = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src2)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and hasattr(n, 'lineno'):
            spans.append((n.lineno, n.end_lineno))
    keep = []
    for i, ln in enumerate(src2.split(chr(10)), 1):
        if any(a <= i <= b for a, b in spans):
            continue
        keep.append(ln.split('#')[0])
    return chr(10).join(keep)


def main():
    fails = []
    print('=' * 100)
    print('b367 -- GATE SUITE (THE SCAFFOLD REPAIR, NOT LOCATED)')
    print('=' * 100)
    extract = io.open(d(_J['E']['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### BUILT BY `gate_needle` FROM THE FILE THAT EMITTED THEM, AND EACH')
    print('  ### ALSO PRESENT IN THE RELIED-ON EXTRACT FILE:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, _line = GN.present(extract, path, hint)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES ### BUILT BY `gate_needle` FROM THIS ACT’S OWN BANK:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, NEVER normalised and never a substring):')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    E, J, F = _J['E'], _J['J'], _J['F']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    K = J['refs']['SIDE-effects']

    print(chr(10) + '  G-HINT (every hint clause reported CONFIRMED / CORRECTED / NOT LOCATED):')
    h = ['(H1)', '(H2)', '(H3)', '(H4)', '(H5)']
    h1 = all(('**%s' % x) in bank for x in h)
    h2 = all(w in bf for w in ('CONFIRMED', 'CORRECTED'))
    # ### **THE FIRST VERSION TYPED A RENDERING**: the bank's heading reads `THE HINT, SCORED.` and then
    # ### `AGAINST WHAT WAS FOUND, NOT THE OTHER WAY ROUND.` on the same flattened line, with a marker run
    # ### between them. ### The arm now asks for the phrase the bank actually carries.
    h3 = 'AGAINST WHAT WAS FOUND, NOT THE OTHER WAY ROUND' in bf
    h4 = 'THE HINT NAMED THE RIGHT TERMINALS AND THE WRONG DEFECT' in bf
    gh = h1 and h2 and h3 and h4
    print('    all five clauses appear with a status : %s ; both statuses used : %s' % (h1, h2))
    print('    ### **AND THE HINT IS SCORED AGAINST WHAT WAS FOUND** : %s' % h3)
    print('    and the characterisation is corrected : %s' % h4)
    print('    %s' % ('PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-HINT')

    print(chr(10) + '  G-REF (BAR 2: the ref read is named, and the refs not read are printed):')
    r1 = K['head'] in bank and K['branch'] in bank
    r2 = all(o['branch'] in bank for o in K['others'])
    r3 = J['branches_with_unread_work'] == 0 and 'BRANCHES CARRYING WORK THE READ REF DOES NOT HAVE' in bf
    r4 = (J['refs'].get('SIDE-grh-transfer') or {}).get('head', 'zz') in bank
    gr = r1 and r2 and r3 and r4
    print('    the read ref `%s` = `%s` is named in the bank : %s' % (K['branch'], K['head'], r1))
    print('    every ref NOT read is named : %s ; and what it carries is measured : %s' % (r2, r3))
    print('    the second kernel read is named too : %s' % r4)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-REF')

    print(chr(10) + '  G-LOCATED (BAR 1: the verdict follows the count, and nothing is described from the hint):')
    l1 = J['verdict'] in ('LOCATED AND PRICED', 'PARTLY LOCATED', 'NOT LOCATED')
    l2 = (J['verdict'] == 'NOT LOCATED') == (J['live_declarations'] == 0)
    l3 = J['all_mentions_in_comments'] is True and J['mentions'] > 0
    l4 = 'THERE IS NO STATEMENT TO QUOTE, BECAUSE THERE IS NO DECLARATION' in bf
    l5 = ('TAKEN: `(%s)`' % J['verdict']) in bank
    l6 = all(('`(%s)` -- UNREACHABLE' % b) in bank
             for b in ('LOCATED AND PRICED', 'PARTLY LOCATED') if b != J['verdict'])
    gl = l1 and l2 and l3 and l4 and l5 and l6
    print('    the verdict is one of the three fixed forms : %s (%r)' % (l1, J['verdict']))
    print('    ### **AND IT FOLLOWS FROM THE COUNT: %d LIVE DECLARATIONS** : %s'
          % (J['live_declarations'], l2))
    print('    every mention is inside a comment : %s ; the bank refuses to describe from the hint : %s'
          % (l3, l4))
    print('    the branch taken is named : %s ; the others shown unreachable : %s' % (l5, l6))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LOCATED')

    print(chr(10) + '  G-QUOTED (what the kernel says happened to them, quoted from the kernel):')
    q1 = 'Retired: opaque-Prop `grh_exclusion`' in bank
    q2 = 'opaque-Prop `no_ls_zero`' in bank
    q3 = '0 sorry and 0 axioms but said nothing about their named problems' in bf
    q4 = all(v['equal'] for v in F['quotes'].values())
    gq = q1 and q2 and q3 and q4
    print('    the GRH entry is quoted : %s ; the Landau-Siegel entry : %s' % (q1, q2))
    print("    the audit's own sentence is quoted : %s" % q3)
    print('    every filed quotation equal under the shared normaliser : %s' % q4)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED')

    print(chr(10) + '  G-PROFILE (the profile is READ or reported absent; never a compile):')
    p1 = 'NO PRINTED PROFILE' in bank
    p2 = 'A PROFILE IS A STATEMENT ABOUT A DECLARATION, AND NO SUCH DECLARATION EXISTS' in bf
    p3 = J['build_run'] is False
    gp = p1 and p2 and p3
    print('    the bank reports NO PRINTED PROFILE : %s ; with the reason : %s' % (p1, p2))
    print('    ### **AND NO BUILD WAS RUN** : %s' % p3)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PROFILE')

    print(chr(10) + '  G-CITES (the sweep is bounded, says where it looked, and answers the paper question):')
    c1 = len(J['sweep']) >= 4
    c2 = all(str(v) in bank or v == 0 for v in (J['sweep'].get('relay'), J['sweep'].get('PLACE-papers')))
    c3 = 'NO PAPER CITES EITHER ONE AS EVIDENCE' in bf
    c4 = 'AN ABSENCE FOUND BY THIS SEARCH IS AN ABSENCE FROM THOSE FIVE REPOSITORIES' in bf
    c5 = 'and it stands anyway, because a name can return' in trails
    gc = c1 and c2 and c3 and c4 and c5
    print('    repositories swept : %d : %s ; the counts are on the bank : %s' % (len(J['sweep']), c1, c2))
    print('    ### **THE FULL-PROMINENCE QUESTION IS ANSWERED** : %s' % c3)
    print('    the bound is stated : %s ; and the standing ban is quoted from the record : %s' % (c4, c5))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CITES')

    print(chr(10) + '  G-ROUTES (### **NOT PRICED** -- and the bank says which branch and why):')
    o1 = J['routes_priced'] == 0 and F['routes_priced'] == 0
    o2 = 'THE THREE ROUTES ARE NOT PRICED' in bf
    o3 = 'AND THE REASON IS NOT TIMIDITY' in bf
    o4 = 'ALL THREE TAKE THE TERMINAL AS THEIR INPUT, AND THERE IS NO' in bf
    o5 = 'AND ROUTE (c) IS ALREADY WHAT HAPPENED' in bf
    go = o1 and o2 and o3 and o4 and o5
    print('    routes priced : %d : %s ; the bank says so : %s' % (J['routes_priced'], o1, o2))
    print('    ### **AND IT GIVES THE REASON RATHER THAN THE ABSENCE** : %s / %s' % (o3, o4))
    print('    and it reports which route the record already took : %s' % o5)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ROUTES')

    print(chr(10) + '  G-NOCHOICE / G-SANCTION (the sanction reported; the recommendation withheld):')
    s1 = F.get('route_recommended') is None
    s2 = 'NO ROUTE IS RECOMMENDED' in bf and 'THE RECOMMENDATION IS THE AUTHOR' in bf
    s3 = 'a legitimate architecture, not a' in bank
    s4 = 'work-orders, not citations' in bank
    s5 = 'IT IS NOT A PRICING, BECAUSE NOTHING WAS PRICED' in bf
    s6 = GN.absent_exact(BANK, '### THE ROUTE IS CHOSEN.')
    gs = s1 and s2 and s3 and s4 and s5 and s6
    print('    no route recorded as recommended : %s ; the bank says so : %s' % (s1, s2))
    print("    ### **THE SANCTION IS QUOTED FROM THE RECORD** : %s ; and the third class too : %s"
          % (s3, s4))
    print('    and the report is marked as not a pricing : %s' % s5)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-NOCHOICE/G-SANCTION')

    print(chr(10) + '  G-NOBUILD (### **NOT ONE BYTE OF EITHER KERNEL**) ### READ BEFORE THE PUSH:')
    kd = git(KERNEL, 'status', '--porcelain').strip()
    gd = git(GRHK, 'status', '--porcelain').strip()
    n1 = not kd and not gd
    n2 = F['kernel_clean'] is True
    n3 = J['lean_written'] == 0 and J['build_run'] is False
    n4 = K['head'] == git(KERNEL, 'rev-parse', '--short', 'HEAD').strip()
    gnb = n1 and n2 and n3 and n4
    print('    SIDE-effects working tree clean : %s ; SIDE-grh-transfer clean : %s' % (not kd, not gd))
    print('    the filing recorded it too : %s ; lean files written : %d ; build run : %s'
          % (n2, J['lean_written'], J['build_run']))
    print('    ### **AND THE KERNEL HEAD IS STILL THE ONE THAT WAS READ** : %s (`%s`)' % (n4, K['head']))
    print('    %s' % ('PASS' if gnb else '### FAIL ###'))
    if not gnb:
        fails.append('G-NOBUILD')

    print(chr(10) + '  G-BYCONTENT (### **(R2): NO ARM OF THIS ACT IS WRITTEN BY ADDRESS**):')
    mine = [t(x) for x in sorted(os.listdir(os.path.join(ROOT, 'tools'))) if x.startswith('b367_')]
    selfhits = []
    for p in mine:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    SELF_DECLARED = {
        ('b367_correspondence.py', 'last-row cells'):
            'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE -- to count its cells; '
            'the same shape `b366` classified NOT AN ADDRESS PREDICATE at `b326` and `b335`.',
    }

    def which(fn, code):
        if fn == 'b367_correspondence.py' and '[-1:]' in code:
            return 'last-row cells'
        return None
    undeclared = []
    for fn, i, code in selfhits:
        key = (fn, which(fn, code))
        print('    %-26s line %-6d | %s' % (fn, i, code))
        if key[1] is None or key not in SELF_DECLARED:
            undeclared.append((fn, i))
            print('        ### ### **UNDECLARED HIT.**')
        else:
            print('        %s' % SELF_DECLARED[key])
    gbc = not undeclared
    print('    ### hits in this act’s own files : %d ; declared with a reason : %d ; UNDECLARED : %d'
          % (len(selfhits), len(selfhits) - len(undeclared), len(undeclared)))
    print('    %s' % ('PASS' if gbc else '### FAIL ###'))
    if not gbc:
        fails.append('G-BYCONTENT')

    print(chr(10) + '  G-NOEDIT (only this act’s papers path; no other act’s files) ### BEFORE THE PUSH:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/gate_content.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py',
             'tools/b366_sweep.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').splitlines()
              if x.strip() and 'b367' not in x and x.strip() != 'tools/banked_index.py']
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'OPEN_TRAILS.md']
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    gne = (not touched and not others and not ppbad and faces_clean and hand and fnd)
    print('    owner instruments modified : %s' % (touched or 'none'))
    print("    ### **TRACKED RELAY FILES OF OTHER ACTS MODIFIED : %s**" % (others or 'none'))
    print('    papers paths beyond OPEN_TRAILS.md : %s' % (ppbad or 'none'))
    print('    ### **FACES_LEDGER.md UNTOUCHED, BECAUSE NO ROW MOVED** : %s' % faces_clean)
    print('    HANDOFF clean : %s ; FINDINGS clean : %s' % (hand, fnd))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-TRAIL (one append-only block; b157’s block not edited) ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    t3 = F['prefix_of_file'] and F['prefix_of_blob']
    t4 = F['status'] == 'NOT LOCATED'
    t5 = trails.count("THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED") == 1
    gt = t1 and t2 and t3 and t4 and t5
    print('    the mark appears once : %s ; the committed blob is a true prefix : %s' % (t1, t2))
    print('    the writer recorded append-only both ways : %s ; marked %s : %s' % (t3, F['status'], t4))
    print("    ### **AND b157's SENTENCE IS STILL THERE, EXACTLY ONCE, UNEDITED** : %s" % t5)
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason) ### BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'THERE WAS NOTHING TO PRICE' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTREPAIRED:')
    irun = io.open(IDX, encoding='utf-8').read()
    kk1 = 'READ BACK : scaffold-not-located returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the terminals are replaced', 'a route is chosen',
               'the scaffold is repaired', 'the kernel was written'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gkk = kk1 and kk2 and kk3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (kk1, kk2, kk3))
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTREPAIRED')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock) ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1b = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1b = o1b and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2b = stampm is not None
    o3b = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, J, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4b = 'JOINTLY SATISFIABLE' in sat
    o5b = 'LOCKED BEFORE ANY READ OF THE KERNEL' in gate_text.flat(reg)
    gob = o1b and o2b and o3b and o4b and o5b
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1b, stampm.group(1) if stampm else 'none', o2b))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3b)
    print('        lock %s ; extract %s ; locate %s ; filing %s'
          % (stampm.group(1) if stampm else '?', E['run_clock'], J['run_clock'], F['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE ANY READ : %s'
          % (o4b, o5b))
    print('    %s' % ('PASS' if gob else '### FAIL ###'))
    if not gob:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b367_hooks.txt'), d('b367_mirror.txt')
    gh2 = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror clean : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    cl = re.search(r'clauses\s*:\s*(\d+)', sat)
    sm = re.search(r'### bytes locked : (\d+)', reg)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [
        ('live declarations %d' % J['live_declarations'],
         ('KERNEL: `%d`' % J['live_declarations']) in bank),
        ('mentions %d' % J['mentions'], ('%d mentions' % J['mentions']) in bank or
         ('Three mentions' in bank and J['mentions'] == 3)),
        ('front exported %d' % J['front_exported'], ('%d NAMED THEOREMS' % J['front_exported']) in bank),
        ('front absent %d' % len(J['front_absent']), ('`%d`\n### ARE ABSENT' % len(J['front_absent'])
                                                      ).replace(chr(10) + '### ', ' ') in ' '.join(bank.split())),
        ('the read ref', K['head'] in bank),
        ('sweep relay %d' % J['sweep'].get('relay', -1), ('`%d` hits' % J['sweep']['relay']) in bank or
         ('`%d` hits in `%d` tracked' % (J['sweep']['relay'], len(J['sweep_files']['relay']))) in bank),
        ('the trail block grew the file by %d bytes' % F['grew'], str(F['grew']) in bank),
        ('reads %d' % E['reads'], ('%d reads' % E['reads']) in bank),
        ('without an anchor %d' % E['without_anchor'],
         ('%d without an anchor' % E['without_anchor']) in bank),
        ('anchors differing %d of %d' % (E['anchors_differing'], E['reads']),
         ('%d of %d anchors differing' % (E['anchors_differing'], E['reads'])) in bf),
        ('kernel lines %d' % E['kernel_lines'], ('%d lines located inside the kernel' % E['kernel_lines'])
         in bf),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on locate run file', J['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks):')
    once = True
    for lbl, jf in (('extract', E), ('locate', J), ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-8s %-26s clock on disk %s == the JSON's %s : %s"
              % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    repeats = sorted(f for f in os.listdir(D) if re.match(r'^b367_extract_notes\d*\.txt$', f))
    named = all(f in bank for f in repeats)
    once = once and named
    print('    ### **EVERY REPEAT IS NAMED IN THE BANK : %s** %s' % (named, repeats))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed about the object, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    mymods = ('b367_regspec.py', 'b367_extract.py', 'b367_locate.py', 'b367_filing.py',
              'b367_correspondence.py', 'b367_index_append.py', 'b367_checks.py')
    for p in [t(x) for x in mymods]:
        src3 = strip_prose(p)
        for b in banned:
            if b in src3:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b367_locate.py', 'b367_extract.py',
                                                       'b367_filing.py'))]
    gnc = not hits and not imports
    print("    numerical calls in this act's STRIPPED sources : %d %s" % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    # ### **A FILE IS SWEPT AS THIS SEAT'S PROSE OR DECLARED AS A CARRIER OF ANOTHER'S WORDS. ### NEVER
    # ### BOTH**, which the first version of this suite did -- and a file counted twice is a file whose
    # ### carrier declaration does nothing.
    OWNED = [BANK, REG, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS, GATE,
             d('b367_satisfiable.json'),
             t('b367_regspec.py'), t('b367_extract.py'), t('b367_filing.py'),
             t('b367_correspondence.py'), t('b367_index_append.py')]
    CARRIERS = [
        (t('b367_checks.py'), 'its own fixtures'),
        (FERRY, "IT IS THE ORDER -- not this act's writing"),
        (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
        (d(E['run_file']), "the extract file carries the kernel's own words"),
        (d(J['run_file']), "the locate file carries the kernel's own words"),
        (d(F['run_file']), "the filing file carries the kernel's own quoted sentence"),
        (t('b367_locate.py'), "ITS SEARCH STRINGS ARE THE FRONT DOCUMENT'S OWN HEADINGS -- a search "
                              "string is a needle, and b348 says the needle is never softened"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for hh in (ch + sh)[:6]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE SCAFFOLD REPAIR, NOT LOCATED (b367).'
    nxt = '# ### THE DATED-ARM SWEEP (b366).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    blk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk),
                      ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-20s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the trail block, the index row):')
    tmpdir = tempfile.mkdtemp(prefix='b367_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles refused : %d ; owner needles not in the extract file : %d' % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
