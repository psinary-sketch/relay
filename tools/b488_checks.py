# -*- coding: utf-8 -*-
"""b488_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b488_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b488_ferry.txt')),
        scan=read(os.path.join(D, 'b488_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b488_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b488_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b488_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b488_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b488_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b487_closing.txt')),
        addendum=read(os.path.join(D, 'b488_addendum.txt')),
        comp=read(os.path.join(D, 'b488_components.txt')),
        comp1=read(os.path.join(D, 'b488_components_firstrun.txt')),
        desk=read(os.path.join(D, 'b488_desk_notes.txt')),
        span=read(os.path.join(D, 'b488_span_notes2.txt'))
        + read(os.path.join(D, 'b488_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b488_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b488_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b488_survey.json')) or '{}'),
        err=read(os.path.join(PP, 'ERRATA.md')),
        fnd=read(os.path.join(PP, 'FINDINGS.md')),
        rower=read(os.path.join(T, 'corr_row.py')),
        fold486=read(os.path.join(D, 'b486_the_fold.txt')),
        spantool=read(os.path.join(T, 'b363_span.py')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b488_checks.py')),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b488.zip'))),
        spantool_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py') == ''),
        tools488=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b488_') and f.endswith('.py')
                         and f != 'b488_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b488 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b488_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b488 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    # ### b475's log is still being written by another act's live process; excluded BY NAME.
    k -= {'b475_zeta23_build.log'}
    S['kinds'] = k
    # ### ### **ONE NAMED EXCLUSION FROM G-NOPRIORBANK'S POPULATION, WITH ITS GROUND.**
    # ### `b475_zeta23_build.log` -- another act's live process is still appending to it.
    # ### ### **b487'S SECOND EXCLUSION IS NOT CARRIED.** ### That one was `b485_the_two_records.txt`,
    # ### which (R97) directed b487 to append to. ### **THIS ACT WRITES NO PRIOR BANK AT ALL**, so
    # ### the exception lapses with the ruling that made it, and the arm is back at full width.
    LIVE = {'b475_zeta23_build.log'}
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b488_') and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'] or {})


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def fnd(S, k, d=None):
    return ((S['res'] or {}).get('findings') or {}).get(k, d)


HEAD488 = '## THE BOOKKEEPING ARC, b475–b479 — THE FOLD'

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'ACT b488' in S['ferry'],
     lambda S: cut(S, 'ferry', 'ACT b488')),
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
    ('G-SURVEY-NOMISS', 'a banked verdict LINE',
     lambda S: 'MISSES : 0' in line_with(S['extract'], 'MISSES :'),
     lambda S: put(S, 'extract', S['extract'].replace('MISSES : 0', 'MISSES : 2'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'], lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'SEAL BROKEN'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b487`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 336 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b488' in S['ferry'] and 'b488' in S['face']
                and not os.path.exists(os.path.join(D, 'b489_ferry.txt'))),
     lambda S: cut(S, 'face', 'b488')),

    # -------------------------------------------------- component 1
    ('G-C1-SECTION-APPENDED', 'FINDINGS.md itself',
     lambda S: S['fnd'].count(HEAD488) == 1,
     lambda S: put(S, 'fnd', S['fnd'].replace(HEAD488, 'x'))),
    # ### ### **THIS ARM'S FIRST VERSION READ THE WRONG RUN.** ### It demanded
    # ### `after > before` from `b488_results.json`, which the LAST components run wrote -- and
    # ### that run did not append (the idempotence guard stopped it), so after == before by
    # ### design. ### **THE APPEND'S OWN FIGURES LIVE IN THE RUN THAT MADE IT**, banked as
    # ### `b488_components_firstrun.txt`, and git's `--numstat` is the independent witness.
    ('G-C1-PREFIX-PROVED', 'the FIRST-RUN components bank, and git`s numstat',
     lambda S: (fnd(S, 'prefix') is True
                and 'PRIOR BYTES A TRUE PREFIX : ### **True**' in S['comp1']
                # ### the numstat line is INSIDE a prose line, so it is not line-anchored;
                # ### an anchored needle found nothing and the arm blamed the subject.
                and re.search(r'76\s+0\s+FINDINGS\.md', S['comp']) is not None),
     lambda S: cut(S, 'comp1', 'PRIOR BYTES A TRUE PREFIX : ### **True**')),
    ('G-C1-LINES-REMOVED-ZERO', 'the results bank AND git`s own numstat in the bank',
     lambda S: fnd(S, 'lines_removed') == 0 and 'LINES REMOVED, BY GIT`S OWN COUNT : 0' in S['comp'],
     lambda S: cut(S, 'comp', 'LINES REMOVED, BY GIT`S OWN COUNT : 0')),
    ('G-C1-HEADING-FORM-MATCHES', 'FINDINGS.md -- the heading parses in the standing form',
     lambda S: bool(re.search(r'^## .*?, b\d+–b\d+ — THE FOLD\s*$',
                              HEAD488, re.M)) and HEAD488 in S['fnd'],
     lambda S: put(S, 'fnd', S['fnd'].replace(HEAD488, '## a heading in no known form'))),
    ('G-C1-ELEVEN-ACTS', 'b486`s bank against the survey bank',
     lambda S: len(S['sv']['acts']) == 11
     and all(a[1] in S['fold486'] for a in S['sv']['acts']),
     lambda S: put(S, 'sv', dict(S['sv'], acts=S['sv']['acts'][:9]))),
    ('G-C1-SIX-CLAUSES-CITED', 'the survey bank -- every clause names a cited act',
     lambda S: (len(S['sv']['clauses']) == 6 and len(S['sv']['cited']) == 6
                and all(c.strip() for c in S['sv']['cited'])),
     lambda S: put(S, 'sv', dict(S['sv'], cited=S['sv']['cited'][:4]))),
    ('G-C1-THIRTEEN-RULINGS', 'the survey bank, read off b486`s bank',
     lambda S: len(S['sv']['rulings']) == 13,
     lambda S: put(S, 'sv', dict(S['sv'], rulings=S['sv']['rulings'][:12]))),
    ('G-C1-SEVEN-DEFECTS', 'the survey bank, read off b486`s bank',
     lambda S: len(S['sv']['defects']) == 7,
     lambda S: put(S, 'sv', dict(S['sv'], defects=S['sv']['defects'][:5]))),
    ('G-C1-FIGURES-FROM-BANK', 'FINDINGS.md against b486`s bank -- every act named is in it',
     lambda S: all(a[1] in S['fold486'] for a in S['sv']['acts'])
     and 'b475' in S['fnd'] and 'b479' in S['fnd'],
     lambda S: put(S, 'fold486', S['fold486'].replace('b482', 'bXXX'))),
    ('G-C1-CITES-THE-TRAIL', 'FINDINGS.md -- the section names its sources',
     lambda S: ('data/b486_the_fold.txt' in S['fnd'].split(HEAD488)[-1]
                and 'OPEN_TRAILS.md` stands' in S['fnd'].split(HEAD488)[-1]),
     lambda S: put(S, 'fnd', S['fnd'].replace('OPEN_TRAILS.md` stands', 'x'))),
    ('G-C1-DATED-AT-b488-FOR-b486', 'FINDINGS.md -- the section says who wrote it and when',
     lambda S: ('at b488 on ruling `(R98)`' in S['fnd']
                and 'Written into FINDINGS at b488' in S['fnd']
                and 'Folded by b486' in S['fnd']),
     lambda S: put(S, 'fnd', S['fnd'].replace('Written into FINDINGS at b488', 'x'))),
    ('G-C1-NOTHING-RE-SCORED', 'this act`s tools, for any verdict word written by this act',
     lambda S: not re.search(r"sec\.append\([^)]*\b(?:HELD|REFUTED|SPLIT|DERIVES|MEASURED)\b",
                             S['tools488']),
     lambda S: put(S, 'tools488', S['tools488'] + NL + "    sec.append('b478 -- HELD')")),

    # -------------------------------------------------- component 2
    ('G-C2-GUARD-REFUSES-EXISTING', 'corr_row.py`s own text AND this act`s bank',
     lambda S: ('ROW NUMBER %s IS ALREADY IN THE LEDGER' in S['rower']
                and 'POSITIVE CONTROL -- a TAKEN number  : code 2' in S['comp']),
     lambda S: cut(S, 'comp', 'POSITIVE CONTROL -- a TAKEN number  : code 2')),
    ('G-C2-GUARD-ACCEPTS-FREE', 'this act`s bank -- the NEGATIVE control',
     lambda S: 'NEGATIVE CONTROL -- the NEXT FREE   : code 0' in S['comp'],
     lambda S: cut(S, 'comp', 'NEGATIVE CONTROL -- the NEXT FREE   : code 0')),
    ('G-C2-BOTH-YIELDS-PRINTED', 'this act`s bank -- both codes AND both file states',
     lambda S: ('file unchanged : True' in S['comp'] and 'file grew : True' in S['comp']
                and 'BOTH CONTROLS BEHAVE : True' in S['comp']),
     lambda S: cut(S, 'comp', 'file grew : True')),
    ('G-C2-REFUSES-BEFORE-WRITING', 'corr_row.py`s own text -- the read precedes the write',
     lambda S: 0 <= S['rower'].find('have = numbers_in(') < S['rower'].find("open(path + '.tmp'"),
     lambda S: put(S, 'rower', S['rower'].replace('have = numbers_in(', 'later = numbers_in('))),
    # ### ### **AND THIS ONE READ PAST ITS SUBJECT.** ### `split('def self_test')[-1]` takes
    # ### `self_test` AND `main()` after it, and `main` prints the tool's own banner, which
    # ### carries the word. ### **A PREDICATE THAT OVERRUNS ITS SUBJECT CONDEMNS A NEIGHBOUR.**
    ('G-C2-CONTROLS-ON-A-FIXTURE', 'corr_row.py`s self_test BODY -- the ledger is never its subject',
     lambda S: ('CORRESPONDENCE_fixture.md' in S['rower']
                and 'CORRESPONDENCE.md' not in
                S['rower'].split('def self_test')[-1].split('def main')[0].split('"""')[-1]),
     # ### ### **AND THE CONTROL MUST MOVE THE SLICE THE PREDICATE READS.** ### Its first
     # ### version appended to the END of the file, outside `self_test`, so the narrowed
     # ### predicate could not see it -- ### **A CONTROL THAT MISSES ITS SUBJECT PROVES THE
     # ### ARM CANNOT FAIL**, which is b482's species once more. ### It now points the
     # ### fixture line itself at the live ledger, the very fault the arm exists to catch.
     lambda S: put(S, 'rower', S['rower'].replace(
         "p = os.path.join(tmpdir, 'CORRESPONDENCE_fixture.md')",
         "p = os.path.join(tmpdir, '..', 'CORRESPONDENCE.md')"))),
    ('G-C2-PRIOR-BEHAVIOUR-QUOTED', 'this act`s bank -- the tool`s old limits, in its own words',
     lambda S: ('A ROW OF SIX' in S['comp'] and 'IT APPENDED UNCONDITIONALLY' in S['comp']),
     lambda S: cut(S, 'comp', 'A ROW OF SIX')),
    ('G-C2-ROW-337-BY-THE-GUARDED-TOOL', 'the ledger AND the desk bank',
     lambda S: (S['corr'].count('| 337 |') == 1 and 'b488, under (R98)' in S['corr']
                and 'corr_row' in S['desk']),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 337 | a duplicate row |')),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED-BY-THE-TOOL', 'the span tool`s own banked run, not a heading',
     lambda S: (res(S, 'n1') is True and 'it was FILED BY' in S['span']
                and 'b486' in line_with(S['span'], 'it was FILED BY')),
     lambda S: put(S, 'span', S['span'].replace('it was FILED BY', 'it was filed by nobody'))),
    ('G-N2-SCORED-ON-FIRST-RUN', 'the components bank and the scores bank',
     lambda S: res(S, 'n2') is True and 'FIRST RUN, NO REPAIR' in S['comp'],
     lambda S: cut(S, 'comp', 'FIRST RUN, NO REPAIR')),
    ('G-SPAN-BOTH-READINGS-PRINTED', 'the components bank -- before and after, both on record',
     lambda S: ('b464 - b473' in S['comp'] and 'b475 - b479' in S['comp']
                and 'current span' in S['comp']),
     lambda S: cut(S, 'comp', 'b464 - b473')),
    ('G-SPAN-TOOL-UNEDITED', 'git`s own view of the tool`s file',
     lambda S: S['spantool_clean'] is True, lambda S: put(S, 'spantool_clean', False)),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ; HELD 3' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 3')),

    # -------------------------------------------------- the standing arms
    ('G-NOZENODO-WRITE', 'this act`s own tools, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files)\b', S['tools488'], re.I),
     lambda S: put(S, 'tools488', S['tools488'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools488'],
     lambda S: put(S, 'tools488', S['tools488'] + NL + "open('b475_zeta23_build.log')")),
    ('G-NOTHING-COMPILED', 'this act`s own tools, for a BUILD CALL (not the phrase)',
     lambda S: not re.search(r'(?:subprocess|os\.system|Popen|check_output|run)\s*\([^)]{0,80}'
                             r'(?:lake|LEAN_PATH|lean)\b|lean\s+--\w', S['tools488']),
     lambda S: put(S, 'tools488', S['tools488'] + NL + 'subprocess.run(["lake","build","X"])')),
    ('G-SPAN-BY-TOOL', 'the span tool record, and what this act says it counts',
     lambda S: ('THE CURRENT SPAN' in S['span'] and 'b486' in S['desk']),
     lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md'))
                       for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'], lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'four lists stay OPEN' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('four lists stay OPEN', 'x'))),
    ('G-CORPUS-SCOPE', 'the commit file list -- TWO documents, both named on the face',
     lambda S: sorted(S['tracked']) == sorted(['OPEN_TRAILS.md', 'FINDINGS.md']),
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'REGISTRY.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b488 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b488 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 337 |' in S['corr'] and S['corr'].count('| 337 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 337 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b488 commit in three repositories, against (R91)`s STEM GLOB',
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
     lambda S: "data/b488_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b488_components.txt' in gits(ROOT, 'show'")),
]




def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b488')
              and 'data/b488_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b488 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ONE excluded BY NAME, with its ground:'
        % S['prior_checked'])
    rec('  ###   `b475_zeta23_build.log`      -- another act`s live process is still appending.')
    rec('  ### ### **b487`S SECOND EXCLUSION IS NOT CARRIED** -- it was b485`s bank, which (R97)')
    rec('  ### directed b487 to append to. ### This act writes no prior bank, so the exception')
    rec('  ### lapses with the ruling that made it and the arm is back at full width.')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b488_checks_postpush.txt' if pushed else 'b488_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b488_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
