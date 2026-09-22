# -*- coding: utf-8 -*-
"""b483_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b483_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b483_ferry.txt')),
        scan=read(os.path.join(D, 'b483_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b483_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b483_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b483_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b483_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b483_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR CLOSED ACT IS b481** -- b482 is banked and unrun, b479 registered and unrun.
        prior=read(os.path.join(D, 'b481_closing.txt')),
        addendum=read(os.path.join(D, 'b483_addendum.txt')),
        comp=read(os.path.join(D, 'b483_components.txt')),
        desk=read(os.path.join(D, 'b483_desk_notes.txt')),
        span=read(os.path.join(D, 'b483_span_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b483_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b483_survey.json')) or '{}'),
        log=read(os.path.join(D, 'b477_gram.log')),
        b476face=read(os.path.join(D, 'b476_registration_2026-09-22.txt')),
        b446=read(os.path.join(D, 'b446_closing.txt')),
        entries=read(os.path.join(D, 'b477_entries.jsonl')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b483_checks.py')),
        tools483=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b483_') and f.endswith('.py') and f != 'b483_checks.py'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b483.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b483 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b483_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b483 --'):
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
             if re.match(r'^b4[0-7][0-9]_|^b48[012]_', f) and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'].get('scores') or {}).get(k, {}).get('verdict', '')


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
    ('G-PRIOR-CLOSED-PUSHED', 'b481`s closing AND the ledger -- each for what it actually holds',
     # ### **THE FIRST VERSION ASKED b481`S CLOSING FOR ITS ROW NUMBER, WHICH IT DOES NOT CARRY**
     # ### -- the row id lives in the DESK bank and in the ledger. ### Re-pointed at the two banks
     # ### that hold the two halves: the closing proves the act closed, the ledger proves the row.
     lambda S: ('THE COMMITS, EACH READ BACK BY ls-remote' in S['prior']
                and S['corr'].count('| 329 |') == 1),
     lambda S: cut(S, 'prior', 'THE COMMITS, EACH READ BACK BY ls-remote')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory`s own banked ferries',
     lambda S: (os.path.exists(os.path.join(D, 'b479_ferry.txt'))
                or os.path.exists(os.path.join(D, 'b482_ferry.txt')))
     and not os.path.exists(os.path.join(D, 'b482_registration_2026-09-22.txt'))
     and 'b483' in S['face'],
     lambda S: cut(S, 'face', 'b483')),

    # -------------------------------------------------- the run, read from its own log
    ('G-RUN-COMPLETE-FROM-LOG', 'b477`s log itself',
     lambda S: 'RUN COMPLETE' in S['log'] and S['sv']['complete'] is True,
     lambda S: put(S, 'log', S['log'].replace('RUN COMPLETE', 'x'))),
    ('G-EXIT-ZERO-FROM-LAUNCHER', 'b477`s log itself',
     lambda S: '=== EXIT 0 : b477_gram.py' in S['log'] and S['sv']['exit0'] is True,
     lambda S: put(S, 'sv', dict(S['sv'], exit0=False))),
    ('G-STAMPS-DISTINCT', 'b477`s log against b475`s defect',
     lambda S: len(set(re.findall(r'^\[(\d\d:\d\d:\d\d)\]', S['log'], re.M))) > 100,
     lambda S: put(S, 'log', re.sub(r'^\[\d\d:\d\d:\d\d\]', '[21:15:02]', S['log'], flags=re.M))),
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools483'],
     lambda S: put(S, 'tools483', S['tools483'] + NL + "read(D + 'b475_zeta23_build.log')")),
    ('G-NO-CHAIN-RUN', 'this act`s own tools, for an IMPORT or a CALL and not for a mention',
     lambda S: not re.search(r'^\s*(?:import|from)\s+(?:b321_window|b325_epstein|b317_smear|'
                            r'b318_square|carto_atlas)\b'
                            r'|\b(?:channels_q|mean_zero_variant|autocorrelation|trunc_bound)\s*\(',
                            S['tools483'], re.M),
     lambda S: put(S, 'tools483', S['tools483'] + NL + 'import b321_window as WI')),

    # -------------------------------------------------- component 1
    ('G-C1-TWO-FAMILIES-NOT-ONE', 'the survey bank against the log`s own header',
     lambda S: (S['sv']['aim'] == 13 and S['sv']['ladder'] == 22
                and 'aim-plane cells 13 ; ladder cells 22' in S['log']),
     lambda S: put(S, 'sv', dict(S['sv'], aim=35, ladder=0))),
    ('G-C1-ENTRY-COUNT-CLOSES', 'the survey bank`s own arithmetic',
     lambda S: (S['sv']['kinds']['offdiagonal']
                == S['sv']['aim'] * (S['sv']['aim'] - 1) // 2
                + S['sv']['ladder'] * (S['sv']['ladder'] - 1) // 2),
     lambda S: put(S, 'sv', dict(S['sv'], kinds=dict(S['sv']['kinds'], offdiagonal=300)))),
    ('G-C1-NO-ENTRY-INVENTED', 'the components record',
     lambda S: ('entries the bank does not hold : 0' in S['comp']
                and 'NONE IS INTERPOLATED' in S['comp']),
     lambda S: put(S, 'comp', S['comp'].replace('entries the bank does not hold : 0',
                                                'entries the bank does not hold : 4'))),
    ('G-C1-RESIDUAL-BESIDE-EVERY-EIGENVALUE', 'the components record`s own columns',
     lambda S: S['comp'].count('max resid') >= 4 and 'e-1' in S['comp'],
     lambda S: put(S, 'comp', S['comp'].replace('max resid', 'x'))),
    ('G-C1-BOTH-ENDS-PRINTED', 'the components record`s own columns',
     lambda S: 'lam_min(-G)' in S['comp'] and 'lam_max(-G)' in S['comp']
     and 'lam_max(G)' in S['comp'],
     lambda S: put(S, 'comp', S['comp'].replace('lam_max(-G)', 'x'))),

    # -------------------------------------------------- component 2
    ('G-C2-DIAGONAL-GATE-PASSED', 'the survey bank against the entry file itself',
     lambda S: (S['sv']['diag_all_ok'] is True and S['sv']['max_abs_diff'] == 0.0
                and S['sv']['diag_checked'] == 32 and '"ok": true' in S['entries']),
     lambda S: put(S, 'sv', dict(S['sv'], diag_all_ok=False))),
    ('G-C2-ZEROSIDE-RELATIVE', 'the survey bank against the face',
     lambda S: (S['sv']['max_zero_resid'] > S['sv']['max_trunc'] * 1e3
                and '3.558e-05' in S['face']),
     lambda S: put(S, 'sv', dict(S['sv'], max_zero_resid=1e-13))),
    ('G-C2-TRUNCBOUND-NOT-THE-AGREEMENT', 'the components record and the survey bank',
     lambda S: ('bounds the truncation of the zero SUM' in S['comp']
                and S['sv']['max_zero_resid'] > S['sv']['max_trunc']),
     lambda S: cut(S, 'comp', 'bounds the truncation of the zero SUM')),
    ('G-C2-THRESHOLD-FIXED-BEFORE-SPECTRUM', 'the SEALED face, whose bytes are hashed',
     lambda S: ('THIS IS STATED BEFORE ANY EIGENVALUE EXISTS' in S['face']
                and 'no threshold is chosen after seeing a spectrum' in S['face']),
     lambda S: cut(S, 'face', 'THIS IS STATED BEFORE ANY EIGENVALUE EXISTS')),
    ('G-C2-ORIENTATION-FROM-R87', 'b476`s appended amendment against the components record',
     lambda S: ('(N2) AND (N3) REFER TO THE LARGEST EIGENVALUE OF `G`' in S['b476face']
                and 'THE SIGNATURE IS' in S['comp'] and '-G' in S['comp']),
     lambda S: cut(S, 'b476face', '(N2) AND (N3) REFER TO THE LARGEST EIGENVALUE OF `G`')),

    # -------------------------------------------------- component 3
    ('G-C3-CONTROL-SCOPED-TO-PLACES', 'the components record',
     lambda S: ('PLACES SIDE ONLY' in S['comp'] and 'NO ZERO SIDE' in S['comp']),
     lambda S: cut(S, 'comp', 'NO ZERO SIDE')),
    ('G-C3-RESOLUTION-STATED', 'the scores bank against the components record',
     lambda S: ('%.3e' % S['sc']['resolution']) in S['comp'] and S['sc']['resolution'] > 1e-6,
     lambda S: put(S, 'sc', dict(S['sc'], resolution=1e-30))),

    # -------------------------------------------------- the six
    ('G-F1-SCORED', 'the scores bank against the components record',
     lambda S: sc(S, 'F1') == 'FIRES' and 'CANNOT BE INDEFINITE WHATEVER ITS ENTRY IS' in S['comp'],
     lambda S: cut(S, 'comp', 'CANNOT BE INDEFINITE WHATEVER ITS ENTRY IS')),
    ('G-F2-SCORED', 'the scores bank against the components record',
     lambda S: (sc(S, 'F2') == 'THRESHOLD-DEPENDENT'
                and S['sc']['scores']['F2']['flips'] is True
                and 'FIRES ON SOME THRESHOLDS AND NOT OTHERS' in S['comp']),
     lambda S: put(S, 'sc', dict(S['sc'], scores=dict(S['sc']['scores'],
                                                      F2=dict(S['sc']['scores']['F2'], flips=False))))),
    ('G-F3-SCORED', 'the scores bank against the components record',
     lambda S: (sc(S, 'F3') == 'NOT MET'
                and S['sc']['scores']['F3']['control_at_priced'] is False
                and 'TAKES NO GRADE FROM THIS' in S['comp']),
     lambda S: cut(S, 'comp', 'TAKES NO GRADE FROM THIS')),
    ('G-N1-SCORED', 'the scores bank against the components record',
     lambda S: (sc(S, 'N1') == 'REFUTED'
                and S['sc']['scores']['N1']['first']['AIM PLANE'] is None
                and 'NEVER INDEFINITE' in S['comp']),
     lambda S: put(S, 'sc', dict(S['sc'], scores=dict(
         S['sc']['scores'], N1=dict(S['sc']['scores']['N1'],
                                    first={'AIM PLANE': 3, 'LADDER': 16}))))),
    ('G-N2-SCORED', 'the scores bank against the components record',
     lambda S: ('HELD at the observed resolution' in sc(S, 'N2')
                and 'REFUTED at the tail figure' in sc(S, 'N2')
                and 'HAD IT' in S['comp'] and 'BACKWARDS' in S['comp']),
     lambda S: cut(S, 'comp', 'BACKWARDS')),
    ('G-N3-SCORED', 'the scores bank against b446`s own bank',
     lambda S: (sc(S, 'N3') == 'REFUTED'
                and 'THE OUTLIER 4.123106' in S['b446']
                and '4.123106' in S['comp']),
     lambda S: cut(S, 'b446', 'THE OUTLIER 4.123106')),
    ('G-VACUOUS-SAID-IF-VACUOUS', 'the scores bank against the components record',
     lambda S: ('VACUOUS' in sc(S, 'N3')) == bool(re.search(r'\(N3\) VACUOUS', S['comp'])),
     lambda S: put(S, 'sc', dict(S['sc'], scores=dict(
         S['sc']['scores'], N3=dict(S['sc']['scores']['N3'], verdict='VACUOUS'))))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the desk bank against the face',
     lambda S: ('THE SEAT`S OWN' in S['face'].replace("'", '`')
                and all(('(%s)' % k) in S['desk'] for k in ('F1', 'F2', 'F3', 'N1', 'N2', 'N3'))),
     lambda S: cut(S, 'desk', '(F2)')),
    ('G-NOGRADE-ABOVE-MEASURED', 'the components record and the desk bank',
     lambda S: ('NOT `MEASURED`' in S['comp'] and 'NO GRADE' in S['desk']
                and 'DERIVES' not in S['comp'] and 'PROVED' not in S['comp']),
     lambda S: put(S, 'comp', S['comp'] + NL + 'the register is graded PROVED')),

    # -------------------------------------------------- the standing arms
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md', 'FINDINGS.md'))
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
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b483 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b483 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 330 |' in S['corr'] and S['corr'].count('| 330 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 330 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b483 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'data/', 'tools/')) for x in S['tracked']),
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
     lambda S: "data/b483_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b483_components.txt' in gits(ROOT, 'show'")),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b483')
              and 'data/b483_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b483 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b483_checks_postpush.txt' if pushed else 'b483_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b483_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
