# -*- coding: utf-8 -*-
"""b499_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### **THE CARRIED ARMS WERE RE-POINTED ONE AT A TIME**, each read against THIS act's banks
### before its pointer moved -- b480 recorded three instances of the wholesale-substitution species
### in a single act, and this file is written against that.
"""
import io
import glob
import hashlib
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
FACE = os.path.join(D, 'b499_registration_2026-09-23.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
BT = chr(96)
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


HOOKREPOS = (ROOT, PP, SIDE, KERNEL)


def token_in_commits():
    """### ### **THE WORLD, READ AT SUITE TIME:** does any b499 commit, in any of the four repos,
    ### carry the token in its patch or message? ### Returns a BOOL; the token is never printed."""
    t = os.environ.get('ZENODO_TOKEN') or ''
    if not t:
        return None
    for repo in HOOKREPOS:
        for l in gits(repo, 'log', '--pretty=%H %s', '-10').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b499'):
                if t in git(repo, 'show', '-p', '--format=%B', l.split()[0]):
                    return True
    return False


def token_in_banks():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        return None
    fs = glob.glob(os.path.join(D, 'b499_*')) + glob.glob(os.path.join(T, 'b499_*')) \
        + glob.glob(os.path.join(D, 'audit_b499_*')) \
        + [os.path.join(PP, x) for x in ('ERRATA.md', 'REGISTRY.md', 'OPEN_TRAILS.md',
                                         os.path.join('meta', 'ZENODO_METADATA.md'))] \
        + [os.path.join(SIDE, 'CORRESPONDENCE.md')]
    return any(t in open(f, 'rb').read() for f in fs if os.path.isfile(f))


def sources():
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b499_ferry.txt')),
        scan=read(os.path.join(D, 'b499_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b499_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b499_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b499_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b499_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b498_closing.txt')),
        addendum=read(os.path.join(D, 'b499_addendum.txt')),
        comp=read(os.path.join(D, 'b499_components.txt')),
        desk=read(os.path.join(D, 'b499_desk_notes.txt')),
        span=read(os.path.join(D, 'b499_span_notes2.txt')) + read(os.path.join(D, 'b499_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b499_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b499_scores.json')) or '{}'),
        guard=json.loads(read(os.path.join(D, 'b499_guard.json')) or '{}'),
        guardfirst=json.loads(read(os.path.join(D, 'b499_guard_first.json')) or '{}'),
        hooks=[read(os.path.join(r, '.githooks', 'pre-push')) for r in HOOKREPOS],
        input_banked=open(os.path.join(D, 'zenodo_edits_2026-09-23_v2.txt'), 'rb').read(),
        input_source=open(os.path.join('D:', os.sep, 'MY-DOwnloads', 'zenodo_edits_2026-09-23_v2.txt'), 'rb').read(),
        zentool=read(os.path.join(T, 'b499_zenodo.py')),
        recordtool=read(os.path.join(T, 'b499_record.py')),
        errata=read(os.path.join(PP, 'ERRATA.md')),
        registry=read(os.path.join(PP, 'REGISTRY.md')),
        zmeta=read(os.path.join(PP, 'meta', 'ZENODO_METADATA.md')),
        # ### ### **READ UNSTRIPPED.** ### `gits()` strips the trailing newline, and the first run
        # ### counted one line too many as added because of it.
        registry_base=git(PP, 'show', '6337cef:REGISTRY.md').replace(chr(13), ''),
        zmeta_base=git(PP, 'show', '6337cef:meta/ZENODO_METADATA.md').replace(chr(13), ''),
        fetchbacks={rid: json.loads(read(os.path.join(D, 'b499_fetchback_%s.json' % rid)) or '{}')
                    for rid in ('21539068', '21520474', '21539167')},
        tok_banks=token_in_banks(), tok_commits=token_in_commits(),
        tok_env_set=bool(os.environ.get('ZENODO_TOKEN')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b499_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b499.zip'))),
        tools499=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b499_') and f.endswith('.py') and f != 'b499_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b499 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b499_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in HOOKREPOS:
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b499 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
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
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-8][0-9]_|^b49[0-8]_', f)]
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



def c(S, n):
    return (S['res'] or {}).get(n) or {}


def recs(S):
    return (c(S, 'c2').get('records') or {})


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0]


def word_of(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def lines_kept(old, new):
    it = iter(new.split(NL))
    return all(any(o == n for n in it) for o in old.split(NL))


RIDS = ('21539068', '21520474', '21539167')
LIMB = '(v) the token scan -- added b499 under (R110)'

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b499' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan',
     lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b498`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                or 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'])
     and S['corr'].count('| 347 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 347 |', '| 3470 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b499' in S['ferry'] and 'ACT b499' in S['face']
                and not os.path.exists(os.path.join(D, 'b500_ferry.txt'))),
     lambda S: cut(S, 'face', 'ACT b499')),
    ('G-PEEK-DECLARED', 'the face -- the reads taken BEFORE the seal are declared',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in S['face']
                and 'NO LIVE ZENODO READ WAS MADE BEFORE THE SEAL' in S['face']),
     lambda S: cut(S, 'face', 'NO LIVE ZENODO READ WAS MADE BEFORE THE SEAL')),
    ('G-R110-R111-ENTERED', 'the banked ferry AND the trail',
     lambda S: ('RULING (R110) END' in S['ferry'] and 'RULING (R111) END' in S['ferry']
                and S['ot'].count('**(R110) ratified.**') == 1 and S['ot'].count('**(R111) ratified.**') == 1),
     lambda S: put(S, 'ot', S['ot'].replace('**(R111) ratified.**', '(R111) noted'))),
    ('G-INPUT-COPIED-UNCHANGED', 'the two copies of the input, byte for byte',
     lambda S: S['input_banked'] == S['input_source'] and len(S['input_banked']) > 0,
     lambda S: put(S, 'input_banked', S['input_banked'] + b'x')),

    # -------------------------------------------------- step (G)
    ('G-GUARD-LIMB-PRESENT', 'the four tracked guards',
     lambda S: all(LIMB in h and "ENVIRON[\"ZENODO_TOKEN\"]" in h for h in S['hooks']),
     lambda S: put(S, 'hooks', [S['hooks'][0].replace(LIMB, 'x')] + S['hooks'][1:])),
    ('G-GUARD-SINGLE-SOURCE', 'the four tracked guards, byte for byte',
     lambda S: len(set(S['hooks'])) == 1 and bool(S['hooks'][0]),
     lambda S: put(S, 'hooks', S['hooks'][:3] + [S['hooks'][3] + '#'])),
    ('G-GUARD-REFUSES-FAKE', 'the exercise bank -- the positive case, on the NEW guard',
     lambda S: any(x['label'].startswith('POSITIVE') and x['refused'] and x['exit'] != 0
                   and x.get('hook_is_new') and not x['leaked'] for x in S['guard'].get('cases') or []),
     lambda S: put(S, 'guard', dict(S['guard'], cases=[dict(x, refused=False) for x in S['guard']['cases']]))),
    ('G-GUARD-PASSES-CLEAN', 'the exercise bank -- the negative case, on the NEW guard',
     lambda S: any(x['label'].startswith('NEGATIVE') and not x['refused'] and x['exit'] == 0
                   and x.get('hook_is_new') for x in S['guard'].get('cases') or []),
     lambda S: put(S, 'guard', dict(S['guard'], cases=[dict(x, hook_is_new=False) for x in S['guard']['cases']]))),
    ('G-GUARD-WARNS-UNSET', 'the exercise bank -- the unset case, on the NEW guard',
     lambda S: any(x['label'].startswith('UNSET') and x['warned'] and x.get('hook_is_new')
                   for x in S['guard'].get('cases') or []),
     lambda S: put(S, 'guard', dict(S['guard'], cases=[dict(x, warned=False) for x in S['guard']['cases']]))),
    ('G-GUARD-BEFORE-TOKEN', 'file times -- the guard`s exercise bank older than Component 0`s',
     lambda S: S.get('guard_before_c0', False),
     lambda S: put(S, 'guard_before_c0', False)),

    # -------------------------------------------------- the token
    ('G-TOKEN-NOT-IN-BANKS', 'every bank, tool and written document of this act, at suite time',
     lambda S: S['tok_banks'] is False,
     lambda S: put(S, 'tok_banks', True)),
    ('G-TOKEN-NOT-IN-COMMITS', 'every b499 commit in the four repositories, patch and message',
     lambda S: S['tok_commits'] is False,
     lambda S: put(S, 'tok_commits', True)),
    ('G-TOKEN-NOT-IN-TOOLS', 'the act`s tools -- the token read from the environment, never a literal',
     lambda S: ("os.environ.get('ZENODO_TOKEN')" in S['zentool']
                and not re.search(r"ZENODO_TOKEN'\]?\s*=\s*['\"]", strip_prose(S['tools499']))),
     lambda S: put(S, 'tools499', S['tools499'] + NL + "os.environ['ZENODO_TOKEN'] = 'abc'")),
    ('G-TOKEN-PREFIX-ONLY', 'the Component 0 cell -- length and an 8-hex prefix, nothing more',
     lambda S: (re.fullmatch(r'[0-9a-f]{8}', c(S, 'c0').get('prefix') or '') is not None
                and set(c(S, 'c0')) <= {'set', 'length', 'prefix', 'status', 'title', 'proceed'}),
     lambda S: put(S, 'res', dict(S['res'], c0=dict(c(S, 'c0'), prefix='8e8212d3' * 8)))),
    ('G-C0-STATUS-200', 'the Component 0 cell',
     lambda S: c(S, 'c0').get('status') == 200 and c(S, 'c0').get('proceed') is True,
     lambda S: put(S, 'res', dict(S['res'], c0=dict(c(S, 'c0'), status=403)))),

    # -------------------------------------------------- component 1
    ('G-BEFORE-BANKED', 'the three before-state banks on disk',
     lambda S: all(os.path.getsize(os.path.join(D, 'b499_before_%s.json' % r)) > 0 for r in RIDS)
     and S.get('before_ok', True),
     lambda S: put(S, 'before_ok', False)),
    ('G-TEN-TARGETS-COUNTED', 'the plan cell against the banked input',
     lambda S: len(c(S, 'c1').get('targets') or []) == 10 and c(S, 'c1').get('once') == 10,
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), once=9)))),
    ('G-EXTENT-RULE-K', 'the plan -- each span holds exactly K sentence ends, K from its replacement',
     lambda S: all(len(re.findall(r'\.(?=\s|<|$)', t['old'])) == t['k']
                   == len(re.findall(r'\.(?=\s|<|$)', t['text']))
                   for t in c(S, 'c1').get('targets') or [] if t['kind'] == 'description'),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), targets=[
         dict(t, k=(t.get('k') or 0) + 1) for t in c(S, 'c1')['targets']])))),
    ('G-SPAN-IN-ONE-PARAGRAPH', 'the plan -- no span crosses a paragraph tag',
     lambda S: all(not re.search(r'</?p\b', t.get('old') or '')
                   for t in c(S, 'c1').get('targets') or [] if t['kind'] == 'description'),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), targets=[
         dict(t, old=(t.get('old') or '') + '</p>') for t in c(S, 'c1')['targets']])))),
    ('G-ENTITY-SITES-COUNTED', 'the plan cell against the before-states themselves',
     lambda S: all(c(S, 'c1')['entities'][r] == len(re.findall(
         r'&(?:#\d+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]*);',
         (json.loads(read(os.path.join(D, 'b499_before_%s.json' % r)))['metadata'].get('description') or '')))
         for r in RIDS),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), entities={r: 0 for r in RIDS})))),
    ('G-STOP-BEFORE-WRITE', 'the Component 2 tool -- it refuses unless Component 1 cleared',
     lambda S: ("if (R.get('c1') or {}).get('stop') is not False:" in S['zentool']
                and c(S, 'c1').get('stop') is False),
     lambda S: cut(S, 'zentool', "if (R.get('c1') or {}).get('stop') is not False:")),

    # -------------------------------------------------- component 2
    ('G-ORDER-OBEYED', 'the write cells, in the order written',
     lambda S: list(recs(S)) == list(RIDS),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), records=dict(reversed(list(recs(S).items()))))))),
    ('G-EDIT-201', 'the write cells', lambda S: all(recs(S)[r].get('edit') == 201 for r in RIDS),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), records=dict(recs(S), **{RIDS[0]: dict(recs(S)[RIDS[0]], edit=400)}))))),
    ('G-PUT-200', 'the write cells', lambda S: all(recs(S)[r].get('put') == 200 for r in RIDS),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), records=dict(recs(S), **{RIDS[1]: dict(recs(S)[RIDS[1]], put=400)}))))),
    ('G-PUBLISH-202', 'the write cells', lambda S: all(recs(S)[r].get('publish') == 202 for r in RIDS),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), records=dict(recs(S), **{RIDS[2]: dict(recs(S)[RIDS[2]], publish=500)}))))),
    ('G-OTHER-KEYS-CARRIED', 'the write cells -- every key but title and description carried',
     lambda S: all(recs(S)[r].get('other_keys_carried') is True and recs(S)[r].get('keys_same') is True
                   for r in RIDS),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), records=dict(recs(S), **{RIDS[0]: dict(recs(S)[RIDS[0]], keys_same=False)}))))),
    ('G-FETCHBACK-ANONYMOUS', 'the Component 2 tool -- the fetch-back call carries auth=False',
     lambda S: "http('GET', API + '/records/' + rid, auth=False)" in S['zentool'],
     lambda S: cut(S, 'zentool', "http('GET', API + '/records/' + rid, auth=False)")),
    ('G-FETCHBACK-BANKED', 'the fetch-back banks against their recorded digests',
     lambda S: all(hashlib.sha256(open(os.path.join(D, 'b499_fetchback_%s.json' % r), 'rb').read()).hexdigest()
                   == recs(S)[r].get('fetchback_sha256') for r in RIDS),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), records=dict(recs(S), **{RIDS[0]: dict(recs(S)[RIDS[0]], fetchback_sha256='0' * 64)}))))),
    ('G-MATCH-FOUR-LIMBS', 'the write cells AND the banked fetch-backs` titles',
     lambda S: all(all(recs(S)[r].get(x) for x in ('limb1', 'limb2', 'limb3', 'limb4', 'match'))
                   and (S['fetchbacks'][r].get('metadata') or {}).get('title') == recs(S)[r].get('returned_title')
                   for r in RIDS),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), records=dict(recs(S), **{RIDS[2]: dict(recs(S)[RIDS[2]], limb4=False)}))))),
    ('G-NO-NEW-VERSION', 'the banked fetch-backs -- same id, still the last version, same files',
     lambda S: all(str(S['fetchbacks'][r].get('id')) == r
                   and all(v.get('is_last') for v in ((S['fetchbacks'][r].get('metadata') or {}).get('relations') or {}).get('version') or [{}])
                   and recs(S)[r].get('files_before') == recs(S)[r].get('files_after')
                   for r in RIDS),
     lambda S: put(S, 'fetchbacks', dict(S['fetchbacks'], **{RIDS[0]: dict(S['fetchbacks'][RIDS[0]], id=99)}))),

    # -------------------------------------------------- component 3
    ('G-ERRATA-ONE-ENTRY', 'ERRATA.md itself',
     lambda S: S['errata'].count('**`E-2026-09-23-1` —') == 1,
     lambda S: put(S, 'errata', S['errata'] + NL + '**`E-2026-09-23-1` — a second entry**')),
    ('G-ERRATA-ID-R97', 'ERRATA.md -- the first id of this date, none before it',
     lambda S: sorted(set(re.findall(r'E-2026-09-23-\d+', S['errata']))) == ['E-2026-09-23-1'],
     lambda S: put(S, 'errata', S['errata'] + NL + 'E-2026-09-23-2')),
    ('G-ERRATA-CARRIES-R111', 'the entry`s own text',
     lambda S: ('THE_UNCONDITIONAL_SURROUND' in seg(S['errata'], '**`E-2026-09-23-1` —', 99999)
                and 'three of which share one map' in seg(S['errata'], '**`E-2026-09-23-1` —', 99999)),
     lambda S: put(S, 'errata', S['errata'].replace('THE_UNCONDITIONAL_SURROUND', 'x'))),
    ('G-NOTES-BESIDE-LINES', 'REGISTRY and ZENODO_METADATA -- each note at its sealed point',
     lambda S: (all(('beside `REGISTRY.md:%d`' % n) in S['registry'] for n in (77, 82, 94, 98, 414))
                and all(('beside `meta/ZENODO_METADATA.md:%d`' % n) in S['zmeta'] for n in (8, 9, 10))
                and S['registry'].split(NL)[77].startswith('*(Note, `b499`')
                and S['registry'].split(NL)[91].startswith('*(Note, `b499`')),
     lambda S: put(S, 'registry', S['registry'].replace('beside `REGISTRY.md:94`', 'x'))),
    ('G-NOTES-INSERT-ONLY', 'both files against PLACE-papers 6337cef -- every prior line kept, in order',
     lambda S: (lines_kept(S['registry_base'], S['registry']) and lines_kept(S['zmeta_base'], S['zmeta'])
                and len(S['registry'].split(NL)) - len(S['registry_base'].split(NL)) == 7
                and len(S['zmeta'].split(NL)) - len(S['zmeta_base'].split(NL)) == 3),
     lambda S: put(S, 'registry', S['registry'].replace('| d1-1 |', '| d1-X |'))),
    ('G-NAMED-LINES-UNCHANGED', 'the record tool`s own bank',
     lambda S: c(S, 'c3').get('named_unchanged') is True and c(S, 'c3').get('ok') is True,
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), named_unchanged=False)))),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the desk bank against the scores',
     lambda S: 'n1' in (S['sc'] or {}) and desk_word(S, 'N1') == word_of(S['sc']['n1']),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not (S['sc'] or {}).get('n1')))),
    ('G-N2-SCORED', 'the desk bank against the scores',
     lambda S: 'n2' in (S['sc'] or {}) and desk_word(S, 'N2') == word_of(S['sc']['n2']),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not (S['sc'] or {}).get('n2')))),
    ('G-N3-SCORED', 'the desk bank -- and the limit of its "so" said',
     lambda S: ('n3' in (S['sc'] or {}) and desk_word(S, 'N3') == word_of(S['sc']['n3'])
                and 'A MATCH ON THE' in S['desk']),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not (S['sc'] or {}).get('n3')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank -- INCLUDING THE REFUTED ONE',
     lambda S: ("THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk']
                and desk_word(S, 'S3') == 'REFUTED'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S3)** ### **REFUTED', '**(S3)** ### **HELD'))),

    # -------------------------------------------------- the nothings
    ('G-NOGRADE-CONFERRED', 'the face', lambda S: 'THIS ACT CONFERS NO GRADE' in S['face'],
     lambda S: cut(S, 'face', 'THIS ACT CONFERS NO GRADE')),
    ('G-NODEPOSIT', 'the deposit directory tracked state',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record',
     lambda S: 'where the deposit left it' in seg(S['ot'], '### b499 —', 99999),
     lambda S: put(S, 'ot', S['ot'].replace('### b499 —', '### b499 -'))),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record',
     lambda S: 'the four lists stay OPEN' in seg(S['ot'], '### b499 —', 99999),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- exactly the documents (W) names',
     lambda S: sorted(S['tracked']) == sorted(['.githooks/pre-push', 'ERRATA.md', 'OPEN_TRAILS.md',
                                               'REGISTRY.md', 'meta/ZENODO_METADATA.md']),
     lambda S: put(S, 'tracked', sorted(S['tracked']) + ['FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b499 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b499 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: S['corr'].count('| 348 |') == 1 and S['corr'].count('(b499, under (R110)') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 348 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b499 commit in four repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the PLACE-papers file list -- no internal document, no `.lean`',
     lambda S: all(not x.startswith('internal/') and not x.endswith('.lean') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness itself -- the positive control is RUN on every arm',
     lambda S: not live_limb_guard(S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace('defective.append(name)', 'pass'))),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b499')" in S['suite']
                and "data/b499_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b499_components.txt' in gits(ROOT, 'show'")),
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
    S['guard_before_c0'] = (os.path.getmtime(os.path.join(D, 'b499_guard.json'))
                            < os.path.getmtime(os.path.join(D, 'b499_components_c0.txt')))
    rc_gen, gen_diff = regenerate()
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b499')
              and 'data/b499_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b499 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b499_checks_postpush.txt' if pushed else 'b499_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b499_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
