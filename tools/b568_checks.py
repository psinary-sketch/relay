# -*- coding: utf-8 -*-
"""b568_checks.py -- THE SUITE OF b568, UNDER (R178): CP-4, THE PAGE WITHOUT NARRATIVE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block, read off the face (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the
### terminal table (R107) unless `--rerun-postpush <name>`; it writes data/b568_checks.txt before the push and
### data/b568_checks_postpush.txt after it.
### ### G-CHAIN-PAGE regenerates the page from the node list by one lean call (tools/g_chain_page.py) and compares it with
### PLACE-papers HEAD's committed blob, byte for byte.
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

import banned_terms as BT     # noqa: E402
import chain_page as C        # noqa: E402
import e0_rule as E0          # noqa: E402
import g_chain_page as G      # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
FACE = os.path.join(D, 'b568_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
PRE = dict(relay='d77bb7aa', pp='5340891', gs='885d1dc')
PRE_HEADS = {'relay': 'd77bb7aa', 'MY-DOwnloads/PLACE-papers': '5340891e', 'SIDE-global-section': '885d1dcb',
             'SIDE-explicit-formula': '6baed63a', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a',
             'SIDE-effects': 'ef4cff77', 'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368',
             'SIDE-structural-error-correction': '6a4f4829', 'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83'}
COMMITS = dict(pushout=('9e9327ba', ['data/b567_closing_push_out.txt']),
               tag=('f35256d8', ['tools/push_gated.sh', 'tools/test_push_gated.sh']),
               asof=('2625d82d', ['tools/asof.py', 'tools/b566_checks.py', 'tools/b567_checks.py', 'tools/test_asof.py']),
               e0=('09f7f60e', ['data/b568_e0_rule_selftest.txt', 'tools/e0_rule.py']),
               gen=('3b3152f4', ['data/b568_nodes.txt', 'data/b568_probe_out.txt', 'data/b568_test_chain_page.txt', 'tools/chain_page.py',
                                 'tools/test_chain_page.py']),
               arm=('65916c16', ['data/b568_test_g_chain_page.txt', 'tools/g_chain_page.py', 'tools/test_g_chain_page.py']))
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
OPEN_LINE = C.OPEN_LINE
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b568')
            and 'data/b568_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
        ch |= set(l[3:].strip() for l in git(repo, 'status', '--porcelain')[1].split(NL)
                  if l.startswith('?? ') and l[3:].strip() == PAGE)
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def sources():
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b568_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    page_head = blob(PP, 'HEAD:' + PAGE)
    page_now = open(os.path.join(PP, PAGE), 'rb').read() if os.path.exists(os.path.join(PP, PAGE)) else None
    readme = blob(PP, 'HEAD:README.md') or b''
    S = dict(
        face=face, ferry=rd('b568_ferry.txt'), scan=rd('b568_ferry_scan.txt'), cens=rd('b568_census_stepzero.txt'),
        fcens=rd('b568_faces_census_stepzero.txt'), pins=rd('b568_pins_stepzero.txt'), procs=rd('b568_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        seal567=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                                os.path.join(D, 'b567_registration_2026-10-01.txt')], capture_output=True, text=True,
                               encoding='utf-8', errors='replace').stdout,
        prior=rd('b567_closing.txt'), reads=rd('b568_reads.txt'), branches=rd('b568_branches.txt'), oldlake=rd('b568_oldlake.txt'),
        old_exists=os.path.exists('D:/b567-lake-51e6992e'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        commits={k: (files_of(v[0]), v[1], subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', v[0], 'HEAD']).returncode == 0)
                 for k, v in COMMITS.items()},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), corr=read(os.path.join(GS, 'CORRESPONDENCE.md')),
        fj=jl('b568_findings.json'), tj=jl('b568_trail.json'), rj=jl('b568_rows.json'), sc=jl('b568_scores.json'), h20=jl('b568_h20ab.json'),
        add=rd('b568_b567_h18b_addendum.txt'), zbj=jl('b568_zetabounds_names.json'), dich=rd('b568_dichotomy.txt'),
        e0src=read(os.path.join(T, 'e0_rule.py')), e0ok=E0.self_test(), standing=read(os.path.join(T, 'FERRY_STANDING.md')),
        pg=read(os.path.join(T, 'push_gated.sh')), tpg=rd('b568_test_push_gated.txt'), tasof=rd('b568_test_asof.txt'),
        r566=rd('b568_b566_rerun_after.txt'), r567=rd('b568_b567_rerun_after.txt'), tgen=rd('b568_test_chain_page.txt'),
        targ=rd('b568_test_g_chain_page.txt'), runs=rd('b568_page_runs.txt'), cellsj=jl('b568_node_cells.json'),
        celltxt=rd('b568_node_cells.txt'), desk=rd('b568_desk_notes.txt'),
        nodes=C.read_nodes(os.path.join(D, 'b568_nodes.txt')),
        page=page_head if page_head is not None else page_now, page_committed=page_head is not None,
        readme121=readme.split(b'\n')[120] if len(readme.split(b'\n')) > 120 else b'',
        errata_now=cr0(open(os.path.join(PP, 'ERRATA.md'), 'rb').read()), errata_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')),
        faces_now=cr0(open(os.path.join(PP, 'FACES_LEDGER.md'), 'rb').read()), faces_pre=cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md')),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read()),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        gs_diff=sorted(x for x in gs(GS, 'diff', '--name-only', PRE['gs']).split(NL) if x.strip()),
        tags=gs(KER, 'tag', '--sort=creatordate').split(NL),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b567*') for r in ('D:/relay', PP, GS, KER)},
        tools8=[os.path.join(T, f) for f in os.listdir(T) if f.startswith('b568_') or f in ('chain_page.py', 'g_chain_page.py', 'asof.py', 'e0_rule.py')],
        dep_clean=gs(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == '',
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b568_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b568_mustnotexist.txt')),
    )
    S['zen'] = [f for f in S['tools8'] if ('https://' + 'zenodo' + '.org') in read(f)]
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        f = os.path.basename(p)
        if f in TABLE_FILES:
            continue
        fp = os.path.join(ROOT, p)
        raw = open(fp, 'rb').read() if os.path.exists(fp) else None
        if raw is None or i not in (blob_id(raw), blob_id(cr0(raw))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    pp_changed = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    pp_changed |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    if page_now is not None:
        pp_changed.add(PAGE)
    S['pp_changed'] = sorted(pp_changed)
    S['stem_hits'] = [m.group(0) for l in (S['page'] or b'').decode('utf-8').split(NL) for m in BT.PAT.finditer(l)]
    rec('  ### G-CHAIN-PAGE: regenerating the page by one lean call (tools/g_chain_page.py) ...')
    import tempfile
    S['arm'] = G.arm(os.path.join(D, 'b568_nodes.txt'), tempfile.mkdtemp(), None, committed=S['page'])
    rec('  ### G-CHAIN-PAGE regeneration: exit %d ; %s ; committed at PLACE-papers HEAD: %s' % (S['arm']['rc'], S['arm']['log'][-1:],
                                                                                            S['page_committed']))
    return S


def put(S, k, v):
    S[k] = v
    return S


def page_lines(S):
    return (S['page'] or b'').split(b'\n')


def page_form(S):
    pl = page_lines(S)
    if b'## Placement' not in pl:
        return False
    i = pl.index(b'## Placement')
    heads = [l for l in pl if l.startswith(b'#')]
    pre = [l for l in pl[:i] if l.strip()]
    body = [l for l in pre if re.match(rb'^\d+\. `', l)]
    head = pl[2].decode('utf-8') if len(pl) > 2 else ''
    sentences = [s for s in re.split(r'(?<=[.])\s+(?=[A-Z])', head) if s.strip()]
    others = [l for l in pre if not l.startswith(b'#') and l not in body and l not in (pl[2], pre[-1], pre[-2])]
    # ### after the open node and the last derived line: only the two table headings, table rows and blank lines (b568's
    # ### defect (i): the first version read only the lines above the tables, and its positive control passed)
    post = [l for l in pl[i:] if l.strip() and not l.startswith(b'## ') and not l.startswith(b'|')]
    return (heads == [b'# THE CLAUSE AND ITS COMPILED FACES', b'## Placement', b'## Correspondence'] and len(sentences) <= 3
            and len(body) == len(S['nodes'][0]) and pre[-2].decode('utf-8') == OPEN_LINE and not others and not post)


def last_line(S):
    pl = page_lines(S)
    if b'## Placement' not in pl:
        return False
    pre = [l for l in pl[:pl.index(b'## Placement')] if l.strip()]
    return bool(S['readme121']) and pre[-1] == S['readme121']


def oline(S, n):
    ls = S['ot'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def fline(S, n):
    ls = S['find'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def trail(S):
    t = S['ot']
    i = t.find('### b568 — lane three, act one under (R178)')
    return t[i:] if i >= 0 else ''


def entry(S):
    t = S['find']
    i = t.find('## CP-4, act one: the page of the compiled chain')
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    pats = S['globs']
    return all(any(fnmatch.fnmatch(f, p) for p in pats) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    # ### the needle is BUILT from fragments, so it cannot match its own definition (b568's defect (j): the first version
    # ### found itself in this file and failed live)
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item']
    pat = re.compile(r'\b(' + '|'.join(words) + r')\b')
    return not [f for f in S['tools8'] if pat.search(strip_prose(read(f)))]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R178) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-REG-LOCKED-FIRST', 'the face`s lock time against the first instrument commit`s time',
     lambda S: S['lock_epoch'] is not None and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith('9e9327ba')),
     lambda S: put(S, 'lock_epoch', 4102444800)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify`s verdict line', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b567`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b567' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'the face`s section (0) and relay`s log before the lock: 9e9327ba alone',
     lambda S: 'Nothing but reads and the step-zero banks' in S['face'] and S['lock_epoch'] is not None
     and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == ['9e9327ba'],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b568 -- x'])),
    ('G-R178-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R178) END' in S['ferry'] and S['ot'].count('**(R178) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R178) ratified', '(R178) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('README.md @', ':121', 'Basic.lean @', ':538', 'push_gated.sh read WHOLE'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay commit 9e9327ba -- b567`s closing push output alone, in HEAD`s ancestry',
     lambda S: S['commits']['pushout'][0] == S['commits']['pushout'][1] and S['commits']['pushout'][2],
     lambda S: put(S, 'commits', dict(S['commits'], pushout=(['x'], S['commits']['pushout'][1], True)))),
    ('G-BRANCHES-DELETED', 'the four repositories` branch lists and the bank',
     lambda S: all(v == '' for v in S['push_lists'].values()) and S['branches'].count('Deleted branch push-b567') == 5,
     lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b567'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'li-weil-b561': '0000000'}))),
    ('G-OLD-LAKE-DELETED', 'the delete bank and the path`s absence', lambda S: 'files 142306' in S['oldlake'] and '-> ABSENT' in S['oldlake']
     and 'worktrees whose path lies inside D:/b567-lake-51e6992e: 0' in S['oldlake'] and not S['old_exists'],
     lambda S: put(S, 'old_exists', True)),
    ('G-WEIGHT-LINES', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('weight_line')).startswith('*Appended 2026-10-01 by b568 to b567’s entry')
     and '(R178)`(1)' in fline(S, S['fj'].get('weight_line')), lambda S: put(S, 'fj', dict(S['fj'], weight_line=1))),
    ('G-H18B-ADDENDUM', 'the addendum bank, and b567`s seal still verifying',
     lambda S: 'DECLARED READING ADDENDUM: H18b' in S['add'] and 'carried by (R178)(2)(i)' in S['add'] and 'SEAL INTACT' in S['seal567'],
     lambda S: put(S, 'seal567', '')),
    ('G-ZB-NAMES-BANKED', 'the class bank', lambda S: sum(len(v) for v in S['zbj'].get('by', {}).values()) == 146 and S['zbj'].get('unplaced') == [],
     lambda S: put(S, 'zbj', dict(S['zbj'], unplaced=['x']))),
    ('G-ZB-COUNT-ENTERED', 'OPEN_TRAILS at the banked line', lambda S: 'W-ORD-GRH-WEIL entry' in oline(S, S['tj'].get('count_line'))
     and 'strip bounds 39' in oline(S, S['tj'].get('count_line')), lambda S: put(S, 'tj', dict(S['tj'], count_line=1))),
    ('G-DICHOTOMY-PRINTED', 'Lean`s print in the bank', lambda S: 'theorem DirichletCharacter.even_or_odd' in S['dich'] and 'ψ.Even ∨ ψ.Odd' in S['dich'],
     lambda S: put(S, 'dich', S['dich'].replace('ψ.Even ∨ ψ.Odd', 'x'))),
    ('G-E0-RULE-WRITTEN', 'tools/e0_rule.py`s text and its self-test', lambda S: S['e0ok'] and '(R178)(2)(iii)' in S['e0src']
     and 'gammaBracket_chi_of_even' in S['e0src'] and 'gammaBracket_chi_of_not_even' in S['e0src'], lambda S: put(S, 'e0ok', False)),
    ('G-STANDING-A5', 'FERRY_STANDING.md', lambda S: '- **A5** No instrument edit before the seal.' in S['standing'],
     lambda S: put(S, 'standing', S['standing'].replace('**A5**', 'A5'))),
    ('G-DEFECT-LINES', 'the FINDINGS entry', lambda S: '(f) -- one `timeout` wrap' in entry(S) and '(g) -- the tag made locally' in entry(S),
     lambda S: put(S, 'find', S['find'].replace('(g) -- the tag made locally', 'x'))),
    ('G-TAG-INSTRUMENT', 'push_gated.sh and its test bank', lambda S: '18 of 18 checks as wanted -- PASS' in S['tpg'] and 'readback_equal=1' in S['pg']
     and 'tag -a' in S['pg'], lambda S: put(S, 'pg', S['pg'].replace('readback_equal=1', ''))),
    ('G-TAG-INSTRUMENT-ALONE', 'relay commit f35256d8`s files', lambda S: S['commits']['tag'][0] == S['commits']['tag'][1] and S['commits']['tag'][2],
     lambda S: put(S, 'commits', dict(S['commits'], tag=(S['commits']['tag'][0] + ['x'], S['commits']['tag'][1], True)))),
    ('G-ASOF-INSTRUMENT', 'the two-sided test bank', lambda S: '10 of 10 cases as wanted -- PASS' in S['tasof'],
     lambda S: put(S, 'tasof', '')),
    ('G-ASOF-ALONE', 'relay commit 2625d82d`s files', lambda S: S['commits']['asof'][0] == S['commits']['asof'][1] and S['commits']['asof'][2],
     lambda S: put(S, 'commits', dict(S['commits'], asof=(['x'], S['commits']['asof'][1], True)))),
    ('G-B566-RERUN-COUNTED', 'b566`s re-run bank', lambda S: 'ARMS RUN : 74.' in S['r566'] and 'THE AS-OF COMMIT : relay ce360e88' in S['r566'],
     lambda S: put(S, 'r566', '')),
    ('G-B567-RERUN-COUNTED', 'b567`s re-run bank', lambda S: 'ARMS RUN : 69. ### LIVE PASSING : 69.' in S['r567'] and 'THE AS-OF COMMIT : relay d77bb7aa' in S['r567'],
     lambda S: put(S, 'r567', '')),
    ('G-NODES-BANKED', 'the node list, read by the generator`s own reader', lambda S: len(S['nodes'][0]) == 23 and len(S['nodes'][1]) == 2,
     lambda S: put(S, 'nodes', ([], [], [], []))),
    ('G-NODE-CELLS', 'the cells json', lambda S: bool(S['cellsj'].get('order')) and all(S['cellsj']['cells'][n].get('statement') and
                                                                                          S['cellsj']['cells'][n].get('axioms') is not None for n in S['cellsj']['order']),
     lambda S: put(S, 'cellsj', dict(S['cellsj'], order=['x'], cells={'x': {}}))),
    ('G-ADDS-DROPS-PRINTED', 'the node-cells bank', lambda S: '**THE ADDITIONS : 2**' in S['celltxt'] and '**THE DROPS : 2**' in S['celltxt'],
     lambda S: put(S, 'celltxt', '')),
    ('G-H20-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('H20a', 'H20b', 'H20c', 'H20d')),
     lambda S: put(S, 'desk', '')),
    ('G-GENERATOR-TESTED', 'the generator`s commit and its test bank', lambda S: '11 of 11 cases as wanted -- PASS' in S['tgen']
     and S['commits']['gen'][0] == S['commits']['gen'][1], lambda S: put(S, 'tgen', '')),
    ('G-PAGE-TWICE', 'the two runs` bank', lambda S: '### cmp run1 run2 : BYTE-IDENTICAL' in S['runs'], lambda S: put(S, 'runs', '')),
    ('G-PAGE-FORM', 'the page`s own lines', lambda S: page_form(S), lambda S: put(S, 'page', (S['page'] or b'') + b'\nA sentence.\n')),
    ('G-LAST-LINE-CEILING', 'the page`s last derived line against README :121 at PLACE-papers HEAD', lambda S: last_line(S),
     lambda S: put(S, 'readme121', S['readme121'] + b' ')),
    ('G-PAGE-STEMS', 'the page, by banned_terms.PAT', lambda S: S['page'] is not None and S['stem_hits'] == [],
     lambda S: put(S, 'stem_hits', ['x'])),
    ('G-CHAIN-PAGE', 'a fresh regeneration against PLACE-papers HEAD`s committed page', lambda S: S['arm']['ok'] and S['page_committed'],
     lambda S: put(S, 'arm', dict(S['arm'], ok=False))),
    ('G-CHAIN-PAGE-ALONE', 'relay commit 65916c16`s files', lambda S: S['commits']['arm'][0] == S['commits']['arm'][1] and S['commits']['arm'][2],
     lambda S: put(S, 'commits', dict(S['commits'], arm=(['x'], S['commits']['arm'][1], True)))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith('## CP-4, act one: the page of the compiled chain'),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORR-ROWS', 'CORRESPONDENCE.md -- row 413 once, no grade word in it', lambda S: S['corr'].count('| 413 | **CP-4, THE PAGE WITHOUT NARRATIVE**') == 1
     and not re.search(r'\b(DERIVES|INTERFACES|SHELL|ENCODES)\b', [l for l in S['corr'].split(NL) if l.startswith('| 413 |')][0]),
     lambda S: put(S, 'corr', S['corr'].replace('| 413 | **CP-4', '| 413 | DERIVES **CP-4'))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b568 — lane three, act one under (R178)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-WORK-ORDERS-ENTERED', 'this act`s trail record', lambda S: all(re.search(r'^\| \*\*\d\*\* \| `%s` \|' % w, trail(S), re.M) for w in
                                                                       ('W-ORD-LI-THREE-WAY', 'W-ORD-KEIPER-FACE', 'W-ORD-BULKA-GENERIC'))
     and '*Filed, not started.*' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('`W-ORD-KEIPER-FACE` |', '`W-ORD-X` |'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: '**Next:** b569, GRH-Weil act four' in trail(S) and 'H21a' in trail(S) and 'H21d' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b569', '**Next:** b570'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against PLACE-papers` pre-act blob', lambda S: S['errata_pre'] is not None and S['errata_now'] == cr0(S['errata_pre']),
     lambda S: put(S, 'errata_now', S['errata_now'] + b'x')),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main against its pre-act head; SIDE-global-section`s diff; the kernel`s tags',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items() if r not in ('relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section'))
     and S['gs_diff'] in ([], ['CORRESPONDENCE.md']) and S['tags'][-1] == 'v0.10' and len(S['tags']) == 10,
     lambda S: put(S, 'tags', S['tags'] + ['v0.11'])),
    ('G-NO-ZENODO-CALL', 'this act`s tools, for the platform`s address', lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['x'])),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tools8', S['tools8'] + [os.path.join(T, 'repair_snapshot.py')])),
    ('G-NODEPOSIT', 'the deposited outputs` status', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces_pre'] is not None and S['faces_now'] == cr0(S['faces_pre']),
     lambda S: put(S, 'faces_now', S['faces_now'] + b'x')),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at d77bb7aa, by blob id (the regenerated table excepted by name)',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b567_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE]),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['ERRATA.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'].startswith(cr0(S['ot_pre'])),
     lambda S: put(S, 'ot_now', b'x' + S['ot_now'])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 8)] + [
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
                                                                          and "startswith('b568')" in S['suite'] and "data/b568_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b568')", ''))),
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
    rec('b568 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if RERUN else regenerate()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    declared = sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at d77bb7aa by blob id; changed %s' % (S['prior_n'], S['prior_bad'] or 'NONE'))
    rec('  ### G-CHAIN-PAGE: committed %d bytes, regenerated %d bytes, first differing line %s' % (S['arm']['committed_bytes'],
                                                                                              S['arm']['regenerated_bytes'], S['arm']['first_diff']))
    if not RERUN:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                              len(gen_diff.get('changed') or [])))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b568_checks_postpush.txt' if pushed else 'b568_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b568_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
