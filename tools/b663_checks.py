# -*- coding: utf-8 -*-
"""b663_checks.py -- THE SUITE OF b663, UNDER (R273): b662 AT ITS WEIGHT; THE EPSTEIN RUNGS READ AND THE PLAN RAISED; THE Q0 CONFIGURATION
BUILT ON PREMISES; THE DETECTOR AND THE RATE INDEX AT THE REAL CONFIGURATION.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM:
### the runner's reading is read from the act's banks, written by the record tool from the run's id and its artifact's digest.
### ### (R264)(2), THE FREEZE: the standing arms are b662's face's (G2) arms less b662's own arms over b662's banks, carried; the act's own
### arms read this act's banks alone (tools/b663_worklist.py ACT_ARMS). The standing runner arms read this kernel's run (b659's form).
### ### The citation check is a gate step (standing from b662), read by G-CITATION-CHECKED; no new standing arm.
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b663_record.py).
### ### The harness is b568's to b662's (helpers, runner, seal), written by the Write tool from tools/b662_checks.py; the sources, predicates
### ### and arms over this act's banks are b663's. tools/e0_rule.py, edited by ruling at b663 (one MET line), is read by G-MET-WIDENED and
### ### is not among G-INSTRUMENTS-UNEDITED's tools.
"""
import copy
import fnmatch
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b616_claims as KC0     # noqa: E402
import b663_worklist as K     # noqa: E402
from b663_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b663_registration_2026-10-13.txt')
B662_FACE = os.path.join(D, 'b662_registration_2026-10-13.txt')
B662_ACT_ARMS = K.B662_ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = K.STEPZERO
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
INST = ('b662_checks.py', 'b662_closing.py', 'b662_tests.py', 'b662_worklist.py', 'b662_reg_gate.py', 'b662_regspec.py', 'b662_record.py',
        'b662_map.py', 'b662_citation.py',
        'b661_checks.py', 'b661_closing.py', 'b661_tests.py', 'b661_worklist.py', 'b661_reg_gate.py', 'b661_regspec.py', 'b661_record.py',
        'b661_map.py',
        'b659_checks.py', 'b659_closing.py', 'b659_tests.py', 'b659_worklist.py', 'b659_reg_gate.py', 'b659_regspec.py', 'b659_record.py',
        'b658_checks.py', 'b658_closing.py', 'b658_tests.py', 'b658_worklist.py', 'b658_reg_gate.py', 'b658_regspec.py', 'b658_record.py',
        'b647_record.py', 'test_msplit_b658.py',
        'b657_checks.py', 'b657_closing.py', 'b657_tests.py', 'b657_worklist.py', 'b657_reg_gate.py', 'b657_regspec.py', 'b657_record.py',
        'b656_checks.py', 'b656_closing.py', 'b656_tests.py', 'b656_worklist.py', 'b656_reg_gate.py', 'b656_regspec.py', 'b656_record.py',
        'b655_checks.py', 'b655_closing.py', 'b655_tests.py', 'b655_worklist.py', 'b655_reg_gate.py', 'b655_regspec.py', 'b655_record.py',
        'edit_route.py', 'test_edit_route_b646.py',
        'b654_checks.py', 'b654_closing.py', 'b654_tests.py', 'b654_worklist.py', 'b654_reg_gate.py', 'b654_regspec.py', 'b654_record.py',
        'b653_checks.py', 'b653_closing.py', 'b653_record.py', 'b652_record.py',
        'b651_record.py', 'b649_record.py', 'b648_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py',
        'test_licensed_table_b645.py', 'b643_record.py', 'b641_record.py', 'b633_record.py', 'b602_record.py', 'b616_record.py', 'b551_record.py',
        'b566_record.py', 'b569_record.py', 'b590_record.py', 'act_root.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py',
        'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py',
        'b616_claims.py', 'ferry_scan.py', 'build_watch.py', 'test_build_watch_b647.py', 'chain_page.py', 'axiom_claim.py',
        'licensed_table.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py', 'test_no_sorry_main.py',
        'test_axiom_claim.py', 'test_module_header.py', 'test_axiom_claim_b651.py', 'test_conversion_b652.py',
        'test_licensed_table_instrument_b652.py', 'test_chain_page_b638.py', 'b314_coldclone.py', 'test_composer_b647.py', 'test_composer_b649.py',
        'test_name_b649.py', 'b627_margin.py', 'b627_worklist.py')
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'day1/ONE_PAGE_PROOF.md',
            'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md')
TABLE_FILES = K.TABLE_FILES
WF = '.github/workflows/build-module.yml'
K_FILES = [WF, K.EPSTEIN_FILE, 'print_targets.txt']


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


def read_blob(repo, spec):
    b = blob(repo, spec)
    return b.decode('utf-8', 'replace').replace(chr(13), '') if b is not None else ''


def iso_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def utc_epoch(text, label):
    m = re.search(re.escape(label) + r'[^0-9]*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', text)
    return iso_epoch(m.group(1)) if m else None


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b663')
            and 'data/b663_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers)/[^`\s]+)`', w)))


def written_files():
    res = []
    for repo, name, pre in ((ROOT, 'relay', PRE['relay']), (PP, 'PLACE-papers', PRE['pp'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


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


def capture_now():
    import b663_record as REC
    return REC.capture()


def run_test(name):
    r = subprocess.run([sys.executable, os.path.join(T, name)], capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return dict(rc=r.returncode, out=r.stdout or '')


def live_arms():
    import no_sorry_main as NSM
    import axiom_claim as AC
    import module_header as MH
    names = NSM.kernels()
    t0 = time.time()
    nsm = NSM.run(names, KC0.remote_refs)
    t1 = time.time()
    idx, counts = AC.index()
    ac_rows, ac_per = AC.run(names, idx)
    t2 = time.time()
    mh_per, mh_rows = MH.run(names)
    t3 = time.time()
    return dict(names=names, nsm=nsm, ac=ac_rows, ac_counts=counts, mh=mh_rows, mh_per=mh_per, secs=(t1 - t0, t2 - t1, t3 - t2))


def conv_alone():
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to',
            'def ' + 'conv(']
    bad = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b663_') and f.endswith('.py'):
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b663_regspec as SPEC
    import b663_record as REC
    P = SPEC.planted()
    ctl = []
    for f in (lambda: REC.read_score_row('X9', 'HELD'), lambda: REC.read_instance(dict(run={}, rows=[])),
              lambda: REC.read_control_cell(dict(name='x', base=['0.8', '29.6'], certs=[], reading='NONE ≤ J_max'))):
        try:
            f()
            ctl.append(False)
        except Exception:
            ctl.append(True)
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def wf_state():
    t = read_blob(K.KD, 'main:' + WF)
    return {K.KERNEL: dict(text=t, commit_files=files_of(K.KD, K.K_WORKFLOW),
                           on_main=subprocess.run(['git', '-C', K.KD, 'merge-base', '--is-ancestor', K.K_WORKFLOW, 'main']).returncode == 0,
                           targets=[l.strip() for l in read_blob(K.KD, 'main:print_targets.txt').split(NL) if l.strip()])}


def merges_state():
    p = K.KD
    return {K.KERNEL: dict(main=gs(p, 'rev-parse', '--short=7', 'main'), parents=gs(p, 'log', '-1', '--format=%p', '--abbrev=7', 'main').split(),
                           built=K.RUN_REF[:7], tree_main=gs(p, 'rev-parse', 'main^{tree}'), tree_built=gs(p, 'rev-parse', K.RUN_REF + '^{tree}'),
                           tags=dict((t, gs(p, 'rev-parse', '--short=7', t + '^{commit}')) for t in gs(p, 'tag', '--points-at', 'main').split()))}


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted(set(g2_of(B662_FACE)) - set(B662_ACT_ARMS))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


def _branch_first_ct():
    """the commit time of the first commit on the instance branch beyond the kernel's main before the act."""
    ls = [l for l in gs(K.KD, 'log', '--reverse', '--format=%ct', '%s..%s' % (K.K_MAIN, K.RUN_REF)).split(NL) if l.strip()]
    return int(ls[0]) if ls else None


def _ct_first(repo, pre, prefix):
    for l in gs(repo, 'log', '--reverse', '--format=%ct %s', pre + '..HEAD').split(NL):
        if l.strip() and l.split(' ', 1)[1].startswith(prefix):
            return int(l.split(' ', 1)[0])
    return None


def sources():
    import b663_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b663_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b663_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    aj = jl('b663_author_answers.json').get('calls') or []
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b663_ferry.txt'), scan=rd('b663_ferry_scan.txt'), stepz=rd('b663_stepzero.txt'),
        readfirst=rd('b663_readfirst.txt'), defects=rd('b663_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b663_author_answers.txt'), answj=aj, prerun=rd('b663_arms_prerun.txt'), rl=jl('b663_record_lines.json'),
        rl2=jl('b663_record_lines_c2.json'), rl3=jl('b663_record_lines_c2b.json'),
        tests=jl('b663_tests_stepzero.json'), testst=rd('b663_tests_stepzero.txt'), rerun=jl('b663_tests_stepzero_rerun.json'),
        withheld=jl('b663_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b663_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), cmdj=jl('b663_commands.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b663_checks.py')),
        citation=rd(K.CITATION_BANK), c1_ct=_ct_first(ROOT, PRE['relay'], 'b663 Component 1'),
        plan=rd('b663_epstein_plan.txt'), domj=jl('b663_dominance.json'), domt=rd('b663_dominance.txt'), a0t=rd('b663_a0_list.txt'),
        branch_ct=_branch_first_ct(), instj=jl('b663_epstein_instance.json'), instt=rd('b663_epstein_instance.txt'),
        ctlj=jl('b663_epstein_control.json'), ctlt=rd('b663_epstein_control.txt'), mapdiff=rd('b663_map_diff.txt'),
        e0_now=cr0(raw(os.path.join(T, 'e0_rule.py'))), e0_pre=cr0(blob(ROOT, PRE['relay'] + ':tools/e0_rule.py')),
        met_before=rd('b663_tests_met_before.txt'), met_after=rd('b663_tests_met_after.txt'),
        standing=STANDING, wf=wf_state(), merges=merges_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b663_closing.py')), gate=rd('b663_reg_gate.txt'),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b663_act_root.json'), arj0=jl('b662_act_root.json'), art=rd('b663_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b663_kernels_face.json').get('kernels') or {}),
        push_lists={r: gs(r, 'branch', '-a', '--list', '*push-b662*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b663_mustnotexist.txt')),
        fj=jl('b663_findings.json'), tj=jl('b663_trail.json'), sc=jl('b663_scores.json'), desk=rd('b663_desk_notes.txt'), tfj=jl('b663_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['live'] = live_arms()
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files()
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    S['pp_changed'] = sorted(ch)
    S['ledger_adds'] = appended(S['fi_pre'], S['fi_now']) + NL + appended(S['ot_pre'], S['ot_now'])
    pub = [S['ledger_adds']]
    for f in sorted(os.listdir(D)):
        if f.startswith(('b663_', 'audit_b663_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [v['text'] for v in S['wf'].values()]
    pub += [read_blob(K.KD, 'main:' + f) for f in K_FILES]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    S['outside'] = [n for n in R41.OAI_NEEDLES if n in S['ledger_adds']]
    shared = set(ADD.shared_files())
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES or p in shared:
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
    import act_root as AR
    try:
        S['ar_verify'] = AR.verify(remote=KC0.remote_refs)
        S['ar_reads'] = dict(AR.READS_AT)
    except Exception as e:
        S['ar_verify'], S['ar_reads'] = [('raised', type(e).__name__, [])], {}
    S['order_slack'] = AR.ORDER_SLACK
    try:
        S['additive'] = ADD.check(worktree=True)
    except Exception as e:
        S['additive'] = [('raised', type(e).__name__, [('x', [])])]
    return S


def put(S, k, v):
    S[k] = v
    return S


def oline(S, n):
    ls = S['ot'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def fline(S, n):
    ls = S['find'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def rline(S, i, key='rl'):
    x = (S[key].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need, key='rl'):
    x = rline(S, i, key)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(conv(x.get('head', '\x00'))) and all(n in o for n in need)


def procs_ok(S):
    p = S['stepz']
    return 'names matching tail, lean, lake, python, bash' in p and 'read before any run: NONE' in p and 'Orphans: NONE' in p \
        and 'Read again after the test loop and the re-run ended: NONE' in p


STEPZERO_FAILING = {'test_asof.py': ['(7)'], 'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)'],
                    'test_g_chain_page.py': []}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    rr = S['rerun']
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 4' % (len(names), len(names) - 1)) in S['testst'] \
        and sorted(rr) == ['test_asof.py', 'test_g_chain_page.py'] and all(x['rc'] == 0 and not x['failing'] for x in rr.values())


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b663 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) >= 1 and all(x >= 2 for x in per) and len(res) == len(calls) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and '(Defects)' in a and '(Instance)' in a and '(E0 / landing)' in a


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def no_local_lean(S):
    import b663_record as REC
    return bool(S['cmds']) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and REC.local_lean(r['cmd'])]


def planted_ok(S, t, n, form='%d of %d cases as wanted -- PASS'):
    p = S['planted'][t]
    return p['rc'] == 0 and (form % (n, n) if '%d' in form else form) in p['out']


def nsm_hits(S):
    return [(r['kernel'], f, ln) for r in S['live']['nsm'] for f, ln, _t in r['hits']]


def no_sorry_main(S):
    rows = S['live']['nsm']
    return len(rows) == len(S['live']['names']) > 0 and all(r['equal'] for r in rows) and not nsm_hits(S)


def ac_count(rows, v):
    return sum(1 for r in rows if r['verdict'] == v)


def axiom_claim(S):
    rows = S['live']['ac']
    return bool(rows) and ac_count(rows, 'CONTRADICTED') == 0


def module_header(S):
    per = S['live']['mh_per']
    return len(per) == len(S['live']['names']) > 0 and sum(v['headers'] for v in per.values()) > 0 and S['live']['mh'] == []


# ================================================================== (R273)(1)-(3): THE READ-FIRST, THE CITATION CHECK, THE PLAN
READFIRST_NEEDLES = ('data/b662_closing.txt', 'data/b662_defects.txt', '(a) :9', '(h) :34', 'data/b642_epstein_rungs.txt', 'R5 :156',
                     'OPEN_TRAILS :13533', 'data/b326_epstein_zeros.json', 'data/b326_offline.json', 'data/b548_reads.txt :307',
                     'Schema/Config.lean :24', 'Schema/Instances.lean :25', 'Schema/RateIndexCfg.lean :135-:148', 'Schema/Converse.lean :161',
                     'Schema/Epstein.lean', 'tools/b662_map.py', 'cell :171-:341', 'data/b662_closing_push_out.txt', 'rows are')


def readfirst_ok(S):
    return all(x in S['readfirst'] for x in READFIRST_NEEDLES)


def branches_ok(S):
    z = ' '.join(S['stepz'].split())          # ### the bank hard-wraps through its needles; read with the whitespace collapsed
    return all(v == '' for v in S['push_lists'].values()) and 'deleted push-b662 (was 83306684)' in z \
        and 'deleted push-b662 (was 16be102)' in z and 'push-b662-closing (was 51838723)' in z \
        and 'docstrings-cut-SIDE-carrier-spec (was 55421a3)' in z and '[deleted]' in z


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def citation_ok(S):
    c = S['citation']
    m = re.search(r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    first = S['answj'][0] if S['answj'] else {}
    ans = iso_epoch((first.get('result_ts') or '')[:19] + 'Z')
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'RUN BEFORE THE FERRY IS BANKED' in c \
        and all(('    (%s) THE NAVIGATOR' % x) in S['defects'] for x in 'abcde') \
        and (int(m.group(3)) == 0 or (ans is not None and S['c1_ct'] is not None and ans < S['c1_ct']))


def plan_ok(S):
    p = S['plan']
    rows = ('R1 :4 ', 'R2 :18 ', 'R3 :37 ', 'R4 :56 ', 'R5 :156 ')
    return '### 1. THE RUNGS' in p and 'THIS ACT BUILDS NO RUNG' in p and all(r in p for r in rows) and '### 8. THE AUTHOR' in p \
        and 'LEAN MAY NOW BE WRITTEN, ON THE AUTHOR' in p and 'b326_offline.json' in p and 'B1, A NAMED READ PREMISE' in p \
        and 'NO SOURCE LINE; ITS REASON' in p and 'listed points` own A₀ = 1' in S['a0t']


def plan_before_lean(S):
    calls = S['answj']
    ts = iso_epoch(((calls[1].get('result_ts') or '') if len(calls) > 1 else '')[:19] + 'Z')
    return len(calls) >= 2 and ts is not None and S['branch_ct'] is not None and ts < S['branch_ct'] and '(Instance)' in S['answers']


def work_orders_ok(S):
    return landed(S, 0, ['W-ORD-EPSTEIN-CERTIFY', 'PRICED, NOT STARTED'], 'rl2') and landed(S, 0, ['W-ORD-FT-FIRST-ORDER', 'PRICED, NOT STARTED'], 'rl3')


def dominance_ok(S):
    j = S['domj']
    rows = j.get('rows') or []
    c = j.get('candidates') or {}
    return len(rows) == 17 and all(r.get('dominant') == 0 and r.get('decided') for r in rows) and j.get('self_dominant') == [0] \
        and sorted(c) == ['0', '1'] and 'THE TWO CANDIDATE BASES' in S['domt']


def instance_gate_ok(S):
    import b663_record as REC
    try:
        h1, h2, rid, merged = REC.read_instance(S['instj'])
    except Exception:
        return False
    rows = S['instj']['rows']
    return h1 and h2 and rid == K.RUN_ID and merged == K.MERGE and S['instj'].get('tag') == K.MERGE_TAG and S['instj'].get('sha_ok') \
        and len(rows) == K.PRINT_TARGETS_N and all(r['std3'] for r in rows) and 'INTERFACES 7, DERIVES 3, DEF 11' in S['instt'] \
        and 'MET at this read carries Q0Premises: True' in S['instt'] and S['instj'].get('merge_tree_equals_built') is True


def met_widened_ok(S):
    a, b = S['e0_pre'], S['e0_now']
    if not a or not b:
        return False
    la, lb = a.decode('utf-8').split(NL), b.decode('utf-8').split(NL)
    if len(la) != len(lb):
        return False
    diff = [(x, y) for x, y in zip(la, lb) if x != y]
    return len(diff) == 1 and "+ ('Q0Premises',)" in diff[0][1] and "+ ('Q0Premises',)" not in diff[0][0] \
        and '(56)' in S['met_before'] and 'NOT CLEAN 1 ["test_e0_rule.py [\'(56)\']"]' in S['met_before'] \
        and '57 of 57 cases as wanted -- PASS' in S['met_after']


def control_ok(S):
    import b663_record as REC
    try:
        cs = [REC.read_control_cell(r) for r in S['ctlj'].get('cells') or []]
    except Exception:
        return False
    z = [c for c in cs if c[0].startswith('THE CONTROL')]
    q = [c for c in cs if c[0].startswith('Q0')]
    t = S['ctlt']
    return len(cs) == 2 and bool(z) and z[0][2] == 31 and z[0][3] is True and bool(q) and q[0][1] == 'j₀' and isinstance(q[0][2], int) \
        and q[0][3] is True and 'THE CONTROL REPRODUCED' in t and '  H3 HELD ON B1' in t and '  H4 HELD ON B1' in t \
        and 'certified on B1 (READ), not a kernel lemma' in t


def script_diff_ok(S):
    d = S['mapdiff']
    m = re.search(r"### the hunks` b662 ranges: (.*)$", d, re.M)
    if not m:
        return False
    starts = [int(x.lstrip('-').split(',')[0]) for x in m.group(1).split()]
    hrate = [s for s in starts if 295 <= s <= 336 or s in (255, 265)]
    return 'Hunks: 33 ;' in d and not hrate


def hypotheses_scored(S):
    import b663_record as REC
    ok = True
    for k in ('H1', 'H2', 'H3', 'H4'):
        try:
            _k, w, _t = REC.read_score_row(k, S['sc'].get(k))
        except Exception:
            return False
        ok = ok and w.startswith(('HELD', 'REFUTED')) and ('(%s)' % k) in S['desk']
    return ok


# ================================================================== THE RUNNER (the standing arms, this kernel's run)
def wf_ok(S):
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or not v['on_main'] or v['commit_files'] != [WF]:
            return False
        if any(w in t for w in ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'lake exe cache get' not in t or '#print axioms' not in t \
                or 'done < print_targets.txt' not in t or len(v['targets']) != K.PRINT_TARGETS_N:
            return False
    return len(S['wf']) == 1


def runner_ok(S):
    j = S['instj']
    return (j.get('run') or {}).get('run_id') == K.RUN_ID and (j.get('run') or {}).get('ref') == K.RUN_REF and j.get('conclusion') == 'success' \
        and j.get('sha_ok') and bool(j.get('sha256')) and isinstance(j.get('mem_low'), int) and j['mem_low'] >= K.HOLD


def gate_ok(S):
    t = S['instt']
    return bool(S['instj'].get('H1')) and 'BUILD EXIT 0 ; ERROR LINES 0' in t and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) is not None \
        and ('TERMINALS %d, PRINTED %d, AT THE STANDARD THREE OR NONE %d' % ((K.PRINT_TARGETS_N,) * 3)) in t


def merges_ok(S):
    j = S['instj']
    for k, m in S['merges'].items():
        if not j.get('merged') or not j.get('H1') or m['main'] != j['merged'] or len(m['parents']) != 2 \
                or m['built'] not in m['parents'] or m['tree_main'] != m['tree_built'] or m['tags'].get(j.get('tag')) != j['merged'] \
                or j.get('tag') != K.MERGE_TAG:
            return False
    return len(S['merges']) == 1


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
def instruments_ok(S):
    for f, (pre, now, head) in S['inst'].items():
        if pre is None or pre != now or pre != head:
            return False
    return True


def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b663 seal', 'b663 pre-root', 'b663 root', 'b663 record', 'b663 --', 'b663 closing')


def _component_commit(s):
    return s.startswith('b663') and not s.startswith(POST_SEAL)


def sealed_after_ok(S):
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def table_final_ok(S):
    t = S['tfj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('grade_moved')


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 40 and rows[39][:3] == ['b663', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b664_' in it] \
        and any(it.startswith('data/b663_epstein_instance.json ') for it in j.get('items') or []) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b663_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b663') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 664)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The record lines**', '**The plan**', '**The instance**', '**The computation**', '**The root.**',
                 '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b664', 'W-ORD-EPSTEIN-CERTIFY')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == conv(S['fj'].get('title') or '\x00') and all(x in tail for x in ENTRY_NEEDLES)


def trail_tail(S):
    t = S['ot']
    i = t.find(conv(S['REC'].TRAIL_HEAD()))
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    import b663_record as REC
    v = S['sc'].get(k)
    try:
        _k, w, _t = REC.read_score_row(k, v)
    except Exception:
        return False
    return w.split(' ')[0].split(',')[0] in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k) in S['desk']


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def publish_uncalled(S):
    pub = ['actions' + '/pub' + 'lish', 'z_' + 'publish']
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if any(p in t for p in pub)]


def kernels_untouched(S):
    import b641_record as R41
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and sorted(f) == sorted(R41.KERNS_READ) and all(k in n and n[k] == f[k] for k in f)


def corpus_scope(S):
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md'])


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE PLAN' in t and '### THE INSTANCE' in t and 'THE HOSTED RUNNER' in t and '### THE DRY RUN' in t \
        and '### THE COMPUTATION' in t and '### THE CITATION CHECK' in t


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _rl(S, i, line, key='rl'):
    ls = list(S[key].get('lines') or [])
    ls[i:i + 1] = [dict(rline(S, i, key), line=line)]
    return put(S, key, dict(S[key], lines=ls))


def _mut(S, key, f):
    d = copy.deepcopy(S[key])
    f(d)
    return put(S, key, d)


def _live(S, f):
    d = copy.deepcopy(S['live'])
    f(d)
    return put(S, 'live', d)


def _planted(S, t):
    return put(S, 'planted', dict(S['planted'], **{t: dict(rc=1, out='')}))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R273) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and bash named, none running at the start, no orphan, read again after the runs',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('Orphans: NONE', 'Orphans: 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host); the two transient failures clean alone',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b662_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay and PLACE-papers branch lists, local and remote-tracking, and the step-zero bank (SIDE-carrier-spec`s three and its remote)',
     lambda S: branches_ok(S), lambda S: put(S, 'push_lists', {'D:/relay': 'push-b662'})),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line, each bank`s row unit named',
     lambda S: readfirst_ok(S), lambda S: put(S, 'readfirst', S['readfirst'].replace('R5 :156', 'x'))),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its prompts with their options and results', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS', 'THE ANSWERS'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b663_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: landed(S, 0, ['b662 AT ITS WEIGHT', 'Nothing deposited.']),
     lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step), its misses raised in one prompt answered before Component 1`s first commit, each a lettered defect of the navigator`s',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('RUN BEFORE THE FERRY IS BANKED', 'RUN'))),
    ('G-PLAN-BANKED', 'the plan bank: the five rungs by line, all priced, b326`s zeros, B1 with its derivation, A0Q`s reason, the author`s word section',
     lambda S: plan_ok(S), lambda S: put(S, 'plan', S['plan'].replace('THIS ACT BUILDS NO RUNG', 'x'))),
    ('G-PLAN-BEFORE-LEAN', 'the answers bank against the instance branch: the plan prompt answered before the branch`s first commit',
     lambda S: plan_before_lean(S), lambda S: put(S, 'branch_ct', 1)),
    ('G-WORK-ORDERS-ENTERED', 'OPEN_TRAILS at the two record-line banks: W-ORD-EPSTEIN-CERTIFY and W-ORD-FT-FIRST-ORDER entered priced',
     lambda S: work_orders_ok(S), lambda S: _rl(S, 0, 1, 'rl2')),
    ('G-DOMINANCE-BANKED', 'the dominance bank: 17 bases, index 0 the decided dominant at each and the one self-dominant, the two candidate bases',
     lambda S: dominance_ok(S), lambda S: _mut(S, 'domj', lambda d: d.update(self_dominant=[0, 1]))),
    ('G-INSTANCE-GATE', 'the instance bank through the record tool`s reader: H1 and H2, the run, 31 prints at the standard three, INTERFACES 7 on the re-grade, merged at d00ab16 tag v0.29, the merged tree the built tree',
     lambda S: instance_gate_ok(S), lambda S: _mut(S, 'instj', lambda d: d.update(H1=False))),
    ('G-MET-WIDENED', 'tools/e0_rule.py against its blob before the act: one line changed, Q0Premises entered; test_e0_rule.py`s case (56) failing before and passing after',
     lambda S: met_widened_ok(S), lambda S: put(S, 'met_after', S['met_after'].replace('57 of 57 cases as wanted -- PASS', '56 of 57'))),
    ('G-CONTROL-BANKED', 'the computation bank through the record tool`s reader: the control at j₀ = 31 and below 0, Q0 with an index and its zero side below 0, H3 and H4 on B1',
     lambda S: control_ok(S), lambda S: put(S, 'ctlt', S['ctlt'].replace('THE CONTROL REPRODUCED', 'THE CONTROL NOT REPRODUCED'))),
    ('G-SCRIPT-DIFF-CONFINED', 'the diff bank: 33 hunks, none in hrate`s lines (b662 :295-:336) or at :255 and :265',
     lambda S: script_diff_ok(S), lambda S: put(S, 'mapdiff', S['mapdiff'].replace("### the hunks` b662 ranges: ", "### the hunks` b662 ranges: -301 "))),
    ('G-HYPOTHESES-SCORED', 'the scores of H1-H4 through the record tool`s reader, and the desk', lambda S: hypotheses_scored(S),
     lambda S: put(S, 'desk', '')),
    ('G-SPEC-PLANTED', 'tools/b663_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('control cell' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b663 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it', lambda S: S['conv_bad'] == []
     and 'from b663_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b663_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-explicit-formula`s main: the workflow file on main since b654, its commit the file alone, no author identifier, no secret, the hold, the cache, the print step reading print_targets.txt of 31 names',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'the instance bank: the run id and ref of the worklist, success, the artifact`s sha256 agreeing, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'instj', lambda d: d.update(mem_low=2000))),
    ('G-RUNNER-GATE', 'the gate reading: build exit 0, no error line, the 31 prints at the standard three, the artifact`s digest agreeing, H1',
     lambda S: gate_ok(S), lambda S: put(S, 'instt', S['instt'].replace('BUILD EXIT 0', 'BUILD EXIT 1'))),
    ('G-MERGES-ON-GATE', 'the kernel`s main: a merge commit of the built tip, the merged tree the built tree, its tag v0.29 peeled to it',
     lambda S: merges_ok(S), lambda S: _mut(S, 'merges', lambda d: d[K.KERNEL]['tags'].clear())),
    ('G-NO-SORRY-MAIN', 'tools/no_sorry_main.py run at HEAD over every kernel, its remote read once by this run: no `sorry` in code, every pair equal',
     lambda S: no_sorry_main(S), lambda S: _live(S, lambda d: d['nsm'][0]['hits'].append(('x.lean', 1, 'sorry')))),
    ('G-NO-SORRY-MAIN-PLANTED', 'tools/test_no_sorry_main.py run: 5 of 5', lambda S: planted_ok(S, 'test_no_sorry_main.py', 5),
     lambda S: _planted(S, 'test_no_sorry_main.py')),
    ('G-AXIOM-CLAIM', 'tools/axiom_claim.py run at HEAD over every kernel against the banked prints: no claim CONTRADICTED', lambda S: axiom_claim(S),
     lambda S: _live(S, lambda d: d['ac'].append(dict(d['ac'][0], verdict='CONTRADICTED')))),
    ('G-AXIOM-CLAIM-PLANTED', 'tools/test_axiom_claim.py run: 12 of 12', lambda S: planted_ok(S, 'test_axiom_claim.py', 12),
     lambda S: _planted(S, 'test_axiom_claim.py')),
    ('G-MODULE-HEADER', 'tools/module_header.py run at HEAD over every kernel: no header OVERREACHES', lambda S: module_header(S),
     lambda S: _live(S, lambda d: d['mh'].append(dict(kernel='x', file='x.lean', line=1, name='x', why='planted')))),
    ('G-MODULE-HEADER-PLANTED', 'tools/test_module_header.py run: 12 of 12', lambda S: planted_ok(S, 'test_module_header.py', 12),
     lambda S: _planted(S, 'test_module_header.py')),
    ('G-CONVERSION-TEST', 'tools/test_conversion_b652.py run: 7 of 7', lambda S: planted_ok(S, 'test_conversion_b652.py', 7),
     lambda S: _planted(S, 'test_conversion_b652.py')),
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS and OPEN_TRAILS', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the registry, the map, the census, the monograph, the pages, the surround: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal', lambda S: kernels_untouched(S),
     lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b662`s and the earlier tools, the instruments and the shared tools (e0_rule.py read by G-MET-WIDENED): before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 51838723 but the shared additive files, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 0,
     lambda S: put(S, 'prior_bad', ['data/b662_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes, the workflow, print_targets.txt and the instance file among them',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b663 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b663_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b662`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b662 — lane three, act eighty-nine' in S['ot']
     and S['rootsf'].count(NL + 'b662 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b662 — lane three', '### b662 - lane three'))),
    ('G-R273-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R273) END' in S['ferry'] and S['ot'].count('**(R273) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R273) ratified', '**(R2730) ratified'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 40th line, the root bank and its items', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b664 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b663 AGREE, b663 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b663 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b663_record.py agree', 'b663_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b664', lambda S: '**Next:** b664, per' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b664, per', '**Next:** b665, per'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 51838723, b662`s push-out bank and the ruled e0_rule line among them, against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b663')" in S['suite'] and "'data/b663_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b663_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the plan, the instance, the runner, the computation, the dry run',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound request', 'x'))),
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
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b663_seal_hashes.json')
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
        print('  %-38s %s' % (t, now[t]))
    print('  written: b663_seal_hashes.json')
    return 0


def main():
    if SEAL:
        return seal()
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b663 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources()
    S['pushed'] = pushed
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID) else regenerate()
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b662`s face less its own arms) %d ; carried here %d ; the act`s arms over its own banks %s ; '
        'arms beyond both %s' % (len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
                                sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    av = S['ar_verify']
    rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    rec('  ### G-EDIT-ROUTE read %d captured commands; offences %d: %s' % (len(S['cmds']), len(S['ER'].scan(S['cmds'])),
                                                                         ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in S['ER'].scan(S['cmds'])] or 'none'))
    rec('  ### THE SPEC`S PLANTED ROWS: %s ; controls refused %s' % (list(zip(S['spec']['shapes'], S['spec']['read'])), S['spec']['controls']))
    mc = re.search(r'CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s' % (mc.group(0) if mc else '### UNREAD'))
    j = S['instj']
    rec('  ### THE INSTANCE : run %s %s ; sha256 %s %s ; memory low %s ; H1 %s ; H2 %s ; merged %s ; tag %s' % (
        (j.get('run') or {}).get('run_id'), j.get('conclusion'), (j.get('sha256') or '-')[:16], 'AGREE' if j.get('sha_ok') else '### NOT AGREED',
        j.get('mem_low'), j.get('H1'), j.get('H2'), j.get('merged'), j.get('tag')))
    for k, m in S['merges'].items():
        rec('  ### THE MERGE %s : main %s ; parents %s ; built %s ; merged tree = built tree %s ; tags %s' % (
            k, m['main'], m['parents'], m['built'], m['tree_main'] == m['tree_built'], m['tags']))
    for l in S['ctlt'].split(NL):
        if l.startswith(('  READING ', '  H3 ', '  H4 ', '  THE CONTROL ')):
            rec('  ### THE COMPUTATION: ' + l.strip()[:200])
    lv = S['live']
    rec('  ### THE THREE ARMS AT HEAD (seconds %s):' % ', '.join('%.0f' % x for x in lv['secs']))
    rec('  ###   G-NO-SORRY-MAIN read %d kernels` mains, pairs unequal %d; sorry in code %d: %s' % (
        len(lv['nsm']), sum(1 for r in lv['nsm'] if not r['equal']), len(nsm_hits(S)), '; '.join('%s %s:%d' % h for h in nsm_hits(S)) or 'none'))
    rec('  ###   G-AXIOM-CLAIM read %d claims: CONTRADICTED %d, UNVERIFIABLE %d, VERIFIED %d, UNBOUND %d, MENTION %d' % (
        sum(1 for r in lv['ac'] if r['verdict'] != 'OUT OF SCOPE'), ac_count(lv['ac'], 'CONTRADICTED'), ac_count(lv['ac'], 'UNVERIFIABLE'),
        ac_count(lv['ac'], 'VERIFIED'), ac_count(lv['ac'], 'UNBOUND'), ac_count(lv['ac'], 'MENTION')))
    for r in lv['ac']:
        if r['verdict'] == 'CONTRADICTED':
            rec('  ###     CONTRADICTED %s %s:%d -- %s' % (r['kernel'], r['file'], r['line'], ', '.join(x['decl'] for x in r['contradicted'][:6])))
    rec('  ###   G-MODULE-HEADER read %d headers: OVERREACHES %d rows' % (sum(v['headers'] for v in lv['mh_per'].values()), len(lv['mh'])))
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
    rec('  ### the run took %.0f s' % (time.time() - t_start))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b663_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b663_checks_postpush.txt' if pushed else 'b663_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b663_arms_prerun.txt', 'b663_lsr_prerun.json').replace('b663_checks', 'b663_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b663_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
