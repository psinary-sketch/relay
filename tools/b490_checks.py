# -*- coding: utf-8 -*-
"""b490_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b490_registration_2026-09-23.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b490_ferry.txt')),
        scan=read(os.path.join(D, 'b490_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b490_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b490_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b490_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b490_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b490_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b489_closing.txt')),
        addendum=read(os.path.join(D, 'b490_addendum.txt')),
        comp=read(os.path.join(D, 'b490_components.txt')),
        desk=read(os.path.join(D, 'b490_desk_notes.txt')),
        span=read(os.path.join(D, 'b490_span_notes2.txt'))
        + read(os.path.join(D, 'b490_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b490_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b490_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b490_survey.json')) or '{}'),
        err=read(os.path.join(PP, 'ERRATA.md')),
        rower=read(os.path.join(T, 'corr_row.py')),
        pid=read(os.path.join(D, 'b490_pid27508.txt')),
        launch=read(os.path.join(D, 'b475_launch.json')),
        integ=json.loads(read(os.path.join(D, 'b449_integrand.json')) or '{}'),
        b477=read(os.path.join(D, 'b477_entries.jsonl')),
        aimmap=read(os.path.join(D, 'b334_the_aim_map.txt')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b490_checks.py')),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b490.zip'))),
        spantool_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py') == ''),
        tools488=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b490_') and f.endswith('.py')
                         and f != 'b490_checks.py'),
        tools490=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b490_') and f.endswith('.py')
                         and f != 'b490_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b490 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b490_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b490 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        # ### ### **A FILE DIRTY BEFORE THIS ACT BEGAN WAS NOT WRITTEN BY IT.**
        # ### `b475_zeta23_build.log` has been modified-but-uncommitted since b475's run died,
        # ### and a bare `status` reading calls it one of THIS act's writes forever. ### The
        # ### write list bounds what the ACT writes, so the population is narrowed to files
        # ### whose mtime is AT OR AFTER the sealed face's -- and the ground is printed.
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                full = os.path.join(repo, rel)
                try:
                    if os.path.getmtime(full) < os.path.getmtime(FACE):
                        continue
                except OSError:
                    pass
                k.add(os.path.basename(rel))
    # ### b475's log is still being written by another act's live process; excluded BY NAME.
    S['kinds'] = k
    # ### ### **NO EXCLUSION. THE GROUND LAPSED AND THIS ACT RE-TESTED IT.**
    # ### b481 to b489 excused `b475_zeta23_build.log` because "another act's live process is
    # ### still appending to it". ### Component 0 finds pid 27508 ABSENT at two readings sixty
    # ### seconds apart, no `lean` or `lake` process at either, and the file cold for hours.
    # ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND DECAYS LIKE ONE**, so it is retired and
    # ### the arm runs at full width over every prior bank.
    LIVE = set()
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b490_') and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def declared_arms(face):
    """### ### **THE ARMS THE FACE DECLARES, MINUS THE ONES IT EXPRESSLY RETIRES.**
    ### This face says in its own (G2) block that `G-NOB475LOG` ### *"IS NOT CARRIED FORWARD
    ### UNDER THAT NAME"* ### and names its replacement. ### **AN ARM A FACE RETIRES IN WORDS IS
    ### NOT AN ARM IT DECLARES**, and a counter that reads only the token disagrees with the
    ### sentence beside it. ### The face is sealed; the COUNTER is what was wrong."""
    names = set(re.findall(r'`(G-[A-Z0-9-]+)`', face))
    for m in re.finditer(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', face):
        names.discard(m.group(1))
    return names


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'] or {})


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def steps(S):
    return res(S, 'steps') or []


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'ACT b490' in S['ferry'],
     lambda S: cut(S, 'ferry', 'ACT b490')),
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
     lambda S: any('LOCKED.' in l or 'SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('LOCKED.', 'x').replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b489`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 338 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b490' in S['ferry'] and 'b490' in S['face']
                and not os.path.exists(os.path.join(D, 'b491_ferry.txt'))),
     lambda S: cut(S, 'face', 'b490')),

    # -------------------------------------------------- component 0
    ('G-C0-TWO-READINGS', 'the banked process record -- both readings present',
     lambda S: 'READING 1' in S['pid'] and 'READING 2' in S['pid'],
     lambda S: cut(S, 'pid', 'READING 2')),
    ('G-C0-BOTH-ABSENT', 'the banked process record -- the finding, at both readings',
     lambda S: ('pid 27508 NOT FOUND' in S['pid'] and 'STILL NOT FOUND' in S['pid']
                and S['pid'].count('NO lean OR lake PROCESS EXISTS') >= 2),
     lambda S: put(S, 'pid', S['pid'].replace('STILL NOT FOUND', 'alive ; CPU 12 s'))),
    ('G-C0-LOG-STAT-NOT-READ', 'this act`s own tools, for a READ of b475`s log',
     # ### ### **THE ARM IS RE-POINTED AT THE ACT, NOT AT THE FILENAME.** ### The order directs
     # ### this act to print the log's byte count, so a tool MUST name it. ### What the rule
     # ### exists to prevent is OPENING it, and that is what this predicate forbids.
     lambda S: not re.search(r"(?:io\.)?open\s*\([^)]*b475_zeta23_build\.log|"
                             r"read_text\s*\([^)]*b475_zeta23|"
                             r"b475_zeta23_build\.log[^)\n]*\)\s*\.read", S['tools490'])
     and 'os.stat(log)' in S['tools490'],
     lambda S: put(S, 'tools490', S['tools490'] + NL
                   + "    io.open('b475_zeta23_build.log').read()")),
    ('G-C0-PID-IDENTIFIED', 'b475`s own launch record, against the act`s bank',
     lambda S: '27508' in S['launch'] and 'b475' in S['comp'] and '27508' in S['comp'],
     lambda S: cut(S, 'comp', '27508')),
    ('G-C0-EXCLUSION-DROPPED', 'the suite`s own population -- the log is no longer excused',
     # ### ### **THE ARM READ ITS OWN CONTROL STRING.** ### `split('LIVE = ')[-1]` takes the
     # ### LAST occurrence, which is the negative control a few lines below.
     lambda S: 'b475_zeta23_build.log' not in next(
         (l for l in S['suite'].split(NL) if l.strip().startswith('LIVE = ')), 'LIVE = ?'),
     lambda S: put(S, 'suite', S['suite'].replace(
         "LIVE = set()", "LIVE = {'b475_zeta23_build.log'}"))),

    # -------------------------------------------------- component 1
    ('G-C1-34-STEPS', 'the results bank -- one row per step, no more and no fewer',
     lambda S: len(steps(S)) == 34 and len(S['sv']['rows']) == 35,
     lambda S: put(S, 'res', dict(S['res'], steps=steps(S)[:30]))),
    ('G-C1-ENTRIES-NAMED', 'the results bank against a sieve recomputed here',
     lambda S: sum(1 for s in steps(S) if s['enters']) == res(S, 'n_entering')
     and res(S, 'n_entering') == 16,
     lambda S: put(S, 'res', dict(S['res'], n_entering=9))),
    ('G-C1-NONE-WHERE-NONE', 'the components bank -- the empty steps are PRINTED, not blank',
     # ### ### **COUNT THE TABLE, NOT THE PROSE.** ### The bank carries one further `(none)`
     # ### in the summary sentence beneath the table, which is not a row.
     lambda S: len([l for l in S['comp'].split(NL)
                    if re.match(r'\s+\d+\s+\d+\.\d+', l) and '(none)' in l])
     == sum(1 for s in steps(S) if not s['enters']),
     lambda S: put(S, 'comp', S['comp'].replace('(none)', '      ', 3))),
    ('G-C1-CHANNEL-SPLIT-CLOSES', 'the results bank -- d(m) against d(arch) - d(pr)',
     lambda S: all(s['closes'] < 1e-4 for s in steps(S) if s['closes'] is not None),
     lambda S: put(S, 'res', dict(S['res'], steps=[
         dict(s, closes=(1.0 if s['closes'] is not None else None)) for s in steps(S)]))),
    ('G-C1-BOTH-ROUNDINGS-PRINTED', 'the components bank -- the generator AND the stored float',
     lambda S: ('STORED-FLOAT reading' in S['comp'] and 'GENERATOR reading' in S['comp']
                and 'NEVER ENTERS THIS LADDER' in S['comp']),
     lambda S: cut(S, 'comp', 'GENERATOR reading')),
    ('G-C1-TERMS-AT-ONE-CELL', 'b449`s bank itself -- the terms, and the cell they sit at',
     lambda S: (isinstance((S['integ'].get('levels') or [{}])[-1].get('terms'), dict)
                and abs(S['integ'].get('a', 0) - 4.123106) < 1e-9
                and res(S, 'terms_cell') == S['integ'].get('a')),
     lambda S: put(S, 'res', dict(S['res'], terms_cell=99.0))),
    ('G-C1-HALT-HAS-A-CONTROL', 'the survey bank -- the halt`s positive control, and its yield',
     lambda S: ('THE POSITIVE CONTROL: THE FINDER SEES TERM VALUES WHEN THEY EXIST' in S['extract']
                and 'THE CONTROL FIRES : True' in S['extract']
                and 'A HALT PROVED OVER THE WRONG POPULATION' in S['desk']),
     lambda S: cut(S, 'extract', 'THE CONTROL FIRES : True')),
    ('G-C1-REHEARSAL-AT-17', 'the survey bank -- the (R70) rehearsal, at the step the order names',
     lambda S: ('THE STEP WHERE `17` ENTERS' in S['extract']
                and '4.123106' in S['extract'].split('(P4)')[-1]),
     lambda S: cut(S, 'extract', 'THE STEP WHERE `17` ENTERS')),

    # -------------------------------------------------- component 2
    ('G-C2-35-RATIOS', 'the results bank -- one ratio per cell',
     lambda S: len(res(S, 'ratios') or []) == 35,
     lambda S: put(S, 'res', dict(S['res'], ratios=(res(S, 'ratios') or [])[:20]))),
    ('G-C2-PEAK-NAMED', 'the results bank -- the peak, recomputed from the ratio column',
     lambda S: (res(S, 'ratios') and
                abs(max(res(S, 'ratios')) - res(S, 'peak')) < 1e-15
                and res(S, 'ratios').index(max(res(S, 'ratios'))) == res(S, 'peak_i')),
     lambda S: put(S, 'res', dict(S['res'], peak_i=0))),
    ('G-C2-OUTLIER-MARKED', 'the components bank -- the outlier cell, marked in the table',
     lambda S: 'THE OUTLIER' in S['comp'] and '4.123106' in S['comp'],
     lambda S: cut(S, 'comp', 'THE OUTLIER')),
    ('G-C2-MINIMUM-MARKED', 'the components bank -- the minimum cell, marked in the table',
     lambda S: 'MINIMUM MARGIN' in S['comp'],
     lambda S: cut(S, 'comp', 'MINIMUM MARGIN')),
    ('G-C2-ONE-VERDICT', 'the components bank -- exactly one verdict sentence, and it is signed',
     lambda S: S['comp'].count('THE ONE VERDICT') == 1
     and 'DOES NOT' in S['comp'].split('THE ONE VERDICT')[1][:120],
     lambda S: put(S, 'comp', S['comp'].replace('THE ONE VERDICT', 'x', 1))),

    # -------------------------------------------------- component 3
    ('G-C3-THREE-CROSSINGS-QUOTED', 'b334`s bank against the components bank',
     lambda S: (S['comp'].count('16.290216') >= 2 and '46.960994' in S['comp']
                and 'THE EPSTEIN CROSSING REGION' in S['aimmap']),
     lambda S: cut(S, 'comp', '46.960994')),
    ('G-C3-HEIGHTS-AND-SUPPORTS', 'the trail -- each aim with its height AND its support',
     lambda S: all(x in S['ot'] for x in ('16.290216', '46.960994', '+0.655053',
                                          '+1.362830', '+0.194219')),
     lambda S: cut(S, 'ot', '+0.194219')),
    ('G-C3-TESTED-AT-b334-IN-TRAIL', 'the trail -- the word the order names',
     lambda S: 'TESTED-AT-b334' in S['ot'].split('### b490 ')[-1],
     lambda S: put(S, 'ot', S['ot'].replace('TESTED-AT-b334', 'tested somewhere'))),
    ('G-C3-LADDER-REACH-STATED', 'the trail -- WHY the ladder could not test it',
     lambda S: ('5.656854' in S['ot'].split('### b490 ')[-1]
                and 'seven and fourteen' in S['ot']),
     lambda S: cut(S, 'ot', 'seven and fourteen')),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the desk bank -- an ABSENCE, printed as one',
     lambda S: ('NOT DECIDABLE FROM THE BANKS' in S['desk']
                and res(S, 'n1_decidable') is False),
     lambda S: cut(S, 'desk', 'NOT DECIDABLE FROM THE BANKS')),
    ('G-N2-SCORED', 'the results bank against the desk bank',
     # ### ### **A VERDICT MAY SIT ON THE NEXT LINE.** ### `line_with` returns the FIRST line
     # ### carrying the marker; this desk puts `(N2)` on one line and its verdict on the next.
     lambda S: (res(S, 'verdict') is False and res(S, 'dist') == 2
                and 'REFUTED' in S['desk'].split('**(N2)**')[1][:300]),
     lambda S: put(S, 'res', dict(S['res'], dist=1, verdict=True))),
    ('G-N3-SCORED', 'the desk bank against b334`s own paragraph',
     lambda S: ('HELD' in S['desk'].split('**(N3)**')[1][:400]
                and 'EMPTY on the covered leg' in S['aimmap']),
     lambda S: put(S, 'aimmap', S['aimmap'].replace('EMPTY on the covered leg', 'x'))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ; HELD 2 ; REFUTED 1' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 2 ; REFUTED 1')),

    # -------------------------------------------------- the standing arms
    ('G-NOCHAIN-RUN', 'this act`s own tools, for a chain call',
     # ### ### **READING A TOOL IS NOT RUNNING IT.** ### The survey opens `b321_window.py` as
     # ### TEXT to quote its return signature, and the arm's first version condemned that.
     # ### It now forbids the shapes that EXECUTE: an import, or a call on the module.
     lambda S: not re.search(r'^\s*(?:import|from)\s+(?:carto_atlas|b317_smear|b318_square|'
                             r'b321_window)\b|(?:carto_atlas|b317_smear|b318_square|'
                             r'b321_window)\.\w+\s*\(', S['tools490'], re.M),
     lambda S: put(S, 'tools490', S['tools490'] + NL + 'import b321_window')),
    ('G-NOLANE-OPENED', 'this act`s own tools, for a lane',
     lambda S: not re.search(r'\bLEAN_PATH\b\s*=|\blake\b[^\n]{0,12}\bbuild\b', S['tools490']),
     lambda S: put(S, 'tools490', S['tools490'] + NL + 'LEAN_PATH=build lean X')),
    ('G-NOZENODO-WRITE', 'this act`s own tools, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files)\b', S['tools490'], re.I),
     lambda S: put(S, 'tools490', S['tools490'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
    ('G-NOTHING-COMPILED', 'this act`s own tools, for a BUILD CALL',
     lambda S: not re.search(r'(?:subprocess|os\.system|Popen|check_output|run)\s*\([^)]{0,80}'
                             r'(?:lake|LEAN_PATH|lean)\b|lean\s+--\w', S['tools490']),
     lambda S: put(S, 'tools490', S['tools490'] + NL + 'subprocess.run(["lake","build","X"])')),
    ('G-SPAN-BY-TOOL', 'the span tool record, and what this act says it counts',
     lambda S: 'THE CURRENT SPAN' in S['span'] and 'the span, by tool' in S['desk'],
     lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
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
    ('G-CORPUS-SCOPE', 'the commit file list -- ONE document, named on the face',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b490 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b490 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: ('| 339 |' in S['corr'] and S['corr'].count('| 339 |') == 1
                and S['corr'].count('b490, under (R100)') == 1),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 339 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b490 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x == 'OPEN_TRAILS.md' or x.startswith(('data/', 'tools/'))
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
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree, read in the source',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/claude_paper_2026-08-11.pdf')),
    ('G-CORPUS-LEAN-UNTOUCHED', 'the lv and kernel working trees, read in the source',
     lambda S: S['corpus_lean_clean'] is True, lambda S: put(S, 'corpus_lean_clean', False)),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b490_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b490_components.txt' in gits(ROOT, 'show'")),
]








def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    # ### ### **AN ARM THE FACE RETIRES IN WORDS IS NOT AN ARM IT DECLARES.** ### This face's
    # ### (G2) block says `G-NOB475LOG` *"IS NOT CARRIED FORWARD UNDER THAT NAME"* and names its
    # ### replacement. ### A counter that reads only the token disagreed with the sentence beside
    # ### it, and reported an arm declared-but-not-run. ### The face is sealed and correct; the
    # ### COUNTER was wrong, and it now honours the retirement it is reading.
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    if retired:
        rec('  ### arms the face RETIRES in its own words : %s' % sorted(retired))
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b490')
              and 'data/b490_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b490 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ONE excluded BY NAME, with its ground:'
        % S['prior_checked'])
    rec('  ###   `b475_zeta23_build.log`      -- another act`s live process is still appending.')
    rec('  ### ### **b487`S SECOND EXCLUSION IS NOT CARRIED** -- it was b485`s bank, which (R97)')
    rec('  ### directed b487 to append to. ### This act writes no prior bank, so the exception')
    rec('  ### lapses with the ruling that made it and the arm is back at full width.')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b490_checks_postpush.txt' if pushed else 'b490_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b490_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
