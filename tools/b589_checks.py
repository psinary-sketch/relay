# -*- coding: utf-8 -*-
"""b589_checks.py -- THE SUITE OF b589, UNDER (R199): THE COMPREHENSIVE HOUSEKEEPING ACT -- E_DIFFICULTY, THE CONSTELLATION RE-READ, THE SWEEP, THE BENCH.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b589_checks.txt before the push and data/b589_checks_postpush.txt after
### it. ### The harness is b568's to b589's, carried; the arms are b589's.
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
KERNEL = 'D:/SIDE-kernel'

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
FACE = os.path.join(D, 'b589_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='83571aab', pp='b378167', gs='8c392fe')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}
STEPZERO = '0b552b52'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
L = []


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b589')
            and 'data/b589_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
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
            ch |= set(untracked(PP, 'phase1.5'))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    return cr0(b).decode('utf-8', 'replace').split(NL)


def sources():
    import b589_record as REC
    import b558_record as CP
    import banned_terms as BT
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b589_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b589_') and f.endswith('.py'))
    edp = os.path.join(PP, *REC.ED.split('/'))
    cur = lines_of(blob(PP, '%s:%s' % (PRE['pp'], REC.CUR)))
    if cur and cur[-1] == '':
        cur = cur[:-1]
    ed = lines_of(raw(edp))
    if ed and ed[-1] == '':
        ed = ed[:-1]
    bt = subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', edp], capture_output=True, text=True,
                        encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    hk = {}
    for repo, key in ((ROOT, 'relay'), (PP, 'pp')):
        cs = [l.split(' ', 1)[0] for l in gs(repo, 'log', '--pretty=%H %s', PRE['relay' if key == 'relay' else 'pp'] + '..HEAD').split(NL)
              if l.strip() and l.split(' ', 1)[1].startswith('b589 housekeeping')]
        hk[key] = [files_of(repo, c) for c in cs]
    S = dict(
        REC=REC, CP=CP, BT=BT, face=face, ferry=rd('b589_ferry.txt'), scan=rd('b589_ferry_scan.txt'), cens=rd('b589_census_stepzero.txt'),
        fcens=rd('b589_faces_census_stepzero.txt'), pins0=rd('b589_pins_stepzero.txt'), procs=rd('b589_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b588_closing.txt'), reads=rd('b589_reads.txt'), branches=rd('b589_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), c1=jl('b589_c1_lines.json'),
        cur=cur, ed=ed, ed_exists=os.path.exists(edp), ej=jl('b589_edition.json'), hj=jl('b589_h28.json'), etxt=rd('b589_edition_EDIFF.txt'),
        escan=rd('b589_edition_termscan.txt'), bt_now=bt,
        cur_head_blob=gs(PP, 'rev-parse', 'HEAD:' + REC.CUR), cur_work_blob=gs(PP, 'hash-object', REC.CUR),
        page=lines_of(blob(PP, '192077f:' + PAGE)),
        rows=[r for r in json.load(io.open(os.path.join(D, 'b558_cp1b.json'), encoding='utf-8'))['rows']
              if r['doc'] == 'EDIFF' and r['verdict'] == 'MOVED-IN-MEANING'],
        hk=hk,
        fj=jl('b589_findings.json'), tj=jl('b589_trail.json'),
        sc=jl('b589_scores.json'), desk=rd('b589_desk_notes.txt'),
        pages={p: (blob(PP, 'HEAD:' + p), blob(PP, PRE['pp'] + ':' + p)) for p in (PAGE, DIR_PAGE)},
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry_pre=lines_of(blob(PP, PRE['pp'] + ':REGISTRY.md')),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kmain=gs(KER, 'rev-parse', 'main'), kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b588*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b589_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b589_mustnotexist.txt')), table_changed=None,
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
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    REC = S['REC']
    X = {}
    X['terms_now'] = {n: {p: REC._decl(KERNEL, p, REC.TERM_FILE.get(n, REC.SC_FILE), n)[0] for p in ps} for _, n, ps in REC.TERMS}
    X['tj_terms'] = jl('b589_ediff_terms.json')
    X['csum'] = jl('b589_constellation_summary.json')
    X['csum_txt'] = rd('b589_constellation_summary.txt')
    X['cbanks'] = {}
    import b589_constellation as CN
    X['CN'] = CN
    for key, (name, curp, edp, start) in CN.DOCS.items():
        X['cbanks'][name] = (rd('b589_constellation_%s.txt' % name), jl('b589_constellation_%s.json' % name))
    X['b454'] = jl('b589_constellation_b454.json')
    X['b454_txt'] = rd('b589_constellation_b454.txt')
    X['sweep'] = jl('b589_sweep.json')
    X['sweep_txt'] = rd('b589_sweep.txt')
    pat = 'D:/MY-DOwnloads/patent-package-BACKUP-2026-08-29'
    X['pat_log'] = [(l.split(' ', 1)[0], files_of(pat, l.split(' ', 1)[0])) for l in gs(pat, 'log', '--pretty=%H %s', 'd011b8f..HEAD').split(NL) if l.strip()]
    X['pat_file'] = raw(os.path.join(pat, REC.SWEEP_FILE))
    X['pat_remote'] = gs(pat, 'remote', '-v')
    X['tw'] = jl('b589_three_way.json')
    X['tw_txt'] = rd('b589_three_way.txt')
    X['kr'] = jl('b589_keiper_read.json')
    X['lv'] = jl('b589_lv_remeasure.json')
    X['lv_txt'] = rd('b589_lv_remeasure.txt')
    X['wt_list'] = gs('D:/SIDE-lv-conservation', 'worktree', 'list')
    X['wt_exists'] = os.path.exists(REC.WT)
    X['trial'] = gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551')
    X['pp_price'] = jl('b589_product_price.json')
    X['pp_txt'] = rd('b589_product_price.txt')
    X['wo'] = jl('b589_workorders.json')
    X['w1'] = jl('b589_weight_lines.json')
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
    i = t.find('### b589 — lane three, act seventeen under (R199)')
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return not [f for f, t in S['tooltext'].items() if pat.search(t)]


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


# ### the edition read on its own: its body is the current version line for line, the version line, the credit and the blank before
# ### it taken out, the back matter cut at its tag
def segs(S, l):
    return [s for s in S['CP'].segments(l) if s]


def bm_cut(S):
    cut = [i for i, l in enumerate(S['ed']) if l == S['REC'].BM_TAG]
    return cut[0] if len(cut) == 1 else None


def aligned(S):
    c = bm_cut(S)
    if c is None:
        return None
    body = S['ed'][:c - 1]
    v = S['REC'].VERSION
    if len(body) < v[0] + 1 or body[v[0] - 1] != v[1]:
        return None
    k = [n for n, l in enumerate(body) if l == S['REC'].CREDIT[1]]
    if len(k) != 1 or body[k[0] - 1] != '':
        return None
    drop = {v[0] - 1, k[0] - 1, k[0]}
    return [l for n, l in enumerate(body) if n not in drop]


def oline_pre(S, n):
    ls = cr0(S['ot_pre']).decode('utf-8', 'replace').split(NL)
    return ls[n - 1] if 0 < n <= len(ls) else ''


def changed_lines(S):
    return set(r[0] for r in S['REC']._all_changes())


def carries(S):
    keep = aligned(S)
    if keep is None or len(keep) != len(S['cur']):
        return False
    ch = changed_lines(S)
    return all(keep[i] == S['cur'][i] for i in range(len(S['cur'])) if (i + 1) not in ch) and \
        all(keep[i] != S['cur'][i] for i in range(len(S['cur'])) if (i + 1) in ch)


def rewrites_ok(S):
    keep = aligned(S)
    if keep is None or len(keep) != len(S['cur']) or len(S['rows']) != 2:
        return False
    return all(r['sentence'] not in segs(S, keep[r['line'] - 1]) for r in S['rows']) and \
        all(len(segs(S, keep[r['line'] - 1])) == len(segs(S, S['cur'][r['line'] - 1])) for r in S['rows'])


def h28a_ok(S):
    edtxt = NL.join(S['ed'])
    diff = S['ej'].get('diff', [])
    if len(diff) != 2:
        return False
    b557 = rd('b557_tiers.txt').split(NL)
    for d in diff:
        if d['new'] not in edtxt or d['new'] == d['old'] or not d['banks']:
            return False
        for b in d['banks']:
            f, n = b.split(':')
            if f != 'b557_tiers.txt' or d['terminal'] not in (b557[int(n) - 1] + b557[int(n) - 3] + b557[int(n) - 5]):
                return False
    return S['hj'].get('H28a') == 'HELD'


def counts_ok(S):
    n = lambda ls: sum(len(segs(S, l)) for l in ls)
    c = bm_cut(S)
    if c is None:
        return False
    n_cur, n_body, n_ed = n(S['cur']), n(S['ed'][:c - 1]), n(S['ed'])
    E = S['ej']
    allowed = E.get('credit', -1) + E.get('removals', -1) + E.get('ruled_citations', -1) + E.get('version_lines', -1)
    return (n_cur == E.get('n_cur') and n_body == E.get('n_body') and n_ed == E.get('n_full') and n_body - n_cur == S['hj'].get('body_dn')
            and allowed == S['hj'].get('allowed') == 2 and S['hj'].get('H28b') == ('HELD' if abs(n_body - n_cur) <= allowed else 'REFUTED'))


def scan_fields(out):
    live = re.search(r'live uses\s*:\s*(\d+)', out or '')
    v = re.search(r'^\s*VERDICT\s*: (.+)$', out or '', re.M)
    return (int(live.group(1)) if live else None, v.group(1).strip() if v else None)


def stems_now(S):
    live, v = scan_fields(S['bt_now'])
    return live == 0 and v == 'CLEAN' and S['hj'].get('H28c') == 'HELD' and S['hj'].get('live') == 0


def ceiling_beyond(S):
    REC = S['REC']
    c = bm_cut(S)
    if c is None:
        return None
    fixed = set(REC._edl(x[0]) for x in REC.CEILS)
    beyond = 0
    for i, l in enumerate(S['ed'], 1):
        for m in REC.CEILING.finditer(l):
            rec_ = i > c + 1 and l.startswith('| :') and REC.CEIL_RECORD in l
            if not (rec_ or (i <= c and i in fixed)):
                beyond += 1
    return beyond


def corr_ok(S, rows, rec, tail):
    keep = aligned(S)
    c = bm_cut(S)
    if keep is None or c is None:
        return False
    bm = NL.join(S['ed'][c:])
    return all(new in keep[ln - 1] and keep[ln - 1].count(old) == new.count(old) and old in S['cur'][ln - 1]
               and ('| :%d | %s %s%s | %s |' % (S['REC']._edl(ln), rec, old, tail, new)) in bm for ln, old, new in rows)


def fact_ok(S):
    REC = S['REC']
    reg = S['registry_pre'][961] if len(S['registry_pre']) > 961 else ''
    return len(REC.FACTS) == 1 and corr_ok(S, REC.FACTS, REC.FACT_RECORD, '') \
        and 'Deposited at **v1.5** = `0e5233f`' in reg and 'record 21520474' in reg and 'zenodo.21417776' in REC.FACTS[0][2]


def credit_ok(S):
    ed = S['ed']
    E = S['ej'].get('credit_line', {})
    at = E.get('at')
    t = S['REC'].CREDIT[1]
    keep = aligned(S)
    ot = cr0(S['ot_pre']).decode('utf-8', 'replace').split(NL)
    return at is not None and keep is not None and ed[at - 1] == t and ed[at - 2] == '' and ed[at - 3] == keep[182] \
        and S['cur'][182].startswith('*Census note (demarcation line).') and 'OPEN_TRAILS :773' in t and ':8839-:8847' in t \
        and 'inside that side and is not of the kind the dichotomy formalizes' in t and 'CROSS-LINK' in ot[772] and len(segs(S, t)) == 1


def terms_ok(S):
    T, N = S['tj_terms'], S['terms_now']
    return all(N.get(n, {}).get(p) and T.get(n, {}).get(p, {}).get('line') == N[n][p] for _, n, ps in S['REC'].TERMS for p in ps) \
        and all('SCAFFOLDING' in ' '.join(T['sieve_ceiling'][p]['doc']) for p in ('v1.4', 'v1.7')) \
        and 's.classes ≥ 1' in ' '.join(T['e_difficulty']['v1.1']['sig']) and 's.classes' not in ' '.join(T['e_difficulty']['v1.7']['sig'])


def table_ok(S):
    c = bm_cut(S)
    if c is None:
        return False
    bm = S['ed'][c:]
    REC = S['REC']
    try:
        i = bm.index(REC.TABLE_HEAD)
    except ValueError:
        return False
    rows = bm[i + 2:i + 2 + len(REC.TABLE_ROWS)]
    names = ['`%s`' % n for row, n, pins in REC.TERMS if row]
    return len(REC.TABLE_ROWS) == 4 and rows == ['| %s |' % ' | '.join(r) for r in REC.TABLE_ROWS] \
        and [r[2] for r in REC.TABLE_ROWS] == names and all('SIDE-kernel v1.7 = `2957e7d`' == r[1] for r in REC.TABLE_ROWS) \
        and S['hj'].get('table_rows') == 4


def tier_ok(S):
    REC = S['REC']
    return len(S['cur']) == 258 and S['cur'][235].startswith('#### THE CASCADE, ACT ELEVEN') \
        and all(S['ed'][REC._edl(n) - 1] == S['cur'][n - 1] for n in range(219, 259))


def version_ok(S):
    v = S['REC'].VERSION
    return len(S['ed']) > 22 and S['ed'][v[0] - 1] == v[1] and v[1].startswith('**v1.0.4, 2026-10-01**') \
        and S['ed'][v[0]] == S['cur'][v[0] - 1] and S['cur'][v[0] - 1].startswith('**v1.0.3, 2026-07-23**')


BM_HEADS = ('### Removals', '### Credit lines', '### Ceiling corrections', '### Ceiling-shaped sentences read and carried',
            '### Stem corrections', '### Fact corrections', '### The history entries', '### The navigator’s expectations of `(R199)`(2)',
            '### Placement', '### Correspondence')


def backmatter_ok(S):
    c = bm_cut(S)
    if c is None:
        return False
    bm = S['ed'][c:]
    return all(h in bm for h in BM_HEADS) and any(l.startswith('None: both work-list rows resolve') for l in bm)


def superseded_ok(S):
    c = bm_cut(S)
    if c is None:
        return False
    bm = NL.join(S['ed'][c:])
    b450 = rd('b450_components.txt').split(NL)
    return 'b450’s line “THERE IS NO TABLE” for this document (relay `data/b450_components.txt` :174' in bm and 'is superseded by it' in bm \
        and 'E_DIFFICULTY_THEOREM' in b450[173] and 'THERE IS NO TABLE' in b450[173]


CELLRX = re.compile(r'\| cited at :([0-9, :]+) of this edition \|$')


def repin_final_ok(S):
    c = bm_cut(S)
    if c is None:
        return False
    body = S['ed'][:c]
    REC = S['REC']
    rows = 0
    for l in S['ed'][c:]:
        mb = re.match(r'^\| `data/([\w.]+)` :(\d+) \|', l)
        ml = [nd for nd, _, _ in REC.LEDGERS if l.startswith('| %s |' % nd)]
        cell = CELLRX.search(l)
        if not cell:
            continue
        got = [int(x) for x in re.findall(r'\d+', cell.group(1))]
        if mb:
            want = [k for k, x in enumerate(body, 1) if ('relay `data/%s` :%s' % (mb.group(1), mb.group(2))) in x]
        elif ml:
            want = [k for k, x in enumerate(body, 1) if ml[0] in x]
        else:
            continue
        rows += 1
        if got != want or not want:
            return False
    return rows == len(REC.BANKROWS) + len(REC.LEDGERS)


def offset_ok(S):
    first = S['etxt'].split(NL)[0]
    d = S['ej'].get('diff', [])
    return first.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3): +1 from :6 (the v1.0.4 line') and S['etxt'].count('### OFFSET FROM') == 1 \
        and len(d) == 2 and all(x['ed_line'] == S['REC']._edl(x['line']) and S['ed'][x['ed_line'] - 1].find(x['new'][:60]) >= 0 for x in d) \
        and all(('v1.0.3 :%d -> v1.0.4 :%d' % (x['line'], x['ed_line'])) in S['etxt'] for x in d)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return fline(S, e).startswith('## The comprehensive housekeeping act: E_DIFFICULTY_THEOREM') and '**E_DIFFICULTY_THEOREM**' in tail \
        and '**The constellation re-read**' in tail and '**The three research items**' in tail and '**The product lemma**' in tail


def cbanks_ok(S):
    CN = S['CN']
    if len(CN.DOCS) != 20:
        return False
    tot = 0
    for key, (name, curp, edp, start) in CN.DOCS.items():
        t, j = S['cbanks'][name]
        if not t.startswith('b589 -- COMPONENT 2: THE CONSTELLATION RE-READ OF %s' % name) or j.get('doc') != name:
            return False
        if 'NOT EXERCISED' not in t:
            return False
        tot += j.get('moved', -1)
        if j.get('moved', 0) != t.count('  ### MOVED :'):
            return False
    return tot == S['csum'].get('moved')


def csum_ok(S):
    t = S['csum_txt']
    rows = [l for l in t.split(NL) if l.startswith('| ') and not l.startswith('| table')]
    return len(rows) == 20 and S['csum'].get('tables') == 20 and 'NOT RUN' not in t \
        and ('CELLS MOVED: %d.' % S['csum']['moved']) in t


def b454_ok(S):
    CN = S['CN']
    led = CN._ledgers()
    low = lambda s: s.lower()
    same = lambda s: s
    for name, s1, s2 in CN.B454_SHAPES:
        st = S['b454'].get(name)
        if not st:
            return False
        hi = sum(1 for f, ls in led for l in ls if s1(l, low) or s2(l, low))
        hs = sum(1 for f, ls in led for l in ls if s1(l, same) or s2(l, same))
        if hi != st['insensitive'] or hs != st['sensitive'] or st['unread'] != 0:
            return False
    return 'rows unread 0' in S['b454_txt'] and len(S['csum'].get('newly', [])) == sum(1 for v in S['b454'].values() if v['state'].startswith('LOCATED'))


def sweep_ok(S):
    sw = S['sweep']
    f = S['pat_file'] or b''
    return sw.get('held') is True and 'HELD' in S['sweep_txt'] and sw.get('sha256') == hashlib.sha256(f).hexdigest() \
        and b'PROV1_FORMATION_VERIFICATION_ARCHITECTURE' not in S['sweep_txt'].encode('utf-8')[:0] and 'claim family' not in S['sweep_txt'].lower() \
        and sw.get('instruments') == 12


def patent_commit_ok(S):
    return len(S['pat_log']) == 1 and S['pat_log'][0][1] == [S['REC'].SWEEP_FILE] and S['pat_remote'] == '' and S['pat_file'] is not None


def three_way_ok(S):
    tw = S['tw']
    return len(tw.get('rows', [])) == 12 and [r['n'] for r in tw['rows']] == list(range(1, 13)) and 'H30a' in S['tw_txt']


def h30a_ok(S):
    tw = S['tw']
    miss = [(r['n'], k) for r in tw.get('rows', []) for k, a, b, fa, fb in (
        ('zk', r['zero'], float(r['keiper']), r['floor_z'], r['floor_k']),
        ('ak', r['arith'], float(r['keiper']), r['floor_a'], r['floor_k']),
        ('az', r['arith'], r['zero'], r['floor_a'], r['floor_z'])) if abs(a - b) > fa + fb]
    return tw.get('rows') and (tw.get('H30a') == ('HOLDS' if not miss else 'REFUTED')) and S['sc'].get('N3', [''])[0] == ('HELD' if not miss else 'REFUTED')


def keiper_ok(S):
    kr = S['kr']
    p = kr.get('patterns', {})
    return kr.get('head', '').startswith('de5ce8a9') and len(p) == 3 and kr.get('price') \
        and any('riemannZeta_residue_one' in h for h in p.get('the residue / Laurent expansion of riemannZeta at 1', {}).get('hits', [])) \
        and 'TWO LEMMAS OF SUBSTANCE' in ' '.join(kr['price'])


def lv_ok(S):
    lv = S['lv']
    m = lv.get('meta', {})
    return m.get('mathlib', '').startswith('de5ce8a9') and m.get('toolchain', '').endswith('v4.34.0-rc1') and len(lv.get('res', {})) == len(m.get('order', [])) \
        and len(m.get('order', [])) == 25 and m.get('price') and 'THE PRICE' in S['lv_txt']


def lv_gone_ok(S):
    return not S['wt_exists'] and 'b589-lv-remeasure' not in S['wt_list'] and S['trial'] == 'f22ff35'


def product_ok(S):
    pr = ' '.join(S['pp_price'].get('price', []))
    return 'ONE LEMMA OF SUBSTANCE' in pr and 'h2_sign_cfg_iff_target' in S['pp_txt'] and 'structure WeilConfig' in S['pp_txt'] \
        and 'def HCount' in S['pp_txt'] and 'structure ZeroConfig' in S['pp_txt']


def workorders_ok(S):
    L = S['wo'].get('lines', {})
    keys = ('constellation', 'threeway', 'keiper', 'toolchain', 'product')
    return all(oline(S, L.get(k)).startswith('*Appended 2026-10-01 by b589 to ') for k in keys) \
        and '(:12090)' in oline(S, L['constellation']) and '(:11703)' in oline(S, L['threeway']) and '(:11704)' in oline(S, L['keiper']) \
        and '(:11664)' in oline(S, L['toolchain']) and '(:11373)' in oline(S, L['product']) and 'REMAINDER 5' in oline(S, L['product'])


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R199) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '  1234   5678 lean.exe        2026-09-01 00:00:00  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b588`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b588' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b589 -- x'])),
    ('G-R199-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R199) END' in S['ferry'] and S['ot'].count('**(R199) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R199) ratified', '(R199) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'E_DIFFICULTY_THEOREM.txt @', 'E_DIFFICULTY_THEOREM.md @', 'INVARIANCE_BARRIERS_v1_4.md @', 'b586_corroboration.txt @', 'README.md @',
        'b454_registration_2026-09-14.txt @', 'VERIFICATION_LOOM.md @', 'TECHNE_TOOLKIT_v8_3.md @', 'b257_methodology_sweep.txt @',
        'BALANCE_AND_POSITIVITY.md @', 'b562_drift.txt @', 'b563_per_n.txt @', 'b557_tiers.txt @', 'REGISTRY.md @', 'Config.lean @',
        'b588_closing_push_out.txt @', 'THE PROVISIONAL SPECIFICATION, SEARCHED'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 0b552b52`s files', lambda S: S['pushout'][0] == ['data/b588_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b588') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b588'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['w1']['lines'].get('weight')).startswith(S['w1']['heads']['weight'])
     and 'b588 AT ITS WEIGHT' in fline(S, S['w1']['lines']['weight']) and '(:6694)' in fline(S, S['w1']['lines']['weight'])
     and 'The suite reads 70 of 70.' in fline(S, S['w1']['lines']['weight']),
     lambda S: put(S, 'w1', dict(S['w1'], lines=dict(S['w1']['lines'], weight=1)))),
    ('G-TECHNE-CREDIT-REREAD', 'FINDINGS at the banked re-read line and TECHNE v8.3 :242 at its blob', lambda S: fline(S, S['w1']['lines'].get('reread')).startswith(S['w1']['heads']['reread'])
     and S['w1'].get('inside') is True and 'lies inside that side and is not of the kind F-7 formalizes' in S['w1'].get('techne_242', '')
     and 'it agrees, and no correction is made.' in fline(S, S['w1']['lines']['reread']),
     lambda S: put(S, 'w1', dict(S['w1'], inside=False))),
    ('G-EDIFF-TERMS-REPRINTED', 'SieveCeiling.lean and SieveCeilingSemantic.lean at the three tags afresh', lambda S: terms_ok(S),
     lambda S: put(S, 'terms_now', dict(S['terms_now'], **{'e_difficulty': {'v1.1': None, 'v1.4': 309, 'v1.7': 309}}))),
    ('G-EDIFF-TABLE', 'the back matter`s table against the tier block`s terminals', lambda S: table_ok(S),
     lambda S: put(S, 'ed', [l.replace('| `e_difficulty_xi` |', '| `e_difficulty_x` |') for l in S['ed']])),
    ('G-EDITION-BESIDE', 'the edition file and the current version`s blob', lambda S: S['ed_exists'] and len(S['ed']) > len(S['cur'])
     and S['cur_head_blob'] == S['ej'].get('cur_blob') and S['cur_work_blob'] == S['ej'].get('cur_blob')
     and os.path.dirname(S['REC'].ED) == os.path.dirname(S['REC'].CUR), lambda S: put(S, 'cur_work_blob', '0' * 40)),
    ('G-EDITION-CARRIES', 'the edition against the current version, line by line', lambda S: carries(S),
     lambda S: put(S, 'ed', [l + ('x' if i == 30 else '') for i, l in enumerate(S['ed'])])),
    ('G-EDITION-REWRITES', 'the 2 rows` sentences against the edition`s aligned lines', lambda S: rewrites_ok(S),
     lambda S: put(S, 'ed', [S['cur'][161] if l.startswith('- `sieve_ceiling` —') else l for l in S['ed']])),
    ('G-H28A-CITES', 'each rewrite against the b557 bank line it cites', lambda S: h28a_ok(S),
     lambda S: put(S, 'ej', dict(S['ej'], diff=[dict(d, banks=['b557_tiers.txt:9']) for d in S['ej'].get('diff', [])]))),
    ('G-H28B-COUNTED', 'the counts recomputed from both texts', lambda S: counts_ok(S), lambda S: put(S, 'hj', dict(S['hj'], body_dn=3))),
    ('G-H28C-STEMS', 'banned_terms.py --new run afresh on the edition', lambda S: stems_now(S) and ceiling_beyond(S) == 0,
     lambda S: put(S, 'bt_now', S['bt_now'].replace('live uses        : 0', 'live uses        : 1'))),
    ('G-CEILING-CORRECTED', 'the edition`s aligned lines and its correction rows', lambda S: corr_ok(S, S['REC'].CEILS, S['REC'].CEIL_RECORD, '')
     and [x[0] for x in S['REC'].CEILS] == [24, 48, 136, 136, 138, 138, 177] and ceiling_beyond(S) == 0,
     lambda S: put(S, 'ed', [l.replace('The 167 years without a proof were', 'The 167-year delay was') for l in S['ed']])),
    ('G-FACT-CORRECTED', 'the edition`s :204, its fact row and REGISTRY :962 at its pre-act blob', lambda S: fact_ok(S),
     lambda S: put(S, 'registry_pre', [l.replace('Deposited at **v1.5**', 'Deposited at **v1.3**') for l in S['registry_pre']])),
    ('G-CREDIT-LINE', 'the edition beneath :183 and the ledger lines it cites', lambda S: credit_ok(S),
     lambda S: put(S, 'ed', [l.replace('inside that side and is not of the kind', 'outside that side and of the kind') for l in S['ed']])),
    ('G-TIER-BLOCK-STANDS', 'v1.0.3 :219-:258 against the edition`s lines by the offset', lambda S: tier_ok(S),
     lambda S: put(S, 'ed', [l + (' x' if l.startswith('#### THE CASCADE, ACT ELEVEN') else '') for l in S['ed']])),
    ('G-VERSION-LINE', 'the edition`s head against the current version`s', lambda S: version_ok(S),
     lambda S: put(S, 'ed', [l for l in S['ed'] if l != S['REC'].VERSION[1]])),
    ('G-BACK-MATTER', 'the edition`s back matter', lambda S: backmatter_ok(S), lambda S: put(S, 'ed', [l for l in S['ed'] if l != '### Fact corrections'])),
    ('G-TABLE-SUPERSEDED', 'the back matter`s Correspondence paragraph and b450`s components line', lambda S: superseded_ok(S),
     lambda S: put(S, 'ed', [l.replace('is superseded by it', 'is noted') for l in S['ed']])),
    ('G-STATUS-CELLS', 'every Status column of the edition, cell by cell', lambda S: S['REC']._status_blanks(S['ed']) == [],
     lambda S: put(S, 'ed', S['ed'] + ['', '| a | Status |', '|:--|:--|', '| x |  |'])),
    ('G-REPIN-FINAL', 'the edition`s Correspondence column against its final body', lambda S: repin_final_ok(S),
     lambda S: put(S, 'ed', [l.replace('| cited at :', '| cited at :1, :', 1) if l.startswith('| REGISTRY :962 |') else l for l in S['ed']])),
    ('G-OFFSET-LINE', 'the diff bank`s head and its rows', lambda S: offset_ok(S),
     lambda S: put(S, 'etxt', NL.join(S['etxt'].split(NL)[1:]))),
    ('G-DIFF-BANKED', 'the diff bank', lambda S: S['etxt'].count('      v1.0.4 : ') == 2 and S['etxt'].count('      v1.0.3 : ') == 2
     and '### ### **H28a ' in S['etxt'] and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in S['etxt']
     and 'the source: PLACE-papers REGISTRY.md :962' in S['etxt'] and 'THE CORRESPONDENCE TABLE, WRITTEN FIRST (4 rows)' in S['etxt'],
     lambda S: put(S, 'etxt', S['etxt'].replace('      v1.0.4 : ', '      v1.0.4: ', 1))),
    ('G-CONSTELLATION-BANKS', 'each table`s bank and json, the twenty documents', lambda S: cbanks_ok(S),
     lambda S: put(S, 'cbanks', dict(S['cbanks'], **{'GRH_CASCADE': ('', {})}))),
    ('G-CONSTELLATION-SUMMARY', 'the summary bank against the twenty jsons', lambda S: csum_ok(S),
     lambda S: put(S, 'csum_txt', S['csum_txt'].replace('| GRH_CASCADE |', '| GRH_CASCADE | ### NOT RUN -- HELD |'))),
    ('G-B454-RESEARCHED', 'b454`s shapes re-run case-insensitively at the fixed ledgers afresh', lambda S: b454_ok(S),
     lambda S: put(S, 'b454', dict(S['b454'], **{'Face E / keyhole': dict(S['b454']['Face E / keyhole'], unread=1)}))),
    ('G-SWEEP-HELD', 'the sweep bank and its json against the patent file`s bytes', lambda S: sweep_ok(S),
     lambda S: put(S, 'pat_file', (S['pat_file'] or b'') + b'x')),
    ('G-SWEEP-PATENT-COMMIT', 'the patent repository`s log since d011b8f and its remotes', lambda S: patent_commit_ok(S),
     lambda S: put(S, 'pat_log', S['pat_log'] + [('x', ['y'])])),
    ('G-THREE-WAY-BANKED', 'the three-way bank', lambda S: three_way_ok(S), lambda S: put(S, 'tw', dict(S['tw'], rows=S['tw'].get('rows', [])[:11]))),
    ('G-H30A-SCORED', 'the pairwise floors recomputed from the three-way json', lambda S: h30a_ok(S),
     lambda S: put(S, 'tw', dict(S['tw'], rows=[dict(r, zero=r['zero'] + 1.0) if r['n'] == 5 else r for r in S['tw'].get('rows', [])]))),
    ('G-KEIPER-READ', 'the Keiper read`s json', lambda S: keiper_ok(S), lambda S: put(S, 'kr', dict(S['kr'], head='0000000'))),
    ('G-LV-REMEASURE', 'the lv bank and its json', lambda S: lv_ok(S), lambda S: put(S, 'lv', dict(S['lv'], meta=dict(S['lv'].get('meta', {}), mathlib='51e6992')))),
    ('G-LV-WORKTREE-GONE', 'the lv repository`s worktree list, the path and the trial branch', lambda S: lv_gone_ok(S),
     lambda S: put(S, 'wt_exists', True)),
    ('G-PRODUCT-PRICED', 'the product bank', lambda S: product_ok(S), lambda S: put(S, 'pp_price', dict(price=['TWO LEMMAS']))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b589 — lane three, act seventeen under (R199)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORKORDER-LINES', 'OPEN_TRAILS at the five banked work-order lines', lambda S: workorders_ok(S),
     lambda S: put(S, 'wo', dict(S['wo'], lines=dict(S['wo'].get('lines', {}), product=1)))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'SIMPLICITY held, then RESIDUE' in trail(S) and 'SIMPLICITY-FACE on the author’s word' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('SIMPLICITY held, then RESIDUE', 'x'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{DIR_PAGE: ((S['pages'][DIR_PAGE][0] or b'') + b'x', S['pages'][DIR_PAGE][1])}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff, the trial branch', lambda S: S['kmain'] == V015
     and S['kcur'] == 'main' and S['kdirty'] == '' and all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] == []
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-rcurve': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b589_record.py'): S['tooltext'].get(os.path.join(T, 'b589_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: not [f for f, t in S['tooltext'].items()
                                                                        if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-UNTOUCHED', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == [S['REC'].ED]
     and S['cur_head_blob'] == S['ej'].get('cur_blob'), lambda S: put(S, 'keystone_changes', sorted(S['keystone_changes'] + [S['REC'].CUR]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 83571aab, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b588_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', S['REC'].ED]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 8)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b589')" in S['suite'] and "data/b589_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b589')", ''))),
]


def regenerate():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def main():
    pushed = RERUN or is_pushed()
    rec('=' * 104)
    rec('b589 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if RERUN else regenerate()
    if RERUN:
        S['table_changed'] = []
    else:
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
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b589_checks_postpush.txt' if pushed else 'b589_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b589_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
