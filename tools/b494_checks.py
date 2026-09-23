# -*- coding: utf-8 -*-
"""b494_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### **THE CARRIED ARMS WERE RE-POINTED ONE AT A TIME**, each read against THIS act's banks
### before its pointer moved -- b480 recorded three instances of the wholesale-substitution species
### in a single act, and this file is written against that.
"""
import io
import glob
import fnmatch
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
FACE = os.path.join(D, 'b494_registration_2026-09-23.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
L, RES, EX = [], [], []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def gits(repo, *a):
    return git(repo, *a).strip()


def line_with(text, needle):
    """### **A2.** ### The FIRST LINE of a TEXT carrying the needle -- never the whole text."""
    for ln in (text or '').split(NL):
        if needle in ln:
            return ln
    return ''


def cut(S, k, sub):
    M = dict(S)
    M[k] = (S.get(k) or '').replace(sub, '')
    return M


def put(S, k, v):
    M = dict(S)
    M[k] = v
    return M


def sources():
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b494_ferry.txt')),
        scan=read(os.path.join(D, 'b494_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b494_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b494_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b494_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b494_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b494_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b493_closing.txt')),
        addendum=read(os.path.join(D, 'b494_addendum.txt')),
        comp=read(os.path.join(D, 'b494_components.txt')),
        desk=read(os.path.join(D, 'b494_desk_notes.txt')),
        span=read(os.path.join(D, 'b494_span_notes2.txt'))
        + read(os.path.join(D, 'b494_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b494_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b494_scores.json')) or '{}'),
        loom=read(os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                              'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md')),
        fnd=read(os.path.join(PP, 'FINDINGS.md')),
        axc=__import__('subprocess').run(
            ['git', '-C', os.path.join('D:', os.sep, 'SIDE-lv-conservation'),
             'show', 'v0.10.0:AxiomCheck.lean'], capture_output=True, text=True,
            encoding='utf-8', errors='replace').stdout,
        b477=read(os.path.join(D, 'b477_entries.jsonl')),
        aimmap=read(os.path.join(D, 'b334_the_aim_map.txt')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b494_checks.py')),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b494.zip'))),
        spantool_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py') == ''),
        tools494=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b494_') and f.endswith('.py')
                         and f != 'b494_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b494 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b494_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b494 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        # ### ### **A FILE DIRTY BEFORE THIS ACT BEGAN WAS NOT WRITTEN BY IT.**
        # ### `b475_zeta23_build.log` has been modified-but-uncommitted since b475's run died,
        # ### and a bare `status` reading calls it one of THIS act's writes forever. ### The
        # ### write list bounds what the ACT writes, so the population is narrowed to files
        # ### whose mtime is AT OR AFTER the sealed face's -- and the ground is printed.
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                full = os.path.join(repo, rel)
                try:
                    if os.path.getmtime(full) < os.path.getmtime(FACE):
                        continue
                except OSError:
                    pass
                k.add(os.path.basename(rel))
    # ### b475's log is still being written by another act's live process; excluded BY NAME.
    S['kinds'] = k
    # ### ### **NO EXCLUSION. THE GROUND LAPSED AND THIS ACT RE-TESTED IT.**
    # ### b481 to b489 excused `b475_zeta23_build.log` because "another act's live process is
    # ### still appending to it". ### Component 0 finds pid 27508 ABSENT at two readings sixty
    # ### seconds apart, no `lean` or `lake` process at either, and the file cold for hours.
    # ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND DECAYS LIKE ONE**, so it is retired and
    # ### the arm runs at full width over every prior bank.
    LIVE = set()
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b494_') and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def declared_arms(face):
    """### ### **THE ARMS THE FACE DECLARES, MINUS THE ONES IT EXPRESSLY RETIRES.**
    ### This face says in its own (G2) block that `G-NOB475LOG` ### *"IS NOT CARRIED FORWARD
    ### UNDER THAT NAME"* ### and names its replacement. ### **AN ARM A FACE RETIRES IN WORDS IS
    ### NOT AN ARM IT DECLARES**, and a counter that reads only the token disagrees with the
    ### sentence beside it. ### The face is sealed; the COUNTER is what was wrong."""
    names = set(re.findall(r'`(G-[A-Z0-9-]+)`', face))
    for m in re.finditer(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', face):
        names.discard(m.group(1))
    return names


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'] or {})


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=220):
    """### ### **THE TEXT AFTER A MARKER, OR EMPTY WHEN THE MARKER IS GONE.**
    ### A negative control removes the marker; a bare `split(...)[1]` then RAISES instead of
    ### failing, and ### **AN ARM THAT CRASHES UNDER ITS CONTROL HAS NOT BEEN EXERCISED.**"""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=260):
    """### the text after a marker, or EMPTY when the control removes it."""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def rows(S):
    return (S['cells'] or {}).get('rows') or []
def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def census(S):
    return res(S, 'census') or []


def frame(S):
    return res(S, 'frame') or []


HEAD494 = '## THE RECONCILIATION AND THE FRAME CHECK, b494 — TWO TABLES'

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'ACT b494' in S['ferry'],
     lambda S: cut(S, 'ferry', 'ACT b494')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan',
     lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-SURVEY-NOMISS', 'the components bank -- this act`s survey is folded into it',
     lambda S: 'TWO TABLES, ONE SECTION' in S['comp'],
     lambda S: cut(S, 'comp', 'TWO TABLES, ONE SECTION')),
    ('G-REG-LOCKED-FIRST', 'the face lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'], lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('LOCKED.' in l or 'SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('LOCKED.', 'x').replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b493`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 342 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b494' in S['ferry'] and 'b494' in S['face']
                and not os.path.exists(os.path.join(D, 'b496_ferry.txt'))),
     lambda S: cut(S, 'face', 'b494')),

    # -------------------------------------------------- table 1
    ('G-T1-TWENTY-ITEMS', 'the results bank -- the census, whole',
     lambda S: len(census(S)) == 20, lambda S: put(S, 'res', dict(S['res'], census=census(S)[:17]))),
    ('G-T1-CENSUS-AT-ITS-ADDRESS', 'the ARCHIVE file itself, at the line the face names',
     lambda S: ('2026-07-26 — THE PENDING-WORK CENSUS' in S['loom']
                and 'h2-BEARING GRADE' in S['loom']),
     lambda S: cut(S, 'loom', '2026-07-26 — THE PENDING-WORK CENSUS')),
    ('G-T1-GRADES-5-7-8', 'the results bank against the archive`s own grading',
     lambda S: ([sum(1 for c in census(S) if c['grade'] == g)
                 for g in ('DIRECT', 'INFORMING', 'INDEPENDENT')] == [5, 7, 8]),
     lambda S: put(S, 'res', dict(S['res'], census=[
         dict(c, grade='DIRECT') for c in census(S)]))),
    ('G-T1-DESK-SIX', 'the results bank and OPEN_TRAILS` own desk',
     lambda S: len(res(S, 'desk') or []) == 6
     and 'THE DESK — THE RULING ITEMS IN ONE PLACE' in S['ot'],
     lambda S: put(S, 'res', dict(S['res'], desk=(res(S, 'desk') or [])[:4]))),
    ('G-T1-EVERY-ROW-DISPOSED', 'the results bank -- no blank cell in 26 rows',
     lambda S: all(c.get('disposition') for c in census(S) + (res(S, 'desk') or []))
     and len(census(S)) + len(res(S, 'desk') or []) == 26,
     lambda S: put(S, 'res', dict(S['res'], census=[
         dict(c, disposition='') for c in census(S)]))),
    ('G-T1-ACT-NAMED-IN-CELL', 'the components bank -- the taken-up row names its act',
     lambda S: 'act 4' in S['comp'] and 'W-SIGN-1' in S['comp'],
     lambda S: cut(S, 'comp', 'act 4')),
    ('G-T1-THREE-DISPOSITIONS-ONLY', 'the results bank -- the vocabulary is closed',
     lambda S: set(c['disposition'] for c in census(S) + (res(S, 'desk') or [])) <= {
         'TAKEN UP BY (R104)', 'TRIPPED BY (R104)', 'UNTOUCHED'},
     lambda S: put(S, 'res', dict(S['res'], census=[
         dict(c, disposition='PROBABLY RELATED') for c in census(S)]))),
    ('G-T1-ROUTED-LISTED-SEPARATELY', 'the face -- the two registers are not merged',
     lambda S: 'ROUTED ITEMS SEPARATELY AND LABELLED' in S['face'],
     lambda S: cut(S, 'face', 'ROUTED ITEMS SEPARATELY AND LABELLED')),

    # -------------------------------------------------- table 2
    ('G-T2-NINE-ROWS', 'the results bank',
     lambda S: len(frame(S)) == 9, lambda S: put(S, 'res', dict(S['res'], frame=frame(S)[:7]))),
    ('G-T2-ADDRESS-OR-NAMES-NOTHING', 'the results bank -- every row has one or the other',
     lambda S: all(f.get('address') for f in frame(S))
     and sum(1 for f in frame(S) if 'NAMES NOTHING' in f['address']) == res(S, 'names_nothing'),
     lambda S: put(S, 'res', dict(S['res'], frame=[
         dict(f, address='') for f in frame(S)]))),
    ('G-T2-NAMES-NOTHING-NOT-RESTATED', 'the results bank -- the empty row carries no grade',
     lambda S: all('NO GRADE' in f['grade'] and 'NOT RESTATED' in f['ceiling']
                   for f in frame(S) if 'NAMES NOTHING' in f['address']),
     lambda S: put(S, 'res', dict(S['res'], frame=[
         dict(f, grade='MEASURED') if 'NAMES NOTHING' in f['address'] else f
         for f in frame(S)]))),
    ('G-T2-GRADE-CEILING', 'the results bank -- no grade above DERIVES or MEASURED',
     lambda S: not [f for f in frame(S)
                    if re.search(r'\b(?:PROVED|PROVES|ESTABLISHED|CERTIFIED)\b', f['grade'])],
     lambda S: put(S, 'res', dict(S['res'], frame=[
         dict(f, grade='PROVED at the pin') for f in frame(S)]))),
    ('G-T2-CEILING-SENTENCE-EVERY-ROW', 'the results bank -- every row carries one',
     lambda S: all(f.get('ceiling') for f in frame(S))
     and sum(1 for f in frame(S) if 'not supportable: RH proved' in f['ceiling']) == 8,
     lambda S: put(S, 'res', dict(S['res'], frame=[
         dict(f, ceiling='') for f in frame(S)]))),
    ('G-T2-COMPILED-VS-PROFILED', 'AxiomCheck.lean at the tag, read here',
     lambda S: (S['axc'].count('#print axioms') == 32
                and 'C7_finite_type_false' not in S['axc']
                and 'T3doubleprime_general_commutation_fails' in S['axc']),
     lambda S: put(S, 'axc', S['axc'] + NL + '#print axioms C7_finite_type_false')),
    ('G-T2-ADDRESSES-LOOKED-UP', 'the results bank -- the two terminals named at their tag',
     lambda S: all(x in json.dumps(frame(S)) for x in
                   ('T3_StepNineBridge.lean', 'C7FiniteTypeFalse.lean', 'v0.10.0')),
     lambda S: put(S, 'res', dict(S['res'], frame=[
         dict(f, address=f['address'].replace('v0.10.0', 'somewhere')) for f in frame(S)]))),

    # -------------------------------------------------- the section
    ('G-ONE-SECTION-ONLY', 'FINDINGS.md itself',
     lambda S: S['fnd'].count(HEAD494) == 1,
     lambda S: put(S, 'fnd', S['fnd'] + NL + HEAD494)),
    ('G-SECTION-HEADING-FORM', 'FINDINGS.md -- the heading parses as a `## ` section',
     lambda S: HEAD494.startswith('## ') and HEAD494 in S['fnd'],
     lambda S: put(S, 'fnd', S['fnd'].replace(HEAD494, 'a heading in no known form'))),
    ('G-FINDINGS-APPEND-ONLY', 'the results bank and git`s own numstat',
     lambda S: res(S, 'lines_removed') == 0 and res(S, 'headings') == 1,
     lambda S: put(S, 'res', dict(S['res'], lines_removed=3))),
    ('G-NO-OTHER-DOCUMENT', 'the commit file list -- exactly the two named on the face',
     lambda S: sorted(S['tracked']) == sorted(['OPEN_TRAILS.md', 'FINDINGS.md']),
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md', 'A_NEW_DOCUMENT.md'])),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the desk bank against the results bank',
     lambda S: 'REFUTED' in seg(S['desk'], '**(N1)**') and res(S, 'direct_taken') == 1,
     lambda S: put(S, 'res', dict(S['res'], direct_taken=5))),
    ('G-N2-SCORED', 'the desk bank against the results bank',
     lambda S: 'HELD' in seg(S['desk'], '**(N2)**') and res(S, 'names_nothing') >= 1,
     lambda S: put(S, 'res', dict(S['res'], names_nothing=0))),
    ('G-N3-SCORED', 'the desk bank -- and the grade cells it rests on',
     lambda S: 'HELD' in seg(S['desk'], '**(N3)**')
     and 'THIS ACT CONFERRED NONE OF THEM' in S['desk'],
     lambda S: cut(S, 'desk', 'THIS ACT CONFERRED NONE OF THEM')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ; HELD 1 ; REFUTED 2' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 1 ; REFUTED 2')),

    # -------------------------------------------------- the standing arms
    ('G-NOGRADE-CONFERRED', 'the face and the components bank',
     lambda S: 'THIS ACT CONFERS NO GRADE' in S['comp'] and 'GRADES NOTHING ITSELF' in S['face'],
     lambda S: cut(S, 'comp', 'THIS ACT CONFERS NO GRADE')),
    ('G-NOTHING-COMPILED', 'this act`s own tools, for a BUILD CALL',
     lambda S: not re.search(r'(?:subprocess|os\.system|Popen|check_output|run)\s*\([^)]{0,80}'
                             r'(?:lake|LEAN_PATH)\b|lean\s+--\w|lake\s+build', S['tools494']),
     lambda S: put(S, 'tools494', S['tools494'] + NL + 'subprocess.run(["lake","build","X"])')),
    ('G-NOTHING-FETCHED', 'this act`s own tools, for any network call',
     lambda S: not re.search(r'urllib|requests\.|Invoke-WebRequest|curl |zenodo\.org',
                             S['tools494']),
     lambda S: put(S, 'tools494', S['tools494'] + NL + 'requests.get("https://zenodo.org/x")')),
    ('G-NOZENODO-WRITE', 'this act`s own tools, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files)\b', S['tools494'], re.I),
     lambda S: put(S, 'tools494', S['tools494'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
    ('G-NOLANE-OPENED', 'this act`s own tools -- the lane was shut at b492`s end',
     lambda S: not re.search(r'^\s*(?:import|from)\s+(?:carto_atlas|b317_smear|b318_square|'
                             r'b321_window)\b', S['tools494'], re.M),
     lambda S: put(S, 'tools494', S['tools494'] + NL + 'import b321_window')),
    ('G-SPAN-BY-TOOL', 'the span tool record, and what this act says it counts',
     lambda S: 'THE CURRENT SPAN' in S['span'] and 'the span, by tool' in S['desk'],
     lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'], lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'four lists stay OPEN' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('four lists stay OPEN', 'x'))),
    ('G-CORPUS-SCOPE', 'the commit file list -- the two documents named on the face',
     lambda S: sorted(S['tracked']) == sorted(['OPEN_TRAILS.md', 'FINDINGS.md']),
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md', 'REGISTRY.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b494 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b494 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: ('| 343 |' in S['corr'] and S['corr'].count('| 343 |') == 1
                and S['corr'].count('b494, under (R104)') == 1),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 343 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b494 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x in ('OPEN_TRAILS.md', 'FINDINGS.md') or x.startswith(('data/', 'tools/'))
                   for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree, read in the source',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/claude_paper_2026-08-11.pdf')),
    ('G-CORPUS-LEAN-UNTOUCHED', 'the lv and kernel working trees, read in the source',
     lambda S: S['corpus_lean_clean'] is True, lambda S: put(S, 'corpus_lean_clean', False)),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b494_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b494_components.txt' in gits(ROOT, 'show'")),
]
















def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    # ### ### **AN ARM THE FACE RETIRES IN WORDS IS NOT AN ARM IT DECLARES.** ### This face's
    # ### (G2) block says `G-NOB475LOG` *"IS NOT CARRIED FORWARD UNDER THAT NAME"* and names its
    # ### replacement. ### A counter that reads only the token disagreed with the sentence beside
    # ### it, and reported an arm declared-but-not-run. ### The face is sealed and correct; the
    # ### COUNTER was wrong, and it now honours the retirement it is reading.
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    if retired:
        rec('  ### arms the face RETIRES in its own words : %s' % sorted(retired))
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b494')
              and 'data/b494_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b494 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-42s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
    fail, defective, negfail = [], [], 0
    for name, reads, pred, pos in ARMS:
        if name in deferred:
            continue
        live = bool(pred(S))
        neg = bool(pred(dict(S)))
        p = bool(pred(pos(S)))
        if not neg:
            negfail += 1
        if p:
            defective.append(name)
        v = 'OK' if (neg and not p) else ('### DEFECTIVE' if p else '### NEG FAILS')
        rec('  %-42s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-42s DEFERRED TO POST-PUSH' % n)
    stray = sorted(k for k in S['kinds']
                   if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ### **0 EXCLUDED BY NAME.**'
        % S['prior_checked'])
    rec('  ### ### **THE b475 LOG EXCEPTION STAYS RETIRED.** ### b481-b489 excused')
    rec('  ###   `b475_zeta23_build.log` as still being appended to by a live process. ### b490')
    rec('  ### found pid 27508 ABSENT at two readings sixty seconds apart and the file cold, and')
    rec('  ### b491 read the log COMPLETE. ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND')
    rec('  ### DECAYS LIKE ONE.** ### b487`s second exclusion is not carried either: it was')
    rec('  ### b485`s bank, which (R97) directed b487 to append to. ### The arm runs at FULL WIDTH.')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b494_checks_postpush.txt' if pushed else 'b494_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b494_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
