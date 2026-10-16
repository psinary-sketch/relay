# -*- coding: utf-8 -*-
"""b672_checks.py -- THE SUITE OF b672, UNDER (R282): b671 AT ITS WEIGHT; THREE RULES; THE CORRESPONDENCE GENERATOR AND ITS FOUR PLANTED
CASES; THE ROSTER'S TABLES REGENERATED AT THEIR KERNELS' TAGS; THE COPY OF RECORD AS REGISTRY NAMES IT, NOTHING MOVED; READING (ii) RE-RUN
AT THE STABLE ANCHORS. NO KERNEL BYTE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R264)(2), THE FREEZE: the standing arms are b671's face's (G2) arms less b671's own arms over b671's banks, carried, their act needles
### read in b672's banks (b671 at its weight, b671's branches, this act's step-zero bank); the act's own arms read this act's banks alone
### (tools/b672_worklist.py ACT_ARMS). The standing runner arms read the last merged run, b669's: this act builds nothing.
### ### Three standing arms read act lists that this act's ruling changes, declared on the face: G-PP-SCOPE (PLACE-papers' changed files
### against the ledgers AND the files the generator wrote and b651's line's file), G-CURRENTS-UNEDITED (the currents less
### SIMPLICITY_OF_RIEMANN_ZEROS.md, the roster's file the generator wrote), G-WEIGHT-LINE (b671's weight).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b672_record.py).
### ### The harness is b568's to b671's (helpers, runner, seal), written by the Write tool from tools/b671_checks.py; the sources, predicates
### ### and arms over this act's banks are b672's.
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
import b672_worklist as K     # noqa: E402
import b671_worklist as K671  # noqa: E402
from b672_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b672_registration_2026-10-16.txt')
B671_FACE = os.path.join(D, 'b671_registration_2026-10-14.txt')
B671_ACT_ARMS = K.B671_ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = K.STEPZERO
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
INST = ('b671_checks.py', 'b671_closing.py', 'b671_tests.py', 'b671_worklist.py', 'b671_reg_gate.py', 'b671_regspec.py', 'b671_record.py',
        'b671_citation.py', 'b671_narrow.py', 'b671_epstein_map_narrowed.py', 'b671_tie_diagnostic.py',
        'b670_checks.py', 'b670_closing.py', 'b670_tests.py', 'b670_worklist.py', 'b670_reg_gate.py', 'b670_regspec.py', 'b670_record.py',
        'b670_citation.py',
        'b669_checks.py', 'b669_closing.py', 'b669_tests.py', 'b669_worklist.py', 'b669_reg_gate.py', 'b669_regspec.py', 'b669_record.py',
        'b669_citation.py',
        'b668_checks.py', 'b668_closing.py', 'b668_tests.py', 'b668_worklist.py', 'b668_reg_gate.py', 'b668_regspec.py', 'b668_record.py',
        'b668_citation.py',
        'b667_checks.py', 'b667_closing.py', 'b667_tests.py', 'b667_worklist.py', 'b667_reg_gate.py', 'b667_regspec.py', 'b667_record.py',
        'b667_citation.py', 'b667_epstein_certify.py', 'b667_epstein_map_balls.py', 'b667_tail_recheck.py', 'b667_bessel_probe.py',
        'b667_ball_probe.py',
        'b666_checks.py', 'b666_closing.py', 'b666_tests.py', 'b666_worklist.py', 'b666_reg_gate.py', 'b666_regspec.py', 'b666_record.py',
        'b666_citation.py',
        'b665_checks.py', 'b665_closing.py', 'b665_tests.py', 'b665_worklist.py', 'b665_reg_gate.py', 'b665_regspec.py', 'b665_record.py',
        'b665_citation.py',
        'b664_checks.py', 'b664_closing.py', 'b664_tests.py', 'b664_worklist.py', 'b664_reg_gate.py', 'b664_regspec.py', 'b664_record.py',
        'b664_citation.py', 'test_met_b646.py',
        'b663_checks.py', 'b663_closing.py', 'b663_tests.py', 'b663_worklist.py', 'b663_reg_gate.py', 'b663_regspec.py', 'b663_record.py',
        'b663_epstein_map.py', 'b663_citation.py',
        'b662_checks.py', 'b662_closing.py', 'b662_tests.py', 'b662_worklist.py', 'b662_reg_gate.py', 'b662_regspec.py', 'b662_record.py',
        'b662_map.py', 'b662_citation.py',
        'b661_checks.py', 'b661_closing.py', 'b661_tests.py', 'b661_worklist.py', 'b661_reg_gate.py', 'b661_regspec.py', 'b661_record.py',
        'b661_map.py',
        'b659_checks.py', 'b659_closing.py', 'b659_tests.py', 'b659_worklist.py', 'b659_reg_gate.py', 'b659_regspec.py', 'b659_record.py',
        'b658_checks.py', 'b658_closing.py', 'b658_tests.py', 'b658_worklist.py', 'b658_reg_gate.py', 'b658_regspec.py', 'b658_record.py',
        'b647_record.py', 'test_msplit_b658.py', 'b572_record.py', 'b564_record.py',
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
        'mirror_roster.json', 'mirror_prevbuild.json',
        'b616_claims.py', 'ferry_scan.py', 'e0_rule.py', 'test_e0_rule.py', 'build_watch.py', 'test_build_watch_b647.py', 'chain_page.py',
        'axiom_claim.py', 'licensed_table.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py',
        'test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_axiom_claim_b651.py', 'test_conversion_b652.py',
        'test_licensed_table_instrument_b652.py', 'test_chain_page_b638.py', 'b314_coldclone.py', 'test_composer_b647.py', 'test_composer_b649.py',
        'test_name_b649.py', 'b627_margin.py', 'b627_worklist.py', 'b326_zeros.py', 'b326_offline.py',
        'rowgen/rowgen.py', 'rowgen/diff_rowpin.py', 'rowgen/namemap.json')
# ### the currents b671 read, less SIMPLICITY_OF_RIEMANN_ZEROS.md: the roster's file for its table, which the generator wrote ((R282)(4))
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md')
TABLE_FILES = K.TABLE_FILES
WF = '.github/workflows/build-module.yml'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b672')
            and 'data/b672_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b672_record as REC
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
        if (f.startswith('b672_') and f.endswith('.py')) or f in K.GEN_FILES_BASE:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b672_regspec as SPEC
    import b672_record as REC
    P = SPEC.planted()
    ctl = []
    for f in (lambda: REC.read_score_row('X9', 'HELD'),
              lambda: REC.read_corr_row(dict(line=1, kernels=['SIDE-x'], reading='PRINTED'))):
        try:
            f()
            ctl.append(False)
        except Exception:
            ctl.append(True)
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def wf_state():
    out = {}
    for k, r in K.RUNNER.items():
        t = read_blob('D:/' + k, 'main:' + WF)
        out[k] = dict(text=t, commit_files=files_of('D:/' + k, r['workflow_commit']),
                      on_main=subprocess.run(['git', '-C', 'D:/' + k, 'merge-base', '--is-ancestor', r['workflow_commit'], 'main']).returncode == 0,
                      targets=[l.strip() for l in read_blob('D:/' + k, 'main:print_targets.txt').split(NL) if l.strip()])
    return out


def merges_state():
    out = {}
    for k, r in K.RUNNER.items():
        p = 'D:/' + k
        out[k] = dict(main=gs(p, 'rev-parse', '--short=7', 'main'), parents=gs(p, 'log', '-1', '--format=%p', '--abbrev=7', 'main').split(),
                      built=r['ref'][:7], tree_main=gs(p, 'rev-parse', 'main^{tree}'), tree_built=gs(p, 'rev-parse', r['ref'] + '^{tree}'),
                      tags=dict((t, gs(p, 'rev-parse', '--short=7', t + '^{commit}')) for t in gs(p, 'tag', '--points-at', 'main').split()))
    return out


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted(set(g2_of(B671_FACE)) - set(B671_ACT_ARMS))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py', 'test_correspondence_gen.py')


def _ct_first(repo, pre, prefix, path=None):
    args = ['log', '--reverse', '--format=%ct %s', pre + '..HEAD'] + (['--', path] if path else [])
    for l in gs(repo, *args).split(NL):
        if l.strip() and l.split(' ', 1)[1].startswith(prefix):
            return int(l.split(' ', 1)[0])
    return None


def gen_dry():
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'correspondence_gen.py'), 'dry'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return dict(rc=r.returncode, out=(r.stdout or '') + (r.stderr or ''))


def sources():
    import b672_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b672_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b672_') and f.endswith('.py')) or f in K.GEN_FILES_BASE)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    aj = jl('b672_author_answers.json').get('calls') or []
    tc = REC._table_commit()
    pairs = REC.read_pairs()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b672_ferry.txt'), scan=rd('b672_ferry_scan.txt'), stepz=rd('b672_stepzero.txt'),
        readfirst=rd('b672_readfirst.txt'), defects=rd('b672_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b672_author_answers.txt'), answj=aj, prerun=rd('b672_arms_prerun.txt'), rl=jl('b672_record_lines.json'),
        rl3=jl('b672_record_lines_c3.json'), rlp=jl('b672_record_lines_prosepins.json'),
        tests=jl('b672_tests_stepzero.json'), testst=rd('b672_tests_stepzero.txt'), withheld=jl('b672_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b672_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), cmdj=jl('b672_commands.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b672_checks.py')),
        citation=rd(K.CITATION_BANK), c1_ct=_ct_first(ROOT, PRE['relay'], 'b672 Component 1'),
        gate=rd('b672_reg_gate.txt'), rules=rd('b672_rules.txt'), gentest=rd('b672_gen_test.txt'),
        roster=jl('b672_roster_read.json'), rostert=rd('b672_roster_read.txt'), b670c=jl('b670_correspondence.json'),
        onecopy=jl('b672_one_copy.json'), onecopyt=rd('b672_one_copy.txt'), npairs=len(pairs), pairs=pairs,
        dj=jl('b672_correspondence_diff.json'), dt=rd('b672_correspondence_diff.txt'), af=jl('b672_correspondence_after.json'),
        at=rd('b672_correspondence_after.txt'), rerun=rd('b672_gen_rerun.txt'), rowsk=rd('b672_rows_kept.txt'),
        hypj=jl('b672_hypotheses.json'), hypt=rd('b672_hypotheses.txt'), gendry=gen_dry(),
        gen_commits=dict((c, (files_of(ROOT, c), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', c, 'HEAD']).returncode == 0,
                              int(gs(ROOT, 'log', '-1', '--format=%ct', c) or 0))) for c in K.GEN_COMMITS),
        table_commit=tc, table_files=files_of(PP, tc) if tc else [], table_ct=int(gs(PP, 'log', '-1', '--format=%ct', tc) or 0) if tc else 0,
        b651=(cr0(blob(PP, PRE['pp'] + ':' + K.B651_COPY)), cr0(raw(os.path.join(PP, *K.B651_COPY.split('/')))),
              read(os.path.join(PP, *K.B651_SOURCE.split('/')))),
        superseded=os.path.exists(os.path.join(PP, 'archive', 'superseded')),
        unversioned=dict((u, (os.path.exists(os.path.join(PP, *u.split('/'))),
                              subprocess.run(['git', '-C', PP, 'cat-file', '-e', 'HEAD:' + u], capture_output=True).returncode == 0)) for u, _v in pairs),
        standing=STANDING, wf=wf_state(), runner=jl(K.RUNNER_ROWS), rbank=rd(K.RUNNER_BANK), merges=merges_state(),
        open_local=gs(K.KD, 'rev-parse', K.OPEN_BRANCH), open_remote=gs(K.KD, 'rev-parse', 'origin/' + K.OPEN_BRANCH),
        open_on_main=subprocess.run(['git', '-C', K.KD, 'merge-base', '--is-ancestor', K.RUNNER[K.KERNEL]['prior_ref'], 'main']).returncode == 0,
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b672_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b672_act_root.json'), arj0=jl('b671_act_root.json'), art=rd('b672_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b672_kernels_face.json').get('kernels') or {}),
        push_lists={r: gs(r, 'branch', '-a', '--list', '*push-b671*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b672_mustnotexist.txt')),
        fj=jl('b672_findings.json'), tj=jl('b672_trail.json'), sc=jl('b672_scores.json'), desk=rd('b672_desk_notes.txt'), tfj=jl('b672_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['pp_allowed'] = sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md']) | set(REC._pp_written()))
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
        if f.startswith(('b672_', 'audit_b672_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith('.gz'):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    S['outside'] = [n for n in R41.OAI_NEEDLES if n in S['ledger_adds']]
    shared = set(ADD.shared_files()) | set(K.SHARED_APPENDED)      # ### (R282)(6) H5's dated line: shared by this act's root
    S['shared_appended'] = dict((p, (cr0(blob(ROOT, PRE['relay'] + ':' + p)), cr0(raw(os.path.join(ROOT, *p.split('/')))))) for p in K.SHARED_APPENDED)
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


def unwrap(t):
    """a bank's text with each line's leading `###` markers dropped and the whitespace collapsed (b670 (h))."""
    return ' '.join(' '.join(re.sub(r'^\s*(?:###\s*)+', '', l) for l in t.split(NL)).split())


def procs_ok(S):
    """the step-zero bank's process listings, in this act's words: at the start and before the tests' restart, the seat's process alone and
    no tail, lean, lake or python process."""
    p = unwrap(S['stepz'])
    return 'claude.exe 14680 alone; no tail, lean, lake or python process' in p and '(before the restart): claude.exe 14680 alone' in p


STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 2' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"
PROMPT_HEADS = ('(One copy)', '(b651 line)', '(Dry diff)', '(H2 ABSENT)', '(REGISTRY)')


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b672 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) >= 1 and all(x >= 2 for x in per) and len(res) == len(calls) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and all(x in a for x in PROMPT_HEADS)


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def no_local_lean(S):
    import b672_record as REC
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


# ================================================================== (R282) STEP ZERO: THE CITATION CHECKS, THE BRANCHES
READFIRST_NEEDLES = ('data/b671_closing.txt', 'data/b671_defects.txt', 'data/b671_closing_push_out.txt')


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    z = unwrap(S['stepz'])
    return all(v == '' for v in S['push_lists'].values()) and 'relay push-b671 (4e3a46d6)' in z and 'push-b671-root (9bdaf75d)' in z \
        and 'push-b671-closing (64158393)' in z and 'PLACE-papers push-b671 (d6d2d4b)' in z and 'push-b671-root (84ba4fa)' in z \
        and 'chi-li-b669 kept at b804bf2' in z and 'after `git branch --merged main` listed them' in z


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def citation_ok(S):
    """the step-zero check: run before the ferry was banked; its misses (none) raised to the author before the component citing them."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'RUN BEFORE THE FERRY IS BANKED' in c \
        and int(m.group(3)) == 0 and S['c1_ct'] is not None


MID_NEEDLES = ('on step zero, under (R282)', 'on the four readings', 'on readings 5', 'on the four tabs', 'on the b651 line',
               'on the NOT PRINTED cells', 'on the ABSENT count', 'on the REGISTRY', 'on Component 3')


def midact_ok(S):
    """(R278)(4): every mid-act answer's check appended; each answer's last print with no miss."""
    blocks = re.split(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', S['citation'], flags=re.M)[1:]
    last = {}
    for b in blocks:
        for n in MID_NEEDLES:
            if repr(n) in b.split(NL)[0]:
                m = re.search(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', b)
                last[n] = m.groups() if m else None
    return all(last.get(n) and last[n][2] == '0' for n in MID_NEEDLES)


# ================================================================== (R282)(1), (2), (7): THE RECORD LINES
def rules_ok(S):
    import b672_record as REC
    o = oline(S, rline(S, 1).get('line'))
    r = S['rules']
    texts = REC.rules_texts()
    return landed(S, 1, ['THREE RULES']) and len(texts) == 3 and all(conv(x) in o for x in texts) \
        and all(' '.join(x.split()).replace('’', "'") in r.replace('’', "'") for x in texts)


def split_item_ok(S):
    dj = S['dj']
    npb = sorted(k for k, v in (dj.get('banks') or {}).items() if v is None and (dj.get('tags') or {}).get(k))
    o3 = oline(S, rline(S, 0, 'rl3').get('line'))
    return landed(S, 2, ['THE LEDGER SPLIT', '**Trigger:** “the b680 reading act”']) and bool(npb) \
        and landed(S, 0, ['THE KERNELS WITH NO RELAY PRINT BANK'], 'rl3') and all(k in o3 for k in npb) and ('%d kernels' % len(npb)) in o3


ORDER_NAMES = ('`W-ORD-TABLE-SHAPE`', '`W-ORD-GRADE-MOVED`', '`W-ORD-PRINT-TARGETS`', '`W-ORD-ABSENT-DECLARATIONS`', '`W-ORD-ONE-COPY`')


def orders_ok(S):
    ok = all(landed(S, i + 1, [n, '**Trigger:**'], 'rl3') for i, n in enumerate(ORDER_NAMES))
    return ok and landed(S, 0, ['`W-ORD-PROSE-PINS`', '**Trigger:** “the document’s next re-cut act”'], 'rlp') \
        and 'REGISTRY’s file column read for every keystone with two copies' in oline(S, rline(S, 5, 'rl3').get('line'))


# ================================================================== (R282)(3)-(6): THE GENERATOR, THE ROSTER, THE RUN, READING (ii)
def gen_planted_ok(S):
    p = S['planted']['test_correspondence_gen.py']
    return p['rc'] == 0 and '### ### **PLANTED CASES 4 ; AS WANTED 4 ; PASS**' in p['out'] and p['out'].strip() == S['gentest'].strip()


def gen_alone_ok(S):
    cs = S['gen_commits']
    return bool(cs) and all(f and set(f) <= set(K.GEN_FILES) and anc and 0 < ct < S['table_ct'] for f, anc, ct in cs.values()) \
        and S['table_ct'] > 0


def roster_ok(S):
    t = S['roster'].get('tables') or []
    return len(t) == len(S['b670c'].get('tables') or []) + 1 and all(isinstance(x.get('found_b670'), list) for x in t) \
        and all(('heading' not in x and 'heading_sha256' in x) if x.get('withheld') else ('heading' in x and 'header' in x) for x in t) \
        and '### ### **TABLES %d ; ANCHOR FOUND AT THE ROSTER`S FILE %d' % (len(t), len(t)) in S['rostert']


def onecopy_ok(S):
    p = S['onecopy'].get('pairs') or []
    return len(p) == S['npairs'] > 0 and all(isinstance(x.get('standing_hits'), list) and x.get('record') for x in p) \
        and ('### ### **PAIRS %d ;' % len(p)) in S['onecopyt']


def gen_run_ok(S):
    import b672_record as REC
    dj = S['dj']
    try:
        for t in dj.get('tables') or []:
            for r in t['rows']:
                REC.read_corr_row(r)
    except Exception:
        return False
    listed = sum(len(t['changes']) if isinstance(t.get('changes'), list) else (t.get('changes') or 0) for t in dj['tables'])
    files = sorted(os.path.relpath(f.replace('\\', '/'), PP).replace('\\', '/') for f in dj.get('files') or [])
    tags = dj.get('tags') or {}
    lines = re.findall(r'^    (SIDE-[a-z0-9-]+)\s+(READ|NO TAG AT THE REMOTE)', S['dt'], re.M)
    return listed == (dj.get('counts') or {}).get('CELLS CHANGED') and files == sorted(S['table_files']) and bool(files) \
        and sorted(k for k, _r in lines) == sorted(tags) and '### THE TAGS: one `git ls-remote --tags origin` per repository' in S['dt']


def gen_rerun_ok(S):
    g = S['gendry']
    return g['rc'] == 0 and 'CELLS CHANGED 0 ; FILES CHANGED 0' in g['out'] and 'CHANGES 0 CELLS IN 0 FILES' in S['rerun'] and ': HELD.**' in S['rerun']


def rows_kept_ok(S):
    m = re.search(r'\*\*H3: FILES (\d+) ; LINES CHANGED (\d+) ; ROWS GAINED OR LOST 0 IN (\d+) OF (\d+) FILES ; CHANGED LINES OUTSIDE A TABLE OR '
                  r'WITH A BLANK OR LOST CELL (\d+) ; DIFF BANK CELLS (\d+), LISTED (\d+) -- (HELD|REFUTED)\.\*\*', S['rowsk'])
    return bool(m) and int(m.group(1)) == len(S['table_files']) and m.group(3) == m.group(4) and m.group(5) == '0' and m.group(6) == m.group(7) \
        and m.group(8) == 'HELD'


def after_ok(S):
    h = S['af'].get('h2') or {}
    m = re.search(r'b670`S 100 \+ (\d+) ANCHOR ROWS ITS READER SKIPPED \+ 0 OTHER', S['at'])
    return bool(h) and h.get('kernel_cell') == 0 and h.get('behind') == (h.get('kernel_cell') or 0) + (h.get('prose') or 0) \
        and 'THE CHANGE OF METHOD, DECLARED' in S['at'] and m is not None and ('H2, OVER THE SHAPED TABLES, BY b670`S METHOD: ROWS BEHIND %s' % h.get('behind')) in S['at']


def state_line_ok(S):
    pre, now = S['shared_appended'][K.SHARED_APPENDED[0]]
    a = appended(pre, now)
    return bool(pre) and bool(now) and now.startswith(pre) and 'Appended 2026-10-16 by b672 under (R282)(6) H5' in a \
        and '54 rows to zero (b670: 90)' in a and 'the 10 anchor rows its reader skipped' in a


def b651_ok(S):
    pre, now, src = S['b651']
    a = appended(pre, now)
    line = next((l for l in src.split(NL) if l.startswith('*Appended 2026-10-11 by b651, under the author\'s ruling `(R261)`(3)(d)')), '')
    return bool(pre) and bool(now) and now.startswith(pre) and bool(line) and line in a and 'b651\'S LINE, CARRIED TO THE COPY OF RECORD' in a


def nothing_moved_ok(S):
    cm = S['cmdj']
    rows = dict((r['n'], r['cmd']) for r in cm.get('rows') or [])
    mv = [rows[n] for n in cm.get('moves_deletes') or [] if n in rows and re.search(r'\bgit\s+(-C\s+\S+\s+)?mv\b', rows[n])]
    return not S['superseded'] and len(S['unversioned']) == S['npairs'] > 0 and all(a and b for a, b in S['unversioned'].values()) \
        and 'moves_deletes' in cm and not mv


def hyp_ok(S):
    import b672_record as REC
    h = S['hypj']
    try:
        st = [REC.read_score_row(k, h.get(k))[1] for k in ('H1', 'H2', 'H3', 'H4', 'H5')]
    except Exception:
        return False
    return sorted(h) == ['H1', 'H2', 'H3', 'H4', 'H5'] and all(' data/b672_' in v[1] for v in h.values()) \
        and ('### ### **H1 %s ; H2 %s ; H3 %s ; H4 %s ; H5 %s.**' % tuple(st)) in S['hypt']


def open_kept_ok(S):
    t = K.RUNNER[K.KERNEL]['prior_ref']
    return S['open_local'] == t and S['open_remote'] == t and not S['open_on_main'] and t.startswith(K.OPEN_TIP)


# ================================================================== THE RUNNER (the standing arms, the last merged run: b669's)
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
    import b672_record as REC
    w = K.RUNNER[K.KERNEL]
    rows = [r for r in S['runner'].get('rows') or [] if r.get('run_id') == w['run_id']]
    if len(rows) != 1:
        return False
    for r in rows:
        x = REC.read_runner_row(r)
        if r['ref'] != w['ref'] or r['conclusion'] != 'success' or not r['artifact_sha256'] or not x['above_hold']:
            return False
    return True


def gate_ok(S):
    rows = [r for r in S['runner'].get('rows') or [] if r.get('run_id') == K.RUNNER[K.KERNEL]['run_id']]
    return bool(rows) and rows[0].get('gate') == 'DERIVES' and 'GATE DERIVES' in S['rbank'] \
        and ('TERMINALS %d, PRINTED %d' % (K.PRINT_TARGETS_N, K.PRINT_TARGETS_N)) in S['rbank'] \
        and 'BUILD EXIT 0 ; ERROR LINES 0' in S['rbank'] and re.search(r'^### the artifact: .* ; AGREE$', S['rbank'], re.M) is not None


def merges_ok(S):
    rows = dict((r['kernel'], r) for r in S['runner'].get('rows') or [] if r.get('run_id') == K.RUNNER[K.KERNEL]['run_id'])
    for k, m in S['merges'].items():
        r = rows.get(k, {})
        if not r.get('merged') or r.get('gate') != 'DERIVES' or m['main'] != r['merged'][:7] or len(m['parents']) != 2 \
                or m['built'] not in m['parents'] or m['tree_main'] != m['tree_built'] or m['tags'].get(r.get('tag')) != r['merged'][:7] \
                or r.get('tag') != K.NEXT_TAG:
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


POST_SEAL = ('b672 seal', 'b672 pre-root', 'b672 root', 'b672 record', 'b672 --', 'b672 closing')


def _component_commit(s):
    return s.startswith('b672') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 49 and rows[48][:3] == ['b672', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b673_' in it] \
        and any(it.startswith('data/b672_correspondence_diff.json ') for it in items) \
        and all(any(it.startswith(p + ' ') for it in items) for p in K.SHARED_APPENDED) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b672_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b672') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 673)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The record lines**', '**The generator**', '**The roster and the copy of record**', '**The run**',
                 '**Reading (ii)**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b673')


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
    import b672_record as REC
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
    """PLACE-papers' changed files against the ledgers, the files the generator wrote and b651's line's file ((R282)(4), (5)); declared."""
    return S['pp_changed'] == S['pp_allowed']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE GENERATOR' in t \
        and '### THE RUN' in t and '### READING (ii)' in t and '### THE HYPOTHESES' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R282) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: the seat`s process alone at the start and before the tests` restart, no tail, lean, lake or python process',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('claude.exe 14680 alone', 'claude.exe 14680 and python'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b671_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay and PLACE-papers branch lists, local and remote-tracking, and the step-zero bank (the ferry`s list alone)',
     lambda S: branches_ok(S), lambda S: put(S, 'push_lists', {'D:/relay': 'push-b671'})),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its prompts with their options and results', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS', 'THE ANSWERS'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b672_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: landed(S, 0, ['b671 AT ITS WEIGHT', 'Nothing deposited.', 'eighteen defects']),
     lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step): run before the ferry was banked, no miss',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('RUN BEFORE THE FERRY IS BANKED', 'RUN'))),
    ('G-MIDACT-CHECKED', 'the citation check`s bank ((R278)(4)): each of the nine answers checked, its last print with no miss',
     lambda S: midact_ok(S), lambda S: put(S, 'citation', S['citation'].replace("'on the REGISTRY'", "'x'"))),
    ('G-RULES-ENTERED', 'OPEN_TRAILS at the record-lines bank`s line and the rules bank: the three rules verbatim from the ferry bank',
     lambda S: rules_ok(S), lambda S: put(S, 'rules', '')),
    ('G-LEDGER-SPLIT-ITEM', 'OPEN_TRAILS at the record-lines banks` lines: the ledger split with its trigger, the kernels without a print bank beneath it by name',
     lambda S: split_item_ok(S), lambda S: _rl(S, 0, 1, 'rl3')),
    ('G-GEN-PLANTED', 'tools/test_correspondence_gen.py run live: four of four, its print the planted-case bank`s', lambda S: gen_planted_ok(S),
     lambda S: put(S, 'gentest', S['gentest'] + 'x')),
    ('G-GEN-COMMITTED-ALONE', 'the generator`s commits: each the tool and its test alone, ancestors of HEAD, before the table commit',
     lambda S: gen_alone_ok(S), lambda S: _mut(S, 'gen_commits', lambda d: d.update({K.GEN_COMMITS[0]: (['data/x.txt'], True, 1)}))),
    ('G-ROSTER-READ', 'the roster bank: b670`s tables and E_DIFFICULTY`s, each anchored, the withheld document`s by sha256 alone',
     lambda S: roster_ok(S), lambda S: _mut(S, 'roster', lambda d: d['tables'][9].update(heading='x'))),
    ('G-ONE-COPY-LIST', 'the one-copy bank: every pair of the census item with its copy and its standing readers listed',
     lambda S: onecopy_ok(S), lambda S: _mut(S, 'onecopy', lambda d: d['pairs'].pop())),
    ('G-GEN-RUN', 'the diff bank: every row through the record tool`s reader, every changed cell listed, the files the table commit`s, one tag line per kernel',
     lambda S: gen_run_ok(S), lambda S: _mut(S, 'dj', lambda d: d['tables'][0]['rows'][0].update(reading='X'))),
    ('G-GEN-IDENTICAL-RERUN', 'the generator run live, dry, over the written tables: 0 cells in 0 files; the H1 bank the same (H1)',
     lambda S: gen_rerun_ok(S), lambda S: put(S, 'gendry', dict(S['gendry'], out='CELLS CHANGED 1 ; FILES CHANGED 1'))),
    ('G-ROWS-KEPT', 'the rows-kept bank: no row gained or lost in any written file, no changed line outside its table, every cell in the diff bank (N3)',
     lambda S: rows_kept_ok(S), lambda S: put(S, 'rowsk', S['rowsk'].replace('-- HELD.**', '-- REFUTED.**'))),
    ('G-READING-II-AFTER', 'the after bank: the change of method declared, 0 behind at the leading clause, the rest by carried prose, the like-for-like line',
     lambda S: after_ok(S), lambda S: _mut(S, 'af', lambda d: d['h2'].update(kernel_cell=1))),
    ('G-STATE-LINE', 'data/b670_state.txt before and now: its prefix intact, H5`s dated line appended with both figures',
     lambda S: state_line_ok(S), lambda S: put(S, 'shared_appended', {K.SHARED_APPENDED[0]: (b'x', b'y')})),
    ('G-ORDERS-ENTERED', 'OPEN_TRAILS at the record-lines banks` lines: the five orders and W-ORD-PROSE-PINS, each with its trigger, by conv',
     lambda S: orders_ok(S), lambda S: _rl(S, 1, 1, 'rl3')),
    ('G-B651-LINE', 'SIMPLICITY`s v1.1.3 before and now: appended only, b651`s line verbatim from the unversioned copy (N4)',
     lambda S: b651_ok(S), lambda S: put(S, 'b651', (S['b651'][0], S['b651'][0], S['b651'][2]))),
    ('G-NOTHING-MOVED', 'PLACE-papers: no archive/superseded, every unversioned copy present and at HEAD, no git mv in the command bank',
     lambda S: nothing_moved_ok(S), lambda S: put(S, 'superseded', True)),
    ('G-HYPOTHESES-SCORED', 'the hypotheses bank: H1-H5 each through the record tool`s reader, the verdict line printed', lambda S: hyp_ok(S),
     lambda S: _mut(S, 'hypj', lambda d: d.pop('H5', None))),
    ('G-OPEN-BRANCH-KEPT', 'SIDE-explicit-formula: chi-li-b669 local and remote-tracking at b804bf2, not an ancestor of main (N1)',
     lambda S: open_kept_ok(S), lambda S: put(S, 'open_on_main', True)),
    ('G-SPEC-PLANTED', 'tools/b672_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('generator row' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b672 tool`s code and the generator`s: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b672_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b672_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-explicit-formula`s main: the workflow file on main (put where absent by 7317db4, the file alone), no author identifier, no secret, the hold, the cache, the print step reading print_targets.txt of 5 names',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'the last merged run`s row (b669`s) through the record tool`s reader: the run id and ref of the worklist, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'the last merged run`s gate reading: build exit 0, no error line, the 5 prints, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbank', S['rbank'].replace('GATE DERIVES', 'GATE NOT DERIVES'))),
    ('G-MERGES-ON-GATE', 'SIDE-explicit-formula`s main: the merge commit of the built tip, the merged tree the built tree, its tag v0.31 peeled to it',
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS, OPEN_TRAILS, the files the generator wrote and b651`s line`s file (declared)',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the registry, the map, the census, the monograph, the pages, the surround: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal', lambda S: kernels_untouched(S),
     lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b671`s and the earlier tools, b667`s certify and map, rowgen`s, the mirror`s, the instruments and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 64158393 but the shared additive files and H5`s dated line, by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b671_stepzero.txt'])),
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
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b672 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b672_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b671`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b671 — lane two, act ninety-eight' in S['ot']
     and S['rootsf'].count(NL + 'b671 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b671 — lane two', '### b671 - lane two'))),
    ('G-R282-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R282) END' in S['ferry'] and S['ot'].count('**(R282) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R282) ratified', '**(R2820) ratified'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 49th line, the root bank and its items, H5`s shared bank among them', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b673 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b672 AGREE, b672 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b672 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b672_record.py agree', 'b672_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b673', lambda S: '**Next:** b673' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b673', '**Next:** b674'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 64158393 and d6d2d4b, the generator`s tables among them, against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b672')" in S['suite'] and "'data/b672_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b672_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the generator, the run, reading (ii), the hypotheses',
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
    p = os.path.join(D, 'b672_seal_hashes.json')
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
    print('  written: b672_seal_hashes.json')
    return 0


def _out_name(pushed):
    if PRERUN:
        return 'b672_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b672_checks_postpush.txt' if pushed else 'b672_checks.txt'


def main():
    if SEAL:
        return seal()
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b672 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    if tuple(K.B671_ACT_ARMS) != tuple(K671.ACT_ARMS):
        rec('### ### **b671`S ACT ARMS IN THE WORKLIST DIFFER FROM tools/b671_worklist.py`S -- THE FREEZE CANNOT BE READ.**')
    S = sources()
    S['pushed'] = pushed
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID) else regenerate()
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names)) and tuple(K.B671_ACT_ARMS) == tuple(K671.ACT_ARMS)
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b671`s face less its own arms) %d ; carried here %d ; the act`s arms over its own banks %s ; '
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
    gm = re.search(r'CELLS CHANGED (\d+) ; FILES CHANGED (\d+)', S['gendry']['out'])
    rec('  ### THE GENERATOR: the diff bank`s cells %s ; the table commit PLACE-papers %s, %d files ; the live dry re-run: cells %s, files %s ; '
        'hypotheses %s' % ((S['dj'].get('counts') or {}).get('CELLS CHANGED'), S['table_commit'], len(S['table_files']),
                           gm.group(1) if gm else '?', gm.group(2) if gm else '?', dict((k, v[0]) for k, v in S['hypj'].items())))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the ledgers, the generator`s, b651`s line`s): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    rec('  ### THE OPEN BRANCH %s: local %s ; remote-tracking %s ; on main %s' % (K.OPEN_BRANCH, S['open_local'][:8], S['open_remote'][:8], S['open_on_main']))
    for k, m in S['merges'].items():
        rec('  ### THE LAST MERGE %s : main %s ; parents %s ; built %s ; the merged tree the built tree %s ; tags at main %s' % (
            k, m['main'], m['parents'], m['built'], m['tree_main'] == m['tree_built'], m['tags']))
    lv = S['live']
    rec('  ### THE THREE ARMS AT HEAD (seconds %s):' % ', '.join('%.0f' % x for x in lv['secs']))
    rec('  ###   G-NO-SORRY-MAIN read %d kernels` mains, pairs unequal %d; sorry in code %d: %s' % (
        len(lv['nsm']), sum(1 for r in lv['nsm'] if not r['equal']), len(nsm_hits(S)), '; '.join('%s %s:%d' % h for h in nsm_hits(S)) or 'none'))
    rec('  ###   G-AXIOM-CLAIM read %d claims: CONTRADICTED %d, UNVERIFIABLE %d, VERIFIED %d, UNBOUND %d, MENTION %d' % (
        sum(1 for r in lv['ac'] if r['verdict'] != 'OUT OF SCOPE'), ac_count(lv['ac'], 'CONTRADICTED'), ac_count(lv['ac'], 'UNVERIFIABLE'),
        ac_count(lv['ac'], 'VERIFIED'), ac_count(lv['ac'], 'UNBOUND'), ac_count(lv['ac'], 'MENTION')))
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
    out = os.path.join(D, _out_name(pushed))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b672_arms_prerun.txt', 'b672_lsr_prerun.json').replace('b672_checks', 'b672_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b672_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
