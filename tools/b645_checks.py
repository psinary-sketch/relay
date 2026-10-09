# -*- coding: utf-8 -*-
"""b645_checks.py -- THE SUITE OF b645, UNDER (R255): THE REVIEW PASS OPENED -- THE LICENSED-STATEMENT TABLE BUILT AND TESTED; THE SEAM
ROWS, THE LOAD-BEARING MAP, SIDE-EXPLICIT-FORMULA'S DOCSTRINGS AT v0.26 AND THE MONOGRAPH'S CLAIMS EACH TO ONE VERDICT; THE CENSUS'S
CLUSTER, PHASE AND MATURITY COLUMNS DEFINED; NO EDITION RE-CUT; THE DEPOSIT HELD.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### The face is sealed AFTER Components 0-6; every commit whose subject opens `b645` and none of POST_SEAL's prefixes precedes the lock.
### ### G-ACTROOT-VERIFY reads the chain at commit (tools/act_root.py, b644's repair): b624 to b645 AGREE, b645's crlf count 0.
### ### The harness is b568's to b644's (helpers, runner, seal), carried from tools/b644_checks.py; the sources, predicates and arms are b645's.
"""
import copy
import fnmatch
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b616_claims as KC0     # noqa: E402
import b645_worklist as K     # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b645_registration_2026-10-09.txt')
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = K.STEPZERO
INSTRUMENT_COMMIT = 'd2ef07c2'    # ### relay: the instrument and its planted test, committed alone before any real row
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
# ### the instruments b645 does not edit, against relay bd1387be: b644's tools, the shared tools, the generators and the intake form
INST = ('b644_checks.py', 'b644_closing.py', 'b644_tests.py', 'b644_worklist.py', 'b644_reg_gate.py', 'b644_regspec.py', 'b644_record.py',
        'b628_record.py', 'b628_worklist.py', 'b643_record.py', 'b633_record.py', 'b602_record.py', 'b641_record.py', 'act_root.py', 'additive_shared.py',
        'build_watch.py', 'premise_status.py', 'e0_rule.py', 'terminal_table.py', 'chain_page.py', 'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py',
        'push_gated.sh', 'mirror_build.ps1', 'mirror_verify.py', 'b616_claims.py', 'ferry_scan.py', 'test_act_root_commit_b644.py',
        'test_additive_shared_b644.py', 'test_build_watch_b644.py')
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'README.md', 'REGISTRY.md', K.MAP, K.MONO, K.CEN71, K.PAGE, K.DIR_PAGE, K.TAXONOMY)
TABLE_FILES = K.TABLE_FILES


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    if 'ls-remote' in a:
        KC0.LSR[repo] = KC0.LSR.get(repo, 0) + 1
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
    return None if b is None else b.replace(b'\r\n', b'\n')


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
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def utc_epoch(text, label):
    m = re.search(re.escape(label) + r'[^0-9]*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', text)
    return iso_epoch(m.group(1)) if m else None


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b645')
            and 'data/b645_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers)/[^`\s]+)`', w)))


def written_files():
    res = []
    for repo, name, pre in ((ROOT, 'relay', PRE['relay']), (PP, 'PLACE-papers', PRE['pp'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def tri(repo, path, pre):
    return (cr0(raw(os.path.join(repo, *path.split('/')))), cr0(blob(repo, '%s:%s' % (pre, path))), cr0(blob(repo, 'HEAD:' + path)))


def kern_now(face):
    out = {}
    for k in face:
        p = 'D:/' + k
        tags = {}
        for l in gs(p, 'for-each-ref', '--format=%(refname:short) %(objectname) %(*objectname)', 'refs/tags').split(NL):
            if l.strip():
                x = l.split()
                tags[x[0]] = (x[2] if len(x) > 2 else x[1])[:7]
        out[k] = [gs(p, 'rev-parse', '--short=7', 'main'), tags, sorted(x for x in gs(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()),
                  gs(p, 'status', '--porcelain', '--untracked-files=no')]
    return out


def sealed_now():
    out = {}
    for t in K.SEALED:
        b = raw(os.path.join(T, t))
        out[t] = hashlib.sha256(b).hexdigest() if b is not None else None
    return out


def appended(pre, now):
    return now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else ''


def sources():
    import b645_record as REC
    import b616_record as R6
    import licensed_table as LT
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b645_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b645_') and f.endswith('.py')) or f in ('licensed_table.py',))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    t0 = subprocess.run([sys.executable, os.path.join(T, 'test_licensed_table_b645.py')], capture_output=True, text=True, encoding='utf-8',
                        errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    S = dict(
        REC=REC, LT=LT, face=face, ferry=rd('b645_ferry.txt'), scan=rd('b645_ferry_scan.txt'), procs=rd('b645_procs.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b644_closing.txt'), reads=rd('b645_reads.txt'), answers=rd('b645_author_answers.txt'), prerun=rd('b645_arms_prerun.txt'),
        rl=jl('b645_record_lines.json'), tests=jl('b645_tests_stepzero.json'), testst=rd('b645_tests_stepzero.txt'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', 'HEAD', 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b645_seal_hashes.json'), sealnow=sealed_now(), bw=jl('b645_build_watch.json'),
        hold=jl('b645_hold_retry.json'), holdp=jl('b645_hold_preseal.json'),
        inst_test=(t0.returncode, t0.stdout), inst_bank=rd('b645_instrument.txt'), files_inst=files_of(ROOT, INSTRUMENT_COMMIT),
        sm=jl('b645_table_seam_map.json'), smt=rd('b645_table_seam_map.txt'), dj=jl('b645_table_docstrings.json'),
        mj=jl('b645_table_monograph.json'), mjt=rd('b645_table_monograph.txt'), cj=jl('b645_census_columns.json'),
        agenda=rd('b645_v6_agenda.txt'), outs=jl('b645_outsider_roster.json'),
        map_rows=REC._map_rows(), mono=(cr0(blob(PP, '%s:%s' % (PRE['pp'], K.MONO))) or b'').decode('utf-8', 'replace'),
        closing_src=read(os.path.join(T, 'b645_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b645_act_root.json'), arj0=jl('b644_act_root.json'), art=rd('b645_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b645_kernels_face.json').get('kernels') or {}),
        push_lists={r: gs(r, 'branch', '--list', 'push-b644*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b645_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b645_mustnotexist.txt')), table_changed=None,
        fj=jl('b645_findings.json'), tj=jl('b645_trail.json'), sc=jl('b645_scores.json'), desk=rd('b645_desk_notes.txt'), tfj=jl('b645_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files()
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    S['pp_changed'] = sorted(ch)
    S['ledger_adds'] = appended(S['fi_pre'], S['fi_now']) + NL + appended(S['ot_pre'], S['ot_now'])
    pub = [S['ledger_adds']]
    for f in sorted(os.listdir(D)):
        if f.startswith(('b645_', 'audit_b645_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    import b641_record as R41
    S['outside'] = [n for n in R41.OAI_NEEDLES if n in S['ledger_adds']]
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES or p == 'data/act_roots.txt':
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S['bank_mtimes'] = {}
    for it in (S['arj'].get('items') or []):
        p = it.split()[0]
        if p.startswith('data/') and os.path.exists(os.path.join(ROOT, *p.split('/'))):
            S['bank_mtimes'][p] = os.path.getmtime(os.path.join(ROOT, *p.split('/')))
    import act_root as AR
    import additive_shared as ADD
    try:
        S['ar_verify'] = AR.verify(remote=KC0.remote_refs)
        S['ar_reads'] = dict(AR.READS_AT)
    except Exception as e:
        S['ar_verify'], S['ar_reads'] = [('raised', type(e).__name__, [])], {}
    S['order_slack'] = AR.ORDER_SLACK
    try:
        S['additive'] = ADD.check(worktree=True)
    except Exception as e:
        S['additive'] = [('raised', type(e).__name__, [('x', [])])]
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


def poss(t):
    import b566_record as R6
    return R6.Q.poss(t)


def rline(S, i, key='rl'):
    x = (S[key].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need, key='rl'):
    x = rline(S, i, key)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


def procs_ok(S):
    p = S['procs']
    return '### NONE: no tail, lean, lake or python process is running' in p and '### orphans: NONE' in p and '### free memory: ' in p


def tests_ok(S):
    """every test file tracked at HEAD run: in the runner bank clean but test_chain_page_b638.py (4)-(7), or recorded RUN-BENEATH-HOLD."""
    j = S['tests']
    names = [n for n in S['tracked_tests'] if n != 'test_licensed_table_b645.py']   # ### written after step zero, run live by G-INSTRUMENT-TESTS
    rbh = sorted(set(str(r['cmd'][-1]) for r in (S['bw'].get('rows') or []) if r.get('cmd') and str(r['cmd'][-1]).startswith('test_')))
    nf = sorted(n for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(set(j) | set(rbh)) == names and nf == ['test_chain_page_b638.py'] \
        and j['test_chain_page_b638.py']['failing'] == ['(4)', '(5)', '(6)', '(7)'] \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 1' % (len(names), len(names) - len(rbh))) in S['testst']


def hold_ok(S):
    rows = S['hold'].get('rows') or []
    rbh = sorted(r['target'] for r in rows if r['verdict'] == 'RUN-BENEATH-HOLD')
    built = sorted(r['target'] for r in rows if r['verdict'] == 'BUILT')
    pre = S['holdp']
    return len(rows) == 7 and rbh == ['RestrictedTensorLayer1', K.HOLD_TEST] and len(built) == 5 \
        and sorted(pre.get('final') or []) == ['RestrictedTensorLayer1', K.HOLD_TEST]


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b645 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    res = re.findall(r'^RESULT \(transcript line \d+\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) >= 3 and all(x >= 2 for x in per) and len(res) >= 2 \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and '(Hold)' in a


READ_NEEDLES = ('data/b644_closing.txt @ bd1387be', 'data/b644_defects.txt @ bd1387be', 'phase1.5/method/THE_LOAD_BEARING_MAP.md @ 6871ba21',
                'FINDINGS.md @ 6871ba21', 'SIDEExplicitFormula/Seam.lean @ 82550e4', 'tools/b628_record.py @ bd1387be', 'data/b643_rerun.txt',
                'data/b644_census_roster.txt', 'THE_DOCUMENT_CLASS_TAXONOMY.md', 'A_Place_to_Stand_v5_18.md', ':13599 ',
                'data/b644_closing_push_out.txt @ 32d4fecd', '### the local intake bank tracked by git: NO -- untracked')


def instrument_ok(S):
    rc, out = S['inst_test']
    m = re.search(r'\*\*(\d+) of (\d+) cases as wanted -- PASS\*\*', out)
    return rc == 0 and bool(m) and m.group(1) == m.group(2) and int(m.group(1)) >= 9 \
        and S['files_inst'] == ['data/b645_instrument.txt', 'tools/licensed_table.py', 'tools/test_licensed_table_b645.py'] \
        and re.search(r'^  \(5\) a HAND row without its citation is refused.*PASS$', out, re.M) is not None


def hand_refused(S):
    LT = S['LT']
    r = dict(id='x', source='a/b.md:1', stated='s', licensed='l', by='HAND', cited=[], verdict='MATCHES', action='none')
    good = dict(r, cited=['a/b.md:1'])
    return bool(LT.check(r)) and LT.check(good) == [] and LT.table([r])[0] is None


def _commit_time(S, sha):
    for h, s, t in S['rlog']:
        if sha.startswith(h) or h.startswith(sha[:7]):
            return t
    return None


def first_bank_commit(S, path):
    hs = [l.split()[0] for l in gs(ROOT, 'log', '--reverse', '--format=%h %ct', PRE['relay'] + '..HEAD', '--', path).split(NL) if l.strip()]
    return _commit_time(S, hs[0]) if hs else None


def instrument_before_rows(S):
    ti = _commit_time(S, INSTRUMENT_COMMIT)
    tb = [first_bank_commit(S, 'data/b645_table_%s.txt' % n) for n in ('seam_map', 'docstrings', 'monograph')]
    return ti is not None and all(t is not None and ti < t for t in tb)


def seam_ok(S):
    LT = S['LT']
    s = S['sm'].get('seam') or []
    return len(s) == 2 and sorted(r['source'] for r in s) == ['FINDINGS.md:7595', 'OPEN_TRAILS.md:13033'] \
        and all(r['verdict'] in ('UNDERSTATES', 'OVERREACHES') and r['action'].startswith('RE-CUT: ') and LT.check(r) == [] for r in s) \
        and all('rh_strip_imp_rh_holds' in r['licensed'] for r in s)


def map_ok(S):
    LT = S['LT']
    m = S['sm'].get('map') or []
    lines = sorted(r['line'] for r in m)
    cnt, faults = LT.table(m)
    tot, _f = LT.table(m + (S['sm'].get('seam') or []))
    return bool(m) and lines == sorted(i for i, _k, _s, _l in S['map_rows']) and not faults and tot is not None \
        and dict(tot) == dict(S['sm'].get('counts') or {})


def doc_ok(S):
    LT = S['LT']
    rows = S['dj'].get('rows') or []
    cnt, faults = LT.table(rows)
    return len(rows) > 1000 and not faults and dict(cnt) == dict(S['dj'].get('counts') or {}) and not [r for r in rows if r.get('hand_needed')]


def doc_control(S):
    return bool((S['dj'].get('control') or {}).get('hand'))


def doc_beyond(S):
    return bool([r for r in S['dj'].get('rows') or [] if r['verdict'] in ('UNDERSTATES', 'OVERREACHES') and 'PlateauRamp' not in r['id']])


def mono_ok(S):
    LT = S['LT']
    rows, skips = S['mj'].get('rows') or [], S['mj'].get('skips') or []
    ls = S['mono'].split(NL)
    cov = set(r['line'] for r in rows) | set(s['line'] for s in skips)
    need = set(i for i, l in enumerate(ls, 1) if l.strip())
    cnt, faults = LT.table(rows)
    return bool(rows) and need <= cov and not faults and all(r['stated'] in ls[r['line'] - 1] for r in rows)


def mono_read(S):
    rd_ = S['mj'].get('read') or {}
    return bool(rd_) and all(r['id'] in rd_ for r in S['mj'].get('rows') or [] if r['verdict'] != 'MATCHES') \
        and sum(1 for v in rd_.values() if v.startswith('SAMPLE')) == 40


def agenda_ok(S):
    c = S['mj'].get('counts') or {}
    m = re.search(r'\*\*ROWS (\d+) ; CHAPTERS (\d+)\.\*\*', S['agenda'])
    return bool(m) and int(m.group(1)) == c.get('OVERREACHES', -1) + c.get('UNLICENSED', -1)


def columns_ok(S):
    rows = S['cj'].get('rows') or []
    LT = S['LT']
    mat = [r for r in rows if r.get('maturity')]
    return len(rows) == 49 and sorted(r['id'] for r in mat) == ['SIDE-explicit-formula v0.26 = 82550e4', 'd1-1'] \
        and all(r['maturity'] in LT.MATURITY for r in mat) and all(r['why'] == 'NOT YET IN THE TABLE' for r in rows if not r.get('maturity')) \
        and all(r['cluster'] in LT.CLUSTERS for r in rows) and all(r['phase'] in ('1', '1.5', '2', '-') for r in rows)


def outsiders_ok(S):
    rows = S['outs'].get('rows') or []
    return len(rows) == 25 and all(r['word'] in ('JOINS', 'RETIRES', 'STANDS ASIDE') and r['why'] for r in rows)


def instruments_ok(S):
    for f, (pre, now, head) in S['inst'].items():
        if pre is None or pre != now or pre != head:
            return False
    return True


def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b645 seal', 'b645 pre-root', 'b645 root', 'b645 record', 'b645 --', 'b645 closing')


def _component_commit(s):
    return s.startswith('b645') and not s.startswith(POST_SEAL)


def sealed_after_ok(S):
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def table_final_ok(S):
    t = S['tfj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('added') and not t.get('grade_moved') and not t.get('moved')


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 22 and rows[21][:3] == ['b645', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it] \
        and any(it.startswith('data/b645_table_monograph.txt ') for it in j.get('items') or []) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b645_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b645') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 646)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The instrument**', '**The seam rows**', '**The load-bearing map**', '**The docstrings**', '**The monograph**',
                 '**The three columns**', '**The record lines**', '**The outsiders**', '**The root.**', '**The scores.**', '**Read in mutual light**',
                 'strengthens', '**Next.**', 'b646', 'b647')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') == S['REC']._title() and all(x in tail for x in ENTRY_NEEDLES)


def trail_tail(S):
    t = S['ot']
    i = t.find(S['REC'].TRAIL_HEAD())
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0].split(',')[0].split(' ')[0] in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k) in S['desk']


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def route_held(S):
    pub = ['actions' + '/publish', 'z_' + 'publish', 'zenodo' + '.org/api']
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if any(p in t for p in pub)]


def kernels_untouched(S):
    import b641_record as R41
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and sorted(f) == sorted(R41.KERNS_READ) and all(k in n and n[k] == f[k] for k in f)


def corpus_scope(S):
    return S['pp_changed'] == ['FINDINGS.md', 'OPEN_TRAILS.md']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author in any ' + 'outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and (', no ' + 'outbound request,') not in t


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def prompts_banked(S):
    return len(re.findall(r'^### PROMPT ', S['answers'], re.M))


def _rl(S, i, line, key='rl'):
    ls = list(S[key].get('lines') or [])
    ls[i:i + 1] = [dict(rline(S, i, key), line=line)]
    return put(S, key, dict(S[key], lines=ls))


def _mut_rows(S, key, sub, f):
    d = copy.deepcopy(S[key])
    f(d[sub] if sub else d)
    return put(S, key, d)


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R255) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-PROCS', 'the process listing: none running, no orphan', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'].replace('### orphans: NONE', '### orphans: 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank and the watchdog`s bank against the test files tracked at HEAD: every one clean but '
     'test_chain_page_b638.py (4)-(7), or run beneath the hold and recorded', lambda S: tests_ok(S),
     lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b644_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay and PLACE-papers branch lists', lambda S: all(v == '' for v in S['push_lists'].values()),
     lambda S: put(S, 'push_lists', {'D:/relay': 'push-b644'})),
    ('G-HOLD-RETRIED', 'the hold banks: five built, two beneath the hold at step zero and again before the seal', lambda S: hold_ok(S),
     lambda S: put(S, 'holdp', {'final': ['RestrictedTensorLayer1']})),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompts, every call`s result', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('(Hold)', '(Hld)'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'] and 'NO SUCH BLOB' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'].replace(':13599 ', ':13598 '))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line', lambda S: landed(S, 0, ['b644 AT ITS WEIGHT', 'relay bd1387be (closing)', '(a) to (r)']),
     lambda S: _rl(S, 0, 1)),
    ('G-WRITING-LAW-LINE', 'OPEN_TRAILS at the record-lines bank`s line', lambda S: landed(S, 1, ['PAPERS STATE; LEDGERS NARRATE', 'No edition is re-cut at b645',
                                                                                             'v6.0, not v5.19', '(:11864)']),
     lambda S: _rl(S, 1, 1)),
    ('G-FOOTPRINT-LINE', 'OPEN_TRAILS at the record-lines bank`s line', lambda S: landed(S, 2, ['W-ORD-HOLD-FOOTPRINT', 'Priced: one act']),
     lambda S: _rl(S, 2, 1)),
    ('G-INSTRUMENT-TESTS', 'tools/test_licensed_table_b645.py run live, and the instrument`s first commit alone', lambda S: instrument_ok(S),
     lambda S: put(S, 'files_inst', S['files_inst'] + ['data/b645_table_seam_map.txt'])),
    ('G-HAND-UNCITED-REFUSED', 'tools/licensed_table.py`s check and table on a planted HAND row without its citation', lambda S: hand_refused(S),
     lambda S: put(S, 'LT', type('LTX', (), dict(check=staticmethod(lambda r: []), table=staticmethod(lambda rs: ({}, {}))))())),
    ('G-INSTRUMENT-BEFORE-ROWS', 'the commit times: the instrument before the first bank of each table', lambda S: instrument_before_rows(S),
     lambda S: put(S, 'rlog', [(h, s, (10 ** 10 if h.startswith(INSTRUMENT_COMMIT[:7]) else t)) for h, s, t in S['rlog']])),
    ('G-SEAM-ROWS', 'the seam table: two rows, each UNDERSTATES or OVERREACHES with its re-cut, taken by the instrument', lambda S: seam_ok(S),
     lambda S: _mut_rows(S, 'sm', 'seam', lambda rs: rs[0].update(verdict='MATCHES'))),
    ('G-MAP-EVERY-ROW', 'the map table against the map`s rows re-parsed at PLACE-papers before the act', lambda S: map_ok(S),
     lambda S: _mut_rows(S, 'sm', 'map', lambda rs: rs.pop())),
    ('G-DOCSTRINGS-EVERY-ROW', 'the docstring table: every row one verdict, the instrument taking it, no flagged row left generated', lambda S: doc_ok(S),
     lambda S: _mut_rows(S, 'dj', 'rows', lambda rs: rs[0].update(verdict='SOMETIMES'))),
    ('G-DOC-CONTROL-FLAGGED', 'the docstring table`s positive control (PlateauRamp`s header at v0.25)', lambda S: doc_control(S),
     lambda S: put(S, 'dj', dict(S['dj'], control={'verdict': 'MATCHES', 'hand': None}))),
    ('G-DOC-BEYOND-PLATEAURAMP', 'the docstring table`s UNDERSTATES and OVERREACHES rows beside PlateauRamp`s', lambda S: doc_beyond(S),
     lambda S: _mut_rows(S, 'dj', 'rows', lambda rs: [r.update(verdict='MATCHES') for r in rs])),
    ('G-MONO-EVERY-LINE', 'the monograph table against the monograph at PLACE-papers before the act: every non-blank line a claim or a skip, '
     'every quote on its line', lambda S: mono_ok(S), lambda S: _mut_rows(S, 'mj', 'skips', lambda rs: rs.clear())),
    ('G-MONO-READ', 'the monograph table`s read record: every non-MATCHES row read, forty sampled', lambda S: mono_read(S),
     lambda S: put(S, 'mj', dict(S['mj'], read={}))),
    ('G-V6-AGENDA', 'the agenda`s row count against the monograph table`s OVERREACHES and UNLICENSED', lambda S: agenda_ok(S),
     lambda S: put(S, 'agenda', S['agenda'].replace('**ROWS ', '**ROWS 9'))),
    ('G-COLUMNS-BANKED', 'the columns bank: 49 rows, maturity for the monograph and the kernel alone, the rest blank and marked', lambda S: columns_ok(S),
     lambda S: _mut_rows(S, 'cj', 'rows', lambda rs: rs[5].update(maturity='SETTLED'))),
    ('G-OUTSIDERS-READ', 'the outsider roster: 25 rows, each a word and its printed reading', lambda S: outsiders_ok(S),
     lambda S: _mut_rows(S, 'outs', 'rows', lambda rs: rs[0].update(word='WELCOMED'))),
    ('G-NO-EDITION', 'PLACE-papers` changed files against FINDINGS and OPEN_TRAILS', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + [K.MONO])),
    ('G-CURRENTS-UNEDITED', 'the current documents, the map, the monograph, the census and the pages: working tree, before and HEAD', lambda S: unedited_all(S),
     lambda S: put(S, 'currents', dict(S['currents'], **{K.MAP: (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal', lambda S: kernels_untouched(S),
     lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b644`s tools, the shared tools and the intake form: before, working tree and HEAD', lambda S: instruments_ok(S),
     lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at bd1387be, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 0,
     lambda S: put(S, 'prior_bad', ['data/b644_closing.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes', lambda S: not any(S['nd_pub'].values()),
     lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-ROUTE-UNCALLED', 'the act`s tools` code: no deposit route', lambda S: route_held(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b645 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b645_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b644`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b644 closed' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-R255-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R255) END' in S['ferry'] and S['ot'].count('**(R255) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R255) ratified', '**(R2550) ratified'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 22nd line, the root bank and its items', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b646 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b645 AGREE, b645 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line', lambda S: bool(S['tj'].get('line')) and oline(S, S['tj']['line']) == S['REC'].TRAIL_HEAD(),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b645 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b645_record.py agree', 'b645_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line', lambda S: '**Next:** per `(R255)`(8) and the author’s answer, b646' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** per `(R255)`(8)', '**Next:** per `(R2550)`(8)'))),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b645')" in S['suite'] and "'data/b645_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b645_closing.py: the closing sentence in the rule`s words with the plain reads named', lambda S: closing_sentence_ok(S),
     lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author in any ' + 'outbound request', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, read after every other arm has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
]


def regenerate():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def seal():
    """### (R246)(3): the sha256 of every sealed tool, recorded at the seal; refuses before the face is locked or once recorded."""
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b645_seal_hashes.json')
    if lock is None:
        print('### THE FACE IS NOT LOCKED -- NOTHING RECORDED')
        return 3
    if os.path.exists(p):
        print('### THE HASHES ARE RECORDED ALREADY -- NOTHING RECORDED TWICE')
        return 3
    now = sealed_now()
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), lock=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock)), tools=now,
             relay_head=gs(ROOT, 'rev-parse', 'HEAD'))
    b = (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    for t in K.SEALED:
        print('  %-24s %s' % (t, now[t]))
    print('  written: b645_seal_hashes.json')
    return 0


def main():
    if SEAL:
        return seal()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b645 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources()
    S['pushed'] = pushed
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID) else regenerate()
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    av = S['ar_verify']
    rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    rec('  %-46s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 98)
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
        rec('  %-46s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else 'FAIL', 'PASS' if posv else 'FAIL',
                                           'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else '### FAILS')))
    rec('')
    rec('  ### tracked files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                          if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this run, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if not (RERUN or PRERUN or MID):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), (gen_diff.get('changed') or '')[:20]))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b645_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b645_checks_postpush.txt' if pushed else 'b645_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b645_arms_prerun.txt', 'b645_lsr_prerun.json').replace('b645_checks', 'b645_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b645_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
