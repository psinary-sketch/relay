# -*- coding: utf-8 -*-
"""b573_checks.py -- THE SUITE OF b573, UNDER (R183): GRH-WEIL ACT EIGHT, THE SCHEMA; THE SUCCESSOR SENTENCE; THE χ PAGE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b573_checks.txt before the push and data/b573_checks_postpush.txt after
### it. ### The harness is b568's to b572's, carried; the arms are b573's.
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

import e0_rule as E0          # noqa: E402
import table_gate as TG       # noqa: E402
import terminal_table as TT   # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
FACE = os.path.join(D, 'b573_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
PRE = dict(relay='c74a6ee2', pp='06275eb', gs='63766ca')
V014, V015 = '4dce7b97eb29733b823919bd80b08d01c82c6d8f', '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
MODULES = ['Config', 'Converse', 'Instances']
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9'}
COMMITS = dict(pushout=('296eb292', ['data/b572_closing_push_out.txt', 'data/b572_housekeeping_push_out.txt']),
               page=('e293b1c7', ['tools/chain_page.py', 'tools/g_chain_page.py', 'tools/test_chain_page.py']))
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


def start_of(name):
    m = re.search(r'^=== START (\S+)', rd(name), re.M)
    return m.group(1) if m else ''


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b573')
            and 'data/b573_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def build_ok(m):
    b = rd('b573_build_%s.txt' % m.lower())
    return ('Built SIDEExplicitFormula.Schema.%s' % m) in b and re.search(r'^=== END \S+ rc=0$', b, re.M) is not None


def sources():
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b573_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    kre_old, kre_new = cr0(blob(KER, V014 + ':README.md')), cr0(blob(KER, 'main:README.md'))
    S = dict(
        face=face, ferry=rd('b573_ferry.txt'), scan=rd('b573_ferry_scan.txt'), cens=rd('b573_census_stepzero.txt'),
        fcens=rd('b573_faces_census_stepzero.txt'), pins=rd('b573_pins_stepzero.txt'), procs=rd('b573_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b572_closing.txt'), reads=rd('b573_reads.txt'), branches=rd('b573_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        commits={k: (files_of(v[0]), v[1], subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', v[0], 'HEAD']).returncode == 0)
                 for k, v in COMMITS.items()},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), corr=read(os.path.join(GS, 'CORRESPONDENCE.md')),
        fj=jl('b573_findings.json'), tj=jl('b573_trail.json'), wj=jl('b573_workorder.json'),
        cj=jl('b573_ceiling.json'), wt=jl('b573_weight.json'), fd=jl('b573_fields.json'), fdtxt=rd('b573_fields.txt'),
        asx=rd('b573_assertions.txt'), runs=rd('b573_page_runs.txt'), pterm=rd('b573_page_termscan.txt'),
        nodes_chi=rd('b573_nodes_chi.txt'), tcp=rd('b573_test_chain_page.txt'),
        rj=jl('b573_rows.json'), sc=jl('b573_scores.json'), desk=rd('b573_desk_notes.txt'), defects=rd('b573_defects.txt'),
        sc_start=start_of('b573_attempt_config_1.txt'), cv_start=start_of('b573_attempt_converse_1.txt'),
        c1_mtime=max(os.path.getmtime(os.path.join(D, f)) for f in ('b573_weight.json', 'b573_ceiling.json')),
        inst_src=(blob(KER, V015 + ':SIDEExplicitFormula/Schema/Instances.lean') or b'').decode('utf-8'),
        dir_head=blob(PP, 'HEAD:' + DIR_PAGE),
        readme_now=read(os.path.join(PP, 'README.md')), readme_pre=(blob(PP, PRE['pp'] + ':README.md') or b'').decode('utf-8').replace(chr(13), ''),
        reg_now=read(os.path.join(PP, 'REGISTRY.md')), reg_pre=(blob(PP, PRE['pp'] + ':REGISTRY.md') or b'').decode('utf-8').replace(chr(13), ''),
        builds={m: build_ok(m) for m in MODULES},
        e0=jl('b573_e0.json'), rowgen=jl('b573_rowgen.json'), kpush=rd('b573_kernel_push_out.txt'), bpush=rd('b573_branches_push_out.txt'),
        kmain=gs(KER, 'rev-parse', 'main'), kff=subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', V014, 'main']).returncode == 0,
        kns=[x for x in gs(KER, 'diff', '--name-status', V014, 'main').split(NL) if x.strip()],
        kre_prefix=bool(kre_old) and kre_new.startswith(kre_old), kre_new=kre_new.decode('utf-8', 'replace'),
        held_exists=bool(gs(KER, 'branch', '--list', 'grh-weil-b573-held')),
        page_head=blob(PP, 'HEAD:' + PAGE), page_b569=blob(PP, 'bd2a616:' + PAGE),
        errata_now=cr0(open(os.path.join(PP, 'ERRATA.md'), 'rb').read()), errata_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')),
        faces_now=cr0(open(os.path.join(PP, 'FACES_LEDGER.md'), 'rb').read()), faces_pre=cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md')),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read()),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b572*') for r in ('D:/relay', PP, GS, KER)},
        tools9=[os.path.join(T, f) for f in os.listdir(T) if f.startswith('b573_')],
        dep_clean=gs(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == '',
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b573_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b573_mustnotexist.txt')), table_changed=None,
    )
    import g_chain_page as GCP
    S['gcp_zeta'] = GCP.arm(os.path.join(D, 'b569_nodes.txt'), os.path.join(D, '_b573_gcp_tmp'), os.path.join(D, 'b569_probe_out.txt'))
    S['gcp_chi'] = GCP.arm(os.path.join(D, 'b573_nodes_chi.txt'), os.path.join(D, '_b573_gcp_tmp'), os.path.join(D, 'b573_chi_probe_out.txt'))
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
    i = t.find('### b573 — lane two, act thirteen under (R183)')
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item']
    pat = re.compile(r'\b(' + '|'.join(words) + r')\b')
    return not [f for f in S['tools9'] if pat.search(strip_prose(read(f)))]


def alone(S, k):
    c = S['commits'][k]
    return c[0] == sorted(c[1]) and c[2]


def corr_rows_ok(S):
    rows = [l for l in S['corr'].split(NL) if re.match(r'^\| (43[7-9]|44[01]) \|', l)]
    nums = sorted(l.split('|')[1].strip() for l in rows)
    final = {o['row']: o['exit'] for o in S['rj'].get('rows', [])}
    return nums == ['437', '438', '439', '440', '441'] and len(final) == 5 and all(v == 0 for v in final.values())


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def written_at(text):
    m = re.search(r'written at \(UTC\) (\S+)', text)
    return m.group(1) if m else '9'


def iso_epoch(s):
    import calendar
    import time
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


CEIL_HEAD = "*(Appended under the author's ruling `(R183)`(3), 2026-10-01, b573"


def ruled_sentence(S):
    f = S['ferry']
    if '"The criterion for primitive' not in f:
        return None
    a = f.index('"The criterion for primitive')
    b = f.index('neither is proved."') + len('neither is proved.')
    return ' '.join(f[a + 1:b].split())


def placed_once(pre, now, S):
    a, b = pre.split(NL), now.split(NL)
    sent = ruled_sentence(S)
    if len(b) != len(a) + 2 or not sent:
        return False
    for k in range(len(a) + 1):
        if b[:k] == a[:k] and b[k + 2:] == a[k:] and b[k] == '' and b[k + 1].startswith(CEIL_HEAD) and sent in b[k + 1]:
            return True
    return False


def placed_line(text, n):
    ls = text.split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def dir_lines(S):
    return (S['dir_head'] or b'').decode('utf-8', 'replace').split(NL)


NS = 'SIDEExplicitFormula.Schema.'
WT_HEAD = '*Appended 2026-10-01 by b573 to b572’s entry ('
WO_HEAD = '*Appended 2026-10-01 by b573, under the author’s ruling `(R183)`(6), to the W-ORD-GRH-WEIL entry'
OPEN_RULED = ('GRH_chi — open, for each primitive χ ≠ 1; by the compiled equivalence the same open statement as Weil positivity on '
              'classK for χ')
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R183) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins'],
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '  1234   5678 lean.exe        2026-09-01 00:00:00  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith('296eb292') and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith('296eb292')), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b572`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b572' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == ['296eb292'],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b573 -- x'])),
    ('G-R183-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R183) END' in S['ferry'] and S['ot'].count('**(R183) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R183) ratified', '(R183) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('Defs.lean @', 'ExplicitFormula.lean @', 'RestBound.lean @',
                                                                               'b572_gen_converse.py.txt @', 'chain_page.py @', 'README.md @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 296eb292`s files', lambda S: alone(S, 'pushout'),
     lambda S: put(S, 'commits', dict(S['commits'], pushout=(['x'], S['commits']['pushout'][1], True)))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b572') == 6, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b572'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b572': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wt'].get('lines', [0])[0]).startswith(WT_HEAD)
     and 'b572 AT ITS WEIGHT' in fline(S, S['wt'].get('lines', [0])[0]), lambda S: put(S, 'wt', dict(S['wt'], lines=[1, 2]))),
    ('G-REREAD-LINE', 'FINDINGS at the banked re-read line', lambda S: len(S['wt'].get('lines', [])) == 2
     and 'H24c RE-READ BY KIND' in fline(S, S['wt']['lines'][1]) and 'the explicit formula (2), the local count (1), the seam (4)'
     in fline(S, S['wt']['lines'][1]), lambda S: put(S, 'wt', dict(S['wt'], lines=[1, 2]))),
    ('G-CEILING-README', 'README at the placed line', lambda S: placed_line(S['readme_now'], S['cj'].get('readme')).startswith(CEIL_HEAD)
     and bool(ruled_sentence(S)) and ruled_sentence(S) in placed_line(S['readme_now'], S['cj'].get('readme')),
     lambda S: put(S, 'cj', dict(S['cj'], readme=1))),
    ('G-CEILING-REGISTRY', 'REGISTRY at the placed line', lambda S: placed_line(S['reg_now'], S['cj'].get('registry')).startswith(CEIL_HEAD)
     and bool(ruled_sentence(S)) and ruled_sentence(S) in placed_line(S['reg_now'], S['cj'].get('registry')),
     lambda S: put(S, 'cj', dict(S['cj'], registry=1))),
    ('G-CEILING-FINDINGS', 'FINDINGS at the successor record line', lambda S: 'THE CEILING’S SUCCESSOR' in fline(S, S['cj'].get('findings'))
     and '(:6328)' in fline(S, S['cj'].get('findings')) and bool(ruled_sentence(S)) and ruled_sentence(S) in fline(S, S['cj'].get('findings')),
     lambda S: put(S, 'cj', dict(S['cj'], findings=1))),
    ('G-COMPONENT1-FIRST', 'the Component 1 banks` times against the first kernel elaboration', lambda S: bool(S['sc_start'])
     and iso_epoch(S['sc_start']) is not None and S['c1_mtime'] < iso_epoch(S['sc_start']), lambda S: put(S, 'c1_mtime', 4102444800)),
    ('G-FIELDS-BANKED', 'the fields json and bank', lambda S: S['fd'].get('fields') == ['EF', 'COUNT', 'TARGET']
     and 'structure WeilConfig extends Zeta23.ZeroConfig where' in S['fdtxt'] and 'H25a, PROVISIONAL' in S['fdtxt'],
     lambda S: put(S, 'fd', dict(S['fd'], fields=['EF', 'COUNT']))),
    ('G-FIELDS-FIRST', 'the fields bank`s time against the first kernel elaboration', lambda S: bool(S['sc_start'])
     and written_at(S['fdtxt']) < S['sc_start'], lambda S: put(S, 'sc_start', '0')),
    ('G-H25A-SCORED', 'the scores and the desk', lambda S: scored(S, 'H25a'), lambda S: put(S, 'desk', '')),
    ('G-ASSERTIONS-FIRST', 'the assertion list`s time against the first Converse elaboration', lambda S: bool(S['cv_start'])
     and written_at(S['asx']) < S['cv_start'] and '56 x' in S['asx'], lambda S: put(S, 'cv_start', '0')),
    ('G-PIECES-BANKED', 'the three build banks', lambda S: all(S['builds'].values()) and len(S['builds']) == 3,
     lambda S: put(S, 'builds', dict(S['builds'], Instances=False))),
    ('G-H25B-SCORED', 'the scores and the desk', lambda S: scored(S, 'H25b'), lambda S: put(S, 'desk', '')),
    ('G-SCHEMA-IFF', 'the E0 json', lambda S: S['e0'].get('rows', {}).get(NS + 'h2_sign_cfg_iff_target', {}).get('grade') == 'DERIVES'
     and S['e0']['rows'][NS + 'h2_sign_cfg_iff_target'].get('std3') is True, lambda S: put(S, 'e0', dict(S['e0'], rows={}))),
    ('G-HOLD-OR-LAND', 'the E0 json, the scores, the branch list', lambda S: S['e0'].get('rows', {}).get(NS + 'h2_sign_cfg_iff_target', {}).get('std3') is True
     and S['sc'].get('H25c', [''])[0] == 'HELD' and not S['held_exists'], lambda S: put(S, 'held_exists', True)),
    ('G-INSTANCE-CHECKS', 'Instances.lean at v0.15 and the E0 json', lambda S: '= (h2_sign ↔ RiemannHypothesis) :=\n  rfl' in S['inst_src']
     and '= (h2_sign_chi χ ↔ GRH_chi χ) :=\n  rfl' in S['inst_src']
     and all(S['e0'].get('rows', {}).get(NS + n, {}).get('std3') for n in ('h2_sign_cfg_zeta_statement', 'h2_sign_cfg_chi_statement')),
     lambda S: put(S, 'inst_src', S['inst_src'].replace('rfl', 'sorry'))),
    ('G-H25C-SCORED', 'the scores and the desk', lambda S: scored(S, 'H25c'), lambda S: put(S, 'desk', '')),
    ('G-BUILD-PRINTS', 'the E0 json`s prints', lambda S: len(S['e0'].get('rows', {})) == 22 and all(r['std3'] for r in S['e0']['rows'].values())
     and all(a is not None for a in S['e0'].get('consumed', {}).values()), lambda S: put(S, 'e0', dict(S['e0'], rows={}))),
    ('G-BUILD-GRADES', 'the E0 gate, read at the branch tip', lambda S: S['e0'].get('gate') is True and S['e0'].get('tip') == V015
     and S['e0'].get('rev') == 'grh-weil-b573', lambda S: put(S, 'e0', dict(S['e0'], rev='main'))),
    ('G-ROWGEN-DIFF', 'the rowgen json', lambda S: S['rowgen'].get('clean') is True and len(S['rowgen'].get('rows', {})) == 4,
     lambda S: put(S, 'rowgen', dict(S['rowgen'], clean=False))),
    ('G-MAIN-FF', 'the kernel`s main and its ancestry', lambda S: S['kmain'] == V015 and S['kff'], lambda S: put(S, 'kff', False)),
    ('G-TAG-BY-SCRIPT', 'the kernel push capture', lambda S: 0 <= S['kpush'].find('main read back at the remote: ' + V015) < S['kpush'].find('push_gated: tag v0.15 made at the read-back')
     and ('tag v0.15 peeled local %s remote %s' % (V015, V015)) in S['kpush'], lambda S: put(S, 'kpush', S['kpush'].replace('tag v0.15 made', 'x'))),
    ('G-HELD-BRANCH-PUSHED', 'the branch push bank', lambda S: ('grh-weil-b573 local %s remote %s' % (V015, V015)) in S['bpush']
     and 'grh-weil-b573-held is not made' in S['bpush'], lambda S: put(S, 'bpush', '')),
    ('G-KERNEL-STATEMENTS-KEPT', 'the kernel, v0.14 against main', lambda S: bool(S['kns']) and all(x.startswith('A\t') or x == 'M\tREADME.md' for x in S['kns'])
     and S['kre_prefix'], lambda S: put(S, 'kns', S['kns'] + ['M\tSIDEExplicitFormula/PowerLimit.lean'])),
    ('G-KERNEL-README-SECTION', 'the kernel README at main', lambda S: S['kre_new'].count('## Appended at act b573 (ruling (R183)(4))') == 1,
     lambda S: put(S, 'kre_new', '')),
    ('G-NODES-CHI', 'the χ node list', lambda S: '# page: dirichlet' in S['nodes_chi'] and '# pin: v0.15' in S['nodes_chi']
     and len([l for l in S['nodes_chi'].split(NL) if l.strip() and not l.startswith('#')]) == 18,
     lambda S: put(S, 'nodes_chi', S['nodes_chi'].replace('# page: dirichlet', ''))),
    ('G-CHAIN-PAGE-ALONE', 'relay e293b1c7`s files and the test bank', lambda S: alone(S, 'page') and '26 of 26 cases as wanted -- PASS' in S['tcp'],
     lambda S: put(S, 'commits', dict(S['commits'], page=(['x'], S['commits']['page'][1], True)))),
    ('G-CHAIN-PAGE', 'the ζ page regenerated from b569`s list against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page regenerated from its list against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-TWICE', 'the runs bank against the committed page', lambda S: 'the two outputs: BYTE-IDENTICAL' in S['runs']
     and S['dir_head'] is not None and hashlib.sha256(S['dir_head']).hexdigest() in S['runs'], lambda S: put(S, 'runs', S['runs'].replace('BYTE-IDENTICAL', 'DIFFER'))),
    ('G-PAGE-LAST-LINE', 'the committed page`s line after the open line, against the ferry`s words', lambda S: OPEN_RULED in dir_lines(S)
     and bool(ruled_sentence(S)) and dir_lines(S)[dir_lines(S).index(OPEN_RULED) + 2] == ruled_sentence(S),
     lambda S: put(S, 'dir_head', (S['dir_head'] or b'').replace('neither is proved.'.encode('utf-8'), b'neither.'))),
    ('G-PAGE-OPEN-LINE', 'the committed page', lambda S: OPEN_RULED in dir_lines(S) and dir_lines(S)[0] == '# THE CLAUSE AT THE DIRICHLET INSTANCE',
     lambda S: put(S, 'dir_head', (S['dir_head'] or b'').replace('GRH_chi — open'.encode('utf-8'), b'GRH_chi -- open'))),
    ('G-PAGE-BANNED', 'the page`s banned-stem scan', lambda S: re.search(r'^\s*VERDICT\s*: CLEAN', S['pterm'], re.M) is not None,
     lambda S: put(S, 'pterm', S['pterm'].replace('CLEAN', 'HITS'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(
        '## GRH-Weil, act eight: the criterion over a configuration with an explicit formula and a local count'),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORR-ROWS', 'CORRESPONDENCE rows 437-441', lambda S: corr_rows_ok(S), lambda S: put(S, 'corr', S['corr'] + NL + '| 438 | dup |')),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b573 — lane two, act thirteen under (R183)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORK-ORDERS-UPDATED', 'OPEN_TRAILS at the work-order line, and this act`s trail record', lambda S: oline(S, S['wj'].get('line')).startswith(WO_HEAD)
     and 'THE SCHEMA LANDED' in oline(S, S['wj'].get('line')) and 'the work-order line' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('THE SCHEMA LANDED', 'x').replace('the work-order line', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'CP-5, the deposit reconciliation' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('CP-5, the deposit reconciliation', 'x'))),
    ('G-PAGE-UNCHANGED', 'the ζ page at PLACE-papers HEAD against b569`s', lambda S: S['page_head'] is not None and S['page_head'] == S['page_b569'],
     lambda S: put(S, 'page_head', (S['page_head'] or b'') + b'x')),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against the pre-act blob', lambda S: S['errata_pre'] is not None and S['errata_now'] == cr0(S['errata_pre']),
     lambda S: put(S, 'errata_now', S['errata_now'] + b'x')),
    ('G-OTHER-KERNELS-UNTOUCHED', 'every other kernel`s main; SIDE-global-section`s diff', lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items())
     and S['gs_diff'] in ([], ['CORRESPONDENCE.md']), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-NO-ZENODO-CALL', 'this act`s tools', lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['x'])),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S), lambda S: put(S, 'tools9', S['tools9'] + [os.path.join(T, 'repair_snapshot.py')])),
    ('G-NODEPOSIT', 'the deposited outputs` status', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces_pre'] is not None and S['faces_now'] == cr0(S['faces_pre']),
     lambda S: put(S, 'faces_now', S['faces_now'] + b'x')),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at c74a6ee2, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b572_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md', DIR_PAGE]),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'].startswith(cr0(S['ot_pre'])),
     lambda S: put(S, 'ot_now', b'x' + S['ot_now'])),
    ('G-PREFIX-KEPT', 'README and REGISTRY against their pre-act blobs', lambda S: placed_once(S['readme_pre'], S['readme_now'], S)
     and placed_once(S['reg_pre'], S['reg_now'], S), lambda S: put(S, 'reg_now', S['reg_now'].replace('## ', '##  ', 1))),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b573')" in S['suite'] and "data/b573_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b573')", ''))),
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
    rec('b573 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at c74a6ee2 by blob id; changed %s' % (S['prior_n'], S['prior_bad'] or 'NONE'))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b573_checks_postpush.txt' if pushed else 'b573_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b573_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
