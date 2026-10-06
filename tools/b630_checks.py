# -*- coding: utf-8 -*-
"""b630_checks.py -- THE SUITE OF b630, UNDER (R240): THE NYMAN–BEURLING DISTANCES d_N² IN ARB BALLS BESIDE 2λ₁; NEW ROWS GRADED FROM
THE RULE WITH PROVENANCE; HELPER ROWS AS OBJECTS; THE PROBE HOLD; THE OUTBOUND-IDENTIFIER LINE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b630_checks.txt before the push and
### data/b630_checks_postpush.txt after it; `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is
### sealed, no table regenerated, its counts written to data/b630_arms_prerun.txt.
### ### Every remote is read once per run (OPEN_TRAILS :12703); G-LSREMOTE-ONE-PER-REPO runs last. The act-root chain is verified
### inside this suite alone.
### ### b629'S FOUR FAILING ARMS, REPAIRED IN THEIR SOURCES ((R240)'s Component 0):
###   G-TABLE-FINAL is keyed to the table's own rows: a grade may move only on a row the table itself marks provenance rule, no row gone;
###   G-WRITELIST-KINDS reads tracked files alone -- the diff of each repository against its pre-act head, never an untracked file;
###   G-INSTRUMENTS-UNEDITED carries the ordered edits: tools/terminal_table.py ((R240)(3)) and tools/chain_page.py ((R240)(5)) must
###       differ from their pre-act blobs and each lands with its test in one commit of its own under the act's subject; every other
###       instrument equals its blob;
###   G-STEPZERO-TESTS reads the test files that existed at the step-zero commit, so a test this act adds is not read as unrun.
### ### b628's local intake bank (relay data/b628_intake_crank_v0_5.txt) is read for its presence and its untracked state alone.
### ### The harness is b568's to b629's, carried from tools/b629_checks.py; the sources, predicates and arms are b630's.
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
from decimal import Decimal

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import terminal_table as TT   # noqa: E402,F401
import b616_claims as KC0     # noqa: E402
import b630_worklist as K     # noqa: E402

NL = chr(10)
PP, GS, KER = K.PP, K.GS, K.KER
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b630_registration_2026-10-05.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs=K.PRE_GS)
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd', 'platt-b626': 'e939c92',
        'cite-b628': '98b7668', 'nb-b629': 'aa17442'}
STEPZERO = K.STEPZERO
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA-E0-12C15C80'
FROZEN_ARM = 'G-GEN-OLD-LISTS-FROZEN-AT-84BAE29A-52822A5-GEN-84BAE29A'
FROZEN_PINS = ('84bae29a', '52822a5')
FROZEN_NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
FROZEN_PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
TABLE_FILES = K.TABLE_FILES
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
ORDERED = {'terminal_table.py': ('tools/test_terminal_table_b630.py', K.SUBJ['table']), 'chain_page.py': (K.PROBE_TEST, K.SUBJ['probe'])}
INST = ('b629_checks.py', 'b629_record.py', 'b629_closing.py', 'b629_tests.py', 'b627_margin.py', 'b604_record.py', 'b602_record.py',
        'b566_record.py', 'b565_record.py', 'b616_record.py', 'b616_claims.py', 'b611_claims.py', 'b558_record.py', 'e0_rule.py',
        'test_e0_rule.py', 'chain_page.py', 'g_chain_page.py', 'test_chain_page_b596.py', 'test_chain_page_b592.py', 'test_chain_page_b629.py',
        'banned_terms.py', 'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'test_push_gated.sh',
        'act_root.py', 'test_act_root.py', 'corr_row.py')
COUNT_CASE = r'^  \(\d+\) '
STD = {'propext', 'Classical.choice', 'Quot.sound'}


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b630')
            and 'data/b630_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section|SIDE-explicit-formula)/[^`\s]+)`', w)))


def untracked(repo, *paths):
    return [l[3:].strip() for l in git(repo, 'status', '--porcelain', '--untracked-files=all', '--', *paths)[1].split(NL) if l.startswith('?? ')]


def written_files():
    """### b629's G-WRITELIST-KINDS defect, repaired: tracked files alone -- each repository's diff against its pre-act head, working
    ### tree and commits; an untracked file (b628's local bank among them) is never read as written."""
    res = []
    for repo, name, pre in ((ROOT, 'relay', PRE['relay']), (PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs']),
                            (KER, 'SIDE-explicit-formula', K.PRE_KER)):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    if b is None:
        return []
    l = cr0(b if isinstance(b, bytes) else b.encode('utf-8')).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


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


def sources():
    import b630_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b630_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b630_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    tj = jl('terminal_table.json')
    S = dict(
        REC=REC, face=face, ferry=rd('b630_ferry.txt'), scan=rd('b630_ferry_scan.txt'), cens=rd('b630_census_stepzero.txt'),
        fcens=rd('b630_faces_census_stepzero.txt'), pins0=rd('b630_pins_stepzero.txt'), procs=rd('b630_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b629_closing.txt'), reads=rd('b630_reads.txt'), branches=rd('b630_branches.txt'), answers=rd('b630_author_answers.txt'),
        prerun=rd('b630_arms_prerun.txt'), rl=jl('b630_record_lines.json'), tests=jl('b630_tests_stepzero.json'), testst=rd('b630_tests_stepzero.txt'),
        stepzero_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', STEPZERO, 'tools/').split(NL)
                              if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        rr=jl('b630_table_rule_readings.json'), rrt=rd('b630_table_rule_readings.txt'),
        tt=jl('b630_table_test.json'), ttt=rd('b630_table_test.txt'), pt=jl('b630_probe_test.json'), ptt=rd('b630_probe_test.txt'),
        prof=jl('b630_probe_profile.json'), proft=rd('b630_probe_profile.txt'),
        inp=jl('b630_nb_inputs.json'), inpt=rd('b630_nb_inputs.txt'), bj=jl('b630_nb_bench.json'), bt=rd('b630_nb_bench.txt'),
        bb=raw(os.path.join(D, 'b630_nb_bench.txt')),
        table=tj, table_head=json.loads((blob(ROOT, 'HEAD:data/terminal_table.json') or b'{}').decode('utf-8')),
        local_present=os.path.exists(local),
        local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK),
        local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        nlist=rd(K.NEW_NODES_ZETA), oldlist=rd(K.NODES['zeta']), probe=rd(K.NEW_PROBE_ZETA),
        tblj=jl('b630_table_final.json'),
        pj={k: jl('b630_page_%s.json' % k) for k in ('zeta', 'chi')}, arms=rd('b630_page_arms.txt'),
        arj=jl('b630_act_root.json'), arj0=jl('b629_act_root.json'), art=rd('b630_act_root.txt'), rootsf=rd('act_roots.txt'),
        rpush=rd('b630_root_push_out.txt'), ppush=rd('b630_pp_root_push_out.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f)))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in REC.CURRENTS},
        pages={p: tri(PP, p, PRE['pp']) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b630_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b629*') for r in ('D:/relay', PP, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b630_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b630_mustnotexist.txt')), table_changed=None,
        fj=jl('b630_findings.json'), tj=jl('b630_trail.json'), sc=jl('b630_scores.json'), desk=rd('b630_desk_notes.txt'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files()
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    S['rfiles'] = {h: files_of(ROOT, h) for h, _s, _t in S['rlog']}
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S['gs_diff'] = sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip()))
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b630_', 'audit_b630_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [rd('act_roots.txt')] + [read(os.path.join(T, f)) for f in ORDERED] + [read(os.path.join(ROOT, v[0])) for v in ORDERED.values()]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
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
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import b626_record as R26
    import b627_record as R27
    X = {}
    zl, zp = S['REC'].zlist()
    X['gcp_zeta'] = GCP.arm(os.path.join(D, zl), os.path.join(SP, '_b630_gcp'), os.path.join(D, zp))
    X['gcp_chi'] = GCP.arm(os.path.join(D, K.NODES['chi']), os.path.join(SP, '_b630_gcp'), os.path.join(D, K.PROBE['chi']))
    rule = CP.E0
    CP.E0 = R26.e0_module(TC.RELAY_PIN)
    try:
        X['ctl'] = TC.control()
    finally:
        CP.E0 = rule
    X['ctl_arm'] = TC.ARM
    old = []
    pins, tc_c, tc_git = (TC.RELAY_PIN, TC.PRE_PP), TC.C, TC._GIT
    try:
        gen = R27.cp_module(FROZEN_PINS[0])
        gen.E0 = R26.e0_module(FROZEN_PINS[0])
        TC.RELAY_PIN, TC.PRE_PP = FROZEN_PINS
        TC.C, TC._GIT = gen, gen.git
        for k in ('zeta', 'chi'):
            lb, pb = blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_NODES[k])), blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_PROBE[k]))
            d = os.path.join(SP, '_b630_frozen')
            os.makedirs(d, exist_ok=True)
            lp, pp = os.path.join(d, FROZEN_NODES[k]), os.path.join(d, FROZEN_PROBE[k])
            open(lp, 'wb').write(lb or b'')
            open(pp, 'wb').write(pb or b'')
            rc, got = TC.regen(lp, pp)
            old.append(dict(list=FROZEN_NODES[k], rc=rc, equal=got is not None and got == cr0(blob(PP, '%s:%s' % (FROZEN_PINS[1], K.PNAME[k])))))
    except Exception as e:
        old.append(dict(list='raised %s' % type(e).__name__, rc=-1, equal=False))
    finally:
        TC.RELAY_PIN, TC.PRE_PP = pins
        TC.C, TC._GIT = tc_c, tc_git
    X['old_frozen'] = old
    try:
        import act_root as AR
        X['ar_verify'] = AR.verify(remote=KC0.remote_refs)
    except Exception as e:
        X['ar_verify'] = [('raised', type(e).__name__, [])]
    X['sorry_tokens'] = S['REC'].sorry_tokens('main')
    try:
        X['rule_of'] = {r['name']: TT.rule_reading(r.get('statement'), r['name']) for r in (S['table'].get('rows') or []) if r['name'] in K.RULE_ROWS}
    except AttributeError:
        X['rule_of'] = {}
    return X


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
    i = t.find(S['REC'].TRAIL_HEAD)
    return t[i:] if i >= 0 else ''


def poss(t):
    import b566_record as R6
    return R6.Q.poss(t)


def procs_ok(S):
    p = S['procs']
    rows = [l for l in p.split(NL) if re.match(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut|python|tail)\.exe', l)]
    return 'powershell.exe' in p and '### ORPHANS:' in p and '\\v1.0\\' in p and all('### STOPPED BY PID' in l for l in rows) \
        and 'tail' in p.split('### names matched:')[1].split(NL)[0]


def absent_ok(S):
    a, b, c = S['absent']
    return a is None and b is None and c is None and cr0(None) is None and cr0(b'') == b'' and lines_of(None) == []


def rline(S, i):
    x = (S['rl'].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need):
    x = rline(S, i)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


def alone(S, files, subject):
    """### the commit carrying exactly `files`, its subject beginning with the act's FULL subject form, the only one so titled."""
    c = [h for h, f in S['rfiles'].items() if f == sorted(files)]
    msg = {h: (s, t) for h, s, t in S['rlog']}
    return len(c) == 1 and msg[c[0]][0].startswith(subject) and S['lock_epoch'] is not None and msg[c[0]][1] > S['lock_epoch'] \
        and not [h for h, f in S['rfiles'].items() if set(f) & set(files) and h != c[0]] \
        and len([h for h, (s, _t) in msg.items() if s.startswith(subject)]) == 1


def count(text):
    cases = [l for l in (text or '').split(NL) if re.match(COUNT_CASE, l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b630 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    blocks = re.split(r'^### CALL ', a, flags=re.M)[1:]
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    if not m:
        return False
    if int(m.group(1)) == 0:
        return not heads and not blocks and '### NONE YET: no prompt has been put to the author in this act.' in a
    return int(m.group(1)) == len(heads) and all(x >= 2 for x in per) and len(per) == len(heads) \
        and len(blocks) == a.count('RESULT (transcript line') and '### NO RESULT' not in a \
        and all(S['REC'].answer_of(i) != 'no answer banked' for i in range(len(heads)))


def tests_ok(S):
    """### b629's G-STEPZERO-TESTS defect, repaired: the test files tracked at the step-zero commit, every one run and clean."""
    j = S['tests']
    names = S['stepzero_tests']
    nf = sorted(n for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == names and nf == [] and ('TEST FILES %d ; RUN %d ; NOT CLEAN 0' % (len(names), len(names))) in S['testst']


def instruments_ok(S):
    """### b629's G-INSTRUMENTS-UNEDITED, carrying the ordered edits: every instrument equals its blob at the pre-act relay head, but the
    ### two the ruling orders edited, which differ and land each with its test in one commit of its own under the act's subject."""
    for f, (pre, now) in S['inst'].items():
        if f in ORDERED:
            test, subj = ORDERED[f]
            if pre is None or now is None or pre == now or not alone(S, ['tools/' + f, test], subj):
                return False
        elif pre is None or pre != now:
            return False
    return True


def local_ok(S):
    return S['local_present'] and S['local_log'] == '' and S['local_index'] == '' and S['local_status'].startswith('??')


def rule_readings_ok(S):
    j, t = S['rr'], S['rrt']
    rows = [l for l in t.split(NL) if l.startswith('  SIDE-') or re.match(r'^  [A-Za-z][\w-]* \| ', l)]
    return bool(j) and j.get('ungraded') == len(rows) and j.get('readable') is not None and 0 < j['readable'] <= j['ungraded'] < j.get('rows', 0) \
        and sum(j.get('kinds', {}).values()) == j['ungraded'] and 'NOT APPLIED' in t


def provenance_ok(S):
    """### the table on disk: every row marked cell, rule or none; a row with grade cells reads cell; the thirteen rows of v0.24 read rule
    ### with the grade the suite recomputes from their statement by the table's own rule; every other row without cells reads none and
    ### UNGRADED; the three helper defs DEF, rhoFun_bound DERIVES."""
    rows = S['table'].get('rows') or []
    if not rows:
        return False
    for r in rows:
        p = r.get('provenance')
        if p not in ('cell', 'rule', 'none'):
            return False
        if r.get('grade_cells') and p != 'cell':
            return False
        if r['name'] in K.RULE_ROWS:
            if p != 'rule' or (S['rule_of'].get(r['name']) or (None, None))[1] != r['grade']:
                return False
        elif not r.get('grade_cells') and (p != 'none' or r['grade'] != 'UNGRADED'):
            return False
    g = {r['name']: r['grade'] for r in rows if r['name'] in K.RULE_ROWS}
    return len(g) == 13 and all(g.get(n) == ('DEF' if k == 'def' else 'DERIVES') for n, k, _w in K.HELPERS)


def nodes_new_ok(S):
    n, o = S['nlist'].split(NL), S['oldlist'].split(NL)
    recs = [l.split(' | ')[0] for l in n if l and not l.startswith('#')]
    return bool(S['nlist']) and '# pin: v0.24' in n and all(l in n for l in o if l) \
        and [l for l in n if l.startswith('# backmatter: ')] == [l for l in o if l.startswith('# backmatter: ')] \
        and recs[-len(K.HELPERS):] == [h[0] for h in K.HELPERS]


def profile_ok(S):
    j = S['prof']
    return bool(j) and j.get('rc') == 0 and (j.get('peak_child') or 0) > 0 and j.get('free_before', 0) >= K.HOLD_MB and bool(S['probe']) \
        and '### ### **PEAK OF THE PROBE`S CHILDREN' in S['proft']


def probe_edit_ok(S):
    pre, now = S['inst']['chain_page.py']
    t = (now or b'').decode('utf-8', 'replace')
    return pre is not None and now is not None and pre != now and 'free memory before the lean call' in t and 'return 4, None, None, log' in t


def inputs_ok(S):
    j, t = S['inp'], S['inpt']
    r = j.get('reads') or {}
    return sorted(r) == sorted(k for k, _u in K.REGISTRY_READS) and all(v.get('bytes', 0) > 0 and v.get('entries') for v in r.values()) \
        and all(('the recollection (the ferry`s, printed beside, not copied): %s' % K.RECOLLECTION[k]) in t for k in r) \
        and j.get('statement_ok') is True and j.get('identity') is True and j.get('prec') == K.PREC and j.get('n_cap') == K.N_CAP


def outbound_ok(S):
    c = S['inp'].get('commands') or ''
    lines = [l for l in c.split(NL) if l.strip()]
    return len(lines) == len(K.REGISTRY_READS) and not re.search(r'@|mailto|User-Agent|\s-A\s|\s-H\s|--header|--user-agent', c) \
        and all(u in c for _k, u in K.REGISTRY_READS)


def _ball(mid, rad):
    return Decimal(mid) - Decimal(rad), Decimal(mid) + Decimal(rad)


def bench_rows(S):
    out = []
    for l in S['bt'].split(NL):
        f = [x.strip() for x in l.split(' | ')]
        if len(f) == 8 and f[0].isdigit():
            out.append(dict(N=int(f[0]), d2=f[1], rad=f[2], above=f[5] == 'yes', six=f[7] == 'yes'))
    return out


def bench_recomputed(S):
    """### from the bench bank's own rows: N_max by the six-digit column; the certified decrease of d_N² by its printed midpoint and radius
    ### (lower of N against upper of N+1); the steps and products the bank names."""
    rows = bench_rows(S)
    if not rows:
        return None
    nmax = max([r['N'] for r in rows if r['six']] or [0])
    mono = [a['N'] for a, b in zip(rows, rows[1:]) if a['N'] < nmax and not (_ball(a['d2'], a['rad'])[0] - _ball(b['d2'], b['rad'])[1] >= 0)]
    above = [r['N'] for r in rows if 2 <= r['N'] <= nmax and not r['above']]
    return dict(nmax=nmax, mono=mono, above=above, n=len(rows))


def bench_ok(S):
    j, b = S['bj'], S['bb']
    rc = bench_recomputed(S)
    return bool(j) and b is not None and j.get('same') is True and len(j.get('runs') or []) == 2 and all(x['rc'] == 0 for x in j['runs']) \
        and hashlib.sha256(b).hexdigest() == j.get('sha256') and rc is not None and rc['n'] == K.N_CAP and rc['nmax'] == j.get('n_max')


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h64_ok(S, k):
    rc, j = bench_recomputed(S), S['bj']
    if rc is None:
        return False
    if k == 'H64a':
        want = 'HOLDS' if rc['mono'] == [] else 'REFUTED'
    elif k == 'H64b':
        want = 'HOLDS' if rc['nmax'] >= 20 else 'REFUTED'
    elif k == 'H64c':
        want = 'HOLDS' if rc['above'] == [] else 'REFUTED'
    else:
        want = 'HOLDS' if j.get('same') is True and all(x['rc'] == 0 for x in j.get('runs') or [{'rc': 1}]) else 'REFUTED'
    return _h(S, k, want)


def page_zeta_ok(S):
    j = S['pj']['zeta']
    a, b, c = S['pages'][PAGE]
    commits = [h for h, f in S['pp_files'].items() if PAGE in f]
    t = (c or b'').decode('utf-8')
    return j.get('rc') == 0 and j.get('changed') is True and a is not None and a == c and hashlib.sha256(c).hexdigest() == j.get('sha256') \
        and bool(S['probe']) and all(S['pp_files'][h] == [PAGE] for h in commits) and len(commits) == 1 \
        and 'generated at SIDE-explicit-formula v0.24 = ' in t and all(('`%s`' % n) in t for n, _k, _w in K.HELPERS) \
        and not (j.get('grade_cells_moved') or [])


def table_final_ok(S):
    """### b629's G-TABLE-FINAL defect, repaired: keyed to the table's own rows -- a grade may move only on a row the table marks
    ### provenance rule; no row gone."""
    t = S['tblj']
    rule = set(r['name'] for r in (S['table'].get('rows') or []) if r.get('provenance') == 'rule')
    return bool(t) and t.get('rc') == 0 and bool(rule) and all(n in rule for n in t.get('grade_moved') or []) and not t.get('gone')


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('PASSING : 2 of 2.**') in t.split('PAGE ARMS PASSING : 2 of 2.**')[-1]


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 7 and rows[6][:3] == ['b630', j.get('root'), j0.get('root')] and len(rows[6]) == 3 \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and len(j['reads']['heads']) == 38 and S['roots_pre'] is not None and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it]


def midpush_ok(S):
    heads = (S['arj'].get('reads') or {}).get('heads') or {}
    m1 = re.search(r'push_gated: main read back at the remote: (\w+)', S['rpush'])
    m2 = re.search(r'push_gated: main read back at the remote: (\w+)', S['ppush'])
    return bool(m1 and m2) and heads.get('relay') == m1.group(1) and heads.get('PLACE-papers') == m2.group(1) \
        and (heads.get('SIDE-explicit-formula') or '').startswith(K.PRE_KER)


def verify_ok(S):
    v = S['ar_verify'] or []
    return [x[0] for x in v] == ['b624', 'b625', 'b626', 'b627', 'b628', 'b629', 'b630'] and all(x[1] == 'AGREE' for x in v)


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 24]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The Nyman–Beurling distances d_N²') \
        and all(x in tail for x in ('**The bench**', 'a T3/T4 bench with no claim', '**The table**', '**The probe hold**',
                                    '**The record lines and the root.**', '**The scores.**', '**Read in mutual light**', 'strengthens',
                                    '**Next.**', 'b631', 'nothing is inferred'))


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE', 'HOLDS') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def kernels_untouched(S):
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and len(f) == 11 and all(k in n and n[k] == f[k] for k in f) and all(n[k][0].startswith(v) for k, v in S['REC'].KERN_PIN.items()) \
        and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') and S['gs_diff'] == [] and n.get('SIDE-explicit-formula', [''])[0] == K.PRE_KER


def corpus_scope(S):
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if S['pj'][k].get('changed') or any(K.PNAME[k] in f for f in S['pp_files'].values())]
    return S['pp_changed'] == sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages))


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


READ_NEEDLES = ('OPEN_TRAILS.md @ 655e2d24', 'FINDINGS.md @ 655e2d24', 'NymanBeurling.lean @ aa17442f', 'Keiper.lean @ 914c4137',
                'KeiperSign.lean @ 914c4137', 'tools/terminal_table.py @ 89fa8fd0', 'tools/chain_page.py @ 89fa8fd0',
                'tools/b627_margin.py @ 89fa8fd0', 'data/b629_defects.txt @ 89fa8fd0', 'data/b629_closing_push_out.txt @ 63433a93',
                ':11864 ', ':12228 ', ':12354 ', ':12356 ', ':12799 ', ':12893 ', ':12895 ', ':13119 ', ':13121 ', ':13123 ', ':94 ', ':101 ',
                ':239 ', '### the local intake bank`s state: ?? data/b628_intake_crank_v0_5.txt')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R240) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + NL + ' 11 22 lean.exe  lean x')),
    ('G-STEPZERO-TESTS', 'the step-zero test bank against the test files tracked at the step-zero commit: every one run and clean', lambda S: tests_ok(S),
     lambda S: put(S, 'stepzero_tests', S['stepzero_tests'] + ['test_x.py'])),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and all(t > S['lock_epoch'] for h, s, t in S['rlog'] if h[:7] != STEPZERO[:7]),
     lambda S: put(put(S, 'lock_epoch', 4 * 10 ** 9), 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b629`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b629' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [h[:8] for h, s, t in S['rlog'] if t <= S['lock_epoch']] == [STEPZERO[:8]],
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-R240-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R240) END' in S['ferry'] and S['ot'].count('**(R240) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R240) ratified', '**(R2400) ratified'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'].replace(':12893 ', ':12892 '))),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompt headers, each prompt`s options, each call`s result, every answer read back by the record tool',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('prompt(s)', 'prompts'))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and 'PRE-SEAL (R202)(3) READING' in S['prerun'] and ('ARMS RUN : %d.' % len(ARMS)) in S['prerun']
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 10 ** 12) < S['lock_epoch'],
     lambda S: put(S, 'prerun', S['prerun'].replace('PRE-SEAL', 'POST-SEAL'))),
    ('G-PUSHOUT-COMMITTED', 'relay 63433a93`s files', lambda S: S['pushout'][0] == ['data/b629_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', ([], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b629') == 6, lambda S: put(S, 'push_lists', {'x': 'push-b629'})),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads, nb-b629 among them', lambda S: all(S['kbranches'].get(b, '').startswith(v) for b, v in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'nb-b629': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80, every PLACE-papers read at ba5f0ea and the E0 rule`s blob at 12c15c80',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] + '-E0-12C15C80' == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(x, ok=False) for x in S['ctl']])),
    (FROZEN_ARM, 'b622`s lists with every relay read at 84bae29a, the E0 rule`s and the generator`s blobs at 84bae29a, against the pages at 52822a5',
     lambda S: len(S['old_frozen']) == 2 and all(x.get('rc') == 0 and x.get('equal') is True for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [dict(x, equal=False) for x in S['old_frozen']])),
    ('G-INSTRUMENTS-UNEDITED', 'b629`s tools, the shared tools, the generator and its tests, the table generator, the seal, the gates, act_root.py and the row writer against 89fa8fd0, the two ordered edits each landed with its test alone',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'e0_rule.py': (b'a', b'b')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', None, None))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b629`s weight', lambda S: landed(S, 0, ('(:7635)', 'aa17442', 'nb-b629', '2002-02-15', '830d2974', '219ae8b5')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=[dict(rline(S, 0), line=1)] + (S['rl'].get('lines') or [])[1:]))),
    ('G-OUTBOUND-LINE', 'OPEN_TRAILS at the banked line: no outbound identifier beneath :11864', lambda S: landed(S, 1, ('(:11864)', 'outbound header, URL or payload', 'polite pool is declined')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=[rline(S, 0), dict(rline(S, 1), line=1)] + (S['rl'].get('lines') or [])[2:]))),
    ('G-PROVENANCE-LINE', 'OPEN_TRAILS at the banked line: the provenance clause', lambda S: landed(S, 2, ('provenance', 'mark rule', '75227e9c', '1799')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[:2] + [dict(rline(S, 2), line=1)] + (S['rl'].get('lines') or [])[3:]))),
    ('G-HELPER-LINE', 'OPEN_TRAILS at the banked line: the helper clause, corrected', lambda S: landed(S, 3, ('defs or instances', 'a helper that is a theorem is a theorem', 'rhoFun_bound')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[:3] + [dict(rline(S, 3), line=1)] + (S['rl'].get('lines') or [])[4:]))),
    ('G-NYMAN-ITEM-LINE', 'OPEN_TRAILS at the banked line: the Nyman registry item', lambda S: landed(S, 4, ('(:12893)', 'Nyman', 'Uppsala, 1950')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[:4] + [dict(rline(S, 4), line=1)] + (S['rl'].get('lines') or [])[5:]))),
    ('G-RULE-GRADES-WO-LINE', 'OPEN_TRAILS at the banked line: W-ORD-TABLE-RULE-GRADES, priced, with the ungraded count', lambda S: landed(S, 5, (
        'W-ORD-TABLE-RULE-GRADES', 'nine-tenths', 'second reader', str(S['rr'].get('ungraded', '#')))),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[:5] + [dict(rline(S, 5), line=1)]))),
    ('G-RULE-READINGS-BANKED', 'the rule-readings bank: its counts against its own rows, not applied', lambda S: rule_readings_ok(S),
     lambda S: put(S, 'rr', dict(S['rr'], ungraded=-1))),
    ('G-TABLE-PROVENANCE', 'the table on disk: provenance per row, the thirteen recomputed from their statements by the table`s rule, the helpers', lambda S: provenance_ok(S),
     lambda S: put(S, 'table', dict(S['table'], rows=[dict(r, provenance='cell') for r in S['table'].get('rows') or []]))),
    ('G-TABLE-TEST-COUNTED', 'the provenance test`s bank counted here by its case pattern, every case passing', lambda S: S['tt'].get('rc') == 0
     and count(S['ttt']) == (S['tt'].get('cases'), S['tt'].get('passing')) and S['tt'].get('cases', 0) >= 2 and S['tt']['cases'] == S['tt']['passing'],
     lambda S: put(S, 'ttt', S['ttt'] + NL + '  (99) x ### FAIL')),
    ('G-TABLE-EDIT-ALONE', 'relay`s log: tools/terminal_table.py with its test in one commit of its own after the lock, its subject the act`s full form',
     lambda S: alone(S, ['tools/terminal_table.py', 'tools/test_terminal_table_b630.py'], K.SUBJ['table']),
     lambda S: put(S, 'rfiles', {h: (f + ['x'] if 'tools/terminal_table.py' in f else f) for h, f in S['rfiles'].items()})),
    ('G-NODES-NEW', 'b630`s ζ list: b629`s lines and backmatter unchanged, the four helpers appended', lambda S: nodes_new_ok(S),
     lambda S: put(S, 'nlist', S['nlist'].replace(K.HELPERS[-1][0] + ' |', 'X |'))),
    ('G-PROBE-EDIT', 'tools/chain_page.py at HEAD against 89fa8fd0: changed, the read and the refusal present', lambda S: probe_edit_ok(S),
     lambda S: put(S, 'inst', dict(S['inst'], **{'chain_page.py': (b'x', b'x')}))),
    ('G-PROBE-TEST-COUNTED', 'the probe-hold test`s bank counted here by its case pattern, every case passing', lambda S: S['pt'].get('rc') == 0
     and count(S['ptt']) == (S['pt'].get('cases'), S['pt'].get('passing')) and S['pt'].get('cases', 0) >= 2 and S['pt']['cases'] == S['pt']['passing'],
     lambda S: put(S, 'ptt', S['ptt'] + NL + '  (99) x ### FAIL')),
    ('G-PROBE-EDIT-ALONE', 'relay`s log: tools/chain_page.py with its test in one commit of its own after the lock, its subject the act`s full form',
     lambda S: alone(S, ['tools/chain_page.py', K.PROBE_TEST], K.SUBJ['probe']),
     lambda S: put(S, 'rfiles', {h: (f + ['x'] if 'tools/chain_page.py' in f else f) for h, f in S['rfiles'].items()})),
    ('G-PROBE-PROFILE-BANKED', 'the profile bank: one probe run above the hold, its children`s peak, its output banked', lambda S: profile_ok(S),
     lambda S: put(S, 'prof', dict(S['prof'], peak_child=0))),
    ('G-NB-INPUTS-BANKED', 'the inputs bank: both records read with entries, the recollection beside them, λ₁`s statement as expected, the identity, the precision and the cap',
     lambda S: inputs_ok(S), lambda S: put(S, 'inp', dict(S['inp'], identity=False))),
    ('G-OUTBOUND-IDENTIFIER-ABSENT', 'the registry command lines: one per read, no header, no address', lambda S: outbound_ok(S),
     lambda S: put(S, 'inp', dict(S['inp'], commands=(S['inp'].get('commands') or '') + ' -H x'))),
    ('G-NB-BENCH-REPRODUCED', 'the bench bank and its json: two runs exit 0 and byte for byte, the bank`s digest, its rows to the cap, N_max recomputed from its own column',
     lambda S: bench_ok(S), lambda S: put(S, 'bj', dict(S['bj'], same=False))),
    ('G-H64A-SCORED', 'H64a recomputed from the bench bank`s midpoints and radii, against the scores and the desk', lambda S: h64_ok(S, 'H64a'), lambda S: _sc(S, 'H64a')),
    ('G-H64B-SCORED', 'H64b recomputed from the bench bank`s six-digit column, against the scores and the desk', lambda S: h64_ok(S, 'H64b'), lambda S: _sc(S, 'H64b')),
    ('G-H64C-SCORED', 'H64c recomputed from the bench bank`s certified comparison, against the scores and the desk', lambda S: h64_ok(S, 'H64c'), lambda S: _sc(S, 'H64c')),
    ('G-H64D-SCORED', 'H64d from the two runs, against the scores and the desk', lambda S: h64_ok(S, 'H64d'), lambda S: _sc(S, 'H64d')),
    ('G-PAGE-ZETA-HELPERS', 'the ζ page at v0.24 on disk and at HEAD against its bank, its probe banked, the helpers printed, no grade cell moved, committed alone',
     lambda S: page_zeta_ok(S), lambda S: put(S, 'pj', dict(S['pj'], zeta=dict(S['pj']['zeta'], changed=False)))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from the list and probe in force against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b622`s list and b603`s v0.21 probe against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank: both page arms and the frozen control', lambda S: arms_ok(S['arms']),
     lambda S: put(S, 'arms', S['arms'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-TABLE-FINAL', 'the final table bank keyed to the table`s own rows: a grade moved only where the table marks provenance rule, no row gone',
     lambda S: table_final_ok(S), lambda S: put(S, 'tblj', dict(S['tblj'], grade_moved=(S['tblj'].get('grade_moved') or []) + ['SIDEExplicitFormula.X']))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s b630 line, the root bank and its items: previous b629`s root, 38 repositories, the file a true prefix extension',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b631 x y' + NL)),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay and PLACE-papers heads against the read-backs of the pushes before it, the kernel at v0.24', lambda S: midpush_ok(S),
     lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed by this suite, one remote read per repository: b624 to b630 AGREE', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', [(a, 'DISAGREE', w) for a, v, w in S['ar_verify']])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous', lambda S: bool(S['arj'])
     and ('**Act root:** b630 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-TERMINALS', 'this act`s trail record: no terminal yet for the Dedekind instance, its two premises read from :12895', lambda S: (
        'the two premises of (R213)(3)(d), from OPEN_TRAILS :12895: the trivial character’s pole term, the Euler factors at p | q' in trail(S)),
     lambda S: put(S, 'ot', S['ot'].replace('the trivial character’s pole term, the Euler factors at p | q', 'x'))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the prompts', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**Prompts to the author:** 2 ' in trail(S) and 'no answer banked' not in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Prompts to the author:** 2 ', '**Prompts to the author:** 0 '))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b631, W-ORD-DEDEKIND-INSTANCE' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b631, W-ORD-DEDEKIND-INSTANCE', 'b632'))),
    ('G-CURRENTS-UNEDITED', 'the current versions, the census, REGISTRY, ERRATA, README, SPIRAL_MAP and the sieve on disk and at HEAD against 655e2d2',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'README.md': (b'a', b'b', b'a')}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the ledger appends, its banks, its tools, the two edited instruments and their tests, the roots file',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-KERNELS-UNTOUCHED', 'every kernel, the explicit-formula kernel among them: main, tags by peel, branches and status against the face; SIDE-global-section unchanged',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-kernel': ['0000000', {}, [], '']}))),
    ('G-SORRY-TOKENS', 'the explicit-formula kernel`s main, comments stripped: no sorry token', lambda S: S['sorry_tokens'] == 0,
     lambda S: put(S, 'sorry_tokens', 1)),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('x', 'y', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b630_record.py'): S['tooltext'].get(os.path.join(T, 'b630_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                                if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 89fa8fd0, by blob id, the roots file read by G-ACTROOT-BANKED', lambda S: S['prior_n'] > 0 and S['prior_bad'] == [],
     lambda S: put(S, 'prior_bad', ['data/x'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers and the pages', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['README.md'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-UNMOVED', 'the suite`s own regeneration against the committed table: no row added or gone and no grade cell moved', lambda S: S['table_changed'] == [],
     lambda S: put(S, 'table_changed', [['x']])),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present on disk, in no relay commit of any branch, not in the index, untracked', lambda S: local_ok(S),
     lambda S: put(S, 'local_log', 'abc1234')),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b630')" in S['suite'] and "'data/b630_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, the act-root arm`s included, read after every other arm has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
]


def regenerate():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def main():
    import time
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b630 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID) else regenerate()
    if RERUN:
        d = jl('terminal_table_diff.json')
        S['table_changed'] = [list(x) for x in (d.get('changed') or [])] + [list(x) if isinstance(x, list) else [x] for x in (d.get('added') or []) + (d.get('gone') or [])]
    elif not (PRERUN or MID):
        S['table_changed'] = ([list(x) for x in (gen_diff.get('changed') or [])] + [list(x) if isinstance(x, list) else [x] for x in
                                                                                    (gen_diff.get('added') or []) + (gen_diff.get('gone') or [])]) \
            if rc_gen == 0 and 'changed' in gen_diff else None
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    av = S['ar_verify']
    rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
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
    bk = bench_recomputed(S)
    rec('  ### the bench recomputed from its own bank: %s' % (bk or 'NO BANK'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this run, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if not (RERUN or PRERUN or MID):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b630_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b630_checks_postpush.txt' if pushed else 'b630_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b630_arms_prerun.txt', 'b630_lsr_prerun.json').replace('b630_checks', 'b630_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b630_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
