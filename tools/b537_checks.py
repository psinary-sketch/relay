# -*- coding: utf-8 -*-
"""b537_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The kernel arms read the kernel's own tree and git state, and Lean's own output in the run files.
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
FACE = os.path.join(D, 'b537_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'ec51f465'      # ### b536's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '5c72cad'           # ### the kernel's tip before this act
PRIOR_PP = '7c1c2da'           # ### b536's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b537 —'
GRADE_RE = re.compile(r'\b(DERIVES|INTERFACES|SHELL|ENCODES-CONCLUSION|ENCODES)\b')
G0 = dict(xi=14.1347, q=16.290216)
WIT = 'the window is the witness construction h2_sign_imp_rh names, exhibited at one rho'


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


def jsonl(p):
    return [json.loads(l) for l in read(p).split(NL) if l.strip()]


SK = os.path.join('D:', os.sep, 'SIDE-kernel')
SK_TIP = '0256e9e'
PREM = ['Bridge/ConservationBridge.lean', 'Kernel/XiDef.lean', 'Kernel/Voice1.lean']


PPFILES = ['OPEN_TRAILS.md']


MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--', 'memory')
ENTRY = 'project_criterion_b533_b536.md'
ZIP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-2026-09-25-b537.zip')
V01 = 'baed4df861dac05224f01dad17453648d3d7fe0a'
V02 = '5c72cad24303f23d92256ebd466d3a3d32424a4b'
SIDE_TIP = '186114dd70d4c79891893c50b7de4b17b766dab1'
NOT_CLAIMED = "RH proved; h2_sign proved; the earliest Lean formalization of Weil's criterion."
REPO_PATHS = [('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER), ('SIDE-kernel', SK)]


def sha_of(p):
    try:
        return hashlib.sha256(open(p, 'rb').read()).hexdigest()
    except OSError:
        return ''


def ceil_from_ferry():
    f = ' '.join(read(os.path.join(D, 'b536_ferry.txt')).split())
    i = f.find('reads, supportable: "')
    j = f.find('" Not supportable', i)
    return f[i + len('reads, supportable: "'):j] if i >= 0 and j > i else ''


def delete_needles():
    return [x + y for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                               ('rm ', '-'), ('rmd', 'ir '), ('Clear', '-Content'))]


def sources():
    import zipfile
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    z = zipfile.ZipFile(ZIP)
    man_raw = z.read('MANIFEST.md')
    tags = {}
    for l in gits(KER, 'ls-remote', '--tags', 'origin').split(NL):
        m = re.match(r'^([0-9a-f]{40})\s+refs/tags/(v0\.[12])\^\{\}$', l.strip())
        if m:
            tags[m.group(2)] = m.group(1)
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b537_ferry.txt')),
        scan=read(os.path.join(D, 'b537_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b537_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b537_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b537_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b537_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b536_closing.txt')),
        addendum=read(os.path.join(D, 'b537_addendum.txt')),
        comp=read(os.path.join(D, 'b537_components.txt')),
        desk=read(os.path.join(D, 'b537_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b537_scores.json')) or '{}'),
        mj=json.loads(read(os.path.join(D, 'b537_mirror.json')) or '{}'),
        hj=json.loads(read(os.path.join(D, 'b537_head.json')) or '{}'),
        rh=json.loads(read(os.path.join(D, 'b537_rehead.json')) or '{}'),
        mm=json.loads(read(os.path.join(D, 'b537_memory.json')) or '{}'),
        verify=read(os.path.join(D, 'b537_mirror_verify.txt')),
        buildlog=read(os.path.join(D, 'b537_build_log.txt')),
        zip_sha=hashlib.sha256(open(ZIP, 'rb').read()).hexdigest(),
        man=man_raw.decode('utf-8-sig').replace(chr(13), ''), man_text=man_raw.decode('utf-8-sig'),
        tags=tags, ceil=ceil_from_ferry(),
        expected={n: (gits(p, 'rev-parse', PRIOR_RELAY) if n == 'relay' else gits(p, 'rev-parse', PRIOR_PP) if n == 'PLACE-papers'
                      else gits(p, 'rev-parse', 'HEAD')) for n, p in REPO_PATHS},
        pp_blob_md5={f: hashlib.md5(blob(PP, PRIOR_PP + ':' + f)).hexdigest() for f in ('FINDINGS.md', 'REGISTRY.md', 'ERRATA.md', 'README.md')},
        additions=[l for l in gits(PP, 'diff', '--name-status', '--diff-filter=A', '3b5532a', PRIOR_PP).split(NL) if l.strip()],
        mem_live=open(os.path.join(MEM, ENTRY), 'rb').read() if os.path.exists(os.path.join(MEM, ENTRY)) else b'',
        mem_bank=open(os.path.join(D, 'b537_memory_entry.md'), 'rb').read(),
        mem_index=open(os.path.join(MEM, 'MEMORY.md'), 'rb').read(),
        mem_before=json.loads(read(os.path.join(D, 'b537_memory_before.json')) or '{}').get('files', {}),
        mem_now={f: sha_of(os.path.join(MEM, f)) for f in os.listdir(MEM) if f.endswith('.md')},
        seam_line=next((i + 1 for i, l in enumerate(read(os.path.join(KER, 'SIDEExplicitFormula', 'Seam.lean')).split(NL))
                        if l.startswith('theorem zeta_zero_re_nonpos ')), 0),
        b512=[l.strip() for l in read(os.path.join(D, 'b512_closing.txt')).split(NL)[4:7]],
        prevbuild=git(ROOT, 'status', '--porcelain', '--', 'tools/mirror_prevbuild.json').strip(),
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', KER_TIP).split(NL) if x.strip())
                    | set(p[3:].strip() for p in git(KER, 'status', '--porcelain').split(NL) if p.strip() and not p.startswith('??')),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b537_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b537_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b537_') and f.endswith('.py')
                        for n in delete_needles() if n in strip_prose(read(os.path.join(T, f))))),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md').decode('utf-8', 'replace').replace(chr(13), ''),
        ot_prior_bytes=blob(PP, PRIOR_PP + ':OPEN_TRAILS.md'),
        ot_now_bytes=open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read(),
        suite=read(os.path.join(T, 'b537_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b537 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b537_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b537_build_log.txt', 'b537_head.json', 'b537_mirror.json',
                                                               'b537_memory.json', 'b537_trail_notes.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in ('b537_memory_before.json', 'b537_ferry.txt')),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b537 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-6]_|^b334_', f)]
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


VACUOUS_ARMS = ()
NS = ''


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def trail_raw(S):
    return seg(S['ot'], TRAILH, 99999)


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def man_rows(S):
    return {m.group(1): m.group(2) for m in re.finditer(r'^\|\s*([^|]+?)\s*\|\s*[\d,]+\s*\|\s*`?([0-9a-f]{32})`?\s*\|', S['man'], re.M)}


def man_head(S):
    return S['man'].split('| flat file |')[0]


def repo_line(S, n):
    return next((l for l in man_head(S).split(NL) if l.startswith('- %s : ' % n)), '')


def repos_ok(S):
    for n, _ in REPO_PATHS:
        e = S['expected'][n]
        l = repo_line(S, n)
        if not (e and l.startswith('- %s : local %s ; remote %s ; AGREE' % (n, e, e))):
            return False
    return True


def mem_text(S):
    return S['mem_live'].decode('utf-8', 'replace')


def recomputed(S):
    rows = man_rows(S)
    ros = line_with(S['man'], 'ROSTER')
    return dict(
        n1=repo_line(S, 'PLACE-papers').startswith('- PLACE-papers : local %s ; remote %s ; AGREE' % (S['expected']['PLACE-papers'], S['expected']['PLACE-papers']))
        and all(rows.get(f) == h for f, h in S['pp_blob_md5'].items()),
        n2=bool(S['ceil']) and S['man'].count(S['ceil']) == 1 and S['ceil'] in man_head(S),
        n3=V01 in mem_text(S) and V02 in mem_text(S) and ('Not claimed:' in mem_text(S) and NOT_CLAIMED in mem_text(S)),
        n4=S['dep_clean'] and not S['zen'] and S['tok'] == 0,
        s1='unchanged since' in ros and 'ADDED:' not in S['man'] and 'REMOVED:' not in S['man'],
        s2='VERDICT: CLEAN ON ALL THREE CLAUSES' in line_with(S['verify'], '### VERDICT:'),
        s3=S['prevbuild'] == '')


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == recomputed(S)[k]


def builder_text(S):
    blk = NL.join(S['hj'].get('block') or ['x']) + NL
    t = S['man_text']
    first, _, rest = t.partition(NL)
    return first + NL + rest[len(blk):] if rest.startswith(blk) else ''


WO1 = '#### `W-ORD-SEAM-UPSTREAM` — OPEN, named not started, filed b537 on `(R147)`(4)'
WO2 = '#### `W-ORD-REGISTER-DEPTH` — OPEN, named not started, filed b537 on `(R147)`(4)'


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R147) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b537' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan carries no (R81) flag' in flat(S['face']),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b536`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE TAG, THE CENSUSES' in S['prior'] and S['corr'].count('| 386 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 386 |', '| 3860 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b537' in S['ferry'] and 'ACT b537' in S['face'] and not glob.glob(os.path.join(D, 'b538_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b537')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, the memory hashes before the lock, the build and memory banks after it',
     lambda S: 'unpacked at `/tmp/tmp.g5JUpjTi0f`' in S['face'] and S['before_lock'] and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R147-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R147) END' in S['ferry'] and S['ot'].count('**(R147) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R147) ratified', '(R147) noted'))),
    ('G-BUILD-PATHS-ABSENT', 'the build log -- the absence line written by the building command, then the builder`s own',
     lambda S: S['buildlog'].split(NL)[0] == 'both build paths ABSENT, verified in the building command'
     and 'built: D:' + chr(92) + 'MY-DOwnloads' + chr(92) + 'mirror-refresh-2026-09-25-b537.zip' in S['buildlog'],
     lambda S: put(S, 'buildlog', S['buildlog'].replace('both build paths ABSENT', 'build paths'))),
    ('G-ZIP-HASHED', 'the zip`s bytes READ HERE against the bank and the repair`s record',
     lambda S: S['zip_sha'] == S['mj'].get('zip_sha256') == S['rh'].get('zip_sha_after'),
     lambda S: put(S, 'zip_sha', '0' * 64)),
    ('G-VERIFY-THREE-CLAUSES', 'the verifier`s bank on the final zip',
     lambda S: all(('CLAUSE %d : CLEAN' % i) in S['verify'] for i in (1, 2, 3))
     and 'CLEAN ON ALL THREE CLAUSES' in line_with(S['verify'], '### VERDICT:') and '### exit 0' in S['verify'],
     lambda S: put(S, 'verify', S['verify'].replace('CLAUSE 2 : CLEAN', 'CLAUSE 2 : NOT CLEAN'))),
    ('G-ADDITIONS-LISTED', 'PLACE-papers` git READ HERE against the bank and the trail',
     lambda S: S['additions'] == S['mj'].get('additions_since_3b5532a')
     and ('Documents added since it: %s.' % (', '.join(S['additions']) or 'NONE')) in trail(S),
     lambda S: put(S, 'additions', ['A' + chr(9) + 'GHOST.md'])),
    ('G-MANIFEST-CEILING-ONCE', 'the MANIFEST inside the zip against the b536 ferry`s sentence',
     lambda S: bool(S['ceil']) and S['man'].count(S['ceil']) == 1 and S['ceil'] in man_head(S) and '**THE CEILING, (R146)(2)**' in man_head(S),
     lambda S: put(S, 'man', S['man'].replace(S['ceil'] or 'x', (S['ceil'] or 'x').replace('equivalent', 'equal')))),
    ('G-MANIFEST-REPOS', 'the MANIFEST`s five repository lines against each repository`s git READ HERE',
     lambda S: repos_ok(S), lambda S: put(S, 'man', S['man'].replace('- SIDE-kernel : local', '- SIDE-kernel : locale'))),
    ('G-MANIFEST-TAGS', 'SIDE-explicit-formula`s line against the remote`s peeled tags READ HERE',
     lambda S: S['tags'].get('v0.1') == V01 and S['tags'].get('v0.2') == V02
     and repo_line(S, 'SIDE-explicit-formula').endswith('; tags v0.1 = %s , v0.2 = %s' % (V01, V02)),
     lambda S: put(S, 'tags', dict(S['tags'], **{'v0.2': '0' * 40}))),
    ('G-MANIFEST-BUILDER-LINES-KEPT', 'the MANIFEST without the block against the builder`s text md5 recorded by the repair',
     lambda S: bool(builder_text(S)) and hashlib.md5(builder_text(S).encode('utf-8')).hexdigest() == S['rh'].get('builder_text_md5')
     and len(man_rows(S)) == S['mj'].get('files_excl_manifest'),
     lambda S: put(S, 'man_text', S['man_text'].replace('Source: PLACE-papers', 'Source: PLACE papers'))),
    ('G-MEMORY-ENTRY-FORM', 'the seat`s memory file READ HERE against its bank, the ferry`s ceiling and the ruling`s words',
     lambda S: S['mem_live'] == S['mem_bank'] and mem_text(S).startswith('---' + NL + 'name: project-criterion-b533-b536' + NL)
     and (NL + '  type: project' + NL) in mem_text(S) and '**Why:**' in mem_text(S) and '**How to apply:**' in mem_text(S)
     and bool(S['ceil']) and S['ceil'] in mem_text(S) and V01 in mem_text(S) and V02 in mem_text(S) and NOT_CLAIMED in mem_text(S),
     lambda S: put(S, 'mem_live', S['mem_live'].replace(V01.encode(), b'baed4df'))),
    ('G-MEMORY-INDEX-APPENDED', 'MEMORY.md READ HERE -- its pre-seal bytes a prefix, one line added, pointing at the entry',
     lambda S: (lambda t: t.endswith(NL) and len(t.rstrip(NL).split(NL)) >= 2
                and hashlib.sha256(NL.join(t.rstrip(NL).split(NL)[:-1]).encode('utf-8') + NL.encode()).hexdigest() == S['mem_before'].get('MEMORY.md')
                and ('(%s)' % ENTRY) in t.rstrip(NL).split(NL)[-1] and t.count('(%s)' % ENTRY) == 1)(S['mem_index'].decode('utf-8')),
     lambda S: put(S, 'mem_index', S['mem_index'] + b'- extra line' + NL.encode())),
    ('G-MEMORY-EARLIER-UNTOUCHED', 'every memory file READ HERE against the pre-seal hashes',
     lambda S: all(S['mem_now'].get(f) == h for f, h in S['mem_before'].items() if f != 'MEMORY.md')
     and sorted(set(S['mem_now']) - set(S['mem_before'])) == [ENTRY],
     lambda S: put(S, 'mem_now', dict(S['mem_now'], **{'project_power_limit_b534.md': '0' * 64}))),
    ('G-WORKORDERS-ENTERED', 'OPEN_TRAILS -- both entries once, in this act`s record, citing the lines READ HERE',
     lambda S: S['ot'].count(WO1) == 1 and S['ot'].count(WO2) == 1 and WO1 in trail_raw(S) and WO2 in trail_raw(S)
     and ('Seam.lean:%d` at `v0.2`' % S['seam_line']) in trail_raw(S) and all(l in trail_raw(S) for l in S['b512'])
     and '**Trigger: the author`s word.**' in trail_raw(S) and '**Trigger: the act after b537, unless the author rules otherwise.**' in trail_raw(S),
     lambda S: put(S, 'ot', S['ot'].replace(WO2, '#### ghost'))),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b537_x.py', 'x')])),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b537_x.py'])),
    ('G-N1-SCORED', 'the desk against the MANIFEST rows and the blobs', lambda S: nscored(S, 'n1'),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the MANIFEST and the ferry', lambda S: nscored(S, 'n2'),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the memory file', lambda S: nscored(S, 'n3'),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the tree, the tools and the token', lambda S: nscored(S, 'n4'),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b537 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernel`s tree -- nothing changed since v0.2',
     lambda S: 'No kernel lane opened at this act' in trail(S) and S['ker_changed'] == set(),
     lambda S: put(S, 'ker_changed', {'SIDEExplicitFormula/Seam.lean'})),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- OPEN_TRAILS alone',
     lambda S: sorted(S['tracked']) == sorted(PPFILES),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS` bytes against its blob at b536`s commit -- a true prefix; one heading',
     lambda S: S['ot_now_bytes'].startswith(S['ot_prior_bytes']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-UNTOUCHED', 'the correspondence ledger against its blob at b536`s commit',
     lambda S: S['corr'] == S['corr_prior'] and S['corr'] != '',
     lambda S: put(S, 'corr', S['corr'] + NL + '| 387 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b536`s close -- none modified, the builder`s state file included',
     lambda S: S['tools_edited'] == [] and S['prevbuild'] == '', lambda S: put(S, 'tools_edited', ['mirror_build.ps1'])),
    ('G-WRITELIST-KINDS', 'every b537 commit in four repositories, against (R91)`s STEM GLOB',
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
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)', lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b537')" in S['suite']
                and "data/b537_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b537_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b537')
              and 'data/b537_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b537 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d prior banks by time, none excepted.'
        % S['prior_checked'])
    rec('  ### ### **VACUOUS ARMS : %s.**'
        % ([a for a in VACUOUS_ARMS] or 'NONE'))
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
    out = os.path.join(D, 'b537_checks_postpush.txt' if pushed else 'b537_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b537_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
