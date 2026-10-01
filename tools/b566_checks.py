# -*- coding: utf-8 -*-
"""b566_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b565's AND RE-POINTED ARM BY ARM TO b566's (G2).

### ### b566: THE CONVERSE VENDORED -- THE LICENCE, THE TOOLCHAIN TRIAL BOTH WAYS, THE EQUALITY LEMMA, THE COMPOSED CRITERION;
### THE CEILING AMENDED, UNDER (R176). The harness, the generic helpers (imported from b564_checks, never copied) and the digest
### readings are b565's, re-pointed; the act's own arms and sources() were written for this face. The (W) reader is b564's
### `globs_of` (a `<...>` placeholder reads as `*`), as tools/SUITE_README.md records.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### `G-PEEK-DECLARED`, `G-WRITELIST-KINDS` and `G-PRIORBANK-UNCHANGED` read file times before the push and content digests
### against the pushed tree after it ((R169)(1)(b), (R170)(3)).
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

import b564_checks as K4          # ### the generic helpers, imported (b564's, carried)
import b566_record as R
import b542_checks as K542
import addenda as ADD             # ### (R177)(3): the post-seal addendum forms, shared (b567)

D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
BULKA = os.path.join('D:', os.sep, 'audit-b565', 'bulka')
ARDA = os.path.join('D:', os.sep, 'audit-b565', 'arda')
FACE = os.path.join(D, 'b566_registration_2026-09-30.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = R.PRIOR_RELAY   # ### dbddf5ce, b565's table housekeeping -- relay's tip before this act
PRIOR_PP = R.PRIOR_PP         # ### b6539b2, b565's PLACE-papers commit
PRIOR_GS = R.PRIOR_GS         # ### b9b0005, SIDE-global-section before this act
PIN = R.PIN
NL = chr(10)
L, RES, EX = [], [], []

read, git, gits, cut, put, blob, flat, rd8, jload = K4.read, K4.git, K4.gits, K4.cut, K4.put, K4.blob, K4.flat, K4.rd8, K4.jload
utc_epoch, cr0, blob_id, tree_ids, strip_prose = K4.utc_epoch, K4.cr0, K4.blob_id, K4.tree_ids, K4.strip_prose
seg, fblock, subseq, delete_needles, globs_of, live_limb_guard = K4.seg, K4.fblock, K4.subseq, K4.delete_needles, K4.globs_of, K4.live_limb_guard


def rec(s=''):
    L.append(s)
    print(s)


def line_with(text, needle):
    """### **A2.** ### The FIRST LINE of a TEXT carrying the needle -- never the whole text."""
    for ln in (text or '').split(NL):
        if needle in ln:
            return ln
    return ''


FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md']
CEIL = ['README.md', 'REGISTRY.md']
OTHER = ['ERRATA.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md',
         'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
AFTER_LOCK = ('b566_reads.txt', 'b566_trials.json', 'b566_prints.txt', 'b566_e0.json', 'b566_findings.json', 'b566_weight.json')
BEFORE_LOCK = ('b566_ferry.txt', 'b566_ferry_scan.txt', 'b566_pins_stepzero.txt', 'b566_step1_license.txt', 'b566_step1_closure.txt',
               'b566_step1_distance.txt', 'b566_vendor_list.txt')
C_PUSHOUT = 'f0e41d7d'
EQ_SHA = '991c0428f7b04cfff4c848909a4b182ba75e1b89c462dc0335fbda567ad3ffeb'
SECOND = 'its converse vendored from Bulka at 35df682f'
CORPUS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
          'SIDE-effects', 'SIDE-silence-principle', 'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo']


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
    """### (R169)(1)(b), carried from b565_checks.py, pointed at this act's banks."""
    lk, rn = utc_epoch(face, 'locked at'), utc_epoch(lockn, 'run at')
    after = lk is not None and all(pushed_digest_ok(x) and (added_epoch(x) or 0) > lk for x in AFTER_LOCK)
    before = (lk is not None and rn is not None and rn <= lk and all(pushed_digest_ok(x) for x in BEFORE_LOCK)
              and 'ferry file                    : b566_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b566_ferry_scan.txt', 'b566_pins_stepzero.txt')))
    return after, before


RERUN = '--rerun-postpush' in sys.argv   # ### (R170)(3): one named record, no table regeneration


def written_by_digest(repo, rel):
    """### (R170)(3): a tracked modified file counts as written when its bytes (CR stripped) differ from the PUSHED tree."""
    p = os.path.join(repo, rel)
    work = cr0(open(p, 'rb').read()) if os.path.isfile(p) else b''
    pub = cr0(blob(repo, 'origin/main:' + rel.replace(os.sep, '/')))
    return pub is None or hashlib.sha256(work).hexdigest() != hashlib.sha256(pub).hexdigest()


def prior_by_digest(files, prior_rev):
    """### (R170)(3): every prior bank by content against the pre-act tip AND the pushed tree; untracked ones by file time."""
    pre, pub = tree_ids(ROOT, prior_rev, 'data'), tree_ids(ROOT, 'origin/main', 'data')
    bad, n_pre, n_pub, n_time = [], 0, 0, 0
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
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b566')
            and 'data/b566_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=60):
    """### the commits of this act in a repository: subjects opening `b566 --`, or housekeeping naming (R176) or b566."""
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b566 --') or (s.startswith('housekeeping:') and ('(R176)' in s or 'b566' in s)):
                out.append(h)
    return out


def files_of(repo, sha):
    return sorted(x for x in gits(repo, 'show', '--name-only', '--pretty=format:', sha).split(NL) if x.strip())


def vendored(S):
    """### every vendored file at the pushed main: header and body split at the header`s closing line; the body`s sha256, the
    ### header`s recorded sha256, the digest bank`s, and the clone`s blob at the pin (while the clone exists)."""
    dig = {r['dest']: r for r in S['vdig'].get('rows', [])}
    rows = []
    for p in [x for x in gits(KER, 'ls-tree', '-r', '--name-only', 'main', 'Vendored/Bulka').split(NL) if x.endswith('.lean')]:
        b = blob(KER, 'main:' + p) or b''
        cut_at = b.find(b"ALTERED.\n-/\n")
        hdr, body = (b[:cut_at + len(b"ALTERED.\n-/\n")], b[cut_at + len(b"ALTERED.\n-/\n"):]) if cut_at >= 0 else (b'', b)
        m = re.search(rb'sha256 of the body below = ([0-9a-f]{64})', hdr)
        src = p[len('Vendored/Bulka/'):]
        cl = blob(BULKA, PIN + ':' + src) if os.path.isdir(BULKA) else None
        rows.append(dict(path=p, hdr_ok=hdr.startswith(b'/-\nVENDORED INTO SIDE-explicit-formula') and (b'Pin        : ' + PIN.encode()) in hdr,
                         body=hashlib.sha256(body).hexdigest(), recorded=m.group(1).decode() if m else None,
                         bank=(dig.get(p) or {}).get('source_blob_sha256'), clone=hashlib.sha256(cl).hexdigest() if cl else None))
    return rows


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    locks = sorted(glob.glob(os.path.join(D, 'b566_lockgate_notes*.txt')))
    rd_d = lambda n: read(os.path.join(D, n))
    k = R.kstate6()
    S = dict(
        face=read(FACE), ferry=rd_d('b566_ferry.txt'), scan=rd_d('b566_ferry_scan.txt'),
        cens=rd_d('b566_census_stepzero.txt'), fcens=rd_d('b566_faces_census_stepzero.txt'), pins=rd_d('b566_pins_stepzero.txt'),
        procs=rd_d('b566_procs_stepzero.txt'), lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=rd_d('b565_closing.txt'), desk=rd_d('b566_desk_notes.txt'), defects=rd_d('b566_defects.txt'),
        sc=jload('b566_scores.json'), reads=rd_d('b566_reads.txt'),
        pushout=dict(files=files_of(ROOT, C_PUSHOUT),
                     anc=subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', C_PUSHOUT, 'HEAD']).returncode == 0),
        wj=jload('b566_weight.json'), cj=jload('b566_ceiling.json'), clj=jload('b566_complete_line.json'), pj=jload('b566_price.json'),
        fj=jload('b566_findings.json'), tj=jload('b566_trail.json'), rows=jload('b566_rows.json'),
        rehash=jload('b566_arda_rehash.json'), adel=rd_d('b566_arda_delete.txt'), arda_exists=os.path.exists(ARDA),
        bulka_head=gits(BULKA, 'rev-parse', 'HEAD') if os.path.isdir(BULKA) else '',
        lic=rd_d('b566_step1_license.txt'), lic_blob=hashlib.sha256(blob(BULKA, PIN + ':LICENSE') or b'').hexdigest(),
        lic_main=hashlib.sha256(blob(KER, 'main:Vendored/Bulka/LICENSE') or b'x').hexdigest(),
        lic_main_bytes=blob(KER, 'main:Vendored/Bulka/LICENSE') or b'',   # ### (R177)(3)(h): the BLOB, compared from b567
        lic_clone_bytes=(blob(BULKA, PIN + ':LICENSE') or b'') if os.path.isdir(BULKA) else None,
        clo=rd_d('b566_step1_closure.txt'), vlist=[x for x in rd_d('b566_vendor_list.txt').split(NL) if x.strip()],
        dist=rd_d('b566_step1_distance.txt'), vdig=jload('b566_vendor_digests.json'),
        notice=rd8(blob(KER, 'main:NOTICE')),
        tr=jload('b566_trials.json'), tra=rd_d('b566_trial_a_build.txt'), trb=rd_d('b566_trial_b_build.txt'), route=jload('b566_route.json'),
        eqs=rd_d('b566_eq_statement.txt'), eqb=rd_d('b566_eq_build.txt'),
        eq_main=hashlib.sha256(blob(KER, 'main:SIDEExplicitFormula/LiCriterionBridge.lean') or b'').hexdigest(),
        prints=rd_d('b566_prints.txt'), e0=jload('b566_e0.json'), kpush=rd_d('b566_kernel_push_out.txt'),
        k=k, lean_ns=[x for x in gits(KER, 'diff', '--name-status', R.V08, 'main', '--', '*.lean').split(NL) if x.strip()],
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        branches=rd_d('b566_branches.txt'),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + CEIL + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + CEIL + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b565*') for r in (ROOT, PP, SIDE, KER)},
        recomputed={k2: v for k2, v in jload('b566_scores.json').items() if k2 not in ('kstate',)},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b566_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b566_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b566_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b566_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b566 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        wl_add=ADD.accepted_bases(rd_d('b566_writelist_addendum.txt'), ADD.paste_reader(D)),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b566_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    S['vend'] = vendored(S)
    S['pushed'] = RERUN or is_pushed()
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    else:
        S['after_lock'] = all(os.path.exists(os.path.join(D, x)) and os.path.getmtime(os.path.join(D, x)) > os.path.getmtime(FACE) for x in AFTER_LOCK)
        S['before_lock'] = all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in BEFORE_LOCK)
    S['priv_names'] = K542.techne_private_names()
    # ### the act's own words: every b566 bank and tool EXCEPT the banks that carry third-party text verbatim -- the licence, and
    # ### the build logs and print and push captures (Lean's, lake's and git's own output), as b565 excepted the clones' output.
    third = re.compile(r'^b566_(step1_license|trial_[ab]_build|route_vendor_build|eq_build|reprint_all|kernel_push_out|prints|provenance)')
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b566_') and os.path.isfile(os.path.join(D, f))
               and not third.match(f)] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b566_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in FIXED + CEIL:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = NL.join(l for l in S['corr'].split(NL) if l not in set(S['corr_prior'].split(NL)))
    S['act_blobs'] = blobs
    kk = set(os.path.basename(x) for x in S['tracked'])
    for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'main'), (KER, R.BR_A)):
        for h in act_commit(repo, rev):
            kk |= set(os.path.basename(x) for x in files_of(repo, h))
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
                kk.add(os.path.basename(rel))
    S['kinds'] = kk
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-5][0-9]_|^b56[0-5]_|^b334_', f)]
    S['prior_checked'] = len(prior)
    if S['pushed']:
        S['noprior'], S['prior_pre'], S['prior_pub'], S['prior_time'], S['prior_bad'] = prior_by_digest(prior, PRIOR_RELAY)
    else:
        S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


# ================================================================================ this act's arm helpers
P = R.poss
TRAILH = '### b566 —'


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0].split(',')[0]


def word_of(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def kept(S, f):
    old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
    return subseq(old, new) and new.startswith(old)


def fline(S, n):
    F = S['find'].split(NL)
    return F[n - 1] if n and n <= len(F) else ''


def reads_ok(S):
    r = S['reads']
    need = ['relay data/b565_audit.json -- Bulka:', 'the converse`s fully qualified name and module: LiCriterion.positivity_implies_RH',
            'theorem taylorCoeff_eq_li_symmetrized', 'OPEN_TRAILS.md ((R82)/(R83), the Zeta23 vendoring record)',
            'SIDE-explicit-formula README.md at v0.8', 'SIDE-explicit-formula lake-manifest.json at v0.8', 'def LiCoeff',
            'theorem li_identity_sym', 'MATHLIB AT 51e6992e', 'MATHLIB AT de5ce8a9', 'lemma Gammaℝ_ne_zero_of_re_pos',
            'FINDINGS.md (b565`s field line) :6168', 'README.md (the ceiling', 'OPEN_TRAILS.md (the (R175)(3) conditional, b565) :11630',
            'OPEN_TRAILS.md (the converse`s price, b564) :11609', 'b565_closing_push_out.txt -- committed alone']
    return all(x in r for x in need) and 'NOT FOUND' not in r


def procs_ok(S):
    p = S['procs']
    return ('ORPHANS STOPPED : 0' in line_with(p, 'ORPHANS STOPPED') and 'POSITIVE CONTROL' in p
            and 'candidates other than powershell.exe: 0' in p)


def weight_ok(S):
    n = S['wj'].get('line')
    t = fline(S, n)
    return (t.startswith(P(R.WEIGHT6_H)) and S['find'].count(P(R.WEIGHT6_H)) == 1 and 'all 19 audited terminals' in t
            and 'no priority is claimed' in t and 'H17a refuted' in t and 'H17b refuted' in t)


def no_priority_text(S):
    txt = ' '.join([fline(S, S['wj'].get('line')), fline(S, S['clj'].get('line')), fblock(S['find'], P(R.FH6))])
    bad = re.compile(r'\b(?:we|the programme|this (?:act|kernel)) (?:is|was|are) the first\b|\bfirst formali[sz]ation\b', re.I)
    return ('no priority is claimed' in txt.lower() or 'No priority is claimed' in txt) and 'claims priority' in txt and not bad.search(txt)


def ceiling_ok(S):
    s = S['cj'].get('sentence') or ''
    f = ' '.join(S['ferry'].split())
    ok = bool(s) and ('"%s"' % s) in f
    for name in CEIL:
        old, new = rd8(S['pp_prior'][name]).split(NL), rd8(S['pp_now'][name]).split(NL)
        added = [l for l in new if l not in set(old)]
        ok = ok and subseq(rd8(S['pp_prior'][name]), rd8(S['pp_now'][name])) and len(added) == 1 and s in added[0]
        ok = ok and new[S['cj']['files'][name]['new_line'] - 1] == added[0] and '(R174)' in new[S['cj']['files'][name]['new_line'] - 3]
    return ok


def vendor_bytes(S):
    v = S['vend']
    return (len(v) == 33 and all(r['body'] == r['recorded'] == r['bank'] for r in v)
            and all(r['clone'] in (None, r['body']) for r in v) and sum(1 for r in v if r['clone']) == (33 if os.path.isdir(BULKA) else 0))


def trial_a_ok(S):
    a = S['tr'].get('a', {})
    errs = re.findall(r'^error: Vendored/Bulka/(\S+):\d+:\d+: Unknown identifier `(ite_eq_(?:right|left))`', S['tra'], re.M)
    return (a.get('modules') == 33 and a.get('errors') == 3 and a.get('bad') == ['Hadamard.General.Factorization'] and not a.get('clean')
            and len(errs) == 3 and all(e[0] == 'Hadamard/General/Factorization.lean' for e in errs))


def trial_b_ok(S):
    b = S['tr'].get('b', {})
    rc0 = set(re.findall(r'^--- \+(\S+) rc=0 ', S['trb'], re.M))
    return (b.get('modules') == 79 and b.get('ok') == 79 and b.get('errors') == 0 and b.get('clean') and len(rc0) == 79
            and not re.search(r'^--- \+\S+ rc=(?!0 )', S['trb'], re.M))


def eq_first(S):
    t0 = re.search(r'written at \(UTC\) (\S+)', S['eqs'])
    b0 = re.search(r'^=== (\S+) \+SIDEExplicitFormula\.LiCriterionBridge ', S['eqb'], re.M)
    return (bool(t0) and bool(b0) and t0.group(1) < b0.group(1) and ('sha256 %s' % EQ_SHA) in S['eqs'] and S['eq_main'] == EQ_SHA
            and 'li_coeff_eq_taylorCoeff (n : ℕ) : LiCoeff (n + 1) = (LiCriterion.taylorCoeff LiCriterion.riemannXi n).re' in S['eqs'])


def eq_lemmas(S):
    rows = S['e0'].get('rows', {})
    need = ['carrierEquiv', 'analyticOrderAt_xi_eq_zeta', 'zeroMult_eq_xiMult', 'neg_term_eq', 'li_coeff_eq_taylorCoeff']
    return (all(rows.get(R.NSB + n, {}).get('std3') for n in need) and 'SIDEExplicitFormula.LiCriterionBridge rc=0 ' in S['eqb'])


def composed_prints(S):
    p = R.prints_axioms(S['prints'])
    return (all(p.get(R.NSB + n) == list(R.STD3) for n in ('li_nonneg_iff_rh', 'arith_limit_nonneg_iff_rh', 'li_coeff_eq_taylorCoeff'))
            and 'sorryAx' not in S['prints'] and len(p) == 27)


def grades_ok(S):
    e = S['e0']
    rows = e.get('rows', {})
    return (e.get('gate') is True and all(rows.get(R.NSB + n, {}).get('grade') == 'DERIVES' for n in R.TERMS6)
            and all(r.get('grade') in ('DERIVES', 'INTERFACES', 'DEF') for r in rows.values()) and e.get('tip', '').startswith(R.V09[:7]))


def tag_ok(S):
    k = S['k']
    kp = S['kpush']
    i_main = kp.find('push_gated: main read back at the remote: ' + k['main'])
    i_tag = kp.find('push_gated: tag v0.9 peeled local')
    return (k['v09'] == k['main'] == k['fwd'] and k['v09type'] == 'tag' and k['remote'].get('refs/heads/main') == k['main']
            and k['remote'].get('refs/tags/v0.9^{}') == k['v09'] and 0 <= i_main < i_tag)


def other_trial_ok(S):
    k = S['k']
    return (k['remote'].get('refs/heads/' + R.BR_A) == k['back'] and k['back'].startswith('76c1f11')
            and k['remote'].get('refs/heads/' + R.BR_B) == k['fwd'])


def ot_once_at(S, head, line):
    ot = rd8(S['pp_now']['OPEN_TRAILS.md']).split(NL)
    ln = [i + 1 for i, l in enumerate(ot) if l.startswith(P(head))]
    return ln == [line] and bool(line)


def price_ok(S):
    n = S['pj'].get('line')
    t = S['ot'].split(NL)[n - 1] if n else ''
    return ot_once_at(S, R.WO6, n) and all(x in t for x in ('(L1)', '(L2)', '(L3)', 'Not attempted', 'inequalityToPositivity', '2f71068'))


def field_ok(S):
    t = fline(S, S['clj'].get('line'))
    return (t.startswith(P(R.COMP6_H)) and S['find'].count(P(R.COMP6_H)) == 1 and 'v0.9' in t and S['k']['v09'][:7] in t
            and '35df682f' in t and 'THE COMPOSITION LANDED' in t)


def findings_ok(S):
    F = S['find'].split(NL)
    b = fblock(S['find'], P(R.FH6))
    n = S['fj'].get('heading_line', 0)
    return (S['find'].count(P(R.FH6)) == 1 and bool(n) and F[n - 1] == P(R.FH6) and 'b567' in b and 'GRH-Weil act three' in b
            and 'v0.9' in b and kept(S, 'FINDINGS.md'))


def row_line(S, n):
    rs = [l for l in S['corr'].split(NL) if l.startswith('| %s |' % n)]
    return rs[0] if len(rs) == 1 else ''


def corr_ok(S):
    rr = [row_line(S, n) for n in (R.ROW_ACT6,) + R.ROW_T]
    return (all(rr) and all(r.get('exit') == 0 for r in S['rows'].get('rows', [])) and len(S['rows'].get('rows', [])) == 4
            and all(S['k']['v09'][:7] in r for r in rr) and S['corr'].startswith(S['corr_prior'].rstrip(NL))
            and all(('`%s` DERIVES' % n) in row_line(S, rn) for rn, n in zip(R.ROW_T, R.TERMS6)))


def trail_ok(S):
    return ot_once_at(S, R.HEADING6, S['tj'].get('line')) and '**Entered:**' in trail(S) and '**(R176) ratified' in trail(S)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b565 (was ') == 3
            and b.count('Deleted branch push-b565-closing (was ') == 1)


def held_kept(S):
    k = S['k']
    return all(k['kept'][b].startswith(t[:12]) and k['remote'].get('refs/heads/' + b, '').startswith(t[:12]) for b, t in R.Z5.KEPT5.items())


def others_ok(S):
    m = S['k']['mains']
    return (len(m) == len(R.Z5.PRE_HEADS5) and all(v == [] for k2, v in m.items() if k2 not in ('SIDE-global-section', 'SIDE-explicit-formula'))
            and set(m.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'})


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


def hword(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0]


VACUOUS_ARMS = ()


def _nscore_arm(k, reads):
    return ('G-%s-SCORED' % k.upper(), reads, lambda S: nscored(S, k), lambda S: put(S, 'sc', dict(S['sc'], **{k: not S['sc'].get(k)})))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R176) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b566' in S['ferry'],
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
    ('G-STEPZERO-PROCS', 'the banked process listing -- its positive control matched, candidates counted, orphans stopped printed',
     lambda S: procs_ok(S), lambda S: put(S, 'procs', S['procs'].replace('ORPHANS STOPPED : 0', 'ORPHANS STOPPED : ?'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'the LAST lock-gate run file, a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 4'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b565`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b565' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b566' in S['ferry'] and 'ACT b566' in S['face'] and not glob.glob(os.path.join(D, 'b567_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b566')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; before the push file times, after it content digests against the pushed tree',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'DECLARED AS PEEKS' in flat(S['face'])
                and S['after_lock'] and S['before_lock']),
     lambda S: put(S, 'after_lock', False)),
    ('G-R176-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R176) END' in S['ferry'] and S['ot'].count('**(R176) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R176) ratified', '(R176) noted'))),
    ('G-READS-CITED', 'the reads bank -- the audit json, the converse, the vendoring record, the kernel`s pins and objects, Mathlib at both pins, the ledger sites',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('MATHLIB AT de5ce8a9', 'x'))),
    ('G-PUSHOUT-COMMITTED', 'relay commit f0e41d7d READ HERE -- b565`s closing push output alone, in HEAD`s ancestry',
     lambda S: S['pushout']['files'] == ['data/b565_closing_push_out.txt'] and S['pushout']['anc'],
     lambda S: put(S, 'pushout', dict(S['pushout'], files=['data/b565_closing_push_out.txt', 'x']))),
    ('G-WEIGHT-LINE', 'FINDINGS READ HERE -- the weight line once at its banked line, (R176)(1)`s terms',
     lambda S: weight_ok(S), lambda S: put(S, 'wj', dict(S['wj'], line=1))),
    ('G-NO-PRIORITY-SENTENCE', 'the weight line, the composition`s line and the entry -- the no-priority sentence present, no priority claimed',
     lambda S: no_priority_text(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH6), P(R.FH6) + ' -- this kernel is the first to prove it'))),
    ('G-CEILING-APPENDED', 'README.md and REGISTRY.md READ HERE against b565`s PLACE-papers tip -- the author`s sentence once, beside b564`s line, nothing else moved',
     lambda S: ceiling_ok(S), lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b'\nx\n'}))),
    ('G-ARDA-REHASHED', 'the rehash bank -- every Arda bank against its relay blob at b565`s close',
     lambda S: S['rehash'].get('total') == 13 and S['rehash'].get('agree') == 13 and all(r['agree'] for r in S['rehash'].get('banks', [])),
     lambda S: put(S, 'rehash', dict(S['rehash'], agree=12))),
    ('G-ARDA-DELETED', 'the clone`s path READ HERE, and the deletion bank -- the path verified in the command, rc 0, ABSENT',
     lambda S: (not S['arda_exists'] and 'END ' in S['adel'] and 'rc=0' in S['adel'] and 'D:/audit-b565/arda ABSENT' in S['adel']
                and 'test "$H" = "acfb0ee5' in S['adel']),
     lambda S: put(S, 'arda_exists', True)),
    ('G-BULKA-KEPT', 'Bulka`s clone READ HERE -- its HEAD the pin',
     lambda S: S['bulka_head'] == PIN, lambda S: put(S, 'bulka_head', '')),
    ('G-LICENCE-PRINTED', 'the licence bank`s BLOB LINE ((R177)(3)(h)) against the LICENSE blob on main and the clone`s at the pin',
     lambda S: (('LICENSE blob' in S['lic']) and ADD.blob_matches(S['lic'], S['lic_main_bytes'])
                and (S['lic_clone_bytes'] is None or ADD.blob_matches(S['lic'], S['lic_clone_bytes']))
                and 'Apache License' in S['lic'] and 'Version 2.0, January 2004' in S['lic']),
     lambda S: put(S, 'lic_main_bytes', S['lic_main_bytes'].replace(b'\n', b'\r\n'))),
    ('G-CLOSURE-LISTED', 'the closure bank and the vendor list -- the converse`s 12, Fidelity`s 33, each module named',
     lambda S: ('ITS CLOSURE: 12 MODULES' in S['clo'] and 'ITS CLOSURE: 33 MODULES' in S['clo'] and len(S['vlist']) == 33
                and all(('    ' + m) in S['clo'] for m in S['vlist'])),
     lambda S: put(S, 'vlist', S['vlist'][:-1])),
    ('G-DISTANCE-PRINTED', 'the distance bank -- the count both ways, printed before trial (a)`s first call',
     lambda S: ('(A-only first, B-only second): 0 129' in S['dist'] and 'A ancestor of B         : yes' in S['dist']
                and re.search(r'at (\S+Z)\.', S['dist']) and re.search(r'^=== (\S+) ', S['tra'], re.M)
                and re.search(r'at (\S+Z)\.', S['dist']).group(1) < re.search(r'^=== (\S+) ', S['tra'], re.M).group(1)),
     lambda S: put(S, 'dist', S['dist'].replace('0 129', '129 0'))),
    ('G-VENDOR-BYTES', 'every vendored file at the pushed main -- the body`s sha256 against its header, the digest bank and the clone`s blob at the pin',
     lambda S: vendor_bytes(S), lambda S: put(S, 'vend', [dict(r, body='0' * 64) if i == 0 else r for i, r in enumerate(S['vend'])])),
    ('G-VENDOR-HEADERS', 'every vendored file at the pushed main -- Zeta23`s header form, the pin named',
     lambda S: len(S['vend']) == 33 and all(r['hdr_ok'] for r in S['vend']),
     lambda S: put(S, 'vend', [dict(r, hdr_ok=False) if i == 5 else r for i, r in enumerate(S['vend'])])),
    ('G-NOTICE-CARRIED', 'NOTICE at the pushed main -- the source, the pin, the licence`s place',
     lambda S: all(x in S['notice'] for x in ('nicholasbulka/li-criterion-rh-equivalence-lean', PIN, 'Vendored/Bulka/LICENSE', 'Copyright 2026 Nicholas Bulka')),
     lambda S: put(S, 'notice', S['notice'].replace(PIN, 'x'))),
    ('G-TRIAL-A-BUILT', 'the trial (a) log and the trials json -- 33 modules, 3 errors in Factorization, the identifiers named',
     lambda S: trial_a_ok(S), lambda S: put(S, 'tr', dict(S['tr'], a=dict(S['tr'].get('a', {}), errors=0)))),
    ('G-TRIAL-B-BUILT', 'the trial (b) log and the trials json -- 79 modules, every call rc 0',
     lambda S: trial_b_ok(S), lambda S: put(S, 'trb', S['trb'] + NL + '--- +Zeta23.Defs rc=1 secs=1')),
    ('G-ROUTE-NAMED', 'the route json against the trials json',
     lambda S: (S['route'].get('word', '').startswith('ROUTE (b)') and S['tr']['b']['clean'] and not S['tr']['a']['clean']
                and S['route'].get('held') is False),
     lambda S: put(S, 'route', dict(S['route'], word='ROUTE (a), THE BACKPORT'))),
    ('G-EQ-STATEMENT-FIRST', 'the statement bank`s time against the module`s first build, and its digest against the file on main',
     lambda S: eq_first(S), lambda S: put(S, 'eq_main', '0' * 64)),
    ('G-EQ-LEMMAS-BANKED', 'the E0 json and the module`s build log -- (E1)-(E4) and the equality lemma at the standard three, rc 0',
     lambda S: eq_lemmas(S), lambda S: put(S, 'eqb', S['eqb'].replace('LiCriterionBridge rc=0 ', 'LiCriterionBridge rc=1 '))),
    ('G-COMPOSED-PRINTS', 'the prints bank -- the composed theorems and the equality lemma at the standard three, no sorryAx, 27 prints',
     lambda S: composed_prints(S), lambda S: put(S, 'prints', S['prints'] + NL + 'sorryAx')),
    ('G-GRADES-BANKED', 'the E0 json -- the gate, the terminals of record DERIVES, the record taken at v0.9',
     lambda S: grades_ok(S), lambda S: put(S, 'e0', dict(S['e0'], gate=False))),
    ('G-TAG-READ-BACK', 'the kernel`s refs READ HERE and the push capture -- main read back before the tag, the tag peeled to main',
     lambda S: tag_ok(S), lambda S: put(S, 'kpush', S['kpush'].replace('push_gated: main read back at the remote:', 'x'))),
    ('G-OTHER-TRIAL-PUSHED', 'the kernel`s remote refs READ HERE -- both trial branches at their tips',
     lambda S: other_trial_ok(S), lambda S: put(S, 'k', dict(S['k'], remote=dict(S['k']['remote'], **{'refs/heads/' + R.BR_A: '0' * 40})))),
    ('G-KERNEL-STATEMENTS-KEPT', 'the kernel`s .lean files, v0.8 against the pushed main -- additions only',
     lambda S: bool(S['lean_ns']) and all(x.startswith('A') for x in S['lean_ns']),
     lambda S: put(S, 'lean_ns', list(S['lean_ns']) + ['M\tSIDEExplicitFormula/LiWeil.lean'])),
    ('G-RESIDUE-PRICED', 'OPEN_TRAILS READ HERE -- the price once at its banked line, (L1)-(L3), the other premise named, not attempted',
     lambda S: price_ok(S), lambda S: put(S, 'pj', dict(S['pj'], line=1))),
    ('G-FIELD-LINE', 'FINDINGS READ HERE -- the composition`s line once at its banked line, v0.9 and the pin',
     lambda S: field_ok(S), lambda S: put(S, 'clj', dict(S['clj'], line=1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once at its banked line, b567 named, the file kept',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH6), 'x'))),
    ('G-CORR-ROWS', 'CORRESPONDENCE READ HERE -- rows 403-406 once each, exits 0, v0.9 cited, the ledger a true prefix extended',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 406 |', '| 407 |'))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS READ HERE -- this act`s record once at its banked line',
     lambda S: trail_ok(S), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-SECOND-AMENDMENT-WAITS', 'README.md and REGISTRY.md READ HERE -- the second amendment`s words absent',
     lambda S: all(SECOND.encode('utf-8') not in S['pp_now'][f] for f in CEIL),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + SECOND.encode('utf-8')}))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in four repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b565'}))),
    ('G-HELD-BRANCH-KEPT', 'the kernel`s refs READ HERE -- the five kept branches at their tips local and remote',
     lambda S: held_kept(S), lambda S: put(S, 'k', dict(S['k'], kept=dict(S['k']['kept'], **{'grh-weil-b562': '0' * 40})))),
    ('G-LINES-KEPT', 'FINDINGS and OPEN_TRAILS against their blobs at b565`s commit -- true prefixes',
     lambda S: all(kept(S, f) for f in FIXED),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-OTHER-KERNELS-UNTOUCHED', 'every other kernel`s main READ HERE against its pre-act head -- SIDE-global-section`s ledger rows alone',
     lambda S: others_ok(S), lambda S: put(S, 'k', dict(S['k'], mains=dict(S['k']['mains'], **{'SIDE-kernel': ['Kernel/X.lean']})))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b566_x.py'])),
    ('G-DELETE-FREE', 'this act`s own Python tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b566_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b566 bank and tool (third-party output excepted) and this act`s ledger bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    _nscore_arm('n1', 'the desk against the licence bank (H19a)'),
    _nscore_arm('n2', 'the desk against the trials json'),
    _nscore_arm('n3', 'the desk against the closure bank'),
    _nscore_arm('n4', 'the desk against the E0 json (H19c)'),
    _nscore_arm('n5', 'the desk against the prints, the grades and the tag'),
    _nscore_arm('n6', 'the desk against the kernel mains, the deposit and the kept branches'),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-H19-SCORED', 'the desk against the banks -- H19a-H19d, each word from the scores',
     lambda S: all(hword(S, x) == word_of(S['sc'][x.lower()]) and S['sc'][x.lower()] == S['recomputed'][x.lower()]
                   for x in ('H19a', 'H19b', 'H19c', 'H19d')),
     lambda S: put(S, 'sc', dict(S['sc'], h19b=not S['sc'].get('h19b')))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b566 -'))),
    ('G-PRIORBANK-UNCHANGED', 'before the push file times against the face; after it content digests against the pre-act tip and the pushed tree, no exception',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED + CEIL), lambda S: put(S, 'tracked', list(S['tracked']) + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING6)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING6) + ' a second record')),
    ('G-WRITELIST-KINDS', 'every b566 commit in four repositories (the kernel`s main and the backport branch), against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds'] if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))
                          and k not in S['wl_add']),   # ### (R177)(3)(g): an ACCEPTED post-seal addendum carries the file
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text', lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
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
                and "log', '-1', '--pretty=%s').startswith('b566')" in S['suite']
                and "data/b566_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b566_components.txt' in gits(ROOT, 'show'")),
]


def regenerate():
    """### ### **(R107): THE GENERATOR IS PART OF THE CLOSING SUITE** -- re-run before anything is scored; its diff a cell."""
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    diff = json.loads(read(os.path.join(D, 'terminal_table_diff.json')) or '{}')
    return r.returncode, diff


def main():
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if RERUN else regenerate()   # ### (R170)(3): a re-run does not regenerate the table
    S['table'] = read(os.path.join(D, 'terminal_table.md'))
    tl = [l for l in S['table'].split(NL) if '`SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh` |' in l]
    rec('  ### the regenerated table`s line for li_nonneg_iff_rh: %s' % (tl[0][:220] if len(tl) == 1 else 'lines found %d' % len(tl)))
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    names = [a[0] for a in ARMS]
    pushed = S['pushed']
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b566 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d' % (len(declared), len(names), len(deferred)))
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
        try:
            live = bool(pred(S))
        except Exception as e:  # ### an arm that cannot read its source FAILS; it is never skipped
            live = False
            rec('  ### %s raised %s: %s' % (name, type(e).__name__, str(e)[:160]))
        try:
            neg = bool(pred(dict(S)))
        except Exception:
            neg = False
        try:
            p = bool(pred(pos(S)))
        except Exception:
            p = False
        if not neg:
            negfail += 1
        if p:
            defective.append(name)
        v = 'OK' if (neg and not p) else ('### DEFECTIVE' if p else '### NEG FAILS')
        rec('  %-42s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    stray = sorted(k for k in S['kinds'] if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### of them, carried by an ACCEPTED post-seal addendum ((R177)(3)(g)) : %d %s'
        % (len([x for x in stray if x in S['wl_add']]), sorted(x for x in stray if x in S['wl_add']) or ''))
    for a in ADD.writelist_addenda(read(os.path.join(D, 'b566_writelist_addendum.txt')), ADD.paste_reader(D)):
        rec('  ###   %s -> %s' % (a['line'], a['why']))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        if gen_diff.get('first_run'):
            rec('  ###   ### **NO PRIOR RUN TO DIFF AGAINST -- THIS CLOSE IS THE FIRST.**')
        else:
            rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
                % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []), len(gen_diff.get('changed') or [])))
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
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if RERUN:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1])
        io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
        print('  written: %s' % os.path.basename(out))
        return 0 if ok else 1
    out = os.path.join(D, 'b566_checks_postpush.txt' if pushed else 'b566_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective, neg_failures=negfail,
                   declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b566_exercise.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
