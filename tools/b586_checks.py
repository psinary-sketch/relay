# -*- coding: utf-8 -*-
"""b586_checks.py -- THE SUITE OF b586, UNDER (R196): CP-7 ACT ELEVEN, THE EDITION OF ENUMERA; THE SCANNER TAUGHT THE EXCEPTIONS; THE CENSUS.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b586_checks.txt before the push and data/b586_checks_postpush.txt after
### it. ### The harness is b568's to b585's, carried; the arms are b586's.
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
FACE = os.path.join(D, 'b586_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='b75a56c5', pp='7e9b771', gs='8c392fe')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}
STEPZERO = '05087ba9'
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b586')
            and 'data/b586_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b586_record as REC
    import b558_record as CP
    import banned_terms as BT
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b586_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b586_') and f.endswith('.py'))
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
              if l.strip() and l.split(' ', 1)[1].startswith('b586 housekeeping')]
        hk[key] = [files_of(repo, c) for c in cs]
    S = dict(
        REC=REC, CP=CP, BT=BT, face=face, ferry=rd('b586_ferry.txt'), scan=rd('b586_ferry_scan.txt'), cens=rd('b586_census_stepzero.txt'),
        fcens=rd('b586_faces_census_stepzero.txt'), pins0=rd('b586_pins_stepzero.txt'), procs=rd('b586_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b585_closing.txt'), reads=rd('b586_reads.txt'), branches=rd('b586_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), c1=jl('b586_c1_lines.json'),
        cur=cur, ed=ed, ed_exists=os.path.exists(edp), ej=jl('b586_edition.json'), hj=jl('b586_h28.json'), etxt=rd('b586_edition_ENUMERA.txt'),
        escan=rd('b586_edition_termscan.txt'), bt_now=bt,
        cur_head_blob=gs(PP, 'rev-parse', 'HEAD:' + REC.CUR), cur_work_blob=gs(PP, 'hash-object', REC.CUR),
        page=lines_of(blob(PP, '192077f:' + PAGE)),
        rows=[r for r in json.load(io.open(os.path.join(D, 'b558_cp1b.json'), encoding='utf-8'))['rows']
              if r['doc'] == 'ENUMERA' and r['verdict'] == 'MOVED-IN-MEANING'],
        hk=hk, order=jl('b586_order.json'), corr=jl('b586_corroboration.json'), corr_txt=rd('b586_corroboration.txt'), scj=jl('b586_scanner.json'),
        fj=jl('b586_findings.json'), tj=jl('b586_trail.json'),
        sc=jl('b586_scores.json'), desk=rd('b586_desk_notes.txt'),
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
        push_lists={r: gs(r, 'branch', '--list', 'push-b585*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b586_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b586_mustnotexist.txt')), table_changed=None,
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
    import contextlib
    REC = S['REC']
    X = {}
    cs = []
    for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD', '--', 'tools/banned_terms.py').split(NL):
        if l.strip():
            sha, ct, subj = l.split(' ', 2)
            cs.append((sha, files_of(ROOT, sha), subj, int(ct)))
    X['scanner_commits'] = cs
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    t = subprocess.run([sys.executable, os.path.join(T, 'test_banned_terms_backmatter.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=env)
    X['test'] = (t.returncode, t.stdout)
    X['rescan'] = {rel: subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', os.path.join(PP, *rel.split('/'))],
                                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=env).stdout
                   for rel in (REC.INDEX19, REC.AMC24)}
    notag = os.path.join(PP, *REC.CUR.split('/'))
    now = subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', notag], capture_output=True, text=True,
                         encoding='utf-8', errors='replace', env=env).stdout
    parent_src = blob(ROOT, '%s^:tools/banned_terms.py' % (cs[0][0] if cs else 'HEAD'))
    buf = io.StringIO()
    ns = {'__name__': 'banned_terms_parent', '__file__': os.path.join(T, 'banned_terms.py')}
    try:
        exec(compile(parent_src.decode('utf-8'), 'banned_terms_parent', 'exec'), ns)
        with contextlib.redirect_stdout(buf):
            ns['main'](['--new', notag])
    except Exception as e:
        buf.write('### PARENT RAISED %s' % e)
    m1 = re.search(r'live uses\s*:\s*(\d+)', now)
    m2 = re.search(r'live uses\s*:\s*(\d+)', buf.getvalue())
    tags = [l for l in read(notag).split(NL) if S['BT'].BM_TAG.match(l)]
    X['notag'] = (int(m1.group(1)) if m1 else None, int(m2.group(1)) if m2 else None, len(tags))
    forms = {}
    for r in (S['corr'].get('rows') or []):
        text = cr0(blob(PP, '%s:%s' % (PRE['pp'], r['path']))).decode('utf-8', 'replace').split(NL)
        tl = re.match(r'^:(\d+)$', r['tier'] or '')
        body = text[:int(tl.group(1)) - 1] if tl else text
        corr_rows, other = REC._term_rows(body)
        forms[r['name']] = 'CORRESPONDENCE' if corr_rows else 'OTHER' if other else 'NONE'
    X['forms_now'] = forms
    paths = sorted(set([p for _, p, _ in REC._roster() if p != 'FINDINGS.md'] + ['day1/A_Place_to_Stand.md'] + list(REC.EDITIONS.values())))
    X['roster_n'] = len(paths)
    X['roster_dirty'] = [p for p in paths if gs(PP, 'hash-object', p) != gs(PP, 'rev-parse', '%s:%s' % (PRE['pp'], p))]
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
    i = t.find('### b586 — lane three, act fourteen under (R196)')
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


# ### the edition read on its own: its body is the current version line for line, the version line and the blank after it taken
# ### out, the back matter cut at its tag
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
    if len(body) < v[0] + 1 or body[v[0] - 1] != v[1] or body[v[0]] != '':
        return None
    drop = {v[0] - 1, v[0]}
    return [l for n, l in enumerate(body) if n not in drop]


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
    if keep is None or len(keep) != len(S['cur']) or len(S['rows']) != 9:
        return False
    return all(r['sentence'] not in segs(S, keep[r['line'] - 1]) for r in S['rows']) and \
        all(len(segs(S, keep[r['line'] - 1])) == len(segs(S, S['cur'][r['line'] - 1])) for r in S['rows'])


def page_pin_ok(S, name, pin):
    page = S['page']
    hit = [l for l in page if ('`%s`' % name) in l or ('.%s`' % name) in l]
    if not hit:
        return False
    node = [l for l in hit if re.match(r'^\d+\. `', l)]
    plain = pin.replace('`', '')
    if node:
        return any(plain in l for l in node)
    return len(page) > 2 and plain in page[2].replace('`', '')


def h28a_ok(S):
    edtxt = NL.join(S['ed'])
    PIN = S['REC'].PIN
    diff = S['ej'].get('diff', [])
    if len(diff) != 9:
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
            and allowed == S['hj'].get('allowed') == 1 and S['hj'].get('H28b') == ('HELD' if abs(n_body - n_cur) <= allowed else 'REFUTED'))


def scan_fields(out):
    live = re.search(r'live uses\s*:\s*(\d+)', out or '')
    exc = re.search(r'excepted \(back matter\): names (\d+) ; carried-by-history (\d+)', out or '')
    v = re.search(r'^\s*VERDICT\s*: (.+)$', out or '', re.M)
    return (int(live.group(1)) if live else None, (int(exc.group(1)), int(exc.group(2))) if exc else None, v.group(1).strip() if v else None)


def stems_now(S):
    live, exc, v = scan_fields(S['bt_now'])
    return live == 0 and exc == (S['REC'].NAMES_COUNT, 0) and v == 'CLEAN' and S['hj'].get('H28c') == 'HELD' \
        and S['hj'].get('live') == 0 and S['hj'].get('excepted_names') == S['REC'].NAMES_COUNT == 7


def ceiling_ok(S):
    REC = S['REC']
    c = bm_cut(S)
    if c is None:
        return False
    carried = set(REC._edl(n) for n in REC.CARRIED)
    beyond, n = 0, 0
    for i, l in enumerate(S['ed'], 1):
        for m in REC.CEILING.finditer(l):
            n += 1
            rec_ = i > c + 1 and l.startswith('| :') and (REC.CEIL_RECORD in l or REC.CARRY_RECORD in l)
            car = i <= c and i in carried
            if not (rec_ or car):
                beyond += 1
    return beyond == 0 and n == len(S['hj'].get('hits', [None])) and S['hj'].get('beyond') == 0


def corr_ok(S, rows, rec, tail):
    keep = aligned(S)
    c = bm_cut(S)
    if keep is None or c is None:
        return False
    bm = NL.join(S['ed'][c:])
    return all(new in keep[ln - 1] and keep[ln - 1].count(old) == new.count(old) and old in S['cur'][ln - 1]
               and ('| :%d | %s %s%s | %s |' % (S['REC']._edl(ln), rec, old, tail, new)) in bm for ln, old, new in rows)


def carried_ok(S):
    keep = aligned(S)
    c = bm_cut(S)
    if keep is None or c is None:
        return False
    REC = S['REC']
    bm = S['ed'][c:]
    # ### a carried line may also hold a rewritten sentence (:20); what carries is each ceiling-pattern hit it had
    return sorted(REC.CARRIED) == [18, 20, 49, 872, 892, 898] \
        and all(all(keep[n - 1].count(h) == S['cur'][n - 1].count(h) for h in REC.CEILING.findall(S['cur'][n - 1])) for n in REC.CARRIED) \
        and sum(len(REC.CEILING.findall(S['cur'][n - 1])) for n in REC.CARRIED) == 3 \
        and all(any(l.startswith('| :%d | %s ' % (REC._edl(n), REC.CARRY_RECORD)) for l in bm) for n in REC.CARRIED) and ceiling_ok(S)


def names_ok(S):
    keep = aligned(S)
    c = bm_cut(S)
    if keep is None or c is None:
        return False
    REC = S['REC']
    bm = S['ed'][c:]
    n = sum(len(S['BT'].PAT.findall(keep[k - 1])) for k in REC.NAMES)
    return n == REC.NAMES_COUNT == 7 and all(S['BT'].PAT.findall(keep[k - 1]) == S['BT'].PAT.findall(S['cur'][k - 1]) for k in REC.NAMES) \
        and all(('| :%d | excepted, the object’s own name (an item label of the CR document) |' % REC._edl(k)) in bm for k in REC.NAMES)


def fact_read_ok(S):
    pins = [l for l in S['reads'].split(NL) if re.match(r'^    SIDE-[a-z-]+ v[0-9.]+ : cited ', l)]
    return len(pins) == 4 and all(l.endswith('; AGREE') for l in pins) and '### DIFFER' not in S['reads'] \
        and 'theorem formation_count : 2 + 3 + 2 + 0 = 7 := SIDEKernel.formation' in S['reads'] and S['REC'].FACTS == []


def oline_pre(S, n):
    ls = cr0(S['ot_pre']).decode('utf-8', 'replace').split(NL)
    return ls[n - 1] if 0 < n <= len(ls) else ''


def tier_ok(S):
    keep = aligned(S)
    REC = S['REC']
    return keep is not None and len(S['cur']) == 1065 and keep[1057:1065] == S['cur'][1057:1065] \
        and S['cur'][1057].startswith('#### THE CASCADE, ACT ELEVEN') and S['ed'][REC._edl(1058) - 1] == S['cur'][1057]


def version_ok(S):
    v = S['REC'].VERSION
    return len(S['ed']) > 22 and S['ed'][v[0] - 1] == v[1] == '**Version 1.6** | 2026-10-01' and S['ed'][v[0]] == '' \
        and S['ed'][v[0] + 1] == S['cur'][v[0] - 1] and S['cur'][v[0] - 1].startswith('**Version 1.5** | **51 Findings**')


BM_HEADS = ('### Removals', '### Credit lines', '### Stem corrections', '### Names excepted', '### Ceiling corrections',
            '### Ceiling-shaped sentences read and carried', '### Fact corrections', '### The navigator’s expectations of `(R196)`(5)',
            '### Placement', '### Correspondence')


def backmatter_ok(S):
    c = bm_cut(S)
    if c is None:
        return False
    bm = S['ed'][c:]
    return all(h in bm for h in BM_HEADS) and any(l.startswith('None: every one of the 9 work-list rows') for l in bm)


CELLRX = re.compile(r'\| cited at :([0-9, :]+) of this edition \|$')


def repin_final_ok(S):
    c = bm_cut(S)
    if c is None:
        return False
    body = S['ed'][:c]
    PIN = S['REC'].PIN
    rows = 0
    for l in S['ed'][c:]:
        m, mb, cell = re.match(r'^\| `SIDEExplicitFormula\.\w+\.(\w+)` \|', l), re.match(r'^\| `data/([\w.]+)` :(\d+) \|', l), CELLRX.search(l)
        if not cell:
            continue
        got = [int(x) for x in re.findall(r'\d+', cell.group(1))]
        if m and m.group(1) in PIN:
            want = [k for k, x in enumerate(body, 1) if ('`%s`' % m.group(1)) in x and PIN[m.group(1)] in x]
        elif mb:
            want = [k for k, x in enumerate(body, 1) if ('relay `data/%s` :%s' % (mb.group(1), mb.group(2))) in x]
        else:
            continue
        rows += 1
        if got != want or not want:
            return False
    return rows == len(PIN) + len(S['REC'].BANKROWS)


def offset_ok(S):
    first = S['etxt'].split(NL)[0]
    d = S['ej'].get('diff', [])
    return first.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3): +2 from :11 (the Version 1.6') and S['etxt'].count('### OFFSET FROM') == 1 \
        and len(d) == 9 and all(x['ed_line'] == S['REC']._edl(x['line']) and S['ed'][x['ed_line'] - 1].find(x['new'][:60]) >= 0 for x in d) \
        and all(('v1.5 :%d -> v1.6 :%d' % (x['line'], x['ed_line'])) in S['etxt'] for x in d)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 14]) if e else ''
    return fline(S, e).startswith(S['REC'].TITLE_HEAD) and '**The scanner**' in tail and '**The corroboration census**' in tail \
        and '**The edition**' in tail


def scanner_commit_ok(S):
    cs = S['scanner_commits']
    return len(cs) == 1 and cs[0][1] == ['tools/banned_terms.py', 'tools/test_banned_terms_backmatter.py'] \
        and cs[0][2].startswith('b586 Component 1 under (R196)(2)') and S['lock_epoch'] is not None and cs[0][3] > S['lock_epoch']


def rescans_ok(S):
    want = {S['REC'].INDEX19: (0, (13, 2), 'CLEAN'), S['REC'].AMC24: (0, (3, 0), 'CLEAN')}
    bank = S['scj'].get('rescans', {})
    return all(scan_fields(S['rescan'].get(k)) == w for k, w in want.items()) \
        and all(bank.get(k, {}).get('verdict') == 'CLEAN' and bank.get(k, {}).get('live') == 0 for k in want) \
        and 'MUTANT NOT CLEAN' in S['scj'].get('test_out', '')


def census_rows_ok(S):
    C = S['corr']
    rows = C.get('rows', [])
    if len(rows) != 22 or [r['name'] for r in rows] != [x[0] for x in S['REC']._roster()]:
        return False
    forms = S['forms_now']
    return all(r['form'] == forms.get(r['name']) for r in rows) and S['corr_txt'].count('\n| ') == 23 \
        and dict((r['name'], r['b450']) for r in rows if r['b450']) == {'TECHNE_TOOLKIT': 'OPEN_TRAILS :6586', 'E_DIFFICULTY_THEOREM': 'OPEN_TRAILS :6587'} \
        and forms.get('TECHNE_TOOLKIT') == 'CORRESPONDENCE' and forms.get('ENUMERA') == 'NONE'


def census_lists_ok(S):
    C = S['corr']
    rows = C.get('rows', [])
    since = C.get('since_b566', [])
    return C.get('no_table') == [r['name'] for r in rows if r['form'] == 'NONE'] \
        and C.get('unread') == [r['name'] for r in rows if r['form'] != 'NONE'] \
        and ('### THE DOCUMENTS WITH NO TABLE NAMING A TERMINAL (%d): %s' % (len(C['no_table']), C['no_table'])) in S['corr_txt'] \
        and ('### THE DOCUMENTS WHOSE TABLES HAVE NOT BEEN RE-READ BY CONSTELLATION MODE SINCE b566 (%d)' % len(C['unread'])) in S['corr_txt'] \
        and since and all('rowgen.diff IMPORTED' in rd(x.split(':', 1)[1]) and 'constellation mode' not in rd(x.split(':', 1)[1]).lower() for x in since) \
        and all(r['constellation_since_b566'] == 'none' for r in rows)


def order_ok(S):
    O = S['order']
    l = oline(S, O.get('line'))
    return l.startswith(O.get('head', '\0')) and '(:11417)' in l and '`(R196)`(4)' in l \
        and "then CP-6; then CP-8 with the monograph's ceiling uses." in l and 'stay priced for the author' in l \
        and oline_pre(S, 11417).startswith('> LANE THREE — THE CLARIFIED LAYER')


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R196) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b585`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b585' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b586 -- x'])),
    ('G-R196-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R196) END' in S['ferry'] and S['ot'].count('**(R196) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R196) ratified', '(R196) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('ENUMERA.txt @', 'ENUMERA.md @', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md @', 'b538_census.json @', 'b558_cp1b.txt @', 'banned_terms.py @', 'INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md @', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md @', 'OPEN_TRAILS.md @', 'FINDINGS.md @', '2026-08-09-correspondence-regrade-sitting-1.md @', 'b566_rowgen.txt @', 'b585_closing_push_out.txt @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 05087ba9`s files', lambda S: S['pushout'][0] == ['data/b585_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b585') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b585'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['c1']['lines'].get('weight')).startswith(S['c1']['heads']['weight'])
     and 'b585 AT ITS WEIGHT' in fline(S, S['c1']['lines']['weight']) and '(:6630)' in fline(S, S['c1']['lines']['weight']),
     lambda S: put(S, 'c1', dict(S['c1'], lines=dict(S['c1']['lines'], weight=1)))),
    ('G-SCANNER-ALONE', 'relay`s commits since b75a56c5 touching tools/banned_terms.py', lambda S: scanner_commit_ok(S),
     lambda S: put(S, 'scanner_commits', [(c[0], c[1] + ['data/x.txt'], c[2], c[3]) for c in S['scanner_commits']])),
    ('G-SCANNER-TEST', 'the test run afresh', lambda S: S['test'][0] == 0 and 'MUTANT NOT CLEAN' in S['test'][1] and 'TEST HELD' in S['test'][1]
     and S['scj'].get('test_exit') == 0, lambda S: put(S, 'test', (1, S['test'][1]))),
    ('G-SCANNER-RESCANS', 'the edited scanner run afresh on INDEX v0.19 and AMC v0.2.4, and the bank', lambda S: rescans_ok(S),
     lambda S: put(S, 'rescan', dict(S['rescan'], **{S['REC'].AMC24: S['rescan'][S['REC'].AMC24].replace('live uses        : 0', 'live uses        : 2')}))),
    ('G-SCANNER-NOTAG-UNCHANGED', 'the edited and the parent scanner on a file with no back-matter tag', lambda S: S['notag'][0] == S['notag'][1] == 13
     and S['notag'][2] == 0, lambda S: put(S, 'notag', (S['notag'][0], 12, S['notag'][2]))),
    ('G-CENSUS-ROWS', 'the census json against the roster and the forms recomputed from each text', lambda S: census_rows_ok(S),
     lambda S: put(S, 'corr', dict(S['corr'], rows=[dict(r, form='NONE') if r['name'] == 'TECHNE_TOOLKIT' else r for r in S['corr'].get('rows', [])]))),
    ('G-CENSUS-LISTS', 'the census`s two lists and the since-b566 banks', lambda S: census_lists_ok(S),
     lambda S: put(S, 'corr', dict(S['corr'], no_table=S['corr'].get('no_table', []) + ['TECHNE_TOOLKIT']))),
    ('G-CENSUS-NO-EDIT', 'every roster document at the worktree against its pre-act blob', lambda S: S['roster_dirty'] == [] and S['roster_n'] == 30,
     lambda S: put(S, 'roster_dirty', ['phase1.5/method/TECHNE_TOOLKIT.md'])),
    ('G-ORDER-LINE', 'OPEN_TRAILS at the banked order line', lambda S: order_ok(S), lambda S: put(S, 'order', dict(S['order'], line=1))),
    ('G-NO-HOUSEKEEPING', 'both logs since the pre-act heads', lambda S: S['hk'].get('pp') == [] and S['hk'].get('relay') == [],
     lambda S: put(S, 'hk', dict(S['hk'], pp=[['FINDINGS.md']]))),
    ('G-EDITION-BESIDE', 'the edition file and the current version`s blob', lambda S: S['ed_exists'] and len(S['ed']) > len(S['cur'])
     and S['cur_head_blob'] == S['ej'].get('cur_blob') and S['cur_work_blob'] == S['ej'].get('cur_blob')
     and os.path.dirname(S['REC'].ED) == os.path.dirname(S['REC'].CUR), lambda S: put(S, 'cur_work_blob', '0' * 40)),
    ('G-EDITION-CARRIES', 'the edition against the current version, line by line', lambda S: carries(S),
     lambda S: put(S, 'ed', [l + ('x' if i == 100 else '') for i, l in enumerate(S['ed'])])),
    ('G-EDITION-REWRITES', 'the 9 rows` sentences against the edition`s aligned lines', lambda S: rewrites_ok(S),
     lambda S: put(S, 'ed', [S['cur'][931] if l.startswith(S['cur'][931][:40]) else l for l in S['ed']])),
    ('G-H28A-CITES', 'each rewrite against the zeta page`s own lines and the banks', lambda S: h28a_ok(S),
     lambda S: put(S, 'ej', dict(S['ej'], diff=[dict(d, new=d['new'].replace('5c72cad', '0000000').replace('baed4df', '0000000').replace('19b7d1e', '0000000')
                                                    .replace('e5a5a83', '0000000').replace('relay `data/b538_census.json`', 'relay `data/nope.txt`')) for d in S['ej'].get('diff', [])]))),
    ('G-H28B-COUNTED', 'the counts recomputed from both texts', lambda S: counts_ok(S), lambda S: put(S, 'hj', dict(S['hj'], body_dn=2))),
    ('G-H28C-STEMS', 'the edited banned_terms.py --new run afresh on the edition', lambda S: stems_now(S),
     lambda S: put(S, 'bt_now', S['bt_now'].replace('live uses        : 0', 'live uses        : 1'))),
    ('G-CEILING-CORRECTED', 'the edition`s aligned lines and its correction rows', lambda S: corr_ok(S, S['REC'].CEILS, S['REC'].CEIL_RECORD, '')
     and len(S['REC'].CEILS) == 8, lambda S: put(S, 'ed', [l.replace('THE RH ARGUMENT IS SIMPLE', 'RH IS SIMPLE') for l in S['ed']])),
    ('G-CEILING-CARRIED', 'the ceiling phrases recomputed over the edition and the carried rows', lambda S: carried_ok(S),
     lambda S: put(S, 'ed', [l for l in S['ed'] if not l.startswith('| :%d | ceiling read, carried:' % S['REC']._edl(872))])),
    ('G-STEM-CORRECTIONS', 'the edition`s aligned lines and its back matter', lambda S: corr_ok(S, S['REC'].STEMS, S['REC'].STEM_RECORD, ' (banned stem; correction record)')
     and len(S['REC'].STEMS) == 6,
     lambda S: put(S, 'ed', [l.replace('the structural distance between identity', 'the structural ' + 'g' + 'ap between identity') for l in S['ed']])),
    ('G-NAMES-EXCEPTED', 'the excepted name uses and their back-matter rows', lambda S: names_ok(S),
     lambda S: put(S, 'ed', [l for l in S['ed'] if not l.startswith('| :%d | excepted' % S['REC']._edl(894))])),
    ('G-FACT-READ', 'the reads bank`s pin lines and the formation count', lambda S: fact_read_ok(S),
     lambda S: put(S, 'reads', S['reads'].replace('v0.2 : cited 5c72cad ; local 5c72cad ; remote 5c72cad ; AGREE', 'v0.2 : cited 5c72cad ; local 5c72cad ; remote 0000000 ; ### DIFFER'))),
    ('G-TIER-BLOCK-STANDS', 'v1.5 :1058-:1065 against the edition`s lines by the offset', lambda S: tier_ok(S),
     lambda S: put(S, 'ed', [l + (' x' if l.startswith('#### THE CASCADE, ACT ELEVEN') else '') for l in S['ed']])),
    ('G-VERSION-LINE', 'the edition`s head against the current version`s', lambda S: version_ok(S),
     lambda S: put(S, 'ed', [l for l in S['ed'] if l != '**Version 1.6** | 2026-10-01'])),
    ('G-BACK-MATTER', 'the edition`s back matter', lambda S: backmatter_ok(S), lambda S: put(S, 'ed', [l for l in S['ed'] if l != '### Names excepted'])),
    ('G-STATUS-CELLS', 'every Status column of the edition, cell by cell', lambda S: S['REC']._status_blanks(S['ed']) == [],
     lambda S: put(S, 'ed', S['ed'] + ['', '| a | Status |', '|:--|:--|', '| x |  |'])),
    ('G-REPIN-FINAL', 'the edition`s Correspondence column against its final body', lambda S: repin_final_ok(S),
     lambda S: put(S, 'ed', [l.replace('| cited at :', '| cited at :1, :', 1) if l.startswith('| `SIDEExplicitFormula.') else l for l in S['ed']])),
    ('G-OFFSET-LINE', 'the diff bank`s head and its rows', lambda S: offset_ok(S),
     lambda S: put(S, 'etxt', NL.join(S['etxt'].split(NL)[1:]))),
    ('G-DIFF-BANKED', 'the diff bank', lambda S: S['etxt'].count('      v1.6 : ') == 9 and S['etxt'].count('      v1.5 : ') == 9
     and '### ### **H28a ' in S['etxt'] and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in S['etxt'],
     lambda S: put(S, 'etxt', S['etxt'].replace('      v1.6 : ', '      v1.6: ', 1))),
    ('G-COVERAGE-BANKED', 'the edition json`s rows against the bank`s coverage line', lambda S: len(S['ej'].get('diff', [])) == 9
     and all(d['reading'] in (0, 1) for d in S['ej']['diff']) and sum(1 for d in S['ej']['diff'] if d['reading']) == S['hj'].get('covered')
     and ('the seat`s hand-read: %d of 9 rows' % S['hj'].get('covered')) in S['etxt'],
     lambda S: put(S, 'hj', dict(S['hj'], covered=8))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b586 — lane three, act fourteen under (R196)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-CEILING-READING', 'this act`s trail record', lambda S: '**A reading on the ceiling clause, the author’s:** the pair “census proved / exhaustiveness open”' in trail(S)
     and 'Ostrowski’s theorem closes the place count (n₂ = 3)' in trail(S) and '“since the same shape will recur in EXHAUSTIVENESS_LICENSE next”' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('“census proved / exhaustiveness open”', '“x”'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'CP-7 act twelve, b587' in trail(S) and 'EXHAUSTIVENESS_LICENSE by the same form' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('CP-7 act twelve, b587', 'x'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{DIR_PAGE: ((S['pages'][DIR_PAGE][0] or b'') + b'x', S['pages'][DIR_PAGE][1])}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff', lambda S: S['kmain'] == V015
     and S['kcur'] == 'main' and S['kdirty'] == '' and all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] == [],
     lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-rcurve': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b586_record.py'): S['tooltext'].get(os.path.join(T, 'b586_record.py'), '') + NL + 'os' + '.remove(p)'}))),
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
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at b75a56c5, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b585_closing.txt'])),
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
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b586')" in S['suite'] and "data/b586_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b586')", ''))),
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
    rec('b586 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b586_checks_postpush.txt' if pushed else 'b586_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b586_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
