# -*- coding: utf-8 -*-
"""b470_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b470_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b470_ferry.txt')),
        scan=read(os.path.join(D, 'b470_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b470_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b470_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b470_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b470_extract.txt')),
        lock=read(os.path.join(D, 'b470_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b470
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b468r_closing.txt')),
        addendum=read(os.path.join(D, 'b470_addendum.txt')),
        census=read(os.path.join(D, 'b470_census.txt')),
        span=read(os.path.join(D, 'b470_span_notes.txt')),
        scores=read(os.path.join(D, 'b470_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b470_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b470_survey.json')) or '{}'),
        cmpn=json.loads(read(os.path.join(D, 'b470_comparison.json')) or '{}'),
        W=json.loads(read(os.path.join(D, 'b470_writes.json')) or '{}'),
        bs=json.loads(read(os.path.join(D, 'b470_build_state.json')) or '{}'),
        blog=read(os.path.join(D, 'b470_build_log.txt')),
        builder=read(os.path.join(T, 'b470_build.py')),
        comp=read(os.path.join(D, 'b470_components.txt')),
        work=read(os.path.join(PP, 'day1', 'A_Place_to_Stand.md')),
        depmono=read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')),
        intake=read(os.path.join(ROOT, 'reports', '2026-08-20-external-intake.md')),
        b321=read(os.path.join(T, 'b321_window.py')),
        atlas=read(os.path.join(T, 'e16', 'carto_atlas.py')),
        efsrc=read(os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23', 'Zeta23', 'ExplicitFormula.lean')),
        desk=read(os.path.join(D, 'b470_desk_notes.txt')),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        clone_clean=gits(os.path.join(D, 'anthropic-zeta23', 'formal-math'), 'status', '--porcelain') == '',
        docs=sorted(f for f in os.listdir(D) if f.startswith('b470_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b470.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b470')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b470_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b470'):
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
    ('G-PRIOR-CLOSED-PUSHED', 'b468r closing -- the prior closed act',
     lambda S: 'row 318' in S['prior'], lambda S: cut(S, 'prior', 'row 318')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the survey record and file times',
     lambda S: 'b470 -- THE SURVEY.' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b470_extract.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', 'b470 -- THE SURVEY.')),
    ('G-J1-ABSENCE-RECORDED', 'the survey bank',
     lambda S: "unknown short option '-j'" in S['sv'].get('j1_error', '')
     and "unknown long option '--jobs'" in S['sv'].get('jobs_error', ''),
     lambda S: put(S, 'sv', dict(S['sv'], j1_error='ok'))),

    ('G-C1-DECLS-VERBATIM', 'the survey bank against the clone`s source',
     lambda S: any(d['label'] == 'EF_lit (statement)' and d['statement'].split(NL)[0] in S['efsrc']
                   for d in S['sv'].get('decls', [])),
     lambda S: put(S, 'efsrc', '')),
    ('G-C1-EXCLUSIONS-REASONED', 'the survey record',
     lambda S: 'EF_lit_chi` family (for L(s, chi)' in S['extract'] and 'xiEF` / `wEF` family' in S['extract'],
     lambda S: cut(S, 'extract', 'xiEF` / `wEF` family')),
    ('G-C1-B321-AT-ITS-LINES', 'b321_window.py itself',
     lambda S: 'residual=Z - (P - PR + A)' in S['b321'].split(NL)[143],
     lambda S: put(S, 'b321', S['b321'].replace('residual=Z - (P - PR + A)', 'residual=Z'))),
    ('G-C1-KERNEL-COMPARED', 'the atlas and the clone`s source',
     lambda S: 'Re psi(1/4 + i u/2) - log pi' in S['atlas']
     and '(Complex.digamma (1 / 4 + I * r / 2)).re - Real.log π' in S['efsrc'],
     lambda S: put(S, 'atlas', S['atlas'].replace('Re psi(1/4 + i u/2) - log pi', 'something else'))),
    ('G-C1-CLASS-OF-G-QUOTED', 'the components record',
     lambda S: 'g in C_c^inf(R*_+) with g~(z) = 0' in S['comp'],
     lambda S: cut(S, 'comp', 'g in C_c^inf(R*_+) with g~(z) = 0')),
    ('G-C1-VERDICT-PER-DECL', 'the comparison bank',
     lambda S: len(S['cmpn'].get('verdicts', [])) == 8 and all(
         v['verdict'] in ('MATCHES', 'CONTAINS', 'DOES NOT') for v in S['cmpn'].get('verdicts', [])),
     lambda S: put(S, 'cmpn', dict(S['cmpn'], verdicts=S['cmpn'].get('verdicts', [])[:7]))),
    ('G-C1-SPECIALIZATION-THREE-PARTS', 'the comparison bank',
     lambda S: all(k in S['cmpn'].get('spec', '') for k in ('[WHICH g]', '[WHICH NORMALIZATION]', '[WHICH SIGN CONVENTION]')),
     lambda S: put(S, 'cmpn', dict(S['cmpn'], spec=S['cmpn'].get('spec', '').replace('[WHICH g]', '')))),
    ('G-C1-DIFFERENCES-PRINTED', 'the comparison bank',
     lambda S: [d[0] for d in S['cmpn'].get('diffs', [])][:2] == ['SIGN', 'NORMALIZATION']
     and sum(1 for d in S['cmpn'].get('diffs', []) if d[0].startswith('SCOPE')) == 3,
     lambda S: put(S, 'cmpn', dict(S['cmpn'], diffs=S['cmpn'].get('diffs', [])[:2]))),
    ('G-C1-WORDER-ON-RULE', 'the comparison bank and the trail`s entry headings',
     lambda S: bool(S['cmpn'].get('contains')) == bool(
         re.search(r'^### `W-ORD-GW-IMPORT` \u2014 OPENED 2026-09-22', S['ot'], re.M)),
     lambda S: put(S, 'cmpn', dict(S['cmpn'], contains=[]))),
    ('G-C1-NOTHING-IMPORTED', 'the commit file lists',
     lambda S: not any(x.endswith('.lean') for x in list(S['tracked']) + list(S['rtracked'])),
     lambda S: put(S, 'rtracked', list(S['rtracked']) + ['tools/lean/EF_lit.lean'])),

    ('G-C2-NOTE-ONCE', 'the working monograph itself',
     lambda S: S['work'].count('**Analytic-row note (2026-09-22') == 1,
     lambda S: put(S, 'work', S['work'] + NL + '**Analytic-row note (2026-09-22, a duplicate).**')),
    ('G-C2-NOTE-FORM', 'the working monograph itself',
     lambda S: S['work'].index('| Mechanism enumeration |') < S['work'].index('**Analytic-row note (2026-09-22')
     < S['work'].index('Five convergent lines.'),
     lambda S: put(S, 'work', S['work'].replace('**Analytic-row note (2026-09-22', '**x')
                   + NL + '**Analytic-row note (2026-09-22')),
    ('G-C2-NOTE-PIN-AND-HASH', 'the working monograph itself',
     lambda S: all(h in S['work'] for h in ('19f827bee5834d61', '6de3b156342e7b4a', 'fbdc36bbf17d20af')),
     lambda S: put(S, 'work', S['work'].replace('19f827bee5834d61', 'xxxx'))),
    ('G-C2-ROW-FIGURE-KEPT', 'the working monograph itself',
     lambda S: '≥ 40.77% simple' in S['work'] and 'stays true as a lower bound' in S['work'],
     lambda S: put(S, 'work', S['work'].replace('≥ 40.77% simple', '≥ 66.67% simple'))),
    ('G-C2-NO-LINE-EDITED', 'the writes bank',
     lambda S: S['W'].get('note', {}).get('no_line_edited') is True and S['W']['note']['removed'] == 0,
     lambda S: put(S, 'W', dict(S['W'], note=dict(S['W'].get('note', {}), no_line_edited=False)))),
    ('G-C2-DEPOSIT-MD5-UNCHANGED', 'the md5 pair banks and the deposited file',
     lambda S: S['W'].get('deposit', {}).get('all_same') is True and 'Analytic-row note' not in S['depmono'],
     lambda S: put(S, 'depmono', S['depmono'] + NL + 'Analytic-row note')),
    ('G-C2-INTAKE-CLOSED-AT-ADDRESS', 'the intake report itself',
     lambda S: 'CLOSED 2026-09-22 (b470)' in S['intake'] and 'b468r_the_proportion_result' in S['intake'],
     lambda S: cut(S, 'intake', 'CLOSED 2026-09-22 (b470)')),
    ('G-C2-INTAKE-PREFIX', 'the writes bank',
     lambda S: S['W'].get('intake', {}).get('prefix') is True and S['W']['intake']['eol'] == '\r\n',
     lambda S: put(S, 'W', dict(S['W'], intake=dict(S['W'].get('intake', {}), prefix=False)))),
    ('G-R78-ENTERED', 'the trail`s entry headings',
     lambda S: S['ot'].count('### (R78) \u2014') == 1 and 'TRIGGER IS FIRED ONLY BY AN IDENTITY OR A BOUND' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('### (R78) \u2014', '### (R7x) \u2014'))),

    ('G-C3-SERIALIZED', 'the builder`s own text and the face',
     lambda S: "['lake', 'build', m]" in S['builder'] and "LEAN_NUM_THREADS='1'" in S['builder'],
     lambda S: cut(S, 'builder', "LEAN_NUM_THREADS='1'")),
    ('G-C3-FOREGROUND-ONLY', 'the build log',
     lambda S: 'CALL 1' in S['blog'] and 'run_in_background' not in S['blog'],
     lambda S: put(S, 'blog', S['blog'] + NL + 'run_in_background')),
    ('G-C3-OUTCOME-RECORDED', 'the build state bank and log',
     lambda S: S['bs'].get('outcome', '').startswith(('NOT COMPLETED', 'COMPLETED'))
     and 'THE FLOOR, MEASURED' in S['blog'],
     lambda S: put(S, 'bs', dict(S['bs'], outcome=''))),
    ('G-C3-PROFILES-FROM-RUN', 'the build state and the profile files',
     lambda S: (S['bs'].get('axioms_run') is True) == os.path.exists(os.path.join(D, 'b470_print_axioms_shipped.txt')),
     lambda S: put(S, 'bs', dict(S['bs'], axioms_run=not S['bs'].get('axioms_run')))),
    ('G-C3-GRADE-RULE', 'the trail`s own text',
     lambda S: (not S['bs'].get('axioms_run')) and 'The grade stays `DERIVES`, conditional' in S['ot'],
     lambda S: cut(S, 'ot', 'The grade stays `DERIVES`, conditional')),
    ('G-C3-SCRIPT-AS-SHIPPED', 'the builder and the clone`s tracked tree',
     lambda S: "'scripts/PrintAxioms.lean'" in S['builder'] and S['clone_clean'] is True,
     lambda S: put(S, 'clone_clean', False)),

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
     lambda S: 'where the deposit left it' in S['ot'], lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md', 'day1/A_Place_to_Stand.md'],
     lambda S: put(S, 'tracked', list(S['tracked']) + ['FINDINGS.md'])),
    ('G-TRAIL-APPEND', 'the trail own text',
     lambda S: S['ot'].count('### b470 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b470 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 319 |' in S['corr'], lambda S: cut(S, 'corr', '| 319 |')),
    ('G-WRITELIST-KINDS', 'every b470 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'day1/', 'data/', 'tools/')) for x in S['tracked']),
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
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b470'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b470 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b470_checks_postpush.txt' if pushed else 'b470_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b470_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
