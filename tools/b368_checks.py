# -*- coding: utf-8 -*-
"""b368_checks.py -- THE GATE SUITE FOR THE FRONT DOCUMENT RECONCILED.

### ### **EVERY ARM IS WRITTEN BY CONTENT AND NOT BY ADDRESS** (`b366`'s `(R2)`), and `G-BYCONTENT`
### re-measures that on this act's own files with `b366`'s own detector, so the claim is a measurement.
### ### **AND BY `(R2)`'S SPLIT THIS IS A `STANDING` SUITE**: its subjects are this act's own artifacts,
### so it must reproduce from a copy at any later date -- ### **AND IT IS WRITTEN TO REPRODUCE.** ### No
### arm reads a living record whose truth is dated; the two arms that must read a working tree
### (`G-NOLEAN`, `G-NOEDIT`) are declared as ### **MOMENT CERTIFICATES** ### on their own faces and are
### stated by CONTENT rather than by a byte-identity that the closing appends would break (`b364`'s
### `G-UNCHANGED` incident).
### ### **IT USES `gate_needle` AND `gate_text.flat` AND DEFINES NO FLATTENER OF ITS OWN** -- `b348`'s rule.
### ### **THE SIDES, BY `b352`:** ### `G-NOLEAN`'s and `G-NOEDIT`'s working-tree halves and `G-ROW`'s,
### `G-TRAIL`'s and `G-APPENDONLY`'s ancestry readings are read BEFORE THE PUSH; `G-HOOK`/`G-MIRROR`
### AFTER; `G-ORDER` is SIDE-INVARIANT.
### ### **AND THE RUN FILES ARE RESOLVED BY THEIR OWN RECORDED CLOCKS, NEVER BY NAME** (`b358`'s cure),
### which this act needed twice: the extract ran twice and the desk tool three times.
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
import b366_sweep as SW    # noqa: E402  ### (R2)'s DETECTOR, TURNED ON THIS ACT

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b368_the_front_document_reconciled.txt')
REG = d('b368_registration_2026-09-08.txt')
FERRY = d('b368_ferry_2026-09-08.txt')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
MODULE = os.path.join(TC, 'modules', '2026-09', 'DESK_FRESHNESS.md')
CORR, IDX = d('b368_corr_run.txt'), d('b368_index_run.txt')
SCAN, TERMSCAN, GATE = d('b368_ferry_scan.txt'), d('b368_reg_termscan.txt'), d('b368_reg_gate.txt')
CENSUS0, FCEN = d('b368_census_stepzero.txt'), d('b368_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b368_regspec_run.txt'), d('audit_b368_reg_satisfiable.txt')
PINS = d('b368_pins_stepzero.txt')
SEAL = '99b16780f1b3e10a706ee63b06946e2bc0d791639c734885b40050e69ff21bde'
ROWNUM = '217'
TRAIL_MARK = '<!-- b368 front document reconciled by an appended currency block -->'
B367_MARK = '<!-- b367 scaffold terminals not located -->'
CURRENCY_MARK = '<!-- b368 currency block: layer-1 export list vs source -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b368_reads.json'), ('C', 'b368_classify.json'),
                   ('R', 'b368_reconcile.json'), ('K', 'b368_desk.json'),
                   ('F', 'b368_filing.json'))}

NEW_THIS_ACT = {'tools/b368_regspec.py', 'tools/b368_extract.py', 'tools/b368_classify.py',
                'tools/b368_reconcile.py', 'tools/b368_desk.py', 'tools/b368_filing.py',
                'tools/b368_bank.py', 'tools/b368_correspondence.py',
                'tools/b368_index_append.py', 'tools/b368_checks.py'}

TOOLNUM = [
    ('the live ref, the re-derivation and the per-name evidence', 'tools/b368_classify.py'),
    ('the branch and the append-only arms', 'tools/b368_reconcile.py'),
    ('the desk rule and the nine marks', 'tools/b368_desk.py'),
    ('the 32 reads', 'tools/b368_extract.py'),
    ('the trail block and its bytes', 'tools/b368_filing.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b368_bank.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 217', 'tools/b368_correspondence.py'),
    ('the key', 'tools/b368_index_append.py'),
    ('55 clauses', 'tools/b368_regspec.py'),
    ('15173 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b368 - THE FRONT DOCUMENT RECONCILED, OR PRICED. The'),
    ('the order -- addition one, the live read', FERRY,
     'ADDITION ONE - THE READ IS LIVE AND ITS REF IS NAMED: the'),
    ('the order -- and why a carried figure will not do', FERRY,
     'classification; the eighteen absent names are re-derived from'),
    ('the order -- addition two, the four kinds', FERRY,
     'ADDITION TWO - EACH NAME CLASSIFIED, one row each: PRESENT'),
    ('the order -- never from its own sound', FERRY,
     'NEVER EXISTED (with the search recorded). No name is'),
    ('the order -- addition three, the two branches', FERRY,
     'ADDITION THREE - THE REPAIR OR THE PRICE. If the front document'),
    ('the order -- and the lean files untouched in either branch', FERRY, 'branch the kernel'),
    ('the order -- addition four, the desk rule', FERRY, 'ADDITION FOUR - THE DESK'),
    ('the order -- marks, not verdicts', FERRY,
     'item is closed by this act; the sweep produces marks, not'),
    ("the order -- the navigator's expectations", FERRY, 'NAVIGATOR EDITS. The navigator'),
    ('the front document -- what the module formalizes', AGENTS,
     '`SIDEEffects/Structural.lean` formalizes the structural content for nine framework'),
    ('the front document -- the GRH layer line', AGENTS, '- **GRH layer**:'),
    ('the front document -- the Landau-Siegel layer line', AGENTS, '- **Landau-Siegel layer**:'),
    ('the kernel -- the retirement ledger heading', STRUCT,
     '-- RETIREMENT LEDGER (audit Phase S.2–S.4)'),
    ('the kernel -- what the ledger says it lists', STRUCT,
     '-- content-free (True-stub or opaque-Prop). Honest status of each'),
    ('the record -- the front document has not caught up', TRAILS,
     'caught up: `AGENTS.md` lists 20 "Theorems exported" of which'),
]

SELF_NEEDLES = [
    ('the bank states the answer first', BANK,
     'THE FRONT DOCUMENT IS RECONCILED, AND IT WAS RECONCILED WITHOUT EDITING A SENTENCE'),
    ('### the figure was re-derived, not carried', BANK, 'RE-DERIVED, NOT CARRIED'),
    ('### and the comparison is reported afterwards', BANK,
     'it is never an input to the count. ### The count comes'),
    ('### every absent name is retired', BANK, 'EVERY ONE OF THE 18 IS `RETIRED`'),
    ('### nothing was invented', BANK, 'SO NOTHING IN THAT LIST WAS EVER INVENTED'),
    ("### this act's own new finding", BANK,
     'AND THIS ACT’S OWN NEW FINDING, WHICH NEITHER `b157` NOR `b367` HAD: THE RETIREMENT'),
    ('### the ledger accurate and incomplete', BANK, 'INCOMPLETE ABOUT WHAT IT NAMES'),
    ('### the list itself is still wrong', BANK, 'AND THE LIST ITSELF STILL EXPORTS 18 ABSENT NAMES'),
    ('### the trail is updated and not closed', BANK, 'UPDATED AND NOT CLOSED'),
    ('### the head had not moved, and why that matters', BANK,
     'HAD IT MOVED, THE AGREEMENT'),
    ('### no name from its own sound', BANK, 'NO NAME IS CLASSIFIED FROM ITS OWN SOUND'),
    ('### the three kinds partition the eighteen', BANK,
     'AND THE THREE KINDS PARTITION THE EIGHTEEN EXACTLY, WHICH IS WHY NO NAME IS'),
    ('### and one layer has no ledger entry at all', BANK,
     'AND `1` HAS NO LEDGER ENTRY FOR ITS LAYER AT ALL'),
    ('### the suite caught the act overstating its own evidence', BANK,
     'THE BANK OVERSTATED ITS OWN EVIDENCE, AND ITS OWN GATE SUITE CAUGHT IT'),
    ('### and after a push the wrong sentence would have stood', BANK,
     'WRONG SENTENCE WOULD HAVE STOOD'),
    ('### RENAMED 0 is a refusal', BANK, 'AND THE ZERO IS A REFUSAL, NOT AN ABSENCE OF LOOKING'),
    ('### the resemblance met and refused', BANK, 'One resemblance was met and refused'),
    ('### the branch was decided, not chosen', BANK, 'THE BRANCH WAS DECIDED, NOT CHOSEN'),
    ('### the other branch unreachable, with its reason printed', BANK,
     'IS UNREACHABLE HERE**, and the reason is printed by the'),
    ('### the check is on the block, not the document', BANK,
     'A CHECK ON THE BLOCK, NOT ON THE DOCUMENT'),
    ('### the half-repair at full prominence', BANK,
     'HALF-REPAIR IS REPORTED AT FULL PROMINENCE RATHER THAN LET PASS AS A REPAIR'),
    ('### the desk rule, in its own words', BANK,
     'every desk item names the file and date at which it was last confirmed, and'),
    ('### the module states its own limit', BANK,
     'NO TOOL CAN CHECK THAT THE NAMED FILE STILL CONFIRMS'),
    ('### the module is local and not pushed', BANK, 'COMMITTED LOCALLY AT'),
    ('### marks, not verdicts, and nothing closed', BANK, 'AND `0` ITEMS CLOSED'),
    ("### the sweep's own reach, stated", BANK,
     'A FILE THAT MENTIONS AN ITEM IS NOT A FILE THAT CONFIRMS IT'),
    ('### the faces ledger not written, and why', BANK, 'BECAUSE NO ROW MOVED'),
    ('### the hook absence filed, not repaired', BANK, 'IT IS NOT REPAIRED HERE'),
    ('### the incident: hints typed from sense', BANK,
     'THE LINE THE TOOL RETURNS IS WHAT IS QUOTED'),
    ('### the incident: numbered repeats, resolved by clock', BANK,
     'ARE `b368_extract_notes2.txt` AND `b368_desk_notes3.txt`, RESOLVED BY THEIR RECORDED CLOCKS'),
    ('### the incident: a wrong arm in this act’s own tool', BANK,
     'THE ARM WAS WRONG AND WAS REPAIRED, NOT THE'),
    ('### the incident: a sweep that read its own paperwork', BANK,
     'A SWEEP THAT READS ITS OWN PAPERWORK CONFIRMS ITSELF'),
    ('### the incident: what the stem scan cannot see', BANK,
     'its stem'),
    ('### (F1) confirmed, and more strongly than asked', BANK,
     'CONFIRMED, AND MORE STRONGLY THAN ASKED'),
    ('### and a stronger result is not a better score', BANK,
     'THE STRONGER RESULT IS NOT A BETTER SCORE'),
    ('### (F2) confirmed, and what still needs the author', BANK,
     'AND THE HALF THAT DOES STILL NEED THE AUTHOR IS NAMED'),
    ('### the seat predicted the easy half', BANK,
     'a seat that predicts a re-run of its'),
    ('### the retirements reported, not endorsed', BANK,
     'THE RETIREMENTS ARE REPORTED, NOT ENDORSED'),
]

MUST_FAIL = [
    ('the bank never says a Lean file was written', BANK, '### A LEAN FILE WAS WRITTEN.'),
    ('the bank never says an existing sentence was edited', BANK,
     '### AN EXISTING SENTENCE WAS EDITED.'),
    ('the bank never says a desk item is closed', BANK, '### A DESK ITEM IS CLOSED.'),
    ('the bank never says the hook was installed', BANK, '### THE HOOK WAS INSTALLED.'),
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
    print('b368 -- GATE SUITE (THE FRONT DOCUMENT RECONCILED)')
    print('=' * 100)
    E, C, R, K, F = _J['E'], _J['C'], _J['R'], _J['K'], _J['F']
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### BUILT BY `gate_needle` FROM THE FILE THAT EMITTED THEM, AND EACH')
    print('  ### ALSO PRESENT IN THE RELIED-ON EXTRACT FILE:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            # ### **THE EXTRACT TOOL PRINTS EACH LINE TRUNCATED AT 200 CHARACTERS**, so a source line
            # ### longer than that CANNOT satisfy a whole-line presence arm -- the arm would be demanding
            # ### something the extract never records. ### **THAT IS A WRONG ARM, NOT A MISSING READ**
            # ### (`b365`'s species), and the cure is to say which reading is being made: for a long line
            # ### the arm requires the RECORDED PREFIX, and prints that it did.
            trunc = False
            if not inx and len(line.rstrip()) > 200:
                inx = line.rstrip()[:200] in extract
                trunc = bool(inx)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    ('  ### -- ITS RECORDED PREFIX (the extract truncates at 200)'
                                     if trunc else ('' if inx else '  -- NOT IN THE EXTRACT FILE'))))
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
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    agents = io.open(AGENTS, encoding='utf-8', newline='').read()

    print(chr(10) + '  G-REF (the read is live and its ref is named BEFORE any classification):')
    r1 = C['head'] in bank and C['ref'] in bank
    r2 = C['pinned'] is True and C['ls_remote'] == C['head']
    r3 = C['dirty'] is False
    # ### **THIS CLAUSE IS SIDE-DEPENDENT AND THE FIRST VERSION DID NOT SAY SO** (`b352`). ### Before the
    # ### push the kernel head IS the head that was read. ### **AFTER THIS ACT'S OWN COMMIT IT IS NOT --
    # ### AND DEMANDING EQUALITY WOULD BE DEMANDING THAT THIS ACT NOT HAVE HAPPENED.** ### The reading
    # ### that carries either way: ### **THE READ HEAD IS STILL AN ANCESTOR, AND EVERY COMMIT SINCE IS
    # ### ### THIS ACT'S OWN.**
    now = git(KERNEL, 'rev-parse', 'HEAD').strip()
    since = [x for x in git(KERNEL, 'log', '--format=%H %s',
                            '%s..HEAD' % C['head']).splitlines() if x.strip()]
    anc = subprocess.run(['git', '-C', KERNEL, 'merge-base', '--is-ancestor', C['head'], 'HEAD'],
                         capture_output=True).returncode == 0
    r4 = anc and all('(b368)' in x for x in since)
    r4side = 'BEFORE THE PUSH' if now == C['head'] else 'AFTER THE PUSH'
    r5 = 'PINNED BY `ls-remote` BEFORE THE FIRST CLASSIFICATION' in bank
    gr = r1 and r2 and r3 and r4 and r5
    print('    the ref `%s` = `%s` is named in the bank : %s' % (C['ref'], C['head'][:7], r1))
    print('    ### **LOCAL HEAD == ls-remote** : %s ; working tree clean at the read : %s' % (r2, r3))
    print('    ### **AND THE READ HEAD IS STILL AN ANCESTOR, EVERY COMMIT SINCE BEING THIS ACT’S OWN** '
          ': %s ### (read %s ; %d commit(s) since)' % (r4, r4side, len(since)))
    for x in since:
        print('        | %s' % x[:96])
    print('    and the bank says the pin came first : %s' % r5)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-REF')

    print(chr(10) + '  G-REDERIVED (BAR 1: the count is this act’s own; no prior figure is an input):')
    src = strip_prose(t('b368_classify.py'))
    e1 = C['n_present'] + C['n_absent'] == C['exported']
    e2 = C['b367_absent_constant'] == 18 and C['agrees_with_b367'] is True
    # ### **THE CONSTANT IS PRESENT IN THE CLASSIFIER AND MUST BE USED ONLY IN A COMPARISON.** ### The
    # ### arm reads the STRIPPED source and demands the constant never reach the absent list.
    e3 = ('B367_ABSENT' in src) and not re.search(r'absent\s*=\s*.*B367_ABSENT', src)
    e4 = 'RE-DERIVED, NOT CARRIED' in bf and 'COMPARISON ONLY' in bank
    e5 = C['head_moved_since_b367'] is False
    ge = e1 and e2 and e3 and e4 and e5
    print('    the kinds partition the exported list (%d + %d == %d) : %s'
          % (C['n_present'], C['n_absent'], C['exported'], e1))
    print("    ### **AND THE TWO INDEPENDENT DERIVATIONS AGREE** : %s (b367 said %d)"
          % (e2, C['b367_absent_constant']))
    print('    ### **THE PRIOR FIGURE IS A COMPARISON, NEVER AN INPUT** (read on stripped code) : %s' % e3)
    print('    the bank says so : %s ; the head is the same object b367 read : %s' % (e4, e5))
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-REDERIVED')

    print(chr(10) + '  G-CLASSIFY (one row each, four kinds, and the kinds partition the list):')
    kinds = {}
    for row in C['rows']:
        kinds[row['kind']] = kinds.get(row['kind'], 0) + 1
    c1 = len(C['rows']) == C['exported']
    c2 = len(set(x['name'] for x in C['rows'])) == C['exported']
    c3 = set(kinds) <= {'PRESENT', 'RETIRED', 'RENAMED', 'NEVER EXISTED'}
    c4 = kinds == C['kinds']
    c5 = C['renamed_rows'] == kinds.get('RENAMED', 0) and C['declared_successors'] == {}
    gc = c1 and c2 and c3 and c4 and c5
    print('    rows : %d, one per exported name : %s ; every name distinct : %s'
          % (len(C['rows']), c1, c2))
    print('    every kind is one of the four : %s %s' % (c3, kinds))
    print('    ### **AND `RENAMED %d` COMES FROM AN EMPTY DECLARED MAPPING, NOT FROM NOT LOOKING** : %s'
          % (C['renamed_rows'], c5))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CLASSIFY')

    print(chr(10) + '  G-EVIDENCE (BAR 2: no name is classified from its own sound):')
    noev = [x['name'] for x in C['rows'] if not x.get('evidence')]
    pres_bad = [x['name'] for x in C['rows'] if x['kind'] == 'PRESENT'
                and not (x['evidence'].get('file', '').endswith('.lean')
                         and x['evidence'].get('line'))]
    ret_bad = [x['name'] for x in C['rows'] if x['kind'] == 'RETIRED'
               and not (x['evidence'].get('line') or x.get('history'))]
    v1 = not noev and not pres_bad and not ret_bad
    v2 = (C['retired_named_by_ledger'] + C['retired_layer_only']) == kinds.get('RETIRED', 0)
    v3 = 'NO NAME IS CLASSIFIED FROM ITS OWN SOUND' in bf
    # ### **THE FIRST VERSION OF THIS ARM ASKED EVERY RETIRED ROW FOR A HISTORY AND GOT `False`.** ### The
    # ### classifier reads the history only where the ledger does NOT name the declaration; where it does,
    # ### the ledger line IS the evidence. ### **THE ARM WAS RIGHT TO FIRE -- THE BANK HAD CLAIMED A
    # ### ### SEARCH IT HAD NOT RUN** -- and the arm now states the true requirement, which is STRICTER
    # ### than "some evidence": ### **EACH GROUP MUST CARRY THE EVIDENCE ITS OWN KIND REQUIRES.**
    named_rows = [x for x in C['rows'] if x['kind'] == 'RETIRED'
                  and x['note'] == 'named by the ledger itself']
    rest_rows = [x for x in C['rows'] if x['kind'] == 'RETIRED'
                 and x['note'] != 'named by the ledger itself']
    layer_rows = [x for x in rest_rows if x['evidence'].get('line')]
    hist_rows = [x for x in rest_rows if not x['evidence'].get('line')]
    v4a = all(x['evidence'].get('line') and x['name'] in x['evidence'].get('text', '')
              for x in named_rows)
    v4b = all(x.get('history') and x['evidence'].get('line') for x in layer_rows)
    v4c = all(x.get('history') for x in hist_rows)
    # ### **AND THE NOTE MUST NOT DESCRIBE EVIDENCE THE ROW DOES NOT CARRY** -- the defect this arm found.
    v4d = not [x for x in hist_rows if 'LAYER entry is quoted' in x['note']]
    v4 = (v4a and v4b and v4c and v4d
          and len(named_rows) == C['retired_named_by_ledger']
          and len(layer_rows) == C['retired_layer_entry']
          and len(hist_rows) == C['retired_history_only'])
    v5 = ('THE HISTORY WAS READ' in bf
          and 'FOR THE SECOND AND THIRD GROUPS AND NOT FOR THE FIRST' in bf
          and 'HAS NO LEDGER ENTRY FOR ITS LAYER AT ALL' in bf)
    gv = v1 and v2 and v3 and v4 and v5
    print('    rows with no evidence : %s ; PRESENT rows without a declaration site : %s'
          % (noev or 'none', pres_bad or 'none'))
    print('    RETIRED rows with neither a ledger line nor a history : %s' % (ret_bad or 'none'))
    print('    ### **THE RETIRED SPLIT IS EXHAUSTIVE (%d named + %d layer-only == %d)** : %s'
          % (C['retired_named_by_ledger'], C['retired_layer_only'], kinds.get('RETIRED', 0), v2))
    print('    ### **EACH GROUP CARRIES THE EVIDENCE ITS OWN KIND REQUIRES** -- the %d the ledger NAMES '
          'carry the ledger line that names them : %s' % (len(named_rows), v4a))
    print('    ### **AND THE %d COVERED BY A LAYER ENTRY CARRY BOTH THAT ENTRY AND A HISTORY** : %s'
          % (len(layer_rows), v4b))
    print('    ### **AND THE %d WITH NO LEDGER ENTRY AT ALL CARRY A HISTORY** : %s ### **AND NO NOTE '
          'CLAIMS A LAYER ENTRY THEY DO NOT HAVE** : %s' % (len(hist_rows), v4c, v4d))
    print('    ### **AND THE BANK KEEPS THE THREE APART RATHER THAN CLAIMING ONE SEARCH** : %s' % v5)
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-EVIDENCE')

    print(chr(10) + '  G-BRANCH (the branch was DECIDED by the classification, and the other shown '
                    'unreachable):')
    b1 = R['branch'] == 'APPEND-ONLY RECONCILIATION'
    b2 = 'BRANCH TAKEN: (APPEND-ONLY RECONCILIATION)' in gate_text.flat(bank)
    b3 = 'IS UNREACHABLE HERE' in bf and 'the reason is printed by the' in bank
    b4 = 'THE BRANCH WAS DECIDED, NOT CHOSEN' in bf
    gb = b1 and b2 and b3 and b4
    print('    the reconciler recorded the branch : %s (%r)' % (b1, R['branch']))
    print('    the bank names it : %s ; the other is shown unreachable WITH ITS REASON : %s' % (b2, b3))
    print('    and it is decided rather than chosen : %s' % b4)
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BRANCH')

    print(chr(10) + '  G-APPENDONLY (BAR 3: no existing sentence edited) ### READ BEFORE THE PUSH:')
    ab = blob_of(KERNEL, 'AGENTS.md')
    a1 = agents.count(CURRENCY_MARK) == 1
    a2 = (ab is not None) and norm(agents).startswith(norm(ab).rstrip(chr(10)))
    a3 = R['prefix_of_file'] and R['prefix_of_blob'] and R['side'] == 'BEFORE THE PUSH'
    blk = agents.split(CURRENCY_MARK)[-1]
    a4 = R['block_exports_nothing'] and R['export_shaped_lines'] == 0 and not R['unstatused']
    # ### **AND THE ARM RE-MEASURES THE BLOCK ITSELF RATHER THAN TRUSTING THE WRITER'S OWN JSON.**
    shape = re.compile(r'^- \*\*[^*]+\*\*:.*`')
    a5 = not [ln for ln in blk.split(chr(10)) if shape.match(ln)]
    a6 = R['list_above_still_exports_absent'] == C['n_absent']
    ga = a1 and a2 and a3 and a4 and a5 and a6
    print('    the currency mark appears once : %s ; the committed blob is a true prefix : %s' % (a1, a2))
    print('    the writer recorded append-only both ways, before the push : %s' % a3)
    print('    ### **THE BLOCK EXPORTS NOTHING** (writer: %s ; re-measured here: %s)' % (a4, a5))
    print('    ### **AND THE LIST ABOVE IT STILL EXPORTS %d, UNEDITED** : %s'
          % (R['list_above_still_exports_absent'], a6))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOLEAN (### **NO `.lean` FILE TOUCHED, NO BUILD RUN**) ### BEFORE THE PUSH:')
    kstat = [x for x in git(KERNEL, 'status', '--porcelain').splitlines() if x.strip()]
    leanish = [x for x in kstat if x.strip().endswith('.lean')]
    n1 = not leanish
    n2 = R['lean_touched'] == 0 and F['lean_touched'] == 0 and C['lean_written'] == 0
    n3 = C['build_run'] is False
    n4 = [x[3:].strip() for x in kstat] in ([], ['AGENTS.md'])
    gn = n1 and n2 and n3 and n4
    print('    `.lean` files dirty in SIDE-effects : %s' % (leanish or 'none'))
    print('    the writers recorded it too : %s ; build run : %s' % (n2, C['build_run']))
    print('    ### **AND THE ONLY DIRTY PATH IS THE FRONT DOCUMENT** : %s %s'
          % (n4, [x[3:].strip() for x in kstat]))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOLEAN')

    print(chr(10) + '  G-HOOKFILED (the hook absence is FILED AS A FINDING and NOT repaired):')
    hookpath = os.path.join(KERNEL, '.git', 'hooks', 'pre-push')
    k1 = not os.path.exists(hookpath)
    k2 = 'HAS NO PRE-PUSH HOOK' in bf
    k3 = 'IT IS NOT REPAIRED HERE' in bf and 'FILED AS A FINDING AND ROUTED' in bf
    k4 = 'BEFORE THE LOCK' in bf and '(A-PRE)' in reg
    k5 = GN.absent_exact(BANK, '### THE HOOK WAS INSTALLED.')
    gk = k1 and k2 and k3 and k4 and k5
    print('    SIDE-effects still has no pre-push hook : %s' % k1)
    print('    the bank says so : %s ; and says it is filed, not repaired : %s' % (k2, k3))
    print("    ### **AND THE PRE-LOCK CHECK IS DECLARED ON THE REGISTRATION'S OWN FACE** : %s" % k4)
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-HOOKFILED')

    print(chr(10) + '  G-DESKRULE (the rule is filed beside the two arm species, LOCAL ONLY):')
    mod = io.open(MODULE, encoding='utf-8').read() if os.path.exists(MODULE) else ''
    mn = GN.norm(mod)
    d1 = os.path.exists(MODULE) and K['module_ok'] is True
    d2 = sorted(K['siblings']) == ['DATED_ARM.md', 'WRONG_ARM.md']
    d3 = GN.norm('RE-VERIFIED before it is ordered') in mn
    d4 = GN.norm('cannot enforce the TRUTH') in mn and GN.norm('and it closes nothing') in mn
    d5 = 'b367' in mod and 'b157' in mod
    ahead = git(TC, 'rev-list', '--count', 'origin/main..HEAD').strip()
    d6 = K['pushed'] is False and ahead.isdigit() and int(ahead) > 0
    d7 = not git(TC, 'status', '--porcelain').strip()
    gd = d1 and d2 and d3 and d4 and d5 and d6 and d7
    print('    the module exists and its writer passed : %s ; the two arm species beside it : %s'
          % (d1, d2))
    print('    the rule is stated in its own words : %s' % d3)
    print('    ### **AND IT STATES ITS OWN LIMIT AND CLOSES NOTHING** : %s' % d4)
    print('    both incidents named : %s' % d5)
    print('    ### **LOCAL ONLY: %s COMMITS AHEAD OF origin/main, NOT PUSHED** : %s ; tree clean : %s'
          % (ahead, d6, d7))
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-DESKRULE')

    print(chr(10) + '  G-SWEEP (every desk item carries a mark, and the sweep states its own reach):')
    marks = K['marks']
    s1 = len(marks) == K['items'] and K['items'] == 9
    s2 = all(m['mark'] in ('CONFIRMED-BY-FILE', 'UNCONFIRMED') for m in marks)
    s3 = all((m['hit'] is not None) == (m['mark'] == 'CONFIRMED-BY-FILE') for m in marks)
    s4 = all(m['hit'] and not m['hit']['file'].startswith('data/b368_')
             for m in marks if m['mark'] == 'CONFIRMED-BY-FILE')
    s5 = 'A FILE THAT MENTIONS AN ITEM IS NOT A FILE THAT CONFIRMS IT' in bf
    s6 = (K['confirmed'] + K['unconfirmed']) == K['items']
    gs = s1 and s2 and s3 and s4 and s5 and s6
    print('    items swept : %d ; every mark is one of the two : %s' % (len(marks), s2))
    print('    every CONFIRMED mark carries its file and every UNCONFIRMED carries none : %s' % s3)
    print("    ### **AND NO ITEM IS CONFIRMED FROM THIS ACT'S OWN PAPERWORK** : %s" % s4)
    print('    ### **AND THE SWEEP STATES ITS OWN REACH** : %s ; the counts add up : %s' % (s5, s6))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SWEEP')

    print(chr(10) + '  G-NOCLOSE (### **NO DESK ITEM IS CLOSED BY THIS ACT**):')
    z1 = K['items_closed'] == 0
    z2 = 'AND `0` ITEMS CLOSED' in bank
    z3 = 'marks, not verdicts' in bf.lower() or 'MARKS, NOT VERDICTS' in bf
    z4 = GN.absent_exact(BANK, '### A DESK ITEM IS CLOSED.')
    z5 = F['closed'] is False and F['status'] == 'UPDATED, NOT CLOSED'
    gz = z1 and z2 and z3 and z4 and z5
    print('    items closed : %d : %s ; the bank says so : %s' % (K['items_closed'], z1, z2))
    print('    the bank says marks, not verdicts : %s' % z3)
    print('    ### **AND THE TRAIL ITSELF IS MARKED %r** : %s' % (F['status'], z5))
    print('    %s' % ('PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-NOCLOSE')

    print(chr(10) + '  G-TRAIL (one append-only block; b157’s and b367’s not edited) ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    t3 = F['prefix_of_file'] and F['prefix_of_blob']
    t4 = trails.count(B367_MARK) == 1 and F['names_b367_block'] is True
    t5 = trails.count("THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED") == 1
    t6 = F['naked_kernel_names'] == 0
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    the mark appears once : %s ; the committed blob is a true prefix : %s' % (t1, t2))
    print('    the writer recorded append-only both ways : %s' % t3)
    print("    ### **AND b367'S BLOCK AND b157'S SENTENCE ARE EACH STILL THERE EXACTLY ONCE** : %s / %s"
          % (t4, t5))
    print('    every kernel name in the block is inside backticks : %s' % t6)
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s) ### BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL' in rows[0]
            and 'STILL EXPORTS' in rows[0] and 'NO DESK ITEM IS CLOSED' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTCLOSED:')
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    kk1 = 'READ BACK : front-document-reconciled returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the export list is repaired', 'the eighteen are removed',
               'a successor is named', 'the desk is confirmed'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    kk4 = 'ANNOTATED, NOT REPAIRED' in idx and 'STILL EXPORTS' in idx
    gkk = kk1 and kk2 and kk3 and kk4
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (kk1, kk2, kk3))
    print('    ### **AND THE KEY ITSELF SAYS THE DOCUMENT IS ANNOTATED, NOT REPAIRED** : %s' % kk4)
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTCLOSED')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock) ### '
                    'SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, C, R, K, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    go = o1 and o2 and o3 and o4 and o5
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('        lock %s ; extract %s ; classify %s' % (stampm.group(1) if stampm else '?',
                                                          E['run_clock'], C['run_clock']))
    print('        reconcile %s ; desk %s ; filing %s' % (R['run_clock'], K['run_clock'],
                                                          F['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE ANY WRITE : %s'
          % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### AFTER THE PUSH:')
    hookp, mirrorp = d('b368_hooks.txt'), d('b368_mirror.txt')
    gh2 = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror clean : %s'
              % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    cl = re.search(r'clauses\s*:\s*(\d+)', sat)
    sm = re.search(r'### bytes locked : (\d+)', reg)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [
        ('exported %d' % C['exported'], ('OF THE %d NAMES' % C['exported']) in bf),
        ('present %d' % C['n_present'], ('`%d` ARE DECLARED' % C['n_present']) in bf),
        ('absent %d' % C['n_absent'], ('`%d`' % C['n_absent']) in bank),
        ('every absent is retired', ('EVERY ONE OF THE %d IS `RETIRED`' % C['n_absent']) in bf),
        ('renamed %d' % C['renamed_rows'], ('`RENAMED`: %d' % C['renamed_rows']) in bank),
        ('named by the ledger %d' % C['retired_named_by_ledger'],
         ('`%d` of the `%d` retired names' % (C['retired_named_by_ledger'], C['n_absent'])) in bf),
        ('covered by a layer entry %d' % C['retired_layer_entry'],
         ('`%d` are covered only by' % C['retired_layer_entry']) in bf),
        ('no ledger entry for their layer %d' % C['retired_history_only'],
         ('AND `%d` HAS NO LEDGER ENTRY FOR ITS LAYER AT ALL' % C['retired_history_only']) in bf),
        ('the read ref', C['head'] in bank),
        ('AGENTS.md grew by %d bytes' % R['grew'], ('grew by %d bytes' % R['grew']) in bf),
        ('the list still exports %d' % R['list_above_still_exports_absent'],
         ('STILL EXPORTS %d ABSENT NAMES' % R['list_above_still_exports_absent']) in bf),
        ('the trail block grew the file by %d bytes' % F['grew'], str(F['grew']) in bank),
        ('reads %d' % E['reads'], ('%d READS' % E['reads']) in bf),
        ('without an anchor %d' % E['without_anchor'],
         ('`%d` WITHOUT AN ANCHOR' % E['without_anchor']) in bf),
        ('anchors differing %d of %d' % (E['anchors_differing'], E['reads']),
         ('%d of %d anchors DIFFER' % (E['anchors_differing'], E['reads'])) in bf),
        ('ledger lines %d' % E['ledger_lines'],
         ("%d lines located inside the kernel's ledger" % E['ledger_lines']) in bf),
        ('desk items %d' % K['items'], ('`%d` ITEMS' % K['items']) in bank),
        ('confirmed %d / unconfirmed %d' % (K['confirmed'], K['unconfirmed']),
         ('`%d` CONFIRMED-BY-FILE, `%d` UNCONFIRMED' % (K['confirmed'], K['unconfirmed'])) in bf),
        ('modules now %d' % K['modules_now'], ('`%d` modules now' % K['modules_now']) in bank),
        ('row %s' % rn, rn == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'),
         ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'),
         ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on desk run file', K['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks):')
    once = True
    for lbl, jf in (('extract', E), ('classify', C), ('reconcile', R), ('desk', K), ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-10s %-26s clock on disk %s == the JSON's %s : %s"
              % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    reps = {}
    for pat, jf in ((r'^b368_extract_notes\d*\.txt$', E), (r'^b368_desk_notes\d*\.txt$', K)):
        got = sorted(f for f in os.listdir(D) if re.match(pat, f))
        reps[jf['run_file']] = got
        named = jf['run_file'] in bank
        once = once and named and len(got) > 0
        print('    ### **%d REPEATS; THE RELIED-ON ONE IS NAMED IN THE BANK : %s** %s'
              % (len(got), named, got))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed about the object, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b368_') and x.endswith('.py')))
    for p in [t(x) for x in mymods]:
        src3 = strip_prose(p)
        for b in banned:
            if b in src3:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits and not imports
    print("    numerical calls in this act's STRIPPED sources : %d %s" % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-BYCONTENT (### **(R2): NO ARM OF THIS ACT IS WRITTEN BY ADDRESS**):')
    mine = [t(x) for x in mymods]
    selfhits = []
    for p in mine:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    SELF_DECLARED = {
        ('b368_correspondence.py', 'last-row cells'):
            'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE -- to count its cells; '
            'the same shape `b366` classified NOT AN ADDRESS PREDICATE at `b326` and `b335`.',
        ('b368_checks.py', 'last-row cells'):
            'the same shape, in the arm that re-reads the row this act just wrote.',
    }

    def which(fn, code):
        if '[-1:]' in code or '[-1]' in code:
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

    print(chr(10) + '  G-NOEDIT (only this act’s paths; no other act’s files) ### BEFORE THE PUSH:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/gate_content.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py',
             'tools/b366_sweep.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').splitlines()
              if x.strip() and 'b368' not in x and x.strip() != 'tools/banked_index.py']
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines()
              if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'OPEN_TRAILS.md']
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    gne = (not touched and not others and not ppbad and faces_clean and hand and fnd)
    print('    owner instruments modified : %s' % (touched or 'none'))
    print('    ### **TRACKED RELAY FILES OF OTHER ACTS MODIFIED : %s**' % (others or 'none'))
    print('    papers paths beyond OPEN_TRAILS.md : %s' % (ppbad or 'none'))
    print('    ### **FACES_LEDGER.md UNTOUCHED, BECAUSE NO ROW MOVED** : %s' % faces_clean)
    print('    HANDOFF clean : %s ; FINDINGS clean : %s' % (hand, fnd))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS, GATE,
             d('b368_satisfiable.json'),
             t('b368_regspec.py'), t('b368_extract.py'), t('b368_reconcile.py'),
             t('b368_bank.py'), t('b368_correspondence.py'), t('b368_index_append.py')]
    CARRIERS = [
        (t('b368_checks.py'), 'its own fixtures'),
        (FERRY, "IT IS THE ORDER -- not this act's writing"),
        (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
        (d(E['run_file']), "the extract file carries the kernel's own words"),
        (d(C['run_file']), "the classify file carries the kernel's own names and ledger lines"),
        (d(R['run_file']), "the reconcile file carries the block's own text"),
        (d(K['run_file']), "the desk file carries the fold's own sentence"),
        (d(F['run_file']), "the filing file carries the kernel's own quoted heading"),
        (t('b368_classify.py'), "ITS SEARCH STRINGS ARE THE FRONT DOCUMENT'S AND THE LEDGER'S OWN "
                                "HEADINGS -- a search string is a needle, and b348 says the needle is "
                                "never softened"),
        (t('b368_desk.py'), "ITS DESK ROWS ARE THE FOLD'S OWN ITEM NAMES"),
        (t('b368_filing.py'), "it quotes the kernel's own ledger heading"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    # ### **`ferry_scan`'s STEM LIST IS RAW: IT CARRIES NONE OF THE RECORD'S DECLARED EXCEPTIONS.** ### So
    # ### a stem hit here is NOT a verdict. ### **IT IS COUNTED, PRINTED, AND HANDED TO THE SHARED
    # ### ### SCANNER, WHICH DECIDES** -- and the arm requires that scanner's LIVE count to be `0`.
    # ### **THE HIT IS NEVER DROPPED AND NEVER EXCUSED BY THIS SUITE'S OWN JUDGEMENT** (`b234`'s rule).
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
            for hh in (ch + sh)[:6]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
        if sh:
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', p],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            live = re.search(r'live uses\s*:\s*(\d+)', rr.stdout or '')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **HANDED TO THE SHARED SCANNER -- live uses : %s ; CLEAN : %s**'
                  % (live.group(1) if live else '?', clean))
            if not clean:
                live_bad.append(os.path.basename(p))
    print('    files scanned %d   struck-clause hits %d   stem hits %d   ### **LIVE USES AFTER THE '
          'SHARED SCANNER : %d** %s'
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

    marker = '# ### THE FRONT DOCUMENT RECONCILED, APPEND-ONLY (b368).'
    nxt = '# ### THE SCAFFOLD REPAIR, NOT LOCATED (b367).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    cblk = agents.split(CURRENCY_MARK)[-1] if CURRENCY_MARK in agents else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the currency block, the index row):'
          % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''),
                      ('the trail block', tblk), ('the currency block', cblk),
                      ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            # ### **A STEM HIT HERE IS EXPECTED AND MUST BE A QUOTED KERNEL IDENTIFIER.** ### The arm
            # ### does not excuse it: it hands it to the SHARED SCANNER and demands the LIVE count be 0.
            tmp = os.path.join(tempfile.mkdtemp(prefix='b368_stem_'), 'blk.txt')
            io.open(tmp, 'w', encoding='utf-8', newline=chr(10)).write(blk2)
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', tmp],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **%d STEM HITS, HANDED TO THE SHARED SCANNER: LIVE USES 0 : %s**'
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the blocks, the index row):')
    tmpdir = tempfile.mkdtemp(prefix='b368_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', tblk),
                      ('the currency block', cblk), ('the index row', ib2)):
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
