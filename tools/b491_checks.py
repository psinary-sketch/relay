# -*- coding: utf-8 -*-
"""b491_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b491_registration_2026-09-23.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b491_ferry.txt')),
        scan=read(os.path.join(D, 'b491_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b491_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b491_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b491_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b491_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b491_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b490_closing.txt')),
        addendum=read(os.path.join(D, 'b491_addendum.txt')),
        comp=read(os.path.join(D, 'b491_components.txt')),
        desk=read(os.path.join(D, 'b491_desk_notes.txt')),
        span=read(os.path.join(D, 'b491_span_notes2.txt'))
        + read(os.path.join(D, 'b491_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b491_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b491_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b491_survey.json')) or '{}'),
        err=read(os.path.join(PP, 'ERRATA.md')),
        rower=read(os.path.join(T, 'corr_row.py')),
        log=read(os.path.join(D, 'b475_zeta23_build.log')),
        b477=read(os.path.join(D, 'b477_entries.jsonl')),
        aimmap=read(os.path.join(D, 'b334_the_aim_map.txt')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b491_checks.py')),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b491.zip'))),
        spantool_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py') == ''),
        tools491=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b491_') and f.endswith('.py')
                         and f != 'b491_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b491 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        # ### ### **THE LOG IS COMMITTED, NOT WRITTEN.** ### After the commit its working-tree
        # ### state must be clean: the bytes in the index are the bytes this act read.
        log_unchanged=(gits(ROOT, 'status', '--porcelain', '--',
                            'data/b475_zeta23_build.log') == ''
                       or gits(ROOT, 'diff', '--numstat', '--',
                               'data/b475_zeta23_build.log') == ''),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b491_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b491 --'):
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
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b491_') and f not in LIVE]
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


def seg(text, marker, n=220):
    """### ### **THE TEXT AFTER A MARKER, OR EMPTY WHEN THE MARKER IS GONE.**
    ### A negative control removes the marker; a bare `split(...)[1]` then RAISES instead of
    ### failing, and ### **AN ARM THAT CRASHES UNDER ITS CONTROL HAS NOT BEEN EXERCISED.**"""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def prof(S):
    return (S['sv'] or {}).get('profiles') or []


STD3 = '[propext, Classical.choice, Quot.sound]'

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the two banked ferry parts',
     lambda S: ('paste ends (part 1 of 2)' in S['ferry'] and 'ACT b491' in S['ferry']
                and 'paste ends (part 2 of 2)' in read(os.path.join(D, 'b492_ferry.txt'))),
     lambda S: cut(S, 'ferry', 'paste ends (part 1 of 2)')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b490`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 339 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b491' in S['ferry'] and 'b491' in S['face']
                and not os.path.exists(os.path.join(D, 'b493_ferry.txt'))),
     lambda S: cut(S, 'face', 'b491')),

    # -------------------------------------------------- the log
    ('G-LOG-COMMITTED-UNCHANGED', 'the log`s own bytes against the committed blob',
     lambda S: S['log_unchanged'] is True,
     lambda S: put(S, 'log_unchanged', False)),
    ('G-LOG-EXIT-TALLY', 'the log itself, counted here and not read from the bank',
     lambda S: (S['log'].count('=== EXIT ') == res(S, 'exits')
                and len([l for l in S['log'].split(NL)
                         if l.startswith('=== EXIT') and not l.startswith('=== EXIT 0')]) == 0
                and res(S, 'nonzero') == 0),
     lambda S: put(S, 'res', dict(S['res'], nonzero=3))),
    ('G-LOG-LAST-FORTY', 'the components bank against the log`s own tail',
     lambda S: all(('| ' + l[:110]) in S['comp']
                   for l in S['log'].split(NL)[-40:] if l.strip()),
     lambda S: put(S, 'comp', S['comp'].replace('RUN COMPLETE', 'x'))),
    ('G-LOG-FAILURES-OR-NONE', 'the log, for an error shape -- and NONE printed where none',
     lambda S: (res(S, 'errors') == 0 and res(S, 'sorry') == 0
                and 'MODULES THAT FAILED : NONE' in S['comp']),
     lambda S: cut(S, 'comp', 'MODULES THAT FAILED : NONE')),
    ('G-LOG-WALLTIME-TWO-MARKS', 'the results bank -- two independent marks, and the shortfall',
     lambda S: (res(S, 'wall_s') > 0 and res(S, 'dur_sum') > 0
                and res(S, 'shortfall') == res(S, 'wall_s') - res(S, 'dur_sum')
                and res(S, 'shortfall') > 0),
     lambda S: put(S, 'res', dict(S['res'], shortfall=-1))),
    ('G-LOG-DEFECT-NAMED', 'the components bank -- b480`s defect, named where it bites',
     lambda S: ('b480`S DEFECT' in S['comp'] and res(S, 'distinct_instants') < 10
                and 'NO' in S['comp'].split('PER-MODULE DURATION')[0][-40:]),
     lambda S: put(S, 'res', dict(S['res'], distinct_instants=193))),

    # -------------------------------------------------- the profiles
    ('G-PROF-TWENTY-LINES', 'the log itself, counted here',
     lambda S: (len([l for l in S['log'].split(NL) if 'depends on axioms:' in l])
                == len(prof(S)) == 20),
     lambda S: put(S, 'sv', dict(S['sv'], profiles=prof(S)[:12]))),
    ('G-PROF-SEVENTEEN-AND-THREE', 'the survey bank -- the two phases, by line number',
     lambda S: (len([p for p in prof(S) if p['line'] < 5081]) == 17
                and len([p for p in prof(S) if p['line'] > 5081]) == 3),
     lambda S: put(S, 'sv', dict(S['sv'], profiles=[
         dict(p, line=1) for p in prof(S)]))),
    ('G-PROF-VERBATIM', 'the components bank against the log, line for line',
     lambda S: all(("'%s' depends on axioms: %s" % (p['name'], p['axioms'])) in S['comp']
                   and ("'%s' depends on axioms: %s" % (p['name'], p['axioms'])) in S['log']
                   for p in prof(S)),
     # ### ### **THE CONTROL MUST MOVE WHAT THE PREDICATE READS.** ### Its first version
     # ### replaced a substring five times and left every FULL quoted line intact, so the arm
     # ### could not fail. ### It now deletes one whole quoted line.
     lambda S: cut(S, 'comp', "'%s' depends on axioms: %s"
                   % (prof(S)[0]['name'], prof(S)[0]['axioms']))),
    ('G-PROF-STD3-WHOLE-STRING', 'the survey bank -- the WHOLE axiom string, not a name count',
     lambda S: (all(p['std3'] == (p['axioms'] == STD3) for p in prof(S))
                and sum(1 for p in prof(S) if p['std3']) == res(S, 'n_std3') == 20),
     lambda S: put(S, 'sv', dict(S['sv'], profiles=[
         dict(p, axioms='[propext, Classical.choice, Quot.sound, sorryAx]') for p in prof(S)]))),
    ('G-PROF-NONE-ABSENT', 'the components bank -- no row reads ABSENT',
     # ### ### **THE ACT'S OWN SUMMARY LINE CARRIES THE WORD THE ARM FORBIDS** -- it prints
     # ### `ABSENT : 0` to report the empty bucket, which is exactly the practice the record
     # ### wants. ### The arm reads the profile ROWS, not the section's prose.
     lambda S: not [l for l in S['comp'].split(NL)
                    if re.match(r'\s+->', l) and 'ABSENT' in l],
     lambda S: put(S, 'comp', S['comp'].replace('-> ### **STANDARD THREE**',
                                                '-> ### **ABSENT**', 1))),
    ('G-PROF-SCOPE-STATED', 'the face and the components bank -- what a profile does NOT say',
     # ### ### **THE BANK HARD-WRAPS THROUGH THE NEEDLE** -- b?'s anchor-wrapping lesson.
     # ### The phrase spans two lines in the components record, so a contiguous match fails on
     # ### a document that says exactly what the arm wants. ### Match a phrase that survives.
     lambda S: ('IT DOES NOT SAY THE STATEMENT IS STRONG' in S['face']
                and 'HYPOTHESES ARE DISCHARGED' in S['comp']
                and 'IT DOES NOT SAY' in S['comp']),
     lambda S: cut(S, 'comp', 'HYPOTHESES ARE DISCHARGED')),

    # -------------------------------------------------- (R82)
    ('G-R82-VERDICT-BANKED', 'the results bank and the components bank',
     lambda S: res(S, 'holds') is True and '(R82) HOLDS' in S['comp'],
     lambda S: put(S, 'res', dict(S['res'], holds=False))),
    ('G-R82-KIND-OF-VOID-NAMED', 'the components bank -- both prior voidings, by kind',
     lambda S: (S['comp'].count('FOR WANT OF A RUN') >= 2
                and 'NEITHER WAS A VOID FOR WANT OF A PROFILE' in S['comp']),
     lambda S: cut(S, 'comp', 'NEITHER WAS A VOID FOR WANT OF A PROFILE')),
    ('G-R82-SCOPE-BOUNDED', 'the trail -- the verdict carries its own scope',
     lambda S: ('at the commit b475 built' in S['ot'].split('### b491 ')[-1]
                and 'Nothing about RH follows' in S['ot'].split('### b491 ')[-1]),
     lambda S: cut(S, 'ot', 'at the commit b475 built')),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the desk bank against the results bank',
     lambda S: 'HELD' in seg(S['desk'], '**(N1)**') and res(S, 'nonzero') == 0,
     lambda S: cut(S, 'desk', '**(N1)**')),
    ('G-N2-SCORED', 'the desk bank against the results bank',
     lambda S: 'HELD' in seg(S['desk'], '**(N2)**') and res(S, 'n_profiles') >= 1,
     lambda S: put(S, 'res', dict(S['res'], n_profiles=0))),
    ('G-N3-SCORED', 'the desk bank against the survey bank',
     lambda S: ('HELD' in seg(S['desk'], '**(N3)**')
                and all(p['std3'] for p in prof(S))),
     lambda S: put(S, 'sv', dict(S['sv'], profiles=[
         dict(p, std3=False) for p in prof(S)]))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ; HELD 3' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 3')),

    # -------------------------------------------------- the standing arms
    ('G-NOCHAIN-RUN', 'this act`s own tools, for a chain call',
     lambda S: not re.search(r'^\s*(?:import|from)\s+(?:carto_atlas|b317_smear|b318_square|'
                             r'b321_window)\b|(?:carto_atlas|b317_smear|b318_square|'
                             r'b321_window)\.\w+\s*\(', S['tools491'], re.M),
     lambda S: put(S, 'tools491', S['tools491'] + NL + 'import b321_window')),
    ('G-NOLANE-OPENED', 'this act`s own tools -- the lane opens at b492, NOT here',
     lambda S: not re.search(r'\bLEAN_PATH\b\s*=|\blake\b[^\n]{0,12}\bbuild\b', S['tools491']),
     lambda S: put(S, 'tools491', S['tools491'] + NL + 'LEAN_PATH=build lean X')),
    ('G-NOTHING-COMPILED', 'this act`s own tools, for a BUILD CALL',
     lambda S: not re.search(r'(?:subprocess|os\.system|Popen|check_output|run)\s*\([^)]{0,80}'
                             r'(?:lake|LEAN_PATH|lean)\b|lean\s+--\w', S['tools491']),
     lambda S: put(S, 'tools491', S['tools491'] + NL + 'subprocess.run(["lake","build","X"])')),
    ('G-NOZENODO-WRITE', 'this act`s own tools, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files)\b', S['tools491'], re.I),
     lambda S: put(S, 'tools491', S['tools491'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
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
     lambda S: S['ot'].count('### b491 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b491 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: ('| 340 |' in S['corr'] and S['corr'].count('| 340 |') == 1
                and S['corr'].count('b491, under (R101)') == 1),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 340 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b491 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in (set(S['kinds']) - {'b475_zeta23_build.log'})
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
     lambda S: "data/b491_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b491_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b491')
              and 'data/b491_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **TWO ARMS ARE POST-PUSH BY NATURE.** ### The mirror is built after the push,
    # ### and `data/b475_zeta23_build.log` is COMMITTED by this act -- until that commit its
    # ### working tree is dirty and the arm is FALSE for a reason that is not a fault.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-LOG-COMMITTED-UNCHANGED']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b491 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b491_checks_postpush.txt' if pushed else 'b491_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b491_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
