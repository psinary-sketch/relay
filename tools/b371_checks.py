# -*- coding: utf-8 -*-
"""b371_checks.py -- THE GATE SUITE FOR THE FIRST TARGET, THE DESK CLOSED, THE GUARD MOVED.

### ### **`G-NOEDIT` IS RESTATED, NOT SOFTENED:** ### one owner instrument was licensed and is named;
### any other moving is still a failure.
### ### **`G-POLARITY` RE-READS THE EXERCISER'S OWN RECORD AND `G-HOOKPATH` RE-READS THE FILESYSTEM**,
### so the claim that the guard is tracked is measured here and not taken from the mover's JSON.
### ### **THE SIDES, BY `b352`:** ### `G-NOEDIT`'s, `G-TRAIL`'s and `G-ROW`'s working-tree and ancestry
### readings are BEFORE THE PUSH; the hook and the mirror AFTER; `G-ORDER` is SIDE-INVARIANT. ### **AND
### ### ANY ARM THAT WOULD TEST A DIRTY TREE IS SIDE-DEPENDENT AND SAYS SO** (`b370`'s incident (vi)).
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
import hedge_audit        # noqa: E402
import ferry_scan         # noqa: E402
import banned_terms       # noqa: E402
import b306_stem_scope    # noqa: E402
import b317_checks as K7   # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN   # noqa: E402
import b366_sweep as SW    # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-effects')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b371_the_first_target.txt')
REG = d('b371_registration_2026-09-08.txt')
FERRY = d('b371_ferry_2026-09-08.txt')
CORR, IDX = d('b371_corr_run.txt'), d('b371_index_run.txt')
SCAN, TERMSCAN, GATE = d('b371_ferry_scan.txt'), d('b371_reg_termscan.txt'), d('b371_reg_gate.txt')
CENSUS0, FCEN = d('b371_census_stepzero.txt'), d('b371_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b371_regspec_run.txt'), d('audit_b371_reg_satisfiable.txt')
PINS0 = d('b371_pins_stepzero.txt')
SEAL = '24d35c83d8719109cde830a8a7207cac7189d24a20d92dc2c245eba039c146e0'
ROWNUM = '220'
TRAIL_MARK = '<!-- b371 the desk closes: scaffold-terminals, the anchored arms, the hook -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b371_reads.json'), ('S', 'b371_settle.json'),
                   ('R', 'b371_repair_desc.json'), ('I', 'b371_inventory.json'),
                   ('H', 'b371_hookpath.json'), ('Q', 'b371_desk.json'),
                   ('F', 'b371_filing.json'))}

LICENSED = {'tools/b304_hooks.py'}
NEW_THIS_ACT = {'tools/b371_regspec.py', 'tools/b371_extract.py', 'tools/b371_reg_gate.py',
                'tools/b371_settle.py', 'tools/b371_repair_desc.py', 'tools/b371_inventory.py',
                'tools/b371_hookpath.py', 'tools/b371_desk.py', 'tools/b371_filing.py',
                'tools/b371_bank.py', 'tools/b371_correspondence.py',
                'tools/b371_index_append.py', 'tools/b371_checks.py'}

TOOLNUM = [
    ('the two refs and the deciding equality', 'tools/b371_settle.py'),
    ('the repair and its read-back', 'tools/b371_repair_desc.py'),
    ('the declared predicate, the sweep and the price', 'tools/b371_inventory.py'),
    ('the guard moved and exercised', 'tools/b371_hookpath.py'),
    ('(R7), with every closure naming a killing file', 'tools/b371_desk.py'),
    ('the closures filed', 'tools/b371_filing.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b371_bank.py'),
    ('the 30 reads', 'tools/b371_extract.py'),
    ('the three-arm registration gate', 'tools/b371_reg_gate.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 220', 'tools/b371_correspondence.py'),
    ('the key', 'tools/b371_index_append.py'),
    ('the clause spec', 'tools/b371_regspec.py'),
    ('19007 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('the guard exercised across four', 'tools/b304_hooks.py'),
    ('the pins across four', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, "ACT b371 - THE AUDIT'S FIRST TARGET, THE DESK CLOSED, THE HOOK"),
    ('the order -- (R6)', FERRY, '(R6) THE AUDIT IS RE-SCOPED TO WHAT IS CITED. Its first pass is'),
    ('the order -- (R7)', FERRY, '(R7) THE DESK CLOSES ITEMS. An item whose occasion is gone'),
    ('the order -- component 1', FERRY, "kernel's public description names a Core terminal count. Read"),
    ('the order -- the two words', FERRY, 'now carries, and settle it: SCOPE-DEPENDENT (the two words'),
    ('the order -- component 2', FERRY, 'COMPONENT 2 - THE ROW INVENTORY, LISTED AND NOT CHECKED: under'),
    ('the order -- audit nothing', FERRY, 'whether the kernel has moved since). Audit nothing.'),
    ('the order -- component 3', FERRY, 'COMPONENT 3 - THE HOOK MADE DURABLE OR STRUCK: the pre-push'),
    ('the order -- not both', FERRY, 'reason. Not both, and the choice is made by what the tracked'),
    ("the order -- the navigator's expectation", FERRY,
     "navigator's expectation: the count claim is SCOPE-DEPENDENT and"),
    ('the kernel README -- the Core line', os.path.join(SIDE, 'README.md'),
     '- **`Core/`** — the vanilla load-bearing layer:'),
    ("the kernel's correspondence -- the tag count sentence", os.path.join(SIDE, 'CORRESPONDENCE.md'),
     'audit at v0.1.0 (103 + 11 = 114 exactly), and each act'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK, 'AND THE NAVIGATOR`S EXPECTATION IS REFUTED ON ITS'),
    ('### the same thing at different refs', BANK,
     'SO THE TWO COUNT THE SAME THING AT DIFFERENT REFS, NOT DIFFERENT THINGS'),
    ('### the test was fixed before the read', BANK,
     'THE TEST WAS FIXED BEFORE THE READ, BECAUSE THIS IS WHERE A SEAT WOULD FIT A NUMBER TO A'),
    ('### the coincidence refused', BANK,
     'AND THE ARITHMETIC COINCIDENCE IS REPORTED AS A COINCIDENCE AND NOT PROMOTED TO A SCOPE.'),
    ('### the description carried no qualifier', BANK, 'THE DESCRIPTION CARRIED NO QUALIFIER AT ALL'),
    ('### a description has no history', BANK,
     'A DESCRIPTION HAS NO HISTORY AND NOTHING ELSE WILL REMEMBER IT'),
    ('### the count removed rather than updated', BANK,
     'THE COUNT IS REMOVED RATHER THAN UPDATED, AND THAT IS THIS SEAT`S JUDGEMENT, FLAGGED'),
    ('### the adjacent finding is the sharper half', BANK,
     'IT IS SHARPER THAN THE DESCRIPTION BECAUSE THE `README` IS A TRACKED FILE AND THE'),
    # ### **THE FIRST NEEDLE WAS AMBIGUOUS TWO WAYS** -- the bank states the pair in its answer and
    # ### again in its own section. ### The tool REFUSED it, which is the tool working.
    ('### rows listed and not checked', BANK,
     'ROWS CHECKED : `0`. ### KERNELS OPENED : `0`. ### COMPLETENESS CLAIMED'),
    ('### the pinless set is a finding', BANK,
     'AND THE PINLESS SET IS A FINDING, NOT A HOLE IN THE SWEEP.'),
    ('### the cross-reference is not a check', BANK,
     'COMPARING A NAME AGAINST A'),
    ('### a row so flagged is not thereby wrong', BANK,
     'A ROW SO FLAGGED IS NOT THEREBY WRONG.'),
    ('### one ranking factor cannot be filled', BANK, 'AND ONE FACTOR CANNOT BE FILLED WITHOUT'),
    ('### the guard chosen by a test', BANK, 'AND IT WAS CHOSEN BY A TEST AND NOT BY PREFERENCE'),
    ('### a clone is still not guarded', BANK, 'A FRESH CLONE STILL'),
    ('### a smaller hole and not no hole', BANK, 'A smaller hole, and not no hole.'),
    ('### the old location a net and a trap', BANK, 'A SAFETY NET AND A TRAP'),
    ('### the exerciser followed the guard', BANK,
     'AND THE EXERCISER FOLLOWED THE GUARD IN THE SAME ACT.'),
    ("### the act's own repair created a stale surface", BANK,
     'AND ONE THING THIS ACT BROKE AND DID NOT FIX'),
    ('### the desk closed for the first time', BANK,
     'AND THIS IS THE FIRST TIME THE NUMBER HAS MOVED.'),
    ('### a closure without a killing file is an opinion', BANK,
     'A CLOSURE WITHOUT A KILLING FILE IS AN OPINION'),
    ('### none of the three acts is re-verdicted', BANK,
     'AND NONE OF THOSE THREE ACTS IS RE-VERDICTED.'),
    ('### one closure flagged as this act`s own', BANK,
     'ONE CLOSURE IS FLAGGED BECAUSE ITS KILLING FILE IS THIS ACT`S OWN'),
    ('### the navigator`s expectation splits', BANK, 'SPLIT, AND THE SPLIT IS THE INTERESTING PART.'),
    ('### (E1) half met half refuted', BANK, 'HALF MET, HALF REFUTED.'),
    ('### the seat predicted its own next command', BANK,
     'A SEAT THAT PREDICTS ITS OWN NEXT COMMAND HAS PREDICTED NOTHING.'),
    ('### the placeholder split, twice in this act', BANK,
     'AND IT HAPPENED TWICE IN THIS ACT: ONCE IN THE REPAIR TOOL, AND THEN AGAIN IN THIS'),
]

MUST_FAIL = [
    ('the bank never says a row was checked', BANK, '### A ROW WAS CHECKED.'),
    ('the bank never says a kernel was opened for a row', BANK, '### A KERNEL WAS OPENED FOR A ROW.'),
    ('the bank never says a build was run', BANK, '### A BUILD WAS RUN.'),
    ('the bank never says a clone runs the hook', BANK, '### A CLONE RUNS THE HOOK.'),
    ('the bank never says an item closed without a file', BANK, '### AN ITEM CLOSED WITHOUT A FILE.'),
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
    print('b371 -- GATE SUITE (THE FIRST TARGET, THE DESK CLOSED, THE GUARD MOVED)')
    print('=' * 100)
    E, S, R, I, H, Q, F = (_J['E'], _J['S'], _J['R'], _J['I'], _J['H'], _J['Q'], _J['F'])
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 230:
                inx = line.rstrip()[:230] in extract
                trunc = bool(inx)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '  ### -- ITS RECORDED PREFIX' if trunc
                                    else ('' if inx else '  -- NOT IN THE EXTRACT FILE')))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES:')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()

    print(chr(10) + '  G-REF / G-PROFILE (BAR 2: the profile at a named ref and against its blob):')
    now = git(SIDE, 'rev-parse', 'HEAD').strip()
    p1 = S['pinned'] is True and S['head'] == S['ls_remote']
    p2 = S['blob_equals_working'] is True
    p3 = S['prints_at_head'] == S['prints_at_head_all']
    p4 = S['tag'] is not None and S['prints_at_tag'] is not None
    p5 = S['head'] == now
    gp = p1 and p2 and p3 and p4 and p5
    print('    ls-remote equals HEAD at the read : %s ; head unmoved since : %s' % (p1, p5))
    print('    ### **THE BLOB AND THE WORKING FILE AGREE : %s** ; every line zero-axiom : %s' % (p2, p3))
    print('    the tag and its count are both read : %s (`%s` -> %s)' % (p4, S['tag'],
                                                                          S['prints_at_tag']))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-REF/G-PROFILE')

    print(chr(10) + '  G-SETTLED / G-SCOPEQUOTED (BAR 1: one of two words, on a stated sentence):')
    s1 = S['verdict'] in ('SCOPE-DEPENDENT', 'STALE')
    s2 = (S['verdict'] == 'STALE') == bool(S['same_quantity'])
    s3 = len(S['scope_statements']) >= 2 and all(x['quote'] for x in S['scope_statements'])
    s4 = 'A SUM THAT HAPPENS TO MATCH IS NOT A SCOPE' in gate_text.flat(reg)
    s5 = S['qualifiers'] == []
    gs = s1 and s2 and s3 and s4 and s5
    print('    the verdict is one of the two ruled words : %s (%r)' % (s1, S['verdict']))
    print('    ### **AND IT FOLLOWS FROM THE DECIDING EQUALITY, NOT FROM PREFERENCE** : %s' % s2)
    print('    the scope candidates were sought in documents that STATE them : %s (%d located)'
          % (s3, len(S['scope_statements'])))
    print('    the registration fixed the test before the read : %s' % s4)
    print('    ### **AND THE DESCRIPTION CARRIED NO QUALIFIER AT ALL** : %s %s' % (s5, S['qualifiers']))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SETTLED/G-SCOPEQUOTED')

    print(chr(10) + '  G-NOBUILD (the profile was READ, never recomputed):')
    n1 = S['build_run'] is False
    src = ' '.join(strip_prose(t(x)) for x in ('b371_settle.py', 'b371_repair_desc.py'))
    n2 = 'lake' not in src and 'AllPrints' not in src
    kdirty = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip()]
    n3 = not [x for x in kdirty if x.strip().endswith('.lean')]
    gn = n1 and n2 and n3
    print('    build run : %s ; no build invocation in stripped sources : %s' % (S['build_run'], n2))
    print('    ### **AND NO `.lean` FILE IS DIRTY IN THE CONSTRUCTION KERNEL** : %s' % n3)
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOBUILD')

    print(chr(10) + '  G-ADJACENT (the README finding is reported and NOT repaired):')
    a1 = S['adjacent_repaired'] is False
    a2 = S['readme_headline'] != S['readme_breakdown_sum']
    a3 = not git(SIDE, 'diff', '--name-only', 'HEAD', '--', 'README.md').strip()
    a4 = 'SHARPER HALF' in bf and 'ROUTED' in bank
    ga = a1 and a2 and a3 and a4
    print('    the writer recorded it as not repaired : %s ; headline vs breakdown : %s vs %s'
          % (a1, S['readme_headline'], S['readme_breakdown_sum']))
    print('    ### **AND THE README IS UNTOUCHED IN THE WORKING TREE** : %s' % a3)
    print('    the bank calls it the sharper half and routes it : %s' % a4)
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ADJACENT')

    print(chr(10) + '  G-INVENTORY / G-NOAUDIT / G-PINLESS (BAR 3):')
    i1 = I['rows_checked'] == 0 and I['kernels_opened'] == 0
    i2 = I['completeness_claimed'] is False
    i3 = I['rows'] == I['with_pin'] + I['without_pin']
    i4 = all(r['kernels'] and r['terminals'] for r in I['inventory'])
    i5 = all(bool(r['pins']) == r['has_pin'] for r in I['inventory'])
    isrc = strip_prose(t('b371_inventory.py'))
    i6 = 'checkout' not in isrc and 'clone' not in isrc and 'rev-parse' not in isrc
    gi = i1 and i2 and i3 and i4 and i5 and i6
    print('    rows checked %d ; kernels opened %d' % (I['rows_checked'], I['kernels_opened']))
    print('    completeness claimed : %s ; the split partitions the set : %s' % (I['completeness_claimed'],
                                                                                 i3))
    print('    every inventoried row really names a kernel and a terminal : %s' % i4)
    print('    ### **AND has_pin AGREES WITH THE PINS RECORDED, ROW BY ROW** : %s' % i5)
    print('    ### **AND THE TOOL RESOLVES NO REF AND FETCHES NOTHING** (stripped code) : %s' % i6)
    print('    %s' % ('PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-INVENTORY/G-NOAUDIT/G-PINLESS')

    print(chr(10) + '  G-PRICE / G-RANK / G-CROSSREF:')
    c1 = I['price_parts'] == 3
    c2 = I['criterion'] == ['pin age', 'count rather than terminal', 'kernel moved since']
    c3 = 'NOT FILLED' in I['factor_c']
    c4 = I['flagged_count'] == len(I['flagged'])
    c5 = 'NOT A CHECK' in bf or 'not a check' in bank
    gc = c1 and c2 and c3 and c4 and c5
    print('    three price parts : %s ; the criterion is the order\'s : %s' % (c1, c2))
    print('    ### **AND THE FACTOR THAT NEEDS A KERNEL IS RECORDED NOT FILLED** : %s' % c3)
    print('    the cross-reference count matches its list : %s ; and is marked not a check : %s'
          % (c4, c5))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-PRICE/G-RANK/G-CROSSREF')

    print(chr(10) + '  G-HOOKPATH / G-POLARITY / G-RESIDUAL (BAR 4) ### RE-MEASURED HERE:')
    src_b = open(t(os.path.join('git-hooks', 'pre-push')), 'rb').read()
    reps = {'relay': ROOT, 'SIDE-global-section': SIDE, 'PLACE-papers': PP, 'SIDE-effects': KER}
    tracked, ident, cfgok = [], [], []
    for nm, rp in reps.items():
        f = os.path.join(rp, H['tracked_dir'], 'pre-push')
        ident.append(os.path.exists(f) and open(f, 'rb').read() == src_b)
        tracked.append(bool(git(rp, 'ls-files', '--', '%s/pre-push' % H['tracked_dir']).strip()))
        cfgok.append(git(rp, 'config', '--get', 'core.hooksPath').strip() == H['tracked_dir'])
    h1 = all(ident) and all(tracked) and all(cfgok)
    h2 = H['outcome'] == 'MADE DURABLE' and not H['failing']
    h2 = h2 and H.get('polarity_bar_met_by', '').startswith('tools/b304_hooks.py')
    # ### **THE POLARITY BAR IS MET BY THE POST-PUSH EXERCISER, NOT BY THE MOVER**, because the mover
    # ### refuses a dirty tree -- which is the cure for the incident this act caused. ### So this arm
    # ### reads `b304_hooks.py`'s own record and requires the mover to have DEFERRED rather than pretended.
    hk0 = io.open(d('b371_hooks.txt'), encoding='utf-8', errors='replace').read()         if os.path.exists(d('b371_hooks.txt')) else ''
    h3 = (all(v['negative']['ok'] and v['positive']['ok'] and v['head_unmoved'] and v['branch_restored']
              for v in H['exercise'].values() if v.get('exercised'))
          and ('### REPOS FAILING : 0' in hk0))
    h4 = H['clone_is_guarded'] is False and H['residual_named'] is True
    h5 = H['old_location_deleted'] is False and all(H['old_location_present'].values())
    gh = h1 and h2 and h3 and h4 and h5
    print('    tracked in every repo : %s ; byte-identical : %s ; hooksPath set : %s'
          % (all(tracked), all(ident), all(cfgok)))
    print('    ### **BOTH POLARITIES CORRECT, HEAD UNMOVED, BRANCH RESTORED, EVERYWHERE** : %s' % h3)
    print('    ### **AND THE ACT DOES NOT CLAIM A CLONE IS GUARDED** : %s ; residual named : %s'
          % (not H['clone_is_guarded'], H['residual_named']))
    print('    the old location is left in place : %s' % h5)
    print('    %s' % ('PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-HOOKPATH/G-POLARITY/G-RESIDUAL')

    print(chr(10) + '  G-EXERCISER (the checker followed the guard):')
    ex = io.open(t('b304_hooks.py'), encoding='utf-8').read()
    x1 = "HOOKS_DIR = '%s'" % H['tracked_dir'] in ex
    x2 = "'.git', 'hooks', 'pre-push'" not in strip_prose(t('b304_hooks.py'))
    x3 = 'GUARD_WITH_NOTHING_LISTENING' in ex
    hk = io.open(d('b371_hooks.txt'), encoding='utf-8', errors='replace').read() \
        if os.path.exists(d('b371_hooks.txt')) else ''
    x4 = 'REPOS FAILING : 0' in hk and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in hk
    gx = x1 and x2 and x3 and x4
    print('    the exerciser names the tracked dir : %s ; the old path is gone from its code : %s'
          % (x1, x2))
    print('    ### **AND IT NAMES THE SPECIES IT WOULD OTHERWISE HAVE BECOME** : %s' % x3)
    print('    its own run record passes : %s' % x4)
    print('    %s' % ('PASS' if gx else '### FAIL ###'))
    if not gx:
        fails.append('G-EXERCISER')

    print(chr(10) + '  G-CLOSED / G-KILLFILE / G-STANDS (BAR 5):')
    k1 = Q['items'] == Q['closed'] + Q['standing'] + Q['unconfirmed']
    k2 = Q['closed'] > 0
    k3 = all(m.get('killing_file') and m.get('exists') and m.get('carries') and m.get('date')
             for m in Q['marks'] if m['disposition'] == 'CLOSE')
    k4 = all(m.get('why') for m in Q['marks'] if m['disposition'] == 'STAND')
    k5 = Q['acts_reverdicted'] == 0
    # ### **AND EVERY KILLING FILE IS RE-READ HERE, NOT TAKEN FROM THE SWEEP'S JSON.**
    bad = []
    for m in Q['marks']:
        if m['disposition'] != 'CLOSE':
            continue
        p = d(m['killing_file'])
        if not os.path.exists(p) or GN.norm(m['sentence']) not in GN.norm(
                io.open(p, encoding='utf-8', errors='replace').read()):
            bad.append(m['killing_file'])
    k6 = not bad
    gk = k1 and k2 and k3 and k4 and k5 and k6
    print('    the dispositions partition the desk : %s (%d = %d + %d + %d)'
          % (k1, Q['items'], Q['closed'], Q['standing'], Q['unconfirmed']))
    print('    every closure names a file that exists and carries its sentence : %s' % k3)
    print('    ### **AND EVERY KILLING FILE IS RE-READ HERE** : %s %s' % (k6, bad or ''))
    print('    every standing item gives a reason : %s ; acts re-verdicted : %d' % (k4, Q['acts_reverdicted']))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-CLOSED/G-KILLFILE/G-STANDS')

    print(chr(10) + '  G-TRAIL (one append-only block; no block above edited) ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    t3 = F['prefix_of_file'] and F['prefix_of_blob'] and F['placeholders'] == 0
    t4 = all(F['names_prior'])
    t5 = F['status'] == 'CLOSED' and F['closed'] == Q['closed']
    t6 = trails.count("THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED") == 1
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    the mark appears once : %s ; blob is a true prefix : %s' % (t1, t2))
    print('    append-only both ways, no placeholders : %s ; names the prior blocks : %s' % (t3, t4))
    print("    ### **SCAFFOLD-TERMINALS IS CLOSED** : %s ; b157's sentence still there once : %s"
          % (t5, t6))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW (row %s) ### BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'EXACT WHEN IT WAS WRITTEN' in rows[0]
            and 'NO ROW WAS CHECKED' in rows[0] and 'A CLONE IS NOT GUARDED' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW')

    print(chr(10) + '  G-KEY / G-NOTCHECKED:')
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    kk1 = 'READ BACK : count-claim-stale returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the rows are checked', 'the clone is guarded', 'the readme is repaired',
               'the federation is audited'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    kk4 = 'LISTED AND NOT CHECKED' in idx and 'A CLONE IS NOT GUARDED' in idx
    gkk = kk1 and kk2 and kk3 and kk4
    print('    one key and one row : %s ; four overreadings NO KEY after : %s ; run passed : %s'
          % (kk1, kk2, kk3))
    print('    ### **AND THE KEY SAYS THE ROWS ARE NOT CHECKED AND THE CLONE IS NOT GUARDED** : %s' % kk4)
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTCHECKED')

    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (S, R, I, H, Q, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    go = o1 and stampm and o3 and o4 and o5 and o6
    print('    the lock recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('    audit JOINTLY SATISFIABLE : %s ; face says LOCKED BEFORE ANY WRITE : %s ; gate CLEAR : %s'
          % (o4, o5, o6))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b371_hooks.txt'), d('b371_mirror.txt')
    gh2 = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 failing, all byte-identical : %s ; mirror clean : %s' % (h_ok, m_ok))
    else:
        print('    ### the mirror record is NOT YET WRITTEN (it is written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('the figure %d' % S['figure'], ('figure of `%d`' % S['figure']) in bf),
        ('prints at the tag %d' % S['prints_at_tag'],
         ('`%d` zero-axiom prints' % S['prints_at_tag']) in bf),
        ('prints at head %d' % S['prints_at_head'], str(S['prints_at_head']) in bank),
        ('commits ahead %s' % S['head_ahead_of_tag'],
         ('`%s` COMMITS PAST THAT TAG' % S['head_ahead_of_tag']) in bf),
        ('readme headline %s' % S['readme_headline'], str(S['readme_headline']) in bank),
        ('readme breakdown %d' % S['readme_breakdown_sum'], str(S['readme_breakdown_sum']) in bank),
        ('rows %d' % I['rows'], ('`%d` ROWS CITE A KERNEL' % I['rows']) in bf),
        ('with pin %d / without %d' % (I['with_pin'], I['without_pin']),
         ('`%d` WITH NONE' % I['without_pin']) in bf),
        ('flagged %d' % I['flagged_count'], str(I['flagged_count']) in bank),
        ('distinct pins %d' % I['distinct_pins'], str(I['distinct_pins']) in bank),
        ('desk items %d' % Q['items'], ('`%d` ITEMS SWEPT' % Q['items']) in bf),
        ('closed %d' % Q['closed'], ('`%d` CLOSED' % Q['closed']) in bf),
        ('trail grew %d' % F['grew'], str(F['grew']) in bank),
        ('row %s' % ROWNUM, re.search(r'row to append : (\d+)',
                                      io.open(CORR, encoding='utf-8').read()).group(1) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on settle run', S['run_file'] in bank),
        ('the relied-on repair run', R['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('settle', S), ('repair', R), ('inventory', I),
                    ('hookpath', H), ('desk', Q), ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-10s %-28s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st,
                                                              jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b371_') and x.endswith('.py')))
    hits = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits and not imports
    print('    numerical calls : %d %s ; libraries : %s' % (len(hits), hits or '', imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-BYCONTENT:')
    selfhits = []
    for p in [t(x) for x in mymods]:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    DECLARED = {'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
                'the located span': 'the span is located by content and only then indexed.'}

    def which(code):
        if '[-1:]' in code or '[-1]' in code:
            return 'last-row cells'
        if 'split(' in code or 'find(' in code:
            return 'the located span'
        return None
    undeclared = []
    for fn, i, code in selfhits:
        key = which(code)
        print('    %-26s line %-6d | %s' % (fn, i, code))
        if key is None:
            undeclared.append((fn, i))
            print('        ### ### **UNDECLARED HIT.**')
        else:
            print('        %s' % DECLARED[key])
    gbc = not undeclared
    print('    ### hits : %d ; UNDECLARED : %d  %s'
          % (len(selfhits), len(undeclared), 'PASS' if gbc else '### FAIL ###'))
    if not gbc:
        fails.append('G-BYCONTENT')

    print(chr(10) + '  G-NOEDIT ### BEFORE THE PUSH:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/gate_content.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py',
             'tools/b363_span.py', 'tools/git-hooks/pre-push']
    GUARD = '.githooks/pre-push'
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    unlicensed = [p for p in touched if p not in LICENSED]
    # ### **THE GUARD THIS ACT PLACED IS THIS ACT'S OWN PATH AND IS NAMED, NOT WAVED THROUGH.**
    GUARD = '.githooks/pre-push'
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').splitlines()
              if x.strip() and 'b371' not in x and x.strip() != 'tools/banked_index.py'
              and x.strip() != GUARD and x.strip() not in LICENSED]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines()
              if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() not in ('OPEN_TRAILS.md', GUARD)]
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    gse = [x for x in git(SIDE, 'status', '--porcelain').splitlines()
           if x.strip() and x[3:].strip() not in ('CORRESPONDENCE.md', GUARD)]
    gne = (not unlicensed and not others and not ppbad and faces_clean and fnd and not gse)
    print('    owner instruments modified : %s' % (touched or 'none'))
    print('    ### **LICENSED : %s** ; ### **UNLICENSED : %s**' % (sorted(LICENSED),
                                                                   unlicensed or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    papers paths beyond the trail and the guard : %s' % (ppbad or 'none'))
    print('    construction-kernel paths beyond the row and the guard : %s' % (gse or 'none'))
    print('    ### **FACES_LEDGER UNTOUCHED** : %s ; FINDINGS clean : %s' % (faces_clean, fnd))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b371_satisfiable.json'), t('b371_regspec.py'), t('b371_extract.py'),
             t('b371_reg_gate.py'), t('b371_bank.py'), t('b371_correspondence.py'),
             t('b371_index_append.py'), t('b371_settle.py'), t('b371_repair_desc.py'),
             t('b371_hookpath.py'), t('b371_desk.py'), t('b371_filing.py')]
    CARRIERS = [
        (t('b371_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the kernel's own documents"),
        (d(S['run_file']), "the settle run carries the description and the README's own lines"),
        (d(R['run_file']), 'the repair run carries the description before and after'),
        (d(I['run_file']), "the inventory carries the rows' own text"),
        (d(H['run_file']), "the hook run carries the guard's own refusal text"),
        (d(Q['run_file']), "the desk run carries the fold's own sentence"),
        (d(F['run_file']), 'the filing carries the closures'),
        (t('b371_inventory.py'), "ITS PATTERNS ARE THE ROWS' OWN SHAPES"),
        (d('b371_hooks.txt'), "the exerciser's own log"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned, live_bad = 0, 0, 0, []
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
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
        if sh:
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', p],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **HANDED TO THE SHARED SCANNER : CLEAN : %s**' % clean)
            if not clean:
                live_bad.append(os.path.basename(p))
    print('    files scanned %d   struck %d   stem %d   ### **LIVE : %d** %s'
          % (scanned, total, stem_total, len(live_bad),
             'PASS' if not (total or live_bad) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in
                [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                 ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                 ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [],
                                     stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or live_bad or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE FIRST TARGET SETTLED, THE DESK CLOSED, THE GUARD MOVED (b371).'
    nxt = '# ### THE APPARATUS ARC, b361-b369 -- THE FOLD (b370).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row):' % ROWNUM)
    for lbl, b2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', tblk),
                    ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(b2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(b2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(b2)))
        if ch or not b2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            tmp = os.path.join(tempfile.mkdtemp(prefix='b371_stem_'), 'blk.txt')
            io.open(tmp, 'w', encoding='utf-8', newline=chr(10)).write(b2)
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', tmp],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **%d STEM HIT(S) HANDED TO THE SHARED SCANNER: CLEAN : %s**'
                  % (len(sh), clean))
            if not clean:
                fails.append('G-STEM-APPENDED live ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
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
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b371_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', tblk),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles refused : %d ; owner needles not in the extract file : %d'
          % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
