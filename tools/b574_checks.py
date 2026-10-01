# -*- coding: utf-8 -*-
"""b574_checks.py -- THE SUITE OF b574, UNDER (R184): CP-5, THE DEPOSIT READ WITH NO WRITE AT ZENODO; THE ζ PAGE'S GENERATOR.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b574_checks.txt before the push and data/b574_checks_postpush.txt after
### it. ### The harness is b568's to b573's, carried; the arms are b574's.
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
FACE = os.path.join(D, 'b574_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='337d5eef', pp='dd87bdc', gs='8c392fe')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}
STEPZERO = 'ea7b1f28'
COMMITS = dict(pushout=(STEPZERO, ['data/b573_closing_push_out.txt', 'data/b573_housekeeping_push_out.txt']),
               generator=('69c2ae5a', ['tools/chain_page.py', 'tools/test_chain_page.py']))
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RECORDS = ('21539167', '21520474')
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
        return cr0(open(p, 'rb').read())
    except OSError:
        return None


def blob_id(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def files_of(sha):
    return sorted(x for x in gs(ROOT, 'show', '--name-only', '--pretty=format:', sha).split(NL) if x.strip())


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b574')
            and 'data/b574_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section)/[^`\s]+)`', w)))


def written_files(lock_epoch):
    out = set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay']).split(NL) if x.strip())
    out |= set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay'], 'HEAD').split(NL) if x.strip())
    for l in git(ROOT, 'status', '--porcelain', '--untracked-files=all', '--', 'data', 'tools')[1].split(NL):
        if l.startswith('?? '):
            p = l[3:].strip()
            try:
                if os.path.getmtime(os.path.join(ROOT, p)) > lock_epoch - 3 * 3600:
                    out.add(p)
            except OSError:
                pass
    res = ['relay/' + x for x in out]
    for repo, name, pre in ((PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def sources():
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b574_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b574_') and f.endswith('.py'))
    fetch = rd('b574_zenodo_fetch.txt')
    S = dict(
        face=face, ferry=rd('b574_ferry.txt'), scan=rd('b574_ferry_scan.txt'), cens=rd('b574_census_stepzero.txt'),
        fcens=rd('b574_faces_census_stepzero.txt'), pins0=rd('b574_pins_stepzero.txt'), procs=rd('b574_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b573_closing.txt'), reads=rd('b574_reads.txt'), branches=rd('b574_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        commits={k: (files_of(v[0]), v[1], subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', v[0], 'HEAD']).returncode == 0)
                 for k, v in COMMITS.items()},
        gen_ct=int(gs(ROOT, 'log', '-1', '--pretty=%ct', COMMITS['generator'][0]) or 0),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        fj=jl('b574_findings.json'), tj=jl('b574_trail.json'), wt=jl('b574_weight.json'), wj=jl('b574_word.json'),
        tcp=rd('b574_test_chain_page.txt'), runs=rd('b574_page_runs.txt'),
        fetch=fetch, fj_fetch=jl('b574_zenodo_fetch.json'), resp={r: jl('b574_fetch_%s.json' % r) for r in RECORDS},
        fetch_epoch=min([e for e in (iso_epoch(x) for x in re.findall(r'at \(UTC\) (\S+Z) ; HTTP', fetch)) if e] or [0]),
        c1_mtime=max(os.path.getmtime(os.path.join(D, f)) if os.path.exists(os.path.join(D, f)) else 4102444800
                     for f in ('b574_weight.json', 'b574_word.json', 'b574_page_runs.txt', 'b574_test_chain_page.txt')),
        pins=rd('b574_pins.txt'), pj=jl('b574_pins.json'), led=rd('b574_ledgers.txt'), lj=jl('b574_ledgers.json'),
        ej=jl('b574_errata.json'), draft=rd('b574_description_draft.txt'),
        sc=jl('b574_scores.json'), desk=rd('b574_desk_notes.txt'),
        reg_now=read(os.path.join(PP, 'REGISTRY.md')),
        ledg={f: (raw(os.path.join(PP, f)), cr0(blob(PP, PRE['pp'] + ':' + f))) for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md')},
        pages={p: (blob(PP, 'HEAD:' + p), blob(PP, PRE['pp'] + ':' + p)) for p in (PAGE, DIR_PAGE)},
        errata_now=raw(os.path.join(PP, 'ERRATA.md')), errata_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')),
        faces_now=raw(os.path.join(PP, 'FACES_LEDGER.md')), faces_pre=cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md')),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=raw(os.path.join(PP, 'OPEN_TRAILS.md')),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kmain=gs(KER, 'rev-parse', 'main'), kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b573*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        dep_clean=gs(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == '',
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b574_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b574_mustnotexist.txt')), table_changed=None,
    )
    import g_chain_page as GCP
    S['gcp_zeta'] = GCP.arm(os.path.join(D, 'b569_nodes.txt'), os.path.join(D, '_b574_gcp_tmp'), os.path.join(D, 'b569_probe_out.txt'))
    S['gcp_chi'] = GCP.arm(os.path.join(D, 'b573_nodes_chi.txt'), os.path.join(D, '_b574_gcp_tmp'), os.path.join(D, 'b573_chi_probe_out.txt'))
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
    pp_changed = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    pp_changed |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    S['pp_changed'] = sorted(pp_changed)
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
    i = t.find('### b574 — lane three, act two under (R184)')
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return not [f for f, t in S['tooltext'].items() if pat.search(t)]


# ### a write-method or a token read in this act's tools: any HTTP method but GET, any requests write call, a urlopen with a body
GET_LIT = 'method=' + "'G" + "ET'"
WRITE_RX = re.compile(r"method\s*=\s*['\"](?!GET['\"])[A-Z]+['\"]|requests\.(post|put|patch|delete)\b|urlopen\([^)]*data\s*=|"
                      + 'ZENODO' + '_' + 'TOKEN')


def no_zenodo_write(S):
    return (not [f for f, t in S['tooltext'].items() if WRITE_RX.search(t)]
            and GET_LIT in S['tooltext'].get(os.path.join(T, 'b574_record.py'), ''))


def alone(S, k):
    c = S['commits'][k]
    return c[0] == sorted(c[1]) and c[2]


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def fetch_ok(S):
    reqs = [l for l in S['fetch'].split(NL) if l.startswith('### REQUEST : ')]
    return (len(reqs) == 2 and all(l.startswith('### REQUEST : GET https://zenodo.org/api/records/') for l in reqs)
            and all('Authorization header sent : False' in l and ' HTTP 200 ' in l for l in reqs)
            and not any(v.get('auth') for v in S['fj_fetch'].values()))


def draft_sentences(S):
    t = S['draft']
    if '### THE DRAFT' not in t or '### NOTE FOR THE RULING' not in t:
        return []
    body = t[t.index('### THE DRAFT'):t.index('### NOTE FOR THE RULING')].split(NL)[1:]
    return [l for l in body if l.strip()]


def norm(s):
    return ' '.join(s.split())


WT_HEAD = '*Appended 2026-10-01 by b574 to b573’s entry ('
WORD_HEAD = '*Appended 2026-10-01 by b574, under the author’s ruling `(R184)`(3), to the W-ORD-GRH-WEIL entry'
TITLE = '## CP-5, act one: the deposit read against REGISTRY'
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R184) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '  1234   5678 lean.exe        2026-09-01 00:00:00  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b573`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b573' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b574 -- x'])),
    ('G-R184-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R184) END' in S['ferry'] and S['ot'].count('**(R184) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R184) ratified', '(R184) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('chain_page.py @', 'REGISTRY.md @', 'README.md @', 'SPIRAL_MAP.md @',
                                                                               'ERRATA.md @', 'b535_zenodo.py @', 'OPEN_TRAILS.md @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay ea7b1f28`s files', lambda S: alone(S, 'pushout'),
     lambda S: put(S, 'commits', dict(S['commits'], pushout=(['x'], S['commits']['pushout'][1], True)))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b573') == 6, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b573'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-GENERATOR-ALONE', 'relay 69c2ae5a`s files', lambda S: alone(S, 'generator'),
     lambda S: put(S, 'commits', dict(S['commits'], generator=(['tools/chain_page.py'], S['commits']['generator'][1], True)))),
    ('G-GENERATOR-TEST', 'the test bank', lambda S: '31 of 31 cases as wanted -- PASS' in S['tcp'] and '(15) the χ list re-emitted' in S['tcp'],
     lambda S: put(S, 'tcp', S['tcp'].replace('31 of 31', '30 of 31'))),
    ('G-CHAIN-PAGE', 'the ζ page regenerated from b569`s list against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page regenerated from its list against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGES-TWICE', 'the runs bank against both committed pages', lambda S: S['runs'].count('BYTE-IDENTICAL') == 4
     and all(S['pages'][p][0] is not None and hashlib.sha256(S['pages'][p][0]).hexdigest() in S['runs'] for p in (PAGE, DIR_PAGE)),
     lambda S: put(S, 'runs', S['runs'].replace('BYTE-IDENTICAL', 'DIFFER', 1))),
    ('G-COMPONENT1-FIRST', 'the generator commit and the Component 1 banks` times against the fetch', lambda S: S['fetch_epoch'] > 0
     and S['gen_ct'] < S['fetch_epoch'] and S['c1_mtime'] < S['fetch_epoch'] and S['gen_ct'] > (S['lock_epoch'] or 0),
     lambda S: put(S, 'c1_mtime', 4102444800)),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wt'].get('lines', [0])[0]).startswith(WT_HEAD)
     and 'b573 AT ITS WEIGHT' in fline(S, S['wt'].get('lines', [0])[0]) and 'v0.15 = `21c8c52`' in fline(S, S['wt'].get('lines', [0])[0]),
     lambda S: put(S, 'wt', dict(S['wt'], lines=[1, 2]))),
    ('G-INSTRUMENT-LINE', 'FINDINGS at the banked instrument line', lambda S: len(S['wt'].get('lines', [])) == 2
     and fline(S, S['wt']['lines'][1]).startswith(WT_HEAD) and 'THE LEMMA WALK' in fline(S, S['wt']['lines'][1]),
     lambda S: put(S, 'wt', dict(S['wt'], lines=[S['wt'].get('lines', [0])[0], 2]))),
    ('G-WORD-CLOSED', 'OPEN_TRAILS at the closing line', lambda S: oline(S, (S['wj'].get('lines') or [0])[0]).startswith(WORD_HEAD)
     and 'CLOSED AT ITS LANDING' in oline(S, (S['wj'].get('lines') or [0])[0]), lambda S: put(S, 'wj', dict(S['wj'], lines=[1]))),
    ('G-REMAINDERS', 'OPEN_TRAILS at the four remainder lines', lambda S: len(S['wj'].get('lines', [])) == 5
     and all(('REMAINDER %d, A PRICED ITEM, NOT STARTED' % i) in oline(S, n) and oline(S, n).startswith(WORD_HEAD)
             and 'Trigger: the author’s word.' in oline(S, n) for i, n in enumerate(S['wj']['lines'][1:], 1)),
     lambda S: put(S, 'wj', dict(S['wj'], lines=S['wj'].get('lines', [])[:4]))),
    ('G-FETCH-BANKED', 'the fetch bank and the two responses banked whole', lambda S: all(str(S['resp'][r].get('id')) == r for r in RECORDS)
     and all(('banked whole as data/b574_fetch_%s.json' % r) in S['fetch'] for r in RECORDS) and set(S['fj_fetch']) == set(RECORDS),
     lambda S: put(S, 'resp', dict(S['resp'], **{'21520474': {}}))),
    ('G-FETCH-NO-WRITE', 'the fetch bank`s request lines', lambda S: fetch_ok(S),
     lambda S: put(S, 'fetch', S['fetch'].replace('### REQUEST : GET', '### REQUEST : PUT', 1))),
    ('G-PINS-BANKED', 'the pins bank and json', lambda S: len(S['pj'].get('files', [])) == 11 and '**FILES: 11 ; DIFFERING: 0.**' in S['pins']
     and S['pj'].get('lf_only') == ['A_Place_to_Stand.md', 'ERRATA.md'] and 'CRLF restored' in S['pins'],
     lambda S: put(S, 'pj', dict(S['pj'], files=[]))),
    ('G-H26A-SCORED', 'the scores and the desk', lambda S: scored(S, 'H26a') and 'line endings alone' in S['sc']['H26a'][1], lambda S: put(S, 'desk', '')),
    ('G-H26B-SCORED', 'the scores and the desk', lambda S: scored(S, 'H26b'), lambda S: put(S, 'desk', '')),
    ('G-ANOMALY1-FROM-FETCH', 'the fetched kernel record and the pins json', lambda S: S['resp']['21520474'].get('metadata', {}).get('version') == 'v1.5'
     and len(S['pj'].get('pin_differences', [])) == 1 and 'WORKING-HEAD' in S['pj']['pin_differences'][0]['kind']
     and (S['pj'].get('kernel_latest') or [''])[0] == 'v1.7', lambda S: put(S, 'pj', dict(S['pj'], pin_differences=[]))),
    ('G-LEDGERS-BANKED', 'the ledgers bank and json', lambda S: S['lj'].get('total') == 3 and S['lj'].get('control', {}).get('fires') is True
     and '### NOT HAND-READ' not in S['led'] and '**DIFFERENCES IN TOTAL (matcher v2): 3' in S['led'],
     lambda S: put(S, 'led', S['led'] + '### NOT HAND-READ')),
    ('G-H26C-SCORED', 'the scores and the desk', lambda S: scored(S, 'H26c'), lambda S: put(S, 'desk', '')),
    ('G-NO-README-EDIT', 'README, REGISTRY and SPIRAL_MAP against their pre-act blobs', lambda S: all(n is not None and p and n == p for n, p in S['ledg'].values()),
     lambda S: put(S, 'ledg', dict(S['ledg'], **{'README.md': ((S['ledg']['README.md'][0] or b'') + b'x', S['ledg']['README.md'][1])}))),
    ('G-ERRATA-LOCATED', 'the errata json', lambda S: len(S['ej'].get('rows', [])) == 7 and all(r['heading'] and r['label'] for r in S['ej']['rows']),
     lambda S: put(S, 'ej', dict(S['ej'], rows=[dict(S['ej']['rows'][0], heading=[])] + S['ej']['rows'][1:]))),
    ('G-H26D-SCORED', 'the scores and the desk', lambda S: scored(S, 'H26d'), lambda S: put(S, 'desk', '')),
    ('G-DRAFT-BANKED', 'the draft bank', lambda S: len(draft_sentences(S)) == 3 and 'NOTHING HERE IS WRITTEN AT ZENODO' in S['draft']
     and all(('(R%s)' % r) in S['draft'] for r in ('177)(2', '182)(2', '183)(3')), lambda S: put(S, 'draft', S['draft'].replace('### THE DRAFT', '### A DRAFT'))),
    ('G-DRAFT-WORDS', 'the draft`s sentences against REGISTRY', lambda S: len(draft_sentences(S)) == 3
     and all(norm(s) in norm(S['reg_now']) for s in draft_sentences(S)), lambda S: put(S, 'draft', S['draft'].replace('classK', 'class K', 1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(TITLE),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b574 — lane three, act two under (R184)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'the reconciling edits and the description edit as the author rules them' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('the reconciling edits and the description edit as the author rules them', 'x'))),
    ('G-PAGE-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{PAGE: ((S['pages'][PAGE][0] or b'') + b'x', S['pages'][PAGE][1])}))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against the pre-act blob', lambda S: S['errata_pre'] and S['errata_now'] == S['errata_pre'],
     lambda S: put(S, 'errata_now', (S['errata_now'] or b'') + b'x')),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff', lambda S: S['kmain'] == V015
     and S['kcur'] == 'main' and S['kdirty'] == '' and all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] == [],
     lambda S: put(S, 'kcur', 'v0.11')),
    ('G-NO-ZENODO-CALL', 'this act`s tools, prose stripped', lambda S: no_zenodo_write(S),
     lambda S: put(S, 'tooltext', {f: t.replace(GET_LIT, 'method=' + "'P" + "UT'") for f, t in S['tooltext'].items()})),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b574_record.py'): S['tooltext'].get(os.path.join(T, 'b574_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'the deposited outputs` status', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces_pre'] and S['faces_now'] == S['faces_pre'],
     lambda S: put(S, 'faces_now', (S['faces_now'] or b'') + b'x')),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 337d5eef, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b573_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == ['FINDINGS.md', 'OPEN_TRAILS.md'],
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 7)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b574')" in S['suite'] and "data/b574_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b574')", ''))),
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
    rec('b574 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    rec('  ### G-NO-ZENODO-CALL read %d tools: %s' % (len(S['tools']), [os.path.basename(f) for f in S['tools']]))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b574_checks_postpush.txt' if pushed else 'b574_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b574_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
