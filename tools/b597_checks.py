# -*- coding: utf-8 -*-
"""b597_checks.py -- THE SUITE OF b597, UNDER (R207): CP-7 ACT SEVENTEEN, THE EDITION OF SIMPLICITY_OF_RIEMANN_ZEROS FROM ITS
TIER BLOCK, WORK-LIST AND THE b596 ADDENDUM; THE CONTROL ARM FROZEN AT ITS PIN.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b597_checks.txt before the push and
### data/b597_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b597_arms_prerun.txt and nothing else.
### ### The harness is b568's to b596's, carried; the arms are b597's. The control arm is the frozen one of (R207)(2), read through
### the test file's control() (relay tools/test_chain_page_b596.py, repaired at 276a7698).
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
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b597_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
ED = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'
PRE = dict(relay='a7843913', pp='a40f2b2', gs='3528bcf')
PRE_HEADS = {'SIDE-explicit-formula': '5a1630b8', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b'}
STEPZERO = '50a76ee8'
REPAIR = '276a7698'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/a5f76775-e614-41b6-b3eb-b08a5db7ea8f/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b597')
            and 'data/b597_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b597_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b597_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b597_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b597_ferry.txt'), scan=rd('b597_ferry_scan.txt'), cens=rd('b597_census_stepzero.txt'),
        fcens=rd('b597_faces_census_stepzero.txt'), pins0=rd('b597_pins_stepzero.txt'), procs=rd('b597_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b596_closing.txt'), reads=rd('b597_reads.txt'), branches=rd('b597_branches.txt'), answers=rd('b597_author_answers.txt'),
        prerun=rd('b597_arms_prerun.txt'), test0=rd('b597_test_chain_page_stepzero.txt'), ctl0=rd('b597_control_stepzero.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        repair=(files_of(ROOT, REPAIR), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', REPAIR, 'HEAD']).returncode == 0,
                gs(ROOT, 'log', '-1', '--pretty=%s', REPAIR)),
        gen_same=(cr0(blob(ROOT, PRE['relay'] + ':tools/chain_page.py')), cr0(raw(os.path.join(T, 'chain_page.py'))), cr0(blob(ROOT, 'HEAD:tools/chain_page.py'))),
        suite596=(cr0(blob(ROOT, PRE['relay'] + ':tools/b596_checks.py')), cr0(raw(os.path.join(T, 'b596_checks.py')))),
        testsrc=read(os.path.join(T, 'test_chain_page_b596.py')),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        cur=(cr0(raw(os.path.join(PP, CUR))), cr0(blob(PP, PRE['pp'] + ':' + CUR)), cr0(blob(PP, 'HEAD:' + CUR))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b596*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b597_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b597_mustnotexist.txt')), table_changed=None,
        fj=jl('b597_findings.json'), tj=jl('b597_trail.json'), sc=jl('b597_scores.json'), desk=rd('b597_desk_notes.txt'),
        wl1=jl('b597_weight_line.json'), rl=jl('b597_rule_lines.json'),
        PZ=jl('b597_page_zeta.json'), PX=jl('b597_page_chi.json'), E=jl('b597_edition.json'), H=jl('b597_h28.json'),
        bank=rd('b597_edition_SIMPLICITY.txt'), termscan=rd('b597_edition_termscan.txt'), repin=rd('b597_repin.txt'),
        arms_c2=rd('b597_page_arms_c2.txt'),
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
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b596_nodes_faces.txt'), os.path.join(SP, '_b597_gcp'), os.path.join(D, 'b596_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b596_nodes_chi.txt'), os.path.join(SP, '_b597_gcp'), os.path.join(D, 'b596_chi_probe_out.txt'))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    X['ed_raw'] = raw(os.path.join(PP, *ED.split('/')))
    X['ed_head'] = cr0(blob(PP, 'HEAD:' + ED))
    X['ed'] = cr0(X['ed_head']).decode('utf-8', 'replace').split(NL) if X['ed_head'] else []
    if X['ed'] and X['ed'][-1] == '':
        X['ed'] = X['ed'][:-1]
    r = subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', os.path.join(PP, *ED.split('/'))], capture_output=True, text=True,
                       encoding='utf-8', errors='replace') if X['ed_raw'] else None
    X['scan_now'] = r.stdout if r else ''
    return X


# ### the act's own predicates
def _edl(S, n):
    return S['REC']._edl(n)


def BM_TAG(S):
    return S['REC'].BM_TAG


def ed_cur_unedited(S):
    a, b, c = S['cur']
    return bool(b) and a == b == c


def ed_carries(S):
    ed, cur = S['ed'], lines_of(S['cur'][1])
    if cur and cur[-1] == '':
        cur = cur[:-1]
    changed = set(x[0] for x in S['REC']._all_changes())
    if not ed or BM_TAG(S) not in ed:
        return False
    return all(ed[_edl(S, n) - 1] == cur[n - 1] for n in range(1, len(cur) + 1) if n not in changed) \
        and all(ed[_edl(S, n) - 1] != cur[n - 1] for n in changed) and S['E'].get('sha256') == hashlib.sha256(S['ed_head']).hexdigest()


def worklist_rows(S):
    import b558_record as CP
    ed = S['ed']
    if not ed:
        return False
    rows = [r for r in json.load(io.open(os.path.join(D, 'b558_cp1b.json'), encoding='utf-8'))['rows'] if r['doc'] == 'SIMP' and r['verdict'] == 'MOVED-IN-MEANING']
    cur = lines_of(S['cur'][1])
    want = {26: ('`h2_sign_iff_rh`', '`5c72cad`', '`li_nonneg_iff_rh`', '`e5a5a83`', 'the ζ page’s last paragraph'),
            405: (r'`∀ s : ℤ, (1 : ℚ) ^ s = 1`', 'relay `data/b558_cp1b.txt` :166'),
            447: (r'`∀ s : ℤ, (1 : ℚ) ^ s = 1`', 'DEFINITIONAL', 'relay `data/b558_cp1b.txt` :169'),
            453: ('`mellin_Phi_eq_zero_of_re_le_one`', 'v0.17 = `5a1630b`', '`h2_sign_iff_rh`', '`5c72cad`')}
    ok = len(rows) == 5 and sorted(set(r['line'] for r in rows)) == [26, 405, 447, 453]
    for r in rows:
        sg = [x for x in CP.segments(cur[r['line'] - 1]) if x]
        k = sg.index(r['sentence'])
        nw = [x for x in CP.segments(ed[_edl(S, r['line']) - 1]) if x][k]
        ok = ok and nw != r['sentence'] and all(w in nw for w in want[r['line']])
    return ok and 'only h2 open' not in ed[_edl(S, 453) - 1]


def addendum_ok(S):
    ed, REC = S['ed'], S['REC']
    if not ed:
        return False
    rew = all(rep in ed[_edl(S, ln) - 1] and old not in ed[_edl(S, ln) - 1] for ln, old, rep, _a in REC.ADDENDUM)
    l24 = ed[_edl(S, 24) - 1]
    hist = all(x in REC.H505 for x in ('`simplicity`', '`simplicity_iff`', '`5a1630b`')) and \
        all(x in REC.H509 for x in ('`h_at_one`', 'allSimple_not_forced', 'relay `data/b596_faces_line.txt`'))
    return rew and hist and '40.77%' not in l24 and '`SimpleProportion`' in l24 and '`Zeta23.thmB₀_mult`' in l24 and 'not as a compiled fact' in l24 \
        and len(REC.ADDENDUM) == 3 and 'The only solution is multiplicity 1.' not in ed[_edl(S, 178) - 1]


def title_clause(S):
    ed = S['ed']
    if not ed:
        return False
    t = ed[_edl(S, 36) - 1]
    return t.startswith('# Chapter 1 — The Reduction: RH $\\iff$ Off-Line Non-Intersection') and '`simplicity_iff`' in t and 'v0.17 = `5a1630b`' in t \
        and 'No Compiled Edge to `h2_sign`' in t and 'relay `data/b596_h29b.txt`' in t and not t.rstrip().endswith('Simplicity')


def ceilings_ok(S):
    ed, REC = S['ed'], S['REC']
    if not ed:
        return False
    for ln, old, rep, why in REC.CEILS:
        l = ed[_edl(S, ln) - 1]
        if rep not in l or l.count(old) > rep.count(old):
            return False
        if '(R207)(6)' in why and ('simplicity' in why or 'title' in why) and 'relay `data/b596_h29b.txt`' not in rep:
            return False
    return len(REC.CEILS) == S['H'].get('n_ceils') == len(S['E'].get('diff', []) and [d for d in S['E']['diff'] if d['kind'] == 'ceiling'])


def facts_ok(S):
    ed, REC = S['ed'], S['REC']
    if not ed:
        return False
    return all(rep in ed[_edl(S, ln) - 1] and old not in ed[_edl(S, ln) - 1] for ln, old, rep, _w in REC.FACTS) \
        and all('`01e5633`' in ed[_edl(S, n) - 1] for n in (436, 437, 438)) and '`bfd2af7`' in ed[_edl(S, 457) - 1]


def restate_ok(S):
    ed, REC = S['ed'], S['REC']
    return bool(ed) and all(rep in ed[_edl(S, ln) - 1] for ln, old, rep, _w in REC.RESTATE) and len(REC.RESTATE) == 2


def collisions(S):
    ed, REC = S['ed'], S['REC']
    if not ed or BM_TAG(S) not in ed:
        return False
    bm = NL.join(ed[ed.index(BM_TAG(S)):])
    try:
        sec = bm[bm.index('### Collisions resolved by the precedence order'):bm.index('### Credit lines')]
    except ValueError:
        return False
    rows = [l for l in sec.split(NL) if re.match(r'^\| :\d+ \| ', l)]
    return len(rows) == len(REC.COLLISIONS) == len(S['E'].get('collisions', [])) and all(('| :%d |' % _edl(S, c[0])) in sec for c in REC.COLLISIONS)


def history_lines(S):
    ed, REC, E = S['ed'], S['REC'], S['E']
    if not ed or len(REC.HIST) != 3:
        return False
    at = E.get('hist_at', {})
    return all(ed[at[str(a)] - 1] == t and ed[at[str(a)] - 2] == '' for a, t, _w, _y in REC.HIST) and at.get('427') == _edl(S, 427) + 2 \
        and at.get('505') == _edl(S, 522) + 2 and at.get('509') == _edl(S, 522) + 4


def credit_lines(S):
    ed, REC, E = S['ed'], S['REC'], S['E']
    at = E.get('cred_at', [])
    return bool(ed) and len(at) == 2 and at == [_edl(S, 457) + 2, _edl(S, 457) + 4] and ed[at[0] - 1] == REC.CR1 and ed[at[1] - 1] == REC.CR2 \
        and 'SIGN_ARRANGEMENT_RECONCILIATION.md` :46, :66' in REC.CR2 and 'W_inf NOT sign-definite' in REC.CR1


def version_line(S):
    ed, REC = S['ed'], S['REC']
    n = _edl(S, 17)
    return bool(ed) and ed[n - 3] == REC.VERSION and ed[n - 2] == '' and ed[n - 1] == '*v1.1.2 — 2026-07-19*' and n == 19


def backmatter(S):
    ed = S['ed']
    if not ed or BM_TAG(S) not in ed:
        return False
    bm = NL.join(ed[ed.index(BM_TAG(S)):])
    heads = ['### Removals', '### Rewrites -- the work-list and the addendum', '### Ceiling corrections', '### Fact corrections', '### Restatement rewrites',
             '### Collisions resolved by the precedence order', '### Credit lines', '### History lines', '### Stem corrections',
             '### Ceiling-shaped sentences read and carried', '### Sentences read and left, for the author’s strike', '### Field context',
             '### The ruling’s readings of `(R207)`(6)', '### Placement', '### Correspondence']
    pos = [bm.find(h) for h in heads]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and (':%d, carried-by-history' % _edl(S, 427)) in bm and S['E'].get('status_blanks') == []


def h28a_ok(S):
    wl = [d for d in S['E'].get('diff', []) if d['kind'] == 'work-list']
    want = 'HELD' if len(wl) == 5 and all(d['changed'] and d['cites'] for d in wl) else 'REFUTED'
    return S['H'].get('H28a') == want and S['sc'].get('H28a', [''])[0] == want and '(H28A)' in S['desk']


def h28b_ok(S):
    import b558_record as CP
    ed = S['ed']
    if not ed:
        return False
    body = ed[:ed.index(BM_TAG(S))]
    while body and body[-1] == '':
        body = body[:-1]
    cur = lines_of(S['cur'][1])
    nb = sum(len([s for s in CP.segments(l) if s]) for l in body)
    nc = sum(len([s for s in CP.segments(l) if s]) for l in cur)
    E = S['E']
    allowed = E.get('credit', 0) + E.get('removals', 0) + E.get('ruled_citations', 0) + E.get('version_lines', 0)
    want = 'HELD' if abs(nb - nc) <= allowed else 'REFUTED'
    return nb == E.get('n_body') and nc == E.get('n_cur') and S['H'].get('H28b') == want and S['sc'].get('H28b', [''])[0] == want


def h28c_ok(S):
    REC = S['REC']
    ed = S['ed']
    if not ed:
        return False
    cut = ed.index(BM_TAG(S))
    ok_lines = set(_edl(S, n) for n in REC.CARRIED) | set(_edl(S, x[0]) for x in REC._all_changes()) | set(S['E'].get('hist_at', {}).values())
    beyond = [i for i, l in enumerate(ed[:cut], 1) for m in REC.CEILING.finditer(l) if i not in ok_lines]
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['scan_now'], re.M) is not None and re.search(r'live uses\s*:\s*0\b', S['scan_now']) is not None
    want = 'HELD' if clean and not beyond else 'REFUTED'
    return S['H'].get('H28c') == want and S['sc'].get('H28c', [''])[0] == want and S['scan_now'].strip() == S['termscan'].strip()


def ed_bank(S):
    b = S['bank']
    return b.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3): ' + S['REC'].OFFSET) and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in b \
        and ('sha256 %s' % S['E'].get('sha256', '#')) in b and 'BACK MATTER %d, printed separately' % S['E'].get('n_backmatter', -1) in b


def repin_ok(S):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', S['repin'])
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > 40 and S['E'].get('sha256', '#') in S['bank']


def pages_alone(S):
    log = S['pp_log']
    want = sorted(p['page'] for p in (S['PZ'], S['PX']) if p.get('changed'))
    pg = [h for h, s_ in log if S['pp_files'][h] in ([PAGE], [DIR_PAGE])]
    edc = [h for h, s_ in log if S['pp_files'][h] == [ED]]
    if len(edc) != 1 or len(pg) != len(want) or not want:
        return False
    idx = {h: i for i, (h, s_) in enumerate(log)}
    return all(idx[h] > idx[edc[0]] for h in pg) and all(s_.startswith('b597 housekeeping -- the ') for h, s_ in log if h in pg) \
        and sorted(S['pp_files'][h][0] for h in pg) == want


def pages_c2_ok(S):
    ch = [p for p in (S['PZ'], S['PX']) if p.get('changed')]
    if not S['PZ'] or not S['PX'] or not ch:
        return False
    for p in ch:
        d = [x for x in p['diff'] if x.startswith(('+', '-')) and not x.startswith(('+++', '---'))]
        if not d or not all(x[1:].startswith('| keystone naming a node |') for x in d) or not any(('`%s`' % ED) in x for x in d if x.startswith('+')):
            return False
    return True


def rule_lines_ok(S):
    ls = S['rl'].get('lines', [])
    if len(ls) != 3:
        return False
    a, b, c = (oline(S, x['line']) for x in ls)
    t = S['ot']
    i = t.find(ls[1]['head'])
    wo = t[i:i + 1600] if i >= 0 else ''
    return a.startswith(ls[0]['head']) and '(:12264)' in ls[0]['head'] and 'one page per call in the foreground' in a and 'not an OOM' in a \
        and b == ls[1]['head'] and 'W-ORD-VENDOR-FINALMULT' in b and '**Items.**' in wo and '**Price:**' in wo and '**Trigger:** the author’s word' in wo \
        and 'thmB₀_mult' in wo and 'SimpleProportion' in wo and c.startswith(ls[2]['head']) and '(:12266)' in ls[2]['head'] \
        and 'FINITE, UNIVERSAL, LIMIT, DENSITY, FAMILY' in c and ls[0]['line'] < ls[1]['line'] < ls[2]['line']


def answers_banked(S):
    a = S['answers']
    return a.count('### PROMPT ') == 1 and a.count('\n  OPTION ') == 3 and a.count('[RECOMMENDED]') == 1 and a.count('\nRESULT ') == 1 \
        and a.count('### CALL tool-use id ') == 1 and '="option 2. All relay reads at 12c15c80' in a


def control_repair(S):
    files, anc, subj = S['repair']
    a, b, c = S['gen_same']
    return files == ['tools/test_chain_page_b596.py'] and anc and subj.startswith('b597 step zero (R207)(2)') and bool(a) and a == b == c \
        and "RELAY_PIN = '12c15c80'" in S['testsrc'] and "PRE_PP = 'ba5f0ea'" in S['testsrc'] and ("ARM = '%s'" % CONTROL_ARM) in S['testsrc']


def control_counted(S):
    t = S['test0']
    cases = [l for l in t.split(NL) if re.match(r'^\s+\(\d\) ', l)]
    return all(('(%d)' % i) in t for i in range(1, 6)) and len(cases) == 5 and all(l.rstrip().endswith(' PASS') for l in cases) \
        and '### ALL PASS' in t and 'exit 0' in t \
        and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['ctl0'] and S['lock_epoch'] is not None \
        and os.path.getmtime(os.path.join(D, 'b597_test_chain_page_stepzero.txt')) < S['lock_epoch']


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


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 16]) if e else ''
    return bool(e) and fline(S, e) == S['REC'].TITLE and '**The edition**' in tail and '**Read in mutual light**' in tail and ED in tail \
        and ('sha256 `%s`' % S['E'].get('sha256', '#')) in tail and 'FINDINGS :5778' in tail and 'strengthens' in tail and CONTROL_ARM in tail


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R207) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and '### ORPHANS:' in S['procs'] and '\\v1.0\\' in S['procs']
     and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut|python)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '\n  1234   5678 grep.exe  grep x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero and repair commits and every later commit', lambda S: S['lock_epoch'] is not None
     and all(any(l.startswith(c) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock']) for c in (STEPZERO, REPAIR))
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith((STEPZERO, REPAIR))), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b596`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b596' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [REPAIR, STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b597 -- x'])),
    ('G-R207-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R207) END' in S['ferry'] and S['ot'].count('**(R207) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R207) ratified', '(R207) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'data/b596_simplicity_reading.txt @', 'data/b596_lemmas.txt @', 'data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt @', CUR + ' @ a40f2b2',
        PAGE + ' @ a40f2b2', 'tools/chain_page.py @', 'tools/test_chain_page_b596.py @', 'tools/b596_checks.py @', 'OPEN_TRAILS.md @ a40f2b2',
        'data/b596_closing_push_out.txt @', 'data/b596_closing_push_out_attempt1.txt @', '### b450`s items for SIMPLICITY_OF_RIEMANN_ZEROS',
        'none derives RH or h2_sign from it', 'Kernel/PerpendicularCrossing.lean @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: one prompt, question, options and recommended mark verbatim, the result', lambda S: answers_banked(S),
     lambda S: put(S, 'answers', S['answers'].replace('[RECOMMENDED]', '', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 50a76ee8`s files', lambda S: S['pushout'][0] == ['data/b596_closing_push_out.txt', 'data/b596_closing_push_out_attempt1.txt']
     and S['pushout'][1], lambda S: put(S, 'pushout', (['data/b596_closing_push_out.txt'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b596') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b596'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'simplicity-b596': '0000000'}))),
    ('G-CONTROL-REPAIR-ALONE', 'relay 276a7698`s files and subject, the generator against a7843913, the test`s pins and arm name', lambda S: control_repair(S),
     lambda S: put(S, 'repair', (['tools/test_chain_page_b596.py', 'tools/chain_page.py'], True, S['repair'][2]))),
    ('G-CONTROL-TEST-COUNTED', 'the step-zero test run and the arm`s step-zero count, banked before the lock', lambda S: control_counted(S),
     lambda S: put(S, 'test0', S['test0'].replace('### ALL PASS', '### NOT ALL PASS'))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-B596-SUITE-UNEDITED', 'b596`s sealed suite on disk against a7843913', lambda S: bool(S['suite596'][0]) and S['suite596'][0] == S['suite596'][1],
     lambda S: put(S, 'suite596', (S['suite596'][0], S['suite596'][1] + b'x'))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wl1'].get('line')).startswith(S['wl1'].get('head', '#'))
     and '(:6856)' in fline(S, S['wl1']['line']) and 'b596 AT ITS WEIGHT' in fline(S, S['wl1']['line']) and 'v0.17 = 5a1630b' in fline(S, S['wl1']['line'])
     and 'H29a REFUTED' in fline(S, S['wl1']['line']), lambda S: put(S, 'wl1', dict(S['wl1'], line=1))),
    ('G-RULE-LINES', 'OPEN_TRAILS at the standing line, the work-order and the DENSITY line', lambda S: rule_lines_ok(S),
     lambda S: put(S, 'rl', dict(S['rl'], lines=S['rl'].get('lines', [])[:2]))),
    ('G-CURRENT-UNEDITED', 'SIMPLICITY_OF_RIEMANN_ZEROS.md on disk and at HEAD against a40f2b2', lambda S: ed_cur_unedited(S),
     lambda S: put(S, 'cur', (S['cur'][0] + b'x', S['cur'][1], S['cur'][2]))),
    ('G-EDITION-CARRIES', 'the edition at HEAD: every v1.1.2 line at its offset, unchanged unless changed by the form', lambda S: ed_carries(S),
     lambda S: put(S, 'ed', [x.replace('Davenport-Heilbronn', 'Davenport–Heilbronn') for x in S['ed']])),
    ('G-WORKLIST-ROWS', 'the five MOVED rows re-read at their segments, rewritten to their compiled facts with pins or bank lines', lambda S: worklist_rows(S),
     lambda S: put(S, 'ed', [x.replace('relay `data/b558_cp1b.txt` :169', 'relay `data/b558_cp1b.txt` :170') for x in S['ed']])),
    ('G-ADDENDUM-SENTENCES', 'the three addendum rewrites in place and the two history lines` citations', lambda S: addendum_ok(S),
     lambda S: put(S, 'ed', [x.replace('not as a compiled fact', 'as a fact') for x in S['ed']])),
    ('G-TITLE-CLAUSE', 'Chapter 1`s title in the edition: simplicity_iff at v0.17, no compiled edge to h2_sign, the walk', lambda S: title_clause(S),
     lambda S: put(S, 'ed', [x.replace('No Compiled Edge to `h2_sign`', 'a Compiled Edge to `h2_sign`') for x in S['ed']])),
    ('G-CEILING-CORRECTIONS', 'every ceiling correction in place, the old wording gone, each join citing the walk', lambda S: ceilings_ok(S),
     lambda S: put(S, 'ed', [x.replace('a sufficiency no compiled statement carries', 'sufficient') for x in S['ed']])),
    ('G-FACT-CORRECTIONS', 'the branch pin and the SIDE-grh-transfer pin corrected', lambda S: facts_ok(S),
     lambda S: put(S, 'ed', [x.replace('`bfd2af7`', '`858cbf6`') for x in S['ed']])),
    ('G-RESTATEMENTS', 'the two restatement rewrites', lambda S: restate_ok(S),
     lambda S: put(S, 'ed', [x.replace('an equivalence this row’s terminal does not state', 'x') for x in S['ed']])),
    ('G-COLLISIONS', 'the back matter`s collision rows against the tool`s list and the edition json', lambda S: collisions(S),
     lambda S: put(S, 'ed', [x for x in S['ed'] if not x.startswith('| :%d | the stem clause and the history clause' % S['REC']._edl(427))])),
    ('G-HISTORY-LINES', 'the three history lines beneath their dated entries', lambda S: history_lines(S),
     lambda S: put(S, 'ed', [x for x in S['ed'] if 'rests on that premise, not on the compiled identity.*' not in x])),
    ('G-CREDIT-LINES', 'the two b450 credit lines beneath the Correspondence footnote', lambda S: credit_lines(S),
     lambda S: put(S, 'E', dict(S['E'], cred_at=S['E'].get('cred_at', [])[:1]))),
    ('G-VERSION-LINE', 'the v1.1.3 line above the v1.1.2 line', lambda S: version_line(S),
     lambda S: put(S, 'ed', [x.replace('*v1.1.3 — 2026-10-02*', '*v1.1.3*') for x in S['ed']])),
    ('G-BACKMATTER', 'the back matter`s sections in order, the carried-by-history row, no blank Status cell', lambda S: backmatter(S),
     lambda S: put(S, 'ed', [x.replace('### Placement', '### Placings') for x in S['ed']])),
    ('G-EDITION-BANK', 'the diff bank`s offset head, its counts and its landing line', lambda S: ed_bank(S), lambda S: put(S, 'bank', S['bank'][5:])),
    ('G-REPIN', 'the re-pin bank against the final file', lambda S: repin_ok(S), lambda S: put(S, 'repin', S['repin'].replace('RE-PIN : ', 'RE-PIN : 9', 1))),
    ('G-H28A-SCORED', 'the work-list rows` citations, the scores, the desk', lambda S: h28a_ok(S), lambda S: put(S, 'H', dict(S['H'], H28a='REFUTED'))),
    ('G-H28B-SCORED', 'the body and the current version counted afresh', lambda S: h28b_ok(S), lambda S: put(S, 'E', dict(S['E'], n_body=1))),
    ('G-H28C-SCORED', 'the scanner run afresh on the edition and the ceiling read afresh', lambda S: h28c_ok(S),
     lambda S: put(S, 'scan_now', S['scan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since a40f2b2: each changed page committed alone after the edition commit',
     lambda S: pages_alone(S), lambda S: put(S, 'pp_files', {h: ([PAGE, DIR_PAGE] if f in ([PAGE], [DIR_PAGE]) else f) for h, f in S['pp_files'].items()})),
    ('G-PAGES-C2', 'the post-edition re-emits: only Placement rows change, the edition among them', lambda S: pages_c2_ok(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], diff=S['PZ'].get('diff', []) + ['+| node | x |']))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b596`s faces list and v0.17 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b596`s χ list and v0.17 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the post-edition commits: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat under the precedence order, for the author’s strike' in trail(S)
     and 'Recorded as the navigator’s' in trail(S) and 'ac8257a5' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Recorded as the navigator’s', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b598, one CP-1b act over SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b598, one CP-1b act over SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-explicit-formula': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b597_record.py'): S['tooltext'].get(os.path.join(T, 'b597_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == [ED],
     lambda S: put(S, 'keystone_changes', [ED, CUR])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at a7843913, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b596_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p['page'] for p in (S['PZ'], S['PX']) if p.get('changed')]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + [CUR]))),
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
                                                                          and "startswith('b597')" in S['suite'] and "data/b597_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b597')", ''))),
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
    rec('b597 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b597_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b597_checks_postpush.txt' if pushed else 'b597_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b597_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
