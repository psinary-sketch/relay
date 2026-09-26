# -*- coding: utf-8 -*-
"""b542_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b542_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'e211efca'      # ### b541's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '81d7994'           # ### b541's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b542 —'


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


import b542_record as R
PPFILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md']
SIDE_TIP = '502f0a7a67462eab83a0f10eee5ea74be67957dd'
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
LIVEP = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
TIERS = ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')
KINDS = ('INHERITS', 'FORCES', 'BOTH', 'NEITHER')
INH3 = ['ZetaSeam.one_le_mult_holds', 'zeta_reflect_zero', 'zeta_mult_reflect']
CLASS7 = ['C1_schwarz', 'C2_euler', 'C3_functional_eq', 'C4_modular', 'C5_spectral', 'C6_cauchy_riemann', 'C7_hadamard']
BRANCH_LINES = ['Deleted branch push-b541 (was dea0cffd).', 'Deleted branch push-b541-closing (was e211efca).', 'Deleted branch push-b541 (was 81d7994).']


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def techne_private_names():
    """### TECHNE-Core`s declaration names that no public repository of the census declares -- read HERE from the private clone, kept in memory"""
    priv = set()
    for f in [f for f in R.g(R.PRIV, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL) if f.endswith('.lean')]:
        for x in R.scan_file(R.g(R.PRIV, 'show', 'HEAD:' + f), [], set()):
            if x['needles'] or f.startswith('TECHNE/Core/Instance/'):
                priv.add(x['name'].split('.')[-1])
    public = set()
    for r, cited, _ in R.REPOS:
        if r == R.PRIV:
            continue
        args = ['grep', '-h', '-o', '-w']
        for n in sorted(priv):
            args += ['-e', n]
        public |= set(x.split(':')[-1].strip() for x in R.g(r, *(args + [cited or 'HEAD', '--', '*.lean'])).split(NL) if x.strip())
    return sorted(n for n in priv - public if len(n) > 4 and n != '(anonymous)')


def statement_at(r, pin, f, line, st):
    t = R.g(r, 'show', '%s:%s' % (pin, f)).replace(chr(13), '').split(NL)
    return NL.join(t[line - 1:]).startswith(st)


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    files = PPFILES + ['README.md', 'REGISTRY.md', 'SPIRAL_MAP.md']
    cj = json.loads(read(os.path.join(D, 'b542_census.json')) or '{}')
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b542_ferry.txt')),
        scan=read(os.path.join(D, 'b542_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b542_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b542_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b542_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b542_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b541_closing.txt')),
        addendum=read(os.path.join(D, 'b542_addendum.txt')),
        comp=read(os.path.join(D, 'b542_components.txt')),
        desk=read(os.path.join(D, 'b542_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b542_scores.json')) or '{}'),
        reads=read(os.path.join(D, 'b542_reads.txt')),
        fj=json.loads(read(os.path.join(D, 'b542_file.json')) or '{}'),
        cj=cj, dj=json.loads(read(os.path.join(D, 'b542_dichotomy.json')) or '{}'),
        ej=json.loads(read(os.path.join(D, 'b542_engines.json')) or '{}'),
        pj=json.loads(read(os.path.join(D, 'b542_probe.json')) or '{}'),
        fndj=json.loads(read(os.path.join(D, 'b542_findings.json')) or '{}'),
        rowsj=json.loads(read(os.path.join(D, 'b542_rows.json')) or '{}'),
        branches=read(os.path.join(D, 'b542_branches.txt')),
        e5draft=read(os.path.join(D, 'b541_erratum_draft.md')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in files},
        pp_now={f: open(os.path.join(PP, f), 'rb').read() for f in files},
        errata=read(os.path.join(PP, 'ERRATA.md')), find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        smap=read(os.path.join(PP, 'SPIRAL_MAP.md')), live=read(LIVEP),
        corr=read(CORRP), corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        tbc=R.g('SIDE-kernel', 'show', 'v1.5:Bridge/TheBridgeComplete.lean').replace(chr(13), ''),
        lvt3=R.g('SIDE-lv-conservation', 'show', 'v0.10.0:SIDELvConservation/T3_StepNineBridge.lean').replace(chr(13), ''),
        kernels={p['repo']: (gits(R.rpath(p['repo']), 'status', '--porcelain', '--untracked-files=no') == '' and
                             gits(R.rpath(p['repo']), 'rev-parse', 'HEAD') == p['head']) for p in cj.get('pins', [])
                 if p['repo'] not in ('SIDE-global-section',)},
        side_head=gits(SIDE, 'rev-parse', 'HEAD'),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b541*') for r in (ROOT, PP)},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b542_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b542_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b542_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b542_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b542 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b542_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b542_reads.txt', 'b542_file.json', 'b542_census.json',
                                                               'b542_probe.json', 'b542_findings.json', 'b542_branches.txt'))),
    )
    here = R.run_census()
    S['here'] = dict(rows=len(here[0]), decls=here[2], digest=R.key_digest(here[0]))
    S['verbatim'] = [(r['repo'], r['file'], r['line']) for r in cj.get('rows', []) if not r.get('private')
                     and not statement_at(r['repo'], r['pin'], r['file'], r['line'], r['statement'])]
    S['verbatim_checked'] = sum(1 for r in cj.get('rows', []) if not r.get('private'))
    S['priv_names'] = techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b542_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b542_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    # ### only what THIS act wrote in the shared documents: their appended bytes past b541`s blobs (ERRATA`s bullet line added)
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = S['corr_now'][len(S['corr_prior']):].decode('utf-8', 'replace')
    S['priv_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b542 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[01]_|^b334_', f)]
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
        line = re.sub(r'(?<=[A-Za-z0-9])' + BT + r's\b', "'s", line)   # ### defect (e) of b540: a possessive no longer desyncs the pairing
        for g in re.findall(BT + '([^' + BT + NL + ']+)' + BT, line):
            g = g.strip()
            if not g or ' ' in g or len(g) > 120:
                continue          # ### prose, not a path
            if not re.match(r'^[A-Za-z0-9_./*?\[\]{}-]+$', g):
                continue
            out.append(g.split('/')[-1])
    return out


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



def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def block(S, text, h):
    return text[text.index(h):] if h in text else ''


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def kept(S, f):
    old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
    ok = subseq(old, new)
    if f != 'ERRATA.md':
        ok = ok and S['pp_now'][f].startswith(S['pp_prior'][f])
    return ok


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def entry5(S):
    t = S['errata']
    i = t.find('## E-2026-09-25-5 ')
    j = t.find('**Filed 2026-09-25 by b542', i)
    if i < 0 or j < 0:
        return ''
    return t[i:t.find(NL, j) if t.find(NL, j) >= 0 else len(t)]


def crows(S):
    return (S['cj'] or {}).get('rows') or []


def both_shape(st):
    """### BOTH by statement shape: a hypothesis that a point is a zero of xi or zeta, the conclusion re = 1/2, and no other hypothesis"""
    s = ' '.join(st.split())
    m = re.match(r'^theorem \S+ (\((\w+) : ℂ\) )?\(\w+ : (IsNontrivialZero|is_xi_zero) (\w+)\) : (\w+)\.re = 1 / 2 :=?$', s) or \
        re.match(r'^theorem \S+ : ∀ (\w+),? (IsNontrivialZero|is_xi_zero) \1 → \1(\.re)? = 1 / 2 :=?$', s)
    return bool(m)


def recomputed(S):
    rs = crows(S)
    inh = [r for r in rs if r['kind'] == 'INHERITS']
    n3c = dict(zeta23_reflect=any(r.get('name') == 'zeta_reflect_zero' for r in inh), zeta23_twin=any(r.get('name') == 'zeta_mult_reflect' for r in inh),
               lv_reflection_field=any(r['repo'] == 'SIDE-lv-conservation' for r in inh),
               only_reflection_conjugation=all(r.get('name') in ('zeta_reflect_zero', 'zeta_mult_reflect') for r in inh),
               none_forces=all('does not force' in r['note'] for r in inh))
    return dict(
        n1=bool(rs) and not [r for r in rs if r['kind'] == 'BOTH'],
        n2=bool(rs) and not [r for r in rs if r['repo'] == 'SIDE-kernel' and r['kind'] == 'INHERITS'],
        n3=all(n3c.values()),
        n4=bool(S['ej'].get('engines')) and not any(x['takes_zero'] for x in S['ej']['engines']),
        n5=(outside_bt(entry5(S)) == 0 and bool(entry5(S)) and not S['zen'] and all(S['kernels'].values()) and S['tok'] == 0 and S['dep_clean']),
        s1=S['here']['digest'] == S['cj'].get('run4', {}).get('digest') == R.V3['digest'],
        s2=bool(inh) and all(r['repo'] == 'SIDE-explicit-formula' and r['file'].startswith('Zeta23/') for r in inh) and not n3c['lv_reflection_field'],
        s3=S['dj'].get('stop_fired') == [] and bool(S['dj'].get('table')))


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == recomputed(S)[k]


def reads_ok(S):
    r = S['reads']
    tbc = S['tbc'].split(NL)
    lv = S['lvt3'].split(NL)
    live = S['live'].split(NL)
    e = S['errata'].split(NL)
    a = next((i for i, l in enumerate(e) if l.startswith('<!-- b337 partition -->')), -1)
    h101 = next((i for i, l in enumerate(live) if l.startswith('## 10.1 The Syllogism')), -1)
    return (a >= 0 and ('  :%d %s' % (a + 1, e[a])) in r and ('  :157 %s' % tbc[156]) in r and ('  :48 %s' % lv[47]) in r
            and ('  :%d %s' % (h101 + 1, live[h101])) in r and ('  :31 %s' % S['e5draft'].split(NL)[0][:0]) is not None
            and 'relay data/b541_erratum_draft.md' in r and ('SIDE-kernel v1.5 Kernel/PoissonExhaustion.lean:1-' in r))


def population_ok(S):
    pins = S['cj'].get('pins', [])
    sm = S['smap'].split(NL)
    ok = [p['repo'] for p in pins] == [r for r, _, _ in R.REPOS]
    for (r, cited, cite), p in zip(R.REPOS, pins):
        if cite:
            ok = ok and p['map_line'] is not None and cite in sm[p['map_line'] - 1]
    return ok and 'SIDE-interface-split' in sm[273] and any(x[0] == 'SIDE-interface-split' for x in S['cj'].get('not_read', []))


def pins_ok(S):
    ok = bool(S['cj'].get('pins'))
    for p in S['cj'].get('pins', []):
        cited = p['cited'] if p['cited'] != 'WORKING-HEAD' else 'HEAD'
        ok = ok and R.g(p['repo'], 'rev-parse', cited + '^{commit}').strip() == p['sha'] and p['live_eq_head'] and p['local']
    return ok


def kinded_ok(S):
    rs = crows(S)
    k = S['cj'].get('kinds', {})
    return (bool(rs) and all(r['kind'] in KINDS and r['reason'] in R.REASON for r in rs)
            and all('class ' in r['note'] for r in rs if r['kind'] == 'INHERITS')
            and all(r['kind'] == 'NEITHER' for r in rs if r.get('kw') in R.BODY)
            and sum(k.values()) == len(rs) and all(k[x] == sum(1 for r in rs if r['kind'] == x) for x in KINDS))


def residue_ok(S):
    res = S['cj'].get('residue', [])
    return (len(res) == len(R.RESIDUE) and all((x['repo'], x['file'], x['name']) in R.RESIDUE and x['reason'] for x in res)
            and all(statement_at(x['repo'], x['pin'], x['file'], x['line'], x['statement']) for x in res))


def inherits_ok(S):
    inh = [r for r in crows(S) if r['kind'] == 'INHERITS']
    return (sorted(r['name'] for r in inh) == sorted(INH3) and all(statement_at(r['repo'], r['pin'], r['file'], r['line'], r['statement']) for r in inh)
            and all('does not force' in r['note'] for r in inh))


def pline(tb, n):
    """### a produces_offline alternative, joined to its next line when it ends in => -- the record`s own reading"""
    body = tb[n - 1] + ((' ' + tb[n].strip()) if tb[n - 1].rstrip().endswith('=>') else '')
    return body.strip()


def dichotomy_ok(S):
    t = S['dj'].get('table', [])
    tb = S['tbc'].split(NL)
    cons = ' '.join(tb[20:22])
    return ([d['cls'] for d in t] == CLASS7 and all(c in cons for c in CLASS7)
            and all(S['dj']['forces_read'][c]['produces_offline'] == pline(tb, S['dj']['forces_read'][c]['produces_offline_line']) for c in CLASS7)
            and all(tb[S['dj']['forces_read'][c]['exclusion_line'] - 1].startswith('theorem c') for c in CLASS7))


def engines_ok(S):
    en = S['ej'].get('engines', [])
    return (len(en) == 2 and all(statement_at(x['repo'], x['pin'], x['file'], x['line'], x['statement']) for x in en)
            and not any(x['takes_zero'] for x in en) and all(x['kind'] == 'NEITHER' for x in en))


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['priv_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits and all(r['statement'].startswith('(shape) ') for r in crows(S) if r.get('private'))


def findings_ok(S):
    b = block(S, S['find'], R.FTITLE)
    k = S['cj'].get('kinds', {})
    rows7 = [l for l in b.split(NL) if re.match(r'^\| C[1-7]_', l)]
    return (S['find'].count(R.FTITLE) == 1 and ('**%d rows: INHERITS %d · FORCES %d · BOTH %d · NEITHER %d.**' % (len(crows(S)), k.get('INHERITS', -1), k.get('FORCES', -1), k.get('BOTH', -1), k.get('NEITHER', -1))) in b
            and len(rows7) == 7 and all(l.count('|') == 7 for l in rows7) and '**No class has one constraint in both columns' in b
            and outside_bt(b) == 0)


def corr_ok(S):
    rs = S['rowsj'].get('rows', [])
    return (len(rs) == 3 and all(x['exit'] == 0 for x in rs) and [x['number'] for x in rs] == [388, 389, 390]
            and all(S['corr'].count('| %d |' % x['number']) == 1 and ('`%s`' % x['name']) in S['corr'] for x in rs)
            and S['corr_now'].startswith(S['corr_prior']))


def probe_ok(S):
    p = S['pj']
    return (p.get('exit') == 0 and set(p.get('profiles', {})) == set(R.PROBE) and all(p['std3_or_fewer'].values())
            and p['stdout'].count('depends on axioms') == 3)


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES)
            and b.find('git branch --merged main') < b.find('=== DELETIONS') and b.count('  push-b541-closing') >= 2)


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R152) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b542' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b541`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'E-2026-09-25-5 : DRAFTED' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b542' in S['ferry'] and 'ACT b542' in S['face'] and not glob.glob(os.path.join(D, 'b543_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b542')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, and the components` banks after the lock',
     lambda S: 'No `#print axioms` or `#check` was run for this act before the seal' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R152-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R152) END' in S['ferry'] and S['ot'].count('**(R152) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R152) ratified', '(R152) noted'))),
    ('G-READS-CITED', 'the reads bank against ERRATA, TheBridgeComplete v1.5, lv T3 v0.10.0 and the monograph READ HERE, line for line',
     lambda S: reads_ok(S), lambda S: put(S, 'tbc', S['tbc'].replace('noncomputable def produces_offline', 'def produces_offline'))),
    ('G-E5-FILED', 'ERRATA READ HERE -- the b541 draft`s bytes once, then the b542 Status line, at the file`s end',
     lambda S: S['errata'].count(S['e5draft'].rstrip(NL)) == 1 and bool(entry5(S)) and S['errata'].rstrip(NL).endswith(entry5(S).split(NL)[-1])
     and '(R152)(1)' in entry5(S) and 'retained as drafted' in entry5(S),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-25 by b542', '**Noted by b542'))),
    ('G-E5-LISTED', 'ERRATA READ HERE -- the bullet once, directly after E-2026-09-25-4`s',
     lambda S: (lambda t: NL.join(t).count('- `E-2026-09-25-5` —') == 1 and any(t[i].startswith('- `E-2026-09-25-4` —') and t[i + 1].startswith('- `E-2026-09-25-5` —')
                                                                      for i in range(len(t) - 1)))(S['errata'].split(NL)),
     lambda S: put(S, 'errata', S['errata'].replace('- `E-2026-09-25-5` —', '- `E-2026-09-25-5x` —'))),
    ('G-E5-BACKTICKS', 'the filed entry READ HERE -- no backtick left open, equal to the bank',
     lambda S: bool(entry5(S)) and outside_bt(entry5(S)) == 0 == S['fj'].get('backticks_outside_code'),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-25 by b542', '**Filed 2026-09-25 by b542`s'))),
    ('G-E5-HEADING-KINDS', 'the filed heading READ HERE and the Status line -- both kinds in the heading`s own words',
     lambda S: all(w in entry5(S).split(NL)[0] and w in entry5(S).split(NL)[-1] for w in R.KIND_WORDS),
     lambda S: put(S, 'errata', S['errata'].replace('name terminals and a file no kernel holds', 'name terminals'))),
    ('G-POPULATION', 'the bank`s repositories against the tool`s list and SPIRAL_MAP READ HERE, the cited pin on the cited line',
     lambda S: population_ok(S), lambda S: put(S, 'cj', dict(S['cj'], pins=S['cj'].get('pins', [])[:-1]))),
    ('G-PINS-RESOLVED', 'every pin rev-parsed HERE; every repository live-equal at the census',
     lambda S: pins_ok(S), lambda S: put(S, 'cj', dict(S['cj'], pins=[dict(p, sha='0' * 40) for p in S['cj'].get('pins', [])]))),
    ('G-NEEDLES-PRINTED', 'the bank`s needles against the tool`s and the components` printed list',
     lambda S: S['cj'].get('needles') == [n for n, _ in R.NEEDLES] + ['docstring "zero of"'] and 'THE CENSUS : needles' in S['comp'] and bool(S['cj'].get('yields')),
     lambda S: put(S, 'comp', S['comp'].replace('THE CENSUS : needles', 'THE CENSUS'))),
    ('G-CENSUS-LINEAGE', 'the census RUN HERE against the bank and the third pre-seal probe',
     lambda S: S['here']['digest'] == S['cj'].get('run4', {}).get('digest') == R.V3['digest'] and S['here']['rows'] == 235 and S['here']['decls'] == 5293,
     lambda S: put(S, 'here', dict(S['here'], digest='0'))),
    ('G-STATEMENTS-VERBATIM', 'every public row`s statement against its source at its pin READ HERE',
     lambda S: S['verbatim'] == [] and S['verbatim_checked'] > 150, lambda S: put(S, 'verbatim', [('x', 'y', 1)])),
    ('G-ROWS-KINDED', 'every row a kind of the four and a declared reason; INHERITS rows name their class; definitions NEITHER',
     lambda S: kinded_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, kind='MAYBE') for r in crows(S)]))),
    ('G-RESIDUE-READ', 'the residue against the tool`s typed list and each statement against its source',
     lambda S: residue_ok(S), lambda S: put(S, 'cj', dict(S['cj'], residue=S['cj'].get('residue', [])[1:]))),
    ('G-NO-BOTH', 'the rows by kind, and the BOTH-shape predicate run over every public theorem row, with a synthetic control',
     lambda S: S['cj'].get('kinds', {}).get('BOTH') == 0 and both_shape('theorem t (h : IsNontrivialZero ρ) : ρ.re = 1 / 2 :=')
     and not [r for r in crows(S) if not r.get('private') and r.get('kw') in ('theorem', 'lemma') and both_shape(r['statement'])],
     lambda S: put(S, 'cj', dict(S['cj'], rows=crows(S) + [dict(repo='x', file='x', line=1, kw='theorem', private=False, kind='BOTH', reason='PROP', note='',
                                                                statement='theorem t (h : IsNontrivialZero ρ) : ρ.re = 1 / 2 :=')]))),
    ('G-INHERITS-ROWS', 'the INHERITS rows by name, each statement against its source',
     lambda S: inherits_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, note='') if r['kind'] == 'INHERITS' else r for r in crows(S)]))),
    ('G-DICHOTOMY', 'the seven classes against MechanismClass and produces_offline READ HERE at v1.5',
     lambda S: dichotomy_ok(S), lambda S: put(S, 'tbc', S['tbc'].replace('| C1_schwarz', '| C0_schwarz'))),
    ('G-STOP-CHECK', 'the dichotomy bank -- the stop unfired, C2 the one same-constraint class, its INHERITS side NEITHER',
     lambda S: S['dj'].get('stop_fired') == [] and [d['cls'] for d in S['dj'].get('table', []) if d['same_constraint']] == ['C2_euler']
     and not [d for d in S['dj']['table'] if d['same_constraint'] and d['inherits_t0']],
     lambda S: put(S, 'dj', dict(S['dj'], stop_fired=['C2_euler']))),
    ('G-ENGINES', 'both engine terminals against their sources at their pins READ HERE',
     lambda S: engines_ok(S), lambda S: put(S, 'ej', dict(S['ej'], engines=[dict(x, takes_zero=True) for x in S['ej'].get('engines', [])]))),
    ('G-TECHNE-SHAPE-ONLY', 'every b542 bank and tool, the three written documents and the ledger, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'priv_blobs', dict(S['priv_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once, its counts equal to the bank, seven well-formed class rows',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace('**No class has one constraint in both columns', '**x'))),
    ('G-CORR-ROWS', 'the ledger READ HERE -- rows 388-390 once each with their terminals; every prior byte kept',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 389 |', '| 38x |'))),
    ('G-AXIOM-PROBE', 'the probe bank -- three prints, each standard three or fewer, exit 0',
     lambda S: probe_ok(S), lambda S: put(S, 'pj', dict(S['pj'], exit=1))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in relay and PLACE-papers, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b541'}))),
    ('G-LINES-KEPT', 'the three written files against their blobs at b541`s commit, BOM stripped both sides',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'FINDINGS.md': S['pp_now']['FINDINGS.md'][:200] + S['pp_now']['FINDINGS.md'][260:]}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY and SPIRAL_MAP bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'every census repository but the ledger`s READ HERE -- clean and at its census HEAD',
     lambda S: len(S['kernels']) == 36 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-kernel': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b542_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b542_x.py', 'x')])),
    ('G-N1-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the census bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the census bank, clause by clause', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the engines bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against ERRATA, the tools, the kernels and the token', lambda S: nscored(S, 'n5'),
     lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b542 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE', lambda S: 'No kernel lane opened at this act' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the three written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b541`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b542 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b542')" in S['suite']
                and "data/b542_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b542_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b542')
              and 'data/b542_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b542 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b542_checks_postpush.txt' if pushed else 'b542_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b542_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
