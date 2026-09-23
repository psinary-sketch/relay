# -*- coding: utf-8 -*-
"""b486_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b486_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b486_ferry.txt')),
        scan=read(os.path.join(D, 'b486_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b486_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b486_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b486_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b486_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b486_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b479_closing.txt')),
        addendum=read(os.path.join(D, 'b486_addendum.txt')),
        comp=read(os.path.join(D, 'b486_components.txt')),
        desk=read(os.path.join(D, 'b486_desk_notes.txt')),
        span=read(os.path.join(D, 'b486_span_notes.txt')),
        spanj=json.loads(read(os.path.join(D, 'b486_span.json')) or '{}'),
        res=json.loads(read(os.path.join(D, 'b486_results.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b486_survey.json')) or '{}'),
        err=read(os.path.join(PP, 'ERRATA.md')),
        errclean=gits(PP, 'status', '--porcelain', '--', 'ERRATA.md'),
        b479c=read(os.path.join(D, 'b479_closing.txt')),
        spantool=read(os.path.join(T, 'b363_span.py')),
        # ### **THE SURVEY TOOL'S OWN TEXT, AS A SOURCE.** ### The arm below first read
        # ### the file from disk INSIDE its predicate and ignored `S`, so its positive
        # ### control could not move it -- b482's species, a second time. ### **AN ARM
        # ### THAT DOES NOT READ ITS SUPPLIED SOURCE CANNOT FAIL.**
        extracttool=read(os.path.join(T, 'b486_extract.py')),
        spantool_clean=gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py'),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b486_checks.py')),
        tools486=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b486_') and f.endswith('.py') and f != 'b486_checks.py'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b486.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b486 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b486_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b486 --'):
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
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b486_') and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


SPANACTS = ['b475', 'b478', 'b476', 'b480', 'b477', 'b481', 'b483', 'b484', 'b485', 'b482', 'b479']

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'RUN b486' in S['ferry'],
     lambda S: cut(S, 'ferry', 'RUN b486')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b479`s closing AND the ledger',
     lambda S: ('THE COMMITS, EACH READ BACK BY ls-remote' in S['prior']
                and S['corr'].count('| 334 |') == 1),
     lambda S: cut(S, 'prior', 'THE COMMITS, EACH READ BACK BY ls-remote')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and the fold`s own number',
     lambda S: (not os.path.exists(os.path.join(D, 'b487_ferry.txt')) and 'b486' in S['face']
                and os.path.exists(os.path.join(D, 'b486_ferry.txt'))),
     lambda S: cut(S, 'face', 'b486')),

    # -------------------------------------------------- component 1
    ('G-C1-ELEVEN-BY-FILING', 'the survey bank against the trail itself',
     lambda S: (S['sv']['count'] == 11 and len(S['sv']['filed']) == 11
                and all(('### %s —' % a) in S['ot'] for a in SPANACTS)),
     lambda S: put(S, 'sv', dict(S['sv'], count=9))),
    ('G-C1-ORDER-MATCHES-TRAIL', 'the survey bank -- the order`s list against the trail`s',
     lambda S: S['sv']['order_matches'] is True and S['sv']['filed'] == SPANACTS,
     lambda S: put(S, 'sv', dict(S['sv'], order_matches=False))),
    ('G-C1-VERDICTS-FROM-OWN-BANKS', 'each act`s own closing bank on disk',
     lambda S: all(os.path.exists(os.path.join(D, '%s_closing.txt' % a)) for a in SPANACTS)
     and len(S['sv']['acts']) == 11,
     lambda S: put(S, 'sv', dict(S['sv'], acts=S['sv']['acts'][:4]))),
    ('G-C1-NO-ACT-SUMMARISED', 'the components record, for any re-scoring verb',
     lambda S: ('A FOLD DECIDES NOTHING NEW' in S['comp']
                and not re.search(r'\bre-?scored to\b|\bnow reads\b|\brevised to\b', S['comp'])),
     lambda S: put(S, 'comp', S['comp'] + NL + 'b483`s (F2) is re-scored to FIRES by this fold')),

    # -------------------------------------------------- component 2
    ('G-C2-SIX-CLAUSES-ALL-CITED', 'the survey bank`s clause check',
     lambda S: (len(S['sv']['clauses']) == 6
                and all(v['ok'] for v in S['sv']['clauses'].values())),
     lambda S: put(S, 'sv', dict(S['sv'], clauses=dict(
         S['sv']['clauses'], S2=dict(S['sv']['clauses']['S2'], ok=False))))),
    ('G-C2-NEEDLES-FIXED-BEFORE', 'the survey tool`s own text, READ IN THE SOURCE',
     lambda S: ('CLAUSES = [' in S['extracttool']
                and 'W-ORD-QUADRATURE-BOUND' in S['extracttool']
                and S['extracttool'].index('CLAUSES = [')
                < S['extracttool'].index('def main(')),
     lambda S: put(S, 'extracttool', S['extracttool'].replace('CLAUSES = [', 'x = ['))),
    ('G-C2-PERMISSIVE-YIELD-PRINTED', 'the components record',
     lambda S: ('A FILTER THAT KEEPS MOST OF THE CORPUS PROVES NOTHING' in S['comp']
                and '85 TO 264 ACTS EACH' in S['comp']),
     lambda S: cut(S, 'comp', 'A FILTER THAT KEEPS MOST OF THE CORPUS PROVES NOTHING')),
    ('G-C2-PRESPAN-MARKED', 'the results bank against the components record',
     lambda S: (sum(1 for d in S['res']['digest'] if d[2]) == 2
                and 'CITED FROM OUTSIDE THE SPAN' in S['comp']),
     lambda S: put(S, 'res', dict(S['res'], digest=[[d[0], d[1], False]
                                                    for d in S['res']['digest']]))),
    ('G-C2-NOTHING-UNCITED-IN-BLOCK', 'the components record -- every clause names its act',
     lambda S: S['comp'].count('--- cited from') == 6,
     lambda S: put(S, 'comp', S['comp'].replace('--- cited from', 'x', 1))),

    # -------------------------------------------------- component 3
    ('G-C3-RULINGS-AT-THEIR-ACTS', 'the survey bank -- each ruling banked at a named act',
     lambda S: (len(S['sv']['rulings']) >= 12
                and all(r[1] in SPANACTS for r in S['sv']['rulings'])),
     lambda S: put(S, 'sv', dict(S['sv'], rulings=[['R99', 'bZZZ', 'x']]))),
    ('G-C3-R88-NAMED-SEPARATELY', 'the components record and the file that banks it',
     lambda S: ('R88' in S['comp'] and 'b477_r88_standing_order.txt' in S['comp']
                and os.path.exists(os.path.join(D, 'b477_r88_standing_order.txt'))),
     lambda S: cut(S, 'comp', 'b477_r88_standing_order.txt')),
    ('G-C3-SEAT-TABLE-FROM-CLOSINGS', 'the survey bank -- each seat row from an act`s closing',
     lambda S: (len(S['sv']['seat']) == 7
                and all(a in SPANACTS for a, _ in S['sv']['seat'])),
     lambda S: put(S, 'sv', dict(S['sv'], seat=[]))),
    ('G-C3-TRUNCATION-NOT-A-DEFECT', 'the components record and b479`s bank on disk',
     lambda S: ('A MESSAGE THAT DID NOT ARRIVE IS NOT A RECORD THAT WAS NOT MADE' in S['comp']
                and len(S['b479c']) > 2000),
     lambda S: put(S, 'b479c', '')),

    # -------------------------------------------------- the errata finding
    ('G-ERRATA-COLLISION-REPORTED', 'ERRATA.md itself against the components record',
     lambda S: (S['err'].count('E-2026-09-22-1') == 2
                and 'E-2026-09-22-1` TWICE' in S['comp'].replace('**', '')
                or ('TWICE' in S['comp'] and S['err'].count('E-2026-09-22-1') == 2)),
     lambda S: put(S, 'err', S['err'].replace('E-2026-09-22-1', 'x', 1))),
    ('G-ERRATA-NOT-RENUMBERED', 'ERRATA.md`s porcelain, READ IN THE SOURCE',
     lambda S: S['errclean'] == '',
     lambda S: put(S, 'errclean', ' M ERRATA.md')),

    # -------------------------------------------------- the standing arms
    ('G-NO-EXPECTATIONS-INVENTED', 'the face and the desk bank',
     lambda S: ('NONE. ### THE ORDER REGISTERS NO EXPECTATION' in S['face']
                and 'NONE REGISTERED BY THIS ACT, AND NONE INVENTED' in S['desk']
                and not os.path.exists(os.path.join(D, 'b486_scores.json'))),
     lambda S: cut(S, 'desk', 'NONE REGISTERED BY THIS ACT, AND NONE INVENTED')),
    ('G-SPAN-BOTH-READINGS', 'the span record, the survey bank and the desk',
     lambda S: ('THE CURRENT SPAN' in S['span'] and S['sv']['count'] == 11
                and str(S['spanj']['current_span']) in S['desk'] and '11' in S['desk']),
     lambda S: put(S, 'sv', dict(S['sv'], count=0))),
    ('G-TOOL-NOT-EDITED', 'the span tool`s porcelain, READ IN THE SOURCE',
     lambda S: S['spantool_clean'] == '' and 'def main(' in S['spantool'],
     lambda S: put(S, 'spantool_clean', ' M tools/b363_span.py')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md', 'FINDINGS.md'))
                       for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['ERRATA.md'])),
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
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b486 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b486 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 335 |' in S['corr'] and S['corr'].count('| 335 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 335 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b486 commit in three repositories, against (R91)`s STEM GLOB',
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
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools486'],
     lambda S: put(S, 'tools486', S['tools486'] + NL + "open('b475_zeta23_build.log')")),
    ('G-NOTHING-COMPILED', 'this act`s own tools, for a build or a Lean invocation',
     lambda S: not re.search(r'\blake\b[^\n]{0,12}\bbuild\b|lean\s+--|LEAN_PATH', S['tools486']),
     lambda S: put(S, 'tools486', S['tools486'] + NL + 'subprocess.run(["lake","build","X"])')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b486_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b486_components.txt' in gits(ROOT, 'show'")),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b486')
              and 'data/b486_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b486 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b486_checks_postpush.txt' if pushed else 'b486_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b486_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
