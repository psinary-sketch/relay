# -*- coding: utf-8 -*-
"""b564_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b564's AND RE-POINTED ARM BY ARM.

### ### b564: THE (W) READER TAKES A `<...>` PLACEHOLDER IN A BACKTICKED PATH AS `*` (the face named the frontier's files
### as `Chi/<name>.lean`; b564 defect (h)). The act's own arms, sources() and helpers were written for this face;
### the harness, the carried helpers and the digest readings are b564's, re-pointed.

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
FACE = os.path.join(D, 'b564_registration_2026-09-29.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'f0e92155'      # ### b564's table housekeeping -- relay's tip before this act
PRIOR_PP = '0a0f958'           # ### b564's PLACE-papers commit
PRIOR_GS = '6fbd70e'           # ### SIDE-global-section before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH0 = '### b564 —'


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


import b564_record as R
import b542_checks as K542
import terminal_table as TT
BALPOS_REL = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md']
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md',
         'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
AFTER_LOCK = ('b564_ceiling.json', 'b564_prior_art.json', 'b564_converse_price.json', 'b564_dag.json', 'b564_a.json', 'b564_e0.json', 'b564_findings.json')
BEFORE_LOCK = ('b564_ferry.txt', 'b564_ferry_scan.txt', 'b564_pins_stepzero.txt')


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
              and 'ferry file                    : b564_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b564_ferry_scan.txt', 'b564_pins_stepzero.txt')))
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
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b564')
            and 'data/b564_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=40):
    """### the commits of this act in a repository: subjects opening `b564 --`, or housekeeping naming (R173) or b564."""
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b564 --') or (s.startswith('housekeeping:') and ('(R174)' in s or 'b564' in s)):
                out.append(h)
    return out




def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS -- b558's reader, carried (a possessive no longer
    ### desyncs the pairing; a bare-wildcard directory glob reads as the files that directory holds)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    out = []
    for line in w.split(NL):
        line = re.sub(r'(?<=[A-Za-z0-9])' + BT + r's\b', "'s", line)
        for g in re.findall(BT + '([^' + BT + NL + ']+)' + BT, line):
            g = g.strip()
            g = re.sub(r'<[^>]*>', '*', g)   # ### b564 defect (h): a placeholder reads as a wildcard
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






def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    locks = sorted(glob.glob(os.path.join(D, 'b564_lockgate_notes*.txt')))
    chi_main = {f: rd8(blob(KER, 'main:' + f)) for f in R.NEW_FILES}
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b564_ferry.txt')),
        scan=read(os.path.join(D, 'b564_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b564_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b564_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b564_pins_stepzero.txt')),
        lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b563_closing.txt')),
        desk=read(os.path.join(D, 'b564_desk_notes.txt')), defects=read(os.path.join(D, 'b564_defects.txt')),
        sc=jload('b564_scores.json'), reads=read(os.path.join(D, 'b564_reads.txt')),
        ceil=jload('b564_ceiling.json'), before=read(os.path.join(D, 'b564_trailsup_before.txt')),
        after=read(os.path.join(D, 'b564_trailsup_after.txt')), aj=jload('b564_trailsup_after.json'), supj=jload('b564_supline.json'),
        pa=read(os.path.join(D, 'b564_prior_art.txt')), paj=jload('b564_prior_art.json'), grep=read(os.path.join(D, 'b564_priorart_grep.txt')),
        ctl=read(os.path.join(D, 'b564_priorart_control.txt')), web=jload('b564_web_search.json'), gh=jload('b564_web_gh.json'),
        faj=jload('b564_fieldappend.json'), conv=read(os.path.join(D, 'b564_converse_price.txt')), cvj=jload('b564_converse_price.json'),
        psum=jload('b564_powersum_grep.json'), dag=read(os.path.join(D, 'b564_dag.txt')), dgj=jload('b564_dag.json'),
        parts={x: jload('b564_%s.json' % x) for x in ('a', 'b', 'c1')}, ptxt={x: read(os.path.join(D, 'b564_%s.txt' % x)) for x in ('a', 'b', 'c1')},
        e0=jload('b564_e0.json'), e0txt=read(os.path.join(D, 'b564_e0.txt')), rowgen=read(os.path.join(D, 'b564_rowgen.txt')),
        v08txt=read(os.path.join(D, 'b564_v08_push.txt')), decls=jload('b564_decls.json'), prints=read(os.path.join(D, 'b564_prints.txt')),
        fj=jload('b564_findings.json'), rows=jload('b564_rows.json'), tj=jload('b564_trail.json'), wj=jload('b564_workorder.json'),
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        branches=read(os.path.join(D, 'b564_branches.txt')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        mains=R.kstate()['mains'], k=R.kstate(), chi_main=chi_main,
        zeta_changed=gits(KER, 'diff', '--name-only', R.V07, 'main', '--', 'Zeta23'),
        tt_src=read(os.path.join(T, 'terminal_table.py')),
        trial=dict(head=gits(R.Q.P.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.Q.P.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b563*') for r in (ROOT, PP, SIDE)},
        recomputed={k2: v for k2, v in jload('b564_scores.json').items() if k2 != 'kstate'},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b564_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b564_') and needle in read(os.path.join(T, f))] +
            [u for s0 in jload('b564_web_search.json') or [] for u in s0.get('urls', []) if 'zenodo' in u],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b564_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b564_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b564 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b564_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    S['pushed'] = RERUN or is_pushed()
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    else:
        S['after_lock'] = all(os.path.exists(os.path.join(D, x)) and os.path.getmtime(os.path.join(D, x)) > os.path.getmtime(FACE) for x in AFTER_LOCK)
        S['before_lock'] = all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in BEFORE_LOCK)
    S['priv_names'] = K542.techne_private_names()
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b564_') and os.path.isfile(os.path.join(D, f))
               and not f.startswith('b564_fetched_')] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b564_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f, t in chi_main.items():
        blobs[f + '@main'] = t
    for f in FIXED + ['README.md', 'REGISTRY.md']:
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-5][0-9]_|^b56[0123]_|^b334_', f)]
    S['prior_checked'] = len(prior)
    if S['pushed']:
        S['noprior'], S['prior_pre'], S['prior_pub'], S['prior_time'], S['prior_bad'] = prior_by_digest(prior, PRIOR_RELAY)
    else:
        S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


# ================================================================================ this act's arm helpers
P = R.poss
TRAILH = '### b564 —'


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def hword(S, tag):
    tag = 'H' + tag[1:].lower() if tag[:1] in 'hH' else tag
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0]


def code(t):
    return re.sub(r'--.*$', '', re.sub(r'/-.*?-/', '', t or '', flags=re.S), flags=re.M)


def reads_ok(S):
    r = S['reads']
    need = ['LiWeil.lean @', 'LiWeilSym.lean @', 'GRHWeil.lean @', 'LFunction_inv_conj', 'analyticOrderAt_LFunction_inv_conj',
            'Zeta23/Defs.lean:', 'ZeroConfig', 'zetaZeroConfig', 'Main.lean:286', 'zeta_reflect_zero', 'zeta_mult_reflect',
            'b562_zeta23_modules.txt sha256', 'DirichletContinuation.lean', 'completedLFunction_one_sub', 'Nonvanishing.lean',
            'FINDINGS.md (b536', 'OPEN_TRAILS.md (b562`s trail line) :11577', 'CORRESPONDENCE row 397', 'README.md (the ceiling',
            'REGISTRY.md (the ceiling']
    return all(x in r for x in need) and 'NOT FOUND' not in r


def row_line(S, n):
    rs = [l for l in S['corr'].split(NL) if l.startswith('| %s |' % n)]
    return rs[0] if len(rs) == 1 else ''


def table_grade(S):
    """### the regenerated table`s grade cell for li_identity_of_exchange (carried from b563`s suite, which main() prints)."""
    tl = [l for l in (S.get('table') or '').split(NL) if '`SIDEExplicitFormula.LiWeil.li_identity_of_exchange` |' in l]
    grade = ' '.join(tl[0].split('|')[7:8]).split() if len(tl) == 1 else []
    blk = seg(S.get('table') or '', '**`SIDE-explicit-formula` / `SIDEExplicitFormula.LiWeil.li_identity_of_exchange`**', 900)
    return tl, ' '.join(grade), blk


def term_cells(S):
    j = S.get('tjson') or {}
    rows = j.get('rows', j) if isinstance(j, dict) else j
    return [c for r in (rows or []) if r.get('name', '').endswith('li_identity_of_exchange') for c in r.get('grade_cells', [])]


def ceiling_ok(S):
    ok = True
    for f, n0 in (('README.md', 115), ('REGISTRY.md', 950)):
        old, new = rd8(S['pp_prior'][f]).split(NL), rd8(S['pp_now'][f]).split(NL)
        n = S['ceil'].get('files', {}).get(f, {}).get('new_line')
        ok = ok and bool(n) and new[:n0] == old[:n0] and '(R146)' in new[n0 - 1] and new[n - 1].startswith('*(Appended under the author')
        ok = ok and new[:n - 2] + new[n:] == old[:n - 2] + old[n - 2:] if n and n < len(new) else ok and new[:len(old)] == old
    return ok


def ceiling_words(S):
    fer = ' '.join(S['ferry'].split())
    m = re.search(r'the sentence, the author.s: "([^"]+)"', fer)
    s = m.group(1) if m else None
    return bool(s) and all(s in rd8(S['pp_now'][f]) for f in ('README.md', 'REGISTRY.md')) and S['ceil'].get('sentence') == s


def supline_ok(S):
    n = S['supj'].get('line')
    ot = S['ot'].split(NL)
    return (bool(n) and ot[n - 1].startswith('SUPERSEDES OPEN_TRAILS :11577 for li_identity_of_exchange: T2-INTERFACES-on-false-premise')
            and S['ot'].count('SUPERSEDES OPEN_TRAILS :11577 for li_identity_of_exchange') == 1 and not TT.NAME_RE.search(ot[n - 1]))


def cells_read(S):
    cells = term_cells(S)
    return (len(cells) == 1 and cells[0]['ledger'] == 'SIDE-global-section/CORRESPONDENCE.md' and cells[0]['line'] == 470
            and not any(c['ledger'] == 'PLACE-papers/OPEN_TRAILS.md' and c['line'] == 11577 for c in cells))


def priorart_ok(S):
    g0 = S['grep']
    return (all(q in g0 for q in ('Keiper', 'Bombieri', 'Lagarias', 'liCoeff', "Li's criterion", 'WIDENED'))
            and 'CONTROL: SIDEExplicitFormula/' in S['ctl'] and len(S['gh']) >= 30 and all('query' in s0 for s0 in S['web'])
            and len(S['web']) >= 5 and all(s0.get('rc') == 0 for s0 in S['gh']) and 'THE COMPARISON, ONE PARAGRAPH' in S['pa'])


def field_ok(S):
    n = S['faj'].get('line')
    F = S['find'].split(NL)
    t = F[n - 1] if n else ''
    return (bool(n) and t.startswith('*Appended 2026-09-29 by b564 to the field entry (:5575)') and R.BULKA in t and R.ARDA in t
            and '2026-09-05' in t and '2026-09-21' in t)


def no_priority(S):
    blocks = [S['find'].split(NL)[S['faj'].get('line', 1) - 1], S['pa']]
    bad = re.compile(r'\b(?:we|the programme|this (?:act|kernel)) (?:is|was|are) the first\b|\bfirst formali[sz]ation\b|\bpriority\b(?! claim)(?!\.)', re.I)
    txt = ' '.join(blocks)
    return 'No sentence here claims priority' in txt and not [m.group(0) for m in bad.finditer(txt.replace('claims priority', ''))]


def converse_ok(S):
    c = S['conv']
    return all(x in c for x in ('(V1) Zeta23/Defs.lean:143', '(V2) SIDEExplicitFormula/LiWeil.lean:91', '(V3) Zeta23/Defs.lean:146',
                                '(V4) THE POWER-SUM LEMMA', '(V2) STATUS', '(V3) STATUS', '(V4) STATUS')) and 'NOT FOUND' not in c


def powersum_ok(S):
    j = S['psum']
    return all(q in j for q in ('Turán', 'powerSum', 'power sum', 'sum of powers', 'Dirichlet approximation', 'Kronecker')) and \
        j['Turán']['files'] > 0 and 'H16d : HELD' in S['conv']


def pointer_ok(S):
    a = S['cvj'].get('appends', {})
    ot = S['ot'].split(NL)
    w, p = a.get('workorder', {}).get('line'), a.get('pointer', {}).get('line')
    return (bool(w and p) and 'THE CONVERSE RE-PRICED' in ot[w - 1] and 'liCriterion' in ot[p - 1] and 'consumer read (:11542)' in ot[p - 1]
            and S['ot'].count('THE RESIDUE CHAIN’S LAST STEP POINTED AT THE PRICE') == 1)


def dag_ok(S):
    return 'EDGES DISAGREEING: NONE' in S['dag'] and 'bank 57, files 57' in S['dag']


def frontier_ok(S):
    j = S['dgj']
    return [f['module'] for f in j.get('frontier', [])] == j.get('order') and len(j.get('order', [])) >= 1 and \
        all(f['kind'] != 'UNREAD' for f in j['frontier']) and '### THE FRONTIER' in S['dag']


def consumes_ok(S):
    return all(f['ids'] for f in S['dgj'].get('frontier', [])) and 'what it consumes from Mathlib about ζ' in S['dag'] and \
        'Mathlib/NumberTheory/LSeries/RiemannZeta.lean:' in S['dag']


def branch_from_v07(S):
    k = S['k']
    first = gits(KER, 'rev-list', '--reverse', R.V07 + '..' + R.BR).split(NL)[0]
    return (gits(KER, 'rev-parse', first + '^').startswith(R.V07) and k['remote'].get('refs/heads/' + R.BR) == k['br'])


def nosorry_main(S):
    rows = S['e0'].get('rows', {})
    return (not any(re.search(r'\bsorry\b', code(t)) for t in S['chi_main'].values()) and bool(rows)
            and not any('sorryAx' in (r.get('axioms') or ['sorryAx']) for r in rows.values()))


def parts_ok(S):
    return all(S['parts'][x].get('all_std3') is True and S['parts'][x].get('rows') for x in ('a', 'b', 'c1'))


def elab_ok(S):
    ok = True
    for x in ('a', 'b', 'c1'):
        at_ = S['parts'][x].get('attempts', [])
        ok = ok and bool(at_) and len(at_) <= 4 and ' exit 0 ' in at_[-1]['head'] and at_[-1]['errors'] == []
    return ok


def facts_ok(S):
    t = S['ptxt']['a']
    return 'EVERY FACT THE INSTANCE CONSUMES' in t and 'NOT LOCATED' not in t and t.count('Mathlib  ') >= 10 and 'kernel   ' in t


def generic_unedited(S):
    return S['zeta_changed'] == '' and 'UNCHANGED' in S['ptxt']['b']


def reclass_ok(S):
    b = S['parts']['b']
    t = S['ptxt']['b']
    return bool(b.get('reclassified')) and all(m in t for m in b['reclassified']) and 'THE COUNT CORRECTED' in t and 'UNREAD' not in t


def held_fact(S):
    t = S['ptxt']['c1']
    return ('HELD, NOT ATTEMPTED' in t and 'LSeries_eq_mul_integral' in t and 'LFunction_eq_LSeries' in t
            and S['parts']['c1'].get('held_at', '').startswith('HasDerivAtZeta0'))


def axioms_ok(S):
    rows = S['e0'].get('rows', {})
    names = sorted(d['name'] for d in S['decls'])
    return sorted(rows) == names and len(rows) == 122 and all(r.get('axioms') is not None and set(r['axioms']) <= set(R.STD3) for r in rows.values())


def salt_ok(S):
    ax = S['chi_main'].get('AxiomCheckChi.lean', '')
    return (S['e0'].get('salt') is True and '#print SIDEExplicitFormula.GRHWeil.chiZeroConfig' in ax
            and 'THE SALT-CHECK: True' in S['e0txt'])


def e0_ok(S):
    e = S['e0']
    rows = e.get('rows', {})
    return (e.get('gate') is True and all(r['grade'] in ('DERIVES', 'DEF', 'INTERFACES') for r in rows.values())
            and all(rows[n]['grade'] == 'DERIVES' for n in rows if not n.startswith(R.NSG + 'Generic.') and rows[n]['grade'] != 'DEF')
            and all(rows[n]['why'] for n in rows if rows[n]['grade'] == 'INTERFACES'))


def rowgen_ok(S):
    return "('SIDEExplicitFormula.GRHWeil.chi_reflect_zero', ['ok'])" in S['rowgen'] and S['e0'].get('rowgen_control') is True


def tag08_ok(S):
    k = S['k']
    return (k['v08'] == k['main'] == k['br'] == k['remote'].get('refs/tags/v0.8^{}') == k['remote'].get('refs/heads/main')
            and k['v08type'] == 'tag' and k['v08obj'] == k['remote'].get('refs/tags/v0.8'))


def pushes_gated(S):
    v = S['v08txt']
    h = S['k']['v08']
    return ('push_gated: main read back at the remote: %s' % h in v and 'push_gated: tag v0.8 peeled local %s' % h in v
            and v.index('main read back at the remote') < v.index('tag v0.8 peeled') and 'push_gated: DONE' in v)


def ot_once_at(S, head, line):
    ot = rd8(S['pp_now']['OPEN_TRAILS.md']).split(NL)
    ln = [i + 1 for i, l in enumerate(ot) if l.startswith(P(head))]
    return ln == [line] and bool(line)


def findings_ok(S):
    F = S['find'].split(NL)
    b = fblock(S['find'], P(R.FH))
    n, nw = S['fj'].get('entry', {}).get('heading_line', 0), S['fj'].get('weight', {}).get('heading_line', 0)
    return (S['find'].count(P(R.FH)) == 1 and bool(n) and F[n - 1] == P(R.FH) and bool(nw) and F[nw - 1] == P(R.FH_W)
            and 'chiZeroConfig' in b and '**Next**' in b and 'GRH-WEIL act three' in b and kept(S, 'FINDINGS.md'))


def corr_ok(S):
    a = row_line(S, R.ROW_ACT)
    return (bool(a) and 'v0.8' in a and 'chiZeroConfig' in a and S['rows'].get('exit_act') == 0
            and S['corr'].startswith(S['corr_prior'].rstrip(NL)))


def trail_ok(S):
    return ot_once_at(S, R.HEADING, S['tj'].get('line')) and '**Entered:**' in trail(S) and '**(R174) ratified' in trail(S)


def workorder_ok(S):
    n = S['wj'].get('line')
    ot = S['ot'].split(NL)
    return ot_once_at(S, R.WO_H, n) and 'THE χ-INSTANCE COMPILED' in ot[n - 1] and 'HasDerivAtZeta0' in ot[n - 1]


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b563 (was ') == 3
            and b.count('Deleted branch push-b563-closing (was ') == 1)


def held_kept(S):
    k = S['k']
    return (all(k['kept'][b].startswith(t) and k['remote'].get('refs/heads/' + b, '').startswith(t) for b, t in R.KEPT_TIPS.items())
            and k['remote'].get('refs/heads/' + R.BR) == k['br'])


def mains_ok(S):
    m = S['mains']
    return (len(m) == len(R.PRE_HEADS) and all(v == [] for k2, v in m.items() if k2 not in ('SIDE-global-section', 'SIDE-explicit-formula'))
            and set(m.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'}
            and m.get('SIDE-explicit-formula') == R.NEW_FILES and S['k']['ff'])


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


VACUOUS_ARMS = ()
N_LIST = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7')


def _nscore_arm(k, reads):
    return ('G-%s-SCORED' % k.upper(), reads, lambda S: nscored(S, k), lambda S: put(S, 'sc', dict(S['sc'], **{k: not S['sc'].get(k)})))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R174) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b564' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b563`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b563' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b564' in S['ferry'] and 'ACT b564' in S['face'] and not glob.glob(os.path.join(D, 'b565_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b564')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; before the push file times, after it content digests against the pushed tree',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE SEAT FORMED ITS READINGS BEFORE THIS SEAL' in flat(S['face'])
                and S['after_lock'] and S['before_lock']),
     lambda S: put(S, 'after_lock', False)),
    ('G-R174-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R174) END' in S['ferry'] and S['ot'].count('**(R174) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R174) ratified', '(R174) noted'))),
    ('G-READS-CITED', 'the reads bank -- the kernel headers, the configuration, the reflection, the Mathlib facts, the ledger lines',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('completedLFunction_one_sub', 'x'))),
    ('G-CEILING-APPENDED', 'README.md and REGISTRY.md READ HERE against b563`s PLACE-papers tip, pre-push -- one paragraph after the (R146)(2) line, nothing above it moved',
     lambda S: ceiling_ok(S), lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'].replace(b'(R146)', b'(R999)', 1)}))),
    ('G-CEILING-WORDS-VERBATIM', 'the author`s sentence in the banked ferry against both appended paragraphs',
     lambda S: ceiling_words(S), lambda S: put(S, 'ceil', dict(S['ceil'], sentence='the converse is compiled.'))),
    ('G-TRAILSUP-LINE', 'OPEN_TRAILS READ HERE -- the ruled line once, at its banked line, no backticked name on it',
     lambda S: supline_ok(S), lambda S: put(S, 'supj', dict(S['supj'], line=1))),
    ('G-CONFLICT-PRINTED', 'the before and after banks -- CONFLICT printed both ways, the terminals changed printed',
     lambda S: ('CONFLICT committed 13 -> regenerated 13' in S['before'] and 'CONFLICT committed 13 -> regenerated 12' in S['after']
                and 'TERMINALS WHOSE GRADE CHANGED' in S['after']),
     lambda S: put(S, 'after', S['after'].replace('regenerated 12', 'regenerated 13'))),
    ('G-TABLE-CELLS-READ', 'the table this suite regenerates, READ HERE -- li_identity_of_exchange`s one cell, CORRESPONDENCE :470',
     lambda S: cells_read(S), lambda S: put(S, 'tjson', dict(rows=[dict(name='SIDEExplicitFormula.LiWeil.li_identity_of_exchange',
                                                                  grade_cells=[dict(grade='SHELL', ledger='PLACE-papers/OPEN_TRAILS.md', line=11577)])]))),
    ('G-TOOLS-UNEDITED', 'relay`s tools against b563`s close READ HERE -- no existing tool modified',
     lambda S: [x for x in S['tools_edited'] if x.endswith(('.py', '.sh'))] == [],
     lambda S: put(S, 'tools_edited', ['terminal_table.py'])),
    ('G-PRIORART-QUERIES-PRINTED', 'the prior-art banks -- every query with its count, the control, the gh and web searches',
     lambda S: priorart_ok(S), lambda S: put(S, 'ctl', '')),
    ('G-PRIORART-FIELD-APPEND', 'FINDINGS READ HERE -- the field-entry append at its banked line, URLs and dates',
     lambda S: field_ok(S), lambda S: put(S, 'faj', dict(S['faj'], line=1))),
    ('G-NO-PRIORITY-SENTENCE', 'the append and the bank -- the no-priority sentence present, no priority claimed',
     lambda S: no_priority(S), lambda S: put(S, 'pa', S['pa'] + ' this kernel is the first to prove it.')),
    ('G-CONVERSE-FOUR-ITEMS', 'the converse bank -- (V1)-(V4), each with its fact by name and line or ABSENT',
     lambda S: converse_ok(S), lambda S: put(S, 'conv', S['conv'].replace('(V3) STATUS', 'x'))),
    ('G-POWERSUM-SEARCH', 'the power-sum grep bank -- six queries, the matcher firing, H16d`s line',
     lambda S: powersum_ok(S), lambda S: put(S, 'psum', {k2: v for k2, v in S['psum'].items() if k2 != 'Kronecker'})),
    ('G-CONVERSE-POINTER', 'OPEN_TRAILS READ HERE -- the work-order price and the residue chain`s pointer at their banked lines',
     lambda S: pointer_ok(S), lambda S: put(S, 'cvj', dict(S['cvj'], appends={}))),
    ('G-DAG-TWO-READS', 'the DAG bank -- the bank and the files compared edge by edge, no disagreement',
     lambda S: dag_ok(S), lambda S: put(S, 'dag', S['dag'].replace('EDGES DISAGREEING: NONE', 'EDGES DISAGREEING: [x]'))),
    ('G-FRONTIER-LISTED', 'the DAG json -- the frontier in the face`s order, each kind read',
     lambda S: frontier_ok(S), lambda S: put(S, 'dgj', dict(S['dgj'], frontier=[dict(f, kind='UNREAD') for f in S['dgj'].get('frontier', [])]))),
    ('G-FRONTIER-CONSUMES', 'the DAG bank -- each frontier module`s ζ identifiers with their Mathlib lines',
     lambda S: consumes_ok(S), lambda S: put(S, 'dgj', dict(S['dgj'], frontier=[dict(f, ids=[]) for f in S['dgj'].get('frontier', [])]))),
    ('G-BRANCH-FROM-V07', 'the kernel`s refs READ HERE -- grh-weil-b564`s first commit on v0.7, pushed by name',
     lambda S: branch_from_v07(S), lambda S: put(S, 'k', dict(S['k'], remote=dict(S['k']['remote'], **{'refs/heads/' + R.BR: 'x'})))),
    ('G-NEW-FILES-ONLY', 'main against v0.7 by name-status READ HERE -- four files added, under Chi/ and the axiom check',
     lambda S: S['k']['ns'] == ['A ' + f for f in R.NEW_FILES], lambda S: put(S, 'k', dict(S['k'], ns=S['k']['ns'] + ['A Zeta23/X.lean']))),
    ('G-EXISTING-UNCHANGED', 'main against v0.7 by name-status READ HERE -- no file modified or deleted',
     lambda S: all(x.startswith('A ') for x in S['k']['ns']), lambda S: put(S, 'k', dict(S['k'], ns=S['k']['ns'] + ['M SIDEExplicitFormula/GRHWeil.lean']))),
    ('G-NO-SORRY-ON-MAIN', 'the new files on main READ HERE and Lean`s prints -- no sorry, no sorryAx',
     lambda S: nosorry_main(S), lambda S: put(S, 'chi_main', dict(S['chi_main'], x='theorem x : False := sorry'))),
    ('G-PART-BANKS', 'the three part banks -- every declaration printed at the standard three',
     lambda S: parts_ok(S), lambda S: put(S, 'parts', dict(S['parts'], b=dict(S['parts']['b'], all_std3=False)))),
    ('G-ELAB-PRINTED', 'the part banks -- each part`s last attempt exit 0, no error, at most four',
     lambda S: elab_ok(S), lambda S: put(S, 'parts', dict(S['parts'], c1=dict(S['parts']['c1'], attempts=S['parts']['c1'].get('attempts', []) + [dict(label='c_5', head='c_5 exit 1', errors=['x'])])))),
    ('G-FACTS-CONSUMED-PRINTED', 'part (a)`s bank -- every consumed fact located by file and line',
     lambda S: facts_ok(S), lambda S: put(S, 'ptxt', dict(S['ptxt'], a=S['ptxt']['a'] + ' NOT LOCATED'))),
    ('G-GENERIC-UNEDITED', 'every Zeta23 blob at the tip against v0.7 READ HERE',
     lambda S: generic_unedited(S), lambda S: put(S, 'zeta_changed', 'Zeta23/Defs.lean')),
    ('G-RECLASS-PRINTED', 'part (b)`s bank -- each re-classified module with its lines, the count corrected',
     lambda S: reclass_ok(S), lambda S: put(S, 'ptxt', dict(S['ptxt'], b=S['ptxt']['b'].replace('THE COUNT CORRECTED', 'x')))),
    ('G-HELD-FACT-NAMED', 'part (c1)`s bank -- the held declaration, the fact it needs, the failed search',
     lambda S: held_fact(S), lambda S: put(S, 'ptxt', dict(S['ptxt'], c1=S['ptxt']['c1'].replace('LSeries_eq_mul_integral', 'x')))),
    ('G-AXIOMS-PRINTED', 'Lean`s prints in the E0 bank against the declaration list READ from the tip -- 122 printed',
     lambda S: axioms_ok(S), lambda S: put(S, 'decls', S['decls'] + [dict(name='unprinted_decl')])),
    ('G-SALT-CHECK', 'the E0 bank and the axiom-check file on main -- every definition printed',
     lambda S: salt_ok(S), lambda S: put(S, 'e0', dict(S['e0'], salt=False))),
    ('G-E0-READ', 'the E0 bank -- the gate, every grade in the vocabulary, INTERFACES only in Generic and each on its named premise',
     lambda S: e0_ok(S), lambda S: put(S, 'e0', dict(S['e0'], gate=False))),
    ('G-ROWGEN-RECORD', 'the rowgen bank -- rowgen`s diff ok on row 400, its control True',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace("['ok']", "['MISSING']"))),
    ('G-TAG-V08-OR-HELD', 'the kernel`s tags READ HERE and at the remote -- v0.8 annotated, peeled to main and the branch',
     lambda S: tag08_ok(S), lambda S: put(S, 'k', dict(S['k'], v08type='commit'))),
    ('G-PUSHES-GATED', 'the push bank -- through push_gated.sh, main read back before the tag',
     lambda S: pushes_gated(S), lambda S: put(S, 'v08txt', S['v08txt'].replace('push_gated: tag v0.8 peeled local', 'x'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the weight entry and the act`s entry once each at their banked lines, the next act, the file kept',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH), 'x'))),
    ('G-CORR-ROW', 'CORRESPONDENCE READ HERE -- row 400 once, the ledger a true prefix extended',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 400 |', '| 401 |'))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS READ HERE -- this act`s record once at its banked line',
     lambda S: trail_ok(S), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORKORDER-LINE', 'OPEN_TRAILS READ HERE -- the W-ORD-GRH-WEIL line once, the instance compiled, the held point',
     lambda S: workorder_ok(S), lambda S: put(S, 'wj', dict(S['wj'], line=1))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in three repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b563'}))),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-HELD-BRANCH-KEPT', 'the kernel`s refs READ HERE -- the four kept branches at their tips local and remote, grh-weil-b564 at the remote',
     lambda S: held_kept(S), lambda S: put(S, 'k', dict(S['k'], kept=dict(S['k']['kept'], **{'grh-weil-b562': '0' * 40})))),
    ('G-LINES-KEPT', 'FINDINGS and OPEN_TRAILS against their blobs at b563`s commit -- true prefixes',
     lambda S: all(kept(S, f) for f in FIXED),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-KERNEL-MAINS-UNTOUCHED', 'every kernel`s main READ HERE against its pre-act head -- the fast-forward adding files and the ledger row alone',
     lambda S: mains_ok(S), lambda S: put(S, 'mains', dict(S['mains'], **{'SIDE-kernel': ['Kernel/X.lean']}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools and the web bank -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b564_x.py'])),
    ('G-DELETE-FREE', 'this act`s own Python tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b564_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b564 bank and tool (the fetched third-party files excepted), the new files and this act`s ledger bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    _nscore_arm('n1', 'the desk against the supersession banks'),
    _nscore_arm('n2', 'the desk against the prior-art bank'),
    _nscore_arm('n3', 'the desk against the converse bank'),
    _nscore_arm('n4', 'the desk against the DAG bank'),
    _nscore_arm('n5', 'the desk against the part banks'),
    _nscore_arm('n6', 'the desk against the kernel refs and part (c1)'),
    _nscore_arm('n7', 'the desk against the mains, the tools, the deposit and the kept branches'),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-H16-SCORED', 'the desk against the banks -- H16a-H16d, each word from the banks',
     lambda S: all(hword(S, x.upper()) == word_of(S['sc'][x]) and S['sc'][x] == S['recomputed'][x] for x in ('h16a', 'h16b', 'h16c', 'h16d')),
     lambda S: put(S, 'sc', dict(S['sc'], h16c=False))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b564 -'))),
    ('G-PRIORBANK-UNCHANGED', 'before the push file times against the face; after it content digests against the pre-act tip and the pushed tree, no exception',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED + ['README.md', 'REGISTRY.md']), lambda S: put(S, 'tracked', list(S['tracked']) + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING) + ' a second record')),
    ('G-WRITELIST-KINDS', 'every b564 commit in five repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b564')" in S['suite']
                and "data/b564_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b564_components.txt' in gits(ROOT, 'show'")),
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
    rec('b564 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b564_checks_postpush.txt' if pushed else 'b564_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b564_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
