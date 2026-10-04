# -*- coding: utf-8 -*-
"""b618_checks.py -- THE SUITE OF b618, UNDER (R228): THE LIVING DOCUMENTS' CURRENCY -- EIGHT DOCUMENTS READ FOR THEIR FUNCTIONS AND FED
IN THEIR OWN FORMS WITH WHAT THE RECORD CARRIED PAST THEM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b618_checks.txt before the push and data/b618_checks_postpush.txt
### after it. `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is sealed, no table regenerated, its
### counts written to data/b618_arms_prerun.txt. ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs),
### each run's ls-remote calls banked per repository beside its output (data/b618_lsr*.json); G-LSREMOTE-ONE-PER-REPO runs last.
### ### The harness is b568's to b617's, carried from tools/b617_checks.py (its imports, helpers, regenerate and main); the sources,
### predicates and arms are b618's. The control arm is the frozen one of (R207)(2). Every positive control mutates a line whose text occurs
### once in its source and that its predicate reads. The no-disclosure needles are built at run time from TECHNE-Core's module documents
### and never printed.
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

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b618_registration_2026-10-04.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='6d813af6', pp='138ea0c', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-explicit-formula': '1d5d4dd9', 'SIDE-global-section': '3528bcfc',
             'SIDE-spinor': '520abe7a'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = 'c38ec385'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/74014083-db4d-4c92-b7fa-834bcf48e96a/scratchpad'


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    if 'ls-remote' in a:   # ### OPEN_TRAILS :12703: every ls-remote of the run counted per repository
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
    return (b or b'').replace(b'\r\n', b'\n')


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b618')
            and 'data/b618_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section)/[^`\s]+)`', w)))


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
    l = cr0(b).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def _scan_bytes(text, name):
    p = os.path.join(SP, '_b618_suite_scan_%s.md' % name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    return subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', p], capture_output=True, text=True,
                          encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout


def _unbom(b):
    t = cr0(b).decode('utf-8', 'replace') if b is not None else ''
    return t[1:] if t.startswith('\ufeff') else t


def sources():
    import b618_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b618_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b618_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b618_ferry.txt'), scan=rd('b618_ferry_scan.txt'), cens=rd('b618_census_stepzero.txt'),
        fcens=rd('b618_faces_census_stepzero.txt'), pins0=rd('b618_pins_stepzero.txt'), procs=rd('b618_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b617_closing.txt'), reads=rd('b618_reads.txt'), branches=rd('b618_branches.txt'), answers=rd('b618_author_answers.txt'),
        prerun=rd('b618_arms_prerun.txt'), defects=rd('b618_defects.txt'), plan=rd('b618_plan.txt'), PJ=jl('b618_plan.json'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b617_checks.py', 'b617_record.py', 'b616_record.py', 'b616_claims.py', 'b604_record.py', 'b602_record.py',
                        'b560_record.py', 'b566_record.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py',
                        'push_gated.sh', 'banned_terms.py', 'b558_record.py', 'terminal_table.py', 'b327_faces_row.py', 'errata_append.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        docs={n: dict(disk=_unbom(raw(os.path.join(PP, *p.split('/')))), head=_unbom(blob(PP, 'HEAD:' + p)), pre=_unbom(blob(PP, PRE['pp'] + ':' + p)),
                      draft=rd('b618_append_%s.md' % n), dj=jl('b618_draft_%s.json' % n), land=jl('b618_land_%s.json' % n))
              for n, p, _nd in REC.LIVING},
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in CURRENTS},
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kern_face=(jl('b618_kernels_face.json').get('kernels') or {}), kern_now={k: list(v) for k, v in REC.kern_state().items()},
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b617*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b618_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b618_mustnotexist.txt')), table_changed=None,
        fj=jl('b618_findings.json'), tj=jl('b618_trail.json'), sc=jl('b618_scores.json'), desk=rd('b618_desk_notes.txt'),
        rl=jl('b618_record_lines.json'), RC=jl('b618_regcheck.json'), HJ=jl('b618_h52.json'),
        PZ=jl('b618_page_zeta.json'), PX=jl('b618_page_chi.json'), arms_c2=rd('b618_page_arms_c2.txt'),
        lsr=None,
    )
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['ins_now'] = REC.instr_resolve()
    S['nd_sets'] = R6.nd_sets()
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append((now or b'')[len(pre or b''):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for n, d in S['docs'].items():
        pub.append(d['disk'][len(d['pre']):] if d['disk'].startswith(d['pre']) else d['disk'])
    for f in sorted(os.listdir(D)):
        if f.startswith(('b618_', 'audit_b618_')):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
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
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['keystone_changes'] = sorted(x for x in ch if x.startswith('phase') or x.startswith('day1/') or x.startswith('outputs/') or x.startswith('heritage/'))
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S['pp_head'], S['pp_remote'] = gs(PP, 'rev-parse', 'HEAD'), KC0.remote_refs(PP).get('refs/heads/main', '')   # ### read once (OPEN_TRAILS :12703)
    S['h52_now'] = REC.h52('HEAD') if all(d['head'] != d['pre'] for d in S['docs'].values()) else []
    S['scan_now'] = {n: _scan_bytes(d['disk'][len(d['pre']):], n) if d['disk'].startswith(d['pre']) and len(d['disk']) > len(d['pre']) else ''
                     for n, d in S['docs'].items()}
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b618_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b618_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    return X


# ### the act's own predicates
CURRENTS = ('README.md', 'ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md',
            'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md', 'phase1.5/proofs/THE_RIEMANN_PATHS_CLUSTER_SPINE.md',
            'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md',
            'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md',
            'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md',
            'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md',
            'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md', 'day1/A_Place_to_Stand_v5_17.md',
            'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md', 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_2.md')
NAMES = ('VERIFICATION_LOOM', 'INSTRUMENTS', 'THE_METHOD_CANON', 'THE_METHOD_AS_IT_STANDS', 'FACES_LEDGER', 'THE_LOAD_BEARING_MAP',
         'GAUGE_AND_INVARIANT', 'REGISTRY')


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


def procs_ok(S):
    p = S['procs']
    rows = [l for l in p.split(NL) if re.match(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut|python|tail)\.exe', l)]
    return 'powershell.exe' in p and '### ORPHANS:' in p and '\\v1.0\\' in p and all('### STOPPED BY PID' in l for l in rows) \
        and 'tail' in p.split('### names matched:')[1].split(NL)[0]


def weight_ok(S):
    x = (S['rl'].get('lines') or [{}])[0]
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7368)' in a and 'b617 AT ITS WEIGHT' in a \
        and 'the suite 80 of 80 before the push and 80 of 80 after it' in a and 'not 2026-09-08' in a and 'on the trails at :12280' in a \
        and 'neither K₇ (6 once, −1 six times) nor the incidence matrix' in a and x['line'] > 7368


def plan_ok(S):
    t, P = S['plan'], S['PJ']
    return t.startswith('b618 -- COMPONENT 2: THE PLAN') and t.count('### THE RULING`S DISPOSITION : ') == 8 \
        and t.count('### THE SEAT`S RECOMMENDATION : ') == 8 and P.get('differs') == ['REGISTRY'] \
        and all((P.get('docs') or {}).get(n, {}).get('function_line', 0) > 0 for n in NAMES)


def plan_first(S):
    at = iso_epoch(S['PJ'].get('at', ''))
    ts = [int(gs(PP, 'log', '-1', '--format=%ct', h)) for h, f in S['pp_files'].items() if any(S['REC'].DOC[n] in f for n in NAMES)]
    return at is not None and bool(ts) and at < min(ts)


def draft_banked(S, n):
    d = S['docs'][n]
    return bool(d['draft']) and d['dj'].get('sha256') == hashlib.sha256(d['draft'].encode('utf-8')).hexdigest() and d['dj'].get('scanner_clean') is True \
        and d['dj'].get('ceiling') == []


def landed(S, n):
    """### the document on disk and at HEAD: its pre-act blob plus the banked draft, byte for byte (FACES_LEDGER: its writer's join)"""
    d = S['docs'][n]
    if not d['pre'] or not d['draft']:
        return False
    if n == 'FACES_LEDGER':
        want = d['pre'].rstrip(NL) + NL + d['draft']
    else:
        want = d['pre'] + d['draft']
    return d['disk'] == want and d['head'] == want and d['land'].get('ok') is True


def alone_in_order(S):
    REC = S['REC']
    order, ok = [], []
    hs = [h for h, _s in S['pp_log']]
    for n in NAMES:
        c = [h for h, f in S['pp_files'].items() if REC.DOC[n] in f]
        ok.append(len(c) == 1 and S['pp_files'][c[0]] == [REC.DOC[n]] and dict(S['pp_log'])[c[0]].startswith(REC.COMMIT_PREFIX[n]))
        order.append(hs.index(c[0]) if c else -1)
    return all(ok) and order == sorted(order) and -1 not in order


def h52a_ok(S):
    it = S['h52_now']
    want = 'HOLDS' if it and all(ok for _d, _i, ok in it) else 'REFUTED'
    return bool(it) and len(it) == len(S['HJ'].get('items') or []) and _h(S, 'H52a', want)


def h52b_now(S):
    t = S['docs']['REGISTRY']['disk']
    i = t.find(S['REC'].MARK['REGISTRY'])
    tail = t[i:] if i >= 0 else ''
    cells = re.findall(r'(?<![\w.])(v\d+(?:\.\d+)+) \(`([^`]+\.md)`', tail) + [
        (m.group(3), m.group(2)) for m in re.finditer(r'^\| (1\.5a-\d+|1\.5e-\d+|p2-\d+|p2-d\d+) \| [^|]+ \| `([^`]+)` \| (v\d+(?:\.\d+)+) \|', tail, re.M)]
    return [(v, f, S['REC'].vline(f, 'HEAD')[1]) for v, f in cells]


def h52b_ok(S):
    c = h52b_now(S)
    want = 'HOLDS' if c and all(v == w for v, _f, w in c) else 'REFUTED'
    return bool(c) and len(c) == S['RC'].get('n') and S['RC'].get('ok') == S['RC'].get('n') and _h(S, 'H52b', want)


def h52c_ok(S):
    want = 'HOLDS' if len(S['ins_now']) == 24 and all(x['ok'] for x in S['ins_now']) else 'REFUTED'
    return _h(S, 'H52c', want)


def h52d_ok(S):
    c = [bool(re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['scan_now'][n], re.M)) for n in NAMES]
    want = 'HOLDS' if all(c) and all(S['docs'][n]['dj'].get('scanner_clean') for n in NAMES) else 'REFUTED'
    return len(c) == 8 and _h(S, 'H52d', want)


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def loom_now(S):
    REC = S['REC']
    rows = REC.loom_rows()
    t = S['docs']['VERIFICATION_LOOM']['disk']
    return len(rows) == 81 and all(('| %s | %s | %s | ' % (r['act'], REC._cnt(r['pre']), REC._cnt(r['post']))) in t for r in rows)


def map_now(S):
    N = S['REC'].page_nodes()
    t = S['docs']['THE_LOAD_BEARING_MAP']['disk']
    names = (S['REC']._cur()['THE_LOAD_BEARING_MAP']['items']['absent_names'])
    return len(names) == 76 and all(any(('| `%s` | %s | %s | %s | %s |' % (x['q'], x['e0'], x['tier'] or '—', x['pin'], x['page'])) in t for x in N.get(s, []))
                                    and N.get(s) for s in names)


def faces_now(S):
    N = S['REC'].page_nodes()
    t = S['docs']['FACES_LEDGER']['disk']
    return all(N.get(dc) and ('| `%s` (SIDE-explicit-formula %s; the %s page) | %s |' % (N[dc][0]['q'], N[dc][0]['pin'], N[dc][0]['page'], N[dc][0]['tier'])) in t
               for _f, dc, _v in S['REC'].FACES)


def spinor_ok(S):
    t = S['docs']['REGISTRY']['disk']
    a = lines_of(blob('D:/SIDE-spinor', 'v0.1.0:SIDESpinor/Spinor.lean'))
    return len(a) > 75 and ('`%s`' % a[69].strip().rstrip(' :=')) in t and ('`%s`' % a[74].strip().rstrip(' :=by').rstrip()) in t \
        and '`SIDE-spinor` `v0.1.0` = `b235bc6`' in t


def pages_banked(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        a, b, c = S['pages'][p]
        if z.get('changed') is True:
            out.append(z.get('rc') == 0 and bool(a) and a == c and a != b and hashlib.sha256(c).hexdigest() == z.get('sha256'))
        else:
            out.append(z.get('rc') == 0 and z.get('changed') is False and bool(a) and a == b == c and hashlib.sha256(c).hexdigest() == z.get('sha256'))
    return all(out)


def pages_alone(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        if z.get('changed') is True:
            c = [h for h, f in S['pp_files'].items() if p in f]
            out.append(len(c) == 1 and S['pp_files'][c[0]] == [p] and dict(S['pp_log'])[c[0]].startswith('b618 (R228): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    order = [h for h, _s in S['pp_log']]
    last_doc = max([order.index(h) for h, f in S['pp_files'].items() if any(S['REC'].DOC[n] in f for n in NAMES)] or [10 ** 6])
    pc = [h for h, f in S['pp_files'].items() if PAGE in f or DIR_PAGE in f]
    return all(out) and all(order.index(h) > last_doc for h in pc)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The living documents’ currency: eight documents fed in their own forms') \
        and all(x in tail for x in ('**The appends**', '**The record line.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**',
                                    'INSTRUMENTS I-16 to I-39', 'b619'))


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE', 'HOLDS') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def kernels_untouched(S):
    return all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == '' \
        and 'v0.21' in S['ktags'] and 'v0.22' not in S['ktags'] and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') \
        and S['lv_dirty'] == '' and bool(S['kern_face']) and S['kern_face'] == S['kern_now']


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def unedited_all(S):
    return all(bool(b) and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


def _mut_doc(S, n, old, new):
    d = dict(S['docs'][n])
    d['disk'] = d['disk'].replace(old, new, 1)
    return put(S, 'docs', dict(S['docs'], **{n: d}))


def _mut_draft(S, n):
    d = dict(S['docs'][n])
    d['draft'] = d['draft'] + 'x'
    return put(S, 'docs', dict(S['docs'], **{n: d}))


READ_NEEDLES = ('data/b617_currency.txt @ 6d813af6', 'data/b617_closing_push_out.txt @ c38ec385', 'VERIFICATION_LOOM.md @ 138ea0c2',
                'INSTRUMENTS.md @ 138ea0c2', 'THE_METHOD_CANON.md @ 138ea0c2', 'THE_METHOD_AS_IT_STANDS.md @ 138ea0c2', 'FACES_LEDGER.md @ 138ea0c2',
                'THE_LOAD_BEARING_MAP.md @ 138ea0c2', 'GAUGE_AND_INVARIANT.md @ 138ea0c2', 'REGISTRY.md @ 138ea0c2', 'OPEN_TRAILS.md @ 138ea0c2',
                'FINDINGS.md @ 138ea0c2', 'Spinor.lean @ b235bc62', 'data/b604_author_answers.txt @ 6d813af6',
                '### THE EIGHT DOCUMENTS` LAST COMMITS', '### THE VERSION LINES OF EVERY EDITION FILE SINCE 192077f',
                ':11864 ', ':12228 ', ':12280 ', ':12304 ', ':12446 ', ':12631 ', ':12699 ', ':12703 ', ':12755 ', ':6856 ', ':7278 ', ':731 ', ':787 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R228) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + '\n  1234   5678 lean.exe  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b617`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b617' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b618 -- x'])),
    ('G-R228-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R228) END' in S['ferry'] and S['ot'].count('**(R228) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R228) ratified', '(R228) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads']
     and 'NO VERSION LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: the one prompt before the seal, its options and recommended mark verbatim, the answer',
     lambda S: S['answers'].startswith('### b618 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, 1 prompt(s)') and S['answers'].count('### PROMPT ') == 1
     and S['answers'].count('  OPTION ') == 3 and 'OPTION 1 [RECOMMENDED]: Pointer line only (Recommended)' in S['answers'] and 'option 3.' in S['answers'],
     lambda S: put(S, 'answers', S['answers'].replace('1 prompt(s)', '2 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay c38ec385`s files', lambda S: S['pushout'][0] == ['data/b617_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b617_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b617') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b617'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b617`s suite and record tool, b616`s record tool and claims module, the shared record tools, the control`s test file, the generator, its arm, the E0 rule, the push gate, the scanner, the sentence counter, the table generator, the faces writer and the errata appender against 6d813af6',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 18,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b327_faces_row.py': (S['inst']['b327_faces_row.py'][0], (S['inst']['b327_faces_row.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b617`s weight, the confirmations, the two corrections and the generator`s channels', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('on the trails at :12280', 'x'))),
    ('G-PLAN-BANKED', 'the plan bank and its json: each document`s function line, disposition and recommendation, the one difference', lambda S: plan_ok(S),
     lambda S: put(S, 'PJ', dict(S['PJ'], differs=[]))),
    ('G-PLAN-BEFORE-WRITE', 'the plan`s stamp against the first append`s commit time', lambda S: plan_first(S),
     lambda S: put(S, 'PJ', dict(S['PJ'], at='2099-01-01T00:00:00Z'))),
    ('G-DRAFTS-BANKED', 'the eight drafts and their json: sha, scanner, ceiling', lambda S: all(draft_banked(S, n) for n in NAMES),
     lambda S: _mut_draft(S, 'GAUGE_AND_INVARIANT')),
    ('G-LOOM-LANDED', 'VERIFICATION_LOOM on disk and at HEAD: its pre-act blob plus the draft', lambda S: landed(S, 'VERIFICATION_LOOM'),
     lambda S: _mut_doc(S, 'VERIFICATION_LOOM', '| b617 | ', '| b6l7 | ')),
    ('G-INSTRUMENTS-LANDED', 'INSTRUMENTS on disk and at HEAD: its pre-act blob plus the draft', lambda S: landed(S, 'INSTRUMENTS'),
     lambda S: _mut_doc(S, 'INSTRUMENTS', '## I-39 — ', '## I-40 — ')),
    ('G-CANON-LANDED', 'THE_METHOD_CANON on disk and at HEAD: its pre-act blob plus the draft', lambda S: landed(S, 'THE_METHOD_CANON'),
     lambda S: _mut_doc(S, 'THE_METHOD_CANON', '## XXI. ', '## XXII. ')),
    ('G-ASIS-LANDED', 'THE_METHOD_AS_IT_STANDS on disk and at HEAD: its pre-act blob plus the draft', lambda S: landed(S, 'THE_METHOD_AS_IT_STANDS'),
     lambda S: _mut_doc(S, 'THE_METHOD_AS_IT_STANDS', '## Addendum, 2026-10-04', '## Addendum, 2026-10-05')),
    ('G-FACES-LANDED', 'FACES_LEDGER on disk and at HEAD: its pre-act blob plus the writer`s block', lambda S: landed(S, 'FACES_LEDGER'),
     lambda S: _mut_doc(S, 'FACES_LEDGER', '<!-- b618 (R228)(2)(v) faces update -->', '<!-- x -->')),
    ('G-MAP-LANDED', 'THE_LOAD_BEARING_MAP on disk and at HEAD: its pre-act blob plus the draft', lambda S: landed(S, 'THE_LOAD_BEARING_MAP'),
     lambda S: _mut_doc(S, 'THE_LOAD_BEARING_MAP', '<!-- b618 (R228)(2)(vi) THE MAP BY POINTER, 2026-10-04 -->', '<!-- x -->')),
    ('G-GAUGE-LANDED', 'GAUGE_AND_INVARIANT on disk and at HEAD: its pre-act blob plus the draft', lambda S: landed(S, 'GAUGE_AND_INVARIANT'),
     lambda S: _mut_doc(S, 'GAUGE_AND_INVARIANT', 'nothing was missed', 'nothing missed')),
    ('G-REGISTRY-LANDED', 'REGISTRY on disk and at HEAD: its pre-act blob plus the draft', lambda S: landed(S, 'REGISTRY'),
     lambda S: _mut_doc(S, 'REGISTRY', '| p2-d10 | ', '| p2-d11 | ')),
    ('G-APPENDS-ALONE-IN-ORDER', 'PLACE-papers` log since 138ea0c: each append in one commit of its own, in the order of (R228)(2)', lambda S: alone_in_order(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if 'REGISTRY.md' in f else f) for h, f in S['pp_files'].items()})),
    ('G-LOOM-ROWS-NOW', 'the loom`s rows recomputed now from relay`s suite banks at 6d813af6 and FINDINGS` blame', lambda S: loom_now(S),
     lambda S: _mut_doc(S, 'VERIFICATION_LOOM', '| b617 | 80 of 80 | ', '| b617 | 79 of 80 | ')),
    ('G-MAP-NODES-NOW', 'the map`s 76 nodes against the pages` node lines read now', lambda S: map_now(S),
     lambda S: _mut_doc(S, 'THE_LOAD_BEARING_MAP', '`SIDEExplicitFormula.Schema.Family.family_theorem` | DERIVES', '`SIDEExplicitFormula.Schema.Family.family_theorem` | INTERFACES')),
    ('G-FACES-TIERS-NOW', 'FACES_LEDGER`s six rows against the pages` node lines read now', lambda S: faces_now(S),
     lambda S: _mut_doc(S, 'FACES_LEDGER', 'v0.17 = 5a1630b; the ζ page) | T0 |', 'v0.17 = 5a1630b; the ζ page) | T1 |')),
    ('G-SPINOR-READ', 'REGISTRY`s :731 note against SIDE-spinor`s statements at v0.1.0', lambda S: spinor_ok(S),
     lambda S: _mut_doc(S, 'REGISTRY', '`SIDE-spinor` `v0.1.0` = `b235bc6`', '`SIDE-spinor` `v0.1.0` = `0000000`')),
    ('G-H52A-SCORED', 'H52a recomputed now from the currency bank and the documents at HEAD, against the scores and the desk', lambda S: h52a_ok(S),
     lambda S: _sc(S, 'H52a')),
    ('G-H52B-SCORED', 'H52b recomputed now from REGISTRY on disk and each named file`s version line, against the read-back bank, the scores and the desk',
     lambda S: h52b_ok(S), lambda S: _sc(S, 'H52b')),
    ('G-H52C-SCORED', 'H52c recomputed now from OPEN_TRAILS at HEAD, against the scores and the desk', lambda S: h52c_ok(S), lambda S: _sc(S, 'H52c')),
    ('G-H52D-SCORED', 'H52d: the scanner run afresh on each landed append, against the drafts` banks, the scores and the desk', lambda S: h52d_ok(S),
     lambda S: _sc(S, 'H52d')),
    ('G-CURRENT-UNEDITED', 'README, ERRATA, SPIRAL_MAP and v0.7, the census and the sieve`s current versions, the spine, the six syntheses and the edited bases` current editions, on disk and at HEAD against 138ea0c',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{CURRENTS[0]: (S['currents'][CURRENTS[0]][0] + b'x', S['currents'][CURRENTS[0]][1], S['currents'][CURRENTS[0]][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the appended ledger bytes, the eight appends, its relay banks and tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: a changed page re-emitted and committed, an unchanged one unwritten', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since 138ea0c: a changed page in one commit of its own after the last append`s, an unchanged one in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[PAGE]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the pages: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the answer, the strike items, b619 priced', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'Answered before the seal, by the author' in trail(S) and 'b619 priced' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('b619 priced', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b619, THE_KEYSTONE_CENSUS’s v0.4; then W-ORD-SECOND-READER’s batch; the author rules' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b619, THE_KEYSTONE_CENSUS’s v0.4; then W-ORD-SECOND-READER’s batch; the author rules', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: its main, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-spinor': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b618_record.py'): S['tooltext'].get(os.path.join(T, 'b618_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1]))),
    ('G-LIVING-APPEND-ONLY', 'the eight living documents -- each pre-act blob a true prefix of its file on disk', lambda S: all(
        d['pre'] and d['disk'].startswith(d['pre'] if n != 'FACES_LEDGER' else d['pre'].rstrip(NL)) and len(d['disk']) > len(d['pre'])
        for n, d in S['docs'].items()), lambda S: _mut_doc(S, 'INSTRUMENTS', '## I-1 — ', '## I-0 — ')),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1, outputs and heritage paths, tracked and untracked: the five phase1.5/method living documents alone',
     lambda S: S['keystone_changes'] == sorted(S['REC'].DOC[n] for n in NAMES if S['REC'].DOC[n].startswith('phase')),
     lambda S: put(S, 'keystone_changes', sorted(S['keystone_changes'] + ['phase1.5/method/ENUMERA_v1_6.md']))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 6d813af6, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b617_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        [S['REC'].DOC[n] for n in NAMES] + ['FINDINGS.md', 'OPEN_TRAILS.md'] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-GRADES-DECLARED', 'the regenerated table`s diff against the face`s TABLE CELL lines, both ways', lambda S: S['table_changed'] is not None
     and sorted(tuple(k) for k in S['table_changed']) == sorted(tuple(x.split(' / ')) for x in re.findall(r'TABLE CELL: (\S+ / \S+)', S['face'])),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b618')" in S['suite'] and "data/b618_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b618')", ''))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, read after every other arm has run (OPEN_TRAILS :12703)', lambda S: lsr_ok(S),
     lambda S: put(S, 'lsr', {PP: 2})),
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
    pushed = RERUN or (not PRERUN and is_pushed())
    rec('=' * 104)
    rec('b618 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN:
        rec('### run at (UTC) : %s   ### the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.' % (
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN) else regenerate()
    if RERUN:
        S['table_changed'] = [list(x) for x in (jl('terminal_table_diff.json').get('changed') or [])]
    elif not PRERUN:
        S['table_changed'] = [list(x) for x in (gen_diff.get('changed') or [])] if rc_gen == 0 and 'changed' in gen_diff else None
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
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
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this run, per repository: %s ; at most %d' % (lsr, max(lsr.values()) if lsr else 0))
    if not (RERUN or PRERUN):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b618_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b618_checks_postpush.txt' if pushed else 'b618_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b618_arms_prerun.txt', 'b618_lsr_prerun.json').replace('b618_checks', 'b618_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b618_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
