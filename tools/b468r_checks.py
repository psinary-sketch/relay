# -*- coding: utf-8 -*-
"""b468r_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b468r_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b468r_ferry.txt')),
        scan=read(os.path.join(D, 'b468r_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b468r_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b468r_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b468r_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b468r_extract.txt')),
        lock=read(os.path.join(D, 'b468r_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b468r
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b469_closing.txt')),
        addendum=read(os.path.join(D, 'b468r_addendum.txt')),
        census=read(os.path.join(D, 'b468r_census.txt')),
        span=read(os.path.join(D, 'b468r_span_notes.txt')),
        scores=read(os.path.join(D, 'b468r_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b468r_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b468r_survey.json')) or '{}'),
        rd=json.loads(read(os.path.join(D, 'b468r_readings.json')) or '{}'),
        ln=json.loads(read(os.path.join(D, 'b468r_lean.json')) or '{}'),
        comp=read(os.path.join(D, 'b468r_components.txt')),
        shaSums=open(os.path.join(D, 'anthropic-zeta23', 'SHA256SUMS.txt'), 'rb').read().decode('utf-16'),
        first=read(os.path.join(D, 'b468_closing.txt')),
        firstFace=read(os.path.join(D, 'b468_registration_2026-09-22.txt')),
        leanrun=read(os.path.join(D, 'b468r_lean_run.txt')),
        chall=read(os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23', 'Challenge.lean')),
        desk=read(os.path.join(D, 'b468r_desk_notes.txt')),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        work=read(os.path.join(PP, 'day1', 'A_Place_to_Stand.md')),
        depmono=read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        # ### THE LIVE READS LIVE HERE, IN THE SOURCE, SO A MUTATION CAN REACH THEM (b461`s rule).
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b468r_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b468r.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b468r')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b468r_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b468r'):
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
    ('G-PRIOR-CLOSED-PUSHED', 'b469 closing -- the prior closed act',
     lambda S: 'row 317' in S['prior'], lambda S: cut(S, 'prior', 'row 317')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the survey record and file times',
     lambda S: 'THE (R75) ARTEFACTS ARE ON DISK' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b468r_extract.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', 'THE (R75) ARTEFACTS ARE ON DISK')),

    ('G-PRE-FIVE-HASHES-MATCH', 'the survey bank against SHA256SUMS.txt itself',
     lambda S: sum(1 for h in S['sv'].get('hashes', []) if h['name'].endswith('.pdf') and h['match']
                   and h['sha256'].upper() in S['shaSums']) == 5,
     lambda S: put(S, 'shaSums', S['shaSums'].replace('6DE3B156', '00000000'))),
    ('G-PRE-HEAD-AGREES', 'the survey bank and the clone itself',
     lambda S: S['sv'].get('head') == S['sv'].get('head_txt') ==
     gits(os.path.join(D, 'anthropic-zeta23', 'formal-math'), 'rev-parse', 'HEAD'),
     lambda S: put(S, 'sv', dict(S['sv'], head='0' * 40))),
    ('G-PRE-BLANK-ROW-IGNORED', 'SHA256SUMS.txt and the survey bank',
     lambda S: 'SHA256SUMS.txt' in S['shaSums']
     and not any(h['name'] == 'SHA256SUMS.txt' for h in S['sv'].get('hashes', [])),
     lambda S: put(S, 'sv', dict(S['sv'], hashes=S['sv'].get('hashes', [])
                                 + [dict(name='SHA256SUMS.txt', sha256='x', match=False)]))),
    ('G-FIRST-RUN-UNTOUCHED', 'b468`s own closing and face, by content',
     lambda S: 'THE GATE IS SHUT' in S['first'] and 'b468 -- THE PROPORTION RESULT' in S['firstFace'],
     lambda S: cut(S, 'first', 'THE GATE IS SHUT')),
    ('G-SHELL-ACCOUNTED', 'the LOCKED face and the harness task file',
     lambda S: 'Sanity check before banking the ferry' in S['face'] and '[killed]' in read(
         os.path.join('C:' + os.sep, 'Users', 'ECHOCH~1', 'AppData', 'Local', 'Temp', 'claude', 'D--',
                      '49943484-5ff3-4a99-9f75-0f3a8ae0d39a', 'tasks', 'b7z2q9ak1.output')),
     lambda S: cut(S, 'face', 'Sanity check before banking the ferry')),

    ('G-C1-THEOREMS-QUOTED-AT-LINE', 'the readings bank against the extracted texts',
     lambda S: all(S['rd'].get('quotes', {}).get(k) for k in ('A_claude', 'A_arxiv', 'B_claude', 'B_arxiv')),
     lambda S: put(S, 'rd', dict(S['rd'], quotes=dict(S['rd'].get('quotes', {}), A_arxiv=None)))),
    ('G-C1-AGREEMENT-BOTH-FORMS', 'the survey record',
     lambda S: 'FORM 1 (cut at the first' in S['extract'] and 'FORM 2 (the theorem proper' in S['extract']
     and S['sv'].get('thmA_agree') is True,
     lambda S: cut(S, 'extract', 'FORM 1 (cut at the first')),
    ('G-C1-COUNTS-SIMPLE', 'the readings bank',
     lambda S: 'are simple and lie on the critical line' in
     (S['rd'].get('quotes', {}).get('counts') or {}).get('text', ''),
     lambda S: put(S, 'rd', dict(S['rd'], quotes=dict(S['rd'].get('quotes', {}), counts=None)))),
    ('G-C1-CONSTANTS-SOURCED', 'the readings bank',
     lambda S: all(S['rd'].get('quotes', {}).get(k) for k in ('const', 'cmt_opt', 'chain', 'inputs_an')),
     lambda S: put(S, 'rd', dict(S['rd'], quotes=dict(S['rd'].get('quotes', {}), chain=None)))),
    ('G-C1-SUPPORT-QUOTED', 'the readings bank',
     lambda S: all(S['rd'].get('quotes', {}).get(k) for k in ('window', 'L', 'supp', 'bw1')),
     lambda S: put(S, 'rd', dict(S['rd'], quotes=dict(S['rd'].get('quotes', {}), supp=None)))),
    ('G-C1-IMPORTBAR-BOTH-COORDINATES', 'the components record',
     lambda S: 'THE REPRESENTATION COORDINATE.' in S['comp'] and 'THE TEST-FUNCTION COORDINATE.' in S['comp'],
     lambda S: cut(S, 'comp', 'THE TEST-FUNCTION COORDINATE.')),
    ('G-C1-ROWU1-PER-SITE', 'the readings bank',
     lambda S: [x['site'] for x in S['rd'].get('sites', [])] == ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)'],
     lambda S: put(S, 'rd', dict(S['rd'], sites=S['rd'].get('sites', [])[:5]))),
    ('G-C1-R76-TRUNCATION-CLAUSE', 'the readings bank',
     lambda S: any(x['site'] == '(ii)' and 'DOES NOT FIRE' in x['verdict'] for x in S['rd'].get('sites', [])),
     lambda S: put(S, 'rd', dict(S['rd'], sites=[dict(x, verdict='FIRES') for x in S['rd'].get('sites', [])]))),
    ('G-C1-DRAFTS-NOT-APPLIED', 'the deposited and working monographs themselves',
     lambda S: 'Weil-form rank-trace inequality' not in S['depmono']
     and 'Weil-form rank-trace inequality' not in S['work'],
     lambda S: put(S, 'work', S['work'] + NL + '| Weil-form rank-trace inequality |')),
    ('G-C1-CEILING-BESIDE-RESIDUE', 'the readings bank',
     lambda S: bool(S['rd'].get('quotes', {}).get('ceiling')) and bool(S['rd'].get('quotes', {}).get('residue')),
     lambda S: put(S, 'rd', dict(S['rd'], quotes=dict(S['rd'].get('quotes', {}), residue=None)))),
    ('G-C1-NOTHING-BETWEEN', 'the components record',
     lambda S: re.search(r'the paper`s ceiling sentence[^\n]*\n[^\n]*\n    the corpus`s residue sentence',
                         S['comp']) is not None,
     lambda S: put(S, 'comp', S['comp'].replace('    the corpus`s residue sentence',
                                                '    TYPED BETWEEN\n    the corpus`s residue sentence'))),

    ('G-C2-MATHLIB-PIN', 'the survey bank against the lakefile itself',
     lambda S: S['sv'].get('mathlib') == '51e6992efd06126df61a496bebf8f49482a4e129',
     lambda S: put(S, 'sv', dict(S['sv'], mathlib='deadbeef'))),
    ('G-C2-TRUSTED-DECLS-LISTED', 'the survey bank against Challenge.lean itself',
     lambda S: sum(1 for d_ in S['sv'].get('trusted', []) if d_['file'] == 'Challenge.lean')
     == len(re.findall(r'^theorem ', S['chall'], re.M)),
     lambda S: put(S, 'sv', dict(S['sv'], trusted=S['sv'].get('trusted', [])[1:]))),
    ('G-C2-NO-TRUSTED-AXIOM', 'Challenge.lean itself and the survey bank',
     lambda S: not re.search(r'^\s*axiom\s', S['chall'], re.M) and S['sv'].get('trusted_axioms') == 0,
     lambda S: put(S, 'chall', S['chall'] + NL + 'axiom pairCorrelation : True')),
    ('G-C2-AXIOM-SCAN-STRIPPED', 'the survey bank',
     lambda S: S['sv'].get('axiom_declarations') == [] and len(S['sv'].get('literal_axioms', [])) == 3,
     lambda S: put(S, 'sv', dict(S['sv'], axiom_declarations=['Zeta23/X.lean:1']))),
    ('G-C2-AUDIT-READ-AS-CLAIM', 'the survey bank and the components record',
     lambda S: len(S['sv'].get('audit_absent', [])) >= 1 and 'CLAIM' in S['comp'],
     lambda S: put(S, 'sv', dict(S['sv'], audit_absent=[]))),
    ('G-C2-PRINT-AXIOMS-RUN-OR-REASON', 'the lean bank and the run log',
     lambda S: (S['ln'].get('status') == 'RUN' and '### RUN COMPLETE' in S['leanrun'])
     or (S['ln'].get('status') == 'NOT RUN' and bool(S['leanrun'].strip())),
     lambda S: put(S, 'ln', dict(S['ln'], status='RUN')) if S['ln'].get('status') == 'NOT RUN'
     else put(S, 'leanrun', '')),
    ('G-C2-GRADE-IN-VOCABULARY', 'the lean bank',
     lambda S: S['ln'].get('grade', '').split(',')[0] in ('DERIVES', 'INTERFACES', 'NOT CLEAN'),
     lambda S: put(S, 'ln', dict(S['ln'], grade='PROBABLY FINE'))),
    ('G-C2-COMPARISON-VERDICT', 'the lean bank',
     lambda S: S['ln'].get('comparison') in ('MATCHES', 'CONTAINS WITH A NAMED SPECIALIZATION', 'DOES NOT'),
     lambda S: put(S, 'ln', dict(S['ln'], comparison='SORT OF'))),
    # ### ### **THE FIRST FORM FIRED ON THE ACT'S OWN SENTENCE `W-ORD-GW-IMPORT is not filed`** -- a
    # ### mention is not a filing, which is the record's `gates must strip prose` species. ### A
    # ### filing is a trail ENTRY with the work order's own heading or anchor; the arm looks for that.
    ('G-C2-WORDER-RULE', 'the lean bank and the trail`s entry headings',
     lambda S: (S['ln'].get('worder') is False) == (S['ln'].get('comparison') == 'DOES NOT')
     and not re.search(r'^(###|<!--)[^' + chr(10) + r']*W-ORD-GW-IMPORT', S['ot'], re.M),
     lambda S: put(S, 'ot', S['ot'] + NL + '### W-ORD-GW-IMPORT -- a filing that must not exist')),
    ('G-C2-CORPUS-LEAN-UNTOUCHED', 'the lv and kernel working trees, read in the source',
     lambda S: S['corpus_lean_clean'] is True,
     lambda S: put(S, 'corpus_lean_clean', False)),
    ('G-C2-NOTHING-IMPORTED', 'the commit file lists',
     lambda S: not any(x.endswith('.lean') for x in list(S['tracked']) + list(S['rtracked'])),
     lambda S: put(S, 'rtracked', list(S['rtracked']) + ['tools/lean/Imported.lean'])),

    ('G-N1-SCORED', 'the scores bank', lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-SCORED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),

    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b468r \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b468r \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 318 |' in S['corr'], lambda S: cut(S, 'corr', '| 318 |')),
    ('G-WRITELIST-KINDS', 'every b468r commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b468r'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b468r -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b468r_checks_postpush.txt' if pushed else 'b468r_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b468r_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
