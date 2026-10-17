# -*- coding: utf-8 -*-
"""b679_checks.py -- THE SUITE OF b679, UNDER (R289): b678 AT ITS WEIGHT; THE STRIP VARIANT STATED, PLANNED, ATTEMPTED ON THE RUNNER AND
MERGED (SIDE-explicit-formula v0.33); Q0 READ AGAINST THE WIDENED CLASS; THE MIRROR RESUMED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b678_rules.txt row 1, standing: every run in THREE foreground parts -- `--part standing-a` (the standing arms but two, over the
### three arms at HEAD, the written files, the public bytes and the prior banks), `--part standing-b` (the two standing arms over the act-root
### chain and the shared additive files) and `--part act` (the act's arms over this act's banks, the table regenerated in a closing run) --
### each computing only the sources its arms read, each under the 600 s limit; `--combine <bank>` writes the run's bank.
### ### (R264)(2), THE FREEZE: the standing arms are b678's face's (G2) arms less b678's own arms over b678's banks, carried, their act needles
### read in b679's banks; the act's own arms read this act's banks alone (tools/b679_worklist.py ACT_ARMS). The standing runner arms read this
### act's merged run: SIDE-explicit-formula's run 39064453563 at 46ee9a4, merged at 95f8dc8, v0.33; the workflow on its main unchanged by the act.
### ### Two standing arms read act lists this act's ruling sets, declared on the face: G-PP-SCOPE (PLACE-papers' changed files against the
### two ledgers) and G-CURRENTS-UNEDITED (b678's currents, README, REGISTRY and the faces page among them, unwritten by this act).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b679_record.py).
### ### The harness is b568's to b678's, written by the Write tool from tools/b678_checks.py; the sources, predicates and arms over this act's
### ### banks are b679's.
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
import b679_worklist as K     # noqa: E402
import b678_worklist as K678  # noqa: E402
import b677_worklist as K677  # noqa: E402
import b676_worklist as K676  # noqa: E402
import b675_worklist as K675  # noqa: E402
import b674_worklist as K674  # noqa: E402
from b679_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b679_registration_2026-10-17.txt')
B678_FACE = os.path.join(D, 'b678_registration_2026-10-17.txt')
B678_ACT_ARMS = K678.ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = 'd0493b41'          # ### relay: b678's closing push-out bank, committed at step zero ((R289)(8))
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
PART = sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
INST = K678.SEALED + ('b678_corrigendum.py',) + K677.SEALED + ('b677_epstein_map_angle.py',) + K676.SEALED + K675.SEALED + ('b675_li_bench.py',) + \
    K674.SEALED + (
        'b673_checks.py', 'b673_closing.py', 'b673_tests.py', 'b673_worklist.py', 'b673_reg_gate.py', 'b673_regspec.py', 'b673_record.py',
        'b673_citation.py', 'b673_v4_control.py',
        'b672_checks.py', 'b672_closing.py', 'b672_tests.py', 'b672_worklist.py', 'b672_reg_gate.py', 'b672_regspec.py', 'b672_record.py',
        'b672_citation.py', 'correspondence_gen.py', 'test_correspondence_gen.py',
        'b671_checks.py', 'b671_closing.py', 'b671_tests.py', 'b671_worklist.py', 'b671_reg_gate.py', 'b671_regspec.py', 'b671_record.py',
        'b671_citation.py', 'b671_narrow.py', 'b671_epstein_map_narrowed.py', 'b671_tie_diagnostic.py',
        'b669_record.py', 'b667_epstein_certify.py', 'b667_epstein_map_balls.py', 'b667_tail_recheck.py',
        'b663_epstein_map.py', 'b655_record.py', 'edit_route.py', 'test_edit_route_b646.py', 'b652_record.py', 'b651_record.py',
        'b649_record.py', 'b648_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py', 'b643_record.py', 'b641_record.py',
        'b633_record.py', 'b616_record.py', 'act_root.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py',
        'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py',
        'b616_claims.py', 'ferry_scan.py', 'e0_rule.py', 'test_e0_rule.py', 'build_watch.py', 'chain_page.py',
        'axiom_claim.py', 'licensed_table.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py',
        'test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py',
        'rowgen/rowgen.py', 'rowgen/diff_rowpin.py', 'rowgen/namemap.json')
# ### b678's currents: this act writes no README, REGISTRY or faces-page byte
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md')
TABLE_FILES = K.TABLE_FILES
# ### this act's merged run, read by the standing runner arms
WD, WF, PT = K.KE, '.github/workflows/build-module.yml', 'print_targets.txt'
W_PRE_MAIN, W_TIP, W_TAG, W_RUNS, W_MERGE = K.KREV, K.K_TIP, K.K_NEXT_TAG, K.K_RUNS, K.K_MERGE
CANDIDATE = 'SIDE-explicit-formula'
# ### data/b678_rules.txt row 1: the parts and the sources each part computes
B_ARMS = ('G-ACTROOT-VERIFY', 'G-SHARED-ADDITIVE')        # ### standing-b's arms: the act-root chain and the shared additive files
NEED = {'standing-a': ('live', 'written'), 'standing-b': ('chain', 'additive'), 'act': ()}


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b679')
            and 'data/b679_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b679_record as REC
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
        if f.startswith('b679_') and f.endswith('.py'):
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b679_regspec as SPEC
    import b679_record as REC
    P = SPEC.planted()
    ctl = []
    for f in (lambda: REC.read_score_row('X9', 'HELD'),
              lambda: REC.read_landing_row('  SIDEExplicitFormula.Schema.Wide.x   DERIVES   x.lean:1   [propext]')):
        try:
            f()
            ctl.append(False)
        except Exception:
            ctl.append(True)
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def wf_state():
    t = read_blob(WD, 'main:' + WF)
    pt = read_blob(WD, 'main:' + PT)
    lf = read_blob(WD, 'main:lakefile.toml') + read_blob(WD, 'main:lakefile.lean')
    return {CANDIDATE: dict(text=t, before=read_blob(WD, '%s:%s' % (W_PRE_MAIN, WF)), mathlib='mathlib' in lf.lower(),
                            targets=[l.strip() for l in pt.split(NL) if l.strip()],
                            act_writes=sorted(set(x for x in gs(WD, 'diff', '--name-only', W_PRE_MAIN, 'main').split(NL) if x.strip())))}


def merges_state():
    p = WD
    return {CANDIDATE: dict(main=gs(p, 'rev-parse', '--short=7', 'main'), parents=gs(p, 'log', '-1', '--format=%p', '--abbrev=7', 'main').split(),
                            built=W_TIP[:7], tree_main=gs(p, 'rev-parse', 'main^{tree}'), tree_built=gs(p, 'rev-parse', W_TIP + '^{tree}'),
                            tags=dict((t, gs(p, 'rev-parse', '--short=7', t + '^{commit}')) for t in gs(p, 'tag', '--points-at', 'main').split()))}


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted(set(g2_of(B678_FACE)) - set(B678_ACT_ARMS))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


def _ct_first(repo, pre, prefix, path=None):
    args = ['log', '--reverse', '--format=%ct %s', pre + '..HEAD'] + (['--', path] if path else [])
    for l in gs(repo, *args).split(NL):
        if l.strip() and l.split(' ', 1)[1].startswith(prefix):
            return int(l.split(' ', 1)[0])
    return None


def sources(need=()):
    """the sources the arms read; `need` (by part, data/b678_rules.txt row 1) names the heavy phases this part computes: 'live' (the three
    arms at HEAD), 'written' (the written files, the public bytes, the prior banks), 'chain' (the act-root chain), 'additive' (the shared files)."""
    import b679_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b679_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b679_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b679_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b679_ferry.txt'), scan=rd('b679_ferry_scan.txt'), stepz=rd('b679_stepzero.txt'),
        readfirst=rd('b679_readfirst.txt'), defects=rd('b679_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b679_author_answers.txt'), prerun=rd('b679_arms_prerun.txt'), rl=jl('b679_record_lines.json'),
        rlo=jl('b679_record_lines_order.json'),
        tests=jl('b679_tests_stepzero.json'), testst=rd('b679_tests_stepzero.txt'), withheld=jl('b679_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b679_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), cmdj=jl('b679_commands.json'), cmdt=rd('b679_commands.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b679_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        c1_ct=_ct_first(PP, PRE['pp'], 'b679 Component 1'),
        gate=rd('b679_reg_gate.txt'), rowgen=rd('b679_rowgen_stepzero.txt'),
        branchj=jl('b679_branches.json'), branchest=rd('b679_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '-a', '--list', *(list(bs) + ['*/' + b for b in bs]))) for repo, bs in K.DELETE),
        orders=rd('b670_work_orders.txt'),
        plan=rd('b679_strip_plan.txt'), plan_ct=int(gs(ROOT, 'log', '-1', '--format=%ct', K.PLAN_COMMIT) or 0),
        lean_ct=int(gs(WD, 'log', '-1', '--format=%ct', W_RUNS[0][1]) or 0),
        landing=rd('b679_landing.txt'), landingj=jl('b679_landing.json'), prints=rd('b679_prints_compare.txt'),
        walk=rd('b679_zeta_walk_%s.txt' % W_TIP[:7]), walk0=rd('b679_zeta_walk.txt'),
        memb=jl('b679_q0_membership.json'), membt=rd('b679_q0_membership.txt'), onset=jl('b679_onset.json'), onsett=rd('b679_onset.txt'),
        main_src=dict((f, read_blob(WD, 'main:' + f)) for f in K.WIDE_FILES),
        rules=rd('b678_rules.txt'),
        repairs=rd('b679_tool_repairs.txt'), citation_src=read(os.path.join(T, 'b679_citation.py')),
        standing=STANDING, wf=wf_state(), runner=jl('b679_runner_rows.json'), rbank=rd('b679_runner_run%d.txt' % W_RUNS[-1][0]),
        ax_after=rd('b679_axioms_run%d.txt' % W_RUNS[-1][0]), merges=merges_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b679_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b679_act_root.json'), arj0=jl('b678_act_root.json'), art=rd('b679_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b679_kernels_face.json').get('kernels') or {}), kerns_read=[k for k in REC._kerns() if k != CANDIDATE],
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b679_mustnotexist.txt')),
        fj=jl('b679_findings.json'), tj=jl('b679_trail.json'), sc=jl('b679_scores.json'), desk=rd('b679_desk_notes.txt'), tfj=jl('b679_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['phase_secs'] = {'the banks and the state': time.time() - t0}
    S['pp_allowed'] = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'])
    t1 = time.time()
    S['live'] = live_arms() if 'live' in need else dict(names=[], nsm=[], ac=[], ac_counts={}, mh=[], mh_per={}, secs=(0, 0, 0))
    S['phase_secs']['the three arms at HEAD' + ('' if 'live' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    S['pp_changed'] = sorted(ch)
    S['ledger_adds'] = appended(S['fi_pre'], S['fi_now']) + NL + appended(S['ot_pre'], S['ot_now'])
    S['globs'] = wl_globs(face)
    S['outside'] = [n for n in R41.OAI_NEEDLES if n in S['ledger_adds']]
    if 'written' in need:
        S['written'] = written_files()
        S['nd_sets'] = R6.nd_sets()
        pub = [S['ledger_adds']]
        for f in sorted(os.listdir(D)):
            if f.startswith(('b679_', 'audit_b679_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith('.gz'):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
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
    else:
        S['written'], S['nd_pub'], S['prior_bad'], S['prior_n'] = [], {}, [], 0
    S['phase_secs']['the written files, the public bytes and the prior banks' + ('' if 'written' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S['bank_mtimes'] = {}
    for it in (S['arj'].get('items') or []):
        p = it.split()[0]
        if p.startswith('data/') and os.path.exists(os.path.join(ROOT, *p.split('/'))):
            S['bank_mtimes'][p] = os.path.getmtime(os.path.join(ROOT, *p.split('/')))
    import act_root as AR
    S['order_slack'] = AR.ORDER_SLACK
    if 'chain' in need:
        try:
            S['ar_verify'] = AR.verify(remote=KC0.remote_refs)
            S['ar_reads'] = dict(AR.READS_AT)
        except Exception as e:
            S['ar_verify'], S['ar_reads'] = [('raised', type(e).__name__, [])], {}
    else:
        S['ar_verify'], S['ar_reads'] = [], {}
    S['phase_secs']['the act-root chain' + ('' if 'chain' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    if 'additive' in need:
        try:
            S['additive'] = ADD.check(worktree=True)
        except Exception as e:
            S['additive'] = [('raised', type(e).__name__, [('x', [])])]
    else:
        S['additive'] = []
    S['phase_secs']['the shared additive files' + ('' if 'additive' in need else ' (not in this part)')] = time.time() - t1
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
    return ' '.join(' '.join(re.sub(r'^\s*(?:###\s*)+', '', l) for l in t.split(NL)).split())


def procs_ok(S):
    """the step-zero bank's process listings, in this act's words (data/b679_stepzero.txt): none of the named before the tests; after the
    tests one match, read as not this session's and not a lean process, nothing stopped."""
    p = unwrap(S['stepz'])
    return 'names tail, lean, lake, python: none of each' in p and 'after the tests: one match, PID 29688 cleanmgr.exe' in p \
        and 'not a lean process, not stopped' in p and 'no orphan, nothing stopped by PID' in p


STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 2' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    """the answers bank as it prints: this act put one call of three questions, each with its options and its result, and banked the
    author's three words."""
    a = S['answers']
    m = re.search(r'^### b679 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    if not m or int(m.group(1)) != len(heads) or len(heads) != 3 or len(calls) != 1:
        return False
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    return all(x >= 2 for x in per) and len(res) == len(calls) and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) \
        and len(re.findall(r'^### THE AUTHOR`S WORD ', a, re.M)) == 3


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def no_local_lean(S):
    import b679_record as REC
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


# ================================================================== (R289) STEP ZERO: THE CITATION CHECK, THE BRANCHES, ROWGEN
READFIRST_NEEDLES = ('data/b678_closing.txt', 'data/b678_defects.txt', 'data/b678_cut.txt', 'data/b676_strip_uses.txt', 'data/b675_hypotheses.txt',
                     'data/b675_li_plan.txt', 'data/b675_li_bench.txt', 'data/b675_li_constants.json', 'data/b673_v4v5_plan.txt',
                     'data/b673_landing.txt', 'Zeta23/Defs.lean :126-:146', 'RestBound.lean :40', 'data/b667_epstein_plan.txt',
                     'data/b671_epstein_zeros_narrowed.json.gz', 'data/b572_lemmas.txt', 'data/b670_work_orders.txt', 'tools/mirror_build.ps1',
                     'data/b678_closing_push_out.txt')


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """the branches (R289)(8) names: none left in its repository, local or remote-tracking; the branches bank lists them, each with its tip."""
    z = S['branchest']
    named = [b for _r, bs in K.DELETE for b in bs]
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 3 and all(b in z for b in named) \
        and 'BRANCHES 9 (LOCAL 8, REMOTE 1) ; MERGED OR ANCESTOR 9 ; TO BE DELETED 9' in z


def branches_banked_ok(S):
    import b679_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 9 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and [r['where'] for r in rows].count('remote') == 1 and [r['branch'] for r in rows if r['where'] == 'remote'] == ['recut-silence-principle-b678']


def deletes_one_ok(S):
    """(R289)(8): every branch delete command names one branch and carries no glob in any half, read from the capture by the record tool's
    own reader and from the command bank; the branches deleted the ruling's list exactly, the one remote delete among them."""
    import b679_record as REC
    shapes = [REC.delete_shape(r['cmd']) for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [s for s in shapes if s[0]]
    named = sorted([b for _r, bs in K.DELETE for b in bs] + [b for _r, b in K.DELETE_REMOTE])
    return bool(shapes) and all(len(d) == 1 and not gl for d, gl in shapes) and sorted(x for d, _g in shapes for x in d) == named \
        and 'BRANCH DELETES OF ONE BRANCH AND NO GLOB 9 OF 9' in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b679 closed:' in g and 'the misses as the bank lists them' in g and '(annotated, peeled) ; main' in g \
        and '### THE PLAN' in g and '### THE ATTEMPT' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the step-zero check: run before the ferry was banked; its one miss, the narrowed ball bank cited as .json and present as .json.gz,
    raised to the author before Component 4 (the plan bank's == 9 (Q3)) and entered as the navigator's (b); Component 1 committed after it."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'RUN BEFORE THE FERRY IS BANKED' in c \
        and int(m.group(3)) == 1 == len(S['cit_misses']) and 'b671_epstein_zeros_narrowed.json' in S['cit_misses'][0] \
        and '(Q3) the citation check`s miss' in S['plan'].replace("'", '`') and "(b) THE NAVIGATOR'S" in S['defects'] \
        and S['c1_ct'] is not None and S['cit_at'] and S['cit_at'] < S['c1_ct']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


# ================================================================== (R289)(3): THE ORDER
def order_entered_ok(S):
    """the order's line at OPEN_TRAILS by the landing bank, found by conv, carrying its trigger, Status and consumers; its row in the orders
    bank through the record tool's reader: OPEN, the trigger the re-cut act after b680, at that line."""
    import b679_record as REC
    x = rline(S, 0, 'rlo')
    ok1 = landed(S, 0, ['W-ORD-CORRESPONDENCE-RUNNER-BANKS', 'Trigger: the re-cut act after b680', 'Status OPEN', ':628–:630'], key='rlo')
    got = None
    for l in S['orders'].split(NL):
        try:
            o, st, tr = REC.read_order_row(l)
        except Exception:
            continue
        if o == 'W-ORD-CORRESPONDENCE-RUNNER-BANKS':
            got = (st, tr, l)
    return ok1 and bool(got) and got[0] == 'OPEN' and got[1] == 'the re-cut act after b680' and (':%s ' % x.get('line')) in got[2]


# ================================================================== (R289)(5): THE PLAN BEFORE ANY LEAN
def plan_ok(S):
    """N2: the plan prints the form with its reason and the exclusion beside :231, every one of the 22 uses re-priced (the bank's rows :9-:30
    each once at == 2), committed before the first Lean write (the kernel commit of the first tree state)."""
    p = S['plan']
    sec2 = p[p.find('== 2.'):p.find('== 3.')]
    rows = sorted(int(x) for x in re.findall(r'^    :(\d+) ', sec2, re.M))
    return '== 0. THE FORM CHOSEN, WITH ITS REASON (N2)' in p and 'A SECOND CONFIGURATION STRUCTURE' in p \
        and 'THE EXCLUSION\'S STATEMENT BESIDE IT: "∀ ρ ∈ Z.carrier, ρ.im = 0 → 0 < ρ.re"' in p and rows == list(range(9, 31)) \
        and S['plan_ct'] and S['lean_ct'] and S['plan_ct'] < S['lean_ct'] and '== 11. THE AUTHOR\'S WORD ON THIS PLAN' in p


def answers_checked_ok(S):
    """(R278)(4): each of the three answers checked before the seat acted on it -- three mid-act prints in the citation bank, each before the
    first Lean write."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the answer carrying \'([^\']+)\'', c)
    return len(stamps) == 3 and all(iso_epoch(t) and S['lean_ct'] and iso_epoch(t) < S['lean_ct'] for t, _n in stamps) \
        and sorted(n for _t, n in stamps) == sorted(['ANSWER on the plan, under (R289)(5)', 'ANSWER on the control, under (R289)(5)(v)',
                                                    'ANSWER on the ball bank'])


# ================================================================== (R289)(6)-(7): THE ATTEMPT, THE MERGE, THE READINGS
def landing_ok(S):
    """N3: each declaration one landing banked: 20 rows through the record tool's reader, every one DERIVES, no sorry in the files, the split
    rule's line; and on main the three files carry no sorry."""
    import b679_record as REC
    rows = []
    for l in S['landing'].split(NL):
        try:
            rows.append(REC.read_landing_row(l))
        except ValueError:
            pass
    main_sorry = [f for f, t in S['main_src'].items() if re.search(r'\bsorry\b', REC._strip_lean_comments(t))]
    return len(rows) == 20 and all(g_ == 'DERIVES' for _n, g_ in rows) and S['landingj'].get('sorry') == [] and not main_sorry \
        and all(S['main_src'].values()) and 'DECLARATIONS 20 ; DERIVES 20 ; OPEN 0 ; SORRY IN THE FILES 0' in S['landing'] \
        and 'the branch merged whole; no declaration left open' in S['landing']


def v032_prints_ok(S):
    return 'v0.32 NAMES 29 ; PRINTED AFTER 29 ; EQUAL 29 ; DIFFERING 0' in S['prints'] and 'b673_axioms_run38960681935.txt' in S['prints']


def walk_ok(S):
    """N4: the walk where S5' lands reads 0 ζ objects at the merged tip, its control reaching ζ; the first tree state's reading (22, by the
    namesake) kept as written and named in the defects bank."""
    m = re.search(r'DECLARATIONS REACHED (\d+) \(IN Schema/Wide/ (\d+)\) ; ζ-NAMING (\d+) ; THE CONTROL (\d+)', S['walk'])
    m0 = re.search(r'ζ-NAMING (\d+) -- ', S['walk0'])
    return bool(m) and int(m.group(3)) == 0 and int(m.group(4)) > 0 and int(m.group(2)) > 0 and W_TIP[:7] in S['walk'] \
        and bool(m0) and int(m0.group(1)) == 22 and "(e) THE SEAT'S: A NAMESAKE" in S['defects']


def runs_ok(S):
    """N1: one dispatch per tree state, each run read by its id, its artifact's sha256 agreeing, both DERIVES, the refs the branch's two tips
    and their trees distinct; two dispatch commands in the capture."""
    import b679_record as REC
    rows = S['runner'].get('rows') or []
    try:
        gates = [REC.read_runner_row(r) for r in rows]
    except Exception:
        return False
    trees = set(gs(WD, 'rev-parse', r['ref'] + '^{tree}') for r in rows)
    return [(r['run_id'], r['ref']) for r in rows] == [(i, f) for i, f in W_RUNS] and all(g_ == 'DERIVES' for _i, g_ in gates) \
        and all(r.get('artifact_sha256') for r in rows) and len(trees) == 2 and 'DISPATCHES 2 ;' in S['cmdt']


def membership_ok(S):
    j = S['memb']
    return j.get('h4') == 'HELD' and j.get('gz_ok') and j.get('json_ok') and j.get('excl') and j.get('band_ok') and not j.get('any_real') \
        and bool(j.get('balls')) and all(b[4] and b[5] for b in j['balls']) and (j.get('z0') or '').startswith('-1.000') \
        and 'ASSUMED -- T-COUNT' in S['membt'] and 'H4 HELD' in S['membt']


def onset_ok(S):
    j = S['onset']
    return j.get('h5') == 'HELD' and j.get('n_star') == 63676 and j.get('n_obs') == 10034 and j.get('n_obs') <= j.get('n_star') \
        and j.get('same_C') is True and j.get('on_sub') == j.get('neg_on') and j.get('window') == 201 and 'H5 HELD' in S['onsett']


def controls_ok(S):
    rows = dict((r['name'].split('.')[-1], r['landing']) for r in S['landingj'].get('rows') or [])
    c = S['main_src'].get('SIDEExplicitFormula/Schema/Wide/Converse.lean', '')
    return rows.get('c2_not_excl') == 'DERIVES' and rows.get('c2b_nonneg_offline') == 'DERIVES' \
        and 'theorem c2_not_excl : ¬ HExcl c2Config' in c and 'carrier := {((-1 / 4 : ℝ) : ℂ), ((5 / 4 : ℝ) : ℂ)}' in c


def hypotheses_ok(S):
    t = S['landing']
    return all(('  (%s) HELD --' % h) in t for h in ('H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H6b')) and 'THE FACES PAGE`S LINE ON THE LI FACE AT Q0' in t


def repairs_ok(S):
    return '### ### **REPAIRS 3 ; THE SEALED COPIES AGREE ; TOOLS CARRIED 8.**' in S['repairs'] and "rfind('BEGIN', 0, k)" in S['citation_src'] \
        and "B_ARMS = ('G-ACTROOT-VERIFY', 'G-SHARED-ADDITIVE')" in S['suite']


def parts_ok(S):
    """data/b678_rules.txt row 1, standing: the pre-run bank printing the three parts with their seconds."""
    return '(1) THE STANDING ARMS IN TWO FOREGROUND PARTS, THE ACT`S IN ONE' in S['rules'] \
        and all(re.search(r'PART %s : ARMS \d+ ; \d+ s' % p, S['prerun']) for p in K.PARTS)


def defects_ok(S):
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", S['defects'], re.M)
    return [x for x, _o in letters] == list('abcde') and [x for x, o in letters if o == 'NAVIGATOR'] == list('abc') \
        and [x for x, o in letters if o == 'SEAT'] == list('de')


# ================================================================== THE RUNNER (the standing arms, this act's merged run)
def wf_ok(S):
    """the workflow on SIDE-explicit-formula's main: unchanged by the act (equal to e36ea31's), no author identifier, no secret, the hold,
    the cache step where Mathlib is required, the print step over print_targets.txt, the list the 49 names; the act's main writes the three
    new files and the list alone."""
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or v['text'] != v['before']:
            return False
        if any(w in t for w in ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'print_targets.txt' not in t or 'lake env lean out/axioms.lean' not in t \
                or (('lake exe cache get' in t) != v['mathlib']) or len(v['targets']) != 49 or v['act_writes'] != sorted(K.K_FILES):
            return False
    return len(S['wf']) == 1


def runner_ok(S):
    import b679_record as REC
    rows = [r for r in S['runner'].get('rows') or [] if r.get('run_id') == W_RUNS[-1][0]]
    if len(rows) != 1:
        return False
    r = rows[0]
    REC.read_runner_row(r)
    return r['ref'] == W_TIP and r['conclusion'] == 'success' and bool(r['artifact_sha256']) and r['mem_low'] is not None \
        and r['mem_low'] >= K.HOLD and not r['stopped']


def gate_ok(S):
    rows = [r for r in S['runner'].get('rows') or [] if r.get('run_id') == W_RUNS[-1][0]]
    n = len(re.findall(r"^'[^']+' (?:depends on axioms|does not depend on any axioms)", S['ax_after'], re.M))
    return bool(rows) and rows[0].get('gate') == 'DERIVES' and 'GATE DERIVES' in S['rbank'] \
        and ('TERMINALS PRINTED %d OF %d ; SORRYAX 0' % (n, n)) in S['rbank'] and n > 0 \
        and 'BUILD EXIT 0 ; ERROR LINES 0' in S['rbank'] and re.search(r'^### the artifact: .* ; AGREE$', S['rbank'], re.M) is not None


def merges_ok(S):
    for k, m in S['merges'].items():
        if m['main'] != W_MERGE or m['parents'] != [W_PRE_MAIN, W_TIP[:7]] or m['built'] not in m['parents'] \
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


POST_SEAL = ('b679 seal', 'b679 pre-root', 'b679 root', 'b679 record', 'b679 --', 'b679 closing')


def _component_commit(s):
    return s.startswith('b679') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 56 and rows[55][:3] == ['b679', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b680_' in it or 'mirror' in it] \
        and any(it.startswith('data/b679_strip_plan.txt ') for it in items) and any(it.startswith('data/b679_landing.txt ') for it in items) \
        and all(any(it.startswith(p + ' ') for it in items) for p in K.SHARED_APPENDED) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b679_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b679') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 680)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The statement**', '**The attempt**', '**The readings**', '**The root.**', '**The scores.**',
                 '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b680')


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
    return bool(S['globs']) and bool(S['written']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    import b679_record as REC
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
    return S['pp_changed'] == S['pp_allowed']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE PLAN' in t \
        and '### THE ATTEMPT' in t and '### THE READINGS' in t and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R289) END' in S['ferry'] and S['ferry'].rstrip().endswith('FERRY END'),
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: before the tests none of tail, lean, lake or python; after them one match read as not a lean process and not stopped',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('none of each', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b678_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s, PLACE-papers` and SIDE-silence-principle`s branch lists, local and remote-tracking, and the branches bank (the ruling`s list alone)',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b678'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: one call of three prompts, each with its options and result, the author`s three words', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS, 3 prompt(s)', 'THE AUTHOR`S ANSWERS, 0 prompt(s)'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b679_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: landed(S, 0, ['b678 AT ITS WEIGHT', 'Nothing deposited.', 'Two defects']),
     lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, verdict lines and tag rows printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step): run before the ferry was banked, its one miss raised in the plan`s prompt and entered as the navigator`s (b)',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('RUN BEFORE THE FERRY IS BANKED', 'RUN'))),
    ('G-R289-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R289) END' in S['ferry'] and S['ot'].count('**(R289) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R289) ratified', '**(R2890) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: nine rows through the record tool`s reader, eight local and the one remote, each merged or an ancestor, each deleted',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob in any half, the ruling`s list exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b678 push-b678-root")])),
    ('G-ORDER-ENTERED', 'OPEN_TRAILS at the landing bank`s line, found by conv, and the orders bank`s row through the record tool`s reader: OPEN, its trigger, its consumers',
     lambda S: order_entered_ok(S), lambda S: put(S, 'orders', S['orders'].replace('OPEN             :%s' % rline(S, 0, 'rlo').get('line'), 'CLOSED           :%s' % rline(S, 0, 'rlo').get('line')))),
    ('G-PLAN-BEFORE-LEAN', 'the plan bank and the two commit times: the form with its reason, the exclusion beside :231, the 22 uses re-priced, committed before the first Lean write (N2)',
     lambda S: plan_ok(S), lambda S: put(S, 'plan_ct', S['lean_ct'] + 1)),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints: each of the three answers checked before the first Lean write ((R278)(4))',
     lambda S: answers_checked_ok(S), lambda S: put(S, 'citation', S['citation'].replace('THE MID-ACT CHECK', 'A CHECK', 1))),
    ('G-LANDING-DERIVES', 'the landing bank`s rows through the record tool`s reader and the three files on main: 20 DERIVES, no sorry, the branch merged whole (N3)',
     lambda S: landing_ok(S), lambda S: put(S, 'landing', S['landing'].replace('DERIVES      SIDEExplicitFormula/Schema/Wide/Converse.lean:191', 'NOT DERIVES  SIDEExplicitFormula/Schema/Wide/Converse.lean:191'))),
    ('G-V032-PRINTS-EQUAL', 'the prints bank: the 29 v0.32 names against b673`s run at the v0.32 tree, equal (N3)',
     lambda S: v032_prints_ok(S), lambda S: put(S, 'prints', S['prints'].replace('DIFFERING 0', 'DIFFERING 1'))),
    ('G-WALK-ZERO', 'the walk banks: 0 ζ-naming at the merged tip with the control reaching ζ; the first tree state`s 22 by the namesake, named in the defects (N4)',
     lambda S: walk_ok(S), lambda S: put(S, 'walk', S['walk'].replace('ζ-NAMING 0 ;', 'ζ-NAMING 1 ;'))),
    ('G-RUNS-ONE-PER-STATE', 'the runner rows through the record tool`s reader and the command bank: two runs by id at the two tips, two trees, two dispatches, both DERIVES with the artifact agreeing (N1)',
     lambda S: runs_ok(S), lambda S: _mut(S, 'runner', lambda d: d['rows'].append(dict(d['rows'][-1])))),
    ('G-Q0-MEMBERSHIP', 'the membership bank: the ball bank`s hashes equal, the strip and the exclusion read with their sources, every ball on [-1/2, 0] negative, Z_Q(0) = -1, T-COUNT assumed (H4, N4)',
     lambda S: membership_ok(S), lambda S: _mut(S, 'memb', lambda d: d['balls'][0].__setitem__(5, False))),
    ('G-ONSET-H5', 'the onset bank: n*` 63676 from the widened constants, n_obs 10034 below it, every n on V4`s subsequence in the window NEG (H5)',
     lambda S: onset_ok(S), lambda S: _mut(S, 'onset', lambda d: d.update(neg_on=0))),
    ('G-CONTROLS-LANDED', 'the landing bank and Converse.lean on main: C2 and C2b DERIVES, C2 the point -1/4 with its reflection (H6, H6b, N4)',
     lambda S: controls_ok(S), lambda S: put(S, 'main_src', dict(S['main_src'], **{'SIDEExplicitFormula/Schema/Wide/Converse.lean': ''}))),
    ('G-HYPOTHESES-READ', 'the landing bank`s readings of H1-H6 and H6b, and the faces line drafted', lambda S: hypotheses_ok(S),
     lambda S: put(S, 'landing', S['landing'].replace('(H5) HELD --', '(H5) REFUTED --'))),
    ('G-TOOL-REPAIRS', 'the carry-time bank`s verdict and the carried tools` code: three repairs, the sealed copies agreeing, the mid-act cut carried',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS 3 ;', 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', 'data/b678_rules.txt row 1 and the pre-run bank`s three parts with their seconds',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART act', 'PART whole'))),
    ('G-DEFECTS-LETTERED', 'the defects bank: (a)-(e), (a)-(c) the navigator`s, (d)-(e) the seat`s', lambda S: defects_ok(S),
     lambda S: put(S, 'defects', S['defects'].replace("(e) THE SEAT'S", "(e) THE NAVIGATOR'S"))),
    ('G-SPEC-PLANTED', 'tools/b679_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('landing' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b679 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b679_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b679_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-explicit-formula`s main, this act`s merged run`s kernel: the workflow unchanged by the act, no author identifier, no secret, the hold, the cache step where Mathlib is required, the print step over the 49-name list; the act`s writes the three files and the list',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[CANDIDATE].update(text=d[CANDIDATE]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s merged run`s row (run 39064453563) through the record tool`s reader: the ref, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s merged run`s gate reading: build exit 0, no error line, every terminal of its axioms bank printed, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbank', S['rbank'].replace('GATE DERIVES', 'GATE NOT DERIVES'))),
    ('G-MERGES-ON-GATE', 'SIDE-explicit-formula`s main: the merge commit of the built tip on e36ea31, the merged tree the built tree, its tag v0.33 peeled to it',
     lambda S: merges_ok(S), lambda S: _mut(S, 'merges', lambda d: d[CANDIDATE]['tags'].clear())),
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
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, SIMPLICITY, README, REGISTRY, the faces page and FOUNDATIONS: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read after Component 4`s merge and before the seal, SIDE-explicit-formula apart (its writes read by G-MERGES-ON-GATE)',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b678`s and the earlier tools, b678`s corrigendum tool, the generator, b667`s certify (imported by this act) and map, b671`s narrowing, rowgen`s, the mirror`s, the instruments and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 435ceb1f but the shared additive files (the orders bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b678_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks and the tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b679 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b679_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in three parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b678`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b678 — lane two, act one hundred and five, the re-cut act' in S['ot']
     and S['rootsf'].count(NL + 'b678 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b678 — lane two', '### b678 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 56th line, the root bank and its items, the plan, landing and orders banks among them, no mirror bank', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b680 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b679 AGREE, b679 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b679 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b679_record.py agree', 'b679_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b680', lambda S: '**Next:** b680' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b680', '**Next:** b681'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 435ceb1f and 935f8df against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b679')" in S['suite'] and "'data/b679_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b679_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the plan, the attempt, the readings, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound request', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
]


def _part_of(name):
    return 'act' if name in K.ACT_ARMS else ('standing-b' if name in B_ARMS else 'standing-a')


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
    p = os.path.join(D, 'b679_seal_hashes.json')
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
    print('  written: b679_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b679_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b679_checks_postpush.txt' if pushed else 'b679_checks.txt'


def _part_name(base, part):
    return base.replace('.txt', '_%s.txt' % part)


def _write(name, lines):
    out = os.path.join(D, name)
    b = (NL.join(lines) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    return out


PART_FOOT = re.compile(r'### PART ([\w-]+) : ARMS (\d+) ; LIVE PASSING (\d+) ; LIVE FAILING (\d+) (\[[^\]]*\]|NONE) ; NEGATIVE-CONTROL FAILURES (\d+) ; '
                       r'POSITIVE-CONTROL PASSES (\d+) (\[[^\]]*\]|NONE) ; DECLARED EQ RUN (\w+) ; (\d+) s')


def combine():
    """data/b678_rules.txt row 1: the run's bank from its three part banks, the counts summed and every part's seconds printed at its head;
    the parts' banks carried whole beneath."""
    base = sys.argv[sys.argv.index('--combine') + 1]
    parts, heads = [], []
    for part in K.PARTS:
        t = rd(_part_name(base, part))
        m = PART_FOOT.search(t)
        if not m or m.group(1) != part:
            print('### THE PART BANK %s HAS NO FOOTER -- NOTHING WRITTEN' % _part_name(base, part))
            return 2
        parts.append((part, m, t))
        heads.append(t.split(NL)[1] if len(t.split(NL)) > 1 else '')
    n = sum(int(m.group(2)) for _p, m, _t in parts)
    lp = sum(int(m.group(3)) for _p, m, _t in parts)
    lf = sum(int(m.group(4)) for _p, m, _t in parts)
    ng = sum(int(m.group(6)) for _p, m, _t in parts)
    pc = sum(int(m.group(7)) for _p, m, _t in parts)
    fails = sum((json.loads(m.group(5)) if m.group(5) != 'NONE' else [] for _p, m, _t in parts), [])
    defs = sum((json.loads(m.group(8)) if m.group(8) != 'NONE' else [] for _p, m, _t in parts), [])
    deq = all(m.group(9) == 'True' for _p, m, _t in parts)
    ok = lf == 0 and pc == 0 and ng == 0 and deq
    out = ['=' * 104, heads[0].replace('PART standing-a', 'THREE PARTS SUMMED (data/b678_rules.txt row 1)'), '=' * 104] + [
        '  ### PART %s : ARMS %s ; %s s' % (p, m.group(2), m.group(10)) for p, m, _t in parts] + [
        '  ### the parts` seconds summed %d ; the longest part %s s, under the 600 s limit %s' % (
            sum(int(m.group(10)) for _p, m, _t in parts), max(int(m.group(10)) for _p, m, _t in parts),
            max(int(m.group(10)) for _p, m, _t in parts) < 600),
        '  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (n, lp, lf, fails or ''),
        '  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (ng, pc, defs or ''),
        '  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'), '=' * 104, '']
    for p, _m, t in parts:
        out += ['### THE PART BANK %s, WHOLE:' % _part_name(base, p)] + t.rstrip(NL).split(NL) + ['']
    _write(base, out)
    ex = {}
    for part in K.PARTS:
        ex.update(jl('b679_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b679_checks.txt', 'b679_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b679_exercise.json')
        open(p_ + '.tmp', 'wb').write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:11]))
    print('  written: %s' % base)
    return 0 if ok else 1


def main():
    if SEAL:
        return seal()
    if COMBINE:
        return combine()
    if PART not in K.PARTS:
        print('### data/b678_rules.txt row 1: every run in three foreground parts -- give `--part %s`' % ' | '.join(K.PARTS))
        return 2
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b679 -- THE SUITE. ### **%s READING.** ### PART %s (data/b678_rules.txt row 1) ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH', PART))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources(NEED[PART])
    S['pushed'] = pushed
    t1 = time.time()
    regen = PART == 'act' and not (RERUN or PRERUN or MID)
    rc_gen, gen_diff = regenerate() if regen else (0, dict(rerun=True))
    S['phase_secs']['the table regenerated' + ('' if regen else ' (not in this part or run)')] = time.time() - t1
    rec('  ### THE PHASES, IN SECONDS: %s' % '; '.join('%s %.0f' % kv for kv in S['phase_secs'].items()))
    rec('  ### THE LONGEST PHASE %.0f s ; above 450 s: %s (b675 rules row 2)' % (max(S['phase_secs'].values()), max(S['phase_secs'].values()) > 450))
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    arms = [a for a in ARMS if _part_of(a[0]) == PART]
    rec('  arms in the (G2) block : %d ; in the suite : %d ; run in this part : %d' % (len(declared), len(names), len(arms)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b678`s face less its own arms) %d ; carried here %d ; the act`s arms over its own banks %s ; '
        'arms beyond both %s' % (len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
                                sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'chain' in NEED[PART]:
        av = S['ar_verify']
        rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    rec('  ### G-EDIT-ROUTE read %d captured commands; offences %d: %s' % (len(S['cmds']), len(S['ER'].scan(S['cmds'])),
                                                                         ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in S['ER'].scan(S['cmds'])] or 'none'))
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s ; THE LANDING: %s ; THE WALK: %s' % (
        mc.group(0) if mc else '### UNREAD', (re.search(r'DECLARATIONS \d+ ; DERIVES \d+ ; OPEN \d+', S['landing']) or [None])[0] if
        re.search(r'DECLARATIONS \d+ ; DERIVES', S['landing']) else '### UNREAD',
        (re.search(r'ζ-NAMING \d+', S['walk']) or [None])[0] if re.search(r'ζ-NAMING', S['walk']) else '### UNREAD'))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    if 'live' in NEED[PART]:
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
    for name, reads, pred, pos in arms:
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
    if 'written' in NEED[PART]:
        rec('  ### tracked files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                              if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
        rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this part, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if regen:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), (gen_diff.get('changed') or '')[:20]))
    secs = time.time() - t_start
    rec('  ### the run took %.0f s' % secs)
    rec('  ### PART %s : ARMS %d ; LIVE PASSING %d ; LIVE FAILING %d %s ; NEGATIVE-CONTROL FAILURES %d ; POSITIVE-CONTROL PASSES %d %s ; '
        'DECLARED EQ RUN %s ; %d s' % (PART, len(arms), len(arms) - len(fail), len(fail), json.dumps(fail) if fail else 'NONE', negfail, len(defective),
                                       json.dumps(defective) if defective else 'NONE', S['declared_eq_run'], int(secs)))
    rec('=' * 104)
    base = _base_name(pushed)
    out = _write(_part_name(base, PART), L)
    lp = os.path.join(D, _part_name(base, PART).replace('b679_arms_prerun', 'b679_lsr_prerun').replace('b679_checks', 'b679_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b679_exercise_%s.json' % PART)
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
