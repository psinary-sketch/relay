# -*- coding: utf-8 -*-
"""b625_checks.py -- THE SUITE OF b625, UNDER (R235): THE 2/3 THEOREM`S CLOSURE LISTED AND HELD; THE 33 LEDGER-AGAINST-RULE NODES
CLASSED UNDER THE DOMAIN-CONDITION CRITERION; THE ROOT`S LIST WIDENED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b625_checks.txt before the push and
### data/b625_checks_postpush.txt after it; `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is
### sealed, no table regenerated, its counts written to data/b625_arms_prerun.txt.
### ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs); G-LSREMOTE-ONE-PER-REPO runs last; the
### act-root arm (G-ACTROOT-VERIFY) recomputes the chain with the suite's own remote reads.
### ### b624'S DEFECTS' SOURCES, REPAIRED ((R235)'s Component 0): (c) the frozen arm re-pinned to the post-b624 pages -- b622's
### lists re-emitted with every relay read at 84bae29a, every PLACE-papers read at 52822a5 AND the E0 rule loaded from its blob at
### 84bae29a, so no edit this act makes to the generator's inputs reaches it (G-GEN-OLD-LISTS-FROZEN-AT-84BAE29A-52822A5); (d) every
### head compared with a ledger line is compared after the ledger's own possessive conversion (Q.poss); (e) a control's bank line is
### read by the record tool's own pattern (b625_record.CONTROL_RE), written beside the format that prints it.
### ### The harness is b568's to b624's, carried from tools/b624_checks.py; the sources, predicates and arms are b625's.
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
import b616_claims as KC0     # noqa: E402
import b625_worklist as K     # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b625_registration_2026-10-05.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs='3528bcf')
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO, NSREPAIR = K.STEPZERO, K.NSREPAIR
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
FROZEN_ARM = 'G-GEN-OLD-LISTS-FROZEN-AT-84BAE29A-52822A5'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'
FROZEN_PINS = (K.PRE_RELAY, K.PRE_PP)
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
INST = ('b624_checks.py', 'b624_record.py', 'b604_record.py', 'b602_record.py', 'b566_record.py', 'b565_record.py', 'b616_record.py',
        'b616_claims.py', 'b611_claims.py', 'b558_record.py', 'chain_page.py', 'test_chain_page_b596.py', 'g_chain_page.py', 'banned_terms.py',
        'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'test_push_gated.sh')
E0_SUBJECT = 'b625 (R235)(2)'
ROOT_SUBJECT = 'b625 (R235)(3)'
NS_SUBJECT = 'b625 (R235) Component 0'
COUNT_CASE = r'^  \(\d+\) '


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b625')
            and 'data/b625_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def written_files(lock_epoch):
    out = set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay']).split(NL) if x.strip())
    out |= set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay'], 'HEAD').split(NL) if x.strip())
    for p in untracked(ROOT, 'data', 'tools'):
        try:
            if os.path.getmtime(os.path.join(ROOT, p)) > lock_epoch - 3 * 3600:
                out.add(p)
        except OSError:
            pass
    res = ['relay/' + x for x in out]
    for repo, name, pre in ((PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        if repo == PP:
            ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1'))
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
    import b625_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b625_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b625_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b625_ferry.txt'), scan=rd('b625_ferry_scan.txt'), cens=rd('b625_census_stepzero.txt'),
        fcens=rd('b625_faces_census_stepzero.txt'), pins0=rd('b625_pins_stepzero.txt'), procs=rd('b625_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b624_closing.txt'), reads=rd('b625_reads.txt'), branches=rd('b625_branches.txt'), answers=rd('b625_author_answers.txt'),
        prerun=rd('b625_arms_prerun.txt'), rl=jl('b625_record_lines.json'), co=jl('b625_corrections.json'),
        svt=rd('b625_section_vars.txt'), svj=jl('b625_section_vars.json'),
        e0b=rd('b625_e0_before.txt'), e0d=rd('b625_e0_diff.txt'), e0t=rd('b625_e0_test.txt'), e0j=jl('b625_e0_test.json'),
        clj=jl('b625_e0_classes.json'), clt=rd('b625_e0_classes.txt'), nodesj=jl('b625_e0_nodes.json'), nodest=rd('b625_e0_nodes.txt'),
        cloj=jl('b625_closure.json'), clot=rd('b625_closure.txt'), tblj=jl('b625_table.json'),
        pj={k: jl('b625_page_%s.json' % k) for k in ('zeta', 'chi')}, arms=rd('b625_page_arms.txt'),
        rtt=rd('b625_root_test.txt'), rtj=jl('b625_root_test.json'), arj=jl('b625_act_root.json'), art=rd('b625_act_root.txt'),
        arj0=jl('b624_act_root.json'), rootsf=rd('act_roots.txt'), armj=jl('b625_root_arm.json'),
        rpush=rd('b625_root_push_out.txt'), ppush=rd('b625_pp_root_push_out.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        e0files={p: tri(ROOT, p, PRE['relay']) for p in K.E0_FILES},
        rootfiles={p: tri(ROOT, p, PRE['relay']) for p in K.ROOT_FILES},
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        nsrep=(files_of(ROOT, NSREPAIR), gs(ROOT, 'log', '-1', '--format=%s', NSREPAIR), gs(ROOT, 'diff', NSREPAIR + '^', NSREPAIR, '--', 'tools/b624_worklist.py')),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f)))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in REC.CURRENTS},
        pages={p: tri(PP, p, PRE['pp']) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        kern_face=(jl('b625_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b624*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b625_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b625_mustnotexist.txt')), table_changed=None,
        fj=jl('b625_findings.json'), tj=jl('b625_trail.json'), sc=jl('b625_scores.json'), desk=rd('b625_desk_notes.txt'),
        lsr=None,
        rlog=[(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    S['rfiles'] = {h: files_of(ROOT, h) for h, _s in S['rlog']}
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S['pp_remote'] = KC0.remote_refs(PP).get('refs/heads/main', '')
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b625_', 'audit_b625_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [rd('act_roots.txt')]
    for p, (now, _b, _h) in list(S['e0files'].items()) + list(S['rootfiles'].items()):
        pub.append((now or b'').decode('utf-8', 'replace'))
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
    X = {}
    for k in ('zeta', 'chi'):
        X['gcp_' + k] = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b625_gcp'), os.path.join(D, K.PROBE[k]))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    # ### b624's defect (c), repaired: b622's lists re-emitted with every relay read at 84bae29a, every PLACE-papers read at 52822a5
    # ### AND the E0 rule loaded from its blob at 84bae29a, against the pages at 52822a5 -- no edit of this act reaches the arm
    old = []
    pins, rule = (TC.RELAY_PIN, TC.PRE_PP), CP.E0
    TC.RELAY_PIN, TC.PRE_PP = FROZEN_PINS
    CP.E0 = S['REC'].e0_module(PRE['relay'])
    try:
        for k in ('zeta', 'chi'):
            lb, pb = blob(ROOT, '%s:data/%s' % (PRE['relay'], K.NODES[k])), blob(ROOT, '%s:data/%s' % (PRE['relay'], K.PROBE[k]))
            d = os.path.join(SP, '_b625_frozen')
            os.makedirs(d, exist_ok=True)
            lp, pp = os.path.join(d, K.NODES[k]), os.path.join(d, K.PROBE[k])
            open(lp, 'wb').write(lb or b'')
            open(pp, 'wb').write(pb or b'')
            rc, got = TC.regen(lp, pp)
            old.append(dict(list=K.NODES[k], rc=rc, equal=got is not None and got == cr0(blob(PP, '%s:%s' % (FROZEN_PINS[1], K.PNAME[k])))))
    finally:
        TC.RELAY_PIN, TC.PRE_PP = pins
        CP.E0 = rule
    X['old_frozen'] = old
    try:
        oldr, newr = S['REC'].e0_module(PRE['relay']), S['REC'].e0_module(None)
        seen, _p = S['REC']._headers(newr)
        heads = {}
        for (k, n), (h, kind) in seen.items():
            heads.setdefault(n, (h, kind))
        X['moved_now'] = sorted(n for n, (h, kind) in heads.items()
                                if oldr.grade(h, 'theorem' if kind == 'theorem' else 'def')[0] != newr.grade(h, 'theorem' if kind == 'theorem' else 'def')[0])
        X['nodes_now'] = len(heads)
    except Exception as e:
        X['moved_now'], X['nodes_now'] = None, 'raised %s' % type(e).__name__
    try:
        import act_root as AR
        X['ar_verify'] = AR.verify(remote=KC0.remote_refs)
    except Exception as e:
        X['ar_verify'] = [('raised', type(e).__name__, [])]
    X['e0_stat'] = gs(ROOT, 'diff', '--stat', PRE['relay'], '--', *K.E0_FILES).split(NL)[-1].strip()
    X['the33'] = sorted(x['name'] for x in json.loads((blob(ROOT, '%s:data/b624_e0_nodes.json' % PRE['relay']) or b'{}').decode('utf-8')).get('disagreements', []))
    X['vendor_branches'] = sorted(b for b in S['kbranches'] if 'vendor' in b and 'b625' in b)
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
    """### b624's defect (d), repaired: the banked head compared with the ledger's line after the ledger's own possessive conversion."""
    x = rline(S, i)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


def corrections_ok(S):
    ls = S['co'].get('lines') or []
    out = []
    for (f, n), x in zip(K.INSERT_CELLS, ls):
        rows = (S['find'] if f == 'FINDINGS.md' else S['ot']).split(NL)
        i = x.get('line', 0)
        out.append(x.get('file') == f and 0 < i < len(rows) and rows[i - 1].startswith(poss(x.get('head', '\x00')))
                   and rows[i].startswith('SUPERSEDES %s :%d for `finsetSum_insert`: DERIVES' % ('FINDINGS' if f == 'FINDINGS.md' else 'OPEN_TRAILS', n)))
    c = [h for h, f in S['pp_files'].items() if f == ['FINDINGS.md', 'OPEN_TRAILS.md'] and dict(S['pp_log'])[h].startswith('b625 (R235)(2): the correction')]
    return len(ls) == 4 and len(out) == 4 and all(out) and len(c) == 1


def alone(S, files, prefix):
    c = [h for h, f in S['rfiles'].items() if f == sorted(files)]
    msg = {h: s for h, s in S['rlog']}
    return len(c) == 1 and msg[c[0]].split(' ', 1)[1].startswith(prefix) and S['lock_epoch'] is not None \
        and int(msg[c[0]].split(' ', 1)[0]) > S['lock_epoch'] and not [h for h, f in S['rfiles'].items() if set(f) & set(files) and h != c[0]]


def count(text):
    cases = [l for l in (text or '').split(NL) if re.match(COUNT_CASE, l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


def secvars_ok(S):
    j, t = S['svj'], S['svt']
    m = re.search(r'LINES (\d+) ; PROP-TYPED BINDERS (\d+) ; THOSE REACHING A GRADED TERMINAL (\d+)', t)
    return bool(m) and bool(j) and int(m.group(1)) == j.get('lines') and int(m.group(2)) == len(j.get('prop_typed') or []) \
        and int(m.group(3)) == len(j.get('reaching') or []) and len(j.get('repos') or []) == 33 and 'SIDE-explicit-formula' in j['repos'] \
        and all(('%s:%d' % (x['file'], x['line'])) in t for x in j.get('reaching') or [])


def classes_ok(S):
    j, t = S['clj'], S['clt']
    rows = j.get('rows') or []
    m = re.search(r'NODES (\d+) ; AGREEING (\d+) ; CORRECTED (\d+) ; FOR THE AUTHOR`S RULING (\d+)', t)
    return bool(m) and len(rows) == 33 and sorted(r['name'] for r in rows) == S['the33'] \
        and [int(m.group(i)) for i in (1, 2, 3, 4)] == [len(rows), sum(r['verdict'] == 'AGREE' for r in rows),
                                                         sum(r['verdict'] == 'CORRECTED' for r in rows), sum(r['verdict'] == 'FOR THE AUTHOR`S RULING' for r in rows)] \
        and all(('### %s (' % r['name']) in t for r in rows) and [r['name'] for r in rows if r['verdict'] == 'CORRECTED'] == [K.INSERT]


def e0_before_ok(S):
    b = S['e0b']
    old = (blob(ROOT, '%s:tools/e0_rule.py' % PRE['relay']) or b'').decode('utf-8')
    gi = [l for l in b.split(NL) if l.startswith('    :232  def grade(')]
    return bool(gi) and all(re.sub(r'^\s*:\d+\s{1,4}', '', l) in old for l in b.split(NL)[2:] if l.startswith('    :')) \
        and "DOMAIN = r'(?:≠|<|≤|=|∈|∉|\\.Even\\b|IsPrimitive)'" in b


def e0_diff_ok(S):
    files = S['e0files']
    banked = [l[4:].strip() for l in S['e0d'].split(NL) if l.startswith('### ') and 'changed' in l]
    return all(a is not None and a == c and a != b for a, b, c in files.values()) and bool(S['e0_stat']) and banked == [S['e0_stat'].strip()] \
        and '+def domain_case(t, head):' in S['e0d'] and '+RESTRICTIONS = [' in S['e0d'] and '+def strip_range(t):' in S['e0d']


def e0_test_ok(S):
    n, p = count(S['e0t'])
    return n == 16 and p == 16 and S['e0j'].get('cases') == n and S['e0j'].get('passing') == p and S['e0j'].get('rc') == 0 \
        and '### ### **16 of 16 cases as wanted -- PASS**' in S['e0t']


def e0_control_ok(S):
    """### b624's defect (e), repaired: the control line read by the record tool's own pattern, from the bank's text."""
    c = S['e0j'].get('control') or {}
    m = re.search(S['REC'].CONTROL_RE, S['e0t'], re.M)
    return bool(m) and m.group(1) == PRE['relay'] and m.group(2) == '1' and m.group(3) == '16' and m.group(4) == '12' \
        and c.get('failing') == S['REC'].CONTROL_FAILING and m.group(5) == str(S['REC'].CONTROL_FAILING)


def nodes_ok(S):
    j = S['nodesj']
    return S['moved_now'] is not None and S['moved_now'] == j.get('moved') and len(S['moved_now']) == 29 \
        and set(S['moved_now']) <= set(S['the33']) and len(j.get('rows') or []) == S['nodes_now']


def planted_ok(S):
    ps = S['e0j'].get('planted') or []
    out = []
    for p in ps:
        m = re.match(r'planted: (.+\.lean) \((\d+) bytes\)$', p)
        out.append(bool(m) and os.path.isabs(m.group(1)) and os.path.exists(m.group(1)) and os.path.getsize(m.group(1)) == int(m.group(2))
                   and m.group(1).replace('\\', '/').startswith(SP.replace('\\', '/')))
    return len(out) == 2 and all(out)


def closure_ok(S):
    j, t = S['cloj'], S['clot']
    rows = j.get('modules') or []
    m = re.search(r'CLOSURE (\d+) MODULES \((\d+) LINES\) ; NEW (\d+)', t)
    return bool(m) and int(m.group(1)) == len(rows) and int(m.group(2)) == sum(r['lines'] for r in rows) \
        and int(m.group(3)) == sum(r['state'] == 'NEW' for r in rows) == j.get('new') and j.get('peel') == K.UP_PIN == j.get('pin') \
        and 'theorem thmB₀_mult' in (j.get('line') or '') and j.get('over') is (len(rows) > K.MAX_MODULES) \
        and all(('  %s ' % r['module']) in t for r in rows) and j.get('lsr') == 1


def hold_ok(S):
    a = S['answers']
    ct = utc_epoch(json.dumps(S['cloj']), '"at": "') or 0
    m = re.search(r'### b625 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a)
    return bool(m) and int(m.group(1)) >= 1 and 'the closure' in a and 'RESULT (transcript line' in a and '### NO RESULT' not in a \
        and S['cloj'].get('over') is True and ct > (S['lock_epoch'] or 10 ** 12)


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h59_ok(S, k):
    held = S['cloj'].get('over') is True
    if k in ('H59a', 'H59b', 'H59c'):
        want = 'NOT SCORABLE' if held else 'REFUTED'
    else:
        moved = [x for x in (S['pj']['zeta'].get('grade_cells_moved') or []) + (S['pj']['chi'].get('grade_cells_moved') or [])
                 if 'exceptional_mass_le_third' not in x]
        want = 'HOLDS' if not moved else 'REFUTED'
    return _h(S, k, want)


def table_after_ok(S):
    t = S['tblj']
    ch = t.get('changed') or []
    return bool(t) and t.get('rc') == 0 and not (t.get('added') or t.get('gone')) and len(ch) == 1 and K.INSERT in json.dumps(ch[0]) \
        and 'DERIVES' in json.dumps(ch[0]) and t.get('files_moved') is not None


def pages_ok(S):
    out = []
    for k, p in (('zeta', PAGE), ('chi', DIR_PAGE)):
        j = S['pj'][k]
        a, b, c = S['pages'][p]
        commits = [h for h, f in S['pp_files'].items() if p in f]
        alone_ = (len(commits) == 1 and S['pp_files'][commits[0]] == [p] and dict(S['pp_log'])[commits[0]].startswith('b625 (R235)')) \
            if j.get('changed') else not commits
        out.append(j.get('rc') == 0 and j.get('dry') is False and a is not None and a == c and hashlib.sha256(c).hexdigest() == j.get('sha256') and alone_)
    return len(out) == 2 and all(out)


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('%s PASSING : 2 of 2' % CONTROL_ARM) in t


def root_test_ok(S):
    n, p = count(S['rtt'])
    return n == 8 and n == p and S['rtj'].get('cases') == n and S['rtj'].get('rc') == 0


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    gained = sorted(set((j.get('reads') or {}).get('heads') or {}) - set((j0.get('reads') or {}).get('heads') or {}))
    return bool(j) and len(rows) == 2 and rows[1][:3] == ['b625', j.get('root'), j0.get('root')] and j.get('previous') == j0.get('root') \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and len(j['reads']['heads']) == 38 and gained and len(rows[1]) == 4 and rows[1][3] == 'list widened: ' + ' '.join('+' + x for x in gained) \
        and S['roots_pre'] is not None and (S['roots_now'] or b'').startswith(S['roots_pre'])


def midpush_ok(S):
    j = S['arj']
    heads = (j.get('reads') or {}).get('heads') or {}
    m1 = re.search(r'push_gated: main read back at the remote: (\w+)', S['rpush'])
    m2 = re.search(r'push_gated: main read back at the remote: (\w+)', S['ppush'])
    return bool(m1 and m2) and heads.get('relay') == m1.group(1) and heads.get('PLACE-papers') == m2.group(1)


def verify_ok(S):
    v = S['ar_verify'] or []
    return [x[0] for x in v] == ['b624', 'b625'] and all(x[1] == 'AGREE' for x in v)


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 24]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The 2/3 theorem held at its closure: ') \
        and all(x in tail for x in ('**The closure**', '**The 33 nodes**', '**The table and the pages.**', '**The section variables**',
                                    '**The act root**', '**The record lines**', '**The scores.**', '**Read in mutual light**', 'strengthens',
                                    '**Next.**', 'b626'))


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
        and S['kcur'] == 'main' and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a')


def corpus_scope(S):
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if S['pj'][k].get('changed')]
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages)


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


READ_NEEDLES = ('OPEN_TRAILS.md @ 52822a5f', 'FINDINGS.md @ 52822a5f', 'data/b624_e0_nodes.txt @ 84bae29a', 'tools/e0_rule.py @ 84bae29a',
                'Simplicity.lean @ 5a1630b8', 'Simplicity.lean @ 1d5d4dd9', 'Zeta23/Defs.lean @ 1d5d4dd9', 'Zeta23/FinalMult.lean @ 3635e748',
                'lakefile.toml @ 3635e748', 'lean-toolchain @ 3635e748', 'tools/act_root.py @ 84bae29a', 'data/act_roots.txt @ 84bae29a',
                'THE_KEYSTONE_CENSUS_v0_4.md @ 52822a5f', 'REGISTRY.md @ 52822a5f', 'data/b624_closing_push_out.txt @ 47875922',
                ':12290 ', ':12436 ', ':11864 ', ':12228 ', ':12354 ', ':12356 ', ':12799 ', ':12919 ', ':12953 ', ':350 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R235) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + '\n  1234   5678 lean.exe  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the two step-zero commits and every later commit', lambda S: S['lock_epoch'] is not None
     and all(any(l.startswith(c) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock']) for c in (STEPZERO, NSREPAIR))
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith((STEPZERO, NSREPAIR))), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b624`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b624' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and sorted(l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']) == sorted([STEPZERO, NSREPAIR]),
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b625 -- x'])),
    ('G-R235-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R235) END' in S['ferry'] and S['ot'].count('**(R235) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R235) ratified', '(R235) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 47875922`s files', lambda S: S['pushout'][0] == ['data/b624_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b624_closing_push_out.txt', 'x'], True))),
    ('G-NSREPAIR-ALONE', 'relay e6781b18: the data module alone, its one changed line the namespace', lambda S: S['nsrep'][0] == ['tools/b624_worklist.py']
     and S['nsrep'][1].startswith(NS_SUBJECT) and S['nsrep'][2].count('\n-  ') + S['nsrep'][2].count('\n+  ') == 2
     and "+                ('SIDEExplicitFormula.B321.power_contDiff'" in S['nsrep'][2],
     lambda S: put(S, 'nsrep', (S['nsrep'][0] + ['x'], S['nsrep'][1], S['nsrep'][2]))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b624') == 5, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b624'}))),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    (FROZEN_ARM, 'b622`s lists re-emitted with every relay read at 84bae29a, every PLACE-papers read at 52822a5 and the E0 rule`s blob at 84bae29a, against the pages at 52822a5',
     lambda S: len(S['old_frozen']) == 2 and all(x['rc'] == 0 and x['equal'] for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [S['old_frozen'][0], dict(S['old_frozen'][1], equal=False)] if len(S['old_frozen']) == 2 else [])),
    ('G-INSTRUMENTS-UNEDITED', 'b624`s suite and record tool, the shared record tools, the claims modules, the generator and its test, the page arm, the scanner, the table generator and its gate, the seal, the lock gate and the push gate against 84bae29a',
     lambda S: all(a is not None and a == b for a, b in S['inst'].values()) and len(S['inst']) == len(INST),
     lambda S: put(S, 'inst', dict(S['inst'], **{'b624_record.py': (S['inst']['b624_record.py'][0], (S['inst']['b624_record.py'][1] or b'') + b'x')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', b'', b''))),
    ('G-SECTION-VARS-BANKED', 'the section-variable bank: its counts against its json, every reaching binder printed by file and line, 33 repositories', lambda S: secvars_ok(S),
     lambda S: put(S, 'svt', re.sub(r'REACHING A GRADED TERMINAL (\d+)', lambda m: 'REACHING A GRADED TERMINAL %d' % (int(m.group(1)) + 1), S['svt']))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b624`s weight, its figures and its defects', lambda S: landed(S, 0, ('(:7512)', 'relay f648d5a5', '8c9d9a52',
                                                                                                                  '1beaba22024ee00a', 'defects (a)-(f) the seat’s', ':12953')),
     lambda S: put(S, 'find', S['find'].replace('defects (a)-(f) the seat’s', 'defects the seat’s'))),
    ('G-CRITERION-LINE', 'OPEN_TRAILS at the banked line: the domain-condition criterion, addressed to :12436', lambda S: landed(S, 1, ('(:12436)', '(i) an instance binder whose class is not Fact', '(iii) a restriction on a variable', 'Summable or HasSum')),
     lambda S: put(S, 'ot', S['ot'].replace('(i) an instance binder whose class is not Fact', '(i) an instance binder'))),
    ('G-ROOTLIST-LINE', 'OPEN_TRAILS at the banked line: the root`s repository list, addressed to :12210', lambda S: landed(S, 2, ('(:12210)', 'REGISTRY’s kernel rows', 'list widened: +<kernel>')),
     lambda S: put(S, 'ot', S['ot'].replace('REGISTRY’s kernel rows', 'REGISTRY’s rows'))),
    ('G-CENSUS-ITEM-LINE', 'OPEN_TRAILS at the banked line: the census item, priced', lambda S: landed(S, 3, ('(:12210)', 'THE_KEYSTONE_CENSUS v0.5', '**Price:**', 'Priced, not started')),
     lambda S: put(S, 'ot', S['ot'].replace('Priced, not started', 'Started'))),
    ('G-CORRECTIONS-LANDED', 'the four ledgers` lines after the banked heads: each directive in its own form; one PLACE-papers commit of the two ledgers', lambda S: corrections_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('SUPERSEDES OPEN_TRAILS :12434 for `finsetSum_insert`', 'SUPERSEDES OPEN_TRAILS :12434 for `finsetSum`'))),
    ('G-E0-BEFORE-BANKED', 'the grade function bank against the rule`s blob at 84bae29a', lambda S: e0_before_ok(S),
     lambda S: put(S, 'e0b', S['e0b'].replace('def grade(', 'def graded('))),
    ('G-CLASSES-BANKED', 'the classes bank: 33 nodes, the verdict counts recomputed from its rows, the one corrected the step lemma', lambda S: classes_ok(S),
     lambda S: put(S, 'clt', S['clt'].replace('AGREEING 29', 'AGREEING 28'))),
    ('G-E0-COMMITTED-ALONE', 'relay`s log: the rule and its test in one commit of their own, after the lock', lambda S: alone(S, list(K.E0_FILES), E0_SUBJECT),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted(K.E0_FILES)))),
    ('G-E0-DIFF-BANKED', 'the rule and its test on disk and at HEAD against 84bae29a; the diff bank`s stat line; the criterion in it', lambda S: e0_diff_ok(S),
     lambda S: put(S, 'e0d', S['e0d'].replace('+def strip_range(t):', '+def strip(t):'))),
    ('G-E0-TEST-COUNTED', 'the test bank`s text counted here by its case pattern: sixteen of sixteen', lambda S: e0_test_ok(S),
     lambda S: put(S, 'e0t', S['e0t'] + '\n  (17) planted : PASS')),
    ('G-E0-CONTROL-REFUTED', 'the test with the rule as it stood, read by the record tool`s own pattern: exactly (9), (13), (14) and (15) fail', lambda S: e0_control_ok(S),
     lambda S: put(S, 'e0t', S['e0t'].replace('cases 16, passing 12', 'cases 16, passing 16'))),
    ('G-E0-NODES-NOW', 'every page node graded now by the rule before and after: twenty-nine move, all among the 33, against the bank', lambda S: nodes_ok(S),
     lambda S: put(S, 'moved_now', (S['moved_now'] or []) + ['x'])),
    ('G-PLANTED-AT-PATHS', 'the two planted modules at the absolute paths the test printed, under the scratchpad, their sizes as printed', lambda S: planted_ok(S),
     lambda S: put(S, 'e0j', dict(S['e0j'], planted=(S['e0j'].get('planted') or [])[:1]))),
    ('G-CLOSURE-BANKED', 'the closure bank: one ls-remote, the peel, the line at :350, every module listed, the counts recomputed', lambda S: closure_ok(S),
     lambda S: put(S, 'cloj', dict(S['cloj'], peel='0' * 40))),
    ('G-ZERO-VENDOR-BRANCHES', 'the explicit-formula kernel`s branches: no b625 vendor branch', lambda S: S['vendor_branches'] == [] and S['cloj'].get('over') is True,
     lambda S: put(S, 'vendor_branches', ['vendor-finalmult-b625'])),
    ('G-HOLD-ANSWERED', 'the answers bank: the prompt at the hold, after the closure bank and the lock, verbatim with its result', lambda S: hold_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('RESULT (transcript line', 'RESULT (no line'))),
    ('G-H59A-SCORED', 'H59a recomputed from the closure bank, against the scores and the desk', lambda S: h59_ok(S, 'H59a'), lambda S: _sc(S, 'H59a')),
    ('G-H59B-SCORED', 'H59b recomputed from the closure bank, against the scores and the desk', lambda S: h59_ok(S, 'H59b'), lambda S: _sc(S, 'H59b')),
    ('G-H59C-SCORED', 'H59c recomputed from the closure bank, against the scores and the desk', lambda S: h59_ok(S, 'H59c'), lambda S: _sc(S, 'H59c')),
    ('G-TABLE-AFTER', 'the table bank: one row changed, the step lemma to DERIVES, none added or gone', lambda S: table_after_ok(S),
     lambda S: put(S, 'tblj', dict(S['tblj'], changed=(S['tblj'].get('changed') or []) + [['SIDE-explicit-formula', 'x']]))),
    ('G-PAGES-NOW', 'both pages on disk and at HEAD against their banks, each committed alone where it changed', lambda S: pages_ok(S),
     lambda S: put(S, 'pages', dict(S['pages'], **{DIR_PAGE: (S['pages'][DIR_PAGE][0], S['pages'][DIR_PAGE][1], (S['pages'][DIR_PAGE][2] or b'') + b'x')}))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b622`s list and b602`s v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b622`s list and b603`s v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank: both page arms and the frozen control', lambda S: arms_ok(S['arms']),
     lambda S: put(S, 'arms', S['arms'].replace('PAGE ARMS PASSING : 2 of 2', 'PAGE ARMS PASSING : 1 of 2'))),
    ('G-H59D-SCORED', 'H59d recomputed from the page banks, against the scores and the desk', lambda S: h59_ok(S, 'H59d'), lambda S: _sc(S, 'H59d')),
    ('G-ACTROOT-COMMITTED-ALONE', 'relay`s log: act_root.py and its test in one commit of their own, after the lock', lambda S: alone(S, list(K.ROOT_FILES), ROOT_SUBJECT),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted(K.ROOT_FILES)))),
    ('G-ACTROOT-TEST-COUNTED', 'the act-root test bank`s text counted here by its case pattern: eight of eight', lambda S: root_test_ok(S),
     lambda S: put(S, 'rtt', S['rtt'] + '\n  (99) planted : FAIL')),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s b625 line, the root bank and its items: previous b624`s root, 38 repositories, the note naming the kernels gained, b624`s line unedited', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'].replace('list widened: ', 'list: ', 1))),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay and PLACE-papers heads against the read-backs of the pushes made before it', lambda S: midpush_ok(S),
     lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed by this suite, one remote read per repository: b624 and b625 AGREE', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', [('b624', 'AGREE', []), ('b625', 'DISAGREE', ['x'])])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous, as data/act_roots.txt holds them', lambda S: bool(S['arj'])
     and ('**Act root:** b625 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Act root:** b625', '**Act root:** b62x'))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items, the hold and the nodes for ruling', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**The hold, and the author’s answer**' in trail(S) and '**For the author’s ruling:**' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**For the author’s ruling:**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b626, W-ORD-PLATT-RUNG' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b626, W-ORD-PLATT-RUNG', 'x'))),
    ('G-CURRENTS-UNEDITED', 'the current versions, the census, REGISTRY, ERRATA, README and SPIRAL_MAP on disk and at HEAD against 52822a5',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'REGISTRY.md': ((S['currents']['REGISTRY.md'][0] or b'') + b'x',
                                                                                                    S['currents']['REGISTRY.md'][1], S['currents']['REGISTRY.md'][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the ledger appends, its banks and tools, the rule, act_root.py and the roots file',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: main, tags by peel, branches and status against the face; the explicit-formula checkout on main; lv and its trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-cosmo': ['0', {}, [], '']}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b625_record.py'): S['tooltext'].get(os.path.join(T, 'b625_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', ((S['errata'][0] or b'') + b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 84bae29a, by blob id, the roots file read by G-ACTROOT-BANKED', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b624_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers and a page only where its re-emission changed', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-UNMOVED', 'the suite`s own regeneration against the committed table: no row added or gone and no grade cell moved', lambda S: S['table_changed'] is not None
     and S['table_changed'] == [], lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b625')" in S['suite'] and "data/b625_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b625')", ''))),
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
    rec('b625 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                  if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
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
        out = os.path.join(D, 'b625_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b625_checks_postpush.txt' if pushed else 'b625_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b625_arms_prerun.txt', 'b625_lsr_prerun.json').replace('b625_checks', 'b625_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b625_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
