# -*- coding: utf-8 -*-
"""b637_checks.py -- THE SUITE OF b637, UNDER (R247): THE BINDER GRAMMAR -- THE E0 RULE AS A TOTAL FUNCTION OVER A FINITE CLASSIFICATION,
NAMES REMOVED FROM THE READING, BOTH READERS RERUN OVER BOTH KERNELS, THE 20 UNNAMED ROWS READ BY CLASS; UPSTREAM ROWS AS KIND; THE ROSTER.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b637_checks.txt before the push and
### data/b637_checks_postpush.txt after it; `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is
### sealed, no table regenerated, its counts written to data/b637_arms_prerun.txt.
### ### THE SEAL'S HASH ARM ((R246)(3), OPEN_TRAILS :13307): `--seal`, run at the seal, records the sha256 of every sealed tool
### (tools/b637_worklist.py SEALED) in data/b637_seal_hashes.json and runs no arm; G-SEAL-HASHES recomputes each at every later run.
### ### Every remote is read once per run (OPEN_TRAILS :12703); G-LSREMOTE-ONE-PER-REPO runs last. The act-root chain is verified
### inside this suite alone. No arm reads a mirror: this act builds none.
### ### The harness is b568's to b636's, carried from tools/b636_checks.py; the sources, predicates and arms are b637's.
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
import b637_worklist as K     # noqa: E402

NL = chr(10)
PP, EF = K.PP, K.EF
GS = 'D:/SIDE-global-section'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b637_registration_2026-10-07.txt')
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
STEPZERO_RELAY = (K.STEPZERO,)    # ### relay's step-zero commits before the lock: b636's push-out and its first attempt
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
INST = ('b636_checks.py', 'b636_record.py', 'b636_closing.py', 'b636_tests.py', 'b636_worklist.py', 'b635_record.py', 'b634_elab.py',
        'test_elab_reader_b634.py', 'b634_record.py', 'b633_record.py', 'b633_census.py', 'b632_record.py', 'test_closing_headline_b634.py',
        'test_chain_page_b635.py', 'test_terminal_table_b635.py', 'test_terminal_table_b636.py', 'test_name_patterns_b636.py',
        'test_registry_tags_b636.py', 'mirror_build.ps1', 'mirror_verify.py', 'mirror_roster.json', 'b604_record.py', 'b602_record.py',
        'b566_record.py', 'b565_record.py', 'b616_record.py', 'b616_claims.py', 'b558_record.py', 'e0_rule.py', 'test_e0_rule.py',
        'test_e0_existential.py', 'chain_page.py', 'g_chain_page.py', 'test_chain_page.py', 'test_g_chain_page.py', 'test_chain_page_b596.py',
        'test_chain_page_b592.py', 'test_chain_page_b629.py', 'test_chain_page_b630.py', 'test_chain_page_b632.py', 'test_terminal_table_b630.py',
        'test_record_findings_b632.py', 'banned_terms.py', 'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py',
        'push_gated.sh', 'test_push_gated.sh', 'act_root.py', 'test_act_root.py', 'corr_row.py')
# ### the instrument edits the ruling orders, each committed alone with its tests: per tool, the file set each commit touching it may carry
RULE_COMMIT = ['tools/e0_rule.py', 'tools/test_e0_existential.py', 'tools/test_e0_rule.py']
GEN_COMMIT = ['tools/terminal_table.py', 'tools/test_terminal_table_b637.py']
ROSTER_COMMIT = ['tools/mirror_roster.json']
DECLARED_EDITS = {'e0_rule.py': [RULE_COMMIT], 'test_e0_rule.py': [RULE_COMMIT], 'test_e0_existential.py': [RULE_COMMIT],
                  'terminal_table.py': [GEN_COMMIT], 'mirror_roster.json': [ROSTER_COMMIT]}
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b637')
            and 'data/b637_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
                            (EF, 'SIDE-explicit-formula', K.EF_PIN), (K.SEC, 'SIDE-structural-error-correction', K.SEC_PIN)):
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
    import b637_record as REC
    import b616_record as R6
    import e0_rule as E
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b637_lockgate_notes*.txt')))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b637_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    table = jl('terminal_table.json')
    try:
        roster_now = json.loads(read(os.path.join(ROOT, *K.ROSTER.split('/'))))
    except Exception:
        roster_now = {}
    S = dict(
        REC=REC, E=E, face=face, ferry=rd('b637_ferry.txt'), scan=rd('b637_ferry_scan.txt'), cens=rd('b637_census_stepzero.txt'),
        fcens=rd('b637_faces_census_stepzero.txt'), pins0=rd('b637_pins_stepzero.txt'), procs=rd('b637_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b636_closing.txt'), reads=rd('b637_reads.txt'), branches=rd('b637_branches.txt'), answers=rd('b637_author_answers.txt'),
        prerun=rd('b637_arms_prerun.txt'), rl=jl('b637_record_lines.json'), tests=jl('b637_tests_stepzero.json'), testst=rd('b637_tests_stepzero.txt'),
        stepzero_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', STEPZERO_RELAY[-1], 'tools/').split(NL)
                              if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b637_seal_hashes.json'), sealnow=sealed_now(),
        ro=jl('b637_roster.json'), roster_now=roster_now, roster_pre=json.loads((blob(ROOT, '%s:%s' % (PRE['relay'], K.ROSTER)) or b'{}').decode('utf-8')),
        ck=jl('b637_binder_classes.json'), ckt=rd('b637_binder_classes.txt'),
        rt=jl('b637_rule_test.json'), et=jl('b637_existential_test.json'), rc=jl('b637_rule_control.json'), pr=jl('b637_planted_read.json'),
        rdiff=rd('b637_rule_diff.txt'), rr=jl('b637_rerun.json'), rrt=rd('b637_rerun.txt'),
        gt=jl('b637_gen_test.json'), gen_src=read(os.path.join(T, 'terminal_table.py')), treg=jl('b637_table_regen.json'),
        pm=jl('b637_premises.json'), cc=jl('b637_census_counts.json'),
        tblj=jl('b637_table_final.json'), table=table,
        table_pre=json.loads((blob(ROOT, '%s:data/terminal_table.json' % PRE['relay']) or b'{}').decode('utf-8')).get('rows') or [],
        closing_src=read(os.path.join(T, 'b637_closing.py')),
        local_present=os.path.exists(local),
        local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK),
        local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        pj={k: jl('b637_page_%s.json' % k) for k in ('zeta', 'chi')}, arms=rd('b637_page_arms.txt'),
        arj=jl('b637_act_root.json'), arj0=jl('b636_act_root.json'), art=rd('b637_act_root.txt'), rootsf=rd('act_roots.txt'),
        rpush=rd('b637_root_push_out.txt'), ppush=rd('b637_pp_root_push_out.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        touch={f: [files_of(ROOT, h) for h in gs(ROOT, 'log', '--format=%h', PRE['relay'] + '..HEAD', '--', 'tools/' + f).split(NL) if h.strip()] for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in REC.CURRENTS},
        pages={p: tri(PP, p, PRE['pp']) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b637_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        ker_main=gs(EF, 'rev-parse', 'main'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        kbranches={l.split()[0]: l.split()[1] for l in gs(EF, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b636*') for r in ('D:/relay', PP, EF)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b637_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b637_mustnotexist.txt')), table_changed=None,
        fj=jl('b637_findings.json'), tj=jl('b637_trail.json'), sc=jl('b637_scores.json'), desk=rd('b637_desk_notes.txt'),
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
    S['rfiles'] = {h: files_of(ROOT, h) for h, _s, _t in S['rlog']}
    S['pp_files'] = {h: files_of(PP, h) for h, _s, _t in S['plog']}
    S['pp_subj'] = {h: s for h, s, _t in S['plog']}
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['gs_diff'] = sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip()))
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b637_', 'audit_b637_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [rd('act_roots.txt')]
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


def live_binders(S):
    """### every binder of both kernels' rows, the table at f3a2f6b2's statements and both elaborated banks, classed by the LIVE rule:
    ### RETURN (binders read, binders reaching no class); (0, 0) where the live rule has no grammar."""
    E = S['E']
    if not hasattr(E, 'binders_of'):
        return 0, 0
    REC = S['REC']
    n = bad = 0
    for r in S['table_pre']:
        if r['repo'] not in K.KERNELS:
            continue
        kind, head = REC._textual_head(r.get('statement'))
        heads = [head] if kind == 'theorem' else []
        e = TT.elab_bank(os.path.join(D, K.KERNELS[r['repo']]['bank'])).get(r['name'])
        if e and not e.get('missing') and e['kind'] == 'theorem':
            heads.append(REC._elab_head(e))
        for h in heads:
            for b in E.binders_of(h):
                n += 1
                bad += not b['cls']
    return n, bad


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import b626_record as R26
    import b627_record as R27
    import act_root as AR
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, K.NODES['zeta']), os.path.join(SP, '_b637_gcp'), os.path.join(D, K.PROBE['zeta']))
    X['gcp_chi'] = GCP.arm(os.path.join(D, K.NODES['chi']), os.path.join(SP, '_b637_gcp'), os.path.join(D, K.PROBE['chi']))
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
            d = os.path.join(SP, '_b637_frozen')
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
        X['live_binders'] = live_binders(S)
    except Exception as e:
        X['live_binders'] = (0, -1)
        print('  ### live binders raised %s: %s' % (type(e).__name__, str(e)[:160]))
    try:
        X['planted_live'] = S['REC']._planted_reads(S['E']) if hasattr(S['E'], 'binders_of') else []
    except Exception:
        X['planted_live'] = []
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
    i = t.find(S['REC'].TRAIL_HEAD)
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


def rline(S, i):
    x = (S['rl'].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need):
    x = rline(S, i)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b637 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    blocks = re.split(r'^### CALL ', a, flags=re.M)[1:]
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    if not m:
        return False
    return int(m.group(1)) == len(heads) and all(x >= 2 for x in per) and len(per) == len(heads) \
        and len(blocks) == a.count('RESULT (transcript line') and '### NO RESULT' not in a \
        and all(S['REC'].answer_of(i) != 'no answer banked' for i in range(len(heads)))


def tests_ok(S):
    """### the test files tracked at the step-zero commit, every one run with the lists in force (b632's lists, b635's probes); every
    ### one clean; the reader's test's first run, stopped by the runner's carried limit, kept as its attempt."""
    j = S['tests']
    names = S['stepzero_tests']
    nf = sorted(n for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == names and nf == [] and len(names) == 27 \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 0' % (len(names), len(names))) in S['testst'] \
        and j['test_chain_page.py']['args'][:2] == ['b632_nodes_zeta.txt', 'b635_probe_out_zeta.txt'] \
        and 'timed out after 580 seconds' in rd('b637_tests_stepzero_attempt1.txt')


def answered_edits(S):
    out = {}
    for x in (jl('b637_answered_edits.json').get('edits') or []):
        if isinstance(x.get('prompt'), int) and S['REC'].answer_of(x['prompt']) != 'no answer banked':
            out.setdefault(x['tool'], []).append(sorted(x.get('files') or []))
    return out


def instruments_ok(S):
    allowed = dict((k, list(v)) for k, v in DECLARED_EDITS.items())
    for k, v in answered_edits(S).items():
        allowed.setdefault(k, []).extend(v)
    for f, (pre, now, head) in S['inst'].items():
        if pre is None:
            return False
        if pre == now:
            continue
        if f not in allowed or now != head:
            return False
        if not S['touch'].get(f) or any(sorted(fs) not in [sorted(a) for a in allowed[f]] for fs in S['touch'][f]):
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
    """### the relay commits since the act began whose file set is exactly `files`."""
    return [h for h, fs in S['rfiles'].items() if sorted(fs) == sorted(files)]


def roster_ok(S):
    """### (R247)(5): the roster on disk -- the old list a prefix, the three current editions appended, each tracked in PLACE-papers; the
    ### superseded versioned files kept; the builder unedited; the edit committed alone; its bank."""
    old, new = S['roster_pre'].get('files') or [], S['roster_now'].get('files') or []
    ro = S['ro']
    return bool(old) and new[:len(old)] == old and new[len(old):] == list(K.ROSTER_ADD) and bool(commit_of(S, ROSTER_COMMIT)) \
        and ro.get('appended') == list(K.ROSTER_ADD) and all((ro.get('tracked') or {}).get(f) for f in K.ROSTER_ADD) \
        and ro.get('builder_edited') is False and S['inst']['mirror_build.ps1'][0] == S['inst']['mirror_build.ps1'][1]


BINDERINFO = ('src/lean/Lean/Expr.lean:71:inductive BinderInfo where', 'src/lean/Lean/Expr.lean:73:  | default', 'src/lean/Lean/Expr.lean:75:  | implicit',
              'src/lean/Lean/Expr.lean:77:  | strictImplicit', 'src/lean/Lean/Expr.lean:79:  | instImplicit')


def kinds_ok(S):
    """### Lean's binder kinds printed in the classes bank from each toolchain's source, file and line."""
    t = S['ckt']
    return all(t.count(x) == 2 for x in BINDERINFO) and all(v in t for v in K.TOOLCHAINS.values())


def classes_ok(S):
    """### the classes bank: the record tool's table, the planted file on disk its sha, every class one planted declaration, the bank written
    ### before the rule's commit."""
    ck = S['ck']
    REC = S['REC']
    pf = raw(ck.get('planted_file') or '')
    at = iso_epoch(ck.get('at') or '')
    rc = [t for h, s, t in S['rlog'] if h in commit_of(S, RULE_COMMIT)]
    return bool(ck) and [c['id'] for c in ck.get('classes') or []] == [c[0] for c in REC.CLASSES] and len(ck['classes']) == len(REC.CLASSES) \
        and pf is not None and hashlib.sha256(pf).hexdigest() == ck.get('planted_sha256') \
        and sorted(p['cls'] for p in ck.get('planted') or [] if p['test'] == 'class') == sorted(c[0] for c in REC.CLASSES) \
        and at is not None and bool(rc) and all(at < t for t in rc)


def rule_ok(S):
    """### (R247)(4)(ii): the live rule -- its binder pattern without the name prefix, grade() reading no pattern by name, a binder reaching
    ### no class raising, its class table the bank's; committed alone with its tests; its diff banked; its test passing."""
    E, ck = S['E'], S['ck']
    pat = getattr(getattr(E, 'BINDER', None), 'pattern', '')
    import inspect
    try:
        src = inspect.getsource(E.grade)
    except Exception:
        src = ''
    rt = S['rt']
    return ('(h' + '\\w*)') not in pat and 'BINDER.finditer' not in src and hasattr(E, 'BinderUnclassed') and hasattr(E, 'binders_of') \
        and [list(c) for c in getattr(E, 'CLASSES', [])] == [[c['id'], c['kind'], c['typing'], c['form'], c['outcome']] for c in ck.get('classes') or []] \
        and bool(commit_of(S, RULE_COMMIT)) and '### lines removed' in S['rdiff'] \
        and rt.get('rc') == 0 and rt.get('cases', 0) >= 26 + len(S['REC'].CLASSES) and rt.get('passing') == rt.get('cases') \
        and S['et'].get('rc') == 0 and S['et'].get('passing') == S['et'].get('cases') == 7


def control_ok(S):
    """### the extended tests against the rule as it stood: the rule's test fails on new cases, printed."""
    runs = S['rc'].get('runs') or []
    r = [x for x in runs if x['test'].endswith('test_e0_rule.py')]
    return bool(r) and len(r[0]['failing']) > 0 and r[0]['cases'] == S['rt'].get('cases')


def planted_ok(S):
    """### the planted set read by the live rule equals the bank, every class as wanted, the no-class control raising, the five names one
    ### reading."""
    pr, live = S['pr'], S['planted_live']
    rows = pr.get('rows') or []
    key = lambda xs: [(x['decl'], x['got_cls'], x['got_grade']) for x in xs]   # noqa: E731
    return bool(rows) and key(rows) == key(live) and all(x['ok'] for x in rows) and pr.get('sha_equal') is True and pr.get('table_equal') is True \
        and len(set(tuple(x) for x in pr.get('five') or [])) == 1 and len(pr.get('five') or []) == len(K.FIVE_NAMES)


def rerun_ok(S):
    """### the rerun bank against the live rule's own count over both kernels: the binders it reads, none reaching no class."""
    rr = S['rr']
    n, bad = S['live_binders']
    return bool(rr) and n > 0 and bad == 0 and sum((rr.get('binders') or {}).values()) == n and not rr.get('bugs') \
        and all(set(k) <= {K.EF_KERNEL, K.SEC_KERNEL} for k in [rr.get('kernels') or {}])


def moves_ok(S):
    """### every grade move of the rerun printed with its class and reader."""
    mv = S['rr'].get('moves') or []
    return bool(S['rr']) and all(m.get('reader') and (m['classes'] or not m['grade_moved']) for m in mv) \
        and S['rr'].get('grade_moves') == sum(1 for m in mv if m['grade_moved'])


def unnamed_ok(S):
    U = S['rr'].get('unnamed') or []
    return len(U) == 20 and sorted(x['id'] for x in U) == ['U%02d' % i for i in range(1, 21)] and all(x.get('binders') is not None for x in U)


def _h(S, k, want):
    got = (S['sc'].get(k) or [''])[0]
    return got.split(',')[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % got) in S['desk']


def h_ok(S, k):
    """### H71a-H71d recomputed from the banks, against the scores and the desk."""
    rr, pr = S['rr'], S['pr']
    if k == 'H71a':
        ok = planted_ok(S) and rerun_ok(S)
    elif k == 'H71b':
        ok = len(set(tuple(x) for x in pr.get('five') or [])) == 1 and len(pr.get('five') or []) == len(K.FIVE_NAMES)
    elif k == 'H71c':
        ok = bool(rr) and rr.get('graded', 0) > 0 and rr.get('grade_moves', 0) / rr['graded'] <= K.H71C_BOUND and moves_ok(S)
    else:
        ok = unnamed_ok(S) and all(x['taken'] for x in rr.get('unnamed') or [])
    return _h(S, k, 'HOLDS' if ok else 'REFUTED')


def upstream_keys(rows):
    return set((r['repo'], r['name']) for r in rows if r.get('mark') == 'upstream' or (r['repo'] == K.EF_KERNEL and r['name'] in K.MATHLIB_FIVE))


def gen_ok(S):
    """### (R247)(2): the generator's upstream exclusion; its test passing; the two committed alone."""
    t = S['gt']
    return ("r['kind'] = " + "'upstream'") in S['gen_src'] and t.get('rc') == 0 and t.get('cases', 0) >= 4 \
        and t.get('passing') == t.get('cases') and bool(commit_of(S, GEN_COMMIT))


def table_up_ok(S):
    """### the table on disk: every row the upstream mark reaches at f3a2f6b2 and the five Mathlib names a kind -- grade —, kind upstream,
    ### provenance none -- and no other row of that kind."""
    rows = S['table'].get('rows') or []
    want = upstream_keys(S['table_pre'])
    up = [r for r in rows if r.get('kind') == 'upstream']
    return bool(want) and set((r['repo'], r['name']) for r in up) == want and all(r['grade'] == '—' and r.get('provenance') == 'none' for r in up)


def regen_ok(S):
    """### the regeneration bank: exit 0, every move caused by the rewritten rule or the upstream exclusion, the counts before and after
    ### the exclusion printed."""
    t = S['treg']
    return bool(t) and t.get('rc') == 0 and 'other' not in set((t.get('causes') or {}).values()) and bool(t.get('counts_after_excluded')) \
        and t.get('upstream') == len(upstream_keys(S['table_pre']))


def premises_ok(S):
    p = S['pm']
    return bool(p) and len(p.get('old') or {}) == 42 and bool(p.get('rule_heads')) and 'unnamed' in p and bool(p.get('by_class'))


def census_ok(S):
    c = S['cc']
    return bool(c) and c.get('upstream') == len(upstream_keys(S['table_pre'])) and c.get('rows') == len(S['table'].get('rows') or []) \
        and S['currents'][K.CEN5][0] == S['currents'][K.CEN5][1]


def pages_ok(S):
    for k in ('zeta', 'chi'):
        j, pg = S['pj'][k], K.PNAME[k]
        a, b, c = S['pages'][pg]
        com = [h for h, fs in S['pp_files'].items() if pg in fs]
        order = [h for h, _s, _t in S['plog'] if h in com]
        if not j or j.get('rc') != 0:
            return False
        if j.get('changed') or com:
            if not (com and all(S['pp_files'][h] == [pg] for h in com) and all('correction' in S['pp_subj'][h].lower() for h in order[1:])
                    and c is not None and hashlib.sha256(c).hexdigest() == j.get('sha256') and a == c):
                return False
        elif a != b:
            return False
    return True


def table_final_ok(S):
    t = S['tblj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('grade_moved')


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('PASSING : 2 of 2.**') in t.split('PAGE ARMS PASSING : 2 of 2.**')[-1]


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 14 and rows[13][:3] == ['b637', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it]


def midpush_ok(S):
    heads = (S['arj'].get('reads') or {}).get('heads') or {}
    m1 = re.search(r'push_gated: main read back at the remote: (\w+)', S['rpush'])
    m2 = re.search(r'push_gated: main read back at the remote: (\w+)', S['ppush'])
    return bool(m1 and m2) and heads.get('relay') == m1.group(1) and heads.get('PLACE-papers') == m2.group(1) \
        and heads.get('SIDE-explicit-formula') == S['ker_main']


def verify_ok(S):
    v = S['ar_verify'] or []
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 638)] and all(x[1] == 'AGREE' for x in v)


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


ENTRY_NEEDLES = ('**The classification**', '**The rule**', '**The rerun**', '**The table and the premises**', '**The mirror’s roster**',
                 '**The record lines**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b638')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The binder grammar: ') \
        and all(x in tail for x in ENTRY_NEEDLES)


def wl_ok(S):
    extra = [f for v in answered_edits(S).values() for fs in v for f in fs]
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) or f[len('relay/'):] in extra for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0].split(',')[0] in ('HELD', 'REFUTED', 'NOT SCORABLE', 'HOLDS', 'PENDING') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def kernels_untouched(S):
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and len(f) == 11 and all(k in n and n[k] == f[k] for k in f) and all(n[k][0].startswith(v) for k, v in S['REC'].KERN_PIN.items()) \
        and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') and S['gs_diff'] == []


def corpus_scope(S):
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if any(K.PNAME[k] in f for f in S['pp_files'].values())]
    return S['pp_changed'] == sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages))


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


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


READ_NEEDLES = ('OPEN_TRAILS.md @ 142c3152', 'FINDINGS.md @ 142c3152', 'tools/e0_rule.py @ f3a2f6b2', 'tools/test_e0_rule.py @ f3a2f6b2',
                'data/b634_elab_types.txt @ f3a2f6b2', 'data/elab_types.txt @ f3a2f6b2', 'data/b636_elab_sec.txt @ f3a2f6b2',
                'data/b634_unnamed_rows.txt @ f3a2f6b2', 'data/terminal_table.json @ f3a2f6b2', 'THE_KEYSTONE_CENSUS_v0_5.md @ 142c3152',
                'tools/mirror_roster.json @ f3a2f6b2', 'tools/mirror_build.ps1 @ f3a2f6b2', 'data/b636_closing_push_out.txt @ 746e32f4',
                'data/b636_closing_push_out_attempt1.txt @ 746e32f4', ':13002 ', ':12955 ', ':13221 ', ':11864 ', ':12228 ', ':12354 ',
                ':12356 ', ':12799 ', ':13167 ', ':13333 ', ':7801 ', 'src/lean/Lean/Expr.lean:71:inductive BinderInfo where',
                '### the local intake bank`s state: ?? data/b628_intake_crank_v0_5.txt')


def prompts_banked(S):
    return len(re.findall(r'^### PROMPT ', S['answers'], re.M))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R247) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + NL + ' 11 22 lean.exe  lean x')),
    ('G-STEPZERO-TESTS', 'the step-zero test bank against the 27 test files tracked at the step-zero commit: every one clean, the lists in force passed, the first run`s limit refusal kept as its attempt',
     lambda S: tests_ok(S), lambda S: put(S, 'stepzero_tests', S['stepzero_tests'] + ['test_x.py'])),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit in relay and PLACE-papers', lambda S: S['lock_epoch'] is not None
     and all(t > S['lock_epoch'] for h, s, t in S['rlog'] if h[:8] not in STEPZERO_RELAY) and all(t > S['lock_epoch'] for h, s, t in S['plog']),
     lambda S: put(put(S, 'lock_epoch', 4 * 10 ** 9), 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b636`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b636' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the two logs before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [h[:8] for h, s, t in S['rlog'] if t <= S['lock_epoch']] == list(STEPZERO_RELAY)
     and [h for h, s, t in S['plog'] if t <= S['lock_epoch']] == [],
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-R247-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R247) END' in S['ferry'] and S['ot'].count('**(R247) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R247) ratified', '**(R2470) ratified'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'] and 'NO SUCH BLOB' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'].replace(':13167 ', ':13166 '))),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompt headers, each prompt`s options, each call`s result, every answer read back by the record tool',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('prompt(s)', 'prompts'))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and 'PRE-SEAL (R202)(3) READING' in S['prerun'] and ('ARMS RUN : %d.' % len(ARMS)) in S['prerun']
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 10 ** 12) < S['lock_epoch'],
     lambda S: put(S, 'prerun', S['prerun'].replace('PRE-SEAL', 'POST-SEAL'))),
    ('G-PUSHOUT-COMMITTED', 'relay 746e32f4`s files', lambda S: S['pushout'][0] == ['data/b636_closing_push_out.txt', 'data/b636_closing_push_out_attempt1.txt']
     and S['pushout'][1], lambda S: put(S, 'pushout', ([], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b636') == 6, lambda S: put(S, 'push_lists', {'x': 'push-b636'})),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(v) for b, v in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'dedekind-b631': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80, every PLACE-papers read at ba5f0ea and the E0 rule`s blob at 12c15c80',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] + '-E0-12C15C80' == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(x, ok=False) for x in S['ctl']])),
    (FROZEN_ARM, 'b622`s lists with every relay read at 84bae29a, the E0 rule`s and the generator`s blobs at 84bae29a, against the pages at 52822a5',
     lambda S: len(S['old_frozen']) == 2 and all(x.get('rc') == 0 and x.get('equal') is True for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [dict(x, equal=False) for x in S['old_frozen']])),
    ('G-INSTRUMENTS-UNEDITED', 'b636`s tools, the reader, the census modules, the shared tools, the rule and its tests, the generators and their tests, the roster, the seal, the gates, act_root.py and the row writer against f3a2f6b2, changed only by the ordered edits, each committed alone with its tests',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'chain_page.py': (b'a', b'b', b'b')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', None, None))),
    ('G-SEAL-HASHES', 'the sealed tools` sha256 recorded at the seal (data/b637_seal_hashes.json) against the tools on disk, agree or differ per tool',
     lambda S: seal_hashes_ok(S), lambda S: put(S, 'sealnow', dict(S['sealnow'], **{K.SEALED[0]: '0' * 64}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b636`s weight, its figures from its banks', lambda S: landed(S, 0, ('(:7801)', '61 of 61', '76d0eab9', '3cb13712', 'f3a2f6b2')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=[dict(rline(S, 0), line=1)] + (S['rl'].get('lines') or [])[1:]))),
    ('G-UPSTREAM-LINE', 'OPEN_TRAILS at the banked line: the upstream clause beneath the criterion, standing', lambda S: landed(S, 1, ('(:12955)', 'riemannZeta₀', 'kind upstream', 'provenance none')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=[rline(S, 0), dict(rline(S, 1), line=1)] + (S['rl'].get('lines') or [])[2:]))),
    ('G-NAME-LINE', 'OPEN_TRAILS at the banked line: the name clause beneath the criterion, standing', lambda S: landed(S, 2, ('(:12955)', 'no part of its reading', 'H : TailHyp')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[:2] + [dict(rline(S, 2), line=1)]))),
    ('G-ROSTER', 'the roster on disk against f3a2f6b2: the three current editions appended, the old list a prefix, each tracked, the builder unedited, the edit committed alone; its bank',
     lambda S: roster_ok(S), lambda S: put(S, 'roster_now', dict(S['roster_now'], files=(S['roster_now'].get('files') or [])[:-1]))),
    ('G-BINDER-KINDS', 'the classes bank: Lean`s BinderInfo constructors printed from each toolchain`s source, file and line', lambda S: kinds_ok(S),
     lambda S: put(S, 'ckt', S['ckt'].replace('|' + ' strictImplicit', '| strict'))),
    ('G-CLASSES-BANKED', 'the classes bank and the planted file: the class table, one planted declaration per class, the file`s sha, the bank written before the rule`s commit',
     lambda S: classes_ok(S), lambda S: put(S, 'ck', dict(S['ck'], planted_sha256='0' * 64))),
    ('G-RULE-REWRITTEN', 'the live rule: no name prefix, grade() reading no pattern by name, a binder reaching no class raising, its class table the bank`s; committed alone with its tests; its diff and tests banked',
     lambda S: rule_ok(S), lambda S: put(S, 'rt', dict(S['rt'], passing=0))),
    ('G-RULE-CONTROL', 'the extended test against the rule as it stood: its new cases failing there, printed', lambda S: control_ok(S),
     lambda S: put(S, 'rc', dict(runs=[dict(x, failing=[]) for x in S['rc'].get('runs') or []]))),
    ('G-PLANTED-READ', 'the planted set read by the live rule against the bank: every class as wanted, the no-class control raising, the five names one reading',
     lambda S: planted_ok(S), lambda S: put(S, 'planted_live', [dict(x, got_grade='DERIVES') for x in S['planted_live']])),
    ('G-RERUN-BINDERS', 'the rerun bank against the live rule over both kernels` statements and banks: every binder classed, the counts equal',
     lambda S: rerun_ok(S), lambda S: put(S, 'live_binders', (S['live_binders'][0], 1))),
    ('G-RERUN-MOVES', 'the rerun bank: every grade move printed with its class and its reader, the count its own', lambda S: moves_ok(S),
     lambda S: put(S, 'rr', dict(S['rr'], grade_moves=(S['rr'].get('grade_moves') or 0) + 1))),
    ('G-UNNAMED-CLASSED', 'the rerun bank: the 20 unnamed rows, each printed with its binders` classes', lambda S: unnamed_ok(S),
     lambda S: put(S, 'rr', dict(S['rr'], unnamed=(S['rr'].get('unnamed') or [])[:-1]))),
] + [('G-%s-SCORED' % k.upper(), '%s recomputed from its banks, against the scores and the desk' % k, (lambda kk: lambda S: h_ok(S, kk))(k),
      (lambda kk: lambda S: _sc(S, kk))(k)) for k in ('H71a', 'H71b', 'H71c', 'H71d')] + [
    ('G-GENERATOR-UPSTREAM', 'tools/terminal_table.py`s upstream exclusion; its test passing; the two committed alone', lambda S: gen_ok(S),
     lambda S: put(S, 'gt', dict(S['gt'], passing=0))),
    ('G-TABLE-UPSTREAM', 'the table on disk: the upstream rows of f3a2f6b2 and the five Mathlib names a kind, grade —, provenance none, and no other',
     lambda S: table_up_ok(S), lambda S: put(S, 'table', dict(S['table'], rows=[dict(r, grade='DERIVES') if r.get('kind') == 'upstream' else r
                                                                               for r in (S['table'].get('rows') or [])]))),
    ('G-TABLE-REGEN', 'the regeneration bank: exit 0, every move by the rewritten rule or the exclusion, the counts before and after the exclusion',
     lambda S: regen_ok(S), lambda S: put(S, 'treg', dict(S['treg'], causes=dict(S['treg'].get('causes') or {}, x='other')))),
    ('G-PREMISES-RECOMPUTED', 'the premises bank: the census`s 42 read and the heads recomputed beside them, the binder-class table and the unnamed rows',
     lambda S: premises_ok(S), lambda S: put(S, 'pm', dict(S['pm'], old={}))),
    ('G-CENSUS-COUNTS', 'the census-counts bank: the upstream rows and the table`s rows counted, the census at v0.5 unedited',
     lambda S: census_ok(S), lambda S: put(S, 'cc', dict(S['cc'], upstream=-1))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b632`s list and b635`s probe against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b632`s list and b635`s probe against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank: both page arms and the frozen control', lambda S: arms_ok(S['arms']),
     lambda S: put(S, 'arms', S['arms'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-PAGES-COMMITTED', 'each page: its bank exit 0; changed and committed alone at its banked digest, its later commits corrections, or unchanged and in no commit',
     lambda S: pages_ok(S), lambda S: put(S, 'pj', dict(S['pj'], zeta=dict(S['pj']['zeta'], rc=9)))),
    ('G-TABLE-FINAL', 'the final table bank: no grade moved and no row gone at the last regeneration', lambda S: table_final_ok(S),
     lambda S: put(S, 'tblj', dict(S['tblj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s b637 line, the root bank and its items: previous b636`s root, the root`s repository list at PLACE-papers HEAD, the file a true prefix extension',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b637 x y' + NL)),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay and PLACE-papers heads against the read-backs of the pushes before it, the explicit-formula kernel at its main',
     lambda S: midpush_ok(S), lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed by this suite, one remote read per repository: b624 to b637 AGREE', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', [(a, 'DISAGREE', w) for a, v, w in S['ar_verify']])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line, the entry read to the next heading', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous', lambda S: bool(S['arj'])
     and ('**Act root:** b637 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-TERMINALS', 'this act`s trail record: the next act named without a kernel terminal', lambda S: 'b638 names no kernel terminal' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b638 names no kernel terminal', 'x'))),
    ('G-TRAIL-CARRIES-SEAL', 'this act`s trail record: every sealed tool agreeing at the record', lambda S: all(
        ('%s agree' % t_) in trail(S) for t_ in K.SEALED), lambda S: put(S, 'ot', S['ot'].replace('%s agree' % K.SEALED[0], '%s differ' % K.SEALED[0]))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the prompts, counted from the answers bank', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and ('**Prompts to the author:** %d ' % prompts_banked(S)) in trail(S) and 'no answer banked' not in trail(S),
     lambda S: put(S, 'answers', S['answers'] + NL + '### PROMPT 9 (x): y')),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b638 on the author’s word' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b638 on the author’s word', 'b639'))),
    ('G-CURRENTS-UNEDITED', 'the current versions, README, the census at v0.4 and v0.5, REGISTRY, ERRATA, SPIRAL_MAP, v5.18 and the sieve on disk and at HEAD against 142c315',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'a', b'b', b'a')}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the ledger appends, its banks, its tools, the roots file',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads, none written: main, tags by peel, branches and status against the face; SIDE-global-section unchanged',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-kernel': ['0000000', {}, [], '']}))),
    ('G-SORRY-TOKENS', 'the explicit-formula kernel`s main, comments stripped: no sorry token', lambda S: S['sorry_tokens'] == 0,
     lambda S: put(S, 'sorry_tokens', 1)),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('x', 'y', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b637_record.py'): S['tooltext'].get(os.path.join(T, 'b637_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                                if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at f3a2f6b2, by blob id, the roots file read by G-ACTROOT-BANKED', lambda S: S['prior_n'] > 0 and S['prior_bad'] == [],
     lambda S: put(S, 'prior_bad', ['data/x'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers and the pages where they moved', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['README.md'])),
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
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs and the answered edits` files', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b637')" in S['suite'] and "'data/b637_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b637_closing.py: the closing sentence in the rule`s words, the carried words absent', lambda S: closing_sentence_ok(S),
     lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author in any ' + 'outbound request', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, the act-root arm`s included, read after every other arm has run (OPEN_TRAILS :12703)',
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
    p = os.path.join(D, 'b637_seal_hashes.json')
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
    print('  written: b637_seal_hashes.json')
    return 0


def main():
    import time
    if SEAL:
        return seal()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b637 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources()
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
    rec('  ### the live rule`s binders over both kernels: %d read, %d reaching no class' % S['live_binders'])
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
        out = os.path.join(D, 'b637_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b637_checks_postpush.txt' if pushed else 'b637_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b637_arms_prerun.txt', 'b637_lsr_prerun.json').replace('b637_checks', 'b637_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b637_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
