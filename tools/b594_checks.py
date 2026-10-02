# -*- coding: utf-8 -*-
"""b594_checks.py -- THE SUITE OF b594, UNDER (R204): CP-7 ACT SIXTEEN, THE EDITION OF FACES_OF_H2_AT_FINITE_INSTANCE UNDER THE
PRECEDENCE ORDER; THE THREE STANDING INSTRUCTIONS ENTERED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b594_checks.txt before the push and
### data/b594_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b594_arms_prerun.txt and nothing else.
### ### The harness is b568's to b593's, carried; the arms are b594's.
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
FACE = os.path.join(D, 'b594_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md'
ED = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md'
PRE = dict(relay='aea25c80', pp='bf4e9f5', gs='3528bcf')
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
PRE_HEADS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72'}
STEPZERO = '2e7c89d6'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f7dd7aec-e7f8-492c-a0db-31ef189124e6/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b594')
            and 'data/b594_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def _old_module(path, name):
    import types
    src = gs(ROOT, 'show', '%s:%s' % (PRE['relay'], path))
    m = types.ModuleType(name)
    m.__dict__['__file__'] = os.path.join(T, os.path.basename(path))
    exec(compile(src, name, 'exec'), m.__dict__)
    return m



def sources():
    import b594_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b594_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b594_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b594_ferry.txt'), scan=rd('b594_ferry_scan.txt'), cens=rd('b594_census_stepzero.txt'),
        fcens=rd('b594_faces_census_stepzero.txt'), pins0=rd('b594_pins_stepzero.txt'), procs=rd('b594_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b593_closing.txt'), reads=rd('b594_reads.txt'), branches=rd('b594_branches.txt'), answers=rd('b594_author_answers.txt'),
        prerun=rd('b594_arms_prerun.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
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
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b593*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b594_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b594_mustnotexist.txt')), table_changed=None,
        fj=jl('b594_findings.json'), tj=jl('b594_trail.json'), sc=jl('b594_scores.json'), desk=rd('b594_desk_notes.txt'),
        wl1=jl('b594_weight_line.json'), rl=jl('b594_rule_lines.json'),
        P=jl('b594_pages.json'), E=jl('b594_edition.json'), H=jl('b594_h28.json'),
        bank=rd('b594_edition_FACES.txt'), termscan=rd('b594_edition_termscan.txt'), repin=rd('b594_repin.txt'),
        arms_c2=rd('b594_page_arms_c2.txt'), runs=rd('b594_page_runs.txt'),
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
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b592_nodes.txt'), os.path.join(SP, '_b594_gcp'), os.path.join(D, 'b592_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b592_nodes_chi.txt'), os.path.join(SP, '_b594_gcp'), os.path.join(D, 'b592_chi_probe_out.txt'))
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
    ed, REC = S['ed'], S['REC']
    if not ed:
        return False
    rows = [r for r in json.load(io.open(os.path.join(D, 'b558_cp1b.json'), encoding='utf-8'))['rows'] if r['doc'] == 'FACES' and r['verdict'] == 'MOVED-IN-MEANING']
    cur = lines_of(S['cur'][1])
    ok = len(rows) == 1
    for r in rows:
        sg = [x for x in CP.segments(cur[r['line'] - 1]) if x]
        k = sg.index(r['sentence'])
        nw = [x for x in CP.segments(ed[_edl(S, r['line']) - 1]) if x][k]
        ok = ok and nw != r['sentence'] and '`v0.6.0 = c80bdc2`' in nw and 'relay `data/b547_faces.json` :27' in nw and '`SIDE-kernel` `v1.5' not in nw
    return ok


def ruled_rewrites(S):
    ed, REC = S['ed'], S['REC']
    if not ed:
        return False
    l = ed[_edl(S, 39) - 1]
    return all(rep in ed[_edl(S, ln) - 1] for ln, old, rep in REC.RULED) and all(
        x in l for x in ('`h2_sign_iff_rh`', '`5c72cad`', '`li_nonneg_iff_rh`', '`arith_limit_nonneg_iff_rh`', '`e5a5a83`'))


def collisions(S):
    ed, REC = S['ed'], S['REC']
    if not ed or BM_TAG(S) not in ed:
        return False
    bm = NL.join(ed[ed.index(BM_TAG(S)):])
    rows = [l for l in bm.split(NL) if re.match(r'^\| :\d+ \| (history clause|the work-list row);', l)]
    return len(REC.COLLISIONS) >= 2 and len(rows) == len(REC.COLLISIONS) and '### Collisions resolved by the precedence order' in bm \
        and all(('| :%d |' % _edl(S, c[0])) in bm for c in REC.COLLISIONS) and len(S['E'].get('collisions', [])) == len(REC.COLLISIONS)


def history_lines(S):
    ed, REC = S['ed'], S['REC']
    return bool(ed) and len(REC.HIST) == 2 and all(ed[_edl(S, a)] == '' and ed[_edl(S, a) + 1] == t for a, s, t in REC.HIST) \
        and '`h2_sign_iff_forall_upto`, SIDE-explicit-formula v0.3 = `04eda4a`' in REC.HIST[1][2] and 'relay `data/b550_reading37.txt` :18' in REC.HIST[0][2]


def version_line(S):
    ed, REC = S['ed'], S['REC']
    n = _edl(S, 10)
    return bool(ed) and ed[n - 3] == REC.VERSION[1] and ed[n - 2] == '' and ed[n - 1].startswith('**Method register · ### DRAFT')


def backmatter(S):
    ed = S['ed']
    if not ed or BM_TAG(S) not in ed:
        return False
    bm = NL.join(ed[ed.index(BM_TAG(S)):])
    heads = ['### Removals', '### Rewrites', '### Collisions resolved by the precedence order', '### Credit lines', '### History lines',
             '### Ceiling corrections', '### Stem corrections', '### Ceiling-shaped sentences read and carried', '### Fact corrections',
             '### The navigator’s expectations', '### Placement', '### Correspondence']
    pos = [bm.find(h) for h in heads]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and 'no object; recorded as the navigator’s' in bm and S['E'].get('status_blanks') == []


def h28a_ok(S):
    wl = [d for d in S['E'].get('diff', []) if d['kind'] == 'work-list']
    want = 'HELD' if len(wl) == 1 and all(d['changed'] and d['cites'] for d in wl) else 'REFUTED'
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
    ok_lines = set(_edl(S, n) for n in REC.CARRIED) | set(_edl(S, x[0]) for x in REC._all_changes()) | set(_edl(S, a) + 2 for a, _s, _t in REC.HIST)
    beyond = [i for i, l in enumerate(ed[:cut], 1) for m in REC.CEILING.finditer(l) if i not in ok_lines]
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['scan_now'], re.M) is not None and re.search(r'live uses\s*:\s*0\b', S['scan_now']) is not None
    want = 'HELD' if clean and not beyond else 'REFUTED'
    return S['H'].get('H28c') == want and S['sc'].get('H28c', [''])[0] == want and S['scan_now'].strip() == S['termscan'].strip()


def ed_bank(S):
    b = S['bank']
    return b.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3): ' + S['REC'].OFFSET) and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in b \
        and ('sha256 %s' % S['E'].get('sha256', '#')) in b


def repin_ok(S):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', S['repin'])
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > 20 and S['E'].get('sha256', '#') in S['bank']


def pages_alone(S):
    log = S['pp_log']
    P = S['P']
    want = sorted(PNAME_[k] for k in ('zeta', 'chi') if P.get(k, {}).get('changed'))
    pg = [h for h, s_ in log if S['pp_files'][h] in ([PAGE], [DIR_PAGE])]
    edc = [h for h, s_ in log if S['pp_files'][h] == [ED]]
    if len(edc) != 1 or len(pg) != len(want) or not want:
        return False
    idx = {h: i for i, (h, s_) in enumerate(log)}
    return all(idx[h] > idx[edc[0]] for h in pg) and all(s_.startswith('b594 housekeeping') for h, s_ in log if h in pg) \
        and sorted(S['pp_files'][h][0] for h in pg) == want


PNAME_ = {'zeta': PAGE, 'chi': DIR_PAGE}


def pages_c2_ok(S):
    P = S['P']
    ch = [k for k in ('zeta', 'chi') if P.get(k, {}).get('changed')]
    return bool(P) and bool(ch) and all(P[k]['identical'] for k in ('zeta', 'chi')) and \
        all(len([x for x in P[k]['diff'] if x.startswith('+| keystone naming a node |')]) == 1 and
            ('`%s`' % ED) in [x for x in P[k]['diff'] if x.startswith('+| keystone')][0] and
            not [x for x in P[k]['diff'] if x.startswith(('+', '-')) and not x.startswith(('+++', '---', '+| keystone'))] for k in ch)


def rule_lines_ok(S):
    rl = S['rl'].get('lines', [])
    return len(rl) == 2 and all(oline(S, x['line']).startswith(x['head']) for x in rl) and 'THE PRECEDENCE ORDER' in rl[0]['head'] \
        and '(:11864)' in rl[0]['head'] and 'the history clause governs, then the name-and-title exception, then the stem clause, then the ceiling ' \
        'clause, then the fact clause, then the restatement clause' in oline(S, rl[0]['line']) and '(:12062)' in rl[1]['head'] \
        and all(x in oline(S, rl[1]['line']) for x in ('research before conclusions', 'mutual light', 'offerings named', 'W-ORD-SIMPLICITY-FACE (b596)',
                                                        'REMAINDER 5', 'W-ORD-KEIPER-FACE', 'family form over χ mod q'))


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 16]) if e else ''
    return bool(e) and fline(S, e) == S['REC'].TITLE and '**The edition**' in tail and '**Read in mutual light**' in tail and ED in tail \
        and ('sha256 `%s`' % S['E'].get('sha256', '#')) in tail and 'DELIBERATION_TREE' in tail and 'FINDINGS :' in tail.split('**Read in mutual light**')[1][:600]


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R204) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b593`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b593' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b594 -- x'])),
    ('G-R204-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R204) END' in S['ferry'] and S['ot'].count('**(R204) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R204) ratified', '(R204) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'data/b558_editions/FACES_OF_H2_AT_FINITE_INSTANCE.txt @', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md @ bf4e9f5', PAGE + ' @ bf4e9f5',
        'FACES_LEDGER.md @ bf4e9f5', 'OPEN_TRAILS.md @ bf4e9f5', 'data/b550_reading37.txt @', 'data/b547_faces.json @', 'CouplingsAtPhi.lean @ c80bdc2',
        'DetectionRegion.lean @ c404e727', 'data/b593_closing_push_out.txt @', '### b450`s items for FACES_OF_H2', '"circularity witness" searched'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-NO-PROMPT', 'the act`s banks: no answers bank, no prompt put (the precedence order resolves)', lambda S: S['answers'] == ''
     and not os.path.exists(os.path.join(D, 'b594_author_answers.txt')), lambda S: put(S, 'answers', 'ANSWER: x')),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 2e7c89d6`s files', lambda S: S['pushout'][0] == ['data/b593_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b593') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b593'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'epstein-b590': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wl1'].get('line')).startswith(S['wl1'].get('head', '#'))
     and '(:6800)' in fline(S, S['wl1']['line']) and 'b593 AT ITS WEIGHT' in fline(S, S['wl1']['line']) and ':12212' in fline(S, S['wl1']['line']),
     lambda S: put(S, 'wl1', dict(S['wl1'], line=1))),
    ('G-RULE-LINES', 'OPEN_TRAILS at the precedence order and the standing instructions', lambda S: rule_lines_ok(S), lambda S: put(S, 'rl', dict(S['rl'], lines=[]))),
    ('G-CURRENT-UNEDITED', 'FACES_OF_H2_AT_FINITE_INSTANCE.md on disk and at HEAD against bf4e9f5', lambda S: ed_cur_unedited(S),
     lambda S: put(S, 'cur', (S['cur'][0] + b'x', S['cur'][1], S['cur'][2]))),
    ('G-EDITION-CARRIES', 'the edition at HEAD: every v0.9.4 line at its offset, unchanged unless changed by the form', lambda S: ed_carries(S),
     lambda S: put(S, 'ed', [x.replace('NON-FUSION', 'NON-FUSSION') for x in S['ed']])),
    ('G-WORKLIST-ROWS', 'the work-list row re-read at its segment, rewritten to its pin with its bank line', lambda S: worklist_rows(S),
     lambda S: put(S, 'ed', [x.replace('`v0.6.0 = c80bdc2`', '`v0.6.0 = c80bdc3`') for x in S['ed']])),
    ('G-RULED-REWRITES', 'the R4 row naming the three faces at their pins', lambda S: ruled_rewrites(S),
     lambda S: put(S, 'ed', [x.replace('`li_nonneg_iff_rh`', '`li_nonneg`') for x in S['ed']])),
    ('G-COLLISIONS', 'the back matter`s collision rows against the tool`s list and the edition json', lambda S: collisions(S),
     lambda S: put(S, 'ed', [x for x in S['ed'] if not x.startswith('| :%d | history clause; the ceiling' % S['REC']._edl(102))])),
    ('G-HISTORY-LINES', 'the two history lines beneath §4.1 and §4.2', lambda S: history_lines(S),
     lambda S: put(S, 'ed', [x for x in S['ed'] if 'a rung and not the face' not in x])),
    ('G-VERSION-LINE', 'the v0.2 line above the method-register line', lambda S: version_line(S), lambda S: put(S, 'ed', [x.replace('**v0.2 — 2026-10-02**', '**v0.2**') for x in S['ed']])),
    ('G-BACKMATTER', 'the back matter`s sections in order, its history rows, no blank Status cell', lambda S: backmatter(S),
     lambda S: put(S, 'ed', [x.replace('### Placement', '### Placings') for x in S['ed']])),
    ('G-EDITION-BANK', 'the diff bank`s offset head and its landing line', lambda S: ed_bank(S), lambda S: put(S, 'bank', S['bank'][5:])),
    ('G-REPIN', 'the re-pin bank against the final file', lambda S: repin_ok(S), lambda S: put(S, 'repin', S['repin'].replace(' of ', ' of 9', 1))),
    ('G-H28A-SCORED', 'the work-list rows` citations, the scores, the desk', lambda S: h28a_ok(S), lambda S: put(S, 'H', dict(S['H'], H28a='REFUTED'))),
    ('G-H28B-SCORED', 'the body and the current version counted afresh', lambda S: h28b_ok(S), lambda S: put(S, 'E', dict(S['E'], n_body=1))),
    ('G-H28C-SCORED', 'the scanner run afresh on the edition and the ceiling read afresh', lambda S: h28c_ok(S),
     lambda S: put(S, 'scan_now', S['scan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since bf4e9f5: each changed page committed alone after the edition commit',
     lambda S: pages_alone(S), lambda S: put(S, 'pp_files', {h: ([PAGE, DIR_PAGE] if f in ([PAGE], [DIR_PAGE]) else f) for h, f in S['pp_files'].items()})),
    ('G-PAGES-C2', 'the post-edition re-emits: byte-identical twice, one Placement row on each changed page', lambda S: pages_c2_ok(S),
     lambda S: put(S, 'P', dict(S['P'], zeta=dict(S['P'].get('zeta', {}), identical=False)))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b592`s v0.16 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b592`s v0.16 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the post-edition commits', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and 'G-CHAIN-PAGE : PASS' in S['arms_c2'] and 'G-CHAIN-PAGE-CHI : PASS' in S['arms_c2'],
     lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat under the precedence order, for the author’s strike' in trail(S)
     and 'no prompt was put' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('no prompt was put', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b595 the DELIBERATION_TREE module (TECHNE-Core, private, unpushed); then b596' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b595 the DELIBERATION_TREE module (TECHNE-Core, private, unpushed); then b596', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-explicit-formula': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b594_record.py'): S['tooltext'].get(os.path.join(T, 'b594_record.py'), '') + NL + 'os' + '.remove(p)'}))),
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
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at aea25c80, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b593_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [PNAME_[k] for k in ('zeta', 'chi') if S['P'].get(k, {}).get('changed')]),
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
                                                                          and "startswith('b594')" in S['suite'] and "data/b594_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b594')", ''))),
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
    rec('b594 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b594_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b594_checks_postpush.txt' if pushed else 'b594_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b594_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
