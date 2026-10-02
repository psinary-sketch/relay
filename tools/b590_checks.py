# -*- coding: utf-8 -*-
"""b590_checks.py -- THE SUITE OF b590, UNDER (R200): THE EPSTEIN NEGATIVE CONTROL; THE SWEEP'S COLUMN; THE DAY-1 SECTION.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b590_checks.txt before the push and data/b590_checks_postpush.txt after
### it. ### The harness is b568's to b589's, carried; the arms are b590's.
### ### **THIS SUITE CARRIES NO FAMILY TEXT OF (R200)(2)**: G-NO-FAMILY-TEXT-PUBLIC builds its needles at run time from the
### local-only paste.
"""
import copy
import fnmatch
import glob
import hashlib
import io
import json
import math
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
PAT = 'D:/MY-DOwnloads/patent-package-BACKUP-2026-08-29'
FACE = os.path.join(D, 'b590_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='8f242f97', pp='53961af', gs='8c392fe', pat='433ae01')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72'}
STEPZERO = '0b2cd9f6'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
L = []
NS = 'SIDEExplicitFormula.Schema.'
KFILES = ['AxiomCheckEpstein.lean', 'SIDEExplicitFormula/Schema/Detector.lean', 'SIDEExplicitFormula/Schema/Epstein.lean',
          'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean']
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b590')
            and 'data/b590_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def build_log_ok(t, module):
    return '### EXIT rc=0' in t and ('Built %s' % module) in t


def log_start(t, module):
    m = re.search(r'=== BUILD %s ; free MB before: \d+ ; start (\S+)' % re.escape(module), t)
    return iso_epoch(m.group(1)) if m else None


def families_from_paste(paste):
    """### the paste's (R200)(2) body and its family labels, read at run time; never written into this file."""
    t = (paste or b'').decode('utf-8', 'replace').replace(chr(13), '')
    if '(2) THE FIVE CLAIM FAMILIES' not in t:
        return '', []
    body = t[t.index('(2) THE FIVE CLAIM FAMILIES'):t.index('(3) THE DAY-1 SECTION NUMBER.')]
    flat = ' '.join(body.split())
    labels = []
    for r in ('I', 'II', 'III', 'IV', 'V'):
        m = re.search(r'\(%s\) (.*?) — ' % r, flat)
        if m:
            labels.append(m.group(1).strip().lower())
    return body, labels


def sources():
    import b590_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b590_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b590_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b590_ferry.txt'), scan=rd('b590_ferry_scan.txt'), cens=rd('b590_census_stepzero.txt'),
        fcens=rd('b590_faces_census_stepzero.txt'), pins0=rd('b590_pins_stepzero.txt'), procs=rd('b590_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b589_closing.txt'), reads=rd('b590_reads.txt'), branches=rd('b590_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        pages={p: (blob(PP, 'HEAD:' + p), blob(PP, PRE['pp'] + ':' + p)) for p in (PAGE, DIR_PAGE)},
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kmain=gs(KER, 'rev-parse', 'main'), kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        kanc=subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', V015, 'main']).returncode == 0,
        kmerges=gs(KER, 'rev-list', '--merges', V015 + '..main'),
        kns=[l for l in gs(KER, 'diff', '--name-status', V015, 'main').split(NL) if l.strip()],
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b589*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b590_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b590_mustnotexist.txt')), table_changed=None,
        fj=jl('b590_findings.json'), tj=jl('b590_trail.json'), sc=jl('b590_scores.json'), desk=rd('b590_desk_notes.txt'),
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
    X['paste'] = raw(os.path.join(PAT, REC.PASTE_FILE))
    X['body'], X['labels'] = families_from_paste(X['paste'])
    X['prior_public'] = read(os.path.join(T, 'b589_record.py')) + rd('b589_sweep.txt')
    X['pat_log'] = [(l.split(' ', 1)[0], files_of(PAT, l.split(' ', 1)[0])) for l in gs(PAT, 'log', '--reverse', '--pretty=%H %s', PRE['pat'] + '..HEAD').split(NL) if l.strip()]
    X['pat_remote'] = gs(PAT, 'remote', '-v')
    X['pat_sweep'] = raw(os.path.join(PAT, REC.SWEEP_FILE))
    X['sweep'], X['sweep_txt'] = jl('b590_sweep.json'), rd('b590_sweep.txt')
    pub = {}
    for p in sorted(glob.glob(os.path.join(D, 'b590_*'))) + S['tools']:
        pub[os.path.relpath(p, ROOT).replace(os.sep, '/')] = read(p)
    pub['PLACE-papers appended'] = (S['fi_now'] or b'')[len(S['fi_pre'] or b''):].decode('utf-8', 'replace') + \
        (S['ot_now'] or b'')[len(S['ot_pre'] or b''):].decode('utf-8', 'replace')
    pub['SIDE-global-section appended'] = (S['corr_now'] or b'')[len(S['corr_pre'] or b''):].decode('utf-8', 'replace')
    X['public'] = pub
    X['w1'] = jl('b590_weight_line.json')
    X['dy'] = jl('b590_day1.json')
    X['day1_blob'] = blob(PP, '%s:%s' % (REC.DAY1_PIN, REC.BALPOS))
    X['credits'] = {p: (blob(PP, 'HEAD:' + p), blob(PP, PRE['pp'] + ':' + p)) for p in (REC.SURR_ED, REC.INDEX_ED)}
    X['st'] = {k: jl('b590_statements_%s.json' % k) for k in ('detector', 'epstein', 'salt')}
    X['st_salt_final'] = jl('b590_statements_salt_final.json')
    X['bld'] = {k: rd('b590_build_%s.txt' % k) for k in ('detector', 'epstein', 'salt')}
    X['kfile_at'] = {f: blob(KER, '%s:%s' % (V016, f)) for f in KFILES}
    X['kfile_det_a'] = blob(KER, '58b912a:SIDEExplicitFormula/Schema/Detector.lean')
    X['pd'], X['pa'] = jl('b590_prints_detector.json'), jl('b590_prints_all.json')
    X['e0'] = {k: jl('b590_e0_%s.json' % k) for k in ('detector', 'epstein', 'salt')}
    X['h31a'], X['h31b'] = jl('b590_h31a.json'), jl('b590_h31b.json')
    X['wj'], X['wtxt'] = jl('b590_witness_vs_bench.json'), rd('b590_witness_vs_bench.txt')
    X['kpush'], X['bpush'] = rd('b590_kernel_push_out.txt'), rd('b590_branch_push_out.txt')
    X['rowgen'] = jl('b590_rowgen.json')
    X['conv171'] = (lines_of(blob(KER, 'v0.15:SIDEExplicitFormula/Schema/Converse.lean')) or [''] * 171)[170]
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
    i = t.find('### b590 — lane two, act fourteen under (R200)')
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE', 'HOLDS') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return not [f for f, t in S['tooltext'].items() if pat.search(t)]


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


# ### the act's own predicates
def paste_ok(S):
    body = S['body']
    if not body:
        return False
    h = hashlib.sha256(body.encode('utf-8')).hexdigest()
    ptr = [l for l in S['ferry'].split(NL) if 'HELD LOCAL-ONLY' in l or h in l]
    return h in S['ferry'] and body not in S['ferry'] and ' '.join(body.split())[:300] not in ' '.join(S['ferry'].split()) \
        and bool(ptr) and S['REC'].PASTE_FILE in S['ferry']


def needles(S):
    """### the family labels, less any already public before this act (b589's sweep tool and bank name an instrument the
    ### same as a family) -- what this act could leak, not what was already out."""
    prior = ' '.join(S['prior_public'].lower().split())
    return [x for x in S['labels'] if len(x) > 12 and x not in prior]


def no_family_public(S):
    if len(S['labels']) != 5:
        return False
    nd = needles(S)
    for name, txt in S['public'].items():
        low = ' '.join(txt.lower().split())
        if any(n in low for n in nd):
            return False
    return len(nd) >= 4


def sweep_ok(S):
    sw, f = S['sweep'], S['pat_sweep'] or b''
    return sw.get('instruments') == 12 and sw.get('per_row') == [1] * 12 and sum(sw.get('counts', {}).values()) == 12 \
        and sw.get('sha256') == hashlib.sha256(f).hexdigest() and S['REC'].CELL_OLD.encode('utf-8') not in f \
        and sw.get('body_sha256') == hashlib.sha256(S['body'].encode('utf-8')).hexdigest()


def patent_ok(S):
    log = S['pat_log']
    return len(log) == 2 and log[0][1] == [S['REC'].PASTE_FILE] and log[1][1] == [S['REC'].SWEEP_FILE] and S['pat_remote'] == ''


def day1_ok(S):
    b = S['day1_blob'] or b''
    ls = b.decode('utf-8', 'replace').split(NL)
    heads = [(i + 1, l) for i, l in enumerate(ls) if l.startswith('## ')]
    sec = lambda n: [h for h in heads if h[0] <= n][-1][1] if [h for h in heads if h[0] <= n] else ''
    row = [i + 1 for i, l in enumerate(ls) if l.startswith('| W_∞ (digamma/Γ)') and 'positive (provable)' in l]
    dom = [i + 1 for i, l in enumerate(ls) if 'the positive archimedean term dominates the indefinite' in l]
    return hashlib.md5(b).hexdigest() == S['REC'].DAY1_MD5 and row == S['dy'].get('row') == [32] and dom == S['dy'].get('sentence') \
        and sec(row[0]).startswith('## I.') and sec(dom[0]).startswith('## II.') and S['dy'].get('corrected') is False


def credits_ok(S):
    ph = 'Day-1 BALANCE_AND_POSITIVITY §I attributed the positivity to the archimedean term alone'
    return all(h is not None and h == p and ph.encode('utf-8') in h for h, p in S['credits'].values())


def statements_ok(S):
    det, ep, sa, saf = S['st']['detector'], S['st']['epstein'], S['st']['salt'], S['st_salt_final']
    t_det, t_ep, t_sa = (log_start(S['bld']['detector'], 'SIDEExplicitFormula.Schema.Detector'),
                         log_start(S['bld']['epstein'], 'SIDEExplicitFormula.Schema.Epstein'),
                         log_start(S['bld']['salt'], 'SIDEExplicitFormula.Schema.SaltCheckEpstein'))
    sha = lambda b: hashlib.sha256(b or b'').hexdigest()
    return None not in (t_det, t_ep, t_sa) and iso_epoch(det.get('at', '')) < t_det and iso_epoch(ep.get('at', '')) < t_ep \
        and iso_epoch(sa.get('at', '')) < t_sa and det.get('sha256') == sha(S['kfile_det_a']) \
        and ep.get('sha256') == sha(S['kfile_at']['SIDEExplicitFormula/Schema/Epstein.lean']) \
        and saf.get('sha256') == sha(S['kfile_at']['SIDEExplicitFormula/Schema/SaltCheckEpstein.lean'])


def prints_ok(S):
    pd, pa = S['pd'].get('axioms', {}), S['pa'].get('axioms', {})
    return len(pd) == 8 and len(pa) == 35 and all(set(a) <= STD3 for a in list(pd.values()) + list(pa.values())) \
        and not S['pd'].get('sorry') and not S['pa'].get('sorry') and S['pd'].get('errors') == 0 and S['pa'].get('errors') == 0


def e0_fresh(S):
    import e0_rule as E0
    import b569_record as R9
    want = {('detector', 'Detector'): 'DERIVES', ('not_h2_sign_cfg_of_offline', 'Detector'): 'DERIVES',
            ('epstein_not_h2_sign_cfg', 'Epstein'): 'INTERFACES'}
    for (n, f), g_ in want.items():
        src = (S['kfile_at']['SIDEExplicitFormula/Schema/%s.lean' % f] or b'').decode('utf-8')
        head, _ = R9.header_of(src, n)
        if E0.grade(head or '', 'theorem')[0] != g_:
            return False
        key = 'epstein' if f == 'Epstein' else 'detector'
        if S['e0'][key].get('rows', {}).get(NS + n, {}).get('grade') != g_:
            return False
    return all(S['e0'][k].get('gate') is True for k in ('detector', 'epstein', 'salt'))


def h31a_ok(S):
    a = S['h31a']
    want = 'REFUTED' if (a.get('quantified') and 'Metric.tendsto_atTop' in S['conv171']) else 'HOLDS'
    return a.get('H31a') == want and S['sc'].get('H31a', [''])[0] == want and '(H31A)' in S['desk']


def salt_ok(S):
    r = S['e0']['salt'].get('rows', {})
    sat, lb = r.get(NS + 'SaltCheckEpstein.epstein_hypotheses_satisfiable', {}), r.get(NS + 'SaltCheckEpstein.membership_load_bearing', {})
    t = S['pa'].get('text', '')
    return sat.get('std3') and lb.get('std3') and (NS + 'SaltCheckEpstein.epstein_hypotheses_satisfiable :') in t \
        and (NS + 'SaltCheckEpstein.membership_load_bearing :') in t and S['h31b'].get('names') is True


def h31b_ok(S):
    b = S['h31b']
    want = 'HOLDS' if salt_ok(S) and b.get('conclusion', {}).get('grade') == 'INTERFACES' else 'REFUTED'
    return b.get('H31b') == want and S['sc'].get('H31b', [''])[0] == want and '(H31B)' in S['desk']


def witness_ok(S):
    w, t = S['wj'], S['wtxt']
    return all(x in t for x in ('### (1) THE SCORES AT THE BASE', '### (2) THE SUPPORT', '### (3) THE SIGN AT THE WITNESS',
                                '### A READING')) and w.get('on_count') == 146 and w.get('off_count') == 17 and w.get('ties') == 1


def h31c_ok(S):
    w = S['wj']
    try:
        D_ = 2 * w['VF'] + 2 * (w['Xr'] + 1) + 2
        half = 2.0 ** D_ * float(w['w'])
        ratio = half / math.log(33.194255)
    except Exception:
        return False
    want = 'HOLDS' if 0.1 <= ratio <= 10 else 'REFUTED'
    return D_ == w['D'] and abs(half / float(w['half_pre']) - 1) < 1e-9 and abs(ratio / float(w['ratio']) - 1) < 1e-9 \
        and w['H31c'] == want and S['sc'].get('H31c', [''])[0] == want and '(H31C)' in S['desk']


def corr_ok(S):
    now, pre = S['corr_now'] or b'', S['corr_pre'] or b''
    t = now.decode('utf-8', 'replace')
    nums = [l.split('|')[1].strip() for l in t.split(NL) if re.match(r'^\| \d+ \|', l)]
    return now.startswith(pre) and all(nums.count(n) == 1 for n in ('442', '443', '444', '445')) \
        and nums[-5:] == ['441', '442', '443', '444', '445'] and S['gs_diff'] == ['CORRESPONDENCE.md']


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return fline(S, e) == S['REC'].TITLE and '**The detector theorem**' in tail and '**The Epstein instance**' in tail \
        and '**The witness against the bench**' in tail


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R200) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and 'ORPHANS STOPPED BY PID' in S['procs']
     and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '  1234   5678 grep.exe        2026-09-01 00:00:00  grep x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b589`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b589' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b590 -- x'])),
    ('G-R200-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R200) END' in S['ferry'] and S['ot'].count('**(R200) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R200) ratified', '(R200) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'Schema/Config.lean @', 'Schema/Converse.lean @', 'PowerWindow.lean @', 'PowerLimit.lean @', 'TwoPropertyWindow.lean @',
        'RestBound.lean @', 'Zeta23/Defs.lean @', 'b554_sign_pattern.txt @', 'b511_families.py @', 'b559_desk_notes.txt @',
        'BALANCE_AND_POSITIVITY.md @ 53961af2', 'BALANCE_AND_POSITIVITY.md @ 0b8f4354', 'FACES_LEDGER.md @', 'THE_DAY1_IMPLICATIONS.md @',
        'SIGN_ARRANGEMENT_RECONCILIATION.md @', 'THE_UNCONDITIONAL_SURROUND_v0_5.md @', 'INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md @',
        'FINDINGS.md @', 'SWEEP_TWO_2026-10-01.md @', 'b589_closing_push_out.txt @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 0b2cd9f6`s files', lambda S: S['pushout'][0] == ['data/b589_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b589') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b589'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-PASTE-HELD-LOCAL', 'the patent repository`s paste, hashed afresh, against the relay bank`s pointer', lambda S: paste_ok(S),
     lambda S: put(S, 'ferry', S['ferry'] + NL + S['body'])),
    ('G-NO-FAMILY-TEXT-PUBLIC', 'every relay file this act writes and every appended PLACE-papers and SIDE-global-section byte, '
                                'against needles built at run time from the local paste', lambda S: no_family_public(S),
     lambda S: put(S, 'public', dict(S['public'], **{'data/b590_x.txt': ' '.join(needles(S)[:1])}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['w1'].get('line')).startswith(S['w1'].get('head', '#'))
     and '(:6718)' in fline(S, S['w1']['line']) and 'b589 AT ITS WEIGHT' in fline(S, S['w1']['line'])
     and 'The suite reads 78 of 78.' in fline(S, S['w1']['line']) and 'H30a held' in fline(S, S['w1']['line']),
     lambda S: put(S, 'w1', dict(S['w1'], line=1))),
    ('G-SWEEP-COLUMN', 'the sweep bank against the patent file`s bytes and the paste`s body', lambda S: sweep_ok(S),
     lambda S: put(S, 'pat_sweep', (S['pat_sweep'] or b'') + b'x')),
    ('G-PATENT-COMMITS', 'the patent repository`s log since 433ae01 and its remotes', lambda S: patent_ok(S),
     lambda S: put(S, 'pat_log', S['pat_log'] + [('x', ['y'])])),
    ('G-DAY1-SECTION', 'the Day-1 blob at 0b8f435, re-hashed and its headings read afresh', lambda S: day1_ok(S),
     lambda S: put(S, 'day1_blob', (S['day1_blob'] or b'') + b'x')),
    ('G-CREDIT-LINES-STAND', 'SURROUND v0.5 and INDEX_ARITY v0.19 at PLACE-papers HEAD against their pre-act blobs', lambda S: credits_ok(S),
     lambda S: put(S, 'credits', {k: ((v[0] or b'') + b'x', v[1]) for k, v in S['credits'].items()})),
    ('G-STATEMENTS-FIRST', 'the statement banks` times and digests against the build logs and the committed files', lambda S: statements_ok(S),
     lambda S: put(S, 'st', dict(S['st'], detector=dict(S['st']['detector'], at='2099-01-01T00:00:00Z')))),
    ('G-DETECTOR-BUILT', 'the detector`s build bank', lambda S: build_log_ok(S['bld']['detector'], 'SIDEExplicitFormula.Schema.Detector')
     and ': error' not in S['bld']['detector'] and 'stopped None' in S['bld']['detector'],
     lambda S: put(S, 'bld', dict(S['bld'], detector=S['bld']['detector'].replace('### EXIT rc=0', '### EXIT rc=1')))),
    ('G-DETECTOR-PRINTS', 'the detector`s prints and the full prints', lambda S: prints_ok(S),
     lambda S: put(S, 'pa', dict(S['pa'], sorry=['x']))),
    ('G-H31A-SCORED', 'the H31a json against Converse :171 at v0.15 and the scores', lambda S: h31a_ok(S),
     lambda S: put(S, 'h31a', dict(S['h31a'], H31a='HOLDS'))),
    ('G-EPSTEIN-BUILT', 'the Epstein and salt-check build banks', lambda S: build_log_ok(S['bld']['epstein'], 'SIDEExplicitFormula.Schema.Epstein')
     and build_log_ok(S['bld']['salt'].split('=== attempt 4 (landed) ===')[-1], 'SIDEExplicitFormula.Schema.SaltCheckEpstein')
     and S['bld']['salt'].count('### EXIT rc=1') == 3,
     lambda S: put(S, 'bld', dict(S['bld'], salt=S['bld']['salt'].replace('Built SIDEExplicitFormula.Schema.SaltCheckEpstein', 'x')))),
    ('G-SALT-CHECK', 'the salt-check`s E0 rows and the full prints', lambda S: salt_ok(S),
     lambda S: put(S, 'h31b', dict(S['h31b'], names=False))),
    ('G-E0-GRADES', 'each terminal`s header at v0.16 re-graded by e0_rule afresh', lambda S: e0_fresh(S),
     lambda S: put(S, 'e0', dict(S['e0'], epstein=dict(S['e0']['epstein'], rows={})))),
    ('G-H31B-SCORED', 'the H31b json, the salt-check and the scores', lambda S: h31b_ok(S),
     lambda S: put(S, 'h31b', dict(S['h31b'], H31b='REFUTED'))),
    ('G-WITNESS-BANKED', 'the witness bank and its json', lambda S: witness_ok(S),
     lambda S: put(S, 'wtxt', S['wtxt'].replace('### (3) THE SIGN AT THE WITNESS', '### (3)'))),
    ('G-H31C-SCORED', 'D, the half-width and the ratio recomputed from the witness json', lambda S: h31c_ok(S),
     lambda S: put(S, 'wj', dict(S['wj'], D=S['wj'].get('D', 0) + 1))),
    ('G-MAIN-FF', 'the kernel`s main and its ancestry', lambda S: S['kmain'] == V016 and S['kanc'] and S['kmerges'] == '',
     lambda S: put(S, 'kanc', False)),
    ('G-TAG-BY-SCRIPT', 'the kernel push capture', lambda S: 0 <= S['kpush'].find('main read back at the remote: ' + V016)
     < S['kpush'].find('push_gated: tag v0.16 made at the read-back') and ('tag v0.16 peeled local %s remote %s' % (V016, V016)) in S['kpush'],
     lambda S: put(S, 'kpush', S['kpush'].replace('tag v0.16 made', 'x'))),
    ('G-BRANCH-PUSHED', 'the branch push bank', lambda S: ('epstein-b590 local %s remote %s' % (V016, V016)) in S['bpush'] and 'push rc=0' in S['bpush'],
     lambda S: put(S, 'bpush', '')),
    ('G-KERNEL-STATEMENTS-KEPT', 'the kernel, v0.15 against main, by status', lambda S: sorted(S['kns']) == sorted('A\t' + f for f in KFILES),
     lambda S: put(S, 'kns', S['kns'] + ['M\tSIDEExplicitFormula/Schema/Converse.lean'])),
    ('G-ROWGEN-DIFF', 'the rowgen json', lambda S: S['rowgen'].get('clean') is True and len(S['rowgen'].get('rows', {})) == 3,
     lambda S: put(S, 'rowgen', dict(S['rowgen'], clean=False))),
    ('G-CORR-ROWS', 'CORRESPONDENCE rows 442-445 at SIDE-global-section HEAD against its pre-act blob', lambda S: corr_ok(S),
     lambda S: put(S, 'corr_now', (S['corr_now'] or b'') + b'| 443 | dup |\n')),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b590 — lane two, act fourteen under (R200)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-STANDING-LINE', 'this act`s trail record', lambda S: 'claim-family text travels in a separate local-only paste from now on' in trail(S)
     and 'is recorded as the navigator’s' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('from now on', 'for now'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b591: the located-clause method document' in trail(S) and 'resume at RESIDUE' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b591: the located-clause', 'x'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{DIR_PAGE: ((S['pages'][DIR_PAGE][0] or b'') + b'x', S['pages'][DIR_PAGE][1])}))),
    ('G-OTHER-KERNELS-UNTOUCHED', 'every other kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['gs_diff'] == ['CORRESPONDENCE.md'] and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-rcurve': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b590_record.py'): S['tooltext'].get(os.path.join(T, 'b590_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: not [f for f, t in S['tooltext'].items()
                                                                        if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-UNTOUCHED', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == [],
     lambda S: put(S, 'keystone_changes', ['phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md'])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 8f242f97, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b589_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == ['FINDINGS.md', 'OPEN_TRAILS.md'],
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 7)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b590')" in S['suite'] and "data/b590_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b590')", ''))),
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
    rec('b590 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b590_checks_postpush.txt' if pushed else 'b590_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b590_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
