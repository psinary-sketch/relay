# -*- coding: utf-8 -*-
"""b388_checks.py -- THE GATE SUITE FOR THE MAP REFRESHED AND THE UNREADABLE ROWS NAMED.

### ### **THE ARM THAT MATTERS MOST IS `G-PRESERVED`.** ### This act writes into a corpus
### document, and the one thing it must not do is lose what was there. ### The arm re-reads
### ### **EVERY ROW OF THE PRIOR CLUSTER TABLE OUT OF THE FILE AFTER THE WRITE** ### and requires
### the file to have grown. ### **A REFRESH THAT DELETES IS NOT A REFRESH.**
###
### ### **`G-NOJUDGEMENT` GUARDS THE SEATING.** ### Every member of the two emergent clusters must
### be carried by a quoted registry move; the member count must equal the count of distinct
### documents moved. ### **A CLUSTER ASSEMBLED FROM A SEAT'S SENSE OF WHAT BELONGS IS A CLUSTER
### ### THE AUTHOR NEVER RULED.**
###
### ### **AND `G-EVIDENCE` GUARDS THE ASSIGNMENTS**, which are the shape of work a seat does well
### and cannot check: a plausible assignment reads like a correct one. ### Every assignment carries
### printed evidence, and one without it is counted `UNASSIGNED`.
###
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`) -- ### **BUT A POSITIVE ARM READS THE CODE ITSELF** (`b386`). ### **A RUN
### ### FILE IS RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`).
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


BANK = d('b388_the_map_refreshed.txt')
REG = d('b388_registration_2026-09-09.txt')
FERRY = d('b388_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b388_ferry_scan.txt'), d('b388_reg_termscan.txt'), d('b388_reg_gate.txt')
CENSUS0, FCEN = d('b388_census_stepzero.txt'), d('b388_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b388_regspec_run.txt'), d('audit_b388_reg_satisfiable.txt')
PINS0 = d('b388_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REFRESH_MARK = '<!-- b388 CLUSTER TABLE REFRESH under RULING (R17), 2026-09-09 -->'
SEAL = 'fb8050740c213d96f846dfb6a4d9ecacfe371ef656d40b0c3ecd608ae4235e56'
ROWNUM = '237'
TRAIL_MARK = '<!-- b388 the map refreshed; (R17) executed; the unreadable rows named -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b388_components.json'), ('LG', 'b388_lockgate.json'),
                   ('E', 'b388_reads.json'), ('Q', 'b388_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b388_regspec.py', 'tools/b388_reg_gate.py', 'tools/b388_extract.py',
                'tools/b388_components.py', 'tools/b388_desk_bank.py', 'tools/b388_checks.py'}

TOOLNUM = [
    ('the extract, the map survey and the live federation read', 'tools/b388_extract.py'),
    ('the six components, and the assignments inside one', 'tools/b388_components.py'),
    ('component 5, (R7), the three closing writes and the bank', 'tools/b388_desk_bank.py'),
    ('the registration gate', 'tools/b388_reg_gate.py'),
    ('the clause spec', 'tools/b388_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b388 — THE MAP REFRESHED, AND THE UNREADABLE ROWS NAMED.'),
    ('the ruling (R17) -- the map is refreshed in full', FERRY,
     'strikeable: THE FEDERATION MAP IS REFRESHED IN FULL. The two'),
    ('the ruling (R17) -- the two clusters named and seated', FERRY,
     'theory-space cluster and the cross-domain cluster — are NAMED'),
    ('the ruling (R17) -- nothing outside the map is edited', FERRY,
     'live because pins move. Nothing outside the map is edited by'),
    ('the order -- component 1, the map quoted before anything moves', FERRY,
     'COMPONENT 1 — THE MAP AS IT STANDS, quoted before anything'),
    ('the order -- component 2, seated from the moves that created them', FERRY,
     'COMPONENT 2 — THE TWO EMERGENT CLUSTERS, seated from the moves'),
    ('the order -- component 2, a third destination is not seated', FERRY,
     'of these two, report it as a third destination and do not seat'),
    ('the order -- component 3, assigned or marked', FERRY,
     "COMPONENT 3 — THE ERA'S OUTPUT ASSIGNED OR MARKED: every"),
    ('the order -- component 3, not by filename or directory', FERRY,
     'filename, by directory, or by resemblance of title.'),
    ('the order -- component 4, the map re-evaluated', FERRY,
     'COMPONENT 4 — THE MAP RE-EVALUATED, which is more than an'),
    ('the order -- component 4, a changed shape is reported not acted on', FERRY,
     'has changed shape, that is REPORTED as a finding and NOT acted'),
    ('the order -- component 5, the refresh written', FERRY,
     'COMPONENT 5 — THE REFRESH WRITTEN: the map updated per (R17),'),
    ('the order -- component 5, nothing deleted from the map', FERRY,
     'map; the superseded table is quoted, not removed.'),
    ('the order -- component 6, the unreadable rows named not repaired', FERRY,
     'COMPONENT 6 — THE UNREADABLE ROWS, NAMED AND NOT REPAIRED: the'),
    ('the order -- component 6, no row edited', FERRY,
     'No row edited, no grade moved, no status assigned.'),
    ('the order -- the closing, the mirror rebuilt after the commit', FERRY,
     'and the mirror rebuilt after the commit so the export the'),
    ('the order -- (F1), more than half assign', FERRY,
     "more than half the era's keystone-class documents assign to an"),
    ('the order -- (F3), a kernel that does not resolve', FERRY,
     "4; (F3) at least one kernel in the map's federation columns"),
]

SELF_NEEDLES = [
    ('the bank leads with the ruling', BANK,
     '### ### ### **THE AUTHOR RULED `(R17)`: THE FEDERATION MAP IS REFRESHED IN FULL.**'),
    ('### an age against a date that has not happened', BANK,
     '### ### IS NOT AN AGE.** ### A first pass took the maximum date and reported `344`'),
    ('### a mention is not a move', BANK,
     '### ### ### **A MENTION IS NOT A MOVE**, and the two figures are reported'),
    ('### no member added on this seat`s judgement', BANK,
     '### ### **`0` MEMBERS WERE ADDED ON THIS SEAT`S JUDGEMENT OF SUBJECT.** ### Each is'),
    ('### neither cluster carries an anchor', BANK,
     '### ### **AND NEITHER CLUSTER CARRIES AN ANCHOR:** ### `(R17)` seats them and names'),
    ('### the population was fixed on the locked face', BANK,
     '### ### **THE POPULATION WAS FIXED ON THE LOCKED FACE: `11` KEYSTONE-CLASS'),
    ('### unassigned is not a defect', BANK,
     '### ### ### **UNASSIGNED IS A PERMITTED AND HONEST OUTCOME, NOT A DEFECT.** ### A'),
    ('### every change of shape reported, none acted on', BANK,
     '### ### ### **EVERY CHANGE OF SHAPE IS REPORTED AS A FINDING AND NONE IS ACTED ON.**'),
    ('### the kernel that does not resolve, and the limit of the read', BANK,
     '###   ### ### **THIS ACT CANNOT TELL WHETHER IT IS ABSENT OR PRIVATE.** ### An'),
    ('### nothing deleted from the map', BANK,
     '### ### ### **NOTHING WAS DELETED FROM THE MAP. ### THE SUPERSEDED TABLE IS QUOTED,'),
    ('### the unreadable rows named, not read', BANK,
     '### ### **NAMING WHAT DEFEATS A READER IS NOT SAYING WHAT THE ROW SHOULD HAVE'),
    ('### (F3) refuted and declared in advance', BANK,
     '### ### **`(F3)` REFUTED**, and it was ### **ALREADY REFUTED BY THE PRE-LOCK'),
    ('### a seat that reshapes while reporting has ruled', BANK,
     '### ### ### **NEW -- `A SEAT THAT RESHAPES WHILE REPORTING HAS RULED`.**'),
    ('### an unauthenticated read cannot tell absent from private', BANK,
     '### ### ### **NEW -- `AN UNAUTHENTICATED READ CANNOT TELL ABSENT FROM PRIVATE`.** ###'),
]

MUST_FAIL = [
    ('the bank never says a cluster was reshaped', BANK, '### A CLUSTER WAS RESHAPED.'),
    ('the bank never says a row was edited', BANK, '### A ROW WAS EDITED.'),
    ('the bank never says a document was reclassified', BANK,
     '### A DOCUMENT WAS RECLASSIFIED.'),
    ('the bank never says a prior row was deleted', BANK,
     '### A ROW OF THE PRIOR TABLE WAS DELETED.'),
    ('the bank never says assigned by filename', BANK, '### ASSIGNED BY FILENAME.'),
    ('the bank never says a member was added by judgement', BANK,
     '### A MEMBER WAS ADDED BY JUDGEMENT.'),
    ('the bank never says a kernel was recalled', BANK, '### A KERNEL WAS RECALLED.'),
    ('the bank never says unassigned is a defect', BANK, '### UNASSIGNED IS A DEFECT.'),
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
        if not subj.startswith('b388'):
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
    print('b388 -- GATE SUITE (THE GUARD MADE SINGLE-SOURCED UNDER (R15))')
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
    l7 = LG['act'] == 'b388' and not os.path.exists(t('b388_lockgate.py'))
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
    # ------------------------------------------------------------------- BAR 2, THE SET BAR
    C1, C2, C3, C4, C6 = AC['C1'], AC['C2'], AC['C3'], AC['C4'], AC['C6']
    C5 = Q['C5']
    maptxt = io.open(MAP, encoding='utf-8', errors='replace').read()

    # ------------------------------------------------------------- BAR 2, THE QUOTATION BAR
    print(chr(10) + '  G-QUOTED / G-REREAD (BAR 2):')
    q1 = len(AC['reread_failures']) == 0
    prior = C1['prior_table']
    q2 = len(prior) == C1['table_lines'] and len(prior) >= 8
    # ### **EVERY PRIOR ROW RE-READS OUT OF THE MAP AFTER THE WRITE, AS A QUOTED LINE.**
    q3 = all(('> ' + ln) in maptxt for ln in prior)
    q4 = E['without_anchor'] == 0
    gq = q1 and q2 and q3 and q4
    print('    quotations that failed to re-read : %d ; extract reads without an anchor : %d'
          % (len(AC['reread_failures']), E['without_anchor']))
    print('    ### **THE PRIOR TABLE : %d LINES, EVERY ONE PRESENT IN THE MAP AS A QUOTED LINE : '
          '%s**' % (len(prior), q3))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED/G-REREAD')

    # ----------------------------------------------------------------- BAR 3, THE MOVE BAR
    print(chr(10) + '  G-MOVES / G-NOJUDGEMENT / G-THIRDDEST (BAR 3):')
    seated = C2['seated']
    members = sorted(set(m for v in seated.values() for m in v['members']))
    moved = sorted(set(m['path'] for m in E['moves'] if m['path']))
    m1 = members == moved
    m2 = len(members) == C2['documents']
    m3 = C2['third'] == 0 and not E['third_destinations']
    m4 = sorted(seated) == ['cross-domain', 'theory-space']
    # ### **EVERY MEMBER IS CARRIED BY A QUOTED MOVE AT ITS OWN REGISTRY LINE.**
    m5 = all(any(mv['path'] == mem for mv in E['moves']) for mem in members)
    gm = m1 and m2 and m3 and m4 and m5
    print('    ### **MEMBERS SEATED : %d ; DISTINCT DOCUMENTS MOVED : %d ; EQUAL : %s**'
          % (len(members), C2['documents'], m1 and m2))
    for mem in members:
        ln = [mv['line'] for mv in E['moves'] if mv['path'] == mem]
        print('        %-58s carried by move(s) at line %s' % (mem[:58], ln))
    print('    ### **THIRD DESTINATIONS : %d ; CLUSTERS SEATED : %s**'
          % (C2['third'], sorted(seated)))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MOVES/G-NOJUDGEMENT/G-THIRDDEST')

    # -------------------------------------------------------------- BAR 4, THE EVIDENCE BAR
    print(chr(10) + '  G-EVIDENCE / G-NOFILENAME / G-UNASSIGNED (BAR 4):')
    rows = C3['rows']
    e1 = len(rows) == C3['population'] == len(E['tierk_unnamed'])
    assigned = [r for r in rows if not r['verdict'].startswith('UNASSIGNED')]
    e2 = all(r['evidence'] for r in assigned)
    e3 = C3['assigned'] == len(assigned)
    e4 = C3['no_evidence'] + C3['no_fit'] == C3['unassigned']
    # ### **AND NO ASSIGNMENT RESTS ON THE DOCUMENT`S OWN NAME.** ### An assignment whose only
    # ### evidence is the document`s basename or its directory would be a filename assignment.
    e5 = True
    for r in assigned:
        stem = r['doc'].split('/')[-1][:-3]
        folder = r['doc'].split('/')[0]
        if all((stem in str(x)) or (folder in str(x)) for x in r['evidence']):
            e5 = False
            print('        ### ### **FILENAME-SHAPED EVIDENCE : %s %s**' % (r['doc'],
                                                                            r['evidence']))
    ge = e1 and e2 and e3 and e4 and e5
    print('    ### **POPULATION %d ; ASSIGNED %d ; UNASSIGNED %d (NO EVIDENCE %d, NO FIT %d)**'
          % (C3['population'], C3['assigned'], C3['unassigned'], C3['no_evidence'],
             C3['no_fit']))
    print('    ### **EVERY ASSIGNMENT CARRIES PRINTED EVIDENCE : %s ; NONE IS FILENAME-SHAPED : '
          '%s**' % (e2, e5))
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-EVIDENCE/G-NOFILENAME/G-UNASSIGNED')

    # ---------------------------------------------------------- BAR 5, THE PRESERVATION BAR
    print(chr(10) + '  G-PRESERVED / G-APPENDONLY / G-MAPONLY (BAR 5):')
    p1 = C5['prior_rows_preserved'] == C5['prior_rows'] == len(prior)
    # ### ### **THE GROWTH IS MEASURED AGAINST THE PRE-ACT BLOB, NOT WITHIN THE RUN.** ###
    # ### On an idempotent re-run the writer`s own `before` and `after` are the SAME file,
    # ### so a within-run comparison reads `False` on a correct act. ### **AN ARM MUST
    # ### ### MEASURE THE SAME THING ON EVERY RUN** (`b352`, `b385`).
    preblob = blob_of(PP, 'SPIRAL_MAP.md', preact(PP)) or ''
    p2 = len(maptxt.encode('utf-8')) > len(preblob.encode('utf-8')) > 0
    p3 = REFRESH_MARK in maptxt and maptxt.count(REFRESH_MARK) == 1
    # ### **AND THE MAP IS THE ONLY CORPUS DOCUMENT TOUCHED BESIDES THE TRAILS LEDGER.**
    ppch = sorted(x.strip() for x in
                  git(PP, 'diff', '--name-only', preact(PP)).split(chr(10)) if x.strip())
    p4 = set(ppch) <= {'SPIRAL_MAP.md', 'OPEN_TRAILS.md'}
    # ### **AND NO SECTION OF THE MAP OUTSIDE 4A`S TABLE MOVED** -- measured as a diff whose only
    # ### added hunks fall inside the refresh block.
    dmap = git(PP, 'diff', '-U0', preact(PP), '--', 'SPIRAL_MAP.md')
    dels = [x for x in dmap.split(chr(10)) if x.startswith('-') and not x.startswith('---')]
    p5 = all(x.lstrip('-').strip() == '' or x.lstrip('-') in chr(10).join(prior) for x in dels)
    gp = p1 and p2 and p3 and p4 and p5
    print('    ### **PRIOR ROWS PRESERVED : %s OF %s** ; the map grew against its PRE-ACT '
          'blob : %s (%d -> %d bytes)'
          % (C5['prior_rows_preserved'], C5['prior_rows'], p2,
             len(preblob.encode('utf-8')), len(maptxt.encode('utf-8'))))
    print('    the refresh mark appears exactly once : %s' % p3)
    print('    ### **PLACE-papers PATHS TOUCHED : %s** ; only the map and the ledger : %s'
          % (ppch, p4))
    print('    ### **EVERY DELETED LINE BELONGS TO THE PRIOR TABLE (it moved into the '
          'blockquote) : %s** (%d deletions)' % (p5, len(dels)))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRESERVED/G-APPENDONLY/G-MAPONLY')

    # ------------------------------------------------------------ BAR 6, THE LIVE-READ BAR
    print(chr(10) + '  G-LIVEREAD (BAR 6):')
    l1 = len(E['kernels']) == 25 and E['kernels_unresolved'] == 0
    l2 = len(E['pins']) > 0 and E['pins_bad'] == 0
    l3 = all(p.get('used') for p in E['pins'])
    # ### **THE ONE KERNEL THAT DOES NOT RESOLVE IS NAMED, AND IT IS NOT IN THE FEDERATION
    # ### COLUMNS** -- so (F3) is refuted and the finding is reported beside it, not as it.
    bad = [k['kernel'] for c in C4['clusters'] for k in c['kernels'] if not k['resolves']]
    l4 = bad == ['SIDE-interface-split'] and 'SIDE-interface-split' not in [
        x['kernel'] for x in E['kernels']]
    l5 = 'CANNOT TELL WHETHER IT IS ABSENT OR PRIVATE' in bu
    gl2 = l1 and l2 and l3 and l4 and l5
    print('    ### **FEDERATION-COLUMN KERNELS : %d, %d NOT RESOLVING**'
          % (len(E['kernels']), E['kernels_unresolved']))
    print('    ### **PIN TRIPLES : %d, %d FAILING AT THE REF THE MAP NAMES ; EVERY ONE RECORDS '
          'THE REF IT USED : %s**' % (len(E['pins']), E['pins_bad'], l3))
    print('    ### **KERNELS NOT RESOLVING ANYWHERE IN THE SEATED CLUSTERS : %s**' % bad)
    print('    ### **AND IT IS NOT IN THE FEDERATION COLUMNS, SO (F3) IS REFUTED : %s**' % l4)
    print('    ### **THE LIMIT OF THE READ IS STATED : %s**' % l5)
    print('    %s' % ('PASS' if gl2 else '### FAIL ###'))
    if not gl2:
        fails.append('G-LIVEREAD')

    # --------------------------------------------------------------- BAR 7, THE CAUSE BAR
    print(chr(10) + '  G-CAUSES (BAR 7):')
    k1 = C6['total'] == 23 == len(C6['rows'])
    k2 = C6['sums'] is True and sum(C6['groups'].values()) == C6['total']
    k3 = C6['causes'] > 1
    k4 = all(r.get('cause') and r.get('doc') and r.get('line') for r in C6['rows'])
    k5 = 'OTHER' not in C6['groups']
    gk = k1 and k2 and k3 and k4 and k5
    for kk, vv in sorted(C6['groups'].items(), key=lambda kv: -kv[1]):
        print('    %-62s %d' % (kk[:62], vv))
    print('    ### **ROWS %d ; CAUSES %d ; THE GROUPS SUM : %s ; NONE BINNED AS `OTHER` : %s**'
          % (C6['total'], C6['causes'], k2, k5))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-CAUSES')

    # ---------------------------------------------------------- BAR 8, THE NO-RESHAPE BAR
    print(chr(10) + '  G-NORESHAPE / G-NOROWEDIT / G-NOREGISTRY (BAR 8):')
    n1 = C4['reshaped'] == 0
    n2 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'REGISTRY.md').strip()
    n3 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'README.md').strip()
    n4 = not git(PP, 'diff', '--name-only', preact(PP), '--',
                 'phase1.5/method/THE_LOAD_BEARING_MAP.md').strip()
    n5 = not git(PP, 'diff', '--name-only', preact(PP), '--',
                 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md').strip()
    # ### **AND NOT ONE OF THE 17 TIER-K DECLARERS MOVED.**
    touched = [x for x in E['tierk']
               if git(PP, 'diff', '--name-only', preact(PP), '--', x).strip()]
    n6 = not touched
    n7 = 'EVERY CHANGE OF SHAPE IS REPORTED AS A FINDING AND NONE IS ACTED ON' in bu
    gn2 = n1 and n2 and n3 and n4 and n5 and n6 and n7
    print('    ### **CLUSTERS RESHAPED BY THIS ACT : %d ; SHAPE FINDINGS REPORTED : %d**'
          % (C4['reshaped'], C4['changed']))
    print('    REGISTRY.md / README.md / the union / the taxonomy unchanged : %s / %s / %s / %s'
          % (n2, n3, n4, n5))
    print('    ### **KEYSTONE-CLASS DOCUMENTS CHANGED : %d** %s' % (len(touched), touched or ''))
    print('    %s' % ('PASS' if gn2 else '### FAIL ###'))
    if not gn2:
        fails.append('G-NORESHAPE/G-NOROWEDIT/G-NOREGISTRY')

    # ------------------------------------------------------------------ G-NOKERNEL
    print(chr(10) + '  G-NOKERNEL:')
    mymods0 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b388_') and x.endswith('.py')))
    kernelish = ('print axioms', 'lake ', 'LEAN_PATH', '.olean')
    khits = [(x, k) for x in mymods0 for k in kernelish if k in strip_prose(t(x))]
    k1 = not khits
    k2 = 'IT DOES NOT SAY THE KERNEL COMPILES' in bu or 'ls-remote SAYS A REF EXISTS' in bu
    gkn = k1 and k2
    print('    kernel-invoking strings in this act`s stripped code : %s' % (khits or 'none'))
    print('    ### **THE LIMIT OF `ls-remote` IS STATED : %s**' % k2)
    print('    %s' % ('PASS' if gkn else '### FAIL ###'))
    if not gkn:
        fails.append('G-NOKERNEL')

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
    ALLOWED = {'relay': {'tools/banked_index.py'},
               'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md', 'SPIRAL_MAP.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b388' not in x)
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    w2 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'REGISTRY.md').strip()
    # ### **NO `.git/hooks/pre-push` WAS DELETED IN ANY REPOSITORY**, measured on disk.
    legacy = [(n, os.path.exists(os.path.join(r, '.git', 'hooks', 'pre-push')))
              for n, r in b303_pins.REPOS]
    w3 = all(ex for _n, ex in legacy)
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
    t3 = len(rws) == 1 and anc and 'THE FEDERATION MAP IS REFRESHED UNDER (R17)' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-map-refreshed-under-r17 returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('a cluster was reshaped', 'a registry row was edited',
              'unassigned is a defect', 'a member was added by judgement'))
    t6 = (Q['trail']['says_r17'] and Q['trail']['says_not_owed']
          and Q['trail']['says_not_acted'] and Q['trail']['says_absent_or_private'])
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; pre-act blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    ### **THE BLOCK NAMES (R17), SAYS NOT OWED, SAYS THE SHAPE FINDING IS NOT ACTED '
          'ON, AND STATES THE LIMIT OF THE KERNEL READ** : %s' % t6)
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
    mirrorp = d('b388_mirror.txt')
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
        ('the clusters in the table %d' % C1['clusters'], str(C1['clusters']) in bank),
        ('the age against today %d' % C1['age_today'], str(C1['age_today']) in bank),
        ('the age against the registry %d' % C1['age_registry'],
         str(C1['age_registry']) in bank),
        ('the move rows %d' % C2['moves_rows'], str(C2['moves_rows']) in bank),
        ('the moved documents %d' % C2['documents'], str(C2['documents']) in bank),
        ('assigned %d of %d' % (C3['assigned'], C3['population']),
         str(C3['assigned']) in bank and str(C3['population']) in bank),
        ('unassigned %d' % C3['unassigned'], str(C3['unassigned']) in bank),
        ('clusters changed %d' % C4['changed'], str(C4['changed']) in bank),
        ('unreadable causes %d' % C6['causes'], str(C6['causes']) in bank),
        ('the map bytes %d -> %d' % (C5['before'], C5['after']),
         str(C5['before']) in bank and str(C5['after']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the component run', AC['run_file'] in bank),
        ('the extract run', E['run_file'] in bank),
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
                          if x.startswith('b388_') and x.endswith('.py')))
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
    DECLARED_W = ('tools/banked_index.py',)
    others = [x for x in git(ROOT, 'diff', '--name-only', preact(ROOT)).split(chr(10))
              if x.strip() and 'b388' not in x and x.strip() not in DECLARED_W]
    e1 = not touched and not others
    e2 = ('AND NOTHING ELSE IN ANY REPOSITORY' in reg
          and 'one key in `tools/banked_index.py`' in reg)
    gne = e1 and e2
    print('    owner instruments modified beyond the declared one : %s' % (touched or 'none'))
    print('    other relay files beyond the four declared : %s' % (others or 'none'))
    print('    ### **THE ONLY RELAY WRITE OUTSIDE THIS ACT`S OWN FILES IS THE INDEX KEY, AND '
          'THE FACE SAYS SO** : %s' % e2)
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b388_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b388_checks.py'), 'its own fixtures'),
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

    marker = '# ### THE MAP REFRESHED UNDER (R17) (b388).'
    nxt = '# ### WHAT THE KEYSTONES` TABLES ACTUALLY CARRY (b387).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b388_stem_'), 'blk.txt')
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
    tmpdir = tempfile.mkdtemp(prefix='b388_hedge_')
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
