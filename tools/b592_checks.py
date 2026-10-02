# -*- coding: utf-8 -*-
"""b592_checks.py -- THE SUITE OF b592, UNDER (R202): CP-7 ACT FOURTEEN, THE EDITION OF THE_RESIDUE_OF_RH; THE TWO PAGES
REGENERATED AT v0.16; THE ARM-UNRUN STANDING LINE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b592_checks.txt before the push and
### data/b592_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b592_arms_prerun.txt and nothing else.
### ### The harness is b568's to b591's, carried; the arms are b592's.
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
FACE = os.path.join(D, 'b592_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'
ED = 'phase1.5/proofs/THE_RESIDUE_OF_RH_v1_2.md'
PRE = dict(relay='652b58d5', pp='9059169', gs='3528bcf')
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
PRE_HEADS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72'}
STEPZERO = '24457265'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
EDITIONS11 = sorted(['phase1.5/method/ENUMERA_v1_6.md', 'phase1.5/method/EXHAUSTIVENESS_LICENSE_v0_2.md', 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md',
                     'phase1.5/method/TECHNE_TOOLKIT_v8_3.md', 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md',
                     'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md',
                     'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md', 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md',
                     'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md', 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md'])
ENGLISH10 = sorted(['heritage/UNIFICATION_OF_FORCES.md', 'internal/CATALOGOS.md', 'internal/CONVERGENCE.md', 'internal/SIDE_EFFECTS.md',
                    'phase1.5/method/INSTRUMENTS.md', 'phase1.5/method/TECHNE_TOOLKIT.md', 'phase1.5/method/TECHNE_TOOLKIT_v8_3.md',
                    'phase1.5/method/THE_INSTRUMENT_SUITE_RELEASE.md', 'phase1.5/method/THE_METHOD_CANON.md', 'phase2/method/THE_KEYSTONE_CENSUS.md'])
EPSTEIN_ROW = ('| `SIDEExplicitFormula.Schema.epstein_not_h2_sign_cfg` | SIDE-explicit-formula | INTERFACES | T2-INTERFACES; premises: '
               'hP : EpsteinPremises Z rhs |')
FOUR = {'h2_sign_iff_rh': '5c72cad', 'li_nonneg_iff_rh': 'e5a5a83', 'arith_limit_nonneg_iff_rh': 'e5a5a83',
        'register4_positivity_liCoeff_iff_rh': '19b7d1e'}


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b592')
            and 'data/b592_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b592_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b592_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b592_') and f.endswith('.py')) or f == 'test_chain_page_b592.py')
    S = dict(
        REC=REC, face=face, ferry=rd('b592_ferry.txt'), scan=rd('b592_ferry_scan.txt'), cens=rd('b592_census_stepzero.txt'),
        fcens=rd('b592_faces_census_stepzero.txt'), pins0=rd('b592_pins_stepzero.txt'), procs=rd('b592_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b591_closing.txt'), reads=rd('b592_reads.txt'), branches=rd('b592_branches.txt'), answers=rd('b592_author_answers.txt'),
        prerun=rd('b592_arms_prerun.txt'),
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
        push_lists={r: gs(r, 'branch', '--list', 'push-b591*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b592_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b592_mustnotexist.txt')), table_changed=None,
        fj=jl('b592_findings.json'), tj=jl('b592_trail.json'), sc=jl('b592_scores.json'), desk=rd('b592_desk_notes.txt'),
        wl1=jl('b592_weight_line.json'), sl=jl('b592_standing_line.json'), fl=jl('b592_form_lines.json'),
        P1=jl('b592_pages.json'), P2=jl('b592_pages_c2.json'), E=jl('b592_edition.json'), H=jl('b592_h28.json'),
        bank=rd('b592_edition_RESIDUE.txt'), termscan=rd('b592_edition_termscan.txt'),
        arms_c1=rd('b592_page_arms_c1.txt'), arms_c2=rd('b592_page_arms_c2.txt'),
        nodes_z=rd('b592_nodes.txt'), nodes_c=rd('b592_nodes_chi.txt'), nodes_z0=rd('b569_nodes.txt'), nodes_c0=rd('b573_nodes_chi.txt'),
        probe_z=rd('b592_probe_out.txt'), probe_c=rd('b592_chi_probe_out.txt'),
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
    import chain_page as C
    REC = S['REC']
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b592_nodes.txt'), os.path.join(REC.SP, '_b592_gcp'), os.path.join(D, 'b592_probe_out.txt')) \
        if os.path.exists(os.path.join(D, 'b592_probe_out.txt')) else dict(ok=False)
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b592_nodes_chi.txt'), os.path.join(REC.SP, '_b592_gcp'), os.path.join(D, 'b592_chi_probe_out.txt')) \
        if os.path.exists(os.path.join(D, 'b592_chi_probe_out.txt')) else dict(ok=False)
    X['page_z'], X['page_c'] = lines_of(blob(PP, 'HEAD:' + PAGE)), lines_of(blob(PP, 'HEAD:' + DIR_PAGE))
    X['reg960'] = (lines_of(blob(PP, 'HEAD:REGISTRY.md')) + [''] * 960)[959]
    gc = gs(ROOT, 'log', '-1', '--format=%H', '--', 'tools/chain_page.py')
    X['gen_commit'] = (gc, files_of(ROOT, gc) if gc else [], gs(ROOT, 'log', '-1', '--format=%ct', gc) if gc else '0',
                       subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', PRE['relay'], gc]).returncode == 0 if gc else False,
                       gc != gs(ROOT, 'rev-parse', PRE['relay']) and gs(ROOT, 'log', '-1', '--format=%H', PRE['relay'], '--', 'tools/chain_page.py') != gc)
    tp = os.path.join(T, 'test_chain_page_b592.py')
    if os.path.exists(tp):
        r = subprocess.run([sys.executable, tp], capture_output=True, text=True, encoding='utf-8', errors='replace')
        X['gen_test'] = (r.returncode, r.stdout, rd('b592_generator_test.txt'))
    else:
        X['gen_test'] = (1, '', '')
    try:
        old = _old_module('tools/chain_page.py', 'chain_page_before')
        zn = [n.split(' | ')[0].strip() for n in S['nodes_z'].split(NL) if n.strip() and not n.startswith(('#', '@'))]
        cn = [n.split(' | ')[0].strip() for n in S['nodes_c'].split(NL) if n.strip() and not n.startswith(('#', '@'))]
        zs = [C.short(n) for n in zn if not n.startswith(('RiemannHypothesis', 'riemannZeta'))]
        cs = [C.short(n) for n in cn]
        X['rule'] = dict(z_old=old.keystones(zs), z_new=C.keystones(zs), c_old=old.keystones(cs), c_new=C.keystones(cs))
    except Exception as e:
        X['rule'] = dict(error=str(e))
    X['ed_raw'] = raw(os.path.join(PP, *ED.split('/')))
    X['ed_head'] = cr0(blob(PP, 'HEAD:' + ED))
    X['ed'] = cr0(X['ed_head']).decode('utf-8', 'replace').split(NL) if X['ed_head'] else []
    if X['ed'] and X['ed'][-1] == '':
        X['ed'] = X['ed'][:-1]
    r = subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', os.path.join(PP, *ED.split('/'))], capture_output=True, text=True,
                       encoding='utf-8', errors='replace') if X['ed_raw'] else None
    X['scan_now'] = r.stdout if r else ''
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


# ### the act's own predicates
def recs(t):
    return [l for l in t.split(NL) if l.strip() and not l.startswith('#')]


def nodes_ok(S):
    z, z0, c, c0 = recs(S['nodes_z']), recs(S['nodes_z0']), recs(S['nodes_c']), recs(S['nodes_c0'])
    return z == z0 and '# pin: v0.16' in S['nodes_z'].split(NL) and c[:-1] == c0 and c[-1].startswith('SIDEExplicitFormula.Schema.detector | kernel | added:') \
        and '# pin: v0.16' in S['nodes_c'].split(NL) and '# page: dirichlet' in S['nodes_c'].split(NL)


def probes_ok(S):
    P1 = S['P1']
    return all(('@@BEGIN' in S[k] and len(S[k]) > 10000) for k in ('probe_z', 'probe_c')) and bool(P1) \
        and all(P1[k]['identical'] and P1[k]['probe_identical'] for k in ('zeta', 'chi'))


def pages_logs_v016(S):
    t = rd('b592_page_runs.txt')
    return t.count('v0.16 c404e727d7f7') == 4 and t.count('lake env lean exit 0') == 4


def zeta_placement(S):
    P1 = S['P1']
    added = sorted(re.search(r'`([^`]+)`', x).group(1) for x in P1.get('zeta', {}).get('added', []))
    return added == EDITIONS11 and P1['zeta']['gone'] == []


def chi_960(S):
    ls = S['page_c']
    if '## Placement' not in ls:
        return False
    last = [x for x in ls[:ls.index('## Placement')] if x.strip()][-1]
    m = re.search(r"Supportable, the author's sentence: \*(.*?)\*", S['reg960'])
    return bool(m) and last == m.group(1) and S['P1'].get('chi', {}).get('last_eq_960') is True


def chi_nodes(S):
    ls = S['page_c']
    return any(re.match(r'^19\. `SIDEExplicitFormula\.Schema\.detector` — SIDEExplicitFormula/Schema/Detector\.lean:99 — v0\.16 = c404e72 — ', l) for l in ls) \
        and EPSTEIN_ROW in ls and '| `SIDEExplicitFormula.Schema.not_h2_sign_cfg_of_offline` | SIDE-explicit-formula | DERIVES | T0 |' in ls \
        and 'v0.16 = `c404e72`' in ls[2] and 'data/b592_nodes_chi.txt' in ls[2]


def chi_placement(S):
    rows = [re.search(r'`([^`]+)`', l).group(1) for l in S['page_c'] if l.startswith('| keystone naming a node |')]
    return not (set(rows) & set(ENGLISH10)) and {'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md', 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md', ED} <= set(rows)


def zeta_head(S):
    ls = S['page_z']
    return len(ls) > 3 and 'v0.16 = `c404e72`' in ls[2] and 'data/b592_nodes.txt' in ls[2] and \
        all(any(('`%s`' % n) in l and ('= ' + FOUR[n.split('.')[-1]]) in l for l in ls) for n in (
            'SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh',
            'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh', 'SIDEExplicitFormula.PageConverses.register4_positivity_liCoeff_iff_rh'))


def pages_alone(S):
    log = S['pp_log']
    pg = [(h, s) for h, s in log if S['pp_files'][h] in ([PAGE], [DIR_PAGE])]
    edc = [h for h, s in log if S['pp_files'][h] == [ED]]
    if len(pg) != 4 or len(edc) != 1:
        return False
    idx = {h: i for i, (h, s) in enumerate(log)}
    e = idx[edc[0]]
    before = [h for h, s in pg if idx[h] < e]
    after = [h for h, s in pg if idx[h] > e]
    return len(before) == 2 and len(after) == 2 and all(s.startswith('b592 housekeeping') for h, s in pg) \
        and sorted(S['pp_files'][h][0] for h in before) == sorted([PAGE, DIR_PAGE]) == sorted(S['pp_files'][h][0] for h in after)


def pages_c2_ok(S):
    P2 = S['P2']
    return bool(P2) and all(P2[k]['identical'] and P2[k]['changed'] for k in ('zeta', 'chi')) and \
        all(len([x for x in P2[k]['diff'] if x.startswith('+| keystone naming a node |')]) == 1 and
            ('`%s`' % ED) in [x for x in P2[k]['diff'] if x.startswith('+| keystone')][0] and
            not [x for x in P2[k]['diff'] if x.startswith(('+', '-')) and not x.startswith(('+++', '---', '+| keystone'))] for k in ('zeta', 'chi'))


def gen_alone(S):
    c, files, ct, anc, moved = S['gen_commit']
    return files == ['tools/chain_page.py', 'tools/test_chain_page_b592.py'] and anc and moved and S['lock_epoch'] is not None and int(ct or 0) > S['lock_epoch']


def gen_test(S):
    rc, out, bank = S['gen_test']
    return rc == 0 and re.search(r'^\s*### (\d+) of \1 cases as wanted -- PASS', out, re.M) is not None and out.strip() == bank.strip()


def rule_checked(S):
    r = S['rule']
    return 'error' not in r and r['z_old'] == r['z_new'] and sorted(set(r['c_old']) - set(r['c_new'])) == ENGLISH10 \
        and set(r['c_new']) <= set(r['c_old'])


def arms_page(S, key):
    return 'PAGE ARMS PASSING : 2 of 2' in S[key] and 'G-CHAIN-PAGE : PASS' in S[key] and 'G-CHAIN-PAGE-CHI : PASS' in S[key]


def ed_cur_unedited(S):
    a, b, c = S['cur']
    return bool(b) and a == b == c


def _edl(S, n):
    return S['REC']._edl(n)


def ed_carries(S):
    ed, cur = S['ed'], lines_of(S['cur'][1])
    if cur and cur[-1] == '':
        cur = cur[:-1]
    REC = S['REC']
    changed = set(x[0] for x in REC._all_changes())
    if not ed or BM_TAG(S) not in ed:
        return False
    return all(ed[_edl(S, n) - 1] == cur[n - 1] for n in range(1, len(cur) + 1) if n not in changed) \
        and all(ed[_edl(S, n) - 1] != cur[n - 1] for n in changed) and S['E'].get('sha256') == hashlib.sha256(S['ed_head']).hexdigest()


def BM_TAG(S):
    return S['REC'].BM_TAG


def worklist_row(S):
    ed = S['ed']
    n = _edl(S, 132)
    return bool(ed) and ed[n - 1] == S['REC'].NEW_132 and '`SIDEExplicitFormula.B321.h2_sign_iff_rh`' in ed[n - 1] and 'v0.2 = `5c72cad`' in ed[n - 1] \
        and '### **OPEN**' in ed[n - 1]


def ruled_rewrites(S):
    ed, REC = S['ed'], S['REC']
    if not ed:
        return False
    l77, l79, l88 = ed[_edl(S, 77) - 1], ed[_edl(S, 79) - 1], ed[_edl(S, 88) - 1]
    four = all(('`%s`' % d) in x and ('`%s`' % FOUR[d]) in x for d in FOUR for x in (l77, l79, l88))
    return four and REC.NEW_77 in l77 and REC.NEW_79A in l79 and REC.NEW_79B in l79 and REC.NEW_88 in l88 \
        and 'only the conjunction is RH' not in NL.join(ed[:ed.index(BM_TAG(S))]) and 'their join is the whole of RH' not in l79


def credit_placed(S):
    ed = S['ed']
    n = _edl(S, 77)
    return bool(ed) and ed[n] == '' and ed[n + 1] == S['REC'].CREDIT[1] and ':6764' in ed[n + 1] and ':3476' in ed[n + 1]


def history_lines(S):
    ed, REC = S['ed'], S['REC']
    return bool(ed) and all(ed[_edl(S, a)] == '' and ed[_edl(S, a) + 1] == t for a, s, t in REC.HIST)


def version_line(S):
    ed, REC = S['ed'], S['REC']
    n = _edl(S, 17)
    return bool(ed) and ed[n - 3] == REC.VERSION[1] and ed[n - 2] == '' and ed[n - 1].startswith('*v1.1 — 2026-07-27')


def backmatter(S):
    ed = S['ed']
    if not ed or BM_TAG(S) not in ed:
        return False
    bm = NL.join(ed[ed.index(BM_TAG(S)):])
    heads = ['### Removals', '### Rewrites', '### Credit lines', '### Stem uses carried by history', '### Ceiling corrections',
             '### Ceiling-shaped sentences read and carried', '### Fact corrections', '### The navigator’s expectations', '### Placement', '### Correspondence']
    pos = [bm.find(h) for h in heads]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and (':%d, carried-by-history' % _edl(S, 134)) in bm \
        and (':%d, carried-by-history' % _edl(S, 152)) in bm and S['E'].get('status_blanks') == []


def h28a_ok(S):
    E = S['E']
    wl = [d for d in E.get('diff', []) if d['kind'] == 'work-list']
    want = 'HELD' if wl and all(d['changed'] and d['cites'] for d in wl) else 'REFUTED'
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
    carried = set(_edl(S, n) for n in REC.CARRIED) | set(_edl(S, x[0]) for x in REC._all_changes())
    beyond = [i for i, l in enumerate(ed[:cut], 1) for m in REC.CEILING.finditer(l) if i not in carried]
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['scan_now'], re.M) is not None and \
        re.search(r'carried-by-history 3\b', S['scan_now']) is not None
    want = 'HELD' if clean and not beyond else 'REFUTED'
    return S['H'].get('H28c') == want and S['sc'].get('H28c', [''])[0] == want and S['scan_now'].strip() == S['termscan'].strip()


def ed_bank(S):
    b = S['bank']
    return b.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3): ' + S['REC'].OFFSET) and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in b \
        and ('sha256 %s' % S['E'].get('sha256', '#')) in b


def form_lines_ok(S):
    fl = S['fl'].get('lines', [])
    return len(fl) == 3 and all(oline(S, x['line']).startswith(x['head']) for x in fl) and 'THE PAGE CLAUSE' in fl[0]['head'] \
        and 'THE RESTATEMENT CLAUSE' in fl[1]['head'] and 'AN ERA ANNOTATION IS A DATED ENTRY' in fl[2]['head'] \
        and '(:11864)' in fl[0]['head'] and '(:12044)' in fl[2]['head']


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 16]) if e else ''
    return bool(e) and fline(S, e) == S['REC'].TITLE and '**The edition**' in tail and '**The pages**' in tail and ED in tail \
        and ('sha256 `%s`' % S['E'].get('sha256', '#')) in tail and 'BALANCE_AND_POSITIVITY' in tail


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R202) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b591`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b591' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b592 -- x'])),
    ('G-R202-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R202) END' in S['ferry'] and S['ot'].count('**(R202) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R202) ratified', '(R202) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'data/b558_editions/THE_RESIDUE_OF_RH.txt @', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md @ 9059169', 'FINDINGS.md @ 9059169',
        'OPEN_TRAILS.md @ 9059169', PAGE + ' @ 9059169', DIR_PAGE + ' @ 9059169', 'data/b569_nodes.txt @', 'data/b573_nodes_chi.txt @',
        'tools/chain_page.py @', 'Schema/Detector.lean @ c404e727', 'Schema/Epstein.lean @ c404e727', 'data/b591_closing_push_out.txt @',
        '### THE b450 ITEM SEARCHED BY NAME', ':11864 ', ':6218 '))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the answers bank', lambda S: S['answers'].count('\nANSWER: Answer to the') == 7 and 'option 1' in S['answers'],
     lambda S: put(S, 'answers', S['answers'].replace('ANSWER: Answer to the', 'x', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 24457265`s files', lambda S: S['pushout'][0] == ['data/b591_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b591') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b591'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'epstein-b590': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wl1'].get('line')).startswith(S['wl1'].get('head', '#'))
     and '(:6760)' in fline(S, S['wl1']['line']) and 'b591 AT ITS WEIGHT' in fline(S, S['wl1']['line']) and '12e4176' in fline(S, S['wl1']['line']),
     lambda S: put(S, 'wl1', dict(S['wl1'], line=1))),
    ('G-STANDING-LINE', 'OPEN_TRAILS at the banked standing line', lambda S: oline(S, S['sl'].get('line')).startswith(S['sl'].get('head', '#'))
     and 'no arm is declared on a face before it has been run at HEAD' in oline(S, S['sl']['line']) and '(:12172)' in oline(S, S['sl']['line']),
     lambda S: put(S, 'sl', dict(S['sl'], line=1))),
    ('G-NODE-LISTS', 'the two new node lists against b569`s and b573`s records', lambda S: nodes_ok(S),
     lambda S: put(S, 'nodes_c', S['nodes_c'].replace('Schema.detector | kernel', 'Schema.detectorX | kernel'))),
    ('G-PROBES-BANKED', 'the v0.16 probe banks and the runs` identity flags', lambda S: probes_ok(S) and pages_logs_v016(S),
     lambda S: put(S, 'probe_c', '')),
    ('G-ZETA-HEAD', 'the ζ page at PLACE-papers HEAD: its head at v0.16 and the four faces` lines at their entry tags', lambda S: zeta_head(S),
     lambda S: put(S, 'page_z', [x.replace('v0.16 = `c404e72`', 'v0.11 = `19b7d1e`') for x in S['page_z']])),
    ('G-ZETA-PLACEMENT', 'the Component 1 ζ diff`s added Placement rows', lambda S: zeta_placement(S),
     lambda S: put(S, 'P1', dict(S['P1'], zeta=dict(S['P1'].get('zeta', {}), gone=['x'])))),
    ('G-CHI-NODES', 'the χ page at PLACE-papers HEAD: the detector`s node line and the two schema rows', lambda S: chi_nodes(S),
     lambda S: put(S, 'page_c', [x for x in S['page_c'] if x != EPSTEIN_ROW])),
    ('G-CHI-LAST-960', 'the χ page`s last derived line against REGISTRY :960, afresh', lambda S: chi_960(S),
     lambda S: put(S, 'reg960', S['reg960'].replace("Supportable, the author's sentence: *", "Supportable, the author's sentence: *x"))),
    ('G-CHI-PLACEMENT', 'the χ page`s Placement rows at PLACE-papers HEAD', lambda S: chi_placement(S),
     lambda S: put(S, 'page_c', S['page_c'] + ['| keystone naming a node | `internal/CONVERGENCE.md` |'])),
    ('G-GENERATOR-EDIT-ALONE', 'the relay commit carrying tools/chain_page.py: its files, its time', lambda S: gen_alone(S),
     lambda S: put(S, 'gen_commit', (S['gen_commit'][0], S['gen_commit'][1] + ['data/b592_x.txt']) + tuple(S['gen_commit'][2:]))),
    ('G-GENERATOR-TEST', 'the generator`s b592 test run afresh, against its bank', lambda S: gen_test(S),
     lambda S: put(S, 'gen_test', (1,) + tuple(S['gen_test'][1:]))),
    ('G-KEYSTONE-RULE-CHECKED', 'the keystone match under the generator before and after the edit, both lists', lambda S: rule_checked(S),
     lambda S: put(S, 'rule', dict(S['rule'], z_new=['x']))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since 9059169: four page commits, each one page, two before the edition commit and two after',
     lambda S: pages_alone(S), lambda S: put(S, 'pp_files', {h: ([PAGE, DIR_PAGE] if f in ([PAGE], [DIR_PAGE]) else f) for h, f in S['pp_files'].items()})),
    ('G-PAGES-C2', 'the post-edition re-emits: byte-identical twice, one Placement row each, the edition`s', lambda S: pages_c2_ok(S),
     lambda S: put(S, 'P2', dict(S['P2'], chi=dict(S['P2'].get('chi', {}), identical=False)))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b592`s v0.16 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b592`s v0.16 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm banks after Component 1 and after the post-edition commits', lambda S: arms_page(S, 'arms_c1') and arms_page(S, 'arms_c2'),
     lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-CURRENT-UNEDITED', 'THE_RESIDUE_OF_RH.md on disk and at HEAD against 9059169', lambda S: ed_cur_unedited(S),
     lambda S: put(S, 'cur', (S['cur'][0] + b'x', S['cur'][1], S['cur'][2]))),
    ('G-EDITION-CARRIES', 'the edition at HEAD: every v1.1 line at its offset, unchanged unless rewritten', lambda S: ed_carries(S),
     lambda S: put(S, 'ed', [x.replace('chiasmus', 'chiasmuz') for x in S['ed']])),
    ('G-WORKLIST-ROW', 'the edition`s MOVED row', lambda S: worklist_row(S), lambda S: put(S, 'ed', [x.replace('### **OPEN**', 'OPEN') for x in S['ed']])),
    ('G-SECTION7-REWRITES', 'the edition`s ruled rewrites, each citing the four at their pins', lambda S: ruled_rewrites(S),
     lambda S: put(S, 'ed', [x.replace('`19b7d1e`', '`19b7d1f`') for x in S['ed']])),
    ('G-CREDIT-PLACED', 'the credit line beneath the §7 clause', lambda S: credit_placed(S), lambda S: put(S, 'ed', [x for x in S['ed'] if not x.startswith('*Credit (b450')])),
    ('G-HISTORY-LINES', 'the two history lines beneath their dated entries', lambda S: history_lines(S),
     lambda S: put(S, 'ed', [x for x in S['ed'] if 'missing information' not in x])),
    ('G-VERSION-LINE', 'the v1.2 line above the v1.1 line', lambda S: version_line(S), lambda S: put(S, 'ed', [x.replace('*v1.2 — 2026-10-02', '*v1.2') for x in S['ed']])),
    ('G-BACKMATTER', 'the back matter`s sections in order, its history rows, no blank Status cell', lambda S: backmatter(S),
     lambda S: put(S, 'ed', [x.replace('### Placement', '### Placings') for x in S['ed']])),
    ('G-EDITION-BANK', 'the diff bank`s offset head and its landing line', lambda S: ed_bank(S), lambda S: put(S, 'bank', S['bank'][5:])),
    ('G-H28A-SCORED', 'the work-list rows` citations, the scores, the desk', lambda S: h28a_ok(S), lambda S: put(S, 'H', dict(S['H'], H28a='REFUTED'))),
    ('G-H28B-SCORED', 'the body and the current version counted afresh', lambda S: h28b_ok(S), lambda S: put(S, 'E', dict(S['E'], n_body=1))),
    ('G-H28C-SCORED', 'the scanner run afresh on the edition and the ceiling read afresh', lambda S: h28c_ok(S),
     lambda S: put(S, 'scan_now', S['scan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-FORM-LINES', 'OPEN_TRAILS at the three banked form lines', lambda S: form_lines_ok(S), lambda S: put(S, 'fl', dict(S['fl'], lines=[]))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-ANSWERS-RECORDED', 'this act`s trail record', lambda S: 'b569’s list kept as the record of the v0.11 page' in trail(S)
     and 'the restatement clause entered' in trail(S) and 'their stems carried by history' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('the restatement clause entered', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'BALANCE_AND_POSITIVITY by the same form; the author rules on the closing' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('BALANCE_AND_POSITIVITY by the same form; the author', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-explicit-formula': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b592_record.py'): S['tooltext'].get(os.path.join(T, 'b592_record.py'), '') + NL + 'os' + '.remove(p)'}))),
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
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 652b58d5, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b591_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE, DIR_PAGE, ED]),
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
                                                                          and "startswith('b592')" in S['suite'] and "data/b592_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b592')", ''))),
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
    rec('b592 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b592_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b592_checks_postpush.txt' if pushed else 'b592_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b592_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
