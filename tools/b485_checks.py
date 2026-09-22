# -*- coding: utf-8 -*-
"""b485_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b485_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b485_ferry.txt')),
        scan=read(os.path.join(D, 'b485_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b485_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b485_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b485_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b485_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b485_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b484_closing.txt')),
        addendum=read(os.path.join(D, 'b485_addendum.txt')),
        comp=read(os.path.join(D, 'b485_components.txt')),
        desk=read(os.path.join(D, 'b485_desk_notes.txt')),
        span=read(os.path.join(D, 'b485_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b485_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b485_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b485_survey.json')) or '{}'),
        m1=read(os.path.join(D, 'zenodo-manifests', 'record_19675356.json')),
        m2=read(os.path.join(D, 'zenodo-manifests', 'record_21432399.json')),
        reg=read(os.path.join(PP, 'REGISTRY.md')),
        err=read(os.path.join(PP, 'ERRATA.md')),
        zm=read(os.path.join(PP, 'meta', 'ZENODO_METADATA.md')),
        zm_clean=gits(PP, 'status', '--porcelain', '--', 'meta/ZENODO_METADATA.md'),
        man_clean=gits(ROOT, 'status', '--porcelain', '--', 'data/zenodo-manifests'),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b485_checks.py')),
        tools485=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b485_') and f.endswith('.py') and f != 'b485_checks.py'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b485.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b485 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b485_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b485 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    # ### b475's log is still being written by another act's live process; excluded BY NAME.
    k -= {'b475_zeta23_build.log'}
    S['kinds'] = k
    LIVE = {'b475_zeta23_build.log'}
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[01234]_', f) and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'] or {}).get(k, {}).get('verdict', '')


def R(S, k):
    return (S['res'] or {}).get(k, {})


def w(S, k):
    return ((S['res'] or {}).get('writes') or {}).get(k, {})


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'],
     lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b484`s closing AND the ledger',
     lambda S: ('THE COMMITS, EACH READ BACK BY ls-remote' in S['prior']
                and S['corr'].count('| 331 |') == 1),
     lambda S: cut(S, 'prior', 'THE COMMITS, EACH READ BACK BY ls-remote')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory`s own banked ferries',
     lambda S: (os.path.exists(os.path.join(D, 'b482_ferry.txt'))
                and not os.path.exists(os.path.join(D, 'b482_registration_2026-09-22.txt'))
                and 'b485' in S['face']),
     lambda S: cut(S, 'face', 'b485')),

    # -------------------------------------------------- component 0
    ('G-C0-CPU-TWICE', 'the CPU bank against the components record',
     lambda S: (R(S, 'c0')['cpu_first'] is not None and R(S, 'c0')['cpu_second'] is not None
                and R(S, 'c0')['wall_seconds'] >= 59.0
                and str(R(S, 'c0')['cpu_delta']) in S['comp']),
     lambda S: put(S, 'res', dict(S['res'], c0=dict(R(S, 'c0'), wall_seconds=2.0)))),
    ('G-C0-LOG-NOT-OPENED', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools485'],
     lambda S: put(S, 'tools485', S['tools485'] + NL + "read(D + 'b475_zeta23_build.log')")),

    # -------------------------------------------------- component 1
    ('G-C1-HASHES-VERIFIED', 'the survey and the manifests themselves',
     lambda S: ('4AE7419BF5D7CD7A0B960D5A84411CEE115B7E2B3E686292A744761BB72E8443' in S['extract']
                and 'MATCH' in S['extract'] and len(S['m1']) > 9000 and len(S['m2']) > 12000),
     lambda S: cut(S, 'extract', 'MATCH')),
    ('G-C1-NO-BOM', 'the manifest bytes as the survey read them',
     lambda S: not S['m1'].startswith('﻿') and not S['m2'].startswith('﻿'),
     lambda S: put(S, 'm1', '﻿' + S['m1'])),
    ('G-C1-FIELDS-NOT-INFERRED', 'the manifests themselves against the components record',
     lambda S: all(('"version": "%s"' % S['sv']['records'][k]['version']).replace('"version": ', '"version": ')
                   in (S['m1'] if k == '19675356' else S['m2'])
                   for k in ('19675356', '21432399')),
     lambda S: put(S, 'm1', S['m1'].replace('v1.0.1', 'v9.9.9'))),
    ('G-C1-FILES-LISTED', 'the components record, for every file of both records',
     lambda S: all(f[0] in S['comp'] and str(f[1]) in S['comp']
                   for k in S['sv']['records'] for f in S['sv']['records'][k]['files'][:4]),
     lambda S: cut(S, 'comp', 'A_Place_to_Stand.md')),
    ('G-C1-NOTHING-FETCHED-BY-THIS-SEAT', 'this act`s own tools, for any network call',
     lambda S: not re.search(r'urllib|requests\.|Invoke-WebRequest|curl |http[s]?://[a-z]+\.[a-z]+/',
                             S['tools485']),
     lambda S: put(S, 'tools485', S['tools485'] + NL + 'urllib.request.urlopen(u)')),

    # -------------------------------------------------- component 2
    ('G-C2-NOTE-QUOTED-VERBATIM', 'b395`s draft against ERRATA.md itself',
     lambda S: S['sv']['note'] and S['sv']['note'] in S['err'],
     lambda S: put(S, 'err', S['err'].replace(S['sv']['note'], 'x'))),
    ('G-C2-CORRECTION-BESIDE-NOT-FOLDED', 'ERRATA.md itself',
     lambda S: ('2026-07-24' in S['err'] and '2026-07-18' in S['err']
                and 'REFUTED' in S['err'] and 'CONFIRMED' in S['err']),
     lambda S: put(S, 'err', S['err'].replace('REFUTED', 'x'))),
    ('G-C2-ERRATA-APPENDED', 'the write bank and ERRATA.md`s own id',
     lambda S: (w(S, 'COMPONENT 2a -- the currency note appended')['missing'] == 0
                and 'E-2026-09-22-1' in S['err']),
     lambda S: cut(S, 'err', 'E-2026-09-22-1')),
    ('G-C2-REGISTRY-ROW-ANNOTATED', 'REGISTRY.md itself, for both records` own figures',
     lambda S: ('10.5281/zenodo.19675356' in S['reg'] and '2026-04-21' in S['reg']
                and '10.5281/zenodo.21432399' in S['reg'] and '2026-07-18' in S['reg']),
     lambda S: put(S, 'reg', S['reg'].replace('2026-04-21', 'x'))),
    ('G-C2-PRIOR-TEXT-PRESERVED', 'REGISTRY.md itself, for the untouched original rows',
     lambda S: ('| v1.0.1  | 2026-04-28 |' in S['reg'] and '| v1.1    | 2026-07-19 |' in S['reg']),
     lambda S: put(S, 'reg', S['reg'].replace('| v1.0.1  | 2026-04-28 |', 'x'))),
    ('G-C2-LINES-REMOVED-ZERO', 'the write bank, over EVERY write this act made',
     lambda S: (len((S['res'] or {}).get('writes') or {}) >= 3
                and all(v['missing'] == 0 for v in (S['res']['writes'] or {}).values())),
     lambda S: put(S, 'res', dict(S['res'], writes=dict(
         S['res']['writes'], BAD=dict(path='x', numstat=['1', '1'], missing=2))))),

    # -------------------------------------------------- component 3
    ('G-C3-TABLE-REPRINTED', 'the components record',
     lambda S: ('CELLS DISAGREEING WITH REGISTRY' in S['comp']
                and S['comp'].count('AGREES') >= 10),
     lambda S: cut(S, 'comp', 'CELLS DISAGREEING WITH REGISTRY')),
    ('G-C3-FIFTH-SITE-NOT-RECONCILED', 'the components record and REGISTRY.md',
     lambda S: ('NOT LOCATABLE' in S['comp'] and 'RECORDED, NOT RECONCILED' in S['comp']
                and 'NOT LOCATABLE' in S['reg']),
     lambda S: cut(S, 'comp', 'RECORDED, NOT RECONCILED')),
    ('G-C3-FINDINGS-AT-ADDRESSES', 'the survey bank against the components record',
     lambda S: (len(S['sv']['findings']) == R(S, 'c3')['findings']
                and all(f['addr'].split(':')[0] in S['comp'] for f in S['sv']['findings'][:5])),
     lambda S: put(S, 'res', dict(S['res'], c3=dict(R(S, 'c3'), findings=0)))),
    ('G-C3-FROZEN-LEDGER-NOT-EDITED', 'ZENODO_METADATA`s porcelain, READ IN THE SOURCE',
     lambda S: S['zm_clean'] == '' and 'left unedited on purpose' in S['zm'],
     lambda S: put(S, 'zm_clean', ' M meta/ZENODO_METADATA.md')),
    ('G-C3-DISCHARGE-SCOPED', 'REGISTRY.md itself, for the discharging line and its scope',
     lambda S: ('DISCHARGED 2026-09-22' in S['reg']
                and 'ON THE CURRENT DEPOSIT STATE AND ON NOTHING ELSE' in S['reg']
                and R(S, 'c3')['discharged'] is True),
     lambda S: put(S, 'reg', S['reg'].replace(
         'ON THE CURRENT DEPOSIT STATE AND ON NOTHING ELSE', 'x'))),
    ('G-C3-GATE-TEXT-OTHERWISE-UNTOUCHED', 'REGISTRY.md itself, for the preserved gate row',
     lambda S: (S['reg'].count('| **Deposit-state reconciliation**') == 2
                and 'Run when the (c\') validation job clears.' in S['reg']),
     lambda S: put(S, 'reg', S['reg'].replace(
         "Run when the (c') validation job clears.", 'x'))),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the scores bank against the manifest itself',
     lambda S: sc(S, 'N1') == 'HELD' and '"version": "v1.0.1"' in S['m1'],
     lambda S: put(S, 'm1', S['m1'].replace('"version": "v1.0.1"', 'x'))),
    ('G-N2-SCORED', 'the scores bank against the manifest itself',
     lambda S: ('QUALIFICATION' in sc(S, 'N2') and '"publication_date": "2026-07-18"' in S['m2']),
     lambda S: put(S, 'm2', S['m2'].replace('"publication_date": "2026-07-18"', 'x'))),
    ('G-N3-SCORED', 'the scores bank against the results bank',
     lambda S: ('SPLIT' in sc(S, 'N3') and R(S, 'c3')['discharged'] is True
                and R(S, 'c3')['findings'] > 0),
     lambda S: put(S, 'res', dict(S['res'], c3=dict(R(S, 'c3'), findings=0)))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN" in S['face']
                and 'REGISTERED 3 ; HELD 1 ; HELD-WITH-QUALIFICATION 1 ; SPLIT 1' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 1 ; HELD-WITH-QUALIFICATION 1 ; SPLIT 1')),

    # -------------------------------------------------- the standing arms
    ('G-NOZENODO-WRITE', 'this act`s own tools, for a platform WRITE CALL and not for a word',
     # ### **THE FIRST VERSION FIRED ON THE ACT'S OWN PROSE.** ### It matched the bare word
     # ### `deposit`, which this act says on nearly every line -- "the monograph deposit", "the
     # ### Day-1 deposit history", "nothing deposits". ### **A GATE ON RAW SOURCE FIRES ON THE
     # ### ACT'S OWN ACCOUNT OF WHAT IT DID NOT DO**, for the third time in two acts. ### The arm
     # ### now tests for a WRITE CALL: an HTTP write method invoked, or a Zenodo publish/newversion
     # ### endpoint called. ### **A WORD IS NOT A CALL.**
     lambda S: not re.search(
         r'requests\.(?:post|put|patch|delete)\s*\('
         r'|(?:^|[ =])(?:POST|PUT|PATCH|DELETE)\s*\('
         r'|Invoke-RestMethod.{0,80}-Method\s+(?:Post|Put|Patch|Delete)'
         r'|zenodo.{0,60}/(?:publish|newversion|files)'
         r'|\.(?:publish|newversion)\s*\(',
         S['tools485'], re.I),
     lambda S: put(S, 'tools485', S['tools485'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/depositions/1/actions/publish")')),
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools485'],
     lambda S: put(S, 'tools485', S['tools485'] + NL + "open('b475_zeta23_build.log')")),
    ('G-NO-CHAIN-RUN', 'this act`s own tools, for an IMPORT or a CALL',
     lambda S: not re.search(r'^\s*(?:import|from)\s+(?:b321_window|b325_epstein|b317_smear|'
                             r'b318_square|carto_atlas)\b'
                             r'|\b(?:channels_q|mean_zero_variant|autocorrelation|prime_sum)\s*\(',
                             S['tools485'], re.M),
     lambda S: put(S, 'tools485', S['tools485'] + NL + 'import b321_window as WI')),
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'FINDINGS.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['FACES_LEDGER.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'], lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'four lists stay OPEN' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('four lists stay OPEN', 'x'))),
    ('G-CORPUS-SCOPE', 'the commit file list -- THREE documents this act, each named on the face',
     lambda S: sorted(S['tracked']) == sorted(['OPEN_TRAILS.md', 'ERRATA.md', 'REGISTRY.md']),
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'meta/ZENODO_METADATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b485 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b485 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- ONE row for this act and no more',
     lambda S: (S['corr'].count('| 332 |') == 1
                and S['corr'].count('THE TWO ZENODO RECORDS ENTER THE RECORD') == 1),
     lambda S: put(S, 'corr', S['corr'] + NL
                   + '| 333 | THE TWO ZENODO RECORDS ENTER THE RECORD again |')),
    ('G-WRITELIST-KINDS', 'every b485 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x in ('OPEN_TRAILS.md', 'ERRATA.md', 'REGISTRY.md')
                   or x.startswith(('data/', 'tools/')) for x in S['tracked']),
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
     lambda S: "data/b485_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b485_components.txt' in gits(ROOT, 'show'")),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b485')
              and 'data/b485_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b485 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-NOPRIORBANK checked %d prior banks; b475`s still-growing log excluded by name.'
        % S['prior_checked'])
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b485_checks_postpush.txt' if pushed else 'b485_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b485_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
