# -*- coding: utf-8 -*-
"""b648_checks.py -- THE SUITE OF b648, UNDER (R258): THE SORRY LINES CLASSIFIED FOR THE AUTHOR'S WORD; THE TWO PAGES THROUGH THE TABLE AND
RE-EMITTED; THE KEYSTONE CENSUS AT v0.8; THE h2 ROW; THE RE-CUT ORDER TO THE AUTHOR.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### The face is sealed AFTER Components 0-5; every commit whose subject opens `b648` and none of POST_SEAL's prefixes precedes the lock.
### ### G-ACTROOT-VERIFY reads the chain at commit (tools/act_root.py): b624 to b648 AGREE, b648's crlf count 0.
### ### G-NO-SORRY-MAIN, from this act (the author's answer at Component 2): every kernel's main grepped for `sorry` in code, by b647's census
### ### rule (tools/b648_record.py code_sorries), the quarantine branches outside it; it fails on any hit.
### ### The harness is b568's to b647's (helpers, runner, seal), written by the Write tool from tools/b647_checks.py; the sources, predicates and
### ### arms are b648's.
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
import b648_worklist as K     # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b648_registration_2026-10-10.txt')
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
STEPZERO = K.STEPZERO
EXPORT = K.EXPORT
REPAIRS = ('b42db0ce', 'ef4e5a2a', '87d3e6b9')      # ### relay: the three template repairs of tools/chain_page.py, in order
PAGE_COMMITS = ('8882980', '5d01279', '0c41807', '8add2af')   # ### PLACE-papers: the four page re-emissions, one page each
CEN_COMMIT = 'f66d23d'                              # ### PLACE-papers: the census at v0.8, alone
QUARANTINE = ('SIDE-kernel', 'SIDE-lv-conservation')
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
# ### the instruments b648 does not edit, against relay 6972e068: b647's tools, the instrument, the arm and the shared tools (tools/chain_page.py,
# ### whose templates the act repairs, is read by the repair arms instead)
INST = ('b647_checks.py', 'b647_closing.py', 'b647_tests.py', 'b647_worklist.py', 'b647_reg_gate.py', 'b647_regspec.py', 'b647_record.py',
        'b646_record.py', 'b645_record.py', 'licensed_table.py', 'test_licensed_table_b645.py', 'b628_record.py', 'b628_worklist.py', 'b644_record.py',
        'b643_record.py', 'b638_record.py', 'b633_record.py', 'b602_record.py', 'b641_record.py', 'b639_record.py', 'b616_record.py', 'act_root.py',
        'additive_shared.py', 'premise_status.py', 'terminal_table.py', 'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh',
        'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py', 'b616_claims.py', 'ferry_scan.py', 'edit_route.py', 'test_edit_route_b646.py',
        'e0_rule.py', 'build_watch.py', 'test_build_watch_b647.py', 'g_chain_page.py', 'test_chain_page_b596.py', 'test_chain_page.py',
        'test_g_chain_page.py')
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md', 'day1/A_Place_to_Stand_v5_18.md',
            'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 'day1/Exhaustive_Enumeration.md',
            'day1/Which_Structure_Confines.md', 'day1/Spectral_Inertness.md', 'day1/Seven_Mechanism_Classes.md', 'day1/Third_Identity_Element.md',
            'day1/Silence_of_Foundations.md', 'day1/ONE_PAGE_PROOF.md')
TABLE_FILES = K.TABLE_FILES
VERDICTS = ('MATCHES', 'UNDERSTATES', 'OVERREACHES', 'UNLICENSED')


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b648')
            and 'data/b648_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    """the act's command capture, read live: the seat's session from the ruling's delivery and its helper readers'."""
    import b648_record as REC
    import edit_route as ER
    rows = ER.capture(REC.SESSION, K.ANCHOR, REC.SUBAGENTS)
    for sid, anc in REC.SESSIONS_AFTER:
        rows += ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc,
                           'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
    return rows


def sources():
    import b648_record as REC
    import b616_record as R6
    import licensed_table as LT
    import edit_route as ER
    import chain_page as CP
    import b641_record as R41
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b648_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b648_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    S = dict(
        REC=REC, LT=LT, ER=ER, face=face, ferry=rd('b648_ferry.txt'), scan=rd('b648_ferry_scan.txt'), procs=rd('b648_procs.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b647_closing.txt'), answers=rd('b648_author_answers.txt'), prerun=rd('b648_arms_prerun.txt'),
        rl=jl('b648_record_lines.json'), cl_=jl('b648_correction_line.json'), tests=jl('b648_tests_stepzero.json'), testst=rd('b648_tests_stepzero.txt'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b648_seal_hashes.json'), sealnow=sealed_now(), bw=jl('b648_build_watch.json'), peaks=jl('b648_build_peaks.json'),
        cmds=capture_now(), cls=jl('b648_sorry_classification.json'), repairs=rd('b648_sorry_repairs.txt'),
        quar={k: dict(main=gs('D:/' + k, 'rev-parse', 'main'), branch=gs('D:/' + k, 'rev-parse', 'refs/heads/sorry-quarantine-' + k),
                      errata=read_blob('D:/' + k, 'main:ERRATA.md'), remote=KC0.remote_refs('D:/' + k)) for k in QUARANTINE},
        sorries={k: REC.code_sorries(k) for k in sorry_kernels(R41)}, before_answer=REC.before_answer_ok(),
        tp=jl('b648_table_pages.json'), ta=jl('b648_table_pages_after.json'), tpt=rd('b648_table_pages.txt'), tat=rd('b648_table_pages_after.txt'),
        arms_c2=rd('b648_page_arms_c2.txt'), arms_c1=rd('b648_page_arms.txt'),
        repair_files={h: files_of(ROOT, h) for h in REPAIRS},
        cp_commits=[l.split()[0] for l in gs(ROOT, 'log', '--format=%h', PRE['relay'] + '..HEAD', '--', 'tools/chain_page.py').split(NL) if l.strip()],
        page_files={h: files_of(PP, h) for h in PAGE_COMMITS}, cen_files=files_of(PP, CEN_COMMIT),
        glb=NL.join(CP.glossary_block()) + NL,
        glossed={p: read(os.path.join(PP, *p.split('/'))) for p in (K.PAGE, K.DIR_PAGE, K.CEN8)},
        kc=jl('b648_kernel_cites.json'), kct=rd('b648_kernel_cites.txt'), ediff=rd('b648_edition_diff.txt'), escan=rd('b648_census_termscan.txt'),
        ej=jl('b648_edition.json'), cen8=read(os.path.join(PP, *K.CEN8.split('/'))),
        cmp=jl('b648_reader_compare.json'), hand=rd('b648_reader_handread.txt'), rcmd=rd('b648_reader_command.txt'),
        h2=jl('b648_h2_row.json'), h2t=rd('b648_h2_row.txt'), lv_main=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'main'),
        ro=jl('b648_recut_order.json'), rot=rd('b648_recut_order.txt'),
        zen=sorted(f for f in os.listdir(D) if f.startswith('b648_zenodo')),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b648_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b648_act_root.json'), arj0=jl('b647_act_root.json'), art=rd('b648_act_root.txt'), rootsf=rd('act_roots.txt'),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b648_kernels_face.json').get('kernels') or {}),
        push_lists={r: gs(r, 'branch', '--list', 'push-b647*') for r in ('D:/relay', PP)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b648_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b648_mustnotexist.txt')),
        fj=jl('b648_findings.json'), tj=jl('b648_trail.json'), sc=jl('b648_scores.json'), desk=rd('b648_desk_notes.txt'), tfj=jl('b648_table_final.json'),
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
        if f.startswith(('b648_', 'audit_b648_')) and os.path.isfile(os.path.join(D, f)) and ('data/' + f) != EXPORT:
            banks.append(read(os.path.join(D, f)))
    pub += banks + [read(f) for f in tools] + [S['cen8'], S['glossed'].get(K.PAGE, ''), S['glossed'].get(K.DIR_PAGE, '')]
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


def sorry_kernels(R41):
    """G-NO-SORRY-MAIN's kernels: every repository of the terminal table (b647's sorry census read these) and every kernel the face reads."""
    t = jl('terminal_table.json').get('rows') or []
    return sorted(set(x['repo'] for x in t if x.get('repo', '').startswith('SIDE-')) | set(R41.KERNS_READ))


def read_blob(repo, spec):
    b = blob(repo, spec)
    return b.decode('utf-8', 'replace') if b is not None else ''


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


STEPZERO_FAILING = {'test_chain_page.py': ['(1)', '(14)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)'], 'test_g_chain_page.py': ['(1)']}


def tests_ok(S):
    """every test file tracked before the act run at step zero, test_elab_reader_b634.py under the watchdog and RUN-BENEATH-HOLD: clean but the
    page tests' glossary cases (cured by Component 3's re-emission) and test_chain_page_b638.py (4)-(7)."""
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 3' % (len(names), len(names) - 1)) in S['testst'] \
        and 'test_elab_reader_b634.py           ### RUN-BENEATH-HOLD' in S['testst']


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b648 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    res = re.findall(r'^RESULT \(transcript line \d+\): (.*)$', a, re.M)
    return bool(m) and int(m.group(1)) == len(heads) >= 1 and all(x >= 2 for x in per) and len(res) == len(heads) \
        and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) \
        and all(('(%s)' % h) in a for h in ('Sorry repairs', '20 kernels', 'Split cites', 'Re-cut order'))


def peaks_ok(S):
    rows = S['peaks'].get('rows') or []
    return bool(rows) and all(isinstance(r.get('tree_peak'), int) and isinstance(r.get('driver_peak'), int) and r.get('host_low') is not None
                              for r in rows)


def edit_route_ok(S):
    return bool(S['cmds']) and S['ER'].scan(S['cmds']) == []


def classified_ok(S):
    rows = S['cls'].get('rows') or []
    c = {}
    for r in rows:
        c[r.get('proposed')] = c.get(r.get('proposed'), 0) + 1
    return len(rows) == 37 and all(r.get('entered') for r in rows) and c == {'QUARANTINED': 33, 'RESTATED': 4} \
        and sum(1 for r in rows if r.get('built')) == 4 and all(r.get('proposed') == 'RESTATED' for r in rows if r.get('built'))


def quarantined_ok(S):
    for k, q in S['quar'].items():
        if not q['main'] or q['remote'].get('refs/heads/main') != q['main'] or q['remote'].get('refs/heads/sorry-quarantine-' + k) != q['branch'] \
                or 'E-2026-10-10-1' not in q['errata'] or not q['branch']:
            return False
    return 'QUARANTINED 33, MERGED AND PUSHED' in S['repairs']


def restated_named(S):
    rows = S['bw'].get('rows') or []
    mods = dict((r.get('module'), r) for r in rows)
    return 'RESTATED 4, ON BRANCHES, NOT MERGED, THEIR BUILDS BENEATH THE HOLD' in S['repairs'] and 'SIDEEffects.Milestones' in mods \
        and all(x < (mods['SIDEEffects.Milestones'].get('hold') or 0) for x in (mods['SIDEEffects.Milestones'].get('lows') or [10 ** 6]))


def no_sorry_main(S):
    return bool(S['sorries']) and all(v == [] for v in S['sorries'].values())


def pages_every_sentence(S):
    LT = S['LT']
    for j, t in ((S['tp'], S['tpt']), (S['ta'], S['tat'])):
        rows = j.get('rows') or []
        cnt, faults = LT.table(rows)
        if not rows or faults or cnt is None or ('%d ROWS: ' % len(rows)) not in t:
            return False
    return True


def repairs_ok(S):
    rf = S['repair_files']
    return sorted(S['cp_commits']) == sorted(h[:len(S['cp_commits'][0])] for h in REPAIRS) if S['cp_commits'] else False


def repairs_alone(S):
    rf = S['repair_files']
    return all(rf.get(h) == ['tools/chain_page.py'] for h in REPAIRS[:2]) and 'tools/chain_page.py' in (rf.get(REPAIRS[2]) or [])


def pages_alone(S):
    pf = S['page_files']
    return all(len(v) == 1 and v[0] in (K.PAGE, K.DIR_PAGE) for v in pf.values()) and sorted(x[0] for x in pf.values()) == sorted([K.PAGE, K.DIR_PAGE] * 2)


def arms_c2_ok(S):
    a = S['arms_c2']
    return 'PAGE ARMS PASSING : 2 of 2.' in a and 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA PASSING : 2 of 2.' in a and 'b648_nodes_zeta.txt' in a \
        and 'PASSING : 0 of 2.' in S['arms_c1']


def glossary_alike(S):
    return len(S['glossed']) == 3 and all(t.count(S['glb']) == 1 for t in S['glossed'].values())


def kcites_ok(S):
    rows = S['kc'].get('rows') or []
    return len(rows) == 20 and all((r['cluster'] != '') == r['how'].startswith(('SERVED-KEYSTONE: ', 'TERMINAL-HEADS: ')) for r in rows) \
        and all(r['how'].startswith(('SERVED-KEYSTONE: ', 'TERMINAL-HEADS: ', 'split: ')) or r['how'] == 'named by no keystone' for r in rows) \
        and 'NOT COUNTED' in S['kct']


def census_ok(S):
    return bool(S['cen8']) and S['cen_files'] == [K.CEN8] and 'HUNKS 3 ({\'insert\': 3}) ; v0.7.1 LINES REMOVED OR REPLACED : 0.' in S['ediff'] \
        and 'VERDICT          : CLEAN' in S['escan'] and S['ej'].get('sha256') == hashlib.sha256(S['cen8'].encode('utf-8')).hexdigest() \
        and '77 rows: 48 keystones, 7 Day 1 companions, 22 kernels' in S['cen8'] and '### The blank cells' in S['cen8']


def reader_ok(S):
    c = S['cmp']
    return c.get('hand') == 2 and c.get('of') == 2 and len(re.findall(r'^HAND \d: AGREE', S['hand'], re.M)) == 2 and c.get('needles') is not None


def reader_cmd_ok(S):
    ls = [l for l in S['rcmd'].split(NL) if l.strip()]
    return len(ls) == 1 and ls[0].startswith('Set-Location C:\\reader_b648; Get-Content C:\\reader_b648\\full_prompt.txt -Raw | claude -p ')


def h2_ok(S):
    h = S['h2']
    q = h.get('quotes') or {}
    return bool(h) and not h.get('faults') and len(q.get('lv') or []) == 2 and len(q.get('gloss') or []) == 1 and (h.get('row') or {}).get('proposed') \
        and S['lv_main'] == 'b2238d4' and 'NO KERNEL FILE WRITTEN' in S['h2t']


def recut_ok(S):
    rows = S['ro'].get('rows') or []
    mono = [r for r in rows if r['kind'] == 'monograph']
    comp = [r for r in rows if r['kind'] == 'companion']
    return len(mono) == 1 and mono[0]['over'] + mono[0]['unl'] == 217 and len(comp) == 7 and sum(r['over'] + r['unl'] for r in comp) == 118 \
        and sum(1 for r in rows if r['kind'] == 'page') == 2 and sum(1 for r in rows if r['kind'] == 'kernel') >= 21 and 'DOCUMENTS' in S['rot']


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


POST_SEAL = ('b648 seal', 'b648 pre-root', 'b648 root', 'b648 record', 'b648 --', 'b648 closing')


def _component_commit(s):
    return s.startswith('b648') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 25 and rows[24][:3] == ['b648', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b649_' in it] \
        and any(it.startswith('data/b648_table_pages.txt ') for it in j.get('items') or []) and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b648_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b648') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 649)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The sorry lines**', '**The two pages**', '**The census at v0.8**', '**The h2 row**', '**The re-cut order**',
                 '**The record lines**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b650')


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
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE, K.CEN8])


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and 'IN FULL ((R258)(2)' in t and 'THE RE-CUT ORDER ((R258)(6)' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R258) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the process listing at step zero: none running, no orphan, free memory read', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'].replace('### orphans: NONE', '### orphans: 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act: every one run but test_elab_reader_b634.py beneath the hold, '
     'clean but the page tests` glossary cases and test_chain_page_b638.py (4)-(7)', lambda S: tests_ok(S),
     lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b647_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay and PLACE-papers branch lists', lambda S: all(v == '' for v in S['push_lists'].values()),
     lambda S: put(S, 'push_lists', {'D:/relay': 'push-b647'})),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompts, every call`s result, the four prompts by header',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('(Split cites)', '(Split cite)'))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'tools/edit_route.py over the act`s command capture, read live', lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -i 's/a/b/' tools/b648_record.py")])),
    ('G-PEAKS-BANKED', 'the peaks bank: every attempt`s driver peak, tree peak and host low', lambda S: peaks_ok(S),
     lambda S: put(S, 'peaks', {'rows': []})),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line', lambda S: landed(S, 0, ['b647']), lambda S: _rl(S, 0, 1)),
    ('G-SORRY-BREACH-LINE', 'OPEN_TRAILS at the record-lines bank`s line', lambda S: landed(S, 1, ['11508']), lambda S: _rl(S, 1, 1)),
    ('G-CORRECTION-LINE', 'OPEN_TRAILS at the correction bank`s line', lambda S: landed(S, 0, ['G-NO-SORRY-MAIN'], key='cl_'),
     lambda S: _rl(S, 0, 1, key='cl_')),
    ('G-SORRY-CLASSIFIED', 'the classification bank: 37 lines, each one of three with its entry date; the four built ones RESTATED', lambda S: classified_ok(S),
     lambda S: _mut(S, 'cls', lambda d: d['rows'][0].update(entered=''))),
    ('G-NO-EDIT-BEFORE-ANSWER', 'the author`s answer`s time in the transcript against every kernel commit since b647`s face',
     lambda S: S['before_answer'], lambda S: put(S, 'before_answer', False)),
    ('G-QUARANTINES-MERGED', 'each quarantined kernel: main and its quarantine branch at the remote, its ERRATA.md on main', lambda S: quarantined_ok(S),
     lambda S: _mut(S, 'quar', lambda d: d['SIDE-kernel'].update(errata=''))),
    ('G-RESTATED-NAMED', 'the repairs bank and the watchdog`s rows: the four restated on branches, unmerged, their builds beneath the hold',
     lambda S: restated_named(S), lambda S: put(S, 'repairs', '')),
    ('G-NO-SORRY-MAIN', 'every kernel`s main by b647`s census rule, the quarantine branches outside it: no `sorry` in code', lambda S: no_sorry_main(S),
     lambda S: put(S, 'sorries', dict(S['sorries'], **{'SIDE-kernel': [('x.lean', 1, 'sorry')]}))),
    ('G-PAGES-EVERY-SENTENCE', 'the two page tables, before and after re-emission: every row taken by the instrument, the counts printed',
     lambda S: pages_every_sentence(S), lambda S: _mut(S, 'ta', lambda d: d['rows'][0].update(verdict='X'))),
    ('G-TEMPLATE-REPAIRS', 'the act`s commits touching tools/chain_page.py: the three repairs, the first two alone', lambda S: repairs_ok(S) and repairs_alone(S),
     lambda S: put(S, 'repair_files', dict(S['repair_files'], **{REPAIRS[0]: ['tools/chain_page.py', 'x']}))),
    ('G-PAGES-ALONE', 'the four page re-emissions in PLACE-papers, one page each', lambda S: pages_alone(S),
     lambda S: put(S, 'page_files', dict(S['page_files'], **{PAGE_COMMITS[0]: [K.PAGE, 'x']}))),
    ('G-PAGE-ARMS', 'the page arms and the frozen control after repair 3, the failing first run kept', lambda S: arms_c2_ok(S),
     lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2.', 'PASSING : 1 of 2.'))),
    ('G-GLOSSARY-ALIKE', 'the generator`s glossary block in both pages and the census at v0.8, byte for byte', lambda S: glossary_alike(S),
     lambda S: put(S, 'glossed', dict(S['glossed'], **{K.CEN8: ''}))),
    ('G-KERNEL-CITES', 'the unplaced kernels` bank: 20 rows, a cluster only by a served keystone or the terminal heads, the census itself not counted',
     lambda S: kcites_ok(S), lambda S: _mut(S, 'kc', lambda d: d['rows'][0].update(cluster='side'))),
    ('G-CENSUS-V08', 'v0.8 at PLACE-papers: its commit alone, three inserts against v0.7.1, the scanner clean, the edition bank`s digest, the columns and blanks',
     lambda S: census_ok(S), lambda S: put(S, 'cen8', S['cen8'] + 'x')),
    ('G-READER-SCORED', 'the compare bank and the hand reading: 2 of 2 by hand', lambda S: reader_ok(S), lambda S: put(S, 'cmp', dict(S['cmp'], hand=1))),
    ('G-READER-COMMAND-ONE-LINE', 'the reader`s command bank: one line, moving to C:\\reader_b648 itself', lambda S: reader_cmd_ok(S),
     lambda S: put(S, 'rcmd', 'cd C:\\reader_b648' + NL + S['rcmd'])),
    ('G-H2-ROW', 'the h2 row`s bank: both definitions quoted, the row taken, one re-cut proposed, SIDE-lv-conservation`s main where the row read it',
     lambda S: h2_ok(S), lambda S: put(S, 'lv_main', 'deadbee')),
    ('G-RECUT-ORDER', 'the re-cut order bank: the monograph 217, the companions 118, the two pages, every kernel', lambda S: recut_ok(S),
     lambda S: _mut(S, 'ro', lambda d: d['rows'].pop(0))),
    ('G-DEPOSIT-UNTOUCHED', 'relay data: no deposit-route bank of this act', lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b648_zenodo.json'])),
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS, OPEN_TRAILS, the two pages and v0.8', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the registry, the map, the census at v0.7.1, the monograph, the companions: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal', lambda S: kernels_untouched(S),
     lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b647`s tools, the instrument, the arm and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'act_root.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 6972e068 but the shared additive files, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 0,
     lambda S: put(S, 'prior_bad', ['data/b647_closing.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes, the pages and the census among them',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b648 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b648_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b647`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b647 closed' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-R258-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R258) END' in S['ferry'] and S['ot'].count('**(R258) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R258) ratified', '**(R2580) ratified'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 25th line, the root bank and its items', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'] + 'b649 x y' + NL)),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b648 AGREE, b648 written LF', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line', lambda S: bool(S['tj'].get('line')) and oline(S, S['tj']['line']) == S['REC'].TRAIL_HEAD(),
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b648 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b648_record.py agree', 'b648_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line, the author`s word on the re-cut order read from the answers bank',
     lambda S: ('**Next:** by the author’s word on the re-cut order (relay data/b648_author_answers.txt), the author chose') in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** by the author’s word', '**Next:** by the seat’s word'))),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b648')" in S['suite'] and "'data/b648_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b648_closing.py: the closing sentence in the rule`s words with the plain reads named; the sorry lines in full; the re-cut order',
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
    p = os.path.join(D, 'b648_seal_hashes.json')
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
    print('  written: b648_seal_hashes.json')
    return 0


def main():
    if SEAL:
        return seal()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b648 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### G-NO-SORRY-MAIN read %d kernels` mains; sorry in code: %s' % (len(S['sorries']), '; '.join(
        '%s %d (%s)' % (k, len(v), ', '.join('%s:%d' % (f, ln) for f, ln, _t in v)) for k, v in sorted(S['sorries'].items()) if v) or 'none'))
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
        out = os.path.join(D, 'b648_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b648_checks_postpush.txt' if pushed else 'b648_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b648_arms_prerun.txt', 'b648_lsr_prerun.json').replace('b648_checks', 'b648_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b648_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
