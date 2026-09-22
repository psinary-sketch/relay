# -*- coding: utf-8 -*-
"""b469_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb, honoured in
### advance even though this act is not the one it binds.
"""
import io
import glob
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
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
FACE = os.path.join(D, 'b469_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b469_ferry.txt')),
        scan=read(os.path.join(D, 'b469_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b469_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b469_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b469_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b469_extract.txt')),
        lock=read(os.path.join(D, 'b469_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b469
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b468_closing.txt')),
        addendum=read(os.path.join(D, 'b469_addendum.txt')),
        census=read(os.path.join(D, 'b469_census.txt')),
        span=read(os.path.join(D, 'b469_span_notes.txt')),
        scores=read(os.path.join(D, 'b469_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b469_checks.py')),
        W=json.loads(read(os.path.join(D, 'b469_writes.json')) or '{}'),
        tal=json.loads(read(os.path.join(D, 'b469_tally.json')) or '{}'),
        surv=json.loads(read(os.path.join(D, 'b469_survey.json')) or '{}'),
        comp=read(os.path.join(D, 'b469_components.txt')),
        errata=read(os.path.join(PP, 'ERRATA.md')),
        work=read(os.path.join(PP, 'day1', 'A_Place_to_Stand.md')),
        depmono=read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        desk=read(os.path.join(D, 'b469_desk_notes.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b469_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b469.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b469')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b469_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b469'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-5][0-9]_|^b46[01]_', f)]
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


BINS = ('NAMES A TERMINAL', 'NAMES A CARRIER', 'NAMES NOTHING')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'],
     lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b468 closing -- the prior closed act',
     lambda S: 'row 316' in S['prior'], lambda S: cut(S, 'prior', 'row 316')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the survey bank and file times',
     lambda S: 'THE ACT WRITES; THE SURVEY FIXES WHERE' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b469_extract.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', 'THE ACT WRITES; THE SURVEY FIXES WHERE')),

    ('G-C1-ENTRY-APPENDED-ONCE', 'ERRATA.md itself',
     lambda S: S['errata'].count('## E-2026-09-22-1') == 1,
     lambda S: put(S, 'errata', S['errata'] + NL + '## E-2026-09-22-1 a duplicate that must not exist')),
    ('G-C1-ERRATA-PREFIX-PROVED', 'the writes bank',
     lambda S: S['W'].get('c1', {}).get('prefix') is True and S['W']['c1']['removed'] == 0,
     lambda S: put(S, 'W', dict(S['W'], c1=dict(S['W'].get('c1', {}), prefix=False)))),
    ('G-C1-EIGHT-QUOTED-AT-LINE', 'ERRATA.md against the DEPOSITED monograph',
     lambda S: all(('`%s:%d`' % (e['surface'], e['line'])) in S['errata']
                   for e in S['surv'].get('eight', []))
     and all(e['at_line'] for e in S['surv'].get('eight', [])),
     lambda S: put(S, 'errata', S['errata'].replace('`A_Place_to_Stand.md:58`', '`nowhere:0`'))),
    ('G-C1-EIGHT-ROWS-PRESENT', 'ERRATA.md itself',
     lambda S: sum(1 for e in S['surv'].get('eight', [])
                   if ('`%s` @' % e['terminal']) in S['errata']) == 8,
     lambda S: put(S, 'errata', S['errata'].replace('`KernelCertificate` @', '`gone` @'))),
    ('G-C1-STANDIN-LABELLED', 'ERRATA.md itself',
     lambda S: S['errata'].count('**STAND-IN**') >= 9,
     lambda S: put(S, 'errata', S['errata'].replace('**STAND-IN**', 'a terminal'))),
    ('G-C1-NOTHING-CALLED-WRONG', 'ERRATA.md itself',
     lambda S: 'Nothing published is called wrong by' in S['errata']
     and 'unanchored in the deposit that makes them' in S['errata'],
     lambda S: cut(S, 'errata', 'Nothing published is called wrong by')),
    ('G-C1-NO-ROW-STATED', 'ERRATA.md itself',
     lambda S: '`NO ROW`' in S['errata'] and 'table of seven' in S['errata'],
     lambda S: cut(S, 'errata', '`NO ROW`')),
    ('G-C1-TALLY-RULE-RUN', 'the tally bank',
     lambda S: S['tal'].get('first_draft_pass') is True
     and S['tal'].get('digits') == [] and S['tal'].get('words') == [],
     lambda S: put(S, 'tal', dict(S['tal'], first_draft_pass=False, digits=['40']))),
    ('G-C1-TALLY-QUIRK-REPORTED', 'the tally bank and the components record',
     lambda S: S['tal'].get('seven_in_list') is False
     and 'IT DOES NOT CONTAIN `seven`' in S['comp'],
     lambda S: cut(S, 'comp', 'IT DOES NOT CONTAIN `seven`')),
    ('G-C1-FORM-MATCHES-b456', 'ERRATA.md itself -- both entries read',
     lambda S: all(k in S['errata'] for k in
                   ('**Affected deposits.**', '**Status.**',
                    'NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY.')),
     lambda S: cut(S, 'errata', '**Status.**')),

    ('G-C2-NOTE-APPENDED-ONCE', 'the working monograph itself',
     lambda S: S['work'].count('**Concordance scope note (2026-09-22') == 1,
     lambda S: put(S, 'work', S['work'] + NL + '**Concordance scope note (2026-09-22, a duplicate).**')),
    ('G-C2-NOTE-FORM-MATCHES', 'the working monograph itself',
     lambda S: '**Kernel lineage note (2026-07-24' in S['work']
     and S['work'].index('**Kernel lineage note (2026-07-24')
     < S['work'].index('**Concordance scope note (2026-09-22'),
     lambda S: cut(S, 'work', '**Kernel lineage note (2026-07-24')),
    ('G-C2-NOTE-POINTS-AT-ERRATUM', 'the working monograph itself',
     lambda S: 'E-2026-09-22-1' in S['work'],
     lambda S: put(S, 'work', S['work'].replace('E-2026-09-22-1', 'some entry'))),
    ('G-C2-WORKING-COPY-ONLY', 'the DEPOSITED monograph itself',
     lambda S: 'Concordance scope note' not in S['depmono'],
     lambda S: put(S, 'depmono', S['depmono'] + NL + '**Concordance scope note (2026-09-22).**')),
    ('G-C2-NO-EXISTING-LINE-EDITED', 'the writes bank',
     lambda S: S['W'].get('c2', {}).get('no_line_edited') is True
     and S['W']['c2']['removed'] == 0,
     lambda S: put(S, 'W', dict(S['W'], c2=dict(S['W'].get('c2', {}), no_line_edited=False)))),
    ('G-C2-DEPOSIT-MD5-UNCHANGED', 'the md5 pair banks',
     lambda S: S['W'].get('deposit', {}).get('all_same') is True
     and S['W']['deposit']['unchanged'] == S['W']['deposit']['total'],
     lambda S: put(S, 'W', dict(S['W'], deposit=dict(S['W'].get('deposit', {}), all_same=False)))),
    ('G-C2-DEPOSIT-NOT-STAGED', 'the commit file list',
     lambda S: not any('DEPOSITED-v1.1.2' in x for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['outputs/DEPOSITED-v1.1.2/ERRATA.md'])),

    ('G-C3-R76-ENTRY-ONCE', 'OPEN_TRAILS.md itself',
     lambda S: S['ot'].count('### (R76) \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### (R76) \u2014 a duplicate that must not exist')),
    ('G-C3-RULING-VERBATIM', 'OPEN_TRAILS.md itself',
     lambda S: 'the instrument\u2019s truncation is the corpus\u2019s and no source fires it'
     in S['ot'],
     lambda S: cut(S, 'ot',
                   'the instrument\u2019s truncation is the corpus\u2019s and no source fires it')),
    ('G-C3-R61-LINE-QUOTED', 'OPEN_TRAILS.md, the (R61) record and the (R76) entry',
     lambda S: S['ot'].count('**Trigger: a source enters the record under the import bar that '
                             'ranges over a class containing the corpus\u2019s own objects.') >= 2,
     lambda S: put(S, 'ot', S['ot'].replace(
         '> **Trigger: a source enters the record', '> **A trigger', 1))),
    ('G-C3-B467-TABLES-CITED', 'OPEN_TRAILS.md itself',
     lambda S: 'OPEN_TRAILS.md:7533' in S['ot'] and 'OPEN_TRAILS.md:7556' in S['ot'],
     lambda S: cut(S, 'ot', 'OPEN_TRAILS.md:7533')),
    ('G-C3-R61-RECORD-UNEDITED', 'the writes bank',
     lambda S: S['W'].get('c3', {}).get('r61_record_untouched') is True,
     lambda S: put(S, 'W', dict(S['W'], c3=dict(S['W'].get('c3', {}),
                                                r61_record_untouched=False)))),
    ('G-C3-PARTITION-ROW-POINTED', 'OPEN_TRAILS.md itself',
     lambda S: 'restated in the clause\u2019s coordinates by `(R76)`' in S['ot'],
     lambda S: cut(S, 'ot', 'restated in the clause\u2019s coordinates by `(R76)`')),
    ('G-C3-B448-ROW-UNTOUCHED', 'the writes bank',
     lambda S: S['W'].get('c3', {}).get('b448_row_untouched') is True,
     lambda S: put(S, 'W', dict(S['W'], c3=dict(S['W'].get('c3', {}),
                                                b448_row_untouched=False)))),
    ('G-C3-ONE-LINE-CHANGED-ONLY', 'the writes bank and the act`s own diff',
     lambda S: S['W'].get('c3', {}).get('changed_count') == 1
     and S['W']['c3']['removed'] == 0,
     lambda S: put(S, 'W', dict(S['W'], c3=dict(S['W'].get('c3', {}), changed_count=3)))),
    ('G-C3-PRIOR-ROW-QUOTED', 'the writes bank and OPEN_TRAILS itself',
     lambda S: S['W'].get('c3', {}).get('prior_row_quoted') is True
     and S['surv'].get('partition_row_text', 'x') in S['ot'],
     lambda S: put(S, 'W', dict(S['W'], c3=dict(S['W'].get('c3', {}),
                                                prior_row_quoted=False)))),

    ('G-N1-SCORED', 'the scores bank', lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-SCORED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),

    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOKERNEL-RUN', 'the trail own text',
     lambda S: 'no Lean was run' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('no Lean was run', 'the kernel ran'))),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list -- THREE targets this act, and no fourth',
     lambda S: sorted(S['tracked']) == sorted(
         ['ERRATA.md', 'OPEN_TRAILS.md', 'day1/A_Place_to_Stand.md']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['FINDINGS.md'])),
    ('G-TRAIL-APPEND-PLUS-ONE', 'the trail own text and the writes bank',
     lambda S: S['ot'].count('### b469 \u2014') == 1
     and S['W'].get('c3', {}).get('changed_count') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b469 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 317 |' in S['corr'], lambda S: cut(S, 'corr', '| 317 |')),
    ('G-WRITELIST-KINDS', 'every b469 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'ERRATA', 'day1/', 'data/', 'tools/'))
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
    ('G-NO-DISPOSITION-TWO', 'the deposited monograph and the trail',
     lambda S: 'disposition (ii) is not taken' in S['ot'].lower()
     and S['W'].get('deposit', {}).get('all_same') is True,
     lambda S: put(S, 'ot', S['ot'].replace('disposition (ii) is not taken',
                                            'disposition (ii) is taken'))),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    # ### ### **THE ARM-NAME REGEX COULD NOT SEE ONE OF THE FACE'S OWN ARMS.** ### `[A-Z0-9-]+`
    # ### stops at the first lowercase letter, so `G-C1-FORM-MATCHES-b456` was read as
    # ### `G-C1-FORM-MATCHES-` and the declared set disagreed with the run set by exactly that arm.
    # ### **THE FACE IS RIGHT AND THE COUNTER WAS WRONG** -- an act id is lowercase by this record's
    # ### own convention, and an arm may be named after one. ### Widened here, and the trailing
    # ### hyphen a bare name would leave is stripped so the two spellings cannot both survive.
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b469'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b469 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    rec('  %-36s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 98)
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
        rec('  %-36s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-36s DEFERRED TO POST-PUSH' % n)
    rec('')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b469_checks_postpush.txt' if pushed else 'b469_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b469_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
