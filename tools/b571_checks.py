# -*- coding: utf-8 -*-
"""b571_checks.py -- THE SUITE OF b571, UNDER (R181): GRH-WEIL ACT SIX; THE FACES_LEDGER FORM; ROWGEN ON LEAN NAMES.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b571_checks.txt before the push and data/b571_checks_postpush.txt after
### it. ### The harness is b568's, b569's and b570's, carried; the arms are b571's.
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
FACE = os.path.join(D, 'b571_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
PRE = dict(relay='b93f47a4', pp='0136597', gs='a6d2a72')
V012, V013 = '141e844b74453a4c329bb6b3a8a70954b6cb04cf', 'ac157c1d0024801116d79cf41126d28780fe1152'
MODULES = ['FullLine', 'Horizontal', 'ZeroSumLimit', 'FullLineAssembly', 'Main']
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844'}
COMMITS = dict(pushout=('96daad63', ['data/b570_closing_push_out.txt', 'data/b570_housekeeping_push_out.txt']),
               faces=('e693efde', ['tools/terminal_table.py', 'tools/test_faces_form.py']),
               rowgen=('618143a8', ['tools/rowgen/rowgen.py', 'tools/test_rowgen_ident.py']))
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b571')
            and 'data/b571_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    b = rd('b571_build_%s.txt' % m.lower())
    return ('Built SIDEExplicitFormula.Chi.%s' % m) in b and re.search(r'^=== END \S+ rc=0$', b, re.M) is not None


def sources():
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b571_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    kre_old, kre_new = cr0(blob(KER, V012 + ':README.md')), cr0(blob(KER, 'main:README.md'))
    S = dict(
        face=face, ferry=rd('b571_ferry.txt'), scan=rd('b571_ferry_scan.txt'), cens=rd('b571_census_stepzero.txt'),
        fcens=rd('b571_faces_census_stepzero.txt'), pins=rd('b571_pins_stepzero.txt'), procs=rd('b571_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b570_closing.txt'), reads=rd('b571_reads.txt'), branches=rd('b571_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        commits={k: (files_of(v[0]), v[1], subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', v[0], 'HEAD']).returncode == 0)
                 for k, v in COMMITS.items()},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), corr=read(os.path.join(GS, 'CORRESPONDENCE.md')),
        fj=jl('b571_findings.json'), tj=jl('b571_trail.json'), nj=jl('b571_nav_clauses.json'), wj=jl('b571_workorder.json'),
        cj=jl('b571_chiff_line.json'), chiff=jl('b571_chiff.json'), chifftxt=rd('b571_chiff.txt'), r70=jl('b571_rows570.json'),
        rj=jl('b571_rows.json'), sc=jl('b571_scores.json'), desk=rd('b571_desk_notes.txt'), defects=rd('b571_defects.txt'),
        tff=rd('b571_test_faces_form.txt'), tri=rd('b571_test_rowgen_ident.txt'),
        ttsrc=read(os.path.join(T, 'terminal_table.py')), rgsrc=read(os.path.join(T, 'rowgen', 'rowgen.py')),
        flst=rd('b571_fullline_statements.txt'), fl_start=start_of('b571_attempt_fullline_1.txt'),
        mlist=rd('b571_module_list.txt'), hz_start=start_of('b571_attempt_horizontal_1.txt'),
        builds={m: build_ok(m) for m in MODULES},
        e0=jl('b571_e0.json'), rowgen=jl('b571_rowgen.json'), kpush=rd('b571_kernel_push_out.txt'), bpush=rd('b571_branches_push_out.txt'),
        kmain=gs(KER, 'rev-parse', 'main'), kff=subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', V012, 'main']).returncode == 0,
        kns=[x for x in gs(KER, 'diff', '--name-status', V012, 'main').split(NL) if x.strip()],
        kre_prefix=bool(kre_old) and kre_new.startswith(kre_old), kre_new=kre_new.decode('utf-8', 'replace'),
        held_exists=bool(gs(KER, 'branch', '--list', 'grh-weil-b571-held')),
        page_head=blob(PP, 'HEAD:' + PAGE), page_b569=blob(PP, 'bd2a616:' + PAGE),
        errata_now=cr0(open(os.path.join(PP, 'ERRATA.md'), 'rb').read()), errata_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')),
        faces_now=cr0(open(os.path.join(PP, 'FACES_LEDGER.md'), 'rb').read()), faces_pre=cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md')),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read()),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b570*') for r in ('D:/relay', PP, GS, KER)},
        tools9=[os.path.join(T, f) for f in os.listdir(T) if f.startswith('b571_') or f in ('test_faces_form.py', 'test_rowgen_ident.py')],
        dep_clean=gs(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == '',
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b571_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b571_mustnotexist.txt')), table_changed=None,
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
    i = t.find('### b571 — lane two, act eleven under (R181)')
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
    rows = [l for l in S['corr'].split(NL) if re.match(r'^\| 4(2[6-9]|3[01]) \|', l)]
    nums = sorted(l.split('|')[1].strip() for l in rows)
    final = {o['row']: o['exit'] for o in S['rj'].get('rows', [])}
    return nums == ['426', '427', '428', '429', '430', '431'] and len(final) == 6 and all(v == 0 for v in final.values())


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def written_at(text):
    m = re.search(r'written at \(UTC\) (\S+)', text)
    return m.group(1) if m else '9'


def conflict_pair(S):
    m = re.search(r'CONFLICT (\d+) BEFORE AND (\d+) AFTER', S['chifftxt'])
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


NS = 'SIDEExplicitFormula.GRHWeil.'
NAV_HEAD = '*Appended 2026-10-01 by b571, under the author’s ruling `(R181)`(1), to b570’s record'
WO_HEAD = '*Appended 2026-10-01 by b571, under the author’s ruling `(R181)`(5), to the W-ORD-GRH-WEIL entry'
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R181) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins'],
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '  1234   5678 lean.exe        2026-09-01 00:00:00  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against every later commit', lambda S: S['lock_epoch'] is not None
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith('96daad63')), lambda S: put(S, 'lock_epoch', 4102444800)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b570`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b570' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == ['96daad63'],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b571 -- x'])),
    ('G-R181-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R181) END' in S['ferry'] and S['ot'].count('**(R181) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R181) ratified', '(R181) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('FullLine.lean @', ':385', 'XiLogDeriv.lean @', 'FACES_LEDGER.md @',
                                                                               'rowgen.py @', 'CORRESPONDENCE.md @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 96daad63`s files', lambda S: alone(S, 'pushout'),
     lambda S: put(S, 'commits', dict(S['commits'], pushout=(['x'], S['commits']['pushout'][1], True)))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b570') == 6, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b570'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b570': '0000000'}))),
    ('G-FACES-FORM', 'terminal_table.py and the test bank', lambda S: 'FACES_SUP_RE' in S['ttsrc']
     and 'supersede_faces(supersede_findings(' in S['ttsrc'] and 'raise FacesRefusal' in S['ttsrc'] and '10 of 10 cases as wanted -- PASS' in S['tff'],
     lambda S: put(S, 'tff', '')),
    ('G-FACES-FORM-ALONE', 'relay e693efde`s files', lambda S: alone(S, 'faces'),
     lambda S: put(S, 'commits', dict(S['commits'], faces=(['x'], S['commits']['faces'][1], True)))),
    ('G-CHIFF-LINE', 'FINDINGS at the banked line, and the regeneration`s row', lambda S: fline(S, S['cj'].get('line')).startswith(
        'SUPERSEDES FACES_LEDGER :497 for ch_iff_rh: T0') and S['chiff'].get('after', {}).get('cells') == []
     and S['chiff'].get('after', {}).get('grade') == 'UNGRADED', lambda S: put(S, 'cj', dict(S['cj'], line=1))),
    ('G-CONFLICT-COUNTED', 'the chiff bank`s count line and its json', lambda S: conflict_pair(S)[0] is not None and conflict_pair(S)[0] == conflict_pair(S)[1]
     == S['chiff'].get('before', {}).get('counts', {}).get('conflict') == S['chiff'].get('after', {}).get('counts', {}).get('conflict'),
     lambda S: put(S, 'chifftxt', S['chifftxt'].replace(' BEFORE AND ', ' BEFORE AND 9'))),
    ('G-ROWGEN-IDENT', 'rowgen.py and the test bank', lambda S: 'LEAN_NAME' in S['rgsrc'] and "re.findall(r'`(' + LEAN_NAME" in S['rgsrc']
     and '9 of 9 cases as wanted -- PASS' in S['tri'], lambda S: put(S, 'tri', '')),
    ('G-ROWGEN-IDENT-ALONE', 'relay 618143a8`s files', lambda S: alone(S, 'rowgen'),
     lambda S: put(S, 'commits', dict(S['commits'], rowgen=(['x'], S['commits']['rowgen'][1], True)))),
    ('G-TERMINAL-ROWS-PRINTED', 'the rows-421-425 json', lambda S: S['r70'].get('read421') is True and S['r70'].get('others_unchanged') is True
     and len(S['r70'].get('rows', {})) == 5, lambda S: put(S, 'r70', dict(S['r70'], read421=False))),
    ('G-NAV-CLAUSES', 'OPEN_TRAILS at the two banked lines', lambda S: len(S['nj'].get('lines', [])) == 2
     and oline(S, S['nj']['lines'][0]).startswith(NAV_HEAD) and 'Abel-summation' in oline(S, S['nj']['lines'][0])
     and oline(S, S['nj']['lines'][1]).startswith(NAV_HEAD) and 'moves nine' in oline(S, S['nj']['lines'][1]),
     lambda S: put(S, 'nj', dict(S['nj'], lines=[1, 2]))),
    ('G-FULLLINE-STATEMENT-FIRST', 'the statements bank`s time against the first elaboration', lambda S: bool(S['fl_start'])
     and written_at(S['flst']) < S['fl_start'] and 'FlineCond_chi' in S['flst'] and 'verticals_eq_chi' in S['flst'], lambda S: put(S, 'fl_start', '0')),
    ('G-FOLD-BUILT', 'the FullLine build bank and the E0 json', lambda S: S['builds'].get('FullLine') is True
     and S['e0'].get('rows', {}).get(NS + 'verticals_eq_chi', {}).get('std3') is True, lambda S: put(S, 'builds', dict(S['builds'], FullLine=False))),
    ('G-H23A-SCORED', 'the scores and the desk', lambda S: scored(S, 'H23a'), lambda S: put(S, 'desk', '')),
    ('G-MODULE-LIST-FIRST', 'the module list`s time against the first module after FullLine', lambda S: bool(S['hz_start'])
     and written_at(S['mlist']) < S['hz_start'] and all(('(%d) %s' % (i + 1, m)) in S['mlist'] for i, m in enumerate(MODULES[1:])),
     lambda S: put(S, 'hz_start', '0')),
    ('G-PIECES-BANKED', 'the five build banks', lambda S: all(S['builds'].values()) and len(S['builds']) == 5,
     lambda S: put(S, 'builds', dict(S['builds'], Main=False))),
    ('G-HOLD-OR-LAND', 'the E0 json, the scores, the branch list', lambda S: S['e0'].get('rows', {}).get(NS + 'EF_lit_chi_holds', {}).get('grade') == 'DERIVES'
     and S['sc'].get('H23c', [''])[0] == 'HELD' and not S['held_exists'], lambda S: put(S, 'held_exists', True)),
    ('G-H23B-SCORED', 'the scores and the desk', lambda S: scored(S, 'H23b'), lambda S: put(S, 'desk', '')),
    ('G-H23C-SCORED', 'the scores and the desk', lambda S: scored(S, 'H23c'), lambda S: put(S, 'desk', '')),
    ('G-BUILD-PRINTS', 'the E0 json`s prints', lambda S: len(S['e0'].get('rows', {})) == 29 and all(r['std3'] for r in S['e0']['rows'].values())
     and all(a is not None for a in S['e0'].get('consumed', {}).values()), lambda S: put(S, 'e0', dict(S['e0'], rows={}))),
    ('G-BUILD-GRADES', 'the E0 gate, read on the branch', lambda S: S['e0'].get('gate') is True and S['e0'].get('tip') == V013
     and S['e0'].get('rev') == 'grh-weil-b571', lambda S: put(S, 'e0', dict(S['e0'], rev='main'))),
    ('G-ROWGEN-DIFF', 'the rowgen json', lambda S: S['rowgen'].get('clean') is True and len(S['rowgen'].get('rows', {})) == 5,
     lambda S: put(S, 'rowgen', dict(S['rowgen'], clean=False))),
    ('G-MAIN-FF', 'the kernel`s main and its ancestry', lambda S: S['kmain'] == V013 and S['kff'], lambda S: put(S, 'kff', False)),
    ('G-TAG-BY-SCRIPT', 'the kernel push capture', lambda S: 0 <= S['kpush'].find('main read back at the remote: ' + V013) < S['kpush'].find('push_gated: tag v0.13 made at the read-back')
     and ('tag v0.13 peeled local %s remote %s' % (V013, V013)) in S['kpush'], lambda S: put(S, 'kpush', S['kpush'].replace('tag v0.13 made', 'x'))),
    ('G-HELD-BRANCH-PUSHED', 'the branch push bank', lambda S: ('grh-weil-b571 local %s remote %s' % (V013, V013)) in S['bpush']
     and 'grh-weil-b571-held is not made' in S['bpush'], lambda S: put(S, 'bpush', '')),
    ('G-KERNEL-STATEMENTS-KEPT', 'the kernel, v0.12 against main', lambda S: bool(S['kns']) and all(x.startswith('A\t') or x == 'M\tREADME.md' for x in S['kns'])
     and S['kre_prefix'], lambda S: put(S, 'kns', S['kns'] + ['M\tSIDEExplicitFormula/Chi/Statement.lean'])),
    ('G-KERNEL-README-SECTION', 'the kernel README at main', lambda S: S['kre_new'].count('## Appended at act b571 (ruling (R181)(4))') == 1,
     lambda S: put(S, 'kre_new', '')),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(
        '## GRH-Weil, act six: the fold at χ⁻¹ with the conductor, the modules after FullLine, the explicit formula for χ landed'),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORR-ROWS', 'CORRESPONDENCE rows 426-431', lambda S: corr_rows_ok(S), lambda S: put(S, 'corr', S['corr'] + NL + '| 427 | dup |')),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b571 — lane two, act eleven under (R181)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORK-ORDERS-UPDATED', 'OPEN_TRAILS at the work-order line, and this act`s trail record', lambda S: oline(S, S['wj'].get('line')).startswith(WO_HEAD)
     and 'THE EXPLICIT FORMULA FOR χ LANDED' in oline(S, S['wj'].get('line')) and 'the work-order line' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('THE EXPLICIT FORMULA FOR χ LANDED', 'x').replace('the work-order line', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'act seven' in trail(S) and 'h2_sign_chi ⟺ GRH_chi' in trail(S) and 'CP-5' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('act seven', 'x'))),
    ('G-PAGE-UNCHANGED', 'the page at PLACE-papers HEAD against b569`s', lambda S: S['page_head'] is not None and S['page_head'] == S['page_b569'],
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
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at b93f47a4, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b570_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md']),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'].startswith(cr0(S['ot_pre'])),
     lambda S: put(S, 'ot_now', b'x' + S['ot_now'])),
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
                                                                          and "startswith('b571')" in S['suite'] and "data/b571_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b571')", ''))),
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
    rec('b571 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at b93f47a4 by blob id; changed %s' % (S['prior_n'], S['prior_bad'] or 'NONE'))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b571_checks_postpush.txt' if pushed else 'b571_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b571_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
