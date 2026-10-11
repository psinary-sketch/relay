# -*- coding: utf-8 -*-
"""b651_checks.py -- THE SUITE OF b651, UNDER (R261): THE RE-CUTS OPENED -- THE DATA AND PAGE ROWS, THE SEAM ROW, THE SIMPLICITY ROW; THE
AXIOM-CLAIM RESOLVER; THE CENSUS AT v0.8.1; THE RESTATED LINES; THE LARGEST KERNEL'S DOCSTRINGS; THE NAVIGATOR'S ROWS.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### The face is sealed AFTER Components 2-6; every commit whose subject opens `b651` and none of POST_SEAL's prefixes precedes the lock.
### ### G-ACTROOT-VERIFY reads the chain at commit (tools/act_root.py): b624 to b651 AGREE, b651's crlf count 0.
### ### The three arms of b649 (G-NO-SORRY-MAIN, G-AXIOM-CLAIM, G-MODULE-HEADER) run here LIVE at HEAD by their own tools, each beside its
### ### planted test; G-NO-SORRY-MAIN and G-AXIOM-CLAIM fail on findings declared on the face (the four restated lines; the four real
### ### contradictions after the resolver's repair).
### ### The harness is b568's to b649's (helpers, runner, seal), written by the Write tool from tools/b649_checks.py; the sources, predicates
### ### and arms are b651's.
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
import b651_worklist as K     # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b651_registration_2026-10-11.txt')
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = K.STEPZERO
EXPORT = K.EXPORT
GEN_COMMITS = {'chain_page.py': ('1e073ac3', 'test_glossary_supersede_b651.py'), 'axiom_claim.py': ('6bb2ed06', 'test_axiom_claim_b651.py'),
               'licensed_table.py': ('3b3f02c0', 'test_clusters_served_b651.py')}
GLOSSARY_COMMITS = ('5c644b0d', '1dd6e85e')         # ### relay: the supersession's data and the six entries, each data/glossary.txt alone
CHI_LIST = 'f789e31c'                                # ### relay: data/b651_nodes_chi.txt alone
PAGE_COMMITS = ('e9466ef', '18ffee6', '0cabd75', '4c88587')   # ### PLACE-papers: four page re-emissions, one page each
SEAM_PP, SIMPL_PP, CENSUS_PP, TRIGGER_PP = '1a7989d', 'ecbaa2a', 'afc46b6', '715b8c3'
DS_COMMITS = ('80a1f87', '45ef0d9')                  # ### SIDE-kernel: the two plain comments on docstrings-SIDE-kernel
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
# ### the instruments b651 does not edit, against relay 936766a8 (tools/chain_page.py, axiom_claim.py and licensed_table.py are edited by the act
# ### and read by G-GENERATORS-ALONE instead)
INST = ('b649_checks.py', 'b649_closing.py', 'b649_tests.py', 'b649_worklist.py', 'b649_reg_gate.py', 'b649_regspec.py', 'b649_record.py',
        'b648_record.py', 'b647_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py', 'test_licensed_table_b645.py', 'b628_record.py',
        'b643_record.py', 'b638_record.py', 'b633_record.py', 'b602_record.py', 'b641_record.py', 'b639_record.py', 'b616_record.py',
        'act_root.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py', 'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py',
        'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py', 'b616_claims.py', 'ferry_scan.py', 'edit_route.py',
        'test_edit_route_b646.py', 'e0_rule.py', 'build_watch.py', 'test_build_watch_b647.py', 'g_chain_page.py', 'test_chain_page_b596.py',
        'test_chain_page.py', 'test_g_chain_page.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py',
        'test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py')
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md', K.CEN8,
            'day1/A_Place_to_Stand_v5_18.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 'day1/Exhaustive_Enumeration.md', 'day1/Which_Structure_Confines.md',
            'day1/Spectral_Inertness.md', 'day1/Seven_Mechanism_Classes.md', 'day1/Third_Identity_Element.md', 'day1/Silence_of_Foundations.md',
            'day1/ONE_PAGE_PROOF.md')
TABLE_FILES = K.TABLE_FILES
PHRASE = '(b638 is this one)'
SENT1, SENT2 = 'NO OFF-LINE ZERO EXISTS.', 'Therefore: all nontrivial zeros on σ = 1/2.'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b651')
            and 'data/b651_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    """the act's command capture, read live: the seat's session from the ruling's delivery."""
    import b651_record as REC
    return REC.capture()


def run_test(name):
    r = subprocess.run([sys.executable, os.path.join(T, name)], capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return dict(rc=r.returncode, out=r.stdout or '')


def live_arms():
    """b649's three arms run at HEAD by their own tools; G-NO-SORRY-MAIN reads each kernel's remote through this run's one ls-remote."""
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


TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_glossary_supersede_b651.py', 'test_axiom_claim_b651.py',
         'test_clusters_served_b651.py')


def sources():
    import b651_record as REC
    import b616_record as R6
    import edit_route as ER
    import chain_page as CP
    import b641_record as R41
    import licensed_table as LT
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b651_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b651_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    S = dict(
        REC=REC, ER=ER, CP=CP, LT=LT, face=face, ferry=rd('b651_ferry.txt'), scan=rd('b651_ferry_scan.txt'), stepz=rd('b651_stepzero.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b651_author_answers.txt'), prerun=rd('b651_arms_prerun.txt'),
        rl=jl('b651_record_lines.json'), seam_line=jl('b651_seam_line.json'), inst_line=jl('b651_instrument_line.json'),
        tests=jl('b651_tests_stepzero.json'), testst=rd('b651_tests_stepzero.txt'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b651_seal_hashes.json'), sealnow=sealed_now(), peaks=jl('b651_build_peaks.json'), watch=jl('b651_build_watch.json'),
        cmds=capture_now(), planted={t: run_test(t) for t in TESTS},
        gen_files={h: files_of(ROOT, h) for h, _t in GEN_COMMITS.values()},
        gen_log={f: [l for l in gs(ROOT, 'log', '--format=%h', '--abbrev=8', PRE['relay'] + '..HEAD', '--', 'tools/' + f).split(NL) if l.strip()]
                 for f in GEN_COMMITS},
        glossary_files={h: files_of(ROOT, h) for h in GLOSSARY_COMMITS}, chi_files=files_of(ROOT, CHI_LIST),
        gl_entries=CP.glossary_entries(), gl_block=CP.glossary_block(),
        chi_list=rd('b651_nodes_chi.txt'), chi_prev=rd('b649_nodes_chi.txt'),
        pages={k: read_blob(PP, 'HEAD:' + p) for k, p in K.PNAME.items()}, census=read_blob(PP, 'HEAD:' + K.CEN81),
        page_files={h: files_of(PP, h) for h in PAGE_COMMITS}, pp_files={h: files_of(PP, h) for h in (SEAM_PP, SIMPL_PP, CENSUS_PP, TRIGGER_PP)},
        arms_c2=rd('b651_page_arms_c2.txt'), arms_c4=rd('b651_page_arms_c4.txt'), alike=rd('b651_glossary_alike.txt'),
        table=jl('terminal_table.json').get('rows') or [], lattice=jl('b651_lattice.json'),
        simpl_pre=cr0(blob(PP, PRE['pp'] + ':' + K.SIMPL)), simpl_now=cr0(raw(os.path.join(PP, *K.SIMPL.split('/')))),
        ac_after=jl('b651_axiom_claim_after.json'), ac_before=jl('b651_axiom_claim_before.json'), rerun=rd('b651_axiom_claim_rerun.txt'),
        rows_b651=rd('b651_axiom_claim_rows.txt'),
        clusters=jl('b651_clusters_served.json'), edition=jl('b651_edition.json'), census_scan=rd('b651_census_termscan.txt'),
        restated=rd('b651_restated.txt'), nsm_bank=jl('b651_no_sorry_main.json'),
        restate_branches={k: gs('D:/' + k, 'branch', '--list', b) for k, b in K.RESTATE.items()},
        sentences=jl('b651_table_SIDE-kernel_sentences.json'), ds_bank=rd('b651_docstrings_SIDE-kernel.txt'),
        ds_log=[l for l in gs('D:/' + K.DS_KERNEL, 'log', '--format=%h', 'main..' + K.DS_BRANCH).split(NL) if l.strip()],
        ds_files={h: files_of('D:/' + K.DS_KERNEL, h) for h in DS_COMMITS},
        ds_text=read_blob('D:/' + K.DS_KERNEL, K.DS_BRANCH + ':Kernel/PerpendicularCrossing.lean'),
        nav=rd('b651_navigator_rows.txt'), nav_bank=jl('b647_table_navigator_memory.json'),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b651_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b651_act_root.json'), arj0=jl('b650_act_root.json'), art=rd('b651_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b651_kernels_face.json').get('kernels') or {}),
        push_lists={r: gs(r, 'branch', '--list', 'push-b650*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b651_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b651_mustnotexist.txt')),
        fj=jl('b651_findings.json'), tj=jl('b651_trail.json'), sc=jl('b651_scores.json'), desk=rd('b651_desk_notes.txt'), tfj=jl('b651_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['live'] = live_arms()
    S['mains_now'] = dict((r['kernel'], r['main']) for r in S['live']['nsm'])
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
        if f.startswith(('b651_', 'audit_b651_')) and os.path.isfile(os.path.join(D, f)) and ('data/' + f) != EXPORT:
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + list(S['pages'].values()) + [S['census']]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    S['outside'] = [n for n in R41.OAI_NEEDLES if n in S['ledger_adds']]
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES or p in ('data/act_roots.txt', 'data/glossary.txt'):
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S['gl_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/glossary.txt'))
    S['gl_now'] = cr0(raw(os.path.join(D, 'glossary.txt')))
    S['bank_mtimes'] = {}
    for it in (S['arj'].get('items') or []):
        p = it.split()[0]
        if p.startswith('data/') and os.path.exists(os.path.join(ROOT, *p.split('/'))):
            S['bank_mtimes'][p] = os.path.getmtime(os.path.join(ROOT, *p.split('/')))
    import act_root as AR
    import additive_shared as ADD
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


def poss(t):
    import b566_record as R6
    return R6.Q.poss(t)


def rline(S, i, key='rl'):
    x = (S[key].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need, key='rl'):
    x = rline(S, i, key)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


def procs_ok(S):
    p = S['stepz']
    return 'NONE: no tail, lean, lake or python process is running' in p and '### orphans: NONE' in p and 'free memory' in p


STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    """every test file tracked before the act run at step zero with the lists in force, test_elab_reader_b634.py under the watchdog and
    RUN-BENEATH-HOLD: clean but test_chain_page.py (9), W-ORD-TESTS-WITH-THE-LISTS-IN-FORCE's case, and test_chain_page_b638.py (4)-(7)."""
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 2' % (len(names), len(names) - 1)) in S['testst'] \
        and re.search(r'^  test_elab_reader_b634\.py +### RUN-BENEATH-HOLD', S['testst'], re.M) is not None


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b651 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    none = '### NONE: no prompt has been put to the author in this act.' in a
    return bool(m) and int(m.group(1)) == len(heads) and all(x >= 2 for x in per) and len(res) == len(calls) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and (none == (len(heads) == 0))


def peaks_ok(S):
    rows = S['peaks'].get('rows') or []
    return bool(rows) and all(isinstance(r.get('tree_peak'), int) and isinstance(r.get('driver_peak'), int) and r.get('host_low') is not None
                              for r in rows)


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def planted_ok(S, t, n):
    p = S['planted'][t]
    return p['rc'] == 0 and ('%d of %d cases as wanted -- PASS' % (n, n)) in p['out']


# ================================================================== b649's ARMS, LIVE AT HEAD
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


def mains_unmoved(S):
    """every kernel's main now against the main Component 5's run of G-NO-SORRY-MAIN banked."""
    b = dict((r['kernel'], r['main']) for r in S['nsm_bank'].get('rows') or [])
    return bool(b) and sorted(b) == sorted(S['mains_now']) and all(S['mains_now'][k] == m for k, m in b.items())


# ================================================================== (R261)(3): THE FIRST ROWS
def generators_alone(S):
    """each generator edit of the act: its tool and its planted test, alone; every commit of the act touching the tool among them."""
    for f, (h, t) in GEN_COMMITS.items():
        if S['gen_log'][f] != [h] or S['gen_files'].get(h) != sorted(['tools/' + f, 'tools/' + t]):
            return False
    return True


def supersede_ok(S):
    names = [e[0] for e in S['gl_entries']]
    return all(PHRASE not in l for l in S['gl_block']) and names.count('bNNN') == 1 and names.count('HINGE') == 3 \
        and b'# SUPERSEDES ENTRY 65: bNNN' in (S['gl_now'] or b'') and all(v == ['data/glossary.txt'] for v in S['glossary_files'].values()) \
        and planted_ok(S, 'test_glossary_supersede_b651.py', 6)


def chi_ok(S):
    a, b = S['chi_list'].split(NL), S['chi_prev'].split(NL)
    body = a[4:]
    diff = [i for i, (x, y) in enumerate(zip(body, b)) if x != y]
    want = "reading the summed side as the Dedekind zeta's costs two premises, which at v0.26 sit on dedekind_rhs'"
    return len(body) == len(b) and len(diff) == 1 and body[diff[0]].startswith('# backmatter:') and want in body[diff[0]] \
        and S['chi_files'] == ['data/b651_nodes_chi.txt'] and want in S['pages'].get('chi', '') \
        and 'the two premises are what it costs' not in S['pages'].get('chi', '')


def seam_table(S):
    r = [x for x in S['table'] if x['name'] == 'rh_strip_imp_rh']
    return len(r) == 1 and r[0]['grade'] == 'DERIVES' and [c['line'] for c in r[0]['grade_cells']] == [S['seam_line'].get('lines', [{}])[0].get('line')]


def seam_lattice(S):
    r = [x for x in S['lattice'].get('rows') or [] if x['name'] == 'rh_strip_imp_rh']
    return len(r) == 1 and r[0]['grade'] == 'DERIVES' and len(S['lattice'].get('rows') or []) == 94


def seam_line(S):
    x = rline(S, 0, 'seam_line')
    o = oline(S, x.get('line'))
    return bool(x) and 'SUPERSEDES OPEN_TRAILS :10909 for `rh_strip_imp_rh`:' in o and '`rh_strip_imp_rh` DERIVES' in o \
        and S['pp_files'].get(SEAM_PP) == ['OPEN_TRAILS.md']


def simpl_ok(S):
    add = appended(S['simpl_pre'], S['simpl_now'])
    return bool(add) and add.count('*Appended 2026-10-11 by b651') == 1 and 'BACK MATTER, THE CEILING ON :355' in add \
        and S['pp_files'].get(SIMPL_PP) == [K.SIMPL]


def pages_alone(S):
    pf = S['page_files']
    return sorted(x for v in pf.values() for x in v) == sorted([K.PAGE, K.DIR_PAGE] * 2) and all(len(v) == 1 for v in pf.values())


def page_arms_ok(S):
    return all('PAGE ARMS PASSING : 2 of 2.' in x and 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA PASSING : 2 of 2.' in x and 'b651_nodes_chi.txt' in x
               for x in (S['arms_c2'], S['arms_c4']))


def glossary_alike(S):
    blk = NL.join(S['gl_block'])
    return all(t.count(blk) == 1 for t in list(S['pages'].values()) + [S['census']]) and 'BYTE FOR BYTE THE SAME IN ALL THREE: True' in S['alike']


# ================================================================== (R261)(4): THE RESOLVER
def _row(rows, f, ln):
    x = [r for r in rows if r['file'] == f and r['line'] == ln and r['verdict'] not in ('MENTION', 'OUT OF SCOPE')]
    return x[0] if x else {}


REAL4 = (('SIDECosmo/SteaneExemplar.lean', 6), ('Kernel/Integration.lean', 215), ('MetaKernel.lean', 3), ('AxiomCheck.lean', 8))


def resolver_rows(S):
    rows = S['live']['ac']
    r2, r5 = _row(rows, 'Interfaces/LocalLimit.lean', 226), _row(rows, 'MetaKernel.lean', 140)
    real = [_row(rows, f, ln) for f, ln in REAL4]
    return r2.get('verdict') == 'VERIFIED' and r2.get('bound_to') == 'TraceSilence' and r5.get('verdict') == 'UNBOUND' \
        and all(x.get('verdict') == 'CONTRADICTED' for x in real) and ac_count(rows, 'CONTRADICTED') == 4 \
        and 'ROWS 6 ; MATCHES 1 ; OVERREACHES 4 ; UNBOUND 1' in S['rows_b651'] and 'CONTRADICTED 6 -> 4' in S['rerun']


def counts_banked(S):
    a = S['ac_after'].get('rows') or []
    return bool(a) and all(ac_count(a, v) == ac_count(S['live']['ac'], v) for v in ('CONTRADICTED', 'UNVERIFIABLE', 'VERIFIED', 'UNBOUND')) \
        and ac_count(S['ac_before'].get('rows') or [], 'CONTRADICTED') == 6


def trigger_line(S):
    x = rline(S, 0, 'inst_line')
    return bool(x) and 'ITS TRIGGER FIRED; THE VERDICT NOT ADDED THIS ACT' in oline(S, x.get('line')) and S['pp_files'].get(TRIGGER_PP) == ['OPEN_TRAILS.md']


# ================================================================== (R261)(5): THE CENSUS AT v0.8.1
def clusters_ok(S):
    rows = S['clusters'].get('rows') or []
    return len(rows) == 22 and all(isinstance(r['served'], list) for r in rows) and planted_ok(S, 'test_clusters_served_b651.py', 5)


def census_ok(S):
    e = S['edition']
    c = S['census'].encode('utf-8')
    return bool(c) and e.get('sha256') == hashlib.sha256(c).hexdigest() and e.get('path') == K.CEN81 and 'VERDICT          : CLEAN' in S['census_scan'] \
        and S['pp_files'].get(CENSUS_PP) == [K.CEN81] and '## Back matter of the v0.8.1 edition' in S['census'] \
        and S['census'].count('| served: none |') == sum(1 for r in S['clusters'].get('rows') or [] if not r['served'])


def entries_ok(S):
    names = [e[0] for e in S['gl_entries']]
    return all(n in names for n in ('the seat', 'sorry quarantine', 'MATCHES, UNDERSTATES, OVERREACHES, UNLICENSED', 'maturity, of a companion',
                                    'maturity, of a kernel', 'HINGE, its three entries')) and len(names) == 89


# ================================================================== (R261)(6), (7), (8)
def restated_ok(S):
    return 'RESTATED LINES MERGED 0 OF 4' in S['restated'] and all(v.strip() for v in S['restate_branches'].values()) \
        and sum(len(r['hits']) for r in S['nsm_bank'].get('rows') or []) == 4


def sentences_ok(S):
    rows = S['sentences'].get('rows') or []
    return len(rows) > 116 and len(set(r['parent'] for r in rows)) == 116 and all(r.get('parent_line') for r in rows)


def ds_branch_ok(S):
    t = S['ds_text']
    return sorted(S['ds_log']) == sorted(DS_COMMITS) and all(S['ds_files'].get(h) == ['Kernel/PerpendicularCrossing.lean'] for h in DS_COMMITS) \
        and bool(t) and SENT1 not in t and SENT2 not in t


def ds_deferred(S):
    rows = [r for r in S['watch'].get('rows') or [] if r.get('module') == 'Kernel.PerpendicularCrossing']
    return len(rows) == 1 and len(rows[0].get('lows') or []) == 2 and all(x < K.HOLD for x in rows[0]['lows']) and 'DEFERRED, UNMERGED' in S['ds_bank'] \
        and K.DS_BRANCH not in gs('D:/' + K.DS_KERNEL, 'branch', '--merged', 'main')


def nav_ok(S):
    want = [r for r in S['nav_bank'].get('rows') or [] if r.get('verdict') in ('OVERREACHES', 'UNDERSTATES')]
    return len(want) == 39 and len(re.findall(r'^### ROW \d+ ', S['nav'], re.M)) == 39 \
        and all((' '.join(r['action'].split()) in S['nav']) for r in want)


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


POST_SEAL = ('b651 seal', 'b651 pre-root', 'b651 root', 'b651 record', 'b651 --', 'b651 closing')


def _component_commit(s):
    return s.startswith('b651') and not s.startswith(POST_SEAL)


def sealed_after_ok(S):
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def table_final_ok(S):
    t = S['tfj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('added') and not t.get('grade_moved') and not t.get('moved')


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 28 and rows[27][:3] == ['b651', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b652_' in it] \
        and any(it.startswith('data/b651_no_sorry_main.txt ') for it in j.get('items') or []) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b651_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b651') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 652)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The first rows**', '**The resolver**', '**The census at v0.8.1**', '**The restated lines**', '**The docstrings**',
                 '**The navigator’s rows**', '**The record lines**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens',
                 '**Next.**', 'b652')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == poss(S['fj'].get('title') or '\x00') and all(x in tail for x in ENTRY_NEEDLES)


def trail_tail(S):
    t = S['ot']
    i = t.find(poss(S['REC'].TRAIL_HEAD()))
    return t[i:] if i >= 0 else ''


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


def publish_uncalled(S):
    pub = ['actions' + '/pub' + 'lish', 'z_' + 'publish']
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if any(p in t for p in pub)]


def kernels_untouched(S):
    import b641_record as R41
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and sorted(f) == sorted(R41.KERNS_READ) and all(k in n and n[k] == f[k] for k in f)


def corpus_scope(S):
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE, K.CEN81, K.SIMPL])


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and 'THE NAVIGATOR`S ROWS, PRINTED VERBATIM' in t and 'THE PRICES' in t and 'THE AXIOM-CLAIM RESOLVER' in t


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


def _plant_ac(d):
    for r in d['ac']:
        if r['file'] == 'Interfaces/LocalLimit.lean' and r['line'] == 226 and r['verdict'] not in ('MENTION', 'OUT OF SCOPE'):
            r['verdict'] = 'CONTRADICTED'


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R261) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: none running, no orphan, free memory read', lambda S: procs_ok(S),
     lambda S: put(S, 'stepz', S['stepz'].replace('### orphans: NONE', '### orphans: 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act: every one run but test_elab_reader_b634.py beneath the hold, '
     'clean but test_chain_page.py (9) and test_chain_page_b638.py (4)-(7)', lambda S: tests_ok(S),
     lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b650_pp_push_out.txt', 'data/b650_relay_push_out.txt']
     and S['pushout'][1], lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay and PLACE-papers branch lists and the step-zero bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['stepz'].count('push-b650* now 0') == 2, lambda S: put(S, 'push_lists', {'D:/relay': 'push-b650'})),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompts, every call`s result', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS', 'THE ANSWERS'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b651_record.py")])),
    ('G-PEAKS-BANKED', 'the peaks bank: every attempt`s driver peak, tree peak and host low', lambda S: peaks_ok(S),
     lambda S: put(S, 'peaks', {'rows': []})),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line', lambda S: landed(S, 0, ['b650', 'AT ITS WEIGHT']), lambda S: _rl(S, 0, 1)),
    ('G-DELIVERY-LINE', 'OPEN_TRAILS at the record-lines bank`s line', lambda S: landed(S, 1, ['THE NAVIGATOR PASTES; THE SEAT FILES']),
     lambda S: _rl(S, 1, 1)),
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
    ('G-MAINS-UNMOVED', 'every kernel`s main now against the main Component 5`s run banked', lambda S: mains_unmoved(S),
     lambda S: put(S, 'mains_now', dict(S['mains_now'], **{'SIDE-kernel': '0' * 40}))),
    ('G-GENERATORS-ALONE', 'the act`s commits touching tools/chain_page.py, axiom_claim.py and licensed_table.py: each the tool and its planted test alone',
     lambda S: generators_alone(S), lambda S: put(S, 'gen_files', dict(S['gen_files'], **{'1e073ac3': ['tools/chain_page.py', 'x']}))),
    ('G-GLOSSARY-SUPERSEDE', 'the glossary and its block: entry 65 out by its marked line, its superseding entry once, the three HINGE entries kept, '
     'each data commit the glossary alone, the planted test 6 of 6', lambda S: supersede_ok(S),
     lambda S: put(S, 'gl_block', S['gl_block'] + ['- **bNNN** — x %s' % PHRASE])),
    ('G-CHI-BACKMATTER', 'b651`s chi list against b649`s: the backmatter line alone re-cut, committed alone; the chi page carrying it',
     lambda S: chi_ok(S), lambda S: put(S, 'pages', dict(S['pages'], chi=S['pages'].get('chi', '') + ' the two premises are what it costs'))),
    ('G-SEAM-TABLE', 'the terminal table`s seam row: DERIVES, its one cell the correction`s line', lambda S: seam_table(S),
     lambda S: put(S, 'table', [dict(r, grade='CONFLICT') if r['name'] == 'rh_strip_imp_rh' else r for r in S['table']])),
    ('G-SEAM-LATTICE', 'the lattice bank`s seam row: DERIVES, 94 rows', lambda S: seam_lattice(S),
     lambda S: _mut(S, 'lattice', lambda d: [r.update(grade='CONFLICT') for r in d['rows'] if r['name'] == 'rh_strip_imp_rh'])),
    ('G-SEAM-LINE', 'OPEN_TRAILS at the seam bank`s line: the supersession directive and the one cell; its commit OPEN_TRAILS alone', lambda S: seam_line(S),
     lambda S: _rl(S, 0, 1, key='seam_line')),
    ('G-SIMPLICITY-LINE', 'the simplicity file before and now: one dated back-matter line appended, nothing above it changed, its commit the file alone',
     lambda S: simpl_ok(S), lambda S: put(S, 'simpl_now', b'x' + (S['simpl_now'] or b''))),
    ('G-PAGES-ALONE', 'the four page re-emissions in PLACE-papers, one page each', lambda S: pages_alone(S),
     lambda S: put(S, 'page_files', dict(S['page_files'], **{PAGE_COMMITS[0]: [K.PAGE, 'x']}))),
    ('G-PAGE-ARMS', 'the page arms and the frozen control after each re-emission, 2 of 2 each', lambda S: page_arms_ok(S),
     lambda S: put(S, 'arms_c4', S['arms_c4'].replace('PASSING : 2 of 2.', 'PASSING : 1 of 2.'))),
    ('G-GLOSSARY-ALIKE', 'the generator`s glossary block in both pages and the census at v0.8.1, byte for byte', lambda S: glossary_alike(S),
     lambda S: put(S, 'census', '')),
    ('G-RESOLVER-ROWS', 'G-AXIOM-CLAIM at HEAD on b649`s rows 2 and 5 and the four real contradictions; the successor rows bank and the rerun bank',
     lambda S: resolver_rows(S), lambda S: _live(S, _plant_ac)),
    ('G-RESOLVER-PLANTED', 'tools/test_axiom_claim_b651.py run: 7 of 7', lambda S: planted_ok(S, 'test_axiom_claim_b651.py', 7),
     lambda S: _planted(S, 'test_axiom_claim_b651.py')),
    ('G-RESOLVER-COUNTS', 'the after bank`s verdict counts against the live run; the before bank`s six', lambda S: counts_banked(S),
     lambda S: _mut(S, 'ac_after', lambda d: next(r for r in d['rows'] if r['verdict'] == 'CONTRADICTED').update(verdict='VERIFIED'))),
    ('G-TRIGGER-LINE', 'OPEN_TRAILS at the trigger line`s bank: W-ORD-VERDICT-INSTRUMENT`s trigger fired, the verdict not added', lambda S: trigger_line(S),
     lambda S: _rl(S, 0, 1, key='inst_line')),
    ('G-CLUSTERS-SERVED', 'the clusters bank over the 22 kernels; the planted test 5 of 5', lambda S: clusters_ok(S),
     lambda S: _planted(S, 'test_clusters_served_b651.py')),
    ('G-CENSUS-081', 'the census at v0.8.1 at PLACE-papers HEAD against its edition bank, its scan CLEAN, its commit the file alone, its served-by-none rows',
     lambda S: census_ok(S), lambda S: put(S, 'census', S['census'] + 'x')),
    ('G-GLOSSARY-ENTRIES', 'the glossary`s six entries for the second reader, 89 entries in all', lambda S: entries_ok(S),
     lambda S: put(S, 'gl_entries', [e for e in S['gl_entries'] if e[0] != 'the seat'])),
    ('G-RESTATED-PRICE', 'the restated bank: none merged, the branches standing, G-NO-SORRY-MAIN`s four hits banked', lambda S: restated_ok(S),
     lambda S: put(S, 'restated', S['restated'].replace('MERGED 0 OF 4', 'MERGED 2 OF 4'))),
    ('G-SENTENCE-ROWS', 'the sentence bank: 116 parent blocks, every row carrying its parent`s bank line', lambda S: sentences_ok(S),
     lambda S: _mut(S, 'sentences', lambda d: d['rows'][0].update(parent_line=None))),
    ('G-DS-BRANCH', 'docstrings-SIDE-kernel: its two commits, each PerpendicularCrossing.lean alone, neither sentence in the file at the branch',
     lambda S: ds_branch_ok(S), lambda S: put(S, 'ds_text', S['ds_text'] + SENT1)),
    ('G-DS-DEFERRED', 'the watchdog bank for Kernel.PerpendicularCrossing: two lows beneath the hold; the branch unmerged; the bank`s deferral',
     lambda S: ds_deferred(S), lambda S: put(S, 'ds_bank', '')),
    ('G-NAVIGATOR-ROWS', 'the navigator`s rows bank against b647`s table: 39 rows, every ACTION printed verbatim', lambda S: nav_ok(S),
     lambda S: put(S, 'nav', '')),
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS, OPEN_TRAILS, the two pages, the census at v0.8.1 and the simplicity file',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the registry, the map, the censuses before v0.8.1, the monograph, the companions, v1.1.3: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal', lambda S: kernels_untouched(S),
     lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b649`s tools, the earlier record tools, the instruments and the shared tools the act does not edit: before, working tree '
     'and HEAD', lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files, and the glossary before and now', lambda S: bool(S['additive'])
     and all(rc == [] for _p, _h, rc in S['additive']) and S['gl_pre'] is not None and (S['gl_now'] or b'').startswith(S['gl_pre']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 936766a8 but the shared additive files, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 0,
     lambda S: put(S, 'prior_bad', ['data/b650_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes, the pages and the census among them',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b651 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b651_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b650`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b650 — lane three, act seventy-seven' in S['ot']
     and S['rootsf'].count(NL + 'b650 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b650 — lane three', '### b650 - lane three'))),
    ('G-R261-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R261) END' in S['ferry'] and S['ot'].count('**(R261) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R261) ratified', '**(R2610) ratified'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 28th line, the root bank and its items', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b652 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b651 AGREE, b651 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line', lambda S: bool(S['tj'].get('line')) and oline(S, S['tj']['line']) == poss(S['REC'].TRAIL_HEAD()),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b651 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b651_record.py agree', 'b651_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b652', lambda S: '**Next:** b652, the author' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b652, the author', '**Next:** b653, the author'))),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 936766a8, b650`s push-out banks among them, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b651')" in S['suite'] and "'data/b651_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b651_closing.py: the closing sentence in the rule`s words with the plain reads named; the navigator`s rows; the prices; the resolver',
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
    """### (R246)(3): the sha256 of every sealed tool, recorded at the seal; refuses before the face is locked or once recorded."""
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b651_seal_hashes.json')
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
        print('  %-24s %s' % (t, now[t]))
    print('  written: b651_seal_hashes.json')
    return 0


def main():
    if SEAL:
        return seal()
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b651 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    av = S['ar_verify']
    rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    rec('  ### G-EDIT-ROUTE read %d captured commands; offences %d' % (len(S['cmds']), len(S['ER'].scan(S['cmds']))))
    lv = S['live']
    rec('  ### THE THREE ARMS AT HEAD (seconds %s):' % ', '.join('%.0f' % x for x in lv['secs']))
    rec('  ###   G-NO-SORRY-MAIN read %d kernels` mains, pairs unequal %d; sorry in code %d: %s' % (
        len(lv['nsm']), sum(1 for r in lv['nsm'] if not r['equal']), len(nsm_hits(S)), '; '.join('%s %s:%d' % h for h in nsm_hits(S)) or 'none'))
    rec('  ###   G-AXIOM-CLAIM read %d claims: CONTRADICTED %d, UNVERIFIABLE %d, VERIFIED %d, UNBOUND %d, MENTION %d; the banked prints %s' % (
        sum(1 for r in lv['ac'] if r['verdict'] != 'OUT OF SCOPE'), ac_count(lv['ac'], 'CONTRADICTED'), ac_count(lv['ac'], 'UNVERIFIABLE'),
        ac_count(lv['ac'], 'VERIFIED'), ac_count(lv['ac'], 'UNBOUND'), ac_count(lv['ac'], 'MENTION'), lv['ac_counts']))
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
        out = os.path.join(D, 'b651_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b651_checks_postpush.txt' if pushed else 'b651_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b651_arms_prerun.txt', 'b651_lsr_prerun.json').replace('b651_checks', 'b651_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b651_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
