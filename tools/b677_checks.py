# -*- coding: utf-8 -*-
"""b677_checks.py -- THE SUITE OF b677, UNDER (R287): b676 AT ITS WEIGHT; THE DETECTION MAP IN THE ANGLE FORM OVER THE NARROWED BALLS; THE
CONTROLS RE-READ; H3 AND H4 READ WITH THE CONSUMER'S TOLERANCE MEASURED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R287)(7): EVERY RUN IN TWO FOREGROUND PARTS -- `--part standing` (the standing arms, over the whole sources: the three arms at HEAD,
### the act-root chain, the shared additive files) and `--part act` (the act's arms, over this act's banks; the light sources alone; the table
### regenerated here in a closing run) -- each under the 600 s limit, then `--combine <bank>` writes the run's bank with the counts summed
### and both parts' seconds printed (data/b677_rules.txt row 1).
### ### (R264)(2), THE FREEZE: the standing arms are b676's face's (G2) arms less b676's own arms over b676's banks, carried, their act needles
### read in b677's banks (b676 at its weight, the branches (R287)(6) names, this act's step-zero bank); the act's own arms read this act's
### banks alone (tools/b677_worklist.py ACT_ARMS). The standing runner arms read the last merged run, b676's: SIDE-trivium's run 39004541707 at
### db315fe, merged at 135be2e, v0.1.1 -- no runner is dispatched in this act, declared on the face.
### ### Two standing arms read act lists this act's ruling sets, declared on the face: G-PP-SCOPE (PLACE-papers' changed files against the
### two ledgers) and G-CURRENTS-UNEDITED (b676's currents, README, REGISTRY and the faces page among them, unwritten by this act).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b677_record.py).
### ### The harness is b568's to b676's (helpers, runner, seal), written by the Write tool from tools/b676_checks.py; the sources, predicates
### ### and arms over this act's banks are b677's.
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
import b677_worklist as K     # noqa: E402
import b676_worklist as K676  # noqa: E402
import b675_worklist as K675  # noqa: E402
import b674_worklist as K674  # noqa: E402
from b677_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b677_registration_2026-10-17.txt')
B676_FACE = os.path.join(D, 'b676_registration_2026-10-17.txt')
B676_ACT_ARMS = K676.ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = '2878d524'          # ### relay: b676's closing push-out bank, committed at step zero ((R287)(6))
TOOL_COMMIT = 'aefd8932'       # ### relay: the new tool committed alone (the ferry's Component 3)
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
PART = sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
INST = K676.SEALED + K675.SEALED + ('b675_li_bench.py',) + K674.SEALED + (
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
# ### b676's currents: this act writes no README, REGISTRY or faces-page byte
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
TABLE_FILES = K.TABLE_FILES
# ### the last merged run, b676's, read by the standing runner arms (no runner is dispatched in this act)
WD, WF, PT = K676.TD, '.github/workflows/build-module.yml', 'print_targets.txt'
W_PRE_MAIN, W_WORKFLOW, W_MAIN, W_CUT, W_TAG, W_RUNS = K676.T_PRE_MAIN, K676.T_WORKFLOW, K676.T_MAIN, K676.T_CUT, K676.T_NEXT_TAG, K676.T_RUNS
W_MERGE = '135be2e'
CANDIDATE = K676.CANDIDATE


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b677')
            and 'data/b677_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b677_record as REC
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
        if f.startswith('b677_') and f.endswith('.py'):
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b677_regspec as SPEC
    import b677_record as REC
    P = SPEC.planted()
    ctl = []
    for f in (lambda: REC.read_score_row('X9', 'HELD'),
              lambda: REC.read_map_row(dict(cell='Q0 AT qE0', bits=200, j=1, rads=[1.0] * 4, angle_rad=1.0, word='MAYBE', b671='PASS'))):
        try:
            f()
            ctl.append(False)
        except Exception:
            ctl.append(True)
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def wf_state():
    t = read_blob(WD, 'main:' + WF)
    pt = read_blob(WD, 'main:' + PT)
    return {CANDIDATE: dict(text=t, commit_files=files_of(WD, W_WORKFLOW), list_files=files_of(WD, W_MAIN),
                            on_main=subprocess.run(['git', '-C', WD, 'merge-base', '--is-ancestor', W_WORKFLOW, 'main']).returncode == 0,
                            targets=[l.strip() for l in pt.split(NL) if l.strip()],
                            lean_in_writes=[f for f in files_of(WD, W_WORKFLOW) + files_of(WD, W_MAIN) if f.endswith('.lean')])}


def merges_state():
    p = WD
    return {CANDIDATE: dict(main=gs(p, 'rev-parse', '--short=7', 'main'), parents=gs(p, 'log', '-1', '--format=%p', '--abbrev=7', 'main').split(),
                            built=W_CUT, tree_main=gs(p, 'rev-parse', 'main^{tree}'), tree_built=gs(p, 'rev-parse', W_CUT + '^{tree}'),
                            tags=dict((t, gs(p, 'rev-parse', '--short=7', t + '^{commit}')) for t in gs(p, 'tag', '--points-at', 'main').split()))}


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted(set(g2_of(B676_FACE)) - set(B676_ACT_ARMS))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


def _ct_first(repo, pre, prefix, path=None):
    args = ['log', '--reverse', '--format=%ct %s', pre + '..HEAD'] + (['--', path] if path else [])
    for l in gs(repo, *args).split(NL):
        if l.strip() and l.split(' ', 1)[1].startswith(prefix):
            return int(l.split(' ', 1)[0])
    return None


def sources(light=False):
    """the sources every arm reads; light (the act part, (R287)(7)) skips the three arms at HEAD, the act-root chain and the shared additive
    files, which only standing arms read."""
    import b677_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b677_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b677_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b677_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b677_ferry.txt'), scan=rd('b677_ferry_scan.txt'), stepz=rd('b677_stepzero.txt'),
        readfirst=rd('b677_readfirst.txt'), defects=rd('b677_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b677_author_answers.txt'), answersj=jl('b677_author_answers.json'), prerun=rd('b677_arms_prerun.txt'),
        rl=jl('b677_record_lines.json'), landing=jl('b677_landing.json'),
        tests=jl('b677_tests_stepzero.json'), testst=rd('b677_tests_stepzero.txt'), withheld=jl('b677_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b677_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), cmdj=jl('b677_commands.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b677_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        c1_ct=_ct_first(PP, PRE['pp'], 'b677 Component 1'),
        gate=rd('b677_reg_gate.txt'), rowgen=rd('b677_rowgen_stepzero.txt'),
        branchj=jl('b677_branches.json'), branchest=rd('b677_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '-a', '--list', *(list(bs) + ['*/' + b for b in bs]))) for repo, bs in K.DELETE),
        plan=rd('b677_map_plan.txt'), plan_ct=_ct_first(ROOT, PRE['relay'], 'b677 Component 2', 'data/b677_map_plan.txt'),
        mapj=jl('b677_map.json'), mapt=rd('b677_map.txt'), maprun=rd('b677_map_run.txt'), mapdiff=rd('b677_map_diff.txt'),
        tolj=jl('b677_tolerance.json'), tolt=rd('b677_tolerance.txt'), tolp1=jl('b677_tolerance_p1.json'),
        hj=jl('b677_map_h.json'), ht=rd('b677_map_h.txt'), diag=rd('b671_tie_diagnostic.txt'), orders=rd('b670_work_orders.txt'),
        tool_files=files_of(ROOT, TOOL_COMMIT), tool_head=cr0(blob(ROOT, 'HEAD:' + K.NEW_TOOL)),
        tool_now=cr0(raw(os.path.join(ROOT, *K.NEW_TOOL.split('/')))), tool_sha=hashlib.sha256(raw(os.path.join(ROOT, *K.NEW_TOOL.split('/'))) or b'').hexdigest(),
        rules=rd('b677_rules.txt'),
        repairs=rd('b677_tool_repairs.txt'), citation_src=read(os.path.join(T, 'b677_citation.py')),
        standing=STANDING, wf=wf_state(), runner=jl('b676_runner_rows.json'), rbank=rd('b676_runner_SIDE-trivium_after.txt'),
        ax_after=rd('b676_axioms_SIDE-trivium_after.txt'), merges=merges_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b677_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b677_act_root.json'), arj0=jl('b676_act_root.json'), art=rd('b677_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b677_kernels_face.json').get('kernels') or {}), kerns_read=REC._kerns(),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b677_mustnotexist.txt')),
        fj=jl('b677_findings.json'), tj=jl('b677_trail.json'), sc=jl('b677_scores.json'), desk=rd('b677_desk_notes.txt'), tfj=jl('b677_table_final.json'),
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
    S['live'] = dict(names=[], nsm=[], ac=[], ac_counts={}, mh=[], mh_per={}, secs=(0, 0, 0)) if light else live_arms()
    S['phase_secs']['the three arms at HEAD' + (' (not run in the act part)' if light else '')] = time.time() - t1
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
        if f.startswith(('b677_', 'audit_b677_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith('.gz'):
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
    S['order_slack'] = AR.ORDER_SLACK
    if light:
        S['ar_verify'], S['ar_reads'] = [], {}
    else:
        try:
            S['ar_verify'] = AR.verify(remote=KC0.remote_refs)
            S['ar_reads'] = dict(AR.READS_AT)
        except Exception as e:
            S['ar_verify'], S['ar_reads'] = [('raised', type(e).__name__, [])], {}
    S['phase_secs']['the act-root chain' + (' (not run in the act part)' if light else '')] = time.time() - t1
    t1 = time.time()
    if light:
        S['additive'] = []
    else:
        try:
            S['additive'] = ADD.check(worktree=True)
        except Exception as e:
            S['additive'] = [('raised', type(e).__name__, [('x', [])])]
    S['phase_secs']['the shared additive files' + (' (not run in the act part)' if light else '')] = time.time() - t1
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
    """the step-zero bank's process listings, in this act's words (data/b677_stepzero.txt): at the start and after the tests, none of tail,
    lean, lake, python or bash running."""
    p = unwrap(S['stepz'])
    return '(names tail, lean, lake, python, bash): none of each' in p and 'after the tests: none of each' in p


STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 2' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"
PROMPT_HEADS = ('(The run)', '(H3 source)')


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b677 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) >= 1 and all(x >= 2 for x in per) and len(res) == len(calls) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and all(x in a for x in PROMPT_HEADS)


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def no_local_lean(S):
    import b677_record as REC
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


# ================================================================== (R287) STEP ZERO: THE CITATION CHECKS, THE BRANCHES, ROWGEN
READFIRST_NEEDLES = ('data/b676_closing.txt', 'data/b676_defects.txt', 'data/b676_q0_lines.txt', 'data/b676_strip_uses.txt',
                     'data/b670_work_orders.txt', 'data/b667_epstein_plan.txt', 'data/b671_narrow_plan.txt', 'data/b667_h4_reading.txt',
                     'tools/b667_epstein_map_balls.py', 'data/b671_tie_diagnostic.txt', 'data/b671_epstein_zeros_narrowed.json.gz',
                     'data/b675_li_plan.txt', 'data/b675_li_bench.txt', 'data/b675_li_controls.txt', 'data/b675_rules.txt',
                     'data/b676_closing_push_out.txt')


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """the branches (R287)(6) names: none left in its repository, local or remote-tracking; the branches bank lists them, each with its tip."""
    z = S['branchest']
    named = [b for _r, bs in K.DELETE for b in bs]
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 3 and all(b in z for b in named) \
        and 'BRANCHES 9 (LOCAL 8, REMOTE 1) ; MERGED 9 ; TO BE DELETED 9' in z


def branches_banked_ok(S):
    import b677_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 9 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sum(1 for r in rows if r['where'] == 'local') == 8 and [r['branch'] for r in rows if r['where'] == 'remote'] == ['recut-trivium-b676']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    """b675's rules row 1: the closing run dry as a gate step before the lock, its readings printed in the gate's record -- the head line,
    the citation line from the banks, the run's, the tolerance's and the hypotheses' verdict lines, the tag rows with their kind."""
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b677 closed:' in g and 'the misses as the bank lists them' in g and '(annotated, peeled) ; main' in g \
        and '### THE RUN ((R287)(4)' in g and '### THE TOLERANCE' in g and '### THE HYPOTHESES' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the step-zero check: run before the ferry was banked; its four misses raised and entered as the navigator's (b) and (d); Component 1
    committed after the check."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    entered = '    (b) THE NAVIGATOR' in S['defects'] and '    (d) THE NAVIGATOR' in S['defects']
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'RUN BEFORE THE FERRY IS BANKED' in c \
        and int(m.group(3)) == 4 == len(S['cit_misses']) and entered and S['c1_ct'] is not None and S['cit_at'] and S['cit_at'] < S['c1_ct']


MID_NEEDLES = ('on the run, under (R287)(3)', 'on the H3 source')


def midact_ok(S):
    """(R278)(4): every mid-act answer's check appended, one answer per check; a miss it printed named in the defects bank as the
    navigator's ((c): data/b663_plan.txt)."""
    blocks = re.split(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', S['citation'], flags=re.M)[1:]
    last = {}
    for b in blocks:
        for n in MID_NEEDLES:
            if repr(n) in b.split(NL)[0]:
                m = re.search(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)(?: -- RAISED: (.*?))?\.\*\*', b)
                last[n] = m.groups() if m else None
    if not all(last.get(n) and int(last[n][0]) > 0 for n in MID_NEEDLES):
        return False
    raised = [p.strip() for n in MID_NEEDLES if last[n][2] != '0' for p in (last[n][3] or '').split(',') if p.strip()]
    return all(p in S['defects'] for p in raised) and '    (c) THE NAVIGATOR' in S['defects']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


# ================================================================== (R287)(3)-(5): THE PLAN, THE RUN, THE TOLERANCE, THE HYPOTHESES, THE LANDING
H3_QUOTE = 'at Q0 every hypothesis of zeroSide_neg_at_rate_cfg certifies by name and hrate holds at some j₀ ≤ D + 40'
H4_QUOTE = 'prints j₀ = 38 and a zero side below zero, each with its ball'


def plan_ok(S):
    """N2: the plan committed (Component 2) before any run bank and before the prompt's call; H3 and H4 quoted by line in it."""
    p = ' '.join(S['plan'].split())
    calls = S['answersj'].get('calls') or []
    call_at = iso_epoch((calls[0].get('ts') or '')[:19] + 'Z') if calls else None
    p1_at = iso_epoch(S['tolp1'].get('at') or '')
    map_at = iso_epoch(S['mapj'].get('at') or '')
    return H3_QUOTE in p and H4_QUOTE in p and 'data/b663_epstein_plan.txt :131' in p and 'data/b667_epstein_plan.txt section 8 :124-:125' in p \
        and bool(S['plan_ct'] and call_at and p1_at and map_at) and S['plan_ct'] <= call_at < p1_at and S['plan_ct'] < map_at


def _diag_keys(S):
    out = set()
    for l in S['diag'].split(NL):
        m = re.match(r'^  (THE CONTROL Z₁\(0\.8, 29\.6\)|Q0 AT qE0)\s+(\d+) j (\d+) : ', l)
        if m:
            out.add((m.group(1), int(m.group(2)), int(m.group(3))))
    return out


def map_rows_ok(S):
    """N4: every row of the map bank through the record tool's reader, the set of (cell, precision, j) b671's list whole, none dropped."""
    import b677_record as REC
    rows = S['mapj'].get('rows') or []
    try:
        got = [REC.read_map_row(r) for r in rows]
    except Exception:
        return False
    keys = set((c, b_, j) for c, b_, j, _w in got)
    dk = _diag_keys(S)
    return len(got) == 123 == len(keys) and keys == dk and 'NONE DROPPED True.**' in S['mapt']


def angle_form_ok(S):
    """N3: the new tool's text holds no repeated-squaring loop; every power of the run taken as exp(n·log z) (no square of a ball holding 0);
    the b667 map's sha256 the same before and after the run and equal to b671's; the map bank naming the committed tool's sha256."""
    t = S['mapj'].get('tally') or {}
    m = re.search(r'the b667 map sha256 (\w+) before and (\w+) after \(EQUAL\)', S['mapt'])
    tm = re.search(r'tools/b677_epstein_map_angle\.py sha256 (\w+)', S['mapt'])
    return "left: NONE" in S['mapdiff'] and t.get('square_by_product') == 0 and (t.get('angle') or 0) > 0 and bool(m) \
        and m.group(1) == m.group(2) == K.MAP_SHA and bool(tm) and tm.group(1) == S['tool_sha']


def control_ok(S):
    c = S['mapj'].get('control') or {}
    return c.get('reproduced') is True and c.get('j0') == 31 and (c.get('zero_side') or {}).get('held') is True


def tolerance_ok(S):
    """H5's plants as the tolerance bank's verdict prints them, and the figures in its JSON: P1 over 19 widths, h_tol(64) and h_tol(38)
    read, P2's shift firing and its quarter-radius shift as unplanted, P3 as planted."""
    v = re.search(r'P1 WIDTHS (\d+) ; h_tol\(38\) (\S+) ; h_tol\(64\) (\S+) ; P2 SHIFT 1e-12 FIRES (\w+) ; P2 QUARTER-RADIUS SHIFT AS UNPLANTED (\w+) ; '
                  r'P3 ([A-Z ]+) ;', S['tolt'])
    j = S['tolj']
    return bool(v) and int(v.group(1)) == len(S['tolp1'].get('widths') or {}) == 19 and v.group(4) == 'True' and v.group(5) == 'True' \
        and v.group(6) == 'AS PLANTED' and j.get('h_tol64') and j.get('h_tol38') and abs(float(v.group(3)) - j['h_tol64']) < 1e-30 \
        and j['h_tol64'] < 1e-24 < j['h_tol38']


def hyp_ok(S):
    """the hypotheses bank against the banks it reads, recomputed here: H1 by b671's INSTRUMENT rows still failing, H2 by the radius at
    j = 64 and h_tol(64), H4 by the map's reading; the verdict line the bank prints."""
    rows = S['mapj'].get('rows') or []
    still = [r for r in rows if r['b671'] == 'INSTRUMENT' and r['word'] != 'PASS']
    h1 = not still and bool([r for r in rows if r['b671'] == 'INSTRUMENT'])
    q64 = [r for r in rows if r['cell'] == 'Q0 AT qE0' and r['j'] == 64]
    h2 = bool(q64) and all(r['rad'] < 2.0 ** -20 for r in q64) and (S['tolj'].get('h_tol64') or 0) >= 1e-24
    h4 = 'SCORABLE' if (S['mapj'].get('q0') or {}).get('zero_side') else 'NOT SCORABLE'
    j = S['hj']
    return j.get('H1') is h1 and j.get('H2') is h2 and j.get('H4') == h4 and j.get('H5') is True \
        and ('### ### **H1 %s ; H2 %s ;' % ('HELD' if h1 else 'REFUTED', 'HELD' if h2 else 'REFUTED')) in S['ht']


def orders_ok(S):
    """(R287)(5): the two orders landed on OPEN_TRAILS at the landing bank's lines, found by conv, each with its Status and trigger; each
    order's row in the orders bank through the record tool's reader, OPEN, at that line."""
    import b677_record as REC
    a = landed(S, 0, ['W-ORD-MAP-ANGLE-FORM', 'Status OPEN', '**Trigger:** after `W-ORD-EPSTEIN-BALL-WIDTH`'], key='landing')
    b = landed(S, 1, ['W-ORD-EPSTEIN-BALL-WIDTH', 'Status OPEN', '3.2·10⁻²⁸', '**Trigger:** a narrowing act'], key='landing')
    la, lb = rline(S, 0, 'landing').get('line'), rline(S, 1, 'landing').get('line')
    got = {}
    for l in S['orders'].split(NL):
        try:
            o, st, tr = REC.read_order_row(l)
        except Exception:
            continue
        m = re.search(r':(\d+)\s+%s' % re.escape(tr), l)
        got[o] = (st, int(m.group(1)) if m else None, tr)
    return a and b and got.get('W-ORD-MAP-ANGLE-FORM') == ('OPEN', la, 'after W-ORD-EPSTEIN-BALL-WIDTH') \
        and got.get('W-ORD-EPSTEIN-BALL-WIDTH', (None, None, ''))[:2] == ('OPEN', lb)


def tool_alone_ok(S):
    return S['tool_files'] == [K.NEW_TOOL] and S['tool_head'] is not None and S['tool_head'] == S['tool_now']


def repairs_ok(S):
    return '### ### **REPAIRS 0 ; THE SEALED COPIES AGREE ; TOOLS CARRIED 8.**' in S['repairs'] and "rfind('BEGIN', 0, k)" in S['citation_src'] \
        and "the (?:navigator`s )?answer carrying" in S['closing_src']


def rules_ok(S):
    """(R287)(7): the split entered as a rule row, and the pre-run bank printing both parts with their seconds."""
    return '(1) THE SUITE IN TWO FOREGROUND PARTS' in S['rules'] and re.search(r'PART standing : ARMS \d+ ; \d+ s', S['prerun']) is not None \
        and re.search(r'PART act : ARMS \d+ ; \d+ s', S['prerun']) is not None


# ================================================================== THE RUNNER (the standing arms, the last merged run: b676's, SIDE-trivium)
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
    import b677_record as REC
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


POST_SEAL = ('b677 seal', 'b677 pre-root', 'b677 root', 'b677 record', 'b677 --', 'b677 closing')


def _component_commit(s):
    return s.startswith('b677') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 54 and rows[53][:3] == ['b677', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b678_' in it] \
        and any(it.startswith('data/b677_map.txt ') for it in items) and any(it.startswith('data/b677_tolerance.txt ') for it in items) \
        and all(any(it.startswith(p + ' ') for it in items) for p in K.SHARED_APPENDED) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b677_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b677') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 678)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The plan**', '**The run**', '**The tolerance**', '**The hypotheses**', '**The landing**',
                 '**The tools**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**',
                 'b678')


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
    import b677_record as REC
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
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE PLAN' in t \
        and '### THE RUN' in t and '### THE TOLERANCE' in t and '### THE HYPOTHESES' in t and '### THE CARRY-TIME READING' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R287) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: at the start and after the tests, none of tail, lean, lake, python or bash running',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('none of each', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b676_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s, PLACE-papers` and SIDE-trivium`s branch lists, local and remote-tracking, and the branches bank (the ruling`s list alone)',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b676'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its prompts with their options and results', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS', 'THE ANSWERS'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b677_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: landed(S, 0, ['b676 AT ITS WEIGHT', 'Nothing deposited.', 'nine defects']),
     lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, verdict lines and tag rows printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step): run before the ferry was banked, its four misses raised and entered as the navigator`s (b) and (d)',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('RUN BEFORE THE FERRY IS BANKED', 'RUN'))),
    ('G-MIDACT-CHECKED', 'the citation check`s bank ((R278)(4)): each of the two answers checked alone, its miss named in the defects bank',
     lambda S: midact_ok(S), lambda S: put(S, 'citation', S['citation'].replace("'on the H3 source'", "'x'"))),
    ('G-R287-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R287) END' in S['ferry'] and S['ot'].count('**(R287) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R287) ratified', '**(R2870) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: nine rows through the record tool`s reader, each merged and deleted, eight local and SIDE-trivium`s recut branch at its remote',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-PLAN-BEFORE-RUN', 'the plan bank and its commit, the answers bank`s call, the run banks` times: H3 and H4 quoted by line, the plan before the prompt and the prompt before any run (N2)',
     lambda S: plan_ok(S), lambda S: put(S, 'plan', S['plan'].replace('data/b663_epstein_plan.txt :131', 'data/b663_epstein_plan.txt'))),
    ('G-MAP-ROWS-READ', 'the map bank`s rows through the record tool`s reader against b671`s diagnostic: 123 rows, its list whole (N4)',
     lambda S: map_rows_ok(S), lambda S: _mut(S, 'mapj', lambda d: d['rows'].pop())),
    ('G-ANGLE-FORM', 'the map`s diff bank, the run`s power tally and the map bank`s two sha256 lines: no repeated squaring, the b667 map unedited, the committed tool the one run (N3)',
     lambda S: angle_form_ok(S), lambda S: _mut(S, 'mapj', lambda d: d['tally'].update(square_by_product=1))),
    ('G-CONTROL-REPRODUCED', 'the map bank`s control: Z₁ reproduced in the angle form, j₀ = 31 and the zero side below 0',
     lambda S: control_ok(S), lambda S: _mut(S, 'mapj', lambda d: d['control'].update(j0=32))),
    ('G-TOLERANCE-MEASURED', 'the tolerance bank`s verdict and its JSON: 19 planted widths, h_tol(64) below the banked width and h_tol(38) above it, the shift control firing, P3 as planted (H5)',
     lambda S: tolerance_ok(S), lambda S: put(S, 'tolt', S['tolt'].replace('P3 AS PLANTED', 'P3 NOT AS PLANTED'))),
    ('G-HYPOTHESES-READ', 'the hypotheses bank against the map and tolerance banks, H1, H2 and H4 recomputed here',
     lambda S: hyp_ok(S), lambda S: _mut(S, 'hj', lambda d: d.update(H1=True))),
    ('G-ORDERS-LANDED', 'OPEN_TRAILS at the landing bank`s lines, found by conv, and the orders bank`s rows through the record tool`s reader: both orders OPEN with their triggers',
     lambda S: orders_ok(S), lambda S: put(S, 'orders', S['orders'].replace('after W-ORD-EPSTEIN-BALL-WIDTH [', 'after the width ['))),
    ('G-NEW-TOOL-ALONE', 'the new tool`s commit (aefd8932): its one file the tool, the working tree equal to HEAD',
     lambda S: tool_alone_ok(S), lambda S: put(S, 'tool_files', S['tool_files'] + ['data/b677_map.txt'])),
    ('G-TOOL-REPAIRS', 'the carry-time bank`s verdict and the carried tools` code: no repair, the sealed copies agreeing, the mid-act cut and the closing`s needle carried',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS 0 ;', 'REPAIRS 1 ;'))),
    ('G-RULES-ROW', 'the rules bank`s row of (R287)(7) and the pre-run bank`s two parts with their seconds',
     lambda S: rules_ok(S), lambda S: put(S, 'rules', S['rules'].replace('(1) THE SUITE IN TWO FOREGROUND PARTS', '(1) THE SUITE'))),
    ('G-SPEC-PLANTED', 'tools/b677_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('map row' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b677 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b677_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b677_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-trivium`s main, the last merged run`s kernel: the workflow file committed alone (dd587f9), the print list committed alone (7074154, 22 names), no .lean byte in either, no author identifier, no secret, the hold, the cache, the print step over print_targets.txt',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[CANDIDATE].update(text=d[CANDIDATE]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'the last merged run`s row (b676`s SIDE-trivium after) through the record tool`s reader: the run id and ref, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'the last merged run`s gate reading: build exit 0, no error line, every terminal of its axioms bank printed, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbank', S['rbank'].replace('GATE DERIVES', 'GATE NOT DERIVES'))),
    ('G-MERGES-ON-GATE', 'SIDE-trivium`s main: the merge commit of the built tip on the print-list main, the merged tree the built tree, its tag v0.1.1 peeled to it',
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
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, SIMPLICITY, README, REGISTRY and the faces page: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal, SIDE-trivium among them',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b676`s and the earlier tools, the generator, b667`s certify and map, b671`s narrowing, rowgen`s, the mirror`s, the instruments and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at e41e165f but the shared additive files (the orders bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b676_stepzero.txt'])),
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
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b677 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b677_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in two parts summed (R287)(7)',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b676`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b676 — lane two, act one hundred and three, the re-cut act' in S['ot']
     and S['rootsf'].count(NL + 'b676 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b676 — lane two', '### b676 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 54th line, the root bank and its items, the map, tolerance and orders banks among them', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b678 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b677 AGREE, b677 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b677 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b677_record.py agree', 'b677_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b678', lambda S: '**Next:** b678' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b678', '**Next:** b679'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since e41e165f and 9abb234 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b677')" in S['suite'] and "'data/b677_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b677_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the plan, the run, the tolerance, the hypotheses, the carry-time reading',
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
    p = os.path.join(D, 'b677_seal_hashes.json')
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
    print('  written: b677_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b677_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b677_checks_postpush.txt' if pushed else 'b677_checks.txt'


def _part_name(base, part):
    return base.replace('.txt', '_%s.txt' % part)


def _write(name, lines):
    out = os.path.join(D, name)
    b = (NL.join(lines) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    return out


PART_FOOT = re.compile(r'### PART (\w+) : ARMS (\d+) ; LIVE PASSING (\d+) ; LIVE FAILING (\d+) (\[[^\]]*\]|NONE) ; NEGATIVE-CONTROL FAILURES (\d+) ; '
                       r'POSITIVE-CONTROL PASSES (\d+) (\[[^\]]*\]|NONE) ; DECLARED EQ RUN (\w+) ; (\d+) s')


def combine():
    """(R287)(7): the run's bank from its two part banks, the counts summed and both parts' seconds printed at its head; the parts' banks
    carried whole beneath."""
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
    fails = sum((json.loads(m.group(5).replace("'", '"')) if m.group(5) != 'NONE' else [] for _p, m, _t in parts), [])
    defs = sum((json.loads(m.group(8).replace("'", '"')) if m.group(8) != 'NONE' else [] for _p, m, _t in parts), [])
    deq = all(m.group(9) == 'True' for _p, m, _t in parts)
    ok = lf == 0 and pc == 0 and ng == 0 and deq
    out = ['=' * 104, heads[0].replace('PART standing', 'TWO PARTS SUMMED ((R287)(7))'), '=' * 104] + [
        '  ### PART %s : ARMS %s ; %s s' % (p, m.group(2), m.group(10)) for p, m, _t in parts] + [
        '  ### the parts` seconds summed %d ; the longer part %s s, under the 600 s limit %s' % (
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
        ex.update(jl('b677_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b677_checks.txt', 'b677_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b677_exercise.json')
        open(p_ + '.tmp', 'wb').write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:10]))
    print('  written: %s' % base)
    return 0 if ok else 1


def main():
    if SEAL:
        return seal()
    if COMBINE:
        return combine()
    if PART not in K.PARTS:
        print('### (R287)(7): every run in two foreground parts -- give `--part standing` or `--part act`')
        return 2
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b677 -- THE SUITE. ### **%s READING.** ### PART %s ((R287)(7)) ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH', PART))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    light = PART == 'act'
    S = sources(light=light)
    S['pushed'] = pushed
    t1 = time.time()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID or not light) else regenerate()
    S['phase_secs']['the table regenerated' + ('' if light and not (RERUN or PRERUN or MID) else ' (not in this part or run)')] = time.time() - t1
    rec('  ### THE PHASES, IN SECONDS: %s' % '; '.join('%s %.0f' % kv for kv in S['phase_secs'].items()))
    rec('  ### THE LONGEST PHASE %.0f s ; above 450 s: %s (b675 rules row 2: such a run is split at the next act)' % (
        max(S['phase_secs'].values()), max(S['phase_secs'].values()) > 450))
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    arms = [a for a in ARMS if (a[0] in K.ACT_ARMS) == light]
    rec('  arms in the (G2) block : %d ; in the suite : %d ; run in this part : %d' % (len(declared), len(names), len(arms)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b676`s face less its own arms) %d ; carried here %d ; the act`s arms over its own banks %s ; '
        'arms beyond both %s' % (len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
                                sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if not light:
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
    rec('  ### THE MAP: rows %d ; the hypotheses %s ; the tolerance h_tol(64) %s, h_tol(38) %s' % (
        len(S['mapj'].get('rows') or []), dict((k, S['hj'].get(k)) for k in ('H1', 'H2', 'H3', 'H4', 'H5')), S['tolj'].get('h_tol64'), S['tolj'].get('h_tol38')))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    if not light:
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
    rec('  ### tracked files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                          if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this run, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if light and not (RERUN or PRERUN or MID):
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
    lp = os.path.join(D, _part_name(base, PART).replace('b677_arms_prerun', 'b677_lsr_prerun').replace('b677_checks', 'b677_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b677_exercise_%s.json' % PART)
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
