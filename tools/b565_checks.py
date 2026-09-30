# -*- coding: utf-8 -*-
"""b565_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b564's AND RE-POINTED ARM BY ARM TO b565's (G2).

### ### b565: THE AUDIT OF TWO PUBLIC FORMALIZATIONS; THE SUPERSEDED GRADE IN A READABLE CELL; HOUSEKEEPING, UNDER (R175).
### The act's own arms, sources() and helpers were written for this face; the harness, the generic helpers (imported from
### b564_checks, never copied) and the digest readings are b564's, re-pointed. The (W) reader is b564's `globs_of` (a `<...>`
### placeholder reads as `*`), as tools/SUITE_README.md records.

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
import time
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b564_checks as K4          # ### the generic helpers, imported (b564's, carried)
import b565_record as R
import b542_checks as K542
import terminal_table as TT

D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
AUD = os.path.join('D:', os.sep, 'audit-b565')
FACE = os.path.join(D, 'b565_registration_2026-09-30.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = R.PRIOR_RELAY   # ### 58d73d24, b564's table housekeeping -- relay's tip before this act
PRIOR_PP = R.PRIOR_PP         # ### 5c50649, b564's PLACE-papers commit
PRIOR_GS = R.PRIOR_GS         # ### 1135887, SIDE-global-section before this act
NL = chr(10)
BT = chr(96)
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
OTHER = ['ERRATA.md', 'README.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md',
         'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
AFTER_LOCK = ('b565_housekeeping.txt', 'b565_supersede_after.json', 'b565_audit_bulka_prints.txt', 'b565_audit_arda_prints.txt',
              'b565_audit.json', 'b565_findings.json')
BEFORE_LOCK = ('b565_ferry.txt', 'b565_ferry_scan.txt', 'b565_pins_stepzero.txt')
C_PUSHOUT, C_CAPTURE, C_SYNONYM = '80346ab6', '9de84b16', '7a2defb1'
PINS = dict(bulka='35df682f', arda='acfb0ee5')
# ### the clones' OWN files, by basename, that no repository of the corpus may track (G-CLONES-OUTSIDE-CORPUS)
CLONE_NAMES = ('E6Bridge27.lean', 'E6Bridge4.lean', 'RvMBridgeXi.lean', 'RvMBridgeGauss.lean', 'AxiomGuardRvMBridge.lean',
               'GenusOnePairedSumFormula.lean', 'XiOrderBridge.lean', 'HadamardSummabilityBridge.lean', 'Pringsheim.lean',
               'ReverseDirection.lean', 'BorelCaratheodory.lean', 'ChallengeDeps.lean')
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
    """### (R169)(1)(b), carried from b564_checks.py, pointed at this act's banks."""
    lk, rn = utc_epoch(face, 'locked at'), utc_epoch(lockn, 'run at')
    after = lk is not None and all(pushed_digest_ok(x) and (added_epoch(x) or 0) > lk for x in AFTER_LOCK)
    before = (lk is not None and rn is not None and rn <= lk and all(pushed_digest_ok(x) for x in BEFORE_LOCK)
              and 'ferry file                    : b565_ferry.txt' in scan
              and all(re.search(re.escape(x) + r'\s+PASS', lockn) for x in ('b565_ferry_scan.txt', 'b565_pins_stepzero.txt')))
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
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b565')
            and 'data/b565_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=40):
    """### the commits of this act in a repository: subjects opening `b565 --`, or housekeeping naming (R175) or b565."""
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b565 --') or (s.startswith('housekeeping:') and ('(R175)' in s or 'b565' in s)):
                out.append(h)
    return out


def files_of(repo, sha):
    return sorted(x for x in gits(repo, 'show', '--name-only', '--pretty=format:', sha).split(NL) if x.strip())


def kstate5():
    """### every kernel`s main against its pre-act head (b565: SIDE-explicit-formula at v0.8 = 6ec71b3), the kept branches."""
    mains = {}
    for k2, h in R.PRE_HEADS5.items():
        mains[k2] = sorted(x for x in gits(os.path.join('D:', os.sep, k2), 'diff', '--name-only', h, 'main').split(NL) if x.strip())
    ls = {}
    for l in git(KER, 'ls-remote', 'origin').split(NL):
        if '\t' in l:
            h, r = l.split('\t')
            ls[r.strip()] = h.strip()
    kept = {b: gits(KER, 'rev-parse', b) for b in R.KEPT5}
    return dict(mains=mains, remote=ls, kept=kept, main=gits(KER, 'rev-parse', 'main'))


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    locks = sorted(glob.glob(os.path.join(D, 'b565_lockgate_notes*.txt')))
    rd_d = lambda n: read(os.path.join(D, n))
    S = dict(
        face=read(FACE), ferry=rd_d('b565_ferry.txt'), scan=rd_d('b565_ferry_scan.txt'),
        cens=rd_d('b565_census_stepzero.txt'), fcens=rd_d('b565_faces_census_stepzero.txt'), pins=rd_d('b565_pins_stepzero.txt'),
        procs=rd_d('b565_procs_stepzero.txt'), lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=rd_d('b564_closing.txt'), desk=rd_d('b565_desk_notes.txt'), defects=rd_d('b565_defects.txt'),
        sc=jload('b565_scores.json'), reads=rd_d('b565_reads.txt'), hk=rd_d('b565_housekeeping.txt'),
        cap=rd_d('b565_capture_test.txt'), fs=read(os.path.join(T, 'FERRY_STANDING.md')),
        fs_prior=rd8(blob(ROOT, PRIOR_RELAY + ':tools/FERRY_STANDING.md')),
        pg=read(os.path.join(T, 'push_gated.sh')), pg_prior=rd8(blob(ROOT, PRIOR_RELAY + ':tools/push_gated.sh')),
        sreadme=read(os.path.join(T, 'SUITE_README.md')),
        tt_src=read(os.path.join(T, 'terminal_table.py')), tt_prior=rd8(blob(ROOT, PRIOR_RELAY + ':tools/terminal_table.py')),
        syn=rd_d('b565_synonym_unit.txt'), noop=rd_d('b565_supersede_noop.txt'), after=rd_d('b565_supersede_after.txt'),
        aj=jload('b565_supersede_after.json'), nj=jload('b565_supersede_noop.json'), tline=rd_d('b565_supersede_tableline.txt'),
        commits={c: dict(files=files_of(ROOT, c), subject=gits(ROOT, 'log', '-1', '--pretty=%s', c),
                         anc=subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', c, 'HEAD']).returncode == 0)
                 for c in (C_PUSHOUT, C_CAPTURE, C_SYNONYM)},
        audit=rd_d('b565_audit.txt'), au=jload('b565_audit.json'), core=jload('b565_audit_core.json'),
        clones={r: jload('b565_audit_%s_clone.json' % r) for r in PINS},
        heads={r: gits(os.path.join(AUD, r), 'rev-parse', 'HEAD') for r in PINS},
        infos={r: ''.join(read(p) for p in sorted(glob.glob(os.path.join(D, 'b565_audit_%s_info*.txt' % r)))) for r in PINS},
        builds={r: rd_d('b565_audit_%s_build.txt' % r) for r in PINS},
        prints={r: rd_d('b565_audit_%s_prints.txt' % r) for r in PINS},
        sreads={r: rd_d('b565_audit_%s_reads.txt' % r) + rd_d('b565_audit_%s_reads2.txt' % r) for r in PINS},
        sorry={os.path.basename(p)[len('b565_audit_'):-5]: json.loads(read(p) or '{}')
               for p in glob.glob(os.path.join(D, 'b565_audit_*_sorry_*.json'))},
        zpins=json.loads(rd_d('b565_zeta23_pins.json') or '[]'),
        corpus_tracked={c: [x for x in gits(os.path.join('D:', os.sep, *c.split('/')), 'ls-files').split(NL) if x.strip()] for c in CORPUS},
        faj=jload('b565_fieldline.json'), cj=jload('b565_conditional.json'), fj=jload('b565_findings.json'), rows=jload('b565_rows.json'),
        tj=jload('b565_trail.json'),
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        branches=rd_d('b565_branches.txt'),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + OTHER},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + OTHER},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), k=kstate5(),
        trial=dict(head=gits(R.Z4.Q.P.TRIAL, 'rev-parse', 'HEAD'), status=gits(R.Z4.Q.P.TRIAL, 'status', '--porcelain', '--untracked-files=no')),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b564*') for r in (ROOT, PP, SIDE, KER)},
        recomputed={k2: v for k2, v in jload('b565_scores.json').items() if k2 != 'kstate'},
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b565_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b565_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b565_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b565_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b565 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b565_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    S['pushed'] = RERUN or is_pushed()
    if S['pushed']:
        S['after_lock'], S['before_lock'] = peek_by_digest(S['face'], S['lock'], S['scan'])
    else:
        S['after_lock'] = all(os.path.exists(os.path.join(D, x)) and os.path.getmtime(os.path.join(D, x)) > os.path.getmtime(FACE) for x in AFTER_LOCK)
        S['before_lock'] = all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE) for x in BEFORE_LOCK)
    S['priv_names'] = K542.techne_private_names()
    # ### the act's own words: every b565 bank and tool EXCEPT the banks that carry the clones' own Lean output verbatim
    # ### (the prints, the reads, the build logs, the clone and info banks) -- third-party text, as b564 excepted its fetched files.
    third = re.compile(r'^b565_audit_(bulka|arda)_(prints|reads2?|build|clone|info)')
    scanned = [os.path.join(D, f) for f in os.listdir(D) if f.startswith('b565_') and os.path.isfile(os.path.join(D, f))
               and not third.match(f)] + [os.path.join(T, f) for f in os.listdir(T) if f.startswith('b565_')]
    blobs = {os.path.basename(p): read(p) for p in scanned}
    for f in FIXED:
        old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
        blobs[f] = NL.join(l for l in new.split(NL) if l not in set(old.split(NL)))
    blobs['CORRESPONDENCE.md'] = NL.join(l for l in S['corr'].split(NL) if l not in set(S['corr_prior'].split(NL)))
    S['act_blobs'] = blobs
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'main')):
        for h in act_commit(repo, rev):
            k |= set(os.path.basename(x) for x in files_of(repo, h))
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-5][0-9]_|^b56[01234]_|^b334_', f)]
    S['prior_checked'] = len(prior)
    if S['pushed']:
        S['noprior'], S['prior_pre'], S['prior_pub'], S['prior_time'], S['prior_bad'] = prior_by_digest(prior, PRIOR_RELAY)
    else:
        S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


# ================================================================================ this act's arm helpers
P = R.poss
TRAILH = '### b565 —'


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0].split(',')[0]


def word_of(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def kept(S, f):
    old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
    return subseq(old, new) and new.startswith(old)


def reads_ok(S):
    r = S['reads']
    need = ['b564_prior_art.txt', 'FINDINGS.md (b536`s prior-art record and its audit form) :4729-:4750',
            'SIDE-explicit-formula README.md (the vendoring record of Zeta23)', 'SIDE-explicit-formula NOTICE',
            'SIDE-explicit-formula lakefile.toml', 'OPEN_TRAILS.md ((R82)`s condition, (R83))',
            'FINDINGS.md (the field entry as b564 wrote it) :6136', 'CORRESPONDENCE row 395 :', 'CORRESPONDENCE row 397 :',
            'tools/terminal_table.py (SYNONYMS, synonym)', 'searched for a tier column', 'FERRY_STANDING.md:']
    return all(x in r for x in need) and 'NOT FOUND' not in r


def procs_ok(S):
    p = S['procs']
    return ('ORPHANS STOPPED : 0' in line_with(p, 'ORPHANS STOPPED') and 'POSITIVE CONTROL' in p
            and 'candidates other than powershell.exe: 0' in p)


def a4_ok(S):
    a4 = [l for l in S['fs'].split(NL) if l.startswith('- **A4**')]
    ver = lambda t: next((l for l in t.split(NL) if l.startswith('VERSION:')), None)
    return (len(a4) == 1 and 'AUTHOR-RULED 2026-09-30' in a4[0] and '(R175)`(5)' in a4[0].replace('(R175)(5)', '(R175)`(5)')
            and ver(S['fs']) == ver(S['fs_prior']) and S['fs'].startswith(S['fs_prior'].rstrip(NL)[:2000]))


def capture_form(S):
    """### push_gated.sh against b564`s close: every prior line kept in order, every added line inside THE CAPTURE`s block."""
    old, new = S['pg_prior'].split(NL), S['pg'].split(NL)
    if not subseq(S['pg_prior'], S['pg']):
        return False
    added = [l for l in new if l not in set(old)]
    blk = S['pg'][S['pg'].find('# ### THE CAPTURE'):]
    blk = blk[:blk.find(NL + 'fi' + NL) + 4] if NL + 'fi' + NL in blk else ''
    return bool(added) and bool(blk) and all(l in blk for l in added) and 'PUSH_GATED_LOG' in blk


def synonym_form(S):
    """### terminal_table.py against b564`s close: the one synonym entry and its note line added. The one line removed may only be the
    ### map`s former closing entry, re-added with a comma in place of its `}` (b565 defect (o): the first form forbade that)."""
    old, new = S['tt_prior'].split(NL), S['tt_src'].split(NL)
    added = [l for l in new if l not in set(old)]
    removed = [l for l in old if l not in set(new)]
    reclosed = [r for r in removed if r.rstrip().endswith('}') and (r.rstrip()[:-1] + ',') in [a.rstrip() for a in added]]
    rest = [a for a in added if a.rstrip() not in [r.rstrip()[:-1] + ',' for r in reclosed]]
    return (removed == reclosed and len(removed) <= 1 and 1 <= len(rest) <= 2
            and any("'INTERFACES-on-false-premise': 'INTERFACES'" in l for l in rest)
            and all('INTERFACES-on-false-premise' in l for l in rest))


def row_line(S, n):
    rs = [l for l in S['corr'].split(NL) if l.startswith('| %s |' % n)]
    return rs[0] if len(rs) == 1 else ''


def supersede_row(S):
    r = row_line(S, R.ROW_SUP)
    return (bool(r) and 'SUPERSEDES row 397: INTERFACES' in r and 'tier T2' in r and '61e3551' in r
            and S['corr'].startswith(S['corr_prior'].rstrip(NL)))


def supersede_read(S):
    a, n = S['aj'], S['nj']
    cells = (a.get('term') or {}).get('regenerated', {}).get('cells', [])
    return (a.get('changed') == ['SIDE-explicit-formula|SIDEExplicitFormula.LiWeil.%s SHELL -> INTERFACES' % R.TERM]
            and n.get('changed') == [] and len(cells) == 1 and cells[0].get('grade') == 'INTERFACES')


def clones_pinned(S):
    return all(S['clones'][r].get('head', '').startswith(p) and S['heads'][r].startswith(p) and S['clones'][r].get('exit') == 0
               and os.path.normcase(S['clones'][r].get('dir', '')).startswith(os.path.normcase(AUD)) for r, p in PINS.items())


def toolchains_ok(S):
    i = S['infos']
    return ('leanprover/lean4:v4.34.0-rc1' in i['bulka'] and 'de5ce8a9' in i['bulka']
            and 'leanprover/lean4:v4.33.0-rc2' in i['arda'] and '51e6992e' in i['arda'] and 'fbdc36bb' in i['arda'])


def builds_ok(S):
    ok = True
    for r, n in (('bulka', 35), ('arda', 74)):
        b = S['builds'][r]
        good = re.findall(r'^--- \+(\S+) rc=0 ', b, re.M)
        bad = re.findall(r'^--- \+(\S+) rc=(?!0 )', b, re.M)
        ok = ok and len(set(good)) == n and not bad and S['au'].get(r, {}).get('build_exit') == 0
    return ok


def prints_ok(S):
    for r, spec in R.AUDIT.items():
        rows = S['core'].get(r, {}).get('rows', {})
        if sorted(rows) != sorted(spec['terminals']):
            return False
        if not all(v.get('axioms') is not None and set(v['axioms']) <= set(R.STD3) for v in rows.values()):
            return False
        if not all(("'%s' depends on axioms:" % n) in S['prints'][r] for n in spec['terminals']):
            return False
    return True


def statements_ok(S):
    for r, spec in R.AUDIT.items():
        txt = S['prints'][r] + NL + S['sreads'][r]
        if not all(re.search(r'^@?' + re.escape(n) + r' :', txt, re.M) for n in spec['terminals']):
            return False
    return all(t.get('statement') for r in PINS for t in S['au'].get(r, {}).get('rows', {}).values())


def provenance_ok(S):
    rows = [t for r in PINS for t in S['au'].get(r, {}).get('rows', {}).values()]
    where = S['sreads']['bulka'] + S['sreads']['arda']
    return (bool(rows) and all(t.get('zero_set') and t.get('rh') for t in rows)
            and 'WHERE RiemannHypothesis : declared in module Mathlib.' in where
            and 'WHERE riemannZeta : declared in module Mathlib.' in where
            and 'WHERE WeilExplicit.zeroMult : declared in module E6Bridge4' in where
            and 'WHERE LiChallenge.NontrivialZero : declared in module ChallengeDeps' in where)


def sorry_ok(S):
    s = S['sorry']
    tot = lambda k: (s.get(k) or {}).get('totals', {})
    closures = ('bulka_sorry_XiOrderBridge_ReverseDirection_Fidelity_RHBridge', 'bulka_sorry_Solution_ChallengeDeps',
                'arda_sorry_E6Bridge27', 'arda_sorry_zeta23')
    return (all(tot(k).get('sorry') == 0 and tot(k).get('admit') == 0 and tot(k).get('axioms') == [] for k in closures)
            and len((s.get('arda_sorry_zeta23') or {}).get('closure', {})) == 59
            and tot('arda_sorry_zeta23_control').get('sorry', 0) > 0 and tot('bulka_sorry_Challenge').get('sorry', 0) > 0)


def grades_ok(S):
    rows = [(n, t) for r in PINS for n, t in S['au'].get(r, {}).get('rows', {}).items()]
    voc = ('DERIVES', 'INTERFACES', 'ENCODES', 'SHELL', 'NOT SCORABLE')
    return (bool(rows) and all(t.get('grade') in voc and t.get('why') for n, t in rows)
            and all(t.get('needles_found') == t.get('needles_total') and t.get('needles_total') for n, t in rows)
            and all(t['grade'] != 'INTERFACES' or t.get('premise') for n, t in rows))


def compared_ok(S):
    a = S['audit']
    c = S['au'].get('comparisons', {})
    return (all(c.get(x, {}).get('word') in ('SAME', 'WEAKER', 'STRONGER', 'DIFFERENT') for x in ('arda_vs_sym', 'bulka_vs_fwd'))
            and '### THE COMPARISON: ARDA`S bl_explicit_formula AGAINST li_identity_sym' in a
            and '### THE COMPARISON: BULKA`S FORWARD DIRECTION AGAINST rh_imp_li_nonneg' in a
            and 'fbdc36bb' in a and '3635e748' in a)


def clones_outside(S):
    hits = [(c, f) for c, fs in S['corpus_tracked'].items() for f in fs if os.path.basename(f) in CLONE_NAMES or 'audit-b565' in f]
    return bool(S['corpus_tracked']['relay']) and not hits


def no_priority_text(S):
    n = S['faj'].get('line')
    F = S['find'].split(NL)
    txt = ' '.join([F[n - 1] if n else '', S['audit'], fblock(S['find'], P(R.FH5))])
    bad = re.compile(r'\b(?:we|the programme|this (?:act|kernel)) (?:is|was|are) the first\b|\bfirst formali[sz]ation\b|\bpriority\b(?! claim)(?!\.)', re.I)
    return 'No sentence here claims priority' in txt and not [m.group(0) for m in bad.finditer(txt.replace('claims priority', ''))]


def field_ok(S):
    n = S['faj'].get('line')
    F = S['find'].split(NL)
    t = F[n - 1] if n else ''
    return (bool(n) and t.startswith(P('*Appended 2026-09-30 by b565 to the field entry')) and R.AUDIT['bulka']['url'] in t
            and R.AUDIT['arda']['url'] in t and '35df682f' in t and 'acfb0ee5' in t and 'fbdc36bb' in t and '2026-09-30' in t
            and S['find'].count(P('*Appended 2026-09-30 by b565 to the field entry')) == 1)


def ot_once_at(S, head, line):
    ot = rd8(S['pp_now']['OPEN_TRAILS.md']).split(NL)
    ln = [i + 1 for i, l in enumerate(ot) if l.startswith(P(head))]
    return ln == [line] and bool(line)


def conditional_ok(S):
    n = S['cj'].get('line')
    ot = S['ot'].split(NL)
    t = ot[n - 1] if n else ''
    return (ot_once_at(S, R.WO5, n) and '(i)' in t and '(ii)' in t and 'T0-vendored' in t and 'T1-lit' in t
            and '(V1)-(V4)' in t and 'fbdc36bb' in t and '3635e748' in t)


def findings_ok(S):
    F = S['find'].split(NL)
    b = fblock(S['find'], P(R.FH5))
    n = S['fj'].get('heading_line', 0)
    return (S['find'].count(P(R.FH5)) == 1 and bool(n) and F[n - 1] == P(R.FH5) and 'b566' in b and 'GRH-Weil act three' in b
            and kept(S, 'FINDINGS.md'))


def corr_ok(S):
    a = row_line(S, R.ROW_AUD)
    return (bool(a) and bool(row_line(S, R.ROW_SUP)) and '35df682f' in a and 'acfb0ee5' in a and S['rows'].get('exit_act') == 0
            and S['corr'].startswith(S['corr_prior'].rstrip(NL)))


def trail_ok(S):
    return ot_once_at(S, R.HEADING5, S['tj'].get('line')) and '**Entered:**' in trail(S) and '**(R175) ratified' in trail(S)


def techne_ok(S):
    names = S['priv_names']
    hits = [(n, f) for n in names for f, t in S['act_blobs'].items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b564 (was ') == 4
            and b.count('Deleted branch push-b564-closing (was ') == 1)


def held_kept(S):
    k = S['k']
    return all(k['kept'][b].startswith(t) and k['remote'].get('refs/heads/' + b, '').startswith(t) for b, t in R.KEPT5.items())


def mains_ok(S):
    m = S['k']['mains']
    return (len(m) == len(R.PRE_HEADS5) and all(v == [] for k2, v in m.items() if k2 != 'SIDE-global-section')
            and set(m.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'} and S['k']['main'].startswith(R.V08))


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == S['recomputed'][k]


def hword(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 16).split('.')[0]


VACUOUS_ARMS = ()


def _nscore_arm(k, reads):
    return ('G-%s-SCORED' % k.upper(), reads, lambda S: nscored(S, k), lambda S: put(S, 'sc', dict(S['sc'], **{k: not S['sc'].get(k)})))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R175) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b565' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b564`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b564' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b565' in S['ferry'] and 'ACT b565' in S['face'] and not glob.glob(os.path.join(D, 'b566_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b565')),
    ('G-PEEK-DECLARED', 'the face`s (C) block; before the push file times, after it content digests against the pushed tree',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in flat(S['face']) and 'THE SEAT FORMED ITS READINGS BEFORE THIS SEAL' in flat(S['face'])
                and S['after_lock'] and S['before_lock']),
     lambda S: put(S, 'after_lock', False)),
    ('G-R175-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R175) END' in S['ferry'] and S['ot'].count('**(R175) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R175) ratified', '(R175) noted'))),
    ('G-READS-CITED', 'the reads bank -- the prior-art record, b536`s form, the vendoring record, :6136, rows 395 and 397, the table`s maps',
     lambda S: reads_ok(S), lambda S: put(S, 'reads', S['reads'].replace('CORRESPONDENCE row 397 :', 'x'))),
    ('G-PUSHOUT-COMMITTED', 'relay commit 80346ab6 READ HERE -- b564`s push output alone, in HEAD`s ancestry',
     lambda S: S['commits'][C_PUSHOUT]['files'] == ['data/b564_relay_push_out.txt'] and S['commits'][C_PUSHOUT]['anc'],
     lambda S: put(S, 'commits', dict(S['commits'], **{C_PUSHOUT: dict(S['commits'][C_PUSHOUT], files=['data/b564_relay_push_out.txt', 'x'])}))),
    ('G-STANDING-A4', 'tools/FERRY_STANDING.md READ HERE against b564`s close -- clause A4 once, author-ruled, the VERSION line unmoved',
     lambda S: a4_ok(S), lambda S: put(S, 'fs', S['fs'].replace('- **A4**', '- **A5**'))),
    ('G-CAPTURE-FORM', 'tools/push_gated.sh READ HERE against b564`s close -- the capture added, nothing else moved',
     lambda S: capture_form(S), lambda S: put(S, 'pg', S['pg'].replace('set -euo pipefail', 'set -eu'))),
    ('G-CAPTURE-COMMIT-ALONE', 'relay commit 9de84b16`s file list READ HERE, and the capture test bank',
     lambda S: (S['commits'][C_CAPTURE]['files'] == ['tools/push_gated.sh'] and S['commits'][C_CAPTURE]['anc']
                and 'CAPTURE TEST : PASS' in line_with(S['cap'], 'CAPTURE TEST :') and "the hook's marker lines in the log 1" in S['cap']),
     lambda S: put(S, 'commits', dict(S['commits'], **{C_CAPTURE: dict(S['commits'][C_CAPTURE], files=['tools/push_gated.sh', 'tools/x.py'])}))),
    ('G-SUITE-README', 'tools/SUITE_README.md READ HERE -- the glob rule, the placeholder, globs_of',
     lambda S: all(x in S['sreadme'] for x in ('placeholder', 'globs_of', '(W)')) and '`*`' in S['sreadme'],
     lambda S: put(S, 'sreadme', '')),
    ('G-SYNONYM-FORM', 'tools/terminal_table.py READ HERE against b564`s close -- the one entry and its note, nothing removed',
     lambda S: synonym_form(S), lambda S: put(S, 'tt_src', S['tt_src'].replace("'INTERFACES-on-false-premise': 'INTERFACES'", "'X': 'Y'"))),
    ('G-SYNONYM-COMMIT-ALONE', 'relay commit 7a2defb1`s file list READ HERE, and its quoted test',
     lambda S: S['commits'][C_SYNONYM]['files'] == ['tools/terminal_table.py'] and S['commits'][C_SYNONYM]['anc'] and 'PASS' in S['syn'],
     lambda S: put(S, 'commits', dict(S['commits'], **{C_SYNONYM: dict(S['commits'][C_SYNONYM], anc=False)}))),
    ('G-SYNONYM-UNIT', 'the synonym unit bank -- both polarities, the three old entries unchanged',
     lambda S: ('FIXTURES 7 ; AGREEING 7 : PASS' in line_with(S['syn'], '**FIXTURES') and S['syn'].count(' AGREES') == 7
                and "'INTERFACES-on-false-premise'      -> 'INTERFACES' AGREES" in S['syn']),
     lambda S: put(S, 'syn', S['syn'].replace('AGREEING 7 : PASS', 'AGREEING 6 : FAIL'))),
    ('G-SUPERSEDE-ROW', 'CORRESPONDENCE READ HERE -- row 401 once, its cell INTERFACES with the tier in words, the ledger a true prefix extended',
     lambda S: supersede_row(S), lambda S: put(S, 'corr', S['corr'].replace('SUPERSEDES row 397: INTERFACES', 'SUPERSEDES row 397: SHELL'))),
    ('G-SUPERSEDE-READ', 'the supersede banks -- the entry alone moves nothing; after the row li_identity_of_exchange SHELL -> INTERFACES alone',
     lambda S: supersede_read(S), lambda S: put(S, 'nj', dict(S['nj'], changed=['x']))),
    ('G-CONFLICT-PRINTED', 'the before and after banks -- CONFLICT printed both ways, the terminals changed printed',
     lambda S: 'CONFLICT committed 12 -> regenerated 12' in S['noop'] and 'CONFLICT committed 12 -> regenerated 12' in S['after']
     and 'TERMINALS WHOSE GRADE CHANGED' in S['after'],
     lambda S: put(S, 'after', S['after'].replace('regenerated 12', 'regenerated 13'))),
    ('G-CLONES-PINNED', 'the clone banks and the clones` HEADs READ HERE -- 35df682f and acfb0ee5, under D:/audit-b565',
     lambda S: clones_pinned(S), lambda S: put(S, 'heads', dict(S['heads'], arda='0' * 40))),
    ('G-TOOLCHAINS-PRINTED', 'the info banks -- each toolchain and Mathlib rev, Zeta23`s pin',
     lambda S: toolchains_ok(S), lambda S: put(S, 'infos', dict(S['infos'], arda=S['infos']['arda'].replace('fbdc36bb', 'x')))),
    ('G-BUILDS-PRINTED', 'the build logs -- every module one call, rc 0, 35 and 74; the audit json`s build exits',
     lambda S: builds_ok(S), lambda S: put(S, 'builds', dict(S['builds'], arda=S['builds']['arda'] + NL + '--- +E6Bridge27 rc=1 secs=1'))),
    ('G-AUDIT-PRINTS', 'the print banks and the core json -- every audited terminal printed at the standard three',
     lambda S: prints_ok(S), lambda S: put(S, 'prints', dict(S['prints'], bulka=S['prints']['bulka'].replace("'li_criterion' depends", "'x' depends")))),
    ('G-AUDIT-STATEMENTS', 'the print and read banks -- every audited terminal`s statement printed, and banked in the audit json',
     lambda S: statements_ok(S), lambda S: put(S, 'au', dict(S['au'], arda=dict(S['au'].get('arda', {}), rows={'x': dict(statement='')})))),
    ('G-AUDIT-PROVENANCE', 'the read banks` WHERE lines and the audit json -- each zero set and each RH read to its declaring module',
     lambda S: provenance_ok(S), lambda S: put(S, 'sreads', dict(S['sreads'], arda=S['sreads']['arda'].replace('declared in module E6Bridge4', 'x')))),
    ('G-AUDIT-SORRY', 'the sorry banks -- every closure 0, Zeta23`s 59 modules read, both controls firing',
     lambda S: sorry_ok(S), lambda S: put(S, 'sorry', dict(S['sorry'], arda_sorry_zeta23_control=dict(totals=dict(sorry=0))))),
    ('G-AUDIT-GRADES', 'the audit json -- every terminal graded in the vocabulary with its clause, every needle of its reading found',
     lambda S: grades_ok(S), lambda S: put(S, 'au', dict(S['au'], bulka=dict(S['au'].get('bulka', {}), rows=dict((S['au'].get('bulka') or {}).get('rows', {}), x=dict(grade='GENUINE', why='x')))))),
    ('G-AUDIT-COMPARED', 'the audit bank and json -- two comparison paragraphs, each with its word, the Zeta23 pins named',
     lambda S: compared_ok(S), lambda S: put(S, 'audit', S['audit'].replace('3635e748', 'x'))),
    ('G-CLONES-OUTSIDE-CORPUS', 'every repository of the corpus`s tracked files READ HERE -- no file of either clone',
     lambda S: clones_outside(S), lambda S: put(S, 'corpus_tracked', dict(S['corpus_tracked'], relay=S['corpus_tracked']['relay'] + ['vendor/E6Bridge27.lean']))),
    ('G-FIELD-LINE', 'FINDINGS READ HERE -- the field line once at its banked line, URLs, pins and dates',
     lambda S: field_ok(S), lambda S: put(S, 'faj', dict(S['faj'], line=1))),
    ('G-NO-PRIORITY-SENTENCE', 'the field line, the audit bank and the entry -- the no-priority sentence present, no priority claimed',
     lambda S: no_priority_text(S), lambda S: put(S, 'audit', S['audit'] + ' this kernel is the first to prove it.')),
    ('G-CEILING-UNTOUCHED', 'README.md and REGISTRY.md READ HERE against b564`s PLACE-papers tip',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b'x'}))),
    ('G-CONDITIONAL-ENTERED', 'OPEN_TRAILS READ HERE -- the (R175)(3) conditional once at its banked line, both branches, the pins',
     lambda S: conditional_ok(S), lambda S: put(S, 'cj', dict(S['cj'], line=1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS READ HERE -- the entry once at its banked line, b566 named, the file kept',
     lambda S: findings_ok(S), lambda S: put(S, 'find', S['find'].replace(P(R.FH5), 'x'))),
    ('G-CORR-ROWS', 'CORRESPONDENCE READ HERE -- rows 401 and 402 once each, the ledger a true prefix extended',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('| 402 |', '| 403 |'))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS READ HERE -- this act`s record once at its banked line',
     lambda S: trail_ok(S), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-BRANCHES-DELETED', 'the branch lists READ HERE in four repositories, and the banked command output',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{ROOT: '  push-b564'}))),
    ('G-TRIAL-UNTOUCHED', 'the trial worktree READ HERE -- HEAD f22ff35, tracked tree clean',
     lambda S: S['trial']['head'].startswith('f22ff35') and S['trial']['status'] == '',
     lambda S: put(S, 'trial', dict(S['trial'], status=' M lean-toolchain'))),
    ('G-HELD-BRANCH-KEPT', 'the kernel`s refs READ HERE -- the five kept branches at their tips local and remote',
     lambda S: held_kept(S), lambda S: put(S, 'k', dict(S['k'], kept=dict(S['k']['kept'], **{'grh-weil-b562': '0' * 40})))),
    ('G-LINES-KEPT', 'FINDINGS and OPEN_TRAILS against their blobs at b564`s commit -- true prefixes',
     lambda S: all(kept(S, f) for f in FIXED),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'OPEN_TRAILS.md': S['pp_now']['OPEN_TRAILS.md'][:200] + S['pp_now']['OPEN_TRAILS.md'][260:]}))),
    ('G-MONOGRAPH-UNTOUCHED', 'the live and deposited monograph against their blobs',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'day1/A_Place_to_Stand.md': b'x'}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-KERNEL-MAINS-UNTOUCHED', 'every kernel`s main READ HERE against its pre-act head -- SIDE-global-section`s ledger rows alone',
     lambda S: mains_ok(S), lambda S: put(S, 'k', dict(S['k'], mains=dict(S['k']['mains'], **{'SIDE-kernel': ['Kernel/X.lean']})))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b565_x.py'])),
    ('G-DELETE-FREE', 'this act`s own Python tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b565_x.py', 'x')])),
    ('G-TECHNE-SHAPE-ONLY', 'every b565 bank and tool (the clones` own output excepted) and this act`s ledger bytes, against TECHNE-Core`s private names READ HERE',
     lambda S: techne_ok(S), lambda S: put(S, 'act_blobs', dict(S['act_blobs'], planted=' '.join(S['priv_names'][:1])))),
    _nscore_arm('n1', 'the desk against the audit json (H17a)'),
    _nscore_arm('n2', 'the desk against the audit json (H17b)'),
    _nscore_arm('n3', 'the desk against the comparison of the forward directions'),
    _nscore_arm('n4', 'the desk against the build logs'),
    _nscore_arm('n5', 'the desk against the supersede banks and row 401`s own cell'),
    _nscore_arm('n6', 'the desk against the kernel mains, the deposit and the kept branches'),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2') and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-H17-SCORED', 'the desk against the audit json -- H17a and H17b, each word from the banks',
     lambda S: all(hword(S, x) == word_of(S['sc'][x.lower()]) and S['sc'][x.lower()] == S['recomputed'][x.lower()] for x in ('H17a', 'H17b')),
     lambda S: put(S, 'sc', dict(S['sc'], h17b=not S['sc'].get('h17b')))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b565 -'))),
    ('G-PRIORBANK-UNCHANGED', 'before the push file times against the face; after it content digests against the pre-act tip and the pushed tree, no exception',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the two written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED), lambda S: put(S, 'tracked', list(S['tracked']) + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING5)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING5) + ' a second record')),
    ('G-WRITELIST-KINDS', 'every b565 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b565')" in S['suite']
                and "data/b565_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b565_components.txt' in gits(ROOT, 'show'")),
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
    tl = [l for l in S['table'].split(NL) if '`SIDEExplicitFormula.LiWeil.li_identity_of_exchange` |' in l]
    rec('  ### the regenerated table`s line for li_identity_of_exchange: %s' % (tl[0][:220] if len(tl) == 1 else 'lines found %d' % len(tl)))
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    names = [a[0] for a in ARMS]
    pushed = S['pushed']
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b565 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    out = os.path.join(D, 'b565_checks_postpush.txt' if pushed else 'b565_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective, neg_failures=negfail,
                   declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b565_exercise.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
