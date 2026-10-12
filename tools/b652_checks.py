# -*- coding: utf-8 -*-
"""b652_checks.py -- THE SUITE OF b652, UNDER (R262): b651 AT ITS WEIGHT; THE CONVERSION RULE; THE BUILD MARGIN MEASURED AND THE BRANCHES
RETRIED UNDER IT; SIDE-KERNEL'S DOCSTRINGS CUT FROM THE SENTENCE ROWS; THE INSTRUMENT VERDICT.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R262)(2): every look-up of a landed line converts by the record tool's conv, imported here (`from b652_record import conv`); no
### other conversion is defined or called in this file. G-CONVERSION-PLANTED lands a head carrying a backtick possessive in a scratch ledger
### and finds it by conv, the straight conversion of b551_record the control that misses.
### ### The harness is b568's to b651's (helpers, runner, seal), written by the Write tool from tools/b651_checks.py; the sources,
### predicates and arms are b652's.
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
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b616_claims as KC0     # noqa: E402
import b652_worklist as K     # noqa: E402
from b652_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
KD = 'D:/' + K.DS_KERNEL
FACE = os.path.join(D, 'b652_registration_2026-10-11.txt')
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = K.STEPZERO
EXPORT = K.EXPORT
GEN_COMMIT = ('eb3141f7', 'licensed_table.py', 'test_licensed_table_instrument_b652.py')
CONV_COMMIT = '1af9626c'
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
# ### the instruments b652 does not edit, against relay 1a4caf67 (tools/licensed_table.py is edited by the act and read by G-GENERATOR-ALONE)
INST = ('b651_checks.py', 'b651_closing.py', 'b651_tests.py', 'b651_worklist.py', 'b651_reg_gate.py', 'b651_regspec.py', 'b651_record.py',
        'b649_record.py', 'b648_record.py', 'b647_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py', 'test_licensed_table_b645.py',
        'b643_record.py', 'b641_record.py', 'b633_record.py', 'b602_record.py', 'b616_record.py', 'b551_record.py', 'b566_record.py',
        'act_root.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py', 'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py',
        'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py', 'b616_claims.py', 'ferry_scan.py', 'edit_route.py',
        'test_edit_route_b646.py', 'e0_rule.py', 'build_watch.py', 'test_build_watch_b647.py', 'chain_page.py', 'axiom_claim.py',
        'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py', 'test_no_sorry_main.py', 'test_axiom_claim.py',
        'test_module_header.py', 'test_axiom_claim_b651.py', 'test_chain_page_b638.py')
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'day1/ONE_PAGE_PROOF.md')
TABLE_FILES = K.TABLE_FILES
UNCUT_FILES = ('Kernel/SimplicityRouteD.lean', 'Kernel/SimplicityRouteE.lean')


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


def read_blob(repo, spec):
    b = blob(repo, spec)
    return b.decode('utf-8', 'replace').replace(chr(13), '') if b is not None else ''


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b652')
            and 'data/b652_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def capture_now():
    import b652_record as REC
    return REC.capture()


def run_test(name):
    r = subprocess.run([sys.executable, os.path.join(T, name)], capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return dict(rc=r.returncode, out=r.stdout or '')


def live_arms():
    """b649's three arms run at HEAD by their own tools; G-NO-SORRY-MAIN reads each kernel's remote through this run's one ls-remote."""
    import no_sorry_main as NSM
    import axiom_claim as AC
    import module_header as MH
    names = NSM.kernels()
    t0 = time.time()
    nsm = NSM.run(names, KC0.remote_refs)
    t1 = time.time()
    idx, counts = AC.index()
    ac_rows, ac_per = AC.run(names, idx)
    t2 = time.time()
    mh_per, mh_rows = MH.run(names)
    t3 = time.time()
    return dict(names=names, nsm=nsm, ac=ac_rows, ac_counts=counts, mh=mh_rows, mh_per=mh_per, secs=(t1 - t0, t2 - t1, t3 - t2))


def conv_planted():
    """the suite's planted case of (R262)(2): a head with a backtick possessive landed in a scratch ledger by the record tool's append_to and
    looked up by conv; the straight conversion of b551_record read beside it as the control that misses."""
    import b652_record as REC
    import b551_record as OLD
    head = '### b999 — a planted record: the largest kernel`s docstrings, the author`s word'
    with tempfile.TemporaryDirectory(prefix='b652_suite_conv_') as d:
        led = os.path.join(d, 'LEDGER.md')
        open(led, 'wb').write(b'# a scratch ledger\n\nline three\n')
        REC.append_to(led, '\n' + head + ': planted.\n')
        lines = io.open(led, encoding='utf-8').read().split(NL)
        landed = [i + 1 for i, l in enumerate(lines) if l.startswith('### b999')]
        found = REC.line_of(led, head)
        straight = OLD.line_of(led, head)
    return dict(landed=landed, found=found, straight=straight)


def conv_alone():
    """every b652 tool's code, prose stripped: no other conversion of a backtick possessive defined or called."""
    # ### the tokens built from pieces, so this file's own text carries none of them
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    bad = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b652_') and f.endswith('.py'):
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def code_only(t):
    out, i, depth, n = [], 0, 0, len(t)
    while i < n:
        if t.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if depth and t.startswith('-/', i):
            depth -= 1
            i += 2
            continue
        if depth:
            i += 1
            continue
        if t.startswith('--', i):
            j = t.find(NL, i)
            i = n if j < 0 else j
            continue
        if t[i] == '"':
            j = i + 1
            while j < n and t[j] != '"':
                j += 2 if t[j] == chr(92) else 1
            out.append(t[i:j + 1])
            i = j + 1
            continue
        out.append(t[i])
        i += 1
    return ' '.join(''.join(out).split())


def cut_state():
    """the cut branch against main: its commits, each one file, the file at the branch against main's blob with the planned replacements, the
    code outside comments; the files left uncut."""
    plan = [b for b in jl('b652_sentence_cut_plan.json').get('blocks') or [] if b.get('kept') is not None]
    files = sorted(set(b['file'] for b in plan))
    log = [l for l in gs(KD, 'log', '--reverse', '--format=%h', 'main..' + K.CUT_BRANCH).split(NL) if l.strip()]
    per = dict((h, files_of(KD, h)) for h in log)
    code_bad, uncut_bad = [], []
    for f in files:
        if code_only(read_blob(KD, 'main:' + f)) != code_only(read_blob(KD, K.CUT_BRANCH + ':' + f)):
            code_bad.append(f)
    for f in UNCUT_FILES:
        if read_blob(KD, 'main:' + f) != read_blob(KD, K.CUT_BRANCH + ':' + f):
            uncut_bad.append(f)
    pc = [l for l in gs(KD, 'log', '--format=%h', K.CUT_BRANCH + '..' + K.DS_BRANCH).split(NL) if l.strip()]
    return dict(files=files, log=log, per=per, code_bad=code_bad, uncut_bad=uncut_bad, pc=pc,
                pc_files=dict((h, files_of(KD, h)) for h in pc),
                pc_on_cut=subprocess.run(['git', '-C', KD, 'merge-base', '--is-ancestor', K.CUT_BRANCH, K.DS_BRANCH]).returncode == 0,
                merged=gs(KD, 'branch', '--merged', 'main', '--list', K.CUT_BRANCH, K.DS_BRANCH),
                blocks=len(plan))


TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py',
         'test_licensed_table_instrument_b652.py', 'test_licensed_table_b645.py')


def sources():
    import b652_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import licensed_table as LT
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b652_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b652_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    S = dict(
        REC=REC, ER=ER, LT=LT, face=face, ferry=rd('b652_ferry.txt'), scan=rd('b652_ferry_scan.txt'), stepz=rd('b652_stepzero.txt'),
        readfirst=rd('b652_readfirst.txt'), defects=rd('b652_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b652_author_answers.txt'), prerun=rd('b652_arms_prerun.txt'),
        rl=jl('b652_record_lines.json'), ml=jl('b652_margin_line.json'),
        tests=jl('b652_tests_stepzero.json'), testst=rd('b652_tests_stepzero.txt'), withheld=jl('b652_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b652_seal_hashes.json'), sealnow=sealed_now(), peaks=jl('b652_build_peaks.json'), watch=jl('b652_build_watch.json'),
        margin=jl('b652_build_margin.json'), builds=jl('b652_build_results.json'),
        cmds=capture_now(), planted={t: run_test(t) for t in TESTS}, conv=conv_planted(), conv_bad=conv_alone(),
        gen_files=files_of(ROOT, GEN_COMMIT[0]), conv_files=files_of(ROOT, CONV_COMMIT),
        gen_log=[l for l in gs(ROOT, 'log', '--format=%h', '--abbrev=8', PRE['relay'] + '..HEAD', '--', 'tools/' + GEN_COMMIT[1]).split(NL) if l.strip()],
        grades=jl('b652_sentence_grades.json'), cut=cut_state(), table_after=jl('b652_table_after.json'),
        parents=dict((r['id'], r) for r in jl('b647_table_SIDE-kernel.json').get('rows') or []),
        sentrows=jl('b651_table_SIDE-kernel_sentences.json').get('rows') or [],
        irows=jl('b652_instrument_rows.json'), conv_bank=rd('b652_conversion.txt'),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b652_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b652_act_root.json'), arj0=jl('b651_act_root.json'), art=rd('b652_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b652_kernels_face.json').get('kernels') or {}),
        push_lists={r: gs(r, 'branch', '--list', 'push-b651*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b652_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b652_mustnotexist.txt')),
        fj=jl('b652_findings.json'), tj=jl('b652_trail.json'), sc=jl('b652_scores.json'), desk=rd('b652_desk_notes.txt'), tfj=jl('b652_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['live'] = live_arms()
    S['mains_now'] = dict((r['kernel'], r['main']) for r in S['live']['nsm'])
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
        if f.startswith(('b652_', 'audit_b652_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
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


def rline(S, i, key='rl'):
    x = (S[key].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need, key='rl'):
    x = rline(S, i, key)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(conv(x.get('head', '\x00'))) and all(n in o for n in need)


def procs_ok(S):
    p = S['stepz']
    return 'NONE: no tail, lean, lake or python process is running' in p and '### orphans: NONE' in p and 'free memory' in p


STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(1)', '(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    """every test file tracked before the act run at step zero with the lists in force, test_elab_reader_b634.py withheld by the margin rule:
    clean but test_chain_page.py (9) and test_chain_page_b638.py (1), (4)-(7)."""
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 2' % (len(names), len(names) - 1)) in S['testst']


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b652 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) == 2 and all(x >= 2 for x in per) and len(res) == len(calls) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) and len(re.findall(r'^### THE AUTHOR`S WORD ', a, re.M)) >= 2


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def planted_ok(S, t, n):
    p = S['planted'][t]
    return p['rc'] == 0 and ('%d of %d cases as wanted -- PASS' % (n, n)) in p['out']


# ================================================================== b649's ARMS, LIVE AT HEAD
def nsm_hits(S):
    return [(r['kernel'], f, ln) for r in S['live']['nsm'] for f, ln, _t in r['hits']]


def no_sorry_main(S):
    rows = S['live']['nsm']
    return len(rows) == len(S['live']['names']) > 0 and all(r['equal'] for r in rows) and not nsm_hits(S)


def ac_count(rows, v):
    return sum(1 for r in rows if r['verdict'] == v)


def axiom_claim(S):
    rows = S['live']['ac']
    return bool(rows) and ac_count(rows, 'CONTRADICTED') == 0


def module_header(S):
    per = S['live']['mh_per']
    return len(per) == len(S['live']['names']) > 0 and sum(v['headers'] for v in per.values()) > 0 and S['live']['mh'] == []


# ================================================================== (R262)(1), (2): THE RECORD LINES, THE CONVERSION
def readfirst_ok(S):
    t = S['readfirst']
    return all(x in t for x in ('data/b651_closing.txt', 'data/b651_defects.txt', 'data/b651_navigator_rows.txt', 'd7ab2fdb', 'data/b649_lv_build.txt',
                                'b648-restate-SIDE-lv-conservation', 'b648-restate-SIDE-effects', 'docstrings-SIDE-kernel', 'tools/axiom_claim.py',
                                'tools/licensed_table.py', 'tools/b641_record.py :255', 'tools/b551_record.py :678', 'FINDINGS.md :8229',
                                'OPEN_TRAILS.md :13874'))


def restoration_ok(S):
    t = S['defects']
    i = t.find('### CARRIED FROM b651')
    j = t.find("### THE ACT'S OWN")
    return 0 <= i < j and 'b651_author_answers.txt' in t[i:j] and 'f2cdc66a' in t[i:j] and 'later than the root' in t[i:j]


def conv_planted_ok(S):
    c = S['conv']
    return c['landed'] == [5] and c['found'] == 5 and c['straight'] is None


def conv_one_ok(S):
    return S['conv_bad'] == [] and 'from b652_record import conv' in S['suite'] and S['conv_files'] == ['tools/b652_record.py', 'tools/test_conversion_b652.py']


# ================================================================== (R262)(3): THE MARGIN AND THE BUILDS
def margin_ok(S):
    rows = S['margin'].get('readings') or []
    tg = ('SIDELvConservation.T3_StepNineBridge', 'SIDEEffects.Milestones', 'Kernel.PerpendicularCrossing')
    corrected = [r for r in rows if r.get('term') == 'host loss']
    return all(len([r for r in rows if r['target'] == t]) >= 2 for t in tg) and bool(corrected) \
        and all(r['needed'] in (1428, 1255, 906) and r['seen'] == r['free'] - 2560 and r['allows'] == (r['seen'] >= r['needed']) for r in corrected) \
        and len((S['margin'].get('cut_branch') or {}).get('files') or []) == 33


def builds_ok(S):
    """no build started where the margin seen at its slot was beneath the margin needed; every start has its slot reading; the results bank
    agrees with the watchdog's peaks bank by module."""
    rows = S['builds'].get('rows') or []
    peaks = S['peaks'].get('rows') or []
    started = [r for r in rows if r.get('started')]
    return bool(rows) and all(r.get('slot_seen') is not None and r['slot_seen'] >= r['needed'] for r in started) \
        and all(any(p.get('module') == r['target'] for p in peaks) for r in started) \
        and all(r.get('outcome') in ('BUILT', 'STOPPED', 'RUN-BENEATH-HOLD', 'UNBUILT') for r in rows)


def merges_ok(S):
    """a branch merged only where its build passed and its gate read clean; the cut branch never merged."""
    rows = S['builds'].get('rows') or []
    for r in rows:
        if r.get('merged') and not (r.get('outcome') == 'BUILT' and r.get('gate') == 'PASS'):
            return False
    return S['cut']['merged'] == ''


# ================================================================== (R262)(4): THE CUT
def grades_ok(S):
    g = S['grades'].get('grades') or {}
    import collections as C
    by = C.OrderedDict()
    for r in S['sentrows']:
        by.setdefault(r['parent'], []).append(r)
    blocks = list(by.items())
    if len(blocks) != 116 or len(g) != 116:
        return False
    for k, lst in g.items():
        p, rs = blocks[int(k) - 1]
        lic = S['parents'][p]['licensed']
        if not lst or any(q not in lic or n > len(rs) for n, q in lst):
            return False
    return sum(len(v) for v in g.values()) == 152


def cut_ok(S):
    c = S['cut']
    return len(c['log']) == len(c['files']) == 33 and all(len(v) == 1 for v in c['per'].values()) \
        and sorted(v[0] for v in c['per'].values()) == c['files'] and c['blocks'] == 113


def cut_code_ok(S):
    c = S['cut']
    return c['code_bad'] == [] and c['uncut_bad'] == [] and bool(c['files'])


def rebased_ok(S):
    c = S['cut']
    return c['pc_on_cut'] and len(c['pc']) == 2 and all(v == ['Kernel/PerpendicularCrossing.lean'] for v in c['pc_files'].values())


def table_after_ok(S):
    ta = S['table_after']
    a, b = ta.get('after') or {}, ta.get('before') or {}
    return bool(a) and sum((a.get('counts') or {}).values()) == 433 and len(ta.get('not_matches') or []) == sum(
        v for k, v in (a.get('counts') or {}).items() if k != 'MATCHES') and b.get('rev') and a.get('rev')


# ================================================================== (R262)(5): THE INSTRUMENT VERDICT
def generator_alone(S):
    return S['gen_log'] == [GEN_COMMIT[0]] and S['gen_files'] == sorted(['tools/' + GEN_COMMIT[1], 'tools/' + GEN_COMMIT[2], 'data/b652_tests_c4.json'])


def irows_ok(S):
    rows = S['irows'].get('rows') or []
    counts, faults = S['LT'].table(rows)
    return len(rows) == 11 and not faults and counts and counts.get('INSTRUMENT') == 11 and all(S['LT'].label(r).startswith('INSTRUMENT(') for r in rows)


def real_stay(S):
    return all(S['LT'].arm_verdict('G-AXIOM-CLAIM', 'CONTRADICTED', False) == 'CONTRADICTED' for _ in range(4)) \
        and ac_count(S['live']['ac'], 'CONTRADICTED') == 4


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
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


POST_SEAL = ('b652 seal', 'b652 pre-root', 'b652 root', 'b652 record', 'b652 --', 'b652 closing')


def _component_commit(s):
    return s.startswith('b652') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 29 and rows[28][:3] == ['b652', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b653_' in it] \
        and any(it.startswith('data/b652_sentence_grades.txt ') for it in j.get('items') or []) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b652_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b652') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 653)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The conversion rule**', '**The build margin**', '**The docstrings**', '**The instrument verdict**', '**The record lines**',
                 '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b653')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == conv(S['fj'].get('title') or '\x00') and all(x in tail for x in ENTRY_NEEDLES)


def trail_tail(S):
    t = S['ot']
    i = t.find(conv(S['REC'].TRAIL_HEAD()))
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
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md'])


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and 'THE BUILD MARGIN' in t and 'THE INSTRUMENT VERDICT' in t and 'THE CUT' in t and 'mirror' in t


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


def _live(S, f):
    d = copy.deepcopy(S['live'])
    f(d)
    return put(S, 'live', d)


def _planted(S, t):
    return put(S, 'planted', dict(S['planted'], **{t: dict(rc=1, out='')}))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R262) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: none running, no orphan, free memory read', lambda S: procs_ok(S),
     lambda S: put(S, 'stepz', S['stepz'].replace('### orphans: NONE', '### orphans: 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act: every one run but test_elab_reader_b634.py withheld by the '
     'margin, clean but test_chain_page.py (9) and test_chain_page_b638.py (1), (4)-(7)', lambda S: tests_ok(S),
     lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b651_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay and PLACE-papers branch lists and the step-zero bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and 'push-b651* now 0' in S['stepz'] and S['stepz'].count('push-b651* now 0') == 2, lambda S: put(S, 'push_lists', {'D:/relay': 'push-b651'})),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', S['readfirst'].replace('tools/b551_record.py :678', 'x'))),
    ('G-RESTORATION-LINE', 'the defects bank`s successor form: the dated post-close line first', lambda S: restoration_ok(S),
     lambda S: put(S, 'defects', S['defects'].replace('### CARRIED FROM b651', '### x'))),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: two prompts with their options and results, the author`s words verbatim', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('THE AUTHOR`S ANSWERS', 'THE ANSWERS'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b652_record.py")])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: landed(S, 0, ['b651 AT ITS WEIGHT', 'Fourteen defects']),
     lambda S: _rl(S, 0, 1)),
    ('G-CONVERSION-LINE', 'OPEN_TRAILS at the record-lines bank`s line, found by conv', lambda S: landed(S, 1, ['THE CONVERSION RULE', '`conv`']),
     lambda S: _rl(S, 1, 1)),
    ('G-CONVERSION-PLANTED', 'the suite`s own planted case: a backtick-possessive head landed in a scratch ledger, found by conv at :5, missed by the '
     'straight conversion', lambda S: conv_planted_ok(S), lambda S: put(S, 'conv', dict(S['conv'], straight=5))),
    ('G-CONVERSION-TEST', 'tools/test_conversion_b652.py run: 7 of 7', lambda S: planted_ok(S, 'test_conversion_b652.py', 7),
     lambda S: _planted(S, 'test_conversion_b652.py')),
    ('G-CONVERSION-ONE', 'every b652 tool`s code: no conversion but conv; the suite importing it; its commit the record tool and its test',
     lambda S: conv_one_ok(S), lambda S: put(S, 'conv_bad', ['b652_checks.py'])),
    ('G-MARGIN-READINGS', 'the margin bank: two or more readings per module, the corrected term`s rows consistent, the cut branch`s 33 files',
     lambda S: margin_ok(S), lambda S: _mut(S, 'margin', lambda d: d['readings'].append(dict(target='Kernel.PerpendicularCrossing', term='host loss',
                                                                                             needed=906, seen=100, free=2000, allows=True)))),
    ('G-MARGIN-LINE', 'OPEN_TRAILS at the margin line`s bank: the term corrected', lambda S: landed(S, 0, ['THE MARGIN TERM CORRECTED', 'host’s measured loss'], key='ml'),
     lambda S: _rl(S, 0, 1, key='ml')),
    ('G-BUILDS-UNDER-MARGIN', 'the build results against their slot readings and the watchdog`s peaks: no start beneath the needed margin',
     lambda S: builds_ok(S), lambda S: _mut(S, 'builds', lambda d: d['rows'].append(dict(target='x', started=True, slot_seen=0, needed=1, outcome='BUILT')))),
    ('G-MERGES-GATED', 'every merge against its build and gate; the cut branch unmerged', lambda S: merges_ok(S),
     lambda S: _mut(S, 'builds', lambda d: d['rows'].append(dict(target='x', merged='abc', outcome='STOPPED')))),
    ('G-NO-SORRY-MAIN', 'tools/no_sorry_main.py run at HEAD over every kernel, its remote read once by this run: no `sorry` in code, every pair equal',
     lambda S: no_sorry_main(S), lambda S: _live(S, lambda d: d['nsm'][0]['hits'].append(('x.lean', 1, 'sorry')))),
    ('G-NO-SORRY-MAIN-PLANTED', 'tools/test_no_sorry_main.py run: 5 of 5', lambda S: planted_ok(S, 'test_no_sorry_main.py', 5),
     lambda S: _planted(S, 'test_no_sorry_main.py')),
    ('G-GRADES-BOUND', 'the sentence grades: 152 rows over the 116 blocks, every quoted cell word a substring of its parent`s LICENSED cell',
     lambda S: grades_ok(S), lambda S: _mut(S, 'grades', lambda d: d['grades']['8'].append([1, 'words no cell carries']))),
    ('G-CUT-COMMITS', 'the cut branch`s commits: 33, one file each, the 33 files of the plan, 113 blocks', lambda S: cut_ok(S),
     lambda S: _mut(S, 'cut', lambda d: d['log'].append('deadbee'))),
    ('G-CUT-CODE-UNCHANGED', 'every cut file`s code outside comments, main against the branch; the two files left uncut', lambda S: cut_code_ok(S),
     lambda S: _mut(S, 'cut', lambda d: d['code_bad'].append('Kernel/Core.lean'))),
    ('G-PLAIN-REBASED', 'docstrings-SIDE-kernel over the cut branch: its two commits, PerpendicularCrossing.lean alone', lambda S: rebased_ok(S),
     lambda S: _mut(S, 'cut', lambda d: d.update(pc_on_cut=False))),
    ('G-TABLE-AFTER', 'the table-after bank: 433 rows after, every row outside MATCHES listed', lambda S: table_after_ok(S),
     lambda S: _mut(S, 'table_after', lambda d: d['not_matches'].pop())),
    ('G-GENERATOR-ALONE', 'the act`s commits touching tools/licensed_table.py: the one, the tool with its planted test and its run bank',
     lambda S: generator_alone(S), lambda S: put(S, 'gen_files', S['gen_files'] + ['x'])),
    ('G-INSTRUMENT-PLANTED', 'tools/test_licensed_table_instrument_b652.py run: 10 of 10', lambda S: planted_ok(S, 'test_licensed_table_instrument_b652.py', 10),
     lambda S: _planted(S, 'test_licensed_table_instrument_b652.py')),
    ('G-TABLE-B645-KEPT', 'tools/test_licensed_table_b645.py run: 18 of 18', lambda S: planted_ok(S, 'test_licensed_table_b645.py', 18),
     lambda S: _planted(S, 'test_licensed_table_b645.py')),
    ('G-INSTRUMENT-ROWS', 'the instrument rows bank through the table: 11 rows, all taken, all INSTRUMENT(<arm>)', lambda S: irows_ok(S),
     lambda S: _mut(S, 'irows', lambda d: d['rows'][0].pop('arm'))),
    ('G-REAL-STAY', 'the four real contradictions through arm_verdict and G-AXIOM-CLAIM at HEAD: CONTRADICTED, four', lambda S: real_stay(S),
     lambda S: _live(S, lambda d: d['ac'].append(dict(d['ac'][0], verdict='CONTRADICTED')))),
    ('G-AXIOM-CLAIM', 'tools/axiom_claim.py run at HEAD over every kernel against the banked prints: no claim CONTRADICTED', lambda S: axiom_claim(S),
     lambda S: _live(S, lambda d: d['ac'].append(dict(d['ac'][0], verdict='CONTRADICTED')))),
    ('G-AXIOM-CLAIM-PLANTED', 'tools/test_axiom_claim.py run: 12 of 12', lambda S: planted_ok(S, 'test_axiom_claim.py', 12),
     lambda S: _planted(S, 'test_axiom_claim.py')),
    ('G-MODULE-HEADER', 'tools/module_header.py run at HEAD over every kernel: no header OVERREACHES', lambda S: module_header(S),
     lambda S: _live(S, lambda d: d['mh'].append(dict(kernel='x', file='x.lean', line=1, name='x', why='planted')))),
    ('G-MODULE-HEADER-PLANTED', 'tools/test_module_header.py run: 12 of 12', lambda S: planted_ok(S, 'test_module_header.py', 12),
     lambda S: _planted(S, 'test_module_header.py')),
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS and OPEN_TRAILS', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the registry, the map, the censuses, the monograph, the pages, the simplicity file: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal', lambda S: kernels_untouched(S),
     lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b651`s tools, the earlier record tools, the instruments and the shared tools the act does not edit: before, working tree '
     'and HEAD', lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 1a4caf67 but the shared additive files, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 0,
     lambda S: put(S, 'prior_bad', ['data/b651_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes', lambda S: not any(S['nd_pub'].values()),
     lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b652 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b652_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b651`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b651 — lane three, act seventy-eight' in S['ot']
     and S['rootsf'].count(NL + 'b651 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b651 — lane three', '### b651 - lane three'))),
    ('G-R262-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R262) END' in S['ferry'] and S['ot'].count('**(R262) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R262) ratified', '**(R2620) ratified'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 29th line, the root bank and its items', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b653 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b652 AGREE, b652 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b652 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b652_record.py agree', 'b652_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b653', lambda S: '**Next:** b653, the author' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b653, the author', '**Next:** b654, the author'))),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 1a4caf67, b651`s push-out bank among them, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b652')" in S['suite'] and "'data/b652_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b652_closing.py: the closing sentence in the rule`s words with the plain reads named; the margin, the cut, the verdict, the mirror',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound request', 'x'))),
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
    p = os.path.join(D, 'b652_seal_hashes.json')
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
        print('  %-38s %s' % (t, now[t]))
    print('  written: b652_seal_hashes.json')
    return 0


def main():
    if SEAL:
        return seal()
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b652 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### G-EDIT-ROUTE read %d captured commands; offences %d' % (len(S['cmds']), len(S['ER'].scan(S['cmds']))))
    rec('  ### THE CONVERSION: the planted head landed at %s, found by conv at %s, by the straight conversion at %s; other conversions in the act`s '
        'tools %s' % (S['conv']['landed'], S['conv']['found'], S['conv']['straight'], S['conv_bad'] or 'NONE'))
    lv = S['live']
    rec('  ### THE THREE ARMS AT HEAD (seconds %s):' % ', '.join('%.0f' % x for x in lv['secs']))
    rec('  ###   G-NO-SORRY-MAIN read %d kernels` mains, pairs unequal %d; sorry in code %d: %s' % (
        len(lv['nsm']), sum(1 for r in lv['nsm'] if not r['equal']), len(nsm_hits(S)), '; '.join('%s %s:%d' % h for h in nsm_hits(S)) or 'none'))
    rec('  ###   G-AXIOM-CLAIM read %d claims: CONTRADICTED %d, UNVERIFIABLE %d, VERIFIED %d, UNBOUND %d, MENTION %d' % (
        sum(1 for r in lv['ac'] if r['verdict'] != 'OUT OF SCOPE'), ac_count(lv['ac'], 'CONTRADICTED'), ac_count(lv['ac'], 'UNVERIFIABLE'),
        ac_count(lv['ac'], 'VERIFIED'), ac_count(lv['ac'], 'UNBOUND'), ac_count(lv['ac'], 'MENTION')))
    for r in lv['ac']:
        if r['verdict'] == 'CONTRADICTED':
            rec('  ###     CONTRADICTED %s %s:%d -- %s' % (r['kernel'], r['file'], r['line'], ', '.join(x['decl'] for x in r['contradicted'][:6])))
    rec('  ###   G-MODULE-HEADER read %d headers: OVERREACHES %d rows' % (sum(v['headers'] for v in lv['mh_per'].values()), len(lv['mh'])))
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
    rec('  ### the run took %.0f s' % (time.time() - t_start))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b652_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b652_checks_postpush.txt' if pushed else 'b652_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b652_arms_prerun.txt', 'b652_lsr_prerun.json').replace('b652_checks', 'b652_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b652_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
