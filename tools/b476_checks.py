# -*- coding: utf-8 -*-
"""b476_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb, honoured in
### advance even though this act is not the one it binds.
"""
import io
import glob
import fnmatch
import b476_extract as X478
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
FACE = os.path.join(D, 'b476_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b476_ferry.txt')),
        scan=read(os.path.join(D, 'b476_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b476_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b476_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b476_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b476_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b476_lockgate_notes*.txt')))[-1]),
        lock_runs=len(glob.glob(os.path.join(D, 'b476_lockgate_notes*.txt'))),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b476
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b478_closing.txt')),
        addendum=read(os.path.join(D, 'b476_addendum.txt')),
        census=read(os.path.join(D, 'b476_census.txt')),
        span=read(os.path.join(D, 'b476_span_notes.txt')),
        scores=read(os.path.join(D, 'b476_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b476_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b476_survey.json')) or '{}'),
        reg=json.loads(read(os.path.join(D, 'b476_registered.json')) or '{}'),
        comp=read(os.path.join(D, 'b476_components.txt')),
        refused=read(os.path.join(D, 'b476_ferry_refused.txt')),
        chain=read(os.path.join(T, 'b321_window.py')),
        extract_src=read(os.path.join(T, 'b476_extract.py')),
        tools476=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b476_') and f.endswith('.py') and f != 'b476_checks.py'),
        rows321=json.loads(read(os.path.join(D, 'b321_rows.json')) or '{}'),
        offline=read(os.path.join(D, 'b326_offline.json')),
        voros=read(os.path.join(D, 'b324_reread_run.txt')),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        desk=read(os.path.join(D, 'b476_desk_notes.txt')),
        gramfiles=[f for f in os.listdir(D) if re.search(r'(^|[_-])gram', f.lower())],
        docs=sorted(f for f in os.listdir(D) if f.startswith('b476_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b476.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b476 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b476_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b476 --'):
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

def globs_of(face):
    """### (R85): THE FACE'S (W) SECTION AS A LIST OF GLOBS. ### Every backticked path in the write-list
    ### table is a pattern; a written file matches if its basename matches any pattern's basename."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    # ### ### **THE FIRST READER DROPPED THE TOOL NAMES AND THEN FAILED ON THEM.** ### It filtered out
    # ### `*.py` entries as "the left column", but a tool file this act creates is itself a written file,
    # ### and (R85) has the face carry each tool's NAME beside its globs. ### Every backticked path in
    # ### the (W) table is a pattern, tool names included.
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'], lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
    ('G-SUBSTITUTION-APPLIED', 'the banked ferry against the refused text',
     lambda S: ('earliest negative excursion' in S['ferry'] and 'first negative excursion' not in S['ferry']
                and 'first negative excursion' in S['refused']),
     lambda S: put(S, 'ferry', S['ferry'].replace('earliest negative', 'first negative'))),
    ('G-REFUSED-TEXT-KEPT', 'the refused ferry, kept whole beside the re-issue',
     lambda S: 'paste ends (part 1 of 1)' in S['refused'] and S['refused'] != S['ferry'],
     lambda S: put(S, 'refused', S['ferry'])),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b478 closing -- the prior closed act',
     lambda S: 'row 325' in S['prior'], lambda S: cut(S, 'prior', 'row 325')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),

    ('G-E1-FAMILY-FROM-BANK', 'the survey bank against b321`s own rows',
     lambda S: (len(S['reg']['cells']) == len(S['rows321']['c2']) == 13
                and len(S['reg']['ladder']) == 22),
     lambda S: put(S, 'reg', dict(S['reg'], cells=S['reg']['cells'][:5]))),
    ('G-E1-ONE-CONSTRUCTION', 'the chain`s own source and this act`s record',
     lambda S: 'mean_zero_variant' in S['comp'] and 'autocorrelation' in S['comp']
     and 'mean_zero_variant' in S['extract_src'],
     lambda S: cut(S, 'comp', 'mean_zero_variant')),
    ('G-E1-RADII-DISJOINT', 'the two radius sets in the survey bank',
     lambda S: not (set(S['reg']['cells']) & set(S['reg']['ladder'])),
     lambda S: put(S, 'reg', dict(S['reg'], ladder=S['reg']['ladder'] + [S['reg']['cells'][0]]))),
    ('G-E1-SUPPORT-SAID-TWICE', 'the components record',
     lambda S: 'a^-1, a' in S['comp'].replace('[', '').replace(']', '')
     or ('p^k <= a' in S['comp'] and 'p^k <= a^2' in S['comp']),
     lambda S: put(S, 'comp', S['comp'].replace('p^k <= a^2', 'x'))),
    ('G-E2-CHAIN-UNEDITED', 'b321_window.py`s own working state',
     lambda S: (gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py') == ''
                and 'def channels(v, w)' in S['chain']),
     lambda S: put(S, 'chain', '')),
    ('G-E3-DIAGONAL-REHEARSED', 'the survey bank`s rehearsal',
     lambda S: S['reg']['rehearsal']['a'] == 1.5 and S['reg']['rehearsal']['banked'] is not None,
     lambda S: put(S, 'reg', dict(S['reg'], rehearsal=dict(S['reg']['rehearsal'], banked=None)))),
    ('G-E3-DIAGONAL-EXACT', 'the rehearsal against b321`s banked total',
     lambda S: (S['reg']['rehearsal']['within'] is True
                and abs(S['reg']['rehearsal']['diag']
                        - S['rows321']['totals']['1.5']) < S['reg']['rehearsal']['floor']),
     lambda S: put(S, 'reg', dict(S['reg'], rehearsal=dict(S['reg']['rehearsal'], diag=0.0, within=False)))),
    ('G-E4-TRUNCATION-FROM-ATLAS', 'the survey bank and the components record',
     lambda S: S['reg']['truncation']['ordinates'] == 10000 and 'Loewner' in S['comp'],
     lambda S: put(S, 'reg', dict(S['reg'], truncation=dict(S['reg']['truncation'], ordinates=0)))),
    ('G-E5-CONTROL-HEIGHT-CHECKED', 'the census bank itself',
     # ### The first form looked for `16.290216` inside a bank that stores `16.290215720390393`.
     # ### A rounded string is not a substring of a full-precision one: the arm now PARSES the
     # ### bank and compares numbers to the same tolerance the rounding implies.
     lambda S: (len(S['reg']['control']['heights']) == 17
                and any(abs(h - S['reg']['control']['lowest']) < 5e-7
                        for h in re.findall(r'\d+\.\d+', S['offline'])[:0]
                        or [float(x) for x in re.findall(r'(\d{2}\.\d{6,})', S['offline'])])),
     lambda S: put(S, 'reg', dict(S['reg'], control=dict(S['reg']['control'], lowest=176.70)))),
    ('G-E5-ORDER-HEIGHT-ABSENT', 'the census bank and the components record',
     lambda S: (S['reg']['control']['order_height_in_bank'] is False
                and '176.70' not in S['offline'] and '176.70' in S['comp']),
     lambda S: put(S, 'reg', dict(S['reg'], control=dict(S['reg']['control'], order_height_in_bank=True)))),
    ('G-E5-RESOLUTION-PRICED', 'the survey bank`s own rows',
     lambda S: (S['reg']['resolution']['resolving'] == len(S['reg']['resolution']['rows']) == 35
                and all(r['hhat'] > 1.49e-08 for r in S['reg']['resolution']['rows'])),
     lambda S: put(S, 'reg', dict(S['reg'], resolution=dict(S['reg']['resolution'], resolving=0)))),
    ('G-E5-VOROS-NOT-CARRIED', 'the Voros line itself and the face',
     lambda S: ('2T^2' in S['voros'] or '2T' in S['voros'])
     and 'DETECTION THRESHOLD IN THE LI REGISTER' in S['face'].upper()
     and 'trunc_bound' in S['face'],
     lambda S: cut(S, 'face', 'trunc_bound')),
    ('G-E6-THREE-FALSIFIERS', 'the components record',
     lambda S: all(x in S['comp'] for x in ('(F1) UNINFORMATIVE', '(F2) HALT', '(F3) MEASURED'))
     and 'NO HIGHER GRADE' in S['comp'].upper(),
     lambda S: cut(S, 'comp', '(F3) MEASURED')),
    ('G-E7-PRICE-FROM-TIMING', 'the survey bank`s own timing',
     lambda S: (S['reg']['price']['seconds_per_run'] > 0
                and S['reg']['price']['aim'] == 91 and S['reg']['price']['ladder'] == 253
                and S['reg']['price']['both'] == 630),
     lambda S: put(S, 'reg', dict(S['reg'], price=dict(S['reg']['price'], aim=0)))),
    ('G-E7-DETACH-REQUIRED', 'the price against the foreground limit, in the record',
     lambda S: (S['reg']['price']['aim'] * S['reg']['price']['seconds_per_run'] > 600
                and 'DETACHED UNDER (R80)' in S['comp']),
     lambda S: cut(S, 'comp', 'DETACHED UNDER (R80)')),
    ('G-NOGRAM-COMPUTED', 'the data directory and the registered bank',
     lambda S: S['reg']['gram_entries'] == 0 and not S['gramfiles'],
     lambda S: put(S, 'gramfiles', ['b476_gram.json'])),
    ('G-NOLANE-OPENED', 'the registered bank and the face',
     lambda S: S['reg']['lane_open'] is False and 'IT IS NOT OPEN NOW' in S['face'],
     lambda S: put(S, 'reg', dict(S['reg'], lane_open=True))),

    ('G-N1-REGISTERED', 'the scores bank', lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-REGISTERED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-REGISTERED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-STATED', 'the scores bank',
     lambda S: '"seat"' in S['scores'] and 'NOT PREDICTED' in S['scores'],
     lambda S: cut(S, 'scores', 'NOT PREDICTED')),

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
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b476 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b476 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 326 |' in S['corr'] and S['corr'].count('| 326 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 326 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b476 commit in three repositories, against (R85)`s GLOBS',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_no_glob_covers.zzz'})),
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
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b476_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b476_components.txt' in gits(ROOT, 'show'")),
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
    # ### before the act ran, because THE REFUSED ISSUE OF b476 HAD ITS OWN COMMIT ON main. ### So the
    # ### post-push arms ran pre-push and failed on banks that do not exist yet. ### **A THIRD CLAUSE
    # ### IS ADDED: the pushed commit must carry this act's own components bank.**
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b476')
              and 'data/b476_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b476 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b476_checks_postpush.txt' if pushed else 'b476_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b476_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
