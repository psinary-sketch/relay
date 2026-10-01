# -*- coding: utf-8 -*-
"""b572_checks.py -- THE SUITE OF b572, UNDER (R182): GRH-WEIL ACT SEVEN, THE CRITERION AT THE χ-INSTANCE; THE CEILING.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b572_checks.txt before the push and data/b572_checks_postpush.txt after
### it. ### The harness is b568's to b571's, carried; the arms are b572's.
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
FACE = os.path.join(D, 'b572_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
PRE = dict(relay='4fca80d6', pp='49a51ec', gs='1afc8d5')
V013, V014 = 'ac157c1d0024801116d79cf41126d28780fe1152', '4dce7b97eb29733b823919bd80b08d01c82c6d8f'
MODULES = ['CriterionForward', 'CriterionConverse']
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1'}
COMMITS = dict(pushout=('547b20fb', ['data/b571_closing_push_out.txt', 'data/b571_housekeeping_push_out.txt']))
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b572')
            and 'data/b572_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    b = rd('b572_build_%s.txt' % m.lower())
    return ('Built SIDEExplicitFormula.Chi.%s' % m) in b and re.search(r'^=== END \S+ rc=0$', b, re.M) is not None


def sources():
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b572_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    kre_old, kre_new = cr0(blob(KER, V013 + ':README.md')), cr0(blob(KER, 'main:README.md'))
    S = dict(
        face=face, ferry=rd('b572_ferry.txt'), scan=rd('b572_ferry_scan.txt'), cens=rd('b572_census_stepzero.txt'),
        fcens=rd('b572_faces_census_stepzero.txt'), pins=rd('b572_pins_stepzero.txt'), procs=rd('b572_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b571_closing.txt'), reads=rd('b572_reads.txt'), branches=rd('b572_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        commits={k: (files_of(v[0]), v[1], subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', v[0], 'HEAD']).returncode == 0)
                 for k, v in COMMITS.items()},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), corr=read(os.path.join(GS, 'CORRESPONDENCE.md')),
        fj=jl('b572_findings.json'), tj=jl('b572_trail.json'), wj=jl('b572_workorder.json'), sj=jl('b572_schema.json'),
        cj=jl('b572_ceiling.json'), wt=jl('b572_weight.json'), rl=jl('b572_reality.json'), rltxt=rd('b572_reality.txt'),
        lm=jl('b572_lemmas.json'), lmtxt=rd('b572_lemmas.txt'),
        rj=jl('b572_rows.json'), sc=jl('b572_scores.json'), desk=rd('b572_desk_notes.txt'), defects=rd('b572_defects.txt'),
        cf_start=start_of('b572_attempt_criterionforward_1.txt'),
        readme_now=read(os.path.join(PP, 'README.md')), readme_pre=(blob(PP, PRE['pp'] + ':README.md') or b'').decode('utf-8').replace(chr(13), ''),
        reg_now=read(os.path.join(PP, 'REGISTRY.md')), reg_pre=(blob(PP, PRE['pp'] + ':REGISTRY.md') or b'').decode('utf-8').replace(chr(13), ''),
        builds={m: build_ok(m) for m in MODULES},
        e0=jl('b572_e0.json'), rowgen=jl('b572_rowgen.json'), kpush=rd('b572_kernel_push_out.txt'), bpush=rd('b572_branches_push_out.txt'),
        kmain=gs(KER, 'rev-parse', 'main'), kff=subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', V013, 'main']).returncode == 0,
        kns=[x for x in gs(KER, 'diff', '--name-status', V013, 'main').split(NL) if x.strip()],
        kre_prefix=bool(kre_old) and kre_new.startswith(kre_old), kre_new=kre_new.decode('utf-8', 'replace'),
        held_exists=bool(gs(KER, 'branch', '--list', 'grh-weil-b572-held')),
        page_head=blob(PP, 'HEAD:' + PAGE), page_b569=blob(PP, 'bd2a616:' + PAGE),
        errata_now=cr0(open(os.path.join(PP, 'ERRATA.md'), 'rb').read()), errata_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')),
        faces_now=cr0(open(os.path.join(PP, 'FACES_LEDGER.md'), 'rb').read()), faces_pre=cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md')),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read()),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b571*') for r in ('D:/relay', PP, GS, KER)},
        tools9=[os.path.join(T, f) for f in os.listdir(T) if f.startswith('b572_')],
        dep_clean=gs(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == '',
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b572_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b572_mustnotexist.txt')), table_changed=None,
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
    i = t.find('### b572 — lane two, act twelve under (R182)')
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
    rows = [l for l in S['corr'].split(NL) if re.match(r'^\| 43[2-6] \|', l)]
    nums = sorted(l.split('|')[1].strip() for l in rows)
    final = {o['row']: o['exit'] for o in S['rj'].get('rows', [])}
    return nums == ['432', '433', '434', '435', '436'] and len(final) == 5 and all(v == 0 for v in final.values())


def g2_names(face):
    g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def written_at(text):
    m = re.search(r'written at \(UTC\) (\S+)', text)
    return m.group(1) if m else '9'


CEIL_HEAD = "*(Appended under the author's ruling `(R182)`(2), 2026-10-01, b572"
CEIL_TEXT = 'The criterion for χ is not yet composed.'


def placed_once(pre, now):
    a, b = pre.split(NL), now.split(NL)
    if len(b) != len(a) + 2:
        return False
    for k in range(len(a) + 1):
        if b[:k] == a[:k] and b[k + 2:] == a[k:] and b[k] == '' and b[k + 1].startswith(CEIL_HEAD) and CEIL_TEXT in b[k + 1]:
            return True
    return False


def placed_line(text, n):
    ls = text.split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


NS = 'SIDEExplicitFormula.GRHWeil.'
WT_HEAD = '*Appended 2026-10-01 by b572 to b571’s entry ('
WO_HEAD = '*Appended 2026-10-01 by b572, under the author’s ruling `(R182)`(6), to the W-ORD-GRH-WEIL entry'
SC_HEAD = '*Appended 2026-10-01 by b572, under the author’s ruling `(R182)`(5), to the W-ORD-GRH-WEIL entry'
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R182) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
     and any(l.startswith('547b20fb') and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith('547b20fb')), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b571`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b571' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == ['547b20fb'],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b572 -- x'])),
    ('G-R182-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R182) END' in S['ferry'] and S['ot'].count('**(R182) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R182) ratified', '(R182) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('Seam.lean @', ':101', 'PowerLimit.lean @', 'GRHWeil.lean @',
                                                                               'README.md @', 'REGISTRY.md @', 'W-ORD-GRH-WEIL heading'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 547b20fb`s files', lambda S: alone(S, 'pushout'),
     lambda S: put(S, 'commits', dict(S['commits'], pushout=(['x'], S['commits']['pushout'][1], True)))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b571') == 6, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b571'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b571': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wt'].get('lines', [0])[0]).startswith(WT_HEAD)
     and 'b571 AT ITS WEIGHT' in fline(S, S['wt'].get('lines', [0])[0]), lambda S: put(S, 'wt', dict(S['wt'], lines=[1, 2]))),
    ('G-NAV-CLAUSE', 'FINDINGS at the banked clause line', lambda S: len(S['wt'].get('lines', [])) == 2
     and fline(S, S['wt']['lines'][1]).startswith(WT_HEAD) and 'ĝ(0)·log N' in fline(S, S['wt']['lines'][1])
     and 'k(0)·log N' in fline(S, S['wt']['lines'][1]), lambda S: put(S, 'wt', dict(S['wt'], lines=[1, 2]))),
    ('G-CEILING-README', 'README at the placed line, and the pre-act blob', lambda S: placed_line(S['readme_now'], S['cj'].get('readme')).startswith(CEIL_HEAD)
     and CEIL_TEXT in placed_line(S['readme_now'], S['cj'].get('readme')), lambda S: put(S, 'cj', dict(S['cj'], readme=1))),
    ('G-CEILING-REGISTRY', 'REGISTRY at the placed line', lambda S: placed_line(S['reg_now'], S['cj'].get('registry')).startswith(CEIL_HEAD)
     and CEIL_TEXT in placed_line(S['reg_now'], S['cj'].get('registry')), lambda S: put(S, 'cj', dict(S['cj'], registry=1))),
    ('G-CEILING-FINDINGS', 'FINDINGS at the ceiling record line', lambda S: 'THE CEILING’S χ-SENTENCE' in fline(S, S['cj'].get('findings'))
     and '(:6144)' in fline(S, S['cj'].get('findings')) and CEIL_TEXT in fline(S, S['cj'].get('findings')),
     lambda S: put(S, 'cj', dict(S['cj'], findings=1))),
    ('G-REALITY-READ', 'the reality bank and json', lambda S: S['rl'].get('choice') == 'REFLECTION' and S['rl'].get('conj_uses') == []
     and 'Zeta23.ZeroConfig.reflect_mem' in S['rl'].get('reflection_uses', []) and 'THE CHOICE: REFLECTION' in S['rltxt'],
     lambda S: put(S, 'rl', dict(S['rl'], conj_uses=['x']))),
    ('G-REALITY-FIRST', 'the reality bank`s time against the first kernel elaboration', lambda S: bool(S['cf_start'])
     and written_at(S['rltxt']) < S['cf_start'], lambda S: put(S, 'cf_start', '0')),
    ('G-H24A-SCORED', 'the scores and the desk', lambda S: scored(S, 'H24a'), lambda S: put(S, 'desk', '')),
    ('G-LEMMA-LIST', 'the lemma json and bank', lambda S: len(S['lm'].get('converse', [])) > 100 and len(S['lm'].get('converse_zeta', [])) > 0
     and all(('naming: ' in l) for l in S['lmtxt'].split(NL) if 'ζ-NAMING' in l and not l.startswith('###')),
     lambda S: put(S, 'lm', dict(S['lm'], converse=[]))),
    ('G-LEMMAS-FIRST', 'the lemma bank`s time against the first kernel elaboration', lambda S: bool(S['cf_start'])
     and written_at(S['lmtxt']) < S['cf_start'], lambda S: put(S, 'cf_start', '0')),
    ('G-H24C-SCORED', 'the scores and the desk', lambda S: scored(S, 'H24c'), lambda S: put(S, 'desk', '')),
    ('G-FORWARD-BUILT', 'the forward build bank and the E0 json', lambda S: S['builds'].get('CriterionForward') is True
     and S['e0'].get('rows', {}).get(NS + 'grh_chi_imp_h2_sign_chi', {}).get('std3') is True,
     lambda S: put(S, 'builds', dict(S['builds'], CriterionForward=False))),
    ('G-H24B-SCORED', 'the scores and the desk', lambda S: scored(S, 'H24b'), lambda S: put(S, 'desk', '')),
    ('G-PIECES-BANKED', 'the two build banks', lambda S: all(S['builds'].values()) and len(S['builds']) == 2,
     lambda S: put(S, 'builds', dict(S['builds'], CriterionConverse=False))),
    ('G-HOLD-OR-LAND', 'the E0 json, the scores, the branch list', lambda S: S['e0'].get('rows', {}).get(NS + 'h2_sign_chi_iff_grh_chi', {}).get('grade') == 'DERIVES'
     and S['sc'].get('H24d', [''])[0] == 'HELD' and not S['held_exists'], lambda S: put(S, 'held_exists', True)),
    ('G-H24D-SCORED', 'the scores and the desk', lambda S: scored(S, 'H24d'), lambda S: put(S, 'desk', '')),
    ('G-BUILD-PRINTS', 'the E0 json`s prints', lambda S: len(S['e0'].get('rows', {})) == 17 and all(r['std3'] for r in S['e0']['rows'].values())
     and all(a is not None for a in S['e0'].get('consumed', {}).values()), lambda S: put(S, 'e0', dict(S['e0'], rows={}))),
    ('G-BUILD-GRADES', 'the E0 gate, read at the branch tip', lambda S: S['e0'].get('gate') is True and S['e0'].get('tip') == V014
     and S['e0'].get('rev') == 'grh-weil-b572', lambda S: put(S, 'e0', dict(S['e0'], rev='main'))),
    ('G-ROWGEN-DIFF', 'the rowgen json', lambda S: S['rowgen'].get('clean') is True and len(S['rowgen'].get('rows', {})) == 4,
     lambda S: put(S, 'rowgen', dict(S['rowgen'], clean=False))),
    ('G-MAIN-FF', 'the kernel`s main and its ancestry', lambda S: S['kmain'] == V014 and S['kff'], lambda S: put(S, 'kff', False)),
    ('G-TAG-BY-SCRIPT', 'the kernel push capture', lambda S: 0 <= S['kpush'].find('main read back at the remote: ' + V014) < S['kpush'].find('push_gated: tag v0.14 made at the read-back')
     and ('tag v0.14 peeled local %s remote %s' % (V014, V014)) in S['kpush'], lambda S: put(S, 'kpush', S['kpush'].replace('tag v0.14 made', 'x'))),
    ('G-HELD-BRANCH-PUSHED', 'the branch push bank', lambda S: ('grh-weil-b572 local %s remote %s' % (V014, V014)) in S['bpush']
     and 'grh-weil-b572-held is not made' in S['bpush'], lambda S: put(S, 'bpush', '')),
    ('G-KERNEL-STATEMENTS-KEPT', 'the kernel, v0.13 against main', lambda S: bool(S['kns']) and all(x.startswith('A\t') or x == 'M\tREADME.md' for x in S['kns'])
     and S['kre_prefix'], lambda S: put(S, 'kns', S['kns'] + ['M\tSIDEExplicitFormula/GRHWeil.lean'])),
    ('G-KERNEL-README-SECTION', 'the kernel README at main', lambda S: S['kre_new'].count('## Appended at act b572 (ruling (R182)(4))') == 1,
     lambda S: put(S, 'kre_new', '')),
    ('G-SCHEMA-PRICED', 'OPEN_TRAILS at the schema line, and its json', lambda S: oline(S, S['sj'].get('line')).startswith(SC_HEAD)
     and 'A PRICED ITEM, NOT STARTED, THE GENERIC SCHEMA' in oline(S, S['sj'].get('line'))
     and sum(len(v) for v in S['sj'].get('kinds', {}).values()) == len(S['lm'].get('converse_zeta', [])),
     lambda S: put(S, 'sj', dict(S['sj'], line=1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(
        '## GRH-Weil, act seven: the criterion at the χ-instance, the form’s reality by reflection, h2_sign_chi ⟺ GRH_chi landed'),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORR-ROWS', 'CORRESPONDENCE rows 432-436', lambda S: corr_rows_ok(S), lambda S: put(S, 'corr', S['corr'] + NL + '| 433 | dup |')),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b572 — lane two, act twelve under (R182)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORK-ORDERS-UPDATED', 'OPEN_TRAILS at the work-order line, and this act`s trail record', lambda S: oline(S, S['wj'].get('line')).startswith(WO_HEAD)
     and 'THE CRITERION FOR χ LANDED' in oline(S, S['wj'].get('line')) and 'the work-order line' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('THE CRITERION FOR χ LANDED', 'x').replace('the work-order line', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'the schema or CP-5' in trail(S) and 'author’s word' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('the schema or CP-5', 'x'))),
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
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 4fca80d6, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b571_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md']),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'].startswith(cr0(S['ot_pre'])),
     lambda S: put(S, 'ot_now', b'x' + S['ot_now'])),
    ('G-PREFIX-KEPT', 'README and REGISTRY against their pre-act blobs', lambda S: placed_once(S['readme_pre'], S['readme_now'])
     and placed_once(S['reg_pre'], S['reg_now']), lambda S: put(S, 'reg_now', S['reg_now'].replace('## ', '##  ', 1))),
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
                                                                          and "startswith('b572')" in S['suite'] and "data/b572_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b572')", ''))),
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
    rec('b572 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at 4fca80d6 by blob id; changed %s' % (S['prior_n'], S['prior_bad'] or 'NONE'))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b572_checks_postpush.txt' if pushed else 'b572_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b572_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
