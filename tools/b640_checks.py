# -*- coding: utf-8 -*-
"""b640_checks.py -- THE SUITE OF b640, UNDER (R250): THE PREMISE STATUS SPLIT TO FIVE AND THE OPEN PREMISES GIVEN WORK-ORDERS; THE DEPOSIT
DESCRIPTION'S ASSUMPTION SECTION RECOMPOSED; A SECOND READER FOR LEGIBILITY; THE DRAFT 23228113 UPDATED AND HELD AT THE SAME PROMPT.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### b639's defects (d) and (e) repaired in their sources: the answers arm admits a call returned unanswered as banked unanswered; the files
### arm reads each kind by its label as written.
### ### The harness is b568's to b639's, carried from tools/b639_checks.py by slicing (its helpers and its runner, b639's name made b640's); the
### sources, predicates and arms are b640's.
"""
import collections
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
import b640_worklist as K     # noqa: E402

NL = chr(10)
PP, EF = K.PP, K.EF
GS = 'D:/SIDE-global-section'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b640_registration_2026-10-08.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs='17ce9ff')
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd', 'platt-b626': 'e939c92',
        'cite-b628': '98b7668', 'nb-b629': 'aa17442', 'dedekind-b631': '8c51431'}
STEPZERO = K.STEPZERO
STEPZERO_RELAY = (K.STEPZERO[:8],)
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
INST = ('b639_checks.py', 'b639_record.py', 'b639_closing.py', 'b639_tests.py', 'b639_worklist.py', 'b639_reg_gate.py', 'b639_regspec.py',
        'b638_checks.py', 'b638_record.py', 'b637_record.py', 'b635_record.py', 'b633_record.py', 'b632_record.py', 'b616_record.py', 'b616_claims.py',
        'b602_record.py', 'b566_record.py', 'e0_rule.py', 'test_e0_rule.py', 'test_e0_existential.py', 'chain_page.py', 'g_chain_page.py',
        'test_chain_page.py', 'test_g_chain_page.py', 'test_chain_page_b596.py', 'test_chain_page_b638.py', 'banned_terms.py', 'terminal_table.py',
        'table_gate.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'test_push_gated.sh', 'act_root.py', 'test_act_root.py', 'corr_row.py',
        'mirror_build.ps1', 'mirror_verify.py', 'mirror_roster.json', 'b575_zenodo.py', 'b576_zenodo.py', 'test_elab_reader_b634.py')
COUNT_CASE = r'^  \(\d+\) '


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b640')
            and 'data/b640_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def sources():
    import b640_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b640_lockgate_notes*.txt')))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b640_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    S = dict(
        REC=REC, face=face, ferry=rd('b640_ferry.txt'), scan=rd('b640_ferry_scan.txt'), cens=rd('b640_census_stepzero.txt'),
        fcens=rd('b640_faces_census_stepzero.txt'), pins0=rd('b640_pins_stepzero.txt'), procs=rd('b640_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b639_closing.txt'), reads=rd('b640_reads.txt'), branches=rd('b640_branches.txt'), answers=rd('b640_author_answers.txt'),
        prerun=rd('b640_arms_prerun.txt'), rl=jl('b640_record_lines.json'), tests=jl('b640_tests_stepzero.json'), testst=rd('b640_tests_stepzero.txt'),
        stepzero_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', STEPZERO, 'tools/').split(NL)
                              if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b640_seal_hashes.json'), sealnow=sealed_now(),
        psj=jl('b640_premise_status.json'), pst=rd('b640_premise_status.txt'), ps_tool=read(os.path.join(ROOT, K.STATUS_TOOL)),
        ps_test=jl('b640_status_test.json'), wo=jl('b640_workorders.json'),
        dsj=jl('b640_description_scan.json'), desc=raw(os.path.join(D, K.DESC)), desc9=raw(os.path.join(D, K.B639_DESC)),
        flj=jl('b640_deposit_files.json'), rpk=rd('b640_reader_packet.txt'), rcj=jl('b640_reader_compare.json'),
        reader_dir=os.path.isdir(K.READER_DIR) and sorted(os.listdir(K.READER_DIR)),
        zj=jl('b640_zenodo.json'), tblj=jl('b640_table_final.json'),
        closing_src=read(os.path.join(T, 'b640_closing.py')),
        local_present=os.path.exists(local),
        local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK),
        local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        pj={k: jl('b640_page_%s.json' % k) for k in ('zeta', 'chi')}, arms=rd('b640_page_arms.txt'),
        arj=jl('b640_act_root.json'), arj0=jl('b639_act_root.json'), art=rd('b640_act_root.txt'), rootsf=rd('act_roots.txt'),
        rpush=rd('b640_root_push_out.txt'), ppush=rd('b640_pp_root_push_out.txt'), lastpp=rd('b640_c6_pp_push_out.txt'),
        mj=jl('b640_mirror.json'), mbj=jl('b640_mirror_build.json'), mirror_zip=os.path.exists(K.MIRROR_ZIP),
        absent=tri(PP, ABSENT, PRE['pp']),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        ps_commits=[(h, files_of(ROOT, h)) for h in gs(ROOT, 'log', '--format=%h', PRE['relay'] + '..HEAD', '--', K.STATUS_TOOL).split(NL) if h.strip()],
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        pages={p: tri(PP, p, PRE['pp']) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b640_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        ker_main=gs(EF, 'rev-parse', 'main'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        kbranches={l.split()[0]: l.split()[1] for l in gs(EF, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b639*') for r in ('D:/relay', PP, EF)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b640_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b640_mustnotexist.txt')), table_changed=None,
        fj=jl('b640_findings.json'), tj=jl('b640_trail.json'), sc=jl('b640_scores.json'), desk=rd('b640_desk_notes.txt'),
        lsr=None, word=REC._word(),
        token_logged=[f for f in os.listdir(D) if f.startswith('b640_') and os.path.isfile(os.path.join(D, f)) and REC._tok() and REC._tok().encode() in open(os.path.join(D, f), 'rb').read()]
        + [f for f in os.listdir(T) if f.startswith('b640_') and REC._tok() and REC._tok().encode() in open(os.path.join(T, f), 'rb').read()]
        + (['the session transcript'] if REC._tok() and os.path.exists(REC.SESSION) and REC._tok().encode() in open(REC.SESSION, 'rb').read() else []),
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files()
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    S['rfiles'] = {h: files_of(ROOT, h) for h, _s, _t in S['rlog']}
    S['pp_files'] = {h: files_of(PP, h) for h, _s, _t in S['plog']}
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['gs_diff'] = sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip()))
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b640_', 'audit_b640_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pk = os.path.join(D, 'b640_reader_packet')
    if os.path.isdir(pk):
        pub += [read(os.path.join(pk, f)) for f in os.listdir(pk)]
    pub += [read(f) for f in tools] + [rd('act_roots.txt'), S['ps_tool']]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES or p == 'data/act_roots.txt':
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S.update(extra_sources(S))
    return S


CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md', K.CEN5, K.CEN6,
            K.MONO, K.SIEVE6)


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import b626_record as R26
    import b627_record as R27
    import act_root as AR
    import b638_record as R8
    X = {}
    for k in ('zeta', 'chi'):
        lp = os.path.join(D, K.NODES[k])
        try:
            X['gcp_' + k] = GCP.arm(lp, os.path.join(SP, '_b640_gcp'), os.path.join(D, K.PROBE[k]))
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
            d = os.path.join(SP, '_b640_frozen')
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
    except Exception as e:
        X['ar_verify'] = [('raised', type(e).__name__, [])]
    X['sorry_tokens'] = S['REC'].sorry_tokens('main')
    try:
        X['gloss_block'] = CP.glossary_block()
    except Exception as e:
        X['gloss_block'] = ['raised %s' % type(e).__name__]
    X['page_text'] = {k: cr0(blob(PP, 'HEAD:' + K.PNAME[k])).decode('utf-8', 'replace') if blob(PP, 'HEAD:' + K.PNAME[k]) else '' for k in ('zeta', 'chi')}
    X['gl_pages'] = {k: R8.glossary_lines(X['page_text'][k]) for k in ('zeta', 'chi')}
    try:
        X['desc_recomposed'] = S['REC'].compose()[0].encode('utf-8')
    except BaseException as e:
        X['desc_recomposed'] = ('raised %s' % type(e).__name__).encode('utf-8')
    X['files_now'] = files_now(S)
    try:
        import premise_status as PS
        X['reclass'] = [(x['head'], PS.classify5(dict(upstream=x['upstream'], domain_vars=x['domain_vars'], consumed=x['consumed'], inline=x['inline'],
                                                      standalone=x['standalone'], cited=x['cited']))[0], x['status']) for x in S['psj'].get('heads') or []]
    except Exception as e:
        X['reclass'] = [('raised', type(e).__name__, '')]
    return X


def files_now(S):
    out = {}
    for x in S['flj'].get('files') or []:
        b = raw(x['source']) if x.get('commit') is None else blob(PP, '%s:%s' % (x['commit'], x['source']))
        out[x['name']] = hashlib.sha256(b).hexdigest() if b is not None else None
    return out


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
    """### the answers bank as it prints: its count line against its prompt headers, each prompt's options, each call's result, every answer read
    ### back by the record tool -- a call returned unanswered by the author (its result the harness's rejection) admitted as banked unanswered,
    ### its prompts read 'no answer banked' and none other (b639's defect (d), repaired in the source)."""
    a = S['answers']
    m = re.search(r'^### b640 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    blocks = re.split(r'^### CALL ', a, flags=re.M)[1:]
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    if not m:
        return False
    unanswered = []
    i = 0
    for b in blocks:
        n = len(re.findall(r'^### PROMPT \d+ \(', b, re.M))
        if UNANSWERED in b:
            unanswered += list(range(i, i + n))
        i += n
    return int(m.group(1)) == len(heads) and all(x >= 2 for x in per) and len(per) == len(heads) \
        and len(blocks) == a.count('RESULT (transcript line') and '### NO RESULT' not in a \
        and all((S['REC'].answer_of(k) != 'no answer banked') == (k not in unanswered) for k in range(len(heads)))


def tests_ok(S):
    j = S['tests']
    names = S['stepzero_tests']
    nf = sorted(n for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == names and nf == [] and len(names) == 29 \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 0' % (len(names), len(names))) in S['testst'] \
        and j['test_chain_page.py']['args'][:2] == ['b638_nodes_zeta.txt', 'b635_probe_out_zeta.txt']


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
    later = [t for h, s, t in S['rlog'] if h[:8] not in STEPZERO_RELAY]
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at and all(at <= t for t in later) \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


def commit_of(S, files):
    return [h for h, fs in S['rfiles'].items() if sorted(fs) == sorted(files)]


def status_tool_ok(S):
    """### the shared status tool: created by the carry, then extended by one edit, each commit alone; its test passing, one planted head per
    ### outcome at least; its five-status rule present."""
    c = S['ps_commits']
    t = S['ps_test']
    return len(c) == 2 and all(fs == [K.STATUS_TOOL] or sorted(fs) == sorted([K.STATUS_TOOL, K.STATUS_TEST]) for _h, fs in c) \
        and any(fs == [K.STATUS_TOOL] for _h, fs in c) and 'def classify5(' in S['ps_tool'] and "STATUSES5 = ('DOMAIN'" in S['ps_tool'] \
        and t.get('rc') == 0 and t.get('passing') == t.get('cases') and t.get('cases', 0) >= 5


def status5_ok(S):
    j = S['psj']
    hs = j.get('heads') or []
    four = j.get('four') or {}
    return len(hs) == 50 and len(set(x['head'] for x in hs)) == 50 and all(x['status'] in K.STATUSES5 for x in hs) \
        and sorted(four) == sorted(K.MATHLIB_FOUR) and all(v == 'DOMAIN' for v in four.values()) and sum(x['rule'] for x in hs) == 123 \
        and S['reclass'] and all(a == b for _h, a, b in S['reclass']) and j.get('h74a') == 'HOLDS' \
        and all(('%s ' % x['head']) in S['pst'] for x in hs) and S['pst'].count('salt-check column:') == 50


def workorders_ok(S):
    w = S['wo']
    op = [x['head'] for x in S['psj'].get('heads') or [] if x['status'] == 'OPEN']
    o = oline(S, w.get('line'))
    t = S['ot'][S['ot'].find(o):] if o else ''
    named = [h for h in op if (h in K.CARRIED_WO and K.CARRIED_WO[h][0] in t) or ('**%s**' % S['REC'].wo_name(h)) in t]
    return bool(o) and o.startswith(poss(S['REC'].WO_HEAD)) and sorted(named) == sorted(op) and len(op) > 0 and w.get('h74b') == 'HOLDS' \
        and 'its count field the open part' in t and 'its ef field cited' in t


def description_ok(S):
    d, j = S['desc'], S['dsj']
    return bool(d) and d == S['desc_recomposed'] and j.get('sha256') == hashlib.sha256(d).hexdigest() and j.get('clean') is True \
        and j.get('undefined') == [] and j.get('markup') == [] and not any((j.get('nd') or {}).values()) and j.get('undeclared') == 0 \
        and not re.search('[’‘“”]', d.decode('utf-8')) and K.NO_CLAIM.encode() in d


def files_ok(S):
    """### the draft's file bank (b639's, the zip replaced): 14 files, each kind read as its label is written (b639's defect (e), repaired), every
    ### sha256 equal to its source bytes re-read now."""
    fl = S['flj'].get('files') or []
    kinds = collections.Counter(next((k for k in ('REPLACED', 'INHERITED', 'ADDED') if x['kind'].startswith(k)), x['kind']) for x in fl)
    return len(fl) == 14 and kinds == {'REPLACED': 9, 'INHERITED': 2, 'ADDED': 3} and all(x['sha256'] for x in fl) \
        and all(S['files_now'].get(x['name']) == x['sha256'] for x in fl) and sum(1 for x in fl if x.get('replaces')) == 1


def packet_ok(S):
    return bool(S['rpk']) and 'THE HOLD, verbatim: %s' % S['REC'].READER_PROMPT in S['rpk'] and S['REC'].READER_PROMPT in S['answers'] \
        and S['reader_dir'] and 'packet' in S['reader_dir'] and 'full_prompt.txt' in S['reader_dir'] \
        and os.path.exists(os.path.join(D, 'b640_reader_packet', 'description.txt')) and "{'method': 0, 'tree': 0, 'modules': 0}" in S['rpk']


def compare_ok(S):
    j = S['rcj']
    return bool(j) and isinstance(j.get('agree'), int) and len(j.get('answers') or {}) == 3 and all(v.get('answer') for v in (j.get('answers') or {}).values()) \
        and os.path.exists(os.path.join(D, 'b640_reader_answers.txt'))


def mirror_ok(S):
    m, b = S['mj'], S['mbj']
    rb = re.search(r'push_gated: main read back at the remote: (\w+)', S['lastpp'])
    upd = ((S['zj'].get('update') or {}).get('at')) or ''
    rows = [l.split() for l in S['rootsf'].split(NL) if l.strip()]
    b639 = next((r[1] for r in rows if r[0] == 'b639'), None)
    return bool(m) and bool(b) and m.get('clean') is True and m.get('files') == K.ROSTER_FILES and m.get('census6') is True \
        and m.get('root_line') == 'Act root: b639 %s' % b639 and bool(rb) and b.get('pp_head') == rb.group(1) and S['mirror_zip'] \
        and not any((m.get('nd') or {}).values()) and S['inst']['mirror_build.ps1'][0] == S['inst']['mirror_build.ps1'][1] \
        and bool(upd) and (m.get('at') or 'z') < upd


def draft_ok(S):
    z = S['zj']
    up, rd_ = z.get('update') or {}, z.get('read') or {}
    return up.get('failed') == 0 and len(up.get('calls') or []) == 3 and rd_.get('get') == 200 and str(rd_.get('id')) == K.DRAFT \
        and rd_.get('title') == K.TITLE and rd_.get('version') == K.VERSION and rd_.get('submitted') is False


def prompt_ok(S):
    rd_ = S['zj'].get('read') or {}
    return bool(rd_) and (S['REC'].PROMPT % (rd_.get('id'), rd_.get('n_files', 0))) in S['answers'] and S['word'] in ('publish', 'hold')


def word_ok(S):
    z = S['zj']
    pub = z.get('publish') or {}
    if S['word'] == 'hold':
        return not pub and bool(z.get('hold'))
    return S['word'] == 'publish' and bool(pub)


def pages_ok(S):
    for k in ('zeta', 'chi'):
        j, (disk, pre, head) = S['pj'][k], S['pages'][K.PNAME[k]]
        if not j or j.get('rc') != 0 or j.get('cells_moved'):
            return False
        if j.get('changed'):
            if head is None or hashlib.sha256(head).hexdigest() != j.get('sha256') or not any(fs == [K.PNAME[k]] for fs in S['pp_files'].values()):
                return False
        elif not (disk == pre == head):
            return False
    return True


def gl_pages_ok(S):
    gb = S['gloss_block']
    return isinstance(gb, list) and bool(gb) and all(S['gl_pages'][k] == gb for k in ('zeta', 'chi'))


def table_final_ok(S):
    t = S['tblj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('grade_moved')


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('PASSING : 2 of 2.**') in t.split('PAGE ARMS PASSING : 2 of 2.**')[-1]


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 17 and rows[16][:3] == ['b640', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it] \
        and any(it.startswith('data/b640_zenodo_read.txt ') for it in j.get('items') or [])


def midpush_ok(S):
    heads = (S['arj'].get('reads') or {}).get('heads') or {}
    m1 = re.search(r'push_gated: main read back at the remote: (\w+)', S['rpush'])
    m2 = re.search(r'push_gated: main read back at the remote: (\w+)', S['ppush'])
    return bool(m1 and m2) and heads.get('relay') == m1.group(1) and heads.get('PLACE-papers') == m2.group(1) \
        and heads.get('SIDE-explicit-formula') == S['ker_main']


def verify_ok(S):
    v = S['ar_verify'] or []
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 641)] and all(x[1] == 'AGREE' for x in v)


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The status at five**', '**The work-orders**', '**The description**', '**The second reader**', '**The draft**',
                 '**The record lines**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b641')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The premise status at five: ') and all(x in tail for x in ENTRY_NEEDLES)


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0].split(',')[0].split(' ')[0] in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def h_ok(S, k):
    got = (S['sc'].get(k) or [''])[0]
    rd_, rc = (S['zj'].get('read') or {}), S['rcj']
    want = {'H74a': S['psj'].get('h74a'), 'H74b': S['wo'].get('h74b'), 'H74c': ('HOLDS' if rc.get('agree') == 3 else 'REFUTED') if rc else 'PENDING',
            'H74d': ('HOLDS' if rd_.get('h74d') else 'REFUTED') if rd_ else 'PENDING'}[k]
    return bool(got) and got == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % got) in S['desk']


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def route_only(S):
    lib = 'urllib' + '.request'
    carriers = sorted(os.path.basename(f) for f, t in S['tooltext'].items() if lib in t)
    rt = S['tooltext'].get(os.path.join(T, 'b640_record.py'), '')
    return carriers == ['b640_record.py'] and ('R9.http' in rt) and ('urlopen' not in rt) \
        and not [f for f, t in S['tooltext'].items() if ('ZENODO' + '_TOKEN') in t]


def kernels_untouched(S):
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and len(f) == len(S['REC'].KERNS_READ) and all(k in n and n[k] == f[k] for k in f) \
        and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') and S['gs_diff'] == []


def corpus_scope(S):
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if any(K.PNAME[k] in f for f in S['pp_files'].values())]
    return S['pp_changed'] == sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages))


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author in any ' + 'outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and ('the route' + '`s requests to zenodo') in t and (', no ' + 'outbound request,') not in t


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


READ_NEEDLES = ('data/b639_premise_status.txt @ be1a4105', 'data/b639_deposit_description.txt @ be1a4105', 'OPEN_TRAILS.md @ 0fede2d0',
                'FINDINGS.md @ 0fede2d0', 'tools/e0_rule.py @ be1a4105', 'data/b639_closing_push_out.txt @ 6e33ccdc', 'tools/b639_record.py @ be1a4105',
                'tools/b632_record.py @ be1a4105', ':12955 ', ':12839 ', ':12863 ', ':13223 ', ':13395 ', ':13397 ', ':13399 ', ':13427 ', ':10257 ',
                ':10608 ', ':12887 ', ':7885 ', 'THE USE SITES', 'THE READER`S STAGING PATTERN', '### the local intake bank`s state: ?? data/b628_intake_crank_v0_5.txt')


def prompts_banked(S):
    return len(re.findall(r'^### PROMPT ', S['answers'], re.M))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R250) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + NL + ' 11 22 lean.exe  lean x')),
    ('G-STEPZERO-TESTS', 'the step-zero test bank against the 29 test files tracked at the step-zero commit: every one clean, b638`s lists in force',
     lambda S: tests_ok(S), lambda S: put(S, 'stepzero_tests', S['stepzero_tests'] + ['test_x.py'])),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit in relay and PLACE-papers', lambda S: S['lock_epoch'] is not None
     and all(t > S['lock_epoch'] for h, s, t in S['rlog'] if h[:8] not in STEPZERO_RELAY) and all(t > S['lock_epoch'] for h, s, t in S['plog']),
     lambda S: put(put(S, 'lock_epoch', 4 * 10 ** 9), 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b639`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b639' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the two logs before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [h[:8] for h, s, t in S['rlog'] if t <= S['lock_epoch']] == list(STEPZERO_RELAY)
     and [h for h, s, t in S['plog'] if t <= S['lock_epoch']] == [],
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-R250-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R250) END' in S['ferry'] and S['ot'].count('**(R250) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R250) ratified', '**(R2500) ratified'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'] and 'NO SUCH BLOB' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'].replace(':12955 ', ':12954 '))),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints, a call returned unanswered admitted as banked unanswered (b639`s (d) repaired)',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('prompt(s)', 'prompts'))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and 'PRE-SEAL (R202)(3) READING' in S['prerun'] and ('ARMS RUN : %d.' % len(ARMS)) in S['prerun']
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 10 ** 12) < S['lock_epoch'],
     lambda S: put(S, 'prerun', S['prerun'].replace('PRE-SEAL', 'POST-SEAL'))),
    ('G-PUSHOUT-COMMITTED', 'relay 6e33ccdc`s files', lambda S: S['pushout'][0] == ['data/b639_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', ([], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b639') == 8, lambda S: put(S, 'push_lists', {'x': 'push-b639'})),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(v) for b, v in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'dedekind-b631': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80, every PLACE-papers read at ba5f0ea and the E0 rule`s blob at 12c15c80',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] + '-E0-12C15C80' == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(x, ok=False) for x in S['ctl']])),
    (FROZEN_ARM, 'b622`s lists with every relay read at 84bae29a, the E0 rule`s and the generator`s blobs at 84bae29a, against the pages at 52822a5',
     lambda S: len(S['old_frozen']) == 2 and all(x.get('rc') == 0 and x.get('equal') is True for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [dict(x, equal=False) for x in S['old_frozen']])),
    ('G-INSTRUMENTS-UNEDITED', 'b639`s and b638`s tools, the readers, the shared tools, the rule and its tests, the generators and their tests, the roster, the builder and verifier, act_root.py, the row writer and the earlier route tools against be1a4105',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'terminal_table.py': (b'a', b'b', b'b')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', None, None))),
    ('G-SEAL-HASHES', 'the sealed tools` sha256 recorded at the seal against the tools on disk', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{K.SEALED[0]: '0' * 64}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b639`s weight, its figures from its banks, the reading of (R250)(2)',
     lambda S: landed(S, 0, ('(:7885)', '23228113', 'v1.2.0', 'WHY THE DESCRIPTION HELD', 'IsOpen', 'concrete witness')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=[dict(rline(S, 0), line=1)] + (S['rl'].get('lines') or [])[1:]))),
    ('G-FIVE-CLAUSE-LINE', 'OPEN_TRAILS at the banked line: the five-status clause beneath the criterion, the letter corrected to the author`s answers',
     lambda S: landed(S, 1, ('(:12955)', 'DOMAIN', 'DISCHARGED', 'CITED', 'WITNESSED', 'OPEN', 'read from the use site', 'premise_status.py')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=[rline(S, 0), dict(rline(S, 1), line=1)]))),
    ('G-STATUS-TOOL', 'tools/premise_status.py: carried, then extended by one edit, each committed alone; its test passing with a planted head per outcome',
     lambda S: status_tool_ok(S), lambda S: put(S, 'ps_test', dict(S['ps_test'], passing=0))),
    ('G-PREMISE-STATUS5', 'the status bank: 50 heads, each one of five statuses recomputed by the live rule from its banked facts; the four Mathlib predicates DOMAIN; the rule rows 123; the salt-check column on every head',
     lambda S: status5_ok(S), lambda S: put(S, 'psj', dict(S['psj'], four=dict(S['psj'].get('four') or {}, Prime='OPEN')))),
    ('G-WORKORDERS', 'OPEN_TRAILS at the banked line: one work-order per open premise or its cross-reference, EpsteinPremises` fields named; zero without',
     lambda S: workorders_ok(S), lambda S: put(S, 'wo', dict(S['wo'], line=1))),
    ('G-DESCRIPTION', 'the description bank against its recomposition, byte for byte; no undeclared change; straight quotes; the note carrying that no claim is added or withdrawn; its scan clean',
     lambda S: description_ok(S), lambda S: put(S, 'desc_recomposed', (S['desc_recomposed'] or b'') + b' ')),
    ('G-FILES-BANK', 'the draft`s file bank: 14 files read by their labels as written (b639`s (e) repaired), every sha256 equal to its source now, the zip replaced',
     lambda S: files_ok(S), lambda S: put(S, 'files_now', dict(S['files_now'], **{'ERRATA.md': '0' * 64}))),
    ('G-READER-PACKET', 'the packet staged off D:\\ and banked, the no-disclosure arm at 0, the hold verbatim in the answers bank',
     lambda S: packet_ok(S), lambda S: put(S, 'reader_dir', [])),
    ('G-READER-COMPARE', 'the reader`s three answers banked and compared to the description`s sentences', lambda S: compare_ok(S),
     lambda S: put(S, 'rcj', dict(S['rcj'], answers={}))),
    ('G-MIRROR', 'the mirror built after the act`s last PLACE-papers push and before the draft`s update by the unedited builder: clean, 74 files, the census at v0.6 in it, the root line b639`s',
     lambda S: mirror_ok(S), lambda S: put(S, 'mj', dict(S['mj'] or {}, census6=False))),
    ('G-DRAFT-UPDATED', 'the route`s bank: the update`s three calls clean, the draft read back unsubmitted with the record`s title and version',
     lambda S: draft_ok(S), lambda S: put(S, 'zj', dict(S['zj'], update=dict(S['zj'].get('update') or {}, failed=1)))),
    ('G-PROMPT-VERBATIM', 'the answers bank: the deposit prompt verbatim with the draft`s identifier and file count, and the author`s word',
     lambda S: prompt_ok(S), lambda S: put(S, 'answers', S['answers'].replace('Publishing is yours', 'Publishing is mine'))),
    ('G-WORD-BEFORE-PUBLISH', 'the route`s bank and the answers: a publication only on the word publish; on hold, the hold bank and nothing published',
     lambda S: word_ok(S), lambda S: put(S, 'word', 'publish' if S['word'] == 'hold' else 'hold')),
    ('G-TOKEN-UNLOGGED', 'every bank and tool of this act and this session`s transcript, searched for the token`s string', lambda S: S['token_logged'] == [],
     lambda S: put(S, 'token_logged', ['data/b640_x.txt'])),
] + [('G-%s-SCORED' % k.upper(), '%s recomputed from its banks, against the scores and the desk' % k, (lambda kk: lambda S: h_ok(S, kk))(k),
      (lambda kk: lambda S: _sc(S, kk))(k)) for k in ('H74a', 'H74b', 'H74c', 'H74d')] + [
    ('G-PAGES-COMMITTED', 'each page re-emitted where a cell moves, committed alone; an unchanged page unmoved',
     lambda S: pages_ok(S), lambda S: put(S, 'pj', dict(S['pj'], zeta=dict(S['pj']['zeta'] or {}, rc=9)))),
    ('G-GLOSSARY-ON-PAGES', 'the glossary block on both pages at PLACE-papers HEAD against the live generator`s block', lambda S: gl_pages_ok(S),
     lambda S: put(S, 'gl_pages', dict(S['gl_pages'], chi=(S['gl_pages']['chi'] or [''])[:-1]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b638`s list and b635`s probe against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b638`s list and b635`s probe against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank: both page arms and the frozen control', lambda S: arms_ok(S['arms']),
     lambda S: put(S, 'arms', S['arms'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-TABLE-FINAL', 'the final table bank: no grade moved and no row gone', lambda S: table_final_ok(S),
     lambda S: put(S, 'tblj', dict(S['tblj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s b640 line, the root bank and its items: previous b639`s root, the draft`s read-back among the banks',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b640 x y' + NL)),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay and PLACE-papers heads against the read-backs of the pushes before it', lambda S: midpush_ok(S),
     lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed by this suite, one remote read per repository: b624 to b640 AGREE', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', [(a, 'DISAGREE', w) for a, v, w in S['ar_verify']])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line, the entry read to the next heading', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD(), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous', lambda S: bool(S['arj'])
     and ('**Act root:** b640 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-TERMINALS', 'this act`s trail record: the next act named without a kernel terminal', lambda S: 'b641 names no kernel terminal' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b641 names no kernel terminal', 'x'))),
    ('G-TRAIL-CARRIES-SEAL', 'this act`s trail record: every sealed tool agreeing at the record', lambda S: all(
        ('%s agree' % t_) in trail(S) for t_ in K.SEALED), lambda S: put(S, 'ot', S['ot'].replace('%s agree' % K.SEALED[0], '%s differ' % K.SEALED[0]))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the prompts, counted from the answers bank', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and ('**Prompts to the author:** %d ' % prompts_banked(S)) in trail(S), lambda S: put(S, 'answers', S['answers'] + NL + '### PROMPT 9 (x): y')),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b641 on the author’s word' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b641 on the author’s word', 'b642'))),
    ('G-CURRENTS-UNEDITED', 'the current versions -- ERRATA, SPIRAL_MAP, README, REGISTRY, the census at v0.4, v0.5 and v0.6, v5.18 and the sieve -- against 0fede2d',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'a', b'b', b'a')}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the ledger appends, its banks, the packet, its tools, the roots file, the status tool',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads, none written: main, tags by peel, branches and status against the face; SIDE-global-section unchanged',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-kernel': ['0000000', {}, [], '']}))),
    ('G-SORRY-TOKENS', 'the explicit-formula kernel`s main, comments stripped: no sorry token', lambda S: S['sorry_tokens'] == 0,
     lambda S: put(S, 'sorry_tokens', 1)),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('x', 'y', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b640_record.py'): S['tooltext'].get(os.path.join(T, 'b640_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-ROUTE-ONLY', 'this act`s tools: the platform reached through b639`s request function alone, imported by the record tool',
     lambda S: route_only(S), lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at be1a4105, by blob id, the roots file read by its own arm', lambda S: S['prior_n'] > 0 and S['prior_bad'] == [],
     lambda S: put(S, 'prior_bad', ['data/x'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers and the pages where they moved', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['SPIRAL_MAP.md'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-UNMOVED', 'the suite`s own regeneration against the committed table: no row added or gone and no grade cell moved', lambda S: S['table_changed'] == [],
     lambda S: put(S, 'table_changed', [['x']])),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present on disk, in no relay commit of any branch, not in the index, untracked', lambda S: local_ok(S),
     lambda S: put(S, 'local_log', 'abc1234')),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b640')" in S['suite'] and "'data/b640_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b640_closing.py: the closing sentence in the rule`s words with the route`s requests named', lambda S: closing_sentence_ok(S),
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
    p = os.path.join(D, 'b640_seal_hashes.json')
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
    print('  written: b640_seal_hashes.json')
    return 0


def main():
    import time
    if SEAL:
        return seal()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b640 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### the status bank re-classed by the live rule, disagreements: %s ; the author`s word: %s ; the token found in: %s' % (
        [h for h, a, b in S['reclass'] if a != b] or 'NONE', S['word'], S['token_logged'] or 'NOTHING'))
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
        out = os.path.join(D, 'b640_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b640_checks_postpush.txt' if pushed else 'b640_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b640_arms_prerun.txt', 'b640_lsr_prerun.json').replace('b640_checks', 'b640_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b640_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
