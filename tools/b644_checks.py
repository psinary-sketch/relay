# -*- coding: utf-8 -*-
"""b644_checks.py -- THE SUITE OF b644, UNDER (R254): THE CHAIN READ AT COMMIT AND SHARED FILES ADDITIVE; THE WATCHDOG STOP; THE HINGES
RECOUNTED AND THE CENSUS AT v0.7.1; SIDE-GLOBAL-SECTION'S INTERFACES UNDER THE STOP; THE TWO ROSTERS; THE SEVEN PATCH EDITIONS; THE DEPOSIT
DESCRIPTION AS SYNTHESIS AND ITS READERS; THE MIRROR AND THE DRAFT HELD; THE LATTICE BANKED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### The face is sealed AFTER Components 0-7, the mirror and the draft among them (b640's order); every commit whose subject opens `b644`
### and none of POST_SEAL's prefixes precedes the lock.
### ### G-ACTROOT-VERIFY reads the chain at commit (W-ORD-CHAIN-AT-COMMIT, tools/act_root.py from relay 60e1adf4): b624 to b644 AGREE.
### ### The harness is b568's to b643's (helpers, runner, seal), carried from tools/b643_checks.py; the sources, predicates and arms are b644's.
"""
import copy
import fnmatch
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import terminal_table as TT   # noqa: E402,F401
import b616_claims as KC0     # noqa: E402
import b644_worklist as K     # noqa: E402
import b641_worklist as K41   # noqa: E402

NL = chr(10)
PP, EF = K.PP, K.EF
GS = 'D:/SIDE-global-section'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b644_registration_2026-10-09.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs=K.GS_PIN)
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd', 'platt-b626': 'e939c92',
        'cite-b628': '98b7668', 'nb-b629': 'aa17442', 'dedekind-b631': '8c51431', 'v0.26-work': '82550e4'}
STEPZERO = K.STEPZERO
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA-E0-12C15C80'
FROZEN_ARM = 'G-GEN-OLD-LISTS-FROZEN-AT-84BAE29A-52822A5-GEN-84BAE29A'
FROZEN_PINS = ('84bae29a', '52822a5')
FROZEN_NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
FROZEN_PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
TABLE_FILES = K.TABLE_FILES
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
SP = K.SP
# ### the instruments b644 does not edit, against relay a0791790: b643's tools, the readers and their tools, the generators and their tests,
# ### the shared tools; tools/act_root.py and tools/mirror_roster.json are this act's two shared edits and are read by their own arms.
INST = ('b643_checks.py', 'b643_closing.py', 'b643_tests.py', 'b643_worklist.py', 'b643_reg_gate.py', 'b643_regspec.py', 'b643_record.py',
        'b642_record.py', 'b641_record.py', 'b640_record.py', 'b639_record.py', 'b638_record.py', 'b634_elab.py', 'b633_record.py', 'b616_record.py',
        'b616_claims.py', 'b602_record.py', 'b566_record.py', 'premise_status.py', 'e0_rule.py', 'b378_terminals.py', 'test_e0_rule.py',
        'chain_page.py', 'g_chain_page.py', 'test_chain_page.py', 'test_g_chain_page.py', 'test_chain_page_b596.py', 'test_chain_page_b638.py',
        'banned_terms.py', 'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'test_push_gated.sh',
        'test_act_root.py', 'test_act_root_order_b641.py', 'corr_row.py', 'mirror_build.ps1', 'mirror_verify.py', 'test_elab_reader_b634.py')
COUNT_CASE = r'^  \(\d+\) '
PRIOR_EDITED = ('data/glossary.txt',)      # ### (R254)(4): the glossary appended, read by G-GLOSSARY-APPENDED and G-SHARED-ADDITIVE


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    if 'ls-remote' in a:
        KC0.LSR[repo] = KC0.LSR.get(repo, 0) + 1
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def gs(repo, *a):
    return git(repo, *a)[1].strip()


def blob(repo, spec):
    r = subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except OSError:
        return ''


def rd(n):
    return read(os.path.join(D, n))


def jl(n):
    try:
        return json.load(io.open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def cr0(b):
    return None if b is None else b.replace(b'\r\n', b'\n')


def raw(p):
    try:
        return open(p, 'rb').read()
    except OSError:
        return None


def blob_id(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def files_of(repo, sha):
    return sorted(x for x in gs(repo, 'show', '--name-only', '--pretty=format:', sha).split(NL) if x.strip())


def iso_epoch(s):
    import calendar
    import time
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def utc_epoch(text, label):
    m = re.search(re.escape(label) + r'[^0-9]*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', text)
    return iso_epoch(m.group(1)) if m else None


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b644')
            and 'data/b644_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section|SIDE-explicit-formula|SIDE-structural-error-correction)/[^`\s]+)`', w)))


def untracked(repo, *paths):
    return [l[3:].strip() for l in git(repo, 'status', '--porcelain', '--untracked-files=all', '--', *paths)[1].split(NL) if l.startswith('?? ')]


def written_files():
    res = []
    for repo, name, pre in ((ROOT, 'relay', PRE['relay']), (PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs']),
                            (EF, 'SIDE-explicit-formula', K.EF_PIN)):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    if b is None:
        return []
    l = cr0(b if isinstance(b, bytes) else b.encode('utf-8')).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def tri(repo, path, pre):
    return (cr0(raw(os.path.join(repo, *path.split('/')))), cr0(blob(repo, '%s:%s' % (pre, path))), cr0(blob(repo, 'HEAD:' + path)))


def kern_now(face):
    out = {}
    for k in face:
        p = 'D:/' + k
        tags = {}
        for l in gs(p, 'for-each-ref', '--format=%(refname:short) %(objectname) %(*objectname)', 'refs/tags').split(NL):
            if l.strip():
                x = l.split()
                tags[x[0]] = (x[2] if len(x) > 2 else x[1])[:7]
        out[k] = [gs(p, 'rev-parse', '--short=7', 'main'), tags, sorted(x for x in gs(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()),
                  gs(p, 'status', '--porcelain', '--untracked-files=no')]
    return out


def sealed_now():
    out = {}
    for t in K.SEALED:
        b = raw(os.path.join(T, t))
        out[t] = hashlib.sha256(b).hexdigest() if b is not None else None
    return out


def appended(pre, now):
    return now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else ''




def rows_of_table():
    try:
        return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']
    except Exception:
        return []



def sources():
    import b644_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b644_lockgate_notes*.txt')))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b644_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cen71 = cr0(raw(os.path.join(PP, *K.CEN71.split('/'))))
    S = dict(
        REC=REC, face=face, ferry=rd('b644_ferry.txt'), scan=rd('b644_ferry_scan.txt'), cens=rd('b644_census_stepzero.txt'),
        fcens=rd('b644_faces_census_stepzero.txt'), pins0=rd('b644_pins_stepzero.txt'), procs=rd('b644_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b643_closing.txt'), reads=rd('b644_reads.txt'), branches=rd('b644_branches.txt'), answers=rd('b644_author_answers.txt'),
        prerun=rd('b644_arms_prerun.txt'), rl=jl('b644_record_lines.json'),
        tests=jl('b644_tests_stepzero.json'), testst=rd('b644_tests_stepzero.txt'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', 'HEAD', 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b644_seal_hashes.json'), sealnow=sealed_now(),
        files_chain=files_of(ROOT, K.CHAIN_COMMIT), files_add=files_of(ROOT, K.ADDITIVE_COMMIT),
        files_watch=(files_of(ROOT, K.WATCH_COMMITS[0]), files_of(ROOT, K.WATCH_COMMITS[1])),
        acc=rd('b644_actroot_commit.txt'), bw=jl('b644_build_watch.json'),
        ibj=jl('b644_iface_builds.json'), ibt=rd('b644_iface_builds.txt'), hj=jl('b644_hinges.json'), ht=rd('b644_hinges.txt'),
        pagej={k: jl('b644_page_%s.json' % k) for k in ('zeta', 'chi')}, pga=rd('b644_page_arms.txt'),
        pages_head={k: cr0(blob(PP, 'HEAD:' + K.PNAME[k])) for k in ('zeta', 'chi')},
        glossary=read(os.path.join(D, 'glossary.txt')), glossary_pre=(cr0(blob(ROOT, '%s:data/glossary.txt' % PRE['relay'])) or b'').decode('utf-8'),
        cen71=cen71, cen71_head=cr0(blob(PP, 'HEAD:' + K.CEN71)), cen7=(cr0(raw(os.path.join(PP, *K.CEN7.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + K.CEN7))),
        edj=jl('b644_edition.json'), ediff=rd('b644_edition_diff.txt'),
        croster=rd('b644_census_roster.txt'), rroster=rd('b644_repo_roster.txt'), patch=rd('b644_patch_editions.txt'),
        companions={c: ((K.show('day1/' + c, 'HEAD') or '').split(NL)[:12]) for c in K.COMPANION_FILES},
        roster_now=json.loads((raw(os.path.join(T, 'mirror_roster.json')) or b'{}').decode('utf-8')).get('files') or [],
        roster_pre=json.loads((blob(ROOT, PRE['relay'] + ':tools/mirror_roster.json') or b'{}').decode('utf-8')).get('files') or [],
        desc=rd(K.DESC), descj=jl('b644_deposit_description.json'), desct=rd('b644_desc_test.txt'), repairs=jl('b644_desc_repairs.json'),
        path=rd('b644_clause_path.txt'), residue=rd('b644_desc_residue.txt'),
        readers={k: jl('b644_reader_%s_compare.json' % k) for k in ('a', 'a2', 'd', 'd2', 'd3')},
        lattice=rd('b644_lattice.txt'), mirj=jl('b644_mirror.json'), zen=jl('b644_zenodo.json'), tfj=jl('b644_table_final.json'),
        closing_src=read(os.path.join(T, 'b644_closing.py')),
        local_present=os.path.exists(local),
        local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK),
        local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b644_act_root.json'), arj0=jl('b643_act_root.json'), art=rd('b644_act_root.txt'), rootsf=rd('act_roots.txt'),
        rpush=rd('b644_relay_root_push_out.txt'), ppush=rd('b644_pp_root_push_out.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b644_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        kbranches={l.split()[0]: l.split()[1] for l in gs(EF, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b643*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b644_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b644_mustnotexist.txt')), table_changed=None,
        fj=jl('b644_findings.json'), tj=jl('b644_trail.json'), sc=jl('b644_scores.json'), desk=rd('b644_desk_notes.txt'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files()
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['gs_tracked'] = gs(GS, 'status', '--porcelain', '--untracked-files=no')
    S['gs_diff'] = sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip()))
    S['ledger_adds'] = appended(S['fi_pre'], S['fi_now']) + NL + appended(S['ot_pre'], S['ot_now'])
    pub = [S['ledger_adds'], (S['cen71'] or b'').decode('utf-8', 'replace'), S['desc']] + [(S['pages_head'][k] or b'').decode('utf-8', 'replace') for k in ('zeta', 'chi')]
    pub += ['\n'.join(v) for v in S['companions'].values()]
    for f in sorted(os.listdir(D)):
        if f.startswith(('b644_', 'audit_b644_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [rd('act_roots.txt'), S['glossary']]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    S['outside'] = [n for n in S['REC'].OUTSIDE_NEEDLES if n in S['ledger_adds'] or n in (S['cen71'] or b'').decode('utf-8', 'replace') or n in S['desc']]
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES or p == 'data/act_roots.txt' or p in PRIOR_EDITED:
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S['bank_mtimes'] = {}
    for it in (S['arj'].get('items') or []):
        p = it.split()[0]
        if p.startswith('data/') and os.path.exists(os.path.join(ROOT, *p.split('/'))):
            S['bank_mtimes'][p] = os.path.getmtime(os.path.join(ROOT, *p.split('/')))
    S.update(extra_sources(S))
    return S


CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md', K41.CEN5, K41.CEN6,
            K.CEN7, K41.MONO, K41.SIEVE6)


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import b626_record as R26
    import b627_record as R27
    import act_root as AR
    import b638_record as R8
    import additive_shared as ADD
    X = {}
    for k in ('zeta', 'chi'):
        lp = os.path.join(D, K.NODES[k])
        try:
            X['gcp_' + k] = GCP.arm(lp, os.path.join(SP, '_b644_gcp'), os.path.join(D, K.PROBE[k]))
        except Exception as e:
            X['gcp_' + k] = dict(ok=False, why='raised %s' % type(e).__name__)
    rule = CP.E0
    CP.E0 = R26.e0_module(TC.RELAY_PIN)
    try:
        X['ctl'] = TC.control()
    finally:
        CP.E0 = rule
    X['ctl_arm'] = TC.ARM
    old = []
    pins, tc_c, tc_git = (TC.RELAY_PIN, TC.PRE_PP), TC.C, TC._GIT
    try:
        gen = R27.cp_module(FROZEN_PINS[0])
        gen.E0 = R26.e0_module(FROZEN_PINS[0])
        TC.RELAY_PIN, TC.PRE_PP = FROZEN_PINS
        TC.C, TC._GIT = gen, gen.git
        for k in ('zeta', 'chi'):
            lb, pb = blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_NODES[k])), blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_PROBE[k]))
            d = os.path.join(SP, '_b644_frozen')
            os.makedirs(d, exist_ok=True)
            lp, pp = os.path.join(d, FROZEN_NODES[k]), os.path.join(d, FROZEN_PROBE[k])
            open(lp, 'wb').write(lb or b'')
            open(pp, 'wb').write(pb or b'')
            rc, got = TC.regen(lp, pp)
            old.append(dict(list=FROZEN_NODES[k], rc=rc, equal=got is not None and got == cr0(blob(PP, '%s:%s' % (FROZEN_PINS[1], K.PNAME[k])))))
    except Exception as e:
        old.append(dict(list='raised %s' % type(e).__name__, rc=-1, equal=False))
    finally:
        TC.RELAY_PIN, TC.PRE_PP = pins
        TC.C, TC._GIT = tc_c, tc_git
    X['old_frozen'] = old
    try:
        X['ar_verify'] = AR.verify(remote=KC0.remote_refs)
        X['ar_reads'] = dict(AR.READS_AT)
    except Exception as e:
        X['ar_verify'], X['ar_reads'] = [('raised', type(e).__name__, [])], {}
    X['order_slack'] = AR.ORDER_SLACK
    X['sorry_tokens'] = S['REC'].sorry_tokens('main')
    try:
        X['gloss_block'] = CP.glossary_block()
    except Exception as e:
        X['gloss_block'] = ['raised %s' % type(e).__name__]
    X['gl_pages'] = {k: R8.glossary_lines((S['pages_head'][k] or b'').decode('utf-8', 'replace')) for k in ('zeta', 'chi')}
    X['gl_census'] = R8.glossary_lines((S['cen71'] or b'').decode('utf-8', 'replace'))
    try:
        X['additive'] = ADD.check(worktree=True)
    except Exception as e:
        X['additive'] = [('raised', type(e).__name__, [('x', [])])]
    X['desc_forbidden'] = S['REC'].forbidden(S['desc']) if S['desc'] else [('empty', '')]
    return X


def put(S, k, v):
    S[k] = v
    return S


def oline(S, n):
    ls = S['ot'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def fline(S, n):
    ls = S['find'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def trail(S):
    t = S['ot']
    i = t.find(S['REC'].TRAIL_HEAD())
    return t[i:] if i >= 0 else ''


def poss(t):
    import b566_record as R6
    return R6.Q.poss(t)


def procs_ok(S):
    p = S['procs']
    rows = [l for l in p.split(NL) if re.match(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut|python|tail)\.exe', l)]
    return 'powershell.exe' in p and '### ORPHANS:' in p and '\\v1.0\\' in p and all('### STOPPED BY PID' in l for l in rows) \
        and 'tail' in p.split('### names matched:')[1].split(NL)[0]


def absent_ok(S):
    a, b, c = S['absent']
    return a is None and b is None and c is None and cr0(None) is None and cr0(b'') == b'' and lines_of(None) == []


def rline(S, i, key='rl'):
    x = (S[key].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need, key='rl'):
    x = rline(S, i, key)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b644 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    blocks = re.split(r'^### CALL ', a, flags=re.M)[1:]
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    return bool(m) and int(m.group(1)) == len(heads) and len(heads) >= 2 and all(x >= 2 for x in per) and len(per) == len(heads) \
        and len(blocks) == a.count('RESULT (transcript line') and '### NO RESULT' not in a


def tests_ok(S):
    """every test file tracked at HEAD run: in the runner bank clean but test_chain_page_b638.py (4)-(7), or recorded RUN-BENEATH-HOLD."""
    j = S['tests']
    names = S['tracked_tests']
    rbh = [r['cmd'][-1] for r in (S['bw'].get('rows') or []) if r.get('cmd') and str(r['cmd'][-1]).startswith('test_')]
    nf = sorted(n for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(set(j) | set(rbh)) == names and nf == ['test_chain_page_b638.py'] \
        and j['test_chain_page_b638.py']['failing'] == ['(4)', '(5)', '(6)', '(7)'] \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 1' % (len(names), len(names) - len(rbh))) in S['testst']


def instruments_ok(S):
    for f, (pre, now, head) in S['inst'].items():
        if pre is None or pre != now:
            return False
    return True


def local_ok(S):
    return S['local_present'] and S['local_log'] == '' and S['local_index'] == '' and S['local_status'].startswith('??')


def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b644 seal', 'b644 pre-root', 'b644 root', 'b644 record', 'b644 --', 'b644 closing')


def _component_commit(s):
    return s.startswith('b644') and not s.startswith(POST_SEAL)


def sealed_after_ok(S):
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def chain_ok(S):
    t = S['tests'].get('test_act_root_commit_b644.py') or {}
    a = S['acc']
    return S['files_chain'] == sorted([K.CHAIN_TOOL, K.CHAIN_TEST]) and t.get('cases') == 5 and t.get('passing') == 5 \
        and re.search(r'AT THE RECORDED COMMIT.*?### ACTS 20 ; BANKS AGREE 20 ; DISAGREE 0', a, re.S) is not None \
        and re.search(r'THE WORKING TREE.*?### ACTS 20 ; BANKS AGREE 17 ; DISAGREE 3', a, re.S) is not None \
        and re.search(r'^  b638 AGREE ', a, re.M) and re.search(r'^  b639 AGREE ', a, re.M)


def additive_ok(S):
    t = S['tests'].get('test_additive_shared_b644.py') or {}
    return S['files_add'] == sorted([K.ADD_TOOL, K.ADD_TEST]) and t.get('cases') == 6 and t.get('passing') == 6


def shared_additive_ok(S):
    import additive_shared as ADD
    return bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']) \
        and ADD.removed_or_changed(ADD.lines(S['glossary_pre'].encode('utf-8')), ADD.lines(S['glossary'].encode('utf-8'))) == []


def watch_ok(S):
    t = S['tests'].get('test_build_watch_b644.py') or {}
    return S['files_watch'][0] == sorted([K.WATCH_TOOL, K.WATCH_TEST]) and S['files_watch'][1] == [K.WATCH_TOOL] \
        and t.get('cases') == 3 and t.get('passing') == 3


def runs_recorded_ok(S):
    rows = S['bw'].get('rows') or []
    mods = sorted(r['module'] for r in rows)
    return len(rows) == 7 and all(min(r['lows']) < r['hold'] == K.HOLD for r in rows) and 'test_elab_reader_b634' in mods \
        and all(any(m.startswith('SIDE-global-section/Interfaces/%s.' % i) for m in mods) for i, _p in K.IFACES)


GL_ADDED_KINDS = ['#', 'HINGE', '#', 'own evidence', 'HINGE']


def glossary_ok(S):
    pre = [l for l in S['glossary_pre'].split(NL) if l.strip()]
    now = [l for l in S['glossary'].split(NL) if l.strip()]
    add = now[len(pre):]
    kinds = ['#' if l.startswith('#') else l.split('\t')[0] for l in add]
    return now[:len(pre)] == pre and kinds == GL_ADDED_KINDS and 'superseding the entry above from 2026-10-09' in add[1] \
        and 'it supersedes the HINGE entry of 2026-10-08' in add[4]


def ifaces_ok(S):
    rows = S['ibj'].get('rows') or []
    return len(rows) == len(K.IFACES) and all(r['build']['verdict'] in ('BUILT', 'RUN-BENEATH-HOLD') for r in rows) \
        and '**INTERFACES MODULES 6 ;' in S['ibt']


def hinges_ok(S):
    rows = S['hj'].get('rows') or []
    nh = sum(1 for r in rows if r['hinge'])
    leave = [r['head'] for r in rows if r['old_hinge'] and not r['hinge']]
    return len(rows) == 50 and 0 < nh < 28 and not [r for r in rows if r['hinge'] and r['status'] == 'DOMAIN'] \
        and all(re.search(r'^  %s\s' % re.escape(h), S['ht'], re.M) for h in leave) and sum(1 for r in rows if r['old_hinge']) == 28


def census_ok(S):
    j = S['edj']
    c = S['cen71']
    a7, b7 = S['cen7']
    return bool(j and c) and S['cen71_head'] == c and j.get('sha256') == hashlib.sha256(c).hexdigest() and a7 is not None and a7 == b7 \
        and 'v0.7 LINES REMOVED OR REPLACED : 0.' in S['ediff'] and not j.get('dry')


def reconciled_ok(S):
    t = (S['cen71'] or b'').decode('utf-8', 'replace')
    tail = t[t.find('### The premise table at v0.7.1'):]
    rows = [l.split(' | ') for l in tail.split(NL) if l.startswith('| ') and not l.startswith('| head') and not l.startswith('|:')]
    back = t[t.find('## Back matter of the v0.7.1 edition'):]
    return bool(rows) and not [r for r in rows if len(r) > 2 and r[1].strip() == 'WITNESSED' and r[2].strip().startswith('UNWITNESSED')] \
        and 'STATUS beside NON-VACUITY' in back


def pages_ok(S):
    return all(S['pagej'][k] and S['pages_head'][k] and S['pagej'][k].get('sha256') == hashlib.sha256(S['pages_head'][k]).hexdigest()
               for k in ('zeta', 'chi'))


def glossary_everywhere_ok(S):
    b = S['gloss_block']
    return isinstance(b, list) and len(b) > 4 and all(S['gl_pages'][k] == b for k in ('zeta', 'chi')) and S['gl_census'] == b \
        and ('- **own evidence** —') in NL.join(b)


def patch_ok(S):
    labels = dict((c, n) for c, _o, n in S['REC'].COMPANIONS)
    return '**COMPANIONS 7 ; LABELLED AND COMMITTED ALONE, THE SCANNER UNMOVED 7.**' in S['patch'] \
        and all(any(('%s, October 2026' % labels[c[:-3]]) in l for l in S['companions'][c]) for c in K.COMPANION_FILES)


ROSTER_ADD = ['day1\\%s' % c for c in K.COMPANION_FILES] + ['phase2\\method\\THE_KEYSTONE_CENSUS_v0_7.md', 'phase2\\method\\THE_KEYSTONE_CENSUS_v0_7_1.md']


def roster_ok(S):
    pre, now = S['roster_pre'], S['roster_now']
    return len(pre) == 74 and now[:len(pre)] == pre and now[len(pre):] == ROSTER_ADD


def description_ok(S):
    j = S['descj']
    ps = re.findall(r'<p>(.*?)</p>', S['desc'], re.S)
    return len(ps) == 5 and all(p.startswith(h) for p, h in zip(ps, S['REC'].PART_HEADS)) and S['desc_forbidden'] == [] \
        and '### ### **9 of 9 cases as wanted -- PASS**' in S['desct'] and 'NOT READ' not in S['desc'] and j.get('order_ok')


def repairs_ok(S):
    r = S['repairs'].get('repairs') or []
    return len(r) == 15 and all(not x['lost'] and x['planted_caught'] for x in r) \
        and r[-1]['sha256'] == hashlib.sha256(S['desc'].encode('utf-8')).hexdigest()


def readers_ok(S):
    R = S['readers']
    want = {'a': (1, 1), 'a2': (1, 1), 'd': (3, 3), 'd2': (3, 3), 'd3': (3, 3)}
    return all((R[k].get('needles'), R[k].get('hand')) == v and R[k].get('of') == v[0] for k, v in want.items())


def mirror_ok(S):
    m = S['mirj']
    return bool(m) and m.get('clean') and m.get('root_line', '').startswith('Act root: b643 ') and all((m.get('appended') or {}).values()) \
        and m.get('files') == len(S['roster_now'])


def draft_ok(S):
    r = (S['zen'].get('read') or {})
    return bool(r) and r.get('exact') and r.get('digest') and r.get('files_ok') and r.get('submitted') is False and r.get('n_files') == 14


def table_final_ok(S):
    t = S['tfj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('added') and not t.get('grade_moved') and not t.get('moved')


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 21 and rows[20][:3] == ['b644', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it] \
        and any(it.startswith('data/b644_hinges.txt ') for it in j.get('items') or []) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b644_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def midpush_ok(S):
    heads = (S['arj'].get('reads') or {}).get('heads') or {}
    m1 = re.search(r'push_gated: main read back at the remote: (\w+)', S['rpush'])
    m2 = re.search(r'push_gated: main read back at the remote: (\w+)', S['ppush'])
    return bool(m1 and m2) and heads.get('relay') == m1.group(1) and heads.get('PLACE-papers') == m2.group(1)


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b644') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 645)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The chain at commit**', '**The watchdog stop**', '**The Interfaces**', '**The hinges and the census at v0.7.1**',
                 '**The rosters**', '**The patch editions**', '**The description**', '**The draft**', '**The lattice**', '**The record lines**',
                 '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b645')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') == S['REC'].TITLE and all(x in tail for x in ENTRY_NEEDLES)


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0].split(',')[0].split(' ')[0] in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k) in S['desk']


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def route_held(S):
    pub = ['actions' + '/publish', 'z_' + 'publish']
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if any(p in t for p in pub)]


def kernels_untouched(S):
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and len(f) == len(S['REC'].KERNS_READ) and all(k in n and n[k] == f[k] for k in f) \
        and S['lv_head'].startswith('2f71068a') and S['gs_diff'] == [] and S['gs_tracked'] == ''


CORPUS = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE, DIR_PAGE, K.CEN71] + ['day1/%s' % c for c in K.COMPANION_FILES])


def corpus_scope(S):
    return S['pp_changed'] == CORPUS


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author in any ' + 'outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and (', no ' + 'outbound request,') not in t


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


READ_NEEDLES = ('data/b643_closing.txt @ a0791790', 'data/b643_defects.txt @ a0791790', 'tools/act_root.py @ a0791790', 'data/glossary.txt @ a0791790',
                'tools/mirror_roster.json @ a0791790', 'tools/b640_record.py @ a0791790', 'ERRATA.md @ 93cfd59e', ':13591 ', ':13397 ',
                'data/b643_closing_push_out.txt @ f09c582a', '### the local intake bank`s state: ?? data/b628_intake_crank_v0_5.txt')


def prompts_banked(S):
    return len(re.findall(r'^### PROMPT ', S['answers'], re.M))


def _rl(S, i, line, key='rl'):
    ls = list(S[key].get('lines') or [])
    ls[i:i + 1] = [dict(rline(S, i, key), line=line)]
    return put(S, key, dict(S[key], lines=ls))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R254) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + NL + ' 11 22 lean.exe  lean x')),
    ('G-STEPZERO-TESTS', 'the runner bank and the watchdog`s bank against the test files tracked at HEAD: every one clean but test_chain_page_b638.py (4)-(7), or run beneath the hold and recorded',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject',
     lambda S: sealed_after_ok(S), lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b644 record', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b643`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b643' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-R254-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R254) END' in S['ferry'] and S['ot'].count('**(R254) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R254) ratified', '**(R2540) ratified'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'] and 'NO SUCH BLOB' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'].replace(':13591 ', ':13590 '))),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompts, every call`s result', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('prompt(s)', 'prompts'))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and 'PRE-SEAL (R202)(3) READING' in S['prerun'] and ('ARMS RUN : %d.' % len(ARMS)) in S['prerun']
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 10 ** 12) < S['lock_epoch'],
     lambda S: put(S, 'prerun', S['prerun'].replace('PRE-SEAL', 'POST-SEAL'))),
    ('G-PUSHOUT-COMMITTED', 'relay f09c582a`s files', lambda S: S['pushout'][0] == ['data/b643_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', ([], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b643') == 5, lambda S: put(S, 'push_lists', {'x': 'push-b643'})),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(v) for b, v in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'dedekind-b631': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80, every PLACE-papers read at ba5f0ea and the E0 rule`s blob at 12c15c80',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] + '-E0-12C15C80' == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(x, ok=False) for x in S['ctl']])),
    (FROZEN_ARM, 'b622`s lists with every relay read at 84bae29a, the E0 rule`s and the generator`s blobs at 84bae29a, against the pages at 52822a5',
     lambda S: len(S['old_frozen']) == 2 and all(x.get('rc') == 0 and x.get('equal') is True for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [dict(x, equal=False) for x in S['old_frozen']])),
    ('G-INSTRUMENTS-UNEDITED', 'b643`s tools, the readers and their tools, the shared tools, the generators and their tests against a0791790',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'terminal_table.py': (b'a', b'b', b'b')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', None, None))),
    ('G-SEAL-HASHES', 'the sealed tools` sha256 recorded at the seal against the tools on disk', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{K.SEALED[0]: '0' * 64}))),
    ('G-CHAIN-AT-COMMIT', 'relay 60e1adf4 alone with tools/act_root.py and its planted test (5 of 5); the commit read of every root, 20 of 20 AGREE, b638 and b639 among them; the working tree 3 DISAGREE',
     lambda S: chain_ok(S), lambda S: put(S, 'acc', S['acc'].replace('BANKS AGREE 20 ; DISAGREE 0', 'BANKS AGREE 19 ; DISAGREE 1'))),
    ('G-ADDITIVE-ARM', 'relay 0651e7cc alone with tools/additive_shared.py and its test (6 of 6)', lambda S: additive_ok(S),
     lambda S: put(S, 'files_add', S['files_add'] + ['tools/x.py'])),
    ('G-SHARED-ADDITIVE', 'every shared data file against its previous commit and HEAD, and the glossary against a0791790: no line removed or changed',
     lambda S: shared_additive_ok(S), lambda S: put(S, 'glossary', S['glossary'].replace('HINGE\t', 'HINGE2\t', 1))),
    ('G-WATCHDOG-STOP', 'relay 1c4ca202 alone with tools/build_watch.py and its test, e0cc0904 the tool alone; the test 3 of 3', lambda S: watch_ok(S),
     lambda S: put(S, 'files_watch', (S['files_watch'][0] + ['x'], S['files_watch'][1]))),
    ('G-RUNS-RECORDED', 'the watchdog`s bank: the lean test and every Interfaces module each recorded RUN-BENEATH-HOLD with its lows beneath 2,560 MB',
     lambda S: runs_recorded_ok(S), lambda S: put(S, 'bw', dict(S['bw'], rows=(S['bw'].get('rows') or [])[:-1]))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b643`s weight, its figures from its banks',
     lambda S: landed(S, 0, ('(:7995)', 'd845516f', '497', '28 hinges', 'Prime')), lambda S: _rl(S, 0, 1)),
    ('G-CHAIN-LINE', 'OPEN_TRAILS at the banked line: W-ORD-CHAIN-AT-COMMIT acted',
     lambda S: landed(S, 1, ('W-ORD-CHAIN-AT-COMMIT', '(:12210)', '20 of 20 AGREE', '85 such reads')), lambda S: _rl(S, 1, 1)),
    ('G-ADDITIVE-LINE', 'OPEN_TRAILS at the banked line: shared data files additive', lambda S: landed(S, 2, ('additive', 'additive_shared.py')),
     lambda S: _rl(S, 2, 1)),
    ('G-WATCHDOG-ACTED-LINE', 'OPEN_TRAILS at the banked line: W-ORD-WATCHDOG-STOP acted', lambda S: landed(S, 3, ('(:13563)', 'RUN-BENEATH-HOLD', '2,560 MB')),
     lambda S: _rl(S, 3, 1)),
    ('G-GLOSSARY-APPENDED', 'data/glossary.txt against a0791790: the old lines unmoved; appended a dated line, the refined HINGE, a dated line, own evidence, the corrected HINGE',
     lambda S: glossary_ok(S), lambda S: put(S, 'glossary', S['glossary'].replace('it supersedes the HINGE entry of 2026-10-08', 'x'))),
    ('G-IFACES-BUILT-OR-RECORDED', 'the Interfaces bank: six modules, each BUILT or RUN-BENEATH-HOLD', lambda S: ifaces_ok(S),
     lambda S: put(S, 'ibj', dict(S['ibj'], rows=(S['ibj'].get('rows') or [])[:5]))),
    ('G-HINGES-REFINED', '(N3): the recount: 50 heads, fewer hinges than b643`s 28, no DOMAIN head among them, every head that leaves printed with its reason',
     lambda S: hinges_ok(S), lambda S: put(S, 'hj', dict(S['hj'], rows=[dict(r, hinge=True) for r in S['hj'].get('rows') or []]))),
    ('G-CENSUS-V071', 'the census at v0.7.1 at PLACE-papers HEAD against its bank; v0.7 unedited; no v0.7 line removed or replaced', lambda S: census_ok(S),
     lambda S: put(S, 'ediff', S['ediff'].replace('REMOVED OR REPLACED : 0.', 'REMOVED OR REPLACED : 1.'))),
    ('G-STATUS-RECONCILED', 'the census at v0.7.1`s premise table: no WITNESSED status beside an UNWITNESSED non-vacuity; the reconciliation read', lambda S: reconciled_ok(S),
     lambda S: put(S, 'cen71', (S['cen71'] or b'').replace(b'STATUS beside NON-VACUITY', b'x'))),
    ('G-INTERFACES-OMISSION-NAMED', 'the census at v0.7.1: the consumers not read named with the Interfaces module that was not built', lambda S: b'UNREAD (Interfaces/LocalLimit.lean, RUN-BENEATH-HOLD)' in (S['cen71'] or b''),
     lambda S: put(S, 'cen71', (S['cen71'] or b'').replace(b'UNREAD (Interfaces/', b'UNREAD (I/'))),
    ('G-PAGES-REEMITTED', 'both page banks against PLACE-papers HEAD', lambda S: pages_ok(S),
     lambda S: put(S, 'pagej', dict(S['pagej'], chi=dict(S['pagej']['chi'], sha256='0')))),
    ('G-PAGE-ARMS-BANKED', 'the page arms bank: 2 of 2', lambda S: '**PAGE ARMS PASSING : 2 of 2.**' in S['pga'],
     lambda S: put(S, 'pga', S['pga'].replace('2 of 2', '1 of 2', 1))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from the lists in force against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from the lists in force against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-GLOSSARY-EVERYWHERE', 'the glossary block on both pages at PLACE-papers HEAD and in the census at v0.7.1, byte for byte the live builder`s, own evidence in it',
     lambda S: glossary_everywhere_ok(S), lambda S: put(S, 'gl_census', (S['gl_census'] or [''])[:-1])),
    ('G-CENSUS-ROSTER', 'the census roster: the section list, the roster header, every keystone read', lambda S: '### THE SECTION LIST' in S['croster']
     and '### THE ROSTER HEADER' in S['croster'] and 'KEYSTONES READ 48' in S['croster'] and 'NO REGISTRY ROW 0' in S['croster'],
     lambda S: put(S, 'croster', S['croster'].replace('NO REGISTRY ROW 0', 'NO REGISTRY ROW 1'))),
    ('G-REPO-ROSTER', 'the repository roster: every chain repository cloned, the outsiders listed', lambda S: 'IN THE CHAIN 38 OF 38' in S['rroster']
     and 'OUTSIDE THE CHAIN (' in S['rroster'], lambda S: put(S, 'rroster', S['rroster'].replace('38 OF 38', '37 OF 38'))),
    ('G-PATCH-EDITIONS', 'the patch bank and each companion`s opening lines at PLACE-papers HEAD: the patch label on every one', lambda S: patch_ok(S),
     lambda S: put(S, 'companions', dict(S['companions'], **{'ONE_PAGE_PROOF.md': []}))),
    ('G-ROSTER-APPENDED', 'tools/mirror_roster.json against a0791790: 74 rows unmoved, the seven companions and both census editions appended', lambda S: roster_ok(S),
     lambda S: put(S, 'roster_now', S['roster_now'][:-1])),
    ('G-DESCRIPTION', '(N4): the description: five parts in the ruled order, no forbidden content, its test 9 of 9, no unread figure', lambda S: description_ok(S),
     lambda S: put(S, 'desc_forbidden', [('an act number', 'b644')])),
    ('G-DESC-REPAIRS', 'the repairs bank: fifteen rewrites, nothing lost in any, every planted failure caught, the last equal to the bank', lambda S: repairs_ok(S),
     lambda S: put(S, 'repairs', dict(S['repairs'], repairs=(S['repairs'].get('repairs') or [])[:-1]))),
    ('G-CLAUSE-PATH', 'the path print: no OPEN premise on the path from h2_sign to RiemannHypothesis', lambda S: '; OPEN 0 ' in S['path'],
     lambda S: put(S, 'path', S['path'].replace('; OPEN 0 ', '; OPEN 1 '))),
    ('G-READERS-SCORED', 'the five reader banks: the hinge question 1 of 1 twice, the description 3 of 3 three times, by the needles and by hand', lambda S: readers_ok(S),
     lambda S: put(S, 'readers', dict(S['readers'], d3=dict(S['readers']['d3'], hand=2)))),
    ('G-RESIDUE-BANKED', 'the residue bank: what the third reader still marks, the repairs stopped', lambda S: re.search(r'RESIDUE \d+ PASSAGES ; NOT REPAIRED IN THIS ACT', S['residue']) is not None,
     lambda S: put(S, 'residue', '')),
    ('G-LATTICE-BANKED', 'the lattice bank: the rule`s test 6 of 6, the table, the top', lambda S: 'THE RULE`S TEST 6 OF 6' in S['lattice'] and '### TOP (' in S['lattice'],
     lambda S: put(S, 'lattice', S['lattice'].replace('TEST 6 OF 6', 'TEST 5 OF 6'))),
    ('G-MIRROR-BUILT', 'the mirror bank: clean on all three clauses, b643`s root line, the appended rows in it, every roster row', lambda S: mirror_ok(S),
     lambda S: put(S, 'mirj', dict(S['mirj'], clean=False))),
    ('G-DRAFT-READBACK', '(N5): the draft read back: the description byte for byte and digest for digest, fourteen files at their digests, unsubmitted', lambda S: draft_ok(S),
     lambda S: put(S, 'zen', dict(S['zen'], read=dict(S['zen'].get('read') or {}, submitted=True)))),
    ('G-TABLE-FINAL', 'the final table bank against relay HEAD`s table: no row moved, added or gone', lambda S: table_final_ok(S),
     lambda S: put(S, 'tfj', dict(S['tfj'], gone=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s b644 line, the root bank and its items: previous b643`s root, the hinges among the banks, the recorded commit',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b644 x y' + NL)),
    ('G-ACTROOT-LAST', 'the root bank`s time against every bank it names, the seal bank among them', lambda S: root_last_ok(S),
     lambda S: put(S, 'arj', dict(S['arj'], at_epoch=0.0))),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay and PLACE-papers heads against the read-backs of the pushes before it', lambda S: midpush_ok(S),
     lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed by this suite at commit, one remote read per repository: b624 to b644 AGREE, b644 with no CRLF read',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', [(a, 'DISAGREE' if a == 'b644' else v, w) for a, v, w in S['ar_verify']])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line, the entry read to the next heading', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD(), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous', lambda S: bool(S['arj'])
     and ('**Act root:** b644 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'this act`s trail record: every sealed tool agreeing at the record', lambda S: all(
        ('%s agree' % t_) in trail(S) for t_ in K.SEALED), lambda S: put(S, 'ot', S['ot'].replace('%s agree' % K.SEALED[0], '%s differ' % K.SEALED[0]))),
    ('G-LABEL-READER-ENTERED', 'this act`s trail record: W-ORD-LABEL-READER entered on the author`s answer', lambda S: 'W-ORD-LABEL-READER, entered on the author’s answer' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('W-ORD-LABEL-READER, entered', 'x'))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the prompts, counted from the answers bank', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and ('**Prompts to the author:** %d ' % prompts_banked(S)) in trail(S), lambda S: put(S, 'answers', S['answers'] + NL + '### PROMPT 99 (x): y')),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b645, the author’s word pending' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b645, the author’s word pending', 'b646'))),
    ('G-CURRENTS-UNEDITED', 'the current versions -- ERRATA, SPIRAL_MAP, README, REGISTRY, the census at v0.4 to v0.7, v5.18, the sieve -- against 93cfd59',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'a', b'b', b'a')}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes', lambda S: not any(S['nd_pub'].values()),
     lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the census at v0.7.1, the description and every byte the act appends to the ledgers: no outside collection named',
     lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads, none written: main, tags, branches and status against the face; SIDE-global-section`s tracked files unchanged',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-kernel': ['0000000', {}, [], '']}))),
    ('G-SORRY-TOKENS', 'the explicit-formula kernel`s main, comments stripped: no sorry token', lambda S: S['sorry_tokens'] == 0,
     lambda S: put(S, 'sorry_tokens', 1)),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'][0] == '36352a0' and S['te'][2] == '',
     lambda S: put(S, 'te', ('x', 'y', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b644_record.py'): S['tooltext'].get(os.path.join(T, 'b644_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-ROUTE-HELD', 'this act`s tools: the route reads, deletes a replaced file and uploads to the draft; no publish call', lambda S: route_held(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at a0791790, by blob id, the roots file and the glossary read by their own arms', lambda S: S['prior_n'] > 0 and S['prior_bad'] == [],
     lambda S: put(S, 'prior_bad', ['data/x'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers, the two pages, the census at v0.7.1 and the seven companions', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['SPIRAL_MAP.md'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-UNMOVED', 'the suite`s own regeneration against the table before it: no row added or gone and no grade cell moved', lambda S: S['table_changed'] == [],
     lambda S: put(S, 'table_changed', [['x']])),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present on disk, in no relay commit of any branch, not in the index, untracked', lambda S: local_ok(S),
     lambda S: put(S, 'local_log', 'abc1234')),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 7)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b644')" in S['suite'] and "'data/b644_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b644_closing.py: the closing sentence in the rule`s words with the plain reads named', lambda S: closing_sentence_ok(S),
     lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author in any ' + 'outbound request', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, read after every other arm has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
]


def regenerate():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def seal():
    """### (R246)(3): the sha256 of every sealed tool, recorded at the seal; refuses before the face is locked or once recorded."""
    import time
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b644_seal_hashes.json')
    if lock is None:
        print('### THE FACE IS NOT LOCKED -- NOTHING RECORDED')
        return 3
    if os.path.exists(p):
        print('### THE HASHES ARE RECORDED ALREADY -- NOTHING RECORDED TWICE')
        return 3
    now = sealed_now()
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), lock=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock)), tools=now,
             relay_head=gs(ROOT, 'rev-parse', 'HEAD'))
    b = (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    for t in K.SEALED:
        print('  %-22s %s' % (t, now[t]))
    print('  written: b644_seal_hashes.json')
    return 0


def main():
    import time
    if SEAL:
        return seal()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b644 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources()
    S['pushed'] = pushed
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID) else regenerate()
    if RERUN:
        d = jl('terminal_table_diff.json')
        S['table_changed'] = [list(x) for x in (d.get('changed') or [])] + [list(x) if isinstance(x, list) else [x] for x in (d.get('added') or []) + (d.get('gone') or [])]
    elif not (PRERUN or MID):
        S['table_changed'] = ([list(x) for x in (gen_diff.get('changed') or [])] + [list(x) if isinstance(x, list) else [x] for x in
                                                                                    (gen_diff.get('added') or []) + (gen_diff.get('gone') or [])]) \
            if rc_gen == 0 and 'changed' in gen_diff else None
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    av = S['ar_verify']
    rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    rec('  ### the hinges the recount marks: %d ; the chain`s reads at commit, b644: %s ; the shared files additive: %s' % (
        sum(1 for r in S['hj'].get('rows') or [] if r.get('hinge')), S['ar_reads'].get('b644') or 'not rooted',
        all(rc == [] for _p, _h, rc in S['additive'])))
    rec('  %-46s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 98)
    fail, defective, negfail, EX = [], [], 0, {}
    for name, reads, pred, pos in ARMS:
        if name == 'G-ARMS-NO-LIVE-LIMB':
            S['no_live_limb'] = not defective
        try:
            live = bool(pred(S))
        except Exception as e:
            live = False
            rec('  ### %s raised %s: %s' % (name, type(e).__name__, str(e)[:160]))
        try:
            neg = bool(pred(copy.copy(S)))
        except Exception:
            neg = False
        try:
            m = pos(copy.copy(S))
            posv = bool(pred(m)) if isinstance(m, dict) else False
        except Exception:
            posv = False
        if not live:
            fail.append(name)
        if neg != live:
            negfail += 1
        if posv:
            defective.append(name)
        EX[name] = dict(live=live, neg=neg, pos=posv, reads=reads)
        rec('  %-46s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else 'FAIL', 'PASS' if posv else 'FAIL',
                                           'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else '### FAILS')))
    rec('')
    rec('  ### tracked files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                          if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this run, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if not (RERUN or PRERUN or MID):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), (gen_diff.get('changed') or '')[:20]))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b644_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b644_checks_postpush.txt' if pushed else 'b644_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b644_arms_prerun.txt', 'b644_lsr_prerun.json').replace('b644_checks', 'b644_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b644_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
