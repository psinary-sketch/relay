# -*- coding: utf-8 -*-
"""b596_checks.py -- THE SUITE OF b596, UNDER (R206): W-ORD-SIMPLICITY-FACE -- THE PROPORTION OF SIMPLE ZEROS WALKED IN THE
VENDORED SET, THE TITLE'S CLAUSE STATED AS A SALT-CHECKED PROP, THE FACES' SILENCE ON MULTIPLICITY ENTERED ON THE PAGE,
SIMPLICITY'S CLAIMS READ AGAINST THEM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b596_checks.txt before the push and
### data/b596_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b596_arms_prerun.txt and nothing else.
### ### The harness is b568's to b595's, carried; the arms are b596's.
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

NL = chr(10)
PP, GS, KER, TE = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula', 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b596_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
TREE_REL = 'modules/2026-10/DELIBERATION_TREE.md'
PRE = dict(relay='0cfe7354', pp='ba5f0ea', gs='3528bcf', te='da89d83', te_origin='29208f6', ker='c404e72')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72'}
KFILES = ['AxiomCheckSimplicity.lean', 'SIDEExplicitFormula/SaltCheckSimplicity.lean', 'SIDEExplicitFormula/Simplicity.lean']
NS = 'SIDEExplicitFormula.Simplicity.'
STEPZERO = '46248b4a'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/4d816814-ed14-4689-b5cb-96db62728606/scratchpad'


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
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
    return (b or b'').replace(b'\r\n', b'\n')


def raw(p):
    try:
        return open(p, 'rb').read()
    except OSError:
        return None


def blob_id(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def files_of(repo, sha_):
    return sorted(x for x in gs(repo, 'show', '--name-only', '--pretty=format:', sha_).split(NL) if x.strip())


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b596')
            and 'data/b596_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section)/[^`\s]+)`', w)))


def untracked(repo, *paths):
    return [l[3:].strip() for l in git(repo, 'status', '--porcelain', '--untracked-files=all', '--', *paths)[1].split(NL) if l.startswith('?? ')]


def written_files(lock_epoch):
    out = set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay']).split(NL) if x.strip())
    out |= set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay'], 'HEAD').split(NL) if x.strip())
    for p in untracked(ROOT, 'data', 'tools'):
        try:
            if os.path.getmtime(os.path.join(ROOT, p)) > lock_epoch - 3 * 3600:
                out.add(p)
        except OSError:
            pass
    res = ['relay/' + x for x in out]
    for repo, name, pre in ((PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        if repo == PP:
            ch |= set(untracked(PP, 'phase1.5', 'phase2'))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    return cr0(b).decode('utf-8', 'replace').split(NL)


def sources():
    import b596_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b596_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b596_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b596_ferry.txt'), scan=rd('b596_ferry_scan.txt'), cens=rd('b596_census_stepzero.txt'),
        fcens=rd('b596_faces_census_stepzero.txt'), pins0=rd('b596_pins_stepzero.txt'), procs=rd('b596_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b595_closing.txt'), reads=rd('b596_reads.txt'), branches=rd('b596_branches.txt'), answers=rd('b596_author_answers.txt'),
        prerun=rd('b596_arms_prerun.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        relay_log=[(l.split(' ', 2)[0], int(l.split(' ', 2)[1]), l.split(' ', 2)[2] if l.count(' ') >= 2 else '')
                   for l in gs(ROOT, 'log', '--reverse', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        simp=(cr0(raw(os.path.join(PP, SIMP))), cr0(blob(PP, PRE['pp'] + ':' + SIMP))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b595*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b596_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b596_mustnotexist.txt')), table_changed=None,
        fj=jl('b596_findings.json'), tj=jl('b596_trail.json'), sc=jl('b596_scores.json'), desk=rd('b596_desk_notes.txt'),
        wl1=jl('b596_weight_line.json'), rl=jl('b596_rule_lines.json'), hl=jl('b596_held_line.json'),
    )
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES:
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs'))
    S['pp_changed'] = sorted(ch)
    S['keystone_changes'] = sorted(x for x in ch if x.startswith('phase') or x.startswith('day1/') or x.startswith('outputs/'))
    S['pp_log'] = [(l.split(' ', 2)[0], int(l.split(' ', 2)[1]), l.split(' ', 2)[2] if l.count(' ') >= 2 else '')
                   for l in gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _t, _s in S['pp_log']}
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    REC = S['REC']
    X = {}
    zl = os.path.join(D, 'b596_nodes_faces.txt')
    X['gcp_zeta'] = GCP.arm(zl, os.path.join(SP, '_b596_gcp'), os.path.join(D, 'b596_probe_out.txt')) if os.path.exists(zl) else dict(ok=False, rc=-1)
    cl = os.path.join(D, 'b596_nodes_chi.txt')
    X['gcp_chi'] = GCP.arm(cl, os.path.join(SP, '_b596_gcp'), os.path.join(D, 'b596_chi_probe_out.txt')) if os.path.exists(cl) else dict(ok=False, rc=-1)
    X['gcp_ctl'] = [GCP.arm(os.path.join(D, n), os.path.join(SP, '_b596_gcp'), os.path.join(D, p), committed=blob(PP, '%s:%s' % (PRE['pp'], pg)))
                    for n, p, pg in (('b592_nodes.txt', 'b592_probe_out.txt', PAGE), ('b592_nodes_chi.txt', 'b592_chi_probe_out.txt', DIR_PAGE))]
    X['lem'], X['lem_txt'] = jl('b596_lemmas.json'), rd('b596_lemmas.txt')
    X['vend_now'] = sorted(x for x in gs(KER, 'ls-tree', '-r', '--name-only', PRE['ker'], 'Zeta23/').split(NL) if x.endswith('.lean'))
    X['vend_thm'] = gs(KER, 'grep', '-n', '-E', r'thmB₀_mult|thmB_mult|two_thirds_simple', PRE['ker'], '--', 'Zeta23/')
    X['up_line'] = (blob(REC.UP, '%s:Zeta23/FinalMult.lean' % REC.UPIN) or b'').decode('utf-8', 'replace').split(NL)
    X['tree'] = (raw(TE + '/' + TREE_REL), blob(TE, 'HEAD:' + TREE_REL), blob(TE, PRE['te'] + ':' + TREE_REL))
    X['tree_sent'] = read(os.path.join(SP, 'tree_sentence.txt')).strip()
    X['ts'] = jl('b596_tree_sentence.json')
    X['te_log'] = [(l.split(' ', 1)[0], files_of(TE, l.split(' ', 1)[0])) for l in gs(TE, 'log', '--reverse', '--pretty=%H %s', PRE['te'] + '..HEAD').split(NL) if l.strip()]
    X['te_origin'], X['te_head'] = gs(TE, 'rev-parse', 'origin/main'), gs(TE, 'rev-parse', 'HEAD')
    X['te_status'] = gs(TE, 'status', '--porcelain', '--untracked-files=no')
    X['st'] = {k: jl('b596_statements_%s.json' % k) for k in ('simp', 'salt')}
    X['e0'] = {k: jl('b596_e0_%s.json' % k) for k in ('simp', 'salt')}
    X['bld'] = {k: rd('b596_build_%s.txt' % k) for k in ('simplicity', 'saltchecksimplicity')}
    X['pr'] = jl('b596_prints.json')
    X['h29b'], X['h29b_txt'] = jl('b596_h29b.json'), rd('b596_h29b.txt')
    try:
        X['fed_now'] = REC.fed_walk()[0]
    except Exception:
        X['fed_now'] = None
    X['kmain'] = gs(KER, 'rev-parse', 'main')
    X['ktag'] = gs(KER, 'rev-parse', '--verify', '-q', 'v0.17^{commit}')
    X['kbranch'] = gs(KER, 'rev-parse', '--verify', '-q', 'refs/heads/simplicity-b596')
    X['kanc'] = subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', PRE['ker'], 'main']).returncode == 0
    X['kmerges'] = gs(KER, 'rev-list', '--merges', PRE['ker'] + '..main')
    X['kns'] = sorted(x for x in gs(KER, 'diff', '--name-status', PRE['ker'], 'main').split(NL) if x.strip())
    X['ksrc'] = {f: (blob(KER, 'main:' + f) or b'').decode('utf-8', 'replace') for f in KFILES}
    X['kpush'], X['bpush'] = rd('b596_kernel_push_out.txt'), rd('b596_branch_push_out.txt')
    X['gen_diff'] = gs(ROOT, 'diff', PRE['relay'], 'HEAD', '--', 'tools/chain_page.py')
    X['gen_now'] = (blob(ROOT, 'HEAD:tools/chain_page.py') or b'').decode('utf-8', 'replace')
    X['gen_test'] = subprocess.run([sys.executable, os.path.join(T, 'test_chain_page_b596.py')], capture_output=True, text=True,
                                   encoding='utf-8', errors='replace') if os.path.exists(os.path.join(T, 'test_chain_page_b596.py')) else None
    X['nodes'], X['nodes_chi'], X['nodes_faces'] = rd('b596_nodes.txt'), rd('b596_nodes_chi.txt'), rd('b596_nodes_faces.txt')
    X['p3'], X['p4'] = jl('b596_pages_c3.json'), jl('b596_pages_c4.json')
    X['pa3'], X['pa4'] = rd('b596_page_arms_c3.txt'), rd('b596_page_arms_c4.txt')
    X['page_head'] = cr0(blob(PP, 'HEAD:' + PAGE)).decode('utf-8', 'replace')
    X['fl'], X['fl_txt'] = jl('b596_faces_line.json'), rd('b596_faces_line.txt')
    X['rdg'], X['rdg_txt'] = jl('b596_simplicity_reading.json'), rd('b596_simplicity_reading.txt')
    return X


# ### the act's own predicates
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


def answers_banked(S):
    a = S['answers']
    return a.count('### PROMPT ') == 2 and a.count('\n  OPTION ') == 6 and a.count('[RECOMMENDED]') == 2 and a.count('\nRESULT ') == 1 \
        and a.count('### CALL tool-use id ') == 1 and '="option 1. The minimal generator edit' in a and '="option 1. The seat runs the face' in a


def rule_lines_ok(S):
    ls = S['rl'].get('lines', [])
    if len(ls) != 3:
        return False
    a, b, c = (oline(S, x['line']) for x in ls)
    return a.startswith(ls[0]['head']) and '(:12246)' in ls[0]['head'] and 'modules/2026-10/' in a and 'nets −1' in a \
        and b.startswith(ls[1]['head']) and 'five or more acts’ prompts' in b and 'scoring rule unchanged' in b \
        and c == ls[2]['head'] and 'W-ORD-QUANTIFIER-COLUMN' in c and ls[0]['line'] < ls[1]['line'] < ls[2]['line']


def workorder_ok(S):
    ls = S['rl'].get('lines', [])
    if len(ls) != 3:
        return False
    t = NL.join(S['ot'].split(NL)[ls[2]['line'] - 1:ls[2]['line'] + 5])
    return all(x in t for x in ('FINITE', 'UNIVERSAL', 'LIMIT', 'FAMILY', '**Price:**', '**Trigger:** the author’s word', '**Expected:**',
                                'the detector reads FAMILY', 'the ladder’s rungs read FINITE'))


def tree_ok(S):
    disk, head, pre = S['tree']
    if not (disk and head and pre and S['tree_sent']):
        return False
    a, b = lines_of(pre), lines_of(head)
    if len(a) != len(b):
        return False
    diff = [i for i in range(len(a)) if a[i] != b[i]]
    v = [i for i, l in enumerate(b) if l.startswith('## (v) ')]
    vi = [i for i, l in enumerate(b) if l.startswith('## (vi) ')]
    return len(diff) == 1 and len(v) == 1 and len(vi) == 1 and v[0] < diff[0] < vi[0] and b[diff[0]] == a[diff[0]].rstrip() + ' ' + S['tree_sent'] \
        and '(R206)' in S['tree_sent'] and cr0(disk) == cr0(head) and sha(S['tree_sent']) == S['ts'].get('sentence_sha256')


def tree_alone(S):
    return [f for _h, f in S['te_log']] == [[TREE_REL]] and S['te_status'] == ''


def walk_ok(S):
    W = S['lem']
    return bool(W) and W.get('modules') == S['vend_now'] and len(S['vend_now']) == 57 and S['vend_thm'] == '' \
        and W.get('upstream') == ['Zeta23/FinalMult.lean:350'] and len(S['up_line']) > 351 and S['up_line'][349].startswith('theorem thmB₀_mult') \
        and '(2 / 3 - ε) * (Ncount T (2 * T) : ℝ) ≤ N0simple T (2 * T)' in S['up_line'][350] and '### (1) THE VENDORED MODULE LIST -- 57 modules' in S['lem_txt']


def h29a_ok(S):
    want = 'HOLDS' if S['vend_thm'] else 'REFUTED'
    return S['lem'].get('H29a') == want and S['sc'].get('H29a', [''])[0] == want and ('### (7) H29a -- “the proportion is in the vendored set by name”: %s.' % want) in S['lem_txt']


def correction_ok(S):
    c = S['lem'].get('correction', '')
    return c.startswith('FACT CORRECTION TO THE WORK-ORDER (OPEN_TRAILS :12014, item (a))') and 'Zeta23.ThmB_statement' in c and 'at the bound 1/2' in c \
        and 'Zeta23/FinalMult.lean :350' in c and 'Alpöge–Furman' in c and '### (8) ' + c in S['lem_txt']


def stmts_ok(S):
    st = S['st']
    for k, rel in (('simp', 'SIDEExplicitFormula/Simplicity.lean'), ('salt', 'SIDEExplicitFormula/SaltCheckSimplicity.lean')):
        if st[k].get('file') != rel or not st[k].get('decls') or sha(S['ksrc'].get(rel, '').encode('utf-8')) != st[k].get('sha256'):
            return False
    names = [d['name'] for d in st['simp']['decls']]
    return names == ['allSimple', 'simplicity', 'simplicity_iff', 'SimpleProportion', 'exceptional_mass_le_third']


def built_ok(S):
    return all('### EXIT rc=0' in t and ('Built SIDEExplicitFormula.%s' % m) in t for t, m in
               ((S['bld']['simplicity'], 'Simplicity'), (S['bld']['saltchecksimplicity'], 'SaltCheckSimplicity')))


def prints_ok(S):
    pr = S['pr']
    ax = pr.get('axioms', {})
    want = [NS + n for n in ('allSimple', 'simplicity', 'simplicity_iff', 'SimpleProportion', 'exceptional_mass_le_third')] + \
        [NS + 'SaltCheck.' + n for n in ('allSimple_satisfiable', 'allSimple_not_forced')]
    return bool(ax) and all(w in ax for w in want) and pr.get('std3') is True and not pr.get('sorry') and pr.get('errors') == 0 \
        and 'rc=0' in (pr.get('exit') or '')


def no_sorry_src(S):
    pat = re.compile(r'\b(sorry|native_decide|admit)\b|^\s*axiom\s', re.M)
    return all(S['ksrc'].get(f) for f in KFILES) and not any(pat.search(re.sub(r'/-[\s\S]*?-/', '', t)) for t in S['ksrc'].values())


def e0_ok(S):
    r1, r2 = S['e0']['simp'].get('rows', {}), S['e0']['salt'].get('rows', {})
    return S['e0']['simp'].get('gate') is True and S['e0']['salt'].get('gate') is True and S['e0']['simp'].get('same_file') is True \
        and r1.get(NS + 'exceptional_mass_le_third', {}).get('grade') == 'INTERFACES' and r1.get(NS + 'simplicity_iff', {}).get('grade') == 'DERIVES' \
        and r1.get(NS + 'simplicity', {}).get('grade') == 'DEF' and r2.get(NS + 'SaltCheck.allSimple_not_forced', {}).get('grade') == 'DERIVES'


def salt_ok(S):
    H = S['h29b']
    return bool(H) and all(H.get('check', {}).get(n) for n in ('allSimple_satisfiable', 'allSimple_not_forced')) \
        and H.get('satisfiable', {}).get('std3') is True and H.get('not_forced', {}).get('std3') is True \
        and '¬SIDEExplicitFormula.Simplicity.allSimple' in H['check']['allSimple_not_forced'].replace(' ', '').replace('¬ ', '¬')


def fed_ok(S):
    H = S['h29b']
    now = S['fed_now']
    return now is not None and bool(H.get('rows')) and [(r['kernel'], r['file'], r['line'], r['cls']) for r in now] == \
        [(r['kernel'], r['file'], r['line'], r['cls']) for r in H['rows']] and all(r['reading'] for r in now if r['cls'] == 'READ') \
        and all(S['REC']._strict_controls().values())


def h29b_ok(S):
    H = S['h29b']
    bad = [r for r in (S['fed_now'] or [{}]) if r.get('cls') in ('CONCLUDES', 'NEGATES') or (r.get('cls') == 'READ' and not r.get('reading'))]
    want = 'HOLDS' if salt_ok(S) and prints_ok(S) and e0_ok(S) and S['fed_now'] is not None and not bad else 'REFUTED'
    return H.get('H29b') == want and S['sc'].get('H29b', [''])[0] == want and ('### ### **H29b %s.**' % want) in S['h29b_txt']


def merge_ok(S):
    return bool(S['ktag']) and S['ktag'] == S['kmain'] == S['kbranch'] and S['kanc'] and S['kmerges'] == '' and S['kmain'] != gs(KER, 'rev-parse', PRE['ker']) \
        and S['kns'] == sorted('A\t' + f for f in KFILES)


def tag_ok(S):
    m = S['kmain']
    k = S['kpush']
    return bool(m) and 0 <= k.find('main read back at the remote: ' + m) < k.find('push_gated: tag v0.17 made at the read-back') \
        and ('tag v0.17 peeled local %s remote %s' % (m, m)) in k


def branch_pushed(S):
    m = S['kmain']
    return bool(m) and ('simplicity-b596 local %s remote %s' % (m, m)) in S['bpush'] and 'push rc=0' in S['bpush']


def gen_edit_ok(S):
    d = S['gen_diff']
    added = [l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    gone = [l[1:] for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    return bool(added) and all(l.strip() == '' or l.strip().startswith('#') or re.search(r'backmatter|\bbm\b', l) for l in added) \
        and gone == [] and "'# backmatter: '" in S['gen_now'] \
        and S['gen_test'] is not None and S['gen_test'].returncode == 0 and 'ALL PASS' in S['gen_test'].stdout


def gen_alone_before(S):
    g = [(h, t) for h, t, s_ in S['relay_log'] if files_of(ROOT, h) == ['tools/chain_page.py', 'tools/test_chain_page_b596.py']]
    c4 = [t for h, t, s_ in S['pp_log'] if S['pp_files'][h] == [PAGE] and s_.startswith('b596 (R206)(4)(c)')]
    return len(g) == 1 and len(c4) == 1 and g[0][1] <= c4[0]


def pages_alone(S):
    log = S['pp_log']
    z3 = [h for h, t, s_ in log if S['pp_files'][h] == [PAGE] and s_.startswith('b596 (R206)(4)(b)')]
    c3 = [h for h, t, s_ in log if S['pp_files'][h] == [DIR_PAGE] and s_.startswith('b596 (R206)(4)(b)')]
    z4 = [h for h, t, s_ in log if S['pp_files'][h] == [PAGE] and s_.startswith('b596 (R206)(4)(c)')]
    pages = [h for h, t, s_ in log if PAGE in S['pp_files'][h] or DIR_PAGE in S['pp_files'][h]]
    return len(z3) == 1 and len(c3) == 1 and len(z4) == 1 and len(pages) == 3 and all(len(S['pp_files'][h]) == 1 for h in pages)


def new_nodes_ok(S):
    new = {x['name']: x for x in S['p3'].get('zeta', {}).get('new', [])}
    page = S['page_head']
    want = {NS + 'allSimple': 'DEF', NS + 'simplicity': 'DEF', NS + 'simplicity_iff': 'DERIVES', NS + 'SimpleProportion': 'DEF',
            NS + 'exceptional_mass_le_third': 'INTERFACES'}
    return len(new) == 5 and all(new.get(n, {}).get('grade') == gr for n, gr in want.items()) \
        and all(re.search(r'^\d+\. `%s` — SIDEExplicitFormula/(Simplicity)\.lean:\d+ — v0\.17 = %s — .* — E0: %s — ' % (re.escape(n), S['kmain'][:7], gr), page, re.M)
                for n, gr in want.items()) and S['nodes'].count('| kernel | added: (R206)(4)(b)') == 5 and '# pin: v0.17' in S['nodes'] \
        and '# pin: v0.17' in S['nodes_chi']


def faces_line_ok(S):
    fl = S['fl']
    line = fl.get('line', '')
    page = S['page_head']
    corr = page.find('\n## Correspondence\n')
    after = page[corr:] if corr >= 0 else ''
    return fl.get('ok') is True and bool(line) and page.count(line) == 1 and after.rstrip(NL).endswith(line) \
        and S['nodes_faces'].rstrip(NL).endswith('# backmatter: ' + line) and S['nodes_faces'].count('# backmatter: ') == 1 \
        and all(x in line for x in ('`h2_sign_iff_rh`', '`li_nonneg_iff_rh`', '`arith_limit_nonneg_iff_rh`', '5c72cad', 'e5a5a83'))


def reading_ok(S):
    R = S['rdg']
    doc = lines_of(S['simp'][1])
    rows = R.get('rows', [])
    return bool(rows) and R.get('all_found') is True and all(0 < r['line'] <= len(doc) and r['quote'] in doc[r['line'] - 1] for r in rows) \
        and all(r.get('cite') and r.get('mover') for r in rows) and 'THE TIER BLOCK, READ LINE BY LINE' in S['rdg_txt'] \
        and 'THE WORK-LIST, READ LINE BY LINE' in S['rdg_txt']


def h29c_ok(S):
    R = S['rdg']
    tb = R.get('tier_block', [0, 0])
    want = 'HOLDS' if any(tb[0] <= r['line'] <= tb[1] and '(a)' in r['mover'] for r in R.get('rows', [])) else 'REFUTED'
    return bool(R.get('rows')) and R.get('H29c') == want and S['sc'].get('H29c', [''])[0] == want and ('### ### **H29c %s**' % want) in S['rdg_txt']


def held_ok(S):
    hl = S['hl']
    want = 'THE HOLD LIFTED' if S['h29b'].get('H29b') == 'HOLDS' else 'THE HOLD KEPT'
    return bool(hl) and oline(S, hl.get('line')).startswith(hl.get('head', '#')) and '(:12026)' in hl['head'] and want in hl['head']


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 24]) if e else ''
    return bool(e) and fline(S, e) == S['REC'].TITLE and '**The walk**' in tail and '**The Prop**' in tail and '**The faces’ line**' in tail \
        and '**The reading**' in tail and '**Read in mutual light**' in tail and 'FINDINGS :5778' in tail and '`Zeta23/FinalMult.lean` :350' in tail


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE', 'HOLDS') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R206) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and '### ORPHANS:' in S['procs']
     and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '\n  1234   5678 grep.exe  grep x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b595`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b595' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b596 -- x'])),
    ('G-R206-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R206) END' in S['ferry'] and S['ot'].count('**(R206) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R206) ratified', '(R206) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'OPEN_TRAILS.md @ ba5f0ea', 'FINDINGS.md @ ba5f0ea', 'data/b572_lemmas.txt @', 'Zeta23/Statement.lean @ c404e727',
        'SIDEExplicitFormula/Schema/Config.lean @ c404e727', 'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean @ c404e727',
        'SIDEExplicitFormula/Seam.lean @ c404e727', PAGE + ' @ ba5f0ea', SIMP + ' @ ba5f0ea',
        'data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt @', 'tools/chain_page.py @', 'tools/push_gated.sh @',
        'data/b595_author_answers.txt @', 'data/b595_closing_push_out.txt @')) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: two prompts, question, options and recommended mark verbatim, the result', lambda S: answers_banked(S),
     lambda S: put(S, 'answers', S['answers'].replace('[RECOMMENDED]', '', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 46248b4a`s files', lambda S: S['pushout'][0] == ['data/b595_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b595') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b595'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'epstein-b590': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wl1'].get('line')).startswith(S['wl1'].get('head', '#'))
     and '(:6836)' in fline(S, S['wl1']['line']) and 'b595 AT ITS WEIGHT' in fline(S, S['wl1']['line']) and 'The suite read 70 of 70.' in fline(S, S['wl1']['line'])
     and 'H33d refuted in its letter on the table' in fline(S, S['wl1']['line']), lambda S: put(S, 'wl1', dict(S['wl1'], line=1))),
    ('G-ITEMS-AND-REFRESH-LINES', 'OPEN_TRAILS at the three banked lines: the seat`s items, the batch refresh, the work-order head', lambda S: rule_lines_ok(S),
     lambda S: put(S, 'rl', dict(S['rl'], lines=S['rl'].get('lines', [])[:2]))),
    ('G-QUANTIFIER-WORKORDER', 'OPEN_TRAILS beneath the work-order head: items, price, trigger, expectations', lambda S: workorder_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Trigger:** the author’s word. **Expected:**', '**Expected:**'))),
    ('G-TREE-SENTENCE', 'TECHNE-Core`s tree on disk, at HEAD and at da89d83: one line of section (v) extended by the sentence', lambda S: tree_ok(S),
     lambda S: put(S, 'tree_sent', S['tree_sent'] + 'x')),
    ('G-TREE-ALONE-NOT-PUSHED', 'TECHNE-Core`s log since da89d83, its status and its remote-tracking main', lambda S: tree_alone(S)
     and S['te_origin'].startswith(PRE['te_origin']) and S['te_head'] != S['te_origin'], lambda S: put(S, 'te_log', S['te_log'] + [('x', ['y'])])),
    ('G-WALK-BANK', 'the vendored tree at c404e72 listed and grepped afresh, the upstream module at its pin, against the bank', lambda S: walk_ok(S),
     lambda S: put(S, 'vend_now', S['vend_now'][1:])),
    ('G-H29A-SCORED', 'the vendored set grepped afresh for the proportion`s theorem names, the bank and the scores', lambda S: h29a_ok(S),
     lambda S: put(S, 'vend_thm', 'Zeta23/x.lean:1:theorem thmB₀_mult')),
    ('G-FACT-CORRECTION', 'the walk bank`s correction line', lambda S: correction_ok(S),
     lambda S: put(S, 'lem', dict(S['lem'], correction=S['lem'].get('correction', '').replace('at the bound 1/2', 'at the bound 2/3')))),
    ('G-KERNEL-STATEMENTS', 'the statements printed before the build against the files at the kernel`s main', lambda S: stmts_ok(S),
     lambda S: put(S, 'ksrc', dict(S['ksrc'], **{'SIDEExplicitFormula/Simplicity.lean': S['ksrc'].get('SIDEExplicitFormula/Simplicity.lean', '') + ' '}))),
    ('G-KERNEL-BUILT', 'the two build banks', lambda S: built_ok(S),
     lambda S: put(S, 'bld', dict(S['bld'], simplicity=S['bld']['simplicity'].replace('### EXIT rc=0', '### EXIT rc=1')))),
    ('G-AXIOMS-STD3', 'the prints bank: every declaration at the standard three, no sorryAx, no error', lambda S: prints_ok(S),
     lambda S: put(S, 'pr', dict(S['pr'], sorry=['x']))),
    ('G-NO-SORRY-SOURCE', 'the three kernel files at main, comments stripped', lambda S: no_sorry_src(S),
     lambda S: put(S, 'ksrc', dict(S['ksrc'], **{'AxiomCheckSimplicity.lean': S['ksrc'].get('AxiomCheckSimplicity.lean', '') + '\nsorry'}))),
    ('G-E0-GRADES', 'the E0 reads at the branch tip', lambda S: e0_ok(S),
     lambda S: put(S, 'e0', dict(S['e0'], simp=dict(S['e0']['simp'], rows=dict(S['e0']['simp'].get('rows', {}), **{NS + 'exceptional_mass_le_third': dict(grade='DERIVES')}))))),
    ('G-SALT-CHECK', 'the H29b bank`s two salt-check prints and rows', lambda S: salt_ok(S),
     lambda S: put(S, 'h29b', dict(S['h29b'], check=dict(S['h29b'].get('check', {}), allSimple_not_forced='')))),
    ('G-FEDERATION-WALK', 'every kernel`s HEAD walked afresh against the bank, the strict shapes exercised', lambda S: fed_ok(S),
     lambda S: put(S, 'fed_now', (S['fed_now'] or [])[1:])),
    ('G-H29B-SCORED', 'the salt-check, the prints, the grades and the fresh walk against the bank and the scores', lambda S: h29b_ok(S),
     lambda S: put(S, 'h29b', dict(S['h29b'], H29B='x', **{'H29b': 'REFUTED' if S['h29b'].get('H29b') == 'HOLDS' else 'HOLDS'}))),
    ('G-KERNEL-MERGE-ONLY', 'the kernel`s main, its tag, its branch and its ancestry from c404e72, by status', lambda S: merge_ok(S),
     lambda S: put(S, 'kns', S['kns'] + ['M\tSIDEExplicitFormula/Schema/Config.lean'])),
    ('G-TAG-BY-SCRIPT', 'the kernel push capture', lambda S: tag_ok(S), lambda S: put(S, 'kpush', S['kpush'].replace('tag v0.17 made', 'x'))),
    ('G-BRANCH-PUSHED', 'the branch push bank', lambda S: branch_pushed(S), lambda S: put(S, 'bpush', '')),
    ('G-GEN-EDIT', 'the generator`s diff since 0cfe7354 and its test run afresh', lambda S: gen_edit_ok(S),
     lambda S: put(S, 'gen_diff', S['gen_diff'] + '\n+    PIN_TAG = "v9"')),
    ('G-GEN-ALONE-BEFORE', 'relay`s log: the generator and its test committed alone before the ζ page`s faces commit', lambda S: gen_alone_before(S),
     lambda S: put(S, 'relay_log', [])),
    ('G-B592-LISTS-CONTROL', 'b592`s two lists re-emitted from their probes by the generator as it stands, against the pre-act page blobs',
     lambda S: all(x.get('ok') is True for x in S['gcp_ctl']), lambda S: put(S, 'gcp_ctl', [dict(ok=False)] + S['gcp_ctl'][1:])),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b596`s faces list and v0.17 probe against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b596`s χ list and v0.17 probe against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm banks after the tag and after the faces commit', lambda S: 'PAGE ARMS PASSING : 4 of 4' in S['pa3']
     and 'PAGE ARMS PASSING : 4 of 4' in S['pa4'], lambda S: put(S, 'pa3', S['pa3'].replace('PASSING : 4 of 4', 'PASSING : 3 of 4'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since ba5f0ea: the ζ page twice and the χ page once, each alone', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', {h: ([PAGE, DIR_PAGE] if f in ([PAGE], [DIR_PAGE]) else f) for h, f in S['pp_files'].items()})),
    ('G-NEW-NODES-ON-PAGE', 'the c3 pages bank, the node lists and the ζ page at HEAD: five rows, their grades, their entry tag', lambda S: new_nodes_ok(S),
     lambda S: put(S, 'nodes', S['nodes'].replace('| kernel | added: (R206)(4)(b)', '| kernel | listed', 1))),
    ('G-FACES-LINE', 'the faces` line bank, the faces list and the ζ page at HEAD: the line once, last, after the Correspondence table', lambda S: faces_line_ok(S),
     lambda S: put(S, 'fl', dict(S['fl'], line=S['fl'].get('line', '') + ' x'))),
    ('G-READING-BANK', 'the reading bank against SIMPLICITY at ba5f0ea, each quoted sentence on its cited line', lambda S: reading_ok(S),
     lambda S: put(S, 'rdg', dict(S['rdg'], rows=[dict(r, line=r['line'] + 1) for r in S['rdg'].get('rows', [])]))),
    ('G-H29C-SCORED', 'the reading`s rows counted afresh in the tier block, the bank and the scores', lambda S: h29c_ok(S),
     lambda S: put(S, 'rdg', dict(S['rdg'], H29c='HOLDS' if S['rdg'].get('H29c') == 'REFUTED' else 'REFUTED'))),
    ('G-HELD-MARK', 'OPEN_TRAILS at the banked HELD line, its word against H29b', lambda S: held_ok(S), lambda S: put(S, 'hl', dict(S['hl'], line=1))),
    ('G-SIMPLICITY-UNEDITED', 'SIMPLICITY`s current version on disk against ba5f0ea', lambda S: bool(S['simp'][1]) and S['simp'][0] == S['simp'][1],
     lambda S: put(S, 'simp', (S['simp'][0] + b'x', S['simp'][1]))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-ANSWERS-RECORDED', 'this act`s trail record', lambda S: '**Answered before the seal, by the author** (relay data/b596_author_answers.txt)' in trail(S)
     and '**Recorded as the navigator’s:**' in trail(S) and 'a `# backmatter:` record' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Recorded as the navigator’s:**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b597, SIMPLICITY_OF_RIEMANN_ZEROS’ edition by the form' in trail(S)
     and 'one CP-1b act over SILENCE_STAGES and REPARAMETERIZATION' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b597, SIMPLICITY_OF_RIEMANN_ZEROS’ edition by the form', 'x'))),
    ('G-OTHER-KERNELS-UNTOUCHED', 'every other kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-rcurve': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b596_record.py'): S['tooltext'].get(os.path.join(T, 'b596_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == [],
     lambda S: put(S, 'keystone_changes', [SIMP])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 0cfe7354, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b595_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE, DIR_PAGE]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b596')" in S['suite'] and "data/b596_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b596')", ''))),
]


def regenerate():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def main():
    import time
    pushed = RERUN or (not PRERUN and is_pushed())
    rec('=' * 104)
    rec('b596 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN:
        rec('### run at (UTC) : %s   ### the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
            % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN) else regenerate()
    if RERUN:
        S['table_changed'] = []
    elif not PRERUN:
        S['table_changed'] = [list(x) for x in (gen_diff.get('changed') or [])] if rc_gen == 0 and 'changed' in gen_diff else None
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-40s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
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
        rec('  %-40s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else 'FAIL', 'PASS' if posv else 'FAIL',
                                           'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else '### FAILS')))
    rec('')
    rec('  ### files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                  if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    if not (RERUN or PRERUN):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b596_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b596_checks_postpush.txt' if pushed else 'b596_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b596_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
