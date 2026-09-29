# -*- coding: utf-8 -*-
"""b563_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b562's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b563_registration_2026-09-29.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '4ab01dcd'      # ### b562's table housekeeping -- relay's tip before this act
PRIOR_PP = '4b6ffe9'           # ### b562's PLACE-papers commit
PRIOR_GS = '9eaec7e'           # ### SIDE-global-section before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH0 = '### b563 —'


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


import b563_record as R
import b542_checks as K542
import terminal_table as TT
BALPOS_REL = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md']
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md',
         'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
AFTER_LOCK = ('b563_reads.json', 'b563_per_n.json', 'b563_decay.json', 'b563_D1.json', 'b563_e0.json', 'b563_findings.json')
BEFORE_LOCK = ('b563_ferry.txt', 'b563_ferry_scan.txt', 'b563_pins_stepzero.txt')


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
    # ### b562 defect (g): both stamps are to the second; the gate and the seal fell in one second (18:06:26Z), so a tie is
    # ### admitted -- the stamps cannot order it either way, and the file times banked in the defect put the gate 0.157 s first.
    before = (lk is not None and rn is not None and rn <= lk and all(pushed_digest_ok(x) for x in BEFORE_LOCK)
              and 'ferry file                    : b563_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b563_ferry_scan.txt', 'b563_pins_stepzero.txt')))
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
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b563')
            and 'data/b563_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=40):
    """### the commits of this act in a repository: subjects opening `b563 --`, or housekeeping naming (R173) or b563."""
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b563 --') or (s.startswith('housekeeping:') and ('(R173)' in s or 'b563' in s)):
                out.append(h)
    return out


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    locks = sorted(glob.glob(os.path.join(D, 'b563_lockgate_notes*.txt')))
    sym_main = rd8(blob(KER, 'main:SIDEExplicitFormula/LiWeilSym.lean'))
    ax_main = rd8(blob(KER, 'main:AxiomCheckLiWeilSym.lean'))
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b563_ferry.txt')),
        scan=read(os.path.join(D, 'b563_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b563_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b563_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b563_pins_stepzero.txt')),
        lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b562_closing.txt')),
        addendum=read(os.path.join(D, 'b563_addendum.txt')),
        desk=read(os.path.join(D, 'b563_desk_notes.txt')), defects=read(os.path.join(D, 'b563_defects.txt')),
        sc=jload('b563_scores.json'), reads=read(os.path.join(D, 'b563_reads.txt')),
        unit=read(os.path.join(D, 'b563_findsup_unit.txt')), noop=read(os.path.join(D, 'b563_findsup_noop.txt')),
        after=read(os.path.join(D, 'b563_findsup_after.txt')), aj=jload('b563_findsup_after.json'),
        supj=jload('b563_supline.json'), daj=jload('b563_defect_a_line.json'), blj=jload('b563_b562_lines.json'),
        pn=read(os.path.join(D, 'b563_per_n.txt')), pnj=jload('b563_per_n.json'), drift_src=read(os.path.join(D, 'b562_drift.txt')),
        drift_sha=hashlib.sha256(open(os.path.join(D, 'b562_drift.txt'), 'rb').read()).hexdigest(),
        decay=read(os.path.join(D, 'b563_decay_read.txt')), dcj=jload('b563_decay.json'),
        decay_mtime=os.path.getmtime(os.path.join(D, 'b563_decay_read.txt')) if os.path.exists(os.path.join(D, 'b563_decay_read.txt')) else 9e18,
        decay_num=read(os.path.join(D, 'b563_decay_num.txt')),
        parts={x: jload('b563_%s.json' % x) for x in ('D1', 'D2', 'stmt', 'D3', 'D4')},
        e0=jload('b563_e0.json'), e0txt=read(os.path.join(D, 'b563_e0.txt')), rowgen=read(os.path.join(D, 'b563_rowgen.txt')),
        v07txt=read(os.path.join(D, 'b563_v07_push.txt')),
        fj=jload('b563_findings.json'), rows=jload('b563_rows.json'), tj=jload('b563_trail.json'), wj=jload('b563_workorder.json'),
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        branches=read(os.path.join(D, 'b563_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        mains=R.mains(), k=R.kstate(), sym_main=sym_main, ax_main=ax_main,
        sym_names=re.findall(r"^(?:theorem|def)\s+([A-Za-z_'0-9]+)", re.sub(r'/-.*?-/', '', sym_main, flags=re.S), re.M),
        tool_commit=(sorted(x for x in gits(ROOT, 'show', '--name-only', '--pretty=format:', TOOL_COMMIT).split(NL) if x.strip()),
                     gits(ROOT, 'log', '-1', '--format=%B', TOOL_COMMIT)),
        tt_src=read(os.path.join(T, 'terminal_table.py')),
        br_ct=int(gits(KER, 'log', '-1', '--format=%ct', R.BR) or 0),
        trial=dict(head=gits(R.Q.P.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.Q.P.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b562*') for r in (ROOT, PP, SIDE)},
        recomputed={k2: v for k2, v in R.scores().items() if not k2.startswith('_')},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b563_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b563_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b563_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b563_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b563 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b563_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    S['pushed'] = RERUN or is_pushed()
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    else:
        S['after_lock'] = all(os.path.exists(os.path.join(D, x)) and os.path.getmtime(os.path.join(D, x)) > os.path.getmtime(FACE) for x in AFTER_LOCK)
        S['before_lock'] = all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in BEFORE_LOCK)
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b563_') and os.path.isfile(os.path.join(D, f))] + \
        [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b563_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    blobs['LiWeilSym.lean@main'] = sym_main
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-5][0-9]_|^b56[012]_|^b334_', f)]
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
TRAILH = '### b563 —'


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def hword(S, tag):
    tag = 'H' + tag[1:].lower() if tag[:1] in 'hH' else tag   # ### the desk writes (H13a), not (H13A)
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0]


def code(t):
    return re.sub(r'--.*$', '', re.sub(r'/-.*?-/', '', t or '', flags=re.S), flags=re.M)


def reads_ok(S):
    r = S['reads']
    need = ['LiWeil.lean:', 'LiLimitExchange', 'li_identity_of_exchange', 'LiWeilExchange.lean:', 'blTransform_holds',
            'PowerLimit.lean:', 'rest_tendsto_zero', 'dominant_summable', 'ZeroSummability.lean:', 'zero_sum_inv_sq', 'EF_lit',
            'b560_reads.txt:', 'b562_drift.txt: sha256', 'b561_decay_read.txt:', 'BALPOS:291', 'BALPOS:303', 'terminal_table.py:',
            'FINDINGS :6048', 'refs/heads/main', 'GRHWeil.lean:1-40']
    return all(x in r for x in need) and 'NOT FOUND' not in r


def row_line(S, n):
    rs = [l for l in S['corr'].split(NL) if l.startswith('| %s |' % n)]
    return rs[0] if len(rs) == 1 else ''


def table_grade(S):
    """### the regenerated table`s grade cell for li_identity_of_exchange, and the cells its conflict block cites."""
    tl = [l for l in (S.get('table') or '').split(NL) if '`SIDEExplicitFormula.LiWeil.li_identity_of_exchange` |' in l]
    grade = ' '.join(tl[0].split('|')[7:8]).split() if len(tl) == 1 else []
    blk = seg(S.get('table') or '', '**`SIDE-explicit-formula` / `SIDEExplicitFormula.LiWeil.li_identity_of_exchange`**', 900)
    return tl, ' '.join(grade), blk


def term_cells(S):
    j = S.get('tjson') or {}
    rows = j.get('rows', j) if isinstance(j, dict) else j
    return [c for r in (rows or []) if r.get('name', '').endswith('li_identity_of_exchange') for c in r.get('grade_cells', [])]


def tool_form(S):
    t = S['tt_src']
    return ("FIND_SUP_RE = re.compile(r'SUPERSEDES FINDINGS :(\\d+) for" in t and 'def supersede_findings(cells, name):' in t
            and 'uniq = supersede_findings(supersede_trail(supersede(uniq), n), n)' in t
            and 'THE FINDINGS-LINE SUPERSESSIONS READ (b563, (R173)(3))' in t)


def commit_alone(S):
    files, msg = S['tool_commit']
    return files == ['tools/terminal_table.py'] and 'THE TEST' in msg and 'CONFLICT 13 -> 13' in msg and '(R173)(3)' in msg


def supline_ok(S):
    n = S['supj'].get('line')
    F = S['find'].split(NL)
    lines = [i + 1 for i, l in enumerate(F) if l.startswith(P(R.SUP_LINE[:60]))]
    return (bool(n) and lines == [n] and F[n - 1].startswith('SUPERSEDES FINDINGS :6048 for `li_identity_of_exchange`: '
                                                            'T2-INTERFACES-on-false-premise'))


def act_lines(S):
    """### the FINDINGS and OPEN_TRAILS lines this act appended (beyond the prior blobs), as (ledger label, line number)."""
    out = set()
    for f, lab in (('FINDINGS.md', 'PLACE-papers/FINDINGS.md'), ('OPEN_TRAILS.md', 'PLACE-papers/OPEN_TRAILS.md')):
        n0 = len(rd8(S['pp_prior'][f]).split(NL))
        n1 = len(rd8(S['pp_now'][f]).split(NL))
        out |= set((lab, i) for i in range(n0, n1 + 1))
    return out


def no_new_cell(S):
    cells = term_cells(S)
    mine = act_lines(S)
    return bool(cells) and not any((c['ledger'], c['line']) in mine for c in cells)


def cells_read(S):
    cells = term_cells(S)
    return (bool(cells) and not any(c['ledger'] == 'PLACE-papers/FINDINGS.md' and c['line'] == 6048 for c in cells)
            and '### after --' in S['after'] and 'OPEN_TRAILS.md:11577' in seg(S['after'], '### after --', 900))


def defect_a_ok(S):
    n = S['daj'].get('line')
    ot = S['ot'].split(NL)
    return bool(n) and ot[n - 1].startswith(P(R.DEF_A_H)) and 'n²' in ot[n - 1] and S['ot'].count(P(R.DEF_A_H)) == 1


def b562_lines_ok(S):
    ot = S['ot'].split(NL)
    a, b, c = S['daj'].get('line'), S['blj'].get('h13b', {}).get('line'), S['blj'].get('h13a', {}).get('line')
    return (bool(a and b and c) and a < b < c and ot[b - 1].startswith(P(R.H13B_H)) and ot[c - 1].startswith(P(R.H13A_H))
            and '(H4, H8, H13b)' in ot[b - 1] and 'bench question' in ot[c - 1] and S['ot'].count(P(R.H13B_H)) == 1)


def per_n_ok(S):
    j = S['pnj']
    return (j.get('source_sha') == S['drift_sha'] and len(j.get('rows', [])) == 12 and 'H15d (the δ → 0 extrapolation' in S['pn']
            and 'FROM b562`S BANK ALONE' in S['pn'] and S['drift_sha'] in S['pn'])


def per_n_recomputed(S):
    import b563_per_n as PN
    try:
        t1, t2 = PN.parse(S['drift_src'])
        rows = S['pnj'].get('rows', [])
        ok = len(rows) == 12
        for r in rows:
            a, b = PN.lsq(list(PN.DELTAS), t2[r['n']]['D'])
            ok = ok and abs(a - r['a']) <= 1e-15 * max(1.0, abs(a)) and abs(b - r['b']) <= 1e-12 * max(1.0, abs(b))
        return ok
    except Exception:
        return False


def decay_ok(S):
    d = S['decay']
    return (S['dcj'].get('h15a') is True and '(2) THE ODD-ABOUT-THE-JUMP CANCELLATION, SHOWN' in d and '(5) THE LEFT EDGE' in d
            and '(3) THE ORDER IN δ AT FIXED n' in d and '(4) THE DECAY IN ‖ρ‖' in d and 'H15a HELD' in d)


def decay_before_build(S):
    return 0 < S['decay_mtime'] < S['br_ct']


def decay_num_ok(S):
    t = S['decay_num']
    return 'AN ILLUSTRATION, NOT EVIDENCE FOR A THEOREM' in t and 'HYPOTHETICAL POINT' in t


def branch_from_v06(S):
    k = S['k']
    return (gits(KER, 'rev-parse', R.BR + '^').startswith(R.V06) and k['remote'].get('refs/heads/' + R.BR) == k['br'])


def nosorry_main(S):
    rows = S['e0'].get('rows', {})
    return (not re.search(r'\bsorry\b', code(S['sym_main'])) and bool(rows)
            and not any('sorryAx' in (r.get('axioms') or ['sorryAx']) for r in rows.values()))


PART_N = {'D1': 11, 'D2': 3, 'stmt': 6, 'D3': 41, 'D4': 4}


def parts_ok(S):
    return all(S['parts'][x].get('all_std3') is True and len(S['parts'][x].get('names', [])) == PART_N[x] for x in PART_N)


def elab_ok(S):
    ok = True
    for x in PART_N:
        by = {}
        for a in S['parts'][x].get('attempts', []):
            by.setdefault(a['unit'], []).append((a['head'], a.get('own_errors', -1)))
        ok = ok and bool(by)
        for u, hs in by.items():
            # ### b563 defect (e): the last attempt's errors IN THIS PART'S OWN DECLARATIONS, as the part bank attributes them
            # ### (a run two parts share can exit 1 on the other part); the first version read the run's exit code.
            ok = ok and hs[-1][1] == 0 and len(hs) <= 4
    return ok


def axioms_ok(S):
    rows = S['e0'].get('rows', {})
    return (sorted(rows) == sorted(S['sym_names']) and len(rows) == 65
            and all(r.get('axioms') is not None and set(r['axioms']) <= set(R.STD3) for r in rows.values()))


def salt_ok(S):
    return (S['e0'].get('salt') is True and '#print SIDEExplicitFormula.LiWeil.LiLimitExchangeSym' in S['ax_main']
            and '#print SIDEExplicitFormula.LiWeil.SymPairBound' in S['ax_main'] and 'THE SALT-CHECK: True' in S['e0txt'])


def held_line(S):
    """### VACUOUS on a landing: the arm asks that a HELD item print its line and re-price; nothing was held (every part
    ### compiled and li_identity_sym is on main), so it reads that no part bank reports a failing last attempt."""
    return elab_ok(S) and 'li_identity_sym' in S['sym_names']


def e0_ok(S):
    e = S['e0']
    rows = e.get('rows', {})
    return (e.get('gate') is True and all(r['grade'] in ('DERIVES', 'DEF', 'INTERFACES') for r in rows.values())
            and [n for n, r in rows.items() if r['grade'] == 'INTERFACES'] == ['exchange_of_bound']
            and rows.get('li_identity_sym', {}).get('grade') == 'DERIVES')


def rowgen_ok(S):
    return "('SIDEExplicitFormula.LiWeil.symPair_bound', ['ok'])" in S['rowgen'] and S['e0'].get('rowgen_control') is True


def tag07_ok(S):
    k = S['k']
    return (k['v07'] == k['main'] == k['br'] == k['remote'].get('refs/tags/v0.7^{}') == k['remote'].get('refs/heads/main')
            and k['v07type'] == 'tag' and k['v07obj'] == k['remote'].get('refs/tags/v0.7'))


def pushes_gated(S):
    v = S['v07txt']
    h = S['k']['v07']
    return ('push_gated: main read back at the remote: %s' % h in v and 'push_gated: tag v0.7 peeled local %s' % h in v
            and v.index('main read back at the remote') < v.index('tag v0.7 peeled') and 'push_gated: DONE' in v)


def ot_once_at(S, head, line):
    ot = rd8(S['pp_now']['OPEN_TRAILS.md']).split(NL)
    ln = [i + 1 for i, l in enumerate(ot) if l.startswith(P(head))]
    return ln == [line] and bool(line)


def findings_ok(S):
    F = S['find'].split(NL)
    b = fblock(S['find'], P(R.FH))
    n = S['fj'].get('heading_line', 0)
    return (S['find'].count(P(R.FH)) == 1 and bool(n) and F[n - 1] == P(R.FH) and 'li_identity_sym' in b
            and '**Next**' in b and 'GRH-WEIL act two' in b and kept(S, 'FINDINGS.md'))


def corr_ok(S):
    a = row_line(S, R.ROW_ACT)
    return (bool(a) and 'v0.7' in a and 'li_identity_sym' in a and S['rows'].get('exit_act') == 0
            and S['corr'].startswith(S['corr_prior'].rstrip(NL)))


def trail_ok(S):
    return ot_once_at(S, R.HEADING, S['tj'].get('line')) and '**Entered:**' in trail(S) and '**(R173) ratified' in trail(S)


def workorder_ok(S):
    n = S['wj'].get('line')
    ot = S['ot'].split(NL)
    return ot_once_at(S, R.WO_H, n) and '(X2) LANDED AT v0.7' in ot[n - 1] and '`li_identity_sym` DERIVES' in ot[n - 1]


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b562 (was ') == 3
            and b.count('Deleted branch push-b562-closing (was ') == 1 and 'toolchain-trial-b551' in b)


def held_kept(S):
    k = S['k']
    return (all(k['kept'][b] == R.KEPT_TIPS[b] == k['remote'].get('refs/heads/' + b) for b in R.KEPT)
            and k['remote'].get('refs/heads/' + R.BR) == k['br'])


def mains_ok(S):
    m = S['mains']
    return (len(m) == len(R.PRE_HEADS) and all(v == [] for k2, v in m.items() if k2 not in ('SIDE-global-section', 'SIDE-explicit-formula'))
            and set(m.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'}
            and m.get('SIDE-explicit-formula') == R.NEW_FILES and S['k']['ff'])


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


VACUOUS_ARMS = ('G-HELD-LINE-PRINTED (nothing was held: every part compiled, so the arm reads only that no part bank ends on a '
                'failing attempt)',)
TOOL_COMMIT = '348a115d'


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R173) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b563' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b562`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b562' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b563' in S['ferry'] and 'ACT b563' in S['face'] and not glob.glob(os.path.join(D, 'b564_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b563')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; before the push file times, after it content digests against the pushed tree',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE SEAT FORMED ITS READINGS BEFORE THIS SEAL' in flat(S['face'])
                and S['after_lock'] and S['before_lock']),
     lambda S: put(S, 'after_lock', False)),
    ('G-R173-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R173) END' in S['ferry'] and S['ot'].count('**(R173) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R173) ratified', '(R173) noted'))),
    ('G-READS-CITED', 'the reads bank -- the kernel, the lemmas by line, the banks, BALPOS, the parser, FINDINGS :6048, the refs',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('ZeroSummability.lean:', 'x'))),
    ('G-FINDSUP-TOOL-FORM', 'tools/terminal_table.py READ HERE -- the regex, the function, the call, the header line',
     lambda S: tool_form(S), lambda S: put(S, 'tt_src', S['tt_src'].replace('def supersede_findings(cells, name):', 'x'))),
    ('G-INSTRUMENT-COMMIT-ALONE', 'relay commit 348a115d READ HERE -- that file alone, its test quoted',
     lambda S: commit_alone(S), lambda S: put(S, 'tool_commit', (S['tool_commit'][0] + ['data/x.txt'], S['tool_commit'][1]))),
    ('G-FINDSUP-UNIT', 'the unit bank -- the fixtures both polarities, every one agreeing',
     lambda S: 'FIXTURES 6 ; AGREEING 6 : PASS' in S['unit'] and 'quiet:' in S['unit'] and 'fires:' in S['unit'],
     lambda S: put(S, 'unit', S['unit'].replace('AGREEING 6', 'AGREEING 5'))),
    ('G-FINDSUP-NOOP', 'the no-op bank (reconstructed, defect (d)) -- CONFLICT 13 -> 13, no grade moved, the header NONE',
     lambda S: ('CONFLICT before 13 -> after 13' in S['noop'] and 'TERMINALS WHOSE GRADE CHANGED : NONE' in S['noop']
                and 'SUPERSESSIONS READ (b563, (R173)(3)) : NONE' in S['noop'] and 'RECONSTRUCTED' in S['noop']),
     lambda S: put(S, 'noop', S['noop'].replace('CHANGED : NONE', 'CHANGED : [x]'))),
    ('G-FINDSUP-LINE', 'FINDINGS READ HERE -- the directive once, at its banked line, in the ruled form',
     lambda S: supline_ok(S), lambda S: put(S, 'supj', dict(S['supj'], line=1))),
    ('G-CONFLICT-PRINTED', 'the after bank -- CONFLICT before and after printed, the terminals changed printed',
     lambda S: 'CONFLICT before 13 -> after 13' in S['after'] and 'TERMINALS WHOSE GRADE CHANGED : NONE' in S['after']
     and len(S['aj'].get('conflict_before', [])) == 13,
     lambda S: put(S, 'after', S['after'].replace('CONFLICT before 13 -> after 13', 'x'))),
    ('G-TABLE-CELLS-READ', 'the table this suite regenerates, READ HERE -- li_identity_of_exchange`s cells carry no FINDINGS :6048',
     lambda S: cells_read(S), lambda S: put(S, 'tjson', dict(rows=[dict(name='SIDEExplicitFormula.LiWeil.li_identity_of_exchange',
                                                                  grade_cells=[dict(grade='INTERFACES', ledger='PLACE-papers/FINDINGS.md', line=6048)])]))),
    ('G-RECORD-ADDS-NO-CELL', 'the regenerated table against every line this act appended -- none a cell of li_identity_of_exchange',
     lambda S: no_new_cell(S), lambda S: put(S, 'tjson', dict(rows=[dict(name='SIDEExplicitFormula.LiWeil.li_identity_of_exchange',
                                                                  grade_cells=[dict(grade='SHELL', ledger='PLACE-papers/OPEN_TRAILS.md', line=S['tj'].get('line', 0) + 8)])]))),
    ('G-DEFECT-A-LINE', 'OPEN_TRAILS READ HERE -- b562`s defect (a) line once, at its banked line, the n² tail',
     lambda S: defect_a_ok(S), lambda S: put(S, 'daj', dict(S['daj'], line=1))),
    ('G-PER-N-BANKED', 'the per-n bank -- from b562`s bank alone (its sha256 printed and matching), 12 rows, H15d`s line',
     lambda S: per_n_ok(S), lambda S: put(S, 'drift_sha', '0' * 64)),
    ('G-PER-N-RECOMPUTED', 'the suite recomputes each intercept from data/b562_drift.txt with the bank tool`s parser',
     lambda S: per_n_recomputed(S), lambda S: put(S, 'pnj', dict(S['pnj'], rows=[dict(r, a=r['a'] + 1e-6) for r in S['pnj'].get('rows', [])]))),
    ('G-B562-RECORD-LINES', 'OPEN_TRAILS READ HERE -- H13b`s mis-specification and H13a`s reading after the defect (a) line',
     lambda S: b562_lines_ok(S), lambda S: put(S, 'blj', dict(S['blj'], h13a=dict(line=1)))),
    ('G-DECAY-READ-BANKED', 'the decay bank -- the cancellation shown, the order in δ, the decay, the left edge, H15a scored',
     lambda S: decay_ok(S), lambda S: put(S, 'decay', S['decay'].replace('(5) THE LEFT EDGE', 'x'))),
    ('G-DECAY-BEFORE-BUILD', 'the decay bank`s file time against the kernel branch`s commit READ HERE',
     lambda S: decay_before_build(S), lambda S: put(S, 'decay_mtime', S['br_ct'] + 10)),
    ('G-DECAY-NUM-LABELLED', 'the illustration bank -- labelled an illustration, the hypothetical points marked',
     lambda S: decay_num_ok(S), lambda S: put(S, 'decay_num', S['decay_num'].replace('NOT EVIDENCE', 'x'))),
    ('G-BRANCH-FROM-V06', 'the kernel`s refs READ HERE -- li-weil-b563`s parent v0.6, pushed by name',
     lambda S: branch_from_v06(S), lambda S: put(S, 'k', dict(S['k'], remote=dict(S['k']['remote'], **{'refs/heads/' + R.BR: 'x'})))),
    ('G-EXISTING-UNCHANGED', 'main against v0.6 by name-status READ HERE -- two files added, none modified',
     lambda S: S['k']['ns'] == ['A AxiomCheckLiWeilSym.lean', 'A SIDEExplicitFormula/LiWeilSym.lean'],
     lambda S: put(S, 'k', dict(S['k'], ns=S['k']['ns'] + ['M SIDEExplicitFormula/LiWeil.lean']))),
    ('G-NO-SORRY-ON-MAIN', 'the new module on main READ HERE and Lean`s prints -- no sorry, no sorryAx',
     lambda S: nosorry_main(S), lambda S: put(S, 'sym_main', S['sym_main'] + NL + 'theorem x : False := sorry')),
    ('G-PART-BANKS', 'the five part banks -- 11, 3, 6, 41 and 4 declarations, each printed at the standard three',
     lambda S: parts_ok(S), lambda S: put(S, 'parts', dict(S['parts'], D3=dict(S['parts']['D3'], all_std3=False)))),
    ('G-ELAB-PRINTED', 'the part banks -- each unit`s last attempt exit 0, errors 0, at most four',
     lambda S: elab_ok(S), lambda S: put(S, 'parts', dict(S['parts'], D4=dict(S['parts']['D4'], attempts=[dict(unit='(e)', head='### symE_9 -- exit 1, elapsed 1 s, errors 3', own_errors=3)])))),
    ('G-AXIOMS-PRINTED', 'Lean`s own prints in the E0 bank against the module on main READ HERE -- every declaration printed',
     lambda S: axioms_ok(S), lambda S: put(S, 'sym_names', S['sym_names'] + ['unprinted_decl'])),
    ('G-SALT-CHECK', 'the E0 bank and the axiom-check file on main -- every definition printed, the statement unfolding to kernel objects',
     lambda S: salt_ok(S), lambda S: put(S, 'e0', dict(S['e0'], salt=False))),
    ('G-HELD-LINE-PRINTED', 'VACUOUS on a landing -- the part banks and the module on main: no part ends on a failing attempt',
     lambda S: held_line(S), lambda S: put(S, 'sym_names', [x for x in S['sym_names'] if x != 'li_identity_sym'])),
    ('G-E0-READ', 'the E0 bank -- the gate, every grade in the vocabulary, one INTERFACES (exchange_of_bound), li_identity_sym DERIVES',
     lambda S: e0_ok(S), lambda S: put(S, 'e0', dict(S['e0'], gate=False))),
    ('G-ROWGEN-RECORD', 'the rowgen bank -- rowgen`s diff ok on row 399, its control True',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace("['ok']", "['MISSING']"))),
    ('G-TAG-V07-OR-HELD', 'the kernel`s tags READ HERE and at the remote -- v0.7 annotated, peeled to main and the branch',
     lambda S: tag07_ok(S), lambda S: put(S, 'k', dict(S['k'], v07type='commit'))),
    ('G-PUSHES-GATED', 'the push bank -- through push_gated.sh, main read back before the tag',
     lambda S: pushes_gated(S), lambda S: put(S, 'v07txt', S['v07txt'].replace('push_gated: tag v0.7 peeled local', 'x'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once at its banked line, li_identity_sym, the next act, the file kept',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-CORR-ROW', 'CORRESPONDENCE READ HERE -- row 399 once, the ledger a true prefix extended',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 399 |', '| 400 |'))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS READ HERE -- this act`s record once at its banked line',
     lambda S: trail_ok(S), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORKORDER-LINE', 'OPEN_TRAILS READ HERE -- the LI-WEIL-BRIDGE line once, (X2) landed at v0.7',
     lambda S: workorder_ok(S), lambda S: put(S, 'wj', dict(S['wj'], line=1))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b562'}))),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-HELD-BRANCH-KEPT', 'the kernel`s refs READ HERE -- detection-region-b559, li-weil-b561, grh-weil-b562 at their tips, li-weil-b563 at the remote',
     lambda S: held_kept(S), lambda S: put(S, 'k', dict(S['k'], kept=dict(S['k']['kept'], **{'grh-weil-b562': '0' * 40})))),
    ('G-LINES-KEPT', 'the written files against their blobs at b562`s commit',
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
    ('G-KERNEL-MAINS-UNTOUCHED', 'every kernel`s main READ HERE against its pre-act head -- the fast-forward adding files and the ledger row alone',
     lambda S: mains_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-kernel': ['Kernel/X.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b563_x.py'])),
    ('G-DELETE-FREE', 'this act`s own Python tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b563_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b563 bank and tool, the new module and this act`s ledger bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    ('G-N1-SCORED', 'the desk against the supersession banks', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the per-n bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the decay bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the part banks', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the E0 bank', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the mains, the tools, the deposit, the kept branches and the trial',
     lambda S: nscored(S, 'n6'), lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-H15-SCORED', 'the desk against the banks -- H15a-H15d, each word from the banks',
     lambda S: all(hword(S, x.upper()) == word_of(S['sc'][x]) and S['sc'][x] == S['recomputed'][x] for x in ('h15a', 'h15b', 'h15c', 'h15d')),
     lambda S: put(S, 'sc', dict(S['sc'], h15c=False))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b563 -'))),
    ('G-PRIORBANK-UNCHANGED', 'before the push file times against the face; after it content digests against the pre-act tip and the pushed tree, no exception',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the two written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-INSTRUMENTS-EDITED-AS-RULED', 'relay`s tools against b562`s close READ HERE -- terminal_table.py alone modified, by the ruled commit',
     lambda S: [x for x in S['tools_edited'] if x.endswith(('.py', '.sh'))] == ['terminal_table.py'] and commit_alone(S),
     lambda S: put(S, 'tools_edited', ['terminal_table.py', 'push_gated.sh'])),
    ('G-WRITELIST-KINDS', 'every b563 commit in five repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b563')" in S['suite']
                and "data/b563_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b563_components.txt' in gits(ROOT, 'show'")),
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
    S['tjson'] = json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}')
    _tl, _grade, _blk = table_grade(S)
    rec('  ### the regenerated table`s line for li_identity_of_exchange: grade cell %r (lines found %d)' % (_grade, len(_tl)))
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    names = [a[0] for a in ARMS]
    pushed = S['pushed']
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b563 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b563_checks_postpush.txt' if pushed else 'b563_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b563_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
