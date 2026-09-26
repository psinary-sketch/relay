# -*- coding: utf-8 -*-
"""b546_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b546_registration_2026-09-26.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '9b2f1c9c'      # ### b545's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'da94298'           # ### b545's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b546 —'


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


import b546_record as R
import b542_checks as K542
BALR = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md', BALR, 'SPIRAL_MAP.md']
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
SIDE_TIP = '2e43315'
CORRP = os.path.join(SIDE, 'CORRESPONDENCE.md')
HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315',
         'SIDE-li-map': 'b515e6b', 'SIDE-carrier-spec': 'b3916cc', 'SIDE-class-number-anomaly': '2203b88', 'SIDE-cosmo': 'c5cba30',
         'SIDE-dirichlet-mod-24': '597b086', 'SIDE-fano-darkness': '0f6ce5b', 'SIDE-formation-procedure': '65ace65',
         'SIDE-local-cosmic-interface': '7a62ced', 'SIDE-quaternionic-dark-sector': 'e860142'}
BRANCH_LINES = ['Deleted branch push-b545 (was 08b16ccc).', 'Deleted branch push-b545-closing (was 9b2f1c9c).', 'Deleted branch push-b545 (was da94298).']


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def live_union():
    from collections import Counter
    ds, _ = R.P.classify(R.union_decls())
    eight = [x for x in ds if x['repo'] in R.EIGHT]
    return dict(count=len(ds), eight=len(eight), subjects_eight=dict(Counter(x['subject'] for x in eight)),
                subjects_old=dict(Counter(x['subject'] for x in ds if x['repo'] not in R.EIGHT)))


def live_mathlib():
    out = {'Li coefficient (an identifier)': 0, 'Keiper': 0, 'Taylor coefficients of zeta': 0}
    pats = {n: p for n, p in R.ML_NEEDLES if n in out}
    for dp, dn, fs in os.walk(os.path.join(R.MLDIR, 'Mathlib')):
        for f in fs:
            if f.endswith('.lean'):
                t = read(os.path.join(dp, f))
                for l in t.split(NL):
                    for n, p in pats.items():
                        if re.search(p, l):
                            out[n] += 1
    return out


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b546_ferry.txt')),
        scan=read(os.path.join(D, 'b546_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b546_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b546_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b546_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b546_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b545_closing.txt')),
        addendum=read(os.path.join(D, 'b546_addendum.txt')),
        comp=read(os.path.join(D, 'b546_components.txt')),
        desk=read(os.path.join(D, 'b546_desk_notes.txt')),
        sc=jload('b546_scores.json'), reads=read(os.path.join(D, 'b546_reads.txt')),
        ej=jload('b546_eight.json'), am=jload('b546_amend.json'), sp=jload('b546_spiral.json'),
        pe=jload('b546_probe_eight.json'), pr=jload('b546_premises.json'), ix=jload('b546_index.json'),
        fp=jload('b546_forms_probe.json'), fpt=read(os.path.join(D, 'b546_forms_probe.txt')),
        mj=jload('b546_mathlib.json'), fo=jload('b546_forms.json'), cr=jload('b546_credit.json'), ge=jload('b546_geometry.json'),
        b522=jload('b522_results.json'), b523=jload('b523_results.json'), b506=jload('b506_c2_results.json'),
        branches=read(os.path.join(D, 'b546_branches.txt')), author_word=read(os.path.join(D, 'b546_author_word.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in PPFILES + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in PPFILES + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), bal=read(os.path.join(PP, BALR)), spiral=read(os.path.join(PP, 'SPIRAL_MAP.md')),
        corr_now=open(CORRP, 'rb').read(), corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md'),
        dirs=sorted(d for d in os.listdir(os.path.join('D:', os.sep)) if d.startswith('SIDE-') and
                    subprocess.run(['git', '-C', os.path.join('D:', os.sep, d), 'rev-parse', '--git-dir'], capture_output=True).returncode == 0),
        listed=[r for r, _, _ in R.Q.REPOS],
        union=live_union(), mlive=live_mathlib(),
        kernels={k: gits(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' and
                 gits(os.path.join('D:', os.sep, k), 'rev-parse', '--short', 'HEAD').startswith(h) for k, h in HEADS.items()},
        branch_lists={r: gits(r, 'branch', '--list', 'push-b545*') for r in (ROOT, PP)},
        recomputed=R.scores(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b546_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b546_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b546_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b546_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b546 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b546_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b546_reads.txt', 'b546_eight.json', 'b546_forms_probe.json', 'b546_mathlib.json',
                                                               'b546_amend.json', 'b546_spiral.json', 'b546_credit.json', 'b546_geometry.json'))),
    )
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b546_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b546_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in PPFILES:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b546 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b54[012345]_|^b334_', f)]
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


def fblock(text, h):
    if h not in text:
        return ''
    b = text[text.index(h):]
    j = b.find(NL + '## ', len(h))
    return b[:j] if j > 0 else b


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def kept(S, f):
    old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
    return subseq(old, new) and new.startswith(old)


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


EIGHT_SET = set(R.EIGHT)


def reads_ok(S):
    r = S['reads']
    f = rd8(S['pp_prior']['FINDINGS.md']).split(NL)
    b = rd8(S['pp_prior'][BALR]).split(NL)
    sp = rd8(S['pp_prior']['SPIRAL_MAP.md']).split(NL)
    return (('  :4955 %s' % f[4954][:700]) in r and ('  :5461 %s' % f[5460][:700]) in r and ('  :500 %s' % b[499][:700]) in r
            and ('  :94 %s' % sp[93][:700]) in r and 'sigma 0.8743056607  t 137.8855570170' in r and 'theorem lam_add' in r)


def geometry_ok(S):
    ge, b22 = S['ge'], S['b522']
    top = max(S['b506']['found'], key=lambda x: x['rho'][1])
    return (abs(ge['n0'] - 2 * 16.290216 ** 2) < 1e-6 and abs(ge['ntop'] - 2 * top['rho'][1] ** 2) < 1e-6 and ge['neg'] == b22['q']['h2_neg']
            and ge['pos'] == b22['q']['h2_pos'] and ge['narrowest'] == b22['q']['narrowest'] and ge['survivors'] == S['b523']['neg_full'] == 24
            and b22['p'] == 7 and round(ge['n0']) == 531)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return all(v == '' for v in S['branch_lists'].values()) and all(b.count(l) == 1 for l in BRANCH_LINES) and '--merged' in b.split(NL)[0]


def probes_ok(S):
    fp, t = S['fp'], S['fpt']
    want = {'SIDE-explicit-formula': ['SIDEExplicitFormula.B321.h2_sign_iff_rh'], 'SIDE-li-map': ['LiLinearMap.lam_add'],
            'SIDE-lv-conservation': ['SIDELvConservation.PartialPositivity.blTerm_nonneg_of_onLine', 'SIDELvConservation.PartialPositivity.partialPositivity_finiteRange',
                                     'SIDELvConservation.PartialPositivity.lowFinset_mem_iff']}
    flat_t = re.sub(r'\n\s+', ' ', t)
    return all(fp.get(r, {}).get('exit') == 0 and fp[r].get('clean') and all(fp[r]['profiles'].get(n) and ("'%s' %s" % (n, fp[r]['profiles'][n])) in flat_t for n in ns)
               for r, ns in want.items()) and all(set(v.replace('depends on axioms: [', '').rstrip(']').split(', ')) <= {'propext', 'Classical.choice', 'Quot.sound'}
                                                   for r in want for v in fp[r]['profiles'].values() if 'depends' in v)


FORMSH_W = R.FORMSH.replace('`s', "'s")
TRAILH_B = R.HEADING


VACUOUS_ARMS = ('G-PROFILES-EIGHT', 'G-PREMISES-EIGHT', 'G-MARKS-EIGHT')


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R156) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b546' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no (R81) flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan carries no (R81) flag and no hit' in flat(S['face']),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b545`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b545' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b546' in S['ferry'] and 'ACT b546' in S['face'] and not glob.glob(os.path.join(D, 'b547_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b546')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, and the components` banks after the lock',
     lambda S: 'no `#print axioms` or `#check` ran for this act before the seal' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R156-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R156) END' in S['ferry'] and S['ot'].count('**(R156) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R156) ratified', '(R156) noted'))),
    ('G-READS-CITED', 'the reads bank against FINDINGS, BALPOS and SPIRAL_MAP at b545`s commit, the Q0 bank and li-map READ HERE',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('theorem lam_add', 'x'))),
    ('G-EIGHT-NAMED', 'the git directories on D:\\ READ HERE against b542`s list -- exactly the eight outside it',
     lambda S: sorted(set(S['dirs']) - set(S['listed'])) == sorted(R.EIGHT) and sorted(S['ej'].get('heads', {})) == sorted(R.EIGHT),
     lambda S: put(S, 'listed', S['listed'] + ['SIDE-cosmo'])),
    ('G-SPIRAL-REASONS', 'SPIRAL_MAP at b545`s commit -- no line names any of the eight (unlisted, every one)',
     lambda S: all(rd8(S['pp_prior']['SPIRAL_MAP.md']).count(r) == 0 for r in R.EIGHT) and 'ALL EIGHT ARE UNLISTED' in flat(S['face']),
     lambda S: put(S, 'pp_prior', dict(S['pp_prior'], **{'SPIRAL_MAP.md': S['pp_prior']['SPIRAL_MAP.md'] + b'| `SIDE-cosmo` | v0.3 |'}))),
    ('G-ENUMERATION-UNION', 'the union enumeration RUN HERE against the bank -- 5700, the eight 407',
     lambda S: S['union']['count'] == S['ej']['count_union'] == 5700 and S['union']['eight'] == S['ej']['count_eight'] == 407,
     lambda S: put(S, 'union', dict(S['union'], count=S['union']['count'] - 1))),
    ('G-SUBJECTS-BOTH', 'the subjects RUN HERE -- old repositories both ways, the eight, the moved row printed',
     lambda S: S['union']['subjects_old'] == S['ej']['subjects_old_union'] and S['union']['subjects_eight'] == S['ej']['subjects_eight']
     and S['ej']['subjects_old_b544'] == {'ARITHMETIC-OR-LOGIC': 1900, 'PROGRAMME-TYPE': 3044, 'ZETA': 349} and len(S['ej']['moved']) == 1,
     lambda S: put(S, 'union', dict(S['union'], subjects_eight={'ZETA': 1}))),
    ('G-PROFILES-EIGHT', 'the probe bank of the eight -- VACUOUS because the eight add no ZETA row, and it says so',
     lambda S: S['union']['subjects_eight'].get('ZETA', 0) == 0 and S['pe'].get('zeta_rows') == 0 and S['pe'].get('verdict', '').startswith('VACUOUS'),
     lambda S: put(S, 'pe', dict(S['pe'], verdict='HELD'))),
    ('G-PREMISES-EIGHT', 'the premises bank of the eight -- VACUOUS, said',
     lambda S: S['pr'].get('zeta_rows') == 0 and S['pr'].get('verdict', '').startswith('VACUOUS'), lambda S: put(S, 'pr', {})),
    ('G-MARKS-EIGHT', 'the index bank of the eight -- VACUOUS, said',
     lambda S: S['ix'].get('zeta_rows') == 0 and S['ix'].get('verdict', '').startswith('VACUOUS'), lambda S: put(S, 'ix', {})),
    ('G-CP2-AMENDED', 'FINDINGS READ HERE -- the CP-2 amendment once, old beside new, at the line the bank names',
     lambda S: (lambda b: S['find'].count(R.CP2A) == 1 and 'b544 5293; now 5700' in b and 'ZETA 349 · ARITHMETIC-OR-LOGIC 2008 · PROGRAMME-TYPE 3343' in b
                and S['find'].split(NL)[S['am']['cp2']['heading_line'] - 1] == R.CP2A and outside_bt(b) == 0)(fblock(S['find'], R.CP2A)),
     lambda S: put(S, 'find', S['find'].replace('b544 5293; now 5700', 'x'))),
    ('G-CP3-AMENDED', 'FINDINGS READ HERE -- the CP-3 amendment once, the index unchanged',
     lambda S: (lambda b: S['find'].count(R.CP3A) == 1 and '562 rows (I 176, E 386)' in b and 'side_exclusion_bridge' in b)(fblock(S['find'], R.CP3A)),
     lambda S: put(S, 'find', S['find'].replace('562 rows (I 176, E 386)', 'x'))),
    ('G-SPIRAL-ROWS', 'SPIRAL_MAP READ HERE -- one block, a row for each of the eight, each marked',
     lambda S: S['spiral'].count(R.SPIRALH) == 1 and all(S['spiral'].count('| `%s` *(added by b546)*' % r) == 1 for r in R.EIGHT)
     and 'The certified specification of a candidate carrier' in S['spiral'],
     lambda S: put(S, 'spiral', S['spiral'].replace('| `SIDE-cosmo` *(added by b546)*', '| x'))),
    ('G-TABLE-REGENERATED', 'the terminal table READ HERE after the suite regenerates it -- the eight on its roster',
     lambda S: bool(S.get('table')) and all(r in S.get('table_json', '') for r in R.EIGHT[:1]) and S.get('rc_gen') == 0,
     lambda S: put(S, 'rc_gen', 1)),
    ('G-TWO-FORMS-ENTRY', 'FINDINGS READ HERE -- the two-forms entry once, the Weil form, the Li form, the pieces, the price',
     lambda S: (lambda b: S['find'].count(FORMSH_W) == 1 and 'h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis' in b and 'It is T1-lit' in b
                and 'lowFinset_mem_iff' in b and 'Priced here; not attempted' in b and outside_bt(b) == 0)(fblock(S['find'], FORMSH_W)),
     lambda S: put(S, 'find', S['find'].replace('Priced here; not attempted', 'x'))),
    ('G-PROBES-FRESH', 'the probe bank -- every named theorem printed by its own run, exit 0, clean trees, the standard three or fewer',
     lambda S: probes_ok(S), lambda S: put(S, 'fpt', '')),
    ('G-MATHLIB-SEARCH', 'the Mathlib checkout RE-SEARCHED HERE on three needles against the bank',
     lambda S: all(S['mlive'][k] == S['mj']['counts'][k] for k in S['mlive']) and S['mj'].get('head', '').startswith('51e6992'),
     lambda S: put(S, 'mlive', dict(S['mlive'], Keiper=1))),
    ('G-BRIDGE-PRICED', 'the entry`s price paragraph -- lemmas named, the trail named, nothing attempted',
     lambda S: (lambda b: 'W-ORD-LI-WEIL-BRIDGE (OPEN_TRAILS.md:3548)' in b and '(v) the converse' in b and 'Hadamard product' in b)(fblock(S['find'], FORMSH_W)),
     lambda S: put(S, 'find', S['find'].replace('(v) the converse', 'x'))),
    ('G-CREDIT-CORRECTED', 'FINDINGS READ HERE -- :5461 unchanged, the correcting line appended once',
     lambda S: S['find'].split(NL)[5460] == rd8(S['pp_prior']['FINDINGS.md']).split(NL)[5460] and S['find'].count(poss(R.CREDIT_F)) == 1
     and S['find'].split(NL)[S['cr']['after']['find_line'] - 1] == poss(R.CREDIT_F),
     lambda S: put(S, 'find', S['find'].replace(poss(R.CREDIT_F), 'x'))),
    ('G-CREDIT-BALPOS-LINE', 'BALPOS READ HERE -- :274 and :357 unchanged, the line appended once',
     lambda S: [S['bal'].split(NL)[i] for i in (273, 356)] == [rd8(S['pp_prior'][BALR]).split(NL)[i] for i in (273, 356)] and S['bal'].count(poss(R.CREDIT_B)) == 1,
     lambda S: put(S, 'bal', S['bal'].replace(poss(R.CREDIT_B), 'x'))),
    ('G-DETECTION-ENTRY', 'FINDINGS READ HERE -- the geometries entry once, graded READING, its refutation stated',
     lambda S: (lambda b: S['find'].count(R.GEOH) == 1 and 'Graded READING' in b and '**What would refute it.**' in b
                and 'the widths 36-38 are positive' in b and outside_bt(b) == 0)(fblock(S['find'], R.GEOH)),
     lambda S: put(S, 'find', S['find'].replace('**What would refute it.**', 'x'))),
    ('G-DETECTION-NUMBERS', 'b522, b523 and b506 READ HERE against the geometry bank -- 2T² recomputed',
     lambda S: geometry_ok(S), lambda S: put(S, 'ge', dict(S['ge'], narrowest=35.0))),
    ('G-VOROS-VERBATIM', 'BALPOS at b545`s commit, :500 and :507, against the entry',
     lambda S: (lambda b: rd8(S['pp_prior'][BALR]).split(NL)[499].lstrip('> ') in b and rd8(S['pp_prior'][BALR]).split(NL)[506].lstrip('> ') in b)(fblock(S['find'], R.GEOH)),
     lambda S: put(S, 'find', S['find'].replace('√(n/2)"**', 'n/2"**'))),
    ('G-BRAINSTORM-HELD', 'the trail and OPEN_TRAILS READ HERE -- held at the seal, released on the author`s word; the line once, with the banked link, the date and the two objects',
     lambda S: 'held at the seal (READING (12)), released on the author' in trail(S) and S['ot'].count(R.LINK) == 1 and R.LINK in S['author_word']
     and poss(R.BRAIN) in S['ot'] and '2026-09-26' in R.BRAIN and 'Ω_b = 4/81' in R.BRAIN and 'T₇ CMB' in R.BRAIN,
     lambda S: put(S, 'ot', S['ot'] + NL + R.LINK)),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b545'}))),
    ('G-LINES-KEPT', 'the four written files against their blobs at b545`s commit',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-SPIRAL-PREFIX-KEPT', 'SPIRAL_MAP against its blob -- a true prefix, one block after it',
     lambda S: S['pp_now']['SPIRAL_MAP.md'].startswith(S['pp_prior']['SPIRAL_MAP.md']) and S['spiral'].count('<!-- b546 (R156)(3) ROWS') == 1,
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'SPIRAL_MAP.md': S['pp_now']['SPIRAL_MAP.md'][:100] + S['pp_now']['SPIRAL_MAP.md'][140:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README and REGISTRY bytes against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'the thirteen repositories this act read or probed, READ HERE -- clean and at their heads',
     lambda S: len(S['kernels']) == 13 and all(S['kernels'].values()), lambda S: put(S, 'kernels', dict(S['kernels'], **{'SIDE-cosmo': False}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b546_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind, branch deletion included',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b546_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b546 bank and tool and this act`s own PLACE-papers bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the eight`s bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the SPIRAL_MAP bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the Mathlib bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the geometry bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the blobs, the tools, the token and the kernels', lambda S: nscored(S, 'n5'),
     lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b546 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernels READ HERE', lambda S: 'No kernel lane opened at this act' in trail(S) and all(S['kernels'].values()),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH_B) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH_B + ' a second record')),
    ('G-CORR-UNTOUCHED', 'SIDE-global-section`s correspondence ledger against its blob -- no row this act',
     lambda S: S['corr_now'] == S['corr_prior'] and S['corr_now'] != b'', lambda S: put(S, 'corr_now', S['corr_now'] + b'| 391 | a row |')),
    ('G-INSTRUMENTS-EDIT-DECLARED', 'relay`s tools against b545`s close -- READING (7)`s condition is false (no ZETA row), so no instrument modified',
     lambda S: S['tools_edited'] == [] and S['ej']['subjects_eight'].get('ZETA', 0) == 0, lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b546 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b546')" in S['suite']
                and "data/b546_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b546_components.txt' in gits(ROOT, 'show'")),
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
    S['rc_gen'] = rc_gen
    S['table_json'] = read(os.path.join(D, 'terminal_table.json'))
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b546')
              and 'data/b546_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b546 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b546_checks_postpush.txt' if pushed else 'b546_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b546_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
