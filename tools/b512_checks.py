# -*- coding: utf-8 -*-
"""b512_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b512's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The kernel arms read the kernel's own tree and git state, not the act's report.
"""
import io
import glob
import hashlib
import fnmatch
import json
import math
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
FACE = os.path.join(D, 'b512_registration_2026-09-24.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '8dc5e1ca'      # ### b512's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_PRIOR = '2255b3f'         # ### the kernel's tip before this act
MODF = os.path.join(KER, 'SIDEExplicitFormula', 'Registers.lean')
PRIOR_PP = '0c90879'           # ### b511's PLACE-papers commit
FIND = os.path.join(PP, 'FINDINGS.md')
DIG = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
NL = chr(10)
NOTEF = ('b489_components.txt', 'b490_components.txt', 'b502_components.txt', 'b503_components.txt', 'b504_components.txt')
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b512 —'
CROSS = re.compile(r'(?i)\bwidths?\s+(?:of\s+)?(?:40|81)\b|\b40 and 81\b|\(\s*(?:40|81)\s*,|\ba\s*=\s*(?:40|81)\b')


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


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


def flat(s):
    return (s or '').replace(NL + '### ', ' ').replace(NL, ' ')


def jl(name):
    return sorted((json.loads(l) for l in read(os.path.join(D, name)).split(NL) if l.strip()), key=lambda c: c['a'])


def sources():
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b512_ferry.txt')),
        scan=read(os.path.join(D, 'b512_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b512_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b512_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b512_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b512_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b508_closing.txt')),
        addendum=read(os.path.join(D, 'b512_addendum.txt')),
        comp=read(os.path.join(D, 'b512_components.txt')),
        desk=read(os.path.join(D, 'b512_desk_notes.txt')),
        stmt=read(os.path.join(D, 'b512_statement.txt')), defs=read(os.path.join(D, 'b512_definitions.txt')),
        prof=json.loads(read(os.path.join(D, 'b512_profile.json')) or '{}'),
        plog=read(sorted(glob.glob(os.path.join(D, 'b512_profile_log*.txt')))[-1]) if glob.glob(os.path.join(D, 'b512_profile_log*.txt')) else '',
        clogs=''.join(read(x) for x in sorted(glob.glob(os.path.join(D, 'b512_compile_log*.txt')))),
        tb=json.loads(read(os.path.join(D, 'b512_table.json')) or '{}'), tbtxt=read(os.path.join(D, 'b512_table.txt')),
        notes=json.loads(read(os.path.join(D, 'b512_notes.json')) or '[]'),
        notefiles={n: read(os.path.join(D, n)) for n in NOTEF}, ft=read(FIND), dg=read(DIG),
        notes_prefix=all(open(os.path.join(D, n), 'rb').read().replace(bytes([13, 10]), bytes([10])).startswith(blob(ROOT, PRIOR_RELAY + ':data/' + n))
                         for n in NOTEF) and open(FIND, 'rb').read().startswith(blob(PP, PRIOR_PP + ':FINDINGS.md')),
        sc=json.loads(read(os.path.join(D, 'b512_scores.json')) or '{}'),
        mod=read(MODF),
        ker_vendored_changed=gits(KER, 'diff', '--name-only', KER_PRIOR, '--', 'Zeta23', 'LICENSE', 'NOTICE', 'lakefile.toml',
                                  'SIDEExplicitFormula/B321Identity.lean', 'SIDEExplicitFormula/H2Sign.lean', 'AxiomCheck.lean'),
        ker_tracked=sorted(x for x in gits(KER, 'diff', '--name-only', KER_PRIOR).split(NL) if x.strip())
        + sorted(p[3:].strip() for p in git(KER, 'status', '--porcelain').split(NL) if p.startswith('??')),
        ker_tags=gits(KER, 'tag', '--points-at', 'HEAD'),
        table=read(os.path.join(D, 'terminal_table.md')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b512_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b512.zip'))),
        chain_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py', 'tools/e16/carto_atlas.py',
                          'tools/b326_closure.py', 'tools/b325_epstein.py', 'tools/b326_windows.py',
                          'tools/b504_chain.py', 'tools/b506_kernel.py') == ''),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b512 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b512_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE) for p in (MODF, os.path.join(D, 'b512_notes.json'), os.path.join(D, 'b512_table.json'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b512 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                try:
                    if os.path.getmtime(os.path.join(repo, rel)) < os.path.getmtime(FACE):
                        continue
                except OSError:
                    pass
                k.add(os.path.basename(rel))
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[01]_|^b334_', f) and f not in NOTEF]
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
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS.

    ### ### **THE CORPUS WRITES A POSSESSIVE WITH A BACKTICK** -- `this act`s record`, `b496`s
    ### face`, `(R108)`s first line` -- a convention adopted so that ground strings survive being
    ### written into Python. ### ### **EVERY SUCH POSSESSIVE MAKES THE BACKTICK COUNT ODD**, and a
    ### naive `` `([^`]+)` `` pairing then DESYNCHRONISES: it pairs the closing backtick of one
    ### path with the possessive of the next sentence and returns a multi-line blob of prose as
    ### though it were a glob.
    ### ### **MEASURED ACROSS THE LAST FIVE FACES: b493 EVEN (0 malformed), b494 EVEN (0), b495
    ### ### ODD (5 malformed), b496 ODD (4), b497 ODD (6).** ### So `G-WRITELIST-KINDS` has been
    ### reading a partly-garbled glob list for three acts, and at b497 it reported a file
    ### UNDECLARED that the face declares by name in its own (W).
    ### ### **THE REPAIR IS TO PAIR WITHIN A LINE AND TO KEEP ONLY WHAT LOOKS LIKE A PATH.**
    ### A glob has no spaces and no newlines; a possessive's neighbourhood has both.
    ### ### **THIS WIDENS NOTHING.** ### It lets the tool read declarations that were already
    ### written; a file the face does not name is still uncovered.
    """
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    out = []
    for line in w.split(NL):
        for g in re.findall(BT + '([^' + BT + NL + ']+)' + BT, line):
            g = g.strip()
            if not g or ' ' in g or len(g) > 120:
                continue          # ### prose, not a path
            if not re.match(r'^[A-Za-z0-9_./*?\[\]{}-]+$', g):
                continue
            out.append(g.split('/')[-1])
    return out


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

def top_level_assign(text):
    """### ### **IS THERE A `:=` AT BRACKET DEPTH 0?** ### `(C := C)` is a NAMED ARGUMENT and
    ### `let n := c.1` inside a `fun` is a binding; neither hands a declaration to its proof."""
    depth = 0
    i = 0
    while i < len(text) - 1:
        c = text[i]
        if c in '([{':
            depth += 1
        elif c in ')]}':
            depth -= 1
        elif c == ':' and text[i + 1] == '=' and depth <= 0:
            return True
        i += 1
    return False


def strip_prose(text):
    """### ### **A `G-NO*` ARM MUST NOT READ THE ACT'S OWN SENTENCE SAYING IT DID NOT DO IT.**

    ### The trail writer holds its record in a module-level string; scanning that string for the
    ### forbidden word finds the DENIAL. ### This removes triple-quoted blocks and comments, so
    ### what remains is CODE, which is the only place a call can be. ### b487 minted this rule and
    ### this act re-learned it by being caught twice on one run.
    """
    t = re.sub(r'"""[\s\S]*?"""', ' ', text or '')
    t = re.sub(r"'''[\s\S]*?'''", ' ', t)
    t = re.sub(r'^\s*#.*$', ' ', t, flags=re.M)
    return t


def live_limb_guard(suite):
    """### ### **THE GUARD AGAINST A CONTROL THAT LEAVES A LIVE LIMB, AND WHERE IT ACTUALLY IS.**

    ### b495's `G-PUSHED-PREDICATE-THREE-CLAUSED` passed its own positive control because its
    ### predicate was `A or B` and the mutation falsified only `B`. ### This act declared a new arm
    ### to catch that species BY READING THE SUITE'S TEXT, and ### **FOUR REVISIONS LATER THE
    ### ### TEXTUAL PROXY STILL COULD NOT DO IT**: it fired on `x or []` none-defaults, on the word
    ### `or` inside quoted strings, on its own source, and on `any(A or B for ...)` whose control
    ### DOES falsify both limbs.
    ### ### **THE REASON IS THAT THE PROPERTY IS NOT TEXTUAL.** ### Whether a control falsifies
    ### every limb is a fact about what the control DOES, and the only thing that can decide it is
    ### ### **RUNNING THE CONTROL** -- which this harness already does for every arm, and whose
    ### result is the `POS` column and the `POSITIVE-CONTROL PASSES` count. ### **b495 WAS CAUGHT
    ### ### BY THAT COLUMN AND BY NOTHING ELSE.**
    ### So this arm no longer proxies. ### It asserts that the guard IS RUN: that the harness
    ### exercises a positive control on every arm, counts the passes, and ### **FAILS THE WHOLE
    ### ### SUITE ON A SINGLE ONE.**
    """
    need = ['p = bool(pred(pos(S)))',
            'defective.append(name)',
            'not defective']
    return [n for n in need if n not in suite]


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def tb(S, k, d=None):
    return (S['tblj'] or {}).get(k, d)


def cnt(S, k, d=None):
    return ((S['tblj'] or {}).get('counts') or {}).get(k, d)


def trows(S):
    return (S['tblj'] or {}).get('rows') or []








def c2(S, k, d=None):
    return (S['c2'] or {}).get(k, d)


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def c2_closed(S):
    f = c2(S, 'found') or []
    return (c2(S, 'not_near') == 0 and all(c2(S, 'control') or [False]) and all(z.get('inside') for z in f)
            and all(z.get('rho') and z.get('route_a', 1) < 1e-10 for z in f) and abs(c2(S, 'whole', 0) - c2(S, 'total', -9)) < 0.05)


def least_nv(L):
    nv = 8193
    while 2 * math.pi * (nv - 1) / L <= 350.0:
        nv += 1
    return nv


def population(S):
    return [c for c in S['cells'] if c['tail_inside']]


def log_span(log):
    ts = re.findall(r'^\[(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)\]', log, re.M)
    if not ts:
        return None
    import datetime
    f = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    return (f(ts[-1]) - f(ts[0])).total_seconds()


def edge_secs(log):
    m = re.findall(r'edges 1051 / 1051  (\d+) s', log)
    return int(m[-1]) if m else -1

def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


STD3N = "'SIDEExplicitFormula.B321.h2_sign_imp_cell' depends on axioms: [propext, Classical.choice, Quot.sound]"
MARKN = 'NOTE APPENDED AT b512 UNDER (R121)(1)'


def c1(S, k):
    return next((r for r in (S['tb'].get('C1') or []) if r['key'] == k), {})


def c2(S, p):
    return next((r for r in (S['tb'].get('C2') or []) if r['pair'] == p), {})


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R121) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b512' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan', lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b511`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 360 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 360 |', '| 3600 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b512' in S['ferry'] and 'ACT b512' in S['face'] and not glob.glob(os.path.join(D, 'b513_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b512')),
    ('G-PEEK-DECLARED', 'the face`s (C) block AND the component records` times against the lock',
     lambda S: 'NO LEAN FILE WAS WRITTEN INTO THE KERNEL, NOTHING WAS COMPILED, AND NO NOTE WAS APPENDED' in flat(S['face'])
     and 'as a `to_additive` name' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R121-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R121) END' in S['ferry'] and S['ot'].count('**(R121) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R121) ratified', '(R121) noted'))),
    ('G-NOTES-WITHDRAWN', 'each noted bank and FINDINGS -- ONE note, after the text, saying WITHDRAWN',
     lambda S: all(S['notefiles'][n].count(MARKN) == 1 and 'WITHDRAWN AS WINDOW ARTEFACTS' in S['notefiles'][n][S['notefiles'][n].index(MARKN):]
                   for n in NOTEF) and S['ft'].count('Note appended at b512 under `(R121)(1)`') == 1
     and S['ft'].rindex('Note appended at b512') > S['ft'].rindex('— THE FOLD'),
     lambda S: put(S, 'notefiles', dict(S['notefiles'], **{'b503_components.txt': S['notefiles']['b503_components.txt'].replace('WITHDRAWN AS WINDOW ARTEFACTS', 'kept')}))),
    ('G-NOTES-PREFIX', 'the notes record AND the committed blobs at b511`s close -- prefixes proved',
     lambda S: len(S['notes']) == 6 and all(n['prefix'] and n['removed'] == 0 and n['marks'] == 1 for n in S['notes']) and S['notes_prefix'],
     lambda S: put(S, 'notes_prefix', False)),
    ('G-DIGEST-UNNOTED', 'the digest -- no b512 note, and none of the withdrawn readings in it',
     lambda S: 'b512' not in S['dg'] and not re.search(r'turning points|three extrema|13\.15', S['dg']),
     lambda S: put(S, 'dg', S['dg'] + ' three extrema')),
    ('G-RULE9-THEOREM', 'the module`s text -- no `lemma` keyword', lambda S: not re.search(r'^\s*lemma\s', S['mod'], re.M) and bool(S['mod']),
     lambda S: put(S, 'mod', S['mod'] + NL + 'lemma x : True := trivial')),
    ('G-VENDORED-UNTOUCHED', 'the kernel`s git state -- nothing but the new module changed',
     lambda S: S['ker_vendored_changed'] == '' and set(S['ker_tracked']) == {'SIDEExplicitFormula/Registers.lean'},
     lambda S: put(S, 'ker_vendored_changed', 'Zeta23/ExplicitFormula.lean')),
    ('G-ONE-THEOREM', 'the module`s text -- exactly one theorem, the specialisation',
     lambda S: re.findall(r'^theorem (\S+)', S['mod'], re.M) == ['h2_sign_imp_cell'],
     lambda S: put(S, 'mod', S['mod'] + NL + 'theorem rh_h2 : True := trivial')),
    ('G-PROFILE-WHOLE-STRING', 'the profile run file -- the theorem`s line equal to the standard-three string',
     lambda S: [l.strip() for l in S['plog'].split(NL) if l.startswith("'SIDEExplicitFormula.B321.h2_sign_imp_cell'")] == [STD3N]
     and S['prof'].get('new_std3') is True,
     lambda S: put(S, 'plog', S['plog'].replace(STD3N, STD3N.replace(', Quot.sound', '')))),
    ('G-NO-SORRY', 'Lean`s own output in the compile and profile run files, and the module text',
     lambda S: bool(S['clogs']) and all("declaration uses 'sorry'" not in t and 'sorryAx' not in t and ': error' not in t for t in (S['plog'], S['clogs']))
     and not re.search(r'\bsorry\b', S['mod']),
     lambda S: put(S, 'clogs', S['clogs'] + "warning: declaration uses 'sorry'")),
    ('G-STATABLE-COMPILED', 'the table against the module -- every STATABLE row`s statement in the compiled module',
     lambda S: all(r['statement'] and r['statement'].split(NL)[0] in (S['mod'] + read(os.path.join(KER, 'SIDEExplicitFormula', 'H2Sign.lean')))
                   for r in (S['tb'].get('C1') or []) if r['status'] == 'STATABLE') and bool(S['tb'].get('C1')),
     lambda S: put(S, 'tb', dict(S['tb'], C1=[dict(r, statement='def ghost : Prop := True') if r['status'] == 'STATABLE' else r for r in S['tb'].get('C1') or []]))),
    ('G-ABSENT-SEARCHED', 'every NOT STATABLE row -- its missing object named and its needles` yields printed',
     lambda S: all(r.get('missing') and r.get('search') for r in (S['tb'].get('C1') or []) if r['status'] == 'NOT STATABLE')
     and sum(1 for r in S['tb'].get('C1') or [] if r['status'] == 'NOT STATABLE') >= 1,
     lambda S: put(S, 'tb', dict(S['tb'], C1=[dict(r, search=[]) for r in S['tb'].get('C1') or []]))),
    ('G-FOUND-FOUND', 'every need printed FOUND -- re-searched here by file`s existence',
     lambda S: all(all(os.path.exists(os.path.join(KER if n['where'] == 'kernel' else os.path.join(KER, '.lake', 'packages', 'mathlib'),
                                                   f.replace('(to_additive) ', ''))) for f in n['files'])
                   for r in (S['tb'].get('C2') or []) for n in r['needs'] if n['found']),
     lambda S: put(S, 'tb', dict(S['tb'], C2=[dict(r, needs=[dict(n, files=['nowhere.lean']) if n['found'] else n for n in r['needs']]) for r in S['tb'].get('C2') or []]))),
    ('G-TWELVE-PAIRS', 'the table -- twelve ordered pairs, each a Prop or the theorem in the module',
     lambda S: len(S['tb'].get('C2') or []) == 12 and all(r['statement'] for r in S['tb']['C2']),
     lambda S: put(S, 'tb', dict(S['tb'], C2=(S['tb'].get('C2') or [])[:-1]))),
    ('G-WEAKEST-READ', 'the table -- the weakest form recomputed from the pairs',
     lambda S: S['tb'].get('weakest') == [p.split(' -> ')[1] for p in [r['pair'] for r in S['tb'].get('C2') or []
                                                                     if r['pair'].startswith('H2 -> ') and r['status'] == 'COMPILED']
                                          if c2(S, p.split(' -> ')[1] + ' -> H2').get('status') != 'COMPILED'],
     lambda S: put(S, 'tb', dict(S['tb'], weakest=['LI']))),
    ('G-DERIVABILITY-SAID', 'the table AND the desk -- non-implication said to be about derivability',
     lambda S: 'NOT A THEOREM' in S['tbtxt'] and 'A STATEMENT ABOUT DERIVABILITY, NOT A THEOREM' in S['desk'],
     lambda S: put(S, 'desk', S['desk'].replace('A STATEMENT ABOUT DERIVABILITY, NOT A THEOREM', ''))),
    ('G-B511-PLACED', 'the components bank AND the trail -- b511 beside the cell form, as measurements',
     lambda S: 'b511`s MEASUREMENTS, AS MEASUREMENTS, NOT TERMINALS' in S['comp'] and 'VERIFIED-EST, and no terminal' in trail(S),
     lambda S: put(S, 'comp', S['comp'].replace('AS MEASUREMENTS, NOT TERMINALS', ''))),
    ('G-N1-SCORED', 'the desk against the table', lambda S: 'n1' in S['sc'] and desk_word(S, 'N1') == word_of(S['sc']['n1'])
     and S['sc']['n1'] == (sum(1 for i in range(1, 6) if c1(S, 'R%d' % i).get('status') == 'NOT STATABLE') >= 2),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the RH -> H2 row', lambda S: 'n2' in S['sc'] and desk_word(S, 'N2') == word_of(S['sc']['n2'])
     and S['sc']['n2'] == (c2(S, 'RH -> H2').get('status') == 'STATABLE-NOT-COMPILED'
                           and all(n['found'] for n in c2(S, 'RH -> H2').get('needs', []) if n['where'] == 'mathlib')),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the cell rows', lambda S: 'n3' in S['sc'] and desk_word(S, 'N3') == word_of(S['sc']['n3'])
     and S['sc']['n3'] == (c1(S, 'CELL').get('status') == 'STATABLE' and c2(S, 'H2 -> CELL').get('status') == 'COMPILED'
                           and c2(S, 'CELL -> H2').get('status') != 'COMPILED'),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from its bank',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk']
     and desk_word(S, 'S1') == word_of(c1(S, 'LI2').get('status') == 'NOT STATABLE'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NOGRADE-CONFERRED', 'the face AND the kernel -- no corpus row graded, the kernel untagged',
     lambda S: 'NO GRADE IS CONFERRED OR MOVED ON ANY ROW' in flat(S['face']) and S['ker_tags'] == '',
     lambda S: put(S, 'ker_tags', 'v1.1')),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b512 -'))),
    ('G-NOPRIORBANK', 'file times against the face, the noted banks excepted by name', lambda S: S['noprior'],
     lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the kernel lane shut, said', lambda S: 'The kernel lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('The kernel lane shuts at this act', 'the lane stays open'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the trail and FINDINGS; no chain file edited',
     lambda S: sorted(S['tracked']) == ['FINDINGS.md', 'OPEN_TRAILS.md'] and S['chain_clean'] is True, lambda S: put(S, 'chain_clean', False)),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text', lambda S: S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- row 361 once, six cells as it landed',
     lambda S: S['corr'].count('| 361 |') == 1 and S['corr'].count('(b512, under (R121))') == 1
     and len([l for l in S['corr'].split(NL) if l.startswith('| 361 |')][0].strip().strip('|').split('|')) == 6,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 361 | a duplicate row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b511`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b504_chain.py'])),
    ('G-WRITELIST-KINDS', 'every b512 commit in four repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds'] if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text', lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the PLACE-papers file list -- no internal document, no `.lean`',
     lambda S: all(not x.startswith('internal/') and not x.endswith('.lean') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text', lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness itself -- the positive control is RUN on every arm',
     lambda S: not live_limb_guard(S['suite']), lambda S: put(S, 'suite', S['suite'].replace('defective.append(name)', 'pass'))),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED', lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)', lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b512')" in S['suite']
                and "data/b512_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b512_components.txt' in gits(ROOT, 'show'")),
]


def regenerate():
    """### ### **(R107): THE GENERATOR IS PART OF THE CLOSING SUITE.**

    ### *"the generator added to the closing suite so every later close regenerates it and diffs
    ### against the prior run"* -- the ruling's own words. ### The suite therefore RE-RUNS
    ### `tools/terminal_table.py` before it scores anything, and the diff it emits is a cell of
    ### this act's record. ### **A TABLE REGENERATED ONLY WHEN SOMEONE REMEMBERS IS A TABLE THAT
    ### ### DRIFTS**, and the whole point of an instrument output is that it cannot.
    """
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    d = os.path.join(D, 'terminal_table_diff.json')
    diff = json.loads(read(d) or '{}')
    return r.returncode, diff


def main():
    S = sources()
    rc_gen, gen_diff = regenerate()
    # ### ### **THE TABLE IS READ AFTER IT IS REGENERATED (b512's own defect, repaired post-push).** ### `sources()`
    # ### read `terminal_table.md` BEFORE `regenerate()` rewrote it, so `G-TABLE-ROW` scored the previous close's
    # ### table; the first post-push run is banked as `b512_checks_postpush_first.txt`.
    S['table'] = read(os.path.join(D, 'terminal_table.md'))
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b512')
              and 'data/b512_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b512 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
    if gen_diff.get('first_run'):
        rec('  ###   ### **NO PRIOR RUN TO DIFF AGAINST -- THIS CLOSE IS THE FIRST.** ### From')
        rec('  ###   ### the next close the diff is a cell; saying "no change" now would be a')
        rec('  ###   ### reassuring line about nothing.')
    else:
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
            % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
               len(gen_diff.get('changed') or [])))
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ### **5 EXCLUDED BY NAME** -- the noted components files, held by G-NOTES-PREFIX against 88c5d6ab.'
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
    out = os.path.join(D, 'b512_checks_postpush.txt' if pushed else 'b512_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b512_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
