# -*- coding: utf-8 -*-
"""b576_checks.py -- THE SUITE OF b576, UNDER (R186): CP-7 ACT ONE, THE TWO ITEMS, THE REFRESH.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b576_checks.txt before the push and data/b576_checks_postpush.txt after
### it. ### The harness is b568's to b575's, carried; the arms are b576's. ### G-TOKEN-UNBANKED reads the token from the
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
FACE = os.path.join(D, 'b576_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='04b98516', pp='b95e5c0', gs='8c392fe')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}
STEPZERO, ROSTERC = '3aff82e8', '0ff04077'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
PAGES = (PAGE, DIR_PAGE)
ZIP = r'D:\MY-DOwnloads\mirror-refresh-2026-10-01.zip'
MEMDIR = r'C:\Users\echo chamber\.claude\projects\D--\memory'
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b576')
            and 'data/b576_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    lockn = sorted(glob.glob(os.path.join(D, 'b576_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b576_') and f.endswith('.py'))
    import b576_record as REC
    er_pre = lines_of(blob(PP, PRE['pp'] + ':ERRATA.md'))
    import zipfile
    zipok = os.path.exists(ZIP)
    S = dict(
        face=face, ferry=rd('b576_ferry.txt'), scan=rd('b576_ferry_scan.txt'), cens=rd('b576_census_stepzero.txt'),
        fcens=rd('b576_faces_census_stepzero.txt'), pins0=rd('b576_pins_stepzero.txt'), procs=rd('b576_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b575_closing.txt'), reads=rd('b576_reads.txt'), branches=rd('b576_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        roster_c=(files_of(ROOT, ROSTERC), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', ROSTERC, 'HEAD']).returncode == 0),
        roster_now=json.loads(read(os.path.join(T, 'mirror_roster.json')) or '{}'),
        roster_pre=json.loads((blob(ROOT, PRE['relay'] + ':tools/mirror_roster.json') or b'{}').decode('utf-8')),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        spm_now=lines_of(raw(os.path.join(PP, 'SPIRAL_MAP.md'))), spm_pre=lines_of(blob(PP, PRE['pp'] + ':SPIRAL_MAP.md')),
        err_now=lines_of(raw(os.path.join(PP, 'ERRATA.md'))), err_pre=er_pre,
        err_sent=[(re.search(r'replacement: \*"(.*)"\*\s*$', er_pre[n - 1]) or re.search('x^', '')) for n in (564, 567)],
        wt=jl('b576_weight.json'), fj=jl('b576_findings.json'), tj=jl('b576_trail.json'),
        zdraft=rd('b576_zenodo_draft.txt'), imeta=jl('b576_intended_meta.json'), c1=rd('b576_zenodo_c1.txt'), c2=rd('b576_zenodo_c2.txt'),
        zr=jl('b576_zenodo_results.json'), intended=jl('b576_intended.json'), fb=jl('b576_fetchback_21539068.json'),
        old=jl('b575_fetch_21539068.json'), fsame=jl('b576_files_same.json'), e2=jl('b576_lv_erratum.json'), e3=jl('b576_corpus_erratum.json'),
        pdt=rd('b576_purpose_drafts.txt'), pdj=jl('b576_purpose_drafts.json'),
        located=[(k, t, REC._locate(k, t)) for d in (REC.DRAFT_A, REC.DRAFT_B) for kk, t, k in d if kk == 'S'],
        editions=sorted(f[:-4] for f in os.listdir(os.path.join(D, 'b558_editions'))),
        observ=[f for f in gs(PP, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL) if 'observ' in f.lower()],
        pp_added=[l for l in gs(PP, 'diff', '--name-status', PRE['pp'], 'HEAD').split(NL) if l.startswith('A')],
        mj=jl('b576_mirror.json'), mtxt=rd('b576_mirror.txt'), mbuild=rd('b576_mirror_build.txt'), mver=rd('b576_mirror_verify.txt'),
        zip_names=zipfile.ZipFile(ZIP).namelist() if zipok else [], zip_mtime=os.path.getmtime(ZIP) if zipok else 0,
        pp_push_at=iso_epoch((re.search(r'capture on -> \S+ \((\S+)\)', rd('b576_push_out.txt')) or re.search('(x)', 'x')).group(1)),
        pp_head=gs(PP, 'rev-parse', '--short=7', 'HEAD'), pp_remote=gs(PP, 'ls-remote', 'origin', 'refs/heads/main')[:7],
        mem=read(os.path.join(MEMDIR, 'MEMORY.md')), memfiles=set(os.listdir(MEMDIR)), refresh=jl('b576_refresh.json'),
        sc=jl('b576_scores.json'), desk=rd('b576_desk_notes.txt'),
        tok=os.environ.get('ZENODO' + '_' + 'TOKEN') or '',
        banks={f: raw(f) for f in glob.glob(os.path.join(D, 'b576_*')) + glob.glob(os.path.join(D, 'audit_b576_*'))},
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
        push_lists={r: gs(r, 'branch', '--list', 'push-b575*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b576_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b576_mustnotexist.txt')), table_changed=None,
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
    S['pp_texts'] = {f: read(os.path.join(PP, f)) for f in S['pp_changed']}
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


def eline(S, n):
    ls = S['err_now']
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def trail(S):
    t = S['ot']
    i = t.find('### b576 — lane three, act four under (R186)')
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
    return len(b) == len(a) + 1 and b[:43] == a[:43] and b[44:] == a[43:] and b[43].startswith('> *(Appended beneath :43 by b576')


def errata_ok(S):
    a, b = S['err_pre'], S['err_now']
    ix = [i for i, l in enumerate(b) if l.startswith('- `E-2026-10-01-2` — ') or l.startswith('- `E-2026-10-01-3` — ')]
    if len(ix) != 2:
        return False
    b2 = [l for i, l in enumerate(b) if i not in ix]
    k2 = [i for i, l in enumerate(a) if l.startswith('- `E-2026-10-01-1` — ')]
    k3 = [i for i, l in enumerate(a) if l.startswith('- `E-2026-09-03-1` — ')]
    return bool(k2 and k3) and ix[0] == k2[0] + 1 and ix[1] == k3[0] + 2 and b2[:len(a) - 1] == a[:-1] and \
        (a[-1] == '' or b2[len(a) - 1].startswith(a[-1]))


def keys_carried(S):
    cell = ((S['zr'].get('c2') or {}).get('records') or {}).get('21539068', {})
    ks = ('title', 'version', 'publication_date', 'creators', 'license', 'resource_type')
    return bool(cell.get('other_keys_carried') and cell.get('keys_same')) and all(
        S['fb'].get('metadata', {}).get(k) == S['old'].get('metadata', {}).get(k) for k in ks)


def mem_ok(S):
    links = re.findall(r'\]\(([^)]+\.md)\)', S['mem'])
    ents = [l for l in S['mem'].split(NL) if l.startswith('- [')]
    stale = [x for x in links if re.search(r'^project_.*_b(559|56\d|57[0-5])\.md$', x) or x == 'project_audit_b565_paused.md']
    new = {'reference_index_archive_b559_b575.md', 'project_state_cp4_cp5_b559_b576.md', 'feedback_standing_rules_b559_b576.md'}
    return bool(links) and all(x in S['memfiles'] for x in links) and not stale and new <= set(links) and new <= S['memfiles'] \
        and len(ents) == (S['refresh'].get('after') or [0, -1])[1]


WT_HEAD = '*Appended 2026-10-01 by b576 to b575’s entry ('
TITLE = '## CP-7, act one: the observation document’s purpose statement drafted from the author’s sentences'
CP5_HEAD = '*Appended 2026-10-01 by b576, under the author’s ruling `(R186)`(1), to the critical path’s lane three (:11417) -- CP-5 CLOSED:*'
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R186) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b575`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b575' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b576 -- x'])),
    ('G-R186-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R186) END' in S['ferry'] and S['ot'].count('**(R186) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R186) ratified', '(R186) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('b543_ferry.txt @', 'b547_ferry.txt @', 'b556_ferry.txt @', 'REGISTRY.md @',
                                                                               'README.md @', 'ERRATA.md @', 'SPIRAL_MAP.md @', 'b575_zenodo_c2.txt @',
                                                                               'b575_zenodo_lv.txt @', 'b558_refresh.txt @', 'b558_editions/'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 3aff82e8`s files', lambda S: S['pushout'][0] == ['data/b575_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b575') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b575'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wt'].get('line')).startswith(WT_HEAD)
     and 'b575 AT ITS WEIGHT, CP-5 CLOSED' in fline(S, S['wt'].get('line')), lambda S: put(S, 'wt', dict(S['wt'], line=1))),
    ('G-LV-TEXT-FROM-ERRATA', 'ERRATA :564 and :567 at the pre-act blob against the banked sentences', lambda S: all(S['err_sent'])
     and S['imeta'].get('sentences') == [m.group(1) for m in S['err_sent']] and '**THE TWO SENTENCES READ FROM ERRATA: True.**' in S['zdraft'],
     lambda S: put(S, 'imeta', dict(S['imeta'], sentences=(S['imeta'].get('sentences') or ['', ''])[::-1]))),
    ('G-CALL-REDACTED', 'the c1 bank', lambda S: S['c1'].count('Bearer [TOKEN REDACTED]') == 3 and len(re.findall(r'Bearer (?!\[TOKEN REDACTED\])', S['c1'])) == 0,
     lambda S: put(S, 'c1', S['c1'].replace('Bearer [TOKEN REDACTED]', 'Bearer abc', 1))),
    ('G-WRITE-BANKED', 'the c2 bank and the results json', lambda S: S['c2'].count('POST actions/edit    : ### **201**') == 1
     and S['c2'].count('PUT metadata         : ### **200**') == 1 and S['c2'].count('POST actions/publish : ### **202**') == 1
     and 'discard' not in S['c2'] and list(((S['zr'].get('c2') or {}).get('records') or {})) == ['21539068'],
     lambda S: put(S, 'c2', S['c2'].replace('### **202**', '### **400**', 1))),
    ('G-FETCHBACK-MATCH', 'the banked fetch-back`s description against the banked intended, and the c2 bank', lambda S:
     bool(S['intended'].get('21539068')) and S['fb'].get('metadata', {}).get('description') == S['intended'].get('21539068')
     and S['c2'].count('-E] ### **MATCH**') == 1, lambda S: put(S, 'intended', {'21539068': (S['intended'].get('21539068') or '') + ' '})),
    ('G-KEYS-CARRIED', 'the results json and the fetch-back`s metadata against b575`s fetch', lambda S: keys_carried(S),
     lambda S: put(S, 'old', {'metadata': {}})),
    ('G-RECORD-FILES-SAME', 'the files-same json', lambda S: S['fsame'].get('same') is True and S['fsame'].get('version') == 'v0.10.0',
     lambda S: put(S, 'fsame', dict(S['fsame'], same=False))),
    ('G-LV-ERRATUM-WRITTEN', 'ERRATA at the banked lines', lambda S: eline(S, S['e2'].get('index_line')).startswith('- `E-2026-10-01-2` — *DEPOSIT-FACING')
     and eline(S, S['e2'].get('heading_line')).startswith('## E-2026-10-01-2 — ') and all(x and x in NL.join(S['err_now']) for x in S['e2'].get('stamps', [None]))
     and 'ERRATA :564’s and :567’s' in NL.join(S['err_now']), lambda S: put(S, 'e2', dict(S['e2'], heading_line=1))),
    ('G-SPIRAL-CORRECTION', 'SPIRAL_MAP at :44', lambda S: len(S['spm_now']) > 44 and S['spm_now'][43].startswith('> *(Appended beneath :43 by b576')
     and all(x in S['spm_now'][43] for x in ('ERRATA :85', 'ERRATA :81', 'REGISTRY :964', '65', '83')),
     lambda S: put(S, 'spm_now', S['spm_now'][:43] + [S['spm_now'][43].replace('ERRATA :85', 'ERRATA :8')] + S['spm_now'][44:])),
    ('G-SPIRAL-SCOPE', 'SPIRAL_MAP against its pre-act blob', lambda S: spiral_ok(S),
     lambda S: put(S, 'spm_now', S['spm_now'][:10] + ['x'] + S['spm_now'][11:])),
    ('G-CORPUS-ERRATUM-WRITTEN', 'ERRATA at the banked lines', lambda S: eline(S, S['e3'].get('index_line')).startswith('- `E-2026-10-01-3` — *CORPUS-FACING')
     and eline(S, S['e3'].get('index_line') - 1).startswith('- `E-2026-09-03-1` — ') and eline(S, S['e3'].get('heading_line')).startswith('## E-2026-10-01-3 — '),
     lambda S: put(S, 'e3', dict(S['e3'], index_line=1))),
    ('G-ERRATA-SCOPE', 'ERRATA against its pre-act blob', lambda S: errata_ok(S), lambda S: put(S, 'err_now', ['x'] + S['err_now'])),
    ('G-TOKEN-UNBANKED', 'every b576 bank, read for the token from the environment', lambda S: len(S['tok']) > 20 and len(S['banks']) > 30
     and all(b is not None and S['tok'].encode('utf-8') not in b for b in S['banks'].values()),
     lambda S: put(S, 'banks', dict(S['banks'], x=b'x' + S['tok'].encode('utf-8')))),
    ('G-DOC-NAMED', 'the drafts bank and PLACE-papers HEAD`s file list', lambda S: S['observ'] == [] and S['pdj'].get('doc_hits') == []
     and '**NO OBSERVATION DOCUMENT EXISTS AND (R153) NAMES NONE' in S['pdt'] and 'its working name is the' in S['pdt'],
     lambda S: put(S, 'observ', ['OBSERVATION.md'])),
    ('G-SOURCES-PRINTED', 'the drafts bank and json', lambda S: '### THE SOURCES, by path and line:' in S['pdt'] and '### NOT FOUND' not in S['pdt']
     and S['pdj'].get('sources_found') is True, lambda S: put(S, 'pdt', S['pdt'] + '### NOT FOUND')),
    ('G-DRAFTS-BANKED', 'the drafts json and bank', lambda S: set((S['pdj'].get('drafts') or {})) == {'A', 'B'} and '### DRAFT A --' in S['pdt']
     and '### DRAFT B --' in S['pdt'] and all(v['text'] in S['pdt'] for v in S['pdj']['drafts'].values()),
     lambda S: put(S, 'pdj', dict(S['pdj'], drafts={'A': S['pdj']['drafts']['A']}))),
    ('G-DRAFT-WORDS', 'each draft`s text, counted', lambda S: bool(S['pdj'].get('drafts')) and all(
        0 < len(v['text'].replace('--', ' ').split()) <= 120 for v in S['pdj']['drafts'].values()),
     lambda S: put(S, 'pdj', dict(S['pdj'], drafts=dict(S['pdj']['drafts'], A=dict(S['pdj']['drafts']['A'], text='w ' * 121))))),
    ('G-DRAFT-SOURCES', 'every author fragment of both drafts, located afresh in its source', lambda S: len(S['located']) >= 10
     and all(n for k, t, n in S['located']), lambda S: put(S, 'located', S['located'] + [('R166(1)', 'x', None)])),
    ('G-WORKLISTS-LISTED', 'the drafts json against data/b558_editions/', lambda S: len(S['editions']) == 17
     and [w[0] for w in S['pdj'].get('worklists', [])] == S['editions'] and all(e in S['pdt'] for e in S['editions']),
     lambda S: put(S, 'editions', S['editions'] + ['X'])),
    ('G-DOC-UNWRITTEN', 'PLACE-papers` diff and its changed files` text', lambda S: S['pp_added'] == [] and not any(
        v['text'][:80] in t for v in (S['pdj'].get('drafts') or {}).values() for t in S['pp_texts'].values()),
     lambda S: put(S, 'pp_added', ['A\tOBSERVATION.md'])),
    ('G-ROSTER-ALONE', 'relay 0ff04077`s files and the roster against its pre-act blob', lambda S: S['roster_c'][0] == ['tools/mirror_roster.json']
     and S['roster_c'][1] and S['roster_now'].get('files', [])[:-2] == S['roster_pre'].get('files') and S['roster_now'].get('files', [])[-2:] == list(PAGES),
     lambda S: put(S, 'roster_now', dict(S['roster_now'], files=S['roster_pre'].get('files')))),
    ('G-MIRROR-BUILT', 'the zip and the build bank', lambda S: len(S['zip_names']) == 45 and S['mj'].get('entries') == 45
     and 'built: D:\\MY-DOwnloads\\mirror-refresh-2026-10-01.zip' in S['mbuild'] and all(any(n.endswith(p) for n in S['zip_names']) for p in PAGES),
     lambda S: put(S, 'zip_names', S['zip_names'][:-1])),
    ('G-MIRROR-VERIFIED', 'the verify bank', lambda S: '### VERDICT: CLEAN ON ALL THREE CLAUSES' in S['mver'] and S['mj'].get('verify_clean') is True,
     lambda S: put(S, 'mver', S['mver'].replace('CLEAN ON ALL THREE', 'NOT CLEAN'))),
    ('G-MIRROR-AFTER-PUSH', 'the zip`s write time against the PLACE-papers push, and the source head against ls-remote', lambda S:
     S['pp_push_at'] is not None and S['zip_mtime'] > S['pp_push_at'] and ('source HEAD: %s' % S['pp_head']) in S['mbuild'] and S['pp_head'] == S['pp_remote'],
     lambda S: put(S, 'zip_mtime', 1)),
    ('G-MEMORY-REWRITTEN', 'the seat`s memory index and the refresh bank', lambda S: mem_ok(S),
     lambda S: put(S, 'mem', S['mem'] + NL + '- [x](project_detection_region_b559.md) — x')),
    ('G-CP5-CLOSING-LINE', 'OPEN_TRAILS at the banked CP-5 line', lambda S: oline(S, S['tj'].get('cp5_line')).startswith(CP5_HEAD),
     lambda S: put(S, 'tj', dict(S['tj'], cp5_line=1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(TITLE),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b576 — lane three, act four under (R186)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'CP-7 act two' in trail(S) and '`(R186)`(6)' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('CP-7 act two', 'x'))),
    ('G-NAVIGATOR-WORDING-LINE', 'this act`s trail record', lambda S: '**The navigator’s wording, recorded:**' in trail(S)
     and 'ERRATA :564’s then :567’s' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('**The navigator’s wording, recorded:**', 'x'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{PAGE: ((S['pages'][PAGE][0] or b'') + b'x', S['pages'][PAGE][1])}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff', lambda S: S['kmain'] == V015
     and S['kcur'] == 'main' and S['kdirty'] == '' and all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] == [],
     lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b576_record.py'): S['tooltext'].get(os.path.join(T, 'b576_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'the files-same json, the fetch-back`s id and version, this act`s tools', lambda S: S['fsame'].get('same') is True
     and S['fb'].get('metadata', {}).get('version') == 'v0.10.0' and str(S['fb'].get('id')) == '21539068'
     and not [f for f, t in S['tooltext'].items() if ('new' + 'version') in t or ('/fil' + 'es' + "'") in t],
     lambda S: put(S, 'fb', dict(S['fb'], id=99))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 04b98516, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b575_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md'],
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
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
                                                                          and "startswith('b576')" in S['suite'] and "data/b576_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b576')", ''))),
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
    rec('b576 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b576_checks_postpush.txt' if pushed else 'b576_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b576_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
