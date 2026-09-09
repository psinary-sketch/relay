# -*- coding: utf-8 -*-
"""b378_checks.py -- THE GATE SUITE FOR THE REFS WIDENED AND THE CONVENTION SWEPT.

### ### **THE ARMS THAT MATTER MOST HERE ARE THE ONES THAT MEASURE WHAT THIS ACT DID *NOT* DO:**
### `G-NORULING`, `G-NOPREFER`, `G-OPEN`, `G-NOWRITE`. ### The order forbids ruling a class,
### reclassifying a document, writing a class line, repairing a document and closing a list; ### **EACH
### ### OF THE FIVE HAS ITS OWN MUST-FAIL FIXTURE AS A WHOLE LINE.**
### ### **AND `G-EVERYGATE` RE-READS THE LOCK GATE'S OWN RECORD**, because Step Zero's whole point is
### that the lock was chained on a tool that reads every gate. ### **AN ACT THAT CURES A GATE FAILURE
### ### AND DOES NOT MEASURE THE CURE HAS NOT CURED IT.**
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`), and ### **AN ARM THAT WOULD FAIL ON A PRE-EXISTING CONDITION IS NOT MEASURING
### ### THIS ACT** (`b375`).
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
import b317_checks as K7  # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN  # noqa: E402
import b366_sweep as SW   # noqa: E402
import b303_pins          # noqa: E402
import gate_hash          # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b378_the_refs_widened.txt')
REG = d('b378_registration_2026-09-08.txt')
FERRY = d('b378_ferry_2026-09-08.txt')
IDX = d('b378_desk_notes.txt')
SCAN, TERMSCAN, GATE = d('b378_ferry_scan.txt'), d('b378_reg_termscan.txt'), d('b378_reg_gate.txt')
CENSUS0, FCEN = d('b378_census_stepzero.txt'), d('b378_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b378_regspec_run.txt'), d('audit_b378_reg_satisfiable.txt')
PINS0 = d('b378_pins_stepzero.txt')
SEAL = 'cf491cc04ea5d6406eeb2f48de48e17dd7e1d77b170d51544c2953d405693873'
ROWNUM = '227'
TRAIL_MARK = '<!-- b378 the refs widened and the convention swept -->'


_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b378_reads.json'), ('LG', 'b378_lockgate.json'),
                   ('TM', 'b378_terminals.json'), ('AR', 'b378_archives.json'),
                   ('HD', 'b378_hand.json'), ('Q', 'b378_desk.json'))}

NEW_THIS_ACT = {'tools/gate_hash.py', 'tools/b378_lockgate.py', 'tools/b378_regspec.py',
                'tools/b378_extract.py', 'tools/b378_reg_gate.py', 'tools/b378_terminals.py',
                'tools/b378_archives.py', 'tools/b378_hand.py', 'tools/b378_desk.py',
                'tools/b378_bank.py', 'tools/b378_checks.py'}

TOOLNUM = [
    ('STEP ZERO -- the stamp the lock can compare (SHARED)', 'tools/gate_hash.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('every ref, both conventions, and a positive control', 'tools/b378_terminals.py'),
    ('the archives, by digest and title line', 'tools/b378_archives.py'),
    ('one NOT DETERMINABLE document, read by hand', 'tools/b378_hand.py'),
    ('(R7), the trail block, the row and the key', 'tools/b378_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b378_bank.py'),
    ('the reads', 'tools/b378_extract.py'),
    ('the registration gate', 'tools/b378_reg_gate.py'),
    ('the clause spec', 'tools/b378_regspec.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
KCENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
PP_RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b378 - THE REFS WIDENED AND THE CONVENTION SWEPT. The'),
    ('the order -- the draft adopted with three additions', FERRY,
     "executor's draft is ADOPTED, with three additions."),
    ('the order -- the lock re-checked if the face is rewritten', FERRY,
     'gate and RE-CHECKED if the registration is rewritten - b377'),
    ('the order -- addition one, every ref not main', FERRY,
     'ADDITION ONE - EVERY REF, NOT MAIN: re-run the terminal search'),
    ('the order -- addition one, an upper bound at one ref', FERRY,
     'the corrected classification and state plainly that the earlier'),
    ('the order -- addition one, the held branch by name', FERRY,
     'names a held branch in its own text, that branch is searched by'),
    ('the order -- addition two, the two conventions', FERRY,
     'ADDITION TWO - THE TWO CONVENTIONS: the corpus writes terminal'),
    ('the order -- addition two, a discrimination arm', FERRY,
     'polarities and a discrimination arm proving it still refuses a'),
    ('the order -- addition two, none is rewritten', FERRY,
     'documents are correct in their own dialect and none is'),
    ('the order -- addition two, what the narrowness cost', FERRY,
     "rewritten. State what the earlier predicate's narrowness cost"),
    ('the order -- addition three, the archives', FERRY,
     'ADDITION THREE - THE ARCHIVES, CONFIRMED AND NOT REMOVED: for'),
    ('the order -- addition three, never by filename', FERRY,
     'content match - never by filename, since the repository strips'),
    ('the order -- addition three, remove nothing', FERRY,
     "nothing; the removal is the author's and depends on this"),
    ('the order -- the closing', FERRY,
     "CLOSING: the lock gate's remaining hole closed as the draft"),
    ("the order -- the navigator's expectations", FERRY,
     "the next ferry as DRAFT - NAVIGATOR EDITS. The navigator's"),
    ('the order -- (F2), a non-main ref', FERRY,
     'thirty-seven; (F2) at least one identifier is found on a'),
    ('the draft -- only main was searched', d('b377_closing.txt'),
     "### ### **AND `b377`'S BRANCH TOOL SEARCHED ONLY `main` AT EACH KERNEL.**"),
    ('the draft -- close the hole in the tool', d('b377_closing.txt'),
     "### ### **COMPONENT 2 -- CLOSE THE LOCK GATE'S HOLE IN THE TOOL.**"),
    ('the draft -- the two by hand', d('b377_closing.txt'),
     '### ### **COMPONENT 3 -- THE TWO `NOT DETERMINABLE` DOCUMENTS, BY HAND.**'),
    ('the draft -- the author chooses the fourth', d('b377_closing.txt'),
     '### ### **THIS DRAFT DOES NOT CHOOSE BETWEEN COMPONENT 4 AND THE REST; THE AUTHOR DOES.**'),
    ('the held branch -- the document names it', PP_RESIDUE,
     'The seven branch artifacts and the edge lemma, at their pins with `#print axioms` profiles,'),
    ("the taxonomy -- Tier K and what it obliges", TAX, '**Tier K — Keystone-certified.**'),
]

SELF_NEEDLES = [
    ('the bank leads with the upper bound and the broken search', BANK,
     '### ### ### **AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT** -- and ### **A SEARCH THAT '
     'CANNOT'),
    ('### the earlier number was never wrong', BANK,
     'IT WAS AN UPPER BOUND TAKEN AT ONE REF AND WAS NOT'),
    ('### a clean confident entirely false answer', BANK,
     'A CLEAN, CONFIDENT, ENTIRELY FALSE ANSWER.'),
    ('### exposed only by a contradiction', BANK,
     'IT WAS EXPOSED ONLY BY A CONTRADICTION WITH `b377`S OWN RECORD'),
    ('### an exit code above 1 is an error', BANK,
     'AN EXIT CODE ABOVE 1 IS AN ERROR AND NOT AN ANSWER'),
    ('### it refuses until it can find a presence', BANK,
     'REFUSES TO REPORT AN ABSENCE UNTIL IT HAS PROVED IT CAN FIND A'),
    ('### the face was rewritten and every gate re-stamped', BANK,
     'THIS ACT`S OWN FACE WAS REWRITTEN BEFORE THE LOCK'),
    ('### what the stamp still does not prove', BANK,
     'THE CALLER`S CLAIM ABOUT WHAT IT FED THE GATE'),
    ('### the branch was searched and the answer is still no', BANK,
     'THE BRANCH WAS SEARCHED BY NAME AND THE ANSWER THERE IS STILL NO.'),
    ('### not one document uses dotted alone', BANK,
     'NOT ONE OF THEM USES THE DOTTED CONVENTION ALONE.'),
    ('### the cost is not hypothetical', BANK, 'THE COST IS NOT HYPOTHETICAL:'),
    ('### the axis-B column is suspect and not re-measured', BANK,
     'HERE AS SUSPECT AND IS NOT RE-MEASURED'),
    ('### b375 is unaffected, so the suspicion is bounded', BANK,
     'than free-floating.'),
    ('### neither dialect is rewritten', BANK,
     'NO DOCUMENT IS REWRITTEN INTO THE OTHER DIALECT.'),
    ('### confirmed by digest and title, never by filename', BANK,
     'CONFIRMED BY A VERIFIED DIGEST AND BY A TITLE LINE. ### NEVER BY FILENAME'),
    ('### the removal is the author`s', BANK,
     'NOTHING WAS REMOVED, MOVED OR RENAMED. ### THE REMOVAL IS THE AUTHOR`S AND DEPENDS'),
    ('### the hand read decides what the scan could not', BANK,
     'WHAT THE HAND READ DECIDES THAT THE TABLE SCAN COULD NOT:'),
    ('### the outcome is a mark, not a class', BANK,
     'THE OUTCOME IS A MARK, NOT A CLASS.'),
    ('### the clusters stay filed and not opened', BANK,
     'THE SIX SUBJECT CLUSTERS STAY FILED AND NOT OPENED.'),
    ('### the reading was declared in advance', BANK,
     'ADVANCE, WHERE THE AUTHOR CAN CORRECT IT'),
    ('### a rule minted is not a rule carried', BANK,
     'DID THE SAME THING AND HAD TO BE CORRECTED.'),
    ('### (E3) refuted without softening', BANK,
     'THAT NAMES ITS OWN SOURCE AND IS STILL WRONG'),
    ('### the four lists restated open in the desk`s own words', BANK,
     'THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS:'),
]

MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a declaration was moved', BANK, '### A DECLARATION WAS MOVED.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never says a document was rewritten', BANK, '### A DOCUMENT WAS REWRITTEN.'),
    ('the bank never says an archive was removed', BANK, '### AN ARCHIVE FILE WAS REMOVED.'),
    ('the bank never says a name was confirmed without being found', BANK,
     '### A NAME WAS CONFIRMED WITHOUT BEING FOUND.'),
]

PREFER = re.compile(r'\b(recommend\w*|prefer\w*|the best option|should be adopted|we advise|'
                    r'the right choice|obviously|clearly the|the correct option|I suggest)\b', re.I)


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
    print('b378 -- GATE SUITE (THE TWO-AXIS READ)')
    print('=' * 100)
    E, LG, TM, AR, HD, Q = (_J['E'], _J['LG'], _J['TM'], _J['AR'], _J['HD'], _J['Q'])
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 200:
                inx = line.rstrip()[:200] in extract
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
    print(chr(10) + '  MUST-FAIL FIXTURES ### (THE ORDER`S FIVE PROHIBITIONS, AS WHOLE LINES):')
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

    # ------------------------------------------------------------- BAR 1, THE STAMPED-GATE BAR
    print(chr(10) + '  G-STAMPED / G-EVERYGATE / G-FIXTURE4 / G-NOSTALE (BAR 1):')
    lgrun = io.open(d(LG['run_file']), encoding='utf-8', errors='replace').read()
    l1 = LG['fixture_ok'] is True and LG['permits'] is True and LG['helper_ok'] is True
    l2 = LG['gates_read'] == LG['gates_passing'] == 8
    l3 = LG['face_subject_gates'] == 4
    l4 = all(g['passed'] for g in LG['gates'])
    # ### **THE STAMP MUST EQUAL THE FACE THAT WAS ACTUALLY LOCKED** -- and the comparison has a
    # ### subtlety worth stating: ### **`reg_seal` APPENDS A LOCK BLOCK**, so the file's bytes change
    # ### AFTER the stamp is taken. ### The stamp is a claim about the face the gates READ, which is
    # ### the body ABOVE the lock block -- exactly what the seal's own hash covers.
    # ### ### **HASHING THE WHOLE FILE HERE WOULD COMPARE THE STAMP AGAINST BYTES NO GATE EVER SAW.**
    face_now = hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest()
    l5 = (LG['face_sha'] == face_now == SEAL)
    l6 = all(g['recorded'] == face_now for g in LG['gates'] if g['subject_is_face'])
    # ### **AND ALL FOUR POLARITIES, EACH REFUSING FOR ITS OWN GATE.**
    fx = LG['fixture']
    l7 = (fx['all gates clean']['permits'] is True
          and all(v['permits'] is False and len(v['failing']) == 1
                  for k, v in fx.items() if k != 'all gates clean')
          and len(fx) == 4)
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7
    print('    gates read %d / passing %d ; face-subject gates %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l4))
    for g in LG['gates']:
        print('      %-46s %-38s %s   stamp %s'
              % (g['gate'][:46], g['file'][:38], 'PASS' if g['passed'] else '### FAIL ###',
                 (g['recorded'] or '-')[:12] if g['subject_is_face'] else 'n/a'))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l5, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l6)
    for k, v in fx.items():
        print('      %-42s permits %-5s failing %s' % (k[:42], v['permits'], v['failing'] or 'none'))
    print('    ### **FOUR POLARITIES, EACH REFUSING FOR ITS OWN GATE** : %s' % l7)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4/G-NOSTALE')

    # ------------------------------------------------------------------ BAR 2, THE EVERY-REF BAR
    print(chr(10) + '  G-EVERYREF / G-REFSLIVE / G-HELDBRANCH (BAR 2):')
    r1 = TM['refs'] > TM['kernels']
    r2 = TM['prior_refs_searched'] == TM['kernels']
    r3 = TM['control_ok'] is True and TM['control_non_main'] >= 1
    r4 = len(TM['grep_errors']) == 0
    hb = TM['held_branch']
    r5 = bool(hb['refs']) and bool(hb['sentence']) and hb['name'] in hb['sentence']
    r6 = str(TM['refs']) in bank and str(TM['kernels']) in bank
    gr = r1 and r2 and r3 and r4 and r5 and r6
    print('    refs searched %d vs kernels %d ; b377 searched %d'
          % (TM['refs'], TM['kernels'], TM['prior_refs_searched']))
    print('    ### **THE SEARCH LEFT main** : %s' % r1)
    print('    ### **POSITIVE CONTROL HELD, ON %d NON-main COMMIT(S)** : %s'
          % (TM['control_non_main'], r3))
    print('    ### **SEARCHES THAT COULD NOT RUN : %d** -- an exit above 1 is an error, not an answer'
          % len(TM['grep_errors']))
    print('    ### **THE HELD BRANCH WAS SEARCHED BY NAME AND ITS SENTENCE QUOTED** : %s %s'
          % (r5, hb['refs']))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-EVERYREF/G-REFSLIVE/G-HELDBRANCH')

    # ----------------------------------------------------------------- BAR 3, THE TWO-DIALECT BAR
    print(chr(10) + '  G-DIALECT / G-DISCRIMINATE / G-SWEEP (BAR 3):')
    d1 = TM['fixtures_ok'] is True
    d2 = all(c['got'] is c['want'] for c in TM['fixtures'])
    # ### **THE MATCHER MUST ACCEPT BOTH DIALECTS AND STILL REFUSE.**
    accepts = [c for c in TM['fixtures'] if c['want'] is True]
    refuses = [c for c in TM['fixtures'] if c['want'] is False]
    d3 = len(accepts) >= 2 and len(refuses) >= 3
    d4 = any('BARE' in c['case'] and c['want'] for c in TM['fixtures'])
    d5 = any('DOTTED' in c['case'] and c['want'] for c in TM['fixtures'])
    d6 = len(TM['conventions']) == 6 and all(c['convention'] for c in TM['conventions'])
    gd = d1 and d2 and d3 and d4 and d5 and d6
    print('    matcher fixtures held : %s ; every case matched : %s' % (d1, d2))
    print('    ### **ACCEPTS BARE : %s ; ACCEPTS DOTTED : %s**' % (d4, d5))
    print('    ### **DISCRIMINATION ARM -- cases it must REFUSE : %d** : %s' % (len(refuses), d3))
    print('    citing documents swept : %d ; each carries a convention verdict : %s'
          % (len(TM['conventions']), d6))
    for c in TM['conventions']:
        print('      %-36s bare %-3d dotted %-3d  %s'
              % (os.path.basename(c['file'])[:-3][:36], c['bare'], c['dotted'], c['convention']))
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-DIALECT/G-DISCRIMINATE/G-SWEEP')

    # ----------------------------------------------------------------- BAR 4, THE CORRECTION BAR
    print(chr(10) + '  G-CORRECTION / G-UPPERBOUND / G-COST (BAR 4):')
    rows = TM['rows']
    c1 = len(rows) == TM['carried'] == 37
    c2 = all(r['classification'] for r in rows)
    c3 = sum(TM['tally'].values()) == len(rows)
    # ### **THE EARLIER FIGURE MUST BE RESTATED AS AN UPPER BOUND, IN THOSE WORDS.**
    c4 = 'UPPER BOUND TAKEN AT ONE REF' in gate_text.flat(bank)
    # ### **AND A NAME IN MORE THAN ONE KERNEL IS CLASSIFIED AS SUCH, NOT READ AS THE FIRST.**
    c5 = all((r['n_kernels'] > 1) == ('MORE THAN ONE KERNEL' in r['classification'])
             for r in rows if r['hits'])
    c6 = 'THE COST IS NOT HYPOTHETICAL' in gate_text.flat(bank)
    c7 = 'NOT RE-MEASURED' in gate_text.flat(bank)
    gc = c1 and c2 and c3 and c4 and c5 and c6 and c7
    print('    identifiers carried %d ; every one classified : %s ; tally sums : %s'
          % (len(rows), c2, c3))
    print('    ### **THE EARLIER FIGURE IS RESTATED AS AN UPPER BOUND AT ONE REF** : %s' % c4)
    print('    ### **A NAME IN MORE THAN ONE KERNEL IS CLASSIFIED AS SUCH** : %s' % c5)
    print('    the cost is stated : %s ; the suspect column is not re-measured : %s' % (c6, c7))
    print('    tally : %s' % TM['tally'])
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CORRECTION/G-UPPERBOUND/G-COST')

    # ------------------------------------------------------------------ BAR 5, THE NO-REWRITE BAR
    print(chr(10) + '  G-NOREWRITE / G-NOMOVE / G-NOREMOVE (BAR 5):')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b378' not in x and x != 'tools/banked_index.py'
                     and x != 'tools/gate_hash.py')
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    n1 = all(not v for v in dirtyrepo.values())
    # ### **NO CORPUS DOCUMENT WRITTEN INTO AT ALL** -- the six, the two, and every archive file.
    watched = ([r['file'] for r in _J['TM'].get('conventions', [])]
               + [HD['chosen']] + HD['other']
               + [r['source_path'] for r in AR['rows']])
    touched = []
    for rel in watched:
        cur = git(PP, 'diff', '--name-only', 'HEAD', '--', rel).strip()
        if cur:
            touched.append(rel)
    n2 = not touched
    n3 = AR['removed'] == 0
    n4 = HD['declaration_moved'] is False and HD['class_ruled'] is False and HD['bytes_written'] == 0
    frozen = [x for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and (x.startswith('outputs/') or x.startswith('archive/'))]
    n5 = not frozen
    gn = n1 and n2 and n3 and n4 and n5
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **CORPUS DOCUMENTS WRITTEN INTO : %d** %s' % (len(touched), touched or ''))
    print('    ### **ARCHIVE FILES REMOVED, MOVED OR RENAMED : %d**' % AR['removed'])
    print('    ### **ANYTHING UNDER archive/ CHANGED : %s**' % (frozen or 'none'))
    print('    the hand read moved no declaration and wrote no byte : %s' % n4)
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOREWRITE/G-NOMOVE/G-NOREMOVE')

    # ------------------------------------------------------------ BAR 6, THE ARCHIVE-EVIDENCE BAR
    print(chr(10) + '  G-ARCHIVE / G-DIGEST / G-NOTBYNAME (BAR 6):')
    ar1 = len(AR['rows']) == AR['ordered_population']
    ar2 = all(r['verdict'] for r in AR['rows'])
    # ### **EVERY CONFIRMATION RESTS ON A DIGEST *AND* A TITLE LINE, NEVER ON A NAME.**
    ar3 = all((('CONFIRMED PRESENT' in r['verdict']) ==
               (r['digest_match'] and r['title_match'])) for r in AR['rows'])
    ar4 = all(r['digest'] for r in AR['rows'] if 'CONFIRMED PRESENT' in r['verdict'])
    ar5 = all(r['missing'] for r in AR['rows'] if 'NOT CONFIRMED' in r['verdict'])
    ar6 = 'NEVER BY FILENAME' in gate_text.flat(bank)
    ar7 = 'CONTEXT, LABELLED AS CONTEXT' in gate_text.flat(bank) or (
        'CONTEXT' in bank and 'NOT THE ORDERED REPORT' in gate_text.flat(bank))
    ga = ar1 and ar2 and ar3 and ar4 and ar5 and ar6 and ar7
    print('    archive files reported %d of %d ; each with a verdict : %s'
          % (len(AR['rows']), AR['ordered_population'], ar2))
    print('    ### **CONFIRMED IFF DIGEST AND TITLE BOTH MATCH** : %s' % ar3)
    print('    every CONFIRMED carries a digest : %s ; every NOT CONFIRMED says what is missing : %s'
          % (ar4, ar5))
    print('    ### **THE BANK SAYS NEVER BY FILENAME** : %s ; the wider count is CONTEXT : %s'
          % (ar6, ar7))
    print('    confirmed %d / not confirmed %d' % (AR['confirmed'], AR['not_confirmed']))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ARCHIVE/G-DIGEST/G-NOTBYNAME')

    # ---------------------------------------------------- BAR 7, THE NO-RULING BAR / G-HAND / G-OPEN
    print(chr(10) + '  G-NORULING / G-HAND / G-OPEN / G-NONEWDOC (BAR 7):')
    h1 = HD['named'] > 0 and (HD['located'] + HD['ambiguous'] + HD['not_located']) == HD['named']
    h2 = all(r['sentence'] for r in HD['rows'])
    h3 = len(HD['other']) == 1
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    k1 = all(x in bank for x in lists)
    k2 = 'ARE RESTATED `OPEN` BY NAME' in bank
    # ### The trail block writes prose, not the bank's shouting caps; the CLAIM is the same
    # ### one and the arm reads it case-insensitively rather than demanding a register.
    k3 = 'open by name' in gate_text.flat(tblk).lower()
    k4 = Q['lists_closed'] == 0
    # ### **THE ONE CLOSURE IS THE LOCK GATE'S HOLE AND IT IS NOT A LIST.**
    k5 = Q['closed'] == 1 and all('lock gate' in c['item'] for c in Q['closed_items'])
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    k6 = not newdocs
    k7 = 'STAY FILED AND NOT OPENED' in gate_text.flat(bank)
    gk = h1 and h2 and h3 and k1 and k2 and k3 and k4 and k5 and k6 and k7
    print('    hand read : %d named = %d + %d + %d : %s ; every row carries its sentence : %s'
          % (HD['named'], HD['located'], HD['ambiguous'], HD['not_located'], h1, h2))
    print('    ### **THE OTHER NOT-DETERMINABLE DOCUMENT IS LEFT** : %s %s' % (h3, HD['other']))
    print('    the four lists named in the bank : %s ; restated OPEN : %s ; in the trail : %s'
          % (k1, k2, k3))
    print('    lists closed : %d ; desk closures : %d (%s)'
          % (Q['lists_closed'], Q['closed'], [c['item'] for c in Q['closed_items']]))
    print('    ### **THE CLUSTERS STAY FILED AND NOT OPENED** : %s' % k7)
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (k6, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-NORULING/G-HAND/G-OPEN/G-NONEWDOC')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'AN UPPER BOUND TAKEN AT ONE REF' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = 'an-upper-bound-at-one-ref returns 1 row(s)' in irun and Q['key_ok'] is True
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the class is ruled', 'the declarations are moved',
              'the lists are closed', 'the archives are removed'))
    gt = t1 and t2 and t3 and t4 and t5
    print('    trail: mark once and append-only : %s ; blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL/G-ROW/G-KEY')

    # ----------------------------------------------------------------------------------- G-ORDER
    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    relied = (TM, AR, HD, Q)
    o3 = (stampm is not None) and all(
        (x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))) > stampm.group(1)
        for x in relied)
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    # ### **AND `b375`'S DEFECTIVE FACE MUST STILL VERIFY, UNEDITED.**
    R375 = d('b377_registration_2026-09-08.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    # ### **AND THE TWO PRIOR LOCKED FACES MUST STILL VERIFY, UNEDITED.**
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b376_registration_2026-09-08.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b376`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b375`S DEFECTIVE FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b378_hooks.txt'), d('b378_mirror.txt')
    gh2 = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 failing : %s ; mirror clean : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook/mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    # --------------------------------------------------------------------------------- G-NUMBERS
    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('gates read %d' % LG['gates_read'], str(LG['gates_read']) in bank),
        ('face-subject gates %d' % LG['face_subject_gates'],
         str(LG['face_subject_gates']) in bank),
        ('refs %d' % TM['refs'], str(TM['refs']) in bank),
        ('commits %d' % TM['commits'], str(TM['commits']) in bank),
        ('kernels %d' % TM['kernels'], str(TM['kernels']) in bank),
        ('carried %d' % TM['carried'], str(TM['carried']) in bank),
        ('still not found %d' % TM['still_not_found'], str(TM['still_not_found']) in bank),
        ('the face sha', LG['face_sha'] in bank),
        ('archives confirmed %d' % AR['confirmed'], str(AR['confirmed']) in bank),
        ('archive files under archive/ %d' % AR['context_archive_files'],
         str(AR['context_archive_files']) in bank),
        ('hand read named %d' % HD['named'], str(HD['named']) in bank),
        ('hand read located %d' % HD['located'], str(HD['located']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on terminals run', TM['run_file'] in bank),
        ('the relied-on archives run', AR['run_file'] in bank),
        ('the relied-on hand run', HD['run_file'] in bank),
        ('the relied-on lock-gate run', LG['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('terminals', TM),
                    ('archives', AR), ('hand', HD), ('desk', Q)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        want = jf.get('run_clock')
        ok = os.path.exists(p) and (st == want if want else bool(st))
        once = once and ok
        print("    %-12s %-30s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st, want, ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b378_') and x.endswith('.py')))
    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid',
              'curve_fit', 'minimize')
    raw2 = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    CALL = {b: __import__('re').compile(r'\b' + b + r'\s*\(') for b in banned}
    hits2 = [(x, b) for x in mymods for b in banned if CALL[b].search(strip_prose(t(x)))]
    print('    ### raw substring hits (a substring is not a call) : %s' % (raw2 or 'none'))
    for _x, _b in [r for r in raw2 if r not in hits2]:
        print('        ### DISCHARGED in %s : `%s` occurs only inside a longer identifier'
              % (_x, _b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits2 and not imports
    print('    numerical calls : %d %s ; libraries : %s' % (len(hits2), hits2 or '', imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-NOLEAN:')
    lean = [x for x in git(os.path.join('D:', os.sep, 'SIDE-effects'),
                           'diff', '--name-only', 'HEAD').split(chr(10)) if x.strip()]
    gnl = not lean
    print('    .lean or kernel files changed : %s  %s'
          % (lean or 'none', 'PASS' if gnl else '### FAIL ###'))
    if not gnl:
        fails.append('G-NOLEAN')

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
                'the located span': 'the span is located by content and only then indexed.',
                'a parsed table cell': 'the cell index is a COLUMN of a row located by its own shape.',
                'a bounded sample': 'a slice of a list THIS ACT built in memory, not an address.',
                'a line read by its own anchor':
                    'the index is a line number the ANCHOR TOOL returned from the file.'}

    def which(code):
        if "['line'] - 1]" in code or 'lineno' in code:
            return 'a line read by its own anchor'
        if 'cells[' in code:
            return 'a parsed table cell'
        if '[-1:]' in code or '[-1]' in code:
            return 'last-row cells'
        if 'split(' in code or 'find(' in code or 'findall' in code:
            return 'the located span'
        if re.search(r'\[:\d+\]|\[\d+:\]', code):
            return 'a bounded sample'
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
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/hedge_audit.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py',
             'tools/b374_hedge.py', 'tools/b375_population.py', 'tools/git-hooks/pre-push']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b378' not in x and x.strip() != 'tools/banked_index.py']
    gne = (not touched and not others)
    print('    owner instruments modified : %s ### -- this act licenses NONE' % (touched or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b378_satisfiable.json')] + [t(x) for x in mymods] + [t('gate_hash.py')]
    CARRIERS = [
        (t('b378_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(TM['run_file']), "the terminals run carries the documents' own identifiers"),
        (d(AR['run_file']), "the archives run carries the archives' own title lines"),
        (d(HD['run_file']), "the hand read carries the document's own sentences"),
        (d(Q['run_file']), "the desk run carries the items' own sentences"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned, live_bad = 0, 0, 0, []
    carriers = set(os.path.abspath(p) for p, _w in CARRIERS)
    for p in OWNED:
        if not os.path.exists(p) or os.path.abspath(p) in carriers:
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
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

    marker = '# ### THE REFS WIDENED AND THE CONVENTION SWEPT (b378).'
    nxt = '# ### THE UNBLOCKED OBLIGATION (b377).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row):' % ROWNUM)
    for lbl, b2 in (('row %s' % ROWNUM, rws[0] if rws else ''), ('the trail block', tblk),
                    ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(b2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(b2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(b2)))
        if ch or not b2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b378_stem_'), 'blk.txt')
            io.open(tmp2, 'w', encoding='utf-8', newline=chr(10)).write(b2)
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', tmp2],
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
    extra2 = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra2), 'PASS' if not extra2 else '### FAIL ###'))
    if extra2:
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT ELEVEN NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods) + ['tools/gate_hash.py']
    gcap = len(made) <= 11 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b378_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED
               if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rws[0] if rws else ''), ('the trail block', tblk),
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
