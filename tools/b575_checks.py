# -*- coding: utf-8 -*-
"""b575_checks.py -- THE SUITE OF b575, UNDER (R185): CP-5, THE RECONCILING EDITS AS RULED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b575_checks.txt before the push and data/b575_checks_postpush.txt after
### it. ### The harness is b568's to b574's, carried; the arms are b575's. ### G-TOKEN-UNBANKED reads the token from the
### environment and never prints it.
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
FACE = os.path.join(D, 'b575_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
MIRROR = 'outputs/DEPOSITED-v1.1.2/'
PRE = dict(relay='66246291', pp='0018869', gs='8c392fe')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
ATTR, MIRC = '383ac23', '8065f97'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}
STEPZERO = 'c8052113'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RIDS = ('21520474', '21539167')
PP_SCOPE = sorted(['.gitattributes', MIRROR + 'A_Place_to_Stand.md', MIRROR + 'ERRATA.md', 'ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md',
                   'REGISTRY.md', 'SPIRAL_MAP.md'])
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


def md5(b):
    return 'md5:' + hashlib.md5(b).hexdigest() if b is not None else None


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b575')
            and 'data/b575_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def lines_of(b):
    return cr0(b).decode('utf-8', 'replace').split(NL)


def sources():
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b575_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b575_') and f.endswith('.py'))
    rec_md5 = jl('b574_zenodo_fetch.json').get('21539167', {}).get('files', {})
    mfiles = sorted(x for x in gs(PP, 'ls-tree', '--name-only', MIRC, MIRROR).split(NL) if x.strip())
    S = dict(
        face=face, ferry=rd('b575_ferry.txt'), scan=rd('b575_ferry_scan.txt'), cens=rd('b575_census_stepzero.txt'),
        fcens=rd('b575_faces_census_stepzero.txt'), pins0=rd('b575_pins_stepzero.txt'), procs=rd('b575_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b574_closing.txt'), reads=rd('b575_reads.txt'), branches=rd('b575_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        attr=(files_of(PP, ATTR), gs(PP, 'show', '--pretty=format:', ATTR, '--', '.gitattributes'),
              subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', ATTR, 'HEAD']).returncode == 0),
        mirc=(files_of(PP, MIRC), subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', MIRC, 'HEAD']).returncode == 0,
              gs(PP, 'rev-parse', MIRC + '^') == gs(PP, 'rev-parse', ATTR)),
        rec_md5=rec_md5,
        mblobs={os.path.basename(p): (md5(blob(PP, '%s:%s' % (MIRC, p))), md5(blob(PP, 'HEAD:' + p))) for p in mfiles},
        mcontent={os.path.basename(p): cr0(blob(PP, '%s:%s' % (MIRC, p))) == cr0(blob(PP, '%s:%s' % (PRE['pp'], p))) for p in mfiles},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        reg_now=read(os.path.join(PP, 'REGISTRY.md')), reg_pre=cr0(blob(PP, PRE['pp'] + ':REGISTRY.md')),
        reg_raw=cr0(raw(os.path.join(PP, 'REGISTRY.md'))),
        spm_now=lines_of(raw(os.path.join(PP, 'SPIRAL_MAP.md'))), spm_pre=lines_of(blob(PP, PRE['pp'] + ':SPIRAL_MAP.md')),
        err_now=lines_of(raw(os.path.join(PP, 'ERRATA.md'))), err_pre=lines_of(blob(PP, PRE['pp'] + ':ERRATA.md')),
        fj=jl('b575_findings.json'), tj=jl('b575_trail.json'), wt=jl('b575_weight.json'),
        facts=jl('b575_facts.json'), ftxt=rd('b575_facts.txt'), rl=jl('b575_registry_lines.json'),
        kl=jl('b575_kernel_lines.json'), kltxt=rd('b575_kernel_lines.txt'),
        draft=rd('b575_zenodo_draft.txt'), c1=rd('b575_zenodo_c1.txt'), c2=rd('b575_zenodo_c2.txt'), zr=jl('b575_zenodo_results.json'),
        intended=jl('b575_intended.json'), fb={r: jl('b575_fetchback_%s.json' % r) for r in RIDS},
        old={r: jl('b574_fetch_%s.json' % r) for r in RIDS}, fsame=jl('b575_files_same.json'),
        ej=jl('b575_erratum.json'), lvtxt=rd('b575_zenodo_lv.txt'), lvj=jl('b575_lv.json'), lvresp=jl('b575_fetch_21539068.json'),
        sc=jl('b575_scores.json'), desk=rd('b575_desk_notes.txt'),
        tok=os.environ.get('ZENODO' + '_' + 'TOKEN') or '',
        banks={f: raw(f) for f in glob.glob(os.path.join(D, 'b575_*')) + glob.glob(os.path.join(D, 'audit_b575_*'))},
        pages={p: (blob(PP, 'HEAD:' + p), blob(PP, PRE['pp'] + ':' + p)) for p in (PAGE, DIR_PAGE)},
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kmain=gs(KER, 'rev-parse', 'main'), kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b574*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b575_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b575_mustnotexist.txt')), table_changed=None,
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
    pp_changed = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    pp_changed |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    S['pp_changed'] = sorted(pp_changed)
    S['faces_edited'] = [x for x in gs(ROOT, 'diff', '--name-only', PRE['relay'], '--', 'data/b56*_registration_*.txt',
                                       'data/b57[0-4]_registration_*.txt').split(NL) if x.strip()]
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


def rline(S, n):
    ls = S['reg_now'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def trail(S):
    t = S['ot']
    i = t.find('### b575 — lane three, act three under (R185)')
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


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def spiral_ok(S):
    a, b = S['spm_pre'], S['spm_now']
    rl = S['rl'].get('lines') or [0, 0, 0, 0]
    want = {41: rl[1], 140: rl[2], 533: rl[3]}
    if len(a) != len(b):
        return False
    diff = [i + 1 for i in range(len(a)) if a[i] != b[i]]
    if diff != [41, 140, 533]:
        return False
    return all(b[n - 1].replace(' (REGISTRY :%d)' % want[n], '', 1) == a[n - 1] and (' (REGISTRY :%d)' % want[n]) in b[n - 1] for n in want)


def errata_ok(S):
    a, b = S['err_pre'], S['err_now']
    idx = [i for i, l in enumerate(b) if l.startswith('- `E-2026-10-01-1` — ')]
    if len(idx) != 1:
        return False
    b2 = b[:idx[0]] + b[idx[0] + 1:]
    k = [i for i, l in enumerate(a) if l.startswith('- `E-2026-09-25-6` — ')]
    return bool(k) and idx[0] == k[0] + 1 and b2[:len(a) - 1] == a[:-1] and (a[-1] == '' or b2[len(a) - 1].startswith(a[-1]))


def fb_match(S):
    return all(S['fb'][r].get('metadata', {}).get('description') == S['intended'].get(r) and S['intended'].get(r) for r in RIDS) \
        and S['c2'].count('-C] ### **MATCH**') == 2


def keys_carried(S):
    c2 = (S['zr'].get('c2') or {}).get('records') or {}
    ks = ('title', 'version', 'publication_date', 'creators', 'license', 'resource_type')
    return all(c2.get(r, {}).get('other_keys_carried') and c2.get(r, {}).get('keys_same') for r in RIDS) and all(
        S['fb'][r].get('metadata', {}).get(k) == S['old'][r].get('metadata', {}).get(k) for r in RIDS for k in ks)


WT_HEAD = '*Appended 2026-10-01 by b575 to b574’s entry ('
TITLE = '## CP-5, act two: the deposit mirror at the deposited bytes'
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R185) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b574`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b574' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b575 -- x'])),
    ('G-R185-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R185) END' in S['ferry'] and S['ot'].count('**(R185) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R185) ratified', '(R185) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('b574_zenodo_fetch.txt @', 'b574_pins.txt @', 'b574_ledgers.txt @',
                                                                               'b574_description_draft.txt @', 'REGISTRY.md @', 'SPIRAL_MAP.md @',
                                                                               'README.md @', 'ERRATA.md @', 'b535_zenodo.py @', 'b540_ferry.txt @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay c8052113`s files', lambda S: S['pushout'][0] == ['data/b574_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b574') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b574'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wt'].get('lines', [0])[0]).startswith(WT_HEAD)
     and 'b574 AT ITS WEIGHT' in fline(S, S['wt'].get('lines', [0])[0]), lambda S: put(S, 'wt', dict(S['wt'], lines=[1, 2]))),
    ('G-NAVIGATOR-LINE', 'FINDINGS at the banked navigator`s line', lambda S: len(S['wt'].get('lines', [])) == 2
     and fline(S, S['wt']['lines'][1]).startswith(WT_HEAD) and 'THE H26a LETTER, THE NAVIGATOR’S' in fline(S, S['wt']['lines'][1]),
     lambda S: put(S, 'wt', dict(S['wt'], lines=[S['wt'].get('lines', [0])[0], 2]))),
    ('G-ATTR-ALONE', 'PLACE-papers 383ac23`s files and diff', lambda S: S['attr'][0] == ['.gitattributes'] and S['attr'][2]
     and '+outputs/DEPOSITED-v1.1.2/** -text' in S['attr'][1], lambda S: put(S, 'attr', (['.gitattributes', 'README.md'], S['attr'][1], True))),
    ('G-MIRROR-RECOMMIT', 'PLACE-papers 8065f97`s files, parent and ancestry', lambda S: S['mirc'][0] == sorted([MIRROR + 'A_Place_to_Stand.md', MIRROR + 'ERRATA.md'])
     and S['mirc'][1] and S['mirc'][2], lambda S: put(S, 'mirc', (S['mirc'][0], S['mirc'][1], False))),
    ('G-MIRROR-MD5', 'every mirror blob at 8065f97 and at HEAD against record 21539167`s md5s', lambda S: len(S['mblobs']) == 11 and all(
        S['rec_md5'].get(k) and a == b == S['rec_md5'].get(k) for k, (a, b) in S['mblobs'].items()),
     lambda S: put(S, 'mblobs', dict(S['mblobs'], **{'ERRATA.md': ('md5:b4159e7a1f9900b4c205238a70bc9e11',) * 2}))),
    ('G-MIRROR-CONTENT', 'every mirror blob at 8065f97 against its pre-act blob, line endings folded', lambda S: len(S['mcontent']) == 11 and all(S['mcontent'].values()),
     lambda S: put(S, 'mcontent', dict(S['mcontent'], **{'A_Place_to_Stand.md': False}))),
    ('G-PAIR-LINE', 'REGISTRY at the banked pair line', lambda S: rline(S, (S['rl'].get('lines') or [0])[0]).startswith("*(Appended under the author's ruling `(R185)`(2)(ii)")
     and ('**v1.7** = `%s`' % S['facts'].get('peeled', {}).get('SIDE-kernel v1.7', {}).get('remote', 'x')) in rline(S, S['rl']['lines'][0])
     and 'The citation rule:' in rline(S, S['rl']['lines'][0]) and '**v1.5** = `0e5233f`' in rline(S, S['rl']['lines'][0]),
     lambda S: put(S, 'rl', dict(S['rl'], lines=[1] + (S['rl'].get('lines') or [0])[1:]))),
    ('G-PAIR-PEELED', 'the facts bank`s v1.7 read at the remote', lambda S: S['facts'].get('peeled', {}).get('SIDE-kernel v1.7', {}).get('agree') is True
     and re.search(r'SIDE-kernel\s+v1\.7\s+remote peeled 2957e7d\w+ ; tag object \w+ ; local 2957e7d\w+ ; AGREE', S['ftxt']) is not None,
     lambda S: put(S, 'ftxt', S['ftxt'].replace('2957e7d', '0000000'))),
    ('G-CITATION-CHECKED', 'the kernel-lines bank and json', lambda S: len(S['kl'].get('v2', [])) == 19 and all(
        o.get('hand') for o in S['kl'].get('v2', []) if o.get('differs')) and 'hand-read: every differing line' in S['kltxt']
     and '### NOT HAND-READ' not in S['kltxt'], lambda S: put(S, 'kltxt', S['kltxt'] + '### NOT HAND-READ')),
    ('G-COUNT-AT-PIN', 'the facts json and REGISTRY`s count line', lambda S: S['facts'].get('count', {}).get('kernel_bridge') == 83
     and (S['facts'].get('pin') or '').startswith('e0a8ba0') and all(x in rline(S, (S['rl'].get('lines') or [0, 0])[1]) for x in ('(70)', '(13)', '`e0a8ba0`', '"83 files"')),
     lambda S: put(S, 'facts', dict(S['facts'], count=dict(S['facts'].get('count', {}), kernel_bridge=84)))),
    ('G-TAGS-PEELED', 'the facts json', lambda S: bool(S['facts'].get('spiral_agree')) and all(S['facts']['spiral_agree'].values())
     and all(v.get('agree') for v in S['facts'].get('peeled', {}).values()) and len(S['facts'].get('peeled', {})) == 5,
     lambda S: put(S, 'facts', dict(S['facts'], spiral_agree={'x': False}))),
    ('G-FACT-LINES', 'REGISTRY at the three banked fact lines', lambda S: len(S['rl'].get('lines') or []) == 4 and all(
        rline(S, n).startswith("*(Appended under the author's ruling `(R185)`(2)(iii)") and rline(S, n).endswith('(SPIRAL_MAP :%d)' % m)
        for n, m in zip(S['rl']['lines'][1:], (41, 140, 533))), lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [0])[:1] + [1, 2, 3]))),
    ('G-SPIRAL-POINTERS', 'SPIRAL_MAP at :41, :140, :533', lambda S: len(S['rl'].get('lines') or []) == 4 and all(
        (' (REGISTRY :%d)' % m) in S['spm_now'][n - 1] for n, m in zip((41, 140, 533), S['rl']['lines'][1:])),
     lambda S: put(S, 'spm_now', [l.replace(' (REGISTRY :', ' (REG :') for l in S['spm_now']])),
    ('G-SPIRAL-SCOPE', 'SPIRAL_MAP against its pre-act blob', lambda S: spiral_ok(S),
     lambda S: put(S, 'spm_now', S['spm_now'][:10] + ['x'] + S['spm_now'][11:])),
    ('G-DRAFT-DIFFED', 'the draft bank', lambda S: S['draft'].count('byte-exact True') == 2 and '**THE TWO SENTENCES EQUAL REGISTRY`S: True.**' in S['draft'],
     lambda S: put(S, 'draft', S['draft'].replace('byte-exact True', 'byte-exact False', 1))),
    ('G-CALL-REDACTED', 'the c1 bank', lambda S: S['c1'].count('Bearer [TOKEN REDACTED]') == 6 and len(re.findall(r'Bearer (?!\[TOKEN REDACTED\])', S['c1'])) == 0,
     lambda S: put(S, 'c1', S['c1'].replace('Bearer [TOKEN REDACTED]', 'Bearer abc', 1))),
    ('G-WRITES-BANKED', 'the c2 bank and the results json', lambda S: S['c2'].count('POST actions/edit    : ### **201**') == 2
     and S['c2'].count('PUT metadata         : ### **200**') == 2 and S['c2'].count('POST actions/publish : ### **202**') == 2
     and 'discard' not in S['c2'] and set(((S['zr'].get('c2') or {}).get('records') or {})) == set(RIDS),
     lambda S: put(S, 'c2', S['c2'].replace('### **202**', '### **400**', 1))),
    ('G-FETCHBACK-MATCH', 'each banked fetch-back`s description against the banked intended, and the c2 bank', lambda S: fb_match(S),
     lambda S: put(S, 'intended', dict(S['intended'], **{'21539167': (S['intended'].get('21539167') or '') + ' '}))),
    ('G-KEYS-CARRIED', 'the results json and each fetch-back`s metadata against b574`s fetch', lambda S: keys_carried(S),
     lambda S: put(S, 'old', dict(S['old'], **{'21520474': {'metadata': {}}}))),
    ('G-RECORD-FILES-SAME', 'the files-same json', lambda S: len(S['fsame']) == 2 and all(v.get('same') for v in S['fsame'].values()),
     lambda S: put(S, 'fsame', dict(S['fsame'], **{'21539167': {'same': False}}))),
    ('G-ERRATUM-WRITTEN', 'ERRATA at the banked index and heading lines', lambda S: S['ej'].get('index_line') and S['err_now'][S['ej']['index_line'] - 1].startswith('- `E-2026-10-01-1` — *DEPOSIT-FACING')
     and S['err_now'][S['ej']['heading_line'] - 1].startswith('## E-2026-10-01-1 — ') and all(
        S['ej'].get('stamps', {}).get(r) and S['ej']['stamps'][r] in NL.join(S['err_now']) for r in RIDS),
     lambda S: put(S, 'ej', dict(S['ej'], heading_line=1))),
    ('G-ERRATA-SCOPE', 'ERRATA against its pre-act blob', lambda S: errata_ok(S), lambda S: put(S, 'err_now', ['x'] + S['err_now'])),
    ('G-TOKEN-UNBANKED', 'every b575 bank, read for the token from the environment', lambda S: len(S['tok']) > 20 and len(S['banks']) > 30
     and all(b is not None and S['tok'].encode('utf-8') not in b for b in S['banks'].values()),
     lambda S: put(S, 'banks', dict(S['banks'], x=b'x' + S['tok'].encode('utf-8')))),
    ('G-LV-FETCHED', 'the lv response banked whole and its bank', lambda S: str(S['lvresp'].get('id')) == '21539068'
     and 'banked whole as data/b575_fetch_21539068.json' in S['lvtxt'], lambda S: put(S, 'lvresp', {})),
    ('G-LV-GET-ONLY', 'the lv bank`s request line', lambda S: len([l for l in S['lvtxt'].split(NL) if l.startswith('### REQUEST : ')]) == 1
     and '### REQUEST : GET https://zenodo.org/api/records/21539068 ; Authorization header sent : False' in S['lvtxt'] and S['lvj'].get('auth') is False,
     lambda S: put(S, 'lvtxt', S['lvtxt'].replace('### REQUEST : GET', '### REQUEST : PUT'))),
    ('G-LV-ERRATUM-LOCATED', 'the lv response`s description and the lv bank', lambda S: 'E-2026-09-25-3' not in S['lvresp'].get('metadata', {}).get('description', 'E-2026-09-25-3')
     and 'Rather than leaving that clause as prose' in S['lvresp'].get('metadata', {}).get('description', '')
     and S['lvj'].get('present') is False and '(R150)(1)' in S['lvtxt'] and 'RECORDED, NOT APPENDED' in S['lvtxt'],
     lambda S: put(S, 'lvj', dict(S['lvj'], present=True))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(TITLE),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b575 — lane three, act three under (R185)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'CP-7 act one' in trail(S) and '`(R157)`(6)' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('CP-7 act one', 'x'))),
    ('G-CP5-STATE', 'the scores and this act`s trail record', lambda S: S['sc'].get('cp5') == 'CLOSED' and '**CP-5 CLOSED**' in trail(S),
     lambda S: put(S, 'sc', dict(S['sc'], cp5='OPEN'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{PAGE: ((S['pages'][PAGE][0] or b'') + b'x', S['pages'][PAGE][1])}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff', lambda S: S['kmain'] == V015
     and S['kcur'] == 'main' and S['kdirty'] == '' and all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] == [],
     lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b575_record.py'): S['tooltext'].get(os.path.join(T, 'b575_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'the files-same json, each fetch-back`s id and version, this act`s tools', lambda S: all(v.get('same') for v in S['fsame'].values())
     and [S['fb'][r].get('metadata', {}).get('version') for r in RIDS] == ['v1.5', 'v1.1.2'] and [str(S['fb'][r].get('id')) for r in RIDS] == list(RIDS)
     and not [f for f, t in S['tooltext'].items() if ('new' + 'version') in t or ('/fil' + 'es' + "'") in t],
     lambda S: put(S, 'fb', dict(S['fb'], **{'21520474': dict(S['fb']['21520474'], id=99)}))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 66246291, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b574_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == PP_SCOPE,
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-REGISTRY-APPEND-ONLY', 'REGISTRY -- its pre-act blob a true prefix', lambda S: S['reg_pre'] and S['reg_raw'] is not None
     and S['reg_raw'].startswith(S['reg_pre']) and len(S['reg_raw']) > len(S['reg_pre']), lambda S: put(S, 'reg_raw', b'x' + (S['reg_raw'] or b''))),
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
                                                                          and "startswith('b575')" in S['suite'] and "data/b575_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b575')", ''))),
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
    rec('b575 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    rec('  ### G-TOKEN-UNBANKED read %d banks (the token itself is not printed)' % len(S['banks']))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b575_checks_postpush.txt' if pushed else 'b575_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b575_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
