# -*- coding: utf-8 -*-
"""b647_checks.py -- THE SUITE OF b647, UNDER (R257): EVERY KERNEL'S DOCSTRINGS THROUGH THE LICENSED-STATEMENT TABLE; THE NAVIGATOR'S
MEMORY THROUGH THE TABLE; THE DESCRIPTION AT v4 WITH ITS GLOSSARY ENTRIES, A FIFTH READER, THE DRAFT HELD; THE WATCHDOG ON THE PROCESS TREE;
THE CENSUS COLUMNS EXTENDED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### The face is sealed AFTER Components 0-5; every commit whose subject opens `b647` and none of POST_SEAL's prefixes precedes the lock.
### ### G-ACTROOT-VERIFY reads the chain at commit (tools/act_root.py): b624 to b647 AGREE, b647's crlf count 0.
### ### G-EDIT-ROUTE reads the act's command capture LIVE -- the seat's session from the ruling's delivery and its helper readers' -- through
### ### tools/edit_route.py.
### ### The harness is b568's to b646's (helpers, runner, seal), written by the Write tool from tools/b646_checks.py; the sources, predicates and
### ### arms are b647's.
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
import b647_worklist as K     # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b647_registration_2026-10-10.txt')
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = K.STEPZERO
WATCH_COMMIT = K.WATCH_COMMIT       # ### relay: the watchdog's tree sampling and its planted test, committed alone at step zero
BRIEF_COMMIT = '41d7f3ae'           # ### relay: the helper readers' brief, banked before any row is read
SORRY_COMMIT = '49d01585'           # ### relay: the sorry census, before any further row (the author's answer, (ii))
ANSWERS_COMMIT = 'a66c50a1'         # ### relay: the author's answer and the brief's addendum
KBANKS_COMMIT = '7ece93aa'          # ### relay: every kernel's banks, first written
NAVRULE_COMMIT = '4b9d8e0e'         # ### relay: the navigator rule, printed before any unit is read
NAVTABLE_COMMIT = '1dc426e5'        # ### relay: the navigator table
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
# ### the instruments b647 does not edit, against relay 48ed6db2: b646's tools, the instrument, the intake form, the composer b646 sealed,
# ### the arm and the shared tools
INST = ('b646_checks.py', 'b646_closing.py', 'b646_tests.py', 'b646_worklist.py', 'b646_reg_gate.py', 'b646_regspec.py', 'b646_record.py',
        'b645_record.py', 'licensed_table.py', 'test_licensed_table_b645.py', 'b628_record.py', 'b628_worklist.py', 'b644_record.py',
        'b643_record.py', 'b638_record.py', 'b633_record.py', 'b602_record.py', 'b641_record.py', 'b639_record.py', 'b616_record.py', 'act_root.py',
        'additive_shared.py', 'premise_status.py', 'terminal_table.py', 'chain_page.py', 'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py',
        'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py', 'b616_claims.py', 'ferry_scan.py', 'edit_route.py',
        'test_edit_route_b646.py', 'e0_rule.py', 'test_composer_b646.py', 'test_build_watch_b644.py')
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'README.md', 'REGISTRY.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md', 'day1/A_Place_to_Stand_v5_18.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
            'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 'day1/Exhaustive_Enumeration.md', 'day1/Which_Structure_Confines.md',
            'day1/Spectral_Inertness.md', 'day1/Seven_Mechanism_Classes.md', 'day1/Third_Identity_Element.md', 'day1/Silence_of_Foundations.md',
            'day1/ONE_PAGE_PROOF.md')
TABLE_FILES = K.TABLE_FILES
VERDICTS = ('MATCHES', 'UNDERSTATES', 'OVERREACHES', 'UNLICENSED')
EXH_ONCE = 'complete over its named classes'
OPEN_PHRASE = re.compile(r'carr\w+ as (?:the|its) one open premise')


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b647')
            and 'data/b647_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def run_py(name, *args):
    r = subprocess.run([sys.executable, os.path.join(T, name)] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def capture_now():
    """the act's command capture, read live: the seat's session from the ruling's delivery and its helper readers'."""
    import b647_record as REC
    import edit_route as ER
    rows = ER.capture(REC.SESSION, K.ANCHOR, REC.SUBAGENTS)
    for sid, anc in REC.SESSIONS_AFTER:
        rows += ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc,
                           'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
    return rows


def sources():
    import b647_record as REC
    import b616_record as R6
    import licensed_table as LT
    import edit_route as ER
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b647_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b647_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    KJ = jl('b647_table_kernels.json')
    S = dict(
        REC=REC, LT=LT, ER=ER, face=face, ferry=rd('b647_ferry.txt'), scan=rd('b647_ferry_scan.txt'), procs=rd('b647_procs.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b646_closing.txt'), answers=rd('b647_author_answers.txt'), prerun=rd('b647_arms_prerun.txt'),
        rl=jl('b647_record_lines.json'), tests=jl('b647_tests_stepzero.json'), testst=rd('b647_tests_stepzero.txt'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))) + ['test_build_watch_b647.py'],
        sealj=jl('b647_seal_hashes.json'), sealnow=sealed_now(), bw=jl('b647_build_watch.json'), peaks=jl('b647_build_peaks.json'),
        watch_test=run_py('test_build_watch_b647.py'), files_watch=files_of(ROOT, WATCH_COMMIT), cmds=capture_now(),
        brief=rd('b647_kernel_brief.txt'), sorry=rd('b647_sorry_census.txt'), kj=KJ,
        ktab={x['kernel']: jl('b647_table_%s.json' % x['kernel']) for x in KJ.get('kernels') or []}, kt=rd('b647_table_kernels.txt'),
        kread=set(REC.KREAD), navrule=rd('b647_nav_rule.txt'), nav=jl('b647_table_navigator_memory.json'), navt=rd('b647_table_navigator_memory.txt'),
        navread=set(REC.NAV_READ), nonrows=REC._nonrow_texts(),
        gl_pre=cr0(blob(ROOT, PRE['relay'] + ':data/glossary.txt')), gl_now=cr0(raw(os.path.join(D, 'glossary.txt'))), glb=rd('b647_glossary_block.txt'),
        comp_test=run_py('test_composer_b647.py'), v4=rd('b647_deposit_description.txt'), v3=rd('b646_deposit_description.txt'),
        dj=jl('b647_deposit_description.json'), desct=rd('b647_desc_test.txt'),
        cmp=jl('b647_reader_d5_compare.json'), hand=rd('b647_reader_d5_handread.txt'), residue=rd('b647_desc_residue.txt'),
        zres=jl('b647_zenodo.json'), cols=jl('b647_census_columns.json'), colst=rd('b647_census_columns.txt'),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b647_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b647_act_root.json'), arj0=jl('b646_act_root.json'), art=rd('b647_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b647_kernels_face.json').get('kernels') or {}),
        push_lists={r: gs(r, 'branch', '--list', 'push-b646*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b647_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b647_mustnotexist.txt')),
        fj=jl('b647_findings.json'), tj=jl('b647_trail.json'), sc=jl('b647_scores.json'), desk=rd('b647_desk_notes.txt'), tfj=jl('b647_table_final.json'),
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
    banks = []
    for f in sorted(os.listdir(D)):
        if f.startswith(('b647_', 'audit_b647_')) and os.path.isfile(os.path.join(D, f)) and ('data/' + f) != EXPORT:
            banks.append(read(os.path.join(D, f)))
    S['banks_text'] = NL.join(banks)
    pub += banks + [read(f) for f in tools]
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
        if os.path.basename(p) in TABLE_FILES or p in ('data/act_roots.txt', 'data/glossary.txt'):
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
    """every test file tracked before the act, and the watchdog's planted test, run at step zero: clean but test_chain_page_b638.py (4)-(7)."""
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = sorted(n for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == names and nf == ['test_chain_page_b638.py'] \
        and j['test_chain_page_b638.py']['failing'] == ['(4)', '(5)', '(6)', '(7)'] \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 1' % (len(names), len(names))) in S['testst']


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b647 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    res = re.findall(r'^RESULT \(transcript line \d+\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) >= 1 and all(x >= 2 for x in per) and len(res) == len(heads) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and '(C2 kernels)' in a


def watch_test_ok(S):
    rc, out = S['watch_test']
    m = re.search(r'\(1\) THE PLANTED TREE: .*?driver peak (\d+) MB ; tree peak (\d+) MB', out)
    return rc == 0 and bool(m) and int(m.group(2)) > int(m.group(1)) and '3 of 3 cases as wanted -- PASS' in out \
        and S['files_watch'] == ['tools/build_watch.py', 'tools/test_build_watch_b647.py']


def peaks_ok(S):
    rows = S['peaks'].get('rows') or []
    return bool(rows) and all(isinstance(r.get('tree_peak'), int) and isinstance(r.get('driver_peak'), int) and r.get('host_low') is not None
                              for r in rows)


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def _commit_time(S, sha):
    for h, s, t in S['rlog']:
        if sha.startswith(h) or h.startswith(sha[:7]):
            return t
    return None


def before(S, a, b):
    ta, tb = _commit_time(S, a), _commit_time(S, b)
    return ta is not None and tb is not None and ta < tb


def kernels_ok(S):
    LT = S['LT']
    n = 0
    for k, j in S['ktab'].items():
        rows = j.get('rows') or []
        cnt, faults = LT.table(rows)
        if not rows or faults or cnt is None or dict(cnt) != {v: (j.get('counts') or {}).get(v, 0) for v in VERDICTS}:
            return False
        if any('textual' not in r or r.get('verdict') not in VERDICTS for r in rows):
            return False
        n += len(rows)
    t = S['kj'].get('rows')
    return len(S['ktab']) == 21 and t == n + 1369 and '**KERNELS 22 (21 read here, 1 carried)' in S['kt']


def kernels_read(S):
    nm = [r['id'] for j in S['ktab'].values() for r in j.get('rows') or [] if r['verdict'] != 'MATCHES']
    return bool(nm) and set(nm) <= S['kread'] and 'THE SEAT`S CONTROLS ON THE TWO CLASSES' in S['kt']


def classes_ok(S):
    tot = dict((c, sum((x.get('classes') or {}).get(c, 0) for x in S['kj'].get('kernels') or [])) for c in 'SAH')
    return all(k in S['brief'] for k in ('S -- A SORRY-CLOSED', 'A -- AN AXIOM-PROFILE', 'H -- A MODULE HEADER')) \
        and re.search(r'CLASSES S %d A %d H %d\.\*\*' % (tot['S'], tot['A'], tot['H']), S['kt']) is not None


def sorry_ok(S):
    s = S['sorry']
    return len(re.findall(r'\| (BUILT|TRACKED ONLY) \|', s)) == 37 and len(re.findall(r'\| BUILT \|', s)) == 4


def nav_ok(S):
    LT = S['LT']
    rows = S['nav'].get('rows') or []
    cnt, faults = LT.table(rows)
    pf = S['nav'].get('per_file') or {}
    return bool(rows) and not faults and cnt is not None and dict(cnt) == {v: (S['nav'].get('counts') or {}).get(v, 0) for v in VERDICTS} \
        and sum((pf.get('FILE %d' % f) or {}).get('units', 0) for f in (1, 2, 3, 4)) == 276 and 'FAULTS 0.**' in S['navt'] \
        and set(r['id'] for r in rows if r['verdict'] != 'MATCHES') <= S['navread'] and '35 agree' in S['navt']


def nav_unbanked(S):
    return bool(S['nonrows']) and not [s for s in S['nonrows'] if len(s) >= 30 and s in S['banks_text']]


def glossary_ok(S):
    a = appended(S['gl_pre'], S['gl_now'])
    ents = [l.split('\t')[0] for l in a.split(NL) if l.strip() and not l.startswith('#')]
    return S['gl_pre'] is not None and (S['gl_now'] or b'').startswith(S['gl_pre']) and ents == ['the surround', 'priced'] \
        and 'THE NEW BLOCK THE OLD PLUS THE TWO ENTRIES: YES' in S['glb'] and 'BYTE FOR BYTE: YES' in S['glb']


def composer_ok(S):
    rc, out = S['comp_test']
    m = re.search(r'(\d+) of (\d+) PASS', out)
    return rc == 0 and bool(m) and m.group(1) == m.group(2) and int(m.group(1)) >= 18


def v4_ok(S):
    v4 = S['v4']
    return bool(v4) and v4.count(EXH_ONCE) == 1 and len(OPEN_PHRASE.findall(v4)) == 2 and 'NOT READ' not in v4 \
        and S['dj'].get('sha256') == hashlib.sha256(v4.encode('utf-8')).hexdigest() and 'FORBIDDEN-CONTENT 9 of 9 ; EDIT TESTS EXIT 0' in S['desct']


def reader_ok(S):
    c = S['cmp']
    return c.get('needles') == 3 and c.get('hand') == 3 and c.get('of') == 3 and len(re.findall(r'^HAND \d: AGREE', S['hand'], re.M)) == 3 \
        and re.search(r'RESIDUE \d+ PASSAGES', S['residue']) is not None


def draft_held(S):
    z = S['zres']
    d, r, h = z.get('desc') or {}, z.get('read') or {}, z.get('hold') or {}
    return d.get('put') == 200 and r.get('exact') is True and r.get('digest') is True and r.get('files_same') is True \
        and r.get('submitted') is False and h.get('submitted') is False and r.get('id') == int(K.DRAFT) \
        and d.get('v4_sha256') == hashlib.sha256(S['v4'].encode('utf-8')).hexdigest()


def columns_ok(S):
    rows = S['cols'].get('rows') or []
    return len(rows) == 77 and sum(1 for r in rows if r.get('kind') == 'kernel') == 22 and sum(1 for r in rows if r.get('kind') == 'companion') == 7 \
        and 'NO BLANK COUNTED AS A VALUE.**' in S['colst']


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


POST_SEAL = ('b647 seal', 'b647 pre-root', 'b647 root', 'b647 record', 'b647 --', 'b647 closing')


def _component_commit(s):
    return s.startswith('b647') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 24 and rows[23][:3] == ['b647', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b648_' in it] \
        and any(it.startswith('data/b647_table_kernels.txt ') for it in j.get('items') or []) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b647_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b647') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 648)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**Every kernel’s docstrings**', '**The navigator’s memory**', '**The description at v4**', '**The watchdog on the process tree**',
                 '**The census columns**', '**The record lines**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens',
                 '**Next.**', 'b648')


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


def publish_uncalled(S):
    pub = ['actions' + '/pub' + 'lish', 'z_' + 'publish']
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
        and (', no ' + 'outbound request,') not in t and 'IN FULL, FOR THE NAVIGATOR' in t and 'BY FILE AND LINE, IN FULL' in t


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _rl(S, i, line, key='rl'):
    ls = list(S[key].get('lines') or [])
    ls[i:i + 1] = [dict(rline(S, i, key), line=line)]
    return put(S, key, dict(S[key], lines=ls))


def _mut(S, key, f):
    d = copy.deepcopy(S[key])
    f(d)
    return put(S, key, d)


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R257) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the process listing at step zero: none running, no orphan, free memory read', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'].replace('### orphans: NONE', '### orphans: 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act and the watchdog`s planted test: every one clean but '
     'test_chain_page_b638.py (4)-(7)', lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b646_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay and PLACE-papers branch lists', lambda S: all(v == '' for v in S['push_lists'].values()),
     lambda S: put(S, 'push_lists', {'D:/relay': 'push-b646'})),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompts, every call`s result', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('(C2 kernels)', '(C2 kernel)'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live (the seat`s session and its helper readers)', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b647_record.py")])),
    ('G-WATCHDOG-TREE', 'tools/test_build_watch_b647.py run live: the tree`s peak above the driver`s; the watchdog`s commit alone', lambda S: watch_test_ok(S),
     lambda S: put(S, 'files_watch', S['files_watch'] + ['data/b647_ferry.txt'])),
    ('G-PEAKS-BANKED', 'the peaks bank: every attempt`s driver peak, tree peak and host low', lambda S: peaks_ok(S),
     lambda S: put(S, 'peaks', {'rows': []})),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line', lambda S: landed(S, 0, ['b646', '8095']), lambda S: _rl(S, 0, 1)),
    ('G-FOOTPRINT-LINE', 'OPEN_TRAILS at the record-lines bank`s line', lambda S: landed(S, 1, ['W-ORD-HOLD-FOOTPRINT', '13631']), lambda S: _rl(S, 1, 1)),
    ('G-BRIEF-BEFORE-ROWS', 'the commit times: the brief before the sorry census before the answer before the kernel banks', lambda S: before(S, BRIEF_COMMIT, SORRY_COMMIT)
     and before(S, SORRY_COMMIT, ANSWERS_COMMIT) and before(S, ANSWERS_COMMIT, KBANKS_COMMIT),
     lambda S: put(S, 'rlog', [(h, s, (10 ** 10 if h.startswith(BRIEF_COMMIT[:7]) else t)) for h, s, t in S['rlog']])),
    ('G-SORRY-CENSUS', 'the sorry census: every sorry in code by file and line, 37, four inside a built library', lambda S: sorry_ok(S),
     lambda S: put(S, 'sorry', S['sorry'].replace('| BUILT |', '| X |', 1))),
    ('G-KERNELS-EVERY-ROW', 'the 21 kernel banks: every row one verdict, the instrument taking each table, TEXTUAL or ELABORATED marked; the joined count',
     lambda S: kernels_ok(S), lambda S: _mut(S, 'ktab', lambda d: d['SIDE-kernel']['rows'].pop())),
    ('G-KERNELS-SEAT-READ', 'the record tool`s KREAD against every non-MATCHES kernel row; the controls printed', lambda S: kernels_read(S),
     lambda S: put(S, 'kread', set())),
    ('G-KERNELS-CLASSES', 'the brief`s three classes and the joined bank`s count of each', lambda S: classes_ok(S),
     lambda S: put(S, 'kt', S['kt'].replace('CLASSES S', 'CLASSES X'))),
    ('G-NAV-RULE-FIRST', 'the commit times and the rule bank: the rule printed before the table', lambda S: before(S, NAVRULE_COMMIT, NAVTABLE_COMMIT)
     and 'A ROW: a unit asserting a fact about the corpus' in S['navrule'], lambda S: put(S, 'navrule', '')),
    ('G-NAV-TABLE', 'the navigator table: every row HAND and taken, 276 units, every non-MATCHES row read by the seat, the sample agreeing',
     lambda S: nav_ok(S), lambda S: put(S, 'navread', set())),
    ('G-NAV-NOT-ROW-UNBANKED', 'every not-row unit`s text of the export against every b647 bank', lambda S: nav_unbanked(S),
     lambda S: put(S, 'banks_text', S['banks_text'] + NL.join(S['nonrows']))),
    ('G-GLOSSARY-APPENDED', 'relay data/glossary.txt before and now, and the block bank: two entries appended, the block the old plus two',
     lambda S: glossary_ok(S), lambda S: put(S, 'gl_now', b'x' + (S['gl_now'] or b''))),
    ('G-COMPOSER-TESTS', 'tools/test_composer_b647.py run live: a test per edit beside its control', lambda S: composer_ok(S),
     lambda S: put(S, 'comp_test', (1, ''))),
    ('G-V4-COMPOSED', 'v4: exhaustiveness once, the open-premise phrase twice, no unread figure, the bank`s digest, the forbidden-content test',
     lambda S: v4_ok(S), lambda S: put(S, 'v4', S['v4'] + ' complete over its named classes')),
    ('G-READER-SCORED', 'the compare bank, the hand reading and the residue', lambda S: reader_ok(S),
     lambda S: put(S, 'cmp', dict(S['cmp'], hand=2))),
    ('G-DRAFT-HELD', 'the route`s bank: the PUT accepted, the description read back byte for byte, the files the same, unsubmitted twice', lambda S: draft_held(S),
     lambda S: put(S, 'zres', dict(S['zres'], read=dict(S['zres'].get('read') or {}, submitted=True)))),
    ('G-COLUMNS-BANKED', 'the columns bank: 77 rows, the companions and the kernels among them, no blank counted', lambda S: columns_ok(S),
     lambda S: _mut(S, 'cols', lambda d: d['rows'].pop())),
    ('G-NO-EDITION', 'PLACE-papers` changed files against FINDINGS and OPEN_TRAILS', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the current documents, the companions, the monograph, the map, the census and the pages: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal', lambda S: kernels_untouched(S),
     lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b646`s tools, the instrument, the intake form, the arm, the sealed composer and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 48ed6db2 but the shared additive files, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 0,
     lambda S: put(S, 'prior_bad', ['data/b646_closing.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes', lambda S: not any(S['nd_pub'].values()),
     lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call (the description`s PUT the route`s one write)', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b647 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b647_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b646`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b646 closed' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-R257-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R257) END' in S['ferry'] and S['ot'].count('**(R257) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R257) ratified', '**(R2570) ratified'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 24th line, the root bank and its items', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b648 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b647 AGREE, b647 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line', lambda S: bool(S['tj'].get('line')) and oline(S, S['tj']['line']) == S['REC'].TRAIL_HEAD(),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b647 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b647_record.py agree', 'b647_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line', lambda S: '**Next:** per `(R257)`(7), the author’s word pending, b648' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** per `(R257)`(7)', '**Next:** per `(R2570)`(7)'))),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b647')" in S['suite'] and "'data/b647_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b647_closing.py: the closing sentence in the rule`s words with the plain reads named; the sorries and the navigator`s rows in full',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author in any ' + 'outbound request', 'x'))),
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
    p = os.path.join(D, 'b647_seal_hashes.json')
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
    print('  written: b647_seal_hashes.json')
    return 0


def main():
    if SEAL:
        return seal()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b647 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### G-EDIT-ROUTE read %d captured commands (the seat`s session and its helper readers); offences %d' % (
        len(S['cmds']), len(S['ER'].scan(S['cmds']))))
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
        out = os.path.join(D, 'b647_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b647_checks_postpush.txt' if pushed else 'b647_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b647_arms_prerun.txt', 'b647_lsr_prerun.json').replace('b647_checks', 'b647_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b647_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
