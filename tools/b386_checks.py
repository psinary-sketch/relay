# -*- coding: utf-8 -*-
"""b386_checks.py -- THE GATE SUITE FOR THE GUARD MADE SINGLE-SOURCED.

### ### **THE ARM THAT MATTERS MOST IS `G-ORDEROFOPS`.** ### `b385`'s defect was not that it
### deleted the wrong thing -- what it deleted was recoverable. ### **IT WAS THAT THE PROOF CAME
### ### AFTER THE DELETION**, which is a proof of nothing. ### So the arm checks the ORDER in the
### run record: the recoverability line must appear ### **BEFORE** ### the deletion line, by
### position, not merely both be present.
###
### ### **AND `G-HOOK` KEEPS `b385`'S EXACT PREDICATE.** ### The face said the failing gate is
### cleared by the repair and not by the arm, so the arm is byte-for-byte the one that failed --
### ### **`### REPOS FAILING : 0`** -- and it passes now because the topology was fixed.
###
### ### **`G-NOWRITE` AND `G-PROPAGATED` DIFF AGAINST THE PRE-ACT COMMIT, NOT `HEAD`.** ### This
### act commits the guard change BEFORE the exercise can run, so by the time this suite runs the
### change is already in `HEAD` and a `HEAD` diff would read EMPTY. ### **AN ARM THAT MEASURES
### ### DIFFERENTLY ON THE TWO SIDES OF A COMMIT IS NOT MEASURING THE ACT** (`b352`, `b385`).
###
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`); ### **A RUN FILE IS RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`).
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

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
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


BANK = d('b386_the_guard_single_sourced.txt')
REG = d('b386_registration_2026-09-09.txt')
FERRY = d('b386_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b386_ferry_scan.txt'), d('b386_reg_termscan.txt'), d('b386_reg_gate.txt')
CENSUS0, FCEN = d('b386_census_stepzero.txt'), d('b386_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b386_regspec_run.txt'), d('audit_b386_reg_satisfiable.txt')
PINS0, HOOKREC = d('b386_pins_stepzero.txt'), d('b386_hooks.txt')
SEAL = '1b2618fbd40c0e0b3250e9f6766d044258672d1370c652b03754a1b65e1c0f29'
ROWNUM = '235'
TRAIL_MARK = '<!-- b386 the guard made single-sourced; (R15) executed -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b386_components.json'), ('LG', 'b386_lockgate.json'),
                   ('E', 'b386_reads.json'), ('Q', 'b386_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b386_regspec.py', 'tools/b386_reg_gate.py', 'tools/b386_extract.py',
                'tools/b386_components.py', 'tools/b386_desk_bank.py', 'tools/b386_checks.py'}

TOOLNUM = [
    ('the extract, the topology survey and the attestation run', 'tools/b386_extract.py'),
    ('the four components, and the repair inside two of them', 'tools/b386_components.py'),
    ('(R7), the three closing writes and the bank', 'tools/b386_desk_bank.py'),
    ('the registration gate', 'tools/b386_reg_gate.py'),
    ('the clause spec', 'tools/b386_regspec.py'),
    ('the installer, repointed and repaired', 'tools/b304_hooks.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b386 — THE GUARD MADE SINGLE-SOURCED. Number not claimed by'),
    ('the ruling (R15) -- one guard, one source', FERRY,
     'strikeable: ONE GUARD, ONE SOURCE. A guard has exactly one'),
    ('the ruling (R15) -- the three disposals of a second copy', FERRY,
     'or made a pointer to the source, or the repository is'),
    ('the ruling (R15) -- a topology defect, not a repair job', FERRY,
     'of one guard is not a repair job; it is a topology defect, and'),
    ('the order -- component 1, the three options quoted first', FERRY,
     "COMPONENT 1 — THE THREE OPTIONS, QUOTED FIRST: reproduce b385's"),
    ('the order -- component 1, halt if none implements it', FERRY,
     'that one. If none implements it, HALT and report — the author'),
    ('the order -- component 2, the face written wide enough to finish', FERRY,
     'COMPONENT 2 — THE REPAIR ITSELF, with the face written wide'),
    ('the order -- component 2, the gate cleared by the repair not the arm', FERRY,
     'repository afterward, with the failing gate cleared by the'),
    ('the order -- component 3, the installer`s second defect', FERRY,
     "COMPONENT 3 — THE INSTALLER'S SECOND DEFECT: the same tool"),
    ('the order -- component 4(i), the search lesson', FERRY,
     'COMPONENT 4 — TWO FILINGS: (i) the search lesson, minted — a'),
    ('the order -- component 4(ii), the paraphrase corrected on the record', FERRY,
     "(ii) the navigator's paraphrase of the reviewer rule corrected"),
    ('the order -- the closing, closed only if the exercise passes', FERRY,
     "item closed only if Component 2's exercise passes and left open"),
    ('the order -- (F1), deletion of the untracked-path copy', FERRY,
     '(R15) is deletion of the untracked-path copy with the installer'),
    ('the order -- (F2), the backup recoverable from a tracked blob', FERRY,
     "repointed; (F2) the destroyed backup's content is recoverable"),
]

SELF_NEEDLES = [
    ('the bank leads with the ruling and the wider defect', BANK,
     '### ### ### **THE AUTHOR RULED `(R15)`: ONE GUARD, ONE SOURCE -- AND THE DEFECT WAS'),
    ('### the face was written from the survey, not a belief', BANK,
     '### ### ### **A FACE WRITTEN FROM A BELIEF ABOUT THE TOPOLOGY WOULD HAVE FAILED THE'),
    ('### the options discrepancy is reported', BANK,
     '### ### **ONE DISCREPANCY WITH THE ORDER, REPORTED RATHER THAN SMOOTHED:** ### the'),
    ('### option (b) implements the ruling', BANK,
     '###   ### **`(b)` RETIRE THE SOURCE AND REPOINT THE INSTALLER -- IMPLEMENTS.** ###'),
    ('### the order of operations b385 got wrong', BANK,
     '### ### ### **THAT IS THE ORDER `b385` GOT WRONG** -- it removed a file and worked'),
    ('### never by filename and never by size alone', BANK,
     '### ### ### **COMPARED AGAINST THE BLOB AND `LF`-NORMALISED. ### NEVER BY FILENAME,'),
    ('### the third disposal, and the judgement marked as one', BANK,
     '### ### ### **AND THAT IS A JUDGEMENT, MARKED AS ONE:** ### deleting them would'),
    ('### the gate cleared by the repair, not the arm', BANK,
     '### ### **`b385`S ARM PREDICATE IS UNCHANGED. ### THE FAILING GATE IS CLEARED BY THE'),
    ('### the substituted invariant is named', BANK,
     '### ### ### **THE INVARIANT IMPLEMENTED IS STRICTLY STRONGER THAN THE ONE THE ORDER'),
    ('### the repair fired for real on the roster', BANK,
     '### ### ### **AND IT FIRED FOR REAL ON THIS ACT`S OWN INSTALL RUN:** ###'),
    ('### the contamination is itself the finding', BANK,
     '### ### ### **THAT CONTAMINATION IS ITSELF THE FINDING:** ### an act`s own records'),
    ('### necessary and not sufficient', BANK,
     '### ### SUFFICIENT**, exactly as `b378`s positive-control rule turned out to be --'),
    ('### the correction is of a paraphrase, not the rule', BANK,
     '### ### ### **THE CORRECTION IS OF A PARAPHRASE AND NOT OF THE RULE.** ###'),
    ('### a conditional closure whose condition is not measured', BANK,
     '### ### ### **NEW -- `A CONDITIONAL CLOSURE WHOSE CONDITION IS NOT MEASURED IS AN`'),
    ('### the face was not widened mid-act', BANK,
     '### ### **THE FACE WAS NOT WIDENED MID-ACT.** ### Every write this act made is named'),
    ('### (F1) met in substance, refuted in its description', BANK,
     '### ### **`(F1)` MET IN SUBSTANCE AND REFUTED IN ITS DESCRIPTION.** ### The disposal'),
]

MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a standard was edited', BANK, '### A STANDARD WAS EDITED.'),
    ('the bank never says an option was invented', BANK, '### AN OPTION WAS INVENTED.'),
    ('the bank never says a copy was deleted unchecked', BANK,
     '### A COPY WAS DELETED UNCHECKED.'),
    ('the bank never says the arm was widened', BANK, '### THE ARM WAS WIDENED.'),
    ('the bank never says the rule was edited', BANK, '### THE RULE WAS EDITED.'),
    ('the bank never says a techne module was pushed', BANK, '### A TECHNE MODULE WAS PUSHED.'),
    ('the bank never says the face was widened mid-act', BANK,
     '### THE FACE WAS WIDENED MID-ACT.'),
]

PREFER = re.compile(r'\b(recommend\w*|prefer\w*|the best option|should be adopted|we advise|'
                    r'the right choice|obviously|clearly the|the correct option|I suggest|'
                    r'likeliest)\b', re.I)
NEG2 = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,70}$', re.I)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel, ref='HEAD'):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (ref, rel)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def preact(repo):
    """### THE LAST COMMIT THAT IS NOT THIS ACT'S. ### **THE ARMS DIFF AGAINST THIS AND NOT
    ### AGAINST `HEAD`**, so they measure the same thing before and after this act's commits."""
    for ln in git(repo, 'log', '--format=%H %s', '-40').split(chr(10)):
        if not ln.strip():
            continue
        h, _, subj = ln.partition(' ')
        if not subj.startswith('b386'):
            return h
    return 'HEAD'


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
    print('b386 -- GATE SUITE (THE GUARD MADE SINGLE-SOURCED UNDER (R15))')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    C1, C2, C3, C4 = AC['C1'], AC['C2'], AC['C3'], AC['C4']
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
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
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES ### (THE LOCKED FACE`S OWN EIGHT, AS WHOLE LINES):')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bu = gate_text.flat(bank).upper()
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    hook = io.open(HOOKREC, encoding='utf-8', errors='replace').read()

    # ------------------------------------------------------------- BAR 1, THE STAMPED-GATE BAR
    print(chr(10) + '  G-STAMPED / G-EVERYGATE / G-FIXTURE4 (BAR 1):')
    l1 = LG['fixture_ok'] is True and LG['permits'] is True and LG['helper_ok'] is True
    l2 = LG['gates_read'] == LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4
    l3 = all(g['passed'] for g in LG['gates'])
    face_now = hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest()
    l4 = (LG['face_sha'] == face_now == SEAL)
    l5 = all(g['recorded'] == face_now for g in LG['gates'] if g['subject_is_face'])
    fx = LG['fixture']
    l6 = (len(fx) == 4 and fx['all gates clean']['permits'] is True
          and all(v['permits'] is False and len(v['failing']) == 1
                  for k, v in fx.items() if k != 'all gates clean'))
    l7 = LG['act'] == 'b386' and not os.path.exists(t('b386_lockgate.py'))
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7
    print('    gates read %d / passing %d ; face-subject %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l3))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l4, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l5)
    print('    four polarities, each refusing for its own gate : %s ; lock gate inherited : %s'
          % (l6, l7))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4')

    # ------------------------------------------------------------------- BAR 2, THE OPTION BAR
    print(chr(10) + '  G-OPTIONS / G-NOINVENT (BAR 2):')
    o1 = C1['options_quoted'] == 3
    o2 = len(C1['implementing']) == 1 and C1['chosen'] == '(b)'
    o3 = C1['options_invented'] == 0
    o4 = C1['halt'] is False
    # ### **THE THREE ARE IN THE RUN RECORD VERBATIM, EACH WITH ITS FILE AND LINE.**
    o5 = all(s in acrun for s in ('(a) REPAIR THE SOURCE', '(b) RETIRE THE SOURCE',
                                  '(c) NEITHER'))
    o6 = 'b385_closing.txt' in acrun and C1['options_in_bank385'] is False
    # ### **AND THE DISCREPANCY WITH THE ORDER IS REPORTED, NOT SMOOTHED.**
    o7 = 'DOES NOT CARRY THEM' in gate_text.flat(acrun).upper()
    go = o1 and o2 and o3 and o4 and o5 and o6 and o7
    print('    ### **OPTIONS REPRODUCED %d ; IMPLEMENTING %s ; INVENTED %d ; HALT %s**'
          % (C1['options_quoted'], C1['implementing'], C1['options_invented'], C1['halt']))
    print('    all three appear verbatim in the run record : %s' % o5)
    print('    ### **THEY ARE NOT IN b385`S BANK, AND THE ACT SAYS SO** : %s / %s' % (o6, o7))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-OPTIONS/G-NOINVENT')

    # --------------------------------------------------------------- BAR 3, THE SINGLE-SOURCE BAR
    print(chr(10) + '  G-SINGLESOURCE / G-INSTALLER (BAR 3):')
    per_repo, s1 = {}, True
    for name, repo in b303_pins.REPOS:
        tracked = [x.strip() for x in git(repo, 'ls-files').split(chr(10))
                   if x.strip().endswith('pre-push')]
        per_repo[name] = tracked
        if len(tracked) != 1 or tracked[0] != '.githooks/pre-push':
            s1 = False
        print('    %-22s tracked guard copies : %d  %s' % (name, len(tracked), tracked))
    # ### ### **THIS ARM READS THE ASSIGNMENT BY AST, NOT BY `strip_prose`.** ### `strip_prose`
    # ### removes every line inside a string-constant span, and `SOURCE = os.path.join(ROOT,
    # ### '.githooks', 'pre-push')` IS such a line -- so the stripped view showed nothing and the
    # ### arm read `?`. ### **AN ARM THAT CANNOT SEE ITS OWN SUBJECT IS NOT MEASURING IT.**
    # ### `strip_prose` is for `G-NO*` arms, which must not fire on prose; this is a POSITIVE
    # ### assertion about a code line and it reads the code.
    srcmod = ast.parse(io.open(t('b304_hooks.py'), encoding='utf-8').read())
    srcargs = []
    for node in srcmod.body:
        if (isinstance(node, ast.Assign) and node.targets
                and getattr(node.targets[0], 'id', None) == 'SOURCE'):
            srcargs = [x.value for x in ast.walk(node)
                       if isinstance(x, ast.Constant) and isinstance(x.value, str)]
    src_line = ['SOURCE = os.path.join(ROOT, %s)' % ', '.join(repr(x) for x in srcargs)]
    s2 = ('.githooks' in srcargs) and ('git-hooks' not in srcargs)
    s3 = not os.path.exists(t('git-hooks'))or not os.path.exists(
        os.path.join(ROOT, 'tools', 'git-hooks', 'pre-push'))
    s4 = C2['repointed'] is True and C2['deleted'] == 1
    gs = s1 and s2 and s3 and s4
    print('    ### **EXACTLY ONE TRACKED GUARD PER REPOSITORY : %s**' % s1)
    print('    ### **THE INSTALLER`S SOURCE** : %s' % (src_line[0].strip() if src_line else '?'))
    print('    it names .githooks and not tools/git-hooks : %s ; the second copy is gone : %s'
          % (s2, s3))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SINGLESOURCE/G-INSTALLER')

    # ---------------------------------------------------------------- BAR 4, THE PROPAGATION BAR
    print(chr(10) + '  G-PROPAGATED / G-REPAIREDLINE (BAR 4):')
    srcblob = blob_of(ROOT, '.githooks/pre-push')
    REPAIRED = '# Tracked at .githooks/pre-push (moved there b371, 2026-09-08).'
    p1, p2, rows = True, True, []
    for name, repo in b303_pins.REPOS:
        pth = os.path.join(repo, '.githooks', 'pre-push')
        raw = io.open(pth, encoding='utf-8', errors='replace').read() if os.path.exists(pth) else ''
        same = norm(raw) == norm(srcblob or '')
        line = REPAIRED in norm(raw)
        p1 = p1 and same
        p2 = p2 and line
        rows.append((name, same, line))
        print('    %-22s blob-equal (LF) : %-5s   carries the repaired line : %-5s'
              % (name, same, line))
    # ### **AND THE PROPAGATION IS MEASURED AGAINST THE PRE-ACT STATE, SO THE ARM SEES THE MOVE.**
    moved = []
    for name, repo in b303_pins.REPOS:
        if name == 'relay':
            continue
        before = blob_of(repo, '.githooks/pre-push', preact(repo))
        moved.append((name, (before is not None) and REPAIRED not in norm(before)))
    p3 = all(m for _n, m in moved)
    p4 = C2['all_match_blob'] is True and C2['all_carry_line'] is True
    gp = p1 and p2 and p3 and p4
    print('    ### **ALL FOUR EQUAL TO THE SOURCE`S BLOB : %s ; ALL FOUR CARRY THE LINE : %s**'
          % (p1, p2))
    print('    ### **AND THE THREE THAT MOVED DID NOT CARRY IT BEFORE THIS ACT** : %s %s'
          % (p3, moved))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PROPAGATED/G-REPAIREDLINE')

    # -------------------------------------------------------------- BAR 5, THE RECOVERABILITY BAR
    print(chr(10) + '  G-RECOVERABLE / G-ORDEROFOPS (BAR 5):')
    r1 = C2['proof_before_deletion'] is True and bool(C2['recoverable_from'])
    r2 = E['copies_unrecoverable'] == 0
    # ### ### **THE ORDERING ARM. ### BOTH LINES PRESENT IS NOT THE CLAIM; THE PROOF MUST COME
    # ### ### FIRST, BY POSITION.**
    ipro = acrun.find('RECOVERABLE FROM :')
    idel = acrun.find('(b) THE DELETION.')
    r3 = 0 <= ipro < idel
    r4 = 'THE PROOF BEFORE THE DELETION' in gate_text.flat(acrun).upper()
    gr = r1 and r2 and r3 and r4
    print('    the proof was printed and the file matched a blob : %s %s'
          % (r1, C2['recoverable_from']))
    print('    ### **COPIES MATCHING NO TRACKED BLOB, SURVEYED BEFORE THE LOCK : %d**'
          % E['copies_unrecoverable'])
    print('    ### **THE PROOF PRECEDES THE DELETION IN THE RECORD, BY POSITION** : %s (%d < %d)'
          % (r3, ipro, idel))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RECOVERABLE/G-ORDEROFOPS')

    # ------------------------------------------------------------------ BAR 6, THE EXERCISE BAR
    print(chr(10) + '  G-EXERCISE / G-HOOK (BAR 6):')
    # ### ### **b385`S EXACT PREDICATE, UNCHANGED.**
    h1 = '### REPOS FAILING : 0' in hook
    exrows = [ln for ln in hook.split(chr(10))
              if 'REFUSED' in ln and 'ALLOWED' in ln and 'PASS' in ln]
    h2 = len(exrows) == 4
    h3 = 'ALL 4 BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in hook
    h4 = Q['exercise_ok'] is True
    gh = h1 and h2 and h3 and h4
    print('    ### **`### REPOS FAILING : 0` -- b385`S PREDICATE, UNCHANGED : %s**' % h1)
    print('    ### **REPOSITORIES EXERCISED IN BOTH POLARITIES AND PASSING : %d of 4**'
          % len(exrows))
    for ln in exrows:
        print('        %s' % ln.strip()[:104])
    print('    ### **THE ARM WAS NOT WIDENED. ### THE GATE WAS CLEARED BY THE REPAIR.**')
    print('    %s' % ('PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-EXERCISE/G-HOOK')

    # -------------------------------------------------------------------- BAR 7, THE BACKUP BAR
    print(chr(10) + '  G-BACKUP / G-BACKUPFIXTURE (BAR 7):')
    hooksrc = strip_prose(t('b304_hooks.py'))
    b1 = 'while os.path.exists(bak)' in hooksrc
    b2 = "shutil.copy2(dest, dest + '.b304-backup')" not in hooksrc
    b3 = C3['tool_repaired'] is True and C3['polarities_held'] is True and C3['polarities'] == 2
    b4 = C3['disposition'] == 'DONE' and C3['routed'] is False
    # ### **AND IT FIRED FOR REAL** -- an artifact only the repaired branch can produce.
    inst = io.open(d('b386_install_run.txt'), encoding='utf-8',
                   errors='replace').read() if os.path.exists(d('b386_install_run.txt')) else ''
    b5 = '.b304-backup-1' in inst
    gb = b1 and b2 and b3 and b4 and b5
    print('    the never-overwrite loop is in the stripped source : %s ; the old call is gone : %s'
          % (b1, b2))
    print('    ### **FIXTURE POLARITIES : %d, BOTH HELD : %s**'
          % (C3['polarities'], C3['polarities_held']))
    print('    ### **AND IT FIRED ON THE ROSTER, NOT ONLY IN A TEMP DIRECTORY** : %s' % b5)
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BACKUP/G-BACKUPFIXTURE')

    # --------------------------------------------------------------- BAR 8, THE ATTESTATION BAR
    print(chr(10) + '  G-ATTEST / G-ATTESTLIMIT (BAR 8):')
    a1 = C4['term_lists'] == 2 and C4['sweeps'] == 2
    a2 = len(E['b383_terms']) == 6 and len(E['b385_terms']) == 7
    a3 = all(('`%s`' % term) in bank for term in E['b383_terms'] + E['b385_terms'])
    a4 = C4['separates_clean'] is True
    a5 = C4['filing'] == 'MECHANIZED'
    a6 = 'NECESSARY AND NOT SUFFICIENT' in bu
    a7 = C4['limit_stated'] is True
    ga = a1 and a2 and a3 and a4 and a5 and a6 and a7
    for lbl, x3, t3, x5, t5, ctl in C4['attestation_rows']:
        print('    %-38s b383 %d/%d   b385 %d/%d   (control %d)' % (lbl, x3, t3, x5, t5, ctl))
    print('    ### **EVERY TERM OF BOTH LISTS IS PRINTED IN THE BANK : %s**' % a3)
    print('    ### **FILED AS %s, AND ITS LIMIT IS STATED : %s / %s**' % (C4['filing'], a6, a7))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ATTEST/G-ATTESTLIMIT')

    # ------------------------------------------------------ G-TECHNE / G-NOPUSHTECHNE
    print(chr(10) + '  G-TECHNE / G-NOPUSHTECHNE:')
    tpath = os.path.join(TC, C4['techne']['path'].replace('/', os.sep))
    m1 = os.path.exists(tpath)
    m2 = not git(TC, 'status', '--porcelain', '--', C4['techne']['path']).strip()
    sb = git(TC, 'status', '-sb').split(chr(10))[0]
    m3 = 'ahead' in sb
    m4 = C4['techne']['pushed'] is False
    remote_has = git(TC, 'branch', '-r', '--contains', C4['techne']['head']).strip()
    m5 = not remote_has
    gm = m1 and m2 and m3 and m4 and m5
    print('    the module exists and is committed : %s / %s' % (m1, m2))
    print('    ### **LOCAL ONLY** : branch `%s` ; no remote ref contains it : %s' % (sb.strip(), m5))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-TECHNE/G-NOPUSHTECHNE')

    # ---------------------------------------------------- G-PARAPHRASE / G-NOEDITRULE
    print(chr(10) + '  G-PARAPHRASE / G-NOEDITRULE:')
    q1 = C4['paraphrase_corrected'] == 1 and C4['rules_edited'] == 0
    q2 = C4['registry_dirty'] is False
    q3 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'REGISTRY.md').strip()
    q4 = 'OVER-STATED' in bu and 'DIGEST AND `LAST-COMMIT` COLUMNS' in bu.replace('`', '`')
    q5 = 'NEITHER PLACE MAKES THE' in bu and 'WHOLE MANIFEST THE AUTHORITY' in bu
    gq = q1 and q2 and q3 and q4 and q5
    print('    ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB, AND UNCHANGED SINCE BEFORE THIS '
          'ACT** : %s / %s' % (q2, q3))
    print('    the mark and the exact correction are in the bank : %s / %s' % (q4, q5))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-PARAPHRASE/G-NOEDITRULE')

    # ------------------------------------------------- G-NORULING / G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-NORULING / G-OPEN / G-NONEWDOC:')
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    om = [m for m in Q['marks'] if m['item'] in LISTS]
    n1 = len(om) == 4 and all(m['disposition'] == 'STAND' for m in om)
    n2 = 'The four open lists are restated OPEN by name' in tblk
    n3 = Q['lists_closed'] == 0
    # ### **THE CITATION QUESTION IS RESTATED AND NOT MOVED.**
    cq = [m for m in Q['marks'] if 'citation question' in m['item']]
    n4 = len(cq) == 1 and cq[0]['disposition'] == 'STAND' and 'NOT MOVED' in cq[0]['why'].upper()
    # ### ### **THE ARM ASKS ABOUT TRACKING DOCUMENTS, SO IT COUNTS DOCUMENTS.** ### Its first
    # ### form counted EVERY untracked path and fired on `.githooks/pre-push.b304-backup`, which
    # ### the installer wrote and which this act NAMES on the desk and in the bank. ### **A
    # ### BACKUP OF A HOOK IS NOT A TRACKING DOCUMENT UNDER ANY READING**, so the predicate is
    # ### narrowed to what it always meant -- a `.md` outside `.githooks/` -- and ### **WHAT IT
    # ### EXCLUDES IS PRINTED**, so the narrowing is visible rather than silent.
    PREEX = ('BLOB_SENSITIVITY',)
    untracked = [x.strip()[3:].strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
                 if x.strip().startswith('??') and not any(p in x for p in PREEX)]
    newdocs = [x for x in untracked
               if x.endswith('.md') and not x.startswith('.githooks/')]
    notdocs = [x for x in untracked if x not in newdocs]
    n5 = not newdocs
    gn = n1 and n2 and n3 and n4 and n5
    print('    the four lists STAND and are named OPEN in the block : %s / %s' % (n1, n2))
    print('    ### **THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND NOT MOVED** : %s'
          % n4)
    print('    no new tracking document in PLACE-papers : %s %s' % (n5, newdocs[:2] or ''))
    print('    ### **UNTRACKED PATHS THAT ARE NOT TRACKING DOCUMENTS, EXCLUDED AND NAMED** : %s'
          % (notdocs or 'none'))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORULING/G-OPEN/G-NONEWDOC')

    # ------------------------------------ G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE
    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE:')
    ALLOWED = {'relay': {'.githooks/pre-push', 'tools/banked_index.py', 'tools/b304_hooks.py',
                         'tools/git-hooks/pre-push'},
               'SIDE-global-section': {'CORRESPONDENCE.md', '.githooks/pre-push'},
               'PLACE-papers': {'OPEN_TRAILS.md', '.githooks/pre-push'},
               'SIDE-effects': {'.githooks/pre-push'}}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b386' not in x)
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    w2 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'REGISTRY.md').strip()
    # ### **NO `.git/hooks/pre-push` WAS DELETED IN ANY REPOSITORY**, measured on disk.
    legacy = [(n, os.path.exists(os.path.join(r, '.git', 'hooks', 'pre-push')))
              for n, r in b303_pins.REPOS]
    w3 = all(ex for _n, ex in legacy) and C2['legacy_deleted'] == 0
    # ### **AND EVERY ONE OF THEM IS STILL INERT**, which is the disposal that was claimed.
    w4 = all(git(r, 'config', 'core.hooksPath').strip() == '.githooks'
             for _n, r in b303_pins.REPOS)
    arch = [x for x in git(PP, 'diff', '--name-only', preact(PP)).split(chr(10))
            if x.strip().startswith(('archive/', 'outputs/'))]
    w5 = not arch
    gw = w1 and w2 and w3 and w4 and w5
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **REGISTRY.md UNCHANGED SINCE BEFORE THIS ACT** : %s' % w2)
    print('    ### **EVERY `.git/hooks/pre-push` STILL PRESENT : %s** %s' % (w3, legacy))
    print('    ### **AND EVERY ONE STILL INERT (core.hooksPath = .githooks) : %s**' % w4)
    print('    archive/ and outputs/ untouched : %s' % w5)
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-NOWRITE/G-NOREGISTRY/G-NOHOOKSDELETE')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY:')
    tb = blob_of(PP, 'OPEN_TRAILS.md', preact(PP))
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md', preact(SIDE))
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE GUARD IS SINGLE-SOURCED UNDER (R15)' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-guard-made-single-sourced-under-r15 returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the guard has two sources', 'a copy was deleted unchecked',
              'the arm was widened', 'a techne module was pushed'))
    t6 = Q['trail']['says_exercise_passes'] and Q['trail']['says_judgement_marked']
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; pre-act blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    ### **THE BLOCK SAYS THE EXERCISE PASSED AND MARKS THE JUDGEMENT AS ONE** : %s' % t6)
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

    def clk(x):
        return x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))
    AFTER = (('components', AC), ('desk_bank', Q))
    BEFORE = (('extract', E), ('lockgate', LG))
    o3a = (stampm is not None) and all(clk(x) > stampm.group(1) for _l, x in AFTER)
    o3b = (stampm is not None) and all(clk(x) <= stampm.group(1) for _l, x in BEFORE)
    for lbl, x in AFTER:
        print('    %-10s AFTER  the lock : %s vs %s'
              % (lbl, clk(x), stampm.group(1) if stampm else '?'))
    for lbl, x in BEFORE:
        print('    %-10s BEFORE the lock : %s vs %s'
              % (lbl, clk(x), stampm.group(1) if stampm else '?'))
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8',
                                               errors='replace').read()
    o8 = 'SEAL INTACT' in (subprocess.run(
        [sys.executable, t('reg_seal.py'), '--verify', d('b385_registration_2026-09-09.txt')],
        capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or '')
    go2 = o1 and stampm and o3a and o3b and o4 and o5 and o6 and o7 and o8
    print('    this act`s lock recomputes : %s' % o1)
    print('    ### **POST-LOCK RUNS AFTER IT : %s ; PRE-LOCK GATES BEFORE IT : %s**' % (o3a, o3b))
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b385`S FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-MIRROR ### AFTER THE PUSH:')
    mirrorp = d('b386_mirror.txt')
    if os.path.exists(mirrorp):
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        print('    mirror clean on all three clauses : %s' % m_ok)
        if not m_ok:
            fails.append('G-MIRROR')
    else:
        print('    ### the mirror record is NOT YET WRITTEN (it is written at the closing).')
        fails.append('G-MIRROR (owed, not yet recorded)')

    # --------------------------------------------------------------------------------- G-NUMBERS
    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('gates read %d' % LG['gates_read'], str(LG['gates_read']) in bank),
        ('face-subject gates %d' % LG['face_subject_gates'], str(LG['face_subject_gates']) in bank),
        ('copies on disk %d' % E['copies_total'], str(E['copies_total']) in bank),
        ('tracked %d / untracked %d' % (E['copies_tracked'], E['copies_untracked']),
         str(E['copies_tracked']) in bank and str(E['copies_untracked']) in bank),
        ('options %d' % C1['options_quoted'], str(C1['options_quoted']) in bank),
        ('deleted %d' % C2['deleted'], str(C2['deleted']) in bank),
        ('the lost backup %d bytes' % C3['lost_bytes'], str(C3['lost_bytes']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the component run', AC['run_file'] in bank),
        ('the extract run', E['run_file'] in bank),
        ('the techne head', C4['techne']['head'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('components', AC), ('desk_bank', Q)):
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
                          if x.startswith('b386_') and x.endswith('.py')))
    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid',
              'curve_fit', 'minimize')
    raw2 = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    CALL = {b: re.compile(r'\b' + b + r'\s*\(') for b in banned}
    hits2 = [(x, b) for x in mymods for b in banned if CALL[b].search(strip_prose(t(x)))]
    print('    ### raw substring hits (a substring is not a call) : %s' % (raw2 or 'none'))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits2 and not imports
    print('    numerical calls : %d ; libraries : %s  %s'
          % (len(hits2), imports or 'none', 'PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-NOLEAN:')
    lean = [x for x in git(os.path.join('D:', os.sep, 'SIDE-effects'),
                           'diff', '--name-only', preact(os.path.join('D:', os.sep,
                                                                      'SIDE-effects'))
                           ).split(chr(10)) if x.strip() and x.strip().endswith('.lean')]
    gnl = not lean
    print('    .lean files changed : %s  %s' % (lean or 'none', 'PASS' if gnl else '### FAIL ###'))
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
    DECLARED = {'last-row cells': '`[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
                'the located span': 'the span is located by content and only then indexed.',
                'a parsed table cell': 'a COLUMN of a row located by its own shape.',
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

    print(chr(10) + '  G-NOEDIT:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/hedge_audit.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b374_hedge.py',
             'tools/b375_population.py', 'tools/gate_hash.py', 'tools/b378_lockgate.py',
             'tools/role_structure.py', 'tools/co_location.py']
    touched = [p for p in owner
               if git(ROOT, 'diff', '--name-only', preact(ROOT), '--', p).strip()]
    # ### **`tools/b304_hooks.py` IS AN OWNER INSTRUMENT AND IT IS EDITED -- DECLARED ON THE FACE
    # ### BEFORE THE ACT, IN SECTION `(F)`.** ### It is therefore NOT on the list above; a
    # ### declared write is not an undeclared one, and the declaration is what makes the
    # ### difference. ### **THE FACE WAS NOT WIDENED MID-ACT TO ACCOMMODATE IT.**
    DECLARED_W = ('tools/banked_index.py', 'tools/b304_hooks.py', 'tools/git-hooks/pre-push',
                  '.githooks/pre-push')
    others = [x for x in git(ROOT, 'diff', '--name-only', preact(ROOT)).split(chr(10))
              if x.strip() and 'b386' not in x and x.strip() not in DECLARED_W]
    e1 = not touched and not others
    e2 = 'tools/b304_hooks.py' in reg and 'AND NOTHING ELSE IN ANY REPOSITORY' in reg
    gne = e1 and e2
    print('    owner instruments modified beyond the declared one : %s' % (touched or 'none'))
    print('    other relay files beyond the four declared : %s' % (others or 'none'))
    print('    ### **b304_hooks.py IS NAMED ON THE LOCKED FACE** : %s' % e2)
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE, HOOKREC,
             d('b386_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b386_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the sources' own lines"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(AC['run_file']), "the component run carries the options' own text"),
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
    fired = sum(1 for _e, text in
                [('S-1', 'a title must name its objects and conditions, not claim an achieved '
                         'property'),
                 ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                 ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [],
                                     stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or live_bad or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE GUARD MADE SINGLE-SOURCED (b386).'
    nxt = '# ### THE RULE LOCATED, THE SIX ON THE TRAILS (b385).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b386_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT SIX NEW TOOL FILES:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 6 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b386_hedge_')
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
