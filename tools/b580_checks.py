# -*- coding: utf-8 -*-
"""b580_checks.py -- THE SUITE OF b580, UNDER (R190): CP-7 ACT FIVE, THE EDITION OF ADDITIVE_MULTIPLICATIVE_CONSPIRACY, THE RE-PIN.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b580_checks.txt before the push and data/b580_checks_postpush.txt after
### it. ### The harness is b568's to b579's, carried; the arms are b580's.
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
FACE = os.path.join(D, 'b580_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='c34ef391', pp='a1de9dc', gs='8c392fe')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}
STEPZERO = 'c066701f'
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b580')
            and 'data/b580_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b580_record as REC
    import b558_record as CP
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b580_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b580_') and f.endswith('.py'))
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
              if l.strip() and l.split(' ', 1)[1].startswith('b580 housekeeping')]
        hk[key] = [files_of(repo, c) for c in cs]
    S = dict(
        REC=REC, CP=CP, face=face, ferry=rd('b580_ferry.txt'), scan=rd('b580_ferry_scan.txt'), cens=rd('b580_census_stepzero.txt'),
        fcens=rd('b580_faces_census_stepzero.txt'), pins0=rd('b580_pins_stepzero.txt'), procs=rd('b580_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b579_closing.txt'), reads=rd('b580_reads.txt'), branches=rd('b580_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), c1=jl('b580_c1_lines.json'),
        cur=cur, ed=ed, ed_exists=os.path.exists(edp), ej=jl('b580_edition.json'), hj=jl('b580_h28.json'), etxt=rd('b580_edition_AMC.txt'),
        escan=rd('b580_edition_termscan.txt'), bt_now=bt,
        cur_head_blob=gs(PP, 'rev-parse', 'HEAD:' + REC.CUR), cur_work_blob=gs(PP, 'hash-object', REC.CUR),
        page=lines_of(blob(PP, '192077f:' + PAGE)),
        rows=[r for r in json.load(io.open(os.path.join(D, 'b558_cp1b.json'), encoding='utf-8'))['rows']
              if r['doc'] == 'AMC' and r['verdict'] == 'MOVED-IN-MEANING'],
        p7_pre=cr0(blob(PP, '%s:%s' % (PRE['pp'], REC.PATHS7))).decode('utf-8', 'replace'),
        p7_now=cr0(raw(os.path.join(PP, *REC.PATHS7.split('/')))).decode('utf-8', 'replace'),
        f5_pre=cr0(blob(PP, '%s:%s' % (PRE['pp'], REC.FOUND5))), f5_now=cr0(raw(os.path.join(PP, *REC.FOUND5.split('/')))),
        b578_pre=cr0(blob(ROOT, '%s:data/%s' % (PRE['relay'], REC.B578_BANK))).decode('utf-8', 'replace'),
        b578_now=cr0(raw(os.path.join(D, REC.B578_BANK))).decode('utf-8', 'replace'), repj=jl('b580_repin.json'), hk=hk,
        fj=jl('b580_findings.json'), tj=jl('b580_trail.json'),
        sc=jl('b580_scores.json'), desk=rd('b580_desk_notes.txt'),
        pages={p: (blob(PP, 'HEAD:' + p), blob(PP, PRE['pp'] + ':' + p)) for p in (PAGE, DIR_PAGE)},
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kmain=gs(KER, 'rev-parse', 'main'), kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b579*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b580_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b580_mustnotexist.txt')), table_changed=None,
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
        if os.path.basename(p) in TABLE_FILES or p == 'data/' + REC.B578_BANK:
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


def trail(S):
    t = S['ot']
    i = t.find('### b580 — lane three, act eight under (R190)')
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


def segs(S, l):
    return [s for s in S['CP'].segments(l) if s]


def bm_cut(S):
    cut = [i for i, l in enumerate(S['ed']) if l == S['REC'].BM_TAG]
    return cut[0] if len(cut) == 1 else None


# ### the edition read on its own: its body is the current version line for line, the version line and the blank after it taken out
def aligned(S):
    c = bm_cut(S)
    if c is None:
        return None
    body = S['ed'][:c - 1]
    v = [i for i, l in enumerate(body) if l == S['REC'].VERSION[1]]
    if len(v) != 1 or body[v[0] + 1] != '':
        return None
    return body[:v[0]] + body[v[0] + 2:]


def changed_lines(S):
    return set(r[0] for r in S['REC'].REWRITES) | set(c[0] for c in S['REC'].CEILS)


def carries(S):
    keep = aligned(S)
    if keep is None or len(keep) != len(S['cur']):
        return False
    ch = changed_lines(S)
    return all(keep[i] == S['cur'][i] for i in range(len(S['cur'])) if (i + 1) not in ch) and \
        all(keep[i] != S['cur'][i] for i in range(len(S['cur'])) if (i + 1) in ch)


def rewrites_ok(S):
    keep = aligned(S)
    if keep is None or len(keep) != len(S['cur']) or len(S['rows']) != 13:
        return False
    return all(r['sentence'] not in segs(S, keep[r['line'] - 1]) for r in S['rows']) and \
        all(len(segs(S, keep[r['line'] - 1])) == len(segs(S, S['cur'][r['line'] - 1])) for r in S['rows'])


def page_pin_ok(S, name, pin):
    """### the declaration is a node of the zeta page, and the pin the edition prints for it is the one the node prints."""
    node = [l for l in S['page'] if re.match(r'^\d+\. `', l) and (('.%s`' % name) in l)]
    return bool(node) and any(pin.replace('`', '') in l for l in node)


def h28a_ok(S):
    edtxt = NL.join(S['ed'])
    PIN = S['REC'].PIN
    diff = S['ej'].get('diff', [])
    if len(diff) != 13:
        return False
    for d in diff:
        if d['new'] not in edtxt or d['new'] == d['old']:
            return False
        cited = [n for n in PIN if ('`%s`' % n) in d['new'] and PIN[n] in d['new'] and page_pin_ok(S, n, PIN[n])]
        banks = [b for b in re.findall(r'relay `(data/[^`]+)` :\d+', d['new']) if os.path.exists(os.path.join(ROOT, b))]
        if not (cited or banks):
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


def live_lines(t):
    return sorted(int(m) for m in re.findall(r'\.md :(\d+)\s+### LIVE USE', t))


def stems_now(S):
    exc = sorted(S['REC']._edl(l) for l, _, _ in S['REC'].STEMX)
    m = re.search(r'live uses\s*:\s*(\d+)', S['bt_now'])
    return m is not None and int(m.group(1)) == 3 and live_lines(S['bt_now']) == exc == live_lines(S['escan']) \
        and S['hj'].get('H28c') == 'HELD'


def stemsx_ok(S):
    keep = aligned(S)
    c = bm_cut(S)
    if keep is None or c is None:
        return False
    bm = NL.join(S['ed'][c:])
    return all(w in keep[ln - 1] and keep[ln - 1] == S['cur'][ln - 1] and S['ed'][S['REC']._edl(ln) - 1] == S['cur'][ln - 1]
               and ('| :%d | %s (banned stem, excepted) | %s |' % (S['REC']._edl(ln), w, why)) in bm for ln, w, why in S['REC'].STEMX)


def ceiling_ok(S):
    hits = [(i, l) for i, l in enumerate(S['ed'], 1) for m in S['REC'].CEILING.finditer(l)]
    return len(hits) == len(S['hj'].get('hits', [None])) == 3 and all(l.startswith('| :') and S['REC'].CEIL_RECORD in l for i, l in hits) \
        and S['hj'].get('beyond') == 0


def ceilcorr_ok(S):
    keep = aligned(S)
    c = bm_cut(S)
    if keep is None or c is None:
        return False
    bm = NL.join(S['ed'][c:])
    return len(S['REC'].CEILS) == 3 and all(new in keep[ln - 1] and old not in keep[ln - 1] and old in S['cur'][ln - 1]
                                            and ('| :%d | %s %s | %s |' % (S['REC']._edl(ln), S['REC'].CEIL_RECORD, old, new)) in bm
                                            for ln, old, new in S['REC'].CEILS) \
        and '`h2_sign_iff_rh`, SIDE-explicit-formula v0.2 = `5c72cad`' in keep[32]


def version_ok(S):
    v = S['REC'].VERSION
    return len(S['ed']) > 20 and S['ed'][v[0] - 1] == v[1] == '*v0.2.4 — 2026-10-01*' and S['ed'][v[0]] == '' \
        and S['ed'][v[0] + 1] == S['cur'][v[0] - 1] == '*v0.2.3 — 2026-07-19*'


def arith_ok(S):
    c = bm_cut(S)
    pin = S['REC'].PIN['arith_limit_nonneg_iff_rh']
    at = [i for i, l in enumerate(S['ed'][:c or 0], 1) if '`arith_limit_nonneg_iff_rh`' in l and pin in l]
    return bool(at) and page_pin_ok(S, 'arith_limit_nonneg_iff_rh', pin) and at == S['hj'].get('arith_limit_at')


def backmatter_ok(S):
    c = bm_cut(S)
    if c is None:
        return False
    bm = S['ed'][c:]
    return all(h in bm for h in ('### Removals', '### Stem uses excepted', '### Ceiling corrections', '### Placement', '### Correspondence')) \
        and any(l.startswith('None: every one of the 13 work-list rows') for l in bm)


CELLRX = re.compile(r'\| cited at :([0-9, :]+) of this edition \|$')


def repin_final_ok(S):
    """### the edition's own Correspondence column read against its final body: every row cites exactly the lines that carry it."""
    c = bm_cut(S)
    if c is None:
        return False
    body = S['ed'][:c]
    PIN = S['REC'].PIN
    rows = 0
    for l in S['ed'][c:]:
        m, mb, cell = re.match(r'^\| `SIDEExplicitFormula\.\w+\.(\w+)` \|', l), re.match(r'^\| `data/b558_cp1b\.txt` :(\d+) \|', l), CELLRX.search(l)
        if not cell:
            continue
        got = [int(x) for x in re.findall(r'\d+', cell.group(1))]
        if m and m.group(1) in PIN:
            want = [k for k, x in enumerate(body, 1) if ('`%s`' % m.group(1)) in x and PIN[m.group(1)] in x]
        elif mb:
            want = [k for k, x in enumerate(body, 1) if re.search(r'relay `data/b558_cp1b\.txt` :(?:\d+, :)?%s\b' % mb.group(1), x)]
        else:
            continue
        rows += 1
        if got != want or not want:
            return False
    return rows == len(PIN) + 12


def offset_ok(S):
    first = S['etxt'].split(NL)[0]
    return first.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3): +2 from :17') and S['etxt'].count('### OFFSET FROM') == 1 \
        and all(d['ed_line'] == d['line'] + 2 for d in S['ej'].get('diff', [])) and len(S['ej'].get('diff', [])) == 13 \
        and all(('v0.2.3 :%d -> v0.2.4 :%d' % (d['line'], d['line'] + 2)) in S['etxt'] for d in S['ej']['diff'])


def nums(l):
    m = CELLRX.search(l)
    return [int(x) for x in re.findall(r'\d+', m.group(1))] if m else None


def paths_ok(S):
    a, b = S['p7_pre'].split(NL), S['p7_now'].split(NL)
    if len(a) != len(b):
        return False
    dif = [i for i in range(len(a)) if a[i] != b[i]]
    return len(dif) == 6 and all(a[i].startswith('| `SIDEExplicitFormula.') and nums(a[i]) and nums(b[i]) == [x + 2 for x in nums(a[i])]
                                 and min(nums(a[i])) > 19 and CELLRX.sub('', a[i]) == CELLRX.sub('', b[i]) for i in dif)


def clause_ok(S, k, text):
    return oline(S, S['c1'].get('lines', {}).get(k)).startswith(S['c1'].get('heads', {}).get(k, '\0')) and text in oline(S, S['c1']['lines'][k])


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R190) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b579`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b579' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b580 -- x'])),
    ('G-R190-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R190) END' in S['ferry'] and S['ot'].count('**(R190) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R190) ratified', '(R190) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('ADDITIVE_MULTIPLICATIVE_CONSPIRACY.txt @', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md @',
                                                                               'THE_CLAUSE_AND_ITS_COMPILED_FACES.md @', 'b558_cp1b.txt @',
                                                                               'OPEN_TRAILS.md @', 'FINDINGS.md @', 'banned_terms.py @',
                                                                               'b578_edition_PATHS.txt @', 'PATHS_TO_THE_CRITICAL_LINE_v0_7.md @',
                                                                               'FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md @', 'Module1.lean @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay c066701f`s files', lambda S: S['pushout'][0] == ['data/b579_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b579') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b579'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-H28B-FINAL', 'OPEN_TRAILS at the banked line', lambda S: clause_ok(S, 'h28b', S['REC'].H28B_TEXT) and '(:11864)' in oline(S, S['c1']['lines']['h28b']),
     lambda S: put(S, 'c1', dict(S['c1'], lines=dict(S['c1']['lines'], h28b=1)))),
    ('G-REPIN-CLAUSE', 'OPEN_TRAILS at the banked line', lambda S: clause_ok(S, 'repin', S['REC'].REPIN_TEXT) and '+2 from :19' in oline(S, S['c1']['lines']['repin']),
     lambda S: put(S, 'c1', dict(S['c1'], lines=dict(S['c1']['lines'], repin=1)))),
    ('G-EXCEPTION-CLAUSE', 'OPEN_TRAILS at the banked line', lambda S: clause_ok(S, 'exc', S['REC'].EXC_TEXT) and ':231' in oline(S, S['c1']['lines']['exc']),
     lambda S: put(S, 'c1', dict(S['c1'], lines=dict(S['c1']['lines'], exc=1)))),
    ('G-NAVIGATOR-WORDING-LINE', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['c1']['lines'].get('nav')).startswith(S['c1']['heads']['nav'])
     and '(:11914)' in oline(S, S['c1']['lines']['nav']) and 'is recorded as the navigator’s' in oline(S, S['c1']['lines']['nav']),
     lambda S: put(S, 'c1', dict(S['c1'], lines=dict(S['c1']['lines'], nav=1)))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['c1']['lines'].get('weight')).startswith(S['c1']['heads']['weight'])
     and 'b579 AT ITS WEIGHT' in fline(S, S['c1']['lines']['weight']) and '(:6500)' in fline(S, S['c1']['lines']['weight']),
     lambda S: put(S, 'c1', dict(S['c1'], lines=dict(S['c1']['lines'], weight=1)))),
    ('G-PATHS-REPINNED', 'PATHS v0.7 now against its blob at a1de9dc, line by line', lambda S: paths_ok(S),
     lambda S: put(S, 'p7_now', S['p7_now'].replace('| cited at :61,', '| cited at :59,', 1))),
    ('G-B578-BANK-HEADED', 'relay data/b578_edition_PATHS.txt against its blob at c34ef391', lambda S: S['b578_now'] == S['REC'].B578_HEAD + NL + S['b578_pre']
     and '+2 from :19' in S['REC'].B578_HEAD, lambda S: put(S, 'b578_now', S['b578_pre'])),
    ('G-FOUNDATIONS-CHECKED', 'FOUNDATIONS v0.2.5 against its blob and the re-pin bank', lambda S: S['f5_pre'] is not None and S['f5_now'] == S['f5_pre']
     and S['repj'].get('foundations_moved') is False and len(S['repj'].get('foundations', [])) == 14
     and all(r['old'] == r['new'] for r in S['repj']['foundations']), lambda S: put(S, 'f5_now', (S['f5_now'] or b'') + b'x')),
    ('G-HOUSEKEEPING-ALONE', 'the two housekeeping commits` file lists', lambda S: S['hk'].get('relay') == [['data/' + S['REC'].B578_BANK]]
     and S['hk'].get('pp') == [[S['REC'].PATHS7]], lambda S: put(S, 'hk', dict(S['hk'], pp=[[S['REC'].PATHS7, 'FINDINGS.md']]))),
    ('G-EDITION-BESIDE', 'the edition file and the current version`s blob', lambda S: S['ed_exists'] and len(S['ed']) > len(S['cur'])
     and S['cur_head_blob'] == S['ej'].get('cur_blob') and S['cur_work_blob'] == S['ej'].get('cur_blob')
     and os.path.dirname(S['REC'].ED) == os.path.dirname(S['REC'].CUR), lambda S: put(S, 'cur_work_blob', '0' * 40)),
    ('G-EDITION-CARRIES', 'the edition against the current version, line by line', lambda S: carries(S),
     lambda S: put(S, 'ed', [l + ('x' if i == 200 else '') for i, l in enumerate(S['ed'])])),
    ('G-EDITION-REWRITES', 'the 13 rows` sentences against the edition`s aligned lines', lambda S: rewrites_ok(S),
     lambda S: put(S, 'ed', [S['cur'][236] if i == 238 else l for i, l in enumerate(S['ed'])])),
    ('G-H28A-CITES', 'each rewrite against the zeta page`s own nodes and the banks', lambda S: h28a_ok(S),
     lambda S: put(S, 'ej', dict(S['ej'], diff=[dict(d, new=d['new'].replace('e5a5a83', '0000000').replace('relay `data/b558_cp1b.txt`', 'relay `data/nope.txt`'))
                                                 for d in S['ej'].get('diff', [])]))),
    ('G-H28B-COUNTED', 'the counts recomputed from both texts', lambda S: counts_ok(S), lambda S: put(S, 'hj', dict(S['hj'], body_dn=3))),
    ('G-H28C-STEMS', 'banned_terms.py --new run afresh on the edition', lambda S: stems_now(S),
     lambda S: put(S, 'bt_now', S['bt_now'] + '\n   X.md :100    ### LIVE USE -- CORRECT BEFORE SHIPPING\n')),
    ('G-STEMS-EXCEPTED', 'the three excepted lines and their back-matter rows', lambda S: stemsx_ok(S),
     lambda S: put(S, 'ed', [l for l in S['ed'] if '(banned stem, excepted) | a published title (Zhang 2014)' not in l])),
    ('G-CEILING-READ', 'the ceiling phrases recomputed over the edition', lambda S: ceiling_ok(S),
     lambda S: put(S, 'ed', S['ed'] + ['RH ' + 'proved.'])),
    ('G-CEILING-CORRECTIONS', 'the edition`s aligned lines and its back matter', lambda S: ceilcorr_ok(S),
     lambda S: put(S, 'ed', [l.replace('— RH-core;', '— RH ' + 'proof core;') for l in S['ed']])),
    ('G-VERSION-LINE', 'the edition`s head against the current version`s', lambda S: version_ok(S),
     lambda S: put(S, 'ed', [l for l in S['ed'] if l != '*v0.2.4 — 2026-10-01*'])),
    ('G-ARITH-LIMIT-CITED', 'the edition`s body against the zeta page`s node 21', lambda S: arith_ok(S),
     lambda S: put(S, 'ed', [l.replace('`arith_limit_nonneg_iff_rh`', '`arith_limit`') for l in S['ed']])),
    ('G-BACK-MATTER', 'the edition`s back matter', lambda S: backmatter_ok(S), lambda S: put(S, 'ed', [l for l in S['ed'] if l != '### Stem uses excepted'])),
    ('G-STATUS-CELLS', 'every Status column of the edition, cell by cell', lambda S: S['REC']._status_blanks(S['ed']) == [],
     lambda S: put(S, 'ed', S['ed'] + ['', '| a | Status |', '|:--|:--|', '| x |  |'])),
    ('G-REPIN-FINAL', 'the edition`s Correspondence column against its final body', lambda S: repin_final_ok(S),
     lambda S: put(S, 'ed', [l.replace('| cited at :', '| cited at :1, :', 1) if l.startswith('| `SIDEExplicitFormula.') else l for l in S['ed']])),
    ('G-OFFSET-LINE', 'the diff bank`s head and its rows', lambda S: offset_ok(S),
     lambda S: put(S, 'etxt', NL.join(S['etxt'].split(NL)[1:]))),
    ('G-DIFF-BANKED', 'the diff bank', lambda S: S['etxt'].count('      v0.2.4 : ') == 13 and S['etxt'].count('      v0.2.3 : ') == 13
     and '### ### **H28a ' in S['etxt'] and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in S['etxt'],
     lambda S: put(S, 'etxt', S['etxt'].replace('      v0.2.4 : ', '      v0.2.4: ', 1))),
    ('G-COVERAGE-BANKED', 'the edition json`s rows against the bank`s N1 line', lambda S: len(S['ej'].get('diff', [])) == 13
     and all(d['reading'] in (0, 2) for d in S['ej']['diff']) and sum(1 for d in S['ej']['diff'] if d['reading']) == S['hj'].get('covered')
     and ('the seat`s hand-read: %d of 13 rows' % S['hj'].get('covered')) in S['etxt'] and '(a) the prime side against the pole-plus-archimedean assembly -- NO OBJECT HERE' in S['etxt'],
     lambda S: put(S, 'hj', dict(S['hj'], covered=13))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(S['REC'].TITLE_HEAD)
     and 'its RH-side twin cited to the Li and arithmetic-limit faces' in fline(S, S['fj'].get('entry_line')),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b580 — lane three, act eight under (R190)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'CP-7 act six, b581' in trail(S) and 'THE_UNCONDITIONAL_SURROUND' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('CP-7 act six, b581', 'x'))),
    ('G-NAVIGATOR-READING-RECORDED', 'this act`s trail record and FINDINGS entry', lambda S: ('**Recorded as the navigator’s:** ' + S['REC'].NAV_READING) in trail(S)
     and ('**A reading, the navigator’s:** ' + S['REC'].NAV_READING) in S['find'] and 'BALANCE_AND_POSITIVITY’s edition' in S['REC'].NAV_READING,
     lambda S: put(S, 'ot', S['ot'].replace('**Recorded as the navigator’s:**', 'x'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{PAGE: ((S['pages'][PAGE][0] or b'') + b'x', S['pages'][PAGE][1])}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff', lambda S: S['kmain'] == V015
     and S['kcur'] == 'main' and S['kdirty'] == '' and all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] == [],
     lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b580_record.py'): S['tooltext'].get(os.path.join(T, 'b580_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: not [f for f, t in S['tooltext'].items()
                                                                        if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-UNTOUCHED', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == sorted([S['REC'].ED, S['REC'].PATHS7])
     and S['cur_head_blob'] == S['ej'].get('cur_blob'), lambda S: put(S, 'keystone_changes', sorted(S['keystone_changes'] + [S['REC'].CUR]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at c34ef391, by blob id, but the one ruled headed', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b579_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', S['REC'].ED, S['REC'].PATHS7]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
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
                                                                          and "startswith('b580')" in S['suite'] and "data/b580_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b580')", ''))),
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
    rec('b580 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b580_checks_postpush.txt' if pushed else 'b580_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b580_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
