# -*- coding: utf-8 -*-
"""b559_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b558's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The kernel arms read the kernel's own tree, refs and git state, and Lean's own output in the run files.
### ### `G-PEEK-DECLARED` carries (R169)(1)(b): file times before the push, content digests against the pushed tree after it.
"""
import io
import glob
import hashlib
import fnmatch
import json
import time
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
FACE = os.path.join(D, 'b559_registration_2026-09-29.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '22e5d2e4'      # ### b558's closing commit -- relay's tip before this act's housekeeping
PRIOR_PP = '5a911f4'           # ### b558's PLACE-papers commit
PRIOR_GS = 'a91d941'           # ### SIDE-global-section before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b559 —'


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


import b559_record as R
import b542_checks as K542
import terminal_table as TT
FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md']
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md',
         'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
AFTER_LOCK = ('b559_constants.json', 'b559_literal.json', 'b559_e0.json', 'b559_axioms.txt', 'b559_branch.txt', 'b559_findings.json')
BEFORE_LOCK = ('b559_ferry.txt', 'b559_ferry_scan.txt', 'b559_pins_stepzero.txt')


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (b540 defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'), ('branch', ' -d'), ('branch', ' -D'), ('worktree', ' remove'))] + [
        '(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def jload(n):
    return json.loads(read(os.path.join(D, n)) or '{}')


def utc_epoch(text, label):
    import calendar
    m = re.search(re.escape(label) + r' \(UTC\) : (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)Z', text or '')
    return calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S')) if m else None


def pushed_digest_ok(name):
    """### (R169)(1)(b): the bank's working bytes (CR stripped) against its blob in the PUSHED tree (origin/main), by sha256."""
    p = os.path.join(D, name)
    work = open(p, 'rb').read().replace(b'\r\n', b'\n') if os.path.exists(p) else None
    pub = blob(ROOT, 'origin/main:data/' + name)
    return bool(work) and bool(pub) and hashlib.sha256(work).hexdigest() == hashlib.sha256(pub).hexdigest()


def added_epoch(name):
    t = gits(ROOT, 'log', '--diff-filter=A', '--format=%ct', 'origin/main', '--', 'data/' + name).split()
    return int(t[-1]) if t else None


def peek_by_digest(face, lockn, scan):
    """### (R169)(1)(b), carried from b558_checks.py as 673a39e2 left it, pointed at this act's banks."""
    lk, rn = utc_epoch(face, 'locked at'), utc_epoch(lockn, 'run at')
    after = lk is not None and all(pushed_digest_ok(x) and (added_epoch(x) or 0) > lk for x in AFTER_LOCK)
    before = (lk is not None and rn is not None and rn < lk and all(pushed_digest_ok(x) for x in BEFORE_LOCK)
              and 'ferry file                    : b559_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b559_ferry_scan.txt', 'b559_pins_stepzero.txt')))
    return after, before


def is_pushed():
    return (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b559')
            and 'data/b559_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=40):
    """### the commits of this act in a repository: subjects opening `b559 --`, or housekeeping naming (R169)."""
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b559 --') or (s.startswith('housekeeping:') and ('(R169)' in s or 'b559' in s)):
                out.append(h)
    return out


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    locks = sorted(glob.glob(os.path.join(D, 'b559_lockgate_notes*.txt')))
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b559_ferry.txt')),
        scan=read(os.path.join(D, 'b559_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b559_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b559_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b559_pins_stepzero.txt')),
        lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b558_closing.txt')),
        addendum=read(os.path.join(D, 'b559_addendum.txt')),
        desk=read(os.path.join(D, 'b559_desk_notes.txt')),
        sc=jload('b559_scores.json'), reads=read(os.path.join(D, 'b559_reads.txt')),
        rerun=read(os.path.join(D, 'b559_b558_postpush_rerun.txt')),
        hk={c: sorted(x for x in gits(ROOT, 'show', '--name-only', '--pretty=format:', c).split(NL) if x.strip()) for c in (R.HK_REFRESH, R.HK_TOOL)},
        hk_parents=[gits(ROOT, 'rev-parse', '--short=8', R.HK_REFRESH + '^'), gits(ROOT, 'rev-parse', '--short=8', R.HK_TOOL + '^')],
        hk_msg=git(ROOT, 'log', '-1', '--pretty=%B', R.HK_TOOL),
        cj=jload('b559_constants.json'), ctxt=read(os.path.join(D, 'b559_constants.txt')),
        v02={f: R.at(R.V02, f) for f in set(r['file'] for r in jload('b559_constants.json').get('rows', []))},
        k=R.kstate(),
        main_tree=[x for x in gits(KER, 'ls-tree', '-r', '--name-only', 'main').split(NL) if x.strip()],
        elab=read(os.path.join(D, 'b559_elab_attempt1.txt')),
        pr=R.prints(), lit=jload('b559_literal.json'), littxt=read(os.path.join(D, 'b559_literal.txt')),
        e0=jload('b559_e0.json'), e0txt=read(os.path.join(D, 'b559_e0.txt')),
        pc=jload('b559_price.json'), fj=jload('b559_findings.json'), rows=jload('b559_rows.json'),
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        branches=read(os.path.join(D, 'b559_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        mains=R.mains(),
        trial=dict(head=gits(R.P.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.P.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b558*') for r in (ROOT, PP)},
        recomputed={k2: v for k2, v in R.scores().items() if not k2.startswith('_')},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b559_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b559_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b559_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b559_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        tool_commits=[x for x in gits(ROOT, 'log', '--pretty=%h', PRIOR_RELAY + '..HEAD', '--', 'tools/b558_checks.py').split(NL) if x.strip()],
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b559 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b559_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    S['pushed'] = is_pushed()
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    else:
        S['after_lock'] = all(os.path.exists(os.path.join(D, x)) and os.path.getmtime(os.path.join(D, x)) > os.path.getmtime(FACE) for x in AFTER_LOCK)
        S['before_lock'] = all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in BEFORE_LOCK)
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b559_') and os.path.isfile(os.path.join(D, f))] + \
        [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b559_')] + \
        [os.path.join(KER, 'SIDEExplicitFormula', 'DetectionRegion.lean')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    blobs['DetectionRegion.lean@branch'] = rd8(blob(KER, R.BRANCH + ':SIDEExplicitFormula/DetectionRegion.lean'))
    for f in FIXED:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = NL.join(l for l in S['corr'].split(NL) if l not in set(S['corr_prior'].split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, R.BRANCH)):
        for h in act_commit(repo, rev):
            k |= set(os.path.basename(x) for x in gits(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-8]_|^b334_', f)]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS -- b558's reader, carried (a possessive no longer
    ### desyncs the pairing; a bare-wildcard directory glob reads as the files that directory holds)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    out = []
    for line in w.split(NL):
        line = re.sub(r'(?<=[A-Za-z0-9])' + BT + r's\b', "'s", line)
        for g in re.findall(BT + '([^' + BT + NL + ']+)' + BT, line):
            g = g.strip()
            if not g or ' ' in g or len(g) > 120:
                continue
            if not re.match(r'^[A-Za-z0-9_./*?\[\]{}-]+$', g):
                continue
            base = g.split('/')[-1]
            if not re.search(r'[A-Za-z0-9]', base):
                root = ROOT if g.startswith('relay/') else (PP if g.startswith('PLACE-papers/') else None)
                if root:
                    rel = g.split('/', 1)[1]
                    out.extend(os.path.basename(x) for x in glob.glob(os.path.join(root, *rel.split('/'))))
                continue
            out.append(base)
    return out


def strip_prose(text):
    """### ### **A `G-NO*` ARM MUST NOT READ THE ACT'S OWN SENTENCE SAYING IT DID NOT DO IT** -- b487's rule, carried."""
    t = re.sub(r'"""[\s\S]*?"""', ' ', text or '')
    t = re.sub(r"'''[\s\S]*?'''", ' ', t)
    t = re.sub(r'^\s*#.*$', ' ', t, flags=re.M)
    return t


def live_limb_guard(suite):
    """### The guard against a control that leaves a live limb is RUNNING the control on every arm (b495's lesson, carried)."""
    need = ['p = bool(pred(pos(S)))',
            'defective.append(name)',
            'not defective']
    return [n for n in need if n not in suite]


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


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
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0].split(',')[0]


def word_of(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper() if not k.startswith('h9') else 'H9' + k[2:]) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


P = R.poss


def reads_ok(S):
    r = S['reads']
    need = ['PowerLimit.lean:1082', 'PowerLimit.lean:1092', 'PowerLimit.lean:245', 'PowerLimit.lean:1193', 'PowerWindow.lean:481',
            'PowerWindow.lean:483', 'PowerWindow.lean:274', 'H2Sign.lean:24', 'H2Sign.lean:29', 'Seam.lean:101', 'Defs.lean:121',
            'Defs.lean:124', 'Main.lean:286', 'LocalCount.lean:310', 'DecayBound.lean:63', 'OPEN_TRAILS.md:11151', 'OPEN_TRAILS.md:11332',
            'b554_sign_pattern.txt:79', 'FINDINGS.md:3044', 'FINDINGS.md:57', 'b551_components.txt:24',
            'lean-toolchain = leanprover/lean4:v4.33.0-rc2', 'mathlib rev = 51e6992efd06126df61a496bebf8f49482a4e129']
    return all(x in r for x in need) and '### BEYOND THE FILE' not in r


def hk_ok(S):
    return (S['hk'].get(R.HK_REFRESH) == ['data/b558_refresh.txt'] and S['hk'].get(R.HK_TOOL) == ['tools/b558_checks.py']
            and S['hk_parents'] == [PRIOR_RELAY, R.HK_REFRESH] and 'TEST VERDICT : BOTH POLARITIES BEHAVE' in S['hk_msg']
            and 'LIVE PASSING : 63' in S['hk_msg'])


def rerun_ok(S):
    r = S['rerun']
    return ('POST-PUSH READING' in line_with(r, 'THE SUITE') and 'LIVE PASSING : 63' in line_with(r, 'ARMS RUN')
            and 'ALL ARMS PASS AND EVERY CONTROL BEHAVES' in line_with(r, 'VERDICT :')
            and line_with(r, 'G-PEEK-DECLARED').split()[1:2] == ['PASS'])


def constants_ok(S):
    rows = S['cj'].get('rows', [])
    names = [r['name'] for r in rows]
    need = ['zeroSide_eventually_neg', 'tie_term_neg', 'rest_term_small', 'dominant_summable', 'paperFT_decay', 'zetaZeroConfig_local_count']
    ok = bool(rows) and all(n in names for n in need)
    for r in rows:
        ln, head, body = R.decl_span(S['v02'].get(r['file'], ''), r['name'])
        ok = ok and ln == r['line'] == r['found_line'] and head == r['statement'] and r['kind'] in R.KINDS and bool(r['witness'])
    return ok


def markers_ok(S):
    c = S['cj']
    body = {r['name']: R.decl_span(S['v02'].get(r['file'], ''), r['name'])[2] for r in c.get('rows', [])}
    nc = sorted(r['name'] for r in c.get('rows', []) if r['kind'] == 'NON-CONSTRUCTIVE')
    return ('Metric.tendsto_atTop' in body.get('zeroSide_eventually_neg', '') and 'tendsto_tsum_of_dominated_convergence' in body.get('rest_tendsto_zero', '')
            and nc == sorted(c.get('nonconstructive', [])) == ['rest_tendsto_zero', 'zeroSide_eventually_neg']
            and c.get('h9a') is False and c.get('markers_ok') is True
            and all(any(m in body.get(n, '') for m in ('Metric.tendsto_atTop', 'tendsto_tsum_of_dominated_convergence')) for n in nc))


def branch_ok(S):
    k = S['k']
    return (k['parent'] == R.V02 and k['remote'] == k['branch'] != '' and k['status'] == ['A']
            and k['files'] == ['AxiomCheckDetection.lean', 'SIDEExplicitFormula/DetectionRegion.lean'])


def held_or_merged(S):
    k = S['k']
    held = (not k['ancestor']) and k['tags'] == [] and k['remote'] == k['branch'] != ''
    merged = k['ancestor'] and k['main'] == k['branch'] and bool(k['tags'])
    return held or merged


def nosorry_ok(S):
    return (not any(x.endswith(('DetectionRegion.lean', 'AxiomCheckDetection.lean')) for x in S['main_tree'])
            and S['k']['main'].startswith('81ae175'))


def elab_ok(S):
    e = S['elab']
    m = re.search(r'exit (\d+) -- (\d+) s -- errors (\d+)', e)
    return bool(m) and m.group(1) == '0' and m.group(3) == '0' and e.count('declaration uses `sorry`') == 2 and ': error' not in e


def axioms_ok(S):
    pr = S['pr']
    return (all(n in pr for n in R.NEW) and all(('sorryAx' in pr[n]) == (n in R.HELDN) for n in R.NEW)
            and all(pr[n] == R.STD3 for n in R.NEW if n not in R.HELDN))


def literal_ok(S):
    v = S['lit'].get('variants', {})
    return (v.get('a', {}).get('exit') == 1 and v.get('a', {}).get('errors', 0) > 0 and v.get('b', {}).get('exit') == 1
            and 'Membership ?m.1 ((ℝ → ℂ) → Prop)' in S['littxt'] and 'Unknown identifier `weilTest`' in S['littxt'])


def e0_ok(S):
    e = S['e0']
    return (e.get('grade') == 'T4' and e.get('derives') is False and all(e.get('grades', {}).get(n) == 'DERIVES' for n in R.COMPILED)
            and 'THE SALT-CHECK' in S['e0txt'] and 'THE ROWGEN DIFF: NOT RUN' in S['e0txt'] and 'ρ.re - 1 / 2 = 0' in e.get('statement', ''))


def price_ok(S):
    ot = rd8(S['pp_now']['OPEN_TRAILS.md']).split(NL)
    ln = [i + 1 for i, l in enumerate(ot) if l.startswith(P(R.PRICEH))]
    return ln == [S['pc'].get('line')] and kept(S, 'OPEN_TRAILS.md') and 'PowerLimit.lean' in ot[ln[0] - 1] if ln else False


def reading_ok(S):
    F = S['find'].split(NL)
    n = S['fj'].get('reading_line')
    return (bool(n) and F[n - 1].startswith('**The reading, `(R169)`(6), descriptive voice.**') and '33.194255' in F[n - 1]
            and '38.961415' in F[n - 1] and 'b554_sign_pattern' in F[n - 1] and ':5529' in F[n - 1])


def findings_ok(S):
    F = S['find'].split(NL)
    b = fblock(S['find'], P(R.FH))
    return (S['find'].count(P(R.FH)) == 1 and F[S['fj'].get('heading_line', 0) - 1] == P(R.FH) and '**Next:** W-ORD-LI-WEIL-BRIDGE' in b
            and 'H9a REFUTED' in b and 'stated and held at the named obstacle' in b and kept(S, 'FINDINGS.md'))


def corr_ok(S):
    rows = [l for l in S['corr'].split(NL) if l.startswith('| 394 |')]
    return (len(rows) == 1 and 'detection-region-b559' in rows[0] and 'HELD' in rows[0] and S['rows'].get('exit') == 0
            and S['corr'].startswith(S['corr_prior'].rstrip(NL)))


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b558 (was ') == 2
            and b.count('Deleted branch push-b558-closing (was ') == 1 and 'toolchain-trial-b551' in b)


def mains_ok(S):
    m = S['mains']
    return (len(m) == len(R.PRE_HEADS) and all(v == [] for k2, v in m.items() if k2 != 'SIDE-global-section')
            and set(m.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'})


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R169) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b559' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no (R81) flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan carries no hit and no flag' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'the LAST lock-gate run file, a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 4'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b558`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b558' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b559' in S['ferry'] and 'ACT b559' in S['face'] and not glob.glob(os.path.join(D, 'b560_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b559')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; before the push file times, after it content digests against the pushed tree ((R169)(1)(b))',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE SEAT FORMED ITS READING OF H9a BEFORE THIS SEAL' in flat(S['face'])
                and S['after_lock'] and S['before_lock']),
     lambda S: put(S, 'after_lock', False)),
    ('G-R169-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R169) END' in S['ferry'] and S['ot'].count('**(R169) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R169) ratified', '(R169) noted'))),
    ('G-READS-CITED', 'the reads bank -- the cited lines at v0.2 by path and line, the toolchain and rev, the trails, the bench, FINDINGS',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('PowerLimit.lean:1092', 'x'))),
    ('G-HOUSEKEEPING-ALONE', 'relay`s two housekeeping commits READ HERE -- each one file, in order after b558`s close, the test quoted',
     lambda S: hk_ok(S), lambda S: put(S, 'hk', dict(S['hk'], **{R.HK_TOOL: ['tools/b558_checks.py', 'tools/terminal_table.py']}))),
    ('G-RERUN-RECORD', 'the re-run record on b558`s push -- post-push reading, 63 of 63, the arm PASS',
     lambda S: rerun_ok(S), lambda S: put(S, 'rerun', S['rerun'].replace('LIVE PASSING : 63', 'LIVE PASSING : 62'))),
    ('G-CONSTANTS-BANKED', 'the constants bank against the v0.2 sources READ HERE -- each statement and line recomputed, one kind of three',
     lambda S: constants_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, line=r['line'] + 1) if i == 0 else r for i, r in enumerate(S['cj'].get('rows', []))]))),
    ('G-H9A-MARKERS', 'the v0.2 proof bodies READ HERE -- the limit markers in the two non-constructive rows, H9a REFUTED',
     lambda S: markers_ok(S), lambda S: put(S, 'cj', dict(S['cj'], nonconstructive=['zeroSide_eventually_neg']))),
    ('G-BRANCH-FROM-V02', 'the kernel`s refs READ HERE -- the branch`s parent v0.2, the remote equal, added files only',
     lambda S: branch_ok(S), lambda S: put(S, 'k', dict(S['k'], parent='81ae1758f28e280f4e924e8acd76b4b76ae4ac9d'))),
    ('G-BRANCH-HELD-OR-MERGED', 'the kernel`s refs READ HERE -- HELD: at the remote, no ancestor of main, no v0.3; or merged and tagged',
     lambda S: held_or_merged(S), lambda S: put(S, 'k', dict(S['k'], ancestor=True))),
    ('G-NO-SORRY-ON-MAIN', 'the kernel`s main tree READ HERE -- neither new file on it; main at its pre-act head',
     lambda S: nosorry_ok(S), lambda S: put(S, 'main_tree', S['main_tree'] + ['SIDEExplicitFormula/DetectionRegion.lean'])),
    ('G-EXISTING-UNCHANGED', 'the branch against v0.2 by name-status READ HERE -- A only',
     lambda S: S['k']['status'] == ['A'], lambda S: put(S, 'k', dict(S['k'], status=['A', 'M']))),
    ('G-ELAB-PRINTED', 'the elaboration bank -- exit 0, errors 0, the two sorry warnings',
     lambda S: elab_ok(S), lambda S: put(S, 'elab', S['elab'].replace('errors 0', 'errors 2'))),
    ('G-AXIOMS-PRINTED', 'Lean`s own prints -- every new declaration printed; sorryAx exactly on j0 and detection_region',
     lambda S: axioms_ok(S), lambda S: put(S, 'pr', dict(S['pr'], detection_region=list(R.STD3)))),
    ('G-LITERAL-PROBE', 'the literal bank -- both variants exit 1, Lean`s Membership and weilTest messages',
     lambda S: literal_ok(S), lambda S: put(S, 'littxt', S['littxt'].replace('Membership', 'x'))),
    ('G-E0-READ', 'the E0 bank -- T4, not DERIVES, the companions DERIVES, the salt-check and the rowgen line, the conclusion read',
     lambda S: e0_ok(S), lambda S: put(S, 'e0', dict(S['e0'], grade='DERIVES'))),
    ('G-PRICE-LINE', 'OPEN_TRAILS READ HERE -- the price line once at its banked line, the file kept',
     lambda S: price_ok(S), lambda S: put(S, 'pc', dict(S['pc'], line=-1))),
    ('G-READING-ENTERED', 'FINDINGS READ HERE -- the (R169)(6) reading at its banked line, the bench`s numbers and :5529 in it',
     lambda S: reading_ok(S), lambda S: put(S, 'fj', dict(S['fj'], reading_line=1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once at its banked line, HELD`s title, H9a REFUTED, the next act, the file kept',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-CORR-ROW', 'CORRESPONDENCE READ HERE -- row 394 once, the branch and HELD in it, the ledger a true prefix extended',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 394 |', '| 395 |'))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in two repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b558'}))),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the written files against their blobs at b558`s commit',
     lambda S: all(kept(S, f) for f in FIXED),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-CEILING-UNCHANGED', 'README, REGISTRY, FACES_LEDGER, SPIRAL_MAP, the map, FOUNDATIONS and the method keystones against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in OTHER if 'A_Place_to_Stand' not in f and f != 'ERRATA.md'),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'REGISTRY.md': S['pp_now']['REGISTRY.md'] + b' '}))),
    ('G-KERNEL-MAINS-UNTOUCHED', 'every kernel`s main READ HERE against its pre-act head -- nothing but SIDE-global-section`s ledger row',
     lambda S: mains_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-explicit-formula': ['SIDEExplicitFormula/DetectionRegion.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b559_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b559_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b559 bank and tool, the branch module and this act`s ledger bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the constants', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against Lean`s print and the E0 bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the absence of a compiled j0', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=False))),
    ('G-N4-SCORED', 'the desk against the absence of a compiled j0', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=True))),
    ('G-N5-SCORED', 'the desk against the kernel`s refs', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the branch, the mains, the tools, the deposit and the trial worktree', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-H9-SCORED', 'the desk against the constants and the prints -- (R169)(4)`s four, each word from the banks',
     lambda S: all(nscored(S, x) for x in ('h9a', 'h9b', 'h9c', 'h9d')),
     lambda S: put(S, 'sc', dict(S['sc'], h9a=True))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b559 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the two written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-EDITED-AS-RULED', 'relay`s tools against b558`s close READ HERE -- b558_checks.py alone, in the one ruled commit',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == ['b558_checks.py'] and S['tool_commits'] == [R.HK_TOOL[:len(S['tool_commits'][0])] if S['tool_commits'] else 'x'],
     lambda S: put(S, 'tools_edited', ['b558_checks.py', 'terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b559 commit in four repositories and the housekeeping commits, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b559')" in S['suite']
                and "data/b559_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b559_components.txt' in gits(ROOT, 'show'")),
]


def regenerate():
    """### ### **(R107): THE GENERATOR IS PART OF THE CLOSING SUITE** -- re-run before anything is scored; its diff a cell."""
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    d = os.path.join(D, 'terminal_table_diff.json')
    diff = json.loads(read(d) or '{}')
    return r.returncode, diff


def main():
    S = sources()
    rc_gen, gen_diff = regenerate()
    S['table'] = read(os.path.join(D, 'terminal_table.md'))
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    names = [a[0] for a in ARMS]
    pushed = S['pushed']
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b559 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  G-PEEK-DECLARED reads %s' % ('CONTENT DIGESTS AGAINST THE PUSHED TREE (origin/main %s)' % gits(ROOT, 'rev-parse', '--short', 'origin/main')
                                        if pushed else 'FILE TIMES AGAINST THE FACE (before any checkout)'))
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
    stray = sorted(k for k in S['kinds']
                   if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
    if gen_diff.get('first_run'):
        rec('  ###   ### **NO PRIOR RUN TO DIFF AGAINST -- THIS CLOSE IS THE FIRST.**')
    else:
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
            % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
               len(gen_diff.get('changed') or [])))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d prior banks by time, none excepted.' % S['prior_checked'])
    rec('  ### ### **VACUOUS ARMS : %s.**' % ([a for a in VACUOUS_ARMS] or 'NONE'))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b559_checks_postpush.txt' if pushed else 'b559_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b559_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
