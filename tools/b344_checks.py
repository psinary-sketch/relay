# -*- coding: utf-8 -*-
"""b344_checks.py -- THE GATE SUITE FOR THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE.

### ### **THE ARMS (registration section (G)):** `G-AXIS` (the axis named with its reason before any value; the two held
### printed at every rung and byte-identical in their emitters), `G-LADDER` (exactly the sealed rungs, frame and object),
### `G-FLOOR` (the verdict by the sealed rule and no other, against b339's own figure; nothing concluded about the two
### held), `G-SEAL` (every existing seal's verdict unchanged, the fresh seal's clock, the clock outside the hash said so,
### `cmd_verify` untouched), `G-MODULE` (the September shape, b342's incident from the extract, the index appended, local
### and NOT PUSHED), `G-EDGE` (exactly the sealed heights at one width; the verdict by its rule; the narrowing quoted with
### the standing sentence), `G-ROW` / `G-ANCESTOR`, `G-KEY` / `G-NOTEXPLAINED`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the struck-clause and stem sweeps, `G-SHARED`, the hedge audit, the must-fail
### fixtures; re-run after the push. ### **NO FILE IS WRITTEN IN THE PAPERS REPO, SO THE HOOK AND THE MIRROR ARE NOT OWED.**
"""
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
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MODIDX = os.path.join(TC, 'modules', 'INDEX.md')
MODULE = os.path.join(TC, 'modules', '2026-09', 'SEAL_CARRIES_ITS_CLOCK.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b344_the_floor_priced.txt')
REG = d('b344_registration_2026-09-06.txt')
RULING = d('b344_ruling_2026-09-06.txt')
EXTRACT = d('b344_extract_notes.txt')
DRAFT = d('b344_executor_draft_2026-09-06.txt')
NRUN, NJ = d('b344_ny_run.txt'), d('b344_ny.json')
ERUN, EJ = d('b344_edge_run.txt'), d('b344_edge.json')
SBEF, SAFT, SJ = d('b344_seal_before_run.txt'), d('b344_seal_after_run.txt'), d('b344_seal_clock.json')
MRUN, MJ = d('b344_module_run.txt'), d('b344_module.json')
CORR, CORRR = d('b344_corr_run.txt'), d('b344_corr_rerun.txt')
IDX, IDXR = d('b344_index_run.txt'), d('b344_index_rerun.txt')
SCAN, RSCAN, TERMSCAN, GATE = d('b344_ferry_scan.txt'), d('b344_ruling_scan.txt'), d('b344_reg_termscan.txt'), d('b344_reg_gate.txt')
CENSUS, FCEN = d('b344_census.txt'), d('b344_faces_census.txt')
REGSPEC, SATIS = d('b344_regspec_run.txt'), d('audit_b344_reg_satisfiable.txt')
PINS, INDEXQ = d('b344_pins_stepzero.txt'), d('audit_b344_index_query.txt')
SEAL = 'cc6ec40d6c13dea67cddabacfe045b80406d51c1c5886066248c6624c38e8b5f'
MARK_I = '<!-- b344 -->'
ROWNUM = '192'
LADDER = [128, 256, 512, 1024, 2048]
EXTEND = [1.0, 1.25, 1.5, 1.75]

OWNED = [BANK, REG, RULING, DRAFT, NRUN, NJ, ERUN, EJ, SBEF, SAFT, SJ, MRUN, MJ, CORR, CORRR, IDX, IDXR, CENSUS, FCEN,
         REGSPEC, SATIS, PINS, INDEXQ, GATE, RSCAN, d('b344_satisfiable.json'), d('b344_seal_census_before.json'), d('b344_seal_census_after.json'),
         t('b344_extract.py'), t('b344_regspec.py'), t('b344_draft.py'), t('b344_ny.py'), t('b344_edge.py'), t('b344_seal_clock.py'),
         t('b344_module.py'), t('b344_correspondence.py'), t('b344_index_append.py'), MODULE]

CARRIERS = [
    (t('b344_checks.py'), 'its own fixtures'),
    (d('b344_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
    (d('b344_seal_before_run_falsepositive.txt'), "the census's own refused first pass, kept"),
]

OWNER_NEEDLES = [
    ('the ferry -- addition one', d('b344_ferry_2026-09-06.txt'), 'ADDITION ONE, to Component 1: the axis moved is chosen and'),
    ("the ferry -- addition two, the room's edge", d('b344_ferry_2026-09-06.txt'), "ADDITION TWO, a new Component 2b \u2014 THE ROOM'S EDGE: b343's"),
    ('### a finer chart and not a trend', d('b344_ferry_2026-09-06.txt'), 'grid is a finer chart and not a trend, and that nothing about'),
    ('the draft -- component 1', DRAFT, "COMPONENT 1 \u2014 THE FLOOR PRICED: b339 found the identity residual's limit"),
    ('### the three candidate origins', DRAFT, "for that floor \u2014 the fixed NY = 512, the cut's tau, the taper. b343 moved"),
    ("### component 2, the seal's clock", DRAFT, "COMPONENT 2 \u2014 THE SEAL'S OWN CLOCK: b342's G-ORDER was declared a"),
    ("### the order's words for the repair", DRAFT, "past: have reg_seal.py record the seal's UTC instant inside the seal block"),
    ('### what it does not recover', DRAFT, "the repair does NOT do: it does not recover b342's lost timestamp."),
    ('### one axis moved is one axis moved', DRAFT, 'COMPONENT 3 \u2014 WHAT IT SAYS AND DOES NOT: one axis moved is one axis'),
    ("the ruling -- this act's number", RULING, "OPTION 1. b344 = THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND"),
    ("b339 -- the floor and its three candidates", d('b339_the_exponent_resolved.txt'), "### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut's `tau`, the"),
    ('b321 -- the separation at the cell', d('b321_the_window_opened.txt'), '    1.41   0.221284108      0.217290580      0.003993528    0.018807781      PASSES'),
    ("b343 -- the room's minimum at the edge", d('b343_the_maps_next_reach.txt'), "### **AND ONE OF THE TWO MINIMA SITS AT THE INTERVAL'S EDGE:** at `a = 40` it is interior (`gamma = 2.0`"),
    ('b342 -- the order arm is a defective bar', d('b342_the_two_rules_as_modules.txt'), '### ### **(4) THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.** ### `G-ORDER`'),
    ("b319 -- tau, 57 times inside the separation", t('b319_stable.py'), '# ### `TAU = 1e-6` therefore sits ### **57 TIMES INSIDE THAT SEPARATION** ### and ten orders of'),
    ('b316 -- the taper ALPHA', t('b316_instrument.py'), "ALPHA = 1.0   # ### Definition 4.4's `a`, at the source's own `S(1,1)`"),
    ('b317 -- NY fixed, one axis at a time', t('b317_smear.py'), 'NY_FIXED = 512        # ### one NY throughout, so each axis moves one thing'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) the residual moves', BANK, 'THE RESIDUAL MOVES WITH `NY`, AND BY THE SEALED RULE THE MOVEMENT IS OF THE SIZE THE FLOOR'),
    ('### (2) the rank does not move', BANK, 'AND THE RANK DOES NOT MOVE AT ALL.**'),
    ('### (3) the reading beside the verdict', BANK, 'A READING BESIDE THE VERDICT, LABELLED AND CONFERRING NOTHING.**'),
    ('### both sentences true', BANK, '**BOTH SENTENCES ARE TRUE AND NEITHER REPLACES THE OTHER:**'),
    ('### (4) the two axes held, printed', BANK, 'THE TWO AXES HELD WERE PRINTED AT EVERY RUNG, AS THE FERRY\'S ADDITION ONE REQUIRES**'),
    ('### one axis moved is one axis moved', BANK, '**ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    ('### (5) the seal carries its clock', BANK, 'THE SEAL NOW CARRIES ITS OWN CLOCK, AND EVERY SEAL WRITTEN BEFORE IT IS UNTOUCHED.**'),
    ('### the honest limit', BANK, '**THE HONEST LIMIT OF THE REPAIR, THE CLOCK IS OUTSIDE THE HASH**'),
    ('### it does not recover b342', BANK, '**THE REPAIR DOES NOT RECOVER b342\'s LOST'),
    ('### (6) bracketed', BANK, "THE ROOM'S MINIMUM AT THE WIDER REACHING WIDTH IS BRACKETED.**"),
    ('### (7) a finer chart and not a trend', BANK, '**A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND'),
    ('### (8) the expectations scored', BANK, 'THE EXPECTATIONS, SCORED.**'),
    ('### no grade moved', BANK, 'NO GRADE MOVED. NO BAR MOVED. THE FLOOR IS NOT EXPLAINED. NOTHING DEPOSITS.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the number first', BANK, '**THE NUMBER FIRST.**'),
    ('bank gives the instruments', BANK, 'THE INSTRUMENTS AND THEIR JUDGEMENT.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED:"),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the ferry-standing note for v2', BANK, 'carries its act number, and a number already claimed by an unclosed ferry is a hit for the ferry'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('registration -- sealed before any rung', REG, 'SEALED BEFORE ANY FRAME IS BUILT AT A NEW `NY`, BEFORE THE SEAL TOOL IS TOUCHED, AND BEFORE ANY'),
    ('registration -- the axis named', REG, '**THE AXIS MOVED IS `NY`.**'),
    ('registration -- why not tau', REG, "**WHY `NY` AND NOT THE CUT'S `tau`:**"),
    ('registration -- why not the taper', REG, '**WHY `NY` AND NOT THE TAPER:**'),
    ('registration -- the ladder fixed', REG, '**THE LADDER, FIXED HERE:**'),
    ('registration -- the verdict rule', REG, '**THE VERDICT RULE:**'),
    ('registration -- the span fixed', REG, '**THE SPAN, FIXED HERE:**'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('the ladder record -- the verdict', NRUN, 'AND THE MOVEMENT IS'),
    ('the ladder record -- nothing about the held axes', NRUN, '  ### NOTHING IS CONCLUDED ABOUT THE TWO AXES HELD. ### ONE AXIS MOVED IS ONE AXIS MOVED.'),
    ('the edge record -- bracketed', ERUN, '**BRACKETED: the room\'s minimum over the extended grid is INTERIOR'),
    ('the edge record -- the standing sentence', ERUN, '  ### ### **A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND NOT A TREND, AND NOTHING ABOUT TOTALITY FOLLOWS.**'),
    ('the seal record -- same verdict', SAFT, '  ### every existing seal gives the SAME verdict before and after'),
    ('the seal record -- the limit stated', SAFT, '**AND THAT IS THE HONEST LIMIT OF THE REPAIR: THE CLOCK IS OUTSIDE THE HASH.**'),
    ('the module record -- not pushed', MRUN, 'NOT PUSHED'),
]

MUST_FAIL = [
    ('the bank never says the floor is explained', BANK, '### ### **THE FLOOR IS EXPLAINED.**'),
    ('the bank never exonerates the axes held', BANK, '### ### **THE CUT AND THE TAPER ARE EXONERATED.**'),
    ('the bank never says the seal recovers b342', BANK, "### ### **THE REPAIR RECOVERS b342'S TIMESTAMP.**"),
    ('the bank never says the narrowing is a trend', BANK, '### ### **THE NARROWING IS A TREND.**'),
    ('the bank never says TECHNE was pushed', BANK, '### ### **TECHNE-Core IS PUSHED.**'),
    ('the bank never says a grade moved', BANK, '### ### **A GRADE MOVED.**'),
]

TOOLNUM = [
    ('the ladder, the residual, the held axes', 'tools/b344_ny.py'),
    ('the extended heights and the bracketing', 'tools/b344_edge.py'),
    ('the seal census and the three fixtures', 'tools/b344_seal_clock.py'),
    ('the module, the index block, the local commit', 'tools/b344_module.py'),
    ('the clock the seal now writes', 'tools/reg_seal.py'),
    ('row 192', 'tools/b344_correspondence.py'),
    ('the key', 'tools/b344_index_append.py'),
    ('29 clauses', 'tools/b344_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('19309 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b344_extract.py'),
    ('the draft banked', 'tools/b344_draft.py'),
    ("the aim-map's seed, quantities and gate", 'tools/b334_aimmap.py'),
    ('the stable cut', 'tools/b319_stable.py'),
]
NEW_THIS_ACT = {'tools/b344_ny.py', 'tools/b344_edge.py', 'tools/b344_seal_clock.py', 'tools/b344_module.py', 'tools/b344_draft.py',
                'tools/b344_correspondence.py', 'tools/b344_index_append.py', 'tools/b344_regspec.py', 'tools/b344_extract.py', 'tools/b344_checks.py'}


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def flat(s):
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^###\s*', ' ', s.replace('\u2019', "'"))).strip()


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def main():
    fails = []
    print('=' * 100)
    print("b344 -- GATE SUITE (ONE AXIS MOVED, A TOOL REPAIRED, A CHART EXTENDED)")
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    N = json.load(io.open(NJ, encoding='utf-8'))
    E = json.load(io.open(EJ, encoding='utf-8'))
    S = json.load(io.open(SJ, encoding='utf-8'))
    M = json.load(io.open(MJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + '  G-AXIS (the axis named with its reason before any value; the two held printed at every rung and unchanged in their emitters):')
    named = "**THE AXIS MOVED IS `NY`.**" in reg and "WHY `NY` AND NOT THE CUT'S `tau`:" in reg and "WHY `NY` AND NOT THE TAPER:" in reg
    held_ok = all('held' in r and r['held']['tau'] == 1e-6 and r['held']['alpha'] == 1.0 and r['held']['beta'] == 1.0 for r in N['rows'])
    emitters = git(ROOT, 'status', '--porcelain', '--', 'tools/b319_stable.py', 'tools/b316_instrument.py', 'tools/b317_smear.py').strip()
    ga = named and held_ok and not emitters
    print('    named with its reason %s ; the two held printed at all %d rungs %s ; their emitters unchanged %r : %s' % (named, len(N['rows']), held_ok, emitters, ga))
    if not ga:
        fails.append('G-AXIS')

    print(chr(10) + '  G-LADDER (exactly the sealed rungs at the sealed frame and object):')
    gl = [r['NY'] for r in N['rows']] == LADDER and N['N'] == 4096 and N['X'] == 32.0 and N['cell'] == 1.41 and N['ladder'] == LADDER
    print('    %s (rungs %s, frame N=%s X=%s, cell %s)' % (gl, [r['NY'] for r in N['rows']], N['N'], N['X'], N['cell']))
    if not gl:
        fails.append('G-LADDER')

    print(chr(10) + "  G-FLOOR (the verdict by the sealed rule, recomputed; nothing concluded about the two held):")
    v = [r['R_EF'] for r in N['rows']]
    w = [r['R_ER'] for r in N['rows']]
    span = max(max(v) - min(v), max(w) - min(w))
    rel = max(N['rel_EF'], N['rel_ER'])
    floor = 1.6 * 0.003993528
    size = 'OF THE SIZE THE FLOOR REQUIRES' if span >= floor / 2 else ('NOT OF THAT SIZE' if span < floor / 10 else 'INCONCLUSIVE AT THIS LADDER')
    gf = abs(span - N['span_abs_EF']) < 1e-12 and abs(floor - N['floor']) < 1e-12 and size == N['size'] and (rel > 1e-3) == N['moves'] \
        and N['size'] in bank and 'NOTHING IS CONCLUDED ABOUT THE TWO' in bf.upper() and 'THE FLOOR IS NOT EXPLAINED' in bf.upper()
    print('    span %.6e ; floor %+.9f ; recomputed verdict %r ; recorded %r ; moves %s : %s' % (span, floor, size, N['size'], N['moves'], gf))
    if not gf:
        fails.append('G-FLOOR')

    print(chr(10) + '  G-SEAL (every existing seal unchanged in verdict, none rewritten; the fresh clock; the limit stated; cmd_verify untouched):')
    src = io.open(t('reg_seal.py'), encoding='utf-8').read()
    vb = blob_of(ROOT, 'tools/reg_seal.py') or ''

    # ### the arm means `cmd_verify` and `digest` THEMSELVES are untouched. ### Comparing the tail of the file from
    # ### `def cmd_verify` onward compares `cmd_reseal` too, which this act DID edit by the order's words; the first
    # ### run failed on exactly that. ### Compare each function's own body, delimited by the next top-level `def`.
    def fnbody(text, name):
        i = text.find('def %s(' % name)
        if i < 0:
            return None
        j = text.find(chr(10) + 'def ', i + 1)
        return text[i:j if j > 0 else len(text)]
    verify_same = all(fnbody(src, n) is not None and fnbody(src, n) == fnbody(vb, n) for n in ('cmd_verify', 'digest', 'split_body'))
    gs = (S['same_verdict'] == S['sealed_before'] == 66 and not S['rewritten'] and not S['missing'] and S['clock_in_source']
          and S['fixture_fresh'] and S['fixture_clock_outside_hash'] and S['fixture_body_refused'] and verify_same and S['ok'])
    print('    %d of %d verdicts unchanged ; rewritten %s ; fixtures %s/%s/%s ; cmd_verify, digest and split_body byte-identical to their blobs %s : %s'
          % (S['same_verdict'], S['sealed_before'], S['rewritten'], S['fixture_fresh'], S['fixture_clock_outside_hash'], S['fixture_body_refused'], verify_same, gs))
    if not gs:
        fails.append('G-SEAL')

    print(chr(10) + '  G-MODULE (the September shape; b342\'s incident from the extract; the index appended; local and NOT PUSHED):')
    mod = io.open(MODULE, encoding='utf-8').read()
    hdr = '*TECHNE module draft \u00b7 extracted 2026-09-06 (research seat, b344) \u00b7 **PRIVATE, TECHNE-Core, local-only**.'
    secs = ('## WHAT IT DOES', '## WHEN IT APPLIES', '## WHAT IT REFUSES', '## PROVENANCE')
    exf = flat(extract)
    quotes = re.findall(r'\*"([^"]{12,})"\*', mod)
    qmiss = [q for q in quotes if flat(q) not in exf]
    on_remote = git(TC, 'branch', '-r', '--contains', M['committed']).strip()
    net = {}
    for ln in git(TC, 'diff', '--name-status', '824f7e5', 'HEAD', '--', 'modules/').splitlines():
        if ln.strip():
            st, name = ln.split(None, 1)
            net[name.strip()] = st
    gm = (hdr in mod and all(s in mod for s in secs) and not qmiss
          and net == {'modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md': 'A', 'modules/INDEX.md': 'M'}
          and M['remote_before'] == M['remote_after'] == '22739c9' and not on_remote and M['clean'] and M['untouched'])
    print('    shape %s ; quotations %d, unlocated %d %s ; the act\'s net effect on modules/ %s ; remote %s, on a remote branch %r : %s'
          % (hdr in mod and all(s in mod for s in secs), len(quotes), len(qmiss), qmiss[:1], net, M['remote_after'], on_remote, gm))
    if not gm:
        fails.append('G-MODULE')

    print(chr(10) + "  G-EDGE (exactly the sealed heights at one width; the verdict by its rule; the narrowing quoted with the standing sentence):")
    ge = ([r['gamma'] for r in E['rows']] == EXTEND and E['width'] == 81.0 and E['minimum']['interior']
          and not E['negative'] and not E['pairs'] and not E['refused'] and len(E['joint']) == 17
          and ('%+.9f' % E['minimum']['room_z']) in bank and ('%.2f' % E['ratio']) in bank
          # ### the standing sentence is one the bank WRAPS across its own lines; read it flattened, as this suite
          # ### reads every other sentence of the bank -- the first run compared it raw and failed on the wrap.
          and 'A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND NOT A TREND' in bf)
    print('    heights %s at a = %s ; interior %s ; no crossing %s ; 17 joint heights %s : %s'
          % ([r['gamma'] for r in E['rows']], E['width'], E['minimum']['interior'], not (E['negative'] or E['pairs']), len(E['joint']) == 17, ge))
    if not ge:
        fails.append('G-EDGE')

    r192 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| %s |' % ROWNUM)]
    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    headb = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r192) == 1 and 'NO TERMINAL, AND THE REASON: A MEASUREMENT OF THE INSTRUMENT, A TOOL REPAIR, AND A CHART' in r192[0] \
        and 'M-2' in r192[0] and 'ONE AXIS MOVED IS ONE AXIS MOVED' in r192[0] and norm(tbl).startswith(norm(headb).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTEXPLAINED (one row; the must-not-hit queries NO KEY; the answer refuses the four overreadings):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('floor-priced')
    gk = o.count('act      :') == 1 and 'ONE AXIS MOVED IS ONE AXIS MOVED' in o and 'THE FLOOR IS NOT EXPLAINED' in o \
        and "DOES NOT RECOVER b342's LOST TIMESTAMP" in o and 'A FINER CHART AND NOT A TREND' in o
    for s in ('the floor explained', 'the taper exonerated', 'the seal recovers b342'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOTEXPLAINED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (no owner instrument but reg_seal changed; the papers repo untouched; the deposit and HANDOFF clean):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md',
              'tools/b334_aimmap.py', 'tools/b319_stable.py', 'tools/b318_square.py', 'tools/b317_smear.py', 'tools/b316_instrument.py',
              'tools/b321_window.py', 'tools/b320_weil.py', 'HANDOFF.md', 'data/STRUCK_CLAUSES.md',
              'data/b339_the_exponent_resolved.txt', 'data/b342_the_two_rules_as_modules.txt', 'data/b343_the_maps_next_reach.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    st_t = git(TC, 'status', '--porcelain').strip()
    # ### the one owner-instrument edit this act made, BY THE ORDER'S WORDS, must be present -- and the test must give
    # ### the same answer before and after the commit. ### `git status` says "modified" only until the commit; the
    # ### stable test is against the tree this act found (`963bfc2`, its step-zero pin). ### The first post-push run
    # ### failed on exactly that.
    seal_changed = bool(git(ROOT, 'diff', '--name-only', '963bfc2', '--', 'tools/reg_seal.py').strip())
    gn2 = not st_r and not st_s and not st_p and not st_t and seal_changed
    print('    relay owners %r ; SIDE (beyond the table) %s ; PLACE-papers %s ; TECHNE %r ; reg_seal changed against the pre-act tree (the one edit by the order) %s : %s'
          % (st_r, st_s, st_p, st_t, seal_changed, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the components after the seal; the audit as it stands):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b344_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    sat_ok = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8', errors='replace').read()
    no_clock = '### sealed at (UTC) : ' not in raw.decode('utf-8', 'replace')
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [NRUN, NJ, ERUN, EJ, SAFT, MRUN, MODULE, CORR, IDX, BANK, t('reg_seal.py')])
        how = 'file times (pre-commit; this registration carries no clock, being sealed before the repair)'
    else:
        pre = io.open(d('b344_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b344_checks_run.txt')) else ''
        after = 'the components, the row, the key and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and sat_ok and after and no_clock
    print('    seal verifies %s ; hash equals the literal %s ; the audit JOINTLY SATISFIABLE %s ; this registration carries no clock (sealed before the repair) %s' % (intact, rawhash == SEAL, sat_ok, no_clock))
    print('    the components, the row, the key and the bank after the seal %s [%s] : %s' % (after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-PAPERS (no file written in the papers repo, so the hook and the mirror are NOT OWED):')
    gp = not [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x] \
        and not os.path.exists(d('b344_hooks.txt')) and not os.path.exists(d('b344_mirror.txt')) and 'the hook and the mirror are not owed' in bf.lower()
    print('    %s' % gp)
    if not gp:
        fails.append('G-PAPERS')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = []
    checks.append(('the five residuals under EF', all(('%+.9f' % x) in bank for x in v)))
    checks.append(('the five under ER', all(('%+.9f' % x) in bank for x in w)))
    checks.append(('the span %.6e' % N['span_abs_EF'], ('%.6e' % N['span_abs_EF']) in bank))
    checks.append(('the floor %+.9f' % N['floor'], ('%+.9f' % N['floor']) in bank))
    checks.append(('the relative %.3e' % rel, ('%.3e' % rel) in bank))
    checks.append(('the rank %d and free %d' % (N['ranks'][0], N['rows'][0]['free']), ('`%d`' % N['ranks'][0]) in bank and ('`%d`' % N['rows'][0]['free']) in bank))
    checks.append(('tau and the taper', ('1.0e-06' in bank) and ('`ALPHA = 1`' in bank)))
    checks.append(('%d sealed files' % S['sealed_before'], ('`%d`' % S['sealed_before']) in bank))
    checks.append(('the stamp %s' % S['stamp'], (S['stamp'] or '') in bank))
    checks.append(('the module commit %s and %d lines' % (M['committed'], M['module_lines']), ('`%s`' % M['committed']) in bank and ('%d lines' % M['module_lines']) in bank))
    checks.append(('the index %d lines' % M['index_lines'], ('%d` lines' % M['index_lines']) in bank or ('-> %d' % M['index_lines']) in bank))
    checks.append(('the edge minimum %+.9f at %.2f' % (E['minimum']['room_z'], E['minimum']['gamma']), ('%+.9f' % E['minimum']['room_z']) in bank and ('%.2f' % E['minimum']['gamma']) in bank))
    checks.append(('the ratio %.2f' % E['ratio'], ('%.2f' % E['ratio']) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    for what, ok in checks:
        print('    %-52s %s' % (what[:52], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the refused first census kept):')
    once_ok = all(os.path.exists(p) for p in [NRUN, ERUN, SBEF, SAFT, MRUN, CORR, CORRR, IDX, IDXR]) \
        and os.path.exists(d('b344_seal_before_run_falsepositive.txt')) and not os.path.exists(d('b344_ny_run2.txt'))
    print('    %s' % once_ok)
    if not once_ok:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in (ch + sh)[:6]:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-40s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                        ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                     if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib = idx[idx.index("# ### THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE (b344"):idx.index("# ### THE MAP'S NEXT REACH (b343")] if "# ### THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE (b344" in idx else ''
    mi = io.open(MODIDX, encoding='utf-8').read()
    mib = mi[mi.index(MARK_I):] if MARK_I in mi else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the module, the index block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, r192[0] if r192 else ''), ('the module', mod), ('the index block', mib), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
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
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-64s %-34s exists=%s tracked=%s' % (what[:64], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the module, the row and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b344_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, r192[0] if r192 else ''), ('the index block', mib), ('the index row', ib)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, gh, ua = hedge_audit.audit(path)
        print('    %-40s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(gh), len(ua)))
        for s2 in gh:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
