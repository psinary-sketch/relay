# -*- coding: utf-8 -*-
"""b617_checks.py -- THE SUITE OF b617, UNDER (R227): THE SIEVE AT v0.5 -- THE TEN CONCLUSIONS GATHERED FROM THE SIX SYNTHESES AS ROWS;
THE 2G PAPERS' FINDINGS AND THREE ERRATA; THE LIVING DOCUMENTS' CURRENCY ENTERED FOR b618.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b617_checks.txt before the push and data/b617_checks_postpush.txt
### after it. `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is sealed, no table regenerated, its
### counts written to data/b617_arms_prerun.txt. ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs),
### each run's ls-remote calls banked per repository beside its output (data/b617_lsr*.json); G-LSREMOTE-ONE-PER-REPO runs last.
### ### The harness is b568's to b616's, carried from tools/b616_checks.py (its imports, helpers, regenerate and main); the sources,
### predicates and arms are b617's. The control arm is the frozen one of (R207)(2). Every positive control mutates a line whose text occurs
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
FACE = os.path.join(D, 'b617_registration_2026-10-04.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
SV4 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'
SV5 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md'
PRE = dict(relay='365bc07e', pp='52962da', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-explicit-formula': '1d5d4dd9', 'SIDE-global-section': '3528bcfc'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = '9d80f449'
ERR_IDS = ('E-2026-10-04-5', 'E-2026-10-04-6', 'E-2026-10-04-7')
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/4430dadd-ebc7-4bca-a2e4-2aa8752aee4f/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b617')
            and 'data/b617_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def _scan(path):
    return subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', path], capture_output=True, text=True,
                          encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout


def sources():
    import b617_record as REC
    import b617_worklist as K
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b617_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b617_') and f.endswith('.py'))
    ep = os.path.join(PP, *SV5.split('/'))
    S = dict(
        REC=REC, K=K, face=face, ferry=rd('b617_ferry.txt'), scan=rd('b617_ferry_scan.txt'), cens=rd('b617_census_stepzero.txt'),
        fcens=rd('b617_faces_census_stepzero.txt'), pins0=rd('b617_pins_stepzero.txt'), procs=rd('b617_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b616_closing.txt'), reads=rd('b617_reads.txt'), branches=rd('b617_branches.txt'), answers=rd('b617_author_answers.txt'),
        prerun=rd('b617_arms_prerun.txt'), defects=rd('b617_defects.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b616_checks.py', 'b616_record.py', 'b616_claims.py', 'b609_record.py', 'b609_worklist.py', 'b604_record.py',
                        'b602_record.py', 'b560_record.py', 'b566_record.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py',
                        'g_chain_page.py', 'push_gated.sh', 'banned_terms.py', 'b558_record.py', 'terminal_table.py', 'errata_append.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in REC.CURRENTS},
        ed_disk=cr0(raw(ep)), ed_head=cr0(blob(PP, 'HEAD:' + SV5)),
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        er_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')), er_now=cr0(raw(os.path.join(PP, 'ERRATA.md'))), er_head=cr0(blob(PP, 'HEAD:ERRATA.md')),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kern_face=(jl('b617_kernels_face.json').get('kernels') or {}), kern_now={k: list(v) for k, v in REC.kern_state().items()},
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b616*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b617_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b617_mustnotexist.txt')), table_changed=None,
        fj=jl('b617_findings.json'), tj=jl('b617_trail.json'), sc=jl('b617_scores.json'), desk=rd('b617_desk_notes.txt'),
        rl=jl('b617_record_lines.json'), AJ=jl('b617_arith.json'), atxt=rd('b617_arith.txt'), CU=jl('b617_currency.json'),
        ctxt=rd('b617_currency.txt'), ERJ=jl('b617_errata.json'), RJ=jl('b617_rows.json'), rtxt=rd('b617_rows.txt'),
        EJ=jl('b617_sieve_edition.json'), H=jl('b617_h51.json'), ebank=rd('b617_edition_FINDINGS_STAND.txt'), escan=rd('b617_sieve_termscan.txt'),
        repin=rd('b617_repin_sieve.txt'), PZ=jl('b617_page_zeta.json'), PX=jl('b617_page_chi.json'), arms_c2=rd('b617_page_arms_c2.txt'),
        mt_rows=os.path.getmtime(os.path.join(D, 'b617_rows.json')) if os.path.exists(os.path.join(D, 'b617_rows.json')) else None,
        mt_ed=os.path.getmtime(os.path.join(D, 'b617_sieve_edition.json')) if os.path.exists(os.path.join(D, 'b617_sieve_edition.json')) else None,
        lsr=None,
    )
    S['ed'] = lines_of(S['ed_disk']) if S['ed_disk'] else []
    S['escan_now'] = _scan(ep) if S['ed_disk'] else ''
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['ins_now'] = K.resolve_instruments()
    S['src_now'] = K.resolve_sources()
    S['S4'], S['sieve_bad'] = K.resolve_sieve()
    S['nd_sets'] = R6.nd_sets()
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now']), ('ERRATA', S['er_pre'], S['er_now'])):
        pub.append((now or b'')[len(pre or b''):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    if S['ed_disk']:
        pub.append(S['ed_disk'].decode('utf-8', 'replace'))
    for f in sorted(os.listdir(D)):
        if f.startswith(('b617_', 'audit_b617_')):
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
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b617_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b617_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    return X


# ### the act's own predicates
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


def _rl(S, role):
    ls = S['rl'].get('lines') or []
    return dict(zip(('fact', 'currency', 'weight'), ls)).get(role, {}) if len(ls) == 3 else {}


def weight_ok(S):
    x, f, c = _rl(S, 'weight'), _rl(S, 'fact'), _rl(S, 'currency')
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7346)' in a and 'b616 AT ITS WEIGHT' in a \
        and '90 of 90 pre-push and 90 of 90 post-push, a kept run at 89 of 90' in a and 'matching RH-60' in a and 'the ten conclusion groupings' in a \
        and ('findings at OPEN_TRAILS :%d' % f.get('line', 0)) in a and ('b618, at :%d' % c.get('line', 0)) in a and x['line'] > 7364


def fact_ok(S):
    x = _rl(S, 'fact')
    a = oline(S, x.get('line'))
    return bool(x) and a.startswith(x['head']) and '(:12733)' in a and all(('(%s)' % r) in a for r in ('i', 'ii', 'iii', 'iv', 'v', 'vi')) \
        and 'sums to 279 constants with 14 not P-smooth' in a and 'domain rows sum to 348' in a and 'over the bins is −0.644' in a \
        and 'K₇ has 6 once and −1 six times' in a and 'has order 24' in a and 'keeps 0.750 of the norm' in a and 'relay data/b617_arith.txt' in a \
        and all(i in a for i in ERR_IDS) and x['line'] > 12751


def currency_ok(S):
    x = _rl(S, 'currency')
    a = oline(S, x.get('line'))
    CU = (S['CU'].get('docs') or {})
    return bool(x) and bool(CU) and a.startswith(x['head']) and '(:12731)' in a and 'relay data/b617_currency.txt' in a and 'not 2026-09-08' in a \
        and all(('%s (' % n) in a and ('last %s %s' % (CU[n]['last'], CU[n]['last_date'])) in a for n in CU) and 'no document retired, none created' in a \
        and ('%d acts since b537' % CU['VERIFICATION_LOOM']['items']['acts']) in a and x['line'] > 12751


def arith_ok(S):
    A, t = S['AJ'], S['atxt']
    sf, th, fa, gl, st = (A.get(k) or {} for k in ('sf', 'th', 'fano', 'gl32', 'steane'))
    return bool(A) and (sf.get('constants'), sf.get('not_psmooth')) == (279, 14) and round(sf.get('spearman', 0), 3) == -0.644 \
        and round(sf.get('pearson', 0), 2) == -0.66 and th.get('theories') == 348 and round(th.get('weighted', 0), 3) == 0.922 \
        and fa.get('K7') == [-1.0] * 6 + [6.0] and (fa.get('mod_N') or [0])[0] == 3.0 and (fa.get('mod_N') or [])[1:] == [1.4142] * 6 \
        and (gl.get('stabilizer'), gl.get('orbits')) == (24, [6, 1]) and st.get('norm') == 0.75 and t.count('THE FACT OF RECORD') == 6


def currency_banked(S):
    CU, t = S['CU'].get('docs') or {}, S['ctxt']
    names = [n for n, _p, _nd in S['REC'].LIVING]
    return sorted(CU) == sorted(names) and all(CU[n].get('function_line', 0) > 0 and 'price' in CU[n] for n in names) \
        and all(x['ok'] for x in CU['INSTRUMENTS']['items']['located']) and CU['REGISTRY']['items']['control'][0] > 0 \
        and '### ### **THE PRICES:' in t and t.count('### THE PRICE: ') == 8


def errata_ok(S):
    E = S['ERJ'].get('entries') or []
    t = cr0(S['er_now']).decode('utf-8', 'replace')
    ls = t.split(NL)
    fa = _rl(S, 'fact').get('line', -1)
    if [e['id'] for e in E] != list(ERR_IDS) or not S['er_pre'] or not S['er_now'].startswith(S['er_pre']):
        return False
    out = []
    for k, e in enumerate(E):
        if not (0 < e['line'] <= len(ls)) or not ls[e['line'] - 1].startswith('## %s — ' % e['id']):
            return False
        end = E[k + 1]['line'] - 1 if k + 1 < len(E) else len(ls)
        blk = NL.join(ls[e['line'] - 1:end])
        out.append(all(x in blk for x in ('**Filed 2026-10-04 by b617', '**What the lines say.**', '**What is true.**', '**The correction.**',
                                          '**Scope.**', '**Status.** FILED.', '(OPEN_TRAILS :%d)' % fa, 'relay `data/b617_arith.txt`')))
    return all(out) and len(out) == 3


def _alone(S, path, prefix):
    c = [h for h, f in S['pp_files'].items() if path in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [path] and dict(S['pp_log'])[c[0]].startswith(prefix)


def rows_banked(S):
    RJ, EJ, t = S['RJ'], S['EJ'], S['rtxt']
    order = S['mt_rows'] is not None and S['mt_ed'] is not None and S['mt_rows'] <= S['mt_ed'] and RJ.get('at', 'z') <= EJ.get('at', '')
    return bool(RJ) and bool(EJ) and order and t.startswith('b617 -- COMPONENT 2') and all(('### PART %s' % p) in t for p in 'ABC') \
        and len(RJ.get('rows') or []) == 10 and RJ.get('H51a') in ('HOLDS', 'REFUTED') and RJ.get('H51b') in ('HOLDS', 'REFUTED')


def rows_now(S):
    return len(S['ins_now']) == 8 and len(S['src_now']) == 14 and all(x['ok'] for x in S['ins_now']) and all(x['ok'] for x in S['src_now']) \
        and S['sieve_bad'] == []


def _h51_now(S):
    REC = S['REC']
    body = S['S4'][:S['S4'].index(REC.R4.BM_TAG)]
    return REC._h51(S['K'].rows_of(body), S['ins_now'], S['src_now'])


def _h(S, k, want, bank):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### ### **%s %s' % (k, want)) in bank


def h51a_ok(S):
    a, _b, _d, _t = _h51_now(S)
    return S['RJ'].get('H51a') == a and _h(S, 'H51a', a, S['rtxt'])


def h51b_ok(S):
    _a, b, _d, t = _h51_now(S)
    return S['RJ'].get('H51b') == b and (S['RJ'].get('tests') or {}).get('t2') == t['t2'] and _h(S, 'H51b', b, S['rtxt'])


def sieve4_now(S):
    S4 = S['S4']
    body = S4[:S4.index(S['REC'].R4.BM_TAG)]
    rows = S['K'].rows_of(body)
    r60 = [x for x in rows if x[0] == 'RH-60']
    return len(rows) == 87 and bool(r60) and r60[0][2] == 'DARK' and r60[0][3] == S['K'].RH60_TEST


def unedited_all(S):
    return all(bool(b) and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def ed_bytes(S):
    return bool(S['ed_disk']) and hashlib.sha256(S['ed_disk']).hexdigest() == S['EJ'].get('sha256')


def ed_carries(S):
    if not S['ed'] or not S['EJ']:
        return False
    ok, bad = S['REC'].sieve_carried(S['EJ'], S['ed'], S['S4'])
    return bad == [] and ok == S['H'].get('carried_ok') and ok > 1000


def ed_rows(S):
    ed, P, K = S['ed'], (S['EJ'].get('pos') or {}).get('rows') or {}, S['K']
    if not ed or not P:
        return False
    ids = ['RH-%02d' % n for n in range(60, 71)]
    return all(ed[P[r['id']] - 1] == K.row_line(r) for r in K.NEW_ROWS) and [P.get(i) for i in ids] == list(range(P.get('RH-60', 0), P.get('RH-60', 0) + 11))


def ed_head(S):
    ed, REC, K = S['ed'], S['REC'], S['K']
    if not ed or REC.R4.BM_TAG not in ed:
        return False
    rows = K.rows_of(ed[:ed.index(REC.R4.BM_TAG)])
    c = {v: sum(1 for x in rows if x[2] == v) for v in ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE')}
    cl = [x for x in rows if x[0].startswith('RH-')]
    cc = {v: sum(1 for x in cl if x[2] == v) for v in ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE')}
    head = next((l for l in ed if l.startswith('**The verdicts at this edition:**')), '')
    clu = next((l for l in ed if l.startswith('## Simplicity / RH cascade')), '')
    return ('%d rows -- %d BRIGHT, %d DARK, %d NOT A ROUTE, and %d FACE rows' % (len(rows), c['BRIGHT'], c['DARK'], c['NOT A ROUTE'], c['FACE'])) in head \
        and ('— %d rows: %d FACE, %d BRIGHT, %d DARK, %d NOT A ROUTE' % (len(cl), cc['FACE'], cc['BRIGHT'], cc['DARK'], cc['NOT A ROUTE'])) in clu \
        and ('the table’s %d rows' % len(rows)) in NL.join(ed[:60]) and c == S['H'].get('c5')


def ed_scanner(S):
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['escan_now'], re.M) is not None
    return clean and S['escan_now'].strip() == S['escan'].strip()


def ed_ceiling(S):
    ed = S['ed']
    if not ed:
        return False
    body, _bm = S['REC'].R4._body_and_bm(ed)
    return not [l for _i, l in body if S['REC'].CEILING.search(l)] and bool(body)


def repin_ok(S):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', S['repin'])
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > 300 and S['EJ'].get('sha256', 'x') in S['ebank']


def h28_now(S):
    ed, REC = S['ed'], S['REC']
    if not ed or not S['EJ']:
        return None
    b5, _x = REC.R4._body_and_bm(ed)
    b4, _y = REC.R4._body_and_bm(S['S4'])
    dn = REC._count([l for _i, l in b5]) - REC._count([l for _i, l in b4])
    return dn


def h28_ok(S):
    H, E = S['H'], S['EJ']
    dn = h28_now(S)
    return dn is not None and dn == H.get('body_dn') and abs(dn) <= H.get('allowed', -1) and (H.get('H28a'), H.get('H28b'), H.get('H28c')) == (
        'HOLDS', 'HOLDS', 'HOLDS') and all(('### ### **%s HOLDS' % k) in S['ebank'] for k in ('H28a', 'H28b', 'H28c')) and E.get('n_body', 0) - E.get('n_v4_body', 0) == dn


def h51c_ok(S):
    want = 'HOLDS' if h28_ok(S) and ed_scanner(S) and ed_ceiling(S) else 'REFUTED'
    return S['H'].get('H51c') == want and _h(S, 'H51c', want, S['ebank'])


def pages_banked(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        a, b, c = S['pages'][p]
        if z.get('changed') is True:
            out.append(z.get('rc') == 0 and bool(a) and a == c and a != b and hashlib.sha256(c).hexdigest() == z.get('sha256')
                       and ('`%s`' % SV5) in c.decode('utf-8').split('## Placement')[-1])
        else:
            out.append(z.get('rc') == 0 and z.get('changed') is False and bool(a) and a == b == c and hashlib.sha256(c).hexdigest() == z.get('sha256'))
    return all(out)


def pages_alone(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        if z.get('changed') is True:
            out.append(_alone(S, p, 'b617 (R227)(4): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    order = [h for h, _s in S['pp_log']]
    ed = [h for h, f in S['pp_files'].items() if SV5 in f]
    pc = [h for h, f in S['pp_files'].items() if PAGE in f or DIR_PAGE in f]
    return all(out) and len(ed) == 1 and all(order.index(h) > order.index(ed[0]) for h in pc)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The sieve at v0.5: ten conclusions from the six syntheses as rows') \
        and all(x in tail for x in ('**The edition**', '**The record lines.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**',
                                    SV5, 'data/b616_routes_for_sieve.txt'))


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


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


READ_NEEDLES = ('data/b616_routes_for_sieve.txt @ 365bc07e', 'THE_FINDINGS_AS_THEY_STAND_v0_4.md @ 52962dac (1083 lines cited, of 1273)',
                'THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md @ 52962dac', 'THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md @ 52962dac',
                'THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md @ 52962dac', 'Schema/Detector.lean @ c404e727', 'Schema/Epstein.lean @ c404e727',
                'INVARIANCE_BARRIERS_v1_4.md @ 1d0109f3', 'ERRATA.md @ 52962dac', 'VERIFICATION_LOOM.md @ 52962dac', 'INSTRUMENTS.md @ 52962dac',
                'THE_METHOD_CANON.md @ 52962dac', 'THE_METHOD_AS_IT_STANDS.md @ 52962dac', 'FACES_LEDGER.md @ 52962dac',
                'THE_LOAD_BEARING_MAP.md @ 52962dac', 'GAUGE_AND_INVARIANT.md @ 52962dac', 'REGISTRY.md @ 52962dac', 'OPEN_TRAILS.md @ 52962dac',
                'FINDINGS.md @ 52962dac', 'data/b616_closing_push_out.txt @ 9d80f449', '### b616 AT ITS WEIGHT', '### THE LIVING DOCUMENTS` LAST COMMITS',
                ':11864 ', ':12228 ', ':12566 ', ':12727 ', ':12731 ', ':12733 ', ':7346 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R227) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b616`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b616' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b617 -- x'])),
    ('G-R227-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R227) END' in S['ferry'] and S['ot'].count('**(R227) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R227) ratified', '(R227) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: no prompt put, said in one line', lambda S: S['answers'].startswith(
        '### b617 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, 0 prompt(s)') and '### NONE: no prompt was put to the author in this act' in S['answers'],
     lambda S: put(S, 'answers', S['answers'].replace('0 prompt(s)', '1 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 9d80f449`s files', lambda S: S['pushout'][0] == ['data/b616_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b616_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b616') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b616'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b616`s suite, record tool and claims module, b609`s record tool and worklist, the shared record tools, the control`s test file, the generator, its arm, the E0 rule, the push gate, the scanner, the sentence counter, the table generator and the errata appender against 365bc07e',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 18,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b558_record.py': (S['inst']['b558_record.py'][0], (S['inst']['b558_record.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b616`s weight, its confirmations and the two trail lines addressed', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('the ten conclusion groupings', 'x'))),
    ('G-FACT-LINE', 'OPEN_TRAILS at the banked line: the 2G fact items by path and line, the three errata named, the computations named', lambda S: fact_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('K₇ has 6 once and −1 six times', 'x'))),
    ('G-CURRENCY-LINE', 'OPEN_TRAILS at the banked line: b618 entered before the census`s v0.4, each living document`s function line, last commit and price',
     lambda S: currency_ok(S), lambda S: put(S, 'ot', S['ot'].replace('no document retired, none created', 'x'))),
    ('G-ARITH-BANKED', 'the arithmetic bank and its json: the bins, the domain counts and mean, the two correlations, the spectra, the stabilizer, the norm',
     lambda S: arith_ok(S), lambda S: put(S, 'AJ', dict(S['AJ'], th=dict(S['AJ'].get('th') or {}, theories=375)))),
    ('G-CURRENCY-BANKED', 'the currency bank and its json: eight documents, each function line and price, every located item located, the REGISTRY control',
     lambda S: currency_banked(S), lambda S: put(S, 'ctxt', S['ctxt'].replace('### THE PRICE: ', '### PRICE: ', 1))),
    ('G-ERRATA-APPENDED', 'ERRATA at the banked lines: the three entries in form, each addressed to the fact items` line, the pre-act blob a prefix',
     lambda S: errata_ok(S), lambda S: put(S, 'ERJ', dict(S['ERJ'], entries=list(reversed(S['ERJ'].get('entries') or []))))),
    ('G-ERRATA-COMMITTED-ALONE', 'PLACE-papers` log since 52962da: ERRATA in one commit of its own, on disk as committed',
     lambda S: _alone(S, 'ERRATA.md', 'b617 (R227)(2): ERRATA') and bool(S['er_head']) and S['er_head'] == S['er_now'],
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if 'ERRATA.md' in f else f) for h, f in S['pp_files'].items()})),
    ('G-ROWS-BANKED', 'the rows bank and its json: banked before the edition (stamps and mtimes), its three parts, ten rows',
     lambda S: rows_banked(S), lambda S: put(S, 'RJ', dict(S['RJ'], at='9999'))),
    ('G-ROWS-RESOLVE-NOW', 'every instrument line and every source route row re-read now at its pin, and the sieve data`s own checks',
     lambda S: rows_now(S), lambda S: put(S, 'src_now', [dict(S['src_now'][0], ok=False)] + S['src_now'][1:])),
    ('G-SIEVE-V04-NOW', 'the sieve v0.4 re-read now at 52962da: 87 rows, RH-60 DARK at test 2`s instrument', lambda S: sieve4_now(S),
     lambda S: put(S, 'S4', [l.replace('| RH-60 | ', '| RH-6O | ') for l in S['S4']])),
    ('G-H51A-SCORED', 'H51a recomputed now from the rows, the instruments and the sources, against the bank, the scores and the desk', lambda S: h51a_ok(S),
     lambda S: _sc(S, 'H51a')),
    ('G-H51B-SCORED', 'H51b recomputed now from the rows` verdicts and tests, against the bank, the scores and the desk', lambda S: h51b_ok(S),
     lambda S: _sc(S, 'H51b')),
    ('G-EDITION-BYTES', 'the edition on disk at its banked sha', lambda S: ed_bytes(S), lambda S: put(S, 'ed_disk', (S['ed_disk'] or b'') + b'x')),
    ('G-EDITION-CARRIES', 'every non-blank v0.4 line re-read now in the edition: carried, rewritten with its fragments recorded, or re-pinned',
     lambda S: ed_carries(S), lambda S: put(S, 'ed', [l.replace('| MT-07 | ', '| MT-07 |  ') for l in S['ed']])),
    ('G-EDITION-ROWS', 'the ten rows at their banked lines, after RH-60, in order', lambda S: ed_rows(S),
     lambda S: put(S, 'ed', [l.replace('the step stated without an argument.', 'the step stated.') for l in S['ed']])),
    ('G-EDITION-HEAD', 'the head`s counts and the cluster`s heading recomputed now from the edition`s rows', lambda S: ed_head(S),
     lambda S: put(S, 'ed', [l.replace('97 rows -- 2 BRIGHT, 16 DARK', '97 rows -- 2 BRIGHT, 15 DARK') for l in S['ed']])),
    ('G-EDITION-SCANNER', 'the scanner run afresh on the edition at PLACE-papers HEAD', lambda S: ed_scanner(S),
     lambda S: put(S, 'escan_now', S['escan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-EDITION-CEILING', 'the ceiling pattern over the edition`s body', lambda S: ed_ceiling(S),
     lambda S: put(S, 'ed', [l.replace('a statistic over finitely many ordinates.', 'a proof over finitely many ordinates.') for l in S['ed']])),
    ('G-REPIN-HOLDS', 'the re-pin bank: every citation holding against the final file, the diff bank naming its sha', lambda S: repin_ok(S),
     lambda S: put(S, 'repin', S['repin'].replace('citations hold', 'citations held'))),
    ('G-H28-SCORED', 'H28a-H28c from the diff bank, the body count recomputed now', lambda S: h28_ok(S),
     lambda S: put(S, 'H', dict(S['H'], body_dn=(S['H'].get('body_dn') or 0) + 1))),
    ('G-H51C-SCORED', 'H51c recomputed now from H28a-H28c, the scanner and the ceiling, against the bank, the scores and the desk', lambda S: h51c_ok(S),
     lambda S: _sc(S, 'H51c')),
    ('G-EDITION-COMMITTED-ALONE', 'PLACE-papers` log since 52962da: the edition in one commit of its own, on disk as committed',
     lambda S: _alone(S, SV5, 'b617 (R227)(4): ' + SV5) and bool(S['ed_head']) and S['ed_head'] == S['ed_disk'],
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if SV5 in f else f) for h, f in S['pp_files'].items()})),
    ('G-CURRENT-UNEDITED', 'the sieve`s earlier versions, the six syntheses, the 2G papers, the living documents, README, the census and SPIRAL_MAP on disk and at HEAD against 52962da',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{S['REC'].CURRENTS[0]: (S['currents'][S['REC'].CURRENTS[0]][0] + b'x', S['currents'][S['REC'].CURRENTS[0]][1], S['currents'][S['REC'].CURRENTS[0]][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the appended ledger and ERRATA bytes, the edition, its relay banks and tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: a changed page re-emitted with the edition in its Placement, an unchanged one unwritten', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since 52962da: a changed page in one commit of its own after the edition`s, an unchanged one in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[DIR_PAGE]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the pages: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items, the author`s items, b618 priced', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'For the author:' in trail(S) and 'b618 priced' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b618, the living documents’ currency; then the census’s v0.4' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b618, the living documents’ currency; then the census’s v0.4', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: its main, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b617_record.py'): S['tooltext'].get(os.path.join(T, 'b617_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1, outputs and heritage paths, tracked and untracked: the edition alone',
     lambda S: S['keystone_changes'] == [SV5], lambda S: put(S, 'keystone_changes', sorted([SV5, SV4]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 365bc07e, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b616_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', SV5] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-ERRATA-APPEND-ONLY', 'ERRATA -- its pre-act blob a true prefix', lambda S: S['er_pre'] and S['er_now'] is not None
     and S['er_now'].startswith(S['er_pre']) and len(S['er_now']) > len(S['er_pre']), lambda S: put(S, 'er_now', b'x' + (S['er_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
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
                                                                          and "startswith('b617')" in S['suite'] and "data/b617_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b617')", ''))),
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
    rec('b617 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN:
        rec('### run at (UTC) : %s   ### the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.' % (
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN) else regenerate()
    if RERUN:
        S['table_changed'] = []
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
        out = os.path.join(D, 'b617_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b617_checks_postpush.txt' if pushed else 'b617_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b617_arms_prerun.txt', 'b617_lsr_prerun.json').replace('b617_checks', 'b617_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b617_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
