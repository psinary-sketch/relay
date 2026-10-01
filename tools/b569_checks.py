# -*- coding: utf-8 -*-
"""b569_checks.py -- THE SUITE OF b569, UNDER (R179): GRH-WEIL ACT FOUR; THE PAGE'S CONVERSES; THE INSTRUMENTS.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block, read off the face (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the
### terminal table (R107) unless `--rerun-postpush <name>`; it writes data/b569_checks.txt before the push and
### data/b569_checks_postpush.txt after it. ### The harness is b568's (tools/b568_checks.py), carried; the arms are b569's.
### ### G-CHAIN-PAGE regenerates the page from data/b569_nodes.txt by one lean call (tools/g_chain_page.py) and compares it
### with PLACE-papers HEAD's committed blob, byte for byte.
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

import asof as AF             # noqa: E402
import banned_terms as BT     # noqa: E402
import chain_page as C        # noqa: E402
import g_chain_page as G      # noqa: E402
import table_gate as TG       # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
FACE = os.path.join(D, 'b569_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
PRE = dict(relay='b2ed4f2e', pp='f2e93b0', gs='b37870f')
V010, V011 = '6baed63ae664a22db1f325177b81253e270de6e3', '19b7d1e48a40ca22618722306194404423dca224'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83'}
COMMITS = dict(pushout=('3f1d1900', ['data/b568_closing_push_out.txt', 'data/b568_housekeeping_push_out.txt']),
               asof=('54cc6f9c', ['tools/asof.py', 'tools/asof_lines.py', 'tools/b566_checks.py', 'tools/b567_checks.py', 'tools/test_asof.py']),
               tier=('afe32bba', ['tools/chain_page.py', 'tools/test_chain_page.py']),
               table=('93cc2f4f', ['tools/push_gated.sh', 'tools/table_gate.py', 'tools/test_push_gated.sh']),
               a6=('386a2572', ['tools/FERRY_STANDING.md']))
CHI = ['ZetaGrowth', 'LocalCount', 'ZeroSummability', 'XiLogDeriv', 'CountByIntegral', 'Landau', 'GoodHeights']
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


def blob_id(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def files_of(sha):
    return sorted(x for x in gs(ROOT, 'show', '--name-only', '--pretty=format:', sha).split(NL) if x.strip())


def utc_epoch(text, label):
    m = re.search(re.escape(label) + r'[^0-9]*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', text)
    if not m:
        return None
    import calendar
    import time
    return calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%SZ'))


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b569')
            and 'data/b569_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def kernel_build_ok(m):
    b = rd('b569_build_%s.txt' % m.lower())
    return ('Built SIDEExplicitFormula.Chi.%s' % m) in b and re.search(r'^=== END \S+ rc=0$', b, re.M) is not None


def sources():
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b569_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    page_head = blob(PP, 'HEAD:' + PAGE)
    page_now = open(os.path.join(PP, PAGE), 'rb').read() if os.path.exists(os.path.join(PP, PAGE)) else None
    readme = blob(PP, 'HEAD:README.md') or b''
    kre_old, kre_new = cr0(blob(KER, V010 + ':README.md')), cr0(blob(KER, 'main:README.md'))
    S = dict(
        face=face, ferry=rd('b569_ferry.txt'), scan=rd('b569_ferry_scan.txt'), cens=rd('b569_census_stepzero.txt'),
        fcens=rd('b569_faces_census_stepzero.txt'), pins=rd('b569_pins_stepzero.txt'), procs=rd('b569_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b568_closing.txt'), reads=rd('b569_reads.txt'), branches=rd('b569_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        commits={k: (files_of(v[0]), v[1], subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', v[0], 'HEAD']).returncode == 0)
                 for k, v in COMMITS.items()},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), corr=read(os.path.join(GS, 'CORRESPONDENCE.md')),
        fj=jl('b569_findings.json'), tj=jl('b569_trail.json'), rj=jl('b569_rows.json'), sc=jl('b569_scores.json'), desk=rd('b569_desk_notes.txt'),
        stmts=rd('b569_converse_statements.txt'), cv=jl('b569_converses.json'), cbuild=rd('b569_converse_build.txt'),
        e0c=jl('b569_e0_converses.json'), e0x=jl('b569_e0_chi.json'), h20b=jl('b569_h20b.json'),
        nodes=C.read_nodes(os.path.join(D, 'b569_nodes.txt')), nodes568=C.read_nodes(os.path.join(D, 'b568_nodes.txt')),
        nodes_pin=C.node_pin(os.path.join(D, 'b569_nodes.txt')), runs=rd('b569_page_runs.txt'),
        tasof=rd('b569_test_asof.txt'), asof_ok=AF.self_test(), asof_lines_src=read(os.path.join(T, 'asof_lines.py')),
        comp6=AF.repo_asof(D, 'b566'), comp7=AF.repo_asof(D, 'b567'),
        r566=rd('b569_b566_rerun.txt'), r567=rd('b569_b567_rerun.txt'),
        tgen=rd('b569_test_chain_page.txt'), tgen11=rd('b569_test_chain_page_v011.txt'), tier_key=C.TIER_KEY,
        tpg=rd('b569_test_push_gated.txt'), pg=read(os.path.join(T, 'push_gated.sh')), tg_ok=TG.self_test(),
        standing=read(os.path.join(T, 'FERRY_STANDING.md')),
        bk=jl('b569_bulka_generic.json'), bktxt=rd('b569_bulka_generic.txt'), rt=jl('b569_route.json'),
        builds={m: kernel_build_ok(m) for m in CHI}, hold=rd('b569_hold_verticalline.txt'), bpush=rd('b569_branches_push_out.txt'),
        kpush=rd('b569_kernel_push_out.txt'), rowgen=jl('b569_rowgen.json'),
        kmain=gs(KER, 'rev-parse', 'main'), kff=subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', V010, 'main']).returncode == 0,
        kns=[x for x in gs(KER, 'diff', '--name-status', V010, 'main').split(NL) if x.strip()],
        kre_prefix=bool(kre_old) and kre_new.startswith(kre_old), kre_new=kre_new.decode('utf-8', 'replace'),
        held_tip=gs(KER, 'rev-parse', 'grh-weil-b569-held'), held_main=subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor',
                                                                                       'grh-weil-b569-held', 'main']).returncode == 0,
        page=page_head if page_head is not None else page_now, page_committed=page_head is not None,
        readme121=readme.split(b'\n')[120] if len(readme.split(b'\n')) > 120 else b'',
        errata_now=cr0(open(os.path.join(PP, 'ERRATA.md'), 'rb').read()), errata_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')),
        faces_now=cr0(open(os.path.join(PP, 'FACES_LEDGER.md'), 'rb').read()), faces_pre=cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md')),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read()),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b568*') for r in ('D:/relay', PP, GS, KER)},
        tools9=[os.path.join(T, f) for f in os.listdir(T) if f.startswith('b569_') or f in ('asof.py', 'asof_lines.py', 'table_gate.py', 'chain_page.py')],
        dep_clean=gs(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == '',
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b569_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b569_mustnotexist.txt')),
        table_changed=None,
    )
    S['zen'] = [f for f in S['tools9'] if ('https://' + 'zenodo' + '.org') in read(f)]
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
        raw = open(fp, 'rb').read() if os.path.exists(fp) else None
        if raw is None or i not in (blob_id(raw), blob_id(cr0(raw))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    pp_changed = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    pp_changed |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    S['pp_changed'] = sorted(pp_changed)
    S['stem_hits'] = [m.group(0) for l in (S['page'] or b'').decode('utf-8').split(NL) for m in BT.PAT.finditer(l)]
    rec('  ### G-CHAIN-PAGE: regenerating the page by one lean call (tools/g_chain_page.py) ...')
    import tempfile
    S['arm'] = G.arm(os.path.join(D, 'b569_nodes.txt'), tempfile.mkdtemp(), None, committed=S['page'])
    rec('  ### G-CHAIN-PAGE regeneration: exit %d ; %s ; committed at PLACE-papers HEAD: %s' % (S['arm']['rc'], S['arm']['log'][-1:],
                                                                                            S['page_committed']))
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
    i = t.find('### b569 — lane two, act nine under (R179)')
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    # ### the needle is BUILT from fragments (b568's defect (j)), so it cannot match its own definition
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item']
    pat = re.compile(r'\b(' + '|'.join(words) + r')\b')
    return not [f for f in S['tools9'] if pat.search(strip_prose(read(f)))]


def alone(S, k):
    c = S['commits'][k]
    return c[0] == sorted(c[1]) and c[2]


def corr_rows_ok(S):
    rows = [l for l in S['corr'].split(NL) if re.match(r'^\| 41[4-9] \|', l)]
    nums = sorted(l.split('|')[1].strip() for l in rows)
    final = {}
    for o in S['rj'].get('rows', []):
        final[o['row']] = o['exit']
    return nums == ['414', '415', '416', '417', '418', '419'] and all(v == 0 for v in final.values()) and len(final) == 6


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R179) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins'],
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: its positive control present, no orphan',
     lambda S: 'powershell.exe' in S['procs'] and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '  1234   5678 lean.exe        2026-09-01 00:00:00  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the face`s lock time against every later commit`s time',
     lambda S: S['lock_epoch'] is not None and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith('3f1d1900')),
     lambda S: put(S, 'lock_epoch', 4102444800)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line (its last run)', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify`s verdict line', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b568`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b568' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'the face`s section (0) and relay`s log before the lock: 3f1d1900 alone',
     lambda S: 'Nothing but reads and the step-zero banks' in S['face'] and S['lock_epoch'] is not None
     and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == ['3f1d1900'],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b569 -- x'])),
    ('G-R179-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R179) END' in S['ferry'] and S['ot'].count('**(R179) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R179) ratified', '(R179) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('WeilEF/Main.lean @', ':286', 'ZetaBoundsStrip.lean @', ':123',
                                                                                  'modules: ')) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay commit 3f1d1900 -- b568`s two push-out banks alone, in HEAD`s ancestry', lambda S: alone(S, 'pushout'),
     lambda S: put(S, 'commits', dict(S['commits'], pushout=(['x'], S['commits']['pushout'][1], True)))),
    ('G-BRANCHES-DELETED', 'the four repositories` branch lists and the bank',
     lambda S: all(v == '' for v in S['push_lists'].values()) and S['branches'].count('Deleted branch push-b568') == 5,
     lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b568'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'li-weil-b561': '0000000'}))),
    ('G-CONVERSE-STATEMENTS-FIRST', 'the statements bank`s time against the build`s start', lambda S: S['cv'].get('statements_first') is True
     and 'taylorCoeff_nonneg_iff_rh' in S['stmts'], lambda S: put(S, 'cv', dict(S['cv'], statements_first=False))),
    ('G-CONVERSES-BUILT', 'the converse build bank', lambda S: 'Built SIDEExplicitFormula.PageConverses' in S['cbuild']
     and re.search(r'^=== END \S+ rc=0$', S['cbuild'], re.M) is not None and 'PageConverses.lean:' not in S['cbuild'],
     lambda S: put(S, 'cbuild', S['cbuild'].replace('rc=0', 'rc=1'))),
    ('G-CONVERSE-PRINTS', 'the converse prints in the E0 json', lambda S: len(S['e0c'].get('rows', {})) == 4 and all(r['std3'] for r in S['e0c']['rows'].values()),
     lambda S: put(S, 'e0c', dict(S['e0c'], rows={}))),
    ('G-CONVERSE-GRADES', 'the converse E0 json', lambda S: S['e0c'].get('gate') is True and all(r['grade'] == 'DERIVES' for r in S['e0c']['rows'].values()),
     lambda S: put(S, 'e0c', dict(S['e0c'], gate=False))),
    ('G-NODES-EXTENDED', 'the node list, read by the generator`s own reader, against b568`s',
     lambda S: len(S['nodes'][0]) == 25 and S['nodes'][0][:23] == S['nodes568'][0] and S['nodes_pin'] == ('v0.11', V011)
     and [n['name'].split('.')[-1] for n in S['nodes'][0][23:]] == ['register4_positivity_liCoeff_iff_rh', 'taylorCoeff_nonneg_iff_rh'],
     lambda S: put(S, 'nodes', (S['nodes'][0][:24], [], [], []))),
    ('G-PAGE-REGENERATED', 'the two runs` bank and the committed page', lambda S: 'byte-identical: True' in S['runs'] and S['page_committed']
     and ('run one %s' % hashlib.sha256(S['page'] or b'').hexdigest()) in S['runs'], lambda S: put(S, 'page', (S['page'] or b'') + b'x')),
    ('G-H20B-RESCORED', 'the H20b json and the scores', lambda S: S['h20b'].get('h20b') == 'HELD' and all(r['iff'] for r in S['h20b'].get('rows', []))
     and scored(S, 'H20b'), lambda S: put(S, 'h20b', dict(S['h20b'], h20b='REFUTED'))),
    ('G-ASOF-LINES-INSTRUMENT', 'the reader`s self-test, the writer`s text, the test bank', lambda S: S['asof_ok'] and '24 of 24 cases as wanted -- PASS' in S['tasof']
     and 'NOTHING WRITTEN' in S['asof_lines_src'], lambda S: put(S, 'tasof', '')),
    ('G-ASOF-ALONE', 'relay commit 54cc6f9c`s files', lambda S: alone(S, 'asof'),
     lambda S: put(S, 'commits', dict(S['commits'], asof=(['x'], S['commits']['asof'][1], True)))),
    ('G-ASOF-TWO-REPOS', 'the test bank`s false-claim cases across PLACE-papers and the kernel',
     lambda S: len(re.findall(r'^  \(8\) .* FAIL \(read FAIL\)\s+PASS$', S['tasof'], re.M)) == 3
     and len(re.findall(r'^  \(10\) .* FAIL \(read FAIL\)\s+PASS$', S['tasof'], re.M)) == 2, lambda S: put(S, 'tasof', S['tasof'].replace('(8)', '(x)'))),
    ('G-ASOF-COMPANIONS', 'the two companion banks, read by asof.repo_asof',
     lambda S: S['comp6'][1] == 'b569_asof_b566.txt' and S['comp7'][1] == 'b569_asof_b567.txt' and len(S['comp6'][0]) == 13 and len(S['comp7'][0]) == 13
     and S['comp6'][0].get('SIDE-explicit-formula', '').startswith('e5a5a83') and S['comp7'][0].get('bulka') == AF.DELETED,
     lambda S: put(S, 'comp6', ({}, None))),
    ('G-B566-RERUN-COUNTED', 'b566`s re-run bank', lambda S: 'ARMS RUN : 74. ### LIVE PASSING : 74.' in S['r566'] and 'THE AS-OF LINES : b569_asof_b566.txt' in S['r566'],
     lambda S: put(S, 'r566', '')),
    ('G-B567-RERUN-COUNTED', 'b567`s re-run bank', lambda S: 'ARMS RUN : 69. ### LIVE PASSING : 69.' in S['r567'] and 'THE AS-OF LINES : b569_asof_b567.txt' in S['r567'],
     lambda S: put(S, 'r567', '')),
    ('G-TIER-KEY', 'the committed page`s head line and its node lines', lambda S: S['page'] is not None and S['tier_key'] in S['page'].decode('utf-8').split(NL)[2]
     and all(' (table: ' in l for l in S['page'].decode('utf-8').split(NL) if re.match(r'^\d+\. `', l)),
     lambda S: put(S, 'page', (S['page'] or b'').replace(S['tier_key'].encode('utf-8'), b''))),
    ('G-TIER-CONFLICT-REFUSED', 'the generator`s test bank, case (7)', lambda S: re.search(r'^  \(7\) a table tier T2 .*exit 7, no page \(read 7\)\s+PASS$', S['tgen'], re.M) is not None
     and '18 of 18 cases as wanted -- PASS' in S['tgen'] and '17 of 17 cases as wanted -- PASS' in S['tgen11'], lambda S: put(S, 'tgen', '')),
    ('G-TIER-ALONE', 'relay commit afe32bba`s files', lambda S: alone(S, 'tier'),
     lambda S: put(S, 'commits', dict(S['commits'], tier=(['x'], S['commits']['tier'][1], True)))),
    ('G-TABLE-GATE-INSTRUMENT', 'table_gate`s self-test, push_gated.sh`s call, the test bank', lambda S: S['tg_ok'] and 'table_gate.py' in S['pg'] and 'exit 9' in S['pg']
     and '29 of 29 checks as wanted -- PASS' in S['tpg'] and 'H exit : wanted 9 ; got 9 ; PASS' in S['tpg'], lambda S: put(S, 'tpg', '')),
    ('G-TABLE-GATE-ALONE', 'relay commit 93cc2f4f`s files', lambda S: alone(S, 'table'),
     lambda S: put(S, 'commits', dict(S['commits'], table=(['x'], S['commits']['table'][1], True)))),
    ('G-STANDING-A6', 'FERRY_STANDING.md and relay commit 386a2572', lambda S: '- **A6** The terminal table is regenerated and diffed' in S['standing'] and alone(S, 'a6'),
     lambda S: put(S, 'standing', S['standing'].replace('**A6**', 'A6'))),
    ('G-BULKA-READ', 'the Bulka json', lambda S: S['bk'].get('modules') == 33 and S['bk'].get('controls') == dict(pos=True, neg=True)
     and len(S['bk'].get('per', {})) == 33, lambda S: put(S, 'bk', dict(S['bk'], modules=32))),
    ('G-H21D-SCORED', 'the scores and the desk', lambda S: scored(S, 'H21d') and S['sc']['H21d'][0] == S['bk'].get('h21d'), lambda S: put(S, 'desk', '')),
    ('G-ZEROCONFIG-PARAGRAPH', 'the Bulka bank', lambda S: 'WHETHER THE CONVERSE IS AN ARGUMENT OVER A ZeroConfig' in S['bktxt'],
     lambda S: put(S, 'bktxt', '')),
    ('G-ROUTE-READ', 'the route json', lambda S: S['rt'].get('unplaced') == [] and S['rt'].get('controls') == dict(pos=True, neg=True)
     and len(S['rt'].get('cls', {})) > 0, lambda S: put(S, 'rt', dict(S['rt'], unplaced=['x']))),
    ('G-H21A-SCORED-FIRST', 'the route bank`s time against the first Component 5 build`s start',
     lambda S: bool(S['rt'].get('written')) and S['rt']['written'] < (re.search(r'^=== START (\S+)', rd('b569_build_zetagrowth.txt'), re.M) or [None, ''])[1]
     and scored(S, 'H21a'), lambda S: put(S, 'rt', dict(S['rt'], written='9999'))),
    ('G-ANALOGUES-BANKED', 'the seven build banks', lambda S: all(S['builds'].values()) and len(S['builds']) == 7,
     lambda S: put(S, 'builds', dict(S['builds'], Landau=False))),
    ('G-HOLD-OR-LAND', 'the hold bank and the held branch', lambda S: len(re.findall(r'error:', S['hold'])) == 1 and 'rc=1' in S['hold']
     and 'linarith failed' in S['hold'] and not S['held_main'] and ('grh-weil-b569-held local %s remote %s' % (S['held_tip'], S['held_tip'])) in S['bpush'],
     lambda S: put(S, 'held_main', True)),
    ('G-H21B-SCORED', 'the scores and the desk', lambda S: scored(S, 'H21b') and 'VACUOUS' in S['sc']['H21b'][1], lambda S: put(S, 'desk', '')),
    ('G-H21C-SCORED', 'the scores and the desk', lambda S: scored(S, 'H21c'), lambda S: put(S, 'desk', '')),
    ('G-BUILD-PRINTS', 'the χ E0 json`s prints', lambda S: len(S['e0x'].get('rows', {})) == 44 and all(r['std3'] for r in S['e0x']['rows'].values())
     and all(a is not None for a in S['e0x'].get('consumed', {}).values()), lambda S: put(S, 'e0x', dict(S['e0x'], rows={}))),
    ('G-BUILD-GRADES', 'both E0 jsons: the gate, read at main', lambda S: S['e0x'].get('gate') is True and S['e0c'].get('gate') is True
     and S['e0x'].get('tip') == V011 and S['e0c'].get('tip') == V011, lambda S: put(S, 'e0x', dict(S['e0x'], tip='x'))),
    ('G-ROWGEN-DIFF', 'the rowgen json', lambda S: S['rowgen'].get('clean') is True and len(S['rowgen'].get('rows', {})) == 5,
     lambda S: put(S, 'rowgen', dict(S['rowgen'], clean=False))),
    ('G-MAIN-FF', 'the kernel`s main and its ancestry', lambda S: S['kmain'] == V011 and S['kff'], lambda S: put(S, 'kff', False)),
    ('G-TAG-BY-SCRIPT', 'the kernel push capture: main read back before the tag made, the tag peeled equal',
     lambda S: 0 <= S['kpush'].find('main read back at the remote: ' + V011) < S['kpush'].find('push_gated: tag v0.11 made at the read-back')
     and ('tag v0.11 peeled local %s remote %s' % (V011, V011)) in S['kpush'],
     lambda S: put(S, 'kpush', S['kpush'].replace('push_gated: tag v0.11 made at the read-back', 'x'))),
    ('G-HELD-BRANCH-PUSHED', 'the branch push bank', lambda S: ('grh-weil-b569 local %s remote %s' % (V011, V011)) in S['bpush']
     and ('grh-weil-b569-held local %s remote %s' % (S['held_tip'], S['held_tip'])) in S['bpush'], lambda S: put(S, 'bpush', '')),
    ('G-KERNEL-STATEMENTS-KEPT', 'the kernel, v0.10 against main: additions, README appended',
     lambda S: bool(S['kns']) and all(x.startswith('A\t') or x == 'M\tREADME.md' for x in S['kns']) and S['kre_prefix'],
     lambda S: put(S, 'kns', S['kns'] + ['M\tSIDEExplicitFormula/LiWeil.lean'])),
    ('G-KERNEL-README-SECTION', 'the kernel README at main', lambda S: S['kre_new'].count('## Appended at act b569 (ruling (R179)(2), (6))') == 1,
     lambda S: put(S, 'kre_new', '')),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith('## GRH-Weil, act four: the explicit formula for χ'),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORR-ROWS', 'CORRESPONDENCE.md rows 414-419 once each, and the writer`s final exits', lambda S: corr_rows_ok(S),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 415 | dup |')),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b569 — lane two, act nine under (R179)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORK-ORDERS-UPDATED', 'OPEN_TRAILS at the two banked lines', lambda S: oline(S, S['tj'].get('grh_line')).startswith('*Appended 2026-10-01 by b569, under the author’s ruling `(R179)`(6)')
     and oline(S, S['tj'].get('bulka_line')).startswith('*Appended 2026-10-01 by b569 to W-ORD-BULKA-GENERIC'), lambda S: put(S, 'tj', dict(S['tj'], grh_line=1))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'GRH-Weil act five at the frontier' in trail(S) and 'The author rules on the closing' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('GRH-Weil act five at the frontier', 'x'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against PLACE-papers` pre-act blob', lambda S: S['errata_pre'] is not None and S['errata_now'] == cr0(S['errata_pre']),
     lambda S: put(S, 'errata_now', S['errata_now'] + b'x')),
    ('G-OTHER-KERNELS-UNTOUCHED', 'every other kernel`s main against its pre-act head; SIDE-global-section`s diff',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] in ([], ['CORRESPONDENCE.md']),
     lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-NO-ZENODO-CALL', 'this act`s tools, for the platform`s address', lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['x'])),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tools9', S['tools9'] + [os.path.join(T, 'repair_snapshot.py')])),
    ('G-NODEPOSIT', 'the deposited outputs` status', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces_pre'] is not None and S['faces_now'] == cr0(S['faces_pre']),
     lambda S: put(S, 'faces_now', S['faces_now'] + b'x')),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at b2ed4f2e, by blob id (the regenerated table excepted by name)',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b568_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE]),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'].startswith(cr0(S['ot_pre'])),
     lambda S: put(S, 'ot_now', b'x' + S['ot_now'])),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff: no grade-or-profile cell moved that the face does not name',
     lambda S: S['table_changed'] is not None and all(TG.CELL.search(S['face']) and ('TABLE CELL: %s / %s' % tuple(k)) in S['face'] for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
    ('G-CHAIN-PAGE', 'a fresh regeneration against PLACE-papers HEAD`s committed page', lambda S: S['arm']['ok'] and S['page_committed'],
     lambda S: put(S, 'arm', dict(S['arm'], ok=False))),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 7)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the face`s (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face`s (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'],
     lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True),
     lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files: the vendored artefacts directory', lambda S: S['artefacts'] == '',
     lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b569')" in S['suite'] and "data/b569_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b569')", ''))),
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
    rec('b569 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if RERUN else regenerate()
    if RERUN:
        S['table_changed'] = []   # ### a named re-run regenerates no table; its reading is the pre-push run's, banked
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at b2ed4f2e by blob id; changed %s' % (S['prior_n'], S['prior_bad'] or 'NONE'))
    rec('  ### G-CHAIN-PAGE: committed %d bytes, regenerated %d bytes, first differing line %s' % (S['arm']['committed_bytes'],
                                                                                              S['arm']['regenerated_bytes'], S['arm']['first_diff']))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b569_checks_postpush.txt' if pushed else 'b569_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b569_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
