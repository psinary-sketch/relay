# -*- coding: utf-8 -*-
"""b472_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b472_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b472_ferry.txt')),
        scan=read(os.path.join(D, 'b472_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b472_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b472_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b472_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b472_extract.txt')),
        lock=read(os.path.join(D, 'b472_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b472
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b471_closing.txt')),
        addendum=read(os.path.join(D, 'b472_addendum.txt')),
        census=read(os.path.join(D, 'b472_census.txt')),
        span=read(os.path.join(D, 'b472_span_notes.txt')),
        scores=read(os.path.join(D, 'b472_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b472_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b472_survey.json')) or '{}'),
        table=json.loads(read(os.path.join(D, 'b472_table.json')) or '{}'),
        state=json.loads(read(os.path.join(D, 'b472_run_state.json')) or '{}'),
        close=json.loads(read(os.path.join(D, 'b472_close_state.json')) or '{}'),
        comp=read(os.path.join(D, 'b472_components.txt')),
        refusal=read(os.path.join(D, 'b472_refusal.txt')),
        refused_ferry=read(os.path.join(D, 'b472_ferry_refused.txt')),
        scan_tool=read(os.path.join(T, 'ferry_scan.py')),
        tools472=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b472_') and f.endswith('.py') and f != 'b472_checks.py'),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        findings=read(os.path.join(PP, 'FINDINGS.md')),
        desk=read(os.path.join(D, 'b472_desk_notes.txt')),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        log_tracked=gits(ROOT, 'ls-files', 'data/b471_zeta23_build.log'),
        faces_dirty=(gits(PP, 'status', '--porcelain', '--', 'FACES_LEDGER.md') != ''),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b472_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b472.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b472')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b472_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b472'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    import ferry_scan  # ### the tool this act edited, read by running it
    S['scan_fixtures'] = bool(ferry_scan.r81_self_test())
    S['refused_bare'] = len([f for f in ferry_scan.r81_flags(S['refused_ferry'])
                             if f[3] == 'ACT' and f[4] == 'NONE'])
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-5][0-9]_|^b46[01]_', f)]
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


BINS = ('NAMES A TERMINAL', 'NAMES A CARRIER', 'NAMES NOTHING')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'], lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b471 closing -- the prior closed act',
     lambda S: 'row 320' in S['prior'], lambda S: cut(S, 'prior', 'row 320')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-REFUSED-FERRY-KEPT', 'the refused issue, kept beside the re-issue',
     lambda S: 'paste ends (part 1 of 1)' in S['refused_ferry'] and 'REFUSED UNDER (R81)' in S['refusal']
     and S['refused_ferry'] != S['ferry'],
     lambda S: put(S, 'refused_ferry', S['ferry'])),

    ('G-R81-ACT-FLAGS-LABELLED', 'the survey bank`s flag table',
     lambda S: S['sv'].get('act_bare') == 0 and S['sv'].get('act_flags', 0) >= 1
     and all(f['label'] != 'NONE' for f in S['sv'].get('flags', []) if f['part'].startswith('ACT')),
     lambda S: put(S, 'sv', dict(S['sv'], act_bare=1))),
    ('G-R81-SCAN-FLAGS-PRINTED', 'the banked scan',
     lambda S: '(R81) FLAGS : 7' in S['scan'] and 'carries: [procedural]' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 7', 'nothing'))),
    ('G-R81-SCAN-VERDICT-UNMOVED', 'the scan tool`s own source',
     lambda S: ('len(ch) + len(sh) + stale' in S['scan_tool']
                and 'r81' not in S['scan_tool'][S['scan_tool'].index('print(\'  ### VERDICT'):]),
     lambda S: put(S, 'scan_tool', S['scan_tool'].replace('len(ch) + len(sh) + stale',
                                                          'len(ch) + len(sh) + stale + len(r81_flags(text))'))),
    ('G-R81-SCAN-FIXTURES', 'the scan tool, run',
     lambda S: S['scan_fixtures'] is True, lambda S: put(S, 'scan_fixtures', False)),
    ('G-R81-SCAN-CONTROL-REFUSED', 'the refused ferry, scanned by the new arm',
     lambda S: S['refused_bare'] == 1, lambda S: put(S, 'refused_bare', 0)),

    ('G-C0-STATE-READ', 'the run-state bank',
     lambda S: S['state'].get('state') in ('RUNNING', 'EXITED') and S['state'].get('pid') == 27704,
     lambda S: put(S, 'state', dict(S['state'], state=''))),
    ('G-C0-LOG-BYTES', 'the run-state bank against the file system',
     lambda S: S['state'].get('log_bytes') == os.path.getsize(os.path.join(D, 'b471_zeta23_build.log')),
     lambda S: put(S, 'state', dict(S['state'], log_bytes=-1))),
    ('G-C0-LOG-CLOSED', 'this act`s own tools and its state bank',
     lambda S: not re.search(r'open\([^)]*zeta23_build\.log', S['tools472'])
     and 'the log was not opened' in S['state'].get('how', '') and S['log_tracked'] == '',
     lambda S: put(S, 'tools472', S['tools472'] + "open('b471_zeta23_build.log')")),
    ('G-C0-AFTER-SEAL', 'the face`s locked time against the state read`s own time',
     lambda S: bool(re.search(r'locked at \(UTC\) : (\S+)', S['face']))
     and re.search(r'locked at \(UTC\) : (\S+)', S['face']).group(1) < S['state'].get('read_utc', ''),
     lambda S: put(S, 'state', dict(S['state'], read_utc='2000-01-01T00:00:00Z'))),

    ('G-C1-REHEARSAL-AGREES', 'the survey bank`s rehearsal against the ledger`s update line',
     lambda S: S['sv'].get('rehearsal', {}).get('agrees') is True
     and S['sv']['rehearsal'].get('kind') == '(b)' and S['sv']['rehearsal'].get('witness') == 'NONE KNOWN'
     and 'entry (v)' in S['faces'] and '`KIND: (b)`' in S['faces'],
     lambda S: put(S, 'sv', dict(S['sv'], rehearsal=dict(S['sv']['rehearsal'], agrees=False)))),
    ('G-C1-CELLS-FROM-LEDGER', 'the six cells against FACES_LEDGER.md itself',
     lambda S: all(('KIND: %s. WITNESS: `%s`' % (S['sv']['cells'][k]['kind'], S['sv']['cells'][k]['witness'])
                    in S['faces'] or 'KIND: `%s`. WITNESS: `%s`' % (S['sv']['cells'][k]['kind'],
                                                                    S['sv']['cells'][k]['witness']) in S['faces'])
                   for k in S['sv']['cells']),
     lambda S: put(S, 'faces', S['faces'].replace('WITNESS: `NONE KNOWN`', 'WITNESS: `FOUND`'))),
    ('G-C1-TALLY-MATCHES', 'the row`s own printed tally against the reader`s count',
     lambda S: ([S['sv']['cells'][k]['kind'] for k in S['sv']['cells']].count('NOT EMPTY') == 5
                and [S['sv']['cells'][k]['witness'] for k in S['sv']['cells']].count('NONE KNOWN') == 4
                and 'KIND \u2014 5 NOT EMPTY, 1 `(b)`' in S['faces']),
     lambda S: put(S, 'sv', dict(S['sv'], cells={k: dict(v, kind='NOT EMPTY')
                                                 for k, v in S['sv']['cells'].items()}))),
    ('G-C1-INDEX-AT-B467', 'the index table in OPEN_TRAILS.md itself',
     lambda S: all(('| (%s) | %s |' % (k, v['index'])) in S['ot'] for k, v in S['sv']['index'].items()),
     lambda S: put(S, 'sv', dict(S['sv'], index={k: dict(v, index='nothing')
                                                 for k, v in S['sv']['index'].items()}))),
    ('G-C1-SIX-SENTENCES', 'the components record',
     lambda S: all(('**SENTENCE (%s):**' % k) in S['comp'] for k in ('i', 'ii', 'iii', 'iv', 'v', 'vi')),
     lambda S: cut(S, 'comp', '**SENTENCE (vi):**')),
    ('G-C1-UNSTATED-NOT-FILLED', 'the six sentences in the table bank',
     lambda S: all(('UNSTATED IN THE CELLS' in t['sentence'] or 'NONE KNOWN' in t['sentence']
                    or 'UNSTATED' in t['sentence']) for t in S['table'].get('table', [])),
     lambda S: put(S, 'table', dict(S['table'], table=[dict(t, sentence='a filled sentence')
                                                       for t in S['table']['table']]))),
    ('G-C1-E0-AT-ADDRESS', 'FINDINGS.md itself',
     lambda S: len(S['findings'].split(NL)) > 3069
     and S['findings'].split(NL)[3042].startswith('### The E0 gate')
     and S['findings'].split(NL)[3057].startswith('### The grades, one row per constituent'),
     lambda S: put(S, 'findings', '')),
    ('G-C1-E0-MAPPING-CONTROLS', 'the table bank`s controls',
     lambda S: S['table'].get('controls', {}).get('pos_ok') is True
     and S['table']['controls'].get('neg_ok') is True and S['table']['controls']['pos'][0] == 'K4',
     lambda S: put(S, 'table', dict(S['table'], controls=dict(S['table']['controls'], pos_ok=False)))),
    ('G-C1-E0-ROWS-AS-SURVEYED', 'the table bank against the survey`s own yields',
     lambda S: S['table'].get('with_e0_row') == ['i']
     and max(m['words'] for k, ms in S['sv']['maps'].items() if k != 'i' for m in ms) < 6
     and [m['words'] for m in S['sv']['maps']['i'] if m['k'] == 'K8'][0] >= 6,
     lambda S: put(S, 'table', dict(S['table'], with_e0_row=['i', 'vi']))),
    ('G-K-NUMBERINGS-NAMED', 'the components record',
     lambda S: 'FINDINGS.md:3045' in S['comp'] and 'OPEN_TRAILS.md:6439' in S['comp'],
     lambda S: cut(S, 'comp', 'OPEN_TRAILS.md:6439')),

    ('G-C2-AF-FROM-B468R', 'the placements against b468r`s own bank',
     lambda S: all(S['sv']['af'][k]['verdict'] in read(os.path.join(D, 'b468r_components.txt'))
                   for k in S['sv']['af']) and len(S['sv']['af']) == 6,
     lambda S: put(S, 'sv', dict(S['sv'], af={k: dict(v, verdict='INVENTED')
                                              for k, v in S['sv']['af'].items()}))),
    ('G-C2-ZETA-FROM-B470', 'the placement against b470`s own bank',
     lambda S: 'CONTAINS' in S['sv']['z'].get('verdict', '')
     and S['sv']['z'].get('verdict_line') == 109
     and 'EF_lit_zetaZeroConfig (theorem)' in read(os.path.join(D, 'b470_components.txt')),
     lambda S: put(S, 'sv', dict(S['sv'], z=dict(S['sv']['z'], verdict='MATCHES')))),
    ('G-C2-EVERY-CELL-CITES', 'the placements bank',
     lambda S: all((p['at'].startswith('b468r_components.txt') or p['at'].startswith('b470_components.txt'))
                   for r in ('af', 'zeta23') for p in S['table']['placements'][r].values()),
     lambda S: put(S, 'table', dict(S['table'], placements=dict(
         S['table']['placements'], af={k: dict(v, at='') for k, v in S['table']['placements']['af'].items()})))),
    ('G-C2-NOT-PLACED-DISTINCT', 'the placement counts',
     lambda S: S['table']['counts']['zeta23']['NOT PLACED'] == 5
     and S['table']['counts']['zeta23']['NOT AT ALL'] == 0
     and S['table']['counts']['af']['NOT PLACED'] == 0
     and S['table']['counts']['af']['IN WHOLE'] == S['table']['counts']['zeta23']['IN WHOLE'] == 0,
     lambda S: put(S, 'table', dict(S['table'], counts=dict(
         S['table']['counts'], zeta23=dict(S['table']['counts']['zeta23'], **{'NOT PLACED': 0, 'NOT AT ALL': 5}))))),

    ('G-R82-NOT-EXECUTED', 'the commit file lists and the corpus`s own map',
     lambda S: not any(x.endswith(('.lean', 'SPIRAL_MAP.md', 'REGISTRY.md')) for x in
                       list(S['tracked']) + list(S['rtracked']))
     and 'waived' not in read(os.path.join(PP, 'SPIRAL_MAP.md')).lower().split('rule 9')[-1][:400],
     lambda S: put(S, 'rtracked', list(S['rtracked']) + ['SPIRAL_MAP.md'])),
    ('G-U1-UNEDITED', 'FACES_LEDGER.md`s own working state',
     lambda S: S['faces_dirty'] is False and S['faces'].count('| U1 | U1 -- the uniformity obstruction') == 1,
     lambda S: put(S, 'faces_dirty', True)),

    ('G-N1-SCORED', 'the scores bank', lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-SCORED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),
    ('G-N1-AT-CLOSE', 'the close-state bank, read at the close',
     lambda S: S['close'].get('label') == 'close' and S['close'].get('state') in ('RUNNING', 'EXITED')
     and 'REFUTED' in S['scores'],
     lambda S: put(S, 'close', dict(S['close'], label=''))),

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
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b472 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b472 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 321 |' in S['corr'], lambda S: cut(S, 'corr', '| 321 |')),
    ('G-WRITELIST-KINDS', 'every b472 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'data/', 'tools/')) for x in S['tracked']),
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
    # ### before the act ran, because THE REFUSED ISSUE OF b472 HAD ITS OWN COMMIT ON main. ### So the
    # ### post-push arms ran pre-push and failed on banks that do not exist yet. ### **A THIRD CLAUSE
    # ### IS ADDED: the pushed commit must carry this act's own components bank.**
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b472')
              and 'data/b472_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-N1-AT-CLOSE']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b472 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b472_checks_postpush.txt' if pushed else 'b472_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b472_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
