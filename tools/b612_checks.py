# -*- coding: utf-8 -*-
"""b612_checks.py -- THE SUITE OF b612, UNDER (R222): THE SYNTHESIS FOR CLUSTER 1.5E -- ONE DOCUMENT FROM THE CLUSTER'S SIX PAPERS READ
AT ADDRESS, EVERY CLAIM GRADED BY ITS PAPER'S OWN TEXT, THE ROUTES READ BY THE FIVE TESTS.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b612_checks.txt before the push and
### data/b612_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b612_arms_prerun.txt and nothing else.
### ### The harness is b568's to b611's, carried from tools/b611_checks.py (its imports, helpers, regenerate and main); the
### sources, predicates and arms are b612's. The control arm is the frozen one of (R207)(2). Every positive control mutates a line whose
### text occurs once in its source (b610's defect (b)); an order of two banks is read from their files' mtimes as well as their
### whole-second stamps (b611's defect (a)).
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
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b612_registration_2026-10-03.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
DOC = 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md'
BODY1 = '## 1. The papers and their scope'
CURRENTS = ('phase1.5/deep-structure/CONSTANCE.md', 'phase1.5/deep-structure/FROBENIUS.md', 'phase1.5/deep-structure/TRIVIUM.md',
            'phase1.5/deep-structure/TRIVIUM_FINDINGS.md', 'phase1.5/deep-structure/TRIVIUM_IDENTITY_SUBSPACE.md',
            'phase1.5/deep-structure/CLASS_NUMBER_ANOMALY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md', 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md',
            'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md',
            'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md')
PRE = dict(relay='4c6c371c', pp='a79215a', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf69', 'SIDE-rcurve': 'd5f33b44', 'SIDE-explicit-formula': '1d5d4dd9',
             'SIDE-frobenius': '2efe9f2f', 'SIDE-class-number-anomaly': '2203b88a', 'SIDE-dirichlet-mod-24': '597b0869',
             'SIDE-substrate-cluster': '2e76426d', 'SIDE-bijection': 'a26f6f1c', 'SIDE-trivium': '1aac3a9e', 'SIDE-spinor': '520abe7a'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = '4bfcaa29'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/8f2ff82c-2889-4443-a8e7-85de4d1b215f/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b612')
            and 'data/b612_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b612_record as REC
    import b612_claims as K
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b612_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b612_') and f.endswith('.py'))
    dp = os.path.join(PP, *DOC.split('/'))
    S = dict(
        REC=REC, K=K, face=face, ferry=rd('b612_ferry.txt'), scan=rd('b612_ferry_scan.txt'), cens=rd('b612_census_stepzero.txt'),
        fcens=rd('b612_faces_census_stepzero.txt'), pins0=rd('b612_pins_stepzero.txt'), procs=rd('b612_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b611_closing.txt'), reads=rd('b612_reads.txt'), branches=rd('b612_branches.txt'), answers=rd('b612_author_answers.txt'),
        prerun=rd('b612_arms_prerun.txt'), defects=rd('b612_defects.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b611_checks.py', 'b611_record.py', 'b611_claims.py', 'b604_record.py', 'b602_record.py', 'b560_record.py',
                        'b566_record.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py', 'push_gated.sh',
                        'banned_terms.py', 'b558_record.py', 'errata_append.py', 'terminal_table.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md')), cr0(blob(PP, 'HEAD:ERRATA.md'))),
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in CURRENTS},
        dd_disk=cr0(raw(dp)), dd_head=cr0(blob(PP, 'HEAD:' + DOC)),
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kern_face=(jl('b612_kernels_face.json').get('kernels') or {}), kern_now={k: list(v) for k, v in REC.kern_state().items()},
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b611*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b612_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b612_mustnotexist.txt')), table_changed=None,
        fj=jl('b612_findings.json'), tj=jl('b612_trail.json'), sc=jl('b612_scores.json'), desk=rd('b612_desk_notes.txt'),
        rl=jl('b612_record_lines.json'), CJ=jl('b612_claims.json'), ctxt=rd(REC.BANK),
        DJ=jl('b612_doc.json'), HJ=jl('b612_h46.json'), dbank=rd('b612_doc_bank.txt'), dscan=rd('b612_doc_termscan.txt'),
        PZ=jl('b612_page_zeta.json'), PX=jl('b612_page_chi.json'), arms_c2=rd('b612_page_arms_c2.txt'),
        mt_claims=os.path.getmtime(os.path.join(D, 'b612_claims.json')) if os.path.exists(os.path.join(D, 'b612_claims.json')) else None,
        mt_doc=os.path.getmtime(os.path.join(D, 'b612_doc.json')) if os.path.exists(os.path.join(D, 'b612_doc.json')) else None,
    )
    S['dd'] = lines_of(S['dd_disk']) if S['dd_disk'] else []
    S['dscan_now'] = _scan(dp) if S['dd_disk'] else ''
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['claims_now'] = K.resolve_claims()
    S['kernel_now'] = K.resolve_kernel()
    S['pins_now'] = [K.pin_state(k) for k in K.PINS]
    S['sieve_now'] = K.sieve_rows()
    S['nd_now'] = REC.nodisclosure() if S['dd_disk'] else {}
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
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs'))
    S['pp_changed'] = sorted(ch)
    S['keystone_changes'] = sorted(x for x in ch if x.startswith('phase') or x.startswith('day1/') or x.startswith('outputs/'))
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b612_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b612_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
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


def _rl(S, i):
    ls = S['rl'].get('lines') or []
    return ls[i] if len(ls) == 3 else {}


def weight_ok(S):
    x = _rl(S, 0)
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7240)' in a and 'b611 AT ITS WEIGHT' in a \
        and 'The author confirms the grading rule, the routes’ verdicts and the KC tier' in a and '82 of 82' in a and x['line'] > 7240


def fact_ok(S):
    x = _rl(S, 1)
    a = oline(S, x.get('line'))
    return bool(x) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(x['head']) and '(:12603)' in a and 'MECHANISM_EXCLUSION.md :210' in a \
        and 'MECHANISM_EXCLUSION.md :93 says native_decide' in a and 'H-TT-1 already' in a \
        and all(s in a for s in ('THE_EXCLUSION_ARCHITECTURE.md :542', 'MECHANISM_EXCLUSION.md :408', 'IDS_TO_RH.md :302', 'INTEGRATED_PROOF.md :403')) \
        and x['line'] > 12603


def regrow_ok(S):
    x = _rl(S, 2)
    a = oline(S, x.get('line'))
    return bool(x) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(x['head']) and 'THE_RIEMANN_PATHS_CLUSTER_SPINE.md' in a \
        and 'no REGISTRY row names it' in a and 'on the author’s word; not started' in a


def claims_banked(S):
    CJ, DJ, t = S['CJ'], S['DJ'], S['ctxt']
    order = S['mt_claims'] is not None and S['mt_doc'] is not None and S['mt_claims'] < S['mt_doc']
    return bool(CJ) and bool(DJ) and CJ.get('at', 'z') <= DJ.get('at', '') and order and t.startswith('b612 -- COMPONENT 2') \
        and all(('### PART %s' % p) in t for p in 'ABCDE') and CJ.get('n') == len(S['K'].C) >= 20


def claims_now(S):
    return len(S['claims_now']) == len(S['K'].C) and all(ok for _i, ok, _l in S['claims_now'])


def kernel_now(S):
    return len(S['kernel_now']) == len(S['K'].KREADS) and all(ok for _k, ok, _l in S['kernel_now'])


def pins_now(S):
    return len(S['pins_now']) == len(S['K'].PINS) and all(p[4] and p[3].startswith(S['K'].PINS[p[0]][2][:7]) for p in S['pins_now'])


def grades_ok(S):
    K = S['K']
    cl = S['CJ'].get('claims') or []
    return len(cl) == len(K.C) and all(K.grade_ok(c) for c in K.C) and all(c[0] == x['id'] and c[5] == x['grade'] for c, x in zip(K.C, cl))


def sieve_match(S):
    h, reached, matched, listed = S['REC'].h46d_score(S['sieve_now'])
    return h == S['CJ'].get('h46d') == 'HOLDS' and [list(x) for x in matched] == [list(x) for x in S['CJ'].get('matched') or []] \
        and [list(x) for x in listed] == [list(x) for x in S['CJ'].get('listed') or []]


def unedited_all(S):
    return all(bool(b) and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


def doc_bytes(S):
    return bool(S['dd_disk']) and hashlib.sha256(S['dd_disk']).hexdigest() == S['DJ'].get('sha256')


def doc_rows(S):
    dd, DJ = S['dd'], S['DJ']
    if not dd or not DJ:
        return False
    rows = [l for l in dd if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]
    ids = [l.split(' | ')[0][2:] for l in rows]
    return ids == [c[0] for c in S['K'].C] and all((' | %s :%d | ' % (c[1], c[2])) in l and (' | %s | ' % c[5]) in l for c, l in zip(S['K'].C, rows))


def doc_title(S):
    dd = S['dd']
    return bool(dd) and dd[0] == S['REC'].TITLE and not S['REC'].PROPERTY_WORDS.findall(dd[0])


def doc_tier(S):
    dd = S['dd']
    t = next((l for l in dd[:6] if l.startswith('**DOCUMENT CLASS')), '')
    kv = sum(1 for c in S['K'].C if c[5] == 'kernel-verified')
    ok, _miss = S['REC'].h46c_check(t)
    return ('TIER KC**' in t if kv else 'TIER C**' in t) and ('%d rows read kernel-verified' % kv) in t and ok


def doc_head(S):
    dd = S['dd']
    return bool(dd) and S['REC'].HEADLINE in dd[:10] and S['REC'].VERSION in dd[:10]


def doc_placed(S):
    DJ, dd = S['DJ'], S['dd']
    if not dd or not DJ:
        return False
    ci = dd.index('## Correspondence') + 1 if '## Correspondence' in dd else 10 ** 9
    bi = dd.index(BODY1) + 1 if BODY1 in dd else -1
    return (ci < bi) if DJ.get('tier') == 'KC' else (ci > bi)


def doc_traces(S):
    if not S['dd'] or not S['DJ']:
        return False
    ok, n, bad = S['REC'].h46a(S['dd'], S['DJ'])
    return ok and n == S['HJ'].get('sentences')


def doc_scanner(S):
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['dscan_now'], re.M) is not None
    return clean and S['dscan_now'].strip() == S['dscan'].strip()


def doc_ceiling(S):
    dd, DJ = S['dd'], S['DJ']
    if not dd or not DJ:
        return False
    return not [l for l in dd[:DJ['bm'] - 1] if S['REC'].CEILING.search(l)]


def doc_bm(S):
    dd, REC = S['dd'], S['REC']
    if not dd or REC.BM_TAG not in dd:
        return False
    bm = dd[dd.index(REC.BM_TAG):]
    heads = ['### The grading rule', '### The routes through the five tests', '### The terminals read at their pins', '### Placement', '### Version history']
    pos = [next((i for i, l in enumerate(bm) if l.startswith(h)), -1) for h in heads]
    routes = [l for l in bm if re.match(r'^\| R\d \| ', l)]
    blanks = [l for l in bm if l.startswith('| ') and not l.startswith('|:--') and l.rstrip().endswith('|  |')]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and len(routes) == len(S['CJ'].get('routes') or [0]) and not blanks


def _h(S, k, want):
    return S['HJ'].get(k) == want and (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### ### **%s %s' % (k, want)) in (S['dbank'] + S['ctxt'])


def h46a_ok(S):
    return _h(S, 'H46a', 'HOLDS' if doc_traces(S) else 'REFUTED')


def h46b_ok(S):
    rows = [l for l in S['dd'] if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]
    return _h(S, 'H46b', 'HOLDS' if len(rows) >= 10 and grades_ok(S) and doc_rows(S) else 'REFUTED')


def h46c_ok(S):
    return _h(S, 'H46c', 'HOLDS' if doc_tier(S) else 'REFUTED')


def h46d_ok(S):
    want = 'HOLDS' if sieve_match(S) else 'REFUTED'
    return S['CJ'].get('h46d') == want and (S['sc'].get('H46d') or [''])[0] == want and '(H46D)' in S['desk'] and ('### ### **H46d %s' % want) in S['ctxt']


def _alone(S, path, prefix):
    c = [h for h, f in S['pp_files'].items() if path in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [path] and dict(S['pp_log'])[c[0]].startswith(prefix)


def pages_banked(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        a, b, c = S['pages'][p]
        if z.get('changed') is True:
            out.append(z.get('rc') == 0 and bool(a) and a == c and a != b and hashlib.sha256(c).hexdigest() == z.get('sha256')
                       and ('`%s`' % DOC) in c.decode('utf-8').split('## Placement')[-1])
        else:
            out.append(z.get('rc') == 0 and z.get('changed') is False and bool(a) and a == b == c and hashlib.sha256(c).hexdigest() == z.get('sha256'))
    return all(out)


def pages_alone(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        if z.get('changed') is True:
            out.append(_alone(S, p, 'b612 (R222)(3): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    order = [h for h, _s in S['pp_log']]
    ed = [h for h, f in S['pp_files'].items() if DOC in f]
    pc = [h for h, f in S['pp_files'].items() if PAGE in f or DIR_PAGE in f]
    return all(out) and len(ed) == 1 and all(order.index(h) > order.index(ed[0]) for h in pc)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 26]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The 1.5E synthesis: the {2, 3} substrate and the Trivium') \
        and all(x in tail for x in ('**The document**', '**The routes**', '**The record lines.**', '**The scores.**', '**Read in mutual light**',
                                    'strengthens', '**Next.**', DOC))


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


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


READ_NEEDLES = ('THE_KEYSTONE_CENSUS_v0_3.md @ a79215a4', 'REGISTRY.md @ a79215a4', 'CONSTANCE.md @ a79215a4', 'FROBENIUS.md @ a79215a4',
                'TRIVIUM.md @ a79215a4', 'TRIVIUM_FINDINGS.md @ a79215a4', 'TRIVIUM_IDENTITY_SUBSPACE.md @ a79215a4',
                'CLASS_NUMBER_ANOMALY.md @ a79215a4', 'THE_DOCUMENT_CLASS_TAXONOMY.md @ a79215a4', 'THE_FINDINGS_AS_THEY_STAND_v0_4.md @ a79215a4',
                'OPEN_TRAILS.md @ a79215a4', 'THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md @ a79215a4',
                'SIDEFrobenius/Indicial.lean @ 2efe9f2f', 'SIDEClassNumberAnomaly/Basic.lean @ 2203b88a', 'SIDEDirichletMod24/Basic.lean @ 597b0869',
                'SIDESubstrateCluster/Substrate.lean @ 06b61c3a', 'SIDEBijection/Theorem.lean @ dd487e61', 'SIDEBijection/Theorem.lean @ a26f6f1c',
                'Trivium/Bijection.lean @ 1df5bad4', 'SIDESpinor/Spinor.lean @ b235bc62', 'data/housekeeping_terminal_table.txt @ 4bfcaa29',
                'data/b611_closing_push_out.txt @ 4bfcaa29', '### THE PINS THE PAPERS NAME', ':11864 ', ':12228 ', ':12566 ', ':12601 ', ':12603 ',
                ':187 ', ':191 ', ':196 ', ':57 ', ':564 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R222) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b611`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b611' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b612 -- x'])),
    ('G-R222-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R222) END' in S['ferry'] and S['ot'].count('**(R222) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R222) ratified', '(R222) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads']
     and 'NOT AT THE REMOTE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: no prompt put, said so', lambda S: S['answers'].startswith('### b612 -- THE AUTHOR`S ANSWERS, 0 prompt(s)')
     and '### NONE: no prompt was put to the author in this act' in S['answers'], lambda S: put(S, 'answers', S['answers'].replace('0 prompt(s)', '1 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 4bfcaa29`s files', lambda S: S['pushout'][0] == ['data/b611_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b611_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b611') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b611'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b611`s suite, record tool and claims module, the shared record tools and appender, the control`s test file, the generator, its arm, the E0 rule, the push gate, the scanner, the sentence counter, the ERRATA id appender and the table generator against 4c6c371c',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 16,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b558_record.py': (S['inst']['b558_record.py'][0], (S['inst']['b558_record.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b611`s weight and the three confirmations', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('The author confirms the grading rule, the routes’ verdicts and the KC tier', 'The author notes the rule'))),
    ('G-FACT-LINE', 'OPEN_TRAILS at the banked line: the three fact items by path and line', lambda S: fact_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('H-TT-1 already (relay', 'H-TT-1 (relay'))),
    ('G-REGROW-LINE', 'OPEN_TRAILS at the banked line: the REGISTRY row-addition item for the author`s word', lambda S: regrow_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('on the author’s word; not started', 'when convenient'))),
    ('G-CLAIMS-BANKED', 'the claim bank and its json: banked before the document (stamps and mtimes), its five parts', lambda S: claims_banked(S),
     lambda S: put(S, 'CJ', dict(S['CJ'], at='9999'))),
    ('G-CLAIMS-RESOLVE-NOW', 'every claim`s needle re-read now on its line at a79215a', lambda S: claims_now(S),
     lambda S: put(S, 'claims_now', [(S['claims_now'][0][0], False, '')] + S['claims_now'][1:])),
    ('G-KERNEL-READS-NOW', 'every kernel read re-read now at its pin', lambda S: kernel_now(S),
     lambda S: put(S, 'kernel_now', [(S['kernel_now'][0][0], False, '')] + S['kernel_now'][1:])),
    ('G-PINS-RESOLVE-NOW', 'every pin the papers name re-resolved now in its clone and at its remote', lambda S: pins_now(S),
     lambda S: put(S, 'pins_now', [S['pins_now'][0][:4] + (None,)] + S['pins_now'][1:])),
    ('G-GRADES-IN-RULE', 'every claim`s grade within its paper`s named backing, as banked', lambda S: grades_ok(S),
     lambda S: put(S, 'CJ', dict(S['CJ'], claims=[dict(S['CJ']['claims'][0], grade='theorem-supported')] + S['CJ']['claims'][1:]) if S['CJ'].get('claims') else S['CJ'])),
    ('G-SIEVE-MATCH-NOW', 'the sieve v0.4 re-read now: the routes` verdicts where it has a row, the rest listed, as banked', lambda S: sieve_match(S),
     lambda S: put(S, 'sieve_now', dict(S['sieve_now'], **{'RH-60': ('BRIGHT', '—')}))),
    ('G-CURRENT-UNEDITED', 'the six papers, the census v0.3, SPIRAL_MAP v0.6 and v0.7, the taxonomy, b611`s document and the sieve on disk and at HEAD against a79215a',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{CURRENTS[0]: (S['currents'][CURRENTS[0]][0] + b'x', S['currents'][CURRENTS[0]][1], S['currents'][CURRENTS[0]][2])}))),
    ('G-DOC-BYTES', 'the document on disk at its banked sha', lambda S: doc_bytes(S), lambda S: put(S, 'dd_disk', (S['dd_disk'] or b'') + b'x')),
    ('G-DOC-ROWS', 'the document`s Correspondence: one row per banked claim, in order, at its line and grade', lambda S: doc_rows(S),
     lambda S: put(S, 'dd', [l.replace('| FR-02 | FR :32 |', '| FR-02 | FR :33 |') for l in S['dd']])),
    ('G-DOC-TITLE', 'the document`s title: its objects, no property word', lambda S: doc_title(S), lambda S: put(S, 'dd', ['# The complete ' + S['dd'][0][2:]] + S['dd'][1:])),
    ('G-DOC-TIER-LINE', 'the tier line against the rows: KC with every certifying terminal named at a resolving pin', lambda S: doc_tier(S),
     lambda S: put(S, 'dd', [l.replace('TIER KC**', 'TIER K**') for l in S['dd']])),
    ('G-DOC-HEAD', 'the head line and the version line', lambda S: doc_head(S), lambda S: put(S, 'dd', [l.replace('certifies nothing they do not', 'certifies') for l in S['dd']])),
    ('G-DOC-PLACEMENT', 'the Correspondence placed by (R221)(3) for the tier', lambda S: doc_placed(S),
     lambda S: put(S, 'DJ', dict(S['DJ'], tier='C'))),
    ('G-DOC-TRACES', 'every body sentence re-read now for its trace into the bank', lambda S: doc_traces(S),
     lambda S: put(S, 'dd', [l.replace(' (FR :32).', '.') for l in S['dd']])),
    ('G-DOC-SCANNER', 'the scanner run afresh on the document at PLACE-papers HEAD', lambda S: doc_scanner(S),
     lambda S: put(S, 'dscan_now', S['dscan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-DOC-CEILING', 'the ceiling pattern over the document above its back matter', lambda S: doc_ceiling(S),
     lambda S: put(S, 'dd', [S['dd'][0] + ' the proof'] + S['dd'][1:])),
    ('G-DOC-NODISCLOSURE', 'the no-disclosure arm re-run now: TECHNE-Core module sentences found in the document', lambda S: S['nd_now'].get('hits') == 0
     and S['nd_now'].get('needles', 0) > 100 and S['HJ'].get('nodisclosure', {}).get('hits') == 0, lambda S: put(S, 'nd_now', dict(S['nd_now'], hits=1))),
    ('G-DOC-BACKMATTER', 'the document`s back matter: its sections in order, one route row per route, no blank cell', lambda S: doc_bm(S),
     lambda S: put(S, 'dd', [l.replace('### The routes through the five tests', '### Routes') for l in S['dd']])),
    ('G-H46A-SCORED', 'H46a recomputed from the document, the scores and the desk', lambda S: h46a_ok(S), lambda S: _sc(S, 'H46a')),
    ('G-H46B-SCORED', 'H46b recomputed from the document and the grading rule', lambda S: h46b_ok(S), lambda S: _sc(S, 'H46b')),
    ('G-H46C-SCORED', 'H46c recomputed from the tier line and the pins', lambda S: h46c_ok(S), lambda S: _sc(S, 'H46c')),
    ('G-H46D-SCORED', 'H46d recomputed from the sieve now', lambda S: h46d_ok(S), lambda S: _sc(S, 'H46d')),
    ('G-DOC-COMMITTED-ALONE', 'PLACE-papers` log since a79215a: the document in one commit of its own, on disk as committed', lambda S: _alone(S, DOC, 'b612 (R222)(3): ' + DOC)
     and bool(S['dd_head']) and S['dd_head'] == S['dd_disk'], lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if DOC in f else f) for h, f in S['pp_files'].items()})),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: a changed page re-emitted with the document in its Placement, an unchanged one unwritten', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since a79215a: a changed page in one commit of its own after the document`s, an unchanged one in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[DIR_PAGE]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the pages: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S) and 'For the author:' in trail(S)
     and 'b613 priced' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b613, the synthesis act for 2B' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('b613, the synthesis act for 2B', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the cluster kernels` mains, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-frobenius': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b612_record.py'): S['tooltext'].get(os.path.join(T, 'b612_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md on disk and at HEAD against a79215a', lambda S: bool(S['errata'][1]) and S['errata'][0] == S['errata'][1] == S['errata'][2],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1], S['errata'][2]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked: the document alone', lambda S: S['keystone_changes'] == [DOC],
     lambda S: put(S, 'keystone_changes', sorted([DOC, CURRENTS[0]]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 4c6c371c, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b611_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['FINDINGS.md', 'OPEN_TRAILS.md', DOC] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
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
                                                                          and "startswith('b612')" in S['suite'] and "data/b612_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b612')", ''))),
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
    rec('b612 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN:
        rec('### run at (UTC) : %s   ### the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
            % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
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
        out = os.path.join(D, 'b612_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b612_checks_postpush.txt' if pushed else 'b612_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b612_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
