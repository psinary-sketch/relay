# -*- coding: utf-8 -*-
"""b577_checks.py -- THE SUITE OF b577, UNDER (R187): CP-7 ACT TWO, THE PURPOSE STATEMENT, THE ADDENDUM, THE ORDER.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`; it writes data/b577_checks.txt before the push and data/b577_checks_postpush.txt after
### it. ### The harness is b568's to b576's, carried; the arms are b577's.
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
FACE = os.path.join(D, 'b577_registration_2026-10-01.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='2eae0499', pp='192077f', gs='8c392fe')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}
STEPZERO, SUITEC = '9cac0572', 'cc4215d9'
RULED_LINE = 'WRITE-LIST ADDENDUM: tools/mirror_prevbuild.json, carried by (R186)(5)'
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b577')
            and 'data/b577_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    lockn = sorted(glob.glob(os.path.join(D, 'b577_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b577_') and f.endswith('.py'))
    import b577_record as REC
    import addenda as ADD
    S = dict(
        face=face, ferry=rd('b577_ferry.txt'), scan=rd('b577_ferry_scan.txt'), cens=rd('b577_census_stepzero.txt'),
        fcens=rd('b577_faces_census_stepzero.txt'), pins0=rd('b577_pins_stepzero.txt'), procs=rd('b577_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b576_closing.txt'), reads=rd('b577_reads.txt'), branches=rd('b577_branches.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        suite_c=(files_of(ROOT, SUITEC), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', SUITEC, 'HEAD']).returncode == 0),
        add_text=rd('b576_writelist_addendum.txt'), add_v=ADD.writelist_addenda(rd('b576_writelist_addendum.txt'), ADD.paste_reader(D)),
        addj=jl('b577_addendum.json'), addt=rd('b577_addendum.txt'), test=rd('b577_test_rerun.txt'), rerun=rd('b577_b576_rerun.txt'),
        wt_head=gs('D:/b577-rerun-b576', 'rev-parse', 'HEAD'),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        b576l=jl('b577_b576_lines.json'), pj=jl('b577_purpose.json'), ptxt=rd('b577_purpose.txt'), pscan=rd('b577_purpose_termscan.txt'),
        draft_b=REC._draft_b(), frags=REC.FRAGS,
        oj=jl('b577_edition_order.json'), otxt=rd('b577_edition_order.txt'), e558=jl('b558_editions.json'), formj=jl('b577_form.json'),
        census=lines_of(blob(PP, PRE['pp'] + ':phase2/method/THE_KEYSTONE_CENSUS.md')),
        fj=jl('b577_findings.json'), tj=jl('b577_trail.json'),
        sc=jl('b577_scores.json'), desk=rd('b577_desk_notes.txt'),
        pages={p: (blob(PP, 'HEAD:' + p), blob(PP, PRE['pp'] + ':' + p)) for p in (PAGE, DIR_PAGE)},
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        keystone_changes=[x for x in (gs(PP, 'diff', '--name-only', PRE['pp']) + NL + gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD')).split(NL)
                          if x.strip() and (x.startswith('phase') or x.startswith('day1/') or x.startswith('outputs/'))],
        new_pp=[l for l in gs(PP, 'diff', '--name-status', PRE['pp'], 'HEAD').split(NL) if l.startswith('A')],
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kmain=gs(KER, 'rev-parse', 'main'), kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b576*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b577_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b577_mustnotexist.txt')), table_changed=None,
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
    i = t.find('### b577 — lane three, act five under (R187)')
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


def amended(S):
    B = S['draft_b']
    want = B.replace('relay banks, the four ledgers, the terminal table', 'relay banks, the four ledgers, the two generated pages, the terminal table') \
            .replace('It is not a claim: neither is proved;', 'It is not a claim: RH reduced to a single located clause, the clause named as '
                     'h2_sign, reduction machine-verified; neither RH nor h2_sign is proved;')
    return bool(B) and S['pj'].get('text') == want and ('> ' + want) in S['find']


def order_ok(S):
    pos = {}
    for i, l in enumerate(S['census'][252:272], 253):
        m = re.match(r'^\| `([A-Za-z0-9_]+)` \|', l)
        if m:
            pos[m.group(1)] = len(pos) + 1
    rows = [(v['file'].split('/')[-1][:-4], v['rows']) for v in S['e558']['lists'].values()]
    want = [n for n, r in sorted([x for x in rows if x[0] in pos], key=lambda x: (-x[1], pos[x[0]]))]
    return want == S['oj'].get('order') and len(want) == 14


WT_HEAD = '*Appended 2026-10-01 by b577 to b576’s entry ('
OT_HEAD = '*Appended 2026-10-01 by b577 to b576’s record (:'
TITLE = '## CP-7, act two: the purpose statement appended to FINDINGS'
PHEAD = '## THE PURPOSE OF THIS RECORD — written 2026-10-01 at b577 under the author’s ruling `(R187)`(2)–(3)'
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R187) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b576`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b576' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'Nothing but reads and the step-zero banks' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b577 -- x'])),
    ('G-R187-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R187) END' in S['ferry'] and S['ot'].count('**(R187) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R187) ratified', '(R187) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in ('b576_purpose_drafts.txt @', 'README.md @', 'FINDINGS.md @',
                                                                               'THE_KEYSTONE_CENSUS.md @', 'b567_ferry.txt @', 'addenda.py @'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-PUSHOUT-COMMITTED', 'relay 9cac0572`s files', lambda S: S['pushout'][0] == ['data/b576_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b576') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b576'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'grh-weil-b573': '0000000'}))),
    ('G-ADDENDUM-WRITTEN', 'relay data/b576_writelist_addendum.txt', lambda S: S['add_text'].strip() == RULED_LINE,
     lambda S: put(S, 'add_text', S['add_text'].replace('(R186)(5)', '(R187)(4)'))),
    ('G-ADDENDUM-VERDICT', 'the form run afresh on the line, against the bank', lambda S: len(S['add_v']) == 1
     and S['add_v'][0]['accepted'] is S['addj'].get('accepted') and S['add_v'][0]['why'] in S['addt'],
     lambda S: put(S, 'addj', dict(S['addj'], accepted=True))),
    ('G-SUITE-EDIT-ALONE', 'relay cc4215d9`s files and the test bank', lambda S: S['suite_c'][0] == ['data/b577_test_rerun.txt', 'tools/b576_checks.py',
                                                                                                    'tools/b577_test_rerun.py'] and S['suite_c'][1]
     and '5 of 5 cases as wanted -- PASS' in S['test'], lambda S: put(S, 'test', S['test'].replace('5 of 5', '4 of 5'))),
    ('G-RERUN-BANKED', 'the re-run bank', lambda S: 'b576 -- THE SUITE. ### **POST-PUSH READING.**' in S['rerun']
     and re.search(r'ARMS RUN : 69\. ### LIVE PASSING : (\d+)\.', S['rerun']) is not None and 'WRITE-LIST ADDENDUM ((R177)(3)(g))' in S['rerun'],
     lambda S: put(S, 'rerun', S['rerun'].replace('ARMS RUN : 69', 'ARMS RUN : 6'))),
    ('G-RERUN-AT-B576', 'the worktree`s HEAD and the addendum bank`s record of it', lambda S: S['wt_head'].startswith('2eae0499')
     and S['addj'].get('worktree_head', '').startswith('2eae0499'), lambda S: put(S, 'wt_head', '5ccf4707')),
    ('G-BUILDER-WRITELIST-LINE', 'OPEN_TRAILS at b576`s record', lambda S: any('THE MIRROR BUILDER’S WRITE LIST' in oline(S, n) and 'tools/mirror_prevbuild.json' in oline(S, n)
                                                                              for n in S['b576l'].get('ot_lines', [])),
     lambda S: put(S, 'b576l', dict(S['b576l'], ot_lines=[1]))),
    ('G-CORRECTION-LINES', 'OPEN_TRAILS at b576`s record', lambda S: sum(1 for n in S['b576l'].get('ot_lines', []) if oline(S, n).startswith(OT_HEAD)
                                                                        and 'THE NAVIGATOR’S CORRECTION' in oline(S, n)) == 4,
     lambda S: put(S, 'b576l', dict(S['b576l'], ot_lines=S['b576l'].get('ot_lines', [])[:3]))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['b576l'].get('weight')).startswith(WT_HEAD)
     and 'b576 AT ITS WEIGHT' in fline(S, S['b576l'].get('weight')), lambda S: put(S, 'b576l', dict(S['b576l'], weight=1))),
    ('G-PURPOSE-TEXT', 'the block`s text against Draft B with the two ruled amendments', lambda S: amended(S),
     lambda S: put(S, 'pj', dict(S['pj'], text=(S['pj'].get('text') or '') + 'x'))),
    ('G-PURPOSE-SOURCES', 'the purpose bank', lambda S: len(S['frags']) == 4 and all(f in S['ptxt'] for f, _ in S['frags'])
     and 'equals Draft B with exactly the two ruled amendments: True' in S['ptxt'], lambda S: put(S, 'ptxt', S['ptxt'].replace(': True ;', ': False ;'))),
    ('G-PURPOSE-BLOCK', 'FINDINGS at the block', lambda S: fline(S, S['pj'].get('heading_line')) == PHEAD
     and fline(S, S['pj'].get('supersedes_line')) == 'SUPERSEDES FINDINGS :7 for the purpose statement: present, at :%d' % S['pj'].get('heading_line'),
     lambda S: put(S, 'pj', dict(S['pj'], supersedes_line=1))),
    ('G-PURPOSE-SCAN', 'the banned-stem scan of the block', lambda S: re.search(r'^\s*VERDICT\s*: CLEAN', S['pscan'], re.M) is not None,
     lambda S: put(S, 'pscan', S['pscan'].replace('CLEAN', 'HITS'))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-ORDER-BANKED', 'the order bank', lambda S: '### ### **THE HEAD OF THE ORDER: PATHS_TO_THE_CRITICAL_LINE (29 rows).' in S['otxt']
     and S['oj'].get('head') == 'PATHS_TO_THE_CRITICAL_LINE', lambda S: put(S, 'oj', dict(S['oj'], head='ENUMERA'))),
    ('G-ORDER-COUNTS', 'the order json against b558_editions.json', lambda S: all(
        any(v['file'].endswith('/' + r['name'] + '.txt') and v['rows'] == r['moved'] and v['lines'] == r['lines'] for v in S['e558']['lists'].values())
        for r in S['oj'].get('rows', [])) and len(S['oj'].get('rows', [])) == 14,
     lambda S: put(S, 'oj', dict(S['oj'], rows=[dict(r, moved=r['moved'] + 1) for r in S['oj'].get('rows', [])]))),
    ('G-ORDER-TIES', 'the order recomputed from the census and b558_editions.json', lambda S: order_ok(S),
     lambda S: put(S, 'oj', dict(S['oj'], order=list(reversed(S['oj'].get('order', [])))))),
    ('G-EXCLUDED-LISTED', 'the order json and bank', lambda S: sorted(r['name'] for r in S['oj'].get('outside', [])) ==
     ['A_Place_to_Stand', 'BALANCE_AND_POSITIVITY', 'FACES_OF_H2_AT_FINITE_INSTANCE'] and 'OUTSIDE THE KEYSTONE CLASS' in S['otxt'],
     lambda S: put(S, 'oj', dict(S['oj'], outside=[]))),
    ('G-FORM-ENTERED', 'OPEN_TRAILS at the banked form line', lambda S: oline(S, S['formj'].get('line')).startswith('*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6)')
     and 'THE FORM OF AN EDITION, STANDING FOR CP-7' in oline(S, S['formj'].get('line')), lambda S: put(S, 'formj', dict(S['formj'], line=1))),
    ('G-EDITION-WITHDRAWN', 'PLACE-papers` diff, this act`s banks and the trail record', lambda S: S['new_pp'] == []
     and not glob.glob(os.path.join(D, 'b577_edition_*.txt')).__contains__(os.path.join(D, 'b577_edition_PATHS_TO_THE_CRITICAL_LINE.txt'))
     and 'the navigator’s Component 4 (the edition begun at b577), withdrawn' in trail(S),
     lambda S: put(S, 'new_pp', ['A\tphase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v2.md'])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: fline(S, S['fj'].get('entry_line')).startswith(TITLE),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')).startswith('### b577 — lane three, act five under (R187)'),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'CP-7 act three, b578' in trail(S) and 'PATHS_TO_THE_CRITICAL_LINE' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('CP-7 act three, b578', 'x'))),
    ('G-CONFLICT-RECORDED', 'this act`s trail record', lambda S: '**Struck and withdrawn, recorded:**' in trail(S) and 'would have moved every later line by' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Struck and withdrawn, recorded:**', 'x'))),
    ('G-PAGES-UNCHANGED', 'both pages at PLACE-papers HEAD against their pre-act blobs', lambda S: all(h is not None and h == p for h, p in S['pages'].values()),
     lambda S: put(S, 'pages', dict(S['pages'], **{PAGE: ((S['pages'][PAGE][0] or b'') + b'x', S['pages'][PAGE][1])}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, SIDE-global-section`s diff', lambda S: S['kmain'] == V015
     and S['kcur'] == 'main' and S['kdirty'] == '' and all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['gs_diff'] == [],
     lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b577_record.py'): S['tooltext'].get(os.path.join(T, 'b577_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: not [f for f, t in S['tooltext'].items()
                                                                        if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-UNTOUCHED', 'PLACE-papers` phase, day1 and outputs paths', lambda S: S['keystone_changes'] == [],
     lambda S: put(S, 'keystone_changes', ['phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md'])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 2eae0499, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b576_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files', lambda S: S['pp_changed'] == ['FINDINGS.md', 'OPEN_TRAILS.md'],
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 5)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b577')" in S['suite'] and "data/b577_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b577')", ''))),
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
    rec('b577 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
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
    out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b577_checks_postpush.txt' if pushed else 'b577_checks.txt'))
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    if not RERUN:
        io.open(os.path.join(D, 'b577_exercise.json'), 'w', encoding='utf-8', newline=NL).write(
            json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
