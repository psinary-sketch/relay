# -*- coding: utf-8 -*-
"""b676_checks.py -- THE SUITE OF b676, UNDER (R286): b675 AT ITS WEIGHT; SIDE-trivium'S DOCSTRINGS NAMED BY THE RULE AND RE-CUT IN b674'S
FORM; THE Q0 LINES READ AND BANKED; THE STRIP'S USES IN V5 AND THE COMPOSITION LISTED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R264)(2), THE FREEZE: the standing arms are b675's face's (G2) arms less b675's own arms over b675's banks, carried, their act needles
### read in b676's banks (b675 at its weight, the branches (R286)(5) names, this act's step-zero bank); the act's own arms read this act's
### banks alone (tools/b676_worklist.py ACT_ARMS). The standing runner arms read this act's merged run: SIDE-trivium's run 39004541707 at
### db315fe, merged at 135be2e, v0.1.1, the workflow in the kernel's Mathlib form with its print list on main.
### ### Two standing arms read act lists this act's ruling sets, declared on the face: G-PP-SCOPE (PLACE-papers' changed files against the
### two ledgers) and G-CURRENTS-UNEDITED (b675's currents, README, REGISTRY and the faces page among them, unwritten by this act).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b676_record.py).
### ### The harness is b568's to b675's (helpers, runner, seal), written by the Write tool from tools/b675_checks.py; the sources, predicates
### ### and arms over this act's banks are b676's.
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
import b676_worklist as K     # noqa: E402
import b675_worklist as K675  # noqa: E402
import b674_worklist as K674  # noqa: E402
from b676_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b676_registration_2026-10-17.txt')
B675_FACE = os.path.join(D, 'b675_registration_2026-10-16.txt')
B675_ACT_ARMS = K675.ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = 'aff60aa3'          # ### relay: b675's closing push-out bank, committed at step zero ((R286)(5))
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
INST = K675.SEALED + ('b675_li_bench.py',) + K674.SEALED + (
        'b673_checks.py', 'b673_closing.py', 'b673_tests.py', 'b673_worklist.py', 'b673_reg_gate.py', 'b673_regspec.py', 'b673_record.py',
        'b673_citation.py', 'b673_v4_control.py',
        'b672_checks.py', 'b672_closing.py', 'b672_tests.py', 'b672_worklist.py', 'b672_reg_gate.py', 'b672_regspec.py', 'b672_record.py',
        'b672_citation.py', 'correspondence_gen.py', 'test_correspondence_gen.py',
        'b671_checks.py', 'b671_closing.py', 'b671_tests.py', 'b671_worklist.py', 'b671_reg_gate.py', 'b671_regspec.py', 'b671_record.py',
        'b671_citation.py', 'b671_narrow.py', 'b671_epstein_map_narrowed.py', 'b671_tie_diagnostic.py',
        'b667_epstein_certify.py', 'b667_epstein_map_balls.py', 'b667_tail_recheck.py',
        'b663_epstein_map.py', 'b655_record.py', 'edit_route.py', 'test_edit_route_b646.py', 'b652_record.py', 'b651_record.py',
        'b649_record.py', 'b648_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py', 'b643_record.py', 'b641_record.py',
        'b633_record.py', 'b616_record.py', 'act_root.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py',
        'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py',
        'b616_claims.py', 'ferry_scan.py', 'e0_rule.py', 'test_e0_rule.py', 'build_watch.py', 'chain_page.py',
        'axiom_claim.py', 'licensed_table.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py',
        'test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py',
        'rowgen/rowgen.py', 'rowgen/diff_rowpin.py', 'rowgen/namemap.json')
# ### b675's currents: this act writes no README, REGISTRY or faces-page byte
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
TABLE_FILES = K.TABLE_FILES
# ### this act's merged run, read by the standing runner arms
WD, WF, PT = K.TD, '.github/workflows/build-module.yml', 'print_targets.txt'
W_PRE_MAIN, W_WORKFLOW, W_MAIN, W_CUT, W_TAG, W_RUNS = K.T_PRE_MAIN, K.T_WORKFLOW, K.T_MAIN, K.T_CUT, K.T_NEXT_TAG, K.T_RUNS
W_MERGE = '135be2e'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b676')
            and 'data/b676_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b676_record as REC
    return REC.capture()


def run_test(name):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, name)], capture_output=True, text=True, encoding='utf-8', errors='replace')
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
        if f.startswith('b676_') and f.endswith('.py'):
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b676_regspec as SPEC
    import b676_record as REC
    P = SPEC.planted()
    ctl = []
    for f in (lambda: REC.read_score_row('X9', 'HELD'),
              lambda: REC.read_q0_row(dict(file='F', line=1, kind='sentence', s='x', reading='MAYBE', why='x'))):
        try:
            f()
            ctl.append(False)
        except Exception:
            ctl.append(True)
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def wf_state():
    t = read_blob(WD, 'main:' + WF)
    pt = read_blob(WD, 'main:' + PT)
    return {K.CANDIDATE: dict(text=t, commit_files=files_of(WD, W_WORKFLOW), list_files=files_of(WD, W_MAIN),
                              on_main=subprocess.run(['git', '-C', WD, 'merge-base', '--is-ancestor', W_WORKFLOW, 'main']).returncode == 0,
                              targets=[l.strip() for l in pt.split(NL) if l.strip()],
                              lean_in_writes=[f for f in files_of(WD, W_WORKFLOW) + files_of(WD, W_MAIN) if f.endswith('.lean')])}


def merges_state():
    p = WD
    return {K.CANDIDATE: dict(main=gs(p, 'rev-parse', '--short=7', 'main'), parents=gs(p, 'log', '-1', '--format=%p', '--abbrev=7', 'main').split(),
                              built=W_CUT, tree_main=gs(p, 'rev-parse', 'main^{tree}'), tree_built=gs(p, 'rev-parse', W_CUT + '^{tree}'),
                              tags=dict((t, gs(p, 'rev-parse', '--short=7', t + '^{commit}')) for t in gs(p, 'tag', '--points-at', 'main').split()))}


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted(set(g2_of(B675_FACE)) - set(B675_ACT_ARMS))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


def _ct_first(repo, pre, prefix, path=None):
    args = ['log', '--reverse', '--format=%ct %s', pre + '..HEAD'] + (['--', path] if path else [])
    for l in gs(repo, *args).split(NL):
        if l.strip() and l.split(' ', 1)[1].startswith(prefix):
            return int(l.split(' ', 1)[0])
    return None


def sources():
    import b676_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b676_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b676_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b676_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b676_ferry.txt'), scan=rd('b676_ferry_scan.txt'), stepz=rd('b676_stepzero.txt'),
        readfirst=rd('b676_readfirst.txt'), defects=rd('b676_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b676_author_answers.txt'), prerun=rd('b676_arms_prerun.txt'), rl=jl('b676_record_lines.json'), rl3=jl('b676_record_lines_c3.json'),
        tests=jl('b676_tests_stepzero.json'), testst=rd('b676_tests_stepzero.txt'), withheld=jl('b676_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b676_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), cmdj=jl('b676_commands.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b676_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        c1_ct=_ct_first(PP, PRE['pp'], 'b676 Component 1'),
        gate=rd('b676_reg_gate.txt'), rowgen=rd('b676_rowgen_stepzero.txt'),
        branchj=jl('b676_branches.json'),
        branch_lists=dict((repo, gs(repo, 'branch', '-a', '--list', *(list(bs) + ['*/' + b for b in bs]))) for repo, bs in K.DELETE),
        naming=rd('b676_naming.txt'), namingj=jl('b676_naming.json'), wf_ct=int(gs(WD, 'log', '-1', '--format=%ct', W_WORKFLOW) or 0),
        cut=rd('b676_cut.txt'), cutdiff=rd('b676_cut_diff.txt'), cut_names=gs(WD, 'diff', '--name-only', W_MAIN, W_CUT).split(NL),
        prints=rd('b676_prints_compare.txt'), corr=rd('b676_correspondence_dry.txt'),
        q0=jl('b676_q0_lines.json'), q0t=rd('b676_q0_lines.txt'), orders=rd('b670_work_orders.txt'),
        strips=jl('b676_strip_uses.json'), stript=rd('b676_strip_uses.txt'),
        strip_blobs=dict((f, read_blob(K.KE, '%s:%s' % (K.KREV, f)).split(NL)) for f in (K.V5_FILE, K.COMP_FILE)),
        repairs=rd('b676_tool_repairs.txt'), citation_src=read(os.path.join(T, 'b676_citation.py')),
        standing=STANDING, wf=wf_state(), runner=jl('b676_runner_rows.json'), rbank=rd('b676_runner_SIDE-trivium_after.txt'),
        ax_after=rd('b676_axioms_SIDE-trivium_after.txt'), merges=merges_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b676_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b676_act_root.json'), arj0=jl('b675_act_root.json'), art=rd('b676_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b676_kernels_face.json').get('kernels') or {}), kerns_read=REC._kerns(),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b676_mustnotexist.txt')),
        fj=jl('b676_findings.json'), tj=jl('b676_trail.json'), sc=jl('b676_scores.json'), desk=rd('b676_desk_notes.txt'), tfj=jl('b676_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    # ### the seconds of each phase of the sources, printed by the run (the 600 s foreground limit and b675's rules row 2, 450 s)
    S['phase_secs'] = {'the banks and the state': time.time() - t0}
    S['pp_allowed'] = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'])
    t1 = time.time()
    S['live'] = live_arms()
    S['phase_secs']['the three arms at HEAD'] = time.time() - t1
    t1 = time.time()
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
        if f.startswith(('b676_', 'audit_b676_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith('.gz'):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    S['outside'] = [n for n in R41.OAI_NEEDLES if n in S['ledger_adds']]
    shared = set(ADD.shared_files()) | set(K.SHARED_APPENDED)
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
    S['phase_secs']['the written files, the public bytes and the prior banks'] = time.time() - t1
    t1 = time.time()
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
    S['phase_secs']['the act-root chain'] = time.time() - t1
    t1 = time.time()
    try:
        S['additive'] = ADD.check(worktree=True)
    except Exception as e:
        S['additive'] = [('raised', type(e).__name__, [('x', [])])]
    S['phase_secs']['the shared additive files'] = time.time() - t1
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


def unwrap(t):
    """a bank's text with each line's leading `###` markers dropped and the whitespace collapsed (b670 (h))."""
    return ' '.join(' '.join(re.sub(r'^\s*(?:###\s*)+', '', l) for l in t.split(NL)).split())


def procs_ok(S):
    """the step-zero bank's process listings, in this act's words: at the start and after the tests, none of tail, lean, lake, python or
    bash running."""
    p = unwrap(S['stepz'])
    return '(names tail, lean, lake, python, bash): none of each' in p and 'after the tests (tail, lean, lake, python, bash): none of each' in p


STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 2' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"
PROMPT_HEADS = ('(Print list)', '(Before run)')


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b676 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) >= 1 and all(x >= 2 for x in per) and len(res) == len(calls) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and all(x in a for x in PROMPT_HEADS)


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def no_local_lean(S):
    import b676_record as REC
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


# ================================================================== (R286) STEP ZERO: THE CITATION CHECKS, THE BRANCHES, ROWGEN
READFIRST_NEEDLES = ('data/b675_closing.txt', 'data/b675_defects.txt', 'data/b675_hypotheses.txt', 'data/b675_li_plan.txt', 'data/b675_rules.txt',
                     'data/b674_rules.txt', 'data/b670_licensed_table.txt', 'data/b647_table_*.txt', 'data/b674_cut.txt', 'data/b674_tool_repairs.txt',
                     'data/b675_tool_repairs.txt', 'SIDE-trivium .github/workflows', 'Zeta23/Defs.lean :142', 'RestBound.lean :40',
                     'tools/correspondence_gen.py', 'data/b670_work_orders.txt', 'data/b675_closing_push_out.txt')


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """the branches (R286)(5) names: none left in its repository, local or remote-tracking; the branches bank lists them, each with its tip."""
    z = rd('b676_branches.txt') if S.get('branchj') else ''
    named = [b for _r, bs in K.DELETE for b in bs]
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and all(b in z for b in named) \
        and 'BRANCHES 5 (LOCAL 5, REMOTE 0) ; MERGED 5 ; TO BE DELETED 5' in z


def branches_banked_ok(S):
    import b676_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 5 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) and all(r['where'] == 'local' for r in rows)


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    """b675's rules row 1: the closing run dry as a gate step before the lock, its readings printed in the gate's record -- the head line,
    the citation line from the banks, the re-cut's and the Q0 bank's verdict lines, the tag rows with their kind."""
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b676 closed:' in g and 'the misses as the bank lists them' in g and '(annotated, peeled) ; main' in g \
        and '### THE RE-CUT ((R286)(2)' in g and '### THE Q0 LINES' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the step-zero check: run before the ferry was banked; its one miss (the arm's removal (R286)(1) asks for) entered by the fact clause in
    the weight line and as the navigator's (e); Component 1 committed after the check."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    entered = '    (e) THE NAVIGATOR' in S['defects'] and landed(S, 0, ['no arm was removed'])
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'RUN BEFORE THE FERRY IS BANKED' in c \
        and int(m.group(3)) == 1 == len(S['cit_misses']) and entered and S['c1_ct'] is not None and S['cit_at'] and S['cit_at'] < S['c1_ct']


MID_NEEDLES = ('on the print list', 'on the ‘before’ bank')


def midact_ok(S):
    """(R278)(4): every mid-act answer's check appended, each answer's last print with no miss; the one-result shape entered ((b))."""
    blocks = re.split(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', S['citation'], flags=re.M)[1:]
    last = {}
    for b in blocks:
        for n in MID_NEEDLES:
            if repr(n) in b.split(NL)[0]:
                m = re.search(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', b)
                last[n] = m.groups() if m else None
    return all(last.get(n) and last[n][2] == '0' and int(last[n][0]) > 0 for n in MID_NEEDLES) and '    (b) THE SEAT' in S['defects']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


# ================================================================== (R286)(2)-(4): THE NAMING, THE CUT, THE Q0 LINES, THE STRIP'S USES
def naming_ok(S):
    """N2: the rule row and the table rows printed verbatim before the naming line, the workflow directory and the print bank read in the
    same bank, the bank written before the kernel's first write (the workflow commit) and so before any branch."""
    t, j = S['naming'], S['namingj']
    idx = [t.find(x) for x in ('### THE RULE, verbatim', '### THE TABLE ROWS, verbatim', '### THE NAMING:',
                               '### THE NAMED KERNEL`S WORKFLOW DIRECTORY AND PRINT BANK (read before any branch is made)')]
    at = iso_epoch(j.get('at') or '')
    return all(i >= 0 for i in idx) and idx == sorted(idx) and j.get('named') == K.CANDIDATE and at and S['wf_ct'] and at < S['wf_ct'] \
        and 'relay data/b674_rules.txt :8' in t and 'licensed table :119' in t and 'WORKFLOW build-module.yml ABSENT ; PRINT BANK ABSENT' in t


def cut_comment_ok(S):
    return '### ### **FILES 1 ; CODE EQUAL WITH COMMENTS STRIPPED True ; CONTROLS UNEQUAL True ; COMMENT AND DOCSTRING LINES ALONE True.**' in S['cutdiff'] \
        and [x for x in S['cut_names'] if x.strip()] == list(K.T_CUT_FILES)


def prints_ok(S):
    import b676_record as REC
    rows = S['runner'].get('rows') or []
    try:
        gates = dict(REC.read_runner_row(r) for r in rows)
    except Exception:
        return False
    return 'EQUAL LINE FOR LINE True.**' in S['prints'] and gates == {'before': 'DERIVES', 'after': 'DERIVES'} \
        and all(r.get('artifact_sha256') for r in rows) and dict((r['label'], r['run_id']) for r in rows) == dict((l_, r_) for r_, l_ in W_RUNS)


def distance_ok(S):
    v = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+) \(OF ANY KIND (\d+), (\d+)\)', S['cut'])
    pins = S['REC']._pin_blocks(S['cut'])
    return bool(v) and int(v.group(2)) <= int(v.group(1)) and int(v.group(4)) <= int(v.group(3)) and len(pins) == 4 \
        and all(re.search(r':\d+', p) for p in pins) and 'the marker at :17' in S['cut']


def corr_ok(S):
    return 'CELLS CHANGED 0 ; LINES NAMING THE CUT KERNEL 0 ; RUN MODE NOT RUN (no cell to change)' in S['corr']


def q0_ok(S):
    """N4's first half: every hit through the record tool's reader with a file, a line, the sentence and a reading; the count printed;
    the TO RE-CUT count the bank's; nothing cut."""
    import b676_record as REC
    hits = S['q0'].get('hits') or []
    try:
        rows = [REC.read_q0_row(h) for h in hits]
    except Exception:
        return False
    rc = sum(1 for _f, _l, r in rows if r == 'TO RE-CUT')
    v = re.search(r'HITS (\d+) ; CONSISTENT (\d+) ; TO RE-CUT (\d+) .* NOTHING CUT\.', S['q0t'])
    return bool(rows) and rc == S['q0'].get('recut') > 0 and bool(v) and int(v.group(1)) == len(rows) and int(v.group(3)) == rc


def order_ok(S):
    """(R286)(3): W-ORD-Q0-CLASS-LINES at OPEN_TRAILS by the landing's bank, its trigger and Status; its row in the orders bank at that line."""
    x = rline(S, 0, 'rl3')
    ln = x.get('line')
    return landed(S, 0, ['W-ORD-Q0-CLASS-LINES', 'the next re-cut act after b676', 'Status: OPEN.'], key='rl3') and ln is not None \
        and re.search(r'^  W-ORD-Q0-CLASS-LINES\s+:%d\s+b676\s+0\s+OPEN\s+:%d\s+the next re-cut act after b676' % (ln, ln), S['orders'], re.M) is not None


def strips_ok(S):
    """N4's second half: every use cited by file and line, its needle read again on its line at e36ea31 by this run; none unlisted."""
    rows = S['strips'].get('uses') or []
    bl = S['strip_blobs']
    hit = [f in bl and 0 < n <= len(bl[f]) and nd in bl[f][n - 1] for f, n, nd, _d in rows]
    return len(rows) == 22 and all(hit) and S['strips'].get('unlisted') == [] and 'UNLISTED 0 ; NO LEAN WRITTEN.**' in S['stript']


def repairs_ok(S):
    return '### ### **REPAIRS 2 ; THE SEALED COPIES AGREE ; HUNKS' in S['repairs'] and 'EACH ANSWER CUT FROM ITS RESULT True' in S['repairs'] \
        and 'THE CHECKS READ BY THE CLOSING True.**' in S['repairs'] and "the (?:navigator`s )?answer carrying" in S['closing_src'] \
        and "rfind('BEGIN', 0, k)" in S['citation_src']


# ================================================================== THE RUNNER (the standing arms, this act's merged run: SIDE-trivium)
def wf_ok(S):
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or not v['on_main'] or v['commit_files'] != [WF] or v['list_files'] != [PT] or v['lean_in_writes']:
            return False
        if any(w in t for w in ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'print_targets.txt' not in t or 'lake env lean out/axioms.lean' not in t \
                or 'lake exe cache get' not in t or len(v['targets']) != 22:
            return False
    return len(S['wf']) == 1


def runner_ok(S):
    import b676_record as REC
    rows = [r for r in S['runner'].get('rows') or [] if r.get('label') == 'after']
    if len(rows) != 1:
        return False
    r = rows[0]
    REC.read_runner_row(r)
    return r['run_id'] == dict((v, k) for k, v in W_RUNS)['after'] and r['ref'].startswith(W_CUT) and r['conclusion'] == 'success' \
        and bool(r['artifact_sha256']) and r['mem_low'] is not None and r['mem_low'] >= K.HOLD and not r['stopped']


def gate_ok(S):
    rows = [r for r in S['runner'].get('rows') or [] if r.get('label') == 'after']
    n = len(re.findall(r"^'[^']+' (?:depends on axioms|does not depend on any axioms)", S['ax_after'], re.M))
    return bool(rows) and rows[0].get('gate') == 'DERIVES' and 'GATE DERIVES' in S['rbank'] \
        and ('TERMINALS PRINTED %d OF %d ; SORRYAX 0' % (n, n)) in S['rbank'] and n > 0 \
        and 'BUILD EXIT 0 ; ERROR LINES 0' in S['rbank'] and re.search(r'^### the artifact: .* ; AGREE$', S['rbank'], re.M) is not None


def merges_ok(S):
    for k, m in S['merges'].items():
        if m['main'] != W_MERGE or m['parents'] != [W_MAIN, W_CUT] or m['built'] not in m['parents'] \
                or m['tree_main'] != m['tree_built'] or m['tags'].get(W_TAG) != W_MERGE:
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


POST_SEAL = ('b676 seal', 'b676 pre-root', 'b676 root', 'b676 record', 'b676 --', 'b676 closing')


def _component_commit(s):
    return s.startswith('b676') and not s.startswith(POST_SEAL)


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
    items = j.get('items') or []
    return bool(j) and len(rows) == 53 and rows[52][:3] == ['b676', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b677_' in it] \
        and any(it.startswith('data/b676_q0_lines.txt ') for it in items) \
        and all(any(it.startswith(p + ' ') for it in items) for p in K.SHARED_APPENDED) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b676_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b676') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 677)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The re-cut**', '**The Q0 lines**', '**The strip’s uses**', '**The tools**', '**The root.**',
                 '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b677')


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
    import b676_record as REC
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
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and sorted(f) == sorted(S['kerns_read']) and all(k in n and n[k] == f[k] for k in f)


def corpus_scope(S):
    """PLACE-papers' changed files against the two ledgers (declared: this act writes no README, REGISTRY or faces-page byte)."""
    return S['pp_changed'] == S['pp_allowed']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE NAMING' in t \
        and '### THE RE-CUT' in t and '### THE Q0 LINES' in t and '### THE STRIP USES' in t and '### THE CARRY-TIME REPAIRS' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R286) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: at the start and after the tests, none of tail, lean, lake, python or bash running',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('none of each', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b675_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s and PLACE-papers` branch lists, local and remote-tracking, and the branches bank (the ruling`s list alone)',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b675'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its prompts with their options and results', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS', 'THE ANSWERS'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b676_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: landed(S, 0, ['b675 AT ITS WEIGHT', 'Nothing deposited.', 'Thirteen defects']),
     lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, verdict lines and tag rows printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step): run before the ferry was banked, its one miss entered by the fact clause in the weight line and as the navigator`s (e)',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('RUN BEFORE THE FERRY IS BANKED', 'RUN'))),
    ('G-MIDACT-CHECKED', 'the citation check`s bank ((R278)(4)): each of the two answers checked, its last print with no miss',
     lambda S: midact_ok(S), lambda S: put(S, 'citation', S['citation'].replace("'on the print list'", "'x'"))),
    ('G-R286-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R286) END' in S['ferry'] and S['ot'].count('**(R286) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R286) ratified', '**(R2860) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: five rows through the record tool`s reader, each local, merged and deleted',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-NAMING-BEFORE-BRANCH', 'the naming bank: the rule row and the table rows verbatim before the naming line, the workflow and print bank declared absent, the bank written before the kernel`s first write (N2)',
     lambda S: naming_ok(S), lambda S: _mut(S, 'namingj', lambda d: d.update(at='2026-10-17T23:59:59Z'))),
    ('G-CUT-COMMENT-ONLY', 'the cut`s diff bank and the kernel`s own diff between the print-list main and the cut: one file, its code equal with comments stripped, the control unequal',
     lambda S: cut_comment_ok(S), lambda S: put(S, 'cut_names', S['cut_names'] + ['Trivium/CardDerived.lean'])),
    ('G-PRINTS-EQUAL', 'the prints bank and the runner rows through the record tool`s reader: both runs DERIVES by their ids, the artifacts` digests agreeing, the prints equal line for line',
     lambda S: prints_ok(S), lambda S: put(S, 'prints', S['prints'].replace('EQUAL LINE FOR LINE True', 'EQUAL LINE FOR LINE False'))),
    ('G-CUT-DISTANCE', 'the cut bank: the distance by b670`s method and of any kind at or below before, every matching row pinned by path and line, the residue named (N3)',
     lambda S: distance_ok(S), lambda S: put(S, 'cut', S['cut'].replace('THE DISTANCE BEFORE 5, AFTER 1', 'THE DISTANCE BEFORE 5, AFTER 6'))),
    ('G-CORRESPONDENCE-DRY', 'the generator`s dry bank: no cell changed, no line naming the cut kernel, the run mode not run',
     lambda S: corr_ok(S), lambda S: put(S, 'corr', S['corr'].replace('CELLS CHANGED 0', 'CELLS CHANGED 1'))),
    ('G-Q0-LINES-BANKED', 'the Q0 bank`s hits through the record tool`s reader: each a file, a line, the sentence and a reading; the counts the verdict prints; nothing cut (N4)',
     lambda S: q0_ok(S), lambda S: _mut(S, 'q0', lambda d: d['hits'][0].update(reading='MAYBE'))),
    ('G-Q0-ORDER-ENTERED', 'OPEN_TRAILS at the landing bank`s line, found by conv: W-ORD-Q0-CLASS-LINES, its trigger and Status; its row in the orders bank at that line',
     lambda S: order_ok(S), lambda S: put(S, 'orders', S['orders'].replace('W-ORD-Q0-CLASS-LINES', 'W-ORD-Q0-CLASS'))),
    ('G-STRIP-USES-BANKED', 'the strip bank`s uses, each needle read again on its line at e36ea31 by this run; none unlisted; no Lean written (N4)',
     lambda S: strips_ok(S), lambda S: _mut(S, 'strips', lambda d: d['uses'][0].__setitem__(1, 1))),
    ('G-TOOL-REPAIRS', 'the repairs bank`s verdict and the carried tools` code: the mid-act reader`s cut and the closing`s needle in both wordings',
     lambda S: repairs_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace("the (?:navigator`s )?answer carrying", 'the navigator`s answer carrying'))),
    ('G-SPEC-PLANTED', 'tools/b676_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('Q0' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b676 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b676_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b676_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-trivium`s main, this act`s merged run`s kernel: the workflow file committed alone (dd587f9), the print list committed alone (7074154, 22 names), no .lean byte in either, no author identifier, no secret, the hold, the cache, the print step over print_targets.txt',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.CANDIDATE].update(text=d[K.CANDIDATE]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s merged run`s row (SIDE-trivium after) through the record tool`s reader: the run id and ref, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s merged run`s gate reading: build exit 0, no error line, every terminal of its axioms bank printed, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbank', S['rbank'].replace('GATE DERIVES', 'GATE NOT DERIVES'))),
    ('G-MERGES-ON-GATE', 'SIDE-trivium`s main: the merge commit of the built tip on the print-list main, the merged tree the built tree, its tag v0.1.1 peeled to it',
     lambda S: merges_ok(S), lambda S: _mut(S, 'merges', lambda d: d[K.CANDIDATE]['tags'].clear())),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS and OPEN_TRAILS (declared)',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, SIMPLICITY, README, REGISTRY and the faces page: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read after Component 2`s kernel writes and before the seal, SIDE-trivium among them',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b675`s and the earlier tools, the generator, b667`s certify and map, b671`s narrowing, rowgen`s, the mirror`s, the instruments and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 7e867b61 but the shared additive files (the orders bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b675_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks and the tools',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b676 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b676_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b675`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b675 — lane two, act one hundred and two, the research act' in S['ot']
     and S['rootsf'].count(NL + 'b675 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b675 — lane two', '### b675 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 53rd line, the root bank and its items, the Q0 bank and the orders bank among them', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b677 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b676 AGREE, b676 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b676 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b676_record.py agree', 'b676_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b677', lambda S: '**Next:** b677' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b677', '**Next:** b678'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 7e867b61 and 0b51683 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b676')" in S['suite'] and "'data/b676_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b676_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the naming, the re-cut, the Q0 lines, the strip uses, the repairs',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound request', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, read after every other arm has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
]


def regenerate():
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def seal():
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b676_seal_hashes.json')
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
    print('  written: b676_seal_hashes.json')
    return 0


def _out_name(pushed):
    if PRERUN:
        return 'b676_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b676_checks_postpush.txt' if pushed else 'b676_checks.txt'


def main():
    if SEAL:
        return seal()
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b676 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources()
    S['pushed'] = pushed
    t1 = time.time()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID) else regenerate()
    S['phase_secs']['the table regenerated'] = time.time() - t1
    rec('  ### THE PHASES, IN SECONDS: %s' % '; '.join('%s %.0f' % kv for kv in S['phase_secs'].items()))
    rec('  ### THE LONGEST PHASE %.0f s ; above 450 s: %s (b675 rules row 2: such a run is split at the next act)' % (
        max(S['phase_secs'].values()), max(S['phase_secs'].values()) > 450))
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b675`s face less its own arms) %d ; carried here %d ; the act`s arms over its own banks %s ; '
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
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s ; the mid-act checks: %s' % (mc.group(0) if mc else '### UNREAD',
                                                                   re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation']) or 'NONE'))
    vc = re.search(r'THE DISTANCE BEFORE \d+, AFTER \d+ \(OF ANY KIND \d+, \d+\)', S['cut'])
    rec('  ### THE RE-CUT: %s ; the runs %s ; the Q0 hits %d, TO RE-CUT %s ; the strip`s uses %d' % (
        vc.group(0) if vc else '### UNREAD', [(r.get('label'), r.get('run_id'), r.get('gate')) for r in S['runner'].get('rows') or []],
        len(S['q0'].get('hits') or []), S['q0'].get('recut'), len(S['strips'].get('uses') or [])))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    lv = S['live']
    rec('  ### THE THREE ARMS AT HEAD (seconds %s):' % ', '.join('%.0f' % x for x in lv['secs']))
    rec('  ###   G-NO-SORRY-MAIN read %d kernels` mains, pairs unequal %d; sorry in code %d: %s' % (
        len(lv['nsm']), sum(1 for r in lv['nsm'] if not r['equal']), len(nsm_hits(S)), '; '.join('%s %s:%d' % h for h in nsm_hits(S)) or 'none'))
    rec('  ###   G-AXIOM-CLAIM read %d claims: CONTRADICTED %d, UNVERIFIABLE %d, VERIFIED %d, UNBOUND %d, MENTION %d' % (
        sum(1 for r in lv['ac'] if r['verdict'] != 'OUT OF SCOPE'), ac_count(lv['ac'], 'CONTRADICTED'), ac_count(lv['ac'], 'UNVERIFIABLE'),
        ac_count(lv['ac'], 'VERIFIED'), ac_count(lv['ac'], 'UNBOUND'), ac_count(lv['ac'], 'MENTION')))
    rec('  ###   G-MODULE-HEADER read %d headers: OVERREACHES %d rows %s' % (sum(v['headers'] for v in lv['mh_per'].values()), len(lv['mh']),
                                                                         ['%s %s:%s' % (x.get('kernel'), x.get('file'), x.get('line')) for x in lv['mh']][:6] or ''))
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
    out = os.path.join(D, _out_name(pushed))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b676_arms_prerun.txt', 'b676_lsr_prerun.json').replace('b676_checks', 'b676_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b676_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
