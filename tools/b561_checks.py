# -*- coding: utf-8 -*-
"""b561_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b560's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b561_registration_2026-09-29.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'd3f1b1d9'      # ### b560's table housekeeping -- relay's tip before this act
PRIOR_PP = '86676f5'           # ### b560's PLACE-papers commit
PRIOR_GS = 'f8b8a1e'           # ### SIDE-global-section before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH0 = '### b561 —'


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


import b561_record as R
import b542_checks as K542
import terminal_table as TT
BALPOS_REL = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md', BALPOS_REL]
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md',
         'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
AFTER_LOCK = ('b561_reads.json', 'b561_decay.json', 'b561_D1.json', 'b561_e0.json', 'b561_weight.json', 'b561_findings.json')
BEFORE_LOCK = ('b561_ferry.txt', 'b561_ferry_scan.txt', 'b561_pins_stepzero.txt')


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
              and 'ferry file                    : b561_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b561_ferry_scan.txt', 'b561_pins_stepzero.txt')))
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
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b561')
            and 'data/b561_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=40):
    """### the commits of this act in a repository: subjects opening `b561 --` or `push discipline:`, or housekeeping naming (R171)."""
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b561 --') or s.startswith('push discipline:') or (s.startswith('housekeeping:') and ('(R171)' in s or 'b561' in s)):
                out.append(h)
    return out


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    locks = sorted(glob.glob(os.path.join(D, 'b561_lockgate_notes*.txt')))
    exch_main = rd8(blob(KER, 'main:SIDEExplicitFormula/LiWeilExchange.lean'))
    pt = [x for x in gits(ROOT, 'log', '--pretty=%h', PRIOR_RELAY + '..HEAD', '--', 'tools/push_gated.sh').split(NL) if x.strip()]
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b561_ferry.txt')),
        scan=read(os.path.join(D, 'b561_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b561_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b561_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b561_pins_stepzero.txt')),
        lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b560_closing.txt')),
        addendum=read(os.path.join(D, 'b561_addendum.txt')),
        desk=read(os.path.join(D, 'b561_desk_notes.txt')), defects=read(os.path.join(D, 'b561_defects.txt')),
        sc=jload('b561_scores.json'), reads=read(os.path.join(D, 'b561_reads.txt')), rj=jload('b561_reads.json'),
        wt=jload('b561_weight.json'), decay=read(os.path.join(D, 'b561_decay_read.txt')), dj=jload('b561_decay.json'),
        d1=jload('b561_D1.json'), d2=jload('b561_D2.json'), d1t=read(os.path.join(D, 'b561_D1.txt')), d2t=read(os.path.join(D, 'b561_D2.txt')),
        d34=read(os.path.join(D, 'b561_D3_D4.txt')),
        e0=jload('b561_e0.json'), e0txt=read(os.path.join(D, 'b561_e0.txt')), rowgen=read(os.path.join(D, 'b561_rowgen.txt')),
        v05txt=read(os.path.join(D, 'b561_v05_push.txt')),
        cons=read(os.path.join(D, 'b561_consumer.txt')), cj=jload('b561_consumer.json'),
        fj=jload('b561_findings.json'), rows=jload('b561_rows.json'), tj=jload('b561_trail.json'), wj=jload('b561_workorder.json'),
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        branches=read(os.path.join(D, 'b561_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), balpos=read(os.path.join(PP, BALPOS_REL)),
        mains=R.mains(), k=R.kstate(), exch_main=exch_main,
        exch_names=re.findall(r"^(?:theorem|def)\s+([A-Za-z_']+)", exch_main, re.M),
        main_tree=[x for x in gits(KER, 'ls-tree', '-r', '--name-only', 'main').split(NL) if x.strip()],
        trial=dict(head=gits(R.Q.P.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.Q.P.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b560*') for r in (ROOT, PP, SIDE)},
        recomputed={k2: v for k2, v in R.scores().items() if not k2.startswith('_')},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b561_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if (f.startswith('b561_') or f == 'push_gated.sh') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b561_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b561_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        tool_commits=pt,
        pt_files=sorted(x for x in gits(ROOT, 'show', '--name-only', '--pretty=format:', pt[-1]).split(NL) if x.strip()) if pt else [],
        pt_msg=git(ROOT, 'log', '-1', '--pretty=%B', pt[-1]) if pt else '',
        pt_parent=gits(ROOT, 'rev-parse', '--short=8', pt[-1] + '^') if pt else '',
        pushsh=read(os.path.join(T, 'push_gated.sh')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b561 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b561_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    S['pushed'] = RERUN or is_pushed()
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    else:
        S['after_lock'] = all(os.path.exists(os.path.join(D, x)) and os.path.getmtime(os.path.join(D, x)) > os.path.getmtime(FACE) for x in AFTER_LOCK)
        S['before_lock'] = all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in BEFORE_LOCK)
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b561_') and os.path.isfile(os.path.join(D, f))] + \
        [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b561_')] + [os.path.join(T, 'push_gated.sh')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    blobs['LiWeilExchange.lean@main'] = exch_main
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-5][0-9]_|^b560_|^b334_', f)]
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
TRAILH = '### b561 —'


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def h12_word(S, tag):
    return seg(S['desk'], '**(H12%s)** ### **' % tag[-1], 16).split('.')[0]


def code(t):
    return re.sub(r'--.*$', '', re.sub(r'/-.*?-/', '', t or '', flags=re.S), flags=re.M)


def reads_ok(S):
    r = S['reads']
    need = ['LiWeil.lean:', 'ZeroSummability.lean:247', 'PowerLimit.lean:934', 'PowerLimit.lean:1025', 'PowerLimit.lean:949',
            'ExplicitFormula.lean:97', 'EXPONENT 2', 'EXPONENT 4', 'b560_stageD.txt:150', 'b560_stageD.txt:166', 'b549_premise.txt:12',
            'BALANCE_AND_POSITIVITY.md:764', 'FINDINGS.md:5478', 'FINDINGS.md:5486', 'FINDINGS.md:5575', 'FINDINGS.md:5601',
            '.githooks/pre-push', 'b560_defects.txt (e)', 'no standing push script']
    rows = S['rj'].get('rows', [])
    ok = all(x in r for x in need) and len(S['rj'].get('names', [])) == 35 and bool(rows)
    for x in rows:
        ok = ok and R.decl_at(R.at(R.V04, x['file']), x['name']) == x['line']
    return ok


def weight_ok(S):
    ln = S['wt'].get('lines', {})
    F, B = S['find'].split(NL), S['balpos'].split(NL)
    try:
        return (F[ln['twoforms'] - 1].startswith(P(R.W_TWOFORMS)) and 'rh_imp_li_nonneg' in F[ln['twoforms'] - 1]
                and F[ln['tier'] - 1].startswith(P(R.W_TIER)) and '**T0**' in F[ln['tier'] - 1]
                and F[ln['field'] - 1].startswith(P(R.W_FIELD)) and 'T1-lit' in F[ln['field'] - 1]
                and B[ln['balpos'] - 1].startswith(P(R.W_BALPOS)) and 'not compiled' in B[ln['balpos'] - 1]
                and S['find'].count(P(R.W_TWOFORMS)) == 1 and S['balpos'].count(P(R.W_BALPOS)) == 1)
    except (KeyError, IndexError, TypeError):
        return False


def push_tool_ok(S):
    return (len(S['tool_commits']) == 1 and S['pt_files'] == ['tools/push_gated.sh'] and S['pt_parent'] == PRIOR_RELAY
            and 'set -euo pipefail' in S['pushsh'] and 'NO TAG IS PUSHED' in S['pushsh']
            and S['pushsh'].index('ls-remote origin refs/heads/main') < S['pushsh'].index('refs/tags/$tag'))


def push_test_ok(S):
    m = S['pt_msg']
    return ('CASE 1 ok' in m and 'MAIN PUSH REFUSED' in m and 'remote tag peeled []' in m and 'CASE 2: DEFECT REPRODUCED' in m
            and 'CASE 3 ok' in m and 'TEST VERDICT : THE TAG PUSH DOES NOT RUN ON A REFUSED MAIN PUSH' in m)


def decay_ok(S):
    d = S['decay']
    return (all(('(%d)' % i) in d for i in range(1, 10)) and 'REFUTED BY THE' in d and 'n/‖ρ‖' in d and 'NEITHER' in d
            and 'AN ILLUSTRATION, NOT EVIDENCE' in d and S['dj'].get('h12a') == 'REFUTED' and len(S['dj'].get('sup_values', [])) == 3)


def before_build(S):
    return ('ON THE PAGE, BEFORE ANY BUILD' in S['decay'] and 'THE SEAT FORMED ITS READING OF H12a BEFORE THIS SEAL' in flat(S['face'])
            and 'D3' not in ' '.join(S['exch_names']) and 'dominant' not in ' '.join(S['exch_names']).lower())


def from_v04(S):
    k = S['k']
    return k['br_parent'] == R.V04 and k['remote'].get('refs/heads/' + R.BR) == k['br']


def nosorry_main(S):
    rows = S['e0'].get('rows', {})
    return (not re.search(r'\bsorry\b', code(S['exch_main'])) and bool(rows)
            and not any('sorryAx' in (r.get('axioms') or ['sorryAx']) for r in rows.values()))


def items_ok(S):
    return (S['d1'].get('all_std3') is True and S['d2'].get('all_std3') is True and len(S['d1'].get('names', [])) == 7
            and len(S['d2'].get('names', [])) == 2 and 'PRINTED 7 OF 7' in S['d1t'] and 'PRINTED 2 OF 2' in S['d2t'])


def elab_ok(S):
    ok = True
    for t in (S['d1t'], S['d2t']):
        heads = re.findall(r'### st(D\d)_(\d+) -- exit (\d+), elapsed \d+ s, errors (\d+)', t)
        ok = ok and bool(heads) and heads[-1][2] == '0' and heads[-1][3] == '0' and len(heads) <= 4
    return ok


def axioms_ok(S):
    rows = S['e0'].get('rows', {})
    return (sorted(rows) == sorted(S['exch_names']) and len(rows) == 9
            and all(r.get('axioms') is not None and set(r['axioms']) <= set(R.STD3) for r in rows.values()))


def e0_ok(S):
    e = S['e0']
    return (e.get('gate') is True and all(r['grade'] == 'DERIVES' for r in e.get('rows', {}).values()) and not e.get('defs')
            and '### UNGRADED' not in S['e0txt'] and 'THE ROWGEN RECORD' in S['e0txt'])


def rowgen_ok(S):
    return "('SIDEExplicitFormula.LiWeil.integral_pow_mul_cexp', ['ok'])" in S['rowgen'] and S['e0'].get('rowgen_control') is True


def tag05_ok(S):
    k = S['k']
    return (k['v05'] == k['main'] == k['br'] == k['remote'].get('refs/tags/v0.5^{}') == k['remote'].get('refs/heads/main')
            and k['v05type'] == 'tag' and k['v05obj'] == k['remote'].get('refs/tags/v0.5')
            and 'main read back at the remote' in S['v05txt'] and S['v05txt'].index('main read back') < S['v05txt'].index('tag v0.5 peeled'))


def held_earliest(S):
    return ('(D3) HELD -- THE EARLIEST OBSTACLE' in S['d34'] and '(D4) NOT REACHED' in S['d34'] and 'RE-PRICED' in S['d34']
            and not any(n for n in S['exch_names'] if 'Exchange' in n or 'exchange' in n.lower() and 'transform' not in n.lower()))


def consumer_ok(S):
    n = S['cj'].get('line')
    ot = S['ot'].split(NL)
    return (bool(n) and ot[n - 1].startswith(P(R.CONSUMER_H)) and "consumes the IDENTITY’S direction" in ot[n - 1]
            and 'inequalityToPositivity' in S['cons'] and 'rh_imp_li_nonneg' in S['cons'] and 'li_identity_of_exchange' in S['cons'])


def ot_once_at(S, head, line):
    ot = rd8(S['pp_now']['OPEN_TRAILS.md']).split(NL)
    ln = [i + 1 for i, l in enumerate(ot) if l.startswith(P(head))]
    return ln == [line] and bool(line)


def findings_ok(S):
    F = S['find'].split(NL)
    b = fblock(S['find'], P(R.FH))
    n = S['fj'].get('heading_line', 0)
    return (S['find'].count(P(R.FH)) == 1 and bool(n) and F[n - 1] == P(R.FH) and 'held at (D3)' in b and 'blTransform_holds' in b
            and '**Next**' in b and 'W-ORD-GRH-WEIL' in b and kept(S, 'FINDINGS.md'))


def corr_ok(S):
    rows = [l for l in S['corr'].split(NL) if l.startswith('| %s |' % R.ROWNO)]
    return (len(rows) == 1 and 'v0.5' in rows[0] and 'blTransform' in rows[0] and S['rows'].get('exit') == 0
            and S['corr'].startswith(S['corr_prior'].rstrip(NL)))


def trail_ok(S):
    return ot_once_at(S, R.HEADING, S['tj'].get('line')) and '**Entered:**' in trail(S) and '**(R171) ratified' in trail(S)


def workorder_ok(S):
    n = S['wj'].get('line')
    ot = S['ot'].split(NL)
    return ot_once_at(S, R.WO_LINE, n) and '(D3) HELD AT THE READ' in ot[n - 1] and 'W-ORD-GRH-WEIL' in ot[n - 1]


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b560 (was ') == 3
            and b.count('Deleted branch push-b560-closing (was ') == 1 and 'Deleted branch li-weil-b560 (was 941503b)' in b
            and 'an ancestor of main: yes' in b and S['k']['old_local'] == '' and 'refs/heads/' + R.OLD not in S['k']['remote'])


def held_kept(S):
    k = S['k']
    return k['held'] == R.Q.HELD_TIP == k['remote'].get('refs/heads/' + R.Q.HELD) and 'toolchain-trial-b551' in S['branches']


def mains_ok(S):
    m = S['mains']
    return (len(m) == len(R.PRE_HEADS) and all(v == [] for k2, v in m.items() if k2 not in ('SIDE-global-section', 'SIDE-explicit-formula'))
            and set(m.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'}
            and m.get('SIDE-explicit-formula') == R.NEW_FILES and S['k']['ff'] and S['k']['status'] == ['A'])


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


def h12_scored(S):
    return all(x in S['sc'] and h12_word(S, x) == word_of(S['sc'][x]) and S['sc'][x] == S['recomputed'][x] for x in ('h12a', 'h12b', 'h12c'))


VACUOUS_ARMS = ()


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R171) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b561' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b560`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b560' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b561' in S['ferry'] and 'ACT b561' in S['face'] and not glob.glob(os.path.join(D, 'b562_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b561')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; before the push file times, after it content digests against the pushed tree',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE SEAT FORMED ITS READING OF H12a BEFORE THIS SEAL' in flat(S['face'])
                and S['after_lock'] and S['before_lock']),
     lambda S: put(S, 'after_lock', False)),
    ('G-R171-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R171) END' in S['ferry'] and S['ot'].count('**(R171) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R171) ratified', '(R171) noted'))),
    ('G-READS-CITED', 'the reads bank against the sources READ HERE -- every LiWeil declaration at its line, the pattern lemmas, the documents, the hooks',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('EXPONENT 2', 'x'))),
    ('G-WEIGHT-LINES', 'FINDINGS and BALPOS READ HERE -- the four weight lines once each at their banked lines',
     lambda S: weight_ok(S), lambda S: put(S, 'balpos', S['balpos'].replace(P(R.W_BALPOS), 'x'))),
    ('G-PUSH-TOOL-ALONE', 'relay`s commits since b560`s close READ HERE -- push_gated.sh alone in one commit, pipefail, main read back before any tag',
     lambda S: push_tool_ok(S), lambda S: put(S, 'pt_files', ['tools/push_gated.sh', 'tools/b561_record.py'])),
    ('G-PUSH-TEST-REFUSED', 'the push tool`s commit message -- the refused case, no tag at the remote, the control reproducing b560`s leak',
     lambda S: push_test_ok(S), lambda S: put(S, 'pt_msg', S['pt_msg'].replace('CASE 1 ok', 'CASE 1 x'))),
    ('G-DECAY-READ-BANKED', 'the decay-read bank -- the nine steps, H12a REFUTED, the order n/‖ρ‖, (D3) neither, the illustration labelled',
     lambda S: decay_ok(S), lambda S: put(S, 'dj', dict(S['dj'], h12a='HOLDS'))),
    ('G-H12A-BEFORE-BUILD', 'the decay bank, the face and the module on main -- the read on the page, no (D3) declaration written',
     lambda S: before_build(S), lambda S: put(S, 'exch_names', S['exch_names'] + ['D3_uniform_dominant'])),
    ('G-LIWEIL561-FROM-V04', 'the kernel`s refs READ HERE -- li-weil-b561`s parent v0.4, pushed by name, equal at the remote',
     lambda S: from_v04(S), lambda S: put(S, 'k', dict(S['k'], br_parent=R.Q.MAIN0))),
    ('G-EXISTING-UNCHANGED', 'main against v0.4 by name-status READ HERE -- A only',
     lambda S: S['k']['status'] == ['A'], lambda S: put(S, 'k', dict(S['k'], status=['A', 'M']))),
    ('G-NO-SORRY-ON-MAIN', 'the new module on main READ HERE and Lean`s prints -- no sorry, no sorryAx',
     lambda S: nosorry_main(S), lambda S: put(S, 'exch_main', S['exch_main'] + NL + 'theorem x : False := sorry')),
    ('G-ITEM-BANKS', 'the item banks -- (D1) 7 and (D2) 2 declarations, each printed at the standard three',
     lambda S: items_ok(S), lambda S: put(S, 'd2', dict(S['d2'], all_std3=False))),
    ('G-ELAB-PRINTED', 'the item banks -- each item`s last attempt exit 0, errors 0, at most four',
     lambda S: elab_ok(S), lambda S: put(S, 'd2t', S['d2t'].replace('### stD2_4 -- exit 0', '### stD2_4 -- exit 1'))),
    ('G-AXIOMS-PRINTED', 'Lean`s own prints in the E0 bank against the module on main READ HERE -- every declaration printed',
     lambda S: axioms_ok(S), lambda S: put(S, 'exch_names', S['exch_names'] + ['unprinted_decl'])),
    ('G-E0-READ', 'the E0 bank -- every declaration DERIVES, no definition, the gate',
     lambda S: e0_ok(S), lambda S: put(S, 'e0', dict(S['e0'], gate=False))),
    ('G-ROWGEN-RECORD', 'the rowgen bank -- rowgen`s diff ok on row 396, its control True',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace("['ok']", "['MISSING']"))),
    ('G-TAG-V05-OR-HELD', 'the kernel`s tags READ HERE and at the remote, and the push bank -- v0.5 annotated, peeled to main, pushed after main read back',
     lambda S: tag05_ok(S), lambda S: put(S, 'k', dict(S['k'], v05type='commit'))),
    ('G-HELD-AT-EARLIEST', 'the D3/D4 bank and the module -- HELD at (D3), (D4) not reached, re-priced, no exchange declaration',
     lambda S: held_earliest(S), lambda S: put(S, 'd34', S['d34'].replace('(D4) NOT REACHED', 'x'))),
    ('G-CONSUMER-READ', 'OPEN_TRAILS READ HERE and the consumer bank -- the paragraph once, the identity`s direction, the three statements',
     lambda S: consumer_ok(S), lambda S: put(S, 'cons', S['cons'].replace('inequalityToPositivity', 'x'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once at its banked line, held at (D3), the next act, the file kept',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-CORR-ROW', 'CORRESPONDENCE READ HERE -- row 396 once, v0.5 and blTransform in it, the ledger a true prefix extended',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 396 |', '| 397 |'))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS READ HERE -- this act`s record once at its banked line',
     lambda S: trail_ok(S), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORKORDER-LINE', 'OPEN_TRAILS READ HERE -- the work-order`s line once, (D3) held at the read, the next act named',
     lambda S: workorder_ok(S), lambda S: put(S, 'wj', dict(S['wj'], line=1))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, the kernel`s refs, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b560'}))),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-HELD-BRANCH-KEPT', 'the kernel`s refs READ HERE -- detection-region-b559 at 8faf7de, local and remote; the trial branch named kept',
     lambda S: held_kept(S), lambda S: put(S, 'k', dict(S['k'], held='0' * 40))),
    ('G-LINES-KEPT', 'the written files against their blobs at b560`s commit',
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
    ('G-KERNEL-MAINS-UNTOUCHED', 'every kernel`s main READ HERE against its pre-act head -- the fast-forward and the ledger row alone',
     lambda S: mains_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-kernel': ['Kernel/X.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools and the push tool -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b561_x.py'])),
    ('G-DELETE-FREE', 'this act`s own Python tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b561_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b561 bank and tool, the push tool, the new module and this act`s ledger bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the decay read', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the item banks', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the unreached identity', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=True))),
    ('G-N4-SCORED', 'the desk against the consumer bank', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the push test', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the mains, the tools, the deposit, the HELD branch and the trial worktree', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-H12-SCORED', 'the desk against the decay read -- (R171)(3)`s three, each word from the banks',
     lambda S: h12_scored(S), lambda S: put(S, 'sc', dict(S['sc'], h12a=True))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b561 -'))),
    ('G-PRIORBANK-UNCHANGED', 'before the push file times against the face; after it content digests against the pre-act tip and the pushed tree, no exception',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the three written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-EDITED-AS-RULED', 'relay`s tools against b560`s close READ HERE -- none modified; push_gated.sh the one new standing tool',
     lambda S: [x for x in S['tools_edited'] if x.endswith(('.py', '.sh'))] == [] and len(S['tool_commits']) == 1,
     lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-WRITELIST-KINDS', 'every b561 commit in five repositories and the push tool`s commit, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b561')" in S['suite']
                and "data/b561_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b561_components.txt' in gits(ROOT, 'show'")),
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
    rec('b561 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b561_checks_postpush.txt' if pushed else 'b561_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b561_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
