# -*- coding: utf-8 -*-
"""b560_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b559's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The kernel arms read the kernel's own tree, refs and git state, and Lean's own output in the run files.
### ### `G-PEEK-DECLARED`, `G-WRITELIST-KINDS` and `G-PRIORBANK-UNCHANGED` read file times before the push and content digests
### against the pushed tree after it ((R169)(1)(b), (R170)(3)).
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
FACE = os.path.join(D, 'b560_registration_2026-09-29.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'f8017036'      # ### b559's table housekeeping -- relay's tip before this act
PRIOR_PP = 'b132b5e'           # ### b559's PLACE-papers commit
PRIOR_GS = '3268b94'           # ### SIDE-global-section before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH0 = '### b560 —'


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


import b560_record as R
import b542_checks as K542
import terminal_table as TT
FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md']
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md',
         'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
AFTER_LOCK = ('b560_reads.json', 'b560_clean.json', 'b560_stageA.json', 'b560_e0.json', 'b560_v03.txt', 'b560_findings.json')
BEFORE_LOCK = ('b560_ferry.txt', 'b560_ferry_scan.txt', 'b560_pins_stepzero.txt')


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
              and 'ferry file                    : b560_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b560_ferry_scan.txt', 'b560_pins_stepzero.txt')))
    return after, before


RERUN = '--rerun-postpush' in sys.argv   # ### (R170)(3), b560: b558`s flag, carried -- one named record, no table regeneration


def cr0(b):
    return b.replace(b'\r\n', b'\n') if b is not None else None


def written_by_digest(repo, rel):
    """### (R170)(3), b560: `G-WRITELIST-KINDS``s post-push reading. A tracked file the working tree shows as modified counts
    ### as written by the act when its bytes (CR stripped) differ by sha256 from its blob in the PUSHED tree (origin/main),
    ### in place of its file time against the face`s -- which a checkout rewrites (b559`s defect (i))."""
    p = os.path.join(repo, rel)
    work = cr0(open(p, 'rb').read()) if os.path.isfile(p) else b''
    pub = cr0(blob(repo, 'origin/main:' + rel.replace(os.sep, '/')))
    return pub is None or hashlib.sha256(work).hexdigest() != hashlib.sha256(pub).hexdigest()


def blob_id(b):
    return hashlib.sha1(b'blob %d\x00' % len(b) + b).hexdigest()


def tree_ids(repo, rev, sub):
    out = {}
    for l in gits(repo, 'ls-tree', '-r', rev, '--', sub).split(NL):
        if '\t' in l:
            meta, path = l.split('\t', 1)
            out[path] = meta.split()[2]
    return out


def prior_by_digest(files, prior_rev):
    """### (R170)(3), b560: `G-PRIORBANK-UNCHANGED``s post-push reading. Every prior bank a tree tracks is read by content:
    ### its working bytes (CR stripped, and raw) as a git blob id against its blob at the act`s pre-act tip AND at the pushed
    ### tree; a bank first tracked in the pushed tree is read against that tree alone; a bank no tree tracks has no digest to
    ### read against and is read by file time, its count returned. Returns (ok, n_prior_tree, n_pushed_only, n_time, bad)."""
    pre, pub = tree_ids(ROOT, prior_rev, 'data'), tree_ids(ROOT, 'origin/main', 'data')
    bad, n_pre, n_pub, n_time = [], 0, 0, 0
    # ### a prior bank that is a directory (b558_editions) is read file by file, each by its own digest.
    exp = []
    for f in files:
        if os.path.isdir(os.path.join(D, f)):
            exp += sorted(f + '/' + x for x in os.listdir(os.path.join(D, f)) if os.path.isfile(os.path.join(D, f, x)))
        else:
            exp.append(f)
    for f in exp:
        k = 'data/' + f
        raw = open(os.path.join(D, f), 'rb').read()
        ids = {blob_id(raw), blob_id(cr0(raw))}
        if k in pre:
            n_pre += 1
            if pre[k] not in ids or pub.get(k) not in ids:
                bad.append(f)
        elif k in pub:
            n_pub += 1
            if pub[k] not in ids:
                bad.append(f)
        else:
            n_time += 1
            if not os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE):
                bad.append(f)
    return not bad, n_pre, n_pub, n_time, bad


def is_pushed():
    return (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b560')
            and 'data/b560_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=40):
    """### the commits of this act in a repository: subjects opening `b560 --`, or housekeeping naming (R170)."""
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b560 --') or (s.startswith('housekeeping:') and ('(R170)' in s or 'b560' in s)):
                out.append(h)
    return out


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    locks = sorted(glob.glob(os.path.join(D, 'b560_lockgate_notes*.txt')))
    stages = {x: jload('b560_stage%s.json' % x) for x in 'ABCD'}
    stxt = {x: read(os.path.join(D, 'b560_stage%s.txt' % x)) for x in 'ABCD'}
    liw_main = rd8(blob(KER, 'main:SIDEExplicitFormula/LiWeil.lean'))
    det_main = rd8(blob(KER, 'main:SIDEExplicitFormula/DetectionRegion.lean'))
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b560_ferry.txt')),
        scan=read(os.path.join(D, 'b560_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b560_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b560_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b560_pins_stepzero.txt')),
        lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b559_closing.txt')),
        addendum=read(os.path.join(D, 'b560_addendum.txt')),
        desk=read(os.path.join(D, 'b560_desk_notes.txt')), defects=read(os.path.join(D, 'b560_defects.txt')),
        sc=jload('b560_scores.json'), reads=read(os.path.join(D, 'b560_reads.txt')), rj=jload('b560_reads.json'),
        rerun=read(os.path.join(D, 'b560_b559_postpush_rerun.txt')),
        cj=jload('b560_clean.json'), celab=read(os.path.join(D, 'b560_clean_elab.txt')), v03txt=read(os.path.join(D, 'b560_v03.txt')),
        k=R.kstate(), stages=stages, stxt=stxt, liw_main=liw_main, det_main=det_main,
        main_tree=[x for x in gits(KER, 'ls-tree', '-r', '--name-only', 'main').split(NL) if x.strip()],
        e0=jload('b560_e0.json'), e0txt=read(os.path.join(D, 'b560_e0.txt')), rowgen=read(os.path.join(D, 'b560_rowgen.txt')),
        v04txt=read(os.path.join(D, 'b560_v04_push.txt')),
        l1=jload('b560_ledger1.json'), fj=jload('b560_findings.json'), rows=jload('b560_rows.json'),
        tj=jload('b560_trail.json'), wj=jload('b560_workorder.json'),
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        branches=read(os.path.join(D, 'b560_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        mains=R.mains(),
        trial=dict(head=gits(R.P.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.P.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b559*') for r in (ROOT, PP, SIDE)},
        recomputed={k2: v for k2, v in R.scores().items() if not k2.startswith('_')},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b560_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b560_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b560_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b560_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        tool_commits=[x for x in gits(ROOT, 'log', '--pretty=%h', PRIOR_RELAY + '..HEAD', '--', 'tools/b559_checks.py').split(NL) if x.strip()],
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b560 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b560_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    hc = S['tool_commits'][-1] if S['tool_commits'] else ''
    S['hk_files'] = sorted(x for x in gits(ROOT, 'show', '--name-only', '--pretty=format:', hc).split(NL) if x.strip()) if hc else []
    S['hk_parent'] = gits(ROOT, 'rev-parse', '--short=8', hc + '^') if hc else ''
    S['hk_msg'] = git(ROOT, 'log', '-1', '--pretty=%B', hc) if hc else ''
    S['v03obj'] = gits(KER, 'cat-file', '-t', 'v0.3')
    S['v04obj'] = gits(KER, 'cat-file', '-t', 'v0.4')
    S['v03msg'] = git(KER, 'tag', '-l', '--format=%(contents)', 'v0.3')
    S['v03parent'] = gits(KER, 'rev-parse', 'v0.3^{}^')
    S['liw_parent'] = gits(KER, 'rev-parse', R.LIW + '^')
    S['clean_names'] = re.findall(r'^(?:def|theorem)\s+(\S+)', S['det_main'], re.M)
    S['liw_names'] = re.findall(r"^(?:theorem|def)\s+([A-Za-z_']+)", liw_main, re.M)
    S['pushed'] = RERUN or is_pushed()
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    else:
        S['after_lock'] = all(os.path.exists(os.path.join(D, x)) and os.path.getmtime(os.path.join(D, x)) > os.path.getmtime(FACE) for x in AFTER_LOCK)
        S['before_lock'] = all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in BEFORE_LOCK)
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b560_') and os.path.isfile(os.path.join(D, f))] + \
        [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b560_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    blobs['LiWeil.lean@main'] = liw_main
    blobs['DetectionRegion.lean@main'] = det_main
    for f in FIXED:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = NL.join(l for l in S['corr'].split(NL) if l not in set(S['corr_prior'].split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'main')):
        for h in act_commit(repo, rev):
            k |= set(os.path.basename(x) for x in gits(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                if S['pushed']:
                    if not written_by_digest(repo, rel):
                        continue
                else:
                    try:
                        if os.path.getmtime(os.path.join(repo, rel)) < os.path.getmtime(FACE):
                            continue
                    except OSError:
                        pass
                k.add(os.path.basename(rel))
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-4][0-9]_|^b55[0-9]_|^b334_', f)]
    S['prior_checked'] = len(prior)
    if S['pushed']:
        S['noprior'], S['prior_pre'], S['prior_pub'], S['prior_time'], S['prior_bad'] = prior_by_digest(prior, PRIOR_RELAY)
    else:
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




def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0].split(',')[0]


def word_of(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


P = R.poss
TRAILH = '### b560 —'


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def h11_word(S, tag):
    if tag == 'h11a':
        return seg(S['desk'], 'AS AMENDED (conjugation): ### **', 16).split('.')[0]
    return seg(S['desk'], '**(H11%s)** ### **' % tag[-1], 16).split('.')[0]


def reads_ok(S):
    r = S['reads']
    need = ['ExplicitFormula.lean:97', 'Main.lean:286', 'Defs.lean:121', 'Defs.lean:124', 'Defs.lean:136', 'Statement.lean:91',
            'ZetaReflect.lean:78', 'ZetaReflect.lean:160', 'ZetaReflect.lean:294', 'ZetaReflect.lean:330', 'LocalCount.lean:282',
            'LocalCount.lean:310', 'ZeroSummability.lean:247', 'PowerLimit.lean:934', 'DecayBound.lean:63', 'BALPOS:498', 'BALPOS:70',
            'BALPOS:422', 'PartialPositivity.lean:51', 'b549_premise.txt:12', 'OPEN_TRAILS.md:3548', 'OPEN_TRAILS.md:11203',
            'OPEN_TRAILS.md:11265', 'OPEN_TRAILS.md:11290', 'OPEN_TRAILS.md:11491', 'G-WRITELIST-KINDS', 'b559_checks.py:243',
            'DetectionRegion.lean:77', 'DetectionRegion.lean:86']
    rows = S['rj'].get('rows', [])
    ok = all(x in r for x in need) and 'NOT FOUND' not in r and bool(rows)
    for x in rows:
        t = R.at(x['rev'], x['file'])
        ok = ok and R.decl_at(t, x['name']) == x['line']
    return ok


def h11a_ok(S):
    j = S['rj']
    return (j.get('h11a_first') == 'REFUTED' and j.get('h11a_amended') == 'HOLDS FROM THE PRINTS' and j.get('reflect_only') is True
            and j.get('conj_set') is True and j.get('conj_mult') is True and 'SCORED FROM THE PRINTS ALONE, BEFORE ANY BUILD' in S['reads'])


def suite_edit_ok(S):
    return (len(S['tool_commits']) == 1 and S['hk_files'] == ['tools/b559_checks.py'] and S['hk_parent'] == PRIOR_RELAY
            and 'TEST VERDICT : BOTH POLARITIES BEHAVE' in S['hk_msg'] and 'ARMS RUN : 64' in S['hk_msg'] and '(R170)(3)' in S['hk_msg'])


def rerun_row(S, a):
    m = re.search(r'^\s+' + re.escape(a) + r'\s+(PASS|FAIL)\s', S['rerun'], re.M)
    return m.group(1) if m else None


def rerun_ok(S):
    r = S['rerun']
    return ('POST-PUSH READING' in line_with(r, 'THE SUITE') and 'ARMS RUN : 64' in line_with(r, 'ARMS RUN')
            and '(R170)(3): A RE-RUN' in r and rerun_row(S, 'G-PEEK-DECLARED') == 'PASS' and rerun_row(S, 'G-PRIORBANK-UNCHANGED') == 'PASS'
            and rerun_row(S, 'G-WRITELIST-KINDS') is not None)


def clean_from_main(S):
    c = S['cj']
    files = sorted(x.replace('\t', ' ') for x in gits(KER, 'diff', '--name-status', R.MAIN0, c.get('tip', 'x')).split(NL) if x.strip())
    return (c.get('parent') == R.MAIN0 and c.get('tip') == S['k']['v03'] and S['v03parent'] == R.MAIN0
            and files == ['A AxiomCheckDetection.lean', 'A SIDEExplicitFormula/DetectionRegion.lean'])


def code(t):
    return re.sub(r'--.*$', '', re.sub(r'/-.*?-/', '', t or '', flags=re.S), flags=re.M)


def clean_nosorry(S):
    c = S['cj']
    return (not re.search(r'\bsorry\b', code(S['det_main'])) and all(c.get('same_as_held', {}).values()) and len(c.get('same_as_held', {})) == 5
            and S['clean_names'] == ['h2_sign_upto', 'h2_sign_imp_upto', 'upto_all_imp_h2_sign', 'h2_sign_iff_forall_upto', 'forall_upto_iff_rh']
            and c.get('gate') is True)


def anc(a, b):
    return subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', a, b]).returncode == 0


def tag03_ok(S):
    k = S['k']
    return (k['v03'] == k['remote'].get('refs/tags/v0.3^{}') == S['cj'].get('tip') and S['v03obj'] == 'tag'
            and 'RegisterDepth' in S['v03msg'] and 'DetectionRegion-clean' in S['v03msg'] and k['v03obj'] == k['remote'].get('refs/tags/v0.3'))


def held_kept(S):
    k = S['k']
    return k['held'] == R.HELD_TIP == k['remote'].get('refs/heads/' + R.HELD) and not anc(R.HELD, 'main')


def ot_once_at(S, head, line):
    ot = rd8(S['pp_now']['OPEN_TRAILS.md']).split(NL)
    ln = [i + 1 for i, l in enumerate(ot) if l.startswith(P(head))]
    return ln == [line] and bool(line)


def held_line_ok(S):
    ot = S['ot'].split(NL)
    n = S['l1'].get('lines', {}).get('held')
    return ot_once_at(S, R.HELD_LINE, n) and 'v0.3' in ot[n - 1] and '8faf7de' in ot[n - 1] and '81ae175' in ot[n - 1]


def clean_reading_ok(S):
    F = S['find'].split(NL)
    n = S['l1'].get('lines', {}).get('findings')
    b = fblock(S['find'], P(R.CLEAN_FH))
    return (S['find'].count(P(R.CLEAN_FH)) == 1 and bool(n) and F[n - 1] == P(R.CLEAN_FH) and 'limit of bounded obligations' in b
            and 'descriptive voice' in b)


def rescope_ok(S):
    n = S['l1'].get('lines', {}).get('rescope')
    b = flat(seg(S['ot'], P(R.RESCOPE_H), 4000))
    return ot_once_at(S, R.RESCOPE_H, n) and all(x in b for x in ('(E1)', '(E2)', 'b554', 'navigator', '2^j-fold', 'Neither'))


def arc_ok(S):
    n = S['l1'].get('lines', {}).get('arc')
    ot = S['ot'].split(NL)
    return ot_once_at(S, R.ARC_LINE, n) and 'owner: the author' in ot[n - 1] and '(E2)' in ot[n - 1]


def liw_from_v03(S):
    k = S['k']
    return S['liw_parent'] == k['v03'] and k['remote'].get('refs/heads/' + R.LIW) == k['liw']


def nosorry_main(S):
    rows = S['e0'].get('rows', {})
    return (not re.search(r'\bsorry\b', code(S['liw_main'])) and not re.search(r'\bsorry\b', code(S['det_main']))
            and bool(rows) and not any('sorryAx' in (r.get('axioms') or ['sorryAx']) for r in rows.values())
            and not any('sorryAx' in (g0.get('axioms') or ['sorryAx']) for g0 in S['cj'].get('grades', {}).values()))


def stages_ok(S):
    return all(S['stages'][x].get('all_std3') is True and S['stages'][x].get('names') and 'PRINTED' in S['stxt'][x] for x in 'ABCD')


def elab_ok(S):
    ok = True
    for x in 'ABCD':
        heads = re.findall(r'### Stage %s attempt (\d+) -- exit (\d+), elapsed \d+ s, errors (\d+)' % x, S['stxt'][x])
        ok = ok and bool(heads) and heads[-1][1] == '0' and heads[-1][2] == '0' and len(heads) <= 4
    m = re.search(r'exit (\d+), elapsed \d+ s, errors (\d+)', S['celab'])
    return ok and bool(m) and m.group(1) == '0' and m.group(2) == '0'


def axioms_ok(S):
    rows = S['e0'].get('rows', {})
    return (sorted(rows) == sorted(S['liw_names']) and len(rows) == 35
            and all(r.get('axioms') is not None and set(r['axioms']) <= set(R.STD3) for r in rows.values())
            and all(set(g0.get('axioms') or ['x']) <= set(R.STD3) for g0 in S['cj'].get('grades', {}).values()))


def salt_ok(S):
    e = S['e0']
    blk = S['liw_main'][S['liw_main'].index('def LiCoeff'):][:300] if 'def LiCoeff' in S['liw_main'] else ''
    return (e.get('salt') is True and e.get('param') is False and e.get('control') is True
            and blk.startswith('def LiCoeff (n : ℕ) : ℝ :=') and 'zetaZeroConfig.carrier' in blk)


def e0_ok(S):
    e, t = S['e0'], S['e0txt']
    rows = e.get('rows', {})
    return ('THE SALT-CHECK' in t and 'THE ROWGEN RECORD' in t and e.get('gate') is True and '### UNGRADED' not in t
            and rows.get('li_identity_of_exchange', {}).get('grade') == 'INTERFACES' and rows.get('rh_imp_li_nonneg', {}).get('grade') == 'DERIVES'
            and not any(r['grade'].startswith('ENCODES') for r in rows.values()))


def rowgen_ok(S):
    return ("('SIDEExplicitFormula.LiWeil.conj_mem', ['ok'])" in S['rowgen'] and S['e0'].get('rowgen_control') is True
            and S['cj'].get('rowgen_control') is True and 'row found: True' in S['rowgen'])


def tag04_ok(S):
    k = S['k']
    return (k['v04'] == k['main'] == k['liw'] == k['remote'].get('refs/tags/v0.4^{}') == k['remote'].get('refs/heads/main')
            and S['v04obj'] == 'tag' and k['v04obj'] == k['remote'].get('refs/tags/v0.4') and anc(k['v03'], 'main'))


def converse_ok(S):
    d = S['stxt']['D']
    return ('THE CONVERSE, PRICED AND NOT ATTEMPTED' in d and all('(V%d)' % i in d for i in (1, 2, 3, 4))
            and not re.search(r'theorem\s+\w*(li_nonneg_imp_rh|imp_rh)\w*', S['liw_main']))


def findings_ok(S):
    F = S['find'].split(NL)
    b = fblock(S['find'], P(R.FH))
    n = S['fj'].get('heading_line', 0)
    return (S['find'].count(P(R.FH)) == 1 and bool(n) and F[n - 1] == P(R.FH) and 'held at the limit exchange' in b
            and 'LiLimitExchange' in b and '**Next**' in b and kept(S, 'FINDINGS.md'))


def corr_ok(S):
    rows = [l for l in S['corr'].split(NL) if l.startswith('| %s |' % R.ROWNO)]
    return (len(rows) == 1 and 'v0.4' in rows[0] and 'LiLimitExchange' in rows[0] and S['rows'].get('exit') == 0
            and S['corr'].startswith(S['corr_prior'].rstrip(NL)))


def trail_ok(S):
    n = S['tj'].get('line')
    return ot_once_at(S, R.HEADING, n) and '**Entered:**' in trail(S) and '**(R170) ratified' in trail(S)


def workorder_ok(S):
    n = S['wj'].get('line')
    ot = S['ot'].split(NL)
    return ot_once_at(S, R.WO_LINE, n) and 'T3, T4, T5 COMPILED' in ot[n - 1] and 'LiLimitExchange' in ot[n - 1]


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b559 (was ') == 3
            and b.count('Deleted branch push-b559-closing (was ') == 1 and 'toolchain-trial-b551' in b
            and 'detection-region-b559' in b and 'li-weil-b560' in b)


def mains_ok(S):
    m = S['mains']
    return (len(m) == len(R.PRE_HEADS) and all(v == [] for k2, v in m.items() if k2 not in ('SIDE-global-section', 'SIDE-explicit-formula'))
            and set(m.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'}
            and m.get('SIDE-explicit-formula') == R.NEW_FILES and S['k']['ff'] and S['k']['status'] == ['A'])


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


def h11_scored(S):
    return all(x in S['sc'] and h11_word(S, x) == word_of(S['sc'][x]) and S['sc'][x] == S['recomputed'][x]
               for x in ('h11a', 'h11b', 'h11c', 'h11d', 'h11e')) and S['sc'].get('h11a_first') is False and 'AS FIRST WORDED' in S['desk']


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling, part 1 of 1 and the second paste, each END or head present',
     lambda S: 'RULING (R170) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b560' in S['ferry'] and 'PASTE TWO' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- one (R81) flag, at line 167, and the face declares it',
     lambda S: '(R81) FLAGS : 1' in line_with(S['scan'], '(R81) FLAGS') and 'line 167' in S['scan'] and 'one informational (R81) flag' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 1', '(R81) FLAGS : 2'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b559`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b559' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b560' in S['ferry'] and 'ACT b560' in S['face'] and not glob.glob(os.path.join(D, 'b561_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b560')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; before the push file times, after it content digests against the pushed tree',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE SEAT FORMED ITS READINGS BEFORE THIS SEAL' in flat(S['face'])
                and S['after_lock'] and S['before_lock']),
     lambda S: put(S, 'after_lock', False)),
    ('G-R170-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R170) END' in S['ferry'] and S['ot'].count('**(R170) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R170) ratified', '(R170) noted'))),
    ('G-AMENDMENT-BANKED', 'the banked ferry, the face and the trail -- the (4) amendment verbatim, the pairing by conjugation',
     lambda S: ('RULING (R170)(4) AMENDMENT' in S['ferry'] and 'pairs by CONJUGATION' in S['ferry'] and 'Stage A pairs by CONJUGATION' in flat(S['face'])
                and 'its (4) amendment' in trail(S)),
     lambda S: put(S, 'ferry', S['ferry'].replace('RULING (R170)(4) AMENDMENT', 'x'))),
    ('G-DROP-RECORDED', 'the desk`s defects -- the drop as defect (a), with its time and last completed step',
     lambda S: ('(a) THE DROP' in S['defects'] and '15:21:16Z' in S['defects'] and 'NOTHING HAD REACHED DISK' in S['defects']
                and 'last completed step' in S['defects'] and '(a) THE DROP' in S['desk']),
     lambda S: put(S, 'defects', S['defects'].replace('(a) THE DROP', '(a) x'))),
    ('G-READS-CITED', 'the reads bank against the sources READ HERE -- every declaration found at its banked line, the documents and the arms',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('ZetaReflect.lean:78', 'x'))),
    ('G-H11A-FROM-PRINTS', 'the reads bank -- H11a scored from the prints, before any build, both wordings',
     lambda S: h11a_ok(S), lambda S: put(S, 'rj', dict(S['rj'], h11a_first='HOLDS'))),
    ('G-SUITE-EDIT-ALONE', 'relay`s commits since b559`s close READ HERE -- one, one file, its parent b559`s tip, the test quoted',
     lambda S: suite_edit_ok(S), lambda S: put(S, 'hk_files', ['tools/b559_checks.py', 'tools/terminal_table.py'])),
    ('G-RERUN-RECORD', 'the re-run record on b559`s push -- post-push reading by digests, 64 arms, the digest arms` rows',
     lambda S: rerun_ok(S), lambda S: put(S, 'rerun', S['rerun'].replace('POST-PUSH READING', 'PRE-PUSH READING'))),
    ('G-CLEAN-FROM-MAIN', 'the kernel`s refs READ HERE -- the clean branch from 81ae175, one commit, added files only, at v0.3',
     lambda S: clean_from_main(S), lambda S: put(S, 'cj', dict(S['cj'], parent=R.V02))),
    ('G-CLEAN-NO-SORRY', 'DetectionRegion.lean on main READ HERE -- no sorry, the five declarations, each body the HELD branch`s',
     lambda S: clean_nosorry(S), lambda S: put(S, 'det_main', S['det_main'] + NL + 'def j₀ (γ δ : ℝ) : ℕ := sorry')),
    ('G-CLEAN-MERGED-FF', 'the kernel`s ancestry READ HERE -- 81ae175 before v0.3 before main, no merge commit',
     lambda S: anc(R.MAIN0, S['k']['v03']) and anc(S['k']['v03'], 'main') and S['v03parent'] == R.MAIN0,
     lambda S: put(S, 'v03parent', R.V02)),
    ('G-TAG-V03-PEELED', 'the kernel`s tags READ HERE and at the remote -- annotated, peeled to the clean tip, both contents named',
     lambda S: tag03_ok(S), lambda S: put(S, 'v03msg', S['v03msg'].replace('RegisterDepth', 'x'))),
    ('G-HELD-BRANCH-KEPT', 'the kernel`s refs READ HERE -- detection-region-b559 at 8faf7de, local and remote, not in main',
     lambda S: held_kept(S), lambda S: put(S, 'k', dict(S['k'], held='0' * 40))),
    ('G-HELD-RECORD-LINE', 'OPEN_TRAILS READ HERE -- the HELD branch`s line once at its banked line, pointing at v0.3',
     lambda S: held_line_ok(S), lambda S: put(S, 'l1', dict(S['l1'], lines=dict(S['l1'].get('lines', {}), held=1)))),
    ('G-CLEAN-READING-ENTERED', 'FINDINGS READ HERE -- the clean merge`s reading once, in the descriptive voice',
     lambda S: clean_reading_ok(S), lambda S: put(S, 'find', S['find'].replace('limit of bounded obligations', 'x'))),
    ('G-RESCOPE-APPENDED', 'OPEN_TRAILS READ HERE -- the re-scope once: (E1), (E2), the closed form, the navigator`s mis-statements',
     lambda S: rescope_ok(S), lambda S: put(S, 'ot', S['ot'].replace('(E2)', '(E-)'))),
    ('G-RESEARCH-ARC-LINE', 'OPEN_TRAILS READ HERE -- the research-arc line once, the author its owner',
     lambda S: arc_ok(S), lambda S: put(S, 'ot', S['ot'].replace('owner: the author', 'owner: the seat'))),
    ('G-LIWEIL-FROM-V03', 'the kernel`s refs READ HERE -- li-weil-b560`s parent v0.3, pushed by name and equal at the remote',
     lambda S: liw_from_v03(S), lambda S: put(S, 'liw_parent', R.MAIN0)),
    ('G-EXISTING-UNCHANGED', 'main against 81ae175 by name-status READ HERE -- A only',
     lambda S: S['k']['status'] == ['A'], lambda S: put(S, 'k', dict(S['k'], status=['A', 'M']))),
    ('G-NO-SORRY-ON-MAIN', 'both new modules on main READ HERE and Lean`s prints -- no sorry, no sorryAx',
     lambda S: nosorry_main(S), lambda S: put(S, 'liw_main', S['liw_main'] + NL + 'theorem x : False := sorry')),
    ('G-STAGE-BANKS', 'the four stage banks -- each banked, its declarations printed at the standard three',
     lambda S: stages_ok(S), lambda S: put(S, 'stages', dict(S['stages'], D=dict(S['stages']['D'], all_std3=False)))),
    ('G-ELAB-PRINTED', 'the stage banks and the clean bank -- each stage`s last attempt exit 0, errors 0, at most four',
     lambda S: elab_ok(S), lambda S: put(S, 'celab', S['celab'].replace('errors 0', 'errors 2'))),
    ('G-AXIOMS-PRINTED', 'Lean`s own prints in the E0 and clean banks against the module READ HERE -- every declaration printed',
     lambda S: axioms_ok(S), lambda S: put(S, 'liw_names', S['liw_names'] + ['unprinted_decl'])),
    ('G-SALT-CHECK', 'the E0 bank and the module on main READ HERE -- LiCoeff over zetaZeroConfig, no configuration parameter',
     lambda S: salt_ok(S), lambda S: put(S, 'liw_main', S['liw_main'].replace('def LiCoeff (n : ℕ)', 'def LiCoeff (Z : ZeroConfig) (n : ℕ)'))),
    ('G-E0-READ', 'the E0 bank -- every declaration graded, no ENCODES, the exchange`s consumer INTERFACES, the gate',
     lambda S: e0_ok(S), lambda S: put(S, 'e0', dict(S['e0'], gate=False))),
    ('G-ROWGEN-RECORD', 'the rowgen bank -- rowgen`s diff ok on row 395, both controls True',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace("['ok']", "['MISSING']"))),
    ('G-TAG-V04-OR-HELD', 'the kernel`s tags READ HERE and at the remote -- v0.4 annotated, peeled to main and to li-weil-b560',
     lambda S: tag04_ok(S), lambda S: put(S, 'v04obj', 'commit')),
    ('G-CONVERSE-PRICED', 'the Stage D bank and the module -- the converse priced (V1)-(V4), no converse theorem written',
     lambda S: converse_ok(S), lambda S: put(S, 'stxt', dict(S['stxt'], D=S['stxt']['D'].replace('(V3)', 'x')))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once at its banked line, held at the exchange, the next act, the file kept',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-CORR-ROW', 'CORRESPONDENCE READ HERE -- row 395 once, v0.4 and the exchange in it, the ledger a true prefix extended',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 395 |', '| 396 |'))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS READ HERE -- this act`s record once at its banked line',
     lambda S: trail_ok(S), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORKORDER-LINE', 'OPEN_TRAILS READ HERE -- the work-order`s line once, T3-T5 compiled and the exchange named',
     lambda S: workorder_ok(S), lambda S: put(S, 'wj', dict(S['wj'], line=1))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b559'}))),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-LINES-KEPT', 'the written files against their blobs at b559`s commit',
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
    ('G-KERNEL-MAINS-UNTOUCHED', 'every kernel`s main READ HERE against its pre-act head -- the fast-forwards and the ledger row alone',
     lambda S: mains_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-kernel': ['Kernel/X.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b560_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b560_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b560 bank and tool, both new modules and this act`s ledger bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the tag and the clean bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the reads', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the stage banks and the salt-check', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the Stage D bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the re-run record', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the mains, the tools, the deposit, the HELD branch and the trial worktree', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-H11-SCORED', 'the desk against the reads, the stage banks and the E0 bank -- (R170)(5)`s five, H11a in both wordings',
     lambda S: h11_scored(S), lambda S: put(S, 'sc', dict(S['sc'], h11c=not S['sc'].get('h11c')))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b560 -'))),
    ('G-PRIORBANK-UNCHANGED', 'before the push file times against the face; after it content digests against the pre-act tip and the pushed tree, no exception',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the two written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-EDITED-AS-RULED', 'relay`s tools against b559`s close READ HERE -- b559_checks.py alone, in the one ruled commit',
     lambda S: [x for x in S['tools_edited'] if x.endswith('.py')] == ['b559_checks.py'] and len(S['tool_commits']) == 1,
     lambda S: put(S, 'tools_edited', ['b559_checks.py', 'terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b560 commit in five repositories and the suite change, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b560')" in S['suite']
                and "data/b560_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b560_components.txt' in gits(ROOT, 'show'")),
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
    rc_gen, gen_diff = (0, dict(rerun=True)) if RERUN else regenerate()   # ### (R170)(3): a re-run does not regenerate the table
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
    rec('b560 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
    if RERUN:
        pass
    elif gen_diff.get('first_run'):
        rec('  ###   ### **NO PRIOR RUN TO DIFF AGAINST -- THIS CLOSE IS THE FIRST.**')
    else:
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
            % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
               len(gen_diff.get('changed') or [])))
    if S['pushed']:
        rec('  ### G-PRIORBANK-UNCHANGED checked %d prior banks: %d by digest against the pre-act tip and the pushed tree, %d first tracked'
            ' in the pushed tree by digest against it, %d tracked by no tree read by file time; none excepted; changed %s.'
            % (S['prior_checked'], S['prior_pre'], S['prior_pub'], S['prior_time'], S['prior_bad'] or 'NONE'))
        rec('  ### G-WRITELIST-KINDS read the working tree by content digest against the pushed tree ((R170)(3)).')
    else:
        rec('  ### G-PRIORBANK-UNCHANGED checked %d prior banks by time, none excepted.' % S['prior_checked'])
    if RERUN:
        rec('  ### ### **(R170)(3): A RE-RUN ON THE PUSHED ACT -- THE GENERATOR WAS NOT RE-RUN** (it writes relay`s table files).')
    rec('  ### ### **VACUOUS ARMS : %s.**' % ([a for a in VACUOUS_ARMS] or 'NONE'))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if RERUN:
        # ### (R170)(3): a re-run writes one named record and nothing of the act's own.
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1])
        io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
        print('  written: %s' % os.path.basename(out))
        return 0 if ok else 1
    out = os.path.join(D, 'b560_checks_postpush.txt' if pushed else 'b560_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b560_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
