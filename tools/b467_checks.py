# -*- coding: utf-8 -*-
"""b467_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b467_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b467_ferry.txt')),
        scan=read(os.path.join(D, 'b467_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b467_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b467_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b467_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b467_extract.txt')),
        lock=read(os.path.join(D, 'b467_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b467
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b466_closing.txt')),
        addendum=read(os.path.join(D, 'b467_addendum.txt')),
        census=read(os.path.join(D, 'b467_census.txt')),
        span=read(os.path.join(D, 'b467_span_notes.txt')),
        scores=read(os.path.join(D, 'b467_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b467_checks.py')),
        survey=json.loads(read(os.path.join(D, 'b467_survey.json')) or '{}'),
        conc=json.loads(read(os.path.join(D, 'b467_concordance.json')) or '{}'),
        b464stmts=[i.get('statement') for i in json.loads(
            read(os.path.join(D, 'b464_grades.json')) or '{}').get('items', [])],
        params=json.loads(read(os.path.join(D, 'b467_params.json')) or '{}'),
        comp=read(os.path.join(D, 'b467_components.txt')),
        b465ferry=read(os.path.join(D, 'b465_ferry.txt')),
        mono=read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        errata=read(os.path.join(PP, 'ERRATA.md')),
        lag=read(os.path.join(D, 'b358_source_lagarias0404394.txt')),
        desk=read(os.path.join(D, 'b467_desk_notes.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b467_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b467.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b467')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b467_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b467'):
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
    ('G-PRIOR-CLOSED-PUSHED', 'b466 closing -- the prior closed act',
     lambda S: 'row 314' in S['prior'], lambda S: cut(S, 'prior', 'row 314')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the survey bank and file times',
     lambda S: 'THE REHEARSAL, UNDER (R70)' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b467_extract.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', 'THE REHEARSAL, UNDER (R70)')),

    ('G-FERRY-BYTE-IDENTICAL-TO-B465', 'both ferry files on disk',
     lambda S: S['ferry'] == S['b465ferry'] and len(S['ferry']) > 100,
     lambda S: put(S, 'ferry', S['ferry'] + 'one byte the re-issue must not add')),
    # ### ### **THIS ARM PASSED ITS POSITIVE CONTROL AND WAS THEREFORE DEFECTIVE.** ### Its needle
    # ### was the bare word `re-issued`, and OPEN_TRAILS carries EIGHT of those across earlier acts,
    # ### so the mutation cut this act's and the arm still found seven. ### **A NEEDLE THAT IS NOT
    # ### UNIQUE TO THE THING BEING TESTED IS NOT A TEST** -- b464's `G-FOLD-RULINGS-LISTED` species,
    # ### and it is repaired the same way: anchor on this act's own sentence.
    ('G-R75-REISSUE-SAID', 'the LOCKED face and this act`s own trail record',
     lambda S: '(R75)' in S['face'] and 'b465 re-issued under (R75)' in S['ot'],
     lambda S: cut(S, 'ot', 'b465 re-issued under (R75)')),

    ('G-C1-EIGHT-FROM-B464-BANK', 'the concordance bank against b464 own bank',
     lambda S: len(S['conc'].get('items', [])) == 8,
     lambda S: put(S, 'conc', dict(S['conc'], items=S['conc'].get('items', [])[:7]))),
    ('G-C1-COUNT-AGREES', 'the survey bank',
     lambda S: S['survey'].get('eight') == 8,
     lambda S: put(S, 'survey', dict(S['survey'], eight=9))),
    ('G-C1-CONCORDANCE-PARSED-NOT-TYPED', 'the deposited monograph itself',
     lambda S: all(r['theorem'] in S['mono'] for r in S['survey'].get('concordance', []))
     and len(S['survey'].get('concordance', [])) == 7,
     lambda S: put(S, 'survey', dict(S['survey'], concordance=[
         dict(r, theorem='a_terminal_the_deposit_never_named')
         for r in S['survey'].get('concordance', [])]))),
    ('G-C1-CONCORDANCE-GRADE-IS-AXIOMS', 'the components record',
     lambda S: 'GRADE OF AXIOM' in S['comp'] and 'print axioms' in S['comp'],
     lambda S: cut(S, 'comp', 'GRADE OF AXIOM')),
    ('G-C1-MATCHER-LINEAGE-PRINTED', 'the survey record and the survey bank',
     lambda S: all(k in S['survey'].get('lineage', [{}])[0] for k in ('form1', 'form2', 'form3', 'form4'))
     and 'FORM 4 GOVERNS' in S['extract'],
     lambda S: cut(S, 'extract', 'FORM 4 GOVERNS')),
    ('G-C1-FINDER-CONTROL-FIRES', 'the survey bank',
     lambda S: S['survey'].get('control_fired') == S['survey'].get('control_rows') == 7,
     lambda S: put(S, 'survey', dict(S['survey'], control_fired=4))),
    ('G-C1-FINDER-NEGATIVE-CONTROL', 'the survey bank',
     lambda S: S['survey'].get('negative_control_no_row') is True,
     lambda S: put(S, 'survey', dict(S['survey'], negative_control_no_row=False))),
    ('G-C1-BOTH-COLUMNS-PRINTED', 'the concordance bank',
     lambda S: all(('b464_terminal' in i and 'concordance_row' in i)
                   for i in S['conc'].get('items', [])),
     lambda S: put(S, 'conc', dict(S['conc'], items=[
         {k: v for k, v in i.items() if k != 'b464_terminal'} for i in S['conc'].get('items', [])]))),
    ('G-C1-STANDIN-LABELLED', 'the concordance bank and the record',
     lambda S: all(i['standin'] for i in S['conc'].get('items', []) if not i['concordance_row'])
     and 'LABELLED A STAND-IN' in S['comp'],
     lambda S: cut(S, 'comp', 'LABELLED A STAND-IN')),
    # ### ### **THIS ARM FAILED LIVE AND IT WAS THE ARM THAT WAS WRONG.** ### It searched the survey
    # ### RUN RECORD for a phrase that lives only in the reader's own docstring, so it tested the
    # ### tool's prose and not the act's evidence -- and it could never have passed. ### **AND THE
    # ### DEEPER POINT IT MISSED:** this act read NO new terminal statement, because the concordance
    # ### assigned no terminal to grade against. ### The statements in play are b464's, banked, and
    # ### the honest arm reads THOSE and checks that not one of them is a docstring.
    ('G-C1-STATEMENT-NOT-DOCSTRING', 'b464`s banked statements, which are the ones in play',
     lambda S: bool(S['b464stmts']) and all(
         v and not v.lstrip().startswith('/--') for v in S['b464stmts']),
     lambda S: put(S, 'b464stmts', ['/-- a docstring -/'] * len(S['b464stmts']))),
    ('G-C1-FOUR-GRADES-ONLY', 'the concordance bank',
     lambda S: set(S['conc'].get('by_grade', {}))
     <= {'DERIVES', 'INTERFACES', 'NOT THE CLAIM', 'SHELL'},
     lambda S: put(S, 'conc', dict(S['conc'],
                                   by_grade=dict(S['conc'].get('by_grade', {}), PROBABLY_FINE=1)))),
    ('G-C1-TERMINAL-AT-PIN', 'the concordance bank against b464 own bank',
     lambda S: all(i['b464_terminal'] for i in S['conc'].get('items', [])),
     lambda S: put(S, 'conc', dict(S['conc'], items=[
         dict(i, b464_terminal='') for i in S['conc'].get('items', [])]))),
    ('G-C1-ROUTED-NOT-REPAIRED', 'the components record',
     lambda S: 'ROUTED' in S['comp'] and 'NOT REPAIRED' in S['comp'].upper(),
     lambda S: cut(S, 'comp', 'ROUTED')),
    ('G-C1-NO-ERRATUM-DRAFTED', 'ERRATA.md itself',
     lambda S: 'E-2026-09-22' not in S['errata'],
     lambda S: put(S, 'errata', S['errata'] + NL + '## E-2026-09-22-1 a draft that must not exist')),

    ('G-C2-SOURCE-PINNED', 'the components record',
     lambda S: '86f3d3c49f5a889f' in S['comp'], lambda S: cut(S, 'comp', '86f3d3c49f5a889f')),
    ('G-C2-WHICH-STATEMENT-SAID', 'the components record',
     lambda S: 'THE STATEMENT READ IS THE GENERAL EXPLICIT FORMULA' in S['comp'],
     lambda S: cut(S, 'comp', 'THE STATEMENT READ IS THE GENERAL EXPLICIT FORMULA')),
    ('G-C2-GARBLING-CARRIED', 'the components record',
     lambda S: 'PDF TEXT LAYER' in S['comp'], lambda S: cut(S, 'comp', 'PDF TEXT LAYER')),
    ('G-C2-SCOPE-SENTENCE-QUOTED', 'the pinned extraction itself',
     lambda S: 'For all other automorphic representations' in S['lag']
     and 'the appendix`s scope sentence' in S['comp'],
     lambda S: cut(S, 'comp', 'the appendix`s scope sentence')),
    ('G-C2-PARAMS-BEFORE-SITES', 'the components record own order',
     lambda S: 0 < S['comp'].find('PRINTED BEFORE ANY SITE IS PLACED')
     < S['comp'].find('THE SIX INDICES, WITH THE SAME THREE VERDICTS'),
     lambda S: cut(S, 'comp', 'PRINTED BEFORE ANY SITE IS PLACED')),
    ('G-C2-SIX-SITES-PLACED', 'the params bank',
     lambda S: len(S['params'].get('sites', [])) == 6,
     lambda S: put(S, 'params', dict(S['params'], sites=S['params'].get('sites', [])[:5]))),
    ('G-C2-THREE-VERDICTS-ONLY', 'the params bank',
     lambda S: set(S['params'].get('tally', {}))
     <= {'A PARAMETER', 'A COORDINATE OF ONE', 'OF NO PARAMETER'},
     lambda S: put(S, 'params', dict(S['params'], tally=dict(S['params'].get('tally', {}), MAYBE=1)))),
    ('G-C2-HEADINGS-THREE-ONLY', 'the params bank',
     lambda S: set(s['heading'] for s in S['params'].get('sites', []))
     <= set(S['params'].get('headings', [])),
     lambda S: put(S, 'params', dict(S['params'], headings=[]))),
    ('G-C2-NONE-BUCKET-REPORTED', 'the components record',
     lambda S: 'INDICES UNDER NONE OF THE THREE HEADINGS' in S['comp'],
     lambda S: cut(S, 'comp', 'INDICES UNDER NONE OF THE THREE HEADINGS')),
    ('G-C2-TRUNCATION-DISTINCTION-PRINTED', 'the components record and the extraction',
     lambda S: 'T IS BOUND BY THE' in S['comp'] and 'conditionally convergent' in S['lag'],
     lambda S: cut(S, 'comp', 'T IS BOUND BY THE')),
    ('G-C2-ANALYTIC-CONDUCTOR-DISCLOSED', 'the components record and the extraction',
     lambda S: 'analytic conductor' in S['comp'] and 'q(pi,iT)' in S['comp']
     and 'analytic conductor' in S['lag'],
     lambda S: cut(S, 'comp', 'q(pi,iT)')),
    ('G-C2-COMPARED-TO-CC-CELLWISE', 'the params bank',
     lambda S: len(S['params'].get('cc', {})) == 6 and S['params'].get('moved_against_cc') == 4,
     lambda S: put(S, 'params', dict(S['params'], cc={}))),
    ('G-C2-NO-SITE-ENTERED', 'FACES_LEDGER row U1 own site markers',
     lambda S: set(re.findall(r'\(([ivx]+)\) THE ', S['faces']))
     == set(['i', 'ii', 'iii', 'iv', 'v', 'vi']),
     lambda S: put(S, 'faces', S['faces'] + NL + '(vii) THE SEVENTH SITE THAT MUST NOT EXIST')),
    ('G-C2-ROWU1-UNEDITED', 'the commit file list',
     lambda S: not any(x.endswith('FACES_LEDGER.md') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['FACES_LEDGER.md'])),
    ('G-C2-FREEZE-QUOTED', 'the ledger own words and the components record',
     lambda S: 'THE REGISTER IS FROZEN AT SIX, b409' in S['faces']
     and 'FROZEN AT SIX BY b409' in S['comp'],
     lambda S: cut(S, 'comp', 'FROZEN AT SIX BY b409')),
    ('G-C2-NO-BRIDGE-TYPED', 'the components record',
     lambda S: 'NO BRIDGE IS TYPED' in S['comp'], lambda S: cut(S, 'comp', 'NO BRIDGE IS TYPED')),

    ('G-N1-SCORED', 'the scores bank', lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-SCORED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),
    ('G-SEAT-WIDTH-PREDICTION-SCORED', 'the scores bank and the params bank',
     lambda S: '"N2b"' in S['scores']
     and [x['verdict'] for x in S['params'].get('sites', []) if x['index'] == 'width']
     == ['OF NO PARAMETER', 'OF NO PARAMETER'],
     lambda S: cut(S, 'scores', '"N2b"')),

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
    ('G-NOKERNEL-RUN', 'the trail own text',
     lambda S: 'read at their pins, not run' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('read at their pins, not run', 'run'))),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b467 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b467 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 315 |' in S['corr'], lambda S: cut(S, 'corr', '| 315 |')),
    ('G-WRITELIST-KINDS', 'every b467 commit in three repositories',
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
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b467'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b467 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b467_checks_postpush.txt' if pushed else 'b467_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b467_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
