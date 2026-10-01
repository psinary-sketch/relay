# -*- coding: utf-8 -*-
"""b567_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b566's AND WRITTEN ARM BY ARM FOR b567's FACE (G2).

### ### b567: GRH-WEIL ACT THREE; THE CEILING AMENDED; THE ADDENDUM FORMS; THE FORWARD MOVE'S CONSEQUENCES; THE RESIDUE
### PREMISE, UNDER (R177). The harness and the generic helpers are b564's and b566's (imported, never copied); the act's arms
### and sources() are written for this face. The (W) reader is b564's `globs_of`.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated source and require it to
### fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.** ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE.**
### ### THE (G2) BLOCK IS READ AS b566 READ IT, WITH ONE READING DECLARED HERE: a token written "`G-X`-kind" names a KIND of
### arm and is not a declaration (the face: "`G-PEEK`-kind reads are not armed separately"); it is printed, not run.
### ### `G-PRIORBANK-UNCHANGED` and `G-WRITELIST-KINDS` read file times before the push and content digests against the pushed
### tree after it ((R169)(1)(b), (R170)(3)); the two prior banks (R177) orders a line appended to are read as prefix + one line.
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
import b567_record as R
import b542_checks as K542
import addenda as ADD

D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
BULKA = os.path.join('D:', os.sep, 'audit-b565', 'bulka')
FACE = os.path.join(D, 'b567_registration_2026-10-01.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
RESREL = 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'
PRIOR_RELAY, PRIOR_PP, PRIOR_GS = R.PRIOR_RELAY, R.PRIOR_PP, R.PRIOR_GS
NL = chr(10)
L, RES, EX = [], [], []

read, git, gits, cut, put, blob, flat, rd8, jload = K4.read, K4.git, K4.gits, K4.cut, K4.put, K4.blob, K4.flat, K4.rd8, K4.jload
utc_epoch, cr0, blob_id, tree_ids, strip_prose = K4.utc_epoch, K4.cr0, K4.blob_id, K4.tree_ids, K4.strip_prose
seg, fblock, subseq, delete_needles, globs_of, live_limb_guard = K4.seg, K4.fblock, K4.subseq, K4.delete_needles, K4.globs_of, K4.live_limb_guard

FIXED = ['FINDINGS.md', 'OPEN_TRAILS.md']
CEIL = ['README.md', 'REGISTRY.md']
OTHER = ['ERRATA.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md', 'phase2/method/THE_KEYSTONE_CENSUS.md',
         'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md']
APPENDED = {'b566_step1_license.txt': '(R177)(3)(h)', 'b551_toolchains.txt': '(R177)(4)'}
OTHER_KERNELS = ['SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle', 'SIDE-compression',
                 'SIDE-structural-error-correction', 'SIDE-cosmo']
C_PUSHOUT = '401bb062'
C_G, C_H = '0e50bd19', '90373807'
FILES_G = ['data/b566_writelist_addendum.txt', 'data/b567_test_writelist.txt', 'tools/addenda.py', 'tools/b566_checks.py',
           'tools/test_addenda_writelist.py']
FILES_H = ['data/b566_step1_license.txt', 'data/b567_test_licence.txt', 'tools/addenda.py', 'tools/b566_checks.py',
           'tools/test_addenda_licence.py']
RERUN = '--rerun-postpush' in sys.argv
TRIAL = '--trial' in sys.argv   # ### a seat's trial run: no table regeneration, its record written to the path given, never to data/


def rec(s=''):
    L.append(s)
    print(s)


def line_with(text, needle):
    """### **A2.** ### The FIRST LINE of a TEXT carrying the needle -- never the whole text."""
    for ln in (text or '').split(NL):
        if needle in ln:
            return ln
    return ''


def is_pushed():
    return (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
            and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b567')
            and 'data/b567_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def act_commit(repo, rev='HEAD', n=60):
    out = []
    for l in gits(repo, 'log', '--pretty=%H %s', '-%d' % n, rev).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            if s.startswith('b567 --') or (s.startswith('housekeeping:') and ('(R177)' in s or 'b567' in s)):
                out.append(h)
    return out


def files_of(repo, sha):
    return sorted(x for x in gits(repo, 'show', '--name-only', '--pretty=format:', sha).split(NL) if x.strip())


def written_by_digest(repo, rel):
    p = os.path.join(repo, rel)
    work = cr0(open(p, 'rb').read()) if os.path.isfile(p) else b''
    pub = cr0(blob(repo, 'origin/main:' + rel.replace(os.sep, '/')))
    return pub is None or hashlib.sha256(work).hexdigest() != hashlib.sha256(pub).hexdigest()


def appended_one_line(name):
    """### a prior bank (R177) orders ONE line appended to: its pre-act blob a true prefix of its bytes now, plus one line."""
    pre = cr0(blob(ROOT, PRIOR_RELAY + ':data/' + name) or b'')
    now = cr0(open(os.path.join(D, name), 'rb').read())
    extra = now[len(pre):]
    return bool(pre) and now.startswith(pre) and extra.count(b'\n') == 1 and extra.endswith(b'\n')


# ### ### **(R178)(2)(ii), b568: THE AS-OF COMMIT.** A sealed face is a statement about the tree at its closing push. When
# ### `data/b567_closing_push_out.txt` names a relay tip read back equal at the remote, the TREE-READING arm of this suite --
# ### G-PRIORBANK-UNCHANGED, the one that lists and compares the relay data tree -- reads the tree at that commit, not at
# ### HEAD (the two ordered appends read there too, each its pre-act blob a true prefix plus one line). With no such bank
# ### -- the act's own closing run -- it reads live, as before. `--as-of <sha>` points it at another commit (relay
# ### tools/test_asof.py). Arms reading a named bank's content are not re-pointed.
import asof as AF   # noqa: E402
AS_OF = AF.from_argv(sys.argv, AF.relay_asof(ROOT, D, 'b567'))
PRIOR_RX = r'^b4[0-9][0-9]_|^b5[0-5][0-9]_|^b56[0-6]_|^b334_'


def prior_check_asof():
    pre, at = tree_ids(ROOT, PRIOR_RELAY, 'data'), AF.ids_at(ROOT, AS_OF, 'data')
    bad, n_pre, n_new, n_app, n = [], 0, 0, 0, 0
    for k, i in sorted(at.items()):
        f = k[len('data/'):]
        if not re.match(PRIOR_RX, f):
            continue
        n += 1
        if f in APPENDED:
            n_app += 1
            p0, p1 = cr0(AF.blob_at(ROOT, PRIOR_RELAY, k) or b''), cr0(AF.blob_at(ROOT, AS_OF, k) or b'')
            extra = p1[len(p0):]
            if not (p0 and p1.startswith(p0) and extra.count(b'\n') == 1 and extra.endswith(b'\n')):
                bad.append(f)
        elif k in pre:
            n_pre += 1
            if pre[k] != i:
                bad.append(f)
        else:
            n_new += 1
    return dict(ok=not bad, checked=n, pre=n_pre, pub=n_new, time=0, app=n_app, bad=bad, asof=AS_OF)


def prior_check(pushed):
    if AS_OF:
        return prior_check_asof()
    """### every prior bank unchanged: after the push by digest against the pre-act tip and the pushed tree; before it by file
    ### time against the face. The two ordered appends are read by `appended_one_line`, by name, and by nothing looser."""
    files = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b5[0-5][0-9]_|^b56[0-6]_|^b334_', f)]
    exp = []
    for f in files:
        if os.path.isdir(os.path.join(D, f)):
            exp += sorted(f + '/' + x for x in os.listdir(os.path.join(D, f)) if os.path.isfile(os.path.join(D, f, x)))
        else:
            exp.append(f)
    bad, n_pre, n_pub, n_time, n_app = [], 0, 0, 0, 0
    pre_ids, pub_ids = tree_ids(ROOT, PRIOR_RELAY, 'data'), tree_ids(ROOT, 'origin/main', 'data')
    for f in exp:
        if f in APPENDED:
            n_app += 1
            if not appended_one_line(f):
                bad.append(f)
            continue
        k = 'data/' + f
        raw = open(os.path.join(D, f), 'rb').read()
        ids = {blob_id(raw), blob_id(cr0(raw))}
        if pushed and k in pre_ids:
            n_pre += 1
            if pre_ids[k] not in ids or pub_ids.get(k) not in ids:
                bad.append(f)
        elif pushed and k in pub_ids:
            n_pub += 1
            if pub_ids[k] not in ids:
                bad.append(f)
        elif k in pre_ids:
            n_pre += 1
            if pre_ids[k] not in ids:
                bad.append(f)
        else:
            n_time += 1
            if not os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE):
                bad.append(f)
    return dict(ok=not bad, checked=len(exp), pre=n_pre, pub=n_pub, time=n_time, app=n_app, bad=bad)


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    rd_d = lambda n: read(os.path.join(D, n))
    locks = sorted(glob.glob(os.path.join(D, 'b567_lockgate_notes*.txt')))
    k = R.kstate7()
    S = dict(
        face=read(FACE), ferry=rd_d('b567_ferry.txt'), scan=rd_d('b567_ferry_scan.txt'),
        cens=rd_d('b567_census_stepzero.txt'), fcens=rd_d('b567_faces_census_stepzero.txt'), pins=rd_d('b567_pins_stepzero.txt'),
        procs=rd_d('b567_procs_stepzero.txt'), lock=read(locks[-1]) if locks else '',
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=rd_d('b566_closing.txt'), desk=rd_d('b567_desk_notes.txt'), defects=rd_d('b567_defects.txt'),
        sc=jload('b567_scores.json'), reads=rd_d('b567_reads.txt'),
        pushout=dict(files=files_of(ROOT, C_PUSHOUT),
                     anc=subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', C_PUSHOUT, 'HEAD']).returncode == 0),
        wj=jload('b567_weight.json'), cj=jload('b567_ceiling.json'), fj=jload('b567_field.json'), sj=jload('b567_s7.json'),
        rl=jload('b567_residue_line.json'), t2=jload('b567_trails2.json'), rv=jload('b567_census_revs.json'),
        dj=jload('b567_deprecations.json'), deps=rd_d('b567_deprecations.txt'), cache=rd_d('b567_cache.txt'),
        nobuild=rd_d('b567_cache_nobuild.txt'), bv=jload('b567_bulka_verify.json'), bdel=rd_d('b567_bulka_delete.txt'),
        bulka_exists=os.path.exists(BULKA),
        ck_mathlib=gits(os.path.join(KER, '.lake', 'packages', 'mathlib'), 'rev-parse', 'HEAD'),
        fwd_lake=os.path.exists(os.path.join('D:', os.sep, 'b566-forward', '.lake')),
        aside=os.path.isdir(os.path.join('D:', os.sep, 'b567-lake-51e6992e')),
        rstmt=rd_d('b567_residue_statement.txt'), rbuild=rd_d('b567_residue_build.txt'), e3=jload('b567_e0_residue.json'),
        e4=jload('b567_e0_chi.json'), cbuild=rd_d('b567_chi_build.txt'), zbj=jload('b567_zb_consumers.json'),
        rowgen=rd_d('b567_rowgen.txt'), kpush=rd_d('b567_kernel_push_out.txt'), branches=rd_d('b567_branches.txt'),
        fnd=jload('b567_findings.json'), tr=jload('b567_trail.json'), rows=jload('b567_rows.json'),
        rr_before=rd_d('b567_b566_rerun_before.txt'), rr_after=rd_d('b567_b566_rerun_after.txt'), rr_read=rd_d('b567_b566_rerun_reading.txt'),
        tw=rd_d('b567_test_writelist.txt'), tl=rd_d('b567_test_licence.txt'), addb=rd_d('b566_writelist_addendum.txt'),
        lic=rd_d('b566_step1_license.txt'), lic_main=blob(KER, 'main:Vendored/Bulka/LICENSE') or b'',
        census=rd_d('b551_toolchains.txt'),
        files_g=files_of(ROOT, C_G), files_h=files_of(ROOT, C_H),
        k=k, lean_ns=[x for x in gits(KER, 'diff', '--name-status', R.V09, 'origin/main', '--').split(NL) if x.strip()],
        stmt=K4.rd8(blob(KER, 'origin/main:SIDEExplicitFormula/Chi/Statement.lean')),
        stmt_sha_main=hashlib.sha256(blob(KER, 'origin/main:SIDEExplicitFormula/ResidueDischarge.lean') or b'').hexdigest(),
        corr=read(R.CORR), corr_prior=rd8(blob(SIDE, PRIOR_GS + ':CORRESPONDENCE.md')),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in FIXED + CEIL + OTHER + [RESREL]},
        pp_now={f: open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n') for f in FIXED + CEIL + OTHER + [RESREL]},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), readme=read(os.path.join(PP, 'README.md')),
        registry=read(os.path.join(PP, 'REGISTRY.md')), resid=read(os.path.join(PP, RESREL)),
        branch_lists={r: gits(r, 'branch', '--list', 'push-b566*') for r in (ROOT, PP, SIDE, KER)},
        b566_remote=jload('b566_scores.json').get('kstate', {}).get('remote', {}),
        others={n: (gits(os.path.join('D:', os.sep, n), 'rev-parse', 'main'),
                    (gits(os.path.join('D:', os.sep, n), 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]) for n in OTHER_KERNELS},
        b566_mains={m.group(1): m.group(2) for m in re.finditer(r'^\s+(\S+)\s+main (\w{12}) ; remote', read(os.path.join(D, 'b566_closing.txt')), re.M)},
        gs_files=sorted(set(f for h in act_commit(SIDE) for f in files_of(SIDE, h))),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0)
                 if f.startswith('b567_') and os.path.isfile(os.path.join(d0, f))) if tok else -1),
        zen=[f for f in os.listdir(T) if (f.startswith('b567_') or f in ('addenda.py', 'test_addenda_writelist.py', 'test_addenda_licence.py'))
             and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if (f.startswith('b567_') or f in ('addenda.py', 'test_addenda_writelist.py',
                                                                                          'test_addenda_licence.py')) and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b567_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b567 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        mustfail=not os.path.exists(os.path.join(D, 'b567_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        relay_commit_time={h: int(gits(ROOT, 'log', '-1', '--format=%ct', h) or 0) for h in (C_G, C_H)},
    )
    S['pushed'] = RERUN or is_pushed()
    kk = set(os.path.basename(x) for x in S['tracked'])
    for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'main'), (KER, 'residue-discharge-b567')):
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
    S['prior_res'] = prior_check(S['pushed'])
    S['priv_names'] = K542.techne_private_names()
    return S


# ================================================================================ this act's arm helpers
P = R.poss


def fline(S, n):
    F = S['find'].split(NL)
    return F[n - 1] if n and n <= len(F) else ''


def trail(S):
    return flat(seg(S['ot'], P(R.HEADING7), 99999))


def scored(S, k):
    v = (S['sc'].get(k) or '')
    return v.split(' --')[0] in ('HELD', 'REFUTED') and ('**(%s)** ### **%s.**' % (k.upper(), v.split(' --')[0])) in S['desk']


def ceiling_ok(S):
    s = S['cj'].get('sentence') or ''
    f = ' '.join(S['ferry'].split())
    ok = bool(s) and ('"%s"' % s) in f
    for name in CEIL:
        old, new = rd8(S['pp_prior'][name]).split(NL), rd8(S['pp_now'][name]).split(NL)
        added = [l for l in new if l not in set(old)]
        ok = ok and subseq(rd8(S['pp_prior'][name]), rd8(S['pp_now'][name])) and len(added) == 1 and s in added[0]
        ok = ok and new[S['cj']['files'][name]['new_line'] - 1] == added[0] and '(R176)' in new[S['cj']['files'][name]['new_line'] - 3]
    return ok and s in fline(S, S['cj'].get('findings_line'))


def not_supp(S):
    want = '*RH proved*; *h2_sign proved*; *λ_n ≥ 0 proved*'
    return all(want in rd8(S['pp_now'][n]).split(NL)[S['cj']['files'][n]['new_line'] - 1] for n in CEIL) and want in fline(S, S['cj'].get('findings_line'))


def census_ok(S):
    pre = rd8(blob(ROOT, PRIOR_RELAY + ':data/b551_toolchains.txt') or b'')
    now = S['census'].replace('\r\n', NL)
    extra = now[len(pre):].strip(NL).split(NL)
    return (now.startswith(pre) and bool(pre) and len(extra) == 1 and extra[0].startswith(R.CENSUS7_H)
            and 'de5ce8a9a66a' in extra[0] and 'RECOMPUTED AT HEAD : %d' % S['rv']['count'] in extra[0])


def cache_ok(S):
    return ('rc=0' in line_with(S['cache'].split('retried from cwd')[-1], 'rc=') and S['ck_mathlib'].startswith('de5ce8a9')
            and not S['fwd_lake'] and S['aside'] and 'BulkaVendored -> ' in S['nobuild'] and 'All targets up-to-date (3721 jobs)' in S['nobuild']
            and 'build Mathlib -> ' in S['nobuild'] and 'All targets up-to-date (8706 jobs)' in S['nobuild']
            and 'CONTROL lake --no-build build +SIDEExplicitFormula.ResidueDischarge' in S['nobuild'] and '-> rc=3' in S['nobuild'])


def bulka_deleted(S):
    st = re.search(r'^START (\S+Z)', S['bdel'], re.M)
    return (not S['bulka_exists'] and 'D:/audit-b565/bulka ABSENT' in S['bdel'] and re.search(r'^END \S+Z rc=0$', S['bdel'], re.M) is not None
            and bool(st) and S['bv'].get('verified') is True)


def rerun_counted(S):
    a = S['rr_after']
    return ('ARMS RUN : 74. ### LIVE PASSING : 72.' in a and "LIVE FAILING : 2 ['G-NUMBER-UNCLAIMED', 'G-PEEK-DECLARED']" in a
            and 'G-NUMBER-UNCLAIMED' in S['rr_read'] and 'G-PEEK-DECLARED' in S['rr_read']
            and "LIVE FAILING : 2 ['G-LICENCE-PRINTED', 'G-WRITELIST-KINDS']" in S['rr_before']
            and re.search(r'^START (\S+Z)', S['bdel'], re.M) is not None)


def residue_first(S):
    t0 = re.search(r'### at (\S+Z), branch residue-discharge-b567', S['rstmt'])
    b0 = re.search(r'^=== (\S+Z) \+SIDEExplicitFormula\.ResidueDischarge', S['rbuild'], re.M)
    sha = re.search(r'sha256 ([0-9a-f]{64}), no build', S['rstmt'])
    return bool(t0) and bool(b0) and t0.group(1) < b0.group(1) and bool(sha) and sha.group(1) == S['stmt_sha_main']


def residue_row(S):
    old, new = rd8(S['pp_prior'][RESREL]), rd8(S['pp_now'][RESREL])
    add = new[len(old):]
    return (new.startswith(old) and add.count(P(R.RES7_H)) == 1 and 'register4_positivity_liCoeff_imp_rh' in add
            and 'is NOT discharged' in add and add.strip(NL).count(NL) == 0)


def chi_banked(S):
    c = S['cbuild']
    return (all(('=== attempt %d at ' % i) in c for i in range(1, 6)) and '=== Chi/Statement.lean attempt 1' in c
            and re.search(r'^--- \+SIDEExplicitFormula\.Chi\.ZetaBoundsStrip rc=0', c, re.M) is not None
            and re.search(r'^--- \+SIDEExplicitFormula\.Chi\.Statement rc=0', c, re.M) is not None)


def ef_stated(S):
    t = S['stmt']
    return ('def EF_lit_chi' in t and 'theorem EF_lit_chi' not in t and 'archTerm_chi χ k - primeSum_chi χ k' in t
            and 'theorem gammaBracket_chi_of_even' in t and 'theorem gammaBracket_chi_of_not_even' in t and 'sorry' not in t)


def tag_ok(S):
    k = S['k']
    kp = S['kpush']
    i_rb, i_tag = kp.find('main read back at the remote: %s' % k['main']), kp.find('[new tag]         v0.10 -> v0.10')
    return (bool(k['main']) and k['v010'] == k['main'] == k['local_main'] and bool(k['v010obj']) and 0 <= i_rb < i_tag
            and 'tag v0.10 peeled local %s remote %s' % (k['main'], k['main']) in kp)


def kernel_kept(S):
    ns = S['lean_ns']
    return bool(ns) and all(not (x.startswith(('M', 'D', 'R')) and x.endswith('.lean')) for x in ns)


def corr_ok(S):
    rows = S['rows'].get('rows', [])
    new = S['corr'].split(NL)
    return (S['corr'].startswith(S['corr_prior']) and len(rows) == 6 and all(r['exit'] == 0 for r in rows)
            and all(sum(1 for l in new if l.startswith('| %s |' % n)) == 1 for n in (R.ROW_ACT7,) + R.ROW_T7))


def branches_ok(S):
    b = S['branches']
    return (all(v == '' for v in S['branch_lists'].values()) and b.count('Deleted branch push-b566 (was ') == 4
            and b.count('Deleted branch push-b566-closing (was ') == 1)


def kept_ok(S):
    k, pr = S['k']['kept'], S['b566_remote']
    return bool(k) and all(v and v == pr.get('refs/heads/' + b) for b, v in k.items())


def others_ok(S):
    o, m = S['others'], S['b566_mains']
    return (all(loc and loc == rem and m.get(n, '') and loc.startswith(m[n]) for n, (loc, rem) in o.items())
            and set(S['gs_files']) <= {'CORRESPONDENCE.md'})


def techne_ok(S):
    names = S['priv_names']
    blobs = {}
    for f in os.listdir(D):
        if f.startswith('b567_') and os.path.isfile(os.path.join(D, f)):
            blobs[f] = read(os.path.join(D, f))
    hits = [(n, f) for n in names for f, t in blobs.items() if re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', t)]
    return bool(names) and not hits


def ranahead(S):
    f = S['face']
    lk = utc_epoch(f, 'locked at')
    return ('### (0) WHAT RAN AHEAD OF THIS SEAL, DECLARED.' in f and all(x in f for x in ('`relay/tools/addenda.py`',
            '`relay/tools/test_addenda_writelist.py`', '`relay/data/b566_writelist_addendum.txt`', 'G-WRITELIST-KINDS'))
            and lk is not None and all(t > lk for t in S['relay_commit_time'].values()))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked paste -- the ruling`s END and part 1 of 1`s END',
     lambda S: 'RULING (R177) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'received IN FULL' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'the ferry scan bank', lambda S: '### VERDICT: ### **0 HIT(S) REPORTED.' in S['scan'] and 'b567_ferry.txt' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S) REPORTED', '1 HIT(S) REPORTED'))),
    ('G-STEPZERO-CENSUS', 'the two step-zero censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens']
     and 'b567' in S['cens'], lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the step-zero pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins'] and 'b567' in S['pins'],
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the step-zero process listing -- powershell its positive control, no lean, lake, grep, du or find',
     lambda S: 'POSITIVE CONTROL' in S['procs'] and 'powershell.exe' in S['procs']
     and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + ' 99 98 lean.exe       2026-10-01 00:00:00  lean x' + NL)),
    ('G-REG-LOCKED-FIRST', 'the face`s lock time against the first component banks` own times',
     lambda S: (utc_epoch(S['face'], 'locked at') or 1e18) < min(S['relay_commit_time'].values())
     and residue_first(S) and re.search(r'### at (\S+Z)', S['rstmt']).group(1) > '2026-10-01T01:37:20Z',
     lambda S: put(S, 'face', S['face'].replace('locked at (UTC) : 2026-10-01T01:37:20Z', 'locked at (UTC) : 2026-10-01T09:00:00Z'))),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s last notes', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify, its verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b566`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b566' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-RANAHEAD-DECLARED', 'the face`s section (0) AND relay`s log -- the section (0) files committed only after the lock',
     lambda S: ranahead(S), lambda S: put(S, 'relay_commit_time', {C_G: 1, C_H: 1})),
    ('G-R177-ENTERED', 'the banked paste AND the trail', lambda S: 'RULING (R177) END' in S['ferry'] and S['ot'].count('**(R177) ratified.**') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R177) ratified.**', '**ratified.**'))),
    ('G-READS-CITED', 'the reads bank', lambda S: 'NOT FOUND' not in S['reads'] and ':149 | theorem li_coeff_eq_taylorCoeff' in S['reads']
     and 'theorem LSeries_eq_mul_integral' in S['reads'] and 'def Register4_positivity' in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + NL + '### x -- NOT FOUND: y')),
    ('G-PUSHOUT-COMMITTED', 'relay commit 401bb062 -- one file, an ancestor of HEAD',
     lambda S: S['pushout']['files'] == ['data/b566_closing_push_out.txt'] and S['pushout']['anc'],
     lambda S: put(S, 'pushout', dict(S['pushout'], files=S['pushout']['files'] + ['data/x.txt']))),
    ('G-WEIGHT-LINES', 'FINDINGS at the weight line', lambda S: fline(S, S['wj'].get('line')).startswith(P(R.WEIGHT7_H))
     and S['find'].count(P(R.WEIGHT7_H)) == 1 and 'The equality lemma is itself a finding' in fline(S, S['wj'].get('line'))
     and 'three faces' in fline(S, S['wj'].get('line')) and 'h2 is open' in fline(S, S['wj'].get('line')),
     lambda S: put(S, 'find', S['find'].replace('The equality lemma is itself a finding', 'The equality lemma'))),
    ('G-CEILING-AMENDED', 'README and REGISTRY against their pre-act blobs, the FINDINGS record, the banked paste`s sentence',
     lambda S: ceiling_ok(S), lambda S: put(S, 'cj', dict(S['cj'], sentence='Li`s criterion is proved.'))),
    ('G-NOT-SUPPORTABLE-KEPT', 'the inserted lines and the FINDINGS record', lambda S: not_supp(S),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'].replace('*λ_n ≥ 0 proved*'.encode(), b'x')}))),
    ('G-FIELD-LINE', 'FINDINGS at the field line', lambda S: fline(S, S['fj'].get('line')).startswith(P(R.FIELD7_H))
     and 'no priority is claimed' in fline(S, S['fj'].get('line')) and 'compose in one kernel at one pin' in fline(S, S['fj'].get('line')),
     lambda S: put(S, 'find', S['find'].replace('no priority is claimed.', 'priority.'))),
    ('G-ADDENDUM-WRITELIST', 'the addendum bank read by tools/addenda.py, and b566`s re-run',
     lambda S: ADD.accepted_bases(S['addb'], ADD.paste_reader(D)) == {'LICENSE'}
     and re.search(r'G-WRITELIST-KINDS\s+PASS\s+PASS\s+FAIL\s+OK', S['rr_after']) is not None,
     lambda S: put(S, 'addb', S['addb'].replace('carried by (R176)(3)', 'carried by (R176)(7)'))),
    ('G-ADDENDUM-LICENCE', 'the licence record`s blob line against the LICENSE blob on the kernel`s main, and b566`s re-run',
     lambda S: ADD.blob_matches(S['lic'], S['lic_main']) and re.search(r'G-LICENCE-PRINTED\s+PASS\s+PASS\s+FAIL\s+OK', S['rr_after']) is not None,
     lambda S: put(S, 'lic_main', S['lic_main'].replace(b'\n', b'\r\n'))),
    ('G-ADDENDA-ALONE', 'relay`s two commits -- each its change and its test, nothing else',
     lambda S: S['files_g'] == FILES_G and S['files_h'] == FILES_H,
     lambda S: put(S, 'files_g', S['files_g'] + ['data/b567_weight.txt'])),
    ('G-ADDENDA-MUTATION', 'the two test banks -- every case as wanted, the mutations among them',
     lambda S: '15 of 15 cases as wanted -- PASS' in S['tw'] and '13 of 13 cases as wanted -- PASS' in S['tl']
     and 'ARM MUTATION: a stray CHANGELOG.md no clause names, beside the addendum -> FAIL got False want False OK' in S['tw']
     and 'MUTATION: a line carrying the WORKING-COPY digest does NOT match the blob' in S['tl'],
     lambda S: put(S, 'tw', S['tw'].replace('15 of 15', '14 of 15'))),
    ('G-B566-RERUN-COUNTED', 'b566`s re-runs before and after, and their reading',
     lambda S: rerun_counted(S), lambda S: put(S, 'rr_after', S['rr_after'].replace('LIVE PASSING : 72.', 'LIVE PASSING : 74.'))),
    ('G-CENSUS-LINE', 'data/b551_toolchains.txt against its pre-act blob -- a true prefix plus ONE line',
     lambda S: census_ok(S), lambda S: put(S, 'census', S['census'] + 'a second line' + NL)),
    ('G-STALE-MARK', 'OPEN_TRAILS', lambda S: S['ot'].count(P(R.STALE7_H)) == 1 and '`toolchain-trial-b551` STALE' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('`toolchain-trial-b551` STALE', 'x'))),
    ('G-DEPRECATIONS-FILED', 'OPEN_TRAILS and the deprecations bank', lambda S: S['ot'].count(P(R.DEPR7_H)) == 1
     and len(S['dj'].get('top', [])) == 10 and 'classes whose warning names NO replacement : 0' in S['deps']
     and 'deprecation warning lines' in S['deps'] and S['dj'].get('lines') == 2044,
     lambda S: put(S, 'dj', dict(S['dj'], top=S['dj']['top'][:9]))),
    ('G-CACHE-MAIN', 'the cache banks AND the checkout READ HERE -- its Mathlib, the forward .lake gone, the old one aside',
     lambda S: cache_ok(S), lambda S: put(S, 'ck_mathlib', '51e6992e')),
    ('G-BULKA-VERIFIED', 'the verification bank -- 33 of 33 bodies and the LICENSE, by blob digest',
     lambda S: S['bv'].get('verified') is True and S['bv'].get('agree') == 33 == S['bv'].get('total') and S['bv'].get('licence') is True,
     lambda S: put(S, 'bv', dict(S['bv'], agree=32))),
    ('G-BULKA-DELETED', 'the clone`s path READ HERE and the deletion bank', lambda S: bulka_deleted(S),
     lambda S: put(S, 'bulka_exists', True)),
    ('G-RESIDUE-STATEMENT-FIRST', 'the statement bank against the build log`s first line and the file on the pushed main',
     lambda S: residue_first(S), lambda S: put(S, 'stmt_sha_main', '0' * 64)),
    ('G-RESIDUE-PRINTS', 'the E0 bank (residue)', lambda S: S['e3'].get('gate') is True and len(S['e3'].get('rows', {})) == 3
     and all(r['std3'] for r in S['e3']['rows'].values()),
     lambda S: put(S, 'e3', dict(S['e3'], gate=False))),
    ('G-RESIDUE-ROW-APPENDED', 'THE_RESIDUE_OF_RH.md against its pre-act blob -- one line appended', lambda S: residue_row(S),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{RESREL: S['pp_now'][RESREL] + b'another line\n'}))),
    ('G-S7-READING', 'FINDINGS at the §7 line, and the residue document`s §§1-8 kept',
     lambda S: fline(S, S['sj'].get('line')).startswith(P(R.S7_H)) and 'a reading, not an edit' in fline(S, S['sj'].get('line'))
     and 'candidate supplier' in fline(S, S['sj'].get('line')) and rd8(S['pp_now'][RESREL]).startswith(rd8(S['pp_prior'][RESREL])),
     lambda S: put(S, 'find', S['find'].replace('a reading, not an edit', 'an edit'))),
    ('G-ZB-CONSUMERS', 'the consumers bank', lambda S: S['zbj'].get('complete') is True
     and sorted(S['zbj'].get('consumed', {})) == ['Zeta0EqZeta', 'ZetaBnd_aux1b', 'analyticAt_riemannZeta', 'riemannZeta0'],
     lambda S: put(S, 'zbj', dict(S['zbj'], complete=False))),
    ('G-CHI-BANKED', 'the χ build log -- the attempts and the module builds of record', lambda S: chi_banked(S),
     lambda S: put(S, 'cbuild', S['cbuild'].replace('--- +SIDEExplicitFormula.Chi.Statement rc=0', '--- +x rc=1'))),
    ('G-CHI-PRINTS', 'the E0 bank (chi)', lambda S: S['e4'].get('gate') is True and len(S['e4'].get('rows', {})) == 29
     and all(r['std3'] for r in S['e4']['rows'].values()),
     lambda S: put(S, 'e4', dict(S['e4'], gate=False))),
    ('G-EF-LIT-CHI-STATED', 'Chi/Statement.lean on the pushed main', lambda S: ef_stated(S),
     lambda S: put(S, 'stmt', S['stmt'].replace('def EF_lit_chi', 'theorem EF_lit_chi'))),
    ('G-H18-SCORED', 'the scores and the desk', lambda S: all(scored(S, x) for x in ('h18a', 'h18b', 'h18c')),
     lambda S: put(S, 'desk', S['desk'].replace('**(H18C)**', '**(H18X)**'))),
    ('G-GRADES-BANKED', 'the two E0 banks` counts and the rowgen diff', lambda S: S['e3'].get('counts') == {'DERIVES': 2, 'INTERFACES': 0}
     and S['e4'].get('counts') == {'DERIVES': 24, 'INTERFACES': 0} and S['rowgen'].count("['ok']") == 6 and 'PIN:' not in S['rowgen'],
     lambda S: put(S, 'rowgen', S['rowgen'] + NL + "('x', ['PIN: x'])")),
    ('G-TAG-READ-BACK', 'ls-remote READ HERE and the kernel push capture -- main read back BEFORE the tag', lambda S: tag_ok(S),
     lambda S: put(S, 'k', dict(S['k'], v010='0' * 40))),
    ('G-KERNEL-STATEMENTS-KEPT', 'the kernel`s .lean files, v0.9 against the pushed main -- added, none modified',
     lambda S: kernel_kept(S), lambda S: put(S, 'lean_ns', S['lean_ns'] + ['M\tSIDEExplicitFormula/LiWeil.lean'])),
    ('G-FINDINGS-ENTRY', 'FINDINGS', lambda S: S['find'].count(P(R.FH7)) == 1 and fline(S, S['fnd'].get('heading_line')) == P(R.FH7),
     lambda S: put(S, 'find', S['find'].replace(P(R.FH7), '## x'))),
    ('G-CORR-ROWS', 'CORRESPONDENCE against its pre-act blob -- rows 407-412, once each', lambda S: corr_ok(S),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 407 | dup |')),
    ('G-TRAIL-RECORD', 'the trail`s own text -- THIS act`s record', lambda S: S['ot'].count(P(R.HEADING7)) == 1 and '(N7)' in trail(S)
     and 'v0.10' in trail(S), lambda S: put(S, 'ot', S['ot'].replace(P(R.HEADING7), '### b567 -'))),
    ('G-NEXT-ACT-NAMED', 'the trail`s own text', lambda S: 'opens lane three for the ζ-leg' in trail(S) and 'CP-4' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('opens lane three for the ζ-leg', 'x'))),
    ('G-BRANCHES-DELETED', 'the branch bank and the repositories READ HERE', lambda S: branches_ok(S),
     lambda S: put(S, 'branch_lists', dict(S['branch_lists'], x='  push-b566'))),
    ('G-KEPT-BRANCHES', 'the kernel`s kept branches at the remote against b566`s recorded heads', lambda S: kept_ok(S),
     lambda S: put(S, 'k', dict(S['k'], kept=dict(S['k']['kept'], **{'grh-weil-b564': '0' * 40})))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA against its blob', lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b' '}))),
    ('G-OTHER-KERNELS-UNTOUCHED', 'every other kernel`s main READ HERE against b566`s closing heads; SIDE-global-section the rows alone',
     lambda S: others_ok(S), lambda S: put(S, 'others', dict(S['others'], **{'SIDE-kernel': ('0' * 40, '0' * 40)}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b567_x.py'])),
    ('G-DELETE-FREE', 'this act`s own Python tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b567_x.py', 'x')])),
    ('G-NODEPOSIT', 'the deposit directory`s tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(P(R.HEADING7), '### b567 -'))),
    ('G-PRIORBANK-UNCHANGED', 'every prior bank -- by digest after the push, by time before it; the two ordered appends as prefix + one line',
     lambda S: S['prior_res']['ok'] and S['prior_res']['app'] == 2, lambda S: put(S, 'prior_res', dict(S['prior_res'], ok=False))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the five written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(FIXED + CEIL + [RESREL]), lambda S: put(S, 'tracked', list(S['tracked']) + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(P(R.HEADING7)) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + P(R.HEADING7) + ' a second record')),
    ('G-N1-SCORED', 'the scores and the desk', lambda S: scored(S, 'n1'), lambda S: put(S, 'desk', S['desk'].replace('**(N1)**', 'x'))),
    ('G-N2-SCORED', 'the scores and the desk', lambda S: scored(S, 'n2'), lambda S: put(S, 'desk', S['desk'].replace('**(N2)**', 'x'))),
    ('G-N3-SCORED', 'the scores and the desk', lambda S: scored(S, 'n3'), lambda S: put(S, 'desk', S['desk'].replace('**(N3)**', 'x'))),
    ('G-N4-SCORED', 'the scores and the desk', lambda S: scored(S, 'n4'), lambda S: put(S, 'desk', S['desk'].replace('**(N4)**', 'x'))),
    ('G-N5-SCORED', 'the scores and the desk', lambda S: scored(S, 'n5'), lambda S: put(S, 'desk', S['desk'].replace('**(N5)**', 'x'))),
    ('G-N6-SCORED', 'the scores and the desk', lambda S: scored(S, 'n6'), lambda S: put(S, 'desk', S['desk'].replace('**(N6)**', 'x'))),
    ('G-N7-SCORED', 'the scores and the desk', lambda S: scored(S, 'n7'), lambda S: put(S, 'desk', S['desk'].replace('**(N7)**', 'x'))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, x) for x in ('s1', 's2', 's3')),
     lambda S: put(S, 'desk', S['desk'].replace('**(S3)**', 'x'))),
    ('G-WRITELIST-KINDS', 'every b567 commit in four repositories (the kernel`s main and the residue branch), against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds'] if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness itself -- the positive control is RUN on every arm',
     lambda S: not live_limb_guard(S['suite']), lambda S: put(S, 'suite', S['suite'].replace('defective.append(name)', 'pass'))),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)', lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b567')" in S['suite']
                and "data/b567_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b567_components.txt' in gits(ROOT, 'show'")),
]


def regenerate():
    """### ### **(R107): THE GENERATOR IS PART OF THE CLOSING SUITE** -- re-run before anything is scored; its diff a cell."""
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    diff = json.loads(read(os.path.join(D, 'terminal_table_diff.json')) or '{}')
    return r.returncode, diff


def main():
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or TRIAL) else regenerate()
    S['table'] = read(os.path.join(D, 'terminal_table.md'))
    tl = [l for l in S['table'].split(NL) if '`SIDEExplicitFormula.GRHWeil.LFunction_eq_mul_integral` |' in l]
    rec('  ### the regenerated table`s line for LFunction_eq_mul_integral: %s' % (tl[0][:220] if len(tl) == 1 else 'lines found %d' % len(tl)))
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    kinds_ref = set(re.findall(r'`(G-[A-Z0-9-]+)`-kind', g2))
    declared = sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - kinds_ref)
    names = [a[0] for a in ARMS]
    pushed = S['pushed']
    S['declared_eq_run'] = set(names) == set(declared)
    rec('=' * 104)
    rec('b567 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; read as a KIND reference, not a declaration : %s' % (len(declared), len(names), sorted(kinds_ref)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-42s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
    fail, defective, negfail = [], [], 0
    for name, reads, pred, pos in ARMS:
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
    pr = S['prior_res']
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d prior banks: %d against the pre-act tip, %d first tracked in the pushed tree, %d by file '
        'time, %d the ordered appends (prefix + one line); changed %s.' % (pr['checked'], pr['pre'], pr['pub'], pr['time'], pr['app'],
                                                                           pr['bad'] or 'NONE'))
    rec('  ### (R178)(2)(ii) THE AS-OF COMMIT : %s' % (('relay %s (%s) -- G-PRIORBANK-UNCHANGED read the relay data tree there, not at HEAD'
                                                      % (AS_OF[:8], '--as-of' if '--as-of' in sys.argv else 'b567_closing_push_out.txt'))
                                                     if AS_OF else 'NONE -- the tree-reading arm read live'))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
            % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []), len(gen_diff.get('changed') or [])))
    else:
        rec('  ### ### **(R170)(3): A RE-RUN ON THE PUSHED ACT -- THE GENERATOR WAS NOT RE-RUN** (it writes relay`s table files).')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if TRIAL:
        out = sys.argv[sys.argv.index('--trial') + 1]
    elif RERUN:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1])
    else:
        out = os.path.join(D, 'b567_checks_postpush.txt' if pushed else 'b567_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not (RERUN or TRIAL):
        json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective, neg_failures=negfail, declared=len(declared),
                       stray=stray), io.open(os.path.join(D, 'b567_exercise.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
