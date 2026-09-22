# -*- coding: utf-8 -*-
"""b474_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b474_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b474_ferry.txt')),
        scan=read(os.path.join(D, 'b474_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b474_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b474_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b474_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b474_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b474_lockgate_notes*.txt')))[-1]),
        lock_runs=len(glob.glob(os.path.join(D, 'b474_lockgate_notes*.txt'))),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b474
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b473_closing.txt')),
        addendum=read(os.path.join(D, 'b474_addendum.txt')),
        census=read(os.path.join(D, 'b474_census.txt')),
        span=read(os.path.join(D, 'b474_span_notes.txt')),
        scores=read(os.path.join(D, 'b474_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b474_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b474_survey.json')) or '{}'),
        fold=json.loads(read(os.path.join(D, 'b474_fold.json')) or '{}'),
        comp=read(os.path.join(D, 'b474_components.txt')),
        foldrun=read(os.path.join(D, 'b474_fold_run.txt')),
        lane=read(os.path.join(D, 'b474_lane.txt')),
        ferry2=read(os.path.join(D, 'b475_ferry.txt')),
        findings=read(os.path.join(PP, 'FINDINGS.md')),
        digest=read(os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')),
        findings_head=gits(PP, 'show', 'HEAD:FINDINGS.md'),
        digest_head=gits(PP, 'show', 'HEAD:phase2/method/THE_FINDINGS_AS_THEY_STAND.md'),
        ot_head=gits(PP, 'show', 'HEAD:OPEN_TRAILS.md'),
        tools474=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b474_') and f.endswith('.py') and f != 'b474_checks.py'),
        closings={a: read(os.path.join(D, '%s_closing.txt' % a))
                  for a in ('b464', 'b466', 'b467', 'b468', 'b469', 'b468r', 'b470', 'b471', 'b472', 'b473')},
        desk=read(os.path.join(D, 'b474_desk_notes.txt')),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        faces_dirty=(gits(PP, 'status', '--porcelain', '--', 'FACES_LEDGER.md') != ''),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b474_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b474.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b474')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b474_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b474'):
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

def nz(x):
    return (x or '').replace(chr(13) + NL, NL)


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 2)' in S['ferry'], lambda S: cut(S, 'ferry', 'paste ends (part 1 of 2)')),
    ('G-PART2-BANKED-NOT-RUN', 'part 2`s bank and this act`s own outputs',
     lambda S: ('paste ends (part 2 of 2)' in S['ferry2']
                and not os.path.exists(os.path.join(D, 'b475_zeta23_build.log'))
                and not os.path.exists(os.path.join(D, 'b475_launch.json'))),
     lambda S: put(S, 'ferry2', '')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAG-LABELLED', 'the banked scan',
     lambda S: '(R81) FLAGS : 1' in S['scan'] and 'Bare in the act text : 0' in S['scan']
     and 'carries: [procedural]' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('Bare in the act text : 0', 'Bare in the act text : 1'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b473 closing -- the prior closed act',
     lambda S: 'row 322' in S['prior'], lambda S: cut(S, 'prior', 'row 322')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),

    ('G-F1-TEN-ROWS', 'the fold bank',
     lambda S: len(S['fold']['rows']) == 10 and [r['act'] for r in S['fold']['rows']][0] == 'b464'
     and [r['act'] for r in S['fold']['rows']][-1] == 'b473' and 'b465' not in [r['act'] for r in S['fold']['rows']],
     lambda S: put(S, 'fold', dict(S['fold'], rows=S['fold']['rows'][:9]))),
    ('G-F1-STRINGS-VERIFIED', 'the fold bank',
     lambda S: S['fold']['strings'] == S['fold']['verified'] == 23 and S['fold']['all_matched'] is True,
     lambda S: put(S, 'fold', dict(S['fold'], all_matched=False))),
    ('G-F1-STRINGS-IN-OWN-BANK', 'each act`s own closing, supplied',
     lambda S: all(any(g['count'] >= 1 for g in r['strings'])
                   and all(g['count'] >= 1 for g in r['strings'])
                   and all(S['closings'][r['act']] for g in r['strings'])
                   for r in S['fold']['rows']),
     lambda S: put(S, 'fold', dict(S['fold'], rows=[dict(r, strings=[dict(g, count=0) for g in r['strings']])
                                                    for r in S['fold']['rows']]))),
    ('G-F1-COLUMNS-PRINTED', 'the written section',
     lambda S: 'RECORD 7' in S['comp'].replace('RECORD %d' % 7, 'RECORD 7')
     and '**7**' in S['findings'] and '### The three columns, kept apart' in S['findings'],
     lambda S: put(S, 'findings', '')),
    ('G-F1-OBJECT-COLUMN-EMPTY', 'the fold bank and the section',
     lambda S: S['fold']['columns'].get('OBJECT', 0) == 0
     and 'object column is empty for the tenth consecutive span' in S['findings'],
     lambda S: put(S, 'fold', dict(S['fold'], columns=dict(S['fold']['columns'], OBJECT=1)))),
    ('G-F1-BORDERLINE-MARKED', 'the section`s own rows',
     lambda S: S['findings'].count('BORDERLINE') >= 3
     and all(('*BORDERLINE' in S['findings']) for _ in (0,)),
     lambda S: put(S, 'findings', S['findings'].replace('BORDERLINE', 'plain'))),
    ('G-F1-SPAN-BOTH-NUMBERS', 'the section and the span tool`s record',
     lambda S: ('reads **%s**' % S['fold']['span_tool']) in S['findings'] and 'is **10**' in S['findings']
     and 'b464 - b473 (10 acts)' in S['span'],
     lambda S: put(S, 'fold', dict(S['fold'], span_tool='99'))),
    ('G-F1-RULINGS-TABLE', 'the section against the survey`s ruling read',
     lambda S: all(('`(R%d)`' % n) in S['findings'] for n in range(74, 85))
     and 'VOID FOR WANT' in S['findings'],
     lambda S: cut(S, 'findings', '`(R84)`')),
    ('G-F1-RULING-ENTRY-ANCHORED', 'the survey tool`s own text and its yield',
     lambda S: "re.search(r'^### \\(R%d\\)' % n, ot, re.M)" in S['tools474']
     and S['sv']['rulings']['(R81)']['entry_in_open_trails'] is False
     and S['sv']['rulings']['(R76)']['entry_in_open_trails'] is True,
     lambda S: put(S, 'sv', dict(S['sv'], rulings=dict(S['sv']['rulings'],
                                                       **{'(R81)': dict(entry_in_open_trails=True, ferries=[])})))),
    ('G-F1-LEDGERS-BOTH', 'the section`s own text',
     lambda S: 'The navigator\u2019s, three' in S['findings'].encode('ascii', 'backslashreplace').decode()
     or ('The navigator' in S['findings'] and 'The seat' in S['findings'] and 'third recurrence' in S['findings']),
     lambda S: cut(S, 'findings', 'third recurrence')),
    ('G-F1-ADDITIVE-PREFIX', 'the three targets against their own HEAD blobs',
     lambda S: (nz(S['findings']).startswith(nz(S['findings_head']).rstrip(NL))
                and nz(S['digest']).startswith(nz(S['digest_head']).rstrip(NL))
                and nz(S['ot']).startswith(nz(S['ot_head']).rstrip(NL))),
     lambda S: put(S, 'findings', 'a rewritten document')),
    ('G-F1-NOTHING-MINTED', 'the section`s own closing sentence',
     lambda S: 'nothing is minted' in S['findings'] and 'no grade is conferred by a seat' in S['findings'],
     lambda S: cut(S, 'findings', 'nothing is minted')),

    # ### The first form of this arm built its needle with `.encode().decode('unicode_escape')`, which
    # ### mangles the em dash it was looking for: the arm failed on its own needle while the digest
    # ### carried the quotation exactly. ### It now compares the fold bank's own sentence to both files.
    ('G-F2-DIGEST-QUOTES-SECTION', 'the digest against the section and the fold bank',
     lambda S: (S['fold']['one'][:80] in S['findings'] and S['fold']['one'][:80] in S['digest']
                and 'filed b474' in S['digest']),
     lambda S: put(S, 'digest', S['digest'].replace(S['fold']['one'][:80], 'a summary in its place'))),
    ('G-F2-DIGEST-ADDITIVE', 'the digest`s own markers',
     lambda S: S['digest'].count('<!-- b474 orientation refresh') == 1
     and S['digest'].count('Orientation refresh') >= 6,
     lambda S: put(S, 'digest', S['digest'] + '<!-- b474 orientation refresh: the external-reading arc -->')),

    ('G-F3-LANE-ENTERED', 'OPEN_TRAILS.md and the lane bank',
     lambda S: S['ot'].count('<!-- b474 (R84): the compression register entered as a research lane -->') == 1
     and 'compression register' in S['lane'] and 'compression register' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('<!-- b474 (R84): the compression register entered as a research lane -->', ''))),
    ('G-F3-FALSIFIERS-AND-CONTROL', 'the lane entry`s own text',
     lambda S: 'Epstein' in S['lane'] and 'control' in S['lane'] and 'falsifiers' in S['lane'],
     lambda S: cut(S, 'lane', 'Epstein')),
    ('G-F3-NO-NUMBER-COMPUTED', 'the lane entry and this act`s own tools',
     lambda S: ('computes no form' in S['lane'] and 'evaluates no signature' in S['lane']
                and not re.search(r'\bmpmath\b|\bnumpy\b|\bscipy\b', S['tools474'])),
     lambda S: put(S, 'tools474', S['tools474'] + NL + 'import numpy')),

    ('G-NOEXPECTATIONS', 'the scores bank and the face',
     lambda S: '"registered": 0' in S['scores'] and 'NONE. THE ORDER REGISTERS NO EXPECTATION' in S['face'],
     lambda S: put(S, 'scores', S['scores'].replace('"registered": 0', '"registered": 3'))),
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'], lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE-THREE-FILES', 'the commit file list',
     lambda S: sorted(S['tracked']) == sorted(['OPEN_TRAILS.md', 'FINDINGS.md',
                                               'phase2/method/THE_FINDINGS_AS_THEY_STAND.md']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b474 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b474 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 323 |' in S['corr'], lambda S: cut(S, 'corr', '| 323 |')),
    ('G-WRITELIST-KINDS', 'every b474 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'FINDINGS', 'phase2/', 'data/', 'tools/')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite own text',
     lambda S: 'def line_with(text, needle)' in S['suite'], lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
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
     lambda S: "data/b474_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b474_components.txt' in gits(ROOT, 'show'")),
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
    # ### ### **THE CARRIED PUSH PREDICATE READ THIS ACT AS ALREADY PUSHED.** ### Its two clauses --
    # ### origin/main == HEAD, and the last subject starting with this act's number -- were BOTH true
    # ### before the act ran, because THE REFUSED ISSUE OF b474 HAD ITS OWN COMMIT ON main. ### So the
    # ### post-push arms ran pre-push and failed on banks that do not exist yet. ### **A THIRD CLAUSE
    # ### IS ADDED: the pushed commit must carry this act's own components bank.**
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b474')
              and 'data/b474_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b474 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b474_checks_postpush.txt' if pushed else 'b474_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b474_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
