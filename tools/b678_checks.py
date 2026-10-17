# -*- coding: utf-8 -*-
"""b678_checks.py -- THE SUITE OF b678, UNDER (R288): b677 AT ITS WEIGHT; THE Q0 LINES ANSWERED BY ONE GENERATED CORRIGENDUM ENTRY; THE
LICENSED TABLE'S NEXT DOCUMENT CUT (SIDE-silence-principle's docstrings, v0.2.1).

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R288)(1), THE REPAIR AT CARRY: every run in THREE foreground parts -- `--part standing-a` (the standing arms but two, over the three
### arms at HEAD, the written files, the public bytes and the prior banks), `--part standing-b` (the two standing arms over the act-root chain
### and the shared additive files) and `--part act` (the act's arms over this act's banks, the table regenerated in a closing run) -- each
### computing only the sources its arms read, each under the 600 s limit; `--combine <bank>` writes the run's bank, the counts summed and
### every part's seconds printed at its head (data/b678_rules.txt row 1).
### ### (R264)(2), THE FREEZE: the standing arms are b677's face's (G2) arms less b677's own arms over b677's banks, carried, their act needles
### read in b678's banks; the act's own arms read this act's banks alone (tools/b678_worklist.py ACT_ARMS). The standing runner arms read this
### act's merged run: SIDE-silence-principle's run 39055212218 at 8829bcc, merged at 96b3098, v0.2.1, the workflow in the Mathlib-free form
### with its print list on main.
### ### Two standing arms read act lists this act's ruling sets, declared on the face: G-PP-SCOPE (PLACE-papers' changed files against the
### two ledgers) and G-CURRENTS-UNEDITED (b677's currents, README, REGISTRY and the faces page among them, unwritten by this act).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b678_record.py).
### ### The harness is b568's to b677's, written by the Write tool from tools/b677_checks.py; the sources, predicates and arms over this act's
### ### banks are b678's.
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
import b678_worklist as K     # noqa: E402
import b677_worklist as K677  # noqa: E402
import b676_worklist as K676  # noqa: E402
import b675_worklist as K675  # noqa: E402
import b674_worklist as K674  # noqa: E402
from b678_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b678_registration_2026-10-17.txt')
B677_FACE = os.path.join(D, 'b677_registration_2026-10-17.txt')
B677_ACT_ARMS = K677.ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = '452c69ff'          # ### relay: b677's closing push-out bank, committed at step zero ((R288)(4))
CORR_TOOL_COMMIT = '5d3416b8'  # ### relay: the corrigendum tool committed alone ((R288)(2))
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
PART = sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
INST = K677.SEALED + ('b677_epstein_map_angle.py',) + K676.SEALED + K675.SEALED + ('b675_li_bench.py',) + K674.SEALED + (
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
# ### b677's currents: this act writes no README, REGISTRY or faces-page byte
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
TABLE_FILES = K.TABLE_FILES
# ### this act's merged run, read by the standing runner arms
WD, WF, PT = K.TD, '.github/workflows/build-module.yml', 'print_targets.txt'
W_PRE_MAIN, W_WORKFLOW, W_MAIN, W_CUT, W_TAG, W_RUNS, W_MERGE = K.T_PRE_MAIN, K.T_WORKFLOW, K.T_MAIN, K.T_CUT, K.T_NEXT_TAG, K.T_RUNS, K.T_MERGE
CANDIDATE = K.CANDIDATE
# ### (R288)(1): the parts and the sources each part computes
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b678')
            and 'data/b678_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b678_record as REC
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
        if f.startswith('b678_') and f.endswith('.py'):
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b678_regspec as SPEC
    import b678_record as REC
    P = SPEC.planted()
    ctl = []
    for f in (lambda: REC.read_score_row('X9', 'HELD'),
              lambda: REC.read_corr_row(dict(file='FINDINGS.md', line=1, quote='x', s='y', reading='x (FINDINGS :1)'))):
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
    return {CANDIDATE: dict(text=t, commit_files=files_of(WD, W_WORKFLOW), list_files=files_of(WD, W_MAIN), mathlib='mathlib' in lf.lower(),
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


STANDING = sorted(set(g2_of(B677_FACE)) - set(B677_ACT_ARMS))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


def _ct_first(repo, pre, prefix, path=None):
    args = ['log', '--reverse', '--format=%ct %s', pre + '..HEAD'] + (['--', path] if path else [])
    for l in gs(repo, *args).split(NL):
        if l.strip() and l.split(' ', 1)[1].startswith(prefix):
            return int(l.split(' ', 1)[0])
    return None


def sources(need=()):
    """the sources the arms read; `need` (by part, (R288)(1)) names the heavy phases this part computes: 'live' (the three arms at HEAD),
    'written' (the written files, the public bytes, the prior banks), 'chain' (the act-root chain), 'additive' (the shared additive files)."""
    import b678_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b678_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b678_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b678_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b678_ferry.txt'), scan=rd('b678_ferry_scan.txt'), stepz=rd('b678_stepzero.txt'),
        readfirst=rd('b678_readfirst.txt'), defects=rd('b678_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b678_author_answers.txt'), prerun=rd('b678_arms_prerun.txt'), rl=jl('b678_record_lines.json'),
        rl2=jl('b678_record_lines_c2.json'), rl3=jl('b678_record_lines_c3.json'),
        tests=jl('b678_tests_stepzero.json'), testst=rd('b678_tests_stepzero.txt'), withheld=jl('b678_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b678_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), cmdj=jl('b678_commands.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b678_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        c1_ct=_ct_first(PP, PRE['pp'], 'b678 Component 1'),
        gate=rd('b678_reg_gate.txt'), rowgen=rd('b678_rowgen_stepzero.txt'), rowgen_after=rd('b678_rowgen_after.txt'),
        branchj=jl('b678_branches.json'), branchest=rd('b678_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '-a', '--list', *(list(bs) + ['*/' + b for b in bs]))) for repo, bs in K.DELETE),
        corrj=jl('b678_corrigendum.json'), corrt=rd('b678_corrigendum.txt'), q0j=jl('b676_q0_lines.json'), orders=rd('b670_work_orders.txt'),
        corr_tool_files=files_of(ROOT, CORR_TOOL_COMMIT), corr_tool_head=cr0(blob(ROOT, 'HEAD:tools/b678_corrigendum.py')),
        corr_tool_now=cr0(raw(os.path.join(T, 'b678_corrigendum.py'))),
        pre_ledgers=dict((f, (cr0(blob(PP, '%s:%s' % (PRE['pp'], f))) or b'').decode('utf-8', 'replace').split(NL)) for f in ('FINDINGS.md', 'OPEN_TRAILS.md')),
        naming=rd('b678_naming.txt'), namingj=jl('b678_naming.json'), wf_ct=int(gs(WD, 'log', '-1', '--format=%ct', W_WORKFLOW) or 0),
        cut=rd('b678_cut.txt'), cutdiff=rd('b678_cut_diff.txt'), cut_names=gs(WD, 'diff', '--name-only', W_MAIN, W_CUT).split(NL),
        prints=rd('b678_prints_compare.txt'), corr=rd('b678_correspondence_dry.txt'),
        rules=rd('b678_rules.txt'),
        repairs=rd('b678_tool_repairs.txt'), citation_src=read(os.path.join(T, 'b678_citation.py')),
        standing=STANDING, wf=wf_state(), runner=jl('b678_runner_rows.json'), rbank=rd('b678_runner_%s_after.txt' % CANDIDATE),
        ax_after=rd('b678_axioms_%s_after.txt' % CANDIDATE), merges=merges_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b678_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b678_act_root.json'), arj0=jl('b677_act_root.json'), art=rd('b678_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b678_kernels_face.json').get('kernels') or {}), kerns_read=REC._kerns(),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b678_mustnotexist.txt')),
        fj=jl('b678_findings.json'), tj=jl('b678_trail.json'), sc=jl('b678_scores.json'), desk=rd('b678_desk_notes.txt'), tfj=jl('b678_table_final.json'),
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
            if f.startswith(('b678_', 'audit_b678_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith('.gz'):
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
    """the step-zero bank's process listings, in this act's words (data/b678_stepzero.txt)."""
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


def answers_ok(S):
    """the answers bank as it prints: this act put no prompt, so the bank's head counts 0 and it prints NONE; were prompts put, each with
    its options and its result (the b677 form)."""
    a = S['answers']
    m = re.search(r'^### b678 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    if not m or int(m.group(1)) != len(heads):
        return False
    if not heads:
        return '### NONE: no prompt has been put to the author in this act.' in a and not calls
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    return all(x >= 2 for x in per) and len(res) == len(calls) and not any(UNANSWERED in r or '### NO RESULT' in r for r in res)


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def no_local_lean(S):
    import b678_record as REC
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


# ================================================================== (R288) STEP ZERO: THE CITATION CHECK, THE BRANCHES, ROWGEN
READFIRST_NEEDLES = ('data/b677_closing.txt', 'data/b677_defects.txt', 'data/b677_map_h.txt', 'data/b677_tolerance.txt', 'data/b670_work_orders.txt',
                     'data/b676_q0_lines.txt', 'FINDINGS :8881', 'Zeta23/Defs.lean :142', 'data/b670_licensed_table.txt', 'data/b647_table_kernels.txt',
                     'data/b674_rules.txt', 'data/b676_cut.txt', 'data/b674_cut.txt', 'tools/correspondence_gen.py', 'data/b675_rules.txt',
                     'data/b677_rules.txt', 'data/b677_closing_push_out.txt')


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """the branches (R288)(4) names: none left in its repository, local or remote-tracking; the branches bank lists them, each with its tip."""
    z = S['branchest']
    named = [b for _r, bs in K.DELETE for b in bs]
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and all(b in z for b in named) \
        and 'BRANCHES 5 (LOCAL 5, REMOTE 0) ; MERGED 5 ; TO BE DELETED 5' in z


def branches_banked_ok(S):
    import b678_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 5 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) and all(r['where'] == 'local' for r in rows)


def deletes_one_ok(S):
    """N4: every branch delete command names one branch and carries no glob in any half, read from the command bank's shapes and again from
    the capture by the record tool's own reader; the branches deleted the ruling's list exactly."""
    import b678_record as REC
    shapes = [REC.delete_shape(r['cmd']) for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and re.search(r'\bbranch\s+-[dD]\b', r['cmd'])]
    named = sorted(b for _r, bs in K.DELETE for b in bs)
    return bool(shapes) and all(len(d) == 1 and not gl for d, gl in shapes) and sorted(x for d, _g in shapes for x in d) == named \
        and 'BRANCH DELETES OF ONE BRANCH AND NO GLOB 5 OF 5' in rd('b678_commands.txt')


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b678 closed:' in g and 'the misses as the bank lists them' in g and '(annotated, peeled) ; main' in g \
        and '### THE CORRIGENDUM' in g and '### THE RE-CUT' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the step-zero check: run before the ferry was banked, no miss (one of the seat's own predicates read unwrapped before banking, the
    step-zero bank saying so); Component 1 committed after the check."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'RUN BEFORE THE FERRY IS BANKED' in c \
        and int(m.group(3)) == 0 == len(S['cit_misses']) and 'read across a hard wrap' in S['stepz'] and S['c1_ct'] is not None \
        and S['cit_at'] and S['cit_at'] < S['c1_ct']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


def rowgen_after_ok(S):
    """(R288)(2): the rowgen diff after the corrigendum, nothing moved -- its totals the step-zero run's."""
    tot = lambda t: re.findall(r'TOTALS\s+checked (\d+) \| present (\d+) \| STALE (\d+)', t)   # noqa: E731
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen_after'] and bool(tot(S['rowgen'])) \
        and tot(S['rowgen_after']) == tot(S['rowgen']) and 'AFTER THE CORRIGENDUM' in S['rowgen_after']


# ================================================================== (R288)(2): THE CORRIGENDUM
def corr_generated_ok(S):
    """N2's count: the corrigendum bank's written rows through the record tool's reader, their number the bank's TO RE-CUT rows less the
    carried, equal to the hand count 36; the entry at FINDINGS by its title through conv, every row's file and line printed in it."""
    import b678_record as REC
    j = S['corrj']
    try:
        got = [REC.read_corr_row(r) for r in j.get('rows') or []]
    except Exception:
        return False
    recut = len([h for h in S['q0j'].get('hits') or [] if h.get('reading') == 'TO RE-CUT'])
    e = j.get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    body = NL.join(ls[e - 1:end]) if e else ''
    return bool(got) and len(got) == recut - len(j.get('carried') or []) and recut == j.get('hand_count') == 36 and e \
        and fline(S, e) == conv(j.get('title') or '\x00') and all(('- %s :%d -- ' % (f.replace('.md', ''), n)) in body for f, n in got) \
        and 'HAND COUNT 36 ; WRITTEN %d ; CARRIED %d' % (len(got), len(j.get('carried') or [])) in S['corrt']


def ledger_unmoved_ok(S):
    """N2: no ledger line among the 35 rewritten or pinned in place -- each line's text at PLACE-papers before the act and now, equal."""
    j = S['corrj']
    keys = sorted(set((r['file'], r['line']) for r in (j.get('rows') or []) + (j.get('carried') or [])))
    now = dict((f, (S['find'] if f == 'FINDINGS.md' else S['ot']).split(NL)) for f in ('FINDINGS.md', 'OPEN_TRAILS.md'))
    return len(keys) == 35 and all(n <= len(S['pre_ledgers'][f]) and S['pre_ledgers'][f][n - 1] == now[f][n - 1] for f, n in keys)


def corr_tool_alone_ok(S):
    return S['corr_tool_files'] == ['tools/b678_corrigendum.py'] and S['corr_tool_head'] is not None and S['corr_tool_head'] == S['corr_tool_now']


def order_discharged_ok(S):
    """the order's record line at OPEN_TRAILS by the landing bank, found by conv, carrying the entry's line, its Status and pin; its row in the
    orders bank through the record tool's reader: DISCHARGED at that line, the pin the entry's line."""
    import b678_record as REC
    e = S['corrj'].get('entry_line')
    x = rline(S, 0, 'rl2')
    ok1 = landed(S, 0, ['W-ORD-Q0-CLASS-LINES', 'Status DISCHARGED', 'Pin: FINDINGS :%s' % e], key='rl2')
    got = None
    for l in S['orders'].split(NL):
        try:
            o, st, tr = REC.read_order_row(l)
        except Exception:
            continue
        if o == 'W-ORD-Q0-CLASS-LINES':
            got = (st, tr, l)
    return ok1 and bool(got) and got[0] == 'DISCHARGED' and got[1] == 'the corrigendum entry at FINDINGS :%s' % e \
        and (':%s ' % x.get('line')) in got[2]


# ================================================================== (R288)(3): THE NAMING, THE CUT, THE PRINTS, THE GENERATOR
def naming_ok(S):
    """N3: the order's line, the rule row and the table rows printed verbatim before the naming line, the workflow, print list and print bank
    read in the same bank, the bank written before the kernel's first write (the workflow commit)."""
    t, j = S['naming'], S['namingj']
    idx = [t.find(x) for x in ('### THE ORDER, verbatim', '### THE RULE, verbatim', '### THE TABLE ROWS, verbatim', '### NAMED:',
                               '### THE NAMED KERNEL`S WORKFLOW DIRECTORY, PRINT LIST AND PRINT BANK (read before any kernel write)')]
    at = iso_epoch(j.get('at') or '')
    return all(i >= 0 for i in idx) and idx == sorted(idx) and j.get('named') == CANDIDATE and at and S['wf_ct'] and at < S['wf_ct'] \
        and 'relay data/b674_rules.txt :8' in t and 'licensed table :114' in t and 'EQUAL, so the larger table' in t \
        and 'WORKFLOW build-module.yml ABSENT ; PRINT LIST ABSENT' in t


def cut_comment_ok(S):
    return '### ### **FILES 1 ; CODE EQUAL WITH COMMENTS STRIPPED True ; CONTROLS UNEQUAL True ; COMMENT AND DOCSTRING LINES ALONE True.**' in S['cutdiff'] \
        and [x for x in S['cut_names'] if x.strip()] == list(K.T_CUT_FILES)


def prints_ok(S):
    import b678_record as REC
    rows = S['runner'].get('rows') or []
    try:
        gates = dict(REC.read_runner_row(r) for r in rows)
    except Exception:
        return False
    return 'EQUAL LINE FOR LINE True.**' in S['prints'] and gates == {'before': 'DERIVES', 'after': 'DERIVES'} \
        and all(r.get('artifact_sha256') for r in rows) and dict((r['label'], r['run_id']) for r in rows) == dict((l_, r_) for r_, l_ in W_RUNS)


def _pin_rows(cut):
    """each row of the cut bank read whole and unwrapped, from its file:line to the next row (a cite that wraps read as one): (row, text)."""
    blocks = re.split(r'(?m)^(?=  SIDESilencePrinciple/\S+\.lean:\d+)', cut.split('### THE DISTANCE BY')[0])[1:]
    return [' '.join(b.split()) for b in blocks]


def distance_ok(S):
    v = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+) \(OF ANY KIND (\d+), (\d+)\)', S['cut'])
    rows = _pin_rows(S['cut'])
    flat = ' '.join(S['cut'].split())
    return bool(v) and int(v.group(2)) <= int(v.group(1)) and int(v.group(4)) <= int(v.group(3)) and len(rows) == 4 \
        and all(re.search(r':\d+', r) for r in rows) and sum('after MATCHES' in r for r in rows) == 3 \
        and "SIDE-window's Sawtooth header marker at :17" in flat and "SIDE-trivium's header introduction (:8, :23 at v0.1.1" in flat


def corr_carried_ok(S):
    """the generator dry after the tag: its cells changed printed, every one in the roster paper the cut bank names, the run mode not run;
    the five cells carried beneath the nine-kernels item at the landing bank's line, found by conv."""
    v = re.search(r'GENERATOR EXIT 0 ; CELLS CHANGED (\d+) ; LINES NAMING THE CUT KERNEL (\d+) ; RUN MODE', S['corr'])
    diffs = re.findall(r'^\s+(\S+) (:\d+) \| (kernel|profile) \| SIDE-silence-principle \|', S['corr'], re.M)
    cells = sorted(set(diffs))
    return bool(v) and int(v.group(1)) == len(cells) == 5 and all(d[0] == 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME' for d in cells) \
        and landed(S, 0, ['nine-kernels item', 'the five cells are carried here'], key='rl3') and 'RUN MODE ### TO BE RUN' in S['corr'] \
        and 'The `run` mode is NOT RUN' in S['cut']


def nine_line_ok(S):
    """the print banks entered beneath the nine-kernels item (OPEN_TRAILS :14440) at the landing bank's line, found by conv, naming both runs
    and the tag."""
    return landed(S, 0, ['39055170313', '39055212218', 'v0.2.1', '58 of 58'], key='rl3') and 'SIDE-silence-principle at v0.2.0' in oline(S, 14440)


def repairs_ok(S):
    return '### ### **REPAIRS 1 ; THE SEALED COPIES AGREE ; TOOLS CARRIED 8.**' in S['repairs'] and "rfind('BEGIN', 0, k)" in S['citation_src'] \
        and "B_ARMS = ('G-ACTROOT-VERIFY', 'G-SHARED-ADDITIVE')" in S['suite']


def rules_ok(S):
    """(R288)(1): the split entered as a rule row, and the pre-run bank printing the three parts with their seconds."""
    return '(1) THE STANDING ARMS IN TWO FOREGROUND PARTS, THE ACT`S IN ONE' in S['rules'] \
        and all(re.search(r'PART %s : ARMS \d+ ; \d+ s' % p, S['prerun']) for p in K.PARTS)


# ================================================================== THE RUNNER (the standing arms, this act's merged run)
def wf_ok(S):
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or not v['on_main'] or v['commit_files'] != [WF] or v['list_files'] != [PT] or v['lean_in_writes']:
            return False
        if any(w in t for w in ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'print_targets.txt' not in t or 'lake env lean out/axioms.lean' not in t \
                or (('lake exe cache get' in t) != v['mathlib']) or len(v['targets']) != 58:
            return False
    return len(S['wf']) == 1


def runner_ok(S):
    import b678_record as REC
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


POST_SEAL = ('b678 seal', 'b678 pre-root', 'b678 root', 'b678 record', 'b678 --', 'b678 closing')


def _component_commit(s):
    return s.startswith('b678') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 55 and rows[54][:3] == ['b678', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b679_' in it] \
        and any(it.startswith('data/b678_corrigendum.txt ') for it in items) and any(it.startswith('data/b678_cut.txt ') for it in items) \
        and all(any(it.startswith(p + ' ') for it in items) for p in K.SHARED_APPENDED) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b678_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b678') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 679)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The corrigendum**', '**The re-cut**', '**The tools**', '**The root.**', '**The scores.**',
                 '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b679')


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
    import b678_record as REC
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
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE CORRIGENDUM' in t \
        and '### THE NAMING' in t and '### THE RE-CUT' in t and '### THE CARRY-TIME' in t


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


def _ledger_mut(S):
    j = S['corrj']
    f, n = (j.get('rows') or [{}])[0].get('file'), (j.get('rows') or [{}])[0].get('line')
    key = 'find' if f == 'FINDINGS.md' else 'ot'
    ls = S[key].split(NL)
    ls[n - 1] = ls[n - 1] + ' (pinned)'
    return put(S, key, NL.join(ls))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R288) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: at the start and after the tests, none of tail, lean, lake, python or bash running',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('none of each', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b677_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s and PLACE-papers` branch lists, local and remote-tracking, and the branches bank (the ruling`s list alone)',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b677'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: no prompt put in this act, the head counting 0 and NONE printed', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS, 0 prompt(s)', 'THE AUTHOR`S ANSWERS, 1 prompt(s)'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b678_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: landed(S, 0, ['b677 AT ITS WEIGHT', 'Nothing deposited.', 'Nine defects']),
     lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, verdict lines and tag rows printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step): run before the ferry was banked, no miss, its predicate read unwrapped and said so',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('RUN BEFORE THE FERRY IS BANKED', 'RUN'))),
    ('G-R288-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R288) END' in S['ferry'] and S['ot'].count('**(R288) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R288) ratified', '**(R2880) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: five rows through the record tool`s reader, each local, merged and deleted',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob in any half, the ruling`s list exactly (N4)',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b677 push-b677-root")])),
    ('G-CORRIGENDUM-GENERATED', 'the corrigendum bank`s rows through the record tool`s reader, the entry at FINDINGS by its title through conv, every row printed in it, the count the hand count less the carried (N2)',
     lambda S: corr_generated_ok(S), lambda S: _mut(S, 'corrj', lambda d: d['rows'].pop())),
    ('G-LEDGER-LINES-UNMOVED', 'the 35 ledger lines the corrigendum answers, each at PLACE-papers before the act and now (N2)',
     lambda S: ledger_unmoved_ok(S), lambda S: _ledger_mut(S)),
    ('G-CORRIGENDUM-TOOL-ALONE', 'the corrigendum tool`s commit (5d3416b8): its one file the tool, the working tree equal to HEAD',
     lambda S: corr_tool_alone_ok(S), lambda S: put(S, 'corr_tool_files', S['corr_tool_files'] + ['data/b678_corrigendum.txt'])),
    ('G-ORDER-DISCHARGED', 'OPEN_TRAILS at the landing bank`s line, found by conv, and the orders bank`s row through the record tool`s reader: DISCHARGED, the entry`s line its pin',
     lambda S: order_discharged_ok(S), lambda S: put(S, 'orders', S['orders'].replace('DISCHARGED       :', 'OPEN             :'))),
    ('G-ROWGEN-AFTER', 'the rowgen bank after the corrigendum: both exit 0, its totals the step-zero run`s',
     lambda S: rowgen_after_ok(S), lambda S: put(S, 'rowgen_after', S['rowgen_after'].replace('STALE 0', 'STALE 1'))),
    ('G-NAMING-BEFORE-WRITE', 'the naming bank: the order`s line, the rule row and the table rows verbatim before the naming line, the tie broken by the larger table, the workflow and print list declared absent, the bank written before the kernel`s first write (N3)',
     lambda S: naming_ok(S), lambda S: _mut(S, 'namingj', lambda d: d.update(at='2026-10-17T23:59:59Z'))),
    ('G-CUT-COMMENT-ONLY', 'the cut`s diff bank and the kernel`s own diff between the print-list main and the cut: one file, its code equal with comments stripped, the control unequal',
     lambda S: cut_comment_ok(S), lambda S: put(S, 'cut_names', S['cut_names'] + ['SIDESilencePrinciple.lean'])),
    ('G-PRINTS-EQUAL', 'the prints bank and the runner rows through the record tool`s reader: both runs DERIVES by their ids, the artifacts` digests agreeing, the prints equal line for line',
     lambda S: prints_ok(S), lambda S: put(S, 'prints', S['prints'].replace('EQUAL LINE FOR LINE True', 'EQUAL LINE FOR LINE False'))),
    ('G-CUT-DISTANCE', 'the cut bank: the distance by b670`s method and of any kind at or below before, every row pinned by path and line, the residues of b674 and b676 named as carried (N3)',
     lambda S: distance_ok(S), lambda S: put(S, 'cut', S['cut'].replace('THE DISTANCE BEFORE 4, AFTER 1', 'THE DISTANCE BEFORE 4, AFTER 6'))),
    ('G-CORRESPONDENCE-CARRIED', 'the generator`s dry bank, the cut bank and the nine-kernels line: the cells it would change printed, the run mode not run, the cells carried',
     lambda S: corr_carried_ok(S), lambda S: put(S, 'cut', S['cut'].replace('The `run` mode is NOT RUN', 'The `run` mode is RUN'))),
    ('G-NINE-KERNELS-LINE', 'OPEN_TRAILS at the landing bank`s line beneath the nine-kernels item, found by conv: both runs, the tag, 58 of 58',
     lambda S: nine_line_ok(S), lambda S: _rl(S, 0, 1, key='rl3')),
    ('G-TOOL-REPAIRS', 'the carry-time bank`s verdict and the carried tools` code: one repair (the standing parts two), the sealed copies agreeing, the mid-act cut carried',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS 1 ;', 'REPAIRS 0 ;'))),
    ('G-RULES-ROW', 'the rules bank`s row of (R288)(1) and the pre-run bank`s three parts with their seconds',
     lambda S: rules_ok(S), lambda S: put(S, 'rules', S['rules'].replace('(1) THE STANDING ARMS IN TWO FOREGROUND PARTS', '(1) THE ARMS'))),
    ('G-SPEC-PLANTED', 'tools/b678_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('corrigendum' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b678 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b678_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b678_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-silence-principle`s main, this act`s merged run`s kernel: the workflow committed alone (5d2e587), the print list alone (6968b6c, 58 names), no .lean byte in either, no author identifier, no secret, the hold, the cache step only where Mathlib is required, the print step over print_targets.txt',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[CANDIDATE].update(text=d[CANDIDATE]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s merged run`s row (SIDE-silence-principle after) through the record tool`s reader: the run id and ref, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s merged run`s gate reading: build exit 0, no error line, every terminal of its axioms bank printed, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbank', S['rbank'].replace('GATE DERIVES', 'GATE NOT DERIVES'))),
    ('G-MERGES-ON-GATE', 'SIDE-silence-principle`s main: the merge commit of the built tip on the print-list main, the merged tree the built tree, its tag v0.2.1 peeled to it',
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
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read after Component 3`s kernel writes and before the seal, SIDE-silence-principle among them',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b677`s and the earlier tools, the generator, b667`s certify and map, b671`s narrowing, rowgen`s, the mirror`s, the instruments and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at da8a46bc but the shared additive files (the orders bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b677_stepzero.txt'])),
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
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b678 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b678_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in three parts summed (R288)(1)',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b677`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b677 — lane two, act one hundred and four, the research act' in S['ot']
     and S['rootsf'].count(NL + 'b677 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b677 — lane two', '### b677 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 55th line, the root bank and its items, the corrigendum, cut and orders banks among them', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b679 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b678 AGREE, b678 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b678 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b678_record.py agree', 'b678_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b679', lambda S: '**Next:** b679' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b679', '**Next:** b680'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since da8a46bc and f614597 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b678')" in S['suite'] and "'data/b678_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b678_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the corrigendum, the naming, the re-cut, the carry-time reading',
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
    p = os.path.join(D, 'b678_seal_hashes.json')
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
    print('  written: b678_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b678_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b678_checks_postpush.txt' if pushed else 'b678_checks.txt'


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
    """(R288)(1): the run's bank from its three part banks, the counts summed and every part's seconds printed at its head; the parts' banks
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
    fails = sum((json.loads(m.group(5)) if m.group(5) != 'NONE' else [] for _p, m, _t in parts), [])
    defs = sum((json.loads(m.group(8)) if m.group(8) != 'NONE' else [] for _p, m, _t in parts), [])
    deq = all(m.group(9) == 'True' for _p, m, _t in parts)
    ok = lf == 0 and pc == 0 and ng == 0 and deq
    out = ['=' * 104, heads[0].replace('PART standing-a', 'THREE PARTS SUMMED ((R288)(1))'), '=' * 104] + [
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
        ex.update(jl('b678_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b678_checks.txt', 'b678_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b678_exercise.json')
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
        print('### (R288)(1): every run in three foreground parts -- give `--part %s`' % ' | '.join(K.PARTS))
        return 2
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b678 -- THE SUITE. ### **%s READING.** ### PART %s ((R288)(1)) ### every arm exercised on both controls.' % (
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b677`s face less its own arms) %d ; carried here %d ; the act`s arms over its own banks %s ; '
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
    rec('  ### THE CITATION CHECK: %s ; THE CORRIGENDUM: rows %d, carried %d, FINDINGS :%s ; THE CUT: %s' % (
        mc.group(0) if mc else '### UNREAD', len(S['corrj'].get('rows') or []), len(S['corrj'].get('carried') or []), S['corrj'].get('entry_line'),
        (re.search(r'THE DISTANCE BEFORE \d+, AFTER \d+', S['cut']) or [None])[0] if re.search(r'THE DISTANCE BEFORE', S['cut']) else '### UNREAD'))
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
    lp = os.path.join(D, _part_name(base, PART).replace('b678_arms_prerun', 'b678_lsr_prerun').replace('b678_checks', 'b678_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b678_exercise_%s.json' % PART)
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
