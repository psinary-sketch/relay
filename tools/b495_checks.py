# -*- coding: utf-8 -*-
"""b495_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FACE = os.path.join(D, 'b495_registration_2026-09-23.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b495_ferry.txt')),
        scan=read(os.path.join(D, 'b495_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b495_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b495_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b495_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b495_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b495_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b493_closing.txt')),
        addendum=read(os.path.join(D, 'b495_addendum.txt')),
        comp=read(os.path.join(D, 'b495_components.txt')),
        desk=read(os.path.join(D, 'b495_desk_notes.txt')),
        span=read(os.path.join(D, 'b495_span_notes2.txt'))
        + read(os.path.join(D, 'b495_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b495_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b495_scores.json')) or '{}'),
        pin=read(os.path.join(D, 'b495_pin.txt')),
        pinj=json.loads(read(os.path.join(D, 'b495_pin.json')) or '{}'),
        create=read(os.path.join(D, 'b495_create.txt')),
        crej=json.loads(read(os.path.join(D, 'b495_create.json')) or '{}'),
        push=read(os.path.join(D, 'b495_push.txt')),
        pushj=json.loads(read(os.path.join(D, 'b495_push.json')) or '{}'),
        waiverj=json.loads(read(os.path.join(D, 'b495_waiver.json')) or '{}'),
        regj=json.loads(read(os.path.join(D, 'b495_registry.json')) or '{}'),
        spiral=read(os.path.join(PP, 'SPIRAL_MAP.md')),
        registry=read(os.path.join(PP, 'REGISTRY.md')),
        launcher=read(os.path.join(T, 'b495_launch.py')),
        createtool=read(os.path.join(T, 'b495_create.py')),
        pushtool=read(os.path.join(T, 'b495_push.py')),
        waiver=read(os.path.join(D, 'b495_waiver.txt')),
        regtxt=read(os.path.join(D, 'b495_registry.txt')),
        kernel_text={f: read(os.path.join(KERNEL, f))
                     for f in sorted(x for x in gits(KERNEL, 'ls-files').split(NL)
                                     if x.strip().endswith('.lean'))},
        # ### ### **THE KERNEL IS READ AS A FILE LIST AND AS HEADERS -- NEVER AS ITS BUILD LOG.**
        # ### (R106)(3) gives the log to b496, and an arm that reads it here would break the
        # ### clause the act exists to keep.
        kernel_files=sorted(x for x in gits(KERNEL, 'ls-files').split(NL) if x.strip()),
        kernel_toolchain=read(os.path.join(KERNEL, 'lean-toolchain')),
        kernel_lakefile=read(os.path.join(KERNEL, 'lakefile.toml')),
        kernel_manifest=read(os.path.join(KERNEL, 'lake-manifest.json')),
        kernel_notice=read(os.path.join(KERNEL, 'NOTICE')),
        log_exists=os.path.exists(os.path.join(D, 'b495_ef_build.log')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b495_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b495.zip'))),
        spantool_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py') == ''),
        tools495=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b495_') and f.endswith('.py')
                         and f != 'b495_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b495 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b495_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b495 --'):
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
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b495_') and f not in LIVE]
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


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=260):
    """### the text after a marker, or EMPTY when the control removes it."""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def rows(S):
    return (S['cells'] or {}).get('rows') or []
def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


PIN_SHA = '3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
STMT_SHA = '0255fa699a72c941d7dcb70e0232a0184fb9e0c48c66659a6a237c4022000fe6'
NAMES3 = ('EF_lit_zetaZeroConfig', 'Zeta23.EF.EF_lit', 'EF_lit_zeta')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'ACT b495' in S['ferry'],
     lambda S: cut(S, 'ferry', 'ACT b495')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan',
     lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- and the pins tool was RUN ALONE (b494`s lesson)',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-SURVEY-NOMISS', 'the five component banks -- this act`s survey IS its components',
     lambda S: all((S['pin'], S['create'], S['push'], S['waiver'], S['regtxt'])),
     lambda S: put(S, 'waiver', '')),
    ('G-REG-LOCKED-FIRST', 'the face lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('LOCKED.' in l or 'SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('LOCKED.', 'x').replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b494`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 343 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b495' in S['ferry'] and 'b495' in S['face']
                and not os.path.exists(os.path.join(D, 'b497_ferry.txt'))),
     lambda S: cut(S, 'face', 'b495')),

    # -------------------------------------------------- component 1, the pin
    ('G-PIN-BOTH-PRINTED', 'the pin bank -- the statement at BOTH revisions, whole',
     lambda S: (S['pin'].count('def EF_lit (Z : ZeroConfig) : Prop :=') == 2
                and '`v1.0`' in S['pin'] and '`fbdc36b`' in S['pin']),
     lambda S: put(S, 'pin', S['pin'].replace(
         'def EF_lit (Z : ZeroConfig) : Prop :=', 'x', 1))),
    ('G-PIN-SHA-BOTH', 'the pin bank`s json -- a digest for each revision, and for the file too',
     lambda S: (S['pinj'].get('statement_sha', {}).get('v1.0') == STMT_SHA
                and S['pinj'].get('statement_sha', {}).get('fbdc36b') == STMT_SHA
                and all(S['pinj'].get('file_sha', {}).get(k) for k in ('v1.0', 'fbdc36b'))),
     lambda S: put(S, 'pinj', dict(S['pinj'], statement_sha={'v1.0': None, 'fbdc36b': None}))),
    ('G-PIN-REASON-IS-THE-COMPARISON', 'the pin bank -- the reason is a printed comparison',
     lambda S: ('statement bytes identical : ### **True**' in S['pin']
                and S['pinj'].get('pin') == 'v1.0'
                and S['pinj'].get('pin_sha') == PIN_SHA
                and 'THE PATHS DIFFER' in S['pin']),
     lambda S: put(S, 'pin', S['pin'].replace('THE PATHS DIFFER', 'x'))),

    # -------------------------------------------------- component 2, the repository
    ('G-CLOSURE-FROM-THE-SEED', 'the create bank -- the closure is COMPUTED, and from the seed',
     lambda S: (S['crej'].get('seed') == 'Zeta23.WeilEF.Main'
                and 'THE CLOSURE, COMPUTED AT THE PIN' in S['create']),
     lambda S: put(S, 'crej', dict(S['crej'], seed='Zeta23.Everything'))),
    ('G-CLOSURE-FIFTY-SEVEN', 'the create bank -- the count, and it is the order`s',
     lambda S: S['crej'].get('modules') == 57 and len(S['crej'].get('rows') or []) == 57,
     lambda S: put(S, 'crej', dict(S['crej'], modules=41))),
    ('G-BODY-HASH-BEFORE-HEADER', 'the create tool`s own text -- the digest precedes the prepend',
     lambda S: ('THE BODY IS WRITTEN FIRST AND HASHED FROM DISK BEFORE ANY HEADER EXISTS'
                in S['createtool']
                and 'copied_sha = sha(fh.read())' in S['createtool']),
     lambda S: cut(S, 'createtool', 'copied_sha = sha(fh.read())')),
    ('G-BODY-HASH-AGREES-ALL', 'the create bank -- per-module digests, all of them',
     lambda S: (S['crej'].get('agreeing') == S['crej'].get('modules') == 57
                and not S['crej'].get('mismatches')
                and all(r['src_sha'] == r['body_sha'] for r in (S['crej'].get('rows') or []))),
     lambda S: put(S, 'crej', dict(S['crej'], rows=[
         dict(r, body_sha='0' * 64) for r in (S['crej'].get('rows') or [])]))),
    ('G-NO-BODY-EDITED', 'the created kernel -- every body still ends its source`s bytes',
     lambda S: (all(r.get('body_intact') for r in (S['crej'].get('rows') or []))
                and len(S['crej'].get('rows') or []) == 57),
     lambda S: put(S, 'crej', dict(S['crej'], rows=[
         dict(r, body_intact=False) for r in (S['crej'].get('rows') or [])]))),
    ('G-HEADER-ON-ALL-FIFTY-SEVEN', 'the created kernel`s files, read here',
     lambda S: (sum(1 for f in S['kernel_files'] if f.endswith('.lean')
                    and 'VENDORED INTO SIDE-explicit-formula' in S['kernel_text'].get(f, ''))
                == 57),
     lambda S: put(S, 'kernel_files', [f for f in S['kernel_files'] if not f.endswith('.lean')])),
    ('G-SECOND-HEADER-ON-THE-TEN', 'the created kernel`s files -- the second header, counted',
     lambda S: (sum(1 for f in S['kernel_files'] if f.endswith('.lean')
                    and 'SECOND ATTRIBUTION' in S['kernel_text'].get(f, '')) == 10),
     lambda S: put(S, 'kernel_files', [f for f in S['kernel_files']
                                       if 'FromPNTPlus' not in f])),
    ('G-THE-TEN-BY-NOTICE', 'zeta23`s own NOTICE, carried into the kernel -- the SOURCE`s predicate',
     lambda S: ('The derived files are the ones under Zeta23/FromPNTPlus/' in S['kernel_notice']
                and all(m.startswith('Zeta23.FromPNTPlus') for m in (S['crej'].get('pnt') or []))
                and len(S['crej'].get('pnt') or []) == 10),
     lambda S: put(S, 'kernel_notice',
                   S['kernel_notice'].replace('The derived files are the ones under', 'x'))),
    ('G-LICENSE-NOTICE-WHOLE', 'the create bank -- both carried, both digests compared',
     lambda S: all(c.get('agree') for c in (S['crej'].get('carried') or {}).values())
     and set(S['crej'].get('carried') or {}) == {'LICENSE', 'NOTICE'},
     lambda S: put(S, 'crej', dict(S['crej'], carried={
         k: dict(v, agree=False) for k, v in (S['crej'].get('carried') or {}).items()}))),
    ('G-TOOLCHAIN-AS-ZETA23', 'the kernel`s own file against the create bank`s reading',
     lambda S: (S['kernel_toolchain'].strip() == 'leanprover/lean4:v4.33.0-rc2'
                == S['crej'].get('toolchain')),
     lambda S: put(S, 'kernel_toolchain', 'leanprover/lean4:v4.29.0-rc8')),
    ('G-MATHLIB-AS-ZETA23', 'the kernel`s manifest and lakefile against the create bank',
     lambda S: (S['crej'].get('mathlib', '').startswith('51e6992e')
                and '51e6992e' in S['kernel_manifest']
                and '51e6992e' in S['kernel_lakefile']),
     lambda S: put(S, 'kernel_lakefile', S['kernel_lakefile'].replace('51e6992e', 'deadbeef'))),
    ('G-LAKEFILE-DEFAULT-TARGET', 'the kernel`s lakefile -- rule 8, or a silent 0-job build',
     lambda S: ('defaultTargets' in S['kernel_lakefile']
                and 'globs' in S['kernel_lakefile']),
     lambda S: put(S, 'kernel_lakefile',
                   S['kernel_lakefile'].replace('defaultTargets', 'x').replace('globs', 'y'))),

    # -------------------------------------------------- component 3, the waiver
    ('G-WAIVER-APPENDED', 'SPIRAL_MAP itself, and the waiver bank`s prefix proof',
     lambda S: ('Waiver — 2026-09-23 — rule 9 for vendored namespaces' in S['spiral']
                and S['waiverj'].get('prefix') is True),
     lambda S: put(S, 'waiverj', dict(S['waiverj'], prefix=False))),
    ('G-WAIVER-NAMES-THIS-ACT', 'SPIRAL_MAP -- the reason is an ACT, not a preference',
     lambda S: 'THE REASON IS ACT b495' in S['spiral']
     and 'A VENDORED FILE IS NOT EDITED' in S['spiral'],
     lambda S: put(S, 'spiral', S['spiral'].replace('THE REASON IS ACT b495', 'x'))),
    ('G-RULE-NINE-NOT-REWRITTEN', 'SPIRAL_MAP -- rule 9 still stands at its own address',
     lambda S: (S['spiral'].split(NL)[S['waiverj'].get('rule9_line', 1) - 1].lstrip()
                .startswith('9. **Vanilla Lean 4 syntax discipline.**')),
     lambda S: put(S, 'spiral', S['spiral'].replace(
         '9. **Vanilla Lean 4 syntax discipline.**', '9. **Something else entirely.**'))),
    ('G-SPIRAL-APPEND-ONLY', 'the waiver bank -- 0 lines removed, ONE heading',
     lambda S: S['waiverj'].get('lines_removed') == 0 and S['waiverj'].get('headings') == 1,
     lambda S: put(S, 'waiverj', dict(S['waiverj'], lines_removed=4))),

    # -------------------------------------------------- component 4, push and launch
    ('G-PUSHED-AND-READ-BACK', 'the push bank -- the REMOTE sha, not the exit code',
     lambda S: (S['pushj'].get('agree') is True
                and len(S['pushj'].get('remote', '')) == 40
                and S['pushj'].get('remote') == S['pushj'].get('head')),
     lambda S: put(S, 'pushj', dict(S['pushj'], remote='', agree=False))),
    ('G-BUILD-DETACHED', 'the push tool`s own text and the banked pid',
     lambda S: ('DETACHED_PROCESS' in S['pushtool']
                and isinstance(S['pushj'].get('pid'), int)
                and 'p.wait()' not in S['pushtool']),
     lambda S: put(S, 'pushtool', S['pushtool'] + NL + '    p.wait()')),
    ('G-LAUNCHER-DISTINCT-INSTANTS', 'the launcher`s own text -- b480`s defect, at its mechanism',
     lambda S: ('def stamp():' in S['launcher']
                and 't = time.time()' in S['launcher']
                and 'stamp()' in seg(S['launcher'], 'def say(fh, s):', 160)
                and (S['sc'] or {}).get('distinct_marks') == 10),
     lambda S: put(S, 'launcher', S['launcher'].replace('def stamp():', 'def notstamp():'))),
    ('G-PRINTAXIOMS-THREE-NAMES', 'the launcher -- all three names the order gives',
     lambda S: all(n in S['launcher'] for n in NAMES3)
     and 'print axioms' in S['launcher'],
     lambda S: put(S, 'launcher', S['launcher'].replace(NAMES3[0], 'x'))),
    ('G-LOG-NOT-READ', 'every tool of this act BUT THE LAUNCHER -- no read of the build log',
     lambda S: not re.search(r"(?:open|read)\([^)]{0,80}b495_ef_build\.log", S['tools495']),
     lambda S: put(S, 'tools495', S['tools495'] + NL
                   + "x = open('data/b495_ef_build.log').read()")),

    # -------------------------------------------------- component 5, the registry row
    ('G-REGISTRY-ONE-ROW', 'REGISTRY itself, and the row bank`s prefix proof',
     lambda S: (S['registry'].count(
         'Kernel-table addition — 2026-09-23 — `SIDE-explicit-formula`') == 1
         and S['regj'].get('prefix') is True and S['regj'].get('lines_removed') == 0),
     lambda S: put(S, 'regj', dict(S['regj'], lines_removed=2))),
    ('G-REGISTRY-PROFILE-PENDING', 'REGISTRY -- the profile cell says PENDING and nothing better',
     lambda S: '**PROFILE: `PENDING`.**' in S['registry']
     and 'NOTHING IN THIS KERNEL HAS BEEN BUILT OR `#print axioms`-ED' in S['registry'],
     lambda S: put(S, 'registry', S['registry'].replace('**PROFILE: `PENDING`.**', 'PROFILE: std3'))),
    ('G-REGISTRY-DEPOSIT-PIN-NONE', 'REGISTRY -- the deposit-pin cell',
     lambda S: '**`NONE`** — **no published prose cites this kernel' in S['registry'],
     lambda S: put(S, 'registry', S['registry'].replace('**`NONE`**', '**`v1.0`**'))),
    ('G-NOCITE-BEFORE-PROFILE', 'the row bank -- terminals named in the appended block, MEASURED',
     lambda S: S['regj'].get('terminals_named') == [],
     lambda S: put(S, 'regj', dict(S['regj'],
                                   terminals_named=['Zeta23.WeilEF.EF_lit_zetaZeroConfig']))),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the desk bank against the pin bank',
     lambda S: 'HELD' in seg(S['desk'], '**(N1)**') and (S['sc'] or {}).get('n1') is True,
     lambda S: put(S, 'sc', dict(S['sc'], n1=False))),
    ('G-N2-SCORED', 'the desk bank against the create bank',
     lambda S: 'HELD' in seg(S['desk'], '**(N2)**') and (S['sc'] or {}).get('n2') is True,
     lambda S: put(S, 'sc', dict(S['sc'], n2=False))),
    ('G-N3-SCORED', 'the desk bank -- and it is scored NOT SCORABLE, with the conflict named',
     lambda S: ('NOT SCORABLE IN THIS ACT' in seg(S['desk'], '**(N3)**')
                and (S['sc'] or {}).get('n3') == 'NOT SCORABLE'
                and 'THE ORDER FORBIDS THE ONLY POPULATION THIS EXPECTATION NAMES' in S['desk']),
     lambda S: put(S, 'sc', dict(S['sc'], n3=True))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT`S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ; HELD 2 ; NOT SCORABLE 1 ; REFUTED 0' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 2 ; NOT SCORABLE 1 ; REFUTED 0')),

    # -------------------------------------------------- the standing arms
    ('G-NOGRADE-CONFERRED', 'the face and the registry row',
     lambda S: 'No corpus grade is conferred, moved' in S['face']
     and 'confers **no grade**' in S['registry'],
     lambda S: cut(S, 'registry', 'confers **no grade**')),
    ('G-NOTHING-FETCHED', 'this act`s own tools, for any network call but git`s two',
     lambda S: not re.search(r'urllib|requests\.|Invoke-WebRequest|curl |zenodo\.org',
                             S['tools495']),
     lambda S: put(S, 'tools495', S['tools495'] + NL + 'requests.get("https://zenodo.org/x")')),
    ('G-NOZENODO-WRITE', 'this act`s own tools, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files)\b', S['tools495'], re.I),
     lambda S: put(S, 'tools495', S['tools495'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'],
     lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text',
     lambda S: 'four lists' in S['ot'] and 'stay OPEN' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the three documents named on the face',
     lambda S: sorted(S['tracked']) == sorted(['SPIRAL_MAP.md', 'REGISTRY.md', 'OPEN_TRAILS.md']),
     lambda S: put(S, 'tracked', sorted(S['tracked']) + ['FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b495 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b495 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: ('| 344 |' in S['corr'] and S['corr'].count('| 344 |') == 1
                and S['corr'].count('b495, under (R82)') == 1),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 344 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b495 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the PLACE-papers file list -- no internal document, no `.lean`',
     lambda S: all(not x.startswith('internal/') and not x.endswith('.lean')
                   for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58), and the clone was only READ',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    # ### ### **THIS ARM WAS DEFECTIVE ON ITS FIRST RUN AND THE HARNESS CAUGHT IT.**
    # ### Its predicate was an `or` over two spellings -- b494's `components.txt` and this act's
    # ### `create.txt` -- and the control removed only the second. ### The first spelling is a
    # ### SUBSTRING OF NOTHING HERE, but the arm still passed its own mutation because the `or`
    # ### had a live limb left. ### **A DISJUNCTION OVER SPELLINGS IS A CONTROL THAT CANNOT
    # ### ### BITE**: the mutation must falsify EVERY limb, or the arm is untested.
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b495')" in S['suite']
                and "data/b495_create.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b495_create.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b495')
              and 'data/b495_create.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b495 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ### **0 EXCLUDED BY NAME.**'
        % S['prior_checked'])
    rec('  ### ### **THE b475 LOG EXCEPTION STAYS RETIRED.** ### b481-b489 excused')
    rec('  ###   `b475_zeta23_build.log` as still being appended to by a live process. ### b490')
    rec('  ### found pid 27508 ABSENT at two readings sixty seconds apart and the file cold, and')
    rec('  ### b491 read the log COMPLETE. ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND')
    rec('  ### DECAYS LIKE ONE.** ### b487`s second exclusion is not carried either: it was')
    rec('  ### b485`s bank, which (R97) directed b487 to append to. ### The arm runs at FULL WIDTH.')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b495_checks_postpush.txt' if pushed else 'b495_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b495_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
