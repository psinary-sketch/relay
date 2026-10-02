# -*- coding: utf-8 -*-
"""b591_checks.py -- THE SUITE OF b591, UNDER (R201): THE LOCATED-CLAUSE METHOD DOCUMENT; THE WITNESS RATIO AS (E3); THE E0
RULE'S EXISTENTIAL-BINDER CLAUSE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b591_checks.txt before the push and data/b591_checks_postpush.txt after
### it. ### The harness is b568's to b590's, carried; the arms are b591's.
### ### **THIS SUITE CARRIES NO SENTENCE OF THE DOCUMENT'S BODY**: G-NO-BODY-PUBLIC builds its needles at run time from the
### TECHNE-Core file.
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
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
FACE = os.path.join(D, 'b591_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='d497de0c', pp='40746b4', gs='3528bcf', te='29208f6')
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
MIRROR_PIN = '192077f'
DOC_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
PRE_HEADS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72'}
STEPZERO = 'fd42f02b'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
L = []
NS = 'SIDEExplicitFormula.Schema.'
MLB = 'membership_load_bearing'
ROMAN = ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii')


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b591')
            and 'data/b591_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
            ch |= set(untracked(PP, 'phase1.5', 'phase2'))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    return cr0(b).decode('utf-8', 'replace').split(NL)


def flat(t):
    return ' '.join(re.sub(r'[*_`]', '', t or '').split())


def sources():
    import b591_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b591_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b591_') and f.endswith('.py')) or f == 'test_e0_existential.py')
    S = dict(
        REC=REC, face=face, ferry=rd('b591_ferry.txt'), scan=rd('b591_ferry_scan.txt'), cens=rd('b591_census_stepzero.txt'),
        fcens=rd('b591_faces_census_stepzero.txt'), pins0=rd('b591_pins_stepzero.txt'), procs=rd('b591_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b590_closing.txt'), reads=rd('b591_reads.txt'), branches=rd('b591_branches.txt'),
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
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b590*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b591_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b591_mustnotexist.txt')), table_changed=None,
        fj=jl('b591_findings.json'), tj=jl('b591_trail.json'), sc=jl('b591_scores.json'), desk=rd('b591_desk_notes.txt'),
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


def _old_rule():
    import types
    src = gs(ROOT, 'show', '%s:tools/e0_rule.py' % PRE['relay'])
    m = types.ModuleType('e0_rule_before')
    exec(compile(src, 'e0_rule_before', 'exec'), m.__dict__)
    return m


def extra_sources(S):
    REC = S['REC']
    import e0_rule as E0
    import g_chain_page as GCP
    X = {}
    X['w1'], X['e3'] = jl('b591_weight_line.json'), jl('b591_e3_line.json')
    e0c = gs(ROOT, 'log', '-1', '--format=%H', '--', 'tools/e0_rule.py')
    X['e0_commit'] = (e0c, files_of(ROOT, e0c), gs(ROOT, 'log', '-1', '--format=%ct', e0c),
                      [l for l in gs(ROOT, 'diff', PRE['relay'], e0c, '--', 'tools/e0_rule.py').split(NL) if l.startswith('-') and not l.startswith('---')])
    r = subprocess.run([sys.executable, os.path.join(T, 'test_e0_existential.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    X['e0_test'] = (r.returncode, r.stdout, rd('b591_e0_test.txt'))
    old = _old_rule()
    head = REC._header_at(V016, 'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', MLB) or ''
    X['mlb'] = (old.grade(head, 'theorem')[0], E0.grade(head, 'theorem')[0])
    X['rg'], X['rg_txt'] = jl('b591_e0_regrade.json'), rd('b591_e0_regrade.txt')
    tt = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    moved, n = [], 0
    for row in tt['rows']:
        m = re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(theorem|lemma)\s+(\S+)(.*)$', row.get('statement') or '', re.S)
        if not m:
            continue
        n += 1
        h = m.group(3).split(':=')[0]
        if old.grade(h, 'theorem')[0] != E0.grade(h, 'theorem')[0]:
            moved.append(row['name'])
    X['census'] = (n, moved)
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b569_nodes.txt'), os.path.join(REC.SP, '_b591_gcp'), os.path.join(D, 'b569_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b573_nodes_chi.txt'), os.path.join(REC.SP, '_b591_gcp'), os.path.join(D, 'b573_chi_probe_out.txt'))
    X['doc_raw'] = raw(REC.DOC)
    X['doc'] = cr0(X['doc_raw']).decode('utf-8', 'replace') if X['doc_raw'] else ''
    X['doc_head'] = cr0(blob(TE, 'HEAD:' + DOC_REL))
    X['te_dir'] = [x.split('/')[-1] for x in gs(TE, 'ls-tree', '--name-only', 'HEAD', 'modules/2026-08/').split(NL) if x.strip()]
    X['te_log'] = [(l.split(' ', 1)[0], files_of(TE, l.split(' ', 1)[0])) for l in gs(TE, 'log', '--reverse', '--pretty=%H %s', PRE['te'] + '..HEAD').split(NL) if l.strip()]
    X['te_origin'], X['te_head'] = gs(TE, 'rev-parse', 'origin/main'), gs(TE, 'rev-parse', 'HEAD')
    X['te_origin_tree'] = gs(TE, 'ls-tree', '--name-only', 'origin/main', '--', DOC_REL)
    X['scan_placed'], X['h32'], X['termscan'] = jl('b591_doc_scan_placed.json'), jl('b591_h32.json'), rd('b591_doc_termscan.txt')
    X['cites'] = rd('b591_doc_citations.txt')
    X['ceil'], X['ceil_txt'], X['scan_d1'] = jl('b591_doc_ceiling_read.json'), rd('b591_doc_ceiling_read.txt'), jl('b591_doc_scan_draft1.json')
    X['tr'] = jl('b591_transfers.json')
    X['table'] = jl('b591_doc_table.json')
    X['tags'] = {}
    for l in gs(KER, 'ls-remote', 'origin', 'refs/tags/v0.*').split(NL):
        if '\t' in l and l.endswith('^{}'):
            sha, ref = l.split('\t')
            X['tags'][ref[len('refs/tags/'):-3]] = sha
    pub = {}
    for p in sorted(glob.glob(os.path.join(D, 'b591_*'))) + S['tools'] + [os.path.join(T, 'e0_rule.py')]:
        pub[os.path.relpath(p, ROOT).replace(os.sep, '/')] = read(p)
    pub['PLACE-papers appended'] = (S['fi_now'] or b'')[len(S['fi_pre'] or b''):].decode('utf-8', 'replace') + \
        (S['ot_now'] or b'')[len(S['ot_pre'] or b''):].decode('utf-8', 'replace')
    pub['SIDE-global-section appended'] = (S['corr_now'] or b'')[len(S['corr_pre'] or b''):].decode('utf-8', 'replace')
    X['public'] = pub
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
def secs(S):
    return S['REC']._sections(S['doc'])


def e0_alone(S):
    c, files, ct, removed = S['e0_commit']
    return files == ['tools/e0_rule.py', 'tools/test_e0_existential.py'] and S['lock_epoch'] is not None and int(ct or 0) > S['lock_epoch'] \
        and len(removed) == 1 and 'BINDER.findall(head)' in removed[0]


def e0_test(S):
    rc, out, bank = S['e0_test']
    return rc == 0 and '7 of 7 cases as wanted -- PASS' in out and '7 of 7 cases as wanted -- PASS' in bank and S['mlb'][0] == 'INTERFACES'


def regrade_ok(S):
    rg = S['rg']
    row = rg.get('rows', {}).get(MLB, {})
    return S['mlb'] == ('INTERFACES', 'DERIVES') and row.get('before') == 'INTERFACES' and row.get('after') == 'DERIVES' \
        and rg.get('table_row') == [['UNGRADED', 0]] and rg.get('corr_rows') == 0 and rg.get('no_grade_moved') is True \
        and rg.get('rows', {}).get('epstein_not_h2_sign_cfg', {}).get('after') == 'INTERFACES'


def census_ok(S):
    n, moved = S['census']
    rg = S['rg']
    return n > 1000 and moved == [NS + 'SaltCheckEpstein.' + MLB] and rg.get('census_n') == n and [x['name'] for x in rg.get('moved', [])] == moved \
        and all(v.get('equal') for v in rg.get('ab', {}).values())


def doc_placed(S):
    b = S['doc_raw'] or b''
    sha = hashlib.sha256(b).hexdigest()
    return bool(b) and sha == S['scan_placed'].get('sha256') == S['h32'].get('sha256') and cr0(b) == S['doc_head'] \
        and {'INDEX.md', 'SIGNEDNESS.md', 'HARNESS_LORE.md'} <= set(S['te_dir'])


def doc_form(S):
    ls = S['doc'].split(NL)
    heads = [m.group(1) for m in re.finditer(r'^## \((\w+)\) ', S['doc'], re.M)]
    return len(ls) > 3 and ls[0].startswith('# THE LOCATED CLAUSE') and '`RiemannHypothesis`' in ls[0] and ls[2] == '*v0.1 — 2026-10-02*' \
        and heads == list(ROMAN) and '### Placement' in S['doc'] and '### Correspondence' in S['doc'] \
        and S['doc'].index('### Placement') > S['doc'].index('## (viii) ')


def doc_sections(S):
    sc = dict(secs(S))
    words = {k: len(v.split()) for k, v in sc.items()}
    body = sum(v for k, v in words.items() if k != 'viii')
    vi = sc.get('vi', '')
    return set(sc) == set(ROMAN) and all(words[k] > 50 for k in ROMAN[:7]) and body == S['scan_placed'].get('body') \
        and vi.count('(PROPOSED)') == 4 and all(x in vi for x in ('BSD', 'Navier', 'Twin primes', 'P versus NP')) \
        and 'salt-checked over the library' in vi


CITE = re.compile(r'(?:\b(?:v0\.\d+ = [0-9a-f]{7}|de5ce8a9|192077f|40746b4)\b|(?:ζ page|χ page|FINDINGS|OPEN_TRAILS|README|SPIRAL_MAP|RESIDUE|THE_METHOD_CANON) :\d+|relay data/\S+)')


def doc_cites(S):
    sc = dict(secs(S))
    return all(CITE.search(sc.get(k, '')) for k in ROMAN[:7]) and S['scan_placed'].get('sha256', '#') in S['cites'] \
        and all(('### (%s) --' % k) in S['cites'] for k in ROMAN)


def h32a_ok(S):
    REC = S['REC']
    import banned_terms as BT
    ceil = [m.group(0) for l in S['doc'].split(NL) for m in REC.CEILING.finditer(l)]
    stems = [m.group(0) for l in S['doc'].split(NL) for m in BT.PAT.finditer(l) if not any(rx.search(l) for rx, _ in BT.EXCEPT)]
    want = 'HOLDS' if not ceil and not stems and re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['termscan'], re.M) else 'REFUTED'
    return bool(S['doc']) and S['h32'].get('H32a') == want and S['sc'].get('H32a', [''])[0] == want and '(H32A)' in S['desk']


def h32b_ok(S):
    pins = S['h32'].get('pins', {})
    ok = bool(pins)
    for p, v in pins.items():
        m = re.match(r'^(v0\.\d+) = ([0-9a-f]{7})$', p)
        if m:
            ok = ok and S['tags'].get(m.group(1), '').startswith(m.group(2))
        elif p in ('192077f', '40746b4'):
            ok = ok and git(PP, 'merge-base', '--is-ancestor', p, 'origin/main')[0] == 0
        elif p == '3528bcf':
            ok = ok and git(GS, 'merge-base', '--is-ancestor', p, 'origin/main')[0] == 0
        elif p == 'de5ce8a9':
            ok = ok and v.get('remote', '').startswith(p) and v.get('ok') is True
        else:
            ok = False
    for k, page in (('ζ', PAGE), ('χ', DIR_PAGE)):
        n = len(lines_of(blob(PP, '%s:%s' % (MIRROR_PIN, page))))
        cited = [int(x) for x in re.findall(r'%s page :(\d+)' % k, S['doc'])] + [int(b) for b in re.findall(r'%s page :\d+-:(\d+)' % k, S['doc'])]
        ok = ok and bool(cited) and max(cited) <= n
    want = 'HOLDS' if ok else 'REFUTED'
    return S['h32'].get('H32b') == want and S['sc'].get('H32b', [''])[0] == want and '(H32B)' in S['desk']


def h32c_ok(S):
    sc = dict(secs(S))
    body = sum(len(v.split()) for k, v in sc.items() if k != 'viii')
    vi = len(sc.get('vi', '').split())
    want = 'HOLDS' if body <= 2500 and 4 * vi <= body else 'REFUTED'
    return body == S['h32'].get('body') and vi == S['h32'].get('vi') and S['h32'].get('H32c') == want \
        and S['sc'].get('H32c', [''])[0] == want and '(H32C)' in S['desk']


def table_rows(S):
    sc = dict(secs(S))
    out = []
    for l in sc.get('viii', '').split(NL):
        m = re.match(r'^\| `([^`]+)` \| (.+?) \| (\S+?):(\d+) \| (\w+) \| (\S+) \|$', l)
        if m:
            out.append(dict(name=m.group(1), pin=m.group(2), file=m.group(3), line=int(m.group(4)), grade=m.group(5), tier=m.group(6)))
    return out


def corr_ok(S):
    rows = table_rows(S)
    sc = dict(secs(S))
    body = ''.join(v for k, v in sc.items() if k != 'viii')
    named = set(re.findall(r'`([A-Za-z_][\w.\']*)`', body))
    last = {r['name'].split('.')[-1] for r in rows} | {r['name'] for r in rows}
    return len(rows) >= 20 and all(S['REC']._resolve_row(r) for r in rows) and named <= last \
        and len(rows) == len(named) and len(rows) == len(S['table'].get('rows', []))


def transfers_ok(S):
    REC = S['REC']
    for name, pat in REC.TRANSFERS:
        hits = REC._mgrep(pat, 'Mathlib', 'Archive', 'Counterexamples')
        if [h for h in hits if re.search(r':\d+:\s*(theorem|lemma|def|structure|class|abbrev|noncomputable def|instance)\b', h)]:
            return False
    ctl = REC._mgrep(REC.CONTROL[1], 'Mathlib')
    vi = dict(secs(S)).get('vi', '')
    named = set(re.findall(r'`([A-Za-z_][\w.\']*)`', vi))
    return len(ctl) == 1 and named <= {'RiemannHypothesis', 'WeierstrassCurve', 'Nat.Prime', 'TM2ComputableInPolyTime'} \
        and S['tr'].get('stated') == [] and gs(MATHLIB, 'rev-parse', 'HEAD').startswith('de5ce8a9')


def ceiling_ok(S):
    c = S['ceil']
    return c.get('corrections') == 1 and c.get('pattern') == 0 and c.get('stems') == 0 and len(c.get('seat', [])) == 1 \
        and c.get('draft1') == S['scan_d1'].get('sha256') and 'CORRECTIONS BEFORE THE SEAL : 1' in S['ceil_txt'] \
        and 'records as RH-false' not in S['doc'] and bool(S['doc'])


def needles(S):
    return S['REC']._prose_sentences(S['doc']) if S['doc'] else []


def no_body_public(S):
    nd = [flat(x) for x in needles(S)]
    if len(nd) < 30:
        return False
    for name, txt in S['public'].items():
        f = flat(txt)
        if any(n in f for n in nd):
            return False
    return True


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 16]) if e else ''
    return fline(S, e) == S['REC'].TITLE and '**The document**' in tail and ('sha256 `%s`' % S['h32'].get('sha256', '#')) in tail \
        and 'TECHNE-Core' in tail and 'not pushed' in tail and '**The E0 rule’s existential-binder clause**' in tail


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R201) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and '### ORPHANS:' in S['procs']
     and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '  1234   5678 grep.exe        2026-09-01 00:00:00  grep x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b590`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b590' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b591 -- x'])),
    ('G-R201-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R201) END' in S['ferry'] and S['ot'].count('**(R201) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R201) ratified', '(R201) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'the b257 drafts` location: D:/MY-DOwnloads/TECHNE-Core/modules/2026-08/', 'INDEX.md @', 'b257_methodology_sweep.txt @',
        'THE_METHOD_CANON.md @', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md @ 192077f', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md @ 192077f',
        'README.md @', 'FINDINGS.md @', 'OPEN_TRAILS.md @', 'THE_RESIDUE_OF_RH.md @', 'SPIRAL_MAP.md @', 'tools/e0_rule.py @ d497de0c',
        'b590_witness_vs_bench.txt @', 'banned_terms.py @', 'b590_closing_push_out.txt @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay fd42f02b`s files', lambda S: S['pushout'][0] == ['data/b590_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b590') == 4, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b590'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'epstein-b590': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['w1'].get('line')).startswith(S['w1'].get('head', '#'))
     and '(:6740)' in fline(S, S['w1']['line']) and 'b590 AT ITS WEIGHT' in fline(S, S['w1']['line'])
     and 'The suite reads 68 of 68.' in fline(S, S['w1']['line']) and '**The witness ratio, entered as a finding' in fline(S, S['w1']['line']),
     lambda S: put(S, 'w1', dict(S['w1'], line=1))),
    ('G-E3-ENTERED', 'OPEN_TRAILS at the banked (E3) line and the lines it addresses', lambda S: oline(S, S['e3'].get('line')).startswith(S['e3'].get('head', '#'))
     and '(E3) THE WITNESS RATIO' in oline(S, S['e3']['line']) and 'priced beside (E1) and (E2), not started' in oline(S, S['e3']['line'])
     and '(C1, :11336)' in oline(S, S['e3']['line']) and oline(S, 11516).startswith('- **(E1)') and oline(S, 11517).startswith('- **(E2)'),
     lambda S: put(S, 'e3', dict(S['e3'], line=11516))),
    ('G-E0-CLAUSE-ALONE', 'the relay commit carrying tools/e0_rule.py: its files, its time, its removed lines', lambda S: e0_alone(S),
     lambda S: put(S, 'e0_commit', (S['e0_commit'][0], S['e0_commit'][1] + ['data/b591_x.txt'], S['e0_commit'][2], S['e0_commit'][3]))),
    ('G-E0-TEST', 'the test run afresh, its bank, and the rule before the clause on the same header', lambda S: e0_test(S),
     lambda S: put(S, 'mlb', ('DERIVES', 'DERIVES'))),
    ('G-E0-REGRADE', 'membership_load_bearing`s header at v0.16 re-graded afresh by both rules, and the regrade json', lambda S: regrade_ok(S),
     lambda S: put(S, 'rg', dict(S['rg'], no_grade_moved=False))),
    ('G-E0-CENSUS', 'every theorem statement of the terminal table re-graded afresh by both rules', lambda S: census_ok(S),
     lambda S: put(S, 'census', (S['census'][0], S['census'][1] + ['x.y']))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b569`s banked probe output against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b573`s banked probe output against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-DOC-PLACED', 'the TECHNE-Core file`s bytes, its HEAD blob, its directory and the banked digests', lambda S: doc_placed(S),
     lambda S: put(S, 'doc_raw', (S['doc_raw'] or b'') + b'x')),
    ('G-DOC-COMMIT-ALONE', 'TECHNE-Core`s log since 29208f6', lambda S: len(S['te_log']) == 1 and S['te_log'][0][1] == [DOC_REL],
     lambda S: put(S, 'te_log', S['te_log'] + [('x', ['y'])])),
    ('G-DOC-NOT-PUSHED', 'TECHNE-Core`s remote-tracking main against its HEAD and its tree', lambda S: S['te_origin'].startswith(PRE['te'])
     and S['te_head'] != S['te_origin'] and S['te_origin_tree'] == '', lambda S: put(S, 'te_origin', S['te_head'])),
    ('G-DOC-FORM', 'the file`s title, version line and headings', lambda S: doc_form(S),
     lambda S: put(S, 'doc', S['doc'].replace('*v0.1 — 2026-10-02*', '*v0.1*'))),
    ('G-DOC-SECTIONS', 'the file`s sections, counted afresh', lambda S: doc_sections(S),
     lambda S: put(S, 'doc', S['doc'].replace('(PROPOSED)', '(proposed)', 1))),
    ('G-DOC-CITATIONS', 'the file`s sections against the citation forms, and the citations bank', lambda S: doc_cites(S),
     lambda S: put(S, 'cites', S['cites'].replace('### (vi) --', '### (vi)'))),
    ('G-H32A-SCORED', 'the file re-read for ceiling and stems, the scanner bank, the scores', lambda S: h32a_ok(S),
     lambda S: put(S, 'h32', dict(S['h32'], H32a='REFUTED'))),
    ('G-H32B-SCORED', 'each pin re-read at its remote (tags by ls-remote, ancestry by remote-tracking main) and each page line at 192077f',
     lambda S: h32b_ok(S), lambda S: put(S, 'tags', dict(S['tags'], **{'v0.2': '0' * 40}))),
    ('G-H32C-SCORED', 'the body and section (vi) counted afresh', lambda S: h32c_ok(S), lambda S: put(S, 'h32', dict(S['h32'], body=1))),
    ('G-CORR-TABLE', 'the file`s Correspondence rows, each resolved at its pin afresh, against the names the body gives', lambda S: corr_ok(S),
     lambda S: put(S, 'doc', S['doc'].replace('| `RiemannHypothesis` |', '| `RiemannHypothesisX` |'))),
    ('G-TRANSFERS-ABSENT', 'Mathlib at de5ce8a9 searched afresh, the control, and section (vi)`s names', lambda S: transfers_ok(S),
     lambda S: put(S, 'tr', dict(S['tr'], stated=['BSD']))),
    ('G-CEILING-READ', 'the ceiling-read bank against the first draft`s scan and the placed file', lambda S: ceiling_ok(S),
     lambda S: put(S, 'ceil', dict(S['ceil'], corrections=0))),
    ('G-NO-BODY-PUBLIC', 'every relay file this act writes and every appended PLACE-papers and SIDE-global-section byte, against needles '
                         'built at run time from the TECHNE-Core file', lambda S: no_body_public(S),
     lambda S: put(S, 'public', dict(S['public'], **{'data/b591_x.txt': (needles(S) or ['x'])[0]}))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-ANSWER-RECORDED', 'this act`s trail record', lambda S: 'struck as the navigator’s and recorded here' in trail(S)
     and 'committed alone locally and not pushed' in trail(S) and DOC_REL in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('struck as the navigator’s and recorded here', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'the RESIDUE edition by the form; the author rules on the closing' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('the RESIDUE edition by the form; the author', 'x'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{DIR_PAGE: ((S['pages'][DIR_PAGE][0] or b'') + b'x', S['pages'][DIR_PAGE][1])}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-explicit-formula': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b591_record.py'): S['tooltext'].get(os.path.join(T, 'b591_record.py'), '') + NL + 'os' + '.remove(p)'}))),
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
     lambda S: put(S, 'keystone_changes', ['phase2/method/THE_LOCATED_CLAUSE_METHOD.md'])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at d497de0c, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b590_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == ['FINDINGS.md', 'OPEN_TRAILS.md'],
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['phase2/method/THE_LOCATED_CLAUSE_METHOD.md']))),
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
                                                                          and "startswith('b591')" in S['suite'] and "data/b591_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b591')", ''))),
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
    rec('b591 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b591_checks_postpush.txt' if pushed else 'b591_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b591_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
