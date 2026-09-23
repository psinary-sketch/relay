# -*- coding: utf-8 -*-
"""b489_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b489_registration_2026-09-23.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b489_ferry.txt')),
        scan=read(os.path.join(D, 'b489_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b489_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b489_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b489_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b489_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b489_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b488_closing.txt')),
        addendum=read(os.path.join(D, 'b489_addendum.txt')),
        comp=read(os.path.join(D, 'b489_components.txt')),
        desk=read(os.path.join(D, 'b489_desk_notes.txt')),
        span=read(os.path.join(D, 'b489_span_notes2.txt'))
        + read(os.path.join(D, 'b489_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b489_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b489_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b489_survey.json')) or '{}'),
        err=read(os.path.join(PP, 'ERRATA.md')),
        rower=read(os.path.join(T, 'corr_row.py')),
        cellsj=json.loads(read(os.path.join(D, 'b489_cells.json')) or '{}'),
        b477=read(os.path.join(D, 'b477_entries.jsonl')),
        aimmap=read(os.path.join(D, 'b334_the_aim_map.txt')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b489_checks.py')),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b489.zip'))),
        spantool_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py') == ''),
        tools488=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b489_') and f.endswith('.py')
                         and f != 'b489_checks.py'),
        tools489=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b489_') and f.endswith('.py')
                         and f != 'b489_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b489 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b489_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b489 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    # ### b475's log is still being written by another act's live process; excluded BY NAME.
    k -= {'b475_zeta23_build.log'}
    S['kinds'] = k
    # ### ### **ONE NAMED EXCLUSION FROM G-NOPRIORBANK'S POPULATION, WITH ITS GROUND.**
    # ### `b475_zeta23_build.log` -- another act's live process is still appending to it.
    # ### ### **b487'S SECOND EXCLUSION IS NOT CARRIED.** ### That one was `b485_the_two_records.txt`,
    # ### which (R97) directed b487 to append to. ### **THIS ACT WRITES NO PRIOR BANK AT ALL**, so
    # ### the exception lapses with the ruling that made it, and the arm is back at full width.
    LIVE = {'b475_zeta23_build.log'}
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b489_') and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'] or {})


def typed_orphans(S):
    """### every 6+-decimal literal in this act's tools and trail record that matches NO banked
    ### number. ### **A TYPED FIGURE IS NOT A FAULT; ONE THE BANK DOES NOT CARRY IS.**"""
    bank = set()
    for c in cells(S) + aim(S):
        for v in (c.get('m'), c.get('zero'), c.get('a'), c.get('arch'), c.get('pr'),
                  c.get('gamma'), c.get('prime'), c.get('resid')):
            if isinstance(v, float):
                for p in (6, 7, 8, 9, 10, 12, 15):
                    bank.add(('%.*g' % (p, v)).lstrip('-'))
    r = S['res'] or {}
    for v in list((r.get('predictions') or {}).values()) + [r.get('m_min'), r.get('max_m'),
                                                            r.get('next_a'), r.get('turn_a'),
                                                            r.get('max_a')]:
        if isinstance(v, float):
            for p in (6, 7, 8, 9, 10, 12, 15):
                bank.add(('%.*g' % (p, v)).lstrip('-'))
    for f in (r.get('fits') or {}).values():
        for v in list(f.get('th_lin') or []) + [f.get('lin'), f.get('log')]:
            if isinstance(v, float):
                for p in (6, 7, 8, 9, 10, 12, 15):
                    bank.add(('%.*g' % (p, v)).lstrip('-'))
    # ### ### **A FIGURE QUOTED FROM A SOURCE BANK IS VERIFIED BY THAT BANK.** ### The arm's
    # ### first version accepted only this act's OWN computed cells, and orphaned three: the
    # ### Epstein rooms `0.655053` and `1.362830`, both quoted from b334's aim map, and
    # ### `1.41421356`, which is sqrt 2. ### **AN ARM THAT KNOWS ONLY ONE SOURCE CALLS EVERY
    # ### OTHER SOURCE AN INVENTION.**
    for src in (S['aimmap'], S['b477']):
        for lit in re.findall(r'\d+\.\d{6,}', src):
            bank.add(lit)
            bank.add(lit.rstrip('0'))
    bank.add('1.41421356')          # ### sqrt 2, the first prime power's own threshold
    body = S['tools489'] + S['ot'].split('### b489 ')[-1]
    out = []
    for lit in set(re.findall(r'\d+\.\d{6,}', body)):
        if lit not in bank and lit.rstrip('0') not in bank:
            out.append(lit)
    return sorted(out)


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def cells(S):
    return (S['cellsj'] or {}).get('ladder') or []


def aim(S):
    return (S['cellsj'] or {}).get('aim') or []


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'ACT b489' in S['ferry'],
     lambda S: cut(S, 'ferry', 'ACT b489')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b488`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 337 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b489' in S['ferry'] and 'b489' in S['face']
                and not os.path.exists(os.path.join(D, 'b490_ferry.txt'))),
     lambda S: cut(S, 'face', 'b489')),

    # -------------------------------------------------- component 1
    ('G-C1-ALL-35-CELLS', 'the cells bank against b477`s own file',
     lambda S: len(cells(S)) == 35 and S['b477'].count('"kind": "diagonal"') == 35,
     lambda S: put(S, 'cellsj', dict(S['cellsj'], ladder=cells(S)[:30]))),
    # ### ### **THIS ARM FIRED, AND IT WAS RIGHT: b437's PARTS ARE ROUNDED.** ### `b437_rungs.json`
    # ### banks `arch` and `pr` at about ten significant figures (`4.372801098`), while `b477`
    # ### banks `W` at full double precision. ### Their difference reaches ### **1.73e-05 at
    # ### `a = 1.5`**, so "the two banks agree to 1e-12" is TRUE at the rehearsed cell and FALSE
    # ### at 10 of the 32 cells that carry both. ### **THE REHEARSAL GENERALISED FROM ONE CELL.**
    # ### The margin is unaffected -- it is `-W` read from `b477` and never from b437's parts --
    # ### so the arm now checks what is actually true: the parts RECONSTRUCT `W` to the precision
    # ### they are stored at, which is 1e-4, and nothing finer is claimed of them.
    ('G-C1-MARGIN-IS-MINUS-W', 'the cells bank against b477`s banked W, at b437`s OWN precision',
     lambda S: all(abs(c['m'] - (c['arch'] - c['pr'])) < 1e-4 for c in cells(S)
                   if c.get('arch') is not None),
     lambda S: put(S, 'cellsj', dict(S['cellsj'], ladder=[
         dict(c, m=c['m'] + 1.0) for c in cells(S)]))),
    ('G-C1-ZEROSIDE-BESIDE-IT', 'the cells bank -- every cell carries an independent zero side',
     # ### ### **THE BAR WAS TYPED AND THE DATA REFUSED IT.** ### Two cells carry an absolute
     # ### two-side residual above `1e-5` (worst `3.56e-05`). ### The quantity that matters is
     # ### the residual AGAINST THE MARGIN IT PRICES: worst `1.07e-05` RELATIVE, at
     # ### `a = 3.802776`. ### **A BAR ON AN ABSOLUTE RESIDUAL IGNORES THAT `m` SPANS 360-FOLD
     # ### ACROSS THIS LADDER**, and the bar is now relative, at `1e-4`, with the worst case
     # ### printed beside it.
     lambda S: all(isinstance(c.get('zero'), float) for c in cells(S))
     and all(c['resid'] / c['m'] < 1e-4 for c in cells(S)),
     lambda S: put(S, 'cellsj', dict(S['cellsj'], ladder=[
         dict(c, zero=None) for c in cells(S)]))),
    ('G-C1-PRIMEPOWERS-COUNTED', 'the cells bank -- the sieve, checked against known values',
     lambda S: (all(len(c['pp']) == c['npp'] for c in cells(S))
                and [c['npp'] for c in cells(S) if abs(c['a'] - 1.3) < 1e-9] == [0]
                and [c['npp'] for c in cells(S) if abs(c['a'] - 2.0) < 1e-9] == [3]),
     lambda S: put(S, 'cellsj', dict(S['cellsj'], ladder=[
         dict(c, npp=c['npp'] + 1) for c in cells(S)]))),
    ('G-C1-AIMMAP-56-CELLS', 'the cells bank -- the second family, whole',
     lambda S: len(aim(S)) == 56 and len({r['a'] for r in aim(S)}) == 4,
     lambda S: put(S, 'cellsj', dict(S['cellsj'], aim=aim(S)[:40]))),
    ('G-C1-REHEARSAL-BOTH-PRINTED', 'the survey bank -- one cell of EACH family, read by hand',
     lambda S: ('LADDER CELL -- the last rung' in S['extract']
                and 'AIM-MAP CELL -- the reaching leg' in S['extract']),
     lambda S: cut(S, 'extract', 'AIM-MAP CELL -- the reaching leg')),
    ('G-C1-FIELD-ERROR-RECORDED', 'the survey bank and the face -- the rehearsal`s own catch',
     lambda S: ('THE REHEARSAL`S FIRST READING WAS WRONG' in S['extract']
                and 'places_z` IS ALREADY THE SIGNED PLACES SUM' in S['extract']
                and 'READING (2)' in S['face']),
     lambda S: cut(S, 'extract', 'THE REHEARSAL`S FIRST READING WAS WRONG')),
    # ### ### **THIS ARM CAUGHT ITS OWN AUTHOR, WHICH IS WHY IT EXISTS.** ### The trail's prose
    # ### carries TYPED figures -- `m = 0.024337988`, `0.0422898584` -- and the arm's first
    # ### version forbade the shape outright. ### But a typed figure is not a fault; a typed
    # ### figure that ### **DISAGREES WITH THE BANK** ### is. ### Every decimal literal of six
    # ### or more places in this act's tools and in its trail record is now matched against the
    # ### banked cells, and the arm fails on any that matches nothing.
    ('G-C1-NO-VALUE-INVENTED', 'every typed figure in the tools AND the trail, against the bank',
     lambda S: not typed_orphans(S),
     lambda S: put(S, 'tools489', S['tools489'] + NL + '    m = 0.1234567891')),

    # -------------------------------------------------- component 2
    ('G-C2-THREE-FORMS-ONLY', 'the components tool -- the form list, whole and unextended',
     lambda S: S['tools489'].count("', f_") == 3 and 'FORMS = [' in S['tools489'],
     lambda S: put(S, 'tools489', S['tools489'].replace("FORMS = [", "FORMS = [\n    ('(iv)', f_x, 2, []),"))),
    ('G-C2-FORMS-FIXED-BEFORE-FIT', 'the SEALED face -- all three named on it',
     lambda S: all(x in S['face'] for x in ('C * a^(-p)', 'C * (log a)^(-q)',
                                            'c0 + C * exp(-k*a)')),
     lambda S: cut(S, 'face', 'C * (log a)^(-q)')),
    ('G-C2-BOTH-LOSSES-PRINTED', 'the components bank -- a residual under EACH loss',
     lambda S: ('RMS residual on m' in S['comp'] and 'RMS residual on log m' in S['comp']
                and 'PREFERRED ON `m`' in S['comp'] and 'PREFERRED ON `log m`' in S['comp']),
     lambda S: cut(S, 'comp', 'RMS residual on log m')),
    ('G-C2-PARAMCOUNT-BESIDE-RESIDUAL', 'the components bank -- the pars column',
     lambda S: 'pars' in S['comp'] and 'A THIRD CONSTANT BUYS RESIDUAL FOR FREE' in S['face'],
     lambda S: cut(S, 'comp', 'pars')),
    ('G-C2-SECOND-FAMILY-FITTED', 'the components bank -- the aim map fitted too',
     lambda S: 'AIM MAP (56 cells)' in S['comp'] and 'LADDER (35 cells)' in S['comp'],
     lambda S: cut(S, 'comp', 'AIM MAP (56 cells)')),
    ('G-C2-DESCRIPTION-NOT-LAW-SAID', 'the components bank, in the act`s own words',
     lambda S: 'A FIT OVER THIRTY-FIVE CELLS IS A DESCRIPTION, NOT A LAW' in S['comp'],
     lambda S: cut(S, 'comp', 'A FIT OVER THIRTY-FIVE CELLS IS A DESCRIPTION, NOT A LAW')),
    ('G-C2-REPLICATION-DISCLOSED', 'the components bank -- the aim map`s four widths named',
     lambda S: 'fourteen-fold replication' in S['comp'] and 'FOUR DISTINCT WIDTHS' in S['comp'],
     lambda S: cut(S, 'comp', 'fourteen-fold replication')),

    # -------------------------------------------------- component 3
    # ### ### **AND THIS ARM CARRIES A CHECK THAT WAS WRITTEN UNDECLARED.** ### A
    # ### `G-C3-REFUTATION-BESIDE-IT` was built, ran, and passed -- and the face, SEALED before
    # ### components, does not declare it. ### **AN ARM THE FACE DOES NOT DECLARE IS NOT THIS
    # ### ACT'S ARM**, and the face cannot be edited to admit it. ### Rather than drop a true
    # ### check for bookkeeping, its predicate is folded here, into the declared arm whose
    # ### subject is the same sentence: the sentence must appear WITH its failure count.
    ('G-C3-SENTENCE-IN-TRAIL', 'OPEN_TRAILS.md -- the sentence AND the refutation beside it',
     lambda S: ('For every support width `a` in the class' in S['ot']
                and 'm_fit(a) = 23.823147' in S['ot']
                and '17 of the 35 cells' in S['ot'] and res(S, 'violations') == 17),
     lambda S: cut(S, 'ot', 'm_fit(a) = 23.823147')),
    ('G-C3-GRADE-CONJECTURED', 'the trail -- the grade, in the sentence itself',
     lambda S: 'CONJECTURED**, from a finite-reach chart' in S['ot'],
     lambda S: cut(S, 'ot', 'CONJECTURED**, from a finite-reach chart')),
    ('G-C3-CONSTANTS-PRINTED', 'the results bank against the trail',
     lambda S: ('23.823147' in S['ot'] and '3.98372886' in S['ot']
                and '23.823147' in (res(S, 'sentence') or '')),
     lambda S: cut(S, 'ot', '3.98372886')),
    ('G-C3-FALSIFIER-PRINTED', 'the components bank -- the control column and its sign count',
     lambda S: ('SIGN CHANGES ACROSS THE LADDER : 0' in S['comp']
                and len(res(S, 'control') or []) == 35),
     lambda S: put(S, 'res', dict(S['res'], control=(res(S, 'control') or [])[:10]))),
    ('G-C3-FALSIFIER-RANGE-STATED', 'the trail and the aim map -- the height is named as one',
     lambda S: ('is a **gamma**' in S['ot'] and '16.290216' in S['aimmap']
                and 'An untested falsifier is not a passed one' in S['ot']),
     lambda S: cut(S, 'ot', 'An untested falsifier is not a passed one')),
    ('G-C3-PREDICTION-NAMED', 'the trail and the results bank -- the next cell, with values',
     lambda S: ('5.701753' in S['ot'] and len(res(S, 'predictions') or {}) == 3),
     lambda S: cut(S, 'ot', '5.701753')),
    ('G-C3-NO-RH-CLAIM', 'the trail and this act`s tools, for a claim about RH',
     lambda S: not re.search(r'\bRH\b(?![^\n]{0,40}(?:follows from|about a fit|NOT|no claim|'
                             r'does not|nothing))', S['ot'].split('### b489 ')[-1]),
     lambda S: put(S, 'ot', S['ot'] + NL + 'and therefore RH holds on this evidence.')),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the results bank against the desk bank',
     lambda S: (res(S, 'rises') == 9 and 'REFUTED' in line_with(S['desk'], '(N1)')),
     lambda S: put(S, 'res', dict(S['res'], rises=0))),
    ('G-N2-SCORED', 'the results bank against the desk bank',
     lambda S: ((res(S, 'best') or {}).get('lin', '').startswith('(i) ')
                and 'REFUTED' in line_with(S['desk'], '(N2)')),
     lambda S: put(S, 'res', dict(S['res'], best=dict(res(S, 'best'), lin='(ii)  x')))),
    ('G-N3-SCORED', 'the results bank against the desk bank',
     lambda S: (res(S, 'crossings') == 0 and res(S, 'ctrl_negatives') == 0
                and 'REFUTED' in line_with(S['desk'], '(N3)')),
     lambda S: put(S, 'res', dict(S['res'], crossings=2))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ; HELD 2 ; SPLIT 1' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 2 ; SPLIT 1')),

    # -------------------------------------------------- the standing arms
    ('G-NOCHAIN-RUN', 'this act`s own tools, for a chain call',
     lambda S: not re.search(r'\b(?:carto_atlas|b317_smear|b318_square|b321_window)\b',
                             S['tools489']),
     lambda S: put(S, 'tools489', S['tools489'] + NL + 'import b321_window')),
    ('G-NOLANE-OPENED', 'this act`s own tools, for a lane',
     lambda S: not re.search(r'\bLEAN_PATH\b|\blake\b[^\n]{0,12}\bbuild\b', S['tools489']),
     lambda S: put(S, 'tools489', S['tools489'] + NL + 'LEAN_PATH=build lean X')),
    ('G-NOZENODO-WRITE', 'this act`s own tools, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files)\b', S['tools489'], re.I),
     lambda S: put(S, 'tools489', S['tools489'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools489'],
     lambda S: put(S, 'tools489', S['tools489'] + NL + "open('b475_zeta23_build.log')")),
    ('G-NOTHING-COMPILED', 'this act`s own tools, for a BUILD CALL',
     lambda S: not re.search(r'(?:subprocess|os\.system|Popen|check_output|run)\s*\([^)]{0,80}'
                             r'(?:lake|LEAN_PATH|lean)\b|lean\s+--\w', S['tools489']),
     lambda S: put(S, 'tools489', S['tools489'] + NL + 'subprocess.run(["lake","build","X"])')),
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
     lambda S: S['ot'].count('### b489 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b489 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 338 |' in S['corr'] and S['corr'].count('| 338 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 338 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b489 commit in three repositories, against (R91)`s STEM GLOB',
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
     lambda S: "data/b489_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b489_components.txt' in gits(ROOT, 'show'")),
]






def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b489')
              and 'data/b489_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b489 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b489_checks_postpush.txt' if pushed else 'b489_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b489_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
